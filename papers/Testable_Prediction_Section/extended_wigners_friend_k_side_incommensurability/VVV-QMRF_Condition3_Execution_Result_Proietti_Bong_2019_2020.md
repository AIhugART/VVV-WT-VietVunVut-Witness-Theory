Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# VVV-QMRF Condition 3 Execution Result
## Applying requires_K_joint to Proietti et al. (2019) and Bong et al. (2020)

**Document type:** Condition 3 execution result  
**Status:** Draft for verification  
**Depends on:** E01 Section 11.3 `requires_K_joint` predicate  
**Primary rule source:** `plan/vvv_qmrf_framework_e01_self_certifying_registration_postulate_v2.md`, Section 11.3  
**Execution plan source:** `plan/VVV-QMRF_Condition3_Execution_Plan.md`  
**Claim class:** C — existing-data compatibility check, not confirmation  
**Result classification:** Consistent at term-contribution / structural-threshold level  

---

## 1. Scope and Evidence Level

This document applies the E01 Section 11.3 `requires_K_joint` predicate to public summaries of Proietti et al. (2019) and Bong et al. (2020).

The evidence level is limited to an **existing-data compatibility check**. It is not a confirmation-level VVV-QMRF experiment, because the original experiments were not designed to isolate `requires_K_joint` as an independent variable.

The supported granularity is:

- Proietti et al. (2019): Bell-Wigner term-contribution level.
- Bong et al. (2020): setting-level structure plus `mu`-threshold behavior.

Therefore, this document may conclude structural consistency with the VVV-QMRF prediction `K_F \perp_K K_W`, but it must not claim that VVV-QMRF is confirmed.

---

## 2. Rule Source: `requires_K_joint` Conditions A-D

The rule source is E01 Section 11.3.

```text
requires_K_joint(F, W, M_F, M_W) = 1
  iff a single joint registration space K_joint is structurally
  required to contain both k_F and k_W as jointly valid entries.

requires_K_joint(F, W, M_F, M_W) = 0
  iff K_F and K_W can remain independent K-side spaces without
  any inference, comparison, or joint validity check between them.
```

### 2.1 Sufficient conditions for `requires_K_joint = 1`

```text
Condition A (Wigner interference):
  W performs an interference measurement on the lab containing F+S.
  M_W registers a superposition description of F+S.
  M_F registers a definite outcome o_F of the same system S.
  Both M_F and M_W claim K-side validity on the same physical event.
  -> requires_K_joint = 1

Condition B (Direct comparison):
  F and W directly compare their registration records
  and a logical contradiction is detectable.
  -> requires_K_joint = 1
```

### 2.2 Sufficient conditions for `requires_K_joint = 0`

```text
Condition C (No interference, no comparison):
  W does not perform interference measurement on F's lab.
  F and W do not compare registration records.
  K_F and K_W remain causally isolated.
  -> requires_K_joint = 0

Condition D (Separable state, no entanglement):
  The shared quantum state |psi> is separable.
  M_F and M_W act on non-overlapping subsystems.
  No joint validity check is structurally required.
  -> requires_K_joint = 0
```

### 2.3 Application guardrails

- Do not modify Conditions A-D during application.
- Do not infer Condition D from "nearly separable" or weakly entangled states unless separability is explicitly verified.
- Treat `requires_K_joint = 1` as a structural condition for possible K-side incommensurability, not as a guarantee that every state regime will violate an inequality.
- Treat existing experimental data as compatibility evidence, not confirmation.

---

## 3. Source Inventory

| Source ID | File | Paper | Role | Key data available |
|---|---|---|---|---|
| P2019-S1 | `supplementary_public_documents/Proietti_et_al_2019/claude_2_proietti2019_wigner_friend_full.md` | Proietti et al. (2019) | Public summary / supplementary extraction | A0/B0, A1/B1, expectation values, `S_exp`, alternative observables |
| B2020-S1 | `supplementary_public_documents/Bong_et_al_2020/wigner_friend_no_go_theorem.md` | Bong et al. (2020) | Public summary / supplementary extraction | LF assumptions, inequality classes, `mu`-level results, x=1 versus x=2,3 implementation |
| B2020-S2 | `supplementary_public_documents/Bong_et_al_2020/wigner_friend_no_go_theorem1.md` | Bong et al. (2020) | Public summary / supplementary extraction | EWFS setup, LF model, settings, measurement implementation, `mu`-level results |

Note: B2020-S1 and B2020-S2 are two public-document views of the same Bong et al. experiment. They are not treated as separate experiments.

---

## 4. Proietti et al. (2019)

### 4.1 Extracted term data

The public document describes an extended Wigner's friend test with four observers and a six-photon optical implementation.

