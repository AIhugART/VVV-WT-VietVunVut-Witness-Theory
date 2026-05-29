# VVV-QMRF Pre-Plan Prompt Sequence
# K-Space Axiomatization v3.0 — Pre-Plan Gate Resolution

**Version:** Pre-Plan v1.0 (2026-05-23)
**Purpose:** Resolve five blocking issues before Main Plan Sprint S1 begins.
**Execution order:** PP-1 → PP-2 → PP-3 → PP-4 → PP-5 (PP-5 may run in parallel).
**Rule:** Do not begin Main Plan S1 until all five Pre-Plan outputs are produced and verified.

---

## MASTER CONTEXT BLOCK
*Paste this block at the top of every Pre-Plan prompt session.*

```
FRAMEWORK: VVV-QMRF (VietVunVut Quantum Measurement Registration Framework)
AXIOM STATUS: K1-K8 are FROZEN (Layer 1). T1-T7 are FROZEN (Layer 2).
              K9 is a candidate bridge axiom (Layer 3, default Class D).

K-STATE TUPLE: k = <M, o, cert, t, V> where:
  M    = measurement-registration act identifier
  o    = registered outcome, o ∈ O ∪ {∅}
  cert = self-certification marker ∈ {0,1}   [K3]
  t    = registration timestamp               [K2]
  V    = validity status ∈ {0,1}             [K4, K5]

KEY AXIOMS RELEVANT TO K9:
  K2: (K_R, <_R) is a strict total order; discrete timestamps
  K3: cert(k) = σ_R(M) determined intrinsically
  K4: V(k) = 1 by default on instantiation; V(k) = 0 for null k
  K5: V(k1) → 0 iff ∃k2 later in order such that k2 ⊥_K k1
      within shared C_K sphere with valid authority
  K7: Registration closes at t_close when no K_joint demands remain
  K8: Cross-space embedding preserves V and all tuple fields

STRUCTURAL GAP: K1-K8 produce binary outputs (cert ∈ {0,1}, V ∈ {0,1}).
No mechanism exists to map binary registration states to continuous
probability values. This is the root cause requiring K9.

THREE DATA SOURCES:
  D1: Proietti et al. 2019, arXiv:1902.05080
      CHSH experiment; S_exp = 2.416 ± 0.075 (5σ); 4 expectation values ⟨A_xB_y⟩
  D2: Bong et al. 2020, arXiv:1907.05607
      Local Friendliness (LF) inequality violation; stronger than Bell-Wigner
  D3: Frauchiger & Renner 2018, arXiv:1604.07422
      Theoretical no-go; agents F/F̄/W/W̄; Table 4 statements

PARAMETER BUDGET CONSTRAINT:
  D1 provides 4 data points → K9 candidates must have ≤ 2 free parameters
  to maintain DOF ≥ 1 for χ² goodness-of-fit test.

CLAIM CLASS DISCIPLINE:
  Class D = conjecture, not yet testable
  Class C = testable claim derived rigorously from K1-K8
  Default for K9 = Class D. Class C requires 2-stage audit (P8-C5 + P9-C6).

BOUNDARY: VVV-QMRF does not modify the Born rule. It adds a registration
layer. K9 must reduce to Born rule when cert=1 ∧ V=1 for all k.
```

---

## PP-1: Fix K9_A — Division by Zero

**Blocking issue:** K9_A as written in plan v3.0 contains division by zero
when V=0. This is a mathematical error that must be corrected before any
Python script uses K9_A.

**Current broken definition:**
```
K9_A: P(o | K) = V(k) · |⟨o|ψ⟩|² / Z(K)
      Z(K) = Σ_o V(k) · Tr(E_o ρ)
```
When V(k)=0: Z(K)=0, P(o|K)=0/0. Undefined.

**Goal of this prompt:** Produce a corrected K9_A definition with no
division by zero, correct Born rule recovery, and honest assessment of
distinguishability conditions.

