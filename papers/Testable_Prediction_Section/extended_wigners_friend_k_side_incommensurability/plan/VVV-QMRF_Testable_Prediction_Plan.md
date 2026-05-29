# VVV-QMRF: Plan for Testable Prediction Section
## "A Testable Prediction: K-side Incommensurability in Extended Wigner's Friend Scenarios"

**Document type:** Section development plan + formalization scaffold
**Target paper:** VVV-QMRF Working Paper v2.0
**Target archive:** PhilSci Archive
**Author:** Viet Nguyen Xuan (VietVunVut)
**Plan version:** 1.0

---

## Part 1: Why This Section Exists

### 1.1 The problem with framework papers

A theoretical framework that is only consistent with existing experiments
is unfalsifiable. Unfalsifiable frameworks are not accepted as scientific
contributions, regardless of their internal coherence.

VVV-QMRF currently satisfies: consistent with all known QM experiments.
VVV-QMRF does not yet satisfy: predicts something new that QM does not.

This section is the bridge between those two states.

### 1.2 Why Wigner's Friend is the right target

Three reasons:

1. Active experimental program exists right now.
   Proietti et al. (2019), Bong et al. (2020), and ongoing work
   at multiple groups mean any prediction can be checked against
   real data within years, not decades.

2. VVV-QMRF already partially addresses it.
   E1 assertion table explicitly marks "Addresses K-side framing
   of Wigner's Friend" as Class C conjecture. This section
   upgrades that conjecture to a formal prediction.

3. The prediction does not require full mathematical structure of K.
   It requires only the layer separation (rho-side vs K-side)
   and the E1 self-certification property. Both are already
   defined at Class D level.

---

## Part 2: Background — What Wigner's Friend Is

### 2.1 Original thought experiment (Wigner, 1961)

Setup:
- Friend F is inside a sealed lab
- F measures quantum system S (spin-1/2, superposition state)
- F obtains definite result: spin up or spin down
- F's measurement collapses the wavefunction from F's perspective

- Outside observer W (Wigner) has not interacted with the lab
- From W's perspective, the lab (F + S) is still in superposition
- W can in principle verify this by performing an interference measurement

Paradox:
- F has a definite registered result
- W describes F+S as still in superposition
- Both descriptions are valid in standard QM
- Standard QM has no formal account of why they differ
  or how to reconcile them

### 2.2 Extended Wigner's Friend (Frauchiger-Renner 2018, Brukner 2018)

Extension adds a second observer pair:
- Two labs, two Friends (F1 and F2), two Wigners (W1 and W2)
- F1 and F2 each measure entangled subsystems
- W1 and W2 each perform interference measurements on their labs
- The four agents can compare notes

Result: under certain assumptions, the four agents reach logically
contradictory conclusions about measurement outcomes.

Brukner (2018) showed this leads to a no-go theorem:
at least one of these must be false:
- (Q) Quantum mechanics is universally valid
- (C) Agents can communicate reliable facts
- (S) Measurement outcomes are single definite facts

This is an open problem. No QM interpretation fully resolves it
without dropping one of the three assumptions.

### 2.3 What standard QM cannot say

Standard QM can describe the physical evolution of each subsystem.
Standard QM cannot formally distinguish:
- A registration event from F's perspective (K-side of F)
- A registration event from W's perspective (K-side of W)
- The relationship between the two K-sides

This is exactly the registration-layer gap that VVV-QMRF addresses.

---

## Part 3: The VVV-QMRF Prediction

### 3.1 Core claim

VVV-QMRF predicts that in Extended Wigner's Friend scenarios,
the K-side registration spaces of different observers are
incommensurable: there is no single K-side space that contains
both observers' registration states as jointly valid entries.

Formally:

Let F and W be two observers in an Extended Wigner's Friend scenario.
Let K_F be the K-side registration space of F.
Let K_W be the K-side registration space of W.

VVV-QMRF prediction:

    There is no K_joint such that:
    K_F ⊆ K_joint AND K_W ⊆ K_joint
    AND all registration states in K_joint satisfy E1 (self-certification)
    AND all registration states in K_joint satisfy E7 (validity)

    Formally: K_F ⊥_K K_W
    where ⊥_K denotes K-side registration incommensurability.

### 3.2 What incommensurability means physically

Incommensurability does NOT mean:
- F and W get different numbers (QM already allows this)
- The outcomes are random or undefined
- Reality is subjective

Incommensurability DOES mean:
- F's registration of outcome o_F is self-certifying (E1) within K_F
- W's registration of F+S as superposition is self-certifying within K_W
- These two certifications cannot be jointly contained in one
  registration space without violating E1 or E7
- The conflict is structural, not epistemic

This is a stronger and more specific claim than QM's current account,
which simply says both descriptions are valid without explaining
the structure of their incompatibility.

### 3.3 Derivation scaffold

