---
title: Two-State Systems, Cooperativity and Allostery
description: The state-variable description of macromolecules with discrete conformations. Two-state systems and the logistic response to a conjugate driving force; tension-, voltage- and temperature-gated channels (MscL, gating charge, TRPV1 and Q10); binding in the grand canonical distribution; the four-state receptor, occupancy versus activity and equilibrium amplification; Ising-type cooperativity, the Hill coefficient of a dimer and the Pauling and Adair models of hemoglobin; the general MWC model, its Hill limit and the nicotinic acetylcholine receptor; Wyman's linkage relation and the Bohr effect.
---

A channel is open or closed, a receptor is empty or occupied, an enzyme is phosphorylated or not. Each of these molecules has an astronomical number of atomic configurations, but for its function only a few classes of them matter, and a single variable that says which class the molecule is in captures what a cell can sense and act on. This chapter develops that idea quantitatively. With the **Boltzmann distribution** and the **partition function** of [7.6.2](/7.6.2) and the **chemical potential** of [7.6.3](/7.6.3), the probability of each state follows from the free energies of the states and from the external variables (tension, voltage, temperature, ligand concentration) that shift them (4.1). Ion channels are the cleanest examples, and their gating curves measure how much area, charge or enthalpy changes in the transition (4.2). Binding of a ligand adds a second state variable, and a receptor with two variables already distinguishes occupancy from activity and amplifies a signal (4.3). Interactions between binding sites give cooperativity (4.4), and coupling of all sites to a common conformational switch, the concerted model of Monod, Wyman and Changeux, explains allostery and the Hill function (4.5). The biochemistry of ligand binding, hemoglobin and the concerted and sequential models was described in [7.1.7](/7.1.7); here the same models are derived from statistical mechanics and applied to channels and receptors. The structure and permeation of channels follow in [7.6.30](/7.6.30), receptor clusters in bacterial chemotaxis in [7.6.35](/7.6.35), and the ways in which cells beat the limits of equilibrium switches, by spending energy, in [7.6.17](/7.6.17) and [7.6.38](/7.6.38).

## 4.1. The State-Variable Description

### 4.1.1. Two-State Systems

A protein in water explores its conformations on time scales from femtoseconds (bond vibrations) to seconds or longer (large rearrangements). When the configurations fall into a few basins separated by barriers much higher than $k_{\mathrm{B}}T$, the molecule spends long periods in each basin and jumps between them rarely and quickly; a single-channel recording ([7.1.14](/7.1.14)) shows exactly this, a current that switches between two levels within microseconds and dwells at each for milliseconds. It is then natural to label each basin by a state variable and to treat everything within a basin as one state with a free energy.

**Definition 4.1.1 (Two-State System)** A **two-state system** is a molecule or assembly whose configurations are grouped into two classes, labelled by a state variable $\sigma \in \{0, 1\}$, such that transitions between the classes are fast compared with the dwell times in each. The free energy of state $\sigma$ is $G(\sigma) = -k_{\mathrm{B}}T\ln\sum_{s \in \sigma}\mathrm{e}^{-E_s/k_{\mathrm{B}}T}$, the sum running over the microstates $s$ in that class.

Because $G(\sigma)$ already contains the entropy of the microstates within each class, the two states can be treated exactly like two energy levels. The probability of state 1 is the Boltzmann weight of that state divided by the sum of the two weights, and since $\sigma$ is 0 or 1 it equals the average of $\sigma$.

**Formula 4.1.1 (Two-State Probability)** With $\Delta G = G(1) - G(0)$ and $\beta = 1/k_{\mathrm{B}}T$,

$$
p_1 = \langle\sigma\rangle = \frac{\mathrm{e}^{-\beta G(1)}}{\mathrm{e}^{-\beta G(0)} + \mathrm{e}^{-\beta G(1)}} = \frac{1}{1 + \mathrm{e}^{\beta\Delta G}}.
$$

This logistic (Fermi) function is the basic response curve of molecular biology. It is $1/2$ when the two states have equal free energies, and a free-energy difference of $1\,k_{\mathrm{B}}T$, $2.3\,k_{\mathrm{B}}T$ or $4.6\,k_{\mathrm{B}}T$ biases the populations $2.7$-, $10$- or $100$-fold. The **two-state model** of protein unfolding ([7.1.6](/7.1.6)) is the same description applied to the native and unfolded ensembles.

### 4.1.2. Driving Forces and Sensitivity

The biologically interesting part is how $\Delta G$ depends on what the cell controls. In each case below the two states differ in some extensive property (area, charge displaced across the membrane, length, number of bound ligands, entropy), and an external intensive variable does work on that property. The free energy that is minimized at a fixed value of the intensive variable is then $G - Xq$, where $q$ is the extensive property and $X$ its conjugate variable, so that

$$
\Delta G(X) = \Delta G_0 - q X, \tag{4.1}
$$
with $q$ now the difference of the property between the two states.

| Two-state system | Control variable $X$ | Conjugate difference $q$ |
|---|---|---|
| Mechanosensitive channel | Membrane tension $\tau$ | Area change $\Delta A$ |
| Voltage-gated channel | Membrane potential $V$ | Gating charge $ze$ |
| Molecule pulled by optical tweezers ([7.6.17](/7.6.17)) | Force $F$ | Change in length $\Delta x$ |
| Receptor with one site | Chemical potential $\mu$ of the ligand | Bound ligands, $1$ |
| Thermosensitive channel | Temperature $T$ | Entropy change $\Delta S$ |

**Theorem 4.1.1 (Response of a Two-State Switch)** If $\Delta G$ depends on $X$ as in Eq. (4.1), then

$$
p_1(X) = \frac{1}{1 + \mathrm{e}^{-\beta q(X - X_{1/2})}}, \qquad X_{1/2} = \frac{\Delta G_0}{q},
$$
the slope at the midpoint is $\mathrm{d}p_1/\mathrm{d}X = \beta q/4$, and $p_1$ rises from $0.1$ to $0.9$ over an interval $\Delta X_{10\text{–}90} = 2\ln 9\,k_{\mathrm{B}}T/q \approx 4.4\,k_{\mathrm{B}}T/q$.

**Proof** Substituting Eq. (4.1) into Formula 4.1.1 gives the first expression. Differentiating, $\mathrm{d}p_1/\mathrm{d}X = \beta q\,p_1(1 - p_1)$, which is $\beta q/4$ at $p_1 = 1/2$. Solving $p_1 = 0.9$ and $p_1 = 0.1$ for $X$ gives $X - X_{1/2} = \pm\ln 9/(\beta q)$. $\square$

The theorem separates two questions that experiments answer independently. Where a switch flips, $X_{1/2}$, is set by the ratio of the intrinsic free-energy difference to the conjugate property; how sharply it flips is set by the conjugate property alone. A sharp switch needs a large change of area, charge, length or entropy between its states.

### 4.1.3. Time Averages and Rates

A single molecule is observed as a trajectory $\sigma(t)$ that alternates between the states. If the trajectory is long enough to sample both states many times, the time average equals the ensemble average (ergodicity), and

$$
p_1 = \frac{T_1}{T_0 + T_1},
$$
where $T_0$ and $T_1$ are the total times spent in the two states. This is how open probabilities are obtained from single-channel recordings: the current trace is thresholded at the midpoint between the two current levels and the open time is summed.

The same probabilities follow from the kinetics. If the molecule leaves state 0 with rate constant $k_{01}$ and state 1 with $k_{10}$, the mean dwell times are $1/k_{01}$ and $1/k_{10}$, and in a steady state the flows balance, $k_{01}p_0 = k_{10}p_1$. Combined with the equilibrium populations of Formula 4.1.1, this is the **detailed balance** condition for the two-state system:

$$
\frac{k_{01}}{k_{10}} = \mathrm{e}^{-\beta\Delta G}, \qquad p_1 = \frac{k_{01}}{k_{01} + k_{10}}, \tag{4.2}
$$
and a perturbed population relaxes back exponentially with rate $k_{01} + k_{10}$ ([7.6.3](/7.6.3)). The equilibrium data constrain only the ratio of the rates; how the ratio is split between opening and closing, and how both depend on $X$, is a question about the barrier between the states (the Kramers theory of [7.6.5](/7.6.5)).

