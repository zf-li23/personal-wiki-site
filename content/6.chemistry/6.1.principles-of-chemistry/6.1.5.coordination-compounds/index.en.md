---
title: Structure of Coordination Compounds
source_hash: 4a33ee9eda66
---

Coordination compounds (also called complexes) consist of a central atom bound to a set of ligands through coordinate bonds. They are the largest and most structurally varied class of inorganic compounds: the heme in hemoglobin is an Fe(II) complex, chlorophyll is a Mg(II) complex, cisplatin is an anticancer drug, and EDTA titrations, the hydrometallurgy of metals, and many industrial catalysts all depend on coordination. This chapter applies the structural theory of the preceding chapters to these compounds. We first introduce their composition, nomenclature, and types (5.1), then discuss geometries and isomerism (5.2) and magnetism (5.3). Two theories then explain their behavior: valence bond theory (5.4) extends the **hybrid orbitals** of [6.1.3](/6.1.3) to central atoms that use d orbitals, and crystal field theory (5.5) uses the splitting of the d orbitals in the electrostatic field of the ligands to account for magnetism, color, and thermodynamic properties in a single picture. The stability of complexes in solution (stability constants and complexation equilibria) is treated in [6.1.9](/6.1.9), the electrode potentials of complex couples in [6.1.11](/6.1.11), and the chemistry of transition-metal complexes in [6.1.15](/6.1.15). A rigorous treatment of ligand field theory, the molecular orbital theory of complexes, and term symbols is given in [Structural Chemistry](/6.2), and a systematic treatment of stereochemistry in [Organic Chemistry](/6.5).

## 5.1. Basic Concepts of Coordination Compounds

### 5.1.1. Composition of Complexes

In 1798 Tassaert prepared orange-yellow crystals of composition $\ce{CoCl3*6NH3}$. Why the already "saturated" $\ce{CoCl3}$ could bind six more $\ce{NH3}$ molecules remained unexplained for a century, until Werner proposed his coordination theory in 1893 (for which he received the 1913 Nobel Prize in Chemistry). Besides its "primary valence" (today's oxidation state), a metal has a "secondary valence" (today's coordination number) directed toward definite positions in space. In modern language, the six $\ce{NH3}$ molecules are bound to $\ce{Co^3+}$ by **coordinate bonds** to give the octahedral $\ce{[Co(NH3)6]^3+}$, and the three $\ce{Cl-}$ ions are counterions.

**Definition 5.1.1 (Coordination Compound)** A complex ion or molecule formed from a central atom (or ion) and several molecules or ions that supply **lone pairs** through coordinate bonds is called a **coordination entity**. A compound that contains a coordination entity is called a **coordination compound** or **coordination complex**, or simply a complex. A charged coordination entity is called a complex ion.

For example, $\ce{[AlF6]^3-}$ and $\ce{[Cu(NH3)4]^2+}$ are complex ions, and $\ce{Ni(CO)4}$ is an electrically neutral complex molecule; $\ce{Na3[AlF6]}$, $\ce{[Cu(NH3)4]SO4}$, and $\ce{Ni(CO)4}$ are all coordination compounds. In a formula, the coordination entity inside the square brackets is the inner sphere, and the ions outside the brackets form the outer sphere. The bond between inner and outer spheres is ionic, and the compound dissociates completely in water: $\ce{[Cu(NH3)4]SO4 -> [Cu(NH3)4]^2+ + SO4^2-}$. The inner sphere itself is comparatively stable and dissociates only partially (complexation equilibrium, [6.1.9](/6.1.9)). A complex may lack an outer sphere ($\ce{Ni(CO)4}$, $\ce{[PtCl2(NH3)2]}$) but never an inner sphere.

**Definition 5.1.2** In a coordination entity, the atom or ion that accepts the lone pairs is called the **central atom** (central ion); the molecules or ions bound to it are called **ligands**, and the atom of a ligand that bonds directly to the central atom is called the **donor atom**. A ligand with a single donor atom is monodentate; a ligand with two or more donor atoms that can bind the same central atom simultaneously is called a **polydentate ligand** (multidentate ligand).

The central atom is usually a positively charged metal ion, especially a transition-metal ion. It may also be a neutral metal atom (Ni in $\ce{Ni(CO)4}$, Fe in $\ce{Fe(CO)5}$) or a nonmetal in a high oxidation state (B in $\ce{BF4-}$, Si in $\ce{SiF6^2-}$). A complex with one central atom is mononuclear, and one with two or more is polynuclear. Forming a coordinate bond means donating and accepting an electron pair: the central atom is the electron-pair acceptor (Lewis acid) and the ligand is the electron-pair donor (Lewis base), see [6.1.9](/6.1.9). Common donor atoms are the halogens, O, N, S, C, and P.

| Ligand | Common name | Donor atom | Denticity | IUPAC name (as a ligand) |
|---|---|---|---|---|
| $\ce{F-}$, $\ce{Cl-}$, $\ce{Br-}$, $\ce{I-}$ | fluoride, chloride, bromide, iodide | X | 1 | fluorido, chlorido, bromido, iodido |
| $\ce{OH-}$ | hydroxide | O | 1 | hydroxido |
| $\ce{H2O}$ | water | O | 1 | aqua |
| $\ce{NH3}$ | ammonia | N | 1 | ammine |
| $\ce{CO}$ | carbon monoxide | C | 1 | carbonyl |
| $\ce{CN-}$ | cyanide | C | 1 | cyanido |
| $\ce{SCN-}$ / $\ce{NCS-}$ | thiocyanate / isothiocyanate | S / N | 1 | thiocyanato-κS / thiocyanato-κN |
| $\ce{NO2-}$ / $\ce{ONO-}$ | nitro / nitrito | N / O | 1 | nitrito-κN / nitrito-κO |
| $\ce{C5H5N}$ (py) | pyridine | N | 1 | pyridine |
| $\ce{H2NCH2CH2NH2}$ (en) | ethylenediamine | N | 2 | ethane-1,2-diamine |
| $\ce{C2O4^2-}$ (ox) | oxalate | O | 2 | oxalato |
| $\ce{H2NCH2COO-}$ (gly) | glycinate | N, O | 2 | glycinato |
| bipy, phen | 2,2′-bipyridine, 1,10-phenanthroline | N | 2 | 2,2′-bipyridine, 1,10-phenanthroline |
| $\ce{EDTA^4-}$ | ethylenediaminetetraacetate | 2 N, 4 O | 6 | ethylenediaminetetraacetato |

Ligands such as $\ce{SCN-}$ and $\ce{NO2-}$ that can coordinate through different atoms are called ambidentate ligands (*ambidentate ligand*); they give rise to linkage isomerism (5.2.2). The polydentate ligands in the table are:

```smiles
NCCN en
[O-]C(=O)C(=O)[O-] ox
NCC(=O)[O-] gly
c1ccnc(c1)-c1ccccn1 bipy
c1cnc2c(c1)ccc1cccnc12 phen
[O-]C(=O)CN(CC(=O)[O-])CCN(CC(=O)[O-])CC(=O)[O-] EDTA
```

### 5.1.2. Coordination Number and Charge of the Complex Ion

**Definition 5.1.3 (Coordination Number)** The number of donor atoms directly bonded to the central atom in a coordination entity is called the **coordination number** of the central atom.

When all ligands are monodentate, the coordination number equals the number of ligands, as for Pt in $\ce{[Pt(NH3)4]Cl2}$, which has coordination number 4. With polydentate ligands the two differ: $\ce{[Pt(en)2]Cl2}$ has only two ligands but still coordination number 4, and in $\ce{[Co(EDTA)]-}$ a single ligand supplies six donor atoms. The most common coordination numbers are 4 and 6, followed by 2, 5, and 8; large lanthanide ions can reach 9–12.

The coordination number is determined jointly by the charges and sizes of the central atom and the ligands and by external conditions:

- The higher the charge of the central ion, the more ligands it attracts: $\ce{[Ag(NH3)2]+}$, $\ce{[Cu(NH3)4]^2+}$, $\ce{[Co(NH3)6]^3+}$.
- The larger the radius of the central ion, the more ligands fit around it: $\ce{BF4-}$ versus $\ce{AlF6^3-}$.
- The larger the ligands and the more negative their charge, the greater the repulsion among them and the smaller the coordination number: $\ce{AlF6^3-}$ versus $\ce{AlCl4-}$.
- A higher ligand concentration favors complexes of high coordination number, whereas raising the temperature often lowers the coordination number.

