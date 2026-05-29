Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chains — K9_D Deep Review (P4)

**Target:** K9_D — Certification Discount (FAIL-FATAL)
**Phase:** P4 execution
**Date:** 2026-05-27
**Method:** 4-Layer RCA (Layer 0 Meta + Layer 1 Per-Component + Layer 2 Cluster + Layer 3 Verdict)
**Parent:** [plan_k9_d_deep_review.md](./plan_k9_d_deep_review.md)
**Companion:** [report_k9_d_traceability_matrix.md](./report_k9_d_traceability_matrix.md)

---

## Layer 0 — Meta-RCA: Why Does K9_D Exist?

**Question:** What structural gap in K1–K8 did K9_D attempt to fill, and why was cert discount chosen?

```
Symptom: K9_D proposes P(o|k) = [cert(k)·1 + (1-cert(k))·α]·Tr(E_o ρ)/Z_D as a
         weighted-average rule where certified registrations contribute fully (weight 1)
         and non-certified registrations contribute at discount α ∈ [0,1].

  Why 1: What structural gap does K9_D claim to address?
    → K1–K8 define registration-logic axioms but contain NO probability rule.
      K9_D proposes that registration quality — specifically whether a registration
      event has cert = 1 (fully certified) or cert = 0 (discounted) — should modulate
      the probability of the registered outcome. A cert-discount would allow K9_D
      to assign lower probability weight to uncertain or marginal registration events.

  Why 2: Why is cert-discount chosen as the modulation mechanism?
    → Cert discount is conceptually the simplest bet-hedging strategy: if a
      registration event is not fully self-certified, its outcome should count
      less. The weighted-average form [cert·1 + (1-cert)·α] interpolates smoothly
      between full weight (cert=1, weight=1) and discounted weight (cert=0, weight=α),
      recovering Born rule when cert=1 everywhere. The design has intuitive appeal:
      a marginal or ambiguous registration should contribute less to the probability
      assignment than a fully certified one.

  Why 3: What makes cert(k) a structural constant inside K_R?
    → K1 admission rule (L135-148): "k ∈ K_R ⇒ cert(k) = 1." K_R is defined as
      the set of registration events that have occurred — every element of K_R is a
      registration that passed the admission boundary. By K3 (§σ_R L217-253),
      occurrence implies σ_R(M)=1, which is the self-certification criterion. Events
      with cert=0 are NOT admitted into K_R; they fall outside K_R's scope entirely.
      The admission filter is at the K_R BOUNDARY, not inside K_R.

  Why 4: What K1 design decision caused cert to be a structural constant?
    → K1–K8 were designed to axiomatize a closed, self-consistent registration space.
      K_R is not a "candidate pool" of possible registrations — it is the actual set
      of OCCURRED registration events. An occurred event is definitionally
      self-certified (it has occurred; something registered it). The K1/K3 design
      treats cert as a BOUNDARY FILTER (cert=0 events never enter K_R) rather than
      an INTERIOR VARIABLE (cert varying within K_R). This was a deliberate design
      choice to prevent K_R from containing "ghost" or "marginal" registrations with
      fractional certifications.

  Why 5: Is there any way to introduce a cert ≠ 1 event into K_R to rescue K9_D?
    → NO (STRUCTURAL NECESSITY). To have cert(k) ≠ 1 inside K_R would require:
        (a) Modifying K1's admission rule — a FROZEN Layer 1 change (blocked).
        (b) Defining a new "marginal K_R" space that accepts cert=0 events — this
            would require unfreezing K1 and K3 and redesigning the admission
            architecture. This is not a "minor fix."
        (c) Reinterpreting cert as a continuous [0,1] variable — contradicted by
            K1's explicit declaration "cert ∈ {0,1}" and the binary K3 σ_R criterion.
      All three paths are blocked: K1/K3 FROZEN. α's multiplier (1-cert)=0 always.

      Root cause: K9_D's cert-discount idea presupposes a K_R that contains
                  non-fully-certified events. K1's admission rule eliminates this
                  possibility structurally. K9_D's entire mechanism depends on
                  cert varying within K_R — a precondition that K1 makes impossible.
                  This is a more elementary failure than K9_B (which required a
                  full PP-2-SI impossibility theorem to prove cancellation); K9_D
                  fails at the AXIOM LOOKUP LEVEL.
```

