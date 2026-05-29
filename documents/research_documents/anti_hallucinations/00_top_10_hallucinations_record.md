Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# 00 — Top 10 Hallucination Risk Record

**Role:** File uu tien cao nhat — ghi nhan cac khai niem co nguy co hallucination cao nhat trong toan bo VVV-QMRF. Day la "danh sach canh bao do" — moi component trong nay can duoc re-audit moi tuan.

**Structure:** 2 independent tables with cross-reference. "Project" field classifies each component.
**Scope (Table 1):** VVV-QMRF Class C — K9_E evidence and validation chain
**Scope (Table 2):** VVV-QMRF Full — structural framework (K1-K8, T1-T8, phi-map Track B, E1-E16, BE-QM mapping, T4-H)
**Compass:** VVV-QMRF-EX (intelligence only — EX flag K-PENDING-RCA, stress points)
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5
**Ranking formula:** Risk Score = H x W x (1 + A)
**Tiebreaker:** Risk Score bang nhau -> sort by H (desc) -> W (desc) -> A (desc) -> Trace score (ascending)
**Shared component rule:** Components appearing in both tables (T5 K_ctx, K5_prospective) MUST have identical H/W/A/Risk scores. Any score change to a shared component MUST be applied to both tables.

**Ngay:** 2026-05-27 UTC+7
**Version:** v1.6 — K7_trace + D_enc AHP evaluation (Layer 2 promotion, 2026-05-27): both GREEN/LOW, G2 gate PASS, no Top 10 entry required
**Previous:** v1.5 (2026-05-25) — AHP Status Model Extension (DORMANT+ARCHIVED) + Tiebreaker #4 (Trace score) + v1.0→v1.1 changelog
**Next audit:** 2026-05-31

---

## Changelog v1.5 -> v1.6

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **EVALUATE** | K7_trace (Closure Transition Record) | Not in AHP pipeline | G2 PASS: H=2, W=2, A=0.2, Risk=4.8 (GREEN/LOW). Trace=3/6 (K7 axiom SOT + BB_VVV_fit_plan §18 + K_Space_Axiomatization.md v2.4). Score ≤ 8, trace ≥ 1, no [AH-CRIT]. | Layer 2 promotion 2026-05-27 (Theoretical_Integration_plan.md v1, RCA 4.77/5). AHP gate mandatory per CLAUDE.md. Risk below Top 10 minimum (9.0) — no table entry required. |
| **EVALUATE** | D_enc (Transition-Encoding Registration Act) | Not in AHP pipeline | G2 PASS: H=3, W=2, A=0.2, Risk=7.2 (GREEN/LOW). Trace=2/6 (K7_trace canonical SOT + BB_VVV_fit_plan §19). Score ≤ 8, trace ≥ 1, no [AH-CRIT]. | Layer 2 promotion 2026-05-27 (same RCA gate). Risk below Top 10 minimum (9.0) — no table entry required. |

**G2 Gate verdict (2026-05-27):** K7_trace Risk=4.8 PASS, D_enc Risk=7.2 PASS. No Yellow/Red. Top 10 tables unchanged.

---

## Changelog v1.4 -> v1.5

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **METHODOLOGY** | Tiebreaker chain | H→W→A (3-level) | H→W→A→Trace (4-level) | 3-Round RCA Decision A (5.00/5): 3 dead-tie pairs khong the phan biet voi H/W/A alone. Trace score (SOT) breaks 2/3 ties. Pair con lai (E1-E16=BE↔QM) o LOW band → chap nhan arbitrary. |
| **RESOLVE** | E1-E16 SOT | SOT=2-4/6 (range) | SOT=2/6 (worst-case) | Decision A prerequisite: "weakest link" principle — risk cua 16-postulate group = risk of weakest postulate. |
| **EXTENSION** | AHP Status Model | 5 statuses (OPEN, MONITORING, DEFERRED, DECISION-LOCKED, CLOSED) | 7 statuses (+DORMANT, +ARCHIVED) | 3-Round RCA Decision C (4.33/5): AHP thieu category cho unactionable risks (DECISION-LOCKED→DORMANT) va resolved-but-kept risks (CLOSED-UNRESOLVABLE→ARCHIVED). New section: AHP Status Model Extension. |
| **RECLASSIFY** | P10-TIM | Status=DECISION-LOCKED, Label=[AH-LOCK] | Status=DORMANT, Label=[AH-DORMANT] | Decision C: P10-TIM la "unactionable" — raw event data external dependency. DORMANT = risk real nhung khong the action, reactivates on trigger. |
| **RECLASSIFY** | K9E-PAT | Status=CLOSED (v31), Label=[CLOSED-UNRESOLVABLE] | Status=ARCHIVED (v31), Label=[AH-ARCHIVED] [CLOSED-UNRESOLVABLE] | Decision C: K9E-PAT RCA 4.92/5 → ARCHIVED. Kept in table for historical traceability, audit N/A, reactivate only with K9-S12 data. |
| **ADD** | v1.0→v1.1 Changelog | Missing historical delta | T5 H=6→5 delta documented (T9 eliminated A-E1) | Decision B (4/5): documentation gap — T5 score change reason not previously documented. Reconstructed from Score Evolution table + T9 RCA verdict. |
| **FIX** | K9E-PAT Score Evolution row | 5 columns (missing v1.2 Risk) | 6 columns (aligned with header) | Decision B (5/5): markup error — manual edit after CLOSED status left misaligned column. Root cause: no automated column count validation. |
| **UPDATE** | Audit Schedule | K9E-PAT=Weekly, P10-TIM=N/A | K9E-PAT=On trigger (ARCHIVED), P10-TIM=On trigger (DORMANT) | Sync with new status model. ARCHIVED items have no active audit cycle. |
| **FIX** | Rank inversion P10-TIM↔BE↔QM | P10-TIM #9 (9.0), BE↔QM #10 (9.6) | BE↔QM #9 (9.6), P10-TIM #10 (9.0) | RCA 5-Why: BE↔QM Risk=9.6 > P10-TIM Risk=9.0 → BE↔QM must rank above P10-TIM. Root cause: BE↔QM appended at #10 in v1.2 without re-ranking P10-TIM (grandfathered). Methodology gap: no "insert & re-rank" verification step for new components. |
| **ADD** | Dead-tie note E1-E16↔BE↔QM | No documentation | Dead-tie note on both components | E1-E16=BE↔QM: all 4 tiebreakers equal (H=4, W=2, A=0.2, Trace=2). Arbitrary order; E1-E16 first by historical precedence. |
| **FIX** | Header tiebreaker | 3-level (H→W→A) | 4-level (H→W→A→Trace) | Sync with methodology section — missed in Decision A implementation. |
| **RECLASSIFY** | phi-map status | OPEN | DEFERRED | RCA 5-Why: "OPEN" misleading — phi-map is in long-term Track B research program (P3), not unattended gap. Giai phap uu tien already DEFER. Both Table 1 and Table 2 updated. |
| **FIX** | K9_E impl status inconsistency | Detail=DOCUMENTED, Summary=OPEN | Detail=MONITORING, Summary=MONITORING | RCA 5-Why: divergence characterized in v31 but Status Summary never updated. Now MONITORING — active watch until K9-S12 selects canonical. |
| **UPDATE** | Status Summaries (both tables) | Table 1: OPEN=2; Table 2: OPEN=1 | Table 1: OPEN=0, DEFERRED=2, MONITORING=5; Table 2: OPEN=0, DEFERRED=2 | All OPEN components reclassified. OPEN count = 0 across both tables. |

