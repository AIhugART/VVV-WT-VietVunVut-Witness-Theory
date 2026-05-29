Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K->p(o) Bridge Law -- Single Entry Point

**Date:** 2026-05-29
**Status:** Canonical index (3-round RCA 4.8/5)
**Role:** Single entry point for the K->p(o) bridge law -- read this FIRST.
**Replaces:** `tuong_lai.bak` S8 vision of "K-rho Coupling Physical Prediction Model"
**VVV-QMRF-EX:** Compass only -- all K9_E terms traceable to K1-K8 via EX map (K9S7_final_lock.md SEX COMPASS)

---

## 0. What Is This? / Day la cai gi?

**EN:** This is the K->p(o) bridge law -- the formula that connects VVV-QMRF's
K-space registration structure to physical measurement probabilities. It is the
**core output** of VVV-QMRF Class C. Read this document first (10 minutes),
then follow links to canonical sources for detail.

**VN:** Day la luat cau noi K->p(o) -- cong thuc ket noi cau truc ghi nhan
K-space cua VVV-QMRF voi xac suat do vat ly. Day la **output cot loi** cua
VVV-QMRF Class C. Doc tai lieu nay truoc (10 phut), sau do theo link den
cac nguon canonical de biet chi tiet.

---

## 1. The Formula / Cong thuc

```
                         P_QM(o) x [1 - beta x f_perp(o, K_ctx)]
  P(o | K_ctx, beta) =  ------------------------------------------
                                        Z(K_ctx)

  where:
    P_QM(o) = Tr(E_o rho)                                   [Standard QM Born rule]
    f_perp  = fraction of K_ctx registrations bot_K-inconsistent with outcome o
    beta    = suppression strength, beta in [0, 1)           [FREE PARAMETER]
    Z       = SUM_o P_QM(o) x [1 - beta x f_perp(o, K_ctx)] [normalization]
```

**In words / Noi don gian:**
> Khi mot observer trong he do co registration mau thuan (bot_K) voi outcome
> dang xet, xac suat cua outcome do bi SUPPRESS (giam di). beta kiem soat
> muc do suppression. Khi beta=0 hoac khong co bot_K -> quay ve QM chuan.

**Source:** [K9S7_final_lock.md](03_k9_sprints/k9_analysis/K9S7_final_lock.md) SFINAL K9_E DEFINITION (LOCKED v1.0, 2026-05-23)

---

## 2. Where Each Piece Comes From / Moi thanh phan tu dau ra

| Symbol | Meaning / Y nghia | Origin / Nguon goc |
|---|---|---|
| **K_ctx** | Tap hop K-state cua CAC observer KHAC (khong phai chinh minh), co T3-morphism va tuong thich thoi gian | **K1-K8:** K1 (act-result), K2 (temporal injectivity), K3 (self-cert), K5 (bot_K). T3-morphism tu bridge theorem T1 (N=2 constructive). |
| **f_perp** | Ty le registration trong K_ctx co bot_K voi outcome dang xet VA outcome-inconsistent qua quantum state (khong phai naive khac) | **K5:** bot_K incommensurability -- registration mau thuan -> suppression. **K9S7_final_lock.md** L43-48. |
| **beta** | Cuong do suppression -- FREE PARAMETER, khong derived tu K1-K8 | **Class C qualified:** beta=0 -> Standard QM. beta>0 -> deviation. Gia tri chua biet -- can experiment. |
| **Z** | Chuan hoa -- dam bao SUM P = 1 | **Toan hoc:** he qua cua multiplicative form. Tu dong giu probability trong [0,1]. |

### Boundary Conditions / Dieu kien bien

| # | Condition | Meaning |
|---|---|---|
| (a) | K_ctx = empty | f_perp = 0 -> P = P_QM (khong co observer khac -> khong co bot_K) |
| (b) | beta = 0 | P = P_QM (suppression tat -> Born rule chinh xac) |
| (c) | N = 1 | K_ctx = empty -> Born (single-observer limit) |
| (d) | All bot_K silent | f_perp = 0 -> Born (khong co mau thuan registration) |
| (e) | V(k_i) = 0 | Khong gan P (Bhranti -- invalid registration) |
| (f) | isNull(k_i) | Khong gan P (Anupalabdhi -- null registration) |

