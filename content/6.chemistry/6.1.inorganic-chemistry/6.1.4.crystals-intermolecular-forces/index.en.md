---
title: Crystal Structures and Intermolecular Forces
source_hash: 6d1e25582604
---

The previous chapter dealt with chemical bonds within single molecules; this chapter deals with how large numbers of particles aggregate into solids. By the type of force between the particles, crystals fall into four classes: metallic, ionic, molecular and covalent network crystals. The first two are held together by the nondirectional metallic and ionic bonds, and their particles pack as closely as rigid spheres; molecular crystals are held together by van der Waals forces and hydrogen bonds, which are much weaker than chemical bonds; covalent network crystals are joined into a single whole by directional covalent bonds. This chapter discusses in turn the packing of equal spheres (the geometric basis of metallic and ionic crystal structures), metallic bonding and energy bands, lattice enthalpy and structure types of ionic crystals, ionic polarization, intermolecular forces and hydrogen bonding, and finally covalent network crystals and crystal defects.

The chapter uses many results of the preceding ones: the concepts of **crystal**, **crystal lattice**, **unit cell** and crystal system are in [6.1.1](/6.1.1#sec-1.3); the charge, electron configuration and radius of ions, bond polarity and the **electric dipole moment** are in [6.1.3](/6.1.3); the physics of energy bands and semiconductors is in [5.5.6](/5.5.6); the Lennard-Jones model of intermolecular interaction and the van der Waals equation are in [5.2.2](/5.2.2#sec-2.2). Crystal symmetry and space groups, the derivation of the Madelung constant and the lattice energy formula, and structure determination by X-ray diffraction belong to [structural chemistry](/6.2).

## 4.1. Types of Crystals and the Packing of Equal Spheres

### 4.1.1. The Four Classes of Crystals

**Definition 4.1.1** By the particles that compose the crystal and the forces between them, crystals fall into four classes: the **metallic crystal**, in which metal atoms (ions) are bound by the metallic bond; the **ionic crystal**, in which cations and anions are bound by ionic bonds; the **molecular crystal**, in which molecules are bound by intermolecular forces (and hydrogen bonds); and the **covalent network crystal**, in which atoms are joined into a three-dimensional network by covalent bonds.

| Type | Particles | Forces | Melting point, hardness | Electrical conductivity | Examples |
|---|---|---|---|---|---|
| Metallic crystal | Metal atoms and ions | Metallic bond | Widely varying | Conducts as solid and liquid | Na, Cu, W |
| Ionic crystal | Cations and anions | Ionic bond | Fairly high, hard and brittle | Insulating as a solid; conducts when molten or dissolved in water | NaCl, MgO |
| Molecular crystal | Molecules | van der Waals forces, hydrogen bonds | Low, soft | Insulating | Dry ice, ice, $\ce{I2}$ |
| Covalent network crystal | Atoms | Covalent bonds | Very high, very hard | Generally insulating (Si and others are semiconductors) | Diamond, $\ce{SiO2}$, SiC |

Real crystals include intermediate cases: in graphite the bonds within layers are covalent and those between layers are intermolecular forces (Section 4.5.2); ionic polarization gives many ionic crystals some covalent character (Section 4.3.5).

### 4.1.2. Coordination Number and the Packing of Equal Spheres

Metallic and ionic bonds are neither directional nor saturable, so metal atoms and ions can be treated approximately as rigid spheres that pack in the crystal as closely as possible to minimize the energy. First consider the packing of spheres of equal size (equal spheres).

**Definition 4.1.2 (Coordination Number)** The number of atoms (or ions) nearest to a given atom (or ion) in a crystal is called its **coordination number**.

The coordination number measures how closely the spheres are packed. The common packings of equal spheres are:

- Simple cubic packing: each layer of spheres forms a square array, with each sphere directly above one in the layer below. The coordination number is 6 and the unit cell is simple cubic; only Po adopts this structure.
- Body-centered cubic packing: spheres lie at the 8 corners and the body center of a cube, and the sphere at the center touches the 8 corner spheres (tangent along the body diagonal). The coordination number is 8 (there are also 6 next-nearest neighbors only 15% farther away).
- Close packing: within a plane each sphere touches 6 others, forming the most compact layer (figure below, left, called layer A). Each sphere of layer A is surrounded by 6 hollows, which fall into two sets (B sites and C sites), and the spheres of the second layer can sit on only one set (called layer B). There are two ways to place the third layer: directly above layer A, repeating in the sequence ABAB…; or on the C sites, repeating in the sequence ABCABC….

**Definition 4.1.3** The packing in which equal spheres are stacked layer by layer in the most compact way, with 6 spheres around 1 in each layer and each sphere touching 6 in its own layer and 3 in each of the layers above and below (coordination number 12), is called **close packing**. Repetition in the sequence ABAB… is called **hexagonal close packing** (hcp), whose unit cell belongs to the hexagonal system; repetition in the sequence ABCABC… is called **cubic close packing** (ccp), whose unit cell is face-centered cubic, with the close-packed layers perpendicular to the body diagonal of the cube. The packing in which spheres lie at the 8 corners and the body center of a cubic cell, with coordination number 8, is called **body-centered cubic packing** (bcc).

![Close-packed layers seen from above. Left: one layer A and the two sets of hollows (B and C sites) on which the next layer can sit. Right: layers A and B, with the tetrahedral holes (under each B sphere and over each A sphere) and the octahedral holes between them (at the C positions)](./plots/close-packed-layers.py)

![Unit cells of simple cubic, body-centered cubic, cubic close packing (face-centered cubic cell) and hexagonal close packing, with coordination numbers and packing efficiencies](./plots/packing-unit-cells.py)

The hcp and ccp packings have the same coordination number and the same packing efficiency (Section 4.1.3) and differ only in the position of the third layer; their energies differ very little, so some metals adopt different close-packed structures under different conditions (such as Co).

### 4.1.3. Packing Efficiency

**Definition 4.1.4 (Packing Efficiency)** The ratio of the total volume of the spheres in a unit cell to the volume of the cell is called the **packing efficiency**.

**Example 4.1.1** Let the radius of the spheres be $r$ and the edge of the cubic cell be $a$.

- Simple cubic: each cell contains 1 sphere, tangent along the edges, $a = 2r$, and the packing efficiency is $\frac{\frac43\pi r^3}{(2r)^3} = \frac{\pi}{6} = 52.4\%$.
- Body-centered cubic: each cell contains $8\times\frac18 + 1 = 2$ spheres, tangent along the body diagonal, $\sqrt{3}a = 4r$, and the packing efficiency is $\frac{2\cdot\frac43\pi r^3}{(4r/\sqrt3)^3} = \frac{\sqrt3\pi}{8} = 68.0\%$.
- Face-centered cubic: each cell contains $8\times\frac18 + 6\times\frac12 = 4$ spheres, tangent along the face diagonal, $\sqrt{2}a = 4r$, and the packing efficiency is $\frac{4\cdot\frac43\pi r^3}{(2\sqrt2 r)^3} = \frac{\pi}{3\sqrt2} = 74.0\%$.

The packing efficiency of hcp is also $74.0\%$. Kepler conjectured in 1611 that this is the maximum density of packing of equal spheres, and this "Kepler conjecture" was proved only in 1998, by Hales with the aid of a computer.

The density of a crystal can be calculated from the lattice parameters: copper is ccp with $a = 361.5\,\mathrm{pm}$ and $M = 63.55\,\mathrm{g\,mol^{-1}}$, so

$$
\rho = \frac{4M}{N_{\mathrm{A}}a^3} = \frac{4\times 63.55\,\mathrm{g\,mol^{-1}}}{6.022\times10^{23}\,\mathrm{mol^{-1}}\times(3.615\times10^{-8}\,\mathrm{cm})^3} = 8.93\,\mathrm{g\,cm^{-3}},
$$
in agreement with the measured value of $8.96\,\mathrm{g\,cm^{-3}}$. Conversely, the Avogadro constant can be found from the density and lattice parameters, which was an accurate method of determining $N_{\mathrm{A}}$ (silicon single-crystal spheres, before the 2019 SI revision).

### 4.1.4. Tetrahedral and Octahedral Holes

In close packing 26% of the space is still empty. The holes are of two kinds:

**Definition 4.1.5** In close packing, the hole enclosed by 3 spheres of one layer and 1 sphere of the adjacent layer, at the center of a regular tetrahedron and equidistant from the centers of these 4 spheres, is called a **tetrahedral hole**; the hole enclosed by 3 spheres of one layer and 3 staggered spheres of the adjacent layer, at the center of a regular octahedron, is called an **octahedral hole**.

In a close packing of $N$ spheres there are $N$ octahedral holes and $2N$ tetrahedral holes. Take the face-centered cubic cell of ccp as an example: the cell contains 4 spheres; the octahedral holes are at the body center and the midpoints of the 12 edges, $1 + 12\times\frac14 = 4$ in all; the tetrahedral holes are at the centers of the 8 small cubes (obtained by bisecting each edge of the cell), 8 in all.

The radius of the largest small sphere that fits into a hole without pushing the surrounding spheres apart is $0.225r$ for a tetrahedral hole and $0.414r$ for an octahedral hole (the derivation is exactly the same as for the radius ratios in Section 4.3.4). In ionic crystals the smaller cations often fill holes in a close packing of anions, and small atoms such as H, C and N in metals can also fill the holes of the metal (Section 4.2.4).

## 4.2. Metallic Crystals

### 4.2.1. Crystal Structures of Metals

About $\frac23$ of the metals adopt close packing (coordination number 12), most of the rest are body-centered cubic (coordination number 8), and a very few are simple cubic (coordination number 6):

| Structure | Examples |
|---|---|
| ccp | Cu, Ag, Au, Al, Ni, Pb, Pt, γ-Fe |
| hcp | Mg, Zn, Cd, Ti, Co, Be |
| bcc | Li, Na, K, Cr, Mo, W, α-Fe |

The same metal can have different crystal structures at different temperatures and pressures. Iron has three at ordinary pressure: α-Fe, bcc, below $912\,{}^\circ\mathrm{C}$; γ-Fe, ccp, from $912$ to $1394\,{}^\circ\mathrm{C}$; and δ-Fe, bcc again, from $1394\,{}^\circ\mathrm{C}$ to the melting point of $1538\,{}^\circ\mathrm{C}$. The octahedral holes of γ-Fe are larger and dissolve more carbon, which is the basis of the heat treatment (quenching) of steel.

Metallic crystals have high density, good electrical and thermal conductivity, metallic luster and good ductility and malleability, while melting points and hardness differ enormously (Hg $-38.8\,{}^\circ\mathrm{C}$, W $3422\,{}^\circ\mathrm{C}$). These properties are explained by the metallic bond.

### 4.2.2. The Metallic Bond and the Electron-Sea Model

Metal atoms have few valence electrons and low ionization energy, which is not enough for localized covalent bonds between the atoms.

**Definition 4.2.1 (Metallic Bond)** The interaction in which the valence electrons of a metal leave the atoms, move freely throughout the crystal, are shared by all the metal ions and bind the metal ions together is called the **metallic bond**.

This picture is called the electron-sea model: the metal ions are immersed in a "sea" of valence electrons. It explains the properties of metals qualitatively:

- Electrical conductivity: free electrons move directionally under an electric field;
- Thermal conductivity: the motion of free electrons rapidly spreads thermal motion through the whole crystal;
- Metallic luster: free electrons can absorb visible light of all frequencies and re-emit it immediately, so metals are opaque and lustrous;
- Ductility and malleability: when layers of metal ions slide over one another the "gluing" action of the electron sea is not disturbed and the metallic bonds do not break (ionic crystals are different, see Section 4.3.1);
- High density: the metallic bond is neither directional nor saturable, and the atoms adopt close packing.

The electron-sea model is the **free electron gas** model of physics ([5.5.6](/5.5.6#sec-6.1.2)); it cannot explain why some solids conduct and others do not, which requires band theory.

### 4.2.3. Band Theory

Band theory can be viewed as the extension of molecular orbital theory to crystals: the atomic orbitals of two atoms form one bonding and one antibonding orbital ([6.1.3](/6.1.3#sec-3.6.1)), and the same atomic orbital on $N$ atoms forms $N$ molecular orbitals. For $N \sim 10^{23}$ the spacing of these molecular orbital levels is extremely small and they can be treated as continuous **energy bands** ([5.5.6](/5.5.6#sec-6.2.1)).

Take lithium metal ($1\mathrm{s}^2 2\mathrm{s}^1$) as an example:

- The $N$ 1s orbitals form the 1s band, which can hold $2N$ electrons; the $2N$ 1s electrons just fill it, so it is a **filled band**;
- The $N$ 2s orbitals form the 2s band, which can hold $2N$ electrons; there are only $N$ 2s electrons, so it is only half filled and is a partially filled band;
- The 2p band holds no electrons and is an **empty band**; it partly overlaps the 2s band;
- The energy interval between bands in which no electron states exist is the **band gap**.

An electric field can excite electrons in a partially filled band to nearby empty levels of the same band, producing a current; electrons in a filled band have nowhere to go and do not conduct ([5.5.6](/5.5.6#sec-6.3.1)). Lithium conducts precisely because 2s is a partially filled band. The 3s band of magnesium ($3\mathrm{s}^2$) is exactly filled, but it overlaps the empty 3p band and together they form a partially filled band, so magnesium is also a metal.

By band structure, solids are classified as conductors, semiconductors and insulators ([5.5.6](/5.5.6#def-6.3.1)): a **conductor** has a partially filled band, or a filled band overlapping an empty one; a **semiconductor** and an **insulator** have only a filled band (the **valence band**) and an empty band (the **conduction band**) and differ in the band gap $E_{\mathrm{g}}$: the $E_{\mathrm{g}}$ of semiconductors is small (Si $1.12\,\mathrm{eV}$, Ge $0.66\,\mathrm{eV}$), a few electrons are thermally excited into the conduction band at room temperature, leaving **holes** in the valence band, and both take part in conduction; the $E_{\mathrm{g}}$ of insulators is very large (diamond $5.5\,\mathrm{eV}$) and electrons can hardly be excited.

The band gap of semiconductor nanocrystals also depends on particle size. Electrons confined in a particle a few nanometers across behave like particles in a potential well ([5.5.3](/5.5.3)), and the level spacing is inversely proportional to the square of the particle size: the smaller the particle, the larger $E_{\mathrm{g}}$ and the shorter the wavelength of the emitted light. This is called the *quantum size effect*. Bulk CdSe has $E_{\mathrm{g}} = 1.74\,\mathrm{eV}$ (corresponding to deep red light of about $710\,\mathrm{nm}$), and the emission of CdSe quantum dots $2$–$7\,\mathrm{nm}$ in diameter can be tuned continuously from blue to red, and has been used in displays. The discovery and synthesis of quantum dots was awarded the 2023 Nobel Prize in Chemistry.

### 4.2.4. Alloys

**Definition 4.2.2 (Alloy)** A substance composed of two or more elements (at least one of them a metal) and having metallic properties is called an **alloy**.

An alloy in which solute atoms dissolve in the lattice of the solvent metal and the solvent crystal structure is retained is called a *solid solution*; by the positions of the solute atoms there are two kinds:

- Substitutional solid solutions: solute atoms replace some atoms in the lattice of the solvent metal. This requires that the two kinds of atoms have similar radii (generally differing by no more than 15%) and similar crystal structures and electronegativities. For example in brass Zn replaces Cu in the ccp lattice of Cu; Cu and Ni are miscible in all proportions.
- Interstitial solid solutions: small nonmetal atoms (H, B, C, N) fill the holes in the metal packing. For example C in steel lies in the octahedral holes of γ-Fe. The interstitial atoms hinder sliding between layers of metal atoms and markedly raise the hardness and strength of the alloy.

There are also *intermetallic compounds* of fixed composition whose structure differs from that of the component metals, such as the $\ce{Nb3Sn}$ superconductor and the $\ce{LaNi5}$ hydrogen-storage alloy.

## 4.3. Ionic Crystals

### 4.3.1. Characteristics of Ionic Crystals

The electrostatic attraction between ions is strong, so ionic crystals generally have high melting and boiling points and considerable hardness. But ionic crystals are brittle: when an external force displaces a layer of ions by half a period, ions of like charge face each other and the repulsion makes the crystal fracture along a cleavage plane. In the solid state the ions of an ionic crystal can only vibrate about their equilibrium positions and the crystal does not conduct; when molten or dissolved in water the ions move freely and conduct electricity.

### 4.3.2. Lattice Enthalpy

The strength of the ionic bond is measured by the lattice enthalpy.

**Definition 4.3.1 (Lattice Enthalpy)** The enthalpy change for the dissociation of $1\,\mathrm{mol}$ of an ionic crystal into gaseous cations and anions far apart from one another under standard conditions,

$$
\ce{M_aX_b (s) -> a M^{b+} (g) + b X^{a-} (g)},\qquad \Delta_{\mathrm{latt}}H^\circ,
$$
is called the **lattice enthalpy** of the crystal. It is always positive, and a larger value means a stronger ionic bond.

Chinese textbooks often call it the lattice energy, write it $U$ and define it as the energy released when gaseous ions combine to form the crystal. In IUPAC notation $U$ is the internal energy, and here the lattice enthalpy $\Delta_{\mathrm{latt}}H^\circ$ is used instead, positive in the direction of dissociation. Strictly speaking the lattice energy at $0\,\mathrm{K}$ (the internal energy change) and the lattice enthalpy at $298\,\mathrm{K}$ differ by a few $RT$, only a few $\mathrm{kJ\,mol^{-1}}$, which can be neglected in comparisons.

Lattice enthalpy cannot be measured directly. It is usually found indirectly from experimental data such as enthalpies of formation and sublimation, ionization energies and electron affinities by Hess's law, which is the [Born–Haber cycle](/6.1.6); it can also be calculated from an electrostatic model (the Born–Landé equation, in which the Madelung constant depends on the crystal structure, see [structural chemistry](/6.2)). The main regularity given by the electrostatic model is that the lattice enthalpy is approximately proportional to $\frac{z_+z_-}{r_+ + r_-}$ ($z_\pm$ the charge numbers of the ions). The higher the ionic charges and the smaller the internuclear distance, the larger the lattice enthalpy, the higher the melting point and the greater the hardness of the crystal:

| Crystal | NaF | NaCl | NaBr | NaI | KCl | KBr | MgO | CaO | BaO |
|---|---|---|---|---|---|---|---|---|---|
| $r_+ + r_-$ / pm | 235 | 283 | 298 | 322 | 319 | 334 | 212 | 240 | 275 |
| $\Delta_{\mathrm{latt}}H^\circ$ / (kJ mol⁻¹) | 923 | 786 | 747 | 704 | 715 | 689 | 3791 | 3401 | 3054 |
| Melting point / °C | 996 | 801 | 747 | 661 | 771 | 734 | 2825 | 2613 | 1973 |

$\ce{MgO}$ and $\ce{NaCl}$ have the same structure, the ratio of $z_+z_-$ is $4$ and the ratio of internuclear distances is $283/212$, so by the electrostatic model the ratio of lattice enthalpies is about $4\times 283/212 = 5.3$, against the measured $3791/786 = 4.8$, in rough agreement; the melting point of $\ce{MgO}$ is as high as $2825\,{}^\circ\mathrm{C}$, and it is a common refractory material.

### 4.3.3. Structure Types of Ionic Crystals

The ionic bond is neither directional nor saturable, and ionic crystals also tend to close packing; but cations and anions differ in size and charge, so generally the larger anions form the packing and the smaller cations fill the holes, while electroneutrality is maintained and ions of opposite charge are kept in contact as far as possible. The six common structure types are:

| Structure type | Arrangement of anions | Positions of cations | Coordination ratio | Formula units per cell | Examples |
|---|---|---|---|---|---|
| NaCl type (rock salt) | ccp | All octahedral holes | 6:6 | 4 | NaCl, LiCl, KBr, AgCl, MgO, CaO, CaS |
| CsCl type | Simple cubic | Cubic hole (body center) | 8:8 | 1 | CsCl, CsBr, CsI, TlCl |
| Cubic ZnS type (zinc blende) | ccp | Half of the tetrahedral holes (alternating) | 4:4 | 4 | ZnS, CuCl, CuBr, CuI, CdS, GaAs |
| Hexagonal ZnS type (wurtzite) | hcp | Half of the tetrahedral holes | 4:4 | 2 | ZnS, ZnO, BeO, AgI, GaN |
| $\ce{CaF2}$ type (fluorite) | Cations ccp | Anions occupy all the tetrahedral holes | 8:4 | 4 | $\ce{CaF2}$, $\ce{SrF2}$, $\ce{BaF2}$, $\ce{UO2}$, $\ce{ThO2}$ |
| Rutile type ($\ce{TiO2}$) | Approximately hcp (distorted) | Half of the octahedral holes | 6:3 | 2 | $\ce{TiO2}$, $\ce{SnO2}$, $\ce{MnO2}$, $\ce{PbO2}$, $\ce{MgF2}$ |

In addition, in the perovskite structure of type $\mathrm{ABX_3}$ the larger A ions and the X ions together form a ccp, and the smaller B ions occupy the $\frac14$ of the octahedral holes that are surrounded entirely by X: the coordination number of A is 12 and that of B is 6, and the ideal cubic cell contains one $\mathrm{ABX_3}$ ($\ce{SrTiO3}$; $\ce{CaTiO3}$ itself has a distorted orthorhombic structure). $\ce{BaTiO3}$ is an important ferroelectric and piezoelectric material, and halide perovskites (such as $\ce{CH3NH3PbI3}$) are new solar cell materials.

Exchanging the positions of cations and anions in the fluorite type gives the antifluorite type ($\ce{Li2O}$, $\ce{Na2O}$, $\ce{K2O}$). The CsCl type looks like body-centered cubic, but the ions at the body center and the corners differ and its lattice is simple cubic ([6.1.1](/6.1.1#sec-1.3.3)).

![Unit cells of six ionic structure types. Green: anions; orange: smaller cations; blue: the large A cations of perovskite. Lines join nearest neighbors](./plots/ionic-structures.py)

### 4.3.4. The Radius Ratio Rule

Among AB-type crystals of the cubic system, NaCl is 6-coordinate, CsCl is 8-coordinate and ZnS is 4-coordinate. The coordination number depends mainly on the radius ratio $r_+/r_-$ of cation to anion: the larger the cation, the more anions can be accommodated around it; but when the cation is too small the anions touch one another while cation and anions lose contact, the structure is unstable and the coordination number must be lowered.

**Proposition 4.3.1 (Critical Radius Ratios for Coordination Numbers)** Treating ions as rigid spheres, the radius ratios at which the cation touches all $n$ surrounding anions and the anions also just touch one another are:

| Coordination number | Coordination polyhedron | Critical $r_+/r_-$ |
|---|---|---|
| 3 | Equilateral triangle | $\frac{2}{\sqrt3} - 1 = 0.155$ |
| 4 | Regular tetrahedron | $\sqrt{\frac32} - 1 = 0.225$ |
| 6 | Regular octahedron | $\sqrt2 - 1 = 0.414$ |
| 8 | Cube | $\sqrt3 - 1 = 0.732$ |
| 12 | Cuboctahedron | $1$ |

**Proof** Six-coordinate: the central cation of an octahedron is coplanar with the 4 anions in the equatorial plane, and these 4 anions form a square. When the anions just touch, the side of the square is $2r_-$; when cation and anions touch, the diagonal is $2(r_+ + r_-)$. So $2(r_+ + r_-) = \sqrt2\cdot 2r_-$ and $r_+/r_- = \sqrt2 - 1$.

Eight-coordinate: the 8 anions are at the corners of a cube and touch along the edges, $a = 2r_-$; the cation is at the body center and touches the anions along the body diagonal, $\sqrt3 a = 2(r_+ + r_-)$. So $r_+/r_- = \sqrt3 - 1$.

Four-coordinate: the 4 anions are at 4 alternate corners of a cube and form a regular tetrahedron, touching along the face diagonals, $\sqrt2 a = 2r_-$; the cation is at the center of the cube, at a distance $\frac{\sqrt3}{2}a = r_+ + r_-$ from the corners. So $r_+ + r_- = \frac{\sqrt3}{2}\cdot\sqrt2 r_- = \sqrt{\tfrac32}\,r_-$ and $r_+/r_- = \sqrt{\tfrac32} - 1$.

Three-coordinate: the 3 anions form an equilateral triangle of side $2r_-$, with the cation at the center, and the distance from the center to a corner is $\frac{2r_-}{\sqrt3} = r_+ + r_-$. For the 12-coordinate cuboctahedron the distance from the center to a vertex equals the edge length, so $r_+ = r_-$. $\square$

![Radius-ratio rule. Left and middle: the critical contact geometries for coordination numbers 6 and 8. Right: AX compounds placed by r₊/r₋ (Shannon radii) against their observed coordination number](./plots/radius-ratio.py)

**Definition 4.3.2 (Radius Ratio Rule)** The coordination number of a cation in an ionic crystal is determined by the radius ratio $r_+/r_-$: for $r_+/r_-$ between $0.225$ and $0.414$ it is 4 (ZnS type), between $0.414$ and $0.732$ it is 6 (NaCl type), and between $0.732$ and $1$ it is 8 (CsCl type). This empirical rule is called the **radius ratio rule**.

When $r_+/r_-$ is smaller than the critical value for a coordination number, the anions touch one another and cation and anions lose contact ("like ions touching, unlike ions apart"), which is unstable; above the critical value unlike ions touch and like ions are apart, which is stable; so each coordination number applies from its critical value up to the critical value of the next higher coordination number.

The radius ratio rule gives the correct coordination number for most strongly ionic crystals ($\ce{NaCl}$ $0.56$, $\ce{MgO}$ $0.51$, $\ce{CsCl}$ $0.96$; in $\ce{CaF2}$ the $0.84$ of $\ce{Ca^2+}$ corresponds to 8-coordination, and in $\ce{TiO2}$ the $0.43$ of $\ce{Ti^4+}$ to 6-coordination), but there are many exceptions (right of the figure above):

- Among the alkali halides, $\ce{KCl}$ (0.76) and $\ce{RbCl}$ (0.84) have radius ratios above 0.732 but are of the NaCl type at ordinary pressure: the energy difference between 6- and 8-coordination is only a few percent, and factors other than the radius ratio are enough to change the result.
- $\ce{AgI}$ (0.45), $\ce{CuCl}$ and others have radius ratios in the 6-coordinate range but are in fact 4-coordinate, of the ZnS type: ionic polarization gives the bond considerable covalent character (Section 4.3.5).

Ions are not rigid spheres, and the ionic radius itself depends on the coordination number and the radius system used, so the radius ratio rule can serve only as a rough criterion.

### 4.3.5. Ionic Polarization

Under the electric field of the surrounding ions of opposite charge, the electron cloud of an ion is deformed, the centers of positive and negative charge no longer coincide and an induced dipole arises (the same as the **displacement polarization** of dielectrics, [5.3.4](/5.3.4#def-4.2.2)).

**Definition 4.3.3** The deformation of the electron cloud of an ion under the electric field of other ions is called **ionic polarization**. The ability of an ion to deform other ions is called its **polarizing power**; the ease with which the electron cloud of an ion is deformed by an external electric field is called its **polarizability** (deformability), and in an external field $\boldsymbol{E}$ the induced dipole is $\boldsymbol{p} = \alpha\boldsymbol{E}$, a larger $\alpha$ meaning easier deformation.

Cations have small radii and concentrated charge and mainly show polarizing power; anions have large radii and outer electrons less tightly held by the nucleus and mainly show deformability. The regularities (Fajans' rules) are as follows.

Polarizing power of cations:

- The higher the charge and the smaller the radius, the stronger the polarizing power: $\ce{Na+} < \ce{Mg^2+} < \ce{Al^3+}$; $\ce{Ba^2+} < \ce{Mg^2+}$;
- For the same charge and similar radius it depends on the electron configuration: 8-electron < 9–17-electron < 18-electron and 18+2-electron (and the 2-electron $\ce{Li+}$ and $\ce{Be^2+}$): for example $\ce{Na+}$, $\ce{Mg^2+}$ < $\ce{Fe^2+}$, $\ce{Ni^2+}$ < $\ce{Ag+}$, $\ce{Pb^2+}$. The d electrons shield the nuclear charge poorly, and ions of the 18-electron configuration have a larger effective nuclear charge.

Deformability of ions:

- For the same electron configuration, the higher the negative charge and the lower the positive charge, the greater the deformability: $\ce{Si^4+} < \ce{Al^3+} < \ce{Mg^2+} < \ce{Na+} < \ce{F-} < \ce{O^2-}$;
- The more electron shells, the greater the deformability: $\ce{Li+} < \ce{Na+} < \ce{K+} < \ce{Rb+} < \ce{Cs+}$, $\ce{F-} < \ce{Cl-} < \ce{Br-} < \ce{I-}$;
- Among cations those of the 18-, 18+2- and 9–17-electron configurations also have considerable deformability, and their mutual polarization with easily deformed anions (additional polarization) strengthens the polarization further;
- Complex anions have low deformability, with the rough order $\ce{ClO4-} < \ce{F-} < \ce{NO3-} < \ce{OH-} < \ce{CN-} < \ce{Cl-} < \ce{Br-} < \ce{I-}$.

Ionic polarization makes the electron clouds of cations and anions overlap, shortens the internuclear distance and moves the bond type from ionic toward covalent:

```mermaid
flowchart LR
  A["Ideal ionic bond<br/>(no polarization)"] --> B["Essentially ionic<br/>(slight polarization)"] --> C["Intermediate bond type<br/>(stronger polarization)"] --> D["Essentially covalent<br/>(strong polarization)"]
```

For example $\ce{NaCl}$ (the 8-electron $\ce{Na+}$ has low polarizing power) is essentially ionic; in $\ce{LiCl}$ the small 2-electron $\ce{Li+}$ has strong polarizing power and the covalent character is larger; in $\ce{AgI}$ the 18-electron $\ce{Ag+}$ and the easily deformed $\ce{I-}$ polarize each other and the bond is essentially covalent. The effects of ionic polarization on the properties of compounds are:

1. Lower melting and boiling points: the melting points of $\ce{BeCl2}$, $\ce{MgCl2}$ and $\ce{CaCl2}$ are about $400$, $714$ and $775\,{}^\circ\mathrm{C}$ respectively. $\ce{Be^2+}$ has the smallest radius and a 2-electron configuration and the strongest polarizing power, and the bonds in $\ce{BeCl2}$ already have marked covalent character (it exists as molecules in the gas phase and has a chain structure in the solid).
2. Lower solubility: polarization strengthens the covalent character of the bond and lowers the solubility in a polar solvent such as water. $\ce{NaCl}$ and $\ce{KCl}$ are readily soluble, whereas the 18-electron $\ce{AgCl}$ and $\ce{CuCl}$ are sparingly soluble; among the silver halides $\ce{AgF}$ is readily soluble and the solubilities of $\ce{AgCl}$, $\ce{AgBr}$ and $\ce{AgI}$ decrease in turn (their **solubility products** are $1.8\times10^{-10}$, $5.4\times10^{-13}$ and $8.5\times10^{-17}$ in turn, [6.1.10](/6.1.10)). $\ce{Na2S}$ is readily soluble in water while $\ce{ZnS}$ is sparingly soluble, for the same reason.
3. Deeper color: the stronger the polarization, the more easily electrons move between cations and anions and the more the absorbed light shifts to longer wavelengths. $\ce{AgCl}$ is white, $\ce{AgBr}$ pale yellow and $\ce{AgI}$ yellow; the deep colors of $\ce{KMnO4}$ and $\ce{K2Cr2O7}$ come from charge-transfer transitions from O to Mn(VII) and Cr(VI).
4. Change of crystal type: polarization shortens the internuclear distance and lowers the coordination number. The radius ratios $r_+/r_-$ (Shannon radii) of the silver halides are $\ce{AgF}$ 0.86, $\ce{AgCl}$ 0.64, $\ce{AgBr}$ 0.59 and $\ce{AgI}$ 0.52, all of which should be of the NaCl type by the radius ratio; the first three are indeed of the NaCl type, but $\ce{AgI}$ is of the 4-coordinate ZnS type. $\ce{CuCl}$, $\ce{CuBr}$ and $\ce{CuI}$ are all of the ZnS type.
5. Lower thermal stability of oxoacid salts: carbonate decomposition $\ce{MCO3 -> MO + CO2}$ can be viewed as the metal ion "pulling" an $\ce{O^2-}$ from the $\ce{CO3^2-}$. The stronger the polarizing power of the metal ion, the less stable the carbonate and the lower the decomposition temperature:

| Carbonate | $\ce{BeCO3}$ | $\ce{MgCO3}$ | $\ce{CaCO3}$ | $\ce{SrCO3}$ | $\ce{BaCO3}$ | $\ce{ZnCO3}$ | $\ce{PbCO3}$ | $\ce{FeCO3}$ |
|---|---|---|---|---|---|---|---|---|
| Cation configuration | 2 | 8 | 8 | 8 | 8 | 18 | 18+2 | 9–17 |
| Decomposition temperature / °C (approx.) | 100 | 540 | 900 | 1290 | 1360 | 350 | 315 | 282 |

Down a group the ionic radius increases and the polarizing power weakens, so carbonates become more and more stable; the carbonates of transition metals and p-block metals of the 18-, 18+2- and 9–17-electron configurations are much less stable than $\ce{CaCO3}$ of the same charge and similar radius. $\ce{H+}$ has no electrons and a very small radius and the strongest polarizing power, so the stability order is $\ce{H2CO3} < \ce{MHCO3} < \ce{M2CO3}$. The direction of the decomposition reaction and its quantitative dependence on temperature are judged by the Gibbs energy ([6.1.6](/6.1.6)).

## 4.4. Molecular Crystals and Intermolecular Forces

### 4.4.1. Molecular Crystals

A crystal in which molecules are bound by intermolecular forces (and sometimes hydrogen bonds) is a molecular crystal, such as dry ice (solid $\ce{CO2}$), ice, iodine and naphthalene, and the crystals of most organic compounds and of the noble gases. Intermolecular forces are much weaker than chemical bonds, so molecular crystals are generally soft with low melting and boiling points and evaporate or sublime readily; they consist of neutral molecules and do not conduct in the solid or molten state. These properties of molecular crystals, like the liquefaction of gases (the **van der Waals equation**, [5.2.2](/5.2.2)) and the evaporation and boiling of liquids ([6.1.1](/6.1.1)), are determined by intermolecular forces.

### 4.4.2. Permanent, Induced and Instantaneous Dipoles

Intermolecular forces originate in the electric dipole moments of molecules. A molecular dipole has three origins:

- Permanent dipole: the permanent electric dipole moment of a **polar molecule** ([6.1.3](/6.1.3#sec-3.7.2)).

**Definition 4.4.1** The dipole produced when the electron cloud of a molecule is deformed by the electric field of a neighboring molecule, pulling the centers of positive and negative charge apart, is called an **induced dipole**; the dipole produced when, owing to the motion of the electrons and the vibration of the nuclei, the centers of positive and negative charge of a molecule fail to coincide at some instant, is called an **instantaneous dipole**.

The size of an induced dipole is proportional to the field strength and to the **polarizability** of the molecule; the time average of an instantaneous dipole is zero (for a **nonpolar molecule**), but its magnitude is related to the deformability of the molecule: the larger the molecule and the more electrons it has, the greater the polarizability and the larger the instantaneous dipole.

### 4.4.3. van der Waals Forces

**Definition 4.4.2** The interactions between molecules, much weaker than chemical bonds, are collectively called **intermolecular forces**. The part of them arising from electrostatic interactions between the electric dipole moments of molecules is called the **van der Waals force** and comprises three kinds: the attraction produced by the mutual orientation of the permanent dipoles of polar molecules is called the **Keesom force** (orientation force); the attraction between the permanent dipole of a polar molecule and the induced dipole in another molecule is called the **Debye force** (induction force); and the attraction between the instantaneous dipole of a molecule and the dipole it induces in a neighboring molecule is called the **London dispersion force**.

The potential energies of all three are inversely proportional to the sixth power of the intermolecular distance $r$ ($\alpha$ is the polarizability and $I$ the ionization energy):

$$
E_{\mathrm{K}} = -\frac{2}{3k_{\mathrm{B}}T}\,\frac{p_1^2p_2^2}{(4\pi\varepsilon_0)^2r^6},\qquad
E_{\mathrm{D}} = -\frac{p_1^2\alpha_2 + p_2^2\alpha_1}{(4\pi\varepsilon_0)^2r^6},\qquad
E_{\mathrm{L}} = -\frac{3}{2}\,\frac{I_1I_2}{I_1+I_2}\,\frac{\alpha_1\alpha_2}{(4\pi\varepsilon_0)^2r^6}.
$$
The Keesom force is obtained from a thermal average over the dipoles and so is inversely proportional to temperature: raising the temperature, thermal motion destroys the ordered orientation of the dipoles (similar to the **orientation polarization** of dielectrics, [5.3.4](/5.3.4#sec-4.2.2)); the formula for the dispersion force comes from quantum mechanics (London, 1930) and depends only on the polarizabilities and ionization energies. The $r^{-6}$ attractive term of the Lennard-Jones potential is the sum of these three terms ([5.2.2](/5.2.2#sec-2.2.1)).

- The Keesom force exists only between polar molecules and is proportional to the square of the dipole moments;
- The Debye force exists between polar and nonpolar molecules and also between polar molecules;
- The dispersion force exists between all molecules and is proportional to the polarizabilities of the molecules.

Estimates of the intermolecular interaction energies of several molecules (data from common textbooks, in $\mathrm{kJ\,mol^{-1}}$):

| Molecule | Keesom | Debye | Dispersion | Total |
|---|---|---|---|---|
| Ar | 0 | 0 | 8.5 | 8.5 |
| CO | 0.003 | 0.008 | 8.75 | 8.75 |
| HI | 0.025 | 0.113 | 25.87 | 26.00 |
| HBr | 0.69 | 0.50 | 21.94 | 23.11 |
| HCl | 3.31 | 1.00 | 16.83 | 21.14 |
| $\ce{NH3}$ | 13.31 | 1.55 | 14.95 | 29.60 |
| $\ce{H2O}$ | 36.39 | 1.93 | 9.00 | 47.31 |

Characteristics of van der Waals forces:

1. They exist universally between molecules (and between noble-gas atoms) and are attractive;
2. The interaction energies are a few to a few tens of $\mathrm{kJ\,mol^{-1}}$, one to two orders of magnitude smaller than chemical bonds (about $100$–$800\,\mathrm{kJ\,mol^{-1}}$);
3. They are neither directional nor saturable;
4. They are short-range forces: the interaction energy decays rapidly as $r^{-6}$, acting mainly at distances at which molecules are in contact (about $0.3$–$0.5\,\mathrm{nm}$) and negligible beyond about $1\,\mathrm{nm}$;
5. Except for a few strongly polar molecules ($\ce{H2O}$, $\ce{NH3}$, $\ce{HF}$), the dispersion force dominates among the three.

Among similar molecules, the larger the relative molecular mass, the greater the polarizability, the stronger the dispersion force and the higher the melting and boiling points: the boiling points of HCl, HBr and HI rise in turn although their dipole moments decrease in turn; $\ce{F2}$ and $\ce{Cl2}$ are gases, $\ce{Br2}$ is a liquid and $\ce{I2}$ is a solid. The dispersion force also depends on molecular shape: for the same relative molecular mass, the closer to spherical the molecule, the smaller the contact area between molecules and the weaker the dispersion force. The boiling points of n-pentane, isopentane (2-methylbutane) and neopentane (2,2-dimethylpropane) (structures 1, 2, 3 below) are $36.1$, $27.8$ and $9.5\,{}^\circ\mathrm{C}$ in turn:

```smiles
CCCCC 1
CCC(C)C 2
CC(C)(C)C 3
```

![Normal boiling points. Left: hydrides of groups 14–17; NH₃, H₂O and HF stand out because of hydrogen bonding. Right: n-alkanes by chain length, with the three pentane isomers](./plots/boiling-points.py)

### 4.4.4. The Hydrogen Bond

The boiling points of $\ce{H2O}$, $\ce{HF}$ and $\ce{NH3}$ are much higher than the trend of the other hydrides in the same group (figure above, left): extrapolating from $\ce{H2Te}$, $\ce{H2Se}$ and $\ce{H2S}$, the boiling point of $\ce{H2O}$ should be about $-80\,{}^\circ\mathrm{C}$, whereas it is actually $100\,{}^\circ\mathrm{C}$. This shows that besides van der Waals forces there is a stronger interaction between these molecules. The electronegativity of O (3.44) is much larger than that of H (2.20) and its radius is small, so the shared pair of the O–H bond is strongly displaced toward O, H becomes almost a bare proton, and it can be attracted by a highly electronegative atom with lone pairs in another molecule.

**Definition 4.4.3 (Hydrogen Bond)** The attractive interaction between a hydrogen atom in a molecule or molecular fragment X–H (X more electronegative than H, commonly F, O or N) and an atom or group Y (with a lone pair or pi electrons) in the same or another molecule, when there is evidence of bond formation, is called a **hydrogen bond**, written X–H⋯Y.

This is the IUPAC definition of 2011. X and Y may be the same or different, and are mainly F, O and N; weaker hydrogen bonds can also have C–H as the donor and Cl, S or pi systems as the acceptor. The energy of a hydrogen bond is the energy needed to separate X–H⋯Y into X–H and Y, and its length is the distance between the nuclei of X and Y. By strength they are roughly divided into three classes:

| Class | Bond energy / (kJ mol⁻¹) | X⋯Y distance / pm | X–H⋯Y angle | Examples |
|---|---|---|---|---|
| Strong | 60–170 | 220–250 | Close to $180^\circ$ | $\ce{[F-H-F]-}$ (about 160) |
| Moderate | 15–60 | 250–320 | Greater than $130^\circ$ | Most hydrogen bonds in water, alcohols, carboxylic acids, proteins and DNA (O⋯O 276 pm in ice, about 20–25) |
| Weak | Less than 15 | 320–400 | Greater than $90^\circ$ | C–H⋯O, O–H⋯π |

Properties of hydrogen bonds:

1. Strength: the greater the electronegativity and the smaller the radius of X and Y, the stronger the hydrogen bond: F–H⋯F > O–H⋯O > N–H⋯N. Although the electronegativity of Cl is close to that of N, its radius is large and it forms very weak hydrogen bonds.
2. Directionality: X–H⋯Y is as nearly linear as possible, which puts Y as far from X as possible and minimizes repulsion, while the lone pair of Y points toward H.
3. Saturability: an X–H can generally form a hydrogen bond with only one Y; H is very small, and once a hydrogen bond has formed, another highly electronegative atom approaching is repelled by X and Y.
4. Nature: the hydrogen bond is predominantly electrostatic but not only electrostatic; it also includes partial charge transfer from the lone pair of Y into the antibonding orbital of X–H (partial covalent character) and contributions from polarization and dispersion. Early textbooks held that the hydrogen bond is "mainly an electrostatic force", which cannot explain its directionality and saturability; charge transfer requires orbital overlap along a particular direction, which accounts for both. Experimentally, Compton scattering in ice and spin–spin coupling across hydrogen bonds in NMR both confirm this covalent contribution. The hydrogen bond therefore lies between the van der Waals force and the covalent bond and can be regarded as a strong intermolecular interaction with directionality and saturability.

Hydrogen bonds are divided into intermolecular and intramolecular ones:

- Intermolecular hydrogen bonds link molecules together and markedly raise the melting point, boiling point and enthalpy of vaporization of a compound (the anomalies of $\ce{H2O}$, $\ce{HF}$ and $\ce{NH3}$). $\ce{HF}$ is also associated as $(\ce{HF})_n$ in the gas phase; ethanol (boiling point $78\,{}^\circ\mathrm{C}$) boils much higher than dimethyl ether of similar relative molecular mass ($-24\,{}^\circ\mathrm{C}$); hydrogen bonds between solute and solvent make ethanol and ammonia very soluble in water.
- Intramolecular hydrogen bonds form rings within one molecule and reduce association between molecules, generally lowering the melting and boiling points. In o-nitrophenol (structure 1 below, melting point $45\,{}^\circ\mathrm{C}$) the O–H forms an intramolecular hydrogen bond with the adjacent nitro group, whereas p-nitrophenol (structure 2 below, melting point $114\,{}^\circ\mathrm{C}$) can form only intermolecular hydrogen bonds; the ortho isomer is more volatile and can be separated from the para isomer by steam distillation.

```smiles
Oc1ccccc1[N+](=O)[O-] 1
Oc1ccc(cc1)[N+](=O)[O-] 2
```

In ice each water molecule forms tetrahedrally oriented hydrogen bonds with four neighboring water molecules, using its two H atoms and two lone pairs, giving an open structure, so ice is less dense than water; when ice melts some hydrogen bonds break and the molecules pack more closely, and water has its maximum density at about $4\,{}^\circ\mathrm{C}$. The structures of biological macromolecules (the α-helix and β-sheet of proteins and the base pairing in the DNA double helix) are also maintained by hydrogen bonds ([7.1](/7.1)).

## 4.5. Covalent Network Crystals and Other Crystals

### 4.5.1. Covalent Network Crystals

In diamond, elemental silicon and boron, $\ce{SiO2}$, SiC, cubic BN and the like, covalent bonds join all the atoms into a three-dimensional network; there are no discrete small molecules in the crystal, and the whole crystal can be regarded as one giant molecule. In diamond each C is $\mathrm{sp}^3$ hybridized and forms tetrahedrally oriented covalent bonds with 4 C atoms (coordination number 4, C–C bond length $154\,\mathrm{pm}$); Si and Ge have the same structure as diamond; in quartz each Si and 4 O form a tetrahedron and each O links two Si.

Covalent network crystals have high melting points and great hardness (diamond is the hardest natural substance), are nonvolatile and insoluble in common solvents, and are generally electrical insulators and poor conductors of heat (diamond is in fact an excellent thermal conductor, conducting heat by lattice vibrations); Si, Ge and SiC are semiconductors.

### 4.5.2. Layered and Mixed-Type Crystals

Graphite is a layered crystal: within each layer each C is $\mathrm{sp}^2$ hybridized and forms sigma bonds with 3 C atoms, giving a planar network of six-membered rings (C–C bond length $142\,\mathrm{pm}$); each C has one remaining 2p electron perpendicular to the layer plane, forming a **delocalized pi bond** extending over the whole layer. The layers are $335\,\mathrm{pm}$ apart and held together only by van der Waals forces. Graphite thus has features of both a covalent network crystal (within the layers) and a molecular crystal (between the layers): the bonding within layers is strong and the melting point very high, while the layers slide easily over one another, so graphite can be used as a lubricant and in pencil leads; the delocalized pi electrons make it conduct along the layer plane, so it can be used for electrodes. A single layer of graphite is graphene. Mica, $\ce{MoS2}$ and hexagonal BN are also layered crystals.

### 4.5.3. Crystal Defects

All the crystals discussed so far are ideal crystals. Real crystals are of finite size, the particles vibrate about their equilibrium positions, and there are various departures from the ideal structure in the crystal.

**Definition 4.5.1 (Crystal Defect)** All deviations from the ideal lattice structure in a real crystal are collectively called **crystal defects**.

By geometry, defects are divided into point defects (vacancies, interstitial atoms, impurity atoms), line defects (dislocations) and planar defects (grain boundaries, stacking faults); by origin, point defects are divided into intrinsic defects and impurity defects.

Intrinsic defects are formed when particles of the crystal itself leave their normal positions and do not change the chemical composition. Two kinds are common in ionic crystals:

- *Schottky defect*: paired vacancies of cations and anions (preserving electroneutrality), as in NaCl and KCl;
- *Frenkel defect*: a cation leaves its normal position and enters an interstitial site, leaving a vacancy and forming a "vacancy–interstitial ion" pair, common in crystals with small, easily deformed cations, such as AgCl and AgBr.

All solids have a thermodynamic tendency to produce intrinsic defects: forming defects costs energy (the enthalpy increases) but increases the disorder (entropy) of the crystal, so at equilibrium there is always a certain concentration of defects, whose number increases with temperature roughly as the **Boltzmann factor** $\mathrm{e}^{-\Delta H/(2RT)}$ ($\Delta H$ is the molar enthalpy of forming a pair of defects, [6.1.6](/6.1.6)). Conduction and diffusion in ionic crystals take place by migration of ions along vacancies or interstitial sites and so are closely tied to the defect concentration.

Impurity defects are formed when foreign atoms replace normal atoms or enter interstitial sites. Doping semiconducting silicon with a little P (5 valence electrons) supplies extra electrons as charge carriers and gives an **n-type semiconductor**; doping with a little B (3 valence electrons) creates holes and gives a **p-type semiconductor** ([5.5.6](/5.5.6#sec-6.4.2)). Defects can also make the chemical composition deviate from integer ratios: for example the composition of iron(II) oxide is actually $\ce{Fe_{1-x}O}$ ($x$ about $0.05$–$0.15$), with some $\ce{Fe^2+}$ sites vacant and the charge compensated by $\ce{Fe^3+}$.

Defects are often decisive for the properties of materials: dislocations make the real strength of metals several orders of magnitude lower than that of ideal crystals and at the same time allow metals to deform plastically; the conductivity of semiconductors is controlled by doping; the colors of gemstones often come from trace impurity ions (ruby is $\ce{Al2O3}$ doped with $\ce{Cr^3+}$).

## Summary

| Crystal type | Structural units and forces | Typical structures | Properties |
|---|---|---|---|
| Metallic crystal | Metal ions, free electrons; metallic bond | ccp, hcp (coordination number 12), bcc (8) | Electrical and thermal conductivity, ductility, luster |
| Ionic crystal | Cations and anions; ionic bond | NaCl, CsCl, ZnS, $\ce{CaF2}$, rutile, perovskite types | Fairly high melting point, hard and brittle, conducts when molten |
| Molecular crystal | Molecules; van der Waals forces, hydrogen bonds | Varied | Low melting point, soft, insulating |
| Covalent network crystal | Atoms; covalent bonds | Diamond type, quartz | Very high melting point, very hard |

- The packing efficiency of close packing is $74.0\%$, and $N$ spheres have $N$ octahedral holes and $2N$ tetrahedral holes; that of bcc is $68.0\%$.
- The lattice enthalpy $\Delta_{\mathrm{latt}}H^\circ$ is roughly proportional to $z_+z_-/(r_+ + r_-)$; the coordination number is divided at the radius ratios $0.225$, $0.414$ and $0.732$, and ionic polarization moves the bond type toward covalent and lowers the coordination number.
- van der Waals forces all decay as $r^{-6}$, with the dispersion force dominant; the hydrogen bond is stronger than the van der Waals force, directional and saturable, mainly electrostatic with some covalent character.

## Questions

1. Why are metals ductile and malleable while ionic crystals are brittle?

   **Answer** When layers of metal slide, the electron sea still holds the ions together; after a layer of an ionic crystal is displaced, ions of like charge face each other and the repulsion fractures the crystal.

2. $\ce{SiO2}$ and $\ce{CO2}$ have similar compositions; why is one a high-melting solid and the other a gas?

   **Answer** The Si atom is large and Si–O pi bonding is very weak, so Si tends to form four Si–O single bonds and joins into a covalent network; C and O form stable C=O double bonds, and $\ce{CO2}$ consists of discrete nonpolar molecules with only dispersion forces between them.

3. Why is the boiling point of $\ce{HF}$ higher than that of $\ce{HCl}$, whereas that of $\ce{HCl}$ is lower than that of $\ce{HBr}$?

   **Answer** There are strong hydrogen bonds between $\ce{HF}$ molecules; between $\ce{HCl}$ and $\ce{HBr}$ molecules dispersion forces dominate, and $\ce{HBr}$ has the larger polarizability.

4. The melting point of $\ce{FeCl3}$ ($307\,{}^\circ\mathrm{C}$) is lower than that of $\ce{FeCl2}$ ($677\,{}^\circ\mathrm{C}$); why?

   **Answer** $\ce{Fe^3+}$ has a higher charge and smaller radius and a stronger polarizing power than $\ce{Fe^2+}$, the bonds in $\ce{FeCl3}$ are more covalent, and in the gas phase it exists as $\ce{Fe2Cl6}$ molecules.
