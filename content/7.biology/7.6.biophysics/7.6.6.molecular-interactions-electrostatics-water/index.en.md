---
title: Molecular Interactions and Electrostatics in Water
description: The noncovalent interactions that hold biological structures together, measured in kBT. The hierarchy of energies and its quantum origin; Coulomb's law in a dielectric, the Bjerrum length, Born solvation and the pKa shifts of buried groups; multipoles, orientation averaging, induction, London dispersion and the Lennard-Jones potential; hydrogen bonds and the hydrophobic effect; the Poisson–Boltzmann equation, the Debye length and screened interactions; charged membranes (Gouy–Chapman, Grahame equation, surface pH); counterion condensation on DNA (Manning) and the salt dependence of protein–DNA binding; protein charge and electrophoresis.
---

The structures of the previous chapters, folded proteins, double helices, bilayers and the complexes they form, are held together by interactions that are individually weak: most are worth between a tenth and a few $k_{\mathrm{B}}T$, and only by adding up many of them do molecules acquire stable shapes. Their weakness is not a defect. Interactions comparable to the thermal energy can be made and broken at physiological temperature, which allows proteins to change conformation, ligands to bind and dissociate, and assemblies to form and dissolve on demand. This chapter treats these interactions as physics, in the medium where they act: water, a solvent of exceptional polarity that weakens electrostatic forces eightyfold, and salt water, which screens them beyond a nanometer. It begins with the scale of molecular energies, their quantum-mechanical origin and the properties of water itself (6.1), develops electrostatics in a dielectric, the energetics of placing charges into proteins and membranes, and the shorter-range dipolar, induction, dispersion and steric interactions (6.2), treats hydrogen bonds and the hydrophobic effect (6.3), and ends with the mean-field electrostatics of salt solutions, which governs charged membranes, nucleic acids and the salt dependence of binding (6.4). The chemistry of intermolecular forces was introduced in [6.1.4](/6.1.4) and their role in biomolecular structure in [7.1.2](/7.1.2); the Debye–Hückel theory of electrolytes is derived in [6.3.12](/6.3.12) and the electric double layer of colloids in [6.3.21](/6.3.21). Here these are combined into quantitative estimates for biological systems. The results are used for the geometry of macromolecules ([7.6.7](/7.6.7)), force fields and simulation ([7.6.15](/7.6.15)), folding ([7.6.16](/7.6.16)), the polymer physics of DNA ([7.6.21](/7.6.21)), recognition ([7.6.17](/7.6.17)) and ion channels ([7.6.30](/7.6.30)).

## 6.1. Energy Scales

### 6.1.1. Interactions Measured in $k_{\mathrm{B}}T$

The natural unit for molecular energies in biology is the thermal energy, $k_{\mathrm{B}}T = 4.1\times10^{-21}\,\mathrm{J} = 4.1\,\mathrm{pN\,nm} = 25.7\,\mathrm{meV}$ at $25\,{}^\circ\mathrm{C}$, or $RT = 2.48\,\mathrm{kJ\,mol^{-1}}$ per mole. An interaction of energy $E$ is populated in proportion to its **Boltzmann factor** $\mathrm{e}^{-E/k_{\mathrm{B}}T}$ ([7.6.2](/7.6.2)), so an interaction of $1\,k_{\mathrm{B}}T$ is made and broken continuously, while one of $40\,k_{\mathrm{B}}T$ is permanent on any biological time scale.

| Interaction | Typical energy / ($\mathrm{kJ\,mol^{-1}}$) | In $k_{\mathrm{B}}T$ (at $25\,{}^\circ\mathrm{C}$) |
|---|---|---|
| Covalent bond (C–C, C–H, C=O) | $350$–$750$ | $140$–$300$ |
| Disulfide bond | $\approx 250$ | $\approx 100$ |
| Visible photon ($500\,\mathrm{nm}$) | $240$ | $96$ |
| ATP hydrolysis under cellular conditions ([7.6.3](/7.6.3)) | $\approx 50$ | $\approx 20$ |
| Hydrogen bond, isolated pair in vacuum (water dimer) | $\approx 21$ | $\approx 8$ |
| Hydrogen bond, net contribution in water | $2$–$6$ | $1$–$2$ |
| Salt bridge on a protein surface, net | $0$–$4$ | $0$–$1.5$ |
| Burial of a $\ce{CH2}$ group (hydrophobic effect) | $\approx 3.5$ | $\approx 1.4$ |
| Van der Waals contact between two atoms | $0.4$–$4$ | $0.15$–$1.5$ |
| Thermal energy $RT$ | $2.48$ | $1$ |

The table shows the central fact of biomolecular energetics. Covalent bonds are two orders of magnitude stronger than thermal energy and do not break spontaneously; the energy of ATP is an order of magnitude stronger and can drive one directed step; the noncovalent interactions that hold structures together are of the order of $k_{\mathrm{B}}T$ each, and their large numbers make a protein stable by only $20$–$60\,\mathrm{kJ\,mol^{-1}}$ in total ([7.1.6](/7.1.6)). The "net" values in water are much smaller than the gas-phase values because in water every group that forms an interaction first gives up its interactions with the solvent.

### 6.1.2. The Quantum Origin of Molecular Interactions

All the interactions in the table are consequences of the Schrödinger equation for electrons and nuclei interacting by Coulomb's law ([5.5](/5.5)). Because nuclei are thousands of times heavier than electrons, the electrons adjust almost instantaneously to the positions of the nuclei (the Born–Oppenheimer approximation), and the electronic energy as a function of nuclear positions is a **potential energy surface** ([6.3.16](/6.3.16)) on which the nuclei move. Force fields for molecular simulation are empirical approximations to this surface ([7.6.15](/7.6.15)).

Covalent bonds arise from the sharing of electrons in bonding orbitals and are directional because of the shapes of the **hybrid orbitals** ([6.1.3](/6.1.3)). The most important example for biology is the peptide bond: delocalization of the nitrogen lone pair into the carbonyl group gives the C–N bond about $40\,\%$ double-bond character, a length of $0.133\,\mathrm{nm}$ (between $0.147\,\mathrm{nm}$ for a single and $0.127\,\mathrm{nm}$ for a double C–N bond), a planar peptide group and a barrier of about $80\,\mathrm{kJ\,mol^{-1}}$ to rotation about it. The backbone of a protein can therefore rotate only about the bonds to the $\alpha$ carbon, the angles $\phi$ and $\psi$ of the **Ramachandran plot** ([7.6.7](/7.6.7)). Nonrelativistic quantum mechanics suffices for the light elements of biomolecules: the speed of an innermost electron is about $Z\alpha c$, where $\alpha \approx 1/137$ is the fine-structure constant, which is $4\,\%$ of the speed of light for carbon and $20\,\%$ for iron, so relativistic corrections matter only for heavy elements.

The noncovalent interactions between closed-shell molecules follow from perturbation theory in the intermolecular Coulomb energy. The four contributions behave very differently.

| Contribution | Origin | Distance dependence | Properties |
|---|---|---|---|
| Electrostatic | Coulomb energy of the unperturbed charge distributions (charges, dipoles, quadrupoles) | $r^{-(k + l + 1)}$ for multipoles of orders $k$ and $l$ | Long range, additive, strongly orientation dependent, either sign |
| Induction | Polarization of one molecule by the permanent multipoles of the other | Charge–induced dipole $r^{-4}$, dipole–induced dipole $r^{-6}$ | Always attractive, not pairwise additive |
| Dispersion | Correlated fluctuations of the electron clouds of both molecules | $r^{-6}$ | Always attractive, nearly orientation independent, approximately additive |
| Exchange (Pauli) repulsion | Antisymmetry of the electronic wave function when clouds overlap | Roughly exponential | Short range, a soft wall that defines molecular shape |

As a rule, the exchange repulsion and the electrostatics determine the geometry of a complex (which molecules fit together and in which orientation), while induction and dispersion add a roughly uniform stabilization to the structure so determined.

### 6.1.3. Quantized Energy Levels and Why Electrons Stay in Their Ground State

Quantum mechanics also explains why some molecular degrees of freedom take part in thermal motion and others do not. A particle confined to a region of size $L$ has a momentum uncertainty of at least $\hbar/L$ and therefore a minimum kinetic energy of order $\hbar^2/mL^2$; its energy levels are discrete. The simplest model, a particle of mass $m$ in a one-dimensional box of length $L$ with impenetrable walls, has the standing-wave solutions $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$ of the Schrödinger equation ([5.5](/5.5)) and the levels