**Source:** [K9S7_final_lock.md](03_k9_sprints/k9_analysis/K9S7_final_lock.md) L54-60

---

## 3. Additive vs Multiplicative -- Why This Form? / Tai sao dang nay?

```
tuong_lai.bak (2026-05-16):           K9_E (2026-05-23):
  p = P_QM + delta_K                    p = P_QM x (1 - beta.f_perp) / Z
  (additive -- tong quat nhat)          (multiplicative -- special case co cau truc)

Multiplicative duoc chon vi:
  1. KHOP VOI K5: bot_K = "mau thuan" -> SUPPRESS (x[1-beta]), khong phai "them vao" (+delta)
  2. TU DONG RANG BUOC: Z dam bao SUM p=1, f_perp in [0,1] dam bao p>=0
  3. DE FALSIFY HON: 1 parameter (beta) thay vi N parameters (delta cho moi outcome)
  4. CO DUONG LUI: Falsification Hierarchy cung cap path ve dang rong hon neu Level 0 bi bac bo

Hai dang TUONG DUONG toan hoc: delta = P_QM x ((1-beta.f_perp)/Z - 1)
Multiplicative = additive voi STRUCTURAL CONSTRAINT tu K5.
```

**Source:** [RCA GAP-B analysis](04_governance/Falsification_Hierarchy.md) + [tuong_lai.bak](../tuong_lai.bak) S4

---

## 4. What It Predicts / Du doan cai gi?

### 4.1 Key Prediction: delta_AB(theta)

```
delta_AB(theta) = AB_measured(theta) - AB_QM(theta)

  delta_AB(theta) = 0  iff  theta = pi/2   (equatorial cancellation -- Proposition 1)
  delta_AB(theta) != 0  for theta != pi/2   (when beta > 0)
  delta_AB(theta) proportional to cos theta (leading order, unrenormalized)
```

### 4.2 Numerical Values (K9-S12 Modified Bong Protocol)

| Observable | Standard QM | K9_E Overlap-Only (Eq. 2-3) |
|---|---|---|
| Gen LF 1 at theta = 31 deg | +0.0891 +/- 0.0103 (8.6sigma) | Same (LF preserved) |
| delta_AB at theta = 31 deg | 0 | ~ 0.115 beta (numerical) |
| delta_AB at theta = pi/2 | 0 | 0 (exact -- equatorial cancellation) |
| delta_AB(theta) functional form | delta = 0 for all theta | delta = 0 iff theta = pi/2; non-zero otherwise |

```
At beta = 0.07 (minimum detectable, Phase 1, single setting):
  delta_AB(31 deg) ~ 0.008  ->  n_sigma ~ 4.7 (single), n_sigma ~ 9.4 (combined)
  beta_min ~ 0.07 (single setting), beta_min ~ 0.038 (combined, 4 settings)

At beta = 0.30 (manuscript benchmark, illustrative):
  delta_AB(31 deg) ~ 0.034  ->  n_sigma ~ 20
  FOM = min(n_sigma_LF, n_sigma_signal) = 8.6 at theta = 31 deg
```

**Source:** [manuscript.md](../../papers/paper_002/manuscript.md) S3-6, S8.1 table

### 4.3 Important Caveat / Luu y quan trong

```
WARNING  K9E-PAT (Proietti fitting) CLOSED as UNRESOLVABLE (v31, RCA 4.92/5).
    beta=0.598 tu Proietti fit KHONG DUOC DUNG lam empirical evidence.
    Noise sensitivity FAIL: noise_threshold = 0.10 sigma_RMS << 1.0.
    A0B0 drives 80% of Delta_chi^2 -> apparent signal is noise artifact.

-> beta chua duoc do. Moi gia tri beta trong tai lieu nay la PREDICTION,
  khong phai measurement. Can K9-S12 experiment de do beta thuc su.
```

**Source:** [P10-NOISE methodology decision](04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md)

---

