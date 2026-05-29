Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Report — K9_A Traceability Matrix

**Target:** K9_A — V-Filter (Three-Case, EX-Enriched)
**Date:** 2026-05-27
**Phase:** P1 (deep review execution)
**Companion files:** [plan_k9_a_deep_review.md](./plan_k9_a_deep_review.md), [rca_k9_a_chains.md](./rca_k9_a_chains.md)
**Method:** AHP-driven provenance audit + 4-layer RCA per plan §3–§4
**Status:** P1 v0.1 — complete

---

## 1. Executive Summary

- **Components inventoried:** 23.
- **Orphans (Trace = 0/6):** 2 (A-17 `v_rate`, A-20 population convention).
- **Mean H-score:** 3.7 / 10 (Band: 🔵 BLUE / `[AH-LOW]`).
- **Components with H ≥ 7:** 3 (A-12 `bādhaka`, A-17 `v_rate`, A-20 population convention).
- **BE-anchored (SOT-1):** 10 rows.
- **QM-anchored (SOT-5):** 5 rows (Born rule, ρ, E_o, o, Case 1 rule).
- **Layer 2 clusters triggered:** 3 (C-1 ensemble gap, C-2 BE interpretive coupling, C-3 K9S2 citation drift).
- **Layer 3 verdict:** **UNCHANGED** — K9-S3 CONDITIONAL PASS / Class D / DIM-2 ≈ 2/5 confirmed.

> The K9_A audit confirms the K9-S3 verdict and identifies that K9_A's "weaknesses" are not defects but a deliberate framework boundary (K-Space Layer 1 is structural, not statistical). The ensemble parameters (`v_rate`, `N_bhranti`, `N_null`) are Layer 4 (empirical) boundary variables — they should be REFRAMED as such rather than treated as K-space orphans.

---

## 2. K9_A Definition (Reference)

From [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) lines 14–31 + [PP-1 v2](../../../04_governance/pre_plan/PP1_K9A_fixed.md):

```
K9_A — V-Filter (Three-Case, EX-Enriched):

Case 1: V(k)=1 ∧ ¬isNull
  P(o|k) = Tr(E_o ρ)          — Born Rule via arthakriyā (EX N_QM_VVV_00027)

Case 2: V(k)=0 ∧ ¬isNull  (Bhrānti / EX N_QM_VVV_00032)
  No P assignment. Event contributes to N_bhranti counter.
  K-side: registration exists but is erroneous (bādhaka-voided).

Case 3: isNull  (Anupalabdhi / EX N_QM_VVV_00020)
  No P assignment. Event contributes to N_null counter.
  K-side: registration itself is absent (no arthakriyā).

Free parameter: v_rate ∈ [0,1] = fraction of runs with V=1.
(Population parameter, not per-event.)
```

---

## 3. SOT Registry (re-used from parent index.md §3.2)

```
SOT-1 — BE Full System         (SYSTEM_Buddhist_Epistemology/system_be_full.md)
SOT-2 — K_Space (canonical)    (meta_architecture/K_Space_Axiomatization.md)
SOT-3 — K_Space (Class C)      (01_axiomatization/K_Space_Axiomatization.md)
SOT-4 — CLAUDE.md              (governance only — not scholarly)
SOT-5 — Standard QM            (Nielsen & Chuang / Peres / Born 1926 / von Neumann 1932)
SOT-6 — Proietti 2019          (arXiv:1902.05080)
EX    — VVV-QMRF-EX            (05_ex_compass/ — compass only, NOT a primary anchor)
```

`Trace_Score = #(SOTs ∈ {SOT-1, SOT-2/3, SOT-5, SOT-6} with verified anchor) / 6`
(SOT-4 excluded; SOT-2 ≡ SOT-3 counted once via PEER-SYNC.)

---

## 4. Component Inventory

