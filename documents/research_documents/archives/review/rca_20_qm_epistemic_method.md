# RCA: Tại sao xác định 20 QM concepts liên quan đến epistemic act?

> **Kết luận trước:** Con số "20" là **sai phương pháp**. Báo cáo trước bị lỗi logic.  
> **Kết luận đúng:** Mapping SOT map **53 BE tier items** → mô tả QM prose, KHÔNG dùng N_QM codes.

---

## 1. Lỗi phương pháp đã xảy ra

### Script trước làm gì?
```
Với mỗi QM concept (105 cái):
  → Tìm keyword (tên concept) trong toàn bộ text Mapping SOT
  → Nếu tìm thấy → đếm là "có mapping"
  → Nếu không → đếm là "không có mapping"
```

### Vấn đề:

| Lỗi | Giải thích |
|-----|------------|
| **False Positive** | Keyword "Measurement" xuất hiện **99 lần** trong file vì đó là chủ đề chính — không có nghĩa N_QM_00019 được formal mapping |
| **False Positive** | "Spin" xuất hiện 4 lần trong mô tả ví dụ ("spin, energy, position") — không phải mapping N_QM_00053 |
| **False Positive** | "Quantum Channel" (N_QM_00035) được tính nhưng thực tế 0 lần xuất hiện |
| **False Positive** | "Copenhagen Interpretation" (N_QM_00093) chỉ nhắc đến trong metadata, không có mapping |
| **Granularity sai** | Keyword matching không phân biệt "được map formal" vs "được nhắc thoáng qua" |

### Kết quả sửa lỗi (đợt 2):

| Verdict | Số lượng | Ví dụ |
|---------|:--------:|-------|
| FORMAL (keyword trong `**Quantum Measurement:**` block) | **18** | Quantum State, Born Rule, Observable |
| MENTION (chỉ nhắc trong metadata) | **1** | Copenhagen Interpretation |
| FALSE POSITIVE (0 lần xuất hiện) | **1** | Quantum Channel |

Nhưng ngay cả con số "18 FORMAL" vẫn sai — vì lý do ở phần 2 dưới đây.

---

## 2. Cấu trúc thật sự của Mapping SOT

### Mapping SOT KHÔNG phải là bảng N_QM ↔ N_BE

Mapping SOT có cấu trúc:

```
Mỗi tier section (53 cái):
  ├── ## T1.01 — [BE concept name]
  ├── **Node:** N_BE_XXXXX — [Sanskrit term]
  ├── **Inbound edges:** ...
  ├── **Outbound edges:** ...
  ├── - **Buddhist Epistemology:** [mô tả chi tiết BE]
  ├── - **Quantum Measurement:** [mô tả tự do QM tương ứng]  ← PROSE, không có N_QM code
  └── - **Correspondence type:** Strong / Medium / Weak / BIAN-n
```

> [!IMPORTANT]
> ### Phát hiện cốt lõi
> 
> **Mapping SOT là bảng BE-driven**, không phải QM-driven:
> - Cột bên trái: 53 BE tier items, mỗi cái có `N_BE_XXXXX` formal code
> - Cột bên phải: mô tả QM **bằng prose tự do**, KHÔNG có `N_QM_XXXXX` code
> - Không có node-to-node cross-system mapping `N_BE → N_QM`

### Ví dụ cụ thể

**T1.01 — Pramāṇa:**
- BE side: `N_BE_00001` (formal code) ✅
- QM side: *"Observable / Hermitian operator, with generalized measurement represented by POVM elements and Kraus operators..."* — prose mô tả, **không có** N_QM_00017 ❌

**T1.02 — Pratyakṣa:**
- BE side: `N_BE_00002` (formal code) ✅
- QM side: *"Eigenvalue readout. The singular, definite numerical outcome produced by a projective measurement..."* — prose mô tả, **không có** N_QM_00014 ❌

---

## 3. Tại sao script tìm ra 18 keyword?

Vì prose mô tả QM **tự nhiên** dùng các thuật ngữ QM chuẩn:

| Keyword tìm thấy | Ngữ cảnh thật | Có phải mapping formal? |
|-------------------|---------------|:-----------------------:|
| "Quantum State" | *"QM describes the system-side state as superposition or **quantum state**"* | ❌ Chỉ là mô tả |
| "Born Rule" | *"outcome probabilities governed by the **Born rule**"* | ❌ Chỉ là tham chiếu |
| "Hilbert Space" | *"pre-measurement state in **Hilbert space**"* | ❌ Chỉ là bối cảnh |
| "Entanglement" | *"Quantum **entanglement** constitutes a non-causal correlation"* | ⚠️ BIAN-10 reverse gap |
| "Decoherence" | *"**decoherence** as an analogy to kṣaṇikavāda"* | ⚠️ BIAN-8 gap discussion |

