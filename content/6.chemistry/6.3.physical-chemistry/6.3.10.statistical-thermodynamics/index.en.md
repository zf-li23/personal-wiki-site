---
title: Foundations of Statistical Thermodynamics
description: Macrostates and microstates; systems of localized and nonlocalized particles, independent systems; the number of microstates of a distribution, Stirling's approximation and the dominance of the most probable distribution; the Boltzmann distribution from Lagrange multipliers and the identification β = 1/(kT); the probabilistic meaning of the molecular partition function, mean energy and energy fluctuations; the system partition function and its relations to U, S, A, G, H, p, C_V, and the choice of energy zero; the statistical meaning of heat, work, entropy and the third law.
source_hash: c1fdb08baa05
---

The chemical thermodynamics of the previous nine chapters starts from a few empirical laws and discusses energy conversion, direction and limits using only macroscopic quantities such as $T$, $p$, $V$, $U$ and $S$, without any reference to what matter is made of ([6.3.1](/6.3.1)). The conclusions are general and reliable, but at a price: every property datum, whether a heat capacity, a standard molar entropy or an equilibrium constant, has to be measured. Statistical thermodynamics takes the opposite route. It regards a macroscopic system as a large collection of molecules and, starting from the molecular energy levels, uses probability to compute the statistical averages that make up the macroscopic properties. It answers questions that thermodynamics cannot: why the $U$ of an ideal gas depends only on $T$, why the $C_{V,\mathrm{m}}$ of a diatomic gas is $\frac{5}{2}R$ at ordinary temperatures, what entropy means microscopically, and how to compute standard molar entropies and equilibrium constants from spectroscopic data alone.

