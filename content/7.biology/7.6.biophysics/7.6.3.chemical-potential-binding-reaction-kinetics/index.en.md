---
title: Chemical Potential, Binding and Reaction Kinetics
description: The chemical potential from a lattice model of a dilute solution; gases, Henry's law and the oxygen cascade; water potential in plants; electrochemical potential; the equilibrium condition and the law of mass action, equilibrium constants from partition functions, and the free energy of ATP hydrolysis in cells; ligand–receptor binding as statistical mechanics and Hill functions; the proton-motive force and the H⁺/ATP ratio set by the c ring; two-state relaxation, detailed balance, Arrhenius and Eyring rates, and the dissipation of reactions out of equilibrium.
---

Cells are chemical systems: their molecules are made and consumed, bind and unbind, cross membranes and react, and their numbers are not fixed. The previous chapter dealt with systems whose particles are conserved; this one adds the variable that governs exchange of particles, the chemical potential, and applies it to the three operations that underlie almost every later model in the course: equilibrium between species (reactions and binding), transport down gradients of chemical and electrochemical potential, and the rates at which equilibrium is approached. It introduces the chemical potential through a lattice model and applies it to gases, water in plants and ions (3.1), derives the law of mass action and the free energy of ATP hydrolysis in a cell (3.2), treats ligand binding as statistical mechanics (3.3), puts numbers on the proton-motive force (3.4), and turns to kinetics, detailed balance and barriers (3.5). The thermodynamics of [6.3.4](/6.3.4), [6.3.5](/6.3.5) and [6.3.7](/6.3.7) and the rate theories of [6.3.16](/6.3.16) are used and not rederived; the biochemistry of binding is in [7.1.7](/7.1.7), of bioenergetics in [7.1.16](/7.1.16) and of chemiosmotic coupling in [7.1.23](/7.1.23). The models of this chapter are the building blocks of the two-state systems of [7.6.4](/7.6.4) and of the gene-regulation models of [7.2.22](/7.2.22).

## 3.1. The Chemical Potential

### 3.1.1. Particles That Come and Go

