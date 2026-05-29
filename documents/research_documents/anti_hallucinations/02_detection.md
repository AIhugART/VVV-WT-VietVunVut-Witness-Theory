Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 02 — Detection: Component Inventory & Tracing Protocol

**Role:** Layer 2 cua pipeline — khi co trigger tu `01_early_warning.md`, file nay cung cap protocol de inventory va trace tung thanh phan cua claim/document.

**Input:** Trigger signal(s) + claim/document can dieu tra.
**Output:** Component Inventory Table + phan loai nguon goc (4 nhom) + so bo hallucination score.
**Next:** `03_sot_traceability.md` — SOT Cross-Reference Matrix.

---

## 1. Component Inventory Template

Moi claim/document duoc "mo xac" thanh cac thanh phan (components). Moi component dien 1 dong trong bang sau:

| # | Ky hieu | Ten & Y nghia | Sinh ra tu dau? | Co truoc khong? | Link nguon xac nhan | QM/Reference standard tuong tu | O dau trong standard | Hallucination (thang 10) |
|---|---------|---------------|-----------------|-----------------|---------------------|------------------------------|----------------------|--------------------------|
| 1 | ... | ... | ... | Y/N | ... | ... | ... | .../10 |

### 1.1 Column Definitions

| Column | Cach dien | Vi du |
|--------|----------|-------|
| **#** | So thu tu thanh phan | T1, T2, ... hoac 1, 2, ... |
| **Ky hieu** | Ma code cua thanh phan | `Tr(E_o rho_i)`, `beta`, `f_perp`, `V(k)` |
| **Ten & Y nghia** | Ten goi + 1 cau mo ta chuc nang | "Born rule probability — xac suat do duoc outcome o tu trang thai rho_i" |
| **Sinh ra tu dau?** | Pham vi tao ra thanh phan nay | "Class C", "Pre-Class C", "Standard QM", "BE SOT" |
| **Co truoc khong?** | Y = da ton tai truoc pham vi hien tai; N = moi duoc tao | Y (da co trong K1-K8 tu 2026-05-19) |
| **Link nguon xac nhan** | File path + line number (neu co) hoac external reference | `K_Space_Axiomatization.md` L300-387; Born rule: POVM textbook |
| **QM/Reference standard** | Trong QM hoac BE co khai niem tuong tu khong? | "Born rule P(o) = Tr(E_o rho)", "Khong co trong QM", "BE: anupalabdhi" |
| **O dau trong standard** | Dinh vi chinh xac trong standard | "QM Postulate P3 (measurement) + POVM formalism" |
| **Hallucination (thang 10)** | Diem so bo, se duoc verify trong `05_scoring.md` | 0-10 (xem rubric) |

---

## 2. Four-Group Origin Classification

Sau khi inventory, phan loai moi thanh phan vao 1 trong 4 nhom:

### Nhom A — Tu Standard QM (Co that 100%)

| Tieu chi | Vi du |
|----------|-------|
| Co trong moi QM textbook | Born rule `P(o) = Tr(E_o rho)` |
| Da duoc kiem chung thuc nghiem tu 1926 | POVM completeness `Sigma_o E_o = I` |
| Khong can anchor them — day la nen tang vat ly | State normalization `Tr(rho) = 1` |
| **Trace score:** 1/1 (chi can SOT-5: Standard QM) | |
| **Hallucination band:** 0-2 (Xanh la) | |

### Nhom B — Tu VVV-QMRF Pre-Existing (K1-K8, E1-E16, BE SOT)

| Tieu chi | Vi du |
|----------|-------|
| Da ton tai truoc Class C (truoc commit `6df1482`) | K4 `V in {0,1}`, K5 `bot_K` |
| Co dinh nghia formal trong K_Space_Axiomatization.md | E9 `isNull(k)`, E7 validity postulate |
| Co BE lineage ro rang (N_BE_XXXXX / ED_BE_XXXXX) | K3 cert <- N_BE_00001 (svasa.mvedana) |
| **Trace score:** >= 2/6 (SOT-2 + SOT-1) | |
| **Hallucination band:** 0-4 (Xanh la hoac Xanh duong) | |

### Nhom C — Moi — Duoc Flag Assumption + Co Anchor

| Tieu chi | Vi du |
|----------|-------|
| Duoc tao ra trong pham vi hien tai | K9_E beta parameter |
| Duoc flag assumption ro rang [A-XX] | [A-E3] beta is universal |
| Co EX anchor (N_QM_VVV_XXXXX) hoac BE anchor | EX anchor: N_QM_VVV_00031 |
| Duoc khai bao minh bach la "POSTULATE" (khong phai theorem) | K9_E = P9 postulate |
| **Trace score:** >= 1/6 (it nhat 1 anchor) | |
| **Hallucination band:** 5-6 (Vang) | |

