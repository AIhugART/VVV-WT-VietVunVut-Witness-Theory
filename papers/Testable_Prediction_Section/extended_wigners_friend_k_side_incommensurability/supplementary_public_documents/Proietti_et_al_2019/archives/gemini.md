# **Experimental Test of Local Observer Independence: Synthesized Document**

## **1\. Introduction and Theoretical Framework**

### **The Wigner's Friend Paradox**

* The "Wigner's friend" thought experiment highlights the conflict regarding the objectivity of observations in quantum mechanics.

* In this scenario, an observer (Wigner's friend) is inside an isolated laboratory and measures a photon that is in an equal superposition of horizontal $|h\\rangle$ and vertical $|v\\rangle$ polarization.

* According to quantum theory, the friend randomly observes one of the two possible outcomes and stores the record in a physical memory, such as "photon is h" or "photon is v".

* From outside the laboratory, Wigner has no information about the friend's measurement outcome.

* Wigner must describe the friend and the photon as a joint entangled state:  
  $$1/\\sqrt{2}(|h\\rangle | \\text{"photon is h"}\\rangle \+ |v\\rangle | \\text{"photon is v"}\\rangle)$$  
  .

* Wigner can verify this state assignment via an interference experiment, establishing a fact from his perspective that suggests his friend could not have observed a definite outcome, thereby contradicting the friend's recorded fact.

### **The Extended Bell-Wigner Scenario**

* An extended Wigner's friend scenario utilizes a pair of physical systems shared between two separate laboratories controlled by Alice and Bob.

* Inside the laboratories, Alice's friend and Bob's friend perform nondestructive measurements on their respective systems and record the outcomes in a memory.

* Alice and Bob can choose to measure their friend's record (defining variables $A\_0$ and $B\_0$) or jointly measure the friend's record and the system (defining variables $A\_1$ and $B\_1$).

* The framework relies on three key assumptions: free choice (F), locality (L), and observer-independent facts (O).

* Under these assumptions, the joint probability distributions must satisfy the Clauser-Horne-Shimony-Holt (CHSH) inequality:  
  $$S \= \\langle A\_1 B\_1 \\rangle \+ \\langle A\_1 B\_0 \\rangle \+ \\langle A\_0 B\_1 \\rangle \- \\langle A\_0 B\_0 \\rangle \\le 2$$  
  .

## ---

**2\. Experimental Setup**

The experiment tests the extended Bell-Wigner scenario using a state-of-the-art six-photon setup.

### **Photon Sources**

* The setup utilizes three photon-pair sources ($S\_0$, $S\_A$, $S\_B$) optimized for brightness and purity based on a Sagnac-type design.

* A 775-nm Ti:sapphire laser is focused into a periodically poled potassium titanyl phosphate (ppKTP) crystal to generate pairs of 1550-nm single photons.

* The laser's repetition rate is temporally multiplexed to effectively quadruple the pulse rate, suppressing higher-order emissions.

* The sources generate polarization-entangled photon pairs in the state $|\\Psi^{-}\\rangle \= (|h\\rangle|v\\rangle \- |v\\rangle|h\\rangle)/\\sqrt{2}$.

### **The Measurement Protocol**

* The central source $S\_0$ generates an entangled pair distributed to the laboratories of Alice's friend and Bob's friend.

* A half-wave plate (HWP) applies a rotation to the photon pair from $S\_0$ to maximize the violation of the inequality for the chosen measurement settings.

* The friends utilize type-I fusion gates, which rely on nonclassical interference at a polarizing beam splitter (PBS), to perform nondestructive polarization measurements.

* Ancilla photons from sources $S\_A$ and $S\_B$ act as physical memories to store the extracted information.

* Superconducting nanowire single-photon detectors (SNSPDs) detect heralding photons to signal the successful measurement of the fusion gates.

* Alice and Bob either utilize a 50/50 beam splitter for a Bell-state measurement to measure $A\_1$ and $B\_1$, or remove the beam splitter to measure $A\_0$ and $B\_0$ directly.

## ---

**3\. Experimental Results**

The experiment successfully demonstrates a violation of the Bell-Wigner inequality across various measurement protocols.

### **Primary Results**

* A total of 1794 six-photon coincidence events were recorded over a total measurement time of 360 hours.

* The measured parameter was $S\_{exp} \= 2.416\_{-0.075}^{+0.075}$.

* This result violates the Bell-Wigner inequality by more than five standard deviations.

### **Alternative Observables and Protocols**

* An alternative definition for observables $A\_0$ and $B\_0$ was tested, which acts as a measurement of the friend's record and a consistency check with the original photon.

* Using this alternative definition, the calculated average values yielded $S\_{exp} \= 2.407\_{-0.073}^{+0.073}$, also violating the inequality by over 5 standard deviations.

* An alternative measurement method for $A\_0$ and $B\_0$ introduced linear polarisers instead of removing the beam splitter to prevent interference.

* This alternative method produced an expectation value of $S\_{exp} \= 2.346\_{-0.110}^{+0.110}$, violating the inequality by more than 3 standard deviations.

* The violation observed in this alternative protocol was slightly reduced due to a \~4.83% optical loss introduced by the polarisers.

### **Error Analysis**

* Statistical uncertainties were independently estimated utilizing an error propagation approach and a Monte Carlo method utilizing 100,000 samples.

* The uncertainty values obtained through these two methods agreed to within 0.0032.

* The experimental violation was primarily limited by higher-order multipair emissions from the probabilistic photon sources.

## ---

**4\. Discussion and Loopholes**

The empirical violation of the Bell-Wigner inequality poses substantial challenges to fundamental assumptions within quantum theory and introduces specific experimental requirements.

### **Interpretation of Observer Independence**

* The violation implies that the assumptions of free choice, locality, and observer-independent facts cannot all be true simultaneously.

* To accommodate the result, one might proclaim that facts can only be established by a privileged observer, such as in the many worlds interpretation or Bohmian mechanics.

* Alternatively, one must abandon observer independence completely, treating facts strictly relative to observers, aligning with interpretations like QBism.

* This requires embracing the possibility that different observers can irreconcilably disagree about what happened in an experiment.

* Quantum theory does not distinguish between information recorded in a microscopic system (like a photonic memory) and a macroscopic system, meaning the conclusions apply regardless of observer size or complexity.

### **Loopholes in Bell-Wigner Tests**

* The experiment is subject to the same conceptual and technical loopholes as traditional Bell tests: locality, freedom of choice, and the detection loophole.

* Closing the locality and freedom of choice loopholes in an "event-ready" configuration requires the heralding events to be space-like separated from the setting choices, which must be space-like separated from the measurement outcomes of the other party.

* Closing the detection loophole requires photon-number-resolving detectors and measurement protocols capable of projecting onto any eigenstate.

* The minimal required detection efficiency to close the detection loophole in a Bell-Wigner test is $\\eta \> 0.875$, a more stringent requirement than the $\\eta \> 0.828$ needed for a standard CHSH test.

* A new loophole specific to Bell-Wigner tests arises if the interpretation that $A\_0$ and $B\_0$ directly measure the friend's memory cannot be maintained.

* Addressing this new loophole requires measurement devices that clearly separate the initial systems from the memories and only "look" at the memory photons.  
