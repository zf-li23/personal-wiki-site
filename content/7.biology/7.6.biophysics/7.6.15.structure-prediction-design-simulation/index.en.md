---
title: Structure Prediction, Design and Molecular Simulation
description: "Computation in structural biology. Potential energy surfaces and classical force fields (bonded and non-bonded terms, water models, periodic boundary conditions, Ewald summation, implicit solvent), molecular mechanics and QM/MM; molecular dynamics with the velocity Verlet integrator, time steps, constraints, thermostats and barostats, accessible time scales and coarse-grained models; Metropolis Monte Carlo, simulated annealing and replica exchange; free energies by umbrella sampling and WHAM, metadynamics, free-energy perturbation and thermodynamic integration; Markov state models and implied time scales; protein structure prediction from Anfinsen and Levinthal to statistical potentials, homology modeling, threading and fragment assembly, coevolution, Potts models and direct coupling analysis, and deep learning (AlphaFold2, RoseTTAFold, AlphaFold 3, language models) with confidence measures and limitations; RNA secondary structure by the Nussinov and Zuker algorithms, McCaskill's partition function and comparative analysis, RNA tertiary structure; docking of small molecules and proteins; protein design from directed evolution and rational design to Rosetta and generative models; RNA design; integrative structural biology with crosslinking, hydrogen-deuterium exchange and native mass spectrometry."
---

The experimental methods of the preceding chapters produce structures: an electron density, a set of distance restraints, a cryo-EM map. Computation does three further things with them. It *simulates*: given the atoms and the forces between them, it follows the motions of a molecule in time and computes the free energies that decide which states it occupies. It *predicts*: given only a sequence, it infers the structure the chain folds into. And it *designs*: given a desired structure or function, it finds a sequence that achieves it. The three rest on the same ideas, an energy function over conformations and an algorithm to explore it, and in the last decade they have been transformed by machine learning trained on the structures that experiment produced. This chapter develops the physics and the algorithms; the neural-network architectures themselves are treated in [4.7](/4.7), and the sequence analysis behind multiple alignments in the bioinformatics course.

The physical part (15.1–15.4) builds on statistical mechanics. A molecule at temperature $T$ visits its conformations with the **Boltzmann distribution** ([7.6.2](/7.6.2)); the **Langevin equation** and the **master equation** of [7.6.5](/7.6.5) describe its stochastic dynamics; the **Lennard-Jones potential** and the electrostatics of water of [7.6.6](/7.6.6) are the ingredients of force fields. Section 15.1 turns them into an energy function for every atom of a protein and its solvent; 15.2 integrates Newton's equations (molecular dynamics); 15.3 samples by Monte Carlo and computes free energies; 15.4 condenses long simulations into kinetic models. The predictive part (15.5–15.7) asks how a sequence determines a structure: by physics, by analogy with known structures, by the record of evolution in sequence families, and finally by deep learning (15.5), for RNA by dynamic programming (15.6), and for complexes by docking (15.7). Design inverts the problem (15.8), and integrative modeling combines computation with sparse experimental data (15.9). The folding problem itself, why and how chains find their native states, is the subject of the next chapter ([7.6.16](/7.6.16)); the overview in [7.1.6](/7.1.6#sec-6.6.5) is the starting point.

## 15.1. Energy Functions

### 15.1.1. From Quantum Mechanics to a Potential Energy Surface

The energy of a molecule is determined by the Schrödinger equation for its electrons and nuclei. Because nuclei are thousands of times heavier than electrons, the electrons adjust almost instantly to the nuclear positions (the Born–Oppenheimer approximation, [6.3.16](/6.3.16)), and the electronic energy as a function of the nuclear coordinates $\boldsymbol{R} = (\boldsymbol{r}_1, \dots, \boldsymbol{r}_N)$ is the **potential energy surface** $U(\boldsymbol{R})$ on which the nuclei move. For the nuclei of biomolecules quantum effects are small: the thermal de Broglie wavelength of a proton at $300\,\mathrm{K}$ is about $0.1\,\mathrm{nm}$, comparable with bond lengths, so hydrogen tunneling and zero-point energy matter in some enzymatic reactions, but heavier nuclei behave as classical particles. Structural biophysics therefore treats atoms as classical point masses moving on $U(\boldsymbol{R})$.

Computing $U$ from quantum mechanics is expensive. Even density functional theory, the cheapest accurate method, scales roughly as the cube of the number of electrons; a protein with $10^4$ atoms in water with $10^5$ atoms, evaluated $10^9$ times in a simulation, is out of reach. The solution is to replace $U$ by an analytic function fitted to quantum calculations and experiments.

### 15.1.2. Force Fields

**Definition 15.1.1 (Force Field)** A **force field** is an analytic approximation to the potential energy surface of a molecular system, a sum of simple terms that depend on the positions of a few atoms each, together with the parameters of these terms for every type of atom. Computing energies and their minima with a force field is called **molecular mechanics**.

The force fields used for proteins and nucleic acids (AMBER, CHARMM, OPLS-AA, GROMOS) share one functional form, the "class I" force field.

**Formula 15.1.1 (Class I Force Field)**

$$
\begin{aligned}
U(\boldsymbol{R}) ={}& \sum_{\text{bonds}} k_b(b - b_0)^2 + \sum_{\text{angles}} k_\theta(\theta - \theta_0)^2 + \sum_{\text{dihedrals}}\sum_n \frac{V_n}{2}\bigl[1 + \cos(n\phi - \delta_n)\bigr] + \sum_{\text{impropers}} k_\omega(\omega - \omega_0)^2 \\
&+ \sum_{i<j}\left\{4\varepsilon_{ij}\left[\left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12} - \left(\frac{\sigma_{ij}}{r_{ij}}\right)^{6}\right] + \frac{q_iq_j}{4\pi\varepsilon_0 r_{ij}}\right\}.
\end{aligned} \tag{15.1}
$$
The first line contains the *bonded* terms, between atoms connected by one, two or three covalent bonds: bond stretching, angle bending, rotation about bonds (torsion, periodic in the **torsion angle** $\phi$) and "improper" dihedrals that keep planar groups such as the peptide bond and aromatic rings planar. The second line contains the *non-bonded* terms between all other pairs: the **Lennard-Jones potential** for exchange repulsion and dispersion ([7.6.6](/7.6.6)) and the electrostatic interaction of fixed partial charges by **Coulomb's law**. Non-bonded interactions between atoms separated by three bonds are scaled down, since part of them is already in the torsion terms.

Each term has a physical meaning and a typical scale.

| Term | Typical parameters | Energy scale for thermal fluctuations |
|---|---|---|
| Bond (C–C) | $b_0 = 0.153\,\mathrm{nm}$, $k_b \approx 1.3\times10^5\,\mathrm{kJ\,mol^{-1}\,nm^{-2}}$ | $\sqrt{k_{\mathrm{B}}T/(2k_b)} \approx 3\,\mathrm{pm}$ fluctuation: bonds are nearly rigid |
| Angle (C–C–C) | $\theta_0 = 111^\circ$, $k_\theta \approx 260\,\mathrm{kJ\,mol^{-1}\,rad^{-2}}$ | $\approx 3^\circ$–$4^\circ$ fluctuation |
| Torsion | barriers $V_n$ of $1$–$20\,\mathrm{kJ\,mol^{-1}}$ | rotamer and backbone transitions on ps–ns scales; determine the **Ramachandran plot** |
| Lennard-Jones | $\varepsilon \approx 0.1$–$1\,\mathrm{kJ\,mol^{-1}}$, $\sigma \approx 0.3$–$0.4\,\mathrm{nm}$ | packing, van der Waals contacts |
| Coulomb | partial charges $\pm0.1$–$0.8\,e$ | **hydrogen bonds**, salt bridges; screened by water |

The **hydrogen bond** has no term of its own in modern force fields: it emerges from the electrostatic attraction between the partial charges of donor H and acceptor, kept from collapsing by the Lennard-Jones repulsion. The **hydrophobic effect** is not a term either: it emerges from the behavior of explicit water molecules around non-polar groups.

Parameters come from two sources. Equilibrium geometries and force constants are fitted to crystal structures, vibrational spectra and quantum calculations on small model compounds; partial charges are fitted to the electrostatic potential computed quantum mechanically around a molecule; torsion parameters and Lennard-Jones parameters are adjusted so that simulations reproduce measured densities and heats of vaporization of liquids, hydration free energies and, for proteins, NMR observables and the populations of helix and coil in peptides. Parameters are transferable within an *atom type* (an aliphatic carbon, a carbonyl oxygen), so a few hundred types describe all proteins. Small molecules such as drugs are handled by general force fields (GAFF, CGenFF) with automatically assigned types.

![The terms of a class I force field with representative parameters. A: bond stretching: the harmonic term and a Morse potential with the same curvature; the harmonic form cannot break bonds but is accurate for thermal fluctuations (k_B T ≈ 2.5 kJ/mol, dotted). B: angle bending. C: torsion about the central bond of butane: trans minimum, two gauche minima about 3 kJ/mol higher, and the cis barrier. D: the non-bonded terms between two atoms with partial charges ±0.25 e: Lennard-Jones, Coulomb in vacuum and Coulomb screened by a dielectric of relative permittivity 80; electrostatics dominates at long range in vacuum and is screened in water](./plots/force-field.py)

The class I form has known limitations. Bonds cannot break, so chemical reactions need quantum methods (15.1.4). Charges are fixed, so electronic polarization (the response of the electron cloud to the local field) is included only on average, by charges slightly larger than in vacuum; this fails at interfaces with very different dielectric environments and for multivalent ions and cation–$\pi$ interactions. *Polarizable force fields* (Drude oscillators, induced dipoles in AMOEBA) are more accurate and several times more expensive. And the parameters encode compromises: force fields of the 2000s overstabilized $\alpha$ helices or made disordered proteins too compact, errors corrected in later versions by refitting torsions and water–protein interactions against NMR data on **intrinsically disordered proteins**.

### 15.1.3. Water and Boundary Conditions