Step 1: Apply E6 to each observer.
Each observer is a registering system defined as a process, not a substance.
F = {M_F1, M_F2, ...} ordered by registration time.
W = {M_W1, M_W2, ...} ordered by registration time.
F and W are distinct processes with distinct registration time sequences.

Step 2: Apply E1 to each observer's registration.
F's measurement M_F is self-certifying within K_F:
sigma_F(M_F) = 1, determined intrinsically within K_F.

W's measurement M_W is self-certifying within K_W:
sigma_W(M_W) = 1, determined intrinsically within K_W.

Step 3: Apply E7 to each observer's validity.
V_F(M_F) = 1 by default within K_F.
V_W(M_W) = 1 by default within K_W.

Step 4: Attempt joint registration space K_joint.
For K_joint to contain both:
- k_F = <M_F, o_F, cert_F, t_F, V_F> must satisfy E1 globally
- k_W = <M_W, o_W, cert_W, t_W, V_W> must satisfy E1 globally

Problem: M_W includes a registration of F+S as superposition.
M_F includes a registration of o_F as definite outcome.
These two registrations are mutually contradicting at E7 level:
M_W ⊥ M_F in the sense that V(M_F) = 1 and V(M_W) = 1
cannot both hold in a single K-space without violating E7 Axiom 2.

Therefore K_joint satisfying all conditions does not exist.
Therefore K_F ⊥_K K_W.

### 3.4 Claim classification

| Claim | Class | Status |
|-------|-------|--------|
| K_F and K_W are distinct registration spaces | D | Follows from E6 applied to distinct observers |
| sigma_F and sigma_W operate independently | D | Follows from E1 applied per observer |
| K_joint violates E7 Axiom 2 | D | Follows from E7 applied to contradicting registrations |
| K_F ⊥_K K_W (incommensurability) | C | Conjectured — requires formal proof of Step 4 |
| This prediction is empirically distinguishable from standard QM | C | Requires experimental operationalization (Part 4) |

---

## Part 4: Experimental Operationalization

### 4.1 The key question

K-side incommensurability is a structural claim about registration spaces.
To test it, it must be translated into a claim about observable
correlation patterns in Extended Wigner's Friend experiments.

The translation is: if K_F ⊥_K K_W, then the joint probability
distribution P(o_F, o_W) — the probability that F gets outcome o_F
and W gets outcome o_W — should show a specific signature that
differs from what standard QM predicts under the assumption that
a single consistent assignment of facts exists.

### 4.2 Connection to existing no-go results

Brukner (2018) already showed that assuming a single consistent
fact assignment leads to contradiction (violation of one of Q, C, S).

VVV-QMRF adds: the reason a single consistent fact assignment fails
is precisely K-side incommensurability. K_F ⊥_K K_W is the
registration-layer explanation of why (S) — single definite facts —
must be dropped.

This is not a new empirical prediction over Brukner's theorem.
It is a structural explanation of Brukner's result from the
registration-layer perspective.

The new empirical content, if any, would come from:

Prediction 4.2.1: In any experiment designed to test Brukner's
no-go theorem, the pattern of violations should be consistent
with K-side incommensurability structure — specifically, violations
should appear precisely when two observers' registration events
would require K_joint, and not otherwise.

This is a structural constraint on where violations appear,
not just that violations appear.

### 4.3 Relevant existing experiments

| Experiment | Year | Group | Relevance |
|------------|------|-------|-----------|
| Proietti et al. | 2019 | Heriot-Watt / Edinburgh | First photonic Extended WF test |
| Bong et al. | 2020 | Queensland / Vienna | Bell-type test of WF assumptions |
| Nurgalieva & del Rio | 2019 | ETH Zurich | Consistency conditions for WF |
| Wiseman et al. | 2023 | Griffith / various | Review of WF experimental status |

For each experiment: check whether violation pattern is consistent
with K_F ⊥_K K_W structure as defined in Step 4 of derivation scaffold.

### 4.4 What would falsify the prediction

The prediction is falsified if:
- An Extended WF experiment produces results consistent with a single
  joint K-space satisfying E1 and E7 simultaneously
- Formally: if K_joint exists empirically, then K_F ⊥_K K_W is false
  and VVV-QMRF E7 requires revision

This is a genuine falsification condition.

---

## Part 5: Positioning Against Existing Interpretations

### 5.1 How VVV-QMRF differs from existing responses to WF

| Interpretation | Response to WF paradox | VVV-QMRF difference |
|----------------|------------------------|---------------------|
| Copenhagen | Measurement requires classical apparatus; WF is ill-posed | VVV-QMRF formalizes why: K-side incommensurability |
| Many-Worlds | All outcomes occur; no paradox | VVV-QMRF: registration events are real and singular per K-side |
| QBism | Facts are agent-relative; no paradox | VVV-QMRF: agrees on agent-relativity, adds formal K-side structure |
| Relational QM | Facts are relation-relative; no paradox | VVV-QMRF: closest alignment; adds Pramana-derived registration architecture |
| Objective Collapse | Physical collapse resolves WF | VVV-QMRF: does not require physical collapse mechanism |

