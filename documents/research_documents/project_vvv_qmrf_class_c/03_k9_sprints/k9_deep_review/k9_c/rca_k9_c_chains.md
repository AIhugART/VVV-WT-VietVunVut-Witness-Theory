Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chains — K9_C Deep Review (P3)

**Target:** K9_C — Registration Latency Weighting (FAIL-FIXABLE)
**Phase:** P3 execution
**Date:** 2026-05-27
**Method:** 4-Layer RCA (Layer 0 Meta + Layer 1 Per-Component + Layer 2 Cluster + Layer 3 Verdict)
**Parent:** [plan_k9_c_deep_review.md](./plan_k9_c_deep_review.md)
**Companion:** [report_k9_c_traceability_matrix.md](./report_k9_c_traceability_matrix.md)

---

## Layer 0 — Meta-RCA: The Temporal Latency Circularity

**Central question:** What structural gap in K1–K8 does K9_C attempt to fill, and why does τ_reg(o) introduce an unresolvable circularity within the frozen axiom set?

```
Symptom: P(o|k,H) = Tr(E_o ρ) · exp(−τ_reg(o)/τ_0) / Z_C contains τ_reg(o),
         a quantity that depends on WHICH outcome o occurs. But P(o|k,H)
         assigns probability TO outcome o BEFORE it is registered. τ_reg(o)
         must be evaluated PRE-registration, yet its definition requires
         POST-registration knowledge of which o was realized.
         → Circular: computing τ_reg(o) requires knowing o, which is what
           P assigns.

  Why 1: What structural gap does K9_C attempt to fill?
    → K1-K8 define registration-logic axioms (admission, ordering, validity,
      incommensurability, authentication, closure, preservation) but contain
      NO probability rule. Layer 3 K9 postulates fill this gap. K9_C proposes
      that outcomes registering faster (smaller τ_reg) receive higher probability
      weight — a temporal dynamics modifier on Born rule.
      Physical intuition: detectors may respond at different rates for different
      outcomes (tunneling rates, fluorescence decay, click latency); faster-
      registering outcomes might be "more real" in some registration sense.

  Why 2: Why must τ_reg(o) be outcome-specific for K9_C to be non-trivial?
    → For K9_C to produce any δP ≠ 0 (distinguish from Standard QM), g(τ_reg(o))
      must vary across outcomes o. If τ_reg is the same for all o, g cancels:
        Z_C = g · Σ_o Tr(E_o ρ) = g · 1 = g  →  P(o) = Tr(E_o ρ).
      So non-trivial K9_C REQUIRES τ_reg(o) to be outcome-dependent (Interp B).
      This is the fundamental tension: the formula needs τ_reg(o) to depend on
      o, but τ_reg(o) must be evaluated before o is known.

  Why 3: What does K1 define, and why does it not anchor τ_reg(o)?
    → K1 (L119-L168) defines the K-state tuple as k = ⟨M, o, cert, t, V⟩.
      The field t ∈ T_R is the registration TIMESTAMP (when the registration
      event completed). K1 does NOT define:
        — t_init: time at which measurement initiation began
        — τ_reg(o) = t(k_o) − t_init: registration LATENCY (duration)
      The K-state records WHAT was registered (o) and WHEN completion occurred (t),
      but NOT HOW LONG the registration process took. K1's design focus is on
      registration-logic completeness (admission, ordering) — not registration
      dynamics (duration, latency, speed).

  Why 4: Why can't K5_prospective (v29) or T8/T9 (v31) rescue K9_C?
    → K5_prospective evaluates: "IF outcome o were registered, WOULD k5_o* be
      contradicted?" — this concerns VALIDITY (⊥_K contradiction), not LATENCY.
      K5_prospective does not add τ_reg(o) to K-state, does not define t_init,
      and provides no outcome-differential timing mechanism.
      T8 (K5_prospective Frequency Bridge) bridges K5_prospective to K9_E's
      f_perp — it concerns ⊥_K suppression, not latency weighting.
      T9 (K_ctx Construction via φ_ij) formalizes morphism channels — not latency.
      None of v29-v31 introduces τ_reg as a K-state field.

  Why 5: What would it take to fix the circularity within K1-K8?
    → Three candidate fixes, all blocked:
      (F1) Make τ_reg outcome-independent: τ_reg(o) = τ_reg for all o.
           Circularity disappears. But g cancels → P = Tr(E_o ρ). FAIL.
           This is Interpretation A. Same algebraic mechanism as K9_B PP-2-SI.
      (F2) Derive τ_reg(o) from Hamiltonian H: τ_reg(o) = f(H, E_o).
           Not circular (H, E_o are pre-measurement quantities). BUT:
             (a) f is unspecified;
             (b) H is a QM H-space operator, not a K-space field;
             (c) incorporating H requires φ-map bridge (Track B, Class D,
                 unproven);
             (d) τ_reg(o) is still not a K-state field — K1 extension
                 k = ⟨M,o,cert,t,V,τ_reg(o)⟩ is FROZEN.
      (F3) Extend K-state with τ_reg vector: k = ⟨M,o,cert,t,V,τ_reg(o)⟩.
           Layer 1 architectural change. FROZEN (CLAUDE.md §Identity).
           Cascades to T1-T9 and all K9_A-F formulas.

      Root cause: K1-K8 were designed to axiomatize registration-LOGIC
      (when events are valid, how they are ordered, when they contradict).
      Registration-DYNAMICS (how fast registration completes, latency per
      outcome) is outside this design scope. τ_reg(o) is a dynamics concept;
      the K-state tuple is a logic-record concept.
      The circularity is not a bug in K9_C's formulation but a STRUCTURAL
      TENSION within frozen K1-K8: any τ_reg-based K9 that is simultaneously
      (a) outcome-dependent and (b) pre-registration-evaluable requires a
      K-state field that K1-K8 do not and cannot provide without a Layer 1
      extension.
```