**Layer 0 conclusion:** K9_D's FAIL-FATAL verdict is rooted in K1's cert structural constant — the simplest possible structural barrier among all FAIL-FATAL candidates. Unlike K9_B (per-tuple cancellation via PP-2-SI) or K9_C (τ_reg absence from K_R), K9_D fails because its motivating concept ("non-self-certified registrations inside K_R") is axiomatically impossible in K1. Layer 0 sets the standard: "can any cert≠1 event appear inside K_R?" Answer: NO, by K1 admission rule. Layers 1–3 confirm this finding at successively more specific levels.

---

## Layer 1 — Per-Component RCA

*Full 5-Whys chains for components with H ≥ 5 OR Trace = 0/6. All others have 3-Whys inline in the traceability matrix.*

### D-04 — α ∈ [0,1] Discount Factor — H=3, Trace=0/6

**Why this component exists:** K9_D introduces α as the probability weight assigned to non-self-certified registration events. Without α, the formula degenerates to P = cert·Tr(E_o ρ)/cert = Tr(E_o ρ) trivially; α gives K9_D its only free parameter and its intended physical meaning (degree of certification required for full probability weight).

```
5-Whys for D-04 (α — free parameter, orphan) — H=3, Trace=0/6

  Symptom: α ∈ [0,1] has no anchor in SOT-1 (BE), SOT-2/3 (K_Space K1-K8),
           SOT-5 (Standard QM), or SOT-6 (Proietti). Trace = 0/6.

    Why 1: What concept does α attempt to operationalize?
      → α is the "discount weight" for non-self-certified registrations:
        if cert(k)=0, the event still contributes to P(o|k) but at reduced
        weight α instead of full weight 1. α=0 means non-certified events
        contribute nothing; α=1 recovers the naive average (no discounting).
        α is therefore operationalizing the intuition: "less-certified
        registrations should have less probability influence."

    Why 2: Why does α have no K1-K8 anchor?
      → K1-K8 contain no concept of "partially certified" or "discounted"
        registration events. K1's cert ∈ {0,1} is a BINARY BOUNDARY FILTER
        (0 = rejected, 1 = admitted). There is no K-state field that
        encodes a fractional "certification quality" or "trust weight"
        within K_R. The K1 design intent is that once an event is in K_R,
        it has passed certification completely (cert=1 by admission rule).
        α would require either a new [0,1]-valued cert field or a separate
        "quality weight" field — neither exists in K1-K8.

    Why 3: Why does α's absence from K1-K8 not constitute a fixable gap?
      → For α to have meaning, K_R would need to contain cert=0 events
        (the events that α is meant to discount). But K1's admission rule
        permanently excludes cert=0 events from K_R. The absence of α in
        K1-K8 is therefore not a gap to fill but a consequence of a
        principled design choice: K_R contains only certified (occurred)
        events. Adding α to K1-K8 would require unfreezing K1 to allow
        non-certified events into K_R — an architectural change, not a
        parameter addition.

    Why 4: Could α be grounded via BE or EX?
      → BE: No N_BE_XXXXX node in system_be_full.md corresponds to a
        fractional "certification quality" or "trust discount" in Dignāga-
        Dharmakīrti pramāṇa theory. The closest BE concepts would be
        bhrānti (N_BE_00006, erroneous cognition) or anyāpoha (exclusion
        cognition), but neither operationalizes a [0,1] weight for
        partially-certified events. bhrānti marks a cognition as invalid
        (V=0), not as partially-weighted; anyāpoha is inferential exclusion,
        not a probability discount.
        EX: α is not in VVV-QMRF-EX (which tracks K-side concepts, not
        K9_D-specific free parameters). EX cannot serve as SOT anchor
        (CLAUDE.md §SOT registry: "EX = compass-only, does NOT count toward
        Trace_Score").

    Why 5: Why is H=3 (BLUE) rather than H=7-10 (ORANGE/RED)?
      → D-04 is assigned H=3 (not 7-10) for three reasons:
        (a) α ∈ [0,1] is standard mathematical notation — not hallucinated.
        (b) The cert-discount concept is conceptually motivated by real
            asymmetry in certification quality (the intuition exists, even if
            K1 precludes it in K_R). The concept is interpretable, not
            fabricated.
        (c) α's architectural irrelevance is unambiguous: (1-cert)=0 → α×0=0.
            The "risk" of α causing misclassification is zero because it
            provably cancels. A truly dangerous orphan (H=7-10) would be one
            that appears in a live formula and could be misinterpreted as an
            active parameter. D-04 is in a dead formula (K9_D pre-eliminated)
            and its zero-effect is proven.

        Root cause: α has no K1-K8 anchor because its motivating concept
                    (non-certified events in K_R) is axiomatically excluded
                    by K1's admission rule. α is an orphaned parameter in a
                    dead formula — architecturally irrelevant, not hallucinated.

        Fix candidate: CONFIRM (dead parameter). D-04 is documented for
                       completeness and to prevent future attempts to revive
                       K9_D by arguing α could be re-grounded if cert were
                       made variable. Layer 1 (K1) is FROZEN; this path is
                       permanently blocked.
        Affected siblings: None — D-04 is isolated. Closing α's orphan status
                           documents the non-anchor for completeness; all other
                           D-XX components trace through K1-K8 + SOT-5 normally.
```