### Nhom D — Moi — ORPHANED (KHONG co Trace)

| Tieu chi | Vi du |
|----------|-------|
| Duoc tao ra trong pham vi hien tai | (chua co vi du trong K9_E — 0 orphaned) |
| KHONG co flag assumption | |
| KHONG co EX anchor hoac BE anchor | |
| KHONG the trace ve bat ky SOT nao | |
| **Trace score:** 0/6 | |
| **Hallucination band:** 7-10 (Cam hoac Do) — RED FLAG | |

---

## 3. Detection Workflow

```
Trigger from 01_early_warning.md
        |
        v
Step 1: DECOMPOSE — "mo xac" claim thanh cac thanh phan
  - Moi term, concept, assumption, equation term la 1 component
  - Dien vao Component Inventory Table (Section 1)
        |
        v
Step 2: TRACE — truy vet nguon goc tung thanh phan
  - Kiem tra git log (neu la file trong repo)
  - Kiem tra SOT cross-reference (03_sot_traceability.md)
  - Kiem tra QM textbook / BE SOT
  - Ghi nhan "Link nguon xac nhan"
        |
        v
Step 3: CLASSIFY — phan loai vao 4 nhom (Section 2)
  - Nhom A: Standard QM
  - Nhom B: Pre-existing VVV-QMRF
  - Nhom C: New — flagged assumption + anchor
  - Nhom D: ORPHANED -> RED FLAG
        |
        v
Step 4: PRE-SCORE — cham diem so bo (se verify trong 05_scoring.md)
  - Ap dung rubric 05_scoring.md
  - Dac biet: Nhom D auto >= 7/10
        |
        v
Step 5: ESCALATE if needed
  - Co component nao Nhom D khong? -> RED FLAG -> escalate ngay
  - Co component nao Nhom C voi score >= 6? -> prioritize
  - Khong co gi dang ngo? -> complete + document
```

---

## 4. Orphaned Component Report Template

Khi phat hien Nhom D component, dien template nay:

```markdown
### Orphaned Component Report — [Component Name]

**Phat hien ngay:** YYYY-MM-DD
**File chua component:** [path]
**Mo ta component:** [1 cau]

**Truy vet:**
- Git log: [khong tim thay / commit X nhung khong co dinh nghia]
- SOT-1 (BE): [khong co match]
- SOT-2 (K-Space canonical): [khong co match]
- SOT-3 (K-Space Class C): [khong co match]
- SOT-5 (Std QM): [khong co match]
- SOT-6 (Experimental data): [khong co match]

**Trace score:** 0/6
**Hallucination score so bo:** [7-10]
**Khan cap:** RED — BLOCKING
**Hanh dong:** Chuyen den `06_solution.md` — Solution type: Remove hoac Anchor
```

---

## 5. Quick Detection Checklist

Khi review 1 file/document, quet qua cac cau hoi sau:

- [ ] Moi term trong file co duoc dinh nghia formal khong? (O1)
- [ ] Moi claim co trace duoc ve SOT khong? (O2)
- [ ] Moi assumption co duoc flag [A-XX] khong? (O3)
- [ ] Co claim nao treated as fact nhung thuc ra la assumption? (O3)
- [ ] Co reference nao den du lieu da INVALIDATED/SUPERSEDED? (O5)
- [ ] Co cross-domain equivalence nao khong co justification? (R4)
- [ ] Co claim nao mau thuan voi K1-K8? (R5)
- [ ] Co term nao thay doi ten giua cac file? (Y3)
- [ ] File co version/date metadata khong? (Y4)
- [ ] BE lineage co duoc document khong? (Y5)

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Completeness — does template capture all K9_E investigation columns? | 5/5 | Template matches `rca_k9e_origin_investigation.md` section 2 exactly. All 9 columns are covered. |
| R2 | Classification accuracy — do 4 groups partition correctly? | 5/5 | 4 nhom la mutually exclusive + exhaustive. Moi component K9_E (19/19) duoc phan loai dung. Nhom D trong — chuan bi cho phat hien hallucination thuc su. |
| R3 | Workflow usability — can a new reviewer follow the steps? | 4.5/5 | 5-step workflow ro rang. Checklist 10 cau hoi giup scan nhanh. Minor: them "estimated time per component" de reviewer biet effort. |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

*Detection Protocol v1.0 — 4 nhom nguon goc, 5-step workflow, 10-point checklist. 3-Round RCA: 4.83/5.*