$$
E_n = \frac{n^2h^2}{8mL^2}, \qquad n = 1, 2, \dots \tag{6.1}
$$
The spacing grows as $1/mL^2$: light particles in small boxes have widely spaced levels. For an electron in a box of $1\,\mathrm{nm}$, $h^2/8m_{\mathrm{e}}L^2 = 0.38\,\mathrm{eV} = 15\,k_{\mathrm{B}}T$; for the $\pi$ electrons of a conjugated chain, which move along the whole chain, the model predicts the absorption of light. In hexatriene, with six $\pi$ electrons filling the levels $n = 1$–$3$ over a length $L \approx 0.84\,\mathrm{nm}$, the lowest transition $n = 3 \to 4$ has $\Delta E = 7h^2/8m_{\mathrm{e}}L^2 \approx 3.7\,\mathrm{eV}$, an ultraviolet wavelength of about $330\,\mathrm{nm}$ (measured: $258\,\mathrm{nm}$); longer conjugated chains absorb at longer wavelengths, which is why retinal, carotenoids and chlorophyll, with ten or more conjugated double bonds, absorb visible light ([7.6.18](/7.6.18)).

The same reasoning orders all the degrees of freedom of a molecule by their level spacing, and compares the spacing with $k_{\mathrm{B}}T$:

| Degree of freedom | Typical spacing | In $k_{\mathrm{B}}T$ at $25\,{}^\circ\mathrm{C}$ | Probed by |
|---|---|---|---|
| Electronic (valence) | $2$–$6\,\mathrm{eV}$ | $80$–$250$ | UV–visible absorption, fluorescence ([7.6.11](/7.6.11)) |
| Bond vibration | $0.1$–$0.4\,\mathrm{eV}$ ($1000$–$3000\,\mathrm{cm^{-1}}$) | $4$–$15$ | Infrared and Raman spectroscopy |
| Torsion, low-frequency modes of a protein | $1$–$10\,\mathrm{meV}$ | $0.04$–$0.4$ | Terahertz, neutron scattering |
| Electron spin in a magnetic field of $0.35\,\mathrm{T}$ | $4\times10^{-5}\,\mathrm{eV}$ | $1.6\times10^{-3}$ | EPR ([7.6.13](/7.6.13)) |
| Proton spin in $14\,\mathrm{T}$ | $2.5\times10^{-6}\,\mathrm{eV}$ | $10^{-4}$ | NMR ([7.6.13](/7.6.13)) |

Degrees of freedom whose spacing is much larger than $k_{\mathrm{B}}T$ are frozen in their ground state, by the Boltzmann factor $\mathrm{e}^{-\Delta E/k_{\mathrm{B}}T} \approx \mathrm{e}^{-100}$ for an electronic excitation: at physiological temperature molecules are electronically in their ground state, their chemistry is that of the ground-state potential surface, and electronic excitation requires a photon or a chemical reaction. Bond vibrations are mostly in their ground state too, which is why covalent geometry is rigid and why force fields can treat bond lengths as nearly fixed; the soft torsional and collective modes are classical and carry the thermal motion that the rest of this course describes. Spin levels are populated almost equally, which makes magnetic resonance insensitive but possible at all. Effects that require a genuinely quantum description in biology, beyond these level structures, are electron and proton tunneling in enzymes and electron-transfer chains, coherent energy transfer among pigments and spin dynamics of radical pairs; they are discussed in [7.6.18](/7.6.18) and [7.6.19](/7.6.19).

### 6.1.4. Water

Water is the medium of all these interactions, and its own properties set most of the numbers in this chapter. Pure water is $55.5\,\mathrm{M}$; each molecule carries a dipole of $1.85\,\mathrm{D}$ and can donate two and accept two hydrogen bonds, and in the liquid at room temperature it forms on average about $3.5$ of them in a fluctuating tetrahedral network whose individual hydrogen bonds last about a picosecond. This network gives water its high relative permittivity ($78$), high heat capacity ($75\,\mathrm{J\,mol^{-1}\,K^{-1}}$), high surface tension ($72\,\mathrm{mN\,m^{-1}}$) and the hydrophobic effect (6.3.2).

Water also dissociates, $\ce{2H2O <=> H3O+ + OH-}$, with ionic product $K_{\mathrm{w}} = [\ce{H+}][\ce{OH-}]/(c^\circ)^2 = 1.0\times10^{-14}$ at $25\,{}^\circ\mathrm{C}$ (about $2.4\times10^{-14}$ at $37\,{}^\circ\mathrm{C}$). At the cytoplasmic pH of about $7.4$ of *E. coli*, the free proton concentration is $10^{-7.4}\,\mathrm{M} = 40\,\mathrm{nM}$, about $24$ free protons in a cell volume of $1\,\mu\mathrm{m^3}$; the protons that matter are those bound to and released from the buffering groups of metabolites and proteins, which number in the millions. The ionization of acidic and basic groups, set by their $\mathrm{p}K_{\mathrm{a}}$ values relative to the pH, gives biomolecules their charges. The phosphodiester of every nucleotide ($\mathrm{p}K_{\mathrm{a}} \approx 1$) is fully ionized, so the $4.6\,\mathrm{Mbp}$ genome of *E. coli* carries about $9\times10^{6}$ negative charges, neutralized by small cations, polyamines and basic proteins; carboxylates ($\mathrm{p}K_{\mathrm{a}} \approx 4$) are negative and the amino groups of lysine ($\mathrm{p}K_{\mathrm{a}} \approx 10.5$) and the guanidinium of arginine ($\mathrm{p}K_{\mathrm{a}} \approx 12.5$) positive, while histidine ($\mathrm{p}K_{\mathrm{a}} \approx 6$) is partly charged and responds to small changes of pH. A typical protein thus carries tens of charges of both signs and a net charge of a few, and how these charges interact, with each other and with the ions of the solution, is the subject of 6.2 and 6.4.

## 6.2. Electrostatics in a Dielectric

### 6.2.1. Coulomb's Law in Water and the Bjerrum Length

Two charges $q_1$ and $q_2$ at distance $r$ in a uniform medium of relative permittivity $\varepsilon_{\mathrm{r}}$ interact with energy

$$
U(r) = \frac{q_1q_2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r}, \tag{6.2}
$$
**Coulomb's law** ([5.3.1](/5.3.1)) reduced by the polarization of the medium ([5.3.4](/5.3.4)). Water has $\varepsilon_{\mathrm{r}} = 78.4$ at $25\,{}^\circ\mathrm{C}$ ($74.2$ at $37\,{}^\circ\mathrm{C}$), mostly from **orientation polarization**: its molecules carry large dipoles and turn them towards a charge. Hydrocarbon and the core of a lipid bilayer have $\varepsilon_{\mathrm{r}} \approx 2$, from electronic polarization only, and the interior of a protein an effective value between about $2$ and $20$ depending on what is measured. A single length characterizes the strength of electrostatics in a medium.

**Definition 6.2.1 (Bjerrum Length)** The **Bjerrum length** of a medium is the distance at which the electrostatic energy of two elementary charges equals the thermal energy:

$$
\ell_{\mathrm{B}} = \frac{\mathrm{e}^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}k_{\mathrm{B}}T},
$$
so that $U(r) = z_1z_2k_{\mathrm{B}}T\,\ell_{\mathrm{B}}/r$ for ions of valences $z_1$ and $z_2$.

In vacuum at $25\,{}^\circ\mathrm{C}$, $\ell_{\mathrm{B}} = 56\,\mathrm{nm}$; in water it is $0.71\,\mathrm{nm}$ ($0.73\,\mathrm{nm}$ at $37\,{}^\circ\mathrm{C}$), about twice the diameter of a water molecule; in a medium with $\varepsilon_{\mathrm{r}} = 4$ it is $14\,\mathrm{nm}$. Two opposite monovalent ions in contact in water ($r \approx 0.28\,\mathrm{nm}$ for $\ce{Na+}$ and $\ce{Cl-}$) attract with only $0.71/0.28 = 2.5\,k_{\mathrm{B}}T$, so salts dissolve; the same pair inside a membrane would be bound by $100\,k_{\mathrm{B}}T$. Water is what makes electrostatics in biology weak enough to be reversible.

### 6.2.2. Born Solvation and the Cost of Burying a Charge

Much of the free energy of an ion is the energy of its own field, and that energy depends on the medium. Charging a sphere of radius $a$ to charge $ze$ in a medium of permittivity $\varepsilon_{\mathrm{r}}$ costs $(ze)^2/(8\pi\varepsilon_0\varepsilon_{\mathrm{r}}a)$, so moving it from vacuum into the medium changes its free energy as follows.

**Formula 6.2.1 (Born Energy)** The free energy of transferring an ion of charge $ze$ and radius $a$ from a medium of permittivity $\varepsilon_1$ to one of permittivity $\varepsilon_2$ is

$$
\Delta G_{\mathrm{Born}} = \frac{z^2\mathrm{e}^2}{8\pi\varepsilon_0a}\left(\frac{1}{\varepsilon_2} - \frac{1}{\varepsilon_1}\right) = \frac{z^2\ell_{\mathrm{B}}^{\mathrm{vac}}}{2a}\left(\frac{1}{\varepsilon_2} - \frac{1}{\varepsilon_1}\right)k_{\mathrm{B}}T,
$$
where $\ell_{\mathrm{B}}^{\mathrm{vac}} = 56\,\mathrm{nm}$ is the Bjerrum length in vacuum at $25\,{}^\circ\mathrm{C}$.

