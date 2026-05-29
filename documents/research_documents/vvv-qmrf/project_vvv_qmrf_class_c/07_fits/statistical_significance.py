"""
K9-S11d: Statistical Significance Analysis
===========================================
Three Questions:
Q1: Is +0.022 LF violation at alpha=45 statistically significant?
Q2: Is alpha=35 better than alpha=45? Proper optimization criterion.
Q3: What is delta<AxBy> in actual measurable units?

Bong experimental parameters (from Paper.tex):
  N = 91,000 coincidences per measurement setting
  9 measurement combinations (3x3)
  XY-plane measurements confirmed (Eq. 4-5 in paper)
"""

import numpy as np

# =================================================================
# EXPERIMENTAL PARAMETERS (from Bong Paper.tex, lines 547-573)
# =================================================================

N_COINC = 91000  # coincidences per measurement setting
PHI_1 = np.radians(168.0)
PHI_2 = np.radians(0.0)
PHI_3 = np.radians(118.0)
BETA = np.radians(175.0)

alice_phi = {2: PHI_2, 3: PHI_3}
bob_phi = {2: BETA - PHI_2, 3: BETA - PHI_3}

# =================================================================
# QUANTUM STATE AND MEASUREMENT FUNCTIONS
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

def get_proj(alpha_deg, side, setting, outcome):
    alpha = np.radians(alpha_deg)
    if setting == 1:
        return z_proj(outcome)
    az = alice_phi[setting] if side == "Alice" else bob_phi[setting]
    return tilted_proj(az, alpha, outcome)

def compute_probs(rho, alpha_deg, x, y):
    """P(a,b|x,y) for all (a,b) pairs"""
    probs = {}
    for a in [+1, -1]:
        for b in [+1, -1]:
            Pa = get_proj(alpha_deg, "Alice", x, a)
            Pb = get_proj(alpha_deg, "Bob", y, b)
            probs[(a,b)] = max(0, np.real(np.trace(np.kron(Pa, Pb) @ rho)))
    return probs

def compute_correlator(rho, alpha_deg, x, y):
    probs = compute_probs(rho, alpha_deg, x, y)
    return (probs[(+1,+1)] - probs[(+1,-1)] - probs[(-1,+1)] + probs[(-1,-1)])

def compute_marginal(rho, alpha_deg, side, setting):
    I2 = np.eye(2, dtype=complex)
    P_p = get_proj(alpha_deg, side, setting, +1)
    P_m = get_proj(alpha_deg, side, setting, -1)
    if side == "Alice":
        pp = np.real(np.trace(np.kron(P_p, I2) @ rho))
        pm = np.real(np.trace(np.kron(P_m, I2) @ rho))
    else:
        pp = np.real(np.trace(np.kron(I2, P_p) @ rho))
        pm = np.real(np.trace(np.kron(I2, P_m) @ rho))
    return pp - pm

# =================================================================
# STATISTICAL ERROR COMPUTATION
# =================================================================

def sigma_correlator(corr_val, N):
    """
    Standard error of a correlator <AB> = sum_{a,b} a*b*P(a,b)
    
    Var(<AB>) = (1 - <AB>^2) / N  (multinomial estimation)
    sigma = sqrt((1 - <AB>^2) / N)
    """
    return np.sqrt(max(0, 1 - corr_val**2) / N)

def sigma_marginal(marg_val, N):
    """
    Standard error of a marginal <A> = P(+1) - P(-1)
    Var(<A>) = (1 - <A>^2) / N
    """
    return np.sqrt(max(0, 1 - marg_val**2) / N)

def genuine_lf_1_value_and_sigma(rho, alpha_deg, N):
    """
    Gen LF 1 = -<A1> - <A2> - <B1> - <B2> 
               - <A1B1> - 2<A1B2> - 2<A2B1> + 2<A2B2>
               - <A2B3> - <A3B2> - <A3B3> - 6
    
    Error propagation: sigma^2(S) = sum_i c_i^2 * sigma_i^2
    """
    # Compute all values and their sigmas
    terms = []  # (coefficient, value, sigma)
    
    # Marginals
    for side, idx in [("Alice", 1), ("Alice", 2), ("Bob", 1), ("Bob", 2)]:
        val = compute_marginal(rho, alpha_deg, side, idx)
        sig = sigma_marginal(val, N)
        terms.append((-1, val, sig))
    
    # Correlators with coefficients
    corr_coeffs = {
        (1,1): -1, (1,2): -2, (2,1): -2, (2,2): 2,
        (2,3): -1, (3,2): -1, (3,3): -1
    }
    for (x,y), coeff in corr_coeffs.items():
        val = compute_correlator(rho, alpha_deg, x, y)
        sig = sigma_correlator(val, N)
        terms.append((coeff, val, sig))
    
    # Compute S value
    S = sum(c * v for c, v, _ in terms) - 6
    
    # Error propagation (independent terms)
    sigma_S = np.sqrt(sum(c**2 * s**2 for c, _, s in terms))
    
    return S, sigma_S

