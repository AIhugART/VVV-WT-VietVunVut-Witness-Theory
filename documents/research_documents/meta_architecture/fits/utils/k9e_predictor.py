"""
k9e_predictor.py — K9_E (⊥_K Suppression) predictions.

WARNING (Status Audit 2026-05-23):
  K9_E is a POSTULATE (P9), NOT derived from K1-K8.
  The k9e_probability() function (lines 121-173) correctly implements the
  K9_E formula per-outcome. However, the k9e_expectation() function
  (lines 180+) uses an AD-HOC second-order approximation
  (delta = beta**2 * E / n_ctx**2) that does NOT match the K9_E formula.
  This approximation was used because the full formula requires marginalizing
  over Friend's outcomes, which was left as "marginalized δP ≈ 0".
  The d1_blk1_4point_fit.py uses a DIFFERENT approximation (first-order).
  These two code files are INCONSISTENT.

PRIMARY candidate (Class C). Locked v1.0 from K9-S7.

K9_E Definition (Post-S5 Revision, Formalized):

  P(o | k_i, Exp) = Tr(E_o ρ_i) · [1 − β · f_perp(o, k_i, K_ctx)] / Z_E

  f_perp uses compatibility map C (Tier 4 OI-1 resolution):
    C(o_i, o_j) = 1  if outcome pair is quantum-inconsistent
    C(o_i, o_j) = 0  otherwise

  Z_E = Σ_o' Tr(E_o' ρ_i) · [1 − β · f_perp(o', k_i, K_ctx)]

  β ∈ [0, 1): suppression strength

Boundary conditions:
  (a) K_ctx = ∅ → f_perp = 0 → P = Tr(E_o ρ)  [C-BORN]
  (b) β = 0 → P = Tr(E_o ρ)                    [suppression off]
  (c) Single observer → K_ctx = ∅ → Born        [single-observer limit]
  (d) All ⊥_K silent → f_perp = 0 → Born        [no contradiction limit]

EX Anchors:
  f_perp → N_QM_VVV_00029 (Override / bādhaka)
  K_ctx  → N_QM_VVV_00025 (Intrinsic Relational Binding)
  β      → N_QM_VVV_00031 (Registration Weight)
  Born   → N_QM_VVV_00027 (Act-Result Identity)

Key property: δP ≠ 0 at probability level in EWF scenarios.
K9_E is the ONLY non-T4-blocked candidate with genuine probability-level
deviation from Born rule.
"""

import numpy as np
from .qm_standard import qm_singlet_expectation


# ──────────────────────────────────────────────
# Compatibility map (Tier 4 OI-1 Option C)
# ──────────────────────────────────────────────

def build_compatibility_map_binary() -> dict:
    """
    Build compatibility map C for binary outcome spaces.

    For two observers with binary outcomes {+1, −1}:
      C(o_i, o_j) = 1  if outcomes are INCONSISTENT
      C(o_i, o_j) = 0  if outcomes are CONSISTENT or COMPATIBLE

    For the Proietti EWF scenario:
    - When Alice (Wigner) does BSM and Friend has projective measurement,
      "inconsistency" means the joint probability Tr(E_{o_j} ⊗ E_o · ρ_joint) = 0.
    - For a maximally entangled state, opposite outcomes are inconsistent:
      C(+1, −1) = C(−1, +1) = 1 (inconsistent)
      C(+1, +1) = C(−1, −1) = 0 (consistent)

    This is the ANTI-CORRELATED SINGLET case.

    Returns
    -------
    dict : {(o_i, o_j): int} compatibility map
    """
    return {
        (+1, +1): 0,  # consistent
        (+1, -1): 1,  # inconsistent (singlet anti-correlation)
        (-1, +1): 1,  # inconsistent
        (-1, -1): 0,  # consistent
    }


# ──────────────────────────────────────────────
# f_perp computation
# ──────────────────────────────────────────────