Relevant observable definitions:

```text
A0 = B0 = 1 x (|v><v| - |h><h|)
```

`A0` and `B0` read the friends' memory records.

```text
A1 = B1 = |Psi+><Psi+| - |Psi-><Psi-|
```

`A1` and `B1` are Wigner-type joint measurements implemented through nonclassical interference on a 50/50 beam splitter.

The alternative-observable supplementary result gives:

| Term | Experimental value | Role in Bell-Wigner expression | Source note |
|---|---:|---|---|
| `<A1B1>` | +0.571 | Added | Wigner-type joint measurement on both sides |
| `<A1B0>` | +0.577 | Added | Alice Wigner-type side, Bob friend-record side |
| `<A0B1>` | +0.573 | Added | Alice friend-record side, Bob Wigner-type side |
| `<A0B0>` | +0.662 | Subtracted | Friend-record readout on both sides |

The reported Bell-Wigner value is:

```text
S = <A1B1> + <A1B0> + <A0B1> - <A0B0>
S = 0.571 + 0.577 + 0.573 - 0.662
S = 2.407
```

This matches the public-document value `S_exp = 2.407 +/- 0.073`, violating the observer-independence bound `S <= 2` by more than five standard deviations.

### 4.2 `requires_K_joint` mapping

| Term | Config | W interference? | Triggering condition | `requires_K_joint` | Experimental value | Role in `S` | Note |
|---|---|---|---|---:|---:|---|---|
| `<A1B1>` | `(A1, B1)` | Both Alice and Bob | Condition A | 1 | +0.571 | Positive contribution | Both sides perform Wigner-type joint measurement |
| `<A1B0>` | `(A1, B0)` | Alice only | Condition A | 1 | +0.577 | Positive contribution | Alice-side Wigner-type joint measurement |
| `<A0B1>` | `(A0, B1)` | Bob only | Condition A | 1 | +0.573 | Positive contribution | Bob-side Wigner-type joint measurement |
| `<A0B0>` | `(A0, B0)` | None | Condition C | 0 | +0.662 | Subtracted term | Friend-record readout; no Wigner interference |

### 4.3 Verification

- The three terms involving Wigner-type joint measurement activate Condition A.
- These three Condition A terms contribute positively to the violated Bell-Wigner expression.
- The no-interference friend-record term activates Condition C and is the subtracted term.
- The reconstructed value `S = 2.407` matches the public supplementary value.

### 4.4 Result for Proietti et al. (2019)

**Result:** Consistent at Bell-Wigner term-contribution level.

The Proietti alternative-observable data are consistent with the `requires_K_joint` prediction at the Bell-Wigner term-contribution level. The three terms involving Wigner-type joint measurement activate Condition A and contribute positively to the violated expression. The non-interference friend-record term activates Condition C and appears as the subtracted term. The resulting value, `S = 2.407 +/- 0.073`, violates the observer-independence bound `S <= 2`.

This supports structural consistency with `K_F \perp_K K_W`, while the claim class remains C because the result is an existing-data compatibility check, not a purpose-designed VVV-QMRF experiment.

---

## 5. Bong et al. (2020)

### 5.1 Extracted setting structure

The public documents describe an Extended Wigner's Friend Scenario with:

- Friends: Charlie and Debbie.
- Superobservers: Alice and Bob.
- Friend outcomes: `c` and `d`.
- Superobserver settings: `x` and `y`.
- Superobserver outcomes: `a` and `b`.

The key setting distinction is:

| Setting | Implementation | Registration-layer reading |
|---|---|---|
| `x=1` / `y=1` | Ask friend; mirror inserted; path revealed; `a=c` or `b=d` | Friend-record readout |
| `x=2,3` / `y=2,3` | Superobserver measurement; mirror removed; interferometer closed; friend measurement reversed | Wigner-type interference / reversal operation |

The tested state family is:

```text
rho_mu = mu |Phi-><Phi-| + (1-mu)/2 (|HV><HV| + |VH><VH|)
```

The public result summary gives:

| `mu` regime | Reported result |
|---|---|
| Low `mu` | No inequalities violated |
| `mu = 0.80, 0.81` | Bell non-LF violated, but no LF inequalities violated |
| `mu approx 0.87` | First LF inequality violation, Semi-Brukner |
| High `mu` | All inequality categories violated, including Genuine LF |

### 5.2 `requires_K_joint` structural mapping