# =================================================================
# Q1: STATISTICAL SIGNIFICANCE OF LF VIOLATION
# =================================================================

print("=" * 70)
print("QUESTION 1: Is +0.022 LF violation statistically significant?")
print("=" * 70)
print()

mu = 0.95
rho = make_rho(mu)

print(f"Parameters: mu={mu}, N={N_COINC:,} coincidences per setting")
print()

# At alpha=45
S_45, sig_45 = genuine_lf_1_value_and_sigma(rho, 45, N_COINC)
nsig_45 = S_45 / sig_45 if sig_45 > 0 else 0

# At alpha=35
S_35, sig_35 = genuine_lf_1_value_and_sigma(rho, 35, N_COINC)
nsig_35 = S_35 / sig_35 if sig_35 > 0 else 0

# At alpha=90 (standard)
S_90, sig_90 = genuine_lf_1_value_and_sigma(rho, 90, N_COINC)
nsig_90 = S_90 / sig_90 if sig_90 > 0 else 0

print(f"{'alpha':>6s}  {'S_LF1':>10s}  {'sigma':>10s}  {'S/sigma':>10s}  {'Significant?':>14s}")
print("-" * 56)
for alpha_deg in [30, 35, 40, 45, 47, 50, 55, 60, 90]:
    S, sig = genuine_lf_1_value_and_sigma(rho, alpha_deg, N_COINC)
    nsig = S / sig if sig > 0 else 0
    violated = S > 0
    if violated:
        sig_label = f"{nsig:.1f}sigma" + (" ***" if nsig >= 3 else " *" if nsig >= 2 else "")
    else:
        sig_label = "not violated"
    print(f"{alpha_deg:6d}  {S:10.4f}  {sig:10.4f}  {nsig:10.2f}  {sig_label:>14s}")

print()
print(f"ANSWER Q1: At alpha=45, mu=0.95:")
print(f"  S_LF1 = {S_45:.4f}, sigma = {sig_45:.4f}, significance = {nsig_45:.1f}sigma")
if nsig_45 < 3:
    print(f"  >>> NOT statistically significant (need >= 3sigma)")
    print(f"  >>> +{S_45:.3f} is BURIED in noise (sigma = {sig_45:.3f})")
else:
    print(f"  >>> STATISTICALLY SIGNIFICANT")

print()

# How many coincidences needed for 3sigma at alpha=45?
if S_45 > 0:
    N_needed = (3 * sig_45 / S_45)**2 * N_COINC
    print(f"  Coincidences needed for 3sigma: {N_needed:,.0f}")
    print(f"  That is {N_needed/N_COINC:.0f}x the Bong count ({N_COINC:,})")
else:
    print(f"  LF not even violated at this alpha/mu")

print()

# =================================================================
# Q2: PROPER OPTIMIZATION — JOINT FIGURE OF MERIT
# =================================================================

print("=" * 70)
print("QUESTION 2: Optimal alpha for BOTH K9_E AND LF significance")
print("=" * 70)
print()

print("Criterion: maximize min(n_sigma_LF, n_sigma_K9E)")
print("           subject to: both > 3sigma with N <= N_Bong")
print()

# For K9_E: the measurable deviation is delta<A1B2>
# delta = <A1B2>_K9E - <A1B2>_QM
# We need to compute this for each alpha and beta_k9