The charge of a complex ion is the algebraic sum of the charges of the central ion and the ligands. For example, in $\ce{K3[Fe(CN)6]}$ the oxidation state of Fe is $+3$ and the six $\ce{CN-}$ carry $-6$ in total, so the complex ion has charge $-3$, balanced by the three $\ce{K+}$ of the outer sphere.

### 5.1.3. Nomenclature of Complexes

The Chinese names of complexes follow the rules of the Chinese Chemical Society, which parallel the IUPAC rules but differ in the order of ligands (anionic ligands before neutral ones); they are given in the Chinese version of this page. The IUPAC (2005 recommendations) nomenclature used in English works as follows:

1. The ligands are listed in alphabetical order of their names, without distinguishing anionic from neutral ligands (the multiplying prefixes di-, tri-, bis-, and so on are ignored in alphabetizing), and then the central atom is named, followed by its oxidation state in Roman numerals in parentheses.
2. Anionic ligands end in -ido, -ato, or -ito (chlorido, cyanido, oxalato). Complex anions end in -ate, and some elements use Latin stems (ferrate, cuprate, argentate, aurate, plumbate, stannate).
3. Multiplying prefixes di-, tri-, tetra-, … are used for simple ligands, and bis-, tris-, tetrakis-, … (with the ligand name in parentheses) for complicated ligands or those that already contain such a prefix.
4. In a salt, the cation is named first, then the anion, whether the complex is the cation or the anion.

| Formula | IUPAC name |
|---|---|
| $\ce{[Co(NH3)6]Cl3}$ | hexaamminecobalt(III) chloride |
| $\ce{[Cu(NH3)4]SO4}$ | tetraamminecopper(II) sulfate |
| $\ce{[Co(NH3)5(H2O)]Cl3}$ | pentaammineaquacobalt(III) chloride |
| $\ce{K3[Fe(CN)6]}$ | potassium hexacyanidoferrate(III) |
| $\ce{H4[Fe(CN)6]}$ | hydrogen hexacyanidoferrate(II) |
| $\ce{K[PtCl3(NH3)]}$ | potassium amminetrichloridoplatinate(II) |
| $\ce{[CoCl(SCN)(en)2]+}$ | chloridobis(ethane-1,2-diamine)(thiocyanato-κS)cobalt(III) ion |
| $\ce{[PtCl2(NH3)2]}$ | diamminedichloridoplatinum(II) |
| $\ce{Ni(CO)4}$ | tetracarbonylnickel(0) |

### 5.1.4. Types of Complexes

Simple complexes. A simple complex consists of one central atom and several monodentate ligands, such as $\ce{[Ag(NH3)2]+}$, $\ce{BF4-}$, $\ce{[Fe(H2O)6]Cl3}$, and $\ce{[CoCl3(NH3)3]}$. Metal ions in aqueous solution actually exist as aqua complexes $\ce{[M(H2O)_n]^{m+}}$.

**Definition 5.1.4 (Chelate)** A complex in which a central atom is bound by a polydentate ligand so as to form a ring structure is called a **chelate**; a polydentate ligand that can form chelates is called a chelating agent.

For example, in $\ce{[Cu(en)2]^2+}$ each ethylenediamine forms with $\ce{Cu^2+}$ a five-membered ring containing Cu, two N, and two C, and $\ce{[Co(EDTA)]-}$ contains five five-membered rings. Five- and six-membered rings have the least strain and are the most common. A chelate is much more stable than a simple complex of similar composition, a phenomenon known as the chelate effect (*chelate effect*). Compare the two complex ions $\ce{[Ni(NH3)6]^2+}$ and $\ce{[Ni(en)3]^2+}$: both contain six Ni–N bonds and have similar enthalpy changes, but in the reaction
$$
\ce{[Ni(NH3)6]^2+ + 3en -> [Ni(en)3]^2+ + 6NH3}
$$
the number of independently moving particles in solution rises from 4 to 7, so the entropy increases (the relation between entropy and the direction of reactions is given in [6.1.6](/6.1.6)) and the equilibrium lies far to the right. Their overall stability constants ([6.1.9](/6.1.9)) are about $10^{8.7}$ and $10^{18.3}$, respectively, and by the rule of multiple equilibria the equilibrium constant of the substitution reaction above is about $10^{18.3}/10^{8.7} = 10^{9.6}$. EDTA forms 1∶1 chelates with almost all metal ions and is widely used in complexometric titration ([Analytical Chemistry](/6.4)), in softening hard water, and in treating heavy-metal poisoning.

Polynuclear complexes contain two or more central atoms linked by bridging ligands (denoted μ-), such as the hydroxo-bridged $\ce{[(NH3)5Co(\mu-OH)Co(NH3)5]^5+}$ and the chloro-bridged gaseous $\ce{Al2Cl6}$ ([6.1.14](/6.1.14)).

**Definition 5.1.5 (Metal Carbonyl)** A complex that has CO as a ligand is called a **metal carbonyl** (carbonyl complex).

Metals of the d block, especially in low oxidation states (often 0), form stable metal carbonyls with CO, such as tetrahedral $\ce{Ni(CO)4}$, trigonal bipyramidal $\ce{Fe(CO)5}$, and octahedral $\ce{Cr(CO)6}$. $\ce{Ni(CO)4}$ forms directly from Ni and CO at about $50\,^\circ\mathrm{C}$ and, once volatilized, decomposes at about $200\,^\circ\mathrm{C}$ to give pure nickel; this is the Mond process for refining nickel. In all these complexes the number of metal valence electrons plus the electrons donated by the ligands equals 18 (Ni 10 + 4 × 2, Fe 8 + 5 × 2, Cr 6 + 6 × 2), an empirical regularity known as the 18-electron rule.

The donor atom of CO is C: according to the molecular orbital diagram of [6.1.3](/6.1.3), the **highest occupied molecular orbital** of CO is concentrated mainly on C and forms a σ coordinate bond with an empty orbital of the metal. With this σ bond alone, too much negative charge would accumulate on a zero-valent metal. In fact the metal also donates electrons from filled d orbitals back into the empty π* antibonding orbitals of CO.

**Definition 5.1.6 (π Back-Bonding)** The π bond formed when a ligand donates a lone pair (or π electrons) to an empty orbital of the central atom while, at the same time, a filled d orbital of the central atom donates electrons to an empty π* orbital of the ligand is called **π back-bonding**.

The σ donation and the π back-bonding reinforce each other (synergic bonding), so that the M–C bond is much stronger than a simple coordinate bond. The electrons donated back enter the antibonding orbital of CO and weaken the C–O bond: the C–O stretching wavenumber falls from $2143\,\mathrm{cm^{-1}}$ for free CO to about $2060\,\mathrm{cm^{-1}}$ in $\ce{Ni(CO)4}$ and about $2000\,\mathrm{cm^{-1}}$ in $\ce{Cr(CO)6}$, which is experimental evidence for back-bonding. Ligands such as $\ce{CN-}$ and $\ce{PPh3}$ can also accept back-donated electrons.

Alkene complexes. Unsaturated hydrocarbons can act as ligands even though they have no lone pairs. The earliest example, prepared in 1827, is Zeise's salt $\ce{K[PtCl3(C2H4)]*H2O}$, which was also the first organometallic compound. The ethylene molecule is perpendicular to the $\ce{PtCl3}$ plane and donates its C=C π electrons to an empty orbital of Pt(II); Pt then donates d electrons back into the π* orbital of ethylene, so that the C=C bond is slightly lengthened. $\ce{Ag+}$ also forms complex ions of the type $\ce{[Ag(C2H4)]+}$ with alkenes, which can be used to separate alkenes.

Polyoxometalate complexes. The oxoanions of high-oxidation-state elements such as Mo, W, and V can condense into polynuclear anions. Those formed by condensation of a single kind of oxoanion are isopolyanions, such as $\ce{[Mo7O24]^6-}$ in ammonium molybdate $\ce{(NH4)6Mo7O24*4H2O}$; those centered on a different atom are heteropolyanions, such as $\ce{[PMo12O40]^3-}$, centered on P, in ammonium phosphomolybdate $\ce{(NH4)3[PMo12O40]}$. The precipitation of yellow ammonium phosphomolybdate is a classical test for phosphate ([6.1.14](/6.1.14)).

## 5.2. Geometries and Isomerism of Complexes

### 5.2.1. Coordination Polyhedra

