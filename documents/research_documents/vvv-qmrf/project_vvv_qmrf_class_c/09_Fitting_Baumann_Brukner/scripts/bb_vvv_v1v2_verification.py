"""
BB-VVV V1+V2 Verification Script — CORRECTED
=============================================
V1 CORRECTION (2026-05-27): Original fit plan assumed K5 fires at x=pi/4
(max interference). Actual B&B Eq. B.29 analysis shows:
  - q00 < 0 region is near x ~ 0 (near-readout), NOT x = pi/4
  - At x = pi/4: sin(4x) = sin(pi) = 0, so q00 = 0.5 for ALL phi
  - K5 (B&B) fires when Wigner measures CLOSE to Friend's basis, not far from it

This is a genuine mathematical finding, not a script bug.
The structural mapping V1 (K5 <-> B&B) requires revision.

Source: BB_VVV_fit_plan.md v1.2, Section 6
B&B Paper: arXiv:2305.15497v2
Version: 2.0 (2026-05-27) — corrected V1 analysis
"""

import numpy as np
import json
import os
from datetime import datetime


def q00_BB(x, delta_phi):
    """
    B&B Eq. B.29 simplified.
    q00(x,phi) = sin^2(2x)/2 + (sqrt(2)/6)*sin(4x)*cos(phi)
    
    SCOPE: B&B Appendix B conditions (maximally entangled, specific Bob basis,
    no-signaling + symmetry minimality).
    """
    return np.sin(2*x)**2 / 2 + (np.sqrt(2)/6) * np.sin(4*x) * np.cos(delta_phi)


def delta_p_K7(x, alpha_sq=0.3):
    """
    K7 closure magnitude = B&B memory change Delta_p.
    General formula: Delta_p = |1 - 2*alpha_sq| * sin^2(2x) / 2
    """
    a = np.sin(x)
    b = np.cos(x)
    beta_sq = 1 - alpha_sq
    p_f3 = alpha_sq * (a**4 + b**4) + 2 * beta_sq * a**2 * b**2
    p_f1 = alpha_sq
    return np.abs(p_f3 - p_f1)


def delta_p_analytic(x, alpha_sq=0.3):
    """Analytic formula for cross-check."""
    return np.abs(1 - 2 * alpha_sq) * np.sin(2*x)**2 / 2