**Layer 0 conclusion:** K9_C's core failure is a registration-dynamics / registration-logic boundary violation. Under Interpretation A the dynamics factor cancels (FAIL). Under Interpretation B the dynamics factor requires a frozen K-state extension (FIXABLE in principle, blocked in practice). Layer 0 sets the standard for judging each component in Layer 1: does this component respect or violate the dynamics/logic boundary?

---

## Layer 1 — Per-Component RCA

*Full 5-Whys chains for H ≥ 5 OR Trace = 0/6. Components with H ≤ 4 have 3-Why summaries in the traceability matrix.*

### C-02 — τ_reg(o) Outcome-Dependent Latency [A-C1] — H=6, Trace=1/6

```
5-Whys for C-02:

  Symptom: K9_C contains τ_reg(o) as ASSUMPTION [A-C1] with no K1-K8 anchor.

    Why 1: What is τ_reg(o) physically?
      → τ_reg(o) = t(k_o) − t_init: elapsed time from measurement initiation
        (t_init) to K-side registration completion of outcome o. In practice:
        detector click time, photon detection latency, fluorescence decay time,
        qubit readout time. Outcome-specific latencies exist in real experiments
        and can differ across POVM elements. The concept is physically real.

    Why 2: Why is t_init not in the K-state tuple?
      → K1 defines k = ⟨M, o, cert, t, V⟩. The field t is the registration
        COMPLETION timestamp. K1's design: a K-state records the COMPLETED
        registration event — WHAT was registered and WHEN it was logged. t_init
        is a measurement-setup timestamp, logically prior to K-state creation.
        K1 does not model the internal dynamics of registration initiation.

    Why 3: Why can't τ_reg(o) be derived from K2's temporal structure?
      → K2 (L171-L214) defines temporal ORDER (strict total order via t-values)
        and cites Kṣaṇabhaṅgavāda (discreteness) as BE lineage. K2 axiomatizes
        the ORDER of completed events, not their DURATION. τ_reg(o) is a duration
        quantity; K2 provides no mechanism for extracting t_init from the
        ordering structure of completed events.

    Why 4: Why is the EX anchor (N_QM_VVV_00039) compass-only?
      → N_QM_VVV_00039 (Momentary Registration Series) conceptually maps
        kṣaṇabhaṅga to sequential registration moments. Per CLAUDE.md §VVV-QMRF
        core/EX integration rule: EX nodes do not contribute to Trace_Score.
        N_QM_VVV_00039 provides conceptual alignment but does not anchor τ_reg(o)
        as a K-state field or specify how to compute it.

    Why 5: Can τ_reg(o) be salvaged via a non-circular Hamiltonian model?
      → Physically YES. In principle: τ_reg(o) ∝ ħ/ΔE_o (energy-time
        uncertainty), or τ_reg(o) = 1/Γ_o (inverse decay rate), or τ_reg(o)
        from quantum Zeno time ∝ ħ/‖H|ψ_o⟩‖. These are NOT circular (computed
        from H, E_o without using P). But: (a) none is specified in
        K9S2_candidate_C; (b) H is an H-space operator (not K-space); (c)
        connecting H to τ_reg requires φ-map (Track B, Class D).
      Root cause: [A-C1] is physically motivated but formally unanchored in
      K1-K8. H=6 (YELLOW) reflects: concept is real (not fabricated), but
      K1-K8 anchor is absent.
      Fix path: Defer ([AH-DEFER]) until Interp B model is specified.
```

