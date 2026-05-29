# RCA Round 1 — Empirical Evidence: Genuine Non-Circular Fit
# 3-Round RCA x 5-Why x Scoring Threshold 4/5
# VVV-QMRF scope, VVV-QMRF-EX as compass

**Date:** 2026-05-23
**Input:** Raw Proietti Figure 3 correlator data from `Wigner_figure_3.md`
**Script:** `07_fits/proietti_raw_fit.py`
**Contrast:** Circular fit (`d1_blk1_4point_fit.py`) used reconstructed data E_exp = V_exp * E_QM

---

## 1. Define — What Changed?

**Symptom (circular fit):** beta=0 best-fit, PATH A beta<=0.175 — tautology.
**Cause:** Data was reconstructed as E_exp = V_exp * E_QM. K9_E at beta=0 = QM. Fit guaranteed beta=0.

**Genuine fit:** Uses raw correlator values extracted from Proietti Figure 3 PDF.

---

## 2. Raw Data vs Reconstructed Data

| Correlator | Raw (Figure 3) | Reconstructed (V*QM) | Difference |
|---|---|---|---|
| A0B0 (0 BSM) | -0.678 +/- 0.033 | -0.604 | +0.074 (12.2%) |
| A0B1 (1 BSM) | 0.570 +/- 0.040 | +0.604 | -0.034 (5.6%) |
| A1B0 (1 BSM) | 0.595 +/- 0.041 | +0.604 | -0.009 (1.5%) |
| A1B1 (2 BSM) | 0.571 +/- 0.034 | +0.604 | -0.033 (5.5%) |

S_raw = 2.414 vs S_paper = 2.416 — confirmed (delta = 0.002 from rounding).

---

## 3. Genuine Fit Results

### Model
E_pred(A_x,B_y; V, beta) = V * E_QM(x,y) * (1 - beta * g)^(n_BSM)
g = 0.146 (effective f_perp per observer)
n_BSM = x + y (number of BSM measurement settings)
Free: V (visibility), beta (K9_E suppression)
DOF = 4 - 2 = 2

### Best-fit

| Parameter | Value |
|-----------|-------|
| V (visibility) | 0.9387 |
| beta (K9_E suppression) | 0.598 |
| chi2_min | 1.340 |
| chi2/DOF | 0.670 |
| p-value | 0.512 |

### Per-setting residuals

| Setting | n_BSM | E_raw | E_pred | Residual | Res/sigma |
|---------|-------|-------|--------|----------|-----------|
| A0B0 | 0 | -0.678 | -0.664 | -0.014 | -0.43 |
| A0B1 | 1 | +0.570 | +0.606 | -0.036 | -0.89 |
| A1B0 | 1 | +0.595 | +0.606 | -0.011 | -0.26 |
| A1B1 | 2 | +0.571 | +0.553 | +0.018 | +0.54 |

### QM-only comparison (beta=0, V free)

| Model | V | chi2 | DOF | chi2/DOF |
|-------|---|------|-----|----------|
| QM-only | 0.860 | 6.687 | 3 | 2.229 |
| K9_E | 0.939 | 1.340 | 2 | 0.670 |

Delta_chi2 = 5.347 (2.31 sigma) — K9_E improves fit over QM-only.

---

## 4. 5-Why Trace

1. Why does K9_E improve fit over QM? → Raw data shows non-uniform visibility: (0,0) setting has V ~ 0.959, while BSM settings have lower effective visibility.
2. Why is visibility non-uniform? → Three possibilities: (a) K9_E suppression (beta > 0), (b) experimental imperfections vary by setting, (c) statistical fluctuation.
3. Why can't we distinguish (a) from (b)? → K9_E's specific pattern (2BSM/1BSM ratio ~ 2, negative residuals at BSM) is NOT confirmed. Ratio = -0.78, and (1,1) residual is POSITIVE (+0.018).
4. Why doesn't the K9_E pattern match? → Either: K9_E's multiplicative model (g=0.146, product form) is wrong; or experimental systematics dominate; or 4 data points insufficient.
5. Root cause: Data shows non-uniform visibility (qualitatively consistent with K9_E direction), but the specific K9_E multiplicative pattern is not confirmed. With 4 data points and unknown experimental systematics, K9_E cannot be uniquely identified as the source.

---

## 5. Isolate

Gap: K9_E's prediction is DIRECTIONALLY correct (0-BSM less suppressed than BSM) but the MAGNITUDE pattern (multiplicative, 2BSM ~ 2x 1BSM) does not match.

Source: The g=0.146 model may be too simplistic. Actual f_perp depends on detailed quantum mechanical overlap calculations per BSM outcome pair.

---

## 6. Score

| Criterion | Score | Notes |
|-----------|-------|-------|
| Data authenticity | 5.0/5 | Raw Figure 3 values, SOT verified against main.tex |
| Non-circularity | 5.0/5 | No reconstructed data; genuine empirical fit |
| Fit quality | 4.0/5 | chi2/DOF=0.67, p=0.51 — good fit, K9_E pattern not confirmed |
| Distinguishability from QM | 3.5/5 | Delta_chi2=5.35 (2.31sigma) favors K9_E, but pattern fails |
| Alternative explanations | 2.5/5 | Non-uniform experimental noise cannot be ruled out |
| **Round 1 Score** | **4.00/5** | **PASS (threshold 3.5/5)** |

---

## 7. Verdict

Genuine empirical evidence now EXISTS. The circular fit has been replaced. Raw data shows K9_E is DIRECTIONALLY favored over QM-uniform-visibility (2.31sigma), but the specific K9_E multiplicative pattern is NOT confirmed. The evidence is REAL but AMBIGUOUS — K9_E is one possible explanation for non-uniform visibility, but experimental systematics are another.

This is a genuine empirical result, not a tautology. Score 4.00/5 passes the 3.5/5 threshold for Condition 1.

---

*RCA Round 1 — 2026-05-23. VVV-QMRF scope, VVV-QMRF-EX as compass.*
