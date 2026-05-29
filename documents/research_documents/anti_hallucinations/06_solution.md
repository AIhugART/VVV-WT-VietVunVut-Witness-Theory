Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 06 — Solution: Prioritized Solution Framework

**Role:** Layer cuoi cua pipeline — tu ket qua scoring + RCA, de xuat giai phap phan loai theo muc uu tien va track den khi RESOLVED.

**Input:** Hallucination score (tu `05_scoring.md`) + root cause (tu `04_analysis.md`).
**Output:** Solution type + priority level + action plan + resolution tracking entry.
**Next:** Quay lai `01_early_warning.md` de re-scan sau khi fix.

---

## 1. Priority Matrix

| Priority | Score range | Label | Hanh dong | Deadline | SLA |
|----------|-------------|-------|----------|----------|-----|
| **P0** | 9-10 (Do) | BLOCKING | Fix ngay — block merge/release | Truoc commit tiep theo | 1 session |
| **P1** | 7-8 (Cam) | HIGH | Fix trong phien lam viec hien tai | Trong ngay | 1-2 sessions |
| **P2** | 5-6 (Vang) | MEDIUM | Cung co anchor / them documentation | Trong tuan | 1 tuan |
| **P3** | 3-4 (Xanh duong) | LOW | Documentation them, BE lineage elaboration | Khi co thoi gian | 1 thang |
| **P4** | 0-2 (Xanh la) | ONGOING | Duy tri practice: flag assumption, trace term | Lien tuc | Khong gioi han |

---

## 2. Solution Categories (5 Loai)

### Type 1 — DERIVE

| Thuoc tinh | Mo ta |
|------------|-------|
| **Muc dich** | Chuyen assumption -> theorem. Xay dung structural proof de loai bo assumption. |
| **Ap dung khi** | Assumption co the duoc chung minh tu K1-K8 + BE SOT (khong can them postulate moi) |
| **Vi du VVV-QMRF** | [A-E2] f_perp: T8 bridge + H1 structural uniqueness -> ELIMINATED |
| **Effort** | HIGH (can 1-3 sessions + 3-round RCA verification) |
| **Impact** | Giam hallucination score 1-3 diem + assumption -1 |
| **RCA Round** | Round 1: correctness, Round 2: consistency, Round 3: impact |

### Type 2 — ANCHOR

| Thuoc tinh | Mo ta |
|------------|-------|
| **Muc dich** | Them SOT reference, EX anchor, hoac BE lineage de tang trace score |
| **Ap dung khi** | Component co trace score thap (0-2) nhung co the tim duoc anchor |
| **Vi du VVV-QMRF** | [A-E3] beta universal — can them experimental motivation hoac BE principle |
| **Effort** | MEDIUM (can 1 session research + documentation) |
| **Impact** | Tang trace score +1-3, co the giam hallucination score 1-2 diem |
| **RCA Round** | Chi can 1-2 rounds (verify anchor validity) |

### Type 3 — DOCUMENT

| Thuoc tinh | Mo ta |
|------------|-------|
| **Muc dich** | Flag assumption ro rang hon, them C-TRACE, them boundary statement |
| **Ap dung khi** | Component da co anchor nhung documentation chua day du |
| **Vi du VVV-QMRF** | Them BE lineage cho K-side concept, them "NEW" flag cho non-QM terms |
| **Effort** | LOW (thuong < 1 session) |
| **Impact** | Tang documentation quality score, khong anh huong hallucination score |
| **RCA Round** | Khong can — du documentation fix |

### Type 4 — REMOVE

| Thuoc tinh | Mo ta |
|------------|-------|
| **Muc dich** | Xoa component khong the cuu (orphaned, fabricated, contradicted) |
| **Ap dung khi** | Component trace score = 0 + khong the anchor + mau thuan voi known fact |
| **Vi du VVV-QMRF** | (Chua co — 0 orphaned components) |
| **Effort** | LOW (xoa + document ly do) |
| **Impact** | Component -1, co the yeu cau re-design cac component phu thuoc |
| **RCA Round** | Round 1: confirm orphaned status, Round 2: assess cascade impact |

### Type 5 — DEFER

| Thuoc tinh | Mo ta |
|------------|-------|
| **Muc dich** | Ghi nhan assumption la can thiet nhung chua the giai quyet ngay |
| **Ap dung khi** | Component can research them, experimental data, hoac theorem chua duoc xay dung |
| **Vi du VVV-QMRF** | T4-H Steps 3-4 (DEFERRED — cho T8 hoan thanh), 3-OBS experiment design |
| **Effort** | LOW (document DEFERRED status + unlock condition) |
| **Impact** | Khong anh huong score, nhung can track de khong bi bo quen |
| **RCA Round** | Round 1: confirm can defer, Round 2: set unlock condition |

---

## 3. Resolution Tracking Table

