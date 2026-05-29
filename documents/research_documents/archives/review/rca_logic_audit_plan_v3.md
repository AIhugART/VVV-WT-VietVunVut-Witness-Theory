# RCA Logic Audit — K_Space_Axiomatization_plan_v3.md

**Auditor:** Antigravity (Claude Opus 4.6 Thinking)
**Date:** 2026-05-23
**Target:** [K_Space_Axiomatization_plan_v3.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/K_Space_Axiomatization_plan_v3.md)
**Cross-references:**
- [K_Space_Axiomatization.md (v2.1)](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/K_Space_Axiomatization.md) — source axioms K1–K8, T1–T7
- [K_Space_Axiomatization_plan.md (v25)](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/meta_architecture/K_Space_Axiomatization_plan.md) — Phase 1–6 complete, Phase 7+ integrated
- [rca_k_h_registration_observability_plan.md](file:///c:/Stable_Diffusion/Buddhist_Epistemology_Quantum_Measurement/documents/research_documents/vvv-qmrf/plan/rca_k_h_registration_observability_plan.md) — Gates 1/2/3 source definitions

**Method:** 7-dimension structural logic check + cross-file verification

---

## Audit Dimensions

| # | Dimension | Verdict |
|---|-----------|---------|
| 1 | RCA Motivation Coherence | ✅ PASS |
| 2 | K9 Candidate Axiom Logic vs K1–K8 | ⚠️ FINDING (2 issues) |
| 3 | Phase Dependency Chain Soundness | ✅ PASS |
| 4 | Gate Structure Rigor | ✅ PASS |
| 5 | Plan v1 ↔ Plan v3 Consistency | ⚠️ FINDING (1 issue) |
| 6 | Parameter Budget & Fitting Logic | ⚠️ FINDING (1 issue) |
| 7 | Honest-Assessment Escape Hatches | ✅ PASS |

**Overall:** 4 findings, none BLOCKING. Plan logic is **structurally sound** with minor gaps that should be addressed before S1 begins.

---

## 1. RCA Motivation Coherence ✅ PASS

### Check: Does §0 correctly diagnose the root cause?

**Symptom** (plan v3 §0.1 line 24): K1–K8 + T1–T7 generate no probability equation; no path from axioms to data fit.

**Root cause** (plan v3 §0.1 line 25): K1–K8 define K-space *structurally* (cert, V ∈ {0,1}, ⊥_K, AdmJoint) but lack a **bridge axiom** mapping registration-state → continuous probability value.

**Verification against source axioms:**
- K1 (line 82–120 of v2.1): cert ∈ {0,1}, V ∈ {0,1} — confirmed binary.
- K4 (line 216–258): V(k) = 1 (non-null) or 0 (null) — confirmed binary, no continuous value.
- K5 (line 260–349): V(k1) → 0 — transition rule, still binary.
- No axiom defines `P(o|K)` or any probability expression.

**Verdict:** Root cause correctly identified. The structural gap is **binary V → continuous P**, and K1–K8 genuinely have no mechanism to produce a probability value. The 5-Why trace (lines 29–33) is logically coherent: each "Why" step follows from the previous and traces to the root.

---

## 2. K9 Candidate Axiom Logic vs K1–K8 ⚠️ 2 FINDINGS

### 2.1 K9_A: V-Weighted Born Rule

```
K9_A: P(o | K) = V(k) · |⟨o|ψ⟩|² / Z(K)
```

**Logic check:**

| Check | Result | Note |
|-------|--------|------|
| V(k) ∈ {0,1} per K4 → P(o\|K) = 0 or \|⟨o\|ψ⟩\|² | ✅ | Correctly uses K4's binary V |
| Born limit: cert=1 ∧ V=1 ∀k → P = \|⟨o\|ψ⟩\|² | ✅ | Z(K) = 1 when all V=1 |
| Free parameter: α=1 default | ✅ | 1 param ≤ 2 budget |

> [!WARNING]
> **FINDING F-2.1: K9_A's distinguishability signal is self-undermining.**
>
> Plan v3 (line 115) correctly notes: "if V is always 1 (all registrations succeed), K9_A is identical to Born rule." But the plan then states "Distinguishability depends on empirical V-fluctuation." This creates a **logical circularity**:
>
> 1. K1 admission rule (line 96–100 of v2.1): `k ∈ K_R ⇒ cert(k) = 1` — all admitted events have cert=1.
> 2. K4 (line 226): `¬isNull(k) → V(k) = 1` — all non-null admitted events have V=1.
> 3. K5 can set V → 0, but only via registered contradiction ⊥ with authority — this requires a **cross-observer C_K context** (requires_K_joint = 1).
>
> **In single-observer experiments** (most standard QM setups), K5 never fires (no C_K, no ⊥). Therefore V=1 for all k, and K9_A = Born rule exactly. The Proietti D1 dataset (Phase 10a) involves a multi-observer EWF setup, so V-fluctuation *may* occur — but only if K5 fires. The plan does not analyze whether K5 firing conditions are met in the Proietti experimental design.
>
> **Severity:** MEDIUM. Pre-Phase-7 forecast (line 183) already marks K9_A as "MARGINAL" — so the plan is aware. But the mechanism by which V≠1 would arise in D1 is unspecified. Phase 7 F11f should explicitly model K5 firing in Proietti's 6-photon setup.

### 2.2 K9_B: Registration-Conditioned Probability

```
K9_B: P(o | K) = Tr(E_o ρ) · f(cert, V, ⊥_K, C_K)
```

**Logic check:**

| Check | Result | Note |
|-------|--------|------|
| f must be specified before Phase 7 | ✅ | Plan correctly marks CONDITIONAL READY |
| Born limit: f(1,1,no-fire,trivial) = 1 | ✅ | Correct |
| Options B1/B2/B3 sketched | ✅ | Reasonable |

> [!IMPORTANT]
> **FINDING F-2.2: K9_B Option B1 has a cert paradox.**
>
> Plan v3 (line 138): `f_cert: {0→α, 1→1}` where cert=0 maps to scaling factor α.
>
> But K1 admission rule guarantees `cert(k) = 1` for all k ∈ K_R (line 96–100 of v2.1). The cert=0 case **never occurs inside K_R**. Therefore f_cert is always 1, and the α parameter is **vacuously free** — it can take any value without affecting any prediction, because it multiplies a case that never exists.
>
> This means in Option B1:
> - f_cert(cert) = 1 always (cert=1 by K1 admission rule)
> - f_V(V) = {0→0, 1→1} (same as K9_A's V-gate)
> - f_context(⊥_K, C_K) = depends on K5 firing
>
> **Net effect:** K9_B Option B1 **collapses to K9_A** (V-gating + context sensitivity) unless f_context introduces new content. The α parameter is not a real degree of freedom.
>
> **Severity:** MEDIUM. Plan should clarify that Option B1's cert-based scaling is vacuous within K_R and that the effective free parameter is in f_context, not f_cert. This affects the parameter-budget accounting (RCA R6).

### 2.3 K9_C: Colimit Probability via T4

**Logic check:** Correctly deferred (T4 formalization incomplete). Plan marks "NOT READY" (line 175). No logic issue — proper gate discipline.

---

## 3. Phase Dependency Chain Soundness ✅ PASS

### Forward dependency map verification (plan v3 §8, lines 525–557):

```
Phase 7 → Phase 8 → Phase 9 → Phase 10 → Phase 11 → Phase 12
```

| Link | Source | Target | Blocking? | Verified |
|------|--------|--------|-----------|----------|
| P7-C3 → P9-C3 | Distinguishability | Verification | Yes (BLOCKING) | ✅ |
| P8-C5 → P9-C6 | Class C Stage 1 | Stage 2 | Yes | ✅ |
| P9-C5 → Phase 10 | Rank-1 selection | Data fit | Yes | ✅ |
| P10-C6 → Phase 11 | Joint verdict | 3-observer pred | Yes | ✅ |
| Phase 11 → Phase 12 | Prediction + reduction | Honest assessment | No (Phase 12 can run even if 11 partial) | ✅ |

**Dependency acyclicity check:** No cycles detected. All arrows point forward. Phase 7 gates (G1/G2/G3) are prerequisites for Phase 8 — cannot be bypassed.

**Sprint sequencing check (§5):** S1→S8 ordering aligns with dependency map. S5a/S5b/S5c can run in parallel (independent D1/D2/D3 fits) — plan correctly notes they are sequential by session but could be parallelized.

**Verdict:** Dependency chain is acyclic, complete, and correctly ordered.

---

## 4. Gate Structure Rigor ✅ PASS

### Gate verification against reference file:

| Plan v3 Gate | Reference file §13 | Correctly cited? | Hard-stop enforced? |
|---|---|---|---|
| P7-G1 (Phys operationalization) | §13 Gate 1 (lines 576–681) | ✅ Correct | ✅ BLOCKING |
| P7-G2 (Registration gap) | §13 Gate 2 (lines 683–731) | ✅ Correct | ✅ BLOCKING |
| P7-G3 (Lock-time definition) | §13 Gate 3 (lines 733–788) | ✅ Correct | ✅ BLOCKING |

**Gate semantics verification:**

- **G1:** Plan correctly requires Phys(o|H_physics) ≠ "detector click" (line 204). Reference file §13 Gate 1 provides Decoh + Ampl + Stable criteria. Plan cites this correctly.
- **G2:** Plan correctly requires Phys=1 ∧ Lock_K=0 scenario to exist (line 205). Reference file §13 Gate 2 provides 10 cases (C1–C10). Plan explicitly cross-references these cases.
- **G3:** Plan correctly requires operational t_lock (prefer t_lock^val) (line 206). Reference file §13 Gate 3 provides 4 lock-time candidates. Plan cross-references correctly.

**RCA R2 (4.9/5) enforcement:** "P7-G1 OR P7-G2 OR P7-G3 = FAIL → candidate REJECTED before Phase 8" (line 211). This is logically correct: gates are **conjunctive requirements** (all must pass), and the OR in the FAIL condition means any single failure rejects.

**Compound gate P9-C6 verification (RCA R3 4.7/5):** Class C requires P8-C5 (Stage 1) AND P9-C6 (Stage 2: adversarial + gates). Both stages must pass. Default Class D. This is logically sound — prevents premature promotion.

**Verdict:** Gate structure is rigorous, correctly sourced, and properly enforces hard stops.

---

## 5. Plan v1 ↔ Plan v3 Consistency ⚠️ 1 FINDING

### Check: Do Phase 7–12 in plan v3 align with the integrated Phase 7–10 in plan v1?

Plan v1 (K_Space_Axiomatization_plan.md) has been **updated to include Phase 7–10 content** (lines 156–419), which mirrors plan v3's Phase 7–10. This is expected because plan v3 line 6 states: "Target (output A): extend plan.md (Phase 7–12 added)."

> [!NOTE]
> **FINDING F-5.1: Plan v1 already contains Phase 7–10c + Joint, but plan v3 also specifies these same phases. Overlap creates dual-source-of-truth risk.**
>
> Plan v1 (lines 156–419) contains detailed Phase 7 issue registry (P7-G1/G2/G3, P7-C1/C2/C3), Phase 8 (P8-C1..C5), Phase 9 (P9-C1..C6), Phase 10a/b/c/Joint — with **fix allocations** (F11a–F17b) that are fully specified.
>
> Plan v3 (lines 198–321) describes the same phases but with **slightly different detail level** — plan v3 has RCA gate questions as prose within tables, while plan v1 has them as issue-registry rows with fix allocations.
>
> **Specific discrepancies:**
> 1. Plan v1 Phase 7 has RCA forecast scores (P7-G1: 4.5/5, P7-C3: 3.8/5). Plan v3 does not include forecast scores in the phase tables (only in §9 verdict templates).
> 2. Plan v1 Phase 10 has explicit fix IDs (F14a–F17b). Plan v3 §7 issue registry uses ID ranges (P10a-C1..C5) without fix IDs — it says "Fix ID allocation: F11a, F11b, …" (line 519) but defers specifics.
> 3. Plan v1 now includes Phase 11/12 content (via the Phase 9→10 gate on lines 412–419) but **does not yet contain Phase 11 and Phase 12 issue registries**. Plan v3 does have Phase 11/12 (lines 287–321).
>
> **Risk:** If sprint S1 updates plan v1 with Phase 7+8 registry (per sprint deliverable, line 448), it may create merge conflicts with the already-integrated Phase 7+8 in plan v1.
>
> **Severity:** LOW. Plan v3 R15 (line 487) already identifies this risk and specifies mitigation: "Read v25 head first in S1; reconcile before extending." The dual-source is acknowledged.

---

## 6. Parameter Budget & Fitting Logic ⚠️ 1 FINDING

### RCA R6 (4.9/5) verification:

| K9 | Claimed free params | Actual effective params | Budget ≤ 2? |
|----|----|----|---|
| K9_A | 1 (α scaling) | **0–1** (α only active if V<1 occurs) | ✅ |
| K9_B (B1) | 1–2 (α + context) | **0–1** (α vacuous per F-2.2; context sensitivity is the real param) | ✅ |
| K9_C | 2–3 (weighting w_i) | 2–3 | ⚠️ If 3: DOF = 4-3 = 1 (minimal) |

### Proietti D1 fitting logic:

| Property | Value | Correct? |
|---|---|---|
| Data points | 4 (⟨A_0B_0⟩, ⟨A_0B_1⟩, ⟨A_1B_0⟩, ⟨A_1B_1⟩) | ✅ |
| DOF = 4 − #params | ≥ 1 required | ✅ |
| χ² test valid with DOF ≥ 1 | ✅ | Correct for goodness-of-fit |

> [!IMPORTANT]
> **FINDING F-6.1: χ² goodness-of-fit with DOF = 1–2 has very low statistical power.**
>
> With 4 data points and 2 free parameters (best case K9_B or K9_C), DOF = 2. A χ² test with DOF=2 has very limited ability to distinguish between competing models. The Δχ² between K9 and Standard QM could easily be within noise.
>
> The plan correctly notes (P10a-C4, line 255): "Fit Standard QM Born rule lên cùng dataset cùng procedure; report Δχ²." This is proper methodology. However, **the plan does not define a significance threshold** for Δχ². When is Δχ² "significant"? Without a pre-registered threshold, the Phase 10 verdict becomes subjective.
>
> **Mitigation already in plan:** Phase 12 P12-C3 (line 316): "Could simpler framework produce same fit?" This honest-assessment check partially covers the issue, but a pre-registered Δχ² significance criterion (e.g., p < 0.05 for likelihood ratio test) would strengthen the protocol.
>
> **Severity:** MEDIUM. Does not block execution but weakens the interpretability of fit results.

---

## 7. Honest-Assessment Escape Hatches ✅ PASS

### Check: Can the plan produce a "null result" (K-space adds nothing) without structural failure?

| Escape hatch | Location | Correctly specified? |
|---|---|---|
| "K1–K8 + K9_A/B/C cannot generate empirical distinguishability" | P7-C3 (line 209) | ✅ Explicit: "state khoa học finding" → stop plan |
| "K-space adds no physical content beyond Standard QM" | P8-C4 (line 226) | ✅ Explicit: discard candidate |
| Zero candidates pass adversarial | P9 gate (line 244) | ✅ "Document failure mode, identify structural gap, dừng v3" |
| Fit identical to Standard QM | R3 (line 475) | ✅ "Honest report; equally well, indistinguishable" |
| "K-space currently a notational variant" | P12-C4 (line 317) | ✅ Explicit: "acceptable nếu đó là sự thật RCA trỏ tới" |
| Phase 12 cannot soften | P12 gate (line 320) | ✅ "KHÔNG được soften" |

**Verdict:** The plan has robust escape hatches at every critical junction. Null results are not only permitted but explicitly documented as valid scientific findings. No escape hatch requires fabrication or forced consensus.

---

## Summary of Findings

| ID | Dimension | Severity | Description | Recommendation |
|----|-----------|----------|-------------|----------------|
| **F-2.1** | K9_A logic | MEDIUM | V-fluctuation mechanism unspecified for Proietti D1; K5 firing conditions in 6-photon EWF setup not analyzed | Phase 7 F11f should explicitly model K5 firing in Proietti's experimental design. If K5 cannot fire in D1 → K9_A produces zero distinguishability for D1 (marginal becomes FAIL). |
| **F-2.2** | K9_B Option B1 cert paradox | MEDIUM | f_cert(cert=0)=α is vacuous: cert=0 never occurs inside K_R by K1 admission rule. α is not a real free parameter. | Clarify that B1's effective free parameter is f_context, not α. Update parameter-budget to reflect effective (not nominal) parameter count. Consider removing α from B1 or redefining cert's role at the K_R *boundary* (pre-admission) for the bridge axiom. |
| **F-5.1** | Plan v1/v3 overlap | LOW | Both plans now contain Phase 7–10 content with slightly different detail levels; dual-source-of-truth risk | Already mitigated by R15. S1 should canonicalize: plan v1 becomes the **operational** source (with fix IDs), plan v3 becomes the **architectural** source (with RCA motivation + K9 pre-analysis). |
| **F-6.1** | χ² statistical power | MEDIUM | 4 data points / 2 params → DOF=2 → very low power to distinguish models; no pre-registered Δχ² significance threshold | Add pre-registered significance criterion (e.g., Δχ² > 3.84 for p<0.05 with ΔDOF=1, or equivalent likelihood ratio test). Document in Phase 10a. |

---

## Overall Verdict

> [!TIP]
> **Plan v3 logic is structurally sound.** The RCA motivation is correct, the dependency chain is acyclic, gates are properly sourced and enforced, and honest-assessment escape hatches exist at every critical point. The 4 findings are all MEDIUM or LOW severity — none blocks S1.
>
> The most impactful finding is **F-2.2** (cert paradox in K9_B Option B1), which reveals that the nominal parameter count overstates the effective degrees of freedom. This should be clarified before Phase 7 evaluates K9_B, to avoid wasting effort on a vacuous parameter.

**Recommended action:** Address F-2.1, F-2.2, and F-6.1 as pre-S1 clarification amendments to plan v3 (no structural redesign needed). F-5.1 can be handled during S1 reconciliation.
