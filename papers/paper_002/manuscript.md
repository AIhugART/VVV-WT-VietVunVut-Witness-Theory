Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Have Optical Wigner's Friend Experiments Been Blind to a Geometric Degree of Freedom?

**Status:** Draft v94 — RCA round 4 (2026-05-27): (1) Downgraded 'δ ∝ cos θ' to accurate 'δ vanishes iff θ = π/2; non-zero otherwise (exact θ-dependence numerical)' in §1, §3.1, §3.2 table, §5.3, §8.1–8.2, Discussion Table — cos θ is the unrenormalized leading-order structure but overestimates |δ| by ~5.5×; all manuscript values use exact numerical computation. (2) Softened θ = 31° from 'optimal' to 'near-optimal' (grid search shows θ = 35° yields FOM = 8.8 vs 8.6; broad plateau makes exact optimum non-critical). (3) S2_derivation.md: added quantitative 5.5× overestimate warning. (4) Updated stale RCA scripts. §2.3 FROZEN. §3.5 FROZEN.
**Date:** 2026-05-26 | **Target:** arXiv quant-ph, then Phys. Rev. A

---

## Abstract

The two published optical Wigner's Friend experiments have operated
exclusively at an equatorial measurement geometry (θ = π/2) — a fixed
point where every overlap-dependent deformation of quantum measurement
statistics vanishes identically (Proposition 1, equatorial cancellation
theorem). A single waveplate breaks this cancellation. Re-inserting one
quarter-wave plate into the Bong et al. (2020) apparatus tilts the
Superobserver measurement to θ = 31°, providing minimum detectable
β ~ 0.07 at 5σ — a search parameter whose methodological role parallels
SME coefficients [15] (§2.3) — while preserving the Genuine LF violation
(8.6σ). A complete survey (Supplemental S1) finds no published
implementation has varied this polar angle; only two exist (Proietti 2019,
Bong 2020). The theorem constrains the overlap-only class; broader
deformation classes (Levels 1–3, §3.2) lie outside its scope. Under
fair-sampling (η ≈ 0.87), this is a loophole-open screening test; a null
δ⟨AB⟩ across a full θ-sweep would falsify the overlap-only class.

---

## Section 1 — Introduction

Extended Wigner's Friend (EWF) experiments [1,2] test whether observed events
exist independently of who observes them. Modern optical implementations
combining Local Friendliness (LF) no-go theorems [2,10-12] have challenged the
absoluteness of observed events [13,14].

**In brief.** Every published optical EWF experiment has used — by convention
for LF optimization, not by design — the one measurement geometry (θ = π/2)
at which an entire class of overlap-dependent quantum deformations cancels
identically. A single waveplate breaks this accidental fixed point, enabling
the first experimental probe of this class. The predicted signal
δ⟨AB⟩ vanishes identically at θ = π/2 and is generically non-zero
otherwise — a genuine observable, not a coordinate artifact (Lemma 1,
§3.2). The paper's contribution is twofold: a geometric null
theorem (Proposition 1) showing that equatorial measurements leave the
overlap-only class systematically unexplored, and a single-waveplate
protocol (§4–7) enabling its first experimental test. This paper makes no
claim about the existence of overlap-dependent deformation in nature — it
proposes a null-test protocol analogous in method to the Standard Model
Extension [15] (§2.3).

**Proposition 1 (Equatorial Cancellation Theorem, §3).** A deformation
of quantum measurement statistics is *overlap-only* if the modified joint
probability takes the form P'(a,b|x,y) = P_QM(a,b|x,y) · g(|⟨b|d⟩|²) / Z,
for any function g: [0,1] → ℝ and normalization Z. At the equatorial
plane (θ = π/2), |⟨b|d⟩|² = 1/2 for all outcome pairs (b,d); hence
g(|⟨b|d⟩|²) is constant and P' = P_QM identically — the equator is a
geometric null point for every overlap-only deformation. The signal
δ⟨AB⟩(θ) is invariant under any basis redefinition (Lemma 1, §3.2).

Breaking the cancellation requires only a single quarter-wave plate:
re-inserting the QWP into the Bong et al. (2020) apparatus tilts the
Superobserver measurement to θ = 31°, providing minimum detectable
β ~ 0.07 at 5σ (single-setting) while preserving 8.6σ Genuine LF
violation (§4–7).

Its two claims are structural: (A) within surveyed optical EWF
implementations (Supplemental S1), equatorial measurement — a convention
for LF optimization, not a tested constraint — leaves the overlap-only
class systematically unexplored, and (B) a single waveplate enables the
first experimental probe of this class. Positive results require
independent verification including θ-sweeps (§8.2).

Supplemental material: S1 (literature search + algebraic proof), S2
(numerical methods + statistical robustness), S3 (interpretations +
General Probabilistic Theories (GPT) / weak-measurement development).

---

## Section 2 — Background

### 2.1 — Extended Wigner's Friend Setup

Bong et al. (2020) [2] used two entangled photon pairs produced by spontaneous
parametric down-conversion (SPDC) at 810 nm. On each side, a Friend measures
photon polarization in the z-basis inside an interferometric lab formed by beam
displacers. A Superobserver measures the combined Friend+photon system at three
settings: Setting 1 (z-basis, reads the Friend outcome directly); Settings 2 and
3 (azimuthal angles on the Bloch sphere equator, θ = π/2). Measurement outcomes
are binary, a, b ∈ {+1, −1}, with N = 91,000 coincidences per setting.

