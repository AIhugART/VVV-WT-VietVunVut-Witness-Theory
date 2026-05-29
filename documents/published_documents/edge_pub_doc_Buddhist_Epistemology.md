# SYSTEM: Buddhist Epistemology

> Derived compact reference: the single RCA source of truth for Buddhist Epistemology node and edge definitions is [system_be_full.md](../../SYSTEM_Buddhist_Epistemology/system_be_full.md). This table preserves the 39 published core edges.

## Published Documents

**Buddhist Epistemology**

| No. | Doc code | Title | Author | Year | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | DOC_BE_01 | [The Buddhist Prama-Epistemology, Logic, and Language: with Reference to Vasubandhu, Dignga, and Dharmakrti](The_Buddhist_Pramana_-Epistemology_Logic_and_Langu.md) | Hari Shankar Prasad | 2023 | *Studia Humana*, Vol. 12:1-2, pp. 21–52. DOI: [10.2478/sh-2023-0004](https://doi.org/10.2478/sh-2023-0004) |

## Key Relationships (extracted from DOC_BE_01)

| No. | Edge code | Source node (Node code) | Target node (Node code) | Relationship | Type | Description |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ED_BE_00001 | Valid cognition (N_BE_00001) | Direct perception (N_BE_00002) | includes | Hierarchical | Pramāṇa encompasses pratyakṣa as one of its two valid sources of knowledge. |
| 2 | ED_BE_00002 | Valid cognition (N_BE_00001) | Inference (N_BE_00003) | includes | Hierarchical | Pramāṇa encompasses anumāna as the second valid source of knowledge. |
| 3 | ED_BE_00003 | Valid cognition (N_BE_00001) | Object of cognition (N_BE_00005) | has as object | Structural | The means of knowing (pramāṇa) is directed toward the object to be known (prameya). |
| 4 | ED_BE_00004 | Valid cognition (N_BE_00001) | Resultant cognition (pramāṇaphala) | produces | Structural | The pramāṇa process culminates in resultant cognition (pramāṇaphala) as its outcome. (Note: pramāṇaphala is a sub-component of N_BE_00001, not a separate node.) |
| 5 | ED_BE_00005 | Direct perception (N_BE_00002) | Particular / Unique mark (N_BE_00013) | apprehends | Epistemic | Pratyakṣa grasps the particular (svalakṣaṇa) directly, without conceptual mediation. |
| 6 | ED_BE_00006 | Inference (N_BE_00003) | Universal / General mark (N_BE_00014) | apprehends | Epistemic | Anumāna operates on the universal (sāmānyalakṣaṇa) through conceptual thought. |
| 7 | ED_BE_00007 | Inference (N_BE_00003) | Sign / Logical reason (N_BE_00016) | operates through | Logical | Inference proceeds via a logical sign (liṅga/hetu) that indicates the probandum. |
| 8 | ED_BE_00008 | Inference (N_BE_00003) | Triple-condition syllogism (N_BE_00018) | validated by | Logical | A valid inference requires the reason to satisfy the three conditions of trairūpya. |
| 9 | ED_BE_00009 | Sign / Logical reason (N_BE_00016) | Thesis (N_BE_00017) | qualifies | Logical | The logical reason (hetu) must be a property of the thesis subject (pakṣadharmatva). |
| 10 | ED_BE_00010 | Sign / Logical reason (N_BE_00016) | Pervasion (N_BE_00019) | requires | Logical | The sign must have pervasion (vyāpti) with the probandum for inference to succeed. |
| 11 | ED_BE_00011 | Pervasion (N_BE_00019) | Essential relation (N_BE_00021) | grounded in | Logical | Dharmakīrti grounds universal pervasion in svabhāvapratibandha (essential relation). |
| 12 | ED_BE_00012 | Essential relation (N_BE_00021) | Causal efficacy (N_BE_00022) | has as basis | Ontological | The causal type (tadutpatti) of essential relation rests on arthakriyā (causal efficacy). |
| 13 | ED_BE_00013 | Conceptual construction (N_BE_00008) | Universal / General mark (N_BE_00014) | operates on | Epistemic | Vikalpa/kalpanā applies names and classes to the universal (sāmānyalakṣaṇa). |
| 14 | ED_BE_00014 | Non-conceptual perception (N_BE_00009) | Particular / Unique mark (N_BE_00013) | apprehends | Epistemic | Nirvikalpaka pratyakṣa grasps the bare particular without conceptual overlay. |
| 15 | ED_BE_00015 | Non-conceptual perception (N_BE_00009) | Conceptual construction (N_BE_00008) | contrasted with | Oppositional | Pure perception is defined by the absence of kalpanā (mental construction). |
| 16 | ED_BE_00016 | Exclusion (N_BE_00015) | Inference (N_BE_00003) | is linguistic variant of | Logical | Dignāga reduces verbal cognition (apoha) to a variety of inference (anumāna). |
| 17 | ED_BE_00017 | Testimony (N_BE_00004) | Inference (N_BE_00003) | reduced to | Hierarchical | Dignāga rejects āgama/śabda as an independent pramāṇa, treating it as inference. |
| 18 | ED_BE_00018 | Mental perception (N_BE_00010) | Direct perception (N_BE_00002) | is subtype of | Hierarchical | [uncertain] Mānasa pratyakṣa is direct perception through mental consciousness, not external senses. (Note: nguồn dòng 185 xếp mano-vijñāna vào hệ 8 thức (vijñāna/consciousness), không gọi là phân nhánh của tri giác (pratyakṣa). Category N_BE_00010 đã là "Type of consciousness".) |
| 19 | ED_BE_00019 | Self-awareness (N_BE_00011) | Direct perception (N_BE_00002) | is subtype of | Hierarchical | [uncertain] Svasaṃvedana is the reflexive awareness of consciousness itself, a form of direct perception. (Note: N_BE_00011 không trực tiếp từ nguồn này.) |
| 20 | ED_BE_00020 | Mental perception (N_BE_00010) | Self-awareness (N_BE_00011) | entails | Structural | [uncertain] Mental perception includes the reflexive dimension by which mind knows its own states. (Note: N_BE_00011 không trực tiếp từ nguồn này.) |
| 21 | ED_BE_00021 | Yogic perception (N_BE_00012) | Direct perception (N_BE_00002) | is subtype of | Hierarchical | [uncertain] Yogipratyakṣa is supra-ordinary direct perception arising from meditative cultivation. (Note: N_BE_00012 không trực tiếp từ nguồn này.) |
| 22 | ED_BE_00022 | Yogic perception (N_BE_00012) | Emptiness (N_BE_00025) | realizes | Epistemic | [uncertain] Yogic perception directly sees ultimate reality (śūnyatā) beyond conceptual mediation. (Note: N_BE_00012 không trực tiếp từ nguồn này.) |
| 23 | ED_BE_00023 | Inductive reasoning (N_BE_00027) | Inference (N_BE_00003) | is subtype of | Hierarchical | Svārthānumāna is "inference for oneself," the private inferential cognition. |
| 24 | ED_BE_00024 | Deductive reasoning (N_BE_00028) | Inference (N_BE_00003) | is subtype of | Hierarchical | Parārthānumāna is "inference for others," the syllogistic communication of knowledge. |
| 25 | ED_BE_00025 | Inductive reasoning (N_BE_00027) | Deductive reasoning (N_BE_00028) | grounds | Logical | The proponent's private inference (svārthānumāna) grounds the public syllogism (parārthānumāna). |
| 26 | ED_BE_00026 | Necessary relation (N_BE_00020) | Pervasion (N_BE_00019) | is precursor of | Logical | Vasubandhu's avinābhāva (not-being-without) is the earlier formulation of vyāpti. |
| 27 | ED_BE_00027 | Ignorance (N_BE_00023) | Erroneous cognition (N_BE_00006) | causes | Causal | Avidyā generates mistaken apprehension of reality, including erroneous cognition (bhrānti). (Implied from source framework; not explicitly stated.) |
| 28 | ED_BE_00028 | Ignorance (N_BE_00023) | Doubt (N_BE_00007) | gives rise to | Causal | [uncertain] Avidyā produces saṃśaya (doubt), the state of indecision about reality. (Note: N_BE_00007 không trực tiếp từ nguồn này.) |
| 29 | ED_BE_00029 | Wisdom (N_BE_00024) | Ignorance (N_BE_00023) | dispels | Soteriological | Prajñā/paññā is the penetrating insight that removes avidyā, the root of suffering. (Implied from three trainings framework; not explicitly stated.) |
| 30 | ED_BE_00030 | Wisdom (N_BE_00024) | Emptiness (N_BE_00025) | realizes | Epistemic | Prajñā is the cognition that directly realizes śūnyatā, the absence of inherent existence. (Implied from source framework; not explicitly stated.) |
| 31 | ED_BE_00031 | Emptiness (N_BE_00025) | Two truths (N_BE_00026) | is ultimate aspect of | Ontological | Śūnyatā is the paramārthasat (ultimate truth) dimension of the two-truth schema. |
| 32 | ED_BE_00032 | Particular / Unique mark (N_BE_00013) | Causal efficacy (N_BE_00022) | possesses | Ontological | Only the particular (svalakṣaṇa) has arthakriyā — the power to produce effects, the criterion of reality. |
| 33 | ED_BE_00033 | Universal / General mark (N_BE_00014) | Causal efficacy (N_BE_00022) | lacks | Ontological | The universal (sāmānyalakṣaṇa) has no causal efficacy and is not ultimately real. |
| 34 | ED_BE_00034 | Momentariness (N_BE_00029) | Causal efficacy (N_BE_00022) | supports | Ontological | Kṣaṇabhaṅgavāda (momentariness) conceptually supports arthakriyā: only momentary entities can be causally efficacious. (Implied from process philosophy framework; not explicitly stated.) |
| 35 | ED_BE_00035 | Momentariness (N_BE_00029) | Particular / Unique mark (N_BE_00013) | characterizes | Ontological | The particular is momentary — "a moment disappears as soon as it appears without duration." |
| 36 | ED_BE_00036 | Means of valid cognition (N_BE_00030) | Valid cognition (N_BE_00001) | is epithet of | Foundational | Pramāṇabhūta is the Buddha as possessor of valid method and cognition. |
| 37 | ED_BE_00037 | Doubt (N_BE_00007) | Inductive reasoning (N_BE_00027) | motivates | Psychological | [uncertain] Saṃśaya (doubt) or jijñāsā (desire to know) provides the motivation for svārthānumāna. (Note: N_BE_00007 không trực tiếp từ nguồn này.) |
| 38 | ED_BE_00038 | Direct perception (N_BE_00002) | Conceptual construction (N_BE_00008) | is free from | Exclusionary | Dignāga defines pratyakṣa as "devoid of mental construction" (kalpanāpodham). |
| 39 | ED_BE_00039 | Sign / Logical reason (N_BE_00016) | Necessary relation (N_BE_00020) | requires | Logical | The sign must have avinābhāva (inseparable connection) with the probandum. |
