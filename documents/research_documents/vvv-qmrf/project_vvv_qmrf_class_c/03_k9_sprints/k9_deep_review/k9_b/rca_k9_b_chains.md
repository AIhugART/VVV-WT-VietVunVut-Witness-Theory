Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chains — K9_B Deep Review (P2)

**Target:** K9_B — Registration-Conditioned (FAIL-FATAL)
**Phase:** P2 execution
**Date:** 2026-05-27
**Method:** 4-Layer RCA (Layer 0 Meta + Layer 1 Per-Component + Layer 2 Cluster + Layer 3 Verdict)
**Parent:** [plan_k9_b_deep_review.md](./plan_k9_b_deep_review.md)
**Companion:** [report_k9_b_traceability_matrix.md](./report_k9_b_traceability_matrix.md)

---

## Layer 0 — Meta-RCA: Why Does K9_B Exist?

**Question:** What structural gap in K1–K8 did K9_B attempt to fill, and why was multiplicative form chosen?

```
Symptom: K9_B proposes P(o|K) = Tr(E_o ρ) · f(cert, V, ⊥_K, C_K) as a multiplicative
         modulation of Born rule by K-side registration fields.

  Why 1: What structural gap does K9_B claim to address?
    → K1–K8 define registration-logic axioms (when events are valid, how they
      contradict) but contain NO probability rule. A K9 postulate is needed to
      connect K-space structure to Born rule probability assignment. K9_B proposes
      that the "health" of a registration (cert, V, ⊥_K, C_K) modifies the
      probability of its registered outcome.

  Why 2: Why is f chosen as multiplicative modulation and not case-based?
    → Multiplicative form is the simplest extension of Born rule:
      P = Tr(E_o ρ) · f(K-fields), where f = 1 recovers Born rule exactly.
      A multiplicative approach avoids introducing conditional branching (as K9_A
      does) and promises a smooth interpolation between Born and modified regimes.
      It is the natural "Born rule × correction factor" template.

  Why 3: What makes all 4 inputs per-tuple rather than per-outcome?
    → K1–K8 only axiomatize tuple-level and context-level properties. K-state
      k = ⟨M, o, cert, t, V⟩ records the entire registration event; its fields
      (cert, V) are properties of the tuple, not of the outcome o within the tuple.
      K5's ⊥_K fires per-tuple-pair (k1 ⊥ k2), not per-outcome. C_K is a
      relational property of the K-space pair (exists or not for the pair), not
      per-outcome within a registration.

  Why 4: What K1–K8 design decision caused this structural constraint?
    → K1–K8 were designed to axiomatize the registration-logic structure:
      admission rules (K1, K3), ordering (K2), validity (K4, K5), authentication
      (K6), closure (K7), and preservation (K8). This design explicitly separates
      registration-logic from probability assignment. K9 postulates are intentionally
      separate (Layer 3) because K1–K8 cannot uniquely determine a probability rule
      from structure alone. The design decision was: K1–K8 = structural rules,
      not statistical weights.

  Why 5: Is the cancellation in normalization a fixable bug or structural necessity?
    → STRUCTURAL NECESSITY. The algebra is unambiguous:
        Σ_o [Tr(E_o ρ) · f(per-tuple vars)] = f · Σ_o Tr(E_o ρ) = f · 1 = f
        → P(o|K) = Tr(E_o ρ) · f / f = Tr(E_o ρ)
      Because f is constant across all outcomes o (it depends only on per-tuple
      fields), it appears in every numerator AND in the normalization denominator.
      This is not a numerical coincidence — it is an algebraic identity from the
      definition of per-tuple functions.

      Root cause: K1–K8 contain no outcome-dependent field beyond o(k) itself.
                  The field o(k) records WHICH outcome occurred, but Tr(E_o ρ)
                  already extracts the complete probability content of outcome o.
                  Any additional K-side function of per-tuple fields produces a
                  constant multiplicative factor that cancels in normalization.
                  This is THEOREM PP-2-SI (PP-2 v2 Round 3, score 5.0/5).

      Implication: FAIL-FATAL follows necessarily and unconditionally from K1–K8
                   algebra. The verdict is not probabilistic or fixable within
                   the FROZEN Layer 1. K9_B cannot be revived by parameter
                   adjustment, re-parameterization, or minor reformulation.
```

**Layer 0 conclusion:** K9_B's FAIL-FATAL verdict is rooted in a structural feature of K1–K8 (no outcome-dependent weighting field), not in a design error that could be corrected. Layer 0 sets the standard against which each component is judged: "necessary for the structural impossibility proof" vs "incidental to the form."

