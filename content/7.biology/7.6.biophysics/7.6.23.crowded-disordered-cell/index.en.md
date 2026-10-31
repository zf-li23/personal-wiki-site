---
title: Life in Crowded and Disordered Environments
description: "Macromolecular crowding and its consequences: the census of the crowded cell, filament networks and crowded membranes; lattice and scaled-particle models of crowding on binding, nonideal osmotic pressure of hemoglobin, depletion forces and entropic ordering, excluded volume and polymer swelling, crowding at membranes; reaction rates, obstructed and anomalous diffusion (continuous-time random walks, fractional Brownian motion, ergodicity breaking) and active diffusion driven by motors."
---

The binding curves and diffusion laws of the earlier chapters assumed dilute, homogeneous solutions: molecules far apart compared with their size, interacting only with their specific partners, and free to wander wherever their random walk takes them. A cell is nothing like this. A bacterium contains about $300\,\mathrm{g\,L^{-1}}$ of protein and RNA, so that neighboring macromolecules are separated by little more than their own diameter; filament networks crisscross the cytoplasm and the extracellular space; and membranes are as much protein as lipid. This chapter asks how such crowding changes equilibria and dynamics. Its answers are toy models in the spirit of the rest of the course: lattice models and hard spheres that show why inert crowders favor binding and compaction, why entropy alone produces attractive forces and order, and why motion in a crowded, viscoelastic and actively stirred medium is often not ordinary diffusion.

