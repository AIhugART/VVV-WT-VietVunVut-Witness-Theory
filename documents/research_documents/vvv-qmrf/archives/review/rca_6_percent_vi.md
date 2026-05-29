# 6% còn lại là gì?

> 94% BE blocks tham chiếu ≥1 concept khác. Vậy 6% (3 blocks) là gì?

---

## Đính chính con số

Khi tìm chính xác hơn (dùng cả Unicode diacritics), kết quả thay đổi:

| Số cross-references | Số blocks | Tỷ lệ |
|:--------------------:|:---------:|:------:|
| **0 refs** | **1** | **2%** |
| **1 ref** | **8** | **15%** |
| **2+ refs** | **44** | **83%** |

Vậy **98% có ít nhất 1 cross-reference**, và chỉ **1 block duy nhất** không nhắc concept khác nào trong phần mô tả.

---

## 1 block = 0 refs: T5.03 — Pakṣa

```
T5.03 — Pakṣa (Chủ thể logic / Trường hợp đang xét)

Mô tả BE: "Chủ thể của suy luận. Thực thể mà 
   phát biểu suy luận hướng đến. Quả đồi, trong 
   suy luận kinh điển: quả đồi có lửa vì có khói."
```

### Tại sao không tham chiếu concept khác?

**Vì Pakṣa là "cái bàn" — nơi mọi thứ đặt lên.**

```
Ví dụ minh họa:

  "Quả đồi (pakṣa) có lửa (sādhya) vì có khói (liṅga)"
       ↑                    ↑                ↑
    Cái bàn             Món ăn           Đũa/thìa
```

Pakṣa giống **cái bàn** — bạn không cần giải thích cái bàn bằng cách nhắc đến món ăn hay đũa. Cái bàn tự nó đã rõ: *"nơi đặt mọi thứ"*.

### Nhưng Pakṣa vẫn bị khóa!

Dù mô tả prose không nhắc concept khác, **edge graph** vẫn khóa nó:

```
N_BE_00016 (Liṅga) ──qualifies──→ N_BE_00017 (Pakṣa)
```

Pakṣa **nhận input** từ Liṅga — không có liṅga thì pakṣa vô nghĩa (bàn trống không có gì đặt lên). Vậy nó vẫn thuộc hệ thống đóng — chỉ là **phần mô tả** đơn giản đến mức không cần nhắc tên concept khác.

---

## 8 blocks = 1 ref: Các subtype và khái niệm đơn giản

| Tier | Tên | Ref duy nhất | Tại sao chỉ 1? |
|------|-----|:------------:|-----------------|
| T1.04 | Indriyajñāna (giác quan) | pratyakṣa | Subtype của pratyakṣa — chỉ cần nói "tôi thuộc pratyakṣa" |
| T1.08 | Svārtha anumāna (suy luận cho mình) | anumāna | Subtype của anumāna |
| T2.01 | Ākāra (hình thức biểu hiện) | ākāra | Tự tham chiếu tên mình |
| T2.04 | Vyavasāya (phán đoán xác định) | pratyakṣa | Kết quả sau pratyakṣa |
| T2.08 | Savikalpaka pratyakṣa (tri giác có khái niệm) | kalpanā | Đối lập của nirvikalpaka |
| T3.07 | Sāmānya (thuộc tính chung) | svalakṣaṇa | Đối lập của svalakṣaṇa |
| T5.11 | Asiddha hetvābhāsa (ngụy biện vô căn) | liṅga | Subtype của hetvābhāsa |
| T6.04 | Anātmavāda (vô ngã) | pramāṇa | Meta-concept, chỉ cần 1 neo |

### Quy luật chung

Ba loại block ít tham chiếu:

```
Loại 1: CỰC ĐƠN GIẢN — Pakṣa
  → "Tôi là cái bàn" — tự giải thích
  
Loại 2: SUBTYPE — Indriyajñāna, Svārtha anumāna, Asiddha
  → "Tôi là con của X" — chỉ cần nhắc cha mẹ
  
Loại 3: ĐỐI LẬP — Savikalpaka, Sāmānya  
  → "Tôi là cái ngược lại của X" — chỉ cần nhắc đối thủ
```

> **Ví dụ:** Trong gia đình, **ông bà** (pramāṇa, pratyakṣa) cần giải thích bằng nhiều mối quan hệ. Nhưng **cháu út** (pakṣa) chỉ cần nói *"tôi là cháu"* — vì vị trí trong gia đình đã nói lên tất cả.

---

## Kết luận

| Phát hiện | Chi tiết |
|-----------|----------|
| 6% thực ra là **2%** | Chỉ 1/53 block không nhắc concept khác |
| Block đó là gì? | **Pakṣa** — khái niệm cực đơn giản ("chủ thể suy luận") |
| Pakṣa có thoát hệ thống? | **Không** — vẫn bị khóa qua edge (Liṅga → Pakṣa) |
| 8 blocks 1-ref là gì? | Subtypes + đối lập — đơn giản nên chỉ cần 1 neo |
| Hệ thống vẫn đóng? | **Có** — 100% nodes connected qua edges |

**Mọi concept, dù đơn giản đến đâu, đều bị khóa trong mạng lưới.** Prose có thể không nhắc, nhưng edges luôn nối.
