# VVV-QMRF: Three Conditions for Scientific Validity
## Applied to the Wigner's Friend Experimental Program

**Document type:** Scientific validity plan
**Target:** VVV-QMRF Working Paper — Testable Prediction Section
**Depends on:** VVV-QMRF_Testable_Prediction_Plan_v3.md
**Author:** Viet Nguyen Xuan (VietVunVut)
**Version:** 1.0

---

## The Central Question VVV-QMRF Must Answer

Not a philosophical question. Not a question about the nature of reality.
One specific, empirically addressable question:

> "In Extended Wigner's Friend experiments, violations of Local Friendliness
> inequalities appear in exactly which configurations — and why those
> configurations and not others?"

Existing frameworks answer: "Do violations occur?" — yes or no depending
on interpretation.

Nobody answers: "Why here and not there?"

VVV-QMRF has a specific answer: violations appear exactly where two
observers require a K_joint, and K_joint does not exist because it
violates E7 Axiom 2. Where K_joint is not required, no violation occurs.

This is a structural prediction about the geometry of violations,
not merely a prediction about their existence.

The following three conditions must all be satisfied for this answer
to have scientific value.

---

## Condition 1: Formalize "Configurations That Require K_joint"

### What this means

VVV-QMRF predicts that violations occur exactly where two observers'
registration spaces cannot be merged into a single K_joint satisfying
E1 and E7 simultaneously.

This prediction is currently stated in prose.
It must be stated in formal parameter terms.

### What must be produced

A formal function or criterion that takes an EWF setup as input and
outputs: "K_joint required" or "K_joint not required."

The input parameters to formalize over:

```
1. Entanglement structure of the shared quantum state |ψ⟩
   - Separable states: K_joint likely not required
   - Maximally entangled states: K_joint likely required
   - Partial entanglement: threshold to be determined

2. Measurement basis choices of each observer
   - Commuting bases: K_joint likely not required
   - Non-commuting bases: K_joint likely required
   - Angle between bases: continuous parameter

3. Whether observers' registration events are space-like separated
   - Separated: K_joint structurally impossible
   - Not separated: K_joint may be possible

4. Whether Wigner performs interference measurement on Friend's lab
   - No interference: K_joint not invoked
   - Interference: K_joint required, E7 Axiom 2 at risk
```

### Formal target

Define a binary predicate:

```
requires_K_joint(ψ, basis_F, basis_W, separation, interference) → {0, 1}

where:
  ψ             = shared quantum state
  basis_F       = Friend's measurement basis
  basis_W       = Wigner's measurement basis
  separation    = space-like separation flag
  interference  = Wigner interference measurement flag

requires_K_joint = 1  iff  K_joint existence would violate E7 Axiom 2
requires_K_joint = 0  iff  K_joint can be constructed satisfying E1 and E7
```

VVV-QMRF prediction, formally stated:

```
violation_predicted(config) = requires_K_joint(config)
```

Violations are predicted if and only if K_joint is required and fails.

### Current status

This predicate is not yet formally defined.
Condition 1 is the primary open item for the working paper.
Without it, the prediction remains a structural claim in prose,
not a falsifiable scientific statement.

### Action required

Write requires_K_joint as a formal definition grounded in E1, E6, E7.
Test it against at least two concrete EWF configurations:
one where K_joint is required, one where it is not.
This must be done before the paper is submitted.

---

## Condition 2: The Prediction Must Be Asymmetric

### What this means

If VVV-QMRF always agrees with standard QM predictions,
it adds nothing. A framework that never disagrees with existing
theory cannot be confirmed or falsified.

The prediction must be asymmetric: there must exist at least one
configuration where VVV-QMRF predicts differently from at least
one existing framework.

### Two target asymmetries

**Asymmetry A: VVV-QMRF predicts NO violation where another framework predicts YES**

Target: find a configuration where:
- Decoherence framework predicts: violations possible
- Objective collapse predicts: violations possible
- VVV-QMRF predicts: NO violation, because requires_K_joint = 0

If K_joint can be constructed without violating E7 for this configuration,
VVV-QMRF predicts no structural incompatibility, therefore no violation
from the registration-layer perspective.

This would be a stronger test than existing no-go theorems provide.

**Asymmetry B: VVV-QMRF predicts YES violation where another framework predicts AMBIGUOUS**

Target: find a configuration where:
- QBism says: question is ill-posed for this configuration
- Relational QM says: both descriptions valid, no violation expected
- VVV-QMRF predicts: violation, because requires_K_joint = 1 and K_joint fails E7

This positions VVV-QMRF as more predictively specific than QBism
and Relational QM for this class of configurations.

### Minimum requirement

At least ONE asymmetric prediction must be identified and stated
before the paper is submitted.

Without asymmetry, the paper describes a consistent framework.
With asymmetry, it describes a testable framework.
The difference matters enormously for how reviewers evaluate it.

### Candidate configuration for Asymmetry A

Configuration: two observers, separable (non-entangled) shared state,
Wigner performs interference measurement.

Standard QM with unitarity: violations possible in principle.
VVV-QMRF: if the shared state is separable, the two registration
events may not require K_joint because E7 Axiom 2 conflict depends
on entanglement structure generating contradicting registrations.

Requires_K_joint(separable, any, any, any, interference) = ?

This is a concrete open question. Answer it formally.

### Action required

For each row of the existing interpretation comparison table
(Copenhagen, Many-Worlds, QBism, Relational QM, Objective Collapse),
identify one configuration where VVV-QMRF predicts differently.
State the configuration precisely using the parameter list from Condition 1.
If no asymmetry can be found for any row, state this explicitly.
Absence of asymmetry is a result. It means the framework is
interpretation-neutral, which is a weaker but still valid contribution.

---

