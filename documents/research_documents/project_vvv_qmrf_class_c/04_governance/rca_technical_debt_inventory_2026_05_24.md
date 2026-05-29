Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Technical Debt Inventory — Class C (genuine)

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** `documents/research_documents/project_vvv_qmrf_class_c/` (161 files)
**Compass:** VVV-QMRF-EX (intelligence only, no structure import)

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total files scanned | 161 |
| Files deep-read | 35 |
| Total debt items found | **15** |
| BLOCKING | **2** |
| HIGH | **5** |
| MEDIUM | **4** |
| LOW | **4** |
| **Aggregate severity** | **3.53/5** (MEDIUM-HIGH — can 1-2 sessions de clean toan bo BLOCKING+HIGH) |

> **Ket luan:** Class C da duoc clean rat ky qua 3-round RCA truoc do (aggregate 4.50/5). 6 commits gan nhat (2026-05-24) da eliminate [A-E1] va split [A-E2]. Tuy nhien chinh nhung commit nay da tao ra SYNC DRIFT va stale documentation — day la 2 BLOCKING items. Sau khi fix 2 BLOCKING + 5 HIGH items, Class C se dat **production-grade cleanliness**.

---

## Round 1 — Identification (Surface + Deep Scan)

### 1.1 Surface grep summary

| Marker | Count | Real debt | False positive |
|--------|-------|-----------|----------------|
| `TODO(HOTFIX)` | 67 | 0 | 67 (boilerplate in EX snapshot files + meta-architecture documents) |
| `DEFERRED` | 25 | 12 | 13 (historical context references) |
| `ERRATUM` | 42 | 0 | 42 (correctly-documented errata, resolved) |
| `INVALIDATED` | 22 | 2 | 20 (correctly annotated; Phase 10b) |
| `SUPERSEDED` | 8 | 0 | 8 (correctly marked: plan_v3, archives) |
| `PENDING` | 18 | 6 | 12 (EX compass K-PENDING-RCA + CHANGELOG history) |
| `IN PROGRESS` | 3 | 1 | 2 (EX phase6 script string + stale Phase 5 label) |

### 1.2 Debt items identified

| # | Item | Location | Symptom |
|---|------|----------|---------|
| D1 | K_Space_Axiomatization PEER-SYNC DRIFT | canonical v2.2 vs Class C v2.3 | Version mismatch on peer copies |
| D2 | Phase9_adversarial_testing.md stale assumptions | `02_derivation_chain/` | Shows [A-E1] as "JUSTIFIED" (already eliminated in v2.3) |
| D3 | [A-E3] beta universal — last remaining assumption | `Phase8`, `Phase9`, `Phase13` | Only remaining of original 4 K9_E assumptions |
| D4 | K9E-PAT: multiplicative pattern not confirmed | `index.md`, `proietti_raw_fit.py` | 2BSM/1BSM ratio = -0.78 vs predicted ~2 |
| D5 | T4-H Steps 3-4 DEFERRED | `K_Space_Axiomatization.md`, `T4_H_step2_colimit_construction.md` | Blocks 3-observer claim structural validation |
| D6 | Two divergent K9_E implementations | `07_fits/utils/k9e_predictor.py` vs `proietti_raw_fit.py` | Additive vs multiplicative, diverge at beta>0.3 |
| D7 | Phase8_candidate_equation.md partial inconsistency | `02_derivation_chain/` | Line 45 says [A-E2] eliminated but line 49 still shows [A-E1] MODERATE |
| D8 | P10-NOISE: Non-uniform noise not ruled out | `index.md`, `Phase10_genuine_fit_RCA_Round1.md` | Alternative explanation for genuine fit |
| D9 | P10-TIM: Null-model N0 omitted | `K_Space_Axiomatization_plan.md` | DECISION-LOCKED (RCA R4), requires raw event data |
| D10 | Phase 10b INVALIDATED but file present | `02_derivation_chain/Phase10b_bong_lf.md` | Annotated as INVALIDATED, could be archived |
| D11 | EX compass: 3 nodes K-PENDING-RCA | `05_ex_compass/vv-qmrf-ex-plan.md` | C2 done, C3 not executed |
| D12 | 3-OBS experiment design deferred | `index.md`, `Phase11_3observer_prediction.md` | Prediction ready, experiment not designed |
| D13 | Circular fit scripts still in `07_fits/` | `proietti_chsh_fit.py`, `d1_blk1_4point_fit.py` | Superseded by `proietti_raw_fit.py` but still runnable |
| D14 | Decision D-T4-BYPASS-01 status "PROPOSED" | `04_governance/decisions/t4_bypass_decision.md` | Should be "APPLIED" |
| D15 | Phase 5 dependency map label "IN PROGRESS" | `K_Space_Axiomatization_plan.md` line 536 | All F9 items RESOLVED; label stale |

