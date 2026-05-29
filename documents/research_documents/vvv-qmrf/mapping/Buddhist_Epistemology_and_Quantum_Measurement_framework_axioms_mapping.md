Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# Framework Mapping: Buddhist Epistemology → Quantum Measurement — Four Axioms

**Document type:** mapping

---

## Canonical Identification / Nhận diện Chuẩn

| Field | Value |
|---|---|
| Document type | mapping |
| System A / Ground system | Buddhist Epistemology / Pramāṇavāda |
| System B / Target system | Quantum Measurement / VVV-QMRF registration layer |
| Mapping status | Structural analogy, support, contrast, or gap mapping unless a local row states otherwise. |
| Graph relation | Uses BE node/edge codes from `SYSTEM_Buddhist_Epistemology/system_be_full.md` when present. |
| Identity boundary | Mapping is not identity; BE concepts do not become canonical QM mechanisms or physical laws. |
| RCA boundary | Treat cross-domain links as structurally useful comparisons, not proof that Buddhist Epistemology solves Quantum Measurement. |
| Terminology rule | Use `registration-state update` for the K-side update and `detector response` only for the apparatus physical signal. |


## Ground System: Pramāṇavāda — Dignāga and Dharmakīrti corpus
## Method: Axiom-driven clustering. BE nodes and edges from [system_be_full.md](../../../SYSTEM_Buddhist_Epistemology/system_be_full.md) are assigned to the axiom they structurally support. Each axiom is mapped to its Quantum Measurement interpretation.
## Scope: Epistemology only. No metaphysics, soteriology, or cosmology.
## Node/Edge Codes: BE node and edge definitions follow the single RCA SOT: [system_be_full.md](../../../SYSTEM_Buddhist_Epistemology/system_be_full.md)
## Framework source: [bei_framework_4_axioms.md](../archives/Framework_Buddhist_Epistemology_Interpretation_of_Quantum_Measurement/bei_framework_4_axioms.md)

---

# Four Axioms — Summary

| # | Axiom | Pali / Sanskrit | Core Principle | QM Mapping |
| --- | --- | --- | --- | --- |
| 1 | Dependent Arising | Paṭiccasamuppāda (Pāli) / Pratītyasamutpāda (Skt.) | No state exists independently. All phenomena arise in dependence on conditions. | No absolute quantum state — only states relative to a reference system. |
| 2 | Emptiness | Suññatā (Pāli) / Śūnyatā (Skt.) | No entity has intrinsic properties (niḥsvabhāvatā). What appears as a property is a conceptual imputation dependent on relational conditions. | Spin, position are properties of the particle-in-relation-to-apparatus. Properties are relations, not intrinsic attributes. |
| 3 | Consciousness-Only | Vijñaptimātra (Skt.) | Consciousness (vijñāna) is the condition for reality to manifest. The object of cognition (ālambana) is nothing other than the appearance of an object in cognition itself. | Measurement does not reveal a pre-existing state — measurement is the condition for the state to manifest. Within this interpretive mapping, the epistemically relevant closure is modeled as a registration-state update; this does not by itself deny Standard QM's ρ-side state-update language. |
| 4 | Two Truths | Dvisatya (Skt.) | Conventional truth (saṃvṛtisat) and ultimate truth (paramārthasat) are two levels at which reality is cognized. | The quantum-classical boundary is epistemic, not physical. Classical emerges from the epistemic position where the observer can stand "outside" the system. |

---

# Axiom 1 — Dependent Arising (Pratītyasamutpāda)

**Principle:** No state exists independently. All phenomena arise in dependence on conditions.
**QM Mapping:** No absolute quantum state exists — there are only states relative to a reference system. Wavefunction describes the structure of possibilities within a given relational network. This is epistemology, not ontology.

## A1.1 — Node Assignment

| Node code | Concept (Skt.) | Category | Role in Axiom 1 |
| --- | --- | --- | --- |
| N_BE_00029 | Kṣaṇabhaṅgavāda (Momentariness) | Ontology–cognition | Primary anchor: radical impermanence as the ontological basis of dependent arising |
| N_BE_00021 | Svabhāvapratibandha (Essential relation) | Logic | Primary anchor: the two types of necessary relation (causal and identity) that ground inference |
| N_BE_00020 | Avinābhāva (Necessary relation) | Logic | Primary anchor: "not-being-without" — the principle of inseparability between ground and consequence |
| N_BE_00001 | Pramāṇa (Valid cognition) | Foundation | Relational validity: a cognition is valid only within its relational context |
| N_BE_00019 | Vyāpti (Pervasion) | Logic | The logical relation of pervasion that depends on relational structure, not intrinsic essence |
| N_BE_00016 | Liṅga / Hetu (Sign / Logical reason) | Logic | The inferential mark — knowledge derived from relational dependence between sign and signified |
| N_BE_00018 | Trairūpya (Triple-condition syllogism) | Logic | Three conditions for valid reason — all defined relationally (presence in similar cases, absence in dissimilar) |
| N_BE_00017 | Pakṣa (Thesis) | Logic | The locus where reason and probandum co-occur — defined by relational co-location |

## A1.2 — Core Mapping

### A1.2.1 — Momentariness and the Relational Foundation

- **Buddhist Epistemology:** N_BE_00029 (Kṣaṇabhaṅgavāda) — "a moment disappears as soon as it appears without duration." The radical culmination of process philosophy. Rooted in the Buddha's dynamic law of dependent arising (pratītyasamutpāda). No entity persists across moments; what appears as continuity is a series of causally connected moments.
- **Quantum Measurement:** No persistent absolute quantum state. The wavefunction at t₁ and the wavefunction at t₂ are linked by unitary evolution, but there is no underlying substance that persists across time. The state is always a state-at-a-moment, defined relative to the measurement context that specifies it.
- **Correspondence type:** Moderate parallel. Both systems reject persistent substance in favor of momentary, relationally-defined states. Divergence: QM has temporal discontinuity formally (collapse, decoherence) but no epistemological doctrine of momentariness equivalent to kṣaṇabhaṅgavāda. The pre-measurement to post-measurement transition is categorically discontinuous but not theorized as a doctrine of momentary existence (cf. BIAN-8 in refine_mapping.md).

