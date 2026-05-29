"""
qm_standard.py — Standard QM predictions for CHSH and LF observables.

Part of VVV-QMRF Phase 10 Python infrastructure (PP-4).
Provides baseline Born-rule predictions against which K9 candidates are compared.
"""

import numpy as np


def qm_singlet_expectation(theta_A: float, theta_B: float) -> float:
    """
    For singlet state |Φ⁻⟩ = (|HV⟩ − |VH⟩)/√2:
    ⟨A(θ_A) B(θ_B)⟩ = −cos(θ_A − θ_B)

    Parameters
    ----------
    theta_A : float — Alice's measurement angle (radians)
    theta_B : float — Bob's measurement angle (radians)

    Returns
    -------
    float in [-1, 1]
    """
    return -np.cos(theta_A - theta_B)


def qm_chsh_all_expectations(
    theta_A1: float, theta_A2: float,
    theta_B1: float, theta_B2: float
) -> dict:
    """
    Compute all four ⟨A_xB_y⟩ correlators for CHSH.

    Returns
    -------
    dict : {(x, y): float} for x ∈ {1,2}, y ∈ {1,2}
    """
    return {
        (1, 1): qm_singlet_expectation(theta_A1, theta_B1),
        (1, 2): qm_singlet_expectation(theta_A1, theta_B2),
        (2, 1): qm_singlet_expectation(theta_A2, theta_B1),
        (2, 2): qm_singlet_expectation(theta_A2, theta_B2),
    }


def qm_chsh_S(
    theta_A1: float, theta_A2: float,
    theta_B1: float, theta_B2: float
) -> float:
    """
    CHSH parameter S = ⟨A1B1⟩ + ⟨A1B2⟩ + ⟨A2B1⟩ − ⟨A2B2⟩.

    Convention: S = E(a,b) + E(a,b') + E(a',b) - E(a',b').
    QM maximum |S| for singlet: 2√2 ≈ 2.828.
    (S = −2√2 for E = −cos convention, |S| = 2√2.)

    Returns
    -------
    float
    """
    e = qm_chsh_all_expectations(theta_A1, theta_A2, theta_B1, theta_B2)
    return e[(1, 1)] + e[(1, 2)] + e[(2, 1)] - e[(2, 2)]


# ──────────────────────────────────────────────
# Proietti-specific utilities
# ──────────────────────────────────────────────

# Proietti experiment angles (from PP-3 / arXiv:1902.05080v2)
# Alice: φ₁ = 168°, φ₂ = 0°   (converted to radians)
# Bob:   φ₁ = 168°, φ₂ = 175°  (needs confirmation from Figure 3)
PROIETTI_ANGLES_A = (168.0 * np.pi / 180.0, 0.0)
PROIETTI_ANGLES_B = (168.0 * np.pi / 180.0, 175.0 * np.pi / 180.0)

# Proietti experimental data
PROIETTI_S_EXP = 2.416
PROIETTI_S_ERR = 0.075
PROIETTI_N_TOTAL = 1794


def proietti_qm_S() -> float:
    """QM prediction for S at Proietti angles."""
    return qm_chsh_S(
        PROIETTI_ANGLES_A[0], PROIETTI_ANGLES_A[1],
        PROIETTI_ANGLES_B[0], PROIETTI_ANGLES_B[1],
    )


# ──────────────────────────────────────────────
# Sanity checks
# ──────────────────────────────────────────────

def run_sanity_checks() -> dict:
    """Run all qm_standard sanity checks. Returns dict of check results."""
    results = {}

    # CHECK 2A: CHSH-optimal angles → |S| = 2√2
    # For singlet E = -cos(a-b), optimal: a1=0, a2=π/2, b1=π/4, b2=-π/4
    theta_A1, theta_A2 = 0.0, np.pi / 2
    theta_B1, theta_B2 = np.pi / 4, -np.pi / 4
    S_computed = qm_chsh_S(theta_A1, theta_A2, theta_B1, theta_B2)
    S_expected = 2 * np.sqrt(2)  # |S| = 2√2
    passed = abs(abs(S_computed) - S_expected) < 0.001
    results["2A"] = {
        "description": "CHSH-optimal angles → |S| = 2√2",
        "expected": S_expected,
        "computed": abs(S_computed),
        "status": "PASS" if passed else "FAIL",
    }

    return results


if __name__ == "__main__":
    checks = run_sanity_checks()
    print("=" * 60)
    print("qm_standard.py — Sanity Checks")
    print("=" * 60)
    for cid, info in checks.items():
        print(f"  CHECK {cid}: {info['description']}")
        print(f"    Expected: {info['expected']:.6f}")
        print(f"    Computed: {info['computed']:.6f}")
        print(f"    Status:   {info['status']}")
    print()
    print(f"  Proietti QM S prediction: {proietti_qm_S():.4f}")
    print(f"  Proietti S_exp:           {PROIETTI_S_EXP}")
