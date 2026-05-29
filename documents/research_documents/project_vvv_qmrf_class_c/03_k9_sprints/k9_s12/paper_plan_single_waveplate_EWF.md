# Paper Writing Plan
## "A Single-Waveplate Test of Outcome-Dependent Quantum Registration in Extended Wigner's Friend Scenarios"

**Status:** Pre-writing plan — LLM-friendly, section-by-section  
**Target venue:** arXiv quant-ph (preprint first), then Physical Review Letters or New Journal of Physics  
**Target length:** 8–12 pages main text + supplemental  
**Framework:** VVV-QMRF / K9 analysis chain (K9-S11 through K9-S12)  
**Date:** 2026-05-23

---

## 0. Document Conventions (LLM Instructions)

- All section prompts below are written as **direct instructions** to an LLM.
- Each section block contains: PURPOSE, INPUTS, CONTENT REQUIREMENTS, OUTPUT FORMAT, and WRITING STYLE.
- Mathematical notation uses LaTeX inline (`$...$`) and display (`$$...$$`) syntax.
- All tables use Markdown pipe syntax.
- Figures are described as `[FIGURE N: description]` placeholders — actual figures generated separately.
- Cross-references use `§` prefix: `§2`, `§3.1`, etc.
- Citations use bracket notation: `[Bong2020]`, `[Proietti2019]`, `[Hardy1992]`.

---

## 1. Paper Metadata

```
Title:    A Single-Waveplate Test of Outcome-Dependent Quantum Registration
          in Extended Wigner's Friend Scenarios

Authors:  [Author list]

Abstract: [Written last — see §10]

Keywords: Extended Wigner's Friend, Bell inequality, quantum measurement,
          outcome-dependent registration, experimental proposal,
          Genuine LF inequality, K-space framework

PACS/MSC: 03.65.Ta, 03.65.Ud, 42.50.Xa
```

---

## 2. Section Map

| # | Section Title | Maps From | Word Target |
|---|--------------|-----------|-------------|
| 1 | Introduction | Background + motivation | 600–800 w |
| 2 | Theoretical Background | K9_E definition, LF inequality | 700–900 w |
| 3 | The Equatorial Cancellation Theorem | K9-S11 core result | 500–700 w |
| 4 | Experimental Protocol | Phần 5 — hardware description | 500–700 w |
| 5 | Predictions and Expected Results | Phần 4 — full prediction tables | 600–800 w |
| 6 | Statistical Analysis | Phần 3 — Monte Carlo, p-value | 500–600 w |
| 7 | Robustness Analysis | Phần 1 — sensitivity analysis | 600–800 w |
| 8 | Loophole Analysis | Phần 2 — loophole discussion | 400–600 w |
| 9 | Discussion | Implications, limitations | 400–600 w |
| 10 | Conclusion | Summary + next steps | 200–300 w |
| — | Abstract | Written last | 150–200 w |
| — | Supplemental | Full derivations, extended tables | unbounded |

---

## 3. Section-by-Section Writing Plan

---

### §1 — Introduction

**PURPOSE:**  
Motivate the paper. Establish why Extended Wigner's Friend (EWF) experiments matter, what they have tested so far, and what they have missed. End with a clear statement of the paper's contribution.

**INPUTS:**  
- Bong et al. 2020 [Bong2020]: original EWF experiment, Genuine LF inequality violation  
- Proietti et al. 2019 [Proietti2019]: first optical EWF experiment  
- Wigner 1961 [Wigner1961]: original Wigner's Friend thought experiment  
- Frauchiger & Renner 2018 [FR2018]: logical contradiction in EWF scenarios  
- K9 analysis chain: equatorial cancellation theorem (K9-S11), modified protocol (K9-S12)

**CONTENT REQUIREMENTS:**  
1. Open with the Wigner's Friend paradox in 2–3 sentences — no jargon.  
2. Explain what EWF experiments test (LF inequalities, absoluteness of observed events).  
3. State what Bong 2020 achieved and why it was a milestone.  
4. Introduce the gap: all existing EWF experiments use equatorial superobserver measurements → outcome-dependent registration is invisible by construction.  
5. State the paper's contribution in one paragraph: we prove this geometrically, identify the fix (one quarter-wave plate, θ = 31°), and provide full experimental predictions.  
6. End with a one-sentence roadmap of the paper structure.