```
TASK: Fix K9_A Bridge Axiom Definition

[PASTE MASTER CONTEXT BLOCK HERE]

The current K9_A definition has a division-by-zero error when V(k)=0.
Your task is to produce a corrected K9_A that satisfies all constraints below.

CONSTRAINT 1 — No division by zero:
  The definition must be well-formed for all V(k) ∈ {0,1}.
  When V=0, the equation must not divide by zero or produce undefined values.

CONSTRAINT 2 — Born rule recovery:
  When cert=1 ∧ V=1 for all k:
    P(o | k) = Tr(E_o ρ) = |⟨o|ψ⟩|²
  The standard Born rule must be recovered exactly in this limit.
  Show the algebraic derivation explicitly.

CONSTRAINT 3 — Physical interpretation of V=0:
  When V=0, an outcome o occurs at the detector level (physical event)
  but is NOT a valid registered event in K-space.
  The correct behavior is NOT P=0. It is: no P assignment.
  V=0 events contribute to N_null(H) (null registration rate),
  not to the probability distribution over outcomes.

CONSTRAINT 4 — Parameter budget:
  K9_A must have ≤ 1 free parameter (the tightest option within the ≤ 2 budget).
  Identify the free parameter explicitly and state its physical interpretation.

PRODUCE:

(A) CORRECTED K9_A DEFINITION
  Write the corrected axiom in the form:
    Case V(k) = 1: P(o | k) = [equation]
    Case V(k) = 0: [convention — not P=0, explain what happens instead]
  Include: normalization condition, Born rule derivation, free parameter list.

(B) DISTINGUISHABILITY ASSESSMENT
  Under what conditions does K9_A predict differently from Standard QM?
  Be precise: if V=1 always (all registrations succeed), does K9_A
  produce any deviation from Born rule?
  If V-fluctuation across runs is required for distinguishability,
  state this explicitly: "K9_A requires empirical V-fluctuation to produce
  δP ≠ 0. If V=1 in all runs, K9_A is identical to Standard QM."

(C) CLASS ASSIGNMENT
  Based on the corrected definition and the distinguishability assessment,
  assign a preliminary class: Class C or Class D.
  Justify the assignment with reference to K1-K8 derivation and
  whether a falsification condition exists.

(D) WHAT WOULD MAKE K9_A CLASS C
  State exactly what additional condition (observable, experiment, or
  axiom specification) would be required to promote K9_A from Class D to Class C.

Do not soften the assessment if K9_A has no distinguishability under
realistic conditions. State the finding directly.
```

**Expected output:** Corrected K9_A definition (Cases V=1 and V=0 explicit),
Born rule derivation, honest distinguishability statement, class assignment.
Save as: `pre_plan/PP1_K9A_fixed.md`

---

## PP-2: Lock K9_B f-specification

**Blocking issue:** K9_B has three sub-options (B1/B2/B3) with unspecified
free parameter counts. B3 (information-theoretic) may exceed the ≤ 2 parameter
budget. Main Plan Phase 7 cannot evaluate K9_B until one option is locked.

**Current state:**
```
K9_B: P(o | K) = Tr(E_o ρ) · f(cert, V, ⊥_K, C_K)
  B1: multiplicative — f = f_cert · f_V · f_context (1-2 params)
  B2: table-lookup   — f derived from K1-K8 (0 params if derivable)
  B3: information-theoretic — f = I(K;o|context)/H(o) (params TBD)
```

**Goal of this prompt:** Choose and lock one f-specification with
explicit parameter count, Born rule derivation, and derivation trace
from K1-K8.

