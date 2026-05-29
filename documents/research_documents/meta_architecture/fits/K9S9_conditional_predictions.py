"""
K9S9_conditional_predictions.py — First genuine K-space numerical predictions.

Computes P(o_F, o_W | o_FA, K-space) using K9_E-JC (P9-JC formulation)
from K9S8_composition_law.md.

KEY: The Marginalization Cancellation Theorem (K9-S8) proves that
MARGINAL correlators = QM for all beta. But CONDITIONAL correlators
(conditioned on Friend's outcome o_FA) ARE distinguishable.

This script computes those conditional correlators.
"""

import numpy as np

# ============================================================
# SECTION 1: QM SINGLET CONDITIONAL PROBABILITIES
# ============================================================

def qm_singlet_conditional_prob(o_W, theta_W, o_FA, theta_FA):
    """
    P_QM(o_W | o_FA, theta_W, theta_FA) for singlet state.
    
    After Friend measures at angle theta_FA and gets outcome o_FA,
    the conditional state for Wigner's photon is:
        |psi_post> = (known from singlet anti-correlation)
    
    For singlet |psi> = (|01> - |10>)/sqrt(2):
        P(o_W=+1 | o_FA=+1) = sin^2((theta_W - theta_FA)/2)
        P(o_W=-1 | o_FA=+1) = cos^2((theta_W - theta_FA)/2)
        P(o_W=+1 | o_FA=-1) = cos^2((theta_W - theta_FA)/2)
        P(o_W=-1 | o_FA=-1) = sin^2((theta_W - theta_FA)/2)
    """
    delta_theta = (theta_W - theta_FA) / 2
    sin2 = np.sin(delta_theta)**2
    cos2 = np.cos(delta_theta)**2
    
    if o_FA == +1:
        return sin2 if o_W == +1 else cos2
    else:  # o_FA == -1
        return cos2 if o_W == +1 else sin2


def qm_conditional_expectation(theta_W, theta_FA, o_FA):
    """
    <B_y | o_FA> = sum_b b * P(o_W=b | o_FA)
    """
    p_plus = qm_singlet_conditional_prob(+1, theta_W, o_FA, theta_FA)
    p_minus = qm_singlet_conditional_prob(-1, theta_W, o_FA, theta_FA)
    return (+1) * p_plus + (-1) * p_minus


# ============================================================
# SECTION 2: K9_E-JC CONDITIONAL PROBABILITIES
# ============================================================

def k9e_jc_conditional_prob(o_W, theta_W, o_FA, theta_FA, beta, setting_x):
    """
    P_K9E(o_W | o_FA, theta_W, theta_FA, beta) using P9-JC formulation.
    
    For setting_x = 0 (Wigner reads Friend): no BSM, no perp_K -> Born rule
    For setting_x = 1 (Wigner does BSM): perp_K fires -> suppression
    
    K9_E-JC:
        P(o_W | o_FA) = P_QM(o_W | o_FA) * h(o_W, o_FA) / Z
        h(o_W, o_FA) = 1 - beta * f_perp(o_W, o_FA)
        f_perp(o_W, o_FA) = delta(o_W, o_FA)  [1 if same, 0 if different]
        Z = sum_b P_QM(b | o_FA) * h(b, o_FA)
    """
    if setting_x == 0 or beta == 0:
        return qm_singlet_conditional_prob(o_W, theta_W, o_FA, theta_FA)
    
    # Compute QM conditional probabilities
    p_qm = {}
    for b in [+1, -1]:
        p_qm[b] = qm_singlet_conditional_prob(b, theta_W, o_FA, theta_FA)
    
    # f_perp: delta(o_W, o_FA) — suppress outcomes matching Friend's
    def f_perp(b):
        return 1.0 if b == o_FA else 0.0
    
    # h factors
    h = {b: 1.0 - beta * f_perp(b) for b in [+1, -1]}
    
    # Normalization
    Z = sum(p_qm[b] * h[b] for b in [+1, -1])
    
    if Z <= 0:
        raise ValueError(f"Z = {Z} <= 0. beta = {beta} too large.")
    
    return p_qm[o_W] * h[o_W] / Z


def k9e_conditional_expectation(theta_W, theta_FA, o_FA, beta, setting_x):
    """
    <B_y | o_FA>_K9E = sum_b b * P_K9E(o_W=b | o_FA)
    """
    p_plus = k9e_jc_conditional_prob(+1, theta_W, o_FA, theta_FA, beta, setting_x)
    p_minus = k9e_jc_conditional_prob(-1, theta_W, o_FA, theta_FA, beta, setting_x)
    return (+1) * p_plus + (-1) * p_minus


# ============================================================
# SECTION 3: PROIETTI ANGLES AND COMPUTATION
# ============================================================

# Proietti angles (from supplementary Eq. S7)
# Alice: A0 = 0, A1 = pi/2
# Bob: B0 = pi/4, B1 = -pi/4
# Friends measure at: FA = 0 (Alice's friend), FB = 0 (Bob's friend)

