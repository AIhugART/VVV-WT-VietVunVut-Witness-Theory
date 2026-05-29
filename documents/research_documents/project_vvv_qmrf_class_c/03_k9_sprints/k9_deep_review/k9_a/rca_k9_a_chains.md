Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chains — K9_A Deep Review

**Target:** K9_A — V-Filter (Three-Case, EX-Enriched)
**Date:** 2026-05-27
**Phase:** P1 (deep review execution)
**Companion files:** [plan_k9_a_deep_review.md](./plan_k9_a_deep_review.md), [report_k9_a_traceability_matrix.md](./report_k9_a_traceability_matrix.md)
**Method:** 4-layer RCA per plan §4

---

## Layer 0 — Meta-RCA on K9_A's existence

```
Symptom: K9_A claims to bridge binary K-state (V ∈ {0,1}) to continuous probability,
         but reduces to standard Born rule in Case 1 (δP=0) and assigns no P in Cases 2–3.

  Why 1: What forces a probability rule beyond K1–K8?
    Answer: K1–K8 produce only binary outputs (cert, V, ⊥_K firing). They define
            registration validity but do NOT assign a probability to any outcome.
            Standard QM needs P(o) ∈ [0,1] via Born rule. Without a K9, K-space has
            no bridge from binary registration logic to continuous probability —
            a gap explicitly identified in K9-S1 §C-FALSI and master plan §0.5.

  Why 2: Why a *V-filter* form and not direct Born rule?
    Answer: Direct Born rule (P=Tr(E_o ρ)) for every k would ignore K4/K5 entirely
            (validity status would be irrelevant for probability). K9_A is the
            MINIMAL form that USES K4/K5: it conditions probability assignment on
            V(k) and isNull(k). The V-filter is "respect K4/K5 without modifying QM".

  Why 3: What forces the three-case partition (V=1, V=0, isNull)?
    Answer: K4 has TWO clauses — K4(a) ¬isNull → V=1 (default) and K4(b) isNull → V=0.
            K5 produces a third state: ¬isNull AND V=0 (registration was valid, then
            invalidated by bādhaka). PP-1 v2 v0 originally conflated V=0 and isNull
            into a single "N_null" category; EX compass (N_QM_VVV_00032 vs
            N_QM_VVV_00020) revealed they are STRUCTURALLY DISTINCT
            (Bhrānti vs Anupalabdhi). Hence three cases.

  Why 4: Why is v_rate introduced at population level, not per-event?
    Answer: V(k) is a per-tuple field (K1: k = ⟨M, o, cert, t, V⟩). Per-event,
            V is binary {0,1}, not [0,1] — so no continuous parameter exists per event.
            The continuous fitting target is the FREQUENCY at which V=1 obtains across
            an ensemble. PP-1 v2 §Round 1 W3 explicitly diagnosed this: V is per-tuple,
            so the only continuous parameter K9_A can expose is the ensemble fraction
            v_rate := |{k : V(k)=1}| / N_runs.

  Why 5: What is the root structural necessity that K9_A satisfies?
    Root cause: K9_A is the minimal K9 form that
                  (a) recovers Born rule exactly when K-side registration is valid,
                  (b) explicitly USES K4/K5 (not just K1–K3) to gate probability,
                  (c) introduces exactly one continuous parameter (v_rate)
                      at the ensemble level — the minimum needed to make K9_A
                      empirically distinct from "ignore K-space, use Born rule directly".

    Implication: K9_A satisfies a MINIMAL DUTY: "make K4/K5 visible at the
                 probability layer". Other K9 candidates (K9_E ⊥_K Suppression,
                 K9_F colimit) go further by modifying probability per-event;
                 K9_A only modifies probability at the ENSEMBLE level via v_rate.
                 K9_A is the conservative baseline; K9_E/K9_F are stronger
                 modifications. K9_A does NOT uniquely satisfy the necessity.
```

**Layer 0 conclusion (one sentence):** K9_A exists as the *minimal* K9 that respects K4/K5 by gating Born-rule assignment on V(k) and isNull(k), exposing exactly one continuous degree of freedom (`v_rate`) at the ensemble level — making it conservative-by-construction and unable to produce per-event δP ≠ 0.

---

## Layer 1 — Per-Component RCA (full 5-Whys for H ≥ 5 OR Trace = 0/6)

Lightweight 3-Whys chains for all components live inline in `report_k9_a_traceability_matrix.md` §5 (column `RCA Summary`). The full 5-Whys chains below are only for components flagged H ≥ 5 OR Trace = 0/6 by §4 scoring.

