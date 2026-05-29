# VVV-QMRF K-Space Formalization — LLM Prompt Sequence

**Purpose:** Derive a probability equation from K-space axioms, fit it against EWF experimental data, and generate a testable prediction that distinguishes VVV-QMRF from Standard QM.

**Instructions for use:** Execute prompts in order. Do not skip steps. Paste outputs from each prompt into the next where indicated. Each prompt must be sent as a fresh message with full context pasted in.

---

## CONTEXT BLOCK
*Paste this block at the top of every prompt session that needs it.*

```
FRAMEWORK: VVV-QMRF (VietVunVut Quantum Measurement Registration Framework)
CORE STRUCTURE: K-space — a registration-logic structure defined by axioms K1-K8
KEY OBJECT: K-state tuple k = <M, o, cert, t, V> where:
  M    = measurement-registration act identifier
  o    = registered outcome (o ∈ O ∪ {∅})
  cert = self-certification marker ∈ {0,1}
  t    = registration time
  V    = validity status ∈ {0,1}
AXIOMS:
  K1: K_R is a set of K-state tuples with cert-admission rule and t-injectivity
  K2: (K_R, <_R) is a strict total order; discrete (no registration state between events)
  K3: cert(k) = σ_R(M) determined intrinsically within K_R
  K4: V(k) = 1 by default for non-null k upon instantiation; V(k) = 0 for isNull(k)
  K5: V(k1) → 0 iff ∃k2 later in order such that k2 ⊥ k1 within shared C_K with valid authority
  K6: Cross-registration authority Auth(k2→k1, C_K) = 1 iff same C_K sphere, V(k2)=1, k1 in scope
  K7: Registration process closes at t_close when no pending requires_K_joint demands remain
  K8: Cross-space embedding preserves V and all tuple fields at embedding time
TARGET EXPERIMENT: Extended Wigner's Friend (EWF)
  Observer F (Friend): measures system S, registers definite outcome o_F
  Observer W (Wigner): measures entire lab including F, registers superposition
  Key paper: Proietti et al. 2019, arXiv:1902.05080
  Measured quantity: correlations P(o_F, o_W) across repeated experimental runs
```

---

## PROMPT 1 — Establish Physics Constraints

**Goal:** Before any equation is proposed, identify all constraints that any valid probability equation for K-space MUST satisfy.

```
TASK: Constraint Identification for K-space Probability Equation

You are analyzing the VVV-QMRF framework. Before proposing any equation,
identify all hard constraints that a probability equation
P(o_F, o_W | K-space parameters) must satisfy.

[PASTE CONTEXT BLOCK HERE]

Produce a numbered list of constraints. For each constraint specify:
1. The constraint statement in formal notation
2. Which axiom or physical requirement it derives from
3. What breaks if this constraint is violated

Organize constraints into three categories:

CATEGORY A — Internal consistency constraints
(derived from K1-K8 axioms alone, independent of experiment)

CATEGORY B — Physical validity constraints
(derived from Standard QM; the equation must reduce to Born rule in some limit)

CATEGORY C — Distinguishability constraints
(the equation must predict something different from Standard QM in at least
one scenario; if no constraint of this type can be identified,
state this explicitly and explain why)

Do not propose any equation yet. Only list constraints.
For Category C, if no distinguishability constraint can be derived from K1-K8,
state: "K-space as currently axiomatized does not generate predictions
distinguishable from Standard QM" and explain the structural reason.
```

---

## PROMPT 2 — Generate Candidate Equations

**Goal:** Propose candidate equations that satisfy the constraints identified in Prompt 1.

**Input required:** Full output from Prompt 1.