theta_FA = 0.0       # Friend Alice measures at 0
theta_FB = 0.0       # Friend Bob measures at 0
theta_A = [0.0, np.pi/2]   # Alice settings: x=0, x=1
theta_B = [np.pi/4, -np.pi/4]  # Bob settings: y=0, y=1

print("=" * 70)
print("K9-S9: CONDITIONAL CORRELATOR PREDICTIONS")
print("First genuine numerical predictions from K-space")
print("=" * 70)

print("\n--- QM vs K9_E conditional expectations ---")
print("Format: <B_y | o_FA>_QM vs <B_y | o_FA>_K9E(beta)")
print()

# For each Alice setting and Bob setting
results = {}
for xi, x in enumerate([0, 1]):
    for yi, y in enumerate([0, 1]):
        theta_a = theta_A[xi]
        theta_b = theta_B[yi]
        
        # Determine which angle Friend measured at
        # In Proietti: Friend measures at same basis as projective setting
        theta_f = theta_FA  # Friend Alice's angle
        
        # Setting x determines if BSM fires
        setting_x = x  # x=1 means Alice does BSM
        
        print(f"Setting (x={x}, y={y}): theta_A={theta_a:.3f}, theta_B={theta_b:.3f}")
        
        for o_fa in [+1, -1]:
            qm_val = qm_conditional_expectation(theta_b, theta_f, o_fa)
            
            print(f"  o_FA = {o_fa:+d}:")
            print(f"    QM:         <B|o_FA>  = {qm_val:+.6f}")
            
            for beta in [0.1, 0.3, 0.5, 0.7, 0.9]:
                k9e_val = k9e_conditional_expectation(
                    theta_b, theta_f, o_fa, beta, setting_x
                )
                delta = k9e_val - qm_val
                print(f"    K9E(beta={beta}): <B|o_FA> = {k9e_val:+.6f}  "
                      f"delta = {delta:+.6f}")
            
            results[(x, y, o_fa)] = {
                'qm': qm_val,
                'k9e': {beta: k9e_conditional_expectation(
                    theta_b, theta_f, o_fa, beta, setting_x
                ) for beta in [0.1, 0.3, 0.5, 0.7, 0.9]}
            }
        print()

# ============================================================
# SECTION 4: SUMMARY TABLE
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY: delta = <B|o_FA>_K9E - <B|o_FA>_QM  at beta = 0.3")
print("=" * 70)
print()
print(f"{'Setting':>10} {'o_FA':>5} {'QM':>10} {'K9E(0.3)':>10} {'delta':>10} {'|d|/QM':>10}")
print("-" * 60)

beta_show = 0.3
for x in [0, 1]:
    for y in [0, 1]:
        for o_fa in [+1, -1]:
            qm = results[(x, y, o_fa)]['qm']
            k9e = results[(x, y, o_fa)]['k9e'][beta_show]
            delta = k9e - qm
            rel = abs(delta / qm) if abs(qm) > 1e-10 else 0
            print(f"  (x={x},y={y}) {o_fa:+d}  {qm:+.6f} {k9e:+.6f} {delta:+.6f} {rel:.4f}")

# ============================================================
# SECTION 5: PROBABILITY TABLE
# ============================================================

print("\n" + "=" * 70)
print("PROBABILITY TABLE: P(o_W | o_FA) at beta = 0.3, setting x=1")
print("=" * 70)
print()

beta_p = 0.3
for yi, y in enumerate([0, 1]):
    theta_b = theta_B[yi]
    print(f"Bob setting y={y} (theta_B = {theta_b:.4f}):")
    for o_fa in [+1, -1]:
        print(f"  o_FA = {o_fa:+d}:")
        for o_w in [+1, -1]:
            p_qm = qm_singlet_conditional_prob(o_w, theta_b, o_fa, theta_FA)
            p_k9e = k9e_jc_conditional_prob(o_w, theta_b, o_fa, theta_FA, beta_p, 1)
            delta_p = p_k9e - p_qm
            print(f"    P(o_W={o_w:+d}): QM={p_qm:.6f}, K9E={p_k9e:.6f}, "
                  f"dP={delta_p:+.6f}")
    print()

# ============================================================
# SECTION 6: NORMALIZATION VERIFICATION
# ============================================================

print("=" * 70)
print("NORMALIZATION CHECK")
print("=" * 70)
for beta_c in [0.1, 0.3, 0.5, 0.9]:
    for o_fa in [+1, -1]:
        total = sum(
            k9e_jc_conditional_prob(b, theta_B[0], o_fa, theta_FA, beta_c, 1)
            for b in [+1, -1]
        )
        status = "PASS" if abs(total - 1.0) < 1e-12 else "FAIL"
        print(f"  beta={beta_c}, o_FA={o_fa:+d}: Sum P = {total:.15f} [{status}]")

print()
print("=" * 70)
print("K9-S9 COMPLETE: First genuine numerical predictions from K-space.")
print("=" * 70)
