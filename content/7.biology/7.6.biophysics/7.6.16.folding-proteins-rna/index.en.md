---
title: Folding of Proteins and RNA
description: "The physics of how a chain finds its structure. Marginal stability and its measurement; Levinthal's estimate and the Zwanzig model solved exactly as a first-passage problem; the random-energy model, the glass temperature and the principle of minimal frustration; free-energy profiles in the fraction of native contacts; two-state kinetics, the Kramers prefactor and the folding speed limit; transition states probed by phi-value analysis and Leffler plots; contact order; compact random walks, the HP lattice model and designability by exact enumeration; scaling of intrinsically disordered chains; folding in the cell, the competition with aggregation and the nucleated growth of amyloid; RNA folding: hierarchy, nearest-neighbour thermodynamics, counterions and magnesium, kinetic traps and kinetic partitioning, cotranscriptional folding and kinetic control of riboswitches; the experimental methods of folding kinetics."
---

A protein or an RNA is synthesized as a linear chain and works as a folded three-dimensional object. How the sequence specifies the structure, how stable the structure is, and how the chain finds it in milliseconds among an astronomical number of alternatives is the folding problem, one of the oldest questions of molecular biophysics. It has three parts: the thermodynamic question (which interactions make the native state the state of lowest free energy, and by how much), the kinetic question (by which routes and how fast the chain reaches it), and the computational question of predicting the structure from the sequence. This chapter treats the first two; prediction is the subject of [7.6.15](/7.6.15).

The biochemical side of protein folding is in [7.1.6](/7.1.6): denaturation and Anfinsen's experiment, the **two-state model** of stability with the stability curve and linear extrapolation, Levinthal's estimate, the **folding funnel**, the chevron plot, **molecular chaperones** and amyloid. Here the same phenomena are treated as problems of statistical physics, building on the Boltzmann statistics of [7.6.2](/7.6.2), the two-state systems of [7.6.4](/7.6.4), Kramers' theory of barrier crossing and first-passage times in [7.6.5](/7.6.5) and the forces of [7.6.6](/7.6.6). The chapter first quantifies stability (16.1), then develops the theory of energy landscapes (16.2) and of folding kinetics and transition states (16.3), solves lattice models exactly (16.4), turns to chains that do not fold (16.5) and to folding in the crowded cell, with its failure mode, aggregation (16.6), and ends with RNA, whose folding follows different rules (16.7). The experimental methods used throughout were developed in earlier chapters: calorimetry ([7.6.8](/7.6.8)), circular dichroism and fluorescence ([7.6.11](/7.6.11)), single-molecule FRET ([7.6.12](/7.6.12)), hydrogen exchange and relaxation dispersion in NMR ([7.6.13](/7.6.13)); mechanical unfolding with force probes follows in [7.6.17](/7.6.17), and the polymer physics of long chains in [7.6.21](/7.6.21).

## 16.1. Stability

### 16.1.1. Three Questions and a Hypothesis