---

### C-06 — Kṣaṇabhaṅga BE Interpretation — H=5, Trace=2/6

```
5-Whys for C-06:

  Symptom: K9_C uses kṣaṇabhaṅga to motivate τ_reg-based probability
           weighting. K2 uses kṣaṇabhaṅga to ground temporal discreteness.
           The interpretive jump from discreteness to weighting is unsupported.

    Why 1: What does kṣaṇabhaṅga actually claim?
      → N_BE_00087 (Kṣaṇabhaṅgavāda, L147-L149): doctrine that a moment
        disappears as soon as it appears — radical momentariness. N_BE_00086
        (Momentariness, L147-L149, L303-L305): reality is fluxional and
        momentary. N_BE_00247 (Dharmakīrti's momentariness, L303-L305):
        fundamental Sautrāntika commitment — existence = momentary causal event.
        Core claim: what EXISTS is momentary; each kṣaṇa is discrete and
        causally efficacious in its instant.

    Why 2: What does K2 derive from kṣaṇabhaṅga?
      → K2 (L206-L214) cites Kṣaṇabhaṅgavāda as BE lineage to ground:
        "registration time is discrete; no continuous registration-state
        identity between events." K2 uses momentariness to justify DISCRETENESS
        of temporal registration structure — not any probability weighting.

    Why 3: What interpretive step does K9_C add beyond K2?
      → K9_C says "faster registration = higher probability." This is NOT
        implied by N_BE_00087 (kṣaṇabhaṅga does not say faster moments are
        more probable) or K2 (discreteness of timestamps says nothing about
        PROBABILITY of different outcomes). K9_C maps kṣaṇabhaṅga's "momentary
        causal reality" to "shorter τ_reg = more probable" — two unjustified
        steps: (i) causal reality → probability magnitude; (ii) registration
        speed → causal reality proxy.

    Why 4: Is the interpretive extension a category boundary violation?
      → Per CLAUDE.md §Terminology: "Treat cross-domain links as analogies
        or mappings unless the text explicitly argues for equivalence."
        The jump from "momentary causal efficacy" (BE ontology) to "probability
        weight via registration speed" (statistics) is an inter-domain
        analogical extension without formal justification. This is a category
        boundary: BE ontology ≠ probability rule.

    Why 5: Why H=5 (YELLOW) rather than higher?
      → BE anchor (N_BE_00087, N_BE_00086) IS present (SOT-1) and K2 BE
        lineage IS Kṣaṇabhaṅgavāda (SOT-2). Trace = 2/6 (MODERATE). Issue
        is not that kṣaṇabhaṅga is fabricated — it is well-anchored.
        Issue is INTERPRETIVE SCOPE OVEREXTENSION. H=5 reflects: anchored
        concept with overextended application.
      Root cause: Analogical extension of kṣaṇabhaṅga beyond K2's scope.
      Fix: PS-1 boundary note in K_Space §K2 — "K2 BE lineage establishes
      discreteness only, not probability weighting via registration speed."
```

---

### C-07 — Arthakriyā → Probability Weight — H=5, Trace=1/6

