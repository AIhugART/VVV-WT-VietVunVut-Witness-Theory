# Supplemental S2: Derivation of Eq.(12) — K9_E Sensitivity Formula

## 1. f_perp values at polar angle theta

Superobserver basis at (theta, phi):

  |b=+1> = cos(theta/2)|H> + e^{i*phi} sin(theta/2)|V>
  |b=-1> = sin(theta/2)|H> - e^{i*phi} cos(theta/2)|V>

Squared overlaps with Friend z-basis (phi drops out):

  |<b=+1|H>|^2 = cos^2(theta/2)     |<b=+1|V>|^2 = sin^2(theta/2)
  |<b=-1|H>|^2 = sin^2(theta/2)     |<b=-1|V>|^2 = cos^2(theta/2)

f_perp(b,d) = 1 - |<b|d>|^2:

  f_perp(+1,H) = sin^2(theta/2)     f_perp(+1,V) = cos^2(theta/2)
  f_perp(-1,H) = cos^2(theta/2)     f_perp(-1,V) = sin^2(theta/2)

The key parameter: |f_perp(+1,H) - f_perp(-1,H)|/2 = |cos theta|/2.

At theta = 31 deg: |cos 31 deg|/2 = 0.8572/2 = 0.4286.

## 2. QM correlator for mixed setting (x=1, y=2)

Standard QM, singlet state with SPDC noise, visibility mu = 0.95:

  <A1 B2>_QM = -cos(theta)

For the SPDC noise model (noise within {|HV>, |VH>} subspace), both the
pure singlet and the noise term yield identical z-vs-tilted correlators
(-cos theta), so the mixed-setting correlator is mu-independent.
At modified Bong geometry (theta=31 deg): <A1 B2>_QM = -cos(31) = -0.8572.

## 3. K9_E-modified correlator

For the multiplicative model: P_K9E = P_QM * (1 - beta*f_perp)^(n_BSM) / Z
where n_BSM = number of BSM (non-z-basis) measurements in the setting pair.

For (1,2): Alice = z-basis (n=0), Bob = tilted (n=1) -> n_BSM = 1.

The K9_E correlator is computed numerically via weighted sums over f_perp
values with full renormalization (see K9S12_proposal.py, function
compute_k9e_correlators). The modification acts at the probability level:
P_K9E ∝ P_QM · (1 − β·f_perp), with Z = Σ P_QM · (1 − β·f_perp) ensuring
normalization. Because Z depends on β and θ, the correlator shift is not a
simple multiplicative factor — the renormalization couples all outcome pairs.

Numerical results at θ = 31°, μ = 0.95 (manuscript §5.3, S2_correlator_table):

| β | <A1B2>_QM | <A1B2>_K9E | δ |
|---|-----------|------------|----|
| 0.10 | −0.8572 | −0.8687 | −0.0115 |
| 0.30 | −0.8572 | −0.8927 | −0.0355 |
| 0.50 | −0.8572 | −0.9180 | −0.0609 |

The K9E modification makes the correlator more negative (enhanced
anti-correlation), not less — the renormalization shifts weight toward
outcome pairs with larger f_perp values, amplifying the geometric asymmetry.

## 4. First-order expansion

Expanding the renormalized probability to first order in β (BEFORE
renormalization by Z):

  δ⟨A1B2⟩ = −β · |cos θ| · ⟨A1B2⟩_QM² + O(β²)   [unrenormalized leading order]

At θ = 31°: ⟨A1B2⟩_QM = −0.8572, |cos θ| = 0.8572:
  δ ≈ −β · 0.8572 · 0.7347 = −0.6298·β   (unrenormalized)

**WARNING: This unrenormalized expansion overestimates |δ| by approximately
a factor of 5.5.** The ratio numerical/LO is nearly constant across β:

| β    | δ (LO)   | δ (numerical) | ratio |
|------|----------|---------------|-------|
| 0.01 | −0.0063  | −0.0011       | 0.181 |
| 0.07 | −0.0441  | −0.0080       | 0.182 |
| 0.10 | −0.0630  | −0.0115       | 0.183 |
| 0.30 | −0.1889  | −0.0355       | 0.188 |
| 0.50 | −0.3149  | −0.0609       | 0.193 |

The overestimate arises because renormalization (Z = Σ P_QM · (1 − β·f_perp))
contributes at the same order as the numerator shift: both are O(β), so the
ratio P'/P_QM involves a cancellation between numerator and denominator
corrections. The unrenormalized formula captures the correct **structural
dependence** (vanishes iff θ = π/2, non-zero otherwise) but not the correct
**magnitude**. All manuscript values (Table §5.3, β_min thresholds) use
exact numerical computation including full renormalization.

## 5. Sensitivity

sigma per setting (N = 91,000): σ = √[(1 − ⟨AB⟩²)/N] ≈ 0.0017.
Combined 4 mixed settings: σ_eff = σ/√4 ≈ 0.00085.

5σ detection thresholds (numerical, from manuscript §5.3):
  beta_min (single setting, 5σ) = 0.075
  beta_min (four combined, 5σ)  = 0.038

## Code

Full computation: 07_fits/K9S12_proposal.py, function compute_k9e_correlators().
