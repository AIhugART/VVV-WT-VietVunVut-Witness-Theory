# RCA Hard Check: Kiểm tra từng dòng báo cáo "Tại sao nhiều framework"

**Ngày:** 2026-05-12  
**File kiểm tra:** `achives/review/RCA_bao_cao_tai_sao_nhieu_framework.md` (147 dòng)  
**Phương pháp:** Cross-check từng tuyên bố sự kiện (fact claim) với SOT + disk

---

## Quy ước

- ✅ = Tuyên bố chính xác, khớp với bằng chứng
- ⚠️ = Tuyên bố gần đúng nhưng có lỗi nhỏ về số liệu
- ❌ = Tuyên bố sai hoặc gây hiểu nhầm nghiêm trọng

---

## Kiểm tra từng dòng

### Phần 1 — Câu hỏi cốt lõi (L1–L11)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L10 | "9 E-postulate mới (E8–E16)" | Disk: E8, E9, E10, E11, E12, E13, E14, E15, E16 = 9 file | ✅ |
| L10 | "5 category mới" | Disk: limit_faculty_perception, temporal_discontinuity_doctrine, epistemic_absence_cognition, intrinsic_relational_binding, pre_measurement_indeterminacy = 5 file | ✅ |

### Phần 2 — Nguyên nhân gốc rễ (L14–L40)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L19 | "Hệ thống 263 nút" | `system_be_full.md` header xác nhận 263 nodes | ✅ |
| L20 | "105 khái niệm QM" | `QM_Measurement_Unified_Concept_Table.md` header xác nhận 105 | ✅ |
| L22 | "20 nhãn BIAN" | SOT Part 1: BIAN-1 → BIAN-20 = 20 dòng | ✅ |
| L24 | "chỉ có 7 E-postulate (E1–E7) được tạo" | Trước phiên: E1–E7 đã có trên disk = 7 file → đúng | ✅ |
| L24 | "13 BIAN chưa có giải pháp framework chính thức" | 20 tổng − 7 E-postulate = 13? **Không chính xác.** E1–E7 cover 9 BIAN (2,4,5,6,7,16,17,18,19). BIAN-1 có Lemma S1-Λ riêng. Vậy 20 − 1(Lemma) − 9(E1–E7) − 1(Reserved) = **9 BIAN chưa có framework**, không phải 13. Nhưng nếu đếm BIAN chưa được SOT ghi nhận resolved thì = 19 (tất cả trừ BIAN-1). Báo cáo lẫn lộn giữa "file chưa tạo" vs "SOT chưa ghi nhận". | ⚠️ |
| L35 | "Tầng 1: Lemma S1-Λ" | SOT L30 xác nhận BIAN-1 = Lemma S1-Λ | ✅ |
| L36 | "Tầng 2-7, 16-19: Có bản vẽ + cột (E1-E7) — SOT chưa ghi nhận" | Đúng: 9 BIAN có pipeline đầy đủ nhưng SOT cũ ghi Open | ✅ |
| L37 | "Tầng 12-15: Có bản vẽ, CHƯA có cột" | Đúng: 4 category files đã tồn tại, chưa có E-postulate | ✅ |
| L38 | "Tầng 3, 8-11: Chưa có gì cả" | Đúng: Không có category lẫn framework cho 5 BIAN này trước phiên | ✅ |
| L39 | "Tầng 20: Dự trữ" | SOT L49: 🔒 Reserved | ✅ |

### Phần 3 — Diễn biến 3 giai đoạn (L44–L83)

#### Giai đoạn A (L46–L52)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L48 | "9 BIAN (2,4,5,6,7,16,17,18,19) ĐÃ được giải quyết từ trước" | SOT Part 5 L269 xác nhận: 9 BIAN → Resolved de facto | ✅ |
| L50 | "Không cần tạo file mới" | Đúng — chỉ cập nhật SOT status | ✅ |
| L52 | "10 BIAN đã giải quyết (1 + 9)" | 1 (BIAN-1) + 9 (đợt audit) = 10 → đúng | ✅ |
| L52 | "Còn lại 9 BIAN chưa xong + 1 dự trữ" | 20 − 10 − 1(reserved) = 9 → đúng | ✅ |

