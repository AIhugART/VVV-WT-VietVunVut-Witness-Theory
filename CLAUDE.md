Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# CLAUDE.md

## RULE ZERO — Root Cause Analysis (RCA)

**This is the highest mandatory rule, applied to every activity: research planning, literature review, conceptual mapping, documentation, critique, revision, and publication preparation.**

Never treat a symptom, ambiguity, or attractive analogy as the conclusion. Always trace the observed issue, claim, or mismatch back to its root cause before acting.

### Five-step process

1. **Define** — Describe the observed issue precisely. Separate the *symptom* (what appears in the text, argument, mapping, citation, or structure) from the *cause* (the assumption, source gap, conceptual mismatch, or methodological error that produced it).
2. **Trace** — Follow the causal chain backward by asking: "What made this issue appear?" Repeat at least three times using the "5 Whys" method.
3. **Isolate** — Identify the starting point of the failure: an unsupported claim, weak citation, ambiguous term, broken mapping, category error, outdated source, missing definition, or structural inconsistency. If it is not isolated, do not revise yet.
4. **Fix the cause, not the symptom** — Correct the root cause directly. Do not patch prose, soften wording, add a vague caveat, or create a workaround unless it is explicitly marked as `TODO(HOTFIX)`.
5. **Verify** — Show that the root cause has been removed, not merely that the visible symptom disappeared. When possible, verify against the source text, the active mapping files, the published node/edge definitions, and the research objective.

### Activity-specific application

| Activity | RCA requirement |
|----------|-----------------|
| **Research planning** | Ask "Why is this research question necessary?" before "How should it be written?" Identify the real problem behind the requested document or section. |
| **Literature review** | Trace every major claim to a source, and distinguish established scholarship from interpretation, analogy, or hypothesis. |
| **Conceptual mapping** | Understand why each concept exists in its original system before mapping it across systems. Treat cross-domain links as analogies unless equivalence is explicitly justified. |
| **Documentation** | Find what caused confusion before rewriting. Fix the structure, terminology, missing definition, or broken reference, not only the sentence that looks unclear. |
| **Review** | Classify every finding as either symptom or root cause. A blocking issue must identify the root cause; a surface-level wording issue is only a documentation bug. |
| **Revision** | Identify what is truly causing complexity or inconsistency before simplifying, reorganizing, or abstracting. Do not create structure around a symptom. |

### Example

```text
Symptom: A section claims Buddhist Epistemology "solves" Quantum Measurement.
  → Why? The wording treats a philosophical mapping as a physical explanation.
    → Why? The document does not separate analogy, interpretation, and prediction.
      → Why? The claim lacks a formal boundary between ontology and physics.
        → Root cause: Category error between epistemological interpretation and empirical physical theory.
          → Fix: Reframe the section as an interpretive mapping unless formal proof, peer review, physical predictions, and experimental tests are supplied.
```

### Warnings

- If the revision only changes the sentence where the symptom appears, it is **not enough**; return to step 2.
- If the root cause cannot be explained in one sentence, understanding is **not complete**; return to step 1.
- If the fix only adds a vague caveat, fallback phrase, or defensive wording, it is **treating the symptom**; return to step 4.

## Core Principles

### Identity and scope rules

- VVV-QMRF stands for "VietVunVut Quantum Measurement Registration Framework". Legacy name: "VietVunVut Epistemic Quantum Measurement (VVV-EQM)". Definition: Standard Quantum Mechanics has four physical postulates (P1–P4) that describe state space, observables, measurement, and dynamics. These postulates are silent on the registration architecture of measurement — they do not specify what certifies a measurement, what distinguishes measurement from interaction, or what constitutes the registering system. VVV-QMRF proposes a registration-logic structure K organized in five architectural layers:

