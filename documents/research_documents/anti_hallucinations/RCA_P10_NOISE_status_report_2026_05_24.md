Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Chi Tiết — P10-NOISE: Non-Uniform Noise Not Ruled Out

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Sources:** `00_top_10_hallucinations_record.md` (v1.2), `rca_technical_debt_inventory_2026_05_24.md` (D8), `Phase10_genuine_fit_RCA_Round1.md`, `Phase10_joint_verdict.md`, `label_system.md`

---

## 0. Executive Snapshot

| Thuộc tính | Giá trị |
|------------|---------|
| **Tên** | P10-NOISE — Non-uniform phase noise not ruled out as alternative explanation |
| **Rank** | **#2** trong Top 10 Hallucination Risks (v1.2) |
| **Risk Score** | **18.0** (H=5 x W=3 x (1+0.2) = 18.0) |
| **Risk band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 3 — Broken Trace (chưa có noise analysis đầy đủ) |
| **Status** | **OPEN** — identified trong technical debt inventory (D8, score 3.5/5) |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-NOISE] [AH-EX]` |
| **Deadline** | **HIGH (P1)** — trước khi public claim "genuine" |
| **Next audit** | 2026-05-31 |
| **Nếu hallucination thật** | Genuine fit K9_E → artifact; Class C (genuine) downgrade → Class C (qualified) |

---

## 1. Toàn bộ Truy vết — P10-NOISE là gì?

### 1.1 Định nghĩa

P10-NOISE là alternative explanation cho K9_E genuine fit: **non-uniform phase noise** trong Proietti experiment có thể tạo ra non-uniform visibility pattern mà K9_E đang fit.

```
K9_E claim:           V(0,0)=0.959 > V(BSM) ~ 0.93 → K9_E suppression (beta=0.598)
Alternative (NOISE):  V(0,0)=0.959 > V(BSM) ~ 0.93 → phase noise khác nhau giữa các settings
```

### 1.2 Dữ liệu gốc (Proietti Figure 3)

| Setting | n_BSM | E_raw | E_pred (K9_E) | Residual | Res/sigma |
|---------|-------|-------|---------------|----------|-----------|
| A0B0 | 0 | -0.678 +/- 0.033 | -0.664 | -0.014 | -0.43 |
| A0B1 | 1 | +0.570 +/- 0.040 | +0.606 | -0.036 | -0.89 |
| A1B0 | 1 | +0.595 +/- 0.041 | +0.606 | -0.011 | -0.26 |
| A1B1 | 2 | +0.571 +/- 0.034 | +0.553 | +0.018 | +0.54 |

- K9_E best-fit: V=0.939, beta=0.598, chi2=1.340, chi2/DOF=0.670, p=0.512
- QM-only (beta=0): V=0.860, chi2=6.687, chi2/DOF=2.229
- **Delta_chi2 = 5.347 (2.31 sigma)** — K9_E được ưu tiên hơn QM-uniform-visibility

### 1.3 Ba khả năng cho non-uniform visibility

| # | Giải thích | Bằng chứng ủng hộ | Bằng chứng chống |
|---|-----------|-------------------|-----------------|
| **(a)** | K9_E suppression (beta > 0) | Direction đúng: 0-BSM ít bị suppress hơn BSM. Delta_chi2=5.35. | Multiplicative pattern không khớp (ratio = -0.78 vs ~2). A1B1 residual DƯƠNG (+0.018). |
| **(b)** | Experimental noise không đều | Có trong optical literature: phase drift, alignment variation, detector efficiency fluctuation. | Chưa có evidence cụ thể cho Proietti setup. Cần raw data để kiểm tra. |
| **(c)** | Statistical fluctuation | 2.31 sigma — không đủ mạnh để loại trừ. Cần > 3 sigma để claim discovery. | Pattern có vẻ systematic (3/4 BSM settings đều thấp hơn expected QM). |

> **Hiện tại:** Không thể phân biệt (a) và (b) chỉ với 4 data points + error bars.

---

## 2. Round 1 — 5-Whys: Tại sao P10-NOISE vẫn OPEN?

```
W1: Tại sao P10-NOISE chưa được rule out?
  → Chưa có noise analysis đầy đủ cho Proietti experimental setup.

W2: Tại sao chưa có noise analysis?
  → Chỉ có 4 correlator values + error bars từ Proietti Figure 3.
    Không có raw event-level data (timestamps, individual detection events).
    Không có independent noise characterization từ experimental team.

