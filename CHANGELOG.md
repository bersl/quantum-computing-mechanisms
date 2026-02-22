# Changelog — Quantum Computing: Mechanisms Unveiled

**Proofread & revised: 2026-02-22**

## Pass 1 — Accuracy Fixes

- **Ch4 (Algorithms)**: Fixed claim that "largest number factored = 21 (2019)" — removed incorrect date, clarified that only small numbers have been factored on quantum hardware
- **Ch4**: Corrected classical factoring complexity from "exponential (e^n)" to "sub-exponential (number field sieve, e^(n^⅓))"
- **Ch4**: Added note that Grover's algorithm provides a *quadratic* speedup (not exponential), and that it's provably optimal for unstructured search
- **Ch6 (Hardware)**: Fixed Google Sycamore qubit count from 70 → 53; added mention of Willow and IBM Heron as newer-generation chips
- **Ch6**: Fixed "SiQure" → "Silicon Quantum Computing (SQC)"
- **Ch6**: Updated Microsoft topological qubit status to reflect 2025 milestone announcement
- **Ch7 (Supremacy)**: Corrected quantum supremacy definition — was overstated as "even theoretical [classical computers] with unlimited resources"; now correctly scoped to best *known* classical algorithms
- **Ch7**: Updated "more recent achievements" with Jiuzhang photon counts, Google Willow, and IBM/Quantinuum advances
- **Ch3 (Entanglement)**: Replaced casual "Einstein was wrong about dice!" with reference to actual Bell test experiments (Aspect 1982, loophole-free 2015)

## Pass 2 — Clarity & Flow

- **Ch3**: Removed duplicate "300 qubits = more states than atoms in the universe" (already stated in Ch1); replaced with general statement about exponential growth
- **Ch1/Ch2 (expanded drafts)**: Removed "In the next chapter..." cross-references that were artifacts of serial posting
- **README**: Added note clarifying that `ch01-qubits.md` and `ch02-gates-circuits.md` are expanded drafts, not part of the main 8-chapter sequence

## Pass 3 — Style & Polish

- Replaced excessive exclamation marks and emoji clusters throughout (e.g., "🎩✨" → removed, "🎯🚀" → "🎯", "🌐✨" → "🌐", "📻🎯" → removed)
- Standardized dash usage: hyphens for compound words, em dashes (—) for parenthetical asides (several chapters mixed these inconsistently)
- Tightened filler phrases: "incredibly important!" → "enormously important", "expensive random number generators!" → "expensive random number generators"
- Replaced informal "The magic:" labels with "The insight:" or "The key insight:" for more appropriate tone
- Cleaned up closing of Ch8: removed "📚" emoji signoff

## Pass 4 — Completeness

- No major missing concepts identified; the 8-chapter arc covers qubits → gates → entanglement → algorithms → error correction → hardware → NISQ → future comprehensively
- All serial-posting cross-references ("Coming up: Chapter X...") removed from ch01 and ch02 expanded drafts
- **Recommendation**: Consider whether `ch01-qubits.md` and `ch02-gates-circuits.md` should replace `chapter-1` and `chapter-2` (they are significantly more detailed) or be removed as redundant drafts