The modern study of folding starts from two observations. Wu Xian (1931) proposed that denaturation is the disruption of the compact native conformation, held together by noncovalent interactions, without breaking the covalent chain. Anfinsen showed in the 1960s that ribonuclease A, reduced and unfolded in urea, regains its native structure and activity when the denaturant is removed: the sequence contains all the information needed to specify the structure, and the native state is the state of lowest Gibbs energy under physiological conditions (the thermodynamic hypothesis, [7.1.6](/7.1.6#sec-6.1.2)). The total chemical synthesis of crystalline active bovine insulin in Shanghai (1965), which required the correct pairing of the disulfide bonds between two chains, was an early demonstration of the same principle on a synthetic protein.

The thermodynamic hypothesis turns structure into a minimization problem and folding into a relaxation towards equilibrium. Neither is simple. The free energy that is minimized is a small difference between large terms (16.1.2), and the relaxation has to cross a configuration space whose size makes random search impossible (16.2).

### 16.1.2. Marginal Stability

For a single-domain protein that unfolds in one cooperative step, the stability is the Gibbs energy of unfolding $\Delta G_{\mathrm{U}} = G_{\mathrm{U}} - G_{\mathrm{N}} = -RT\ln K$, with $K = [\mathrm{U}]/[\mathrm{N}]$ ([7.1.6](/7.1.6#def-6.2.1)). Typical values are $20$–$60\,\mathrm{kJ\,mol^{-1}}$ ($5$–$15\,\mathrm{kcal\,mol^{-1}}$) at $25\,^\circ\mathrm{C}$, that is $8$–$25\,k_{\mathrm{B}}T$ per molecule. This is the energy of a few hydrogen bonds or of burying a few hydrophobic side chains, although folding forms hundreds of such contacts. The native state is stable only by a small margin.

The margin is small because large terms nearly cancel. Folding buries nonpolar surface (favourable through the **hydrophobic effect**, [7.6.6](/7.6.6#sec-6.3.2)), forms hydrogen bonds and van der Waals contacts within the protein that replace similar contacts with water, and costs the **conformational entropy** of the chain, roughly $10$–$20\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per residue, about $T\Delta S \approx 400$–$600\,\mathrm{kJ\,mol^{-1}}$ for a $100$-residue protein at room temperature. The decomposition of $\Delta G_{\mathrm{U}}$ into enthalpy, entropy and heat capacity, and the stability curve with its maximum and cold denaturation, are derived from calorimetry in [7.6.8](/7.6.8#sec-8.3.1).

Marginal stability has two consequences. First, single mutations matter: a core mutation that removes a methyl group typically costs $4$–$6\,\mathrm{kJ\,mol^{-1}}$ and can unfold a marginally stable protein, which is the molecular basis of many loss-of-function alleles and temperature-sensitive mutants. Second, stability is not maximized by evolution. Most random mutations are destabilizing; under selection only for being folded, a protein drifts towards the lowest stability that still keeps it folded, and the marginal stability of natural proteins is largely what this mutation–selection balance predicts ([7.6.41](/7.6.41)). Function adds a second reason: catalysis, binding and allostery require conformational fluctuations that a very stable protein would suppress. Proteins of hyperthermophiles and some proteins used in the laboratory, such as streptavidin, show that much higher stabilities ($\Delta G_{\mathrm{U}} \gtrsim 60\,\mathrm{kJ\,mol^{-1}}$) are physically attainable.

Thermodynamic stability is distinct from kinetic stability, the lifetime $1/k_{\mathrm{u}}$ of the native state set by the barrier to unfolding. A protein can be thermodynamically marginal but kinetically persistent (α-lytic protease, whose native state is less stable than the unfolded state but unfolds with a half-life of a year), and degradation, translocation through membranes and aggregation are often governed by $k_{\mathrm{u}}$ rather than by $\Delta G_{\mathrm{U}}$.

### 16.1.3. Measuring Stability

Because the unfolded fraction under native conditions is tiny ($\mathrm{e}^{-\Delta G_{\mathrm{U}}/RT} \approx 10^{-4}$–$10^{-10}$), stability is measured by shifting the equilibrium with a denaturant or with temperature and extrapolating back. A spectroscopic signal $y$ (tryptophan fluorescence, far-UV CD at $222\,\mathrm{nm}$) that depends linearly on the populations gives the equilibrium constant in the transition region,

$$
K = \frac{y_{\mathrm{N}} - y}{y - y_{\mathrm{U}}},
$$
with $y_{\mathrm{N}}$ and $y_{\mathrm{U}}$ the baselines of the pure states, extrapolated linearly into the transition.

**Example 16.1.1 (A Urea Melt)** In a urea titration followed by intrinsic tryptophan fluorescence, the Gibbs energy of unfolding in the transition region falls linearly with urea concentration, $\Delta G_{\mathrm{U}} = \Delta G_{\mathrm{U}}(\ce{H2O}) - m[\text{urea}]$, with $m = 3.9\,\mathrm{kJ\,mol^{-1}\,M^{-1}}$ ($0.93\,\mathrm{kcal\,mol^{-1}\,M^{-1}}$) and $\Delta G_{\mathrm{U}}(\ce{H2O}) = 9.8\,\mathrm{kJ\,mol^{-1}}$ ($2.34\,\mathrm{kcal\,mol^{-1}}$). The midpoint is at $C_{\mathrm{m}} = \Delta G_{\mathrm{U}}(\ce{H2O})/m = 2.5\,\mathrm{M}$, and at $25\,^\circ\mathrm{C}$ in water $K = \mathrm{e}^{-9.8/2.48} = 0.019$: about $2\,\%$ of the molecules are unfolded at any moment. The $m$ value measures how much surface is exposed on unfolding; empirically (Myers, Pace and Scholtz 1995) $m/(\mathrm{cal\,mol^{-1}\,M^{-1}}) \approx 374 + 0.11\,\Delta\mathrm{ASA}/\text{Å}^2$ for urea, where $\Delta\mathrm{ASA}$ is the accessible surface area exposed on unfolding, so this protein exposes about $5000\,\text{Å}^2$ ($50\,\mathrm{nm^2}$), as expected for a small domain of $50$–$60$ residues.

The linear extrapolation is an empirical rule (the linear extrapolation model, [7.1.6](/7.1.6#fml-6.2.2)); it works because denaturants act by preferential interaction with the exposed surface, roughly in proportion to its area. Thermal melts give $T_{\mathrm{m}}$, $\Delta H$ and, by calorimetry, $\Delta C_p$; their extrapolation to room temperature requires the full stability curve ([7.6.8](/7.6.8)) and fails for proteins that aggregate on heating. Native-state hydrogen exchange measures stability without any extrapolation: an amide proton exchanges only when the structure that protects it opens, and the protection factor of the most protected amides equals $1/K$ of global unfolding ([7.6.13](/7.6.13#sec-13.6.5)).

## 16.2. Energy Landscapes

### 16.2.1. The Size of Conformation Space

Levinthal's argument ([7.1.6](/7.1.6#def-6.3.1)) counts conformations: with three backbone conformations per residue, a $100$-residue chain has $3^{100} \approx 5\times10^{47}$ of them, and sampling one per $10^{-13}\,\mathrm{s}$ would take about $10^{27}$ years. Proteins fold in microseconds to seconds, so folding is not a random search. Even a coarse lattice model makes the same point: on a cubic lattice each bond can point in six directions, $6^{100} \approx 6.5\times10^{77}$ walks for a $100$-mer, and an exhaustive search at $10^{15}$ conformations per second would last $10^{55}$ years.

Counting says what folding is not. A theory must say what it is: a biased diffusion on a free-energy surface whose overall slope points towards the native state. Three models make this quantitative: a solvable model of independent residues (16.2.2), the statistical mechanics of random heteropolymers (16.2.3), and the free-energy profile along a reaction coordinate (16.2.4).

### 16.2.2. The Zwanzig Model

Zwanzig, Szabo and Bagchi (1992) asked how large a bias towards the native state is needed to turn a Levinthal search into a fast relaxation.

**Definition 16.2.1 (Zwanzig Model)** In the *Zwanzig model* each of $N$ residues is either in its single correct conformation or in one of $\nu$ incorrect ones, and every incorrect residue raises the energy by $U$. Residues change conformation independently: an incorrect residue becomes correct with rate $k_0$, a correct one becomes incorrect with rate $\nu k_0\mathrm{e}^{-U/k_{\mathrm{B}}T}$, the ratio required by detailed balance. The native state has all residues correct.

Lumping the states by the number $n$ of incorrect residues gives a one-dimensional random walk on $n = 0, 1, \dots, N$: the **birth–death process** with death rate $d_n = nk_0$ and birth rate $b_n = (N - n)\nu k_0\mathrm{e}^{-\beta U}$, where $\beta = 1/k_{\mathrm{B}}T$. Its equilibrium distribution is the binomial weight of $n$ incorrect residues,

$$
\pi_n \propto \binom{N}{n}\left(\nu\mathrm{e}^{-\beta U}\right)^n, \qquad \frac{F(n)}{k_{\mathrm{B}}T} = n\beta U - \ln\left[\binom{N}{n}\nu^n\right] + \mathrm{const}.
$$

**Theorem 16.2.1 (Folding Time of the Zwanzig Model)** The mean first-passage time from $n = N$ (all residues incorrect) to the native state $n = 0$ is

$$
\tau = \sum_{j=1}^{N}\frac{1}{d_j\pi_j}\sum_{i=j}^{N}\pi_i .
$$
Without bias ($U = 0$) and for large $N$, $\tau \approx (1 + \nu)^N/(N\nu k_0)$, a Levinthal time. With bias, for $\nu\mathrm{e}^{-\beta U} \ll 1$, $\tau$ grows only slowly with $N$.

**Proof** To reach $0$ the walk must pass through every intermediate $n$, so $\tau = \sum_j \tau_j$, where $\tau_j$ is the mean time to go from $j$ to $j - 1$ for the first time. Consider the walk restricted to $\{j, \dots, N\}$ with $j - 1$ absorbing. In its stationary flux picture, the probability current through the bond $j \to j-1$ equals $d_j$ times the probability of being at $j$; renormalizing the equilibrium weights over $\{j,\dots,N\}$, the mean time between exits is the inverse of that current, $\tau_j = \sum_{i \ge j}\pi_i/(d_j\pi_j)$. (Equivalently, the recursion $\tau_j = 1/d_j + (b_j/d_j)\tau_{j+1}$ obtained by conditioning on the first step, together with detailed balance $b_j\pi_j = d_{j+1}\pi_{j+1}$, gives the same sum.) For $U = 0$ the sum is dominated by $j = 1$: $\tau_1 = \sum_{i\ge1}\pi_i/(d_1\pi_1) = [(1+\nu)^N - 1]/(k_0 N\nu)$. $\square$

![The Zwanzig model with ν = 2 incorrect conformations per residue and k₀ = 10⁹ s⁻¹, solved exactly. A: free-energy profile along the number n of incorrect residues for a 100-residue chain: without bias the entropy of the many incorrect states makes the profile slope away from the native state (minimum at n = 67); a bias of a few k_BT per residue tilts it towards n = 0. B: mean first-passage time from the fully incorrect chain to the native state against chain length: without bias it follows the Levinthal time (1 + ν)^N/k₀ and exceeds the age of the universe for N ≈ 80; a bias of 2 k_BT per residue brings a 100-residue chain to about 1 s and 3 k_BT to microseconds. C: the equilibrium fraction of the fully native state when that state is given an extra stability ΔE: with independent residues the native state is negligible (for U = 2 k_BT, 21 % of residues are incorrect at equilibrium) unless ΔE exceeds N ln(1 + ν e^−U/kT) (dotted lines), which requires cooperative interactions that exist only in the complete fold](./plots/zwanzig.py)

The model makes two points. A modest bias, of the order of $k_{\mathrm{B}}T$ per residue, removes the paradox: once correct local structure is more stable than incorrect structure, the search is a downhill walk whose time grows only weakly with $N$. But independent residues do not produce a stable native state. With $U = 2\,k_{\mathrm{B}}T$ and $\nu = 2$, each residue is incorrect $21\,\%$ of the time, and the probability that all $100$ are correct at once is $0.79^{100} \approx 5\times10^{-11}$. The native state becomes populated only if it is stabilized by interactions that appear when the chain is complete, a free-energy bonus that grows with $N$: folding must be cooperative. Cooperativity in turn creates a barrier between partly folded and native chains, which is why small proteins fold in a two-state manner (16.2.4, 16.3).

### 16.2.3. Random Heteropolymers and Minimal Frustration

Why is the bias there? A random sequence of amino acids has a rugged energy surface: interactions that favour one contact conflict with interactions that favour another, and no conformation satisfies them all. Such conflict is called frustration. Bryngelson and Wolynes (1987) analysed its consequences with the random-energy model of spin-glass theory.

**Formula 16.2.1 (Random-Energy Model of a Heteropolymer)** Let the chain have $\Omega = \mathrm{e}^{S_0}$ non-native compact conformations whose energies are independent Gaussian random variables of mean $\bar E$ and standard deviation $\Delta E$ (the roughness). The microcanonical entropy of the non-native ensemble at energy $E$ is

$$
S(E) = S_0 - \frac{(E - \bar E)^2}{2\Delta E^2},
$$
and its free energy is

$$
F_{\mathrm{M}}(T) = \bar E - \frac{\Delta E^2}{2k_{\mathrm{B}}T} - TS_0 \quad (T > T_{\mathrm{g}}), \qquad
F_{\mathrm{M}} = E_{\min} = \bar E - \Delta E\sqrt{2S_0}\quad (T \le T_{\mathrm{g}}),
$$
with the glass temperature $k_{\mathrm{B}}T_{\mathrm{g}} = \Delta E/\sqrt{2S_0}$, at which the entropy of the occupied energy band vanishes. If the native conformation has energy $E_{\mathrm{N}} < E_{\min}$, it is stable below the folding temperature $T_{\mathrm{f}}$ defined by $F_{\mathrm{M}}(T_{\mathrm{f}}) = E_{\mathrm{N}}$.

**Proof** The thermodynamic temperature of the band is $1/T = \partial S/\partial E$, so the occupied energy is $E(T) = \bar E - \Delta E^2/k_{\mathrm{B}}T$ and $F = E - TS(E)$ gives the expression above. The occupied energy cannot fall below the lowest state $E_{\min}$, where $S = 0$; there the ensemble is frozen in a few deep minima, and $T_{\mathrm{g}}$ follows from $E(T_{\mathrm{g}}) = E_{\min}$. $\square$

Below $T_{\mathrm{g}}$ the non-native ensemble behaves as a glass: the chain is trapped in a few low-energy, unrelated conformations, and the time to escape from them is not reduced by lowering the temperature further. A chain that is to fold must therefore reach its native state at a temperature where the misfolded ensemble is still liquid.

**Definition 16.2.2 (Principle of Minimal Frustration)** The **principle of minimal frustration** (Bryngelson and Wolynes 1987) states that the sequences of natural proteins have been selected so that their native interactions are mutually consistent and much stronger than the random non-native ones: the native state lies far below the energy band of misfolded states (a large stability gap $E_{\min} - E_{\mathrm{N}}$ compared with the roughness $\Delta E$), so that $T_{\mathrm{f}} > T_{\mathrm{g}}$ and the energy landscape is funnelled.

![The random-energy model with S₀ = 40 (about 2 × 10¹⁷ misfolded states) and roughness ΔE = 10 (arbitrary energy units). A: the density of states is a Gaussian band, with a lowest misfolded state at E_min = −ΔE√(2S₀) = −89; a minimally frustrated sequence has its native state (E_N = −110) isolated below the band. B: the free energy of the misfolded ensemble falls with temperature until it freezes at T_g = 1.12; the native state becomes stable below T_f = 2.18, so the chain folds while the misfolded ensemble is still liquid, T_f/T_g = 1.95. C: T_f/T_g grows with the ratio of the stability gap to the roughness; without a gap, folding and glassy freezing coincide](./plots/rem-frustration.py)

The ratio $T_{\mathrm{f}}/T_{\mathrm{g}}$ is a measure of foldability: estimates for small proteins from simulations and from the temperature dependence of folding rates give values of about $1.5$–$2$. Minimal frustration also explains why the Gō model of folding, in which only native contacts attract, reproduces many experimental folding mechanisms: in a minimally frustrated protein non-native interactions are a perturbation. Frustration is not eliminated everywhere. Binding sites, hinges and allosteric switches are often locally frustrated, because a site that must change conformation on binding cannot be optimally packed in both states (Ferreiro, Wolynes and colleagues 2007): function is bought with local frustration within a globally funnelled landscape.

### 16.2.4. The Funnel and Its Projections

The funnel ([7.1.6](/7.1.6#def-6.3.2)) is a picture of the free energy of a chain as a function of its conformation, with the width representing the conformational entropy at each energy. To compute with it, one projects it on a few coordinates. The most common is the fraction $Q$ of native contacts formed, which runs from near $0$ for the unfolded ensemble to $1$ for the native structure. The free energy $F(Q) = -k_{\mathrm{B}}T\ln \int \delta(Q - Q(\boldsymbol{x}))\,\mathrm{e}^{-\beta H(\boldsymbol{x})}\,\mathrm{d}\boldsymbol{x}$ is the result of balancing the energy of the contacts against the entropy lost in forming them.

A mean-field version shows how a barrier arises. Let each of $N$ residues be native (energy $-\varepsilon$, no conformational freedom) or non-native (energy $0$, entropy $s_0$ per residue), and let a partially folded chain pay an interfacial cost $aQ(1 - Q)$ per residue for the boundary between folded and unfolded parts. With the entropy of choosing which residues are native,

$$
\frac{F(Q)}{N} = -\varepsilon Q - Ts_0(1 - Q) + aQ(1 - Q) + k_{\mathrm{B}}T\left[Q\ln Q + (1 - Q)\ln(1 - Q)\right].
$$
At the folding temperature $k_{\mathrm{B}}T_{\mathrm{f}} = \varepsilon/s_0$ the two minima, near $Q \approx 0.1$ and $Q \approx 0.9$, are equal, and the barrier between them grows in proportion to $N$. Lowering the temperature tilts the profile towards the native minimum and lowers the barrier; raising it does the opposite. The peak of $F(Q)$ is the transition-state ensemble, a set of partly structured conformations rather than a single structure.

![The folding funnel. A: a schematic rugged funnel: energy decreases towards the native state at the bottom while the conformational breadth (the radius) shrinks; random bumps and pits on the walls are local minima, kinetic traps that slow folding. B: projection on the fraction Q of native contacts in the mean-field model described in the text (N = 50, s₀ = ln 4 per residue, interfacial cost a = 3 k_BT per residue): at the folding temperature the unfolded and native minima have equal free energy and are separated by a barrier of 5.8 k_BT at Q ≈ 0.5, the transition-state ensemble; 6 % below T_f the native minimum is favoured and the barrier for folding is lower, 6 % above it the unfolded minimum is favoured](./plots/funnel.py)

Reduced coordinates are useful only if the dynamics along them is approximately diffusive and the other coordinates relax fast. When that holds, the kinetics follows from Kramers' theory ([7.6.5](/7.6.5#thm-5.6.2)) with $F(Q)$ as the potential: the folding rate is $k_{\mathrm{f}} = k_0\mathrm{e}^{-\Delta F^\ddagger/k_{\mathrm{B}}T}$ with a prefactor set by the curvatures of $F$ and by the diffusion coefficient along $Q$. Single-molecule experiments have measured both: Chung and Eaton (2012) resolved transition paths in single-molecule FRET ([7.6.12](/7.6.12)) lasting a few microseconds, and Woodside and colleagues reconstructed one-dimensional landscapes from optical-tweezers trajectories of folding nucleic-acid hairpins and proteins ([7.6.17](/7.6.17)).

## 16.3. Folding Kinetics and the Transition State

### 16.3.1. Two-State Kinetics and the Speed Limit

Many small single-domain proteins fold in a single exponential phase without detectable intermediates. Their kinetics is described by two rate constants, $k_{\mathrm{f}}$ and $k_{\mathrm{u}}$, with $K = k_{\mathrm{u}}/k_{\mathrm{f}}$ and relaxation rate $k_{\mathrm{obs}} = k_{\mathrm{f}} + k_{\mathrm{u}}$ after a perturbation. Both rates depend exponentially on denaturant, which gives the V-shaped chevron plot of $\ln k_{\mathrm{obs}}$ against denaturant ([7.1.6](/7.1.6#fml-6.3.1)); its two arms, with slopes $-m_{\mathrm{f}}/RT$ and $m_{\mathrm{u}}/RT$, must reproduce the equilibrium $m$ value and stability, the consistency test of the two-state model. The Tanford value $\beta_{\mathrm{T}} = m_{\mathrm{f}}/(m_{\mathrm{f}} + m_{\mathrm{u}})$ places the transition state on a scale of buried surface; for most small proteins it is $0.6$–$0.9$, a compact transition state.

The rate constants of real proteins span eight orders of magnitude, from $\sim 10^6\,\mathrm{s^{-1}}$ for the fastest designed and natural mini-proteins to $\sim 10^{-2}\,\mathrm{s^{-1}}$. The upper end is set not by the barrier but by the prefactor. In Kramers' theory the prefactor is a curvature divided by a friction, not the universal frequency $k_{\mathrm{B}}T/h$ of **transition state theory** ([7.6.5](/7.6.5#sec-5.6.2)); for folding it is estimated at $10^6$–$10^7\,\mathrm{s^{-1}}$ for small proteins, and folding rates fall roughly in inverse proportion to solvent viscosity when viscogens such as glycerol are added, which confirms the diffusive character of the barrier crossing.

**Formula 16.3.1 (Folding Speed Limit)** For a chain of $N$ residues, the fastest possible folding time, reached when the barrier vanishes (downhill folding), is approximately

$$
\tau_{\min} \approx \frac{N}{100}\,\mu\mathrm{s}
$$
(Kubelka, Hofrichter and Eaton 2004), from the time to form an α-helical turn or a β-hairpin ($\sim 0.1$–$1\,\mu\mathrm{s}$) and the diffusion of a chain segment over the size of the protein.

**Example 16.3.1** The $35$-residue villin headpiece subdomain, engineered to fold faster, folds in about $0.7\,\mu\mathrm{s}$, close to the estimated limit of $0.35\,\mu\mathrm{s}$; the $20$-residue Trp-cage folds in about $4\,\mu\mathrm{s}$. A $100$-residue protein folding in $10\,\mathrm{ms}$ is about $10^4$ times slower than its speed limit, which corresponds to a barrier of about $\ln 10^4 \approx 9\,k_{\mathrm{B}}T$, of the order of the barrier in the funnel model above. Proteins near the speed limit were the first whose folding could be simulated atom by atom and compared directly with experiment (Lindorff-Larsen, Shaw and colleagues 2011; [7.6.15](/7.6.15)).

### 16.3.2. Probing the Transition State: Phi-Value Analysis

The transition state is populated too briefly to be observed directly, but its structure can be inferred from how mutations change the rates. The method was introduced by Fersht and colleagues (Matouschek, Kellis, Serrano and Fersht 1989) and is a protein version of the **linear free-energy relationship** of physical organic chemistry.

**Definition 16.3.1 (Phi Value)** For a mutation that changes the Gibbs energy of unfolding by $\Delta\Delta G_{\mathrm{U}} = \Delta G_{\mathrm{U}}^{\mathrm{wt}} - \Delta G_{\mathrm{U}}^{\mathrm{mut}}$ and the activation Gibbs energy of folding by $\Delta\Delta G^{\ddagger} = RT\ln(k_{\mathrm{f}}^{\mathrm{wt}}/k_{\mathrm{f}}^{\mathrm{mut}})$, the **phi value** is

$$
\phi = \frac{\Delta\Delta G^{\ddagger}}{\Delta\Delta G_{\mathrm{U}}}.
$$
*Phi-value analysis* is the mapping of transition-state structure by the phi values of mutations, typically conservative truncations of side chains (Ile → Val, Leu → Ala), scattered over the protein.

If the mutated side chain makes its native interactions already in the transition state, the mutation destabilizes the transition state as much as the native state, folding slows by the full $\Delta\Delta G_{\mathrm{U}}$ and unfolding is unchanged: $\phi = 1$. If the residue is still unstructured in the transition state, folding is unaffected and only unfolding speeds up: $\phi = 0$. Intermediate values mean partial structure, or a mixture of transition-state structures in parallel pathways.

![Phi-value analysis (synthetic data). A: chevron plots of a wild-type two-state protein (k_f = 500 s⁻¹, k_u = 0.05 s⁻¹ in water, m_f = 7 and m_u = 3 kJ mol⁻¹ M⁻¹) and of three mutants that destabilize it by the same ΔΔG = 5 kJ mol⁻¹: for φ = 0 only the unfolding arm moves up, for φ = 1 only the folding arm moves down, for φ = 0.5 both move. B: Gibbs-energy diagrams (with the unfolded state as reference): a φ = 0 mutation raises only the native state, a φ = 1 mutation raises the transition state by the same amount. C: a Leffler plot for 14 hypothetical mutations in a protein whose transition state is uniformly, partially structured: the change of ln k_f against the change of ln K lies on a line through the wild type whose slope is the mean φ (0.34), between the limits φ = 0 and φ = 1 (dotted)](./plots/phi-value.py)

**Example 16.3.2 (Two Transition States)** For the barley chymotrypsin inhibitor 2 (CI2, $64$ residues), the most thoroughly mapped two-state folder, almost all phi values are fractional, about $0.2$–$0.6$, with the highest in the α-helix and in contacts between the helix and two β-strands. The transition state is an expanded version of the native state in which secondary and tertiary structure form together around a diffuse nucleus: the nucleation–condensation mechanism. In barnase ($110$ residues), by contrast, phi values are near $1$ in parts of the β-sheet and the first helix and near $0$ elsewhere, a polarized transition state in which some elements are essentially complete while others have not started.

Phi values are interpreted with care. A mutation must not change the structure of the native or the unfolded state, its $\Delta\Delta G_{\mathrm{U}}$ must be large enough (more than about $2.5\,\mathrm{kJ\,mol^{-1}}$) for the ratio to be measured precisely, and $\phi$ near $0$ or $1$ is unambiguous while fractional values can mean either partial structure or heterogeneous pathways. The analysis is the kinetic analogue of the **Hammond postulate** and of the **Brønsted catalysis law**: as the native state is destabilized, the transition state becomes more native-like, which appears as curvature (a Hammond shift) in the chevron arms of strongly destabilized proteins. In computation, phi values are calculated from transition-state ensembles of simulations and are the most direct test of simulated folding mechanisms.

### 16.3.3. Topology Sets the Rate: Contact Order

Plaxco, Simons and Baker (1998) found that the folding rates of small two-state proteins are predicted better by the topology of the native structure than by size or stability.

**Definition 16.3.2 (Contact Order)** For a native structure of $L$ residues with $N_{\mathrm{c}}$ contacts between non-adjacent residues (heavy atoms within $0.6\,\mathrm{nm}$), the **relative contact order** is the mean sequence separation of the contacting residues divided by the chain length,

$$
\mathrm{RCO} = \frac{1}{L N_{\mathrm{c}}}\sum_{\text{contacts }(i,j)}\lvert i - j\rvert .
$$

For their set of two-state proteins, $\ln k_{\mathrm{f}}$ fell linearly with RCO with a correlation coefficient of about $0.9$, over six orders of magnitude in rate: proteins whose contacts are mostly local (α-helical bundles, RCO $\approx 0.05$–$0.1$) fold fast, those with many long-range contacts (β-sheet proteins with strands far apart in sequence, RCO $\approx 0.15$–$0.25$) fold slowly. The interpretation is entropic: closing a loop of $\ell$ residues costs a conformational entropy of about $\frac32 k_{\mathrm{B}}\ln\ell$ for an ideal chain ([7.6.21](/7.6.21)), so a transition state that must bring residues far apart in sequence into contact has a higher barrier. The correlation implies that transition states resemble the native topology, which is the conclusion of phi-value analysis by a different route.

### 16.3.4. Intermediates and Parallel Pathways

Larger proteins (above about $100$ residues) usually fold through intermediates. A kinetic intermediate on the pathway (U ⇌ I → N) produces a lag in the appearance of N and a curvature (rollover) of the folding arm of the chevron at low denaturant, where the intermediate is stable enough to accumulate. A misfolded intermediate off the pathway must partly unfold before folding, and slows it. Many intermediates are compact and have much native secondary structure but fluid side chains, the **molten globule** state. Slow phases can also come from chemistry rather than from the landscape: cis–trans isomerization of X–Pro peptide bonds and the formation or reshuffling of disulfide bonds, which are catalysed in the cell by prolyl isomerases and protein disulfide isomerase ([7.1.6](/7.1.6#sec-6.4.3)).

Parallel pathways are a natural consequence of a funnel: the unfolded ensemble is heterogeneous, and different members can reach the native state by different routes. If the routes are separated by high barriers, the population is partitioned into fast and slow subpopulations whose relative amplitudes are fixed early and do not depend on the final conditions, a phenomenon developed for RNA in 16.7.4. Hen lysozyme is the classic protein example: about $25\,\%$ of the molecules fold in about $50\,\mathrm{ms}$, while $75\,\%$ form an intermediate with a folded α-domain and an unfolded β-domain that completes folding in about $0.4\,\mathrm{s}$.

### 16.3.5. Methods of Folding Kinetics

| Method | Principle | Time resolution | Measures |
|---|---|---|---|
| Stopped-flow mixing | Rapid dilution of denatured protein, fluorescence or CD readout | about $1\,\mathrm{ms}$ dead time | $k_{\mathrm{f}}$, $k_{\mathrm{u}}$, chevrons, burst phases |
| Continuous-flow mixing | Turbulent mixing, observation along a flow channel | $10$–$100\,\mu\mathrm{s}$ | early events, collapse |
| Temperature jump | Laser heating of water by $5$–$20\,\mathrm{K}$ in nanoseconds, relaxation to the new equilibrium | $10\,\mathrm{ns}$ | fast folders, helix and hairpin formation |
| Pressure jump | Release of high hydrostatic pressure | $\mu\mathrm{s}$–$\mathrm{ms}$ | volume changes of the transition state |
| Pulsed hydrogen exchange | Labeling of amides at variable times after initiating folding, read out by NMR or mass spectrometry ([7.6.13](/7.6.13#sec-13.6.5)) | $\mathrm{ms}$ | which structure forms first, residue by residue |
| NMR relaxation dispersion, CEST | Exchange broadening under native conditions ([7.6.13](/7.6.13#sec-13.6.4)) | $\mu\mathrm{s}$–$\mathrm{ms}$ processes at equilibrium | rates and structures of sparsely populated states (down to $\sim 1\,\%$) |
| Single-molecule FRET | Fluctuations of FRET efficiency of single molecules ([7.6.12](/7.6.12)) | $\mu\mathrm{s}$ with photon-by-photon analysis | heterogeneity, transition-path times, unfolded-state dimensions |
| Force spectroscopy | Unfolding and refolding under tension ([7.6.17](/7.6.17)) | $\mu\mathrm{s}$–$\mathrm{ms}$ | landscapes along the pulling coordinate, intermediates |

## 16.4. Lattice Models: Compactness, Hydrophobicity and Designability

### 16.4.1. Compact Random Walks and the Size of Proteins

A coarse but instructive picture treats a protein as a chain of residues on a lattice. Unfolded proteins are expanded random coils, while native globular proteins are compact random walks that fill space with no holes. The two pictures predict different relations between size and chain length, which are confirmed by small-angle scattering ([7.6.9](/7.6.9)).

**Formula 16.4.1 (Size Scaling of Polypeptide Chains)** The **radius of gyration** of a chain of $N$ residues scales as $R_{\mathrm{g}} = R_0N^{\nu}$, with

| State | Exponent $\nu$ | Empirical law |
|---|---|---|
| Native globular protein (compact) | $1/3$ | $R_{\mathrm{g}} \approx 2.2N^{0.38}\,\text{Å}$ (Skolnick and colleagues 1997) |
| Chemically denatured protein (good solvent, self-avoiding walk) | $\approx 0.59$ (Flory exponent $3/5$) | $R_{\mathrm{g}} \approx 1.93N^{0.60}\,\text{Å}$ (Kohn and colleagues 2004) |
| Ideal chain (θ solvent) | $1/2$ | — |
| Intrinsically disordered protein under native conditions | $0.45$–$0.6$, depending on sequence | $R_{\mathrm{g}} \approx 2.54N^{0.52}\,\text{Å}$ (Bernadó and Blackledge 2009) |

For a $100$-residue protein, the native $R_{\mathrm{g}}$ is about $13\,\text{Å}$ and the denatured $R_{\mathrm{g}}$ about $30\,\text{Å}$: unfolding more than doubles the linear size and increases the volume about tenfold. The exponent of a compact object is $1/3$ because its volume, which scales as $R^3$, is proportional to its mass; the exponent of a self-avoiding walk, $3/5$ in Flory's approximation, is derived in [7.6.21](/7.6.21).

### 16.4.2. The HP Model

The simplest lattice model with a sequence reduces the twenty amino acids to two classes, hydrophobic (H: Ala, Val, Ile, Leu, Met, Phe, Trp, Cys, Tyr in one common partition) and polar (P), on the view that hydrophobic collapse is the dominant driving force of folding (Dill 1985; Lau and Dill 1989).

**Definition 16.4.1 (HP Model)** In the **HP model** a protein is a self-avoiding walk on a lattice whose monomers are of two kinds, H and P. Each conformation has an energy from contacts between monomers that are lattice neighbours but not neighbours along the chain, favourable for H–H contacts (or, in the solvation version, an unfavourable cost $\varepsilon$ for each contact of an H with a P monomer or with solvent). The native structure of a sequence is its conformation of lowest energy.

Reducing the alphabet shrinks sequence space from $20^{100} \approx 10^{130}$ to $2^{100} \approx 10^{30}$ for a $100$-mer, and restricting structures to compact walks makes structure space enumerable for short chains: there are $103\,346$ compact walks of $27$ monomers on a $3\times3\times3$ cube (counted with the symmetry-related ones removed, about $5\times10^4$), against $2^{27} \approx 1.3\times10^8$ sequences. Some questions that are hopeless for real proteins can be answered exactly.

**Example 16.4.1 (The HP Six-Mer)** On a $2\times3$ lattice a six-mer has three compact structures unrelated by symmetry. With the solvation energy, the sequence HPHPHP has the same energy $7\varepsilon$ in all three and so has no native structure at any temperature. The sequence PHPPHP has energies $4\varepsilon$, $4\varepsilon$ and $2\varepsilon$: the U-shaped structure, in which the two H monomers touch, is its unique ground state, and the probability of being native is

$$
p_{\mathrm{fold}} = \frac{\mathrm{e}^{-2\beta\varepsilon}}{\mathrm{e}^{-2\beta\varepsilon} + 2\mathrm{e}^{-4\beta\varepsilon}},
$$
which falls sigmoidally from $1$ at low temperature towards $1/3$, a melting curve. Enumerating all $2^6 = 64$ sequences, $19$ have a unique ground state: $10$ fold into the U shape, $6$ and $3$ into the other two structures.

The idea that a binary pattern of hydrophobic and polar residues is the main determinant of a fold has been used in protein design. Hecht and colleagues designed libraries of four-helix bundles with the pattern PHPPHHP repeated, which places a hydrophobic residue every three or four positions in register with the $3.6$ residues per turn of an α-helix; the residues within each class were chosen at random, and a large fraction of the designed sequences formed helical bundles, some with enzymatic activity. The same binary patterning with alternating H and P gives β-strands and, at high concentration, amyloid-like fibrils.

### 16.4.3. Designability

Li, Helling, Tang and Wingreen (1996) asked which structures are most often chosen as unique ground states.

**Definition 16.4.2 (Designability)** The **designability** $N_{\mathrm{s}}$ of a structure is the number of sequences that have it as their unique ground state.

In the $3\times3\times3$ HP model with contact energies chosen to mimic the hydrophobic effect ($E_{\mathrm{HH}} = -2.3$, $E_{\mathrm{HP}} = -1$, $E_{\mathrm{PP}} = 0$, so that H–H contacts are favoured and H and P segregate), only about $5\,\%$ of the $2^{27}$ sequences have a unique ground state, and designability is extremely uneven: most compact structures are designed by few or no sequences, while a small number are designed by thousands. The highly designable structures are also those whose sequences have the largest energy gap between the ground state and the first excited structure, so they are thermodynamically stable and, in simulations, fast-folding; they are robust to mutation, since many neighbouring sequences design the same structure; and they show "protein-like" regularities, such as symmetric arrangements reminiscent of secondary-structure motifs. The same behaviour appears in a calculation small enough to be done exactly here.

![Lattice HP models solved by exact enumeration. A: the 2 × 3 six-mer: the three compact structures with the sequence PHPPHP (H yellow, P grey; the dot marks the first monomer) and their solvation energies, 4ε, 4ε and 2ε; the non-protein-like sequence HPHPHP has 7ε in all three. B: probability that PHPPHP is in its native structure against temperature. C: designability of the 38 compact structures of a 16-mer on a 4 × 4 lattice, from all 65 536 HP sequences with contact energies E_HH = −2.3, E_HP = −1, E_PP = 0: 48 % of the sequences have a unique ground state, and the number designing each structure ranges over two orders of magnitude, from 2483 to 23. D: the most and the least designable structures (non-bonded contacts dotted), each with its designing sequence of largest energy gap. E: the mean energy gap between ground state and next structure, for the sequences designing each structure, grows with designability (correlation with ln N_s 0.87): highly designable structures are the stable ones](./plots/hp-designability.py)

Designability connects the physics of folding to evolution: if structures with large $N_{\mathrm{s}}$ occupy large, connected regions of sequence space, random mutation and selection find them more easily and keep them longer. Natural proteins use only a few thousand distinct folds, many of them (the TIM barrel, the Rossmann fold, the four-helix bundle) adopted by unrelated sequences, consistent with the idea that a limited set of highly designable architectures dominates the protein universe ([7.6.41](/7.6.41)). The two-letter models also explain why the energy gap, not the absolute energy, controls foldability, the lattice version of the principle of minimal frustration.

## 16.5. Proteins That Do Not Fold

About a third of eukaryotic proteins contain long disordered regions (more than $30$ residues), and some are disordered throughout; in prokaryotes such regions are far rarer. These **intrinsically disordered proteins** ([7.2.21](/7.2.21)) have sequences low in hydrophobic residues and rich in charged and polar residues and in proline and glycine, often with low-complexity repeats. Their stable state is an ensemble.

An empirical rule of Uversky and colleagues (2000) separates folded from disordered sequences by two numbers, the mean net charge $\langle R\rangle$ and the mean hydropathy $\langle H\rangle$ (on a normalized Kyte–Doolittle scale): disordered sequences lie below the boundary $\langle H\rangle = (\langle R\rangle + 1.151)/2.785$. Physically, a high net charge expands the chain by electrostatic repulsion, and a low hydropathy removes the driving force for collapse. Within disordered sequences, the arrangement of charges also matters: at the same composition, sequences in which positive and negative residues are segregated into blocks are more compact than well-mixed ones, as quantified by the charge patterning parameter of Das and Pappu (2013), which interpolates between an expanded chain ($\nu \approx 0.6$) and a collapsed globule ($\nu \approx 1/3$).

Disordered regions are not structureless. They often contain short linear motifs that fold on binding, by **induced fit** or **conformational selection**, and the coupling of folding and binding allows high specificity with modest affinity, because part of the binding free energy is spent on folding; it also allows fast association, because an extended chain has a large capture radius (the "fly-casting" mechanism). Multivalent disordered regions drive the liquid–liquid phase separation of condensates, whose physics is the subject of [7.6.29](/7.6.29). Experimentally, the ensembles are characterized by NMR chemical shifts and paramagnetic relaxation ([7.6.13](/7.6.13)), SAXS ([7.6.9](/7.6.9)) and single-molecule FRET ([7.6.12](/7.6.12)), combined with ensemble modelling.

## 16.6. Folding in the Cell

### 16.6.1. Cotranslational Folding

In the cell a chain begins to fold before it is complete. The ribosome adds about $20$ amino acids per second in *Escherichia coli* and $4$–$6$ in eukaryotes, so a $300$-residue protein emerges over $15$–$75\,\mathrm{s}$, while small domains fold in milliseconds. The ribosomal exit tunnel, about $10\,\mathrm{nm}$ long and $1$–$2\,\mathrm{nm}$ wide, holds $30$–$40$ residues in an extended or α-helical conformation and allows only small tertiary structures to form within its vestibule; its negatively charged walls interact with the nascent chain and can slow translation at clusters of positive residues. Folding domain by domain as they emerge reduces the risk that domains of a large protein interact non-natively. About a third of *E. coli* proteins are estimated to fold, at least partly, cotranslationally, and translation rates are tuned by synonymous codons: replacing slowly translated codons by fast ones can change the folding yield of some multidomain proteins.

### 16.6.2. Chaperones as Energy-Driven Machines

The mechanisms of the main chaperone systems, Hsp70 with its Hsp40 cofactors and nucleotide-exchange factors, the chaperonin GroEL–GroES and its eukaryotic homologue TRiC, Hsp90, and the disaggregase Hsp100, are described in [7.1.6](/7.1.6#sec-6.4). In *E. coli*, about $70\,\%$ of nascent chains fold with the help of the ribosome-associated trigger factor alone, while the rest require Hsp70 (DnaK–DnaJ–GrpE) and about $10$–$15\,\%$ GroEL–GroES. Physically, these machines act on the landscape in three ways:

- Holding: binding exposed hydrophobic segments of non-native chains prevents their association with other chains (16.6.3), at the cost of no energy beyond the binding itself.
- Unfolding: an ATP-driven cycle that binds a misfolded chain tightly and releases it partly unfolded returns it to the top of the funnel, from where it has a new chance to fold correctly (kinetic partitioning is restarted); this "iterative annealing" can raise the steady-state fraction of native protein above its equilibrium value, because the cycle is driven by ATP hydrolysis and is not bound by detailed balance ([7.6.38](/7.6.38)).
- Confining: folding inside the GroEL cavity for the $\sim 10\,\mathrm{s}$ of one cycle isolates the chain from aggregation partners and, by confinement, lowers the entropy of the unfolded state, which can accelerate folding of some substrates.

### 16.6.3. Folding Against Aggregation

Folding is first order in the concentration of unfolded chains, aggregation second order or higher. Their competition decides the yield of refolding experiments and the burden of misfolding in cells.

**Formula 16.6.1 (Kinetic Competition)** If unfolded chains $U$ fold with rate constant $k_{\mathrm{f}}$ and aggregate irreversibly with second-order rate constant $k_{\mathrm{a}}$, $\mathrm{d}U/\mathrm{d}t = -k_{\mathrm{f}}U - k_{\mathrm{a}}U^2$, the fraction folded starting from $U(0) = c_0$ is

$$
Y = \frac{k_{\mathrm{f}}}{k_{\mathrm{a}}c_0}\ln\left(1 + \frac{k_{\mathrm{a}}c_0}{k_{\mathrm{f}}}\right).
$$

**Proof** The folded amount is $\int_0^\infty k_{\mathrm{f}}U\,\mathrm{d}t$. Changing variable to $U$, $\mathrm{d}t = -\mathrm{d}U/(k_{\mathrm{f}}U + k_{\mathrm{a}}U^2)$, so $\int_0^{c_0}k_{\mathrm{f}}\,\mathrm{d}U/(k_{\mathrm{f}} + k_{\mathrm{a}}U) = (k_{\mathrm{f}}/k_{\mathrm{a}})\ln(1 + k_{\mathrm{a}}c_0/k_{\mathrm{f}})$; dividing by $c_0$ gives $Y$. $\square$

The yield depends only on the dimensionless ratio $k_{\mathrm{a}}c_0/k_{\mathrm{f}}$: it is close to $1$ when the aggregation rate per molecule at the starting concentration is small compared with the folding rate, and falls as $\ln(x)/x$ beyond. This is why refolding in the laboratory is done at low protein concentration or by slow dilution, and why slowly folding proteins at high cellular concentrations depend on holdases that reduce the effective $k_{\mathrm{a}}$.

### 16.6.4. The Kinetics of Amyloid Formation

When aggregation produces ordered cross-β fibrils (**amyloid fibrils**, [7.1.6](/7.1.6#sec-6.5)), the kinetics takes a characteristic sigmoidal form: a lag phase, rapid growth and a plateau. It is described by nucleated polymerization, with a rate-limiting formation of nuclei and fast growth of existing fibrils, and, as Knowles, Dobson and colleagues showed, by secondary nucleation, the formation of new nuclei on the surface of existing fibrils, which makes the reaction autocatalytic.

**Formula 16.6.2 (Moment Equations of Fibril Formation)** Let $P(t)$ be the number concentration of fibrils, $M(t)$ the mass concentration of monomer in fibrils and $m = m_{\mathrm{tot}} - M$ the free monomer. With primary nucleation of order $n_{\mathrm{c}}$ (rate constant $k_{\mathrm{n}}$), elongation at both ends ($k_+$) and secondary nucleation of order $n_2$ ($k_2$),

$$
\frac{\mathrm{d}P}{\mathrm{d}t} = k_{\mathrm{n}}m^{n_{\mathrm{c}}} + k_2m^{n_2}M, \qquad \frac{\mathrm{d}M}{\mathrm{d}t} = 2k_+mP.
$$
For early times the fibril mass grows as $\cosh(\kappa t) - 1$ with $\kappa = \sqrt{2k_+k_2m_{\mathrm{tot}}^{n_2 + 1}}$, and the half time scales with the total monomer concentration as $t_{1/2} \propto m_{\mathrm{tot}}^{\gamma}$ with $\gamma \approx -(n_2 + 1)/2$ when secondary nucleation dominates and $\gamma = -n_{\mathrm{c}}/2$ when it is absent.

![Folding against aggregation and the kinetics of amyloid. A: native yield after dilution of an unfolded protein that folds with k_f = 1 s⁻¹ and aggregates with second-order rate constants of 10⁵, 10⁶ and 10⁷ M⁻¹ s⁻¹ (Formula 16.6.1): the yield falls once k_a c₀ exceeds k_f. B: fibril formation at 5 µM total monomer computed from Formula 16.6.2 with rate constants of the order measured for the amyloid-β 42 peptide (k₊ = 3 × 10⁶ M⁻¹ s⁻¹, k_n = 10⁻⁷ M⁻¹ s⁻¹, k₂ = 1.3 × 10⁴ M⁻² s⁻¹, n_c = n₂ = 2; logarithmic time axis): with secondary nucleation the half time is about 1.3 h after a lag phase; with primary nucleation alone it would be about 90 h; preformed seeds (1 % of the mass) abolish the lag. C: half time against total monomer concentration: the slopes, −1.4 (approaching −1.5) with secondary nucleation and −1.0 without, identify the dominant nucleation mechanism in global fits of experimental data](./plots/aggregation.py)

**Example 16.6.1 (Amyloid-β 42)** Cohen and colleagues (2013) fitted aggregation curves of the Alzheimer amyloid-β 42 peptide over a range of concentrations with Formula 16.6.2 and found $k_+k_{\mathrm{n}} \approx 3\times10^{-1}\,\mathrm{M^{-2}\,s^{-2}}$ and $k_+k_2 \approx 4\times10^{10}\,\mathrm{M^{-3}\,s^{-2}}$, with $\gamma \approx -1.3$. Once a small amount of fibril is present, more than $99\,\%$ of new nuclei are produced by secondary nucleation, and these small, newly formed oligomers are the most toxic species to neurons in culture. The analysis turned a qualitative distinction (nucleation versus growth) into a basis for drug design: molecular chaperones and small molecules that bind fibril surfaces suppress secondary nucleation specifically, reducing the flux of oligomers without necessarily slowing fibril growth.

The same kinetics, with a lag that is abolished by seeding, underlies the propagation of **prions** ([7.1.6](/7.1.6#def-6.5.2)) and the cell-to-cell spread of α-synuclein and tau aggregates. The structures of amyloid fibrils, insoluble and heterogeneous, are determined by solid-state NMR and cryo-electron microscopy of helical filaments ([7.6.14](/7.6.14)), which revealed that one peptide can form several distinct fibril polymorphs and that patients with different diseases carry different polymorphs of the same protein.

## 16.7. RNA Folding

### 16.7.1. How RNA Folding Differs from Protein Folding

RNA folds into specific three-dimensional structures, catalyses reactions in ribozymes and the ribosome, and switches conformation in riboswitches, but its folding follows different rules.

| Property | Protein | RNA |
|---|---|---|
| Alphabet | 20 residues of diverse size, charge and polarity | 4 nucleotides of two similar shapes (purines, pyrimidines), each with one negative charge |
| Secondary structure | Helices and sheets stable only within the tertiary context (an isolated α-helix of 15 residues lives microseconds) | Helices are stable on their own (a 6-bp RNA duplex persists for days) |
| Driving force | Hydrophobic burial | Base pairing and stacking; electrostatic repulsion must be screened by counterions |
| Hierarchy | Secondary and tertiary structure form together | Secondary structure forms first, tertiary structure later (hierarchical folding) |
| Landscape | Funnelled, mostly smooth for small domains | Rugged: many alternative secondary structures of similar stability separated by high barriers |
| Typical kinetics | Two-state or few intermediates, μs–s | Multiple phases, long-lived misfolded states, ms–hours |

Because secondary structure dominates the free energy, RNA folding is often described in two steps: secondary structure under monovalent salt, and tertiary structure assembled from the preformed helices when $\ce{Mg^2+}$ is added. This hierarchy is a first approximation: tertiary contacts can remodel secondary structure, as in the P5abc subdomain of the *Tetrahymena* group I intron, where binding of $\ce{Mg^2+}$ and formation of the tertiary core shift a stem by one register and convert two base pairs into non-canonical pairs, and as in riboswitches, where ligand binding to the aptamer rearranges the downstream secondary structure that controls expression (16.7.5).

### 16.7.2. Thermodynamics of Secondary Structure

Because base pairing and stacking are local, the free energy of a secondary structure is, to a good approximation, a sum of contributions of its elements.

**Definition 16.7.1 (Nearest-Neighbour Model)** In the *nearest-neighbour model* of nucleic-acid thermodynamics (Tinoco, Uhlenbeck and colleagues 1973; Turner and colleagues; SantaLucia for DNA), the standard Gibbs energy of a secondary structure is the sum of a stacking free energy for each pair of adjacent base pairs in a helix, which depends on the identity of both pairs, and of loop free energies for each hairpin, bulge, internal and multibranch loop, which depend on loop size and on the closing pairs and first mismatches:

$$
\Delta G^\circ = \sum_{\text{stacks}}\Delta G^\circ_{\mathrm{stack}}(i, i+1) + \sum_{\text{loops}}\Delta G^\circ_{\mathrm{loop}} + \Delta G^\circ_{\mathrm{init}} .
$$
Each term has an enthalpy and an entropy measured from optical melting of model oligonucleotides, in $1\,\mathrm{M}$ NaCl.

For RNA at $37\,^\circ\mathrm{C}$, Watson–Crick stacks contribute from about $-0.9\,\mathrm{kcal\,mol^{-1}}$ (5′-AA-3′/3′-UU-5′) to $-3.4\,\mathrm{kcal\,mol^{-1}}$ (5′-GC-3′/3′-CG-5′), with enthalpies of $-7$ to $-14\,\mathrm{kcal\,mol^{-1}}$; the order follows the stacking strength of G·C pairs, not merely their three hydrogen bonds. Loops cost free energy because they restrict the chain: a hairpin loop of four nucleotides costs about $+4.5$ to $+5.6\,\mathrm{kcal\,mol^{-1}}$ before sequence-specific bonuses. A single base pair cannot pay for the loop it closes, so a hairpin is stable only when several consecutive stacks form beneath the loop, and hairpin formation is nucleated at the loop and zips down the stem.

**Example 16.7.1 (A Tetraloop Hairpin)** The hairpin 5′-GGAC(UUCG)GUCC-3′ has a four-pair stem with three stacks, GG/CC ($-3.26$), GA/CU ($-2.35$) and AC/UG ($-2.24\,\mathrm{kcal\,mol^{-1}}$), and a UUCG loop that, including its favourable terminal mismatch and the bonus of this unusually stable tetraloop, costs about $+4.5\,\mathrm{kcal\,mol^{-1}}$. Then $\Delta G^\circ_{37} \approx -3.4\,\mathrm{kcal\,mol^{-1}}$ ($-14\,\mathrm{kJ\,mol^{-1}}$), $K = \mathrm{e}^{3.4/0.616} \approx 250$, and with $\Delta H^\circ \approx -37\,\mathrm{kcal\,mol^{-1}}$ from the stacks the hairpin melts, as a unimolecular two-state transition, at $T_{\mathrm{m}} = \Delta H^\circ/\Delta S^\circ \approx 68\,^\circ\mathrm{C}$ in $1\,\mathrm{M}$ NaCl.

The nearest-neighbour model is the basis of secondary-structure prediction: since the free energy is additive over nested elements, the minimum-free-energy structure and the full **partition function** over all secondary structures are computed by dynamic programming in $O(N^3)$ time (Zuker's algorithm, McCaskill's algorithm; the algorithms belong to [7.8](/7.8)). Predicted structures of single sequences are about $70\,\%$ correct for RNAs of a few hundred nucleotides; accuracy improves with comparative sequence analysis and chemical probing data (16.7.5).

### 16.7.3. Counterions and Magnesium

Folding an RNA brings its phosphates together, and the electrostatic repulsion between them must be screened. Monovalent ions screen nonspecifically and stabilize secondary structure: the melting temperature of a hairpin increases linearly with $\ln[\ce{Na+}]$. Thermodynamically, if unfolding releases $\Delta n$ counterions, the equilibrium constant depends on salt activity as $\partial\ln K_{\mathrm{fold}}/\partial\ln a_{\ce{Na+}} = \Delta n$, and with the van 't Hoff equation

$$
\frac{\mathrm{d}T_{\mathrm{m}}}{\mathrm{d}\ln[\ce{Na+}]} = \frac{RT_{\mathrm{m}}^2}{\Delta H_{\mathrm{U}}}\,\Delta n ,
$$
with $\Delta H_{\mathrm{U}} > 0$ the enthalpy of unfolding. The released counterions are those condensed on the compact folded structure, whose charge density is higher; the theory of **counterion condensation** and of the Poisson–Boltzmann atmosphere around nucleic acids is in [7.6.6](/7.6.6#sec-6.4.3).

![Thermodynamics of an RNA hairpin in the nearest-neighbour model (5′-GGAC(UUCG)GUCC-3′, Turner-type parameters at 37 °C, loop given a single approximate cost). A: the free-energy budget: three stacks contribute −7.85 kcal mol⁻¹ and the loop costs about +4.5, leaving ΔG°₃₇ ≈ −3.35 kcal mol⁻¹ for the hairpin. B: two-state melting curves at 10, 100 and 1000 mM Na⁺: the melting temperature rises from 51 to 68 °C. C: T_m is linear in ln[Na⁺], here 8 °C per tenfold increase, computed from the counterion-release relation with Δn = 0.6 ions released on unfolding](./plots/rna-hairpin.py)

Tertiary structure requires more than screening. Divalent $\ce{Mg^2+}$ stabilizes compact folds far more effectively than $\ce{Na+}$ or $\ce{K+}$, partly because the ionic atmosphere of a divalent ion pays half the entropic cost per charge, and partly through specific binding. RNA binds metal ions in two modes: diffuse binding, in which fully hydrated ions accumulate in the electrostatic potential of the RNA and remain mobile, and site binding, in which a partly dehydrated $\ce{Mg^2+}$ binds in a pocket where phosphates or base atoms converge, either through its hydration shell (outer-sphere) or by direct coordination (inner-sphere). Inner-sphere sites are typical of catalytic centres of ribozymes; outer-sphere sites, such as tandem G·U pairs that bind $\ce{Mg(H2O)6^2+}$, often lie near tertiary contacts. Monovalent ions can also be specific: guanine quadruplexes are stabilized by $\ce{K+}$ coordinated between stacked G-quartets, much less by $\ce{Na+}$ and hardly by $\ce{Li+}$, and $\ce{K+}$ is required for the active site of group II introns. Cellular conditions differ from those of most in vitro studies: about $140\,\mathrm{mM}$ $\ce{K+}$, $0.5$–$1\,\mathrm{mM}$ free $\ce{Mg^2+}$ in eukaryotes ($1.5$–$3\,\mathrm{mM}$ in bacteria) but about $20\,\mathrm{mM}$ total $\ce{Mg^2+}$, and $20$–$40\,\%$ of the volume occupied by macromolecules ([7.6.23](/7.6.23)).

### 16.7.4. Kinetic Traps and Kinetic Partitioning

The rugged landscape of RNA makes misfolding common. Once a wrong helix of several base pairs has formed, correcting it requires melting the helix, a barrier of many kilocalories per mole, so misfolded states can persist for minutes to hours although the native state is the global minimum.

**Definition 16.7.2 (Kinetic Partitioning)** **Kinetic partitioning** (Thirumalai and colleagues) is the division of a folding population, early in folding, into a fraction $\Phi$ that reaches the native state directly and fast, and a fraction $1 - \Phi$ that is trapped in misfolded states and reaches the native state only slowly, by partial unfolding. The partition factor $\Phi$ is set by the relative rates of the competing early steps, $\Phi = k_{\mathrm{N}}/(k_{\mathrm{N}} + k_{\mathrm{M}})$, and not by the stabilities of the final states.

For the scheme $\mathrm{U} \to \mathrm{N}$ (rate $k_{\mathrm{N}}$), $\mathrm{U} \to \mathrm{M}$ ($k_{\mathrm{M}}$), $\mathrm{M} \to \mathrm{N}$ ($k_{\mathrm{MN}} \ll k_{\mathrm{N}} + k_{\mathrm{M}}$), the native fraction rises in two phases, $f_{\mathrm{N}}(t) \approx \Phi[1 - \mathrm{e}^{-(k_{\mathrm{N}} + k_{\mathrm{M}})t}] + (1 - \Phi)(1 - \mathrm{e}^{-k_{\mathrm{MN}}t})$, whose amplitudes measure $\Phi$ directly.

**Example 16.7.2 (The *Tetrahymena* Group I Intron)** In vitro, less than $10\,\%$ of molecules of the *Tetrahymena* ribozyme fold directly to the active structure at about $1\,\mathrm{s^{-1}}$; more than $90\,\%$ are trapped within seconds in a long-lived misfolded state, in which most native contacts, including the peripheral ones, are formed but a helix of the core (the alt-P3 pairing) is wrong. Escape from it requires unfolding of much of the structure and takes minutes to hours. The independently folding P4–P6 domain folds hierarchically: the P5abc subdomain binds two $\ce{Mg^2+}$ and folds first, then the metal-core/metal-core-receptor contact forms, and finally the tetraloop/tetraloop-receptor contact docks the two helical stacks. Slow cooling after heat denaturation, which gives molecules time to escape traps at intermediate temperatures, increases the fraction folded correctly, the experimental analogue of annealing.

![Kinetic partitioning in RNA folding. A: scheme: unfolded RNA folds directly to the native state N (k_N = 1 s⁻¹) or into a long-lived misfolded state M (k_M = 9 s⁻¹), so the partition factor is 10 %, as for the *Tetrahymena* group I ribozyme; M reaches N only by partly unfolding (k_MN). B: fraction native against time (logarithmic axis): a fast phase of 10 % amplitude and a slow phase of 90 % with time constant 1/k_MN ≈ 8 min (k_MN = 2 × 10⁻³ s⁻¹); a DEAD-box RNA chaperone that accelerates the escape from M 30-fold shortens the slow phase but does not change the fast one. C: kinetic control of a riboswitch that binds its ligand with k_on = 10⁷ M⁻¹ s⁻¹ and K_D = 10 nM: if the decision must be made within a window 1/k_t before the polymerase passes the terminator, the fraction switched is k_on L/(k_on L + k_t); the ligand concentration for half switching, T50, then exceeds K_D tenfold for a 1 s window and a hundredfold for 0.1 s (dashed: equilibrium binding)](./plots/rna-partitioning.py)

### 16.7.5. Folding in the Cell: Cotranscription, Chaperones and Riboswitches

In cells, RNA folds as it is transcribed. RNA polymerase adds $20$–$80$ nucleotides per second in bacteria, while short helices form in microseconds, so the $5′$ part of a transcript folds into structures that are optimal for the partial chain before the rest exists. The landscape changes as the chain grows: a barrier that is insurmountable for the full-length RNA may never be encountered, or a structure favoured early may become a trap later. The hepatitis delta virus ribozyme is more active when folded cotranscriptionally than after renaturation of the full-length chain, and transcriptional pausing at specific sites gives time for particular structures to form.

Riboswitches exploit these kinetics. An aptamer in the $5′$ untranslated region binds a metabolite and, through an expression platform, controls transcription termination or translation initiation; in the adenine riboswitch, ligand binding stabilizes the aptamer and releases a sequence that otherwise sequesters the Shine–Dalgarno sequence ([7.2.18](/7.2.18)). Many transcriptional riboswitches are under kinetic control: the aptamer must bind its ligand within the few seconds before the polymerase reaches the terminator, so the concentration needed to switch is set by $k_{\mathrm{on}}$ and the speed of transcription rather than by $K_{\mathrm{D}}$. For the FMN riboswitch, Wickiser, Breaker and Crothers (2005) found that the switching concentration exceeded the equilibrium dissociation constant about tenfold and depended on polymerase pausing, as in panel C of the figure above.

RNA chaperones resolve misfolded structures. ATP-independent ones, such as the bacterial StpA protein and many ribosomal proteins, are positively charged and destabilize helices nonspecifically through electrostatic interactions, lowering the barriers between alternative secondary structures. ATP-dependent ones are DEAD-box helicases (helicase superfamily 2), which unwind short helices locally in an ATP-driven cycle; CYT-19 of *Neurospora* accelerates the escape of the group I intron from its misfolded state and, because it acts preferentially on less stable structures, leaves the native fold intact. Chemical probing in vivo (dimethyl sulfate, which methylates unpaired A and C, and SHAPE reagents, which acylate the 2′-hydroxyl of flexible nucleotides, read out by sequencing) shows that many mRNAs are less structured in cells than in vitro, because helicases, ribosomes and RNA-binding proteins continually unfold them.

## Summary

| Topic | Key relation or result |
|---|---|
| Stability (16.1) | $\Delta G_{\mathrm{U}} = 20$–$60\,\mathrm{kJ\,mol^{-1}}$, a small difference of large terms; $K = (y_{\mathrm{N}} - y)/(y - y_{\mathrm{U}})$; $m \propto \Delta\mathrm{ASA}$ (Example 16.1.1); kinetic stability $1/k_{\mathrm{u}}$ |
| Zwanzig model (Definition 16.2.1) | birth–death chain; $\tau = \sum_j\sum_{i\ge j}\pi_i/(d_j\pi_j)$ (Theorem 16.2.1); a bias of $\sim k_{\mathrm{B}}T$ per residue removes Levinthal's paradox, but stability needs cooperativity |
| Random-energy model (Formula 16.2.1) | $k_{\mathrm{B}}T_{\mathrm{g}} = \Delta E/\sqrt{2S_0}$; folding requires $T_{\mathrm{f}} > T_{\mathrm{g}}$: minimal frustration (Definition 16.2.2), a large gap over roughness |
| Free-energy profiles | $F(Q)$ with unfolded and native minima and a transition-state ensemble; Kramers rate with prefactor $10^6$–$10^7\,\mathrm{s^{-1}}$ |
| Kinetics (16.3) | chevrons, $\beta_{\mathrm{T}} = m_{\mathrm{f}}/m$; speed limit $N/100\,\mu\mathrm{s}$ (Formula 16.3.1); contact order (Definition 16.3.2) |
| Transition states | $\phi = \Delta\Delta G^\ddagger/\Delta\Delta G_{\mathrm{U}}$ (Definition 16.3.1): $1$ native-like, $0$ unstructured; nucleation–condensation (Example 16.3.2) |
| Lattice models (16.4) | $R_{\mathrm{g}} \propto N^{1/3}$ folded, $N^{0.59}$ denatured (Formula 16.4.1); HP model (Definition 16.4.1); designability correlates with energy gap (Definition 16.4.2) |
| Disordered proteins (16.5) | net charge and hydropathy; charge patterning; coupled folding and binding |
| Cell (16.6) | cotranslational folding; chaperones hold, unfold and confine; yield $Y = \ln(1 + x)/x$, $x = k_{\mathrm{a}}c_0/k_{\mathrm{f}}$ (Formula 16.6.1); amyloid with secondary nucleation, $t_{1/2} \propto m_{\mathrm{tot}}^{-(n_2+1)/2}$ (Formula 16.6.2) |
| RNA (16.7) | hierarchical folding; nearest-neighbour model (Definition 16.7.1); $\mathrm{d}T_{\mathrm{m}}/\mathrm{d}\ln[\ce{Na+}] = RT_{\mathrm{m}}^2\Delta n/\Delta H_{\mathrm{U}}$; $\ce{Mg^2+}$ diffuse and site binding; kinetic partitioning (Definition 16.7.2); kinetic control of riboswitches |

## Questions

1. Why does a protein with hundreds of stabilizing contacts have a stability of only $8$–$25\,k_{\mathrm{B}}T$? Give two reasons why natural selection does not make proteins much more stable.

   **Answer** The free energy of folding is the small difference between the favourable energy and hydrophobic free energy of the contacts and the large loss of conformational entropy (several hundred $\mathrm{kJ\,mol^{-1}}$ at room temperature for $100$ residues); most intramolecular contacts also replace similar contacts with water, so their net contribution is small. Selection does not maximize stability because (i) most mutations are destabilizing, so under selection only for "folded enough" proteins drift to the stability threshold (mutation–selection balance), and (ii) function requires conformational flexibility, which a very stable fold would suppress.

2. In the Zwanzig model with $\nu = 2$ and $U = 2\,k_{\mathrm{B}}T$, what fraction of a $100$-residue chain's residues are incorrect at equilibrium, and what is the probability that the chain is fully native? What does this imply?

   **Answer** Per residue the ratio incorrect : correct is $\nu\mathrm{e}^{-2} = 0.271$, so the incorrect fraction is $0.271/1.271 = 0.21$ and $P(\text{all correct}) = (1/1.271)^{100} = 4\times10^{-11}$. Although the bias makes folding fast, the native state is essentially unpopulated: a stable native state requires an additional free-energy bonus for the complete structure, of about $100\ln 1.271 = 24\,k_{\mathrm{B}}T$, that is, cooperative interactions present only in the full fold.

3. In the random-energy model with $S_0 = 40$ and $\Delta E = 10$, compute $T_{\mathrm{g}}$ and the folding temperature for a native energy $E_{\mathrm{N}} = -110$ (units $k_{\mathrm{B}} = 1$). How much lower must $E_{\mathrm{N}}$ be for $T_{\mathrm{f}}/T_{\mathrm{g}} = 2.5$?

   **Answer** $T_{\mathrm{g}} = 10/\sqrt{80} = 1.118$. $T_{\mathrm{f}}$ solves $-50/T - 40T = -110$, i.e. $40T^2 - 110T + 50 = 0$, whose larger root is $T_{\mathrm{f}} = (110 + 64.0)/80 = 2.18$, a ratio of $1.95$. For $T_{\mathrm{f}} = 2.5\times1.118 = 2.795$ we need $E_{\mathrm{N}} = F_{\mathrm{M}}(2.795) = -50/2.795 - 40\times2.795 = -129.7$, about $20$ units lower. The stability gap below the lowest misfolded state ($E_{\min} = -89.4$) then grows from $2.1\Delta E$ to $4.0\Delta E$.

4. A mutation destabilizes a protein by $6.0\,\mathrm{kJ\,mol^{-1}}$ and lowers $k_{\mathrm{f}}$ from $400$ to $80\,\mathrm{s^{-1}}$ at $25\,^\circ\mathrm{C}$. What is its phi value, and how does $k_{\mathrm{u}}$ change? What would you conclude about the residue?

   **Answer** $\Delta\Delta G^\ddagger = RT\ln(400/80) = 2.479\times1.609 = 3.99\,\mathrm{kJ\,mol^{-1}}$, so $\phi = 3.99/6.0 = 0.67$. The remaining $2.0\,\mathrm{kJ\,mol^{-1}}$ raises $k_{\mathrm{u}}$ by $\mathrm{e}^{2.0/2.479} = 2.2$-fold. The side chain makes a large part of its native interactions in the transition state; it belongs to, or is close to, the folding nucleus.

5. Estimate the speed-limit folding time of a $60$-residue protein. If it folds in $5\,\mathrm{ms}$, estimate its folding barrier assuming the speed limit is the Kramers prefactor.

   **Answer** $\tau_{\min} \approx 60/100\,\mu\mathrm{s} = 0.6\,\mu\mathrm{s}$. Then $\mathrm{e}^{\Delta F^\ddagger/k_{\mathrm{B}}T} = 5\times10^{-3}/6\times10^{-7} \approx 8\times10^3$, so $\Delta F^\ddagger \approx 9\,k_{\mathrm{B}}T$ ($22\,\mathrm{kJ\,mol^{-1}}$ at $25\,^\circ\mathrm{C}$).

6. Explain with the HP six-mer why HPHPHP is "not protein-like". Compute the probability that PHPPHP is native at $k_{\mathrm{B}}T = \varepsilon$.

   **Answer** HPHPHP has the same energy ($7\varepsilon$) in all three compact structures, so all are equally populated at every temperature: there is no unique native structure. For PHPPHP, $p = \mathrm{e}^{-2}/(\mathrm{e}^{-2} + 2\mathrm{e}^{-4}) = 1/(1 + 2\mathrm{e}^{-2}) = 1/1.271 = 0.79$.

7. A protein that folds with $k_{\mathrm{f}} = 0.5\,\mathrm{s^{-1}}$ aggregates with $k_{\mathrm{a}} = 10^5\,\mathrm{M^{-1}\,s^{-1}}$. What is the refolding yield after dilution to $50\,\mu\mathrm{M}$, and to what concentration must you dilute for a $90\,\%$ yield?

   **Answer** $x = k_{\mathrm{a}}c_0/k_{\mathrm{f}} = 10^5\times5\times10^{-5}/0.5 = 10$, $Y = \ln 11/10 = 0.24$. For $Y = 0.9$, solve $\ln(1+x)/x = 0.9$: $x \approx 0.22$, so $c_0 = 0.22\times0.5/10^5 \approx 1.1\,\mu\mathrm{M}$.

8. Aggregation half times of a peptide are $10\,\mathrm{h}$ at $2\,\mu\mathrm{M}$ and $1.8\,\mathrm{h}$ at $6\,\mu\mathrm{M}$. What is the scaling exponent, and what does it suggest about the mechanism? Design an experiment to confirm it.

   **Answer** $\gamma = \ln(1.8/10)/\ln 3 = -1.56$, consistent with $-(n_2 + 1)/2$ for secondary nucleation with $n_2 \approx 2$, and not with primary nucleation alone ($-n_{\mathrm{c}}/2 = -1$ for $n_{\mathrm{c}} = 2$). Confirmation: add small amounts of preformed fibrils (a few percent); if secondary nucleation dominates, even small seed concentrations abolish the lag and the early growth is exponential rather than polynomial, and very high seed concentrations (where elongation of seeds dominates) give linear initial growth; global fitting of curves at several concentrations and seed levels to Formula 16.6.2 discriminates the models.

9. A hairpin has $\Delta H_{\mathrm{U}} = 150\,\mathrm{kJ\,mol^{-1}}$ and $T_{\mathrm{m}} = 330\,\mathrm{K}$ in $100\,\mathrm{mM}$ NaCl, and its $T_{\mathrm{m}}$ increases by $6\,\mathrm{K}$ for a tenfold increase in salt. How many counterions are released on unfolding?

   **Answer** $\mathrm{d}T_{\mathrm{m}}/\mathrm{d}\ln[\ce{Na+}] = 6/\ln 10 = 2.6\,\mathrm{K}$. Then $\Delta n = 2.6\times\Delta H_{\mathrm{U}}/(RT_{\mathrm{m}}^2) = 2.6\times1.5\times10^5/(8.314\times330^2) = 0.43$ ions per molecule.

10. In a ribozyme folding experiment, $15\,\%$ of the activity appears within $2\,\mathrm{s}$ and the rest with a half-time of $20\,\mathrm{min}$. Adding urea to $1\,\mathrm{M}$ during folding increases the fast fraction to $40\,\%$, although urea destabilizes the native state. Explain. What would an RNA chaperone change?

    **Answer** The data show kinetic partitioning with $\Phi = 0.15$ and $k_{\mathrm{MN}} = \ln 2/1200\,\mathrm{s} = 5.8\times10^{-4}\,\mathrm{s^{-1}}$. Urea destabilizes the misfolded helices more than it slows the direct route (or prevents the early formation of the trap), changing the ratio $k_{\mathrm{N}}/k_{\mathrm{M}}$ of the competing early steps; the partition factor depends on rates, not on the stability of the final states. A DEAD-box chaperone increases $k_{\mathrm{MN}}$ (the slow phase becomes faster) without necessarily changing $\Phi$.

11. (Design) How would you show that a riboswitch is under kinetic rather than thermodynamic control?

    **Answer** Measure $K_{\mathrm{D}}$ of the isolated aptamer at equilibrium and the ligand concentration $T_{50}$ for half-maximal switching in single-round transcription assays. Kinetic control predicts $T_{50} > K_{\mathrm{D}}$ and a dependence of $T_{50}$ on transcription speed: lowering NTP concentrations or adding a pause site before the terminator (longer decision window) lowers $T_{50}$ towards $K_{\mathrm{D}}$, and faster polymerases raise it; adding ligand after the transcript is complete has no effect. Under thermodynamic control $T_{50} \approx K_{\mathrm{D}}$ independently of speed.
