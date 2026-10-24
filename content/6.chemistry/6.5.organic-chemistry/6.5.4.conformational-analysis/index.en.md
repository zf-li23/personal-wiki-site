---
title: Conformational Analysis
source_hash: e33bc980f36d
---

Organic molecules are not rigid ball-and-stick models: single bonds rotate, rings flip, and at room temperature a molecule goes through hundreds of millions of changes of shape every second. Stereochemistry studies the arrangement of atoms in space and divides into two questions: the various shapes produced by rotation about single bonds and their energies, that is, conformations, and the spatial arrangements that cannot be interconverted without breaking chemical bonds, that is, configurations. This chapter treats the former and [6.5.5](/6.5.5) the latter. Conformation determines the shape in which a molecule mainly exists and the shape from which a reaction starts: the requirement of antiperiplanar geometry in the E2 elimination of [6.5.9](/6.5.9#sec-9.4.2), the stereoselectivity of the reduction of cyclohexanones in [6.5.17](/6.5.17#sec-17.1.2) and the reason why glucose exists mainly as the β form in [6.5.32](/6.5.32) all have to be explained with the chair conformation of this chapter.

The tools of this chapter are few: first, the electronic effects of [6.5.2](/6.5.2#def-2.6.1) (**hyperconjugation**) and van der Waals repulsion; second, the conversion between energy and populations, that is, the **Boltzmann distribution** ([6.3.10](/6.3.10)) and $\Delta G^\circ = -RT\ln K$ ([6.5.3](/6.5.3#sec-3.6.2)); and third, the use of heats of combustion to measure the stability of molecules. We begin with the torsional energy of ethane and butane, then discuss ring strain quantitatively with heats of combustion, then concentrate on the most important ring, cyclohexane and its substituted derivatives, and finally look at fused rings and cage molecules.

## 4.1. Classification of Isomerism

**Definition 4.1.1** Compounds with the same molecular formula but different structures are called **isomers**. Those that differ in the way and order in which the atoms are connected are called **constitutional isomers**, as in chain isomerism, positional isomerism of functional groups, functional group isomerism and tautomerism; those with the same connectivity that differ only in the arrangement of atoms in space are called **stereoisomers**.

Stereoisomers are further divided into two kinds according to the cost of interconversion.

**Definition 4.1.2** The spatial arrangements of atoms that can be interconverted merely by rotation about single bonds (and by ring flipping, nitrogen inversion and other motions that do not involve bond breaking) are called the **conformations** of a molecule; stereoisomers that differ only in conformation are called **conformers**. The spatial arrangements that can be interconverted only by breaking and re-forming chemical bonds are called the **configurations** of a molecule; stereoisomers with different configurations are called configurational isomers.

| Class | Interconversion | Typical barrier | Examples | In this course |
|---|---|---|---|---|
| Constitutional isomers | Bond breaking and reorganization | Generally $> 150\,\mathrm{kJ\,mol^{-1}}$ | Butane and isobutane, ethanol and dimethyl ether | [6.5.1](/6.5.1) |
| Conformers | Rotation about single bonds, ring flipping | Mostly $5$–$60\,\mathrm{kJ\,mol^{-1}}$ | The anti and gauche conformers of butane, the two chair conformations of cyclohexane | This chapter |
| Configurational isomers | Bond breaking and reorganization | Generally $> 150\,\mathrm{kJ\,mol^{-1}}$ | *cis*- and *trans*-but-2-ene, a pair of enantiomers | [6.5.5](/6.5.5) |

Configurational isomers are further divided into **enantiomers** and **diastereomers**, and those showing **cis–trans isomerism** are diastereomers ([6.1.5](/6.1.5) introduced these concepts with coordination compounds). The boundary between the two kinds of stereoisomers is a barrier, and is therefore not absolute: conformers with a half-life above $1000\,\mathrm{s}$ at room temperature can be separated (Ōki's criterion, corresponding to a rotational barrier of about $93\,\mathrm{kJ\,mol^{-1}}$, estimated with the **Eyring equation**), and such separable isomers arising from hindered rotation are called **atropisomers**, for example the binaphthol of [6.5.5](/6.5.5#sec-5.5.1). Conversely, conformational changes of very low energy are too fast at room temperature to be separated: ethane rotates about $10^{10}$ times per second and cyclohexane flips about $10^5$ times per second.

The significance of studying conformations is that a molecule exists mainly in its lowest-energy, preferred conformation; structures are usually drawn in the preferred conformation; and reactions often (though not always, see the **Curtin–Hammett principle** of [6.5.3](/6.5.3#sec-3.9.3)) proceed through the preferred conformation. The analysis of the various conformations of a molecule, their energies and populations and their influence on properties and reactivity is called *conformational analysis*. In 1969 Barton and Hassel received the Nobel Prize in Chemistry for establishing conformational analysis.

## 4.2. Conformations of Open-Chain Compounds

### 4.2.1. Representations of Conformations

A three-dimensional conformation must be represented in a two-dimensional drawing. Three kinds of drawings are commonly used:

- Wedge formula: a solid wedge bond points out of the paper, a hashed wedge bond points into the paper, and an ordinary line lies in the plane of the paper; it is suitable for showing the stereochemical relations around one carbon atom.
- Sawhorse formula: the $\ce{C-C}$ bond is viewed obliquely from above and the substituents of both carbon atoms are drawn; it is intuitive but inconvenient for comparing dihedral angles.
- Newman projection: the molecule is viewed along the direction of the $\ce{C-C}$ bond.

**Definition 4.2.1 (Newman Projection)** When a molecule is viewed along the axis of a particular $\ce{C-C}$ bond, the front carbon atom is drawn as a point from which its three bonds radiate, and the rear carbon atom, hidden behind the front carbon, is drawn as a circle from whose circumference its three bonds radiate. Such a projection is called a **Newman projection**.

A Newman projection directly shows the dihedral angle between the substituents on the two carbon atoms.

**Definition 4.2.2 (Torsion Angle)** For four atoms A–B–C–D joined in sequence, the angle $\varphi$ between the projections of the A–B bond and the C–D bond on a plane perpendicular to the B–C bond is called the **torsion angle** (also called the dihedral angle). Looking from B toward C, $\varphi$ is positive when A is turned clockwise to D and negative when counterclockwise, $-180^\circ < \varphi \le 180^\circ$.

By the IUPAC (Klyne–Prelog) convention, $\varphi$ in the ranges $0^\circ \pm 30^\circ$, $\pm 60^\circ \pm 30^\circ$, $\pm 120^\circ \pm 30^\circ$ and $180^\circ \pm 30^\circ$ is called synperiplanar (sp), synclinal (sc), anticlinal (ac) and antiperiplanar (ap), respectively. In everyday language synclinal means the gauche conformation, antiperiplanar means the anti conformation, and "**antiperiplanar**" is the arrangement referred to as anti coplanar.

### 4.2.2. Ethane

The two methyl groups of ethane rotate about the $\ce{C-C}$ bond, and there are two extreme conformations: the *staggered conformation*, in which the $\ce{C-H}$ bonds on the front and rear carbons are pairwise offset ($\varphi = 60^\circ$), and the *eclipsed conformation*, in which they coincide pairwise ($\varphi = 0^\circ$). The staggered conformation has the lowest energy and the eclipsed one the highest, the difference being $12\,\mathrm{kJ\,mol^{-1}}$ ($2.9\,\mathrm{kcal\,mol^{-1}}$), on average about $4\,\mathrm{kJ\,mol^{-1}}$ per eclipsing $\ce{H/H}$ pair. This barrier is far smaller than the energy available from molecular collisions at room temperature; estimated with the Eyring equation, each ethane molecule rotates about $10^{10}$ times per second at room temperature, so the conformers of ethane cannot be separated.

![Torsional potential energy curves of ethane and butane; the horizontal axis is the torsion angle and the energy is zero at the lowest-energy conformation; the insets are Newman projections of the extreme conformations](./plots/torsion-energy.py)

**Definition 4.2.3 (Torsional Strain)** The rise in energy caused by a departure from the staggered conformation, which brings the bonds on adjacent carbon atoms toward eclipsing, is called **torsional strain**.

In the eclipsed conformation the two H atoms are about $230\,\mathrm{pm}$ apart, slightly less than the sum of the van der Waals radii of two H atoms ($240\,\mathrm{pm}$), but such steric repulsion is too weak to explain a barrier of $12\,\mathrm{kJ\,mol^{-1}}$. The origin of the torsional barrier is still debated in quantum chemistry, and there are two main views:

| View | Main point | Representative work |
|---|---|---|
| **Hyperconjugation** | In the staggered conformation the bonding orbital $\sigma_{\ce{C-H}}$ on one carbon overlaps best with the antibonding orbital $\sigma^*_{\ce{C-H}}$ on the other carbon in the antiperiplanar position, and electron delocalization stabilizes the staggered conformation ($\sigma\to\sigma^*$ hyperconjugation of [6.5.2](/6.5.2#def-2.6.1)); when this interaction is "switched off" in the calculation, the staggered conformation is no longer more stable | Pophristic and Goodman, *Nature* 2001 |
| Steric (Pauli) repulsion | In the eclipsed conformation the bonding electron pairs of the $\ce{C-H}$ bonds approach each other, and Pauli exchange repulsion raises the energy of the eclipsed conformation; hyperconjugation plays only a minor role | Bickelhaupt and Baerends, *Angew. Chem.* 2003; Mo and Gao, *Acc. Chem. Res.* 2007 |

The root of the disagreement is that the total energy (calculated values agree with experiment) can be decomposed in different ways into "electrostatic", "exchange repulsion" and "orbital interaction" terms; the decomposition is not unique, and the individual terms do not correspond to observables. In the applications of this course the two models give the same qualitative conclusions (the staggered conformation is stable and the barrier increases with the size of the substituents), and we use whichever is needed: the hyperconjugation picture is more useful for cases involving strong acceptor orbitals such as 1,2-difluoroethane (4.2.4).

### 4.2.3. Propane and Butane

The barrier to rotation about the $\ce{C1-C2}$ bond of propane is $14\,\mathrm{kJ\,mol^{-1}}$: in the eclipsed conformation there are two $\ce{H/H}$ eclipsing pairs ($2\times 4$) and one $\ce{CH3/H}$ pair (about $6\,\mathrm{kJ\,mol^{-1}}$).

For rotation about the $\ce{C2-C3}$ bond of butane, the conformation is described by the torsion angle of $\ce{C1-C2-C3-C4}$, and there are four extreme conformations:

| Conformation | $\varphi$ | Relative energy / $(\mathrm{kJ\,mol^{-1}})$ | Origin |
|---|---|---|---|
| Anti (ap) | $180^\circ$ | $0$ | The two methyl groups are as far apart as possible |
| Gauche (sc) | $\pm 60^\circ$ | $3.8$ | Steric repulsion between two methyl groups that are fairly close |
| Partially eclipsed (ac) | $\pm 120^\circ$ | $16$ | Two $\ce{CH3/H}$ eclipsing pairs $+$ one $\ce{H/H}$ pair: $6 + 6 + 4$ |
| Fully eclipsed (syn, sp) | $0^\circ$ | $19$ | One $\ce{CH3/CH3}$ eclipsing pair (about $11$) $+$ two $\ce{H/H}$ pairs: $11 + 4 + 4$ |

Values for the fully eclipsed conformation in the literature range from $19$ to $25\,\mathrm{kJ\,mol^{-1}}$, and the commonly used $19\,\mathrm{kJ\,mol^{-1}}$ is taken here. The gauche and partially eclipsed conformations have different sources of energy: the former is steric repulsion between two groups on different carbons that are too close, the latter is mainly torsional strain.

**Definition 4.2.4 (Steric Strain)** The repulsion energy produced when atoms or groups that are not directly bonded come closer than the sum of their van der Waals radii is called **steric strain** (also called steric repulsion or van der Waals strain). The repulsion between the two methyl groups in the gauche conformation of butane is called the gauche interaction and is about $3.8\,\mathrm{kJ\,mol^{-1}}$; it is the basic unit for estimating the energies of substituted cyclohexanes in 4.6.

**Example 4.2.1** Estimate the ratio of the anti and gauche conformations of butane at $298\,\mathrm{K}$.

**Solution** The barrier between the two conformations is low, the conformations are at equilibrium, and the populations obey the Boltzmann distribution. The gauche conformation has two forms, $\varphi = +60^\circ$ and $-60^\circ$ (mirror images of equal energy), so

$$
K = \frac{[\text{gauche}]}{[\text{anti}]} = 2\exp\left(-\frac{3.8\times 10^3}{8.314\times 298}\right) = 2\times 0.216 = 0.43,
$$
that is, the anti conformation accounts for about $70\%$ and the gauche conformation for about $30\%$. The factor 2 comes from the degeneracy and corresponds to an entropy contribution $R\ln 2$.

As the temperature rises, the proportion of the gauche conformation increases toward $2/3$; only the conformations at the three energy minima are counted here, which is a very good approximation at room temperature.

### 4.2.4. The Gauche Effect and Intramolecular Hydrogen Bonds

In general, the energy is lowest when large groups are anti. But conformational analysis must take into account every factor that affects the energy, and there are two important kinds of exceptions.

**Definition 4.2.5 (Gauche Effect)** For molecules of the type $\ce{X-CH2-CH2-Y}$ (X and Y being highly electronegative atoms or groups such as F, OR, $\ce{NR3+}$), the phenomenon that the gauche conformation is more stable than the anti conformation is called the **gauche effect**.

The most typical example is 1,2-difluoroethane: in the gas phase the gauche conformation is about $2$–$4\,\mathrm{kJ\,mol^{-1}}$ lower than the anti conformation. The explanation by **hyperconjugation** is that in the gauche conformation each $\ce{C-F}$ bond is antiperiplanar to a $\ce{C-H}$ bond on the other carbon, so two $\sigma_{\ce{C-H}}\to\sigma^*_{\ce{C-F}}$ donations are possible, whereas in the anti conformation $\ce{C-F}$ is antiperiplanar to $\ce{C-F}$ and $\ce{C-H}$ to $\ce{C-H}$. Among the possible combinations $\sigma_{\ce{C-H}}\to\sigma^*_{\ce{C-F}}$ is the most favorable: the stabilization from an orbital interaction is inversely proportional to the energy difference, and $\sigma_{\ce{C-H}}$ is a better donor than $\sigma_{\ce{C-F}}$ (higher in energy), $\sigma^*_{\ce{C-F}}$ is a better acceptor than $\sigma^*_{\ce{C-H}}$ (lower in energy, with a coefficient larger on carbon), and the antiperiplanar arrangement gives maximum overlap. The gauche effect is common in biomolecules: the $\ce{O-C-C-O}$ fragment of ribose and the $\ce{N+-C-C-O}$ fragment of acetylcholine both prefer the gauche conformation.

The second kind of exception is the intramolecular **hydrogen bond**. Ethane-1,2-diol exists mainly in a gauche conformation in the gas phase, in which the two hydroxyl groups can form an $\ce{O-H\cdots O}$ hydrogen bond; in water the intramolecular hydrogen bond is replaced by hydrogen bonds to the solvent and this advantage is weakened. When the substituents are bulky, hydrogen bonding and steric repulsion compete, and the preferred conformation may be one with no intramolecular hydrogen bond in which the large groups are anti to each other; they must be compared case by case.

![Newman projections for the gauche effect and the intramolecular hydrogen bond. Left: gauche 1,2-difluoroethane, in which each C–F bond is antiperiplanar to a C–H bond on the other carbon (the two pairs in matching colours), giving two σ(C–H) → σ*(C–F) donations; middle: in the anti conformer F is anti to F and H to H; right: gauche ethane-1,2-diol, with an O–H···O hydrogen bond between the two hydroxyl groups (dotted)](./plots/gauche-effect.py)

### 4.2.5. Long-Chain Alkanes: Zigzag Chains, Helices and Physical Properties

When every $\ce{C-C}$ bond of a long-chain unbranched alkane is anti, the carbon chain lies in one plane in a zigzag; this is the lowest-energy conformation in the crystal and in the gas phase. In the liquid about $30\%$ of the bonds are gauche (Example 4.2.1) and the chain is coiled.

Perfluoroalkanes are different. The carbon chain of polytetrafluoroethylene (PTFE) is not a planar zigzag but is twisted into a helix: each $\ce{C-C-C-C}$ torsion angle deviates from $180^\circ$ by about $15^\circ$–$17^\circ$, and below $19\,^\circ\mathrm{C}$ about 13 $\ce{CF2}$ units make a half turn (the "13/6 helix"). The main reason is steric repulsion: the van der Waals radius of F (about $147\,\mathrm{pm}$) is larger than that of H ($120\,\mathrm{pm}$), and in a planar zigzag chain two F atoms on carbons one apart (1,3 positions) are about $250\,\mathrm{pm}$ apart, less than the sum of the radii; when the chain twists they move apart. The molecule contains no $\ce{C-H}$ bonds, so there is no $\sigma_{\ce{C-H}}\to\sigma^*_{\ce{C-F}}$ hyperconjugation here; calculations show that $\sigma_{\ce{C-C}}\to\sigma^*_{\ce{C-F}}$ hyperconjugation also favors the twist and is a minor factor. The helix makes the PTFE molecule a rigid rod uniformly sheathed in F, which is related to its low surface energy and chemical inertness.

Between alkane molecules there are only dispersion forces (**van der Waals forces**), and the boiling point rises with the size of the molecule; among isomers, the more branched, the closer the molecule is to a sphere and the smaller the surface available for contact, so the lower the boiling point. The melting point also depends on the packing of molecules in the crystal: the melting points of unbranched alkanes alternate between odd and even carbon numbers (the zigzag chains with an even number of carbons are arranged symmetrically at the ends and pack more tightly), and the highly symmetrical neopentane has an anomalously high melting point.

| Compound | Boiling point / $^\circ\mathrm{C}$ | Melting point / $^\circ\mathrm{C}$ |
|---|---|---|
| Pentane | $36.1$ | $-129.7$ |
| Isopentane (2-methylbutane) | $27.8$ | $-159.8$ |
| Neopentane (2,2-dimethylpropane) | $9.5$ | $-16.4$ |

## 4.3. Heats of Combustion and Ring Strain

### 4.3.1. Comparing Stability by Heats of Combustion

The most direct data for comparing the thermodynamic stability of isomers is the **standard enthalpy of combustion**: isomers burn to the same products, so the less heat is released on combustion, the lower the enthalpy of the molecule itself and the more stable it is. The values in the table are calculated from the standard enthalpies of formation in the CRC (gaseous hydrocarbons, $25\,^\circ\mathrm{C}$, products $\ce{CO2(g)}$ and $\ce{H2O(l)}$).

| Alkane | $-\Delta_{\mathrm{c}}H^\circ/(\mathrm{kJ\,mol^{-1}})$ | Alkane | $-\Delta_{\mathrm{c}}H^\circ/(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|
| Methane | $890.6$ | Butane | $2877.6$ |
| Ethane | $1560.5$ | Isobutane | $2869.0$ |
| Propane | $2220.0$ | Pentane | $3535.6$ |
| Hexane | $4195.0$ | Neopentane | $3514.5$ |

Two regularities: each additional $\ce{CH2}$ in a homologous series increases the enthalpy of combustion by about $658.6\,\mathrm{kJ\,mol^{-1}}$ (the reference value for a "strain-free $\ce{CH2}$"); and branched alkanes are more stable than unbranched ones, isobutane being $8.6\,\mathrm{kJ\,mol^{-1}}$ lower than butane and neopentane $21\,\mathrm{kJ\,mol^{-1}}$ lower than pentane. Why branching is more stable is still explained in different ways (for example correlation between carbons in 1,3 positions, "protobranching"), which does not affect our use of this experimental fact.

### 4.3.2. Baeyer Strain Theory and Its Failure

In 1885 Baeyer assumed that cycloalkanes are planar regular polygons. The ideal bond angle of an $\mathrm{sp^3}$ carbon is $109.5^\circ$, and the interior angle of a planar regular polygon is $180^\circ - 360^\circ/n$: $60^\circ$ for cyclopropane, $90^\circ$ for cyclobutane, $108^\circ$ for cyclopentane, $120^\circ$ for cyclohexane, and so on. He therefore inferred that cyclopentane has the least strain, that cyclopropane and cyclobutane have great strain, and that rings larger than six-membered become more and more strained as the ring grows and can hardly exist.

This inference can be tested with heats of combustion. Divide the heat of combustion of a cycloalkane $(\ce{CH2})_n$ by $n$, compare with the strain-free $658.6\,\mathrm{kJ\,mol^{-1}}$, and multiply the excess by $n$ to obtain the ring strain energy.

| $n$ | Cycloalkane | $-\Delta_{\mathrm{c}}H^\circ/(\mathrm{kJ\,mol^{-1}})$ | Per $\ce{CH2}$ | Strain energy / $(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|---|
| 3 | Cyclopropane | $2091$ | $697$ | $115$ |
| 4 | Cyclobutane | $2744$ | $686$ | $110$ |
| 5 | Cyclopentane | $3320$ | $664$ | $27$ |
| 6 | Cyclohexane | $3953$ | $659$ | $1$ |
| 7 | Cycloheptane | $4637$ | $662$ | $27$ |
| 8 | Cyclooctane | $5310$ | $664$ | $41$ |
| 9 | Cyclononane | $5981$ | $665$ | $54$ |
| 10 | Cyclodecane | $6636$ | $664$ | $50$ |
| 14 | Cyclotetradecane | $9220$ | $659$ | $0$ |

![Strain energies of cycloalkanes (numbers on the bars) and heats of combustion per CH2 (numbers below the bars); the dashed line is the Baeyer estimate assuming planar rings and counting only angle strain (normalized to cyclopropane)](./plots/ring-strain.py)

The experimental results agree with Baeyer's inference only for small rings: cyclohexane has almost no strain (about $1\,\mathrm{kJ\,mol^{-1}}$, within the error of the data), the strain of large rings does not increase with ring size, and the fourteen-membered ring is back to zero. The reason is that apart from cyclopropane, cycloalkanes are not planar: once the carbon atoms leave a common plane, the bond angles can approach $109.5^\circ$. The error of Baeyer's theory lies in the planarity assumption and not in the idea that "deviation of bond angles causes strain".

### 4.3.3. Sources of Strain

**Definition 4.3.1 (Angle Strain)** The rise in energy caused by the deviation of a bond angle from the ideal angle of the hybrid orbitals is called **angle strain** (also called Baeyer strain).

**Definition 4.3.2 (Ring Strain)** The excess energy of a cyclic molecule over the corresponding strain-free reference structure is called **ring strain**. It is the sum of angle strain, torsional strain and steric strain and is determined from heats of combustion or enthalpies of formation.

The three kinds of strain contribute differently in rings of different size: angle strain dominates in three- and four-membered rings; torsional strain dominates in five- and seven-membered rings; steric strain across the ring dominates in medium rings of eight to eleven members (the inward-pointing H atoms on opposite sides of the ring crowd each other, called transannular strain), which also makes medium rings difficult to synthesize; large rings of twelve or more members can adopt fully staggered conformations like open-chain alkanes, and the strain is close to zero.

## 4.4. Small Rings and the Five-Membered Ring

### 4.4.1. Cyclopropane

Cyclopropane is the only planar cycloalkane. The angle between the lines joining the three carbon nuclei is only $60^\circ$, whereas $\mathrm{sp^3}$-type orbitals of carbon cannot subtend $60^\circ$: calculations show that the angle between the ring-forming orbitals is about $104^\circ$, and the orbitals of two carbons overlap outside the line joining the nuclei rather than along it, forming a *bent bond* (colloquially a "banana bond"). Such overlap is poor, and the $\ce{C-C}$ bond is weaker than an ordinary $\sigma$ bond; the ring-forming orbitals have more p character and the $\ce{C-H}$ bonds have more s character (the $\ce{H-C-H}$ angle is about $115^\circ$, the $\ce{C-H}$ bond is shorter and more acidic). In addition the six H atoms of the ring are exactly eclipsed in pairs, giving torsional strain. The total strain is $115\,\mathrm{kJ\,mol^{-1}}$ ($27.6\,\mathrm{kcal\,mol^{-1}}$).

![Bent bonds of cyclopropane: the internuclear angle is 60° (dashed lines), while the two ring-forming hybrid orbitals of each carbon make an angle of about 104°, so the orbitals of neighbouring carbons overlap outside the internuclear line (blue); the solid curves show the bent bond paths](./plots/cyclopropane-bent-bonds.py)

The strain makes the chemistry of cyclopropane somewhat like that of alkenes: it undergoes ring-opening by catalytic hydrogenation and ring-opening addition with $\ce{Br2}$ and HBr (radical ring opening of small rings is in [6.5.7](/6.5.7#sec-7.9.3)). The strain can be seen directly from the heats of hydrogenation:

| Reaction | $\Delta_{\mathrm{r}}H^\circ/(\mathrm{kJ\,mol^{-1}})$ | Conditions |
|---|---|---|
| Cyclopropane $+ \ce{H2} \to$ propane | $-157$ | Ni or Pd, room temperature to $80\,^\circ\mathrm{C}$ |
| Cyclobutane $+ \ce{H2} \to$ butane | $-153$ | Ni, about $200\,^\circ\mathrm{C}$ |
| Cyclopentane $+ \ce{H2} \to$ pentane | $-70$ | No reaction under ordinary conditions |
| Cyclohexane $+ \ce{H2} \to$ hexane | $-44$ | No reaction under ordinary conditions |

(Calculated from the gas-phase standard enthalpies of formation in the CRC.) The heat of hydrogenation is approximately $-44\,\mathrm{kJ\,mol^{-1}}$ minus the ring strain: the greater the strain, the more heat released on ring opening. But whether a reaction occurs also depends on kinetics: cyclopropane and cyclobutane have almost the same strain, yet cyclopropane reacts much more easily because its bent bonds interact more readily with the metal surface.

Small rings are useful in synthesis and drug design. The three-membered ring "locks" the *cis*/*trans* relation of substituents: two substituents on a cyclopropane cannot change their relative position by isomerization as they can at a double bond. When a cyclopropyl group is conjugated with an adjacent π system or a **carbocation**, the plane of the cyclopropyl group tends to bisect the adjacent p orbital (the bisected conformation), in which the bent $\ce{C-C}$ bonds of the ring overlap best with the p orbital; the cyclopropylmethyl cation is therefore unusually stable ([6.5.8](/6.5.8#sec-8.3.2)).

### 4.4.2. Cyclobutane

Planar cyclobutane would have little angle strain ($90^\circ$), but all 8 H atoms would be eclipsed. Real cyclobutane folds into a "butterfly" shape with an angle of about $25^\circ$ between the two three-carbon planes: the bond angle decreases to about $88^\circ$ and the angle strain increases slightly, but adjacent $\ce{C-H}$ bonds are partly staggered and the torsional strain decreases. The two folded conformations interconvert rapidly through a planar transition state, with a barrier of only about $6\,\mathrm{kJ\,mol^{-1}}$. The total strain is $110\,\mathrm{kJ\,mol^{-1}}$ ($26.3\,\mathrm{kcal\,mol^{-1}}$), and the ring also has some bent-bond character.

### 4.4.3. Cyclopentane

The interior angle of $108^\circ$ of planar cyclopentane has almost no angle strain, but there are 10 eclipsed $\ce{C-H}$ pairs and the torsional strain is about $40\,\mathrm{kJ\,mol^{-1}}$. Real cyclopentane lets one carbon leave the plane of the other four (the *envelope conformation*) or puts two adjacent carbons on opposite sides of the plane (the *half-chair conformation*), which partly removes the torsional strain, and the total strain falls to $27\,\mathrm{kJ\,mol^{-1}}$. The two conformations have almost the same energy, and the "puckered" position is passed along the ring continuously with almost no barrier to cross, a motion called *pseudorotation*. Five-membered rings are therefore very flexible; five-membered rings are widespread in natural products and drugs (furanoses, proline, prostaglandins), and their conformations are often determined by the substituents.

![Non-planar conformations of small rings and of cyclohexene (carbon skeletons only, viewed nearly edge-on): puckered cyclobutane; the envelope (one carbon out of the plane of the other four) and half-chair (two adjacent carbons on opposite sides of the plane of the other three) of cyclopentane, generated from the Cremer–Pople formula with a puckering amplitude of 0.43 Å; the half-chair of cyclohexene (MMFF-optimised), with C1, C2, C3 and C6 coplanar and C4 and C5 on opposite sides. Red: above the reference plane, blue: below, grey: in it](./plots/small-rings-3d.py)

## 4.5. Cyclohexane

### 4.5.1. The Chair Conformation

If cyclohexane were planar, it would have six $120^\circ$ bond angles and 12 eclipsed $\ce{C-H}$ pairs. Moving C1 and C4 to opposite sides of the plane gives a conformation with neither angle strain nor torsional strain.

**Definition 4.5.1 (Chair Conformation)** The conformation of cyclohexane in which the six carbons lie alternately in two parallel planes, all $\ce{C-C-C}$ bond angles are about $111^\circ$ and all bonds on adjacent carbons are staggered is called the **chair conformation**.

The $\ce{C-C-C}$ bond angle of chair cyclohexane is measured to be $111.4^\circ$ (electron diffraction), slightly larger than $109.5^\circ$, and the ring torsion angles are about $55^\circ$; viewed along any $\ce{C-C}$ bond, the Newman projection is staggered. Chair cyclohexane has almost no strain, which is exactly what the heat of combustion data show.

**Definition 4.5.2 (Axial and Equatorial Bonds)** Of the two bonds on each carbon of chair cyclohexane, the one parallel to the symmetry axis of the ring (the $C_3$ axis perpendicular to the mean plane) is called the **axial bond** (a bond), and the one that points outward roughly along the mean plane of the ring is called the **equatorial bond** (e bond).

The six axial bonds point alternately up and down: the three carbons in the "upper layer" have axial bonds pointing up and the three in the "lower layer" have axial bonds pointing down. The three axial H atoms on the same side are about $250\,\mathrm{pm}$ apart, just slightly more than the sum of the van der Waals radii, so there is no repulsion in cyclohexane itself; but if one of these H atoms is replaced by a larger group, the repulsion appears (4.6).

![Three-dimensional structures of chair and boat cyclohexane. Left: chair, axial H in red and equatorial H in blue; right: boat, the two "flagpole" H atoms in orange](./plots/cyclohexane-3d.py)

### 4.5.2. Boat and Twist-Boat Conformations

Flipping C4 of the chair to the same side as C1 gives the *boat conformation*. The boat has no angle strain but two problems: the $\ce{C-H}$ bonds on the C2–C3 and C5–C6 bonds are exactly eclipsed (torsional strain), and the two inward-pointing "flagpole" H atoms on C1 and C4 are only about $183\,\mathrm{pm}$ apart, far less than $240\,\mathrm{pm}$ (steric strain). The boat is about $29\,\mathrm{kJ\,mol^{-1}}$ above the chair and is not an energy minimum. A slight twist of the boat moves the flagpole H atoms apart and reduces the eclipsing, giving the lower-energy *twist-boat conformation*, about $23\,\mathrm{kJ\,mol^{-1}}$ above the chair, which is a true (but very shallow) energy minimum. The population of the twist-boat at room temperature is about $\exp(-23/2.48)\approx 10^{-4}$ and can be neglected.

### 4.5.3. Ring Flip

**Definition 4.5.3 (Ring Flip)** The process by which one chair conformation converts to the other chair conformation through intermediate conformations such as the half-chair and twist-boat is called the **ring flip** (also called ring inversion). After a ring flip, all the former axial bonds become equatorial and all the equatorial bonds become axial; bonds that pointed up still point up.

![Energy diagram of the ring flip of cyclohexane: the chair passes through a half-chair transition state to a twist-boat, two twist-boats are connected through the boat, and the ring then flips to the other chair (energies in kJ/mol)](./plots/ring-flip-energy.py)

The barrier of the ring flip (half-chair transition state) is about $45\,\mathrm{kJ\,mol^{-1}}$ ($10.8\,\mathrm{kcal\,mol^{-1}}$). By the Eyring equation the rate constant at $25\,^\circ\mathrm{C}$ is about $10^5\,\mathrm{s^{-1}}$, so at room temperature the axial and equatorial H atoms of cyclohexane give only one averaged peak in the ¹H NMR spectrum; only when the sample is cooled to about $-100\,^\circ\mathrm{C}$ is the ring flip slower than the NMR time scale and the two kinds of H give separate peaks (dynamic NMR, [6.4.12](/6.4.12)). This is how the barrier of the ring flip is measured.

### 4.5.4. Drawing the Chair Conformation

Drawing the chair conformation well is the most practical skill of this chapter. Follow these steps (Klein's method):

1. Draw two parallel, slightly inclined lines as the two sides of the "seat" of the chair, one end slightly higher;
2. Add a "tip" at one end pointing up and one at the other end pointing down (the head and foot), so that the six edges form three pairs of parallel lines;
3. Draw the axial bonds first: identify the three carbons that point up and the three that point down; the axial bond of an up carbon points vertically up and that of a down carbon vertically down;
4. Then draw the equatorial bonds: each equatorial bond is parallel to the two ring edges that are one carbon away, pointing outward and roughly opposite to the axial bond (the equatorial bond of an up carbon points slightly down).

A common mistake is to draw an equatorial bond as a horizontal line or parallel to an adjacent ring edge. In drawing the two chairs of a substituted cyclohexane, first determine from the planar structure (wedge formula) whether each substituent is "above" or "below" the ring and draw the first chair keeping these relations; then draw the other chair with the tips pointing the other way, keeping the position numbers and the above/below relations of the substituents, with a and e interchanged.

![The standard drawing obtained by projecting the three-dimensional chair: axial bonds in red, equatorial bonds in blue. After the ring flip the methyl group on C1 changes from equatorial to axial but remains on the same side of the ring (the other bond on C1 is always H)](./plots/chair-flip-2d.py)

## 4.6. Substituted Cyclohexanes

### 4.6.1. Monosubstituted Cyclohexanes and A Values

The two chair conformations of methylcyclohexane are no longer equivalent. When the methyl group is axial it comes very close to the axial H atoms on C3 and C5 on the same side; when it is equatorial it points away from the ring. This is seen more clearly in a Newman projection: viewed along the C1–C2 bond, the equatorial methyl group is anti to C3 on the ring, and the axial methyl group is gauche to C3, equivalent to one gauche interaction of butane; the same holds when viewed along the C1–C6 bond.

![Newman projection of methylcyclohexane along the C1–C2 bond: the equatorial methyl group is anti to C3 and the axial methyl group is gauche to C3](./plots/methylcyclohexane-newman.py)

**Definition 4.6.1 (1,3-Diaxial Interaction)** The steric repulsion between an axial substituent on cyclohexane and the axial atoms or groups on C3 and C5 on the same side is called the **1,3-diaxial interaction**.

An axial methyl group has two 1,3-diaxial $\ce{CH3/H}$ interactions, equivalent to two gauche interactions of butane, estimated as $2\times 3.8 = 7.6\,\mathrm{kJ\,mol^{-1}}$, very close to the experimental value of $7.3\,\mathrm{kJ\,mol^{-1}}$.

**Definition 4.6.2 (A Value)** In a monosubstituted cyclohexane, the decrease in standard Gibbs energy when the substituent goes from the axial to the equatorial position, that is, $-\Delta G^\circ$ of the equilibrium a ⇌ e, is called the **A value** of the substituent.

**Formula 4.6.1** The ratio of the two conformations from the A value:

$$
K = \frac{[\mathrm{e}]}{[\mathrm{a}]} = \exp\left(\frac{A}{RT}\right), \qquad x_{\mathrm{e}} = \frac{K}{1+K}. \tag{4.1}
$$

For methyl $A = 7.3\,\mathrm{kJ\,mol^{-1}}$, so at $298\,\mathrm{K}$, $K = 19$ and the equatorial conformation accounts for $95\%$. A values of common substituents (representative values from Eliel's compilation, differing slightly with the solvent):

| Substituent | $A/(\mathrm{kJ\,mol^{-1}})$ | Substituent | $A/(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|---|
| $\ce{-F}$ | $1.0$ | $\ce{-CN}$ | $0.8$ |
| $\ce{-Cl}$ | $1.8$ | $\ce{-C#CH}$ | $1.7$ |
| $\ce{-Br}$ | $1.6$–$2.0$ | $\ce{-COOH}$ | $5.9$ |
| $\ce{-I}$ | $1.8$ | $\ce{-CH3}$ | $7.3$ |
| $\ce{-OH}$ | $2.5$–$4.2$ (depending on solvent) | $\ce{-CH2CH3}$ | $7.5$ |
| $\ce{-OCH3}$ | $2.5$ | $\ce{-CH(CH3)2}$ | $9.2$ |
| $\ce{-NH2}$ | $5.0$–$6.7$ | $\ce{-C6H5}$ | $11.7$ |
| | | $\ce{-C(CH3)3}$ | ca. $20$ |

![Fraction of the equatorial conformation at 298 K as a function of the A value (Eq. (4.1))](./plots/a-value-boltzmann.py)

Several points in the table deserve attention:

- The A values of the halogens are all small and close to one another: the larger the atom, the longer the $\ce{C-X}$ bond, and the two effects largely cancel.
- Ethyl is almost the same as methyl and isopropyl is only slightly larger: the ethyl group can rotate about the $\ce{C1-C\alpha}$ bond so that its methyl group points away from the ring, and in the axial position it still meets only an H. The *tert*-butyl group cannot do this; it always has one methyl group pointing toward the axial H atoms on C3 and C5, and the A value increases sharply.
- The linear $\ce{-C#CH}$ and $\ce{-CN}$ groups are not small, but they are slender and far from the ring, and their A values are small.

The equilibrium constant of *tert*-butyl is about $3\times10^{3}$, so it is almost completely equatorial and "locks" the ring in one chair. 4-*tert*-Butylcyclohexane derivatives are therefore often used as conformationally locked models to measure separately the reactivity of axial and equatorial groups (the method of Winstein and Eliel); the **E2** elimination of [6.5.9](/6.5.9#sec-9.4.4) and the reduction selectivity of [6.5.17](/6.5.17#sec-17.1.2) both use them.

### 4.6.2. Disubstituted Cyclohexanes

Disubstituted cyclohexanes show *cis*–*trans* isomerism ([6.5.5](/6.5.5#sec-5.1.1)): two substituents on the same side of the ring plane are *cis* and those on opposite sides are *trans*. *Cis* and *trans* are configurations and cannot be changed by a ring flip; each configuration has two chair conformations. Drawing them one by one gives the following table (a for axial, e for equatorial):

| Positions | Two chairs of the *cis* isomer | Two chairs of the *trans* isomer | More stable isomer |
|---|---|---|---|
| 1,2- | a,e ⇌ e,a | e,e ⇌ a,a | *trans* |
| 1,3- | e,e ⇌ a,a | a,e ⇌ e,a | *cis* |
| 1,4- | a,e ⇌ e,a | e,e ⇌ a,a | *trans* |

The principle for judging the preferred conformation: as far as the configuration allows, put as many substituents as possible in equatorial positions; when this cannot be satisfied for all, put the group with the larger A value in the equatorial position. Energies can be estimated by adding A values and gauche interactions.

**Example 4.6.1** Estimate the energy difference between the two chairs of each isomer of dimethylcyclohexane.

**Solution** Taking the gauche interaction ($3.8\,\mathrm{kJ\,mol^{-1}}$) as the unit:

- *trans*-1,2-Dimethyl: in the e,e conformation the two adjacent equatorial methyl groups are gauche to each other (1 interaction, $3.8$); in the a,a conformation each axial methyl group has 2 1,3-diaxial interactions (4 in all, $15.2$), and the two methyl groups are anti to each other. The difference is about $11\,\mathrm{kJ\,mol^{-1}}$, and the e,e conformation accounts for more than $99\%$.
- *cis*-1,2-Dimethyl: both chairs are a,e and have the same energy (each $3 \times 3.8 = 11.4$: 2 interactions of the axial methyl group plus 1 between the two methyl groups); the two conformations are mirror images and each accounts for half. The *trans* isomer is therefore more stable than the *cis* by about $7.6\,\mathrm{kJ\,mol^{-1}}$, the experimental value being $7.8\,\mathrm{kJ\,mol^{-1}}$.
- *cis*-1,3-Dimethyl: the e,e conformation has no interaction; in the a,a conformation the two axial methyl groups are on the same side and 1,3-diaxial to each other, and this one $\ce{CH3/CH3}$ interaction is about $15\,\mathrm{kJ\,mol^{-1}}$, for a total difference of about $23\,\mathrm{kJ\,mol^{-1}}$, so the molecule is almost entirely e,e. *cis*-1,3 is more stable than *trans*-1,3 (a,e, $7.6$).

![The two chairs of each dimethylcyclohexane in Example 4.6.1: on ring flip each methyl group stays on its side of the ring (up or down) while axial (a) and equatorial (e) are exchanged; the numbers in parentheses are the strain counted in gauche interactions (3.8 kJ/mol each), with about 15 kJ/mol for a CH₃/CH₃ 1,3-diaxial interaction](./plots/dimethylcyclohexane-chairs.py)

**Example 4.6.2** Draw the preferred conformations of *cis*- and *trans*-1-*tert*-butyl-4-chlorocyclohexane.

**Solution** The A value of *tert*-butyl is much larger than that of Cl, and *tert*-butyl is equatorial in both isomers. *trans*: *tert*-butyl e, Cl e, both substituents equatorial; *cis*: *tert*-butyl e, and Cl can only be axial. Because of the locking by *tert*-butyl, these two compounds are "pure" models of equatorial chlorine and axial chlorine, respectively.

### 4.6.3. Polysubstituted Cyclohexanes

The principle is the same for polysubstitution. "All-equatorial" structures are common among natural products, and they are the most stable of the isomers. For example, all three substituents of menthol ((1R,2S,5R)-2-isopropyl-5-methylcyclohexan-1-ol) are equatorial, and it is the most stable of the eight stereoisomers; all five substituents on the pyranose ring of β-D-glucose are equatorial, which is one reason why it is the most common in nature ([6.5.32](/6.5.32)).

```smiles
CC(C)[C@@H]1CC[C@@H](C)C[C@H]1O (−)-menthol
```

## 4.7. Cyclohexene, Fused Rings and Cage Compounds

### 4.7.1. Cyclohexene

When the ring contains $\mathrm{sp^2}$ carbons the chair is no longer possible: the $\ce{C=C}$ and the two carbons attached to it (C1, C2, C3, C6) must be coplanar, and the other two carbons lie on opposite sides of the plane, giving a half-chair. The bonds on C3 and C6 are of two kinds, pseudo-axial and pseudo-equatorial; the ring-flip barrier is about $22\,\mathrm{kJ\,mol^{-1}}$, much lower than that of cyclohexane. The carbonyl carbon of cyclohexanone is also $\mathrm{sp^2}$, and its ring is slightly flatter than that of cyclohexane.

### 4.7.2. Decalin

Decalin (bicyclo[4.4.0]decane) is formed by fusing two cyclohexane rings along one bond, and the two bridgehead hydrogens can be on the same side (*cis*) or opposite sides (*trans*). The two are configurational isomers, not conformers.

- *trans*-Decalin: both rings are chairs, and each ring is connected to the other by two equatorial bonds. It cannot ring-flip: a flip would make both of these bonds axial, and two adjacent axial bonds point in opposite directions (an angle of $180^\circ$) and could no longer be joined into a six-membered ring. *trans*-Decalin is conformationally rigid.
- *cis*-Decalin: each ring is connected to the other by one axial and one equatorial bond, and the two rings can flip simultaneously (barrier about $52\,\mathrm{kJ\,mol^{-1}}$), giving after the flip a conformation of the same energy as before.

The *trans* isomer is more stable than the *cis* by about $11\,\mathrm{kJ\,mol^{-1}}$. Counting gauche interactions: regarding one ring as two substituents on the other ring, the axial "substituent" in the *cis* isomer has three gauche interactions with the other ring ($3 \times 3.8 = 11.4$), and the *trans* isomer has none.

![Carbon skeletons of trans- and cis-decalin, adamantane and 5α-androstane (three-dimensional structures computed with RDKit; bridgehead H in orange, angular methyl groups in green)](./plots/polycyclic-3d.py)

### 4.7.3. Perhydrophenanthrene

Perhydrophenanthrene (tetradecahydrophenanthrene) consists of three cyclohexane rings fused angularly, has 4 bridgehead carbons (4a, 4b, 8a, 10a), and has 10 stereoisomers: 4 pairs of enantiomers and 2 meso compounds (the method of [6.5.5](/6.5.5#sec-5.4) can verify this). The most stable is the isomer in which all three rings are chairs and both fusions are *trans*, which is the arrangement of rings A, B and C of the steroid skeleton.

### 4.7.4. Adamantane

Adamantane ($\ce{C10H16}$) consists of four chair cyclohexane rings, with the 10 carbons arranged as a unit of the diamond lattice; it is a strain-free, highly symmetrical ($T_{\mathrm{d}}$) cage molecule with a melting point as high as $270\,^\circ\mathrm{C}$ (in a sealed tube). It was first isolated from petroleum (1933); in 1957 Schleyer prepared it in one step by the **carbocation** rearrangement of tetrahydrodicyclopentadiene catalyzed by $\ce{AlCl3}$ (for rearrangements see [6.5.30](/6.5.30)), and it has been a common reagent since. Diadamantane, triadamantane and so on, obtained by further fusing adamantane units, are collectively called diamondoids.

The adamantyl group is bulky, rigid and hydrophobic, and can be regarded as a "larger *tert*-butyl". 1-Aminoadamantane (amantadine) blocks the M2 proton channel of influenza A virus and prevents uncoating of the virus, and was used as an anti-influenza drug (most circulating strains are now resistant); its derivative memantine is an NMDA receptor antagonist used for Alzheimer's disease. In chemical biology, attaching an adamantyl group to a protein as a "hydrophobic tag" mimics the hydrophobic surface exposed by a misfolded protein and causes the protein quality control system of the cell to degrade the protein ([6.6](/6.6)).

### 4.7.5. Steroids

The skeleton of a steroid is cyclopenta[a]perhydrophenanthrene: three six-membered rings (A, B, C) and one five-membered ring (D) are fused, and the carbon atoms are numbered by special rules. In natural steroids the B/C and C/D fusions are almost always *trans*, and the A/B fusion has two forms: the *trans* 5α series (such as cholestanol and epiandrosterone, in which the whole skeleton is a nearly flat elongated strip) and the *cis* 5β series (such as the bile acids, in which ring A bends to one side). A substituent above the plane of the ring (on the same side as the angular methyl groups at C10 and C13) is denoted β and drawn with a solid wedge bond; one below is denoted α and drawn with a hashed wedge bond.

The all-*trans* fusion makes the steroid skeleton completely unable to ring-flip, and the axial or equatorial orientation of each substituent is fixed. For example, the 3β-OH of epiandrosterone (3β-hydroxy-5α-androstan-17-one) is equatorial. The stereoselectivity of steroid reactions (the reagent attacks from the less hindered α face) and the recognition of steroid hormones by receptors are both based on this rigid conformation.

```smiles
C[C@]12CC[C@H]3[C@H]([C@@H]1CCC2=O)CC[C@H]4C[C@@H](O)CC[C@]34C epiandrosterone
```

## Summary

| Topic | Main points |
|---|---|
| Classification | Constitutional isomerism and stereoisomerism; stereoisomers are divided into conformations (interconverted by rotation about single bonds) and configurations (bond breaking required); the boundary is set by the barrier (Definition 4.1.2) |
| Open chains | Staggered conformations are stable; ethane barrier $12$, butane anti $0$ / gauche $3.8$ / ac $16$ / syn $19\,\mathrm{kJ\,mol^{-1}}$; the gauche effect and intramolecular hydrogen bonds are exceptions (Definition 4.2.5) |
| Strain | The sum of angle strain, torsional strain and steric strain (Definitions 4.2.3, 4.2.4, 4.3.1) is the ring strain (Definition 4.3.2), determined from heats of combustion: three-membered $115$, four-membered $110$, five-membered $27$, six-membered $0\,\mathrm{kJ\,mol^{-1}}$ |
| Small rings | Cyclopropane planar, bent bonds, ring opens easily; cyclobutane folded; cyclopentane envelope and pseudorotation |
| Cyclohexane | The chair is strain-free ($111.4^\circ$); twist-boat $+23$, boat $+29$, ring-flip barrier $45\,\mathrm{kJ\,mol^{-1}}$; the ring flip interchanges a and e |
| Substituted cyclohexanes | A value (Definition 4.6.2) and Eq. (4.1): methyl $7.3\,\mathrm{kJ\,mol^{-1}}$, equatorial $95\%$; *tert*-butyl locks the conformation; large groups prefer equatorial |
| Fused rings | *trans*-Decalin is rigid and about $11\,\mathrm{kJ\,mol^{-1}}$ more stable than *cis*; steroids are all-*trans* fused; adamantane is strain-free |

It is worth remembering a few numbers for the conversion between energy and populations $K = \exp(-\Delta G^\circ/RT)$: at $298\,\mathrm{K}$ each increase of $5.7\,\mathrm{kJ\,mol^{-1}}$ in $\Delta G^\circ$ increases the equilibrium constant tenfold; $3.8\,\mathrm{kJ\,mol^{-1}}$ corresponds to about $4.6 : 1$ and $7.3\,\mathrm{kJ\,mol^{-1}}$ to $19 : 1$.

## Questions

1. Draw the Newman projections of all the staggered and eclipsed conformations of 2-methylbutane for rotation about the C2–C3 bond, estimate their relative energies with the interaction energies of 4.2.3, and identify the lowest- and highest-energy conformations.

   **Answer** The front carbon C2 carries H, $\ce{CH3}$ (C1) and $\ce{CH3}$; the rear carbon C3 carries H, H and $\ce{CH3}$ (C4). Three staggered conformations: when C4 is anti to the H on C2, C4 is gauche to both methyl groups (2 gauche interactions, $7.6\,\mathrm{kJ\,mol^{-1}}$); when C4 is anti to one of the methyl groups it is gauche to the other methyl group (1 interaction, $3.8\,\mathrm{kJ\,mol^{-1}}$), and there are two such conformations, of lowest energy. Three eclipsed conformations: C4 eclipsing H (the other two pairs being $\ce{CH3/H}$ and $\ce{CH3/H}$): $6 + 6 + 6 = 18\,\mathrm{kJ\,mol^{-1}}$; C4 eclipsing one of the methyl groups (the other two pairs $\ce{CH3/H}$ and $\ce{H/H}$): $11 + 6 + 4 = 21\,\mathrm{kJ\,mol^{-1}}$, and there are two such conformations, of highest energy.

2. Which of the following cycloalkanes can be ring-opened by catalytic hydrogenation under ordinary conditions: cyclopropane, cyclobutane, cyclopentane, cyclohexane, cyclooctane? How is the heat of hydrogenation related to ring strain?

   **Answer** Cyclopropane (Ni or Pd, room temperature to $80\,^\circ\mathrm{C}$) and cyclobutane (Ni, about $200\,^\circ\mathrm{C}$) can; rings of five or more members do not open under ordinary conditions. The heat of hydrogenation is approximately $-(44 + E_{\text{strain}})\,\mathrm{kJ\,mol^{-1}}$ (the table of 4.4.1; cyclooctane $-84$, strain $41$, also fits): the greater the strain, the more heat released. But the ease of reaction also depends on kinetics: although the hydrogenation of cyclooctane releases $84\,\mathrm{kJ\,mol^{-1}}$, there is no easy reaction pathway.

3. Use Newman projections to explain why in the chair conformation of cyclohexane the equatorial bond on C1 is anti to the C2–C3 bond and the axial bond is gauche to it. From this, explain how many gauche interactions of butane an axial methyl group in methylcyclohexane corresponds to.

   **Answer** See the Newman projection in 4.6.1: viewed along C1–C2, the ring torsion angle is about $55^\circ$ and C6 is gauche to C3; the other two positions on C1 are at $180^\circ$ (equatorial) and $60^\circ$ (axial) from C3. Viewed along C1–C6 the situation is the same (for C5). The axial methyl group therefore has one gauche interaction with each of C3 and C5, 2 in all, about $7.6\,\mathrm{kJ\,mol^{-1}}$, which is just the two 1,3-diaxial $\ce{CH3/H}$ interactions.

4. Draw the two chair conformations of each of the following compounds, decide which is more stable, and estimate the proportion of the preferred conformation at $298\,\mathrm{K}$: (a) *trans*-1-ethyl-2-methylcyclohexane; (b) *cis*-1-ethyl-3-methylcyclohexane; (c) *trans*-1-*tert*-butyl-4-methylcyclohexane.

   **Answer** (a) The e,e conformation (only 1 gauche interaction between Et and Me, $3.8$) is about $11\,\mathrm{kJ\,mol^{-1}}$ lower than the a,a conformation ($7.5 + 7.3 = 14.8$, the two groups anti to each other), $K \approx \exp(11/2.48) \approx 85$, and e,e accounts for about $99\%$. (b) The two conformations of *cis*-1,3 are e,e and a,a; in a,a the two groups are 1,3-diaxial with very large repulsion ($>20\,\mathrm{kJ\,mol^{-1}}$), and e,e is almost $100\%$. (c) *trans*-1,4 gives e,e and a,a; in a,a the *tert*-butyl group is axial (about $20$) plus the axial methyl ($7.3$), a difference of about $27\,\mathrm{kJ\,mol^{-1}}$, and e,e is almost $100\%$.

5. Draw the preferred conformation of the isomer of 1,2,4-trimethylcyclohexane in which the methyl groups are "1,2-*trans*, 1,4-*cis*" (the 1-methyl and 2-methyl groups *trans*, the 1-methyl and 4-methyl groups *cis*).

   **Answer** 1,2-*trans* requires C1 and C2 to be both e or both a; 1,4-*cis* requires one of C1 and C4 to be a and the other e. If C1 and C2 are e,e, then C4 must be a: there is only one axial methyl group ($7.3$) plus one gauche interaction between the C1 and C2 methyl groups ($3.8$), about $11\,\mathrm{kJ\,mol^{-1}}$. After the ring flip C1 and C2 are a,a and C4 is e: two axial methyl groups ($14.6$), which is less stable. The preferred conformation is therefore 1e, 2e, 4a, the two differing by about $3.5\,\mathrm{kJ\,mol^{-1}}$, a ratio of about $80 : 20$.

6. *trans*-Decalin is about $11\,\mathrm{kJ\,mol^{-1}}$ more stable than the *cis* isomer. If this much energy is supplied to *trans*-decalin, can it convert to the *cis* isomer? Can *cis*-decalin ring-flip?

   **Answer** No. *cis*- and *trans*-Decalin are configurational isomers (the relative configurations of the bridgehead H atoms differ), and their interconversion requires breaking $\ce{C-H}$ or $\ce{C-C}$ bonds, with a barrier far greater than $11\,\mathrm{kJ\,mol^{-1}}$; the $11\,\mathrm{kJ\,mol^{-1}}$ is only the difference in thermodynamic stability and has nothing to do with the barrier for conversion. *cis*-Decalin can ring-flip (the two rings flip simultaneously, barrier about $52\,\mathrm{kJ\,mol^{-1}}$), and *trans*-decalin cannot.

7. The ¹H NMR spectrum of cyclohexane at room temperature has only one peak ($\delta$ 1.43), but at $-100\,^\circ\mathrm{C}$ it splits into two groups of peaks. Explain the reason, and use the Eyring equation to estimate: if the chemical shifts of the two peaks differ by $\Delta\nu = 30\,\mathrm{Hz}$, what is the rate constant of the ring flip at which the two peaks just coalesce (at coalescence $k \approx \pi\Delta\nu/\sqrt2$)? From this find the Gibbs energy of activation at the coalescence temperature $T_{\mathrm{c}} \approx 210\,\mathrm{K}$.

   **Answer** The axial H and equatorial H are in different chemical environments, but the ring flip exchanges them at a rate of $10^5\,\mathrm{s^{-1}}$, much faster than the frequency difference between the two peaks, so the spectrometer sees only the averaged peak; at low temperature the ring flip slows down and the two kinds of H give separate peaks. At coalescence $k \approx \pi\times 30/\sqrt2 \approx 67\,\mathrm{s^{-1}}$. From $k = \frac{k_{\mathrm{B}}T}{h}\exp\left(-\frac{\Delta G^\ddagger}{RT}\right)$, $\Delta G^\ddagger = RT\ln\frac{k_{\mathrm{B}}T}{hk} = 8.314\times 210 \times \ln\frac{4.38\times 10^{12}}{67}\,\mathrm{J\,mol^{-1}} \approx 43\,\mathrm{kJ\,mol^{-1}}$, in agreement with the barrier of the ring flip.

8. In the series $\ce{X-CH2-CH2-X}$ the anti conformation predominates for X = Cl and Br, and the gauche conformation predominates for X = F. Explain the difference from the viewpoint of 4.2.4.

   **Answer** The stabilization of the gauche conformation comes from $\sigma_{\ce{C-H}}\to\sigma^*_{\ce{C-X}}$ hyperconjugation, which requires a low-energy $\sigma^*_{\ce{C-X}}$ and atoms small enough that the steric and electrostatic repulsion between the two X atoms in the gauche conformation is not large. The F atom is small and the $\ce{C-F}$ bond highly polar, so the gain from hyperconjugation exceeds the repulsion; the Cl and Br atoms are large, the van der Waals and dipole repulsion between the two halogens dominates in the gauche conformation, and the anti conformation is more stable.