| # | Issue | Component | Score | Priority | Root Cause Type | Solution Type | Status | Assignee | Open Date | Resolve Date | Commit |
|---|-------|-----------|-------|----------|-----------------|---------------|--------|----------|-----------|-------------|--------|
| 1 | ... | ... | X/10 | P0-P4 | 1-6 | 1-5 | OPEN | ... | YYYY-MM-DD | — | — |

### 3.1 Status Options

| Status | Y nghia |
|--------|---------|
| **OPEN** | Da xac dinh, chua bat dau |
| **IN PROGRESS** | Dang thuc hien |
| **RESOLVED** | Da fix xong + verified |
| **DEFERRED** | Tam hoan — co unlock condition |
| **WONT_FIX** | Chap nhan risk — co ly do |

### 3.2 Vi du da calibrate — K9_E Recommendations (tu reference §9)

| # | Issue | Component | Score | Priority | Root Cause | Solution Type | Status |
|---|-------|-----------|-------|----------|------------|---------------|--------|
| 1 | Cung co EX anchor cho [A-E2] | f_perp | 6/10 | MEDIUM | Assumption masquerading (Type 4) | DERIVE | **RESOLVED** (T8 bridge, 2026-05-24) |
| 2 | Cung co EX anchor cho [A-E3] | beta universal | 5/10 | MEDIUM | Assumption masquerading (Type 4) | ANCHOR | Open |
| 3 | Formal hoa T3-morphism cho K_ctx | K_ctx | 5/10 | HIGH | Structural gap (Type 5) | DERIVE | **RESOLVED** (T9, 2026-05-24) |
| 4 | Cung co [A-E2b] outcome filter | f_perp filter | 2/10 | LOW | Structural gap (Type 5) | DERIVE | **RESOLVED** (H1, 2026-05-24) |
| 5 | Document motivation cua fraction form | f_perp | — | LOW | Documentation (n/a) | DOCUMENT | **RESOLVED** (T8+H3+H4) |
| 6 | Giữ nguyen practice: flag assumption, trace term | ALL | — | ONGOING | Prevention (n/a) | ONGOING | Ongoing |
| 7 | Trien khai H1 uniqueness proof | [A-E2b] | 2/10 | HIGH | Structural gap (Type 5) | DERIVE | **RESOLVED** (H1, 2026-05-24) |

---

## 4. Implementation Record Template

Khi mot solution duoc trien khai, ghi nhan theo mau nay (ke thua tu reference §8):

```markdown
### [Solution Name] — Implementation Record

**Ngay:** YYYY-MM-DD
**Target:** [Component / Issue #]
**Solution type:** [1-5]
**RCA score truoc:** X.X/10
**RCA score sau:** Y.Y/10

#### What was built

[Mo ta ngan gon nhung gi da duoc thuc hien]

#### RCA Verification

| Round | Focus | Score |
|-------|-------|-------|
| Round 1 | [Focus] | X.X/5 |
| Round 2 | [Focus] | X.X/5 |
| Round 3 | [Focus] | X.X/5 |
| **Aggregate** | | **X.XX/5** [PASS/FAIL] |

#### Files modified

| File | Change |
|------|--------|
| `path/to/file` | [Description] |

#### Net impact

| Metric | Before | After |
|--------|--------|-------|
| [Metric 1] | X | Y |
| [Metric 2] | X | Y |
```

---

## 5. Decision Matrix — Chon Solution Type Nao?

| Tinh huong | Solution Type | Vi du |
|------------|---------------|-------|
| Assumption co the prove tu K1-K8 | **DERIVE** | [A-E2] f_perp -> T8 bridge |
| Assumption can research them (experiment, theorem) | **DEFER** | T4-H Steps 3-4 |
| Component trace score = 0, khong the cuu | **REMOVE** | Orphaned component |
| Component trace score thap nhung tim duoc anchor | **ANCHOR** | [A-E3] beta universal |
| Component co anchor nhung documentation thieu | **DOCUMENT** | Them BE lineage |
| Component < 5 diem + stable | **ONGOING** | K1-K8 axioms |

---

## 6. 3-Round RCA Design Verification

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Solution type coverage — do 5 types cover all K9_E fix patterns? | 5/5 | DERIVE (T8, H1, T9), ANCHOR (A-E3 pending), DOCUMENT (BE lineage), REMOVE (chua can), DEFER (T4-H Steps 3-4). All covered. |
| R2 | Priority matrix calibration — do P0-P4 thresholds match scoring bands? | 5/5 | P0(9-10) = Do, P1(7-8) = Cam, P2(5-6) = Vang, P3(3-4) = Xanh duong, P4(0-2) = Xanh la. Mapping 1:1 — consistent. |
| R3 | Tracking usability — can resolution tracking catch stale issues? | 4.5/5 | Resolution tracking table + Implementation Record template day du. Minor: them auto-reminder cho DEFERRED items (sau 2 tuan). |
| **Aggregate** | | **4.83/5** PASS (>= 4/5) | |

---

*Solution Framework v1.0 — 5 priority levels, 5 solution types, full tracking. 3-Round RCA: 4.83/5.*
