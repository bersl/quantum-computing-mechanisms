# Chapter 9: The Major Players
*Who's building quantum computers, how, and how far they've come*

*Last updated: February 2025*

The quantum computing race is a global competition involving tech giants, startups, national labs, and entire governments. Each player has bet on a different physical approach, a different timeline, and a different vision of what quantum computers will do first. Here's where they all stand.

---

## IBM — The Steady Roadmap

**Approach**: Superconducting transmon qubits
**Headquarters**: Yorktown Heights, New York

**The strategy**: IBM has published the most detailed public roadmap in the industry, committing to specific qubit counts and capabilities years in advance. Their bet is on steady, predictable scaling — like Moore's Law for quantum.

**Key milestones**:
- **2019**: 27-qubit Falcon processor
- **2021**: 127-qubit Eagle — first processor beyond 100 qubits
- **2022**: 433-qubit Osprey
- **2023**: 1,121-qubit Condor — crossed the 1,000-qubit mark
- **2023**: Heron processor (133 qubits) — focused on quality over quantity, with tunable couplers for lower error rates
- **2024**: IBM pivoted to a modular strategy, connecting multiple Heron chips rather than making single chips bigger

**Roadmap ahead**:
- **Flamingo** (2025): Mid-scale processors with chip-to-chip quantum links
- **Starling** (~2027): Error-corrected logical qubits
- **Blue Jay** (~2029): 100,000+ qubits through modular architecture

**Distinctive approach**:
- **Qiskit**: The most widely-used quantum software framework, open-source
- **Cloud access**: 28 quantum devices (~100 qubits each), totaling 2,299 available qubits, with 97% uptime and over 3.6 trillion circuits executed
- **Error mitigation**: Pioneered techniques to extract useful results from noisy hardware without full error correction
- **Modularity**: Bet on linking smaller, high-quality chips rather than building one massive chip
- **Quantum System Two**: A modular multi-QPU architecture designed to link multiple processors together
- **Manufacturing**: Operates a 300mm semiconductor fab dedicated to qubit manufacturing
- **Scaling R&D**: Developing ℓ-couplers for inter-module quantum communication, cryogenic CMOS control electronics, and qLDPC (quantum low-density parity check) error-correcting codes for more efficient fault tolerance

**Current standing**: The largest quantum cloud provider with the most deployed systems. Shifted focus from raw qubit count to "useful quantum computing" — practical results on real problems. Their modular strategy with Quantum System Two and investment in custom semiconductor fabrication position them for the next phase of scaling.

---

## Google Quantum AI — The Moonshot Lab

**Approach**: Superconducting transmon qubits (Sycamore architecture)
**Headquarters**: Santa Barbara, California

**The strategy**: Google takes a research-first, milestone-driven approach. Rather than building cloud services, they focus on achieving specific scientific breakthroughs that prove quantum computing works.

**Key milestones**:
- **2019**: Achieved "quantum supremacy" with 53-qubit Sycamore — completed a sampling task in 200 seconds that would take classical supercomputers ~10,000 years. The most famous result in quantum computing history.
- **2023**: Demonstrated that increasing the size of their surface error-correcting code actually *reduces* logical error rates — a critical proof that error correction works as theory predicts
- **2024**: Willow processor (105 qubits) — a landmark result published in *Nature* (December 2024). Tested surface code error correction on 3×3, 5×5, and 7×7 grids of encoded qubits, demonstrating that the error rate *halved* with each increase in grid size. This exponential error reduction with scaling — operating "below threshold" — is the strongest evidence yet that quantum error correction works as theory predicts. Willow also completed a benchmark computation in under 5 minutes that would take the fastest classical supercomputer 10 septillion (10²⁵) years.

**Roadmap ahead**:
- **Near-term**: Build a long-lived logical qubit from ~1,000 physical qubits
- **Mid-term**: Useful error-corrected quantum computer
- **Long-term target**: A system capable of commercially relevant computations in chemistry and materials science

**Distinctive approach**:
- **Error correction focus**: Google sees fault tolerance as the only path to useful quantum computing — not interested in NISQ workarounds
- **Fewer, better qubits**: Quality-obsessed, not chasing qubit counts
- **Vertical integration**: Designs chips, cryogenics, and control electronics in-house
- **Open research**: Publishes extensively in Nature, Science, and arXiv

**Current standing**: Holds the strongest experimental claims for quantum supremacy and error correction. Fewer deployed cloud systems than IBM, but arguably leading on the scientific frontier.