```
TASK: Lock K9_B f-Specification

[PASTE MASTER CONTEXT BLOCK HERE]

K9_B modulates the Born rule by a context-dependent function f:
  P(o | K) = Tr(E_o ρ) · f(cert, V, ⊥_K, C_K)

Three sub-options exist (B1/B2/B3). Your task is to evaluate all three
and select the primary specification for Main Plan Phase 7.

EVALUATION CRITERIA (apply to each option):
  E1: Can f be fully derived from K1-K8 without additional axioms?
  E2: What is the exact free parameter count? Is it ≤ 2?
  E3: Does f produce a well-formed probability (f ∈ [0,1], normalization)?
  E4: Under what conditions does f ≠ 1? (If f=1 always, K9_B=Standard QM)
  E5: Is the Born rule recovered when cert=1 ∧ V=1 ∧ ⊥_K does not fire?

EVALUATE EACH OPTION:

OPTION B2 — Table-lookup (evaluate first):
  Attempt to fully specify f as a lookup table from K1-K8.
  The inputs are: cert ∈ {0,1}, V ∈ {0,1}, ⊥_K ∈ {fires, silent}.
  That gives 2×2×2 = 8 combinations.
  For each combination, derive f value from K1-K8 axioms.
  If any f value cannot be derived from K1-K8 (requires additional assumption),
  flag it as ASSUMPTION and mark B2 as INCOMPLETE.

OPTION B1 — Multiplicative:
  f = f_cert(cert) · f_V(V) · f_context(⊥_K, C_K)
  Specify:
    f_cert: {0 → α, 1 → 1} where α is a free parameter ∈ [0,1]
    f_V:    {0 → 0, 1 → 1}  (derived from K4/K5, 0 free params)
    f_context: {⊥_K fires → β, ⊥_K silent → 1} where β ∈ [0,1]
  Free parameter count: α + β = 2 parameters (at budget limit).
  Evaluate E1-E5 for B1.

OPTION B3 — Information-theoretic:
  f = I(K; o | context) / H(o)
  Attempt to derive this from K1-K8.
  Count free parameters.
  If parameter count > 2 OR derivation from K1-K8 is not possible
  without additional axioms: formally exclude B3 from Phase 7 and defer.

SELECTION DECISION:
  Using the evaluation above, select ONE primary specification:
  - If B2 is complete (all 8 table entries derivable): select B2 (0 params, strongest)
  - If B2 is incomplete but B1 passes E1-E5: select B1 (2 params, fallback)
  - If both B2 and B1 fail any criterion: report failure; K9_B may not be
    viable for Phase 7

PRODUCE:

(A) EVALUATION TABLE
  For each option: E1/E2/E3/E4/E5 verdict (PASS/FAIL/INCOMPLETE), free param count.

(B) LOCKED SPECIFICATION
  The selected option with complete definition:
  — Exact form of f for all input combinations
  — Free parameter list with physical interpretation
  — Born rule recovery derivation
  — Distinguishability condition (when does f ≠ 1?)

(C) DEFERRED ITEMS
  B3 formal deferral statement (if excluded).
  Any B2 table entries that could not be derived (if B2 is partial).

(D) CLASS ASSIGNMENT
  Preliminary class for locked K9_B (C or D), with justification.
```

**Expected output:** Locked f-specification, evaluation table, class assignment.
Save as: `pre_plan/PP2_K9B_locked.md`

---

## PP-3: Data Extraction from Three Papers

**Blocking issue:** Python fit scripts cannot be written without knowing
exactly which numbers are available in published form in D1/D2/D3.
AI must not assume data availability — every number must be traceable
to a specific paper, section, table, or equation.

**Goal of this prompt:** Produce a data extraction table with every
available numerical value from D1/D2/D3, with explicit source citations
and "NOT FOUND" flags where data is not in published text.