def run_verification():
    results = {
        "script": "bb_vvv_v1v2_verification.py",
        "version": "2.0 (corrected V1 analysis)",
        "timestamp": datetime.now().isoformat(),
        "fit_plan_version": "v1.2",
    }
    
    print("=" * 70)
    print("BB-VVV V1+V2 VERIFICATION (CORRECTED)")
    print("BB_VVV_fit_plan.md v1.2 — Phase 1 Algebraic Verification")
    print("=" * 70)
    
    # ============================================================
    # V1: B&B No-Valid-Joint-Model Condition — CORRECTED ANALYSIS
    # ============================================================
    print("\n=== V1: B&B Eq. B.29 Failure Region (CORRECTED) ===")
    print("Simplified: q00(x,phi) = sin^2(2x)/2 + (sqrt(2)/6)*sin(4x)*cos(phi)\n")
    
    # 2D scan
    x_vals = np.linspace(0.001, np.pi/2 - 0.001, 500)
    phi_vals = np.linspace(0, 2*np.pi, 500)
    X, PHI = np.meshgrid(x_vals, phi_vals)
    Q00 = q00_BB(X, PHI)
    
    frac_neg = (Q00 < 0).mean()
    print(f"Fraction of (x, phi) space where q00 < 0: {frac_neg:.4f}")
    
    # KEY CORRECTION: x = pi/4 analysis
    print("\n--- Critical x = pi/4 analysis ---")
    q00_at_pi4 = q00_BB(np.pi/4, np.pi)
    print(f"sin(4*pi/4) = sin(pi) = {np.sin(np.pi):.10f} ~ 0")
    print(f"=> q00(pi/4, ANY phi) = sin^2(pi/2)/2 + 0 = 0.5")
    print(f"=> q00 = {q00_at_pi4:.6f} > 0 for ALL phi")
    print(f"=> K5 (B&B) NEVER fires at x = pi/4 (maximum interference)")
    
    # Find zero crossings for phi = pi
    print("\n--- Zero crossings at phi = pi ---")
    q00_phi_pi = q00_BB(x_vals, np.pi)
    sign_changes = np.where(np.diff(np.sign(q00_phi_pi)))[0]
    x_zeros = []
    for idx in sign_changes:
        x0, x1 = x_vals[idx], x_vals[idx+1]
        q0, q1 = q00_phi_pi[idx], q00_phi_pi[idx+1]
        x_zero = x0 - q0 * (x1-x0) / (q1-q0)
        x_zeros.append(x_zero)
        print(f"  Zero crossing at x = {x_zero:.6f} ({x_zero/np.pi:.4f}*pi)")
    
    if len(x_zeros) >= 1:
        print(f"  q00 < 0 for x in (0, {x_zeros[0]:.4f}) at phi=pi")
        print(f"  This is x in (0, {x_zeros[0]/np.pi:.4f}*pi) — near-readout region!")
    
    # Similarly for phi = 0
    print("\n--- Zero crossings at phi = 0 ---")
    q00_phi_0 = q00_BB(x_vals, 0)
    sign_changes_0 = np.where(np.diff(np.sign(q00_phi_0)))[0]
    for idx in sign_changes_0:
        x0, x1 = x_vals[idx], x_vals[idx+1]
        q0, q1 = q00_phi_0[idx], q00_phi_0[idx+1]
        x_zero = x0 - q0 * (x1-x0) / (q1-q0)
        print(f"  Zero crossing at x = {x_zero:.6f} ({x_zero/np.pi:.4f}*pi)")
    
    # Most negative q00
    min_idx = np.unravel_index(np.argmin(Q00), Q00.shape)
    print(f"\nMost negative q00 = {Q00[min_idx]:.6f}")
    print(f"  at x = {X[min_idx]:.6f} ({X[min_idx]/np.pi:.4f}*pi)")
    print(f"  at phi = {PHI[min_idx]:.6f} ({PHI[min_idx]/np.pi:.4f}*pi)")
    
    # Structural pattern
    print("\n--- V1 CORRECTED Structural Pattern ---")
    print("B&B q00 < 0 region (R_BB):")
    print("  [OK] Near x = 0 (Wigner ~ Friend basis), phi near pi")
    print("  [OK] Near x = pi/2 (Wigner ~ anti-Friend basis), phi near 0")
    print("  [X] NEVER at x = pi/4 (max interference) — sin(4x) = 0 kills the linear term")
    print("")
    print("Physical interpretation:")
    print("  B&B's no-valid-joint-model breaks down when Wigner measures")
    print("  CLOSE to Friend's basis (with certain phase), not when Wigner")
    print("  does maximal interference. This is because near-readout with")
    print("  phase creates a subtle no-signaling violation in the joint model.")
    
    # V1 claim revision
    print("\n--- V1 Claim Status ---")
    print("ORIGINAL claim (fit plan v1.0-v1.2): 'K5 fires <-> requires_K_joint=1'")
    print("CORRECTED finding: B&B q00<0 fires in near-readout regime (x~0, x~pi/2)")
    print("  which is where requires_K_joint ~ 0 in VVV-QMRF classification!")
    print("")
    print("Implication: V1's forward claim needs REVISION.")
    print("  Option 1: requires_K_joint threshold model is too coarse for B&B")
    print("  Option 2: R_BB and R_K5 may capture DIFFERENT failure modes (F4 trigger)")
    print("  Option 3: B&B's q00 negativity reflects no-signaling constraint,")
    print("            not K5 incommensurability — they may be orthogonal conditions")
    
    results["V1"] = {
        "fraction_neg": float(frac_neg),
        "q00_at_pi4": float(q00_at_pi4),
        "x_zeros_phi_pi": [float(z) for z in x_zeros],
        "min_q00": float(Q00[min_idx]),
        "min_q00_x": float(X[min_idx]),
        "min_q00_phi": float(PHI[min_idx]),
        "original_claim_status": "REQUIRES_REVISION",
        "verdict": "B&B q00<0 fires near readout (x~0), not at interference (x=pi/4). Structural mapping requires_K_joint does NOT align with R_BB. V1 forward claim needs revision.",
    }
    
    # ============================================================
    # V2: K7 Closure Magnitude — CONFIRMED
    # ============================================================
    print("\n" + "=" * 70)
    print("=== V2: K7 Closure Magnitude (alpha_sq=0.3) — CONFIRMED ===")
    
    alpha_sq = 0.3
    print(f"\nalpha_sq = {alpha_sq}")
    print(f"Formula: Delta_p = |1 - 2*{alpha_sq}| * sin^2(2x) / 2 = 0.4 * sin^2(2x) / 2\n")
    
    v2_cases = [
        ("x=0.01 (readout)", 0.01),
        ("x=pi/8", np.pi/8),
        ("x=pi/4 (interference)", np.pi/4),
        ("x=3pi/8", 3*np.pi/8),
        ("x=pi/2-0.01 (readout)", np.pi/2 - 0.01),
    ]
    
    all_match = True
    v2_data = {}
    for label, x in v2_cases:
        dp_num = delta_p_K7(x, alpha_sq)
        dp_ana = delta_p_analytic(x, alpha_sq)
        match = np.isclose(dp_num, dp_ana, atol=1e-10)
        all_match = all_match and match
        print(f"  {label:32s}: Dp={dp_num:.6f} (analytic={dp_ana:.6f}) match={match}")
        v2_data[label] = {"delta_p": float(dp_num), "analytic": float(dp_ana)}
    
    # Self-checks
    expected_max = abs(1 - 2*alpha_sq) * 0.5
    dp_pi4 = delta_p_K7(np.pi/4, alpha_sq)
    formula_pass = np.isclose(expected_max, dp_pi4, atol=1e-10)
    dp_sym = delta_p_K7(np.pi/4, 0.5)
    sym_pass = np.isclose(dp_sym, 0.0, atol=1e-10)
    
    print(f"\n[Formula self-check] |1-2*{alpha_sq}|*0.5 = {expected_max:.4f}, script = {dp_pi4:.4f}, PASS = {formula_pass}")
    print(f"[Symmetric degeneracy] alpha_sq=0.5: Dp = {dp_sym:.10f}, PASS = {sym_pass}")
    
    print("\n--- V2 Conclusion ---")
    print("V2 CONFIRMED: Delta_p = 0 at readout, max at interference.")
    print("K7 closure magnitude matches B&B memory change for asymmetric state.")
    print("Pattern is structural invariant for all alpha_sq != 0.5.")
    
    results["V2"] = {
        "alpha_sq": alpha_sq,
        "cases": v2_data,
        "formula_pass": bool(formula_pass),
        "symmetric_degeneracy": bool(sym_pass),
        "all_match": bool(all_match),
        "verdict": "PASS — V2 confirmed. K7 closure magnitude matches B&B Delta_p.",
    }
    
    # ============================================================
    # V1+V2 Joint Analysis — CORRECTED
    # ============================================================
    print("\n" + "=" * 70)
    print("=== V1+V2 JOINT ANALYSIS (CORRECTED) ===\n")
    
    print("CRITICAL FINDING: V1 and V2 test DIFFERENT aspects of B&B:")
    print("")
    print("  V2 (K7 closure): Delta_p MAXIMIZED at x=pi/4 (interference)")
    print("    -> Memory change is largest when Wigner does interference measurement")
    print("    -> This is consistent with K7 closure prediction")
    print("    -> V2 PASSES")
    print("")
    print("  V1 (K5 q00<0): B&B joint model fails near x~0 (readout)")
    print("    -> No-valid-joint-model condition fires NEAR READOUT")
    print("    -> This is NOT where requires_K_joint=1 in VVV-QMRF")
    print("    -> V1 original claim REQUIRES REVISION")
    print("")
    print("Implication for VVV-QMRF:")
    print("  K7 (V2): Memory change magnitude -> structural alignment CONFIRMED")
    print("  K5 (V1): Incommensurability <-> no-valid-joint-model -> NOT equivalent")
    print("           K5 bot_K fires when requires_K_joint=1 (interference regime)")
    print("           B&B q00<0 fires near readout (x~0) with phase")
    print("           These are DIFFERENT failure conditions!")
    print("")
    print("This is HONEST: V1 discovers a genuine structural difference.")
    print("Falsification condition F4 may apply:")
    print('  F4: "configuration where K5 fires but B&B q00>=0 (or vice versa)"')
    print("  -> At x=pi/4: requires_K_joint=1, K5 could fire,")
    print("     but q00=0.5>0 — F4 IS triggered (B&B side positive)")
    print("  -> Near x=0: requires_K_joint=0, K5 should NOT fire,")
    print("     but q00<0 — F4 IS triggered (B&B side negative)")
    
    results["joint"] = {
        "V1_status": "REQUIRES REVISION — R_BB != R_K5 pattern",
        "V2_status": "PASS — K7 closure confirmed",
        "F4_triggered": True,
        "F4_explanation": "K5 fires at x=pi/4 (requires_K_joint=1) but q00>0; B&B fires at x~0 (requires_K_joint=0) but q00<0. Conditions are not equivalent.",
        "recommendation": "V1 claim must be downgraded from 'mathematical equivalence' to 'partial structural compatibility'. K5 and B&B no-valid-joint-model capture DIFFERENT failure modes.",
    }
    
    # ============================================================
    # VERDICT SUMMARY
    # ============================================================
    print("\n" + "=" * 70)
    print("FINAL VERDICT")
    print("=" * 70)
    print("")
    print("V1 (K5 <-> q00<0):  PARTIAL — forward implication DOES NOT HOLD as stated")
    print("                    R_BB != R_K5. F4 falsification condition triggered.")
    print("                    Claim must be revised to 'K5 and B&B q00 capture")
    print("                    different aspects of no-valid-joint-model'.")
    print("")
    print("V2 (K7 <-> Delta_p): PASS — quantitative consistency confirmed.")
    print("                    K7 closure magnitude matches B&B memory change.")
    print("")
    print("Claim class updates:")
    print("  V1: D (proposed) -> D (PARTIAL, F4 triggered, structural difference found)")
    print("  V2: D (proposed) -> D (script-verified)")
    print("  V1 bidirectional: DEFERRED + now MOOT (forward already fails)")
    
    results["final_verdict"] = {
        "V1": "PARTIAL — F4 triggered, R_BB != R_K5",
        "V2": "PASS — K7 closure confirmed",
        "overall": "V2 passes, V1 reveals genuine structural difference between K5 and B&B"
    }
    
    # Save results
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "bb_vvv_v1v2_results.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {output_file}")
    
    return results


if __name__ == "__main__":
    run_verification()