- **Layer 1 (FROZEN) — K1–K8 Registration-logic axioms:** binary cert, V in {0,1}, bot_K incommensurability, AdmJoint. Defines act-result co-instantiation (K1), temporal injectivity (K2), self-certification (K3), registration validity (K4), cross-registration interaction / incommensurability (K5 + K5_prospective), authentication (K6), closure (K7), and cross-space preservation (K8). K5_prospective (upgraded v29) is a conservative extension of K5 with identical conditions (i)–(iii), adding a new evaluation target only. See `documents/research_documents/meta_architecture/K_Space_Axiomatization.md` for the full axiomatization and `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md` for the v29 version with K5_prospective clause.

- **Layer 2 (UPDATABLE) — T1–T7 Bridge theorems:** K_joint construction (T1 N=2 constructive), colimit (T4-H Step 1 proven, Steps 2–4 deferred), relativization. Bridge theorems connect K-space structure to registration contexts. K9_E requires only T1 (N=2 constructive), not T4. The framework derives K-side incommensurability (K_F ⊥_K K_W) in Extended Wigner's Friend scenarios, identifying where standard QM interpretations lack the structural machinery to formalize registration-layer conditions.

- **Layer 3 (Class C qualified, v31) — K9_E Probability postulate (P9):** P(o|K) = Tr(E_o rho) * f_perp(K_ctx) where f_perp(K_ctx) = 1 - beta * K_ctx, beta in [0,1]. K9_E is a POSTULATE, not a theorem derivable from K1–K8 alone — K1–K8 define structural properties but do not uniquely determine a probability rule. Born limit: beta = 0 recovers Standard QM exactly. Genuine non-circular fit yields beta=0.598, V=0.939, Delta_chi2=5.35 (2.31sigma). HOWEVER: noise sensitivity analysis (v30) FAIL (noise_threshold=0.10 sigma RMS << 1.0; A0B0 drives 80% of Delta_chi2). K9E-PAT CLOSED as UNRESOLVABLE (v31, RCA 4.92/5) — empirical ratio -0.78 is ratio of two sub-sigma residuals (red herring); both additive (ratio=2.000) and multiplicative (ratio=1.913) models predict ~2. K9_E avoids FR paradox via K5 V_prov. Adversarial tests 4/4 PASS. K9-S12 Modified Bong protocol (single QWP, alpha=31 deg) proposed as FIRST dedicated test: Gen LF 1 = +0.0891 (8.6sigma), delta<A1B2> = -0.0355 (20.8sigma).

