Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF: Condition 3 Execution Plan
## Applying requires_K_joint to Proietti et al. (2019) and Bong et al. (2020)

**Document type:** Execution plan
**Status:** Ready to execute — E01 Section 11 complete
**Depends on:** E01 Section 11.3 (requires_K_joint predicate, Conditions A-D)
**Target:** Satisfy Condition 3 of VVV-QMRF Scientific Validity Requirements
**Author:** Viet Nguyen Xuan (VietVunVut)
**Version:** 1.0

---

## What Condition 3 Requires

Condition 3 states:

> Apply requires_K_joint to existing experimental data.
> Check whether violations in the data correspond to configurations
> where requires_K_joint = 1, and non-violations correspond to
> configurations where requires_K_joint = 0.

This is the step that moves VVV-QMRF from a philosophical framework
to a framework with empirical contact.

Without Condition 3, the paper describes a consistent framework.
With Condition 3, it describes a framework that makes contact
with real experimental evidence.

---

## The requires_K_joint Decision Procedure

Apply this decision tree to every configuration in every experiment.
Use E01 Section 11.3 Conditions A-D as the sole authority.

```
For each configuration (F, W, M_F, M_W, |ψ⟩):

Q1: Does W perform an interference measurement on F's lab?
    YES → requires_K_joint = 1  [Condition A]  STOP
    NO  → continue to Q2

Q2: Do F and W directly compare registration records
    such that a K-side contradiction is detectable?
    YES → requires_K_joint = 1  [Condition B]  STOP
    NO  → continue to Q3

Q3: Is there no interference, no direct comparison,
    and causal isolation between K_F and K_W?
    YES → requires_K_joint = 0  [Condition C]  STOP
    NO  → continue to Q4

Q4: Is the shared quantum state |ψ⟩ separable AND do
    M_F and M_W act on non-overlapping subsystems AND is no
    joint validity check structurally required?
    YES → requires_K_joint = 0  [Condition D]  STOP
    NO  → requires_K_joint = AMBIGUOUS / UNRESOLVED  STOP
```

Conditions A-D are sufficient conditions, not a complete
necessary-and-sufficient classifier. Do not convert the final unresolved
branch into requires_K_joint = 1 unless Condition A or Condition B
clearly applies. Record the triggering condition (A, B, C, or D) for
every resolved result.
If no condition clearly applies, record as AMBIGUOUS and explain why.

---

## Target Paper 1: Proietti et al. (2019)

**Full citation:**
Proietti, M., Pickston, A., Graffitti, F., Barrow, P., Kundys, D.,
Branciard, C., Ringbauer, M., Fedrizzi, A. (2019).
Experimental test of local observer-independence.
Science Advances 5(9), eaaw9832.
DOI: 10.1126/sciadv.aaw9832

**Access:** https://www.science.org/doi/10.1126/sciadv.aaw9832
Supplementary materials available at the same URL.

### Setup summary

Six photons distributed across two laboratories.
Two Friends (internal photons F1, F2).
Two Wigners (external photons W1, W2).
Measured Bell-type correlations to test Local Observer-Independence.
Reported violation of a Clauser-Horne-Shimony-Holt (CHSH) type
inequality by approximately 5 standard deviations.

### What to extract from the paper

Read the paper and supplementary materials. Extract:

```
1. The full list of measurement settings (basis choices) tested.
   These are typically labeled by angles θ_F1, θ_F2, θ_W1, θ_W2
   or similar parametrization.

2. For each measurement setting:
   - Does W perform an interference (reversal) measurement on F's lab?
   - Are F and W measuring entangled subsystems?
   - What is the reported correlation value C(θ_F, θ_W)?
   - Is the Local Friendliness inequality violated for this setting?

3. The specific inequality tested and its classical bound.

4. The data granularity available for comparison:
   - per-configuration / per-setting values,
   - per-inequality-term values,
   - or aggregate-only statistics.

5. Whether supplementary data provides per-configuration violation
   values or only aggregate statistics.
```

If the paper reports only aggregate inequality violation, do not assign
Violation reported? = YES or NO to individual configurations. Mark the
configuration-level match as INCONCLUSIVE and record the data-granularity
limitation explicitly.

### Application table to fill

Fill one row per measurement configuration tested in the paper.

```
| Config ID | W interference? | |ψ⟩ entangled? | Triggering condition | requires_K_joint | Violation reported? | Match? | Notes |
|-----------|----------------|--------------|---------------------|-----------------|---------------------|--------|-------|
| C1        | ?              | ?            | ?                   | ?               | ?                   | ?      |       |
| C2        | ?              | ?            | ?                   | ?               | ?                   | ?      |       |
| ...       |                |              |                     |                 |                     |        |       |
```

Match = YES if:
  requires_K_joint = 1 AND violation reported = YES
  OR
  requires_K_joint = 0 AND violation reported = NO

Match = NO if:
  requires_K_joint = 1 AND violation reported = NO
  OR
  requires_K_joint = 0 AND violation reported = YES

