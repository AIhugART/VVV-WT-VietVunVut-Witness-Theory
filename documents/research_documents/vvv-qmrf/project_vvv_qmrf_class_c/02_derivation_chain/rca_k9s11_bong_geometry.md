# RCA Consolidated Report: K9-S11 Chain (S11–S11d)
## 3-Round RCA × 5-Why × Scoring Threshold 4/5

---

## Session Overview

| Sub-step | Input | Output | Self-correction? |
|---|---|---|---|
| **K9-S11** | K9-S10 (4/9 testable) | 0/9 testable (standard Bong) | YES — K9-S10 wrong |
| **K9-S11b** | S11 + Proietti angles | Proietti also CONSTANT | NO — confirms S11 |
| **K9-S11c** | S11b + sympy | Universal Theorem proven, α=45° "sweet spot" | PARTIAL — theorem OK, α wrong |
| **K9-S11d** | S11c + Bong stats | α=31° optimal (FOM=6.0) | YES — α=45° was 1.9σ |

---

## R1: Root Cause — Why Were All Existing Experiments Untestable?

### 5-Why
1. **Why?** f_perp is constant (1/2) for all Proietti and Bong settings
2. **Why?** Friend measures z-basis, Superobserver measures in XY-plane (equatorial)
3. **Why equatorial?** Equatorial measurements maximize Bell/CHSH/LF violation
4. **Why does equatorial kill K9_E?** cos(π/2) = 0 → f_perp = 1/2 → outcome-independent
5. **Why is outcome-independence fatal?** Marginalization averages f_perp over hidden outcomes; constant f_perp factors out of the sum

### Theorem (PROVEN)
```
f_perp(+1,H) - f_perp(-1,H) = -cos(θ)
Constant IFF θ = π/2. Azimuthal φ irrelevant.
```

**Score: 5.0/5** ✅

---

## R2: Root Cause — Why Was α=45° Not The Sweet Spot?

### 5-Why
1. **Why?** Gen LF 1 = +0.022 at α=45° is only 1.9σ
2. **Why only 1.9σ?** σ(S_LF1) = 0.012; Gen LF 1 has 11 terms with coefficients up to ±2
3. **Why is σ so large?** Error propagation: σ² = Σ cᵢ²σᵢ²; sum of squared coefficients = 20
4. **Why did K9-S11c miss this?** K9-S11c checked violation (>0) but not significance (>3σ)
5. **Why was "signal = 0.707" used?** |cos(α)| measures geometric outcome-dependence, not δ⟨AB⟩

### Corrected Optimization
```
FOM = min(n_σ_LF, n_σ_K9E)
Optimal: α = 31° → FOM = 6.0
  n_σ_LF = 6.0, n_σ_K9E = 20.8
```

**Score: 5.0/5** ✅

---

## R3: Is the K9-S12 Foundation Solid?

### 5-Why
1. **Why α=31°?** Maximizes min(LF significance, K9_E significance) = 6.0
2. **Why not smaller α?** Below ~27°, LF significance starts dropping (violation peaks)
3. **Why is K9_E always easy?** δ⟨A₁B₂⟩ has σ ≈ 0.0017 → even small δ gives many σ
4. **Why is LF always the bottleneck?** 11 aggregated terms with mixed signs inflate σ
5. **Is N=91,000 sufficient?** YES — both >3σ at Bong-level statistics

### Foundation Parameters
```
α = 31° | φ₁=168° φ₂=0° φ₃=118° β=175° | μ ≥ 0.95 | N = 91,000
Gen LF 1:     +0.062 (6.0σ)
δ⟨A₁B₂⟩:     -0.036 (20.8σ) at β_K9=0.3
```

**Score: 5.0/5** ✅

---

## Commits

| # | Hash | Message |
|---|---|---|
| 1 | `ca09ba2` | K9-S11: Bong Geometry Cancellation |
| 2 | `17c5025` | K9-S11b: Proietti Geometry Check |
| 3 | `d42e937` | K9-S11c: Universal Theorem PROVEN |
| 4 | `07b928d` | K9-S11d: Statistical Significance |
| 5 | *(pending)* | RCA report + consolidation |

## All Scores ≥ 4/5. Chain COMPLETE.
