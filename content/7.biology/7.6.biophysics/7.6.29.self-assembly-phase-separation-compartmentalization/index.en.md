---
title: Self-Assembly, Phase Separation and Cellular Compartmentalization
description: "How many molecules build structures together: the thermodynamics of ordered self-assembly (isodesmic and nucleated polymerization, capsids and kinetic trapping), the thermodynamics of demixing (common tangent, binodal and spinodal, the lattice derivation of Flory–Huggins), multivalency and gelation (Flory–Stockmayer, stickers and spacers), the derivation and linear stability of the Cahn–Hilliard equation, interfaces, nucleation and Lifshitz–Slyozov–Wagner coarsening, the mechanics of liquid droplets (diffusion, viscosity, fusion, micropipette aspiration, wetting, aging), active emulsions, the control of organelle size, and the physics of compartments and membraneless organelles."
---

The chapters so far treated macromolecules one at a time: how a chain folds ([7.6.16](/7.6.16)), how two molecules recognize each other ([7.6.17](/7.6.17)). A cell is built from very many molecules that act together, and two modes of collective organization dominate. In ordered self-assembly a definite number of subunits joins by specific contacts into a structure of fixed geometry: a virus capsid, a microtubule, a ribosome. In phase separation an indefinite number of molecules, held by many weak and exchanging contacts, separates from the surrounding solution as a liquid droplet: a nucleolus, a stress granule, a P granule. This chapter develops the physics of both: the thermodynamics that decides whether assembly happens, the kinetics that decides how and whether it reaches the intended state, the mechanics of the resulting liquids, and the ways in which cells, out of equilibrium, control the size and number of their compartments. It ends with the cell as a whole, partitioned into membrane-bound and membraneless compartments.