```
TASK: Data Extraction Audit for D1/D2/D3

[PASTE MASTER CONTEXT BLOCK HERE]

Your task is to identify every numerical value available for fitting
from the three primary data sources. For each source, work only from
the published arXiv paper text — do not assume or invent values.

For each value you report, provide:
  — The exact number and its uncertainty (if reported)
  — Source: paper, section, table/equation number
  — Physical quantity it represents
  — Whether it is usable as a direct fit target

If a value is not found in the published text, state: NOT FOUND.
Do not substitute with calculated estimates unless explicitly noted.

---

SOURCE D1: Proietti et al. 2019 (arXiv:1902.05080)
"Experimental test of local observer-independence"

Extract:
  D1-N1: CHSH parameter S_exp (value ± uncertainty)
  D1-N2: Individual expectation value ⟨A_1 B_1⟩ (value ± uncertainty)
  D1-N3: Individual expectation value ⟨A_1 B_2⟩ (value ± uncertainty)
  D1-N4: Individual expectation value ⟨A_2 B_1⟩ (value ± uncertainty)
  D1-N5: Individual expectation value ⟨A_2 B_2⟩ (value ± uncertainty)
  D1-N6: Measurement angles used (φ_1, φ_2 for Alice; φ_1, φ_2 for Bob)
  D1-N7: Total coincidence count (1794 6-fold coincidences — confirm source)
  D1-N8: Quantum state used (singlet fraction or density matrix parameters)

For each: provide source location or NOT FOUND.

DATA USABILITY ASSESSMENT for D1:
  How many independent data points can be used for fitting?
  If only S_exp is available (1 number), state: "D1 provides 1 fit point,
  insufficient for 2-parameter fit. Individual ⟨A_xB_y⟩ values required."
  If all 4 expectation values are available (4 numbers), state: "D1 provides
  4 fit points, sufficient for ≤ 2 free parameters with DOF ≥ 2."

---

SOURCE D2: Bong et al. 2020 (arXiv:1907.05607)
"A strong no-go theorem on the Wigner's friend paradox"

Extract:
  D2-N1: Maximum quantum violation of Genuine LF Facet 1 (value, LF bound)
  D2-N2: Maximum quantum violation of Genuine LF Facet 2 (value, LF bound)
  D2-N3: Measurement angles (φ_1, φ_2, φ_3 for Alice; β for Bob)
  D2-N4: State parameter μ at first LF violation (Semi-Brukner)
  D2-N5: State parameter μ at Genuine LF violation threshold
  D2-N6: LF violation values at high μ with error bars (from experiment)
  D2-N7: Number of measurement settings per party (N=3 confirmed?)
  D2-N8: Total coincidences per measurement set

For each: provide source location or NOT FOUND.

DATA USABILITY ASSESSMENT for D2:
  Are violation values with error bars available per inequality?
  Can the violations be used as fit targets for K9_candidate?
  Note: D2 uses LF observables (not CHSH). State whether K9 candidates
  as currently defined can produce LF observable predictions or require
  extension.

---

SOURCE D3: Frauchiger & Renner 2018 (arXiv:1604.07422)
"Quantum theory cannot consistently describe the use of itself"

Extract:
  D3-S1: Statement from agent F (exact logical content from Table 4 or equivalent)
  D3-S2: Statement from agent F̄ (exact logical content)
  D3-S3: Statement from agent W (exact logical content)
  D3-S4: Statement from agent W̄ (exact logical content)
  D3-N1: Halting probability P(w=ok ∧ w̄=ok) per round (value if given)
  D3-N2: Quantum state used in the thought experiment
  D3-N3: Any numerical prediction distinguishing consistent vs inconsistent theories

For each: provide source location or NOT FOUND.

NOTE: D3 is theoretical. The goal is consistency check, not numerical fit.
State clearly which D3 statements are checkable (K9 either avoids or
reproduces the contradiction) versus which require additional formalization.

---

PRODUCE:

(A) EXTRACTION TABLE
  Three sections (D1/D2/D3), one row per item, columns:
  | ID | Quantity | Value | Uncertainty | Source Location | Usable for Fit |

(B) DATA AVAILABILITY VERDICT
  D1: "N data points available for fitting. Sufficient for M free parameters."
  D2: "LF observable extension required? Y/N. N data points with error bars."
  D3: "Theoretical only. N statements extractable for consistency check."

(C) BLOCKERS
  List any quantity marked NOT FOUND that is required for Phase 10 fitting.
  For each blocker, state: "Phase 10a/b/c cannot proceed without this value.
  Resolution: [contact authors / supplementary material / accept limitation]."

(D) FIT PROTOCOL REVISION (if needed)
  If D1 provides fewer than 4 independent values, revise the fit protocol:
  "Phase 10a fit is constrained to [N] data points. Maximum free parameters: [M]."
```

**Expected output:** Complete extraction table, availability verdict, blocker list.
Save as: `pre_plan/PP3_data_extraction.md`

---

## PP-4: Python Infrastructure Setup and Sanity Check

**Blocking issue:** Phase 10 requires working Python scripts. Bugs found
during Main Plan would block the entire phase. Pre-Plan builds and tests
the infrastructure first.

**This prompt produces code. Run it in a Python environment with numpy,
scipy, and matplotlib installed.**