```
5-Whys for C-07:

  Symptom: K9_C maps arthakriyā to probability weighting via registration
           speed. N_BE_00022 defines arthakriyā as an ontological existence
           criterion, not a probability-weighting principle.

    Why 1: What does arthakriyā formally mean in BE SOT?
      → N_BE_00022 (Arthakriyā, L73, L171-L173): (1) Ontological — causal
        efficacy as criterion of EXISTENCE (only what can perform a function
        exists ultimately). (2) Epistemological — to fulfill a practical
        purpose (puruṣārthasiddhi). N_BE_00197 (L171-L173): only what can
        perform a function exists ultimately. Core claim: arthakriyā = existence
        test. NOT: arthakriyā = probability magnitude.

    Why 2: How does K9_C use arthakriyā?
      → K9_C's implicit chain: faster τ_reg → event registers (completes
        causal act) sooner → more causally efficacious (arthakriyā) → "more
        real" → higher probability. Treats P(o) as proportional to causal
        efficacy of the registration process.

    Why 3: Is this mapping supported by N_BE_00022's formal content?
      → NO. N_BE_00022 is a binary existence criterion, not a graduated
        probability rule. Arthakriyā asks "does this causally act?" (yes/no),
        not "how much does it causally act?" (magnitude). N_BE_00198
        (Arthakriyā as practical success) concerns COGNITION VALIDITY, not
        outcome probability.

    Why 4: What formal bridge would be needed?
      → A Bridge Theorem: "arthakriyā-degree ∝ registration speed ∝
        probability magnitude" — requiring (a) continuous arthakriyā degree
        (not in BE SOT — arthakriyā is used as existence qualifier, not
        magnitude), (b) formal K→BE ontology connection, (c) Class C K9
        postulate justification. None provided.

    Why 5: Why H=5 (YELLOW) rather than ORANGE?
      → N_BE_00022 is correctly cited and understood. The error is scope
        extension, not fabrication. Trace=1/6 (SOT-1 only). H=5: anchor
        exists, interpretive use exceeds formal scope.
      Root cause: Arthakriyā is an ontological existence criterion; using
      it as a probability-weighting motivation requires a Bridge Theorem
      currently absent from T1-T9. Without it: analogical only [AH-WARN].
```

---

### C-09 — Circularity: τ_reg(o) Requires Knowing o — H=8, Trace=0/6

*Layer 0 provides the full meta-circularity analysis. This Layer 1 chain focuses on the component-level resolution paths.*

```
5-Whys for C-09:

  Symptom: τ_reg(o) = t(k_o) − t_init requires knowing which outcome o
           occurred. P(o|k,H) must be assigned BEFORE o is observed. Circular.

    Why 1: When is P(o|k,H) used?
      → P(o|k,H) is a PRE-registration predictive probability — evaluated
        before the measurement outcome is known. It is the Born-rule role:
        "given K-context k and H, what is P of registering outcome o?"

    Why 2: When can τ_reg(o) be known?
      → τ_reg(o) = t(k_o) − t_init. t(k_o) is defined AFTER outcome o is
        registered (K1). τ_reg(o) is POST-registration; P(o|k,H) is
        PRE-registration. Temporal inconsistency: the formula requires a
        post-registration quantity as a pre-registration probability input.

    Why 3: What is the only non-circular resolution?
      → τ_reg(o) must be computed from quantities known BEFORE measurement:
        H (Hamiltonian), {E_o} (POVM), ρ (state). If τ_reg(o) = f(H, E_o, ρ),
        it is pre-registration and non-circular. Candidate models:
          f_Zeno: τ_reg(o) ∝ ħ / ‖H E_o‖
          f_decay: τ_reg(o) = ħ / Tr(E_o H E_o)
        These are physically motivated but none is specified in K9_C.

    Why 4: Why is C-09 an ORPHAN (Trace=0/6)?
      → Circularity is a logical issue internal to K9_C's formulation.
        No SOT (SOT-1 through SOT-6) addresses self-referential τ_reg.
        K1-K8 are silent on registration latency. Standard QM (SOT-5)
        does not weight outcomes by detector speed. Proietti (SOT-6)
        does not measure per-outcome τ_reg. The circularity is K9_C's
        own structural problem — no external SOT can anchor its resolution.

    Why 5: Root cause of C-09?
      Root cause: τ_reg(o) is a registration-DYNAMICS quantity (posterior
      to registration completion) while K9_C uses it as an input to a
      registration-LOGIC probability rule (anterior to registration).
      K1-K8 architecture: K-state is a COMPLETED registration record.
      Any formula including post-registration dynamics as a pre-registration
      probability input violates the temporal ordering of the K-architecture.
      Fix: (A) τ_reg outcome-independent [→ FAIL], or (B) specify pre-
      registration f(H, E_o) model + Layer 1 extension [→ deferred].
```

