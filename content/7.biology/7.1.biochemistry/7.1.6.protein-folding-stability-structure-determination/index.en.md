---
title: Protein Folding, Stability, and Structure Determination
description: Denaturation and Anfinsen's experiment; the two-state model, thermal and chemical denaturation, the stability curve and cold denaturation; Levinthal's paradox, biased search and the folding funnel; chevron plots; Hsp70, chaperonins, PDI and prolyl isomerases; amyloid, prions and misfolding diseases; X-ray crystallography, NMR, cryo-electron microscopy and structure prediction.
---

The previous chapter described the native structures of proteins; this one asks three questions about them. How stable is a native structure, and how can its stability be measured? How does a chain find its native structure, among astronomically many alternatives, in milliseconds to seconds? And how are structures determined in the first place? The answers rest on the physical chemistry of the earlier courses: the stability of a protein is an equilibrium constant whose temperature dependence follows the **Gibbs–Helmholtz equation** ([6.3.3](/6.3.3)), folding kinetics is the kinetics of an **opposing reaction** ([6.3.15](/6.3.15)), and the structural methods are applications of **X-ray diffraction** ([6.4.8](/6.4.8)), **nuclear magnetic resonance** ([6.4.12](/6.4.12)) and the **Fourier transform** ([2.5.6](/2.5.6)). The same principles reappear in cells as proteostasis: chaperones that assist folding, enzymes that catalyze slow steps, and diseases in which misfolded proteins aggregate. Protein synthesis, targeting and degradation by the ubiquitin–proteasome system belong to molecular biology ([7.2.19](/7.2.19), [7.2.20](/7.2.20)).

## 6.1. Denaturation and Renaturation

### 6.1.1. Proteostasis and Denaturation