```
TASK: Build and Verify Python Fit Infrastructure for Phase 10

[PASTE MASTER CONTEXT BLOCK HERE]

[PASTE PP-3 EXTRACTION TABLE OUTPUT HERE — or use placeholder values if PP-3 is incomplete]

Build the Python infrastructure for Phase 10 numerical fits.
Execute all sanity checks and report results. Do not proceed to the
next step if a sanity check fails — fix the bug first.

---

STEP 1: Environment setup

Create directory structure:
  fits/
  fits/.venv/          [Python virtual environment]
  fits/utils/
  fits/utils/__init__.py
  fits/utils/qm_standard.py
  fits/utils/k9a_predictor.py
  fits/utils/k9b_predictor.py
  fits/proietti_chsh_fit.py
  fits/bong_lf_fit.py
  fits/fr_consistency.py
  fits/requirements.txt

requirements.txt content:
  numpy>=1.24
  scipy>=1.10
  matplotlib>=3.7

---

STEP 2: Write fits/utils/qm_standard.py

This module computes Standard QM predictions for CHSH and LF observables.

Functions required:

def qm_singlet_expectation(theta_A, theta_B):
    """
    For singlet state |Φ⁻⟩ = (|HV⟩ - |VH⟩)/√2:
    ⟨A(θ_A) B(θ_B)⟩ = -cos(θ_A - θ_B)
    Returns: float in [-1, 1]
    """

def qm_chsh_S(theta_A1, theta_A2, theta_B1, theta_B2):
    """
    S = ⟨A1B1⟩ - ⟨A1B2⟩ + ⟨A2B1⟩ + ⟨A2B2⟩
    QM maximum: 2√2 ≈ 2.828
    Returns: float
    """

def qm_chsh_all_expectations(theta_A1, theta_A2, theta_B1, theta_B2):
    """
    Returns dict: {(1,1): ⟨A1B1⟩, (1,2): ⟨A1B2⟩, (2,1): ⟨A2B1⟩, (2,2): ⟨A2B2⟩}
    """

SANITY CHECK 2A: At angles θ_A1=0, θ_A2=π/4, θ_B1=π/8, θ_B2=3π/8
(CHSH-optimal angles), verify S = 2√2 ≈ 2.828 ± 0.001.
Report: PASS or FAIL with computed value.

---

STEP 3: Write fits/utils/k9a_predictor.py

This module computes K9_A predictions using the corrected definition from PP-1.

[PASTE PP-1 CORRECTED K9_A DEFINITION HERE]

Functions required:

def k9a_expectation(theta_A, theta_B, v_rate=1.0):
    """
    K9_A prediction for ⟨A(θ_A) B(θ_B)⟩.
    v_rate: fraction of runs where V(k)=1 (registered).
            Range: [0, 1]. Default 1.0 = all runs registered.
    
    When v_rate=1.0: must return identical value to qm_singlet_expectation.
    When v_rate=0.0: no registered events (return None or raise, not 0/0).
    """

def k9a_chsh_S(theta_A1, theta_A2, theta_B1, theta_B2, v_rate=1.0):
    """
    K9_A CHSH parameter S.
    """

SANITY CHECK 3A: k9a_expectation(0, π/8, v_rate=1.0) must equal
qm_singlet_expectation(0, π/8) exactly.
Report: PASS or FAIL with both values.

SANITY CHECK 3B: k9a_expectation(any, any, v_rate=0.0) must not
produce division by zero or NaN. Must return None or equivalent.
Report: PASS or FAIL.

SANITY CHECK 3C: At CHSH-optimal angles with v_rate=1.0,
k9a_chsh_S must equal 2√2 ≈ 2.828.
Report: PASS or FAIL with computed value.

---

STEP 4: Write fits/utils/k9b_predictor.py

This module computes K9_B predictions using the locked specification from PP-2.

[PASTE PP-2 LOCKED K9_B SPECIFICATION HERE]

Functions required:

def k9b_f(cert, V, perp_k_fires, alpha=1.0, beta=1.0):
    """
    K9_B modulation function f(cert, V, ⊥_K).
    cert: int ∈ {0,1}
    V: int ∈ {0,1}
    perp_k_fires: bool
    alpha: free parameter for cert scaling (default 1.0 = no effect)
    beta:  free parameter for ⊥_K context (default 1.0 = no effect)
    Returns: float in [0,1]
    """

def k9b_expectation(theta_A, theta_B, cert=1, V=1,
                    perp_k_fires=False, alpha=1.0, beta=1.0):
    """
    K9_B prediction for ⟨A(θ_A) B(θ_B)⟩.
    """

SANITY CHECK 4A: k9b_expectation(any, any, cert=1, V=1,
perp_k_fires=False, alpha=1.0, beta=1.0) must equal
qm_singlet_expectation(any, any) exactly.
(Born rule recovery: all defaults → Standard QM)
Report: PASS or FAIL.

SANITY CHECK 4B: k9b_expectation(any, any, cert=0, V=1,
perp_k_fires=False, alpha=0.5, beta=1.0) must equal
0.5 × qm_singlet_expectation(any, any).
(cert=0 with α=0.5 produces half-weighted prediction)
Report: PASS or FAIL.

---

STEP 5: Write fits/proietti_chsh_fit.py (skeleton with placeholder data)

[PASTE D1 EXTRACTED VALUES FROM PP-3 HERE, or use placeholders]

PLACEHOLDER (use if PP-3 data not yet available):
  DATA = {
    (1,1): {'value': None, 'error': None},  # ⟨A1B1⟩ NOT YET EXTRACTED
    (1,2): {'value': None, 'error': None},  # ⟨A1B2⟩ NOT YET EXTRACTED
    (2,1): {'value': None, 'error': None},  # ⟨A2B1⟩ NOT YET EXTRACTED
    (2,2): {'value': None, 'error': None},  # ⟨A2B2⟩ NOT YET EXTRACTED
  }
  S_EXP = 2.416
  S_ERR = 0.075
  ANGLES_A = (168 * pi/180, 0 * pi/180)       # φ1=168°, φ2=0°
  ANGLES_B = (168 * pi/180, 175 * pi/180)     # β=175°, confirm from paper

Script structure (do not run fit if data is None):

  1. Load data (real or placeholder)
  2. Define residuals function for K9_A (v_rate as free param)
  3. Define residuals function for K9_B (alpha, beta as free params)
  4. If data is not None: run scipy.optimize.least_squares
     If data is None: print "DATA NOT YET EXTRACTED — placeholder mode"
  5. Compare fit quality: K9_A vs K9_B vs Standard QM
  6. Report: best-fit params, χ², DOF, residuals per data point

SANITY CHECK 5A: Run script in placeholder mode.
Script must print "DATA NOT YET EXTRACTED — placeholder mode" without errors.
Report: PASS or FAIL.

---

STEP 6: Write fits/fr_consistency.py (skeleton)

Script structure:

  1. Load FR statements D3-S1/S2/S3/S4 (as strings or structured data)
  2. For each statement, check whether K9_candidate's registration logic
     is consistent with the statement (manual logical check, not numerical fit)
  3. Output: CONSISTENT / INCONSISTENT / UNDETERMINED per statement
  4. If K9 avoids FR contradiction: identify which axiom blocks it
     (K5 V_prov pre-closure / K7 t_close timing / K8 cross-space)

SANITY CHECK 6A: Run script with placeholder statements.
Script must run without errors and output UNDETERMINED for all statements.
Report: PASS or FAIL.

---

PRODUCE:

(A) ALL SCRIPT FILES
  Paste complete code for each file.

(B) SANITY CHECK REPORT
  Table: | Check ID | Expected | Actual | Status (PASS/FAIL) |
  All checks must PASS before Pre-Plan PP-4 is complete.
  If any check FAILS: identify the bug, fix it, re-run, report fix.

(C) INFRASTRUCTURE READINESS VERDICT
  "All N sanity checks PASS. Python infrastructure is ready for Phase 10."
  OR
  "N checks FAIL. Blockers: [list]. Phase 10 cannot begin until resolved."
```