```
TASK: Candidate Equation Generation for K-space

[PASTE CONTEXT BLOCK HERE]

[PASTE FULL OUTPUT FROM PROMPT 1 HERE]

Using the constraints identified above, propose exactly 3 candidate equations
for P(o_F, o_W | K-space parameters).

For each candidate equation provide:

CANDIDATE [N]:
  Equation: [write the full equation in unambiguous mathematical notation]
  
  Term-by-term derivation:
    [For each term or symbol in the equation, state which axiom or
     physical principle it derives from. If any term cannot be derived
     from K1-K8 or Standard QM, flag it as an ASSUMPTION and state it explicitly.]
  
  Born rule limit:
    [State the exact condition under which this equation reduces to the
     Born rule P(o) = |<o|ψ>|². If it never reduces to Born rule, discard
     this candidate and state why.]
  
  Distinguishability condition:
    [State the exact condition under which this equation predicts something
     different from Standard QM. Compute the magnitude of the difference.
     If the equation is identical to Standard QM in all conditions,
     discard this candidate and state why.]
  
  Role of cert and V:
    [Explain explicitly how cert and V from the K-state tuple appear in
     this equation. If cert and V do not appear, state: "This equation
     does not use cert or V, therefore K-space adds no physical content
     beyond Standard QM in this formulation."]

Do not proceed with any candidate that: 
  (a) cannot reduce to Born rule in any limit, or
  (b) is identical to Standard QM in all scenarios, or
  (c) contains undefined terms not traceable to K1-K8 or Standard QM.

If all 3 candidates fail these tests, state this explicitly.
```

---

## PROMPT 3 — Adversarial Testing

**Goal:** Attempt to falsify each candidate equation before fitting any data.

**Input required:** Full output from Prompt 2.

```
TASK: Adversarial Testing of Candidate Equations

[PASTE CONTEXT BLOCK HERE]

[PASTE FULL OUTPUT FROM PROMPT 2 HERE]

For each candidate equation that survived Prompt 2 screening,
attempt to falsify it using the following four tests.
Apply all four tests to each candidate. Do not defend the equation —
find its weakest points.

TEST 1 — Physical counterexample
  Construct a concrete scenario (specific quantum state, specific measurements)
  where the equation produces a result that is:
    (a) outside [0,1], or
    (b) does not sum to 1 over all outcomes, or
    (c) violates no-signaling conditions
  If no such counterexample exists, state why and confirm the equation
  passes this test.

TEST 2 — Axiom consistency check
  Identify any term in the equation that contradicts or is undefined by K1-K8.
  Pay special attention to:
    — How ⊥_K is operationalized numerically (K5 does not give a number)
    — How V ∈ {0,1} produces a continuous probability (binary → continuous gap)
    — Whether the equation requires assumptions beyond K1-K8

TEST 3 — Distinguishability verification
  Take the scenario where the equation is supposed to differ from Standard QM.
  Compute the numerical prediction of Standard QM for the same scenario.
  Compute the numerical prediction of the candidate equation.
  State the difference explicitly as a number.
  If the difference is zero in all computable scenarios, the equation
  is not distinguishable from Standard QM — state this as a failure.

TEST 4 — cert and V sensitivity
  Set cert = 1 and V = 1 for all k (the trivial case where all registrations
  are valid and self-certified).
  Does the equation reduce to Standard QM exactly in this case?
  If yes: this is the correct Born rule limit — confirm and document the limit.
  If no: explain what goes wrong.

After all tests, rank surviving candidates:
  RANK 1: Most physically consistent and most distinguishable from Standard QM
  RANK 2: ...
  RANK 3: ...

If no candidate survives all four tests, state this explicitly and identify
which structural gap in K1-K8 prevents generating a valid probability equation.
```

---

## PROMPT 4 — Fit Against Proietti 2019 Data

**Goal:** Fit the surviving candidate equation against real experimental data.

**Input required:** Output from Prompt 3 (rank 1 candidate). Proietti et al. 2019 data.

**Before running this prompt:** Obtain Table 1 from arXiv:1902.05080 and paste the numerical correlation values below.