---

### C-11 — Interpretation B: K-State Extension — H=7, Trace=0/6

```
5-Whys for C-11:

  Symptom: Interpretation B requires τ_reg(o) as a genuine K-state field
           varying across outcomes. K1's 5-field tuple is FROZEN.

    Why 1: Why would τ_reg(o) need to be a K-state field?
      → For P(o|k,H) to be a K9-level postulate in VVV-QMRF, τ_reg(o) must
        be a K-side property. If it lives entirely on the QM H-side, K9_C
        becomes a QM postulate, not a K-space postulate — outside VVV-QMRF
        scope boundary.

    Why 2: What would the extension look like formally?
      → Option 1: k = ⟨M, o, cert, t, V, τ_reg(o)⟩ [6-field tuple].
        Option 2: τ_reg: O → ℝ⁺ as an outcome-indexed map attached to M.
        Either requires redefining K1's K_R = {k | k = ⟨...⟩} — a Layer 1
        axiom text change (FROZEN).

    Why 3: Why is Layer 1 FROZEN for this extension?
      → CLAUDE.md §Identity (Layer 1 FROZEN): K1-K8 axiom text is frozen.
        Adding τ_reg(o) would: (a) change K1's formal definition (frozen text),
        (b) require K2 re-verification (new field in ordering?), (c) require
        T1 update (K_joint construction), (d) cascade to all K9_A-F formulas.
        Architectural change with wide blast radius.

    Why 4: Is there a path avoiding Layer 1 extension?
      → Yes: τ_reg(o) = f(H, E_o) as EXTERNAL function computed from QM side,
        feeding into K9_C as an external parameter (not K-state field). This
        treats τ_reg as H-side input rather than K-side property. Requirements:
        (a) explicit f specification (currently absent), (b) φ-map bridge
        (Track B, Class D, unproven), (c) reformulation separating K-side
        from H-side input. Path is theoretically open but practically deferred.

    Why 5: Why is C-11 an ORPHAN (Trace=0/6)?
      Root cause: K-state extension proposal has no SOT anchor. SOT-2/3
      (K_Space Axiomatization) DEFINES the frozen tuple and implicitly PROHIBITS
      extension without PEER-SYNC. The proposal is an internal K9_C construction
      with no prior SOT precedent. [AH-ORPHAN] + [AH-DEFER]: structurally
      coherent idea, cannot be anchored in current frozen framework.
      Fix: Label [AH-DEFER]. Re-open when Layer 1 extension formally considered.
```

---

### C-12 — K-State Extension Blocked by Frozen K1-K8 — H=7, Trace=1/6

```
5-Whys for C-12:

  Symptom: K1's 5-field tuple is frozen. Adding τ_reg(o) is architecturally
           blocked at the Layer 1 boundary.

    Why 1: Why is Layer 1 frozen?
      → CLAUDE.md §0.5: "Layer 1 — CORE AXIOMS (K1-K8): Frozen (syntactic)."
        The FREEZE is a stability mechanism: K1-K8 form the invariant foundation
        on which all downstream theorems (T1-T9) and K9_A-F rest. Changing K1-K8
        text would invalidate the entire derived structure.

    Why 2: What precedent exists for this frozen boundary?
      → K9_B audit (P2, B-09): SNR escape route (N_QM_VVV_00031) confirmed
        CLOSED because adding SNR to K-state requires unfreezing Layer 1.
        K9_B Layer 2 Cluster C-1: "K1-K8 fields are not statistical outcome
        weights. Any K9 of the form P = Tr(E_o ρ) · g(K-logic fields) inherits
        this boundary and cancels in normalization." K9_C faces analogous
        constraint for τ_reg.

    Why 3: Does the frozen boundary mean K9_C is permanently dead?
      → NO. K9_C is FAIL-FIXABLE, not FAIL-FATAL. K9_B's PP-2-SI impossibility
        was algebraic (per-tuple constants cancel regardless). K9_C's failure
        under Interp A is algebraic (same). But Interp B has a conditional path:
        if a non-circular f(H, E_o) is specified AND Layer 1 extension is
        formally considered (PEER-SYNC), K9_C Interp B could become viable.
        Frozen boundary DEFERS, does not eliminate.

    Why 4: What would a Layer 1 extension process look like?
      → Per CLAUDE.md §PEER-SYNC: (1) formal proposal, (2) impact assessment
        on T1-T9 and K9_A-F, (3) 5-Whys RCA on necessity (RULE ZERO),
        (4) PEER-SYNC edit to both K_Space copies simultaneously,
        (5) update all downstream references. Significant undertaking — justified
        only if Interp B produces detectable δP and non-circular f is validated.

    Why 5: Root cause of H=7 (ORANGE) for C-12?
      Root cause: C-12 is ORANGE because it represents a genuine unresolved
      tension between K9_C's potential (Interp B could be physically meaningful)
      and the architectural boundary (Layer 1 FROZEN). The tension is deferred,
      not resolved. Trace=1/6: SOT-2 K1 definitively specifies the 5-field tuple,
      providing a negative anchor confirming τ_reg's absence.
```