![State, energy and statistical weight of three two-state systems. A: a tension-gated channel; opening enlarges the channel's footprint in the membrane by ΔA, and the tension τ pulling on the membrane lowers the free energy of the open state by τΔA. B: a voltage-gated channel; on opening, positively charged groups of the voltage sensor (green) move from near the inner to near the outer face of the membrane, and the membrane potential V does work zeV on the effective gating charge ze. C: a receptor that is empty (free energy 0, ligand in solution) or holds one ligand taken from a solution of chemical potential μ; the weight of the bound state is c/K_d. In each panel the probability of the lower state is its weight divided by the sum of both weights](./plots/state-energy-weight.py)

## 4.2. Ion Channels as Two-State Systems

### 4.2.1. Tension-Gated Channels

When a bacterium is moved from a concentrated to a dilute medium, water rushes in and the cell swells; most of the turgor is carried by the cell wall, but the cytoplasmic membrane is stretched, and if the tension reaches the rupture tension of a lipid bilayer (of the order of $5$–$15\,\mathrm{mN\,m^{-1}}$) the cell lyses. *Escherichia coli* protects itself with **mechanosensitive channels** ([7.3.5](/7.3.5)) that open under tension and release solutes. The largest of them, MscL (mechanosensitive channel of large conductance), forms a pentameric pore of about $3\,\mathrm{nm}$ diameter with a conductance of about $3\,\mathrm{nS}$; it opens only near the rupture tension and acts as an emergency valve.

Opening MscL tilts and spreads its transmembrane helices, so that the channel occupies a larger area of the membrane. At constant membrane tension $\tau$ the free energy that is minimized contains $-\tau A$ for the area $A$ occupied by the protein (the tension does work $\tau\Delta A$ when the channel expands), and Eq. (4.1) gives the following.

**Formula 4.2.1 (Tension Gating)** A channel whose open state occupies an area larger by $\Delta A$ and has a higher free energy by $\Delta\varepsilon$ at zero tension has open probability

$$
p_{\mathrm{o}}(\tau) = \frac{1}{1 + \mathrm{e}^{\beta(\Delta\varepsilon - \tau\Delta A)}}, \qquad \tau_{1/2} = \frac{\Delta\varepsilon}{\Delta A}.
$$

A convenient unit for tension is $k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 4.1\,\mathrm{pN\,nm^{-1}} = 4.1\,\mathrm{mN\,m^{-1}}$ at room temperature.

**Example 4.2.1 (MscL)** Patch-clamp measurements of MscL in *E. coli* spheroplasts and reconstituted membranes, fitted with Formula 4.2.1, give a free-energy difference of about $50\,k_{\mathrm{B}}T$ and an area change of about $20\,\mathrm{nm^2}$ (Sukharev and colleagues, 1999). The midpoint tension is $\tau_{1/2} = 50/20\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 2.5 \times 4.1 = 10\,\mathrm{mN\,m^{-1}}$, just below the rupture tension, and by Theorem 4.1.1 the channel goes from $10\,\%$ to $90\,\%$ open over $4.4\,k_{\mathrm{B}}T/\Delta A = 0.22\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} \approx 0.9\,\mathrm{mN\,m^{-1}}$. A channel that stays closed at $\tau = 8\,\mathrm{mN\,m^{-1}}$ (open probability $\mathrm{e}^{-50 + 8 \times 20/4.1} = \mathrm{e}^{-11} \approx 2\times10^{-5}$) and is almost fully open at $12\,\mathrm{mN\,m^{-1}}$ needs both the large $\Delta\varepsilon$, so that it does not leak at ordinary tensions, and the large $\Delta A$, so that it opens decisively. The smaller channel MscS opens at about half this tension. The structure of MscL and the coupling of its gating to membrane deformation are treated in [7.6.25](/7.6.25), the membrane mechanics that sets $\tau$ in [7.6.24](/7.6.24) and mechanosensation in eukaryotes (Piezo channels, hair cells) in [7.6.31](/7.6.31).

### 4.2.2. Voltage-Gated Channels and the Gating Charge

The voltage-gated $\ce{Na+}$, $\ce{K+}$ and $\ce{Ca^2+}$ channels that produce action potentials have four voltage-sensing domains, each with a transmembrane helix (S4) that carries a positively charged arginine or lysine at every third position ([7.1.14](/7.1.14)). The field across the membrane, about $70\,\mathrm{mV}$ over $4\,\mathrm{nm}$ or $2\times10^{7}\,\mathrm{V\,m^{-1}}$, pulls these charges inward at rest; depolarization lets them move outward, and their movement is coupled to opening of the pore. If a charge $q_i$ of the protein moves through a fraction $\delta_i$ of the membrane potential $V$ during opening, the electrical work done on it is $q_i\delta_iV$, and the sum defines one number.

**Definition 4.2.1 (Gating Charge)** The **gating charge** of a voltage-gated channel is the charge $ze = \sum_i q_i\delta_i$ effectively carried across the whole membrane potential when the channel goes from the closed to the open state, so that $\Delta G(V) = \Delta G_0 - zeV$.

**Formula 4.2.2 (Voltage Gating)** A two-state voltage-gated channel with gating charge $ze$ has

$$
p_{\mathrm{o}}(V) = \frac{1}{1 + \mathrm{e}^{-ze(V - V_{1/2})/k_{\mathrm{B}}T}}, \qquad V_{1/2} = \frac{\Delta G_0}{ze},
$$
and its open probability changes $\mathrm{e}$-fold per $k_{\mathrm{B}}T/ze$ of voltage when it is mostly closed.

At $25\,{}^\circ\mathrm{C}$, $k_{\mathrm{B}}T/e = 25.7\,\mathrm{mV}$ ($26.7\,\mathrm{mV}$ at $37\,{}^\circ\mathrm{C}$). A plot of $\ln[p_{\mathrm{o}}/(1 - p_{\mathrm{o}})]$ against $V$ is a straight line with slope $ze/k_{\mathrm{B}}T$ (panel C of the figure), which gives $z$. For the *Shaker* $\ce{K+}$ channel of *Drosophila* the total gating charge is about $13\,e$ per channel, measured both from the limiting slope of $p_{\mathrm{o}}$ at very negative voltages and by counting channels and integrating the gating current, the small transient current produced by the movement of the sensors themselves (Schoppa and colleagues, 1992; Aggarwal and MacKinnon, 1996). With $z = 13$ the open probability of a mostly closed channel rises $\mathrm{e}$-fold every $2\,\mathrm{mV}$; a single elementary charge would need $26\,\mathrm{mV}$.

**Remark 4.2.1** Real voltage-gated channels have many closed states: each of the four sensors moves in several steps, and the pore opens in a final concerted step. A single Boltzmann function fitted to the whole gating curve then returns an apparent $z$ smaller than the total charge, typically a third to a half of it, because the intermediate states broaden the curve. Only the limiting slope at very low $p_{\mathrm{o}}$, where the channel must carry all its charge to open, gives the total (Almers, 1978). The two-state description is nevertheless the right starting point: it shows why voltage sensors need many charges, and the same statistical mechanics with more states is the subject of [7.6.30](/7.6.30).

![Gating curves of two-state channels. A: open probability of a tension-gated channel against membrane tension for Δε = 50 kBT and ΔA = 20 nm² (MscL-like, half-open at 10.3 mN/m) and for a channel with the same midpoint but half the area change, which is half as steep. B: open probability against membrane potential for gating charges z = 1, 4 and 12 at V½ = −40 mV and 25 °C. C: the same curves as ln[p_o/(1 − p_o)] against V are straight lines whose slope ze/kBT gives the gating charge](./plots/gating-curves.py)

### 4.2.3. Temperature-Gated Channels

The sensation of warmth, heat and cold begins with channels of the TRP (transient receptor potential) family, named after a *Drosophila* mutant, *trp*, whose photoreceptors responded only transiently to continuous light (Cosens and Manning, 1969). The capsaicin receptor TRPV1, cloned by David Julius and colleagues in 1997, is opened by capsaicin, protons and temperatures above about $42\,{}^\circ\mathrm{C}$; its structure was among the first membrane-protein structures determined at near-atomic resolution by **cryo-electron microscopy** (Liao, Cao, Julius and Cheng, 2013), and Julius shared the 2021 Nobel Prize in Physiology or Medicine with Ardem Patapoutian, who discovered the Piezo mechanosensitive channels. TRPM8 is opened by cooling below about $25\,{}^\circ\mathrm{C}$ and by menthol.

Temperature is not a force acting on a coordinate, but it enters $\Delta G = \Delta H - T\Delta S$ linearly, with the entropy difference as the conjugate property (table in 4.1.2). For a channel with temperature-independent $\Delta H$ and $\Delta S$, the midpoint is $T_{1/2} = \Delta H/\Delta S$, and with $R = N_{\mathrm{A}}k_{\mathrm{B}}$ for molar quantities the following holds.

**Formula 4.2.3 (Temperature Gating)** A two-state channel with gating enthalpy $\Delta H$ and midpoint $T_{1/2}$ has

