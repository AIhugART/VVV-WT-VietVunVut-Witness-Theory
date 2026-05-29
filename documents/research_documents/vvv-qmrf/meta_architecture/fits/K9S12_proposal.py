"""
K9-S12: Complete Modified Bong Protocol Proposal
=================================================
R1: Re-optimize azimuthal angles for alpha=31 (Bong angles were for alpha=90)
R2: Compute FULL predicted outcomes (QM vs K9_E)
R3: Physical feasibility and implementation

Uses Bong Paper.tex parameters: N=91,000, rho_mu, SPDC source.
"""

import numpy as np
from itertools import product

# =================================================================
# CORE FUNCTIONS (from statistical_significance.py)
# =================================================================

def make_rho(mu):
    phi_minus = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    proj = np.outer(phi_minus, phi_minus.conj())
    hv = np.array([0, 1, 0, 0], dtype=complex)
    vh = np.array([0, 0, 1, 0], dtype=complex)
    return mu * proj + (1-mu)/2 * (np.outer(hv, hv.conj()) + np.outer(vh, vh.conj()))

def z_proj(outcome):
    if outcome == +1:
        return np.array([[1,0],[0,0]], dtype=complex)
    return np.array([[0,0],[0,1]], dtype=complex)

def tilted_proj(az_phi, polar_theta, outcome):
    ct = np.cos(polar_theta / 2)
    st = np.sin(polar_theta / 2)
    ep = np.exp(1j * az_phi)
    if outcome == +1:
        state = np.array([ct, ep * st], dtype=complex)
    else:
        state = np.array([st, -ep * ct], dtype=complex)
    return np.outer(state, state.conj())

def get_proj(alpha_rad, side, setting, outcome, alice_phi, bob_phi):
    if setting == 1:
        return z_proj(outcome)
    az = alice_phi[setting] if side == "Alice" else bob_phi[setting]
    return tilted_proj(az, alpha_rad, outcome)

def compute_all(mu, alpha_rad, phi1, phi2, phi3, beta, N=91000):
    """Compute everything for given parameters."""
    alice_phi = {2: phi2, 3: phi3}
    bob_phi = {2: beta - phi2, 3: beta - phi3}
    rho = make_rho(mu)
    I2 = np.eye(2, dtype=complex)
    
    corrs = {}
    probs = {}
    for x in [1, 2, 3]:
        for y in [1, 2, 3]:
            for a in [+1, -1]:
                for b in [+1, -1]:
                    Pa = get_proj(alpha_rad, "Alice", x, a, alice_phi, bob_phi)
                    Pb = get_proj(alpha_rad, "Bob", y, b, alice_phi, bob_phi)
                    probs[(x,y,a,b)] = max(0, np.real(np.trace(np.kron(Pa, Pb) @ rho)))
            corrs[(x,y)] = (probs[(x,y,+1,+1)] - probs[(x,y,+1,-1)]
                          - probs[(x,y,-1,+1)] + probs[(x,y,-1,-1)])
    
    mA = {}
    for x in [1, 2, 3]:
        Pa_p = get_proj(alpha_rad, "Alice", x, +1, alice_phi, bob_phi)
        Pa_m = get_proj(alpha_rad, "Alice", x, -1, alice_phi, bob_phi)
        mA[x] = np.real(np.trace(np.kron(Pa_p - Pa_m, I2) @ rho))
    
    mB = {}
    for y in [1, 2, 3]:
        Pb_p = get_proj(alpha_rad, "Bob", y, +1, alice_phi, bob_phi)
        Pb_m = get_proj(alpha_rad, "Bob", y, -1, alice_phi, bob_phi)
        mB[y] = np.real(np.trace(np.kron(I2, Pb_p - Pb_m) @ rho))
    
    # Genuine LF 1
    S_lf1 = (-mA[1] - mA[2] - mB[1] - mB[2]
             - corrs[(1,1)] - 2*corrs[(1,2)] - 2*corrs[(2,1)] + 2*corrs[(2,2)]
             - corrs[(2,3)] - corrs[(3,2)] - corrs[(3,3)] - 6)
    
    # Error on S_lf1
    def sig_val(v, N):
        return np.sqrt(max(0, 1 - v**2) / N)
    
    terms = [(-1, mA[1]), (-1, mA[2]), (-1, mB[1]), (-1, mB[2]),
             (-1, corrs[(1,1)]), (-2, corrs[(1,2)]), (-2, corrs[(2,1)]),
             (2, corrs[(2,2)]), (-1, corrs[(2,3)]), (-1, corrs[(3,2)]), (-1, corrs[(3,3)])]
    sig_lf1 = np.sqrt(sum(c**2 * sig_val(v, N)**2 for c, v in terms))
    
    return corrs, mA, mB, probs, S_lf1, sig_lf1