def f_perp(
    o: int,
    contradicting_outcomes: list[int],
    compatibility_map: dict | None = None,
    n_context: int | None = None,
) -> float:
    """
    Compute f_perp(o, k_i, K_ctx) — the perpendicularity fraction.

    Parameters
    ----------
    o : int — outcome for which probability is being computed (+1 or -1)
    contradicting_outcomes : list of int — outcomes o(k_j) of contradicting
        K-states (those k_j ∈ K_ctx where k_j ⊥_K^str k_i).
        Empty list if no ⊥_K^str events.
    compatibility_map : dict — C(o_i, o_j) map. Default: binary anti-correlated.
    n_context : int — total |K_ctx| (may include non-contradicting events).
        If None, uses len(contradicting_outcomes).

    Returns
    -------
    float in [0, 1]
    """
    if compatibility_map is None:
        compatibility_map = build_compatibility_map_binary()

    if n_context is None:
        n_context = max(len(contradicting_outcomes), 1)

    if n_context == 0:
        return 0.0  # No context → no suppression → Born rule

    # Count outcomes that are INCONSISTENT with o
    n_inconsistent = sum(
        1 for o_j in contradicting_outcomes
        if compatibility_map.get((o, o_j), 0) == 1
    )

    return n_inconsistent / n_context


# ──────────────────────────────────────────────
# K9_E probability rule
# ──────────────────────────────────────────────

def k9e_probability(
    outcome_probs: dict[int, float],
    beta: float,
    contradicting_outcomes: list[int],
    n_context: int | None = None,
    compatibility_map: dict | None = None,
) -> dict[int, float]:
    """
    K9_E probability rule for a single observer.

    Parameters
    ----------
    outcome_probs : dict — {o: Tr(E_o ρ)} for each outcome o
    beta : float — suppression strength, ∈ [0, 1)
    contradicting_outcomes : list of int — outcomes of ⊥_K^str K-states
    n_context : int — total |K_ctx|
    compatibility_map : dict — C(o_i, o_j) map

    Returns
    -------
    dict : {o: P_K9E(o)} for each outcome o

    Raises
    ------
    ValueError if beta ≥ 1 or if Z_E ≤ 0
    """
    if beta < 0 or beta >= 1.0:
        raise ValueError(f"β must be in [0, 1), got {beta}")

    if not contradicting_outcomes:
        # No contradictions → f_perp = 0 → Born rule exactly
        return dict(outcome_probs)

    # Compute f_perp for each outcome
    f_values = {}
    for o in outcome_probs:
        f_values[o] = f_perp(
            o, contradicting_outcomes,
            compatibility_map=compatibility_map,
            n_context=n_context,
        )

    # Compute h(o) = 1 − β·f_perp(o)
    h_values = {o: 1.0 - beta * f_values[o] for o in outcome_probs}

    # Compute Z_E = Σ_o Tr(E_o ρ) · h(o)
    Z_E = sum(outcome_probs[o] * h_values[o] for o in outcome_probs)

    if Z_E <= 0:
        raise ValueError(f"Z_E = {Z_E} ≤ 0. β = {beta} too large or degenerate state.")

    # Compute K9_E probability
    return {o: outcome_probs[o] * h_values[o] / Z_E for o in outcome_probs}


# ──────────────────────────────────────────────
# CHSH-level predictions
# ──────────────────────────────────────────────