When the number of molecules of a species can change, the free energy depends on it, and the derivative is the **chemical potential** ([6.3.4](/6.3.4#sec-4.3.1)):

$$
\mu_i = \left(\frac{\partial G}{\partial N_i}\right)_{T,p,N_{j\ne i}}, \qquad \mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_i\mu_i\,\mathrm{d}N_i. \tag{3.1}
$$
It is the free-energy cost of adding one molecule (in biophysics usually per molecule, in units of $k_{\mathrm{B}}T$; in chemistry per mole, in units of $RT$; the two differ by $N_{\mathrm{A}}$). Like temperature and pressure it is an intensive quantity, and like them it equalizes at equilibrium: molecules move from regions, phases or compounds of high chemical potential to those of low chemical potential until the values are equal. Diffusion down a concentration gradient, osmosis, the uptake of oxygen into blood, the binding of a ligand and the progress of a reaction are all instances of this one rule.

In statistical mechanics the chemical potential enters as the Lagrange multiplier of a constraint on the number of particles, just as $\beta$ was that of the energy in [7.6.2](/7.6.2#sec-2.2.2). For a system that can exchange both energy and molecules with a reservoir at temperature $T$ and chemical potential $\mu$, the probability of a microstate with energy $E_i$ and $N_i$ molecules is

$$
p_i = \frac{\mathrm{e}^{-\beta(E_i - \mu N_i)}}{\mathcal{Z}}, \qquad \mathcal{Z} = \sum_i\mathrm{e}^{-\beta(E_i - \mu N_i)}, \qquad \langle N\rangle = k_{\mathrm{B}}T\,\frac{\partial\ln\mathcal{Z}}{\partial\mu}, \tag{3.2}
$$
the Gibbs (grand canonical) distribution: a reservoir of high chemical potential pushes molecules into the system. Equation (3.2) is the form used for binding in 3.3: a binding site is a small system that exchanges ligands with the solution.

### 3.1.2. A Lattice Derivation for Dilute Solutions

**Formula 3.1.1 (Chemical Potential of a Dilute Solute)** In an ideal dilute solution, the chemical potential of a solute at concentration $c$ is

$$
\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{c}{c^\circ}, \tag{3.3}
$$
where $c^\circ$ is a reference concentration (in chemistry $1\,\mathrm{M}$) and $\mu^\circ$ the standard chemical potential, the value at $c = c^\circ$.

**Proof** Model the solution as a lattice of $N$ sites of volume $v$ each, occupied by $N_p$ solute and $N - N_p$ solvent molecules, with energies $\varepsilon_p$ and $\varepsilon_s$ per molecule that include their interactions with the surrounding solvent (for a dilute solution each solute is surrounded only by solvent). The free energy is

$$
G = N_p\varepsilon_p + (N - N_p)\varepsilon_s - k_{\mathrm{B}}T\ln\binom{N}{N_p}.
$$
Adding one solute molecule replaces a solvent molecule; with Stirling's approximation, $\partial\ln\binom{N}{N_p}/\partial N_p = \ln[(N - N_p)/N_p]$, so

$$
\mu_p = \frac{\partial G}{\partial N_p} = \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln\frac{N_p}{N - N_p} \approx \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln(cv)
$$
for $N_p \ll N$, with $c = N_p/(Nv)$. Writing $\ln(cv) = \ln(c/c^\circ) + \ln(c^\circ v)$ gives Eq. (3.3) with $\mu^\circ = \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln(c^\circ v)$. $\square$

The derivation shows what the two terms mean. The logarithmic term is entropic, the mixing entropy of the solute: the more dilute a species, the more ways there are to place it, and the lower its chemical potential. The standard chemical potential collects everything else: the difference of interaction energies of solute and solvent with their surroundings, and a term that depends on the arbitrary choice of $c^\circ$. Only differences of chemical potential at the same standard state have physical meaning. Deviations from ideality, from interactions between solute molecules or from crowding (7.6.23), are absorbed by replacing $c/c^\circ$ by the **activity** $a = \gamma c/c^\circ$ ([6.3.6](/6.3.6)).

### 3.1.3. Gases and Dissolved Gases

For an ideal gas, the same reasoning with partial pressure in place of concentration gives

$$
\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{p}{p^\circ}, \qquad p^\circ = 10^5\,\mathrm{Pa}, \tag{3.4}
$$
with the standard pressure of IUPAC, $1\,\mathrm{bar}$ (older texts use $101\,325\,\mathrm{Pa}$, which shifts $\mu^\circ$ by $k_{\mathrm{B}}T\ln 1.013 = 0.013\,k_{\mathrm{B}}T$). A gas in contact with a liquid dissolves until its chemical potential in solution equals that in the gas; with Eq. (3.3) for the dissolved gas this gives **Henry's law** ([6.3.5](/6.3.5#sec-5.2.1)), $c = k_{\mathrm{H}}p$: the dissolved concentration is proportional to the partial pressure. For oxygen in plasma at $37\,^\circ\mathrm{C}$, $k_{\mathrm{H}} \approx 1.4\,\mu\mathrm{M}$ per mmHg ($10\,\mu\mathrm{M\,kPa^{-1}}$).

**Example 3.1.1 (The oxygen cascade)** Dry air contains 20.95 % oxygen; at a total pressure of $101.3\,\mathrm{kPa}$ its partial pressure is, by **Dalton's law of partial pressures**, $21.2\,\mathrm{kPa}$, or $159\,\mathrm{mmHg}$. On the way to the mitochondria the partial pressure falls step by step:

| Location | $p_{\ce{O2}}$ / mmHg | Reason for the drop |
|---|---|---|
| Dry air | $159$ | |
| Humidified air in the trachea | $149$ | Water vapor ($47\,\mathrm{mmHg}$ at $37\,^\circ\mathrm{C}$) dilutes the gas |
| Alveolar gas | about $100$ | Mixing with air not exchanged at each breath, and uptake into blood |
| Arterial blood | about $95$ | Small alveolar–arterial gradient |
| Mixed venous blood | about $40$ | Uptake by tissues |
| Mitochondria | about $1$–$10$ | Consumption by cytochrome oxidase |

Oxygen moves down this cascade by diffusion alone. The chemical-potential difference between air and mitochondria at $5\,\mathrm{mmHg}$ is $k_{\mathrm{B}}T\ln(159/5) = 3.5\,k_{\mathrm{B}}T$ per molecule ($8.9\,\mathrm{kJ\,mol^{-1}}$), small compared with the $\sim 200\,k_{\mathrm{B}}T$ released when the same molecule is reduced to water. In arterial plasma, Henry's law gives only $0.13\,\mathrm{mM}$ of dissolved oxygen; hemoglobin raises the oxygen content of blood about seventyfold, binding it cooperatively at high partial pressure and releasing it at low ([7.1.7](/7.1.7#sec-7.3)). The physiology of gas exchange belongs to [7.14](/7.14).

### 3.1.4. Water Potential

Water moves between soil, roots, stems, leaves and air without pumps: plants have no heart, and the energy that lifts water to the top of a tree comes from evaporation at the leaves. Its direction is set by the chemical potential of water, which plant physiologists express per unit volume.

**Definition 3.1.1 (Water Potential)** The **water potential** of a sample (a cell, the soil, the xylem sap, the air) is the chemical potential of water in it relative to pure water at the same temperature, at atmospheric pressure and zero height, divided by the partial molar volume of water $\bar V_{\mathrm{w}} = 18.0\,\mathrm{cm^3\,mol^{-1}}$:

$$
\Psi_{\mathrm{w}} = \frac{\mu_{\mathrm{w}} - \mu_{\mathrm{w}}^\circ}{\bar V_{\mathrm{w}}}. \tag{3.5}
$$
It has the units of pressure and is usually given in megapascals; pure free water has $\Psi_{\mathrm{w}} = 0$, and water flows spontaneously from higher to lower $\Psi_{\mathrm{w}}$.

The chemical potential of water is lowered by solutes, raised by pressure, raised by height, and lowered by binding to surfaces; correspondingly

$$
\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}} + \Psi_{\mathrm{g}} + \Psi_{\mathrm{m}}, \qquad
\Psi_{\mathrm{s}} = -cRT, \qquad \Psi_{\mathrm{g}} = \rho_{\mathrm{w}}gh. \tag{3.6}
$$

- The solute (osmotic) potential $\Psi_{\mathrm{s}} = -\Pi$ is the negative of the osmotic pressure of Eq. (2.10) ([7.6.2](/7.6.2#sec-2.3.3)), with $c$ the total concentration of solute particles: $-2.44\,\mathrm{MPa}$ for an ideal $1\,\mathrm{M}$ solution at $20\,^\circ\mathrm{C}$. Real solutions deviate: $1\,\mathrm{M}$ sucrose has about $-2.7\,\mathrm{MPa}$, $1\,\mathrm{M}$ $\ce{KCl}$, which dissociates into about 1.8 osmotically effective particles, about $-4.5\,\mathrm{MPa}$, and seawater about $-2.5\,\mathrm{MPa}$.
- The pressure potential $\Psi_{\mathrm{p}}$ is the hydrostatic pressure above atmospheric: positive in a turgid cell pressing on its wall (turgor, typically $0.3$–$1\,\mathrm{MPa}$), zero at incipient plasmolysis, negative (tension) in the xylem of a transpiring plant.
- The gravitational potential $\Psi_{\mathrm{g}}$ adds $0.0098\,\mathrm{MPa}$ per metre of height: negligible in herbs, about $1\,\mathrm{MPa}$ at the top of a $100\,\mathrm{m}$ tree.
- The matric potential $\Psi_{\mathrm{m}}$ describes water bound to surfaces and held in narrow pores (soil particles, cell walls); it dominates in dry soils and seeds and is usually neglected in hydrated cells.

The air is the strongest sink. Water vapor at relative humidity $\mathrm{RH}$ has $\mu_{\mathrm{w}} - \mu_{\mathrm{w}}^\circ = RT\ln(\mathrm{RH})$ by Eq. (3.4), so

$$
\Psi_{\mathrm{air}} = \frac{RT}{\bar V_{\mathrm{w}}}\ln(\mathrm{RH}), \qquad \frac{RT}{\bar V_{\mathrm{w}}} = 135\,\mathrm{MPa}\ \text{at}\ 20\,^\circ\mathrm{C}, \tag{3.7}
$$
which is $-2.7\,\mathrm{MPa}$ at $98\,\%$ and $-94\,\mathrm{MPa}$ at $50\,\%$ relative humidity.

**Example 3.1.2 (Water flow through a tree)** On a moist day the soil around the roots has $\Psi_{\mathrm{w}} \approx -0.3\,\mathrm{MPa}$, the root xylem about $-0.6\,\mathrm{MPa}$, the stem xylem $10\,\mathrm{m}$ up about $-0.8\,\mathrm{MPa}$ (of which $0.1\,\mathrm{MPa}$ is the gravitational term), the leaf xylem about $-1.0\,\mathrm{MPa}$ and the mesophyll cells about $-1.2\,\mathrm{MPa}$; the air at 50 % humidity is at $-94\,\mathrm{MPa}$. Water flows down this gradient through the whole plant, pulled by evaporation from the leaves and held together as a continuous column under tension by the cohesion of hydrogen-bonded water (the cohesion–tension mechanism). The largest drop is between the leaf and the air, across the stomata, which is why the plant controls its water loss by opening and closing them. The gravitational term and the friction of flow in narrow xylem conduits add up with height; at about $120$–$130\,\mathrm{m}$ the water potential at the top would become so negative that leaf cells could no longer expand and the water columns would break by cavitation, which is the estimated upper limit for tree height. The physiology of water transport is treated in [7.13](/7.13).

![Water potential along the soil–plant–atmosphere continuum of a transpiring tree on a moist day (typical values, 20 °C). Left: schematic tree with the sampling points: soil −0.3 MPa, root xylem −0.6 MPa, stem xylem −0.8 MPa (including 0.1 MPa of gravitational potential at 10 m), leaf xylem −1.0 MPa, mesophyll cells −1.2 MPa and air at 50 % relative humidity −94 MPa. Right: the water potentials in order along the path; water flows passively from higher to lower Ψw, and the value of the air, far off the scale, shows where the driving force comes from](./plots/water-potential.py)

### 3.1.5. Charged Species

For an ion of charge $ze$ at electric potential $\varphi$, the free energy of adding one ion includes the electrical work $ze\varphi$; the relevant quantity is the **electrochemical potential**

$$
\tilde\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{c}{c^\circ} + ze\varphi. \tag{3.8}
$$
Across a membrane permeable to the ion, equilibrium requires $\tilde\mu_{\mathrm{in}} = \tilde\mu_{\mathrm{out}}$, which gives the **Nernst equation** ([6.3.13](/6.3.13)) for the equilibrium potential,

$$
\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = \frac{k_{\mathrm{B}}T}{ze}\ln\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}} = \frac{61.5\,\mathrm{mV}}{z}\lg\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}}\quad(37\,^\circ\mathrm{C}), \tag{3.9}
$$
with $k_{\mathrm{B}}T/e = 26.7\,\mathrm{mV}$ at $310\,\mathrm{K}$ ($25.7\,\mathrm{mV}$ at $298\,\mathrm{K}$, where the prefactor is $59.2\,\mathrm{mV}$). A tenfold concentration ratio of a monovalent ion is worth $61.5\,\mathrm{mV}$, or $2.3\,k_{\mathrm{B}}T$ per ion. Membrane potentials and their origin in ion gradients and permeabilities are the subject of 7.6.30; here we use Eq. (3.8) for protons.

## 3.2. Chemical Equilibrium and the Law of Mass Action

### 3.2.1. The Equilibrium Condition

Write a reaction as $\sum_i\nu_i\mathrm{X}_i = 0$, with stoichiometric coefficients $\nu_i$ negative for reactants and positive for products ($\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$ has $\nu_{\mathrm{A}} = \nu_{\mathrm{B}} = -1$, $\nu_{\mathrm{AB}} = 1$). When the reaction advances by one event, $\mathrm{d}N_i = \nu_i$.

