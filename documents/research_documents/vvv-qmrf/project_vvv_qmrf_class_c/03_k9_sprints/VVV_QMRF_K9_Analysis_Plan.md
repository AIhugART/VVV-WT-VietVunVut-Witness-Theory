# VVV-QMRF K9 Analysis and Identification Plan
# Bridge Axiom Selection: Binary Registration → Continuous Probability

**Version:** K9-Plan v1.0 (2026-05-23)
**Purpose:** Systematically analyze, evaluate, and select the K9 bridge axiom
that connects K-space binary registration states to continuous probability values.
**Execution order:** K9-S1 → K9-S2 → K9-S3 → K9-S4 → K9-S5 → K9-S6
**Output:** One selected and locked K9 candidate with class assignment,
derivation trace, and falsification rule.

---

## MASTER CONTEXT BLOCK
*Paste this block at the top of every K9 prompt session.*

```
FRAMEWORK: VVV-QMRF (VietVunVut Quantum Measurement Registration Framework)

FROZEN AXIOMS K1-K8:
  K1: K_R is a set of K-state tuples k=<M,o,cert,t,V> with cert-admission
      rule and t-injectivity (no two tuples share the same t)
  K2: (K_R, <_R) is a strict total order; timestamps are discrete
  K3: cert(k) = σ_R(M), determined intrinsically within K_R
  K4: V(k) = 1 by default on instantiation; V(k) = 0 for null k
  K5: V(k1) → 0 iff ∃k2 later in order such that k2 ⊥_K k1
      within shared C_K sphere with valid authority
  K6: Cross-registration authority Auth(k2→k1, C_K) = 1 iff
      same C_K sphere, V(k2)=1, k1 in scope
  K7: Registration closes at t_close when no K_joint demands remain
  K8: Cross-space embedding preserves V and all tuple fields

STRUCTURAL GAP (root cause requiring K9):
  K1-K8 produce only binary outputs:
    cert ∈ {0,1}
    V    ∈ {0,1}
    ⊥_K  ∈ {fires, silent}
  Standard QM requires continuous probability:
    P(o) ∈ [0,1]   via Born rule: P(o) = Tr(E_o ρ)
  No mechanism in K1-K8 maps binary states to continuous probability.
  K9 must provide this bridge.

MANDATORY CONSTRAINTS FOR ANY K9:
  C-BORN: When cert=1 ∧ V=1 ∧ ⊥_K silent → P(o|k) = Tr(E_o ρ)
          (Standard QM Born rule recovered exactly)
  C-NORM: Σ_o P(o|k) = 1 for all valid k (normalization)
  C-NONDIV: No division by zero for any k with V ∈ {0,1}
  C-PARAM: ≤ 2 free parameters (D1 provides 4 data points → DOF ≥ 2)
  C-TRACE: Every term in K9 must be traceable to K1-K8 or flagged ASSUMPTION
  C-FALSI: K9 must produce at least one falsifiable prediction

CLAIM CLASS DISCIPLINE:
  Class D: Conjecture. Internally consistent, not yet testable.
  Class C: Testable claim. Rigorously derived from K1-K8.
           Requires 2-stage audit before promotion.
  Default for new K9 = Class D.

FIVE K9 CANDIDATES FOR EVALUATION:
  K9_A: V-filter (Born rule with registration filter)
  K9_C: Registration latency weighting
  K9_D: Certification discount
  K9_E: ⊥_K suppression
  K9_F: Colimit probability (T4-dependent)

EWF EXPERIMENTAL CONTEXT:
  D1: Proietti et al. 2019, arXiv:1902.05080
      S_exp = 2.416 ± 0.075; CHSH observable; 4 expectation values
  D2: Bong et al. 2020, arXiv:1907.05607
      Local Friendliness inequalities; violation at high μ
      Genuine LF Facet 1 max violation = 1.345 (LF bound = 0)
  D3: Frauchiger & Renner 2018, arXiv:1604.07422
      Theoretical no-go; agents F/F̄/W/W̄; logical contradiction
```

---

## K9-S1: Constraint Verification — What Any K9 Must Satisfy

**Goal:** Before evaluating any specific candidate, establish and verify
the complete set of constraints that any valid K9 must satisfy.
This step prevents premature commitment to a candidate that fails
a basic requirement.

```
TASK: K9 Constraint Verification and Completeness Audit

[PASTE MASTER CONTEXT BLOCK HERE]

Your task is to verify and complete the constraint set for K9.
Do not propose any K9 equation yet. Only analyze what is required.

PART 1: VERIFY MANDATORY CONSTRAINTS

For each constraint below, verify it is correctly stated and non-redundant.
If a constraint is incorrectly stated or follows from another, flag it.

C-BORN: When cert=1 ∧ V=1 ∧ ⊥_K silent → P(o|k) = Tr(E_o ρ)
  Verify: Is this a necessary condition? What breaks if violated?
  Derive: From which K axioms does this constraint follow (if any)?

C-NORM: Σ_o P(o|k) = 1 for all valid k
  Verify: Does this hold trivially if C-BORN holds and V=1 always?
  Derive: What additional structure is needed if V can be 0?

C-NONDIV: No division by zero for any k with V ∈ {0,1}
  Verify: Is this a constraint on K9 or a consequence of C-NORM?
  Derive: Under what conditions does division by zero threaten a K9 equation?

C-PARAM: ≤ 2 free parameters
  Verify: Is this derived from D1 data availability?
  State: What is the exact DOF calculation?
  If D1 provides only S_exp (1 number, not 4): revise to ≤ 1 free parameter.

C-TRACE: Every term traceable to K1-K8
  Verify: What does "traceable" mean exactly?
  State: Is an assumption flag sufficient, or must assumptions be justified?

C-FALSI: At least one falsifiable prediction
  Verify: What is the minimum falsifiability requirement?
  State: Does "falsifiable" require δP ≠ 0 vs Standard QM, or is
         a registration-layer observable (tau_reg, N_null) sufficient?

PART 2: IDENTIFY MISSING CONSTRAINTS

Are there constraints not listed above that any valid K9 must satisfy?
Consider:

  C-?: Non-negativity: P(o|k) ≥ 0 for all o, k
  C-?: Monotonicity: If V increases, does P change monotonically?
  C-?: Context independence: Does P(o|k) depend on other k' not in the tuple?
  C-?: Time invariance: Does P depend on t in ways not derivable from K2?
  C-?: Observer invariance: Is P the same for all observers? (EWF relevance)

For each candidate missing constraint:
  — State it precisely
  — Argue for or against its inclusion
  — Note which K9 candidates would be eliminated if it were included

PART 3: CONSTRAINT INTERACTION MAP

Build a dependency map: which constraints imply or conflict with others?
Format:
  C-BORN → implies → C-NORM (in the limit V=1)
  C-NONDIV → required by → C-NORM (normalization requires defined denominator)
  [continue for all pairs]

Identify any constraints that are in tension:
  If C-X and C-Y cannot both be satisfied simultaneously, flag as CONFLICT.

PART 4: ELIMINATION PRE-SCREEN

Without evaluating specific K9 candidates yet, state:
Which constraints are most likely to eliminate candidates?
Which constraint is hardest to satisfy?
Which candidate (K9_A/C/D/E/F) is most likely to fail which constraint?

PRODUCE:
  (A) Verified constraint list with derivation traces
  (B) Any additional constraints to add
  (C) Constraint interaction map
  (D) Pre-screen elimination predictions
```