| Setting pair | Alice side | Bob side | W interference? | Triggering condition | `requires_K_joint` | VVV-QMRF prediction | Data relation |
|---|---|---|---|---|---:|---|---|
| `x=1, y=1` | Ask Charlie | Ask Debbie | None | Condition C | 0 | LF consistency expected | Friend-read anchor; `a=c`, `b=d` |
| `x=1, y=2/3` | Ask Charlie | Bob superobserver | Bob side | Condition A | 1 | LF violation possible if state supports K_joint failure | Mixed LF terms |
| `x=2/3, y=1` | Alice superobserver | Ask Debbie | Alice side | Condition A | 1 | LF violation possible if state supports K_joint failure | Mixed LF terms |
| `x=2/3, y=2/3` | Alice superobserver | Bob superobserver | Both sides | Condition A | 1 | Strongest K-side incommensurability regime | Genuine LF / high-`mu` violation regime |

### 5.3 `mu`-threshold mapping

| `mu` regime | Reported result | `requires_K_joint` reading | Note |
|---|---|---|---|
| Low `mu` | No inequalities violated | Condition A may be structurally present in `x=2/3` settings, but empirical LF violation is absent | Consistent if the state is too weakly entangled or too mixed; do not invoke Condition D unless separability is proven |
| `mu = 0.80, 0.81` | Bell non-LF violated, LF not violated | Bell violation alone does not imply LF-level K-side failure | Consistent with LF being stronger than Bell |
| `mu approx 0.87` | First LF violation, Semi-Brukner | Mixed friend/superobserver settings become empirically relevant | Consistent with threshold behavior |
| High `mu` | All inequality categories violated, including Genuine LF | `x=2/3, y=2/3` Condition A regime strongly active | Consistent with strongest K_joint failure regime |

### 5.4 Correction on Condition D

Condition D should not be invoked merely because a state is near-separable, weakly entangled, or mixed. Condition D requires explicit separability, non-overlapping subsystems, and absence of a structurally required joint validity check.

Therefore, for low-`mu` Bong regimes, the correct classification is:

```text
Condition A structurally applies when superobserver interference/reversal is present.
Empirical LF violation may be absent because the state regime is too weakly entangled or too mixed.
Condition D remains a candidate only if separability is explicitly verified.
```

### 5.5 Result for Bong et al. (2020)

**Result:** Consistent at structural setting-level and `mu`-threshold level.

Bong et al. are consistent with the VVV-QMRF prediction at the structural setting-level and threshold-regime level. Settings `x=1` and `y=1` correspond to friend-record readout and support `requires_K_joint = 0` under Condition C when no Wigner interference or direct contradiction-producing comparison is present. Settings `x=2,3` or `y=2,3` involve superobserver interference/reversal operations and activate Condition A, giving `requires_K_joint = 1`.

The reported `mu`-threshold behavior is also consistent with the VVV-QMRF reading: Bell non-LF violations can occur while LF inequalities remain unviolated, and LF violations appear only when the state and measurement regime are strong enough. At high `mu`, all inequality categories are violated, including Genuine LF, matching the strongest Condition A regime where both sides perform superobserver measurements.

This supports structural consistency with `K_F \perp_K K_W`, while the claim class remains C because the analysis uses existing experiments rather than a purpose-designed VVV-QMRF test.

---

## 6. Cross-Paper Summary

| Paper | Supported test level | Main mapping | Empirical pattern | Result |
|---|---|---|---|---|
| Proietti et al. (2019) | Bell-Wigner term-contribution level | `A1`/`B1` terms activate Condition A; `A0B0` activates Condition C | Condition A terms contribute positively; Condition C term is subtracted; `S = 2.407 > 2` | Consistent |
| Bong et al. (2020) | Setting-level and `mu`-threshold level | `x=1`/`y=1` friend-read settings map to Condition C; `x=2,3`/`y=2,3` superobserver settings map to Condition A | LF violations emerge only above threshold; high `mu` violates all categories including Genuine LF | Consistent |

Overall, the available public data are consistent with the VVV-QMRF prediction that K-side incommensurability becomes empirically relevant when Wigner-type interference/reversal operations structurally require `K_joint` and no jointly valid `K_joint` can be maintained.

---

## 7. Scientific Conclusion

Applying the `requires_K_joint` predicate to the available public Proietti and Bong data yields a structurally consistent and asymmetric pattern.

The key asymmetry is that Bell non-LF violation can appear before LF-level Wigner-friend violation. In Bong et al. (2020), at `mu = 0.80, 0.81`, the public summaries report Bell non-LF violation while LF inequalities remain unviolated. This is the central discriminating point: ordinary Bell-type nonclassicality and LF-level Wigner-friend inconsistency occupy different regimes. A decoherence-only framework does not distinguish these two regimes at the registration-layer level, because it has no predicate equivalent to `requires_K_joint` for separating Bell non-LF violation from LF-level joint-validity failure.

