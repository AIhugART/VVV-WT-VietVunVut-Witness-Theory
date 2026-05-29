Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Phase 8 Audit Closure Report — VVV-QMRF-EX v1.6

> **Document type:** RCA audit-closure report
> **Status:** Completed
> **Date:** 2026-05-20
> **Scope:** F-RCA-05, F-RCA-07, F-RCA-08, F-RCA-09, F-RCA-10, F-RCA-11
> **Decision protocol:** 3 rounds max; each round uses RCA x 5-Why x scoring; closure threshold = 4/5

---

## 1. Executive Result

| Finding | Root cause class | Accepted closure action | Round | Score | Status |
|---|---|---|---:|---:|---|
| F-RCA-05 | Mixed baseline / stale audit field | Create Phase 8 full boundary report for 143 entries | 1 | 4.6/5 | RESOLVED |
| F-RCA-07 | Missing re-audit artifact | Use same Phase 8 report as explicit machine-readable boundary re-audit | 1 | 4.7/5 | RESOLVED |
| F-RCA-08 | Historical snapshot not marked | Preserve Phase 5 historical qualifier in plan §13 | 1 | 4.4/5 | RESOLVED |
| F-RCA-09 | Misread community count metric | Update §5.2 to focus on top non-singleton communities | 1 | 4.5/5 | RESOLVED |
| F-RCA-10 | Baseline/current-state ambiguity | Add Phase 4 / Phase 6 / Phase 7 entry-count qualifier | 1 | 4.5/5 | RESOLVED |
| F-RCA-11 | Reproducibility gap / API-boundary mismatch | Deterministic post-detection ordering + context note; no unsupported `random_state` argument | 2 | 4.2/5 | RESOLVED |

**Batch result:** 6/6 findings resolved. 5 resolved in Round 1; 1 resolved in Round 2. No Round 3 required.

---

## 2. Scoring Rubric

| Criterion | Meaning |
|---|---|
| Root-cause fit | Fix addresses the isolated root cause, not only the visible symptom |
| Evidence traceability | Fix points to a concrete artifact, field, or source line |
| Boundary safety | Fix does not overclaim, overwrite frozen artifacts, or violate EX isolation |
| Reproducibility / maintainability | Fix improves future auditability and repeatability |
| Minimality | Fix is surgical and preserves existing valid document structure |

---

## 3. Detailed RCA Closure Notes

### F-RCA-05 — Mixed Phase 5 / Phase 6 baseline

**5 Whys:** Symptom: `phase5_coverage_report.json` mixed post-Phase 6 coverage fields with a Phase 5 `entries_audited: 111` audit field. Why? New entries were added after the original audit. Why not synchronized? Boundary audit was phase-specific, not invalidation-triggered. Why harmful? JSON and Markdown told different audit scopes. Why Phase 8? Phase 7 raised scope again to 143 entries. Root cause: no fresh machine-readable audit artifact existed for the current registry scope.

**Round 1:** Create `data/phase8_boundary_audit_report.json` for 143 entries. Score: 1.0 + 0.95 + 0.9 + 0.9 + 0.85 = **4.6/5**. **ACCEPTED.**

**Closure evidence:** `data/phase8_boundary_audit_report.json` records `entries_audited: 143`, `violations: 0`, `overall: PASS`.

### F-RCA-07 — Phase 6/7 boundary re-audit not explicitly run

**5 Whys:** Symptom: new entries were assumed to pass boundary checks. Why? Prior audit report covered 120 entries and no post-stretch JSON existed. Why not caught? Boundary validation was documented narratively, not machine-recorded after each registry growth. Why dangerous? Future reviewers cannot distinguish assumption from re-audit. Root cause: missing explicit audit artifact for expanded registry.

**Round 1:** Use Phase 8 report as the explicit re-audit for all current entries, not only the 9 Phase 6 entries. Score: 1.0 + 1.0 + 0.9 + 0.95 + 0.85 = **4.7/5**. **ACCEPTED.**

**Closure evidence:** Scope is 69 `BR_EX_BE` + 74 `BR_EX_QM` = 143 entries; identity claim violations = 0.

### F-RCA-08 — Historical 82.7% K-effective value lacked data trace