$$
p_{\mathrm{o}}(T) = \frac{1}{1 + \exp\left[\dfrac{\Delta H}{R}\left(\dfrac{1}{T} - \dfrac{1}{T_{1/2}}\right)\right]},
$$
and the equilibrium constant $K = p_{\mathrm{o}}/(1 - p_{\mathrm{o}})$ changes over $10\,\mathrm{K}$ by the factor

$$
Q_{10} = \frac{K(T + 10\,\mathrm{K})}{K(T)} = \exp\left[\frac{\Delta H}{R}\left(\frac{1}{T} - \frac{1}{T + 10\,\mathrm{K}}\right)\right] \approx \exp\left(\frac{10\,\mathrm{K}\cdot\Delta H}{RT^2}\right).
$$

$\ln K$ against $1/T$ is a straight line of slope $-\Delta H/R$, the **van 't Hoff equation** ([6.1.8](/6.1.8)). A channel opened by heat has $\Delta H > 0$ (and $\Delta S > 0$): the open state is the high-enthalpy, high-entropy state, favoured as $T$ rises. A cold-activated channel has $\Delta H < 0$.

**Example 4.2.2 (How much enthalpy does a thermometer need?)** A typical enzymatic rate has an activation enthalpy near $50\,\mathrm{kJ\,mol^{-1}}$ and, by the same formula, $Q_{10} = \exp(10 \times 50\,000/(8.314 \times 310^2)) = 1.9$ at $37\,{}^\circ\mathrm{C}$. To go from mostly closed to mostly open over the few degrees between "warm" and "painfully hot", Theorem 4.1.1 requires $\Delta S \approx 4.4\,RT_{1/2}/\Delta T$ per mole, that is $\Delta H = T_{1/2}\Delta S \approx 4.4\,RT_{1/2}^2/\Delta T$; for $\Delta T = 5\,\mathrm{K}$ and $T_{1/2} = 315\,\mathrm{K}$ this is $730\,\mathrm{kJ\,mol^{-1}}$. Fits of TRPV1 gating give enthalpies of the order of $400\,\mathrm{kJ\,mol^{-1}}$ (about $100\,\mathrm{kcal\,mol^{-1}}$ in the literature) with a correspondingly large entropy, $\Delta S = \Delta H/T_{1/2} \approx 1.3\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$, so that the large enthalpy and entropy nearly cancel at body temperature. Such values, about $150\,k_{\mathrm{B}}T$ per channel, are comparable to the unfolding enthalpy of a small protein, and how the channel concentrates them in one transition is not settled; one proposal attributes temperature sensitivity to a change of heat capacity between the states, which would make $\Delta H$ itself temperature dependent and could let one channel respond to both heat and cold (Clapham and Miller, 2011).

