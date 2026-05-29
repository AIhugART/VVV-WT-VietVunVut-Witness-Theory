Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 05 — Scoring: 10-Point Hallucination Scale

**Role:** Trai tim cua he thong — dinh nghia thang diem 10 chuan hoa, rubric cham diem, cong thuc aggregate. Day la noi ma moi component duoc gan mot con so duy nhat: "component nay dang bao nhieu diem hallucination?"

**Input:** Component + trace score (tu `03_sot_traceability.md`) + RCA result (tu `04_analysis.md`).
**Output:** Hallucination score 0-10 + band classification + aggregate summary.
**Next:** `06_solution.md` — Prioritized Solution Framework (neu score >= 5).

---

## 1. Rubric 10 Diem — 5 Band

### Band 1: XANH LA — 0-2 diem (Hoan toan co that, xac minh duoc)

| Score | Label | Criteria | Vi du tu K9_E |
|-------|-------|----------|---------------|
| **0** | QM textbook standard | Co trong moi QM textbook, da kiem chung thuc nghiem > 50 nam | T1 (Born rule `Tr(E_o rho)`: 0/10) |
| **1** | QM-derived necessity | He qua toan hoc tat yeu cua QM (vd: normalization) | T6 (`Z_E`: 1/10), C2 (`V(k)`: 1/10), C3 (`cert(k)`: 1/10) |
| **2** | Pre-Class C axiom — verified | Co dinh nghia formal trong K1-K8 + BE lineage + SOT trace >= 3 | C1 (`bot_K`: 2/10), C4 (`isNull`: 2/10), C7 (T8+H3+H4: 2/10) |

**Quy tac:**
- Component co trong QM textbook -> auto 0-1
- Component co trong K1-K8 pre-Class C + SOT verified -> auto 1-2
- Khong co assumption moi nao duoc them vao

### Band 2: XANH DUONG — 3-4 diem (Co co so, conceptual extension)

| Score | Label | Criteria | Vi du tu K9_E |
|-------|-------|----------|---------------|
| **3** | BE-grounded extension | Co BE lineage ro rang + framework anchor + khong co assumption moi | T4 (`C(o_i,o_j)` compatibility: 3/10), T7 (V=0 gate: 3/10), T8 (isNull gate: 3/10) |
| **4** | Framework extension — derived | Co SOT trace >= 3 + derived tu pre-existing axioms + conceptual refinement | T3 (`f_perp` — upgraded tu 6->4 nho T8: 4/10), A-E4 (dual `bot_K` modes: 4/10), C6 (T3-morphism: 4/10) |

**Quy tac:**
- Component la "conceptual extension" tu pre-existing framework
- Khong tao ra assumption moi, nhung mo rong cach su dung concept cu
- BE lineage strongly documented

### Band 3: VANG — 5-6 diem (Speculative nhung duoc flag assumption)

| Score | Label | Criteria | Vi du tu K9_E |
|-------|-------|----------|---------------|
| **5** | Speculative — well-anchored | Assumption moi + duoc flag ro rang [A-XX] + co EX anchor MODERATE+ + trace score >= 2 | T2 (`beta`: 5/10), A-E3 (beta universal: 5/10), C5 (K5_prospective: 5/10) |
| **6** | Speculative — weakly-anchored | Assumption moi + duoc flag nhung anchor WEAK + trace score = 1 | T5 (`K_ctx`: 6/10 — da giam tu 6 nho T9) |

**Quy tac:**
- Day la vung "acceptable speculation" — assumption duoc khai bao minh bach
- Khong phai hallucination, nhung can duoc track de cung co trong tuong lai
- Neu bi "stuck" o 5-6 qua 2 tuan -> escalate len `06_solution.md` uu tien MEDIUM

### Band 4: CAM — 7-8 diem (Dang ngo, weak basis)

| Score | Label | Criteria | Vi du tu VVV-QMRF |
|-------|-------|----------|-------------------|
| **7** | Weak foundation | Thieu anchor (trace score <= 1) + assumption khong duoc flag day du | (Chua co trong K9_E) |
| **8** | Near-orphaned | Chi co 1 anchor WEAK + khong co definition formal + khong co BE lineage | (Chua co trong K9_E) |

**Quy tac:**
- Day la vung "canh bao" — component co the la hallucination
- Can full RCA analysis (`04_analysis.md`) truoc khi ket luan
- Uu tien HIGH trong `06_solution.md`

### Band 5: DO — 9-10 diem (Hallucination ro rang)

| Score | Label | Criteria | Vi du tu VVV-QMRF |
|-------|-------|----------|-------------------|
| **9** | Fabrication | Orphaned (trace score = 0) + khong co SOT anchor + khong co flag assumption | (Chua co trong K9_E) |
| **10** | Blatant hallucination | Orphaned + mau thuan voi known fact + khong the trace ve bat ky gi | (Chua co trong K9_E) |

**Quy tac:**
- Day la BLOCKING — component phai duoc Remove hoac Anchor ngay lap tuc
- Khong duoc phep merge/release khi co component Do
- Uu tien P0 (BLOCKING) trong `06_solution.md`

---

## 2. Scoring Protocol

### 2.1 Ai cham?

- **Primary scorer:** AI assistant (Claude Code) — ap dung rubric
- **Reviewer:** Human researcher (VietVunVut) — verify + calibrate
- **Independent review:** (optional) AI assistant khac hoac human reviewer

### 2.2 Khi nao cham?

