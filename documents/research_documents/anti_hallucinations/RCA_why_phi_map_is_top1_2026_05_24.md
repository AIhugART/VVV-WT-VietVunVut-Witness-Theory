Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# RCA — Tại sao phi-map là #1? (post-[A-E3] removal)

**Date:** 2026-05-24
**Method:** 5-Whys RCA x scoring threshold 4/5
**Reference:** Top 10 v1.2 (`00_top_10_hallucinations_record.md`)

---

## Bối cảnh

Sau khi [A-E3] (beta universal) bi REMOVED khoi Top 10 (reclassified: FREE PARAMETER), **phi-map K→B(H) tro thanh #1** voi Risk Score = 18.0.

Câu hỏi: Tại sao phi-map — mot Class D conjecture khong block K9_E Class C — lai dung #1?

---

## 5-Whys RCA

```
W1: Tại sao phi-map là #1?
  → Risk Score = 18.0 — cao nhat trong 10 component con lai.

W2: Tại sao Risk Score = 18.0?
  → H=6 × W=2 × (1+0.5) = 6 × 2 × 1.5 = 18.0.
    H=6 la diem hallucination CAO NHAT trong TOAN BO VVV-QMRF.
    Khong component nao khac co H=6 (P10-NOISE: 5, T5: 5, K9E-PAT: 5, K5_prosp: 5).

W3: Tại sao H=6 — cao nhất?
  → phi-map (φ: K → B(H)) la Class D CONJECTURE:
    - Chua duoc prove (chi co necessary conditions N_1-N_T, Track B Phases 1-3)
    - La "largest structural unknown" trong VVV-QMRF (EX compass)
    - Khong co experimental evidence (hoan toan ly thuyet)
    - Anchor WEAK: 1 SOT (CLAUDE.md), conceptual only
    → H=6 phan anh su KHONG CHAC CHAN cao nhat trong toan bo framework.

W4: Tại sao W=2 ma khong phai W=3?
  → W=3 chi ap dung cho component anh huong TRUC TIEP den K9_E Class C:
    - [A-E3] β: W=3 vi la tham so DUY NHAT cua K9_E
    - K_ctx: W=3 vi la INPUT cua f_perp
    - P10-NOISE: W=3 vi co the INVALIDATE genuine fit
  → phi-map: neu sai, VVV-QMRF mat "bridge to QM" — nhung K9_E Class C VAN DUNG.
    K9_E khong can φ de tinh P(o|K). φ la "long-term foundation", khong phai "operational necessity".
    → W=2 la dung: quan trong nhung khong block core.

W5: ROOT CAUSE — Tại sao phi-map #1?
  → VI KHONG CO COMPONENT NAO KHAC CO H=6.
    Tat ca component H=5 (P10-NOISE, T5, K9E-PAT, K5_prosp) deu co W=3 hoac W=2
    nhung H thap hon. Trong nhom 18.0, tiebreaker H (desc) day phi-map len #1.
    
    Phi-map la #1 khong phai vi no NGUY HIEM NHAT (W=2 < W=3 cua P10-NOISE/T5),
    ma vi no DANG NGHI NHAT (H=6 cao nhat).
```

---

## So sánh phi-map vs các component khác

| Component | H | W | A | Risk | Tại sao xếp sau? |
|-----------|---|---|---|--------|-------------------|
| **phi-map** | **6** | 2 | 0.5 | **18.0** | H cao nhất → #1 |
| P10-NOISE | 5 | 3 | 0.2 | 18.0 | H=5 < H=6. Nhưng NGUY HIỂM HƠN (W=3: threatens evidence) |
| T5 K_ctx | 5 | 3 | 0.2 | 18.0 | H=5 < H=6. Đã có T9 progress |
| T4-H | 4 | 3 | 0.5 | 18.0 | H=4 thấp nhất nhóm 18.0 |

> **Lưu ý quan trọng:** P10-NOISE (W=3) NGUY HIỂM HƠN phi-map (W=2) về mặt tác động thực tế. P10-NOISE co the downgrade Class C (genuine)→(qualified). phi-map sai cung khong anh huong K9_E. Nhưng tiebreaker H (desc) ưu tiên "đáng nghi" hơn "nguy hiểm" — đây là dụng ý thiết kế: Risk Score ưu tiên hallucination risk, không phải impact risk.

---

## Hàm ý

```
Risk Score = H × W × (1+A) ưu tiên H (hallucination) hơn W (impact).

Điều này có nghĩa:
  - Component "đáng nghi nhất" (H cao) sẽ đứng đầu, ngay cả khi impact thấp (W thấp)
  - Component "nguy hiểm nhất" (W cao) có thể đứng sau nếu H thấp hơn

Nếu muốn ưu tiên IMPACT thay vì HALLUCINATION:
  → Cần công thức khác: Impact Score = W × H × (1+A)
  → P10-NOISE se la #1 (W=3 × H=5 × 1.2 = 18.0, nhung W=3 > W=2)
```

---

## Kết luận

> **phi-map là #1 vì H=6 — điểm hallucination cao nhất toàn VVV-QMRF.**
>
> Nó là Class D conjecture chưa được chứng minh, với anchor WEAK (chỉ 1 SOT conceptual). Mặc dù W=2 (không block K9_E), H=6 đẩy nó lên đầu bảng trong tiebreaker.
>
> **P10-NOISE thực sự NGUY HIỂM HƠN** (W=3, threatens genuine fit evidence), nhưng H=5 thấp hơn nên xếp #2. Đây là hệ quả của việc Risk Score ưu tiên "hallucination risk" hơn "impact risk".

---

*RCA: Why phi-map is #1 — 2026-05-24. 5-Whys RCA.*