![Temperature gating. A: open probability against temperature for a heat-activated channel half-open at 42 °C with gating enthalpy ΔH = 420, 630 or 840 kJ/mol (TRPV1-like) and for a cold-activated channel with ΔH = −420 kJ/mol half-open at 25 °C (TRPM8-like); dashed: the relative rate of a process with activation energy 50 kJ/mol, typical of enzymes, normalized to 1 at 55 °C, which changes only gradually. B: the van 't Hoff plot of K = p_o/(1 − p_o) gives straight lines of slope −ΔH/R. C: the temperature coefficient Q10 of the equilibrium constant at 37 °C rises exponentially with the enthalpy of the transition, from about 2 for a typical enzymatic step to more than 100 for TRPV1-like gating](./plots/trp-temperature.py)

## 4.3. Binding in the State-Variable Language

### 4.3.1. The Grand Canonical Distribution

For a receptor that exchanges ligands with the surrounding solution, the number of ligand molecules in the receptor is itself a variable. The solution acts as a reservoir of ligand at chemical potential $\mu$ as well as of energy at temperature $T$, and the Boltzmann distribution generalizes as follows.

**Definition 4.3.1 (Grand Canonical Distribution)** For a system in contact with a reservoir of energy and particles at temperature $T$ and chemical potential $\mu$, the probability of a microstate $s$ with energy $E_s$ and particle number $N_s$ is given by the **grand canonical distribution** (Gibbs distribution)

$$
p(s) = \frac{\mathrm{e}^{-\beta(E_s - N_s\mu)}}{\mathcal{Z}}, \qquad \mathcal{Z} = \sum_s \mathrm{e}^{-\beta(E_s - N_s\mu)},
$$
where $\mathcal{Z}$ is the grand partition function. The mean particle number is $\langle N\rangle = k_{\mathrm{B}}T\,\partial\ln\mathcal{Z}/\partial\mu$.

The derivation repeats the one for the Boltzmann distribution ([7.6.2](/7.6.2)): the probability of a system state is proportional to the number of microstates of the reservoir, $\mathrm{e}^{S_{\mathrm{r}}/k_{\mathrm{B}}}$, and when the system takes energy $E_s$ and $N_s$ particles from the reservoir, $S_{\mathrm{r}}$ decreases by $(E_s - \mu N_s)/T$ because $\partial S/\partial E = 1/T$ and $\partial S/\partial N = -\mu/T$. The derivative formula follows by differentiating $\ln\mathcal{Z}$.

For a receptor with one site, the states are empty ($E = 0$, $N = 0$) and bound ($E = \varepsilon_{\mathrm{b}}$, $N = 1$), so $\mathcal{Z} = 1 + \mathrm{e}^{-\beta(\varepsilon_{\mathrm{b}} - \mu)}$. In a dilute solution $\mu = \mu_0 + k_{\mathrm{B}}T\ln(c/c_0)$ ([7.6.3](/7.6.3)), and

$$
p_{\mathrm{b}} = \frac{(c/c_0)\,\mathrm{e}^{-\beta\Delta\varepsilon}}{1 + (c/c_0)\,\mathrm{e}^{-\beta\Delta\varepsilon}} = \frac{c}{c + K_{\mathrm{d}}}, \qquad K_{\mathrm{d}} = c_0\,\mathrm{e}^{\beta\Delta\varepsilon}, \quad \Delta\varepsilon = \varepsilon_{\mathrm{b}} - \mu_0, \tag{4.3}
$$
the binding curve of [7.1.7](/7.1.7), now with the **dissociation constant** expressed through a binding free energy relative to the standard state. With $c_0 = 1\,\mathrm{M}$, $\Delta\varepsilon = -12\,k_{\mathrm{B}}T$ gives $K_{\mathrm{d}} = \mathrm{e}^{-12}\,\mathrm{M} = 6\,\mu\mathrm{M}$, and every further $2.3\,k_{\mathrm{B}}T$ ($5.9\,\mathrm{kJ\,mol^{-1}}$ at $37\,{}^\circ\mathrm{C}$) of binding free energy lowers $K_{\mathrm{d}}$ tenfold. The lattice derivation of [7.6.3](/7.6.3) gives the same result; the grand canonical form is more economical when there are many sites, because the weight of a state with $N$ ligands simply carries the factor $(c/K_{\mathrm{d}})^N$. The sum $\mathcal{Z}$ over the ligation states of a protein, written as a polynomial in $c$, is the binding polynomial of [7.1.7](/7.1.7), and $\langle N\rangle = c\,\partial\ln\mathcal{Z}/\partial c$.

### 4.3.2. Two State Variables: Occupancy and Activity

Most receptors do something when they bind: they change conformation, become catalytically active or open a pore. The simplest model has two binary variables, $\sigma_{\mathrm{a}}$ for activity (inactive 0, active 1) and $\sigma_{\mathrm{b}}$ for occupancy (empty 0, bound 1), and four states. Let activation cost $\varepsilon$ in the empty receptor, and let the bound ligand stabilize the active state by an interaction energy $J > 0$:

$$
G(\sigma_{\mathrm{a}}, \sigma_{\mathrm{b}}) = \varepsilon\sigma_{\mathrm{a}} + (\varepsilon_{\mathrm{b}} - \mu)\sigma_{\mathrm{b}} - J\sigma_{\mathrm{a}}\sigma_{\mathrm{b}}.
$$
With $x = c/K_{\mathrm{I}}$, where $K_{\mathrm{I}}$ is the dissociation constant of the inactive receptor, the four weights are $1$, $\mathrm{e}^{-\beta\varepsilon}$, $x$ and $x\,\mathrm{e}^{-\beta(\varepsilon - J)}$, and the active receptor binds with the smaller dissociation constant $K_{\mathrm{A}} = K_{\mathrm{I}}\mathrm{e}^{-\beta J}$.

**Definition 4.3.2 (Occupancy and Activity)** For a receptor described by binding and activity variables, the **occupancy** $p_{\mathrm{b}} = \langle\sigma_{\mathrm{b}}\rangle$ is the probability that the site is bound and the **activity** $p_{\mathrm{a}} = \langle\sigma_{\mathrm{a}}\rangle$ the probability that the receptor is in its active state, each summed over the states of the other variable.

**Formula 4.3.1 (Four-State Receptor)** With $\mathcal{Z} = 1 + \mathrm{e}^{-\beta\varepsilon} + x\left[1 + \mathrm{e}^{-\beta(\varepsilon - J)}\right]$,

$$
p_{\mathrm{b}} = \frac{x\left[1 + \mathrm{e}^{-\beta(\varepsilon - J)}\right]}{\mathcal{Z}}, \qquad
p_{\mathrm{a}} = p_{\mathrm{a}}^{(0)}(1 - p_{\mathrm{b}}) + p_{\mathrm{a}}^{(1)}p_{\mathrm{b}}, \qquad
p_{\mathrm{a}}^{(0)} = \frac{1}{1 + \mathrm{e}^{\beta\varepsilon}},\ p_{\mathrm{a}}^{(1)} = \frac{1}{1 + \mathrm{e}^{\beta(\varepsilon - J)}},
$$
where $p_{\mathrm{a}}^{(0)}$ and $p_{\mathrm{a}}^{(1)}$ are the probabilities of being active when empty and when bound. The amplification, the ratio of activity with and without ligand, is

$$
A = \frac{p_{\mathrm{a}}^{(1)}}{p_{\mathrm{a}}^{(0)}} = \frac{1 + \mathrm{e}^{\beta\varepsilon}}{1 + \mathrm{e}^{\beta(\varepsilon - J)}} < \mathrm{e}^{\beta J}.
$$

The activity formula is exact because, given the occupancy, the receptor is active with the conditional probabilities $p_{\mathrm{a}}^{(0)}$ or $p_{\mathrm{a}}^{(1)}$. With one site, therefore, activity is occupancy rescaled between a leak $p_{\mathrm{a}}^{(0)}$ and a ceiling $p_{\mathrm{a}}^{(1)}$; the two curves have the same midpoint. The useful regime is $0 < \varepsilon < J$: a positive activation cost keeps the empty receptor quiet, a coupling larger than this cost makes the bound receptor active, and the gain is close to $\mathrm{e}^{\beta\varepsilon}$. When $\varepsilon > J$ the gain approaches its bound $\mathrm{e}^{\beta J}$, but the bound receptor is then mostly inactive as well.

**Example 4.3.1** For $\varepsilon = 5\,k_{\mathrm{B}}T$ and $J = 10\,k_{\mathrm{B}}T$, the empty receptor is active with probability $1/(1 + \mathrm{e}^{5}) = 0.0067$ and the bound one with $1/(1 + \mathrm{e}^{-5}) = 0.993$, an amplification of $148$. An interaction of $10\,k_{\mathrm{B}}T$ ($26\,\mathrm{kJ\,mol^{-1}}$), the energy of a few hydrogen bonds and a salt bridge, thus turns a receptor from essentially off to essentially on. The same coupling also works backwards: the active receptor binds $\mathrm{e}^{10} = 2\times10^4$ times more tightly than the inactive one, and a mutation or a second effector that changes $\varepsilon$ shifts the apparent affinity measured in a binding assay (panel C of the figure).

The second variable need not be a bound ligand. Covalent modification works the same way: for phosphorylation, $\sigma_{\mathrm{b}}$ records whether a residue carries a phosphate, and $J$ is the stabilization of the active conformation by the phosphate. In bacterial **two-component systems** ([7.1.15](/7.1.15)) a sensor histidine kinase is activated by its stimulus and phosphorylates a response regulator, whose phosphorylation in turn shifts its own conformational equilibrium; each step is a four-state module of this kind.

![The four-state receptor (energies in kBT). A: activity (solid) and occupancy (dashed) against ligand concentration in units of the dissociation constant K_I of the inactive receptor. With ε = 5 and J = 10 the activity rises from 0.007 to 0.993, a gain of about 150, and almost coincides with the occupancy; with ε = 2 and J = 3 it rises only from 0.12 to 0.73. With a single site, activity is always leak + (ceiling − leak) × occupancy, with the same midpoint. B: amplification against the activation cost ε for J = 4, 7 and 10; it approaches its upper bound e^J (dotted) once ε exceeds J. C: the apparent dissociation constant of the occupancy curve against ε moves from K_A = K_I e^−J (receptor mostly active) to K_I (mostly inactive): whatever changes the activation free energy changes the measured affinity](./plots/four-state.py)

## 4.4. Cooperativity from Interactions: The Ising Picture

### 4.4.1. Interacting Sites

When a protein has several binding sites, the energy of binding at one site can depend on whether the others are occupied. The natural model assigns a binary variable to each site and a pairwise interaction to each pair; it has the form of the model introduced by Wilhelm Lenz and his student Ernst Ising (1925) for ferromagnetism and used throughout physics.

**Definition 4.4.1 (Ising Model)** The **Ising model** is a system of binary variables $\sigma_i \in \{0, 1\}$ (or spins $s_i = 2\sigma_i - 1 = \pm 1$) with energy

$$
E(\sigma_1, \dots, \sigma_N) = \sum_i h_i\sigma_i + \sum_{i<j}J_{ij}\sigma_i\sigma_j,
$$
where $h_i$ is the energy of setting variable $i$ and $J_{ij}$ the interaction between variables $i$ and $j$; $J_{ij} < 0$ favours equal values of the two variables.

The same model describes the helix–coil transition of polypeptides and the melting of DNA (each residue or base pair helical or not, with an interaction that favours helical neighbours, [7.2.3](/7.2.3)), arrays of chemoreceptors ([7.6.35](/7.6.35)) and neural networks ([7.6.33](/7.6.33)). For binding, $h_i = \varepsilon - \mu$ is the free energy of occupying site $i$ and $J$ the interaction between two bound ligands.

A dimer with two identical sites, $E = \varepsilon(\sigma_1 + \sigma_2) + J\sigma_1\sigma_2$, has the grand partition function

$$
\mathcal{Z} = 1 + 2x + \omega x^2, \qquad x = \frac{c}{c_0}\mathrm{e}^{-\beta(\varepsilon - \mu_0)}, \quad \omega = \mathrm{e}^{-\beta J}, \tag{4.4}
$$
and mean occupancy

**Formula 4.4.1 (Dimer with Interacting Sites)**

$$
\langle N\rangle = x\frac{\partial\ln\mathcal{Z}}{\partial x} = \frac{2x + 2\omega x^2}{1 + 2x + \omega x^2}, \qquad
\frac{p(1,1)\,p(0,0)}{p(1,0)\,p(0,1)} = \omega.
$$

The second relation states that the occupancies of the two sites are statistically correlated exactly when $J \ne 0$: for $J < 0$ a doubly bound or empty dimer is more likely than independent sites would predict, and the binding curve is sigmoid. Without interaction, $\langle N\rangle = 2x/(1 + x)$ is twice a single-site curve.

**Theorem 4.4.1 (Hill Coefficient of a Dimer)** The binding curve of Formula 4.4.1 is half-saturated at $x = \omega^{-1/2}$, where its **Hill coefficient** is

$$
n_{\mathrm{H}} = \frac{2}{1 + \mathrm{e}^{\beta J/2}}.
$$

**Proof** With $\theta = \langle N\rangle/2 = (x + \omega x^2)/(1 + 2x + \omega x^2)$, $\theta = 1/2$ gives $2x + 2\omega x^2 = 1 + 2x + \omega x^2$, so $\omega x^2 = 1$. Since $1 - \theta = (1 + x)/(1 + 2x + \omega x^2)$,

$$
\ln\frac{\theta}{1 - \theta} = \ln x + \ln(1 + \omega x) - \ln(1 + x), \qquad
n_{\mathrm{H}} = \frac{\mathrm{d}\ln[\theta/(1 - \theta)]}{\mathrm{d}\ln x} = 1 + \frac{\omega x}{1 + \omega x} - \frac{x}{1 + x}.
$$
At $x = \omega^{-1/2}$, with $s = \omega^{1/2}$, this is $1 + s/(1 + s) - 1/(1 + s) = 2s/(1 + s) = 2/(1 + \omega^{-1/2})$, and $\omega^{-1/2} = \mathrm{e}^{\beta J/2}$. $\square$

The Hill coefficient increases from $1$ at $J = 0$ to the number of sites, $2$, as $J \to -\infty$, and is less than $1$ (negative cooperativity) for $J > 0$. For $J = -2.5\,k_{\mathrm{B}}T$, $n_{\mathrm{H}} = 2/(1 + \mathrm{e}^{-1.25}) = 1.55$. The theorem makes precise the statement of [7.1.7](/7.1.7) that $n_{\mathrm{H}}$ measures the strength of coupling, not the number of sites, and reaches the number of sites only in the limit of infinitely strong coupling.

### 4.4.2. Hemoglobin: A Hierarchy of Models

Hemoglobin has four sites, and the binding curve can be described at several levels of detail. The most general equilibrium description is Adair's (1925).

**Definition 4.4.2 (Adair Equation)** For a protein with four sites, let $K_i$ be the intrinsic association constant for binding the $i$th ligand (the macroscopic stepwise constant divided by the statistical factor of the step). The **Adair equation** gives the saturation as $\theta = \frac14\,x\,\partial\ln\mathcal{Z}/\partial x$ with

$$
\mathcal{Z} = 1 + 4K_1x + 6K_1K_2x^2 + 4K_1K_2K_3x^3 + K_1K_2K_3K_4x^4,
$$
where $x$ is the ligand concentration or partial pressure and the binomial coefficients count the ways of choosing the occupied sites.

Every mechanism for four sites in equilibrium, MWC, sequential or any other, produces a binding polynomial of this form, so the Adair constants are what a binding curve alone can determine. For human hemoglobin the fitted $K_4$ exceeds $K_1$ by a factor of order $100$: the last $\ce{O2}$ binds two orders of magnitude more tightly than the first. A model with fewer parameters must explain this. In Pauling's model (1935) all six pairs of sites interact equally, with $\omega = \mathrm{e}^{-\beta J}$ per pair of occupied sites, so that $K_2/K_1 = \omega$, $K_3/K_2 = \omega^2$, $K_4/K_3 = \omega^3$ and

$$
\mathcal{Z} = 1 + 4x + 6\omega x^2 + 4\omega^3x^3 + \omega^6x^4
$$
in units of the first intrinsic constant. In the MWC model of [7.1.7](/7.1.7) the sites do not interact directly at all; the ratios of successive constants come from the shift of the T–R equilibrium. Panel C of the figure compares the two with the same $p_{50}$ and Hill coefficient: the curves are indistinguishable. Distinguishing mechanisms requires other observables, such as the fraction of molecules in the R state measured spectroscopically or structurally, the kinetics of the individual steps, or the effect of mutations that act on the quaternary equilibrium alone.

![Cooperativity from interactions between sites. A: mean occupancy per site of a dimer with interaction energy J between bound ligands against x = (c/c0) e^−β(ε−μ0), for J = +2.5 kBT (negative cooperativity), 0 (independent sites), −2.5 and −5 kBT (positive cooperativity). B: Hill coefficient at half-saturation from Theorem 4.4.1 (line) and from numerical differentiation of the binding curves (dots); it approaches the number of sites, 2, only for very strong coupling. C: oxygen saturation of a tetramer against oxygen partial pressure: the MWC curve of 7.1.7 (L = 10⁴, c = 0.01, K_R = 0.35 kPa; p50 = 3.5 kPa, n_H = 3.0) and the Pauling model of pairwise interacting sites with the same p50 and Hill coefficient (ω = 5.3) coincide; the noncooperative curve with the same p50 shows what cooperativity buys: between the lungs (13 kPa) and active tissue (2.5 kPa) the cooperative protein releases about 0.7 of its oxygen, the hyperbolic one less than 0.4](./plots/ising-dimer.py)

## 4.5. Allostery and the MWC Model

### 4.5.1. Allostery as Coupling Through Conformations

The interaction $J$ of the Ising model is phenomenological: it does not say how a ligand at one site, often several nanometers from the next, knows that the other is occupied. Monod, Wyman and Changeux (1965) proposed that it does not need to. If the whole protein can exist in two conformations, and every site binds more tightly in one of them, then each bound ligand shifts the conformational equilibrium, and the shift changes the affinity of all other sites. The protein is an **allosteric protein** ([7.1.7](/7.1.7)), and the general phenomenon has a statistical-mechanical definition.

**Definition 4.5.1 (Allostery)** **Allostery** is the coupling between two sites of a macromolecule (for binding, modification or catalysis) that arises because the sites act on a common distribution of conformational states: binding at one site changes the populations of the states, and with them the properties of the other site.

In the **MWC model** the conformations are two, called active and inactive (R and T for hemoglobin, open and closed for a channel), each with $n$ identical, independent sites, binding with dissociation constants $K_{\mathrm{A}}$ and $K_{\mathrm{I}}$. Within a conformation the sites are independent, so summing the weights $(c/K)^N$ over all subsets of occupied sites gives $\sum_N\binom{n}{N}(c/K)^N = (1 + c/K)^n$. With free energies $\varepsilon_{\mathrm{A}}$ and $\varepsilon_{\mathrm{I}}$ of the empty conformations,

$$
\mathcal{Z} = \mathrm{e}^{-\beta\varepsilon_{\mathrm{A}}}\left(1 + \frac{c}{K_{\mathrm{A}}}\right)^n + \mathrm{e}^{-\beta\varepsilon_{\mathrm{I}}}\left(1 + \frac{c}{K_{\mathrm{I}}}\right)^n. \tag{4.5}
$$

**Formula 4.5.1 (MWC Activity and Occupancy)** With $L = \mathrm{e}^{\beta(\varepsilon_{\mathrm{A}} - \varepsilon_{\mathrm{I}})}$ the ratio of inactive to active empty molecules (as in [7.1.7](/7.1.7)),

$$
p_{\mathrm{A}} = \frac{(1 + c/K_{\mathrm{A}})^n}{(1 + c/K_{\mathrm{A}})^n + L(1 + c/K_{\mathrm{I}})^n}, \qquad
\theta = \frac{\dfrac{c}{K_{\mathrm{A}}}\left(1 + \dfrac{c}{K_{\mathrm{A}}}\right)^{n-1} + L\dfrac{c}{K_{\mathrm{I}}}\left(1 + \dfrac{c}{K_{\mathrm{I}}}\right)^{n-1}}{(1 + c/K_{\mathrm{A}})^n + L(1 + c/K_{\mathrm{I}})^n},
$$
where $p_{\mathrm{A}}$ is the activity and $\theta = \langle N\rangle/n$ the occupancy, obtained from $\langle N\rangle = c\,\partial\ln\mathcal{Z}/\partial c$.

With $n$ sites the activity is no longer a rescaled occupancy: the two curves have different shapes and midpoints (panel A of the figure below), and which of them an experiment measures matters. A binding assay measures $\theta$; an electrophysiological or enzymatic assay measures $p_{\mathrm{A}}$.

**Theorem 4.5.1 (Limits of the MWC Response)** The activity of Formula 4.5.1 has the leak $p_{\mathrm{A}}(0) = 1/(1 + L)$ and the ceiling $p_{\mathrm{A}}(\infty) = 1/[1 + L(K_{\mathrm{A}}/K_{\mathrm{I}})^n]$. If $L \gg 1$ and $K_{\mathrm{A}} \ll c \ll K_{\mathrm{I}}$, then

$$
p_{\mathrm{A}} \approx \frac{(c/K_{\mathrm{A}})^n}{(c/K_{\mathrm{A}})^n + L} = \frac{c^n}{c^n + K_{1/2}^n}, \qquad K_{1/2} = K_{\mathrm{A}}L^{1/n},
$$
a Hill function with Hill coefficient $n$.

**Proof** At $c = 0$ both bracketed factors are $1$. As $c \to \infty$, $(1 + c/K)^n \approx (c/K)^n$ and the ratio of the two terms tends to $L(K_{\mathrm{A}}/K_{\mathrm{I}})^n$. If $c \ll K_{\mathrm{I}}$ the inactive term is approximately $L$, and if $c \gg K_{\mathrm{A}}$ the active term is approximately $(c/K_{\mathrm{A}})^n$; the activity is then as stated, and the window in which both approximations hold contains the midpoint when $L \gg 1$ and $L^{1/n} \ll K_{\mathrm{I}}/K_{\mathrm{A}}$. $\square$

The theorem explains the success of the **Hill equation** ([7.1.7](/7.1.7)) as a phenomenological fit. Hill's original picture, in which all $n$ ligands bind at once, is physically implausible; in the MWC model the ligands bind one at a time and independently, and the high-order dependence on $c$ arises because the active conformation is populated only when many of its sites are occupied. Outside the window of the theorem the response is less steep: the Hill coefficient of the MWC curve is always less than $n$, and it is largest when the conformational switch happens in the middle of the binding range, at $L(K_{\mathrm{A}}/K_{\mathrm{I}})^{n/2} = 1$ (for hemoglobin, $n = 4$ and $K_{\mathrm{A}}/K_{\mathrm{I}} = c$, the condition $Lc^2 = 1$ of [7.1.7](/7.1.7)). The model has only three parameters, and each controls a different feature: $L$ the leak, $K_{\mathrm{A}}/K_{\mathrm{I}}$ together with $L$ the ceiling and steepness, and the scale of $K_{\mathrm{A}}$ the position on the concentration axis.

### 4.5.2. The Nicotinic Acetylcholine Receptor

The **nicotinic acetylcholine receptor** of the neuromuscular junction is a pentameric channel ($\alpha_2\beta\gamma\delta$ in the fetal and $\alpha_2\beta\delta\varepsilon$ in the adult muscle) with two acetylcholine sites at the interfaces of the $\alpha$ subunits with their neighbours. It was the first receptor to which the MWC model was applied (Changeux, Karlin and colleagues, from 1966 onward), and it shows all its features: the channel opens spontaneously, rarely, without agonist, and opens most of the time when both sites are occupied.

**Example 4.5.1 (How much does each acetylcholine contribute?)** Single-channel recordings give an unliganded open probability of the muscle receptor of the order of $10^{-6}$ and a doubly liganded open probability of about $0.95$. In Formula 4.5.1 with $n = 2$, the first gives $L \approx 10^6$ ($\varepsilon_{\mathrm{A}} - \varepsilon_{\mathrm{I}} \approx 14\,k_{\mathrm{B}}T$), and the second, at saturating agonist, $L(K_{\mathrm{A}}/K_{\mathrm{I}})^2 \approx 0.05$, so $K_{\mathrm{I}}/K_{\mathrm{A}} \approx (10^6/0.05)^{1/2} \approx 4.5\times10^3$. Each acetylcholine binds the open receptor about four thousand times more tightly than the closed one, a difference of $\ln(4.5\times10^3) = 8.4\,k_{\mathrm{B}}T$ ($22\,\mathrm{kJ\,mol^{-1}}$), and the two together pay for the $14\,k_{\mathrm{B}}T$ that opening costs. One ligand is not enough: with one site occupied the open probability is $1/[1 + 10^6/4.5\times10^3] \approx 0.004$. The receptor therefore responds to the coincidence of two acetylcholine molecules, which helps it ignore stray transmitter.

Mutations confirm that the parameters are separable. Substitutions at the binding sites, for example of the tryptophan $\alpha$W149 whose aromatic face binds the quaternary ammonium of acetylcholine by a cation–π interaction (Zhong and colleagues, 1998, with a series of fluorinated tryptophans), change $K_{\mathrm{A}}$ and $K_{\mathrm{I}}$; substitutions in the pore-lining M2 helix far from the binding sites, such as the conserved leucine at position 9′, change $L$, and each Leu9′Ser subunit introduced into the pentamer lowers the half-maximal acetylcholine concentration roughly tenfold and increases spontaneous opening (Labarca and colleagues, 1995). Both observations are what Formula 4.5.1 predicts for changes of affinity and of the gating free energy, respectively (panels B and C).

![The MWC model of a ligand-gated channel with two binding sites (nicotinic acetylcholine receptor). A: open probability (solid) and occupancy of the binding sites (dashed) against acetylcholine concentration in units of the closed-state dissociation constant K_C, for K_C/K_O = 100 and gating energies ε = εopen − εclosed = 3, 5 and 7 kBT; increasing ε lowers the spontaneous open probability 1/(1 + e^ε) and shifts the response to higher concentrations, and the activity and occupancy curves have different midpoints. B: open probability for ε = 5 kBT and K_C/K_O = 10, 100 and 1000: the ratio of affinities sets the ceiling and the sharpness. C: half-maximal concentration (solid, left axis) and Hill coefficient of the normalized open probability (dashed, right axis) against ε for K_C/K_O = 100; mutations that change only the gating energy shift the EC50 by orders of magnitude, and the Hill coefficient is largest, but below n = 2, near ε = ln(K_C/K_O) ≈ 4.6 kBT, where the switch happens in the middle of the binding range](./plots/mwc-channel.py)

### 4.5.3. Linkage: Why Allostery Is Reciprocal

In the MWC model a ligand that prefers the active state shifts the population towards it, and a second ligand that also prefers it binds more tightly as a result. The coupling is necessarily mutual, and its strength is the same in both directions. This is a theorem about any system in equilibrium with reservoirs of two ligands.

**Theorem 4.5.2 (Wyman's Linkage Relation)** For a macromolecule in equilibrium with ligands A and B at chemical potentials $\mu_{\mathrm{A}}$ and $\mu_{\mathrm{B}}$, the mean numbers of bound ligands satisfy

$$
\frac{\partial\langle N_{\mathrm{A}}\rangle}{\partial\mu_{\mathrm{B}}} = \frac{\partial\langle N_{\mathrm{B}}\rangle}{\partial\mu_{\mathrm{A}}}.
$$
At constant saturation by A, the activity $a_{\mathrm{A}}$ of A needed for that saturation changes with the activity of B as

$$
\left(\frac{\partial\ln a_{\mathrm{A}}}{\partial\ln a_{\mathrm{B}}}\right)_{\langle N_{\mathrm{A}}\rangle} = -\left(\frac{\partial\langle N_{\mathrm{B}}\rangle}{\partial\langle N_{\mathrm{A}}\rangle}\right)_{a_{\mathrm{B}}}.
$$

**Proof** Both sides of the first relation equal $k_{\mathrm{B}}T\,\partial^2\ln\mathcal{Z}/\partial\mu_{\mathrm{A}}\partial\mu_{\mathrm{B}}$, by Definition 4.3.1 applied to each ligand. For the second, write $\ln a_i = \beta(\mu_i - \mu_i^\circ)$. Along a curve of constant $\langle N_{\mathrm{A}}\rangle$, $\mathrm{d}\langle N_{\mathrm{A}}\rangle = \frac{\partial\langle N_{\mathrm{A}}\rangle}{\partial\ln a_{\mathrm{A}}}\mathrm{d}\ln a_{\mathrm{A}} + \frac{\partial\langle N_{\mathrm{A}}\rangle}{\partial\ln a_{\mathrm{B}}}\mathrm{d}\ln a_{\mathrm{B}} = 0$, so the left side equals $-\frac{\partial\langle N_{\mathrm{A}}\rangle/\partial\ln a_{\mathrm{B}}}{\partial\langle N_{\mathrm{A}}\rangle/\partial\ln a_{\mathrm{A}}}$; by the first relation the numerator is $\partial\langle N_{\mathrm{B}}\rangle/\partial\ln a_{\mathrm{A}}$, and the quotient of the two derivatives at constant $a_{\mathrm{B}}$ is $\partial\langle N_{\mathrm{B}}\rangle/\partial\langle N_{\mathrm{A}}\rangle$. $\square$

**Example 4.5.2 (The Bohr effect)** For hemoglobin, let A be $\ce{O2}$ and B the proton, with $\ln a_{\mathrm{B}} = -\ln 10\cdot\mathrm{pH}$. At half-saturation the theorem reads $\partial\lg p_{50}/\partial\mathrm{pH} = \partial\langle N_{\ce{H+}}\rangle/\partial\langle N_{\ce{O2}}\rangle$. The measured Bohr coefficient of human blood, $\partial\lg p_{50}/\partial\mathrm{pH} \approx -0.5$, therefore means that about $0.5$ protons are released for each $\ce{O2}$ bound, about two per tetramer between deoxy- and oxyhemoglobin, a number confirmed by direct titration. The **Bohr effect** ([7.1.7](/7.1.7)) and the release of protons on oxygenation are the same fact seen from the two ligands. In the MWC model, protons, $\ce{CO2}$ and 2,3-bisphosphoglycerate bind more tightly to T and act by increasing $L$; a fall of blood pH from $7.4$ to $7.2$ in active muscle raises $p_{50}$ by $10^{0.1} = 1.26$-fold and unloads more oxygen.

The linkage relation contains no assumption about mechanism and holds equally for the four-state receptor of 4.3.2 (panel C of its figure is a linkage plot), for the effect of an allosteric drug on agonist binding, and for the coupling of protonation to folding or binding ([7.6.8](/7.6.8)). It also limits what equilibrium allostery can do. The gain of one ligand is bounded by $\mathrm{e}^{\beta J}$ (Formula 4.3.1), the steepness by the number of sites (Theorem 4.5.1), and a switch with high gain and no leak needs large free-energy differences between conformations. Receptor arrays in which many receptors switch together raise the effective $n$ ([7.6.35](/7.6.35)); kinetic schemes that dissipate free energy, such as covalent modification cycles operating near saturation (**zero-order ultrasensitivity**, [7.1.9](/7.1.9)) and kinetic proofreading ([7.6.17](/7.6.17)), escape the equilibrium bounds altogether ([7.6.38](/7.6.38)).

### 4.5.4. Concerted, Sequential and Ensemble Views

The MWC model is the limit in which the subunits change conformation all together; the **sequential model** of Koshland, Némethy and Filmer ([7.1.7](/7.1.7)) is the opposite limit, in which each subunit changes when it binds and interacts with its neighbours through its interfaces. In the language of this chapter, the sequential model is an Ising model in which each subunit carries a conformational variable with a strong coupling to its own ligand and a weaker coupling to its neighbours' conformations; the MWC model is the limit of infinitely strong coupling between conformations, so that only the two uniform states survive. Intermediate cases are described by the same partition functions with more states.

Two further points follow from the statistical view. First, the states of Definition 4.5.1 need not differ in average structure: a ligand can couple distant sites by changing the amplitude of fluctuations, and thus the conformational entropy, without any change of mean conformation (Cooper and Dryden, 1984), a mechanism detected by NMR relaxation ([7.6.13](/7.6.13)). Second, allosteric proteins usually exist as ensembles of many conformations, of which crystal or cryo-EM structures capture the most populated, and an effector redistributes the ensemble rather than switching a single structure; the two-state MWC model is the coarsest useful description of such an ensemble, and its success for hemoglobin, ligand-gated channels, chemoreceptors and transcription factors (the induction of the lac repressor by IPTG, [7.2.11](/7.2.11)) shows how often the coarse description suffices.

## Summary

| Topic | Key results |
|---|---|
| Two-state systems (Definition 4.1.1, Formula 4.1.1) | States are free-energy basins; $p_1 = 1/(1 + \mathrm{e}^{\beta\Delta G})$; a bias of $2.3\,k_{\mathrm{B}}T$ is tenfold |
| Driving forces (Eq. (4.1), Theorem 4.1.1) | $\Delta G = \Delta G_0 - qX$ for a control variable $X$ and conjugate property $q$; midpoint $\Delta G_0/q$, slope $\beta q/4$, $10$–$90\,\%$ width $4.4\,k_{\mathrm{B}}T/q$ |
| Kinetics (Eq. (4.2)) | $p_1 = T_1/(T_0 + T_1) = k_{01}/(k_{01} + k_{10})$; detailed balance $k_{01}/k_{10} = \mathrm{e}^{-\beta\Delta G}$ |
| Tension gating (Formula 4.2.1, Example 4.2.1) | $p_{\mathrm{o}} = 1/[1 + \mathrm{e}^{\beta(\Delta\varepsilon - \tau\Delta A)}]$; MscL: $50\,k_{\mathrm{B}}T$, $20\,\mathrm{nm^2}$, $\tau_{1/2} \approx 10\,\mathrm{mN\,m^{-1}}$, width $\approx 1\,\mathrm{mN\,m^{-1}}$ |
| Voltage gating (Definition 4.2.1, Formula 4.2.2, Remark 4.2.1) | Gating charge $ze = \sum q_i\delta_i$; $\mathrm{e}$-fold per $k_{\mathrm{B}}T/ze$; *Shaker* $z \approx 13$; a single Boltzmann fit underestimates $z$ |
| Temperature gating (Formula 4.2.3, Example 4.2.2) | $T_{1/2} = \Delta H/\Delta S$; $Q_{10} \approx \exp(10\,\mathrm{K}\,\Delta H/RT^2)$; TRPV1 $\Delta H \sim 400\,\mathrm{kJ\,mol^{-1}}$ versus $\sim 50$ for enzymes |
| Binding (Definition 4.3.1, Eq. (4.3)) | Grand canonical weights $\mathrm{e}^{-\beta(E - N\mu)}$; $K_{\mathrm{d}} = c_0\mathrm{e}^{\beta\Delta\varepsilon}$; $\langle N\rangle = c\,\partial\ln\mathcal{Z}/\partial c$ |
| Four-state receptor (Definition 4.3.2, Formula 4.3.1, Example 4.3.1) | Activity = leak $\times(1 - p_{\mathrm{b}})$ + ceiling $\times p_{\mathrm{b}}$; gain $(1 + \mathrm{e}^{\beta\varepsilon})/(1 + \mathrm{e}^{\beta(\varepsilon - J)}) < \mathrm{e}^{\beta J}$; $\varepsilon = 5$, $J = 10$: gain $148$ |
| Ising cooperativity (Definition 4.4.1, Formula 4.4.1, Theorem 4.4.1) | Dimer $\mathcal{Z} = 1 + 2x + \omega x^2$; correlation ratio $\omega = \mathrm{e}^{-\beta J}$; $n_{\mathrm{H}} = 2/(1 + \mathrm{e}^{\beta J/2})$ |
| Hemoglobin (Definition 4.4.2) | Adair polynomial is model-independent; Pauling and MWC fit equally; mechanism needs conformational observables |
| MWC (Definition 4.5.1, Formula 4.5.1, Theorem 4.5.1) | $p_{\mathrm{A}} = (1 + c/K_{\mathrm{A}})^n/[(1 + c/K_{\mathrm{A}})^n + L(1 + c/K_{\mathrm{I}})^n]$; leak $1/(1 + L)$; Hill limit with $K_{1/2} = K_{\mathrm{A}}L^{1/n}$; $n_{\mathrm{H}} < n$, largest at $L(K_{\mathrm{A}}/K_{\mathrm{I}})^{n/2} = 1$ |
| nAChR (Example 4.5.1) | $L \approx 10^6$, $K_{\mathrm{I}}/K_{\mathrm{A}} \approx 4.5\times10^3$ ($8.4\,k_{\mathrm{B}}T$ per ligand); binding-site mutations change $K$, pore mutations change $L$ |
| Linkage (Theorem 4.5.2, Example 4.5.2) | $\partial\langle N_{\mathrm{A}}\rangle/\partial\mu_{\mathrm{B}} = \partial\langle N_{\mathrm{B}}\rangle/\partial\mu_{\mathrm{A}}$; Bohr coefficient $-0.5$ means $0.5\,\ce{H+}$ released per $\ce{O2}$ |

## Questions

1. MscL has $\Delta\varepsilon = 50\,k_{\mathrm{B}}T$ and $\Delta A = 20\,\mathrm{nm^2}$. (a) At what tension is it half open, and over what range of tension does it go from $10\,\%$ to $90\,\%$ open? (b) A mutation lowers $\Delta\varepsilon$ to $35\,k_{\mathrm{B}}T$ without changing $\Delta A$. What is its open probability at $5\,\mathrm{mN\,m^{-1}}$, and why could such a mutant be harmful to the cell?

   **Answer** (a) $\tau_{1/2} = \Delta\varepsilon/\Delta A = 2.5\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 2.5 \times 4.11 = 10.3\,\mathrm{mN\,m^{-1}}$; the $10$–$90\,\%$ range is $2\ln 9/\Delta A = 0.22\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}} = 0.90\,\mathrm{mN\,m^{-1}}$ (Theorem 4.1.1). (b) $\beta\tau\Delta A = 5 \times 20/4.11 = 24.3$, so $p_{\mathrm{o}} = 1/(1 + \mathrm{e}^{35 - 24.3}) = 1/(1 + \mathrm{e}^{10.7}) \approx 2\times10^{-5}$, compared with $\mathrm{e}^{-25.7} \approx 7\times10^{-12}$ for the wild type. The mutant opens at $\tau_{1/2} = 35 \times 4.11/20 = 7.2\,\mathrm{mN\,m^{-1}}$, at tensions reached in ordinary growth; a pore of $3\,\mathrm{nm}$ opening even occasionally dissipates ion gradients and leaks metabolites. Gain-of-function MscL mutants of this kind indeed slow or stop bacterial growth.