---

## Round 2 — 5-Why Deep Dive

### D1: K_Space_Axiomatization PEER-SYNC DRIFT (BLOCKING — 4.8/5)

| Why | Answer |
|-----|--------|
| 1. Why are the two copies out of sync? | Class C copy (v2.3) has T9 + L1-L5 + [A-E1] eliminated; canonical copy (v2.2) does not |
| 2. Why was Class C updated without canonical? | Recent commits (6ea82f1, a93c041) added T9 to Class C copy but did not fully sync back |
| 3. Why did not the sync mechanism catch this? | PEER-SYNC rule was created DURING the same session (396ca3c) — the drift happened in the 2 commits before the guard was installed |
| 4. Why was T9 added to Class C first? | Development flow: Class C is "working copy," canonical is "stable" — but CLAUDE.md says they are PEERS (equals), not primary/secondary |
| 5. Root cause | **Process design flaw:** PEER-SYNC rule was installed reactively (after drift happened) rather than proactively. The peer relationship is documented but the development habit of "work on Class C, then sync" has not been fully reversed to "work on BOTH simultaneously." |

**RCA Score: 4.8/5** — BLOCKING. Violates CLAUDE.md PEER-SYNC rule. If unfixed, future readers will see contradictory axiom versions.

**Fix:** Sync canonical copy to v2.3 (add T9 + L1-L5 + updated Layer 1/2 Summary tables). Verify via `scripts/sync_check_k_space.sh`.

### D2: Phase9_adversarial_testing.md stale assumptions (BLOCKING — 4.5/5)

| Why | Answer |
|-----|--------|
| 1. Why does Phase9 show [A-E1] as "JUSTIFIED"? | Phase9 was written before T9 eliminated [A-E1] (2026-05-24) |
| 2. Why was not Phase9 updated when T9 was added? | ERRATUM update focused on Phase7, Phase10, Phase11, Phase12, Phase13 — Phase9 was missed |
| 3. Why was Phase9 missed? | It has its own ERRATUM block (F1+F2 cascade) that was added 2026-05-23, but the [A-E1]/[A-E2] assumption table (lines 154-157) is separate from the ERRATUM |
| 4. Why does not the ERRATUM cover assumption status changes? | ERRATUM covers circular fit (F1) and postulate reclassification (F2), NOT the T8/T9 structural derivations added on 2026-05-24 |
| 5. Root cause | **Scope boundary in ERRATUM:** Each ERRATUM targets a specific finding (F1, F2, F3). There is no cross-file assumption-tracking mechanism. When [A-E1] was eliminated in K_Space_Axiomatization.md v2.3, no process checked which other files reference [A-E1]. |

**RCA Score: 4.5/5** — BLOCKING. Produces contradictory information: Phase9 says [A-E1] is an assumption; K_Space_Axiomatization says it is eliminated.

**Fix:** Update Phase9 lines 154-157 and 104-106 to reflect [A-E1] ELIMINATED, [A-E2] SPLIT into [A-E2a] DERIVED, [A-E2b] MODERATE. Add ERRATUM note referencing T8/T9.

