Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 04 — RCA Analysis: 5-Whys + Root Cause Taxonomy

**Role:** Layer 4 cua pipeline — tu symptom + trace score, ap dung 5-Whys RCA de truy nguoc den root cause. Ke thua truc tiep tu CLAUDE.md Rule Zero (5-step process).

**Input:** Component inventory (tu `02_detection.md`) + trace score (tu `03_sot_traceability.md`).
**Output:** Root cause (1 cau) + verdict + documentation quality audit.
**Next:** `05_scoring.md` — 10-Point Hallucination Scale.

---

## 1. 5-Whys Template Chuan Hoa

Ap dung cho moi component co dau hieu dang ngo (trace score <= 2 hoac signal ORANGE+):

```markdown
### W1: Tai sao [SYMPTOM] xuat hien?
**Tra loi:** [Nguyen nhan truc tiep]

### W2: Tai sao [NGUYEN NHAN W1]?
**Tra loi:** [Nguyen nhan sau hon 1 cap]

### W3: Tai sao [NGUYEN NHAN W2]?
**Tra loi:** [Nguyen nhan sau hon 2 cap]

### W4: Tai sao [NGUYEN NHAN W3]?
**Tra loi:** [Nguyen nhan sau hon 3 cap]

### W5: Co phai [COMPONENT] la "bia dat" (fabrication)?
**Tra loi:** CO / KHONG. [Giai thich 1 cau]

### Root Cause (1 cau):
[Root cause duoc isolate — diem bat dau cua failure]
```

### 1.1 Vi du da calibrate — K9_E tong the (tu rca_k9e_origin_investigation.md §4)

```
Symptom: VVV-QMRF co K1-K8 (structural axioms) nhung khong co probability rule
  W1: Tai sao K9_E co ve "nhieu thanh phan moi"?
    -> Vi K9_E la POSTULATE (P9), khong phai theorem derived tu K1-K8.
  W2: Tai sao K9_E khong derive duoc tu K1-K8?
    -> K1-K8 chi dinh nghia structural properties — khong uniquely determine probability rule.
  W3: Tai sao chon functional form P = Tr(E_o rho) * [1 - beta * f_perp] / Z?
    -> La candidate DUY NHAT co delta_P != 0 o probability level + EWF relevance 5/5.
  W4: Tai sao 6/8 terms la "moi" (khong co trong QM)?
    -> Day la KY VONG cho postulate moi. Terms moi chinh la "K-side machinery."
  W5: Co phai K9_E la "bia dat"?
    -> KHONG. 19/19 thanh phan deu trace duoc ve Std QM, pre-Class C, hoac flagged assumption.

Root Cause: K9_E fills the EXACT SAME architectural gap that Born rule fills in Standard QM
  — a probability postulate for the registration layer.
```

---

## 2. Root Cause Taxonomy (6 Loai)

Moi root cause duoc phan loai vao 1 trong 6 loai sau:

### Type 1 — Category Error

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Epistemology claim bi nham lan thanh physics claim (hoac nguoc lai) |
| **Dau hieu** | Claim asserts "X solves/explains/predicts Y" khong co formal proof |
| **Vi du VVV-QMRF** | "Buddhist Epistemology solves Quantum Measurement" |
| **Signal match** | R1 (category error), R4 (equivalence without justification) |
| **Solution type** | Reframe claim thanh interpretive mapping UNLESS co formal proof + experimental test |
| **Prevention** | Luon dat boundary statement: "day la interpretive mapping, khong phai physical explanation" |

### Type 2 — Missing Definition

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Term duoc su dung nhung khong co dinh nghia formal |
| **Dau hieu** | Term xuat hien >= 3 lan khong co definition block |
| **Vi du VVV-QMRF** | "K_ctx" truoc K9-S1 |
| **Signal match** | O1 (undefined term) |
| **Solution type** | Document — them definition block + link den SOT |
| **Prevention** | Rule: moi term moi phai co definition block truoc khi su dung |

### Type 3 — Broken Trace

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Claim khong the trace ve bat ky SOT nao |
| **Dau hieu** | Trace score = 0 |
| **Vi du VVV-QMRF** | (chua co — 0 orphaned components trong K9_E) |
| **Signal match** | O2 (broken trace) |
| **Solution type** | Anchor (them SOT reference) hoac Remove (neu khong the anchor) |
| **Prevention** | Moi claim phai kem SOT reference luc tao |

### Type 4 — Assumption Masquerading

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Claim duoc trinh bay nhu fact nhung thuc ra la assumption |
| **Dau hieu** | Khong co flag [A-XX], khong co C-TRACE, khong co "assumption" |
| **Vi du VVV-QMRF** | "beta is universal" truoc khi duoc flag [A-E3] |
| **Signal match** | O3 (assumption not flagged) |
| **Solution type** | Document — flag assumption ro rang + them EX anchor |
| **Prevention** | Moi assumption moi -> flag [A-XX] + C-TRACE + anchor strength |