**Save output as:** `k9_analysis/K9S1_constraints.md`

---

## K9-S2: Individual Candidate Analysis

**Goal:** Evaluate each K9 candidate against the verified constraint set.
One prompt per candidate. Run all five. Do not skip any.

**Run this prompt five times, once per candidate.**

```
TASK: K9 Candidate Analysis — [CANDIDATE NAME]

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE K9-S1 OUTPUT (verified constraint list) HERE]

CANDIDATE UNDER ANALYSIS: [K9_A / K9_C / K9_D / K9_E / K9_F]

CANDIDATE DEFINITIONS (use exactly as written):

K9_A — V-Filter:
  Case V(k)=1: P(o|k) = Tr(E_o ρ)
  Case V(k)=0: No P assignment (event contributes to N_null, not to P)
  Free parameter: v_rate ∈ [0,1] = fraction of runs with V=1
  (v_rate is a population parameter, not a per-event parameter)

K9_C — Registration Latency Weighting:
  P(o|k,H) = Tr(E_o ρ) · g(tau_reg(o)) / Z_C
  g(tau_reg) = exp(-tau_reg / tau_0)
  tau_0 ∈ (0,∞) = characteristic registration time [free parameter]
  Z_C = Σ_o Tr(E_o ρ) · g(tau_reg(o))  [normalization]
  tau_reg(o) = registration latency for outcome o under H

K9_D — Certification Discount:
  P(o|k) = [cert(k) · 1 + (1-cert(k)) · α] · Tr(E_o ρ) / Z_D
  α ∈ [0,1] = discount factor for non-self-certified registrations [free parameter]
  Z_D = Σ_o [cert(k) + (1-cert(k)) · α] · Tr(E_o ρ)
       = [cert(k) + (1-cert(k)) · α]  [since Σ_o Tr(E_o ρ) = 1]
  Simplified: P(o|k) = Tr(E_o ρ)  [cert cancels in normalization]
  NOTE: Check whether Z_D cancellation eliminates distinguishability.

K9_E — ⊥_K Suppression:
  P(o|k,K_context) = Tr(E_o ρ) · [1 - β · f_perp(o,K_context)] / Z_E
  f_perp(o,K_context) = |{k' ∈ K_context : k' ⊥_K k and o(k')≠o}| / |K_context|
  β ∈ [0,1] = suppression strength [free parameter]
  Z_E = Σ_o Tr(E_o ρ) · [1 - β · f_perp(o,K_context)]  [normalization]

K9_F — Colimit Probability:
  P(o_F, o_W | K_joint) defined via T4 colimit:
    K_joint = colim(K_F, K_W) in K-space category
    P(o_F, o_W | K_joint) = Tr(E_{o_F} ⊗ E_{o_W} · ρ_joint)
    where ρ_joint is the density matrix of the joint system
  Free parameters: 0 (if T4 fully determines K_joint)
  PREREQUISITE: T4 Colimit Existence Hypothesis must be proven first.

---

ANALYSIS PROTOCOL (apply to the selected candidate):

STEP 1: CONSTRAINT CHECK
For each constraint from K9-S1 (C-BORN, C-NORM, C-NONDIV, C-PARAM,
C-TRACE, C-FALSI, and any additional constraints identified):
  — Does this candidate satisfy the constraint? YES / NO / CONDITIONAL
  — If CONDITIONAL: state the exact condition
  — If NO: is the violation fatal (cannot be fixed) or fixable?

Format as table:
| Constraint | Status | Condition or Fix |
|---|---|---|

STEP 2: BORN RULE DERIVATION
Show algebraically that the candidate reduces to Tr(E_o ρ) when
cert=1 ∧ V=1 ∧ ⊥_K silent.
If the reduction is not exact, state the deviation.

STEP 3: DIVISION BY ZERO AUDIT
Identify every denominator in the candidate equation.
For each denominator: when can it be zero?
If zero is possible: propose the convention or fix.

STEP 4: DERIVATION TRACE
For each term or symbol in the candidate equation:
  — Which K axiom does it derive from?
  — If not derivable from K1-K8: flag as ASSUMPTION [A-N]
  — For each assumption: is it physically motivated or arbitrary?

Format as table:
| Term | Source | Axiom or ASSUMPTION |
|---|---|---|

STEP 5: DISTINGUISHABILITY ANALYSIS
Under what conditions does this candidate predict P(o|k) ≠ Tr(E_o ρ)?
  — Identify the exact scenario where deviation occurs
  — Compute the deviation δP = P_K9(o) - P_QM(o) symbolically
  — Is δP zero in all realistic EWF scenarios? If yes: state explicitly.
  — If δP ≠ 0: compute the order of magnitude for a typical EWF setup

STEP 6: EWF RELEVANCE CHECK
In the Extended Wigner's Friend scenario (Friend F, Wigner W):
  — What values do cert, V, ⊥_K take for F's registration? For W's registration?
  — Does the candidate produce different predictions for F vs W's perspective?
  — Does the candidate have a natural role in joint probability P(o_F, o_W)?

STEP 7: SPECIAL PROBLEM CHECK (candidate-specific)

For K9_A: If v_rate=1 in all experimental runs (all registrations succeed),
  does K9_A reduce to Standard QM exactly? State Yes/No.

For K9_C: tau_reg(o) must be defined before the outcome o is known
  (otherwise circular). Is tau_reg an outcome-independent quantity?
  If outcome-dependent: flag as CIRCULAR DEFINITION.

For K9_D: Verify whether Z_D cancellation eliminates α from P(o|k).
  Work through the algebra explicitly. If α cancels: K9_D has zero
  distinguishability. State this directly.

For K9_E: f_perp(o, K_context) requires counting ⊥_K events in context.
  Is K_context defined within K1-K8? Which axiom defines it?
  If not defined: flag as UNDEFINED REFERENCE.

For K9_F: T4 Colimit Existence Hypothesis is currently unproven.
  List every mathematical condition that must hold for K_joint to exist.
  State: "K9_F is blocked until T4 is proven. Estimated prerequisites:
  [list specific mathematical results needed]."

STEP 8: VERDICT

State one of:
  PASS: Candidate satisfies all constraints. Proceed to K9-S3 comparison.
  CONDITIONAL PASS: Satisfies all constraints with modifications [list].
  FAIL-FIXABLE: Fails constraint(s) [list] but fixes are possible [describe].
  FAIL-FATAL: Fails constraint(s) [list] that cannot be fixed within K1-K8.
              Elimination reason: [state precisely].

For PASS and CONDITIONAL PASS: assign preliminary class (C or D).
For CONDITIONAL PASS: state the exact modifications required.
```

