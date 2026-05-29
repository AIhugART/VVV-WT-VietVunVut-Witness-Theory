"""
k9e_predictor.py — K9_E (f_perp registration suppression) predictions.

Model: P(o|K) = Tr(E_o rho) * f_perp(K_ctx)
       f_perp(K_ctx) = 1 - beta * K_ctx
       K_ctx = sum_{i!=j} I(k_i bot k_j) / N_pairs

Uses additive K_ctx approximation for the 2-observer EWF context:
  E_K9E(x,y) = E_QM(x,y) * (1 - beta * K_ctx(x,y))
  K_ctx(x,y) = n_BSM(x,y) * g_ctx
  g_ctx = 0.055 / (2 * sqrt(2) * 0.5) ~ 0.0389

Calibrated to: delta_S(beta=0.5) = -0.055 (index.md line 122)

WARNING — MODEL INCONSISTENCY:
  This module uses an ADDITIVE K_ctx model (g_ctx ~ 0.039).
  The standalone scripts (d1_blk1_4point_fit.py, proietti_raw_fit.py)
  use a MULTIPLICATIVE per-observer model with g_eff = 0.146:
    E = E_QM * (1 - beta*g)^n_BSM   [multiplicative, g=0.146]
  vs this module:
    E = E_QM * (1 - beta*n_BSM*g_ctx) [additive, g_ctx=0.039]

  The two models agree at first order in beta*g but diverge at
  beta > 0.3. The multiplicative model produces larger suppression.
  The genuine fit (proietti_raw_fit.py) uses g=0.146 multiplicative
  and yields beta=0.598. This module's additive model gives a smaller
  delta_S at the same beta.

Part of VVV-QMRF PP-4 (Phase 10 Python Package).

Usage:
  from utils.k9e_predictor import k9e_chsh_S, k9e_delta_S
"""

import numpy as np
from utils.qm_standard import (
    qm_chsh_S,
    E_QM,
    CHSH_SIGNS,
    PROIETTI_ANGLES_A,
    PROIETTI_ANGLES_B,
)


# ──────────────────────────────────────────────
# K_ctx coupling constant (additive model)
# ──────────────────────────────────────────────
# Calibrated from: delta_S(beta=0.5) = -0.055
# Derivation:
#   delta_S = -beta * g_ctx * sum(CHSH_SIGN * E_QM * n_BSM)
#   sum = (1/sqrt(2)) * [0 + 1 + 1 + 2] = 4/sqrt(2) = 2*sqrt(2)
#   => g_ctx = |delta_S| / (beta * 2*sqrt(2))
#            = 0.055 / (0.5 * 2*sqrt(2))
#            = 0.055 / sqrt(2)
#            ~ 0.03889

G_CTX = 0.055 / (2.0 * np.sqrt(2) * 0.5)  # ~ 0.03889


def k9e_K_ctx(x: int, y: int) -> float:
    """
    K-space context parameter for setting pair (x, y).

    Parameters
    ----------
    x : int — Alice's setting (0=projective, 1=BSM)
    y : int — Bob's setting (0=projective, 1=BSM)

    Returns
    -------
    float : K_ctx = n_BSM * g_ctx

    Setting interpretation:
      x=0: Alice projective → no bot_K with Friend_A
      x=1: Alice BSM → bot_K fires between Alice and Friend_A
      y=0: Bob projective → no bot_K with Friend_B
      y=1: Bob BSM → bot_K fires between Bob and Friend_B
    """
    n_bsm = x + y
    return n_bsm * G_CTX


def k9e_f_perp(K_ctx: float, beta: float) -> float:
    """
    Registration suppression factor.

    f_perp = 1 - beta * K_ctx

    At beta=0: f_perp = 1 (Born recovery).
    At beta>0, K_ctx>0: f_perp < 1 (suppression).
    """
    return 1.0 - beta * K_ctx


def k9e_correlator(x: int, y: int, beta: float) -> float:
    """
    K9_E predicted correlator for setting (x, y) at given beta.

    E_K9E(x,y) = E_QM(x,y) * (1 - beta * K_ctx(x,y))
    """
    K_ctx = k9e_K_ctx(x, y)
    return E_QM[(x, y)] * k9e_f_perp(K_ctx, beta)


def k9e_chsh_S(
    a0: float, a1: float, b0: float, b1: float, beta: float = 0.0
) -> float:
    """
    K9_E predicted CHSH S value.

    At beta=0: returns S_QM = 2*sqrt(2) (Born recovery).
    At beta>0: returns S < S_QM (K9_E suppression).

    Parameters
    ----------
    a0, a1 : float — Alice's measurement angles (symbolic)
    b0, b1 : float — Bob's measurement angles (symbolic)
    beta : float — K9_E suppression parameter in [0, 1]
    """
    return sum(
        CHSH_SIGNS[(x, y)] * k9e_correlator(x, y, beta)
        for x in [0, 1]
        for y in [0, 1]
    )


def k9e_delta_S(beta: float) -> float:
    """
    K9_E deviation from QM.

    delta_S = S_K9E(beta) - S_QM

    At beta=0: delta_S = 0.
    At beta=0.5: delta_S ~ -0.055 (by calibration).
    """
    S_qm = qm_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B)
    S_k9e = k9e_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B, beta=beta)
    return S_k9e - S_qm


def run_sanity_checks() -> dict:
    """PP-4 sanity checks for K9_E predictions."""
    results = {}

    S_qm = qm_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B)

    # Check 3A: beta=0 → Born recovery
    S_k9e_0 = k9e_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B, beta=0.0)
    results["3A"] = {
        "description": "K9_E at beta=0 -> QM (Born recovery)",
        "expected": f"{S_qm:.6f}",
        "computed": f"{S_k9e_0:.6f}",
        "status": "PASS" if abs(S_k9e_0 - S_qm) < 1e-10 else "FAIL",
    }

    # Check 3B: beta>0 → delta_S < 0
    ds = k9e_delta_S(0.5)
    results["3B"] = {
        "description": "K9_E at beta=0.5 -> delta_S < 0 (suppression)",
        "expected": "delta_S < 0",
        "computed": f"{ds:.6f}",
        "status": "PASS" if ds < 0 else "FAIL",
    }

    # Check 3C: delta_S(0.5) ~ -0.055
    results["3C"] = {
        "description": "delta_S(beta=0.5) ~ -0.055",
        "expected": "-0.0550",
        "computed": f"{ds:.4f}",
        "status": "PASS" if abs(ds - (-0.055)) < 0.002 else "FAIL",
    }

    # Check 3D: K9_E S-value monotonically decreases with beta
    s_values = [
        k9e_chsh_S(*PROIETTI_ANGLES_A, *PROIETTI_ANGLES_B, beta=b)
        for b in [0.0, 0.3, 0.5, 0.7, 0.9]
    ]
    monotonic = all(
        s_values[i] >= s_values[i + 1] for i in range(len(s_values) - 1)
    )
    results["3D"] = {
        "description": "K9_E S monotonically decreases with beta",
        "expected": "True",
        "computed": str(monotonic),
        "status": "PASS" if monotonic else "FAIL",
    }

    return results