**Relevant edges:**
- ED_BE_00034: N_BE_00029 → N_BE_00022 (supports — momentariness supports causal efficacy)
- ED_BE_00035: N_BE_00029 → N_BE_00013 (characterizes — the particular is momentary)

### A1.2.2 — Essential Relation as the Ground of Dependence

- **Buddhist Epistemology:** N_BE_00021 (Svabhāvapratibandha) — Dharmakīrti's innovation. Two types: tadutpatti (causality — relation between effect and cause) and tādātmya (logical genus-species identity — relation between a specific and its general class). Replaces Dignāga's purely inductive vyāpti with a deductive, ontology-grounded relation. Things are connected not by logical convention but by ontological dependence.
- **Quantum Measurement:** Entanglement correlations and conservation-based correlations. The quantum state of a composite system is not factorable into independent states of subsystems. Conservation laws (e.g., angular momentum in pair production) ground correlations of the tadutpatti type; any comparison with tādātmya is only an analogy to invariance, not a physical identity relation. Entanglement proper motivates a VVV-QMRF extension relation — non-causal, non-identity-based registration non-separability — beyond Buddhist Epistemology's two classical *svabhāvapratibandha* relation types (see BIAN-10 in refine_mapping.md). Svabhāvapratibandha supplies the bounded source analogue; IRB is the VVV-QMRF extension.
- **Correspondence type:** Partial. Conservation-based correlations approximate tadutpatti; they are at most analogies to invariance, not tādātmya proper. Entanglement proper exceeds both classical BE relation categories; VVV-QMRF treats it as IRB, an extension relation using N_BE_00021 only as a source analogue (BIAN-10).

**Relevant edges:**
- ED_BE_00011: N_BE_00019 → N_BE_00021 (grounded in — pervasion grounded in essential relation)
- ED_BE_00012: N_BE_00021 → N_BE_00022 (has as basis — essential relation has causal efficacy as basis)

### A1.2.3 — Pramāṇa as Relational Validity

- **Buddhist Epistemology:** N_BE_00001 (Pramāṇa) — validity is relational and functional, not intrinsic to any object or subject alone. Pramāṇa is the condition-event under which knowledge is certified. The four components (pramāṇa, pramā, prameya, pramāṇaphala) are relationally integrated — none functions independently.
- **Quantum Measurement:** Measurement operator. Defines the formal conditions under which a physical quantity is valid. The operator is not valid in isolation — it is valid only in relation to the Hilbert space structure, the state preparation, and the measurement context.
- **Correspondence type:** Structural parallel. Both define validity relationally at the level of the act-instrument.

**Relevant edges:**
- ED_BE_00001: N_BE_00001 → N_BE_00002 (includes — pramāṇa encompasses pratyakṣa)
- ED_BE_00002: N_BE_00001 → N_BE_00003 (includes — pramāṇa encompasses anumāna)
- ED_BE_00003: N_BE_00001 → N_BE_00005 (has as object — pramāṇa directed toward prameya)
- ED_BE_00004: N_BE_00001 → pramāṇaphala (produces — the pramāṇa process culminates in resultant cognition as its outcome)

### A1.2.4 — Inference and the Logic of Dependence

- **Buddhist Epistemology:** N_BE_00020 (Avinābhāva) — Vasubandhu's principle of "not-being-without": a property which does not occur without the probandum. N_BE_00019 (Vyāpti) — Dignāga's pervasion: the logical relation between probans and probandum. N_BE_00016 (Liṅga) — the sign that indicates the probandum through relational dependence. N_BE_00018 (Trairūpya) — the three conditions all defined relationally (presence in sapakṣa, absence in vipakṣa).
- **Quantum Measurement:** Predictive structure of QM. The wavefunction ψ encodes probabilistic relations between preparation and measurement outcomes. ψ does not describe an object — it describes the relational structure linking preparation context to outcome distributions. The relation between preparation and outcome is one of probabilistic dependence, analogous to the sign-signified relation in inference.
- **Correspondence type:** Structural parallel. Both systems derive knowledge from relational dependence structures rather than direct access to objects.

**Relevant edges:**
- ED_BE_00026: N_BE_00020 → N_BE_00019 (is precursor of — avinābhāva as precursor of vyāpti)
- ED_BE_00010: N_BE_00016 → N_BE_00019 (requires — sign requires pervasion)
- ED_BE_00009: N_BE_00016 → N_BE_00017 (qualifies — sign qualifies thesis subject)
- ED_BE_00039: N_BE_00016 → N_BE_00020 (requires — sign requires necessary relation)

### A1.2.5 — Axiom 1 Conclusion

Wavefunction does not describe "where a particle is." Wavefunction describes the structure of possibilities within a given relational network. All quantum states are states-in-relation. No state exists independently — this is the quantum expression of pratītyasamutpāda.

---

# Axiom 2 — Emptiness (Śūnyatā)

**Principle:** No entity has intrinsic properties (niḥsvabhāvatā). What appears as a property is a conceptual imputation dependent on relational conditions.
**QM Mapping:** "Particle has spin 1/2" is a syntactically incorrect statement. The correct statement is: "Particle-when-measured-by-this-apparatus has spin 1/2." Properties are not intrinsic — properties are relations.

## A2.1 — Node Assignment