**Expected output:** All script files + sanity check report + readiness verdict.
Save scripts to: `fits/` directory structure as specified.
Save report as: `pre_plan/PP4_infrastructure_report.md`

---

## PP-5: Gate Relocation — Move G1/G2/G3 from Phase 7 to Phase 9

**Blocking issue:** Plan v3.0 places operationalizability gates G1/G2/G3
in Phase 7 (Constraint Identification). These gates test properties of
a proposed equation — but no equation exists at Phase 7. Gates can only
apply to equations generated in Phase 8. This is a structural logic error
that must be corrected before Phase 7 runs.

**This prompt produces a patch document, not code.**

```
TASK: Gate Relocation Patch — P7-G1/G2/G3 to Phase 9

[PASTE MASTER CONTEXT BLOCK HERE]

PROBLEM STATEMENT:
Plan v3.0 Phase 7 includes three blocking gates:
  P7-G1: Operationalization of Phys(o|H_physics)
  P7-G2: Nontrivial registration gap (Phys=1 ∧ Lock_K=0 possible?)
  P7-G3: Operational t_lock definition

These gates ask: "Does the equation satisfy operationalizability conditions?"
Phase 7 is Constraint Identification — no equation has been proposed yet.
The gates cannot be evaluated against a non-existent equation.

Phase 8 generates candidate equations.
Phase 9 adversarially tests them.
Gates G1/G2/G3 belong in Phase 9, applied to each surviving candidate.

YOUR TASK: Produce a formal patch document that:

(A) DOCUMENTS THE LOGIC ERROR
  State in one paragraph why G1/G2/G3 cannot be evaluated in Phase 7.
  Use the principle: "A gate that tests property X of object Y
  can only fire after object Y exists."

(B) SPECIFIES THE RELOCATION
  FROM: Phase 7 (Constraint Identification) — REMOVE G1/G2/G3
  TO:   Phase 9 (Adversarial Falsification) — ADD as P9-G1/G2/G3
  
  New Phase 9 check order (after relocation):
    P9-C1: Physical counterexample test
    P9-C2: Axiom consistency check
    P9-C3: Distinguishability verification
    P9-C4: cert + V sensitivity
    P9-G1: [relocated] Operationalization of Phys(o|H_physics)
    P9-G2: [relocated] Nontrivial registration gap
    P9-G3: [relocated] Operational t_lock definition
    P9-C5: Ranking (after all above)
    P9-C6: Class C eligibility Stage 2

(C) REVISED PHASE 7 SCOPE
  After removing G1/G2/G3, Phase 7 contains only:
    P7-C1: Category A — Internal consistency K1-K8
    P7-C2: Category B — Physical validity (Born rule limit)
    P7-C3: Category C — Distinguishability of K9_A/B (BLOCKING gate)
  
  State: "Phase 7 evaluates constraints on what any valid K9 equation
  must satisfy. It does not evaluate specific equations. Gates that test
  equation-level properties are deferred to Phase 9."

(D) VERIFY NO OTHER PHASE ASSIGNMENTS ARE AFFECTED
  Check the dependency map:
    Phase 7 → Phase 8: P7-C1/C2/C3 feed derivation constraints. UNCHANGED.
    Phase 8 → Phase 9: P8-C1..C5 feed adversarial tests. UNCHANGED.
    Phase 9 now includes P9-G1/G2/G3. Does this affect Phase 10 inputs?
    Phase 9 → Phase 10: P9-C5 ranking selects K9_candidate for fit. UNCHANGED.
  
  Confirm: relocation affects Phase 7 and Phase 9 only. No cascade changes.

(E) ISSUE REGISTRY UPDATE
  Remove P7-G1/G2/G3 from Phase 7 issue registry.
  Add P9-G1/G2/G3 to Phase 9 issue registry with severity BLOCKING.
  Updated Phase 7 registry: P7-C1 (HIGH), P7-C2 (HIGH), P7-C3 (BLOCKING).
  Updated Phase 9 registry: P9-C1..C6 (existing) + P9-G1/G2/G3 (BLOCKING).
```