---

## Layer 2 — Cluster RCA

**Trigger check:**
- Orphans ≥ 2? **NO** — only D-04 (Trace=0/6). Condition NOT met.
- ≥ 3 components share upstream "Why"? **YES** — D-03 (cert=1), D-05 ((1-cert)=0), D-06 (Z_D=1), D-07 (Born recovery) all trace to "K1 cert structural constant" as their shared upstream cause. Condition MET.
- ≥ 2 components with PP-2-only anchor? **NO** — only D-09 primarily cites PP-2-SI (D-08 also cites K1 alongside PP-2-SI). Condition NOT met.

**Layer 2 triggered: condition 2 met. One cluster identified.**

### Cluster C-D1: Structural Constants Cascade (D-03, D-05, D-06, D-07)

```
Cluster C-D1: "cert=1 propagates as structural constant through K9_D algebra"
  Affected components: D-03 (cert=1), D-05 ((1-cert)=0), D-06 (Z_D=1), D-07 (Born recovery)
  Shared symptom: Each component follows NECESSARILY from K1 admission rule — no
                  assumption or approximation is involved. The cascade is one-step
                  algebra at each stage.

    Why 1: Why do D-03, D-05, D-06, D-07 form a cascade?
      → They represent successive algebraic applications of one K1 fact:
          D-03: cert(k) = 1 ∀k ∈ K_R (K1 axiom, direct read L135-148)
          D-05: (1-cert(k)) = (1-1) = 0 (elementary subtraction)
          D-06: Z_D = [cert+(1-cert)·α]·Σ_o Tr(E_o ρ) = 1·1 = 1 (two substitutions)
          D-07: P(o|k) = 1·Tr(E_o ρ)/1 = Tr(E_o ρ) (one substitution)
        Each step is a single algebraic operation. The entire cascade requires
        no theorem, no approximation, no new postulate.

    Why 2: Why is cert=1 (D-03) the root of the cascade rather than a derived result?
      → cert=1 is a DIRECT READ from K1 §cert admission rule (L135-148 + PG-01
        L142-147). It is not derived from any K9 postulate or T1-T4 theorem.
        D-03 is a pure axiom lookup: "read K1, find cert=1 ∀k ∈ K_R." The cascade
        that follows is thus anchored to the most foundational level (FROZEN Layer 1),
        making the FAIL-FATAL verdict immune to any Layer 2 (bridge theorem) update.

    Why 3: What does this cascade reveal about K9_D's structural position?
      → K9_D failed at the FIRST axiom check (K1), not at a theorem boundary or
        data-fit level. Compare:
          K9_B: failed at PP-2-SI theorem (Layer 2 / T1–T4 level — needed formal proof)
          K9_C: failed at τ_reg absence (Layer 2 derivation level — τ_reg not in K2)
          K9_D: failed at K1 axiom lookup (Layer 1 level — cert=1 by definition)
        K9_D is the "earliest failure" in the K-space hierarchy. Its elimination
        required no theorem, no derivation, only one axiom.

    Why 4: Does the cascade provide any information for K9_E (survivor)?
      → YES — by contrapositive. K9_E's f_perp(K_ctx) is designed specifically to
        avoid the cert-constant problem: f_perp is not a function of cert(k) but of
        K_ctx (incommensurability context). K_ctx is NOT a structural constant —
        it depends on the K-space pair and the measurement scenario. K9_E learns
        from K9_D's failure: do not build probability modulation on structural
        constants; build it on contextual variables that CAN vary across scenarios.

    Why 5: Could the cascade be broken by a v31+ update?
      Root cause: NO. The cascade D-03→D-05→D-06→D-07 depends entirely on K1's
                  cert structural constant. K1 is FROZEN (CLAUDE.md §Identity and
                  scope rules: "Layer 1 (FROZEN) — K1-K8 Registration-logic axioms").
                  No v31+ update can modify K1 without unfreezing Layer 1. The
                  cascade is permanently locked.

                  Fix strategy: The cluster cannot be "fixed." It documents the
                  structural boundary between K9_D's cert-discount intuition and
                  K1's actual cert architecture. Resolution requires abandoning
                  cert-as-modulation-variable (K9_D) in favor of cert-as-boundary-
                  filter (K1 as-designed). This is already the case — K9_D is DEAD,
                  K1 is intact.
      Priority: LOW (informational; confirms structural boundary, no action needed)
```

