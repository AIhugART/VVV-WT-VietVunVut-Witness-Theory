Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Plan — K9_A Deep Review (Provenance + 4-Layer RCA)

**Target candidate:** K9_A — V-Filter (Three-Case, EX-Enriched)
**Phase:** P1 (executes this plan)
**Method:** AHP-driven component provenance audit + 4-layer Root Cause Analysis
**Parent program:** [K9 Deep Review Master Index](../index.md)
**Pre-existing sources:** [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md), [K9S3_ranking.md](../../k9_analysis/K9S3_ranking.md), PP-1 v2
**Status:** Plan v0.3 (2026-05-27) — **P1 EXECUTED** (see §0 file map and §14a execution RCA). RCA framework formalized, all K9_A artifacts unified under `k9_a/`.

---

## §0. Predecessor and Successor File Map

### §0.1 Predecessor files (read BEFORE P1 execution)

These are the SOT inputs and contextual documents that informed the deep review.

**K9_A primary sources:**

- [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) — K9-S2 verdict + constraint check + derivation trace (CONDITIONAL PASS, Class D).
- [PP1_K9A_fixed.md](../../../04_governance/pre_plan/PP1_K9A_fixed.md) — PP-1 v2 three-case EX-enriched design (root cause of K9_A's current form).

**Comparative context:**

- [K9S3_ranking.md](../../k9_analysis/K9S3_ranking.md) — DIM-1…DIM-5 ranking of K9_A vs K9_E.
- [K9S6_new_candidates.md](../../k9_analysis/K9S6_new_candidates.md) — post-S3 candidate revisions (no K9_A modification found).
- [VVV_QMRF_K9_Analysis_Plan.md](../../VVV_QMRF_K9_Analysis_Plan.md) — master K9 analysis plan + master context block.

**K-Space SOT (SOT-2/SOT-3, PEER-SYNC pair):**

- [K_Space_Axiomatization.md (canonical)](../../../../meta_architecture/K_Space_Axiomatization.md) — §K1, §K3, §K4, §K5 verified.
- [K_Space_Axiomatization.md (Class C copy)](../../../01_axiomatization/K_Space_Axiomatization.md) — peer copy.

**BE SOT (SOT-1):**

- [`SYSTEM_Buddhist_Epistemology/system_be_full.md`](../../../../../../SYSTEM_Buddhist_Epistemology/system_be_full.md) — verified anchors: `N_BE_00006` (bhrānti), `N_BE_00011` (svasaṃvedana), `N_BE_00022` (arthakriyā), `N_BE_00253` (anupalabdhi RCA-level), `N_BE_00197/00198` (arthakriyā sub-senses).

**Anti-Hallucination Pipeline (AHP):**

- [`03_sot_traceability.md`](../../../../anti_hallucinations/03_sot_traceability.md) — SOT registry conventions (SOT-1…SOT-6).
- [`04_analysis.md`](../../../../anti_hallucinations/04_analysis.md) — 5-Whys RCA framework.
- [`05_scoring.md`](../../../../anti_hallucinations/05_scoring.md) — H-score rubric (0–10 bands).
- [`label_system.md`](../../../../anti_hallucinations/label_system.md) — `[AH-OK]`/`[AH-LOW]`/`[AH-WARN]`/`[AH-HIGH]`/`[AH-CRIT]` + secondary labels.
- [`00_top_10_hallucinations_record.md`](../../../../anti_hallucinations/00_top_10_hallucinations_record.md) — top-10 cross-reference target.

**Parent program & meta:**

- [K9 Deep Review Master Index](../index.md) — parent program (P0–P7 phase plan, SOT registry, conventions).
- [project_vvv_qmrf_class_c/index.md](../../../index.md) — Class C master index (Class boundaries, v31 changes, Layer 3+4 distinction).

**EX compass (NOT primary anchor; cross-checked only):**

- `documents/research_documents/project_vvv_qmrf_class_c/05_ex_compass/` — `N_QM_VVV_00020` (Validated Absence), `N_QM_VVV_00027` (Born Rule Act-Result Identity), `N_QM_VVV_00029` (Retroactive Override), `N_QM_VVV_00032` (Registration Error).

### §0.2 Successor files (produced BY P1 execution, alongside this plan)

P1 produced exactly the 3-file shape declared in §1 of this plan. All live in this folder (`k9_a/`):

| File | Role | Status |
|------|------|--------|
| `plan_k9_a_deep_review.md` (this file) | Methodology + 4-layer RCA framework + execution RCA | v0.3 (updated post-execution) |
| [`rca_k9_a_chains.md`](./rca_k9_a_chains.md) | Layer 0 Meta-RCA + 9 Layer-1 5-Whys (A-09, A-12, A-17, A-18, A-19, A-20, A-21, A-22, A-23) + 3 Layer-2 cluster RCAs (C-1, C-2, C-3) + Layer-3 verdict RCA | v0.1 (P1 execution) |
| [`report_k9_a_traceability_matrix.md`](./report_k9_a_traceability_matrix.md) | 23-row component traceability matrix + aggregate metrics + 7-item action register + 3 PEER-SYNC suggestions | v0.1 (P1 execution) |

> **Reading order:** plan → rca_chains (full 4-layer RCA) → report (matrix + actions + PEER-SYNC). The plan is the methodology contract; the chains are the deep analysis; the report is the operational summary.

### §0.3 External-impact suggestions emerging from P1

P1 produced 3 PEER-SYNC suggestions targeting files OUTSIDE `k9_a/` (advisory only; require separate approval):

- **PS-1** → [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) — fix `isNull → K8` to `isNull → K4(b)` + drop stale line ranges.
- **PS-2** → K9_A description in K9S2 / `VVV_QMRF_K9_Analysis_Plan.md` — document K9_A as Layer 3+4 hybrid.
- **PS-3** (optional) → [`SYSTEM_Buddhist_Epistemology/system_be_full.md`](../../../../../../SYSTEM_Buddhist_Epistemology/system_be_full.md) — add `bādhaka` as RCA-level node.

---

## §1. Objective

Run a **provenance audit** on every atomic component of K9_A **AND** a **4-layer Root Cause Analysis** on the candidate as a whole. P1 produces three coupled deliverables — all in this folder (`k9_a/`):

| Deliverable | Purpose |
|-------------|---------|
| `plan_k9_a_deep_review.md` (this file) | Methodology + 4-layer RCA framework |
| `report_k9_a_traceability_matrix.md` | Component inventory, SOT anchors, H-scores, AHP labels |
| `rca_k9_a_chains.md` | Full 5-Whys chains for Layer 0, Layer 1 (per H≥5 component), Layer 2 (clusters), Layer 3 (verdict) |

**Out of scope:** Re-running DIM-1…DIM-5 ranking from K9-S3. The deep review is a *provenance + RCA* operation, prerequisite to any verdict change.

---

## §2. K9_A Definition (Reference)

From [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) lines 14–31 and PP-1 v2:

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

> **Reminder:** EX references (`N_QM_VVV_*`) are **compass only**, not primary SOT. They must be cross-traced to SOT-1 / SOT-2/3 / SOT-5 to count toward Trace_Score.

---

## §3. SOT Registry (re-use parent `index.md` §3.2)

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

## §4. 4-Layer RCA Framework (CORE OF P1)

This is the **central methodological addition in v0.2**. RCA does not run only on weak components — it runs on **four nested layers**, each answering a distinct "why".

### Layer 0 — Meta-RCA (about K9_A itself)

**Question:** Why does K9_A exist? What structural gap in K1–K8 does it claim to fill, and why was V-filter the chosen shape?

**Output:** One RCA chain at the start of `rca_k9_a_chains.md` (§ Layer 0).

**Template:**

```
Symptom: K9_A claims to bridge binary K-state (V ∈ {0,1}) to continuous probability.
  Why 1: What forces a probability rule beyond K1–K8?
  Why 2: Why a *V-filter* form and not direct Born rule?
  Why 3: What forces the three-case partition (V=1, V=0, isNull)?
  Why 4: Why is v_rate introduced at population level, not per-event?
  Why 5: What is the root structural necessity that K9_A satisfies (and which other K9 candidates may also satisfy)?
    Root cause: <one sentence>
    Implication: <does K9_A uniquely satisfy this necessity, or is it one of several valid forms?>
```

Layer 0 RCA must be completed **before** Layer 1 component-level work, because it sets the criteria by which each component is judged "necessary" or "incidental".

### Layer 1 — Per-Component RCA

**Question:** For every component, what causal chain produced its presence in K9_A?

**Granularity:**
- **All components** get a **3-Whys chain** (lightweight RCA) — recorded inline in the traceability matrix `RCA Summary` column.
- **Components with H ≥ 5 OR Trace = 0/6** get a **full 5-Whys chain** — recorded in `rca_k9_a_chains.md` § Layer 1.

**3-Whys (lightweight, inline) template:**

```
3-Whys for A-NN (<component>):
  Why 1: <why does this appear in K9_A?>
  Why 2: <where does the previous "why" trace to?>
  Why 3: <SOT layer or assumption flag?>
  → Anchor verdict: <SOT-X | derived from PP-1 v2 | orphan>
```

**5-Whys (full, separate file) template:**

```
5-Whys for A-NN (<component>) — H=<score>, Trace=<x/6>
  Symptom: <observed weakness — orphan, weak anchor, ambiguous semantics>
    Why 1: <immediate cause>
      Why 2: <upstream cause>
        Why 3: <structural cause>
          Why 4: <root assumption / category boundary>
            Why 5: <SOT gap / definitional gap / framework boundary>
              Root cause: <one sentence>
              Fix candidate: <Confirm | Fix | Re-derive | Remove | Defer>
              Affected siblings: <other components likely affected by same root cause>
```

### Layer 2 — Cluster RCA (cross-component patterns)

**Question:** Do orphans / weak anchors cluster? Is there a *shared* root cause that produces multiple weak components?

**Triggers (run Layer 2 if any holds):**
- ≥ 2 orphans exist (Trace = 0/6).
- ≥ 3 components share the same upstream "Why" in their Layer 1 chains.
- ≥ 2 components both depend on PP-1 v2 only (no L1/L2/L3 anchor).

**Template:**

```
Cluster <C-1>: <name — e.g., "v_rate + N_bhranti + N_null all unanchored at K1–K8">
  Affected components: A-NN, A-MM, A-PP
  Shared symptom: <what they have in common>
    Why 1: <shared upstream cause>
      Why 2: <deeper cause>
        Why 3: <structural / SOT-level cause>
          Why 4: <root assumption>
            Why 5: <category boundary or framework gap>
              Root cause: <one sentence describing the SHARED root>
              Fix strategy: <does fixing the cluster require one targeted change or multiple?>
              Priority: <HIGH if root cause is structural; MEDIUM if cosmetic>
```

### Layer 3 — Verdict-Level RCA

**Question:** After Layers 0–2, does the K9-S3 verdict (CONDITIONAL PASS, DIM-2 = 2/5) still hold?

**Template:**

```
Verdict RCA:
  S3 verdict (2026-05-23): CONDITIONAL PASS, Class D, DIM-2 = 2/5 (distinguishability).
  S3 root cause for low DIM-2: P(o|k) at probability level = Tr(E_o ρ) under Case 1; δP = 0 vs Born rule.

  Post-deep-review question 1: Does this root cause still apply?
    Why 1: <yes/no, with evidence from matrix>
    Why 2: <which components confirm/refute>
    Why 3: <what changed in v31 that could affect this — T9, T8-H1, K5_prospective>
    → Update verdict: <unchanged | softened | strengthened | re-classified>

  Post-deep-review question 2: Does K9_A have hidden registration-layer testability?
    (N_bhranti, N_null measurable at SOT-6 Proietti event-level?)
    Why 1: <can Proietti raw data distinguish a Case 2 event from a Case 1 event?>
    Why 2: <what does "no P assignment" mean operationally for Case 2/3 events?>
    Why 3: <does v_rate fitting require event-level discrimination?>
    → Hidden testability: <yes — flag for further study | no — confirms Class D>

  Final reconciliation: <3–5 sentences. Recommendation for K9_A's status going forward.>
```

---

## §5. Methodology (10 Steps — RCA-Augmented)

Compared to the prior v0.1 (9 steps), step 0 (Layer 0 RCA) is added at the front and Layer 2 (Cluster RCA) is added as step 7.

| Step | Action | Output location |
|------|--------|-----------------|
| **0** | **Layer 0 Meta-RCA** — why does K9_A exist? | `rca_k9_a_chains.md` § Layer 0 |
| 1 | **Inventory** — list every component (≤ 25) | `report_k9_a_traceability_matrix.md` § Inventory |
| 2 | **SOT Lookup** — grep SOT-1/2/3/5/6 for each component | matrix anchor cells |
| 3 | **Anchor Recording** — cite file path + line range OR node ID | matrix anchor cells |
| 4 | **Trace_Score + H-score** — per AHP `05_scoring.md` | matrix scoring columns |
| 5 | **Label Assignment** — primary + secondary AHP labels | matrix label columns |
| 6 | **Layer 1 Per-Component RCA** — 3-Whys (inline) for all; 5-Whys (separate) for H ≥ 5 or Trace = 0/6 | matrix RCA col + `rca_k9_a_chains.md` § Layer 1 |
| **7** | **Layer 2 Cluster RCA** — find shared root causes | `rca_k9_a_chains.md` § Layer 2 |
| 8 | **Action Assignment** — Confirm / Fix / Re-derive / Remove / Defer | matrix Action column |
| 9 | **Cross-Reference AHP top-10** — link to `00_top_10_hallucinations_record.md` | report § Cross-References |
| **10** | **Layer 3 Verdict-Level RCA** — does S3 verdict still hold? | `rca_k9_a_chains.md` § Layer 3 + report § Verdict Reconciliation |

---

## §6. Draft Component Inventory (≈ 22 items)

Anchors marked `<TBD>` are hypotheses; P1 must verify.

| ID | Component | Type | Expected SOT trace (hypothesis) | Pre-RCA risk |
|----|-----------|------|-------------------------------|--------------|
| A-01 | `k = (M, o, cert, t, V)` K-state tuple | SYMBOL | SOT-2/3 (K1) | LOW |
| A-02 | `V(k) ∈ {0,1}` validity flag | SYMBOL | SOT-2/3 (K4); SOT-1 (`N_BE_00006`) | LOW |
| A-03 | `cert(k) ∈ {0,1}` certification | SYMBOL | SOT-2/3 (K3); SOT-1 (`N_BE_00001` svasaṃvedana) | LOW |
| A-04 | `isNull(k)` predicate | SYMBOL | SOT-2/3 (K4 isNull clause); SOT-1 | MED |
| A-05 | `o` outcome | SYMBOL | SOT-5 (P3 measurement) | LOW |
| A-06 | `Tr(E_o ρ)` Born rule | OPERATION | SOT-5 (P3) | LOW (`[AH-OK]`) |
| A-07 | `E_o` POVM element | SYMBOL | SOT-5 (P3) | LOW |
| A-08 | `ρ` density matrix | SYMBOL | SOT-5 (P1 state) | LOW |
| A-09 | `arthakriyā` (pragmatic efficacy) | TERM | SOT-1 (`N_BE_?????` <TBD>); EX `N_QM_VVV_00027` | HIGH |
| A-10 | `bhrānti` (erroneous cognition) | TERM | SOT-1 (`N_BE_00006`); EX `N_QM_VVV_00032` | LOW |
| A-11 | `anupalabdhi` (non-cognition) | TERM | SOT-1 (`N_BE_?????` <TBD>); EX `N_QM_VVV_00020` | HIGH |
| A-12 | `bādhaka` (contradicting cognition) | TERM | SOT-1 (`N_BE_00006`); ED_BE_? | MED |
| A-13 | Case-split partition (Case 1/2/3) | OPERATION | SOT-2/3 (K4 partition?) OR derived in PP-1 v2 | HIGH |
| A-14 | `V=1 ∧ ¬isNull → Born rule` (Case 1) | OPERATION | SOT-2/3 (K4) + SOT-5 (P3) | LOW |
| A-15 | `V=0 → no P, count N_bhranti` (Case 2) | OPERATION | SOT-2/3 (K5 V→0 via ⊥_K?) + SOT-1 | MED |
| A-16 | `isNull → no P, count N_null` (Case 3) | OPERATION | SOT-2/3 (K4 isNull) + SOT-1 | MED |
| A-17 | `v_rate ∈ [0,1]` population free parameter | ASSUMPTION | **expected ORPHAN** — no L1/L2/L3 anchor | HIGH |
| A-18 | `N_bhranti` counter | SYMBOL | Derived from A-02 + A-15 | MED |
| A-19 | `N_null` counter | SYMBOL | Derived from A-04 + A-16 | MED |
| A-20 | "Population parameter, not per-event" | ASSUMPTION | <expected weakly anchored> | MED |
| A-21 | "No P assignment" semantics (Cases 2 & 3) | OPERATION | Custom to K9_A — outside Born rule | MED |
| A-22 | EX enrichment marker (`EX N_QM_VVV_*`) | ASSUMPTION | EX (compass-only) | Trace = 0 unless cross-traced |

> P1 may merge or split items after re-reading PP-1 v2 in full.

---

## §7. Traceability Matrix Template (P1 — in `report_k9_a_traceability_matrix.md`)

```
| ID  | Component | Type | SOT-1 (BE)   | SOT-2/3 (K_Space)   | SOT-4 (CLAUDE) | SOT-5 (Std QM) | SOT-6 (Proietti) | Trace | H | Primary Label | Secondary | RCA Summary | Action |
|-----|-----------|------|--------------|----------------------|-----------------|-----------------|-------------------|-------|---|---------------|-----------|-------------|--------|
| A-01| k tuple   | SYM  | -            | K1, §<line range>    | def §<line>     | -               | -                 | 2/6   | 2 | [AH-OK]       | —         | 3-Why: K1   | Confirm|
| A-02| V(k)      | SYM  | N_BE_00006   | K4, §<line range>    | def §<line>     | -               | -                 | 3/6   | 1 | [AH-OK]       | —         | 3-Why: K4+BE| Confirm|
| ... | ...       | ...  | ...          | ...                  | ...             | ...             | ...               | ...   | ..| ...           | ...       | ...         | ...    |
| A-17| v_rate    | ASSU | -            | -                    | -               | -               | -                 | 0/6   | 8 | [AH-HIGH]     | [AH-ORPHAN]| see L1 RCA  | Re-derive or Remove|
```

**Column conventions:**
- Anchor: `<node ID>` for BE; `K<n>, §<line range>` for K_Space; `P<n>` for QM; `arXiv:1902.05080 Fig.<n>` for Proietti.
- `Trace` = `#anchored_SOTs / 6` (SOT-4 excluded; SOT-2 ≡ SOT-3 counted once).
- `H` = integer 0–10 per AHP `05_scoring.md`.
- `RCA Summary` = "3-Why: <short>" inline; for full chain, see `rca_k9_a_chains.md` § Layer 1 § A-NN.
- `Action` = `Confirm` / `Fix` / `Re-derive` / `Remove` / `Defer`.

---

## §8. RCA Chains File Template (P1 — in `rca_k9_a_chains.md`)

```
# RCA Chains — K9_A Deep Review

## Layer 0 — Meta-RCA on K9_A's existence
<full 5-Whys chain per §4 Layer 0 template>

## Layer 1 — Per-Component RCA
### A-NN (<component>) — H=<x>, Trace=<y/6>
<full 5-Whys chain per §4 Layer 1 template>
(only components with H ≥ 5 or Trace = 0/6 get an entry here;
 lightweight 3-Whys for others lives in the matrix RCA Summary column.)

## Layer 2 — Cluster RCA
### Cluster C-1: <name>
<full chain per §4 Layer 2 template>
### Cluster C-2: ...
(only triggered if Layer 2 conditions met — see §4)

## Layer 3 — Verdict-Level RCA
<full chain per §4 Layer 3 template>
```

---

## §9. Aggregate Metrics (in P1 report — `report_k9_a_traceability_matrix.md`)

| Metric | Formula | Target |
|--------|---------|--------|
| Total components | count rows | 18–25 |
| Orphan count | rows with Trace = 0/6 | 0 (any orphan triggers Layer 1 + Layer 2 RCA) |
| Mean H-score | sum(H) / count | ≤ 4.0 |
| Components with H ≥ 7 | count | ≤ 3 |
| BE-anchored (SOT-1) | rows with SOT-1 ≠ blank | ≥ 4 (the four Sanskrit terms) |
| QM-anchored (SOT-5) | rows with SOT-5 ≠ blank | ≥ 4 (Born rule, ρ, E_o, o) |
| Pure-derived (only PP-1 v2) | rows with no L1/L2/L3 trace | 0 ideally; flag if > 0 |
| Layer 1 5-Whys count | components with full RCA | matches (#H≥5 + #orphans) |
| Layer 2 clusters | count | ≥ 1 if Layer 2 triggered |
| Layer 3 verdict change | unchanged / softened / strengthened / re-classified | reported |

---

## §10. Sources to Read (Required Before P1 Execution)

1. **K9_A primary:**
   - [K9S2_candidate_A.md](../../k9_analysis/K9S2_candidate_A.md) — full file.
   - PP-1 v2 — grep repository for `"PP-1 v2"` to locate.

2. **Comparative context:**
   - [K9S3_ranking.md](../../k9_analysis/K9S3_ranking.md) — DIM-1…DIM-5.
   - [K9S6_new_candidates.md](../../k9_analysis/K9S6_new_candidates.md) — post-S3 revisions.

3. **K-Space SOT:**
   - [K_Space_Axiomatization.md (canonical)](../../../../meta_architecture/K_Space_Axiomatization.md) — §K3, §K4, §K5.
   - [K_Space_Axiomatization.md (Class C copy)](../../../01_axiomatization/K_Space_Axiomatization.md) — PEER-SYNC verification.

4. **BE SOT:**
   - `SYSTEM_Buddhist_Epistemology/system_be_full.md` — grep for `arthakriyā`, `bhrānti`, `anupalabdhi`, `bādhaka`. Record exact `N_BE_XXXXX` IDs.

5. **AHP:**
   - [`03_sot_traceability.md`](../../../../anti_hallucinations/03_sot_traceability.md) — SOT registry conventions.
   - [`04_analysis.md`](../../../../anti_hallucinations/04_analysis.md) — 5-Whys RCA framework.
   - [`05_scoring.md`](../../../../anti_hallucinations/05_scoring.md) — H-score rubric.
   - [`label_system.md`](../../../../anti_hallucinations/label_system.md) — label taxonomy.
   - [`00_top_10_hallucinations_record.md`](../../../../anti_hallucinations/00_top_10_hallucinations_record.md) — cross-reference top 10.

6. **EX (compass only):**
   - `05_ex_compass/` — look up `N_QM_VVV_00020`, `N_QM_VVV_00027`, `N_QM_VVV_00032`.

---

## §11. Verification Checklist (P1 Closing Gates)

P1 is complete only when **all** of the following hold:

### Inventory + Matrix
- [ ] ≥ 15 components inventoried; total ≤ 25.
- [ ] Every BE anchor (SOT-1) cites a specific `N_BE_XXXXX` or `ED_BE_XXXXX` from `system_be_full.md`, verified by grep.
- [ ] Every K_Space anchor (SOT-2/3) cites file path + line range; PEER-SYNC parity verified.
- [ ] Every Standard QM anchor (SOT-5) cites a specific postulate (P1–P4).
- [ ] Zero un-cited anchors.
- [ ] Aggregate metrics §9 computed and reported.

### RCA Layers
- [ ] **Layer 0** Meta-RCA chain complete in `rca_k9_a_chains.md`.
- [ ] **Layer 1** 3-Whys inline for every component (matrix `RCA Summary` col).
- [ ] **Layer 1** Full 5-Whys for every component with H ≥ 5 OR Trace = 0/6, in `rca_k9_a_chains.md`.
- [ ] **Layer 2** Cluster RCA run if any trigger condition (§4 Layer 2) holds; otherwise explicit "Layer 2 not triggered" note.
- [ ] **Layer 3** Verdict-level RCA + 3–5 sentence reconciliation, in `rca_k9_a_chains.md` AND mirrored in `report_k9_a_traceability_matrix.md` § Verdict.

### Cross-Cuts
- [ ] AHP `00_top_10_hallucinations_record.md` cross-referenced for every `[AH-HIGH]`/`[AH-CRIT]` row.
- [ ] No edits to `K_Space_Axiomatization.md` (canonical or Class C). Any suggested edit lives in a "PEER-SYNC suggestion" subsection at the end of `report_k9_a_traceability_matrix.md`.

---

## §12. Risks Specific to K9_A

| # | Risk | Level | Mitigation |
|---|------|-------|-----------|
| R1-A | **Sanskrit terms** (`arthakriyā`, `anupalabdhi`) may not have direct `N_BE_XXXXX` nodes in the 30-node BE SOT | HIGH | Also search `ED_BE_*` edges; if absent, flag `[AH-WARN]` and propose BE-extension as Layer 2 cluster issue |
| R2-A | **`v_rate` is likely an ORPHAN** — no axiomatic source | HIGH | Pre-flag `[AH-HIGH] + [AH-ORPHAN]`; Layer 1 5-Whys must establish if root cause is fixable (link to K7 closure) or fatal |
| R3-A | **`N_bhranti`, `N_null` counters** lack operational definition | MEDIUM | Layer 1 must clarify; Layer 3 must address whether these provide hidden testability |
| R4-A | **Three-case partition** may have no formal SOT anchor (only PP-1 v2) | MEDIUM | Layer 1 + Layer 2 must determine if partition is exhaustive (no missing case) and whether it can be derived from K4 |
| R5-A | **Case 2 "No P assignment"** could violate C-NORM if not carefully scoped | MEDIUM | Cross-check K9-S1 constraint set; document the conditional |
| R6-A | **EX-only anchors** (`N_QM_VVV_*`) mistaken for primary SOT | HIGH | Strict rule applied to every row: EX appearance does not contribute to Trace_Score |
| R7-A | **PP-1 v2 location unknown** | LOW | First grep step in P1 |
| R8-A | **Layer 0 RCA over-philosophizes** (drifts beyond V-filter to general K9 design) | MEDIUM | Hard scope: Layer 0 must conclude with one specific root cause + one specific implication for K9_A |
| R9-A | **Layer 2 cluster invention** — RCA artificially groups unrelated components | MEDIUM | Trigger conditions in §4 Layer 2 are strict; cluster requires ≥ 2 components with shared upstream "Why" |
| R10-A | **Confirmation bias** — judgment biased by K9-S3 verdict | HIGH | Blind-score H and Trace before re-reading K9-S3; record Layer 3 RCA *before* opening K9-S3 |

---

## §13. Expected Deliverable Shapes

### `report_k9_a_traceability_matrix.md` (~ 400–600 lines)

```
1. Header (Author + metadata)
2. Executive Summary (5–10 lines: totals, orphans, mean H, verdict)
3. K9_A Definition (quoted from §2)
4. Component Inventory (numbered list)
5. Full Traceability Matrix (§7 template)
6. Aggregate Metrics (§9 table)
7. Verdict Reconciliation (3–5 sentences, mirrors Layer 3 RCA conclusion)
8. Action Register (Confirm / Fix / Re-derive / Remove / Defer items)
9. Cross-References (AHP top-10, K9-S3, K9-S6)
10. PEER-SYNC Suggestions (if any; otherwise "None")
11. Change Log
```

### `rca_k9_a_chains.md` (~ 300–500 lines)

```
1. Header
2. Layer 0 — Meta-RCA (5-Whys)
3. Layer 1 — Per-Component RCA (one subsection per component with H ≥ 5 or Trace = 0/6)
4. Layer 2 — Cluster RCA (if triggered)
5. Layer 3 — Verdict-Level RCA
6. Aggregate RCA Findings (1–2 paragraphs: what's the dominant root cause of K9_A's weaknesses?)
7. Change Log
```

---

## §14. Estimated Complexity

| Activity | Items | Effort |
|----------|-------|--------|
| Read sources (§10) | 6 primary + 5 AHP files | ~30 min |
| Layer 0 Meta-RCA | 1 chain | ~20 min |
| Inventory (step 1) | ≈ 22 components | ~30 min |
| SOT lookup + anchoring (steps 2–3) | 22 × 5 cells = 110 cells | ~75 min (grep-heavy) |
| Scoring + labeling (steps 4–5) | 22 rows | ~20 min |
| Layer 1 RCA — 3-Whys inline | 22 rows | ~30 min |
| Layer 1 RCA — full 5-Whys | ≈ 4–6 components | ~40 min |
| Layer 2 Cluster RCA (if triggered) | 1–3 clusters | ~30 min |
| Layer 3 Verdict RCA | 1 chain | ~20 min |
| Action assignment + cross-ref + writing report | — | ~45 min |
| **Total** | — | **~5–6 hours focused session** |

Complexity: **MEDIUM-HIGH** (RCA-augmented vs prior MEDIUM).

---

## §14a. Execution RCA — Plan v0.2 vs P1 Actual

This section was added in plan v0.3 after P1 was executed. It is a Root Cause Analysis comparing what the plan predicted versus what the execution actually produced. Findings here feed the change log §16.

### §14a.1 Plan ↔ Actual delta table

| Aspect | Plan (v0.2) | Actual (P1) | Match? | RCA verdict |
|--------|-------------|-------------|--------|-------------|
| Inventory size | ≈ 22 components | **23 components** (added A-23 audit-finding) | NO (+1) | EXPECTED — plan §11 verification checklist explicitly permits in-flight refinement; A-23 emerged from a citation-drift discovery during Step 2 (SOT lookup) |
| Mean H-score | ≤ 4.0 target | **3.7** | YES | Plan target met; band 🔵 BLUE |
| Orphans (Trace = 0/6) | 0 target | **2** (A-17 `v_rate`, A-20 population convention) | NO | EXPECTED per Risk R2-A (pre-flagged as `[AH-HIGH] + [AH-ORPHAN]`). Resolved by Layer 2 Cluster C-1 RCA → reclassification as Layer 4 boundary variables, not unresolved orphans |
| Components with H ≥ 7 | ≤ 3 target | **3** (A-12, A-17, A-20) | YES (at cap) | At cap, no overflow |
| BE-anchored (SOT-1) | ≥ 4 target | **10 rows** | YES (exceeded) | Sanskrit terms anchored more broadly than draft anticipated (also covers Case 2/3 rules) |
| QM-anchored (SOT-5) | ≥ 4 target | **5 rows** | YES (exceeded) | Includes Case 1 rule (A-14) in addition to ρ, E_o, o, Tr(E_o ρ) |
| Layer 1 5-Whys count | "match (#H≥5 + #orphans)" | **9 full chains** (A-09, A-12, A-17, A-18, A-19, A-20, A-21, A-22, A-23) | YES | Matches formula |
| Layer 2 trigger | "if triggered" | **All 3 triggers fired** (orphan ≥ 2, shared upstream ≥ 3, PP-1 v2-only ≥ 2) | NO (stronger) | Plan §4 Layer 2 conditions all activated; 3 clusters identified (C-1, C-2, C-3) |
| Layer 3 verdict outcome | unchanged / softened / strengthened / re-classified | **UNCHANGED** (Layer 3 §Final reconciliation) | YES | DIM-2 ≈ 2/5 confirmed; K9-S3 holds; K9_A remains conservative Class D |
| Estimated effort | ≈ 5–6 hours | ~ 2 hours (single session, automated SOT grep) | NO (faster) | Plan estimate assumed manual SOT cross-checking; AHP `03_sot_traceability.md` pre-existing matrix accelerated Step 2 significantly |
| PEER-SYNC suggestions | "if any; otherwise 'None'" | **3 suggestions filed** (PS-1, PS-2, PS-3) | NO (more) | Citation-drift cluster (C-3) generated PS-1; ensemble reframing generated PS-2; `bādhaka` BE-extension generated PS-3 |
| Action register | Confirm/Fix/Re-derive/Remove/Defer items | **7 actions** (AC-01…AC-07) | YES | Covers all H ≥ 5 components plus the verdict confirmation |

### §14a.2 Surprises (positive)

- **AHP `03_sot_traceability.md` already contained K9_E and K1–K8 SOT cross-references** — the existing table accelerated Step 2 (SOT lookup) and validated the SOT-1…SOT-6 scoring convention used here. P1 did not need to invent or audit the SOT registry.
- **K9_A's three-case partition is BETTER anchored than the plan's pre-RCA risk assessment suggested.** Risk R4-A worried that the partition might have only PP-1 v2 anchor; in fact K4(a) + K5 + K4(b) jointly cover the three cases, so the partition is K_Space-derivable (A-13: H=4, `[AH-LOW]`).
- **`bhrānti` (A-10) has the strongest BE anchor** of all Sanskrit terms (N_BE_00006, 30-core), giving Case 2 a very clean BE → K_Space mapping.

### §14a.3 Surprises (negative)

- **K9S2 citation drift was unanticipated** — Risk R7-A flagged that PP-1 v2 location was unknown, but Risk R-* did NOT predict that K9S2 itself contains stale line ranges and an incorrect `isNull → K8` anchor. This emerged during Step 2 verification (A-23) and triggered Cluster C-3.
- **`bādhaka` lacks a dedicated BE node** — Risk R1-A anticipated that `arthakriyā`/`anupalabdhi` might lack 30-core nodes, but `bādhaka` was assumed to be a sibling node. In fact, the 30-core BE focuses on patient-side concepts; `bādhaka` (the agent role) is subsumed under N_BE_00006. This is a real BE-coverage gap (A-12, H=7).

### §14a.4 What the plan did NOT predict but happened

| Discovery | Where it surfaced | Impact |
|-----------|-------------------|--------|
| A-23 (K9S2 anchor error) | Step 2 SOT lookup for `isNull` | New component added; PS-1 PEER-SYNC suggestion filed; Cluster C-3 triggered |
| Layer 4 reframing as resolution path | Layer 2 Cluster C-1 RCA Why 5 | NEW PEER-SYNC suggestion PS-2 (document K9_A as Layer 3+4 hybrid); resolves 4 components at once |
| Cluster C-2 (BE interpretive coupling) | Layer 1 of A-09, A-10, A-11, A-22 | Confirmed K_Space §0.4 design intent; no defect, but presentation refinement suggested (AC-04) |

### §14a.5 Layer 0 prediction vs Layer 3 outcome consistency

Layer 0 Meta-RCA (Why 5) concluded:

> "K9_A is the MINIMAL K9 form that recovers Born rule exactly when K-side registration is valid (Case 1), explicitly USES K4/K5 (not just K1–K3), and introduces exactly one continuous parameter (`v_rate`) at the ensemble level."

Layer 3 Verdict RCA confirmed: per-event δP = 0 always in Case 1, no v31 update interacts with K9_A, DIM-2 ≈ 2/5 holds. **Layer 0 → Layer 3 chain is internally consistent**: the minimal-form thesis predicted the conservative Class D verdict.

### §14a.6 RCA root cause of execution-vs-plan deviations

5-Whys on "Why did execution exceed plan in some dimensions (PEER-SYNC count, Layer 2 clusters)?"

```
  Why 1: Why were 3 PEER-SYNC suggestions produced when the plan said "if any"?
    Answer: The audit surfaced 3 distinct external-impact issues — citation drift,
            Layer 3+4 hybrid documentation gap, and bādhaka BE-extension.
  Why 2: Why did these 3 issues surface together?
    Answer: They were not visible from K9_A's surface definition; they emerged only
            after Step 2 (SOT lookup) and Step 6 (Layer 1 RCA) forced verification
            against current SOT state.
  Why 3: Why was verification needed only now?
    Answer: K9S2 was written 2026-05-23 (4 days before this audit); no peer-sync
            mechanism existed for derivative documents; K_Space line ranges drift.
  Why 4: Why does no peer-sync mechanism cover derivative documents?
    Answer: PEER-SYNC is scoped to K_Space_Axiomatization canonical ↔ Class C copy
            only (per CLAUDE.md §PEER-SYNC). K9 derivative analysis files are not
            peer-sync'd today.
  Why 5: Is this a systemic gap?
    Root cause: YES — derivative documents (K9S2, K9-S3 etc.) cite K_Space line
                ranges but are not subject to refresh discipline. The K9 Deep
                Review program (this audit's parent) is the FIRST systematic
                attempt to audit this drift; expect similar findings in P2–P6.
    Implication: P2–P6 should include "K9S2_candidate_X.md citation drift check"
                 as a default audit step. Recommend adding to parent
                 `index.md` workflow.
```

### §14a.7 Plan v0.2 acceptance criteria — post-execution status

All 7 P0 v0.2 gate criteria were met BEFORE execution and remain met AFTER execution. The 8th criterion (user confirmation to begin P1) was satisfied with the "execute K9_A" message on 2026-05-27. See updated §15.

---

## §15. Acceptance Criteria for This Plan (P0 v0.2 Gate)

- [x] Methodology (§5) integrates RCA at 4 layers, not only Step 6.
- [x] All P1 outputs land in `k9_a/` subfolder (no parent-folder artifacts).
- [x] SOT registry matches parent `index.md` §3.2.
- [x] Draft inventory (§6) has ≥ 15 candidate components.
- [x] Matrix template (§7) and RCA chains template (§8) are concrete.
- [x] Verification checklist (§11) is operational and includes per-layer RCA gates.
- [x] Risks (§12) cover RCA-specific failure modes (R8 over-philosophizing, R9 cluster invention).
- [ ] User explicitly confirms with "proceed P1" or "execute K9_A" to begin P1.

---

## §16. Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-05-27 | v0.1 | (deprecated, file deleted) Initial plan at parent folder, RCA only at one step. |
| 2026-05-27 | v0.2 | Moved to `k9_a/`. Added 4-layer RCA framework (Layer 0 Meta, Layer 1 Per-Component, Layer 2 Cluster, Layer 3 Verdict). Methodology re-numbered to 10 steps. Deliverables split into 3 files (plan + report + RCA chains). New risks R8/R9/R10 added for RCA-specific failure modes. |

---

*Plan K9_A Deep Review v0.2 (2026-05-27). Provenance + 4-layer RCA. All K9_A artifacts in `k9_a/`. Advisory only — no K_Space edits. PEER-SYNC required for any structural change suggested by P1 outputs.*