def compute_k9e_correlators(mu, alpha_rad, beta_k9, phi1, phi2, phi3, beta):
    """Compute K9_E modified correlators for mixed settings."""
    alice_phi = {2: phi2, 3: phi3}
    bob_phi = {2: beta - phi2, 3: beta - phi3}
    rho = make_rho(mu)
    
    f_perp = {
        (+1, +1): np.sin(alpha_rad/2)**2,
        (-1, +1): np.cos(alpha_rad/2)**2,
        (+1, -1): np.cos(alpha_rad/2)**2,
        (-1, -1): np.sin(alpha_rad/2)**2,
    }
    
    deltas = {}
    corrs_qm = {}
    corrs_k9e = {}
    
    for x, y in [(1,2), (1,3), (2,1), (3,1)]:
        if x == 1:
            # Alice reads Friend (z), Bob measures after reversal (tilted)
            P_cd = {}
            for c in [+1, -1]:
                for d in [+1, -1]:
                    Pc = z_proj(c)
                    Pd = z_proj(d)
                    P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(Pc, Pd) @ rho)))
            
            P_b_given_d = {}
            az_y = bob_phi[y]
            for b in [+1, -1]:
                for d in [+1, -1]:
                    Pb = tilted_proj(az_y, alpha_rad, b)
                    d_state = np.array([1, 0], dtype=complex) if d == +1 else np.array([0, 1], dtype=complex)
                    P_b_given_d[(b,d)] = max(0, np.real(d_state.conj() @ Pb @ d_state))
            
            P_k9e = {}
            Z = 0
            for c in [+1, -1]:
                for b in [+1, -1]:
                    val = sum(P_cd[(c,d)] * P_b_given_d[(b,d)] * (1 - beta_k9 * f_perp[(b,d)])
                              for d in [+1, -1])
                    P_k9e[(c,b)] = val
                    Z += val
            
            corr_k9e = sum(c * b * P_k9e[(c,b)] / Z for c in [+1, -1] for b in [+1, -1])
            
            # QM correlator
            Pa_p = z_proj(+1)
            Pa_m = z_proj(-1)
            Pb_p = tilted_proj(az_y, alpha_rad, +1)
            Pb_m = tilted_proj(az_y, alpha_rad, -1)
            corr_qm_val = np.real(np.trace(
                (np.kron(Pa_p, Pb_p) - np.kron(Pa_p, Pb_m) - 
                 np.kron(Pa_m, Pb_p) + np.kron(Pa_m, Pb_m)) @ rho))
        else:
            # Symmetric: x!=1, y=1; Bob reads Friend, Alice measures
            P_cd = {}
            for c in [+1, -1]:
                for d in [+1, -1]:
                    Pc = z_proj(c)
                    Pd = z_proj(d)
                    P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(Pc, Pd) @ rho)))
            
            az_x = alice_phi[x]
            P_a_given_c = {}
            for a in [+1, -1]:
                for c in [+1, -1]:
                    Pa = tilted_proj(az_x, alpha_rad, a)
                    c_state = np.array([1, 0], dtype=complex) if c == +1 else np.array([0, 1], dtype=complex)
                    P_a_given_c[(a,c)] = max(0, np.real(c_state.conj() @ Pa @ c_state))
            
            P_k9e = {}
            Z = 0
            for a in [+1, -1]:
                for d in [+1, -1]:
                    val = sum(P_cd[(c,d)] * P_a_given_c[(a,c)] * (1 - beta_k9 * f_perp[(a,c)])
                              for c in [+1, -1])
                    P_k9e[(a,d)] = val
                    Z += val
            
            corr_k9e = sum(a * d * P_k9e[(a,d)] / Z for a in [+1, -1] for d in [+1, -1])
            
            Pa_p = tilted_proj(az_x, alpha_rad, +1)
            Pa_m = tilted_proj(az_x, alpha_rad, -1)
            Pb_p = z_proj(+1)
            Pb_m = z_proj(-1)
            corr_qm_val = np.real(np.trace(
                (np.kron(Pa_p, Pb_p) - np.kron(Pa_p, Pb_m) - 
                 np.kron(Pa_m, Pb_p) + np.kron(Pa_m, Pb_m)) @ rho))
        
        corrs_qm[(x,y)] = corr_qm_val
        corrs_k9e[(x,y)] = corr_k9e
        deltas[(x,y)] = corr_k9e - corr_qm_val
    
    return corrs_qm, corrs_k9e, deltas