**5 Whys:** Symptom: plan quoted 82.7% while JSON later reported 100%. Why? The 82.7% belonged to the Phase 5 historical snapshot before Phase 6. Why did confusion appear? Later JSON was updated to post-Phase 6 state. Why not obvious? The plan line lacked explicit historical qualifier. Root cause: historical milestone and current data snapshot were not separated.

**Round 1:** Preserve the historical qualifier in §13 and explain that later JSON reflects post-Phase 6 state. Score: 0.9 + 0.9 + 0.9 + 0.85 + 0.85 = **4.4/5**. **ACCEPTED.**

**Closure evidence:** `vvv-qmrf-ex-plan.md` §13 now marks Phase 5 as pre-Phase 6 historical baseline.

### F-RCA-09 — Community count dominated by orphan singleton nodes

**5 Whys:** Symptom: community count seemed meaningful but was dominated by singleton orphan BE nodes. Why? All 263 BE nodes were loaded, many without edges. Why does modularity over-count? Disconnected singleton components become separate communities. Why misleading? Total count does not measure BIAN cluster quality. Root cause: plan expectation used total community count as if it were a semantic-cluster metric.

**Round 1:** Update §5.2 expectation: top non-singleton communities are meaningful; total singleton-heavy count is not a quality metric. Score: 0.95 + 0.9 + 0.9 + 0.9 + 0.85 = **4.5/5**. **ACCEPTED.**

**Closure evidence:** `vvv-qmrf-ex-plan.md` Step 2.3 now contains the non-singleton caveat.

### F-RCA-10 — Phase 4 entry count needed baseline qualifier

**5 Whys:** Symptom: Phase 4 log said 111 entries while current registries were larger. Why? Phase 4 was a historical milestone; Phase 6 and Phase 7 later added entries. Why confusing? Plan mixed milestone log with current-state inventory. Why not fixed by changing the number only? That would erase history. Root cause: missing baseline/current-state qualifier.

**Round 1:** Add qualifier with Phase-4 baseline, post-Phase 6, and post-Phase 7 counts. Score: 0.95 + 0.9 + 0.9 + 0.85 + 0.9 = **4.5/5**. **ACCEPTED.**

**Closure evidence:** `vvv-qmrf-ex-plan.md` §13 now records 111 baseline, 120 post-Phase 6, and 143 post-Phase 7.

### F-RCA-11 — Community reproducibility / `random_state` issue

**5 Whys:** Symptom: community count differed across artifacts. Why? Community detection output can vary by graph/order/library behavior. Why proposed `random_state=42`? It looked like a standard reproducibility fix. Why not apply directly? NetworkX 3.3 `greedy_modularity_communities` does not expose a supported `random_state` parameter. Why still fix? Reports need stable ordering and an explicit API boundary note. Root cause: reproducibility fix was underspecified against the actual library API.

**Round 1:** Add `random_state=42` directly. Score: 1.0 + 0.8 + 0.9 + 0.4 + 0.6 = **3.7/5**. **REJECTED** because the local NetworkX API does not support that parameter.

**Round 2:** Sort detected communities deterministically after detection and document the API boundary in context. Score: 0.85 + 0.9 + 0.95 + 0.8 + 0.7 = **4.2/5**. **ACCEPTED.**

**Closure evidence:** `phase2_intersection_analysis.py` now sorts communities by `(-len(c), sorted(c))`; `data/vvv_qmrf_ex_context.json` records that `random_state` is unsupported in NetworkX 3.3 and that `stable_post_detection_sort` is the replacement control.

---

## 4. Closure Verification

| Artifact | Verification |
|---|---|
| `data/phase8_boundary_audit_report.json` | Created; `entries_audited: 143`, `violations: 0`, `overall: PASS` |
| `phase2_intersection_analysis.py` | Community output ordering stabilized without unsupported API argument |
| `data/vvv_qmrf_ex_context.json` | Phase 8 closure metadata added |
| `vvv-qmrf-ex-plan.md` | Phase 8 table marked DONE for F-RCA-05/07/08/09/10/11 |

---

*Phase 8 closes audit findings by fixing root causes: stale audit scope, missing re-audit artifact, historical/current-state ambiguity, community metric interpretation, baseline ambiguity, and reproducibility/API-boundary mismatch.*