| Node code | Concept (Skt.) | Category | Role in Axiom 2 |
| --- | --- | --- | --- |
| N_BE_00025 | Śūnyatā (Emptiness) | Ultimate object | Primary anchor: the absence of inherent existence in self and phenomena |
| N_BE_00013 | Svalakṣaṇa (Particular / Unique mark) | Ontology–cognition | Primary anchor: the unique particular that possesses causal efficacy — the ultimately real |
| N_BE_00014 | Sāmānyalakṣaṇa (Universal / General mark) | Ontology–cognition | Primary anchor: the conceptually constructed universal — empty of causal efficacy |
| N_BE_00022 | Arthakriyā (Causal efficacy) | Ontology–cognition | Primary anchor: the criterion of reality — only causally efficacious entities exist ultimately |
| N_BE_00005 | Prameya (Object of cognition) | Foundation | The object domain structured by the particular-universal duality |
| N_BE_00015 | Apoha / Anyāpoha (Exclusion) | Philosophy of language | Meaning by exclusion — concepts are defined by what they are not, not by intrinsic content |
| N_BE_00008 | Vikalpa / Kalpanā (Conceptual construction) | Mental structure | The mind's superimposition of categories onto bare perception — the source of imputed properties |
| N_BE_00009 | Nirvikalpaka pratyakṣa (Non-conceptual perception) | Mental structure | Pure perception free from conceptual overlay — access to the particular without imputation |

## A2.2 — Core Mapping

### A2.2.1 — Emptiness as the Ground Principle

- **Buddhist Epistemology:** N_BE_00025 (Śūnyatā) — the absence of inherent existence (niḥsvabhāvatā). Nāgārjuna's metaphysical essencelessness. No entity possesses svabhāva (own-being or intrinsic nature). What appears as a stable property is a conceptual imputation arising from relational conditions. Emptiness is not nihilism — it is the rejection of intrinsic nature as the ground of the conventional order.
- **Quantum Measurement:** No pre-measurement values. A quantum system does not possess definite values for all observables prior to measurement. The Kochen-Specker theorem (contextuality) demonstrates that measurement outcomes depend on the measurement context — there are no context-independent values. Bell's theorem rules out local hidden variables. Properties are not carried by the particle; they are constituted in the measurement relation.
- **Correspondence type:** Strong parallel. Both systems deny intrinsic properties and ground the manifest order in relational conditions. Emptiness (niḥsvabhāvatā) coincides structurally with the rejection of hidden variables as intrinsic attributes.

**Relevant edges:**
- ED_BE_00031: N_BE_00025 → N_BE_00026 (is ultimate aspect of — emptiness is the ultimate truth dimension)
- ED_BE_00022: N_BE_00012 → N_BE_00025 (realizes — yogic perception realizes emptiness)
- ED_BE_00030: N_BE_00024 → N_BE_00025 (realizes — wisdom realizes emptiness)

### A2.2.2 — Svalakṣaṇa and the Criterion of Reality

- **Buddhist Epistemology:** N_BE_00013 (Svalakṣaṇa) — the unique particular. Per Dharmakīrti: (a) has power to produce effects (arthakriyākāritva), (b) is specific (asādhāraṇa), (c) is not denotable by a word (śabdasyāviṣaya), (d) is apprehensible without depending upon other factors. N_BE_00022 (Arthakriyā) — "That which is able to perform a function exists ultimately." Only objects able to participate causally in producing phenomena are real.
- **Quantum Measurement:** Measurement outcome. The singular, definite result produced in a specific measurement context. The outcome is causally efficacious — it produces effects in the apparatus and the observer's register. It is specific, non-repeatable (the post-measurement state differs from the pre-measurement state), and not fully denotable by the wavefunction alone (which encodes probabilities, not actualities).
- **Correspondence type:** Moderate parallel. The measurement outcome shares the causal efficacy and specificity of svalakṣaṇa. Divergence: the outcome is already numerically encoded — a symbolic object — whereas svalakṣaṇa is pre-conceptual.

**Relevant edges:**
- ED_BE_00032: N_BE_00013 → N_BE_00022 (possesses — the particular possesses causal efficacy)
- ED_BE_00005: N_BE_00002 → N_BE_00013 (apprehends — direct perception apprehends the particular)
- ED_BE_00014: N_BE_00009 → N_BE_00013 (apprehends — non-conceptual perception apprehends the particular)

### A2.2.3 — Sāmānyalakṣaṇa and the Conceptual Superstructure

- **Buddhist Epistemology:** N_BE_00014 (Sāmānyalakṣaṇa) — the universal, general characteristic. Per Dharmakīrti: (a) has no power to produce effects, (b) is common to many things, (c) is denotable by a word, (d) is not apprehensible without depending upon other factors such as verbal conventions. The universal is not ultimately real — it is a conceptual construction (vikalpa) superimposed on the particular.
- **Quantum Measurement:** Wavefunction ψ. Encodes the statistical structure of possible outcomes across many measurements. ψ is common to an ensemble of identically prepared systems. It is denotable by mathematical symbols. But ψ does not produce a specific outcome — it encodes probabilities, not actualities. It is the conceptual vehicle for prediction, not the causally efficacious particular.
- **Correspondence type:** Strong parallel. Both are epistemically necessary but ontologically secondary — real as conceptual structure, not as causally efficacious particular.

**Relevant edges:**
- ED_BE_00033: N_BE_00014 → N_BE_00022 (lacks — the universal lacks causal efficacy)
- ED_BE_00006: N_BE_00003 → N_BE_00014 (apprehends — inference apprehends the universal)
- ED_BE_00013: N_BE_00008 → N_BE_00014 (operates on — conceptual construction operates on the universal)

### A2.2.4 — Apoha and the Empty Nature of Concepts

- **Buddhist Epistemology:** N_BE_00015 (Apoha) — Dignāga's theory: "a word expresses its own object through the exclusion of the other [things]." Meaning is conveyed by excluding what something is not (not-non-cow → cow). Concepts have no positive intrinsic content — they function through differential exclusion. Verbal cognition is not an independent pramāṇa but a variety of inference.
- **Quantum Measurement:** Complementarity at the meta-semantic level. Bohr's complementarity: conjugate observables (position–momentum, energy–time) are mutually exclusive — the definition of one excludes the simultaneous definite determination of the other. An observable is constituted partly by its exclusion relations with incompatible observables. This is the meta-semantic parallel: physical meaning in QM is partly constituted by exclusion, just as apoha constitutes conceptual meaning through exclusion.
- **Correspondence type:** Moderate structural parallel. Both constitute meaning through differential exclusion rather than positive intrinsic content. The parallel is at the meta-semantic level (see refine T6.05).