**OUTPUT FORMAT:** Flowing prose, no subsections, no bullet points.  
**WRITING STYLE:** Physical Review Letters style — direct, no hedging, every sentence earns its place.

---

### §2 — Theoretical Background

**PURPOSE:**  
Define all quantities needed to understand the paper. Reader should finish this section knowing exactly what K9_E, Genuine LF, and f⊥ are, without needing external references.

**INPUTS:**  
- Bong et al. 2020 [Bong2020]: LF inequality definition, correlator notation  
- VVV-QMRF framework: K-space registration, K9_E definition  
- K9-S11d: f⊥ definition and role in K9_E

**CONTENT REQUIREMENTS:**  

**§2.1 — Extended Wigner's Friend Setup**  
- Describe the physical setup: Friend (F), Lab (L), Superobserver (S), entangled source.  
- Define the relevant measurements: A₁, A₂ (Superobserver Alice side), B₁, B₂, B₃ (Superobserver Bob side).  
- State clearly what "equatorial measurement" means on the Bloch sphere.  
- Include: [FIGURE 1: EWF setup schematic — two labs, two superobservers, entangled source]

**§2.2 — Genuine Local Friendliness (LF) Inequality**  
- State the inequality: Gen LF 1 ≤ 0 under local friendliness assumptions.  
- Define each of the 11 correlator terms with their coefficients.  
- State what a violation (Gen LF 1 > 0) implies physically.

**§2.3 — Outcome-Dependent Registration: K9_E**  
- Define f⊥(o, H) = probability that superobserver outcome is +1 given Friend outcome o and hidden variable H.  
- Define K9_E as the difference δ⟨A₁B₂⟩ = ⟨A₁B₂⟩_QM − ⟨A₁B₂⟩_K9.  
- Explain: if f⊥ is constant across Friend outcomes, K9_E = 0 and the quantity is untestable.

**OUTPUT FORMAT:** Prose with equations. Use subsections §2.1, §2.2, §2.3.  
**WRITING STYLE:** Pedagogical but concise. Define every symbol at first use.

---

### §3 — The Equatorial Cancellation Theorem

**PURPOSE:**  
Prove the central theoretical result of the paper. This is the key contribution that explains why all prior experiments were blind to K9_E.

**INPUTS:**  
- K9-S11: algebraic proof  
- K9-S11b: Proietti geometry check (confirms universality)  
- Sympy verification (from universal_theorem_lf_check.py)

**CONTENT REQUIREMENTS:**  

**§3.1 — Statement**  
State the theorem formally:

> **Theorem (Equatorial Cancellation).**  
> For any Extended Wigner's Friend experiment in which the Superobserver measures in the equatorial plane of the Bloch sphere (polar angle θ = π/2), the outcome-overlap function satisfies:  
> $$f_\perp(+1, H) - f_\perp(-1, H) = -\cos\theta = 0$$  
> independently of the azimuthal angle φ and of the Friend's outcome. Consequently, K9_E = 0 for all such experiments.

**§3.2 — Proof**  
- Start from the definition of f⊥ in terms of Born rule overlaps.  
- Show that the difference f⊥(+1,H) − f⊥(−1,H) = −cos(θ).  
- Show this vanishes iff θ = π/2.  
- Show azimuthal angle φ drops out of the expression.  
- Conclude: outcome-dependence is geometrically invisible at the equator.

**§3.3 — Corollary: All Existing EWF Experiments Are Blind to K9_E**  
- Apply theorem to Bong 2020: superobserver angles are all equatorial → K9_E = 0.  
- Apply theorem to Proietti 2019: BSM projected onto Bell states also gives constant 50/50 overlap for any Friend outcome → K9_E = 0.  
- State: this is not a limitation of those experiments' goals — they were not designed to test K9_E. But it means K9_E has never been tested.

**OUTPUT FORMAT:** Theorem/Proof block, then prose corollary.  
**WRITING STYLE:** Mathematical precision. Every step of the proof explicit.

---

### §4 — Experimental Protocol

