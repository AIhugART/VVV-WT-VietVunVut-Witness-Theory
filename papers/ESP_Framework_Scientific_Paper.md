Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

# ESP Framework
## Epistemic-Structural-Presentational Framework for Scientific Paper Writing
### For Independent Authors Without Institutional Affiliation Submitting to Peer-Reviewed Journals

---

> **Core Premise**
>
> An independent author without institutional affiliation faces two simultaneous threats: the reviewer will not trust a claim larger than its evidence, and the reviewer will not read carefully enough to find the evidence if the paper fails to earn attention in the first paragraph. ESP Framework addresses these threats in sequence — first by disciplining what you claim (Epistemic layer), then by building how you argue it (Structural layer), then by sharpening how you present it (Presentational layer).

## Scope and Evidence Status

ESP is a disciplined writing framework for planning, drafting, and auditing scientific papers. It is not an empirically validated method and does not claim to guarantee acceptance, improve citation outcomes, or prove the truth of a paper's claims. It aims to reduce avoidable epistemic, structural, and presentational errors by making claim boundaries explicit before prose is written.

---

## Framework Architecture

```
ESP = E + S + P

E — Epistemic Layer    → What am I allowed to claim? (Before writing)
S — Structural Layer   → How do I build the argument? (While writing)
P — Presentational     → How do I make it readable? (Before submitting)
```

Each layer has its own phase, its own tools, and its own checklist. They run in order. Do not skip to S before completing E. Do not submit before completing P.

---

# LAYER E — EPISTEMIC LAYER
## Discipline the Claim Before Writing Anything

**Purpose:** To identify the root cause of your research problem, locate the exact level of your claim, and set the boundary of what the paper will and will not assert.

**When to run:** Before drafting any section, including the abstract.

---

### E.1 — Five-Layer Root Cause Analysis (RCA Stack)

Run this stack on your central claim before writing.

| Layer | Question to answer |
|---|---|
| L1 — Phenomenon | What is actually observed or experienced? |
| L2 — Proximate Cause | What directly produces this phenomenon? |
| L3 — Underlying Mechanism | What produces the proximate cause? |
| L4 — Root Cause / New Principle | What hidden assumption must change? |
| L5 — Generalization | Where else may this apply, and within what limits? |

**Rule:** A claim is not ready to write until all five layers are answered in one paragraph or less.

**Template:**

```
Phenomenon:
[What is observed or unresolved in the field?]

Proximate Cause:
[What directly produces this gap or problem?]

Underlying Mechanism:
[What deeper structure produces the proximate cause?]

Root Cause / New Principle:
[What one assumption, if changed, resolves the problem?]

Generalization:
[Where does this apply? State the scope explicitly and conservatively.]
```

---

### E.2 — Three-Why Drill

For every major claim in the paper, drill backward at least three times.

```
Claim:
[State the claim in one sentence.]

Symptom:
[What is the visible problem this claim addresses?]

Why 1:
[What directly makes this symptom appear?]

Why 2:
[What deeper mechanism produces Why 1?]

Why 3:
[What hidden assumption makes that mechanism possible?]

Root Cause:
[One sentence. If it cannot be stated in one sentence, the claim is not ready.]

Fix:
[What exactly must change — a definition, a mapping, a sentence, a framing?]

Boundary:
[What does this claim NOT assert?]

Verification:
[What source, data, or logic confirms the fix?]
```

---

### E.3 — Claim Ladder

Locate your claim on this ladder before writing. Do not write above the level your evidence supports.

| Level | Description | Condition for use |
|---|---|---|
| Analogy | Structural resemblance between domains | Always safe; label it as analogy |
| Interpretive Mapping | Cross-domain reading of a concept | Safe with clear definitions |
| Ontological Framework | New explanatory frame without physical mechanism | Use with strict scope and definitions |
| Physical Model | Formal mathematical mechanism | Only if equations and derivations are provided |
| Empirical Solution | Experimental replacement of prior theory | Only if data and tests are provided |