def compute_k9e_delta_correlator(mu, alpha_deg, beta_k9, x=1, y=2):
    """
    Compute delta<AxBy> = <AxBy>_K9E - <AxBy>_QM
    
    For mixed settings (x=1, y!=1):
    K9_E modifies the probability through f_perp on Bob's side.
    
    P_K9E(a=c, b | y=j) = sum_d P_QM(c, b, d | y=j) * [1 - beta*f_perp(b,d)] / Z
    
    where f_perp(b, d) = 1 - |<b|d>|^2
    
    For tilted measurement at polar angle alpha:
    f_perp(+1, H) = sin^2(alpha/2)
    f_perp(-1, H) = cos^2(alpha/2)
    f_perp(+1, V) = cos^2(alpha/2)
    f_perp(-1, V) = sin^2(alpha/2)
    """
    alpha = np.radians(alpha_deg)
    rho = make_rho(mu)
    
    # f_perp values
    f_perp = {
        (+1, +1): np.sin(alpha/2)**2,  # b=+1, d=H
        (-1, +1): np.cos(alpha/2)**2,  # b=-1, d=H
        (+1, -1): np.cos(alpha/2)**2,  # b=+1, d=V
        (-1, -1): np.sin(alpha/2)**2,  # b=-1, d=V
    }
    
    # QM correlator (standard)
    corr_qm = compute_correlator(rho, alpha_deg, x, y)
    
    # K9_E correlator: need full 4-outcome computation
    # P_K9E(a=c, b) = sum_d P_QM(c, d) * P(b|d, alpha) * [1 - beta*f_perp(b,d)] / Z
    
    # For x=1: Alice reads Friend, so a=c (z-basis)
    # For y=j: Bob reverses Debbie + measures at (alpha, phi_y)
    
    # Step 1: Compute P_QM(c, d) from rho (z-basis on both)
    P_cd = {}
    for c in [+1, -1]:
        for d in [+1, -1]:
            Pc = z_proj(c)
            Pd = z_proj(d)
            P_cd[(c,d)] = max(0, np.real(np.trace(np.kron(Pc, Pd) @ rho)))
    
    # Step 2: Compute P(b|d, alpha, phi_y) - Bob's measurement after reversal
    # This is |<b(alpha, phi_y) | d>|^2
    az_y = bob_phi[y]
    P_b_given_d = {}
    for b in [+1, -1]:
        for d in [+1, -1]:
            Pb = tilted_proj(az_y, alpha, b)
            d_state = np.array([1, 0], dtype=complex) if d == +1 else np.array([0, 1], dtype=complex)
            P_b_given_d[(b,d)] = max(0, np.real(d_state.conj() @ Pb @ d_state))
    
    # Step 3: Compute unnormalized K9_E probabilities
    P_k9e_unnorm = {}
    Z = 0
    for c in [+1, -1]:
        for b in [+1, -1]:
            val = 0
            for d in [+1, -1]:
                pqm = P_cd[(c,d)] * P_b_given_d[(b,d)]
                h = 1 - beta_k9 * f_perp[(b, d)]
                val += pqm * h
            P_k9e_unnorm[(c,b)] = val
            Z += val
    
    # Step 4: Normalize and compute correlator
    corr_k9e = 0
    for c in [+1, -1]:
        for b in [+1, -1]:
            corr_k9e += c * b * P_k9e_unnorm[(c,b)] / Z
    
    delta = corr_k9e - corr_qm
    return corr_qm, corr_k9e, delta

print("K9_E delta correlator for mixed settings (x=1, y=2):")
print()
print(f"{'alpha':>6s}  {'beta_k9':>8s}  {'<A1B2>_QM':>12s}  {'<A1B2>_K9E':>12s}  "
      f"{'delta':>10s}  {'sigma':>10s}  {'n_sigma_K9E':>12s}")
print("-" * 80)

for alpha_deg in [30, 35, 40, 45, 50, 60]:
    for beta_k9 in [0.3]:
        rho = make_rho(0.95)
        corr_qm, corr_k9e, delta = compute_k9e_delta_correlator(0.95, alpha_deg, beta_k9, x=1, y=2)
        sig_corr = sigma_correlator(corr_qm, N_COINC)
        nsig_k9e = abs(delta) / sig_corr if sig_corr > 0 else 0
        print(f"{alpha_deg:6d}  {beta_k9:8.1f}  {corr_qm:12.6f}  {corr_k9e:12.6f}  "
              f"{delta:10.6f}  {sig_corr:10.6f}  {nsig_k9e:12.1f}")

print()

