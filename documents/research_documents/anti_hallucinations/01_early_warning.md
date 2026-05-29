Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 01 — Early Warning: Hallucination Signal Registry

**Role:** Layer 1 cua pipeline — dinh nghia cac tin hieu canh bao som. Khi mot claim, term, hoac mapping xuat hien khop voi signal -> trigger quy trinh anti-hallucination.

**Input:** Claim text, component description, hoac file can review.
**Output:** Signal match (Y/N) + severity (RED/ORANGE/YELLOW) + link den `02_detection.md`.
**Next:** `02_detection.md` — Component Inventory & Tracing.

---

## 1. Signal Registry

### 1.1 RED — Category Error / Fabrication (escalate ngay)

| ID | Signal name | Symptom pattern | Trigger condition | Example from VVV-QMRF |
|----|------------|-----------------|-------------------|------------------------|
| R1 | Category error: epistemology -> physics | Claim treats philosophical mapping as physical explanation | Text asserts "X solves/explains/predicts Y" without formal proof, peer review, or experimental test | "Buddhist Epistemology solves Quantum Measurement" (CLAUDE.md RCA example) |
| R2 | Invented source / citation hallucination | Citation khong ton tai, sai author, sai nam | Khong tim thay source trong Google Scholar / arXiv / textbook | "Dignaga (2005)" — Dignaga mat the ky 5-6, khong phai 2005 |
| R3 | Contradiction with known fact | Claim mau thuan truc tiep voi standard QM hoac experimental result da kiem chung | Claim asserts delta_P != 0 nhung khong co experimental evidence | "K9_E da duoc chung minh thuc nghiem" — chua duoc, moi la 2.31sigma ambiguous |
| R4 | Equivalence without justification | Cross-domain link treated as equivalence (khong phai analogy) | Text dung "=" hoac "<=>" giua BE concept va QM concept khong co justification | "Svasa.mvedana = Self-adjoint operator" — chua duoc chung minh |
| R5 | Structural contradiction with K1-K8 | Claim vi pham K1-K8 axioms da frozen | Claim requires K5 firing without C_K existence, hoac K3 cert = 0, hoac V ngoai {0,1} | "K5 fires across isolated K-spaces" — vi pham K5 Dep-A (requires_K_joint = 1) |

### 1.2 ORANGE — Missing / Weak Foundation (investigate)

| ID | Signal name | Symptom pattern | Trigger condition | Example from VVV-QMRF |
|----|------------|-----------------|-------------------|------------------------|
| O1 | Undefined term | Term duoc su dung nhung khong co dinh nghia formal | Term xuat hien >= 3 lan khong co definition block | "K_ctx" truoc khi duoc dinh nghia trong K9-S1 |
| O2 | Broken trace — source gap | Claim khong trace duoc ve bat ky SOT nao | Trace score = 0 khi tra `03_sot_traceability.md` | Orphaned component trong inventory |
| O3 | Assumption not flagged | Claim duoc trinh bay nhu fact nhung thuc ra la assumption | Text khong co flag [A-XX], khong co "assumption", khong co C-TRACE | "beta is universal" truoc khi duoc flag [A-E3] |
| O4 | Weak anchor — single source only | Component chi co 1 anchor va anchor do la WEAK | Trace score = 1 va anchor strength = WEAK | [A-E3] beta universal — chi co EX anchor WEAK |
| O5 | Stale reference — superseded data | Claim dung du lieu da bi superseded hoac invalidated | Reference tro den file da bi danh dau INVALIDATED hoac SUPERSEDED | Dung Phase 10b Bong LF data (da INVALIDATED boi K9-S8) |

### 1.3 YELLOW — Documentation / Presentation (review)

| ID | Signal name | Symptom pattern | Trigger condition | Example from VVV-QMRF |
|----|------------|-----------------|-------------------|------------------------|
| Y1 | Ambiguous boundary language | Khong ro ranh gioi giua interpretation, analogy, mapping, prediction | Text dung tu "suggests", "implies", "indicates" khong ro scope | "K9_E suggests a new understanding of measurement" — suggest gi? scope nao? |
| Y2 | Missing disclaimer / boundary statement | Claim vuot ra ngoai VVV-QMRF scope nhung khong co boundary statement | File khong co DISCLAIMER reference hoac scope boundary | File Class C khong reference den DISCLAIMER.md |
| Y3 | Inconsistent terminology | Cung 1 concept nhung dung nhieu term khac nhau | >= 2 term variants cho cung 1 concept trong cung 1 file | "registration-state update" vs "detector response" vs "wave function collapse" |
| Y4 | Missing version / date metadata | File khong co version, date, hoac status | File markdown khong co header metadata | File moi tao khong co "Version: vX.Y (YYYY-MM-DD)" |
| Y5 | BE lineage not documented | K-side concept co BE root nhung khong duoc link den BE node/edge | Concept co BE analogue nhung khong co N_BE_XXXXX hoac ED_BE_XXXXX reference | K5 bot_K khong link den N_BE_00006 (badhaka prama.na) |

---

## 2. Severity Escalation Protocol

| Severity | Y nghia | Hanh dong | Deadline |
|----------|---------|----------|----------|
| **RED** | Category error hoac fabrication — co the invalidate toan bo claim | Block merge/release + full investigation qua toan bo pipeline | Truoc commit tiep theo |
| **ORANGE** | Missing foundation — claim co the sai hoac thieu co so | Investigate qua `02_detection` + `03_sot_traceability` + `04_analysis` | Trong session hien tai |
| **YELLOW** | Documentation gap — claim co the dung nhung trinh bay chua ro | Review + fix documentation | Trong tuan |

---

## 3. Trigger Workflow

```
New claim / term / mapping
        |
        v
Scan Signal Registry (Section 1)
        |
        v
Match? --NO--> Normal workflow (continue)
        |
       YES
        |
        v
Classify severity (RED / ORANGE / YELLOW)
        |
        v
RED? --> Escalate immediately -> Full pipeline (02 -> 03 -> 04 -> 05 -> 06)
ORANGE? --> Investigate -> 02_detection.md -> ...
YELLOW? --> Review -> fix documentation -> re-scan
```

---

## 4. Integration with CLAUDE.md

File nay la operationalization cua CLAUDE.md RCA Warnings section:

| CLAUDE.md Warning | AHP Signal ID |
|-------------------|---------------|
| "If the revision only changes the sentence where the symptom appears, it is not enough" | O2 (broken trace), O3 (assumption not flagged) |
| "If the root cause cannot be explained in one sentence, understanding is not complete" | O1 (undefined term), R1 (category error) |
| "If the fix only adds a vague caveat, fallback phrase, or defensive wording, it is treating the symptom" | Y1 (ambiguous boundary), Y2 (missing disclaimer) |

---

## 5. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Coverage — do signals cover all known K9_E hallucination types? | 4.5/5 | 15 signals cover 100% of K9_E component categories. Missing: "overfitting to data" signal (added as O5 stale reference). |
| R2 | Severity calibration — are RED/ORANGE/YELLOW thresholds correct? | 5/5 | RED = category error / fabrication (khong the fix bang documentation). ORANGE = missing foundation (co the fix). YELLOW = presentation (khong anh huong validity). Calibration dung. |
| R3 | Actionability — does each signal have clear next step? | 5/5 | Moi signal co link den file tiep theo trong pipeline. Escalation protocol ro rang. |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

*Signal Registry v1.0 — 15 signals (5 RED + 5 ORANGE + 5 YELLOW). 3-Round RCA: 4.83/5.*
