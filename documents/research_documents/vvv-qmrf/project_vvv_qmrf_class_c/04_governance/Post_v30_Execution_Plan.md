Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Class C — Post-v30 Execution Plan
# K9E-PAT Resolution → K9-S12 Paper → Experimental Path

**Version:** v1.1 (2026-05-27)
**Status:** Track 1 & Track 2 COMPLETED (arXiv submitted) — Track 3 (Experimental) ACTIVE
**Parent:** VVV-QMRF Class C (qualified, v32)
**RCA basis:** 3-Round RCA (aggregate 4.92/5) — IBM Quantum approach rejected (category error)
**Location:** `04_governance/Post_v30_Execution_Plan.md`

---

## MASTER CONTEXT BLOCK

*Dán block này vào đầu mỗi session làm việc với plan này.*

```
FRAMEWORK: VVV-QMRF K9_E — Registration-Layer Suppression
CLASS: Class C (qualified) — structurally testable, empirically UNCONFIRMED
       v30 downgrade (2026-05-24): noise sensitivity FAIL (0.10 σ << 1.0)

K9_E POSTULATE (P9):
  P(o | K) = Tr(E_o ρ) · [1 − β · f_perp(o, K_ctx)] / Z_E, β ∈ [0,1]

UNIVERSAL THEOREM (K9-S11c):
  f_perp(+1,H) − f_perp(−1,H) = −cos(θ) → vanishes at θ=π/2
  ALL existing EWF experiments use equatorial geometry → K9_E = QM

K9-S12 PROTOCOL: α = 31° tilt, one QWP insertion, N = 91,000
  δ⟨A₁B₂⟩ = −0.036 (20.8σ) + LF Genuine Facet 1 = +0.089 (8.6σ)

CURRENT BLOCKERS:
  P10-NOISE: noise_threshold = 0.10 σ RMS → 2.31σ signal = noise artifact likely
  K9E-PAT: 2BSM/1BSM ratio empirical = −0.78, multiplicative model predicts ~2
  → Both require resolution before public claims.

TWO CO-EXISTING K9_E MODELS:
  ADDITIVE (k9e_predictor.py):    E = E_QM·(1 − β·n_BSM·g_ctx), g_ctx ≈ 0.039
  MULTIPLICATIVE (proietti_raw_fit.py): E = E_QM·(1 − β·g_eff)^(n_BSM), g_eff = 0.146
  Agree at first order; diverge at β > 0.3.

IBM QUANTUM: REJECTED (RCA 4.92/5) — double category error.
  K9_E operates on K-space registration structure; IBM QPU has no K-space.
  → No hardware track. K9E-PAT resolved theoretically. K9_E testing needs optics.

THIS PLAN — 3 TRACKS:
  Track 1: K9E-PAT theoretical resolution (1-2 sessions, no hardware) — COMPLETED (v31)
  Track 2: K9-S12 paper writing (3-5 sessions, existing paper plan) — COMPLETED & SUBMITTED (v32)
  Track 3: Experimental path (future, needs optical lab) — ACTIVE
```

---

## PLAN ARCHITECTURE

```
POST-v30 EXECUTION
│
├─ Track 1: K9E-PAT RESOLUTION (COMPLETED)
│   ├─ [x] 1A: Compute additive model 2BSM/1BSM ratio
│   ├─ [x] 1B: RCA — additive vs multiplicative vs empirical (−0.78)
│   └─ [x] 1C: Decision — model/structural/noise? (Resolved: T1C Closed)
│
├─ Track 2: K9-S12 PAPER (COMPLETED & SUBMITTED TO arXiv)
│   ├─ [x] 2A: Numerical computations (Monte Carlo, sensitivity scans)
│   ├─ [x] 2B: Paper section writing (theorem → predictions → discussion)
│   └─ [x] 2C: Quality check → arXiv submission (Submitted on 2026-05-27)
│
└─ Track 3: EXPERIMENTAL PATH (ACTIVE — needs optical lab)
    ├─ 3A: K9-S12 optical experiment proposal
    └─ 3B: 3-observer experiment design (delta_M3 = −0.223, 11x)
```

---

## TRACK 1 — K9E-PAT Theoretical Resolution

**Priority:** HIGH — làm ngay
**Sessions:** 1-2
**Input:** `k9e_predictor.py` (additive), `proietti_raw_fit.py` (multiplicative), Proietti raw data
**Output:** RCA verdict — tại sao 2BSM/1BSM ratio empirical (−0.78) ≠ predicted (~2)?

### Why

K9E-PAT là open issue HIGH priority từ v29. Ba khả năng:

| # | Khả năng | Severity | Hành động nếu đúng |
|---|----------|----------|-------------------|
| A | Multiplicative model sai parameterization; additive model khớp | MEDIUM | Recalibrate với additive model |
| B | Cả hai model đều fail → K9_E functional form cần revision | HIGH | Mở K9-S13 sprint |
| C | Empirical ratio −0.78 là noise artifact (P10-NOISE confirms possible) | MEDIUM | Đóng K9E-PAT, defer sang experiment |