```
TASK: Fitting K-space Equation to Proietti et al. 2019 EWF Data

[PASTE CONTEXT BLOCK HERE]

[PASTE RANK 1 CANDIDATE EQUATION FROM PROMPT 3 HERE]

EXPERIMENTAL DATA (Proietti et al. 2019, arXiv:1902.05080):
[PASTE TABLE 1 DATA HERE — correlation values P(o_F, o_W) for each
measurement setting. Include error bars.]

Perform the following steps:

STEP 1 — Identify free parameters
  List every free parameter in the candidate equation.
  For each parameter state:
    — Its physical interpretation within K-space
    — Its expected range (if constrainable from K1-K8)
    — Whether it is independent of the other parameters

STEP 2 — Fitting procedure
  Find parameter values that minimize residual between equation predictions
  and Proietti data.
  Report:
    — Best-fit value for each parameter with uncertainty
    — Residual sum of squares
    — Chi-squared statistic if error bars are available
    — Degrees of freedom remaining after fitting

STEP 3 — Fit quality assessment
  Can the equation fit the data within experimental error bars?
    — If YES: report the fit and proceed to Step 4
    — If NO: state explicitly "The candidate equation is falsified by
      Proietti 2019 data" and identify which data points are inconsistent

STEP 4 — Comparison with Standard QM fit
  Fit Standard QM Born rule to the same data using the same procedure.
  Compare residuals.
  Report whether VVV-QMRF fits the data better, worse, or equally well
  compared to Standard QM.
  If equally well: note that both frameworks are currently
  indistinguishable by this dataset.

STEP 5 — Parameter interpretation
  For each best-fit parameter value, state its physical meaning.
  Do the best-fit values correspond to any known physical quantity?
  Are any values at boundary (0 or 1)? If so, explain the implication.
```

---

## PROMPT 5 — Generate 3-Observer Prediction

**Goal:** Use fitted parameters to predict results of a 3-observer EWF experiment not yet performed.

**Input required:** Full output from Prompt 4 (best-fit parameters and equation).

```
TASK: Generate Testable Prediction for 3-Observer EWF Experiment

[PASTE CONTEXT BLOCK HERE]

[PASTE FITTED EQUATION AND BEST-FIT PARAMETERS FROM PROMPT 4 HERE]

STEP 1 — Extend to 3-observer scenario
  The 2-observer EWF has: Friend F, Wigner W
  The 3-observer EWF adds: Super-Wigner SW who measures the entire W lab
  
  Using T4 colimit generalization from VVV-QMRF (N-observer K_joint),
  extend the fitted equation to compute:
    P(o_F, o_W, o_SW | best-fit parameters)
  
  State all additional assumptions required for this extension.
  If the extension requires assumptions not present in K1-K8 or T4,
  flag each one explicitly as ASSUMPTION.

STEP 2 — Compute VVV-QMRF prediction
  Using best-fit parameter values from Prompt 4 (no re-fitting),
  compute P(o_F, o_W, o_SW) for the 3-observer scenario.
  Report the full probability distribution over all outcome combinations.

STEP 3 — Compute Standard QM prediction
  For the same 3-observer scenario, compute the Standard QM prediction
  using the Born rule and unitary evolution.
  Use the same physical setup (same states, same measurements).

STEP 4 — Identify the difference
  For each outcome combination (o_F, o_W, o_SW):
    — VVV-QMRF prediction: [number]
    — Standard QM prediction: [number]
    — Difference: [number]
    — Difference as fraction of Standard QM value: [number]
  
  If all differences are zero: state "VVV-QMRF makes no new prediction
  in the 3-observer scenario with current axiomatization."
  
  If any difference is nonzero:
    — Identify the outcome combination with the largest difference
    — Compute how many experimental runs are needed to distinguish
      the two predictions at 3-sigma confidence
    — Describe the physical setup of the experiment required

STEP 5 — Falsifiability statement
  Write a single falsifiability statement in the form:
  "VVV-QMRF predicts [X] in scenario [Y].
   If experimental measurement of [observable] yields [Z] ≠ [X],
   VVV-QMRF as currently formulated is falsified."
  
  If no such statement can be written, state why and identify
  which additional axioms or definitions would be needed.
```

---

## PROMPT 6 — Structural Reduction Check

**Goal:** Verify whether known QM interpretations are special cases of VVV-QMRF.

**Input required:** Full outputs from Prompts 1-5.