**Relevant edges:**
- ED_BE_00016: N_BE_00015 → N_BE_00003 (is linguistic variant of — apoha reduced to inference)

### A2.2.5 — Vikalpa and the Imputation of Properties

- **Buddhist Epistemology:** N_BE_00008 (Vikalpa/Kalpanā) — conceptualized, categorizing cognition that applies names and classes. The mind superimposes structures like proper names (yadṛcchā-śabda), genus-words (jāti-śabda), quality-words (guṇa-śabda), action-words (kriyā-śabda), and substance-words (dravya-śabda). N_BE_00009 (Nirvikalpaka pratyakṣa) — pure perception free from this superimposition.
- **Quantum Measurement:** The language of classical properties. Statements like "the electron has spin up" or "the particle is at position x" apply classical property-language to quantum systems. These statements are pragmatic (vyavahāra) — they are useful but do not correspond to intrinsic attributes of the system. They are conceptual constructions imposed on measurement outcomes.
- **Correspondence type:** Structural parallel. Both identify a layer of conceptual imputation that is pragmatically necessary but ontologically empty.

**Relevant edges:**
- ED_BE_00015: N_BE_00009 → N_BE_00008 (contrasted with — non-conceptual perception contrasted with conceptual construction)
- ED_BE_00038: N_BE_00002 → N_BE_00008 (is free from — direct perception is free from conceptual construction)

### A2.2.6 — Axiom 2 Conclusion

"Particle has spin 1/2" is syntactically incorrect. The correct statement is: "Particle-when-measured-by-this-apparatus has spin 1/2." Properties are not intrinsic attributes carried by objects — properties are relations constituted in measurement contexts. This is the quantum expression of śūnyatā.

---

# Axiom 3 — Consciousness-Only (Vijñaptimātra)

**Principle:** Consciousness (vijñāna) is the condition for reality to manifest. The object of cognition (ālambana) is nothing other than the appearance of an object in cognition itself (svasaṃvedana).
**QM Mapping:** Measurement does not "reveal" a pre-existing state — measurement is the condition for the state to manifest. Within this interpretive mapping, the epistemically relevant closure is modeled as a cognitive or registration-state update when a new relation is established. This does not deny that Standard QM may use ρ-side state-update or collapse language when describing the physical layer.

## A3.1 — Node Assignment

| Node code | Concept (Skt.) | Category | Role in Axiom 3 |
| --- | --- | --- | --- |
| N_BE_00011 | Svasaṃvedana (Self-awareness) | Type of perception | Primary anchor: reflexive cognition — the mind's awareness of its own states; the self-certification principle |
| N_BE_00010 | Mānasa pratyakṣa (Mental perception) | Type of consciousness | Primary anchor: inner cognition through mental consciousness, independent of external sense faculties |
| N_BE_00002 | Pratyakṣa (Direct perception) | Source of knowledge | Primary anchor: immediate cognition — the terminal, non-inferential epistemic event |
| N_BE_00006 | Bhrānti (Erroneous cognition) | Epistemic error | Mistaken apprehension — the inversion of reality that consciousness can fall into |
| N_BE_00007 | Saṃśaya (Doubt) | Epistemic error | Indecision — the state that motivates the pursuit of certainty through cognition |
| N_BE_00023 | Avidyā / Avijjā (Ignorance) | Epistemic obstacle | Fundamental non-knowing — the root obstruction that consciousness must overcome |

## A3.2 — Core Mapping

### A3.2.1 — Svasaṃvedana and the Measurement Problem

- **Buddhist Epistemology:** N_BE_00011 (Svasaṃvedana) — every cognition is simultaneously aware of itself. Cognition of blue is also, non-inferentially, an awareness of the cognizing-of-blue. Self-luminous (svaprakāśa), not requiring a second-order act to register the first-order act. Svasaṃvedana is the structural grounding of the entire Pramāṇavāda system: it stops the regress of meta-cognitions and self-certifies every valid cognition without external verification.
- **Quantum Measurement:** BIAN-2 — Observer Self-Reference / Reflexive Cognition of Measurement Act. QM has no formal account of an observer's cognition of its own measurement act. The measurement problem (von Neumann chain / Wigner's friend) is, in structural terms, the consequence of this gap: without a self-certifying epistemic layer, the registration chain has no formal stopping point.
- **Correspondence type:** Structural gap. This is the deepest single asymmetry in the mapping. Svasaṃvedana is not one feature among others in Pramāṇavāda; it is the system's foundational self-certification principle. QM has no equivalent, and the absence of an equivalent is precisely what makes the measurement problem formally irresolvable within standard QM formalism.

**Relevant edges:**
- ED_BE_00019: N_BE_00011 → N_BE_00002 (is subtype of — self-awareness is a subtype of direct perception) [uncertain]
- ED_BE_00020: N_BE_00010 → N_BE_00011 (entails — mental perception entails self-awareness) [uncertain]

### A3.2.2 — Measurement as Condition for Manifestation

- **Buddhist Epistemology:** N_BE_00002 (Pratyakṣa) — immediate cognition through the senses, prior to inference or conceptual overlay. Dignāga defines it as "devoid of mental construction (kalpanāpodham)." It apprehends the particular (svalakṣaṇa) as pure sensation. Pratyakṣa is the condition under which the particular manifests to a cognizing agent. Without the cognitive act, there is no manifestation of the object-as-known.
- **Quantum Measurement:** Measurement does not "reveal" a pre-existing state — measurement is the condition for the state to manifest as a definite outcome. Prior to measurement, the system is in a superposition — not in a definite state waiting to be discovered. The measurement act is constitutive of the outcome, not merely revelatory of a pre-existing fact.
- **Correspondence type:** Strong parallel. Both systems treat the epistemic act as constitutive of the manifest outcome, not merely revelatory of a pre-existing reality.