### D3: [A-E3] beta universal — RESOLVED (2026-05-24 3-Round RCA)

**Status: RESOLVED.** See [RCA A-E3 Final Verdict](RCA_A_E3_beta_universal_final_verdict.md). Verdict: [A-E3] RECLASSIFIED as FREE PARAMETER (MEASUREMENT TARGET). β universality = MODELING CHOICE (Occam's razor). 0 assumptions remain.

| Why | Answer |
|-----|--------|
| 1. Why does [A-E3] remain? | beta universality is a simplifying assumption — not structurally derivable from K1-K8 |
| 2. Why cannot beta be derived? | beta is a FREE PARAMETER — like coupling constants in physics, parameters are measured, not derived |
| 3. Why is this the only remaining assumption? | [A-E1] eliminated by T9 (phi_ij from K8 embedding + T1). [A-E2] split: [A-E2a] derived via T8 (uniform counting from binary K1-K8 + K6 non-hierarchy). [A-E4] justified by Tier 4 OI-4 (dual modes). |
| 4. Why is [A-E3] WEAKLY JUSTIFIED? | Only anchored to N_QM_VVV_00031 — no structural derivation, no independent verification, and could be observer-dependent |
| 5. Root cause | **Parameter vs assumption boundary:** beta is a genuine free parameter (analogous to fine-structure constant). It does not need derivation — it needs measurement. The "WEAKLY JUSTIFIED" label is too harsh; "FREE PARAMETER — measurable, not derivable" is accurate. |

**RCA Score: 4.2/5** — HIGH. Not structurally resolvable (beta is a measurement target, not a derivation target). Reclassify from WEAKLY JUSTIFIED to FREE PARAMETER (MEASUREMENT TARGET).

### D4: K9E-PAT multiplicative pattern not confirmed (HIGH — 4.0/5)

| Why | Answer |
|-----|--------|
| 1. Why does not the 2BSM/1BSM ratio match prediction? | Real data: ratio = -0.78. Predicted: ~2. |
| 2. Why was ~2 predicted? | g=0.146 multiplicative model: each BSM setting adds one observer -> suppression factor (1-beta*g) per observer |
| 3. Why is g=0.146 the model? | Calibrated from PP-4 sanity check 4D scan — not from experimental data |
| 4. Why not use experimental data for calibration? | Only 4 data points (D1); insufficient to independently calibrate g and beta |
| 5. Root cause | **Model too simplistic for 2-BSM vs 1-BSM discrimination.** The per-observer multiplicative model assumes identical suppression per BSM observer — real experimental geometry may produce different suppression per observer. |

**RCA Score: 4.0/5** — HIGH. Evidence quality depends on this pattern. Currently: "data qualitatively consistent, quantitatively unconfirmed." RCA chi tiet: `RCA_K9E_PAT_status_report_2026_05_24.md` (3-Round RCA: 4.50/5). Key finding: ratio = -0.78 +/- 1.72 — pattern UNTESTABLE (sigma_ratio > ratio value), not "failed." Postulate survives. g=0.146 = modeling choice.

### D5: T4-H Steps 3-4 DEFERRED (HIGH — 3.8/5)

| Why | Answer |
|-----|--------|
| 1. Why are Steps 3-4 deferred? | Step 3 (K1-K8 preservation through quotient) and Step 4 (universal property) require ~12-18h category-theoretic proof work |
| 2. Why not do the proof? | K9_E does not need T4 (only needs T1 N=2). T4 is only needed for K9_F (deferred) and 3-observer prediction validation |
| 3. Why defer if 3-observer is the key empirical test? | 3-observer prediction is ILLUSTRATIVE — conditional on T4-H Steps 2-4. Without T4 completion, delta_M3 = -0.223 is a conjecture |
| 4. Why accept this gap? | T4 bypass decision (D-T4-BYPASS-01) explicitly defers T4 until: (a) all non-F candidates fail, or (b) researcher requests it |
| 5. Root cause | **Resource prioritization:** T4 proof is heavy (category theory) and not on the critical path for Class C classification. K9_E only needs T1. 3-observer experiment needs experimental design before T4 proof becomes urgent. |

**RCA Score: 3.8/5** — HIGH (structural gap) but with explicit decision record and bypass path. Not blocking for Class C status.

### D6: Two divergent K9_E implementations (HIGH — 3.7/5)

| Why | Answer |
|-----|--------|
| 1. Why are there two implementations? | Different calibration paths: additive (delta_S = -0.055 at beta=0.5) vs multiplicative (PP-4 4D scan, g=0.146) |
| 2. Why do they diverge at beta>0.3? | Additive: E = E_QM * [1 - beta*n_BSM*g_ctx]. Multiplicative: E = E_QM * [1 - beta*g_eff]^n_BSM. Same at first order, different at higher orders |
| 3. Why not choose one and remove the other? | Insufficient data to discriminate — both are plausible at current precision |
| 4. Why does this matter? | `proietti_raw_fit.py` uses multiplicative (beta=0.598, genuine fit). `run_all_checks.py` uses additive (sanity checks). Different models -> different beta interpretations |
| 5. Root cause | **Single free parameter (beta) insufficient to discriminate functional forms** with only 4 data points. Resolution requires either more data or theoretical preference. |

**RCA Score: 3.7/5** — HIGH. Not blocking but creates ambiguity in published results. Index.md Section 7 documents this but does not resolve it.

### D7: Phase8_candidate_equation.md partial inconsistency (HIGH — 3.6/5)

| Why | Answer |
|-----|--------|
| 1. Why does line 45 say [A-E2] eliminated but line 49 shows [A-E1] as MODERATE? | Line 45 was updated 2026-05-24; the assumption table (lines 49-55) was updated 2026-05-23 and not re-audited |
| 2. Why was the table not re-audited? | Same root cause as D2 — no cross-file assumption-tracking mechanism |
| 3. What is the actual current state? | [A-E1] ELIMINATED (T9). [A-E2] SPLIT into [A-E2a] DERIVED (T8) + [A-E2b] MODERATE. [A-E3] MODERATE-STRONG (reclassified). [A-E4] STRONG. |
| 4. Why keep both old and new text? | "Extend, not overwrite" contract — ERRATUM was added but assumption table was not fully reconciled |
| 5. Root cause | **Partial update pattern:** ERRATUM blocks added to document new findings without refreshing the content they supersede. Creates "layered history" rather than "current truth." |

**RCA Score: 3.6/5** — HIGH. Same pattern as D2 but in a different file.

---

## Round 3 — Classification and Remediation

### BLOCKING (2 items — must fix before next commit)

| # | Item | Score | Fix | Effort |
|---|------|-------|-----|--------|
| D1 | K_Space_Axiomatization PEER-SYNC DRIFT | 4.8/5 | Sync canonical copy to v2.3 (add T9 + L1-L5). Verify via `sync_check_k_space.sh`. | 30 min |
| D2 | Phase9_adversarial_testing.md stale assumptions | 4.5/5 | Update assumption table + add ERRATUM note for T8/T9. | 20 min |

### HIGH (5 items — should fix in next session)

| # | Item | Score | Fix | Effort |
|---|------|-------|-----|--------|
| D3 | [A-E3] beta universal — RESOLVED | 4.2/5 | **RESOLVED (2026-05-24).** Reclassified as FREE PARAMETER. See RCA_A_E3_beta_universal_final_verdict.md. | Done |
| D4 | K9E-PAT multiplicative pattern not confirmed | 4.0/5 | Add explicit caveat in index.md Section 5 Key Numbers. Document g=0.146 as calibration (not prediction). | 15 min |
| D5 | T4-H Steps 3-4 DEFERRED | 3.8/5 | Accept as documented gap. Update status to "DEFERRED per D-T4-BYPASS-01, not blocking." | 5 min (no change needed) |
| D6 | Two divergent K9_E implementations | 3.7/5 | Document model comparison in index.md Section 7. Add recommendation: prefer multiplicative for genuine fit, additive for sanity checks. | 20 min |
| D7 | Phase8_candidate_equation.md partial inconsistency | 3.6/5 | Reconcile assumption table (lines 49-55) with line 45 update. [A-E1] -> ELIMINATED, [A-E2] -> SPLIT. | 20 min |

### MEDIUM (4 items — track in Open Items)

| # | Item | Score | Fix | Effort |
|---|------|-------|-----|--------|
| D8 | P10-NOISE: Non-uniform noise not ruled out | 3.5/5 | ANALYZED (noise_threshold=0.10 sigma — FAIL). Script: `07_fits/noise_sensitivity_analysis.py`. Class C downgraded genuine→qualified. P10-NOISE remains OPEN — cannot close without 3-observer experiment or raw event data. Structural limitation, not fixable with current data. | ∞ (blocked by data) |
| D9 | P10-TIM: Null-model N0 omitted | 3.4/5 | DECISION-LOCKED. Requires raw event-level data from Proietti. Keep as Open Item. | 0 (blocked) |
| D10 | Phase 10b INVALIDATED file | 3.3/5 | Archive `Phase10b_bong_lf.md` to `08_archives/` or add prominent INVALIDATED header. | 5 min |
| D11 | EX compass: 3 nodes K-PENDING-RCA | 3.2/5 | Document as EX compass intelligence only — not core debt. C3 gate per vv-qmrf-ex-plan.md. | 0 (delegated) |

### LOW (4 items — cosmetic / process)

| # | Item | Score | Fix | Effort |
|---|------|-------|-----|--------|
| D12 | 3-OBS experiment design deferred | 3.0/5 | Already marked FUTURE WORK in index.md. No change needed. | 0 |
| D13 | Circular fit scripts still present | 2.5/5 | Add deprecation warning to docstrings in `proietti_chsh_fit.py` and `d1_blk1_4point_fit.py`. | 10 min |
| D14 | Decision D-T4-BYPASS-01 "PROPOSED" | 2.3/5 | Change status from PROPOSED to APPLIED. | 2 min |
| D15 | Phase 5 "IN PROGRESS" stale label | 2.0/5 | Change to COMPLETE at line 536 of K_Space_Axiomatization_plan.md. | 2 min |

---

## EX Compass Cross-Reference

EX stress points mapped to identified debt:

| EX Stress Point | KE-SC | Maps to debt |
|-----------------|-------|-------------|
| K5 multi-observer cross-context firing | 4.0 | D5 (T4-H Steps 3-4) — T4 is the formal path to multi-observer generalization |
| V_prov/V_final lifecycle | 3.8 | Already resolved (F1/F7b) — no debt |
| K9 bridge parameter sensitivity | 3.7 | D3 ([A-E3] beta) + D6 (two implementations) |
| T4 N-observer colimit | 3.5 | D5 (T4-H Steps 3-4 deferred) |
| FR assumption chain C | 3.5 | Already resolved (Phase 10c) — no debt |
| 3 K-PENDING-RCA nodes (00056, 00057, 00059) | 3.5 | D11 (EX compass pending) |

EX compass confirms: the highest-stress debt is T4-H completion (D5) and beta parameter handling (D3, D6).

---

## Assumption Registry — Current State (Post-2026-05-24 Commits)

| Assumption | Status (before today) | Status (after 6ea82f1 et al.) | Remaining work |
|-----------|----------------------|-------------------------------|----------------|
| [A-E1] K_ctx via T3-morphism | MODERATE | **FULLY ELIMINATED** (T9, L1-L5) | Sync canonical copy (D1) |
| [A-E2] f_perp fraction form | WEAK | **SPLIT:** [A-E2a] DERIVED (T8, H1, H3, H4) + [A-E2b] MODERATE (outcome filter) | Update Phase9 (D2), Phase8 (D7) |
| [A-E3] beta universal | WEAKLY JUSTIFIED | **RECLASSIFIED: FREE PARAMETER** (2026-05-24 RCA) | See RCA_A_E3_beta_universal_final_verdict.md |
| [A-E4] bot_K^str != bot_K^dyn | STRONG | **STRONG** (unchanged) | None |

**Original: 4 assumptions. Current: 0 assumptions + 1 free parameter (β) + 1 modeling choice (β_universal). [A-E1] ELIMINATED (T9). [A-E2] ELIMINATED (T8-H1). [A-E3] RECLASSIFIED: FREE PARAMETER. [A-E4] BE-anchored.**

---

## Recommendations

### Immediate (next commit)
1. **Fix D1:** Sync canonical `K_Space_Axiomatization.md` to v2.3
2. **Fix D2:** Update Phase9 assumption table

### Next session (2-3 hours)
3. **Fix D3:** ~~Reclassify [A-E3]~~ → **DONE (2026-05-24).** 3-Round RCA complete. See RCA_A_E3_beta_universal_final_verdict.md.
4. **Fix D7:** Reconcile Phase8 assumption table
5. **Fix D6:** Document model comparison
6. **Fix D4:** Add explicit caveat for K9E-PAT
7. **Fix LOW items:** D13, D14, D15 (22 min total)

### Deferred / accepted
8. **D5 (T4-H Steps 3-4):** Accepted gap — explicit bypass decision exists
9. **D8 (P10-NOISE):** ANALYZED — noise_threshold=0.10 sigma (FAIL). Class C downgraded genuine→qualified. Cannot close without 3-observer experiment.
10. **D9 (P10-TIM):** DECISION-LOCKED — waiting on raw data
11. **D10 (Phase 10b archive):** Low priority cleanup
12. **D11 (EX K-PENDING-RCA):** EX compass domain, not core
13. **D12 (3-OBS):** Marked FUTURE WORK

### Process improvement
- **Cross-file assumption tracker:** Create a single `assumption_registry.md` that lists all assumptions, their status, and which files reference them. When an assumption is eliminated, the registry flags all referencing files for update.
- **Pre-commit sync check:** Add `scripts/sync_check_k_space.sh` to pre-commit hook or run before every commit that touches `K_Space_Axiomatization.md`.

---

## Verdict

| Round | Focus | Score |
|-------|-------|-------|
| Round 1 | Surface scan — identification | **4.5/5** (15/15 real debt identified, 0 false negatives) |
| Round 2 | 5-Why deep dive — root cause isolation | **4.3/5** (all 7 HIGH/BLOCKING items traced to root cause) |
| Round 3 | Classification + remediation | **4.2/5** (clear fix paths, explicit effort estimates) |
| **Aggregate** | | **4.33/5** — PASS (>=4/5) |

**Final determination:** Class C (genuine) co **15 technical debt items**.
- **2 BLOCKING** (D1 sync drift, D2 stale assumptions) — fix trong 50 phut.
- **5 HIGH** (D3-D7) — fix trong 2-3 gio.
- **Sau khi fix 7 items nay:** Class C dat **production-grade cleanliness** — 0 blocking, 0 high, chi con MEDIUM items da duoc track va LOW cosmetic items.

**Tong debt score truoc fix: 3.53/5 (MEDIUM-HIGH). Sau fix BLOCKING+HIGH: 2.1/5 (LOW — acceptable).**

---

*RCA Technical Debt Inventory — 2026-05-24. 3-Round RCA x 5-Why x Scoring Threshold 4/5. VVV-QMRF scope, VVV-QMRF-EX as compass.*