### Phân loại đúng

Trong 18 keyword "FORMAL", thực tế:

| Loại | Số | Mô tả |
|------|:--:|-------|
| **QM thuật ngữ nền** | ~10 | "Measurement", "Observable", "Quantum State", "Superposition", "Wave Function"... — dùng để **mô tả** phía QM, không phải mapping riêng |
| **QM concept có structural analogy** | ~5 | "Born Rule", "Projective Measurement", "Density Matrix", "Null Measurement", "Generalized Measurement" — được so sánh trực tiếp với BE |
| **QM concept trong BIAN gap** | ~3 | "Entanglement" (BIAN-10), "Heisenberg Cut" (BIAN-17/19), "Decoherence" (BIAN-8/13/17) — được nhắc đến vì **không có** BE tương đương |

---

## 4. Câu trả lời đúng cho câu hỏi gốc

### "QM system có mà BE system không có"

**Câu trả lời đúng không phải dựa trên keyword matching**, mà phải dựa trên cấu trúc:

#### 4a. BIAN Index đã trả lời câu này

BIAN Index có **20 entries**, trong đó:
- **19 entries**: BE có mà QM không có (BE → QM gap)
- **1 entry** (BIAN-10): QM có mà BE không có (QM → BE **reverse gap**)

```
BIAN-10: Non-Classical Correlation Relation
  QM concept: Entanglement correlation
  BE status: Không có tương đương trong Pramāṇavāda
  Phân loại: REVERSE GAP (QM → BE)
```

#### 4b. Mapping SOT section "Correspondence type" trả lời chi tiết hơn

Trong 53 tier sections, mỗi cái có `**Correspondence type:**` nói rõ mức độ mapping:

| Correspondence type | Ý nghĩa | QM concept status |
|----|---------|---------|
| **Strong** | Tương đồng cấu trúc cao | QM có BE tương đương |
| **Medium** | Tương đồng rõ ràng nhưng không formal | QM có BE tương tự |
| **Weak** | Chỉ so sánh gần nhất | QM gần như không có BE |
| **BIAN-n** | Gap chính thức | QM hoặc BE thiếu |

#### 4c. 105 N_QM codes thì sao?

105 N_QM codes **không nằm trong Mapping SOT** vì:
1. Mapping SOT dùng **BE node codes** (N_BE), không dùng QM node codes (N_QM)
2. QM Unified Concept Table là **bảng tham khảo độc lập**, không phải bên phải của mapping
3. Framework không thiết kế mapping N_QM ↔ N_BE 1:1 vì hai hệ thống **không đẳng cấu** (non-isomorphic)

---

## 5. Tóm tắt RCA

```
RCA Level 1: Tại sao script cho ra 20?
  → Keyword matching trên prose text, không phải formal node matching.

RCA Level 2: Tại sao keyword matching sai?
  → Mapping SOT không chứa N_QM codes; QM phía bên phải là mô tả prose tự do.

RCA Level 3: Tại sao Mapping SOT không chứa N_QM codes?
  → Thiết kế BE-driven: mỗi tier bắt đầu từ BE concept, QM chỉ là mô tả so sánh.

RCA Level 4: Tại sao không N_QM ↔ N_BE 1:1?
  → Hai hệ thống không đẳng cấu — BE có 53 tiers / 30 nodes / 39 edges;
     QM có 105 concepts / 11 categories — cấu trúc hoàn toàn khác nhau.

RCA Level 5 (Root Cause):
  → Framework VVV-QMRF là REGISTRATION LAYER, không phải translation layer.
     Nó không dịch QM sang BE hay ngược lại.
     Nó đăng ký (register) điểm tương đồng và điểm khác biệt ở lớp nhận thức luận.
```

> [!WARNING]
> ### Đính chính
> Báo cáo trước ([qm_without_be_mapping.md](file:///C:/Users/PC/.gemini/antigravity/brain/ea8c9085-1a7b-43e8-b01b-81c22b105901/artifacts/qm_without_be_mapping.md)) có kết luận "20 QM mapped, 85 not mapped" — con số này **sai phương pháp**.
> 
> **Đúng:** Mapping SOT map **53 BE tier items** → **53 QM prose descriptions**. Không có mapping N_QM ↔ N_BE node-level. Câu hỏi "QM có mà BE không có" được trả lời chính xác nhất qua **BIAN-10 (reverse gap)** — chỉ có **1** QM concept chính thức không có BE tương đương: **Entanglement**.
