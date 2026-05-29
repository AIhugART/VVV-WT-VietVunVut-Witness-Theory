"""
k9a_predictor.py — K9_A (V-Filter) predictions for VVV-QMRF Phase 10.

K9_A is a Class D model: delta_P = 0 always (no probability-level deviation).
K9_A modifies only validity-rate statistics, not outcome probabilities.
Therefore K9_A = Standard QM at the probability level.

Part of VVV-QMRF PP-4 (Phase 10 Python Package).

Usage:
  from utils.k9a_predictor import k9a_chsh_S
"""

import numpy as np
from utils.qm_standard import qm_chsh_S, PROIETTI_ANGLES_A, PROIETTI_ANGLES_B


def k9a_chsh_S(
    a0: float, a1: float, b0: float, b1: float, v_rate: float = 1.0
) -> float:
    """
    K9_A predicted CHSH S value.

    K9_A = QM at probability level (delta_P = 0 always).
    The v_rate parameter modifies validity statistics only, not S.

    Parameters
    ----------
    a0, a1 : float — Alice's measurement angles (symbolic)
    b0, b1 : float — Bob's measurement angles (symbolic)
    v_rate : float — validity acceptance rate (does not affect S)

    Returns
    -------
    float : S value (always equals S_QM)
    """
    return qm_chsh_S(a0, a1, b0, b1)


def run_sanity_checks() -> dict:
    """PP-4 sanity checks for K9_A predictions."""
    results = {}

    S_k9a = k9a_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B, v_rate=1.0)
    S_qm = qm_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B)

    # Check 2A: K9_A = QM
    results["2A"] = {
        "description": "K9_A = QM at probability level (delta_P = 0)",
        "expected": f"{S_qm:.6f}",
        "computed": f"{S_k9a:.6f}",
        "status": "PASS" if abs(S_k9a - S_qm) < 1e-10 else "FAIL",
    }

    # Check 2B: K9_A independent of v_rate
    S_k9a_half = k9a_chsh_S(
        *PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B, v_rate=0.5
    )
    results["2B"] = {
        "description": "K9_A(v_rate=0.5) = K9_A(v_rate=1.0)",
        "expected": f"{S_k9a:.6f}",
        "computed": f"{S_k9a_half:.6f}",
        "status": "PASS" if abs(S_k9a - S_k9a_half) < 1e-10 else "FAIL",
    }

    return results