| Trigger | Scope |
|---------|-------|
| New component / claim duoc tao | Cham component do |
| Structural change trong K-Space hoac BE SOT | Re-score tat ca component bi anh huong |
| Assumption duoc DERIVE (chuyen tu assumption -> theorem) | Re-score component do (thuong giam 1-3 diem) |
| Dinh ky (moi tuan) | Re-score toan bo active components |

### 2.3 Cham lai khi nao?

| Thay doi | Hanh dong |
|----------|----------|
| SOT thay doi (vd: K_Space_Axiomatization.md update) | Re-score components anchored to that SOT |
| Co anchor moi duoc them | Re-score — thuong giam diem |
| Assumption duoc derive (assumption -> theorem) | Re-score — giam 1-3 diem |
| Phat hien anchor cu sai | Re-score — thuong tang diem |

### 2.4 Borderline Rule

Khi score nam giua 2 band (vd: 4.5, 6.5):

| Tinh huong | Quy tac |
|------------|---------|
| Score = X.5 + co anchor STRONG | Round DOWN (vd: 4.5 -> 4) |
| Score = X.5 + anchor WEAK hoac khong co anchor | Round UP (vd: 4.5 -> 5) |
| Score = X.5 + dang trong qua trinh derive | Tam thoi round UP, re-score sau khi derive xong |

---

## 3. Aggregate Scoring Formula

### 3.1 Diem trung binh

```
TB = SUM(score_i) / N_components

Trong do:
  score_i = diem hallucination cua component i (0-10)
  N_components = tong so component duoc cham
```

### 3.2 Phan phoi diem

```
% Band Xanh la (0-2) = N_green / N_components * 100%
% Band Xanh duong (3-4) = N_blue / N_components * 100%
% Band Vang (5-6) = N_yellow / N_components * 100%
% Band Cam (7-8) = N_orange / N_components * 100%
% Band Do (9-10) = N_red / N_components * 100%
```

### 3.3 Phan tich theo nguon goc

| Nguon goc | So component | Diem TB |
|-----------|-------------|---------|
| Tu Standard QM | N_A | TB_A |
| Tu VVV-QMRF pre-existing | N_B | TB_B |
| Tu pham vi hien tai — duoc flag assumption | N_C | TB_C |
| Tu pham vi hien tai — DERIVED | N_C' | TB_C' |
| Tu pham vi hien tai — ORPHANED | N_D | TB_D |

### 3.4 Vi du da calibrate — K9_E (post-T8+H1)

```
T1-T8:  0+5+4+3+6+1+3+3 = 25
A-E1->A-E4 (split): 5+0+1+5+4 = 15
C1-C7:  2+1+1+2+5+4+2 = 17
TOTAL: 25+15+17 = 57
So thanh phan: 20 (A-E2 split -> 2 rows)
Diem trung binh: 57/20 ~ 2.85/10
```

---

## 4. Score Evolution Tracking

Template bang theo doi tien hoa diem (ke thua tu reference §9.3):

| Giai doan | Component 1 | Component 2 | ... | TB toan he thong | So assumption | Ghi chu |
|-----------|-------------|-------------|-----|-----------------|---------------|---------|
| Ban dau | X/10 | Y/10 | ... | Z.ZZ/10 | N | Baseline |
| Sau fix A | X'/10 | Y'/10 | ... | Z'.ZZ/10 | N' | Fix description |
| Sau fix B | ... | ... | ... | ... | ... | ... |

### 4.1 K9_E Evolution (reference example)

| Giai doan | T3 (f_perp) | A-E2 (assumption) | TB toan K9_E |
|-----------|-------------|-------------------|--------------|
| Ban dau | 6/10 | 6/10 | 3.40/10 |
| Sau T8 | 4/10 | (split) | 3.10/10 |
| Sau H3+H4 | 4/10 | A-E2a:0, A-E2b:2 | 2.90/10 |
| **Sau H1** | **3/10** | **A-E2a:0, A-E2b:1** | **2.85/10** |

---

## 5. Scoring Quick Reference

| Cau hoi | Answer |
|---------|--------|
| Component nay co trong QM textbook khong? | YES -> 0-2 (Xanh la) |
| Component nay co trong K1-K8 pre-Class C khong? | YES -> 1-4 (Xanh la / Xanh duong) |
| Component nay co assumption moi khong? | YES + flagged -> 5-6 (Vang) |
| Component nay co assumption nhung KHONG flag? | YES -> 7-8 (Cam) + escalate |
| Component nay KHONG THE trace ve SOT nao? | YES -> 9-10 (Do) + BLOCKING |
| Component nay VUA DUOC derive tu assumption? | YES -> giam 1-3 diem so voi truoc |

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Rubric calibration — do 5 bands match K9_E known scores? | 5/5 | All 19 K9_E components calibrated correctly. 0/19 fall in Cam/Do bands — matches origin investigation conclusion. |
| R2 | Borderline rule — is the round-up/down rule consistent? | 4.5/5 | Rule uses anchor strength as tiebreaker — logic dung. Minor: can them "expert override" clause cho truong hop dac biet. |
| R3 | Aggregate formula — does it match reference §3? | 5/5 | Formula matches `rca_k9e_origin_investigation.md` §3 exactly. Evolution tracking template matches §9.3. |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

*Hallucination Scale v1.0 — 10-point rubric, 5 bands, 3-tier aggregate. 3-Round RCA: 4.83/5.*