**Expected output:** Formal patch document with all five sections (A-E) complete.
Save as: `pre_plan/PP5_gate_relocation_patch.md`

---

## PRE-PLAN COMPLETION GATE

Before approving Main Plan Sprint S1, verify all five outputs exist and pass:

```
TASK: Pre-Plan Completion Verification

Verify the following five outputs are complete and internally consistent.
For each output, state: COMPLETE / INCOMPLETE / FAILED, with one-sentence reason.

PP-1 VERIFICATION:
  File: pre_plan/PP1_K9A_fixed.md
  Check: Does K9_A definition have no division by zero?
  Check: Is Born rule recovery algebraically shown?
  Check: Is distinguishability condition stated honestly?
  Verdict: COMPLETE / INCOMPLETE / FAILED

PP-2 VERIFICATION:
  File: pre_plan/PP2_K9B_locked.md
  Check: Is exactly ONE f-specification selected (B1, B2, or B3)?
  Check: Is free parameter count explicitly stated and ≤ 2?
  Check: Is B3 formally deferred if not selected?
  Verdict: COMPLETE / INCOMPLETE / FAILED

PP-3 VERIFICATION:
  File: pre_plan/PP3_data_extraction.md
  Check: Does table have explicit NOT FOUND entries where data is unavailable?
  Check: Is data usability verdict stated (N data points for D1/D2)?
  Check: Are Phase 10 blockers listed if any values are NOT FOUND?
  Verdict: COMPLETE / INCOMPLETE / FAILED

PP-4 VERIFICATION:
  Files: fits/utils/qm_standard.py, fits/utils/k9a_predictor.py,
         fits/utils/k9b_predictor.py, fits/proietti_chsh_fit.py,
         fits/fr_consistency.py
  Check: Do all sanity checks PASS (2A, 3A, 3B, 3C, 4A, 4B, 5A, 6A)?
  Check: Does K9_A predictor return None (not 0/0) when v_rate=0?
  Check: Does K9_A predictor return Standard QM value when v_rate=1.0?
  Verdict: COMPLETE / INCOMPLETE / FAILED

PP-5 VERIFICATION:
  File: pre_plan/PP5_gate_relocation_patch.md
  Check: Are G1/G2/G3 removed from Phase 7 issue registry?
  Check: Are P9-G1/G2/G3 added to Phase 9 issue registry?
  Check: Is dependency map verified (cascade = none)?
  Verdict: COMPLETE / INCOMPLETE / FAILED

OVERALL PRE-PLAN VERDICT:
  If ALL FIVE = COMPLETE: "Pre-Plan complete. Main Plan S1 is approved."
  If ANY = INCOMPLETE or FAILED: "Pre-Plan incomplete. Main Plan S1 is BLOCKED.
  Remaining items: [list]. Resolve before S1."
```

