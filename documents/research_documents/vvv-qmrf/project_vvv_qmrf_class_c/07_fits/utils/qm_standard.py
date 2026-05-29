"""
qm_standard.py — Standard QM predictions for VVV-QMRF Phase 10 infrastructure.

Part of VVV-QMRF PP-4 (Phase 10 Python Package).
Provides QM predictions, Proietti experimental constants, and sanity checks.

Data source: Proietti et al. 2019, arXiv:1902.05080v2
  S_exp = 2.416 +/- 0.075 (main.tex L196)
  N_total = 1794 coincidences (main.tex L195)
  QM predictions from Eq. S5 + S7

Usage:
  from utils.qm_standard import qm_chsh_S, PROIETTI_S_EXP
"""

import numpy as np


# ──────────────────────────────────────────────
# Proietti Experimental Constants
# Source: Proietti et al. 2019, arXiv:1902.05080v2
# ──────────────────────────────────────────────

PROIETTI_ANGLES_A = [0.0, np.pi / 2]             # Symbolic: A0=projective, A1=BSM
PROIETTI_ANGLES_B = [np.pi / 4, 3 * np.pi / 4]   # Symbolic: B0=projective, B1=BSM
PROIETTI_S_EXP = 2.416       # S_exp from main.tex L196
PROIETTI_S_ERR = 0.075       # sigma_S from main.tex L196
PROIETTI_N_TOTAL = 1794      # Total coincidences from main.tex L195


# ──────────────────────────────────────────────
# QM Predictions for Proietti CHSH Setup
# Source: Eq. S5 + S7 of arXiv:1902.05080v2
# State: 4-photon entangled (Wigner's friend EWF)
#
# NOTE: Angles are symbolic. The Proietti experiment uses
# projective (x=0) vs BSM (x=1) measurements, not simple
# polarizer angles. QM predictions are hardcoded from the
# paper's theoretical analysis.
# ──────────────────────────────────────────────

E_QM = {
    (0, 0): -1.0 / np.sqrt(2),   # A0B0: -cos(pi/4) ~ -0.7071
    (0, 1): +1.0 / np.sqrt(2),   # A0B1: +sin(pi/4) ~ +0.7071
    (1, 0): +1.0 / np.sqrt(2),   # A1B0: +sin(pi/4) ~ +0.7071
    (1, 1): +1.0 / np.sqrt(2),   # A1B1: +cos(pi/4) ~ +0.7071
}

# CHSH signs: S = -E(A0B0) + E(A0B1) + E(A1B0) + E(A1B1)
# From main.tex L146
CHSH_SIGNS = {(0, 0): -1, (0, 1): +1, (1, 0): +1, (1, 1): +1}


def qm_correlator(x: int, y: int) -> float:
    """
    QM predicted correlator for Proietti setting pair (x, y).

    Parameters
    ----------
    x : int — Alice's setting (0=projective, 1=BSM)
    y : int — Bob's setting (0=projective, 1=BSM)

    Returns
    -------
    float : E_QM(x, y)
    """
    return E_QM[(x, y)]


def qm_chsh_S(a0: float, a1: float, b0: float, b1: float) -> float:
    """
    Standard QM CHSH S value for the Proietti setup.

    Returns S_QM = 2*sqrt(2) (Tsirelson bound).

    Parameters are symbolic angles (retained for interface compatibility).
    The actual QM predictions depend on the entangled state (Eq. S5)
    and measurement operators (Eq. S7), not simple polarizer angles.
    """
    return sum(
        CHSH_SIGNS[(x, y)] * E_QM[(x, y)]
        for x in [0, 1]
        for y in [0, 1]
    )


def run_sanity_checks() -> dict:
    """PP-4 sanity checks for Standard QM predictions."""
    results = {}

    S_QM = qm_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B)
    expected = 2.0 * np.sqrt(2)

    # Check 1A: S_QM = 2*sqrt(2)
    results["1A"] = {
        "description": "S_QM = 2*sqrt(2) (Tsirelson bound)",
        "expected": f"{expected:.6f}",
        "computed": f"{S_QM:.6f}",
        "status": "PASS" if abs(S_QM - expected) < 1e-10 else "FAIL",
    }

    # Check 1B: Each |E_QM| = 1/sqrt(2)
    all_correct = all(
        abs(abs(v) - 1.0 / np.sqrt(2)) < 1e-10 for v in E_QM.values()
    )
    results["1B"] = {
        "description": "All |E_QM| = 1/sqrt(2)",
        "expected": "True",
        "computed": str(all_correct),
        "status": "PASS" if all_correct else "FAIL",
    }

    # Check 1C: CHSH sign structure correct
    S_check = -E_QM[(0, 0)] + E_QM[(0, 1)] + E_QM[(1, 0)] + E_QM[(1, 1)]
    results["1C"] = {
        "description": "CHSH sign structure: -E00 + E01 + E10 + E11 = 2*sqrt(2)",
        "expected": f"{expected:.6f}",
        "computed": f"{S_check:.6f}",
        "status": "PASS" if abs(S_check - expected) < 1e-10 else "FAIL",
    }

    return results