**Run five times. Save outputs as:**
`k9_analysis/K9S2_candidate_A.md`
`k9_analysis/K9S2_candidate_C.md`
`k9_analysis/K9S2_candidate_D.md`
`k9_analysis/K9S2_candidate_E.md`
`k9_analysis/K9S2_candidate_F.md`

---

## K9-S3: Comparative Ranking

**Goal:** Compare all surviving candidates across five dimensions and
produce a ranked selection with justification.

**Input required:** All five K9-S2 outputs.

```
TASK: K9 Candidate Comparative Ranking

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE ALL FIVE K9-S2 OUTPUTS HERE]

STEP 1: SURVIVOR LIST

From the five K9-S2 analyses, list:
  PASSED candidates (PASS or CONDITIONAL PASS):
  FAILED candidates with reason:

If fewer than 2 candidates pass: state "Insufficient survivors for comparison.
K9 cannot be selected from current candidates. See K9-S6 for new candidate
generation." Do not proceed with ranking.

STEP 2: COMPARATIVE MATRIX

For each surviving candidate, score on five dimensions (1=worst, 5=best):

DIM-1: K1-K8 Derivability
  5 = all terms derived from K1-K8, zero assumptions
  3 = 1-2 assumptions, physically motivated
  1 = 3+ assumptions, or assumptions not physically motivated

DIM-2: Distinguishability
  5 = δP ≠ 0 in realistic EWF scenarios, computable, nonzero magnitude
  3 = δP ≠ 0 only under special conditions
  1 = δP = 0 in all realistic scenarios (K9 = Born rule relabeling)

DIM-3: Parameter efficiency
  5 = 0 free parameters (fully derived)
  4 = 1 free parameter
  3 = 2 free parameters (at budget limit)
  1 = > 2 free parameters (over budget)

DIM-4: EWF experimental relevance
  5 = directly connects to cert/V asymmetry in EWF setup
  3 = indirectly relevant, requires additional mapping
  1 = no natural connection to EWF scenario

DIM-5: Falsifiability
  5 = concrete falsification rule exists, testable with current experiments
  3 = testable in principle, requires new experimental setup
  1 = no falsification path identified

Format as table:
| Candidate | DIM-1 | DIM-2 | DIM-3 | DIM-4 | DIM-5 | Total |
|---|---|---|---|---|---|---|

STEP 3: DISTINGUISHABILITY DEEP-DIVE

For each candidate with DIM-2 score ≥ 3:
  Compute δP explicitly for the Proietti 2019 EWF setup:
    — State the cert and V values for Friend F and Wigner W
    — Compute P_K9(o_F, o_W) symbolically
    — Compute P_QM(o_F, o_W) = Tr(E_{o_F} ⊗ E_{o_W} ρ)
    — Compute δP = P_K9 - P_QM
    — Is δP zero or nonzero for this specific setup?

If DIM-2 = 1 for all surviving candidates:
  State: "No surviving K9 candidate produces observable deviation from
  Standard QM in the EWF setup. VVV-QMRF registration layer is currently
  empirically equivalent to Standard QM. See K9-S6."

STEP 4: PRIMARY SELECTION

Select the candidate with the highest total score as primary K9.
If tie: prefer higher DIM-2 (distinguishability) then DIM-1 (derivability).

State:
  PRIMARY: [candidate name]
  Justification: [2-3 sentences]
  Modifications required (if CONDITIONAL PASS): [list]
  Preliminary class: [C or D]

If no candidate scores ≥ 12/25 total: do not select. State:
  "No candidate meets minimum quality threshold. Proceed to K9-S6
  for new candidate generation."

STEP 5: BACKUP SELECTION

Select the second-highest candidate as backup K9 (for Phase 10 comparison).
State:
  BACKUP: [candidate name]
  Justification: [1 sentence]
  Under what conditions would backup be promoted to primary?
```

**Save output as:** `k9_analysis/K9S3_ranking.md`

---

## K9-S4: Primary Candidate Formalization

**Goal:** Produce the complete, finalized definition of the selected
primary K9 candidate, ready for Phase 7 (Constraint Identification)
and Phase 10 (Python fitting).

**Input required:** K9-S3 primary selection + K9-S2 analysis of primary candidate.