---

## Layer 2 — Cluster RCA

**Trigger check:**
- Orphans ≥ 2? **YES** — C-09 (0/6) and C-11 (0/6). Condition 1 MET.
- ≥ 3 components share upstream "Why"? **YES** — C-02, C-08, C-09, C-11, C-12 all trace to "K1-K8 has no τ_reg field in the K-state tuple." Condition 2 MET.
- ≥ 2 components with interpretation-split ambiguity? **YES** — C-09, C-10, C-11 all resolve around the Interp A/B bifurcation. Condition 3 MET.

**Layer 2 triggered: all three conditions MET. One primary cluster identified (C-C1).**

### Cluster C-C1: No-τ_reg Cluster (C-02, C-08, C-09, C-11, C-12)

```
Cluster C-C1: "K1-K8 contains no τ_reg field in the K-state tuple"
  Affected components: C-02 (τ_reg assumption), C-08 (H-bridge assumption),
                       C-09 (circularity), C-11 (Interp B extension),
                       C-12 (frozen K1 constraint)
  Shared symptom: All five fail to find a K-state anchor for τ_reg(o).

    Why 1: Why do C-02, C-08, C-09, C-11, C-12 all converge to "no τ_reg"?
      → K1 defines k = ⟨M, o, cert, t, V⟩ — a 5-field LOGIC tuple.
        The five fields were chosen to cover measurement identity (M),
        outcome (o), admission (cert), ordering (t), validity (V).
        These are exactly what K2-K8 require. τ_reg was NOT needed for any
        of K2-K8: K2 needs t (not τ_reg) for ordering; K3 needs cert;
        K4-K5 need V and ⊥_K; K6 needs cert; K7-K8 need t.
        τ_reg is a DYNAMICS property orthogonal to all K2-K8 logic operations.

    Why 2: Why is this a principled boundary rather than a design oversight?
      → K1-K8 axiomatize REGISTRATION-LOGIC (admitting, ordering, validating,
        authenticating, closing, preserving registration events). Structurally
        analogous to K9_B's Layer 2 Cluster C-1 finding: "K1-K8 fields are not
        statistical outcome weights." Similarly: K1-K8 fields are not
        registration-dynamics quantities. K-space is a LOGIC space, not a
        DYNAMICS space. τ_reg(o) lives on the H-side (determined by H and POVM),
        not on the K-side (K1-K8 registration logic).

    Why 3: What makes C-C1 different from K9_B's Cluster C-1?
      → K9_B Cluster C-1 (per-tuple anchoring) was FATAL: K-logic fields
        algebraically cancel regardless of their values. C-C1 here is FIXABLE:
        τ_reg(o) is not a per-tuple constant — it CAN vary across outcomes (Interp B).
        The difference:
          K9_B: K-logic fields are proven outcome-independent → FAIL-FATAL.
          K9_C: τ_reg is ABSENT from K-state → fix requires specifying τ_reg
                as a non-circular external function f(H, E_o).
        K9_C is FAIL-FIXABLE because τ_reg absence is a missing-field
        problem, not an algebraic-impossibility problem.

    Why 4: Does C-C1 have any escape route within frozen K1-K8?
      → Only Interpretation B path (B1): τ_reg(o) = f(H, E_o) computed
        externally from QM H-side, fed as external parameter (not K-state field).
        Avoids Layer 1 extension by treating τ_reg as H-side input. Requirements:
          (a) Explicit f(H, E_o) specified (unmet currently)
          (b) Reformulation of K9_C separating K-side formula from H-side input
          (c) Verification that f produces detectable δP
          (d) Possible φ-map bridge (Track B, Class D)
        This is the only C-C1 escape within frozen K1-K8. All five cluster
        components must be revisited once f is specified.

    Why 5: What does C-C1 imply for P4 (K9_D) and P5 (K9_E) deep reviews?
      Root cause: C-C1 reveals that any K9 candidate requiring K-state dynamics
      fields (not in K1's 5-field tuple) will face the same cluster.
        K9_D (Certification Discount): uses cert and α. cert is in K-state;
        α is a per-tuple constant → same PP-2-SI FAIL-FATAL as K9_B. P4 should
        confirm this quickly (expected 1-layer RCA, no new cluster needed).
        K9_E (⊥_K Suppression): uses f_perp(K_ctx). K_ctx is derivable via
        K5_prospective (T9) and is GENUINELY per-outcome-evaluation. K9_E was
        designed precisely to avoid both C-C1 and PP-2-SI. P5 should verify
        that f_perp is outcome-dependent and that K_ctx is not a per-tuple
        constant — this is the critical verification for Class C status.
        K9_F (Colimit Probability): uses T4-H Steps 2-4 (DEFERRED). C-C1
        irrelevant until T4-H is proven.
      Priority: MEDIUM (informational for P4-P6; confirms structural boundary)
```