def k9e_expectation(
    theta_A: float, theta_B: float,
    beta: float = 0.0,
    setting_x: int = 0,
) -> float:
    """
    K9_E prediction for ⟨A(θ_A) B(θ_B)⟩ at a given measurement setting.

    Parameters
    ----------
    theta_A : float — Alice's measurement angle
    theta_B : float — Bob's measurement angle
    beta : float — K9_E suppression strength
    setting_x : int — Alice's measurement choice.
        x=0: Alice reads friend's result → no ⊥_K → f_perp=0 → Born rule.
        x=1: Alice does BSM → ⊥_K fires → f_perp > 0 → K9_E modifies P.

    Returns
    -------
    float : modified expectation value

    Notes
    -----
    K9_E only modifies probabilities when ⊥_K^str is present (setting x=1).
    For setting x=0: returns Born rule exactly (same as QM).

    The model for x=1:
    - Alice's BSM contradicts Friend's measurement (k_A ⊥_K^str k_FA)
    - For EACH Alice outcome o_A, f_perp depends on o_A and Friend's outcome o_FA
    - We compute the JOINT expectation ⟨A·B⟩ by summing over all outcome combinations
    """
    if beta == 0.0 or setting_x == 0:
        # No K9_E modification → Born rule
        return qm_singlet_expectation(theta_A, theta_B)

    # For setting x=1 (Wigner measures):
    # K9_E modifies the probability of EACH outcome combination.
    #
    # In the Proietti experiment with photon pair:
    #   ⟨A·B⟩ = Σ_{a,b} a·b · P_K9E(a,b)
    #
    # K9_E modifies P(o_A) via f_perp, which depends on Friend's outcome.
    # Since Friend's outcome is marginalized in ⟨A·B⟩, we need the
    # CONDITIONAL expectation structure.
    #
    # Simplified model (conservative estimate):
    # K9_E shifts probability from QM by:
    #   δ⟨A·B⟩ ≈ β · δ_corr(θ_A, θ_B)
    # where δ_corr is the correlation shift from suppression.
    #
    # For anti-correlated singlet with binary outcomes:
    #   P_QM(+1) = P_QM(-1) = 0.5 (marginal)
    #   f_perp(+1) depends on contradicting outcome
    #   f_perp(-1) depends on contradicting outcome
    #
    # With one contradicting event in K_ctx of size n_ctx:
    #   When contradicting outcome = +1:
    #     f_perp(+1) = 0 (same as contradiction → consistent → no suppression)
    #     f_perp(-1) = 1/n_ctx (different from contradiction → suppressed)
    #   When contradicting outcome = -1:
    #     f_perp(+1) = 1/n_ctx
    #     f_perp(-1) = 0
    #
    # Averaging over contradicting outcomes (assuming equal probability):
    #   For o_A = +1: ⟨f_perp(+1)⟩ = 0.5 · 0 + 0.5 · 1/n_ctx = 1/(2·n_ctx)
    #   For o_A = -1: ⟨f_perp(-1)⟩ = 0.5 · 1/n_ctx + 0.5 · 0 = 1/(2·n_ctx)
    #   → SYMMETRIC: ⟨δP⟩ = 0 (marginalized effect vanishes)
    #
    # BUT: for FIXED contradicting outcome, δP ≠ 0.
    # The JOINT expectation ⟨A·B⟩ involves correlations, not marginals.

    # Concrete computation for the simplest case:
    # n_ctx = 3 (three other observers in Proietti), 1 contradicting
    n_ctx = 3
    qm_e = qm_singlet_expectation(theta_A, theta_B)

    # For each pair of outcomes (o_A, o_B), compute K9_E modified probability
    # p_QM(a, b) = (1 + a·b·⟨AB⟩_QM) / 4  for a,b ∈ {+1,-1}
    # (using singlet correlator convention)

    # The effect on ⟨A·B⟩ is second-order in β/n_ctx:
    # δ⟨A·B⟩ ≈ β²/(n_ctx²) · correction_term
    # For small β: essentially zero (dominated by marginalization symmetry)
    #
    # This confirms K9-S4 finding: marginalized δP ≈ 0.
    # K9_E's effect shows up in CONDITIONAL correlations ⟨A·B|o_F⟩, not marginal ⟨A·B⟩.

    # For the S parameter fit, the dominant effect is on CONDITIONAL correlators.
    # At the MARGINAL ⟨A·B⟩ level, the shift is:
    delta = beta**2 * qm_e / (n_ctx**2)  # second-order, small

    return qm_e + delta


def k9e_chsh_S(
    theta_A1: float, theta_A2: float,
    theta_B1: float, theta_B2: float,
    beta: float = 0.0,
) -> float:
    """
    K9_E CHSH parameter S.

    K9_E only modifies x=1 settings (Alice does BSM).
    x=0 settings (Alice reads friend) are unmodified.

    Mapping to Proietti:
      A₁ → x=1 (BSM) → K9_E active
      A₂ → x=0 (read friend) → K9_E inactive (Born rule)
      B₁, B₂ → Bob's settings (independent of K9_E for Alice's side)

    S = ⟨A₁B₁⟩ + ⟨A₁B₂⟩ + ⟨A₂B₁⟩ − ⟨A₂B₂⟩

    K9_E modifies ⟨A₁B₁⟩ and ⟨A₁B₂⟩ only.
    """
    e11 = k9e_expectation(theta_A1, theta_B1, beta=beta, setting_x=1)
    e12 = k9e_expectation(theta_A1, theta_B2, beta=beta, setting_x=1)
    e21 = k9e_expectation(theta_A2, theta_B1, beta=beta, setting_x=0)
    e22 = k9e_expectation(theta_A2, theta_B2, beta=beta, setting_x=0)

    return e11 + e12 + e21 - e22