| ID | Component | Type | Verbatim source span |
|----|-----------|------|----------------------|
| A-01 | `k = (M, o, cert, t, V)` K-state tuple | SYMBOL | K9S2 line 14 (PP-1 v2 lines 86–93) |
| A-02 | `V(k) ∈ {0,1}` validity flag | SYMBOL | K9S2 lines 18, 21 |
| A-03 | `cert(k) ∈ {0,1}` certification | SYMBOL | K9S2 line 87 (implied via K1) |
| A-04 | `isNull(k)` predicate | SYMBOL | K9S2 lines 18, 21, 25 |
| A-05 | `o` outcome | SYMBOL | K9S2 line 19 `P(o\|k) = Tr(E_o ρ)` |
| A-06 | `Tr(E_o ρ)` Born rule | OPERATION | K9S2 line 19 |
| A-07 | `E_o` POVM element | SYMBOL | K9S2 line 19 |
| A-08 | `ρ` density matrix | SYMBOL | K9S2 line 19 |
| A-09 | `arthakriyā` (pragmatic efficacy) | TERM | K9S2 line 19 "Born Rule via arthakriyā" |
| A-10 | `bhrānti` (erroneous cognition) | TERM | K9S2 line 21 "Bhrānti" |
| A-11 | `anupalabdhi` (non-cognition) | TERM | K9S2 line 25 "Anupalabdhi" |
| A-12 | `bādhaka` (contradicting cognition) | TERM | K9S2 line 23 "bādhaka-voided" |
| A-13 | Case-split partition (Case 1/2/3) | OPERATION | K9S2 lines 18–27 (PP-1 v2 design) |
| A-14 | Case 1 rule: V=1 ∧ ¬isNull → Born rule | OPERATION | K9S2 lines 18–19 |
| A-15 | Case 2 rule: V=0 → no P, count N_bhranti | OPERATION | K9S2 lines 21–23 |
| A-16 | Case 3 rule: isNull → no P, count N_null | OPERATION | K9S2 lines 25–27 |
| A-17 | `v_rate ∈ [0,1]` population free parameter | ASSUMPTION | K9S2 lines 29–30 |
| A-18 | `N_bhranti` counter | SYMBOL | K9S2 line 22 |
| A-19 | `N_null` counter | SYMBOL | K9S2 line 26 |
| A-20 | "Population parameter, not per-event" meta-assumption | ASSUMPTION | K9S2 line 30 |
| A-21 | "No P assignment" semantics (Cases 2 & 3) | OPERATION | K9S2 lines 22, 26 |
| A-22 | EX enrichment marker (`EX N_QM_VVV_*`) | ASSUMPTION | K9S2 lines 19, 21, 25 |
| A-23 | K9S2 anchor error (`isNull → K8`) | AUDIT-FINDING | K9S2 STEP 4 line 87 |

---

## 5. Full Traceability Matrix

> **Anchor cell conventions:**
> - SOT-1: `N_BE_NNNNN` node ID from `system_be_full.md`.
> - SOT-2/3: `K<n>` axiom + section anchor (line ranges in current Class C copy).
> - SOT-4: `def §<n>` if formally defined in CLAUDE.md.
> - SOT-5: `P<n>` standard QM postulate.
> - SOT-6: `arXiv:1902.05080 Fig<n>` if empirical.
> - `—` if no anchor in that SOT.
>
> Per AHP convention, EX anchors live in a separate column ("EX (compass)") and do NOT contribute to Trace.