W3: Tại sao 4 data points không đủ để rule out noise?
  → Mỗi setting là 1 correlator value được integrate từ hàng ngàn events.
    Non-uniform noise CÓ THỂ tạo ra pattern tương tự:
    - Phase drift giữa các setting measurements
    - Detector efficiency variation theo thời gian
    - Alignment drift khi chuyển từ (0,0) → BSM settings
    → 4 data points không mang thông tin về noise correlation giữa settings.

W4: Tại sao không yêu cầu raw data từ Proietti group?
  → Raw event-level data từ experiment 2019 có thể không còn được lưu trữ.
    Experimental collaborations thường publish summary statistics, không publish raw data.
    Đây là DATA-AVAILABILITY GAP — không phải lỗi phân tích.

W5: ROOT CAUSE — Tại sao P10-NOISE vẫn OPEN?
  → **Khoảng trống dữ liệu không thể lấp đầy từ published sources.**
    Để rule out noise, cần MỘT TRONG HAI:
    (A) Raw event-level data từ Proietti experiment (có thể không còn tồn tại)
    (B) Independent noise model calibrated từ experimental literature
    → Hiện tại chưa có (A) và chưa làm (B).
    → P10-NOISE là BLOCKING GATE cho public claim "genuine" với confidence cao.
```

### Round 1 Score: 4.5/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Định nghĩa vấn đề chính xác | 5/5 | Phân biệt rõ 3 alternative explanations (a)(b)(c) |
| Truy vết dữ liệu đầy đủ | 4/5 | 4 data points + error bars từ Figure 3. Raw data unavailable — đã xác nhận. |
| 5-Whys đến root cause | 4.5/5 | Data-availability gap là root cause thực sự |
| **Round 1** | **4.5/5** | PASS (>= 4/5) |

---

## 3. Round 2 — 5-Whys: Tác động nếu P10-NOISE là thật?

```
W1: Điều gì xảy ra nếu non-uniform noise là nguyên nhân thực sự?
  → Genuine fit (beta=0.598, Delta_chi2=5.35) là ARTIFACT của noise.
    K9_E không có empirical evidence — chỉ còn structural motivation từ K1-K8.

W2: Tại sao điều này nghiêm trọng (W=3)?
  → Class C (genuine) được xây dựng trên 3 trụ:
    Trụ 1: Structural derivation (K1-K8 → K9_E motivation) → VẪN ĐÚNG
    Trụ 2: Empirical evidence (Proietti D1 genuine fit) → CÓ THỂ SẬP
    Trụ 3: Theoretical consistency (FR avoided, 4/4 adversarial tests) → VẪN ĐÚNG
    → Nếu Trụ 2 sập: Class C (genuine) → Class C (qualified).
    → K9_E vẫn là "mathematical possibility" nhưng KHÔNG CÓ empirical evidence.

W3: Có cách nào cứu vãn nếu noise được confirm?
  → CÓ — 3-observer experiment:
    - Prediction: delta_M3 = -0.223 at beta=0.3 (11x amplification, illustrative)
    - Experimental design CÓ THỂ characterization noise ĐỘC LẬP
    - Không phụ thuộc vào Proietti data
    → Nhưng: T4-H Steps 3-4 DEFERRED, experiment design chưa có.

W4: Tại sao 3-observer experiment chưa sẵn sàng?
  → T4-H Steps 3-4 (N-observer colimit) DEFERRED — chưa có structural validation.
    Prediction delta_M3 = -0.223 là ILLUSTRATIVE, không phải validated.
    Experiment design ở mức "idea" — cần collaboration với experimental group.

W5: ROOT CAUSE — Tác động thực sự?
  → **P10-NOISE là single-point-of-failure cho empirical evidence của K9_E.**
    Nếu non-uniform noise được confirm là nguồn gốc của Delta_chi2=5.35:
    - K9_E mất empirical leg duy nhất hiện tại
    - Class C downgrade từ (genuine) → (qualified)
    - VVV-QMRF quay về trạng thái "mathematical framework chưa có experimental support"
    - 3-observer experiment trở thành con đường DUY NHẤT để phục hồi