**Example 6.2.1 (Why membranes are impermeable to ions)** For $\ce{Na+}$ with an effective Born radius of $0.187\,\mathrm{nm}$, hydration from vacuum ($\varepsilon_1 = 1$, $\varepsilon_2 = 78.4$) gives $-(56/0.374)(1 - 1/78.4) = -148\,k_{\mathrm{B}}T = -367\,\mathrm{kJ\,mol^{-1}}$, close to the experimental hydration free energy of $-365\,\mathrm{kJ\,mol^{-1}}$. Moving the ion from water into the hydrocarbon core of a bilayer ($\varepsilon_2 = 2$) costs $(56/0.374)(1/2 - 1/78.4) = 73\,k_{\mathrm{B}}T$, so the equilibrium concentration of $\ce{Na+}$ inside the membrane is a fraction $\mathrm{e}^{-73} \approx 10^{-32}$ of that in water. Ions cross membranes only through proteins that provide a polar path: channels whose pores are lined with carbonyl oxygens or water ([7.6.30](/7.6.30)), carriers, and ionophores such as valinomycin, which wraps $\ce{K+}$ in a shell of oxygens with a hydrophobic exterior about $0.6\,\mathrm{nm}$ in radius and reduces the Born penalty to about $23\,k_{\mathrm{B}}T$, which the hydrophobic contacts of its surface partly compensate.

The same physics shifts the ionization constants of groups that are buried in proteins. A carboxylate or ammonium group moved from water into a region of low permittivity pays a Born penalty in its charged form only, so the equilibrium shifts towards the neutral form: acids become weaker and bases weaker as well, the **acid dissociation constant** of an Asp or Glu falling and that of a Lys or Arg rising (in the sense that the protonated, neutral acid and the deprotonated, neutral base are favoured). With the **Henderson–Hasselbalch equation** ([6.1.9](/6.1.9)) the shift is $\Delta\mathrm{p}K_{\mathrm{a}} = \pm\Delta G_{\mathrm{Born}}/(k_{\mathrm{B}}T\ln 10)$, positive for acids and negative for bases. For a charge of radius $0.25\,\mathrm{nm}$ moved into a site of effective permittivity $10$, the Born estimate is $9.8\,k_{\mathrm{B}}T$, a shift of $4.2$ units. Lysines, glutamates and aspartates engineered into the hydrophobic core of staphylococcal nuclease show shifts of this order, up to about five units, often accompanied by local unfolding or water penetration that limit the shift (García-Moreno and colleagues). Ionizable groups are therefore found almost exclusively at protein surfaces, and the few that are buried are usually functional: they pair with an opposite charge, are stabilized by hydrogen bonds and dipoles, or are needed for catalysis or proton transport precisely because their $\mathrm{p}K_{\mathrm{a}}$ is unusual.

A buried salt bridge is not automatically stabilizing. Two monovalent ions of radius $0.25\,\mathrm{nm}$ in contact at $0.4\,\mathrm{nm}$ in a medium of permittivity $4$ attract with $14/0.4 = 35\,k_{\mathrm{B}}T$, but bringing both from water costs $2 \times 27 = 53\,k_{\mathrm{B}}T$ of Born energy, and the net balance is unfavourable unless the protein supplies further polar interactions. This desolvation penalty explains why measured contributions of salt bridges to stability are small and sometimes negative (Honig and Hubbell, 1984), and why electrostatic calculations for proteins must treat the solvent and the protein as media of different permittivity, solving the Poisson or Poisson–Boltzmann equation numerically for the real molecular shape.

![Why charges stay in water. A: Born free energy of transferring a monovalent ion of radius a from water into a medium of relative permittivity 2 (the hydrocarbon core of a lipid bilayer), 4 or 10 (effective values for the interior of a protein), in units of kBT at 25 °C; the dotted lines mark the radii of Na⁺ and Cl⁻. For divalent ions the energy is four times larger. B: the shift of the pKa of an ionizable group (charge radius 0.25 nm) moved from water into a site of permittivity εr, from the Born energy alone: the pKa of an acid rises and that of a base falls, because burial favours the uncharged form. Hydrogen bonds, nearby charges and penetrating water compensate part of the cost, so measured shifts are smaller than these estimates](./plots/born.py)

### 6.2.3. Dipoles and Orientation

Most chemical groups are neutral but have an uneven distribution of charge. Far from a neutral group, its potential is dominated by the **electric dipole moment** $\boldsymbol{p} = \sum_iq_i\boldsymbol{r}_i$ ([5.3.1](/5.3.1)): the first nonvanishing term of the expansion of the potential in powers of $1/r$, which for a charge distribution of net charge $Q$, dipole $\boldsymbol{p}$ and higher moments decays as $Q/r$, $p/r^2$, and so on. The energy of two distributions with lowest nonvanishing multipoles of orders $k$ and $l$ (charge $0$, dipole $1$, quadrupole $2$) decays as $r^{-(k + l + 1)}$.

**Formula 6.2.2 (Electrostatic Interactions of Dipoles)** In a medium of permittivity $\varepsilon_{\mathrm{r}}$, with $\hat{\boldsymbol{r}}$ the unit vector between the groups and $\theta$ the angle between $\boldsymbol{p}$ and $\hat{\boldsymbol{r}}$,

$$
U_{q\text{–}p} = -\frac{qp\cos\theta}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}, \qquad
U_{p\text{–}p} = \frac{\boldsymbol{p}_1\cdot\boldsymbol{p}_2 - 3(\boldsymbol{p}_1\cdot\hat{\boldsymbol{r}})(\boldsymbol{p}_2\cdot\hat{\boldsymbol{r}})}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^3}.
$$
If the dipoles rotate freely and the interaction is weak compared with $k_{\mathrm{B}}T$, Boltzmann averaging over orientations gives the attractions

$$
\langle U_{q\text{–}p}\rangle = -\frac{q^2p^2}{6(4\pi\varepsilon_0\varepsilon_{\mathrm{r}})^2k_{\mathrm{B}}Tr^4}, \qquad
\langle U_{p\text{–}p}\rangle = -\frac{2p_1^2p_2^2}{3(4\pi\varepsilon_0\varepsilon_{\mathrm{r}})^2k_{\mathrm{B}}Tr^6},
$$
the second being the **Keesom force** ([6.1.4](/6.1.4)).

The orientation average is not zero because favourable orientations are more populated than unfavourable ones; to first order the bias is $U/k_{\mathrm{B}}T$, which is why the averaged energy is quadratic in the field and inversely proportional to temperature. Dipole moments are quoted in debye ($1\,\mathrm{D} = 3.336\times10^{-30}\,\mathrm{C\,m}$): $1.85\,\mathrm{D}$ for water and about $3.6\,\mathrm{D}$ for the peptide group. In an $\alpha$ helix all peptide dipoles point along the axis, and their sum acts approximately like half an elementary charge at each end, positive at the N terminus and negative at the C terminus (Hol, 1978); anion- and phosphate-binding sites are often located at helix N termini, as in the P-loop of nucleotide-binding proteins. In a protein the dipoles do not rotate freely, and the full orientation-dependent energies of Formula 6.2.2 apply.

### 6.2.4. Induction and Dispersion

A field $\boldsymbol{E}$ also induces a dipole $\boldsymbol{p}_{\mathrm{ind}} = \alpha\boldsymbol{E}$ in any molecule, where $\alpha$ is the **polarizability** ([6.1.4](/6.1.4)), usually quoted as a polarizability volume $\alpha' = \alpha/4\pi\varepsilon_0$ (about $1.5\times10^{-3}\,\mathrm{nm^3}$ for water and $2.6\times10^{-3}\,\mathrm{nm^3}$ for methane). The energy of an **induced dipole** in the field of a charge is $-\frac12\alpha E^2$, an attraction $-\alpha'q^2/(2\cdot4\pi\varepsilon_0r^4)$; with a permanent dipole as the source it is the **Debye force**.

Even two nonpolar molecules attract. The electron cloud of each fluctuates, the instantaneous dipole of one polarizes the other, and the correlated fluctuations lower the energy: this is the **London dispersion force** ([6.1.4](/6.1.4)), a quantum-mechanical effect of the zero-point motion of the electrons.

**Formula 6.2.3 (London Formula)** Two atoms or molecules with polarizability volumes $\alpha_1'$, $\alpha_2'$ and ionization energies $I_1$, $I_2$ attract by the dispersion energy

$$
U_{\mathrm{disp}} = -\frac{3}{2}\frac{I_1I_2}{I_1 + I_2}\frac{\alpha_1'\alpha_2'}{r^6},
$$
which for identical molecules reduces to $-\frac34I\alpha'^2/r^6$.

