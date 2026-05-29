# RCA — Phân tích Lan truyền khi Đồng bộ 4 Chỗ lệch SOT

> **Ngày:** 2026-05-17  
> **Mục tiêu:** Xác định xem việc sửa 4 chỗ lệch giữa Mapping SOT và BIAN Index SOT có gây sai lan truyền đến `category/`, `framework/`, `meta_architecture/`, `synthesis/`.

---

## Phương pháp

Quét tất cả thuật ngữ bị ảnh hưởng bằng `grep_search` (exact + case-insensitive) trong 4 thư mục mục tiêu.

---

## Kết quả chi tiết

### Lệch 1 — BIAN-9: Thêm N_BE_00253 (Anupalabdhi) vào Mapping SOT

**Hiện trạng Mapping SOT:** `"(No separate node — abhāva/anupalabdhi)"`  
**BIAN Index SOT:** `N_BE_00253 (Anupalabdhi)`

| Thư mục | Kết quả tìm `N_BE_00253` | Dùng đúng? |
|---------|:------------------------:|:----------:|
| `category/` | **9 hit** (Cat 13 + Cat 01) | ✅ Đúng — gọi N_BE_00253 = Anupalabdhi, liên kết ED_BE_00116 |
| `framework/` | **1 hit** (E14) | ✅ Đúng — `BIAN-9 (SOT L38, N_BE_00253)` |
| `meta_architecture/` | **3 hit** (class_x_gap_triage) | ✅ Đúng — `N_BE_00253 (Anupalabdhi — Non-perception)` |
| `synthesis/` | **0 hit** | ✅ Không liên quan |

> **Phát hiện quan trọng:** Cả 3 thư mục **đã dùng** N_BE_00253 theo đúng BIAN Index SOT. Mapping SOT là file **duy nhất** ghi "No separate node". → Sửa Mapping SOT sẽ **khớp** với toàn bộ hệ thống.

**Phán quyết: AN TOÀN — sửa giúp đồng bộ, không gây mâu thuẫn.**

---

### Lệch 2 — BIAN-19: Thêm N_BE_00066 (Anātmavāda) vào Mapping SOT

**Hiện trạng Mapping SOT:** `"(No separate node — anātmavāda structural)"`  
**BIAN Index SOT:** `N_BE_00066 (Anātmavāda)`

| Thư mục | Kết quả tìm `N_BE_00066` | Dùng đúng? |
|---------|:------------------------:|:----------:|
| `category/` | **4 hit** (Cat 07) | ✅ Đúng — `N_BE_00066; support: N_BE_00029` |
| `framework/` | **4 hit** (E06) | ✅ Đúng — `N_BE_00066 = Anātmavāda confirmed` |
| `meta_architecture/` | **1 hit** (GCS) | ✅ Đúng — `N_BE_00066` trong bảng BIAN-19 |
| `synthesis/` | **3 hit** (S3) | ✅ Đúng — `N_BE_00066 (Anātmavāda)` |

> **Phát hiện:** Tất cả 4 thư mục **đã dùng** N_BE_00066. Mapping SOT ghi "No separate node" là bất đồng bộ duy nhất.

**Phán quyết: AN TOÀN — sửa giúp đồng bộ.**

---

### Lệch 3 — BIAN-20: Thêm N_BE_00021 vào Mapping SOT

**Hiện trạng Mapping SOT:** `"— (no node, reserved)"`  
**BIAN Index SOT:** `N_BE_00021 (Svabhāvapratibandha)`

| Thư mục | Kết quả tìm `BIAN-20` | Dùng đúng? |
|---------|:---------------------:|:----------:|
| `category/` | **1 hit** (index — lineage mention) | ✅ Chỉ reference range "BIAN-1–BIAN-20" |
| `framework/` | **0 hit** | ✅ Không liên quan |
| `meta_architecture/` | **2 hit** (GCS) | ✅ Đúng — `Reserved, Placeholder, not substantive` |
| `synthesis/` | **0 hit** | ✅ Không liên quan |

> **Phát hiện:** BIAN-20 là reserved cross-reference, xử lý qua BIAN-10. Meta_architecture ghi đúng "Reserved/Placeholder". Việc thêm node N_BE_00021 vào Mapping SOT chỉ **bổ sung thông tin**, không mâu thuẫn vì BIAN-10 trong Mapping SOT đã ghi N_BE_00021.

