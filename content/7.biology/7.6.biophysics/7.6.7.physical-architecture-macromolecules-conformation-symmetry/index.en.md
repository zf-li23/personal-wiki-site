---
title: "The Physical Architecture of Macromolecules: Conformation, Symmetry and Assembly"
description: The physics and geometry behind macromolecular structure. A hierarchy of stiff and soft degrees of freedom; the peptide group and prolyl isomerization; a soft-potential Ramachandran map and conformational entropy; sugar pucker; every repeat is a screw (Chasles) and the helix parameters computed from (φ, ψ); the α helix macrodipole and the coiled-coil supercoil; base-pair step parameters and the A, B and Z duplexes; counterions and RNA architecture; the finite rotation groups C_n, D_n, T, O, I and helical symmetry; icosahedral capsids, quasi-equivalence and the Caspar–Klug triangulation number T = h² + hk + k²; size–mass scaling of assemblies.
---

The structures of proteins and nucleic acids have already been described in biochemical terms: amino acids, the planar peptide group, the α helix and β sheet, the double helix and the nucleosome ([7.1.5](/7.1.5), [7.1.11](/7.1.11), [7.2.4](/7.2.4)). This chapter asks the physicist's questions about the same objects. Which degrees of freedom of a chain are actually free at $k_{\mathrm{B}}T$, and how much entropy do they carry? Why does the repetition of one local conformation always produce a helix, and how are its parameters computed? Why are the double helices of DNA and RNA wider or narrower, right- or left-handed? And why do assemblies of identical subunits have only a few kinds of symmetry, among which icosahedral shells obey a simple counting law? The answers are geometry (rigid motions, rotation groups, Euler's formula) and statistical mechanics (Boltzmann weights over conformations), and they are the vocabulary of the structural methods that follow: crystallography uses point groups and helical symmetry ([7.6.12](/7.6.12)), cryo-electron microscopy reconstructs icosahedral and helical assemblies ([7.6.20](/7.6.20)), and the conformational entropy introduced here is the main opponent of folding ([7.6.22](/7.6.22)). The energies of the noncovalent interactions themselves are the subject of [7.6.6](/7.6.6).

## 7.1. Conformational Degrees of Freedom

### 7.1.1. A Hierarchy of Stiffness

A macromolecule of $N$ atoms has $3N - 6$ internal coordinates, but they are far from equally soft. In a molecular-mechanics description ([7.6.21](/7.6.21)) bond lengths $b$, bond angles $\theta$ and torsions $\tau$ have energies

$$
E = \sum_{\text{bonds}} k_b (b - b_0)^2 + \sum_{\text{angles}} k_\theta (\theta - \theta_0)^2 + \sum_{\text{torsions}} \frac{V_n}{2}\bigl[1 + \cos(n\tau - \delta)\bigr] + E_{\text{nonbonded}},
$$
with typical force constants $k_b \approx 300\,\mathrm{kcal\,mol^{-1}\,\text{Å}^{-2}}$ for a C–C bond, $k_\theta \approx 60\,\mathrm{kcal\,mol^{-1}\,rad^{-2}}$, and torsional barriers $V_n$ of only $1$–$3\,\mathrm{kcal\,mol^{-1}}$ ($4$–$12\,\mathrm{kJ\,mol^{-1}}$) about single bonds. By the **equipartition theorem** each quadratic coordinate fluctuates with $\langle\delta q^2\rangle = k_{\mathrm{B}}T/\kappa$, where $\kappa = 2k$ is the second derivative of the energy.

**Example 7.1.1** For a C–C bond $\kappa = 620\,\mathrm{kcal\,mol^{-1}\,\text{Å}^{-2}} = 431\,\mathrm{N\,m^{-1}}$, so at $298\,\mathrm{K}$ the root-mean-square fluctuation is $\sqrt{k_{\mathrm{B}}T/\kappa} = \sqrt{4.11\times10^{-21}/431}\,\mathrm{m} = 0.031\,\text{Å}$, two percent of the bond length. A bond angle with $\kappa = 126\,\mathrm{kcal\,mol^{-1}\,rad^{-2}}$ fluctuates by $0.069\,\mathrm{rad} = 3.9^\circ$. A torsion with a barrier of $3\,\mathrm{kcal\,mol^{-1}} \approx 5k_{\mathrm{B}}T$, by contrast, explores a whole well $\pm 30^\circ$ wide and hops between wells on a nanosecond time scale.

The conformations of a macromolecule are therefore, to a good approximation, the values of its torsion angles at fixed bond lengths and angles. This separation of stiff and soft coordinates is what makes the Ramachandran description of proteins and the six-torsion description of nucleic acids possible, and it is also the reason why molecular dynamics needs femtosecond time steps (to follow bond vibrations) while the interesting motions are millions of times slower.

### 7.1.2. The Peptide Group and Its Two Torsions