**Relevant edges:**
- ED_BE_00001: N_BE_00001 → N_BE_00002 (includes — pramāṇa encompasses pratyakṣa)
- ED_BE_00005: N_BE_00002 → N_BE_00013 (apprehends — perception apprehends the particular)
- ED_BE_00038: N_BE_00002 → N_BE_00008 (is free from — perception is free from conceptual construction)

### A3.2.3 — Mānasapratyakṣa and the Unmodeled Stratum

- **Buddhist Epistemology:** N_BE_00010 (Mānasa pratyakṣa) — inner cognition through mental consciousness, independent of the five external sense faculties. Apprehends the mental image (ākāra) of the sense object rather than the external object directly. One causal step removed from direct sense contact, but still non-conceptual.
- **Quantum Measurement:** BIAN-1 — Post-Detection Internal Representational State. The internal state of an observer or apparatus system after a detector event fires but before any symbolic encoding, recording, or storage of the result. QM moves directly from physical interaction to symbolic output value. The intermediate stratum between raw physical signal and registered number is unmodeled.
- **Correspondence type:** Structural gap. QM has no formal account of the representational transition between physical detection and symbolic readout. The gap between click and number is outside the formalism.

**Relevant edges:**
- ED_BE_00018: N_BE_00010 → N_BE_00002 (is subtype of — mental perception is a subtype of direct perception)
- ED_BE_00020: N_BE_00010 → N_BE_00011 (entails — mental perception entails self-awareness)

### A3.2.4 — Error, Doubt, and Ignorance

- **Buddhist Epistemology:** N_BE_00006 (Bhrānti) — mistaken apprehension; inversion of the true nature of an object. N_BE_00007 (Saṃśaya) — a state of indecision; the pursuit of certainty (nirṇaya) requires some initial doubt as motivation. N_BE_00023 (Avidyā) — fundamental non-knowing of the true nature of reality; the root of suffering and cyclic existence. These three form the negative space around valid cognition: error is wrong cognition, doubt is absent cognition, ignorance is the structural precondition for both.
- **Quantum Measurement:** Measurement error, statistical uncertainty, and the unknown. QM has a formal theory of measurement error (standard deviation, confidence intervals) and statistical uncertainty (inherent in the probabilistic structure). But QM has no equivalent for avidyā as a structural epistemic obstacle — the theory itself is neutral with respect to the observer's cognitive state. The observer's ignorance is not a formal variable in the theory.
- **Correspondence type:** Partial parallel for error and doubt (formal QM analogues exist); structural gap for ignorance (no QM analogue for a structural epistemic obstacle).

**Relevant edges:**
- ED_BE_00027: N_BE_00023 → N_BE_00006 (causes — ignorance causes erroneous cognition)
- ED_BE_00028: N_BE_00023 → N_BE_00007 (gives rise to — ignorance gives rise to doubt) [uncertain]
- ED_BE_00037: N_BE_00007 → N_BE_00027 (motivates — doubt motivates inductive reasoning) [uncertain]

### A3.2.5 — Axiom 3 Conclusion

Within this interpretive mapping, the epistemically relevant closure is modeled as a cognitive or registration-state update when a new relation is established. This does not deny that Standard QM may use ρ-side state-update or collapse language for the physical layer. Nothing in this claim by itself replaces the physical description of the particle; it marks a change in epistemic relation and registered status. Measurement is the condition for the state to manifest, not the revelation of a pre-existing state. The observer is structurally necessary but undefined in QM — this is the deepest gap in the mapping (BIAN-2).

---

# Axiom 4 — Two Truths (Dvisatya)

**Principle:** Conventional truth (saṃvṛtisat) and ultimate truth (paramārthasat) are two levels at which reality is cognized. The conventional world is the domain of conceptual construction (vikalpa); the ultimate is dynamically subtle, non-conceptual, irreducible.
**QM Mapping:** The quantum-classical boundary is epistemic, not physical. Classical emerges from the epistemic position where the observer can stand "outside" the system; quantum is the domain where the observer cannot be separated.

## A4.1 — Node Assignment

| Node code | Concept (Skt.) | Category | Role in Axiom 4 |
| --- | --- | --- | --- |
| N_BE_00026 | Dvisatya (Two truths) | Ontology–cognition | Primary anchor: the two-tier epistemic framework |
| N_BE_00003 | Anumāna (Inference) | Source of knowledge | Primary anchor: indirect cognition operating on the universal — the conventional tier's primary instrument |
| N_BE_00027 | Svārthānumāna (Inductive reasoning) | Logic | "Inference for oneself" — the private, psychologically real form of inference |
| N_BE_00028 | Parārthānumāna (Deductive reasoning) | Logic | "Inference for others" — the public, communicable, contestable form of inference |
| N_BE_00024 | Prajñā / Paññā (Wisdom) | Liberation | Penetrating insight into ultimate reality — the cognitive instrument of the ultimate tier |
| N_BE_00012 | Yogipratyakṣa (Yogic perception) | Type of perception | Direct, supra-ordinary perception accessing ultimate reality through cultivated faculty |
| N_BE_00030 | Pramāṇabhūta (Means of valid cognition) | Foundation | The Buddha as possessor of ultimate valid knowledge — the ideal epistemic agent |
| N_BE_00004 | Āgama / Śabda (Testimony) | Source of knowledge | Knowledge from reliable authority — reduced to inference by Dignāga; conventional knowledge |

## A4.2 — Core Mapping

### A4.2.1 — The Two Truths as Epistemic Tiers

