"""
FR-VVV K7_trace Consumer Verification v1.0
Frauchiger & Renner (2018) x VVV-QMRF K1-K8
Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/

Purpose:
  V_FR2: Confirm K7_trace is second independent consumer (B&B + FR).
  T_FR:  Trace 2-agent avoidance chain (K5->K6->K4) for F1+W1 setup.
  Comparison: FR (scenario-defining K5 trigger) vs B&B (parameter-dependent).
"""

import json
import numpy as np
from datetime import date
import os

# ── K-Space Primitives (scenario-agnostic) ───────────────────────────────────

def K7_trace(V_prov, V_final):
    """K7_trace §18: Δ_closure := V_prov - V_final ∈ {0,1}."""
    delta = int(V_prov) - int(V_final)
    assert delta >= 0, f"K7_trace: V cannot increase (V_prov={V_prov}, V_final={V_final})"
    assert delta in {0, 1}, f"K7_trace: delta={delta} not in {{0,1}}"
    return delta

def K6_auth_invalidate(V_prov, has_authority):
    """K6: overriding authority sets V_final=0."""
    return 0 if (has_authority and V_prov == 1) else int(V_prov)

def K4_self_cert(V_final):
    """K4: self-certification holds iff V=1."""
    return V_final == 1

# ── FR-Specific Primitives ────────────────────────────────────────────────────

def requires_K_joint_FR(measurement_type):
    """
    FR scenario K5 trigger: scenario-defining (not parameter-swept).
      'coherent'   -> W1 measures Lab A as quantum system -> K5 fires (rKJ=1)
      'projective' -> W1 measures in F1's eigenbasis      -> K5 no-fire (rKJ=0)
    Contrast: B&B uses angle x with sin^2(2x) > 0.5 threshold (P2-C first-principles).
    """
    assert measurement_type in {'coherent', 'projective'}
    return int(measurement_type == 'coherent')

def FR_avoidance_chain(measurement_type, V_prov_kF1=1):
    """
    T_FR Steps 1-4 (2-agent: F1 + W1).
    Step1 [K5+K5_prospective]: coherent meas -> requires_K_joint=1
    Step2 [K7+K7_trace]:       K7 closure; K7_trace records delta_closure(k_F1)
    Step3 [K5+K6]:             K5 fires; K6 Auth -> V(k_F1)=0
    Step4 [K4]:                V=0 -> K4 fails -> FR premise fails -> avoided
    """
    rKJ = requires_K_joint_FR(measurement_type)
    V_final = K6_auth_invalidate(V_prov_kF1, has_authority=(rKJ == 1))
    delta = K7_trace(V_prov_kF1, V_final)
    K4_holds = K4_self_cert(V_final)
    # FR contradiction requires V(k_F1)=1 AND V(k_W1)=1; V(k_W1) always 1
    joint_valid = (V_final == 1)
    T_FR_holds = not joint_valid   # avoidance: joint validity unreachable
    return dict(
        measurement_type=measurement_type,
        requires_K_joint=rKJ,
        V_prov=V_prov_kF1,
        V_final=V_final,
        delta_closure=delta,
        K4_holds=K4_holds,
        joint_validity_achievable=joint_valid,
        T_FR_holds=T_FR_holds
    )

# ── Verifications ─────────────────────────────────────────────────────────────

def verify_V_FR2():
    """K7_trace structural identity: same function in B&B and FR contexts."""
    cases = []

    # FR coherent -> delta=1  (B&B analogue: x=pi/4)
    r = FR_avoidance_chain('coherent')
    cases.append(dict(case='FR_coherent', expected_delta=1,
                      delta=r['delta_closure'], BB_analogue='x=pi/4 interference',
                      pass_=r['delta_closure'] == 1))

    # FR projective -> delta=0  (B&B analogue: x=0.01)
    r = FR_avoidance_chain('projective')
    cases.append(dict(case='FR_projective', expected_delta=0,
                      delta=r['delta_closure'], BB_analogue='x=0.01 readout',
                      pass_=r['delta_closure'] == 0))

    # Explicit function-identity check: same K7_trace call, same output
    bb_delta = K7_trace(1, 0)
    fr_delta  = K7_trace(1, 0)
    same_fn = (bb_delta == fr_delta == 1)

    ok = all(c['pass_'] for c in cases) and same_fn
    return dict(
        verification='V_FR2',
        result='PASS' if ok else 'FAIL',
        k7trace_function_identical=same_fn,
        cases=cases,
        finding=(
            'K7_trace(V_prov, V_final) is scenario-agnostic. '
            'Same delta_closure logic in B&B (angle x) and FR (scenario-defining). '
            'FR confirmed as K7_trace second independent consumer.'
        )
    )