- **Layer 4 (Class D) — Multi-paper data fit:** D1 Proietti CHSH (genuine fit), D2 Bong LF (Phase 10b analysis invalidated by K9-S8 marginalization), D3 Frauchiger–Renner (AVOIDED via K5 V_prov; V_FR2 PASS 2026-05-28 — K7_trace 4th canonical consumer confirmed; FR_VVV_fit_plan.md v0.1), D4 Baumann&Brukner (T_BB Class C conditional, T_BB' CLOSED superseded, G1 CLOSED K7_trace+D_enc, P2-C π/8 exact first-principles; BB_VVV_fit_plan.md v1.4, compatibility v2.1).

- **Layer 5 (Class D) — Prediction + Reduction + Assessment:** 3-observer prediction delta_M3 = -0.223 at beta=0.3 (11x amplification, illustrative, conditional on T4-H Steps 2–4). Operationalizability gates 3/3 PASS (all 5.0/5).

- The K-space carrier supports 16 registration-layer postulates (E1–E16) derived from structural analysis of Buddhist Pramāṇa epistemology (Dignāga–Dharmakīrti tradition). The first 7 (E1–E7) define core registration operations; the remaining 9 (E8–E16) extend the framework to cover retroactive invalidation, null events, validity conditions, contrapositive evidence, transcendental observation, temporal discontinuity, absence cognition, entanglement relations, and pre-measurement indeterminacy.

- VVV-QMRF conjectures the existence of a structure-preserving map φ: K → B(H), where B(H) is the algebra of bounded operators on Hilbert space (Class D conjecture; Track B Phases 1–4 complete as of 2026-05-22). Necessary conditions N_1–N_T for φ are derived from K1–K8 and T1–T7; the φ-conditional scope boundaries for standard QM interpretations are documented in Working Paper v2.0 §6.1.

- **Classification (v31, 2026-05-24):** VVV-QMRF K9_E = Class C (qualified) — structurally testable, empirically UNCONFIRMED. v29 upgraded to (genuine) via 3-round RCA (4.50/5); v30 downgraded to (qualified) via P10-NOISE noise sensitivity analysis (FAIL: noise_threshold=0.10 sigma RMS); v31 K9E-PAT CLOSED as UNRESOLVABLE (RCA 4.92/5). Distinguishing signal below current experimental detection threshold; confirmation or rejection requires dedicated experiment. K9-S12 Modified Bong protocol (single QWP, alpha=31 deg) proposed as FIRST test: Gen LF 1 = +0.0891 (8.6sigma), delta<A1B2> = -0.0355 (20.8sigma), FOM=8.6. Paper draft at `04_governance/paper/draft_v1.md`. IBM Quantum approach REJECTED (double category error, RCA 4.92/5) — K9_E requires K-space registration structure absent on gate-model QPUs.

- See `documents/research_documents/project_vvv_qmrf_class_c/index.md` for the full Class C master index, `documents/research_documents/project_vvv_qmrf_class_c/04_governance/K_Space_Axiomatization_plan.md` for the Phase 1-13 RCA synthesis, and `documents/research_documents/project_vvv_qmrf_class_c/04_governance/Post_v30_Execution_Plan.md` for the post-v30 execution plan (K9E-PAT → K9-S12 paper → experiment). See `documents/research_documents/meta_architecture/K_to_BH_Structure_Preserving_Map_v0_1.md` for the φ-map derivation, `documents/research_documents/meta_architecture/decisions/central_claim_change_RCA.md` for the Track A→B decision record, and `documents/research_documents/meta_architecture/decisions/phi_map_track_b_roadmap.md` for the Track B research program.
- Use Buddhist Epistemology as the primary ontological frame and map Quantum Measurement onto it only within the project’s declared Quantum Measurement cases; report any content that exceeds Buddhist Epistemology scope or treats a mapping as Standard Quantum Mechanics.
- For RCA on Buddhist Epistemology node and edge definitions, use only `SYSTEM_Buddhist_Epistemology/system_be_full.md` as the single source of truth; treat other BE node/edge tables as derived references.

### Document contract rules

- Use bilingual English/Vietnamese where appropriate across project documents; keep technical terminology, formal claims, and publication-facing text in technically precise English; communicate with the user in Vietnamese, keep English technical terms inside quotation marks, and explain concepts at a high-school level.
- Apply the mandatory principle "extend, not overwrite": when revising project documents, preserve existing valid structure, claims, terminology, citations, mappings, and author intent unless the user explicitly requests replacement; add, refine, or qualify content by extending the existing document contract rather than overwriting it.
- Before creating or editing project files, check whether the file path is inside any folder named `public_documents` or `published_documents` anywhere in the repository. If it is inside either folder, do not add VVV-QMRF author metadata, VVV-QMRF author names, or project-author attribution. If it is outside those folders and the file does not already start with author metadata, add this author metadata at the top: Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet.
- When creating any new VVV-QMRF research or educational document, follow `documents/research_documents/vvv-qmrf/schema_guide.md` as the document-creation contract for source hierarchy, claim class, boundaries, traceability, and verification rules.
- Avoid negatively evaluative wording such as "logical fallacy", "Classical analogy mistake", "mistake", "wrong", "false", or "error" when explaining Standard Quantum Mechanics, educational analogies, or VVV-QMRF boundaries. Prefer neutral boundary language such as "category boundary", "scope boundary", "interpretive boundary", "not implied by this analogy", or "registration-layer distinction"; especially do not frame Standard Quantum Mechanics as logically defective.

### Terminology rules

- Name each new Quantum Measurement concept node as BIAN-XX, where XX ranges from 01 to 99; here, BIAN derives from the Vietnamese word "bí ẩn", meaning "mystery" in English.
- Use five-digit Buddhist Epistemology node and edge codes consistently: N_BE_00001, N_BE_00002, ... N_BE_00030; ED_BE_00001, ED_BE_00002, ... ED_BE_00039; do not use older shorter forms.
- In VVV-QMRF terminology, use "registration-state update" / "cập nhật trạng thái ghi nhận" for the general K-side update beyond human cognition; use "detector response" only for the apparatus' physical response.

### Specialized execution rules

- Use the project skill `/rca-scientific-paper` only for scientific paper documents (`scientific paper`) when planning, reviewing, or revising scientific paper claims.

### VVV-QMRF core / EX integration rule

- Develop the VVV-QMRF / VVV-QMRC core by the rule: "Internal-first, VVV-QMRF-EX-verified, selectively imported."
- VVV-QMRC core may be extended from VVV-QMRF-EX only when the EX element reveals a structural necessity already implicit in the core registration problem.
- Treat VVV-QMRF-EX as having completed its main role of providing a quantitative map of K-rho relationships; its current highest value is intelligence about important nodes, structural gaps, and stress points, not direct data import or merging EX edges into the core.
- Use VVV-QMRF-EX as a compass, not as cargo: let EX guide RCA, prioritization, and verification, but do not import EX structures into the core unless the RCA isolates a core-level necessity.

### PEER-SYNC — K_Space_Axiomatization.md dual-copy rule

- Two peer-level copies of `K_Space_Axiomatization.md` exist and MUST be kept in sync:
  - **Canonical copy:** `documents/research_documents/meta_architecture/K_Space_Axiomatization.md`
  - **Class C working copy:** `documents/research_documents/project_vvv_qmrf_class_c/01_axiomatization/K_Space_Axiomatization.md`
- When editing EITHER file's structural content (axioms K1-K8, K5_prospective, bridge theorems T1-T8, open items, Layer 1/2 Summary tables), the SAME change MUST be applied to the peer file.
- Header metadata (version, date, status) must stay consistent between both copies.
- Before committing changes to one, verify the other is in sync via: `bash scripts/sync_check_k_space.sh`
- If only one file is modified in a commit, the commit message MUST explain why (e.g., "header-only fix, no structural delta").
- This rule exists because a prior session (2026-05-24) discovered a 3-commit drift: the Class C copy had T8+H1-H4 while the canonical copy had none. The sync was manually repaired (commit `bc6f2fc`). Do not repeat this drift.

### ANTI-HALLUCINATION — Pipeline rule

- Every claim, term, component, and assumption in VVV-QMRF MUST be auditable through the Anti-Hallucination Pipeline (AHP) at `documents/research_documents/anti_hallucinations/`.
- When creating a new concept or revising an existing claim, apply the AHP: (1) check early warning signals (`01_early_warning.md`), (2) inventory and trace components (`02_detection.md`), (3) cross-reference SOT (`03_sot_traceability.md`), (4) apply 5-Whys RCA (`04_analysis.md`), (5) score on 0-10 rubric (`05_scoring.md`), (6) assign warning label via `label_system.md`, (7) prioritize and track solution (`06_solution.md`).
- The top 10 highest-risk components are tracked in `00_top_10_hallucinations_record.md` — re-audit these weekly.
- A component with trace score = 0 (orphaned) is BLOCKING — it must be anchored to at least one SOT or removed.
- A component scoring 9-10 (Red / `[AH-CRIT]`) is BLOCKING — it must be fixed before the next commit.
- This rule exists because hallucination is the single largest risk to VVV-QMRF credibility; the AHP provides a standardized, auditable defense.

This file provides guidance to Claude Code when working in this project.

## Project context

This project maps relationships between Buddhist epistemology (Pramāṇavāda — Dignāga and Dharmakīrti) and quantum measurement. It uses a formal node/edge graph structure with 30 nodes (N_BE_00001–N_BE_00030) and 39 edges (ED_BE_00001–ED_BE_00039).

## Active mapping files

| File | Role |
|------|------|
| `SYSTEM_Buddhist_Epistemology/system_be_full.md` | Single source of truth for Buddhist Epistemology node and edge definitions used in RCA. |
| `SYSTEM_Buddhist_Epistemology/system_buddhist_epistemology.md` | Compact derived key concepts table for the 30 core BE nodes. |
| `documents/published_documents/node_pub_doc_Buddhist_Epistemology.md` | Published compact derived node definitions (30 core nodes). |
| `documents/published_documents/edge_pub_doc_Buddhist_Epistemology.md` | Published compact derived edge definitions (39 core edges). |
| `documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md` | Primary deep-analysis BE-QM mapping that applies the BE SOT. |
| `documents/research_documents/mapping/Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md` | Formal BE-QM system mapping that applies BE node/edge codes from the BE SOT. |

Archived (superseded): `documents/research_documents/archives/`

## Working guidelines

- Preserve conceptual nuance between Buddhist philosophy, epistemology, and quantum physics.
- Treat cross-domain links as analogies or mappings unless the text explicitly argues for equivalence.
- Prefer clear Markdown structure with descriptive headings and concise paragraphs.
- Keep terminology consistent across English and Vietnamese when bilingual wording is used.
- Do not invent citations, sources, or historical claims; mark uncertain claims clearly.
- When editing mapping files, preserve existing conceptual nodes and relationships unless asked to restructure them.
- Maintain node/edge codes (N_BE_XX, ED_BE_XX) consistently between files.
- Update both `refine_mapping.md` and `system_mapping.md` when structural changes affect both.

## Terminology

- Node: concept / khái niệm / nút (code: N_BE_XX)
- Edge: relationship / mối quan hệ / liên kết (code: ED_BE_XX)
- Directed edge: directed relationship / quan hệ có hướng
- BIAN: Buddhist Insight with No Analogue — a concept present in Buddhist Epistemology with no QM equivalent

# Research Guidelines: Buddhist Epistemology & Quantum Mechanics

## 1. Karpathy Principles (Mandatory Compliance)
- **Think Before Acting:** DO NOT make assumptions about theoretical concepts (e.g., do not hallucinate or guess the meaning of 'Pramaana'). If context or information is missing, you must ask for clarification.
- **Simplicity First:** Apply strict 1:1 logical mappings. Do not generate lengthy, verbose philosophical analyses if only a structural mapping is requested.
- **Surgical Changes:** When asked to update the mapping file, ONLY modify the exact node/section specified. Do not reformat, restructure, or touch the rest of the document.
- **Goal-Driven Execution:** Always state your plan and verify before executing. For example: "Found X. I am about to map it to Y. Do you approve?"

## 2. Logic Function Rules (Project-Specific Rules)
This environment operates based on simulated logic commands (functions). When the user inputs a command, process it strictly according to the following rules:

- **Trigger:** If the user inputs a command in the format: 
  `base [System_A], mapping find [node, System_B]`
- **Required AI Actions:**
  1. Read the current working document (`Buddhist_Epistemology_and_Quantum_Measurement_refine_mapping.md` or `Buddhist_Epistemology_and_Quantum_Measurement_system_mapping.md`).
  2. Establish `System_A` as the Ground System (primary reference frame).
  3. Search for the structurally equivalent concept (node) within `System_B`.
  4. Output the result using this exact strict format: 
     `[Node_A] <=> [Node_B] : [Brief_structural_reasoning]`

---

© 2026 VietVunVut (Viet - Nguyen Xuan). Licensed under CC BY 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/