**PURPOSE:**  
Describe exactly what a laboratory group needs to do to implement the modified experiment. Sufficient detail to implement without further correspondence.

**INPUTS:**  
- K9-S12: hardware change (one QWP), optimized angles  
- Bong et al. 2020 supplemental: original apparatus description  
- K9-S11d: α = 31° derivation

**CONTENT REQUIREMENTS:**  

**§4.1 — Base Apparatus**  
- State that the protocol is a minimal modification of Bong et al. 2020.  
- Describe the base setup in one paragraph: entangled photon source (SPDC, 810 nm), beam splitters, waveplates, single-photon detectors, coincidence logic.  
- Reference [Bong2020] supplemental for full base apparatus details.

**§4.2 — Single Hardware Modification**  
- Specify: re-insert one quarter-wave plate (QWP) into the superobserver measurement path.  
- State exact position: in the polarization analysis path of Superobserver Alice, before the polarizing beam splitter.  
- State fast-axis orientation: adjusted to realize an effective polar angle θ = 31° on the Bloch sphere.  
- State wavelength requirement: QWP must be specified for λ = 810 nm (or the source wavelength of the base apparatus).  
- State retardance tolerance: δ_ret ≤ ±2 nm to keep effective θ within ±0.5° of 31°.  
- Include: [FIGURE 2: Modified optical path — original Bong schematic with QWP insertion point marked]

**§4.3 — Measurement Settings**  
Provide the full angle table:

| Parameter | Standard Bong | Modified (K9-S12) |
|-----------|--------------|-------------------|
| Superobserver polar angle θ | 90° (equatorial) | **31°** |
| Azimuthal φ₁ | — | — |
| Azimuthal φ₂ | 0° | **112°** |
| Azimuthal φ₃ | 118° | **217°** |
| Analyzer angle β | 175° | **20°** |
| Visibility μ (required) | — | ≥ 0.95 |
| Total coincidences N | 91,000 | **91,000** |

**§4.4 — Calibration Procedure**  
- Describe how to verify that θ = 31° has been achieved: measure |⟨σ_z⟩| = cos(31°) ≈ 0.857 on a known state; confirm to within ±0.01.  
- Describe alignment verification for each azimuthal angle: use known two-photon state and check single-photon count rates match predictions to within 2%.

**OUTPUT FORMAT:** Prose with one table and two figures.  
**WRITING STYLE:** Technical instruction manual style. Unambiguous. Imperative verbs where appropriate ("insert", "set", "verify").

---

### §5 — Predictions and Expected Results

**PURPOSE:**  
State all quantitative predictions so that after the experiment, there is no ambiguity about what the data mean.

**INPUTS:**  
- K9-S12: Gen LF 1 = +0.089 (8.6σ), δ⟨A₁B₂⟩ = −0.036 (20.8σ)  
- K9-S11d: full correlator table at α = 31°  
- Standard quantum mechanics predictions for all 9 Bong correlators at modified angles

**CONTENT REQUIREMENTS:**  

**§5.1 — Quantum Mechanical Predictions**  
Provide a complete table of all 9 two-photon correlators ⟨AᵢBⱼ⟩ at the modified angles. Include:
- Value under standard QM
- Value under K9 theory (where different)
- Difference δ⟨AᵢBⱼ⟩

**§5.2 — Primary Test Quantities**  
State the two primary observables:

| Observable | QM prediction | K9 prediction | Significance (N=91,000) |
|-----------|--------------|---------------|------------------------|
| Gen LF 1 | +0.089 | ≤ 0 | **8.6σ** above LF bound |
| δ⟨A₁B₂⟩ | −0.036 | 0 | **20.8σ** |

**§5.3 — Decision Criteria**  
State explicitly:
- If Gen LF 1 > 0 with significance ≥ 5σ: Genuine LF violated → incompatible with local friendliness.  
- If δ⟨A₁B₂⟩ ≠ 0 with significance ≥ 5σ: K9_E ≠ 0 → outcome-dependent registration is real.  
- If both: joint confirmation of both effects.  
- If neither: null result → either θ = 31° is not realized, or both effects are absent. Check calibration first.  
- If Gen LF 1 > 0 but δ⟨A₁B₂⟩ ≈ 0: LF violation confirmed but K9_E absent → standard EWF result without registration dependence.