---

## 3-Round RCA Classification Decision (v1.3)

**Purpose:** Phan loai 10 components hien tai vao 2 scope (Class C / Full) bang 3-Round RCA. Ket qua classification quyet dinh component nao xuat hien trong Table 1, Table 2, hoac ca hai.

**Compass:** VVV-QMRF-EX — intelligence only, flag K-PENDING-RCA, stress points
**Method:** 3-Round RCA x 5-Why x scoring threshold 4/5

### Round 1 — Per-Component Scope Classification

| Component | Current Risk | Class C Impact | VVV-QMRF Full Impact | Classification | Project Value |
|-----------|-------------|----------------|----------------------|----------------|---------------|
| phi-map K→B(H) | 18.0 (#1) | Does not block K9_E | Long-term foundation, Track B Phase 1-3 complete | **VVV-QMRF Full** | VVV-QMRF (Track B) |
| P10-NOISE | 18.0 (#2) | Noise analysis for K9_E genuine fit validation | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| T5 K_ctx | 18.0 (#3) | Input to K9_E f_perp via K_ctx parameter | Defined at Layer 1-2, observer set selection rule unformalized | **Shared (Both)** | VVV-QMRF Full (feeds Class C) |
| T4-H Steps 3-4 | 18.0 (#4) | Deferred, not blocking K9_E | N-observer colimit, structural gap at Layer 2 | **VVV-QMRF Full** | VVV-QMRF (Layer 2) |
| K9E-PAT | 12.0 (#5) | Internal consistency test for K9_E multiplicative pattern | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| K9_E implementations | 12.0 (#6) | Implementation divergence for K9_E numerical prediction | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| K5_prospective | 12.0 (#7) | Core to K9_E T8 bridge derivation | Axiom extension at Layer 1-2, conservative extension of K5 | **Shared (Both)** | VVV-QMRF Full (feeds Class C) |
| E1-E16 | 9.6 (#8) | Non-blocking BE grounding for K9_E | BE registration postulates, full framework foundation | **VVV-QMRF Full** | VVV-QMRF (BE Layer) |
| P10-TIM | 9.0 (#9) | Null-model N0 for K9_E validation, decision-locked | Not relevant beyond K9_E | **VVV-QMRF Class C** | VVV-QMRF Class C |
| BE↔QM mapping | 9.6 (#10) | Non-blocking documentation | Cross-domain category error, full framework foundation | **VVV-QMRF Full** | VVV-QMRF (BE-QM bridge) |

#### 5-Why: T5 K_ctx = Shared (Both)

| # | Question | Answer |
|---|----------|--------|
| 1. | Why does T5 appear in both tables? | Because K_ctx is both a Class C input (to f_perp in K9_E) and a Layer 1-2 structural definition. |
| 2. | Why not classify as Class C only? | K_ctx's formal construction (via T3-morphism) lives at Layer 2, independent of K9_E. The observer set selection rule is a structural gap at Layer 1-2, not K9_E-specific. |
| 3. | Why not classify as Full only? | K_ctx is the DIRECT INPUT to f_perp(K_ctx) in K9_E. If K_ctx is hallucination, K9_E is invalid. Class C project MUST track it. |
| 4. | Why shared instead of splitting? | Splitting would create two K_ctx definitions — a structural violation. K_ctx is ONE definition used by both scopes. |
| 5. | Root cause: | K_ctx bridges Layer 2 ↔ Layer 3. Duality is inherent in the architecture, not a classification error. Shared = correct. |

**Verdict:** Shared (Both) — 5/5. Appears in Table 1 and Table 2 with identical scores.

#### 5-Why: K5_prospective = Shared (Both)

| # | Question | Answer |
|---|----------|--------|
| 1. | Why does K5_prospective appear in both tables? | K5_prospective is a Layer 1 axiom extension (conservative, v29) but its firing is core to K9_E's T8 bridge. |
| 2. | Why not classify as Full only? | K9_E's T8 bridge (derivation path for f_perp) depends on K5_prospective firing on hypothetical k_o*. Without it, K9_E derivation gap. |
| 3. | Why not classify as Class C only? | K5_prospective is a Layer 1 FROZEN axiom clause — it exists independent of K9_E. Any future Class D/E extension would also use it. |
| 4. | Why shared instead of splitting? | Same reason as T5: ONE definition, dual relevance. |
| 5. | Root cause: | K5_prospective is a structural axiom whose primary application is currently Class C but whose definition scope is Layer 1. Shared = correct. |

**Verdict:** Shared (Both) — 5/5. Appears in Table 1 and Table 2 with identical scores.

#### 5-Why: P10-NOISE = Class C Exclusive

| # | Question | Answer |
|---|----------|--------|
| 1. | Why is P10-NOISE Class C exclusive? | P10-NOISE is the alternative explanation for K9_E's genuine fit to Proietti D1 data. Existence scope = Class C. |
| 2. | Does P10-NOISE affect phi-map or T4-H? | No. phi-map and T4-H are structural conjectures independent of experimental noise in Proietti data. |
| 3. | Does P10-NOISE affect BE↔QM mapping? | Only indirectly (BE↔QM mapping risk is category error, not noise). Separate risk type. |
| 4. | Could P10-NOISE generalize to other VVV-QMRF data fits? | Conceptually yes (any future experimental fit could have noise risk), but the CURRENT P10-NOISE analysis is tied to Proietti D1 specifically. Future fits would have their own noise analysis. |
| 5. | Root cause: | P10-NOISE is scoped to K9_E empirical validation against Proietti 2019 D1. Its existence is bounded by Class C data. Full scope has no current data to which P10-NOISE applies. |

**Verdict:** Class C Exclusive — 5/5. Appears in Table 1 only.

### Round 2 — Scoring Consistency Check

| Check | Focus | Verdict | Score |
|-------|-------|---------|-------|
| C1 | Shared components (T5 K_ctx, K5_prospective) have identical H/W/A/Risk in both tables | PASS — scores cloned from v1.2, cross-verified | 5/5 |
| C2 | Class C exclusive components (P10-NOISE, K9E-PAT, K9_E impl, P10-TIM) do not hallucinate from Full scope perspective | PASS — Full scope exclusion correct: these are K9_E-specific, no structural relevance to broader VVV-QMRF | 5/5 |
| C3 | Full exclusive components (phi-map, T4-H, E1-E16, BE↔QM) do not hallucinate from Class C perspective | PASS — Class C scope documentation: these are VVV-QMRF Full components present in Table 1 for cross-reference only, tracked via Project field | 5/5 |

**Round 2 Aggregate:** 5.00/5 PASS (>= 4/5)

### Round 3 — Two-Table Structure Verification

| Check | Focus | Verdict | Score |
|-------|-------|---------|-------|
| T1 | Every component from v1.2 appears in correct table(s) per classification | PASS — 4 Class C exclusive (Table 1), 4 Full exclusive (Table 1 + Table 2), 2 Shared (Both) | 5/5 |
| T2 | No hallucination risk lost — cross-reference complete | PASS — all 10 v1.2 components present in Table 1 (rank preserved). Table 2 has 6 Full+Shared components. | 5/5 |
| T3 | Two-table structure self-consistent and independently readable | PASS — each table has its own header, version/timestamp, scope, summary. Shared components cross-referenced. | 4.5/5 |
| **Aggregate** | | **4.83/5 PASS (>= 4/5)** | |

---

## Changelog v1.2 -> v1.3

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **STRUCTURE** | File architecture | Single Top 10 table (v1.2), scope: "VVV-QMRF toan bo" | **Dual-table:** Table 1 (VVV-QMRF Class C, v1.3) + Table 2 (VVV-QMRF Full Scope, v1.0) | 3-Round RCA Classification Decision (4.83/5): 10 components span 3 buckets (Class C exclusive / Full exclusive / Shared). Explicit dual-table structure prevents scope ambiguity. |
| **ADD** | Project field | No Project classification | `Project` row added to every component field table | Requirement: each component needs explicit scope label. 3 buckets: VVV-QMRF Class C / VVV-QMRF (Full) / VVV-QMRF Full (feeds Class C) |
| **RECLASSIFY** | Current Top 10 table | "Top 10 Hallucination Risks (v1.2)" — ambiguous scope | **Table 1: VVV-QMRF Class C** — explicit Class C project scope with Project field showing cross-scope membership | Round 1 classification: current 10 components span 3 scopes. Table 1 name now reflects primary scope (Class C). |
| **ADD** | Table 2: VVV-QMRF Full Scope | N/A | **NEW** — 6 components (phi-map, T4-H, T5 K_ctx, K5_prosp., E1-E16, BE↔QM). Version v1.0. | Round 1: 4 components + 2 shared = 6 Full-scope hallucination risks. Independent table with own versioning. |
| **ADD** | Shared component rule | N/A | T5 K_ctx + K5_prospective appear in both tables. Any score change MUST sync both. | Round 2: shared components must have identical scores in both tables. |
| **ADD** | Timestamp on version | Ngay: 2026-05-24 | Ngay: 2026-05-24 16:22 UTC+7 | Requirement: "gio va ngay update" on table name |

## Changelog v1.1 -> v1.2

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **REMOVED** | [A-E3] beta universal | #1, Risk=22.5, `[AH-WARN] [RS-CRIT]` | **REMOVED khỏi Top 10** | RCA A-E3 Final Verdict (`897028b`): [A-E3] RECLASSIFIED → FREE PARAMETER (MEASUREMENT TARGET). H=5→2, A=0.5→0, Risk=6.0 (LOW). Khong con la assumption. Xem `RCA_A_E3_beta_universal_final_verdict.md`. |
| Re-rank | All #2-#10 | — | +1 rank | [A-E3] removal shifts all |
| **ADDED** | BE↔QM cross-domain mapping | — | #10, H=4, W=2, Risk=9.6 | Category error risk: mapping files chua boundary statement ro rang |

### Free Parameter Registry (thay thế [A-E3] trong Top 10)

| Parameter | Value | Classification | Anchor | Risk |
|-----------|-------|----------------|--------|------|
| **β** (K9_E suppression strength) | β=0.598 (Proietti D1 fit) | **FREE PARAMETER (MEASUREMENT TARGET)** | Measured, not derived. Analogous to α ≈ 1/137, G, g. | H=2, Risk=6.0 (LOW) |
| β universal | Modeling choice (Occam's razor) | **MODELING CHOICE** — cross-experiment verification pending | 1 dataset only (D1). 3-observer experiment can cross-check. | H=2, Risk=3.0 (LOW) |

## Changelog v1.0 -> v1.1

| Change | Component | Before | After | RCA Reason |
|--------|-----------|--------|-------|-------------|
| **SCORE CHANGE** | T5 K_ctx | H=6, Risk=21.6 (#2) | H=5, Risk=18.0 (#3) | [A-E1] ELIMINATED boi T9 (2026-05-24). T9 cung cap formal construction cho K_ctx — khong con la "missing definition." Residual risk: observer set selection chua formal hoa. |
| **SCORE CHANGE** | phi-map K→B(H) | H=6, Risk=21.6 (#1) | H=6, Risk=18.0 (#2) | W giam 3→2: structural weight reassessed — phi-map la Class D conjecture, khong block K9_E Class C. |
| **SCORE CHANGE** | P10-NOISE | H=5, Risk=22.5 (#3) | H=5, Risk=18.0 (#4) | A giam 0.5→0.2: anchor penalty reassessed — co experimental literature ve phase noise, khong con WEAK anchor. |
| Re-rank (all) | — | [A-E3] #1 (22.5), T5 #2 (21.6), phi-map #6 (18.0) | phi-map #1, T5 #3, P10-NOISE #2 | [A-E3] removed in v1.2; pre-removal T5 scored higher. Full score evolution tracked in Score Evolution table. |

Note: v1.0 changelog reconstructed from Score Evolution table + git history (`897028b`, `bc6f2fc`). Delta reasoning extracted from component status fields and T9 RCA verdict.

---

## Ranking Methodology (3-Round RCA)

### Round 1 — Identify candidates

Pool tu 4 nguon:
1. **K9_E Origin Investigation** (`rca_k9e_origin_investigation.md`): 19 components
2. **Technical Debt Inventory** (`rca_technical_debt_inventory_2026_05_24.md`): 15 debt items
3. **SOT Traceability Matrix** (`03_sot_traceability.md`): trace score thap nhat + anchor WEAK
4. **EX Compass** (`vvv-qmrf-ex/`): nodes flagged K-PENDING-RCA, structural gaps

**FILTER:** Chi tinh components la ASSUMPTION hoặc STRUCTURAL GAP. FREE PARAMETERS (như β) khong nam trong Top 10 — chung duoc do, khong derive.

### Round 2 — Score & Rank

**Risk Score formula:**

```
Risk = H x W x (1 + A)

  H = Hallucination score (0-10)
  W = Structural weight (1-3)
  A = Anchor penalty (0-0.5)

Tiebreaker: H (desc) -> W (desc) -> A (desc) -> Trace score (ascending)
```

**Trace score** = SOT traceability score (0-6) from `03_sot_traceability.md`. Lower score = fewer SOT anchors = higher hallucination risk. When H, W, A are equal, the component with lower Trace score ranks higher. If Trace score is also equal (persistent dead-tie), order is arbitrary with methodology note.

**E1-E16 SOT resolution:** E1-E16 trace score resolved to `2` (worst-case/minimum of range 2-4). Applies "weakest link" principle: risk of the 16-postulate group = risk of the postulate with weakest trace.

**E3 state change 2026-05-29 (commit cfbca7d):** E3 trace improved — §3d K1-K8 anchor (SOT-2), tier co-extensionality via K4 (Class D), §3e L4 type signature. E3 individual trace: ~2/6 → ~3-4/6. Group minimum (2/6) and Risk Score (9.6) **unchanged pending full weekly re-audit** of remaining E4-E16 postulates.

### Round 3 — Calibrate & Lock

Cross-check voi EX compass + BE SOT + RCA verdicts. Khoa ranking.

---

## Table 1: VVV-QMRF Class C — Top 10 Hallucination Risks

**Version:** v1.3 — 2026-05-24 16:22 UTC+7
**Scope:** VVV-QMRF Class C deliverable. Includes shared VVV-QMRF Full components that directly impact K9_E validation. "Project" field classifies each component's primary scope.
**Note:** Components marked "VVV-QMRF (Full)" or "VVV-QMRF Full (feeds Class C)" appear here because they rank in Top 10 hallucination risks relevant to Class C. Their primary structural scope is VVV-QMRF Full. See Table 2 for the independent Full-Scope ranking.

### Rank 1: phi-map — K -> B(H) structure-preserving map (Class D conjecture)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `phi: K -> B(H)` — conjectured structure-preserving map between K-space and bounded operators on Hilbert space |
| **Project** | VVV-QMRF (Track B) — long-term foundation, not Class C blocking |
| **Hallucination score (H)** | **6/10** (Vang — H CAO NHAT trong toan bo VVV-QMRF; Class D conjecture, chua duoc prove; Track B Phases 1-3 complete nhung chi la necessary conditions N_1-N_T) |
| **Structural weight (W)** | **2** (MEDIUM — quan trong cho VVV-QMRF long-term foundation nhung khong block K9_E Class C) |
| **Anchor penalty (A)** | **0.5** (WEAK — conjecture only; necessary conditions chua du de prove) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 6 x 2 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — Track B ongoing (Phases 1-3 complete, Phases 4+ pending). Class D conjecture; not actively blocking. RCA 5-Why (2026-05-25): "OPEN" misleading — phi-map is in long-term research program, not unattended gap. |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-DEFER]` |
| **EX compass** | Flag: phi-map la "largest structural unknown" trong VVV-QMRF |
| **Giai phap uu tien** | DEFER (long-term research program) |
| **Neu hallucination that:** | Khong anh huong K9_E Class C, nhung VVV-QMRF mat "bridge to QM" |
| **Deadline** | LOW (P3) — long-term |

### Rank 2: P10-NOISE — Non-uniform noise not ruled out

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Alternative explanation for K9_E genuine fit: non-uniform phase noise in Proietti experiment |
| **Project** | VVV-QMRF Class C — noise analysis for K9_E genuine fit validation |
| **Hallucination score (H)** | **5/10** (Vang — chua duoc kiem tra, co the invalidate genuine fit) |
| **Structural weight (W)** | **3** (HIGH — neu noise duoc confirm, K9_E mat evidence co so; genuine fit beta=0.598 tro thanh artifact) |
| **Anchor penalty (A)** | **0.2** (MODERATE — co experimental literature ve phase noise nhung chua ap dung vao Proietti setup) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 3 — Broken Trace → Type 4 (Structural Limitation). Noise analysis complete: random noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations (directional sensitivity + 4 data points). Cannot be resolved with published data. |
| **Status** | **ANALYZED — FAIL** (noise_threshold = 0.10 sigma RMS << 1.0 FAIL threshold). RCA status: `RCA_P10_NOISE_status_report_2026_05_24.md` (4.67/5). RCA methodology: `project_vvv_qmrf_class_c/04_governance/RCA_P10_NOISE_methodology_decision_2026_05_24.md` (4.77/5). Script: `project_vvv_qmrf_class_c/07_fits/noise_sensitivity_analysis.py`. Noise at ANY magnitude produces Delta_chi2 >= 5.35 in ~50% of realizations. Class C downgraded genuine→qualified. P10-NOISE remains OPEN as structural limitation — cannot be closed without 3-observer experiment or raw event data. |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-NOISE] [AH-EX]` |
| **EX compass** | Flag: EX co K-PENDING-RCA ve noise model. N_QM_VVV_00032 (Bhranti ↔ Decoherence) — structural analogue cho noise/registration error. |
| **Giai phap uu tien** | DONE: (1) Noise sensitivity analysis DA THUC HIEN — FAIL (noise_threshold=0.10 sigma). (2) Boundary statement DA THEM vao index.md. (3) Class C DA DOWNGRADE genuine→qualified. NEXT: 3-observer experiment hoac raw event data — chi 2 con duong dong P10-NOISE. |
| **Neu hallucination that:** | **DA XAC NHAN:** Noise CO THE giai thich Delta_chi2=5.35. K9_E directional sensitivity + 4 data points → ~50% random noise realizations produce "signal." 2.31sigma KHONG PHAI evidence cho K9_E suppression. Class C da downgrade. K9_E empirical leg KHONG CON — chi con structural leg. |
| **Deadline** | BLOCKED (khong co data) — chi co the dong qua 3-observer experiment hoac raw event data |

### Rank 3: T5 — K_ctx context set definition

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K_ctx(k_i, Exp)` — tap cac K-state tu observer khac, truy cap qua T3-morphism |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1-2 construction, direct input to K9_E f_perp |
| **Hallucination score (H)** | **5/10** (Vang — [A-E1] da ELIMINATED boi T9. K_ctx co formal construction. Residual: observer set selection chua formal hoa) |
| **Structural weight (W)** | **3** (HIGH — K_ctx la INPUT cua f_perp; neu K_ctx sai, K9_E modifier sai) |
| **Anchor penalty (A)** | **0.2** (MODERATE — T9 cung cap STRONG anchor cho construction; observer set selection rule van MODERATE) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap (observer set selection chua duoc formal hoa) |
| **Status** | **MONITORING** — [A-E1] da ELIMINATED (T9, 2026-05-24) |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-EX]` |
| **EX compass** | Flag: K_ctx computation depends on "observer set" |
| **Giai phap uu tien** | DERIVE (formal hoa observer set selection rule) |
| **Neu hallucination that:** | f_perp(K_ctx) undefined — K9_E khong the tinh |
| **Deadline** | MEDIUM (P2) |

### Rank 4: T4-H Steps 3-4 — N-observer colimit (DEFERRED)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | T4-H Steps 3-4 — N-observer K_joint colimit construction (global commutativity) |
| **Project** | VVV-QMRF (Layer 2) — N-observer colimit, deferred structural gap |
| **Hallucination score (H)** | **4/10** (Xanh duong — Steps 1-2 proven, Steps 3-4 DEFERRED) |
| **Structural weight (W)** | **3** (HIGH — blocks 3-observer prediction structural validation) |
| **Anchor penalty (A)** | **0.5** (WEAK — Steps 3-4 chua duoc prove) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 3 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — D-T4-BYPASS-01 "APPLIED" |
| **Full Label** | `[AH-LOW] [RS-HIGH] [AH-DEFER]` |
| **EX compass** | Flag: N-observer colimit la "structural bottleneck" |
| **Giai phap uu tien** | DEFER (cho resource) |
| **Neu hallucination that:** | 3-observer prediction ILLUSTRATIVE ONLY |
| **Deadline** | LOW (P3) |

### Rank 5: K9E-PAT — Multiplicative pattern not confirmed

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | K9_E multiplicative pattern (2BSM/1BSM ratio ~2) — NOT confirmed (ratio = -0.78 ± 1.72). Pattern UNTESTABLE voi data hien tai: sigma_ratio > ratio value. |
| **Project** | VVV-QMRF Class C — K9_E multiplicative pattern test |
| **Hallucination score (H)** | **5/10** (Vang — pattern predicted but UNTESTABLE; direction confirmed, magnitude unconstrained) |
| **Structural weight (W)** | **2** (MEDIUM — internal consistency test; postulate P=Tr*f_perp survives regardless of functional form) |
| **Anchor penalty (A)** | **0.2** (MODERATE — g=0.146 la PP-4 theoretical calibration, khong measured tu experimental data) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 3 — Broken Trace (data precision gap: 4 data points, sigma~0.04 → ratio error ±1.72) |
| **Status** | **ARCHIVED (v31)** — VERDICT C: UNRESOLVABLE with current data. "Ratio = -0.78" la red herring: ratio cua hai sub-sigma residuals. Ca hai model deu predict ratio ~2 (additive: 2.000, multiplicative: 1.913). 4 data points khong du de test pattern. P10-NOISE confirms. Deferred to K9-S12 optical experiment. RCA 4.92/5. See `04_governance/T1C_k9e_pat_resolution.md`. |
| **Full Label** | `[AH-LOW] [RS-LOW] [AH-ARCHIVED] [CLOSED-UNRESOLVABLE]` |
| **Deadline** | RESOLVED — deferred to K9-S12 experiment |

### Rank 6: K9_E two implementations — Additive vs Multiplicative divergence

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `k9e_predictor.py` (additive) vs `proietti_raw_fit.py` (multiplicative) — divergence tai beta > 0.3 |
| **Project** | VVV-QMRF Class C — K9_E implementation divergence |
| **Hallucination score (H)** | **4/10** (Xanh duong — implementation issue) |
| **Structural weight (W)** | **2** (MEDIUM) |
| **Anchor penalty (A)** | **0.5** (WEAK — ambiguity trong operationalization) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 4 x 2 x 1.5 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 2 — Missing Definition |
| **Status** | **MONITORING** — Divergence characterized (v31): additive vs multiplicative agree on PATTERN (ratio~2), differ on MAGNITUDE (~3.5x). 4 data points insufficient to select canonical. Canonical resolution deferred to K9-S12 optical experiment. See `04_governance/T1B_model_comparison_RCA.md`. RCA 5-Why (2026-05-25): was DOCUMENTED but counted as OPEN in summary — inconsistency fixed. MONITORING = active watch until K9-S12 data selects canonical. |
| **Full Label** | `[AH-LOW] [RS-MED]` |
| **Deadline** | P2 — duoc giam nhe. Van con 2 implementations, divergence characterized. K9-S12 experiment expected to resolve canonical choice. |

### Rank 7: K5_prospective — v29 axiom extension

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K5_prospective` — conservative extension cua K5 (v29). Firing tren hypothetical k_o*. |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1 axiom extension, core to K9_E T8 bridge |
| **Hallucination score (H)** | **5/10** (Vang — new axiom clause, 6/6 consistency checks) |
| **Structural weight (W)** | **2** (MEDIUM — cot loi cua T8 bridge, conservative extension) |
| **Anchor penalty (A)** | **0.2** (MODERATE — 6/6 checks, 3-Round RCA verified) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 4 — Assumption Masquerading (la axiom clause) |
| **Status** | **MONITORING** — "young axiom" |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | LOW (P3) |

### Rank 8: E1-E16 — 16 Registration-Layer Postulates (BE-derived)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | 16 postulates (E1-E16) derived from BE Pramana epistemology |
| **Project** | VVV-QMRF (BE Layer) — registration postulates, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — BE lineage ro rang, cross-domain interpretive) |
| **Structural weight (W)** | **2** (MEDIUM — BE grounding, K9_E khong depends on all 16) |
| **Anchor penalty (A)** | **0.2** (MODERATE) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (risk: BE as physical registration logic) |
| **Status** | **MONITORING** |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Deadline** | LOW (P3) |
| **Dead-tie note** | #8 E1-E16 = #9 BE↔QM (H=4=4, W=2=2, A=0.2=0.2, Trace=2=2 — all 4 tiebreakers equal). Arbitrary order; E1-E16 placed first by historical precedence (added to Top 10 v1.0, BE↔QM added v1.2). |

### Rank 9: BE↔QM cross-domain mapping — Category error risk

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Cross-domain links trong `refine_mapping.md` va `system_mapping.md` — BE concepts mapped to QM concepts |
| **Project** | VVV-QMRF (BE-QM bridge) — cross-domain mapping, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — mapping co BE SOT lineage, nhung cross-domain links co the bi nham thanh equivalence) |
| **Structural weight (W)** | **2** (MEDIUM — mapping files la foundation cua BE-QM connection; neu category error, toan bo BE-QM bridge bi nghi van) |
| **Anchor penalty (A)** | **0.2** (MODERATE — BE SOT strong, QM standard strong, nhung MAPPING giua chung la interpretive) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (BE epistemology mapped as QM registration logic) |
| **Status** | **MONITORING** — CLAUDE.md warning: "Treat cross-domain links as analogies or mappings unless the text explicitly argues for equivalence" |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **EX compass** | Flag: BE domain outside EX scope |
| **Giai phap uu tien** | DOCUMENT (boundary statement cho tung mapping link) |
| **Neu hallucination that:** | BE-QM mapping tro thanh pseudo-science |
| **Deadline** | LOW (P3) — documentation improvement |
| **Dead-tie note** | #8 E1-E16 = #9 BE↔QM (H=4=4, W=2=2, A=0.2=0.2, Trace=2=2 — all 4 tiebreakers equal). Arbitrary order; E1-E16 placed first by historical precedence (added to Top 10 before BE↔QM). |

### Rank 10: P10-TIM — Null-model N0 omitted (DORMANT)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Null-model N0: "QM with uniform visibility V=1" — omitted, needs raw event data |
| **Project** | VVV-QMRF Class C — K9_E null-model validation |
| **Hallucination score (H)** | **3/10** (Xanh duong — omitted analysis, khong hallucination) |
| **Structural weight (W)** | **2** (MEDIUM) |
| **Anchor penalty (A)** | **0.5** (WEAK — can raw event data khong co san) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 3 x 2 x 1.5 = **9.0** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 5 — Structural Gap (raw event data unavailable) |
| **Status** | **DORMANT** — DECISION-LOCKED (RCA Round 4); reactivates when raw event data available |
| **Full Label** | `[AH-LOW] [RS-LOW] [AH-DORMANT]` |
| **Deadline** | LOW (P3) — depends on external data |

---

### Risk Score Summary — Table 1: VVV-QMRF Class C (v1.3)

#### Phan phoi

| Risk Score Range | Count | Components |
|------------------|-------|------------|
| **20+ (CRITICAL)** | **0** | — (was 1: [A-E3], removed v1.2) |
| **15-20 (HIGH)** | 4 | phi-map (18.0), P10-NOISE (18.0), T5 K_ctx (18.0), T4-H (18.0) |
| **10-15 (MEDIUM)** | 3 | K9E-PAT (12.0), K9_E impl (12.0), K5_prosp. (12.0) |
| **5-10 (LOW)** | 3 | E1-E16 (9.6), BE↔QM (9.6), P10-TIM (9.0) |

#### Theo Status

| Status | Count | Components |
|--------|-------|------------|
| **OPEN** | 0 | — |
| **MONITORING** | 5 | T5 K_ctx, K5_prospective, K9_E implementations, E1-E16, BE↔QM |
| **DEFERRED** | 2 | phi-map, T4-H Steps 3-4 |
| **DORMANT** | 1 | P10-TIM |
| **ARCHIVED** | 1 | K9E-PAT |
| **RECLASSIFIED** | 1 | [A-E3] → FREE PARAMETER (removed v1.2) |

---

## Table 2: VVV-QMRF Full Scope — Top Hallucination Risks

**Version:** v1.0 — 2026-05-24 16:22 UTC+7
**Scope:** Full VVV-QMRF project hallucination risks. Includes structural framework components (phi-map Track B, T4-H, E1-E16, BE-QM bridge) plus shared components that feed into Class C.
**Cross-reference:** Components marked "VVV-QMRF Full (feeds Class C)" also appear in Table 1 with identical scores. See Shared Component Rule in header.

### Rank 1: phi-map — K -> B(H) structure-preserving map (Class D conjecture)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `phi: K -> B(H)` — conjectured structure-preserving map between K-space and bounded operators on Hilbert space |
| **Project** | VVV-QMRF (Track B) — long-term foundation, largest structural unknown |
| **Hallucination score (H)** | **6/10** (Vang — Class D conjecture, chua duoc prove; Track B Phases 1-3 complete nhung chi la necessary conditions N_1-N_T) |
| **Structural weight (W)** | **2** (MEDIUM — quan trong cho VVV-QMRF long-term foundation) |
| **Anchor penalty (A)** | **0.5** (WEAK — conjecture only; necessary conditions chua du de prove) |
| **Trace score (SOT)** | 1/6 |
| **Risk Score** | 6 x 2 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — Track B ongoing (Phases 1-3 complete, Phases 4+ pending). Class D conjecture; long-term research program. |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-DEFER]` |
| **Giai phap uu tien** | DEFER (long-term research program) |
| **Neu hallucination that:** | VVV-QMRF mat "bridge to QM" |
| **Deadline** | LOW (P3) — long-term |

### Rank 2: T4-H Steps 3-4 — N-observer colimit (DEFERRED)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | T4-H Steps 3-4 — N-observer K_joint colimit construction (global commutativity) |
| **Project** | VVV-QMRF (Layer 2) — N-observer colimit, deferred structural gap |
| **Hallucination score (H)** | **4/10** (Xanh duong — Steps 1-2 proven, Steps 3-4 DEFERRED) |
| **Structural weight (W)** | **3** (HIGH — blocks 3-observer prediction structural validation) |
| **Anchor penalty (A)** | **0.5** (WEAK — Steps 3-4 chua duoc prove) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 3 x 1.5 = **18.0** |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap |
| **Status** | **DEFERRED** — D-T4-BYPASS-01 "APPLIED" |
| **Full Label** | `[AH-LOW] [RS-HIGH] [AH-DEFER]` |
| **Giai phap uu tien** | DEFER (cho resource) |
| **Neu hallucination that:** | 3-observer prediction ILLUSTRATIVE ONLY |
| **Deadline** | LOW (P3) |

### Rank 3: T5 — K_ctx context set definition (Shared with Table 1)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K_ctx(k_i, Exp)` — tap cac K-state tu observer khac, truy cap qua T3-morphism |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1-2 construction, direct input to K9_E f_perp |
| **Hallucination score (H)** | **5/10** (Vang — [A-E1] da ELIMINATED boi T9. K_ctx co formal construction. Residual: observer set selection chua formal hoa) |
| **Structural weight (W)** | **3** (HIGH — K_ctx la INPUT cua f_perp) |
| **Anchor penalty (A)** | **0.2** (MODERATE — T9 cung cap STRONG anchor; observer set selection rule van MODERATE) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 3 x 1.2 = **18.0** (identical to Table 1) |
| **Risk Score band** | **HIGH** (15-19.9) |
| **Root cause type** | Type 5 — Structural Gap (observer set selection chua duoc formal hoa) |
| **Status** | **MONITORING** — [A-E1] da ELIMINATED (T9, 2026-05-24) |
| **Full Label** | `[AH-WARN] [RS-HIGH] [AH-EX]` |
| **Giai phap uu tien** | DERIVE (formal hoa observer set selection rule) |
| **Neu hallucination that:** | f_perp(K_ctx) undefined — K9_E khong the tinh |
| **Deadline** | MEDIUM (P2) |

### Rank 4: K5_prospective — v29 axiom extension (Shared with Table 1)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | `K5_prospective` — conservative extension cua K5 (v29). Firing tren hypothetical k_o*. |
| **Project** | VVV-QMRF Full (feeds Class C) — Layer 1 axiom extension, core to K9_E T8 bridge |
| **Hallucination score (H)** | **5/10** (Vang — new axiom clause, 6/6 consistency checks) |
| **Structural weight (W)** | **2** (MEDIUM — cot loi cua T8 bridge, conservative extension) |
| **Anchor penalty (A)** | **0.2** (MODERATE — 6/6 checks, 3-Round RCA verified) |
| **Trace score (SOT)** | 3/6 |
| **Risk Score** | 5 x 2 x 1.2 = **12.0** (identical to Table 1) |
| **Risk Score band** | **MEDIUM** (10-14.9) |
| **Root cause type** | Type 4 — Assumption Masquerading (la axiom clause) |
| **Status** | **MONITORING** — "young axiom" |
| **Full Label** | `[AH-WARN] [RS-MED]` |
| **Deadline** | LOW (P3) |

### Rank 5: E1-E16 — 16 Registration-Layer Postulates (BE-derived)

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | 16 postulates (E1-E16) derived from BE Pramana epistemology |
| **Project** | VVV-QMRF (BE Layer) — registration postulates, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — BE lineage ro rang, cross-domain interpretive) |
| **Structural weight (W)** | **2** (MEDIUM — BE grounding, K9_E khong depends on all 16) |
| **Anchor penalty (A)** | **0.2** (MODERATE) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (risk: BE as physical registration logic) |
| **Status** | **MONITORING** |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Deadline** | LOW (P3) |

### Rank 6: BE↔QM cross-domain mapping — Category error risk

| Thuoc tinh | Gia tri |
|------------|---------|
| **Component** | Cross-domain links trong `refine_mapping.md` va `system_mapping.md` — BE concepts mapped to QM concepts |
| **Project** | VVV-QMRF (BE-QM bridge) — cross-domain mapping, full framework foundation |
| **Hallucination score (H)** | **4/10** (Xanh duong — mapping co BE SOT lineage, nhung cross-domain links co the bi nham thanh equivalence) |
| **Structural weight (W)** | **2** (MEDIUM — mapping files la foundation cua BE-QM connection) |
| **Anchor penalty (A)** | **0.2** (MODERATE — BE SOT strong, QM standard strong, nhung MAPPING giua chung la interpretive) |
| **Trace score (SOT)** | 2/6 |
| **Risk Score** | 4 x 2 x 1.2 = **9.6** |
| **Risk Score band** | **LOW** (< 10) |
| **Root cause type** | Type 1 — Category Error (BE epistemology mapped as QM registration logic) |
| **Status** | **MONITORING** — CLAUDE.md warning |
| **Full Label** | `[AH-LOW] [RS-LOW]` |
| **Giai phap uu tien** | DOCUMENT (boundary statement cho tung mapping link) |
| **Neu hallucination that:** | BE-QM mapping tro thanh pseudo-science |
| **Deadline** | LOW (P3) — documentation improvement |

---

### Risk Score Summary — Table 2: VVV-QMRF Full Scope (v1.0)

#### Phan phoi

| Risk Score Range | Count | Components |
|------------------|-------|------------|
| **20+ (CRITICAL)** | **0** | — |
| **15-20 (HIGH)** | 3 | phi-map (18.0), T4-H (18.0), T5 K_ctx (18.0) |
| **10-15 (MEDIUM)** | 1 | K5_prosp. (12.0) |
| **5-10 (LOW)** | 2 | E1-E16 (9.6), BE↔QM (9.6) |

#### Theo Status

| Status | Count | Components |
|--------|-------|------------|
| **OPEN** | 0 | — |
| **MONITORING** | 4 | T5 K_ctx, K5_prospective, E1-E16, BE↔QM |
| **DEFERRED** | 2 | phi-map, T4-H Steps 3-4 |

#### Theo Classification

| Classification | Count | Components |
|----------------|-------|-------------|
| **VVV-QMRF Full exclusive** | 4 | phi-map, T4-H, E1-E16, BE↔QM |
| **Shared (Both tables)** | 2 | T5 K_ctx, K5_prospective |

---

## Score Evolution v1.0 -> v1.1 -> v1.2 -> v1.3

| Component | v1.0 Risk | v1.1 Risk | v1.2 Risk | v1.3 Table(s) | Trend |
|-----------|-----------|-----------|-----------|---------------|-------|
| [A-E3] beta universal | 22.5 (#1) | 22.5 (#1) | **REMOVED** (→ FREE PARAMETER) | — | ↓↓ |
| phi-map K→B(H) | 18.0 (#6) | 18.0 (#2) | **18.0 (#1)** | Table 1 + Table 2 | — |
| P10-NOISE | 18.0 (#4) | 18.0 (#3) | **18.0 (#2)** | Table 1 | — |
| T5 K_ctx | 21.6 (#2) | 18.0 (#4) | **18.0 (#3)** | Table 1 + Table 2 (Shared) | — |
| T4-H Steps 3-4 | 18.0 (#3) | 18.0 (#5) | **18.0 (#4)** | Table 1 + Table 2 | — |
| K9E-PAT | 12.0 (#5) | 12.0 (#5) | **CLOSED (v1.4)** | Table 1 | ↓↓ |
| K9_E implementations | 12.0 (#8) | 12.0 (#7) | **12.0 (#6)** | Table 1 | — |
| K5_prospective | 12.0 (#9) | 12.0 (#8) | **12.0 (#7)** | Table 1 + Table 2 (Shared) | — |
| E1-E16 | 9.6 (#7) | 9.6 (#9) | **9.6 (#8)** | Table 1 + Table 2 | — |
| P10-TIM | 9.0 (#10) | 9.0 (#10) | **9.0 (#10)** | Table 1 | — |
| BE↔QM mapping | — | — | **9.6 (#9)** | Table 1 + Table 2 | NEW |

---

## Free Parameter Registry

Khong nam trong Top 10 (khong phai assumption), nhung can duoc track:

| # | Parameter | Value | Unit | Classification | Caveat |
|---|-----------|-------|------|----------------|--------|
| FP-1 | **β** (suppression strength) | 0.598 (Proietti D1) | [0, 1) dimensionless | FREE PARAMETER — measured, not derived | 1 dataset only. Cross-experiment pending. |
| FP-2 | β_universal | Modeling choice | — | MODELING CHOICE (Occam's razor) | Will be tested by 3-observer experiment |

---

## Audit Schedule (v1.3)

| Component | Table(s) | Next Audit | Frequency | Trigger |
|-----------|----------|-----------|-----------|---------|
| phi-map K→B(H) | Both | 2026-06-30 | Monthly | Moi Track B milestone |
| P10-NOISE | Table 1 | 2026-05-31 | Weekly | Truoc khi public "genuine" claim |
| T5 K_ctx | Both | 2026-05-31 | Weekly | Moi khi T3/T9 duoc update. Sync both tables. |
| T4-H Steps 3-4 | Both | 2026-06-30 | Monthly | Khi co resource |
| K9E-PAT | Table 1 | N/A | On trigger (reactivate) | ARCHIVED; reactivate if K9-S12 experiment provides new data |
| K9_E implementations | Table 1 | 2026-05-31 | Weekly | Moi numerical prediction |
| K5_prospective | Both | 2026-05-31 | Weekly | Moi khi K5/K9_E thay doi. Sync both tables. |
| E1-E16 | Both | 2026-06-30 | Monthly | Moi khi BE SOT thay doi |
| P10-TIM | Table 1 | N/A | On trigger (reactivate) | DORMANT; reactivates khi raw event data available |
| BE↔QM mapping | Both | 2026-06-30 | Monthly | Moi khi mapping files thay doi |
| **β (Free Param)** | Table 1 | 2026-05-31 | Weekly | Moi experimental data moi |

---

## AHP Status Model Extension (v1.5)

**Purpose:** Mo rong AHP status model de phan biet "unactionable" risks (DORMANT) va "resolved-but-kept" risks (ARCHIVED). Tranh nham lan giua active monitoring, deferred, va truly dormant.

**RCA Decision:** 3-Round RCA (C2+C3, 4.33/5) — AHP thieu category cho DECISION-LOCKED (dormant, unactionable) va CLOSED-UNRESOLVABLE (archived, kept for reference). Them 2 status moi:

### Status Definitions

| Status | Meaning | Action | Example |
|--------|---------|--------|---------|
| **DORMANT** | Risk is real but unactionable — blocked by external dependency. Not currently monitored. Reactivates automatically when blocker resolves. | Remove from active monitoring; keep in table with `[AH-DORMANT]` label; re-evaluate when trigger fires. | P10-TIM: needs raw event data from Proietti |
| **ARCHIVED** | Risk has been RCA'd to exhaustion (RCA >= 4.5/5) and found UNRESOLVABLE with current data. Kept in table for historical traceability and to prevent re-litigation. | Reduce audit frequency to N/A; mark with `[AH-ARCHIVED]` label; keep in table for reference; reactivate only if new experiment provides qualitatively new data. | K9E-PAT: multiplicative pattern untestable (sigma_ratio > ratio value) |

### Status Lifecycle

```
OPEN → MONITORING → DEFERRED → DORMANT → (reactivate) → MONITORING
                                          ↘ ARCHIVED (end state)
OPEN → MONITORING → ARCHIVED (RCA >= 4.5/5, UNRESOLVABLE)
```

### Current Assignments (v1.5)

| Component | Old Status | New Status | Reason |
|-----------|-----------|------------|--------|
| P10-TIM | DECISION-LOCKED | **DORMANT** | Raw event data unavailable; reactivates when data released |
| K9E-PAT | CLOSED (v31) | **ARCHIVED** | RCA 4.92/5; UNRESOLVABLE with 4 data points; deferred to K9-S12 |

---

## 3-Round RCA Design Verification (v1.3)

| Round | Focus | Score | Findings |
|-------|-------|-------|----------|
| R1 | Classification RCA — per-component scope split via 5-Why for borderline cases (T5, K5_prospective shared; P10-NOISE exclusive). 10/10 components classified correctly. | 5/5 | 4 Class C exclusive + 4 Full exclusive + 2 Shared. All classifications backed by 5-Why analysis. No misclassifications. |
| R2 | Scoring consistency — shared components (T5 K_ctx, K5_prospective) have identical H/W/A/Risk in both tables. | 5/5 | T5: 5/3/0.2/18.0 in both. K5_prosp: 5/2/0.2/12.0 in both. 0 divergence. |
| R3 | Two-table completeness — all v1.2 risks covered, no risks lost. Table 2 self-contained and independently readable. | 4.5/5 | All 10 v1.2 components present in Table 1. Table 2 has 6 Full+Shared. Minor: Table 2 may need expansion as new Full-scope risks are identified from EX compass or technical debt inventory. |
| **Aggregate** | | **4.83/5 PASS (>= 4/5)** | |

---

*Top 10 Hallucination Risk Record v1.5 — Dual-table architecture: Table 1 (VVV-QMRF Class C, 10 components) + Table 2 (VVV-QMRF Full Scope, 6 components). 2 shared components (T5 K_ctx, K5_prospective) with identical scores in both tables. 0 CRITICAL + 4 HIGH + 2 MEDIUM + 2 LOW + 1 DORMANT + 1 ARCHIVED. 0 hallucination that su (9-10). Tiebreaker: H→W→A→Trace. AHP Status Model: 7 statuses (v1.5 extension). Next audit: 2026-05-31.*