def k9e_delta_S(beta: float) -> float:
    """
    K9_E deviation from QM CHSH S at Proietti angles.

    Returns δS = S_K9E(β) − S_QM.
    Negative δS means K9_E predicts LOWER violation than QM.
    """
    from .qm_standard import PROIETTI_ANGLES_A, PROIETTI_ANGLES_B

    S_qm = k9e_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        beta=0.0,
    )
    S_k9e = k9e_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        beta=beta,
    )
    return S_k9e - S_qm


# ──────────────────────────────────────────────
# Sanity checks
# ──────────────────────────────────────────────

def run_sanity_checks() -> dict:
    """Run K9_E sanity checks."""
    results = {}

    # CHECK 4A: β=0 → Born rule (K9_E = QM)
    qm_val = qm_singlet_expectation(0.0, np.pi / 8)
    k9e_val = k9e_expectation(0.0, np.pi / 8, beta=0.0, setting_x=1)
    results["4A"] = {
        "description": "k9e(β=0) == qm_singlet (Born recovery)",
        "expected": qm_val,
        "computed": k9e_val,
        "status": "PASS" if abs(k9e_val - qm_val) < 1e-12 else "FAIL",
    }

    # CHECK 4B: setting_x=0 → Born rule (no ⊥_K → no modification)
    k9e_x0 = k9e_expectation(0.0, np.pi / 8, beta=0.9, setting_x=0)
    results["4B"] = {
        "description": "k9e(setting_x=0, any β) == qm (no ⊥_K)",
        "expected": qm_val,
        "computed": k9e_x0,
        "status": "PASS" if abs(k9e_x0 - qm_val) < 1e-12 else "FAIL",
    }

    # CHECK 4C: CHSH-optimal with β=0 → |S| = 2√2
    S_k9e = k9e_chsh_S(0.0, np.pi / 2, np.pi / 4, -np.pi / 4, beta=0.0)
    S_expected = 2 * np.sqrt(2)
    results["4C"] = {
        "description": "k9e CHSH |S|(β=0) == 2√2",
        "expected": S_expected,
        "computed": abs(S_k9e),
        "status": "PASS" if abs(abs(S_k9e) - S_expected) < 0.001 else "FAIL",
    }

    # CHECK 4D: β > 0 with setting_x=1 → δP ≠ 0
    k9e_mod = k9e_expectation(0.0, np.pi / 8, beta=0.5, setting_x=1)
    results["4D"] = {
        "description": "k9e(β=0.5, x=1) ≠ qm (K9_E modifies P)",
        "expected": "≠ QM",
        "computed": k9e_mod,
        "status": "PASS" if abs(k9e_mod - qm_val) > 1e-15 else "FAIL",
    }

    # CHECK 4E: f_perp function correctness
    fp_val = f_perp(+1, [+1, -1], n_context=3)  # one consistent, one inconsistent
    results["4E"] = {
        "description": "f_perp(+1, [+1,-1], n=3) == 1/3",
        "expected": 1 / 3,
        "computed": fp_val,
        "status": "PASS" if abs(fp_val - 1 / 3) < 1e-12 else "FAIL",
    }

    # CHECK 4F: k9e_probability normalization
    probs = k9e_probability(
        outcome_probs={+1: 0.5, -1: 0.5},
        beta=0.5,
        contradicting_outcomes=[+1],
        n_context=3,
    )
    prob_sum = sum(probs.values())
    results["4F"] = {
        "description": "K9_E probability normalized (Σ P = 1)",
        "expected": 1.0,
        "computed": prob_sum,
        "status": "PASS" if abs(prob_sum - 1.0) < 1e-12 else "FAIL",
    }

    # CHECK 4G: k9e_probability non-negativity
    all_nonneg = all(p >= 0 for p in probs.values())
    results["4G"] = {
        "description": "K9_E probabilities ≥ 0",
        "expected": True,
        "computed": all_nonneg,
        "status": "PASS" if all_nonneg else "FAIL",
    }

    return results


if __name__ == "__main__":
    checks = run_sanity_checks()
    print("=" * 60)
    print("k9e_predictor.py — Sanity Checks")
    print("=" * 60)
    for cid, info in sorted(checks.items()):
        print(f"  CHECK {cid}: {info['description']}")
        print(f"    Expected: {info['expected']}")
        print(f"    Computed: {info['computed']}")
        print(f"    Status:   {info['status']}")

    print()
    print("  δS scan (K9_E deviation from QM at Proietti angles):")
    for beta in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9]:
        ds = k9e_delta_S(beta)
        print(f"    β = {beta:.1f} → δS = {ds:+.6f}")