#### Giai đoạn B (L54–L67)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L56 | "BIAN-12,13,14,15 đã có category/ nhưng CHƯA có E-postulate" | Disk: retroactive_epistemic_override.md ✅, null_observer_event.md ✅, tripartite_validity_matrix.md ✅, contrapositive_quantum_evidence.md ✅; E8–E11 chưa tồn tại trước phiên | ✅ |
| L62 | "BIAN-12 → Bādhaka pramāṇa → E8" | SOT L41 + L68: Cat 03 + E8 | ✅ |
| L63 | "BIAN-13 → Anadhyavasāya → E9" | SOT L42 + L69: Cat 06 + E9 | ✅ |
| L64 | "BIAN-14 → Trairūpya → E10" | SOT L43 + L70: Cat 09 + E10 | ✅ |
| L65 | "BIAN-15 → Kevalavyatirekin → E11" | SOT L44 + L71: Cat 01 + E11 | ✅ |
| L67 | "14 BIAN giải quyết" | 10 + 4 = 14 → đúng | ✅ |

#### Giai đoạn C (L69–L83)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L71 | "Năm BIAN-3,8,9,10,11 CHƯA có gì" | Đúng — không có category lẫn framework trước phiên | ✅ |
| L73 | "tạo 10 file mới (5 category + 5 framework)" | Disk: 5 cat mới + 5 E mới = 10 | ✅ |
| L77 | "BIAN-3 → Alaukika → Cat 11 + E12" | SOT L32 + L59 khớp | ✅ |
| L78 | "BIAN-8 → Kṣaṇabhaṅgavāda → Cat 12 + E13" | SOT L37 + L64 khớp | ✅ |
| L79 | "BIAN-9 → Anupalabdhi → Cat 13 + E14" | SOT L38 + L65 khớp | ✅ |
| L80 | "BIAN-10 → Svabhāvapratibandha → Cat 14 + E15" | SOT L39 + L66 khớp | ✅ |
| L81 | "BIAN-11 → Saṃśaya → Cat 15 + E16" | SOT L40 + L67 khớp | ✅ |
| L83 | "19/19 BIAN giải quyết" | SOT Part 4 L227: 19 Resolved | ✅ |

### Phần 4 — Tổng hợp (L87–L116)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L91 | "Mỗi BIAN phải qua 3 tầng" | Quy tắc kiến trúc VVV-EQM — gap → category → framework | ✅ |
| L105 | "Viết E1–E7 cho 10 BIAN dễ nhất" | E1–E7 phục vụ 9 BIAN (2,4,5,6,7,16,17,18,19) — **không phải 10**. BIAN-1 dùng Lemma S1-Λ, không dùng E-postulate. | ⚠️ |
| L113 | "E8 (phủ quyết kết quả đo) hoàn toàn khác E9 (đo mà không nhận thông tin)" | Đúng — E8 = Bādhaka (override), E9 = Anadhyavasāya (null observer) | ✅ |
| L114 | "E14 (nhận thức vắng mặt) khác E11 (nhận thức bằng loại trừ)" | Đúng — E14 = Anupalabdhi (absence cognition), E11 = Kevalavyatirekin (contrapositive) | ✅ |

### Phần 5 — Thống kê (L120–L129)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L124 | "Category mới tạo: 5" | Disk: 5 file mới (limit_faculty, temporal_discontinuity, epistemic_absence, intrinsic_relational, pre_measurement) | ✅ |
| L125 | "E-postulate mới tạo: 9 (E8–E16)" | Disk: 9 file mới (E8–E16) | ✅ |
| L126 | "SOT cập nhật: 4 lần" | Git log: 4 commits sửa SOT — có thể xem là 4 lần | ✅ |
| L127 | "Lineage header sửa lỗi: 6 file" | Thực tế: phiên sửa lineage cho retroactive (E3→E8), null_observer (E6→E9), tripartite (E3→E10 rồi 01→09), contrapositive (—→E11 rồi 09→01) = **4 file sửa lineage tên E-postulate + 2 file sửa số category** = 6 lượt sửa trên 4 file. Con số "6 file" gây hiểu nhầm — đúng hơn là "6 lượt sửa trên 4 file". | ⚠️ |
| L128 | "Git commits: 4" | Git log: commit b0d740e, 426e73e, c161270, 748f9b2 = 4 → đúng | ✅ |
| L129 | "Tổng file mới: 14" | 5 category + 9 E-postulate = 14 | ✅ |