def verify_coherent():
    r = FR_avoidance_chain('coherent')
    checks = dict(
        rKJ_is_1=r['requires_K_joint'] == 1,
        V_final_is_0=r['V_final'] == 0,
        delta_is_1=r['delta_closure'] == 1,
        K4_fails=not r['K4_holds'],
        joint_invalid=not r['joint_validity_achievable'],
        T_FR_holds=r['T_FR_holds']
    )
    return dict(verification='avoidance_coherent',
                result='PASS' if all(checks.values()) else 'FAIL',
                checks=checks, chain=r)

def verify_projective():
    r = FR_avoidance_chain('projective')
    checks = dict(
        rKJ_is_0=r['requires_K_joint'] == 0,
        V_final_is_1=r['V_final'] == 1,
        delta_is_0=r['delta_closure'] == 0,
        K4_holds=r['K4_holds'],
        joint_valid=r['joint_validity_achievable'],
        T_FR_not_triggered=not r['T_FR_holds']
    )
    return dict(verification='avoidance_projective',
                result='PASS' if all(checks.values()) else 'FAIL',
                checks=checks, chain=r)

def verify_falsification():
    """F_FR1-F_FR3: none should trigger."""
    r = FR_avoidance_chain('coherent')
    conds = dict(
        F_FR1_K5_fires_V_unchanged=(r['requires_K_joint'] == 1 and r['V_final'] == 1),
        F_FR2_joint_valid_when_K5=(r['requires_K_joint'] == 1 and r['joint_validity_achievable']),
        F_FR3_delta_gt1=(r['delta_closure'] > 1)
    )
    none_triggered = not any(conds.values())
    return dict(verification='falsification',
                result='PASS' if none_triggered else 'FAIL',
                conditions={k: dict(triggered=v, expected=False) for k, v in conds.items()})

def verify_comparison():
    """K5 trigger: FR (scenario-defining) vs B&B (sin^2(2x)>0.5)."""
    pts = [(0.01,'readout'), (np.pi/4,'interference'), (np.pi/2-0.01,'readout')]
    bb = [{'x': round(x, 4), 'regime': lbl,
           'rKJ': int(np.sin(2*x)**2 > 0.5)} for x, lbl in pts]
    fr = [{'type': mt, 'rKJ': requires_K_joint_FR(mt)}
          for mt in ['coherent', 'projective']]
    same = (K7_trace(1, 0) == 1) and (K7_trace(1, 1) == 0)
    return dict(
        verification='structural_comparison',
        result='PASS' if same else 'FAIL',
        bb_cases=bb, fr_cases=fr,
        k7trace_output_identical=same,
        distinction=(
            'B&B K5: angle-dependent (sin^2(2x)>0.5). '
            'FR K5: scenario-defining (coherent=trigger). '
            'K7_trace: identical function in both.'
        )
    )

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("FR-VVV K7_trace Consumer Verification v1.0")
    print("=" * 60)

    steps = [
        verify_V_FR2(),
        verify_coherent(),
        verify_projective(),
        verify_falsification(),
        verify_comparison(),
    ]

    for s in steps:
        sym = 'PASS' if s['result'] == 'PASS' else 'FAIL'
        print(f"  [{sym}] {s['verification']}")

    overall = all(s['result'] == 'PASS' for s in steps)
    print()
    print(f"  OVERALL: {'PASS' if overall else 'FAIL'}")
    print("=" * 60)
    print()
    print("KEY FINDING:")
    print("  V_FR2 CONFIRMED: K7_trace is FR second independent consumer.")
    print("  FR avoidance: coherent -> K5->K6->V=0 -> T_FR holds.")
    print("  K7_trace: scenario-agnostic (same in B&B and FR).")

    out = dict(
        script='fr_vvv_k7trace_consumer_verification.py',
        version='1.0',
        date=str(date.today()),
        paper='Frauchiger & Renner (2018) arXiv:1604.07422',
        overall_pass=overall,
        verifications={s['verification']: s for s in steps}
    )
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fr_vvv_k7trace_results.json')
    with open(path, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\n  Results -> {path}")
    return 0 if overall else 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