**Definition 5.2.1 (Coordination Polyhedron)** The polyhedron (or polygon) obtained by taking the donor atoms of a coordination entity as vertices and joining them by line segments is called the **coordination polyhedron**; it represents the geometry of the complex.

The central atom lies at the center of the coordination polyhedron, and the ligands tend to stay as far from one another as possible to reduce repulsion, as in the **valence shell electron pair repulsion theory** of [6.1.3](/6.1.3). The geometry of transition-metal complexes, however, also depends on the number of d electrons (for instance, d⁸ ions often adopt a square planar geometry, see 5.5.3), so it cannot be judged from the coordination number alone.

| Coordination number | Geometry | Examples |
|---|---|---|
| 2 | linear | $\ce{[CuCl2]-}$, $\ce{[Ag(NH3)2]+}$, $\ce{[Au(CN)2]-}$ (d¹⁰ $\ce{M+}$ of Group 11) |
| 3 | trigonal planar | $\ce{[HgI3]-}$, $\ce{[Pt(PPh3)3]}$ (d¹⁰) |
| 4 | tetrahedral | $\ce{[BeF4]^2-}$, $\ce{[AlCl4]-}$, $\ce{[Zn(NH3)4]^2+}$, $\ce{[NiCl4]^2-}$ |
| 4 | square planar | $\ce{[Ni(CN)4]^2-}$, $\ce{[PtCl4]^2-}$, $\ce{[Cu(NH3)4]^2+}$ |
| 5 | trigonal bipyramidal | $\ce{Fe(CO)5}$, $\ce{[CuCl5]^3-}$ |
| 5 | square pyramidal | $\ce{[Ni(CN)5]^3-}$ |
| 6 | octahedral | $\ce{[Co(NH3)6]^3+}$, $\ce{[Fe(CN)6]^3-}$, $\ce{[AlF6]^3-}$ |
| 6 | trigonal prismatic (rare) | $\ce{[Re(S2C2Ph2)3]}$ |

The two geometries of five-coordinate complexes are close in energy and often interconvert; both occur together in some crystals of $\ce{[Ni(CN)5]^3-}$.

![Coordination polyhedra for coordination numbers 2–6: linear, trigonal planar, tetrahedral, square planar, trigonal bipyramidal, square pyramidal, octahedral, and trigonal prismatic](./plots/coordination-polyhedra.py)

### 5.2.2. Isomerism and Structural Isomers

Compounds with the same formula but different structures are isomers, and their properties differ. The isomerism of complexes falls into two broad classes: structural isomerism, in which the atoms are connected differently, and stereoisomerism, in which the connectivity is the same and only the arrangement in space differs; the latter is further divided into geometric isomerism (5.2.3) and optical isomerism (5.2.4). There are four main kinds of structural isomerism:

| Type | Cause | Examples |
|---|---|---|
| Hydrate isomerism | different distribution of water between inner and outer sphere | $\ce{CrCl3*6H2O}$: $\ce{[Cr(H2O)6]Cl3}$ (violet), $\ce{[CrCl(H2O)5]Cl2*H2O}$ (blue-green), $\ce{[CrCl2(H2O)4]Cl*2H2O}$ (dark green) |
| Ionization isomerism | different distribution of anions between inner and outer sphere | $\ce{[CoBr(NH3)5]SO4}$ (purple-red) and $\ce{[Co(SO4)(NH3)5]Br}$ (red) |
| Linkage isomerism | an ambidentate ligand coordinates through different atoms | $\ce{[Co(NO2)(NH3)5]^2+}$ (nitro, yellow-brown) and $\ce{[Co(ONO)(NH3)5]^2+}$ (nitrito, red) |
| Coordination isomerism | different distribution of ligands between complex cation and complex anion | $\ce{[Co(NH3)6][Cr(CN)6]}$ and $\ce{[Cr(NH3)6][Co(CN)6]}$ |

Outer-sphere ions are free in solution, so they can be distinguished by precipitation reactions. Adding excess $\ce{AgNO3}$ to solutions of the three $\ce{CrCl3*6H2O}$ isomers precipitates 3, 2, and 1 mol of AgCl per mole, respectively. A solution of $\ce{[CoBr(NH3)5]SO4}$ gives a $\ce{BaSO4}$ precipitate with $\ce{Ba^2+}$, whereas its ionization isomer gives an AgBr precipitate with $\ce{Ag+}$.

### 5.2.3. Geometric Isomerism

**Definition 5.2.2 (Geometric Isomerism)** The isomerism that arises in complexes of the same composition from different relative positions of the ligands around the central atom is called **geometric isomerism** (cis–trans isomerism). Identical ligands in adjacent positions are called cis, and those in opposite positions are called trans.

In a tetrahedron any two vertices are adjacent, so tetrahedral complexes show no geometric isomerism; square planar and octahedral complexes do. The most famous example is square planar $\ce{[PtCl2(NH3)2]}$:

| Property | cis (cisplatin) | trans |
|---|---|---|
| Color | orange-yellow | pale yellow |
| Dipole moment | $p > 0$ | $p = 0$ |
| Solubility/(g per 100 g water) | 0.2523 | 0.0366 |
| Anticancer activity | yes | no |

The cis isomer is a polar molecule and is more soluble in water. In 1965 Rosenberg discovered by chance that it inhibits cell division, and since then cisplatin has become an important drug for testicular and ovarian cancer. After entering a cell it loses $\ce{Cl-}$ and uses its two adjacent coordination sites to bind two adjacent guanine bases on the same DNA strand, which bends the DNA and blocks replication. The two vacant sites of the trans isomer are opposite each other and cannot form this cross-link (for the mechanism of action see [Chemical Biology](/6.6)).

Octahedral complexes have more geometric isomers. The $\ce{MA4B2}$ type has a cis and a trans form; for example, cis-$\ce{[CoCl2(NH3)4]+}$ is violet and trans is green. The $\ce{MA3B3}$ type also has two forms: when the three A ligands occupy one triangular face of the octahedron the isomer is facial (fac-), and when the three A ligands lie in one plane with the central atom, that is, along a "meridian" of the octahedron, it is meridional (mer-), as for $\ce{[Co(NO2)3(NH3)3]}$. The $\ce{MA2B2C2}$ type has five geometric isomers, one of which (the all-cis form) also has a pair of enantiomers (5.2.4).

![Geometric isomerism: cis and trans isomers of square planar [PtCl2(NH3)2] and of octahedral [CoCl2(NH3)4]+, and the fac and mer isomers of the MA3B3 type](./plots/geometric-isomers.py)

### 5.2.4. Optical Isomerism

**Definition 5.2.3 (Chirality)** The property of an object that cannot be superimposed on its mirror image, like the left and right hands, is called **chirality**. A molecule with this property is called a chiral molecule.

The rigorous criterion for a chiral molecule is that it has no improper rotation axis of any order (including mirror planes and centers of inversion; see the point groups in [Structural Chemistry](/6.2)). For the examples in this course it suffices to check for mirror planes and a center of inversion.

**Definition 5.2.4 (Enantiomer)** Two stereoisomers that are nonsuperimposable mirror images of each other are called a pair of **enantiomers**. The isomerism caused by enantiomers is called **optical isomerism**.

