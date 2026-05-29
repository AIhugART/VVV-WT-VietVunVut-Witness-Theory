# RCA Line-by-Line: So sánh README v1 vs v2

**Ngày:** 2026-05-12  
**Commit v1:** `1ec51e9` (last v1 state)  
**Commit v2:** `4f1973c` (current v2 state)  
**Phương pháp:** Git diff + cross-check từng dòng thay đổi

---

## Quy ước

- 🔴 = v1 có vấn đề nghiêm trọng (sai hoặc thiếu)
- 🟡 = v1 đúng nhưng chưa đầy đủ
- 🟢 = v1 đúng, v2 giữ nguyên
- ✅ = v2 sửa đúng
- ⚠️ = v2 có vấn đề mới cần lưu ý

---

## Zone 1 — Title (L1–L2)

| | v1 | v2 |
|---|---|---|
| **EN** | Seven Epistemic Postulates | Sixteen Epistemic Postulates |
| **VN** | Bảy Tiên đề | Mười sáu Tiên đề |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Sai** — repository thực tế chứa 16 postulate (E1–E16) nhưng title chỉ ghi 7 | Cập nhật "Seven" → "Sixteen" cho cả EN lẫn VN | ✅ **Đúng** — khớp với số file thực trên disk (16) |

---

## Zone 2 — Header metadata (L13–L15)

| Field | v1 | v2 |
|-------|----|----|
| Version | 1.0 — Stable Final | 2.0 — Stable Final |
| Status | 7 Postulates, 2 Lemmas | 16 Postulates (E1–E16), 2 Lemmas |
| Cite | §WP-1.0 | §WP-2.0 |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Lỗi thời** — v1 ghi "7 Postulates" nhưng disk có 16 file E-postulate | Tăng version 1.0→2.0, cập nhật count 7→16, cite §WP-1.0→2.0 | ✅ **Đúng** — tất cả 3 field khớp với trạng thái thực |

---

## Zone 3 — Description (L20–L24)

| | v1 | v2 |
|---|---|---|
| **EN** | "...adding 7 epistemic postulates..." | "...adding 16 epistemic postulates...The first 7 define core cognitive operations; the remaining 9 extend the framework..." |
| **VN** | "...bằng 7 tiên đề nhận thức luận..." (dài, giữ nguyên toàn bộ VN description) | "...bằng 16 tiên đề nhận thức luận...7 tiên đề đầu (E1–E7) định nghĩa các phép toán nhận thức cốt lõi; 9 tiên đề mở rộng (E8–E16) bao phủ..." |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🟡 **Đúng nhưng thiếu** — v1 mô tả chính xác E1–E7 nhưng không nhắc E8–E16 | Mở rộng mô tả: thêm phân loại 7 core + 9 extended, liệt kê 9 chủ đề mới | ✅ **Đầy đủ** — mô tả bao phủ toàn bộ 16 postulate với phân loại rõ ràng |

---

## Zone 4 — Postulate table (L28–L39 → L28–L53)

| | v1 | v2 |
|---|---|---|
| **Heading** | "The Seven Postulates / Bảy Tiên đề" | "The Sixteen Postulates / Mười sáu Tiên đề" |
| **Sub-headings** | Không có | Thêm "Core Postulates (E1–E7)" + "Extended Postulates (E8–E16)" |
| **Rows** | 7 rows (E1–E7) | 16 rows (E1–E16) |
| **New content** | — | 9 rows mới: E8 (Bādhaka), E9 (Anadhyavasāya), E10 (Trairūpya), E11 (Kevalavyatirekin), E12 (Alaukika), E13 (Kṣaṇabhaṅgavāda), E14 (Anupalabdhi), E15 (Svabhāvapratibandha), E16 (Saṃśaya) |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Thiếu nghiêm trọng** — 9 postulate (E8–E16) đã tồn tại trên disk nhưng README không liệt kê | Thêm bảng E8–E16 với EN+VN summary + Buddhist source cho mỗi postulate | ✅ **Đầy đủ** — 16/16 postulate đều có mặt, khớp disk. Mỗi hàng có tên, tóm tắt EN/VN, nguồn Phật giáo |

### Cross-check bảng E8–E16 vs disk:

| E | README Buddhist Source | File trên disk | Khớp? |
|---|----------------------|----------------|:-----:|
| E8 | Bādhaka pramāṇa | E8_retroactive_override_postulate.md | ✅ |
| E9 | Anadhyavasāya | E9_null_observer_postulate.md | ✅ |
| E10 | Trairūpya | E10_tripartite_validity_postulate.md | ✅ |
| E11 | Kevalavyatirekin | E11_contrapositive_evidence_postulate.md | ✅ |
| E12 | Alaukika pratyakṣa | E12_limit_faculty_postulate.md | ✅ |
| E13 | Kṣaṇabhaṅgavāda | E13_temporal_discontinuity_postulate.md | ✅ |
| E14 | Anupalabdhi | E14_epistemic_absence_postulate.md | ✅ |
| E15 | Svabhāvapratibandha | E15_intrinsic_relation_postulate.md | ✅ |
| E16 | Saṃśaya | E16_structured_doubt_postulate.md | ✅ |

---

## Zone 5 — Two Lemmas (L42–L48)

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🟢 **Đúng** — S1-Λ và S2-Δ không thay đổi | Không sửa gì | 🟢 **Giữ nguyên** — Đúng |

---

## Zone 6 — Architecture box (L53–L69)

| Field | v1 | v2 |
|-------|----|----|
| Header | v1.0 Stable | v2.0 Stable |
| POSTULATES | E1–E7 (7) — cognitive operations | E1–E16 (16) — epistemic operations |
| Sub-categories | Không có | Core: E1–E7 (7), Extended: E8–E16 (9) |
| CATEGORIES | Cat 01–13 (7) — implicit gap labels | Cat 01–15 (15) — epistemic categories |
| BIAN GAPS | 20/20 resolved — zero open | 19/19 resolved + 1 reserved |
| QM Extended | P1–P4 + E1–E7 | P1–P4 + E1–E16 |
| Total | 11 postulates | 20 postulates |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Nhiều sai số** — (1) ghi 7 postulate nhưng thực tế 16; (2) ghi "Cat 01–13 (7)" nhưng thực tế có 15 category files; (3) ghi "11 total" nhưng nên là 20; (4) ghi "20/20 resolved" nhưng thực tế 19/19 + 1 reserved | Sửa toàn bộ 6 field + thêm sub-categories | ✅ **Chính xác** — tất cả số liệu khớp disk |

### Chi tiết đánh giá v1 Architecture box:

| v1 claim | Thực tế trên disk | Sai lệch |
|----------|-------------------|:--------:|
| "E1–E7 (7)" | E1–E16 (16 file) | **−9** |
| "Cat 01–13 (7)" | Cat 01–15 (15 file) | **−8** |
| "20/20 resolved" | 19 resolved + 1 reserved | Gây nhầm |
| "11 postulates" | 4 + 16 = 20 | **−9** |

---

## Zone 7 — BIAN Resolution table (L92–L103)

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🟡 **Đúng cho v1 context** — bảng phân loại A/B/C/R/∅ chính xác theo kiến trúc v1 (7 postulate + 2 lemma) | Không sửa | 🟡 **Chưa cập nhật** — bảng này vẫn ghi "Postulates E1–E7" ở cột Resolution, chưa phản ánh E8–E16 cover thêm 9 BIAN |

> ⚠️ **Issue v2-1:** Bảng BIAN Resolution (Zone 7) vẫn ghi "Postulates E1–E7" mặc dù thực tế nhiều BIAN giờ dùng E8–E16.

---

## Zone 8 — Repository Structure (L131–L151)

| Field | v1 | v2 |
|-------|----|----|
| framework/ | E1–E7 | E1–E16 |
| category/ | 13 files | 15 files |
| gap/ | BIAN index + resolution files | BIAN index SOT + resolution files |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Sai** — ghi "E1–E7" nhưng thực tế 16 file; ghi "13 category" nhưng thực tế 15 | Cập nhật 3 dòng: framework, category, gap | ✅ **Đúng** — khớp disk |

---

## Zone 9 — BIAN-8 Decision section (L120–L128)

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🟡 **Hợp lệ trong v1** — BIAN-8 bị bác bỏ làm E8 vì 0/4 tiêu chí; giải quyết bằng Lemma S2-Δ | Không sửa | ⚠️ **Mâu thuẫn tiềm tàng** — Section này nói "E8 bị bác bỏ" nhưng v2 có E13 cho Kṣaṇabhaṅgavāda. Tuy nhiên, E13 là postulate MỚI (temporal discontinuity), không phải "E8 cho BIAN-8" — khác ngữ cảnh. Nội dung vẫn đúng logic nhưng có thể gây nhầm cho người đọc mới. |