**Cross-reference with K9_B Layer 2 Cluster C-1:** K9_B's Cluster C-1 (per-tuple anchoring of B-04, B-05, B-06) identified a structural boundary: "K1-K8 fields are registration-logic properties, not statistical outcome weights." K9_D's Cluster C-D1 is a more elementary version of the same insight: K1's cert field is a BOUNDARY FILTER, not an interior variable. K9_D fails at step zero (cert can't vary), while K9_B fails at step one (even with valid variation, per-tuple functions cancel). Together, Cluster C-1 and Cluster C-D1 define the **"K-logic constants barrier"** — any K9 postulate built on structural constants or per-tuple logic fields inherits cancellation.

---

## Layer 3 — Verdict-Level RCA

**Question:** After Layers 0–2, is the FAIL-FATAL verdict still locked? Does any v31 update affect K9_D?

```
Verdict RCA:
  PP-2 verdict (2026-05-23): FAIL-FATAL — cert(k)=1 ∀k ∈ K_R → α cancels → P=Tr(E_o ρ).
  Root cause (PP-2): K1 admission rule makes cert a structural constant inside K_R.

  Post-deep-review question 1: Does any v31 update interact with K9_D?
    Why 1: What are the v29-v31 updates?
      → v29: K5_prospective added (prospective evaluation extension for K9_E P9).
        v30: Noise sensitivity analysis (K9_E downgraded to Class C qualified).
        v31: K9E-PAT CLOSED as UNRESOLVABLE (RCA 4.92/5). T8 (K5_prospective
             Frequency Bridge) and T9 (K_ctx Construction) added to Layer 2.
    Why 2: Do any of these affect K9_D?
      → NO. K5_prospective is explicitly a "P9 bridge" — extends K5's evaluation
        MODE for K9_E probability assignment only. It does not modify K1's cert
        admission rule. T8 bridges K5_prospective ↔ K9_E f_perp (not cert-discount).
        T9 formalizes φ_ij morphism channel (not cert-modification). None of these
        creates a cert-like field that could vary inside K_R.
    Why 3: Could K5_prospective provide a prospective evaluation of cert?
      → NO. K5_prospective's conditions (i)–(iii) concern whether a HYPOTHETICAL
        outcome o would trigger K5 incommensurability (k5_o* ⊥_K k5_o'*). This
        operates on the prospective K5 firing, not on cert evaluation. cert remains
        a structural constant even in prospective mode: a prospective registration
        event would also be cert=1 if it occurred (K3 σ_R criterion is binary).
    → Update verdict: UNCHANGED. v29/v30/v31 updates are K9_E-specific.

  Post-deep-review question 2: Does K9_D have any open escape route (analogous to K9_B's C5 gap)?
    Why 1: Is there any K1-K8 mechanism that could introduce cert ≠ 1 inside K_R?
      → NO. K1's admission rule is unconditional: "k ∈ K_R ⇒ cert(k) = 1."
        PG-01 (L142-147) explicitly clarifies: cert is a structural constant inside
        K_R. The only way to have cert ≠ 1 inside K_R would be to modify K1 —
        FROZEN, architecturally blocked.
    Why 2: Could α be re-interpreted as an outcome-dependent weight (analogous to SNR)?
      → NO. α is introduced as a constant discount for non-certified registrations.
        Even if α were reinterpreted as α(o) — an outcome-specific discount — it
        would still be multiplied by (1-cert(k))=0 for all k ∈ K_R. The problem
        is not α's form but its multiplier being identically zero. No reinterpretation
        of α can fix this.
    Why 3: Could a new Level 4 predicate create cert-variable events?
      → NO. Level 4 (D_joint, requires_K_joint, AdmJoint) concerns joint registration
        contexts, not cert variation. K1-K4 and K8 carry NO Level 4 semantic
        dependency (K_Space_Axiomatization.md §Layer 1 note, L100-106). cert(k)
        remains a structural constant regardless of Level 4 specifications.
    → K9_D has NO open escape route. Unlike K9_B's C5 gap (which was a genuine
      candidate requiring explicit closing), K9_D's cert constraint admits no
      gap — it is a one-line axiom, not a derivation that could have a loophole.

  Final reconciliation:
    K9_D's FAIL-FATAL verdict is confirmed by P4 deep review with no modifications.
    The structural impossibility is anchored to K1's cert admission rule — the
    simplest possible structural barrier in the K9 program. No v29-v31 update,
    no Level 4 extension, no EX node, and no reinterpretation of α can rescue K9_D
    while K1 remains FROZEN. The 9-component inventory confirms mean H-score ≈ 1.3
    (overwhelming GREEN), consistent with a trivially impossible candidate rather
    than an ambiguous borderline case. The only orphan (D-04, α, H=3) is a confirmed
    dead parameter. Verdict: FAIL-FATAL LOCKED.
```

