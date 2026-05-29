Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA Quyết Định Phương Pháp — P10-NOISE Noise Sensitivity Analysis

**Date:** 2026-05-24
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Scope:** VVV-QMRF, VVV-QMRF-EX as compass
**Trigger:** RCA P10-NOISE status report (2026-05-24, aggregate 4.67/5) xác định "phải làm noise sensitivity analysis" nhưng chưa quyết định methodology
**Sources:** `RCA_P10_NOISE_status_report_2026_05_24.md`, `proietti_raw_fit.py`, `Wigner_figure_3.md`, `batch_2026_05_23_cross_domain_analysis.md`, `k9e_predictor.py`

---

## 0. Executive Snapshot

| Thuộc tính | Giá trị |
|------------|---------|
| **Câu hỏi quyết định** | Làm THẾ NÀO để trả lời: "Non-uniform noise cần lớn đến mức nào để tạo ra Delta_chi2=5.35?" |
| **RCA trước đã quyết định** | PHẢI làm noise sensitivity analysis (P1, BẮT BUỘC, 2-3 giờ) |
| **RCA trước CHƯA quyết định** | Methodology, noise model, PASS/FAIL criteria, boundary conditions |
| **Input constraint** | Chỉ có 4 correlator values + error bars từ Proietti Figure 3. Không có raw event-level data. |
| **EX compass constraint** | Không EX node nào trực tiếp resolve P10-NOISE. g_eff=0.146 là MODELING CHOICE không phải empirical measurement. |

---

## 1. Round 1 — 5-Whys: Tại sao noise sensitivity analysis chưa có methodology?

```
W1: Tại sao noise sensitivity analysis chưa được thực hiện?
  → Chưa có quyết định về methodology — không rõ phải làm GÌ và LÀM THẾ NÀO.

W2: Tại sao methodology chưa được quyết định?
  → RCA trước (2026-05-24) tập trung vào status assessment và decision ("có nên downgrade không?"),
    không đi sâu vào technical implementation của noise analysis.
    Đây là PHÂN CÔNG ĐÚNG: RCA đó quyết định "phải làm", RCA này quyết định "làm thế nào."

W3: Tại sao methodology không hiển nhiên?
  → Có 3 cách tiếp cận khác nhau, mỗi cách có risk profile khác:
    (A) Parametric noise model — giả định phân phối noise cụ thể
    (B) Error-bar bootstrap — dùng published uncertainties để sinh synthetic data
    (C) Literature-calibrated bound — dùng giá trị noise từ experimental literature
    → Không có approach nào là "hiển nhiên đúng" vì data quá ít (4 điểm).

W4: Tại sao 4 data points làm methodology khó?
  → Với 4 điểm, MỌI noise model đều underdetermined:
    - Parametric model cần ít nhất 2-3 tham số noise (phase drift, amplitude, correlation)
      → 4 data points không đủ để constrain
    - Bootstrap từ error bars chỉ capture được statistical noise (Poisson),
      không capture được systematic noise (phase drift, alignment)
    - Literature values từ experiment khác có thể không áp dụng được cho Proietti setup
    → Bất kỳ methodology nào cũng sẽ có caveat lớn.

W5: ROOT CAUSE — Tại sao methodology chưa được quyết định?
  → **4 data points tạo ra underdetermination không thể giải quyết triệt để.**
    Mọi noise model đều cần thêm assumptions không kiểm chứng được từ published data.
    → Methodology phải CHẤP NHẬN underdetermination này và chọn approach
      MINIMIZE assumptions trong khi MAXIMIZE honesty về boundary.
    → Đây KHÔNG PHẢI là "chọn model đúng" mà là "chọn model an toàn nhất
      để đặt upper bound có ý nghĩa."
```

### Round 1 Score: 4.6/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Định nghĩa vấn đề chính xác | 5/5 | Phân biệt rõ: RCA trước quyết định "phải làm", RCA này quyết định "làm thế nào" |
| 3 approaches được phân tích | 5/5 | (A) parametric, (B) bootstrap, (C) literature — mỗi cái có risk profile riêng |
| Underdetermination được nhận diện | 4.5/5 | 4 data points là fundamental constraint, không phải temporary limitation |
| Root cause được isolate | 4/5 | Root cause = underdetermination. Giải pháp = chấp nhận và minimize assumptions |
| **Round 1** | **4.6/5** | PASS (>= 4/5) |