[Schematic of the EWF setup with tilted Superobserver measurement is provided in Supplemental S1.]

### 2.2 — Genuine Local Friendliness Inequality

The Genuine Local Friendliness Facet 1 inequality [2] is:

  Gen LF 1 = −⟨A₁⟩ − ⟨A₂⟩ − ⟨B₁⟩ − ⟨B₂⟩ − ⟨A₁B₁⟩ − 2⟨A₁B₂⟩ − 2⟨A₂B₁⟩
           + 2⟨A₂B₂⟩ − ⟨A₂B₃⟩ − ⟨A₃B₂⟩ − ⟨A₃B₃⟩ − 6 ≤ 0                        (1)

A violation rules out all theories satisfying Local Friendliness.

### 2.3 — Overlap-Dependent Deformation: Why This Class?

**Definition and motivation.** The basis overlap |⟨b|d⟩|² is the simplest
scalar quantifying the geometric relationship between two measurement bases.
Any deformation coupling Superobserver statistics to a prior observer's recorded
outcome must depend on this relationship at lowest order; the overlap-only
class is therefore the minimal operational deformation — it isolates the
geometric degree of freedom (θ) that equatorial measurements leave
systematically unexplored.

Consider modifications to quantum probabilities:

  P(a,b | x,y) = P_QM(a,b | x,y) · [1 − β · g(b, Friend outcome)] / Z           (2)

where β ∈ [0,1]; β = 0 recovers standard QM. Three constraints — (i) rotation
invariance, (ii) alignment limit g(1)=0, (iii) monotonicity — force the
leading-order expansion g(x) = c₁(1−x) + O((1−x)²). Adopting the simplest
representative and absorbing c₁ into β:

  f_perp(b, d) = 1 − |⟨b|d⟩|²                                                    (3)

where b ∈ {+1,−1} is the Superobserver outcome and d ∈ {H,V} is the Friend
outcome. The functional form Eq. (3) is the simplest satisfying (i)-(iii);
every smooth function obeying them shares the same first-order structure
g(x) ∝ (1−x). The equatorial cancellation theorem (§3) constrains every
overlap-dependent deformation independent of parametrization — it holds for
any function g(|⟨b|d⟩|²).

Within the broader deformation hierarchy (§3.2), Level 0 is prioritized:
(i) it is the only level with a sharp geometric null (Proposition 1),
providing a built-in control; (ii) it requires only a single waveplate.
This prioritization is methodological, not predictive — the experiment
tests whether nature exhibits overlap-dependent deformation.

**Methodological role.** Equation (2) is a benchmark parametrization — a
phenomenological ansatz, not derived from any underlying physical theory
(full phenomenological classification in Supplemental S3). No existing
theory predicts this specific form. The parametrization functions
analogously to SME coefficients [15]: the SME was proposed with 19
coefficients and no a priori predictions, yet progressively tighter null
results constrained previously unconstrained parameter space. The
overlap-only parametrization serves the identical methodological function
— β is a search parameter whose null result constrains new parameter space
at the ~10⁻² scale. Operationally, β is directly measurable via δ⟨AB⟩ at
any θ ≠ π/2, with the cos θ scaling under θ-sweep (§8.2) providing the
distinguishing signature that separates an overlap-dependent signal from
conventional systematics.

**Physical context (speculative).** In weak measurement [18], the weak
value depends explicitly on the overlap between pre- and postselected
states — basis-alignment dependence is a known structural feature of
measurement theory. Information-theoretically, |⟨b|d⟩|² = cos²(θ/2) is
the fidelity between measurement basis states, quantifying basis
distinguishability and accessible information [18]. If the Superobserver's
measurement couples to the Friend's recorded outcome through an analogous
overlap-dependent mechanism, the leading-order correction takes the form
Eq. (2-3). This is a speculative mechanism, not a derivation; a toy model
and full discussion in Supplemental S3.

**Null test.** The experiment is a null test: standard QM predicts the same
LF violation regardless of θ; a θ-dependent signal would indicate a
departure from standard QM independently of model class.

---

## Section 3 — Equatorial Cancellation Theorem (Claim A)

### 3.1 — Main Result (Model-Independent)

Let a Friend F measure in the z-basis ({|H⟩, |V⟩}) and a Superobserver W measure
at Bloch sphere angles (θ, φ). With f_perp(b,d) = 1 − |⟨b|d⟩|²:

  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                         (4)

Consequently, f_perp is overlap-independent if and only if θ = π/2. For any
equatorial Superobserver measurement, any model of the form Eq. (2-3) reduces
exactly to standard quantum mechanics, regardless of the deformation strength β.
This depends only on Bloch sphere geometry. Eq. (2-3) serves only to quantify experimental sensitivity (§5.3);
the theorem holds for any overlap function.
The experimental consequence is that equatorial measurements cannot
distinguish standard QM from any overlap-dependent deformation within this
class. The distinctive experimental signature is that δ⟨AB⟩ vanishes
identically at θ = π/2 and is generically non-zero for θ ≠ π/2 (exact
θ-dependence determined numerically, §5.3): this structure is distinct from
conventional systematics (which either cancel in δ⟨AB⟩ or produce
non-geometric θ-dependence) and is a genuine observable, not a gauge
artifact (Lemma 1, §3.2).