---

## Layer 3 — Verdict-Level RCA

**Question:** After Layers 0–2, is the FAIL-FIXABLE verdict still locked? Does any v29–v31 update affect K9_C?

```
Verdict RCA:
  K9-S2 verdict (2026-05-23): FAIL-FIXABLE — τ_reg circularity and
  outcome-independence cancellation. 3-round RCA: ≥ 4.5/5 all rounds.
  Root cause (K9-S2): τ_reg not in K1-K8; Interp A → FAIL; Interp B →
  needs non-circular model + K-state extension.

  Post-deep-review question 1: Do v29-v31 updates affect K9_C?
    Why 1: What are the relevant v29-v31 updates?
      → v29 (2026-05-23): K5_prospective (P9 bridge for K9_E). T9 (K_ctx
        Construction via φ_ij).
        v30 (2026-05-24): P10-NOISE analysis (K9_E Class C qualified).
        v31 (2026-05-24): K9E-PAT CLOSED (UNRESOLVABLE, RCA 4.92/5). T8
        (K5_prospective Frequency Bridge).
    Why 2: Do K5_prospective or T8 interact with K9_C?
      → K5_prospective evaluates ⊥_K for hypothetical outcome tuples —
        concerns VALIDITY, not LATENCY. τ_reg requires t_init, not ⊥_K.
        K5_prospective does not add τ_reg to K-state. T8 bridges
        K5_prospective to K9_E's f_perp — orthogonal to τ_reg.
    Why 3: Could T9 (K_ctx construction via φ_ij) help K9_C?
      → T9 formalizes morphism channels φ_ij connecting K_R to B(H).
        In principle φ_ij could eventually provide a path to derive τ_reg(o)
        from H. But T9 as formulated does not produce τ_reg values —
        it produces K_ctx context information. Even if T9 eventually provided
        τ_reg-like quantities, K9_C would need a K-state field or an explicit
        external-parameter reformulation.
    Why 4: Does K9E-PAT CLOSED affect K9_C's FAIL-FIXABLE status?
      → K9E-PAT CLOSED defers the multiplicative-vs-additive ambiguity to
        K9-S12 experiment — entirely K9_E-specific. K9_C's verdict depends
        on τ_reg circularity and Layer 1 FROZEN constraint, not on K9_E's
        empirical ratio analysis.
    → Update verdict: UNCHANGED. v29-v31 updates are K9_E/T-specific.

  Post-deep-review question 2: Does C-C1 (No-τ_reg Cluster) remain open?
    Why 1: Is τ_reg(o) now axiomatized by any v29-v31 addition?
      → NO. K5_prospective, T8, T9 do not add τ_reg to K-state. K1 remains
        k = ⟨M,o,cert,t,V⟩. No t_init added.
    Why 2: Could T4-H (colimit) enable Interp B?
      → T4-H (Steps 2-4 DEFERRED) creates multi-observer K_joint — not a
        τ_reg weighting mechanism within individual K_R. T4-H relevant to
        K9_F, not K9_C.
    Why 3: Does Proietti 2019 data constrain K9_C?
      → K9_C not advanced to data fit (FAIL-FIXABLE pre-eliminated). No
        Proietti constraint.
    → C-C1 confirmed OPEN (deferred with [AH-DEFER]).

  Final reconciliation:
    K9_C's FAIL-FIXABLE verdict is confirmed by P3 deep review with no
    modifications to the K9-S2 (2026-05-23) verdict.
    FAIL (Interp A: τ_reg outcome-independent → PP-2-SI cancellation):
      If τ_reg(o) = constant for all o, Z_C = g·1 = g, P(o) = Tr(E_o ρ).
      Algebraically identical to K9_B failure. δP = 0. FAIL.
    FIXABLE (Interp B: τ_reg outcome-dependent → deferred):
      Requires explicit non-circular f(H, E_o) + Layer 1 extension review.
      Two orphans (C-09 circularity, C-11 Interp B extension) labeled
      [AH-DEFER]. Structurally coherent, blocked in current frozen framework.
    No v29-v31 update introduces τ_reg as K-state field.
    C-C1 cluster (5 components) confirms registration-dynamics /
    registration-logic design boundary as root cause.
    One PEER-SYNC suggestion (PS-1: K2 boundary note).
    Verdict: FAIL-FIXABLE LOCKED.
```