---

## Layer 1 — Per-Component RCA

*Full 5-Whys chains for components with H ≥ 5 OR Trace = 0/6. All others have 3-Whys inline in the traceability matrix.*

### B-09 — C5 Gap: N_QM_VVV_00031 (SNR / Registration Weight) — H=5, Trace=0/6

**Why this component exists:** PP-2 v2 Round 2 Option B2 analysis identified EX node N_QM_VVV_00031 (Registration Weight / Signal-to-Noise Ratio) as a potentially outcome-dependent escape route — the only EX node that could in principle provide per-outcome modulation and break the cancellation.

```
5-Whys for B-09 (C5 gap — SNR potential escape route) — H=5, Trace=0/6

  Symptom: N_QM_VVV_00031 (Registration Weight / SNR) maps to N_QM_00068
           (Signal-to-Noise Ratio) in EX and is potentially outcome-dependent
           (some outcomes have higher SNR). This could, in principle, allow
           f(SNR(o)) to break the per-tuple cancellation.

    Why 1: Why is SNR potentially outcome-dependent?
      → In standard measurement physics, detector SNR may vary by detector
        outcome: some outcomes (clear signals) have higher SNR than others
        (ambiguous readings). If SNR(o) genuinely varies with o, then
        f(SNR(o)) would not cancel in normalization.

    Why 2: Why is this identified as a "gap" rather than an escape route?
      → K1–K8 contain no SNR field. The K-state tuple is k = ⟨M, o, cert, t, V⟩.
        None of the five fields encodes Signal-to-Noise Ratio or any outcome-
        differential weighting. The EX node N_QM_VVV_00031 exists as a CONCEPT
        in the EX graph but has NO BACK-TRACE to a K-state field in K1–K8.

    Why 3: Why can't SNR be added to K1–K8 to fix K9_B?
      → Layer 1 (K1–K8) is FROZEN (CLAUDE.md §Identity and scope rules).
        Adding a new K-state field would require unfreezing Layer 1, which would
        cascade to all downstream theorems (T1–T9) and all existing K9 derivations.
        This is not a "minor fix" — it is a Layer 1 architectural change.

    Why 4: What would "outcome-dependent SNR" look like formally?
      → It would require either:
        (a) A new K-state field: k = ⟨M, o, cert, t, V, w(o)⟩ where w: O→ℝ+
            is an outcome-dependent weight — Layer 1 extension (FROZEN, blocked).
        (b) A Level 4 predicate that maps outcomes to weights — not currently
            in D_joint, requires_K_joint, AdmJoint, or ⊥_K definitions.
        (c) A direct redefinition of Tr(E_o ρ) to incorporate K-side SNR —
            which would be a Standard QM modification, not a K-side modification.
        All three paths are blocked: (a) FROZEN, (b) undefined in Level 4,
        (c) outside K-space scope.

    Why 5: Is N_QM_VVV_00031 an SOT anchor or compass-only?
      → COMPASS-ONLY (EX). By the VVV-QMRF/VVV-QMRC integration rule
        (CLAUDE.md §VVV-QMRF core/EX integration rule): "Treat VVV-QMRF-EX as
        having completed its main role..." EX nodes do NOT contribute to
        Trace_Score (SOT-1 through SOT-6 only).

      Root cause: The SNR escape route exists as an EX concept (N_QM_VVV_00031)
                  but has no K1–K8 structural anchor. To become a valid K9
                  modification, SNR would require a FROZEN Layer 1 extension —
                  architecturally blocked. The C5 gap is a CONFIRMED CLOSED gap.

      Fix candidate: CONFIRM (closed gap). B-09 documents the gap for completeness
                     and to prevent future revival of K9_B via SNR arguments.
      Affected siblings: None — B-09 is isolated. Closing C5 reinforces B-08
                         (FAIL-FATAL verdict).
```

---

## Layer 2 — Cluster RCA

**Trigger check:**
- Orphans ≥ 2? **NO** — only B-09 (Trace=0/6). Condition NOT met.
- ≥ 3 components share upstream "Why"? **YES** — B-04 (⊥_K), B-05 (C_K), B-06 (f outcome-independent) all trace to "K1–K8 has no outcome-dependent field" as shared upstream Why 3. Condition MET.
- ≥ 2 components with PP-2-only anchor? **YES** — B-06 and B-08 both have PP-2-SI as primary anchor. Condition MET.

