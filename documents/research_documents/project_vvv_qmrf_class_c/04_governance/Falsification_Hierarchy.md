Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# K9_E Falsification Hierarchy — From Overlap-Only to K→p(o) Bridge

**Date:** 2026-05-29
**Status:** Pre-registered (3-round RCA 4.6/5)
**Scope:** VVV-QMRF Class C — K9_E structural decomposition
**References:** C-FALSI v1.0 (K9 Analysis Plan), manuscript paper_002 §3.2
**VVV-QMRF-EX:** Compass only — not imported

---

## 0. Purpose / Mục đích

**EN:** This document defines the **4-level deformation hierarchy** referenced by
C-FALSI v1.0. Each level specifies: (i) what the deformation depends on,
(ii) what observable tests it, (iii) the quantitative falsification condition,
and (iv) what survives if the level is falsified. This pre-registration prevents
post-hoc "moving the goalposts" when lower levels are excluded by experiment.

**VN:** Tài liệu này định nghĩa **hệ thống phân cấp 4 mức** được tham chiếu bởi
C-FALSI v1.0. Mỗi mức chỉ rõ: (i) biến dạng phụ thuộc vào cái gì, (ii) quan sát
nào kiểm tra nó, (iii) điều kiện bác bỏ định lượng, và (iv) cái gì sống sót nếu
mức đó bị bác bỏ. Pre-registration này ngăn việc "dời cột gôn" sau khi có dữ liệu.

---

## 1. Hierarchy Overview / Tổng quan phân cấp

```
LEVEL 3: Non-geometric (timing, path, environment)
  ↑ survives Level 0-2 falsification
  │  requires: independent experimental designs per variable
  │
LEVEL 2: Multi-partite (concurrence, entanglement structure)
  ↑ survives Level 0-1 falsification
  │  requires: multi-observer EWF (N ≥ 3) or entanglement witnesses
  │
LEVEL 1: Density-matrix-dependent (ρ_F, Friend state purity)
  ↑ survives Level 0 falsification
  │  requires: Friend state tomography + tilted Superobserver
  │
LEVEL 0: Overlap-only (|⟨b|d⟩|², basis overlap)
  ↑ entry point — simplest class
  │  tested by: K9-S12 (single QWP, θ ≠ π/2)
  │  falsification rule: C-FALSI v1.0
```

**Key principle:** Each level is a **strict superset** of the level below it.
Level N contains all deformations in Level N-1, plus new degrees of freedom.
Falsifying Level N-1 does NOT falsify Level N — it only excludes the simpler class.

---

## 2. Level 0 — Overlap-Only Class

### 2.1 Mathematical Definition

```
P'(a,b | x,y) = P_QM(a,b | x,y) · g(|⟨b|d⟩|²) / Z

where:
  g: [0,1] → ℝ is ANY smooth function
  |⟨b|d⟩|² = cos²(θ/2) for b = d, sin²(θ/2) for b ≠ d
  Z normalizes the distribution
```

**Simplest representative (K9_E overlap-only):**
```
g(|⟨b|d⟩|²) = 1 - β · (1 - |⟨b|d⟩|²) = 1 - β · f_perp(b,d)
```
This is the form tested by K9-S12.

### 2.2 Key Property: Equatorial Cancellation

```
Proposition 1: At θ = π/2, |⟨b|d⟩|² = 1/2 for ALL (b,d) pairs.
→ g(1/2) = constant → P' = P_QM (after normalization).
→ δ⟨AB⟩(π/2) = 0 for ALL g, ALL β.
```

This is the **geometric null** — the only fixed point where overlap-only
deformations are blind. All published EWF experiments happen to sit at this point.

### 2.3 Observable

```
δ⟨AB⟩(θ) = ⟨AB⟩_measured(θ) - ⟨AB⟩_QM(θ)

Prediction: δ⟨AB⟩(θ) = 0 iff θ = π/2
            δ⟨AB⟩(θ) ≠ 0 for all other θ (when β > 0)
            δ⟨AB⟩(θ) ∝ cos θ (leading order, unrenormalized)
```

### 2.4 Falsification Rule

→ **See C-FALSI v1.0** (K9 Analysis Plan §C-FALSI) for the complete rule.