The chapter builds on several earlier ones and goes deeper where they stop. The biology of condensates, the Flory–Huggins phase diagram, the lever rule and a first simulation of demixing are in [7.2.21](/7.2.21); here the theory behind them is derived. Surface tension, the Laplace pressure, the Gibbs–Thomson effect and nucleation from vapor and solution are in [6.3.19](/6.3.19), polymer solutions in [6.3.21](/6.3.21), and the Cahn–Hilliard equation was introduced as a gradient flow for sorting cells in [7.5.7](/7.5.7#def-7.7.2). Nucleated polymerization and the critical concentration of actin are in [7.3.13](/7.3.13), and their mechanics and kinetics are developed in [7.6.26](/7.6.26); the self-assembly of amphiphiles into micelles and bilayers is in [7.6.24](/7.6.24); the size of organelles and the limiting-pool model are in [7.3.6](/7.3.6#def-6.2.1). The organelles themselves are described in the cell-biology chapters 7.3.6–7.3.12 and are only summarized here.

## 29.1. Ordered Self-Assembly

### 29.1.1. Assembly and Organization

**Definition 29.1.1 (Self-Assembly)** **Self-assembly** is the spontaneous formation of an ordered or disordered structure from preexisting components through noncovalent interactions among them, without an external template or energy input; the structure is a minimum of free energy (or a long-lived state on the way to it) under the given conditions.

Protein folding, the formation of complexes of fixed stoichiometry, the polymerization of cytoskeletal filaments and the assembly of virus capsids are self-assembly. **Self-organization** is the broader notion: order that is maintained by a continuous flux of energy or matter and by feedback, such as the mitotic spindle, whose microtubules turn over in seconds and are positioned by motors and chromosome-derived signals, or the patterns of [7.6.36](/7.6.36). The distinction matters physically. A self-assembled structure can be understood with equilibrium thermodynamics plus kinetics; a self-organized one disappears when the energy supply stops.

The tobacco mosaic virus (TMV) is the classical example of ordered assembly. Its 2130 identical coat-protein subunits and one RNA of 6400 nucleotides reassemble in the test tube into infectious rods $300\,\mathrm{nm}$ long (Fraenkel-Conrat and Williams, 1955). Assembly begins when a two-layer disk of 34 subunits binds a specific origin sequence of the RNA; the disk converts to a helical "lock washer", and further disks add while the RNA is threaded through the central hole. The structure is encoded in the shapes and contacts of its parts, and the RNA both nucleates assembly and selects which RNA is packaged.

### 29.1.2. The Thermodynamics of Linear Aggregation

Consider subunits that associate into linear chains $A_n$. Let the equilibrium constant for adding one subunit to a chain be $K$, the same for every step (isodesmic assembly). The law of mass action gives the concentration of $n$-mers in terms of the free subunit concentration $c_1$,
$$
c_n = K^{n-1}c_1^n = \frac{1}{K}(Kc_1)^n,
$$
and the total subunit concentration is
$$
c = \sum_{n\ge1} n c_n = \frac{1}{K}\frac{x}{(1 - x)^2}, \qquad x = Kc_1 < 1.
$$
As $c$ increases, $x$ approaches 1 but never reaches it, and the mean chain length $\bar n = \sum nc_n/\sum c_n = 1/(1 - x) \approx \sqrt{Kc}$ grows gradually. There is no threshold: isodesmic assembly produces a broad, exponential length distribution at every concentration.

Most cytoskeletal polymers assemble differently. A small oligomer (the actin trimer, a few tubulin dimers) is unstable because each of its subunits makes fewer contacts than a subunit at the end of a long filament. Write the equilibrium constant of the first step as $\sigma K$ with $\sigma \ll 1$ and that of every later step as $K$.

**Proposition 29.1.1 (Nucleated Polymerization)** In the nucleated model, $c_n = \sigma K^{n-1}c_1^n$ for $n \ge 2$, and the total concentration is
$$
c = c_1 + \frac{\sigma}{K}\left[\frac{x}{(1 - x)^2} - x\right], \qquad x = Kc_1. \tag{29.1}
$$
For $\sigma \to 0$ almost all subunits are free below the **critical concentration** $c^* = 1/K$; above it the free concentration stays at $c^*$ and every additional subunit is in polymer.

**Proof** Summing $n c_n$ over $n \ge 2$ gives the bracket in Eq. (29.1). If $\sigma$ is small, the polymer term is negligible unless $x/(1 - x)^2$ is of order $1/\sigma$, that is, unless $1 - x$ is of order $\sqrt\sigma$. Hence for $c < 1/K$ the solution is $c_1 \approx c$, and for $c > 1/K$ it is $x = 1 - O(\sqrt\sigma)$, $c_1 \approx 1/K$, with the excess $c - 1/K$ in polymer. $\square$

The critical concentration is the dissociation constant of the end, $c^* = k_{\mathrm{off}}/k_{\mathrm{on}}$, the result derived kinetically for actin in [7.3.13](/7.3.13). The equilibrium statement adds that cooperativity, the weakness of the nucleus, is what converts a gradual polymerization into a sharp threshold; this is the same physics as the critical micelle concentration of amphiphiles ([7.6.24](/7.6.24)), where the cooperative unit is a closed aggregate rather than a nucleus. A nucleated polymer behaves like a phase: the free subunit concentration is buffered at $c^*$, just as the dilute-phase concentration of a condensate is buffered at its saturation concentration (Formula 21.3.2 of [7.2.21](/7.2.21#sec-21.3.2)).

![Ordered self-assembly. A: fraction of subunits in polymers at equilibrium against the total concentration (units of 1/K): isodesmic assembly rises gradually; nucleated assembly with a nucleation penalty σ = 10⁻³ switches on sharply at the critical concentration c* = 1/K (Proposition 29.1.1). B: kinetics of assembly of a 12-subunit icosahedral capsid in a Zlotnick-type model (trimer nucleus formed by two weak steps, then elongation with two to four contacts per addition, contact free energy 4 kBT): a lag while nuclei form, then sigmoidal growth; at the highest concentration growth stops early. C: yield of complete capsids at a fixed late time against total concentration for three contact free energies: assembly needs enough concentration and binding to proceed, but too much of either makes nuclei so fast that the free subunits are used up by many partial shells, which are kinetically trapped](./plots/assembly.py)

### 29.1.3. Capsid Assembly and Kinetic Traps

Icosahedral capsids are closed shells of $60T$ proteins arranged with the **quasi-equivalence** of Caspar and Klug, where $T$ is the **triangulation number** ([7.6.7](/7.6.7)). Their assembly from purified subunits follows nucleation–elongation kinetics with a characteristic lag phase, measured by light scattering for the capsid of hepatitis B virus and for cowpea chlorotic mottle virus (Zlotnick and colleagues). The contacts are weak: the free energy per contact is typically only $-3$ to $-4\,k_{\mathrm{B}}T$ (about $-2$ to $-2.5\,\mathrm{kcal\,mol^{-1}}$), although a subunit in a complete shell, held by several contacts, is very stable.

Weakness is a design principle. Assembly is a search in which wrongly placed subunits must be able to leave; with strong contacts they cannot, and malformed or incomplete structures persist. A second trap arises from kinetics alone. When nucleation is fast compared with elongation, many shells start at once and consume the free subunits before any is finished; each partial shell is stable and the free concentration is too low for any to grow further. The yield of complete capsids is therefore a nonmonotonic function of concentration and of contact strength (Figure above, C).

**Remark 29.1.1** Three features of real assembly reduce trapping: nucleation is slow because the nucleus is weakly bound, which keeps the number of growing shells small; assembly can be triggered by a conformational switch (scaffolding proteins, the RNA in TMV, the binding of packaging signals) so that subunits are activated only where needed; and errors can be annealed by subunit exchange when contacts are weak. The same logic governs the assembly of ribosomes, which use dozens of assembly factors that act as checkpoints, and of amyloid fibrils, where secondary nucleation on existing fibrils produces explosive, autocatalytic growth ([7.1.6](/7.1.6)).

## 29.2. The Thermodynamics of Demixing

### 29.2.1. Liquids, Solids and Complex Fluids

A phase, in Gibbs's definition, is a region of matter homogeneous in composition and physical state; his phase rule $F = C - P + 2$ counts the intensive variables that can be varied independently when $P$ phases of $C$ components coexist at given temperature and pressure. Three properties distinguish a liquid from a solid. Its positional order is short-ranged; its particles exchange neighbors quickly and diffuse over long distances; and under a steady force it flows at a rate proportional to the force and keeps no memory of its shape, whereas a solid deforms until elastic stresses balance the force and recovers its shape when the force is removed.

The cytoplasm and the condensates in it are complex fluids: solutions of polymers and colloids whose structural units are far larger than water molecules. Their responses are slow (the relaxation time of a concentrated polymer solution can be $10^3$–$10^9$ times that of a simple liquid), nonlinear and often viscoelastic ([Definition 22.7.1](/7.6.22#def-22.7.1)). Whether a cellular body is liquid, gel or solid is therefore a question about time scales: on what time does it flow, and on what time do its molecules exchange?

### 29.2.2. The Common Tangent, the Binodal and the Spinodal

A homogeneous solution of volume $V$ and solute volume fraction $\phi$ has free energy $Vf(\phi)$, where $f$ is the free energy per volume. Suppose it splits into two phases of volumes $V_A, V_B$ and compositions $\phi_A < \phi < \phi_B$. Conservation of volume and solute gives $V = V_A + V_B$ and $\phi V = \phi_AV_A + \phi_BV_B$, hence the fractions
$$
\frac{V_A}{V} = \frac{\phi_B - \phi}{\phi_B - \phi_A}, \qquad \frac{V_B}{V} = \frac{\phi - \phi_A}{\phi_B - \phi_A},
$$
and, neglecting the interface, the free energy of the split state is
$$
\frac{F_{\mathrm{split}}}{V} = \frac{\phi_B - \phi}{\phi_B - \phi_A}f(\phi_A) + \frac{\phi - \phi_A}{\phi_B - \phi_A}f(\phi_B),
$$
which is the chord of $f$ between $\phi_A$ and $\phi_B$ evaluated at $\phi$. Splitting lowers the free energy whenever $f$ lies above some chord through $\phi$; the lowest chord is the common tangent.

**Theorem 29.2.1 (Common-Tangent Construction)** Two phases of compositions $\phi_A$ and $\phi_B$ coexist in equilibrium if and only if
$$
f'(\phi_A) = f'(\phi_B) = \frac{f(\phi_B) - f(\phi_A)}{\phi_B - \phi_A}, \tag{29.2}
$$
that is, the exchange chemical potential $\mu = f'(\phi)$ and the osmotic pressure $\Pi = \phi f'(\phi) - f(\phi)$ are equal in the two phases. A homogeneous solution is locally stable if $f''(\phi) > 0$ and unstable if $f''(\phi) < 0$.

**Proof** Minimizing the chord value over $\phi_A$ and $\phi_B$ at fixed $\phi$, the two partial derivatives vanish when the slopes of $f$ at both ends equal the slope of the chord, Eq. (29.2). The second equality, $f(\phi_B) - \phi_Bf'(\phi_B) = f(\phi_A) - \phi_Af'(\phi_A)$, is the equality of $-\Pi$, the intercept of the tangent. For local stability, a small fluctuation splitting the solution into compositions $\phi \pm \delta$ in equal volumes changes the free energy by $\frac{1}{2}f''(\phi)\delta^2$ per volume, which is positive (the fluctuation decays) if and only if $f'' > 0$. $\square$

The compositions given by Eq. (29.2), traced as a function of temperature, form the binodal (coexistence curve); the inflection points $f'' = 0$ form the **spinodal**. Between them the solution is metastable: stable against small fluctuations but not against a large one, a nucleus of the other phase. Inside the spinodal it is unstable and demixes by **spinodal decomposition**. At the critical point the two curves meet, with $f'' = f''' = 0$. For the Flory–Huggins free energy these curves were computed in [7.2.21](/7.2.21#sec-21.3.1).

### 29.2.3. The Lattice Derivation of Flory–Huggins

The Flory–Huggins free energy (Formula 21.3.1 of [7.2.21](/7.2.21)) follows from counting on a lattice (Flory 1942, Huggins 1942; **Flory–Huggins theory**). Place $n_P$ chains of $N$ segments and $n_S$ solvent molecules on $M = Nn_P + n_S$ sites with coordination number $z$; let $\phi = Nn_P/M$.

The entropy of mixing is the logarithm of the number of arrangements. For a solvent of monomers ($N = 1$), $W = M!/(n_P!\,n_S!)$, and Stirling's approximation gives $\Delta S = -k_{\mathrm{B}}M[\phi\ln\phi + (1 - \phi)\ln(1 - \phi)]$ (the **Boltzmann entropy formula**). For chains, Flory placed the segments one after another, each in one of the $z - 1$ neighboring sites, counting a site as free with probability equal to the fraction of empty sites; the result is the same expression with the polymer term divided by $N$, because a chain has the translational freedom of one molecule, not of $N$.

The energy is a mean-field count of contacts. Each segment has $z$ neighbors, of which a fraction $1 - \phi$ are solvent on average, so the number of polymer–solvent contacts is $zM\phi(1 - \phi)$. Each such contact replaces half a polymer–polymer and half a solvent–solvent contact, and the energy of mixing is $zM\phi(1 - \phi)\,\Delta\varepsilon$ with $\Delta\varepsilon = \varepsilon_{PS} - \frac{1}{2}(\varepsilon_{PP} + \varepsilon_{SS})$. Defining
$$
\chi = \frac{z\,\Delta\varepsilon}{k_{\mathrm{B}}T},
$$
the free energy of mixing per site is $k_{\mathrm{B}}T[(\phi/N)\ln\phi + (1 - \phi)\ln(1 - \phi) + \chi\phi(1 - \phi)]$.

The approximations are severe: the mean field ignores the correlations that make neighbors of a sticky segment more likely to be segments; the chain statistics ignore the excluded volume and the conformational entropy changes of real chains ([7.6.21](/7.6.21)); and $\chi$ is in practice a free-energy parameter with an entropic part, $\chi = A + B/T$. With $B > 0$ the solution demixes on cooling (an upper critical solution temperature, UCST), as for FUS and many proteins with aromatic and charged stickers; with $B < 0$, as for elastin-like polypeptides, whose contacts release ordered water, it demixes on heating (LCST). Condensates are also multicomponent and their interior is heterogeneous. The theory is nevertheless the right first model, because it captures the two facts that matter: long chains need only weak attractions per segment to demix, and they do so at low concentration.

### 29.2.4. Multivalency, Stickers and Spacers

What makes a protein or RNA phase-separate is **multivalency**: the presence of several binding modules on one molecule. Modules can be folded domains in tandem (the five SH3 domains of Nck and the proline-rich motifs of N-WASP; the PRM–SH3 system studied by Li, Rosen and colleagues, 2012); oligomerization domains that turn a monovalent protein into a multivalent one (the PB1 domain of p62, the chromoshadow domain of HP1); repeated posttranslational modifications recognized by reader domains (phosphotyrosines of nephrin, polyubiquitin and polySUMO chains); intrinsically disordered regions whose aromatic, charged and polar residues provide many weak contacts (the QGSY-rich and RGG domains of FUS: π–π, cation–π, electrostatic and dipolar interactions, and transient cross-β contacts); and RNA, through its charge, its modifications ($\mathrm{m^6A}$ read by YTHDF proteins) and base pairing of repeat expansions (the GGGGCC repeats of *C9orf72* in ALS and frontotemporal dementia). The biology of these systems is in [7.2.21](/7.2.21#sec-21.2); here we ask how valence enters the physics.

**Definition 29.2.1 (Stickers-and-Spacers Model)** In the **stickers-and-spacers model** an associative polymer is described by its stickers, the residues or domains that form reversible, saturable bonds (one partner per sticker), and its spacers, the segments between them, which determine the chain's flexibility, its excluded volume and its interaction with the solvent. Phase separation of such polymers is driven by the formation of a bond network among the stickers and modulated by the solvation of the spacers.

The simplest quantitative treatment of sticker networks is the gelation theory of Flory and Stockmayer, which counts tree-like networks without closed loops.

**Theorem 29.2.2 (Flory–Stockmayer Gel Point)** Let two complementary molecules, each with $f$ stickers, be present at equal concentrations $c$, and let each pair of stickers bind with dissociation constant $K_{\mathrm{d}}$. Neglecting loops, a network spanning the system (a gel) exists when the fraction $p$ of bound stickers exceeds $p_{\mathrm{c}} = 1/(f - 1)$; in terms of concentration, the gel point is
$$
c_{\mathrm{gel}} = K_{\mathrm{d}}\,\frac{f - 1}{f(f - 2)^2}. \tag{29.3}
$$

**Proof** Start from a sticker on a molecule in the network and follow the tree outward. The sticker is bound with probability $p$; the partner molecule it reaches has $f - 1$ further stickers, each bound with probability $p$. The expected number of new branches per step is $p(f - 1)$, and the tree is infinite with positive probability (a branching process with mean offspring number above 1) if and only if $p(f - 1) > 1$. Mass action for site binding, with bound pairs at concentration $fcp$ and free sites at $fc(1 - p)$ on each species, gives $fcp/[fc(1 - p)]^2 = 1/K_{\mathrm{d}}$, so $p/(1 - p)^2 = fc/K_{\mathrm{d}}$. Setting $p = 1/(f - 1)$ gives $p/(1 - p)^2 = (f - 1)/(f - 2)^2$ and Eq. (29.3). $\square$

The threshold falls steeply with valence: $c_{\mathrm{gel}}/K_{\mathrm{d}} = 0.67$, $0.19$, $0.089$ and $0.052$ for $f = 3, 4, 5, 6$. Proteins with $K_{\mathrm{d}}$ of $100\,\mu\mathrm{M}$ per contact, far too weak to form stable dimers at cellular concentrations, form networks at a few micromolar when they carry five or six stickers, which is what Li and colleagues observed: the phase boundary of (SH3)$_n$ with (PRM)$_n$ moved to lower concentrations by more than an order of magnitude as $n$ increased from 3 to 5. Gelation (percolation) and phase separation are distinct transitions: in the stickers-and-spacers picture, a network can form within a dense phase without spanning the whole system, and phase separation is coupled to percolation when the spacers are poorly solvated (Choi, Holehouse and Pappu, 2020). Valence and spacer properties are therefore the two dials that evolution turns, and mutations or modifications that change one sticker can move a phase boundary across the physiological concentration.

![Multivalency and gelation in Flory–Stockmayer theory for two complementary f-valent molecules at equal concentrations c (sticker dissociation constant K_d). A: fraction of bound stickers p from mass action, p/(1 − p)² = fc/K_d, with the gel points p = 1/(f − 1) marked. B: fraction of molecules in the system-spanning network: it appears abruptly at c_gel (Theorem 29.2.2). C: the gel point c_gel/K_d against valence on a logarithmic scale](./plots/multivalency.py)

## 29.3. The Kinetics of Phase Separation

### 29.3.1. The Free-Energy Functional and the Interface

A solution that is demixing is inhomogeneous, and its free energy depends on gradients of composition as well as on composition. Near the critical point, and qualitatively elsewhere, the free energy is the Ginzburg–Landau functional
$$
F[\phi] = \int\left[f(\phi) + \frac{\kappa}{2}\lvert\nabla\phi\rvert^2\right]\mathrm{d}V, \tag{29.4}
$$
where the gradient coefficient $\kappa > 0$ penalizes sharp variations; in the lattice model $\kappa$ arises because a segment at an interface has fewer like neighbors, and it is of order $\chi k_{\mathrm{B}}T a^2/a^3$ for a lattice spacing $a$.

The equilibrium interface between coexisting phases minimizes $F$. Take the symmetric double-well form $f(\psi) = -\frac{a}{2}\psi^2 + \frac{b}{4}\psi^4$ for the order parameter $\psi = \phi - \phi_{\mathrm{c}}$, whose minima are $\psi = \pm\psi_0$, $\psi_0 = \sqrt{a/b}$.

**Proposition 29.3.1 (Interface Profile and Tension)** The planar interface minimizing Eq. (29.4) with the double-well $f$ is
$$
\psi(x) = \psi_0\tanh\frac{x}{\sqrt2\,\xi}, \qquad \xi = \sqrt{\kappa/a},
$$
and its excess free energy per area, the interfacial tension, is
$$
\gamma = \int\kappa\,\psi'(x)^2\,\mathrm{d}x = \frac{2\sqrt2}{3}\,\frac{\kappa^{1/2}a^{3/2}}{b}. \tag{29.5}
$$

**Proof** The Euler–Lagrange equation of Eq. (29.4) is $\kappa\psi'' = f'(\psi) = -a\psi + b\psi^3$; substituting the tanh profile verifies it. Multiplying by $\psi'$ and integrating gives the first integral $\frac{\kappa}{2}\psi'^2 = f(\psi) - f(\psi_0)$, so the gradient and the bulk excess contribute equally and $\gamma = \int\kappa\psi'^2\,\mathrm{d}x$. With $\psi' = (\psi_0/\sqrt2\xi)\operatorname{sech}^2(x/\sqrt2\xi)$ and $\int\operatorname{sech}^4u\,\mathrm{d}u = 4/3$, $\gamma = \kappa\psi_0^2(2\sqrt2/3)/\xi$, which is Eq. (29.5). $\square$

Near the critical point $a \propto T_{\mathrm{c}} - T$, so the interface widens as $\xi \propto (T_{\mathrm{c}} - T)^{-1/2}$ and the tension vanishes as $(T_{\mathrm{c}} - T)^{3/2}$ (mean-field exponents). This is one reason why the **surface tensions** of biomolecular condensates are tiny: measured values are $10^{-7}$–$10^{-5}\,\mathrm{N\,m^{-1}}$ (0.1–10 $\mu\mathrm{N\,m^{-1}}$), compared with $0.072\,\mathrm{N\,m^{-1}}$ for water against air. The other reason is size: the tension scales as $k_{\mathrm{B}}T/\xi^2$ and condensate interfaces are tens of nanometers wide, the size of the molecules. Indeed $k_{\mathrm{B}}T/(20\,\mathrm{nm})^2 \approx 10^{-5}\,\mathrm{N\,m^{-1}}$.

### 29.3.2. The Cahn–Hilliard Equation

The solute is conserved: its concentration can change only by a flux, $\partial_t\phi = -\nabla\cdot\boldsymbol{J}$. Near equilibrium the flux is proportional to the gradient of the local exchange chemical potential, $\boldsymbol{J} = -M\nabla\mu$, where $M$ is a mobility and $\mu$ the functional derivative of $F$:
$$
\mu = \frac{\delta F}{\delta\phi} = f'(\phi) - \kappa\nabla^2\phi.
$$
Combining the two gives the **Cahn–Hilliard equation** (Cahn and Hilliard 1958; [Definition 7.7.2](/7.5.7#def-7.7.2)),
$$
\frac{\partial\phi}{\partial t} = \nabla\cdot\left[M\nabla\left(f'(\phi) - \kappa\nabla^2\phi\right)\right]. \tag{29.6}
$$
The free energy can only decrease, $\mathrm{d}F/\mathrm{d}t = -\int M\lvert\nabla\mu\rvert^2\,\mathrm{d}V \le 0$ ([7.5.7](/7.5.7)), and the stationary states have uniform $\mu$, which are the coexisting phases of Theorem 29.2.1 with interfaces between them. For a dilute ideal solution $f' = k_{\mathrm{B}}T\ln\phi$ and $M = D\phi/k_{\mathrm{B}}T$ reproduce Fick's law, $\boldsymbol{J} = -D\nabla\phi$: Eq. (29.6) is diffusion driven by chemical potential, which runs uphill in concentration when $f'' < 0$.

**Theorem 29.3.1 (Linear Stability of a Homogeneous Solution)** Linearize Eq. (29.6) with constant $M$ about $\phi = \phi_0 + \delta\phi$. A perturbation $\delta\phi \propto \mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r} + \sigma t}$ grows or decays at the rate
$$
\sigma(q) = -Mq^2\left[f''(\phi_0) + \kappa q^2\right]. \tag{29.7}
$$
If $f''(\phi_0) > 0$ all modes decay. If $f''(\phi_0) < 0$, modes with $q < q_{\mathrm{c}} = \sqrt{-f''/\kappa}$ grow, fastest at $q_{\max} = q_{\mathrm{c}}/\sqrt2$, with $\sigma_{\max} = M f''^2/(4\kappa)$.

**Proof** Substituting, $\partial_t\delta\phi = M\nabla^2[f''(\phi_0)\delta\phi - \kappa\nabla^2\delta\phi]$, and $\nabla^2 \to -q^2$ gives Eq. (29.7). Maximizing $-Mq^2f'' - M\kappa q^4$ over $q^2$ gives $q^2 = -f''/2\kappa$ and the stated $\sigma_{\max}$. $\square$

Two features are specific to conserved dynamics. Long wavelengths grow slowly ($\sigma \propto q^2$ as $q \to 0$) because material must be carried far, and short wavelengths are suppressed by the interfacial cost; hence spinodal decomposition selects a wavelength $\lambda_{\max} = 2\pi/q_{\max} = 2\pi\sqrt{2\kappa/\lvert f''\rvert}$, a few interface widths, which grows without bound as the spinodal is approached. Light-scattering experiments on demixing polymer blends show the predicted ring of scattered intensity at $q_{\max}$ that grows exponentially at early times. In cells, where condensates usually form at modest supersaturation and on nucleating sites, spinodal patterns are rarely seen; they are seen in vitro and in optogenetic systems that raise valence abruptly (Shin, Brangwynne and colleagues, 2017).

**Algorithm 29.3.1 (Semi-Implicit Fourier Integration of Cahn–Hilliard)** On a periodic grid, write the dimensionless equation as $\partial_t\psi = \nabla^2(\psi^3 - \psi) - \nabla^4\psi$. At each step, with time step $\Delta t$ and a stabilizing constant $A \approx 2$:

1. Compute $N = \mathcal{F}[\psi^3 - (1 + A)\psi]$ and $\hat\psi = \mathcal{F}[\psi]$ with the fast Fourier transform.
2. Update $\hat\psi \leftarrow \left(\hat\psi - \Delta t\,q^2 N\right)/\left(1 + \Delta t(q^4 + Aq^2)\right)$, treating the stiff fourth-order term and the stabilizing term $Aq^2\hat\psi$ implicitly and the nonlinearity explicitly.
3. Transform back and increase $\Delta t$ slowly as the structure coarsens.

Implicit treatment of $q^4$ removes the time-step limit $\Delta t \lesssim \Delta x^4$ of explicit schemes, and the scheme conserves $\int\psi$ exactly because the $q = 0$ mode is unchanged.

![The Cahn–Hilliard equation in dimensionless form (f = (ψ² − 1)²/4, κ = M = 1). A: linear growth rate σ(q) = q²(1 − 3ψ0²) − q⁴ (Theorem 29.3.1) for four compositions: inside the spinodal (|ψ0| < 0.577) a band of wave numbers grows; at ψ0 = −0.65 the solution is metastable and all small perturbations decay. B, C: simulation on a periodic 128 × 128 grid by Algorithm 29.3.1 from small fluctuations about ψ0 = −0.35: dense droplets (light) emerge with a preferred spacing and then coarsen. D: domain size L = 2π/⟨q⟩ from the structure factor; after the early stage it grows as t^(1/3) (dashed), the coarsening law of Theorem 29.3.2](./plots/cahn-hilliard-coarsening.py)

### 29.3.3. Nucleation

Outside the spinodal, in the metastable region, a new phase forms by nucleation: a thermal fluctuation must produce a droplet large enough to grow. **Classical nucleation theory** ([7.6.10](/7.6.10), for protein crystals) gives the free energy of a spherical droplet of radius $R$ as
$$
\Delta G(R) = 4\pi R^2\gamma - \frac{4\pi}{3}R^3\,\frac{\Delta\mu}{v},
$$
where $\Delta\mu = k_{\mathrm{B}}T\ln(c/c_{\mathrm{sat}})$ is the chemical-potential gain per molecule transferred from the supersaturated dilute phase into the dense phase and $v$ is the volume per molecule in the dense phase. The maximum lies at the critical radius $R^* = 2\gamma v/\Delta\mu$, with barrier
$$
\Delta G^* = \frac{16\pi\gamma^3v^2}{3\Delta\mu^2}, \tag{29.8}
$$
and the nucleation rate per volume is $J \propto \exp(-\Delta G^*/k_{\mathrm{B}}T)$. Smaller droplets are dissolved by their Laplace pressure ([6.3.19](/6.3.19)): the **Gibbs–Thomson equation** gives the concentration in equilibrium with a droplet of radius $R$ as
$$
c_{\mathrm{eq}}(R) = c_{\mathrm{sat}}\left(1 + \frac{\ell_\gamma}{R}\right), \qquad \ell_\gamma = \frac{2\gamma v}{k_{\mathrm{B}}T}, \tag{29.9}
$$
for $\ell_\gamma \ll R$, and $R^*$ is the radius at which $c_{\mathrm{eq}}(R)$ equals the actual concentration.

**Example 29.3.1 (Nucleation barriers of condensates)** Take a dense phase of $4\,\mathrm{mM}$ protein, so $v = 1/(4\,\mathrm{mol\,m^{-3}}\cdot N_{\mathrm{A}}) \approx 4\times10^{-25}\,\mathrm{m^3}$, and $\gamma = 1\,\mu\mathrm{N\,m^{-1}}$. Then $\ell_\gamma = 2\gamma v/k_{\mathrm{B}}T \approx 0.2\,\mathrm{nm}$, smaller than a molecule, and by Eq. (29.8) $\Delta G^*/k_{\mathrm{B}}T = 4\times10^{-5}/\ln^2(c/c_{\mathrm{sat}})$. The barrier exceeds $10\,k_{\mathrm{B}}T$ only for $\ln(c/c_{\mathrm{sat}}) < 2\times10^{-3}$, that is, within a fifth of a percent of saturation, where $R^* = 2\gamma v/\Delta\mu \approx 100\,\mathrm{nm}$. The ultralow surface tension makes homogeneous nucleation easy as soon as a solution is appreciably supersaturated, but cells operate close to saturation, where the barrier is large and sensitive. This explains why nucleation in cells is usually heterogeneous: the nucleolus nucleates on rDNA, paraspeckles on nascent *NEAT1* RNA, transcriptional condensates on enhancer clusters, and synthetic seeds placed in cells produce condensates at concentrations where none form spontaneously (**heterogeneous nucleation**). Location is therefore controlled by seeds, and timing by small shifts of saturation concentration through modification.

### 29.3.4. Coarsening: Ostwald Ripening and the LSW Law

After the droplets have formed, the dilute phase is almost at saturation and the droplets compete. By Eq. (29.9) the concentration just outside a small droplet is higher than outside a large one, so material diffuses from small to large droplets: small ones shrink and vanish, large ones grow (**Ostwald ripening**, [6.3.21](/6.3.21)). Lifshitz and Slyozov (1961) and Wagner (1961) turned this into a quantitative theory.

Consider a dilute dispersion of droplets in a medium of mean concentration $\bar c$. Around a droplet of radius $R$ the quasi-static diffusion field is $c(r) = \bar c - [\bar c - c_{\mathrm{eq}}(R)]R/r$, and the flux into the droplet is $4\pi DR[\bar c - c_{\mathrm{eq}}(R)]$. With $n_{\mathrm{in}} = 1/v$ molecules per volume in the droplet, $n_{\mathrm{in}}\,4\pi R^2\dot R = 4\pi DR(\bar c - c_{\mathrm{eq}})$, or
$$
\frac{\mathrm{d}R}{\mathrm{d}t} = \frac{Dc_{\mathrm{sat}}\ell_\gamma v}{R}\left(\frac{1}{R_{\mathrm{c}}} - \frac{1}{R}\right), \qquad R_{\mathrm{c}} = \frac{c_{\mathrm{sat}}\ell_\gamma}{\bar c - c_{\mathrm{sat}}}. \tag{29.10}
$$
Droplets larger than the critical radius $R_{\mathrm{c}}$ grow and smaller ones shrink, and as the population coarsens $\bar c$ falls and $R_{\mathrm{c}}$ grows.

**Definition 29.3.1 (Lifshitz–Slyozov–Wagner Theory)** The **Lifshitz–Slyozov–Wagner theory** (LSW theory) is the mean-field theory of diffusion-limited Ostwald ripening of a dilute population of droplets that grow by Eq. (29.10), with the supersaturation fixed by conservation of the dispersed material.

**Theorem 29.3.2 (LSW Coarsening Law)** At long times the size distribution of LSW theory approaches a universal scaling form in $\rho = R/\langle R\rangle$, which vanishes for $\rho \ge 3/2$, the mean radius equals the critical radius, and
$$
\langle R\rangle^3 - \langle R_0\rangle^3 = \frac{4}{9}Dc_{\mathrm{sat}}\ell_\gamma v\,t = \frac{8\gamma Dc_{\mathrm{sat}}v^2}{9k_{\mathrm{B}}T}\,t. \tag{29.11}
$$
The number of droplets per volume decreases as $1/t$.

**Proof** (Outline) Conservation of dispersed volume, $\sum_iR_i^2\dot R_i = 0$, with Eq. (29.10) gives $\sum_iR_i(1/R_{\mathrm{c}} - 1/R_i) = 0$, so $R_{\mathrm{c}}$ is the mean radius. Write $\alpha = Dc_{\mathrm{sat}}\ell_\gamma v$, $\rho = R/R_{\mathrm{c}}$ and assume $R_{\mathrm{c}}^3 = \beta\alpha t$. Then $\mathrm{d}\rho^3/\mathrm{d}\ln t = (3/\beta)(\rho - 1) - \rho^3$. For the distribution of $\rho$ to become stationary, droplets must neither all run away to large $\rho$ nor all shrink, which requires the right side to touch zero without changing sign; the double root of $3(\rho - 1)/\beta = \rho^3$ is at $\rho = 3/2$ with $\beta = 4/9$. Droplets at every $\rho < 3/2$ then shrink relative to the scaling and vanish, and none exceed $3/2$. The continuity equation for the distribution then gives the explicit LSW form shown in the figure. Since total volume $\propto N\langle R\rangle^3$ is conserved, $N \propto 1/t$. $\square$

Coalescence of diffusing droplets (Brownian coalescence) gives the same $t^{1/3}$ law with a different prefactor, because a droplet of radius $R$ diffuses with $D \propto 1/R$ and a population at volume fraction $\varphi$ merges after a time $\sim R^3\eta/(k_{\mathrm{B}}T\varphi)$. The $t^{1/3}$ law is also what the Cahn–Hilliard simulation shows at late times (Figure in 29.3.2, D).

![Nucleation and Ostwald ripening. A: ΔG(R) of classical nucleation theory (γa² = kBT, v = 4πa³/3) for three supersaturations, with the critical radii marked. B: the barrier ΔG* of Eq. (29.8) for condensate-like parameters (v = 4 × 10⁻²⁵ m³) and three surface tensions against ln(c/c_sat); shaded: 10–30 kBT, where nucleation becomes rate-limiting (Example 29.3.1). C: LSW coarsening of 40 000 droplets growing by Eq. (29.10) (radii in units of the initial mean, time in units of R0³/(Dc_sat ℓγ v)): ⟨R⟩³ grows linearly, its rate approaching the LSW value 4/9 (dashed) slowly, and the number of droplets falls as 1/t. D: the scaled size distribution at late times compared with the universal LSW distribution (Theorem 29.3.2)](./plots/nucleation-lsw.py)

**Example 29.3.2 (How slow is ripening in a cell?)** For a protein with $D = 10\,\mu\mathrm{m^2\,s^{-1}}$ in the nucleoplasm, $c_{\mathrm{sat}} = 1\,\mu\mathrm{M}$ ($6\times10^{20}\,\mathrm{m^{-3}}$), $\ell_\gamma = 0.2\,\mathrm{nm}$ and $v = 4\times10^{-25}\,\mathrm{m^3}$, the coefficient in Eq. (29.11) is $\frac{4}{9}Dc_{\mathrm{sat}}\ell_\gamma v \approx \frac{4}{9}(10^{-11})(6\times10^{20})(2\times10^{-10})(4\times10^{-25}) \approx 2\times10^{-25}\,\mathrm{m^3\,s^{-1}}$. To coarsen droplets from 0.5 to $1\,\mu\mathrm{m}$ radius takes $(10^{-18} - 1.25\times10^{-19})/(2\times10^{-25}) \approx 4\times10^6\,\mathrm{s}$, about seven weeks. Ripening of micrometer condensates at micromolar saturation is far slower than a cell cycle; coexisting nucleoli and speckles need not be explained by active arrest alone. Fusion, when droplets meet, is faster, and in the nucleus it is limited by the slow motion of droplets embedded in chromatin.

### 29.3.5. Coarsening in Cells

Several mechanisms keep cellular condensates from coarsening further. Their slowness (Example 29.3.2) is one. Elasticity of the surrounding medium is another: droplets growing in a crosslinked gel must deform it, which costs elastic energy increasing with size, so that droplets in stiffer regions are smaller and material flows from stiff to soft regions (elastic ripening, Style, Dufresne and colleagues 2018; Rosowski 2020); in the nucleus, condensates nucleated by optogenetic clustering grow preferentially in chromatin-poor regions and exclude chromatin as they grow (Shin, Brangwynne and colleagues 2018). Chemical activity, finally, can stop ripening altogether (29.5).

## 29.4. The Mechanics of Droplets

### 29.4.1. Diffusion and Viscosity

A condensate is liquid if its molecules diffuse within it and exchange with the surroundings on observable time scales. Diffusion is measured by **fluorescence recovery after photobleaching** (bleach part of a droplet with intense light and watch the fluorescence return), by fluorescence correlation spectroscopy, and by tracking single molecules or embedded beads ([7.6.12](/7.6.12)). For tracked particles the **mean squared displacement** in $d$ dimensions is $\langle r^2\rangle = 2dDt^\alpha$, with $\alpha = 1$ for normal diffusion and $\alpha < 1$ (subdiffusion) in viscoelastic or crowded interiors ([7.6.23](/7.6.23)). Diffusion coefficients of scaffold proteins inside condensates are typically 10–1000 times lower than in the dilute phase, and different components of the same condensate can differ by orders of magnitude.

The viscosity of the interior follows from the diffusion of an inert bead of radius $a$ through the **Stokes–Einstein equation**, $D = k_{\mathrm{B}}T/6\pi\eta a$. Beads of $100\,\mathrm{nm}$ radius that diffuse with $D = 2\times10^{-3}\,\mu\mathrm{m^2\,s^{-1}}$ report $\eta = k_{\mathrm{B}}T/(6\pi Da) \approx 1\,\mathrm{Pa\,s}$, a thousand times the viscosity of water; such values are typical of P granules and of droplets of LAF-1 and FUS in vitro, while nucleoli are more viscous still. Viscosity can also be measured rheologically, by aspirating a droplet into a micropipette (29.4.2) or by deforming it with optical traps. The bead must be larger than the mesh of the network but smaller than the droplet; otherwise it measures the solvent or the surface.

### 29.4.2. Surface Tension, Aspiration and Fusion

The surface tension of a droplet can be measured by micropipette aspiration. A pipette of inner radius $R_{\mathrm{p}}$ draws part of a droplet of radius $R_{\mathrm{d}}$ inside at suction pressure $\Delta p$; when the aspirated tongue becomes a hemisphere of radius $R_{\mathrm{p}}$, the **Young–Laplace equation** applied to the two surfaces gives
$$
\Delta p = 2\gamma\left(\frac{1}{R_{\mathrm{p}}} - \frac{1}{R_{\mathrm{d}}}\right), \tag{29.12}
$$
and at larger suction the droplet flows into the pipette at a rate set by its viscosity. The same equation applied to cortical tension is the basis of cell aspiration ([7.5.8](/7.5.8)).

Two touching liquid droplets fuse because the merged drop has less surface. At low Reynolds number ([7.6.22](/7.6.22)) surface tension drives the flow and viscosity resists it; dimensional analysis then fixes the time scale.

**Definition 29.4.1 (Inverse Capillary Velocity)** For a viscous droplet with viscosity $\eta$ and surface tension $\gamma$, the **inverse capillary velocity** $\eta/\gamma$ is the time per unit length of shape relaxation; a droplet of size $R$ relaxes after a deformation, and two droplets of radius $R$ fuse, in the visco-capillary time
$$
\tau \approx \frac{\eta R}{\gamma}. \tag{29.13}
$$

In a fusion experiment the aspect ratio of the merging pair (long axis over short) decays from about 2 to 1 approximately as $1 + \mathrm{e}^{-t/\tau}$; plotting $\tau$ against $R$ for many fusion events gives a line through the origin whose slope is $\eta/\gamma$. For P granules $\eta/\gamma$ is of order $1\,\mathrm{s\,\mu m^{-1}}$ (Brangwynne, Hyman and colleagues 2009), so micrometer granules fuse in seconds; the large nucleoli of *Xenopus laevis* oocytes take tens of minutes. A measurement of $\eta/\gamma$ combined with a separate measurement of $\eta$ (from bead diffusion) yields $\gamma$.

![Mechanics of liquid condensates. A: aspect ratio of two fusing droplets against time for three radii at η/γ = 1 s µm⁻¹, relaxing with τ = ηR/γ (Definition 29.4.1). B: the visco-capillary scaling τ ∝ R for inverse capillary velocities from 0.1 to 1000 s µm⁻¹, an illustrative range from protein droplets in vitro to nucleoli. C: micropipette aspiration of a droplet of radius 10 µm with three pipettes: synthetic measurements of the threshold suction against 1/R_p − 1/R_d and the fit to Eq. (29.12), which recovers γ ≈ 1 µN m⁻¹. D: the three wetting configurations of two condensate phases in a medium, decided by the three interfacial tensions (Proposition 29.4.1)](./plots/droplet-mechanics.py)

### 29.4.3. Wetting and Multiphase Condensates

Cellular condensates are often layered: the nucleolus has a fibrillar center inside a dense fibrillar component inside a granular component ([7.2.21](/7.2.21#sec-21.5.1)); stress granules have a stable core inside a dynamic shell; germ granules are aggregates of adjacent but distinct bodies. Layering follows from the interfacial tensions between the phases, the physics of **wetting** ([6.3.19](/6.3.19)).

**Proposition 29.4.1 (Engulfment Criterion)** Let two immiscible condensate phases 1 and 2 coexist in a medium 0, with interfacial tensions $\gamma_{01}, \gamma_{02}, \gamma_{12}$. At equilibrium phase 1 is completely engulfed by phase 2 if $\gamma_{01} > \gamma_{02} + \gamma_{12}$, the two droplets stay separate if $\gamma_{12} > \gamma_{01} + \gamma_{02}$, and otherwise they form a partially engulfed doublet whose contact angles satisfy Neumann's triangle: the three tension vectors at the three-phase line sum to zero.

**Proof** In complete engulfment the 0–1 interface is replaced by a 1–2 and a 0–2 interface. If $\gamma_{01} > \gamma_{02} + \gamma_{12}$, any exposed 0–1 interface can be covered by phase 2 at a lower cost, so the minimum has no 0–1 interface; similarly for the 1–2 interface in the separate case. If none of the tensions exceeds the sum of the other two, a triangle with these side lengths exists, and force balance at the line where three interfaces meet requires the tensions, as vectors along the interfaces, to form that closed triangle. $\square$

Feric, Brangwynne and colleagues (2016) showed that the granular-component protein nucleophosmin and the dense-fibrillar protein fibrillarin form immiscible droplets in vitro, with the fibrillarin phase engulfed by the nucleophosmin phase, because the tension of the fibrillarin phase against the nucleoplasm is the largest. The layered structure of the nucleolus thus reflects equilibrium wetting, and the order of the layers follows the order in which rRNA is processed as it moves outward.

### 29.4.4. Viscoelasticity, Aging and Material Properties

Condensates are not simple liquids. On short time scales they respond elastically; the elastic moduli are low, from tens of pascals to a few kilopascals, measured by atomic force microscopy indentation (analyzed with the Hertz model of [7.6.31](/7.6.31)), by optical-trap rheology, or by microrheology of embedded beads. Reconstituted postsynaptic-density condensates with two scaffold proteins were reported at about $2.5\,\mathrm{kPa}$, and with six at about $3.5\,\mathrm{kPa}$. Jawerth, Jülicher, Hyman and colleagues (2020) found that droplets of several proteins behave as **Maxwell viscoelastic liquids** whose viscosity increases with time after formation while the elastic modulus stays nearly constant: the droplets age, a glass-like slowing of relaxation, and some eventually convert into fibrous solids ([7.2.21](/7.2.21#sec-21.6)). Aging of reconstituted postsynaptic-density droplets over 5–8 hours lowers the mobility of their components.

Material properties are tuned to function. The Balbiani body of oocytes, a store of mitochondria, RNA and proteins scaffolded by the prion-like protein Xvelo in *Xenopus laevis*, is nearly solid and stable for months; signaling clusters of the T-cell receptor component CD3ε with the kinase Lck are highly dynamic, which allows rapid amplification and reversal. Composition changes the properties: in *Caenorhabditis elegans* P granules, recruitment of EPG-2 slows diffusion of the PGL scaffold, and MEG-3 lowers the surface tension of PGL-3 droplets without changing their viscosity, acting as a surfactant that keeps the granules small. Charge-modifying changes, such as acetylation of lysines in TDP-43 or binding of HP1α to H3K9me3 chromatin, alter mobility and viscoelasticity. A useful summary is that the dials of phase separation (valence, sticker strength, spacer solvation) also set material properties, because the same bonds that hold the network together set its relaxation times.

## 29.5. Active Emulsions and the Control of Size

### 29.5.1. Chemically Active Droplets

Passive droplets ripen until a single drop remains (Theorem 29.3.2). Cells contain many condensates of similar size, persistent over hours, and their components are continually modified and demodified, synthesized and degraded. Zwicker, Jülicher, Weber and colleagues (2015–2017) showed that such chemical reactions change the coarsening dynamics qualitatively.

**Definition 29.5.1 (Active Emulsion)** An **active emulsion** is an emulsion whose droplet material is produced and removed by chemical reactions maintained away from equilibrium by an energy supply (for example, phosphorylation by a kinase in one phase and dephosphorylation in the other), so that the droplets exchange material with the surroundings through both diffusion and reaction fluxes.

Consider the simplest model. Droplet material is made in the dilute phase at rate $s$ per volume and converted into a soluble form inside droplets at rate $k$ per molecule. A droplet now gains material by diffusion, Eq. (29.10), and loses it by reaction, at a rate proportional to its volume. In the units of Eq. (29.10),
$$
\frac{\mathrm{d}R}{\mathrm{d}t} = \frac{1}{R}\left(\varepsilon - \frac{1}{R}\right) - \frac{k}{3}R, \tag{29.14}
$$
where $\varepsilon$ is the scaled supersaturation of the dilute phase, maintained by production.

**Proposition 29.5.1 (Size Selection by Reactions)** For $k > 0$ the growth law (29.14) has, for sufficiently large $\varepsilon$, two positive fixed points. The larger one, $R^*$, is stable against size differences between droplets at the same $\varepsilon$ if and only if $R^* > \frac{3}{2}\varepsilon^{-1}$; it then sets a common droplet size, and Ostwald ripening is suppressed.

**Proof** Let $g(R)$ be the right side of Eq. (29.14). At a fixed point $\varepsilon/R - 1/R^2 = kR/3$. A small difference between two droplets grows if $g'(R^*) > 0$ and shrinks if $g'(R^*) < 0$. Differentiating, $g'(R) = -\varepsilon/R^2 + 2/R^3 - k/3$, and using the fixed-point condition to eliminate $k/3 = \varepsilon/R^{*2} - 1/R^{*3}$, $g'(R^*) = (-2\varepsilon R^* + 3)/R^{*3}$, which is negative if and only if $R^* > 3/(2\varepsilon)$. Without reactions the only fixed point is $R_{\mathrm{c}} = 1/\varepsilon$, where $g'(R_{\mathrm{c}}) = \varepsilon^3 > 0$: unstable, which is Ostwald ripening. $\square$

The physics is that degradation inside a droplet grows with its volume ($\propto R^3$) while diffusive influx grows only with its radius ($\propto R$); large droplets lose more than they gain. The selected radius is of order $(D/k)^{1/2}$ times factors of order 1, a reaction–diffusion length. Such droplets can also divide: when the selected size is exceeded, a shape instability elongates and splits the droplet (Zwicker 2017), a mechanism discussed for protocells in the origin of life ([7.10](/7.10)).

![Chemically active droplets. A: growth law dR/dt of Eq. (29.14) at supersaturation ε = 0.37: a passive droplet has a single unstable fixed point (open circle) at the critical radius; with reactions (k = 0.02) a stable fixed point (filled) appears at larger R (Proposition 29.5.1). B, C: 60 droplets with random initial radii exchanging material through a common dilute phase. B: passive: Ostwald ripening, droplets dissolve one after another and the survivors grow. C: active (production in the dilute phase, conversion inside droplets): small droplets dissolve, the rest converge to a common radius and persist. D: number of droplets against time](./plots/active-emulsion.py)

Centrosomes are a candidate biological example. The pericentriolar material (PCM) of *C. elegans* embryos grows by recruiting the scaffold protein SPD-5 in a way that is accelerated by the PCM itself (autocatalysis, through phosphorylation by PLK-1), and the two centrosomes of a cell reach the same size even when one starts larger. Zwicker, Jülicher and Hyman (2014) showed that centrosomes treated as droplets of an autocatalytically produced component, nucleated by the centrioles, grow to equal size and are protected from ripening, with the size set by the limiting pool of the component.

### 29.5.2. The Physics of Organelle Size

How large an organelle is depends on how its assembly is regulated. Three classes of model are distinguished by how the growth rate depends on size.

In the **limiting-pool model** ([7.3.6](/7.3.6#def-6.2.1)) an organelle grows from a pool of subunits whose total is proportional to cell volume, until the free concentration has fallen to the critical value at which assembly and disassembly balance. Size then scales with cell volume, as observed for centrosomes and mitotic spindles in the early embryos of *C. elegans* and in droplets of *Xenopus laevis* egg extract of controlled size (Good, Heald and colleagues 2013). With two organelles drawing on one pool, a growth rate independent of size fixes only the total, not the share of each; equal sizes need a size-dependent rate, such as the autocatalytic growth of active droplets.

**Definition 29.5.2 (Balance-Point Model)** In the **balance-point model** of organelle size, the assembly rate decreases with the size $L$ of the organelle while the disassembly rate does not, so that the steady size $L^*$ is the point where the two rates are equal and is stable because a larger organelle disassembles faster than it assembles.

The model was proposed for the flagella of the green alga *Chlamydomonas reinhardtii* (Marshall and Rosenbaum, 2001). Flagellar tubulin turns over at the tip, where it is delivered by **intraflagellar transport** trains moving at constant speed; the number of trains in a flagellum is roughly constant, so the delivery rate per unit length, and hence the assembly rate, falls as $A/L$, while disassembly at the tip proceeds at a constant rate $D$. The balance point is $L^* = A/D$. The model explains the classical "long-zero" experiment: when one of the two flagella is amputated, the stump regrows quickly while the intact flagellum shortens, and both converge to the same length, because the two draw on a shared precursor pool (Coyne and Rosenbaum, 1970).

![Length control of flagella. A: in the balance-point model (Definition 29.5.2) assembly falls as A/L while disassembly is constant, and the steady length is L* = A/D (A = 10 µm² min⁻¹, D = 1 µm min⁻¹). B: two flagella sharing a precursor pool, with assembly rate aP/L and the free pool P equal to the total minus the two lengths; one flagellum is amputated at t = 0 (its material is lost) and new synthesis restores the total pool with a 30 min time constant. The stump regrows rapidly, the intact flagellum transiently shortens, and the two converge, as in the long-zero experiment of *Chlamydomonas*](./plots/size-control.py)

The nucleus offers a third, physical mechanism. The ratio of nuclear to cell volume is remarkably constant within a cell type (about 0.08 in fission yeast, and constant over a range of cell sizes in many cells), and nuclei grow in proportion to the cell. Since the nuclear envelope is permeable to small molecules but the nucleus retains macromolecules, its volume is set by an osmotic balance: the nucleus swells until the osmotic pressure of the macromolecules it contains, mostly proteins and their counterions rather than chromatin, equals that of those outside, which makes the volume ratio equal to the ratio of macromolecule numbers inside and outside (Lemière, Chang and colleagues 2022; Deviri and Safran 2022). The ratio is then set by nuclear import, a size control by transport rather than by assembly.

## 29.6. Cellular Compartmentalization

### 29.6.1. Why Compartments: Concentration and Specificity

**Compartmentalization** separates reactions in space. In the broadest sense the cytoplasm is never homogeneous: concentrations differ near membranes, on the surfaces of filaments and within the crowded interior ([7.6.23](/7.6.23)). In the narrow sense a compartment is a volume bounded by a sharp interface, a membrane or a phase boundary, across which composition jumps. Two benefits are quantitative. First, a compartment that concentrates reactants accelerates reactions whose rate is nonlinear in concentration. Second, by excluding some molecules and admitting others it creates specificity that the binding affinities alone do not provide: two enzymes with the same substrate act differently if they are in different places, and the specificity measured in a homogeneous test tube ([7.6.17](/7.6.17)) is often not the specificity in the cell.

**Proposition 29.6.1 (Rate Enhancement by Partitioning)** Let a bimolecular reaction $A + B \to C$ with rate constant $k$ (the same inside and outside) occur in a cell in which a compartment of volume fraction $\phi$ concentrates $A$ and $B$ by partition coefficients $K_A$ and $K_B$, the total amounts being fixed. The total rate relative to the well-mixed cell is
$$
\frac{r}{r_0} = \frac{1 - \phi + \phi K_AK_B}{(1 - \phi + \phi K_A)(1 - \phi + \phi K_B)}. \tag{29.15}
$$
For $K_A = K_B = K \gg 1$ the maximum is approximately $K/4$, at $\phi \approx 1/K$. If only one reactant is concentrated ($K_B = 1$), $r = r_0$.

**Proof** With mean concentrations $\bar a, \bar b$, the outside concentration of $A$ is $a = \bar a/(1 - \phi + \phi K_A)$ and the inside one $K_Aa$, and similarly for $B$. The total rate per volume is $k[(1 - \phi)ab + \phi K_AK_Bab]$, which divided by $r_0 = k\bar a\bar b$ gives Eq. (29.15). For $K_A = K_B = K$ and $\phi = 1/K$, $r/r_0 = (1 - 1/K + K)/(2 - 1/K)^2 \approx K/4$; setting $K_B = 1$ the numerator equals the first factor of the denominator. $\square$

The result shows the limits of the popular idea that condensates are "crucibles" of biochemistry. Enhancement requires that both partners partition, and it is largest when the compartment is small; a condensate that takes up a large fraction of the cell dilutes rather than concentrates. For first-order reactions, such as conformational changes or the action of an enzyme far from saturation on a fixed amount of enzyme–substrate complexes, partitioning does not change the total rate at all. Compartments can also slow reactions, by excluding a partner ($K_B < 1$) or by lowering the diffusion and rate constants inside, which the formula ignores. Partition coefficients of client molecules into condensates range from about 1 to more than 100 and depend on composition; a partition coefficient corresponds to a transfer free energy $\Delta G = -k_{\mathrm{B}}T\ln K$.

![Reactions in compartments (Proposition 29.6.1). A: rate of a bimolecular reaction relative to the well-mixed cell when both reactants partition into a compartment with coefficient K, against the volume fraction φ of the compartment: the enhancement peaks near φ = 1/K at about K/4 (dots). B: one reactant concentrated 100-fold (K_A = 100): the rate is unchanged if the second reactant does not partition (K_B = 1), rises if it does and falls if it is excluded](./plots/compartment-reactions.py)

### 29.6.2. The Membrane-Bound Organelles in Numbers

The nucleus was the first organelle described (Robert Brown, 1831), and the nucleolus inside it the first membraneless one. Mitochondria were seen by Kölliker (1857) and Altmann (1890) and named by Benda (1898); Camillo Golgi described the "internal reticular apparatus" in 1898 and Santiago Ramón y Cajal the nuclear "accessory body" in 1903, which became the Cajal body; peroxisomes were described as microbodies by Rhodin (1954) and identified biochemically by de Duve (1965–1967). The modern biology of each organelle is in 7.3.6–7.3.12; the numbers below give the physical layout of an animal cell.

| Compartment | Size and number | Share of the cell | Physical remarks |
|---|---|---|---|
| Nucleus | $5$–$10\,\mu\mathrm{m}$ across in animal cells | about $10\,\%$ of volume | double membrane with perinuclear space continuous with the ER lumen; nuclear lamina; nuclear pore complexes, about $3000$–$5000$ per nucleus, the only route between nucleus and cytoplasm |
| Endoplasmic reticulum | continuous network of sheets and tubules | over $10\,\%$ of volume, about half of all membrane | sheets stacked and connected by helicoidal ramps (see below); tubules shaped by curvature-stabilizing reticulons |
| Golgi apparatus | stacks of 4–8 cisternae; 40–100 stacks in mammalian cells, linked into a ribbon near the centrosome | a few percent | depends on microtubules; disperses into individual stacks when they depolymerize and in mitosis |
| Mitochondria | cross section $0.75$–$3\,\mu\mathrm{m^2}$; $1000$–$2000$ per hepatocyte | about $20\,\%$ of volume in hepatocytes | a dynamic network maintained by fission (DRP1) and fusion (mitofusins, OPA1); inner membrane folded into cristae; outer membrane $6$–$7.5\,\mathrm{nm}$ thick |
| Lysosomes, peroxisomes | $0.1$–$1\,\mu\mathrm{m}$; hundreds per cell | about $1\,\%$ each | lysosomal lumen at $\mathrm{pH} \approx 4.5$–$5$; peroxisomes oxidize long-chain fatty acids and degrade the $\ce{H2O2}$ they produce |
| Vesicles and endosomes | $50$–$500\,\mathrm{nm}$ | small | carriers between compartments |
| Extracellular vesicles | exosomes about $100\,\mathrm{nm}$; migrasomes $0.5$–$3\,\mu\mathrm{m}$ | released | exosomes derive from multivesicular bodies; migrasomes grow on retraction fibers left behind by migrating cells (Ma, Yu and colleagues 2015) |

The shapes of membrane organelles are those that minimize bending, tension and edge energies under the constraints of their proteins ([7.6.24](/7.6.24)). An example is the stacking of ER sheets. Serial-section electron microscopy showed that the stacked sheets of rough ER are connected by helicoidal membrane surfaces, like the ramps of a parking garage (Terasaki, Huber, Kasthuri, Lichtman and colleagues 2013). A minimal elastic model in which the sheet edges carry a line tension and the surfaces a bending energy shows that helicoids of opposite handedness connecting the sheets lower the total energy and set the spacing; a helicoid is a minimal surface, with zero mean curvature, so it costs no bending energy at all (Guven, Huber and Valencia 2014).

### 29.6.3. The Membraneless Organelles

Many compartments have no membrane. That at least some of them are liquid condensates was shown for the P granules of *C. elegans*, which fuse, drip, wet the nucleus and dissolve and condense within minutes (Brangwynne, Hyman and colleagues 2009); since then a large number of bodies have been examined in the same way, with varying conclusions about how liquid they are. The table groups the main ones by location; their biology is in [7.2.21](/7.2.21) and the cell-biology chapters.

| Location | Body | Typical size | Main components and role |
|---|---|---|---|
| Nucleus | **nucleolus** | $1$–$5\,\mu\mathrm{m}$ | three nested phases (fibrillar center with rDNA, dense fibrillar component, granular component) in mammals, two in budding yeast; ribosome biogenesis; disassembles in mitosis and reforms |
| | **Cajal body** and gems | $0.2$–$1\,\mu\mathrm{m}$ | coilin, snRNPs, scaRNAs; snRNP maturation |
| | **nuclear speckle** | $0.5$–$2\,\mu\mathrm{m}$, 20–50 per nucleus | SON, SRRM2, splicing factors; near active genes |
| | paraspeckle | $0.2$–$1\,\mu\mathrm{m}$ | lncRNA *NEAT1* and some 40 proteins; retains edited RNAs |
| | PML body, nuclear stress body, histone locus body, Polycomb body | $0.1$–$1\,\mu\mathrm{m}$ | stress responses, histone mRNA processing, gene silencing |
| | DNA-damage foci, replication compartments | sub-micrometer | γH2AX-marked repair foci; replication factories |
| | heterochromatin, transcriptional condensates | variable | HP1 and H3K9me3 chromatin; Mediator, BRD4 and Pol II at enhancers |
| Cytoplasm | **stress granule** | $0.1$–$2\,\mu\mathrm{m}$ | stalled translation initiation complexes, G3BP1/2, TIA-1; core and shell; forms within minutes of stress |
| | **processing body** (P-body) | $0.1$–$1\,\mu\mathrm{m}$ | decapping and decay factors; mRNA storage |
| | germ granules (P granules) | about $1\,\mu\mathrm{m}$ | PGL-1/3, MEG-3, RNA; germ-cell specification |
| | Balbiani body | tens of $\mu\mathrm{m}$ in oocytes | mitochondria, RNA, Xvelo; long-term storage |
| | RNA transport granules, U-bodies, proteasome storage granules, metabolic granules (purinosomes), p62 bodies | sub-micrometer | transport, storage of snRNPs and proteasomes, enzyme clustering, autophagy |
| Membrane-associated | signaling clusters (T-cell receptor with LAT, nephrin with Nck and N-WASP), postsynaptic density, **focal adhesion** | $0.1$–$1\,\mu\mathrm{m}$ | two-dimensional condensates on the plasma membrane that concentrate kinases and exclude phosphatases |
| | TIS granules | network around the ER | the RNA-binding protein TIS11B; localized translation of membrane proteins |
| | Sec bodies | $\sim 1\,\mu\mathrm{m}$ | ER exit-site components stored during amino-acid starvation in *Drosophila* cells |
| | **nuclear pore complex** | $120\,\mathrm{nm}$ | the permeability barrier is a hydrogel-like meshwork of **FG repeats** |

Two-dimensional condensates on membranes are a distinct physical case: binding to a membrane reduces dimensionality, raises local concentration and lowers the threshold for phase separation (Banjade and Rosen 2014; Su, Vale and colleagues 2016, for LAT clusters that exclude the phosphatase CD45 and enhance signaling). The nuclear pore illustrates that a phase-separated material can be a selective barrier: the FG-repeat meshwork excludes inert macromolecules larger than about $40\,\mathrm{kDa}$ but dissolves the nuclear transport receptors that bind FG motifs, which then pass at rates of about a thousand per pore per second (Frey and Görlich, 2006).

**Remark 29.6.1** Calling a body "phase-separated" is a hypothesis to be tested, not a description. Spherical shape, fusion and recovery after photobleaching are consistent with a liquid but also with a dynamic cluster of binding sites; the quantitative tests are those of this chapter and of [7.2.21](/7.2.21): a dilute-phase concentration buffered at saturation (the lever rule), a sharp dependence on concentration and valence, visco-capillary fusion with a size-independent $\eta/\gamma$, and ripening or its absence for a reason.

## Summary

| Topic | Key results | Where |
|---|---|---|
| Ordered assembly | Isodesmic: no threshold, $\bar n \approx \sqrt{Kc}$; nucleated: sharp critical concentration $c^* = 1/K$, free subunits buffered | Definition 29.1.1, Proposition 29.1.1, Eq. (29.1) |
| Capsids | Weak contacts ($3$–$4\,k_{\mathrm{B}}T$), lag phase; yield nonmonotonic in concentration and contact strength (kinetic traps) | 29.1.3, Remark 29.1.1 |
| Demixing | Common tangent = equal $\mu$ and $\Pi$; spinodal $f'' = 0$; Flory–Huggins from lattice counting, $\chi = z\Delta\varepsilon/k_{\mathrm{B}}T$, UCST/LCST | Theorem 29.2.1, 29.2.3 |
| Multivalency | Stickers and spacers; gel point $c_{\mathrm{gel}} = K_{\mathrm{d}}(f - 1)/[f(f - 2)^2]$, steep in valence | Definition 29.2.1, Theorem 29.2.2, Eq. (29.3) |
| Interfaces | $\psi = \psi_0\tanh(x/\sqrt2\xi)$, $\gamma = \frac{2\sqrt2}{3}\kappa^{1/2}a^{3/2}/b$; condensates $\gamma \sim 0.1$–$10\,\mu\mathrm{N\,m^{-1}}$ | Proposition 29.3.1, Eq. (29.5) |
| Cahn–Hilliard | $\partial_t\phi = \nabla\cdot[M\nabla(f' - \kappa\nabla^2\phi)]$; $\sigma(q) = -Mq^2(f'' + \kappa q^2)$, $q_{\max} = \sqrt{-f''/2\kappa}$; semi-implicit spectral scheme | Eqs. (29.6)–(29.7), Theorem 29.3.1, Algorithm 29.3.1 |
| Nucleation | $R^* = 2\gamma v/\Delta\mu$, $\Delta G^* = 16\pi\gamma^3v^2/3\Delta\mu^2$; barriers large only near saturation; seeds control location | Eq. (29.8), Example 29.3.1 |
| Coarsening | LSW: $\langle R\rangle^3 \propto \frac{8\gamma Dc_{\mathrm{sat}}v^2}{9k_{\mathrm{B}}T}t$, $N \propto 1/t$, distribution ends at $1.5\langle R\rangle$; weeks for cellular condensates | Definition 29.3.1, Theorem 29.3.2, Example 29.3.2 |
| Droplet mechanics | Stokes–Einstein viscosity; aspiration $\Delta p = 2\gamma(1/R_{\mathrm{p}} - 1/R_{\mathrm{d}})$; fusion $\tau = \eta R/\gamma$; engulfment $\gamma_{01} > \gamma_{02} + \gamma_{12}$; aging Maxwell fluids | Eqs. (29.12)–(29.13), Definition 29.4.1, Proposition 29.4.1 |
| Active emulsions | Reactions make loss $\propto R^3$, gain $\propto R$: stable size if $R^* > 3/2\varepsilon$; centrosomes | Definition 29.5.1, Proposition 29.5.1 |
| Size control | Limiting pool (size ∝ volume), balance point $L^* = A/D$ (flagella, long-zero), osmotic N/C ratio | Definition 29.5.2, 29.5.2 |
| Compartments | Rate enhancement $\le K/4$ at $\phi \approx 1/K$, only if both partners partition; organelle census; membraneless organelles by location | Proposition 29.6.1, 29.6.2–29.6.3 |

## Questions

1. Show that for isodesmic assembly the mean length of chains is $\bar n = 1/(1 - Kc_1)$ and that $\bar n \approx \sqrt{Kc}$ when $Kc \gg 1$. How long are the chains for $K = 10^6\,\mathrm{M^{-1}}$ and $c = 1\,\mathrm{mM}$?

   **Answer** $\sum c_n = (1/K)x/(1 - x)$ and $\sum nc_n = (1/K)x/(1 - x)^2$, so $\bar n = 1/(1 - x)$. For $c$ large, $Kc = x/(1 - x)^2 \approx 1/(1 - x)^2$, so $\bar n \approx \sqrt{Kc}$. Here $Kc = 10^3$ and $\bar n \approx 32$: a broad distribution of short chains, unlike the long filaments of nucleated polymers.

2. Actin polymerizes with $k_{\mathrm{on}} = 11.6\,\mu\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 1.4\,\mathrm{s^{-1}}$ at the barbed end. What is the critical concentration, and how much F-actin is there at equilibrium in a solution of $5\,\mu\mathrm{M}$ total actin? Why does the presence of a weak nucleus matter for the answer?

   **Answer** $c^* = k_{\mathrm{off}}/k_{\mathrm{on}} \approx 0.12\,\mu\mathrm{M}$; by Proposition 29.1.1 the free monomer stays at $0.12\,\mu\mathrm{M}$ and $4.88\,\mu\mathrm{M}$ is polymer. Without the nucleation penalty (isodesmic case) a sizable fraction of subunits would be in short oligomers at all concentrations and there would be no sharp threshold; the weak nucleus makes polymer appear only above $c^*$ and keeps the number of filaments small and their length large.

3. Explain why the yield of complete capsids can fall when the subunit concentration is raised. Design an in vitro experiment that distinguishes this kinetic trap from aggregation into misassembled structures.

   **Answer** At high concentration nucleation, which depends on a higher power of concentration than elongation, outpaces growth: many shells start, free subunits are depleted below the concentration needed to finish any of them, and the partial shells are stable (Figure in 29.1.2, C). Test: follow assembly by light scattering and size-exclusion chromatography or native mass spectrometry. Kinetically trapped intermediates have masses that are fractions of a capsid and convert slowly to complete capsids on dilution or on adding free subunits; misassembled aggregates are larger than a capsid, polydisperse, and do not anneal. Electron microscopy shows open partial shells in the first case and malformed or fused shells in the second.

4. Derive the common-tangent construction from minimizing the free energy of two phases at fixed total volume and solute. Why is the equality of chemical potentials alone not sufficient?

   **Answer** See Theorem 29.2.1. Equal slopes $f'(\phi_A) = f'(\phi_B)$ are satisfied by many pairs of compositions (for example by any two points symmetric about the critical composition in a symmetric $f$ with a linear term added); coexistence also requires that the tangents at both points be the same line, which is the equality of intercepts, $-\Pi$, the osmotic pressure. Physically, solute must be in exchange equilibrium (equal $\mu$) and the two volumes in mechanical equilibrium (equal $\Pi$).

5. Two proteins each have $f$ binding modules with $K_{\mathrm{d}} = 50\,\mu\mathrm{M}$ per module pair. At what concentration does a network form for $f = 3$ and $f = 6$ in the Flory–Stockmayer theory? Why might real gel points be higher?

   **Answer** By Eq. (29.3), $c_{\mathrm{gel}} = 50 \times 2/3 \approx 33\,\mu\mathrm{M}$ for $f = 3$ and $50 \times 5/96 \approx 2.6\,\mu\mathrm{M}$ for $f = 6$. Real gel points are higher because bonds within one pair of molecules (intramolecular loops and multiple bonds between the same two partners) waste stickers without extending the network, which the tree approximation neglects; rigid or short linkers between modules favor such loops, flexible long linkers disfavor them.

6. For the dimensionless Cahn–Hilliard equation $\partial_t\psi = \nabla^2(\psi^3 - \psi - \nabla^2\psi)$, find the fastest-growing wavelength and its growth rate at $\psi_0 = 0$ and $\psi_0 = -0.35$. What happens at $\psi_0 = -0.65$?

   **Answer** $f''(\psi_0) = 3\psi_0^2 - 1$, so $\sigma = q^2(1 - 3\psi_0^2) - q^4$, $q_{\max}^2 = (1 - 3\psi_0^2)/2$, $\sigma_{\max} = (1 - 3\psi_0^2)^2/4$. For $\psi_0 = 0$: $q_{\max} = 0.707$, $\lambda_{\max} = 8.9$, $\sigma_{\max} = 0.25$. For $\psi_0 = -0.35$: $1 - 3\psi_0^2 = 0.6325$, $q_{\max} = 0.562$, $\lambda_{\max} = 11.2$, $\sigma_{\max} = 0.100$. At $\psi_0 = -0.65$, $1 - 3\psi_0^2 = -0.27 < 0$: outside the spinodal ($\lvert\psi_0\rvert > 0.577$), all small perturbations decay and demixing requires nucleation.

7. Using Eq. (29.12), what suction pressure is needed to aspirate a droplet of radius $5\,\mu\mathrm{m}$ with surface tension $0.5\,\mu\mathrm{N\,m^{-1}}$ into a pipette of radius $1\,\mu\mathrm{m}$? Compare with the hydrostatic pressure of a column of water 1 mm high.

   **Answer** $\Delta p = 2(0.5\times10^{-6})(10^6 - 2\times10^5) = 0.8\,\mathrm{Pa}$. A millimeter of water exerts $\rho gh = 10^3 \times 9.8 \times 10^{-3} \approx 9.8\,\mathrm{Pa}$, twelve times more: micropipette aspiration of condensates requires pressure control at the sub-pascal level, and reference pressure drift is the main experimental difficulty.

8. Two P granules of radius $1\,\mu\mathrm{m}$ fuse with a time constant of $1\,\mathrm{s}$; beads of radius $0.1\,\mu\mathrm{m}$ inside them diffuse with $D = 2\times10^{-3}\,\mu\mathrm{m^2\,s^{-1}}$ at $25\,{}^\circ\mathrm{C}$. Estimate the viscosity and surface tension.

   **Answer** $\eta = k_{\mathrm{B}}T/(6\pi Da) = 4.1\times10^{-21}/(6\pi \times 2\times10^{-15} \times 10^{-7}) \approx 1.1\,\mathrm{Pa\,s}$. From $\tau = \eta R/\gamma$, $\gamma = \eta R/\tau = 1.1 \times 10^{-6}/1 \approx 1\,\mu\mathrm{N\,m^{-1}}$.

9. Estimate, with Theorem 29.3.2, how long it would take Ostwald ripening to double the radius of $1\,\mu\mathrm{m}$ nucleoli ($D = 1\,\mu\mathrm{m^2\,s^{-1}}$ for the scaffold, $c_{\mathrm{sat}} = 0.1\,\mu\mathrm{M}$, $\gamma = 1\,\mu\mathrm{N\,m^{-1}}$, $v = 4\times10^{-25}\,\mathrm{m^3}$, $k_{\mathrm{B}}T = 4.3\times10^{-21}\,\mathrm{J}$). What do you conclude about the coexistence of several nucleoli?

   **Answer** The coefficient $8\gamma Dc_{\mathrm{sat}}v^2/(9k_{\mathrm{B}}T) = 8(10^{-6})(10^{-12})(6\times10^{19})(1.6\times10^{-49})/(9 \times 4.3\times10^{-21}) \approx 2\times10^{-27}\,\mathrm{m^3\,s^{-1}}$. Doubling from $1$ to $2\,\mu\mathrm{m}$ requires $\Delta\langle R\rangle^3 = 7\times10^{-18}\,\mathrm{m^3}$, about $3.5\times10^9\,\mathrm{s}$, a century. Ripening is irrelevant on the time scale of the cell cycle; nucleoli coexist because they are nucleated on separate rDNA clusters, held apart by chromatin and reassembled at every mitosis. Fusion upon contact is the only relevant coarsening.

10. In the active-droplet model (29.14), show that the passive critical radius is unstable and find the condition for stability of the larger fixed point. Why does degradation inside droplets, rather than in the dilute phase, stabilize size?

    **Answer** See Proposition 29.5.1: passive $g'(R_{\mathrm{c}}) = \varepsilon^3 > 0$; active, stable if $R^* > 3/(2\varepsilon)$. Degradation inside droplets removes material at a rate proportional to droplet volume, $R^3$, whereas diffusive supply grows with $R$; the net growth of large droplets becomes negative, so that a droplet larger than its neighbors shrinks back. Degradation confined to the dilute phase would only lower the supersaturation, which affects all droplets alike and leaves ripening intact.

11. A condensate occupies $0.5\,\%$ of the nucleus and concentrates an enzyme and its substrate 200-fold each. By how much does it accelerate their encounter rate? What if it occupied $20\,\%$ of the nucleus?

    **Answer** Eq. (29.15) with $K = 200$, $\phi = 0.005$: numerator $0.995 + 0.005 \times 4\times10^4 = 201$, denominator $(0.995 + 1)^2 = 3.98$, so $r/r_0 \approx 50$, the maximum ($K/4$). At $\phi = 0.2$: numerator $0.8 + 8000 = 8001$, denominator $(0.8 + 40)^2 = 1665$, so $r/r_0 \approx 4.8$: a large condensate dilutes the reactants it contains, because the total amounts are fixed.

12. (Open question) Propose a set of measurements to decide whether a nuclear body of interest forms by liquid–liquid phase separation or by binding of its components to a fixed scaffold.

    **Answer** Approach: (a) vary the expression of the putative scaffold over a wide range in single cells and measure the concentrations inside and outside the body: a buffered dilute phase (lever rule) indicates phase separation of a single scaffold, while proportional increases indicate saturable binding to sites; (b) measure fusion events and extract $\eta/\gamma$, checking that $\tau \propto R$; (c) use FRAP on the whole body and on half of it to distinguish internal mixing from exchange with the outside; (d) remove or multiply sticker domains or change valence with oligomerization domains and test whether formation shifts sharply with valence as Eq. (29.3) predicts; (e) induce the body optogenetically (Cry2-fusion seeding) at defined concentrations to map a phase boundary; (f) test for nucleation by seeds (tethering a component to a genomic locus). Consistency across several of these, not one, supports phase separation.