---

## Quantinuum — The Quality Leader

**Approach**: Trapped ion qubits (ytterbium ions)
**Headquarters**: Broomfield, Colorado (formed from Honeywell Quantum + Cambridge Quantum)

**The strategy**: Quantinuum bets that qubit quality matters far more than qubit quantity. Their trapped-ion systems have the highest gate fidelities and most connectivity of any commercial platform.

**Key milestones**:
- **2020**: Honeywell launched the H0 system, claimed "highest quantum volume" 
- **2021**: Merged Honeywell Quantum Solutions with Cambridge Quantum Computing
- **2023**: H1 system (20 qubits) achieved two-qubit gate fidelity >99.8% — best in the industry
- **2023**: H2 system (56 qubits) with all-to-all connectivity
- **2024**: Demonstrated fault-tolerant operations and real-time error correction on the H2 system. First company to demonstrate "useful" logical qubit operations.

**Roadmap ahead**:
- **Helios** (~2027): Hundreds of qubits with built-in error correction
- **Long-term**: Targeting 10,000+ physical qubits and meaningful logical qubit counts

**Distinctive approach**:
- **All-to-all connectivity**: Any qubit can interact with any other — eliminates SWAP overhead
- **QCCD architecture**: Quantum Charge-Coupled Device — ions are physically shuttled between zones for different operations
- **Integrated software**: Strong software stack (TKET compiler, Inquanto for chemistry)
- **Business model**: Subscription cloud access + partnerships with enterprise customers

**Current standing**: Widely regarded as having the highest-quality qubits commercially available. Fewer total qubits than superconducting competitors, but each qubit is dramatically more reliable.

---

## IonQ — The Public Market Pioneer

**Approach**: Trapped ion qubits (ytterbium ions, barium ions)
**Headquarters**: College Park, Maryland

**The strategy**: IonQ was the first pure-play quantum computing company to go public (NYSE: IONQ, 2021). They focus on making quantum computers accessible through major cloud platforms.

**Key milestones**:
- **2020**: Launched 32-qubit system with 99.9% single-qubit and 99.4% two-qubit fidelity
- **2022**: IonQ Aria — improved performance, available on AWS, Azure, and Google Cloud
- **2023**: IonQ Forte — 36 qubits with acousto-optic deflector (AOD) for flexible qubit addressing
- **2024**: Forte Enterprise — deployed to national labs; announced plans for barium-based qubits for better performance

**Roadmap ahead**:
- **IonQ Tempo** (~2025): Next-generation system with significantly more qubits
- **2028+**: Targeting broad quantum advantage with networked trapped-ion processors

**Distinctive approach**:
- **Multi-cloud**: Available on AWS Braket, Azure Quantum, and Google Cloud simultaneously
- **Photonic interconnects**: Plan to network multiple ion traps using photon links
- **Barium transition**: Moving from ytterbium to barium ions for better optical properties
- **Enterprise partnerships**: US Air Force, Hyundai, Goldman Sachs collaborations

**Current standing**: The most commercially visible quantum company due to its public listing. Hardware quality slightly behind Quantinuum, but strong cloud accessibility and partnerships.

---

## Microsoft Azure Quantum — The Topological Bet

**Approach**: Topological qubits (Majorana-based) + cloud platform for third-party hardware
**Headquarters**: Redmond, Washington

**The strategy**: Microsoft made the boldest and most controversial bet in quantum computing — topological qubits that would be inherently error-resistant. After years of setbacks, they've recently claimed breakthroughs.

**Key milestones**:
- **2012–2018**: Major investment in topological qubit research at Station Q (Santa Barbara) and Delft
- **2018**: Published a landmark paper claiming Majorana zero modes — later retracted in 2021 due to data issues
- **2022**: Published new, more rigorous evidence for topological superconductivity in indium arsenide/aluminum nanowires
- **2024**: Claimed creation of the first topological qubit and published a roadmap to scale
- **2025**: Announced Majorana 1 (February 2025) — the first quantum processor powered by topological qubits. The chip uses a new class of material called a "topoconductor" and contains 8 topological qubits. While still very early — no complex computations have been performed — it represents proof that topological qubits can actually be manufactured. Microsoft claims this architecture could enable a million-qubit quantum computer faster than competing approaches