---

## 2. Round 2 — 5-Whys: Tác động nếu chọn sai methodology?

```
W1: Điều gì xảy ra nếu chọn methodology quá lạc quan (underestimate noise)?
  → Noise sensitivity analysis cho kết quả "noise không thể giải thích Delta_chi2"
    nhưng thực tế noise CÓ THỂ.
    → P10-NOISE bị đóng SAI → Class C (genuine) public claim dựa trên false confidence.
    → Khi experimental group khác phân tích độc lập và tìm ra noise → CREDIBILITY COLLAPSE.

W2: Điều gì xảy ra nếu chọn methodology quá bi quan (overestimate noise)?
  → Noise sensitivity analysis cho kết quả "noise CÓ THỂ giải thích Delta_chi2"
    nhưng thực tế noise KHÔNG THỂ.
    → P10-NOISE vẫn OPEN → Class C bị downgrade hoặc giữ "ambiguous" vĩnh viễn.
    → K9_E có empirical evidence thật nhưng không được công nhận.
    → Tác động: MISSED OPPORTUNITY, không phải credibility damage.

W3: Tại sao false positive (underestimate) nguy hiểm hơn false negative (overestimate)?
  → Trong khoa học, claim sai (Type I error) gây hại NHIỀU HƠN bỏ lỡ (Type II error).
    → Nếu K9_E bị bỏ lỡ: 3-observer experiment vẫn là con đường phục hồi.
    → Nếu K9_E được claim sai: toàn bộ project mất credibility, không phục hồi được.
    → **Nguyên tắc: ERR ON THE SIDE OF CAUTION — methodology phải CONSERVATIVE.**

W4: Risk nào từ việc chọn methodology quá phức tạp?
  → Methodology phức tạp (parametric model nhiều tham số) tạo ra 2 rủi ro:
    (1) Overfitting: model noise fit data tốt hơn K9_E vì nhiều tham số hơn,
        nhưng không có ý nghĩa vật lý
    (2) Opacity: người đọc không hiểu methodology → không trust kết quả
    → **Nguyên tắc: SIMPLICITY — methodology phải đủ đơn giản để audit được.**

W5: ROOT CAUSE — Tác động của sai methodology?
  → **TYPE I ERROR (false claim noise đã được rule out) = FATAL cho project credibility.**
    TYPE II ERROR (false claim noise chưa được rule out) = DELAY, có thể phục hồi.
    → Methodology phải được thiết kế để BẢO VỆ CHỐNG TYPE I ERROR.
    → Điều này có nghĩa: conservative assumptions, upper-bound approach,
      explicit boundary conditions, và CLEAR STATEMENT về những gì analysis KHÔNG làm được.
```

### Round 2 Score: 4.9/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Type I vs Type II error analysis | 5/5 | Phân biệt rõ: false claim = fatal, missed opportunity = recoverable |
| Conservative principle | 5/5 | ERR ON THE SIDE OF CAUTION — đây là nguyên tắc thiết kế then chốt |
| Simplicity constraint | 5/5 | Methodology phức tạp → opacity → không trust được |
| Impact calibration | 4.5/5 | Credibility collapse là worst-case scenario đã được xác định |
| **Round 2** | **4.9/5** | PASS (>= 4/5) |

---

## 3. Round 3 — 5-Whys: Chọn methodology nào?