Resonance gives the C–N bond of the **peptide bond** about $40\,\%$ double-bond character ([7.1.5](/7.1.5#sec-5.1.3)): the six atoms $\mathrm{C}_\alpha$, C, O, N, H, $\mathrm{C}_\alpha$ are coplanar and the torsion $\omega$ is close to $180^\circ$ (trans) or, rarely, $0^\circ$ (cis). Each residue then has two soft backbone torsions, $\varphi$ about N–$\mathrm{C}_\alpha$ and $\psi$ about $\mathrm{C}_\alpha$–C (the **torsion angles** that define the **Ramachandran plot**). The barrier to rotation about the peptide bond is about $80$–$90\,\mathrm{kJ\,mol^{-1}}$. For an ordinary peptide the cis form lies about $10\,\mathrm{kJ\,mol^{-1}}$ above the trans form and is populated at the level of $0.1$–$0.5\,\%$; when the following residue is proline both forms put a carbon next to the preceding $\mathrm{C}_\alpha$, the difference shrinks to a few kJ/mol, and $5$–$30\,\%$ of X–Pro bonds are cis in unfolded chains.

**Example 7.1.2** By the **Eyring equation** ([6.3.16](/6.3.16#sec-16.3.1)), a barrier $\Delta G^\ddagger = 85\,\mathrm{kJ\,mol^{-1}}$ gives $k = (k_{\mathrm{B}}T/h)\,\mathrm{e}^{-\Delta G^\ddagger/RT} = 6.2\times10^{12}\,\mathrm{s^{-1}} \times \mathrm{e}^{-34.3} = 8\times10^{-3}\,\mathrm{s^{-1}}$ at $25\,^\circ\mathrm{C}$, a time constant of about two minutes ($32\,\mathrm{s}$ at $37\,^\circ\mathrm{C}$). Prolyl cis–trans isomerization is therefore one of the slowest elementary steps a polypeptide can undergo: it causes the slow phases seen in the refolding of many proteins, and cells accelerate it with prolyl isomerases ([7.1.6](/7.1.6#sec-6.4.3)).

### 7.1.3. From Hard Spheres to an Energy Map

The Ramachandran map of [7.1.5](/7.1.5#sec-5.2.5) treats atoms as hard spheres: a conformation is allowed or forbidden. A physical description replaces the yes/no test by an energy and the energy by a probability. Summing a pair potential over all atom pairs whose distance depends on $(\varphi, \psi)$ gives a conformational energy $E(\varphi, \psi)$, and the residue samples the torus of angles with the **Boltzmann distribution**.

**Formula 7.1.1 (Conformational Energy Map)** For a residue with fixed bond geometry,

$$
E(\varphi,\psi) = \sum_{i<j} \left\{ \varepsilon_{ij}\left[\left(\frac{r^{\min}_{ij}}{r_{ij}}\right)^{12} - 2\left(\frac{r^{\min}_{ij}}{r_{ij}}\right)^{6}\right] + \frac{q_i q_j}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}} r_{ij}} \right\} + E_{\mathrm{tors}}(\varphi,\psi), \qquad
p(\varphi,\psi) = \frac{\mathrm{e}^{-E(\varphi,\psi)/k_{\mathrm{B}}T}}{\displaystyle\iint \mathrm{e}^{-E/k_{\mathrm{B}}T}\,\mathrm{d}\varphi\,\mathrm{d}\psi},
$$
where the sum runs over pairs separated by at least three bonds, $r_{ij}(\varphi,\psi)$ is their distance, $r^{\min}_{ij}$ and $\varepsilon_{ij}$ are the position and depth of the Lennard-Jones minimum, and $q_i$ are partial charges screened by a dielectric constant $\varepsilon_{\mathrm{r}}$.

The steep $r^{-12}$ wall reproduces the hard-sphere boundary; the shallow $r^{-6}$ well and the electrostatic term add the shape of the energy inside the allowed regions.

![A soft-potential Ramachandran map computed from scratch for the blocked residue acetyl-X-N-methylamide (standard geometry, trans peptides, 3° grid; Lennard-Jones 12-6 with AMBER-like radii and well depths, united-atom methyls; Coulomb interactions between peptide partial charges with dielectric constant 4; no intrinsic torsion term). A: energy of L-Ala relative to its minimum, with the 2 kcal/mol contour (black line); the β/polyproline II basin is lowest, the right-handed α region is about 2 kcal/mol higher, the left-handed α region about 6 kcal/mol higher. Points: ideal conformations. B: the Boltzmann probability at 298 K on a logarithmic scale; in this solvent-free model 93 % of the population is in the β and polyproline II region, 7 % in the α region and less than 0.1 % at positive φ. C: glycine, whose second α hydrogen replaces Cβ; its map is centrosymmetric, (φ, ψ) → (−φ, −ψ), and the regions with positive φ are open. D: the effective accessible fraction of the torus, exp(S/k_B)/N for the Boltzmann distribution over the N grid cells: 0.08 for Ala and 0.31 for Gly, a difference in conformational entropy of 10.8 J/(mol K)](./plots/ramachandran-energy.py)

The map makes the amount of freedom of a residue a number. The natural measure is the Gibbs entropy of the distribution $p(\varphi, \psi)$.

**Definition 7.1.1 (Conformational Entropy)** The **conformational entropy** of a molecule is the entropy associated with the distribution of its conformations,

$$
S_{\mathrm{conf}} = -k_{\mathrm{B}} \sum_c p_c \ln p_c ,
$$
where $p_c$ is the equilibrium probability of conformation $c$ (for continuous coordinates, of a cell of fixed size on the conformational torus). Only differences of $S_{\mathrm{conf}}$ between states of the same molecule are independent of the cell size.

If the probability were spread uniformly over $W$ of $N$ cells, $S_{\mathrm{conf}} = k_{\mathrm{B}}\ln W$ (the **Boltzmann entropy formula**); for any distribution $\mathrm{e}^{S_{\mathrm{conf}}/k_{\mathrm{B}}}$ is the effective number of accessible cells, and its ratio to $N$ is the accessible fraction plotted in panel D.

**Example 7.1.3** In the model of the figure the accessible fraction is $f_{\mathrm{Ala}} = 0.084$ and $f_{\mathrm{Gly}} = 0.31$. Fixing a residue in one conformation (as in a helix) therefore costs glycine more entropy than alanine, by $\Delta S = R\ln(f_{\mathrm{Gly}}/f_{\mathrm{Ala}}) = 10.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$, or $T\Delta S = 3.2\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$. The measured difference in helix propensity between Gly and Ala is about $4\,\mathrm{kJ\,mol^{-1}}$, of the same size; this is why Ala is the strongest helix former and Gly a helix breaker. Per residue, the unfolded chain of a protein retains roughly $R\ln(0.1 \times 3600) \approx 50\,\mathrm{J\,mol^{-1}\,K^{-1}}$ relative to a single $6^\circ \times 6^\circ$ cell of a folded residue; with backbone and side chains together, a typical estimate is $T\Delta S_{\mathrm{conf}} \approx 5$–$10\,\mathrm{kJ\,mol^{-1}}$ per residue at room temperature, which a folded protein must repay with its enthalpy and the **hydrophobic effect** (and the reason why the net stability is small, [7.6.8](/7.6.8)).

The model is deliberately crude: without water it overweights conformations with internal hydrogen bonds, and real residues in proteins populate the α region far more than panel B suggests, because a helix is stabilized cooperatively by the hydrogen bonds between residues $i$ and $i+4$, not by local energy. Its value is that it shows which part of the Ramachandran plot is set by sterics (the forbidden regions are the same as with hard spheres), and how an energy landscape becomes a probability and an entropy.

### 7.1.4. The Nucleic Acid Backbone

A nucleotide has six backbone torsions ($\alpha$ to $\zeta$, along P–O5′–C5′–C4′–C3′–O3′–P), the glycosidic torsion $\chi$ (anti or syn) and the five endocyclic torsions $\nu_0$–$\nu_4$ of the furanose ring. The ring cannot be flat, and its five torsions are not independent: they are well described by two numbers.

**Formula 7.1.2 (Pseudorotation)** The endocyclic torsions of a furanose ring are

$$
\nu_j = \nu_{\max}\cos\!\left(P + \frac{4\pi(j-2)}{5}\right), \qquad j = 0, 1, \dots, 4,
$$
with puckering amplitude $\nu_{\max} \approx 35$–$40^\circ$ and phase angle $P$; the C3′-endo (N-type) pucker has $P \approx 0$–$36^\circ$, the C2′-endo (S-type) pucker $P \approx 144$–$180^\circ$.

Moving through $P$ (**pseudorotation**) costs only a few kJ/mol, so sugars interconvert between N and S on a picosecond-to-nanosecond time scale, but the pucker sets a long distance: the two phosphates of one nucleotide are about $5.9\,\text{Å}$ apart with C3′-endo and $7.0\,\text{Å}$ apart with C2′-endo. This one number decides the family of the double helix (§7.3.2): C2′-endo gives the long rise of **B-DNA**, C3′-endo the short rise of **A-DNA** and of RNA, whose 2′-OH sterically disfavors C2′-endo.

## 7.2. Helices from Repetition

### 7.2.1. Every Repeat Is a Screw

A regular secondary structure is a chain in which every residue has the same $(\varphi, \psi)$. The geometric consequence is general: the rigid motion that carries residue $i$ onto residue $i+1$ is the same for every $i$, and every rigid motion of space is a screw.

**Theorem 7.2.1 (Chasles)** Every proper rigid motion $\boldsymbol{x} \mapsto R\boldsymbol{x} + \boldsymbol{t}$ of three-dimensional space ($R \in \operatorname{SO}(3)$) is a screw motion: a rotation by some angle $\theta$ about some line combined with a translation $d$ along the same line. If $R \ne I$, then $\cos\theta = (\operatorname{tr} R - 1)/2$, the line is parallel to the rotation axis $\boldsymbol{u}$ of $R$, and $d = \boldsymbol{t}\cdot\boldsymbol{u}$.

**Proof** A rotation $R \ne I$ has a unique axis $\boldsymbol{u}$ ($R\boldsymbol{u} = \boldsymbol{u}$) and acts on the plane perpendicular to $\boldsymbol{u}$ as a rotation by $\theta \ne 0$, so $\operatorname{tr} R = 1 + 2\cos\theta$. Write $\boldsymbol{t} = d\boldsymbol{u} + \boldsymbol{t}_\perp$. On the perpendicular plane $I - R$ is invertible, so there is a point $\boldsymbol{c}_\perp$ in that plane with $(I - R)\boldsymbol{c}_\perp = \boldsymbol{t}_\perp$. Then $R\boldsymbol{x} + \boldsymbol{t} = R(\boldsymbol{x} - \boldsymbol{c}_\perp) + \boldsymbol{c}_\perp + d\boldsymbol{u}$: a rotation about the line through $\boldsymbol{c}_\perp$ parallel to $\boldsymbol{u}$, followed by the translation $d\boldsymbol{u}$ along it. $\square$

Applying the same screw again and again to a residue generates a helix with $n = 360^\circ/\theta$ residues per turn, rise $d$ per residue and pitch $p = \lvert n\rvert d$; the helix is right-handed when the rotation and the translation have the same sense. Two special cases are not helices in the usual sense: $\theta = 180^\circ$ ($n = 2$) gives a flat zigzag ribbon, the β strand, and $\theta = 0$ a straight line.

**Algorithm 7.2.1 (Helix Parameters from Backbone Torsions)** Input: $(\varphi, \psi, \omega)$ and standard bond lengths and angles.

1. Build a few residues of backbone N, $\mathrm{C}_\alpha$, C atoms with the given torsions (each new atom is placed from the previous three by its bond length, bond angle and torsion).
2. Find the rotation $R$ and translation $\boldsymbol{t}$ that superimpose the three atoms of residue $i$ on those of residue $i+1$ (least squares, the Kabsch algorithm via a singular value decomposition, [2.1](/2.1)).
3. Compute $\theta$, $\boldsymbol{u}$ and $d$ by Theorem 7.2.1; orient $\boldsymbol{u}$ so that $d > 0$, and give $\theta$ the sign of the rotation about this $\boldsymbol{u}$.
4. Output $n = 360^\circ/\theta$ (positive: right-handed), $d$, $p = \lvert n\rvert d$ and the radius of the $\mathrm{C}_\alpha$ atoms about the axis.

![Helices generated by repeating one backbone conformation, computed with Algorithm 7.2.1 (standard geometry, trans peptides). A: Cα traces about 2.4 nm long, viewed perpendicular to the computed helix axis (dotted), for the α helix, the 3₁₀ helix, the π helix, polyproline II and the β strand; darker segments are nearer the viewer. B: helical net of the α helix: the cylinder through the Cα atoms is cut along a line parallel to the axis and unrolled; with 3.62 residues per turn, residues i, i+3, i+4 and i+7 lie on the same face, and the i → i+4 lines follow the backbone hydrogen bonds. C: parameters computed by the algorithm: residues per turn n (positive for right-handed, negative for left-handed), rise per residue d, pitch p and radius of the Cα atoms](./plots/helix-geometry.py)

The computed parameters agree with the measured ones within the accuracy of the ideal $(\varphi,\psi)$ values: $3.6$ residues and $5.4$–$5.6\,\text{Å}$ per turn for the α helix, $3.0$ for the $3_{10}$ helix, a left-handed threefold helix with a long rise ($3.1\,\text{Å}$ per residue) for polyproline II. The algorithm also explains why only a few helices occur. Most of the $(\varphi,\psi)$ plane generates helices whose atoms collide with those of the next turn (when $d$ is small and $r$ large) or that leave the backbone NH and CO groups without partners. The α helix sits at the special point where the turn is tight enough that the C=O of residue $i$ meets the N–H of residue $i+4$ at hydrogen-bonding distance, with the N–H⋯O nearly linear, while the side chains point outward and backward without colliding.

### 7.2.2. The α Helix as a Physical Object

**Example 7.2.1** Each peptide group carries an **electric dipole moment** of about $3.5\,\mathrm{D}$ ($1.17\times10^{-29}\,\mathrm{C\,m}$), and in an α helix all of them point nearly along the axis, from C- to N-terminus. A row of dipoles $p$ spaced $d = 1.5\,\text{Å}$ apart is equivalent, far from its ends, to a charge $\pm p/d$ at each end: $p/d = 7.8\times10^{-20}\,\mathrm{C} \approx 0.49\,e$. A helix thus behaves as if it carried about half an elementary charge of positive sign at its N-terminus and of negative sign at its C-terminus. This helix macrodipole is why phosphate groups and other anions are often bound at the N-termini of helices (in nucleotide-binding P-loops, in the selectivity filter of potassium channels, [7.6.27](/7.6.27)), and why acidic residues near the N-terminus and basic residues near the C-terminus stabilize isolated helices. In water and inside proteins the field is screened, and the effect is worth a few kJ/mol rather than the tens suggested by vacuum electrostatics.

The non-integer number of residues per turn has a geometric consequence for helices that pack against each other. In a **coiled coil** the hydrophobic residues occupy positions $a$ and $d$ of a heptad repeat ([7.1.5](/7.1.5#sec-5.3.2)), and seven residues of a straight α helix rotate by $7 \times 100^\circ = 700^\circ$, $20^\circ$ short of two turns. The stripe of $a$ and $d$ residues therefore winds slowly around the helix in a left-handed sense, and two helices can keep their stripes in contact only by winding around each other.

**Example 7.2.2** The stripe advances $-20^\circ$ per heptad, so it returns to the same azimuth after $360/20 = 18$ heptads, $126$ residues, or $126 \times 0.15\,\text{nm} \approx 19\,\mathrm{nm}$ along the axis. This is the order of magnitude of the supercoil pitch of natural two-stranded coiled coils ($14$–$20\,\mathrm{nm}$); the helices also unwind slightly, to about $3.5$ residues per turn, which is why the supercoil is tighter than the estimate. Francis Crick derived the complete parametrization of coiled coils from this argument in 1953, before any protein structure was known.

### 7.2.3. Sheets and Polyproline Helices

A β strand is a twofold screw, so a perfectly flat sheet is possible in principle. Real strands lie near, not at, $n = 2$: their small residual rotation gives β strands a right-handed twist when viewed along the strand direction, and neighboring strands in a sheet are inclined to each other by about $-20^\circ$. The polyproline II helix, with $n = -3$ and $3.1\,\text{Å}$ rise, has no internal hydrogen bonds at all; its backbone groups bind water or the partner proteins of proline-rich motifs (SH3 domains), and three PPII-like chains wound together into a right-handed superhelix make **collagen**.

## 7.3. Double Helices of Nucleic Acids

### 7.3.1. Base-Pair Step Parameters

In nucleic acids the natural rigid units are base pairs, not nucleotides. The relative position of two successive base pairs is a rigid motion with six parameters: three translations (shift, slide, rise) and three rotations (tilt, roll, twist), defined in a standard reference frame attached to each base pair (the Cambridge convention of 1989). Six further parameters describe the two bases within a pair (shear, stretch, stagger, buckle, propeller, opening). A regular duplex is again a screw (Theorem 7.2.1): its helical twist and helical rise are the rotation and translation of the screw that carries one base pair to the next, and two further parameters, the x-displacement and the inclination, locate each base pair relative to the helix axis.

**Formula 7.3.1 (Helical Repeat)** A duplex with helical twist $\Omega$ per base-pair step and helical rise $h$ has

$$
n = \frac{360^\circ}{\Omega} \ \text{bp per turn}, \qquad p = n h, \qquad L = N h \ \text{for } N \text{ bp};
$$
for B-DNA in solution $\Omega \approx 34.3^\circ$, $n \approx 10.5$, $h = 0.338\,\mathrm{nm}$, $p \approx 3.5\,\mathrm{nm}$.

The fiber diffraction patterns from which the double helix was deduced gave $10$ bp per turn, the value of the 1953 model. Two solution measurements in 1979–1980 gave $10.4$–$10.6$: Daniela Rhodes and Aaron Klug cut DNA adsorbed on a surface with DNase I, which can reach only the exposed side and therefore cleaves with the helical period, and James Wang measured the shift of topoisomer bands on gels when short segments were inserted into a circular DNA. The difference matters: over the $147\,\mathrm{bp}$ of a nucleosome, $10.0$ and $10.5$ bp per turn differ by $0.7$ turns, which is the order of the twist changes behind the **linking number** paradox of chromatin ([7.2.3](/7.2.3), [7.2.4](/7.2.4)).

### 7.3.2. The A, B and Z Families

Real sequences deviate from these averages by several degrees per step (sequence-dependent twist, roll and propeller, the basis of the indirect readout of DNA by proteins, [7.6.25](/7.6.25)), but they fall into three families with different sugar puckers and very different shapes ([7.1.11](/7.1.11#sec-11.3.2)).

| Parameter | A-DNA (and A-RNA) | B-DNA | Z-DNA |
|---|---|---|---|
| Handedness | right | right | left |
| Repeating unit | 1 bp | 1 bp | 2 bp (CpG / GpC) |
| Twist per step | $32.7^\circ$ | $34.3^\circ$ ($36^\circ$ in fibers) | $-9^\circ$ / $-51^\circ$ |
| bp per turn | $11$ | $10.5$ | $12$ |
| Rise per bp | $0.26$–$0.29\,\mathrm{nm}$ | $0.338\,\mathrm{nm}$ | $0.37\,\mathrm{nm}$ |
| Pitch | $2.8$–$3.2\,\mathrm{nm}$ | $3.5\,\mathrm{nm}$ | $4.5\,\mathrm{nm}$ |
| x-displacement | $-4.5\,\text{Å}$ (toward the minor groove) | $\approx 0$ | $+3\,\text{Å}$ |
| Inclination of base pairs | $+20^\circ$ | $-6^\circ$ | $-6^\circ$ |
| Sugar pucker | C3′-endo | C2′-endo | alternating C2′-endo (C) / C3′-endo (G, syn) |
| **Major groove** / **minor groove** | narrow and deep / wide and shallow | wide / narrow, both of similar depth | flat / narrow and deep |
| Diameter | $2.3$–$2.6\,\mathrm{nm}$ | $2.0$–$2.4\,\mathrm{nm}$ | $1.8\,\mathrm{nm}$ |

![A, B and Z duplexes built only from their helical parameters (twist, rise, x-displacement and inclination in the table): each base pair is drawn as a rod 10.5 Å long, the C1′–C1′ distance. Top: one helical turn viewed down the axis (cross: helix axis; dashed circle: radius of the phosphates, about 9 Å; darker rods nearer the viewer). In B-DNA the base pairs cross the axis; in A-DNA they are displaced by 4.5 Å toward the minor groove and leave a hole of about 1 nm along the axis; in Z-DNA the twist alternates between the CpG and GpC steps and the dinucleotide is the repeating unit. Bottom: one turn viewed from the side, showing the strong inclination of the base pairs in A-DNA and the short rise that makes the A form 25 % shorter than the B form for the same number of base pairs](./plots/dna-forms.py)

Which family a duplex adopts depends on the free energy of its hydration and of its counterions, and the transitions between them can be followed by circular dichroism and by fiber diffraction.

- *B to A.* Lowering the water activity (relative humidity below about $75\,\%$, or $\gtrsim 70\,\%$ ethanol) converts B-DNA to A-DNA: the A form needs fewer ordered water molecules in its grooves and brings the phosphates closer together, which is favorable when water is scarce. Double-stranded RNA and RNA–DNA hybrids are A-form under all conditions because of the 2′-OH. In nature A-like DNA occurs in bacterial spores, where small acid-soluble proteins coat the DNA and protect it from UV damage, and in some viruses of hyperthermophiles that survive desiccation and heat.
- *B to Z.* Alternating purine–pyrimidine sequences, especially $(\mathrm{CG})_n$, switch to the left-handed Z form at high salt ($\approx 2.5\,\mathrm{M}$ NaCl or $0.7\,\mathrm{M}$ $\ce{MgCl2}$), when C5 is methylated, or under negative superhelical stress. Converting $12$ bp from B ($+1.14$ turns) to Z ($-1$ turn) changes the twist by about $-2.1$ turns, so Z segments absorb negative supercoiling (**supercoiling**, [7.2.3](/7.2.3)). Proteins with Zα domains (the RNA-editing enzyme ADAR1, the necroptosis sensor ZBP1) recognize Z-DNA and Z-RNA specifically.

**Example 7.3.1** The $48\,502\,\mathrm{bp}$ genome of phage λ is $48\,502 \times 0.338\,\mathrm{nm} = 16.4\,\mu\mathrm{m}$ long as B-DNA, with $4\,619$ helical turns; as A-DNA it would be $12.4\,\mu\mathrm{m}$ long with about $4\,409$ turns. A B to A transition of a closed circular DNA would therefore reduce the twist by $210$ turns; since the linking number of a closed circle cannot change, the molecule would have to compensate with $+210$ turns of writhe.

### 7.3.3. Stacking, Charge and Counterions

The stability of a duplex comes from the stacking of successive base pairs (van der Waals and electrostatic interactions of the aromatic rings, together with the hydrophobic effect), worth roughly $4$–$10\,\mathrm{kJ\,mol^{-1}}$ per step depending on the sequence, rather than from the hydrogen bonds between paired bases, which the bases of single strands can also make with water. These nearest-neighbor energies are what the unified parameters of [7.1.11](/7.1.11#sec-11.4.2) tabulate.

The backbone carries one negative charge per phosphate, two per base pair, so B-DNA has a linear charge density of one charge per $0.17\,\mathrm{nm}$ along the axis. This is a strongly charged rod: the electrostatic energy of bringing a monovalent counterion close is larger than $k_{\mathrm{B}}T$, and a fraction of the counterions remains bound to the rod however dilute the solution.

**Example 7.3.2** The Manning parameter of a charged rod is the ratio of the Bjerrum length to the charge spacing, $\xi = \ell_{\mathrm{B}}/b$ ([7.6.6](/7.6.6)). With $\ell_{\mathrm{B}} = 0.71\,\mathrm{nm}$ in water at $25\,^\circ\mathrm{C}$ and $b = 0.17\,\mathrm{nm}$, $\xi = 4.2$. Counterion condensation theory predicts that monovalent counterions neutralize a fraction $1 - 1/\xi = 76\,\%$ of the phosphate charge and divalent ones $1 - 1/(2\xi) = 88\,\%$. A-form RNA, with its shorter rise, is even more highly charged ($b \approx 0.14\,\mathrm{nm}$), which is one reason why RNA folding is so sensitive to $\ce{Mg^2+}$.

### 7.3.4. RNA Architecture

A single RNA strand folds back on itself into A-form helices joined by loops, bulges and junctions. Its tertiary structure is assembled from a small set of recurring motifs, each of which has a simple physical rationale.

- *Coaxial stacking*: helices whose ends meet at a junction stack end to end to recover stacking energy. In **transfer RNA** the acceptor and T arms stack into one helix and the D and anticodon arms into another, giving the L shape whose two arms are each about $7\,\mathrm{nm}$ long.
- *A-minor interactions*: adenines insert their minor-groove edge into the shallow minor groove of a neighboring A-form helix; the A form, with its wide minor groove, offers this surface, which B-DNA does not.
- *Tetraloop–receptor and kissing loops*: a GNRA tetraloop docks into a receptor motif in another helix; complementary hairpin loops pair with each other.
- *Kink-turns*: a three-nucleotide bulge that bends a helix by about $60^\circ$, stabilized by specific proteins and ions.
- *Pseudoknots*: a loop pairs with a sequence outside its own hairpin, so that the secondary structure is no longer nested (which also places pseudoknots outside the dynamic-programming algorithms of secondary-structure prediction, [7.6.21](/7.6.21)).

The packing of these motifs brings phosphates together at densities that would be impossible without counterions. Most $\ce{Mg^2+}$ ions around an RNA are diffuse (in the ion atmosphere), but a few are bound at specific sites where they bridge phosphates through direct or water-mediated coordination; **ribozymes** use such ions in catalysis. The hierarchy, with secondary structure forming first and stable on its own, and tertiary contacts forming later and depending on ions, makes RNA folding a sequence of distinct transitions, a subject continued in [7.6.22](/7.6.22).

## 7.4. Symmetry of Assemblies

### 7.4.1. Point Groups of Chiral Objects

Biological macromolecules are chiral: proteins are made of L-amino acids and nucleic acids of D-sugars (**chirality**). A symmetry operation of an assembly must map each subunit onto an identical subunit, so it cannot be a reflection or an inversion, which would turn L into D. The symmetries of a finite assembly are therefore proper rotations that fix its center.

**Definition 7.4.1 (Point Group)** A **point group** is a **group** of isometries of space that fix a point. The point group of an object is the group of all such isometries that map the object onto itself; for an assembly of chiral subunits it is a finite **subgroup** of the rotation group $\operatorname{SO}(3)$.

**Theorem 7.4.1 (Finite Rotation Groups)** Every finite subgroup of $\operatorname{SO}(3)$ is one of the following: the cyclic groups $C_n$ (order $n$), the dihedral groups $D_n$ (order $2n$, $n \geq 2$), the tetrahedral group $T$ (order $12$, isomorphic to the **alternating group** $A_4$), the octahedral group $O$ (order $24$, isomorphic to the **symmetric group** $S_4$) and the icosahedral group $I$ (order $60$, isomorphic to $A_5$).

**Proof** Let $G$ have order $N > 1$. Each rotation $g \ne e$ fixes exactly two points of the unit sphere, the poles of its axis, and $G$ maps poles to poles, so it acts on the set of poles (**group action**, [1.3.2](/1.3.2#sec-2.5.5)). Count the pairs $(g, x)$ with $g \ne e$ and $gx = x$. Each of the $N - 1$ non-identity elements contributes $2$. Grouping instead by poles: a pole $x$ is fixed by its **stabilizer** $G_x$ of order $n_x \ge 2$, contributing $n_x - 1$ pairs, and by the **orbit–stabilizer theorem** ([1.3.2](/1.3.2#thm-2.5.4)) its orbit has $N/n_x$ poles, all with the same $n_x$. If there are $k$ orbits with stabilizer orders $n_1, \dots, n_k$,

$$
2(N - 1) = \sum_{i=1}^{k} \frac{N}{n_i}(n_i - 1), \qquad\text{that is}\qquad 2\left(1 - \frac{1}{N}\right) = \sum_{i=1}^{k}\left(1 - \frac{1}{n_i}\right).
$$
The left side lies in $[1, 2)$ and each term on the right in $[\tfrac12, 1)$, so $k = 2$ or $k = 3$. If $k = 2$, then $1/n_1 + 1/n_2 = 2/N$ with $n_i \le N$, which forces $n_1 = n_2 = N$: all elements share one axis, and $G = C_N$. If $k = 3$, then $1/n_1 + 1/n_2 + 1/n_3 = 1 + 2/N > 1$; with $n_1 \le n_2 \le n_3$ this requires $n_1 = 2$, and then $(n_2, n_3) = (2, n)$ with $N = 2n$, or $(3, 3)$ with $N = 12$, $(3, 4)$ with $N = 24$, $(3, 5)$ with $N = 60$. These are the stabilizer data of $D_n$, $T$, $O$ and $I$; that each set of data determines the group up to conjugacy follows by reconstructing the polyhedron from the orbits of poles. $\square$

In crystallography, where mirror and inversion operations are allowed for achiral molecules, there are infinitely many point groups (and $32$ crystallographic ones), but for proteins and nucleic acids the list of Theorem 7.4.1 is complete. Crystals of biological macromolecules accordingly belong to the $65$ space groups without improper operations ([7.6.12](/7.6.12)). The exception proves the rule: racemic mixtures of a chemically synthesized L-protein and its D-enantiomer crystallize readily in centrosymmetric space groups, which natural proteins can never use.

### 7.4.2. Why Identical Subunits Assemble Symmetrically

Suppose identical subunits bind each other through the same pair of complementary surfaces, $A$ on one subunit binding $B$ on the next. The rigid motion that relates the two subunits is then the same for every bound pair, so by Theorem 7.2.1 the assembly is generated by repeating one screw. If the screw is a pure rotation by $360^\circ/n$, the assembly closes into a ring with $C_n$ symmetry; otherwise it grows into an open helix. Using two different interfaces gives the dihedral and cubic groups (a $D_n$ assembly is two $C_n$ rings related by twofold axes, $I$ assemblies use fivefold, threefold and twofold contacts). Symmetric assemblies are therefore the natural result of **quaternary structure** built from a small number of interface types, and closed assemblies are favored because every subunit makes all its contacts, which maximizes the binding free energy per subunit and makes assembly cooperative ([7.6.26](/7.6.26)).

| Symmetry | Order | Examples |
|---|---|---|
| $C_2$ | 2 | many homodimers; HIV protease |
| $C_3$ | 3 | the PCNA sliding clamp (pseudo-sixfold); trimeric viral fusion proteins such as influenza hemagglutinin |
| $C_4$, $C_5$ | 4, 5 | potassium channels ($C_4$); pentameric ligand-gated channels such as the nicotinic acetylcholine receptor ($C_5$, or pseudo-$C_5$ for heteromers) |
| $C_7$ to $C_{17}$ | | GroES ($C_7$), the ATP synthase c ring ($C_8$–$C_{15}$, [7.1.23](/7.1.23)), the bacterial flagellar motor C ring (about $C_{34}$) |
| $D_2$ | 4 | tetramers such as lactate dehydrogenase and (approximately) hemoglobin |
| $D_7$ | 14 | the GroEL double ring (**chaperonin**) |
| $T$ | 12 | Dps (a ferritin-like DNA-protecting dodecamer of bacteria); the TET aminopeptidase of archaea |
| $O$ | 24 | ferritin (iron store, $12\,\mathrm{nm}$ shell with an $8\,\mathrm{nm}$ cavity); the E2 core of pyruvate dehydrogenase in bacteria |
| $I$ | 60 | lumazine synthase, the E2 core of mammalian pyruvate dehydrogenase, the capsids of $T = 1$ viruses |

![The symmetries available to assemblies of identical chiral subunits (Theorem 7.4.1). Each group was generated numerically by closure from two rotation generators and applied to one asymmetric subunit (a large and a small sphere, so that its orientation can be seen); nearer subunits are darker, and one copy is highlighted. C₅: one fivefold axis (viewed along it). D₄: two C₄ rings related by twofold axes. T, O, I: the rotation groups of the tetrahedron, the cube or octahedron, and the icosahedron or dodecahedron, with 12, 24 and 60 equivalent positions; faint lines are the edges of the corresponding polyhedron. Last panel: a helical array with 3.5 subunits per turn, open-ended along its vertical axis](./plots/point-groups.py)

### 7.4.3. Helical Assemblies

**Definition 7.4.2 (Helical Symmetry)** An assembly has **helical symmetry** if all its subunits are related by powers of one screw operation, a rotation by $\Delta\phi$ about an axis combined with a translation $\Delta z$ along it, possibly together with a $C_m$ rotational symmetry about the same axis. It is characterized by the twist $\Delta\phi$ and the rise $\Delta z$ per subunit, or equivalently by the number of subunits per turn $u = 360^\circ/\Delta\phi$ and the pitch $p = u\,\Delta z$.

Because the screw can be repeated indefinitely, helical assemblies are open-ended: their length is set by kinetics, by a template or by a ruler, not by the symmetry itself. A helix with a non-integer number of subunits per turn can be described by several families of helical lines through its subunits (the 1-start, 2-start and higher "start" helices of a helical net); which one is called the helix is a convention, and the same structure can have a left-handed short-pitch helix and right-handed long-pitch helices.

| Assembly | Twist / rise per subunit | Description |
|---|---|---|
| Tobacco mosaic virus | $360^\circ/16.33 = 22.0^\circ$ / $0.14\,\mathrm{nm}$ | right-handed; $49$ subunits in $3$ turns, pitch $2.3\,\mathrm{nm}$; rod $300\,\mathrm{nm} \times 18\,\mathrm{nm}$ |
| **actin filament** | $-166.6^\circ$ / $2.75\,\mathrm{nm}$ | the 1-start (genetic) helix is left-handed with nearly two subunits per turn; seen as two right-handed long-pitch strands in which subunits are $5.5\,\mathrm{nm}$ apart, crossing every $36\,\mathrm{nm}$ |
| **microtubule** | 13 protofilaments, 3-start lattice | αβ-**tubulin** dimers $8\,\mathrm{nm}$ long; the lattice has a seam, so it is not strictly helical; outer diameter $25\,\mathrm{nm}$ |
| Bacterial flagellar filament | about $5.5$ subunits per turn | 11 protofilaments that switch between two lengths to make the filament supercoil |

**Example 7.4.1** The RNA of tobacco mosaic virus has $6\,395$ nucleotides and each coat-protein subunit binds three of them, so the rod contains about $2\,130$ subunits. At $16.33$ subunits per turn that is $130.5$ turns, and with a pitch of $2.3\,\mathrm{nm}$ the rod is $300\,\mathrm{nm}$ long, exactly the length seen in the electron microscope. The genome is the ruler: TMV coat protein alone forms rods of any length, and the RNA fixes the length of the virion.

The two notations for actin illustrate the convention of the previous paragraph: successive subunits along the 1-start helix are related by $-166.6^\circ$ and $2.75\,\mathrm{nm}$, which places them on alternate long-pitch strands; within one strand, subunits are related by twice the screw, $2 \times (-166.6^\circ) + 360^\circ = 26.8^\circ$ and $5.5\,\mathrm{nm}$. (A description in which adjacent subunits "of one protofilament" are rotated by $167^\circ$ and raised by $2.7\,\mathrm{nm}$ mixes the two.) The polymerization dynamics of these filaments, treadmilling and dynamic instability, are treated in [7.3.13](/7.3.13), [7.3.14](/7.3.14) and [7.6.34](/7.6.34).

## 7.5. Icosahedral Capsids

### 7.5.1. The Coding Argument

In 1956 Francis Crick and James Watson pointed out that small viruses cannot code for a protein shell made of one large protein: a genome of a few thousand nucleotides codes for at most a few thousand amino acids, too few to enclose itself. The shell must be built from many copies of one or a few small proteins, and by §7.4.2 identical copies bound by identical contacts form either a helix (as in TMV) or a closed shell with cubic symmetry. Of the cubic groups the icosahedral one has the largest order, $60$, so it encloses the largest volume with subunits of a given size, and most "spherical" viruses are icosahedral.

**Example 7.5.1** Satellite tobacco necrosis virus has a $1\,239$-nucleotide RNA and a capsid of $60$ copies of a $195$-residue coat protein: the coat gene uses $3 \times 195 = 585$ nucleotides, about half of the genome, yet the shell of $60 \times 21\,\mathrm{kDa} = 1.3\,\mathrm{MDa}$ is twice the mass of the RNA it encloses. A single protein large enough to make the same shell would need a gene of $35\,000$ nucleotides.

### 7.5.2. Quasi-Equivalence and the Triangulation Number

Sixty is the largest number of subunits that can occupy strictly equivalent positions on a closed shell, but many capsids contain $180$, $240$, $420$ or more copies of the same protein. In 1962 Donald Caspar and Aaron Klug explained how.

**Definition 7.5.1 (Quasi-Equivalence)** **Quasi-equivalence** is the principle that identical subunits in a shell of more than $60$ copies occupy slightly different environments, making the same kinds of bonds with small deformations, so that the subunits are grouped into pentamers and hexamers whose bonding pattern is locally the same everywhere.

The subunits cluster into **capsomeres**, pentamers at the twelve fivefold vertices and hexamers elsewhere. The geometry of such shells is fixed by two counting results.

**Theorem 7.5.1 (Twelve Pentamers)** A closed shell, topologically a sphere, in which each capsomer touches its neighbors so that the capsomer centers are the vertices of a triangulated surface, and in which every capsomer is a pentamer or a hexamer (five or six neighbors), contains exactly $12$ pentamers.

**Proof** Let $V_5$ and $V_6$ be the numbers of pentamers and hexamers, $V = V_5 + V_6$, and let $E$ and $F$ be the numbers of edges and triangular faces of the triangulation. Euler's formula for a sphere ([1.4.4](/1.4.4#thm-4.1.1)) gives $V - E + F = 2$. Each face has three edges and each edge borders two faces, so $3F = 2E$; each edge has two ends, so $5V_5 + 6V_6 = 2E$. Eliminating $F$, $E = 3V - 6$, hence $5V_5 + 6V_6 = 6V - 12 = 6V_5 + 6V_6 - 12$, that is, $V_5 = 12$. $\square$

The number of hexamers is not fixed by topology. Icosahedral symmetry restricts it: the triangulation must look the same around each of the twelve pentamers, which means that it is cut from a hexagonal lattice.

**Definition 7.5.2 (Triangulation Number)** Place capsomer positions on a hexagonal lattice with unit vectors $\boldsymbol{a}_1$, $\boldsymbol{a}_2$ at $60^\circ$. One face of the icosahedral shell is the equilateral triangle spanned by the lattice vector $h\boldsymbol{a}_1 + k\boldsymbol{a}_2$ ($h, k$ non-negative integers) and its rotation by $60^\circ$, with pentamers at its corners. The **triangulation number** is

$$
T = h^2 + hk + k^2 ,
$$
the area of this face in units of the smallest lattice triangle.

The face area is proportional to the squared length of its edge vector, $\lvert h\boldsymbol{a}_1 + k\boldsymbol{a}_2\rvert^2 = h^2 + 2hk\,\boldsymbol{a}_1\cdot\boldsymbol{a}_2 + k^2 = h^2 + hk + k^2$ (since $\boldsymbol{a}_1\cdot\boldsymbol{a}_2 = \tfrac12$ for unit vectors), which is why $T$ is this quadratic form. The allowed values are $1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, \dots$; $T = 2, 5, 6, 8, 10, 11, \dots$ cannot occur.

**Theorem 7.5.2 (Caspar–Klug Counting)** An icosahedral shell with triangulation number $T$ has $20T$ triangular faces, $30T$ edges and $10T + 2$ capsomers: $12$ pentamers and $10(T - 1)$ hexamers, containing $60T$ subunits, so that each of the $60$ icosahedral asymmetric units contains $T$ quasi-equivalent subunits.

**Proof** Each of the $20$ icosahedral faces contains $T$ elementary triangles, so $F = 20T$ and $E = 3F/2 = 30T$. Euler's formula gives $V = 2 + E - F = 10T + 2$, and Theorem 7.5.1 gives $V_5 = 12$, $V_6 = 10T - 10$. The number of subunits is $5 \times 12 + 6(10T - 10) = 60T$. $\square$

![The Caspar–Klug construction. A: capsomer positions on a hexagonal lattice; the face of the shell is the equilateral triangle spanned by the lattice vector (h, k), reached by h steps along a₁ and k steps along a₂ (dashed), and its rotation by 60°; its corners become pentamers (blue) and all other lattice points hexamers. B: shells built by mapping the lattice points inside each face onto the twenty faces of an icosahedron and projecting them onto a sphere (nearer capsomers larger and brighter); the program counts 12 pentamers and 10(T − 1) hexamers, 60T subunits, as Theorem 7.5.2 states. T = 1 and T = 3 have the capsomer arrangement of a dodecahedron and of a truncated icosahedron (a soccer ball); T = 7, with h ≠ k and both nonzero, is chiral and exists in two mirror-image forms (laevo and dextro), only one of which a given virus uses](./plots/caspar-klug.py)

| $T$ | $(h, k)$ | Capsomers (pentamers + hexamers) | Subunits | Examples |
|---|---|---|---|---|
| 1 | (1, 0) | 12 + 0 | 60 | satellite tobacco necrosis virus, adeno-associated virus |
| 3 | (1, 1) | 12 + 20 | 180 | tomato bushy stunt virus, cowpea chlorotic mottle virus |
| 4 | (2, 0) | 12 + 30 | 240 | hepatitis B virus core (mostly $T = 4$, some $T = 3$), alphavirus shells |
| 7 | (2, 1) | 12 + 60 | 420 | phage HK97 and λ heads ($T = 7$ laevo) |
| 13 | (3, 1) | 12 + 120 | 780 | outer layer of reoviruses and bluetongue virus |
| 16 | (4, 0) | 12 + 150 | 960 | herpesvirus capsid (162 capsomeres) |

### 7.5.3. Beyond Quasi-Equivalence

The Caspar–Klug scheme predicts the capsomer lattice of a great many viruses, but structures solved later showed that quasi-equivalence is a geometric rule rather than a law of bonding.

- *Pseudo-$T$ capsids.* Picornaviruses (poliovirus, rhinovirus) have $60$ copies each of three different proteins, VP1–VP3, with the same jelly-roll fold, arranged like a $T = 3$ shell (called pseudo-$T = 3$, or $P = 3$). Adenovirus has $240$ hexon trimers and $12$ penton bases, the capsomer count $10T + 2 = 252$ of $T = 25$, but its hexons are trimers of a protein different from the pentons: each triangular facet carries $12$ hexon trimers.
- *All-pentamer shells.* The capsids of polyomaviruses (SV40) and papillomaviruses consist of $72$ pentamers ($360$ subunits) on a $T = 7$ lattice: the $60$ hexavalent positions are occupied by pentamers, held together by flexible C-terminal arms that make different contacts in different environments. Quasi-equivalence of bonding fails completely, while the lattice survives.
- *Non-icosahedral closed shells.* Theorem 7.5.1 does not require icosahedral symmetry. The mature capsid of HIV is a fullerene cone of about $250$ hexamers of the CA protein and exactly $12$ pentamers, $7$ at the wide end and $5$ at the narrow end; the cone shape is the result of distributing the twelve pentamers unequally.
- *Large and complex viruses.* Giant DNA viruses (the African swine fever virus, $260\,\mathrm{nm}$ across, with more than $30\,000$ protein subunits) have multilayered capsids with triangulation numbers in the hundreds and minor proteins that act as rulers and glue.

## 7.6. From Complexes to Cellular Ultrastructure

The size of a compact macromolecule follows from its mass and density. Proteins have a nearly constant density of about $1.35\,\mathrm{g\,cm^{-3}}$ (partial specific volume $0.73\,\mathrm{cm^3\,g^{-1}}$), because their interiors are packed as densely as organic crystals.

**Formula 7.6.1 (Minimal Radius of a Protein)** A compact sphere of protein of molar mass $M$ has radius

$$
R_{\min} = \left(\frac{3M}{4\pi\rho N_{\mathrm{A}}}\right)^{1/3} \approx 0.066\,M^{1/3}\ \mathrm{nm} \qquad (M \text{ in Da}, \ \rho = 1.35\,\mathrm{g\,cm^{-3}}).
$$

For $M = 50\,\mathrm{kDa}$, $R_{\min} = 2.4\,\mathrm{nm}$; real globular proteins are $10$–$20\,\%$ larger because they are not spheres and carry a hydration layer, a difference that hydrodynamic measurements turn into information about shape ([7.6.9](/7.6.9)).

![Size against mass for macromolecules and assemblies. Line: diameter of a compact sphere of protein density (Formula 7.6.1), d ∝ M^(1/3). Points: approximate largest dimensions of real objects (rounded literature values); compact objects (purple) lie close to the line, hollow shells and rings (pink) and elongated molecules (green) above it, myosin and the tobacco mosaic virus rod by a factor of 10 or more. Top axis: the equivalent number of amino-acid residues at 110 Da per residue](./plots/size-mass.py)

The machines of the cell span four orders of magnitude in mass and two in size: the **nucleosome** core ($206\,\mathrm{kDa}$, $11\,\mathrm{nm}$), RNA polymerase II ($0.5\,\mathrm{MDa}$, $15\,\mathrm{nm}$), the bacterial and eukaryotic **ribosomes** ($2.5$ and $4.3\,\mathrm{MDa}$, $21$ and $25$–$30\,\mathrm{nm}$), the **spliceosome** (about $100$ proteins and five RNAs, $\approx 30\,\mathrm{nm}$), the red-algal phycobilisome–photosystem supercomplex (more than $30\,\mathrm{MDa}$, $\approx 50\,\mathrm{nm}$) and the human **nuclear pore complex** (more than $100\,\mathrm{MDa}$, $120\,\mathrm{nm}$). Their structures were solved first by crystallography of the smaller complexes (the nucleosome core in 1997, Pol II and the ribosomal subunits in 2000) and in the last decade by cryo-electron microscopy, often combined with prediction and cross-linking ([7.6.21](/7.6.21)).

Above the scale of single complexes, machines are organized into what has been called the molecular sociology of the cell: ribosomes arrayed on the endoplasmic reticulum and in polysomes, phycobilisomes packed in rows on thylakoid membranes, ATP synthase dimers lining the curved ridges of mitochondrial cristae, nucleosome arrays condensed into heterochromatin. Cryo-electron tomography of frozen cells and lamellae ([7.6.20](/7.6.20)) now resolves such arrangements in situ. The same few physical rules recur at every level: identical contacts generate symmetry, closure is favored over open growth when it satisfies all contacts, and the free energy of assembly is a small difference between large terms, as the measurements of the next chapter make explicit.

## Summary

| Topic | Key result | Where |
|---|---|---|
| Stiffness hierarchy | bonds fluctuate by $0.03\,\text{Å}$, angles by $4^\circ$; torsions are the soft coordinates | Example 7.1.1 |
| Peptide group | planar, trans; X–Pro cis–trans isomerization takes minutes ($\Delta G^\ddagger \approx 85\,\mathrm{kJ/mol}$) | Example 7.1.2 |
| Energy map | $E(\varphi,\psi)$ from pair potentials, $p \propto \mathrm{e}^{-E/k_{\mathrm{B}}T}$ | Formula 7.1.1 |
| Conformational entropy | $S_{\mathrm{conf}} = -k_{\mathrm{B}}\sum p_c\ln p_c$; Gly − Ala $\approx 11\,\mathrm{J\,mol^{-1}\,K^{-1}}$ | Definition 7.1.1, Example 7.1.3 |
| Sugar pucker | $\nu_j = \nu_{\max}\cos(P + 4\pi(j-2)/5)$; C2′-endo (B) vs C3′-endo (A, RNA) | Formula 7.1.2 |
| Repeats are screws | $\cos\theta = (\operatorname{tr}R - 1)/2$, $d = \boldsymbol{t}\cdot\boldsymbol{u}$, $n = 360^\circ/\theta$ | Theorem 7.2.1, Algorithm 7.2.1 |
| α helix | $3.6$ residues, $1.5\,\text{Å}$ rise; macrodipole $\approx \pm 0.5\,e$; heptads give a supercoil of $\sim 15$–$20\,\mathrm{nm}$ | Examples 7.2.1–7.2.2 |
| Duplexes | B: $10.5\,\mathrm{bp}$, $0.338\,\mathrm{nm}$; A: $11\,\mathrm{bp}$, $0.26$–$0.29\,\mathrm{nm}$, displaced bp; Z: left-handed, dinucleotide repeat | Formula 7.3.1, table in §7.3.2 |
| Counterions | DNA charge spacing $0.17\,\mathrm{nm}$, Manning $\xi = 4.2$, $76\,\%$ neutralized by monovalent ions | Example 7.3.2 |
| Point groups | chiral assemblies: $C_n$, $D_n$, $T$ (12), $O$ (24), $I$ (60) | Definition 7.4.1, Theorem 7.4.1 |
| Helical symmetry | twist $\Delta\phi$ and rise $\Delta z$ per subunit; TMV $16.33$/turn, actin $-166.6^\circ$/$2.75\,\mathrm{nm}$ | Definition 7.4.2, Example 7.4.1 |
| Capsids | always $12$ pentamers; $T = h^2 + hk + k^2$, $10T + 2$ capsomers, $60T$ subunits | Definitions 7.5.1–7.5.2, Theorems 7.5.1–7.5.2 |
| Size | $R_{\min} \approx 0.066\,M^{1/3}\,\mathrm{nm}$ | Formula 7.6.1 |

## Questions

1. A C–N peptide bond has a stretching constant $\kappa \approx 950\,\mathrm{kcal\,mol^{-1}\,\text{Å}^{-2}}$. What is its root-mean-square length fluctuation at $310\,\mathrm{K}$? Compare with the change in C–N length between a single ($1.47\,\text{Å}$) and a double ($1.27\,\text{Å}$) bond.

   **Answer** $\kappa = 950 \times 4184/(6.022\times10^{23}) \times 10^{20}\,\mathrm{J\,m^{-2}} = 660\,\mathrm{N\,m^{-1}}$ and $k_{\mathrm{B}}T = 4.28\times10^{-21}\,\mathrm{J}$, so $\sqrt{k_{\mathrm{B}}T/\kappa} = 2.5\times10^{-12}\,\mathrm{m} = 0.025\,\text{Å}$, an eighth of the single–double difference of $0.2\,\text{Å}$. Thermal motion cannot change the bond order; the planarity of the peptide is not threatened by fluctuations, only by the much softer torsion $\omega$ (which varies by $\pm 5$–$10^\circ$ in real structures).

2. The refolding of a denatured protein with one cis X–Pro bond in its native state shows a fast phase ($10\,\mathrm{ms}$) with $20\,\%$ amplitude and a slow phase ($\tau \approx 2\,\mathrm{min}$ at $25\,^\circ\mathrm{C}$) with $80\,\%$ amplitude. Interpret both phases, estimate the activation free energy of the slow phase, and predict the effect of adding a prolyl isomerase.

   **Answer** In the unfolded state the X–Pro bond equilibrates between cis and trans; the $20\,\%$ of molecules that happen to have it cis fold fast, the $80\,\%$ with trans must isomerize first. From $k = 1/120\,\mathrm{s^{-1}}$, $\Delta G^\ddagger = RT\ln(k_{\mathrm{B}}T/hk) = 2.48 \times \ln(6.2\times10^{12} \times 120) = 2.48 \times 34.2 = 85\,\mathrm{kJ\,mol^{-1}}$ (Example 7.1.2). A prolyl isomerase lowers this barrier and accelerates the slow phase, without changing the amplitudes (which reflect the cis/trans equilibrium of the unfolded chain); the fast phase is unaffected.

3. Explain, using Theorem 7.2.1, why a chain with $n = 2$ residues per turn is achiral, and why real β strands are not exactly at $n = 2$.

   **Answer** For $n = 2$ the screw is a rotation by $180^\circ$ combined with a translation; a rotation by $+180^\circ$ and by $-180^\circ$ are the same, so the screw has no handedness, and the ribbon is the same as its mirror image as far as the backbone trace is concerned. But each residue is chiral (L-$\mathrm{C}_\alpha$), so there is no reason for the energy minimum of a strand to lie exactly at $\theta = 180^\circ$; the minima of the L-amino-acid map lie slightly off it, which gives strands a small right-handed twist and sheets their twisted, propeller-like shape. A strand made of D-amino acids would twist the other way.

4. A transmembrane helix must span the hydrophobic core of a bilayer, about $3.0\,\mathrm{nm}$ thick. How many residues does it need as an α helix, and how many would it need as a β strand? What does this imply for the structure of outer-membrane proteins of bacteria?

   **Answer** α helix: $3.0/0.15 = 20$ residues; β strand: $3.0/0.33$–$0.35 \approx 9$ residues (more if tilted). A single β strand cannot satisfy its backbone hydrogen bonds inside the bilayer, so strands occur only in closed sheets: the β barrels of outer-membrane porins, with 8 to 26 strands of $9$–$11$ residues each, every strand hydrogen-bonded to its two neighbors.

5. Using Formula 7.3.1, compute the number of helical turns in a $5\,000\,\mathrm{bp}$ closed circular DNA as B-DNA in solution and in the fiber form with $10.0$ bp per turn. If the circle was closed with linking number $Lk = 476$ and is then studied in solution, what is the writhe, and is the DNA positively or negatively supercoiled?

   **Answer** $Tw = 5\,000/10.5 = 476.2$ turns in solution and $500$ in the fiber form. With $Lk = 476$, $Wr = Lk - Tw = 476 - 476.2 = -0.2$: essentially relaxed, very slightly negatively supercoiled. If the same molecule were forced into $10.0$ bp per turn (for example by a twisting ligand), $Wr = 476 - 500 = -24$: strong negative writhe. The correct solution value of the helical repeat is thus essential to interpret supercoiling (**supercoiling**, [7.2.3](/7.2.3)).

6. Natural proteins never crystallize in centrosymmetric space groups, but a 1:1 mixture of a chemically synthesized protein and its mirror image does, and often more easily than either enantiomer alone. Explain both facts with §7.4.1, and suggest why racemic crystallization is useful for structure determination.

   **Answer** Inversion and mirror operations map an L-protein onto a D-protein, so in a crystal of one enantiomer they can never be symmetry operations; only the $65$ space groups of proper operations are available. In a racemic mixture an inversion can relate an L molecule to a D molecule, so all $230$ space groups are available, including the centrosymmetric ones such as $P\bar{1}$ and $P2_1/c$ that are the most common for small achiral molecules (they allow the densest packings). Racemic crystals therefore form more readily, and centrosymmetric structures have phases restricted to $0$ or $\pi$, which simplifies phasing ([7.6.13](/7.6.13)).

7. Which triangulation numbers between $1$ and $30$ are possible? For $T = 13$ and $T = 16$, give $(h, k)$, the numbers of pentamers, hexamers and subunits, and say which of the two is chiral.

   **Answer** $T = h^2 + hk + k^2$ takes the values $1, 3, 4, 7, 9, 12, 13, 16, 19, 21, 25, 27, 28$ below $30$ (pairs $(1,0), (1,1), (2,0), (2,1), (3,0), (2,2), (3,1), (4,0), (3,2), (4,1), (5,0), (3,3), (4,2)$). $T = 13$: $(3, 1)$, $12$ pentamers, $120$ hexamers, $780$ subunits; chiral, because $h \ne k$ and both are nonzero (the laevo and dextro lattices are mirror images). $T = 16$: $(4, 0)$, $12$ pentamers, $150$ hexamers, $960$ subunits; achiral (the $k = 0$ and $h = k$ classes have mirror-symmetric lattices).

8. Prove that in a closed shell built of pentamers, hexamers and heptamers (each capsomer a vertex of a triangulated sphere), $V_5 - V_7 = 12$. What does this mean for tubular or conical capsids?

   **Answer** As in Theorem 7.5.1, $E = 3V - 6$ and $2E = 5V_5 + 6V_6 + 7V_7$, so $5V_5 + 6V_6 + 7V_7 = 6(V_5 + V_6 + V_7) - 12$, that is, $V_5 - V_7 = 12$. Each heptamer allows one extra pentamer: shells can contain negative curvature (heptamers, saddle-shaped regions) if it is paid for by additional positive curvature. In cones and tubes the twelve units of positive curvature are distributed between the two ends (the HIV cone puts $7$ pentamers at the wide end and $5$ at the narrow end).

9. A plant virus with a $4.2\,\mathrm{kb}$ RNA genome has a $T = 3$ capsid of a $20\,\mathrm{kDa}$ coat protein. What fraction of the genome codes for the coat, what is the mass of the capsid, and how does it compare with the mass of the RNA ($330\,\mathrm{Da}$ per nucleotide)? Estimate the outer diameter, assuming a shell $3\,\mathrm{nm}$ thick of protein density.

   **Answer** $20\,\mathrm{kDa}/110\,\mathrm{Da} \approx 180$ residues, $540$ nucleotides: $13\,\%$ of the genome. Capsid: $180 \times 20\,\mathrm{kDa} = 3.6\,\mathrm{MDa}$; RNA: $4\,200 \times 330 = 1.4\,\mathrm{MDa}$, so the shell is about $2.6$ times heavier. Shell volume: $3.6\times10^6 \times 1.23\times10^{-3}\,\mathrm{nm^3} = 4.4\times10^3\,\mathrm{nm^3}$ (Formula 7.6.1); for a shell of thickness $t = 3\,\mathrm{nm}$ and mean radius $r$, $4\pi r^2 t = 4.4\times10^3$ gives $r = 10.8\,\mathrm{nm}$, an outer diameter of about $25$–$28\,\mathrm{nm}$, typical of $T = 3$ plant viruses.

10. Show from Formula 7.6.1 that a spherical protein of $150\,\mathrm{kDa}$ would have a diameter of $7\,\mathrm{nm}$. Immunoglobulin G has this mass but spans about $15\,\mathrm{nm}$. What does this say about its shape, and how could it be measured in solution?

    **Answer** $d = 2 \times 0.0665 \times (1.5\times10^5)^{1/3} = 2 \times 0.0665 \times 53.1 = 7.1\,\mathrm{nm}$. An IgG of twice this length is far from compact: it is a flexible Y of three globular arms ($\approx 50\,\mathrm{kDa}$ each) joined by a hinge. In solution this shows up as a frictional ratio $f/f_0 \approx 1.5$ from sedimentation velocity and diffusion ([7.6.9](/7.6.9)), a radius of gyration larger than that of a sphere of the same mass in small-angle scattering ([7.6.10](/7.6.10)), and directly in cryo-EM images and single-particle classes.

11. (Open) The structure of the tobacco mosaic virus rod is set by its RNA (Example 7.4.1), while the length of an actin filament in a cell is set by kinetics. Propose one mechanism by which a cell could build helical filaments of a well-defined length, and say how you would test it.

    **Answer** Possible mechanisms: a molecular ruler (a long protein that spans the filament and caps it at a fixed length, as nebulin is thought to do for thin filaments in skeletal muscle, or the tape-measure protein for phage tails); a length-dependent depolymerization rate (motors such as kinesin-8 that walk to the plus end and remove subunits, so longer filaments are shortened faster); or a limiting pool of subunits shared by a fixed number of filaments. Tests: change the length of the putative ruler by deletion or insertion and see whether filament length changes proportionally; measure the length distribution (a ruler gives a narrow peak, balanced assembly and disassembly an exponential or Gamma distribution); vary the subunit concentration (a limiting pool makes length depend on the number of nucleation sites).