**Roadmap ahead**:
- **Near-term**: Demonstrate logical qubit operations with topological protection
- **Mid-term**: Build small fault-tolerant systems
- **Long-term**: Million-qubit machines with dramatically lower error correction overhead

**Distinctive approach**:
- **Topological protection**: If it works, each qubit is inherently resistant to local noise — needing far fewer physical qubits per logical qubit
- **High risk, high reward**: Years behind on hardware but could leapfrog competitors if the physics pans out
- **Azure Quantum platform**: Meanwhile, offers access to IonQ, Quantinuum, Rigetti, and Pasqal hardware through Azure
- **Software leadership**: Q# programming language, strong compiler and resource estimation tools

**Current standing**: The most uncertain but potentially transformative trajectory. The Majorana 1 announcement in February 2025 was a significant credibility boost — proving that topological qubits can be physically built using topoconductor materials. However, with only 8 qubits and no complex computations demonstrated, real-world performance data is still emerging. If topological qubits deliver on their promise, Microsoft could bypass the massive error correction overhead that burdens other approaches. If not, they're years behind.

---

## QuEra Computing — The Neutral Atom Challenger

**Approach**: Neutral atom qubits (rubidium atoms in optical tweezers)
**Headquarters**: Boston, Massachusetts (Harvard/MIT spinout)

**The strategy**: QuEra bets on neutral atoms as the best of both worlds — scalable like superconducting qubits, high-quality like trapped ions.

**Key milestones**:
- **2021**: Founded based on Harvard/MIT research demonstrating 256-qubit neutral atom arrays
- **2023**: Demonstrated 48 logical qubits using transversal gates — a landmark result for error correction
- **2024**: Published results showing up to 280 physical qubits with reconfigurable connectivity

**Roadmap ahead**:
- **2025**: 256-qubit system with error correction
- **2026–2028**: 3,000–10,000+ qubit machines
- **Long-term**: 100,000 qubits — potentially the fastest path to large-scale fault tolerance

**Distinctive approach**:
- **Reconfigurable arrays**: Atoms can be physically moved with optical tweezers to create any connectivity pattern on-the-fly
- **Fast Rydberg gates**: Exciting atoms to Rydberg states creates strong interactions for fast two-qubit gates
- **Natural scaling**: Adding more atoms is relatively straightforward compared to fabricating more superconducting circuits
- **Open-source**: Bloqade software framework

**Current standing**: One of the most exciting emerging players. The 48-logical-qubit demonstration was a watershed moment that put neutral atoms on the map as a serious contender for fault-tolerant quantum computing.

---

## PsiQuantum — The Photonic Moonshot

**Approach**: Photonic (fusion-based linear optical quantum computing)
**Headquarters**: Palo Alto, California

**The strategy**: PsiQuantum's thesis is radical — skip the NISQ era entirely and build a million-qubit fault-tolerant machine from the start, using photons and existing semiconductor manufacturing.

**Key milestones**:
- **2016**: Founded by Jeremy O'Brien (Bristol University photonics pioneer)
- **2021**: Raised $450M+ in funding — among the most well-funded quantum startups
- **2023**: Partnership with GlobalFoundries to manufacture photonic chips in existing semiconductor fabs
- **2024**: Secured $940M from Australian government to build a fault-tolerant quantum computer in Brisbane

**Roadmap ahead**:
- **~2027–2029**: First fault-tolerant quantum computer (their stated target)
- **Architecture**: Millions of photonic components networked through optical fiber

**Distinctive approach**:
- **Semiconductor manufacturing**: Chips made in standard fabs (GlobalFoundries), not specialized quantum labs
- **Room temperature optics**: Photonic circuits work at room temperature (detectors need cooling)
- **Fusion-based**: Entanglement generated by "fusing" photons together probabilistically, with error correction handling the randomness
- **No NISQ products**: They have no cloud quantum computer — all resources focused on the fault-tolerant end goal

**Current standing**: The most secretive major player. Very few public benchmarks or published results. Their bet is that when they deliver, they'll jump straight to useful fault tolerance while competitors are still scaling up noisy systems. High conviction, high risk.

---

## Rigetti Computing — The Full-Stack Startup

**Approach**: Superconducting qubits
**Headquarters**: Berkeley, California (NYSE: RGTI)

**Key milestones**:
- **2017**: Launched first cloud quantum computing platform (Forest/Quilc)
- **2022**: 80-qubit Aspen-M processor
- **2023**: Ankaa-2 (84 qubits) with improved gate fidelities using tunable couplers
- **2024**: Announced 9-qubit error correction demonstrations; working toward 100+ qubit systems