**Phán quyết: AN TOÀN — bổ sung, nhất quán với BIAN-10.**

---

### Lệch 4 — BIAN-3: Chuẩn hóa tên "Yogipratyakṣa" → "Alaukika pratyakṣa"

**Hiện trạng Mapping SOT:** `"Yogipratyakṣa"` (Pramāṇavāda naming)  
**BIAN Index SOT:** `"Alaukika pratyakṣa"` (Nyāya/general naming)

| Thư mục | "Yogipratyakṣa" | "Alaukika pratyakṣa" | Kết luận |
|---------|:---------------:|:--------------------:|----------|
| `category/` | 0 hit | **11 hit** (Cat 11) | Dùng "Alaukika" |
| `framework/` | 0 hit | **5 hit** (E12) | Dùng "Alaukika" |
| `meta_architecture/` | 0 hit | **4 hit** (class_x, GCS) | Dùng "Alaukika" |
| `synthesis/` | 0 hit | 0 hit | Không liên quan |

> **Phát hiện quan trọng:** Toàn bộ hệ thống **đã dùng** "Alaukika pratyakṣa", không file nào dùng "Yogipratyakṣa". Mapping SOT dùng "Yogipratyakṣa" là ngoại lệ duy nhất.

> [!NOTE]
> **Giải thích ngôn ngữ học:** Cả hai tên đều chỉ N_BE_00012, nhưng:
> - "Yogipratyakṣa" = yogic perception (thuật ngữ Pramāṇavāda hẹp — chỉ yogic)
> - "Alaukika pratyakṣa" = extraordinary perception (thuật ngữ rộng hơn, bao gồm cả yogic)
> 
> Hệ thống VVV-QMRF sử dụng "Alaukika" vì nó map đến *limit-faculty* registration (weak measurement), không chỉ riêng yogic.

**Phán quyết: AN TOÀN — sửa Mapping SOT để dùng "Alaukika pratyakṣa" sẽ khớp với tất cả file downstream.**

---

## Ma trận Tổng hợp

```
              category/   framework/   meta_arch/   synthesis/
Lệch 1 (BIAN-9)   ✅*          ✅*          ✅*          ✅
Lệch 2 (BIAN-19)  ✅*          ✅*          ✅*          ✅*
Lệch 3 (BIAN-20)  ✅           ✅           ✅           ✅
Lệch 4 (BIAN-3)   ✅*          ✅*          ✅*          ✅

✅  = Không tìm thấy thuật ngữ bị ảnh hưởng / không liên quan
✅* = TÌM THẤY thuật ngữ — dùng ĐÚNG theo BIAN Index SOT
     → Sửa Mapping SOT sẽ ĐỒNG BỘ chứ không gây mâu thuẫn
```

---

## Kết luận RCA

> [!IMPORTANT]
> **Tất cả 4 chỗ lệch đều an toàn để sửa trong Mapping SOT.** 
> 
> Hơn thế, **3 trong 4 lệch** (BIAN-9, BIAN-19, BIAN-3) cho thấy Mapping SOT là file **lạc hậu** — tất cả các file downstream đã dùng phiên bản đúng theo BIAN Index SOT. Sửa Mapping SOT **giải quyết bất đồng bộ**, không tạo ra lỗi mới.

### Hành động cụ thể trên Mapping SOT

| Lệch | Dòng | Sửa gì | Rủi ro |
|:----:|:----:|--------|:------:|
| 1 (BIAN-9) | L865 | `"(No separate node — abhāva/anupalabdhi)"` → `N_BE_00253 (Anupalabdhi)` | **0** |
| 2 (BIAN-19) | L875 | `"(No separate node — anātmavāda structural)"` → `N_BE_00066 (Anātmavāda)` | **0** |
| 3 (BIAN-20) | L876 | `"—"` → `N_BE_00021 (Svabhāvapratibandha — reserved cross-ref to BIAN-10)` | **0** |
| 4 (BIAN-3) | L859 | `"Yogipratyakṣa"` → `"Alaukika pratyakṣa"` (cả node table L72) | **0** |