| ID | Component | Type | SOT-1 (BE) | SOT-2/3 (K_Space) | SOT-4 (CLAUDE) | SOT-5 (Std QM) | SOT-6 (Proietti) | EX (compass) | Trace | H | Primary | Secondary | RCA Summary | Action |
|----|-----------|------|------------|--------------------|-----------------|------------------|--------------------|---------------|-------|---|---------|-----------|-------------|--------|
| A-01 | K-state tuple | SYM | — | K1 §1.1 (formal block) | — | — | — | — | 1/6 | 2 | [AH-OK] | — | 3-Why: tuple primitives are K1 axiomatized fields | Confirm |
| A-02 | `V(k)` | SYM | N_BE_00022 (arthakriyā via svataḥ prāmāṇya) | K4 clause (a)+(b) §K4 | — | — | — | — | 2/6 | 1 | [AH-OK] | — | 3-Why: K4 default + BE svataḥ lineage | Confirm |
| A-03 | `cert(k)` | SYM | N_BE_00011 (svasaṃvedana) | K3 §K3 (σ_R definition); K1 admission rule | — | — | — | — | 2/6 | 1 | [AH-OK] | — | 3-Why: K3 intrinsic + K1 admission | Confirm |
| A-04 | `isNull(k)` | SYM | N_BE_00253 (anupalabdhi, RCA-level) + N_BE_00161 (nonoccurrence) | **K4(b)** formal block (NOT K8 as K9S2 says) | — | — | — | N_QM_VVV_00020 | 2/6 | 3 | [AH-LOW] | — | 3-Why: K4(b) clause; BE anchor RCA-level not 30-core | Confirm |
| A-05 | `o` outcome | SYM | — | implicit in K1 tuple | — | P1 (state) + P3 (measurement) | — | — | 1/6 | 0 | [AH-OK] | — | 3-Why: QM textbook standard | Confirm |
| A-06 | `Tr(E_o ρ)` Born rule | OP | — | — | — | **P3** (POVM measurement, Born 1926) | — | N_QM_00016 | 1/6 | 0 | [AH-OK] | — | 3-Why: QM Born rule, 100-year provenance | Confirm |
| A-07 | `E_o` POVM | SYM | — | — | — | P3 (POVM elements) | — | — | 1/6 | 0 | [AH-OK] | — | 3-Why: QM standard POVM | Confirm |
| A-08 | `ρ` density matrix | SYM | — | — | — | P1 (state) | — | — | 1/6 | 0 | [AH-OK] | — | 3-Why: QM standard state | Confirm |
| A-09 | `arthakriyā` | TERM | **N_BE_00022** (core) + N_BE_00196/197/198 (RCA) | K4 BE lineage L294 | — | — | — | N_QM_VVV_00027 | 2/6 | 5 | [AH-WARN] | [AH-EX] | **L1 5-Why §A-09** — interpretive lineage, not derivational | Confirm |
| A-10 | `bhrānti` | TERM | **N_BE_00006** (core) | K5 mechanism + K4 boundary (L297) | — | — | — | N_QM_VVV_00032 | 2/6 | 2 | [AH-OK] | — | 3-Why: BE core anchored + K5 mechanism | Confirm |
| A-11 | `anupalabdhi` | TERM | **N_BE_00253** (RCA, not in 30-core) + N_BE_00256 (anupalabdhi-hetu) | K4(b) lineage (via isNull) | — | — | — | N_QM_VVV_00020 | 2/6 | 3 | [AH-LOW] | — | 3-Why: BE RCA-level + K4(b) | Confirm |
| A-12 | `bādhaka` | TERM | **No dedicated N_BE node** (subsumed under N_BE_00006 as agent role) | K5 BE lineage L385 | — | — | — | N_QM_VVV_00029 (retroactive override) | 1/6 | 7 | [AH-HIGH] | [AH-WEAK] | **L1 5-Why §A-12** — no standalone BE node | Fix (BE SOT extension) |
| A-13 | Case-split partition | OP | — | K4(a) + K5 + K4(b) (jointly cover the three cases) | — | — | — | — | 1/6 | 4 | [AH-LOW] | — | 3-Why: jointly derived from K4(a/b) + K5 via PP-1 v2 EX-distinction | Confirm |
| A-14 | Case 1 rule | OP | — | K4(a) + Born rule | — | P3 | — | N_QM_VVV_00027 | 2/6 | 1 | [AH-OK] | — | 3-Why: K4(a) ∧ P3 Born rule | Confirm |
| A-15 | Case 2 rule | OP | N_BE_00006 (bhrānti) | K5 mechanism + K4 boundary | — | — | — | N_QM_VVV_00032 | 2/6 | 4 | [AH-LOW] | — | 3-Why: K5 invalidation + N_bhranti definition | Confirm |
| A-16 | Case 3 rule | OP | N_BE_00253 (anupalabdhi) | K4(b) + K4 boundary | — | — | — | N_QM_VVV_00020 | 2/6 | 4 | [AH-LOW] | — | 3-Why: K4(b) ∧ isNull definition | Confirm |
| A-17 | `v_rate` | ASSU | — | — | — | — | — | N_QM_VVV_00032 → N_QM_00095 | **0/6** | **8** | [AH-HIGH] | [AH-ORPHAN], [AH-EX] | **L1 5-Why §A-17** — ensemble property, K-space silent | Re-derive (Layer 4 reclassification) OR Defer |
| A-18 | `N_bhranti` counter | SYM | N_BE_00006 (defining concept) | derived from A-02 + A-15 | — | — | — | N_QM_VVV_00032 | 1/6 | 6 | [AH-WARN] | [AH-DEFER] | **L1 5-Why §A-18** — K9_A-defined observable | Defer (K9-S* operationalization sprint) |
| A-19 | `N_null` counter | SYM | N_BE_00253 (defining concept) | derived from A-04 + A-16 | — | — | — | N_QM_VVV_00020 → N_QM_00033 | 1/6 | 6 | [AH-WARN] | [AH-DEFER] | **L1 5-Why §A-19** — better measurement traction than N_bhranti | Defer (K9-S* operationalization sprint) |
| A-20 | "Population parameter, not per-event" | ASSU | — | — | — | — | — | — | **0/6** | **7** | [AH-HIGH] | [AH-ORPHAN] | **L1 5-Why §A-20** — ensemble convention layered on K-space | Confirm (Layer 4 convention) |
| A-21 | "No P assignment" semantics | OP | (interpretive) BE arthakriyā / bhrānti / anupalabdhi distinction | K4(a) implies P only when V=1; not derived | — | — | — | — | 1/6 | 5 | [AH-WARN] | — | **L1 5-Why §A-21** — K9_A construction, K9-S1 C-NORM consistent | Confirm |
| A-22 | EX enrichment marker | ASSU | (cross-traced via PP-1 v2) | — | — | — | — | N_QM_VVV_00027/00032/00020 | 1/6 | 5 | [AH-WARN] | [AH-EX] | **L1 5-Why §A-22** — compass cited inline, primary anchors exist separately | Fix (rewrite definition with primary anchors lead) |
| A-23 | K9S2 anchor error: isNull → K8 | AUDIT-FINDING | — | corrected anchor: K4(b) (not K8) | — | — | — | — | — | 6 | [AH-WARN] | [AH-DERIVED] | **L1 5-Why §A-23 + L2 C-3** — citation drift | Fix (PEER-SYNC suggestion: update K9S2) |