The formula is approximate (it replaces the spectrum of excitations by a single energy close to $I$), but it gives the right magnitudes. The simpler expression $-3I\alpha_1'\alpha_2'/4r^6$ often quoted holds only for identical molecules. For two methane molecules ($I = 12.6\,\mathrm{eV}$) at $0.4\,\mathrm{nm}$, $U = -\frac34 \times 12.6 \times (2.6\times10^{-3})^2/(0.4)^6\,\mathrm{eV} = -0.016\,\mathrm{eV} = -0.6\,k_{\mathrm{B}}T$. Dispersion is small per pair but present between every pair of atoms in contact and approximately additive, and a protein interface of $1000\,\mathrm{\AA^2}$ contains about a hundred atom–atom contacts; summed over macroscopic bodies, the $r^{-6}$ attraction becomes the Hamaker interaction of colloid science ([6.3.21](/6.3.21)).

### 6.2.5. Steric Repulsion and the Lennard-Jones Potential

When the electron clouds of two closed-shell atoms overlap, the Pauli principle forces electrons into higher orbitals and the energy rises steeply, roughly exponentially with decreasing distance. The combination of this repulsion with the dispersion attraction is usually represented by one function.

**Definition 6.2.2 (Lennard-Jones Potential)** The **Lennard-Jones potential** between two atoms is

$$
U_{\mathrm{LJ}}(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right] = \varepsilon\left[\left(\frac{r_{\mathrm{m}}}{r}\right)^{12} - 2\left(\frac{r_{\mathrm{m}}}{r}\right)^6\right],
$$
where $\varepsilon$ is the depth of the minimum, $\sigma$ the distance at which $U = 0$ and $r_{\mathrm{m}} = 2^{1/6}\sigma$ the position of the minimum.

The attractive term has the $r^{-6}$ form of dispersion; the exponent $12$ of the repulsion has no physical basis beyond being steep and computationally convenient (the square of $r^{-6}$), and an exponential form is more accurate. The minimum $r_{\mathrm{m}}$ is close to the sum of the van der Waals radii of the atoms (Bondi's values: H $0.12$, C $0.17$, N $0.155$, O $0.152$, S $0.18\,\mathrm{nm}$): two aliphatic carbons touch at about $0.34$–$0.40\,\mathrm{nm}$, which is also the spacing of graphite sheets and of the base pairs in a DNA helix. In biomolecular force fields $\varepsilon$ for carbon is about $0.3$–$0.4\,\mathrm{kJ\,mol^{-1}}$ ($0.15\,k_{\mathrm{B}}T$), so the attraction per contact is small while the repulsion is a hard wall: closer than about $0.9\,r_{\mathrm{m}}$ the energy rises by several $k_{\mathrm{B}}T$. This hard core is what forbids most combinations of backbone angles ([7.6.7](/7.6.7)) and makes the packing of protein interiors, as dense as that of organic crystals, a major determinant of structure.

![Interaction energies of molecular groups against distance, in units of kBT at 25 °C. A: magnitudes on logarithmic axes: two unit charges in vacuum and in water (∝ 1/r), a unit charge and a water dipole aligned in vacuum (∝ 1/r²), two aligned water dipoles in vacuum (∝ 1/r³), the orientation-averaged Keesom attraction of two water dipoles and the London dispersion attraction of two methane molecules (both ∝ 1/r⁶); the dotted line marks kBT. Interactions between charges in water remain above kBT only within the Bjerrum length, 0.7 nm, and the r⁻⁶ interactions only at contact. B: the Lennard-Jones potential of two aliphatic carbons (ε = 0.16 kBT at r_m = 0.40 nm, magnified tenfold) compared with the attraction of two opposite unit charges in water, bare and screened by 150 mM salt](./plots/interaction-curves.py)

## 6.3. Hydrogen Bonds and the Hydrophobic Effect

### 6.3.1. Hydrogen Bonds

A **hydrogen bond** ([6.1.4](/6.1.4)) D–H⋯A forms between a hydrogen covalently bound to an electronegative donor D (O, N) and an acceptor A with a lone pair (O, N, less often S). Its energy is mostly electrostatic: the hydrogen carries a partial charge of about $+0.4\,e$ and, being small and nearly stripped of electron density, allows the donor's dipole to approach the acceptor closely; induction and a small charge transfer add to it. Three properties follow and matter for structure. Hydrogen bonds are short, with D⋯A distances of $0.27$–$0.31\,\mathrm{nm}$ (inside the sum of van der Waals radii, which is $0.30\,\mathrm{nm}$ for two oxygens); they are directional, strongest for a nearly linear D–H⋯A arrangement (backbone hydrogen bonds in antiparallel $\beta$ sheets are close to linear); and they saturate, each hydrogen forming essentially one bond.

In vacuum a hydrogen bond between two water molecules is worth about $21\,\mathrm{kJ\,mol^{-1}}$ ($8\,k_{\mathrm{B}}T$), and an amide–carbonyl bond somewhat more. In water the relevant quantity is the exchange $\mathrm{D{-}H}\cdots\mathrm{OH_2} + \mathrm{H_2O}\cdots\mathrm{A} \to \mathrm{D{-}H}\cdots\mathrm{A} + \mathrm{H_2O}\cdots\mathrm{H_2O}$, whose free energy is small: mutation studies give a net contribution of a few $\mathrm{kJ\,mol^{-1}}$ per hydrogen bond to protein stability, about $1$–$2\,k_{\mathrm{B}}T$. The asymmetry matters more than the average: a donor or acceptor buried without a partner loses its hydrogen bonds to water and gains nothing, a penalty of several $k_{\mathrm{B}}T$. This is why the backbone NH and CO groups in a protein interior are almost always paired in helices and sheets ([7.6.7](/7.6.7)), and why hydrogen bonds contribute more to specificity, the discrimination between partners that fit and those that do not (base pairing, [7.1.11](/7.1.11); protein–DNA recognition, [7.6.17](/7.6.17)), than to affinity.

### 6.3.2. The Hydrophobic Effect

Nonpolar molecules are poorly soluble in water, and nonpolar surfaces in water associate. This **hydrophobic effect** ([7.1.2](/7.1.2)) is the main driving force of protein folding, membrane formation and many binding events, but it is not an attraction between the nonpolar molecules: their dispersion attraction to each other is about the same as to water. It is a property of water, a free energy of the solvent that depends on how much nonpolar surface it must accommodate, and thus a potential of mean force between solutes.

The thermodynamics of transferring a small hydrocarbon from a nonpolar liquid into water at $25\,{}^\circ\mathrm{C}$ has a characteristic signature: a positive free energy (about $3.5\,\mathrm{kJ\,mol^{-1}}$ per $\ce{CH2}$ group), an enthalpy close to zero, a large negative entropy, and a large positive change of **heat capacity**. Water molecules next to a small nonpolar solute cannot point hydrogen bonds towards it and keep their hydrogen-bond network intact by restricting their orientations, which costs entropy. Because the heat capacity change is large, the enthalpy and entropy both increase with temperature, so that the effect becomes enthalpic at high temperature and weakens at low temperature, the origin of the cold denaturation of proteins ([7.6.8](/7.6.8)). The free energy scales with the nonpolar surface area buried, about $0.1\,\mathrm{kJ\,mol^{-1}}$ per $\mathrm{\AA^2}$ (roughly $25\,\mathrm{cal\,mol^{-1}\,\AA^{-2}}$ in the older literature), so burying $1000\,\mathrm{\AA^2}$ of nonpolar surface on binding or folding gains about $100\,\mathrm{kJ\,mol^{-1}}$.

The molecular picture depends on size (Lum, Chandler and Weeks, 1999). Around solutes smaller than about $1\,\mathrm{nm}$ water rearranges without breaking hydrogen bonds, and the cost grows with the solute's volume and is mainly entropic, as described above. Around larger nonpolar surfaces water cannot maintain its network and forms an interface like that between water and oil or vapour; the cost then grows with area and is mainly enthalpic, approaching the macroscopic interfacial tension (about $50\,\mathrm{mN\,m^{-1}}$ for an oil–water interface, $0.3\,\mathrm{kJ\,mol^{-1}\,\AA^{-2}}$). The crossover lies at the scale of protein side chains and interfaces, which is why simple additive estimates work only roughly, and why the estimate of [7.6.2](/7.6.2) in terms of the entropy of blocked hydrogen-bond configurations explains the order of magnitude but not the temperature and size dependence.

## 6.4. Electrostatics in Salt Solutions

### 6.4.1. The Poisson–Boltzmann Equation and the Debye Length

Cells and their surroundings contain about $150\,\mathrm{mM}$ of small ions. Around a charged molecule these ions are not uniformly distributed: counterions accumulate and coions are depleted, and the resulting ionic atmosphere screens the charge. In the mean-field approximation each ion species is distributed according to its Boltzmann factor in the average potential $\varphi$, and the potential is produced, through Poisson's equation, by the fixed charges and the ions together.

**Formula 6.4.1 (Poisson–Boltzmann Equation)** For ions of valences $z_i$ and bulk concentrations $c_i^\infty$ (number densities) in a medium of permittivity $\varepsilon_{\mathrm{r}}$,

$$
\nabla^2\varphi = -\frac{1}{\varepsilon_0\varepsilon_{\mathrm{r}}}\left[\rho_{\mathrm{fixed}} + \sum_iz_iec_i^\infty\mathrm{e}^{-z_ie\varphi/k_{\mathrm{B}}T}\right].
$$
For a $1{:}1$ salt of concentration $c_{\mathrm{s}}$ and the dimensionless potential $y = e\varphi/k_{\mathrm{B}}T$, outside the fixed charges $\nabla^2y = \kappa^2\sinh y$, with

$$
\kappa^2 = \frac{1}{\lambda_{\mathrm{D}}^2} = 8\pi\ell_{\mathrm{B}}N_{\mathrm{A}}I, \qquad \lambda_{\mathrm{D}} = \frac{0.304\,\mathrm{nm}}{\sqrt{I/\mathrm{M}}}\ \text{(water, } 25\,{}^\circ\mathrm{C)},
$$
where $I = \frac12\sum_iz_i^2c_i$ is the **ionic strength** in molar units.

This is the **Poisson–Boltzmann equation** of [6.3.12](/6.3.12), whose linearization for $\lvert y\rvert \ll 1$, $\nabla^2y = \kappa^2y$, is the **Debye–Hückel theory**. The **Debye length** $\lambda_{\mathrm{D}}$ is $0.78\,\mathrm{nm}$ at $150\,\mathrm{mM}$, about the size of a small protein's charged groups' separation, $3\,\mathrm{nm}$ in a $10\,\mathrm{mM}$ buffer and almost $1\,\mu\mathrm{m}$ in pure water. In the linearized theory two point charges interact with the screened Coulomb (Yukawa) energy

$$
U(r) = z_1z_2k_{\mathrm{B}}T\,\frac{\ell_{\mathrm{B}}\,\mathrm{e}^{-r/\lambda_{\mathrm{D}}}}{r}, \tag{6.3}
$$
and a sphere of radius $a$ carrying charge $Ze$ has the potential $\varphi(r) = \frac{Ze}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}}\frac{\mathrm{e}^{-\kappa(r - a)}}{(1 + \kappa a)r}$ outside it.