**For a first paper with no institutional backing:** Stay in Analogy, Interpretive Mapping, or Ontological Framework. Do not write at Physical Model or Empirical Solution level unless the formal apparatus is complete.

---

### E.4 — Epistemic Status of the Title

Before writing the title, answer:

```
Main claim of the paper: [one sentence]
Level of evidence: [theoretical / analogical / experimental / proven]
Epistemic status: [conjecture / model / framework / proof / observation]
```

Then choose the correct title register:

| Evidence level | Title form |
|---|---|
| Theoretical conjecture | "Toward a...", "A Heuristic Approach to...", "On the Possibility of..." |
| Interpretive framework | "A Framework for...", "Reinterpreting X in Terms of Y" |
| Experimental support | "Evidence for...", "X as a Function of Y: Experimental Results" |
| Proven result | State the result directly without hedging |

**Rule:** Do not hedge a proven result. Do not assert an unproven conjecture as fact. Match the title exactly to the strongest defensible claim.

---

### E.5 — Mandatory Boundary Statement

Every paper must contain at least one explicit boundary statement in the introduction. Write it before drafting anything else.

```
This paper does not claim: [state what the paper explicitly does not assert]
This paper claims: [state what the paper does assert, at the correct claim level]
```

**Examples of correct form:**
- "This paper does not propose a physical mechanism for X. It proposes an interpretive framework for reexamining the structure of X."
- "This paper does not replace prior theory Y. It examines whether framework Z is consistent with the assumptions underlying Y."

---

### E.6 — Epistemic Layer Checklist

Complete before moving to Layer S.

```
[ ] RCA Stack completed — all five layers answered
[ ] Three-Why drill completed for every major claim
[ ] Claim located on Claim Ladder
[ ] Title epistemic status identified and matched
[ ] Boundary statement written ("does not claim / does claim")
[ ] Each claim classified as: analogy / interpretation / ontology / model / empirical
```

---

# LAYER S — STRUCTURAL LAYER
## Build the Argument Before Writing the Prose

**Purpose:** To organize the paper as a sequence of resolved sub-questions, each answering one thing and building on the previous. This is the architecture of the argument.

**When to run:** After Layer E is complete. Before drafting prose.

---

### S.1 — Open with Contradiction, Not Definition

The first paragraph must present a concrete tension, not background theory.

**Structure:**

```
Paragraph 1: The phenomenon as observed or experienced.
Paragraph 2: What current theory or understanding predicts about it.
Paragraph 3: The specific, named contradiction between the two.
Paragraph 4: The paper's approach to resolving it.
```

**Rule:** The contradiction must be concrete enough that an intelligent non-specialist can feel why it is strange. If a definition or literature survey appears in paragraph one, restructure.

**LLM Prompt for this step:**

```
Here is my paper's core finding: [FINDING]
Here is what prior work predicted: [PRIOR EXPECTATION]
Write an opening paragraph that frames this as a productive contradiction,
without using jargon specific to [FIELD].
```

---

### S.2 — Sub-Question Architecture

Before drafting, list every sub-question the paper must answer to establish its main claim. Assign one section per sub-question.

**Step 1:** Write the thesis in one sentence.

**Step 2:** List 6 to 9 sub-questions in the order they must be answered. Each answer should make the next sub-question possible.

**Step 3:** Write a declarative section title for each sub-question.

**Section title templates:**

```
"Why [existing approach] cannot account for [phenomenon]"
"What [concept] means under [new framework]"
"How [framework] maps onto [domain]"
"Testing the proposal against [case or counterargument]"
"Implications beyond [primary domain]"
"What this framework does not resolve"
```

**LLM Prompt for this step:**

```
Here is my paper's thesis: [THESIS]
List 6–9 sub-questions that must be answered to fully establish this thesis,
ordered so each answer builds on the previous.
Then suggest a declarative section title for each.
```

---

### S.3 — Section Internal Structure

Each section follows this internal sequence:

```
1. State the sub-question this section answers.
2. Present the current best answer or prior assumption.
3. Identify what this section adds, changes, or reframes.
4. Present the argument or evidence.
5. State the answer to the sub-question in one or two sentences.
6. Connect to the next section in one sentence.
```