```
TASK: K9 Primary Candidate Formalization

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE K9-S3 PRIMARY SELECTION HERE]
[PASTE K9-S2 ANALYSIS OF PRIMARY CANDIDATE HERE]

Produce the complete, finalized definition of the primary K9 candidate.
This document will be directly used in Phase 7, Phase 9, and Phase 10.
Every section must be complete. No placeholders.

SECTION 1: AXIOM STATEMENT

Write the K9 axiom in the standard VVV-QMRF format:

  K9 [Name]: [One-sentence description]

  Formal definition:
    [Complete mathematical definition with all cases explicit]

  Domain:
    [Specify the domain of each variable]

  Free parameters:
    [List each free parameter: name, symbol, range, physical interpretation]

  Boundary statement:
    [State explicitly what K9 does NOT do:
     "K9 does not modify the Born rule."
     "K9 does not replace Standard QM."
     etc.]

SECTION 2: DERIVATION TRACE

For every symbol and term in K9:
| Symbol | Definition | Source: K-axiom or ASSUMPTION |
|---|---|---|

For each ASSUMPTION:
  — Label it A-1, A-2, etc.
  — State the assumption precisely
  — Provide physical motivation
  — State what would change if the assumption were false

SECTION 3: CONSTRAINT SATISFACTION PROOF

Prove each mandatory constraint is satisfied:

C-BORN proof:
  [Show algebraically that when cert=1 ∧ V=1 ∧ ⊥_K silent,
   K9 reduces exactly to Tr(E_o ρ). Every step explicit.]

C-NORM proof:
  [Show Σ_o P(o|k) = 1 for all valid k. Handle V=0 case explicitly.]

C-NONDIV proof:
  [Enumerate all denominators. Show none can be zero.]

C-PARAM statement:
  [Count free parameters. State DOF = 4 - [param count] for D1 fit.]

C-FALSI statement (v1.0, pre-registered 2026-05-29, 3-round RCA 4.5/5):

  === K9_E FALSIFICATION RULE (Level 0: Overlap-Only Class) ===

  C-FALSI-L0-EXCLUSION (Parameter exclusion -> Class falsification):
    K9_E overlap-only class (Eq. 2-3, manuscript paper_002) is FALSIFIED
    if BOTH Condition A and Condition B hold in a dedicated EWF experiment
    with tilted Superobserver measurement (K9-S12 or equivalent):

  CONDITION A -- Null at near-optimal angle (theta = 31 deg):
    |delta_AB_combined(theta=31deg)| < 3 * sigma_stat(theta=31deg, N)
    where sigma_stat = sqrt(SUM_i (d_delta/d_AB_i)^2 * sigma^2(AB_i))
    and sigma(AB_i) = sqrt((1 - AB_i^2) / N)
    (Poisson error, propagation through delta_AB formula)

  CONDITION B -- No theta-dependence (functional form null):
    chi^2(delta_AB=0 model) / DOF < chi^2_critical(DOF, alpha=0.05)
    where the model "delta_AB=0" is fit to measured delta_AB(theta_i)
    across theta_i in {20deg, 31deg, 35deg, 45deg, 58deg} (>=5 angles),
    DOF = number_of_angles (model has zero free parameters: delta=0 for all theta)

  IF BOTH HOLD:
    -> K9_E overlap-only class (Level 0) is FALSIFIED.
    -> beta >= beta_min excluded at 95% CL (beta_min = achieved sensitivity).
    -> Higher-order g(x) classes (Levels 1-3) survive.
    -> f_perp framework (K9_E core) is NOT falsified by Level 0 rejection.

  IF CONDITION A holds but CONDITION B fails:
    -> Inconsistent pattern. Check systematics (esp. phi-scramble).
    -> If systematics ruled out: overlap functional form wrong;
       higher-order g(x) required. Level 0 falsified; framework survives.

  IF CONDITION A fails (|delta_AB| >= 3sigma at 31deg):
    -> Evidence for beta > 0. Proceed to fit beta and verify theta-dependence.
    -> If beta > 0 AND delta_AB(pi/2) = 0: K9_E overlap-only class SURVIVES.

  IF delta_AB(pi/2) != 0 (equatorial cancellation violated):
    -> Proposition 1 (equatorial cancellation theorem) is violated.
    -> Overlap-only class is FALSIFIED regardless of beta.
    -> This would indicate a fundamental error in the theoretical framework.

  === GATE CONDITIONS (must be satisfied before unblinding) ===

  C-FALSI-GATE-LF:
    Gen LF 1 violation MUST be confirmed at >= 5sigma.
    If Gen LF 1 < 5sigma: no EWF setup -> experiment INCONCLUSIVE.

  C-FALSI-GATE-SENSITIVITY:
    Achieved beta_min MUST be <= 0.10 (Phase 1) or <= 0.05 (Phase 2).
    If beta_min > 2x target: experiment INCONCLUSIVE regardless of delta_AB.
    (Prevents "low-sensitivity null" masquerading as falsification.)

  C-FALSI-GATE-SYSTEMATICS:
    ALL six systematic error sources (S7 error budget) MUST be
    individually < 1.0 * Poisson sigma at the measured N.
    phi-scramble control MUST show: B ~ 0, C ~ 0 (no birefringence).

  C-FALSI-GATE-BLINDING:
    Analysis pipeline (theta unmasking, delta_AB computation, chi^2 test)
    MUST be frozen and committed to Git before theta-sequence is unmasked.
    Pre-registration timestamp: git commit hash of analysis scripts.

  === CONFOUNDERS CONTROLLED ===

  1. QWP retardance tolerance (< 1x Poisson)
  2. Birefringence (phi-scramble: B,C ~ 0 at >= 5sigma)
  3. Polarization-dependent loss (power monitoring per channel)
  4. Calibration offset (theta-verification protocol S4.4)
  5. Detector asymmetry (channel efficiency balancing)
  6. Accidentals (timing windows + dark-count subtraction)
  7. Fair-sampling assumption (Phase 1: stated; Phase 2: closed via eta >= 0.91)
  8. Analysis confirmation bias (blinding protocol)

  === IMPORTANT DISTINCTIONS ===

  "Falsified" != "beta = 0 proven":
    C-FALSI excludes beta >= beta_min; it does NOT prove beta = 0.
    beta < beta_min is always possible (and unfalsifiable below sensitivity).

  "Inconclusive" != "Confirmed" != "Falsified":
    Inconclusive: achieved beta_min > target (experiment not sensitive enough)
    Confirmed: |delta_AB| >= 3sigma at theta != pi/2 AND delta_AB(pi/2) = 0
    Falsified: BOTH Condition A AND Condition B hold

  Level 0 falsification != K9_E falsification:
    Level 0 is the SIMPLEST representative of the overlap-dependent class.
    Higher-order g(x) and alternative f_perp forms survive Level 0 rejection.
    Full K9_E falsification requires multiple independent null protocols.

  === PRE-REGISTRATION ===

  This rule was pre-registered on 2026-05-29, BEFORE any K9-S12
  experimental data exists. It was derived via 3-round RCA (4.5/5)
  referencing: K1-K8 axiomatization, K9_E v31 (Class C qualified),
  K9-S12 manuscript v94, P10a-C4 pre-registered fitting criterion
  (Delta_chi^2 > 3.84), and VVV-QMRF-EX compass.

  C-FALSI-L1/L2/L3 (higher-order classes): TBD -- requires dedicated
  predictions for each level. See [Falsification Hierarchy](../04_governance/Falsification_Hierarchy.md)
  for the complete 4-level deformation hierarchy (Level 0-3 + full K9_E),
  including preliminary C-FALSI-L1/L2/L3 rules and falsification-vs-confirmation
  asymmetry analysis. Pre-registered 2026-05-29.

SECTION 4: DISTINGUISHABILITY STATEMENT

Case 1: Standard scenario (cert=1, V=1, ⊥_K silent)
  δP = [compute]
  Verdict: [δP = 0 → identical to QM / δP ≠ 0 → deviation]

Case 2: EWF scenario (mixed cert and V, ⊥_K may fire)
  δP = [compute symbolically]
  Verdict: [δP = 0 → identical to QM / δP ≠ 0 → deviation]
  Magnitude estimate: [order of magnitude of δP for realistic parameters]

If δP = 0 in all cases:
  State: "K9 [Name] does not produce observable probability deviations
  from Standard QM under any scenario analyzable from K1-K8.
  K9 provides registration-layer structure without empirical
  deviation. Class D assignment confirmed."

SECTION 5: CLASS ASSIGNMENT

Assign: Class C or Class D

For Class C:
  — Identify the specific testable prediction
  — State the experiment required
  — State the numerical prediction with uncertainty
  — State the falsification condition

For Class D:
  — Identify what would be needed for Class C promotion
  — List: mathematical proof needed / experimental access needed /
          additional axiom needed

SECTION 6: PYTHON SPECIFICATION

For Phase 10 Python implementation:

Function signature:
  def k9_[name]_probability(theta_A, theta_B, [free params], [k_state_params]):
    """
    [Docstring with complete description]
    Parameters: [list each with type and range]
    Returns: float in [0,1]
    Raises: [any exceptions, e.g., ValueError for invalid params]
    """

Sanity checks (must all pass):
  CHECK-1: [name](cert=1, V=1, perp_k=False, [defaults]) == qm_born_rule()
           [Born rule recovery]
  CHECK-2: [specific edge case] → [expected result]
  CHECK-3: [V=0 case] → [expected behavior, not 0/0]

SECTION 7: EWF JOINT PROBABILITY EXTENSION

How does K9 extend to joint probability P(o_F, o_W) in the 2-observer EWF?

  P(o_F, o_W | K_F, K_W) = [formula]

  When cert_F ≠ cert_W (asymmetric certification in EWF):
    [What happens to P(o_F, o_W)?]
    [Does this produce deviation from Born rule for joint probability?]

  Connection to Bong et al. LF inequalities:
    [Can K9 produce different LF inequality violation magnitudes than QM?]
    [If yes: which inequality? What is the predicted violation value?]
```