Biomolecules live in water, and water makes up most of the atoms in a simulation. Explicit water models (TIP3P, SPC/E, TIP4P/2005, OPC) represent each molecule by three or four rigid sites with partial charges and one Lennard-Jones center; they differ in how well they reproduce the density, dielectric constant ($\approx 80$), diffusion coefficient and structure of real water, and the choice of water model is coupled to the protein force field.

A finite droplet of water would be dominated by its surface. Simulations therefore use *periodic boundary conditions*: the system is placed in a box (cubic, or a truncated octahedron or rhombic dodecahedron that wastes less solvent around a globular protein) surrounded by infinitely many images of itself, so that a molecule leaving one face enters through the opposite face. The box must be large enough that a protein does not interact with its own images, typically leaving $1$–$1.5\,\mathrm{nm}$ of water around it. Lennard-Jones interactions decay fast and are truncated at about $1\,\mathrm{nm}$. Coulomb interactions decay as $1/r$, and truncating them produces serious artefacts; they are summed over all periodic images by *Ewald summation*, which splits the $1/r$ potential into a short-range part summed in real space and a smooth long-range part summed in Fourier space. In the particle-mesh Ewald method, charges are interpolated onto a grid and the Fourier part is computed with the **fast Fourier transform**, reducing the cost from $O(N^2)$ to $O(N\log N)$.

Where explicit water is too expensive, *implicit solvent* models replace it by a continuum. The electrostatic part of solvation is computed from the **Poisson–Boltzmann equation** ([7.6.6](/7.6.6)) or its fast approximation, the generalized Born model, which writes the solvation energy of each charge as a Born term with an effective radius that depends on how deeply the atom is buried; the non-polar part is taken proportional to the solvent-accessible surface area. Implicit solvent removes the friction and the slow relaxation of water, which speeds conformational sampling, but loses specific water molecules, which are often structurally important.

### 15.1.4. Energy Minimization, Molecular Mechanics and QM/MM

The simplest use of a force field is to find local minima of $U$, by **gradient descent** (steepest descent), conjugate gradients or quasi-Newton methods (L-BFGS). Since the force field is analytic, its gradient, the negative of the force on every atom, costs about as much as the energy. Minimization removes steric clashes from models built by hand, from homology models and from structures fitted into cryo-EM maps, and the energy and stereochemistry of a model are standard measures of its quality. Minimization finds the nearest local minimum, not the global one: the energy surface of a protein has astronomically many minima, and only sampling at finite temperature (15.2–15.3) explores it.

For chemical reactions in enzymes, the hybrid *QM/MM* method (Warshel and Levitt, 1976) treats the active site, a few tens of atoms whose bonds change, by quantum mechanics and the rest of the protein and solvent by a force field, with electrostatic coupling between the two. Martin Karplus, Michael Levitt and Arieh Warshel received the Nobel Prize in Chemistry in 2013 for the development of multiscale models of complex chemical systems. A newer approach trains neural networks on large sets of quantum calculations to predict energies and forces with nearly quantum accuracy at a small fraction of the cost (machine-learned potentials); being differentiable, they can be used in molecular dynamics directly.

## 15.2. Molecular Dynamics

### 15.2.1. The Method

**Definition 15.2.1 (Molecular Dynamics)** **Molecular dynamics** (MD) is the computation of the time evolution of a system of atoms by numerical integration of Newton's equations of motion,

$$
m_i\ddot{\boldsymbol{r}}_i = \boldsymbol{F}_i = -\nabla_{\boldsymbol{r}_i}U(\boldsymbol{R}), \qquad i = 1, \dots, N, \tag{15.2}
$$
with forces from a force field, starting from given positions and velocities; averages over the trajectory estimate thermodynamic quantities, and the trajectory itself shows the mechanism of motions.

The first MD simulations were of hard spheres (Alder and Wainwright, 1957) and liquid argon (Rahman, 1964); the first of a protein, the bovine pancreatic trypsin inhibitor for $9\,\mathrm{ps}$ in vacuum, was by McCammon, Gelin and Karplus (1977). If the dynamics is ergodic, time averages along a long trajectory equal ensemble averages, and MD computes the same equilibrium properties as statistical mechanics; but it also gives the dynamics: how fast a channel opens, the path by which a ligand leaves its pocket, the motions that couple distant sites in an allosteric protein.

### 15.2.2. Integrating the Equations of Motion

Newton's equations for $10^5$ coupled atoms must be integrated numerically with a time step $\Delta t$. The algorithm of choice is simple and has deep properties.

**Algorithm 15.2.1 (Velocity Verlet)** Given positions $\boldsymbol{r}(t)$, velocities $\boldsymbol{v}(t)$ and forces $\boldsymbol{F}(t)$, repeat:

1. $\boldsymbol{v}(t + \tfrac12\Delta t) = \boldsymbol{v}(t) + \tfrac{\Delta t}{2m}\boldsymbol{F}(t)$ (half kick);
2. $\boldsymbol{r}(t + \Delta t) = \boldsymbol{r}(t) + \Delta t\,\boldsymbol{v}(t + \tfrac12\Delta t)$ (drift);
3. compute the forces $\boldsymbol{F}(t + \Delta t)$ at the new positions;
4. $\boldsymbol{v}(t + \Delta t) = \boldsymbol{v}(t + \tfrac12\Delta t) + \tfrac{\Delta t}{2m}\boldsymbol{F}(t + \Delta t)$ (half kick).

One force evaluation per step, which is the expensive part. Eliminating the velocities gives the original Verlet (1967) form $\boldsymbol{r}(t + \Delta t) = 2\boldsymbol{r}(t) - \boldsymbol{r}(t - \Delta t) + \Delta t^2\boldsymbol{F}(t)/m$, with local error $O(\Delta t^4)$ in positions.

The *velocity Verlet algorithm* is time-reversible (running it backward with $-\Delta t$ retraces the trajectory) and symplectic: it preserves phase-space volume, as the exact Hamiltonian flow does. A consequence is that it exactly conserves a "shadow" energy that differs from the true energy by $O(\Delta t^2)$, so the energy fluctuates but does not drift over very long runs. Simple methods such as the explicit Euler method, which update positions and velocities from the forces at the beginning of the step only, are neither reversible nor symplectic, and their energy drifts systematically.

The time step is limited by the fastest motion. The stretching of bonds to hydrogen has a period of about $10\,\mathrm{fs}$ (wavenumber $3000\,\mathrm{cm^{-1}}$), and the step must be a fraction of the period: $\Delta t = 1\,\mathrm{fs}$. Constraining the lengths of bonds to hydrogen (algorithms SHAKE, LINCS) removes the fastest motion and allows $2\,\mathrm{fs}$; transferring mass from heavy atoms to their hydrogens ("hydrogen mass repartitioning") allows $4\,\mathrm{fs}$.

**Example 15.2.1** How much computing does a microsecond cost? At $\Delta t = 2\,\mathrm{fs}$, $1\,\mu\mathrm{s}$ is $5\times10^8$ steps. A membrane protein in a lipid bilayer with water has about $10^5$ atoms; with cutoffs and particle-mesh Ewald a force evaluation costs some $10^7$–$10^8$ floating-point operations, so a microsecond needs about $10^{16}$–$10^{17}$ operations. A modern graphics processor runs such a system at a few hundred nanoseconds per day; special-purpose machines (Anton, D. E. Shaw Research) reach tens of microseconds per day and have simulated the folding of small fast-folding proteins to their native states, repeatedly, in millisecond-long trajectories (Lindorff-Larsen and colleagues, 2011).

![Molecular dynamics of a two-dimensional Lennard-Jones fluid (64 particles, reduced units). A: final positions and the trajectories of four particles over 1000 steps. B: deviation of the total energy from its initial value (log scale): with velocity Verlet it fluctuates without drift and grows as Δt², while the explicit Euler method drifts away within a few time units. C: the kinetic temperature in a microcanonical run and with a Langevin thermostat set to T = 0.7, which brings the system to the target temperature and keeps it there with canonical fluctuations](./plots/md-lj.py)

### 15.2.3. Thermostats and Barostats

Newton's equations conserve energy: they sample the microcanonical ensemble (fixed $N$, $V$, $E$). Experiments are done at constant temperature and pressure. A *thermostat* couples the system to a heat bath, modifying the equations of motion so that they sample the canonical distribution at a chosen temperature.

- The *Langevin thermostat* adds to each atom the friction and random force of the **Langevin equation** ([7.6.5](/7.6.5)), $m\dot{\boldsymbol{v}} = \boldsymbol{F} - m\gamma\boldsymbol{v} + \boldsymbol{\xi}(t)$ with $\langle\xi_\alpha(t)\xi_\beta(t')\rangle = 2m\gamma k_{\mathrm{B}}T\delta_{\alpha\beta}\delta(t - t')$, the strength fixed by the **fluctuation–dissipation theorem**. It samples the canonical ensemble exactly (for small time steps) but perturbs the dynamics; with small friction $\gamma$, kinetics are nearly unaffected.
- The *Nosé–Hoover thermostat* adds a dynamical friction variable coupled to the kinetic energy, giving deterministic dynamics that sample the canonical ensemble; chains of such variables avoid non-ergodic behavior.
- Velocity-rescaling thermostats rescale velocities toward the target. The original Berendsen scheme is fast at equilibrating but suppresses the fluctuations of the kinetic energy and does not produce the canonical ensemble; the stochastic variant of Bussi, Donadio and Parrinello (2007) does.

A barostat likewise lets the box volume fluctuate to keep the pressure (Parrinello–Rahman, Monte Carlo barostats). Production simulations of biomolecules are run at constant $N$, $p$, $T$.

### 15.2.4. Time Scales and Coarse-Grained Models

Biomolecular motions span many decades of time.

| Motion | Time scale | Accessible by all-atom MD |
|---|---|---|
| Bond vibrations | $10\,\mathrm{fs}$ | yes (constrained) |
| Side-chain rotamer jumps, loop fluctuations | $\mathrm{ps}$–$\mathrm{ns}$ | routinely |
| Helix formation, small-ligand unbinding from shallow sites | $\mathrm{ns}$–$\mu\mathrm{s}$ | routinely to with effort |
| Folding of small fast-folding proteins, domain motions | $\mu\mathrm{s}$–$\mathrm{ms}$ | with special hardware or many parallel runs |
| Folding of typical proteins, drug residence times, channel gating cycles, enzymatic turnover | $\mathrm{ms}$–$\mathrm{s}$ and longer | only with enhanced sampling (15.3) or kinetic models (15.4) |