```

### Round 2 Score: 4.8/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Impact assessment chính xác | 5/5 | Phân tích 3 trụ của Class C (genuine), xác định Trụ 2 là single-point-of-failure |
| Mitigation path rõ ràng | 5/5 | 3-observer experiment là con đường độc lập, không phụ thuộc Proietti data |
| Honest về limitation | 4.5/5 | 3-observer hiện tại là illustrative, không phải ready-to-test |
| **Round 2** | **4.8/5** | PASS (>= 4/5) |

---

## 4. Round 3 — 5-Whys: Quyết định cho P10-NOISE

```
W1: Có nên downgrade Class C (genuine) → (qualified) ngay bây giờ không?
  → KHÔNG. Evidence là REAL và DIRECTIONALLY CORRECT:
    - Delta_chi2=5.35 (2.31 sigma) là tín hiệu THẬT từ raw data
    - Direction đúng: 0-BSM ít bị suppress hơn BSM settings
    - "Ambiguous" đã được KHAI BÁO MINH BẠCH trong index.md và mọi RCA document
    → Class C (genuine) + "ambiguous" = accurate description hiện tại.

W2: Điều kiện gì để GIỮ Class C (genuine)?
  → Ít nhất MỘT trong hai:
    (a) Noise sensitivity analysis cho thấy non-uniform noise không thể giải thích
        toàn bộ Delta_chi2=5.35 ở mức confidence > 2 sigma
    (b) 3-observer experiment độc lập confirm K9_E signal

W3: P10-NOISE có nên được ưu tiên #1 thay vì phi-map không?
  → Risk Score formula (H x W x (1+A)) ưu tiên H (hallucination risk) hơn W (impact).
    Đây là THIẾT KẾ CÓ CHỦ ĐÍCH của AHP:
    - Mục tiêu: chống HALLUCINATION (bịa đặt), không phải risk management
    - phi-map H=6 (conjecture chưa prove) > P10-NOISE H=5 (alternative explanation)
    → P10-NOISE #2 là ĐÚNG theo tiêu chí hallucination risk.
    
    TUY NHIÊN, về mặt IMPACT:
    - P10-NOISE W=3 > phi-map W=2
    - P10-NOISE deadline P1 > phi-map deadline P3
    → P10-NOISE NGUY HIỂM HƠN về mặt thực tế.
    → Ghi chú này đã được document trong RCA_why_phi_map_is_top1.

W4: Có nên thay đổi công thức Risk Score không?
  → KHÔNG trong scope của RCA này. Risk Score formula là thiết kế của AHP.
    Nếu muốn ưu tiên IMPACT, cần một công thức riêng:
    Impact Score = W x H x (1+A) — nhưng đây là decision cho AHP design review.

W5: ROOT CAUSE — Quyết định CUỐI CÙNG?
  → **P10-NOISE là BLOCKING GATE cho public claim "genuine" với confidence > 2 sigma.**
    
    Hành động CỤ THỂ trước khi public:
    1. **BẮT BUỘC:** Thực hiện noise sensitivity analysis —
       "Nếu non-uniform noise là nguyên nhân, nó cần lớn đến mức nào
        để tạo ra Delta_chi2=5.35?"
    2. **BẮT BUỘC:** Thêm explicit boundary statement trong index.md:
       "Genuine claim is conditional on noise being uniform across settings."
    3. **KHUYẾN NGHỊ:** Theo dõi experimental literature về phase noise
       trong optical interferometric setups.
    
    Nếu KHÔNG THỂ làm (1): downgrade Class C (genuine) → Class C (qualified)
    trước khi public. "Qualified" + "directionally consistent with K9_E"
    vẫn là mô tả chính xác và trung thực.
