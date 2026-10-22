---
title: Chemical Bonding and Molecular Structure
source_hash: 2c5ed20a89dd
---

What holds atoms together in molecules and crystals, and what shape the resulting molecules have, are among the central questions of chemistry. The strong interactions between adjacent atoms (or ions) in a molecule or crystal are called *chemical bonds*, with bond energies generally in the range $100$–$800\,\mathrm{kJ\,mol^{-1}}$; the van der Waals forces and hydrogen bonds between molecules are weaker by one to two orders of magnitude and are left to the next chapter. This chapter presents several theories of chemical bonding in historical and logical order: the ionic bond theory (Kossel); the classical valence bond theory centered on the shared electron pair (Lewis); the modern valence bond theory that explains the shared pair by quantum mechanics (Heitler–London, Pauling) and its extension, hybrid orbital theory; valence shell electron pair repulsion theory, which predicts molecular geometry from electron-pair repulsion alone; and molecular orbital theory, which regards electrons as belonging to the whole molecule. Finally we discuss bond polarity and molecular polarity.

All these theories rest on the atomic structure of the previous chapter ([6.1.2](/6.1.2)): the shapes and directions of **atomic orbitals** determine the directional character of covalent bonds, and the **electron configuration** and **electronegativity** determine whether an atom tends to gain or lose electrons or to share them. The basic concepts of quantum mechanics (the **wave function**, the **Pauli exclusion principle** and **Hund's rule**) are in [5.5.3](/5.5.3) and [5.5.4](/5.5.4); combining two atomic orbitals into a bonding and an antibonding orbital is mathematically the eigenvalue problem of a $2\times 2$ real symmetric matrix ([2.1.7](/2.1.7)), the same calculation as the tight-binding model of energy bands in solids ([5.5.6](/5.5.6#sec-6.2.3)). This chapter goes only as deep as is needed for applications: the rigorous treatments, such as quantitative molecular orbital calculations, point groups and symmetry, and the Hückel method, belong to [structural chemistry](/6.2), and hybridization, resonance and inductive effects in organic molecules belong to [organic chemistry](/6.5).

## 3.1. The Ionic Bond

### 3.1.1. Formation and Characteristics of the Ionic Bond

In 1916 Kossel noticed that the outermost shell of a noble-gas atom has the eight-electron structure $n\mathrm{s}^2 n\mathrm{p}^6$ ($1\mathrm{s}^2$ for He) and that the noble gases are chemically very inert; he proposed that other atoms reach this structure by gaining or losing electrons, forming positive and negative ions that then combine through electrostatic attraction. For example,

$$
\ce{Na (3s^1) + Cl (3s^2 3p^5) -> Na+ (2s^2 2p^6) + Cl- (3s^2 3p^6)}.
$$
This electron transfer occurs readily between reactive metals with low **ionization energy** and reactive nonmetals with large **electron affinity** ([6.1.2](/6.1.2)).

**Definition 3.1.1 (Ionic Bond)** The chemical bond formed between positive and negative ions by electrostatic interaction is called the **ionic bond**.

The essence of the ionic bond is the electrostatic interaction described by **Coulomb's law**, so it has two characteristics:

- It is nondirectional: the charge distribution of an ion is approximately spherically symmetric, so it can attract ions of opposite charge in any direction.
- It is nonsaturable: as long as space allows, an ion can attract as many oppositely charged ions as possible around it. In a $\ce{NaCl}$ crystal each $\ce{Na+}$ is surrounded by 6 $\ce{Cl-}$ and each $\ce{Cl-}$ by 6 $\ce{Na+}$; the whole crystal is one giant aggregate of ions in which no separate "$\ce{NaCl}$ molecule" can be identified, and the formula gives only the ratio of the numbers of ions.

The strength of the ionic bond and the properties of ionic crystals depend on three characteristics of the ions: charge, electron configuration and radius.

### 3.1.2. Characteristics of Ions

Consider first the charge of the ion. Ions of the same element with different charges can have entirely different properties: $\ce{Fe^3+}$ is oxidizing and $\ce{Fe^2+}$ is reducing; $\ce{Fe^3+}$ forms a blood-red complex with $\ce{SCN-}$ while $\ce{Fe^2+}$ gives no color; their aqueous solutions are yellow-brown and pale green respectively.

Next is the electron configuration of the ion. Simple anions generally have the 8-electron noble-gas configuration ($\ce{F-}$ and $\ce{O^2-}$: $2\mathrm{s}^2 2\mathrm{p}^6$; $\ce{Cl-}$: $3\mathrm{s}^2 3\mathrm{p}^6$). Cations are divided into five classes by the number of electrons in the outermost shell:

| Configuration | Outermost electrons | Examples |
|---|---|---|
| 2 electrons | $1\mathrm{s}^2$ | $\ce{Li+}$, $\ce{Be^2+}$ |
| 8 electrons | $n\mathrm{s}^2 n\mathrm{p}^6$ | $\ce{Na+}$, $\ce{Mg^2+}$, $\ce{Al^3+}$, $\ce{Ca^2+}$ |
| 18 electrons | $n\mathrm{s}^2 n\mathrm{p}^6 n\mathrm{d}^{10}$ | $\ce{Zn^2+}$ ($3\mathrm{s}^2 3\mathrm{p}^6 3\mathrm{d}^{10}$), $\ce{Ag+}$, $\ce{Cu+}$, $\ce{Hg^2+}$ |
| 18+2 electrons | 18 in the penultimate shell, $(n+1)\mathrm{s}^2$ in the outermost | $\ce{Pb^2+}$ ($[\ce{Xe}]4\mathrm{f}^{14}5\mathrm{d}^{10}6\mathrm{s}^2$), $\ce{Sn^2+}$, $\ce{Bi^3+}$ |
| 9–17 electrons | $n\mathrm{s}^2 n\mathrm{p}^6 n\mathrm{d}^{1\text{–}9}$ | $\ce{Fe^2+}$ ($3\mathrm{s}^2 3\mathrm{p}^6 3\mathrm{d}^6$, 14 electrons), $\ce{Fe^3+}$ (13), $\ce{Cu^2+}$ (17) |

Transition metals lose their $4\mathrm{s}$ electrons first ($\ce{Fe}$: $[\ce{Ar}]3\mathrm{d}^6 4\mathrm{s}^2$, $\ce{Fe^2+}$: $[\ce{Ar}]3\mathrm{d}^6$), for reasons given in [6.1.2](/6.1.2). Through ionic polarization the electron configuration affects the properties of compounds ([6.1.4](/6.1.4)).

Finally, the radius of the ion. The electron cloud of an ion has no definite boundary, and the size of an ion can only be specified from internuclear distances in crystals.

**Definition 3.1.2 (Ionic Radius)** The internuclear distance $d$ between adjacent cations and anions in an ionic crystal is regarded as the sum of the two ionic radii, $d = r_+ + r_-$; the radii obtained by apportioning the internuclear distance between the ions according to a convention (for example taking $r(\ce{O^2-}) = 140\,\mathrm{pm}$) are called **ionic radii**.

The internuclear distance can be determined accurately by X-ray diffraction, but the way it is apportioned is a convention. The commonly used sets are the Pauling radii and the Shannon effective ionic radii (1976), the latter giving separate values for different coordination numbers. In this course Shannon radii (six-coordinate) are used throughout. The trends are as follows:

1. For ions of the same group and charge, the radius increases down the group: $\ce{F-}$ $133$ < $\ce{Cl-}$ $181$ < $\ce{Br-}$ $196$ < $\ce{I-}$ $220\,\mathrm{pm}$.
2. For cations of the same period with the same electron configuration, the higher the charge the smaller the radius: $\ce{Na+}$ $102$ > $\ce{Mg^2+}$ $72$ > $\ce{Al^3+}$ $54\,\mathrm{pm}$ (the nuclear charge increases, and so does the **effective nuclear charge**).
3. For one element, the higher the charge of the cation the smaller the radius: $r(\ce{Fe}) > r(\ce{Fe^2+}) = 78\,\mathrm{pm} > r(\ce{Fe^3+}) = 65\,\mathrm{pm}$ (high spin); an anion is larger than the corresponding atom.
4. Anion radii are generally large (about $130$–$220\,\mathrm{pm}$) and cation radii small (about $10$–$170\,\mathrm{pm}$).

The radius affects the properties of ionic compounds. The smaller the internuclear distance, the greater the electrostatic attraction between the ions and the higher the melting point of the ionic crystal: $\ce{NaF}$ $996$, $\ce{NaCl}$ $801$, $\ce{NaBr}$ $747$, $\ce{NaI}$ $661\,{}^\circ\mathrm{C}$. The larger the anion, the farther the outermost electrons from the nucleus and the more easily they are lost, and the stronger the reducing power: $\ce{I-} > \ce{Br-} > \ce{Cl-}$.

## 3.2. Classical Valence Bond Theory

### 3.2.1. The Covalent Bond and Lewis Structures

The ionic bond theory cannot explain molecules composed of identical atoms such as $\ce{H2}$, $\ce{O2}$ and $\ce{N2}$, nor how atoms of similar electronegativity combine ($\ce{CH4}$, $\ce{CO2}$). In 1916 Lewis proposed that atoms can share electron pairs so that every atom attains a noble-gas electron configuration.

**Definition 3.2.1 (Covalent Bond)** The chemical bond formed between atoms by sharing an electron pair is called the **covalent bond**. Sharing one, two or three pairs gives a single, double or triple bond respectively.

**Definition 3.2.2 (Lewis Structure)** The tendency of atoms in a molecule to share electron pairs so that the outermost shell holds 8 electrons (2 for H) is an empirical rule called the **octet rule**. A formula that represents molecular structure by showing shared pairs as lines and unshared valence electrons as dots is called a **Lewis structure**; an electron pair that belongs to a single atom and takes no part in bonding is called a **lone pair**, and a species with a single unpaired electron is a free radical.

Examples are $\ce{H-H}$, $\ce{H-Cl}$, $\ce{O=C=O}$ and $\ce{N#N}$; in $\ce{NH3}$ N has one lone pair and in $\ce{H2O}$ O has two. The general steps for drawing a Lewis structure are:

1. Count all the valence electrons (add the charge for an anion, subtract it for a cation);
2. Write the skeleton, with the less electronegative atom generally the central atom (H is always terminal);
3. Draw a single bond for each connection, then distribute the remaining electrons as lone pairs, first on the terminal atoms and then on the central atom;
4. If the central atom has fewer than 8 electrons, convert lone pairs of terminal atoms into double or triple bonds.

![Lewis structures with lone pairs and formal charges. Top: H₂O, NH₃, NH₄⁺ and CH₄; bottom: N₂, CO₂, CO, O₃ and the nitrate ion (one resonance form each)](./plots/lewis-structures.py)

### 3.2.2. Formal Charge

Several Lewis structures that all satisfy the octet rule can often be written for the same molecule. Formal charge is a commonly used criterion for choosing the reasonable ones.

**Definition 3.2.3 (Formal Charge)** In a Lewis structure, assuming that each shared electron pair is divided equally between the two atoms, the **formal charge** of an atom is

$$
\text{formal charge} = V - L - \tfrac{1}{2}B,
$$
where $V$ is the number of valence electrons of the (free) atom, $L$ is the number of electrons in its lone pairs and $B$ is the number of shared electrons it takes part in.

The formal charges of all the atoms in a structure add up to the charge of the molecule or ion. A more reasonable structure satisfies: (1) the absolute values of the formal charges are as small as possible; (2) when formal charges cannot be avoided, negative formal charge is on the more electronegative atom; (3) adjacent atoms do not carry formal charges of the same sign.

**Example 3.2.1** In the structure $\ce{C#O}$ of $\ce{CO}$, C has $4 - 2 - 3 = -1$ and O has $6 - 2 - 3 = +1$. This is contrary to the intuition from electronegativity, but it is the only structure in which both atoms satisfy the octet rule; the measured **electric dipole moment** of $\ce{CO}$ is very small ($0.11\,\mathrm{D}$) with the negative end on the C side, in the direction of the formal charges (the cause must be explained by molecular orbital theory, Section 3.6.5). $\ce{O3}$ is written $\ce{O=O+-O-}$: the central O is $+1$ and the singly bonded terminal O is $-1$; the double bond can equally be drawn on the other side, the two structures being equivalent, and in real $\ce{O3}$ the two O–O bonds are exactly the same (bond length $127.8\,\mathrm{pm}$, between a single and a double bond), which is described by a delocalized pi bond (Section 3.4.4).

**Example 3.2.2** If the sulfate ion $\ce{SO4^2-}$ is written with four S–O single bonds, S has formal charge $+2$ and each O has $-1$; if it is written with two S=O double bonds, S has 0 and the formal charges are smaller, but S then has 12 electrons around it. Chinese textbooks often adopt the latter. Modern quantum-chemical calculations show that the 3d orbitals of S take almost no part in bonding and that the S–O bonds are strongly polar; the former structure (together with partial back-donation of electrons from O to S) is closer to reality, and the formal charge rule should be used with caution for structures that exceed the octet (Section 3.4.5).

### 3.2.3. Shortcomings of Classical Valence Bond Theory

1. The octet rule has exceptions: B in $\ce{BF3}$ has only 6 electrons around it, P in $\ce{PCl5}$ has 10 and S in $\ce{SF6}$ has 12, and these molecules are all stable; $\ce{NO}$ and $\ce{NO2}$ contain an odd number of electrons, so not every atom can satisfy the octet rule.
2. It cannot explain the directional character and saturability of covalent bonds, nor predict the spatial structure of molecules.
3. It cannot explain the nature of the covalent bond: by classical electrostatics two negatively charged electrons should repel each other, so why does pairing them stabilize the system?

The third question must be answered by quantum mechanics.

## 3.3. Modern Valence Bond Theory

### 3.3.1. The Hydrogen Molecule and the Nature of the Covalent Bond

In 1927 Heitler and London treated the formation of $\ce{H2}$ from two hydrogen atoms by quantum mechanics and obtained the variation of the energy $E$ of the system with internuclear distance $r$ (figure below).

- When the two electrons have opposite spins, the energy of the system first decreases as $r$ decreases, reaches a minimum at $r_{\mathrm{e}} = 74\,\mathrm{pm}$ and then rises rapidly on closer approach because of internuclear repulsion. The energy minimum is the stable ground state of $\ce{H2}$, with well depth $D_{\mathrm{e}} = 458\,\mathrm{kJ\,mol^{-1}}$; after subtracting the zero-point vibrational energy the measured dissociation energy is $D_0 = 432\,\mathrm{kJ\,mol^{-1}}$ (the bond energy at $298.15\,\mathrm{K}$ is $436\,\mathrm{kJ\,mol^{-1}}$, Section 3.3.5).
- When the two electrons have the same spin, the **Pauli exclusion principle** prevents them from being in the internuclear region at the same time, and the energy rises monotonically as $r$ decreases, so no bond forms (a repulsive state).

The simple Heitler–London calculation gives $r_{\mathrm{e}} \approx 87\,\mathrm{pm}$ and $D_{\mathrm{e}} \approx 303\,\mathrm{kJ\,mol^{-1}}$, which is quantitatively inaccurate but was the first derivation from first principles that two hydrogen atoms can combine; more accurate variational calculations can agree fully with experiment, and these belong to [structural chemistry](/6.2).

![Potential energy curves of H₂: the bound ground state with antiparallel spins (experiment and the Heitler–London estimate) and the repulsive state with parallel spins](./plots/h2-potential-curves.py)

This is exactly the picture of the **potential energy curve** in [5.1.4](/5.1.4): the minimum of the curve is the stable equilibrium position, near which the molecule vibrates ([5.5.5](/5.5.5#sec-5.3.3)). The calculation also shows that the electron probability density between the two nuclei increases markedly in the ground state and decreases in the repulsive state: when two 1s orbitals are superposed with the same sign, the wave functions add between the nuclei and the probability of finding the electrons there increases, at the same time attracting both nuclei and "gluing" them together.

This gives the nature of the covalent bond: when atoms approach, their atomic orbitals overlap (the wave functions superpose), the two atoms share a pair of electrons of opposite spin, and the dense electron cloud between the nuclei lowers the energy of the system and creates the bond. The covalent bond is still electrical in nature, but the two conditions "opposite spins" and "orbital overlap" come from quantum mechanics and cannot be derived from classical theory.

### 3.3.2. Main Points of Valence Bond Theory

Extending the Heitler–London result to other molecules gives *valence bond theory*, also called the electron-pair theory, developed mainly by Pauling and Slater around 1930. Its basic points are:

1. When two atoms approach, the atomic orbitals containing unpaired electrons of opposite spin overlap and form a covalent bond;
2. The more the atomic orbitals overlap, the greater the electron probability density between the nuclei and the more stable the bond.

**Definition 3.3.1 (Principle of Maximum Overlap)** Bonding atomic orbitals always overlap along the direction in which the overlap is greatest; this rule is called the **principle of maximum overlap**.

This gives two characteristics of the covalent bond:

- Saturability: the number of covalent bonds an atom can form depends on its number of unpaired electrons (and available orbitals), each unpaired electron being able to pair with only one electron of opposite spin. H has only one 1s electron, so it can form only $\ce{H2}$ and there is no $\ce{H3}$; N has three unpaired 2p electrons and forms $\ce{NH3}$.
- Directional character: apart from s orbitals, atomic orbitals have definite orientations in space, and by the principle of maximum overlap bonds must form along particular directions. For example in $\ce{H2S}$ the two unpaired electrons of S are in the mutually perpendicular $3\mathrm{p}_x$ and $3\mathrm{p}_y$ orbitals, the 1s orbitals of H overlap with them along the $x$ and $y$ axes respectively, and the bond angle should be close to $90^\circ$ (measured $92.1^\circ$); in $\ce{HCl}$ the 1s orbital of H overlaps along the symmetry axis of the $3\mathrm{p}$ orbital of Cl.

The strength of a covalent bond depends on the degree of orbital overlap and the number of shared electron pairs: generally triple > double > single.

### 3.3.3. Sigma, Pi and Delta Bonds

Take the line joining the two nuclei (the bond axis) as the $z$ axis; by the symmetry of the overlap region of the atomic orbitals about the bond axis, covalent bonds fall into three kinds.

**Definition 3.3.2** A covalent bond in which two atomic orbitals overlap "head-on" along the bond axis, with the overlap region cylindrically symmetric about the bond axis (unchanged by rotation through any angle about it), is called a **sigma bond**, as in s–s, s–$\mathrm{p}_z$ and $\mathrm{p}_z$–$\mathrm{p}_z$ overlap. A covalent bond in which two atomic orbitals overlap "side by side", with the overlap region antisymmetric with respect to a plane through the bond axis (a nodal plane, on which the electron density is zero), is called a **pi bond**, as in $\mathrm{p}_x$–$\mathrm{p}_x$ and $\mathrm{p}_y$–$\mathrm{p}_y$ overlap. A covalent bond in which two d orbitals overlap "face to face" (such as $\mathrm{d}_{xy}$–$\mathrm{d}_{xy}$), with the overlap region having two nodal planes through the bond axis, is called a **delta bond**.

- If there is only one covalent bond between two atoms it must be a sigma bond; a double bond consists of one sigma and one pi bond and a triple bond of one sigma and two pi bonds. For example in $\ce{N2}$ (each N, $1\mathrm{s}^2 2\mathrm{s}^2 2\mathrm{p}^3$, has three unpaired 2p electrons), $2\mathrm{p}_z$–$2\mathrm{p}_z$ forms the sigma bond and $2\mathrm{p}_x$–$2\mathrm{p}_x$ and $2\mathrm{p}_y$–$2\mathrm{p}_y$ form two mutually perpendicular pi bonds.
- The overlap of a pi bond is generally smaller than that of a sigma bond and its bond energy is smaller; the pi electrons are farther from the nucleus and less tightly bound, so molecules containing pi bonds (such as alkenes) are chemically more reactive. A pi bond does not allow free rotation about the bond axis, which is the origin of cis–trans isomerism.
- Delta bonds occur only between transition-metal atoms, as in the Re–Re quadruple bond ($\sigma^2\pi^4\delta^2$) of $\ce{[Re2Cl8]^2-}$.

### 3.3.4. The Coordinate Bond

**Definition 3.3.3 (Coordinate Bond)** A covalent bond in which the shared electron pair is supplied entirely by one of the bonded atoms is called a **coordinate bond**, often denoted by an arrow from the donor to the acceptor, $\ce{A -> B}$. The conditions for forming one are that one partner has a lone pair and the other has an empty orbital that can accept an electron pair.

For example in $\ce{NH3 + H+ -> NH4+}$ the lone pair of N forms a coordinate bond with the empty 1s orbital of $\ce{H+}$; once formed, a coordinate bond is no different from other covalent bonds, and the four N–H bonds of $\ce{NH4+}$ are completely equivalent. In $\ce{CO}$, besides two normal covalent bonds (one sigma, one pi) there is a coordinate pi bond formed by a lone pair of O entering an empty 2p orbital of C, so $\ce{CO}$ has a triple bond, which is also the origin of the formal charges in Example 3.2.1. $\ce{BF3 + NH3 -> F3B<-NH3}$ is a typical Lewis acid–base reaction ([6.1.9](/6.1.9)); the coordinate bonds between metal ions and ligands are the basis of coordination compounds ([6.1.5](/6.1.5)).

### 3.3.5. Bond Parameters

The physical quantities that characterize covalent bonds are called bond parameters.

**Definition 3.3.4** The equilibrium distance between the nuclei of two bonded atoms in a molecule is called the **bond length**; the angle between two bonds formed by the same atom in a molecule is called the **bond angle**; the energy required at $298.15\,\mathrm{K}$ and the standard pressure to break the A–B bond of $1\,\mathrm{mol}$ of gaseous molecules AB, forming gaseous atoms A and B, is called the **bond energy** (dissociation energy) of the A–B bond. For polyatomic molecules the energies needed to break the bonds of one kind (such as the four C–H bonds of $\ce{CH4}$) one after another are not the same, and their mean is taken as the bond energy.

Bond lengths and bond angles determine the geometry of the molecule and can be measured by molecular spectroscopy ([5.5.5](/5.5.5)), X-ray diffraction or electron diffraction; the bond energy determines the strength of the bond. The thermochemical definitions of bond energy (standard molar bond enthalpy and mean bond enthalpy) and the estimation of reaction enthalpies from bond enthalpies are in [6.1.6](/6.1.6). Some typical mean values:

| Bond | Bond length / pm | Bond energy / (kJ mol⁻¹) | Bond | Bond length / pm | Bond energy / (kJ mol⁻¹) |
|---|---|---|---|---|---|
| H–H | 74 | 436 | C–H | 109 | 413 |
| C–C | 154 | 346 | C–O | 143 | 358 |
| C=C | 134 | 610 | C=O | 120 | 745 |
| C≡C | 120 | 835 | O=O | 121 | 498 |
| N≡N | 110 | 945 | F–F | 141 | 159 |

Between the same pair of atoms, the higher the bond order, the shorter the bond and the greater the bond energy; but the energy of a double bond is less than twice that of a single bond, showing that a pi bond is weaker than a sigma bond. Examples of bond angles: $\ce{CH4}$ $109.5^\circ$, $\ce{NH3}$ $106.7^\circ$, $\ce{H2O}$ $104.5^\circ$, $\ce{CO2}$ $180^\circ$.

## 3.4. Hybrid Orbital Theory

### 3.4.1. The Concept of Hybridization

Valence bond theory explains the directional character of covalent bonds but meets difficulty with the geometry of polyatomic molecules. The ground-state configuration of C is $1\mathrm{s}^2 2\mathrm{s}^2 2\mathrm{p}^2$, with only two unpaired electrons, so by Section 3.3.2 it should form $\ce{CH2}$ with a bond angle of $90^\circ$; in fact C forms $\ce{CH4}$ in which the four C–H bonds are identical, pointing to the four vertices of a regular tetrahedron with bond angles of $109.5^\circ$. In 1931 Pauling proposed hybrid orbital theory to explain such phenomena.

**Definition 3.4.1 (Hybrid Orbital)** In the formation of a molecule, several atomic orbitals of similar energy on the same atom recombine linearly into the same number of new orbitals with definite composition and direction; this process is called **hybridization**, and the new orbitals obtained are called **hybrid orbitals**.

The formation of $\ce{CH4}$ can be understood in steps: a 2s electron is promoted to a 2p orbital (promotion), one 2s and three 2p orbitals combine into four $\mathrm{sp}^3$ hybrid orbitals (hybridization), and each of the four hybrid orbitals overlaps with the 1s orbital of an H atom to form a sigma bond (bonding). Promotion costs energy, but the energy released by forming two more covalent bonds more than compensates. These steps are only a bookkeeping device to aid understanding and not a real sequence of events. Some points to note:

1. Hybridization occurs only in the formation of a molecule; isolated atoms are not hybridized;
2. Only orbitals of similar energy (such as ns and np of the same shell) can hybridize effectively;
3. Hybridizing $n$ atomic orbitals gives $n$ hybrid orbitals (a linear combination does not change the dimension of the space);
4. The angular distribution of a hybrid orbital is concentrated in one direction, overlapping more with the orbitals of other atoms and forming more stable bonds.

The angles between hybrid orbitals can be calculated directly. Suppose that in a set of equivalent hybrid orbitals each is composed of an s orbital and a p orbital pointing in its own direction:

$$
h_k = \frac{1}{\sqrt{1+\lambda^2}}\left(\phi_{\mathrm{s}} + \lambda\,\phi_{\mathrm{p}}^{(k)}\right),
$$
where $\phi_{\mathrm{p}}^{(k)} = n_x\phi_{\mathrm{p}_x} + n_y\phi_{\mathrm{p}_y} + n_z\phi_{\mathrm{p}_z}$ is the p orbital pointing along the unit vector $\boldsymbol{n}_k$ and $\lambda^2$ is the ratio of p character to s character ($\lambda^2 = m$ in $\mathrm{sp}^m$ hybridization). Since $\phi_{\mathrm{s}}, \phi_{\mathrm{p}_x}, \phi_{\mathrm{p}_y}, \phi_{\mathrm{p}_z}$ are mutually orthogonal and normalized, the overlap integral of $\phi_{\mathrm{p}}^{(k)}$ and $\phi_{\mathrm{p}}^{(l)}$ equals $\boldsymbol{n}_k\cdot\boldsymbol{n}_l = \cos\theta$. Hybrid orbitals must be mutually orthogonal (otherwise they would overlap one another and could not each hold an independent pair of electrons), and so

$$
\int h_k h_l\,\mathrm{d}V = \frac{1 + \lambda^2\cos\theta}{1+\lambda^2} = 0,\qquad \cos\theta = -\frac{1}{\lambda^2}.
\tag{3.1}
$$
For $\mathrm{sp}^3$, $\cos\theta = -\frac13$ and $\theta = 109.47^\circ$; for $\mathrm{sp}^2$, $\cos\theta = -\frac12$ and $\theta = 120^\circ$; for sp, $\cos\theta = -1$ and $\theta = 180^\circ$. This agrees exactly with the geometry of the regular tetrahedron, the equilateral triangle and the straight line. It amounts to choosing an orthogonal basis in a four-dimensional function space ([2.1.7](/2.1.7)): hybridization does not change the total electron distribution, only switches to a basis better suited to describing localized bonds.

Equation (3.1) can also be used the other way round: the bond angle of $\ce{H2O}$, $104.5^\circ$, corresponds to $\lambda^2 = -1/\cos 104.5^\circ \approx 4.0$, that is, the two hybrid orbitals O uses for bonding contain about 20% s character, less than the 25% of $\mathrm{sp}^3$, the extra s character going to the lone pairs.

![sp, sp² and sp³ hybrids built from hydrogen-like 2s and 2p orbitals, drawn as contours in one plane: each hybrid is concentrated on one side of the nucleus](./plots/hybrid-orbitals.py)

### 3.4.2. The sp³, sp² and sp Hybridizations

| Hybridization | Orbitals involved | s character | Angle | Geometry | Examples |
|---|---|---|---|---|---|
| $\mathrm{sp}^3$ | 1 s + 3 p | $\frac14$ | $109.5^\circ$ | Regular tetrahedron | $\ce{CH4}$, $\ce{SiF4}$, $\ce{CCl4}$, diamond |
| $\mathrm{sp}^2$ | 1 s + 2 p | $\frac13$ | $120^\circ$ | Trigonal planar | $\ce{BF3}$, $\ce{BCl3}$, $\ce{C2H4}$, graphite |
| sp | 1 s + 1 p | $\frac12$ | $180^\circ$ | Linear | $\ce{BeCl2}$ (gas), $\ce{HgCl2}$, $\ce{C2H2}$, $\ce{CO2}$ |

In $\ce{BF3}$ B ($2\mathrm{s}^2 2\mathrm{p}^1$) is promoted and $\mathrm{sp}^2$ hybridized; the three hybrid orbitals bond with F, leaving an empty 2p orbital perpendicular to the molecular plane, which makes $\ce{BF3}$ a Lewis acid.

Now consider ethylene and acetylene. In $\ce{C2H4}$ each C is $\mathrm{sp}^2$ hybridized: two hybrid orbitals form C–H sigma bonds with H and the third forms the C–C sigma bond with the other C; each C has one remaining 2p orbital perpendicular to the molecular plane, and these overlap side by side to form a pi bond. Ethylene is therefore a planar molecule with bond angles of about $120^\circ$, and the C=C bond cannot rotate freely. In $\ce{C2H2}$ each C is sp hybridized, the C–C sigma bond and the C–H sigma bonds lie on one line, and each C has two remaining mutually perpendicular 2p orbitals, forming two pi bonds that make up the C≡C triple bond.

```smiles
C=C C2H4
C#C C2H2
```

**Example 3.4.1** Use hybrid orbitals to explain the geometry of the following molecules. (1) $\ce{HgCl2}$ (linear): one 6s and one 6p orbital of Hg are sp hybridized. (2) $\ce{SiF4}$ (regular tetrahedron): the 3s and three 3p orbitals of Si are $\mathrm{sp}^3$ hybridized. (3) $\ce{BCl3}$ (trigonal planar): the 2s and two 2p orbitals of B are $\mathrm{sp}^2$ hybridized. (4) $\ce{NF3}$ (trigonal pyramidal, bond angle $102.2^\circ$): N is $\mathrm{sp}^3$ nonequivalently hybridized (Section 3.4.3), and the repulsion of the lone pair on the N–F bonds makes the bond angle smaller than $109.5^\circ$.

### 3.4.3. Equivalent and Nonequivalent Hybridization

**Definition 3.4.2** Hybridization in which the resulting hybrid orbitals have exactly the same composition (such as the four $\mathrm{sp}^3$ orbitals of $\ce{CH4}$, each containing $\frac14$ s and $\frac34$ p) is called **equivalent hybridization**; hybridization in which the compositions of the hybrid orbitals are not all the same because lone pairs take part is called **nonequivalent hybridization**.

In general, hybridization is equivalent when the electrons in all the participating orbitals are unpaired (or all used for bonding), and nonequivalent when lone pairs occupy some of the hybrid orbitals.

- $\ce{NH3}$: the $2\mathrm{s}^2 2\mathrm{p}^3$ of N is $\mathrm{sp}^3$ hybridized, one hybrid orbital is occupied by a lone pair and three bond with H. The lone pair is attracted by only one nucleus, so its electron cloud lies closer to N and is "fatter", and it repels the bonding electrons more strongly, compressing the bond angle from $109.5^\circ$ to $106.7^\circ$ and giving a trigonal pyramidal molecule.
- $\ce{H2O}$: the $2\mathrm{s}^2 2\mathrm{p}^4$ of O is $\mathrm{sp}^3$ hybridized, two hybrid orbitals are occupied by lone pairs, the bond angle is compressed further to $104.5^\circ$ and the molecule is V-shaped.

The hybrid orbitals occupied by lone pairs contain more s character (lower energy) and the bonding orbitals more p character, consistent with the calculation from Eq. (3.1).

### 3.4.4. Delocalized Pi Bonds

The Lewis structures of molecules such as $\ce{O3}$, $\ce{NO3-}$ and benzene must be written as several equivalent structures (Example 3.2.1), yet the measured bond lengths are completely equalized. The reason is that the electrons forming the pi bonds in these molecules do not belong to two particular atoms but move over three or more atoms.

**Definition 3.4.3 (Delocalized Pi Bond)** A pi bond formed by the continuous overlap of several (three or more) mutually parallel p orbitals, with the pi electrons moving over several atoms, is called a **delocalized pi bond** (large pi bond), written $\Pi_m^n$, where $m$ is the number of atoms involved and $n$ the number of pi electrons. The conditions for forming one are that the atoms involved lie in one plane (or on one line), each atom supplies one mutually parallel p orbital, and $n < 2m$.

A pi bond between only two atoms is a localized pi bond. A convenient way to find the number $n$ of pi electrons: subtract from the total number of valence electrons the sigma-bond electrons and the lone-pair electrons that are not in pi orbitals; what remains are the pi electrons.

| Species | Hybridization of central atom | Valence electrons | Sigma electrons | Lone-pair electrons not in pi | Delocalized pi bond |
|---|---|---|---|---|---|
| $\ce{O3}$ | $\mathrm{sp}^2$ | 18 | 4 | 10 (1 pair on the center, 2 on each end) | $\Pi_3^4$ |
| $\ce{SO2}$ | $\mathrm{sp}^2$ | 18 | 4 | 10 | $\Pi_3^4$ |
| $\ce{CO2}$ | sp | 16 | 4 | 4 (1 pair on each O) | Two mutually perpendicular $\Pi_3^4$ |
| $\ce{NO3-}$, $\ce{CO3^2-}$ | $\mathrm{sp}^2$ | 24 | 6 | 12 (2 pairs on each O) | $\Pi_4^6$ |
| $\ce{SO3}$ | $\mathrm{sp}^2$ | 24 | 6 | 12 | $\Pi_4^6$ |
| Benzene $\ce{C6H6}$ | $\mathrm{sp}^2$ | 30 | 24 | 0 | $\Pi_6^6$ |

All six C atoms of benzene are $\mathrm{sp}^2$ hybridized, forming 6 C–C and 6 C–H sigma bonds in a planar regular hexagon; each C has one remaining 2p orbital perpendicular to the ring plane, 6 electrons in all, forming $\Pi_6^6$, so the six C–C bonds are all $139.7\,\mathrm{pm}$ long, between a single bond ($154$) and a double bond ($134$). Skeletal formulas are usually drawn as one Kekulé structure:

```smiles
c1ccccc1 C6H6
[O-][N+](=O)[O-] NO3-
[O-]C(=O)[O-] CO3^2-
[O-][O+]=O O3
```

Delocalization widens the range of motion of the electrons and lowers the energy, so molecules with delocalized pi bonds are more stable than estimated from localized structures (the delocalization energy of benzene is about $150\,\mathrm{kJ\,mol^{-1}}$); this is described in organic chemistry by resonance theory and aromaticity ([6.5](/6.5)) and calculated quantitatively in structural chemistry by Hückel molecular orbital theory ([6.2](/6.2)).

### 3.4.5. Hybridization Involving d Orbitals

| Hybridization | Number of orbitals | Geometry | Examples |
|---|---|---|---|
| $\mathrm{dsp}^2$ | 4 | Square planar | $\ce{[Ni(CN)4]^2-}$, $\ce{[Cu(NH3)4]^2+}$ |
| $\mathrm{sp}^3\mathrm{d}$ | 5 | Trigonal bipyramidal | $\ce{PCl5}$ |
| $\mathrm{sp}^3\mathrm{d}^2$ | 6 | Octahedral | $\ce{SF6}$ |
| $\mathrm{sp}^3\mathrm{d}^3$ | 7 | Pentagonal bipyramidal | $\ce{IF7}$ |

For transition-metal complexes the energies of $(n-1)\mathrm{d}$, $n\mathrm{s}$ and $n\mathrm{p}$ are close, and hybridizations such as $\mathrm{dsp}^2$ and $\mathrm{d}^2\mathrm{sp}^3$ are the basic tools of valence bond theory for describing the geometry of complexes ([6.1.5](/6.1.5)).

For molecules such as $\ce{PCl5}$ and $\ce{SF6}$ in which the central main-group atom has more than 8 electrons around it, that is, *hypervalent molecules*, the language of "$\mathrm{sp}^3\mathrm{d}$" and "$\mathrm{sp}^3\mathrm{d}^2$ hybridization" is outdated: the 3d orbitals of P and S are much higher in energy than 3s and 3p and too diffuse in space, and modern quantum-chemical calculations show that they contribute little to bonding (acting mainly as polarization functions). The bonding in these molecules is better explained by the *three-center four-electron bond* and strong bond polarity: for example the F–Xe–F unit of $\ce{XeF2}$ and the axial Cl–P–Cl unit of $\ce{PCl5}$ both share 4 electrons among three p orbitals on three atoms, as discussed in [structural chemistry](/6.2). Their geometries can nevertheless be predicted correctly by the valence shell electron pair repulsion theory below.

## 3.5. Valence Shell Electron Pair Repulsion Theory

### 3.5.1. Basic Points

Hybrid orbital theory can explain known molecular geometries, but which hybridization a molecule adopts is often hard to judge in advance (what are the hybridizations of Cl in $\ce{ClO3-}$ and P in $\ce{PCl6-}$?). The *valence shell electron pair repulsion theory*, VSEPR theory for short, proposed by Sidgwick and Powell in 1940 and developed by Gillespie and Nyholm in 1957, needs no orbital concepts and predicts the geometries of main-group compounds fairly reliably from the repulsion between electron pairs alone. Its main points are:

1. In a molecule or ion of type $\mathrm{AX}_m\mathrm{E}_n$ (A the central atom, X the ligand atoms, E lone pairs), the electron pairs in the valence shell of the central atom (bonding pairs and lone pairs) stay as far apart as possible so that the repulsion is smallest, which determines the arrangement of electron pairs in space;
2. The molecular geometry is the geometry determined by the positions of the ligand atoms after removing the lone pairs;
3. Double and triple bonds are treated as one electron pair (they occupy only one direction);
4. The order of repulsion strength is: lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair.

The number of valence-shell electron pairs (bonding pairs plus lone pairs) is calculated from

$$
\text{number of pairs} = \frac{\text{valence electrons of central atom} + \text{electrons supplied by ligand atoms} - \text{charge of ion}}{2},
\tag{3.2}
$$
where each ligand H and halogen supplies 1 electron, O and S as ligand atoms supply none (they form double bonds with the central atom or take electrons from it), and the charge of the ion is signed (for an anion subtract the negative number, that is, add the electrons). When the result is a half-integer (a single electron is included), the single electron is counted as one electron pair. For example $\ce{SO4^2-}$: $(6 + 0 + 2)/2 = 4$; $\ce{NH4+}$: $(5 + 4 - 1)/2 = 4$. The number of lone pairs = number of valence-shell pairs − number of ligand atoms.

### 3.5.2. Electron-Pair Geometry and Molecular Geometry

| Number of pairs | Electron-pair geometry | Lone pairs | Type | Molecular geometry | Examples |
|---|---|---|---|---|---|
| 2 | Linear | 0 | $\mathrm{AX_2}$ | Linear | $\ce{BeCl2}$, $\ce{CO2}$ |
| 3 | Trigonal planar | 0 | $\mathrm{AX_3}$ | Trigonal planar | $\ce{BF3}$, $\ce{SO3}$, $\ce{CO3^2-}$ |
| | | 1 | $\mathrm{AX_2E}$ | V-shaped | $\ce{SO2}$, $\ce{O3}$ |
| 4 | Tetrahedral | 0 | $\mathrm{AX_4}$ | Tetrahedral | $\ce{CH4}$, $\ce{SO4^2-}$ |
| | | 1 | $\mathrm{AX_3E}$ | Trigonal pyramidal | $\ce{NH3}$, $\ce{ClO3-}$ |
| | | 2 | $\mathrm{AX_2E_2}$ | V-shaped | $\ce{H2O}$, $\ce{ICl2+}$ |
| 5 | Trigonal bipyramidal | 0 | $\mathrm{AX_5}$ | Trigonal bipyramidal | $\ce{PCl5}$ |
| | | 1 | $\mathrm{AX_4E}$ | Seesaw | $\ce{SF4}$ |
| | | 2 | $\mathrm{AX_3E_2}$ | T-shaped | $\ce{ClF3}$ |
| | | 3 | $\mathrm{AX_2E_3}$ | Linear | $\ce{XeF2}$, $\ce{I3-}$ |
| 6 | Octahedral | 0 | $\mathrm{AX_6}$ | Octahedral | $\ce{SF6}$, $\ce{PCl6-}$ |
| | | 1 | $\mathrm{AX_5E}$ | Square pyramidal | $\ce{BrF5}$ |
| | | 2 | $\mathrm{AX_4E_2}$ | Square planar | $\ce{XeF4}$ |

![VSEPR: the five electron-pair geometries (rows for 2 and 3, 4, 5, 6 pairs) and the molecular shapes derived from them; blue balls are bonded atoms, orange lobes are lone pairs](./plots/vsepr-geometries.py)

The number of valence-shell electron pairs corresponds one to one with the hybridization: 2 pairs sp, 3 pairs $\mathrm{sp}^2$, 4 pairs $\mathrm{sp}^3$ (for main-group molecules with 5 and 6 pairs see the remarks in Section 3.4.5). It is therefore usual to determine the geometry with VSEPR first and then describe the bonding with hybrid orbitals.

### 3.5.3. Positions of Lone Pairs and Bond Angles

- Positions of lone pairs: repulsion is strongest between electron pairs at $90^\circ$, so a lone pair preferentially occupies the position with the fewest $90^\circ$ contacts with other pairs. In a trigonal bipyramid an equatorial position makes $90^\circ$ with only two axial positions, while an axial position makes $90^\circ$ with three equatorial positions, so lone pairs always occupy equatorial positions ($\ce{SF4}$, $\ce{ClF3}$, $\ce{XeF2}$); in an octahedron two lone pairs sit opposite each other ($\ce{XeF4}$ is square planar).
- Lone pairs compress bond angles: $\ce{CH4}$ $109.5^\circ$ > $\ce{NH3}$ $106.7^\circ$ > $\ce{H2O}$ $104.5^\circ$.
- Effect of the electronegativity of the ligand atom: the greater the electronegativity of the ligand atom, the more the bonding pair is drawn toward it, the farther from the central atom and the smaller the repulsion between bonding pairs, so the smaller the bond angle: $\ce{NF3}$ $102.2^\circ$ < $\ce{NH3}$ $106.7^\circ$.
- Effect of the electronegativity of the central atom: in one group, the smaller the electronegativity of the central atom, the farther the bonding pairs are from the center and the smaller the bond angle: $\ce{NH3}$ $106.7^\circ$ > $\ce{PH3}$ $93.3^\circ$.
- Effect of multiple bonds: double and triple bonds have higher electron density and repel more strongly, as in $\ce{COCl2}$, where $\angle\ce{ClCCl} \approx 112^\circ$, smaller than $120^\circ$.

### 3.5.4. Worked Examples

**Example 3.5.1** Use VSEPR theory to determine the geometries of $\ce{I3-}$, $\ce{ICl2+}$, $\ce{CO3^2-}$, $\ce{NO2}$, $\ce{O3}$, $\ce{SO3}$, $\ce{ClO3-}$ and $\ce{PCl6-}$.

| Species | Number of pairs (Eq. (3.2)) | Lone pairs | Electron-pair geometry | Molecular geometry |
|---|---|---|---|---|
| $\ce{I3-}$ | $(7 + 2 + 1)/2 = 5$ | 3 | Trigonal bipyramidal | Linear |
| $\ce{ICl2+}$ | $(7 + 2 - 1)/2 = 4$ | 2 | Tetrahedral | V-shaped |
| $\ce{CO3^2-}$ | $(4 + 0 + 2)/2 = 3$ | 0 | Trigonal planar | Trigonal planar |
| $\ce{NO2}$ | $(5 + 0)/2 = 2.5 \to 3$ | 1 (single electron) | Trigonal planar | V-shaped |
| $\ce{O3}$ | $(6 + 0)/2 = 3$ | 1 | Trigonal planar | V-shaped |
| $\ce{SO3}$ | $(6 + 0)/2 = 3$ | 0 | Trigonal planar | Trigonal planar |
| $\ce{ClO3-}$ | $(7 + 0 + 1)/2 = 4$ | 1 | Tetrahedral | Trigonal pyramidal |
| $\ce{PCl6-}$ | $(5 + 6 + 1)/2 = 6$ | 0 | Octahedral | Octahedral |

In $\ce{NO2}$ the single electron repels less than a lone pair, and the bond angle is $134^\circ$, larger than $120^\circ$; $\ce{NO2+}$, which has lost this electron, is linear, and $\ce{NO2-}$, which has gained one, has a bond angle of $115^\circ$. The bond angle of $\ce{O3}$ is $116.8^\circ$.

Limitations of VSEPR theory: it is basically inapplicable to transition-metal compounds (because of the influence of d electrons), and fails for a few compounds of heavy elements (for example $\ce{[SeCl6]^2-}$ and $\ce{[TeBr6]^2-}$ have a lone pair yet are regular octahedra; the lone pair has no directional character in space and is called a stereochemically inert lone pair).

## 3.6. Molecular Orbital Theory

### 3.6.1. Molecular Orbitals and the Linear Combination of Atomic Orbitals

Valence bond theory localizes the bonding electrons between two atoms, which is intuitive and consistent with chemical structural formulas, but it has two clear difficulties:

1. $\ce{O2}$ is a **paramagnetic substance** (liquid oxygen is attracted by a magnet), which shows that the molecule has unpaired electrons, whereas in the Lewis structure $\ce{O=O}$ all electrons are paired.
2. $\ce{H2+}$ has only one electron yet is stable (dissociation energy $256\,\mathrm{kJ\,mol^{-1}}$), which cannot be explained by "electron pairs".

*Molecular orbital theory*, proposed by Mulliken and Hund around 1932, treats the molecule as a whole:

**Definition 3.6.1 (Molecular Orbital)** Each electron in a molecule moves in the average field of all the nuclei and the remaining electrons and no longer belongs to a particular atom; the wave function $\psi_i$ describing the state of motion of a single electron over the whole molecule is called a **molecular orbital**, and it has a definite energy $E_i$.

Molecular orbitals are polycentric whereas atomic orbitals are monocentric; molecular orbitals are labeled sigma, pi, delta and so on (with the same symmetry about the bond axis as in Section 3.3.3). The electrons of a molecule are filled into the molecular orbitals according to the **aufbau principle**, the **Pauli exclusion principle** and **Hund's rule**, exactly as for electron configurations in atoms ([5.5.4](/5.5.4#sec-4.4.3)).

The commonly used approximation for molecular orbitals is the *linear combination of atomic orbitals*, LCAO: a molecular orbital is written as a linear combination of atomic orbitals, and $n$ atomic orbitals combine into $n$ molecular orbitals. Take two atoms a and b each supplying one atomic orbital, $\phi_a$ and $\phi_b$:

$$
\psi = c_a\phi_a + c_b\phi_b .
$$
Finding the extremum of the energy by the variational principle ([structural chemistry](/6.2)) gives the $2\times 2$ secular equation

$$
\begin{bmatrix} \alpha_a - E & \beta - ES \\ \beta - ES & \alpha_b - E \end{bmatrix}
\begin{bmatrix} c_a \\ c_b \end{bmatrix} = \boldsymbol{0},
$$
where $\alpha_a$ and $\alpha_b$ are the energies of the two atomic orbitals (Coulomb integrals), $\beta < 0$ is the interaction between the two atomic orbitals (the exchange integral, also called the resonance integral) and $S$ is their overlap integral. The condition for a nonzero solution is that the determinant of the coefficients vanishes. For the homonuclear case $\alpha_a = \alpha_b = \alpha$ and the solution is

$$
E_\pm = \frac{\alpha \pm \beta}{1 \pm S},\qquad \psi_\pm = \frac{\phi_a \pm \phi_b}{\sqrt{2(1\pm S)}} .
\tag{3.3}
$$
Neglecting $S$, these are exactly the two eigenvalues $\alpha\pm\beta$ and the orthogonal eigenvectors of the real symmetric matrix $\begin{bmatrix}\alpha & \beta\\ \beta & \alpha\end{bmatrix}$ ([2.1.7](/2.1.7#thm-7.1.1)), and also the case $N = 2$ of the tight-binding model ([5.5.6](/5.5.6#sec-6.2.3)): the two atomic levels split into one higher and one lower, and for $N$ atoms they broaden into an energy band ([6.1.4](/6.1.4)).

**Definition 3.6.2 (Bonding and Antibonding Orbitals)** The molecular orbital formed by in-phase combination of atomic orbitals ($\phi_a + \phi_b$) has increased electron probability density between the nuclei and an energy lower than that of the original atomic orbitals, and is called a **bonding orbital**; the molecular orbital formed by out-of-phase combination ($\phi_a - \phi_b$) has a nodal plane between the nuclei, reduced electron probability density there and an energy higher than that of the original atomic orbitals, and is called an **antibonding orbital**, marked with an asterisk ($\sigma^*$, $\pi^*$). A molecular orbital with the same energy as the atomic orbitals that takes no part in bonding is called a nonbonding orbital.

From Eq. (3.3), for $S > 0$ the energy by which the antibonding orbital is raised, $\frac{\alpha S - \beta}{1 - S}$, is greater than the energy by which the bonding orbital is lowered, $\frac{\alpha S - \beta}{1 + S}$ (the numerators are the same and the denominator $1 - S < 1 + S$), so when both the bonding and antibonding orbitals are filled the energy of the system actually rises, which explains why $\ce{He2}$ cannot form a stable molecule.

### 3.6.2. Three Principles for Effective Combination into Molecular Orbitals

1. Symmetry matching: only atomic orbitals with the same symmetry about the bond axis can combine into molecular orbitals. For example s and $\mathrm{p}_z$ (with the bond axis along $z$) can form a sigma orbital; in the overlap of s with $\mathrm{p}_x$ the positive and negative parts cancel, the net overlap is zero and no bond forms. A rigorous statement of symmetry matching requires point groups ([6.2](/6.2)).
2. Similar energy: the greater the energy difference between two atomic orbitals, the closer the resulting molecular orbitals are to the original atomic orbitals and the weaker the bonding effect; when the difference is too large the orbitals effectively cannot combine. In homonuclear diatomic molecules identical orbitals combine; in heteronuclear diatomic molecules it is mainly valence orbitals of similar energy that combine.
3. Maximum overlap: given symmetry matching, the more the atomic orbitals overlap, the more the energy of the bonding orbital is lowered and the more stable the bond (the same as the **principle of maximum overlap** of valence bond theory).

The types of overlap satisfying these conditions are s–s, s–p, p–p (sigma and pi types), p–d (pi type, for example between a transition metal and a ligand with p orbitals) and d–d (sigma, pi and delta types).

### 3.6.3. Homonuclear Diatomic Molecules of the Second Period

Take the bond axis as $z$. The 1s orbitals of the two atoms form $\sigma_{1\mathrm{s}}$ and $\sigma^*_{1\mathrm{s}}$, and the 2s orbitals form $\sigma_{2\mathrm{s}}$ and $\sigma^*_{2\mathrm{s}}$; the $2\mathrm{p}_z$ orbitals overlap head-on to form $\sigma_{2\mathrm{p}}$ and $\sigma^*_{2\mathrm{p}}$, and the $2\mathrm{p}_x$ and $2\mathrm{p}_y$ orbitals overlap side by side to form two degenerate $\pi_{2\mathrm{p}}$ orbitals and two degenerate $\pi^*_{2\mathrm{p}}$ orbitals. The inner $\sigma_{1\mathrm{s}}$ and $\sigma^*_{1\mathrm{s}}$ are both filled and make no net contribution to bonding, and are usually written KK. There are two orders of energy levels:

- $\ce{O2}$, $\ce{F2}$ (large 2s–2p energy difference): $\sigma_{2\mathrm{s}} < \sigma^*_{2\mathrm{s}} < \sigma_{2\mathrm{p}} < \pi_{2\mathrm{p}} < \pi^*_{2\mathrm{p}} < \sigma^*_{2\mathrm{p}}$;
- $\ce{Li2}$–$\ce{N2}$ (similar 2s and 2p energies): $\sigma_{2\mathrm{s}} < \sigma^*_{2\mathrm{s}} < \pi_{2\mathrm{p}} < \sigma_{2\mathrm{p}} < \pi^*_{2\mathrm{p}} < \sigma^*_{2\mathrm{p}}$.

The difference comes from s–p mixing: when the energies of 2s and $2\mathrm{p}_z$ are close, the sigma orbitals of the same symmetry formed from them ($\sigma_{2\mathrm{s}}$ with $\sigma_{2\mathrm{p}}$, and $\sigma^*_{2\mathrm{s}}$ with $\sigma^*_{2\mathrm{p}}$) interact further, one going down and one going up in the manner of Eq. (3.3), which raises $\sigma_{2\mathrm{p}}$ above $\pi_{2\mathrm{p}}$. From Li to F the nuclear charge increases and the 2s level falls faster than 2p (2s penetrates more, [6.1.2](/6.1.2)), the gap between them grows and s–p mixing weakens, and by O and F the order is reversed. That $\ce{B2}$ is paramagnetic and $\ce{C2}$ diamagnetic both confirm that $\pi_{2\mathrm{p}}$ lies below $\sigma_{2\mathrm{p}}$.

![Schematic valence MO energy diagrams: O₂ without s–p mixing, N₂ with s–p mixing (σ₂ₚ above π₂ₚ), and the heteronuclear CO with its HOMO and LUMO](./plots/mo-diagrams.py)

**Definition 3.6.3 (Bond Order)** The **bond order** of a molecule is defined as

$$
\text{bond order} = \frac{\text{number of electrons in bonding orbitals} - \text{number of electrons in antibonding orbitals}}{2}.
$$

The bond order corresponds to the number of bonds in valence bond theory and can be a half-integer. The greater the bond order, the stronger and shorter the bond; a molecule with bond order zero cannot exist stably. Another direct consequence of molecular orbital theory is the magnetism of the molecule: a molecule with unpaired electrons is paramagnetic, otherwise it is diamagnetic (**diamagnetic substance**, [5.3.8](/5.3.8)).

| Molecule | Valence configuration | Bond order | Bond length / pm | Dissociation energy / (kJ mol⁻¹) | Magnetism |
|---|---|---|---|---|---|
| $\ce{H2+}$ | $(\sigma_{1\mathrm{s}})^1$ | 0.5 | 106 | 256 | Paramagnetic |
| $\ce{H2}$ | $(\sigma_{1\mathrm{s}})^2$ | 1 | 74 | 436 | Diamagnetic |
| $\ce{He2+}$ | $(\sigma_{1\mathrm{s}})^2(\sigma^*_{1\mathrm{s}})^1$ | 0.5 | 108 | about 240 | Paramagnetic |
| $\ce{Li2}$ | KK$(\sigma_{2\mathrm{s}})^2$ | 1 | 267 | 101 | Diamagnetic |
| $\ce{Be2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2$ | 0 | 245 | about 11 | Diamagnetic |
| $\ce{B2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2(\pi_{2\mathrm{p}})^2$ | 1 | 159 | 290 | Paramagnetic |
| $\ce{C2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2(\pi_{2\mathrm{p}})^4$ | 2 | 124 | about 600 | Diamagnetic |
| $\ce{N2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2(\pi_{2\mathrm{p}})^4(\sigma_{2\mathrm{p}})^2$ | 3 | 110 | 945 | Diamagnetic |
| $\ce{O2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2(\sigma_{2\mathrm{p}})^2(\pi_{2\mathrm{p}})^4(\pi^*_{2\mathrm{p}})^2$ | 2 | 121 | 498 | Paramagnetic |
| $\ce{F2}$ | KK$(\sigma_{2\mathrm{s}})^2(\sigma^*_{2\mathrm{s}})^2(\sigma_{2\mathrm{p}})^2(\pi_{2\mathrm{p}})^4(\pi^*_{2\mathrm{p}})^4$ | 1 | 141 | 159 | Diamagnetic |

Some remarks:

- The two $\pi^*_{2\mathrm{p}}$ electrons of $\ce{O2}$ occupy two degenerate orbitals with parallel spins by Hund's rule, so $\ce{O2}$ has two unpaired electrons and is paramagnetic, the most famous success of molecular orbital theory. In the language of valence bond theory, $\ce{O2}$ has one sigma bond and two three-electron pi bonds (each consisting of two electrons in a bonding pi orbital and one in an antibonding pi orbital, equivalent to half a bond), giving a total bond order of 2.
- The bond in $\ce{H2+}$ is a one-electron bond (bond order 0.5).
- By bond order $\ce{Be2}$ should not exist; in fact it is a very weakly bound molecule (dissociation energy about $11\,\mathrm{kJ\,mol^{-1}}$, of the order of van der Waals interactions) that can be observed spectroscopically in the gas phase but cannot form a stable substance. $\ce{He2}$ and $\ce{Ne2}$ likewise have only very weak van der Waals binding.
- $\ce{N2}$ has bond order 3 and dissociation energy $945\,\mathrm{kJ\,mol^{-1}}$, among the strongest bonds in homonuclear diatomic molecules, which is why nitrogen is chemically inert and why ammonia synthesis requires a catalyst.

**Example 3.6.1** Write the molecular orbital configurations of $\ce{O2+}$, $\ce{O2}$, $\ce{O2-}$ and $\ce{O2^2-}$, and compare their bond orders, bond lengths and magnetism.

Their electron numbers are 15, 16, 17 and 18, obtained from $\ce{O2}$ by adding or removing $\pi^*_{2\mathrm{p}}$ electrons:

| Species | Number of $\pi^*_{2\mathrm{p}}$ electrons | Bond order | Bond length / pm | Magnetism | Example |
|---|---|---|---|---|---|
| $\ce{O2+}$ | 1 | 2.5 | 112 | Paramagnetic | $\ce{O2+[PtF6]-}$ |
| $\ce{O2}$ | 2 | 2 | 121 | Paramagnetic | Oxygen gas |
| $\ce{O2-}$ | 3 | 1.5 | about 133 | Paramagnetic | Potassium superoxide $\ce{KO2}$ |
| $\ce{O2^2-}$ | 4 | 1 | about 149 | Diamagnetic | Sodium peroxide $\ce{Na2O2}$ |

Removing an antibonding electron strengthens the bond, so $\ce{O2+}$ is more stable than $\ce{O2}$ and its bond is shorter (dissociation energy $643$ against $498\,\mathrm{kJ\,mol^{-1}}$); from $\ce{O2+}$ to $\ce{O2^2-}$ the bond order decreases and the bond length increases in turn.

### 3.6.4. Frontier Orbitals

**Definition 3.6.4 (Frontier Orbitals)** The occupied molecular orbital of highest energy in a molecule is called the **highest occupied molecular orbital** (HOMO) and the unoccupied molecular orbital of lowest energy is called the **lowest unoccupied molecular orbital** (LUMO); together they are called the **frontier orbitals**.

The electrons in the HOMO have the highest energy and are the most easily lost or donated, and the LUMO accepts electrons most readily, so much of the chemical behavior of a molecule (acting as an electron-pair donor or acceptor, redox reactions, light absorption) is determined mainly by the frontier orbitals. In the 1950s Fukui's frontier orbital theory and the Woodward–Hoffmann rules thereby explained a large class of organic reactions ([6.5](/6.5)). For example the HOMO of $\ce{N2}$ is $\sigma_{2\mathrm{p}}$ and its LUMO is $\pi^*_{2\mathrm{p}}$; the HOMO of $\ce{O2}$ is the half-filled $\pi^*_{2\mathrm{p}}$.

### 3.6.5. Heteronuclear Diatomic Molecules: CO

In a heteronuclear diatomic molecule the orbital energies of the two atoms differ: the more electronegative atom has lower atomic orbital energies. A bonding orbital lies closer to the lower-energy atomic orbital and is mainly composed of it; an antibonding orbital is mainly composed of the higher-energy atomic orbital.

$\ce{CO}$ and $\ce{N2}$ have the same number of atoms and the same number of valence electrons (10). Molecules or ions with the same number of atoms and the same total number of valence electrons are *isoelectronic species*, and their molecular orbitals and structures are often similar (right of the figure above). Numbering the valence orbitals, the valence configuration of $\ce{CO}$ is

$$
(3\sigma)^2(4\sigma)^2(1\pi)^4(5\sigma)^2,
$$
with bond order 3, bond length $112.8\,\mathrm{pm}$ and dissociation energy $1072\,\mathrm{kJ\,mol^{-1}}$, one of the strongest known chemical bonds. The orbital energies of O are low, and bonding orbitals such as $3\sigma$ and $1\pi$ are weighted toward O; the HOMO $5\sigma$ is concentrated mainly on the outer side of C and corresponds to a lone pair on C, and the LUMO $2\pi$ (that is, $\pi^*$) is also mainly composed of C. $\ce{CO}$ therefore always coordinates to metals through the C end: $5\sigma$ donates electrons to an empty orbital of the metal (a sigma coordinate bond) while d electrons of the metal flow back into the $2\pi$ orbital of $\ce{CO}$ (a back-donation pi bond), which is the bonding mode of metal carbonyls ([6.1.5](/6.1.5)). The electrons of $5\sigma$ weighted toward the outside of C also explain why the negative end of the dipole moment of $\ce{CO}$ is on the C side (Example 3.2.1).

## 3.7. Bond Polarity and Molecular Polarity

### 3.7.1. Polar and Nonpolar Bonds

The shared electron pair in a covalent bond is not necessarily located midway between the nuclei.

**Definition 3.7.1 (Polar and Nonpolar Bonds)** In a covalent bond between atoms of the same kind the two atoms attract electrons equally and the shared pair is not displaced toward either; such a bond is called a **nonpolar bond**. In a covalent bond between different atoms the shared pair is displaced toward the atom of larger **electronegativity**, so that one end of the bond carries a partial negative charge ($\delta^-$) and the other a partial positive charge ($\delta^+$); such a bond is called a **polar bond**.

The larger the electronegativity difference $\Delta\chi$ of the bonded atoms, the stronger the polarity of the bond: $\Delta\chi = 0$ gives a nonpolar bond; a moderate $\Delta\chi$ gives a polar bond; and when $\Delta\chi$ is very large the electron is almost completely transferred and the bond becomes ionic. There is thus no sharp boundary between ionic and covalent bonds: the polar covalent bond is the transition between them, and the ionic bond can be regarded as the limit of the polar bond. Empirically, when $\Delta\chi > 1.7$ or so the ionic character of the bond exceeds 50%, but this is only a rough criterion ($\Delta\chi$ for $\ce{HF}$ is 1.78, yet it is a covalent molecule). The ionic bond theory and the covalent bond theory each describe one aspect of the chemical bond and complement each other; the covalent character in ionic compounds is described by ionic polarization ([6.1.4](/6.1.4)).

### 3.7.2. Polar Molecules and Dipole Moments

If the center of positive charge (the nuclei) and the center of negative charge (the electron cloud) in a molecule do not coincide, the molecule has a permanent **electric dipole moment** ([5.3.4](/5.3.4#sec-4.2.1)) and is called a polar molecule; otherwise it is a nonpolar molecule. In the chemical literature the electric dipole moment is often written $\mu$; this wiki follows the physics convention and writes it $\boldsymbol{p}$, with magnitude $p = qd$, where $q$ is the charge at the center of positive (negative) charge and $d$ is the distance between the two centers (the dipole length), and with direction from the negative to the positive center. The SI unit is $\mathrm{C\,m}$, and chemists often use the debye: $1\,\mathrm{D} = 3.336\times 10^{-30}\,\mathrm{C\,m}$ (that is, $10^{-21}/c\,\mathrm{C\,m}$ with $c$ in $\mathrm{m\,s^{-1}}$). The magnitude of molecular dipole moments is $e \times 10^{-10}\,\mathrm{m} \approx 10^{-29}$–$10^{-30}\,\mathrm{C\,m}$.

The dipole moment of a molecule is the vector sum of the dipole moments of the individual bonds (plus the contribution of lone pairs), so whether a molecule is polar depends both on the polarity of the bonds and on the geometry of the molecule:

- Molecules composed of nonpolar bonds ($\ce{H2}$, $\ce{P4}$, $\ce{S8}$) are nonpolar ($\ce{O3}$ is an exception: the chemical environments of the central and terminal O differ, $p = 0.53\,\mathrm{D}$);
- Molecules composed of polar bonds are still nonpolar if the geometry is symmetric and the bond dipoles cancel: linear $\ce{CO2}$, trigonal planar $\ce{BCl3}$, tetrahedral $\ce{CH4}$ and $\ce{CCl4}$;
- Molecules with unsymmetrical geometry are polar: V-shaped $\ce{H2O}$, trigonal pyramidal $\ce{NH3}$.

| Molecule | $p$ / D | Geometry | Molecule | $p$ / D | Geometry |
|---|---|---|---|---|---|
| $\ce{HF}$ | 1.83 | Linear | $\ce{H2O}$ | 1.85 | V-shaped |
| $\ce{HCl}$ | 1.11 | Linear | $\ce{NH3}$ | 1.47 | Trigonal pyramidal |
| $\ce{HBr}$ | 0.83 | Linear | $\ce{NF3}$ | 0.23 | Trigonal pyramidal |
| $\ce{HI}$ | 0.45 | Linear | $\ce{SO2}$ | 1.63 | V-shaped |
| $\ce{CO}$ | 0.11 | Linear | $\ce{CO2}$, $\ce{BCl3}$, $\ce{CH4}$ | 0 | Symmetric |

Conversely, the dipole moment can be used to infer the geometry of a molecule: $p = 1.47\,\mathrm{D}$ ($4.90\times 10^{-30}\,\mathrm{C\,m}$) for $\ce{NH3}$ shows that it is not planar but trigonal pyramidal; $p = 0$ for $\ce{BCl3}$ shows that it is trigonal planar. The dipole moment of $\ce{NF3}$ is much smaller than that of $\ce{NH3}$: the dipole of the N–F bond (pointing toward F) is opposite in direction to the contribution of the lone pair and they partly cancel, whereas the dipole of the N–H bond (pointing toward N) is in the same direction as the lone pair and they add.

**Example 3.7.1** The bond length of $\ce{HCl}$ is $127.5\,\mathrm{pm}$ and its dipole moment is $1.11\,\mathrm{D}$. If $\ce{HCl}$ were completely ionic, $\ce{H+Cl-}$, the dipole moment would be $p_{\mathrm{ion}} = ed = 1.602\times10^{-19}\,\mathrm{C} \times 1.275\times10^{-10}\,\mathrm{m} = 2.04\times10^{-29}\,\mathrm{C\,m} = 6.12\,\mathrm{D}$. The ratio of the measured value to this is $1.11/6.12 \approx 0.18$, so the partial charges on H and Cl are about $\pm 0.18e$, and one commonly says roughly that the H–Cl bond is about 18% ionic. Similarly one obtains about 41% for $\ce{HF}$ and about 6% for $\ce{HI}$ (bond lengths $91.7$ and $160.9\,\mathrm{pm}$ respectively).

The dipole moment is the source of the orientation (Keesom) and induction (Debye) forces between molecules and determines many properties of molecular crystals, as discussed in the next chapter, [6.1.4](/6.1.4).

## Summary

| Theory | Central idea | Explains | Limitations |
|---|---|---|---|
| Ionic bond theory | Gain and loss of electrons form ions, bound electrostatically | Composition and high melting points of ionic compounds | Cannot explain covalent molecules |
| Lewis theory | Shared electron pairs, octet rule | Composition and structural formulas of most molecules | Many exceptions; no directionality; does not explain the nature of the bond |
| Valence bond theory | Pairing of electrons of opposite spin, maximum orbital overlap | Nature, saturability and directionality of covalent bonds; sigma and pi bonds | Geometry of polyatomic molecules |
| Hybrid orbital theory | Recombination of orbitals on one atom | Molecular geometry, bond angles | Hybridization is hard to predict |
| VSEPR theory | Repulsion between valence-shell electron pairs | Geometry of main-group compounds (prediction) | Does not explain bonding; inapplicable to transition metals |
| Molecular orbital theory | Electrons belong to the whole molecule, LCAO | Magnetism, one-electron bonds, bond order, delocalization, spectra | Less intuitive than localized bonds; quantitative treatment needs calculation |

- The usual procedure for determining molecular geometry: draw the Lewis structure (choosing by formal charge when necessary) → find the number of valence-shell electron pairs from Eq. (3.2) → obtain the geometry from VSEPR → describe the sigma bonds with the corresponding hybridization, with the remaining p orbitals forming localized or delocalized pi bonds.
- The greater the bond order, the shorter and stronger the bond; molecules with unpaired electrons are paramagnetic.
- Bond polarity is determined by the electronegativity difference, and molecular polarity by the bond polarity and the molecular geometry together.

## Questions

1. Why does $\ce{PCl5}$ exist while $\ce{NCl5}$ does not? (N is a second-period element whose valence shell has only the four orbitals 2s and 2p, so it can form at most 4 covalent bonds, and the N atom is too small to accommodate 5 Cl; the larger P atom can form a hypervalent molecule, in the three-center four-electron bond picture.)
2. Why is $\ce{BF3}$ trigonal planar and $\ce{NF3}$ trigonal pyramidal? (B has 3 valence-shell electron pairs and no lone pair; N has 4 pairs including one lone pair.)
3. Use molecular orbital theory to decide which has the stronger bond, $\ce{N2+}$ or $\ce{N2}$, and $\ce{O2+}$ or $\ce{O2}$. ($\ce{N2+}$ has lost a bonding electron from $\sigma_{2\mathrm{p}}$, with bond order 2.5 < 3, weaker than $\ce{N2}$; $\ce{O2+}$ has lost an antibonding electron, with bond order 2.5 > 2, stronger than $\ce{O2}$.)
4. $\ce{CO2}$ and $\ce{SO2}$ are both triatomic molecules; why is one nonpolar and the other polar? (C in $\ce{CO2}$ has no lone pair and the molecule is linear, so the dipoles of the two C=O bonds cancel; S in $\ce{SO2}$ has one lone pair and the molecule is V-shaped, so they cannot cancel.)