**Layer 2 triggered: conditions 2 and 3 both met. One cluster identified.**

### Cluster C-1: Per-Tuple Anchoring Cluster (B-04, B-05, B-06)

```
Cluster C-1: "All K9_B input variables are per-tuple or per-context"
  Affected components: B-04 (⊥_K), B-05 (C_K), B-06 (f outcome-independent)
  Shared symptom: Each component is not outcome-dependent — ⊥_K fires per-tuple-pair,
                  C_K exists per-context, and f therefore cannot vary with o.

    Why 1: Why do B-04, B-05, B-06 all converge to "per-tuple"?
      → They are all derived from the same architectural layer:
        K5 defines both ⊥_K (firing condition) and C_K (comparison context),
        while K1–K3 define cert and K4 defines V. All these axioms describe
        REGISTRATION-LEVEL properties, not outcome-differential properties.

    Why 2: Why does K5 define ⊥_K as per-tuple-pair rather than per-outcome?
      → K5's function is invalidation: when k2 contradicts k1, V(k1) → 0.
        The contradiction is between TUPLES (the entire registration event k2
        contradicts k1), not between specific outcomes within a measurement.
        K5 was designed for the EWF scenario where ENTIRE registration acts
        are incommensurable — not for distinguishing between different outcomes
        of the same measurement.

    Why 3: What structural decision caused C_K to be per-context?
      → C_K (comparison context) is tied to D_joint / requires_K_joint (Level 4 §4.3).
        This is a BINARY property: either K-spaces are in a joint-registration
        context or they are not. There is no graduated or outcome-dependent version
        of C_K in K1–K8. The design reflects the EWF scenario binary: two observers
        are either jointly registered (incommensurability possible) or isolated
        (standard Born rule applies).

    Why 4: Why does K1–K8 not include an outcome-differential weighting field?
      → K1–K8 axiomatize REGISTRATION LOGIC: which events are registered, how
        registrations are ordered, when validity is voided, how K-spaces are joined.
        Statistical weighting of specific outcomes is the role of the PROBABILITY
        POSTULATE (K9), NOT of K1–K8. The separation is intentional:
        K1–K8 = structural; K9 = statistical. K9_B attempts to bridge this by
        using K1–K8 fields as statistical weights — but K1–K8 fields are not
        statistical quantities.

    Why 5: Is this a fixable design gap or a principled boundary?
      Root cause: K1–K8 define a registration-logic layer STRUCTURALLY SEPARATE
                  from the probability layer. This is a PRINCIPLED DESIGN BOUNDARY,
                  not an oversight. K1–K8 fields (cert, V, ⊥_K, C_K) are all
                  binary or relational registration-logic properties; they are not
                  continuous statistical weights. Any K9 of the form
                  P = Tr(E_o ρ) · g(K-logic fields) inherits this boundary and
                  cancels in normalization.

      Fix strategy: The cluster cannot be fixed within K1–K8. Resolution requires
                    EITHER a case-based K9 (K9_A approach — avoids multiplication)
                    OR an outcome-dependent field beyond K1–K8 (K9_C: τ_reg,
                    K9_E: f_perp). K9_B's multiplicative form is incompatible
                    with per-tuple K-logic inputs.
      Priority: LOW (informational; confirms structural boundary, no action needed)
```

---

## Layer 3 — Verdict-Level RCA

**Question:** After Layers 0–2, is the FAIL-FATAL verdict still locked? Does any v31 update affect K9_B?