In physics we have already used the **Boltzmann distribution** ([5.2.1](/5.2.1#sec-1.7)) for the distribution of gas molecules in an external field, and the counting of **microstates** together with the **Boltzmann entropy formula** ([5.2.4](/5.2.4#sec-4.7)) to explain the statistical meaning of the second law. This chapter systematizes these ideas. We first learn to count how many microstates an energy distribution contains (Section 10.2), then use the method of Lagrange multipliers to find the distribution with the most microstates, which is the Boltzmann distribution in terms of energy levels (Section 10.3). This leads to the central quantity of statistical thermodynamics, the **partition function**, in terms of which all thermodynamic functions are expressed (Section 10.4). The explicit partition functions for translation, rotation and vibration, and the heat capacities, entropies and equilibrium constants of ideal gases obtained from them, are the subject of the next chapter, [6.3.11](/6.3.11). The molecular energy levels used here come from quantum physics: the particle in a box and the harmonic oscillator ([5.5.3](/5.5.3)), **degeneracy** and identical particles ([5.5.4](/5.5.4)), and molecular rotational and vibrational levels ([5.5.5](/5.5.5#sec-5.3)). The mathematics is combinatorics and the **multinomial distribution** ([3.1.6](/3.1.6)) together with constrained extrema ([2.2.11](/2.2.11#sec-11.6)).

## 10.1. Basic Concepts

### 10.1.1. Macrostates and Microstates

The state of a system described only by experimentally measurable macroscopic properties ($N$, $V$, $U$, $T$, $p$, etc.) is a **macrostate**, for example an isolated system with given $\{N, V, U\}$, or a closed system in contact with a heat reservoir with given $\{N, V, T\}$. When the state of every particle in the system is specified completely, the state of the system is a **microstate** ([5.2.4 Definition 4.7.1](/5.2.4#def-4.7.1)). In quantum mechanics the energy of a particle can take only discrete levels $\varepsilon_0 < \varepsilon_1 < \varepsilon_2 < \cdots$, and stating which quantum state each particle occupies determines a microstate.

An equilibrium state that is macroscopically at rest is microscopically in constant change: molecules collide incessantly, jump between energy levels, and switch between different quantum states of the same level. A measured macroscopic quantity is the time average of a microscopic quantity. The basic procedure of statistical thermodynamics is to replace the time average by an average over microstates, thereby turning "the mechanics of a huge number of particles" into probability theory.

Statistical methods can be classified in several ways: by how a single particle is described, into classical and quantum statistics; by whether the system is in equilibrium, into equilibrium and nonequilibrium statistics; by the method of treatment, into molecular statistics, which regards the system as a collection of molecules (Boltzmann's method), and Gibbs's ensemble method. Quantum statistics is further divided by the type of particle into Bose–Einstein statistics and Fermi–Dirac statistics ([5.5.4](/5.5.4#sec-4.3.3)). This chapter treats Boltzmann statistics, which is the limit of quantum statistics when the number of particles is much smaller than the number of accessible quantum states (Section 10.2.3) and applies to all gases at ordinary temperature and pressure and to many other systems.

### 10.1.2. Classification of Statistical Systems

**Definition 10.1.1** A system whose particles can be distinguished is called a **system of localized particles** (distinguishable particles); a system whose particles cannot be distinguished is called a **system of nonlocalized particles** (indistinguishable particles).

All microscopic particles are **identical particles** ([5.5.4 Definition 4.3.1](/5.5.4#def-4.3.1)) and cannot in principle be distinguished. In a crystal, however, each atom is bound to vibrate about its own lattice site, so the site position can serve as a "label": exchanging the atoms on two sites changes the state of the system. A crystal is therefore a system of localized particles. Molecules in a gas or a liquid move throughout the container and cannot be labeled, so these are systems of nonlocalized particles.

**Definition 10.1.2** A system in which the interactions between particles can be neglected, so that the energy of the system is the sum of the particle energies $U = \sum_{i} N_i\varepsilon_i$, is called a **system of independent particles** (nearly independent particles); a system in which the interactions cannot be neglected, $U = \sum_{i} N_i\varepsilon_i + U_{\mathrm{p}}$ ($U_{\mathrm{p}}$ is the potential energy of the interactions), is called a **system of interacting particles**.

An **ideal gas** is a system of independent, nonlocalized particles. Real gases, liquids and real crystals are systems of interacting particles; but the lattice vibrations of a crystal can be decomposed into $3N$ mutually independent vibrational modes (the Einstein and Debye models), and in this sense the crystal can be treated as a system of independent, localized particles. This chapter and the next consider only (nearly) independent systems.

### 10.1.3. Energy Levels and Degeneracy

Particles with the same energy can be in different quantum states. The number of quantum states belonging to an energy level is the **degeneracy** (statistical weight) of that level, denoted $g_i$.

**Example 10.1.1 (Three-dimensional translator)** A particle of mass $m$ moves in a cubic box of edge $a$ and volume $V = a^3$. From the levels of the one-dimensional box ([5.5.3](/5.5.3#sec-3.2.2), Eq. (3.6)) and separation of variables in three directions,

$$
\varepsilon_{\mathrm{t}} = \frac{h^2}{8mV^{2/3}}\left(n_x^2 + n_y^2 + n_z^2\right), \qquad n_x, n_y, n_z = 1, 2, 3, \dots
\tag{10.1}
$$
In units of $\varepsilon^* = h^2/(8mV^{2/3})$, the lowest levels and their degeneracies are:

| $n_x^2 + n_y^2 + n_z^2$ | 3 | 6 | 9 | 11 | 12 | 14 |
|---|---|---|---|---|---|---|
| $(n_x, n_y, n_z)$ | $(1,1,1)$ | permutations of $(1,1,2)$ | permutations of $(1,2,2)$ | permutations of $(1,1,3)$ | $(2,2,2)$ | permutations of $(1,2,3)$ |
| $g$ | 1 | 3 | 3 | 3 | 1 | 6 |

For a macroscopic container the level spacing is astonishingly small: for an $\ce{N2}$ molecule ($m = 4.65\times10^{-26}\,\mathrm{kg}$) in a box with $a = 10\,\mathrm{cm}$, $\varepsilon^* \approx 1.2\times10^{-40}\,\mathrm{J}$, whereas $k_{\mathrm{B}}T = 4.1\times10^{-21}\,\mathrm{J}$ at $298\,\mathrm{K}$, a ratio of more than $10^{19}$. The number of quantum states with energy not exceeding $\varepsilon$ equals the number of lattice points in the first octant of a sphere of radius $R = (\varepsilon/\varepsilon^*)^{1/2}$, approximately $\frac{1}{8}\cdot\frac{4}{3}\pi R^3 = \frac{\pi}{6}(\varepsilon/\varepsilon^*)^{3/2}$; for $\varepsilon \sim k_{\mathrm{B}}T$ this is a number of order $10^{29}$. Translational levels can therefore be regarded as continuous, and the number of quantum states with energy near $k_{\mathrm{B}}T$ is far larger than the number of molecules.

## 10.2. Number of Microstates

### 10.2.1. Counting Tools and Stirling's Approximation

Two combinatorial formulas are needed. The number of ways to divide $N$ distinct objects into $k$ groups containing $N_1, \dots, N_k$ objects in turn ($\sum N_i = N$) is

$$
\frac{N!}{N_1!\,N_2!\cdots N_k!},
$$
which is the coefficient of the **multinomial distribution** ([3.1.6 Definition 6.2.3](/3.1.6#def-6.2.3)); the number of ways to place $N$ distinct objects into $g$ distinct boxes with no limit on the occupancy of each box is $g^N$.

The factorials in the number of microstates are factorials of numbers of order $10^{23}$ and must be handled by an asymptotic formula.

**Theorem 10.2.1 (Stirling's approximation)** As $N \to \infty$,

$$
N! \sim \sqrt{2\pi N}\left(\frac{N}{\mathrm{e}}\right)^N, \qquad \ln N! = N\ln N - N + \frac{1}{2}\ln(2\pi N) + O\!\left(\frac{1}{N}\right).
$$
In statistical thermodynamics $N$ is huge, and we use the crude form

$$
\ln N! \approx N\ln N - N.
\tag{10.2}
$$

**Proof** We prove only the crude form. $\ln N! = \sum_{k=1}^{N}\ln k$, and $\ln x$ is increasing, so

$$
\int_1^N \ln x\,\mathrm{d}x \le \sum_{k=1}^{N}\ln k \le \int_1^{N+1}\ln x\,\mathrm{d}x,
$$
that is, $N\ln N - N + 1 \le \ln N! \le (N+1)\ln(N+1) - N$. Both ends differ from $N\ln N - N$ by $O(\ln N)$, which is negligible relative to $N\ln N$. The factor $\sqrt{2\pi N}$ in the exact form can be obtained from the central limit theorem ([3.1.13 Example 13.4.3](/3.1.13#ex-13.4.3)). $\square$

The term $\frac{1}{2}\ln(2\pi N)$ dropped in Eq. (10.2) is only about $27$ for $N = 10^{23}$, completely negligible compared with $N\ln N \approx 5\times10^{24}$ (see the figure below). A corollary often used in derivations is $\frac{\mathrm{d}\ln N!}{\mathrm{d}N} \approx \ln N$.

![Relative error of Stirling's approximation for ln N!: the crude form N ln N − N has a relative error of about 1/(2N), and adding the term ½ ln(2πN) reduces it to about 1/(12N² ln N)](./plots/stirling-accuracy.py)

### 10.2.2. Number of Microstates of a System of Localized Particles

Consider a system of independent, localized particles with given $N$, $V$ and $U$. Given $V$ fixes the energy levels $\varepsilon_i$ and degeneracies $g_i$. At a given moment each particle is in some energy level, and the set of numbers of particles in the levels $\{N_0, N_1, N_2, \dots\}$ is an energy distribution of the system (a distribution for short, denoted $D$). Every distribution must satisfy

$$
\sum_i N_i = N, \qquad \sum_i N_i\varepsilon_i = U.
\tag{10.3}
$$

The number of microstates $t_D$ realizing a distribution $D$ is computed in two steps. First decide which particles are in which level: dividing $N$ distinguishable particles into groups of sizes $N_0, N_1, \dots$ can be done in $N!/\prod_i N_i!$ ways. Then each of the $N_i$ particles in level $i$ chooses one of the $g_i$ quantum states of that level, giving $g_i^{N_i}$ ways. Hence

$$
t_D = N!\prod_i\frac{g_i^{N_i}}{N_i!} \qquad (\text{localized particles}).
\tag{10.4}
$$
The total number of microstates of the system is the sum over all distributions satisfying Eq. (10.3):

$$
\Omega = \sum_D t_D.
$$
$\Omega$ is the **thermodynamic probability** of the macrostate $(N, V, U)$ ([5.2.4 Definition 4.7.2](/5.2.4#def-4.7.2)).

### 10.2.3. Number of Microstates of a System of Nonlocalized Particles

The particles of a nonlocalized system are indistinguishable, so "which particles are in level $i$" no longer has meaning; we only need to count the ways of distributing $N_i$ identical particles among the $g_i$ quantum states. This depends on whether the particles are bosons or fermions ([5.5.4](/5.5.4#sec-4.3.2)):

- **Bosons**: any number of particles may occupy each quantum state. Placing $N_i$ identical balls into $g_i$ boxes is equivalent to arranging $N_i$ balls and $g_i - 1$ dividers in a row, which can be done in $\frac{(N_i + g_i - 1)!}{N_i!\,(g_i - 1)!}$ ways;
- **Fermions**: by the **Pauli exclusion principle**, each quantum state holds at most one particle, giving $\binom{g_i}{N_i} = \frac{g_i!}{N_i!\,(g_i - N_i)!}$ ways.

Finding the most probable distribution for these two kinds of counting gives the **Bose–Einstein distribution** and the **Fermi–Dirac distribution**, respectively. When each level has far more quantum states than particles, $g_i \gg N_i$,

$$
\frac{(N_i + g_i - 1)!}{(g_i - 1)!} = g_i(g_i + 1)\cdots(g_i + N_i - 1) \approx g_i^{N_i}, \qquad \frac{g_i!}{(g_i - N_i)!} = g_i(g_i - 1)\cdots(g_i - N_i + 1) \approx g_i^{N_i},
$$
and both statistics give the same result:

$$
t_D = \prod_i\frac{g_i^{N_i}}{N_i!} \qquad (\text{nonlocalized particles},\ g_i \gg N_i).
\tag{10.5}
$$
This is exactly Eq. (10.4) for localized particles divided by $N!$. "Dividing by $N!$" is often called the "correction for identical particles"; the derivation above shows where it comes from and when it applies: the particles are indistinguishable, and almost no two particles are in the same quantum state. By Example 10.1.1, at ordinary temperatures the number of accessible quantum states of a gas exceeds the number of molecules by many orders of magnitude, so the condition is well satisfied (a quantitative check is given in [6.3.11](/6.3.11#sec-11.2)); it fails for an electron gas, liquid helium or an ultracold atomic gas at low temperature, which must be treated by quantum statistics.

### 10.2.4. The Equal Probability Principle and the Most Probable Distribution

Are all the microstates in $\Omega$ equally likely? The basic postulate of statistical thermodynamics is the **principle of equal a priori probabilities** ([5.2.4 Property 4.7.1](/5.2.4#pty-4.7.1)): when an isolated system with given $N$, $V$, $U$ is in equilibrium, every possible microstate occurs with probability $1/\Omega$. The probability of distribution $D$ is then $t_D/\Omega$.

**Definition 10.2.1** The distribution with the largest number of microstates $t_D$ under the constraints (10.3) is called the **most probable distribution**; its number of microstates is denoted $t_{\max}$.

Boltzmann further assumed that for sufficiently large $N$ the equilibrium state is the most probable distribution, so that $t_{\max}$ can replace $\Omega$. This "assumption" can in fact be proved. Let the number of distributions satisfying the constraints be $n_D$. Then

$$
t_{\max} \le \Omega = \sum_D t_D \le n_D\,t_{\max}, \qquad\text{that is,}\qquad \ln t_{\max} \le \ln\Omega \le \ln t_{\max} + \ln n_D.
$$
If $k$ levels are actually occupied, each $N_i$ can take only the values $0, 1, \dots, N$, so $n_D \le (N + 1)^k$ and $\ln n_D \le k\ln(N + 1)$ grows only logarithmically with $N$; by Stirling's approximation, $\ln t_{\max}$ is proportional to $N$. Therefore

$$
\ln\Omega = \ln t_{\max}\left[1 + O\!\left(\frac{\ln N}{N}\right)\right],
\tag{10.6}
$$
and for $N \sim 10^{23}$ the two are indistinguishable by any measurement. Entropy depends only on $\ln\Omega$, so the most probable distribution alone suffices for computing it: $S = k_{\mathrm{B}}\ln\Omega \approx k_{\mathrm{B}}\ln t_{\max}$.

More intuitively, expand $\ln t_D$ about the most probable distribution $N_i^*$ to second order ($\partial^2\ln t_D/\partial N_i^2 = -1/N_i$):

$$
t_D \approx t_{\max}\exp\left[-\sum_i\frac{(N_i - N_i^*)^2}{2N_i^*}\right]:
$$
the deviation of the number of particles in each level from its most probable value approximately follows a **normal distribution** with variance $N_i^*$, and the relative **fluctuation** is $\Delta N_i/N_i^* \sim (N_i^*)^{-1/2}$. For $N_i^* \sim 10^{20}$ the relative fluctuation is only $10^{-10}$: almost all microstates belong to distributions that cannot be distinguished from the most probable one. This is a manifestation of the **law of large numbers** in statistical thermodynamics.

The figure below illustrates this with a small system that can be counted exactly: $N$ distinguishable particles are distributed among three nondegenerate levels of energy $0$, $\varepsilon$ and $2\varepsilon$, with total energy $U = N\varepsilon/2$. A distribution is determined by $N_2$ ($N_1 = U/\varepsilon - 2N_2$, $N_0 = N - N_1 - N_2$), and $t_D$ is computed exactly from Eq. (10.4). As $N$ grows, $t_D/\Omega$ rapidly concentrates at the position given by the Boltzmann distribution of Section 10.3, and $\ln t_{\max}/\ln\Omega$ tends to 1.

![Exact counting for N distinguishable particles on three equally spaced levels (U = Nε/2). Left: the fraction of all microstates contained in each distribution, plotted against N₂/N; as N increases from 40 to 40000 it concentrates rapidly at N₂/N = 0.116 given by the Boltzmann distribution (dashed line). Right: ln t_max / ln Ω tends to 1 as N increases](./plots/three-level-distributions.py)

## 10.3. The Boltzmann Distribution

### 10.3.1. Finding the Most Probable Distribution

Finding the most probable distribution means maximizing $t_D$ under the two constraints (10.3). This is a **constrained extremum** problem, solved by the **method of Lagrange multipliers** ([2.2.11](/2.2.11#sec-11.6)).

**Theorem 10.3.1 (Boltzmann distribution)** For a system of independent, localized particles, and for a system of independent, nonlocalized particles satisfying $g_i \gg N_i$, the most probable distribution at given $N$, $V$, $U$ is

$$
N_i^* = \frac{N}{q}\,g_i\,\mathrm{e}^{-\beta\varepsilon_i}, \qquad q = \sum_i g_i\,\mathrm{e}^{-\beta\varepsilon_i},
\tag{10.7}
$$
where $\beta$ is a constant determined by the total energy $U$ (Section 10.3.2 proves $\beta = 1/(k_{\mathrm{B}}T)$).

**Proof** Take the logarithm of Eq. (10.4) and apply Stirling's approximation to $N!$ and to each $N_i!$:

$$
\ln t_D = \ln N! + \sum_i\left(N_i\ln g_i - \ln N_i!\right) \approx \ln N! + \sum_i\left(N_i\ln g_i - N_i\ln N_i + N_i\right).
$$
$\ln t_D$ and $t_D$ attain their maximum together. Form the Lagrange function

$$
L = \ln t_D - \alpha\left(\sum_i N_i - N\right) - \beta\left(\sum_i N_i\varepsilon_i - U\right),
$$
treat the $N_i$ as independent variables, and set $\partial L/\partial N_i = 0$:

$$
\ln g_i - \ln N_i - \alpha - \beta\varepsilon_i = 0, \qquad\text{that is,}\qquad N_i^* = g_i\,\mathrm{e}^{-\alpha}\,\mathrm{e}^{-\beta\varepsilon_i}.
$$
Substituting into $\sum_i N_i = N$ gives $\mathrm{e}^{-\alpha} = N/\sum_i g_i\mathrm{e}^{-\beta\varepsilon_i} = N/q$, which is Eq. (10.7); $\beta$ is determined by the second constraint $\sum_i N_i^*\varepsilon_i = U$. Moreover $\partial^2\ln t_D/\partial N_i\partial N_j = -\delta_{ij}/N_i < 0$, so $\ln t_D$ is strictly concave and the stationary point is the unique maximum. For nonlocalized particles, the logarithm of Eq. (10.5) differs from that for localized particles only by the constant $\ln N!$, so the derivation and result are identical. $\square$

**Remark 10.3.1** The derivation applies Stirling's approximation to every $N_i$, which requires every level to hold a large number of particles. For a gas, the number of molecules in a single translational level is not large ($g_i \gg N_i$ says precisely that on average there is far less than one molecule per quantum state). The rigorous procedure is to group the many levels with nearby energies into "level groups", within which both the numbers of quantum states and of particles are large, and to repeat the derivation for the groups; the result is unchanged. Alternatively one can use Gibbs's canonical ensemble (Section 10.4.2), which does not need the most probable distribution at all.

### 10.3.2. Determination of β

The physical meaning of $\beta$ is fixed by the entropy. For localized particles, substitute the most probable distribution (10.7) into $\ln t_{\max} = N\ln N + \sum_i N_i^*\ln(g_i/N_i^*)$ (Stirling's approximation), noting that $\ln(g_i/N_i^*) = \ln(q/N) + \beta\varepsilon_i$:

$$
\ln t_{\max} = N\ln N + N\ln\frac{q}{N} + \beta U = N\ln q + \beta U.
$$
From $S = k_{\mathrm{B}}\ln\Omega \approx k_{\mathrm{B}}\ln t_{\max}$,

$$
S = k_{\mathrm{B}}\left[N\ln q(\beta) + \beta U\right].
$$
At fixed $N$ and $V$ the levels $\varepsilon_i$ do not change, and $S$ varies only through $U$ and $\beta(U)$:

$$
\mathrm{d}S = k_{\mathrm{B}}\left[N\frac{\mathrm{d}\ln q}{\mathrm{d}\beta}\,\mathrm{d}\beta + U\,\mathrm{d}\beta + \beta\,\mathrm{d}U\right].
$$
Since $N\frac{\mathrm{d}\ln q}{\mathrm{d}\beta} = -\frac{N}{q}\sum_i g_i\varepsilon_i\mathrm{e}^{-\beta\varepsilon_i} = -\sum_i N_i^*\varepsilon_i = -U$, the first two terms cancel and $\left(\frac{\partial S}{\partial U}\right)_{N,V} = k_{\mathrm{B}}\beta$. On the other hand, by the **fundamental equation of thermodynamics** $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ ([6.3.3 Theorem 3.2.1](/6.3.3#thm-3.2.1)), $\left(\frac{\partial S}{\partial U}\right)_V = \frac{1}{T}$. Comparing the two,

$$
\beta = \frac{1}{k_{\mathrm{B}}T}.
\tag{10.8}
$$
For nonlocalized particles $\ln t_{\max}$ has only one extra term independent of $U$ (Section 10.4.1), and the conclusion is the same.

Some textbooks write the Lagrange multiplier term as $+\beta(\sum_i N_i\varepsilon_i - U)$, obtaining $N_i \propto g_i\mathrm{e}^{\beta\varepsilon_i}$ and $\beta = -1/(k_{\mathrm{B}}T)$; this site uses the common convention of current textbooks, $\beta = 1/(k_{\mathrm{B}}T) > 0$. The $T$ so defined is the thermodynamic temperature: $\beta$ is a Lagrange multiplier, and when two systems that can exchange energy reach equilibrium their $\beta$ must be equal, which corresponds precisely to the equality of temperatures in thermal equilibrium (the **zeroth law of thermodynamics**).

Substituting back into Eq. (10.7) gives the **Boltzmann distribution** in terms of energy levels:

$$
\frac{N_i^*}{N} = \frac{g_i\,\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}}{q}, \qquad \frac{N_i^*}{N_j^*} = \frac{g_i}{g_j}\,\mathrm{e}^{-(\varepsilon_i - \varepsilon_j)/(k_{\mathrm{B}}T)}.
\tag{10.9}
$$
The **Boltzmann factor** $\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}$ shows that levels with energy much higher than $k_{\mathrm{B}}T$ are hardly populated, while the degeneracy $g_i$ gives the weight of the number of states in a level. Theorem 1.7.1 of the physics part ([5.2.1](/5.2.1#thm-1.7.1)) is its form for classical continuous energies: for molecules at height $h$ in a gravitational field, $\varepsilon = mgh$, which gives the isothermal barometric formula $p = p_0\mathrm{e}^{-mgh/(k_{\mathrm{B}}T)}$.

### 10.3.3. The Molecular Partition Function and Its Probabilistic Meaning

**Definition 10.3.1** The sum of the Boltzmann factors of all energy levels of a single molecule, weighted by degeneracy,

$$
q = \sum_i g_i\,\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)} = \sum_{s}\mathrm{e}^{-\varepsilon_s/(k_{\mathrm{B}}T)}
\tag{10.10}
$$
is called the **molecular partition function**. The first sum runs over energy levels, the second over all quantum states $s$ of the molecule; the two are equal.

- $q$ is dimensionless and is computed from the energy levels of the molecule. It depends on $T$, and through the levels (for example the translational levels (10.1)) on $V$, but not on $N$: $q = q(T, V)$.
- $q$ is "the number of thermally accessible quantum states": with the ground-state energy taken as zero, $q \to g_0$ as $T \to 0$ and only the ground state is populated; as $T$ rises, more and more excited states come within reach of $k_{\mathrm{B}}T$ and $q$ increases; as $T \to \infty$, $q$ approaches the total number of quantum states.
- The name of $q$ comes from Eq. (10.9): it is the normalization factor for "partitioning" $N$ molecules among the levels.

In the language of probability, the probability that a randomly chosen molecule is in level $i$ is $P_i = g_i\mathrm{e}^{-\beta\varepsilon_i}/q$, and $q$ is the normalization constant of this probability distribution. The mean and variance of the molecular energy can both be obtained by differentiating $\ln q$ with respect to $\beta$:

$$
\langle\varepsilon\rangle = \sum_i P_i\varepsilon_i = -\frac{\partial\ln q}{\partial\beta} = k_{\mathrm{B}}T^2\,\frac{\partial\ln q}{\partial T}, \qquad \sigma_\varepsilon^2 = \langle\varepsilon^2\rangle - \langle\varepsilon\rangle^2 = \frac{\partial^2\ln q}{\partial\beta^2} = k_{\mathrm{B}}T^2\,\frac{\partial\langle\varepsilon\rangle}{\partial T},
\tag{10.11}
$$
with all derivatives taken at constant $V$. The second expression shows that the energy fluctuation is proportional to the heat capacity: the larger the heat capacity, the larger the energy fluctuation. The total energy of $N$ independent molecules is $U = N\langle\varepsilon\rangle$ with variance $N\sigma_\varepsilon^2$, so the relative fluctuation is $\propto N^{-1/2}$, consistent with Section 10.2.4.

**Example 10.3.1 (Two-level system)** Let a molecule have only two levels: a ground state of energy $0$ and degeneracy $g_0$, and an excited state of energy $\varepsilon$ and degeneracy $g_1$. Then $q = g_0 + g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$, and the fraction of molecules in the excited state and the mean energy per molecule are

$$
\frac{N_1}{N} = \frac{g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}}{g_0 + g_1\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}}, \qquad \langle\varepsilon\rangle = \varepsilon\,\frac{N_1}{N}.
$$
As $T \to \infty$, $N_1/N \to g_1/(g_0 + g_1)$ but never exceeds it: thermal equilibrium cannot produce a population inversion (a laser requires nonequilibrium pumping, [5.5.5](/5.5.5#sec-5.2.3)). From Eq. (10.11) the heat capacity is $C_V = N\,\mathrm{d}\langle\varepsilon\rangle/\mathrm{d}T = Nk_{\mathrm{B}}(\varepsilon/k_{\mathrm{B}}T)^2\,P_0P_1$. It has a peak at $k_{\mathrm{B}}T \approx 0.42\,\varepsilon$ (for $g_0 = g_1$): at too low a temperature the excitation cannot occur, while at too high a temperature the two levels are nearly saturated and absorbing more heat cannot change the populations. This heat-capacity peak is called the *Schottky anomaly* and is observed in the low-temperature heat capacity of paramagnetic salts ([5.3.8](/5.3.8)).

![Two-level system (g₁/g₀ = 1 and 3). Left: fraction of molecules in the excited state, with the dotted line showing the high-temperature limit g₁/(g₀ + g₁). Right: heat capacity per molecule, the Schottky anomaly](./plots/two-level-system.py)

The Boltzmann distribution for two levels has many uses. In nuclear magnetic resonance, the proton spin level splitting $h\nu$ at $400\,\mathrm{MHz}$ is only $6.4\times10^{-5}$ of $k_{\mathrm{B}}T$ ($298\,\mathrm{K}$), and the population difference between the upper and lower levels is only about $3\times10^{-5}$, which is the fundamental reason for the low sensitivity of NMR. In biophysics, the opening and closing of ion channels and the folded and unfolded states of proteins are commonly described by two-state models: the open probability is $P_{\mathrm{open}} = 1/[1 + \mathrm{e}^{\Delta G/(k_{\mathrm{B}}T)}]$, where $\Delta G$ is the difference in Gibbs free energy between the open and closed states (the free energy rather than the energy is used here because each "state" itself contains a large number of microstates).

## 10.4. Partition Functions and Thermodynamic Functions

### 10.4.1. Entropy

From $S = k_{\mathrm{B}}\ln t_{\max}$ and the calculation of Section 10.3.2, the entropy of a system of localized particles is

$$
S = Nk_{\mathrm{B}}\ln q + \frac{U}{T} \qquad (\text{localized particles}).
\tag{10.12}
$$
For nonlocalized particles, use $t_D$ of Eq. (10.5): $\ln t_{\max} = \sum_i\left[N_i^*\ln(g_i/N_i^*) + N_i^*\right] = N\ln(q/N) + \beta U + N$, and then, since $N\ln N - N = \ln N!$ by Stirling's approximation,

$$
S = k_{\mathrm{B}}\ln\frac{q^N}{N!} + \frac{U}{T} \qquad (\text{nonlocalized particles}).
\tag{10.13}
$$
The two differ by $k_{\mathrm{B}}\ln N!$.

### 10.4.2. The System Partition Function

From $A = U - TS$, for localized particles $A = -Nk_{\mathrm{B}}T\ln q = -k_{\mathrm{B}}T\ln q^N$, and for nonlocalized particles $A = -k_{\mathrm{B}}T\ln(q^N/N!)$. The two cases can be written uniformly as $A = -k_{\mathrm{B}}T\ln Z$, where $Z$ has a more general meaning.

**Definition 10.4.1** Let $s$ label the microstates of a system with given $N$ and $V$, with energies $E_s$. Then

$$
Z = \sum_s \mathrm{e}^{-E_s/(k_{\mathrm{B}}T)}
$$
is called the **partition function** (canonical partition function) of the system.

Gibbs's canonical ensemble theory shows that a system in contact with a heat reservoir at temperature $T$ is in microstate $s$ with probability $\mathrm{e}^{-E_s/(k_{\mathrm{B}}T)}/Z$ (this is just "the probability of a microstate" mentioned in the last sentence of [5.2.1 Theorem 1.7.1](/5.2.1#thm-1.7.1)), and that $A = -k_{\mathrm{B}}T\ln Z$ holds for any system, including systems of interacting particles. For independent systems, the system partition function can be expressed through the molecular partition function:

**Theorem 10.4.1** For a system of $N$ independent particles,

$$
Z = q^N \quad (\text{localized particles}), \qquad Z = \frac{q^N}{N!} \quad (\text{nonlocalized particles},\ g_i \gg N_i).
\tag{10.14}
$$

**Proof** A microstate of an independent system is determined by the quantum states $(s_1, s_2, \dots, s_N)$ of the particles, with $E_s = \varepsilon_{s_1} + \cdots + \varepsilon_{s_N}$. When the particles are distinguishable, each $s_k$ independently runs over all single-particle quantum states, and the exponential turns the sum into a product:

$$
Z = \sum_{s_1}\cdots\sum_{s_N}\mathrm{e}^{-\beta(\varepsilon_{s_1} + \cdots + \varepsilon_{s_N})} = \left(\sum_{s}\mathrm{e}^{-\beta\varepsilon_s}\right)^N = q^N.
$$
When the particles are indistinguishable, each arrangement of $N$ particles in $N$ mutually different quantum states is counted $N!$ times in the above (all permutations of the particle labels). For $g_i \gg N_i$ the terms in which two particles share a quantum state form a negligible fraction, so $Z = q^N/N!$. $\square$

**Remark 10.4.1** The symbol $Z$ denotes the **compressibility factor** in [6.3.1](/6.3.1) and [6.3.4](/6.3.4) and the system partition function in this chapter and the next; the two never appear together. In physics, [5.2.1](/5.2.1#sec-1.7.2) also writes the sum of Boltzmann factors of single-particle states as $Z$; in chemistry it is customary to use $q$ for the molecular partition function and $Z$ (or $Q$) for the system partition function, and this site uses $q$ and $Z$ ($Q$ is already used for heat and the reaction quotient).

Given $A(T, V, N) = -k_{\mathrm{B}}T\ln Z$, all other thermodynamic functions follow from $\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V$ ([6.3.3 Theorem 3.2.1](/6.3.3#thm-3.2.1)), because $A$ with natural variables $T$, $V$ is a **characteristic function** ([6.3.3 Definition 3.2.1](/6.3.3#def-3.2.1)):

| Function | In terms of $Z$ | Localized ($Z = q^N$) | Nonlocalized ($Z = q^N/N!$) |
|---|---|---|---|
| $A$ | $-k_{\mathrm{B}}T\ln Z$ | $-Nk_{\mathrm{B}}T\ln q$ | $-k_{\mathrm{B}}T\ln\dfrac{q^N}{N!}$ |
| $S$ | $k_{\mathrm{B}}\ln Z + k_{\mathrm{B}}T\left(\dfrac{\partial\ln Z}{\partial T}\right)_V$ | $Nk_{\mathrm{B}}\ln q + \dfrac{U}{T}$ | $k_{\mathrm{B}}\ln\dfrac{q^N}{N!} + \dfrac{U}{T}$ |
| $U$ | $k_{\mathrm{B}}T^2\left(\dfrac{\partial\ln Z}{\partial T}\right)_V$ | $Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V$ | same |
| $p$ | $k_{\mathrm{B}}T\left(\dfrac{\partial\ln Z}{\partial V}\right)_T$ | $Nk_{\mathrm{B}}T\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | same |
| $H = U + pV$ | — | $Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | same |
| $G = A + pV$ | — | $-Nk_{\mathrm{B}}T\ln q + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ | $-k_{\mathrm{B}}T\ln\dfrac{q^N}{N!} + Nk_{\mathrm{B}}TV\left(\dfrac{\partial\ln q}{\partial V}\right)_T$ |
| $C_V$ | $\left(\dfrac{\partial U}{\partial T}\right)_V$ | $\dfrac{\partial}{\partial T}\left[Nk_{\mathrm{B}}T^2\left(\dfrac{\partial\ln q}{\partial T}\right)_V\right]_V$ | same |

(All partial derivatives in the table are taken at constant $N$.) $U$, $H$, $p$ and $C_V$ contain only derivatives of $\ln q$, so their expressions are the same for localized and nonlocalized particles; $S$, $A$ and $G$ contain $\ln q$ itself, and for nonlocalized particles there is an extra constant term of the form $-k_{\mathrm{B}}\ln N!$. The expression for $U$ agrees with $U = N\langle\varepsilon\rangle$ from Eq. (10.11).

**Example 10.4.1 (Equation of state of an ideal gas)** Among the molecular energy levels only the translational levels depend on the volume; by Eq. (10.1) the translational partition function is proportional to $V$ ([6.3.11](/6.3.11#sec-11.2)), and the partition functions of the internal motions are independent of $V$, so for any ideal gas $q = V f(T)$. Then

$$
p = Nk_{\mathrm{B}}T\left(\frac{\partial\ln q}{\partial V}\right)_T = \frac{Nk_{\mathrm{B}}T}{V}, \qquad pV = Nk_{\mathrm{B}}T = nRT,
$$
independently of the internal structure of the molecule. Likewise, the factor $V$ in $U = Nk_{\mathrm{B}}T^2(\partial\ln q/\partial T)_V$ disappears on differentiation, so $U$ is a function of $T$ only: this is the microscopic explanation of the result of Joule's experiment ([6.3.1](/6.3.1)). From $pV = Nk_{\mathrm{B}}T$ and Stirling's approximation, the Gibbs free energy of an ideal gas is

$$
G = A + pV = -k_{\mathrm{B}}T\left(N\ln q - N\ln N + N\right) + Nk_{\mathrm{B}}T = -Nk_{\mathrm{B}}T\ln\frac{q}{N},
\tag{10.15}
$$
so the Gibbs free energy per molecule, that is, the **chemical potential**, is $\mu = -k_{\mathrm{B}}T\ln(q/N)$. Its use in computing equilibrium constants is given in [6.3.11](/6.3.11#sec-11.7).

### 10.4.3. Choice of the Energy Zero

Energy has only relative meaning. The partition function may be measured from the ground-state energy $\varepsilon_0$ of the molecule or from some other zero. Let $q^{(0)} = \sum_i g_i\mathrm{e}^{-(\varepsilon_i - \varepsilon_0)/(k_{\mathrm{B}}T)}$ be the partition function with the ground state as zero. Then

$$
q = \mathrm{e}^{-\varepsilon_0/(k_{\mathrm{B}}T)}\,q^{(0)}, \qquad \ln q = \ln q^{(0)} - \frac{\varepsilon_0}{k_{\mathrm{B}}T}.
$$
Substituting into the table above: the $T$ derivative of $\ln q$ acquires an extra $\varepsilon_0/(k_{\mathrm{B}}T^2)$ and the $V$ derivative is unchanged. Hence (with $U_0 = N\varepsilon_0$, the energy of the system at $0\,\mathrm{K}$)

$$
U = U^{(0)} + U_0, \quad H = H^{(0)} + U_0, \quad A = A^{(0)} + U_0, \quad G = G^{(0)} + U_0, \qquad S = S^{(0)}, \quad p = p^{(0)}, \quad C_V = C_V^{(0)}.
$$
In $S$ the changes $\mp N\varepsilon_0/T$ of the two terms $Nk_{\mathrm{B}}\ln q$ and $U/T$ exactly cancel. $N_i^*/N$ is also independent of the zero (numerator and denominator are multiplied by the same factor).

For a process that involves no chemical change, $U_0$ is the same in the initial and final states, so the choice of zero does not affect $\Delta U$, $\Delta H$, $\Delta A$ or $\Delta G$. In a chemical reaction the molecules of different species differ, and the energies of all species must be placed on a common zero; the difference in $U_0$ (the energy change of the reaction at $0\,\mathrm{K}$) is then a key term in the equilibrium constant ([6.3.11](/6.3.11#sec-11.7)). In the next chapter, the partition function of each mode of motion is always computed with the ground state of that mode as zero, and $U_0$ is added explicitly when needed.

## 10.5. Statistical Meaning of the Laws of Thermodynamics

### 10.5.1. Heat and Work

The internal energy of an independent system is $U = \sum_i N_i\varepsilon_i$, and its total differential

$$
\mathrm{d}U = \sum_i\varepsilon_i\,\mathrm{d}N_i + \sum_i N_i\,\mathrm{d}\varepsilon_i
\tag{10.16}
$$
has two parts: the energy change caused by redistributing particles among the levels while the levels stay fixed, and the energy change caused by the shifting of the levels themselves while the distribution stays fixed. For a **reversible process** in a closed system, these are heat and work, respectively:

- The levels change only with an external parameter (here the volume), $\sum_i N_i\,\mathrm{d}\varepsilon_i = \left(\sum_i N_i\frac{\partial\varepsilon_i}{\partial V}\right)\mathrm{d}V = -p\,\mathrm{d}V = \delta W_{\mathrm{r}}$, where $p = -\sum_i N_i\,\partial\varepsilon_i/\partial V$. (It is easily verified that this agrees with $p = Nk_{\mathrm{B}}T(\partial\ln q/\partial V)_T$ in the table.)
- From $S = k_{\mathrm{B}}\ln t_{\max}$ and $\partial\ln t_D/\partial N_i = \ln(g_i/N_i) = \alpha + \beta\varepsilon_i$ (Section 10.3.1), for $\sum_i\mathrm{d}N_i = 0$ we have $\mathrm{d}S = k_{\mathrm{B}}\sum_i(\alpha + \beta\varepsilon_i)\,\mathrm{d}N_i = \frac{1}{T}\sum_i\varepsilon_i\,\mathrm{d}N_i$, so $\sum_i\varepsilon_i\,\mathrm{d}N_i = T\,\mathrm{d}S = \delta Q_{\mathrm{r}}$.

Eq. (10.16) is thus the microscopic form of the **first law of thermodynamics** $\mathrm{d}U = \delta Q + \delta W$: heat is the energy transferred by redistributing particles among levels with the levels fixed, and work is the energy transferred by the shifting of the levels with the distribution fixed.

**Example 10.5.1 (Reversible adiabatic expansion)** Consider a monatomic ideal gas whose volume changes adiabatically and reversibly: $\delta Q_{\mathrm{r}} = 0$, the numbers of molecules in the levels do not change, and the translational levels (10.1) shift together as $V^{-2/3}$. The distribution must remain of Boltzmann form $N_i/N \propto g_i\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}$; since $N_i$ is fixed and $\varepsilon_i \propto V^{-2/3}$, this is possible only if $\varepsilon_i/(k_{\mathrm{B}}T)$ stays constant, so $T \propto V^{-2/3}$, that is, $TV^{2/3} = \text{constant}$. This is exactly the equation $TV^{\gamma - 1} = \text{constant}$ of the **adiabatic process** with $\gamma = 5/3$ ([6.3.1](/6.3.1)), obtained here without using the numerical value of the heat capacity.

### 10.5.2. Entropy, Spontaneous Processes and the Third Law

The **Boltzmann entropy formula** $S = k_{\mathrm{B}}\ln\Omega$ says that entropy measures the number of microstates of a system. A spontaneous process in an isolated system is, microscopically, the removal of a constraint (a partition, the energy barrier of a reaction, a phase boundary) so that the set of microstates accessible to the system is enlarged: after the constraint is removed the original microstates remain accessible and new ones are added, so $\Omega_2 \ge \Omega_1$ and $\Delta S \ge 0$. The system "wanders" through the enlarged set of microstates and is almost always in those belonging to the most probable distribution, which shows up macroscopically as an approach to a new equilibrium state; this is the statistical meaning of the **principle of entropy increase**. For example, for the expansion of an ideal gas into a vacuum, $q \propto V$, and by Eq. (10.13) $\Delta S = Nk_{\mathrm{B}}\ln(V_2/V_1)$, the same as the counting result of [5.2.4 Example 4.8.1](/5.2.4#ex-4.8.1).

As $T \to 0$ the Boltzmann factor drives all particles into the ground state. If the ground state has degeneracy $g_0$, then for localized particles there is only one distribution $N_0 = N$, Eq. (10.4) gives $\Omega = g_0^N$, and $S(0\,\mathrm{K}) = Nk_{\mathrm{B}}\ln g_0$. In a **perfect crystal** the ground state of every particle is unique, $g_0 = 1$, and $S(0\,\mathrm{K}) = 0$; this is the statistical interpretation of the **third law of thermodynamics** ([6.3.2 Theorem 2.4.2](/6.3.2#thm-2.4.2)). If the orientations of the molecules in a crystal are "frozen" in a disordered arrangement during solidification, the number of microstates at $0\,\mathrm{K}$ is still greater than 1, and the crystal has a **residual entropy** ([6.3.11](/6.3.11#sec-11.6.3)).

### 10.5.3. Discussion: Entropy of Crystals and Gases

By Eqs. (10.4) and (10.5), for the same $q$ we have $\Omega_{\text{localized}}/\Omega_{\text{nonlocalized}} = N!$, so the entropy of a system of localized particles is greater by $k_{\mathrm{B}}\ln N!$. On the other hand, the entropy of the crystal of a substance is always much smaller than that of its vapor ($S_{\mathrm{m}}(\mathrm{s}) < S_{\mathrm{m}}(\mathrm{l}) < S_{\mathrm{m}}(\mathrm{g})$). There is no contradiction: the comparison was made "for the same $q$", while the $q$ of a crystal and that of a gas are completely different.

- A crystal is a system of interacting particles; the interactions bind each atom near its lattice site, and when it is treated as a system of localized particles each atom has only 3 vibrational modes, with a vibrational partition function of order $1$–$10$.
- In a gas the molecules move freely throughout the container and the translational partition function is enormous: for $\ce{N2}$ at $298\,\mathrm{K}$ and $p^\circ$, $q_{\mathrm{t}}/N_{\mathrm{A}} \approx 6\times10^6$ ([6.3.11](/6.3.11#sec-11.2)), and rotation contributes further.
- A liquid lies between the two: the molecules can move and rotate over a larger range, and more energy levels are accessible than in the crystal.

The factor $N!$ arises from the indistinguishability of the particles and merely corrects the huge $q^N$ of a gas to $(q/N)^N\mathrm{e}^N$; the decisive factor is that the denser the energy levels and the more quantum states are accessible (the larger $q$), the larger the entropy.

## Summary

| Quantity | Localized particles | Nonlocalized particles ($g_i \gg N_i$) |
|---|---|---|
| Number of microstates of a distribution $t_D$ | $N!\prod_i g_i^{N_i}/N_i!$ | $\prod_i g_i^{N_i}/N_i!$ |
| Most probable distribution | $N_i^*/N = g_i\mathrm{e}^{-\varepsilon_i/(k_{\mathrm{B}}T)}/q$ | same |
| System partition function $Z$ | $q^N$ | $q^N/N!$ |
| $S$ | $Nk_{\mathrm{B}}\ln q + U/T$ | $k_{\mathrm{B}}\ln(q^N/N!) + U/T$ |
| $A$ | $-Nk_{\mathrm{B}}T\ln q$ | $-k_{\mathrm{B}}T\ln(q^N/N!)$ |
| $U$, $p$, $H$, $C_V$ | given by derivatives of $\ln q$, the same for both | |

- The basic postulate of statistical thermodynamics is the principle of equal a priori probabilities; for large $N$ the relative error of $\ln\Omega = \ln t_{\max}$ is $O(\ln N/N)$, so only the most probable distribution is needed.
- The Boltzmann distribution is found by the method of Lagrange multipliers, and the multiplier $\beta = 1/(k_{\mathrm{B}}T)$ is determined by $(\partial S/\partial U)_V = 1/T$.
- The partition function is the bridge between macroscopic and molecular properties: molecular energy levels → $q$ → $Z$ → $A = -k_{\mathrm{B}}T\ln Z$ → all thermodynamic functions.
- Changing the energy zero only shifts $U$, $H$, $A$ and $G$ by $U_0$ and does not change $S$, $p$ or $C_V$.

## Questions

1. Which of the following are characteristics of Boltzmann statistics? (A) It treats a system with given $N$, $V$, $U$; (B) the energy of the system satisfies $\sum_i N_i\varepsilon_i = U$; (C) the number of particles in each quantum state is limited by the Pauli exclusion principle; (D) all possible microstates occur with equal probability.
   Answer: A, B and D. C is a characteristic of Fermi–Dirac statistics; Boltzmann statistics is the limit $g_i \gg N_i$, in which the restriction of the Pauli principle plays no role.
2. If the following functions are computed with $q$ and with $q^{(0)}$, which results differ: $U$, $H$, $S$, $A$, $G$, $p$, $C_V$?
   Answer: $U$, $H$, $A$ and $G$ differ by $U_0 = N\varepsilon_0$; $S$, $p$ and $C_V$ are the same.
3. Using the statistical meaning of entropy, determine the sign of the entropy change in each process: (1) water vapor condenses to water; (2) $\ce{CaCO3}$ decomposes on heating; (3) ethylene polymerizes to polyethylene; (4) a gas adsorbs on a catalyst surface; (5) a phospholipid membrane changes from the gel state to the fluid liquid-crystalline state.
   Answer: (1) the molecules lose translation throughout the container, $\Delta S < 0$; (2) a gas is formed, and the number of molecules and of translational degrees of freedom increases, $\Delta S > 0$; (3) the number of molecules decreases, $\Delta S < 0$; (4) the molecules are confined to the surface and translation decreases, $\Delta S < 0$; (5) the hydrocarbon chains of the lipid molecules change from ordered to disordered, and lateral motion in the plane of the membrane and rotation of chain segments increase, $\Delta S > 0$ (this transition is endothermic and entropy-driven).
4. Why is the statement "statistical thermodynamics can compute the absolute entropy of a system with given $N$, $V$, $U$" not entirely accurate?
   Answer: $S = k_{\mathrm{B}}\ln\Omega$ in principle gives the absolute value of the entropy, but in practice the calculation always omits degrees of freedom that are "frozen" in the temperature range considered and do not change in chemical and physical processes, the most typical being the nuclear spin ([6.3.11](/6.3.11#sec-11.5)). The statistical entropy usually quoted is therefore also a conventional entropy: it follows the same convention as the calorimetric entropy with the perfect crystal at $0\,\mathrm{K}$ as zero, so the two can be compared directly, and their difference is the residual entropy.