Match = INCONCLUSIVE if:
  Data does not provide per-configuration resolution.
  Record reason.

### Expected outcome

Proietti et al. use a fixed entangled state and vary measurement
basis angles. The interference measurement by W is the key parameter.

Expected under VVV-QMRF:
- Configurations where W performs interference measurement
  → requires_K_joint = 1 → violations expected
- Configurations where W does not perform interference measurement
  → requires_K_joint = 0 → no violations expected

If the paper only reports aggregate violation (all configurations
together), record Condition 3 as INCONCLUSIVE for Proietti et al.
and state this explicitly in Section 8 (Open Items) of the paper.

---

## Target Paper 2: Bong et al. (2020)

**Full citation:**
Bong, K.W., Utreras-Alarcón, A., Ghafari, F., Liang, Y.C.,
Tischler, N., Cavalcanti, E.G., Pryde, G.J., Wiseman, H.M. (2020).
A strong no-go theorem on the Wigner's friend paradox.
Nature Physics 16, 1199-1205.
DOI: 10.1038/s41567-020-0990-x

**Access:** https://www.nature.com/articles/s41567-020-0990-x
Supplementary materials available at the same URL.

### Setup summary

Bell-type test of Local Friendliness (LF) assumptions.
Three assumptions tested jointly:
- No-Superdeterminism (NS)
- Locality (L)
- Absoluteness of Observed Events (AoE)

Result: at least one of NS, L, AoE must be false.
Reported violation of Local Friendliness inequalities.

### VVV-QMRF position on AoE

VVV-QMRF drops AoE via K_F ⊥_K K_W:
Observed events are not absolute across observers when
requires_K_joint = 1 and K_joint fails.

This is the primary connection between VVV-QMRF and Bong et al.
Do not state that Bong et al. directly prove AoE alone is violated
unless the source explicitly isolates AoE from NS and L. Treat AoE as
VVV-QMRF's registration-layer interpretation of the Local Friendliness
failure, not as a directly extracted experimental datum.

### What to extract from the paper

```
1. The specific Local Friendliness inequalities tested.
   Bong et al. derive new inequalities beyond Bell inequalities —
   extract their form and classical bounds.

2. For each experimental configuration:
   - Which of the three assumptions (NS, L, AoE) is under test?
   - Does the configuration require joint registration (W interference)?
   - What is the reported inequality value and violation magnitude?

3. Whether the violation pattern clusters in configurations where
   AoE is relevant under the VVV-QMRF registration-layer reading.

4. Whether the supplementary data provides per-configuration
   violation values, per-inequality-term values, or only aggregate
   statistics.
```

### Application table to fill

```
| Config ID | Assumption under test | W interference? | requires_K_joint | LF violation? | AoE relevance under VVV-QMRF? | Match? | Notes |
|-----------|-----------------------|----------------|-----------------|---------------|--------------------------------|--------|-------|
| B1        | ?                     | ?              | ?               | ?             | ?                              | ?      |       |
| B2        | ?                     | ?              | ?               | ?             | ?                              | ?      |       |
| ...       |                       |                |                 |               |                                |        |       |
```

### Expected outcome

VVV-QMRF predicts that Local Friendliness violations should be
relevant to AoE under the VVV-QMRF registration-layer reading when
requires_K_joint = 1 — specifically where W performs interference
measurement on F's lab, forcing a K_joint that fails.

The structural claim: AoE fails because K_F ⊥_K K_W, not because
of a physical property of the quantum state alone.

This is the asymmetric prediction relative to standard QM:
standard QM explains Local Friendliness violations via quantum correlations
alone. VVV-QMRF adds: the registration-layer interpretation of AoE
failure is the empirical signature of K-side incommensurability.

---

## Output Format for Each Paper

When the application is complete, produce a result document
with this structure:

```
# Condition 3 Result: [Paper name]

## Configuration List
[Table filled from above]

## Match Summary
Total configurations: N
Match = YES: n1 (n1/N)
Match = NO: n2 (n2/N)
Match = INCONCLUSIVE: n3 (n3/N)

## Conclusion
[One of three options — use exact wording:]

Option A (Consistent):
"The distribution of violations in [paper] is consistent with the
requires_K_joint = 1 prediction. Configurations where requires_K_joint = 1
show violations; configurations where requires_K_joint = 0 do not.
This is consistent with K_F ⊥_K K_W. Claim class remains C (conjecture)
pending further experimental tests."

Option B (Inconsistent):
"Configuration [ID] shows requires_K_joint = 1 but no violation [or vice versa].
This is inconsistent with the K_F ⊥_K K_W prediction.
Conditions A-D require revision. Specifically: [state which condition failed
and what revision is needed]."

Option C (Inconclusive):
"The published data does not provide per-configuration resolution sufficient
to test requires_K_joint. The aggregate violation is consistent with
VVV-QMRF but does not distinguish it from other frameworks.
Condition 3 is inconclusive for this paper. Stated as open item."
```