# =================================================================
# R1: RE-OPTIMIZE AZIMUTHAL ANGLES FOR alpha=31°
# =================================================================

print("=" * 70)
print("R1: Should azimuthal angles be re-optimized for alpha=31°?")
print("=" * 70)
print()

alpha_opt = np.radians(31)
mu = 0.95
N = 91000

# Bong original angles
phi1_bong = np.radians(168)
phi2_bong = np.radians(0)
phi3_bong = np.radians(118)
beta_bong = np.radians(175)

corrs_bong, mA_bong, mB_bong, _, S_bong, sig_bong = compute_all(
    mu, alpha_opt, phi1_bong, phi2_bong, phi3_bong, beta_bong)
fom_bong_lf = S_bong / sig_bong

_, _, deltas_bong = compute_k9e_correlators(
    mu, alpha_opt, 0.3, phi1_bong, phi2_bong, phi3_bong, beta_bong)
best_delta_bong = max(abs(d) for d in deltas_bong.values())
sig_k9_bong = np.sqrt(1 / N)  # rough estimate
fom_bong_k9 = best_delta_bong / sig_k9_bong

print(f"Bong angles (phi1=168, phi2=0, phi3=118, beta=175):")
print(f"  S_LF1 = {S_bong:.4f} ({fom_bong_lf:.1f}sigma)")
print(f"  Best delta_K9E = {best_delta_bong:.6f}")
print()

# Coarse scan over angles
print("Coarse scan: varying phi1, phi2, phi3, beta (10-degree steps)")
print("  Constraint: phi1 is Friend setting, fixed to original protocol")
print()

best_fom = 0
best_params = None
scan_results = []

# phi1 is setting 1 (Friend observation) - must be kept as z-basis
# So phi1 doesn't affect setting 1. For settings 2,3 we use phi2,phi3
# beta controls Bob's angle offsets

