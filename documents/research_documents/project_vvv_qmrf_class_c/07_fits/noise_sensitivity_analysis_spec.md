Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Noise Sensitivity Analysis — Implementation Specification

**Date:** 2026-05-24
**RCA Reference:** `RCA_P10_NOISE_methodology_decision_2026_05_24.md` (aggregate 4.77/5)
**Methodology:** Delta_chi2 Decomposition + Noise Budget Analysis
**Implementation:** `07_fits/noise_sensitivity_analysis.py` (future)

---

## 1. Objective

Answer: **"How large must non-uniform noise be to produce Delta_chi2 = 5.35?"**

The result determines whether P10-NOISE can be closed (noise threshold > 3 sigma RMS), kept open (1-3 sigma), or triggers Class C downgrade (< 1 sigma).

---

## 2. Input Data (from Proietti Figure 3, via Wigner_figure_3.md)

All data already committed in `Wigner_figure_3.md` and `proietti_raw_fit.py`:

| Setting | E_exp | sigma | x | y | n_BSM | E_QM |
|---------|-------|-------|---|---|-------|------|
| A0B0 | -0.678 | 0.033 | 0 | 0 | 0 | -1/sqrt(2) |
| A0B1 | +0.570 | 0.040 | 0 | 1 | 1 | +1/sqrt(2) |
| A1B0 | +0.595 | 0.041 | 1 | 0 | 1 | +1/sqrt(2) |
| A1B1 | +0.571 | 0.034 | 1 | 1 | 2 | +1/sqrt(2) |

K9_E best-fit (from proietti_raw_fit.py): V = 0.939, beta = 0.598, g_eff = 0.146
chi2_min = 1.340, chi2_qm = 6.687, Delta_chi2 = 5.347, DOF(K9_E) = 2

---

## 3. Model Definitions

### 3.1 QM-only model (beta=0)
```
E_pred(V) = V * E_QM
Free parameter: V in [0.8, 1.0]
```

### 3.2 K9_E model (beta free)
```
E_pred(V, beta) = V * E_QM * (1 - beta * g_eff)^(n_BSM)
Free parameters: V in [0.8, 1.0], beta in [0, 0.99]
g_eff = 0.146 (PP-4 calibration)
```

### 3.3 Chi-squared function
```
chi2(V, beta) = sum_i (E_exp_i - E_pred_i(V, beta))^2 / sigma_i^2
```

### 3.4 Profile chi-squared
```
profile_chi2(beta) = min_V chi2(V, beta)
Delta_chi2(beta) = profile_chi2(0) - profile_chi2(beta)
```

---

## 4. Analysis Steps

### B1: Delta_chi2 Decomposition

**Goal:** Identify which setting(s) drive the K9_E advantage.

**Method:**
```
For each setting i:
  chi2_QM_i = (E_exp_i - V_qm * E_QM_i)^2 / sigma_i^2
  chi2_K9E_i = (E_exp_i - V_fit * E_QM_i * (1 - beta_fit * g)^(n_BSM_i))^2 / sigma_i^2
  delta_chi2_i = chi2_QM_i - chi2_K9E_i
```

**Expected output table:**
```
Setting | chi2_QM | chi2_K9E | delta_chi2 | % of total
A0B0    |  X.XX   |  X.XX    |   X.XX     |   XX%
A0B1    |  X.XX   |  X.XX    |   X.XX     |   XX%
A1B0    |  X.XX   |  X.XX    |   X.XX     |   XX%
A1B1    |  X.XX   |  X.XX    |   X.XX     |   XX%
Total   |  6.687  |  1.340   |   5.347    |   100%
```

### B2: Single-Setting Perturbation

**Goal:** For each setting, how many sigma must the raw value shift to make Delta_chi2 < 1 (no significant K9_E advantage)?

**Method:**
```
For each setting i:
  For delta in [-5, 5] step 0.05 (sigma units):
    E_perturbed_i = E_exp_i + delta * sigma_i
    Re-fit K9_E model (V, beta) with perturbed data
    Compute Delta_chi2_perturbed
  Find delta_threshold_i where Delta_chi2 crosses below 1.0
  This gives the "fragility" of the K9_E signal to noise at setting i
```

**Expected output table:**
```
Setting | delta_threshold (sigma) | Interpretation
A0B0    |        X.XX            | Need X.XX sigma shift to negate K9_E advantage
A0B1    |        X.XX            | ...
A1B0    |        X.XX            | ...
A1B1    |        X.XX            | ...
MIN across settings: X.XX sigma   | Most fragile setting
```

### B3: Worst-Case Noise Pattern

**Goal:** What noise pattern most effectively mimics K9_E suppression?