### Phần 6 — Kết luận (L133–L147)

| Dòng | Tuyên bố | Kiểm chứng | Verdict |
|:----:|----------|-----------|:-------:|
| L139 | "9 BIAN chưa có E-postulate + 5 BIAN chưa có gì → 14 file phải tạo" | 4 BIAN Partial (cần E-postulate) + 5 BIAN Open (cần cả cat + E) = 4 + (5+5) = 14. **Nhưng báo cáo viết "9 BIAN chưa có E-postulate" — sai.** 4 BIAN chưa có E-postulate (12-15), 5 BIAN chưa có gì (3,8,9,10,11). Tổng BIAN cần hành động = 9, tổng file phải tạo = 14. Phân tách "9 BIAN → 14 file" thì đúng, nhưng cách diễn đạt "9 BIAN chưa có E-postulate" bao gồm cả 5 BIAN cũng chưa có category — gây nhập nhằng. | ⚠️ |
| L144 | "Trước phiên: 10/20 Resolved, 4/20 Partial, 5/20 Open, 1/20 Reserved" | Thực tế lúc đầu phiên, SOT ghi: 1 Resolved (BIAN-1) + 19 Open. Con số "10/20 Resolved" là trạng thái *de facto* (file tồn tại trên disk) nhưng chưa được SOT ghi nhận. Ý đúng nhưng thiếu clarification — SOT lúc đầu chỉ ghi 1 Resolved. | ⚠️ |
| L145 | "Sau phiên: 19/20 Resolved, 1/20 Reserved" | SOT Part 4 L227-L230 xác nhận: 19 Resolved, 0 Partial, 0 Open, 1 Reserved | ✅ |

---

## Tổng kết phát hiện

| Mức | Số lượng | Chi tiết |
|:---:|:--------:|----------|
| ✅ Chính xác | 32 | Tuyệt đại đa số tuyên bố khớp với bằng chứng |
| ⚠️ Gần đúng | 5 | Lỗi số liệu nhỏ hoặc diễn đạt gây nhập nhằng |
| ❌ Sai nghiêm trọng | 0 | Không có |

### Chi tiết 5 lỗi ⚠️

| # | Dòng | Vấn đề | Mức nghiêm trọng |
|---|:----:|--------|:-----------------:|
| 1 | L24 | "13 BIAN chưa có giải pháp" — lẫn lộn giữa "file chưa tạo" vs "SOT chưa ghi nhận" | Thấp |
| 2 | L105 | "E1–E7 cho 10 BIAN dễ nhất" — thực tế E1-E7 cover 9 BIAN, BIAN-1 dùng Lemma | Thấp |
| 3 | L127 | "6 file" sửa lineage — thực tế là 6 lượt sửa trên 4 file | Thấp |
| 4 | L139 | "9 BIAN chưa có E-postulate" — diễn đạt nhập nhằng (4 partial + 5 open) | Thấp |
| 5 | L144 | "Trước phiên: 10/20 Resolved" — là de facto, SOT lúc đó chỉ ghi 1 | Thấp |

---

## Phán quyết cuối cùng

> **Báo cáo ĐÚNG VỀ BẢN CHẤT.** Logic nhân-quả chính xác: nợ kỹ thuật tích lũy → buộc phải tạo 14 file trong một phiên. 5 lỗi ⚠️ đều là sai số liệu nhỏ hoặc diễn đạt mơ hồ, không ảnh hưởng đến kết luận chính. Không có lỗi nghiêm trọng nào.