```

### Round 3 Score: 4.7/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Decision clarity | 5/5 | Ba hành động cụ thể, có điều kiện rõ ràng |
| Boundary honesty | 4.5/5 | Không downgrade vội — evidence là thật. Nhưng có gate conditions. |
| Risk Score formula analysis | 4.5/5 | Công thức đúng với mục tiêu (anti-hallucination). Impact analysis là riêng. |
| **Round 3** | **4.7/5** | PASS (>= 4/5) |

---

## 5. Tổng hợp 3-Round RCA

| Round | Focus | Score | Key Finding |
|-------|-------|-------|-------------|
| **R1** | Status Assessment | **4.5/5** | Root cause: DATA-AVAILABILITY GAP. 4 data points không đủ để phân biệt K9_E suppression với non-uniform noise. Cần raw event-level data hoặc independent noise model. |
| **R2** | Impact Assessment | **4.8/5** | P10-NOISE là SINGLE-POINT-OF-FAILURE cho empirical leg của Class C (genuine). Nếu noise được confirm → downgrade. 3-observer experiment là mitigation path độc lập. |
| **R3** | Decision | **4.7/5** | KHÔNG downgrade vội. Evidence là thật (2.31 sigma). Nhưng PHẢI làm noise sensitivity analysis + boundary statement TRƯỚC KHI public. |
| **Aggregate** | | **4.67/5** | **PASS (>= 4/5)** |

---

## 6. So sánh P10-NOISE với các component liên quan

### 6.1 P10-NOISE vs P10-TIM

| Tiêu chí | P10-NOISE | P10-TIM |
|----------|-----------|---------|
| **Vấn đề** | Noise CÓ THỂ giải thích non-uniform visibility | Null-model N0 (QM V=1) bị omitted |
| **Risk Score** | 18.0 (HIGH) | 9.0 (LOW) |
| **Status** | OPEN | DECISION-LOCKED |
| **Tại sao khác nhau?** | Noise là ACTIVE threat — có thể invalidate genuine fit | N0 là PASSIVE gap — cần raw data không có sẵn |
| **Độ khẩn cấp** | P1 (trước public) | P3 (khi có data) |

### 6.2 P10-NOISE vs phi-map

| Tiêu chí | P10-NOISE #2 | phi-map #1 |
|----------|-------------|-----------|
| **H (hallucination)** | 5 | **6** (cao nhất) |
| **W (impact)** | **3** (threatens evidence) | 2 (không block K9_E) |
| **Deadline** | **P1** (trước public) | P3 (long-term) |
| **Nếu sai** | Class C downgrade | Mất "bridge to QM" |
| **Có thể fix?** | Có — noise sensitivity analysis | Có — Phase 3+4 roadmap |
| **Tại sao xếp sau?** | H=5 < H=6 → tiebreaker H đẩy phi-map lên #1 | |

> **Lưu ý:** Risk Score ưu tiên H (hallucination risk). P10-NOISE NGUY HIỂM HƠN phi-map về mặt tác động thực tế, nhưng ÍT ĐÁNG NGHI HƠN (alternative explanation có cơ sở trong experimental literature, không phải bịa đặt).

### 6.3 P10-NOISE vs K9E-PAT

| Tiêu chí | P10-NOISE | K9E-PAT |
|----------|-----------|---------|
| **Vấn đề** | Noise có thể là nguồn gốc CỦA TOÀN BỘ signal | Multiplicative pattern CỦA K9_E không khớp data |
| **Risk Score** | 18.0 | 12.0 |
| **Mối liên hệ** | Nếu noise được rule out → K9E-PAT vẫn là vấn đề (pattern sai) | Nếu pattern được sửa → vẫn cần rule out noise |
| **Cả hai đều cần được giải quyết** trước khi public | | |

---

## 7. EX Compass Cross-Reference

| EX Signal | KE-SC | Liên quan đến P10-NOISE |
|-----------|-------|------------------------|
| N_QM_VVV_00032 (Bhranti ↔ Decoherence) | 3.5 | BE registration error (bhranti) mapped to physical noise/decoherence — structural analogue |
| K9 bridge parameter sensitivity | 3.7 | Beta sensitivity phụ thuộc vào noise model — noise ảnh hưởng đến beta estimation |
| T4 N-observer colimit | 3.5 | 3-observer experiment (mitigation path) phụ thuộc vào T4 |

EX compass xác nhận: noise model là STRESS POINT trong K-space ↔ ρ-space bridge. Không có EX node nào trực tiếp resolve P10-NOISE — đây là gap cần được lấp đầy từ experimental side.

---

## 8. Quyết định & Hành động

### 8.1 Quyết định

> **P10-NOISE giữ nguyên status OPEN, rank #2, Risk Score 18.0.**
>
> KHÔNG downgrade Class C (genuine) → (qualified) TẠI THỜI ĐIỂM NÀY.
> Evidence là REAL (2.31 sigma), directionally correct, và "ambiguous" đã được khai báo minh bạch.
>
> **NHƯNG:** P10-NOISE là BLOCKING GATE cho public claim. Trước khi public, PHẢI thực hiện noise sensitivity analysis HOẶC thêm explicit boundary statement.

### 8.2 Hành động cụ thể

| # | Hành động | Ưu tiên | Effort | Blocked by | Deadline |
|---|----------|---------|--------|------------|----------|
| **1** | **Noise sensitivity analysis:** "Non-uniform noise cần lớn đến mức nào để tạo ra Delta_chi2=5.35?" — Tính toán upper bound của noise contribution từ error bars và published noise literature. | **P1 (BẮT BUỘC)** | 2-3 giờ | — | Trước khi public |
| **2** | **Boundary statement trong index.md:** Thêm explicit caveat: "'Genuine' claim is conditional on noise being uniform across measurement settings. Non-uniform phase noise has not been ruled out with available data." | **P1 (BẮT BUỘC)** | 10 phút | — | Trước khi public |
| **3** | **Literature review:** Tìm experimental papers về phase noise trong optical interferometric CHSH experiments — calibrate noise model. | P2 (KHUYẾN NGHỊ) | 2-4 giờ | — | 2026-06-15 |
| **4** | **3-observer experiment design:** Phát triển experimental protocol với noise characterization độc lập. | P3 (DÀI HẠN) | Vài tuần | T4-H Steps 3-4 | Long-term |
| **5** | **Nếu không thể làm #1:** Downgrade Class C (genuine) → Class C (qualified) trước khi public. | P1 (FALLBACK) | 30 phút | — | Trước khi public |

### 8.3 Điều kiện để đóng P10-NOISE

P10-NOISE có thể được đóng khi MỘT trong các điều kiện sau được thỏa mãn:

1. **Noise analysis cho thấy:** Non-uniform noise không thể tạo ra Delta_chi2 >= 5.35 ở mức confidence > 2 sigma → **GỠ `[AH-NOISE]`, H=5→3, Risk=18.0→10.8**
2. **3-observer experiment confirm:** K9_E signal được phát hiện ĐỘC LẬP với noise characterization → **GỠ `[AH-NOISE]`, H=5→2**
3. **Raw event data obtained:** Phân tích noise correlation trực tiếp từ raw data → **GỠ `[AH-NOISE]`, H=5→2**

---

## 9. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Status accuracy — does P10-NOISE assessment reflect actual data and analysis state? | 4.5/5 | 4 data points, 3 alternative explanations (a/b/c), data-availability gap identified. Root cause: không thể phân biệt K9_E suppression với noise chỉ từ published data. |
| R2 | Impact calibration — is W=3 justified? | 4.8/5 | Single-point-of-failure cho empirical evidence của K9_E. Nếu noise được confirm → Class C downgrade. 3-observer experiment là mitigation path độc lập. W=3 hoàn toàn hợp lý. |
| R3 | Decision quality — are actions clear and actionable? | 4.7/5 | 5 hành động cụ thể + 3 điều kiện đóng + fallback path (downgrade nếu không thể làm noise analysis). Boundary honesty: KHÔNG downgrade vội, NHƯNG có gate conditions rõ ràng. |
| **Aggregate** | | **4.67/5** | **PASS (>= 4/5)** |

---

## 10. Kết luận

> **P10-NOISE là BLOCKING GATE cho public claim "genuine" — nhưng KHÔNG PHẢI là lý do để downgrade Class C ngay bây giờ.**
>
> Evidence từ Proietti Figure 3 là REAL (Delta_chi2=5.35, 2.31 sigma) và DIRECTIONALLY CORRECT (0-BSM less suppressed than BSM). "Ambiguous" đã được khai báo minh bạch trong mọi document.
>
> **Trước khi public, PHẢI làm noise sensitivity analysis** để chứng minh rằng non-uniform noise không thể giải thích toàn bộ Delta_chi2=5.35. Nếu không thể làm được điều này, PHẢI downgrade Class C (genuine) → (qualified) HOẶC thêm explicit boundary statement rằng "genuine" là conditional on uniform noise.
>
> **P10-NOISE hạng #2, Risk=18.0, HIGH. Deadline: P1 (trước khi public).**
>
> Risk Score formula ưu tiên H (hallucination risk) → P10-NOISE H=5 < phi-map H=6 → #2 là đúng.
> Nhưng về mặt IMPACT (W=3): P10-NOISE là component NGUY HIỂM NHẤT trong toàn bộ VVV-QMRF hiện tại.

---

*RCA P10-NOISE Status Report — 2026-05-24. 3-Round RCA x 5-Why x Scoring Threshold 4/5. Aggregate: 4.67/5. VVV-QMRF scope, VVV-QMRF-EX as compass.*