**§5.4 — Comparison With Standard Bong**  
One-paragraph comparison: what changes and what stays the same relative to Bong 2020.

**OUTPUT FORMAT:** Prose + two tables + decision tree (can be text-formatted).  
**WRITING STYLE:** Precise. Every claim has a number attached.

---

### §6 — Statistical Analysis

**PURPOSE:**  
Justify the statistical claims. Demonstrate that N = 91,000 is sufficient, that the σ values are robust, and that the analysis method is standard.

**INPUTS:**  
- K9-S11d: FOM = min(n_σ_LF, n_σ_K9E) definition and calculation  
- statistical_significance.py: computation method  
- Standard photon-counting statistics (Poisson)

**CONTENT REQUIREMENTS:**  

**§6.1 — Error Model**  
- State that photon coincidence counts follow Poisson statistics.  
- Define σ for each correlator: σ(⟨AᵢBⱼ⟩) = 1/√N for N coincidences per setting.  
- State error propagation rule for Gen LF 1 (11-term sum with coefficients up to ±2): σ²(Gen LF 1) = Σᵢ cᵢ² σᵢ².  
- Compute σ(Gen LF 1) = √20 × (1/√N) at equal counts per setting.

**§6.2 — Sample Size Justification**  
- State N = 91,000 total coincidences (matching Bong 2020 for direct comparability).  
- Perform power analysis: with effect size Gen LF 1 = 0.089, σ per trial as above, compute minimum N for 5σ detection. Show N = 91,000 gives 8.6σ >> 5σ.  
- Conclude: experiment is not statistics-limited.

**§6.3 — Monte Carlo Validation**  
- Describe simulation: 10,000 independent runs of N = 91,000 simulated coincidences, Poisson noise added to each correlator.  
- Report: mean Gen LF 1 from simulation, standard deviation, fraction of runs achieving > 5σ.  
- Report: mean δ⟨A₁B₂⟩ from simulation, standard deviation, fraction of runs achieving > 5σ.  
- Include: [FIGURE 3: Histogram of Gen LF 1 values across 10,000 Monte Carlo runs, with 0 (LF bound) and +0.089 (QM prediction) marked]

**§6.4 — Figure of Merit**  
- Define FOM = min(n_σ_LF, n_σ_K9E).  
- Justify: FOM ensures both quantities are simultaneously significant, not just one.  
- State FOM = 8.6 for the modified protocol, compared to FOM = 0 for the standard Bong protocol.

**OUTPUT FORMAT:** Prose with equations and one figure.  
**WRITING STYLE:** Methods section style — reproducible, every parameter stated.

---

### §7 — Robustness Analysis

**PURPOSE:**  
Show that the predictions survive realistic experimental imperfections. Give the experimentalist a map of the parameter space.

**INPUTS:**  
- K9-S12: predictions at ideal conditions (μ = 0.95, η = 1.0, θ_exact = 31°)  
- Bong 2020: achievable μ ≈ 0.92, achievable η ≈ 0.87 (from their apparatus specs)

**CONTENT REQUIREMENTS:**  

**§7.1 — State Visibility Degradation**  
- Scan μ from 0.80 to 0.99 in steps of 0.01.  
- For each μ, compute Gen LF 1(μ) and n_σ_LF(μ), and δ⟨A₁B₂⟩(μ) and n_σ_K9E(μ).  
- Find μ_min such that FOM ≥ 5σ (the detection threshold).  
- Report: at μ = 0.92 (Bong achievable), FOM = [computed value].  
- Include: [FIGURE 4: FOM vs μ plot, with horizontal dashed line at 5σ and vertical dashed line at μ = 0.92]

**§7.2 — Detector Efficiency**  
- Scan η from 0.70 to 1.00.  
- State that detection loophole requires η > η_crit (compute η_crit for this specific inequality).  
- Show FOM vs η.  
- Report η_min for FOM ≥ 5σ.

**§7.3 — Angular Misalignment**  
- Scan θ_actual = 31° ± Δ for Δ ∈ {0.5°, 1°, 2°, 3°, 5°}.  
- Compute FOM at each Δ.  
- State the alignment tolerance: the maximum Δ that still gives FOM ≥ 5σ.  
- Repeat for azimuthal angles φ₂, φ₃, β: ±1° perturbation each.  
- Report which angle is most sensitive (bottleneck for calibration).