At physiological ionic strength, therefore, electrostatic interactions between charged groups are cut off beyond about a nanometer: at $2\,\mathrm{nm}$ only $\mathrm{e}^{-2/0.78} = 8\,\%$ of the unscreened energy remains. Electrostatics in cells is a short-range interaction between charges, a long-range one only for highly charged objects and for the collective field of many charges (membranes, nucleic acids, the surfaces of viruses), and it can be tuned in experiments by salt: a binding constant or a rate that depends strongly on ionic strength reveals an electrostatic contribution.

The mean-field theory neglects the correlations between ions, their finite size and the discreteness of fixed charges. It is accurate for monovalent salts at moderate surface charge, and it fails when the electrostatic coupling between ions is strong: near highly charged surfaces with multivalent counterions, such as DNA in the presence of $\ce{Mg^2+}$, spermidine$^{3+}$ or cobalt hexammine$^{3+}$, ion correlations produce an attraction between like-charged surfaces that the Poisson–Boltzmann equation cannot give, and that condenses DNA into compact toroids ([7.6.21](/7.6.21)). For proteins the Poisson–Boltzmann equation is solved numerically with the molecular shape, a low permittivity inside and $78$ outside, to compute electrostatic potentials, $\mathrm{p}K_{\mathrm{a}}$ shifts and binding energies.

![Electrostatic screening by salt. A: Debye length of a 1:1 electrolyte in water at 25 °C against ionic strength, λ_D = 0.304 nm/√(I/M), with typical media marked: fresh water (about 1 mM), a 10 mM buffer, cytoplasm and blood plasma (about 150 mM) and seawater (about 0.7 M). B: interaction energy of two opposite unit charges in water without salt, at 10 mM and at 150 mM (Eq. (6.3)); without salt the energy equals kBT at the Bjerrum length ℓB = 0.71 nm. C: the screening factor e^−r/λ_D, the fraction of the unscreened interaction that survives: at 150 mM salt removes more than 90 % of the interaction beyond 2 nm](./plots/debye.py)

### 6.4.2. Charged Membranes

The inner leaflet of the plasma membrane contains $20$–$30\,\%$ anionic lipids (phosphatidylserine, phosphatidylinositol and its phosphates), and with an area of $0.65\,\mathrm{nm^2}$ per lipid this is a surface charge density of about $\sigma = -0.3\,e\,\mathrm{nm^{-2}}$. For a uniformly charged plane the Poisson–Boltzmann equation is one-dimensional and can be solved exactly; this is the **Gouy–Chapman model** of the diffuse double layer ([6.3.21](/6.3.21)), written here in terms of the surface charge, which is what biology fixes.

**Formula 6.4.2 (Gouy–Chapman Solution and Grahame Equation)** For a plane of charge density $\sigma$ in a $1{:}1$ salt, the dimensionless potential at distance $x$ is

$$
y(x) = 4\operatorname{artanh}\left[\tanh\frac{y_0}{4}\,\mathrm{e}^{-x/\lambda_{\mathrm{D}}}\right],
$$
and the surface potential $y_0$ is fixed by the surface charge through the Grahame equation

$$
\sinh\frac{y_0}{2} = 2\pi\ell_{\mathrm{B}}\frac{\sigma}{e}\lambda_{\mathrm{D}} = \frac{\lambda_{\mathrm{D}}}{\ell_{\mathrm{GC}}}\,\operatorname{sgn}\sigma, \qquad \ell_{\mathrm{GC}} = \frac{e}{2\pi\ell_{\mathrm{B}}\lvert\sigma\rvert},
$$
where $\ell_{\mathrm{GC}}$ (the Gouy–Chapman length) is the distance at which the energy of a counterion in the field of the bare surface equals $k_{\mathrm{B}}T$.

For $\lambda_{\mathrm{D}} \ll \ell_{\mathrm{GC}}$ (weakly charged surface or high salt) the surface potential is small and the linearized solution $y = (2\lambda_{\mathrm{D}}/\ell_{\mathrm{GC}})\mathrm{e}^{-x/\lambda_{\mathrm{D}}}$ applies; for $\lambda_{\mathrm{D}} \gg \ell_{\mathrm{GC}}$ the potential grows only logarithmically with the charge, because the accumulated counterions neutralize most of it within $\ell_{\mathrm{GC}}$ of the surface.

**Example 6.4.1 (The inner leaflet of the plasma membrane)** With $20\,\%$ anionic lipids, $\sigma = -0.31\,e\,\mathrm{nm^{-2}}$ and $\ell_{\mathrm{GC}} = 1/(2\pi \times 0.715 \times 0.31)\,\mathrm{nm} = 0.72\,\mathrm{nm}$. At $150\,\mathrm{mM}$, $\lambda_{\mathrm{D}} = 0.78\,\mathrm{nm}$, so $\sinh(y_0/2) = -1.09$, $y_0 = -1.89$ and $\varphi_0 = -1.89 \times 25.7\,\mathrm{mV} = -49\,\mathrm{mV}$ (the linearized theory gives $-56\,\mathrm{mV}$). Cations are enriched at the surface by $\mathrm{e}^{1.89} = 6.6$-fold, to about $1\,\mathrm{M}$, and anions depleted by the same factor. Protons are enriched as well, so the pH at the surface is lower than in the bulk by $1.89/\ln 10 = 0.82$ units, enough to shift the protonation of surface histidines and the activity of membrane enzymes. A cluster of $Z$ basic residues near the membrane gains roughly $Z \times 1.89\,k_{\mathrm{B}}T$; for the polybasic tails of K-Ras4B or MARCKS, with several lysines, this is enough to recruit the protein to the inner leaflet in combination with a lipid anchor, and phosphorylation of the cluster, which adds negative charges, releases it (an electrostatic switch, studied by McLaughlin and colleagues).

![A charged membrane in salt water. The membrane carries σ = −0.31 e nm⁻² (20 % anionic lipids at 0.65 nm² per lipid) in a 1:1 salt at 25 °C. A: electric potential against distance from the surface at 150 mM (Debye length 0.78 nm) and 15 mM (2.5 nm): exact Gouy–Chapman solution (solid), a numerical solution of the nonlinear Poisson–Boltzmann boundary-value problem (dots), and the linearized Debye–Hückel solution (dashed), which overestimates the surface potential, strongly so at low salt. B: concentrations of Na⁺ and Cl⁻ at 150 mM: counterions accumulate about sevenfold at the surface and coions are depleted, within about one Debye length. C: surface potential (left axis) and the corresponding lowering of the surface pH relative to the bulk (right axis) against salt concentration for 5, 20 and 100 % anionic lipids, from the Grahame equation](./plots/charged-membrane.py)

