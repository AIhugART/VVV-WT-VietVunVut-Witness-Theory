Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Session Report — P10-NOISE Resolution + Class C Downgrade

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Trigger:** RCA P10-NOISE status report (4.67/5) → mandatory noise sensitivity analysis

---

## Session Summary

| Metric | Value |
|--------|-------|
| **Task** | RCA giai quyet P10-NOISE: methodology decision → implementation → execution → downgrade |
| **Files created** | 4 |
| **Files modified** | 4 |
| **Total 3-Round RCAs** | 2 (methodology: 4.77/5 + status: 4.67/5) |
| **Key decision** | Class C downgrade: genuine → qualified (noise_threshold = 0.10 sigma RMS) |

---

## Deliverables

### RCA Documents (2)

| # | File | Type | Score | Key Finding |
|---|------|------|-------|-------------|
| 1 | `04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md` | 3-Round RCA | **4.77/5** | Delta_chi2 Decomposition + Noise Budget Analysis. Conservative, simple, data-minimal. |
| 2 | `RCA_session_P10_NOISE_resolution_2026_05_24.md` | Session report | — | This file |

### Implementation (2)

| # | File | Type | Purpose |
|---|------|------|---------|
| 3 | `07_fits/noise_sensitivity_analysis_spec.md` | Specification | 4-step methodology (B1-B4), PASS/AMBIGUOUS/FAIL criteria |
| 4 | `07_fits/noise_sensitivity_analysis.py` | Python script | Executable noise budget analysis |

### System Updates (4)

| # | File | Change |
|---|------|--------|
| 5 | `index.md` (Class C) | v30: status genuine→qualified, boundary statement, noise results in Key Numbers, run order updated |
| 6 | `00_top_10_hallucinations_record.md` | P10-NOISE: status→ANALYZED-FAIL, root cause→Structural Limitation, solution→DONE |
| 7 | `rca_technical_debt_inventory_2026_05_24.md` | D8: effort 1-2hr→∞(blocked by data), Class C downgraded |
| 8 | `anti_hallucinations/index.md` | File map updated with 4 new entries |

---

## Analysis Results

### B1: Delta_chi2 Decomposition

| Setting | delta_chi2 | % of total |
|---------|------------|------------|
| A0B0 | +4.2788 | **80.0%** |
| A0B1 | +0.1169 | 2.2% |
| A1B0 | +0.0361 | 0.7% |
| A1B1 | +0.9149 | 17.1% |
| **Total** | **+5.3467** | **100%** |

A0B0 alone drives 80% of K9_E "advantage."

### B2: Single-Setting Fragility

| Setting | Threshold |
|---------|-----------|
| A0B0 | **1.85 sigma** |
| A1B1 | 1.85 sigma |
| A0B1 | >8 sigma (robust) |
| A1B0 | >8 sigma (robust) |

### B3: Worst-Case Noise Pattern

- Noise mimics K9_E multiplicative pattern: 2BSM/1BSM ratio = 1.58 (K9_E predicts ~2)
- Delta_chi2 with worst-case noise = 36.46 (7x the original "signal")

### B4: Noise Threshold (Monte Carlo)

- **noise_threshold (2-sigma) = 0.10 sigma RMS** (PASS requires > 3.0, FAIL < 1.0)
- At ALL RMS levels (0.5–5.0), ~50% of random noise vectors produce Delta_chi2 >= 5.35
- g_eff sensitivity: threshold stable at 0.20 sigma RMS across g_eff in [0.05, 0.29]

### Root Cause Insight