```
W1: Methodology nào thỏa mãn conservative + simplicity + chỉ dùng published data?
  → **Delta_chi2 Decomposition + Single-Setting Perturbation Analysis.**
    KHÔNG dùng parametric noise model.
    KHÔNG dùng bootstrap (vì error bars là Poisson, không capture systematic noise).
    KHÔNG dùng literature calibration (vì không có data cho Proietti setup cụ thể).
    → Approach: phân tích ĐỘ NHẠY của Delta_chi2 với perturbation tại TỪNG setting.

W2: Approach này hoạt động như thế nào?
  → 4 bước:
    B1: Decompose Delta_chi2 — mỗi setting đóng góp bao nhiêu vào lợi thế của K9_E?
    B2: Single-setting perturbation — cần shift 1 setting bao nhiêu sigma để Delta_chi2 < 1?
    B3: Identify worst-case noise pattern — pattern noise nào giả lập K9_E suppression
        hiệu quả nhất?
    B4: Multi-setting threshold — noise RMS tối thiểu (theo đơn vị sigma) để
        Delta_chi2 >= 5.35?
  → Output: "Noise must be at least X sigma per setting (RMS) to explain the K9_E signal."

W3: Tại sao approach này conservative?
  → Vì nó tính UPPER BOUND của noise sensitivity, không phải point estimate.
    → "Noise cần ít nhất X sigma" — nếu X > 3: noise không thể là nguyên nhân.
    → Nếu X < 1: ngay cả statistical noise cũng có thể giải thích.
    → Approach này KHÔNG giả định phân phối noise cụ thể → không bị model risk.
    → Approach này CHỈ dùng published data (4 values + error bars) → auditable.

W4: Approach này có limitation gì?
  → (1) KHÔNG phân biệt được statistical noise với systematic noise —
      error bars từ Proietti đã là Poisson, systematic component chưa được characterize.
  → (2) KHÔNG tính đến noise correlation giữa các settings —
      4 data points không mang thông tin về correlation.
  → (3) KHÔNG thay thế được 3-observer experiment —
      ngay cả khi PASS, vẫn cần independent confirmation.
  → **Tất cả limitations phải được ghi EXPLICIT trong spec và output.**

W5: ROOT CAUSE — Quyết định methodology?
  → **Delta_chi2 Decomposition + Noise Budget Analysis là methodology được chọn.**
    Lý do:
    (1) CONSERVATIVE: tính upper bound, không point estimate.
    (2) SIMPLE: 4 bước, mỗi bước có thể audit độc lập.
    (3) DATA-MINIMAL: chỉ dùng 4 values + 4 error bars từ Proietti Figure 3.
    (4) HONEST: explicit về những gì analysis KHÔNG làm được.
    (5) EX-ALIGNED: tận dụng 00065 (2BSM/1BSM ratio) như cross-check pattern.
    
    PASS/FAIL criteria:
    - PASS (đóng P10-NOISE):      Noise threshold > 3.0 sigma (RMS) —
      non-uniform noise không thể giải thích Delta_chi2 >= 5.35 ở > 2 sigma confidence
    - AMBIGUOUS (giữ OPEN):       Noise threshold 1.0–3.0 sigma —
      noise là plausible, cần 3-observer experiment để phân biệt
    - FAIL (downgrade Class C):   Noise threshold < 1.0 sigma —
      published error bars một mình có thể giải thích non-uniform pattern
    
    Decision rule: nếu AMBIGUOUS hoặc FAIL → thêm explicit boundary statement
    trong index.md: "'Genuine' claim is conditional on uniform noise assumption."
```

### Round 3 Score: 4.8/5

| Tiêu chí | Điểm | Ghi chú |
|----------|------|---------|
| Methodology clarity | 5/5 | 4 bước rõ ràng, mỗi bước có input/output xác định |
| Conservative principle upheld | 5/5 | Upper bound approach, không point estimate, không model risk |
| Limitations explicit | 5/5 | 3 limitations được liệt kê — correlation, systematic vs statistical, không thay thế experiment |
| PASS/FAIL criteria concrete | 4.5/5 | 3 bands (PASS/AMBIGUOUS/FAIL) với threshold số cụ thể |
| EX alignment | 4.5/5 | 00065 pattern cross-check được tích hợp |
| **Round 3** | **4.8/5** | PASS (>= 4/5) |

---

## 4. Tổng hợp 3-Round RCA

| Round | Focus | Score | Key Finding |
|-------|-------|-------|-------------|
| **R1** | Status — tại sao chưa có methodology? | **4.6/5** | 4 data points → underdetermination. Mọi noise model cần thêm assumptions. Phải chấp nhận và chọn approach an toàn nhất. |
| **R2** | Impact — nếu chọn sai methodology? | **4.9/5** | Type I error (false claim) = FATAL. Phải ERR ON THE SIDE OF CAUTION. Methodology phải conservative + simple. |
| **R3** | Decision — chọn methodology nào? | **4.8/5** | Delta_chi2 Decomposition + Noise Budget Analysis. 4 bước, PASS/AMBIGUOUS/FAIL criteria. |
| **Aggregate** | | **4.77/5** | **PASS (>= 4/5)** |