Do not write Option A if the data is inconclusive.
Do not write Option B without identifying the specific configuration
that falsifies the prediction.
Inconclusive is a valid scientific result. State it honestly.

---

## What a Successful Condition 3 Looks Like

Not acceptable:
> "Our framework is broadly consistent with Proietti et al."

Acceptable:
> "Applying requires_K_joint to the 6 configurations tested in
> Proietti et al., we find requires_K_joint = 1 in C1, C3, C5
> (W performs interference measurement) and requires_K_joint = 0
> in C2, C4, C6 (W does not). Violations appear in C1, C3, C5
> and not in C2, C4, C6. This is consistent with the K_F ⊥_K K_W
> prediction. The check for Bong et al. is pending."

The difference: the acceptable version names specific configurations,
states the predicate value for each, and checks it against data.
The unacceptable version is untestable prose.

---

## Honest Disclosure Rules

These rules are mandatory. Apply them without exception.

Rule 1: If per-configuration data is not available in the paper,
state Condition 3 as INCONCLUSIVE. Do not infer from aggregate data.
If only per-inequality-term or aggregate data is available, record
that granularity explicitly and do not assign configuration-level
YES/NO violation labels.

Rule 2: If any configuration produces Match = NO,
do not suppress it. State it as a falsification signal and
identify which of Conditions A-D requires revision.

Rule 3: If requires_K_joint is AMBIGUOUS for any configuration
(no Condition A-D clearly applies), record it as AMBIGUOUS
and explain why. Do not force a value.

Rule 4: Consistent result ≠ confirmed result.
Condition 3 can at best show the prediction is consistent
with existing data. Confirmation requires a purpose-designed
experiment. State this distinction in the paper.

Rule 5: Conditions A-D remain Class D proposed and sufficient-only.
Unmatched or ambiguous cases must be treated as open formalization
items, not repaired by prose or forced into requires_K_joint = 1.

---

## Paper Integration

When Condition 3 is complete, add results to the paper as follows:

```
Section 6: Experimental Connection

6.1 Proietti et al. (2019)
    [Configuration table]
    [One-paragraph result using Option A, B, or C wording]

6.2 Bong et al. (2020)
    [Configuration table]
    [One-paragraph result using Option A, B, or C wording]

6.3 Limitations
    "Per-configuration data resolution is limited by what is
    published. A purpose-designed experiment applying the
    requires_K_joint decision procedure to a controlled
    parameter sweep would provide a definitive test."
```

If both papers return INCONCLUSIVE, Section 6 still exists
and still has value: it shows the framework is compatible
with existing results and identifies what a definitive test
would require.

---

## After Condition 3 Is Complete

If Condition 3 returns at least one CONSISTENT result:
→ Paper is ready to submit to PhilSci Archive.
→ Label as Working Paper v2.0.
→ Include the falsifiable prediction sentence from E01 Section 11.6.

If Condition 3 returns INCONSISTENT for any configuration:
→ Do not suppress. Revise Conditions A-D in E01 Section 11.3.
→ Rerun the decision procedure with revised conditions.
→ Submit only after revised conditions produce consistent results
  or are explicitly flagged as requiring further work.

If both papers return INCONCLUSIVE:
→ Paper is still submittable.
→ Section 6 states: framework is compatible with existing data;
  definitive test requires purpose-designed experiment.
→ This is a weaker but still valid contribution.

---

## Execution Checklist

```
[ ] Download Proietti et al. (2019) full paper + supplementary
[ ] Extract measurement configuration list from Proietti et al.
[ ] Apply requires_K_joint decision procedure to each configuration
[ ] Fill Proietti application table
[ ] Write Condition 3 result for Proietti (Option A, B, or C)

[ ] Download Bong et al. (2020) full paper + supplementary
[ ] Extract measurement configuration list from Bong et al.
[ ] Apply requires_K_joint decision procedure to each configuration
[ ] Fill Bong application table
[ ] Write Condition 3 result for Bong (Option A, B, or C)

[ ] Write Section 6 of paper using both results
[ ] Add any new open items to Section 8 (Open Items)
[ ] Verify falsifiable prediction sentence is in abstract
[ ] Submit to PhilSci Archive
```

---

## Summary

Condition 3 is the final step before paper submission.
It does not require a new experiment.
It requires reading two published papers carefully and
applying a formal decision procedure to their configurations.

The output is one of three honest conclusions per paper:
consistent, inconsistent, or inconclusive.

Any of the three is acceptable in a working paper.
None of the three should be falsified, suppressed, or inflated.

The framework lives or dies on whether it can make contact
with real data. This is the step that finds out.

---

*Plan version: 1.0*
*Depends on: E01 Section 11.3 (requires_K_joint Conditions A-D)*
*Depends on: VVV-QMRF_Three_Conditions_Scientific_Validity.md*
*Next output: Condition_3_Result_Proietti_2019.md*
*Next output: Condition_3_Result_Bong_2020.md*
*Repository: https://github.com/AIhugART/VVV-QMRF-VietVunVut-Quantum-Measurement-Registration-Framework*
