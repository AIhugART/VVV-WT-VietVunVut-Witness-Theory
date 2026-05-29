Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF-EX Archives

**Archived on:** 2026-05-21 (after v1.7 commit `7fdd681` — Phase 11 fully closed)

**Archival authority:** Plan §16 (Post-v1.7 Archival)

---

## Purpose

This directory preserves **process artefacts** from VVV-QMRF-EX execution. These files are not final results — they are the working logs used to reach the results now visible at the top-level folder.

Files here are **read-only references**. The active, canonical deliverables remain in the parent directory (`vvv-qmrf-ex/`).

---

## Archived Files

### `phase7_logs/` — Phase 7 Stretch Mapping Process Logs

| Original path | New path | Reason |
|---|---|---|
| `phase7_candidate_pool.md` | `archives/phase7_logs/phase7_candidate_pool.md` | Working candidate pool (≥3 BE candidates per VVV node); final accepted entries are in `br_ex_be_registry.md` |
| `phase7_ke_of_rca_log.md` | `archives/phase7_logs/phase7_ke_of_rca_log.md` | Per-entry RCA decision log for 13 KE-OF nodes (threshold 4.5/5); conclusions captured in `reviews/rca_checkpoint.md` + `reviews/rca_plan_v1.6_completion_audit.md` |
| `phase7_ke_sc_rca_log.md` | `archives/phase7_logs/phase7_ke_sc_rca_log.md` | Per-entry RCA decision log for 10 KE-SC nodes (v1.6 threshold 3.5/5, v1.7 raised to 4.0/5 + carve-out 3.8); v1.7 reclassification annotations still in-file; conclusions in `reviews/rca_plan_v1.7_completion_audit.md` |

---

## Reproducibility Note

`br_ex_be_registry.md` entries with `Phase 7 KE-OF/KE-SC stretch mapping; see <logfile>` in their Origin field point to the files in this directory. Git history preserves full content and diff trail.

The active Python scripts (`phase1_graph_construction.py` through `phase6_expert_mapping.py` + `phase4_graph_sync.py`) remain at top-level — NOT archived — to preserve Criterion C7 reproducibility (graph re-runnable from `vvv_qmrf_ex_graph.json`).

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