Enantiomers have identical physical properties such as melting point, boiling point, solubility, and spectra, and differ in only one respect: they rotate the plane of plane-polarized light by the same angle but in opposite directions (**optical activity**, [5.4.3](/5.4.3#sec-3.9)). An isomer that rotates the plane clockwise as seen facing the light source is dextrorotatory, denoted (+); one that rotates it counterclockwise is levorotatory, denoted (−). Enantiomers react identically with achiral reagents but may interact quite differently with chiral reagents (including enzymes and receptors in living organisms), which is why the enantiomers of a drug often have different effects.

Note that the sense of rotation is a measured result, denoted (+)/(−), whereas D/L is a configurational label relative to glyceraldehyde and R/S is an absolute-configuration label assigned by the Cahn–Ingold–Prelog rules ([Organic Chemistry](/6.5)); there is no necessary correspondence between these labels and the sense of rotation. Octahedral tris(chelate) complexes are designated Δ (right-handed helix) and Λ (left-handed helix).

**Definition 5.2.5 (Racemate)** A mixture of equal amounts of two enantiomers is called a **racemate** (racemic mixture), denoted (±) or rac-; its optical rotations cancel, so it is optically inactive. Separating a racemate into its two enantiomers is called resolution.

In 1848 Pasteur found that crystals of racemic sodium ammonium tartrate have two mirror-image shapes. He separated them with tweezers under a microscope, and solutions of the two kinds of crystals rotated light in opposite directions: this was the first resolution. The optical isomerism of complexes was key evidence for Werner's theory. In 1911 he resolved cis-$\ce{[CoCl(NH3)(en)2]^2+}$, which showed that six-coordinate Co(III) is octahedral rather than planar hexagonal (a planar molecule has a mirror plane and cannot have enantiomers). In 1914 he resolved a polynuclear complex ion containing no carbon at all, $\ce{[Co(OH)6Co3(NH3)12]^6+}$, showing that chirality is not unique to carbon compounds.

Among octahedral complexes, cis-$\ce{[CoCl2(en)2]+}$ has no mirror plane and has a pair of enantiomers, whereas trans-$\ce{[CoCl2(en)2]+}$ has a mirror plane and is achiral. The three ethylenediamine ligands of $\ce{[Co(en)3]^3+}$ are arranged like the three blades of a propeller, giving the Δ and Λ enantiomers.

![Optical isomerism: Δ- and Λ-[Co(en)3]3+ are mirror images of each other (the mirror plane is in the middle); each ethylenediamine is simplified to an arc connecting two adjacent donor atoms](./plots/optical-isomers.py)

**Definition 5.2.6 (Diastereomer)** Stereoisomers that are not mirror images of each other are called **diastereomers**.

Geometric isomers (such as cis- and trans-$\ce{[CoCl2(NH3)4]+}$) are diastereomers of each other. A molecule with two stereocenters has at most four stereoisomers, forming two pairs of enantiomers, and isomers from different pairs are diastereomers. Diastereomers differ in physical properties and are similar but not identical in chemical properties, so they can be separated by ordinary methods such as recrystallization and chromatography; the usual way to resolve a racemate is to first convert the enantiomers into diastereomers with a pure chiral reagent. When the groups attached to the two stereocenters are identical (as in tartaric acid), one "pair" of isomers has an internal mirror plane and is in fact a single achiral molecule, called a meso compound (*meso compound*): tartaric acid has only three stereoisomers, (+), (−), and meso. A systematic treatment of stereochemistry is given in [Organic Chemistry](/6.5).

## 5.3. Magnetism of Complexes

Both the orbital motion and the spin of electrons produce magnetic moments ([5.3.8](/5.3.8#sec-8.2)). In a substance in which all electrons are paired, the moments cancel and there is no permanent magnetic moment; such a substance is weakly repelled by a magnetic field and is a **diamagnetic substance**, as are most organic compounds, He, Ne, $\ce{SiO2}$, $\ce{Al2O3}$, $\ce{CO2}$, and the salts of the alkaline earth metals. A substance with unpaired electrons has a permanent magnetic moment and is attracted into a magnetic field; it is a **paramagnetic substance**, as are $\ce{O2}$, NO, $\ce{NO2}$, organic free radicals, and most complexes of transition-metal ions such as $\ce{Cu^2+}$ and $\ce{Fe^3+}$ and of rare-earth ions such as $\ce{Gd^3+}$ and $\ce{Dy^3+}$. **Ferromagnetic substances** such as Fe, Co, and Ni are strongly attracted into a magnetic field; this is a collective effect in the solid, in which the moments of many atoms align spontaneously in parallel within magnetic domains, and an individual complex molecule has no such property.

The magnetism of complexes is measured with a Gouy balance or a SQUID magnetometer. The molar magnetic susceptibility $\chi_{\mathrm{m}}$ of a paramagnetic substance is approximately inversely proportional to temperature (Curie's law), and from it the magnetic moment of a molecule is defined:

**Definition 5.3.1 (Effective Magnetic Moment)** The molecular magnetic moment calculated from the molar magnetic susceptibility $\chi_{\mathrm{m}}$ of a paramagnetic substance (SI unit $\mathrm{m^3\,mol^{-1}}$) as
$$
\mu_{\mathrm{eff}} = \sqrt{\frac{3k_{\mathrm{B}}T\chi_{\mathrm{m}}}{\mu_0N_{\mathrm{A}}}}
$$
is called the **effective magnetic moment**, usually expressed in units of the Bohr magneton $\mu_{\mathrm{B}}$.

In complexes of the first transition series the orbital angular momentum of the d electrons is largely "quenched" by the ligand field: the ligand field removes the degeneracy of the d orbitals (5.5), the electrons can occupy only real orbitals, and electrons in real orbitals have no net orbital angular momentum (for real orbitals see [6.1.2](/6.1.2)). The magnetic moment then arises from spin alone. For $n$ unpaired electrons the total spin quantum number is $S = n/2$, the magnitude of the spin moment is $g_{\mathrm{e}}\sqrt{S(S+1)}\,\mu_{\mathrm{B}}$, and the electron $g$ factor is $g_{\mathrm{e}} \approx 2$ ([5.5.4](/5.5.4#sec-4.2.3)), so that

**Formula 5.3.1 (Spin-Only Formula)**
$$
\mu_{\mathrm{eff}} \approx 2\sqrt{\frac{n}{2}\left(\frac{n}{2}+1\right)}\,\mu_{\mathrm{B}} = \sqrt{n(n+2)}\,\mu_{\mathrm{B}}.
$$

| Number of unpaired electrons $n$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $\mu_{\mathrm{eff}}/\mu_{\mathrm{B}}$ | 0 | 1.73 | 2.83 | 3.87 | 4.90 | 5.92 |

Conversely, the number of unpaired electrons can be determined from the measured effective magnetic moment, and from it one infers the electron configuration of the central ion and the mode of bonding (5.4, 5.5).

**Example 5.3.1** $\ce{Mn^2+}$ is $3\mathrm{d}^5$. If all five d electrons are unpaired, $\mu_{\mathrm{eff}} = \sqrt{5\times7}\,\mu_{\mathrm{B}} = 5.92\,\mu_{\mathrm{B}}$, in agreement with the measured value for $\ce{[Mn(H2O)6]^2+}$. For $\ce{[FeF6]^3-}$ the measured value is $5.90\,\mu_{\mathrm{B}}$, so the five d electrons of $\ce{Fe^3+}$ are also all unpaired. For $\ce{[Fe(CN)6]^3-}$ the measured value is about $2.4\,\mu_{\mathrm{B}}$, closest to the $1.73\,\mu_{\mathrm{B}}$ of $n = 1$, so there is only one unpaired electron. $\ce{[Ni(CN)4]^2-}$ is diamagnetic, $n = 0$.

The spin-only formula is an approximation. The measured value for $\ce{[Fe(CN)6]^3-}$ is clearly larger than $1.73\,\mu_{\mathrm{B}}$ because in its $t_{2g}^5$ configuration the degenerate orbitals are unevenly occupied and the orbital angular momentum is not completely quenched. The deviation, however, generally does not exceed the gap between neighboring values of $n$, so the determination of the number of unpaired electrons is unaffected. The 4f electrons of lanthanide ions are shielded by outer electrons, their orbital angular momentum is not quenched, and their magnetic moments must be calculated from the total angular momentum, see [6.1.15](/6.1.15).

## 5.4. Valence Bond Theory of Complexes

In the 1930s Pauling applied the theory of hybrid orbitals ([6.1.3](/6.1.3)) to complexes, giving the valence bond theory of complexes. Its main points are:

1. The central atom provides a set of empty valence orbitals; these first undergo **hybridization**, giving hybrid orbitals equal in number to the coordination number and pointing in definite directions.
2. Lone pairs of the donor atoms enter the hybrid orbitals of the central atom and form σ coordinate bonds.
3. The geometry of the coordination entity is determined by the hybridization of the central atom.

| Coordination number | Hybridization | Geometry | Examples |
|---|---|---|---|
| 2 | $\mathrm{sp}$ | linear | $\ce{[Ag(NH3)2]+}$, $\ce{[Ag(CN)2]-}$ |
| 3 | $\mathrm{sp}^2$ | trigonal planar | $\ce{[CuCl3]^2-}$, $\ce{[HgI3]-}$ |
| 4 | $\mathrm{sp}^3$ | tetrahedral | $\ce{[BeF4]^2-}$, $\ce{[Zn(NH3)4]^2+}$, $\ce{[NiCl4]^2-}$ |
| 4 | $\mathrm{dsp}^2$ | square planar | $\ce{[Ni(CN)4]^2-}$, $\ce{[PtCl4]^2-}$ |
| 5 | $\mathrm{dsp}^3$ | trigonal bipyramidal | $\ce{Fe(CO)5}$ |
| 6 | $\mathrm{d}^2\mathrm{sp}^3$ | octahedral | $\ce{[Fe(CN)6]^3-}$, $\ce{[Co(NH3)6]^3+}$ |
| 6 | $\mathrm{sp}^3\mathrm{d}^2$ | octahedral | $\ce{[FeF6]^3-}$, $\ce{[CoF6]^3-}$ |

In the hybrid orbital symbols, a d written before s is a $(n-1)\mathrm{d}$ orbital of the penultimate shell, and a d written after p is an $n\mathrm{d}$ orbital of the outermost shell. The following table uses box diagrams for the valence electrons of the central ion in several examples (↑↓ denotes an electron pair, and ·· denotes a pair supplied by a ligand):

| Coordination entity | $(n-1)\mathrm{d}$ | $n\mathrm{s}$ | $n\mathrm{p}$ | $n\mathrm{d}$ | Hybridization | Unpaired electrons |
|---|---|---|---|---|---|---|
| $\ce{[Ag(NH3)2]+}$ ($4\mathrm{d}^{10}$) | ↑↓ ↑↓ ↑↓ ↑↓ ↑↓ | ·· | ·· | | $\mathrm{sp}$ | 0 |
| $\ce{[NiCl4]^2-}$ ($3\mathrm{d}^8$) | ↑↓ ↑↓ ↑↓ ↑ ↑ | ·· | ·· ·· ·· | | $\mathrm{sp}^3$ | 2 |
| $\ce{[Ni(CN)4]^2-}$ ($3\mathrm{d}^8$) | ↑↓ ↑↓ ↑↓ ↑↓ ·· | ·· | ·· ·· | | $\mathrm{dsp}^2$ | 0 |
| $\ce{[FeF6]^3-}$ ($3\mathrm{d}^5$) | ↑ ↑ ↑ ↑ ↑ | ·· | ·· ·· ·· | ·· ·· | $\mathrm{sp}^3\mathrm{d}^2$ | 5 |
| $\ce{[Fe(CN)6]^3-}$ ($3\mathrm{d}^5$) | ↑↓ ↑↓ ↑ ·· ·· | ·· | ·· ·· ·· | | $\mathrm{d}^2\mathrm{sp}^3$ | 1 |

When $\ce{Ni^2+}$ forms a four-coordinate complex with $\ce{Cl-}$, it uses the 4s and 4p orbitals in $\mathrm{sp}^3$ hybridization, giving tetrahedral $\ce{[NiCl4]^2-}$ with two unpaired electrons (spin-only value $2.83\,\mu_{\mathrm{B}}$). With $\ce{CN-}$, the two unpaired 3d electrons are squeezed into one orbital and pair up, freeing a 3d orbital for $\mathrm{dsp}^2$ hybridization, which gives the square planar, diamagnetic $\ce{[Ni(CN)4]^2-}$, in agreement with experiment. Likewise, the five unpaired electrons of $\ce{[FeF6]^3-}$ show that no 3d orbital has been vacated, so the hybridization must use the 4s, 4p, and 4d orbitals ($\mathrm{sp}^3\mathrm{d}^2$). $\ce{[Fe(CN)6]^3-}$ has only one unpaired electron: the five d electrons are crowded into three 3d orbitals, and the two vacated 3d orbitals take part in $\mathrm{d}^2\mathrm{sp}^3$ hybridization.

**Definition 5.4.1 (Inner-Orbital and Outer-Orbital Complexes)** A complex in which the central atom uses the penultimate-shell $(n-1)\mathrm{d}$ orbitals in hybridization (such as $\mathrm{d}^2\mathrm{sp}^3$ and $\mathrm{dsp}^2$) is called an **inner-orbital complex**; a complex in which only the outermost $n\mathrm{s}$, $n\mathrm{p}$, and $n\mathrm{d}$ orbitals are hybridized (such as $\mathrm{sp}^3$ and $\mathrm{sp}^3\mathrm{d}^2$) is called an **outer-orbital complex**.

The energy of the $(n-1)\mathrm{d}$ orbitals is lower than that of the $n\mathrm{d}$ orbitals, so the coordinate bonds of inner-orbital complexes are stronger and such complexes are generally more stable ($\ce{[Fe(CN)6]^3-}$ is much more stable than $\ce{[FeF6]^3-}$). Inner-orbital complexes often require the d electrons to be "squeezed" into pairs, leaving few unpaired electrons, and correspond to the low-spin complexes of 5.5; outer-orbital complexes correspond to high-spin complexes. Ligands with highly electronegative donor atoms such as $\ce{F-}$ and $\ce{H2O}$ tend to form outer-orbital complexes, and $\ce{CN-}$ and CO tend to form inner-orbital complexes, but this is only an empirical tendency, and which type actually forms must be settled by measuring the magnetic moment.

Valence bond theory explains the coordination numbers, geometries, and magnetism of complexes in an intuitive way, but its limitations are obvious:

- It can explain the mode of bonding only after the magnetic moment has been measured and cannot predict whether a complex is high-spin or low-spin.
- It says nothing about excited states and cannot explain the colors and absorption spectra of complexes.
- It cannot explain thermodynamic regularities such as the "double-humped" variation of the hydration enthalpies of first-series ions (5.5.7).
- Some of its explanations are strained: if square planar $\ce{[Cu(NH3)4]^2+}$ were $\mathrm{dsp}^2$ hybridized, one 3d electron of $\ce{Cu^2+}$ ($3\mathrm{d}^9$) would have to be promoted to a 4p orbital and should then be lost very easily, yet $\ce{[Cu(NH3)4]^2+}$ is not easily oxidized.

These problems are resolved by crystal field theory.

## 5.5. Crystal Field Theory

### 5.5.1. Basic Principles

Crystal field theory was proposed by Bethe (1929) and Van Vleck (1932) to explain the spectra and magnetism of ions in crystals, and it was applied to complexes in the 1950s.

**Definition 5.5.1 (Crystal Field Theory)** The theory that treats the interaction between the central ion and the ligands entirely as electrostatic (the ligands being point charges or point dipoles) and studies the effect of the electrostatic field produced by the ligands on the energies of the d orbitals of the central ion is called **crystal field theory**.

Its main points are:

1. The central ion lies in the electrostatic field (crystal field) formed by the ligands, and the two are held together by electrostatic attraction.
2. The crystal field splits the five degenerate d orbitals of the central ion into levels; the pattern and magnitude of the splitting depend on the kind and spatial arrangement of the ligands.
3. The d electrons are redistributed among the split orbitals so that the energy of the system is lower than in a spherically symmetric field, and the complex gains additional stability (5.5.6).

### 5.5.2. Splitting of the d Orbitals in an Octahedral Field

Let six ligands approach the central ion along the $\pm x$, $\pm y$, and $\pm z$ axes. If the negative charge of the ligands were spread uniformly over a spherical surface (a spherical field), the repulsion on the d electrons would raise the energies of all five d orbitals equally, and they would remain degenerate. In an octahedral field, the electron density maxima of $\mathrm{d}_{z^2}$ and $\mathrm{d}_{x^2-y^2}$ point directly at the ligands, so they experience greater repulsion and rise in energy; the maxima of $\mathrm{d}_{xy}$, $\mathrm{d}_{yz}$, and $\mathrm{d}_{xz}$ point between the axes, so they experience less repulsion and fall in energy (for the angular distributions of the d orbitals see [6.1.2](/6.1.2)). The five d orbitals thus split into two sets: the higher, doubly degenerate $e_g$ ($\mathrm{d}_{z^2}$, $\mathrm{d}_{x^2-y^2}$) and the lower, triply degenerate $t_{2g}$ ($\mathrm{d}_{xy}$, $\mathrm{d}_{yz}$, $\mathrm{d}_{xz}$). The symbols $e_g$ and $t_{2g}$ denote irreducible representations in group theory ([Structural Chemistry](/6.2)).

**Definition 5.5.2 (Crystal Field Splitting Energy)** The energy difference between the highest and lowest sets of d orbitals after splitting is called the **crystal field splitting energy**. For an octahedral field the splitting energy is denoted $\Delta_{\mathrm{o}}$, the energy difference between $e_g$ and $t_{2g}$, and it is conventionally also written $\Delta_{\mathrm{o}} = 10\,Dq$.

The average energy of the d orbitals is unchanged by the splitting: when a set of degenerate orbitals is split by a perturbation, the sum of the energy changes of the orbitals, weighted by degeneracy, is zero (the barycenter rule). Taking the energy of the d orbitals in the spherical field as the zero,
$$
E(e_g) - E(t_{2g}) = 10\,Dq, \qquad 2E(e_g) + 3E(t_{2g}) = 0,
$$
which gives $E(e_g) = +6\,Dq = +0.6\Delta_{\mathrm{o}}$ and $E(t_{2g}) = -4\,Dq = -0.4\Delta_{\mathrm{o}}$: an electron entering $t_{2g}$ lowers the energy by $4\,Dq$, and an electron entering $e_g$ raises it by $6\,Dq$.

Splitting energies are determined from the absorption spectra of complexes and are often expressed as wavenumbers in $\mathrm{cm^{-1}}$: $1\,\mathrm{cm^{-1}}$ corresponds to $hcN_{\mathrm{A}} = 11.96\,\mathrm{J\,mol^{-1}}$, that is, $1\,\mathrm{kJ\,mol^{-1}} \leftrightarrow 83.59\,\mathrm{cm^{-1}}$. $\Delta_{\mathrm{o}}$ generally lies between $7000$ and $40\,000\,\mathrm{cm^{-1}}$ (about $80$–$480\,\mathrm{kJ\,mol^{-1}}$), comparable to the energies of visible and near-ultraviolet photons, which is why most transition-metal complexes are colored.

### 5.5.3. Tetrahedral and Square Planar Fields

In a tetrahedral field the four ligands sit at alternate vertices of a cube, and the coordinate axes pass through the face centers of the cube. The maxima of $\mathrm{d}_{xy}$, $\mathrm{d}_{yz}$, and $\mathrm{d}_{xz}$ point to the midpoints of the cube edges, closer to the ligands, and those of $\mathrm{d}_{z^2}$ and $\mathrm{d}_{x^2-y^2}$ point to the face centers, farther from the ligands. The order of the split levels is therefore the reverse of that in the octahedral field: the triply degenerate $t_2$ lies above and the doubly degenerate $e$ below (a tetrahedron has no center of symmetry, so the symbols carry no subscript g). The point-charge model gives, for the same ligands and distance,
$$
\Delta_{\mathrm{t}} = \frac{4}{9}\Delta_{\mathrm{o}}, \qquad E(t_2) = +1.78\,Dq, \quad E(e) = -2.67\,Dq.
$$
A tetrahedral field has fewer ligands and none points directly at a d orbital, so its splitting energy is only about half that of an octahedral field.

A square planar field can be viewed as an octahedral field with the two ligands on the $z$ axis moved to infinity. The repulsion along $z$ vanishes and the orbitals containing $z$ drop in energy. In the point-charge model $\mathrm{d}_{x^2-y^2}$ ($+12.28\,Dq$) is highest, followed by $\mathrm{d}_{xy}$ ($+2.28\,Dq$) and $\mathrm{d}_{z^2}$ ($-4.28\,Dq$), with $\mathrm{d}_{xz}$ and $\mathrm{d}_{yz}$ ($-5.14\,Dq$) lowest; the spread between the highest and lowest levels is $17.42\,Dq$. The highest orbital, $\mathrm{d}_{x^2-y^2}$, lies far above the other four, so for a d⁸ ion in a strong field it is particularly favorable to put all eight electrons into the lower four orbitals and leave $\mathrm{d}_{x^2-y^2}$ empty. Accordingly, $\ce{[Ni(CN)4]^2-}$ and almost all four-coordinate complexes of $\ce{Pd^2+}$, $\ce{Pt^2+}$, and $\ce{Au^3+}$ are square planar and diamagnetic. This is the reason behind "$\mathrm{dsp}^2$ hybridization" in valence bond theory.

![Splitting of the d orbitals in octahedral, tetrahedral, and square planar fields (energy of the d orbitals in the spherical field taken as zero, units of Dq; same ligands, same distance)](./plots/d-orbital-splitting.py)

### 5.5.4. Factors Affecting the Splitting Energy

Oxidation state of the central ion. For the same ligands, the higher the charge of the central ion, the closer the ligands approach and the larger the splitting energy; trivalent ions generally have a splitting energy 25%–100% larger than divalent ones:

| $\Delta_{\mathrm{o}}/\mathrm{cm^{-1}}$ of $\ce{[M(H2O)6]^{n+}}$ | V | Cr | Fe | Co |
|---|---|---|---|---|
| $\ce{M^2+}$ | 12 600 | 14 000 | 10 400 | 9300 |
| $\ce{M^3+}$ | 17 700 | 17 600 | 13 700 | 18 600 |

Ligands. For the same central ion the splitting energy varies with the ligand, as in the complex ions of Co(III):

| Complex ion | $\ce{[CoF6]^3-}$ | $\ce{[Co(H2O)6]^3+}$ | $\ce{[Co(NH3)6]^3+}$ | $\ce{[Co(CN)6]^3-}$ |
|---|---|---|---|---|
| $\Delta_{\mathrm{o}}/\mathrm{cm^{-1}}$ | 13 000 | 18 600 | 22 900 | 34 000 |

**Definition 5.5.3 (Spectrochemical Series)** The sequence of ligands arranged in order of increasing splitting energy for the same central ion is called the **spectrochemical series**:
$$
\ce{I-} < \ce{Br-} < \ce{S^2-} < \ce{SCN-} < \ce{Cl-} < \ce{NO3-} < \ce{F-} < \ce{OH-} < \ce{C2O4^2-} < \ce{H2O} < \ce{NCS-} < \ce{CH3CN} < \mathrm{py} < \ce{NH3} < \mathrm{en} < \mathrm{bipy} < \mathrm{phen} < \ce{NO2-} < \ce{PPh3} < \ce{CN-} < \ce{CO}
$$

The spectrochemical series was deduced from absorption spectra by Ryutaro Tsuchida in 1938 and holds approximately for most central ions, although the order of neighboring ligands may interchange with the metal. Roughly, by donor atom the order is halogen < O < N < C. Ligands before $\ce{H2O}$ are called weak-field ligands, and $\ce{CN-}$ and CO are the strongest strong-field ligands. For the same thiocyanate ion, S-bonded coordination ($\ce{SCN-}$) gives a weak field and N-bonded coordination ($\ce{NCS-}$) a field of medium strength.

Period. For central ions of the same group and charge, the splitting energy increases in the order 3d < 4d < 5d, by about 25%–50% for each additional period: $\ce{[CrCl6]^3-}$ is $13\,600\,\mathrm{cm^{-1}}$ and $\ce{[MoCl6]^3-}$ is $19\,200\,\mathrm{cm^{-1}}$; $\ce{[RhCl6]^3-}$ is $20\,300\,\mathrm{cm^{-1}}$ and $\ce{[IrCl6]^3-}$ is $24\,900\,\mathrm{cm^{-1}}$. The 4d and 5d orbitals extend farther and interact more strongly with the ligands.

Geometry. Square planar field > octahedral field > tetrahedral field: for example, $\ce{[CoCl4]^2-}$ (tetrahedral) has only $3100\,\mathrm{cm^{-1}}$, $\ce{[Fe(CN)6]^4-}$ (octahedral) has $33\,800\,\mathrm{cm^{-1}}$, and $\ce{[Ni(CN)4]^2-}$ (square planar) reaches $35\,500\,\mathrm{cm^{-1}}$.

### 5.5.5. Pairing Energy and High-Spin and Low-Spin Complexes

How the d electrons are arranged in the split orbitals depends on a competition between two energies. By **Hund's rule**, electrons tend to occupy different orbitals with parallel spins; to place two electrons in the same orbital one must overcome the additional Coulomb repulsion between them and give up the exchange stabilization of parallel spins.

**Definition 5.5.4 (Pairing Energy)** The energy required to pair two electrons in the same orbital is called the **pairing energy**, denoted $P$.

In an octahedral field, the d¹–d³ electrons enter $t_{2g}$ in turn, and for d⁸–d¹⁰ the $t_{2g}$ set is full and the extra electrons can only enter $e_g$; each of these has only one possible arrangement. For d⁴–d⁷ there are two possibilities. If $\Delta_{\mathrm{o}} < P$ (weak field), the fourth and fifth electrons enter the higher $e_g$ orbitals rather than pair up, so that the electrons first occupy the five orbitals singly and then pair. If $\Delta_{\mathrm{o}} > P$ (strong field), the electrons first pair up in $t_{2g}$ and enter $e_g$ only after it is full.

**Definition 5.5.5** A complex with many unpaired electrons (the same number as in the free ion) is called a **high-spin complex**, and one with few unpaired electrons is called a **low-spin complex**.

Take d⁶ as an example and compare the energies of the two arrangements (with the d⁶ configuration in the spherical field as zero; by Hund's rule the free ion has one electron pair). The high-spin $t_{2g}^4e_g^2$ has energy $4(-4\,Dq) + 2(6\,Dq) = -4\,Dq$ and the same number of pairs as the free ion. The low-spin $t_{2g}^6$ has energy $6(-4\,Dq) + 2P = -24\,Dq + 2P$, with two more pairs. Low spin is more stable when $-24\,Dq + 2P < -4\,Dq$, that is, $20\,Dq > 2P$, or $\Delta_{\mathrm{o}} > P$. The same calculation for d⁴, d⁵, and d⁷ gives the same criterion:

| $\mathrm{d}^n$ | Weak field (high spin) | Unpaired electrons | Strong field (low spin) | Unpaired electrons |
|---|---|---|---|---|
| d⁴ | $t_{2g}^3e_g^1$ | 4 | $t_{2g}^4$ | 2 |
| d⁵ | $t_{2g}^3e_g^2$ | 5 | $t_{2g}^5$ | 1 |
| d⁶ | $t_{2g}^4e_g^2$ | 4 | $t_{2g}^6$ | 0 |
| d⁷ | $t_{2g}^5e_g^2$ | 3 | $t_{2g}^6e_g^1$ | 1 |

**Example 5.5.1** Use the pairing energies of the free ions ($\ce{Fe^3+}$ about $30\,000\,\mathrm{cm^{-1}}$, $\ce{Fe^2+}$ about $17\,600\,\mathrm{cm^{-1}}$, $\ce{Co^3+}$ about $21\,000\,\mathrm{cm^{-1}}$) to determine the spin state of the following complex ions.

| Complex ion | $\mathrm{d}^n$ | $\Delta_{\mathrm{o}}/\mathrm{cm^{-1}}$ | $P/\mathrm{cm^{-1}}$ | Conclusion | Unpaired electrons |
|---|---|---|---|---|---|
| $\ce{[Fe(H2O)6]^3+}$ | d⁵ | 13 700 | 30 000 | high spin $t_{2g}^3e_g^2$ | 5 |
| $\ce{[Fe(CN)6]^3-}$ | d⁵ | about 35 000 | 30 000 | low spin $t_{2g}^5$ | 1 |
| $\ce{[Fe(H2O)6]^2+}$ | d⁶ | 10 400 | 17 600 | high spin $t_{2g}^4e_g^2$ | 4 |
| $\ce{[Fe(CN)6]^4-}$ | d⁶ | 33 800 | 17 600 | low spin $t_{2g}^6$ | 0 |
| $\ce{[CoF6]^3-}$ | d⁶ | 13 000 | 21 000 | high spin | 4 |
| $\ce{[Co(NH3)6]^3+}$ | d⁶ | 22 900 | 21 000 | low spin, diamagnetic | 0 |

All conclusions agree with the magnetic measurements (5.3). The electron cloud in a complex is more expanded than in the free ion, and the actual $P$ is 15%–30% smaller than that of the free ion, so caution is needed when $\Delta_{\mathrm{o}}$ and $P$ are close. The general rules are:

- Complexes of 3d metals are commonly either high-spin or low-spin, depending mainly on the position of the ligand in the spectrochemical series.
- Complexes of 4d and 5d metals are generally low-spin: their splitting energies are large and their d orbitals are more diffuse, so the pairing energy is small.
- The splitting energy of tetrahedral complexes is only $\frac{4}{9}$ of the octahedral one and is generally smaller than the pairing energy, so they are almost always high-spin.

Crystal field theory predicts the spin state from the relative sizes of $\Delta_{\mathrm{o}}$ and $P$, whereas the inner-orbital and outer-orbital classification of valence bond theory can be assigned only afterward from the magnetic moment: low spin corresponds roughly to inner-orbital and high spin to outer-orbital complexes.

### 5.5.6. Crystal Field Stabilization Energy

**Definition 5.5.6 (Crystal Field Stabilization Energy)** The change in the total energy of the system when the d electrons pass from the unsplit d orbitals of the spherical field into the split d orbitals of the crystal field is called the **crystal field stabilization energy**, abbreviated CFSE. In an octahedral field
$$
\mathrm{CFSE} = (-4n_1 + 6n_2)\,Dq + (m_1 - m_2)P,
$$
where $n_1$ and $n_2$ are the numbers of electrons in the $t_{2g}$ and $e_g$ orbitals, and $m_1$ and $m_2$ are the numbers of electron pairs in the octahedral field and in the spherical field, respectively. A negative CFSE means stabilization.

Including the change in pairing energy in the CFSE allows the energies of the high-spin and low-spin arrangements to be compared directly. Some textbooks call only the first term the CFSE and account for the pairing energy separately; the two conventions give the same result for comparisons.

| $\mathrm{d}^n$ | Weak-field configuration | $m_1$ | $m_2$ | Weak-field CFSE | Strong-field configuration | $m_1$ | $m_2$ | Strong-field CFSE |
|---|---|---|---|---|---|---|---|---|
| d⁰ | — | 0 | 0 | $0$ | — | 0 | 0 | $0$ |
| d¹ | $t_{2g}^1$ | 0 | 0 | $-4\,Dq$ | $t_{2g}^1$ | 0 | 0 | $-4\,Dq$ |
| d² | $t_{2g}^2$ | 0 | 0 | $-8\,Dq$ | $t_{2g}^2$ | 0 | 0 | $-8\,Dq$ |
| d³ | $t_{2g}^3$ | 0 | 0 | $-12\,Dq$ | $t_{2g}^3$ | 0 | 0 | $-12\,Dq$ |
| d⁴ | $t_{2g}^3e_g^1$ | 0 | 0 | $-6\,Dq$ | $t_{2g}^4$ | 1 | 0 | $-16\,Dq + P$ |
| d⁵ | $t_{2g}^3e_g^2$ | 0 | 0 | $0$ | $t_{2g}^5$ | 2 | 0 | $-20\,Dq + 2P$ |
| d⁶ | $t_{2g}^4e_g^2$ | 1 | 1 | $-4\,Dq$ | $t_{2g}^6$ | 3 | 1 | $-24\,Dq + 2P$ |
| d⁷ | $t_{2g}^5e_g^2$ | 2 | 2 | $-8\,Dq$ | $t_{2g}^6e_g^1$ | 3 | 2 | $-18\,Dq + P$ |
| d⁸ | $t_{2g}^6e_g^2$ | 3 | 3 | $-12\,Dq$ | $t_{2g}^6e_g^2$ | 3 | 3 | $-12\,Dq$ |
| d⁹ | $t_{2g}^6e_g^3$ | 4 | 4 | $-6\,Dq$ | $t_{2g}^6e_g^3$ | 4 | 4 | $-6\,Dq$ |
| d¹⁰ | $t_{2g}^6e_g^4$ | 5 | 5 | $0$ | $t_{2g}^6e_g^4$ | 5 | 5 | $0$ |

In a weak field the CFSE of d⁰, d⁵, and d¹⁰ is zero (the electrons are distributed spherically symmetrically over the five orbitals), and d³ and d⁸ have the largest stabilization; in a strong field d⁶ has the largest stabilization. This explains why octahedral complexes of $\ce{Cr^3+}$ (d³) and of low-spin $\ce{Co^3+}$ (d⁶) are particularly stable and exchange their ligands particularly slowly.

**Example 5.5.2** The absorption peak of $\ce{[Ti(H2O)6]^3+}$ is at $20\,300\,\mathrm{cm^{-1}}$. Find its CFSE.

Solution: $\ce{Ti^3+}$ is d¹, and the absorption corresponds to the transition of the single d electron from $t_{2g}$ to $e_g$, so $\Delta_{\mathrm{o}} = 20\,300\,\mathrm{cm^{-1}}$. For the ground state $t_{2g}^1$,
$$
\mathrm{CFSE} = -0.4\Delta_{\mathrm{o}} = -8120\,\mathrm{cm^{-1}} = -\frac{8120}{83.59}\,\mathrm{kJ\,mol^{-1}} = -97.1\,\mathrm{kJ\,mol^{-1}}.
$$

### 5.5.7. Applications of Crystal Field Theory

Magnetism. From $\Delta_{\mathrm{o}}$ and $P$ we predict the high-spin or low-spin state and the number of unpaired electrons, and then the magnetic moment from the spin-only formula (5.5.5).

Color. A d electron absorbs light of a certain frequency and jumps from a lower d orbital to a higher one (a d–d transition). The energy of the absorbed **photon**, $h\nu = hc\tilde\nu$, is comparable to the splitting energy and lies in the visible region. After the absorbed part is removed from white light, the transmitted (or reflected) light appears as the complementary color of the absorbed light. $\ce{[Ti(H2O)6]^3+}$ absorbs blue-green light near $20\,300\,\mathrm{cm^{-1}}$ (about $490\,\mathrm{nm}$), and the solution is purple-red. The larger the splitting energy, the more the absorption peak shifts toward shorter wavelengths: for example, $\ce{[Cu(H2O)6]^2+}$ absorbs orange-red light and is blue, and on adding $\ce{NH3}$ the splitting energy increases, the absorption shifts to yellow-orange light, and the solution turns deep blue-violet.

| Color of absorbed light | violet | blue | blue-green | green | yellow | orange | red |
|---|---|---|---|---|---|---|---|
| Wavelength/nm | 400–435 | 435–480 | 480–500 | 500–560 | 560–595 | 595–610 | 610–750 |
| Observed color (complementary) | yellow-green | yellow | orange-red | purple-red | blue-violet | green-blue | blue-green |

![The d–d absorption band of [Ti(H2O)6]3+ (schematic): the peak is near 20 300 cm−1, and the shoulder on the low-wavenumber side comes from Jahn–Teller splitting of the excited state; the visible spectrum is shown below](./plots/ti-absorption.py)

Ions with d⁰ ($\ce{Sc^3+}$, $\ce{Ti^4+}$) and d¹⁰ ($\ce{Zn^2+}$, $\ce{Cu+}$, $\ce{Ag+}$) have no d–d transitions, and their aqua ions are colorless. The intensity of the color depends on the transition probability. In complexes with a center of symmetry such as $\ce{[M(H2O)6]^{n+}}$ the d–d transition is parity-forbidden and occurs weakly only because molecular vibrations break the symmetry, so these solutions are pale. For high-spin d⁵ $\ce{[Mn(H2O)6]^2+}$ the d–d transition must in addition change the spin and is spin-forbidden, so the color is a very faint pink. $\ce{MnO4-}$ and $\ce{CrO4^2-}$ are d⁰ yet intensely colored, because their color comes from ligand-to-metal charge-transfer transitions rather than d–d transitions ([Structural Chemistry](/6.2)). The colors of common aqua ions of the first transition series are: $\ce{Ti^3+}$ purple-red, $\ce{V^3+}$ green, $\ce{Cr^3+}$ violet, $\ce{Cr^2+}$ sky blue, $\ce{Mn^2+}$ very faint pink, $\ce{Fe^2+}$ pale green, $\ce{Co^2+}$ pink, $\ce{Ni^2+}$ green, and $\ce{Cu^2+}$ blue.

Hydration enthalpy. The hydration enthalpy $\Delta_{\mathrm{hyd}}H$ of gaseous $\ce{M^2+}$ ions of the first transition series is the enthalpy change of the reaction
$$
\ce{M^2+(g) + 6H2O(l) -> [M(H2O)6]^2+(aq)}.
$$
From $\ce{Ca^2+}$ to $\ce{Zn^2+}$ the ionic radius decreases steadily, so the magnitude of the hydration enthalpy should increase smoothly. In fact only $\ce{Ca^2+}$ (d⁰), $\ce{Mn^2+}$ (high-spin d⁵), and $\ce{Zn^2+}$ (d¹⁰), whose CFSE is zero, lie on a smooth curve; all the other ions lie below it (more exothermic), giving a "double hump" with extrema near d³ and d⁸. The size of the deviation is close to the weak-field CFSE obtained from spectra, and after subtracting the CFSE the points essentially return to the smooth curve. This is the most convincing thermochemical evidence for crystal field theory. The same double hump appears in the lattice enthalpies of $\ce{MCl2}$ and in the ionic radii of $\ce{M^2+}$.

![Hydration enthalpies of first-series M2+ ions (left): the d0, d5, and d10 points lie on a smooth baseline and the others lie below it; variation of the weak-field octahedral CFSE with the number of d electrons (right)](./plots/hydration-cfse.py)

Jahn–Teller effect. In the configuration $t_{2g}^6e_g^3$ of $\ce{Cu^2+}$ (d⁹), three electrons occupy two degenerate $e_g$ orbitals, and whichever orbital holds the extra electron, the electron distribution no longer matches the symmetry of a regular octahedron.

**Definition 5.5.7 (Jahn–Teller Effect)** The phenomenon in which a nonlinear molecule with asymmetrically occupied degenerate orbitals spontaneously undergoes a geometric distortion that removes the degeneracy and lowers the energy is called the **Jahn–Teller effect**.

$\ce{[Cu(H2O)6]^2+}$ elongates along the $z$ axis: the repulsion on $\mathrm{d}_{z^2}$ decreases and its energy drops, so it holds two electrons, whereas $\mathrm{d}_{x^2-y^2}$ rises in energy and holds only one, and the total energy of the system is lowered. As a result the two axial Cu–O bonds are clearly longer than the four in the equatorial plane. In the extreme, when the elongation is so great that the two axial ligands almost leave, one arrives at square planar complexes such as $\ce{[Cu(NH3)4]^2+}$, with no need to assume, as valence bond theory does, that a 3d electron is promoted to 4p. Octahedral complexes of high-spin d⁴ ($\ce{Cr^2+}$, $\ce{Mn^3+}$) and low-spin d⁷ also show clear Jahn–Teller distortions. The general theorem behind this effect is given in [Structural Chemistry](/6.2).

### 5.5.8. Limitations of Crystal Field Theory

Crystal field theory treats ligands as point charges and ignores covalent interactions between metal and ligands altogether, so it cannot explain the spectrochemical series: in an electrostatic model, negatively charged $\ce{F-}$ and $\ce{OH-}$ should produce a stronger field than neutral $\ce{NH3}$ and CO, whereas the opposite is observed. There is ample evidence for covalency in complexes, such as the hyperfine coupling of unpaired electrons to ligand nuclei in electron paramagnetic resonance spectra and the smaller repulsion between d electrons in complexes than in free ions (expansion of the electron cloud).

The remedy is to consider electrostatic interaction and orbital overlap together, which leads to ligand field theory and the molecular orbital theory of complexes. In the molecular orbital picture $e_g$ is the σ antibonding orbital between metal and ligand, and $t_{2g}$ interacts with the π orbitals of the ligands. Ligands with empty π* orbitals such as CO and $\ce{CN-}$ form π back-bonds, which lowers $t_{2g}$ and increases $\Delta_{\mathrm{o}}$, so they are strong-field ligands; ligands with filled π orbitals such as the halide ions and $\ce{OH-}$ raise $t_{2g}$ and decrease $\Delta_{\mathrm{o}}$, so they are weak-field ligands. These topics are treated in [Structural Chemistry](/6.2).

## Summary

| | Valence bond theory | Crystal field theory |
|---|---|---|
| Nature of bonding | lone pairs of the ligands enter hybrid orbitals of the central atom to form coordinate covalent bonds | electrostatic interaction between central ion and ligands |
| Geometry | determined by hybridization ($\mathrm{sp}^3$ tetrahedral, $\mathrm{dsp}^2$ square planar, $\mathrm{d}^2\mathrm{sp}^3$ octahedral, …) | determined jointly by ligand repulsion and the CFSE of the d electrons |
| Magnetism | inner-orbital or outer-orbital, to be judged from the magnetic moment | high or low spin predicted from $\Delta_{\mathrm{o}}$ and $P$ |
| Color and spectra | cannot explain | d–d transitions, $h\nu \approx \Delta$ |
| Thermodynamic properties | cannot explain | CFSE explains the double humps of hydration and lattice enthalpies |
| Main defects | cannot predict, does not treat excited states | ignores covalency, cannot explain the spectrochemical series |

The structure of a complex is determined by the central atom, the ligands, and the coordination number: the coordination polyhedron gives the geometry, and the relative positions of the ligands and chirality give geometric and optical isomerism; the effective magnetic moment gives the number of unpaired electrons. Crystal field theory unifies magnetism, color, and stability through the comparison of a single parameter $\Delta$ with the pairing energy $P$, and its shortcomings are remedied by ligand field theory.
