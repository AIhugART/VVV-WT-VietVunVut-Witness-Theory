# K9-S11d: Statistical Significance Analysis
# 3-Round RCA x 5-Why x Scoring Threshold 4/5
# With VVV-QMRF-EX as Compass

**Step:** K9-S11d (Statistical Significance — Foundation Validation)
**Date:** 2026-05-23
**Input:** K9-S11c (Universal Theorem + LF Compatibility)

---

## CRITICAL SELF-CORRECTIONS OF K9-S11c

> **K9-S11c was WRONG about α=45° being the "sweet spot."**
>
> At α=45°, μ=0.95:
>   Gen LF 1 = +0.022, σ(S_LF1) = 0.012 → **1.9σ**
>   This is NOT statistically significant. 3σ requires 236,589 coincidences (2.6× Bong).
>
> **K9-S11c also used a meaningless "signal" metric.**
>   "K9_E signal = 0.707" was |cos(α)| = f_perp outcome-dependence.
>   This is NOT a measurable quantity. The actual measurable is δ⟨A_xB_y⟩.

---

## Q1: Is +0.022 LF violation statistically significant?

**Answer: NO.**

| α (deg) | S_LF1 | σ(S_LF1) | Significance | Status |
|---|---|---|---|---|
| 30 | +0.061 | 0.010 | **5.9σ** | ✅ significant |
| 31 | +0.062 | 0.010 | **6.0σ** | ✅ significant |
| 35 | +0.062 | 0.011 | **5.7σ** | ✅ significant |
| 40 | +0.051 | 0.012 | **4.4σ** | ✅ significant |
| **45** | **+0.022** | **0.012** | **1.9σ** | ❌ NOT significant |
| 47 | +0.005 | 0.012 | 0.4σ | ❌ NOT significant |

**5-Why: Why was α=45° chosen as "sweet spot"?**
1. K9-S11c maximized the K9_E "signal" |cos(α)| while keeping LF violated
2. But |cos(α)| is not the right metric — the actual measurable δ⟨A_xB_y⟩ matters
3. And "violated" without significance check is meaningless
4. σ(S_LF1) ≈ 0.012 because Gen LF 1 has 11 terms with coefficients up to ±2
5. The violation (+0.022) is smaller than σ → buried in noise

---

## Q2: Optimal α — Proper Figure of Merit

### Criterion
```
FOM = min(n_σ_LF, n_σ_K9E)

where:
  n_σ_LF  = S_LF1 / σ(S_LF1)     [significance of LF violation]
  n_σ_K9E = |δ⟨A₁B₂⟩| / σ(⟨A₁B₂⟩)  [significance of K9_E deviation]

Subject to: both > 3σ with N = 91,000 (Bong statistics)
```

### Results

| α (deg) | n_σ_LF | n_σ_K9E | FOM = min | Status |
|---|---|---|---|---|
| 27 | 5.7 | 18.9 | 5.7 | ✅ both >3σ |
| 30 | 5.9 | 20.4 | 5.9 | ✅ both >3σ |
| **31** | **6.0** | **20.8** | **6.0** | ✅ **OPTIMAL** |
| 33 | 5.9 | 21.6 | 5.9 | ✅ both >3σ |
| 35 | 5.7 | 22.4 | 5.7 | ✅ both >3σ |
| 40 | 4.4 | 23.8 | 4.4 | ✅ both >3σ |
| 42 | 3.5 | 24.1 | 3.5 | ✅ both >3σ |
| 45 | 1.9 | 24.5 | 1.9 | ❌ LF not significant |

### Answer: **α = 31° is optimal.** FOM = 6.0

At α=31°, μ=0.95, N=91,000:
- Gen LF 1 = **+0.062** at **6.0σ** significance
- δ⟨A₁B₂⟩ = **-0.0355** at **20.8σ** significance
- BOTH are above 3σ with Bong-level statistics

**5-Why: Why is α=31° better than α=45°?**
1. LF violation grows rapidly as α decreases (from +0.022 at 45° to +0.062 at 31°)
2. K9_E signal also strong (20.8σ) — barely reduced from 45° (24.5σ)
3. The bottleneck is LF, not K9_E — LF significance is ALWAYS the limiting factor
4. Maximizing FOM = min(LF, K9E) pushes toward smaller α
5. Below α=27°, LF significance starts dropping because the LF violation itself peaks

---

## Q3: K9_E Signal in Measurable Units

### Correction

The "0.707" from K9-S11c was |cos(α)| — a **dimensionless parameter**, not a measurable quantity.

### Actual Measurable: δ⟨A_xB_y⟩

At the optimal **α=31°**, μ=0.95:

| β_K9 | δ⟨A₁B₂⟩ | δ(%) | σ | Significance |
|---|---|---|---|---|
| 0.1 | -0.0114 | 1.3% | 0.0017 | 6.7σ |
| 0.3 | -0.0355 | 4.2% | 0.0017 | **20.8σ** |
| 0.5 | -0.0614 | 7.2% | 0.0017 | 36.0σ |

**For ALL testable correlators** (x=1,y≠1 and x≠1,y=1):
```
⟨A₁B₂⟩_QM  = -0.857
⟨A₁B₂⟩_K9E = -0.893  (at β_K9=0.3)
δ = -0.036  →  20.8σ with N=91,000
```

The K9_E effect shifts the correlator by **4.2%** — easily measurable even at β_K9=0.1 (6.7σ).

**5-Why: Why is K9_E so much more significant than LF?**
1. K9_E affects 4 correlators directly (mixed settings)
2. Each correlator has σ ≈ 0.0017 (very small for N=91,000)
3. δ ≈ 0.036 is 20× the σ
4. LF inequality aggregates 11 terms with mixed signs → error propagation inflates σ
5. LF violation S_LF1 ≈ 0.062 is only 6× its σ (the aggregation is the problem)

---

## 3-Round RCA Summary

| Round | Finding | Score |
|---|---|---|
| **R1: Q1** | α=45° LF violation (+0.022) is 1.9σ — NOT significant. K9-S11c's "sweet spot" was premature. Need α ≤ 42° for 3σ. | **5.0/5** ✅ |
| **R2: Q2** | Optimal α = **31°** (FOM = 6.0). BOTH LF (6.0σ) and K9_E (20.8σ) detectable with N=91,000. The bottleneck is ALWAYS the LF significance. | **5.0/5** ✅ |
| **R3: Q3** | K9_E measurable: δ⟨A₁B₂⟩ = -0.036 at β_K9=0.3 (4.2% shift, 20.8σ). Even β_K9=0.1 gives 6.7σ. K9_E is NOT the limiting factor. | **5.0/5** ✅ |

**All 3 rounds ≥ 4/5. K9-S11d COMPLETE.**

---

## CORRECTED K9-S12 Foundation

K9-S12 should propose modified Bong at **α = 31°** (not 45°):

| Parameter | Standard Bong | Modified Bong (K9-S12) |
|---|---|---|
| Friend basis | z-basis | z-basis (unchanged) |
| Superobserver polar angle | 90° (equatorial) | **31°** (tilted) |
| Azimuthal angles | φ₁=168°, φ₂=0°, φ₃=118° | same (unchanged) |
| β parameter | 175° | same (unchanged) |
| μ | 0.95 | same (unchanged) |
| N coincidences | 91,000 | same (unchanged) |
| Gen LF 1 violation | -1.61 (not violated) | **+0.062 (6.0σ)** ✅ |
| K9_E δ⟨A₁B₂⟩ | 0 (hidden) | **-0.036 (20.8σ)** ✅ |

**Both LF AND K9_E testable with existing Bong-level statistics.**