## 5. How It Gets Tested / Duoc kiem tra the nao?

### 5.1 Experiment: K9-S12 Modified Bong Protocol

```
Nen tang:    Bong et al. (2020) EWF experiment
Sua doi:     THEM 1 QWP -> tilt Superobserver measurement tu theta=pi/2 sang theta~31 deg
Thoi gian:   ~1 gio (khong can phan cung moi ngoai QWP)
Phase 1:      Loophole-open screening test (eta~0.87, fair-sampling)
Phase 2:      Loophole-closed (eta>=0.91, SNSPD upgrade)
```

### 5.2 Falsification: C-FALSI v1.0

```
CONDITION A: |delta_AB_combined(31 deg)| < 3sigma -> null o goc toi uu
CONDITION B: chi^2(delta=0) < chi^2_critical across theta-sweep -> khong co theta-dependence

  A+B both hold  -> Level 0 FALSIFIED (beta >= beta_min excluded at 95% CL)
  A fails        -> Evidence for beta > 0 -> SURVIVES
  A holds, B fails -> Inconsistent -> check systematics
  delta_AB(pi/2) != 0 -> Proposition 1 VIOLATED -> FALSIFIED regardless
```

### 5.3 Falsification Hierarchy: 4 Levels

```
Level 0: Overlap-only -- tested by K9-S12 -> C-FALSI v1.0 (PRE-REGISTERED)
Level 1: Density-matrix-dependent -- requires Friend tomography
Level 2: Multi-partite -- requires T4-H + N>=3 observers
Level 3: Non-geometric -- requires multi-platform scans

Level 0 falsification != K9_E falsification.
Higher levels survive Level 0 rejection.
```

**Sources:**
- Protocol: [K9S12_PreRegistration_Protocol.md](04_governance/K9S12_PreRegistration_Protocol.md)
- C-FALSI: [VVV_QMRF_K9_Analysis_Plan.md](03_k9_sprints/VVV_QMRF_K9_Analysis_Plan.md) SC-FALSI
- Hierarchy: [Falsification_Hierarchy.md](04_governance/Falsification_Hierarchy.md)

---

## 6. Canonical Source Map / Ban do nguon canonical

**Neu ban muon biet ve...** | **Doc file nay** | **Section**
---|---|---
Dinh nghia K9_E (cong thuc goc) | [K9S7_final_lock.md](03_k9_sprints/k9_analysis/K9S7_final_lock.md) | SFINAL K9_E DEFINITION
K1-K8 axioms (nen tang) | [K_Space_Axiomatization.md](01_axiomatization/K_Space_Axiomatization.md) | SK1-K8
Toan bo K9 development history | [VVV_QMRF_K9_Analysis_Plan.md](03_k9_sprints/VVV_QMRF_K9_Analysis_Plan.md) | toan bo
Du doan thuc nghiem (paper) | [manuscript.md](../../papers/paper_002/manuscript.md) | S3-8
Falsification rule (C-FALSI) | [VVV_QMRF_K9_Analysis_Plan.md](03_k9_sprints/VVV_QMRF_K9_Analysis_Plan.md) | SC-FALSI v1.0
Falsification hierarchy (4 levels) | [Falsification_Hierarchy.md](04_governance/Falsification_Hierarchy.md) | toan bo
Pre-registration protocol (K9-S12) | [K9S12_PreRegistration_Protocol.md](04_governance/K9S12_PreRegistration_Protocol.md) | toan bo
Formal terminology | [VVV_QMRF_Definitions.md](06_references/VVV_QMRF_Definitions.md) | SK9_E
Noise sensitivity analysis | [RCA_P10_NOISE](04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md) | toan bo
Phan tich additive->multiplicative (GAP-B) | [Falsification_Hierarchy.md](04_governance/Falsification_Hierarchy.md) | S6.2 + RCA response
Historical context (tuong_lai.bak) | [tuong_lai.bak](../tuong_lai.bak) | toan bo
VVV-QMRF-EX compass map | [K9S7_final_lock.md](03_k9_sprints/k9_analysis/K9S7_final_lock.md) | SEX COMPASS FINAL ANCHORING
Toan bo Class C overview | [index.md](index.md) | toan bo