Per Step 4 scoring against AHP `05_scoring.md`, the components requiring full RCA in this audit are:
- **A-09** `arthakriyā` lineage in K9_A definition body — H = 5 (BE node exists, but K9_A's `arthakriyā` usage is EX-mediated through `N_QM_VVV_00027`, not a direct K_Space anchor).
- **A-12** `bādhaka` term — H = 7, Trace = 1/6 (no dedicated BE node in 30-core or RCA-extension list; appears only as K5 BE-lineage label).
- **A-17** `v_rate` free parameter — H = 8, Trace = 0/6 (orphan: no L1/L2/L3 SOT anchor; ASSUMPTION [A1] per K9S2).
- **A-18** `N_bhranti` counter — H = 6 (ASSUMPTION [A2] with EX anchor only).
- **A-19** `N_null` counter — H = 6 (ASSUMPTION [A3] with EX anchor only).
- **A-20** "population parameter, not per-event" — H = 7, Trace = 0/6 (orphan: meta-assumption without SOT trace).
- **A-21** "No P assignment" semantics for Cases 2 & 3 — H = 5, Trace = 1/6 (custom to K9_A; partially aligns with K9-S1 C-NORM by construction).
- **A-22** EX enrichment marker (`EX N_QM_VVV_*`) — H = 5 (compass-only anchor by construction).
- **A-23** K9S2 anchor error (`isNull → K8`) — H = 6 (citation error discovered during audit; see Layer 2 C-3).

### A-09 — `arthakriyā` as K9_A's Case 1 lineage (H = 5, Trace = 2/6)

```
Symptom: K9_A Case 1 cites "Born Rule via arthakriyā (EX N_QM_VVV_00027)",
         but the K_Space axioms (K3, K4) reference arthakriyā only as BE lineage
         of svataḥ prāmāṇya, not as a primary derivation step for Born rule.
         The arthakriyā ↔ Born rule link is mediated by EX node N_QM_VVV_00027,
         not by K1–K8 directly.

  Why 1: Why does Case 1 cite arthakriyā instead of citing K4 directly?
    Answer: PP-1 v2 introduced the EX-enrichment to explain WHY V=1 events get Born rule:
            because they are arthakriyā-bearing (causally efficacious).

  Why 2: Why is the explanation routed through EX?
    Answer: K_Space K4 says V=1 means "valid by default", but does not link V=1
            to causal efficacy explicitly. The arthakriyā framing is BE-original
            (N_BE_00022) and was imported through EX (N_QM_VVV_00027) into K9_A.

  Why 3: Is the BE → K_Space link formal or interpretive?
    Answer: K4 BE lineage row in K_Space_Axiomatization.md L294 states:
            "Svataḥ prāmāṇya — intrinsic validity: a cognition is valid by default
             in virtue of its occurrence (arthakriyā — causal efficacy)".
            The link is BE LINEAGE annotation, not a formal axiomatic derivation.
            K9_A's use of arthakriyā as Case 1 lineage is therefore an INTERPRETIVE
            justification, not a structural derivation.

  Why 4: Does this affect the strength of Case 1?
    Answer: NO for Case 1's MATHEMATICAL content (it is just Born rule).
            YES for Case 1's NARRATIVE coupling to BE — if arthakriyā is interpretive
            only, then Case 1 = Standard QM regardless of arthakriyā framing.

  Why 5: Is this a definitional gap?
    Root cause: The BE → K_Space lineage map (svataḥ prāmāṇya → arthakriyā → V=1)
                is INTERPRETIVE, not derivational. K9_A inherits this interpretive
                framing without strengthening it.
    Fix candidate: Confirm (interpretive use is acceptable for Layer 0 narrative;
                   formal proof is in K4 + Born rule, both anchored).
    Affected siblings: A-10 (bhrānti for Case 2), A-11 (anupalabdhi for Case 3) — same
                       interpretive-vs-derivational status.
```

### A-12 — `bādhaka` term (H = 7, Trace = 1/6)

```
Symptom: K9_A Case 2 description says "K-side: registration exists but is erroneous
         (bādhaka-voided)". The term `bādhaka` appears as a NAMED MECHANISM but has
         NO dedicated N_BE node in either the 30-core list (N_BE_00001–00030) or
         the RCA-extension list searched.

  Why 1: Where does `bādhaka` come from?
    Answer: From K_Space_Axiomatization.md K5 BE lineage L385:
            "Parataḥ prāmāṇya — invalidity is detected extrinsically.
             Bādhaka pramāṇa — a contradicting cognition (bādhaka)
             retroactively voids the earlier cognition."

  Why 2: Why doesn't `bādhaka` have its own BE node?
    Answer: The 30-node BE core focuses on pramāṇa schema (means/instrument of valid
            cognition). `Bādhaka` is a sub-mechanism — a TYPE of cognition that
            invalidates another, structurally subsumed under N_BE_00006 (Erroneous
            cognition / bhrānti, but acting as the AGENT not the patient).

  Why 3: Is `bādhaka` traceable to any BE source doc?
    Answer: YES indirectly — Source doc L259–263 mentions Erroneous cognition;
            paper v2.0 §4.4 formalizes act-level contradiction. But there is no
            line in `system_be_full.md` defining `bādhaka` as a standalone node.

  Why 4: Does K_Space §K5 anchor it?
    Answer: K_Space K5 USES `bādhaka` as a BE-lineage label but does not derive
            it — the K5 formal block defines `⊥` (registered contradiction) and
            "valid cross-registration authority" without explicit reliance on
            the term `bādhaka`.

  Why 5: Is this a SOT gap or a label/term mismatch?
    Root cause: `Bādhaka` is a BE doctrinal term used as a LABEL for the K5
                invalidation mechanism, but is not a formally registered node
                in the BE SOT. It is anchored via the doctrine of bhrānti
                (N_BE_00006) and the structural mechanism of K5 (registered
                contradiction), but does not have its own SOT entry.
    Fix candidate: Fix — file a BE SOT extension request:
                   "Add `bādhaka` as RCA-level node N_BE_XXXXX with source
                   doc reference L259–263 and edge to N_BE_00006 (acts on
                   bhrānti) and ED_BE_XX edge into K5 mechanism."
    Affected siblings: None (single term, but the resolution affects K_Space K5
                       documentation clarity).
```

### A-17 — `v_rate ∈ [0,1]` free parameter (H = 8, Trace = 0/6) — ORPHAN

```
Symptom: `v_rate` is the SOLE free parameter in K9_A's empirical content, but it
         has zero anchor in SOT-1, SOT-2/3, or SOT-5. K9S2 STEP 4 explicitly flags
         it as ASSUMPTION [A1] with only an EX anchor (N_QM_VVV_00032 ⇒ N_QM_00095
         decoherence). This makes v_rate ORPHAN per AHP convention.

  Why 1: Why is v_rate needed?
    Answer: PP-1 v2 Layer 0 W4: K9_A needs at least one continuous parameter to be
            empirically distinguishable from "ignore K-space + use Born rule"; v_rate
            is the only such parameter compatible with K1's per-tuple V.

  Why 2: Why is no K_Space axiom or K-Space theorem about ensemble V=1 fraction?
    Answer: K1–K8 are STRUCTURAL axioms about individual k-tuples and their relations.
            They do not predict or constrain ENSEMBLE statistics. K9_A's v_rate is an
            ensemble property, structurally orthogonal to K1–K8.

  Why 3: Is there a derived theorem (T1–T8) that gives v_rate?
    Answer: NO. T1 (K_joint), T2 (AdmJoint), T3 (Relativization), T4 (colimit), T7,
            T8 (K9_E bridge), T9 (K_ctx) all operate on individual k-tuples or
            categorical morphisms. None predicts ensemble V=1 fractions.

  Why 4: Could v_rate be derived from K7 closure dynamics or decoherence model?
    Answer: PARTIALLY — K9S2 STEP 7 notes v_rate < 1 requires "K5 ⊥_K firing in
            genuine EWF scenario". v_rate is then derivable from the ⊥_K firing
            rate, which itself depends on the physical decoherence rate
            (ρ-side, N_QM_00095). But this is not a K-space derivation — it is
            an ANCHORING to ρ-side physics.

  Why 5: Is v_rate a free parameter or an experimental input?
    Root cause: `v_rate` is a population-level quantity that K9_A CANNOT predict
                from K1–K8. It must be either (a) FIT to experimental data, or
                (b) DERIVED from a ρ-side decoherence model (out of K-space scope).
                Hence: ORPHAN in K-space, anchored only via EX compass to ρ-side.
    Fix candidate: Re-derive (link to K7 closure dynamics if possible; if not,
                   accept v_rate as a BOUNDARY VARIABLE — input to K-space, not
                   output) OR Defer with [AH-DEFER] until K9-S* sprint addresses
                   ensemble statistics from K-space.
    Affected siblings: A-18 (N_bhranti), A-19 (N_null), A-20 (population assumption).
                       All four orphans share the same root cause: K-space provides
                       no ensemble-statistics theorem.
```

### A-18 — `N_bhranti` counter (H = 6, Trace = 1/6)

```
Symptom: K9_A Case 2 declares "Event contributes to N_bhranti counter", but the
         counter is K9_A-defined, not K_Space-defined. EX compass anchors to
         N_QM_VVV_00032 (Registration Error), but no SOT-1/2/3 anchor exists for
         the OBSERVABLE.

  Why 1: Where is N_bhranti defined operationally?
    Answer: PP-1 v2 §Round 2: "N_bhranti(H) — count of Bhrānti events". Operational
            definition is "count of (¬isNull(k) ∧ V(k)=0) events in K_R".

  Why 2: Is this measurable in current experiments?
    Answer: NOT IN PROIETTI directly. Bhrānti events require detecting "registration
            occurred, then invalidated" — which requires either monitoring K5 firing
            in real time or post-hoc detecting V=1 → V=0 transitions. Proietti's
            CHSH-style dataset does not distinguish Case 1 from Case 2 events.

  Why 3: Is N_bhranti a K-space-derivable theorem?
    Answer: NO. Counts are ensemble quantities (same root cause as v_rate).

  Why 4: Is N_bhranti derivable from K-space + ρ-side model?
    Answer: YES if ⊥_K firing rate is computable from decoherence rate (ρ-side).
            This makes N_bhranti a HYBRID quantity (K-side definition, ρ-side
            statistics).

  Why 5: Is this acceptable for Class D?
    Root cause: `N_bhranti` is a K-space-defined OBSERVABLE without a current
                experimental discriminator. It is structurally consistent with K1–K5
                + EX, but not measurable in standard Wigner-friend datasets without
                purpose-built protocols.
    Fix candidate: Defer — operationalize in a dedicated K9-S* sprint
                   (suggested name: K9-S13 N_bhranti operationalization).
    Affected siblings: A-19 (N_null) — same status with different EX anchor.
```

### A-19 — `N_null` counter (H = 6, Trace = 1/6)

```
Symptom: K9_A Case 3 declares "Event contributes to N_null counter". Anchored via
         EX N_QM_VVV_00020 (Validated Absence) → N_QM_00033 (Null Measurement).
         BE anchor via N_BE_00253 (anupalabdhi, RCA-level not core).

  Why 1: Where is N_null defined?
    Answer: PP-1 v2 §Round 2: "N_null(H) — count of Anupalabdhi events". Operational
            definition is "count of isNull(k) events" = events where outcome o(k)=∅
            and ΔI(k)=0 (per K4 isNull definition).

  Why 2: Is N_null measurable?
    Answer: PARTIALLY. Null events ARE detected by null-detector dark counts in many
            experiments. The link "null detector dark count → isNull(k) event" needs
            EXPLICIT mapping; not all dark counts are anupalabdhi (some are noise).

  Why 3: Is N_null K-space-derivable?
    Answer: NO. Same ensemble-statistics root cause.

  Why 4: Is the QM substrate identified?
    Answer: YES — N_QM_00033 (Null Measurement) per EX.

  Why 5: What is the status?
    Root cause: Same as N_bhranti — K-space-defined observable, hybrid K+ρ statistics.
                Better experimental traction than N_bhranti (dark-count datasets
                exist), but still requires explicit "dark count → isNull" mapping
                to be operationalizable.
    Fix candidate: Defer — operationalize jointly with N_bhranti in K9-S* sprint.
    Affected siblings: A-18 (N_bhranti), A-17 (v_rate via constraint
                       v_rate = 1 − bhrānti_rate − null_rate).
```

### A-20 — "Population parameter, not per-event" meta-assumption (H = 7, Trace = 0/6) — ORPHAN

```
Symptom: K9_A definition specifies v_rate as "Population parameter, not per-event",
         making this a SCOPE CHOICE about how v_rate enters statistical analysis.
         The scope choice itself has no SOT anchor.

  Why 1: Why population, not per-event?
    Answer: Per-event v_rate would be circular: each event has V ∈ {0,1}, so per-event
            "rate" is just V itself. Population-level v_rate := |{k:V(k)=1}|/N is the
            only non-trivial reading.

  Why 2: Is "population" defined formally?
    Answer: NO. "Population" here means ensemble of K_R registration events in a
            single experimental run, but K_Space K1–K8 do not formalize ensembles —
            they formalize individual K_R structures.

  Why 3: Could "population" be formalized via T-theorems?
    Answer: T1 (K_joint) builds joint K-spaces; T3 (relativization) describes morphisms.
            Neither constructs an "ensemble" or a statistical sampling structure.

  Why 4: Is this a K-space gap or a methodological convention?
    Answer: BOTH. Methodologically, "population-level" is the standard frequentist
            interpretation of probability fits. Structurally, K-space lacks a
            statistical ensemble layer; "population" is borrowed from QM/statistics.

  Why 5: Is this fixable?
    Root cause: Same fundamental gap as A-17/A-18/A-19. K-space is single-K_R
                structural — it has no native ensemble theory. v_rate as a population
                parameter is an EXTERNAL methodological convention layered on top of
                K-space, not a K-space-internal construct.
    Fix candidate: Confirm (acceptable convention) OR Re-derive (introduce a
                   K-space ensemble structure as part of T4-H expansion).
    Affected siblings: A-17, A-18, A-19 — all share the missing ensemble layer.
```

### A-21 — "No P assignment" semantics for Cases 2 & 3 (H = 5, Trace = 1/6)

```
Symptom: Cases 2 and 3 declare "No P assignment" for V=0 (Bhrānti) and isNull
         (Anupalabdhi) events respectively. This is a NEW semantic outside Standard
         QM (which assigns Tr(E_o ρ) to every event).

  Why 1: Why no P assignment?
    Answer: V=0 (Case 2) means registration is invalid (K5 fired or K4(b) fires);
            Born rule presupposes a valid registration (svataḥ prāmāṇya).
            For isNull (Case 3), o(k) = ∅ — there is no outcome to assign P to.

  Why 2: Does this violate C-NORM?
    Answer: NO per K9S2 STEP 1 C-NORM: "V=0 and isNull: no P assigned →
            normalization vacuously satisfied". C-NORM applies to events that DO
            get a probability — for V=1 events, Σ_o Tr(E_o ρ) = 1 by POVM completeness.

  Why 3: Is this anchored in K_Space?
    Answer: NOT FORMALLY. K_Space K4(a) gives V=1 default; K4(b) gives V=0 for isNull;
            K5 gives V=0 for bādhaka-voided. None says "no P assignment". This is a
            K9_A DESIGN CHOICE consistent with — but not derived from — K_Space.

  Why 4: Is the alternative (P=0) wrong?
    Answer: PP-1 v2 Round 1 ROOT CAUSE: "V=0 ≠ P=0" — V=0 means erroneous
            REGISTRATION, not zero PROBABILITY of an outcome. P=0 would incorrectly
            equate registration error with vanishing outcome probability.

  Why 5: Is "no P" semantics a K9_A invention or BE inheritance?
    Root cause: It is a K9_A construction — a choice to handle invalid/null events
                by exclusion from P-assignment, justified by BE's distinction between
                arthakriyā (valid → P meaningful) and bhrānti/anupalabdhi (invalid →
                P not meaningful). Anchored interpretively in BE doctrine but not
                derived from K_Space axioms.
    Fix candidate: Confirm — interpretive anchor is consistent with K_Space; formal
                   derivation would require an extra K-axiom (e.g., "P is defined
                   only when V=1 ∧ ¬isNull"), which goes beyond Layer 1 frozen set.
    Affected siblings: A-22 (EX enrichment) shares the same interpretive-anchor status.
```

### A-22 — EX enrichment marker (`EX N_QM_VVV_*`) (H = 5, Trace = 1/6)

```
Symptom: K9_A definition explicitly cites EX nodes (N_QM_VVV_00027,
         N_QM_VVV_00032, N_QM_VVV_00020) inline as part of the candidate.
         EX is COMPASS-ONLY per parent program convention; it must not be
         counted toward Trace_Score as primary.

  Why 1: Why is EX cited in the definition itself?
    Answer: PP-1 v2 designed K9_A as "EX-Enriched" — using EX compass intelligence
            to distinguish Bhrānti (N_QM_VVV_00032) from Anupalabdhi
            (N_QM_VVV_00020), which the original PP-1 v1 conflated.

  Why 2: Does this violate the rule "EX is compass, not core"?
    Answer: NOT IF EX nodes are cross-traced to SOT-1 (BE). PP-1 v2 EX compass
            table DOES cross-trace each EX node to a BE node and a QM node.
            So EX is methodologically used as compass, then anchored.

  Why 3: But the K9_A definition text still cites EX directly — is that a problem?
    Answer: PRESENTATIONAL: yes, slightly. The EX references in the K9_A definition
            line could be replaced with BE/K_Space anchors (N_BE_00022 for Case 1,
            N_BE_00006 for Case 2, N_BE_00253 for Case 3) to make primary anchors
            explicit. Currently the EX framing makes the definition appear
            EX-dependent.

  Why 4: Is the dependence real?
    Answer: NO. The MATHEMATICAL content of K9_A (V=1 → Tr(E_o ρ), V=0 → no P,
            isNull → no P) is K_Space-anchored (K4, K5). EX is presentational and
            interpretive.

  Why 5: What is the action?
    Root cause: K9_A's definition body uses EX nodes as INTERPRETIVE labels even
                though primary anchors (BE + K_Space) exist. The choice is
                stylistic, not structural.
    Fix candidate: Fix (rewrite definition body to lead with primary SOT-1/2-3
                   anchors and relegate EX to a "compass" footnote).
                   OR Confirm (acceptable as long as report cross-traces every EX).
    Affected siblings: A-09, A-10, A-11 — same EX-presentational issue across the
                       three cases.
```

### A-23 — K9S2 anchor error: `isNull → K8` (H = 6, audit-finding)

```
Symptom: K9S2_candidate_A.md STEP 4 "Derivation Trace" anchors `isNull` to
         "K8 (absence axiom, L480-540)". K_Space_Axiomatization.md K4 clause (b)
         defines `isNull(k) := o(k) = ∅ ∧ ΔI(k) = 0` and assigns V=0; K8 is
         "Cross-Space Preservation", not an "absence axiom".

  Why 1: Why does K9S2 trace isNull to K8?
    Answer: Likely a citation lookup error: the author intended K4(b) but wrote K8.
            The line range "L480-540" does not match the K_Space versions current
            in Class C copy (where K4 spans roughly L255–L300).

  Why 2: Is the error material?
    Answer: For K9_A's MECHANICS: no — isNull → V=0 path is still anchored in K4(b)
            regardless of where the citation points. For AUDITABILITY: yes — a
            reader following K9S2 STEP 4 to K8 will not find an "absence axiom".

  Why 3: Has this been caught before?
    Answer: Not in the AHP top-10 list per `00_top_10_hallucinations_record.md`
            cross-reference (verify in report). This audit appears to be the
            first detection.

  Why 4: Is this part of a larger pattern of citation errors?
    Answer: POSSIBLE — line range "L96-100" for K1 admission rule and "L260-349"
            for K5 in K9S2 STEP 4 also need verification against current K_Space.
            (Current K_Space K5 spans roughly L300–L390 in Class C copy; not
            L260–349. These may reflect an older K_Space version.)

  Why 5: Is this a SOT integrity issue?
    Root cause: K9S2 was written against an EARLIER K_Space version; line ranges
                drifted but no peer-sync was performed for downstream derivative
                documents. This is a documentation-drift issue, NOT a structural
                K9_A defect.
    Fix candidate: Fix — open a PEER-SYNC suggestion: refresh K9S2_candidate_A.md
                   STEP 4 line ranges and correct `isNull → K8` to `isNull → K4(b)`.
                   Flag for the K9 Deep Review program's Layer 2 cluster (C-3
                   citation drift).
    Affected siblings: Likely affects K9S2 anchors for K1, K3, K4, K5 (other
                       line ranges may also have drifted). Layer 2 cluster
                       candidate.
```

---

## Layer 2 — Cluster RCA

**Trigger check (per plan §4 Layer 2 conditions):**
- ≥ 2 orphans (Trace = 0/6): **TRUE** — A-17 (v_rate), A-20 (population assumption) both orphans.
- ≥ 3 components share same upstream "Why": **TRUE** — A-17, A-18, A-19, A-20 all trace to "K-space lacks ensemble statistics theorem".
- ≥ 2 components depend only on PP-1 v2: **TRUE** — A-13 (three-case partition) and A-21 (no-P semantics) both have PP-1 v2 as derived-layer anchor only.

Layer 2 triggered. Three clusters identified:

### Cluster C-1 — K-Space Ensemble-Statistics Gap

```
Affected components: A-17 (v_rate), A-18 (N_bhranti), A-19 (N_null), A-20 (population convention)

Shared symptom: All four components are ENSEMBLE-LEVEL quantities (fractions,
                counts, population conventions). All four are orphan or weak-anchor
                with respect to K_Space SOT.

  Why 1: What do these four components have in common?
    Answer: They all require a NOTION OF ENSEMBLE — a statistical structure layered
            on top of individual K_R structures.

  Why 2: Where does K-space define ensemble?
    Answer: NOWHERE in Layer 1. K1 defines individual k-tuples; K2 orders them
            within a single K_R; K7 closes a single K_R. K8 embeds K_R into K_joint.
            None defines an ENSEMBLE OF K_R structures or a sampling/frequency layer.

  Why 3: Do T-theorems supply this?
    Answer: T1 (K_joint), T3 (Relativization), T4 (colimit), T8 (K5_prospective
            bridge), T9 (K_ctx) all operate on categorical/morphism structures
            between K_R spaces. None defines ensemble statistics.

  Why 4: Is this a deliberate design choice or an omission?
    Answer: K_Space_Axiomatization.md §0.6 STATUS AUDIT explicitly states:
            "This document is PURELY STRUCTURAL — contains zero probability
             equations, zero numerical values, zero experimental data,
             zero data comparisons." Ensemble statistics is intentionally
             EXCLUDED from Layer 1.

  Why 5: Where is ensemble supposed to live?
    Root cause: K-Space Layer 1 is intentionally agnostic about ensembles —
                they belong to the EMPIRICAL FIT LAYER (Layer 4 in
                project_vvv_qmrf_class_c/index.md §3), which K9_A's v_rate
                straddles. K9_A is therefore a HYBRID Layer 3/4 object: the
                three-case partition is Layer 3 structural, but v_rate fitting
                is Layer 4 empirical.
    Fix strategy: ONE structural change addresses all four components — explicitly
                  document K9_A as a Layer 3+4 hybrid in the K9_A description, and
                  classify v_rate/N_bhranti/N_null as Layer 4 quantities that
                  REFERENCE Layer 3 axioms but are NOT derived from them.
                  Alternative: introduce an ensemble structure (would require
                  Layer 1 extension — out of scope, requires PEER-SYNC).
    Priority: HIGH — clarifies K9_A's class boundary and removes the
              "orphan" status for A-17/A-20 by reclassifying as Layer 4
              boundary variables rather than K-space orphans.
```

### Cluster C-2 — Interpretive vs Derivational BE-Lineage Coupling

```
Affected components: A-09 (arthakriyā), A-10 (bhrānti), A-11 (anupalabdhi), A-22 (EX
                     enrichment marker)

Shared symptom: K9_A's three cases each cite a BE concept (arthakriyā, bhrānti,
                anupalabdhi) plus an EX node (N_QM_VVV_00027/00032/00020). The
                BE concept appears as INTERPRETIVE LABEL in the K_Space axioms
                (K3 BE lineage, K4 BE lineage, K5 BE lineage), not as a
                derivation step.

  Why 1: What's common?
    Answer: All four are BE concepts referenced as "lineage" or "EX-enrichment"
            rather than as formal derivation inputs.

  Why 2: Is BE → K_Space link formal or interpretive?
    Answer: Per K_Space §0.4 design decision: "K-space is (math + registration-logic).
            The mathematical structure is the carrier, not the content." BE → K_Space
            is INTERPRETIVE: BE doctrines are the philosophical motivation/lineage,
            but K-axioms are stated in mathematical-logical form without BE-term
            primitives.

  Why 3: Does this weaken K9_A?
    Answer: NO for K9_A's MATHEMATICAL content (the three cases are determined by
            K4 + K5 alone). YES for K9_A's PRESENTATION (the EX-enrichment narrative
            could be replaced with K_Space-only anchors without loss).

  Why 4: Is this a SOT integrity risk?
    Answer: LOW. The BE lineage labels in K3/K4/K5 are documented in K_Space and
            BE SOT independently. The EX-enrichment is documented in PP-1 v2.
            All anchors exist; only the presentation level is non-primary.

  Why 5: Should this be fixed?
    Root cause: K9_A inherits K_Space's deliberate "math carrier + BE lineage"
                design. The interpretive coupling is consistent with the framework
                design, not a defect.
    Fix strategy: Confirm (acceptable convention). Optional: in the report, present
                  K9_A's three cases first with K_Space-only anchors, then add a
                  separate "BE Lineage" subsection citing arthakriyā/bhrānti/
                  anupalabdhi as interpretive labels.
    Priority: MEDIUM — improves presentation clarity but does not affect content.
```

### Cluster C-3 — K9S2 Citation Drift

```
Affected components: A-23 (isNull → K8 error), and probably A-02 (V→K4 L215-258),
                     A-03 (cert→K1 L96-100), A-15 (⊥_K→K5 L260-349).

Shared symptom: K9S2_candidate_A.md STEP 4 cites K_Space axioms with specific line
                ranges that do not match the current Class C K_Space copy:
                - K9S2 says cert(k) → K1 L96-100; the K1 admission rule is around
                  L86–93 in current K_Space; K3 (σ_R) is L216–253.
                - K9S2 says V(k) → K4 L215-258; current K4 is around L255–300.
                - K9S2 says ⊥_K → K5 L260-349; current K5 is around L300–390.
                - K9S2 says isNull → K8 L480-540; current K8 is much later, and
                  isNull is defined in K4 clause (b), not K8.

  Why 1: Why do the line numbers not match?
    Answer: K_Space_Axiomatization.md has been revised multiple times (v2.3 current).
            K9S2 was written 2026-05-23 against an earlier version. Downstream
            derivative documents were not refreshed.

  Why 2: Why was no peer-sync triggered?
    Answer: K9S2 is in the `k9_analysis/` derivative folder, not in the
            PEER-SYNC scope (which currently covers only the K_Space_Axiomatization
            canonical ↔ Class C pair). Derivative documents are not under
            peer-sync today.

  Why 3: Is this a SOT integrity issue?
    Answer: PARTIAL. The K9S2 *axiom references* (K1, K4, K5) are CORRECT
            at the axiom level. The *line ranges* and the K8 mis-citation
            are drift artifacts.

  Why 4: What is the risk?
    Answer: A reader following K9S2 line ranges to K_Space will not find what
            K9S2 claims, eroding trust. The isNull → K8 error is the most material:
            it points to the wrong axiom entirely.

  Why 5: Fix?
    Root cause: K9 derivative documents are not under peer-sync. K_Space line
                ranges drift over revisions; derivative citations become stale
                unless explicitly refreshed.
    Fix strategy: ONE PEER-SYNC suggestion: extend peer-sync to cover derivative
                  documents that cite K_Space line ranges, OR update K9S2 to use
                  AXIOM IDENTIFIERS (K1/K4/K5) only, dropping line ranges.
                  Immediate fix: open ticket to correct isNull → K4(b) in K9S2 STEP 4.
    Priority: MEDIUM — does not affect K9_A content but affects audit traceability.
```

---

## Layer 3 — Verdict-Level RCA

```
S3 verdict (2026-05-23): CONDITIONAL PASS, Class D, DIM-2 = 2/5 (distinguishability).
S3 root cause for low DIM-2: P(o|k) at probability level = Tr(E_o ρ) under Case 1;
                              δP = 0 vs Born rule.

Post-deep-review question 1: Does this root cause still apply?

  Why 1: Does the per-event δP = 0 result survive the deep review?
    Answer: YES. Layer 0 Why 5 confirms K9_A is the MINIMAL K9 that respects K4/K5
            without modifying probability per-event. By construction, Case 1 = Born
            rule exactly. Layer 1 reviews confirm no component pushes δP off 0
            in Case 1.

  Why 2: Do any v31 changes (T9, T8-H1, K5_prospective) affect this?
    Answer: NO directly. T9 and T8-H1 are derivations supporting K9_E (⊥_K
            Suppression); they affect components specific to K9_E (K_ctx, f_perp).
            K9_A does NOT use K_ctx or f_perp. K5_prospective is a conservative
            extension; K9_A uses standard K5 (post-hoc invalidation), not
            prospective firing. K9_A is structurally unaffected by v31 updates.

  Why 3: Has any deep-review finding strengthened or weakened DIM-2?
    Answer: WEAKENED by Cluster C-1 finding: v_rate orphan status means K9_A
            CANNOT predict its own primary parameter from K1–K8 alone — v_rate
            is a Layer 4 quantity, fitted from experiment. This makes K9_A
            even MORE Class D than K9-S3 estimated, not less. DIM-2 = 2/5 holds
            or could even be reduced to 1.5–2/5.

  → Update verdict: UNCHANGED (CONDITIONAL PASS, Class D, DIM-2 ≈ 2/5).
                    The deep review CONFIRMS rather than overturns S3.

Post-deep-review question 2: Does K9_A have hidden registration-layer testability?

  Why 1: Can Proietti raw data distinguish a Case 2 event from a Case 1 event?
    Answer: A-18 W2 — NO. Proietti's CHSH-style dataset records coincidence counts
            but does not flag which events are V=0 (Bhrānti) vs V=1. The dataset
            is K-blind: it sees outcomes only, not registration validity.

  Why 2: What does "no P assignment" mean operationally for Case 2/3 events?
    Answer: A-21 W2 — these events are EXCLUDED from probability-fit inputs.
            Operationally, K9_A predicts that v_rate · N events follow Born rule;
            the remaining (1 − v_rate) · N events are filtered out as Bhrānti/null.
            If v_rate is setting-dependent, the FILTERED ensemble produces apparent
            δS via selection bias — but the per-event P is still Born rule.

  Why 3: Does v_rate fitting require event-level discrimination?
    Answer: A-17 W5 + A-18 W2 — YES if v_rate is estimated as |{V=1}|/N.
            NO if v_rate is fitted as a global ensemble normalization parameter
            (e.g., comparing observed coincidence rates to QM-predicted rates).
            The latter is the only path currently feasible with Proietti data.

  → Hidden testability: NO at probability level; PARTIAL at statistical level
                        (selection-bias channel via Channel 3 in PP-1 v2 §Round 3).
                        Confirms Class D classification.

Final reconciliation (≤ 5 sentences):

  K9_A's K9-S3 verdict (CONDITIONAL PASS, Class D, DIM-2 ≈ 2/5) is CONFIRMED by
  the deep review and slightly WEAKENED in one respect: the v_rate parameter is
  orphan in K-space and must be sourced from Layer 4 (empirical fit) or from a
  ρ-side decoherence model, not from K1–K8. The deep review identified one
  primary structural cluster — Cluster C-1 (K-space ensemble-statistics gap) —
  which affects 4 of K9_A's most empirically loaded components (v_rate,
  N_bhranti, N_null, population convention), but this is a DESIGN BOUNDARY of
  K-space Layer 1 (intentional, per K_Space §0.6 STATUS AUDIT), not a defect
  unique to K9_A. K9_A's per-event probability identity with Born rule
  (δP = 0 always in Case 1) is structurally unaffected by v31 updates (T9,
  T8-H1, K5_prospective do not interact with K9_A). The recommendation going
  forward is to retain K9_A as the conservative baseline and Class D reference
  candidate, and to address Cluster C-1 by EXPLICITLY documenting K9_A as a
  Layer 3+4 hybrid (structural partition Layer 3, ensemble fitting Layer 4)
  rather than by attempting to derive v_rate from K1–K8.
```

---

## Aggregate RCA Findings

**Dominant root cause of K9_A's weaknesses:** K-space Layer 1 is intentionally agnostic about ensemble statistics. All four orphan/weak-anchor components in K9_A (`v_rate`, `N_bhranti`, `N_null`, and the population convention) trace to this single structural choice. This is not a K9_A defect — it is a framework boundary.

**Secondary finding:** Documentation drift in K9S2 (Cluster C-3) is a low-severity but auditable issue requiring a one-time peer-sync of derivative-document citations.

**Tertiary finding:** The BE-lineage coupling (arthakriyā/bhrānti/anupalabdhi) is INTERPRETIVE not derivational by design (per K_Space §0.4). This is consistent with the framework and not a defect.

**Verdict-level outcome:** K9-S3 verdict UNCHANGED. K9_A remains the conservative Class D baseline.

---

## Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-05-27 | v0.1 | P1 execution. Layer 0 Meta-RCA, Layer 1 RCA for 9 components (H ≥ 5 or orphan), Layer 2 with 3 clusters triggered (C-1 ensemble gap, C-2 BE interpretive coupling, C-3 citation drift), Layer 3 verdict confirmed unchanged. |

---

*K9_A RCA Chains v0.1 (2026-05-27). 4-layer RCA per plan §4. Advisory only — no K_Space edits.*