K9_E has directional sensitivity (only captures suppression, beta >= 0). Random noise is symmetric → ~50% of realizations have a suppression-like component. With 4 data points and 2 parameters (vs QM's 1), K9_E captures this component and reports Delta_chi2 > 0. **The 2.31sigma from profile likelihood is misleading** — it assumes chi-squared(1) null distribution, but with 4 data points and a bounded parameter [0, 0.99], the actual null distribution is very different.

---

## 3-Round RCA Summary

### RCA 1: P10-NOISE Status (prior session, committed as 7b5a8be)

| Round | Focus | Score |
|-------|-------|-------|
| R1 | Status Assessment — data-availability gap | 4.5/5 |
| R2 | Impact Assessment — single-point-of-failure | 4.8/5 |
| R3 | Decision — BLOCKING GATE, 3 mandatory actions | 4.7/5 |
| **Aggregate** | | **4.67/5** |

### RCA 2: Methodology Decision (this session)

| Round | Focus | Score |
|-------|-------|-------|
| R1 | Status — underdetermination from 4 data points | 4.6/5 |
| R2 | Impact — Type I error = FATAL, conservative principle | 4.9/5 |
| R3 | Decision — Delta_chi2 Decomposition + Noise Budget | 4.8/5 |
| **Aggregate** | | **4.77/5** |

### RCA 3: Execution Verdict (implicit — from analysis results)

| Criterion | Value | Threshold | Verdict |
|-----------|-------|-----------|---------|
| noise_threshold | 0.10 sigma | > 3.0 (PASS) | **FAIL** |
| Most fragile setting | A0B0: 1.85 sigma | — | Single data point drives 80% of signal |
| Noise pattern match | YES (ratio=1.58 vs 2) | — | Noise can mimic K9_E |
| Monte Carlo fraction | ~50% at all RMS | < 5% would indicate robustness | **FAIL** |

---

## Decision: Class C Downgrade

```
Class C (genuine) → Class C (qualified)

Reason:  Noise sensitivity analysis FAIL.
         noise_threshold = 0.10 sigma RMS << 1.0 FAIL threshold.
         K9_E empirical evidence NOT robust to noise.

Status:  Class C (qualified) — structurally testable,
         empirically UNCONFIRMED (noise not ruled out).

Remaining empirical path:
         3-observer experiment with dedicated noise characterization.
         delta_M3 = -0.223 at beta=0.3 (illustrative, T4-H Steps 2-4 needed).
```

---

## P10-NOISE Status: Post-Resolution

| Attribute | Before | After |
|-----------|--------|-------|
| Status | OPEN — BLOCKING GATE | ANALYZED — FAIL (cannot close) |
| Root cause | Type 3 (Broken Trace) | Type 4 (Structural Limitation) |
| Hallucination | "chua duoc kiem tra" | DA XAC NHAN: noise CO THE giai thich |
| Risk Score | 18.0 (HIGH) | 18.0 (HIGH) — unchanged |
| Deadline | P1 (truoc public) | BLOCKED (khong co data) |
| Fixable? | Yes — noise analysis | No — only 3-observer experiment or raw data |

---

## File Inventory

```
NEW (4):
  project_vvv_qmrf_class_c/04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md
  project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis_spec.md
  project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis.py
  anti_hallucinations/RCA_session_P10_NOISE_resolution_2026_05_24.md

MODIFIED (4):
  project_vvv_qmrf_class_c/index.md                              (v30 downgrade)
  anti_hallucinations/00_top_10_hallucinations_record.md         (P10-NOISE update)
  project_vvv_qmrf_class_c/04_governance/rca_technical_debt_inventory_2026_05_24.md  (D8)
  anti_hallucinations/index.md                                   (file map)
```

---

## Next Steps

1. **3-observer experiment design** — only path to close P10-NOISE
2. **T4-H Steps 2-4** — colimit construction needed before 3-observer prediction is validated
3. **Track Proietti raw data availability** — if raw event data becomes available, re-run noise correlation analysis
4. **K9_E structural leg remains intact** — K1-K8 motivation, FR avoidance, 4/4 adversarial tests unaffected by noise

---

*RCA Session Report — P10-NOISE Resolution + Class C Downgrade. 2026-05-24. VVV-QMRF scope, VVV-QMRF-EX as compass.*