2. For a sodium channel in a lipid bilayer, the fitted free-energy differences $\varepsilon_{\mathrm{open}} - \varepsilon_{\mathrm{closed}}$ were $3.24$, $1.14$, $0.05$ and $-1.27\,k_{\mathrm{B}}T$ at $-125$, $-105$, $-95$ and $-85\,\mathrm{mV}$. Estimate the gating charge (take $k_{\mathrm{B}}T/e = 25.7\,\mathrm{mV}$) and the voltage of half-activation. Why is the value much smaller than the $12$–$13\,e$ measured for voltage-gated channels by other methods?

   **Answer** A least-squares line through the four points has slope $-0.111\,k_{\mathrm{B}}T$ per mV (the energy falls by $4.51\,k_{\mathrm{B}}T$ over $40\,\mathrm{mV}$), so $z = 0.111 \times 25.7 \approx 2.9$; the free-energy difference vanishes at about $-95\,\mathrm{mV}$, the midpoint. The value is an apparent charge from a two-state fit over the middle of the gating curve. With many closed states in series, the curve near the midpoint is broadened and its slope reflects only part of the charge (Remark 4.2.1); the total is obtained from the limiting slope at very low open probability or from gating currents. (The record was also obtained with a toxin-modified channel in a bilayer, conditions that alter gating.)