### 5.2 Relation to Relational QM (Rovelli)

Relational QM is the closest existing framework to VVV-QMRF on this point.
Rovelli (1996) argues that quantum states are relative to observers.
VVV-QMRF adds: the registration-layer structure that explains *why*
they are relative, and *what formal conditions* govern the relationship
between two observers' relative states.

K_F ⊥_K K_W in VVV-QMRF maps onto Rovelli's claim that F's
description and W's description are both valid relative to their
respective reference systems — but VVV-QMRF provides the formal
machinery (E1, E6, E7) that Relational QM does not.

This is a genuine extension, not a restatement.

---

## Part 6: Section Draft Outline

The actual paper section should follow this structure:

```
Section X: A Testable Prediction: K-side Incommensurability
           in Extended Wigner's Friend Scenarios

X.1 The Extended Wigner's Friend Setup
    - Brief description of EWF scenario
    - State the paradox in terms of registration, not just states
    - Cite: Wigner (1961), Frauchiger & Renner (2018), Brukner (2018)

X.2 Applying VVV-QMRF to EWF
    - Apply E6: two distinct registering processes
    - Apply E1: independent self-certification per observer
    - Apply E7: independent validity per observer
    - Show K_joint fails Axiom 2 of E7

X.3 The Formal Prediction
    - State K_F ⊥_K K_W
    - State claim classification (Class C conjecture)
    - State falsification condition explicitly

X.4 Experimental Connection
    - Connect to Proietti et al. (2019), Bong et al. (2020)
    - State what violation pattern is consistent with K_F ⊥_K K_W
    - State what would falsify it

X.5 Relation to Existing Interpretations
    - Comparison table (abbreviated from Part 5 above)
    - Emphasize: closest to Relational QM, extends it formally

X.6 Status and Limitations
    - Class C: formal proof of Step 4 not yet complete
    - Empirical operationalization requires further work
    - This section is a prediction scaffold, not a completed proof
```

---

## Part 7: Open Items Before Section Can Be Finalized

These must be resolved or explicitly disclosed:

| Item | Status | Action required |
|------|--------|-----------------|
| Formal proof that K_joint violates E7 Axiom 2 | Missing | Write out Step 4 as full logical derivation |
| Definition of ⊥_K (K-side incommensurability) | Informal only | Give precise formal definition |
| Connection between ⊥_K and observable correlations | Informal only | Operationalize into statement about P(o_F, o_W) |
| Check against Proietti et al. data | Not done | Apply ⊥_K structure to published results |
| Distinguish from Relational QM formally | Partial | Write explicit comparison paragraph |

Recommendation: disclose all five as open items within the section.
Label the section "Prediction Scaffold" rather than "Completed Prediction"
if Step 4 formal proof is not ready before submission.

---

## Part 8: Required References for This Section

| Reference | Why needed |
|-----------|-----------|
| Wigner, E.P. (1961). Remarks on the mind-body question. In: The Scientist Speculates, Good (ed.), pp. 284–302 | Original WF thought experiment |
| Frauchiger, D. & Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. Nature Communications 9, 3711 | Extended WF no-go theorem |
| Brukner, C. (2018). A no-go theorem for observer-independent facts. Entropy 20(5), 350 | Bell-type no-go for WF |
| Proietti, M. et al. (2019). Experimental test of local observer-independence. Science Advances 5(9), eaaw9832 | First experimental EWF test |
| Bong, K.W. et al. (2020). A strong no-go theorem on the Wigner's friend paradox. Nature Physics 16, 1199–1205 | Bell-type experimental WF test |
| Rovelli, C. (1996). Relational quantum mechanics. International Journal of Theoretical Physics 35, 1637–1678 | Closest existing framework — must distinguish from |

---

## Summary

Goal: upgrade E1 assertion "Addresses K-side framing of Wigner's Friend"
from Class C conjecture to a formal testable prediction.

Core prediction: K_F ⊥_K K_W — two observers' K-side registration
spaces are incommensurable in Extended Wigner's Friend scenarios.

Falsification condition: existence of K_joint satisfying E1 and E7
simultaneously for both observers would falsify the prediction.

Experimental connection: violation patterns in Proietti et al. (2019)
and Bong et al. (2020) should be consistent with ⊥_K structure.

Status of prediction: Class C — formal derivation scaffold complete,
formal proof of Step 4 and empirical operationalization still required.

Disclose status openly in the paper. A labeled prediction scaffold
is more scientifically valuable than an overclaimed proof.

---

*Plan version: 1.0*
*Repository: https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework*
*To be integrated into: VVV-QMRF Working Paper v2.0, Section X*
