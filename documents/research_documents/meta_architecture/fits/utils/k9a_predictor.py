"""
k9a_predictor.py — K9_A (V-Filter) predictions.

FALLBACK candidate (Class D). Locked v2.0 from PP-1 v2.

K9_A Definition (Three-Case, EX-Enriched):
  Case 1: V(k)=1 ∧ ¬isNull → P(o|k) = Tr(E_o ρ)  [Born Rule]
  Case 2: V(k)=0 ∧ ¬isNull → No P assignment        [Bhrānti]
  Case 3: isNull            → No P assignment        [Anupalabdhi]

Free parameter: v_rate ∈ [0,1] (fraction of runs with V=1)

Key property: δP = 0 at probability level for all V=1 events.
Distinguishability is at registration/statistical level only.

EX Anchors:
  V=1 → N_QM_VVV_00027 (arthakriyā → Born Rule)
  V=0 → N_QM_VVV_00032 (Bhrānti)
  isNull → N_QM_VVV_00020 (Anupalabdhi)
"""

import numpy as np
from .qm_standard import qm_singlet_expectation, qm_chsh_S as _qm_S


def k9a_expectation(
    theta_A: float, theta_B: float,
    v_rate: float = 1.0
) -> float | None:
    """
    K9_A prediction for ⟨A(θ_A) B(θ_B)⟩.

    Parameters
    ----------
    theta_A : float — Alice's measurement angle (radians)
    theta_B : float — Bob's measurement angle (radians)
    v_rate : float — fraction of runs with V=1 (registered).
             Range: [0, 1]. Default 1.0 = all runs registered.

    Returns
    -------
    float : expectation value (same as QM when v_rate > 0)
    None  : if v_rate = 0 (no registered events)

    Notes
    -----
    K9_A predicts P(o|k) = Tr(E_o ρ) for ALL V=1 events.
    Therefore ⟨A_xB_y⟩ computed from V=1 events equals the QM value,
    UNLESS V=0 events introduce selection bias (PP-1 v2 Channel 3).

    For this predictor, we assume NO selection bias (v_rate uniform
    across all settings). With selection bias, use k9a_biased_expectation.
    """
    if v_rate <= 0.0:
        return None
    if v_rate > 1.0:
        raise ValueError(f"v_rate must be in [0,1], got {v_rate}")

    # K9_A Case 1: V=1 events give Born rule exactly
    # Expectation from V=1 subset = QM expectation (no bias assumed)
    return qm_singlet_expectation(theta_A, theta_B)


def k9a_chsh_S(
    theta_A1: float, theta_A2: float,
    theta_B1: float, theta_B2: float,
    v_rate: float = 1.0
) -> float | None:
    """
    K9_A CHSH parameter S.

    With no selection bias: S_K9A = S_QM for any v_rate > 0.
    K9_A is Class D: δS = 0 at probability level.

    Returns None if v_rate = 0.
    """
    if v_rate <= 0.0:
        return None
    if v_rate > 1.0:
        raise ValueError(f"v_rate must be in [0,1], got {v_rate}")

    return _qm_S(theta_A1, theta_A2, theta_B1, theta_B2)


def k9a_effective_N(N_total: int, v_rate: float) -> int:
    """
    Effective sample size after V-filtering.

    N_eff = v_rate × N_total (events contributing to probability estimation).
    The remaining (1 - v_rate) × N_total events are Bhrānti or Anupalabdhi.

    Returns
    -------
    int : effective sample size (rounded down)
    """
    if v_rate < 0.0 or v_rate > 1.0:
        raise ValueError(f"v_rate must be in [0,1], got {v_rate}")
    return int(np.floor(N_total * v_rate))


def k9a_registration_observables(
    N_total: int, v_rate: float, null_rate: float = 0.0
) -> dict:
    """
    K9_A registration-layer observables (not probability-level).

    Parameters
    ----------
    N_total : int — total runs
    v_rate : float — fraction with V=1
    null_rate : float — fraction with isNull (subset of 1-v_rate)

    Returns
    -------
    dict with N_valid, N_bhranti, N_null
    """
    if null_rate > (1.0 - v_rate):
        raise ValueError("null_rate cannot exceed 1 - v_rate")

    N_valid = int(np.floor(N_total * v_rate))
    N_null = int(np.floor(N_total * null_rate))
    N_bhranti = N_total - N_valid - N_null

    return {
        "N_valid": N_valid,
        "N_bhranti": N_bhranti,
        "N_null": N_null,
        "v_rate": v_rate,
        "null_rate": null_rate,
        "bhranti_rate": 1.0 - v_rate - null_rate,
    }


# ──────────────────────────────────────────────
# Sanity checks
# ──────────────────────────────────────────────

def run_sanity_checks() -> dict:
    """Run K9_A sanity checks."""
    results = {}

    # CHECK 3A: v_rate=1.0 → equals QM
    qm_val = qm_singlet_expectation(0.0, np.pi / 8)
    k9a_val = k9a_expectation(0.0, np.pi / 8, v_rate=1.0)
    results["3A"] = {
        "description": "k9a(v_rate=1.0) == qm_singlet",
        "expected": qm_val,
        "computed": k9a_val,
        "status": "PASS" if k9a_val is not None and abs(k9a_val - qm_val) < 1e-12 else "FAIL",
    }

    # CHECK 3B: v_rate=0.0 → no division by zero
    k9a_zero = k9a_expectation(0.0, np.pi / 8, v_rate=0.0)
    results["3B"] = {
        "description": "k9a(v_rate=0.0) → None (no div/0)",
        "expected": None,
        "computed": k9a_zero,
        "status": "PASS" if k9a_zero is None else "FAIL",
    }

    # CHECK 3C: CHSH-optimal with v_rate=1.0 -> |S| = 2sqrt2
    S_k9a = k9a_chsh_S(0.0, np.pi / 2, np.pi / 4, -np.pi / 4, v_rate=1.0)
    S_expected = 2 * np.sqrt(2)
    results["3C"] = {
        "description": "k9a CHSH |S|(v_rate=1.0) == 2√2",
        "expected": S_expected,
        "computed": abs(S_k9a) if S_k9a is not None else None,
        "status": "PASS" if S_k9a is not None and abs(abs(S_k9a) - S_expected) < 0.001 else "FAIL",
    }

    return results


if __name__ == "__main__":
    checks = run_sanity_checks()
    print("=" * 60)
    print("k9a_predictor.py — Sanity Checks")
    print("=" * 60)
    for cid, info in checks.items():
        print(f"  CHECK {cid}: {info['description']}")
        print(f"    Expected: {info['expected']}")
        print(f"    Computed: {info['computed']}")
        print(f"    Status:   {info['status']}")
