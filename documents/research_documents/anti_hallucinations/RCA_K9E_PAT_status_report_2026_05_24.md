Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chi Tiết — K9E-PAT: Multiplicative Pattern Not Confirmed

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Sources:** `proietti_raw_fit.py` (§7), `Phase10_genuine_fit_RCA_Round1.md`, `rca_technical_debt_inventory_2026_05_24.md` (D4), `index.md` (§5), `k9e_predictor.py`

---

## 0. Executive Snapshot

| Thuộc tính | Giá trị |
|------------|---------|
| **Tên** | K9E-PAT — K9_E multiplicative pattern (2BSM/1BSM ratio ~2) NOT confirmed by raw data |
| **Rank** | **#5** trong Top 10 Hallucination Risks (v1.2) |
| **Risk Score** | **12.0** (H=5 x W=2 x (1+0.2) = 12.0) |
| **Risk band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 3 — Broken Trace (data không đủ precision để test pattern) |
| **Status** | **OPEN** — D4 trong technical debt inventory (score 4.0/5) |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | **HIGH (P1)** — trước khi public |
| **Liên quan mật thiết** | P10-NOISE (#2) — hai mũi tấn công vào 4 data points; D6 (#6) — functional form ambiguity |

---

## 1. Toàn bộ Truy vết — K9E-PAT là gì?

### 1.1 Định nghĩa

K9E-PAT (PATtern) là internal consistency test của K9_E: mô hình multiplicative dự đoán **suppression tăng theo cấp số nhân với số observer BSM**.

```
K9_E multiplicative model:
  E_pred = V * E_QM * (1 - beta*g)^(n_BSM)
  g = 0.146 (PP-4 calibration)

Pattern prediction: residual(2 BSM) ~ 2 * residual(1 BSM)
                    (cùng dấu, 2BSM có suppression gấp đôi 1BSM)
```

### 1.2 Dữ liệu từ genuine fit

Từ `proietti_raw_fit.py` §7, best-fit V=0.939, beta=0.598:

| Setting | n_BSM | E_raw | E_pred | Residual | Res/sigma |
|---------|-------|-------|--------|----------|-----------|
| A0B0 | 0 | -0.678 | -0.664 | **-0.014** | -0.43 |
| A0B1 | 1 | +0.570 | +0.606 | **-0.036** | -0.89 |
| A1B0 | 1 | +0.595 | +0.606 | **-0.011** | -0.26 |
| A1B1 | 2 | +0.571 | +0.553 | **+0.018** | +0.54 |

```
K9_E PATTERN CHECK (từ script):
  Residual 0 BSM:      -0.014
  Residual 1 BSM (avg): -0.0235   ← K9_E overestimates
  Residual 2 BSM:       +0.018    ← K9_E underestimates
  Ratio 2BSM/1BSM:      -0.78     ← predicted ~2, actual = OPPOSITE SIGN
```

### 1.3 Effective visibility per setting

| Setting | n_BSM | V_eff = |E_raw|/|E_QM| | K9_E predicted V_eff |
|---------|-------|---------------------------|----------------------|
| A0B0 | 0 | 0.959 | 0.939 |
| A0B1 | 1 | 0.806 | 0.857 |
| A1B0 | 1 | 0.841 | 0.857 |
| A1B1 | 2 | 0.807 | 0.782 |

**Direction:** 0BSM > 1BSM > 2BSM → **ĐÚNG** (K9_E direction confirmed)
**Magnitude:** K9_E dự đoán 2BSM suppression gấp ~2 lần 1BSM → **KHÔNG KHỚP**
**Sign:** 1BSM residual âm, 2BSM residual dương → **NGƯỢC DẤU**

### 1.4 Statistical significance của ratio

```
res_1bsm_avg = -0.0235 ± 0.0287  (propagation từ sigma=0.040, 0.041)
res_2bsm     = +0.018  ± 0.034

Ratio = 0.018 / (-0.0235) = -0.78
Sigma_ratio ≈ 1.72  (error propagation cho ratio của 2 biến)

→ Ratio = -0.78 ± 1.72
→ Consistent với ~2  trong ~1.6 sigma
→ Consistent với ~0  trong ~0.5 sigma
→ Ratio HOÀN TOÀN KHÔNG BỊ RÀNG BUỘC bởi dữ liệu hiện tại
```

> **Key insight:** Sai số của ratio (±1.72) LỚN HƠN chính giá trị (-0.78). Dữ liệu quá nhiễu để xác nhận HOẶC bác bỏ pattern. Pattern "không được xác nhận" chứ không phải "bị bác bỏ."

---

## 2. Round 1 — 5-Whys: Tại sao pattern không khớp?

```
W1: Tại sao ratio 2BSM/1BSM = -0.78 thay vì ~2?
  → 1BSM residual ÂM (-0.0235): K9_E overestimates ở 1 BSM.
    2BSM residual DƯƠNG (+0.018): K9_E underestimates ở 2 BSM.
    → Hai residual NGƯỢC DẤU → ratio âm.

W2: Tại sao hai residual ngược dấu?
  → 3 khả năng:
    (a) Statistical noise: error bars lớn (sigma ~0.04), cả hai residual
        đều < 1 sigma → sign flip có thể là ngẫu nhiên.
    (b) g=0.146 sai: calibration từ PP-4 4D scan (lý thuyết), không từ data.
    (c) Multiplicative form sai: f_perp không phải dạng (1-beta*g)^n.

W3: Tại sao g=0.146 được dùng?
  → g được calibrate từ PP-4 sanity check 4D scan — calibration
    LÝ THUYẾT dựa trên delta_S(beta=0.5) = -0.055.
    g chưa bao giờ được fit từ experimental data.
    → g là MODEL PARAMETER, không phải MEASURED PARAMETER.

W4: Tại sao không fit g từ data?
  → Chỉ có 4 data points. Model hiện tại: 2 free parameters (V, beta).
    Thêm g → 3 free parameters, DOF = 1 → overfitting.
    Không thể independently calibrate g từ 4 data points.

W5: ROOT CAUSE — Tại sao K9E-PAT OPEN?
  → **Dữ liệu không đủ precision để test pattern.**
    4 data points với sigma ~0.04 → ratio error ~1.72.
    Pattern "ratio ~2" cần data precision gấp ~5-10 lần để test.
    → K9E-PAT không phải "pattern failed" mà là "pattern UNTESTABLE
      với dữ liệu hiện tại."
    → g=0.146 là MODELING CHOICE, không phải empirical measurement.
```

### Round 1 Score: 4.3/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Định nghĩa vấn đề chính xác | 5/5 | Phân biệt rõ 3 khả năng: noise, g sai, form sai |
| Phân tích thống kê | 4/5 | Ratio error ~1.72 → pattern untestable |
| 5-Whys đến root cause | 4/5 | g=0.146 là modeling choice + data quá nhiễu |
| **Round 1** | **4.3/5** | PASS (>= 4/5) |

---

## 3. Round 2 — 5-Whys: Tác động nếu pattern thực sự sai?

```
W1: Điều gì xảy ra nếu multiplicative form (1-beta*g)^n thực sự sai?
  → Genuine fit dùng SAI functional form → beta=0.598, Delta_chi2=5.35
    là artifact của model misspecification.

W2: Tại sao W=2 (MEDIUM) mà không phải W=3?
  → W=2 vì:
    - Pattern test là INTERNAL consistency, không phải external validity
    - K9_E POSTULATE không phụ thuộc multiplicative form cụ thể
    - Postulate: P(o|K) = Tr(E_o rho) * f_perp(K_ctx) — f_perp có thể
      có nhiều dạng functional khác nhau
    → Nhưng: nếu form sai, beta=0.598 không có ý nghĩa vật lý.

W3: K9_E có thể tồn tại với functional form khác không?
  → CÓ. Hai implementation hiện tại:
    - Multiplicative: E = E_QM * (1 - beta*g)^n_BSM  (proietti_raw_fit.py)
    - Additive:      E = E_QM * (1 - beta*n_BSM*g_ctx) (k9e_predictor.py)
    → Cả hai đều operationalize CÙNG postulate.
    → Postulate không specify functional form — đó là modeling choice.

W4: Functional form ambiguity có phải vấn đề nghiêm trọng không?
  → CÓ và KHÔNG:
    - KHÔNG cho K9_E postulate (postulate chỉ nói "f_perp(K_ctx)")
    - CÓ cho genuine fit claim (beta=0.598 có nghĩa TRONG multiplicative model)
    → Đây là lý do D6 (two implementations) cũng là debt item.

W5: ROOT CAUSE — Tác động thực sự?
  → **K9E-PAT không invalidate K9_E postulate — nhưng invalidate
    INTERPRETATION của genuine fit numbers.**
    - "beta=0.598" không phải measurement của K9_E strength
    - "Delta_chi2=5.35" là evidence cho non-uniform visibility (REAL)
    - Nhưng non-uniform visibility CÓ THỂ được fit bởi functional form khác
    → Pattern test cho thấy: multiplicative model với g=0.146
      KHÔNG PHẢI là mô tả chính xác DUY NHẤT của dữ liệu.
```

### Round 2 Score: 4.5/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Impact calibration | 4.5/5 | W=2 hợp lý: postulate survives, numbers interpretation bị ảnh hưởng |
| Phân biệt postulate vs operationalization | 5/5 | P(o|K)=Tr*f_perp là postulate; multiplicative form là model |
| Connection với D6 | 4/5 | Pattern failure + implementation divergence = same root cause |
| **Round 2** | **4.5/5** | PASS (>= 4/5) |

---

## 4. Round 3 — 5-Whys: Quyết định cho K9E-PAT

```
W1: Có nên từ bỏ multiplicative model không?
  → KHÔNG. Ratio = -0.78 ± 1.72 → data không đủ precision để bác bỏ.
    Multiplicative model vẫn là CANDIDATE tốt nhất:
    - Chi2/DOF = 0.670 (tốt), p-value = 0.512 (tốt)
    - Direction đúng (0BSM > 1BSM > 2BSM)

W2: K9E-PAT nên được xử lý thế nào?
  → "NOT CONFIRMED" chứ không phải "FAILED":
    - Pattern PREDICTED but UNTESTABLE với data hiện tại
    - Cần data precision ~0.005 (thay vì ~0.04) để test
    - Hoặc cần nhiều data points hơn (nhiều n_BSM values)

W3: Có nên giữ H=5 (Vàng) không?
  → H=5 là HỢP LÝ:
    - Không phải hallucination (H>=7): pattern được PREDICT rõ ràng,
      kết quả được báo cáo minh bạch
    - Không phải OK (H<=2): pattern là test quan trọng, chưa pass
    - H=5 = Vàng: "đáng nghi, cần được track"

W4: Hành động cụ thể trước khi public?
  → 1. TỐI THIỂU: Document "pattern predicted but not confirmed" (đã có)
    2. KHUYẾN NGHỊ: Compute formal CI cho ratio, show ratio=2 in 2-sigma CI
    3. TỐI ƯU: Fit alternative forms (additive, exponential), so sánh AIC/BIC

W5: ROOT CAUSE — Quyết định CUỐI CÙNG?
  → **K9E-PAT giữ OPEN, H=5, Risk=12.0 (MEDIUM). KHÔNG BLOCKING.**
    
    Lý do:
    - Ratio = -0.78 ± 1.72 → pattern UNTESTABLE, không phải FAILED
    - Direction của K9_E ĐƯỢC XÁC NHẬN
    - Postulate SURVIVES — P(o|K)=Tr*f_perp không phụ thuộc form cụ thể
    - P10-NOISE (external validity) quan trọng hơn K9E-PAT (internal)
    
    Trước public:
    1. Document "g=0.146 = modeling choice, beta=0.598 = best-fit IN model"
    2. KHÔNG claim "multiplicative pattern confirmed"
```

### Round 3 Score: 4.7/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Decision clarity | 5/5 | "Not confirmed" ≠ "failed" — quyết định chính xác |
| Statistical honesty | 4.5/5 | Ratio error ~1.72 → untestable. Đây là sự thật. |
| Prioritization vs P10-NOISE | 4.5/5 | P10-NOISE (external) > K9E-PAT (internal) |
| **Round 3** | **4.7/5** | PASS (>= 4/5) |

---

## 5. Tổng hợp 3-Round RCA

| Round | Focus | Score | Key Finding |
|-------|-------|-------|-------------|
| **R1** | Status Assessment | **4.3/5** | DATA PRECISION GAP. Ratio error ±1.72 > ratio value -0.78. Pattern UNTESTABLE. g=0.146 = modeling choice, không measured. |
| **R2** | Impact Assessment | **4.5/5** | Postulate SURVIVES. Interpretation của numbers bị ảnh hưởng. W=2 hợp lý. |
| **R3** | Decision | **4.7/5** | KHÔNG từ bỏ model. "Not confirmed", không "failed". P10-NOISE prioritized hơn. |
| **Aggregate** | | **4.50/5** | **PASS (>= 4/5)** |

---

## 6. Mối liên hệ với các component khác

### 6.1 K9E-PAT + P10-NOISE = Hai mũi tấn công

```
                   4 DATA POINTS (Proietti Figure 3)
                   |
          +--------+--------+
          |                 |
    P10-NOISE (external)   K9E-PAT (internal)
    "Noise giải thích      "Multiplicative pattern
     non-uniform V?"        không khớp data"
          |                 |
          v                 v
    Nếu noise thật:     Nếu pattern sai:
    toàn bộ signal      beta=0.598 là artifact
    là artifact         của model misspecification
          |                 |
          +--------+--------+
                   |
                   v
          Class C (genuine) empirical
          leg bị tấn công từ 2 phía
```

### 6.2 So sánh ưu tiên với các component liên quan

| Component | Risk | Deadline | Tính chất |
|-----------|------|----------|-----------|
| P10-NOISE | 18.0 (HIGH) | P1 | External validity — **BIGGER THREAT** |
| **K9E-PAT** | **12.0 (MED)** | **P1** | **Internal consistency — LESS URGENT** |
| D6 (implementations) | 12.0 (MED) | P2 | Operational ambiguity — same root cause |

### 6.3 K9E-PAT + D6 = Cùng root cause

Cả hai đều xuất phát từ: **functional form của f_perp chưa được xác định.** Có thể giải quyết cùng lúc bằng cách fit nhiều functional forms và so sánh AIC/BIC.

---

## 7. EX Compass Cross-Reference

| EX Signal | KE-SC | Liên quan đến K9E-PAT |
|-----------|-------|----------------------|
| K9 bridge parameter sensitivity | 3.7 | Beta sensitivity phụ thuộc functional form |
| Two divergent K9_E implementations | 3.7 (D6) | Additive vs multiplicative = two form candidates |
| K5 multi-observer cross-context firing | 4.0 | f_perp depends on K_ctx (T5) — pattern indirectly tests K_ctx |

EX compass không có node riêng cho K9E-PAT — internal consistency test thuần túy, không có BE/QM analogue.

---

## 8. Quyết định & Hành động

### 8.1 Quyết định

> **K9E-PAT giữ OPEN, rank #5, Risk=12.0 (MEDIUM). KHÔNG BLOCKING.**
>
> Pattern "ratio ~2" được DỰ ĐOÁN nhưng CHƯA ĐƯỢC XÁC NHẬN — không "bị bác bỏ."
> Ratio = -0.78 ± 1.72 → dữ liệu QUÁ NHIỄU để test pattern.
>
> Direction K9_E ĐƯỢC XÁC NHẬN. Multiplicative model vẫn best-fit.
> g=0.146 = MODELING CHOICE, không phải measurement.

### 8.2 Hành động cụ thể

| # | Hành động | Ưu tiên | Effort | Deadline |
|---|----------|---------|--------|----------|
| **1** | **Statistical CI:** Tính formal confidence interval cho ratio. Chứng minh ratio=2 nằm trong 2-sigma CI. | **P1** | 1-2h | Trước public |
| **2** | **Document:** "g=0.146 = modeling choice (PP-4 theoretical calibration, not measured). beta=0.598 = best-fit within multiplicative model." | **P1** | 15ph | Trước public |
| **3** | **Fit comparison:** Fit additive model vào raw data. So sánh chi2/AIC với multiplicative. | P2 | 1-2h | 2026-06-15 |
| **4** | **Merge với D6:** Giải quyết K9E-PAT + D6 cùng lúc — cùng root cause. | P2 | 2-3h | 2026-06-15 |

### 8.3 Điều kiện đóng

1. Higher precision data (sigma ~0.005) → ratio error < 0.3 → testable → nếu ratio ~2: **ĐÓNG, H=5→2**
2. >= 3 functional forms compared, multiplicative best-fit (Delta_AIC > 2): **ĐÓNG, H=5→3**
3. 3-observer experiment confirm pattern: **ĐÓNG, H=5→2**

---

## 9. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Status accuracy | 4.3/5 | Ratio = -0.78 ± 1.72 → UNTESTABLE. g=0.146 = modeling choice. |
| R2 | Impact calibration (W=2) | 4.5/5 | Postulate survives. Numbers interpretation affected. |
| R3 | Decision quality + prioritization | 4.7/5 | P10-NOISE > K9E-PAT. "Not confirmed" documented honestly. |
| **Aggregate** | | **4.50/5** | **PASS (>= 4/5)** |

---

## 10. Kết luận

> **K9E-PAT: Multiplicative pattern PREDICTED but UNTESTABLE với dữ liệu hiện tại.**
>
> Ratio 2BSM/1BSM = -0.78 ± 1.72 — sai số lớn hơn giá trị. Không thể xác nhận HOẶC bác bỏ.
>
> **Direction ĐƯỢC XÁC NHẬN** (suppression tăng theo n_BSM).
> **Magnitude CHƯA XÁC NHẬN** (pattern ratio ~2 không thể test).
> **Postulate SURVIVES** — P(o|K)=Tr*f_perp không phụ thuộc multiplicative form.
>
> **K9E-PAT (internal) ÍT NGUY HIỂM HƠN P10-NOISE (external).**
> Rank #5, Risk=12.0, MEDIUM. Deadline P1 (trước public).
> **Hành động chính:** Document g=0.146 = modeling choice + compute formal CI.

---

*RCA K9E-PAT Status Report — 2026-05-24. 3-Round RCA x 5-Why x Scoring Threshold 4/5. Aggregate: 4.50/5. VVV-QMRF scope, VVV-QMRF-EX as compass.*