```
Verdict RCA:
  PP-2 verdict (2026-05-23): FAIL-FATAL — STRUCTURAL IMPOSSIBILITY THEOREM PP-2-SI.
  Root cause (PP-2): per-tuple multiplicative modulation cancels in normalization
                     within K1–K8 (Layer 1 FROZEN). Score: 5.0/5 × 3 rounds.

  Post-deep-review question 1: Does any v31 update interact with K9_B?
    Why 1: What are the v29–v31 updates?
      → v29: K5_prospective added (prospective evaluation extension for K9_E P9).
        v30: Noise sensitivity analysis (K9_E downgraded to Class C qualified).
        v31: K9E-PAT CLOSED as UNRESOLVABLE (RCA 4.92/5). T8 (K5_prospective
             Frequency Bridge) and T9 (K_ctx Construction) added to Layer 2.
    Why 2: Do any of these affect K9_B?
      → NO. K5_prospective is explicitly a "P9 bridge" — extends K5's evaluation
        MODE for K9_E probability assignment only. It does not add an outcome-
        dependent field to K1–K8. T8 bridges K5_prospective ↔ K9_E f_perp; T9
        formalizes φ_ij morphism channel. Neither creates a new K-state field
        or modifies the per-tuple nature of cert, V, ⊥_K, C_K.
    Why 3: Could T8's "prospective" mode provide an escape for K9_B?
      → NO. T8's prospective evaluation asks: "IF outcome o were registered,
        WOULD k5_o* be contradicted?" This still operates on HYPOTHETICAL tuples
        (one per outcome o), not on actual outcome-differential weighting. The
        prospective mode is a modal extension, not a statistical weighting.
        K9_B's problem is that f cancels regardless of evaluation mode.
    → Update verdict: UNCHANGED. v29/v30/v31 updates are K9_E-specific.

  Post-deep-review question 2: Does the C5 gap (B-09, SNR) remain open?
    Why 1: Is N_QM_VVV_00031 (SNR) now axiomatized in any v29–v31 addition?
      → NO. T8 and T9 do not add SNR. K5_prospective does not add SNR. Layer 1
        remains K1–K8 with no SNR field. B-09 gap is confirmed CLOSED.
    Why 2: Could SNR be incorporated via T4-H (colimit theorem)?
      → T4-H (Steps 2–4) remains DEFERRED (relevant to K9_F, not K9_B). Even if
        T4 were proven, it would create new K_joint structure for multi-observer
        scenarios — not an SNR weighting for per-outcome modulation within K9_B.
    Why 3: Does Proietti 2019 data suggest any outcome-differential registration?
      → K9_B was pre-eliminated before K9-S2 (data analysis phase). No Proietti
        data fit was attempted. Even if SNR were measured in Proietti, adding it
        to K9_B would require Layer 1 extension (FROZEN).
    → C5 gap confirmed CLOSED by Layer 1 FROZEN constraint.

  Final reconciliation:
    K9_B's FAIL-FATAL verdict is confirmed by P2 deep review with no modifications.
    The structural impossibility (THEOREM PP-2-SI) is anchored to K1–K8's principled
    design boundary: registration-logic fields (cert, V, ⊥_K, C_K) are not
    statistical outcome weights. No v29–v31 update introduces an outcome-dependent
    K-state field. The C5 gap (SNR, N_QM_VVV_00031) is confirmed closed: it exists
    as an EX concept but has no K1–K8 anchor and cannot be added without unfreezing
    FROZEN Layer 1. K9_B is permanently eliminated and cannot be revived by
    parameter adjustment, re-parameterization, or any selective update to K5_prospective,
    T8, or T9. The 9-component inventory confirms mean H-score ≈ 2.1 (mostly GREEN),
    consistent with a well-understood structural failure rather than an ambiguous
    borderline case. Verdict: FAIL-FATAL LOCKED.
```

---

## Aggregate RCA Findings

**Dominant root cause of K9_B's failure (one sentence):**
K1–K8 axiomatize registration-logic (which events are valid and how they contradict) but contain no outcome-differential weighting field — making any multiplicative K9 of the form P = Tr(E_o ρ) · g(K-logic fields) algebraically equivalent to Born rule after normalization.

**Secondary finding from Layer 2 Cluster C-1:**
The per-tuple anchoring of B-04 (⊥_K), B-05 (C_K), and B-06 (outcome-independence) is not a design flaw but a principled boundary between the registration-logic layer (K1–K8) and the probability-assignment layer (K9). Surviving K9 candidates (K9_A, K9_E) work precisely BECAUSE they respect this boundary: K9_A uses case-based gating (no multiplicative normalization), K9_E uses f_perp as an outcome-specific function derived via K5_prospective (prospective mode, not per-tuple).

**Impact on P3–P6 deep reviews:**
The PP-2-SI structural impossibility theorem applies to K9_D with the same mechanism (per-tuple cert discount, α cancels). P3 review of K9_D should reference this cluster finding. P4 (K9_C) and P5 (K9_E) should verify that τ_reg(o) and f_perp(K_ctx, o) are GENUINELY outcome-dependent (not per-tuple) before declaring them survivors — this is pre-identified in PP-2 v2 as "⚠️ check needed" for K9_C and K9_E.

---

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-05-27 | v0.1 | P2 execution. Layer 0–3 complete. 9 components (B-01…B-09). Layer 2 triggered (conditions 2+3). FAIL-FATAL confirmed. |