- **Buddhist Epistemology:** N_BE_00026 (Dvisatya) — Conventional truth (saṃvṛtisat, prajñaptisat): the conceptually constructed phenomenal world. Ultimate truth (paramārthasat, dravyasat): the dynamically subtle, spatio-temporally unstructured, non-conceptual, irreducible reality. These are not two separate worlds — they are two epistemic positions on the same reality. The conventional is not false; it is the way reality appears when filtered through conceptual construction.
- **Quantum Measurement:** The quantum-classical cut is epistemic, not physical. Classical physics operates as the effective description when the observer can stand "outside" the system and treat measurement as non-invasive. Quantum mechanics is required when the observer cannot be separated from the system. The boundary is not a physical line in nature — it is the boundary between epistemic positions. Structurally, this parallels the two-truth distinction: classical physics functions analogously to conventional description (pragmatically indispensable but not ultimate), while quantum mechanics approaches the ultimate tier (where observer and system cannot be pried apart).
- **Correspondence type:** Strong parallel. Both systems recognize two tiers of description not as ontological division but as epistemic distinction arising from the observer's relation to the observed.

**Relevant edges:**
- ED_BE_00031: N_BE_00025 → N_BE_00026 (is ultimate aspect of — emptiness is the ultimate truth dimension)

### A4.2.2 — Anumāna as the Conventional Tier's Instrument

- **Buddhist Epistemology:** N_BE_00003 (Anumāna) — the second valid pramāṇa. Operates on the universal (sāmānyalakṣaṇa) through conceptual thought. Does not contact its object directly; constructs knowledge from relational structure via sign (liṅga) and pervasion (vyāpti). This is the cognitive instrument of the conventional tier: indirect, conceptual, mediated.
- **Quantum Measurement:** Wavefunction ψ and the predictive formalism. All quantum predictions are inferential: they derive expected value distributions from ψ without direct access to individual outcomes. The formalism operates at the level of the universal — it predicts statistical patterns, not singular events. It is the conventional tier's instrument for the quantum domain.
- **Correspondence type:** Strong structural parallel. Both are indirect, conceptually mediated instruments operating at the level of the universal rather than the particular.

**Relevant edges:**
- ED_BE_00002: N_BE_00001 → N_BE_00003 (includes — pramāṇa encompasses anumāna)
- ED_BE_00006: N_BE_00003 → N_BE_00014 (apprehends — inference apprehends the universal)
- ED_BE_00007: N_BE_00003 → N_BE_00016 (operates through — inference operates through logical sign)
- ED_BE_00008: N_BE_00003 → N_BE_00018 (validated by — inference validated by triple-condition)

### A4.2.3 — Public and Private Inference

- **Buddhist Epistemology:** N_BE_00027 (Svārthānumāna) — "inference for oneself." Private, psychologically real. Begins with perceptible observation (darśana) of the sign. The full syllogistic structure need not be made explicit. N_BE_00028 (Parārthānumāna) — "inference for others." Public, communicable, contestable. Requires full articulation of pakṣa, hetu, and dṛṣṭānta. Taken in a metaphorical sense (upacāra).
- **Quantum Measurement:** Private theoretical calculation vs. published experimental result. Svārtha: a physicist's internal derivation of predicted outcomes from ψ before experiment. Parārtha: the published result with full measurement protocol, apparatus specification, statistical output, and error bars — subject to peer scrutiny and replication.
- **Correspondence type:** Functional parallel. Both distinguish the private cognitive act from the public, communicable demonstration. Scientific communication norms structurally mirror the svārtha-parārtha distinction.

**Relevant edges:**
- ED_BE_00023: N_BE_00027 → N_BE_00003 (is subtype of — svārtha is subtype of anumāna)
- ED_BE_00024: N_BE_00028 → N_BE_00003 (is subtype of — parārtha is subtype of anumāna)
- ED_BE_00025: N_BE_00027 → N_BE_00028 (grounds — private inference grounds public syllogism)

### A4.2.4 — Wisdom and Yogic Perception: Access to the Ultimate Tier

- **Buddhist Epistemology:** N_BE_00024 (Prajñā) — penetrating insight into the nature of reality; the path out of ignorance. The third of the three trainings: virtue (śīla), concentration (samādhi), and wisdom (prajñā). N_BE_00012 (Yogipratyakṣa) — direct, supra-ordinary perception arising from deep meditative cultivation. A mode of transcendental (alaukika) perception not involving external objects and sensory faculties. Accesses the ultimate tier directly, beyond conceptual mediation.
- **Quantum Measurement:** BIAN-3 — Limit-Case Observation by Different Faculty. QM has no formal category for observation that operates through a qualitatively different faculty or mechanism than standard measurement. All observers are formally equivalent in QM. There is no spectrum of observer types based on cultivated capacity.
- **Correspondence type:** Structural gap. Buddhist Epistemology has a spectrum of observer types distinguished by epistemic faculty. QM has one observer type, undefined. However, the structural insight — that different epistemic positions yield different tiers of description — is preserved in the two-truths mapping.

**Relevant edges:**
- ED_BE_00021: N_BE_00012 → N_BE_00002 (is subtype of — yogic perception is a subtype of direct perception) [uncertain]
- ED_BE_00022: N_BE_00012 → N_BE_00025 (realizes — yogic perception realizes emptiness) [uncertain]
- ED_BE_00029: N_BE_00024 → N_BE_00023 (dispels — wisdom dispels ignorance)
- ED_BE_00030: N_BE_00024 → N_BE_00025 (realizes — wisdom realizes emptiness)

### A4.2.5 — Pramāṇabhūta and Testimony

- **Buddhist Epistemology:** N_BE_00030 (Pramāṇabhūta) — the Buddha as possessor of valid method, arguments, meaning, practice, and purpose. Dignāga's guiding principle: one should accept a statement only after testing its validity, not out of reverence. N_BE_00004 (Āgama/Śabda) — testimony reduced to inference by Dignāga. Not an independent pramāṇa.
- **Quantum Measurement:** Authority of experimental consensus. Scientific knowledge is ultimately grounded in replicable measurement, not authority. A published result is accepted not because of the prestige of the lab but because it can be independently replicated. This mirrors Dignāga's epistemic stance: validity is tested, not inherited from authority.
- **Correspondence type:** Functional parallel at the level of epistemic norms. Both reject authority-as-validity and require independent verification.

