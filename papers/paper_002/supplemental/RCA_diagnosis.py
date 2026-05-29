"""
RCA DIAGNOSIS: Identify root cause of discrepancies
====================================================
Key question: Which density matrix model produces the manuscript's numbers?
   Model A (manuscript text):  rho = mu*|Phi-><Phi-| + (1-mu)*I/4
   Model B (existing code):    rho = mu*|Phi-><Phi-| + (1-mu)/2*(|HV><HV| + |VH><VH|)
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import numpy as np

# === Density matrices ===
def rho_modelA(mu):
    """Manuscript text: rho = mu|Phi-><Phi-| + (1-mu)*I/4"""
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    return mu * np.outer(phi_minus, phi_minus.conj()) + (1-mu)/4 * np.eye(4)

def rho_modelB(mu):
    """Existing code: rho = mu|Phi-><Phi-| + (1-mu)/2*(|HV><HV|+|VH><VH|)"""
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    hv = np.array([0, 1, 0, 0], dtype=complex)
    vh = np.array([0, 0, 1, 0], dtype=complex)
    return mu * np.outer(phi_minus, phi_minus.conj()) + (1-mu)/2 * (
        np.outer(hv, hv.conj()) + np.outer(vh, vh.conj()))

# === Projectors ===
def z_proj(outcome):
    if outcome == +1:
        return np.array([[1,0],[0,0]], dtype=complex)
    return np.array([[0,0],[0,1]], dtype=complex)

def bloch_state(theta, phi, outcome):
    ct, st = np.cos(theta/2), np.sin(theta/2)
    ep = np.exp(1j * phi)
    if outcome == +1:
        return np.array([ct, ep * st], dtype=complex)
    else:
        return np.array([st, -ep * ct], dtype=complex)

def tilted_proj(az_phi, polar_theta, outcome):
    state = bloch_state(polar_theta, az_phi, outcome)
    return np.outer(state, state.conj())

def compute_correlator(rho, x, y, theta, alice_az, bob_az):
    result = 0.0
    for a in [+1, -1]:
        for b in [+1, -1]:
            if x == 1:
                Pa = z_proj(a)
            else:
                Pa = tilted_proj(alice_az[x], theta, a)
            if y == 1:
                Pb = z_proj(b)
            else:
                Pb = tilted_proj(bob_az[y], theta, b)
            result += a * b * max(0, np.real(np.trace(np.kron(Pa, Pb) @ rho)))
    return result

# === Test parameters ===
mu = 0.95
theta = np.radians(31)

# Manuscript optimized angles (Table 4.3)
phi2_A = np.radians(112)
phi3_A = np.radians(217)
beta_B = np.radians(20)
alice_az = {2: phi2_A, 3: phi3_A}
bob_az   = {2: beta_B - phi2_A, 3: beta_B - phi3_A}

# Bong original angles 
phi2_bong = np.radians(0)
phi3_bong = np.radians(118)
beta_bong = np.radians(175)
alice_az_bong = {2: phi2_bong, 3: phi3_bong}
bob_az_bong   = {2: beta_bong - phi2_bong, 3: beta_bong - phi3_bong}

print("="*80)
print("DIAGNOSIS 1: Which density matrix gives the manuscript correlators?")
print("="*80)
print()

# Manuscript claims at theta=31, mu=0.95:
# (1,1): -1.0000   (1,2): -0.8572   (2,2): -0.5045   (2,3): -0.8933   (3,3): -0.8829
claimed = {(1,1): -1.0, (1,2): -0.8572, (2,2): -0.5045, (2,3): -0.8933, (3,3): -0.8829}

for label, rho_fn in [("Model A (I/4 mixing)", rho_modelA),
                       ("Model B (HV+VH mixing)", rho_modelB)]:
    rho = rho_fn(mu)
    print(f"{label}:")
    print(f"  {'(x,y)':>8s}  {'computed':>12s}  {'claimed':>12s}  {'diff':>10s}")
    for (x,y), cv in claimed.items():
        # Try both angle sets
        c_opt = compute_correlator(rho, x, y, theta, alice_az, bob_az)
        c_bong = compute_correlator(rho, x, y, theta, alice_az_bong, bob_az_bong)
        d_opt = abs(c_opt - cv)
        d_bong = abs(c_bong - cv)
        best = "opt" if d_opt < d_bong else "bong"
        best_c = c_opt if d_opt < d_bong else c_bong
        best_d = min(d_opt, d_bong)
        print(f"  ({x},{y})    {best_c:12.6f}  {cv:12.6f}  {best_d:10.6f}  [{best}]")
    print()

print("="*80)
print("DIAGNOSIS 2: Correlator (1,1) at z-basis should be -mu")
print("="*80)
print()
for label, rho_fn in [("Model A", rho_modelA), ("Model B", rho_modelB)]:
    rho = rho_fn(mu)
    c11 = compute_correlator(rho, 1, 1, theta, alice_az, bob_az)
    print(f"  {label}: <A1B1> = {c11:.6f}  (expected -1.0 per manuscript)")

# KEY INSIGHT: <A1B1> = -mu = -0.95 for Model A (I/4 mixing)
#              <A1B1> = -1.0  for Model B (HV+VH mixing)
# Because Model B's noise term has only |HV> and |VH> which are 
# ALREADY anti-correlated in z-basis, so <A1B1>_noise = -1.
# Model A's noise term I/4 gives <A1B1>_noise = 0 (maximally mixed).
print()
print("  For Model A: <A1B1> = mu*(-1) + (1-mu)*0 = -mu = -0.95")
print("  For Model B: <A1B1> = mu*(-1) + (1-mu)*(-1) = -1.0")
print("  Manuscript claims -1.0 => Model B is the correct one!")
print()

print("="*80)
print("DIAGNOSIS 3: Re-verify with Model B and BOTH angle sets")
print("="*80)
print()

rho_B = rho_modelB(mu)
for label, aa, ba in [("Optimized angles (112,217,20)", alice_az, bob_az),
                       ("Bong original (0,118,175)", alice_az_bong, bob_az_bong)]:
    print(f"{label}:")
    for (x,y), cv in sorted(claimed.items()):
        c = compute_correlator(rho_B, x, y, theta, aa, ba)
        d = abs(c - cv)
        ok = "[OK]" if d < 0.005 else "[MISS]"
        print(f"  ({x},{y}): {c:12.6f}  claimed={cv:12.4f}  diff={d:.6f}  {ok}")
    print()

# Full table with Model B + optimized angles
print("Full 9-correlator table (Model B, optimized angles):")
for x in [1,2,3]:
    for y in [1,2,3]:
        c = compute_correlator(rho_B, x, y, theta, alice_az, bob_az)
        print(f"  ({x},{y}): {c:12.6f}")
print()

# Full table with Model B + Bong angles
print("Full 9-correlator table (Model B, Bong angles):")
for x in [1,2,3]:
    for y in [1,2,3]:
        c = compute_correlator(rho_B, x, y, theta, alice_az_bong, bob_az_bong)
        print(f"  ({x},{y}): {c:12.6f}")
print()

print("="*80)
print("DIAGNOSIS 4: Gen LF 1 with both models and angle sets")
print("="*80)
print()

def compute_gen_lf1(rho, theta, aa, ba):
    I2 = np.eye(2, dtype=complex)
    corrs = {}
    for x in [1,2,3]:
        for y in [1,2,3]:
            corrs[(x,y)] = compute_correlator(rho, x, y, theta, aa, ba)
    mA = {}
    mB = {}
    for s in [1,2,3]:
        if s == 1:
            P_p = z_proj(+1)
            P_m = z_proj(-1)
        else:
            P_p = tilted_proj(aa[s], theta, +1)
            P_m = tilted_proj(aa[s], theta, -1)
        mA[s] = np.real(np.trace(np.kron(P_p - P_m, I2) @ rho))
        
        if s == 1:
            P_p = z_proj(+1)
            P_m = z_proj(-1)
        else:
            P_p = tilted_proj(ba[s], theta, +1)
            P_m = tilted_proj(ba[s], theta, -1)
        mB[s] = np.real(np.trace(np.kron(I2, P_p - P_m) @ rho))
    
    S = (-mA[1] - mA[2] - mB[1] - mB[2]
         - corrs[(1,1)] - 2*corrs[(1,2)] - 2*corrs[(2,1)] + 2*corrs[(2,2)]
         - corrs[(2,3)] - corrs[(3,2)] - corrs[(3,3)] - 6)
    return S, corrs, mA, mB

for label, rho_fn in [("Model A", rho_modelA), ("Model B", rho_modelB)]:
    rho = rho_fn(mu)
    for alabel, aa, ba in [("optimized", alice_az, bob_az),
                            ("Bong", alice_az_bong, bob_az_bong)]:
        S, _, _, _ = compute_gen_lf1(rho, theta, aa, ba)
        print(f"  {label}, {alabel} angles: Gen LF 1 = {S:+.4f}")
print()
print("  Manuscript claims: Gen LF 1 = +0.0891 at theta=31")
print()

# Check at theta=90 (equatorial) for comparison
print("  At theta=90 (equatorial):")
theta_eq = np.radians(90)
for label, rho_fn in [("Model A", rho_modelA), ("Model B", rho_modelB)]:
    rho = rho_fn(mu)
    for alabel, aa, ba in [("Bong", alice_az_bong, bob_az_bong)]:
        S, _, _, _ = compute_gen_lf1(rho, theta_eq, aa, ba)
        print(f"  {label}, {alabel} angles, theta=90: Gen LF 1 = {S:+.4f}")

print()
print("="*80)
print("DIAGNOSIS 5: sigma values")
print("="*80)
print()

N = 91000
rho_B = rho_modelB(mu)
S, corrs_B, mA_B, mB_B = compute_gen_lf1(rho_B, theta, alice_az, bob_az)

# sigma_correlator for mixed settings
sig_12 = np.sqrt((1 - corrs_B[(1,2)]**2) / N)
print(f"  Model B, optimized: sigma(1,2) = {sig_12:.6f}")
print(f"  Manuscript claims:  sigma ≈ 0.0017")
print()

# Significance
terms_sig = []
for v in [mA_B[1], mA_B[2], mB_B[1], mB_B[2]]:
    terms_sig.append((-1, v))
for (x,y), c in {(1,1):-1,(1,2):-2,(2,1):-2,(2,2):2,(2,3):-1,(3,2):-1,(3,3):-1}.items():
    terms_sig.append((c, corrs_B[(x,y)]))
sigma_S = np.sqrt(sum(c**2 * max(0, 1 - v**2) / N for c, v in terms_sig))
print(f"  Model B, optimized: Gen LF 1 = {S:+.4f}")
print(f"  sigma(S) = {sigma_S:.4f}")
print(f"  significance = {S/sigma_S:.1f} sigma")
print(f"  Manuscript: +0.0891 +/- 0.0103 (8.6 sigma)")