**Expected output:** Five-item verification table + overall verdict.
Save as: `pre_plan/PP0_completion_gate.md`

---

## EXECUTION NOTES

**Session allocation:** Each PP task is one session. Do not combine PP-1
and PP-2 into a single session — they are independent problems that benefit
from full attention per session.

**PP-3 requires paper access:** PP-3 cannot be completed by AI alone.
The researcher must open arXiv:1902.05080, arXiv:1907.05607, and
arXiv:1604.07422, locate the specific tables and equations, and paste
the extracted numbers into the prompt. AI will structure and verify the
extraction but cannot substitute for reading the actual papers.

**PP-4 depends on PP-1 and PP-2:** Do not run PP-4 until PP-1 and PP-2
are complete. The corrected K9_A and locked K9_B definitions must be
pasted into the PP-4 prompt where indicated.

**PP-5 is independent:** PP-5 can run in parallel with PP-1 through PP-4.
It requires no numerical outputs from other Pre-Plan tasks.

**If PP-1 finds K9_A has no distinguishability:** This is a legitimate
scientific finding. Document it honestly in PP1_K9A_fixed.md. Do not
modify K9_A to artificially introduce distinguishability. The Pre-Plan
completion gate (PP0) still passes — "K9_A has no distinguishability
under realistic conditions" is a valid output that informs Phase 7.

**LLM recommendation:** Use Claude Opus or GPT-4 class models.
For PP-4 (code generation and execution), use a model with code
execution capability. Run PP-3 with the researcher present to paste
actual paper values.