**Save output as:** `k9_analysis/K9S4_primary_formalized.md`

---

## K9-S5: Adversarial Falsification Attempt

**Goal:** Attempt to break the formalized primary K9 before it enters
Phase 7. Find every weakness, circular definition, and failure mode.
This is the most adversarial prompt in the sequence.

**Input required:** K9-S4 complete formalization.

```
TASK: Adversarial Falsification of Primary K9

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE K9-S4 COMPLETE FORMALIZATION HERE]

You are acting as the most skeptical reviewer at Foundations of Physics.
Your job is to find every flaw in K9 [Name]. Do not be constructive.
Find problems. If you cannot find problems, state why and what you tried.

ATTACK 1: ALGEBRAIC COUNTEREXAMPLE

Construct a specific quantum state ρ and measurement {E_o} such that
K9 produces a result that is:
  (a) outside [0,1], or
  (b) not normalized (Σ_o P ≠ 1), or
  (c) negative for some outcome

Try at least three different (ρ, {E_o}) pairs.
For each: compute K9's prediction step by step.
If no counterexample found after three attempts: state this.

ATTACK 2: CIRCULAR DEFINITION HUNT

For each term in K9 that depends on the outcome o:
  Does computing P(o|k) require knowing o before it is observed?
  If yes: this is a circular definition. Flag it.

Specifically check:
  — Does tau_reg(o) require knowing o? (K9_C vulnerability)
  — Does f_perp(o, K_context) require knowing o? (K9_E vulnerability)
  — Does cert depend on the outcome, not just the registration act? (K9_D)

ATTACK 3: ASSUMPTION AUDIT

List all assumptions flagged A-1, A-2, etc. in K9-S4.
For each assumption:
  — Is it derivable from K1-K8? (If yes: it is not an assumption, derive it)
  — If not derivable: is there a physically motivated alternative assumption
    that produces a different K9? If yes: K9 is underdetermined.
  — If underdetermined: how many distinct K9 variants exist under
    different assumption choices?

If K9 has ≥ 3 underdetermined assumptions: flag as UNDERDETERMINED.
An underdetermined K9 cannot be uniquely selected.

ATTACK 4: CANCELLATION CHECK

Work through K9's normalization Z explicitly.
Does the free parameter cancel out in the normalized P(o|k)?

Example of problematic cancellation (do not assume this applies):
  If P(o|k) = α · Tr(E_o ρ) / Z  and  Z = α · Σ_o Tr(E_o ρ) = α
  then P(o|k) = Tr(E_o ρ)  [α cancels, K9 = Born rule, zero distinguishability]

Apply this check to K9 [Name]:
  Compute Z explicitly.
  Substitute Z into P(o|k).
  Simplify completely.
  Does the free parameter survive simplification?
  If parameter cancels: K9 has zero distinguishability. State: FATAL.

ATTACK 5: EWF SCENARIO STRESS TEST

In the Proietti 2019 EWF setup:
  Friend F: self-certifies outcome (cert=1), V=1, ⊥_K silent
  Wigner W: measures entire lab, cert=0 from F's perspective, V=?

Apply K9 to compute P(o_F) and P(o_W) separately.
Then compute joint P(o_F, o_W).
Compare with Standard QM prediction Tr(E_{o_F} ⊗ E_{o_W} ρ).

Is the deviation δP(o_F, o_W) = K9 - QM:
  (a) Zero for all outcome combinations → K9 has no content in this setup
  (b) Nonzero for some combination → which one? What is the value?
  (c) Undefined for some combination → flag as UNDEFINED

ATTACK 6: PARAMETER RANGE VIOLATION

For each free parameter, check boundary behavior:
  When parameter → 0: what does K9 predict? Is it physically sensible?
  When parameter → 1: what does K9 predict? Is it Born rule?
  When parameter → ∞ (if unbounded): what happens to P(o|k)?

If any boundary produces P < 0 or P > 1 or undefined: flag as BOUNDARY FAILURE.

ATTACK 7: COMPARISON WITH KNOWN FRAMEWORKS

Does K9 [Name] reproduce the predictions of any known QM interpretation
in its parameter space?

Check:
  — Copenhagen: single outcome, collapse, cert=V=1 always → K9 = QM?
  — Relational QM: facts relative to observer, different cert per observer
    → does K9 produce observer-relative probabilities?
  — QBism: agent-specific priors → does cert encode agent-specific belief?

If K9 is isomorphic to an existing interpretation:
  State: "K9 [Name] is mathematically equivalent to [interpretation]
  in the parameter range [range]. It is not a new framework in this range."

PRODUCE:

(A) ATTACK RESULTS TABLE
| Attack | Finding | Severity: FATAL / FIXABLE / NONE |
|---|---|---|

(B) SURVIVING FLAWS
List all non-NONE findings that require attention before Phase 7.
For each: proposed fix, or "no fix available within K1-K8."

(C) ADVERSARIAL VERDICT
  SURVIVES: K9 passes all attacks. Ready for Phase 7.
  SURVIVES WITH FIXES: K9 passes with modifications [list].
  ELIMINATED: K9 fails attack(s) [list]. Cannot proceed to Phase 7.
              Escalate to K9-S6 (new candidate generation).
```