---

## 5. EX Compass Verification

### 5.1 EX intelligence applied trong methodology decision

| EX Node | Insight | Áp dụng vào methodology |
|---------|---------|------------------------|
| **00059** (Decoherence-Induced Registration Update) | BE Bhranti→Avisamvaditva→Prama spectrum: error-to-validity routing | Methodology phân biệt "noise as error" (invalidates K9_E) vs "noise as registration route" (compatible với K9_E) |
| **00065** (2BSM/1BSM Ratio) | Sharpest structural signature distinguishing K9_E from noise | Pattern cross-check: noise analysis output được compare với K9_E multiplicative prediction |
| **00064** (Genuine Fit — Evidence Node) | Evidence node classification — không phải conceptual bridge | Methodology tôn trọng evidence/data boundary: analysis là về data, không phải về model |
| **00062** (f_perp) | f_perp là mathematical construct, BE bridge indirect-2-level | Methodology không dùng BE concepts để motivate noise model — giữ technical purity |

### 5.2 EX gaps confirmed

| Gap | Impact | Mitigation |
|-----|--------|------------|
| Không EX node nào resolve P10-NOISE trực tiếp | Methodology phải stand-alone, không dựa vào EX | Đã làm — methodology chỉ dùng published data |
| g_eff=0.146 là modeling choice | Sensitivity analysis phải test sensitivity với g_eff | B4 sẽ scan g_eff values |
| N_QM_00061, N_QM_00068 centrality = 0.0 | Không có BE→noise bridge mạnh | Không cần — noise analysis là purely empirical |

---

## 6. Quyết định & Hành động

### 6.1 Quyết định

> **Methodology: Delta_chi2 Decomposition + Noise Budget Analysis.**
>
> KHÔNG parametric noise model. KHÔNG bootstrap. KHÔNG literature calibration.
> Approach: direct perturbation analysis trên 4 data points + error bars.
>
> **Nguyên tắc thiết kế:**
> 1. CONSERVATIVE — upper bound, không point estimate
> 2. SIMPLE — 4 bước, auditable từng bước
> 3. DATA-MINIMAL — chỉ dùng published Proietti Figure 3 data
> 4. HONEST — explicit về 3 limitations không thể vượt qua
>
> **PASS/FAIL:**
> - PASS (noise_threshold > 3.0 sigma RMS) → đóng P10-NOISE, H=5→3, Risk=18.0→10.8
> - AMBIGUOUS (1.0–3.0 sigma) → giữ OPEN, thêm boundary statement
> - FAIL (< 1.0 sigma) → downgrade Class C (genuine) → (qualified)

### 6.2 Hành động cụ thể

| # | Hành động | Ưu tiên | Effort | Output |
|---|----------|---------|--------|--------|
| **1** | Viết `noise_sensitivity_analysis.py` trong `07_fits/` | **P1 (BẮT BUỘC)** | 1-2 giờ | Python script, executable, có comment |
| **2** | Chạy analysis, generate output | **P1 (BẮT BUỘC)** | 15 phút | Console output + markdown report |
| **3** | Dựa trên kết quả: đóng P10-NOISE hoặc thêm boundary statement | **P1 (BẮT BUỘC)** | 15 phút | Update Top 10 + index.md |
| **4** | Cross-check với K9E-PAT pattern | P2 | 30 phút | Verify noise pattern vs K9_E multiplicative pattern |
| **5** | Nếu AMBIGUOUS: literature review về phase noise trong optical CHSH | P2 | 2-4 giờ | Literature summary |

### 6.3 Điều kiện đóng P10-NOISE (updated)

P10-NOISE có thể được đóng khi MỘT trong các điều kiện sau:

