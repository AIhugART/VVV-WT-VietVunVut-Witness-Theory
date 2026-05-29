Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Track 1B — Model Comparison RCA
# Additive vs Multiplicative vs Empirical

**Date:** 2026-05-24
**Plan:** Post-v30 Execution Plan, Track 1
**Method:** 3-Round RCA x 5-Why x Scoring Threshold 4/5

---

## Comparison Table

| Source | 1BSM delta | 2BSM delta | Ratio |
|--------|-----------|-----------|-------|
| ADDITIVE prediction (g=0.039, beta=0.598) | -0.0164 | -0.0329 | 2.000 |
| MULTIPLICATIVE prediction (g=0.146, beta=0.598) | -0.0580 | -0.1109 | 1.913 |
| EMPIRICAL residual (after multiplicative fit) | -0.0235 | +0.0179 | -0.762 |

---

## Round 1 — Tai sao empirical ratio (-0.76) khac model predictions (~2)?

### 5-Whys

W1: Tai sao empirical ratio khac model predictions?
  -> Vi residuals sau K9_E fit deu nam trong 1sigma cua zero.
     Ratio -0.76 la ket qua cua viec chia hai con so gan zero.

W2: Tai sao residuals nho nhu vay?
  -> Vi multiplicative model (V=0.939, beta=0.598, 2 params) da fit
     4 data points kha tot (chi2/DOF = 0.67, p=0.51).

W3: Neu fit tot, tai sao residual ratio trong "sai"?
  -> "Ratio = -0.78" la metric gay hieu nham. No lay hai residuals deu
     consistent voi zero (moi cai <1sigma), chia cho nhau, va coi ket qua
     la co y nghia. Khi chia hai so gan zero, ket qua cuc ky khong on dinh
     va bi chi phoi boi random sign fluctuations.

W4: Empirical ratio co phai la test hop le cua K9_E khong?
  -> Khong. K9_E du doan SUPPRESSION PATTERN (delta = E_K9E - E_QM),
     khong phai residual pattern sau fit. K9_E prediction (ratio ~2 cho
     suppression) la ve MODEL. Empirical residual ratio -0.78 la ve
     NHUNG GI CON LAI sau fit.

W5: ROOT CAUSE
  -> "K9E-PAT ratio = -0.78" la MISINTERPRETATION. No khong phai la
     K9_E prediction that bai. No la residual noise sau mot fit tot
     bi chia cho nhau tao ra mot con so ngau nhien. Ca hai K9_E model
     deu du doan suppression ratio ~2. Du lieu thuc nghiem, sau khi
     loai bo K9_E suppression, cho thay residuals consistent voi zero.

### Round 1 Score: 4.88/5 — PASS

| Criteria | Score |
|----------|-------|
| So lieu chinh xac | 5.0/5 |
| Misinterpretation identified | 5.0/5 |
| Noise-level residuals recognized | 5.0/5 |
| Root cause isolated | 4.5/5 |

---

## Round 2 — Du lieu thuc su noi gi ve K9_E?

### 5-Whys

W1: 4 data points tu Proietti cho ta biet duoc gi?
  -> Rat it, ngoai nhung gi chi2 fit da noi.

W2: Chi2 noi gi?
  -> Multiplicative K9_E (beta=0.598) cai thien chi2 tu 6.687 (QM-only)
     xuong 1.340 (Delta_chi2=5.35, 2.31sigma). Nhung P10-NOISE da chung
     minh: random noise o BAT KY magnitude nao cung tao ra Delta_chi2 >= 5.35
     trong ~50% so lan.

W3: Du lieu consistent voi CA "K9_E co that" VA "pure noise"?
  -> Dung. Khong the phan biet duoc.

W4: Additive model tot hon hay te hon multiplicative?
  -> Additive model voi beta=0.598 tao suppression delta ~ -0.016 moi BSM,
     nho hon nhieu so voi multiplicative (delta ~ -0.058 moi BSM).
     Additive model's suppression qua nho de phat hien duoc.

W5: ROOT CAUSE
  -> 4 Proietti data points KHONG DU de:
     (a) Phan biet additive vs multiplicative K9_E model
     (b) Phan biet K9_E voi noise (P10-NOISE)
     (c) Validate hay reject 2BSM/1BSM ratio prediction
  -> K9E-PAT "ratio = -0.78" la RED HERRING.

### Round 2 Score: 5.00/5 — PASS

| Criteria | Score |
|----------|-------|
| Data limitation analysis | 5.0/5 |
| Additive vs multiplicative | 5.0/5 |
| P10-NOISE consistency | 5.0/5 |
| Red herring identified | 5.0/5 |

---

## Round 3 — Quyet dinh: Lam gi voi K9E-PAT?

### 5-Whys

W1: Co the dong K9E-PAT voi du lieu hien tai khong?
  -> Co, nhung la UNRESOLVABLE, khong phai CONFIRMED hay REJECTED.

W2: Tai sao UNRESOLVABLE?
  -> Du lieu thuc su ambiguous. Khong the rule out K9_E, cung khong the
     confirm. Tot nhat co the noi: "2BSM/1BSM ratio khong the do duoc
     voi precision co y nghia tu 4 data points."

W3: Cai gi SE resolve duoc K9E-PAT?
  -> Dedicated experiment voi: nhieu data points (alpha-sweep),
     noise duoc dac trung hoa, direct 2BSM vs 1BSM comparison.
  -> K9-S12 optical experiment.

W4: Co the cai thien theoretical understanding trong luc cho khong?
  -> Co. Hai model dai dien cho hai assumptions khac nhau ve K_ctx scaling:
     Additive: delta ti le n_BSM -> ratio = 2.000 chinh xac
     Multiplicative: delta ti le (1-bg)^(n_BSM) -> ratio ~ 2-bg ~ 1.91
     Ca hai deu predict ratio ~2 (khac biet <5%).

W5: ROOT CAUSE
  -> K9E-PAT nen duoc DONG la UNRESOLVABLE with current data.
  -> Path to resolution: K9-S12 optical experiment.
  -> K9E-PAT KHONG PHAI evidence CHONG LAI K9_E.
  -> K9E-PAT KHONG PHAI evidence UNG HO K9_E.

### Round 3 Score: 4.88/5 — PASS

| Criteria | Score |
|----------|-------|
| Closure decision hop ly | 5.0/5 |
| Path to resolution ro rang | 5.0/5 |
| Model difference documented | 4.5/5 |
| Honest assessment | 5.0/5 |

---

## Aggregate: 4.92/5 — PASS (>=4/5)

## Final Decision

K9E-PAT -> CLOSED as UNRESOLVABLE with current data.

Ly do:
1. "Ratio = -0.78" la misinterpretation — ratio cua hai sub-sigma residuals
2. Ca hai model deu predict suppression ratio ~2 (2.000 va 1.913)
3. 4 data points khong du de test pattern — P10-NOISE confirms
4. Residuals sau K9_E fit deu <1sigma -> consistent voi zero

Path to resolution: K9-S12 optical experiment (alpha-sweep + noise characterization)