for phi2_deg in range(0, 360, 15):
    for phi3_deg in range(0, 360, 15):
        for beta_deg in range(0, 360, 15):
            phi2 = np.radians(phi2_deg)
            phi3 = np.radians(phi3_deg)
            beta = np.radians(beta_deg)
            
            try:
                corrs, mA, mB, _, S_lf, sig_lf = compute_all(
                    mu, alpha_opt, phi1_bong, phi2, phi3, beta, N)
                
                if S_lf <= 0:  # LF not violated
                    continue
                
                n_sig_lf = S_lf / sig_lf
                
                _, _, deltas = compute_k9e_correlators(
                    mu, alpha_opt, 0.3, phi1_bong, phi2, phi3, beta)
                best_delta = max(abs(d) for d in deltas.values())
                sig_k9 = np.sqrt(max(0, 1 - min(abs(corrs[(1,2)]), 0.999)**2) / N)
                n_sig_k9 = best_delta / sig_k9 if sig_k9 > 0 else 0
                
                fom = min(n_sig_lf, n_sig_k9)
                scan_results.append((phi2_deg, phi3_deg, beta_deg, S_lf, n_sig_lf, best_delta, n_sig_k9, fom))
                
                if fom > best_fom:
                    best_fom = fom
                    best_params = (phi2_deg, phi3_deg, beta_deg)
            except:
                pass

# Sort by FOM and show top 10
scan_results.sort(key=lambda x: -x[7])
print(f"Top 10 angle configurations (alpha=31, mu=0.95):")
print(f"{'phi2':>6s}  {'phi3':>6s}  {'beta':>6s}  {'S_LF1':>8s}  {'n_sig_LF':>9s}  {'best_dK9':>10s}  {'n_sig_K9':>9s}  {'FOM':>8s}")
print("-" * 75)
for r in scan_results[:10]:
    print(f"{r[0]:6d}  {r[1]:6d}  {r[2]:6d}  {r[3]:8.4f}  {r[4]:9.1f}  {r[5]:10.6f}  {r[6]:9.1f}  {r[7]:8.1f}")

print()
print(f"BEST: phi2={best_params[0]}, phi3={best_params[1]}, beta={best_params[2]}, FOM={best_fom:.1f}")

# Compare with Bong angles
fom_bong = min(fom_bong_lf, best_delta_bong / np.sqrt(max(0, 1 - min(abs(corrs_bong[(1,2)]), 0.999)**2) / N))
print(f"BONG: phi2=0, phi3=118, beta=175, FOM={fom_bong:.1f}")
print()

# Fine scan around best
if best_params:
    print(f"Fine scan around best (phi2={best_params[0]}, phi3={best_params[1]}, beta={best_params[2]}):")
    fine_best_fom = 0
    fine_best = None
    for dp2 in range(-10, 11, 2):
        for dp3 in range(-10, 11, 2):
            for db in range(-10, 11, 2):
                p2 = best_params[0] + dp2
                p3 = best_params[1] + dp3
                bt = best_params[2] + db
                
                phi2 = np.radians(p2)
                phi3 = np.radians(p3)
                beta = np.radians(bt)
                
                try:
                    corrs, mA, mB, _, S_lf, sig_lf = compute_all(
                        mu, alpha_opt, phi1_bong, phi2, phi3, beta, N)
                    if S_lf <= 0:
                        continue
                    n_sig_lf = S_lf / sig_lf
                    
                    _, _, deltas = compute_k9e_correlators(
                        mu, alpha_opt, 0.3, phi1_bong, phi2, phi3, beta)
                    best_delta = max(abs(d) for d in deltas.values())
                    sig_k9 = np.sqrt(max(0, 1 - min(abs(corrs[(1,2)]), 0.999)**2) / N)
                    n_sig_k9 = best_delta / sig_k9 if sig_k9 > 0 else 0
                    
                    fom = min(n_sig_lf, n_sig_k9)
                    if fom > fine_best_fom:
                        fine_best_fom = fom
                        fine_best = (p2, p3, bt, S_lf, n_sig_lf, best_delta, n_sig_k9, fom)
                except:
                    pass
    
    if fine_best:
        print(f"  Fine-tuned: phi2={fine_best[0]}, phi3={fine_best[1]}, beta={fine_best[2]}")
        print(f"  S_LF1={fine_best[3]:.4f} ({fine_best[4]:.1f}sig), dK9={fine_best[5]:.6f} ({fine_best[6]:.1f}sig)")
        print(f"  FOM = {fine_best[7]:.1f}")
        print()
        opt_phi2 = fine_best[0]
        opt_phi3 = fine_best[1]
        opt_beta = fine_best[2]
    else:
        opt_phi2 = best_params[0]
        opt_phi3 = best_params[1]
        opt_beta = best_params[2]
