---
title: Entropy, Free Energy and the Statistical Physics of Life
description: Counting microstates and the sharpness of the most probable macrostate; the Boltzmann distribution derived from the principle of maximum entropy; partition function, free energy and generalized forces; energy against entropy in hairpin melting, the thermal spring and equipartition (Metropolis sampling), osmotic pressure, entropic forces and the hydrophobic effect; information and thermodynamics (Maxwell's demon, the Szilard engine, Landauer's principle); and the entropy balance of open living systems, from a cell to the Earth.
---

Molecules in a cell are never still. Every degree of freedom is shaken by collisions with water, and every bond weaker than a few times the **thermal energy** is constantly made and broken. The order of living matter therefore has to be understood statistically: we cannot follow each molecule, but we can say how probable each arrangement is. This chapter develops the statistical physics needed for the rest of the course. It starts from counting (2.1), derives the Boltzmann distribution from the principle of maximum entropy and introduces the partition function and free energy (2.2), and then uses the competition between energy and entropy to explain the melting of hairpins, the fluctuations of a spring, osmotic pressure, entropic forces and the hydrophobic effect (2.3). It ends with two topics that connect thermodynamics to the essence of life: the physical cost of information (2.4) and the entropy balance of open systems that stay far from equilibrium (2.5). The thermodynamics of [5.2](/5.2) and the statistical thermodynamics of [6.3.10](/6.3.10), [6.3.11](/6.3.11) and [6.3.18](/6.3.18) are assumed; the emphasis here is on the models and numbers that biological questions require. The chemical potential, binding and rates follow in [7.6.3](/7.6.3).

## 2.1. Microstates, Macrostates and Counting

### 2.1.1. Counting Configurations

A **microstate** is a complete specification of a system: the position of every molecule, the conformation of every chain. A **macrostate** is what we observe or care about: the number of molecules in the left half of a box, the number of proteins bound to DNA, whether a protein is folded. Each macrostate $I$ comprises a number $\Omega_I$ of microstates, its multiplicity.

Two examples recur. First, $N$ molecules in a box, each independently in the left or right half: the macrostate "$N_1$ on the left" has

$$
\Omega(N_1) = \binom{N}{N_1} = \frac{N!}{N_1!\,(N - N_1)!}
$$
microstates, and $\sum_{N_1}\Omega(N_1) = 2^N$. Second, $P$ RNA polymerases bound nonspecifically to a genome with $N$ binding positions (ignoring overlaps): the number of arrangements is $\binom{N}{P}$, and if each bound polymerase has energy $\varepsilon$, the statistical weight of the macrostate "$P$ bound" is $\binom{N}{P}\mathrm{e}^{-P\varepsilon/k_{\mathrm{B}}T}$. Counting arrangements and weighting them by energy is the whole method of this chapter.

### 2.1.2. The Most Probable Macrostate

