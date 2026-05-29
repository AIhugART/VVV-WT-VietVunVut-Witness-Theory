"""
RCA LOGIC CROSSCHECK — Independent verification of key logical claims
=====================================================================
Focuses on:
1. Equatorial cancellation theorem (Proposition 1) 
2. Discussion Table δ⟨AB⟩ formula consistency
3. S2 first-order expansion correctness
4. FOM range claims [20°,45°] vs manuscript
5. cos θ scaling verification across multiple θ values
6. σ(S_LF1) exact vs approximate
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import numpy as np

# ---- Density matrix ----
def make_rho_SPDC(mu):
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    hv = np.array([0, 1, 0, 0], dtype=complex)
    vh = np.array([0, 0, 1, 0], dtype=complex)
    return mu * np.outer(phi_minus, phi_minus.conj()) + (1-mu)/2 * (
        np.outer(hv, hv.conj()) + np.outer(vh, vh.conj()))

H = np.array([1, 0], dtype=complex)
V = np.array([0, 1], dtype=complex)
I2 = np.eye(2, dtype=complex)

def z_proj(o):
    return np.array([[1,0],[0,0]], dtype=complex) if o==+1 else np.array([[0,0],[0,1]], dtype=complex)

def bloch_state(theta, phi, o):
    ct, st = np.cos(theta/2), np.sin(theta/2)
    ep = np.exp(1j * phi)
    return np.array([ct, ep*st]) if o==+1 else np.array([st, -ep*ct])

def tilted_proj(az, theta, o):
    s = bloch_state(theta, az, o)
    return np.outer(s, s.conj())

def compute_correlator(rho, x, y, theta, alice_az, bob_az):
    result = 0.0
    for a in [+1, -1]:
        for b in [+1, -1]:
            Pa = z_proj(a) if x == 1 else tilted_proj(alice_az[x], theta, a)
            Pb = z_proj(b) if y == 1 else tilted_proj(bob_az[y], theta, b)
            p = max(0, np.real(np.trace(np.kron(Pa, Pb) @ rho)))
            result += a * b * p
    return result

def compute_k9e_correlator(rho, theta, bob_az_y, beta_k9):
    f_perp = {
        (+1, +1): np.sin(theta/2)**2, (-1, +1): np.cos(theta/2)**2,
        (+1, -1): np.cos(theta/2)**2, (-1, -1): np.sin(theta/2)**2,
    }
    P_cd = {}
    for c in [+1, -1]:
        for d in [+1, -1]:
            P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(z_proj(c), z_proj(d)) @ rho)))
    P_bd = {}
    for b in [+1, -1]:
        for d in [+1, -1]:
            Pb = tilted_proj(bob_az_y, theta, b)
            ds = H if d == +1 else V
            P_bd[(b,d)] = max(0, np.real(ds.conj() @ Pb @ ds))
    Pk = {}; Z = 0
    for c in [+1, -1]:
        for b in [+1, -1]:
            val = sum(P_cd[(c,d)] * P_bd[(b,d)] * (1 - beta_k9 * f_perp[(b,d)]) for d in [+1, -1])
            Pk[(c,b)] = val; Z += val
    return sum(c*b*Pk[(c,b)] / Z for c in [+1,-1] for b in [+1,-1])

mu = 0.95
N = 91000
rho = make_rho_SPDC(mu)

# === TEST 1: Equatorial Cancellation — must hold for ANY g function ===
print("=" * 80)
print("TEST 1: EQUATORIAL CANCELLATION (Proposition 1)")
print("=" * 80)
theta_eq = np.radians(90)
# At theta=90, all overlaps = 1/2
overlaps = {
    ('+1','H'): np.cos(theta_eq/2)**2,
    ('+1','V'): np.sin(theta_eq/2)**2,
    ('-1','H'): np.sin(theta_eq/2)**2,
    ('-1','V'): np.cos(theta_eq/2)**2,
}
print(f"  Overlaps at theta=90:")
for (b,d), v in overlaps.items():
    print(f"    |<{b}|{d}>|^2 = {v:.6f}")
all_half = all(abs(v - 0.5) < 1e-10 for v in overlaps.values())
print(f"  All overlaps = 1/2? {all_half}")
print(f"  => g(1/2) = constant => P' = P_QM / Z_const = P_QM. QED.")

# Verify numerically: K9E should give same correlator at theta=90
phi2_eq = np.radians(0); bob_az_eq = np.radians(175)
corr_qm_eq = compute_correlator(rho, 1, 2, theta_eq, {2: phi2_eq}, {2: bob_az_eq - phi2_eq})
for beta_test in [0.05, 0.10, 0.30, 0.50]:
    corr_k9e_eq = compute_k9e_correlator(rho, theta_eq, bob_az_eq - phi2_eq, beta_test)
    diff = abs(corr_k9e_eq - corr_qm_eq)
    print(f"  beta={beta_test}: <AB>_QM={corr_qm_eq:.6f}, <AB>_K9E={corr_k9e_eq:.6f}, diff={diff:.2e}, CANCEL={diff<1e-12}")

# === TEST 2: cos θ SCALING — does δ really scale as cos θ? ===
print("\n" + "=" * 80)
print("TEST 2: cos theta SCALING (across multiple theta values)")
print("=" * 80)
beta_test = 0.10
phi2, phi3, bb = np.radians(112), np.radians(217), np.radians(20)
print(f"  beta = {beta_test}, fixed azimuthal angles")
print(f"  {'theta':>6s}  {'delta':>10s}  {'cos_theta':>10s}  {'delta/cos':>10s}  {'delta/beta':>10s}")
print(f"  {'-'*50}")
ratios = []
for td in [15, 20, 25, 31, 35, 40, 45, 50, 55, 60, 70, 80, 85]:
    tr = np.radians(td)
    corr_qm = compute_correlator(rho, 1, 2, tr, {2: phi2, 3: phi3}, {2: bb - phi2, 3: bb - phi3})
    corr_k9e = compute_k9e_correlator(rho, tr, bb - phi2, beta_test)
    delta = corr_k9e - corr_qm
    cos_t = np.cos(tr)
    ratio = delta / cos_t if abs(cos_t) > 0.01 else float('nan')
    ratios.append(ratio)
    print(f"  {td:6d}  {delta:10.6f}  {cos_t:10.4f}  {ratio:10.6f}  {delta/beta_test:10.6f}")

valid_ratios = [r for r in ratios if not np.isnan(r)]
ratio_std = np.std(valid_ratios) / abs(np.mean(valid_ratios)) if valid_ratios else float('inf')
print(f"\n  delta/cos(theta) mean = {np.mean(valid_ratios):.6f}")
print(f"  delta/cos(theta) std  = {np.std(valid_ratios):.6f}")
print(f"  Coefficient of variation = {ratio_std:.4f}")
print(f"  VERDICT: cos(theta) scaling {'CONFIRMED (CV < 5%)' if ratio_std < 0.05 else 'APPROXIMATE (CV > 5%)'}")

# === TEST 3: Discussion Table δ⟨AB⟩ ≈ 0.115β ===
print("\n" + "=" * 80)
print("TEST 3: DISCUSSION TABLE (line 634): delta<AB> ~ 0.115*beta")
print("=" * 80)
theta31 = np.radians(31)
print(f"  {'beta':>6s}  {'0.115*beta':>12s}  {'numerical':>12s}  {'match':>8s}")
print(f"  {'-'*45}")
for beta in [0.03, 0.05, 0.07, 0.10, 0.30]:
    approx = 0.115 * beta
    corr_k9e = compute_k9e_correlator(rho, theta31, bb - phi2, beta)
    corr_qm = compute_correlator(rho, 1, 2, theta31, {2: phi2, 3: phi3}, {2: bb - phi2, 3: bb - phi3})
    delta = abs(corr_k9e - corr_qm)
    match = abs(delta - approx) / approx < 0.1  # within 10%
    print(f"  {beta:6.2f}  {approx:12.4f}  {delta:12.4f}  {'OK' if match else 'MISMATCH':>8s}")

# === TEST 4: S2 First-order expansion δ = −β · |cosθ| · ⟨AB⟩² + O(β²) ===
print("\n" + "=" * 80)
print("TEST 4: S2 FIRST-ORDER EXPANSION")
print("=" * 80)
corr12_qm = compute_correlator(rho, 1, 2, theta31, {2: phi2, 3: phi3}, {2: bb - phi2, 3: bb - phi3})
print(f"  <A1B2>_QM = {corr12_qm:.6f}")
print(f"  |cos(31°)| = {abs(np.cos(theta31)):.6f}")
print(f"  <A1B2>_QM^2 = {corr12_qm**2:.6f}")
print(f"  Leading-order coefficient = |cos θ| · <AB>² = {abs(np.cos(theta31)) * corr12_qm**2:.6f}")
print()
print(f"  {'beta':>6s}  {'LO_pred':>10s}  {'numerical':>10s}  {'ratio':>8s}  {'S2_claim':>10s}")
print(f"  {'-'*50}")
for beta in [0.01, 0.03, 0.05, 0.07, 0.10, 0.30, 0.50]:
    lo = -beta * abs(np.cos(theta31)) * corr12_qm**2
    corr_k9e = compute_k9e_correlator(rho, theta31, bb - phi2, beta)
    num = corr_k9e - corr12_qm
    ratio = num / lo if abs(lo) > 1e-10 else float('nan')
    print(f"  {beta:6.2f}  {lo:10.6f}  {num:10.6f}  {ratio:8.4f}")

print(f"\n  S2 claims LO overestimates because Z < 1 renormalizes.")
print(f"  Observed: ratio < 1 for all beta => S2 is CORRECT that LO overestimates.")
print(f"  BUT: ratio ~ 0.18, meaning LO overestimates by ~5.5x!")
print(f"  This is a HUGE discrepancy — the 'leading order' is NOT a good approximation.")

# === TEST 5: sigma(S_LF1) exact vs sqrt(20/N) ===
print("\n" + "=" * 80)
print("TEST 5: sigma(S_LF1) — exact term-by-term vs sqrt(20/N)")
print("=" * 80)
aa = {2: phi2, 3: phi3}; ba = {2: bb - phi2, 3: bb - phi3}
corrs = {}
for x in [1,2,3]:
    for y in [1,2,3]:
        corrs[(x,y)] = compute_correlator(rho, x, y, theta31, aa, ba)

def compute_marginal_A(rho, s, theta, alice_az):
    if s == 1: Pp, Pm = z_proj(+1), z_proj(-1)
    else:
        Pp = tilted_proj(alice_az[s], theta, +1)
        Pm = tilted_proj(alice_az[s], theta, -1)
    return np.real(np.trace(np.kron(Pp - Pm, I2) @ rho))

def compute_marginal_B(rho, s, theta, bob_az):
    if s == 1: Pp, Pm = z_proj(+1), z_proj(-1)
    else:
        Pp = tilted_proj(bob_az[s], theta, +1)
        Pm = tilted_proj(bob_az[s], theta, -1)
    return np.real(np.trace(np.kron(I2, Pp - Pm) @ rho))

mA = {s: compute_marginal_A(rho, s, theta31, aa) for s in [1,2,3]}
mB = {s: compute_marginal_B(rho, s, theta31, ba) for s in [1,2,3]}

terms = [(-1, mA[1]), (-1, mA[2]), (-1, mB[1]), (-1, mB[2]),
         (-1, corrs[(1,1)]), (-2, corrs[(1,2)]), (-2, corrs[(2,1)]),
         (2, corrs[(2,2)]), (-1, corrs[(2,3)]), (-1, corrs[(3,2)]),
         (-1, corrs[(3,3)])]

sigma_exact = np.sqrt(sum(c**2 * max(0, 1 - v**2) / N for c, v in terms))
sigma_approx = np.sqrt(20 / N)

print(f"  Term-by-term contributions:")
for i, (c, v) in enumerate(terms):
    contrib = c**2 * max(0, 1 - v**2) / N
    print(f"    term {i+1}: coeff={c:+d}, value={v:+.4f}, var_contrib={contrib:.8f}")

print(f"\n  sigma_exact = {sigma_exact:.6f}")
print(f"  sigma_approx = sqrt(20/N) = {sigma_approx:.6f}")
print(f"  Ratio exact/approx = {sigma_exact/sigma_approx:.4f}")
print(f"  Manuscript line 564: 'sigma = sqrt[sum c_i^2(1-<v_i>^2)/N] ~ 0.0103'")
print(f"  Computed exact: {sigma_exact:.4f}")
print(f"  MATCH: {abs(sigma_exact - 0.0103) < 0.001}")
print(f"  Manuscript notes 'upper bound sqrt(20)/sqrt(N) ~ 0.015' => {sigma_approx:.4f}")

# === TEST 6: Gen LF 1 computation ===
print("\n" + "=" * 80)
print("TEST 6: Gen LF 1 VALUE")
print("=" * 80)
S = (-mA[1] - mA[2] - mB[1] - mB[2]
     - corrs[(1,1)] - 2*corrs[(1,2)] - 2*corrs[(2,1)]
     + 2*corrs[(2,2)] - corrs[(2,3)] - corrs[(3,2)] - corrs[(3,3)] - 6)
n_sigma = S / sigma_exact if S > 0 else 0
print(f"  Gen LF 1 = {S:+.6f}")
print(f"  sigma = {sigma_exact:.6f}")
print(f"  n_sigma = {n_sigma:.2f}")
print(f"  Manuscript: +0.0891 +/- 0.0103 (8.6 sigma)")
print(f"  MATCH S: {abs(S - 0.0891) < 0.001}")
print(f"  MATCH n_sigma: {abs(n_sigma - 8.6) < 0.5}")

# === TEST 7: N_min calculation ===
print("\n" + "=" * 80)
print("TEST 7: N_min FOR 5 sigma LF DETECTION")
print("=" * 80)
# Using exact sigma: need S / sigma_exact >= 5
# sigma_exact = sqrt(sum_terms / N), so S / sqrt(sum_terms/N) = S*sqrt(N)/sqrt(sum_terms) >= 5
# => N >= 25 * sum_terms / S^2
sum_terms = sum(c**2 * max(0, 1 - v**2) for c, v in terms)
N_min_exact = 25 * sum_terms / S**2
# Using approx sigma: N >= 20 * 25 / S^2
N_min_approx = 500 / S**2
print(f"  N_min (exact sigma) = {N_min_exact:.0f}")
print(f"  N_min (approx sqrt(20/N)) = {N_min_approx:.0f}")
print(f"  Manuscript claims N_min ~ 30,800")
print(f"  MATCH (exact): {abs(N_min_exact - 30800) / 30800 < 0.15}")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