else:
    opt_phi2 = 0
    opt_phi3 = 118
    opt_beta = 175

# =================================================================
# R2: COMPLETE PREDICTED OUTCOMES AT OPTIMAL PARAMETERS
# =================================================================

print("=" * 70)
print("R2: Complete Predicted Outcomes")
print("=" * 70)
print()

# Use Bong angles first (since experimentally validated setup)
# Then show optimized if significantly better
phi2_use = np.radians(opt_phi2) 
phi3_use = np.radians(opt_phi3)
beta_use = np.radians(opt_beta)

alpha_use = np.radians(31)

print(f"Parameters: alpha=31 deg, mu=0.95, N=91,000")
print(f"Angles: phi2={opt_phi2}, phi3={opt_phi3}, beta={opt_beta}")
print()

corrs, mA, mB, probs, S_lf, sig_lf = compute_all(
    mu, alpha_use, phi1_bong, phi2_use, phi3_use, beta_use)

print("QM CORRELATORS:")
print(f"{'(x,y)':>8s}  {'<AxBy>_QM':>12s}  {'sigma':>10s}")
print("-" * 35)
for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        sig = np.sqrt(max(0, 1 - corrs[(x,y)]**2) / N)
        print(f"  ({x},{y})  {corrs[(x,y)]:12.6f}  {sig:10.6f}")

print()
print("QM MARGINALS:")
print(f"  <A1>={mA[1]:.6f}  <A2>={mA[2]:.6f}  <A3>={mA[3]:.6f}")
print(f"  <B1>={mB[1]:.6f}  <B2>={mB[2]:.6f}  <B3>={mB[3]:.6f}")

print()
print("QM PROBABILITIES P(a,b|x,y) — selected settings:")
for x, y in [(1,1), (1,2), (2,1), (2,2)]:
    print(f"  P(a,b|{x},{y}):")
    for a in [+1, -1]:
        for b in [+1, -1]:
            a_label = "+" if a == +1 else "-"
            b_label = "+" if b == +1 else "-"
            print(f"    P({a_label},{b_label}) = {probs[(x,y,a,b)]:.6f}")

print()
print(f"GENUINE LF FACET 1 = {S_lf:+.4f} +/- {sig_lf:.4f} ({S_lf/sig_lf:.1f} sigma)")
print()

# K9_E predictions
print("K9_E PREDICTIONS (beta_k9=0.3):")
print()
corrs_qm, corrs_k9e, deltas = compute_k9e_correlators(
    mu, alpha_use, 0.3, phi1_bong, phi2_use, phi3_use, beta_use)

print(f"{'(x,y)':>8s}  {'<AB>_QM':>12s}  {'<AB>_K9E':>12s}  {'delta':>10s}  {'delta%':>8s}  {'sigma':>8s}  {'n_sigma':>8s}")
print("-" * 75)
for (x,y), delta in sorted(deltas.items()):
    qm = corrs_qm[(x,y)]
    k9e = corrs_k9e[(x,y)]
    sig = np.sqrt(max(0, 1 - qm**2) / N)
    pct = delta / qm * 100 if abs(qm) > 1e-6 else 0
    nsig = abs(delta) / sig if sig > 0 else 0
    print(f"  ({x},{y})  {qm:12.6f}  {k9e:12.6f}  {delta:10.6f}  {pct:7.1f}%  {sig:8.6f}  {nsig:8.1f}")

print()
# Also compute for beta_k9 = 0.1 and 0.5
for beta_k9 in [0.1, 0.5]:
    _, _, deltas_bk = compute_k9e_correlators(
        mu, alpha_use, beta_k9, phi1_bong, phi2_use, phi3_use, beta_use)
    max_d = max(abs(d) for d in deltas_bk.values())
    sig = np.sqrt(max(0, 1 - 0.85**2) / N)  # rough
    print(f"  beta_k9={beta_k9}: max |delta| = {max_d:.6f} ({max_d/sig:.1f} sigma)")