**Distinctive approach**: Vertical integration — designs, fabricates, and deploys its own chips in its own fab (Fab-1). Smaller scale than IBM/Google but fully independent supply chain.

**Current standing**: Smaller player competing against tech giants. Public listing provides capital but also pressure to show results. Focused on near-term enterprise applications.

---

## China — The National Program

China runs the most significant government-backed quantum computing program alongside the US and EU.

### USTC (University of Science and Technology of China)
**Leader**: Jian-Wei Pan ("China's Father of Quantum")
- **2020**: Jiuzhang photonic computer — 76-photon Boson sampling, claimed quantum supremacy
- **2021**: Jiuzhang 2.0 (113 photons) and Zuchongzhi 2.1 (66 superconducting qubits)
- **2023**: Jiuzhang 3.0 (255 photons) — significantly extended quantum advantage claims

### Origin Quantum (本源量子)
- China's leading quantum computing startup
- Developed Wuyuan superconducting processor (up to 72 qubits)
- Offers cloud access through Origin Quantum Cloud
- Focus on building a domestic quantum computing ecosystem independent of Western technology

### National investment
- China's 14th Five-Year Plan designated quantum computing as a strategic priority
- Estimated $15B+ in government quantum investment
- Building the National Laboratory for Quantum Information Sciences in Hefei
- Strong focus on quantum communication networks (Beijing-Shanghai quantum link operational since 2017)

---

## Europe — The Collaborative Approach

### Pasqal (France)
**Approach**: Neutral atoms
- Founded by Nobel laureate Alain Aspect's research group
- Up to 200+ qubits in neutral atom arrays
- Focus on quantum optimization and simulation for industry
- Partnerships with EDF, Airbus, BMW

### IQM Quantum Computers (Finland)
**Approach**: Superconducting qubits
- Leading European superconducting quantum hardware company
- 20-qubit processors deployed; scaling to 50+ qubits
- Building Finland's first quantum computer
- Co-design approach: custom processors for specific applications

### European Quantum Flagship
- €1 billion, 10-year EU program launched in 2018
- Funds research across quantum computing, communication, sensing, and simulation
- Coordinates efforts across 5,000+ researchers in 30+ countries

---

## The Landscape at a Glance

| Player | Approach | Max Qubits | Key Strength | Key Risk |
|--------|----------|-----------|-------------|----------|
| **IBM** | Superconducting | 1,121 | Largest ecosystem, modularity | Can modular links maintain coherence? |
| **Google** | Superconducting | 105 | Error correction breakthroughs | Narrow focus, fewer deployed systems |
| **Quantinuum** | Trapped ions | 56 | Highest gate fidelity | Scaling ion traps beyond ~100 qubits |
| **IonQ** | Trapped ions | 36 | Multi-cloud access | Quality gap vs Quantinuum |
| **Microsoft** | Topological | ~8 (early) | Could bypass error correction overhead | Unproven physics, years behind |
| **QuEra** | Neutral atoms | 280 | 48 logical qubits demonstrated | Young company, needs to scale |
| **PsiQuantum** | Photonic | N/A | Semiconductor fab manufacturing | No public benchmarks, high secrecy |
| **Rigetti** | Superconducting | 84 | Own fabrication facility | Small scale vs IBM/Google |
| **USTC** | Photonic + SC | 255 (photonic) | Strong government backing | Limited commercial access |

---

## The Race: What to Watch

**Near-term (2025–2027)**: Who demonstrates the first *useful* logical qubit? Google and Quantinuum are closest. QuEra's neutral atom approach could surprise.

**Mid-term (2027–2030)**: Can modular architectures (IBM) or photonic manufacturing (PsiQuantum) deliver thousands of qubits? Does Microsoft's topological bet pay off?

**Long-term (2030+)**: Which approach scales to millions of qubits for fault tolerance? The answer might be "all of them, for different use cases" — or one approach could decisively win.

**The wildcard**: A breakthrough in materials science, a new qubit type, or an unexpected algorithmic advance could reshuffle the entire race overnight.

One thing is clear: this isn't a winner-take-all race. The quantum ecosystem will likely be heterogeneous — different hardware for different problems, connected by quantum networks, managed by sophisticated software that abstracts away the underlying physics. The real winners will be the ones who find the first problems where quantum computers deliver undeniable, practical value.