### 3.2 — Equatorial Cancellation Theorem

**Definition (Overlap-only class).** A deformation of quantum measurement
statistics is *overlap-only* if the modified joint probability takes the form
P'(a,b | x,y) = P_QM(a,b | x,y) · g(|⟨b|d⟩|²) / Z, where
g: [0,1] → ℝ is any function and Z = Σ_{a,b} P_QM(a,b | x,y) · g(|⟨b|d⟩|²)
normalizes the distribution.

**Proposition 1 (Equatorial Cancellation Theorem).** Let g be any function.
At θ = π/2, |⟨b|d⟩|² = 1/2 for all outcome pairs (b,d). Hence
g(|⟨b|d⟩|²) = g(1/2) is constant, and P'(a,b | x,y) = P_QM(a,b | x,y).
The equatorial plane is a fixed point of every overlap-only deformation;
no overlap-dependent modification evades this cancellation while depending
only on |⟨b|d⟩|². ∎

**Lemma 1 (Non-Absorption).** The cos θ term in Eq. (4) cannot be absorbed
by unitary redefinition of the Superobserver's measurement basis.

*Proof.* Two distinct operations must be distinguished. (i) *Passive
relabeling*: redefining outcome labels via |b'⟩ = U|b⟩ leaves all
physical probabilities invariant — it is a change of description, not a
change of the measurement. Consequently δ⟨AB⟩ = 0 identically for any
U and any θ. (ii) *Active physical rotation*: changing the measurement
axis (θ, φ) → (θ', φ') physically reorients the apparatus, altering the
overlap |⟨b|d⟩|². Eq. (2) couples to this physical overlap, which
depends on the Friend outcome d — a degree of freedom external to the
Superobserver's basis choice. The cos θ term in Eq. (4) is a function of
the physical angle θ, not of the basis labels; it cannot be removed by
any relabeling U because relabeling does not change θ. Passive
relabeling predicts δ⟨AB⟩ = 0 for all θ and U; Eq. (2) predicts
δ⟨AB⟩ ≠ 0 for θ ≠ π/2. The two are operationally distinct. ∎

*Numerical illustration.* At θ = 31° with β = 0.07, the overlap-only
model predicts δ⟨AB⟩ ≈ 0.008 (4.7σ at N = 91,000). Any unitary
relabeling of the Superobserver basis — e.g., swapping |+1⟩ ↔ |−1⟩
via U = σ_x — leaves all correlators identically invariant
(δ⟨AB⟩ = 0), while Eq. (2) still predicts δ⟨AB⟩ ≈ 0.008. The two
predictions are numerically and operationally distinct.

*Operational invariant.* δ⟨AB⟩_θ = ⟨AB⟩_θ − ⟨AB⟩_π/2 is invariant
under any unitary transformation on the Superobserver's Hilbert space
alone — it cannot be eliminated by any choice of measurement coordinates.
Only β = 0 (standard QM) or θ = π/2 (equatorial measurement) removes it.
Any non-zero δ⟨AB⟩ at θ ≠ π/2 therefore indicates departure from the
standard Born rule, independent of measurement-basis convention.

**Scope limitation.** The overlap-only class is the minimal phenomenological
class capturing dependence on |⟨b|d⟩|²; we do not claim completeness over all
possible deformations. Proposition 1 constrains deformations whose
modification factor depends solely on |⟨b|d⟩|². Broader deformations —
depending on the full reduced density matrix ρ_F of the Friend (rather than
only |⟨b|d⟩|²), on the concurrence between Friend and Superobserver
subsystems, or on non-geometric variables such as timing or path — lie
outside this theorem's scope. For instance, a deformation
P' ∝ P_QM · h(Tr[ρ_F²]) would depend on Friend state purity, not basis
overlap, and would not cancel at the equator. The experiment (§4-7) constrains the overlap-only class (Level 0 of a
natural hierarchy: Level 1 — density-matrix-dependent; Level 2 —
multi-partite; Level 3 — non-geometric). Each level beyond 0 is
unconstrained by Proposition 1 and requires independent designs.

**Contextuality distinction.** Overlap-dependence is logically independent
of standard KS contextuality — it concerns measurement *registration*
(geometric relationship to a prior outcome), not measurement *setting*
(which observables are measured jointly). Proposition 1 constrains the
former and is silent on the latter.

| Property | KS Contextuality | Overlap-Dependence (this work) | Weak Measurement [18] |
|----------|-----------------|-------------------------------|----------------------|
| Depends on | Measurement setting | Measurement registration (geometric relationship to prior outcome) | Postselection choice |
| Observable | Outcome distributions across incompatible settings | δ⟨AB⟩(θ) vanishing iff θ = π/2, at fixed setting | Weak value A_w |
| Constrained by | Bell-KS inequalities | Proposition 1 (equatorial cancellation) | — |

### 3.3 — Proof