3. A heat-activated channel has $\Delta H = 420\,\mathrm{kJ\,mol^{-1}}$ and is half open at $42\,{}^\circ\mathrm{C}$. (a) What are $\Delta S$ and the free-energy difference at $37\,{}^\circ\mathrm{C}$ in units of $k_{\mathrm{B}}T$? (b) Calculate $p_{\mathrm{o}}$ at $37$ and $47\,{}^\circ\mathrm{C}$.

   **Answer** (a) $\Delta S = \Delta H/T_{1/2} = 420/315.15 = 1.333\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$. At $310.15\,\mathrm{K}$, $\Delta G = 420 - 310.15 \times 1.333 = 6.66\,\mathrm{kJ\,mol^{-1}}$, which divided by $RT = 2.579\,\mathrm{kJ\,mol^{-1}}$ is $2.58\,k_{\mathrm{B}}T$: two enormous terms nearly cancel. (b) $\ln K = (\Delta H/R)(1/T_{1/2} - 1/T)$: at $37\,{}^\circ\mathrm{C}$, $50\,517 \times (-5.12\times10^{-5}) = -2.58$, $K = 0.076$, $p_{\mathrm{o}} = 0.07$; at $47\,{}^\circ\mathrm{C}$, $50\,517 \times 4.96\times10^{-5} = 2.50$, $K = 12.2$, $p_{\mathrm{o}} = 0.92$. Ten degrees take the channel from $7\,\%$ to $92\,\%$ open.