**Relevant edges:**
- ED_BE_00036: N_BE_00030 → N_BE_00001 (is epithet of — pramāṇabhūta as epithet of the Buddha as pramāṇa)
- ED_BE_00017: N_BE_00004 → N_BE_00003 (reduced to — testimony reduced to inference)

### A4.2.6 — Axiom 4 Conclusion

No physical boundary separates the macro world from the micro world. The boundary lies between the tier where the observer can stand "outside" (classical) and the tier where the observer cannot be separated (quantum). Classical physics is saṃvṛtisat — conventionally valid, pragmatically indispensable, but not the ultimate description. Quantum mechanics is closer to paramārthasat — but both are epistemic positions, not ontological territories.

---

# Cross-Axiom Edge Table

All 39 core edges from [system_be_full.md](../../../SYSTEM_Buddhist_Epistemology/system_be_full.md) assigned to their primary axiom.

| Edge code | Source → Target | Relationship | Type | Axiom |
| --- | --- | --- | --- | --- |
| ED_BE_00034 | N_BE_00029 → N_BE_00022 | supports | Ontological | 1 |
| ED_BE_00035 | N_BE_00029 → N_BE_00013 | characterizes | Ontological | 1 |
| ED_BE_00011 | N_BE_00019 → N_BE_00021 | grounded in | Logical | 1 |
| ED_BE_00012 | N_BE_00021 → N_BE_00022 | has as basis | Ontological | 1 |
| ED_BE_00026 | N_BE_00020 → N_BE_00019 | is precursor of | Logical | 1 |
| ED_BE_00010 | N_BE_00016 → N_BE_00019 | requires | Logical | 1 |
| ED_BE_00009 | N_BE_00016 → N_BE_00017 | qualifies | Logical | 1 |
| ED_BE_00039 | N_BE_00016 → N_BE_00020 | requires | Logical | 1 |
| ED_BE_00001 | N_BE_00001 → N_BE_00002 | includes | Hierarchical | 1, 3 |
| ED_BE_00002 | N_BE_00001 → N_BE_00003 | includes | Hierarchical | 1, 4 |
| ED_BE_00003 | N_BE_00001 → N_BE_00005 | has as object | Structural | 1 |
| ED_BE_00004 | N_BE_00001 → pramāṇaphala | produces | Structural | 1 |
| ED_BE_00032 | N_BE_00013 → N_BE_00022 | possesses | Ontological | 2 |
| ED_BE_00033 | N_BE_00014 → N_BE_00022 | lacks | Ontological | 2 |
| ED_BE_00005 | N_BE_00002 → N_BE_00013 | apprehends | Epistemic | 2, 3 |
| ED_BE_00014 | N_BE_00009 → N_BE_00013 | apprehends | Epistemic | 2 |
| ED_BE_00006 | N_BE_00003 → N_BE_00014 | apprehends | Epistemic | 2, 4 |
| ED_BE_00013 | N_BE_00008 → N_BE_00014 | operates on | Epistemic | 2 |
| ED_BE_00015 | N_BE_00009 → N_BE_00008 | contrasted with | Oppositional | 2 |
| ED_BE_00016 | N_BE_00015 → N_BE_00003 | is linguistic variant of | Logical | 2 |
| ED_BE_00031 | N_BE_00025 → N_BE_00026 | is ultimate aspect of | Ontological | 2, 4 |
| ED_BE_00022 | N_BE_00012 → N_BE_00025 | realizes | Epistemic | 2, 4 |
| ED_BE_00030 | N_BE_00024 → N_BE_00025 | realizes | Epistemic | 2, 4 |
| ED_BE_00038 | N_BE_00002 → N_BE_00008 | is free from | Exclusionary | 2, 3 |
| ED_BE_00019 | N_BE_00011 → N_BE_00002 | is subtype of | Hierarchical | 3 |
| ED_BE_00020 | N_BE_00010 → N_BE_00011 | entails | Structural | 3 |
| ED_BE_00018 | N_BE_00010 → N_BE_00002 | is subtype of | Hierarchical | 3 |
| ED_BE_00027 | N_BE_00023 → N_BE_00006 | causes | Causal | 3 |
| ED_BE_00028 | N_BE_00023 → N_BE_00007 | gives rise to | Causal | 3 |
| ED_BE_00037 | N_BE_00007 → N_BE_00027 | motivates | Psychological | 3 |
| ED_BE_00007 | N_BE_00003 → N_BE_00016 | operates through | Logical | 4 |
| ED_BE_00008 | N_BE_00003 → N_BE_00018 | validated by | Logical | 4 |
| ED_BE_00023 | N_BE_00027 → N_BE_00003 | is subtype of | Hierarchical | 4 |
| ED_BE_00024 | N_BE_00028 → N_BE_00003 | is subtype of | Hierarchical | 4 |
| ED_BE_00025 | N_BE_00027 → N_BE_00028 | grounds | Logical | 4 |
| ED_BE_00029 | N_BE_00024 → N_BE_00023 | dispels | Soteriological | 4 |
| ED_BE_00021 | N_BE_00012 → N_BE_00002 | is subtype of | Hierarchical | 4 |
| ED_BE_00036 | N_BE_00030 → N_BE_00001 | is epithet of | Foundational | 4 |
| ED_BE_00017 | N_BE_00004 → N_BE_00003 | reduced to | Hierarchical | 4 |

**Note:** Edges spanning multiple axioms (e.g., ED_BE_00001 under Axiom 1 and 3) are listed with both assignments. Their primary treatment is in the first-listed axiom.

---

# BIAN Gap Summary

BIAN (Buddhist Insight with No Analogue) designations identify BE concepts that have no formal equivalent in Quantum Measurement. These structural gaps are not defects in either system — they reveal where the two epistemic frameworks diverge at the level of foundational architecture.