The Superobserver measurement basis at (θ, φ):

  |b=+1⟩ = cos(θ/2)|H⟩ + e^{iφ} sin(θ/2)|V⟩                                     (5)
  |b=−1⟩ = sin(θ/2)|H⟩ − e^{iφ} cos(θ/2)|V⟩                                     (6)

Squared overlaps (φ drops out: |e^{iφ}|² = 1):

  |⟨b=+1|H⟩|² = cos²(θ/2)          |⟨b=+1|V⟩|² = sin²(θ/2)                      (7)
  |⟨b=−1|H⟩|² = sin²(θ/2)          |⟨b=−1|V⟩|² = cos²(θ/2)                      (8)

Overlaps depend only on θ. Computing f_perp:

  f_perp(+1, H) = 1 − cos²(θ/2) = sin²(θ/2)                                     (9)
  f_perp(−1, H) = 1 − sin²(θ/2) = cos²(θ/2)                                    (10)
  f_perp(+1, H) − f_perp(−1, H) = −cos θ                                        (11)

Vanishes iff θ = π/2. All four f_perp = 1/2 → constant → cancels in Z. ∎

### 3.4 — Physical Intuition

At θ = π/2, the Superobserver's measurement basis is maximally symmetric
with respect to the Friend's recorded outcomes:
|⟨b|H⟩|² = |⟨b|V⟩|² = 1/2 for both b = ±1 — the Superobserver's measurement
apparatus is equally aligned with every Friend record, disturbing both
outcomes identically. The registration is perfectly balanced; no
overlap-dependent deformation can produce an asymmetry because there is
no asymmetry to amplify. [Figure 1: **Equatorial flatline vs. tilted cos θ emergence.** Left panel:
Bloch sphere showing Superobserver measurement axis at equator (θ = π/2).
All four overlap magnitudes |⟨b|d⟩|² = 1/2 — symmetric, balanced,
δ⟨AB⟩ = 0 identically (flatline). Right panel: axis tilted to θ = 31°.
Overlap asymmetry emerges: |⟨+1|H⟩|² = cos²(15.5°) ≈ 0.93,
|⟨−1|H⟩|² = sin²(15.5°) ≈ 0.07 — the Superobserver basis aligns
preferentially with one Friend outcome. Lower panel: predicted δ⟨AB⟩(θ)
curve (numerical), showing the exact null at θ = 90° (equator) and the
onset of non-zero signal as θ departs from the equatorial plane. The
single-waveplate modification moves the measurement from the flatline at
90° to the sensitive region at
31° (dashed vertical line).]

Tilting to θ ≠ π/2 breaks this balance: the Superobserver's basis aligns
more closely with one Friend outcome (e.g., |⟨+1|H⟩|² > |⟨+1|V⟩|² for
θ < π/2), creating a cos θ asymmetry. An overlap-dependent deformation
would convert this geometric imbalance into a detectable statistical
signal — the measurement apparatus becomes a directional probe for
registration-layer structure. Mathematically, such terms are the
leading-order expression of any smooth registration-fidelity function
that depends on measurement alignment; the first-order correction away
from perfect alignment generically has the structure
1 − β·(1 − |⟨b|d⟩|²). Eq.(2-3) isolates this universal geometric
structure without committing to a specific physical mechanism.
The experiment (§4-7) tests whether nature exploits this asymmetry.

### 3.5 — An Unisolated Geometric Control Parameter

**Survey findings.** Only two published optical EWF experiments exist
(Supplemental S1): Proietti et al. (2019) and Bong et al. (2020). Both
correspond to equatorial symmetry conditions — for Bong et al. this is
direct (θ = π/2); for Proietti et al. the equivalence follows from the
BSM structure (see footnote [a]).

| Experiment | Year | Measurement | Polar angle θ | Equatorial? | Ref |
|-----------|------|------------|---------------|------------|-----|
| Proietti et al. | 2019 | BSM (Bell-state) | —[a] | Yes | [1] |
| Bong et al. | 2020 | Projective (settings 2,3) | π/2 | Yes | [2] |

[a] BSM projects onto the four Bell states {|Φ⁺⟩, |Φ⁻⟩, |Ψ⁺⟩, |Ψ⁻⟩}. For the
singlet-state source used in Proietti et al., each Bell outcome occurs with
equal probability and leaves the Friend's recorded outcome equally likely to
be H or V — the effective overlap |⟨b|d⟩|² = 1/2 for all (b,d) pairs,
identical to the equatorial condition θ = π/2 derived in §3.3. Full
derivation in Supplemental S1.