### 6.4.3. DNA and Counterion Condensation

DNA is the most highly charged molecule of the cell: one negative phosphate per $0.17\,\mathrm{nm}$ of length in B-DNA (two per base pair of rise $0.34\,\mathrm{nm}$). For such a line charge the mean-field picture predicts something qualitatively new.

**Definition 6.4.1 (Counterion Condensation)** For a linear polyelectrolyte with one elementary charge per length $b$, the Manning parameter is $\xi = \ell_{\mathrm{B}}/b$. **Counterion condensation** is the accumulation, when $z\xi > 1$, of counterions of valence $z$ in a thin layer at the polyelectrolyte, which reduces its effective linear charge to the critical value $e/(z\ell_{\mathrm{B}})$ independently of salt concentration.

**Theorem 6.4.1 (Manning Criterion)** In the limit of low salt, an infinitely thin line charge with Manning parameter $\xi$ retains a finite number of uncondensed counterions of valence $z$ per unit length only if $z\xi \le 1$; when $z\xi > 1$ the fraction of its charge neutralized by condensed counterions is

$$
\theta = 1 - \frac{1}{z\xi}.
$$

**Proof** (Heuristic, after Manning and Oosawa.) The potential of a line charge of density $-e/b$ is $\varphi(r) = (2k_{\mathrm{B}}T\xi/e)\ln r + \mathrm{const}$, by Gauss's law. A counterion of charge $ze$ at distance $r$ has the Boltzmann weight $\mathrm{e}^{-ze\varphi/k_{\mathrm{B}}T} \propto r^{-2z\xi}$, and the number of counterions within radius $R$ per unit length is proportional to $\int_0^Rr^{1 - 2z\xi}\,\mathrm{d}r$, which diverges at $r \to 0$ when $z\xi \ge 1$: the attraction of the line beats the entropy of the counterions, and they collapse onto it. Condensation stops when the remaining charge density $-e(1 - \theta)/b$ gives an effective parameter $z\xi(1 - \theta) = 1$, which is the stated $\theta$. $\square$

For B-DNA in water, $\xi = 0.71/0.17 = 4.2$, and $76\,\%$ of the phosphate charge is neutralized by monovalent counterions ($88\,\%$ by $\ce{Mg^2+}$); single-stranded DNA, with $b \approx 0.6\,\mathrm{nm}$, has $\xi \approx 1.2$ and condenses little. The condensed counterions are not bound to specific sites; they remain mobile within about a nanometer of the backbone, and the remaining charge is screened by the diffuse atmosphere over a Debye length. Numerical solutions of the Poisson–Boltzmann equation around a DNA cylinder of finite radius confirm this two-layer structure.

Condensation has a direct consequence for every protein that binds DNA. When a positively charged protein surface forms ion pairs with phosphates, it displaces the condensed and screening counterions into the bulk, and their gain of translational entropy is a large part of the binding free energy. This makes the binding constant depend steeply on salt.

**Formula 6.4.3 (Salt Dependence of Protein–DNA Binding)** If a protein forms $Z$ ion pairs with the phosphates of B-DNA, the observed equilibrium constant depends on the concentration of monovalent salt as

$$
\frac{\mathrm{d}\lg K_{\mathrm{obs}}}{\mathrm{d}\lg[\ce{M+}]} = -Z\psi, \qquad \psi = 1 - \frac{1}{2\xi} \approx 0.88,
$$
where $\psi$ is the number of counterions released per phosphate neutralized, condensed and screening ions together (Record, Lohman and de Haseth, 1976).

A protein that forms six ion pairs has a slope of $-5.3$: a fourfold increase in salt, from $50$ to $200\,\mathrm{mM}$, lowers its affinity by $10^{5.3 \times 0.6} \approx 1600$-fold. Slopes of several units are typical of DNA-binding proteins, and the salt dependence is a standard way to count the ion pairs at an interface. Because nonspecific binding is largely electrostatic and specific recognition adds hydrogen bonds and shape complementarity that do not depend on salt, raising the salt concentration increases specificity, which is used in the target-search experiments of [7.2.22](/7.2.22) and analyzed in [7.6.17](/7.6.17). The same electrostatics stiffens DNA at low salt (an electrostatic contribution to its persistence length) and resists its packing into phage heads, both treated in [7.6.21](/7.6.21), and $\ce{Mg^2+}$ is required for the folding of RNA, whose compact tertiary structures bring phosphates close together ([7.6.16](/7.6.16)).

![Counterion condensation on DNA. A: end view of B-DNA (radius 1 nm, one phosphate charge per 0.17 nm of length, Manning parameter ξ = ℓB/b = 4.2): about three quarters of the phosphate charge is neutralized by counterions (blue) held within about a nanometer of the backbone in the condensed layer, and the rest is screened over a Debye length by the diffuse atmosphere of counterions and coions (green). B: fraction of the charge neutralized by condensed counterions of valence z = 1, 2 and 3, θ = 1 − 1/(zξ) for zξ > 1, against ξ, with single-stranded DNA (ξ ≈ 1.2), F-actin (about 2.8) and double-stranded DNA marked. C: salt dependence of the binding constant of a protein forming Z ion pairs with DNA, lg[K(c)/K(0.1 M)] = −0.88 Z lg(c/0.1 M), for Z = 3, 6 and 10: binding driven by counterion release weakens steeply as salt is added](./plots/dna-manning.py)

### 6.4.4. Protein Charge and Electrophoresis

The net charge of a protein is the sum over its ionizable groups, each protonated according to the Henderson–Hasselbalch equation with its own $\mathrm{p}K_{\mathrm{a}}$; at the **isoelectric point** ([6.4.2](/6.4.2)) the net charge is zero. Because each group responds to the local potential, the apparent $\mathrm{p}K_{\mathrm{a}}$ of a group is shifted by the potential $\varphi$ at its position created by all other charges and by nearby membranes:

$$
\mathrm{p}K_{\mathrm{a,app}} = \mathrm{p}K_{\mathrm{a,intr}} - \frac{e\varphi}{k_{\mathrm{B}}T\ln 10}, \tag{6.4}
$$
so that in a negative potential protons bind more strongly. This is the same statement as the lowered surface pH of Example 6.4.1, and with the Born energy of 6.2.2 it accounts for most of the measured $\mathrm{p}K_{\mathrm{a}}$ shifts in proteins.

In an electric field $E$ a charged molecule drifts at a velocity $v = \mu E$ set by the balance of the electric force and friction ([7.6.5](/7.6.5)), where $\mu$ is the **electrophoretic mobility** ([6.3.21](/6.3.21)). The ionic atmosphere complicates the simple estimate $\mu = Q/\gamma$, because the counterions are pulled the other way and drag solvent with them.

**Formula 6.4.4 (Electrophoretic Mobility)** For a sphere of radius $a$ with **zeta potential** $\zeta$ (the potential at the slipping plane) in an electrolyte with Debye length $\lambda_{\mathrm{D}} = 1/\kappa$,

$$
\mu = \frac{2\varepsilon_0\varepsilon_{\mathrm{r}}\zeta}{3\eta} \quad (\kappa a \ll 1,\ \text{Hückel}), \qquad
\mu = \frac{\varepsilon_0\varepsilon_{\mathrm{r}}\zeta}{\eta} \quad (\kappa a \gg 1,\ \text{Smoluchowski}),
$$
with Henry's function interpolating between the two limits; in the Hückel limit this is equivalent to $\mu = Q/6\pi\eta a$.

Proteins at physiological salt ($a \approx 2$–$3\,\mathrm{nm}$, $\kappa a \approx 3$) lie between the limits. DNA behaves differently: for a long polyelectrolyte both the driving charge and the friction are proportional to the length (the chain is free-draining at the scale that matters), so in free solution the mobility of DNA longer than a few hundred base pairs is independent of its length, about $3.8\times10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}$; in a field of $10\,\mathrm{V\,cm^{-1}}$ it drifts at about $40\,\mu\mathrm{m\,s^{-1}}$. Separating DNA by size therefore requires a gel or a polymer solution, in which the chain must thread through pores and its mobility falls with length (sieving for short fragments, reptation for long ones), the principle of **electrophoresis** in agarose and polyacrylamide gels ([6.4.14](/6.4.14)). Proteins are separated by charge in isoelectric focusing and by size in SDS gels, where the bound detergent gives them a nearly constant charge-to-mass ratio, again leaving the gel to discriminate by size.

### 6.4.5. Viruses and Other Charged Spheres

Many biological objects are approximately charged spheres: globular proteins, micelles, vesicles and the capsids of viruses. In the linearized theory, a sphere of radius $a$ carrying charge $Ze$ uniformly on its surface has the electrostatic self-energy