If all microstates of an isolated system are equally probable (the principle of equal a priori probabilities, [5.2.4](/5.2.4#sec-4.7.2)), the probability of a macrostate is proportional to its multiplicity. For molecules in a box, $\Omega(N_1)$ is largest at $N_1 = N/2$, and its peak narrows as $N$ grows.

**Formula 2.1.1 (Width of the Binomial Peak)** By **Stirling's approximation** $\ln N! = N\ln N - N + \frac{1}{2}\ln(2\pi N) + O(1/N)$ ([6.3.10](/6.3.10#sec-10.2.1)), the multiplicity near its maximum is a Gaussian:

$$
\frac{\Omega(N_1)}{\Omega(N/2)} \approx \exp\!\left[-\frac{(N_1 - N/2)^2}{N/2}\right], \qquad
\Omega(N/2) \approx 2^N\sqrt{\frac{2}{\pi N}}. \tag{2.1}
$$
The standard deviation of $N_1$ is $\sqrt{N}/2$, so the relative width of the peak is $1/\sqrt{N}$, the rule of [7.6.1](/7.6.1#sec-1.2.3).

For $N = 10^{24}$ the relative width is $10^{-12}$: a deviation of one part in a million from an even split would be $10^6$ standard deviations away and would never be seen. Moreover $\ln\Omega(N/2) = N\ln 2 - \frac{1}{2}\ln(\pi N/2)$ differs from the logarithm of the total number of microstates, $N\ln 2$, by about 28 out of $7\times10^{23}$: the most probable macrostate contains, on a logarithmic scale, essentially all microstates. This is why thermodynamics works for macroscopic systems, and why it must be used with care for a single protein, a few hundred molecules of a transcription factor, or one gene.

![Sharpening of the most probable macrostate for N molecules distributed between the two halves of a box. A: the multiplicity Ω(N₁) relative to its maximum, against the scaled deviation (N₁ − N/2)/(N/2), for N = 10, 100 and 10 000 (exact binomial coefficients); the relative width falls as 1/√N. B: the logarithm of the largest multiplicity, ln Ω(N/2), divided by N ln 2, the logarithm of the total number of microstates: the exact values (points) agree with Stirling's estimate N ln 2 − ½ ln(πN/2) (line), and the ratio approaches 1 (dashed) as N grows](./plots/multiplicity.py)

### 2.1.3. Boltzmann Entropy

Because multiplicities of independent subsystems multiply while thermodynamic entropies add, the entropy of a macrostate must be a logarithm of its multiplicity; this is the **Boltzmann entropy formula** $S = k_{\mathrm{B}}\ln\Omega$ ([5.2.4](/5.2.4#sec-4.8)). The second law in its statistical form follows from 2.1.2: an isolated system left to itself passes, overwhelmingly probably, into the macrostate of largest multiplicity, the **equilibrium state**, and stays there. Entropy measures how many microstates are compatible with what we know about a system, and in this sense how little we know about its microscopic state.

In thermodynamics entropy is introduced through heat: $\mathrm{d}S = \delta Q_{\mathrm{rev}}/T$ for a reversible exchange of heat at temperature $T$, and $\Delta S > \int\delta Q/T$ for an irreversible one ([5.2.4](/5.2.4#sec-4.5)). The relation "$S = Q/T$" sometimes quoted for the Clausius entropy holds only for a reversible isothermal process starting from a reference state; the general statement is the differential one, and the two definitions, by heat and by counting, agree for systems at equilibrium.

### 2.1.4. Equilibrium between Subsystems and Fluxes

Equilibrium conditions follow from maximizing the entropy of a composite system. Let an isolated system consist of two parts that can exchange a conserved extensive quantity: energy, volume (through a movable wall) or molecules (through a permeable membrane). The total entropy $S_1 + S_2$ is maximal when an exchange $\mathrm{d}X_1 = -\mathrm{d}X_2$ no longer changes it, $\partial S_1/\partial X_1 = \partial S_2/\partial X_2$. With $\partial S/\partial E = 1/T$, $\partial S/\partial V = p/T$ and $\partial S/\partial N = -\mu/T$ this gives the three conditions:

| Exchanged quantity | Equilibrium condition | Name |
|---|---|---|
| Energy | $T_1 = T_2$ | Thermal equilibrium |
| Volume | $p_1 = p_2$ | Mechanical equilibrium |
| Molecules of a species | $\mu_1 = \mu_2$ | Chemical (diffusive) equilibrium |

For each conserved extensive quantity, equilibrium equalizes the conjugate intensive one. Out of equilibrium, the second law requires $\mathrm{d}S > 0$: for particle exchange, $(\mu_2 - \mu_1)\,\mathrm{d}N_1/T > 0$, so molecules flow from high to low chemical potential, energy flows from hot to cold, and a wall moves toward lower pressure. Near equilibrium the flows are proportional to the differences that drive them,

$$
\text{flux} = \text{transport coefficient}\times\text{driving force},
$$
as in Fourier's law of heat conduction, Fick's law of diffusion (7.6.5), Ohm's law for ions through channels (7.6.30) and the flow of water through a membrane down a gradient of water potential ([7.6.3](/7.6.3#sec-3.1.4)); the general theory of such linear relations is the linear nonequilibrium thermodynamics of [6.3.18](/6.3.18#sec-18.2).

### 2.1.5. Equilibrium Models for a Living Cell

A living cell is not at equilibrium: it takes up nutrients, dissipates free energy and exports entropy (2.5). Equilibrium statistical mechanics is nevertheless the main tool of this course, because it applies wherever some processes are much faster than others. If a reaction $\mathrm{A} \rightleftharpoons \mathrm{B}$ interconverts in milliseconds while B is consumed in minutes, A and B keep their equilibrium ratio at all times (a rapid pre-equilibrium), and the slow process can be treated as acting on an equilibrium mixture. In the same way a protein exchanges conformations in microseconds to seconds and can be described by the equilibrium between folded and unfolded states (7.6.16); the binding of a transcription factor equilibrates in seconds, faster than expression changes ([7.2.22](/7.2.22#sec-22.1.2)); and a membrane relaxes its shape faster than the cytoskeleton remodels, so the shape of a red blood cell can be computed as the shape that minimizes the elastic free energy of its membrane at fixed area and volume (7.6.24). Two steps are common to all such problems: choose the class of competing states (all shapes with given area and volume, all conformations, all arrangements of molecules), and assign each its free energy; equilibrium is the competitor of lowest free energy.

For purely mechanical problems, without thermal fluctuations, the rule reduces to minimizing the potential energy. Newton's condition $\sum_i\boldsymbol{F}_i = \boldsymbol{0}$ for a body at rest is equivalent to $\partial U/\partial x = 0$ at a minimum of $U(x)$: a spring of stiffness $k$ holding a weight $mg$ minimizes $U = \frac{1}{2}kx^2 - mgx$ at $x = mg/k$. When the state is described by a function, such as the profile of a membrane $h(x)$ or the contour of a filament, the energy is a functional $U[h]$, a number for each function, and its minimum satisfies the Euler–Lagrange equation of the calculus of variations ([2.2](/2.2)); this is how membrane shapes and filament buckling are computed (7.6.24, 7.6.26).

Near any minimum the energy is quadratic: $U(x) \approx U_0 + \frac{1}{2}U''(x_0)(x - x_0)^2$. For a rod of length $L$, cross-section $A$ and Young's modulus $E$, the stress is proportional to the strain, $F/A = E\,\Delta L/L$, which is Hooke's law with spring constant $k = EA/L$: the stretching of a macroscopic rod is the collective stretching of its atomic bonds. An actin filament ($E \approx 2\,\mathrm{GPa}$, $A \approx 40\,\mathrm{nm}^2$) $1\,\mu\mathrm{m}$ long has $k \approx 80\,\mathrm{pN\,nm^{-1}}$ and stretches by about $0.1\,\mathrm{nm}$ under a $10\,\mathrm{pN}$ load: filaments are nearly inextensible, and their mechanics is dominated by bending (7.6.26).

### 2.1.6. The Energy Budget of a Cell

Cells store free energy in three interconvertible forms: the phosphoanhydride bonds of ATP (about $20\,k_{\mathrm{B}}T$ per hydrolysis under cellular conditions, [7.6.3](/7.6.3#sec-3.2.4)), between the thermal energy and the $\sim 150\,k_{\mathrm{B}}T$ of a covalent bond, a currency of convenient denomination; the reducing power of NADH and NADPH, which carry electrons for biosynthetic reductions; and ion gradients across membranes, built by electron transport and converted into ATP by ATP synthase ([7.6.3](/7.6.3#sec-3.4)).

**Example 2.1.1 (What it costs to build *E. coli*)** A new *E. coli* cell contains about $10^{10}$ carbon atoms. Growing on glucose, it must take up $10^{10}/6 \approx 2\times10^9$ glucose molecules just for its carbon skeletons. The energy to rebuild those skeletons into its macromolecules can be estimated from typical costs: making an amino acid from glucose costs on average about 1 ATP equivalent in aerobic growth and adding it to a protein about 4 more (charging tRNA and driving the ribosome), so the $3\times10^6$ proteins of 300 residues cost $5.2\times300\times3\times10^6 \approx 4.5\times10^9$ ATP equivalents; for nucleic acids the precursors dominate (10–20 ATP equivalents per nucleotide, little for polymerization), and adding RNA ($1.6\times10^9$), phospholipids ($3.2\times10^9$), DNA ($3.5\times10^8$), lipopolysaccharide ($3.8\times10^8$), peptidoglycan ($1.7\times10^8$) and glycogen gives about $10^{10}$ ATP equivalents per cell. At up to 30 ATP per glucose oxidized aerobically, this requires about $3\times10^8$ glucose molecules, a fifth of those used as material; in a 40-minute cell cycle the cell hydrolyzes some $4\times10^6$ ATP per second. Under anaerobic growth the energy cost can exceed the material cost tenfold, and the turnover of macromolecules adds to the budget.

## 2.2. The Boltzmann Distribution from Maximum Entropy

### 2.2.1. The Principle of Maximum Entropy

A molecule in a cell is not isolated: it exchanges energy with its surroundings. We want the probability $p_i$ that it is in microstate $i$ with energy $E_i$. The answer can be found by asking which probability distribution assumes the least beyond what we know.

For a distribution $\{p_i\}$, the Gibbs entropy

$$
S = -k_{\mathrm{B}}\sum_i p_i\ln p_i \tag{2.2}
$$
is $k_{\mathrm{B}}\ln 2$ times the Shannon entropy in bits of information theory ([4.5.6](/4.5.6)): it is zero when one state is certain, and largest, $k_{\mathrm{B}}\ln\Omega$, when all $\Omega$ states are equally likely. It measures the information we lack about which microstate the system is in.

**Definition 2.2.1 (Maximum Entropy Principle)** The **maximum entropy principle** states that, among all probability distributions consistent with what is known about a system (normalization and the values of some averages), the one to be used is the one that maximizes the entropy (2.2). It was proposed by Edwin Jaynes (1957) as a rule of statistical inference: any other choice would assume information that we do not have.

With no constraint other than normalization, the maximum is the uniform distribution $p_i = 1/\Omega$, which gives back the equal a priori probabilities of an isolated system. A constraint on the mean energy gives the Boltzmann distribution.

### 2.2.2. The Boltzmann Distribution

**Theorem 2.2.1 (Boltzmann Distribution)** The distribution that maximizes the entropy (2.2) subject to $\sum_i p_i = 1$ and a given mean energy $\sum_i p_iE_i = \langle E\rangle$ is

$$
p_i = \frac{\mathrm{e}^{-\beta E_i}}{Z}, \qquad Z = \sum_i \mathrm{e}^{-\beta E_i}, \tag{2.3}
$$
where $\beta$ is fixed by the value of $\langle E\rangle$. For a system in contact with surroundings at temperature $T$, $\beta = 1/k_{\mathrm{B}}T$.

**Proof** Introduce **Lagrange multipliers** $\lambda$ and $\beta$ for the two constraints and maximize

$$
\mathcal{S} = -\sum_i p_i\ln p_i - \lambda\Big(\sum_i p_i - 1\Big) - \beta\Big(\sum_i p_iE_i - \langle E\rangle\Big).
$$
Setting $\partial\mathcal{S}/\partial p_i = -\ln p_i - 1 - \lambda - \beta E_i = 0$ gives $p_i = \mathrm{e}^{-1-\lambda}\mathrm{e}^{-\beta E_i}$, and normalization gives Eq. (2.3). The function $-p\ln p$ is strictly concave and the constraints are linear, so this stationary point is the unique maximum. To identify $\beta$, insert (2.3) into (2.2): $S = k_{\mathrm{B}}\sum_i p_i(\beta E_i + \ln Z) = k_{\mathrm{B}}(\beta\langle E\rangle + \ln Z)$. A small change of the energy levels at fixed $\{E_i\}$ (heat, no work) changes $\langle E\rangle$ and $S$ with $\mathrm{d}S = k_{\mathrm{B}}\beta\,\mathrm{d}\langle E\rangle$, because the terms from $\mathrm{d}\beta$ cancel ($\mathrm{d}\ln Z/\mathrm{d}\beta = -\langle E\rangle$). The thermodynamic relation $\mathrm{d}S = \delta Q_{\mathrm{rev}}/T$ then requires $k_{\mathrm{B}}\beta = 1/T$. $\square$

The **Boltzmann distribution** ([5.2.1](/5.2.1)) was derived in [6.3.10](/6.3.10#sec-10.3) by finding the most probable distribution of a large number of particles over energy levels; the derivation here reaches the same result by a different route, which needs no large number of copies and applies to a single molecule in a bath. Each derivation has its use: the counting one shows why the result is sharp for large systems, the inference one why it can be applied to one protein.

**Remark 2.2.1 (The Boltzmann distribution from a reservoir)** The classic derivation considers the system together with a large reservoir, the two forming an isolated whole of total energy $E_{\mathrm{tot}}$ in which all microstates are equally likely. The probability that the system is in its microstate $i$ is proportional to the number of microstates of the reservoir with the remaining energy, $\Omega_{\mathrm{R}}(E_{\mathrm{tot}} - E_i) = \mathrm{e}^{S_{\mathrm{R}}(E_{\mathrm{tot}} - E_i)/k_{\mathrm{B}}}$. Expanding the reservoir's entropy to first order in the small $E_i$, with $\partial S_{\mathrm{R}}/\partial E = 1/T$, gives $p_i \propto \mathrm{e}^{-E_i/k_{\mathrm{B}}T}$: the Boltzmann factor is the reservoir's loss of microstates when the system takes energy from it.

### 2.2.3. Partition Function and Free Energy

The normalization $Z$ of Eq. (2.3), the **partition function**, contains all the equilibrium thermodynamics of the system.

**Formula 2.2.1 (Thermodynamics from the Partition Function)** For a system at temperature $T$ with partition function $Z(\beta)$, $\beta = 1/k_{\mathrm{B}}T$,

$$
F = -k_{\mathrm{B}}T\ln Z, \qquad \langle E\rangle = -\frac{\partial\ln Z}{\partial\beta}, \qquad
S = \frac{\langle E\rangle - F}{T}, \qquad \langle E^2\rangle - \langle E\rangle^2 = \frac{\partial^2\ln Z}{\partial\beta^2} = k_{\mathrm{B}}T^2C_V, \tag{2.4}
$$
where $F$ is the **Helmholtz free energy** and $C_V = \partial\langle E\rangle/\partial T$ the **heat capacity**.

The last relation is the first example of a general theme: the response of a system to a change in a parameter (here the energy's response to temperature) is determined by its spontaneous fluctuations at equilibrium.

The same reasoning applies to macrostates. If macrostate $I$ collects the microstates $i \in I$, its probability is

$$
P_I = \sum_{i\in I}p_i = \frac{Z_I}{Z} = \mathrm{e}^{-\beta(F_I - F)}, \qquad F_I = -k_{\mathrm{B}}T\ln Z_I = E_I - TS_I, \tag{2.5}
$$
where the last form holds when all microstates of $I$ have the same energy $E_I$, so that $Z_I = \Omega_I\mathrm{e}^{-\beta E_I}$ and $S_I = k_{\mathrm{B}}\ln\Omega_I$. The probability of a macrostate is a Boltzmann factor of its free energy, not of its energy. A folded protein, a bound complex, a closed channel are macrostates comprising very many microstates, and their relative probabilities are set by free-energy differences:

$$
\frac{P_I}{P_J} = \mathrm{e}^{-\beta(F_I - F_J)}. \tag{2.6}
$$
For a large system, $F_I$ is extensive, $F_I = Nf_I$, and $Z = \sum_I\mathrm{e}^{-\beta Nf_I}$ is dominated by the smallest $f_I$: the equilibrium macrostate is the one of minimum free energy. At constant temperature and pressure, the relevant free energy is the **Gibbs free energy** $G = E + pV - TS$ ([6.3.3](/6.3.3)), the one used for reactions in solution.

### 2.2.4. Generalized Forces and Fluctuations

Often an external parameter couples to a variable of the system: a force $f$ to an extension $x$, a voltage to a charge, a chemical potential to a number of molecules. If the energy of microstate $i$ becomes $E_i - fx_i$, the partition function $Z(f) = \sum_i\mathrm{e}^{-\beta(E_i - fx_i)}$ defines a free energy $G(f) = -k_{\mathrm{B}}T\ln Z(f)$, and

$$
\langle x\rangle = -\frac{\partial G}{\partial f} = k_{\mathrm{B}}T\frac{\partial\ln Z}{\partial f}, \qquad
\frac{\partial\langle x\rangle}{\partial f} = \frac{\langle x^2\rangle - \langle x\rangle^2}{k_{\mathrm{B}}T}. \tag{2.7}
$$
The second relation says that the stiffness of a system's response to a force equals its spontaneous fluctuations divided by $k_{\mathrm{B}}T$: a soft system fluctuates much, a stiff one little. This is the static form of the **fluctuation**–dissipation relations of 7.6.5, and it is how forces are measured in single-molecule experiments: one observes fluctuations and infers stiffnesses, or applies forces and infers free energies (7.6.17).

### 2.2.5. The Ideal Gas: Pressure, Velocities and Sedimentation

The ideal gas, molecules without interactions, is the model in which the connection between microscopic motion and macroscopic quantities can be followed most directly. A molecule of mass $m$ bouncing between two walls a distance $L$ apart transfers momentum $2mv_x$ to a wall every $2L/v_x$; summing over $N$ molecules in a volume $V$ gives the pressure $p = Nm\langle v_x^2\rangle/V$. Comparison with the ideal gas law $pV = Nk_{\mathrm{B}}T$ gives $\frac{1}{2}m\langle v_x^2\rangle = \frac{1}{2}k_{\mathrm{B}}T$, and by symmetry the mean kinetic energy of a molecule is $\frac{3}{2}k_{\mathrm{B}}T$, the equipartition result of 2.3.2. The distribution of each velocity component is the Boltzmann factor of the kinetic energy, $p(v_x) \propto \mathrm{e}^{-mv_x^2/2k_{\mathrm{B}}T}$, a Gaussian of variance $k_{\mathrm{B}}T/m$ (the **Maxwell velocity distribution**, [5.2.1](/5.2.1)). The entropy of the gas counts the positions and velocities available to its molecules,

$$
S = Nk_{\mathrm{B}}\left[\ln\frac{V}{N\lambda^3} + \frac{5}{2}\right], \qquad \lambda = \frac{h}{\sqrt{2\pi mk_{\mathrm{B}}T}}, 
$$
the Sackur–Tetrode formula, which grows with the volume per molecule and with temperature; its volume dependence, $Nk_{\mathrm{B}}\ln V$, is all that the osmotic pressure of 2.3.3 needs.

In an external field the potential energy enters the Boltzmann factor as well. In gravity the number density falls with height as $n(z) \propto \mathrm{e}^{-mgz/k_{\mathrm{B}}T}$, with a scale height $k_{\mathrm{B}}T/mg$ of about $9\,\mathrm{km}$ for nitrogen in air. For a molecule in solution, $m$ is replaced by the buoyant mass $m(1 - \bar v\rho)$, where $\bar v$ is its partial specific volume and $\rho$ the density of the solvent.

**Example 2.2.1 (Sedimentation of a protein)** A protein of $50\,\mathrm{kDa}$ ($8.3\times10^{-23}\,\mathrm{kg}$) with $\bar v = 0.73\,\mathrm{cm^3\,g^{-1}}$ in water has a buoyant mass of $2.2\times10^{-23}\,\mathrm{kg}$. In the Earth's gravity its scale height is $k_{\mathrm{B}}T/(m_{\mathrm{b}}g) \approx 4.3\times10^{-21}/(2.2\times10^{-23}\times9.8)\,\mathrm{m} \approx 20\,\mathrm{m}$: proteins do not settle in a test tube. In an ultracentrifuge the centrifugal potential $-\frac{1}{2}m_{\mathrm{b}}\omega^2r^2$ replaces $m_{\mathrm{b}}gz$, and at an acceleration of $10^5\,g$ the scale height shrinks to $0.2\,\mathrm{mm}$, comparable to the length of the sample cell. The concentration profile at **sedimentation equilibrium**, $c(r) \propto \exp[m_{\mathrm{b}}\omega^2r^2/2k_{\mathrm{B}}T]$, therefore measures the buoyant mass and hence the molecular mass ([6.3.21](/6.3.21), 7.6.8).

## 2.3. Energy against Entropy

In $F = E - TS$ energy and entropy enter with opposite signs. Low temperature favors the macrostate of lowest energy, high temperature the one of largest entropy; biological systems live where the two are comparable, which is why they can switch between states with modest changes of temperature, force, voltage or concentration.

### 2.3.1. Hairpins: A Model of Melting

An RNA or DNA strand with two complementary segments folds into a hairpin: a base-paired stem closed by a loop. Opening the hairpin costs the base-pairing and stacking energy, but frees the strand to adopt many conformations.

**Example 2.3.1 (Melting of hairpins)** Consider $N$ independent hairpins, each closed (energy 0, one conformation) or open (energy $\Delta h$ higher, with $g$ conformations, internal entropy $\Delta s = k_{\mathrm{B}}\ln g$). If $n$ are open, the free energy of the macrostate is

$$
F(n) = n(\Delta h - T\Delta s) - k_{\mathrm{B}}T\ln\binom{N}{n},
$$
the last term being the entropy of choosing which hairpins are open. With Stirling's approximation and $x = n/N$, $F/N = x(\Delta h - T\Delta s) + k_{\mathrm{B}}T[x\ln x + (1 - x)\ln(1 - x)]$, and $\partial F/\partial x = 0$ gives the equilibrium fraction open,

$$
x_{\mathrm{eq}} = \frac{1}{1 + \mathrm{e}^{(\Delta h - T\Delta s)/k_{\mathrm{B}}T}}, \tag{2.8}
$$
the same as the two-state probability of a single hairpin from Eq. (2.6). The hairpins are half open at the melting temperature $T_{\mathrm{m}} = \Delta h/\Delta s$. For a short hairpin with $\Delta H = 200\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S = 606\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per mole of hairpins, $T_{\mathrm{m}} = 330\,\mathrm{K}$ ($57\,^\circ\mathrm{C}$), and the slope at $T_{\mathrm{m}}$, $\mathrm{d}x/\mathrm{d}T = \Delta H/(4RT_{\mathrm{m}}^2) = 0.055\,\mathrm{K^{-1}}$, makes the transition about $20\,\mathrm{K}$ wide.

If the open state had no conformational entropy ($g = 1$), Eq. (2.8) would become $x = 1/(1 + \mathrm{e}^{\Delta h/k_{\mathrm{B}}T}) < 1/2$ at every temperature: the mixing entropy of which hairpins are open can never melt them. A transition between macrostates requires that the high-energy state have a larger internal entropy; the slope of the transition, the van 't Hoff enthalpy, measures $\Delta h$ (7.6.8).

![Energy against entropy in RNA hairpins (ΔH = 200 kJ/mol, ΔS = 606 J/(mol K) per mole of hairpins). A: fraction open against temperature from Eq. (2.8), with melting temperature T_m = ΔH/ΔS = 57 °C (solid); dashed, the model without conformational entropy of the open state (g = 1), in which fewer than 10⁻³⁰ of the hairpins are ever open. B: free energy per hairpin as a function of the open fraction x, in units of RT, at 49, 57 and 65 °C: energy favors x = 0, the mixing entropy rounds the curve, and the minimum (dots) moves from mostly closed to mostly open as the temperature crosses T_m](./plots/hairpin.py)

### 2.3.2. Equipartition and the Thermal Spring

A bead held in a harmonic potential, by an optical trap or by the elasticity of a molecule, has energy $E(x) = \frac{1}{2}kx^2$. By Eq. (2.3) its position is distributed as $p(x) \propto \mathrm{e}^{-kx^2/2k_{\mathrm{B}}T}$, a Gaussian of variance

$$
\langle x^2\rangle = \frac{k_{\mathrm{B}}T}{k}, \qquad \Big\langle\tfrac{1}{2}kx^2\Big\rangle = \tfrac{1}{2}k_{\mathrm{B}}T. \tag{2.9}
$$
This is the **equipartition theorem** ([5.2.1](/5.2.1)): every degree of freedom that enters the energy quadratically carries a mean energy $\frac{1}{2}k_{\mathrm{B}}T$, whatever its stiffness.

**Example 2.3.2 (Calibrating an optical trap)** A bead in **optical tweezers** with stiffness $k = 0.05\,\mathrm{pN\,nm^{-1}}$ at $310\,\mathrm{K}$ fluctuates with a root-mean-square displacement $\sqrt{k_{\mathrm{B}}T/k} = \sqrt{4.28/0.05}\,\mathrm{nm} = 9.3\,\mathrm{nm}$. Conversely, measuring the variance of the bead's position gives $k = k_{\mathrm{B}}T/\langle x^2\rangle$ without any knowledge of the optics; the force on a molecule attached to the bead is then $k$ times its displacement from the trap center. Forces of a piconewton, displacements of nanometers and the thermal energy of a few $\mathrm{pN\,nm}$ are of one scale, and Eq. (2.9) ties them together (7.6.17).

Equation (2.3) can also be used to generate samples. The **Metropolis algorithm**, a **Markov chain Monte Carlo** method ([3.5.9](/3.5.9)), proposes a random move and accepts it with probability $\min(1, \mathrm{e}^{-\Delta E/k_{\mathrm{B}}T})$; the chain visits microstates with Boltzmann probabilities, so averages over the chain are equilibrium averages. For a spring it reproduces Eq. (2.9), and the same algorithm, applied to the energy of a protein or a lattice model, is how equilibrium properties of systems too complex for exact calculation are computed (7.6.15).

![Metropolis sampling of a bead in a harmonic trap, E = kx²/2 with k = 0.05 pN/nm at 310 K (uniform proposals of up to ±12 nm, 40 000 steps). A: the first 600 steps of the chain, starting far from the center. B: histogram of the positions after a burn-in of 1000 steps, with the Boltzmann (Gaussian) density of standard deviation √(kBT/k) = 9.3 nm. C: the running average of the energy converges to kBT/2, equipartition](./plots/spring-metropolis.py)

### 2.3.3. Ideal Solutions and Osmotic Pressure

$N$ solute molecules dilute enough not to interact behave like an ideal gas within the solvent. In a volume $V$, each can be anywhere, so the number of microstates grows as $V^N$, and the free energy contains $-Nk_{\mathrm{B}}T\ln V$. A membrane permeable to water but not to the solute feels the derivative of this free energy, a pressure:

$$
\Pi = -\frac{\partial F}{\partial V} = \frac{Nk_{\mathrm{B}}T}{V} = ck_{\mathrm{B}}T, \tag{2.10}
$$
the van 't Hoff relation for the **osmotic pressure** ([6.3.5](/6.3.5#sec-5.3.4)), where $c$ is the number density of solute particles (ions counted separately).

**Example 2.3.3 (The osmotic pressure of a cell)** A concentration of $100\,\mathrm{mM}$ is $0.1\times6.0\times10^{23}$ molecules per $10^{24}\,\mathrm{nm}^3$, or $0.060\,\mathrm{nm}^{-3}$. With $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$, $\Pi = 0.25\,\mathrm{pN\,nm^{-2}} = 2.5\times10^5\,\mathrm{Pa}$ (since $1\,\mathrm{pN\,nm^{-2}} = 10^6\,\mathrm{Pa}$), about $2.4\,\mathrm{atm}$. The cytoplasm of an animal cell has a total of about $300\,\mathrm{mM}$ of osmotically active particles, an osmotic pressure of about $7.7\times10^5\,\mathrm{Pa}$ ($7.6\,\mathrm{atm}$) at $310\,\mathrm{K}$, balanced by an equal concentration outside. A red blood cell placed in pure water feels this full difference and bursts; bacteria, fungi and plants keep their cytoplasm more concentrated than their surroundings and resist the resulting turgor pressure, a few to tens of atmospheres, with a cell wall (**osmosis**, [7.1.2](/7.1.2#sec-2.1.6)).

Osmotic pressure acts wherever a membrane or shell separates solutions of different composition: organelles and vesicles swell or shrink with the osmolarity of the cytoplasm, and the capsid of a bacteriophage must withstand the osmotic pressure of the ions and DNA it contains. It is also a measuring tool. In osmotic stress experiments, DNA is condensed into a hexagonal array in a solution of a polymer such as polyethylene glycol, too large to enter the array; the polymer's osmotic pressure, known from its concentration, presses the strands together, and X-ray diffraction measures their spacing. The pressure needed to bring parallel DNA strands from about $3.5$ to $2.5\,\mathrm{nm}$ apart rises exponentially as the spacing decreases, with a decay length of about $0.3\,\mathrm{nm}$, a short-range repulsion between the strands due to the structured water between them that dominates the electrostatics at close approach (7.6.6).

The pressure is entropic: nothing pushes on the membrane except the solute's tendency to occupy more volume. This leads to a general notion.

### 2.3.4. Entropic Forces

**Definition 2.3.1 (Entropic Force)** An **entropic force** is a generalized force $f = -\partial F/\partial x$ on a coordinate $x$ whose origin is the dependence of the entropy, not of the energy, on $x$: at constant temperature and energy, $f = T\,\partial S/\partial x$.

Entropic forces are everywhere in the cell:

| Entropic force | Coordinate | Origin of the entropy change | Chapter |
|---|---|---|---|
| Osmotic pressure | Volume | Positions of solute molecules | 2.3.3 |
| Gas pressure on a piston | Volume | Positions of gas molecules | 5.2 |
| Elasticity of a polymer chain | End-to-end distance | Number of chain conformations | 7.6.21 |
| Depletion attraction | Distance between large particles | Volume available to small crowders | 7.6.23 |
| Hydrophobic attraction | Buried nonpolar area | Orientations of water molecules | 2.3.5 |
| Polymerization ratchet | Gap at a filament tip | Thermal fluctuations of a membrane or particle | 7.6.26 |

A useful check that a force is entropic: it is proportional to the absolute temperature at fixed geometry. A rubber band (an entropic spring) pulls harder when heated, unlike a steel spring.

The maximum work obtainable from such a force is the decrease of free energy. For $N$ molecules of ideal gas or solute expanding isothermally from $V_1$ to $V_2$ against a matched external pressure,

$$
W_{\max} = \int_{V_1}^{V_2}\frac{Nk_{\mathrm{B}}T}{V}\,\mathrm{d}V = Nk_{\mathrm{B}}T\ln\frac{V_2}{V_1} = -\Delta F, \tag{2.11}
$$
with $\Delta E = 0$ and $\Delta S = Nk_{\mathrm{B}}\ln(V_2/V_1)$. The energy for this work comes from the heat bath; the free energy acts as a potential energy for systems in thermal contact, and its decrease is the most work they can do. For one molecule doubling its volume, $W_{\max} = k_{\mathrm{B}}T\ln 2$, a number that returns in 2.4.

### 2.3.5. The Hydrophobic Effect

Oil and water separate, even in the weightlessness of orbit. This seems to contradict the tendency to mix that underlies Eq. (2.10). The resolution is that the relevant entropy is that of the water.

Water is held together by **hydrogen bonds** of about $9\,k_{\mathrm{B}}T$ each in the gas phase (much less net in water, where breaking one bond lets others form), compared with about $1\,k_{\mathrm{B}}T$ for a **van der Waals force** contact and $\sim 150\,k_{\mathrm{B}}T$ for a covalent bond. A water molecule can donate two and accept two hydrogen bonds, toward the corners of a tetrahedron; in ice every molecule makes four, and liquid water at room temperature still makes about 3.5 on average. A molecule in the bulk with four bonds can be oriented in six ways (its two hydrogens point along two of the six edges of its tetrahedron). Next to a nonpolar surface, which offers no partner, a water molecule keeps its four bonds only by pointing no bond toward the surface, which leaves about three of the six orientations.

**Example 2.3.4 (Estimating the hydrophobic cost)** The entropy lost by each interfacial water molecule is $\Delta S = k_{\mathrm{B}}\ln(3/6) = -k_{\mathrm{B}}\ln 2$, a free-energy cost $k_{\mathrm{B}}T\ln 2 \approx 0.7\,k_{\mathrm{B}}T$. Water has $33$ molecules per $\mathrm{nm}^3$, so a surface layer has about $33^{2/3} \approx 10$ molecules per $\mathrm{nm}^2$, and the cost of exposing nonpolar surface is about $7\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$. Transfer free energies of hydrocarbons from water to oil give $3$–$7\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$ depending on the reference state (the frequently used $25\,\mathrm{cal\,mol^{-1}\,\text{Å}^{-2}}$ is $4\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$). For an $\ce{O2}$ molecule, with a surface below $0.3\,\mathrm{nm}^2$, the cost is about one $k_{\mathrm{B}}T$, and oxygen dissolves; for an unfolded protein exposing $100\,\mathrm{nm}^2$ of nonpolar surface it is hundreds of $k_{\mathrm{B}}T$, and the chain collapses to bury it.

The estimate captures why the **hydrophobic effect** ([7.1.2](/7.1.2#sec-2.1.3)) is mainly entropic at room temperature: its free energy increases with temperature at first (as $-T\Delta S$ would), it is accompanied by a large positive heat capacity of hydration, and it is the main driving force of protein folding and of membrane formation. Its limits are equally instructive: around solutes larger than about $1\,\mathrm{nm}$ the hydrogen-bond network can no longer wrap around the surface, bonds are broken outright, and the cost becomes enthalpic and proportional to area with a coefficient set by the surface tension of water; at high temperature the entropic part weakens and the effect changes character, which is one origin of the cold denaturation of proteins (7.6.8). Protein folding, the assembly of lipid bilayers and the binding of nonpolar ligands are all ordered structures produced by an increase of total entropy: the order of the solute is paid for by the disorder of the solvent.

## 2.4. Information and Thermodynamics

### 2.4.1. Bits and Entropy

Equation (2.2) identifies thermodynamic entropy with missing information: one bit, the information needed to decide between two equally likely alternatives, corresponds to an entropy $k_{\mathrm{B}}\ln 2$. The three historical meanings of entropy (Clausius, Boltzmann, Shannon) and their unification were set out in [6.3.18](/6.3.18#sec-18.4.3); here we follow the consequence that information has a physical cost, and what that cost means for cells, which acquire, store and copy information constantly.

### 2.4.2. Maxwell's Demon

**Definition 2.4.1 (Maxwell's Demon)** **Maxwell's demon** is a hypothetical being, proposed by James Clerk Maxwell in 1867–1871, that observes the molecules of a gas in a container divided by a wall with a small door, and opens the door only for fast molecules moving from left to right and slow ones moving from right to left. Without doing work, it would make one side hotter than the other, in apparent violation of the second law.

For eighty years the demon resisted a satisfactory answer. The resolution, completed by Leo Szilard (1929), Rolf Landauer (1961) and Charles Bennett (1982), is that the demon is itself a physical system: to sort molecules it must acquire and store information about them, and its memory must eventually be reset, which has an entropy cost at least equal to the entropy it removes from the gas.

Two clarifications prevent common confusions. Membrane transporters and pumps, which move solutes against their gradients, are sometimes called Maxwell's demons; they are not, because they do not sort by information alone but are driven by a free-energy source (ATP hydrolysis or a coupled ion gradient), and they obey the second law locally, step by step ([7.1.13](/7.1.13), [6.3.18](/6.3.18#sec-18.2.5)). Nor is the demon a prototype of a **dissipative structure**: a dissipative structure ([6.3.18](/6.3.18#sec-18.3)) is a pattern maintained by a continuous flux of free energy through an open system, whereas the demon is a device that would decrease entropy without any flux, which is exactly what is impossible.

### 2.4.3. The Szilard Engine and Landauer's Principle

**Definition 2.4.2 (Szilard Engine)** The **Szilard engine** is a thought experiment in which a single molecule in a box at temperature $T$ is used to extract work from one heat bath with the help of information: a partition is inserted in the middle, the side on which the molecule is found is measured and recorded, and the partition is used as a piston on that side, letting the one-molecule gas expand isothermally back to the full volume.

By Eq. (2.11) with $N = 1$ and $V_2/V_1 = 2$, the expansion delivers work $W = k_{\mathrm{B}}T\ln 2$, drawn as heat from the bath. If this were the whole cycle, the engine would convert heat from a single bath into work, contradicting the second law. The missing step is the memory: after the cycle the record "left" or "right" is still there, and to run the engine again the memory must be returned to a standard state.

**Theorem 2.4.1 (Landauer Bound)** Erasing one bit of information, that is, mapping a memory that is in either of two equally probable states into one definite state, in contact with a bath at temperature $T$, dissipates at least $k_{\mathrm{B}}T\ln 2$ of heat into the bath.

**Proof** Before erasure the memory is in one of two macrostates with probabilities $\frac{1}{2}$; its entropy contains a term $k_{\mathrm{B}}\ln 2$ from not knowing which. After erasure it is in one definite macrostate, and this term is gone: $\Delta S_{\mathrm{mem}} = -k_{\mathrm{B}}\ln 2$ (other contributions being equal, since the two states are physically equivalent). The total entropy of memory and bath cannot decrease, so the bath's entropy must rise by at least $k_{\mathrm{B}}\ln 2$, which at temperature $T$ requires heat $Q \ge k_{\mathrm{B}}T\ln 2$. $\square$

This is **Landauer's principle** ([6.3.18](/6.3.18#sec-18.4.3)) applied to the demon: the work gained from one bit of information, $k_{\mathrm{B}}T\ln 2$, is exactly the minimum cost of erasing it, and the second law holds for the engine and its memory together. Bennett showed that the measurement itself can in principle be done reversibly; the irreducible cost lies in erasure. Experiments have since approached both halves: feedback on a Brownian particle converted information into free energy (Toyabe and colleagues, 2010), and erasure of a one-bit memory made of a colloidal bead in a double-well optical trap dissipated heat approaching $k_{\mathrm{B}}T\ln 2$ when done slowly (Bérut and colleagues, 2012).

![The Szilard engine. 1: one molecule moves through the whole box, in contact with a heat bath at temperature T; the demon's memory is in its reset state 0. 2: a partition is inserted in the middle and the demon measures and records on which side the molecule is (L). 3: using the record, the partition is coupled as a piston to a load on the correct side, and the one-molecule gas expands isothermally from V/2 to V, lifting the load by W = kBT ln 2 with the heat Q = kBT ln 2 drawn from the bath. 4: to close the cycle the memory is reset to 0; by Landauer's principle this dissipates at least kBT ln 2 into the bath, so that no net work is gained from a single bath over the whole cycle](./plots/szilard-engine.py)

### 2.4.4. Information in Cells

At $310\,\mathrm{K}$ the Landauer bound is $k_{\mathrm{B}}T\ln 2 = 3.0\times10^{-21}\,\mathrm{J}$, $0.69\,k_{\mathrm{B}}T$, about $1/30$ of the free energy of one ATP. Biological information processing is far above this bound. Adding one nucleotide to a DNA strand consumes two phosphoanhydride bonds (the dNTP is cleaved to dNMP and pyrophosphate, which is then hydrolyzed), some $40\,k_{\mathrm{B}}T$, whereas the information it stores is at most $2$ bits, $1.4\,k_{\mathrm{B}}T$; Bennett showed that copying, unlike erasure, can in principle be done at no cost at all if done infinitely slowly. The excess pays for speed and accuracy: a polymerase must work in milliseconds per step, and it reaches error rates of $10^{-9}$, far below what equilibrium discrimination allows, by dissipating free energy in proofreading ([7.2.22](/7.2.22#sec-22.7)). Sensing (7.6.35) and timekeeping (7.6.38) carry similar costs. The relations between the information a cell processes, the speed and accuracy it achieves and the free energy it dissipates are a central subject of quantitative biology (7.6.38).

## 2.5. Open Systems and the Entropy Balance of Life

### 2.5.1. The Entropy Balance Equation

An isolated system approaches equilibrium, the state of maximum entropy, in which nothing happens. A living system is not isolated: it exchanges matter and energy with its surroundings. For an open system the change of entropy splits into two parts ([6.3.18](/6.3.18#sec-18.1.5)):

$$
\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S, \qquad \mathrm{d}_{\mathrm{i}}S \ge 0, \tag{2.12}
$$
where $\mathrm{d}_{\mathrm{e}}S$ is the **entropy flux** exchanged with the surroundings (with heat and matter), of either sign, and $\mathrm{d}_{\mathrm{i}}S$ the **entropy production** by irreversible processes inside the system, never negative. A living cell in steady state has $\mathrm{d}S = 0$: it produces entropy continuously, by every reaction, every transport process, every dissipation of free energy, and exports at least as much to its surroundings, $\mathrm{d}_{\mathrm{e}}S = -\mathrm{d}_{\mathrm{i}}S < 0$.

Schrödinger's phrase that life "feeds on negative entropy" (**negentropy**, [6.3.18](/6.3.18#sec-18.4.1)) means precisely this export, and is better expressed in terms of free energy. The statement that "life produces negative entropy", or that evolution or growth is "a process of negative entropy change", is wrong as physics: every living process produces entropy, $\mathrm{d}_{\mathrm{i}}S > 0$, and the order of the organism is maintained or increased only because the entropy exported to the surroundings is larger still. A cell consumes free energy, low-entropy inputs (sunlight, glucose and oxygen), and discards high-entropy outputs (heat, $\ce{CO2}$, water); the free energy of the input, $F = E - TS$, is the resource, and its dissipation is what drives every process away from equilibrium.

### 2.5.2. The Earth as an Open System

The free energy of the biosphere comes from the Sun. The Earth absorbs sunlight emitted by the solar surface at about $5800\,\mathrm{K}$ and returns the same energy (in steady state) as **thermal radiation** at its effective emission temperature, about $255\,\mathrm{K}$. Black-body radiation at temperature $T$ carries an entropy $\frac{4}{3}E/T$ with energy $E$, its **photons** have a mean energy $2.70\,k_{\mathrm{B}}T$, and each carries an entropy of $3.60\,k_{\mathrm{B}}$.

**Example 2.5.1 (Few photons in, many out)** Per joule, sunlight brings $1/(2.70\,k_{\mathrm{B}}\times5772\,\mathrm{K}) = 4.6\times10^{18}$ photons and an entropy $\frac{4}{3}/5772\,\mathrm{K} = 2.3\times10^{-4}\,\mathrm{J\,K^{-1}}$; the Earth sends back $1.1\times10^{20}$ infrared photons carrying $5.2\times10^{-3}\,\mathrm{J\,K^{-1}}$, both 23 times more. With the global mean of $240\,\mathrm{W\,m^{-2}}$ absorbed, the Earth exports entropy at about $\frac{4}{3}\times240\times(1/255 - 1/5772) = 1.2\,\mathrm{W\,K^{-1}}$ per square metre, $6\times10^{14}\,\mathrm{W\,K^{-1}}$ in total. All processes on Earth that produce entropy, the weather, the water cycle and life, run on this export. Photosynthesis captures a small part: global net primary production, about $1.0\times10^{17}\,\mathrm{g}$ of carbon per year at about $470\,\mathrm{kJ}$ per mole of carbon fixed as carbohydrate, is $4\times10^{21}\,\mathrm{J}$ per year or $1.3\times10^{14}\,\mathrm{W}$, about $0.1\,\%$ of the $1.2\times10^{17}\,\mathrm{W}$ the Earth absorbs.

![The entropy budget of the Earth, treating incoming sunlight as black-body radiation at 5772 K and outgoing radiation as black-body radiation at 255 K. A: the distribution of power over wavelength (per unit ln λ) for equal total power: sunlight peaks in the visible, the outgoing infrared near 13 µm. B: per joule of energy, the entropy carried by the incoming and outgoing radiation, with the numbers of photons in brackets: the Earth returns 23 times as many photons and exports 23 times the entropy it imports](./plots/earth-entropy.py)

The calculation idealizes: sunlight at the Earth is dilute, not black-body radiation at the solar temperature, which raises its entropy somewhat, and the Earth's emission is not a single black body. The conclusion is robust: the low entropy of sunlight relative to the Earth's thermal radiation is what the biosphere lives on, and the free energy that flows through the biosphere is a small fraction of what passes through the planet.

### 2.5.3. The Budget of an Organism

**Example 2.5.2 (A human at rest)** A resting adult dissipates about $100\,\mathrm{W}$, about $2000\,\mathrm{kcal}$ or $8.4\,\mathrm{MJ}$ per day, almost all of it eventually as heat at $310\,\mathrm{K}$. The entropy exported is about $100\,\mathrm{W}/310\,\mathrm{K} \approx 0.3\,\mathrm{W\,K^{-1}}$, together with a smaller amount in the excreted matter. If about 40 % of the free energy of food is captured in ATP at about $55\,\mathrm{kJ\,mol^{-1}}$ under cellular conditions, the body synthesizes $8.4\times10^6\times0.4/5.5\times10^4 \approx 60\,\mathrm{mol}$ of ATP a day, some $30\,\mathrm{kg}$, while the body contains only about $100\,\mathrm{g}$ of ATP at any moment: each ATP molecule is recycled several hundred times a day. A living body is a steady state of very fast turnover maintained by a steady flux of free energy, like the virus population of [7.6.1](/7.6.1#sec-1.5.3).

### 2.5.4. Order and Entropy in Biological Structures

Ordered biological structures do not all owe their order to the same thing, and the distinction matters.

- Equilibrium order: the folded state of a protein, a lipid bilayer, a DNA double helix and a virus capsid assembled from its subunits are macrostates of minimum free energy at physiological conditions. They form spontaneously, and their order is paid for by the entropy of the solvent (2.3.5) or by favorable energies. No continuous supply of free energy is needed to keep them, only to make their components (the covalent polymer chains, which are far from equilibrium with respect to hydrolysis).
- Nonequilibrium order: the concentration gradients across membranes, the oscillations of the cell cycle and the circadian clock, the polarity and motility of cells, and the patterns of development are maintained only as long as free energy flows; they are **dissipative structures** in the sense of Prigogine ([6.3.18](/6.3.18#sec-18.3)) and disappear at equilibrium. A system in equilibrium can have spatial order (a crystal) but no sustained temporal order: a time-periodic state requires a flux of free energy. These are the subject of the last part of the course (7.6.33–7.6.38).

Which kind of order a structure has is a question that can be settled by experiment: stop the free-energy supply (deplete ATP, collapse the proton gradient) and see whether the structure persists.

## Summary

- Counting (2.1): a macrostate's probability is proportional to its multiplicity; the binomial multiplicity peaks at an even split with relative width $1/\sqrt{N}$ (Formula 2.1.1), so macroscopic systems show sharp thermodynamics while single molecules and small copy numbers fluctuate. Entropy is $S = k_{\mathrm{B}}\ln\Omega$; the Clausius form is $\mathrm{d}S = \delta Q_{\mathrm{rev}}/T$, not "$S = Q/T$" in general. Maximizing the entropy of a composite system equalizes $T$, $p$ and $\mu$ between its parts, and near equilibrium fluxes are proportional to the differences (2.1.4). Equilibrium models apply to a living cell where fast processes equilibrate on the time scale of slow ones; mechanical equilibrium minimizes potential energy, near a minimum every system is a Hooke spring, $k = EA/L$ for a rod (2.1.5). Building one *E. coli* costs about $10^{10}$ ATP equivalents, a fifth of the glucose used as material (Example 2.1.1).
- Boltzmann distribution (2.2): maximizing the entropy $-k_{\mathrm{B}}\sum p\ln p$ under normalization and a mean energy (Definition 2.2.1) gives $p_i = \mathrm{e}^{-\beta E_i}/Z$ with $\beta = 1/k_{\mathrm{B}}T$ (Theorem 2.2.1). The partition function gives $F = -k_{\mathrm{B}}T\ln Z$, $\langle E\rangle$, $S$ and the energy fluctuations $k_{\mathrm{B}}T^2C_V$ (Formula 2.2.1); macrostates are weighted by $\mathrm{e}^{-\beta F_I}$, Eqs. (2.5)–(2.6); responses to forces equal fluctuations over $k_{\mathrm{B}}T$, Eq. (2.7). The Boltzmann factor is also the reservoir's loss of microstates (Remark 2.2.1). For the ideal gas, kinetic pressure gives $\frac{3}{2}k_{\mathrm{B}}T$ per molecule, velocities are Gaussian, and in a field the density falls as $\mathrm{e}^{-m_{\mathrm{b}}gz/k_{\mathrm{B}}T}$: proteins settle only in an ultracentrifuge (Example 2.2.1).
- Energy against entropy (2.3): hairpins melt at $T_{\mathrm{m}} = \Delta h/\Delta s$ only if the open state has conformational entropy (Example 2.3.1); a harmonic degree of freedom carries $\frac{1}{2}k_{\mathrm{B}}T$ and the variance $k_{\mathrm{B}}T/k$ calibrates an optical trap (Example 2.3.2), reproduced by Metropolis sampling; osmotic pressure is $ck_{\mathrm{B}}T$, about $2.4\,\mathrm{atm}$ per $100\,\mathrm{mM}$ (Example 2.3.3), and osmotic stress measures the forces between DNA strands; entropic forces (Definition 2.3.1) include osmotic pressure, polymer elasticity, depletion and the hydrophobic effect, which costs about $3$–$7\,k_{\mathrm{B}}T$ per $\mathrm{nm}^2$ of exposed nonpolar surface (Example 2.3.4).
- Information (2.4): one bit is an entropy $k_{\mathrm{B}}\ln 2$; Maxwell's demon (Definition 2.4.1) and the Szilard engine (Definition 2.4.2), which extracts $k_{\mathrm{B}}T\ln 2$ per bit, are reconciled with the second law by the Landauer bound for erasure (Theorem 2.4.1). Cells operate far above this bound, paying for speed and accuracy; transporters are free-energy-driven, not demons.
- Open systems (2.5): $\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S$ with $\mathrm{d}_{\mathrm{i}}S \ge 0$, Eq. (2.12); life produces entropy and exports more, consuming free energy. The Earth exports 23 times the entropy it receives from sunlight (Example 2.5.1); a human dissipates $100\,\mathrm{W}$ and turns over some $30\,\mathrm{kg}$ of ATP a day from a pool of about $100\,\mathrm{g}$ (Example 2.5.2). Equilibrium order (folded proteins, bilayers) and nonequilibrium order (gradients, oscillations, patterns) must be distinguished.

## Questions

1. For $N = 100$ molecules in a box, compute the probability that at least 60 are in the left half. Repeat for $N = 10\,000$ and at least 6000. What does the comparison say about thermodynamics for small systems?

   **Answer** $N_1$ is binomial with mean $N/2$ and standard deviation $\sqrt{N}/2$. For $N = 100$, 60 is two standard deviations above the mean, and the exact tail probability is $\mathbb{P}(N_1 \ge 60) = 0.028$. For $N = 10\,000$, 6000 is 20 standard deviations above the mean; the probability is about $10^{-89}$. A fluctuation of 20 % in the composition of a hundred-molecule system is a common event, in a ten-thousand-molecule system it never happens: small systems are described by distributions, not by single thermodynamic values.

2. Show that, among all distributions of a continuous variable $x$ on the real line with given mean $0$ and variance $\sigma^2$, the one of maximum entropy $-\int p\ln p\,\mathrm{d}x$ is the Gaussian. Interpret the result for a spring.

   **Answer** Maximize $-\int p\ln p - \lambda_0(\int p - 1) - \lambda_1\int xp - \lambda_2(\int x^2p - \sigma^2)$; the variation gives $-\ln p - 1 - \lambda_0 - \lambda_1x - \lambda_2x^2 = 0$, so $p \propto \mathrm{e}^{-\lambda_1x - \lambda_2x^2}$; the constraints give $\lambda_1 = 0$ and $\lambda_2 = 1/(2\sigma^2)$, a Gaussian. For a spring, fixing $\langle x^2\rangle$ is fixing the mean energy $\frac{1}{2}k\langle x^2\rangle$, and the Gaussian is the Boltzmann distribution with $\sigma^2 = k_{\mathrm{B}}T/k$: the two derivations coincide.

3. A two-state molecule has states of energy $0$ and $\varepsilon$. Compute its partition function, mean energy and heat capacity, and show that the heat capacity has a maximum near $k_{\mathrm{B}}T \approx 0.42\,\varepsilon$. Why does a protein solution show a peak of heat capacity at its melting temperature?

   **Answer** $Z = 1 + \mathrm{e}^{-\beta\varepsilon}$, $\langle E\rangle = \varepsilon/(\mathrm{e}^{\beta\varepsilon} + 1)$, $C = k_{\mathrm{B}}(\beta\varepsilon)^2\mathrm{e}^{\beta\varepsilon}/(\mathrm{e}^{\beta\varepsilon} + 1)^2$ (equivalently $\langle\delta E^2\rangle/k_{\mathrm{B}}T^2$). Maximizing over $u = \beta\varepsilon$ gives $u\tanh(u/2) = 2$, $u \approx 2.40$, so $k_{\mathrm{B}}T \approx 0.42\,\varepsilon$ and $C_{\max} \approx 0.44\,k_{\mathrm{B}}$. Heat capacity measures energy fluctuations (Formula 2.2.1); they are largest where the two states are comparably populated. For a protein, the two states are folded and unfolded with a large enthalpy difference, and the excess heat capacity peaks at $T_{\mathrm{m}}$; its area is the enthalpy of unfolding, measured by differential scanning calorimetry (7.6.8).

4. A dsDNA molecule is held by optical tweezers between two beads; the trap stiffness is $0.1\,\mathrm{pN\,nm^{-1}}$. What root-mean-square fluctuation of the bead position is expected at $298\,\mathrm{K}$? How long must the bead's position be recorded to measure $k$ with 1 % precision, if independent samples are obtained every $1\,\mathrm{ms}$?

   **Answer** $\sqrt{k_{\mathrm{B}}T/k} = \sqrt{4.11/0.1}\,\mathrm{nm} = 6.4\,\mathrm{nm}$. The variance of a Gaussian variable estimated from $n$ independent samples has relative standard error $\sqrt{2/n}$; for 1 %, $n = 2\times10^4$ samples, 20 seconds of recording. In practice the power spectrum of the fluctuations is fitted, which also gives the bead's friction coefficient and accounts for correlations between samples (7.6.17).

5. Estimate the osmotic pressure difference across the membrane of a red blood cell placed in pure water (internal osmolarity $300\,\mathrm{mOsm}$, $37\,^\circ\mathrm{C}$). If the membrane can withstand a tension of about $10\,\mathrm{mN\,m^{-1}}$ before rupture, use the Laplace relation $\Delta p = 2\gamma/R$ for a sphere of radius $R = 4\,\mu\mathrm{m}$ to decide whether the membrane can resist.

   **Answer** $\Pi = cRT = 300\,\mathrm{mol\,m^{-3}}\times8.314\times310\,\mathrm{Pa} = 7.7\times10^5\,\mathrm{Pa}$. A membrane at its rupture tension supports $2\times10^{-2}/(4\times10^{-6})\,\mathrm{Pa} = 5\times10^3\,\mathrm{Pa}$, about 150 times less. The cell swells as water enters until its membrane, which can stretch only a few percent in area, ruptures: hemolysis. A cell wall of a bacterium or plant cell is what makes a turgor pressure of several atmospheres sustainable.

6. Why must the open state of a hairpin, or the unfolded state of a protein, have a larger internal entropy than the closed or folded state for a melting transition to occur? Use Eq. (2.8) to explain, and give the physical origin of this entropy.

   **Answer** By Eq. (2.8), $x_{\mathrm{eq}} > 1/2$ requires $\Delta h - T\Delta s < 0$; with $\Delta h > 0$ (opening costs energy) this is possible only if $\Delta s > 0$, and then it happens above $T_{\mathrm{m}} = \Delta h/\Delta s$. The combinatorial entropy of which molecules are open does not help: it only rounds the curve and never pushes $x$ beyond $1/2$. The internal entropy is the number of conformations accessible to the unpaired strand or unfolded chain (rotations about backbone bonds), with a contribution from released water and ions.

7. A Szilard engine operates with a bath at $310\,\mathrm{K}$, extracting work from each bit of information. How many bits would be needed to make one ATP from ADP and phosphate under cellular conditions ($\Delta G \approx 20\,k_{\mathrm{B}}T$)? A bacterium that measures the concentration of an attractant every second and stores one bit per measurement must erase its memory continuously; what is the minimum power required, and how does it compare with the cell's metabolic power of about $10^{-12}\,\mathrm{W}$?

   **Answer** Each bit gives at most $k_{\mathrm{B}}T\ln 2 = 0.69\,k_{\mathrm{B}}T$, so $20/0.69 \approx 29$ bits per ATP. Erasing one bit per second costs at least $3.0\times10^{-21}\,\mathrm{W}$, nine orders of magnitude below the metabolic power: the Landauer bound itself is negligible for cells, and the real costs of sensing come from maintaining nonequilibrium signaling cycles at useful speed and precision (7.6.35, 7.6.38).

8. Using Example 2.3.4, estimate the hydrophobic free energy gained when a protein buries $50\,\mathrm{nm}^2$ of nonpolar surface on folding, and compare it with the typical net stability of a folded protein, $5$–$15\,k_{\mathrm{B}}T$. What opposes folding, and why is the net stability so small?

   **Answer** At $4$–$7\,k_{\mathrm{B}}T\,\mathrm{nm^{-2}}$, burying $50\,\mathrm{nm}^2$ gains $200$–$350\,k_{\mathrm{B}}T$. Folding is opposed by the loss of conformational entropy of the chain (a few $k_{\mathrm{B}}T$ per residue for a hundred or more residues) and by the loss of hydrogen bonds to water that are not fully replaced by internal ones. The net stability is a small difference of two large terms, which is why single mutations can unfold a protein and why proteins are only marginally stable, an advantage for turnover and conformational change (7.6.16).

9. Estimate the rate at which a single *E. coli* cell produces entropy, given that it oxidizes glucose at about $10^6$ molecules per second while growing aerobically ($\Delta G \approx -2900\,\mathrm{kJ\,mol^{-1}}$). Express the answer in $k_{\mathrm{B}}$ per second and in $\mathrm{W\,K^{-1}}$.

   **Answer** Free energy dissipated per glucose: $2.9\times10^6\,\mathrm{J\,mol^{-1}}/N_{\mathrm{A}} = 4.8\times10^{-18}\,\mathrm{J}$, about $1100\,k_{\mathrm{B}}T$ at $310\,\mathrm{K}$; part is stored in biomass, but most is eventually dissipated. Upper bound: $10^6\times4.8\times10^{-18}\,\mathrm{W} = 4.8\times10^{-12}\,\mathrm{W}$, an entropy production of $4.8\times10^{-12}/310 \approx 1.6\times10^{-14}\,\mathrm{W\,K^{-1}}$, or $1.6\times10^{-14}/1.38\times10^{-23} \approx 10^9\,k_{\mathrm{B}}$ per second. This must be exported, as heat and in the waste products, for the cell to remain in a steady state.

10. (Open) Design an experiment to decide whether the localization of a protein to one pole of a bacterium is equilibrium order (like binding to a curved membrane) or nonequilibrium order (like a dynamic pattern maintained by ATP hydrolysis).

    **Answer** Remove the free-energy supply and see whether the order persists: deplete ATP (with an uncoupler and an inhibitor of glycolysis, or in mutants unable to hydrolyze ATP or GTP in the relevant protein) and image the protein over time; equilibrium localization survives, a dissipative pattern decays. Complementary tests are fluorescence recovery after photobleaching (exchange continues at equilibrium but with no net flux) and searching for a directed cycle of states, for example by mutating the protein's nucleotide-hydrolysis site. The Min oscillation of 7.6.36 fails the first test (it stops without ATP), the polar localization of some proteins by membrane curvature passes it.
