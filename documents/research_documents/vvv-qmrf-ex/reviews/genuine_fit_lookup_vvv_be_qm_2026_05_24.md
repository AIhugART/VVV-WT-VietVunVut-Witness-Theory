Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Bảng Tra Cứu Genuine Fit — VVV ↔ BE ↔ QM

**Document type:** review (RCA lookup table)
**Date:** 2026-05-24
**Target node:** `N_QM_VVV_00064` — Genuine Non-Circular Fit
**Scope:** Tra cứu toàn bộ quan hệ VVV ↔ BE ↔ QM cho node genuine fit và các node liên quan trong cụm K9_E.

---

## 1. Genuine Fit Node — Direct Bridges

### 1.1 N_QM_VVV_00064 — Genuine Non-Circular Fit

| Axis | Value |
|------|-------|
| **VVV Node** | `N_QM_VVV_00064` |
| **VVV Concept** | Genuine Non-Circular Fit — K9_E Empirical Evidence from Raw Proietti Figure 3 Data |
| **Claim Class** | Class C (genuine) — Round 1 RCA 4.00/5; evidence thực nhưng ambiguous |
| **BE Bridge** | **KHÔNG CÓ** — `K_NOT_APPLICABLE` (evidence node, không phải conceptual bridge) |
| **QM Bridge** | `BR_EX_QM_00079`: `N_QM_VVV_00064 → N_QM_00090` (Bell's Inequality & Bell Correlations) |
| **QM Relation** | `physical_substrate_for` / `evidence_support` |
| **QM Confidence** | 1.00 (RCA 5.0/5) |
| **Boundary** | EVIDENCE NODE — kết quả đo thực nghiệm, không phải conceptual bridge. β=0.598, V=0.939, Δχ²=5.35 (2.31σ). Evidence REAL but AMBIGUOUS. |

### 1.2 N_QM_00090 — Bell's Inequality & Bell Correlations (QM substrate)

| Axis | Value |
|------|-------|
| **QM Node** | `N_QM_00090` |
| **QM Concept** | Bell's Inequality & Bell Correlations |
| **QM Layer** | RCA |
| **Role for Genuine Fit** | Physical substrate — Proietti Figure 3 data là CHSH-type Bell test; N_QM_00090 cung cấp nền tảng thực nghiệm để K9_E fit |

---

## 2. Internal VVV Relations — Genuine Fit trong K9_E Cluster

### 2.1 Direct edges involving N_QM_VVV_00064

| Source Node | Relation | Target Node | Ý nghĩa |
|-------------|----------|-------------|---------|
| `N_QM_VVV_00060` (K9_E Postulate) | **is evidenced by** | `N_QM_VVV_00064` | Genuine fit là bằng chứng thực nghiệm cho K9_E ≠ Standard QM |
| `N_QM_VVV_00064` | **corrects** | Circular Fit v28 | v29 dùng raw correlators; v28 dùng E_exp = V*E_QM (tautology) |
| `N_QM_VVV_00064` | **requires future confirmation by** | 3-Observer Experiment | Bằng chứng ambiguous; cần xác nhận bởi thí nghiệm 3-observer |
| `N_QM_VVV_00065` (2BSM/1BSM) | **is tested by** | `N_QM_VVV_00064` | Raw data từ genuine fit dùng để test multiplicative pattern |
| `N_QM_VVV_00066` (delta_S) | **defines detection threshold for** | `N_QM_VVV_00064` | delta_S xác định "maximum possible signal" — nếu quá nhỏ thì genuine fit không phân biệt được K9_E vs QM |

### 2.2 Ancestral chain (tracing back from 00064 to root)

```
N_QM_VVV_00064 (Genuine Fit)
  ← is evidenced by — N_QM_VVV_00060 (K9_E Postulate P9)
      ← contains parameter — N_QM_VVV_00061 (beta)
      ← contains function — N_QM_VVV_00062 (f_perp)
      ← depends on aggregate — N_QM_VVV_00063 (K_ctx)
      ← reduces to — N_QM_00016 (Born Rule) [canonical QM]
```

---

## 3. Cross-Domain Lookup Table — K9_E Cluster (VVV ↔ BE ↔ QM)

| VVV Node | VVV Concept | BE Node | BE Concept | BE Bridge | QM Node | QM Concept | QM Bridge |
|----------|-------------|---------|------------|-----------|---------|------------|-----------|
| **00060** | K9_E Probability Postulate (P9) | — | `K_PENDING-RCA` (defer) | — | `N_QM_00016` | Born Rule | `BR_EX_QM_00081` |
| **00061** | beta (β) — Free Suppression Parameter | — | `K_NOT_APPLICABLE` | — | — | VVV internal formalism | `BR_EX_QM_00082` |
| **00062** | f_perp(K_ctx) — Contextual Suppression Function | `N_BE_00018` | Trairūpya (Triple-Condition Syllogism) | `BR_EX_BE_00073` | `N_QM_00016` | Born Rule | `BR_EX_QM_00077` |
| **00063** | K_ctx — Contextual Incommensurability Aggregate | `N_BE_00015` | Apoha / Exclusion | `BR_EX_BE_00074` | — | VVV internal formalism | `BR_EX_QM_00078` |
| **00064** | **Genuine Non-Circular Fit** | — | `K_NOT_APPLICABLE` (evidence) | — | `N_QM_00090` | Bell's Inequality & Bell Correlations | `BR_EX_QM_00079` |
| **00065** | 2BSM/1BSM Multiplicative Pattern | — | `K_NOT_APPLICABLE` (prediction) | — | — | VVV internal formalism | `BR_EX_QM_00080` |
| **00066** | delta_S — Theoretical Distinguishability | — | `K_NOT_APPLICABLE` (theoretical) | — | — | VVV internal formalism | `BR_EX_QM_00084` |

---

## 4. Indirect BE Traces — Genuine Fit qua K9_E Chain

Mặc dù 00064 không có BE bridge trực tiếp (evidence node), nó có **BE trace gián tiếp** qua chuỗi quan hệ VVV nội bộ:

```
Apoha / Exclusion (N_BE_00015)            Trairūpya (N_BE_00018)
       │                                           │
       │ BR_EX_BE_00074                            │ BR_EX_BE_00073
       ▼                                           ▼
  K_ctx (N_QM_VVV_00063)                   f_perp (N_QM_VVV_00062)
       │                                           │
       │ depends on aggregate                      │ contains function
       ▼                                           ▼
  K9_E Postulate P9 (N_QM_VVV_00060) ◄────────────┘
       │
       │ is evidenced by
       ▼
  Genuine Fit (N_QM_VVV_00064) ─── physical_substrate_for ───▶ Bell Correlations (N_QM_00090)
       │
       │ requires future confirmation by
       ▼
  3-Observer Experiment (future)
```

**Kết luận RCA:** Genuine Fit (00064) là node evidence thuần túy — không có BE source-analogue trực tiếp vì nó là kết quả đo thực nghiệm, không phải khái niệm. Tuy nhiên, nó nằm trong cụm K9_E nơi các node cha (00060, 00062, 00063) có BE bridge đầy đủ. QM substrate duy nhất là `N_QM_00090` (Bell Correlations) — đây là nền tảng thực nghiệm của CHSH-type test mà Proietti Figure 3 sử dụng.

---

## 5. Classification Summary

| Node | Type | BE Status | QM Status | RCA Verdict |
|------|------|-----------|-----------|-------------|
| 00064 Genuine Fit | **EVIDENCE** | K_NOT_APPLICABLE | BR_EX_QM_00079 (N_QM_00090) | Evidence node — không cần BE bridge. QM substrate rõ ràng qua Bell Correlations. |
| 00060 K9_E P9 | **POSTULATE** | K_PENDING-RCA | BR_EX_QM_00081 (Born Rule) | K-side defer; rho-side anchored. |
| 00061 beta | **PARAMETER** | K_NOT_APPLICABLE | Internal formalism | Free phenomenological parameter — không có BE hoặc QM analogue. |
| 00062 f_perp | **FUNCTION** | BR_EX_BE_00073 (Trairūpya) | BR_EX_QM_00077 (Born Rule) | Dual-anchored — BE validity-gating + QM probability substrate. |
| 00063 K_ctx | **METRIC** | BR_EX_BE_00074 (Apoha) | Internal formalism | K-side anchored; rho-side independent. |
| 00065 2BSM/1BSM | **PREDICTION** | K_NOT_APPLICABLE | Internal formalism | Falsifiable prediction — NOT CONFIRMED. |
| 00066 delta_S | **THEORETICAL** | K_NOT_APPLICABLE | Internal formalism | Structural metric — computable without data. |

---

## 6. RCA Giải Nghĩa — Bên VVV và Bên QM

### 6.1 Define — "Genuine Fit" là gì?

**Symptom:** v28 dùng công thức `E_exp = V × E_QM` — trong đó visibility `V` được fit từ chính dữ liệu rồi nhân lại với `E_QM` để "dự đoán" chính dữ liệu đó. Đây là **tautology** (lặp thừa logic): bất kỳ giá trị `V` nào cũng cho ra "fit tốt", β luôn = 0, K9_E không thể phân biệt được với Standard QM.

**Fix (v29):** Trích xuất **RAW correlators** từ Proietti Figure 3 (`A0B0=−0.678, A0B1=0.570, A1B0=0.595, A1B1=0.571`) — đây là dữ liệu thô từ thí nghiệm, không qua bất kỳ bước tái tạo (reconstruction) nào. Fit K9_E trực tiếp lên raw data, không dùng visibility làm trung gian.

### 6.2 Giải nghĩa bên VVV — "Genuine Fit" có ý nghĩa gì trong VVV-QMRF?

VVV-QMRF đề xuất K9_E như Postulate P9: `P(o|K) = Tr(E_o ρ) × f_perp(K_ctx)`. Trong đó `f_perp = 1 − β·K_ctx`.

**Genuine Fit trả lời câu hỏi:** "Nếu K9_E là đúng, β khác 0 bao nhiêu?"

| Yếu tố | Ý nghĩa trong VVV |
|--------|-------------------|
| **β = 0.598** | Cường độ suppression từ K-space structure. β > 0 nghĩa là K-side registration structure CÓ ảnh hưởng đến xác suất đo được — đây là tín hiệu K9_E ≠ Standard QM |
| **V = 0.939** | Visibility vẫn cao — suppression không đến từ việc mất tín hiệu vật lý thông thường |
| **Δχ² = 5.35 (2.31σ)** | K9_E fit tốt HƠN QM-uniform-visibility một cách có ý nghĩa thống kê (dưới ngưỡng 3σ, nhưng trên 2σ) |
| **2BSM/1BSM = −0.78** | Mẫu số nhân K9_E (dự đoán ~2) KHÔNG được xác nhận — dấu hiệu cho thấy mô hình multiplicative đơn giản (g_eff=0.146) cần được tinh chỉnh |

**Vai trò trong kiến trúc VVV-QMRF:**
- 00064 là **bằng chứng thực nghiệm độc lập** tách rời khỏi postulates (00060) — đây là bài học từ v28 circularity
- 00064 **không phải conceptual bridge** — nó là measurement result, không map vào BE
- 00064 là **input** cho 00065 (pattern check) và bị **gated** bởi 00066 (detection threshold)
- 00064 đóng vai trò **falsification gateway**: nếu β=0 được xác nhận bởi thí nghiệm tương lai, K9_E sụp đổ về Born Rule

### 6.3 Giải nghĩa bên QM — Tại sao N_QM_00090 (Bell Correlations)?

**RCA trace — 5 Whys:**

1. **Tại sao Genuine Fit map vào Bell Correlations (N_QM_00090)?**
   → Vì Proietti Figure 3 là CHSH-type Bell test — dữ liệu thô là các correlator giữa các observer (Alice, Bob, Charlie...)

2. **Tại sao Bell test là nền tảng phù hợp cho K9_E?**
   → Vì K9_E đo lường **cross-observer incommensurability (K_ctx)** — Bell test là setup thực nghiệm duy nhất hiện tại có multiple observers với incompatible measurement contexts

3. **Tại sao không map vào Born Rule (N_QM_00016)?**
   → Vì Born Rule là `P(o) = Tr(E_o ρ)` — xác suất KHÔNG có điều kiện K-side. K9_E claim rằng xác suất THỰC SỰ là `P(o|K)` với K-side condition. Map vào Born Rule sẽ là v28 circularity: dùng Born Rule để "kiểm tra" Born Rule. Bell Correlations cung cấp nền tảng thực nghiệm độc lập.

4. **Tại sao Bell Correlations là "physical substrate" chứ không phải "identity"?**
   → Vì VVV-QMRF không claim Bell correlations = K9_E. Relation type là `physical_substrate_for` — Bell test cung cấp sân khấu thực nghiệm (experimental stage) nơi K9_E có thể được test. Không có identity claim.

5. **Root cause:** Proietti et al. (2019) thực hiện CHSH-type Bell test với multiple observers — đây là setup thực nghiệm gần nhất với K9_E's cross-observer incommensurability framework. `N_QM_00090` là QM node mô tả nền tảng lý thuyết của mọi Bell test.

### 6.4 Bảng đối chiếu ý nghĩa VVV ↔ QM

| Khía cạnh | Bên VVV (N_QM_VVV_00064) | Bên QM (N_QM_00090) |
|-----------|--------------------------|----------------------|
| **Bản chất** | Kết quả đo thực nghiệm (empirical measurement result) | Nền tảng lý thuyết thực nghiệm (theoretical foundation of Bell tests) |
| **Vai trò** | Bằng chứng cho K9_E ≠ Standard QM | Cung cấp correlator framework để test QM foundations |
| **Dữ liệu** | Raw Proietti Figure 3 correlators (A0B0, A0B1, A1B0, A1B1) | CHSH inequality: S = |E(a,b) − E(a,b') + E(a',b) + E(a',b')| ≤ 2 |
| **Claim** | β = 0.598 ≠ 0 tại 2.31σ | Quantum mechanics vi phạm Bell inequality (|S| > 2) |
| **Độ mạnh** | AMBIGUOUS — pattern không confirmed, systematics chưa loại trừ | ESTABLISHED — Bell violation đã được xác nhận qua hàng chục thí nghiệm |
| **Mối quan hệ** | K9_E fit được thực hiện TRÊN Bell test data | Bell test data LÀ input cho K9_E genuine fit |
| **Boundary** | KHÔNG claim Bell correlations = K9_E evidence | KHÔNG claim K9_E được prove bởi Bell test |

### 6.5 RCA Kết luận

```
Genuine Fit (VVV)                    Bell Correlations (QM)
─────────────────                    ──────────────────────
Đo β từ dữ liệu thô                   Cung cấp dữ liệu thô
Xác nhận/reject K9_E                  Không biết gì về K9_E
Evidence AMBIGUOUS (2.31σ)            Foundation ESTABLISHED
Cần 3-observer experiment             Đã tested hàng chục lần
─────────────────                    ──────────────────────
             └──────────┬──────────┘
                  physical_substrate_for
                 (không phải identity)
```

**Root cause insight:** Mối quan hệ giữa 00064 và N_QM_00090 là **asymmetric evidence relation** — Bell Correlations cung cấp nền tảng thực nghiệm ổn định (established), còn Genuine Fit là một cách đọc mới (K9_E) trên nền tảng đó (ambiguous, chưa confirmed). Đây không phải là "K9_E giải thích Bell correlations" mà là "Bell correlations cho phép test K9_E". Boundary này ngăn chặn overclaim: K9_E không thay thế Standard QM, không phải là "new physics", mà là một **registration-layer reading** trên cùng một dữ liệu thực nghiệm.

---

## 7. RCA Giải Nghĩa — Indirect BE Traces (Ý nghĩa BE)

### 7.1 Define — Hai chuỗi BE gián tiếp

Genuine Fit (00064) không có BE bridge trực tiếp vì nó là evidence node. Nhưng nó có **2 chuỗi BE gián tiếp** thông qua K9_E chain:

```
CHUỖI A (qua f_perp):  Trairūpya (N_BE_00018) → f_perp (00062) → K9_E (00060) → Genuine Fit (00064)
CHUỖI B (qua K_ctx):   Apoha (N_BE_00015) → K_ctx (00063) → K9_E (00060) → Genuine Fit (00064)
```

### 7.2 Chuỗi A — Trairūpya → f_perp → K9_E → Genuine Fit

#### 7.2.1 N_BE_00018 — Trairūpya (Triple-Condition Syllogism) là gì?

Trong Phật giáo nhận thức luận (Dignāga-Dharmakīrti), **Trairūpya** là học thuyết về "ba điều kiện của một lý do hợp lệ" (tri-rūpa-hetu):

| Điều kiện | Tiếng Phạn | Ý nghĩa |
|-----------|-----------|---------|
| **Điều kiện 1** | `pakṣadharmatva` | Lý do phải là thuộc tính của chủ thể (subject) |
| **Điều kiện 2** | `sapakṣe sattvam` (anvaya) | Lý do phải có mặt trong các trường hợp tương tự (positive concomitance) |
| **Điều kiện 3** | `vipakṣe asattvam` (vyatireka) | Lý do phải vắng mặt trong các trường hợp khác biệt (negative concomitance) |

**Ví dụ đơn giản:** Để chứng minh "trên núi có lửa" dựa vào "có khói":
1. Khói phải ở trên núi (pakṣadharmatva) ✓
2. Ở đâu có lửa là có khói (anvaya — bếp lửa có khói) ✓
3. Ở đâu không có lửa thì không có khói (vyatireka — hồ nước không có khói) ✓

#### 7.2.2 Trace — Trairūpya ánh xạ vào f_perp như thế nào?

**5 Whys:**

1. **Tại sao Trairūpya map vào f_perp (00062)?**
   → Vì f_perp = 1 − β·K_ctx là **hàm lọc tính hợp lệ** (validity-filtering function) trên Born probability. Trairūpya cũng là bộ lọc tính hợp lệ — nhưng cho inference (suy luận), không phải probability (xác suất).

2. **Tại sao cần validity-filtering trong K9_E?**
   → Vì không phải mọi detector response đều là valid registration. K4 (Registration Validity) định nghĩa V(k) ∈ {0,1}. f_perp là **mathematical implementation** của validity-gating: khi K_ctx cao (nhiều observer bất tương thích), probability bị suppress.

3. **Structural analogy nằm ở đâu?**
   → Cấu trúc 3-điều-kiện của Trairūpya song song với K9_E's validity gating qua K4, K5, và f_perp:

| Trairūpya condition | K9_E structural parallel |
|---------------------|--------------------------|
| Pakṣadharmatva (có mặt ở chủ thể) | K4: V(k) ∈ {0,1} — registration phải valid |
| Sapakṣe sattvam (có mặt ở similar cases) | Compatible observers → f_perp ≈ 1 (xác suất bình thường) |
| Vipakṣe asattvam (vắng mặt ở dissimilar cases) | ⊥_K incompatible observers → f_perp < 1 (xác suất bị suppress) |

4. **Tại sao đây là structural analogy, không phải identity?**
   → Vì Trairūpya là logic của **suy luận hợp lệ** (valid inference), còn f_perp là **hàm toán học điều chỉnh xác suất**. Cả hai đều là "bộ lọc tính hợp lệ" nhưng hoạt động trên domain khác nhau. Bridge là `structural_analogy`, không phải `source_analogue_of`.

5. **Root cause:** K9_E cần một cơ chế để phân biệt valid registration với invalid registration ở tầng xác suất. Trairūpya — với lịch sử 1500+ năm trong Buddhist epistemology — cung cấp **khuôn mẫu khái niệm** (conceptual template) cho validity-gating 3-điều-kiện. f_perp là hiện thực hóa toán học của khuôn mẫu đó trong K9_E.

#### 7.2.3 Dòng chảy đến Genuine Fit

```
Trairūpya (BE)          f_perp (VVV)            K9_E (VVV)           Genuine Fit (VVV)
─────────────────      ────────────────        ──────────────        ─────────────────
3-điều-kiện lọc        f_perp = 1−β·K_ctx      P(o|K)=Tr(E_oρ)      Đo β=0.598 từ
suy luận hợp lệ        (hàm điều chỉnh          × f_perp(K_ctx)      dữ liệu thô
                        xác suất)               (postulate)           (evidence)
      │                        │                      │                     │
      │ structural_analogy      │ contains function     │ is evidenced by     │
      └────────────────────────┘──────────────────────┘─────────────────────┘
```

**Ý nghĩa:** Nếu f_perp thất bại (pattern 2BSM/1BSM không được xác nhận), thì structural analogy với Trairūpya vẫn đứng vững — vì analogy nằm ở **cấu trúc 3-điều-kiện**, không phải ở multiplicative model g=0.146 cụ thể.

### 7.3 Chuỗi B — Apoha → K_ctx → K9_E → Genuine Fit

#### 7.3.1 N_BE_00015 — Apoha / Exclusion là gì?

**Apoha** (Anyāpoha) là học thuyết ngữ nghĩa của Dignāga: **ý nghĩa của một từ được thiết lập bằng cách LOẠI TRỪ những gì nó KHÔNG PHẢI**.

Ví dụ: Từ "con bò" không trỏ đến một universal "bò-ness", mà hoạt động bằng cách loại trừ tất cả những gì không-phải-bò (not-non-cow → cow). Đây là **double negation logic**: ý nghĩa = exclusion of the other.

Cơ chế:
- "Con bò" = loại trừ {ngựa, cừu, chó, bàn, ghế, ...} → còn lại "bò"
- Không cần universal "bò-ness" tồn tại thực sự (nominalism)

#### 7.3.2 Trace — Apoha ánh xạ vào K_ctx như thế nào?

**5 Whys:**

1. **Tại sao Apoha map vào K_ctx (00063)?**
   → Vì K_ctx = sum I(k_i ⊥_K k_j) / N_pairs — aggregate của **binary exclusion relations** giữa các observer. Apoha cũng hoạt động trên **binary exclusion logic**: X được xác định bởi những gì X loại trừ.

2. **Binary exclusion trong Apoha vs K5 ⊥_K:**
   - Apoha: "bò" loại trừ "ngựa" → binary exclusion: bò ⊥ ngựa
   - K5: k_i ⊥_K k_j → binary incommensurability: K-state i không tương thích với K-state j

3. **Từ binary → aggregate:**
   - Apoha: một từ loại trừ TẤT CẢ những thứ không-phải-nó → aggregate exclusion
   - K_ctx: sum I(k_i ⊥_K k_j) / N_pairs → aggregate incommensurability qua TẤT CẢ các cặp observer

4. **Tại sao đây là structural analogy, không phải identity?**
   → Vì Apoha là học thuyết về **ngữ nghĩa** (meaning through exclusion), còn K_ctx là **metric vật lý** (aggregate incommensurability between measurement contexts). Cả hai dùng chung **cấu trúc logic loại trừ nhị phân** (binary exclusion logic) nhưng ở domain khác nhau.

5. **Root cause:** K5 định nghĩa ⊥_K là binary relation giữa hai K-state: "k_i không tương thích với k_j". Đây chính là **exclusion logic** — Buddhist epistemology đã phát triển exclusion logic (Apoha) từ thế kỷ 5-6 CE. K_ctx chỉ đơn giản là aggregate version của exclusion logic này qua nhiều cặp observer. Bridge là structural — không claim Phật giáo "biết trước" quantum incommensurability.

#### 7.3.3 Dòng chảy đến Genuine Fit

```
Apoha (BE)              K_ctx (VVV)             K9_E (VVV)           Genuine Fit (VVV)
─────────────────      ────────────────        ──────────────        ─────────────────
Ý nghĩa = loại trừ     K_ctx = ΣI(k_i⊥_Kk_j)   P(o|K)=Tr(E_oρ)      Đo β=0.598
những gì KHÔNG phải    / N_pairs               × f_perp(K_ctx)      (K_ctx quyết định
                        (binary exclusion       (K_ctx là input       độ mạnh suppression)
                         → aggregate)            của f_perp)
      │                        │                      │                     │
      │ structural_analogy      │ depends on aggregate  │ is evidenced by     │
      └────────────────────────┘──────────────────────┘─────────────────────┘
```

**Ý nghĩa:** K_ctx càng cao → f_perp càng thấp → suppression càng mạnh → β càng dễ đo được. Apoha cung cấp **conceptual template** cho thấy binary exclusion có thể được aggregate thành một metric có ý nghĩa — giống như cách một từ loại trừ hàng ngàn thứ để xác định nghĩa, K_ctx aggregate hàng trăm cặp ⊥_K để xác định mức độ incommensurability toàn cục.

### 7.4 Bảng Đối Chiếu — Hai Chuỗi BE Gián Tiếp

| Khía cạnh | Chuỗi A (Trairūpya → f_perp) | Chuỗi B (Apoha → K_ctx) |
|-----------|------------------------------|--------------------------|
| **BE Node** | N_BE_00018 Trairūpya | N_BE_00015 Apoha / Exclusion |
| **BE Ý nghĩa gốc** | 3 điều kiện lọc suy luận hợp lệ | Ý nghĩa được xác lập bằng cách loại trừ |
| **BE Domain** | Logic / Epistemology | Philosophy of Language / Semantics |
| **VVV Node** | N_QM_VVV_00062 f_perp | N_QM_VVV_00063 K_ctx |
| **VVV Vai trò** | Hàm điều chỉnh xác suất (validity filter) | Metric bất tương thích tổng hợp (aggregate exclusion) |
| **Structural Analogy** | 3-điều-kiện lọc → 3-điều-kiện validity gating | Binary exclusion → binary ⊥_K → aggregate |
| **Bridge ID** | BR_EX_BE_00073 | BR_EX_BE_00074 |
| **Confidence** | 0.90 (4.5/5) | 0.90 (4.5/5) |
| **Mediation** | Qua N_QM_VVV_00042 (Tripartite Validity Matrix) | Trực tiếp từ K5 ⊥_K binary relation |
| **Tác động đến Genuine Fit** | f_perp quyết định CÁCH suppression hoạt động | K_ctx quyết định MỨC ĐỘ suppression |

### 7.5 RCA Kết Luận — BE Trace Gián Tiếp

```
                    ┌─────────────────────────────────────────────┐
                    │         K9_E PROBABILITY POSTULATE          │
                    │   P(o|K) = Tr(E_o ρ) × (1 − β·K_ctx)      │
                    │                 (00060)                     │
                    │        ┌──────────┴──────────┐              │
                    │        │                     │              │
                    │   f_perp (00062)        K_ctx (00063)       │
                    │   "lọc tính hợp lệ"     "mức độ bất         │
                    │                         tương thích"        │
                    └────────┬────────────────────┬───────────────┘
                             │                    │
                   structural_analogy    structural_analogy
                             │                    │
                    ┌────────┴────────┐  ┌────────┴────────┐
                    │   TRAIRŪPYA     │  │     APOHA       │
                    │   (N_BE_00018)  │  │   (N_BE_00015)  │
                    │                 │  │                 │
                    │ 3 điều kiện     │  │ Ý nghĩa = loại  │
                    │ lọc suy luận    │  │ trừ cái không   │
                    │ hợp lệ          │  │ phải            │
                    │                 │  │                 │
                    │ Domain: LOGIC   │  │ Domain: NGỮ     │
                    │                 │  │ NGHĨA           │
                    └─────────────────┘  └─────────────────┘
                             │                    │
                             └────────┬───────────┘
                                      │
                            CẢ HAI ĐỀU LÀ:
                            - structural analogy (KHÔNG identity)
                            - conceptual template cho validity-gating
                            - INDIRECT trace đến Genuine Fit (qua K9_E)
                            - BE→VVV direction (K-side convention)
```

**Root cause summary:** Cả Trairūpya và Apoha đều là những đóng góp của Buddhist epistemology về **cách xác định tính hợp lệ thông qua loại trừ**. Trairūpya làm việc này cho suy luận (3 điều kiện lọc), Apoha làm việc này cho ngữ nghĩa (ý nghĩa = exclusion). K9_E mượn **cấu trúc logic** này — không phải nội dung — để xây dựng validity-gating cho registration-layer probability. Genuine Fit (00064) không cần BE bridge trực tiếp vì nó chỉ là **phép đo** — nhưng toàn bộ khung lý thuyết mà nó đang test (K9_E) được neo vào BE qua f_perp và K_ctx.