**Save output as:** `k9_analysis/K9S5_adversarial.md`

---

## K9-S6: New Candidate Generation (Conditional — Run Only If Needed)

**Trigger conditions:** Run K9-S6 only if:
  — Fewer than 2 candidates passed K9-S2
  — No candidate scored ≥ 12/25 in K9-S3
  — Primary candidate was ELIMINATED in K9-S5

**Goal:** Generate new K9 candidates from first principles,
constrained by K1-K8 and the verified constraint set.

```
TASK: K9 New Candidate Generation from First Principles

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE K9-S1 CONSTRAINT LIST HERE]
[PASTE K9-S2 THROUGH K9-S5 FAILURE SUMMARY HERE]

TRIGGER: Previous K9 candidates failed because: [state reason from S2-S5]

Your task is to generate new K9 candidates from K1-K8 structure,
not from analogy or physical intuition.

METHOD: Structural derivation from K1-K8

K1-K8 produce four binary objects:
  cert ∈ {0,1}  [K3]
  V    ∈ {0,1}  [K4, K5]
  ⊥_K  ∈ {0,1}  [K5, K6]
  [t]  ∈ ℕ      [K2, discrete timestamp]

Standard QM produces:
  P(o) = Tr(E_o ρ) ∈ [0,1]   [Born rule]

DERIVATION CHALLENGE:
What is the most general function f: {0,1}³ × ℕ → [0,1] that:
  (a) Satisfies all constraints from K9-S1
  (b) Has ≤ 2 free parameters
  (c) Is not equivalent to any failed candidate

STEP 1: ENUMERATE POSSIBLE FUNCTIONAL FORMS

List all distinct ways to combine (cert, V, ⊥_K, t) into a
modulation function f such that:
  P(o|k) = Tr(E_o ρ) · f(cert, V, ⊥_K, t) / Z

Do not pre-filter. List at minimum 5 functional forms.
For each: write f explicitly, count parameters.

STEP 2: APPLY CONSTRAINT FILTER

For each functional form from Step 1:
  — Check C-BORN: does f → 1 when cert=1, V=1, ⊥_K=0?
  — Check C-NONDIV: can f = 0 while Z = 0?
  — Check C-PARAM: count free parameters
  Eliminate any that fail. Mark survivors.

STEP 3: DISTINGUISHABILITY SCREEN

For each surviving functional form:
  — Does f ≠ 1 in any realistic EWF scenario?
  — If f = 1 always → eliminate (Born rule relabeling)
  — If f ≠ 1 in some scenario → keep, note the scenario

STEP 4: SELECT TOP 2 NEW CANDIDATES

From survivors, select 2 with highest distinguishability and lowest
parameter count. Name them K9_G and K9_H (or appropriate labels).

For each new candidate: write complete definition matching K9-S2 format.

STEP 5: RAPID ADVERSARIAL CHECK

Apply Attack 4 (cancellation check) from K9-S5 to each new candidate.
If both fail cancellation check: state "K1-K8 structure does not support
a non-trivial continuous probability bridge. K9 cannot be constructed
within current K1-K8 framework. Recommend axiom extension."

PRODUCE:
  (A) At least 2 new K9 candidates with complete definitions
  (B) Constraint satisfaction status for each
  (C) Distinguishability verdict for each
  (D) If no valid candidate found: explicit statement of the structural
      impossibility and what additional axiom would be needed
```

**Save output as:** `k9_analysis/K9S6_new_candidates.md`

**If K9-S6 produces no valid candidates:** Document the finding formally.
This is a scientific result: K1-K8 cannot bridge to continuous probability
without additional axioms. VVV-QMRF requires a structural extension.

---

## K9-S7: Final Selection and Lock

**Goal:** Produce the official locked K9 selection document.
This document is the handoff from K9 Analysis Plan to Main Plan.

**Input required:** K9-S4 (formalization) + K9-S5 (adversarial result).
If K9-S6 was run: also paste K9-S6 output.