$$
U_{\mathrm{self}} = \frac{Z^2k_{\mathrm{B}}T\,\ell_{\mathrm{B}}}{2a(1 + \kappa a)}, \tag{6.5}
$$
the energy of charging the sphere against its own field, which is reduced by the factor $1 + \kappa a$ by the ionic atmosphere. The quadratic dependence on $Z$ makes highly charged objects very costly to assemble. The single-stranded RNA genome of a small icosahedral virus, about $3000$ nucleotides, carries $3000$ negative charges; packed into a sphere of $10\,\mathrm{nm}$ radius it would have, by Eq. (6.5), $9\times10^{6} \times 0.71/(20 \times 13.8)\,k_{\mathrm{B}}T \approx 2\times10^{4}\,k_{\mathrm{B}}T$ of self-energy at $150\,\mathrm{mM}$ salt ($\kappa a = 12.8$), and $3\times10^{5}\,k_{\mathrm{B}}T$ without salt. The cost is paid by neutralization: the capsid proteins of many such viruses have flexible, arginine- and lysine-rich tails that extend into the interior, and across many viruses the number of packaged nucleotides is roughly proportional to the number of basic residues in these tails, with a ratio of order $1.5$–$2$ (Belyi and Muthukumar, 2006), as expected if the genome length is chosen to nearly neutralize the interior with the help of the counterions. Double-stranded DNA phages instead package their genomes with an ATP-driven motor against the combined electrostatic and bending energy, building internal pressures of tens of atmospheres ([7.6.21](/7.6.21)). The net charge of the capsid exterior, in turn, governs the colloidal stability of virus suspensions and their adsorption to cells and surfaces, in the same way as the surface charge of the colloids of [6.3.21](/6.3.21).

## Summary

| Topic | Key results |
|---|---|
| Energy scale (table in 6.1.1) | $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm} = 2.5\,\mathrm{kJ\,mol^{-1}}$; covalent $\sim 150\,k_{\mathrm{B}}T$, ATP $20$, noncovalent $0.1$–$2$ net in water; proteins stable by $20$–$60\,\mathrm{kJ\,mol^{-1}}$ |
| Quantum origin (6.1.2) | Born–Oppenheimer potential surface; peptide bond $40\,\%$ double, planar; electrostatic, induction, dispersion, exchange contributions |
| Energy levels (Eq. (6.1), table in 6.1.3) | Box levels $n^2h^2/8mL^2$; electronic $\sim 100\,k_{\mathrm{B}}T$ frozen out, vibrations mostly ground state, torsions classical, spins nearly equally populated |
| Water (6.1.4) | $55.5\,\mathrm{M}$, $\sim 3.5$ hydrogen bonds per molecule, ps lifetimes; $K_{\mathrm{w}} = 10^{-14}$; $24$ free protons in $1\,\mu\mathrm{m^3}$ at pH $7.4$; $9\times10^6$ charges on the *E. coli* genome |
| Coulomb in water (Eq. (6.2), Definition 6.2.1) | $U = z_1z_2k_{\mathrm{B}}T\ell_{\mathrm{B}}/r$; $\ell_{\mathrm{B}} = 0.71\,\mathrm{nm}$ in water, $56\,\mathrm{nm}$ in vacuum, $14\,\mathrm{nm}$ at $\varepsilon_{\mathrm{r}} = 4$ |
| Born energy (Formula 6.2.1, Example 6.2.1) | $\Delta G = (z^2\ell_{\mathrm{B}}^{\mathrm{vac}}/2a)(1/\varepsilon_2 - 1/\varepsilon_1)k_{\mathrm{B}}T$; $\ce{Na+}$ hydration $-367\,\mathrm{kJ\,mol^{-1}}$; into a bilayer $+73\,k_{\mathrm{B}}T$; buried groups shift $\mathrm{p}K_{\mathrm{a}}$ by several units; buried salt bridges pay desolvation |
| Dipoles (Formula 6.2.2) | $r^{-2}$, $r^{-3}$ fixed; averaged $r^{-4}$, $r^{-6}$ (Keesom) $\propto 1/T$; helix macrodipole $\pm e/2$ |
| Induction, dispersion (Formula 6.2.3) | $p_{\mathrm{ind}} = \alpha E$; London $-\frac32\frac{I_1I_2}{I_1 + I_2}\alpha_1'\alpha_2'/r^6$; $\ce{CH4}$ pair at $0.4\,\mathrm{nm}$: $0.6\,k_{\mathrm{B}}T$ |
| Lennard-Jones (Definition 6.2.2) | $\varepsilon[(r_{\mathrm{m}}/r)^{12} - 2(r_{\mathrm{m}}/r)^6]$; $r_{\mathrm{m}} \approx$ sum of van der Waals radii; carbon $\varepsilon \approx 0.15\,k_{\mathrm{B}}T$; hard core sets packing |
| Hydrogen bonds (6.3.1) | $0.27$–$0.31\,\mathrm{nm}$, directional, saturating; $8\,k_{\mathrm{B}}T$ in vacuum, $1$–$2$ net in water; unpaired buried donors costly; specificity more than affinity |
| Hydrophobic effect (6.3.2) | Solvent free energy; entropic with large $\Delta C_p$ at small scale, interfacial at large; $\approx 0.1\,\mathrm{kJ\,mol^{-1}\,\AA^{-2}}$ |
| Poisson–Boltzmann (Formula 6.4.1, Eq. (6.3)) | $\nabla^2y = \kappa^2\sinh y$; $\lambda_{\mathrm{D}} = 0.304/\sqrt{I}\,\mathrm{nm}$, $0.78\,\mathrm{nm}$ at $150\,\mathrm{mM}$; screened Coulomb; fails for multivalent ions |
| Charged membranes (Formula 6.4.2, Example 6.4.1) | Grahame $\sinh(y_0/2) = \lambda_{\mathrm{D}}/\ell_{\mathrm{GC}}$; $20\,\%$ anionic lipid: $-49\,\mathrm{mV}$, $6.6$-fold cation enrichment, surface pH $-0.8$; electrostatic switches |
| DNA (Definition 6.4.1, Theorem 6.4.1, Formula 6.4.3) | $\xi = \ell_{\mathrm{B}}/b = 4.2$; $\theta = 1 - 1/z\xi = 0.76$ ($z = 1$); counterion release: $\mathrm{d}\lg K/\mathrm{d}\lg[\ce{M+}] = -0.88Z$ |
| Charge and electrophoresis (Eq. (6.4), Formula 6.4.4) | $\mathrm{p}K_{\mathrm{a}}$ shifted by $-e\varphi/(k_{\mathrm{B}}T\ln 10)$; $\mu = 2\varepsilon\zeta/3\eta$ to $\varepsilon\zeta/\eta$; DNA free mobility length independent, gels sieve |
| Charged spheres (Eq. (6.5)) | $U_{\mathrm{self}} = Z^2k_{\mathrm{B}}T\ell_{\mathrm{B}}/2a(1 + \kappa a)$; RNA genomes neutralized by basic capsid tails |

## Questions

1. Calculate the Bjerrum length in water at $37\,{}^\circ\mathrm{C}$ ($\varepsilon_{\mathrm{r}} = 74.2$) and in the hydrocarbon core of a membrane ($\varepsilon_{\mathrm{r}} = 2$). What is the electrostatic energy of two opposite monovalent ions at $0.5\,\mathrm{nm}$ in each medium?

   **Answer** $\mathrm{e}^2/(4\pi\varepsilon_0k_{\mathrm{B}}T) = 53.9\,\mathrm{nm}$ at $310\,\mathrm{K}$, so $\ell_{\mathrm{B}} = 53.9/74.2 = 0.73\,\mathrm{nm}$ in water and $27\,\mathrm{nm}$ in the membrane core. At $0.5\,\mathrm{nm}$ the energies are $-0.73/0.5 = -1.5\,k_{\mathrm{B}}T$ in water and $-54\,k_{\mathrm{B}}T$ in the membrane: an ion pair that is easily dissociated in water would never dissociate in a membrane (though forming it there is prevented by the larger Born cost of bringing two ions in).

2. Estimate whether a salt bridge between an Asp and a Lys buried in the interior of a protein ($\varepsilon_{\mathrm{r}} = 4$, ion radii $0.25\,\mathrm{nm}$, contact distance $0.4\,\mathrm{nm}$) stabilizes the protein relative to the two side chains being exposed to water without interacting. What would make it stabilizing?

   **Answer** Coulomb gain in the interior: $\ell_{\mathrm{B}}(\varepsilon_{\mathrm{r}} = 4)/0.4 = 14/0.4 = 35\,k_{\mathrm{B}}T$. Born cost of moving each charge from water into the interior: $(56/0.5)(1/4 - 1/78.4) = 27\,k_{\mathrm{B}}T$, $53\,k_{\mathrm{B}}T$ for both. Net: about $18\,k_{\mathrm{B}}T$ destabilizing. It becomes favourable if the protein supplies additional polar interactions to both charges (hydrogen bonds, helix dipoles, a network of several ion pairs), if the site is partly accessible to water (higher effective permittivity) or if the pair is needed functionally despite the cost. The estimate explains why buried salt bridges are rare and why mutating them often has little effect on stability.