| BIAN | BE Concept | Node | Tier (from system_mapping) | Gap Description |
| --- | --- | --- | --- | --- |
| BIAN-1 | Mānasapratyakṣa (Mental perception) | N_BE_00010 | T1.05 | QM has no account of the representational transition between physical detection and symbolic readout. The gap between click and number is outside the formalism. |
| BIAN-2 | Svasaṃvedana (Self-awareness) | N_BE_00011 | T1.06 | The deepest asymmetry. QM has no self-certifying epistemic layer. The measurement problem is the consequence: without reflexive cognition, the registration chain has no formal stopping point. |
| BIAN-3 | Yogipratyakṣa (Yogic perception) | N_BE_00012 | T1.07 | QM has no formal category for observation through a qualitatively different faculty. All observers are formally equivalent; there is no spectrum of observer types. |
| BIAN-4 | Ākāra (Representational form) | — (no node) | T2.01 | Buddhist Epistemology has an explicit theory of representational form as the proximate object of cognition. QM specifies output values but not how output is internally represented. |
| BIAN-5 | Vyavasāya (Determinate judgment) | — (no node) | T2.04 | QM merges physical registration with epistemic commitment into a single undefined event. BE maintains the distinction formally. |
| BIAN-6 | Pramātṛ (Knower / epistemic agent) | — (no node) | — | Pramāṇa formally requires a knower as constitutive condition. QM's measurement operator is defined without reference to any observer. This divergence is foundational. |
| BIAN-7 | Non-conceptual stratum of pratyakṣa | N_BE_00002 | T1.02 | Pratyakṣa is non-conceptual by definition. An eigenvalue readout is already a number — a symbolic, conceptual object. No QM concept maps to pratyakṣa at its deepest pre-conceptual level. |

## Gap Distribution by Axiom

| Axiom | BIAN gaps | Nature of the asymmetry |
| --- | --- | --- |
| 1 — Dependent Arising | BIAN-6 (Pramātṛ) | QM has relational states but no relational knower |
| 2 — Emptiness | — (no BIAN gaps) | Axiom 2 has the strongest QM parallels; contextuality and Bell's theorem structurally mirror emptiness |
| 3 — Consciousness-Only | BIAN-1, BIAN-2, BIAN-4, BIAN-5, BIAN-7 | The deepest concentration of gaps. Consciousness is the condition for manifestation in BE but undefined in QM |
| 4 — Two Truths | BIAN-3 | Only one gap, but significant: QM has no spectrum of observer faculties or epistemic cultivation |

**Structural observation:** Axiom 3 (Consciousness-Only) carries 5 of the 7 BIAN gaps. This is not accidental. The role of consciousness is precisely where Buddhist Epistemology makes its strongest architectural claims and where Quantum Measurement makes its weakest. The four axioms together diagnose the measurement problem as fundamentally an epistemic architecture problem: QM has the relational structure (Axiom 1), the anti-intrinsic-property structure (Axiom 2), and the two-tier descriptive structure (Axiom 4), but lacks the reflexive cognitive architecture (Axiom 3) that would close the system.

---

# Structural Summary

| Axiom | Sanskrit | BE Anchor Nodes | QM Mapping | BIAN Gaps |
| --- | --- | --- | --- | --- |
| 1 | Pratītyasamutpāda | N_BE_00029, N_BE_00021, N_BE_00020, N_BE_00001, N_BE_00019, N_BE_00016, N_BE_00018, N_BE_00017 | Relational QM, no absolute state, entanglement | BIAN-6 |
| 2 | Śūnyatā | N_BE_00025, N_BE_00013, N_BE_00014, N_BE_00022, N_BE_00005, N_BE_00015, N_BE_00008, N_BE_00009 | Contextuality, Bell's theorem, properties-as-relations | — |
| 3 | Vijñaptimātra | N_BE_00011, N_BE_00010, N_BE_00002, N_BE_00006, N_BE_00007, N_BE_00023 | Collapse as registration-state update, measurement as condition | BIAN-1, BIAN-2, BIAN-4, BIAN-5, BIAN-7 |
| 4 | Dvisatya | N_BE_00026, N_BE_00003, N_BE_00027, N_BE_00028, N_BE_00024, N_BE_00012, N_BE_00030, N_BE_00004 | Quantum-classical cut as epistemic boundary | BIAN-3 |

**Final conclusion:** Wavefunction does not describe "where a particle is." Wavefunction describes the structure of possibilities within a given relational network. The quantum-classical boundary is epistemic, not physical. Properties are relations, not intrinsic attributes. Within this interpretive mapping, the epistemically relevant closure is modeled as a registration-state update; this does not by itself deny Standard QM's ρ-side state-update language. This is epistemology, not ontology.

---

## What This Mapping Does NOT Claim / Những gì Mapping này KHÔNG tuyên bố

1. This mapping does not claim identity between Buddhist Epistemology and Quantum Measurement.
2. This mapping does not introduce new canonical QM laws, operators, or postulates unless a separate VVV-QMRF framework document explicitly proposes them.
3. This mapping does not claim that Buddhist Epistemology proves or solves Quantum Measurement; it only identifies structural analogies, contrasts, supports, and gaps.
4. `registration-state update` names the VVV-QMRF K-side update; `detector response` remains only the apparatus physical response.

---

## Schema Validation Checklist / Checklist Kiểm chứng Schema

| Check | Status | RCA note |
|---|---|---|
| Document type declared | Pass | Declared as `mapping` for schema alignment. |
| Source traceability | Pass | Existing source/cross-reference sections provide the trace base. |
| Claim traceability | Review required | Add claim IDs, claim types, source anchors, and boundaries for major claims. |
| Boundary / non-claim guardrail | Pass | Existing boundary/non-claim text limits overclaiming. |
| Validation rule | Pass | Reuse only with source, claim type, and boundary preserved; unresolved items must be marked `TODO(HOTFIX)` before publication use. |