---

## Aggregate RCA Findings

**Dominant root cause of K9_C's failure (one sentence):**
K1's 5-field K-state tuple axiomatizes registration-logic (admission, ordering, validity) but contains no registration-dynamics field — making τ_reg(o) unavailable as a K-side mechanism; under Interpretation A this forces algebraic cancellation (FAIL), and under Interpretation B it requires a frozen Layer 1 extension blocked until an explicit non-circular f(H, E_o) model is provided.

**Secondary finding from Layer 2 Cluster C-C1:**
Five components converge to the same root-level gap: K1-K8's principled design boundary between registration-LOGIC and registration-DYNAMICS. This boundary is structurally analogous to K9_B's per-tuple cancellation boundary (Layer 2 Cluster C-1) but differs in outcome: K9_C is FAIL-FIXABLE (not FAIL-FATAL) because τ_reg is absent (missing-field problem) rather than algebraically cancelled (impossibility theorem).

**PEER-SYNC finding (PS-1):**
K2's kṣaṇabhaṅga BE lineage grounds temporal discreteness only — not probability weighting by registration speed. Suggest adding a boundary note to K_Space_Axiomatization.md §K2 Boundary cell. Open separate PEER-SYNC ticket before editing.

**Impact on P4 (K9_D) and P5 (K9_E) deep reviews:**
- P4 (K9_D): K9_D uses cert and discount factor α (per-tuple constant). C-C1 pattern + PP-2-SI predicts FAIL-FATAL via same algebraic cancellation as K9_B. P4 should confirm quickly.
- P5 (K9_E): K9_E uses f_perp(K_ctx). C-C1's cluster finding raises the critical question: IS f_perp genuinely outcome-dependent (not per-tuple)? K5_prospective (v29) and T9 (v31) were designed precisely to ensure K_ctx is per-outcome-evaluation. P5 must verify this — it is the core validation for K9_E's Class C survival.

---

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-05-27 | v0.1 | P3 execution. Layer 0–3 complete. 12 components (C-01…C-12). Layer 2 triggered (conditions 1+2+3). Cluster C-C1 (No-τ_reg, 5 components). FAIL-FIXABLE confirmed. 2 orphans (C-09, C-11) labeled [AH-DEFER]. PS-1 (K2 boundary note). |
