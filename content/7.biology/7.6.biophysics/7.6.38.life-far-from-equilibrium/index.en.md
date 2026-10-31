---
title: Life Far from Equilibrium
description: "Nonequilibrium steady states of Markov jump processes: probability currents, the Kolmogorov criterion, cycle affinities and the coupling of a cycle to ATP hydrolysis, the steady-state flux of the three-state cycle and its saturation far from equilibrium, observing broken detailed balance. Schnakenberg's entropy production and its cycle decomposition. Stochastic thermodynamics: heat and entropy along a trajectory, the detailed and integral fluctuation theorems. The thermodynamic uncertainty relation with a proof by the Cramér–Rao inequality, its consequences for motors and the cost of Brownian clocks such as KaiABC. The free-energy cost of sensitivity, accuracy and adaptation."
---

Equilibrium is the state in which nothing happens on average: every elementary process runs as often forward as backward, and no free energy is spent. A living cell is never there. It keeps ATP at a concentration some ten orders of magnitude above its equilibrium value, so that the enzymes and machines that use ATP run in cycles with a preferred direction, and it pays for this with a steady dissipation of free energy into heat. The previous chapters met this regime many times: motors walking along filaments ([7.6.27](/7.6.27)), proofreading enzymes ([7.6.17](/7.6.17#sec-17.9)), the adapting receptors of bacterial chemotaxis ([7.6.35](/7.6.35)) and the KaiABC clock ([7.6.33](/7.6.33#sec-33.6.2)). This chapter gives the general theory behind them, following the third part of the framework of the course, quantitative biology. Its subject is the nonequilibrium steady state of a network of chemical states: how to recognize it, how to compute its fluxes and its **entropy production**, what the fluctuations of a single trajectory obey (the fluctuation theorems of stochastic thermodynamics), and what it costs, in free energy, to be precise, accurate, sensitive or adaptive.

The linear thermodynamics of irreversible processes near equilibrium, with Onsager's relations and the principle of minimum entropy production, was developed in [6.3.18](/6.3.18); the entropy balance of open systems and Landauer's principle in [7.6.2](/7.6.2#sec-2.4); the law of mass action, **detailed balance** and the free energy of ATP hydrolysis in [7.6.3](/7.6.3#sec-3.5.2); the **master equation** in [7.6.5](/7.6.5#sec-5.5.1); and the Jarzynski and Crooks relations for pulled molecules in [7.6.17](/7.6.17#sec-17.6). Here we work far from equilibrium, where the driving forces are tens of $k_{\mathrm{B}}T$ and the linear theory does not apply. The network design principles that use these costs, in signaling, gene regulation and development, are the subject of systems biology ([7.9](/7.9)).

## 38.1. Equilibrium and Nonequilibrium Steady States

### 38.1.1. Probability Currents

We describe a molecule (an enzyme, a receptor, a motor) by a finite set of discrete states $i$ and the rates $w_{ij}$ of the transitions from state $j$ to state $i$. The probabilities $p_i(t)$ obey the master equation of [7.6.5](/7.6.5#sec-5.5.1),

$$
\frac{\mathrm{d}p_i}{\mathrm{d}t} = \sum_{j\ne i}J_{ij}, \qquad J_{ij} = w_{ij}p_j - w_{ji}p_i, \tag{38.1}
$$
where $J_{ij} = -J_{ji}$ is the net probability current from $j$ to $i$. We assume that every transition is reversible ($w_{ij} > 0$ whenever $w_{ji} > 0$), as microscopic reversibility requires, and that the network is connected, so that there is a unique stationary distribution $p_i^{\mathrm{s}}$ with $\sum_jJ_{ij} = 0$ for every $i$.

**Definition 38.1.1 (Nonequilibrium Steady State)** A stationary state of Eq. (38.1) is an equilibrium state if every current vanishes, $J_{ij} = 0$ for all pairs (detailed balance); it is a **nonequilibrium steady state** (NESS) if the probabilities are constant, $\sum_jJ_{ij} = 0$ for every $i$, while some currents $J_{ij} \ne 0$.

Stationarity is Kirchhoff's current law for the probability currents: what flows into each state flows out. In a network without loops (a chain, a tree) the currents must then vanish edge by edge, and the only stationary state is equilibrium. A nonequilibrium steady state requires cycles, around which the probability can circulate. This is the precise version of the statement, made in [7.6.3](/7.6.3#sec-3.5.2), that detailed balance must be distinguished from a **steady state**: a steady state is a balance of each state, detailed balance a balance of each transition.

**Theorem 38.1.1 (Kolmogorov Criterion)** The stationary state of Eq. (38.1) satisfies detailed balance if and only if, for every cycle $i_1 \to i_2 \to \cdots \to i_n \to i_1$ of the network,

$$
w_{i_2i_1}w_{i_3i_2}\cdots w_{i_1i_n} = w_{i_1i_2}w_{i_2i_3}\cdots w_{i_ni_1}. \tag{38.2}
$$

**Proof** If detailed balance holds, $w_{i_{k+1}i_k}/w_{i_ki_{k+1}} = p_{i_{k+1}}/p_{i_k}$ on each edge, and the product of these ratios around a cycle telescopes to one. Conversely, if Eq. (38.2) holds, fix a reference state $0$ and define $q_i$ as the product of the ratios $w_{ba}/w_{ab}$ along any path from $0$ to $i$; by Eq. (38.2) the result does not depend on the path. Then $w_{ij}q_j = w_{ji}q_i$ for every edge, so $p_i = q_i/\sum_kq_k$ makes every current vanish and is stationary; by uniqueness it is the stationary distribution. $\square$

When the rates come from energies, $w_{ij}/w_{ji} = \mathrm{e}^{-(G_i - G_j)/k_{\mathrm{B}}T}$, Eq. (38.2) holds automatically because the free energy is a function of state. It can fail only if some transitions are coupled to a reservoir that is not itself at equilibrium: a pool of ATP and ADP, a proton gradient, light.

### 38.1.2. The Cycle Affinity

**Definition 38.1.2 (Cycle Affinity)** The **cycle affinity** of a cycle $C = (i_1 \to i_2 \to \cdots \to i_n \to i_1)$ of a Markov network is

$$
\mathcal{A}_C = k_{\mathrm{B}}T\ln\frac{w_{i_2i_1}w_{i_3i_2}\cdots w_{i_1i_n}}{w_{i_1i_2}w_{i_2i_3}\cdots w_{i_ni_1}}, \tag{38.3}
$$
the logarithm of the product of the rates around the cycle in one direction divided by the product in the other. By Theorem 38.1.1, the stationary state is an equilibrium if and only if every cycle affinity vanishes.

The affinity is a thermodynamic quantity, not a kinetic one. Consider the simplest cycle, three conformations A, B and C of an enzyme interconverting as A ⇌ B ⇌ C ⇌ A. If the three reactions are unimolecular, each ratio of rate constants is an equilibrium constant, $k_+/k_- = \mathrm{e}^{-(\mu^\circ_{\text{product}} - \mu^\circ_{\text{reactant}})/k_{\mathrm{B}}T}$ ([7.6.3](/7.6.3#sec-3.5.2)), and the product around the cycle is $\mathrm{e}^0 = 1$: the cycle has zero affinity, and the system relaxes to equilibrium whatever its rate constants. Now let one step use a fuel: A + T → B in place of A → B and C → A + D in place of C → A, with T and D held at constant concentrations $c_{\mathrm{T}}$ and $c_{\mathrm{D}}$ (for a kinase, T = ATP and D = ADP). With the pseudo-first-order rate constants $k_1 = k_1^0c_{\mathrm{T}}$ and $k_{-3} = k_{-3}^0c_{\mathrm{D}}$ the dynamics of A, B and C has exactly the form of the unimolecular cycle, but now

$$
\mathcal{A} = k_{\mathrm{B}}T\ln\frac{k_1k_2k_3}{k_{-1}k_{-2}k_{-3}} = \mu_{\mathrm{T}} - \mu_{\mathrm{D}} \equiv \Delta\mu, \tag{38.4}
$$
because the product of the three equilibrium constants is the equilibrium constant of the overall reaction T ⇌ D, and the concentration factors turn $\mu^\circ$ into $\mu = \mu^\circ + k_{\mathrm{B}}T\ln c$. Each turn of the cycle converts one T into one D, and the affinity is the free energy released by that conversion. Detailed balance, $k_1k_2k_3 = k_{-1}k_{-2}k_{-3}$, holds only if T and D are themselves at equilibrium. In a cell $\Delta\mu_{\mathrm{ATP}} \approx 20\,k_{\mathrm{B}}T$ ([7.6.3](/7.6.3#sec-3.2.4)), so the product of the forward rates around an ATP-driven cycle exceeds that of the backward rates by a factor $\mathrm{e}^{20} \approx 5\times10^8$. This is how the cell "breaks" detailed balance without breaking any law: the law applies to closed systems, and the cell holds its fuel pools open.

### 38.1.3. The Three-State Cycle

The stationary state of a network can be written down explicitly, by a combinatorial formula that goes back to Kirchhoff's analysis of electrical circuits and was introduced into biochemistry by King and Altman (1956) and by Hill (1966).

**Theorem 38.1.2 (Markov Chain Tree Theorem)** For a connected network with rates $w_{ij}$, the stationary probability of state $i$ is proportional to the sum, over all **spanning trees** of the network directed towards $i$ (every edge oriented along the unique path to $i$), of the product of the rates of the directed edges:

$$
p_i^{\mathrm{s}} = \frac{\Sigma_i}{\sum_k\Sigma_k}, \qquad \Sigma_i = \sum_{\text{trees } \mathcal{T} \to i}\ \prod_{(j\to l) \in \mathcal{T}}w_{lj}. \tag{38.5}
$$

The theorem is the probabilistic form of the **matrix-tree theorem** of graph theory ([1.4](/1.4)): $\Sigma_i$ is the cofactor of the generator matrix. For the three-state cycle with forward rates $k_1$ (A → B), $k_2$ (B → C), $k_3$ (C → A) and backward rates $k_{-1}$, $k_{-2}$, $k_{-3}$, each state has three spanning trees.

**Formula 38.1.1 (Steady State of the Three-State Cycle)** With total concentration $c_{\mathrm{tot}}$,

$$
\begin{aligned}
c_{\mathrm{A}} &= \frac{c_{\mathrm{tot}}}{\Sigma}\,(k_2k_3 + k_{-1}k_3 + k_{-1}k_{-2}), \qquad
c_{\mathrm{B}} = \frac{c_{\mathrm{tot}}}{\Sigma}\,(k_3k_1 + k_{-2}k_1 + k_{-2}k_{-3}), \\
c_{\mathrm{C}} &= \frac{c_{\mathrm{tot}}}{\Sigma}\,(k_1k_2 + k_{-3}k_2 + k_{-3}k_{-1}),
\end{aligned}
$$
where $\Sigma$ is the sum of the nine products in the brackets, and the cycle flux, the number of turns per unit time and the rate at which T is converted into D, is

$$
J = k_1c_{\mathrm{A}} - k_{-1}c_{\mathrm{B}} = \frac{c_{\mathrm{tot}}}{\Sigma}\left(k_1k_2k_3 - k_{-1}k_{-2}k_{-3}\right) = \frac{c_{\mathrm{tot}}\,k_{-1}k_{-2}k_{-3}}{\Sigma}\left(\mathrm{e}^{\mathcal{A}/k_{\mathrm{B}}T} - 1\right). \tag{38.6}
$$

The flux is the same on all three edges, as stationarity requires, and it vanishes exactly when the Kolmogorov condition holds. Equation (38.6) contains the whole thermodynamics of a driven cycle. Near equilibrium, $|\mathcal{A}| \ll k_{\mathrm{B}}T$, the flux is proportional to the force, $J \approx L\mathcal{A}$, with a coefficient $L = c_{\mathrm{tot}}k_{-1}k_{-2}k_{-3}/(\Sigma k_{\mathrm{B}}T)$ that is the Onsager coefficient of the cycle ([6.3.18](/6.3.18#sec-18.2.1)). Far from equilibrium the flux saturates: as $\mathcal{A}$ grows by making backward rates small, $J$ approaches $c_{\mathrm{tot}}k_1k_2k_3/(k_1k_2 + k_2k_3 + k_3k_1)$, the rate of a one-way cycle limited by its slowest step, and no further increase of the driving force speeds it up. Biological cycles, at $20\,k_{\mathrm{B}}T$ per turn, sit deep in this saturated regime, where the linear theory with its reciprocal relations and its minimum entropy production does not hold. The thermodynamics of life is nonlinear.

![Equilibrium and nonequilibrium steady states. A: a three-state cycle with the same forward rates (3, 1, 2) twice; on the left the backward rates satisfy the Kolmogorov criterion (Theorem 38.1.1, cycle affinity zero) and every transition is balanced by its reverse; on the right the backward rates are lowered by a factor e² so that the cycle affinity is 6 kBT, and a net flux circulates (arrow widths proportional to the net current, node areas to the stationary probabilities). B: in a continuous state space, here an overdamped particle in a harmonic well with an additional rotational force, the stationary density (shading) is the same Boltzmann-like distribution as without the rotation, but the probability current (streamlines) circulates: a density alone cannot tell equilibrium from a nonequilibrium steady state, the current can. C: the cycle flux of the three-state cycle (Eq. (38.6)) against the cycle affinity: linear near equilibrium (dashed, the Onsager regime), saturating far from it](./plots/cycle-flux.py)

### 38.1.4. Observing Broken Detailed Balance

Panel B of the figure points to an experimental test. A system in a nonequilibrium steady state can have the same stationary distribution as an equilibrium one; what distinguishes it is a net circulation of probability in its state space. Battle, MacKintosh, Schmidt and colleagues (2016) recorded long movies of the beating flagella of *Chlamydomonas* and of the fluctuating primary cilia of kidney epithelial cells, reduced each shape to the amplitudes of its first two principal modes, and measured the probability current in this two-dimensional space by counting transitions between neighboring bins. The flagellum shows a strong circulating current, as expected for a driven beat; the primary cilium, which was thought to fluctuate thermally, also showed a significant current, which revealed active forces inside it. The method needs no knowledge of the forces and no perturbation; it only uses the time-reversal asymmetry of the trajectories. A nonzero current in any coarse-grained description proves that the underlying dynamics is out of equilibrium, but the converse fails: a system can be far from equilibrium in variables that are not observed and look balanced in those that are. Lower bounds on the entropy production obtained from coarse-grained currents (38.4) make the test quantitative.

## 38.2. Entropy Production of Markov Processes

### 38.2.1. Schnakenberg's Formula

In the macroscopic thermodynamics of [6.3.18](/6.3.18#sec-18.1.3), the entropy production of a chemical reaction is the product of its rate and its affinity divided by $T$. Schnakenberg (1976) showed that the same structure holds edge by edge in any Markov network.

**Theorem 38.2.1 (Entropy Production of a Markov Network)** Let the network be in contact with a heat bath at temperature $T$, with rates satisfying local detailed balance, $k_{\mathrm{B}}\ln(w_{ij}/w_{ji})$ being the entropy delivered to the environment (as heat, and as the free energy of the coupled reservoirs) by the transition $j \to i$. Then the rate of change of the system's Gibbs–Shannon entropy $S_{\mathrm{sys}} = -k_{\mathrm{B}}\sum_ip_i\ln p_i$ and the entropy flow to the environment add up to the total entropy production

$$
\dot S_{\mathrm{tot}} = \frac{k_{\mathrm{B}}}{2}\sum_{i\ne j}\left(w_{ij}p_j - w_{ji}p_i\right)\ln\frac{w_{ij}p_j}{w_{ji}p_i} \ge 0, \tag{38.7}
$$
with equality if and only if detailed balance holds.

**Proof** From Eq. (38.1), $\dot S_{\mathrm{sys}} = -k_{\mathrm{B}}\sum_i\dot p_i\ln p_i = -k_{\mathrm{B}}\sum_{i\ne j}J_{ij}\ln p_i = \frac{k_{\mathrm{B}}}{2}\sum_{i\ne j}J_{ij}\ln(p_j/p_i)$, using $\sum_i\dot p_i = 0$ and the antisymmetry of $J_{ij}$. The entropy flow to the environment is the number of transitions $j \to i$ per unit time, minus those $i \to j$, times the entropy each delivers: $\dot S_{\mathrm{env}} = \frac{k_{\mathrm{B}}}{2}\sum_{i\ne j}J_{ij}\ln(w_{ij}/w_{ji})$. The sum is Eq. (38.7). Each term has the form $(a - b)\ln(a/b) \ge 0$, with equality only for $a = b$. $\square$

In a steady state $\dot S_{\mathrm{sys}} = 0$, and the total entropy production equals the entropy given to the environment: the heat dissipated, plus the free energy drawn from the fuel reservoirs, divided by $T$. Equation (38.7) is the second law for one molecule, averaged over its fluctuations; it is the precise content of the statement $\mathrm{d}_{\mathrm{i}}S \ge 0$ of [7.6.2](/7.6.2#sec-2.5.1).

### 38.2.2. Decomposition into Cycles

Because currents are conserved at every state, the steady-state currents of any network can be decomposed into currents around a set of fundamental cycles (one for each edge not in a chosen spanning tree), and the entropy production regroups accordingly.

**Formula 38.2.1 (Cycle Decomposition)** In a nonequilibrium steady state,

$$
T\dot S_{\mathrm{tot}} = \sum_CJ_C\,\mathcal{A}_C, \tag{38.8}
$$
where the sum runs over the fundamental cycles $C$ of the network, $J_C$ is the current around cycle $C$ (the current on its chord) and $\mathcal{A}_C$ its affinity (Definition 38.1.2). For a network with a single cycle, $T\dot S_{\mathrm{tot}} = J\mathcal{A}$.

For the driven three-state cycle the dissipation is $J\Delta\mu$: each turn converts a molecule of T into D and releases $\Delta\mu$ as heat. This is the macroscopic result in molecular form, and it shows that only the cycles matter: the probability of the states and the kinetic details enter only through the cycle currents. A cycle with zero affinity carries no current in the steady state, and a cycle with affinity but zero current (blocked by a vanishing rate) dissipates nothing.

**Example 38.2.1 (The Power of a Kinesin Molecule)** At saturating ATP a kinesin dimer hydrolyzes about $100$ ATP per second, one per $8\,\mathrm{nm}$ step ([7.6.27](/7.6.27)). With $\Delta\mu \approx 20\,k_{\mathrm{B}}T = 8.2\times10^{-20}\,\mathrm{J}$ per ATP, the free energy dissipated against no load is $T\dot S \approx 8\times10^{-18}\,\mathrm{W}$, an entropy production of about $2000\,k_{\mathrm{B}}$ per second. An *E. coli* cell growing rapidly turns over about $4\times10^6$ ATP per second ([7.6.2](/7.6.2#sec-2.1.6)) and dissipates about $3\times10^{-13}\,\mathrm{W}$ in a volume of about $1\,\mu\mathrm{m}^3$; a human body, at $100\,\mathrm{W}$ for $10^{14}$ cells of $10^3\,\mu\mathrm{m}^3$, dissipates about $10^{-15}\,\mathrm{W}\,\mu\mathrm{m}^{-3}$ on average.

## 38.3. Stochastic Thermodynamics

### 38.3.1. Thermodynamics of a Single Trajectory

Molecules are small enough that thermodynamic quantities fluctuate. A single kinesin occasionally steps backward and absorbs heat from the bath in doing so; a single enzyme cycle occasionally turns the wrong way. Stochastic thermodynamics makes these statements precise by defining heat, work and entropy for every trajectory.

**Definition 38.3.1 (Stochastic Thermodynamics)** **Stochastic thermodynamics** is the extension of thermodynamics to individual trajectories of small systems described by Markov dynamics (master equations or Langevin equations) in contact with a heat bath (Sekimoto 1997; Seifert 2005). For a trajectory $x(\tau)$, $0 \le \tau \le t$, of a Markov jump process, it assigns

- to each jump $j \to i$ the entropy $k_{\mathrm{B}}\ln(w_{ij}/w_{ji})$ delivered to the environment, and to the trajectory the sum $\Delta S_{\mathrm{env}}$ of these terms;
- to the system at time $\tau$ the stochastic entropy $s(\tau) = -k_{\mathrm{B}}\ln p_{x(\tau)}(\tau)$, whose average is the Gibbs–Shannon entropy;
- to the trajectory the total entropy production $\Delta S_{\mathrm{tot}} = \Delta S_{\mathrm{env}} + s(t) - s(0)$.

These quantities are random. Their averages over trajectories are the entropies of Theorem 38.2.1, $\langle\Delta S_{\mathrm{tot}}\rangle = \int_0^t\dot S_{\mathrm{tot}}\,\mathrm{d}\tau \ge 0$, but individual trajectories with $\Delta S_{\mathrm{tot}} < 0$ occur. Their statistics are constrained by exact relations.

### 38.3.2. Fluctuation Theorems

The central observation is that the entropy production of a trajectory measures how much more probable the trajectory is than its time reverse.

**Theorem 38.3.1 (Detailed Fluctuation Theorem)** Let a Markov jump process be in its stationary state, and let $P(\Delta S_{\mathrm{tot}})$ be the distribution of the total entropy production of trajectories of duration $t$. Then

$$
\frac{P(\Delta S_{\mathrm{tot}} = \Sigma)}{P(\Delta S_{\mathrm{tot}} = -\Sigma)} = \mathrm{e}^{\Sigma/k_{\mathrm{B}}}. \tag{38.9}
$$

**Proof** A trajectory $\omega$ starting in $x_0$ and jumping $x_0 \to x_1 \to \cdots \to x_n$ at times $\tau_1 < \cdots < \tau_n$ has probability density

$$
\mathcal{P}[\omega] = p_{x_0}\,w_{x_1x_0}w_{x_2x_1}\cdots w_{x_nx_{n-1}}\,\exp\Bigl(-\int_0^t r_{x(\tau)}\,\mathrm{d}\tau\Bigr),
$$
where $r_i = \sum_{j\ne i}w_{ji}$ is the escape rate. The time-reversed trajectory $\tilde\omega$ visits the same states in the opposite order for the same durations, so its exponential factor is the same, and its probability is $p_{x_n}w_{x_{n-1}x_n}\cdots w_{x_0x_1}$ times that factor. The ratio is

$$
\ln\frac{\mathcal{P}[\omega]}{\mathcal{P}[\tilde\omega]} = \ln\frac{p_{x_0}}{p_{x_n}} + \sum_{k=1}^n\ln\frac{w_{x_kx_{k-1}}}{w_{x_{k-1}x_k}} = \frac{\Delta S_{\mathrm{tot}}[\omega]}{k_{\mathrm{B}}}
$$
by Definition 38.3.1, and $\Delta S_{\mathrm{tot}}[\tilde\omega] = -\Delta S_{\mathrm{tot}}[\omega]$. Hence $P(\Sigma) = \int\mathcal{P}[\omega]\,\delta(\Delta S_{\mathrm{tot}}[\omega] - \Sigma)\,\mathcal{D}\omega = \mathrm{e}^{\Sigma/k_{\mathrm{B}}}\int\mathcal{P}[\tilde\omega]\,\delta(\Delta S_{\mathrm{tot}}[\tilde\omega] + \Sigma)\,\mathcal{D}\tilde\omega = \mathrm{e}^{\Sigma/k_{\mathrm{B}}}P(-\Sigma)$, since time reversal is a one-to-one map of trajectories. $\square$

**Corollary 38.3.1 (Integral Fluctuation Theorem and Second Law)** Under the same conditions $\langle\mathrm{e}^{-\Delta S_{\mathrm{tot}}/k_{\mathrm{B}}}\rangle = 1$, and therefore $\langle\Delta S_{\mathrm{tot}}\rangle \ge 0$ and $\mathbb{P}(\Delta S_{\mathrm{tot}} \le -\Sigma) \le \mathrm{e}^{-\Sigma/k_{\mathrm{B}}}$ for every $\Sigma > 0$.

The first statement follows by integrating $P(-\Sigma) = \mathrm{e}^{-\Sigma/k_{\mathrm{B}}}P(\Sigma)$ over $\Sigma$; the second from Jensen's inequality, $\mathrm{e}^{-\langle x\rangle} \le \langle\mathrm{e}^{-x}\rangle$; the third from Markov's inequality applied to $\mathrm{e}^{-\Delta S_{\mathrm{tot}}/k_{\mathrm{B}}}$. The integral version holds for arbitrary initial distributions and time-dependent driving as well (Seifert 2005). The second law is therefore a statement about averages and about the exponential rarity of large violations; small violations of a few $k_{\mathrm{B}}$ are common in molecules, as the figure shows. The **Jarzynski equality** and the **Crooks fluctuation theorem** of [7.6.17](/7.6.17#sec-17.6) are the versions for a system driven by a time-dependent protocol from an initial equilibrium state, where the entropy production is $(W - \Delta F)/T$; Theorem 38.3.1 is the version for a nonequilibrium steady state (Evans, Cohen and Morriss 1993; Gallavotti and Cohen 1995 for deterministic dynamics; Lebowitz and Spohn 1999 and Seifert 2005 for stochastic dynamics).

**Example 38.3.1 (A Motor Run Backward)** For the one-state motor of [7.6.27](/7.6.27#sec-27.3.2), stepping forward at rate $k_+$ and backward at rate $k_-$ with $k_+/k_- = \mathrm{e}^{x}$, $x = (\Delta\mu - Fa)/k_{\mathrm{B}}T$, the net number of steps $n$ in time $t$ is the difference of two independent Poisson variables, and $\Delta S_{\mathrm{tot}} = nxk_{\mathrm{B}}$. Its distribution satisfies $P(n)/P(-n) = (k_+/k_-)^n = \mathrm{e}^{nx}$ exactly, as Theorem 38.3.1 requires. If kinesin dissipated the full $\Delta\mu \approx 20\,k_{\mathrm{B}}T$ of an ATP in each step, backward steps would be $\mathrm{e}^{-20} \approx 2\times10^{-9}$ times as frequent as forward ones. Measured ratios of forward to backward steps are instead in the hundreds at low load, and they fall exponentially with load to one at the stall force (Nishiyama, Higuchi and Yanagida 2002; Carter and Cross 2005): the effective affinity per observed step is much smaller than $\Delta\mu$, because backward steps are not the reverse of forward ones but consume ATP through a second pathway ([7.6.27](/7.6.27#sec-27.5.1)). The fluctuation theorem applies to the total entropy production, and it identifies the free energy per step only when the observed steps are the only irreversible events, as in a tightly coupled motor.

**Example 38.3.2 (Measuring the Torque of F₁ from Its Fluctuations)** Hayashi, Ueno, Iino and Noji (2010) recorded the rotation of a probe attached to the γ subunit of F₁-ATPase ([7.6.28](/7.6.28#sec-28.2)). For a rotor driven by a constant torque $N$ against viscous drag, the entropy produced in a rotation $\Delta\theta$ is $N\Delta\theta/T$, and the fluctuation theorem gives $\ln[P(\Delta\theta)/P(-\Delta\theta)] = N\Delta\theta/k_{\mathrm{B}}T$. From the slope of the measured ratio they obtained the torque without knowing the friction coefficient of the probe, and found that the work per $120^\circ$ step, $2\pi N/3$, was close to the free energy of hydrolysis of one ATP under the conditions of the assay: the motor converts the chemical free energy into mechanical work with near-unit efficiency.

![Fluctuations of the entropy production (Gillespie simulation of the driven three-state cycle of the previous figure with cycle affinity 2 kBT, 40,000 trajectories of each duration started in the stationary state; entropy production per trajectory as in Definition 38.3.1). A: for short trajectories (t = 0.5) the distribution is narrow and almost a fifth of the trajectories have negative entropy production; for longer ones (t = 3) the mean grows in proportion to the duration and the distribution develops a comb of peaks spaced by the entropy of one cycle, while negative values remain but are exponentially suppressed. B: for both durations the logarithm of the ratio of the probabilities of +S and −S lies on the line of slope 1, as the detailed fluctuation theorem (Theorem 38.3.1) states](./plots/fluctuation-theorem.py)

## 38.4. The Thermodynamic Uncertainty Relation

### 38.4.1. Statement and Proof

The fluctuation theorems constrain the distribution of the entropy production itself. A further relation, discovered numerically by Barato and Seifert (2015) and proved by Gingrich, Horowitz, Perunov and England (2016), constrains every observable current: a motor's displacement, the number of ATP hydrolyzed, the number of turns of a clock, the number of products made.

A current of a Markov jump process is a trajectory observable of the form $\mathcal{J}_t = \sum_{\text{jumps } j \to i}d_{ij}$ with antisymmetric increments $d_{ij} = -d_{ji}$: it counts each transition with a weight that changes sign under time reversal. In the steady state its mean is $\langle\mathcal{J}_t\rangle = t\sum_{i<j}d_{ij}J_{ij}$.

**Theorem 38.4.1 (Thermodynamic Uncertainty Relation)** For any current $\mathcal{J}_t$ of a Markov jump process in a nonequilibrium steady state, observed over any time $t$,

$$
\frac{\operatorname{Var}(\mathcal{J}_t)}{\langle\mathcal{J}_t\rangle^2}\,\langle\Delta S_{\mathrm{tot}}\rangle \ge 2k_{\mathrm{B}}, \tag{38.10}
$$
where $\langle\Delta S_{\mathrm{tot}}\rangle = t\dot S_{\mathrm{tot}}$ is the mean entropy produced during the observation.

The relation says that a relative precision $\varepsilon^2 = \operatorname{Var}(\mathcal{J}_t)/\langle\mathcal{J}_t\rangle^2$ costs at least $2k_{\mathrm{B}}T/\varepsilon^2$ of free energy: halving the relative error of any output quadruples the minimal dissipation. The proof below uses only the **Cramér–Rao inequality** of statistics ([3.2](/3.2)) and an elementary inequality for logarithms (Dechant and Sasa 2018; Hasegawa and Van Vu 2019).

**Lemma 38.4.1 (Logarithmic Mean)** For $a, b > 0$, $\dfrac{2(a - b)^2}{a + b} \le (a - b)\ln\dfrac{a}{b}$.

**Proof** Both sides are symmetric in $a$ and $b$ and homogeneous of degree one, so it suffices to take $b = 1$, $a = u \ge 1$ and show $g(u) = \ln u - 2(u - 1)/(u + 1) \ge 0$. Since $g(1) = 0$ and $g'(u) = 1/u - 4/(u + 1)^2 = (u - 1)^2/[u(u + 1)^2] \ge 0$, this holds. $\square$

We now prove the theorem.

**Proof** Write $a_{ij} = w_{ij}p_j$ for the stationary flux from $j$ to $i$, $J_{ij} = a_{ij} - a_{ji}$ for the net current and $\tau_{ij} = a_{ij} + a_{ji}$ for the traffic on the edge. Consider the family of perturbed dynamics

$$
w_{ij}^\theta = w_{ij}\left(1 + \theta\,\frac{J_{ij}}{\tau_{ij}}\right),
$$
defined for small $|\theta|$. Because $J_{ji} = -J_{ij}$, the net current on each edge in the unperturbed distribution $p$ becomes $a_{ij}(1 + \theta J_{ij}/\tau_{ij}) - a_{ji}(1 - \theta J_{ij}/\tau_{ij}) = (1 + \theta)J_{ij}$. All currents are multiplied by the same factor, so they are still conserved at every state, $p$ remains the stationary distribution, and the mean of every current is $\langle\mathcal{J}_t\rangle_\theta = (1 + \theta)\langle\mathcal{J}_t\rangle$.

The trajectory of length $t$ is a sample from which $\theta$ could be estimated. The **Fisher information** of a Markov jump process started in a $\theta$-independent distribution is $I(\theta) = t\sum_{i\ne j}p_j(\partial_\theta w_{ij}^\theta)^2/w_{ij}^\theta$ (each transition type is a Poisson stream whose intensity depends on $\theta$). At $\theta = 0$,

$$
I(0) = t\sum_{i\ne j}a_{ij}\frac{J_{ij}^2}{\tau_{ij}^2} = t\sum_{i<j}\frac{J_{ij}^2}{\tau_{ij}}.
$$
The Cramér–Rao inequality for $\mathcal{J}_t$, regarded as an estimator of its own mean $(1 + \theta)\langle\mathcal{J}_t\rangle$, gives $\operatorname{Var}(\mathcal{J}_t) \ge (\partial_\theta\langle\mathcal{J}_t\rangle_\theta)^2/I(0) = \langle\mathcal{J}_t\rangle^2/I(0)$. By Lemma 38.4.1 with $a = a_{ij}$, $b = a_{ji}$, each term satisfies $J_{ij}^2/\tau_{ij} \le \frac{1}{2}J_{ij}\ln(a_{ij}/a_{ji})$, and by Theorem 38.2.1 the sum of the right-hand sides is $\dot S_{\mathrm{tot}}/(2k_{\mathrm{B}})$. Hence $I(0) \le t\dot S_{\mathrm{tot}}/(2k_{\mathrm{B}})$ and

$$
\frac{\operatorname{Var}(\mathcal{J}_t)}{\langle\mathcal{J}_t\rangle^2} \ge \frac{1}{I(0)} \ge \frac{2k_{\mathrm{B}}}{t\dot S_{\mathrm{tot}}}. \qquad \square
$$

The proof shows where the bound is tight. Lemma 38.4.1 is an equality only when $a_{ij} = a_{ji}$, so equality in Eq. (38.10) is approached only near equilibrium, where the currents are small compared with the traffic; far from equilibrium the bound is loose, and real networks lie well above it. The relation holds for continuous-time Markov dynamics with time-independent rates in a steady state and for overdamped Langevin dynamics. It can be violated by systems with momenta (underdamped dynamics, magnetic fields), by periodically driven systems, and by observables that are even under time reversal (the number of jumps, residence times); generalizations exist for these cases.

### 38.4.2. Motors and the Inference of Dissipation

For a motor the current is the displacement $X_t$, with $\langle X_t\rangle = Vt$ and $\operatorname{Var}(X_t) \approx 2Dt$, and the **randomness parameter** of [7.6.27](/7.6.27#sec-27.4.2) is $r = 2D/(Va)$. For a tightly coupled motor that dissipates $\Delta\mu - Fa$ per step of length $a$, Eq. (38.10) becomes $r(\Delta\mu - Fa) \ge 2k_{\mathrm{B}}T$, the inequality found for the one-state model in [7.6.27](/7.6.27#sec-27.5.3), where $r = \coth(x/2)$ and $rx = x\coth(x/2) \ge 2$. The one-state model saturates the bound near stall and lies far above it when strongly driven. The bound on efficiency, Formula 27.5.2, follows by inserting $T\dot S \ge 2k_{\mathrm{B}}TV/(ra) = k_{\mathrm{B}}TV^2/D$ into $\eta = FV/(FV + T\dot S)$.

Turned around, Theorem 38.4.1 is a measurement tool. The mean and the variance of an observed current, obtained from trajectories, give a lower bound on the entropy production of the whole system, however many hidden states it has: $\dot S_{\mathrm{tot}} \ge 2k_{\mathrm{B}}\langle\mathcal{J}\rangle^2/(t\operatorname{Var}\mathcal{J})$. For kinesin, whose randomness at saturating ATP and low load is about $0.5$ (Svoboda, Mitra and Block 1994; Visscher, Schnitzer and Block 1999), the bound requires at least $4\,k_{\mathrm{B}}T$ per step, consistent with the $20\,k_{\mathrm{B}}T$ actually available; a randomness below one also shows that the step contains at least two sequential substeps ([7.6.27](/7.6.27#sec-27.4.2)), which the one-state model cannot produce at any driving force.

![The thermodynamic uncertainty relation. A: the uncertainty product Q = Var(J) ⟨ΔS⟩/(⟨J⟩² kB) of a current in the long-time limit, against the entropy produced per unit current, for the one-state motor (red, Q = x coth(x/2) with x the affinity per step) and for 3000 random four-state networks with all six transitions present (rates log-uniform over four decades; the current counts net transitions between two states), computed exactly from the largest eigenvalue of the tilted generator. No point falls below the bound Q = 2 (dashed), which is approached only close to equilibrium. B: the minimum free energy a motor must dissipate per step to achieve randomness r (dashed, 2 kBT/r) and the dissipation of a one-state motor with the same randomness (red); a one-state motor cannot have r < 1. Kinesin's randomness of about 0.5 requires at least 4 kBT per step](./plots/tur.py)

### 38.4.3. The Cost of Keeping Time

A clock is a current that is meant to be regular: the number of turns of a biochemical cycle, read as elapsed time. Its precision after $M$ cycles is measured by the relative variance $\varepsilon^2 = \operatorname{Var}(n)/\langle n\rangle^2$ of the number of turns, which for a renewal process falls as $1/M$; the quantity $\varepsilon^2M$, the relative variance of a single period, characterizes the clock. Theorem 38.4.1 with the dissipation $\mathcal{A}$ per cycle gives $\varepsilon^2M \ge 2k_{\mathrm{B}}T/\mathcal{A}$ for any clock driven by a free-energy source, whatever its internal design.

**Formula 38.4.1 (Brownian Clock)** A ring of $N$ states traversed with uniform forward rate $k_+$ and backward rate $k_-$, with cycle affinity $\mathcal{A} = Nk_{\mathrm{B}}T\ln(k_+/k_-)$, has

$$
\varepsilon^2M = \frac{1}{N}\coth\frac{\mathcal{A}}{2Nk_{\mathrm{B}}T}. \tag{38.11}
$$
The precision is limited by the dissipation, $\varepsilon^2M \to 2k_{\mathrm{B}}T/\mathcal{A}$ when $\mathcal{A} \ll Nk_{\mathrm{B}}T$, and by the number of states, $\varepsilon^2M \to 1/N$ when $\mathcal{A} \gg Nk_{\mathrm{B}}T$ (Barato and Seifert 2016).

The net number of steps $n$ in time $t$ has mean $(k_+ - k_-)t$ and variance $(k_+ + k_-)t$, the number of cycles is $n/N$, and $\varepsilon^2M = (k_+ + k_-)/[N(k_+ - k_-)] = \coth(x/2)/N$ with $x = \mathcal{A}/(Nk_{\mathrm{B}}T)$. A clock that is to tick precisely must have many sequential states per period and must dissipate a free energy of many $k_{\mathrm{B}}T$ per period; with few states, extra free energy is wasted, with little free energy, extra states do not help. Rings with unequal affinities per step are less precise than the uniform ring of the same $N$ and $\mathcal{A}$.

**Example 38.4.1 (The Free-Energy Budget of KaiC)** In the KaiABC oscillator ([7.6.33](/7.6.33#sec-33.6.2)), each KaiC monomer hydrolyzes about $15$ ATP per day, about $90$ per hexamer per circadian period. At $\Delta\mu \approx 20\,k_{\mathrm{B}}T$, a hexamer dissipates about $1.8\times10^3\,k_{\mathrm{B}}T$ per cycle, which by the uncertainty relation allows a relative variance of the period as small as $1.1\times10^{-3}$, a standard deviation of about $3\,\%$ or $50$ minutes per day. Each subunit, however, passes through only four phosphorylation states in a cycle (unphosphorylated, T432, S431/T432, S431), and even the hexamer has a modest number of sequential intermediates; by Eq. (38.11) the precision of one hexamer is set by this number rather than by the free energy. The oscillation of a test tube is far more regular than that of one hexamer, because the hexamers are synchronized by their competition for KaiA, and the coherence of the collective oscillation is bought by the free energy of all of them (Cao, Wang, Ouyang and Tu 2015 showed in models that the phase coherence of biochemical oscillators requires a minimum dissipation per cycle and improves with it). Individual cyanobacteria, which couple the KaiABC clock to a transcriptional loop, keep phase for months without coupling to each other (Mihalcescu, Hsing and Leibler 2004).

![The cost and precision of a Brownian clock. A: relative variance per cycle of a ring of N states with uniform rates (Formula 38.4.1) against the free energy dissipated per cycle; every curve lies above the thermodynamic uncertainty bound 2kBT/𝒜 (dashed) and levels off at the floor 1/N set by the number of states. B: distributions of the time needed to complete ten cycles (10,000 simulated runs per clock, time in units of the mean period) for a clock with 3 states and 10 kBT per cycle, one with 30 states and 30 kBT, and one with 30 states and 300 kBT; their coefficients of variation agree with the formula, √(ε²M/10)](./plots/brownian-clock.py)

## 38.5. The Free-Energy Cost of Biological Functions

The uncertainty relation is one instance of a general pattern: many biological functions are impossible at equilibrium and their performance grows with the free energy dissipated. We look at three, sensitivity, accuracy and adaptation, with minimal models in which the dependence on the dissipation can be computed exactly.

### 38.5.1. Sensitivity

The response of a protein to an enzyme that modifies it is the archetype of signaling: a kinase K phosphorylates a substrate E to Ep, a phosphatase P removes the phosphate, and the fraction of Ep reports the activity of the kinase. The two reactions form a cycle, E → EK → Ep → EpP → E, coupled to the hydrolysis of ATP; the cycle is a **substrate cycle**, often called "futile" although it is what makes the switch work.

At equilibrium such a cycle cannot respond at all: the steady-state ratio $[\mathrm{Ep}]/[\mathrm{E}]$ is then fixed by the equilibrium constant of the overall reaction and the ATP/ADP ratio, independent of the enzymes (Theorem 35.5.2 of [7.6.35](/7.6.35#sec-35.5.4)). An enzyme accelerates a reaction in both directions without shifting its equilibrium ([7.6.3](/7.6.3#sec-3.5.3)); a kinase that operated at equilibrium would be accompanied by an equal and opposite reverse flux, and the phosphorylation level would be fixed by the free energy of the phosphoester bond alone. Only the driving of the cycle by ATP makes the output follow the input. For a single substrate molecule whose kinase binding and release are the only steps that depend on $[\mathrm{K}]$, the sensitivity $S = \partial\ln([\mathrm{Ep}]/[\mathrm{E}])/\partial\ln[\mathrm{K}]$ grows from zero at equilibrium to at most one when the cycle is strongly driven, and for any rates it obeys

$$
S \le \tanh\frac{\Delta\mu}{4k_{\mathrm{B}}T}, \tag{38.12}
$$
a special case of the universal response bounds proved by Owen, Gingrich and Horowitz (2020) for any Markov network, with $\Delta\mu$ the largest cycle affinity (panel C of the figure checks it numerically over random rate constants). Sensitivities above one, the steep switches of **ultrasensitivity**, require more: cooperativity among many molecules. In the Goldbeter–Koshland mechanism of **zero-order ultrasensitivity** ([7.3.18](/7.3.18)), the kinase and phosphatase are saturated by many substrate molecules, and the steady state switches sharply where the two maximal rates are equal; the switch is again possible only out of equilibrium, and its steepness improves with the driving force (Qian 2007). Qian's *phosphorylation energy hypothesis* summarizes these results: the ubiquity of ATP-driven modification cycles in signaling reflects the fact that sensitivity, amplification and memory in a biochemical switch are bought with free energy.

The same bounds bear on the flagellar motor of *E. coli* ([7.6.35](/7.6.35#sec-35.5.3)). For a two-state switch at equilibrium, the Hill coefficient of the CW bias as a function of CheY-P cannot exceed the difference between the numbers of CheY-P bound in the two states (the linkage relation, Theorem 4.5.2 of [7.6.4](/7.6.4)); measured Hill coefficients of $10$ to $20$ for adapted motors are close to or above the difference in bound CheY-P inferred from binding measurements. Tu (2008) proposed that the switch is driven out of equilibrium by the proton flux that powers the motor, so that the switching rates violate detailed balance; Wang, Shi, He and colleagues (2017) found that the distributions of CW and CCW dwell times of single motors are not consistent with an equilibrium two-state switch and that the switch dynamics break detailed balance. The general theory limits what dissipation can buy: the effective sensitivity of any kinetic scheme, driven or not, is bounded by a quantity that grows with its number of states and approaches it only for large driving (Owen and Horowitz 2023), so that nonequilibrium driving can raise the steepness of a switch above the equilibrium bound, but by a bounded factor that a larger cooperative unit would also give.

### 38.5.2. Accuracy

At equilibrium, a receptor R that binds a correct ligand L and a wrong ligand L′ at equal concentrations discriminates between them by the ratio of the dissociation constants, $\theta = K_{\mathrm{d}}/K_{\mathrm{d}}' < 1$ (Boltzmann's law, [7.6.17](/7.6.17#sec-17.9.1)). For the ribosome choosing tRNAs, $\theta \approx 10^{-2}$; the observed error, $10^{-4}$, is much lower. In terms of free energy, an error of $10^{-4}$ at equilibrium would require a binding free-energy difference of $k_{\mathrm{B}}T\ln10^4 = 9.2\,k_{\mathrm{B}}T$, about $23\,\mathrm{kJ\,mol^{-1}}$, twice what is measured.

Couple the binding to a driven cycle, R + L ⇌ RL ⇌ RL\* ⇌ R + L, in which the step RL → RL\* consumes a nucleotide triphosphate and the activated complex RL\* can also dissociate. If the wrong ligand dissociates $1/\theta$ times faster from both RL′ and RL′\*, the error $f = [\mathrm{RL'^*}]/[\mathrm{RL^*}]$ equals $\theta$ when the cycle is at equilibrium, whatever the rates, and can fall towards $\theta^2$ when the cycle affinity $\Delta\mu = k_{\mathrm{B}}T\ln\gamma$, $\gamma = k_1k_2k_3/(k_{-1}k_{-2}k_{-3})$, is large and the kinetics are suitably chosen. This is **kinetic proofreading** in the form of Hopfield (1974) and Ninio (1975), whose kinetic analysis, speed–accuracy trade-off and application to T-cell recognition are in [7.6.17](/7.6.17#sec-17.9) and [7.2.19](/7.2.19). Panel A of the figure shows the minimum error that can be reached at a given affinity, optimized over all rate constants: a proofreading step gains at most a factor $\theta$, and only for $\Delta\mu$ of several times $k_{\mathrm{B}}T\ln(1/\theta)$. An equivalent statement is a bound in the form of the first law: the free energy that the cycle dissipates must at least make up the missing discrimination, $\Delta\mu \ge k_{\mathrm{B}}T\ln(\theta/f)$, so that each further factor of ten in accuracy costs at least $2.3\,k_{\mathrm{B}}T$ per cycle, and in practice much more.

### 38.5.3. Adaptation

The receptors of bacterial chemotaxis adapt: after a step of attractant their activity returns to its prestimulus value, so that the cell responds to changes rather than to absolute concentrations ([7.6.35](/7.6.35), where the Barkai–Leibler mechanism and the physics of chemotaxis are developed). Adaptation is achieved by methylation of the receptors by CheR, which acts on inactive receptors, and demethylation by CheB, which acts on active ones. Together the two enzymes drive a cycle in the space of activity and methylation states: inactive receptors are methylated, become active, are demethylated, become inactive. Lan, Sartori, Neumann, Sourjik and Tu (2012) showed that this cycle must be driven for adaptation to work. At equilibrium the methylation level would be set by the free energies of the states alone, and a ligand that inactivates the receptor would shift the activity permanently; only when CheR and CheB break detailed balance, with methylation consuming S-adenosylmethionine, can the methylation level track the ligand and restore the activity. The adaptation error decreases exponentially with the free energy dissipated per methylation cycle until it reaches a floor set by kinetics, and the speed of adaptation is proportional to the dissipation rate: an energy–speed–accuracy trade-off, which they confirmed by measuring adaptation in *E. coli* cells with reduced energy supply. A scaling argument shows the form of the trade-off. In a model with methylation levels $m$, let the methylation and demethylation reactions together dissipate $\Delta G$ per cycle (a receptor methylated while inactive and demethylated while active). The rate of the backward, wrong-way transitions relative to the forward ones is $\mathrm{e}^{-\Delta G/k_{\mathrm{B}}T}$ per step, and the adaptation error, the residual dependence of the adapted activity on the ligand, is proportional to the fraction of such transitions: $\varepsilon \approx \varepsilon_0\,\mathrm{e}^{-\Delta G/(ck_{\mathrm{B}}T)}$ with a constant $c$ of order one. Adaptation to a stimulus in time $\tau_{\mathrm{a}}$ requires a methylation flux of order $\omega_m \propto 1/\tau_{\mathrm{a}}$ per receptor, so that the dissipation rate is $\dot W = \omega_m\Delta G$. Eliminating $\Delta G$,

$$
\dot W \approx c\,k_{\mathrm{B}}T\,\omega_m\ln\frac{\varepsilon_0}{\varepsilon}, \tag{38.13}
$$
the energy–speed–accuracy relation of Lan and colleagues: the power spent on adaptation is proportional to its speed and to the logarithm of its accuracy. Panel B of the figure reproduces the exponential decrease of the error with $\Delta G$, and its saturation at a floor set by the finite number of methylation levels, in a minimal model of this kind. For *E. coli*, with a few thousand receptor dimers methylated and demethylated on a time scale of seconds to minutes, the power spent is of order $10^3$–$10^4\,k_{\mathrm{B}}T\,\mathrm{s^{-1}}$ per cell, small compared with the cell's total dissipation of about $10^8\,k_{\mathrm{B}}T\,\mathrm{s^{-1}}$ ($4\times10^6$ ATP per second), but not zero: a cell whose energy supply is reduced adapts more slowly and less precisely, as Lan and colleagues observed.

### 38.5.4. A Common Pattern

| Function | At equilibrium | With dissipation $\Delta\mu$ per cycle | Chapter |
|---|---|---|---|
| Directed motion | no net current (no ratchet works) | velocity, efficiency $\le$ Formula 27.5.2 | [7.6.27](/7.6.27) |
| Precision of a current (motor, clock) | — | relative variance $\ge 2k_{\mathrm{B}}T/\Delta S$ (Theorem 38.4.1) | 38.4 |
| Sensitivity of a modification cycle | none (Theorem 35.5.2) | $S \le \tanh(\Delta\mu/4k_{\mathrm{B}}T)$ per molecule; collective ultrasensitivity | 38.5.1 |
| Accuracy of selection | error $\theta$ | down to $\theta^{n+1}$ with $n$ proofreading steps | [7.6.17](/7.6.17#sec-17.9) |
| Adaptation | none | error falls exponentially with $\Delta\mu$, speed $\propto$ dissipation | [7.6.35](/7.6.35) |
| Sensing | Berg–Purcell limit for a passive receptor | readout of the time history costs free energy | [7.6.35](/7.6.35) |
| Erasing a memory | — | at least $k_{\mathrm{B}}T\ln2$ per bit | [7.6.2](/7.6.2#sec-2.4.3) |
| Sustained oscillation | impossible | coherence grows with dissipation per cycle | 38.4.3, [7.6.33](/7.6.33) |

The general lesson is that biological function, in the sense of an output that depends usefully on an input, is a property of nonequilibrium steady states. The free energy that cells spend on these functions is not large in absolute terms: a bacterium that turns over a few million ATP per second can afford to spend a few hundred of them per second on its chemotactic network. But the costs are real, they are measurable through fluctuations, and evolution has to trade them against speed and against the cost of the proteins that carry them, as the growth laws of [7.6.39](/7.6.39) make explicit.

![What free energy buys, in three exact models. A: accuracy. The minimum error of the driven binding cycle R → RL → RL* → R (wrong ligand dissociating 1/θ times faster from both bound states), optimized over all rate constants at fixed cycle affinity, divided by the equilibrium error θ: it falls from 1 at zero affinity to θ (dotted), the kinetic proofreading limit f = θ², reached only for affinities of several times kBT ln(1/θ). B: adaptation. A receptor with two activity states and nine methylation levels, methylated only when inactive and demethylated only when active, the methylation cycle driven with affinity ΔG; the error of adaptation, the relative change of steady-state activity after a fivefold step of attractant, falls exponentially with ΔG and then levels off at a floor set by the finite number of methylation levels. C: sensitivity. Response of a single substrate molecule in a phosphorylation–dephosphorylation cycle to the kinase concentration, for 300 random rate sets at each driving force: zero at equilibrium and never above tanh(Δμ/4kBT) (dashed)](./plots/cost-of-function.py)

## Summary

- States and currents: A Markov network is at equilibrium when every probability current vanishes (detailed balance) and in a nonequilibrium steady state when the states are balanced but currents circulate around cycles (Definition 38.1.1). The Kolmogorov criterion (Theorem 38.1.1) and the cycle affinity $\mathcal{A}_C = k_{\mathrm{B}}T\ln(\prod w_+/\prod w_-)$ (Definition 38.1.2) decide which; for a cycle coupled to a fuel, $\mathcal{A} = \Delta\mu$ of the fuel (Eq. (38.4)), about $20\,k_{\mathrm{B}}T$ for ATP.
- Fluxes: The steady state follows from spanning trees (Theorem 38.1.2); the flux of the three-state cycle (Formula 38.1.1) is linear in $\mathcal{A}$ near equilibrium (Onsager) and saturates far from it, where biological cycles operate.
- Entropy production: $\dot S_{\mathrm{tot}} = \frac{k_{\mathrm{B}}}{2}\sum J_{ij}\ln(w_{ij}p_j/w_{ji}p_i) \ge 0$ (Theorem 38.2.1), equal in a steady state to $\sum_CJ_C\mathcal{A}_C/T$ (Formula 38.2.1).
- Fluctuation theorems: For a trajectory, $\Delta S_{\mathrm{tot}}/k_{\mathrm{B}}$ is the log-ratio of its probability to that of its time reverse; hence $P(\Sigma)/P(-\Sigma) = \mathrm{e}^{\Sigma/k_{\mathrm{B}}}$ (Theorem 38.3.1) and $\langle\mathrm{e}^{-\Delta S_{\mathrm{tot}}/k_{\mathrm{B}}}\rangle = 1$ (Corollary 38.3.1); Jarzynski and Crooks are the driven-from-equilibrium versions. Applications: back steps of motors, the torque of F₁ (Examples 38.3.1–38.3.2).
- Uncertainty relation: $\operatorname{Var}(\mathcal{J}_t)\langle\Delta S_{\mathrm{tot}}\rangle/\langle\mathcal{J}_t\rangle^2 \ge 2k_{\mathrm{B}}$ for every current (Theorem 38.4.1, proved from the Cramér–Rao inequality and Lemma 38.4.1); it bounds the efficiency of motors, gives a lower bound on hidden dissipation from observed fluctuations, and limits clocks together with the number of states, $\varepsilon^2M = \coth(\mathcal{A}/2Nk_{\mathrm{B}}T)/N$ (Formula 38.4.1).
- Cost of function: Sensitivity (Eq. (38.12)), accuracy (proofreading), adaptation and timekeeping are impossible at equilibrium and improve with the free energy dissipated per cycle (table in 38.5.4).

## Questions

1. Explain why a network without cycles (a linear chain of states) cannot have a nonequilibrium steady state, however its rates are chosen.

   **Answer** In a stationary state the currents obey Kirchhoff's law, $\sum_jJ_{ij} = 0$ at every state. In a chain, the end state has a single edge, so its current must vanish; then the next state has only one edge with possibly nonzero current, which must vanish too, and so on along the chain. All currents vanish, which is detailed balance. Equivalently, the Kolmogorov criterion has no cycles to test and holds trivially. A nonequilibrium steady state needs a loop around which probability can circulate (or a connection to reservoirs that closes one, such as a fuel pool).

2. A three-state enzyme cycle has forward rates $k_1 = 10\,\mathrm{s^{-1}}$, $k_2 = 5\,\mathrm{s^{-1}}$, $k_3 = 2\,\mathrm{s^{-1}}$ and backward rates $k_{-1} = 1\,\mathrm{s^{-1}}$, $k_{-2} = 1\,\mathrm{s^{-1}}$, $k_{-3} = 0.01\,\mathrm{s^{-1}}$. Compute the cycle affinity, the flux per enzyme and the power dissipated per enzyme.

   **Answer** $\mathcal{A}/k_{\mathrm{B}}T = \ln[(10\times5\times2)/(1\times1\times0.01)] = \ln10^4 = 9.21$. The nine products in $\Sigma$ (Formula 38.1.1) are $k_2k_3 = 10$, $k_{-1}k_3 = 2$, $k_{-1}k_{-2} = 1$, $k_3k_1 = 20$, $k_{-2}k_1 = 10$, $k_{-2}k_{-3} = 0.01$, $k_1k_2 = 50$, $k_{-3}k_2 = 0.05$, $k_{-3}k_{-1} = 0.01$, sum $93.07\,\mathrm{s^{-2}}$. The flux is $(100 - 0.01)/93.07 = 1.07\,\mathrm{s^{-1}}$ per enzyme. The dissipated power is $J\mathcal{A} = 1.07\times9.21\,k_{\mathrm{B}}T\,\mathrm{s^{-1}} = 9.9\,k_{\mathrm{B}}T\,\mathrm{s^{-1}} \approx 4\times10^{-20}\,\mathrm{W}$ at $310\,\mathrm{K}$.

3. Show that in the near-equilibrium limit the uncertainty relation is saturated by the one-state motor, and compute the uncertainty product for a motor dissipating $20\,k_{\mathrm{B}}T$ per step.

   **Answer** For the biased random walk, $\langle n\rangle = (k_+ - k_-)t$, $\operatorname{Var}(n) = (k_+ + k_-)t$ and $\langle\Delta S\rangle = xk_{\mathrm{B}}(k_+ - k_-)t$ with $x = \ln(k_+/k_-)$. The product is $Q = x(k_+ + k_-)/(k_+ - k_-) = x\coth(x/2)$. Expanding, $\coth(x/2) = 2/x + x/6 + \cdots$, so $Q = 2 + x^2/6 + \cdots \to 2$ as $x \to 0$. At $x = 20$, $\coth10 \approx 1$ and $Q \approx 20$, ten times the bound: a strongly driven one-state motor wastes most of its free energy as far as precision is concerned.

4. A single-molecule experiment records a motor whose mean velocity is $400\,\mathrm{nm\,s^{-1}}$ and whose effective diffusion coefficient is $1600\,\mathrm{nm^2\,s^{-1}}$. Nothing is known about its mechanism. What is the minimum rate of free-energy dissipation?

   **Answer** Over time $t$, $\operatorname{Var}(X)/\langle X\rangle^2 = 2Dt/(Vt)^2 = 2D/(V^2t)$. Theorem 38.4.1 gives $t\dot S \ge 2k_{\mathrm{B}}V^2t/(2D)$, so $T\dot S \ge k_{\mathrm{B}}TV^2/D = (400^2/1600)\,k_{\mathrm{B}}T\,\mathrm{s^{-1}} = 100\,k_{\mathrm{B}}T\,\mathrm{s^{-1}}$, about $4\times10^{-19}\,\mathrm{W}$. If the motor makes $8\,\mathrm{nm}$ steps ($50$ per second), this is at least $2\,k_{\mathrm{B}}T$ per step; the randomness is $r = 2D/(Va) = 1$, and the bound is $2k_{\mathrm{B}}T/r$, as it must be.

5. Why does the absence of response at equilibrium (Theorem 35.5.2) not contradict the fact that kinases are catalysts that can be inhibited and regulated in cells?

   **Answer** Regulation of a kinase changes the rate of phosphorylation, and in a cell this changes the phosphorylation level only because the cycle is driven: the phosphatase removes phosphate by hydrolysis, not by the reverse of the kinase reaction, and ATP is kept far from equilibrium with ADP and phosphate. If ATP, ADP and Pi were at equilibrium, every acceleration of the forward reaction by more kinase would be matched by an acceleration of the reverse reaction (phosphoryl transfer from Ep back to ADP), and the steady-state ratio would be fixed by thermodynamics alone. The kinase's catalytic power is the same in both cases; only in the driven case is it informative.

6. (Experimental design) You suspect that the fluctuations of a membrane-bound organelle are actively driven. Design an experiment based on broken detailed balance, and say what a negative result would and would not prove.

   **Answer** Record the organelle's shape or position at high frame rate for long times, reduce each frame to two or more coordinates (for example the first two principal shape modes), bin the coordinate space and count transitions between neighboring bins in both directions; compute the net probability current per bin and its statistical error by bootstrapping over time segments, and test whether the circulation around closed loops differs from zero. A significant circulating current proves nonequilibrium dynamics without any model; its magnitude gives, through the uncertainty relation or coarse-graining bounds, a lower bound on the dissipation. A zero current does not prove equilibrium: the driving may act in unobserved degrees of freedom, the chosen coordinates may be time-reversal symmetric projections, or the current may be below the resolution. A complementary test compares the response to a small applied force with the spontaneous fluctuations, since the fluctuation–dissipation theorem holds only at equilibrium.

7. Using Formula 38.4.1, design the cheapest Brownian clock with a relative standard deviation of the period of $5\,\%$. How many states does it need, and how much free energy per cycle?

   **Answer** We need $\varepsilon^2M = 2.5\times10^{-3}$. The floor $1/N$ requires $N > 400$. For given $N$, $\coth(\mathcal{A}/2N)/N = 2.5\times10^{-3}$ gives $\coth(\mathcal{A}/2N) = 2.5\times10^{-3}N$. With $N = 800$: $\coth y = 2$, $y = 0.549$, $\mathcal{A} = 2Ny = 879\,k_{\mathrm{B}}T$. With $N = 4000$: $\coth y = 10$, $y = 0.1003$, $\mathcal{A} = 802\,k_{\mathrm{B}}T$. As $N \to \infty$, $\mathcal{A} \to 2/2.5\times10^{-3} = 800\,k_{\mathrm{B}}T$, the uncertainty bound. So the clock needs at least $800\,k_{\mathrm{B}}T$ (40 ATP) per period and of the order of a thousand states; with only 500 states it needs $\coth y = 1.25$, $y = 1.10$, $\mathcal{A} = 1100\,k_{\mathrm{B}}T$. This is why biochemical oscillators couple many molecules: no single molecule has so many states.

8. In the proofreading scheme of 38.5.2, show that the error equals $\theta$ at zero cycle affinity whatever the rates.

   **Answer** At zero affinity detailed balance holds on every edge, so the stationary concentrations are equilibrium ones: $[\mathrm{RL^*}]/[\mathrm{R}] = k_{-3}/k_3$ along the direct edge R ⇌ RL\*, and for the wrong ligand $[\mathrm{RL'^*}]/[\mathrm{R}] = k_{-3}/k_3' = \theta k_{-3}/k_3$, the association rate $k_{-3}$ being the same and the dissociation rate $k_3' = k_3/\theta$ larger. The ratio is $f = \theta$, independent of $k_1, k_2$ and all other rates. Proofreading needs the step RL → RL\* to be effectively irreversible, which is possible only with $\gamma > 1$.

9. (Open question) The adaptation of chemotaxis receptors and the oscillation of KaiABC both use ATP-driven cycles. Suppose you could vary the ATP/ADP ratio in each system in vitro. Predict qualitatively how the adaptation error, the adaptation speed, and the period and coherence of the oscillator would change as $\Delta\mu_{\mathrm{ATP}}$ is lowered, and how you would test the predictions.

   **Answer** Adaptation: as the methylation cycle's affinity falls, the error grows (roughly exponentially in $-\Delta G$) and adaptation slows, because the net rate of methylation tracking falls with the dissipation; at very low driving the receptors no longer return to their prestimulus activity. Test with FRET between CheY-P and CheZ in cells or reconstituted receptor arrays, measuring the activity before and long after a step stimulus at several energy levels (Lan and colleagues used cells with reduced energy supply). Oscillator: below a threshold driving the oscillation should disappear (the Hopf bifurcation of the collective dynamics moves), and above it its coherence (the number of cycles over which the phase stays correlated, from the decay of the autocorrelation function of KaiC phosphorylation) should increase with $\Delta\mu$; the period may change little because it is set by the slow ATPase. Test by mixing KaiA, KaiB and KaiC at different ATP/ADP ratios and recording phosphorylation by gel shift or fluorescence over several days; Rust, Golden and O'Shea (2011) showed that the in vitro clock responds to the ATP/ADP ratio, which is how changes in metabolism between day and night entrain it.

10. Lemma 38.4.1 is an equality only when $a = b$. Use this to explain why real enzymes, operating at $20\,k_{\mathrm{B}}T$ per cycle, are far from the uncertainty bound, and what kind of design would come closer.

    **Answer** The bound is tight only when every transition has nearly equal forward and backward fluxes, that is, when each step dissipates a small fraction of $k_{\mathrm{B}}T$. An enzyme cycle with three or four steps carrying $20\,k_{\mathrm{B}}T$ has steps of $5$–$7\,k_{\mathrm{B}}T$, where $J^2/\tau$ is much smaller than $\frac{1}{2}J\ln(a/b)$ (for $a/b = \mathrm{e}^6$, $2(a-b)^2/(a+b) = 1.98(a - b)$ against $6(a - b)$, a factor three); most of the free energy is spent driving steps irreversibly rather than reducing fluctuations. A design closer to the bound divides the free energy over many small steps, as in the Brownian clock with large $N$, which needs many intermediate states; the limited number of conformations of a protein therefore caps its precision per unit of energy, and precision beyond it is obtained by combining many molecules.