# COMPREHENSIVE FIGURE OF MERIT TABLE
print("=" * 70)
print("JOINT FIGURE OF MERIT: min(n_sigma_LF, n_sigma_K9E)")
print("  mu=0.95, N=91000, beta_k9=0.3")
print("=" * 70)
print()

print(f"{'alpha':>6s}  {'S_LF1':>8s}  {'sig_LF':>8s}  {'n_sig_LF':>9s}  "
      f"{'delta_K9':>10s}  {'sig_K9':>8s}  {'n_sig_K9':>9s}  {'FOM':>8s}")
print("-" * 80)

best_fom = -999
best_alpha = 0
results = []

for alpha_deg in range(25, 75):
    rho = make_rho(0.95)
    
    # LF significance
    S_lf, sig_lf = genuine_lf_1_value_and_sigma(rho, alpha_deg, N_COINC)
    n_sig_lf = S_lf / sig_lf if sig_lf > 0 else -999
    
    # K9_E significance (using best testable correlator)
    best_delta = 0
    best_sig_k9 = 1
    for y in [2, 3]:
        _, _, delta = compute_k9e_delta_correlator(0.95, alpha_deg, 0.3, x=1, y=y)
        corr_qm = compute_correlator(rho, alpha_deg, 1, y)
        sig_k9 = sigma_correlator(corr_qm, N_COINC)
        if abs(delta) / sig_k9 > abs(best_delta) / best_sig_k9:
            best_delta = delta
            best_sig_k9 = sig_k9
    
    n_sig_k9 = abs(best_delta) / best_sig_k9 if best_sig_k9 > 0 else 0
    
    # FOM = min(n_sig_LF, n_sig_K9) — only if LF is violated
    if S_lf > 0:
        fom = min(n_sig_lf, n_sig_k9)
    else:
        fom = -abs(n_sig_lf)  # negative = LF not violated
    
    results.append((alpha_deg, S_lf, sig_lf, n_sig_lf, best_delta, best_sig_k9, n_sig_k9, fom))
    
    if fom > best_fom:
        best_fom = fom
        best_alpha = alpha_deg

# Print every 3 degrees + key points
for r in results:
    alpha_deg = r[0]
    if alpha_deg % 3 == 0 or alpha_deg == best_alpha or alpha_deg in [35, 45, 47]:
        S_lf, sig_lf, n_sig_lf = r[1], r[2], r[3]
        delta, sig_k9, n_sig_k9, fom = r[4], r[5], r[6], r[7]
        marker = " <<<" if alpha_deg == best_alpha else ""
        lf_note = "" if S_lf > 0 else " (no viol)"
        print(f"{alpha_deg:6d}  {S_lf:8.4f}  {sig_lf:8.4f}  {n_sig_lf:9.1f}  "
              f"{delta:10.6f}  {sig_k9:8.6f}  {n_sig_k9:9.1f}  {fom:8.1f}{marker}{lf_note}")

print()
print(f"OPTIMAL ALPHA = {best_alpha} deg (FOM = {best_fom:.1f})")
print()

# =================================================================
# Q3: WHAT DOES K9_E SIGNAL MEAN IN MEASURABLE UNITS?
# =================================================================

print("=" * 70)
print("QUESTION 3: K9_E signal in measurable quantities")
print("=" * 70)
print()

print("The '0.707' from K9-S11c was |cos(alpha)| = f_perp outcome-dependence.")
print("This is NOT directly measurable. The MEASURABLE quantity is:")
print()
print("  delta<A_x B_y> = <A_x B_y>_K9E - <A_x B_y>_QM")
print()
print("This depends on alpha AND beta_k9 (K9_E coupling strength).")
print()

print("ACTUAL MEASURABLE DELTAS (mu=0.95):")
print()
print(f"{'alpha':>6s}  {'beta_k9':>8s}  {'(x,y)':>6s}  {'<AB>_QM':>10s}  {'<AB>_K9E':>10s}  "
      f"{'delta':>10s}  {'delta%':>8s}  {'sigma':>8s}  {'n_sigma':>8s}")
print("-" * 85)