### Step 1A — Compute Additive Model Ratio

```
Additive model (k9e_predictor.py):
  E_K9E = E_QM · (1 − β · n_BSM · g_ctx)
  g_ctx ≈ 0.03889, n_BSM ∈ {0, 1, 2}

Method:
  Proietti CHSH settings: A₀=−π/4, A₁=π/4, B₀=0, B₁=π/2
  E_QM(x,y) = −cos(θ_Ax − θ_By)  [singlet]

  For β = 0.598 (genuine fit best-fit):
    n_BSM = x + y
    delta_xy = −β · n_BSM · g_ctx · E_QM(x,y)

  delta_1BSM = (delta₁₀ + delta₀₁)/2
  delta_2BSM = delta₁₁
  ratio_additive = delta_2BSM / delta_1BSM

Expected: ≈ 2.0 (linear in n_BSM)
  But: model calibrated for CHSH S, not per-correlator.
  Actual ratio may differ slightly due to E_QM variation across settings.

Output → 04_governance/T1A_additive_ratio.md
```

### Step 1B — Model Comparison RCA

```
5-WHY CORE:

W1: Why empirical ratio (−0.78) ≠ multiplicative prediction (~2)?
  → Model wrong OR data noise-dominated.

W2: Why would multiplicative model be wrong?
  → Assumes K_ctx compounds multiplicatively with n_BSM.
    If actual effect is additive → ratio prediction changes.

W3: Why does additive predict ratio ≈ 2?
  → Linear in n_BSM → ratio = 2 automatically (when E values equal).

W4: What pattern matches empirical −0.78?
  → Negative ratio = delta_2BSM and delta_1BSM have OPPOSITE SIGNS.
    Neither additive nor multiplicative predicts sign flip.
    → If empirical ratio truly negative → BOTH models structurally wrong.

W5: Is empirical ratio reliable?
  → P10-NOISE: noise_threshold = 0.10 σ RMS.
    4 data points, 50% chance random noise produces Δχ² ≥ 5.35.
    → Empirical ratio −0.78 likely PURE NOISE.
    → Most parsimonious explanation.

COMPARISON TABLE:
| Model                    | 2BSM delta | 1BSM delta | Ratio | Match −0.78? |
|--------------------------|-----------|-----------|-------|--------------|
| Multiplicative (g=0.146) | [TBD]     | [TBD]     | ~2.0  | NO           |
| Additive (g=0.039)       | [TBD]     | [TBD]     | [TBD] | [YES/NO]     |
| Empirical (Proietti raw) | [TBD]     | [TBD]     | −0.78 | —            |

VERDICTS:
  A: "Additive matches empirical → multiplicative parameterization wrong."
  B: "Both fail → K9_E functional form needs revision → K9-S13."
  C: "Empirical ratio = noise artifact (P10-NOISE) → UNRESOLVABLE without new data."

Output → 04_governance/T1B_model_comparison_RCA.md
```

### Step 1C — Resolution Decision

```
IF A: Recalibrate genuine fit with additive model.
      Update proietti_raw_fit.py. K9E-PAT → RESOLVED.

IF B: Open K9-S13 sprint. Explore non-multiplicative, non-additive f_perp.
      Must satisfy Born recovery (β=0 → QM exact).
      K9E-PAT → OPEN (structural revision).

IF C: Close K9E-PAT as UNRESOLVABLE with current data.
      P10-NOISE boundary applies to K9E-PAT too.
      Only K9-S12 optical experiment can resolve.
      K9E-PAT → DEFERRED.

Output → 04_governance/T1C_k9e_pat_resolution.md
Update → index.md K9E-PAT row, Top 10 hallucinations record.
```

### Track 1 Gate

```
GATE T1: After 1A-1C
  ✓ Resolved (A or C) → proceed to Track 2
  ✗ Structural issue (B) → open K9-S13, defer Track 2
```

---

## TRACK 2 — K9-S12 Paper Writing (COMPLETED & SUBMITTED)

**Priority:** HIGH — COMPLETED
**Sessions:** 3-5 (All executed)
**Input:** Paper plan `03_k9_sprints/k9_s12/paper_plan_single_waveplate_EWF.md`
**Output:** arXiv-ready preprint (`manuscript.tex` and `manuscript.md` Draft v94)

### Context

Paper plan đã hoàn thành xuất sắc (2026-05-26): 10 sections, 5 figures, 8 refs, và tất cả 11 sessions K9-S13-A đến K đã được thực hiện đầy đủ.

### Step 2A — Numerical Computations (2 sessions) — COMPLETED

```
[x] K9-S13-A: Sensitivity scan FOM(μ, η, Δθ)    → 07_fits/K9S12_sensitivity_scan.py
[x] K9-S13-B: Monte Carlo (10,000 runs)          → 07_fits/K9S12_monte_carlo.py
[x] K9-S13-C: Full correlator table              → 07_fits/K9S12_correlator_table.py
[x] K9-S13-D: Detection loophole η_crit          → 07_fits/K9S12_eta_critical.py

Output: CSV/JSON và 5/5 figures (fig1-fig5.png) tạo lập thành công.
```