---

## 6. Aggregate Metrics

| Metric | Formula | Value | Target | Status |
|--------|---------|-------|--------|--------|
| Total components | count rows | **23** | 18–25 | ✅ |
| Orphan count | rows with Trace = 0/6 | **2** (A-17, A-20) | 0 (any orphan triggers Layer 1 + Layer 2 RCA) | ⚠️ — both flagged + reframed as Layer 4 |
| Mean H-score | sum(H) / count_scored | **3.7** | ≤ 4.0 | ✅ |
| Components with H ≥ 7 | count | **3** (A-12, A-17, A-20) | ≤ 3 | ✅ (at cap) |
| BE-anchored (SOT-1) | rows with SOT-1 ≠ — | **10** (A-02, A-03, A-04, A-09, A-10, A-11, A-15, A-16, A-18, A-19) | ≥ 4 | ✅ |
| QM-anchored (SOT-5) | rows with SOT-5 ≠ — | **5** (A-05, A-06, A-07, A-08, A-14) | ≥ 4 | ✅ |
| Pure-derived (only PP-1 v2 anchor) | rows with no L1/L2/L3 trace | **0** | 0 | ✅ |
| Layer 1 5-Whys count | full RCA chains | **9** | match (#H≥5 + #orphans) = 9 | ✅ |
| Layer 2 clusters | count | **3** (C-1, C-2, C-3) | ≥ 1 if Layer 2 triggered | ✅ |
| Layer 3 verdict change | label | **UNCHANGED** | reported | ✅ |

### H-score histogram (band view)

| Band | Range | Count | Components |
|------|-------|-------|------------|
| 🟢 GREEN (0–2) | `[AH-OK]` | 9 | A-01, A-02, A-03, A-05, A-06, A-07, A-08, A-10, A-14 |
| 🔵 BLUE (3–4) | `[AH-LOW]` | 5 | A-04, A-11, A-13, A-15, A-16 |
| 🟡 YELLOW (5–6) | `[AH-WARN]` | 6 | A-09, A-18, A-19, A-21, A-22, A-23 |
| 🟠 ORANGE (7–8) | `[AH-HIGH]` | 3 | A-12, A-17, A-20 |
| 🔴 RED (9–10) | `[AH-CRIT]` | 0 | — (no BLOCKING components) |

---

## 7. Verdict Reconciliation (Layer 3 mirror)

K9_A's K9-S3 verdict (**CONDITIONAL PASS, Class D, DIM-2 ≈ 2/5**) is **CONFIRMED** by this deep review and slightly **WEAKENED** in one respect: the `v_rate` parameter is orphan in K-space and must be sourced from Layer 4 (empirical fit) or from a ρ-side decoherence model, not from K1–K8.

The audit identified one primary structural cluster — **Cluster C-1 (K-space ensemble-statistics gap)** — affecting 4 of K9_A's most empirically loaded components (`v_rate`, `N_bhranti`, `N_null`, population convention). This is a **DESIGN BOUNDARY** of K-Space Layer 1 (intentional, per K_Space_Axiomatization §0.6 STATUS AUDIT), **not** a defect unique to K9_A.

K9_A's per-event probability identity with Born rule (δP = 0 always in Case 1) is **structurally unaffected** by v31 updates (T9, T8-H1, K5_prospective do not interact with K9_A).

**Recommendation:** Retain K9_A as the conservative baseline / Class D reference candidate. Address Cluster C-1 by **explicitly documenting K9_A as a Layer 3+4 hybrid** (structural partition Layer 3, ensemble fitting Layer 4) rather than by attempting to derive `v_rate` from K1–K8.

Full chains: see [`rca_k9_a_chains.md`](./rca_k9_a_chains.md) § Layer 3.

---

## 8. Action Register

| ID | Action | Priority | Rationale |
|----|--------|----------|-----------|
| **AC-01** | **Fix**: file BE SOT extension request to add `bādhaka` as RCA-level N_BE node (currently subsumed under N_BE_00006 as agent role) | MEDIUM | A-12 5-Why root cause |
| **AC-02** | **Re-derive / Reclassify**: explicitly document `v_rate`, `N_bhranti`, `N_null`, population convention as Layer 4 (empirical) boundary variables in K9_A description | HIGH | Cluster C-1 resolution; resolves A-17, A-18, A-19, A-20 |
| **AC-03** | **Defer**: operationalize `N_bhranti` and `N_null` counters in a dedicated K9-S* sprint (suggested name: K9-S13 ensemble-observable operationalization) | MEDIUM | A-18, A-19 fix candidates |
| **AC-04** | **Fix**: rewrite K9_A definition body to lead with primary SOT-1/2-3 anchors; relegate EX nodes to a "compass footnote" subsection | MEDIUM | A-22 root cause; Cluster C-2 fix strategy |
| **AC-05** | **Fix**: open PEER-SYNC ticket — update [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) STEP 4 to use axiom identifiers (K1/K3/K4/K5) without specific line ranges; correct `isNull → K8` to `isNull → K4(b)` | MEDIUM | A-23 + Cluster C-3 |
| **AC-06** | **Confirm**: interpretive BE-lineage coupling (A-09 arthakriyā, A-10 bhrānti, A-11 anupalabdhi) is consistent with K_Space §0.4 design — no structural fix required, only optional presentation refinement | LOW | A-09 + Cluster C-2 |
| **AC-07** | **Confirm**: K9-S3 verdict (CONDITIONAL PASS / Class D / DIM-2 ≈ 2/5) — deep review supports without modification | INFO | Layer 3 outcome |

---

## 9. Cross-References

### AHP top-10 cross-check

Checked against [`00_top_10_hallucinations_record.md`](../../../../anti_hallucinations/00_top_10_hallucinations_record.md):

| Component | Listed in AHP top 10? | Notes |
|-----------|------------------------|-------|
| A-12 `bādhaka` | TBD (verify) | Single-term BE-extension issue; may not have made the top 10 |
| A-17 `v_rate` | TBD (verify) | Strong candidate for top 10 since ORPHAN H=8 |
| A-20 population convention | TBD (verify) | Companion to A-17 |
| A-23 K9S2 anchor error | NOT IN TOP 10 (audit finding new) | First detection in this deep review |

> **Note:** The top-10 file should be re-audited after this deep review to incorporate findings A-17, A-20, A-23 if they qualify.

### Related sprint documents

- [K9S3_ranking.md](../../k9_analysis/K9S3_ranking.md) — K9_A DIM scoring (2/5 distinguishability, 4/5 derivability, 4/5 parameter efficiency, 5/5 math robustness, 4/5 EWF relevance). Deep review confirms.
- [K9S6_new_candidates.md](../../k9_analysis/K9S6_new_candidates.md) — checked; no K9_A revision post-S3.
- [PP-1 v2](../../../04_governance/pre_plan/PP1_K9A_fixed.md) — three-case design source.

---

## 10. PEER-SYNC Suggestions

These are advisory only; this report does **not** edit K_Space_Axiomatization.md or any frozen Layer 1 axiom.

### PS-1 — Update K9S2 anchors (A-23 + Cluster C-3)

**Target:** [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) STEP 4 "Derivation Trace" table.

**Suggested change:**

| Term | Current K9S2 anchor (incorrect/stale) | Suggested anchor (verified) |
|------|---------------------------------------|------------------------------|
| `V(k)` | K4 (arthakriyā axiom, L215-258) | K4 §K4 clause (a) + (b) |
| `cert(k)` | K1 (admission rule, L96-100) | K1 admission rule + K3 (σ_R definition) |
| `⊥_K` | K5 (bādhaka axiom, L260-349) | K5 §K5 (registered contradiction ⊥) |
| `isNull` | **K8 (absence axiom, L480-540)** ← INCORRECT | **K4 clause (b)** + EX N_QM_VVV_00020 |

Rationale: K9S2 line ranges are stale relative to current K_Space v2.3 Class C copy. The `isNull → K8` citation is structurally incorrect — `isNull` is defined in K4(b), not K8 (which is Cross-Space Preservation).

### PS-2 — Document K9_A as Layer 3+4 hybrid (AC-02)

**Target:** K9_A description in [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) STEP 8 "VERDICT" or in [VVV_QMRF_K9_Analysis_Plan.md](../../VVV_QMRF_K9_Analysis_Plan.md) §K9-S2.

**Suggested addition (verbatim):**

> K9_A operates across Layer 3 (structural partition via K4(a)+K5+K4(b)) and Layer 4 (empirical fit via `v_rate`, `N_bhranti`, `N_null`). The ensemble parameters are boundary variables — input to K-space from Layer 4 empirical fitting, not output derivable from K1–K8. K-Space Layer 1 is intentionally agnostic about ensemble statistics (per K_Space_Axiomatization §0.6 STATUS AUDIT); the orphan status of v_rate is a framework boundary, not a K9_A-specific defect.

### PS-3 — (Optional) Add `bādhaka` to BE SOT (AC-01)

**Target:** [SYSTEM_Buddhist_Epistemology/system_be_full.md](../../../../../SYSTEM_Buddhist_Epistemology/system_be_full.md).

**Suggested addition:** Add new RCA-level node `N_BE_XXXXX` for `bādhaka` (contradicting cognition acting as agent), referencing Source doc L259–L263 and paper v2.0 §4.4, with edges:
- `ED_BE_XX`: `bādhaka → bhrānti (N_BE_00006)` (produces / acts on)
- `ED_BE_YY`: `bādhaka → K5 mechanism` (K5 invalidation agent)

Low priority — current BE SOT structure can be read as treating `bādhaka` implicitly via N_BE_00006 with agent/patient role distinction.

---

## 11. Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-05-27 | v0.1 | P1 execution complete. 23 components inventoried, 4 layers of RCA, K9-S3 verdict CONFIRMED unchanged. 3 Layer 2 clusters triggered (C-1 ensemble gap, C-2 BE interpretive coupling, C-3 K9S2 citation drift). 7 actions registered (AC-01 through AC-07). 3 PEER-SYNC suggestions filed (PS-1, PS-2, PS-3). |

---

*K9_A Traceability Matrix Report v0.1 (2026-05-27). 23 components, 0 BLOCKING, K9-S3 verdict CONFIRMED. Advisory only — no K_Space edits performed.*