Section length: 300 to 600 words per section when possible. If a section exceeds 800 words, consider whether it contains two sub-questions and split accordingly.

---

### S.4 — Literature Review as Lineage, Not Decoration

For every cited source, name specifically what you are borrowing.

**Correct form:**

```
[Author] established that [specific claim or result].
This paper extends that result by [specific extension].
```

**Incorrect form:**

```
Previous work has explored this area [1, 2, 3, 4, 5].
```

Label every claim in the literature review as one of:

```
[established scholarship] — consensus in the field
[contested scholarship] — debated, with opposing views
[project interpretation] — the author's reading of prior work
[analogy] — structural resemblance, not equivalence
[hypothesis] — proposed but not yet tested
```

**Rule:** Do not cite to demonstrate breadth. Cite only what your argument directly depends on.

---

### S.5 — Conclusion Architecture

The conclusion must resolve the opening contradiction and distinguish between levels of certainty.

```
1. Restate the opening contradiction.
2. Summarize how the paper resolved it.
3. State explicitly what has been proven / demonstrated / modeled / suggested.
4. State the single most important implication not yet tested.
5. Pose the next-order question this paper opens.
```

**LLM Prompt for this step:**

```
Here are my paper's main findings: [FINDINGS]
Distinguish which of these are: (a) formally proven, (b) empirically supported,
(c) theoretically implied but not yet tested.
Write a conclusion paragraph that treats each category with appropriate confidence.
```

**Rule:** The conclusion must end with a specific next question, not a generic call for further research.

---

### S.6 — Structural Layer Checklist

Complete before moving to Layer P.

```
[ ] First paragraph presents contradiction, not definition or literature
[ ] Thesis stated in one sentence
[ ] 6–9 sub-questions listed in logical order
[ ] One section assigned per sub-question
[ ] Every section title is declarative or question-form, not a vague noun
[ ] Literature review labels every claim by type
[ ] Every citation names specifically what is borrowed
[ ] Conclusion distinguishes proven / supported / implied findings
[ ] Conclusion ends with a specific next question
[ ] Opening contradiction is explicitly resolved in the conclusion
```

---

# LAYER P — PRESENTATIONAL LAYER
## Make It Readable Before Submitting

**Purpose:** To ensure every formal element is preceded by a plain-language statement, and to audit the paper for overclaimed conclusions, hedged arguments, and missing boundaries.

**When to run:** After a complete draft exists. Before submission.

---

### P.1 — Intuition Before Formalism

For every equation, diagram, formal definition, or proof, provide a plain-language statement before the formal element.

**Internal structure for each formal element:**

```
1. State the conceptual claim in plain language.
2. State what needs to be quantified or formalized and why.
3. Introduce the equation or formal definition.
4. Walk through each term's meaning in plain language.
5. State what the formal result implies beyond its algebra or structure.
```

**Test:** Remove all equations and formal definitions. Does the argument still make logical sense? If yes, the structure is correct. If no, the formal elements are doing work that prose should do.

**LLM Prompt for this step:**

```
Here is an equation from my paper: [EQUATION]
Explain it in two sentences using no mathematical notation,
as if speaking to an intelligent non-specialist.
Then identify which term is doing the most important conceptual work.
```

---

### P.2 — Argument vs. Conclusion Discipline

Apply these two rules simultaneously and never reverse them.

**Rule 1 — Argue boldly:** In the body of the paper, state each logical inference directly. Do not hedge a valid deduction with "it might be possible that" or "one could potentially argue." If the logic is sound, state it as sound.

**Rule 2 — Conclude carefully:** In the conclusion and abstract, distinguish what has been shown from what has been suggested from what remains to be tested. Use the language of the correct epistemic level.

**Language guide:**