## Condition 3: Map the Prediction onto Existing Experimental Data

### What this means

No new experiment is required.
Proietti et al. (2019) and Bong et al. (2020) produced published data.
The $K_F \perp_K K_W$ prediction must be applied to that data.

This is the difference between a theoretical framework and a scientific one:
a scientific framework makes contact with existing evidence.

### Proietti et al. (2019) — Science Advances 5(9), eaaw9832

Setup summary:
- Six photons across two laboratories
- Two Friends (internal photons), two Wigners (external photons)
- Measured Bell-type correlations
- Violated Local Friendliness inequality by ~5 standard deviations

VVV-QMRF application target:

```
Step 1: Identify all measurement configurations tested in the experiment.
Step 2: Apply requires_K_joint to each configuration.
Step 3: Check: do violations in the data correspond to
        configurations where requires_K_joint = 1?
Step 4: Check: do non-violations (or weaker violations) correspond to
        configurations where requires_K_joint = 0?
Step 5: State whether the distribution of violations is consistent
        with the K_F ⊥_K K_W prediction.
Step 6: State explicitly whether the check was passed, failed,
        or inconclusive due to incomplete formalization of
        requires_K_joint (Condition 1).
```

### Bong et al. (2020) — Nature Physics 16, 1199-1205

Setup summary:
- Bell-type test of Local Friendliness assumptions
- Three assumptions tested: No-Superdeterminism, Locality,
  Absoluteness of Observed Events (AoE)
- Results: at least one of the three must be false

VVV-QMRF application target:

```
Step 1: VVV-QMRF drops AoE — Absoluteness of Observed Events.
        K_F ⊥_K K_W directly implies that observed events
        are not absolute across observers.
Step 2: Check: is the pattern of AoE violations in Bong et al.
        consistent with the K_joint failure structure?
Step 3: Specifically: do violations cluster in the parameter
        region where requires_K_joint = 1?
Step 4: State consistency or inconsistency explicitly.
```

### Honest disclosure requirement

If Condition 1 (formal definition of requires_K_joint) is not complete
before the paper is submitted, this section must be labeled:

> "Condition 3 check is pending formalization of requires_K_joint.
> The structural prediction is stated. Contact with existing data
> is an open item listed in Section 8 (Open Items)."

Do not claim the check has been done if it has not.
An honest "not yet done" is more valuable than a vague "consistent with."

### What a successful Condition 3 looks like

Not: "Our framework is broadly consistent with Proietti et al."
This is untestable prose.

Yes: "Applying requires_K_joint to the 6 configurations tested in
Proietti et al., we find K_joint required in configurations C1, C3, C5,
and not required in C2, C4, C6. Violations in the published data
appear in C1, C3, C5 and not in C2, C4, C6. This is consistent with
the K_F ⊥_K K_W prediction. The check for Bong et al. is pending."

This is specific. This is falsifiable. This is science.

---

## Execution Order

Do these in strict order.
Condition 2 and 3 depend on Condition 1 being formalized first.

```
Step 1: Define requires_K_joint formally.
        Ground it in E1, E6, E7.
        Test it on two concrete configurations.
        Target: 1-2 pages of formal definitions.

Step 2: Apply requires_K_joint to the interpretation comparison table.
        Find at least one asymmetric prediction.
        If none found, state this explicitly.
        Target: 1 page, one configuration per interpretation row.

Step 3: Download Proietti et al. (2019) supplementary data.
        List all tested configurations.
        Apply requires_K_joint to each.
        Check against published violation results.
        Target: 1 table, honest status per configuration.

Step 4: Repeat Step 3 for Bong et al. (2020).

Step 5: Write the paper section using outputs of Steps 1-4.
        Label all incomplete items honestly.
        Submit when Step 1 and at least one of Steps 2-4 are complete.
```

---

## What Each Condition Proves

| Condition | If satisfied | If not satisfied |
|-----------|-------------|-----------------|
| 1: Formalize requires_K_joint | Prediction is precise | Prediction is prose — not falsifiable |
| 2: Asymmetric prediction exists | Framework is testable | Framework is consistent but unfalsifiable |
| 3: Contact with existing data | Framework is scientific | Framework is theoretical only |

All three together: VVV-QMRF makes a specific, falsifiable, evidentially
grounded claim about the geometry of violations in WF experiments.

This is the minimum bar for a working paper in foundations of physics
to be taken seriously by the community.

---

## The One Sentence That Must Appear in the Paper

After completing these three conditions, the paper must contain
this sentence in the abstract or conclusion:

> "VVV-QMRF predicts that violations of Local Friendliness inequalities
> in Extended Wigner's Friend experiments occur if and only if the
> experimental configuration requires a joint K-side registration space
> K_joint that cannot satisfy E1 and E7 simultaneously; this prediction
> is falsified if K_joint can be empirically demonstrated to exist."

If the paper cannot contain this sentence because requires_K_joint
is not yet formalized, the paper is not ready to submit.
Finish Condition 1 first.

---

## Open Items Summary

| Item | Condition | Status |
|------|-----------|--------|
| Define requires_K_joint formally | 1 | Not done |
| Test requires_K_joint on 2 concrete configurations | 1 | Not done |
| Find at least 1 asymmetric prediction | 2 | Not done |
| Apply to Proietti et al. (2019) data | 3 | Not done |
| Apply to Bong et al. (2020) data | 3 | Not done |
| Write requires_K_joint into paper Section 5 | 1,2,3 | Not done |

All six items must be attempted before submission.
Items marked "not done" that remain incomplete must be disclosed
in Section 8 (Open Items) of the paper.

---

*Plan version: 1.0*
*Depends on: VVV-QMRF_Testable_Prediction_Plan_v3.md*
*Next output: requires_K_joint formal definition document*
*Repository: https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework*