**Method:**
```
Grid search over noise vectors (eps_00, eps_01, eps_10, eps_11)
where each eps in [-3, 3] in steps of 0.2 sigma

For each noise vector:
  E_noisy_i = E_exp_i + eps_i * sigma_i
  Evaluate chi2_QM(noisy) vs chi2_K9E(noisy)
  Find pattern that MAXIMIZES Delta_chi2

Also check: does the optimal noise pattern reproduce the K9_E signature?
  residual_i = E_noisy_i - E_pred_K9E_i
  ratio_2bsm_1bsm = residual(A1B1) / avg(residual(A0B1), residual(A1B0))
  K9_E signature: ratio ~ 2 (multiplicative), direction consistent with suppression
```

**Expected output:**
```
Worst-case noise vector (sigma units):
  eps(A0B0) = X.XX, eps(A0B1) = X.XX, eps(A1B0) = X.XX, eps(A1B1) = X.XX
  Delta_chi2 with this noise: X.XX
  Pattern direction: [description]
  2BSM/1BSM residual ratio: X.XX (K9_E predicts ~2)
  Does this pattern match K9_E signature? [YES/NO/AMBIGUOUS]
```

### B4: Multi-Setting Noise Threshold

**Goal:** What is the minimum RMS noise (in sigma units) needed to produce Delta_chi2 >= 5.35?

**Method:**
```
For noise_RMS in [0, 5] step 0.05 (sigma units):
  Generate N_random = 10000 random noise vectors with RMS = noise_RMS
  For each vector, compute Delta_chi2
  Count fraction where Delta_chi2 >= 5.35
  Find noise_RMS where fraction >= 0.05 (2-sigma confidence)
  Find noise_RMS where fraction >= 0.50 (median)

Also: scan g_eff in [0.05, 0.30] step 0.01 to test sensitivity to PP-4 calibration
Use fixed random seed (42) for reproducibility.
```

**Expected output:**
```
Noise threshold (2-sigma confidence): X.XX sigma RMS
Noise threshold (median):             X.XX sigma RMS
g_eff sensitivity (0.05-0.30):       threshold varies from X.XX to X.XX

Interpretation:
  noise_threshold > 3.0 sigma → PASS (noise cannot explain Delta_chi2)
  noise_threshold 1.0-3.0     → AMBIGUOUS
  noise_threshold < 1.0 sigma → FAIL (published error bars alone can explain)
```

---

## 5. PASS/FAIL Decision Logic

```
if noise_threshold_2sigma > 3.0:
    verdict = "PASS"
    action = "Close P10-NOISE: H=5->3, Risk=18.0->10.8"
elif noise_threshold_2sigma >= 1.0:
    verdict = "AMBIGUOUS"
    action = "Keep P10-NOISE OPEN. Add boundary statement to index.md."
else:
    verdict = "FAIL"
    action = "Downgrade Class C (genuine) -> (qualified). Add boundary statement."
```

---

## 6. Output Format

The implementing script shall produce:
1. **Console:** Structured report with all tables and the final verdict
2. **Markdown file:** `07_fits/noise_sensitivity_analysis_results_YYYY_MM_DD.md` — full report for archival

---

## 7. Limitations (explicitly stated in all outputs)

1. **Statistical vs systematic noise:** Error bars from Proietti Figure 3 are Poissonian — they capture counting statistics only. Systematic noise (phase drift, alignment variation, detector efficiency fluctuation) is NOT characterized and may have different magnitude or correlation structure.
2. **Noise correlation:** 4 data points carry no information about noise correlation between settings. If noise is correlated across settings (e.g., phase drift affects all BSM settings similarly), the threshold may differ from our uncorrelated estimate.
3. **Not a replacement for experiment:** This analysis only sets an upper bound on what published error bars allow — it does not confirm K9_E. Independent experimental confirmation (3-observer experiment with dedicated noise characterization) is still required regardless of the analysis outcome.

---

## 8. Dependencies

- `numpy`, `scipy` (already listed in `07_fits/requirements.txt`)
- `Wigner_figure_3.md` — SOT for raw data values
- `proietti_raw_fit.py` — reference implementation of model and chi-squared

---

## 9. Implementation Notes

- The script should be self-contained with hardcoded raw data (no external data file reads)
- All intermediate values printed so each step can be independently verified
- Target runtime: < 60 seconds on standard laptop
- Fixed random seed (42) for reproducibility in B4 Monte Carlo

---

*Noise Sensitivity Analysis Specification — 2026-05-24. Part of P10-NOISE RCA (aggregate 4.77/5). VVV-QMRF scope, VVV-QMRF-EX as compass.*