### Step 2B — Section Writing (3-4 sessions) — COMPLETED

```
Order (per paper plan §7):

[x] K9-S13-E: §3  Theorem + Proof (core)                → ~600 words
[x] K9-S13-F: §4  Experimental Protocol (one QWP, 31°)  → ~600 words
[x] K9-S13-G: §5  Predictions + Expected Results        → ~700 words + 2 tables
[x] K9-S13-H: §6+7 Statistics + Robustness              → ~1200 words + 2 figures
[x] K9-S13-I: §8+9 Loopholes + Discussion               → ~1000 words
[x] K9-S13-J: §1+2+10+Abstract (intro, background, conclusion) → ~1400 words
[x] K9-S13-K: Full integration, consistency, formatting  → Final draft v94

Output → papers/paper_002/manuscript.md + manuscript.tex
```

### Step 2C — Pre-Submission QC — PASSED

```
[x] Every symbol defined at first use
[x] Every number has associated uncertainty
[x] Every figure has self-contained caption
[x] All 5 loopholes addressed (§8)
[x] Decision criteria cover all 4 outcome combinations (§5.3)
[x] Code (Supplemental S3) runnable by third party
[x] Abstract: no undefined acronyms
[x] Reference list: complete, consistent formatting
[x] FOM values consistent across §5, §6, §7
[x] §7.5 Robustness table: actual computed values, not placeholders
[x] K9E-PAT status from Track 1 reflected accurately

Output → papers/paper_002/QC_checklist.md (15/15 PASS)
```

### Track 2 Gate — CLOSED

```
GATE T2: QC PASS → arXiv submitted successfully! (2026-05-27)
```

---

## TRACK 3 — Experimental Path

**Priority:** MEDIUM — future
**Dependency:** Optical lab access (không có sẵn)

### 3A — K9-S12 Experiment Proposal

```
Formal proposal for optical EWF lab:
  - Equipment list + specs
  - Alignment procedure (step-by-step)
  - Expected timeline + budget
  - Risk assessment

Output → 04_governance/proposal/K9S12_experiment_proposal.md
```

### 3B — 3-Observer Experiment Design

```
delta_M3 = −0.223 at β=0.3 (11× amplification over 2-observer)
Requires T4-H Steps 2-4 (deferred).

Output → 04_governance/proposal/3observer_experiment_design.md
```

---

## FILE MAP (outputs from this plan)

```
04_governance/
├── Post_v30_Execution_Plan.md          ← THIS FILE
├── T1A_additive_ratio.md               Track 1 output
├── T1B_model_comparison_RCA.md         Track 1 output
├── T1C_k9e_pat_resolution.md           Track 1 output
├── paper/                              Track 2 output
│   ├── draft_v1.md
│   ├── QC_checklist.md
│   ├── figures/
│   └── supplemental/
└── proposal/                           Track 3 output (future)
    ├── K9S12_experiment_proposal.md
    └── 3observer_experiment_design.md
```

---

## DEPENDENCIES

```
TRACK 1 ← k9e_predictor.py, proietti_raw_fit.py, P10-NOISE RCA
TRACK 2 ← Track 1 verdict + paper_plan_single_waveplate_EWF.md
          + K9-S11c proof + K9-S12 proposal
TRACK 3 ← Track 2 paper + optical lab access (external)
```

---

## ESTIMATED EFFORT

| Track | Sessions | Hours | Difficulty | Blocker |
|-------|----------|-------|------------|---------|
| 1: K9E-PAT | 1-2 | 2-4 | MEDIUM | Không |
| 2: Paper | 3-5 | 6-10 | HIGH | Cần Track 1 xong |
| 3: Experiment | FUTURE | TBD | HIGH | Cần optical lab |

---

## DECISION GATES

```
GATE 0: START → Track 1 (no prerequisites)

GATE T1: After Track 1
  A (model fix)    → recalibrate → Track 2
  B (structural)   → K9-S13 → DEFER Track 2
  C (noise)        → document → Track 2 with caveat

GATE T2: After Track 2 QC
  PASS → arXiv submit → Track 3 (if lab available)
  FAIL → fix → re-check

GATE T3: After arXiv
  → K9-S12 experiment proposal (if lab access)
  → OR 3-observer design
```

---

## NOTES

**Model recommendation:**
- Track 1: Claude Opus (RCA + reasoning sâu)
- Track 2: Opus cho core (§3, §5, §9); Sonnet cho boilerplate (§1, §4, §8)

**EX compass:** EX_NODE_K5_CTX (KE-SC 4.0) + EX_NODE_K9_BETA (KE-SC 3.7). Compass only — no structure import.

**AHP:** Mỗi paper claim phải audit được. Top 10 cập nhật sau mỗi track.

---

*Post-v30 Execution Plan v1.0 — 2026-05-24. Located in 04_governance/. Replaces IBM Quantum approach (RCA rejected: double category error, 4.92/5). Three tracks: K9E-PAT theory → K9-S12 paper → Experimental path.*