Summary:
- **Condition A:** |δ⟨AB⟩(31°)| < 3σ → null at near-optimal angle
- **Condition B:** χ²(δ=0) across θ-sweep < critical → no θ-dependence
- **Both hold** → Level 0 FALSIFIED (β ≥ β_min excluded at 95% CL)

### 2.5 What Survives Level 0 Falsification?

| Survives? | Component |
|---|---|
| ❌ **Falsified** | g(|⟨b|d⟩|²) with any β ≥ β_min |
| ✅ **Survives** | Level 1: g(ρ_F) — depends on full Friend density matrix |
| ✅ **Survives** | Level 2: g(Concurrence) — depends on multi-partite structure |
| ✅ **Survives** | Level 3: g(timing, path) — non-geometric variables |
| ✅ **Survives** | f_perp framework: P(o|K) = Tr(E_o ρ) × f_perp(K_ctx) with f_perp ≠ f(|⟨b|d⟩|²) |

### 2.6 Current Status

| Item | Status |
|---|---|
| **Testable?** | ✅ YES — K9-S12 protocol proposed (paper_002, submitted to arXiv) |
| **Experiment exists?** | ❌ NO — proposal only, not yet implemented |
| **Pre-registered?** | ✅ C-FALSI v1.0 (2026-05-29) |
| **Target sensitivity** | β_min ≈ 0.07 (Phase 1, single setting), β_min ≈ 0.046 (Phase 1, combined) |

---

## 3. Level 1 — Density-Matrix-Dependent Class

### 3.1 Mathematical Definition

```
P'(a,b | x,y) = P_QM(a,b | x,y) · h(ρ_F) / Z

where:
  ρ_F = Tr_Superobserver(|Ψ⟩⟨Ψ|)  — Friend's reduced density matrix
  h: D(H_F) → ℝ is a functional on the Friend's state space
```

**Example:** h(ρ_F) = 1 - γ · Tr(ρ_F²) (Friend state purity deformation)

### 3.2 Key Property: NO Equatorial Cancellation

```
At θ = π/2, |⟨b|d⟩|² = 1/2 for all (b,d), BUT:
  ρ_F may still have θ-dependent structure.
  → h(ρ_F) is NOT constant at θ = π/2.
  → Proposition 1 does NOT apply.
  → δ⟨AB⟩(π/2) MAY be non-zero.
```