| Use this | Not this |
|---|---|
| "This paper proposes..." | "This paper proves..." (unless proven) |
| "This framework may clarify..." | "This framework solves..." |
| "One interpretation consistent with this mapping is..." | "This demonstrates that..." (without demonstration) |
| "Within the limits of the present theoretical analysis..." | "It is clear that..." |
| "This paper does not replace X, but examines..." | "This overturns X." |
| "Future formal work could test whether..." | "Further research is needed." (generic) |

---

### P.3 — Abstract Compression Test

The abstract must survive this compression test:

```
[X] remains a central problem in [field].
While [prior work] established [accepted result], [specific gap] remains unresolved.
Here we examine [approach].
We find / suggest / propose that [bounded result].
This may clarify [scoped implication].
```

If the abstract cannot be compressed into this structure without losing its core claim, it contains either too many claims or a claim that is not yet well-defined.

---

### P.4 — Red Flag Audit

Stop and revise if the draft contains any of the following:

```
[ ] Wording changed but underlying assumption unchanged — this is cosmetic revision, not RCA
[ ] Analogy treated as equivalence — label it correctly
[ ] Ontological framework presented as physical mechanism — lower to correct level
[ ] Solution claimed without formal mechanism — remove or qualify
[ ] Prior work attacked rather than extended — reframe as extension
[ ] Words: "revolutionary," "groundbreaking," "overturns," "proves" without proof
[ ] No "This paper does not claim..." boundary anywhere in the paper
[ ] Prior successful theory not recoverable as limiting case — address this in discussion
[ ] Conclusion ends with "further research is needed" without specifying what research
[ ] Any equation appears without prior plain-language explanation
[ ] Logical steps hedged with "might possibly" or "could perhaps"
```

---

### P.5 — Final Submission Audit

Answer all six questions before submitting. If any answer is unclear, the paper is not ready.

```
1. What is the symptom or observable problem?

2. What is the root cause — the hidden assumption that produces the problem?

3. What exact assumption changed in this paper?

4. What does the paper claim?
   (Use the correct epistemic level from Claim Ladder)

5. What does the paper explicitly not claim?
   (Copy the boundary statement from E.5)

6. How is the claim verified?
   (Source / logic chain / data / derivation)
```

---

### P.6 — Presentational Layer Checklist

```
[ ] Every equation preceded by a plain-language statement
[ ] Every formal term explained in prose before or after the formal element
[ ] "Remove all equations" test passed — argument survives in prose
[ ] All logical steps in the body stated directly without false hedging
[ ] Abstract fits the compression template
[ ] Conclusion distinguishes proven / supported / implied
[ ] Red Flag Audit passed — all 11 items checked
[ ] Final Submission Audit answered — all six questions answered
[ ] Title matches epistemic status
[ ] Boundary statement present in introduction
```

---

# FULL ESP WORKFLOW — Step by Step

This is the complete sequence for an independent author without institutional affiliation from blank page to submission.

---

## Phase 0 — Before You Write Anything

**Step 0.1** — State the research problem in one sentence.

**Step 0.2** — Run the Five-Layer RCA Stack (E.1). Stop if L4 cannot be stated in one sentence.

**Step 0.3** — Run the Three-Why Drill on the central claim (E.2).

**Step 0.4** — Locate the claim on the Claim Ladder (E.3). Confirm you have evidence for the level you are claiming.

**Step 0.5** — Determine the epistemic status of the title (E.4). Write a candidate title.

**Step 0.6** — Write the Boundary Statement (E.5): "This paper does not claim... This paper claims..."

**Step 0.7** — Complete the Epistemic Layer Checklist (E.6). Do not proceed until all items are checked.

---

## Phase 1 — Architecture Before Prose

**Step 1.1** — Write the opening contradiction (S.1). Four paragraphs: phenomenon, prediction, contradiction, approach. Do not cite anyone yet.

**Step 1.2** — Write the thesis in one sentence.

**Step 1.3** — List 6 to 9 sub-questions (S.2). Order them so each answer enables the next.

**Step 1.4** — Write a declarative section title for each sub-question.

**Step 1.5** — For each section, write one sentence stating: what sub-question it answers, and what the answer is. This is your section map.