4. A receptor has activation cost $\varepsilon = 3\,k_{\mathrm{B}}T$ and coupling $J = 8\,k_{\mathrm{B}}T$. Compute its leak, ceiling and gain. Then show that changing $\varepsilon$ to $8\,k_{\mathrm{B}}T$ raises the gain but makes a poor receptor.

   **Answer** Leak $1/(1 + \mathrm{e}^{3}) = 0.047$, ceiling $1/(1 + \mathrm{e}^{-5}) = 0.993$, gain $21$. With $\varepsilon = 8$: leak $1/(1 + \mathrm{e}^{8}) = 3.4\times10^{-4}$, ceiling $1/(1 + \mathrm{e}^{0}) = 0.5$, gain $1490$. The ratio is larger, but the fully occupied receptor is active only half the time, so the absolute signal at saturation is halved, and a smaller fraction of the binding energy goes into activation. Good receptors have $0 < \varepsilon < J$ with $J - \varepsilon$ of several $k_{\mathrm{B}}T$.

5. A dimeric protein binds a ligand with interaction energy $J = -4\,k_{\mathrm{B}}T$ between the two bound ligands. (a) What is its Hill coefficient at half-saturation? (b) By what factor is the probability of the doubly bound state larger than the product of the probabilities of the two singly bound states, relative to the empty state?

   **Answer** (a) $n_{\mathrm{H}} = 2/(1 + \mathrm{e}^{-2}) = 2/1.135 = 1.76$ (Theorem 4.4.1). (b) By Formula 4.4.1, $p(1,1)p(0,0)/[p(1,0)p(0,1)] = \omega = \mathrm{e}^{4} = 55$: the two sites are strongly positively correlated, which is the microscopic meaning of cooperativity.