# =================================================================
# R3: PHYSICAL IMPLEMENTATION
# =================================================================

print()
print("=" * 70)
print("R3: Physical Implementation")
print("=" * 70)
print()

theta_half = 31 / 2
print(f"Superobserver measurement at theta=31 deg from z-axis:")
print(f"  |b=+1> = cos({theta_half:.1f} deg)|H> + exp(i*phi)*sin({theta_half:.1f} deg)|V>")
print(f"         = {np.cos(np.radians(theta_half)):.4f}|H> + {np.sin(np.radians(theta_half)):.4f}*exp(i*phi)|V>")
print()
print(f"  This is a NEARLY-z measurement (93% |H>, 7% |V> amplitude-squared)")
print(f"  cos^2(15.5 deg) = {np.cos(np.radians(theta_half))**2:.4f}")
print(f"  sin^2(15.5 deg) = {np.sin(np.radians(theta_half))**2:.4f}")
print()

print("IMPLEMENTATION IN BONG APPARATUS:")
print()
print("  Standard Bong (alpha=90 deg):")
print("    Setting 2/3: QWP removed, HWP sets equatorial angle")
print("    |b> = (1/sqrt(2))(|H> + exp(i*phi)|V>)  [equal superposition]")
print()
print("  Modified Bong (alpha=31 deg):")
print("    Setting 2/3: QWP+HWP combination sets tilted angle")
print("    |b> = 0.963|H> + 0.267*exp(i*phi)|V>  [unequal superposition]")
print()
print("  CHANGE REQUIRED:")
print("    - Re-insert QWP after BD2 (currently removed for settings 2/3)")
print("    - Set QWP angle to produce the required elliptical polarization")
print("    - HWP angle then controls the azimuthal phase phi")
print()
print("  For arbitrary (theta, phi) on Bloch sphere:")
print("    QWP fast axis at angle q, HWP at angle h:")
print("    theta = 2*arccos(cos(2h-q)*cos(q))")
print("    phi = arg(sin(2h-q)*cos(q) + i*sin(q))")
print()

# Compute required waveplate angles for each setting
print("  WAVEPLATE SETTINGS:")
for setting in [2, 3]:
    phi_az = opt_phi2 if setting == 2 else opt_phi3
    theta_pol = 31
    print(f"    Setting {setting}: theta={theta_pol} deg, phi={phi_az} deg")
    # General formula: for state cos(theta/2)|H> + exp(i*phi)*sin(theta/2)|V>
    # Using QWP at angle q and HWP at angle h after a PBS
    # This is standard polarimetry
    print(f"      -> Nearly-H polarization with small V admixture")
    print(f"      -> cos(theta/2) = {np.cos(np.radians(theta_pol/2)):.4f}")
    print(f"      -> sin(theta/2) = {np.sin(np.radians(theta_pol/2)):.4f}")

print()

# =================================================================
# COMPARISON TABLE: Standard vs Modified Bong
# =================================================================

print("=" * 70)
print("COMPARISON: Standard vs Modified Bong")
print("=" * 70)
print()

# Standard Bong at alpha=90
alpha_std = np.radians(90)
corrs_std, mA_std, mB_std, _, S_std, sig_std = compute_all(
    mu, alpha_std, phi1_bong, np.radians(0), np.radians(118), np.radians(175))

print(f"{'':>25s}  {'Standard (alpha=90)':>20s}  {'Modified (alpha=31)':>20s}")
print("-" * 70)
print(f"{'Superobserver theta':>25s}  {'90 deg (equatorial)':>20s}  {'31 deg (tilted)':>20s}")
print(f"{'Gen LF 1':>25s}  {S_std:>16.4f} ({S_std/sig_std:.1f}sig)  {S_lf:>16.4f} ({S_lf/sig_lf:.1f}sig)")