**Step 1.6** — Plan the literature review. For every source you plan to cite, write: "[Author] established [specific claim]. This paper uses that by [specific use]."

**Step 1.7** — Write the conclusion architecture (S.5) before writing the body. Know where you are going.

**Step 1.8** — Complete the Structural Layer Checklist (S.6). Do not proceed until all items are checked.

---

## Phase 2 — Draft the Paper

**Step 2.1** — Draft the introduction using the opening contradiction (S.1). Move literature review to Section 2.

**Step 2.2** — Draft each section using the internal structure (S.3): sub-question stated, prior answer, new contribution, argument, answer, transition.

**Step 2.3** — For every equation or formal element, write the plain-language statement first, then introduce the formal element (P.1).

**Step 2.4** — In the body, state all logical inferences directly. Do not hedge valid deductions (P.2, Rule 1).

**Step 2.5** — Draft the conclusion following the five-part architecture (S.5). Distinguish proven, supported, and implied.

**Step 2.6** — Write the abstract last. Apply the compression test (P.3).

---

## Phase 3 — Audit Before Submission

**Step 3.1** — Run the Red Flag Audit (P.4). Fix every flagged item.

**Step 3.2** — Run the "Remove all equations" test (P.1). If the argument collapses, restructure.

**Step 3.3** — Run the Final Submission Audit (P.5). Answer all six questions clearly.

**Step 3.4** — Complete the Presentational Layer Checklist (P.6).

**Step 3.5** — Re-read the boundary statement (E.5). Confirm the abstract and conclusion are consistent with it.

**Step 3.6** — Submit.

---

# Worked Example — Applying ESP to a Theoretical Paper

This example illustrates how ESP can discipline a claim before drafting. It is a demonstration of workflow use, not empirical validation of the framework.

## Example research problem

Quantum measurement remains difficult to interpret because a mathematical description of probabilistic states must be connected to definite observed outcomes.

## Layer E — Epistemic discipline

```
Phenomenon:
Quantum systems are represented probabilistically, but measurement yields definite outcomes.

Proximate Cause:
The tension appears at the relation among state, measurement, observer, and outcome.

Underlying Mechanism:
The ontology of observation is often assumed rather than explicitly analyzed.

Root Cause / New Principle:
The paper should not begin by treating observer, object, and outcome as fully independent givens without examining the conditions under which appearance and valid knowledge arise.

Generalization:
A Buddhist Epistemology framework may clarify the structure of measurement as an interpretive and ontological mapping, within strict limits.
```

**Claim level:** Ontological framework with interpretive mapping.

**Boundary statement:** This paper does not claim that Buddhist Epistemology provides a physical mechanism for wavefunction collapse. It proposes a disciplined interpretive framework for reexamining the relation among observation, appearance, and valid knowledge in quantum measurement.

## Layer S — Structural architecture

**Thesis:** Buddhist Epistemology can be used as a bounded ontological-epistemological framework for reinterpreting the structure of quantum measurement without replacing quantum mechanics.

| Sub-question | Section title |
|---|---|
| What makes measurement conceptually difficult? | Why Quantum Measurement Remains Structurally Tense |
| What does prior quantum theory already explain successfully? | What Quantum Mechanics Already Accounts For |
| What assumption does this paper examine? | The Assumed Independence of Observer, Object, and Outcome |
| What does Buddhist Epistemology contribute? | Cognition, Appearance, and Valid Knowledge as Interpretive Tools |
| How does the mapping work without claiming equivalence? | Mapping Measurement as Analogy, Not Physical Identity |
| What does the framework clarify and not clarify? | What the Framework Reframes and What It Does Not Resolve |

## Layer P — Presentation discipline

**Abstract compression draft:**

```
Quantum measurement remains a central interpretive problem in the foundations of physics. While quantum mechanics successfully predicts measurement probabilities, the conceptual relation among observer, state, and definite outcome remains contested. Here we examine whether Buddhist Epistemology can provide a bounded ontological-epistemological framework for reinterpreting this relation. We propose that its analysis of cognition, appearance, and valid knowledge may clarify the structure of measurement as an interpretive mapping. This framework does not replace quantum mechanics or explain collapse as a physical mechanism, but it may help identify assumptions that future formal work could test.
```