In Proietti et al. (2019), the Bell-Wigner terms involving Wigner-type joint measurements activate Condition A and contribute positively to the violated expression, while the no-interference friend-record term activates Condition C and appears as the subtracted term. The reconstructed value `S = 2.407` matches the reported supplementary result.

In Bong et al. (2020), friend-read settings map to `requires_K_joint = 0`, while superobserver interference/reversal settings map to `requires_K_joint = 1`. LF violation becomes empirically visible only when the state and measurement regime are strong enough to expose failure of `K_joint`, with higher-`mu` regimes reaching Semi-Brukner, Brukner, or Genuine LF violation classes.

This result is consistent with the `K_F \perp_K K_W` prediction. It does not confirm VVV-QMRF, because the analysis uses existing experiments not designed specifically to isolate `requires_K_joint`. Claim class remains C pending a purpose-designed test.

---

## 8. Limitations

| Limitation | Cause | Required fix |
|---|---|---|
| Proietti result is term-contribution level, not a standalone per-configuration violation proof | Bell-Wigner violation is an aggregate expression over four terms | Reconstruct raw count-level data or design a test isolating each `requires_K_joint` class |
| Bong result is setting-level and threshold-level, not direct per-setting-pair violation labeling | Public results are reported by `mu` regime and inequality class | Map each LF facet term to setting-pair contributions and raw probabilities |
| Condition C requires causal-isolation verification | No interference alone is not always sufficient for Condition C | Verify absence of direct comparison and joint validity check in each friend-read setting |
| Condition D is not established for low-`mu` regimes | Weak entanglement or mixedness is not equivalent to separability | Perform explicit separability analysis for each `rho_mu` regime |
| AOE relevance is interpretive | LF violation rejects at least one of AOE, NSD, or L, not AOE alone | State VVV-QMRF's registration-layer reading only under retained NSD and L |

---

## 9. Open Items

| Open item | Status | Needed for |
|---|---|---|
| Raw count-level reconstruction for Proietti alternative observables | Not done | Stronger term-level verification |
| LF facet-to-setting-pair contribution table for Bong | Not done | Stronger per-setting-pair verification |
| Explicit separability check for Bong `rho_mu` regimes | Not done | Valid Condition D application |
| Purpose-designed VVV-QMRF experiment varying `requires_K_joint` directly | Not done | Confirmation-level test |
| Formal refinement of `requires_K_joint` from sufficient-only to necessary-and-sufficient | Open in E01 Section 11.5 | Stronger prediction classifier |

---

## 10. Verification Checklist

| Check | Status | Note |
|---|---|---|
| Author metadata present | Pass | Required because file is outside `documents/published_documents/` |
| Source paths listed | Pass | Public source inventory included |
| E01 Section 11.3 used as rule source | Pass | Conditions A-D preserved |
| Proietti `S = 2.407` reconstructed | Pass | `0.571 + 0.577 + 0.573 - 0.662 = 2.407` |
| Condition A applied to Wigner-type joint terms | Pass | `A1`/`B1` terms mapped to `requires_K_joint = 1` |
| Condition C applied to no-interference friend-read term | Pass with caveat | Requires no direct comparison / joint validity check |
| Bong `x=1` / `y=1` mapped to friend-read settings | Pass | Condition C candidate when no comparison contradiction is present |
| Bong `x=2,3` / `y=2,3` mapped to superobserver interference | Pass | Condition A |
| Condition D not overused | Pass | Low-`mu` regimes marked as state-regime limitation, not Condition D proof |
| No claim that Bong proves AOE alone false | Pass | AOE reading stated under retained NSD and L |
| No claim that VVV-QMRF is confirmed | Pass | Claim class remains C |

---

## 11. Final Assessment

The available public Proietti and Bong documents are sufficient to apply `requires_K_joint` now, provided the result is stated at the correct evidence level.

- Proietti et al. (2019): **consistent at Bell-Wigner term-contribution level**.
- Bong et al. (2020): **consistent at structural setting-level and `mu`-threshold level**.
- Overall Condition 3 status: **satisfied as an existing-data compatibility check**, not as final confirmation.

Final claim:

```text
Existing public data from Proietti et al. (2019) and Bong et al. (2020)
are consistent with the VVV-QMRF prediction that Wigner-type
interference/reversal settings activate requires_K_joint = 1 and expose
K-side incommensurability, while friend-record readout settings support
requires_K_joint = 0 when no joint validity check is structurally required.
This prediction is not trivially true for every framework, because it
separates ordinary Bell non-LF violation from LF-level Wigner-friend
violation, as illustrated by mu = 0.80, 0.81 where Bell non-LF violation
is reported while LF inequalities remain unviolated.
```