The concepts used are the **entropic force** and the statistical mechanics of binding of [7.6.2](/7.6.2) and [7.6.3](/7.6.3), the random walks, **Langevin equation** and **fluctuation–dissipation theorem** of [7.6.5](/7.6.5), the polymer physics of [7.6.21](/7.6.21), and the viscoelasticity of [7.6.22](/7.6.22#sec-22.7). **Macromolecular crowding** was introduced in [7.1.1](/7.1.1) and the **biomolecular condensates** it favors are in [7.2.21](/7.2.21) and [7.6.29](/7.6.29); the experimental tools, **fluorescence recovery after photobleaching** and single-particle tracking, are in [7.3.2](/7.3.2) and [7.6.12](/7.6.12), and the hop diffusion of membrane proteins in [7.3.4](/7.3.4#sec-4.5.3).

## 23.1. Crowding, Linkage and Entanglement

### 23.1.1. The Cell Is Crowded

The census of a bacterium ([7.6.20](/7.6.20)) gives the simplest measure of crowding. An *E. coli* cell of about $1\,\mu\mathrm{m^3}$ holds about $3\times10^6$ protein molecules, so each protein has a volume of $(1\,\mu\mathrm{m})^3/3\times10^6 \approx 330\,\mathrm{nm^3}$, a cube of $7\,\mathrm{nm}$. A protein of radius $2.5\,\mathrm{nm}$ thus sits with only a few nanometers of water between it and its neighbors, about one protein diameter. Measured concentrations of macromolecules are $300$–$400\,\mathrm{g\,L^{-1}}$ in *E. coli* and $200$–$300\,\mathrm{g\,L^{-1}}$ in eukaryotic cytoplasm, and the red cell is filled with $330\,\mathrm{g\,L^{-1}}$ of hemoglobin; with a partial specific volume of $0.73\,\mathrm{mL\,g^{-1}}$ and bound water, these correspond to volume fractions of $0.2$–$0.4$.

The contrast with the test tube is a factor of ten in spacing and a thousand in concentration. At $1\,\mu\mathrm{M}$, a high concentration for a biochemical assay, there are $6\times10^{2}$ molecules per $\mu\mathrm{m^3}$, separated by about $120\,\mathrm{nm}$. Kornberg's tenth commandment of enzymology, "correct for extract dilution with molecular crowding", states the consequence: activities that require the cell's crowded interior often disappear on dilution and reappear when inert polymers such as polyethylene glycol (PEG), dextran or Ficoll are added to the assay.

### 23.1.2. Filament Networks

Crowding is not only a matter of compact proteins. The **cytoskeleton** is a set of polymer networks: the actin cortex under the plasma membrane, with a mesh size of $50$–$200\,\mathrm{nm}$, the dendritic network at the leading edge of a crawling cell, the bundles of **microtubules** and neurofilaments in an axon. Outside the cell, the **extracellular matrix** is a felt of collagen fibrils and proteoglycans, and the wall of a bacterium a single crosslinked molecule of **peptidoglycan**. These networks are linked (crosslinked by proteins, attached to membranes) and entangled (filaments cannot pass through each other), and their mesh size, not the size of the cell, sets the scale on which they obstruct diffusion. For a solution of actin filaments at mass concentration $c$, the mesh size is about $\xi \approx 0.3\,\mu\mathrm{m}/\sqrt{c/(\mathrm{mg\,mL^{-1}})}$, about $100\,\mathrm{nm}$ at the $10\,\mathrm{mg\,mL^{-1}}$ of a cortex: proteins pass through freely, while vesicles and ribosome-sized particles are caged.

Filaments in cells are rarely random. Aligned bundles stiffen microvilli and filopodia, aligned collagen gives tendons their tensile strength, aligned cellulose microfibrils let a tree grow a hundred meters tall, and the polarity of filaments in a bundle is set by nucleation sites and sorting by motors rather than by entropy ([7.6.26](/7.6.26)). The mechanics of such networks is the subject of [7.6.26](/7.6.26) and [7.6.31](/7.6.31); here they matter as obstacles.

### 23.1.3. Crowded Membranes

Membranes are crowded in two dimensions. The inner and outer membranes of *E. coli*, each about $6\,\mu\mathrm{m^2}$, hold some $5\times10^5$ protein molecules each, about $12\,\mathrm{nm^2}$ per protein, a mean spacing of $3.5\,\mathrm{nm}$: roughly half the area is protein. In the inner mitochondrial membrane protein is about $70\,\%$ of the mass, and freeze-fracture images show a surface paved with particles. Lipids in such membranes are mostly in contact with proteins, and membrane proteins diffuse $10$–$100$ times more slowly than in pure lipid bilayers ([7.3.4](/7.3.4#sec-4.5)).

### 23.1.4. Two Kinds of Consequence

Crowding alters equilibria and kinetics. Inert crowders shift binding towards association: in the T4 DNA replication system, PEG 12000 at $7.5\,\%$ by weight lowers the dissociation constant of the clamp loader (gp44/62) for the sliding clamp (gp45) by more than an order of magnitude, although PEG binds neither protein (Jarvis and colleagues 1990). Crowding also slows diffusion. FRAP in mammalian cells gives cytoplasmic diffusion coefficients about a quarter of those in water for small molecules and GFP, and much smaller fractions for large DNA fragments and dextrans (Verkman 2002); in *E. coli*, GFP diffuses at about $8\,\mu\mathrm{m^2\,s^{-1}}$, a tenth of its value in water. Tracking single membrane proteins reveals trajectories in which free diffusion alternates with confinement in cages and transient trapping. The rest of the chapter builds minimal models of these effects: 23.2 for equilibria, 23.3 for dynamics.

## 23.2. Equilibria in Crowded Environments

### 23.2.1. Crowding and Binding: Lattice Models

Divide the reaction volume into $\Omega$ lattice cells. Each cell holds a solvent molecule, a ligand or an inert crowder, and a single receptor binds one ligand with energy $\varepsilon_L$ relative to solution. With $L$ ligands and $C$ crowders of the same size, the partition function of the solution is the number of arrangements,

$$
Z_{\mathrm{sol}}(L, C) = \frac{\Omega!}{L!\,C!\,(\Omega - L - C)!}\,\mathrm{e}^{-\beta(L\varepsilon_L^{\mathrm{sol}} + C\varepsilon_C^{\mathrm{sol}})},
$$
and the probability that the receptor is occupied is the ratio of the weight of the bound state, $Z_{\mathrm{sol}}(L - 1, C)\mathrm{e}^{-\beta\varepsilon_L^{\mathrm{b}}}$, to the sum of both weights. Dividing by $Z_{\mathrm{sol}}(L - 1, C)$ and using $\Omega - L - C \gg 1$,

$$
p_{\mathrm{bound}} = \frac{1}{1 + \dfrac{\Omega - L - C}{L}\,\mathrm{e}^{\beta\varepsilon_L}}, \qquad \varepsilon_L = \varepsilon_L^{\mathrm{b}} - \varepsilon_L^{\mathrm{sol}}. \tag{23.1}
$$
The crowders reduce the volume available to the ligands from $\Omega$ to $\Omega - C$ cells: their effective concentration rises and so does the occupancy. The effect is appreciable only when $C$ is comparable to $\Omega$, at the volume fractions of the cytoplasm.

Real crowders and ligands differ in size. Let each ligand (here a protein) occupy $r$ small cells, each the size of one crowder, and let the proteins sit on a coarser lattice of $\Omega$ large cells. Counting the arrangements of $L$ proteins on the large lattice and $C$ crowders on the $r\Omega - rL$ remaining small cells and repeating the calculation with $(N + r)!/N! \approx N^r$ gives the following result.

**Formula 23.2.1 (Crowding and Dissociation Constants: Lattice Model)** For a protein that excludes $r$ times the volume of a crowder, at crowder volume fraction $\varphi = C/r\Omega$ and dilute protein,

$$
p_{\mathrm{bound}} = \frac{1}{1 + \dfrac{\Omega}{L}(1 - \varphi)^r\,\mathrm{e}^{\beta\varepsilon_L}}, \qquad \frac{K_{\mathrm{d}}(\varphi)}{K_{\mathrm{d}}(0)} = (1 - \varphi)^r.
$$

The exponent $r$ makes the effect strong: binding is favored by the volume freed for the crowders when two large molecules combine, and for $r \gg 1$ even a modest $\varphi$ changes $K_{\mathrm{d}}$ by orders of magnitude. For the T4 proteins (gp44/62 of $164\,\mathrm{kDa}$ and PEG of $12\,\mathrm{kDa}$) the mass ratio suggests $r \approx 15$, while a fit of the measured $K_{\mathrm{d}}(\varphi)$ gives $r \approx 45$: PEG is a flexible polymer whose excluded volume is larger than its mass suggests, and the lattice model forbids arrangements (a ligand between lattice positions) that real molecules can adopt.

### 23.2.2. Scaled-Particle Theory

A more faithful model treats all molecules as hard spheres, which exclude each other from a volume set by the sum of their radii but are otherwise inert. The cost of inserting a molecule into the crowded solution is the work needed to open a cavity for it.

**Definition 23.2.1 (Excluded Volume)** The **excluded volume** of a molecule with respect to another is the volume in which the center of the second molecule cannot be placed without overlapping the first: for hard spheres of radii $R_1$ and $R_2$, a sphere of radius $R_1 + R_2$.

**Formula 23.2.2 (Scaled-Particle Theory)** The activity coefficient of a hard sphere of radius $R$ in a fluid of hard-sphere crowders of radius $r_{\mathrm{c}}$ at volume fraction $\varphi$ is, with $z = R/r_{\mathrm{c}}$ and $y = \varphi/(1 - \varphi)$,

$$
\ln\gamma = -\ln(1 - \varphi) + (3z + 3z^2 + z^3)\,y + \left(\tfrac92 z^2 + 3z^3\right)y^2 + 3z^3y^3
$$
(Lebowitz, Helfand and Praestgaard 1965). For an association $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$, the thermodynamic equilibrium constant is fixed, so the apparent dissociation constant measured in concentrations changes by

$$
\frac{K_{\mathrm{d}}(\varphi)}{K_{\mathrm{d}}(0)} = \frac{\gamma_{\mathrm{AB}}}{\gamma_{\mathrm{A}}\gamma_{\mathrm{B}}}. \tag{23.2}
$$

The **activity coefficient** ([6.3](/6.3)) measures the excess chemical potential, $\mu = \mu^\circ + k_{\mathrm{B}}T\ln(\gamma c/c^\circ)$; a crowded solution makes every large solute act as if it were at a higher concentration, and complexes, which exclude less volume than their separated parts, gain most. Two features distinguish the hard-sphere result from the lattice model. The effect grows steeply with the size ratio $z$: at the same volume fraction, small crowders exclude large molecules more effectively than large crowders, because the volume from which a large sphere is excluded, a shell of thickness $r_{\mathrm{c}}$, is large compared with the crowders' own volume. And the effect is nonlinear in $\varphi$: crowding is negligible below a volume fraction of about $0.1$ and dominant above $0.2$, which is where cells are.

![Crowding shifts binding equilibria. A: lattice model of a receptor among Ω = 1000 lattice cells holding L ligands and C inert crowders of the same size (binding energy −5 k_BT, Eq. (23.1)): the more crowders, the higher the occupancy at the same number of ligands. B: dissociation constant relative to its dilute value against the crowder volume fraction: lattice model (1 − φ)^r for r = 15 and r = 45 (Formula 23.2.1), and scaled-particle theory (Formula 23.2.2 with Eq. (23.2)) for the dimerization of two hard spheres of radius 2.5 nm among crowders of radius 2 or 5 nm. At the volume fractions of the cytoplasm (shaded) complexes are stabilized several-fold to a hundred-fold, more strongly by small crowders](./plots/crowding-binding.py)

The same reasoning applies to any process that changes the excluded volume of a molecule. Folding compacts a protein and is stabilized by crowding by a few $k_{\mathrm{B}}T$, mostly by destabilizing the expanded unfolded state ([7.6.16](/7.6.16)); polymerization of actin and tubulin, the formation of amyloid fibrils and the phase separation of condensates are all favored by crowders ([7.6.29](/7.6.29)). Crowding is not always inert: crowders also interact weakly with proteins through charges and hydrophobic patches, and these "soft" interactions can partly cancel the hard-core effect, which is why measured crowding effects in cell lysates and in cells are often smaller than those of synthetic polymers.

### 23.2.3. Osmotic Pressure of Crowded Solutions

The **osmotic pressure** of a solution ([6.3.5](/6.3.5)) measures the same nonideality. In the lattice model with $H$ hemoglobin molecules on $\Omega$ cells of volume $\nu$, the osmotic pressure is the free-energy change per volume when the volume shrinks by one cell, $p\nu = G(\Omega - 1) - G(\Omega) = -k_{\mathrm{B}}T\ln[Z_{\mathrm{sol}}(H, \Omega - 1)/Z_{\mathrm{sol}}(H, \Omega)]$, which gives

$$
\Pi = \frac{k_{\mathrm{B}}T}{\nu}\ln\frac{\Omega}{\Omega - H} = -\frac{k_{\mathrm{B}}T}{\nu}\ln(1 - c\nu), \tag{23.3}
$$
with $c = H/\Omega\nu$ the number concentration. At low concentration $\Pi \approx ck_{\mathrm{B}}T(1 + c\nu/2 + \cdots)$: the van 't Hoff law with a second **virial coefficient** $\nu/2$. Hard spheres do better.

**Formula 23.2.3 (Hard-Sphere Osmotic Pressure)** For hard spheres of volume $V$ at number concentration $c$ and volume fraction $\varphi = cV$, the osmotic pressure is accurately given by the Carnahan–Starling equation

$$
\Pi = ck_{\mathrm{B}}T\,\frac{1 + \varphi + \varphi^2 - \varphi^3}{(1 - \varphi)^3},
$$
whose expansion $\Pi = ck_{\mathrm{B}}T(1 + 4\varphi + 10\varphi^2 + 18.4\varphi^3 + 28.2\varphi^4 + \cdots)$ reproduces the virial coefficients computed by Boltzmann. The corresponding activity coefficient is $\ln\gamma = (8\varphi - 9\varphi^2 + 3\varphi^3)/(1 - \varphi)^3$.

**Example 23.2.1 (Hemoglobin)** Ross and Minton (1977) measured the osmotic pressure of hemoglobin solutions up to $350\,\mathrm{g\,L^{-1}}$. With a molar mass of $64.5\,\mathrm{kDa}$ and a single parameter, a hard-sphere diameter of $5.8\,\mathrm{nm}$ close to the size of the molecule in crystal structures ($V = 102\,\mathrm{nm^3}$), Formula 23.2.3 describes the data over the whole range; the lattice model, whose only parameter is $\nu$, reproduces the trend but not the shape. At $330\,\mathrm{g\,L^{-1}}$, $c = 330/64.5\,\mathrm{mM} = 5.1\,\mathrm{mM}$, $\varphi = 0.31$, the osmotic pressure is about four times the ideal value and the activity coefficient is about $200$: in a red cell, hemoglobin behaves as if it were two hundred times more concentrated than it is. This is why sickle-cell hemoglobin, whose deoxy form polymerizes, polymerizes so readily in the cell and why the delay time before it polymerizes varies as about the inverse thirtieth power of its concentration ([7.6.29](/7.6.29)).

![Osmotic pressure and activity of concentrated hemoglobin (0 °C; molar mass 64.5 kDa, hard-sphere diameter 5.8 nm). A: osmotic pressure against concentration: ideal (van 't Hoff), lattice model with lattice cell volumes 2V and 3V (Eq. (23.3), which diverges when the cells are full), and the hard-sphere fluid (Formula 23.2.3), which describes the measurements of Ross and Minton with a single size parameter. B: activity coefficient of hemoglobin from the hard-sphere model: at the 330 g/L of the red cell interior (dotted) the effective concentration is one to two hundred times the actual one](./plots/osmotic-hemoglobin.py)

### 23.2.4. Depletion Forces: Order from Disorder

Two large particles in a solution of small inert crowders attract each other, although no force acts between them, the crowders or the solvent other than hard-core repulsion. The center of a crowder of radius $r$ cannot approach a large sphere of radius $R$ closer than $R + r$: each large sphere is surrounded by a depletion shell of thickness $r$ from which the crowders are excluded. When two large spheres come within $D < 2(R + r)$ of each other, their shells overlap, the total excluded volume decreases by the overlap $V_{\mathrm{ov}}(D)$, and the crowders gain that volume and entropy.

**Definition 23.2.2 (Depletion Force)** A **depletion force** is the attractive **entropic force** between two particles, or between a particle and a wall, in a solution of smaller particles that are excluded from the gap between them: it equals the osmotic pressure of the small particles times the rate of change with distance of the volume from which they are excluded (Asakura and Oosawa 1954).

**Formula 23.2.4 (Asakura–Oosawa Potential)** For $N$ crowders in a volume $V_{\mathrm{box}}$, the free energy of exclusion is $G_{\mathrm{ex}} = -Nk_{\mathrm{B}}T\ln[(V_{\mathrm{box}} - V_{\mathrm{ex}})/V_{\mathrm{box}}] \approx \Pi V_{\mathrm{ex}}$ with $\Pi = nk_{\mathrm{B}}T$ the ideal osmotic pressure of the crowders ($n = N/V_{\mathrm{box}}$). For two spheres of radius $R$ at center distance $2R \le D \le 2(R + r)$, the overlap of the depletion shells is two spherical caps,

$$
V_{\mathrm{ov}}(D) = \frac{2\pi}{3}\left(R + r - \frac D2\right)^2\left(2R + 2r + \frac D2\right),
$$
and the interaction free energy and force are

$$
W(D) = -\Pi\,V_{\mathrm{ov}}(D), \qquad F = -\frac{\mathrm{d}W}{\mathrm{d}D} = -\pi\Pi\left[(R + r)^2 - \frac{D^2}{4}\right] \tag{23.4}
$$
(the minus sign of $F$ denoting attraction). For $R \gg r$ the contact value is $W(2R) \approx -2\pi Rr^2\Pi = -\frac32\varphi\frac Rr\,k_{\mathrm{B}}T$, with $\varphi = \frac43\pi r^3n$ the crowder volume fraction.

**Proof** The volume of each cap is the volume of a spherical sector of radius $R + r$ and half-angle $\theta$, with $\cos\theta = (D/2)/(R + r)$, minus that of the cone with the same apex and base: $\frac{2\pi}{3}(R + r)^2(R + r - D/2) - \frac{\pi}{3}\frac D2[(R + r)^2 - D^2/4]$. Doubling and simplifying gives $V_{\mathrm{ov}}$. Differentiating, $\mathrm{d}V_{\mathrm{ov}}/\mathrm{d}D = -\pi[(R + r)^2 - D^2/4]$. At contact, $R + r - R = r$ and $V_{\mathrm{ov}} = \frac{2\pi}{3}r^2(3R + 2r) \approx 2\pi Rr^2$, and $2\pi Rr^2n = \frac32\varphi R/r$. $\square$

**Example 23.2.2** For a bead of $R = 1\,\mu\mathrm{m}$ in a solution of $1\,\mathrm{mM}$ of crowders of $r = 2\,\mathrm{nm}$, $\Pi = 6.0\times10^{23}\,\mathrm{m^{-3}} \times 4.1\times10^{-21}\,\mathrm{J} = 2.5\,\mathrm{kPa}$. The contact energy is $2\pi \times 10^{-6} \times (2\times10^{-9})^2 \times 2.5\times10^3\,\mathrm{J} = 6.2\times10^{-20}\,\mathrm{J} = 15\,k_{\mathrm{B}}T$, and at a gap of one crowder radius the force is $\pi\Pi Rr \approx 16\,\mathrm{pN}$, comparable to the force of several molecular motors. In the cell, where proteins are at millimolar total concentrations, micrometer-sized objects such as vesicles, chromosomes or the nucleoid are pressed together by forces of this size.

![Depletion attraction (Asakura–Oosawa model, Formula 23.2.4). A: interaction free energy of two spheres of radius 1 µm against their surface separation h = D − 2R, in solutions of crowders of radius 2 nm at 0.5, 1 and 2 mM: the attraction is short-ranged (it vanishes beyond h = 2r) and deep, 15 k_BT at contact at 1 mM. B: the depletion force, linear in the separation; at h = r (dotted) it is about πnk_BTrR, 16 pN at 1 mM. C: contact free energy at a fixed crowder volume fraction of 0.1 against the size ratio R/r: it grows as (3/2)φR/r, so that at the same volume fraction small crowders bind large particles strongly, while two proteins of the crowders' own size attract by only a fraction of k_BT](./plots/depletion.py)

Depletion forces have been measured directly. Two silica beads of $1.25\,\mu\mathrm{m}$ diameter, confined by a scanned optical trap to move along a line in a solution of λ-phage DNA (which forms coils of about $0.5\,\mu\mathrm{m}$ radius that exclude each other like hard spheres), sample distances with the Boltzmann weight $\mathrm{e}^{-\beta W(D)}$; the logarithm of the measured distance distribution gives $W(D)$, which follows Formula 23.2.4 with the coil radius as fitted size (Verma, Crocker, Lubensky and Yodh 1998). The fitted osmotic pressure was about half the van 't Hoff value of the DNA, a reminder that soft polymer coils are not hard spheres.

Depletion also orders. A mixture of rod-like viruses and spheres separates on purely entropic grounds into alternating layers of rods and spheres, a microphase separation (Adams, Dogic, Keller and Fraden 1998); hard rods alone form a nematic liquid crystal above a critical concentration (Onsager), because aligned rods exclude less volume from each other. In cells, depletion by crowders bundles actin filaments and DNA, compacts the bacterial nucleoid into a region separated from the ribosome-rich cytoplasm, and promotes the adhesion of vesicles to membranes. Whether a specific cellular structure relies on it is often hard to show, because depletion acts on everything at once.

### 23.2.5. Excluded Volume Within a Polymer

Excluded volume also acts between the parts of one large molecule. Place $N$ molecules on a lattice of $\Omega$ cells, with at most one per cell. Compared with ideal particles that ignore each other, the ratio of partition functions is $Z_{\mathrm{ex}}/Z_{\mathrm{nex}} = \Omega!/[(\Omega - N)!\,\Omega^N] \approx (1 - N/\Omega)^N$ by Stirling's formula, and

$$
\Delta G_{\mathrm{ex}} = -Nk_{\mathrm{B}}T\ln\left(1 - \frac N\Omega\right) \approx k_{\mathrm{B}}T\frac{N^2}{\Omega} = Nk_{\mathrm{B}}T\varphi: \tag{23.5}
$$
excluded volume raises the free energy by $k_{\mathrm{B}}T$ times the volume fraction per molecule. Applied to the Kuhn segments of a polymer coil of size $R$, each a cylinder of length $a$ and diameter $d$ excluding a volume $\frac{\pi}{2}a^2d$ (averaged over orientations) from another, this repulsion competes with the entropic elasticity of the chain, $3k_{\mathrm{B}}TR^2/2Na^2$. Minimizing the sum (Flory's argument, developed in [7.6.21](/7.6.21)) gives $R \sim (a^4d)^{1/5}N^{3/5}$, a coil swollen beyond the random-walk size $\sqrt N a$. Comparing the two terms at the random-walk size, swelling matters only for $N \gtrsim (a/d)^2$ segments. For DNA, with $a = 100\,\mathrm{nm}$ and a bare diameter of $2\,\mathrm{nm}$, that is $2500$ Kuhn segments, or $250\,\mu\mathrm{m}$; but the electrostatic repulsion between strands makes the effective diameter of DNA about $10$–$20\,\mathrm{nm}$ at physiological to low salt ([7.6.6](/7.6.6)), lowering the threshold to a few micrometers, in agreement with the measured scaling $D \propto L^{-0.57}$ of the diffusion coefficient of DNA molecules of $5$–$300\,\mathrm{kb}$ (Robertson, Laib and Smith 2006).

Excluded volume between crowders and a polymer can also shape it. A flexible tube surrounded by small crowders lowers the excluded volume around it by coiling into a helix whose turns are close enough for their depletion zones to overlap; the optimal pitch-to-radius ratio of such a helix is about $2.5$, close to the ratio of $2$ of protein α-helices (Snir and Kamien 2005). The calculation illustrates how simple entropic principles can generate familiar structures; it is not an explanation of the α-helix, whose geometry is set by hydrogen bonds ([7.6.7](/7.6.7)).

### 23.2.6. Crowding at Membranes

The same entropy acts in two dimensions. A channel whose radius changes from $R_{\mathrm{c}}$ to $R_{\mathrm{o}}$ when it opens, in a membrane crowded with other proteins of radius $R_{\mathrm{p}}$ at area concentration $c_A$, removes area from the crowders when it opens. For ideal crowders the free energy of each is $-k_{\mathrm{B}}T\ln(A_{\mathrm{free}}/A_0)$, and expanding to first order in the excluded area gives

$$
\Delta G_{\mathrm{crowd}} \approx c_Ak_{\mathrm{B}}T\left[\pi(R_{\mathrm{o}}^2 - R_{\mathrm{c}}^2) + 2\pi R_{\mathrm{p}}(R_{\mathrm{o}} - R_{\mathrm{c}})\right] = \sigma_{\mathrm{crowd}}\Delta A + \tau_{\mathrm{crowd}}\Delta C, \tag{23.6}
$$
an entropic surface pressure $\sigma_{\mathrm{crowd}} = c_Ak_{\mathrm{B}}T$ opposing the area change $\Delta A$ and a line tension $\tau_{\mathrm{crowd}} = c_AR_{\mathrm{p}}k_{\mathrm{B}}T$ opposing the change $\Delta C$ of the circumference (Lindén, Sens and Phillips 2012). Crowding thus acts on a channel like a negative membrane tension: it favors the closed, smaller state, and tension-gated channels such as MscL ([7.6.4](/7.6.4#sec-4.2), [7.6.25](/7.6.25)) should need a higher tension to open in a crowded membrane. With $c_A = 0.01\,\mathrm{nm^{-2}}$ (one protein per $100\,\mathrm{nm^2}$), $\sigma_{\mathrm{crowd}} = 0.04\,\mathrm{mN\,m^{-1}}$, small compared with the gating tension of MscL of about $10\,\mathrm{mN\,m^{-1}}$; at the densities of real membranes, where the ideal approximation underestimates exclusion severalfold, the effect reaches a few $k_{\mathrm{B}}T$.

## 23.3. Crowded Dynamics

### 23.3.1. Crowding and Reaction Rates

Crowding affects a reaction in two opposite ways. It raises the activity of the reactants (23.2), which accelerates any association whose rate-limiting step is a transition state more compact than the separated reactants. It also slows diffusion (23.3.2), which slows a **diffusion-controlled reaction**, whose rate constant $k_{\mathrm{D}} = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})(R_{\mathrm{A}} + R_{\mathrm{B}})$ is proportional to the diffusion coefficients ([7.6.5](/7.6.5#sec-5.2.3)). As the crowder volume fraction increases, the association rate of a diffusion-limited reaction therefore first rises and then falls, while its equilibrium constant keeps rising; dissociation rates fall. Which effect wins depends on the reaction, and in vitro rates cannot be transferred into cells without measuring.

Cells often bypass diffusion altogether. In **substrate channeling** the enzymes of a pathway form a complex in which an intermediate passes from one active site to the next without equilibrating with the bulk, through a tunnel (tryptophan synthase, carbamoyl phosphate synthetase) or by electrostatic guidance along the surface; it raises the flux through pathways whose free intermediates are too dilute to sustain it, such as oxaloacetate in the citric acid cycle, and protects unstable intermediates. Crowding has a darker side for proteins that are not yet folded: at cellular concentrations, the exposed hydrophobic patches of unfolded chains associate with each other and aggregate. **Molecular chaperones** prevent this, either by binding the patches of nascent chains (Hsp70, which requires ATP to release them) or by enclosing a single chain in a cavity where it can fold alone (the **chaperonin** GroEL–GroES and TRiC/CCT, [7.1](/7.1)).

### 23.3.2. Diffusion Among Obstacles

The simplest model of crowded diffusion is a random walker on a lattice whose sites are occupied by other molecules with probability $\varphi$. At each time step $\tau$ the walker attempts a jump of length $a$ to the left or right, which succeeds only if the target site is empty. Then $p_{\mathrm{right}} = p_{\mathrm{left}} = \frac12(1 - \varphi)$ and $p_{\mathrm{stay}} = \varphi$, so that $\langle x^2(\tau)\rangle = a^2(1 - \varphi)$ and after $t/\tau$ steps

$$
\langle x^2(t)\rangle = \frac{a^2}{\tau}(1 - \varphi)\,t, \qquad D = D_0(1 - \varphi), \tag{23.7}
$$
with $D_0 = a^2/2\tau$ the dilute diffusion coefficient. This mean-field result assumes that the environment is new at every step, as if the crowders rearranged infinitely fast. It underestimates the slowing in two ways. Mobile crowders that have just been passed are likely to block a return step, which correlates successive steps; and when the crowders are immobile (the cytoskeleton, large complexes, the fences of the membrane skeleton), the walker is confined to the connected clusters of free sites. In two dimensions on a square lattice these clusters stop spanning the system when the obstacle fraction reaches $\varphi_{\mathrm{c}} = 1 - 0.593 = 0.407$, the site percolation threshold: the long-time diffusion coefficient vanishes there, and near it the walker explores a fractal cluster on which its MSD grows more slowly than linearly over long times. Measurements of protein diffusion as a function of protein concentration follow the trend of Eq. (23.7) but fall below it, and the hard-sphere theories that account for them are quantitative only for globular proteins without specific interactions (Muramatsu and Minton 1988).

### 23.3.3. Anomalous Diffusion

Single-particle tracking in cells often finds that the MSD does not grow linearly with time.

**Definition 23.3.1 (Anomalous Diffusion)** **Anomalous diffusion** is random motion whose mean squared displacement grows as a power of time different from one, $\langle\Delta x^2(t)\rangle = 2K_\alpha t^\alpha$ with $\alpha \neq 1$ over the range of times considered: subdiffusion for $0 < \alpha < 1$, superdiffusion for $1 < \alpha < 2$. The generalized diffusion coefficient $K_\alpha$ has the unit $\mathrm{m^2\,s^{-\alpha}}$.

Several physically different mechanisms produce subdiffusion with the same exponent, and the exponent alone does not identify them.

| Mechanism | Model | Origin of $\alpha \neq 1$ | Diagnostic |
|---|---|---|---|
| Trapping | continuous-time random walk: jumps separated by waiting times with a heavy-tailed distribution $\psi(t) \propto t^{-1-a}$, $0 < a < 1$ | the mean waiting time is infinite; longer and longer traps are found as time goes on; $\alpha = a$ | time-averaged MSD of single trajectories is linear in the lag but differs from trajectory to trajectory and from the ensemble average (ergodicity breaking); immobile periods |
| Viscoelasticity | fractional Brownian motion: Gaussian increments with long-range anticorrelations, $\langle\Delta x^2\rangle \propto t^{2H}$, Hurst exponent $H < 1/2$ | the elastic medium pushes the particle back (memory of the medium, the generalized Langevin equation with power-law friction) | ergodic; Gaussian displacements; negative velocity autocorrelation |
| Obstruction | random walk on a fractal (percolation cluster near $\varphi_{\mathrm{c}}$) | the accessible space has a fractal dimension | ergodic; non-Gaussian displacements; crossover to normal diffusion away from $\varphi_{\mathrm{c}}$ |
| Polymer connectivity | Rouse motion of a monomer in a chain, $\alpha = 1/2$ (in good solvent about $0.54$) | the monomer drags the chain along ([7.6.21](/7.6.21)) | chromosomal loci: $\alpha \approx 0.4$ |
| Active transport | persistent or directed motion, $\alpha \to 2$ at short times | motors or swimming give velocity memory | ATP depletion abolishes it |

**Example 23.3.1** Single mRNA molecules tagged with many copies of an MS2–GFP fusion move through the cytoplasm of *E. coli* subdiffusively with $\alpha \approx 0.7$ (Golding and Cox 2006), and lipid granules in the fission yeast *Schizosaccharomyces pombe* with $\alpha \approx 0.7$ over many decades of time (Tolić-Nørrelykke and colleagues 2004). Chromosomal loci in bacteria move with $\alpha \approx 0.4$, close to the Rouse value for a polymer in a viscoelastic medium (Weber, Spakowitz and Theriot 2010). The bacterial cytoplasm behaves for particles larger than about $30\,\mathrm{nm}$ like a glass-forming liquid near its glass transition: depleting ATP freezes such particles, while metabolism fluidizes the cytoplasm and keeps them mobile (Parry and colleagues 2014). Small proteins, a few nanometers across, are not caged and diffuse nearly normally, more slowly than in water.

![Anomalous diffusion (simulations). A: ensemble MSD of Brownian motion, fractional Brownian motion with Hurst exponent 0.35 (α = 0.7), a continuous-time random walk with power-law waiting times (exponent a = 0.6) and a persistent random walk (ballistic at short times, diffusive at long times), scaled to agree at lag 100; lines show the expected power laws. B: for the continuous-time random walk, the time-averaged MSDs of individual trajectories (thin lines) are linear in the lag, scatter over orders of magnitude and lie below the subdiffusive ensemble average (thick): weak ergodicity breaking. C: tracer diffusion on a square lattice among immobile obstacles occupying a fraction φ of the sites: the diffusion coefficient after 6000 steps falls faster than the mean-field 1 − φ of Eq. (23.7) and tends to zero at the percolation threshold φ_c = 0.407](./plots/anomalous-msd.py)

The table and the figure contain the practical lesson for analyzing tracking data ([7.6.12](/7.6.12), [7.7](/7.7)): an exponent fitted to an ensemble MSD over one or two decades is a description, not a mechanism. Distinguishing the mechanisms requires the time-averaged MSD of single trajectories, the distribution of displacements, the velocity autocorrelation, and perturbations (ATP depletion, drugs that disrupt the cytoskeleton, changes in particle size).

### 23.3.4. Active Diffusion

Fluctuations in a living cell are not all thermal. Motors such as myosin II pull on the actin network, microtubules polymerize and depolymerize, and vesicles are carried by kinesin and dynein; together they shake the cytoplasm and everything embedded in it with forces that have nothing to do with $k_{\mathrm{B}}T$.

**Definition 23.3.2 (Active Diffusion)** **Active diffusion** is the random motion of particles in a living cell driven by nonequilibrium, energy-consuming processes (motor activity, filament polymerization) rather than by thermal agitation. It is identified by its dependence on ATP and by a violation of the **fluctuation–dissipation theorem**: the fluctuations exceed those predicted from the measured mechanical response of the medium.

A minimal model is a particle held in an elastic network of stiffness $k$ with friction $\gamma$, subject to thermal noise and to an active force $f_{\mathrm{a}}(t)$ from many motors:

$$
\gamma\dot x = -kx + \xi(t) + f_{\mathrm{a}}(t), \qquad \langle\xi(t)\xi(t')\rangle = 2\gamma k_{\mathrm{B}}T\,\delta(t - t'). \tag{23.8}
$$
Without the active force this is the **Ornstein–Uhlenbeck process** of [7.6.5](/7.6.5#sec-5.4.2): the MSD from a stationary start, $\langle\Delta x^2(t)\rangle = (2k_{\mathrm{B}}T/k)(1 - \mathrm{e}^{-t/\tau})$ with $\tau = \gamma/k$, grows diffusively and then saturates. An elastic medium should therefore confine a thermal particle. Yet tracer particles in cells continue to move on long time scales, with an MSD that often grows nearly linearly with time, as if they diffused (Guo and colleagues 2014). The model explains this if the active force itself wanders.

**Formula 23.3.1 (Particle in an Elastic Medium Driven by Active Forces)** Let $f_{\mathrm{a}}$ be stationary with $\langle f_{\mathrm{a}}(t)f_{\mathrm{a}}(t')\rangle = s^2\mathrm{e}^{-\lvert t - t'\rvert/\tau_{\mathrm{a}}}$, the sum of many motors that each act for a time of order $\tau_{\mathrm{a}} \gg \tau$. Then the MSD of the particle in the stationary state is

$$
\langle\Delta x^2(t)\rangle = \frac{2k_{\mathrm{B}}T}{k}\left(1 - \mathrm{e}^{-t/\tau}\right) + \frac{2s^2}{k^2(1 - \lambda^2)}\left[(1 - \lambda) - \mathrm{e}^{-t/\tau_{\mathrm{a}}} + \lambda\,\mathrm{e}^{-t/\tau}\right], \qquad \lambda = \frac{\tau}{\tau_{\mathrm{a}}}.
$$
For $\tau \ll t \ll \tau_{\mathrm{a}}$ the active part is $\approx 2s^2t/(k^2\tau_{\mathrm{a}})$: the particle follows the slowly changing force, whose changes over a time $t$ have variance $2s^2t/\tau_{\mathrm{a}}$, like a random walk. The MSD saturates only for $t \gg \tau_{\mathrm{a}}$, at $2s^2/[k^2(1 + \lambda)]$.

**Proof** Since the equation is linear, the thermal and active contributions add. For the active part, $x_{\mathrm{a}}(t) = \gamma^{-1}\int_{-\infty}^t\mathrm{e}^{-(t - u)/\tau}f_{\mathrm{a}}(u)\,\mathrm{d}u$, and its stationary autocorrelation, evaluated by the double integral over the two exponential kernels (most simply via the spectrum $\lvert\chi(\omega)\rvert^2 \cdot 2s^2\tau_{\mathrm{a}}/(1 + \omega^2\tau_{\mathrm{a}}^2)$ with $\chi = 1/(k - \mathrm{i}\gamma\omega)$), is $C(t) = \frac{s^2}{k^2(1 - \lambda^2)}(\mathrm{e}^{-t/\tau_{\mathrm{a}}} - \lambda\,\mathrm{e}^{-t/\tau})$ for $t \ge 0$. Then $\langle\Delta x_{\mathrm{a}}^2\rangle = 2[C(0) - C(t)]$ gives the stated expression. For $t \ll \tau_{\mathrm{a}}$, $1 - \mathrm{e}^{-t/\tau_{\mathrm{a}}} \approx t/\tau_{\mathrm{a}}$ and, for $t \gg \tau$, the $\mathrm{e}^{-t/\tau}$ term is negligible, which gives the linear regime. $\square$

![A particle in an elastic medium stirred by active forces (Eq. (23.8) and Formula 23.3.1; units γ = k = k_BT = 1, τ = 1, active force correlation time τ_a = 300 and variance 20 k_BT k). A: MSD of passive and active particles (dots: simulation of 200 particles from the stationary state; lines: theory): both diffuse at first; the passive particle saturates at 2k_BT/k, while the active particle's MSD grows nearly linearly between τ and τ_a, mimicking free diffusion with a much smaller coefficient, and saturates beyond τ_a. B: ratio of the fluctuation spectrum of the particle to the value predicted from its response by the fluctuation–dissipation theorem: one for the passive particle, far larger than one at frequencies below 1/τ_a for the active particle](./plots/active-diffusion.py)

The violation of the fluctuation–dissipation theorem is the experimental signature. Active microrheology measures the response function $\chi(\omega)$ by pushing a bead with an optical trap; passive microrheology measures its spontaneous fluctuation spectrum $S_x(\omega)$. In equilibrium the two are linked by $S_x(\omega) = 2k_{\mathrm{B}}T\operatorname{Im}\chi(\omega)/\omega$ ([7.6.5](/7.6.5#def-5.4.2)). In reconstituted actin–myosin networks with ATP and in the cytoplasm of living cells, the fluctuations agree with this prediction above about $10\,\mathrm{Hz}$ and exceed it by orders of magnitude at lower frequencies, where motors dominate (Mizuno, Tardin, Schmidt and MacKintosh 2007); combining the two measurements yields the spectrum of the active forces themselves ("force spectrum microscopy", Guo and colleagues 2014), which is larger in malignant cells than in benign ones. Active diffusion transports large objects that thermal diffusion would leave in place: in mouse oocytes, which lack centrosomes, active diffusion driven by myosin V on actin-coated vesicles creates a gradient of activity that pushes the large nucleus to the center of the cell (Almonacid and colleagues 2015). The energetic cost of such nonequilibrium fluctuations, and the general relations between dissipation and precision, are the subject of [7.6.38](/7.6.38).

## Summary

| Topic | Key result | Reference |
|---|---|---|
| Census | proteins about $7\,\mathrm{nm}$ apart in *E. coli*; $200$–$400\,\mathrm{g\,L^{-1}}$, volume fraction $0.2$–$0.4$; $120\,\mathrm{nm}$ apart at $1\,\mu\mathrm{M}$ in vitro; membranes half protein | 23.1 |
| Lattice model of binding | crowders reduce the free volume; $K_{\mathrm{d}}(\varphi)/K_{\mathrm{d}}(0) = (1 - \varphi)^r$ | Eq. (23.1), Formula 23.2.1 |
| Hard spheres | scaled-particle theory; $K_{\mathrm{d}} \propto \gamma_{\mathrm{AB}}/\gamma_{\mathrm{A}}\gamma_{\mathrm{B}}$; small crowders act more strongly; negligible below $\varphi \approx 0.1$ | Definition 23.2.1, Formula 23.2.2, Eq. (23.2) |
| Osmotic pressure | lattice $-(k_{\mathrm{B}}T/\nu)\ln(1 - c\nu)$; Carnahan–Starling fits hemoglobin; activity coefficient about $200$ in red cells | Eq. (23.3), Formula 23.2.3, Example 23.2.1 |
| Depletion | $W = -\Pi V_{\mathrm{ov}}$; contact $\frac32\varphi(R/r)k_{\mathrm{B}}T$; $15\,k_{\mathrm{B}}T$ and $16\,\mathrm{pN}$ for a $1\,\mu\mathrm{m}$ bead in $1\,\mathrm{mM}$ of $2\,\mathrm{nm}$ crowders; entropic ordering | Definition 23.2.2, Formula 23.2.4, Example 23.2.2 |
| Excluded volume in polymers | $k_{\mathrm{B}}T\varphi$ per molecule; swelling $R \propto N^{3/5}$ for $N > (a/d)^2$; effective DNA diameter set by electrostatics | Eq. (23.5) |
| Crowded membranes | entropic pressure $c_Ak_{\mathrm{B}}T$ and line tension $c_AR_{\mathrm{p}}k_{\mathrm{B}}T$ favor closed channels | Eq. (23.6) |
| Rates | activity raises, slower diffusion lowers association; substrate channeling; chaperones prevent aggregation | 23.3.1 |
| Obstructed diffusion | mean field $D = D_0(1 - \varphi)$; immobile obstacles: $D \to 0$ at percolation ($0.407$ on a square lattice) | Eq. (23.7) |
| Anomalous diffusion | $\langle\Delta x^2\rangle \propto t^\alpha$; trapping (CTRW, nonergodic), viscoelasticity (fBm), obstruction, polymer connectivity, active transport; mRNA in *E. coli* $\alpha \approx 0.7$ | Definition 23.3.1, Example 23.3.1 |
| Active diffusion | wandering motor forces make confined particles move as if diffusing; violation of the fluctuation–dissipation theorem below $10\,\mathrm{Hz}$ | Definition 23.3.2, Formula 23.3.1 |

## Questions

1. Estimate the mean spacing between molecules at $1\,\mathrm{M}$ (the biochemical standard state), $1\,\mathrm{mM}$ and $1\,\mathrm{nM}$, and the concentration that corresponds to one molecule in an *E. coli* cell of $1\,\mu\mathrm{m^3}$.

   **Answer** Number density $n = cN_{\mathrm{A}}$; spacing $n^{-1/3}$. $1\,\mathrm{M}$: $6.0\times10^{26}\,\mathrm{m^{-3}}$, spacing $1.2\,\mathrm{nm}$ (smaller than a protein: a 1 M protein solution is impossible). $1\,\mathrm{mM}$: $12\,\mathrm{nm}$. $1\,\mathrm{nM}$: $1.2\,\mu\mathrm{m}$. One molecule per $1\,\mu\mathrm{m^3} = 10^{-15}\,\mathrm{L}$ is $1/(6.0\times10^{23}\times10^{-15})\,\mathrm{M} = 1.7\,\mathrm{nM}$. Transcription factors present at tens of copies per cell are thus at tens of nanomolar, and in vitro binding assays at micromolar concentrations work at spacings of $120\,\mathrm{nm}$, ten times larger than the spacing of proteins in the cell.

2. In the lattice model with equal sizes (Eq. (23.1)), take $\Omega = 1000$, $\varepsilon_L = -5\,k_{\mathrm{B}}T$ and $L = 10$. Compute $p_{\mathrm{bound}}$ without crowders and with $C = 500$ crowders. Why does the effect depend so weakly on $C$ when crowders and ligands are the same size, compared with Formula 23.2.1 for large ligands?

   **Answer** $\mathrm{e}^{-5} = 6.74\times10^{-3}$. $C = 0$: $(990/10) \times 6.74\times10^{-3} = 0.667$, $p = 1/1.667 = 0.60$. $C = 500$: $(490/10) \times 6.74\times10^{-3} = 0.330$, $p = 0.75$. For equal sizes, crowders only reduce the free volume, a factor $1 - \varphi$ in the effective concentration. A ligand that is $r$ times larger than a crowder must find $r$ adjacent free small cells, a probability $(1 - \varphi)^r$: excluded volume is cooperative in the size ratio, which is why crowding by small molecules has large effects on the binding of large ones.

3. Show from Formula 23.2.3 that the second virial coefficient of hard spheres is $B_2 = 4V$ (per molecule) and explain the factor of four.

   **Answer** Expanding, $\Pi/ck_{\mathrm{B}}T = 1 + 4\varphi + \cdots = 1 + 4Vc + \cdots$, so $B_2 = 4V$. In general $B_2 = \frac12\int(1 - \mathrm{e}^{-\beta u(r)})\,\mathrm{d}^3r$, and for hard spheres of diameter $\sigma$ the integrand is one inside the excluded sphere of radius $\sigma$, so $B_2 = \frac12\cdot\frac43\pi\sigma^3 = \frac12 \times 8V = 4V$: the excluded volume of a pair is eight times the volume of one sphere (radius doubled), and the factor $\frac12$ avoids counting each pair twice.

4. Compute the depletion force between a sphere of radius $R$ and a flat wall in a solution of crowders of radius $r$ at number density $n$, and compare it with the force between two spheres (Formula 23.2.4). Estimate it for two beads of $1\,\mu\mathrm{m}$ radius in a protein solution at the concentration of the *E. coli* cytoplasm ($3\times10^6$ proteins per $\mu\mathrm{m^3}$, $r = 3\,\mathrm{nm}$).

   **Answer** The wall's depletion layer is a slab of thickness $r$; at a gap $h < 2r$ between sphere surface and wall, the overlap is a single cap of the sphere of radius $R + r$ cut by the plane at distance $r$ from the wall, of height $2r - h$: $V_{\mathrm{ov}} = \frac{\pi}{3}(2r - h)^2[3(R + r) - (2r - h)] \approx \pi R(2r - h)^2$ for $R \gg r$, and $F = -\mathrm{d}(\Pi V_{\mathrm{ov}})/\mathrm{d}h \approx 2\pi\Pi R(2r - h)$, twice the sphere–sphere force at the same gap (the wall is a sphere of infinite radius; the Derjaguin approximation gives a factor $2$). For two beads in cytoplasm-like crowding, $n = 3\times10^{24}\,\mathrm{m^{-3}}$, $\Pi = nk_{\mathrm{B}}T = 1.2\times10^4\,\mathrm{Pa}$ (ideal; the real value is several times larger, Formula 23.2.3), and at $h = r$ the force is $\pi\Pi Rr = \pi \times 1.2\times10^4 \times 10^{-6} \times 3\times10^{-9}\,\mathrm{N} \approx 120\,\mathrm{pN}$, with a contact energy $2\pi Rr^2\Pi \approx 170\,k_{\mathrm{B}}T$. Such numbers suggest that large structures in the cytoplasm would stick irreversibly unless repulsive interactions (charge, polymer brushes) kept them apart, as they do.

5. Repeat the Flory argument (23.2.5) for a polymer confined to two dimensions, such as DNA adsorbed on a lipid bilayer, and find the exponent $\nu$ in $R \propto N^\nu$. Is self-avoidance more or less important in two dimensions?

   **Answer** In two dimensions the entropic term is $k_{\mathrm{B}}TR^2/Na^2$ (up to a constant) and the excluded-volume term is $k_{\mathrm{B}}TN^2v/R^2$ with $v \sim ad$ an excluded area. Minimizing $R^2/Na^2 + N^2ad/R^2$ gives $R^4 \propto N^3a^3d$, so $R \propto N^{3/4}$, $\nu = 3/4$ (exact in two dimensions). The criterion for swelling, comparing the two terms at $R^2 = Na^2$, is $N^2ad/(Na^2) = Nd/a > 1$, so $N > a/d$ instead of $(a/d)^2$: for DNA, $N > 50$ Kuhn segments, a few micrometers even for bare DNA. Self-avoidance is more important in two dimensions because the chain meets itself more often; in Flory's general formula $\nu = 3/(d + 2)$, which gives $3/4$, $3/5$ and $1/2$ for $d = 2$, $3$ and $4$.

6. A tracer protein is followed by FRAP in a cell and in buffer containing $30\,\%$ (by volume) of an inert crowder; in both cases the recovery is slower than in water by a factor of four. How would you decide whether the slowing in the cell comes from crowding, binding to immobile structures, or higher fluid-phase viscosity?

   **Answer** Measure the rotational mobility, for instance by time-resolved fluorescence anisotropy of the tracer ([7.6.11](/7.6.11)): rotation is sensitive to the local (fluid-phase) viscosity but much less to obstruction by distant crowders, so a normal rotational correlation time with slowed translation indicates crowding or obstruction rather than viscosity. Binding to immobile structures produces a FRAP curve with an immobile fraction or two components and a recovery rate that depends on the size of the bleached spot differently from diffusion (reaction-dominated recovery is independent of spot size, diffusive recovery scales with its area); fluorescence correlation spectroscopy and single-particle tracking show bound and free populations directly ([7.6.12](/7.6.12)). Comparing tracers of different sizes distinguishes obstruction (strongly size-dependent above the mesh size) from viscosity (Stokes–Einstein scaling, $D \propto 1/R$).

7. In Formula 23.3.1, take $k = 10^{-5}\,\mathrm{N\,m^{-1}}$ (a bead in a network of shear modulus about $10\,\mathrm{Pa}$), $\gamma = 10^{-8}\,\mathrm{N\,s\,m^{-1}}$, $\tau_{\mathrm{a}} = 1\,\mathrm{s}$ and an active force of root-mean-square $s = 1\,\mathrm{pN}$. Compute the thermal plateau, the active MSD at $t = 0.1\,\mathrm{s}$ and the long-time plateau. Which dominates, and at what time scales?

   **Answer** $\tau = \gamma/k = 1\,\mathrm{ms}$, $\lambda = 10^{-3}$. Thermal plateau $2k_{\mathrm{B}}T/k = 2 \times 4.1\times10^{-21}/10^{-5} = 8.2\times10^{-16}\,\mathrm{m^2} = 8.2\times10^{-4}\,\mu\mathrm{m^2}$ (an rms displacement of $29\,\mathrm{nm}$). Active part at $0.1\,\mathrm{s}$: $\approx 2s^2t/(k^2\tau_{\mathrm{a}}) = 2 \times 10^{-24} \times 0.1/10^{-10}\,\mathrm{m^2} = 2\times10^{-15}\,\mathrm{m^2} = 2\times10^{-3}\,\mu\mathrm{m^2}$, already larger than the thermal plateau. Long-time plateau $2s^2/k^2 = 2\times10^{-14}\,\mathrm{m^2} = 0.02\,\mu\mathrm{m^2}$ ($140\,\mathrm{nm}$ rms). Thermal motion dominates below about $40\,\mathrm{ms}$ (where the two contributions are equal), active motion above: the apparent diffusion coefficient in the linear regime is $s^2/(k^2\tau_{\mathrm{a}}) = 10^{-14}\,\mathrm{m^2\,s^{-1}} = 0.01\,\mu\mathrm{m^2\,s^{-1}}$, far below the Stokes–Einstein value in water.

8. (Experimental design) How would you demonstrate that the motion of ribosome-sized particles in the cytoplasm of a bacterium depends on metabolism? What controls are needed to rule out simple changes of cell volume or ionic strength?

   **Answer** Express or introduce tracer particles of defined size (for example genetically encoded multimeric nanoparticles of $20$–$50\,\mathrm{nm}$, or fluorescent protein–tagged large complexes) and track them before and after depleting ATP (2,4-dinitrophenol or carbonyl cyanide m-chlorophenylhydrazone, or glucose removal in a sugar-dependent strain), measuring the MSD exponent and the time-averaged MSD distributions. Controls: measure cell volume (phase contrast and membrane stain) and use osmotic adjustments to show that the change is not due to shrinkage and the resulting increase of crowding; follow small tracers (GFP) that should be little affected; check that ionic strength and pH are maintained or vary them deliberately; and restore metabolism to show reversibility. The experiment of Parry and colleagues found that large particles become nearly immobile after ATP depletion while small ones do not.

9. A lattice model gave $r = 45$ for the T4 proteins in PEG 12000, three times the mass ratio. Give two physical reasons why a flexible polymer crowder can be more effective, per unit mass, than a compact one, and one reason why it can be less effective in a cell.

   **Answer** A flexible polymer coil occupies a much larger volume (its radius of gyration, about $4\,\mathrm{nm}$ for PEG 12000) than its mass and density suggest, and its excluded volume for a compact protein is set by the coil size; moreover, a polymer solution's osmotic pressure rises faster than linearly with concentration once coils overlap. Both raise the effective $r$. In a cell, crowders are mostly proteins and nucleic acids with charged and sticky surfaces; weak attractive interactions between crowders and the reactants partly cancel the hard-core excluded-volume effect, and crowding by large, compact macromolecules at the same volume fraction is weaker than by small ones (Formula 23.2.2).

10. (Open question) Consider an enzyme whose substrate must diffuse to it. Using the competing effects in 23.3.1, discuss whether crowding should increase or decrease the turnover rate at substrate concentrations far below $K_{\mathrm{M}}$, distinguishing enzymes near the diffusion limit from slow ones.

    **Answer** Far below $K_{\mathrm{M}}$ the rate is $k_{\mathrm{cat}}/K_{\mathrm{M}}$ times the concentrations, and $k_{\mathrm{cat}}/K_{\mathrm{M}}$ is bounded by the encounter rate. For a diffusion-limited enzyme (such as catalase, triose phosphate isomerase or acetylcholinesterase), $k_{\mathrm{cat}}/K_{\mathrm{M}} \approx k_{\mathrm{D}} \propto D$, and crowding lowers the rate roughly in proportion to the slowing of diffusion of the larger of the partners (for small substrates, little). For a slow enzyme whose rate-limiting step is a chemical or conformational step from a compact enzyme–substrate complex, crowding raises the activity of the enzyme and favors compact conformations, and can raise $k_{\mathrm{cat}}/K_{\mathrm{M}}$ modestly. Large effects are expected only for large substrates (macromolecules, assembly reactions) and at high crowder volume fractions; channeling and compartmentalization (23.3.1, [7.6.29](/7.6.29)) can change the picture entirely.