---

# ESP Quick Reference Card

For use while writing. Keep this visible.

## Before writing (Layer E)
- Run the RCA Stack. Cannot state L4 in one sentence = not ready.
- Locate claim on Claim Ladder. No evidence for this level = move down.
- Write the boundary statement. Missing = do not proceed.

## While writing (Layer S)
- Open with contradiction. No contradiction in paragraph 1 = restructure.
- One section = one sub-question. Two questions = two sections.
- Every citation names what is borrowed. Generic citation = remove or specify.

## Before submitting (Layer P)
- Every equation has a plain-language sentence before it. Missing = add.
- Body arguments stated directly. Hedged logic = remove hedge.
- Conclusion distinguishes proven / supported / implied. Collapsed = separate.
- Red flag list cleared. Any flag present = fix before submitting.

---

# LLM Prompt Library

Use these prompts at each stage of the ESP workflow.

## Prompts for Layer E

```
PROMPT E1 — RCA STACK
Given this research problem: [PROBLEM]
Run a five-layer root cause analysis:
Layer 1 — Phenomenon: What is observed?
Layer 2 — Proximate Cause: What directly produces it?
Layer 3 — Underlying Mechanism: What produces the proximate cause?
Layer 4 — Root Cause / New Principle: What hidden assumption must change?
Layer 5 — Generalization: Where does this apply, and within what limits?
State each layer in one or two sentences.
```

```
PROMPT E2 — CLAIM LEVEL CHECK
Here is my paper's main claim: [CLAIM]
Here is my evidence: [EVIDENCE TYPE: theoretical / analogical / experimental / formal proof]
Identify which level of this ladder my claim belongs to:
analogy / interpretive mapping / ontological framework / physical model / empirical solution.
Flag if my claim is above the level my evidence supports.
Suggest revised language at the correct level.
```

```
PROMPT E3 — BOUNDARY STATEMENT
Here is my paper's main claim: [CLAIM]
Write:
(a) one sentence stating what this paper does not claim
(b) one sentence stating what this paper does claim
Use conservative, precise academic language.
```

```
PROMPT E4 — TITLE EPISTEMIC STATUS
Here is my paper's main claim: [CLAIM]
Its level of evidence is: [theoretical / analogical / experimental / proven]
Suggest 3 title variants that accurately signal the epistemic status.
One variant should be more assertive, one moderate, one most conservative.
```

## Prompts for Layer S

```
PROMPT S1 — OPENING CONTRADICTION
Here is my paper's core finding: [FINDING]
Here is what prior work predicted: [PRIOR EXPECTATION]
Write four paragraphs:
Para 1: The phenomenon as observed.
Para 2: What current theory predicts.
Para 3: The specific named contradiction.
Para 4: This paper's approach to resolving it.
Do not use jargon specific to [FIELD]. Write for an intelligent non-specialist.
```

```
PROMPT S2 — SUB-QUESTION ARCHITECTURE
Here is my paper's thesis: [THESIS]
List 6 to 9 sub-questions that must be answered to establish this thesis.
Order them so each answer enables the next.
For each sub-question, write a declarative section title.
Avoid vague titles like "Discussion" or "Background."
```

```
PROMPT S3 — LITERATURE CITATION FORMAT
Here is a claim I want to cite: [CLAIM]
Here is the source: [SOURCE]
Write a citation sentence in this form:
"[Author] established that [specific result]. This paper [extends / applies / reframes] that result by [specific use]."
```

```
PROMPT S4 — CONCLUSION AUDIT
Here are my paper's main findings: [FINDINGS]
Classify each finding as:
(a) formally proven
(b) empirically supported
(c) theoretically implied but not yet tested
Write a conclusion that treats each category with appropriate confidence.
End with one specific next-order question this paper opens.
```

## Prompts for Layer P

