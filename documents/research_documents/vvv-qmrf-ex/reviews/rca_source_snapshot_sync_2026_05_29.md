Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Summary — VVV-QMRF-EX Source Snapshot Sync

> **Date:** 2026-05-29
> **Scope:** `documents/research_documents/vvv-qmrf-ex/source_snapshot/` synchronization with the current codebase
> **Status:** CLOSED — snapshot sync completed; frozen EX metrics preserved
> **Boundary:** This report updates source-snapshot provenance only. It does not recompute EX graph metrics, promote draft bridges, mutate `data/*.json`, or change frozen `/52` baselines.

---

## 1. Define — Symptom vs Cause

**Symptom:** `source_snapshot` no longer matched the current codebase for key VVV-QMRF Core and K-space inputs. The manifest claimed a point-in-time snapshot through the 2026-05-23 partial sync, but current source files had moved forward.

**Cause:** The project intentionally uses `source_snapshot` as a read-only EX input layer, but later Core/K-space work updated the live source files after the previous partial re-snapshot. The snapshot was not re-copied afterward.

---

## 2. Trace — 5 Whys

1. Why did snapshot verification show drift? -> The snapshot copies of `node_QM_VVV.md` and `K_Space_Axiomatization.md` differed from their live codebase originals.
2. Why did those files differ? -> The live codebase advanced to v32/Class C qualified node status and K-space v2.4 after the older snapshot state.
3. Why was the drift risky? -> EX scripts and analyses rely on snapshot inputs for reproducibility and boundary isolation.
4. Why would copying alone not fully fix the risk? -> `phase1_graph_construction.py` still read several live paths directly, so future runs could bypass `source_snapshot` and reintroduce input drift.
5. **Root cause F-RCA-23:** The snapshot layer had been updated as copied files, but the executable Phase 1 input contract still mixed snapshot paths and live codebase paths.

---

## 3. Isolate — Starting Point of Failure

The failure starts at the input-contract boundary:

| Layer | Expected contract | Observed before fix |
|---|---|---|
| Snapshot files | Snapshot copies match declared codebase source versions | Two core inputs drifted from live source |
| Manifest | Partial re-snapshot dates describe current snapshot provenance | Manifest stopped at 2026-05-23 |
| Phase 1 script | Reads EX inputs from `source_snapshot` only | Mixed snapshot and live source paths |

---

## 4. Fix Applied

| File | Fix |
|---|---|
| `source_snapshot/vvv_qmrf_core/node_QM_VVV.md` | Re-copied from `documents/research_documents/vvv-qmrf/node_QM_VVV.md` |
| `source_snapshot/meta_architecture/K_Space_Axiomatization.md` | Re-copied from `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` |
| `source_snapshot/SNAPSHOT_MANIFEST.md` | Added 2026-05-29 partial re-snapshot entry; updated node/K-space inventory and totals notes |
| `phase1_graph_construction.py` | Repointed BE, QM, VVV edge, bridge, and draft-bridge inputs to `source_snapshot` paths |

---

## 5. Verification

Hash verification confirmed all checked source/snapshot pairs match:

| Snapshot pair | Result |
|---|---|
| BE SOT full | MATCH |
| BE compact table | MATCH |
| QM SOT full | MATCH |
| VVV node table | MATCH |
| VVV edge table | MATCH |
| VVV bridge registry | MATCH |
| VVV schema guide | MATCH |
| K-space axiomatization | MATCH |
| Project disclaimer | MATCH |

Parser verification using the updated Phase 1 module returned:

| Metric | Result |
|---|---:|
| BE nodes | 263 |
| VVV nodes | 62 |
| QM nodes | 105 |
| VVV edges | 131 |
| Graphable BR bridges | 13 |
| Draft links | 21 |
| Boundary guards skipped | 2 |
| Draft warnings | 0 |

Additional verification:

- `scripts/sync_check_k_space.sh` returned `PASS: Both copies in sync. Safe to commit.`
- The K-space checker also reported a line-delta warning, but its verdict remained PASS.
- No generated `data/*.json` file was changed by this sync.

---

## 6. Boundary Statement

This sync updates the source input layer only. It must not be interpreted as:

- a recomputation of `v1.5`, `v1.6`, `v1.7`, or node-aligned EX metrics;
- activation of draft bridge rows;
- promotion from EX into Core;
- a new Standard Quantum Mechanics claim;
- a new Buddhist Epistemology equivalence claim.

Frozen EX metrics remain historical baselines. Any future publication-facing re-run must use a new explicit suffix and metric policy.

---

## 7. Closure

**F-RCA-23 closure:** Source snapshot drift was caused by live source updates after the previous partial re-snapshot plus a mixed live/snapshot script input contract. The fix copied the two drifted source files into `source_snapshot`, updated manifest provenance, and forced Phase 1 input paths to read from `source_snapshot` only. Verification confirms the checked snapshot inputs now match the codebase and the parser sees the expected current snapshot counts.