```
TASK: Check Whether Standard QM Interpretations Are Special Cases of VVV-QMRF

[PASTE CONTEXT BLOCK HERE]

[PASTE FITTED EQUATION FROM PROMPT 4 HERE]

For each interpretation below, determine whether it is a special case
of VVV-QMRF by identifying the K-space parameter values or conditions
under which VVV-QMRF reduces to that interpretation.

For each interpretation, answer:
  CONDITION: "VVV-QMRF reduces to [interpretation] when [parameter conditions]"
  VERIFICATION: Show that under these conditions the VVV-QMRF equation
                produces identical predictions to [interpretation]
  STATUS: CONFIRMED / UNCONFIRMED / IMPOSSIBLE

INTERPRETATION 1 — Copenhagen (single definite outcome, collapse upon measurement)
  Candidate reduction condition: cert=1, V=1 for exactly one outcome per measurement,
  V=0 for all others. Verify or refute.

INTERPRETATION 2 — Many-Worlds (all outcomes realized in branches)
  Candidate reduction condition: K_joint always exists for all observer pairs,
  ⊥_K never fires. Verify or refute.

INTERPRETATION 3 — Relational QM (facts relative to each observer, no absolute facts)
  Candidate reduction condition: ⊥_K fires for all cross-observer pairs,
  no global K_joint exists. Verify or refute.

INTERPRETATION 4 — QBism (probabilities are agent beliefs, not objective facts)
  Candidate reduction condition: cert encodes agent-specific registration,
  no inter-agent V comparison is defined. Verify or refute.

After checking all four:
  — Which interpretations are confirmed special cases?
  — Which are impossible to recover from K1-K8?
  — Is there a region of K-space parameter space that corresponds to
    none of the above interpretations? If yes, describe it.
    This region, if nonempty, is where VVV-QMRF makes genuinely new claims.
```

---

## PROMPT 7 — Honest Assessment

**Goal:** Identify the weakest points in the entire derivation chain before any publication or claim.

**Input required:** Full outputs from Prompts 1-6.

```
TASK: Adversarial Assessment of Entire VVV-QMRF Derivation Chain

[PASTE CONTEXT BLOCK HERE]

[PASTE SUMMARY OF KEY RESULTS FROM PROMPTS 1-6 HERE]

You are acting as the most skeptical reviewer at a top physics journal.
Your job is to find every weak point. Do not be diplomatic.

ASSESSMENT 1 — Assumption audit
  List every assumption made across Prompts 1-6 that is NOT derivable from K1-K8.
  For each assumption:
    — State it precisely
    — State what breaks if it is false
    — Rate its justification: JUSTIFIED / WEAKLY JUSTIFIED / UNJUSTIFIED

ASSESSMENT 2 — Circular reasoning check
  Identify any place in the derivation chain where a conclusion was used
  to justify a premise that leads back to that conclusion.
  Flag AJVS specifically: is it a genuine axiom or a conclusion disguised as an axiom?

ASSESSMENT 3 — Alternative explanations
  For each result that differs from Standard QM:
    — Can the difference be explained by a simpler existing framework?
    — Does the difference require VVV-QMRF specifically, or would any
      framework with similar free parameters produce the same fit?

ASSESSMENT 4 — Missing physics
  What physical content is cert encoding that Standard QM does not encode?
  What physical content is V encoding that Standard QM does not encode?
  If the answer to both is "none," state: "K-space is currently a
  notational variant of Standard QM, not an extension of it."

ASSESSMENT 5 — Publication readiness
  What is the minimum additional work required before this framework
  could be submitted to Foundations of Physics or Physical Review A?
  State each item as a concrete task with estimated difficulty:
    EASY / MEDIUM / HARD / REQUIRES_EXPERT_COLLABORATION

Conclude with a single paragraph summary of the overall scientific status
of VVV-QMRF as assessed through this prompt sequence.
Do not soften the assessment.
```

---

## EXECUTION NOTES

**Data source for Prompt 4:**
Proietti et al. 2019 — "Experimental test of local observer independence"
arXiv: 1902.05080
DOI: 10.1126/sciadv.aaw9832
Obtain Table 1 from the published paper for correlation values.

**If Prompt 2 produces no surviving candidates:**
This is a significant finding. It means K1-K8 as currently formulated
do not generate a probability equation distinguishable from Standard QM.
The correct response is to document this finding and identify which
additional axiom or definition would be needed to close the gap —
not to continue to Prompts 3-7.

**If Prompt 5 produces zero difference:**
This means VVV-QMRF is currently empirically equivalent to Standard QM.
The framework may still have philosophical or interpretational value,
but cannot be claimed as a physical extension of QM without further development.

**LLM recommendation:**
Use Claude Opus or GPT-4 class models for Prompts 1-3 (structural reasoning).
Use a model with code execution for Prompts 4-5 (numerical fitting).
Run Prompt 7 in a separate session after all other outputs are complete.