The gap between what happens and what can be simulated is closed in three ways: by enhanced sampling, by building kinetic models from many short simulations, and by simplifying the model itself. **Coarse-graining** ([7.6.1](/7.6.1)) groups several atoms into one interaction site: the Martini model maps about four heavy atoms (and associated hydrogens) to one bead and is widely used for membranes and large assemblies; models with one bead per residue, including structure-based (Gō) models whose energy function rewards only native contacts, capture the topology of folding at a fraction of the cost. Coarse-graining smooths the energy surface, so coarse-grained dynamics is faster than real dynamics by a factor that is not uniform; it is used for structures and mechanisms, not for absolute rates. Multiscale approaches back-map selected coarse-grained configurations to atomic detail.

## 15.3. Monte Carlo and Free Energies

### 15.3.1. Metropolis Monte Carlo

Equilibrium properties do not need realistic dynamics, only correct sampling of the Boltzmann distribution. A Markov chain whose **stationary distribution** is the Boltzmann distribution produces such samples. The **Metropolis algorithm** ([3.5.9](/3.5.9)) proposes a random change of conformation (move an atom, rotate a torsion, exchange a fragment) and accepts it with probability $\min\{1, \exp(-\Delta U/k_{\mathrm{B}}T)\}$, which satisfies the **detailed balance condition** with respect to $\mathrm{e}^{-U/k_{\mathrm{B}}T}$ and is therefore an instance of **Markov chain Monte Carlo** ([7.6.2](/7.6.2)). Compared with MD, Monte Carlo can make large, unphysical moves (swap a side chain rotamer, insert a fragment of backbone from a library, exchange particles with a reservoir), needs no forces and no time step, but has no time axis; it is the method of choice for discrete models (lattice proteins in [7.6.16](/7.6.16), rotamer packing in design) and for structure prediction by fragment assembly (15.5.3).

### 15.3.2. The Global Minimum: Annealing and Replica Exchange

