"""
proietti_chsh_fit.py — Proietti CHSH fitting for K9_E (primary) and K9_A (fallback).

Part of VVV-QMRF Phase 10 Python infrastructure (PP-4).
Re-scoped from original PP-4 spec: K9_B replaced by K9_E.

Usage:
  python proietti_chsh_fit.py

Data source: Proietti et al., arXiv:1902.05080v2
  S_exp = 2.416 ± 0.075 (1794 coincidences)
  Individual ⟨A_xB_y⟩: D1-BLK-1 (pending extraction from Figure 3)
"""

import sys
import numpy as np

# Add parent path for imports
sys.path.insert(0, ".")

from utils.qm_standard import (
    qm_chsh_S,
    PROIETTI_ANGLES_A,
    PROIETTI_ANGLES_B,
    PROIETTI_S_EXP,
    PROIETTI_S_ERR,
    PROIETTI_N_TOTAL,
)
from utils.k9a_predictor import k9a_chsh_S
from utils.k9e_predictor import k9e_chsh_S, k9e_delta_S


# ──────────────────────────────────────────────
# Experimental Data
# ──────────────────────────────────────────────

# Individual ⟨A_xB_y⟩ values (D1-BLK-1: pending extraction from Figure 3)
DATA = {
    (1, 1): {"value": None, "error": None},  # ⟨A₁B₁⟩ NOT YET EXTRACTED
    (1, 2): {"value": None, "error": None},  # ⟨A₁B₂⟩ NOT YET EXTRACTED
    (2, 1): {"value": None, "error": None},  # ⟨A₂B₁⟩ NOT YET EXTRACTED
    (2, 2): {"value": None, "error": None},  # ⟨A₂B₂⟩ NOT YET EXTRACTED
}

# Aggregate S value (available)
S_EXP = PROIETTI_S_EXP
S_ERR = PROIETTI_S_ERR


def data_available() -> bool:
    """Check if individual ⟨A_xB_y⟩ data is available."""
    return all(d["value"] is not None for d in DATA.values())


# ──────────────────────────────────────────────
# Fit functions
# ──────────────────────────────────────────────

def fit_k9e_beta_from_S(verbose: bool = True) -> dict:
    """
    Fit K9_E β from S_exp aggregate value.

    PATH B (OI-2): 1 data point (S_exp), 1 free parameter (β).
    DOF = 0 → no goodness-of-fit test. Only point estimate.

    Returns
    -------
    dict with beta_fit, S_predicted, residual
    """
    from scipy.optimize import minimize_scalar

    def residual(beta):
        S_k9e = k9e_chsh_S(
            PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
            PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
            beta=beta,
        )
        return (S_k9e - S_EXP) ** 2

    # Search β ∈ [0, 0.99]
    result = minimize_scalar(residual, bounds=(0.0, 0.99), method="bounded")
    beta_fit = result.x

    S_predicted = k9e_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        beta=beta_fit,
    )

    S_qm = k9e_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        beta=0.0,
    )

    output = {
        "beta_fit": beta_fit,
        "S_predicted": S_predicted,
        "S_exp": S_EXP,
        "S_qm": S_qm,
        "residual": abs(S_predicted - S_EXP),
        "dof": 0,
        "note": "DOF=0: point estimate only, no χ² test possible",
    }

    if verbose:
        print("\n  K9_E β fit (PATH B — S_exp only):")
        print(f"    β_fit     = {beta_fit:.4f}")
        print(f"    S_K9E(β)  = {S_predicted:.4f}")
        print(f"    S_exp     = {S_EXP:.3f} ± {S_ERR:.3f}")
        print(f"    S_QM      = {S_qm:.4f}")
        print(f"    Residual  = {output['residual']:.6f}")
        print(f"    DOF       = 0 (no χ² test)")
        print()
        print("    ⚠️  β is confounded with experimental noise.")
        print("    S_exp < S_QM due to imperfections + possibly K9_E suppression.")
        print("    Cannot separate the two with S_exp alone.")
        print("    Individual ⟨A_xB_y⟩ data (D1-BLK-1) would enable DOF≥2 fit.")

    return output