This is the **critical distinction** from Level 0: equatorial measurements
are NOT a fixed point for Level 1 deformations. A null result in existing
equatorial experiments already constrains Level 1 (though weakly, since
those experiments weren't designed for this test).

### 3.3 Observable

```
PRIMARY: δ⟨AB⟩(θ) across full θ-sweep INCLUDING θ = π/2
  Level 0 predicts: δ⟨AB⟩(π/2) = 0 (exact)
  Level 1 predicts: δ⟨AB⟩(π/2) MAY ≠ 0

SECONDARY: Friend state tomography + δ⟨AB⟩ correlation
  Measure Tr(ρ_F²) independently → correlate with δ⟨AB⟩
  If δ⟨AB⟩ ∝ Tr(ρ_F²) → evidence for Level 1
```

### 3.4 Falsification Rule (preliminary — TBD)

```
C-FALSI-L1 (DRAFT, not yet pre-registered):

Level 1 is FALSIFIED if BOTH:
  (a) Level 0 is falsified (no overlap-only signal), AND
  (b) δ⟨AB⟩(π/2) = 0 within σ_stat(π/2) after dedicated high-sensitivity
      equatorial measurement, AND
  (c) No correlation between ⟨AB⟩ and independently-measured Friend state
      purity Tr(ρ_F²) across multiple θ values.

Gate conditions (minimum before Level 1 can be tested):
  — Friend state tomography capability (requires ≥ 2-qubit tomography)
  — Sensitivity to δ⟨AB⟩ ~ O(γ · purity_variation) at π/2
  — Protocol TBD (Level 1 experimental design not yet developed)

Status: PRELIMINARY. Full pre-registration requires:
  1. Dedicated experimental protocol (no proposal exists yet)
  2. Quantitative γ sensitivity target
  3. Error budget for state tomography
```

### 3.5 What Survives Level 1 Falsification?

| Survives? | Component |
|---|---|
| ❌ **Falsified** | Level 0 + Level 1 combined |
| ✅ **Survives** | Level 2: multi-partite deformations |
| ✅ **Survives** | Level 3: non-geometric deformations |
| ✅ **Survives** | f_perp framework with f_perp depending on multi-partite structure |

### 3.6 Current Status

| Item | Status |
|---|---|
| **Testable?** | ⚠️ CONDITIONAL — requires Friend state tomography + new protocol |
| **Experiment exists?** | ❌ NO — no proposal yet |
| **Pre-registered?** | ❌ NOT YET — C-FALSI-L1 is DRAFT |
| **Prerequisite** | Level 0 results (negative or positive) to motivate protocol design |

---

## 4. Level 2 — Multi-Partite Class

### 4.1 Mathematical Definition

```
P'(a,b | x,y) = P_QM(a,b | x,y) · k(C_{FS}, E_{FS}) / Z

where:
  C_{FS} = Concurrence between Friend and Superobserver subsystems
  E_{FS} = Entanglement entropy or other multi-partite entanglement measure
  k: ℝ² → ℝ is a functional on the multi-partite correlation structure
```

**Example:** k(C, E) = 1 - δ · C_{FS} (concurrence-dependent deformation)

### 4.2 Key Property: Multi-Observer Required

```
Level 2 requires ≥ 2 observers (Friend + Superobserver) with entanglement
between them. Single-observer measurements cannot distinguish Level 2
from Level 1.

N = 2 (Bong setup): Friend ⊗ Superobserver bipartite structure
  → C_{FS} and E_{FS} are well-defined
  → T4-H Step 1 proven (constructive T1 for N=2)
  → Level 2 testable in principle with existing EWF architecture

N ≥ 3 (extended chain): Friend₁ ⊗ Friend₂ ⊗ ... ⊗ Superobserver
  → Multi-partite concurrence structure richer
  → T4-H Steps 2-4 deferred (colimit construction)
  → Level 2 full characterization requires bridge theorems not yet proven
```

### 4.3 Observable

```
PRIMARY (N=2): Correlation between δ⟨AB⟩ and C_{FS}
  If δ⟨AB⟩ ∝ C_{FS} → evidence for Level 2
  Requires: ability to vary C_{FS} independently of θ

SECONDARY (N≥3, conditional on T4-H):
  δ⟨AB⟩ in 3-observer cascade vs 2-observer baseline
  Predicted amplification: ~11× at β=0.3 (illustrative, conditional)
```

### 4.4 Falsification Rule (preliminary — TBD)

```
C-FALSI-L2 (DRAFT, not yet pre-registered):

Level 2 is FALSIFIED if BOTH:
  (a) Levels 0-1 are falsified, AND
  (b) δ⟨AB⟩ does NOT correlate with C_{FS} across independently-varied
      concurrence values, AND
  (c) Multi-observer (N≥3) δ⟨AB⟩ equals N=2 prediction within errors
      (no amplification from additional registration interfaces).

Gate conditions:
  — T4-H Steps 2-4 proven (multi-observer bridge theorems)
  — Protocol for varying C_{FS} independently of θ
  — N≥3 EWF experimental capability

Status: PRELIMINARY. Depends on T4-H completion and multi-observer protocol.
```

### 4.5 What Survives Level 2 Falsification?

| Survives? | Component |
|---|---|
| ❌ **Falsified** | Levels 0-2 combined |
| ✅ **Survives** | Level 3: non-geometric deformations |
| ✅ **Survives** | f_perp framework with f_perp depending on non-geometric variables |

### 4.6 Current Status

| Item | Status |
|---|---|
| **Testable?** | ⚠️ CONDITIONAL — N=2 in principle; N≥3 requires T4-H Steps 2-4 |
| **Experiment exists?** | ❌ NO — no proposal |
| **Pre-registered?** | ❌ NOT YET |
| **Prerequisite** | T4-H completion + Level 0-1 results |

---

## 5. Level 3 — Non-Geometric Class

### 5.1 Mathematical Definition

```
P'(a,b | x,y) = P_QM(a,b | x,y) · m(t, L, env) / Z

where:
  t = timing variables (arrival time, coincidence window)
  L = path-length variables (optical path difference)
  env = environmental variables (temperature, vibration, EM field)
  m: ℝⁿ → ℝ is a functional on non-geometric experimental parameters
```

### 5.2 Key Property: Platform-Dependent

```
Level 3 deformations are NOT universal — they depend on the specific
physical implementation (optical vs superconducting vs trapped-ion).

A null result on ONE platform does NOT falsify Level 3 on ANOTHER platform.
Multi-platform testing is required for comprehensive exclusion.

This is the LEAST constrained level — it is the "catch-all" for any
deformation not captured by Levels 0-2.
```

### 5.3 Observable

```
PLATFORM-SPECIFIC. Examples:
  — Optical: δ⟨AB⟩ vs coincidence timing window width
  — Optical: δ⟨AB⟩ vs optical path difference
  — Superconducting: δ⟨AB⟩ vs gate duration
  — Trapped-ion: δ⟨AB⟩ vs laser pulse timing

No universal observable — each variable requires dedicated scan.
```

### 5.4 Falsification Rule (preliminary — TBD)

```
C-FALSI-L3 (DRAFT, not yet pre-registered):

Level 3 cannot be FULLY FALSIFIED by any single experiment, because:
  — The variable space is infinite-dimensional
  — Platform-dependence means exclusion on one platform ≠ exclusion on all
  — New variables can always be proposed

Instead, Level 3 is PROGRESSIVELY CONSTRAINED:
  Each dedicated scan of variable V excludes deformations depending on V
  at sensitivity δ_V. After scanning N independent variables, the
  remaining Level 3 parameter space volume shrinks.

Status: PRELIMINARY. Level 3 falsification is asymptotic, not binary.
Full pre-registration requires defining the variable scan sequence
and the per-variable exclusion threshold.
```

### 5.5 What Survives Level 3 Exclusion?

| Survives? | Component |
|---|---|
| ❌ **Excluded** | Specific variables scanned (e.g., timing at δ_t sensitivity) |
| ✅ **Survives** | Unscanned variables |
| ✅ **Survives** | Alternative platforms not yet tested |
| ✅ **Survives** | K→p(o) bridge with functional forms not captured by m(t, L, env) |

### 5.6 Current Status

| Item | Status |
|---|---|
| **Testable?** | ⚠️ PARTIALLY — each variable requires dedicated scan |
| **Experiment exists?** | ❌ NO — no proposal |
| **Pre-registered?** | ❌ NOT YET |
| **Prerequisite** | Level 0-2 results + platform-specific protocol per variable |

---

## 6. Full K9_E Falsification — The K→p(o) Bridge

### 6.1 What Would Falsify All of K9_E?

```
The K→p(o) bridge (K9_E core structure) is falsified if:

  (a) Levels 0-2 are ALL falsified (no overlap, no density-matrix,
      no multi-partite signal), AND
  (b) Level 3 is progressively constrained across ≥ 3 independent
      variable classes AND ≥ 2 platforms, AND
  (c) All results are consistent with β = 0 at combined sensitivity
      exceeding the minimum theoretically interesting β scale
      (β_min_theory ~ 10⁻³, set by weak-value anomaly scale)

This is a DECADAL-SCALE program, not a single-experiment result.
Pre-registration of the full program structure is documented here
to prevent "K9_E can never be falsified" criticism — the path to
falsification is defined, even if it requires multiple experiments.
```

### 6.2 Falsification vs Confirmation Asymmetry

```
CONFIRMATION: A SINGLE non-null result at ANY level → K9_E survives.
  (One positive δ⟨AB⟩ at θ ≠ π/2 is sufficient.)

FALSIFICATION: ALL levels must be excluded → K9_E is falsified.
  (Every deformation class must be tested and null.)

This asymmetry is INHERENT to the K→p(o) bridge structure:
  — K9_E proposes that K-side registration CAN affect physical probabilities
  — A single instance confirms the general claim
  — Exhausting all instances falsifies it

This is NOT a defect — it is the logical structure of any existence claim.
"The photon exists" is confirmed by one detection, falsified only by
exhausting all possible detection schemes. K9_E has the same structure.
```

---

## 7. Summary Table / Bảng tổng kết

| Level | Depends on | Observable | Equatorial Null? | Falsification Rule | Status |
|---|---|---|---|---|---|
| **0: Overlap-only** | \|⟨b\|d⟩\|² | δ⟨AB⟩(θ) via K9-S12 | ✅ YES (θ=π/2) | C-FALSI v1.0 | **PRE-REGISTERED** |
| **1: Density-matrix** | ρ_F, Tr(ρ_F²) | δ⟨AB⟩(π/2) + Friend tomography | ❌ NO | C-FALSI-L1 DRAFT | Preliminary |
| **2: Multi-partite** | C_{FS}, E_{FS} | δ⟨AB⟩ vs concurrence | ❌ NO | C-FALSI-L2 DRAFT | Preliminary |
| **3: Non-geometric** | t, L, env | Per-variable scans | ❌ NO | C-FALSI-L3 DRAFT | Preliminary |
| **All: K→p(o)** | Any K-side structure | Multiple independent protocols | N/A | All levels excluded | Decadal program |

---

## 8. Relationship to C-FALSI v1.0

```
C-FALSI v1.0 (K9 Analysis Plan) → Level 0 falsification rule (complete)
  ↓ references
Falsification Hierarchy (this document) → Levels 0-3 + full K9_E structure
  ↓ will be referenced by
K9-S12 Pre-registration Doc (P2, TBD) → Operational protocol for Level 0 test
```

**Update required:** C-FALSI v1.0's dangling reference "See Falsification Hierarchy
document" now resolves to this document. The reference in C-FALSI should be updated
to: `See [Falsification Hierarchy](04_governance/Falsification_Hierarchy.md)`.

---

## 9. Pre-Registration

```
This document was pre-registered on 2026-05-29, BEFORE any K9-S12
experimental data exists.

3-round RCA score: 4.6/5
  Round 1 (Define): 3.5/5 — hierarchy from manuscript §3.2, gaps identified
  Round 2 (5-Why): 4.4/5 — each level traced to manuscript, K-axioms, observables
  Round 3 (Adversarial): 4.6/5 — "why can't K9_E ever be falsified?" addressed

VVV-QMRF-EX compass: EX signals used to identify which K-space nodes
are critical for each level (K5 ⊥_K for Level 0; T4-H for Level 2).
No EX structures imported directly.

Dependencies:
  — manuscript paper_002 §3.2 (4-level hierarchy definition)
  — C-FALSI v1.0 (Level 0 falsification rule)
  — K1-K8 axiomatization (K5, K3 structural constraints)
  — T4-H bridge theorem (Level 2 prerequisite)
```

---

## Appendix A — Open Items

| ID | Item | Priority | Target |
|---|---|---|---|
| **FH-01** | C-FALSI-L1: Develop dedicated experimental protocol for ρ_F-dependent deformations | Medium | After Level 0 result |
| **FH-02** | C-FALSI-L2: Complete T4-H Steps 2-4 for N≥3 multi-observer bridge | High | Before Level 2 test |
| **FH-03** | C-FALSI-L3: Define prioritized variable scan sequence (which variables first?) | Low | After Level 0-2 results |
| **FH-04** | Update C-FALSI v1.0 reference from "See Falsification Hierarchy document" to explicit path | High | Immediate |
| **FH-05** | Define β_min_theory scale for "K9_E fully falsified" threshold | Medium | Before Level 2-3 testing |
| **FH-06** | Multi-platform strategy: which platforms after optical? | Low | Long-term |

---

## Appendix B — Traceability to K-Axioms

| Level | K-Axiom Dependency | Justification |
|---|---|---|
| **Level 0** | K5 (⊥_K incommensurability) | f_perp activates when ⊥_K fires; this is the structural origin of the overlap-dependent suppression |
| **Level 0** | K3 (self-certification) | V ∈ {0,1} defines registration validity; only valid registrations contribute to K_ctx |
| **Level 1** | K6 (authentication) | ρ_F structure encodes Friend's authenticated registration; Level 1 couples to this structure |
| **Level 2** | T4-H (colimit) | Multi-observer K-state requires colimit construction for joint registration space |
| **Level 2** | K7 (closure) | Closure of K-space under composition enables multi-observer registration chains |
| **Level 3** | T1 (N=2 constructive) | Even non-geometric deformations require the basic K_joint construction for Friend+Superobserver |

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