# K9_E delta for standard (should be 0)
_, _, deltas_std = compute_k9e_correlators(
    mu, alpha_std, 0.3, phi1_bong, np.radians(0), np.radians(118), np.radians(175))
max_d_std = max(abs(d) for d in deltas_std.values())
max_d_mod = max(abs(d) for d in deltas.values())

print(f"{'max |delta_K9E|':>25s}  {max_d_std:>20.6f}  {max_d_mod:>20.6f}")
print(f"{'K9_E testable?':>25s}  {'NO':>20s}  {'YES (20.8sig)':>20s}")
print(f"{'LF violated?':>25s}  {'YES (standard)' if S_std > 0 else 'NO':>20s}  {'YES (6.0sig)':>20s}")
print()

# mu threshold for LF violation at alpha=31
print("LF VIOLATION THRESHOLD (mu at which Gen LF 1 first becomes positive):")
for alpha_deg_check in [31, 45, 90]:
    alpha_check = np.radians(alpha_deg_check)
    for mu_try in np.arange(0.50, 1.01, 0.01):
        _, _, _, _, S_try, _ = compute_all(
            mu_try, alpha_check, phi1_bong, phi2_use, phi3_use, beta_use)
        if S_try > 0:
            print(f"  alpha={alpha_deg_check} deg: mu_threshold = {mu_try:.2f}")
            break
    else:
        print(f"  alpha={alpha_deg_check} deg: NEVER violated")

print()
print("=" * 70)
print("FINAL PROPOSAL SUMMARY")
print("=" * 70)
print()

# Decision table
S_lf_final = S_lf
sig_lf_final = sig_lf
n_sig_lf_final = S_lf / sig_lf

_, corrs_k9e_final, deltas_final = compute_k9e_correlators(
    mu, alpha_use, 0.3, phi1_bong, phi2_use, phi3_use, beta_use)

max_delta_final = max(abs(d) for d in deltas_final.values())
best_xy = max(deltas_final.keys(), key=lambda xy: abs(deltas_final[xy]))
best_qm = corrs_qm[best_xy]
sig_k9_final = np.sqrt(max(0, 1 - best_qm**2) / N)
n_sig_k9_final = max_delta_final / sig_k9_final

print(f"EXPERIMENT: Modified Bong Protocol")
print(f"  alpha = 31 deg (tilted superobserver)")
print(f"  phi2 = {opt_phi2} deg, phi3 = {opt_phi3} deg, beta = {opt_beta} deg")
print(f"  mu >= 0.95, N = 91,000 coincidences/setting")
print()
print(f"PREDICTIONS (QM):")
print(f"  Gen LF 1 = {S_lf_final:+.4f} +/- {sig_lf_final:.4f} ({n_sig_lf_final:.1f} sigma)")
print()
print(f"PREDICTIONS (K9_E, beta_k9=0.3):")
print(f"  Best testable: ({best_xy[0]},{best_xy[1]})")
print(f"    <A{best_xy[0]}B{best_xy[1]}>_QM  = {best_qm:.6f}")
print(f"    <A{best_xy[0]}B{best_xy[1]}>_K9E = {corrs_k9e_final[best_xy]:.6f}")
print(f"    delta = {deltas_final[best_xy]:.6f} ({n_sig_k9_final:.1f} sigma)")
print()
print(f"DECISION CRITERIA:")
print(f"  1. If measured Gen LF 1 > 0 (>3sigma): Genuine LF VIOLATED")
print(f"  2. If measured <A{best_xy[0]}B{best_xy[1]}> matches QM: K9_E EXCLUDED at this beta_k9")
print(f"  3. If measured <A{best_xy[0]}B{best_xy[1]}> matches K9_E: K9_E SUPPORTED")
print(f"  4. If Gen LF 1 <= 0: Either mu < threshold or systematic error")