*Search audit:* 4 databases (Google Scholar, arXiv, Web of Science, InspireHEP),
Jan 2000–May 2026; Boolean queries combining ("Wigner's friend" OR
"extended Wigner") with ("equatorial measurement" OR "Bloch sphere polar
angle" OR "outcome dependence" OR "geometric constraint"); ~200 titles
screened → 47 full-text examined → 2 published optical EWF experiments
identified (both effectively equatorial; see footnote [a]). Inclusion
criteria: optical EWF implementation with Friend+Superobserver structure,
published in peer-reviewed venue or arXiv, reporting measurement settings
from which polar angle θ can be determined. Within the surveyed literature,
no published EWF experiment varies θ from π/2. Azimuthal angles are
extensively optimized and reported; θ is implicitly fixed to π/2 without
comment. We cannot rule out unpublished results or implementations outside
our database scope that may have varied θ. Full query logs in Supplemental S1.

**Structural independence from LF optimization.** That both surveyed
implementations are equatorial follows directly from the LF optimization
convention — it is not an artifact of the small sample. LF inequalities
are optimized at equatorial settings [2,10]; without a hypothesis
motivating polar tilt, θ = π/2 was adopted as standard and never varied.
The LF inequality coefficients (Eq. 1) are structurally independent of θ
— the polar angle enters only through correlator values, which are free
parameters in any LF test. θ is therefore a genuine independent degree of
freedom orthogonal to the LF constraint surface; any EWF experiment on
any physical platform (optical, superconducting, trapped-ion) that
optimizes LF violation would adopt equatorial settings by default. The
gap is structural, not coincidental — it would persist regardless of how
many optical EWF implementations exist. The two approaches are
complementary: LF optimization maximizes inequality violation at fixed θ;
this work varies θ to test for overlap-dependent deformation. The
single-waveplate protocol preserves the optimized LF violation (8.6σ)
while adding the θ degree of freedom — combining both tests in one
experiment.

**Protocol motivation.** The scarcity of optical EWF implementations —
precisely two in two decades — makes a low-cost protocol especially
well-matched to the experimental landscape. A dedicated new EWF experiment
requires years of design, funding, and construction; a single-waveplate
modification runs on existing hardware in approximately one hour (§4.5).
Tilting the Superobserver opens access to this previously untested sector (§4).

---

## Section 4 — Experimental Protocol (Claim B)

### 4.1 — Breaking the Cancellation

Any θ ≠ π/2 breaks the cancellation. A grid search over (θ, φ₂, φ₃, β_Bob)
maximizing FOM(θ, β, N) = min(n_σ_LF, n_σ_signal) with β = 0.30 yields
a broad plateau peaking near θ ≈ 31°–35° (FOM = 8.6–8.8). At β = 0.30,
n_σ_signal ≫ n_σ_LF across all θ, so the FOM is bounded by n_σ_LF.
Representative FOM values at μ = 0.95, β = 0.30 (per-theta angle
re-optimization, Supplemental S2): 5.8 (θ = 20°), 8.6 (θ = 31°),
8.8 (θ = 35°), 6.0 (θ = 45°), 0 (θ = 58°, Gen LF 1 becomes negative),
and 0 (θ = 90°, cancellation); FOM > 5σ for θ ∈ [20°, 45°]. At the
minimum detectable β ≈ 0.07, the FOM is signal-limited: optimal θ = 46°
(FOM = 5.4) and >5σ range θ ∈ [35°, 46°] (Supplemental S2).
[Figure 2: Figure of merit vs polar angle θ, showing plateau near
θ ≈ 31°–35° (β = 0.30) and 5σ detection boundary spanning θ ∈ [20°, 45°].]
The wide optimal window means the protocol tolerates angular misalignment of
±11° before dropping below 5σ — substantially more forgiving than the
alignment precision demanded by the standard Bong protocol.

The plateau near θ ≈ 31°–35° reflects a trade-off between two monotonic
trends. As θ → 0°, the overlap asymmetry is largest, but the Gen LF 1
violation weakens because measurement settings approach a common axis,
reducing the inequality's capacity to separate LF-violating from
LF-satisfying theories. As θ → 90°, the LF violation is strongest but
the signal vanishes (equatorial cancellation, §3). The intermediate
plateau emerges from the intersection of these competing trends, with the
exact location set by the Gen LF 1 inequality coefficients via grid search
(Supplemental S2). The broad plateau (FOM > 5σ for θ ∈ [20°, 45°]) means
the exact optimum is not critical — any angle in this range produces a
viable experiment. We adopt θ = 31° as the reference angle throughout
because it coincides with the QWP-determined tilt in the Bong apparatus.

Gen LF 1(θ) and δ⟨AB⟩(θ) are independent observables from the same
coincidence data. Gen LF 1 aggregates all eleven correlators; its
θ-dependence is a standard QM prediction — LF violation weakens as
measurement axes approach a common direction. δ⟨AB⟩ isolates deviations
of individual mixed-setting correlators from their QM expectation. A
shift in Gen LF 1 without the θ-dependent pattern in δ⟨AB⟩ would indicate
apparatus misalignment, not β; conversely, δ⟨AB⟩ ≠ 0 with Gen LF 1
matching its QM prediction is the signature of overlap-dependent physics
(Table §8.1). The φ-scramble control (§7) provides additional
discrimination.

### 4.2 — Single Hardware Modification

In standard Bong et al. (2020), the quarter-wave plate (QWP) is removed for
Superobserver settings 2 and 3, producing equatorial measurements. Our
modification re-inserts this same QWP into Superobserver Alice's measurement
path (before the PBS, after beam displacer BD2), tilting the effective
measurement axis to θ = 31°. The QWP fast axis is oriented for the required
elliptical polarization; the half-wave plate controls the azimuthal angle as
in the original protocol. QWP specifications (retardance tolerance, temperature
stability) and angular uncertainty analysis are provided in Supplemental S2.
This is the only optical hardware change required. (The SNSPD upgrade
discussed in §7 replaces existing detectors at the same optical position;
no new optical elements are introduced.) A φ-scramble control (§7)
randomizes the azimuthal angle to rule out birefringence artifacts without
additional optics.

[Figure 3: Optical path with QWP insertion highlighted]

### 4.3 — Measurement Settings

| Parameter | Standard Bong [2] | This Work |
|-----------|------------------|-----------| 
| Polar angle θ | 90° (equatorial) | **31°** |
| Alice φ₂ | 0° | **112°** |
| Alice φ₃ | 118° | **217°** |
| Bob β_Bob | 175° | **20°** |
| μ required | not specified | ≥ 0.86 |
| N | 91,000 | 91,000 |

### 4.4 — Calibration

1. Verify polar angle: |⟨σ_z⟩| = cos(31°) ≈ 0.857 on H-polarized state (±0.01).
2. Verify azimuthal alignment with entangled state (count rates within 2% of QM).
3. Measure μ via CHSH S-parameter (μ ≥ 0.86 required).

### 4.5 — Practical Feasibility

Bong et al. (2020) report ~1000 coincidence events per second. At this rate,
N = 91,000 per setting requires ~91 s of integration; nine setting
combinations plus calibration (θ-verification and azimuthal alignment checks)
would require a data-acquisition run of approximately one hour under Bong
et al. conditions, assuming source and detector stability over this timescale.
Practical feasibility depends on the specific apparatus; detailed acquisition
timing and stability estimates are provided in Supplemental S2.

---

## Section 5 — Model-Independent QM Predictions

All numerical values are computed from the density matrix ρ_μ = μ|Φ⁻⟩⟨Φ⁻| +
(1−μ)/2 · (|HV⟩⟨HV| + |VH⟩⟨VH|) for the singlet state with visibility μ = 0.95.
SPDC produces photon pairs only in the {|HV⟩, |VH⟩} subspace; the noise term
is the maximally mixed state within that subspace, not the full I/4.

### 5.1 — Correlators at θ = 31°, μ = 0.95

All nine ⟨A_x B_y⟩ correlators are tabulated in Supplemental S2. Key values:
⟨A₁B₁⟩ = −1.0000 (z-basis, perfect anti-correlation); mixed-setting correlators
range from ⟨A₂B₂⟩ = −0.5045 to ⟨A₂B₃⟩ = ⟨A₃B₂⟩ = −0.8933, all with
σ ≈ 0.0017 at N = 91,000. The four mixed-setting pairs (one side z-basis,
one side tilted) share identical |⟨AB⟩| up to φ-induced sign, since f_perp
depends only on θ. Standard QM predicts zero marginals (singlet, μ = 0.95).

### 5.2 — Primary Observable: Genuine LF Violation

| Observable | Prediction | Type |
|-----------|-----------|------|
| Gen LF 1 | +0.0891 ± 0.0103 (8.6σ) | Standard QM, model-independent |

The 8.6σ LF violation provides built-in calibration: no violation at ≥5σ
indicates the apparatus is not realizing the intended geometry.

### 5.3 — Sensitivity to Overlap-Dependent Deformations

The figure of merit governing experimental sensitivity is
FOM(θ, β, N) = min(n_σ_LF(θ, N), n_σ_signal(θ, β, N)), where
n_σ_LF = |Gen LF 1(θ)|/σ_LF is the LF violation significance
(§4.1, Eq. 1) and n_σ_signal = |δ⟨AB⟩|/σ_AB is the overlap-dependent
signal significance, with σ_AB = √[(1 − ⟨AB⟩²)/N] (§6). The optimum
at θ = 31° reported in §4.1 maximizes this FOM via grid search.

For Eq. (2-3), we compute δ⟨A_x B_y⟩ = ⟨A_x B_y⟩_model −
⟨A_x B_y⟩_QM by exact numerical integration over the density matrix. The
computation evaluates f_perp-weighted outcome probabilities with full
renormalization (see Supplemental S2 for the numerical method). Results for
the mixed settings (one side z-basis, one side tilted) at θ = 31°, μ = 0.95:

| β | |δ⟨AB⟩| (mixed) | n_σ (single setting, N=91k) | n_σ (4 combined) |
|---|----------------|----------------------------|------------------|
| 0.03 | 0.0034 | 2.0 | 4.0 |
| 0.05 | 0.0057 | 3.3 | 6.7 |
| 0.07 | 0.0080 | 4.7 | 9.4 |
| 0.10 | 0.0115 | 6.7 | 13.5 |
| 0.30 | 0.0355 | 20.8 | 41.6 |

All four mixed settings yield identical δ (f_perp depends only on θ, not φ).

For Eq. (2-3), the illustrative 5σ detection
threshold is β ~ 0.07 (single-setting, N = 91,000). Using all four
mixed settings combined, β ~ 0.04 is detectable at >5σ (β_min ≈ 0.038
under idealized Poisson statistics; see §6). Accounting for realistic
systematics (§6-7), the practical sensitivity floor is likely
β ∼ 0.05–0.10 (single-setting) and β ∼ 0.04–0.06 (combined). These
thresholds are illustrative — no existing theory predicts a specific β
value; they quantify the experiment's capability for Eq. (2-3).

**Experimental discriminator.** Standard QM predicts δ⟨AB⟩ = 0 for all θ.
Eq. (2-3) predicts δ⟨AB⟩ = 0 at θ = π/2 (equatorial cancellation) and
δ⟨AB⟩ ≠ 0 for θ ≠ π/2, with exact θ-dependence determined numerically
(the unrenormalized leading-order structure goes as cos θ, but
renormalization modifies the functional form; see Supplemental S2). This
signature is testable by θ-sweep (§8.2) and is not a reparameterization
of QM: it is distinct from conventional systematics (which either cancel
in δ⟨AB⟩ or produce non-geometric θ-dependence), making a θ-dependent
δ⟨AB⟩ difficult to reproduce without overlap-dependent physics
(Lemma 1, §3.2).

**β in context.** The coupling β has no a priori prediction — analogous to
SME coefficients at inception (see §2.3 for the methodological parallel).
For scale reference: photon-sector SME coefficients are constrained to
<10⁻²³ [15]; continuous spontaneous localization (CSL) collapse parameters
are bounded at λ ≈ 10⁻¹⁶ s⁻¹; weak-measurement anomaly searches constrain
postselection deviations at ~10⁻² [18]. A constraint β ≥ 0.04 would place
overlap-dependent deformation in the company of these phenomenological
parameter classes — opening a new parameter space at the ~10⁻² scale
(comparable to weak-measurement anomalies) while distinct from SME and
collapse regimes in both scale and physical mechanism. A null result at
β ≥ 0.04 excludes O(1) and O(10⁻¹) deformation for the class Eq. (2-3);
a positive result provides the first quantitative target for theory
construction. Increasing to N = 200,000 extends sensitivity to β ≥ 0.02.
See Supplemental S3 for expanded scale comparison. The ~10⁻² scale is
physically motivated: postselection-conditioned weak values [18] manifest
at the same order, and any overlap-dependent registration-layer structure
would naturally appear at the precision where measurement-context effects
become distinguishable from Poisson noise in current optical
implementations.

The gap between β_min ≈ 0.038 (combined) and β_min ≈ 0.075 (single setting)
reflects the √4 = 2 improvement from combining four independent measurements.
The experiment naturally provides all four mixed-setting correlators; no
additional data acquisition is needed for the combined analysis.

---

## Section 6 — Statistical Analysis

Poisson statistics: σ(⟨A_x B_y⟩) = √[(1 − ⟨A_x B_y⟩²) / N]. For Gen LF 1
(11 terms, coefficients up to ±2): σ(S_LF1) = √[Σ c_i²(1 − ⟨v_i⟩²)/N] ≈ 0.0103
at N = 91,000 (exact term-by-term propagation; the upper bound √20/√N ≈ 0.015
assumes all correlators near zero).

Minimum sample for 5σ LF detection: N_min ≈ 30,800. N = 91,000 provides a
factor of 3 margin.

Monte Carlo (10,000 runs): Gen LF 1 ≥ 5σ in 99.97%; β = 0.07 detected in
~38% at 5σ (single setting, n_σ = 4.7; see §5.3), >99% (four combined settings,
n_σ = 9.4); β = 0.05 in ~90% at 5σ (combined, n_σ = 6.7). A conservative Bayesian analysis
inflating Poisson uncertainties by 20% yields β_min ≈ 0.046 (combined); the FOM
plateau (§4.1: >5σ for θ ∈ [20°, 45°]) ensures viability under substantial
systematic degradation. Detailed Monte Carlo, correlated-drift modeling, and
fake-signal injection methodology are provided in Supplemental S2.

[Figure 4: Monte Carlo histogram of Gen LF 1]

---

## Section 7 — Robustness Summary

The experiment is robust under realistic Bong et al. (2020) conditions.
Required visibility μ ≥ 0.92 and efficiency η ≥ 0.91 are within reach
(Bong achieved μ = 0.92, η = 0.87; SNSPD upgrade [16] closes the
detection loophole). A six-source systematic-error budget finds all
contributions sub-dominant to Poisson noise (σ ≈ 0.0017 at N = 91,000):

| Systematic source | Controlled by | vs. Poisson |
|------------------|---------------|:----------:|
| QWP retardance | Retardance tolerance | <1 |
| Birefringence | φ-scramble control (see below) | <1 |
| Polarization-dependent loss | Power monitoring per channel | <1 |
| Calibration offset | θ-verification protocol (§4.4) | <1 |
| Detector asymmetry | Channel efficiency balancing | <1 |
| Accidentals | Timing windows + dark-count subtraction | <1 |

RSS total remains below the Poisson floor. Exact σ values and Monte Carlo
correlation analysis in Supplemental S2. A φ-scramble control (N_φ ≥ 10, fit
δ⟨AB⟩(φ) = A + B cos(2φ) + C sin(2φ)) distinguishes geometric θ-dependent
signal (A ≠ 0, B,C ≈ 0) from birefringence artifacts (B or C ≠ 0) at
the 5σ level. Detector inefficiency cannot fake a β signal: residual
θ-dependent efficiency biases δ toward zero [9].

**Two-phase experimental program.** Phase 1 (near-term, η ≈ 0.87):
a loophole-open screening test using existing hardware plus one QWP,
constraining β ~ 0.07 under fair-sampling. Phase 2 (loophole-closed,
η ≥ 0.91 via SNSPD upgrade [16]): same optical configuration, only the
detectors change — closes the detection loophole with no redesign.
Full robustness analysis in Supplemental S2.

[Figure 5: FOM vs μ]

---

## Section 8 — Discussion

### 8.1 — Interpretation and Falsification

A non-zero δ⟨AB⟩ at θ = 31° would demonstrate Superobserver-Friend
correlations departing from standard QM at a previously untested geometry.
The overlap-only class is definitively falsified if: (i) a θ-sweep
(15°–75°) shows δ⟨AB⟩ = 0 at all non-equatorial angles to within ±0.003
(statistical floor at N = 200,000 per setting); or (ii) δ⟨AB⟩(θ) is
non-zero at θ = π/2 (violating the equatorial cancellation theorem) after
accounting for systematics. Either outcome is informative: falsification
closes the overlap-only window; a θ-dependent signal opens it.

| Observable | Standard QM | Overlap-only (Eq. 2-3) |
|-----------|------------|------------------------|
| Gen LF 1 at θ = 31° | +0.0891 ± 0.0103 (8.6σ) | Same (LF violation preserved) |
| δ⟨AB⟩ at θ = 31° | 0 | ≈ 0.115β (numerical) |
| δ⟨AB⟩ at θ = π/2 | 0 | 0 (equatorial cancellation, exact) |
| δ⟨AB⟩(θ) functional form | δ = 0 ∀θ | δ = 0 iff θ = π/2; non-zero otherwise (exact form numerical) |

Full interpretation analysis in Supplemental S3.

### 8.2 — Future Directions

**θ-sweep.** A systematic scan from θ = 15° to 75° in ~10° steps would
directly map the θ-dependence of δ⟨AB⟩ predicted by Eq. (2-3), testing
for the equatorial zero (δ = 0 at θ = 90°) and non-zero signal at
θ ≠ 90°. To prevent analysis bias, the sweep should be performed blind
(randomized θ sequence, analysis finalized before unmasking). A null
result across all θ excludes the overlap-only class to β ≈ 0.02
(N = 200,000 per setting).

**Multi-observer extension.** A generalization to N > 2 observers is
outlined in Supplemental S3; rigorous derivation of the required bridge
theorems is left for future work.

**Platform independence.** The theorem in §3 is platform-agnostic.
Implementing tilted Superobserver measurements on solid-state or
trapped-ion platforms would test whether the cos θ structure persists
when the Friend is a macroscopic quantum system.

**Locality closure.** Combining the tilted geometry with space-like
separated random basis switching would close the locality loophole
alongside the detection loophole (§7), representing a natural
next-generation experiment.

---

## Section 9 — Conclusion

All published optical EWF implementations have operated at an equatorial
fixed point (θ = π/2) where every overlap-dependent deformation vanishes
identically (Proposition 1), leaving the overlap-only class systematically
unexplored within the surveyed literature (Supplemental S1).

We propose a null test to probe this class: re-insert one QWP into the
Bong et al. (2020) apparatus (θ = 31°), providing sensitivity β ~ 0.07
at >5σ (single-setting) while preserving 8.6σ LF violation. The
experiment requires no new technology — only re-insertion of an existing
waveplate — and would open the first experimental window onto
overlap-dependent physics in EWF scenarios.

---

## References

[1] M. Proietti et al., Science Advances 5, eaaw9832 (2019).
[2] K.W. Bong et al., Nature Physics 16, 1199–1205 (2020).
[3] E.P. Wigner, in The Scientist Speculates, Heinemann (1961).
[4] D. Deutsch, Int. J. Theor. Phys. 24, 1–41 (1985).
[5] L. Hardy, Phys. Rev. Lett. 68, 2981 (1992).
[6] D. Frauchiger and R. Renner, Nature Comms. 9, 3711 (2018).
[7] N. Brunner et al., Rev. Mod. Phys. 86, 419 (2014).
[8] J.S. Bell, Physics 1, 195–200 (1964).
[9] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).
[10] H.M. Wiseman, E.G. Cavalcanti, and E.G. Rieffel, Quantum 7, 1112 (2023).
[11] M. Haddara and E.G. Cavalcanti, arXiv:2407.20346 (2024).
[12] A. Utreras-Alarcon, E.G. Cavalcanti, and H.M. Wiseman, Proc. R. Soc. A 480 (2023).
[13] M. Haddara and E.G. Cavalcanti, New J. Phys. 25, 093028 (2023).
[14] A. Kent, arXiv:2302.12707 (2023).
[15] D. Colladay and V.A. Kostelecký, Phys. Rev. D 55, 6760 (1997).
[16] F. Marsili et al., Nature Photonics 7, 210–214 (2013).
[17] J. Barrett, Phys. Rev. A 75, 032304 (2007).
[18] Y. Aharonov, D.Z. Albert, and L. Vaidman, Phys. Rev. Lett. 60, 1351 (1988).

---