**§7.4 — Joint Parameter Scan**  
- Produce a 2D heatmap: x-axis = μ, y-axis = η, color = FOM.  
- Mark the Bong 2020 operating point on the heatmap.  
- Mark the 5σ contour.  
- Include: [FIGURE 5: 2D heatmap FOM(μ, η) with 5σ contour and Bong 2020 operating point marked]

**§7.5 — Summary Table**

| Parameter | Ideal | Bong achievable | FOM at achievable | 5σ threshold |
|-----------|-------|-----------------|-------------------|--------------|
| μ | 0.95 | 0.92 | [value] | μ ≥ [value] |
| η | 1.00 | 0.87 | [value] | η ≥ [value] |
| Δθ | 0° | ±1° | [value] | Δθ ≤ [value] |

**OUTPUT FORMAT:** Prose + two figures + one summary table.  
**WRITING STYLE:** Engineering tolerance style. Each result stated as "if X then Y".

---

### §8 — Loophole Analysis

**PURPOSE:**  
Address the standard objections that any Bell-type experiment must face. State clearly which loopholes are closed, which remain open, and why the open ones are acceptable.

**INPUTS:**  
- Bong 2020: their loophole status  
- Bell 1964, Aspect 1982, Giustina 2015 (detection loophole): standard references  
- Brunner et al. 2014 [Brunner2014]: loophole review

**CONTENT REQUIREMENTS:**  

**§8.1 — Locality Loophole**  
- State: the modified protocol makes no changes to the spatial separation or timing of measurements.  
- Therefore: locality loophole status is identical to Bong 2020 — [open/closed, state which and why].  
- If open: state why this is acceptable for the purpose of this experiment (the goal is to test K9_E and LF, not to close locality loophole).

**§8.2 — Detection Loophole**  
- State the η_crit computed in §7.2.  
- Compare to Bong 2020 achievable η.  
- State: if η < η_crit, the detection loophole is open, and the result is conditional on the fair-sampling assumption.  
- State explicitly whether fair-sampling is assumed and justify.

**§8.3 — Freedom of Choice Loophole**  
- State: measurement settings (angles) are chosen by [random number generator type, same as Bong 2020].  
- State: no change from Bong 2020 in this respect.

**§8.4 — Superobserver Assumption (EWF-Specific)**  
- This is the loophole specific to EWF experiments, not Bell tests generally.  
- The Superobserver must be able to perform a coherent measurement on the entire Friend+Lab system.  
- In the optical implementation: "Friend" is a beam path, not a conscious observer. The coherent measurement is a standard interferometric operation.  
- State: this assumption is fully satisfied in the optical implementation. Limitations arise only when the "Friend" is a macroscopic system.

**§8.5 — Loophole Summary Table**

| Loophole | Status | Condition |
|----------|--------|-----------|
| Locality | Same as Bong 2020 | [open/closed] |
| Detection | Conditional | η ≥ η_crit = [value] |
| Freedom of choice | Same as Bong 2020 | [open/closed] |
| Superobserver assumption | Satisfied | Optical implementation only |

**OUTPUT FORMAT:** Subsections with one summary table.  
**WRITING STYLE:** Honest and precise. Do not claim more than is proven.

---

### §9 — Discussion

**PURPOSE:**  
Interpret the results. Connect to broader physics. State limitations. Suggest follow-up.

**CONTENT REQUIREMENTS:**  

**§9.1 — What a Positive Result Would Mean**  
- If Gen LF 1 > 0 at 5σ: local friendliness is violated, consistent with Bong 2020 but now with a modified geometry confirming the result is not angle-specific.  
- If δ⟨A₁B₂⟩ ≠ 0 at 5σ: first experimental evidence that the Friend's outcome influences superobserver correlations in a way not predicted by standard QM marginalization. Interpret in terms of the K-space registration framework.  
- Discuss: does this conflict with standard QM? (Answer: depends on interpretation — the VVV-QMRF framework is an extension, not a contradiction.)