```
TASK: K9 Final Selection and Lock Document

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE K9-S4 FORMALIZATION HERE]
[PASTE K9-S5 ADVERSARIAL VERDICT HERE]
[PASTE K9-S6 OUTPUT IF RUN HERE]

Produce the official K9 lock document for handoff to Main Plan.

SECTION 1: SELECTION RECORD

Primary K9: [name and one-line description]
Status: LOCKED / LOCKED WITH CONDITIONS / NOT LOCKED

If LOCKED: confirm all of:
  ☐ Satisfies C-BORN (Born rule recovery proven)
  ☐ Satisfies C-NORM (normalization verified)
  ☐ Satisfies C-NONDIV (no division by zero)
  ☐ Satisfies C-PARAM (≤ 2 free parameters)
  ☐ Satisfies C-TRACE (all terms traced to K1-K8 or flagged)
  ☐ Satisfies C-FALSI (falsification rule stated)
  ☐ Survived K9-S5 adversarial attacks
  ☐ Class assignment confirmed

If LOCKED WITH CONDITIONS: list unresolved conditions.
If NOT LOCKED: state reason and recommended path forward.

SECTION 2: DISTINGUISHABILITY FINAL VERDICT

State one of:

VERDICT A: "K9 [name] produces δP ≠ 0 in EWF scenario [describe].
  The deviation is [symbolic expression]. For parameter value [α/β/etc] = X,
  δP ≈ [magnitude]. This is detectable with [N] experimental runs."

VERDICT B: "K9 [name] produces δP = 0 in all EWF scenarios analyzable
  from K1-K8. The registration layer adds structure without observable
  probability deviation. VVV-QMRF is currently empirically equivalent
  to Standard QM at the probability level. Observable consequences
  exist only at the registration-layer level: tau_reg, N_null, I(K;H)."

VERDICT C: "K9 cannot be determined from current K1-K8 axioms.
  Additional axiom K10 is required. Recommended structure: [describe]."

SECTION 3: HANDOFF CHECKLIST FOR MAIN PLAN

Items passed to Phase 7 (Constraint Identification):
  ☐ K9 formal definition (K9-S4 Section 1)
  ☐ Constraint satisfaction proofs (K9-S4 Section 3)
  ☐ Distinguishability statement (K9-S4 Section 4)
  ☐ Class assignment (K9-S4 Section 5)

Items passed to Phase 9 (Adversarial):
  ☐ Surviving attack results from K9-S5
  ☐ Known weaknesses with proposed fixes

Items passed to Phase 10 (Python fitting):
  ☐ Python function specification (K9-S4 Section 6)
  ☐ Sanity check list (K9-S4 Section 6)
  ☐ EWF joint probability extension (K9-S4 Section 7)
  ☐ Free parameter list with ranges

SECTION 4: OPEN PROBLEMS

List any unresolved questions that remain after K9 is locked:
  — Mathematical: [e.g., "T4 colimit proof required for K9_F promotion"]
  — Experimental: [e.g., "tau_reg operationalization needs lab protocol"]
  — Theoretical: [e.g., "A-2 assumption needs justification from K1-K8"]

These do not block K9 lock. They are logged for future work.

SECTION 5: IF NO K9 CAN BE LOCKED

If VERDICT C applies or if K9-S6 found no valid candidate:

Write a formal finding document:

  FINDING VVV-K9-NULL:
  "VVV-QMRF axioms K1-K8 do not contain sufficient structure to derive
  a continuous probability function P(o|k) that is distinguishable from
  the Standard QM Born rule P(o) = Tr(E_o ρ).

  Structural reason: [state the specific gap — e.g., "binary cert and V
  cannot produce continuous modulation without an additional continuity axiom"]

  Required extension: [describe the minimal additional axiom needed]

  Consequence for VVV-QMRF: The framework currently functions as a
  registration-logic language. Its scientific value is:
    (a) Formal vocabulary for AOE-rejection in EWF contexts
    (b) Registration-layer observables: tau_reg, N_null, I(K;H)
    (c) Structural pre-condition for quantum measurement events

  This finding does not invalidate VVV-QMRF. It precisely locates
  where K1-K8 end and where new physics must begin."
```

**Save output as:** `k9_analysis/K9S7_final_lock.md`

---

## EXECUTION NOTES

**Session allocation:**
  K9-S1: 1 session (constraint analysis, no equations)
  K9-S2: 5 sessions (one per candidate — do not combine)
  K9-S3: 1 session (ranking, requires all S2 outputs)
  K9-S4: 1 session (formalization of primary only)
  K9-S5: 1 session (adversarial — use separate session to avoid bias)
  K9-S6: 1 session (only if triggered)
  K9-S7: 1 session (lock document)

**Critical rule for K9-S2:** Run each candidate in a completely
separate session. Do not analyze two candidates in the same session.
Cross-contamination between candidate analyses produces biased results.

**Critical rule for K9-S5:** Run in a separate session from K9-S4.
The same LLM that formalized K9 in S4 will be biased toward defending it.
A fresh session with adversarial framing is more likely to find real flaws.

**Cancellation check is mandatory:** K9_D failed this check in preliminary
analysis (α cancels in normalization). Apply Attack 4 to every candidate,
even those that appear promising. This is the most common failure mode
for registration-layer modulations of Born rule.

**Honest failure is a valid output:** If K9-S7 produces FINDING VVV-K9-NULL,
this is not a failure of VVV-QMRF as a framework. It is a precise scientific
finding that locates the boundary of K1-K8. Document it carefully.
A framework that knows its own limits is more credible than one that claims
everything.

**LLM recommendation:** Use Claude Opus or GPT-4 class models throughout.
For K9-S5 (adversarial), explicitly instruct the model: "Do not be
constructive. Find problems." This framing produces better adversarial
analysis than asking for "balanced evaluation."

---

## K9-S8: Composition Law — Joint Probability Extension (ADDED 2026-05-23)

**Goal:** Define P(o_F, o_W | K-space parameters) — the MISSING PIECE.

**Motivation:** K9-S1 through K9-S7 defined P(o | k_i) for single observer.
The joint probability P(o_F, o_W) was never defined. K9_Analysis_Plan §K9-S4
Section 7 (line 543) left a placeholder `P(o_F, o_W | K_F, K_W) = [formula]`
that was never filled. This step fills it.

**Status:** COMPLETE — see `K9S8_composition_law.md`

**KEY FINDING (Marginalization Cancellation Theorem):**
```
2-observer MARGINAL P(o_F, o_W) = QM exactly for all β.
K9_E is distinguishable from QM ONLY in:
  (a) Conditional correlators P(o_F, o_W | o_FA)
  (b) 3+ observer joint probabilities P(o_FA, o_F, o_W)
```

**Two formulations defined:**
- P9-JC (conditional): testable with Proietti Figure 3
- P9-3O (3-observer): testable with future experiments

**Output:** `k9_analysis/K9S8_composition_law.md`

---

## K9-S9: Conditional Correlator Computation (COMPLETE)

**Goal:** Compute numerical predictions from P9-JC for conditional
correlators ⟨A_xB_y | o_FA⟩.

**Status:** COMPLETE — see `K9S9_conditional_predictions.md`

**KEY FINDING:** 11% deviation from QM at beta=0.3 for conditional correlators
in BSM settings (x=1). x=0 (projective) gives delta=0 (correct Born limit).

**Output:** `k9_analysis/K9S9_conditional_predictions.md` + `fits/K9S9_conditional_predictions.py`

---

## K9-S10: Testability Analysis + Bong Protocol Check (COMPLETE)

**Goal:** Determine which experiments can actually test K9_E, given the
Marginalization Cancellation Theorem (K9-S8).

**Status:** COMPLETE — see `K9S10_testability_analysis.md`