Native proteins are only marginally stable ([7.1.5](/7.1.5#sec-5.1.1)), and most must stay flexible to work. Every cell therefore runs a network of hundreds of proteins that fold newly made chains, refold chains that have partly unfolded, and sequester or degrade chains that are irreversibly misfolded or no longer needed.

**Definition 6.1.1 (Proteostasis)** **Proteostasis** is the maintenance of the set of active proteins that a cell requires under given conditions, by the coordinated pathways of protein synthesis, folding, refolding, sequestration and degradation.

**Definition 6.1.2 (Denaturation)** **Denaturation** is a loss of three-dimensional structure sufficient to cause loss of function. The denatured state is not necessarily a fully unfolded random chain; under most conditions it is an ensemble of partly folded states.

| Denaturing agent | Main mode of action |
|---|---|
| Heat | weakens many weak interactions at once, mainly hydrogen bonds; the transition is sharp (cooperative) |
| Extremes of pH | change the net charge; electrostatic repulsion and loss of some hydrogen bonds and ion pairs |
| Organic solvents (alcohol, acetone), detergents | disrupt the hydrophobic core |
| Urea, guanidine hydrochloride (GdnHCl) | solvate the backbone and nonpolar groups better than water; urea also competes for hydrogen bonds |

None of these treatments breaks covalent bonds of the chain, and the denatured structures they produce are not identical. Exposed hydrophobic surfaces of denatured molecules often associate into disordered aggregates (the white of a boiled egg) or, in some proteins, into ordered fibrils (§6.5). Proteins of thermophilic bacteria and archaea, which work near $100\ ^\circ\mathrm{C}$, have folds similar to those of mesophiles but take the stabilizing principles to extremes: more charged residues on the surface, networks of ion pairs, tighter hydrophobic packing and often more disulfides.

### 6.1.2. Anfinsen's Experiment: Sequence Determines Structure

Ribonuclease A is a small enzyme of $124$ residues with eight Cys residues paired into four **disulfide bonds**. In the 1950s Christian Anfinsen denatured it completely in $8\ \mathrm{M}$ urea containing 2-mercaptoethanol ($\ce{HOCH2CH2SH}$): urea disrupts the noncovalent structure, and the thiol reduces the disulfides to eight free SH groups (being itself oxidized to the disulfide dimer). The product had the viscosity and optical rotation of a random chain and no enzymatic activity. The decisive results came from three ways of removing the reagents.

| Procedure | Outcome | Interpretation |
|---|---|---|
| Remove urea and 2-mercaptoethanol together by dialysis, then let air oxidize the thiols | activity and all physical properties of the native enzyme recovered; the four native disulfides re-formed | the sequence alone contains the information for the native structure |
| Reoxidize the thiols while still in $8\ \mathrm{M}$ urea, then remove urea | "scrambled" ribonuclease with about $1\%$ activity | in urea the disulfides form at random; the correct pairing requires the weak interactions of the native fold |
| Add a trace of 2-mercaptoethanol to scrambled ribonuclease | slow conversion to fully active enzyme | catalytic thiol allows disulfide exchange, so the system reaches the thermodynamically most stable pairing |

The second result is quantitative. Eight cysteines can be paired in $7 \times 5 \times 3 \times 1 = 105$ ways, only one of them native, so random pairing gives $1/105 \approx 1\%$ correctly bridged molecules, exactly the activity observed. Later, chemically synthesized ribonuclease A (Merrifield, 1969) also folded to the active enzyme, excluding any contaminant as a folding agent.

**Proposition 6.1.1 (Thermodynamic Hypothesis)** For a protein that can renature, the native structure is the state of lowest Gibbs energy of the whole system (chain and solvent) under physiological conditions, and it is determined by the amino acid sequence in that environment (Anfinsen, Nobel Prize in Chemistry 1972).

**Definition 6.1.3 (Renaturation)** **Renaturation** is the spontaneous return of a denatured protein to its native, active structure when the conditions in which the native state is stable are restored.

**Remark 6.1.1** The thermodynamic hypothesis must be read with care. Only a minority of proteins, mostly small and stable ones, refold efficiently in a test tube; many need help in the crowded cell (§6.4), although that help usually changes the rate and yield of folding, not the final structure. Some proteins are kinetically trapped in a native state that is not the global minimum: the serpin protease inhibitors fold into a metastable "spring-loaded" form, and α-lytic protease folds only with the help of its pro-region. Metamorphic proteins such as lymphotactin interconvert between two different folds, and amyloid (§6.5) is, for many sequences, more stable than the native state at high concentration.

### 6.1.3. Local Sequence Does Not Fix Secondary Structure

Secondary structure is not a simple function of the local sequence. The hexapeptide VDLLKN, for example, is an α helix in one protein and a β strand in another: tertiary interactions decide which structure a segment adopts. This is why predicting secondary structure from sequence alone reached only about $75$–$80\%$ accuracy, and why reliable prediction came only from methods that model the whole chain at once (§6.6.5).

## 6.2. Thermodynamics of Stability

### 6.2.1. The Two-State Model

When a small protein is denatured by heat or by increasing concentrations of a denaturant, the transition is sharp, and different probes (circular dichroism of the backbone, fluorescence of a buried Trp, enzymatic activity) report the same transition. This means that only two species are populated to a significant extent.

**Definition 6.2.1 (Two-State Model)** In the **two-state model** of unfolding, a protein exists only as the native state N and the unfolded state U, interconverting in a single cooperative transition $\ce{N <=> U}$ with equilibrium constant and stability

$$
K_{\mathrm{U}} = \frac{[\mathrm{U}]}{[\mathrm{N}]}, \qquad
f_{\mathrm{U}} = \frac{K_{\mathrm{U}}}{1 + K_{\mathrm{U}}}, \qquad
\Delta_{\mathrm{U}}G^\circ = -RT\ln K_{\mathrm{U}} .
$$

Since N ⇌ U is a unimolecular isomerization, $K_\mathrm{U}$ is dimensionless and independent of the standard concentration. A positive $\Delta_{\mathrm{U}}G^\circ$ means the native state is stable; at the midpoint of the transition $K_\mathrm{U} = 1$ and $\Delta_{\mathrm{U}}G^\circ = 0$. The model has a striking consequence: a half-denatured solution does not contain half-unfolded molecules, but a $50\!:\!50$ mixture of fully folded and fully unfolded ones. Cooperativity arises because each part of the structure is stabilized by the others (loss of structure in one region destabilizes the rest), so partly folded states have high Gibbs energy.

Any measured signal $y$ (ellipticity, fluorescence) is the population-weighted average of the signals of the two states, $y = y_\mathrm{N}(1 - f_\mathrm{U}) + y_\mathrm{U} f_\mathrm{U}$, where the baselines $y_\mathrm{N}$ and $y_\mathrm{U}$ usually vary slightly and linearly with temperature or denaturant. Fitting this expression to a whole transition is a **nonlinear regression** problem ([3.3.6](/3.3.6)). The two-state assumption can be tested: transitions followed by different probes must coincide, and the enthalpy measured directly by differential scanning calorimetry must equal the van 't Hoff enthalpy obtained from the shape of the transition.

### 6.2.2. Thermal Denaturation and the Stability Curve

The temperature dependence of $K_\mathrm{U}$ follows from thermodynamics. Unfolding exposes nonpolar groups to water, which raises the **heat capacity** of the system: $\Delta_{\mathrm{U}}C_p > 0$, and to a good approximation it is independent of temperature. Integrating $\left(\partial \Delta H/\partial T\right)_p = \Delta C_p$ and $\left(\partial \Delta S/\partial T\right)_p = \Delta C_p/T$ from the melting temperature $T_\mathrm{m}$, where $\Delta_{\mathrm{U}}G^\circ = 0$ and hence $\Delta_{\mathrm{U}}S^\circ(T_\mathrm{m}) = \Delta_{\mathrm{U}}H_\mathrm{m}/T_\mathrm{m}$, gives the integrated **Gibbs–Helmholtz equation** ([6.3.3](/6.3.3#sec-3.6)).

**Formula 6.2.1 (Protein Stability Curve)** With $\Delta_{\mathrm{U}}H_\mathrm{m}$ the unfolding enthalpy at $T_\mathrm{m}$ and a constant $\Delta_{\mathrm{U}}C_p$,

$$
\begin{aligned}
\Delta_{\mathrm{U}}H(T) &= \Delta_{\mathrm{U}}H_\mathrm{m} + \Delta_{\mathrm{U}}C_p\,(T - T_\mathrm{m}),\\
\Delta_{\mathrm{U}}S(T) &= \frac{\Delta_{\mathrm{U}}H_\mathrm{m}}{T_\mathrm{m}} + \Delta_{\mathrm{U}}C_p \ln\frac{T}{T_\mathrm{m}},\\
\Delta_{\mathrm{U}}G^\circ(T) &= \Delta_{\mathrm{U}}H_\mathrm{m}\left(1 - \frac{T}{T_\mathrm{m}}\right) + \Delta_{\mathrm{U}}C_p\left[T - T_\mathrm{m} - T\ln\frac{T}{T_\mathrm{m}}\right].
\end{aligned}
$$

Three consequences follow.

1. *Sharpness of the melt.* From the van 't Hoff equation $\mathrm{d}\ln K_\mathrm{U}/\mathrm{d}T = \Delta_{\mathrm{U}}H/(RT^2)$, the slope of $f_\mathrm{U}$ at $T_\mathrm{m}$ is $\Delta_{\mathrm{U}}H_\mathrm{m}/(4RT_\mathrm{m}^2)$. Because unfolding a protein breaks many interactions at once, $\Delta_{\mathrm{U}}H_\mathrm{m}$ is large ($200$–$600\ \mathrm{kJ\,mol^{-1}}$ for small proteins), and the transition spans only $10$–$20\ \mathrm{K}$. For $\Delta_{\mathrm{U}}H_\mathrm{m} = 350\ \mathrm{kJ\,mol^{-1}}$ and $T_\mathrm{m} = 333\ \mathrm{K}$ the slope is $0.095\ \mathrm{K^{-1}}$: about $10\%$ more molecules unfold per kelvin at the midpoint.
2. *A maximum of stability.* The curve $\Delta_{\mathrm{U}}G^\circ(T)$ is concave (its second derivative is $-\Delta_{\mathrm{U}}C_p/T < 0$). Stability is greatest at the temperature $T_\mathrm{s}$ where $\Delta_{\mathrm{U}}S = 0$, namely $T_\mathrm{s} = T_\mathrm{m}\exp[-\Delta_{\mathrm{U}}H_\mathrm{m}/(T_\mathrm{m}\Delta_{\mathrm{U}}C_p)]$; even there, typical stabilities are only $20$–$60\ \mathrm{kJ\,mol^{-1}}$, the equivalent of a few hydrogen bonds.
3. *Cold denaturation.* A concave curve that crosses zero at $T_\mathrm{m}$ must cross it again at a lower temperature: proteins also unfold on cooling, because the hydrophobic effect weakens at low temperature (at low $T$ unfolding becomes enthalpically favorable). For most proteins the second crossing lies below $0\ ^\circ\mathrm{C}$ and is observed only in supercooled water or for destabilized mutants.

![Two-state unfolding. A: fraction unfolded against temperature for a protein with Tm = 60 °C and three unfolding enthalpies (heat-capacity change set to zero to isolate the effect of ΔH): the larger the enthalpy, the sharper the cooperative transition. B: simulated chemical denaturation followed by the circular dichroism at 222 nm (true values ΔG(H₂O) = 30 kJ/mol, m = 12 kJ mol⁻¹ M⁻¹, sloping baselines, Gaussian noise); the fitted two-state curve (black) recovers the parameters within their standard errors and gives the midpoint Cm = ΔG/m; inset: ΔG computed for each point in the transition zone falls on the straight line of the linear extrapolation model, whose intercept is the stability in water. C: stability curves from Formula 6.2.1 for a stable protein (Tm = 60 °C, ΔH = 350 kJ/mol, ΔCp = 6 kJ mol⁻¹ K⁻¹) and a destabilized variant (Tm = 45 °C, ΔH = 220 kJ/mol, ΔCp = 9 kJ mol⁻¹ K⁻¹): triangles mark the maximum stability (ΔS = 0), circles the heat and cold denaturation temperatures; cold denaturation occurs at −44 °C for the stable protein but near 0 °C for the variant](./plots/two-state-unfolding.py)

**Example 6.2.1** For the stable protein of the figure ($T_\mathrm{m} = 333.15\ \mathrm{K}$, $\Delta_{\mathrm{U}}H_\mathrm{m} = 350\ \mathrm{kJ\,mol^{-1}}$, $\Delta_{\mathrm{U}}C_p = 6\ \mathrm{kJ\,mol^{-1}\,K^{-1}}$), $T_\mathrm{s} = 333.15\ \mathrm{K} \times \mathrm{e}^{-350/(333.15 \times 6)} = 279.6\ \mathrm{K}$ ($6.5\ ^\circ\mathrm{C}$) and $\Delta_{\mathrm{U}}G^\circ(T_\mathrm{s}) = 28.9\ \mathrm{kJ\,mol^{-1}}$. At $25\ ^\circ\mathrm{C}$, $\Delta_{\mathrm{U}}G^\circ = 25.3\ \mathrm{kJ\,mol^{-1}}$, so $K_\mathrm{U} = \mathrm{e}^{-25.3/2.479} = 3.7\times 10^{-5}$: about one molecule in $27\,000$ is unfolded at any instant; at $37\ ^\circ\mathrm{C}$ ($\Delta_{\mathrm{U}}G^\circ = 19.3\ \mathrm{kJ\,mol^{-1}}$) it is one in $1\,800$. Solving $\Delta_{\mathrm{U}}G^\circ(T) = 0$ numerically gives the cold-denaturation temperature $229\ \mathrm{K}$ ($-44\ ^\circ\mathrm{C}$).

The heat-capacity change is the thermodynamic fingerprint of the hydrophobic effect: it is roughly proportional to the nonpolar surface area exposed on unfolding, about $50$–$60\ \mathrm{J\,mol^{-1}\,K^{-1}}$ per residue. Proteins of thermophiles reach higher $T_\mathrm{m}$ by raising the whole stability curve, by flattening it (a smaller $\Delta_{\mathrm{U}}C_p$), or by shifting it to higher temperature, rather than by a single universal mechanism.

### 6.2.3. Chemical Denaturation and Linear Extrapolation

Denaturants act at room temperature, which makes them convenient for measuring stability. Empirically, the unfolding free energy decreases linearly with denaturant concentration over the transition region:

**Formula 6.2.2 (Linear Extrapolation Model)**

$$
\Delta_{\mathrm{U}}G^\circ([\mathrm{D}]) = \Delta_{\mathrm{U}}G^\circ(\ce{H2O}) - m\,[\mathrm{D}], \qquad C_\mathrm{m} = \frac{\Delta_{\mathrm{U}}G^\circ(\ce{H2O})}{m},
$$
where $[\mathrm{D}]$ is the molar concentration of denaturant, $m$ the *m-value* and $C_\mathrm{m}$ the midpoint concentration.

The $m$-value measures how much more surface the unfolded state exposes to the denaturant, and it is proportional to the change in solvent-accessible surface area on unfolding; for a given protein it is about $2$–$2.5$ times larger for GdnHCl than for urea, which is the more weakly acting denaturant. Fitting the whole transition (panel B of the figure) gives $\Delta_{\mathrm{U}}G^\circ(\ce{H2O})$ by extrapolation to zero denaturant. The extrapolation extends far beyond the data, so $\Delta_{\mathrm{U}}G^\circ(\ce{H2O})$ is less precise than $C_\mathrm{m}$; for comparing mutants, the change in stability $\Delta\Delta G \approx m\,\Delta C_\mathrm{m}$ is often more reliable.

## 6.3. Folding Kinetics and the Energy Landscape

### 6.3.1. Levinthal's Paradox

Proteins fold fast. An *E. coli* cell makes a $100$-residue protein in about $5\ \mathrm{s}$, and small proteins fold in microseconds to seconds. Cyrus Levinthal (1968) pointed out that folding cannot be a random search. Suppose each residue has only three backbone conformations: a $100$-residue chain then has $3^{100} \approx 5\times 10^{47}$ conformations, and sampling them at one per $10^{-13}\ \mathrm{s}$ (a molecular vibration) would take $5\times10^{34}\ \mathrm{s}$, about $1.6\times 10^{27}$ years. With ten conformations per residue the time becomes $10^{87}\ \mathrm{s}$, about $3\times 10^{79}$ years.

**Definition 6.3.1 (Levinthal's Paradox)** **Levinthal's paradox** is the contradiction between the astronomically long time a protein would need to find its native conformation by random search of all conformations and the short times in which proteins actually fold.

The resolution is that the search is biased: partly correct structures are, on average, lower in Gibbs energy and are retained ("cumulative selection"), so the chain does not return to arbitrary conformations. A simple model in the spirit of Zwanzig, Szabo and Bagchi (1992) makes this quantitative. Let each of $N$ residues be either native or in one of $\nu$ non-native conformations; a non-native residue becomes native with rate constant $k_0$, and each native residue is favored by an energy $U$, so that the equilibrium constant for one residue is $K = [\text{non-native}]/[\text{native}] = \nu\,\mathrm{e}^{-U/RT}$. The number $n$ of non-native residues then performs a random walk that can be solved exactly (a birth–death chain), and the mean time to reach $n = 0$ falls exponentially as the bias grows.

![The folding funnel and the resolution of Levinthal's paradox. A: cross-section of a rugged free-energy funnel (schematic): the width at each level stands for the number of conformations; the unfolded ensemble at the top is broad (high entropy), the chain descends through compact molten-globule-like states with much native secondary structure to the narrow native state at the bottom, and local minima on the walls are partly folded intermediates or misfolded kinetic traps that may aggregate. B: mean folding time of the model described in the text (N = 100 residues, ν = 2 non-native conformations per residue, k₀ = 10⁹ s⁻¹), computed exactly as a mean first-passage time: without bias (U = 0, random search) it is about 3 × 10³⁶ s, far longer than the age of the universe; a bias of only 2RT per residue (5 kJ/mol at 25 °C) brings it down to about 1 s](./plots/folding-funnel.py)

### 6.3.2. Folding Pathways and the Funnel

Folding is generally hierarchical. Local secondary structures form first, guided by the propensities of [7.1.5](/7.1.5#sec-5.2) and by ionic interactions between residues near each other in the sequence; elements then pair up into motifs, motifs into domains, and the hydrophobic effect provides entropic stabilization throughout. Proteins whose native contacts are mostly between residues close in sequence (low *contact order*) fold faster than those with many long-range contacts. Domains near the N-terminus can fold while the rest of the chain is still being synthesized on the ribosome.

**Definition 6.3.2 (Folding Funnel)** The **folding funnel** (energy landscape) is the representation of the Gibbs energy of a polypeptide as a function of its conformation: the unfolded states, of high conformational entropy and high Gibbs energy, form the broad top; the conformational space narrows as the chain approaches the native state, which lies at the bottom; local minima on the surface are semistable intermediates.

Funnels differ in shape. A smooth funnel allows many parallel pathways with no significant intermediates (two-state folders); a rugged funnel has semistable intermediates that slow folding and may send molecules into aggregates. A common intermediate is the *molten globule*, a compact state with much native-like secondary structure but fluctuating, poorly packed side chains, which often forms within milliseconds after a chain is diluted out of denaturant. Stability is not uniformly distributed over a structure: a protein may have stable domains joined by disordered linkers, and regions of low stability allow the conformational changes on which function depends ([7.1.7](/7.1.7)).

### 6.3.3. Two-State Kinetics and the Chevron Plot

For a protein that folds without detectable intermediates, $\ce{N <=>[k_\mathrm{u}][k_\mathrm{f}] U}$ is a reversible first-order reaction in both directions. After a sudden change of conditions (rapid mixing into a new denaturant concentration, a temperature jump), the population relaxes to the new equilibrium with a single exponential whose rate constant is the sum of the forward and backward rate constants ([6.3.15](/6.3.15), the **relaxation method**):

$$
f_\mathrm{U}(t) = f_\mathrm{U}^{\mathrm{eq}} + \left[f_\mathrm{U}(0) - f_\mathrm{U}^{\mathrm{eq}}\right]\mathrm{e}^{-k_{\mathrm{obs}}t}, \qquad k_{\mathrm{obs}} = k_\mathrm{f} + k_\mathrm{u}, \qquad K_\mathrm{U} = \frac{k_\mathrm{u}}{k_\mathrm{f}} .
$$

Both rate constants depend exponentially on denaturant concentration, by analogy with Formula 6.2.2 applied to the transition state:

**Formula 6.3.1 (Chevron Plot)**

$$
\ln k_\mathrm{obs} = \ln\left[k_\mathrm{f}(\ce{H2O})\,\mathrm{e}^{-m_\mathrm{f}[\mathrm{D}]/RT} + k_\mathrm{u}(\ce{H2O})\,\mathrm{e}^{m_\mathrm{u}[\mathrm{D}]/RT}\right] .
$$

The plot of $\ln k_\mathrm{obs}$ against $[\mathrm{D}]$ has the shape of a "V" or chevron: at low denaturant $k_\mathrm{f}$ dominates (the folding arm, slope $-m_\mathrm{f}/RT$), at high denaturant $k_\mathrm{u}$ (the unfolding arm, slope $+m_\mathrm{u}/RT$), and the minimum lies at the equilibrium midpoint. Kinetics and equilibrium must agree, which provides a stringent test of the two-state model:

$$
\Delta_{\mathrm{U}}G^\circ(\ce{H2O}) = RT\ln\frac{k_\mathrm{f}(\ce{H2O})}{k_\mathrm{u}(\ce{H2O})}, \qquad m = m_\mathrm{f} + m_\mathrm{u} .
$$

The ratio $\beta_\mathrm{T} = m_\mathrm{f}/m$ (the Tanford β value) places the transition state on the scale from unfolded (0) to native (1) in terms of buried surface; most small proteins have $\beta_\mathrm{T} \approx 0.6$–$0.9$, a compact transition state. Mutations add residue-level detail: the φ-value analysis of Alan Fersht compares the effect of a mutation on the activation Gibbs energy of folding with its effect on stability, $\phi = \Delta\Delta^{\ddagger}G/\Delta\Delta G$; $\phi \approx 1$ means the mutated residue already has native interactions in the transition state, $\phi \approx 0$ that it is still unfolded there. A curvature ("rollover") of the folding arm at low denaturant reveals an intermediate.

![Two-state folding kinetics simulated with k_f(H₂O) = 500 s⁻¹, k_u(H₂O) = 0.05 s⁻¹, m_f = 7 and m_u = 3 kJ mol⁻¹ M⁻¹ at 25 °C. A: chevron plot: the logarithm of the observed relaxation rate constant (points with 5 % noise) against urea concentration is the sum of a folding arm and an unfolding arm (dashed); its minimum is at the midpoint Cm = 2.28 M. B: the equilibrium fraction unfolded predicted from the kinetic parameters (K_U = k_u/k_f) coincides with independent equilibrium data, as the two-state model requires; ΔG(H₂O) = 22.8 kJ/mol, m = 10 kJ mol⁻¹ M⁻¹, βT = 0.7. C: relaxation after jumps to 2 M urea from fully unfolded (refolding) and from fully native (unfolding) protein: both approach the same equilibrium with the same time constant 1/(k_f + k_u) = 430 ms](./plots/chevron-plot.py)

Some slow phases have a chemical origin. About $6\%$ of X–Pro peptide bonds are cis in native proteins, and in an unfolded chain each X–Pro bond is a mixture of cis and trans; molecules with non-native isomers must wait for cis–trans isomerization ($\tau \approx 10$–$100\ \mathrm{s}$ at $25\ ^\circ\mathrm{C}$) before they can fold completely. Formation and reshuffling of disulfides is another slow, chemically limited step. Both are catalyzed in the cell (§6.4.3).

## 6.4. Assisted Folding

### 6.4.1. Molecular Chaperones and the Hsp70 Cycle

Folding in the cell faces difficulties that a dilute test tube does not: the cytoplasm contains $300$–$400\ \mathrm{g\,L^{-1}}$ of macromolecules, nascent chains emerge from the ribosome before they can fold, and stress unfolds existing proteins. Exposed hydrophobic segments of such chains are "sticky" and lead to aggregation.

**Definition 6.4.1 (Molecular Chaperone)** A **molecular chaperone** is a protein that interacts with partly folded or improperly folded polypeptides and facilitates correct folding pathways or provides a microenvironment in which folding can occur, without becoming part of the final structure.

Chaperones do not carry folding information; the native structure is still encoded in the sequence. They work by kinetic partitioning: by binding non-native chains transiently they prevent aggregation and give each chain repeated chances to fold. Two families are best understood, the Hsp70 proteins and the chaperonins (many are *heat shock proteins*, Hsp, whose synthesis increases on heat stress; the number gives the approximate molecular mass in kDa).

Hsp70 proteins (DnaK in *E. coli*) bind short extended segments rich in hydrophobic residues. They consist of a nucleotide-binding domain (NBD) and a substrate-binding domain (SBD) with a helical lid, and they alternate between two states coupled to ATP:

- with ATP bound, the lid is open and the affinity for substrate is low, with fast binding and release;
- a J-domain protein of the Hsp40 family (DnaJ) delivers the substrate and stimulates hydrolysis of ATP; with ADP bound the lid closes over the substrate, which is held with high affinity and slow release;
- a nucleotide-exchange factor (NEF; GrpE in *E. coli*) replaces ADP by ATP, the lid opens and the substrate is released.

Released chains fold, are rebound, or are passed on to a chaperonin. Hsp70 proteins also keep some proteins unfolded until they are translocated across membranes and assist the assembly of oligomers. The principle that ATP binding and hydrolysis switch the affinity of a protein for its partner recurs in motor proteins ([7.1.7](/7.1.7#sec-7.5)).

### 6.4.2. Chaperonins

**Definition 6.4.2 (Chaperonin)** A **chaperonin** is a large, double-ring chaperone complex that encloses a single non-native polypeptide in a central cavity, where it can fold in isolation, in a cycle driven by ATP hydrolysis.

The bacterial chaperonin GroEL consists of two stacked rings of seven $57\ \mathrm{kDa}$ subunits; the heptameric GroES ($10\ \mathrm{kDa}$ subunits) acts as a lid. A substrate binds to hydrophobic residues on the rim of an open ring; binding of seven ATP and GroES to the same ring (the cis ring) causes a large conformational change that buries the hydrophobic sites and releases the substrate into an enlarged, hydrophilic chamber, where it has about $10\ \mathrm{s}$ to fold (while ATP is hydrolyzed). ATP binding to the opposite (trans) ring then releases GroES, ADP and the protein, folded or not; a chain that has not folded is rebound for another cycle. About $10$–$15\%$ of *E. coli* proteins need GroEL/GroES under normal conditions, up to $30\%$ under heat stress. The isolation prevents aggregation and confines the conformational search.

Eukaryotes have two kinds of chaperonin: Hsp60 with its lid Hsp10 in mitochondria, a close homolog of GroEL/GroES (group I), and, in the cytosol, the TRiC/CCT complex (group II, also found in archaea), whose eight different subunits per ring carry a built-in lid instead of a separate GroES. TRiC folds cytoskeletal proteins such as actin and tubulin.

![Chaperone cycles (schematic). A: the Hsp70 cycle: Hsp70 with ATP (lid of the substrate-binding domain open) binds a hydrophobic segment of an unfolded substrate weakly and rapidly; Hsp40 stimulates ATP hydrolysis and the lid closes, holding the substrate tightly; a nucleotide-exchange factor exchanges ADP for ATP, the lid opens and the substrate is released to fold or to be rebound. B: the GroEL/GroES cycle, side view of the two heptameric rings: the substrate binds the hydrophobic rim of an open ring; binding of seven ATP and GroES closes a hydrophilic folding chamber in which the protein folds for about 10 s; ATP binding to the opposite ring releases GroES, ADP and the protein](./plots/chaperone-cycles.py)

### 6.4.3. Folding Catalysts

Two kinds of enzyme accelerate chemically slow steps of folding:

- *Protein disulfide isomerase* (PDI), abundant in the endoplasmic reticulum, has thioredoxin-like domains with CXXC active sites that catalyze the formation, reduction and exchange ("shuffling") of disulfide bonds, so that non-native pairings are eliminated until the native set is reached, the cellular counterpart of the trace of 2-mercaptoethanol in Anfinsen's experiment.
- *Peptidyl-prolyl cis–trans isomerases* (PPIases) catalyze the isomerization of X–Pro peptide bonds. The two main families, the cyclophilins and the FKBPs, were discovered independently as the receptors of the immunosuppressive drugs cyclosporin A and FK506 (tacrolimus), whose drug–isomerase complexes inhibit the phosphatase calcineurin.

## 6.5. Misfolding and Disease

### 6.5.1. Amyloid

Misfolding is a substantial problem in all cells: a quarter or more of newly synthesized polypeptides may be degraded because they fail to fold correctly. In some cases misfolded proteins form a highly ordered, alternative structure.

**Definition 6.5.1 (Amyloid)** An **amyloid fibril** is an unbranched protein fiber, $7$–$10\ \mathrm{nm}$ in diameter, whose core is a cross-β structure: β strands run perpendicular to the fiber axis and are hydrogen-bonded along it ($0.47\ \mathrm{nm}$ apart), forming sheets that stack $\approx 1\ \mathrm{nm}$ apart; diseases caused by amyloid deposits are **amyloidoses**.

Many unrelated proteins can adopt the amyloid structure as an alternative to their native fold; the cross-β core is stabilized by backbone hydrogen bonds common to all chains, and often by stacked aromatic side chains. Formation is a nucleated polymerization: a few incompletely folded molecules associate through their β-prone segments into an unfavorable nucleus, after which further molecules add rapidly to the fiber ends. The kinetics therefore has a lag phase that can be shortened by adding preformed fibrils (seeding), and because most molecules fold normally, symptoms often appear slowly and late in life; a mutation that favors aggregation brings the onset earlier.

| Disease | Protein | Location of the aggregates |
|---|---|---|
| Alzheimer disease | amyloid-β peptide (from the transmembrane amyloid precursor protein, APP); tau | extracellular plaques; intracellular tangles |
| Parkinson disease | α-synuclein | intracellular Lewy bodies |
| Huntington disease | huntingtin with an expanded polyglutamine tract (more than about $36$–$40$ Gln) | intracellular aggregates |
| Type 2 diabetes | islet amyloid polypeptide (amylin) | pancreatic islets |
| Systemic amyloidoses | transthyretin, immunoglobulin light chains and others | many tissues |

In Alzheimer disease, proteolytic cleavage of APP releases the amyloid-β peptide; separated from the membrane, its two α-helical segments lose their structure and the peptide assembles into fibrils made of parallel β sheets. Whether the fibrils themselves, smaller soluble oligomers, or the tau aggregates are mainly responsible for the death of neurons is still debated. Antibodies that remove amyloid-β plaques (lecanemab, approved 2023; donanemab, 2024) modestly slow cognitive decline in early disease, which supports a causal role for amyloid-β. Inherited mutations in tau do not cause Alzheimer disease but cause frontotemporal dementia. In *Drosophila* expressing the human proteins of Parkinson or Huntington disease, neurodegeneration is strongly suppressed by overexpression of Hsp70, which shows the protective role of chaperones.

### 6.5.2. Prions

A remarkable form of misfolding is transmissible.

**Definition 6.5.2 (Prion)** A **prion** is an infectious agent consisting only of a misfolded protein that propagates by converting the normally folded form of the same protein into its own misfolded form.

The prion diseases (transmissible spongiform encephalopathies: bovine spongiform encephalopathy, Creutzfeldt–Jakob disease and kuru in humans, scrapie in sheep, chronic wasting disease in deer and elk) are fatal neurodegenerations in which the brain becomes riddled with vacuoles. In the 1960s the infectious agent was found to resist treatments that destroy nucleic acids, and Tikvah Alper proposed that it was a protein; Stanley Prusiner identified the prion protein PrP ($M_\mathrm{r}$ $28\,000$; Nobel Prize in Physiology or Medicine 1997). The normal cellular form $\mathrm{PrP^C}$, a glycosylated membrane protein of neurons whose function is still unclear, has a flexible N-terminal segment and a globular C-terminal domain with three α helices and a short two-stranded β sheet. The disease form $\mathrm{PrP^{Sc}}$ has the same sequence but is rich in β structure and forms protease-resistant amyloid; $\mathrm{PrP^{Sc}}$ acts as a template that converts $\mathrm{PrP^C}$, so the misfolded form multiplies. Mice lacking the PrP gene are healthy and cannot be infected. Inherited prion diseases are caused by point mutations that make conversion more likely. Cryo-EM structures of infectious prion fibrils (2021) show stacked, in-register parallel β sheets, as in other amyloids. Prion-like seeded spreading from cell to cell has since been demonstrated for α-synuclein, tau and amyloid-β.

### 6.5.3. Loss of Function by Misfolding

Misfolding can cause disease without amyloid, by loss of the protein. Cystic fibrosis is caused by defects in CFTR, a chloride channel of epithelial membranes ([7.1.13](/7.1.13)); the most common mutation, deletion of Phe508 (ΔF508), destabilizes a nucleotide-binding domain so that most of the protein is recognized by quality control in the endoplasmic reticulum and degraded. Small molecules called *correctors* (pharmacological chaperones) bind and stabilize the mutant protein; the combination of the correctors elexacaftor and tezacaftor with the channel potentiator ivacaftor (approved 2019) restores enough function to transform the treatment of most patients. Many disease-causing collagen mutations ([7.1.5](/7.1.5#sec-5.3.3)) also act through defective folding.

## 6.6. Determining Protein Structures

### 6.6.1. X-ray Crystallography

Objects smaller than about half the wavelength of light cannot be resolved by a light microscope; atoms require X-rays of wavelength $0.07$–$0.15\ \mathrm{nm}$. Since there are no lenses for X-rays, the image is reconstructed computationally from the diffraction pattern, the computer acting as a "computational lens". The steps are:

1. purify the protein and grow well-ordered crystals (often the hardest step; protein crystals contain $30$–$70\%$ solvent);
2. record the positions and intensities of the diffraction spots (reflections) in an X-ray beam, today mostly at synchrotrons; the geometry of the reflections is governed by the Bragg condition of **X-ray diffraction** ([6.4.8](/6.4.8));
3. compute the electron density as a **Fourier transform** of the reflections,

$$
\rho(x, y, z) = \frac{1}{V}\sum_{h,k,l} \lvert F_{hkl}\rvert\, \mathrm{e}^{\mathrm{i}\alpha_{hkl}}\, \mathrm{e}^{-2\pi\mathrm{i}(hx + ky + lz)},
$$
where $V$ is the volume of the unit cell and $F_{hkl}$ the structure factor of reflection $hkl$;
4. fit the amino acid sequence into the density and refine the model.

The measured intensities give only the amplitudes $\lvert F_{hkl}\rvert^2$; the phases $\alpha_{hkl}$ are lost (the *phase problem*). They are recovered by molecular replacement (using a known similar structure, or today a predicted one), by isomorphous replacement with heavy-atom derivatives (the method of Perutz and Kendrew), or by anomalous scattering from selenomethionine or metal atoms. The resolution $d_\mathrm{min} = \lambda/(2\sin\theta_\mathrm{max})$ determines what is seen: at $0.3\ \mathrm{nm}$ the path of the chain and most side chains, at $0.2\ \mathrm{nm}$ individual atoms of side chains and bound water, below $0.12\ \mathrm{nm}$ some hydrogen atoms, which otherwise scatter too weakly to be seen.

Kendrew's myoglobin crystals gave nearly $25\,000$ reflections; the resolution was improved in stages until in 1959 the positions of almost all non-hydrogen atoms were determined, and the model agreed with the chemically determined sequence. A crystal averages over time and over millions of molecules and offers little information about motion, and crystal contacts can occasionally distort a structure; but comparison with solution methods shows that crystal structures almost always represent functional conformations. X-ray crystallography accounts for most of the structures in the PDB.

### 6.6.2. Nuclear Magnetic Resonance

**Nuclear magnetic resonance** spectroscopy ([6.4.12](/6.4.12)) studies proteins in solution and can follow conformational changes, folding and binding. $^1\mathrm{H}$ is the most sensitive nucleus, but even a small protein has hundreds of protons whose one-dimensional spectrum overlaps hopelessly; structure determination became possible with **two-dimensional NMR** and its multidimensional extensions, together with uniform labeling with $^{13}\mathrm{C}$ and $^{15}\mathrm{N}$ by expression in bacteria grown on labeled nutrients.

- TOCSY and related through-bond experiments connect nuclei within a residue and assign each signal to an atom, using the known sequence.
- NOESY detects the nuclear Overhauser effect between protons close in space (less than about $0.5\ \mathrm{nm}$), whose intensity falls as $r^{-6}$, and thus gives distance restraints between atoms that may be far apart in sequence.
- A computer finds all conformations consistent with hundreds to thousands of restraints and with known covalent geometry (bond lengths and angles, chirality, van der Waals radii). The result is an ensemble of similar structures whose spread reflects both the uncertainty of the restraints and real motions ("breathing") of the molecule.

NMR works best for proteins smaller than about $30$–$50\ \mathrm{kDa}$ (larger with special techniques such as TROSY and selective labeling), because large molecules tumble slowly and their signals broaden.

### 6.6.3. Cryo-Electron Microscopy

Large dynamic complexes and membrane proteins often refuse to crystallize and are too large for NMR. Electron microscopy can image them, but the electron beam destroys biological specimens before a high-resolution image accumulates.

**Definition 6.6.1 (Cryo-Electron Microscopy)** In single-particle **cryo-electron microscopy** (cryo-EM), a solution of many copies of a macromolecule is frozen so rapidly that the water forms vitreous (noncrystalline) ice; the molecules, in random orientations, are imaged at low electron dose, and tens of thousands to millions of noisy two-dimensional projections are classified, aligned and combined computationally into a three-dimensional density map.

The reconstruction rests on the projection–slice theorem: the two-dimensional Fourier transform of each projection is a central slice of the three-dimensional Fourier transform of the object, so enough projections at known orientations fill Fourier space. Around 2013, direct electron detectors (which record individual electrons fast enough to correct for beam-induced motion) and maximum-likelihood image processing produced a "resolution revolution": the structure of the TRPV1 ion channel at $0.34\ \mathrm{nm}$ (Liao, Cao, Julius and Cheng, 2013) was one of the first atomic models of a membrane protein obtained without crystals, and resolutions better than $0.2\ \mathrm{nm}$ are now reached for favorable samples. The Nobel Prize in Chemistry 2017 was awarded to Jacques Dubochet, Joachim Frank and Richard Henderson for the development of cryo-EM. Because each particle is imaged individually, cryo-EM can sort a heterogeneous sample into several conformational states, and it needs only small amounts of material: the architecture of human telomerase was determined from quantities far too small for crystallization. Cryo-electron tomography extends the approach to complexes inside cells.

### 6.6.4. Comparison of the Methods

| | X-ray crystallography | NMR | Cryo-EM |
|---|---|---|---|
| Sample | crystal | concentrated solution, isotope labeled | thin vitreous ice, microgram amounts |
| Size range | no upper limit (ribosomes, viruses) | best below $\sim 50\ \mathrm{kDa}$ | best above $\sim 50\ \mathrm{kDa}$; complexes and membrane proteins |
| Typical resolution | $0.1$–$0.3\ \mathrm{nm}$ | ensemble from distance restraints | $0.2$–$0.4\ \mathrm{nm}$ |
| Hydrogen atoms | only at very high resolution | many observed directly | not resolved |
| Dynamics | little (time- and space-averaged) | motions on ps–s time scales, folding, binding | multiple conformational states by classification |
| Main limitation | crystallization; crystal contacts | size; spectral assignment | small or very flexible particles; specimen preparation |

### 6.6.5. Structure Prediction and Design

Computation has become a full partner of experiment. Molecular dynamics simulations, which integrate Newton's equations for all atoms of a protein and its solvent, were made possible by the work of Martin Karplus, Michael Levitt and Arieh Warshel (Nobel Prize in Chemistry 2013) and can now follow the folding of small proteins atom by atom. The Rosetta programs of David Baker's group predict structures by searching for low-energy conformations; the projects Rosetta@home and Foldit enlisted volunteers, the latter as a video game in which players improved designed enzymes, including a Diels–Alderase, a reaction almost unknown among natural enzymes.

The decisive advance came from deep learning. AlphaFold2 (DeepMind, 2020–2021) predicted the structures of single protein chains in the blind assessment CASP14 with accuracy comparable to experiment for most targets, by learning from the PDB and from the patterns of correlated mutations in multiple sequence alignments. Its database now contains predictions for more than $200$ million proteins, essentially every sequenced protein, each with a per-residue confidence score (pLDDT); regions of low confidence often correspond to intrinsically disordered segments ([7.1.5](/7.1.5#sec-5.4.3)). AlphaFold 3 (2024) and similar methods extend prediction to complexes with other proteins, nucleic acids and small molecules, while generative methods design new proteins with chosen shapes and functions. The Nobel Prize in Chemistry 2024 was awarded to David Baker for computational protein design and to Demis Hassabis and John Jumper for protein structure prediction. Predictions do not replace experiment: they give one static model, are less reliable for conformational changes, the effects of point mutations and novel complexes, and are themselves trained on the structures that X-ray crystallography, NMR and cryo-EM produced.

## Summary

| Topic | Key relations and facts |
|---|---|
| Denaturation (Definition 6.1.2) | heat, pH, solvents, urea, GdnHCl, detergents; no covalent bonds broken |
| Anfinsen (Proposition 6.1.1) | sequence determines structure; random pairing of 8 Cys gives $1/105 \approx 1\%$ active enzyme |
| Two-state model (Definition 6.2.1) | $K_\mathrm{U} = [\mathrm{U}]/[\mathrm{N}]$, $\Delta_{\mathrm{U}}G^\circ = -RT\ln K_\mathrm{U}$; half-denatured solution = half folded + half unfolded |
| Stability curve (Formula 6.2.1) | Gibbs–Helmholtz with $\Delta_{\mathrm{U}}C_p > 0$; maximum at $\Delta_{\mathrm{U}}S = 0$; heat and cold denaturation; stabilities $20$–$60\ \mathrm{kJ\,mol^{-1}}$ |
| Chemical denaturation (Formula 6.2.2) | $\Delta_{\mathrm{U}}G^\circ = \Delta_{\mathrm{U}}G^\circ(\ce{H2O}) - m[\mathrm{D}]$, $C_\mathrm{m} = \Delta_{\mathrm{U}}G^\circ(\ce{H2O})/m$ |
| Levinthal's paradox (Definition 6.3.1) | random search $\sim 10^{27}$ years or more; a bias of $\sim 2RT$ per residue brings it to seconds |
| Folding funnel (Definition 6.3.2) | hierarchical folding, molten globule, intermediates and traps |
| Chevron plot (Formula 6.3.1) | $k_\mathrm{obs} = k_\mathrm{f} + k_\mathrm{u}$; $\Delta_{\mathrm{U}}G^\circ = RT\ln(k_\mathrm{f}/k_\mathrm{u})$, $m = m_\mathrm{f} + m_\mathrm{u}$; $\beta_\mathrm{T} = m_\mathrm{f}/m$; φ values |
| Chaperones (Definitions 6.4.1, 6.4.2) | Hsp70/Hsp40/NEF: ATP open/low affinity, ADP closed/high affinity; GroEL/GroES: 7 ATP, closed chamber, $\sim 10\ \mathrm{s}$; TRiC in the eukaryotic cytosol; PDI and PPIases catalyze slow chemical steps |
| Misfolding (Definitions 6.5.1, 6.5.2) | cross-β amyloid, nucleated polymerization; Aβ, tau, α-synuclein, huntingtin, amylin; prions template their own conformation; ΔF508 CFTR and correctors |
| Structure determination | X-ray: Fourier synthesis, phase problem, resolution; NMR: NOE distances $< 0.5\ \mathrm{nm}$, ensembles, small proteins; cryo-EM (Definition 6.6.1): single particles in vitreous ice; AlphaFold and design (Nobel 2024) |

## Questions

1. A protein has $C_\mathrm{m} = 3.0\ \mathrm{M}$ urea and $m = 8.0\ \mathrm{kJ\,mol^{-1}\,M^{-1}}$ at $25\ ^\circ\mathrm{C}$. What is its stability in water, and what fraction of the molecules is unfolded in $2.0\ \mathrm{M}$ urea? A mutant has $C_\mathrm{m} = 2.5\ \mathrm{M}$ with the same $m$; by how much is it destabilized?

   **Answer** $\Delta_{\mathrm{U}}G^\circ(\ce{H2O}) = mC_\mathrm{m} = 24.0\ \mathrm{kJ\,mol^{-1}}$. In $2.0\ \mathrm{M}$ urea, $\Delta_{\mathrm{U}}G^\circ = 24.0 - 16.0 = 8.0\ \mathrm{kJ\,mol^{-1}}$, so $K_\mathrm{U} = \mathrm{e}^{-8.0/2.479} = 0.040$ and $f_\mathrm{U} = 0.040/1.040 = 3.8\%$. The mutant is destabilized by $\Delta\Delta G = m\,\Delta C_\mathrm{m} = 8.0 \times 0.5 = 4.0\ \mathrm{kJ\,mol^{-1}}$.
2. Why does a large positive $\Delta_{\mathrm{U}}C_p$ imply that a protein must also denature at low temperature? Use Formula 6.2.1.

   **Answer** Differentiating twice, $\partial^2 \Delta_{\mathrm{U}}G^\circ/\partial T^2 = -\Delta_{\mathrm{U}}C_p/T < 0$, so the stability curve is concave with a single maximum at $T_\mathrm{s}$ (where $\Delta_{\mathrm{U}}S = 0$). A concave function that is positive at $T_\mathrm{s}$ and zero at $T_\mathrm{m} > T_\mathrm{s}$ must also fall to zero at some $T < T_\mathrm{s}$ (as $T \to 0$, the term $-\Delta_{\mathrm{U}}C_p T\ln(T/T_\mathrm{m})$ vanishes and the constant terms $\Delta_{\mathrm{U}}H_\mathrm{m} - \Delta_{\mathrm{U}}C_p T_\mathrm{m}$ are negative whenever $\Delta_{\mathrm{U}}C_p T_\mathrm{m} > \Delta_{\mathrm{U}}H_\mathrm{m}$, as for real proteins). Physically, $\Delta_{\mathrm{U}}C_p > 0$ means that $\Delta_{\mathrm{U}}H$ decreases on cooling and becomes negative below a certain temperature: the hydration of exposed nonpolar groups becomes enthalpically favorable and the hydrophobic effect weakens, so the entropy of the chain wins again. The larger $\Delta_{\mathrm{U}}C_p$, the more sharply curved the stability curve and the closer the cold-denaturation temperature is to $T_\mathrm{s}$.
3. In a refolding experiment monitored by Trp fluorescence, 85% of the amplitude appears with $k = 30\ \mathrm{s^{-1}}$ and 15% with $k = 0.03\ \mathrm{s^{-1}}$. The slow phase disappears when the protein is unfolded for only a few seconds before refolding ("double jump"), and is accelerated by cyclophilin. What is its origin?

   **Answer** It is limited by cis–trans isomerization of an X–Pro peptide bond. In the native protein that bond has one configuration (say cis). In the unfolded chain it slowly equilibrates (time constant of tens of seconds) to a mixture in which about 15% of the molecules have the native isomer and the rest the non-native one; molecules with a non-native isomer can fold only after isomerization. After a short unfolding time the isomers have not yet re-equilibrated, so nearly all molecules still have the native isomer and fold fast. A peptidyl-prolyl isomerase such as cyclophilin catalyzes the isomerization and accelerates the slow phase.
4. Estimate the Levinthal search time for a 150-residue protein with two conformations per residue, sampled at $10^{13}\ \mathrm{s^{-1}}$. Why does the answer not mean that folding proteins search less than all conformations "by luck"?

   **Answer** $2^{150} \approx 1.4\times 10^{45}$ conformations, so random sampling would take $1.4\times10^{32}\ \mathrm{s}$, about $4\times 10^{24}$ years. Folding in milliseconds therefore cannot be a lucky random search; it requires that the energy landscape be funneled, so that each step that forms native interactions lowers the Gibbs energy on average and native structure, once formed, tends to be retained. In the model of the funnel figure, a bias of about $2RT$ per residue is enough.
5. GroEL/GroES encloses one substrate at a time and needs seven ATP per cycle. Why is it nevertheless not needed by most *E. coli* proteins, and which proteins depend on it?

   **Answer** Most proteins fold fast enough, on the ribosome or shortly after release, often helped only by trigger factor and Hsp70, that they rarely aggregate; for them the large ATP cost and the size limit of the chamber (about $60\ \mathrm{kDa}$) would be pointless. GroEL is required by proteins that fold slowly and tend to aggregate: typically $20$–$60\ \mathrm{kDa}$ proteins with complex α/β topologies (for example TIM barrels) and many long-range contacts, which spend a long time in sticky intermediates. Under heat stress more proteins become dependent on it.
6. Which method would you choose to determine (a) the structure of a $15\ \mathrm{kDa}$ soluble domain and its motions on binding a peptide, (b) a $900\ \mathrm{kDa}$ membrane complex that resists crystallization, and (c) the positions of protons in the active site of an enzyme? Justify each choice.

   **Answer** (a) NMR: the domain is small enough, can be labeled with $^{15}\mathrm{N}$ and $^{13}\mathrm{C}$, and NMR measures binding and dynamics in solution (chemical-shift changes, relaxation); X-ray would give a higher-resolution static structure if crystals form. (b) Single-particle cryo-EM: it needs no crystals, works best for large particles, tolerates detergent- or nanodisc-solubilized membrane proteins, and can separate several conformations. (c) X-ray crystallography at ultrahigh resolution (better than about $0.1\ \mathrm{nm}$), or better neutron crystallography, in which hydrogen (deuterium) scatters strongly; NMR can also identify protonation states of particular residues.