3. What is the Debye length at $1\,\mathrm{mM}$ and at $150\,\mathrm{mM}$ NaCl? What fraction of the unscreened Coulomb interaction between two charges $2\,\mathrm{nm}$ apart remains in each case? An enzyme–substrate association rate falls sixfold when the salt concentration is raised from $10$ to $150\,\mathrm{mM}$. What does this suggest?

   **Answer** $\lambda_{\mathrm{D}} = 0.304/\sqrt{0.001} = 9.6\,\mathrm{nm}$ and $0.304/\sqrt{0.15} = 0.78\,\mathrm{nm}$. The factors $\mathrm{e}^{-2/9.6} = 0.81$ and $\mathrm{e}^{-2/0.78} = 0.08$. A strong decrease of the association rate with ionic strength indicates that opposite charges on the two molecules attract them before contact (electrostatic steering), which salt screens; the rate at high salt approaches that of uncharged molecules with the same geometry ([7.6.17](/7.6.17)).

4. A membrane contains $20\,\%$ anionic lipids ($0.65\,\mathrm{nm^2}$ per lipid) and is bathed in $15\,\mathrm{mM}$ NaCl. Calculate the surface potential, the concentration of $\ce{Na+}$ at the surface and the shift of surface pH. Compare with $150\,\mathrm{mM}$ (Example 6.4.1) and explain why the linearized theory fails here.

   **Answer** $\lambda_{\mathrm{D}} = 0.304/\sqrt{0.015} = 2.48\,\mathrm{nm}$, $\ell_{\mathrm{GC}} = 0.72\,\mathrm{nm}$, so $\sinh(y_0/2) = -3.43$, $y_0/2 = -1.95$, $y_0 = -3.9$, $\varphi_0 = -100\,\mathrm{mV}$. Surface $\ce{Na+}$: $15\,\mathrm{mM} \times \mathrm{e}^{3.9} = 0.74\,\mathrm{M}$; surface pH lowered by $3.9/2.30 = 1.7$ units. Tenfold less salt doubles the surface potential but leaves the surface counterion concentration within the same range, because the surface charge must be neutralized by about the same number of counterions in a thicker layer. The linearized theory assumes $\lvert y\rvert \ll 1$ and gives $y_0 = -2\lambda_{\mathrm{D}}/\ell_{\mathrm{GC}} = -6.9$ ($-176\,\mathrm{mV}$), far too large: at such potentials the Boltzmann factors are strongly nonlinear.

5. Single-stranded DNA has about one phosphate per $0.6\,\mathrm{nm}$ of contour. What fraction of its charge is neutralized by condensed $\ce{Na+}$ and by condensed $\ce{Mg^2+}$? Compare with double-stranded DNA and comment on the consequences for proteins that bind single-stranded DNA.

   **Answer** $\xi = 0.71/0.6 = 1.2$; for $z = 1$, $\theta = 1 - 1/1.2 = 0.15$; for $z = 2$, $\theta = 1 - 1/2.4 = 0.58$. Double-stranded DNA: $0.76$ and $0.88$. Binding to ssDNA releases fewer counterions per ion pair, so its affinity depends less steeply on monovalent salt, and $\ce{Mg^2+}$ affects ssDNA more than $\ce{Na+}$. (Real ssDNA is flexible and its local charge density varies with conformation, so the line-charge model is only a guide.)

6. A protein binds a DNA site with $K = 10^{10}\,\mathrm{M^{-1}}$ at $0.1\,\mathrm{M}$ KCl and forms $8$ ion pairs with the phosphates. Estimate $K$ at $0.05$ and at $0.2\,\mathrm{M}$ KCl. What part of the binding free energy at $0.1\,\mathrm{M}$ could be called nonelectrostatic, if extrapolation to $1\,\mathrm{M}$ salt is taken to remove the counterion-release contribution?

   **Answer** Slope $-0.88 \times 8 = -7.0$. At $0.05\,\mathrm{M}$: $\lg K = 10 + 7.0 \times \lg 2 = 12.1$; at $0.2\,\mathrm{M}$: $10 - 2.1 = 7.9$. At $1\,\mathrm{M}$: $\lg K = 10 - 7.0 = 3.0$, which corresponds to $\Delta G^\circ = -RT\ln(10^{3}) = -17\,\mathrm{kJ\,mol^{-1}}$ at $25\,{}^\circ\mathrm{C}$, compared with $-57\,\mathrm{kJ\,mol^{-1}}$ at $0.1\,\mathrm{M}$. The salt-independent part, from hydrogen bonds, van der Waals contacts and the hydrophobic effect, is what discriminates the specific site; most of the affinity at physiological salt comes from counterion release, which is the same for specific and nonspecific DNA.

7. Use the London formula to estimate the dispersion attraction of two argon atoms at contact ($\alpha' = 1.64\times10^{-3}\,\mathrm{nm^3}$, $I = 15.8\,\mathrm{eV}$, $r = 0.38\,\mathrm{nm}$), and compare with the measured well depth of the argon dimer, $1.2\times10^{-21}\,\mathrm{J}$. Why does the London estimate exceed it?

   **Answer** $U = -\frac34 \times 15.8 \times (1.64\times10^{-3})^2/(0.38)^6\,\mathrm{eV} = -\frac34 \times 15.8 \times 2.69\times10^{-6}/3.01\times10^{-3} = -0.0106\,\mathrm{eV} = -1.7\times10^{-21}\,\mathrm{J}$, about $0.4\,k_{\mathrm{B}}T$. The measured well depth is about $70\,\%$ of this, because at the minimum the exchange repulsion already cancels part of the attraction: the London term is the attraction alone, and the well of the Lennard-Jones potential at $r_{\mathrm{m}}$ is the sum of both. The agreement in order of magnitude shows that the formula captures the physics.

8. Explain, with a numerical estimate, why lipid bilayers are almost impermeable to $\ce{K+}$ but permeable to water and $\ce{O2}$, and how valinomycin makes them permeable to $\ce{K+}$.

   **Answer** The Born cost of moving $\ce{K+}$ (Born radius about $0.23\,\mathrm{nm}$) from water into a medium of $\varepsilon_{\mathrm{r}} = 2$ is $(56/0.46)(0.5 - 0.013) \approx 59\,k_{\mathrm{B}}T$, so its partition coefficient into the membrane core is about $\mathrm{e}^{-59} \approx 10^{-26}$. Water and $\ce{O2}$ are neutral: their partition coefficients are $10^{-4}$–$10^{-1}$, set by hydrogen bonding (water) or small dispersion differences ($\ce{O2}$), and they cross rapidly. Valinomycin surrounds $\ce{K+}$ with six carbonyl oxygens that replace the hydration shell and presents a hydrophobic surface of radius about $0.6\,\mathrm{nm}$; the Born cost of the complex is $(56/1.2)(0.487) \approx 23\,k_{\mathrm{B}}T$, partly offset by the favourable transfer of its hydrophobic surface, so the complex partitions into the membrane at a useful rate.

9. Why is the electrophoretic mobility of long DNA in free solution independent of its length, and how does a gel restore separation by size? Estimate how far a DNA molecule travels in $1\,\mathrm{h}$ in free solution at $5\,\mathrm{V\,cm^{-1}}$.

   **Answer** The electric force is proportional to the charge, which is proportional to the length, and, because the counterions and the solvent move around each segment locally (free draining, with hydrodynamic interactions screened by the counterion atmosphere), the friction is also proportional to the length; their ratio, the mobility, is constant. In a gel the chain must pass through pores comparable to or smaller than its size: short fragments are sieved (Ogston), long ones move head-first by reptation, and in both regimes the mobility falls with length. Free solution: $v = 3.8\times10^{-8} \times 500\,\mathrm{m\,s^{-1}} = 1.9\times10^{-5}\,\mathrm{m\,s^{-1}}$, $6.8\,\mathrm{cm}$ in an hour for all lengths alike.

10. (Concept) Why do biologists say that the hydrophobic effect "is not a force between nonpolar groups", and what experimental signature distinguishes it from the attraction of two dipoles?

    **Answer** Two hydrocarbon molecules attract each other by dispersion about as strongly as each attracts water, so a direct interaction cannot explain their association in water. Their association is driven by the change in the free energy of the solvent when the nonpolar surface exposed to water decreases; it is a potential of mean force that exists only in water and depends on the structure of water around the solutes. Its signatures are thermodynamic: at room temperature an unfavourable transfer free energy that is mostly entropic with a near-zero enthalpy, a large positive heat capacity change of hydration (so that the effect weakens on cooling, causing cold denaturation), proportionality to buried nonpolar area, and weakening by cosolvents that perturb water structure. A dipole–dipole attraction, by contrast, exists in vacuum, is enthalpic, and becomes weaker with increasing temperature when averaged over orientations, as $1/T$ (Formula 6.2.2).