for alpha_deg in [35, 45]:
    for beta_k9 in [0.1, 0.3, 0.5]:
        for x, y in [(1,2), (1,3), (2,1), (3,1)]:
            rho = make_rho(0.95)
            
            # Swap sides for (2,1) and (3,1)
            if x != 1:
                # Symmetric: compute delta for (y=1, x=setting) on Bob's side
                corr_qm, corr_k9e, delta = compute_k9e_delta_correlator(
                    0.95, alpha_deg, beta_k9, x=1, y=x)
                # Symmetric, so same magnitude
            else:
                corr_qm, corr_k9e, delta = compute_k9e_delta_correlator(
                    0.95, alpha_deg, beta_k9, x=x, y=y)
            
            sig = sigma_correlator(corr_qm, N_COINC)
            delta_pct = (delta / corr_qm * 100) if abs(corr_qm) > 1e-6 else float('inf')
            nsig = abs(delta) / sig if sig > 0 else 0
            
            print(f"{alpha_deg:6d}  {beta_k9:8.1f}  ({x},{y})  {corr_qm:10.4f}  {corr_k9e:10.4f}  "
                  f"{delta:10.6f}  {delta_pct:7.1f}%  {sig:8.4f}  {nsig:8.1f}")
    print()

print()
print("KEY TAKEAWAY:")
print(f"  At alpha=45, beta_k9=0.3: delta<A1B2> = {compute_k9e_delta_correlator(0.95, 45, 0.3, 1, 2)[2]:.6f}")
print(f"  At alpha=35, beta_k9=0.3: delta<A1B2> = {compute_k9e_delta_correlator(0.95, 35, 0.3, 1, 2)[2]:.6f}")
print()

# =================================================================
# FINAL SUMMARY
# =================================================================

print("=" * 70)
print("FINAL SUMMARY: Three Answers")
print("=" * 70)
print()

# Re-compute at best alpha
rho = make_rho(0.95)
S_best, sig_best = genuine_lf_1_value_and_sigma(rho, best_alpha, N_COINC)
n_best_lf = S_best / sig_best
_, _, delta_best = compute_k9e_delta_correlator(0.95, best_alpha, 0.3, 1, 2)
sig_k9_best = sigma_correlator(compute_correlator(rho, best_alpha, 1, 2), N_COINC)
n_best_k9 = abs(delta_best) / sig_k9_best

print(f"Q1: Is +0.022 at alpha=45 significant?")
print(f"    NO. sigma(S_LF1) = {sig_45:.4f}, significance = {nsig_45:.1f}sigma")
print(f"    +0.022 is BURIED in experimental noise.")
print()
print(f"Q2: Better alpha?")
print(f"    OPTIMAL alpha = {best_alpha} deg")
print(f"    FOM = min(n_sig_LF, n_sig_K9E) = {best_fom:.1f}")
print(f"    Gen LF 1 = {S_best:+.4f} ({n_best_lf:.1f}sigma)")
print(f"    delta<A1B2> = {delta_best:.6f} ({n_best_k9:.1f}sigma)")
print()
print(f"Q3: K9_E signal in measurable units (alpha={best_alpha}, beta=0.3):")
print(f"    delta<A1B2> = {delta_best:.6f}")
print(f"    This is the ACTUAL change in the correlator that")
print(f"    an experiment would need to resolve.")
print()

# Can EITHER be detected with N_Bong?
if n_best_lf >= 3 and n_best_k9 >= 3:
    print("VERDICT: BOTH LF and K9_E detectable with Bong statistics.")
elif n_best_lf >= 3 or n_best_k9 >= 3:
    winner = "LF" if n_best_lf > n_best_k9 else "K9_E"
    loser = "K9_E" if winner == "LF" else "LF"
    print(f"VERDICT: {winner} detectable, {loser} NOT with Bong statistics.")
else:
    print("VERDICT: NEITHER LF nor K9_E detectable with N=91,000.")
    
    # How much N needed?
    if S_best > 0 and abs(delta_best) > 0:
        N_lf_3sig = int((3 * sig_best / S_best)**2 * N_COINC) if S_best > 0 else float('inf')
        N_k9_3sig = int((3 * sig_k9_best / abs(delta_best))**2 * N_COINC)
        N_both = max(N_lf_3sig, N_k9_3sig)
        print(f"  For 3sigma LF:  N = {N_lf_3sig:>15,}")
        print(f"  For 3sigma K9E: N = {N_k9_3sig:>15,}")
        print(f"  For BOTH:       N = {N_both:>15,} ({N_both/N_COINC:.0f}x Bong)")