### Type 5 — Structural Gap

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Framework thieu machinery de support claim |
| **Dau hieu** | Claim requires T3-morphism nhung T3 chua duoc formal hoa day du |
| **Vi du VVV-QMRF** | T4-H Steps 3-4 DEFERRED — blocks 3-observer claim structural validation |
| **Signal match** | O4 (weak anchor) |
| **Solution type** | Derive (xay dung theorem) hoac Defer (neu can research them) |
| **Prevention** | Khong claim dieu gi vuot qua layer hien tai da duoc verify |

### Type 6 — Citation Hallucination

| Thuoc tinh | Mo ta |
|------------|-------|
| **Dinh nghia** | Invented source, sai author, sai nam, sai noi dung |
| **Dau hieu** | Khong tim thay source trong Google Scholar / arXiv / textbook |
| **Vi du VVV-QMRF** | "Dignaga (2005)" — Dignaga mat the ky 5-6 |
| **Signal match** | R2 (invented source) |
| **Solution type** | Remove (xoa claim) hoac Anchor (tim source that) |
| **Prevention** | Moi citation phai verify truoc khi su dung |

---

## 3. Isolation Checklist

Truoc khi ket luan root cause, kiem tra 7 cau hoi (ke thua CLAUDE.md step 3):

- [ ] Root cause co the giai thich trong 1 cau khong?
- [ ] Root cause nam o dau: assumption, source gap, category error, hay structural gap?
- [ ] Co phai symptom chi la "visible surface" cua 1 issue sau hon khong?
- [ ] Neu fix root cause nay, symptom co bien mat vinh vien khong?
- [ ] Co cascade effect nao tu root cause nay den cac component khac khong?
- [ ] Root cause nay co nam trong SOT khong? (neu co, SOT nao?)
- [ ] Co the verify root cause nay doc lap (khong chi dua tren symptom) khong?

---

## 4. Documentation Quality Audit

Sau khi xac dinh root cause, audit chat luong documentation cua component (ke thua tu reference §5):

| Tieu chi | Thang 1-5 | Cau hoi kiem tra |
|----------|-----------|-----------------|
| **Minh bach ve assumption** | ?/5 | Moi assumption co duoc flag [A-XX] + C-TRACE khong? |
| **Traceability** | ?/5 | Moi term co source traced (K1-K8, assumption, hoac QM standard) khong? |
| **Self-awareness ve limitation** | ?/5 | File co tu nhan la "POSTULATE" (khong phai "theorem") khong? Co boundary statement khong? |
| **QM boundary honesty** | ?/5 | Cac terms moi co duoc flag "NEW" — khong gia vo la QM standard khong? |
| **BE lineage documentation** | ?/5 | Moi K-side concept co BE node/edge reference khong? |

**Audit score:** Tong / 25. Threshold: >= 20/25 = PASS.

---

## 5. Verdict Template

Sau khi hoan thanh RCA + audit, dien verdict template:

```markdown
### Verdict — [Component/Document Name]

**Ngay:** YYYY-MM-DD
**RCA Method:** 5-Whys x scoring threshold 4/5
**Root cause type:** [1-6]
**Root cause (1 cau):** [...]

**Danh gia tong the:**

| Chi so | Gia tri |
|--------|---------|
| Tong so thanh phan dieu tra | N |
| So thanh phan co truoc | N (XX%) |
| So thanh phan sinh ra trong scope | N (XX%) |
| So thanh phan duoc flag assumption | N (XX%) |
| So thanh phan DERIVED | N (XX%) |
| So thanh phan ORPHANED | N (XX%) |
| Diem hallucination trung binh | X.XX/10 |
| So thanh phan hallucination (7-10) | N |

**Ket luan:**

> [Component] [LA / KHONG PHAI] hallucination. [...]
>
> [Neu khong phai:] No la mot [postulate / theorem / conceptual extension] duoc xay dung co he thong tu:
> - XX% thanh phan ke thua [...]
> - XX% thanh phan tu [...]
> - XX% thanh phan moi duoc flag assumption
>
> [Neu co hallucination:] Diem yeu: [...]
> Diem manh: [...]
```

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | 5-Whys template — does it match CLAUDE.md Rule Zero? | 5/5 | Template matches CLAUDE.md 5-step process exactly. Vi du calibrated tu K9_E tong the (§4 reference case). |
| R2 | Root cause taxonomy — are 6 types exhaustive? | 4.5/5 | 6 types cover 100% of known K9_E RCA findings. Potential gap: "methodological error" (RCA process itself applied wrongly) — co the them Type 7 trong tuong lai. |
| R3 | Audit criteria — do 5 criteria match reference §5? | 5/5 | 5 criteria match reference exactly. Threshold 20/25 duoc calibrate tu K9_E (documentation quality 23/25). |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

*RCA Analysis Framework v1.0 — 6 root cause types, 5-Whys template, 5 audit criteria. 3-Round RCA: 4.83/5.*