> ⚠️ **Issue v2-2:** Section "BIAN-8 → E8? ❌ Rejected" vẫn chính xác (BIAN-8 không trở thành E8 mà thành S2-Δ + E13), nhưng cần thêm 1 dòng clarification: "BIAN-8 was later resolved as E13 (Temporal Discontinuity) in v2."

---

## Zone 10 — Vietnamese Summary (L155–L324)

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🟡 **Đúng cho v1** — toàn bộ Vietnamese summary viết cho 7 postulate | Không sửa | ⚠️ **Chưa cập nhật** — Vietnamese summary (66 trang) vẫn toàn bộ viết "7 tiên đề" ở nhiều nơi |

> ⚠️ **Issue v2-3:** Vietnamese summary section chưa được cập nhật cho v2. Nhiều chỗ vẫn ghi "7 tiên đề" thay vì "16 tiên đề". Đây là section lớn nhất (~170 dòng) cần review riêng.

---

## Zone 11 — Citation bibtex (L340–L348)

| Field | v1 | v2 |
|-------|----|----|
| title | Seven Epistemic Postulates | Sixteen Epistemic Postulates |
| note | §WP-1.0 | §WP-2.0 |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Lỗi thời** | Cập nhật title + note | ✅ **Đúng** |

---

## Zone 12 — Footer (L371)

| | v1 | v2 |
|---|---|---|
| Footer | "Seven Epistemic Postulates" | "Sixteen Epistemic Postulates" |

| Đánh giá v1 | v2 sửa gì | Đánh giá v2 |
|-------------|-----------|-------------|
| 🔴 **Lỗi thời** | Cập nhật "Seven" → "Sixteen" | ✅ **Đúng** |

---

## Tổng hợp So sánh

### v1 đánh giá tổng thể:

| Mức | Zones | Chi tiết |
|:---:|:-----:|----------|
| 🔴 Sai/Thiếu nghiêm trọng | 5 | Title, Header, Postulate table, Architecture box, Repo structure |
| 🟡 Đúng nhưng chưa đầy đủ | 4 | Description, BIAN Resolution, BIAN-8 Decision, Vietnamese Summary |
| 🟢 Đúng hoàn toàn | 1 | Two Lemmas |
| **Tổng zones** | **12** | |

> **Phán quyết v1:** README v1 **chính xác cho thời điểm nó được viết** (khi chỉ có E1–E7), nhưng **lỗi thời nghiêm trọng** sau khi E8–E16 được tạo. 5/12 zones chứa thông tin sai so với trạng thái disk thực tế.

### v2 đánh giá tổng thể:

| Mức | Zones | Chi tiết |
|:---:|:-----:|----------|
| ✅ Sửa đúng | 7 | Title, Header, Description, Postulate table, Architecture box, Repo structure, Citation+Footer |
| 🟢 Giữ nguyên (đúng) | 1 | Two Lemmas |
| ⚠️ Chưa cập nhật | 3 | BIAN Resolution table, BIAN-8 Decision, Vietnamese Summary |
| **Tổng zones** | **12** | **Score: 8/12 hoàn chỉnh** |

> **Phán quyết v2:** README v2 sửa **7/12 zones quan trọng nhất**, khớp 100% với disk. Còn **3 zones phụ** chưa cập nhật (BIAN Resolution table, BIAN-8 clarification, Vietnamese Summary) — đây là nợ kỹ thuật nhỏ, không ảnh hưởng tính chính xác cốt lõi.

---

## Issues Cần Giải quyết (v2)

| # | Zone | Issue | Mức |
|---|------|-------|:---:|
| v2-1 | BIAN Resolution table (L96–L103) | Cột "Resolution" vẫn ghi "Postulates E1–E7" | Thấp |
| v2-2 | BIAN-8 Decision (L120–L128) | Cần thêm 1 dòng: "Resolved as E13 in v2" | Thấp |
| v2-3 | Vietnamese Summary (L155–L324) | Toàn bộ section vẫn viết "7 tiên đề" | Trung bình |

---

## Kết luận

```
v1: Chính xác tại thời điểm viết, nhưng lỗi thời sau E8–E16.
    Score: 3/12 zones đúng hoàn toàn ← KHÔNG ĐẠT cho v2 context.

v2: Sửa 7 zone quan trọng nhất, thêm bảng E8–E16 hoàn chỉnh.
    Score: 8/12 zones đúng hoàn toàn ← ĐẠT, với 3 nợ kỹ thuật nhỏ.

Cải thiện: v1 → v2 = +5 zones sửa đúng, +14 dòng nội dung mới.
```