---

## Aggregate RCA Findings

**Dominant root cause of K9_D's failure (one sentence):**
K1's cert admission rule (cert(k) = 1 ∀k ∈ K_R, L135-148, PG-01 L142-147) makes (1-cert(k)) identically zero for all k ∈ K_R, rendering α's entire discount mechanism algebraically inert and collapsing Z_D to 1.

**Secondary finding from Layer 2 Cluster C-D1:**
The cert=1 structural constant cascades trivially through K9_D's algebra in four steps (D-03→D-05→D-06→D-07), yielding P(o|k) = Tr(E_o ρ) without any theorem, approximation, or postulate. K9_D is the "earliest failure" among all FAIL-FATAL candidates — failing at Layer 1 axiom lookup, not at theorem derivation (K9_B) or field absence analysis (K9_C).

**Impact on P5–P6 deep reviews (K9_E and K9_F):**
Cluster C-D1 reinforces the lesson from K9_B's Cluster C-1: K9 postulates built on structural constants or per-tuple K-logic fields will cancel. K9_E survives precisely because f_perp(K_ctx) is built on K_ctx (a contextual variable, not a structural constant) — K_ctx can vary across measurement scenarios while cert(k) cannot. P5 (K9_E) should verify that K_ctx is genuinely non-constant across the measurement scenarios of interest (K9-S12 protocol): this is the core distinguishing condition between K9_D/K9_B (structural-constant inputs, always cancel) and K9_E (contextual input, can differ across scenarios).

---

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-05-27 | v0.1 | P4 execution. Layer 0–3 complete. 9 components (D-01…D-09). Layer 2 triggered (condition 2, Cluster C-D1). FAIL-FATAL confirmed. Simplest failure in K9 program (Layer 1 axiom lookup only). |