**Theorem 3.2.1 (Law of Mass Action)** At constant temperature and pressure, a reaction is at equilibrium when

$$
\sum_i\nu_i\mu_i = 0. \tag{3.10}
$$
For ideal dilute solutes this is equivalent to

$$
\prod_i\left(\frac{c_i}{c^\circ}\right)^{\nu_i} = K, \qquad K = \exp\!\left(-\frac{\sum_i\nu_i\mu_i^\circ}{k_{\mathrm{B}}T}\right) = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}, \tag{3.11}
$$
where the equilibrium constant $K$ does not depend on the concentrations.

**Proof** One event changes $G$ by $\mathrm{d}G = \sum_i\mu_i\,\mathrm{d}N_i = \sum_i\nu_i\mu_i$. At equilibrium $G$ is minimal with respect to the extent of reaction, so this derivative vanishes, Eq. (3.10). Inserting Eq. (3.3), $\sum_i\nu_i\mu_i^\circ + k_{\mathrm{B}}T\sum_i\nu_i\ln(c_i/c^\circ) = 0$, and exponentiating gives Eq. (3.11). $\square$

Equation (3.11) is the **law of mass action** ([6.3.7](/6.3.7#sec-7.2.1)) for the **standard equilibrium constant**. For binding, $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$, biologists use its inverse with dimensions restored, the **dissociation constant**

$$
K_{\mathrm{d}} = \frac{[\mathrm{A}][\mathrm{B}]}{[\mathrm{AB}]} = c^\circ\,\mathrm{e}^{\Delta G^\circ_{\mathrm{bind}}/k_{\mathrm{B}}T}, \tag{3.12}
$$
a concentration: the free concentration of A at which half of B is bound. A binding free energy of $-20.7\,k_{\mathrm{B}}T$ ($-53\,\mathrm{kJ\,mol^{-1}}$ at $310\,\mathrm{K}$) corresponds to $K_{\mathrm{d}} = 1\,\mathrm{nM}$, and each $2.3\,k_{\mathrm{B}}T$ changes $K_{\mathrm{d}}$ tenfold.

### 3.2.2. The Free Energy of a Reaction away from Equilibrium

If the concentrations are not at equilibrium, one reaction event changes $G$ by

$$
\Delta G = \sum_i\nu_i\mu_i = \Delta G^\circ + k_{\mathrm{B}}T\ln Q, \qquad Q = \prod_i\left(\frac{c_i}{c^\circ}\right)^{\nu_i}, \tag{3.13}
$$
the **reaction isotherm** ([6.3.7](/6.3.7)) with the **reaction quotient** $Q$; $\Delta G = k_{\mathrm{B}}T\ln(Q/K)$. The reaction runs forward if $\Delta G < 0$, that is, if $Q < K$. The standard free energy $\Delta G^\circ$ says how far the equilibrium lies to one side; the actual $\Delta G$, which also depends on the concentrations, says in which direction the reaction will go and how much work it can do. Judging the direction of a reaction in a cell from $\Delta G^\circ$ alone is a common mistake, since cellular concentrations are far from $1\,\mathrm{M}$. The standard free energy is meaningful as a measure of stability when it is compared between related reactions under the same conditions (the effect of a mutation on folding or binding), which is how it is used in 7.6.8 and 7.6.16.

### 3.2.3. Equilibrium Constants from Partition Functions

The standard chemical potentials, and hence $K$, can be computed from molecular partition functions ([6.3.11](/6.3.11)). For an ideal gas or dilute solution of $N_i$ molecules of species $i$ with molecular partition function $q_i$, the free energy is $-k_{\mathrm{B}}T\ln\prod_i(q_i^{N_i}/N_i!)$, so $\mu_i = -k_{\mathrm{B}}T\ln(q_i/N_i)$, and Eq. (3.10) becomes

$$
\prod_i\left(\frac{N_i}{V}\right)^{\nu_i} = \prod_i\left(\frac{q_i}{V}\right)^{\nu_i}. \tag{3.14}
$$
The equilibrium constant is a ratio of the numbers of states available per volume to products and reactants, each weighted by its Boltzmann factor (which is contained in $q_i$, with all energies measured from a common zero). A reaction is favored by a lower energy of products and by more states: two molecules have more translational states than their complex, which is why binding must overcome a loss of translational and rotational entropy of some $10$–$15\,k_{\mathrm{B}}T$ at $1\,\mathrm{M}$ (7.6.17).

### 3.2.4. ATP Hydrolysis in the Cell

**Example 3.2.1 (How much free energy does one ATP deliver?)** For $\ce{ATP + H2O -> ADP + P_i}$ at pH 7, with the biochemical standard state ($1\,\mathrm{M}$ of each species except water and protons), $\Delta G^{\circ\prime} \approx -30.5\,\mathrm{kJ\,mol^{-1}}$, about $-12\,k_{\mathrm{B}}T$ per molecule at $310\,\mathrm{K}$ (the exact value depends on $\ce{Mg^2+}$, pH and ionic strength; values near $-13\,k_{\mathrm{B}}T$ are also quoted). In *E. coli*, with $[\mathrm{ATP}] \approx 5\,\mathrm{mM}$, $[\mathrm{ADP}] \approx 0.5\,\mathrm{mM}$ and $[\mathrm{P_i}] \approx 10\,\mathrm{mM}$,

$$
Q = \frac{[\mathrm{ADP}][\mathrm{P_i}]}{[\mathrm{ATP}]} = \frac{(0.5\times10^{-3})(10^{-2})}{5\times10^{-3}} = 10^{-3}, \qquad
\Delta G \approx -12\,k_{\mathrm{B}}T + k_{\mathrm{B}}T\ln10^{-3} \approx -19\,k_{\mathrm{B}}T,
$$
about $-48\,\mathrm{kJ\,mol^{-1}}$. In resting muscle, where free ADP is only about $20\,\mu\mathrm{M}$, $\Delta G \approx -24\,k_{\mathrm{B}}T$ ($-61\,\mathrm{kJ\,mol^{-1}}$). At equilibrium $Q$ would be $K = \mathrm{e}^{11.8} \approx 1.4\times10^5$: the ratio $[\mathrm{ATP}]/[\mathrm{ADP}]$ in a living cell is some eight to nine orders of magnitude above its equilibrium value, and this displacement, not the chemistry of the phosphoanhydride bond as such, is what makes ATP a store of free energy. The free energy of ATP hydrolysis under cellular conditions, the **phosphorylation potential** ([7.1.16](/7.1.16#sec-16.3.2)), is about $20\,k_{\mathrm{B}}T$, the value used throughout this course.

![The free energy of ATP hydrolysis against the mass-action ratio Q = [ADP][Pi]/[ATP] (in M), ΔG = ΔG°′ + RT ln Q at 310 K with ΔG°′ = −30.5 kJ/mol (about −12 kBT), in units of kBT (left) and kJ/mol (right). Points: the standard state (all species at 1 M), equilibrium (ΔG = 0 at Q ≈ 1.4 × 10⁵ M), an *E. coli* cell (Q = 10⁻³ M, about −19 kBT) and resting muscle (Q ≈ 7.5 × 10⁻⁶ M, about −24 kBT); each factor of 10 in Q changes ΔG by 2.3 kBT](./plots/atp-free-energy.py)

## 3.3. Binding as Statistical Mechanics

### 3.3.1. A Receptor in a Lattice of Ligands

The binding of a **ligand** to a receptor, a transcription factor to DNA, oxygen to myoglobin or a drug to its target is the simplest reaction in biology, and it can be treated from first principles in a toy model.

**Theorem 3.3.1 (Occupancy of a Single Site)** Let a receptor be in a solution modeled as a lattice of $\Omega$ sites, containing $L \ll \Omega$ ligand molecules. Each ligand in solution has energy $\varepsilon_{\mathrm{s}}$, a ligand bound to the receptor has energy $\varepsilon_{\mathrm{b}}$, and $\Delta\varepsilon = \varepsilon_{\mathrm{b}} - \varepsilon_{\mathrm{s}}$. The probability that the receptor is occupied is

$$
p_{\mathrm{b}} = \frac{c/K_{\mathrm{d}}}{1 + c/K_{\mathrm{d}}} = \frac{c}{c + K_{\mathrm{d}}}, \qquad K_{\mathrm{d}} = c_0\,\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}, \tag{3.15}
$$
where $c = L/V$ is the ligand concentration and $c_0 = \Omega/V$ the concentration of lattice sites.

**Proof** The two macrostates of the receptor are empty and occupied. Empty: all $L$ ligands are in solution, with $\binom{\Omega}{L} \approx \Omega^L/L!$ arrangements and weight $(\Omega^L/L!)\mathrm{e}^{-\beta L\varepsilon_{\mathrm{s}}}$. Occupied: one ligand is bound and $L - 1$ are in solution, with weight $\mathrm{e}^{-\beta\varepsilon_{\mathrm{b}}}(\Omega^{L-1}/(L-1)!)\mathrm{e}^{-\beta(L-1)\varepsilon_{\mathrm{s}}}$. The ratio of the occupied to the empty weight is $(L/\Omega)\mathrm{e}^{-\beta\Delta\varepsilon} = (c/c_0)\mathrm{e}^{-\beta\Delta\varepsilon} = c/K_{\mathrm{d}}$, and $p_{\mathrm{b}}$ is this ratio divided by one plus the ratio. $\square$

The result is the hyperbolic binding curve of biochemistry, and the model says what $K_{\mathrm{d}}$ is: a concentration scale set by the binding energy (through the Boltzmann factor) and by the entropy of the free ligand (through $c_0$, the concentration at which a ligand has as little positional entropy in solution as on the receptor). The approximation $\binom{\Omega}{L} \approx \Omega^L/L!$ is the dilute limit; the exact lattice result, $c/K_{\mathrm{d}}$ replaced by $(L/(\Omega - L + 1))\mathrm{e}^{-\beta\Delta\varepsilon}$, departs from Eq. (3.15) only when the ligand fills a sizable fraction of the lattice.

**Example 3.3.1 (RNA polymerase at a promoter)** In *E. coli* nearly all of the roughly $10^3$ RNA polymerase molecules are bound to DNA, most of them nonspecifically. Model the genome as $N_{\mathrm{NS}} \approx 5\times10^6$ nonspecific sites with binding energy $\varepsilon_{\mathrm{NS}}$ and one promoter with energy $\varepsilon_{\mathrm{S}}$, shared by $P$ polymerases. Counting the arrangements as in Theorem 3.3.1, with the nonspecific sites playing the role of the lattice and $P \ll N_{\mathrm{NS}}$, the promoter is occupied with probability

$$
p_{\mathrm{bound}} = \frac{1}{1 + \dfrac{N_{\mathrm{NS}}}{P}\,\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}}, \qquad \Delta\varepsilon = \varepsilon_{\mathrm{S}} - \varepsilon_{\mathrm{NS}}.
$$
With $P = 500$ polymerases available and $\Delta\varepsilon = -5\,k_{\mathrm{B}}T$, $(N_{\mathrm{NS}}/P)\mathrm{e}^{\Delta\varepsilon} = 10^4\times6.7\times10^{-3} = 67$ and $p_{\mathrm{bound}} \approx 0.015$; a strong promoter with $\Delta\varepsilon = -12\,k_{\mathrm{B}}T$ is occupied 94 % of the time. The genome itself acts as the solvent, the ratio $P/N_{\mathrm{NS}}$ as the concentration, and the occupancy rises with the number of polymerases exactly as a binding curve rises with ligand concentration. Regulators that bind next to the promoter change its effective $\Delta\varepsilon$; this is the starting point of the **thermodynamic model** of gene regulation ([7.2.11](/7.2.11)).

![Ligand binding as statistical mechanics. A, B: occupancy p_b = cⁿ/(cⁿ + Kⁿ) for a simple site (n = 1) and for all-or-none binding of n = 2 and 4 ligands with the same half-saturation concentration K, on linear (A) and logarithmic (B) concentration axes; dotted lines in B mark 10 % and 90 % occupancy, between which c changes 81-fold for n = 1, 9-fold for n = 2 and 3-fold for n = 4. C: the lattice model of Theorem 3.3.1 with Ω = 1000 sites and Δε = −2 kBT: the exact occupancy (points) follows the dilute result c/(c + K_d) (line) while the ligand is dilute and exceeds it as the lattice fills](./plots/binding-curves.py)

### 3.3.2. Two Routes to the Same Result

The same occupancy follows from two other descriptions, and seeing that they agree is the point.

- Chemical potential: treat the site as a system exchanging ligands with a reservoir of chemical potential $\mu = \mu^\circ + k_{\mathrm{B}}T\ln(c/c^\circ)$ (Eq. (3.3)). By Eq. (3.2) with two states, empty ($E = 0$, $N = 0$) and occupied ($E = \varepsilon_{\mathrm{b}}$, $N = 1$), $p_{\mathrm{b}} = \mathrm{e}^{-\beta(\varepsilon_{\mathrm{b}} - \mu)}/[1 + \mathrm{e}^{-\beta(\varepsilon_{\mathrm{b}} - \mu)}]$, which is Eq. (3.15) with $K_{\mathrm{d}} = c^\circ\mathrm{e}^{\beta(\varepsilon_{\mathrm{b}} - \mu^\circ)}$.
- Mass action: for $\mathrm{R} + \mathrm{L} \rightleftharpoons \mathrm{RL}$, $[\mathrm{R}][\mathrm{L}]/[\mathrm{RL}] = K_{\mathrm{d}}$ (Eq. (3.12)), and $p_{\mathrm{b}} = [\mathrm{RL}]/([\mathrm{R}] + [\mathrm{RL}]) = [\mathrm{L}]/([\mathrm{L}] + K_{\mathrm{d}})$.

The statistical-mechanical routes give $K_{\mathrm{d}}$ in terms of energies; the thermodynamic route gives it in terms of a measured standard free energy. In models of gene regulation, the same reasoning applied to a promoter with several binding sites and polymerase is the **thermodynamic model** of [7.2.11](/7.2.11).

### 3.3.3. Hill Functions

If a receptor binds $n$ ligands and the intermediate states with fewer ligands are negligibly populated (all-or-none binding, $\mathrm{R} + n\mathrm{L} \rightleftharpoons \mathrm{RL}_n$), mass action gives $[\mathrm{R}][\mathrm{L}]^n/[\mathrm{RL}_n] = K^n$ and

$$
p_{\mathrm{b}} = \frac{c^n}{c^n + K^n}, \tag{3.16}
$$
the **Hill equation** ([7.1.7](/7.1.7#sec-7.3.4)), sigmoidal for $n > 1$. Its steepness is measured by the **Hill coefficient**: the concentration ratio between 10 % and 90 % occupancy is $81^{1/n}$, 81-fold for $n = 1$, 9-fold for $n = 2$, 3-fold for $n = 4$. Real receptors populate their intermediate states, and the measured Hill coefficient (the slope of $\ln[p_{\mathrm{b}}/(1 - p_{\mathrm{b}})]$ against $\ln c$ at half saturation) lies between 1 and the number of sites; for hemoglobin, with four sites, it is about 2.8. A Hill function is a phenomenological description; the mechanisms that produce **cooperativity**, interactions between sites and concerted conformational changes, are modeled in [7.6.4](/7.6.4), and the steep responses of signaling cascades, which can exceed the Hill coefficient of any single binding step, in 7.6.35.

### 3.3.4. Measuring Binding

A binding curve is measured by varying the ligand concentration and recording a signal proportional to the fraction bound: a change of fluorescence or of fluorescence anisotropy when a labeled ligand binds a larger partner (7.6.11), the heat released in each step of a titration (isothermal titration calorimetry, 7.6.8), the mass accumulating on a surface carrying the receptor (surface plasmon resonance, 7.6.17), or the radioactivity retained on a filter with the complex. Fitting Eq. (3.15) gives $K_{\mathrm{d}}$, provided that $c$ is the free ligand concentration: if the receptor concentration is comparable to $K_{\mathrm{d}}$, binding depletes the ligand and the total concentration must be corrected by the quadratic solution of the mass-action equations. The temperature dependence of $K_{\mathrm{d}}$ gives the binding enthalpy by the van 't Hoff relation, and a direct calorimetric measurement gives it independently; comparing the two tests whether binding is a simple two-state process (7.6.8).

## 3.4. The Proton-Motive Force, Quantitatively

### 3.4.1. Two Components

The **chemiosmotic theory** of Peter Mitchell ([7.1.23](/7.1.23#sec-23.2.2)) states that respiratory and photosynthetic electron transport pumps protons across a membrane, and that the free energy stored in the resulting gradient drives **ATP synthase**. By Eq. (3.8), moving one proton from the outside (the intermembrane space of a mitochondrion, the periplasm of a bacterium, the lumen of a thylakoid) to the inside changes the free energy by $\tilde\mu_{\mathrm{in}} - \tilde\mu_{\mathrm{out}} = k_{\mathrm{B}}T\ln(c_{\mathrm{in}}/c_{\mathrm{out}}) + e\,\Delta\Psi$, with $\Delta\Psi = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$. With $\mathrm{pH} = -\lg a_{\ce{H+}}$, $\ln(c_{\mathrm{in}}/c_{\mathrm{out}}) = -2.303\,\Delta\mathrm{pH}$ with $\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{in}} - \mathrm{pH}_{\mathrm{out}}$. Dividing by $e$ (or, per mole, by $F$) gives a potential.

**Formula 3.4.1 (Proton-Motive Force)** The **proton-motive force** across a membrane is

$$
\Delta p = \Delta\Psi - \frac{2.303\,RT}{F}\,\Delta\mathrm{pH}, \qquad \frac{2.303\,RT}{F} = 61.5\,\mathrm{mV}\ (37\,^\circ\mathrm{C}),\ 59.2\,\mathrm{mV}\ (25\,^\circ\mathrm{C}), \tag{3.17}
$$
with $\Delta\Psi = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$ and $\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{in}} - \mathrm{pH}_{\mathrm{out}}$. The free energy released by one mole of protons flowing inward is $\Delta G = F\,\Delta p$, negative for an energized membrane (inside negative and alkaline).

The 59 mV often quoted is the value at $25\,^\circ\mathrm{C}$; at body temperature the factor is $61.5\,\mathrm{mV}$ per pH unit. The two components are interconvertible: a membrane that lets a counterion pass collapses $\Delta\Psi$ and builds up $\Delta\mathrm{pH}$, and the balance between them differs between membranes.

### 3.4.2. Mitochondria, Bacteria and Chloroplasts

**Example 3.4.1 (The proton-motive force of liver mitochondria)** With $\Delta\Psi \approx -170\,\mathrm{mV}$ (matrix negative) and $\Delta\mathrm{pH} \approx +0.5$ (matrix alkaline), Eq. (3.17) gives

$$
\Delta p = -170\,\mathrm{mV} - 61.5\,\mathrm{mV}\times0.5 \approx -201\,\mathrm{mV},
$$
of which 85 % is electrical. Each proton entering the matrix releases $F\,\lvert\Delta p\rvert = 96\,485\,\mathrm{C\,mol^{-1}}\times0.201\,\mathrm{V} = 19.4\,\mathrm{kJ\,mol^{-1}}$, $7.5\,k_{\mathrm{B}}T$ per proton.

In *E. coli* at an external pH of 7 the proton-motive force is of the same magnitude, mostly electrical. In illuminated chloroplasts it is mostly chemical: the thylakoid membrane is permeable to $\ce{Cl-}$ and $\ce{Mg^2+}$, which neutralize the charge of the pumped protons, so the lumen acidifies by 2–3 pH units below the stroma while $\Delta\Psi$ stays small.

![The proton-motive force, quantitatively (310 K). A: electrical (ΔΨ) and chemical (61.5 mV × ΔpH) components for typical energized membranes: mammalian mitochondria (170 mV and 0.5 pH unit, total about 200 mV), *E. coli* at external pH 7 (140 mV and 0.4, about 165 mV) and chloroplast thylakoids in the light (about 30 mV and 2.5 pH units, about 185 mV). B: the largest phosphorylation potential an ATP synthase with a c ring of c subunits can sustain, (c/3)FΔp, at Δp = 150 and 200 mV, compared with the phosphorylation potential in cells (shaded, 45–60 kJ/mol); points mark known ring sizes: c8 in bovine mitochondria, c10 in yeast mitochondria and *E. coli*, c14 in chloroplasts and c15 in some cyanobacteria](./plots/proton-motive-force.py)

### 3.4.3. How Many Protons per ATP?

To make one ATP against a phosphorylation potential $\Delta G_{\mathrm{p}}$, ATP synthase must let at least $n_{\min} = \Delta G_{\mathrm{p}}/(F\,\lvert\Delta p\rvert)$ protons through. In the mitochondrial matrix $\Delta G_{\mathrm{p}} \approx 50\,\mathrm{kJ\,mol^{-1}}$, so $n_{\min} \approx 50/19.4 \approx 2.6$: thermodynamics requires more than two protons per ATP, not merely one.

The actual number is fixed by the structure of the enzyme ([7.1.23](/7.1.23#sec-23.3.4)). Each proton passing through $\mathrm{F_o}$ turns the c ring by one subunit, and one full turn of the ring and of the γ shaft makes three ATP at the three catalytic sites of $\mathrm{F_1}$ ([7.1.23](/7.1.23#sec-23.3.3)). A ring of $c$ subunits therefore gives $c/3$ protons per ATP: $8/3 = 2.7$ for the c₈ ring of animal mitochondria, $10/3 = 3.3$ for yeast mitochondria and *E. coli*, $14/3 = 4.7$ for chloroplasts. The mammalian enzyme works close to the thermodynamic limit: $2.7\times19.4\,\mathrm{kJ\,mol^{-1}} = 52\,\mathrm{kJ\,mol^{-1}}$, just above the phosphorylation potential it maintains. Chloroplasts, with a larger ring, can make ATP at a lower proton-motive force per proton, or against a higher $\Delta G_{\mathrm{p}}$. Exporting each ATP from the matrix to the cytosol costs about one more proton (the phosphate carrier imports $\mathrm{P_i}$ with a proton, and the adenine nucleotide translocase exchanges $\ce{ATP^4-}$ for $\ce{ADP^3-}$ against the membrane potential), so a cytosolic ATP costs about $3.7$ protons, which with ten protons pumped per NADH oxidized gives the P/O ratio of about $2.7$ ([7.1.23](/7.1.23#sec-23.3.5)).

## 3.5. Rates

### 3.5.1. Relaxation of a Two-State Reaction

Equilibrium says where a system ends up, not how fast it gets there. For the simplest reaction, $\mathrm{S} \rightleftharpoons \mathrm{P}$ with rate constants $k_+$ (S to P) and $k_-$ (P to S) and total concentration $C = [\mathrm{S}] + [\mathrm{P}]$, the fraction $x = [\mathrm{P}]/C$ obeys a **first-order reaction** equation.

**Formula 3.5.1 (Two-State Relaxation)** The fraction in state P obeys

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = k_+(1 - x) - k_-x, \qquad
x(t) = x_{\mathrm{eq}} + [x(0) - x_{\mathrm{eq}}]\,\mathrm{e}^{-t/\tau}, \qquad
x_{\mathrm{eq}} = \frac{k_+}{k_+ + k_-}, \quad \tau = \frac{1}{k_+ + k_-}. \tag{3.18}
$$

Two features are general. The **relaxation time** $\tau$ is set by the sum of the two rate constants, not by either one alone: a reaction relaxes faster than its slower direction would suggest. And the equilibrium depends only on the ratio $k_+/k_-$, the relaxation only on the sum; measuring both the equilibrium and the relaxation (for example after a jump in temperature, the **relaxation method** of [6.3.15](/6.3.15)) therefore determines both rate constants.

![Kinetics of a two-state reaction S ⇌ P. A: a free-energy profile along a reaction coordinate: P lies about 2 kBT below S, and the transition state about 12 kBT above S. B: relaxation of the fraction x in P from x = 0 (solid) and from x = 1 (dashed) with k₊ = 0.88 and k₋ = 0.12 in units of 1/τ: both reach x_eq = k₊/(k₊ + k₋) = 0.88 with the same time constant τ = 1/(k₊ + k₋). C: the Eyring rate k = (kBT/h) e^(−ΔG‡/kBT) at 310 K against the barrier, with the mean waiting times 1/k of 1 ns, 1 µs, 1 ms, 1 s, 1 h and 1 yr marked: each 2.3 kBT of barrier slows the reaction tenfold](./plots/two-state-kinetics.py)

### 3.5.2. Detailed Balance

The equilibrium fraction can be computed in three ways: from the kinetics, $x_{\mathrm{eq}} = k_+/(k_+ + k_-)$; from mass action, $[\mathrm{P}]/[\mathrm{S}] = K$; and from the Boltzmann distribution of macrostates (Eq. (2.6)), $[\mathrm{P}]/[\mathrm{S}] = \mathrm{e}^{-\Delta G/k_{\mathrm{B}}T}$ with $\Delta G = G_{\mathrm{P}} - G_{\mathrm{S}}$. They must agree.

**Theorem 3.5.1 (Detailed Balance for a Reaction)** At equilibrium the forward and backward fluxes of every elementary reaction are equal, and the ratio of the rate constants is fixed by thermodynamics:

$$
k_+[\mathrm{S}]_{\mathrm{eq}} = k_-[\mathrm{P}]_{\mathrm{eq}}, \qquad \frac{k_+}{k_-} = K = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}. \tag{3.19}
$$
For an elementary reaction $\sum_s\nu_s\mathrm{S}_s \rightleftharpoons \sum_p\nu_p\mathrm{P}_p$ with mass-action fluxes $J_+ = k_+\prod_sc_s^{\nu_s}$ and $J_- = k_-\prod_pc_p^{\nu_p}$, equilibrium ($J_+ = J_-$) combined with Eq. (3.11) gives $k_+/k_- = K$ in the units of $c^\circ$.

This is the principle of **detailed balance** ([3.5.9](/3.5.9)): at equilibrium each process is balanced by its reverse, not merely the total production and consumption of each species. It constrains models: in a network of reactions with a closed loop, the product of the forward rate constants around the loop divided by the product of the backward ones must equal 1 at equilibrium (the free energy is a state function), so the rate constants of a cycle are not independent. Detailed balance is a property of equilibrium. It must be distinguished from a **steady state**, in which concentrations are constant but net fluxes may run around cycles; the steady states of living cells, maintained by ATP, are exactly the states in which detailed balance is broken (3.5.4).

### 3.5.3. Barriers: Arrhenius and Eyring

The ratio $k_+/k_-$ is fixed by the free-energy difference, but the rates themselves are set by the barrier between the states. Transition state theory ([6.3.16](/6.3.16#sec-16.3)) gives the **Eyring equation**

$$
k = \kappa\,\frac{k_{\mathrm{B}}T}{h}\,\mathrm{e}^{-\Delta G^\ddagger/k_{\mathrm{B}}T}, \tag{3.20}
$$
with transmission coefficient $\kappa \le 1$ and $k_{\mathrm{B}}T/h = 6.5\times10^{12}\,\mathrm{s^{-1}}$ at $310\,\mathrm{K}$. Both directions cross the same transition state, $\Delta G^\ddagger_- = \Delta G^\ddagger_+ - \Delta G$, so Eq. (3.20) satisfies Eq. (3.19) automatically. A barrier of $30\,k_{\mathrm{B}}T$ gives about one event per second, and each additional $2.3\,k_{\mathrm{B}}T$ slows the reaction tenfold.

An enzyme lowers $\Delta G^\ddagger$ without changing $\Delta G$: it speeds both directions by the same factor and leaves the equilibrium untouched. A rate enhancement of $10^{10}$, typical of enzymes, corresponds to lowering the barrier by $23\,k_{\mathrm{B}}T$ ([7.1.8](/7.1.8)).

**Example 3.5.1 (Temperature coefficients)** The empirical **Arrhenius equation** $k = A\,\mathrm{e}^{-E_{\mathrm{a}}/RT}$ gives the ratio of rates at $310$ and $300\,\mathrm{K}$, the $Q_{10}$, as $\exp[(E_{\mathrm{a}}/R)(1/300 - 1/310)\,\mathrm{K^{-1}}]$: $1.9$ for $E_{\mathrm{a}} = 50\,\mathrm{kJ\,mol^{-1}}$ and $3.6$ for $100\,\mathrm{kJ\,mol^{-1}}$. Most enzymatic and physiological rates have $Q_{10}$ between 2 and 3, which is why the metabolism of an ectotherm slows severalfold in cold weather. Much steeper temperature dependences, $Q_{10}$ of 10 to 100, signal something other than a single barrier: the large enthalpy changes of the temperature-gated channels of thermosensation (7.6.4) or of protein unfolding (7.6.8).

For conformational changes of macromolecules in water, the prefactor $k_{\mathrm{B}}T/h$ of Eq. (3.20), the frequency of crossing a barrier in a gas, is not appropriate: the motion along the reaction coordinate is overdamped by the solvent, and the prefactor is set by friction. The theory for that case, that of Kramers, requires the theory of Brownian motion and is developed in 7.6.5; it gives prefactors of $10^6$–$10^8\,\mathrm{s^{-1}}$ for protein folding, the "speed limit" of 7.6.16.

### 3.5.4. Reactions out of Equilibrium

For an elementary reaction with mass-action fluxes $J_\pm$, Eqs. (3.11), (3.13) and (3.19) combine into a relation between the fluxes and the thermodynamic driving force $\Delta\mu = -\Delta G = -\sum_i\nu_i\mu_i$ (the free energy released per event):

$$
\frac{J_+}{J_-} = \mathrm{e}^{\Delta\mu/k_{\mathrm{B}}T}, \qquad \dot W = (J_+ - J_-)\,\Delta\mu = k_{\mathrm{B}}T\,(J_+ - J_-)\ln\frac{J_+}{J_-} \ge 0. \tag{3.21}
$$
The net flux runs in the direction of $\Delta\mu$, and the free energy is dissipated at the rate $\dot W$ (per unit volume), which vanishes only at equilibrium. The inequality holds because $(a - b)\ln(a/b) \ge 0$ for any positive $a, b$: it is the second law, $\mathrm{d}_{\mathrm{i}}S \ge 0$ ([7.6.2](/7.6.2#sec-2.5.1)), for one reaction.

Equation (3.21) also shows what a cell does with ATP. Consider an enzyme that cycles through three states, binding ATP, hydrolyzing it and releasing the products. Around the cycle, detailed balance would require the product of forward rate constants (each multiplied by the relevant concentrations) to equal that of the backward ones; with ATP and ADP held away from equilibrium, the ratio is instead $\mathrm{e}^{\Delta\mu_{\mathrm{ATP}}/k_{\mathrm{B}}T} \approx \mathrm{e}^{20}$, and the cycle turns preferentially in one direction. Molecular motors (7.6.27), kinetic proofreading ([7.2.22](/7.2.22#sec-22.7), 7.6.17), sensory adaptation (7.6.35) and biochemical clocks (7.6.38) are all cycles of this kind, and the theory of their fluxes and dissipation, stochastic thermodynamics, is developed in 7.6.38.

### 3.5.5. Cells as Chemical Factories

A cell whose composition is constant is not static: its molecules are continuously made and degraded, metabolites are converted into one another in seconds, and even its structural elements turn over. Rate equations describe this flux. The level of a molecule made at rate $\beta$ and removed at rate $\gamma$ obeys $\mathrm{d}n/\mathrm{d}t = \beta - \gamma n$, a first-order relaxation toward the steady state $\beta/\gamma$ with time constant $1/\gamma$ (Formula 3.5.1 with one state held fixed); proteins in growing bacteria are removed mainly by dilution, $\gamma = \ln 2/\tau_{\mathrm{doubling}}$ ([7.2.22](/7.2.22#sec-22.3)). The cytoskeleton gives a second example. An actin filament grows at its barbed end by adding monomers at rate $k_{\mathrm{on}}c$ and losing them at rate $k_{\mathrm{off}}$, so its length changes as

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = \delta\,(k_{\mathrm{on}}c - k_{\mathrm{off}}), \qquad c_{\mathrm{c}} = \frac{k_{\mathrm{off}}}{k_{\mathrm{on}}}, \tag{3.22}
$$
with $\delta = 2.7\,\mathrm{nm}$ per subunit: it grows above the critical concentration $c_{\mathrm{c}}$ and shrinks below it, and by detailed balance $c_{\mathrm{c}}$ is the dissociation constant of a subunit from the filament end. With $k_{\mathrm{on}} \approx 11\,\mu\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} \approx 1.4\,\mathrm{s^{-1}}$, $c_{\mathrm{c}} \approx 0.13\,\mu\mathrm{M}$, and at $10\,\mu\mathrm{M}$ actin a filament grows by about $110$ subunits, $0.3\,\mu\mathrm{m}$, per second, the speed at which the leading edge of a crawling cell advances. Because ATP hydrolysis in the filament makes the two ends differ, the steady state of a filament in a cell is not an equilibrium, and filaments treadmill (7.6.26).

## Summary

- Chemical potential (3.1): $\mu = \partial G/\partial N$ is the free-energy cost of one molecule; for a dilute solute $\mu = \mu^\circ + k_{\mathrm{B}}T\ln(c/c^\circ)$ (Formula 3.1.1), from the mixing entropy of a lattice model, and for a gas $\mu^\circ + k_{\mathrm{B}}T\ln(p/p^\circ)$ with $p^\circ = 10^5\,\mathrm{Pa}$, Eq. (3.4). Oxygen descends a cascade of partial pressures from $159\,\mathrm{mmHg}$ in air to a few mmHg in mitochondria by diffusion (Example 3.1.1). Water potential $\Psi_{\mathrm{w}} = (\mu_{\mathrm{w}} - \mu^\circ_{\mathrm{w}})/\bar V_{\mathrm{w}}$ (Definition 3.1.1) is the sum of solute, pressure, gravitational and matric terms, Eq. (3.6), and drives water from soil ($-0.3\,\mathrm{MPa}$) to air ($-94\,\mathrm{MPa}$ at 50 % humidity) (Example 3.1.2). For ions the electrochemical potential adds $ze\varphi$, Eq. (3.8), and gives the Nernst equation, $61.5\,\mathrm{mV}$ per decade at $37\,^\circ\mathrm{C}$, Eq. (3.9).
- Equilibrium (3.2): $\sum\nu_i\mu_i = 0$ gives the law of mass action $\prod(c_i/c^\circ)^{\nu_i} = K = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}$ (Theorem 3.2.1); $K_{\mathrm{d}} = 1\,\mathrm{nM}$ corresponds to $-20.7\,k_{\mathrm{B}}T$, Eq. (3.12). Away from equilibrium $\Delta G = \Delta G^\circ + k_{\mathrm{B}}T\ln Q$, Eq. (3.13); $K$ is a ratio of partition functions, Eq. (3.14). ATP hydrolysis releases about $-12\,k_{\mathrm{B}}T$ at standard state but about $-20\,k_{\mathrm{B}}T$ in cells because $[\mathrm{ATP}]/[\mathrm{ADP}]$ is held $10^8$–$10^9$ times above equilibrium (Example 3.2.1).
- Binding (3.3): a receptor in a lattice of ligands is occupied with probability $c/(c + K_{\mathrm{d}})$, $K_{\mathrm{d}} = c_0\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}$ (Theorem 3.3.1), the same result as from the chemical potential or from mass action; all-or-none binding of $n$ ligands gives the Hill function, Eq. (3.16), with a 10–90 % range of $81^{1/n}$. RNA polymerase partitioning between a promoter and millions of nonspecific sites follows the same law, with $P/N_{\mathrm{NS}}$ as the concentration (Example 3.3.1); binding is measured by fluorescence, calorimetry or surface methods, with care for ligand depletion (3.3.4).
- Proton-motive force (3.4): $\Delta p = \Delta\Psi - 61.5\,\mathrm{mV}\,\Delta\mathrm{pH}$ (Formula 3.4.1); about $-200\,\mathrm{mV}$ in mitochondria, 85 % electrical, $7.5\,k_{\mathrm{B}}T$ per proton (Example 3.4.1). At least 2.6 protons are needed per ATP; the c ring sets $c/3$: 2.7 (c₈), 3.3 (c₁₀), 4.7 (c₁₄).
- Rates (3.5): two-state relaxation has $\tau = 1/(k_+ + k_-)$ (Formula 3.5.1); detailed balance $k_+/k_- = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}$ is a property of equilibrium, not of a steady state (Theorem 3.5.1); Eyring rates fall tenfold per $2.3\,k_{\mathrm{B}}T$ of barrier, Eq. (3.20), enzymes lower barriers without moving equilibria, and $Q_{10} \approx 2$–$3$ for typical activation energies (Example 3.5.1). Out of equilibrium $J_+/J_- = \mathrm{e}^{\Delta\mu/k_{\mathrm{B}}T}$ and the dissipation $(J_+ - J_-)\Delta\mu \ge 0$, Eq. (3.21); ATP-driven cycles break detailed balance. Cells are chemical factories in steady flux: production and removal relax with time constant $1/\gamma$, and filaments grow above a critical concentration $c_{\mathrm{c}} = k_{\mathrm{off}}/k_{\mathrm{on}}$, Eq. (3.22).

## Questions

1. Two compartments contain a gas mixture with oxygen mole fractions $0.5436$ and $0.2000$ at the same total pressure and temperature ($37\,^\circ\mathrm{C}$). What is the difference in the chemical potential of oxygen, per molecule in units of $k_{\mathrm{B}}T$ and per mole? In which direction does oxygen move through a membrane permeable to it?

   **Answer** At equal total pressure, $\Delta\mu = k_{\mathrm{B}}T\ln(0.5436/0.2000) = k_{\mathrm{B}}T\ln 2.718 = 1.00\,k_{\mathrm{B}}T$ per molecule, $RT = 2.58\,\mathrm{kJ\,mol^{-1}}$ per mole. Oxygen moves from the compartment with the higher mole fraction (higher partial pressure, higher chemical potential) to the other until the partial pressures are equal.

2. A leaf cell has a solute potential of $-1.5\,\mathrm{MPa}$ and a turgor pressure of $0.6\,\mathrm{MPa}$. It is placed in (a) pure water, (b) a solution with $\Psi_{\mathrm{w}} = -0.9\,\mathrm{MPa}$, (c) a solution with $\Psi_{\mathrm{w}} = -2.0\,\mathrm{MPa}$. Does water enter or leave the cell in each case, and what is the final state?

   **Answer** The cell's water potential is $\Psi_{\mathrm{w}} = -1.5 + 0.6 = -0.9\,\mathrm{MPa}$. (a) Water enters (from $0$ to $-0.9$); the cell swells until its wall raises the turgor to about $1.5\,\mathrm{MPa}$, at which point $\Psi_{\mathrm{w}} = 0$ (the solute potential also rises slightly as the cell dilutes). (b) No net flow: the cell is already in equilibrium. (c) Water leaves; turgor falls to zero and, with $\Psi_{\mathrm{s}}$ still above $-2.0\,\mathrm{MPa}$, the protoplast shrinks away from the wall (plasmolysis) until its solute potential, concentrated by water loss, reaches $-2.0\,\mathrm{MPa}$.

3. The tallest trees are about $115\,\mathrm{m}$. What is the gravitational contribution to the water potential at the top? If the leaves at the top must keep $\Psi_{\mathrm{w}} \ge -2.0\,\mathrm{MPa}$ to grow, and friction in the xylem costs about as much as gravity, what limit does this suggest for tree height, given a soil at $-0.3\,\mathrm{MPa}$?

   **Answer** $\rho gh = 1000\times9.8\times115\,\mathrm{Pa} = 1.13\,\mathrm{MPa}$. With friction equal to gravity, the drop along the trunk is $2\rho gh$; requiring $-0.3 - 2\rho gh/10^6 \ge -2.0$ gives $h \le 1.7/(2\times0.0098) \approx 87\,\mathrm{m}$. The real trees are taller because friction is less than gravity in wide conduits; detailed analyses of redwoods put the limit at about $120$–$130\,\mathrm{m}$, where leaves at the top, at about $-2\,\mathrm{MPa}$, can barely expand.

4. A protein binds a ligand with $K_{\mathrm{d}} = 10\,\mu\mathrm{M}$ at $25\,^\circ\mathrm{C}$. What is the standard free energy of binding at $c^\circ = 1\,\mathrm{M}$? A mutation weakens binding by $1.4\,\mathrm{kcal\,mol^{-1}}$; what is the new $K_{\mathrm{d}}$, and how does the occupancy at $10\,\mu\mathrm{M}$ ligand change?

   **Answer** $\Delta G^\circ = RT\ln(K_{\mathrm{d}}/c^\circ) = 2.48\,\mathrm{kJ\,mol^{-1}}\times\ln10^{-5} = -28.5\,\mathrm{kJ\,mol^{-1}}$ ($-11.5\,k_{\mathrm{B}}T$, $-6.8\,\mathrm{kcal\,mol^{-1}}$). $1.4\,\mathrm{kcal\,mol^{-1}} = 5.86\,\mathrm{kJ\,mol^{-1}} = 2.36\,RT$, a factor $\mathrm{e}^{2.36} = 10.6$: $K_{\mathrm{d}} \approx 106\,\mu\mathrm{M}$. The occupancy at $10\,\mu\mathrm{M}$ falls from $0.50$ to $10/116 = 0.086$.

5. For a receptor with two sites that bind sequentially, $\mathrm{R} \rightleftharpoons \mathrm{RL} \rightleftharpoons \mathrm{RL}_2$ with dissociation constants $K_1$ and $K_2$, write the mean fraction of occupied sites $\bar\theta$ as a function of $c$. Show that it reduces to a simple binding curve when the two sites are independent and identical, with site dissociation constant $K$, and to a Hill function with $n = 2$ when $K_2 \ll K_1$ with $K_1K_2$ fixed.

   **Answer** The weights of R, RL and RL₂ are $1$, $c/K_1$ and $c^2/(K_1K_2)$, so $\bar\theta = \dfrac{c/K_1 + 2c^2/(K_1K_2)}{2\left[1 + c/K_1 + c^2/(K_1K_2)\right]}$. For two independent identical sites with site constant $K$, the macroscopic constants are $K_1 = K/2$ (two ways to bind the first ligand) and $K_2 = 2K$ (two ways to lose the second), and $\bar\theta$ simplifies to $c/(c + K)$. If $K_2 \to 0$ and $K_1 \to \infty$ with $K_1K_2 = K^2$ fixed, the middle state disappears and $\bar\theta \to c^2/(c^2 + K^2)$, the Hill function with $n = 2$: strong positive cooperativity means the second ligand binds much more tightly than the first.

6. Thylakoid lumen pH is 5.5 and stroma pH 8.0 in the light, with $\Delta\Psi \approx 0$ ($25\,^\circ\mathrm{C}$). Calculate the proton-motive force and the free energy per proton. With a c₁₄ ring, what is the largest phosphorylation potential that chloroplast ATP synthase can sustain?

   **Answer** With "in" the stroma, $\Delta\mathrm{pH} = 8.0 - 5.5 = 2.5$ and $\Delta p = -59.2\,\mathrm{mV}\times2.5 = -148\,\mathrm{mV}$; each proton flowing into the stroma releases $F\times0.148\,\mathrm{V} = 14.3\,\mathrm{kJ\,mol^{-1}}$. With $14/3 = 4.67$ protons per ATP, the maximum $\Delta G_{\mathrm{p}}$ is $4.67\times14.3 = 67\,\mathrm{kJ\,mol^{-1}}$, comfortably above the stromal phosphorylation potential of about $45$–$55\,\mathrm{kJ\,mol^{-1}}$: the larger ring compensates for a proton-motive force lower than in mitochondria.

7. A conformational change has rate constants $k_+ = 50\,\mathrm{s^{-1}}$ and $k_- = 5\,\mathrm{s^{-1}}$ at $25\,^\circ\mathrm{C}$. What are the free-energy difference between the states, the equilibrium fraction and the relaxation time after a perturbation? If a drug stabilizes the product state by $2\,k_{\mathrm{B}}T$ by slowing $k_-$ alone, how do the three quantities change?

   **Answer** $\Delta G = -k_{\mathrm{B}}T\ln(k_+/k_-) = -2.30\,k_{\mathrm{B}}T$ ($-5.7\,\mathrm{kJ\,mol^{-1}}$); $x_{\mathrm{eq}} = 50/55 = 0.909$; $\tau = 1/55\,\mathrm{s} = 18\,\mathrm{ms}$. With $k_-$ reduced by $\mathrm{e}^2 = 7.39$ to $0.68\,\mathrm{s^{-1}}$: $\Delta G = -4.30\,k_{\mathrm{B}}T$, $x_{\mathrm{eq}} = 50/50.68 = 0.987$, $\tau = 19.7\,\mathrm{ms}$. The equilibrium shifts strongly while the relaxation time hardly changes, because it is dominated by the faster rate constant.

8. Show that the dissipation rate $\dot W$ of Eq. (3.21) is non-negative, and that near equilibrium it is quadratic in the driving force: $\dot W \approx J_{\mathrm{eq}}\,\Delta\mu^2/k_{\mathrm{B}}T$, where $J_{\mathrm{eq}}$ is the one-way flux at equilibrium. What is the corresponding linear relation between net flux and force?

   **Answer** With $a = J_+$, $b = J_-$, $(a - b)\ln(a/b) \ge 0$ because $a - b$ and $\ln(a/b)$ have the same sign. Near equilibrium write $J_\pm = J_{\mathrm{eq}}(1 \pm \varepsilon/2)$ with small $\varepsilon$; then $J_+ - J_- = J_{\mathrm{eq}}\varepsilon$ and $\Delta\mu = k_{\mathrm{B}}T\ln(J_+/J_-) \approx k_{\mathrm{B}}T\varepsilon$, so $J_+ - J_- \approx (J_{\mathrm{eq}}/k_{\mathrm{B}}T)\Delta\mu$, a linear flux–force relation with coefficient $J_{\mathrm{eq}}/k_{\mathrm{B}}T$, and $\dot W \approx (J_{\mathrm{eq}}/k_{\mathrm{B}}T)\Delta\mu^2$. This is the linear regime of nonequilibrium thermodynamics ([6.3.18](/6.3.18#sec-18.2.1)); cells, with $\Delta\mu_{\mathrm{ATP}} \approx 20\,k_{\mathrm{B}}T$, operate far outside it.

9. (Design) You want to know whether a slow conformational change of a protein, observed by fluorescence, is limited by a single energy barrier. Propose measurements of rates as functions of temperature and of a stabilizing ligand, and state what results would support a single-barrier model.

   **Answer** Measure $k_+$ and $k_-$ separately (from the equilibrium fraction and the relaxation time after temperature or concentration jumps, Formula 3.5.1) at several temperatures. A single barrier predicts straight Arrhenius (or Eyring) plots for both, with activation enthalpies whose difference equals the van 't Hoff enthalpy of the equilibrium. Adding a ligand that binds one state should change $k_+/k_-$ according to the binding constants (detailed balance, Theorem 3.5.1), with a linear relation between $\ln k$ and $\ln K$ whose slope locates the transition state between the two end states. Curved Arrhenius plots, a relaxation that needs more than one exponential, or a lag phase indicate intermediates or several barriers.