---

## 7. What `tuong_lai.bak` Asked For -- Status / Dieu `tuong_lai.bak` yeu cau

Ngay 2026-05-16, `tuong_lai.bak` dat cau hoi: *"Repo co du thong tin de sua QM chuan khong?"*
va liet ke 7 yeu cau cho "K-rho Coupling Physical Prediction Model."

| # | Yeu cau (2026-05-16) | Trang thai (2026-05-29) | Reference |
|---|---|---|---|
| 1 | K_before hoac K_context | YES K_ctx -- tap K-state cua observer KHAC | K9S7 SK_ctx |
| 2 | P_K activation condition | YES K_ctx khac empty -> f_perp co the khac 0 | K9S7 S(a) |
| 3 | delta_K(o) deviation function | YES f_perp -- multiplicative, khop K5 bot_K | K9S7 Sf_perp |
| 4 | Probability constraints | YES Z normalization + f_perp in [0,1] | K9S7 SZ_E |
| 5 | Numerical predictions | YES delta_AB(31 deg) ~ 0.115 beta, beta_min ~ 0.07 | manuscript S8.1 |
| 6 | Experimental protocol | YES K9-S12 Phase 1 pre-registered | PreReg Protocol |
| 7 | Falsification rule | YES C-FALSI v1.0 + 4-level Hierarchy | C-FALSI + Hierarchy |

**Ket luan:** 7/7 structural items DA CO. Nhung cau hoi GOC ("co du de sua QM chuan khong?")
-> **VAN CHUA**, vi experiment chua duoc thuc hien. Khac biet: ngay 16/5 thieu bridge law;
ngay 29/5 co bridge law + protocol + falsification rule, dang cho experiment.

**3 gap con lai:**
- **GAP-A (empirical):** Can lab thuc hien K9-S12 -- CRITICAL
- **GAP-B (formula):** Additive->Multiplicative -- da giai quyet (multiplicative la refinement)
- **GAP-C (organization):** Tai lieu nay (K_to_p_bridge_law.md) -- DA GIAI QUYET HOM NAY

---

## 8. Pre-Registration Statement

```
Document created:     2026-05-29
3-round RCA score:    4.8/5 (Round 1: 4.5, Round 2: 5.0, Round 3: 4.8)
VVV-QMRF-EX compass:  Applied -- all K9_E terms verified traceable to K1-K8
                      via EX map in K9S7_final_lock.md SEX COMPASS
Anti-hallucination:   Every claim in S1-6 traceable to canonical source in S6 table.
                      No new claims introduced -- this is an INDEX, not a source.

Maintenance rule:     When canonical sources change, update S6 table.
                      If formula changes -> update S1.
                      If predictions change -> update S4.
                      This document is DERIVED -- canonical sources are authoritative.
```

---

## Appendix A -- Quick Reference / Tham khao nhanh

```
+---------------------------------------------------------------+
|             K->p(o) BRIDGE LAW -- QUICK CARD                   |
+---------------------------------------------------------------+
| Formula:    P = P_QM x (1 - beta.f_perp) / Z                  |
| f_perp:     Fraction of bot_K-inconsistent registrations       |
| beta:       Suppression strength in [0,1) -- FREE PARAMETER    |
| Born limit: beta=0 or K_ctx=empty -> P = P_QM exactly          |
| Test:       K9-S12 -- single QWP tilts theta from pi/2 -> 31 deg|
| Signal:     delta_AB(theta) != 0 iff theta != pi/2 (Prop 1)    |
| Sensitivity: beta_min ~ 0.07 (Phase 1, single setting)          |
| Status:     Class C qualified -- structurally testable,         |
|             empirically UNCONFIRMED                             |
| Falsified:  If delta_AB=0 at ALL non-equatorial theta (C-FALSI)|
| Confirmed:  If delta_AB != 0 at any theta != pi/2 AND           |
|             delta_AB(pi/2) = 0                                  |
| Experiment: NOT YET PERFORMED -- proposal only                  |
+---------------------------------------------------------------+
```

---

(C) 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