```
PROMPT P1 — EQUATION TO PROSE
Here is an equation from my paper: [EQUATION]
Write two sentences explaining it without mathematical notation,
for an intelligent reader who is not a specialist in [FIELD].
Then identify which term is doing the most important conceptual work.
```

```
PROMPT P2 — BOLD ARGUMENT CHECK
Here is a paragraph from my paper: [PARAGRAPH]
Identify any logical inferences that are unnecessarily hedged with phrases like
"might possibly," "one could argue," "it seems perhaps."
Rewrite those inferences stated directly, as sound deductions.
Do not change the conclusion language — only the body argument language.
```

```
PROMPT P3 — ABSTRACT COMPRESSION TEST
Here is my abstract: [ABSTRACT]
Compress it into this structure:
"[X] remains a central problem in [field].
While [prior work] established [accepted result], [specific gap] remains unresolved.
Here we examine [approach].
We find / suggest / propose that [bounded result].
This may clarify [scoped implication]."
If the abstract cannot fit this structure, identify which claim is undefined or overclaimed.
```

```
PROMPT P4 — RED FLAG SCAN
Here is my draft: [DRAFT SECTION]
Scan for:
(a) analogy treated as equivalence
(b) overclaimed conclusions without evidence
(c) logical steps hedged with "might possibly" or "could perhaps"
(d) equations without prior plain-language explanation
(e) generic citations not naming what is borrowed
(f) language such as "revolutionary," "overturns," "proves" without formal proof
List every instance and suggest a fix for each.
```

```
PROMPT P5 — FULL SUBMISSION AUDIT
Here is my paper's abstract and conclusion: [ABSTRACT + CONCLUSION]
Answer these six questions:
1. What is the symptom or observable problem?
2. What is the root cause — the hidden assumption that produces it?
3. What exact assumption changed in this paper?
4. What does the paper claim? (State the claim level: analogy / interpretation / ontology / model / empirical)
5. What does the paper explicitly not claim?
6. How is the claim verified?
Flag any question whose answer is unclear in the current text.
```

---

# ESP Framework Summary Table

| Layer | Phase | Core Tool | Key Rule | Output |
|---|---|---|---|---|
| E — Epistemic | Before writing | RCA Stack + Claim Ladder | Locate the claim level. Write the boundary statement. | Root cause in one sentence. Boundary statement. |
| S — Structural | While building | Sub-question architecture + Section map | One section, one sub-question. Open with contradiction. | Section titles. Section map. Conclusion architecture. |
| P — Presentational | Before submitting | Red Flag Audit + Submission Audit | Argue boldly. Conclude carefully. Intuition before formalism. | Cleared checklists. Submission-ready draft. |

---

# Applying ESP to Other Papers

This framework is domain-independent. To apply it to any new paper:

**Step 1:** Run the RCA Stack on the new research problem. The five layers are universal.

**Step 2:** Locate the new claim on the Claim Ladder. The ladder levels are universal.

**Step 3:** Write a new boundary statement. The structure is universal.

**Step 4:** Use the Sub-Question Architecture prompt with the new thesis.

**Step 5:** Apply all three layer checklists without modification.

**Step 6:** Use the LLM Prompt Library with the new paper's content substituted into each [BRACKET].

The only thing that changes between papers is the content inside the brackets. The framework structure, the checklist sequence, and the LLM prompts are reusable as-is.

---

## Attribution

ESP Framework synthesizes principles from:

- RCA Scientific Paper Skill (Author: Viet Nguyen Xuan, GitHub: AIhugART) — Epistemic discipline, claim ladder, boundary statements, red flag protocol
- Einstein Writing Framework (derived from rhetorical analysis of Einstein's 1905 papers) — Contradiction opening, sub-question architecture, intuition before formalism, bold reasoning with careful conclusions

Neither source is reproduced. Both are synthesized into a unified, domain-independent, LLM-friendly workflow.

---

*ESP Framework — Version 1.0*
*Designed for independent authors without institutional affiliation submitting to peer-reviewed journals.*
*All prompts are LLM-ready. All checklists are self-contained.*
*Apply to any scientific paper by substituting content into the bracket fields.*