6. Show that the Hill limit of Theorem 4.5.1 gives $K_{1/2} = K_{\mathrm{A}}L^{1/n}$, and evaluate it for $n = 4$, $K_{\mathrm{A}} = 1\,\mu\mathrm{M}$, $L = 10^4$, $K_{\mathrm{I}} = 1\,\mathrm{mM}$. Check numerically with Formula 4.5.1 whether the approximation is good.

   **Answer** Setting $(c/K_{\mathrm{A}})^n = L$ gives $c = K_{\mathrm{A}}L^{1/n} = 1 \times 10 = 10\,\mu\mathrm{M}$. At $c = 10\,\mu\mathrm{M}$ the full formula gives $(11)^4/[11^4 + 10^4(1.01)^4] = 14\,641/(14\,641 + 10\,406) = 0.58$, close to $0.5$ (the approximation $1 + c/K_{\mathrm{A}} \approx c/K_{\mathrm{A}}$ underestimates the active term by $11^4/10^4 = 1.46$). The exact midpoint is near $9\,\mu\mathrm{M}$, and the Hill coefficient there is about $3.5$, approaching $n = 4$ because $K_{\mathrm{A}} \ll K_{1/2} \ll K_{\mathrm{I}}$.

7. In Example 4.5.1, suppose a pore mutation lowers the gating free energy of the nicotinic receptor by $2.3\,k_{\mathrm{B}}T$ per mutated subunit. By how much do the spontaneous open probability and the half-maximal acetylcholine concentration change when one subunit carries the mutation? Use the Hill limit.

   **Answer** $L$ falls tenfold, from $10^6$ to $10^5$, so the spontaneous open probability $1/(1 + L)$ rises tenfold, from $10^{-6}$ to $10^{-5}$. In the Hill limit $K_{1/2} = K_{\mathrm{A}}L^{1/2}$ falls by $\sqrt{10} = 3.2$-fold. (Measured shifts for Leu9′Ser are about tenfold per subunit, which corresponds to a larger change of the gating energy, about $4.6\,k_{\mathrm{B}}T$, or to effects of the mutation on the affinities as well.)

8. The Bohr coefficient of human hemoglobin is $\partial\lg p_{50}/\partial\mathrm{pH} \approx -0.5$. (a) How many protons are released per tetramer on full oxygenation? (b) Venous blood in exercising muscle reaches pH $7.2$. By how much does $p_{50}$ change relative to pH $7.4$? (c) Use the linkage relation to explain why oxygenated blood is a stronger acid than deoxygenated blood, and why this helps carry $\ce{CO2}$.

   **Answer** (a) By Theorem 4.5.2, $0.5$ protons per $\ce{O2}$, about $2$ per tetramer. (b) $\Delta\lg p_{50} = -0.5 \times (-0.2) = 0.1$, a $1.26$-fold increase, from $3.5$ to $4.4\,\mathrm{kPa}$, which unloads extra oxygen at the same tissue partial pressure. (c) Because oxygen and protons are linked with negative coupling, binding $\ce{O2}$ lowers proton affinity, so oxyhemoglobin releases protons and is the stronger acid. In tissues, deoxygenation lets hemoglobin take up the protons produced when $\ce{CO2}$ is hydrated to $\ce{HCO3-}$, buffering the blood and allowing more $\ce{CO2}$ to be carried as bicarbonate; in the lungs the reverse happens.

9. (Experimental design) A receptor's dose–response curve, measured by its enzymatic activity, has a Hill coefficient of $2.5$. How would you decide whether the protein has at least three ligand-binding sites, and whether its cooperativity is better described by the MWC or the sequential model?

   **Answer** The Hill coefficient is a lower bound on the number of sites coupled to the response (Theorem 4.4.1, Theorem 4.5.1), so $n_{\mathrm{H}} = 2.5$ requires at least three. The number of sites is best measured directly: by binding stoichiometry (isothermal titration calorimetry, [7.6.8](/7.6.8); equilibrium dialysis), mass spectrometry of complexes, or structure. To distinguish mechanisms, compare the activity and the occupancy curves (they differ in a characteristic way in the MWC model, Formula 4.5.1), measure the fraction of molecules in each conformation at intermediate saturation (spectroscopic or structural probes, single-molecule FRET, [7.6.12](/7.6.12)), look for negative cooperativity (impossible in the MWC model), and use mutations: in the MWC model a mutation far from the binding sites should change only $L$, shifting leak and EC50 together as in panel C of the nAChR figure.

10. (Order of magnitude) Why are equilibrium two-state switches with very high gain and very low leak expensive in terms of free energy, and what is the alternative used by cells?

    **Answer** Low leak requires the inactive state to be favoured by many $k_{\mathrm{B}}T$ ($\varepsilon$ large), and high activity on binding requires the ligand to overcome this ($J > \varepsilon$); the gain cannot exceed $\mathrm{e}^{\beta J}$ per ligand, and the steepness cannot exceed the number of coupled sites. A tenfold change in output over a twofold change in input needs $n_{\mathrm{H}} \approx \ln 10/\ln 2 = 3.3$ coupled sites at least. These energies must come from binding, which also makes the ligand bind slowly off and hence makes the switch slow to reset. Cells circumvent the bounds with nonequilibrium mechanisms that spend ATP or GTP: covalent modification cycles that operate near saturation (zero-order ultrasensitivity), kinetic proofreading and cooperative receptor arrays coupled to enzymatic amplification, at the price of a continuous free-energy dissipation ([7.6.35](/7.6.35), [7.6.38](/7.6.38)).