Prediction and design must find the lowest minimum of a rugged energy surface. At low temperature a sampler is trapped near its start; at high temperature it explores but does not concentrate in the low minima. **Simulated annealing** ([7.6.9](/7.6.9#sec-9.11.2)) combines the two by lowering the temperature slowly during the run: barriers are crossed while $T$ is high, and the system settles in a deep basin as $T$ falls. In MD the temperature is lowered through the thermostat; in Monte Carlo it enters only the acceptance probability. A logarithmically slow schedule guarantees convergence to the global minimum in principle, but practical schedules can be trapped, and they are trapped in a characteristic way: at intermediate temperatures the free energy, not the energy, decides, and a broad basin of many conformations (high entropy) can capture the system before a narrower, deeper basin wins.

*Replica exchange* (parallel tempering) runs $M$ copies of the system simultaneously at temperatures $T_1 < T_2 < \cdots < T_M$ and periodically attempts to exchange the configurations of neighbors $i$ and $j$, accepting with probability

$$
\min\left\{1, \exp\bigl[(\beta_i - \beta_j)(U_i - U_j)\bigr]\right\}, \qquad \beta = 1/k_{\mathrm{B}}T, \tag{15.3}
$$
which preserves the Boltzmann distribution at every temperature. A configuration diffuses in temperature: it crosses barriers at high temperature and returns to be sampled correctly at low temperature. Neighboring temperatures must be close enough that their energy distributions overlap, so the number of replicas grows as the square root of the number of degrees of freedom; variants exchange Hamiltonians (scaled interactions of a region) rather than temperatures.

![Metropolis Monte Carlo and simulated annealing on a rugged two-dimensional energy landscape with a deep global minimum (star) and a broader, shallower basin. A: at low temperature the walker is trapped near its starting point; at high temperature it wanders over the whole surface without settling. B: an annealing run explores at high temperature and comes to rest in the global minimum as the temperature falls (colour shows time). C: energies of 30 annealing runs with the exponential temperature schedule (dashed): about half reach the global minimum, the others are captured by the broader basin; a rapid quench never does](./plots/annealing.py)

### 15.3.3. Free Energies and Enhanced Sampling

Which state a molecule occupies, how tightly a drug binds, how high a barrier is: these are questions about free energies, not energies. Along a chosen reaction coordinate $\xi(\boldsymbol{R})$ (a distance, an angle, a number of native contacts), the *potential of mean force* is

$$
G(\xi) = -k_{\mathrm{B}}T\ln p(\xi) + \mathrm{const}, \qquad p(\xi) = \frac{\int\delta(\xi(\boldsymbol{R}) - \xi)\,\mathrm{e}^{-U(\boldsymbol{R})/k_{\mathrm{B}}T}\,\mathrm{d}\boldsymbol{R}}{\int\mathrm{e}^{-U(\boldsymbol{R})/k_{\mathrm{B}}T}\,\mathrm{d}\boldsymbol{R}}, \tag{15.4}
$$
the free energy profile on which, in the simplest picture, the motion along $\xi$ is diffusion in the sense of Kramers ([7.6.5](/7.6.5)). An unbiased simulation samples $p(\xi)$ only where it is not exponentially small: a barrier of $10\,k_{\mathrm{B}}T$ is visited $\mathrm{e}^{-10} \approx 5\times10^{-5}$ as often as the minimum. Enhanced-sampling methods bias the simulation so that it samples the barrier, then remove the bias.

*Umbrella sampling* (Torrie and Valleau, 1977) runs a series of simulations ("windows") $i = 1, \dots, K$, each with a harmonic bias $w_i(\xi) = \frac{k}{2}(\xi - \xi_i)^2$ that holds the system near $\xi_i$. Window $i$ samples the biased distribution $p_i^{\mathrm{b}}(\xi) \propto p(\xi)\mathrm{e}^{-w_i(\xi)/k_{\mathrm{B}}T}$, so $p(\xi) \propto p_i^{\mathrm{b}}(\xi)\mathrm{e}^{w_i(\xi)/k_{\mathrm{B}}T}$ up to an unknown constant for each window. The constants are found by requiring the windows to agree where they overlap.

**Algorithm 15.3.1 (Weighted Histogram Analysis Method)** Let $n_i(\xi)$ be the histogram of window $i$, with $N_i$ samples, and let $f_i$ be the dimensionless free energy of window $i$ (in units of $k_{\mathrm{B}}T$, with $b_i = w_i/k_{\mathrm{B}}T$). Iterate to self-consistency

$$
p(\xi) = \frac{\sum_i n_i(\xi)}{\sum_i N_i\,\mathrm{e}^{f_i - b_i(\xi)}}, \qquad \mathrm{e}^{-f_i} = \sum_\xi p(\xi)\,\mathrm{e}^{-b_i(\xi)}. \tag{15.5}
$$
The first equation is the maximum-likelihood combination of all histograms; the second normalizes each biased distribution. The result is the unbiased $p(\xi)$, hence $G(\xi)$ by Eq. (15.4).

*Metadynamics* (Laio and Parrinello, 2002) builds the bias during a single simulation: small Gaussian hills are added at the current value of $\xi$ at regular intervals, filling the free-energy minima like sand until the system can move freely; the accumulated bias then approximates $-G(\xi)$ (in the well-tempered variant, a known fraction of it). Both methods need a good reaction coordinate; if a slow motion is not captured by $\xi$, the profile is wrong however long one samples.

Free-energy differences between chemically different states, such as the binding of two related drugs, are computed by *alchemical* methods. Free-energy perturbation (Zwanzig, 1954) is based on the exact identity

$$
\Delta G_{A\to B} = -k_{\mathrm{B}}T\ln\left\langle\exp\left[-\frac{U_B - U_A}{k_{\mathrm{B}}T}\right]\right\rangle_A, \tag{15.6}
$$
an average over configurations sampled in state $A$. It converges only when $A$ and $B$ overlap, so the transformation is broken into many small steps along a coupling parameter $\lambda$ that turns one molecule into the other (or a ligand into nothing); thermodynamic integration computes $\Delta G = \int_0^1\langle\partial U/\partial\lambda\rangle_\lambda\,\mathrm{d}\lambda$ instead. Closing a thermodynamic cycle (transform ligand $A$ into $B$ in the binding site and in water) gives relative binding free energies to within about $4\,\mathrm{kJ\,mol^{-1}}$ for well-behaved systems, accurate enough to guide drug optimization. The nonequilibrium analogue of Eq. (15.6), the Jarzynski equality, connects free energies to work in pulling experiments ([7.6.17](/7.6.17)).

![Umbrella sampling and WHAM on a double well with a barrier of about 6 k_B T (overdamped Brownian dynamics). A: an unbiased run started in the left well never crosses and gives the free energy only there (grey squares); fifteen harmonically biased windows combined by WHAM reproduce the exact profile across the barrier and in the second well (red). B: the histograms of the biased windows, which must overlap](./plots/umbrella.py)

## 15.4. Markov State Models

A single long trajectory explores slowly and its statistics converge slowly. Many short simulations, run in parallel, explore faster, but how are they combined into a description of the long-time kinetics? The answer is to divide conformation space into many small regions and to model the transitions between them as a Markov chain.

**Definition 15.4.1 (Markov State Model)** Let conformation space be partitioned into $n$ disjoint microstates, and let $T_{ij}(\tau)$ be the probability that a system in microstate $i$ is found in microstate $j$ a lag time $\tau$ later, estimated from simulations by counting transitions. If $\tau$ is long enough that the next state depends only on the current one, the evolution of the state populations $\boldsymbol{p}(t)$ (a row vector) is

$$
\boldsymbol{p}(t + k\tau) = \boldsymbol{p}(t)\,T(\tau)^k, \tag{15.7}
$$
and the **Markov chain** with transition matrix $T(\tau)$ is a **Markov state model** (MSM) of the dynamics.

The MSM is a discrete-time version of the **master equation** of [7.6.5](/7.6.5): $T(\tau) = \exp(K\tau)$ for a rate matrix $K$. Its stationary distribution $\boldsymbol{\pi}$ ($\boldsymbol{\pi}T = \boldsymbol{\pi}$) gives equilibrium populations, hence free energies of states $G_i = -k_{\mathrm{B}}T\ln\pi_i$. Its eigenvalues give the kinetics. For dynamics in equilibrium, detailed balance $\pi_iT_{ij} = \pi_jT_{ji}$ makes $T$ similar to a symmetric matrix, with real eigenvalues $1 = \lambda_1 > \lambda_2 \ge \cdots$; the left eigenvectors $\boldsymbol{\psi}_k$ decompose any relaxation,

$$
\boldsymbol{p}(k\tau) = \boldsymbol{\pi} + \sum_{m \ge 2} c_m\lambda_m^k\boldsymbol{\psi}_m, \qquad t_m = -\frac{\tau}{\ln\lambda_m}, \tag{15.8}
$$
where $t_m$ is the *implied time scale* of process $m$: the relaxation time of the $m$-th slowest mode, which redistributes population between the regions where $\boldsymbol{\psi}_m/\boldsymbol{\pi}$ is positive and those where it is negative.

Two checks make an MSM trustworthy. If the model is Markovian, the implied time scales do not depend on the lag time; plotting $t_m$ against $\tau$ and choosing $\tau$ beyond the point where they level off is the standard test. The Chapman–Kolmogorov test compares $T(\tau)^k$ with $T(k\tau)$ estimated directly. A good partition into microstates matters: modern pipelines first project the trajectories onto slow collective coordinates (time-lagged independent component analysis, a variational principle for the slowest modes), cluster in that space into hundreds of microstates, and then lump them into a few metastable macrostates using the slow eigenvectors. Transition path theory, built on the *committor* (the probability of reaching state $B$ before $A$ from each microstate), gives the fluxes and the dominant pathways between states. MSMs built from thousands of short simulations, including the distributed computing project Folding@home, have described protein folding, the activation of kinases and receptors, and the binding of ligands at time scales of milliseconds.

![A Markov state model built from 20 short Brownian-dynamics trajectories in a triple-well potential. A: the potential with wells A, B, C and one trajectory (inset). B: the implied time scales of the two slowest processes against the lag time level off once the lag exceeds the fast motion within the wells (the Markovian regime); the dotted line t = τ marks the limit below which a process cannot be resolved. C: the stationary distribution of the model agrees with the Boltzmann distribution, and the second and third eigenvectors (divided by it, dashed) are nearly constant within each well and change sign between the wells that exchange population in each slow process](./plots/msm.py)

## 15.5. Protein Structure Prediction

### 15.5.1. The Problem

Christian Anfinsen's experiments on ribonuclease ([7.1.6](/7.1.6#sec-6.1.2)) established the **thermodynamic hypothesis**: for small globular proteins the native structure is the state of lowest free energy under physiological conditions, determined by the amino acid sequence. In principle, structure follows from sequence by minimizing a free energy. In practice two difficulties arise. The search: a chain of 100 residues with three conformations per residue has $3^{100} \approx 5\times10^{47}$ backbone conformations, which could not be enumerated even at $10^{13}$ per second in the age of the universe (**Levinthal's paradox**, whose resolution by funnel-shaped energy landscapes is discussed in [7.6.16](/7.6.16)). And the energy: the native state is typically only $20$–$60\,\mathrm{kJ\,mol^{-1}}$ more stable than the unfolded ensemble, a small difference of large terms, so the energy function must be very accurate to identify it.

Meanwhile sequences accumulate far faster than structures: the **Protein Data Bank** holds about $2\times10^5$ experimental structures, the sequence databases billions of sequences. Prediction methods are assessed in the blind Critical Assessment of protein Structure Prediction (CASP), organized every two years since 1994 by John Moult and colleagues: participants predict structures that have been determined but not yet released, and predictions are compared with experiment by measures such as the global distance test (GDT, the percentage of residues within distance cutoffs after superposition, $0$–$100$) and the local distance difference test (lDDT), which is superposition-free.

### 15.5.2. Physical and Statistical Energy Functions

All-atom force fields with explicit solvent can, in long simulations, fold small proteins (15.2.2), but they are too slow and not yet accurate enough to rank the decoys of a general prediction. Prediction methods long relied instead on energy functions derived from the database of known structures.

**Formula 15.5.1 (Statistical Potential)** If the conformations observed in native proteins were Boltzmann-distributed with respect to a free energy $E$, the probability $p(r)$ of finding a pair of atom (or residue) types $a, b$ at distance $r$ in native structures, compared with its probability $p_{\mathrm{ref}}(r)$ in a reference state without specific interactions, would give

$$
E_{ab}(r) = -k_{\mathrm{B}}T\ln\frac{p_{ab}(r)}{p_{ab,\mathrm{ref}}(r)}. \tag{15.9}
$$
The total energy of a model is the sum over pairs. Potentials of this "inverse Boltzmann" kind are called *statistical potentials* or knowledge-based potentials.

The assumption is not literally true (native proteins are not a thermal ensemble of one molecule, and the counts mix many proteins), and the result depends strongly on the reference state: an ideal-gas-like reference (as in the potential DFIRE) and the uniform distribution of contacts give different potentials. Statistical potentials nevertheless capture packing, burial of hydrophobic residues and hydrogen-bonding geometry efficiently, and they were the energy functions of the most successful pre-deep-learning methods, including Rosetta, which combines physical terms (Lennard-Jones, solvation, hydrogen bonds) with statistical ones for backbone torsions and rotamers.

### 15.5.3. Templates and Fragments

Evolution conserves structure more than sequence: proteins whose sequences are more than about $30\,\%$ identical almost always share a fold, and many with $15$–$25\,\%$ identity do too (the "twilight zone"). Only a limited number of folds exist: the classification SCOPe distinguishes about $1\,200$–$1\,300$ folds and $2\,000$ superfamilies among all known structures. Two methods exploit this.

- *Homology modeling* (comparative modeling) aligns the target sequence to a homologous protein of known structure (the template), copies the aligned backbone, and builds the loops and side chains that differ, satisfying spatial restraints derived from the template (the program MODELLER builds models by optimizing such restraints, much as NMR structures are computed from distance restraints, [7.6.13](/7.6.13)). The accuracy is set by the sequence identity and the quality of the alignment.
- *Threading* (fold recognition) searches the library of known folds for one that is compatible with the target sequence even when the sequence similarity is undetectable, by "threading" the sequence onto each backbone and scoring the fit with environment-dependent statistical potentials (buried or exposed, helix or strand).

When no template exists, *fragment assembly* (Rosetta, Simons and Baker, 1997) builds the structure from short pieces. For every window of 3 and 9 residues of the target, the database supplies 25–200 fragments of known proteins with similar local sequence and predicted secondary structure; local sequence determines local structure only loosely, but the library captures the possibilities. A Monte Carlo search, starting from an extended chain, repeatedly replaces the backbone torsions of a random window by those of one of its fragments and accepts the move by the Metropolis criterion with a coarse statistical energy, with simulated annealing; thousands of independent runs give decoys, which are refined in all-atom detail, and the lowest-energy clusters are the predictions. Fragment assembly predicted structures of small proteins of new folds to about $0.4\,\mathrm{nm}$ accuracy in CASP, but rarely larger ones: the search does not scale.

### 15.5.4. Coevolution

A protein family is a record of an evolutionary experiment. If two residues are in contact in the structure, a mutation of one that disturbs the contact (replacing a small residue by a large one, or reversing a charge) is often compensated by a mutation of the other. In a multiple sequence alignment (MSA) of the family, the two columns are then correlated. Such *coevolution* of residue pairs, read in reverse, predicts contacts from sequences alone.

The obvious measure of correlation between columns $i$ and $j$ is their mutual information

$$
\mathrm{MI}_{ij} = \sum_{a, b}f_{ij}(a, b)\ln\frac{f_{ij}(a, b)}{f_i(a)f_j(b)},
$$
with $f_i(a)$ the frequency of amino acid $a$ in column $i$ and $f_{ij}(a, b)$ the frequency of the pair. It fails for two reasons. Correlations are transitive: if $i$ contacts $j$ and $j$ contacts $k$, then $i$ and $k$ are correlated without being in contact. And sequences are related by phylogeny, so columns are correlated by shared ancestry. A global statistical model separates direct from indirect correlations.

**Definition 15.5.1 (Potts Model of a Protein Family)** The *Potts model* of a family of aligned sequences of length $L$ over an alphabet of $q$ symbols (20 amino acids and a gap) is the probability distribution

$$
\mathbb{P}(\boldsymbol{s}) = \frac{1}{Z}\exp\Bigl[\sum_i h_i(s_i) + \sum_{i<j}J_{ij}(s_i, s_j)\Bigr], \qquad \boldsymbol{s} = (s_1, \dots, s_L), \tag{15.10}
$$
with fields $h_i$ and couplings $J_{ij}$ chosen so that its single-site and pair frequencies equal those of the alignment. It is the maximum-entropy distribution with these constraints (the **maximum entropy principle** of [7.6.2](/7.6.2)); for $q = 2$ it is the **Ising model** of [7.6.4](/7.6.4).

*Direct coupling analysis* (DCA; Weigt, White, Szurmant, Hoch and Hwa, 2009; Morcos and colleagues, 2011) infers the couplings and ranks residue pairs by their strength, usually the Frobenius norm $\lVert J_{ij}\rVert$ of the $q\times q$ coupling matrix in a gauge where rows and columns sum to zero, corrected by the average-product correction (APC) that removes a background proportional to the overall coupling of each site. Inference is hard because $Z$ is a sum over $q^L$ sequences. In the mean-field approximation, the couplings are the negative inverse of the connected correlation matrix,

$$
J_{ij}(a, b) \approx -\left(C^{-1}\right)_{ia, jb}, \qquad C_{ia, jb} = f_{ij}(a, b) - f_i(a)f_j(b), \tag{15.11}
$$
a matrix of dimension $L(q - 1)$ (one state per site is dropped because frequencies sum to one); the inversion is what removes the indirect correlations, just as partial correlations do in a Gaussian model. Pseudo-likelihood maximization (plmDCA) is more accurate. Both need deep alignments: as a rule of thumb, an effective number of sequences (after down-weighting close relatives) of at least $5L$.

Contacts alone suffice to fold a protein: with the top $L$–$2L$ predicted contacts as distance restraints, simulated annealing produces correct folds (EVfold, Marks and colleagues, 2011). Coevolution predicted the structures of membrane proteins and of hundreds of families without templates, and coupling between residues of different proteins predicts interfaces of complexes when interacting pairs can be matched in genomes (for example, operon neighbors in bacteria). The same principle applies to RNA (15.6.4), where it was used first.

![Contacts from coevolution in a toy Potts model (30 sites, 4 residue types, 36 contacts, 800 sampled sequences). A: true contacts (grey) and the top 36 predictions by direct coupling analysis (upper triangle) and by mutual information (lower triangle); filled symbols are correct, open symbols wrong. B: the precision of the top-ranked pairs: DCA, which removes correlations transmitted along chains of contacts, is consistently more precise than mutual information; both fall once the number of predictions exceeds the number of true contacts](./plots/dca.py)

### 15.5.5. Deep Learning and AlphaFold

From 2016 the analysis of coevolution was taken over by **deep learning**. Jinbo Xu and colleagues (RaptorX-Contact) treated the coupling matrix of an alignment as an image of $L\times L$ pixels with many channels and trained deep residual **convolutional neural networks** on known structures to predict contact maps, nearly doubling the precision of top contacts in CASP12–13. AlphaFold (DeepMind, CASP13, 2018) predicted distributions of distances rather than contacts, converted them into a smooth potential and minimized it by gradient descent. Prediction was still a two-step process: networks predicted geometry, and a separate search built the structure.

**Definition 15.5.2 (AlphaFold)** **AlphaFold** is a family of deep neural networks for protein structure prediction developed by DeepMind; AlphaFold2 (2020–2021) predicts the three-dimensional coordinates of all heavy atoms of a protein chain directly from its sequence, a multiple sequence alignment of its homologs and optional structural templates, end to end, together with estimates of its own accuracy.

AlphaFold2's architecture embodies physical and evolutionary ideas. Its trunk, the Evoformer (48 blocks), maintains two representations: an MSA representation (one vector per sequence and residue) and a pair representation (one vector per residue pair, which plays the role of a distance map). Attention along rows and columns of the MSA exchanges information between residues and sequences; the outer product of MSA columns transfers coevolutionary information into the pair representation; "triangle" updates enforce geometric consistency among triples of residues, the way distances $d_{ij}$, $d_{jk}$ and $d_{ik}$ must satisfy the triangle inequality; and the pair representation biases the attention over the MSA. The structure module (8 blocks) treats each residue as a rigid body, a frame with a rotation and a translation, initially all at the origin, and moves the frames with an attention mechanism that is invariant to global rotations and translations of the whole structure (invariant point attention), then places side chains by predicted torsion angles. The network is trained against experimental structures with a loss that compares atom positions in the local frames of all residues (frame-aligned point error), and its output is fed back into its input three times (recycling).

![The flow of information in AlphaFold2 (schematic). Sequence and structure databases supply a multiple sequence alignment and templates; the Evoformer refines an MSA representation and a pair representation that exchange information in every block; the structure module moves rigid residue frames by invariant point attention; the predicted structure, with per-residue confidence (pLDDT) and predicted aligned error (PAE), is recycled three times](./plots/alphafold.py)

In CASP14 (2020) AlphaFold2 reached a median GDT of about 92 across targets, an accuracy comparable to experimental structures for most single domains; Demis Hassabis and John Jumper received the Nobel Prize in Chemistry in 2024 for it, together with David Baker for protein design (15.8). The AlphaFold database now contains predictions for more than $2\times10^8$ proteins, nearly every known sequence. RoseTTAFold (Baek and colleagues, 2021) reached similar accuracy with a three-track network (sequence, distance and coordinates); AlphaFold-Multimer extended prediction to protein complexes, and AlphaFold 3 (2024) and RoseTTAFold All-Atom to complexes with nucleic acids, small molecules, ions and modified residues, replacing the structure module by a diffusion model that generates atom coordinates from noise. Protein language models (ESM-2, ESMFold), trained only on sequences to predict masked residues, learn enough about structure to predict it from a single sequence, less accurately but much faster, without an alignment.

Prediction comes with confidence. The *predicted local distance difference test* (pLDDT, $0$–$100$) estimates for each residue how well its local environment is predicted; above $90$ the backbone and most side chains are reliable, below $50$ the region is usually disordered or unstructured in isolation, which makes pLDDT one of the best predictors of **intrinsically disordered proteins**. The predicted aligned error (PAE) estimates the error in the position of residue $j$ when the structure is superposed on residue $i$, which reveals whether two domains are placed reliably relative to each other. For the human proteome, about $58\,\%$ of residues are predicted with pLDDT above $70$ and $36\,\%$ above $90$ (Tunyasuvunakool and colleagues, 2021).

The limits are as important as the successes. AlphaFold predicts one structure, usually the most common state in the PDB, not the ensemble of conformations a protein visits or the change upon binding a ligand; it does not reliably predict the effect of point mutations on stability or the structures of designed sequences without homologs as well as those of natural families; it needs deep alignments for its best accuracy, so orphan proteins and fast-evolving viral proteins are harder; and its knowledge comes from the structures that experiment produced, so it extends rather than replaces them. It is a powerful learned model of the sequence–structure relation, not a simulation of folding: it says what a protein folds into, not how (the subject of [7.6.16](/7.6.16)). Its predictions are now routinely used as starting models for crystallographic molecular replacement ([7.6.10](/7.6.10)), for fitting into cryo-EM maps ([7.6.14](/7.6.14)) and for template matching in tomograms.

## 15.6. RNA Structure Prediction

### 15.6.1. Secondary Structure and the Nearest-Neighbor Model

RNA folds hierarchically: base pairing forms the secondary structure, helices and loops, which is largely stable on its own and is then arranged into a tertiary structure by weaker interactions and $\ce{Mg^2+}$ ions ([7.6.7](/7.6.7)). Because secondary structure accounts for most of the folding free energy and is often conserved in evolution, predicting it is useful by itself.

A secondary structure is a set of base pairs $(i, j)$, $i < j$, Watson–Crick (G–C, A–U) or wobble (G–U), such that each nucleotide pairs at most once and no two pairs cross: if $(i, j)$ and $(k, l)$ are pairs with $i < k$, then either $k > j$ or $l < j$. Crossing pairs form pseudoknots, which occur in real RNAs (in telomerase RNA, riboswitches and frameshifting signals) but are excluded from the standard algorithms, because their exclusion makes the problem decompose into independent subproblems. A secondary structure is written in *dot-bracket notation*: an opening parenthesis for the $5'$ partner of a pair, a closing one for the $3'$ partner, a dot for an unpaired nucleotide; non-crossing pairs nest like parentheses.

The free energy of a structure is not a sum over base pairs but over *loops*: stacked pairs, hairpin loops, bulges, internal loops and multiloops. In the nearest-neighbor model (Tinoco, Turner and colleagues), each stack of two adjacent base pairs contributes a free energy that depends on both pairs (for example $-3.3\,\mathrm{kcal\,mol^{-1}}$, or $-13.8\,\mathrm{kJ\,mol^{-1}}$, for $5'$-GC-$3'$/$3'$-CG-$5'$ at $37\,^\circ\mathrm{C}$), and each loop a destabilizing free energy that grows with its size, mostly entropic; the parameters (the "Turner 2004" set) were measured by optical melting of hundreds of short duplexes and hairpins. Stacking, not hydrogen bonding, dominates: an isolated base pair is not stable, and helices need at least about three stacked pairs.

### 15.6.2. Dynamic Programming: Nussinov and Zuker

The non-crossing structure makes secondary structure prediction an exact optimization by **dynamic programming** ([4.1.13](/4.1.13)). The idea is seen most clearly in Nussinov's algorithm (Nussinov and Jacobson, 1980), which maximizes the number of base pairs, or more generally minimizes a sum of pair energies.

**Algorithm 15.6.1 (Nussinov Algorithm)** For a sequence $x_1, \dots, x_n$, let $E(i, j)$ be the minimum energy of a secondary structure of the subsequence $x_i \dots x_j$, with pair energies $e(i, k) < 0$ for allowed pairs and hairpin loops of at least three nucleotides. Initialize $E(i, j) = 0$ for $j - i < 4$, and for increasing lengths compute

$$
E(i, j) = \min\Bigl\{E(i + 1, j),\ \min_{\substack{i + 4 \le k \le j \\ (i, k)\text{ allowed}}}\bigl[e(i, k) + E(i + 1, k - 1) + E(k + 1, j)\bigr]\Bigr\}. \tag{15.12}
$$
Either nucleotide $i$ is unpaired, or it pairs with some $k$, which splits the rest into the parts inside and outside the pair. The optimum of the whole sequence is $E(1, n)$, and the structure is recovered by tracing back which alternative gave each minimum. The table has $O(n^2)$ entries, each computed in $O(n)$ time: $O(n^3)$ time and $O(n^2)$ memory.

The recursion works because non-crossing pairs make the inside and outside of a pair independent. Zuker's algorithm (Zuker and Stiegler, 1981) uses the same principle with the loop-based nearest-neighbor energies, keeping several tables (for subsequences closed by a pair, inside multiloops, and so on); it is implemented in Mfold, RNAfold (ViennaRNA) and RNAstructure, and predicts on average about $70\,\%$ of the base pairs of RNAs up to a few hundred nucleotides correctly, less for longer ones. The *minimum free energy* structure is only the single best structure, and the energy differences between alternatives are often within the uncertainty of the parameters.

### 15.6.3. The Partition Function and Base-Pair Probabilities

At temperature $T$ an RNA is an ensemble of structures, each with probability proportional to $\exp(-G/k_{\mathrm{B}}T)$. McCaskill (1990) observed that replacing $\min$ by sum and energies by Boltzmann factors in the recursion gives the **partition function**:

$$
Z(i, j) = Z(i + 1, j) + \sum_{k}\mathrm{e}^{-e(i, k)/k_{\mathrm{B}}T}\,Z(i + 1, k - 1)\,Z(k + 1, j), \tag{15.13}
$$
with $Z = 1$ for empty and too-short subsequences; this works only because each structure is generated exactly once by the decomposition. From $Z$ follow the ensemble free energy $-k_{\mathrm{B}}T\ln Z(1, n)$ and, with a second "outside" recursion, the probability $P_{ij}$ of every base pair in the ensemble. Alternatively, structures can be drawn from the Boltzmann distribution by stochastic traceback (Ding and Lawrence, 2003): at each step choose the alternative of Eq. (15.13) with probability proportional to its term. Base-pair probabilities show which helices are well determined and which are not, and the maximum expected accuracy structure built from them is usually more accurate than the minimum free energy structure. The same machinery computes the probability that a site is unpaired, which determines its accessibility to microRNAs, ribosomes or antisense oligonucleotides.

![RNA secondary structure by dynamic programming in a simple model (pair energies G–C −3, A–U −2, G–U −1 k_B T; hairpin loops of at least 3 nt). A: the matrix E(i, j) of Eq. (15.12), filled from the diagonal outward; the optimum of the whole sequence is in the upper right corner. B: the optimal structure as an arc diagram and in dot-bracket notation. C: base-pair probabilities from 2000 structures sampled from the Boltzmann ensemble with the partition function of Eq. (15.13) (upper triangle) and the optimal pairs (lower triangle): the optimal helices dominate the ensemble, but alternative pairings have appreciable probability](./plots/nussinov.py)

### 15.6.4. Comparative Analysis and Other Data

The secondary structures of transfer RNA (the cloverleaf), of ribosomal RNA and of RNase P RNA were established before any crystal structure, by comparative sequence analysis: in an alignment of homologous RNAs, the two columns of a conserved base pair covary, changing together from G–C to A–U or C–G while remaining complementary (compensatory mutations, a special case of coevolution, 15.5.4). Programs that combine covariation with folding energies (RNAalifold) predict consensus structures of aligned families, and statistical tests that account for phylogeny (R-scape) separate significant covariation from chance. Chemical probing adds experimental constraints: reagents such as those of SHAPE chemistry acylate the $2'$-hydroxyl of flexible, mostly unpaired nucleotides, and the reactivity profile, read out by sequencing, enters the folding algorithm as pseudo-energies.

Formal grammars give a probabilistic version of the same recursions. A stochastic **context-free grammar** generates sequences with nested pairs by rules such as "a structure is an unpaired base followed by a structure, or a pair enclosing a structure followed by a structure", each with a probability learned from known structures; the most probable structure of a sequence is found by the **CYK algorithm**, a dynamic program like Nussinov's, and covariance models built on such grammars are the basis of the RNA family database Rfam. Deep networks trained on known structures now predict secondary structures as well, with the risk that they learn the families in their training set rather than the physics; hybrids that constrain networks by thermodynamic parameters generalize better.

Tertiary structure prediction for RNA lags behind that for proteins, mainly because far fewer RNA structures are known. Fragment-assembly methods (FARFAR2 in Rosetta), coarse-grained models with statistical potentials (SimRNA) and, recently, deep networks that predict distances or coordinates (trRosettaRNA, DRfold, and the RNA modes of AlphaFold 3 and RoseTTAFold) achieve useful accuracy for small RNAs with well-defined folds, as assessed in the blind RNA-Puzzles experiments, but remain unreliable for large RNAs and those without homologs of known structure.

## 15.7. Predicting Interactions: Docking

Function is exercised through interactions, and predicting them from structures is the step from structure to biology.

*Molecular docking* predicts how a small molecule binds to a protein of known structure: where (the pocket), in what orientation and conformation (the pose) and how strongly. A docking program combines a search over poses (rigid-body translations and rotations of the ligand, its torsions, sometimes side chains of the pocket) with a fast scoring function that estimates binding free energy from steric fit, hydrogen bonds, electrostatics and buried hydrophobic surface (AutoDock Vina, Glide). Treating the protein as rigid is the main approximation; it fails when binding involves **induced fit** or **conformational selection** among states, which is handled by docking to an ensemble of structures from MD or experiment. Docking is the basis of *virtual screening*, in which libraries of $10^6$–$10^{10}$ purchasable compounds are docked to a target and the best-scoring few hundred are tested; hit rates of $10$–$40\,\%$ have been reported for well-defined pockets. Scoring functions rank poses better than affinities: binding free energies need the free-energy methods of 15.3.3.

Protein–protein docking predicts the structure of a complex from the structures of its components. Global rigid-body searches over all orientations are made fast by the **convolution theorem**: the shape complementarity of two proteins represented on grids, for all relative translations at once, is a correlation computed with three fast Fourier transforms per orientation (ZDOCK and related methods); refinement with flexible side chains and backbone follows (RosettaDock, HADDOCK, which can also incorporate experimental restraints). Protein–DNA and protein–RNA complexes are docked similarly, and the specificity of DNA-binding proteins is predicted from sequence by models trained on binding experiments. Deep-learning predictors of complexes (AlphaFold-Multimer, AlphaFold 3) have largely superseded docking for proteins with homologs in the training data, with confidence (interface PAE) that distinguishes many true from false interactions; they have been used to screen all pairs of proteins of a proteome for likely complexes.

## 15.8. Protein Design

### 15.8.1. The Inverse Problem and Directed Evolution

**Definition 15.8.1 (Protein Design)** **Protein design** is the determination of amino acid sequences that fold into a specified three-dimensional structure or perform a specified function; *de novo design* starts from no natural sequence, as opposed to the redesign of existing proteins.

Design is the inverse of prediction, and in one respect easier: a designer may choose any sequence that folds stably into the target, and many do, so the problem can be solved by finding sequences for which the target is a deep, clearly separated minimum ("negative design" against alternatives being the hard part). The sequence space is vast: there are $20^{200} \approx 10^{260}$ sequences of 200 residues, while all natural proteins number perhaps $10^{12}$ families and variants; natural evolution has explored only a tiny region near existing proteins.

The most successful practical route to new protein functions has been evolutionary rather than physical. In *directed evolution* (Frances Arnold, from 1993), a library of variants of a protein is generated by random mutagenesis or recombination, the variants with the best activity are selected by a screen, and the cycle is repeated, accumulating beneficial mutations; enzymes have been evolved to work in organic solvents, at high temperature and on non-natural reactions such as carbene and nitrene transfer. Arnold shared the Nobel Prize in Chemistry in 2018 with George Smith and Gregory Winter, who developed phage display for evolving peptides and antibodies. Directed evolution and computational design are complementary: designs are routinely improved by a few rounds of evolution.

### 15.8.2. Rational and Physics-Based Design

Early designs used simple principles. The binary patterning of hydrophobic and polar residues with the periodicity of an $\alpha$ helix ($3.6$ residues per turn) or a $\beta$ strand (alternating) is enough to determine which secondary structure forms and how it packs: peptides of leucine and lysine (DeGrado) formed $\beta$ sheets when the residues alternated and four-helix bundles when they followed the helical heptad pattern, and a $74$-residue four-helix bundle, $\alpha_4$, was the first designed protein confirmed to fold cooperatively. The next principle was packing: the interior of a protein is as densely packed as a crystal of small molecules, side chains adopt a small set of preferred conformations (*rotamers*), and a design must fill the core with rotamers that fit together without voids or clashes.

Computational design turned this into an optimization. The backbone is fixed; for each position, all amino acids in all their rotamers are considered; the energy is written as a sum of terms for single rotamers and for pairs of rotamers, and the best combination is found by Monte Carlo with simulated annealing or by exact methods such as dead-end elimination, which removes rotamers that provably cannot be in the optimum. Dahiyat and Mayo (1997) designed the sequence of a zinc-finger fold ($28$ residues, FSD-1) entirely by computer, and it folded without zinc. Helical bundles can be described by a few parameters (Crick's equations for coiled coils), which allowed the design of backbones not found in nature, such as right-handed coiled coils (Harbury and colleagues, 1998).

The Rosetta software (Baker and colleagues) combined fragment-based backbone building with sequence design and structure prediction in a loop: Top7 (Kuhlman and colleagues, 2003), a $93$-residue protein with a fold not observed in nature, was designed this way, and its crystal structure matched the design to $0.12\,\mathrm{nm}$. Later work designed ideal folds from rules relating loop lengths to the orientation of secondary structures, enzymes for reactions without natural catalysts (Kemp eliminases, a retro-aldolase, a Diels–Alderase, with modest activity that directed evolution then increased by orders of magnitude), symmetric cages and icosahedral nanoparticles used as vaccine scaffolds, transmembrane channels, and small proteins that bind targets with high affinity, including a designed COVID-19 vaccine antigen display approved in 2022. A designed sequence is checked by predicting its structure: if the prediction recovers the design with high confidence, the design is likely to fold.

### 15.8.3. Generative Design

Deep learning changed design as it changed prediction, in three steps.

- *Hallucination* (Anishchenko and colleagues, 2021) runs a structure predictor in reverse: starting from random sequences, Monte Carlo mutations are accepted when they make the predicted distance map more confident, measured by its **Kullback–Leibler divergence** from the prediction for a random background; the sequences that emerge fold into diverse, often new structures, many of which were confirmed experimentally.
- *Inverse folding networks* (ProteinMPNN, Dauparas and colleagues, 2022) predict sequences for a given backbone, trained on the PDB; they recover native sequences better than physics-based design and give designs that express and fold at high rates.
- *Generative models of backbones* (RFdiffusion, Watson and colleagues, 2023; Chroma) adapt the diffusion models of image generation: starting from random coordinates, a network trained to remove noise from protein structures generates new backbones, conditioned on symmetry, on a binding target or on a functional motif to be scaffolded. Combined with inverse folding and validation by prediction, they design binders to chosen protein surfaces with experimental success rates far higher than earlier methods.

Language models trained on sequences with functional labels generate sequences of a requested family; a model trained on hundreds of millions of sequences generated lysozymes with natural-like activity but less than $40\,\%$ identity to any natural protein (Madani and colleagues, 2023). The 2024 Nobel Prize in Chemistry recognized computational design (David Baker) together with structure prediction. The frontiers are design of enzymes with high catalytic efficiency, of proteins that switch conformations, and of function in cells.

### 15.8.4. RNA Design

RNA design asks for sequences that fold into a target secondary structure (the inverse folding problem, solved by local search with the folding algorithms of 15.6 as the evaluator, as in RNAinverse), or that perform a function: **riboswitches** that change structure on binding a metabolite, aptamers, ribozymes and logic circuits for synthetic biology. The most consequential RNA design problem is now practical: mRNA vaccines and therapeutics require sequences that are translated efficiently and are stable. Because the genetic code is degenerate, a protein of $300$ residues is encoded by more than $10^{140}$ mRNAs; their stability, structure and translation differ. Codon choice (favoring codons frequent in highly expressed genes), the design of the $5'$ and $3'$ untranslated regions, the use of an **internal ribosome entry site** to translate circular RNAs, modified nucleotides that evade innate immune sensors of double-stranded RNA, and folding algorithms that jointly optimize the codon sequence for stable secondary structure (with dynamic programming over a lattice of codon choices) have all been used.

## 15.9. Integrative Structural Biology

Many assemblies are too large, too flexible or too heterogeneous for any single method. They are modeled by combining several.

**Definition 15.9.1 (Integrative Structural Biology)** **Integrative structural biology** (integrative or hybrid modeling) determines the structures of macromolecular assemblies by combining data from several experimental methods, often each sparse or of low resolution, with physical and statistical knowledge, in a single model whose parameters are sampled to satisfy all the data, with an estimate of the uncertainty.

The procedure has four parts: gather the data; choose a representation (atomic models of components where known, beads at lower resolution elsewhere); translate each data type into a scoring function, ideally a likelihood within a Bayesian framework; and sample models (by Monte Carlo, often with replica exchange) and analyze the ensemble that satisfies the data (Integrative Modeling Platform). Common data types are:

| Data | Information | Chapter |
|---|---|---|
| Cryo-EM maps, cryo-ET subtomogram averages | shape, positions of components at $0.3$–$3\,\mathrm{nm}$ | [7.6.14](/7.6.14) |
| Crystal and NMR structures, predicted models | atomic structures of components | [7.6.10](/7.6.10), [7.6.13](/7.6.13), 15.5 |
| SAXS, SANS | size, shape and flexibility in solution | [7.6.9](/7.6.9) |
| FRET, DEER | distances between labeled sites ($2$–$10\,\mathrm{nm}$) | [7.6.12](/7.6.12), [7.6.13](/7.6.13) |
| Crosslinking mass spectrometry | pairs of residues within a crosslinker span | below |
| Hydrogen–deuterium exchange mass spectrometry | solvent protection and dynamics of segments | below |
| Native mass spectrometry | stoichiometry and subunit interactions | below |
| Coevolution | likely contacts within and between proteins | 15.5.4 |

Mass spectrometry contributes three of these ([6.4.15](/6.4.15)).

- In *crosslinking mass spectrometry* (XL-MS), a bifunctional reagent with two amine-reactive *N*-hydroxysuccinimide esters (DSS, BS³, or the MS-cleavable DSSO) links pairs of lysine residues whose $\mathrm{C}\alpha$ atoms are within about $3\,\mathrm{nm}$; after proteolysis, the crosslinked peptides are identified by tandem mass spectrometry, giving distance restraints within and between proteins, even in cells.
- In *hydrogen–deuterium exchange mass spectrometry* (HDX-MS), the protein is diluted into $\ce{D2O}$; backbone amide hydrogens exchange with deuterium at rates that depend on their protection by hydrogen bonds and burial, the reaction is quenched at low pH and $0\,^\circ\mathrm{C}$ at chosen times, the protein is digested and the mass increase of each peptide measured. Changes upon ligand binding or mutation map interfaces and allosteric effects segment by segment; the same exchange chemistry is read out residue by residue by NMR ([7.6.13](/7.6.13)).
- **Native mass spectrometry** sprays intact complexes from volatile buffers (ammonium acetate) into the gas phase by gentle electrospray ionization; the masses of the intact complex and of subcomplexes reveal stoichiometry, bound lipids and ligands, and how subunits are connected.

Integrative modeling produced the structure of the yeast and human nuclear pore complexes, about $50\,\mathrm{MDa}$ and some 500 proteins, by combining cryo-ET maps, crosslinks, crystal structures of subcomplexes and, recently, predicted models of all components, and is the natural form of structural biology in cells: an atomic picture assembled from many incomplete views. The PDB now archives such models with their data and uncertainty.

## Summary

| Topic | Key relation or idea | Reference |
|---|---|---|
| Force field | bonds, angles, torsions, impropers + Lennard-Jones + Coulomb; fixed charges; water models; periodic boundaries and particle-mesh Ewald; implicit solvent (PB, generalized Born) | Definition 15.1.1, Formula 15.1.1 |
| Molecular mechanics | minimization to the nearest minimum; QM/MM for reactions; machine-learned potentials | 15.1.4 |
| Molecular dynamics | $m\ddot{\boldsymbol{r}} = -\nabla U$; velocity Verlet: reversible, symplectic, no drift; $\Delta t = 1$–$2\,\mathrm{fs}$ | Definition 15.2.1, Algorithm 15.2.1, Example 15.2.1 |
| Ensembles | thermostats (Langevin, Nosé–Hoover, stochastic rescaling), barostats; NpT | 15.2.3 |
| Time scales | fs to s; coarse-grained models (Martini, Gō) | 15.2.4 |
| Sampling | Metropolis Monte Carlo; simulated annealing; replica exchange with acceptance Eq. (15.3) | 15.3.1–15.3.2 |
| Free energies | PMF Eq. (15.4); umbrella sampling and WHAM; metadynamics; FEP Eq. (15.6), thermodynamic integration | Algorithm 15.3.1 |
| Markov state models | $\boldsymbol{p}(t + k\tau) = \boldsymbol{p}(t)T(\tau)^k$; implied time scales $-\tau/\ln\lambda$; lag-time test | Definition 15.4.1, Eq. (15.8) |
| Prediction before deep learning | thermodynamic hypothesis, Levinthal; statistical potentials; homology modeling, threading, fragment assembly | Formula 15.5.1, 15.5.3 |
| Coevolution | Potts model, maximum entropy; DCA $J \approx -C^{-1}$ removes indirect correlations | Definition 15.5.1, Eq. (15.11) |
| Deep learning | Evoformer (MSA and pair representations, triangle updates), structure module with residue frames, recycling; pLDDT and PAE; AlphaFold 3, language models; limits | Definition 15.5.2 |
| RNA | non-crossing pairs; nearest-neighbor loop energies; Nussinov/Zuker DP $O(n^3)$; McCaskill partition function and pair probabilities; covariation, SHAPE, SCFGs | Algorithm 15.6.1, Eq. (15.13) |
| Docking | search + scoring; virtual screening; FFT rigid-body protein docking | 15.7 |
| Design | inverse problem; directed evolution; binary patterning, rotamer packing, Rosetta (Top7); hallucination, ProteinMPNN, RFdiffusion; RNA and mRNA design | Definition 15.8.1, 15.8.2–15.8.4 |
| Integrative modeling | many sparse data in one Bayesian model; XL-MS, HDX-MS, native MS | Definition 15.9.1 |

## Questions

1. Estimate the root-mean-square fluctuation of a C–C bond length at $300\,\mathrm{K}$ with $k_b = 1.3\times10^5\,\mathrm{kJ\,mol^{-1}\,nm^{-2}}$ (in the convention $U = k_b(b - b_0)^2$), and the period of its vibration (reduced mass of two carbon atoms, $6\,\mathrm{g\,mol^{-1}}$). What do these numbers imply for the time step and for constraining bonds?

   **Answer** By the **equipartition theorem**, $\langle k_b(b - b_0)^2\rangle = k_{\mathrm{B}}T/2$, so $\sqrt{\langle(b - b_0)^2\rangle} = \sqrt{RT/(2k_b)} = \sqrt{2.49/(2.6\times10^5)}\,\mathrm{nm} = 3.1\,\mathrm{pm}$, $2\,\%$ of the bond length. The spring constant is $2k_b = 2.6\times10^5\,\mathrm{kJ\,mol^{-1}\,nm^{-2}} = 432\,\mathrm{N\,m^{-1}}$; $\mu = 6\times10^{-3}/N_{\mathrm{A}} = 1.0\times10^{-26}\,\mathrm{kg}$; $\omega = \sqrt{432/10^{-26}} = 2.1\times10^{14}\,\mathrm{s^{-1}}$, period $2\pi/\omega = 30\,\mathrm{fs}$ (bonds to hydrogen, with $\mu \approx 1\,\mathrm{g\,mol^{-1}}$, about $10\,\mathrm{fs}$). The time step must be a small fraction of the fastest period, hence $1\,\mathrm{fs}$ with flexible X–H bonds; since bond fluctuations are tiny and of little biological interest, constraining them costs little accuracy and removes the fastest motions, allowing $2\,\mathrm{fs}$.

2. Show that the Metropolis acceptance rule $\min\{1, \mathrm{e}^{-\Delta U/k_{\mathrm{B}}T}\}$ with a symmetric proposal satisfies detailed balance with respect to the Boltzmann distribution, and derive the acceptance probability for exchanging configurations between replicas at inverse temperatures $\beta_i$ and $\beta_j$.

   **Answer** For states $a, b$ with $U_b > U_a$: the flux $a \to b$ is $\pi_a \cdot g\,\mathrm{e}^{-\beta(U_b - U_a)}$ and $b \to a$ is $\pi_b \cdot g \cdot 1$, where $g$ is the symmetric proposal probability. With $\pi \propto \mathrm{e}^{-\beta U}$, both equal $g\,\mathrm{e}^{-\beta U_b}/Z$. For replica exchange the joint distribution is $\propto \mathrm{e}^{-\beta_iU(x) - \beta_jU(y)}$ for configuration $x$ at $T_i$ and $y$ at $T_j$; after the swap it is $\propto \mathrm{e}^{-\beta_iU(y) - \beta_jU(x)}$. The ratio is $\exp[(\beta_i - \beta_j)(U(x) - U(y))]$, and the Metropolis rule accepts with $\min\{1, \text{ratio}\}$, which is Eq. (15.3).

3. Why does the velocity Verlet algorithm conserve energy over long simulations while the explicit Euler method does not, even though both have errors of the same order in a single step? What happens to the energy in velocity Verlet if the time step is doubled?

   **Answer** Velocity Verlet is symplectic and time-reversible: it is the exact flow of a modified ("shadow") Hamiltonian that differs from the true one by $O(\Delta t^2)$, so the true energy oscillates about a constant without systematic drift. The explicit Euler method does not preserve phase-space volume; for an oscillator it multiplies the energy by $1 + \omega^2\Delta t^2$ each step, so errors accumulate and the energy grows exponentially. Doubling $\Delta t$ in velocity Verlet multiplies the fluctuations of the energy about four times (error $\propto \Delta t^2$), until $\Delta t$ approaches the stability limit $2/\omega_{\max}$ for the fastest vibration, beyond which the integration blows up.

4. In an umbrella-sampling calculation, why must neighboring windows overlap, and what determines the spring constant to use? What is the main source of error that cannot be removed by sampling longer?

   **Answer** WHAM determines the free-energy offset $f_i$ of each window from the regions of $\xi$ that windows sample in common; without overlap the offsets, and hence the relative heights of different parts of the profile, are undetermined. The spring constant must be large enough that each window samples a narrow region including high-energy points (the bias must overcome the slope of the PMF, $k\,\delta\xi \gtrsim \lvert\mathrm{d}G/\mathrm{d}\xi\rvert$) but small enough that the distribution width $\sqrt{k_{\mathrm{B}}T/k}$ is comparable to the window spacing. The irreducible error is the choice of reaction coordinate: if a slow orthogonal motion (a side chain, a water entering a pocket) is not equilibrated within each window, the windows sample different, non-equilibrium distributions and the PMF is wrong (hysteresis between forward and backward scans is a diagnostic).

5. An MSM of a protein gives implied time scales of $0.8$, $3$ and $10\,\mu\mathrm{s}$ at lag time $\tau = 5\,\mathrm{ns}$, and $1.5$, $9$ and $50\,\mu\mathrm{s}$ at $\tau = 50\,\mathrm{ns}$. What do you conclude? The second eigenvalue of $T(50\,\mathrm{ns})$ is $0.999$; check its time scale.

   **Answer** The time scales grow with the lag time, so the model at $5\,\mathrm{ns}$ is not Markovian: memory within the microstates (poorly chosen states or fast motions not captured) makes processes appear faster than they are. One should increase $\tau$ until the time scales level off, or improve the state decomposition (better collective coordinates, more microstates). For $\lambda = 0.999$, $t = -50\,\mathrm{ns}/\ln 0.999 = 50\,\mathrm{ns}/0.0010005 = 50\,\mu\mathrm{s}$, consistent with the slowest time scale listed.

6. Explain why mutual information between alignment columns predicts false contacts, and how the inverse of the correlation matrix in Eq. (15.11) removes them. Illustrate with three residues $i$, $j$, $k$ in which only $i$–$j$ and $j$–$k$ are in contact.

   **Answer** If $i$ and $j$ coevolve, and $j$ and $k$ coevolve, a change at $i$ tends to be accompanied by one at $j$ and hence at $k$: $i$ and $k$ are correlated indirectly, and their mutual information may be as large as that of real contacts. In a Gaussian model of the alignment (the mean-field approximation), the couplings are the entries of the inverse covariance (precision) matrix, which are the partial correlations: the correlation of $i$ and $k$ conditioned on all other sites, including $j$. Given $j$, $i$ and $k$ are independent in the chain $i$–$j$–$k$, so their entry in $C^{-1}$ vanishes, while those of $i$–$j$ and $j$–$k$ do not. This is the same distinction as between a correlation network and a conditional-independence graph of a Gaussian graphical model.

7. Fill in the Nussinov table for the sequence GGGAAAUCC with pair energies G–C $-1$, A–U $-1$ (counting pairs), minimum hairpin loop 3, and give an optimal structure. How many base pairs does it have? Why is the result unrealistic as an RNA structure prediction?

   **Answer** Positions $1$–$9$: G G G A A A U C C. Pairs possible: G1–C8, G1–C9, G2–C8, G2–C9, G3–C8, G3–C9 (with $\ge 3$ nucleotides between), A4–U7? only 2 between, not allowed; A5–U7 no. The best: G1–C9, G2–C8 nested, then G3 with nothing ($G3$–$C$ requires a C after position 6 inside, none left), and A4–U7 not allowed; so 2 pairs, or alternatively G2–C9, G3–C8 (loop AAAU of 4) also 2 pairs. $E(1, 9) = -2$; structure `((.....))` or `.((....))`. In the full nearest-neighbor model a helix of two G–C pairs closing a hairpin of 4–5 nucleotides is unstable: the hairpin loop costs about $+4$ to $+6\,\mathrm{kcal\,mol^{-1}}$ while one GC/GC stack gives about $-3.3$, so the realistic prediction is the open chain. Counting pairs ignores stacking and loop entropy.

8. Why does replacing min by sum in Eq. (15.12) give the partition function only if each structure is generated exactly once by the recursion? Give an example of a decomposition that would double count.

   **Answer** The partition function is a sum of Boltzmann weights over distinct structures; the recursion builds the sum from subproblems, so a structure that can be built in two ways is counted twice and the probabilities are wrong (minimization is insensitive to this, since a minimum attained twice is still the minimum). The decomposition "$i$ unpaired, or $i$ paired with $k$" is unambiguous: in any structure, $i$ is either unpaired or has exactly one partner. A rule that also allowed splitting the interval at any position $k$ into two independent halves, $Z(i, j) \mathrel{+}= Z(i, k)Z(k + 1, j)$, would count the unpaired structure of $i \dots j$ at every split point.

9. What does a pLDDT of $35$ over a 60-residue segment of an AlphaFold model usually mean, and how would you test it? Give two other situations in which a confident AlphaFold prediction may still not represent the relevant structure.

   **Answer** Very low pLDDT usually indicates an intrinsically disordered region or a region that is structured only in a complex; the coordinates there are not a prediction (often a ribbon-like extended shape). Tests: NMR chemical shifts and relaxation (disordered segments show random-coil shifts and fast motions), CD, SAXS (Kratky plot of a disordered protein), HDX (no protection), or binding experiments to identify a partner that induces folding. Situations: (a) proteins with several conformations, for example a transporter or a kinase whose active and inactive states both exist; AlphaFold usually predicts one, typically the more frequent in the PDB, with high confidence; (b) effects of point mutations, such as destabilizing mutations, which the model often does not register; (c) conformations induced by ligands, post-translational modifications or membranes not represented in the input; (d) fold-switching proteins.

10. (Design) You want to design a small protein that binds a specific surface patch of a viral glycoprotein. Outline a computational workflow and the experiments that would validate the design, and explain where directed evolution enters.

    **Answer** (1) Obtain the target structure (experimental or predicted) and choose the epitope; (2) generate binder backbones with a diffusion model (RFdiffusion) conditioned on the target surface and hotspot residues, or by docking designed scaffolds; (3) design sequences for each backbone with an inverse-folding network (ProteinMPNN) and optimize the interface with Rosetta energies; (4) filter by re-predicting each designed complex with AlphaFold (high pLDDT, low interface PAE, recovered design) and by computed interface energy and shape complementarity; (5) test thousands of designs by yeast display or as synthetic gene libraries, measuring binding by flow cytometry; confirm hits by surface plasmon resonance or biolayer interferometry for affinity, by competition with known antibodies for epitope, by thermal melting for stability and by crystallography or cryo-EM for the structure; (6) improve affinity by directed evolution: mutagenesis libraries of the best designs screened for binding (site-saturation mutagenesis of the interface), which often gives tenfold to thousandfold improvements.

11. In crosslinking mass spectrometry with DSS, a lysine pair is found crosslinked in a complex but is $4.5\,\mathrm{nm}$ apart in a model. List possible explanations.

    **Answer** (a) The model is wrong in the relative placement of domains or subunits; (b) the complex is flexible and samples conformations in which the lysines approach (crosslinks capture transient states); (c) the crosslink is between two copies of the complex (intermolecular) or from aggregates, which can be tested by crosslinking at lower concentration or by isotope-labeled mixing experiments; (d) false identification of the crosslinked peptide (false discovery rates must be controlled); (e) the distance limit was misjudged: with flexible lysine side chains, DSS links $\mathrm{C}\alpha$ atoms up to about $2.5$–$3.5\,\mathrm{nm}$ apart, so $4.5\,\mathrm{nm}$ is a genuine violation if the model is rigid. Integrative modeling handles such data probabilistically, allowing a fraction of violated restraints.

12. Rigid-body protein–protein docking evaluates the overlap of two shape functions for all relative translations at once with the FFT. Write the correlation, estimate the cost for grids of $128^3$ points and $5\times10^4$ rotations, and compare with direct evaluation.

    **Answer** With receptor grid $a(\boldsymbol{x})$ and ligand grid $b(\boldsymbol{x})$ (positive on the surface layer, negative inside to penalize overlap), the score for translation $\boldsymbol{t}$ is $c(\boldsymbol{t}) = \sum_{\boldsymbol{x}}a(\boldsymbol{x})b(\boldsymbol{x} + \boldsymbol{t}) = \mathscr{F}^{-1}\{A^*B\}(\boldsymbol{t})$ by the convolution theorem. One FFT of $N = 128^3 = 2.1\times10^6$ points costs about $5N\log_2N \approx 2.2\times10^8$ operations; per rotation two FFTs (ligand transform and inverse) plus a pointwise product, about $5\times10^8$ operations; for $5\times10^4$ rotations about $2.5\times10^{13}$ operations, minutes to hours on a GPU. Direct evaluation would cost $N$ operations per translation for each of $N$ translations, $N^2 \approx 4\times10^{12}$ per rotation, $2\times10^{17}$ in total, about ten thousand times more.