**§9.2 — What a Null Result Would Mean**  
- Both quantities consistent with 0: either apparatus does not achieve required μ or η, or K9_E is genuinely absent at this geometry.  
- Distinguish: a calibration failure (θ ≠ 31° in practice) from a genuine null. The calibration procedure in §4.4 should disambiguate.

**§9.3 — Relation to Interpretations of Quantum Mechanics**  
- Brief discussion: which QM interpretations are consistent with a positive result, which are challenged.  
- Copenhagen: no challenge (the Friend has no definite outcome before Superobserver measures).  
- Many-worlds: challenged by LF violation (absoluteness of events).  
- Relational QM: no challenge.  
- VVV-QMRF / K-space: predicts non-zero K9_E — positive result confirms, null result falsifies.

**§9.4 — Limitations**  
- Optical implementation only — "Friend" is not a conscious observer.  
- Loopholes as stated in §8.  
- Framework (VVV-QMRF) not yet independently tested — this experiment is a first test.

**§9.5 — Future Directions**  
- Extend to solid-state or superconducting qubit implementations where macroscopic "Friend" is more physically meaningful.  
- Test other tilted angles to map out the full θ-dependence of K9_E.  
- Design experiments that close the locality loophole simultaneously.

**OUTPUT FORMAT:** Subsections, flowing prose.  
**WRITING STYLE:** Measured, scholarly. Distinguish what is proven from what is speculated.

---

### §10 — Conclusion

**PURPOSE:**  
Summarize the paper in 3–5 paragraphs. No new information.

**CONTENT REQUIREMENTS:**  
1. Restate the main finding: equatorial cancellation theorem explains why existing EWF experiments cannot test K9_E.  
2. Restate the proposed solution: one quarter-wave plate, θ = 31°, same N as Bong 2020.  
3. Restate the predictions: 8.6σ LF violation, 20.8σ K9_E signal, simultaneously.  
4. Restate the robustness: predictions survive realistic apparatus imperfections down to μ = [value] and η = [value].  
5. Closing statement: the experiment is feasible with existing hardware and represents the first test of outcome-dependent quantum registration in an EWF scenario.

**OUTPUT FORMAT:** Prose only, no subheadings.  
**WRITING STYLE:** Direct. Repeat key numbers. End on the scientific significance, not on hype.

---

### Abstract (Written Last)

**PURPOSE:**  
150–200 words. Written after all sections are complete.

**STRUCTURE:**  
- Sentence 1–2: motivation (what EWF experiments test and why they matter).  
- Sentence 3–4: the gap (equatorial cancellation theorem — why existing experiments cannot test K9_E).  
- Sentence 5–6: the proposal (one QWP, θ = 31°).  
- Sentence 7–8: the predictions (Gen LF 1 = +0.089 at 8.6σ, δ⟨A₁B₂⟩ = −0.036 at 20.8σ, N = 91,000).  
- Sentence 9: robustness (survives realistic imperfections).  
- Sentence 10: significance (first test of outcome-dependent registration in EWF scenarios).

**NO:** jargon not defined in the abstract, acronyms without expansion, claims beyond what the paper proves.

---

## 4. Supplemental Material Plan

| Supplement | Content | Priority |
|-----------|---------|----------|
| S1 | Full algebraic proof of Equatorial Cancellation Theorem | High |
| S2 | Complete correlator table (all 9 ⟨AᵢBⱼ⟩, all angles) | High |
| S3 | Monte Carlo simulation code (Python, reproducible) | High |
| S4 | Sensitivity analysis full numerical results | Medium |
| S5 | VVV-QMRF framework summary (self-contained, 2–3 pages) | Medium |
| S6 | Comparison table: Proietti 2019, Bong 2020, this work | Low |

---

## 5. Figure List

| Figure | Description | Section | Software |
|--------|-------------|---------|---------|
| 1 | EWF setup schematic: two labs, two superobservers, entangled source | §2.1 | Inkscape / TikZ |
| 2 | Modified optical path: QWP insertion point marked on Bong schematic | §4.2 | Inkscape / TikZ |
| 3 | Monte Carlo histogram: Gen LF 1 distribution across 10,000 runs | §6.3 | Python / matplotlib |
| 4 | FOM vs μ: with 5σ threshold and Bong operating point | §7.1 | Python / matplotlib |
| 5 | 2D heatmap: FOM(μ, η) with 5σ contour | §7.4 | Python / matplotlib |