1. **Noise budget analysis PASS (> 3.0 sigma RMS):** Non-uniform noise không thể tạo ra Delta_chi2 >= 5.35 → **Gỡ `[AH-NOISE]`, H=5→3, Risk=18.0→10.8**
2. **3-observer experiment confirm:** K9_E signal được phát hiện độc lập → **Gỡ `[AH-NOISE]`, H=5→2**
3. **Raw event data obtained:** Phân tích noise correlation trực tiếp → **Gỡ `[AH-NOISE]`, H=5→2**

Điều kiện (1) được ưu tiên vì khả thi ngay với published data.

---

## 7. Methodology Specification (tóm tắt)

Xem chi tiết: `07_fits/noise_sensitivity_analysis_spec.md` (sẽ được tạo trong action #1)

### B1: Delta_chi2 Decomposition
- Input: 4 raw correlators, 4 error bars, QM-only best fit, K9_E best fit
- Output: Per-setting chi2 contribution table
- Question: Setting nào đóng góp nhiều nhất vào Delta_chi2?

### B2: Single-Setting Perturbation
- Input: K9_E best-fit parameters (V=0.939, beta=0.598)
- Method: Với mỗi setting, shift E_raw đi delta (theo đơn vị sigma) và re-fit
- Output: delta_threshold cho mỗi setting — cần shift bao nhiêu sigma để Delta_chi2 < 1?

### B3: Worst-Case Noise Pattern
- Input: 4 data points, error bars, QM and K9_E models
- Method: Grid search over noise vectors (eps_00, eps_01, eps_10, eps_11)
- Output: Noise pattern giả lập K9_E suppression hiệu quả nhất

### B4: Multi-Setting Noise Threshold
- Input: Kết quả B2 và B3
- Method: Tính RMS noise tối thiểu (theo đơn vị sigma) cần để Delta_chi2 >= 5.35
- Output: noise_threshold_RMS (đơn vị: sigma)

### Cross-Check với 2BSM/1BSM Pattern
- K9_E predicts: residual(2 BSM) / residual(1 BSM) ≈ 2
- Noise budget analysis: liệu worst-case noise pattern có tạo ra ratio ≈ 2 không?
- Nếu có → noise và K9_E hoàn toàn degenerate với 4 data points
- Nếu không → 2BSM/1BSM ratio vẫn là structural signature

---

## 8. 3-Round RCA Design Verification

| Round | Focus | Score | Key Verification |
|-------|-------|-------|-----------------|
| R1 | Is the methodology gap correctly diagnosed? | 4.6/5 | Underdetermination từ 4 data points được nhận diện là root cause. 3 approaches được so sánh. |
| R2 | Is the risk of wrong methodology correctly calibrated? | 4.9/5 | Type I > Type II. Conservative principle được establish làm design constraint. |
| R3 | Is the chosen methodology the right one? | 4.8/5 | Delta_chi2 decomposition — minimal assumptions, auditable, conservative. PASS/FAIL criteria concrete. |
| **Aggregate** | | **4.77/5** | **PASS (>= 4/5)** |

---

## 9. Kết luận

> **Methodology cho P10-NOISE noise sensitivity analysis đã được quyết định qua 3-Round RCA (aggregate 4.77/5).**
>
> **Approach:** Delta_chi2 Decomposition + Noise Budget Analysis — upper bound trên noise cần thiết để giải thích K9_E signal. KHÔNG parametric model, KHÔNG bootstrap, KHÔNG literature calibration.
>
> **Nguyên tắc:** CONSERVATIVE (ERR ON THE SIDE OF CAUTION) + SIMPLE (auditable) + HONEST (explicit limitations).
>
> **PASS threshold:** noise_threshold > 3.0 sigma RMS → P10-NOISE được đóng.
>
> **FAIL threshold:** noise_threshold < 1.0 sigma RMS → Class C downgrade.
>
> **AMBIGUOUS (1.0–3.0 sigma):** giữ OPEN, thêm boundary statement, chờ 3-observer experiment.
>
> **Kết quả của analysis này sẽ quyết định:** liệu Class C (genuine) empirical evidence có đứng vững trước noise alternative không, hay cần downgrade trước khi public.

---

*RCA P10-NOISE Methodology Decision — 2026-05-24. 3-Round RCA x 5-Why x Scoring Threshold 4/5. Aggregate: 4.77/5. VVV-QMRF scope, VVV-QMRF-EX as compass.*