**KEY FINDINGS:**
```
1. PROIETTI CANNOT TEST K9_E
   All marginal correlators = QM exactly (Marginalization Cancellation).
   S_exp, individual <A_xB_y> are all uninformative.

2. PHASE 10b IS INVALIDATED
   Phase10b_bong_lf.md applied f_perp to marginal probabilities BEFORE
   K9-S8 was proven. Its "reduced LF violation" was a computational error.
   
3. BONG PROTOCOL CAN TEST K9_E (partially)
   Settings (x=1, y!=1) and (x!=1, y=1) are testable because:
   - x=1 means a=c (Friend's outcome known, not marginalized)
   - y!=1 means Bob does BSM (d marginalized, but P(d|c) non-uniform)
   - Non-uniform P(d|c) breaks the marginalization symmetry
   
4. 4 OF 9 BONG CORRELATORS ARE TESTABLE:
   <A_1 B_2>, <A_1 B_3>, <A_2 B_1>, <A_3 B_1>
   
5. GENUINE LF FACET 1 contains testable terms:
   <A_1 B_2> (coefficient -2) and <A_2 B_1> (coefficient -2)
```

**Output:** `k9_analysis/K9S10_testability_analysis.md`

---

## K9-S11: Numerical Bong Predictions (COMPLETE -- 2026-05-23)

**Goal:** Compute K9_E predictions for the 4 testable Bong correlators.
Compare with Bong experimental data (Fig. 4, results.pdf).

**RESULT: K9-S10 WAS PARTIALLY WRONG.**

K9-S10's Partial Marginalization Non-Cancellation Theorem was correct in
principle but MISAPPLIED to the Bong geometry:

```
CRITICAL FINDING (K9-S11):
  For the standard Bong protocol:
    Friend measures: z-basis ({|H>, |V>}, Bloch z-pole)
    Superobserver measures: XY-plane (Bloch equator)
    
  |<b|d>|^2 = 1/2 for ALL (b,d) pairs.
  f_perp is outcome-INDEPENDENT => marginalization cancellation applies.
  
  RESULT: 0 of 9 standard Bong correlators are testable by K9_E.
  K9_E = QM for ALL Bong settings, ALL beta.
```

K9-S10 assumed f_perp would be outcome-dependent for Bong settings.
K9-S11 computed the actual overlaps and found f_perp = constant = 1/2.
This is because z-axis and XY-equator are maximally incompatible:
every z-eigenstate decomposes 50/50 into any equatorial basis.

**WHEN IS K9_E TESTABLE?**

K9_E IS testable in a MODIFIED Bong protocol where the superobserver
measures at a TILTED angle (0 < alpha < 90 deg from z-axis):

| alpha | beta_k9 | delta(%) | Testable? |
|---|---|---|---|
| 90 (standard) | any | 0.0% | NO |
| 60 | 0.3 | -12.7% | YES |
| 45 | 0.3 | -8.1% | YES |
| 45 | 0.5 | -14.3% | YES |

**Output:** `k9_analysis/K9S11_bong_predictions.md` + `fits/K9S11_bong_predictions.py`

### K9-S11b: Proietti Geometry Check (COMPLETE -- 2026-05-23)

Binary answer: f_perp = 1/2 (constant) for ALL Proietti settings.
CHSH-optimal angles are ALL equatorial. BSM groupings also constant.
**Decision: GO TO K9-S12** (no need to revisit Phase 10a).

**Output:** `fits/proietti_geometry_check.py`

### K9-S11c: Universal Theorem + LF Compatibility (COMPLETE -- 2026-05-23)

**Universal Equatorial Cancellation Theorem** — PROVEN algebraically:
```
f_perp(+1,H) - f_perp(-1,H) = -cos(theta)
Vanishes IFF theta = pi/2 (equatorial). QED.
Azimuthal phi is IRRELEVANT.
```

LF Compatibility: Gen LF 1 IS violated at alpha=45° (mu>=0.95).

> **ERRATUM (K9-S11d):** alpha=45° is NOT the sweet spot.
> Gen LF 1 = +0.022 at alpha=45° is only 1.9sigma (not significant).
> See K9-S11d for corrected optimal alpha.

**Output:** `k9_analysis/K9S11c_universal_theorem_lf_check.md` + `fits/universal_theorem_lf_check.py`

### K9-S11d: Statistical Significance (COMPLETE -- 2026-05-23)

**Self-correction of K9-S11c.** Proper statistical analysis with N=91,000:

```
OPTIMAL ALPHA = 31 deg (FOM = 6.0)
  Gen LF 1:     +0.062 at 6.0sigma  (SIGNIFICANT)
  delta<A1B2>:  -0.036 at 20.8sigma (SIGNIFICANT)
  BOTH detectable with Bong-level statistics.
  
K9_E measurable: delta<A1B2> = -0.036 (4.2% shift at beta_k9=0.3)
Bottleneck is ALWAYS the LF significance, not K9_E.
```

**Output:** `k9_analysis/K9S11d_statistical_significance.md` + `fits/statistical_significance.py`

---

## K9-S12: Modified Bong Protocol Proposal (COMPLETE -- 2026-05-23)

**Goal:** Design a complete experimental proposal for testing K9_E using a
modified Bong protocol with tilted superobserver measurement basis.

**RESULT: PROPOSAL COMPLETE. Single waveplate change from standard Bong.**

```
OPTIMAL PARAMETERS (re-optimized for alpha=31):
  Superobserver polar angle:  alpha = 31 deg
  Azimuthal angles:           phi_2=112, phi_3=217, beta=20 (RE-OPTIMIZED)
  State:                      rho_mu with mu >= 0.95
  Coincidences:               N = 91,000 (Bong-level, sufficient)

PREDICTED RESULTS (mu=0.95, beta_k9=0.3):
  Gen LF 1 = +0.089 (8.6sigma) -> Genuine LF VIOLATED
  delta<A1B2> = -0.036 (20.8sigma) -> K9_E DETECTABLE
  BOTH with Bong-level statistics.
  FOM = min(8.6, 20.8) = 8.6 (vs 6.0 with Bong angles)

PHYSICAL CHANGE:
  Re-insert QWP after BD2 for settings 2/3 (currently removed).
  Same source, same state, same statistics. No new hardware.
  
SENSITIVITY:
  beta_k9=0.1 -> 6.6sigma (detectable)
  beta_k9=0.3 -> 20.8sigma (strong)
  beta_k9=0.5 -> 34.9sigma (very strong)
```

**Output:** `k9_analysis/K9S12_modified_bong_proposal.md` + `fits/K9S12_proposal.py`