---

## 6. Reference List (Minimum Required)

| Key | Citation |
|-----|---------|
| [Wigner1961] | Wigner, E.P. (1961). Remarks on the mind-body question. |
| [Hardy1992] | Hardy, L. (1992). Quantum mechanics, local realistic theories, and Lorentz-invariant realistic theories. PRL 68, 2981. |
| [FR2018] | Frauchiger, D. & Renner, R. (2018). Quantum theory cannot consistently describe the use of itself. Nature Comms 9, 3711. |
| [Proietti2019] | Proietti, M. et al. (2019). Experimental test of local observer-independence. Science Advances 5, eaaw9832. |
| [Bong2020] | Bong, K.W. et al. (2020). A strong no-go theorem on the Wigner's friend paradox. Nature Physics 16, 1199–1205. |
| [Brunner2014] | Brunner, N. et al. (2014). Bell nonlocality. Reviews of Modern Physics 86, 419. |
| [Bell1964] | Bell, J.S. (1964). On the Einstein Podolsky Rosen paradox. Physics 1, 195–200. |
| [Giustina2015] | Giustina, M. et al. (2015). Significant-loophole-free test of Bell's theorem. PRL 115, 250401. |

---

## 7. Writing Order (Recommended)

Write sections in this order to minimize backtracking:

1. §3 first — the theorem is the core, write it while the proof is freshest.  
2. §4 — hardware description, mostly lookup from Bong 2020 supplemental.  
3. §5 — predictions table, direct output of K9-S12 calculations.  
4. §6 — statistical analysis, run Monte Carlo simulation to get numbers.  
5. §7 — robustness, run sensitivity scans to populate tables.  
6. §8 — loophole analysis, mostly reference lookup + one computation (η_crit).  
7. §2 — background, now written knowing exactly what needs to be defined.  
8. §9 — discussion, written after knowing all results.  
9. §1 — introduction, written after knowing the full story.  
10. §10 — conclusion, written last among main sections.  
11. Abstract — written absolutely last.  
12. Supplemental — parallel to main text, as computations are done.

---

## 8. LLM Session Plan

Each session below is one focused writing or computation task:

| Session | Task | Output |
|---------|------|--------|
| K9-S13-A | Run sensitivity scan: FOM(μ, η, Δθ) | Numerical tables for §7 |
| K9-S13-B | Run Monte Carlo: 10,000 runs, Gen LF 1 and δ⟨A₁B₂⟩ distributions | Histogram data for §6 |
| K9-S13-C | Compute full correlator table at modified angles | Table for §5 |
| K9-S13-D | Compute η_crit for detection loophole | Number for §8 |
| K9-S13-E | Write §3 (theorem + proof) | Draft text |
| K9-S13-F | Write §4 (experimental protocol) | Draft text |
| K9-S13-G | Write §5 (predictions) | Draft text |
| K9-S13-H | Write §6 + §7 (statistical + robustness) | Draft text |
| K9-S13-I | Write §8 + §9 (loopholes + discussion) | Draft text |
| K9-S13-J | Write §1 + §2 + §10 + Abstract | Draft text |
| K9-S13-K | Full paper integration, consistency check, reference formatting | Final draft |

---

## 9. Quality Checklist (Pre-Submission)

- [ ] Every symbol defined at first use  
- [ ] Every number in the paper has an associated uncertainty  
- [ ] Every figure has a self-contained caption  
- [ ] All 5 loopholes addressed in §8  
- [ ] Decision criteria in §5.3 cover all four possible outcome combinations  
- [ ] Supplemental S3 (code) is runnable by a third party without modification  
- [ ] Abstract contains no undefined acronyms  
- [ ] Reference list complete and formatted consistently  
- [ ] FOM values in §7 match values in §5 and §6 (no internal inconsistency)  
- [ ] Robustness table §7.5 populated with actual computed values (not placeholders)

---

*End of plan. Next step: K9-S13-A (sensitivity scan) or K9-S13-E (write §3 theorem).*