def beta_upper_bound(sigma: float = 1.0) -> float:
    """
    Compute upper bound on β from S_exp.

    β_max such that S_K9E(β_max) = S_exp − sigma × S_ERR.
    This gives the maximum β consistent with the data at the given sigma level.

    Parameters
    ----------
    sigma : float — number of standard deviations

    Returns
    -------
    float : β upper bound
    """
    from scipy.optimize import brentq

    S_lower = S_EXP - sigma * S_ERR
    S_qm = k9e_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        beta=0.0,
    )

    # If S_QM is already below S_lower, β_max = 0
    if S_qm <= S_lower:
        return 0.0

    def equation(beta):
        S_k9e = k9e_chsh_S(
            PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
            PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
            beta=beta,
        )
        return S_k9e - S_lower

    try:
        beta_max = brentq(equation, 0.0, 0.99)
    except ValueError:
        # S_K9E never reaches S_lower for β ∈ [0, 0.99]
        beta_max = 0.99

    return beta_max


# ──────────────────────────────────────────────
# Comparison report
# ──────────────────────────────────────────────

def comparison_report() -> None:
    """Generate comparison between Standard QM, K9_A, and K9_E."""
    print("=" * 70)
    print("PROIETTI CHSH FIT — Comparison Report")
    print("=" * 70)

    # Standard QM
    S_qm = qm_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
    )
    print(f"\n  Standard QM:  S_QM = {S_qm:.4f}")
    print(f"  Experimental: S_exp = {S_EXP:.3f} ± {S_ERR:.3f}")
    print(f"  Gap:          S_QM − S_exp = {S_qm - S_EXP:.3f}")
    print(f"  Significance: {(S_qm - S_EXP) / S_ERR:.1f}σ from ideal QM")

    # K9_A (Class D)
    print("\n  K9_A (V-Filter, Class D — FALLBACK):")
    S_k9a = k9a_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
        v_rate=1.0,
    )
    print(f"    S_K9A(v_rate=1.0) = {S_k9a:.4f}")
    print(f"    δS = S_K9A − S_QM = {S_k9a - S_qm:.6f}")
    print(f"    K9_A = QM at probability level (δP = 0 always)")

    # K9_E (Class C)
    fit_result = fit_k9e_beta_from_S(verbose=True)

    # β upper bounds
    print("\n  K9_E β upper bounds:")
    for sig in [1.0, 2.0, 3.0]:
        b_max = beta_upper_bound(sigma=sig)
        print(f"    β_max ({sig:.0f}σ) = {b_max:.4f}")

    # δS scan
    print("\n  K9_E δS scan (deviation from QM):")
    print(f"    {'β':>6s}  {'S_K9E':>10s}  {'δS':>10s}  {'δS/σ_S':>8s}")
    for beta in [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95]:
        ds = k9e_delta_S(beta)
        S_val = S_qm + ds
        sig = ds / S_ERR if S_ERR > 0 else 0
        print(f"    {beta:6.2f}  {S_val:10.4f}  {ds:+10.6f}  {sig:+8.2f}σ")

    if not data_available():
        print("\n  ⚠️  Individual ⟨A_xB_y⟩ data NOT YET EXTRACTED (D1-BLK-1)")
        print("     Cannot perform PATH A fit (individual correlators).")
        print("     Running in PLACEHOLDER MODE.")


# ──────────────────────────────────────────────
# Sanity check
# ──────────────────────────────────────────────

def run_sanity_check() -> dict:
    """CHECK 5A: Script runs in placeholder mode without errors."""
    try:
        # Suppress verbose output during check
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            comparison_report()
        output = f.getvalue()
        has_placeholder = "PLACEHOLDER" in output or "NOT YET EXTRACTED" in output
        return {
            "5A": {
                "description": "Script runs in placeholder mode without errors",
                "expected": "No errors + placeholder message",
                "computed": "OK" if has_placeholder else "No placeholder message",
                "status": "PASS" if has_placeholder else "FAIL",
            }
        }
    except Exception as e:
        return {
            "5A": {
                "description": "Script runs without errors",
                "expected": "No errors",
                "computed": str(e),
                "status": "FAIL",
            }
        }


if __name__ == "__main__":
    # Run sanity check first
    check = run_sanity_check()
    print("=" * 60)
    print("proietti_chsh_fit.py — Sanity Check")
    print("=" * 60)
    for cid, info in check.items():
        print(f"  CHECK {cid}: {info['description']}")
        print(f"    Status: {info['status']}")
    print()

    # Run full report
    comparison_report()
