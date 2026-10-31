---
title: "X-Ray Crystallography: From Diffraction to Models"
description: X-ray crystallography of biological macromolecules from first principles to deposited model. Lattices, unit cells, symmetry operations, point groups and space groups, the crystallographic restriction and the 65 space groups of chiral molecules; the Laue equations, the reciprocal lattice, Bragg's law and the Ewald sphere; Thomson scattering, atomic scattering factors, the structure factor, the electron density as a Fourier series, temperature factors, Friedel's law and systematic absences; the phase problem, the Patterson function and direct methods; fiber diffraction of helices and Photo 51; crystallization, phase diagrams and nucleation; synchrotron data collection, radiation damage and the rotation method; indexing, integration, scaling, data quality and Wilson statistics, twinning; isomorphous replacement, anomalous scattering, SAD and MAD; molecular replacement with experimental and predicted models; density modification; model building, refinement, R and R_free, validation; X-ray free-electron lasers, serial and time-resolved crystallography.
---

X-ray crystallography determined the first atomic structures of proteins and of the DNA double helix, and it still accounts for most of the structures in the **Protein Data Bank**. Its principle is the one met in solution scattering ([7.6.9](/7.6.9#sec-9.3.1)): the amplitude of X-rays scattered by a distribution of electrons is the **Fourier transform** of that distribution. In solution the molecules tumble, the transform is averaged over orientations, and a one-dimensional curve remains. In a crystal, $10^{12}$–$10^{15}$ copies of the molecule are held in the same orientation at the points of a lattice. The orientational average disappears, the weak scattering of one molecule is amplified by coherent addition, and the transform is sampled at the points of a second lattice, the reciprocal lattice. From the intensities of tens of thousands of such samples, and from phases that have to be recovered by other means, the electron density of the molecule is computed as a Fourier series, and an atomic model is built into it and refined.

The chapter follows this path. It first describes crystals as lattices with symmetry (10.1) and derives the geometry of diffraction, the Laue equations, the reciprocal lattice, Bragg's law and the Ewald construction (10.2). It then computes the intensities, from the scattering of one electron to the structure factor of the unit cell, and shows that the electron density is the Fourier synthesis of the structure factors (10.3). The intensities alone do not determine the density; this **phase problem** is the central difficulty of the method, and the Patterson function and direct methods are the classical answers to it for small structures (10.4). Helical molecules that do not crystallize but can be aligned in fibers give a different kind of pattern, which revealed the α helix and the double helix (10.5). The second half follows a structure determination: crystallization (10.6), data collection (10.7), data processing and the statistics of intensities (10.8), experimental phasing by heavy atoms and anomalous scattering (10.9), molecular replacement (10.10), density modification (10.11), model building, refinement and validation (10.12), and finally the new possibilities of X-ray free-electron lasers and time-resolved crystallography (10.13).

The physics of X-ray **diffraction** by a crystal and Bragg's law are introduced in [5.4.2](/5.4.2#sec-2.5.3), the spectrum of X-rays in [5.5.5](/5.5.5), and the principle of crystal-structure analysis in [6.4.8](/6.4.8#sec-8.6); the overview of structure determination in [7.1.6](/7.1.6#sec-6.6.1) and the history of the double helix in [7.1.11](/7.1.11) are the biological starting points. The symmetry of molecular assemblies, point groups and helical symmetry, is the subject of [7.6.7](/7.6.7#sec-7.4); the Fourier series and transforms used throughout are those of [2.5.6](/2.5.6). Crystallography is compared with nuclear magnetic resonance ([7.6.13](/7.6.13)) and cryo-electron microscopy ([7.6.14](/7.6.14)) at the end, and predicted structures, which now often provide the starting phases, are the subject of [7.6.15](/7.6.15).

## 10.1. Crystals, Lattices and Symmetry

### 10.1.1. Why Crystals

A single protein molecule scatters X-rays extremely weakly. The scattering cross-section of one electron is $\frac{8\pi}{3}r_{\mathrm{e}}^2 = 6.65\times10^{-29}\,\mathrm{m^2}$, and a protein of $25\,\mathrm{kDa}$ has about $13\,000$ electrons; even the brightest synchrotron beam would deposit enough energy to destroy the molecule long before it had scattered enough photons to define its structure. The solution is to scatter from many identical molecules at once and to make their scattered waves add coherently. If $N$ molecules in identical orientations are placed at the points of a regular lattice, the waves they scatter in certain directions are in phase, and the intensity in those directions is $N^2$ times that of one molecule; in all other directions the waves cancel. A crystal of $0.1\,\mathrm{mm}$ contains about $10^{13}$ molecules, so the diffracted beams are strong enough to be measured, while the dose per molecule stays tolerable. The figure in 10.3.2 shows this amplification and sampling for a two-dimensional example.

The price is that the molecules must form an ordered crystal, which is often the hardest step of a project (10.6), and that the result is an average over all molecules of the crystal and over the time of the measurement. The average is sharp only if the molecules are identical and identically placed: chemical heterogeneity, flexible loops and disorder in the packing all blur the electron density and limit the resolution.

### 10.1.2. Lattice, Motif and Unit Cell

A crystal structure is described as a lattice plus a motif. The **crystal lattice** is the set of points $\boldsymbol{t} = m\boldsymbol{a} + n\boldsymbol{b} + p\boldsymbol{c}$ ($m, n, p \in \mathbb{Z}$) generated by three non-coplanar vectors; the motif (the structural unit) is the arrangement of atoms that is repeated at every lattice point. The parallelepiped spanned by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ is the **unit cell**, characterized by the six **lattice parameters** $a, b, c, \alpha, \beta, \gamma$ ($\alpha$ the angle between $\boldsymbol{b}$ and $\boldsymbol{c}$, and so on). The position of an atom in the cell is given by its fractional coordinates $(x, y, z)$, $\boldsymbol{r} = x\boldsymbol{a} + y\boldsymbol{b} + z\boldsymbol{c}$, with $0 \le x, y, z < 1$. The volume of the cell is

$$
V = \boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{c}) = abc\sqrt{1 - \cos^2\alpha - \cos^2\beta - \cos^2\gamma + 2\cos\alpha\cos\beta\cos\gamma}.
$$
For protein crystals the cell edges are typically $30$–$300\,\text{Å}$ (virus crystals reach $1000\,\text{Å}$), compared with $3$–$30\,\text{Å}$ for crystals of small molecules. The large cell is the source of both the richness of protein diffraction (many reflections) and its weakness (each reflection is weak, 10.3.4).

The geometry of diffraction (10.2) depends only on the lattice, the intensities (10.3) only on the contents of the cell. The determination of a crystal structure therefore splits into two problems: the six cell parameters and the symmetry, which follow from the positions of the diffraction spots, and the positions of the atoms in the cell, which follow from the intensities and phases.

### 10.1.3. Symmetry Operations and the Crystallographic Restriction

A symmetry operation of a crystal is an isometry of space that maps the crystal structure onto itself. In fractional coordinates it is written $\boldsymbol{x} \mapsto R\boldsymbol{x} + \boldsymbol{t}$ with a $3\times3$ matrix $R$ and a translation $\boldsymbol{t}$. Point operations, which leave at least one point fixed, are rotations, the mirror reflection $m$, the inversion $\bar 1$ and the rotoinversions $\bar n$ (rotation followed by inversion through a point on the axis). Operations with a translational part add the lattice translations themselves and two new kinds of operation:

- a screw axis $n_k$ combines a rotation by $360^\circ/n$ with a translation by $k/n$ of the lattice period along the axis; $2_1$, $3_1$, $3_2$, $4_1$, $4_2$, $4_3$ and $6_1$–$6_5$ are the eleven screw axes;
- a glide plane combines a reflection with a translation by half a lattice vector parallel to the plane.

For example, a twofold rotation axis along $\boldsymbol{b}$ through the origin maps $(x, y, z)$ to $(-x, y, -z)$, and a $2_1$ screw axis in the same place maps it to $(-x, y + \frac12, -z)$; in matrix form,

$$
2\colon\ \boldsymbol{x} \mapsto \begin{bmatrix} -1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & -1\end{bmatrix}\boldsymbol{x}, \qquad 2_1\colon\ \boldsymbol{x} \mapsto \begin{bmatrix} -1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & -1\end{bmatrix}\boldsymbol{x} + \begin{bmatrix} 0\\ \frac12\\ 0\end{bmatrix}.
$$

Not every rotation is compatible with a lattice.

**Theorem 10.1.1 (Crystallographic Restriction)** A rotation that maps a three-dimensional lattice onto itself has order $1$, $2$, $3$, $4$ or $6$.

**Proof** In the basis $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$, the rotation maps lattice vectors to lattice vectors, so its matrix $R$ has integer entries and its trace is an integer. In an orthonormal basis adapted to the axis, the same rotation by $\varphi$ has trace $1 + 2\cos\varphi$, and the trace does not depend on the basis. Hence $2\cos\varphi \in \{-2, -1, 0, 1, 2\}$, that is, $\varphi \in \{180^\circ, 120^\circ, 90^\circ, 60^\circ, 0^\circ\}$ up to sign, which are the rotations of orders $2, 3, 4, 6, 1$. $\square$

Fivefold, sevenfold and higher axes therefore never occur as symmetries of a crystal, although they are common in molecular assemblies (the pentameric channels and icosahedral capsids of [7.6.7](/7.6.7#sec-7.5)). Such non-crystallographic symmetry may still relate several copies of a molecule inside the crystal (10.11).

### 10.1.4. Crystal Systems, Point Groups and Bravais Lattices

The symmetry operations of a crystal form a **group**. Its rotational part, the set of matrices $R$ with the translations removed, is one of the $32$ crystallographic point groups (the finite point groups, [7.6.7](/7.6.7#def-7.4.1), whose rotations satisfy Theorem 10.1.1). The point group determines the macroscopic symmetry of the crystal and constrains the shape of the cell, which defines the seven **crystal systems**:

| Crystal system | Minimal symmetry | Cell constraints | Bravais lattices | Point groups without inversion or mirrors |
|---|---|---|---|---|
| triclinic | none | none | $P$ | $1$ |
| monoclinic | one $2$ axis | $\alpha = \gamma = 90^\circ$ | $P$, $C$ | $2$ |
| orthorhombic | three perpendicular $2$ axes | $\alpha = \beta = \gamma = 90^\circ$ | $P$, $C$, $I$, $F$ | $222$ |
| tetragonal | one $4$ axis | $a = b$; $\alpha = \beta = \gamma = 90^\circ$ | $P$, $I$ | $4$, $422$ |
| trigonal | one $3$ axis | $a = b$; $\alpha = \beta = 90^\circ$, $\gamma = 120^\circ$ (or rhombohedral) | $P$, $R$ | $3$, $32$ |
| hexagonal | one $6$ axis | $a = b$; $\alpha = \beta = 90^\circ$, $\gamma = 120^\circ$ | $P$ | $6$, $622$ |
| cubic | four $3$ axes along body diagonals | $a = b = c$; $\alpha = \beta = \gamma = 90^\circ$ | $P$, $I$, $F$ | $23$, $432$ |

The constraints are consequences of the symmetry, not its definition: a cell with $a = b$ by accident is not tetragonal unless the contents have a fourfold axis. The cell is conventionally chosen to display the symmetry, and sometimes this requires a centred cell with lattice points also at the centre of the cell ($I$), at the centre of one face ($C$), or at the centres of all faces ($F$). Combining the seven systems with the possible centrings gives the $14$ **Bravais lattices**.

### 10.1.5. Space Groups and the Asymmetric Unit

**Definition 10.1.1 (Space Group)** The **space group** of a crystal is the group of all isometries that map the crystal structure onto itself. It contains the lattice translations as a normal **subgroup**, and its quotient by them is isomorphic to the crystal's point group. There are $230$ space groups in three dimensions, listed with their symmetry operations, equivalent positions and conditions for reflections in the International Tables for Crystallography, Volume A.

**Definition 10.1.2 (Asymmetric Unit)** The **asymmetric unit** of a crystal is a smallest part of the unit cell from which the whole cell is generated by the operations of the space group. Its contents (one or several molecules, or part of a molecule lying on a symmetry axis) are all that a crystallographer has to determine.

The international (Hermann–Mauguin) symbol of a space group gives the lattice type followed by the symmetry along the principal directions: $P2_1$ is a primitive monoclinic lattice with a $2_1$ axis along $\boldsymbol{b}$ (two equivalent positions, $(x, y, z)$ and $(-x, y + \frac12, -z)$); $C2$ adds $C$ centring (four positions); $P2_12_12_1$ has three mutually perpendicular, non-intersecting $2_1$ axes (four positions). The number of molecules in the unit cell is $Z = n_{\mathrm{asu}}\times(\text{number of equivalent positions})$, where $n_{\mathrm{asu}}$ is the number in the asymmetric unit.

Biological macromolecules are chiral: proteins are made of L-amino acids and nucleic acids of D-sugars, and the mirror image of a protein is a different molecule (**chirality**). Mirror planes, glide planes, inversion centres and rotoinversions map a molecule onto its **enantiomer** and so cannot relate two molecules of a natural protein. Only the $65$ space groups whose operations are all proper (rotations, screw rotations and translations; the Sohncke groups) are possible for crystals of natural macromolecules, with the $11$ point groups of the last column of the table above. The most common are $P2_12_12_1$, $P2_1$, $C2$, $P2_12_12$, $C222_1$ and tetragonal and trigonal groups such as $P4_32_12$ and $P3_221$. As noted in [7.6.7](/7.6.7#sec-7.4.1), racemic mixtures of a synthetic protein and its D-enantiomer can use all $230$ groups.

The fraction of the crystal occupied by protein is estimated from the cell volume and the molar mass before the structure is known.

**Formula 10.1.1 (Matthews Coefficient)** For a crystal with cell volume $V$ containing $Z$ molecules of molar mass $M$ (in daltons), the Matthews coefficient and the solvent fraction are

$$
V_{\mathrm{M}} = \frac{V}{ZM}, \qquad f_{\mathrm{solv}} = 1 - \frac{1.23\,\text{Å}^3\,\mathrm{Da^{-1}}}{V_{\mathrm{M}}},
$$
where $1.23\,\text{Å}^3\,\mathrm{Da}^{-1}$ is the specific volume of protein ($\bar v = 0.74\,\mathrm{cm^3\,g^{-1}}$ divided by $N_{\mathrm{A}}$). Protein crystals have $V_{\mathrm{M}} = 1.6$–$3.5\,\text{Å}^3\,\mathrm{Da}^{-1}$, most often about $2.4$, that is, $30$–$65\,\%$ solvent (about $50\,\%$ on average).

**Example 10.1.1 (Lysozyme)** Hen egg-white lysozyme ($M = 14.3\,\mathrm{kDa}$) crystallizes in $P4_32_12$ with $a = b = 79.1\,\text{Å}$, $c = 37.9\,\text{Å}$, so $V = 2.37\times10^5\,\text{Å}^3$. The space group has eight equivalent positions. With one molecule per asymmetric unit, $Z = 8$, $V_{\mathrm{M}} = 2.07\,\text{Å}^3\,\mathrm{Da}^{-1}$ and $f_{\mathrm{solv}} = 0.41$; two molecules per asymmetric unit would give $V_{\mathrm{M}} = 1.04$, which is impossibly dense. The solvent channels, about $40\,\%$ of the volume here, are what allow small molecules (substrates, inhibitors, heavy-atom reagents) to be soaked into protein crystals, and they explain why crystallized enzymes are usually active.

## 10.2. The Geometry of Diffraction

### 10.2.1. The Laue Equations

Let a plane wave of wavelength $\lambda$ travel in the direction of the unit vector $\boldsymbol{s}_0$ and be scattered elastically in the direction $\boldsymbol{s}$ by two identical scatterers at $\boldsymbol{0}$ and $\boldsymbol{r}$. The path difference between the two scattered waves is $\boldsymbol{r}\cdot(\boldsymbol{s} - \boldsymbol{s}_0)$, so their phase difference is $2\pi\boldsymbol{r}\cdot\boldsymbol{S}$ with the scattering vector

$$
\boldsymbol{S} = \frac{\boldsymbol{s} - \boldsymbol{s}_0}{\lambda}, \qquad \lvert\boldsymbol{S}\rvert = \frac{2\sin\theta}{\lambda},
$$
where $2\theta$ is the scattering angle (crystallographers call $\theta$ the Bragg angle). This is the **scattering vector** of [7.6.9](/7.6.9#def-9.1.2) in crystallographic units: $\boldsymbol{q} = 2\pi\boldsymbol{S}$.

**Theorem 10.2.1 (Laue Equations)** The waves scattered by all points of the lattice generated by $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ are in phase if and only if

$$
\boldsymbol{a}\cdot\boldsymbol{S} = h, \qquad \boldsymbol{b}\cdot\boldsymbol{S} = k, \qquad \boldsymbol{c}\cdot\boldsymbol{S} = l, \qquad h, k, l \in \mathbb{Z}. \tag{10.1}
$$

The equations (Laue, 1912) follow from requiring the phase difference $2\pi\boldsymbol{t}\cdot\boldsymbol{S}$ to be a multiple of $2\pi$ for every lattice vector $\boldsymbol{t} = m\boldsymbol{a} + n\boldsymbol{b} + p\boldsymbol{c}$. Each equation alone describes a family of cones around one lattice direction (the diffraction of a one-dimensional row of scatterers, a grating); the three conditions together are met only along the lines where three cones intersect, so a crystal diffracts into discrete directions. The integers $h, k, l$ are the indices of the reflection.

### 10.2.2. The Reciprocal Lattice

The Laue equations are solved by introducing a second lattice.

**Definition 10.2.1 (Reciprocal Lattice)** The **reciprocal lattice** of the lattice with basis $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ and cell volume $V$ is the lattice generated by

$$
\boldsymbol{a}^* = \frac{\boldsymbol{b}\times\boldsymbol{c}}{V}, \qquad \boldsymbol{b}^* = \frac{\boldsymbol{c}\times\boldsymbol{a}}{V}, \qquad \boldsymbol{c}^* = \frac{\boldsymbol{a}\times\boldsymbol{b}}{V}.
$$
Its points are $\boldsymbol{H} = h\boldsymbol{a}^* + k\boldsymbol{b}^* + l\boldsymbol{c}^*$ with integers $h, k, l$, and its cell has volume $V^* = 1/V$.

By construction $\boldsymbol{a}\cdot\boldsymbol{a}^* = 1$, $\boldsymbol{a}\cdot\boldsymbol{b}^* = \boldsymbol{a}\cdot\boldsymbol{c}^* = 0$, and so on: the two bases are dual. Hence $\boldsymbol{a}\cdot\boldsymbol{H} = h$, and the Laue equations (10.1) say exactly that

$$
\boldsymbol{S} = \boldsymbol{H}_{hkl}: \tag{10.2}
$$
diffraction occurs when the scattering vector equals a vector of the reciprocal lattice (the Laue condition). For orthogonal axes, $a^* = 1/a$, $b^* = 1/b$, $c^* = 1/c$; in general $a^* = bc\sin\alpha/V$. In physics the reciprocal lattice is usually defined with an extra factor $2\pi$, matching $\boldsymbol{q} = 2\pi\boldsymbol{S}$.

The reciprocal lattice also describes the lattice planes. A **family of lattice planes** ([5.4.2](/5.4.2#def-2.5.1)) with Miller indices $(hkl)$ is the set of parallel, equally spaced planes of which the first from the origin cuts the axes at $\boldsymbol{a}/h$, $\boldsymbol{b}/k$, $\boldsymbol{c}/l$ (for coprime $h, k, l$; an index $0$ means the plane is parallel to that axis).

**Proposition 10.2.1 (Reciprocal Vectors and Lattice Planes)** The reciprocal-lattice vector $\boldsymbol{H}_{hkl}$ is perpendicular to the planes $(hkl)$, and its length is the reciprocal of their spacing: $\lvert\boldsymbol{H}_{hkl}\rvert = 1/d_{hkl}$.

**Proof** The vectors $\boldsymbol{a}/h - \boldsymbol{b}/k$ and $\boldsymbol{a}/h - \boldsymbol{c}/l$ lie in the plane; their scalar products with $\boldsymbol{H}$ are $1 - 1 = 0$, so $\boldsymbol{H}$ is normal to it. The spacing is the distance of the plane from the origin, the projection of $\boldsymbol{a}/h$ onto the unit normal: $d = (\boldsymbol{a}/h)\cdot\boldsymbol{H}/\lvert\boldsymbol{H}\rvert = 1/\lvert\boldsymbol{H}\rvert$. $\square$

For an orthogonal cell this gives

$$
\frac{1}{d_{hkl}^2} = \frac{h^2}{a^2} + \frac{k^2}{b^2} + \frac{l^2}{c^2}.
$$
Indices with a common factor, such as $(220)$, belong to planes parallel to $(110)$ at half the spacing; they describe the second-order reflection from $(110)$, and in crystallography all integer triples are used as reflection indices.

### 10.2.3. Bragg's Law

**Theorem 10.2.2 (Bragg's Law)** A crystal gives a diffracted beam from the planes $(hkl)$ when the glancing angle $\theta$ between the incident beam and the planes satisfies

$$
2d_{hkl}\sin\theta = \lambda, \tag{10.3}
$$
and the diffracted beam leaves at the same angle $\theta$ on the other side of the planes, as if reflected by them.

**Proof** By Eq. (10.2), $\boldsymbol{S} = \boldsymbol{H}_{hkl}$. Since $\lvert\boldsymbol{s}\rvert = \lvert\boldsymbol{s}_0\rvert = 1$, the vector $\boldsymbol{s} - \boldsymbol{s}_0$ bisects the angle between $-\boldsymbol{s}_0$ and $\boldsymbol{s}$ and is perpendicular to the mirror plane between them; its length is $2\sin\theta$. Hence the planes perpendicular to $\boldsymbol{H}$ act as mirrors, and $2\sin\theta/\lambda = \lvert\boldsymbol{H}\rvert = 1/d_{hkl}$ by Proposition 10.2.1. $\square$

W. L. Bragg derived the law in 1913 by treating the planes as weakly reflecting mirrors (the form $2d\sin\theta = n\lambda$ with order $n$, [5.4.2](/5.4.2#sec-2.5.3)); here the order is absorbed into the indices, since the $n$-th order from $(hkl)$ is the first order from $(nh\,nk\,nl)$. With his father, W. H. Bragg, he used it to solve the structures of $\ce{NaCl}$, $\ce{KCl}$ and diamond, the beginning of structural crystallography (Nobel Prize in Physics 1915).

Since $\sin\theta \le 1$, only planes with $d \ge \lambda/2$ can diffract. The spacing $d$ of the planes that give a reflection is called its resolution, and the smallest spacing $d_{\min}$ in a data set is the resolution of the data; the electron density computed from them shows details of about that size (10.3.5).

**Example 10.2.1 (Diffraction Angles)** With copper $\mathrm{K}\alpha$ radiation ($\lambda = 1.5418\,\text{Å}$), a reflection at $d = 2.0\,\text{Å}$ is observed at $2\theta = 2\arcsin(\lambda/2d) = 45.3^\circ$; with synchrotron radiation of $\lambda = 1.0\,\text{Å}$ the same reflection lies at $2\theta = 28.9^\circ$. For a cell edge of $79\,\text{Å}$, the first reflection along that axis ($d = 79\,\text{Å}$) lies at $2\theta = 0.73^\circ$ (at $\lambda = 1.0\,\text{Å}$): protein crystals give many reflections close to the beam, and the beam stop and detector distance must be chosen accordingly.

### 10.2.4. The Ewald Sphere

**Definition 10.2.2 (Ewald Sphere)** The **Ewald sphere** is the sphere of radius $1/\lambda$ in reciprocal space whose centre lies at $-\boldsymbol{s}_0/\lambda$ from the origin of the reciprocal lattice, so that it passes through the origin. A reflection $hkl$ is in diffracting position when the reciprocal-lattice point $\boldsymbol{H}_{hkl}$ lies on the sphere; the diffracted beam then runs from the centre of the sphere (the crystal) through that point.

The construction (Ewald, 1913) is Eq. (10.2) drawn as geometry: $\boldsymbol{S} = \boldsymbol{s}/\lambda - \boldsymbol{s}_0/\lambda$ is the difference between two vectors of length $1/\lambda$ that start at the centre, so the tip of $\boldsymbol{S}$ lies on the sphere. Rotating the crystal rotates its reciprocal lattice about the origin, and points pass through the sphere one after another. All points within the limiting sphere of radius $2/\lambda$ about the origin can be brought into diffraction, which is again $d \ge \lambda/2$. The number of reflections to resolution $d_{\min}$ is the number of reciprocal-lattice points in a sphere of radius $1/d_{\min}$:

$$
N(d_{\min}) \approx \frac{4\pi}{3}\,\frac{V}{d_{\min}^3}. \tag{10.4}
$$

![Diffraction geometry in two dimensions. (A) An oblique real lattice with its unit cell (shaded) and the family of lattice planes (1 1), spacing $d_{11}$. (B) The reciprocal lattice: $\boldsymbol{a}^*$ is perpendicular to $\boldsymbol{b}$ and $\boldsymbol{b}^*$ to $\boldsymbol{a}$, and the reciprocal vector $\boldsymbol{H}_{11}$ is perpendicular to the planes (1 1) with length $1/d_{11}$. (C) The Ewald construction: the crystal sits at C, the incident wave vector $\boldsymbol{s}_0/\lambda$ ends at the reciprocal origin O, and the sphere of radius $1/\lambda$ through O is drawn. The crystal is oriented so that the reciprocal point (2, 1) lies on the sphere (circled); the diffracted beam $\boldsymbol{s}/\lambda$ runs from C through it, and $\boldsymbol{H}_{21} = \boldsymbol{s}/\lambda - \boldsymbol{s}_0/\lambda$. All points inside the dotted limiting sphere of radius $2/\lambda$ can be brought onto the Ewald sphere by rotating the crystal.](./plots/ewald.py)

**Example 10.2.2 (How Many Reflections?)** For the lysozyme cell of Example 10.1.1 ($V = 2.37\times10^5\,\text{Å}^3$), Eq. (10.4) gives $1.24\times10^5$ reciprocal-lattice points to $2.0\,\text{Å}$ resolution. Symmetry makes many of them equivalent: the point group $422$ has $8$ operations, and Friedel's law (10.3.6) doubles this, so about $1.24\times10^5/16 \approx 7800$ unique reflections must be measured. At $3.0\,\text{Å}$ there are about $2300$, at $1.5\,\text{Å}$ about $18\,000$. The number grows as $d_{\min}^{-3}$, and so does the information about the structure.

### 10.2.5. The Laue Method and the Rotation Method

There are two ways of bringing many reciprocal-lattice points onto the Ewald sphere. In the Laue method, used in the first experiment of 1912, the crystal is stationary and illuminated with a continuous spectrum from $\lambda_{\min}$ to $\lambda_{\max}$; each wavelength has its own sphere, and every point between the spheres of radii $1/\lambda_{\max}$ and $1/\lambda_{\min}$ (and within the resolution limit) diffracts simultaneously. A single short exposure records a large fraction of the reflections, which is the reason the Laue method returned for time-resolved studies at synchrotrons (10.13), but the overlap of orders and the wavelength dependence of each spot make the analysis complicated.

The standard method for macromolecules is the monochromatic rotation method: the crystal is rotated at constant speed about an axis perpendicular to the beam, and the detector records a frame every $0.05$–$1^\circ$. Each reflection is recorded as it passes through the sphere, and a rotation of $90$–$360^\circ$ (depending on symmetry, 10.7.3) measures every unique reflection at least once. Since the cell of a protein is large and its reciprocal lattice dense, every frame contains hundreds of reflections, arranged in lunes, each lune being the intersection of one plane of the reciprocal lattice with the sphere during the rotation.

## 10.3. Diffraction Intensities and the Electron Density

### 10.3.1. Scattering by an Electron and by an Atom

X-rays are scattered by electrons. A free electron in the oscillating field of the beam is accelerated and radiates as a dipole ([5.3.10](/5.3.10#sec-10.4.2)); the scattered intensity at distance $r$ from an electron illuminated by an unpolarized beam of intensity $I_0$ is given by the Thomson formula,

$$
I = I_0\,\frac{r_{\mathrm{e}}^2}{r^2}\,\frac{1 + \cos^2 2\theta}{2}, \qquad r_{\mathrm{e}} = \frac{{e}^2}{4\pi\varepsilon_0 m_{\mathrm{e}}c^2} = 2.818\times10^{-15}\,\mathrm{m},
$$
where $(1 + \cos^2 2\theta)/2$ is the polarization factor (for the horizontally polarized beam of a synchrotron it is different and depends on the direction). Nuclei also scatter, but the scattered amplitude is inversely proportional to the mass of the particle, so a proton contributes $(m_{\mathrm{e}}/m_{\mathrm{p}})^2 = 3\times10^{-7}$ of the intensity of an electron, and the X-ray picture of a molecule is a picture of its electrons. Hydrogen atoms, with one electron each, are correspondingly faint.

The electrons of an atom are spread over a volume comparable to the wavelength, so the waves they scatter interfere.

**Definition 10.3.1 (Atomic Scattering Factor)** The **atomic scattering factor** $f(S)$ of an atom is the amplitude it scatters, in units of the amplitude scattered by one free electron. For a spherically symmetric electron density $\rho_{\mathrm{at}}(r)$,

$$
f(S) = \int_0^\infty 4\pi r^2\rho_{\mathrm{at}}(r)\,\frac{\sin 2\pi Sr}{2\pi Sr}\,\mathrm{d}r,
$$
a decreasing function of $S = 2\sin\theta/\lambda$ with $f(0) = Z$, the number of electrons.

The scattering factor is the Fourier transform of the atom's density, averaged over directions (compare the Debye formula, [7.6.9](/7.6.9#thm-9.3.1)). For carbon it falls from $6$ at $S = 0$ to about $1.7$ at $d = 1\,\text{Å}$. Tabulated values are fitted by sums of Gaussians, $f(s) = \sum_{i=1}^4 a_i\mathrm{e}^{-b_is^2} + c$ with $s = \sin\theta/\lambda$ (Cromer–Mann coefficients); the figure in 10.8.3 uses them. Near an absorption edge the electrons can no longer be treated as free, and $f$ acquires wavelength-dependent real and imaginary corrections; this anomalous scattering is a tool for phasing (10.9.2).

### 10.3.2. The Crystal as a Convolution

A crystal is the convolution of the contents of one unit cell with the lattice. Writing the lattice as a sum of **Dirac delta functions**,

$$
\rho_{\mathrm{crystal}}(\boldsymbol{r}) = \rho_{\mathrm{cell}}(\boldsymbol{r}) * \sum_{m,n,p}\delta(\boldsymbol{r} - m\boldsymbol{a} - n\boldsymbol{b} - p\boldsymbol{c}).
$$
By the **convolution theorem** ([2.5.6](/2.5.6)), the scattered amplitude, the Fourier transform of $\rho_{\mathrm{crystal}}$, is the product of the transform of one cell and the transform of the lattice. The transform of an infinite lattice of delta functions is the reciprocal lattice of delta functions, $\frac{1}{V}\sum_{hkl}\delta(\boldsymbol{S} - \boldsymbol{H}_{hkl})$. The crystal therefore diffracts only at the reciprocal-lattice points, and there with the amplitude of the transform of one unit cell: the crystal samples the molecular transform.

For a finite crystal of $N_1\times N_2\times N_3$ cells the sum over the lattice is finite, and its transform is the product of three Laue interference functions,

$$
\left\lvert\sum_{m=0}^{N_1-1}\mathrm{e}^{2\pi\mathrm{i}m\boldsymbol{a}\cdot\boldsymbol{S}}\right\rvert^2 = \frac{\sin^2(\pi N_1\boldsymbol{a}\cdot\boldsymbol{S})}{\sin^2(\pi\boldsymbol{a}\cdot\boldsymbol{S})},
$$
which has maxima of height $N_1^2$ at integer $\boldsymbol{a}\cdot\boldsymbol{S}$ and width about $1/N_1$ in $\boldsymbol{a}\cdot\boldsymbol{S}$, the interference function of a grating with $N_1$ slits ([5.4.2](/5.4.2#sec-2.3)). The integrated intensity of a reflection, its peak height times its width in three dimensions, is proportional to $N_1N_2N_3$, the number of cells in the crystal. For a crystal of $1000$ cells along each edge, the width $10^{-3}$ is far smaller than the angular spread caused by the mosaic structure of real crystals, which consist of slightly misoriented blocks (mosaic spread $0.1$–$0.5^\circ$ for good cryocooled crystals). The size of the crystal therefore affects the strength of the diffraction, not the sharpness of the spots or the resolution, which is limited by disorder (10.3.5) and by the strength of the signal at high angle; only microcrystals of a few hundred cells give measurably broadened spots.

![The crystal transform samples the molecular transform. (A) A two-dimensional "molecule" of seven Gaussian atoms. (B) Its continuous transform $\lvert F(\boldsymbol{s})\rvert^2$ (logarithmic scale up to $\lvert\boldsymbol{s}\rvert = 0.25\,\text{Å}^{-1}$), which depends on the orientation and shape of the molecule. (C) A $9\times9$ patch of a crystal with the same molecule at every point of an oblique lattice ($a = 24\,\text{Å}$, $b = 22.2\,\text{Å}$, $\gamma = 71^\circ$). (D) The transform of the crystal: it vanishes except at the points of the reciprocal lattice, and the intensities of the spots follow the molecular transform of panel B. The spots are narrow because the crystal contains many cells; the lattice determines where the spots are, the molecule how strong they are.](./plots/molecular-transform.py)

### 10.3.3. The Structure Factor

**Definition 10.3.2 (Structure Factor)** The **structure factor** of the reflection $\boldsymbol{h} = (h, k, l)$ is the amplitude scattered by one unit cell, in units of the amplitude scattered by one electron:

$$
F(\boldsymbol{h}) = \sum_{j=1}^{N} f_j\,\mathrm{e}^{2\pi\mathrm{i}(hx_j + ky_j + lz_j)} = \int_{\text{cell}}\rho(\boldsymbol{r})\,\mathrm{e}^{2\pi\mathrm{i}\boldsymbol{H}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r}, \tag{10.5}
$$
where the sum runs over the atoms of the cell at fractional coordinates $(x_j, y_j, z_j)$ with scattering factors $f_j$, and $\rho$ is the electron density. It is a complex number, $F(\boldsymbol{h}) = \lvert F(\boldsymbol{h})\rvert\mathrm{e}^{\mathrm{i}\varphi(\boldsymbol{h})}$, with amplitude $\lvert F\rvert$ and phase $\varphi$.

The phase of each atomic term is $2\pi\boldsymbol{H}\cdot\boldsymbol{r}_j = 2\pi(hx_j + ky_j + lz_j)$, the phase difference of Theorem 10.2.1 between the atom and the origin; note that $\boldsymbol{H}\cdot\boldsymbol{r} = hx + ky + lz$ for fractional coordinates, because the bases are dual. The structure factor is the Fourier transform of the electron density of one cell, evaluated at the reciprocal-lattice points.

**Remark 10.3.1 (Sign Convention)** Crystallography writes the structure factor with $\mathrm{e}^{+2\pi\mathrm{i}\boldsymbol{H}\cdot\boldsymbol{r}}$ and the Fourier synthesis of the density with $\mathrm{e}^{-2\pi\mathrm{i}\boldsymbol{H}\cdot\boldsymbol{r}}$ (Eq. (10.6)), as in [7.1.6](/7.1.6#sec-6.6.1) and the International Tables. Solution scattering and physics usually use the opposite sign, $A(\boldsymbol{q}) = \int\rho\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r}$ ([7.6.9](/7.6.9#eq-9.8)), so that $F(\boldsymbol{h}) = A(-2\pi\boldsymbol{H}) = A(2\pi\boldsymbol{H})^*$ for a real density. The two conventions differ only by the sign of all phases, which leaves intensities unchanged and turns the structure into its mirror image if the conventions are mixed. What matters is that the transform and its inverse carry opposite signs; writing both with the same sign, as is sometimes seen, is an error.

The intensity of a reflection is proportional to $\lvert F(\boldsymbol{h})\rvert^2$. For a crystal of volume $V_x$ rotated with angular velocity $\omega$ through the reflecting position, the energy diffracted into the reflection is, in the kinematic approximation (weak scattering, no multiple scattering),

**Formula 10.3.1 (Integrated Intensity)**

$$
E(\boldsymbol{h}) = \frac{I_0}{\omega}\,r_{\mathrm{e}}^2\,\frac{\lambda^3V_x}{V^2}\,L\,p\,A\,\lvert F(\boldsymbol{h})\rvert^2,
$$
with the Lorentz factor $L$ (the time a reflection spends in diffracting position, $1/\sin 2\theta$ for a reflection in the plane perpendicular to the rotation axis), the polarization factor $p$ and the absorption factor $A$.

Two consequences are important for macromolecules. First, the intensity is proportional to the crystal volume and inversely proportional to the square of the cell volume. Since $\lvert F\rvert^2$ itself is on average proportional to the number of atoms in the cell, $\langle\lvert F\rvert^2\rangle = \sum_jf_j^2 \propto V$ (10.8.3), the average intensity per reflection scales as $V_x/V$: for crystals of the same size, a protein with a $100$ times larger cell than a small molecule gives reflections $100$ times weaker. Second, the factor $\lambda^3$ favours longer wavelengths, but absorption and radiation damage grow faster; wavelengths near $1\,\text{Å}$ are the usual compromise.

### 10.3.4. The Electron Density as a Fourier Series

The electron density of a crystal is periodic, so it is represented by a **Fourier series** ([2.5.6](/2.5.6)) whose coefficients are, by Eq. (10.5), the structure factors divided by the cell volume.

**Theorem 10.3.1 (Fourier Synthesis of the Electron Density)** The electron density at fractional position $(x, y, z)$ in the unit cell is

$$
\rho(x, y, z) = \frac{1}{V}\sum_{h,k,l}F(hkl)\,\mathrm{e}^{-2\pi\mathrm{i}(hx + ky + lz)} = \frac{1}{V}\sum_{h,k,l}\lvert F(hkl)\rvert\cos[2\pi(hx + ky + lz) - \varphi(hkl)], \tag{10.6}
$$
where the second form uses Friedel's law (10.3.6) to combine the terms $\boldsymbol{h}$ and $-\boldsymbol{h}$.

**Proof** Insert Eq. (10.5) into the right-hand side and use the orthogonality $\frac{1}{V}\int_{\text{cell}}\mathrm{e}^{2\pi\mathrm{i}(\boldsymbol{H} - \boldsymbol{H}')\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r} = \delta_{\boldsymbol{h}\boldsymbol{h}'}$ of the exponentials over one period; the sum becomes the Fourier series of the periodic function $\rho$, which converges to $\rho$ ([2.5.6](/2.5.6)). $\square$

Each reflection contributes a plane density wave, $\cos[2\pi\boldsymbol{H}\cdot\boldsymbol{r} - \varphi]$, with wavefronts parallel to the planes $(hkl)$, wavelength $d_{hkl}$, amplitude $\lvert F\rvert/V$ and a position fixed by the phase $\varphi$. The density is the superposition of all these waves. The amplitudes are measured; the phases, which say where the crests of each wave lie relative to the origin, are not. Without phases there is no density.

The importance of the phases is illustrated by combining the amplitudes of one structure with the phases of another: the result resembles the structure that supplied the phases. The amplitudes of a protein are, to a first approximation, determined by its composition (Wilson statistics, 10.8.3), while the phases carry the arrangement. This is also why a map computed with phases from a model tends to show that model, whether it is right or not (model bias, 10.10).

![Phases carry most of the structural information. (A) A ring-shaped two-dimensional molecule of Gaussian atoms and (B) a zigzag chain, each computed from its own amplitudes and phases. (C) The Fourier synthesis with the amplitudes of the ring and the phases of the chain resembles the chain; (D) the amplitudes of the chain with the phases of the ring resemble the ring. Negative density is not shown. Crystallographers' versions of this demonstration famously swap the photographs of two people.](./plots/phase-swap.py)

### 10.3.5. Resolution and the Temperature Factor

A data set measured to resolution $d_{\min}$ contains the terms of Eq. (10.6) with $\lvert\boldsymbol{H}\rvert \le 1/d_{\min}$. Truncating a Fourier series removes the waves shorter than $d_{\min}$ and blurs the density; features closer than about $0.7$–$0.9\,d_{\min}$ merge. At $3.5\,\text{Å}$ the density of a protein shows the path of the chain, α helices as rods and β sheets as slabs, and large side chains as bumps; at $2.5\,\text{Å}$ most side chains have recognizable shapes, and carbonyl groups appear as bulges on the main chain; at $1.5\,\text{Å}$ individual atoms begin to separate; below $1.2\,\text{Å}$ (atomic resolution) all non-hydrogen atoms are resolved and some hydrogen atoms are visible in difference maps ([7.1.6](/7.1.6#sec-6.6.1)). A truncated series also produces ripples around strong peaks, which is why heavy atoms are surrounded by rings in low-resolution maps.

![Resolution in a two-dimensional Fourier synthesis. A tyrosine-like fragment (ring carbons $1.39\,\text{Å}$ apart, a hydroxyl oxygen, a $\mathrm{C}_\beta$, $\mathrm{C}_\alpha$ and N; grey circles mark the true positions) in a periodic cell of $16\times16\,\text{Å}$, computed from its structure factors with $B = 8\,\text{Å}^2$ and truncated at $d_{\min} = 3.5$, $2.5$, $1.5$ and $1.0\,\text{Å}$. At $3.5\,\text{Å}$ the side chain is one featureless blob; at $2.5\,\text{Å}$ the ring is a flat disc with a hint of the hole; at $1.5\,\text{Å}$ the hole in the ring and the hydroxyl are clear; at $1.0\,\text{Å}$ every atom is a separate peak.](./plots/resolution.py)

Atoms in a crystal are not at rest. Thermal vibration and static disorder (slightly different positions in different unit cells) spread each atom over a small volume, and the crystal averages over all cells. If the displacement $\boldsymbol{u}$ of an atom from its mean position is Gaussian with mean square $\langle u^2\rangle$ in each direction, the averaged density is the convolution of the atom with a Gaussian, and its transform is multiplied by a Gaussian.

**Definition 10.3.3 (Temperature Factor)** The (isotropic) **temperature factor**, or **B-factor**, of an atom is the parameter $B$ in the attenuation of its scattering factor,

$$
f_j \to f_j\,\exp\left(-B_j\,\frac{\sin^2\theta}{\lambda^2}\right), \qquad B_j = 8\pi^2\langle u_j^2\rangle,
$$
where $\langle u_j^2\rangle$ is the mean square displacement of the atom along the scattering vector (the Debye–Waller factor). Anisotropic displacements are described by a $3\times3$ tensor $U$ (six parameters per atom) at high resolution.

Typical protein atoms have $B = 10$–$40\,\text{Å}^2$; $B = 20\,\text{Å}^2$ corresponds to an rms displacement of $\sqrt{20/8\pi^2} = 0.50\,\text{Å}$, and $B = 80\,\text{Å}^2$ (a mobile surface loop) to $1.0\,\text{Å}$. The B-factors of a refined model map flexibility: they are low in the core, high on the surface and at the termini, and high for side chains that point into the solvent. They also include static disorder and errors of the model, and they are correlated with occupancy, so they are interpreted cautiously. The overall falloff of intensity with resolution, which sets the resolution limit of a crystal, is governed by an average B-factor of the whole crystal (the Wilson B, 10.8.3).

### 10.3.6. Friedel's Law and the Symmetry of the Diffraction Pattern

**Theorem 10.3.2 (Friedel's Law)** If the atomic scattering factors are real, then $F(-\boldsymbol{h}) = F(\boldsymbol{h})^*$; hence $\lvert F(-\boldsymbol{h})\rvert = \lvert F(\boldsymbol{h})\rvert$ and $\varphi(-\boldsymbol{h}) = -\varphi(\boldsymbol{h})$, and the reflections $\boldsymbol{h}$ and $-\boldsymbol{h}$ (a Friedel pair) have equal intensities.

**Proof** Changing $\boldsymbol{h}$ to $-\boldsymbol{h}$ in Eq. (10.5) conjugates every term when all $f_j$ are real. $\square$

The diffraction pattern is therefore centrosymmetric even when the crystal is not. In addition, a rotation $R$ of the crystal's point group maps the reflection $\boldsymbol{h}$ to an equivalent reflection with the same amplitude: for an operation $\boldsymbol{x} \mapsto R\boldsymbol{x} + \boldsymbol{t}$, substitution in Eq. (10.5) gives $F(\boldsymbol{h}R) = F(\boldsymbol{h})\,\mathrm{e}^{-2\pi\mathrm{i}\boldsymbol{h}\cdot\boldsymbol{t}}$ ($\boldsymbol{h}$ written as a row vector). Equivalent reflections have equal amplitudes, and their phases differ by the known amount $2\pi\boldsymbol{h}\cdot\boldsymbol{t}$. The intensities thus have the symmetry of the point group plus an inversion centre: one of the $11$ centrosymmetric point groups, the Laue groups. For macromolecular crystals, whose point groups are the $11$ proper ones, the Laue group is obtained by adding the inversion ($222 \to mmm$, $422 \to 4/mmm$, and so on). The Laue group is determined from the data during processing (10.8.1).

Friedel's law fails when some atoms scatter anomalously, with complex $f$ (10.9.2). The small differences between $\lvert F(\boldsymbol{h})\rvert$ and $\lvert F(-\boldsymbol{h})\rvert$ (Bijvoet differences) then carry phase information, and they also allow the absolute configuration of a chiral molecule to be determined, as Bijvoet showed in 1951 for sodium rubidium tartrate.

Some reflections are related to themselves with a phase change by an operation that maps $\boldsymbol{h}$ to $-\boldsymbol{h}$. These centric reflections, for example $h0l$ in a monoclinic crystal with the twofold axis along $\boldsymbol{b}$, have phases restricted to two values ($0$ or $\pi$ when the operation has no translation along $\boldsymbol{h}$); their statistics differ (10.8.3), and they are especially useful in phasing.

### 10.3.7. Systematic Absences

Translations that are fractions of a lattice vector, from centring, screw axes and glide planes, make certain classes of reflections vanish identically. Consider $P2_1$ with the screw axis along $\boldsymbol{b}$: every atom at $(x, y, z)$ has a partner at $(-x, y + \frac12, -z)$. For the reflections $0k0$, the two contribute

$$
F(0k0) = \sum_{j=1}^{N/2}f_j\left(\mathrm{e}^{2\pi\mathrm{i}ky_j} + \mathrm{e}^{2\pi\mathrm{i}k(y_j + 1/2)}\right) = \left(1 + (-1)^k\right)\sum_{j=1}^{N/2}f_j\,\mathrm{e}^{2\pi\mathrm{i}ky_j},
$$
which is zero for every odd $k$, whatever the structure. Physically, the projection of the structure onto the $\boldsymbol{b}$ axis repeats every $b/2$, so only the even orders of the period $b$ survive. A twofold rotation axis in the same place gives no such absences.

| Symmetry element | Reflections affected | Condition for absence |
|---|---|---|
| $2_1$ along $\boldsymbol{a}$, $\boldsymbol{b}$ or $\boldsymbol{c}$ | $h00$, $0k0$, $00l$ | index odd |
| $4_2$ or $6_3$ along $\boldsymbol{c}$ | $00l$ | $l$ odd |
| $3_1$, $3_2$, $6_2$, $6_4$ along $\boldsymbol{c}$ | $00l$ | $l$ not a multiple of $3$ |
| $4_1$, $4_3$ along $\boldsymbol{c}$ | $00l$ | $l$ not a multiple of $4$ |
| $6_1$, $6_5$ along $\boldsymbol{c}$ | $00l$ | $l$ not a multiple of $6$ |
| $C$ centring | $hkl$ | $h + k$ odd |
| $I$ centring | $hkl$ | $h + k + l$ odd |
| $F$ centring | $hkl$ | $h, k, l$ of mixed parity |

The Laue group and the absences together narrow down the space group, but not always uniquely: enantiomorphic pairs such as $P4_1$ and $P4_3$, or $P3_121$ and $P3_221$, have identical absences and intensities, and the correct one is found only when the structure is solved (or from anomalous differences).

![Systematic absences reveal screw axes. (A) A $P2_1$ crystal viewed along $\boldsymbol{a}$: every three-atom motif at $(x, y, z)$ (filled) has a partner at $(-x, y + \frac12, -z)$ (open), generated by the $2_1$ screw axes along $\boldsymbol{b}$ (dash-dotted lines at $z = 0$ and $z = \frac12$). (B) Intensities of the axial reflections $0k0$ computed for 30 random atoms and their partners in $P2$ (grey) and $P2_1$ (purple) with the same coordinates. In $P2_1$ every reflection with odd $k$ (crosses) is exactly zero, and the even ones are the same in both groups.](./plots/absences.py)

## 10.4. The Phase Problem and the Patterson Function

### 10.4.1. Why the Phases Are Lost

A detector counts photons; it measures the time-averaged intensity $\lvert F\rvert^2$ and is blind to the phase of a wave that oscillates at $10^{18}\,\mathrm{Hz}$. In a light microscope the phases are not measured either, but they are never lost: the objective lens collects the diffracted waves and recombines them in the image plane with their phases intact. In Abbe's theory of image formation the back focal plane of the lens contains the Fourier transform of the object and the image plane its inverse transform. For X-rays the refractive index of all materials differs from $1$ by only $10^{-5}$–$10^{-6}$, there is no practical lens of atomic resolution, and the second Fourier transform has to be computed. It needs the phases of the waves that arrive at the detector, and those are exactly what is not recorded. This is the **phase problem** ([7.1.6](/7.1.6#sec-6.6.1)). It is not a technical limitation of detectors but a loss of information: the intensities $\lvert F(\boldsymbol{h})\rvert^2$ determine the autocorrelation of the density (Theorem 10.4.1), not the density itself.

The phase problem is solved by bringing in information other than the intensities: that the density is made of atoms (direct methods, 10.4.3), that a few heavy atoms can be located first (10.9.1), that some atoms scatter differently at different wavelengths (10.9.2), that a similar structure is known or can be predicted (10.10), and that the density is positive, flat in the solvent and repeated by non-crystallographic symmetry (10.11).

### 10.4.2. The Patterson Function

In 1934 A. L. Patterson asked what can be computed from the intensities alone, without phases.

**Definition 10.4.1 (Patterson Function)** The **Patterson function** of a crystal is the Fourier synthesis with the intensities as coefficients and all phases zero,

$$
P(\boldsymbol{u}) = \frac{1}{V}\sum_{\boldsymbol{h}}\lvert F(\boldsymbol{h})\rvert^2\cos(2\pi\boldsymbol{h}\cdot\boldsymbol{u}),
$$
a function of a vector $\boldsymbol{u} = (u, v, w)$ in the unit cell.

**Theorem 10.4.1 (Patterson Function as Autocorrelation)** The Patterson function is the autocorrelation of the electron density,

$$
P(\boldsymbol{u}) = \int_{\text{cell}}\rho(\boldsymbol{r})\,\rho(\boldsymbol{r} + \boldsymbol{u})\,\mathrm{d}^3\boldsymbol{r}.
$$
For point-like atoms it has a peak at every interatomic vector $\boldsymbol{r}_j - \boldsymbol{r}_k$, with height proportional to $Z_jZ_k$.

**Proof** Substitute the Fourier series (10.6) for both densities and integrate over the cell; orthogonality leaves $\frac{1}{V}\sum_{\boldsymbol{h}}F(\boldsymbol{h})F(\boldsymbol{h})^*\mathrm{e}^{-2\pi\mathrm{i}\boldsymbol{h}\cdot\boldsymbol{u}}$, and Friedel's law turns the exponential into the cosine. This is the Wiener–Khinchin relation: the transform of a power spectrum is an autocorrelation. $\square$

The Patterson function has the following properties, all visible in the figure below.

- It is centrosymmetric ($\boldsymbol{u}$ and $-\boldsymbol{u}$ correspond to the pairs $jk$ and $kj$) and has a large origin peak from all self-vectors $\boldsymbol{r}_j - \boldsymbol{r}_j$.
- For $N$ atoms in the cell it has $N(N-1)$ non-origin peaks, which are broader than atoms (each is a convolution of two atoms). For a protein with $N \approx 10^4$ atoms the $10^8$ peaks overlap completely, and the Patterson map is a smooth function with no resolved peaks; for a small molecule or a few heavy atoms it can be interpreted.
- Peaks between heavy atoms dominate, since their heights grow as $Z_jZ_k$: a mercury–mercury vector ($80\times80$) is $180$ times higher than a carbon–carbon vector ($6\times6$).
- Symmetry produces Harker peaks. In $P2_1$ an atom at $(x, y, z)$ and its partner at $(-x, y + \frac12, -z)$ give a vector $(2x, \frac12, 2z)$, so the self-vectors of all atoms between symmetry mates lie in the Harker section $v = \frac12$, from which $x$ and $z$ of a heavy atom are read off directly.

![The Patterson function. (A) Three atoms ($Z = 30$, $16$, $8$) in a two-dimensional cell of $20\times20\,\text{Å}$ (plane group $p1$). (B) Their Patterson function computed from the intensities alone: six cross peaks at the interatomic vectors $\boldsymbol{r}_j - \boldsymbol{r}_k$ (labelled $jk$), with heights proportional to $Z_jZ_k$, arranged centrosymmetrically, and the origin peak at the corners. (C) A heavy atom ($Z = 80$) and 40 light atoms in plane group $p2$, where each atom at $\boldsymbol{r}$ has a partner at $-\boldsymbol{r}$: the Patterson is dominated by the heavy-atom vector $2\boldsymbol{r}_{\mathrm{H}}$ (circled, and its centrosymmetric mate), from which the heavy-atom position follows, above a background of overlapping light-atom vectors. The mean intensity is subtracted before the synthesis to lower the origin peak.](./plots/patterson.py)

The heavy-atom method exploits the last two properties: find the heavy atom from the Patterson map, compute the structure factors of the heavy atom alone, use their phases as approximations to the phases of the whole structure, compute a density map, find more atoms, and iterate. Dorothy Hodgkin solved the structures of penicillin (1945) and vitamin $\mathrm{B}_{12}$ (1956, with a cobalt atom) in this way (Nobel Prize in Chemistry 1964). For proteins the heavy atom is far too weak to phase the whole structure directly, but the same idea, applied to differences between data sets, is the basis of isomorphous replacement (10.9.1).

### 10.4.3. Direct Methods

For crystals of small molecules the phase problem is solved routinely by direct methods, which derive phase relations from two facts about the density: it is non-negative, and it is made of discrete, similar atoms. The structure factors are first normalized, $E(\boldsymbol{h}) = F(\boldsymbol{h})/\sqrt{\varepsilon\sum_jf_j^2}$ ($\varepsilon$ a symmetry factor), which removes the falloff with resolution and makes $\langle\lvert E\rvert^2\rangle = 1$, as if the atoms were points.

**Theorem 10.4.2 (Sayre Equation)** For a structure of $N$ identical, resolved atoms, the density $\rho^2$ consists of the same atoms with a different shape, and its structure factors are proportional to those of $\rho$. By the convolution theorem,

$$
F(\boldsymbol{h}) = \frac{\vartheta(\boldsymbol{h})}{V}\sum_{\boldsymbol{k}}F(\boldsymbol{k})\,F(\boldsymbol{h} - \boldsymbol{k}),
$$
where $\vartheta$ is the ratio of the scattering factors of an atom and of its square.

When $\lvert E(\boldsymbol{h})\rvert$, $\lvert E(\boldsymbol{k})\rvert$ and $\lvert E(\boldsymbol{h} - \boldsymbol{k})\rvert$ are all large, the largest terms of the sum dominate, and the phases satisfy the triplet relation $\varphi(\boldsymbol{h}) \approx \varphi(\boldsymbol{k}) + \varphi(\boldsymbol{h} - \boldsymbol{k})$. Cochran showed that the triplet invariant $\Phi = \varphi(\boldsymbol{h}) - \varphi(\boldsymbol{k}) - \varphi(\boldsymbol{h} - \boldsymbol{k})$ has the distribution $P(\Phi) \propto \exp(\kappa\cos\Phi)$ with

$$
\kappa = \frac{2}{\sqrt N}\,\lvert E(\boldsymbol{h})E(\boldsymbol{k})E(\boldsymbol{h} - \boldsymbol{k})\rvert,
$$
so the relation is reliable only for strong reflections and becomes useless as $N$ grows. Combining many triplets gives the tangent formula of Karle and Hauptman,

$$
\tan\varphi(\boldsymbol{h}) \approx \frac{\sum_{\boldsymbol{k}}\lvert E(\boldsymbol{k})E(\boldsymbol{h} - \boldsymbol{k})\rvert\sin[\varphi(\boldsymbol{k}) + \varphi(\boldsymbol{h} - \boldsymbol{k})]}{\sum_{\boldsymbol{k}}\lvert E(\boldsymbol{k})E(\boldsymbol{h} - \boldsymbol{k})\rvert\cos[\varphi(\boldsymbol{k}) + \varphi(\boldsymbol{h} - \boldsymbol{k})]},
$$
which propagates a few starting phases (some fixed by the choice of origin, the others tried as many random sets) to all strong reflections. With modern dual-space algorithms, which alternate phase refinement in reciprocal space with peak picking in real space (SHELXD, "shake-and-bake"), direct methods solve structures of up to $1000$–$2000$ atoms if the data extend to atomic resolution ($\lesssim 1.2\,\text{Å}$). Hauptman and Karle received the Nobel Prize in Chemistry in 1985. Proteins are too large and rarely diffract that far, but direct methods are used to locate the substructure of heavy or anomalous atoms (tens to a few hundred sites) from difference data, which is a small-molecule problem (10.9).

## 10.5. Fiber Diffraction of Helices

### 10.5.1. Fibers and Layer Lines

Long helical molecules that do not crystallize, such as DNA, fibrous proteins and filamentous viruses, can often be aligned in a fiber: a bundle in which the molecules are parallel to the fiber axis but randomly rotated about it. The diffraction pattern of a fiber is the transform of one molecule averaged over rotations about its axis, a cylindrically averaged transform. It is recorded in cylindrical coordinates $(R, \psi, Z)$ of reciprocal space, with $Z$ along the fiber axis (the meridian) and $R$ perpendicular to it (the equator).

**Definition 10.5.1 (Fiber Diffraction)** **Fiber diffraction** is the diffraction of X-rays (or neutrons) by an assembly of molecules aligned along a common axis and randomly oriented about it. For molecules with a repeat distance $c$ along the axis, the intensity is confined to layer lines $Z = l/c$ ($l \in \mathbb{Z}$), and along each layer line it varies continuously with $R$.

The layer lines arise for the same reason as reciprocal-lattice points (10.3.2): the molecule is periodic in one dimension, and its transform is sampled at the reciprocal of that period. In the other two dimensions there is no lattice, so the intensity along a layer line is continuous; partially crystalline fibers add sampling along $R$ as well.

### 10.5.2. The Transform of a Helix

The transform of a helix was worked out by Cochran, Crick and Vand in 1952, in time for both the α helix and DNA.

**Theorem 10.5.1 (Cochran–Crick–Vand)** (a) A continuous helical wire of radius $r$ and pitch $P$, $\boldsymbol{r}(t) = (r\cos 2\pi t, r\sin 2\pi t, Pt)$, has a transform that is non-zero only on the layer lines $Z = n/P$, and on the $n$-th layer line

$$
F(R, \psi, n/P) = J_n(2\pi Rr)\,\mathrm{e}^{\mathrm{i}n(\psi + \pi/2)},
$$
where $J_n$ is the **Bessel function** of the first kind of order $n$ ([2.5](/2.5)).

(b) A discontinuous helix of point scatterers with $u$ units in $v$ turns (rise $p = vP/u$ per unit, repeat $c = vP$) has non-zero transform on the layer lines $Z = l/c$, and on layer line $l$ only the Bessel orders $n$ allowed by the selection rule

$$
l = vn + um, \qquad m \in \mathbb{Z},
$$
contribute, each with amplitude proportional to $J_n(2\pi Rr)$. For an integral helix ($v = 1$), $l = n + um$.

**Proof** (a) In cylindrical coordinates $\boldsymbol{S}\cdot\boldsymbol{r}(t) = Rr\cos(2\pi t - \psi) + ZPt$. Summed over many turns, the transform $\int\exp[2\pi\mathrm{i}\boldsymbol{S}\cdot\boldsymbol{r}(t)]\,\mathrm{d}t$ vanishes unless $ZP = n$ is an integer, which gives the layer lines; on them it equals the integral over one turn. The Jacobi–Anger expansion $\mathrm{e}^{\mathrm{i}x\cos\alpha} = \sum_m\mathrm{i}^mJ_m(x)\mathrm{e}^{\mathrm{i}m\alpha}$ with $x = 2\pi Rr$, $\alpha = 2\pi t - \psi$ turns the integrand into $\sum_m\mathrm{i}^mJ_m(x)\mathrm{e}^{-\mathrm{i}m\psi}\mathrm{e}^{2\pi\mathrm{i}(m + n)t}$, and integration over $t \in [0, 1]$ keeps only $m = -n$: $F = \mathrm{i}^{-n}J_{-n}(x)\mathrm{e}^{\mathrm{i}n\psi} = \mathrm{i}^nJ_n(x)\mathrm{e}^{\mathrm{i}n\psi}$, using $J_{-n} = (-1)^nJ_n$. (b) Sampling the continuous helix at points spaced by $1/u$ of a turn multiplies it by a one-dimensional lattice along the axis with period $p$, whose transform is a set of planes $Z = m/p$; the convolution shifts the layer lines of (a) by $m/p$, and $Z = n/P + m/p$ is the selection rule. $\square$

Two features make the transform easy to read. The first maximum of $J_n(x)$ lies at $x \approx n + 0.8n^{1/3}$ ($1.84$, $3.05$, $4.20$ for $n = 1, 2, 3$), so the strongest intensity on layer line $n$ moves outward in proportion to $n$: the pattern is a cross whose arms are, for large $n$, perpendicular to the strands of the helix. And $J_0$ is the only Bessel function that is non-zero at $R = 0$, so a meridional reflection appears only on the layer lines with $n = 0$ allowed, that is, at $Z = m/p$: it gives the rise per unit directly.

### 10.5.3. The α Helix and Photo 51

In 1951 Pauling and Corey proposed the α helix with $3.6$ residues per turn and a rise of $1.5\,\text{Å}$ per residue. The selection rule predicted a meridional reflection at $1/1.5\,\text{Å}^{-1}$, which no one had looked for; Perutz found it within days in horse hair and synthetic polypeptides, the first confirmation of the model.

The B form of DNA was photographed by Rosalind Franklin and Raymond Gosling in May 1952 (Photo 51), and it shows the cross of a helix at once. The analysis of such a pattern runs as follows (the figure computes it for the phosphate backbone).

- The spacing of the layer lines gives the repeat, $1/(0.294\,\mathrm{nm^{-1}}) = 3.4\,\mathrm{nm}$.
- A strong meridional reflection on the tenth layer line, at $0.34\,\mathrm{nm}$, gives the rise per unit, the stacking distance of the bases; so there are $10$ units per turn (in the fiber; $10.5$ in solution, [7.6.7](/7.6.7#sec-7.3)).
- The position of the first maximum on a layer line gives the radius of the helix: on layer line $n = 2$ the maximum lies at $R \approx 0.49\,\mathrm{nm^{-1}}$, so $2\pi Rr = 3.05$ gives $r \approx 1.0\,\mathrm{nm}$, the radius of the phosphates.
- The fourth layer line is missing. A single helix would give a strong fourth layer line; two identical helices displaced along the axis by $\Delta$ multiply the transform on layer line $l$ by $1 + \mathrm{e}^{2\pi\mathrm{i}l\Delta/P}$, which vanishes for $l = 4$ when $\Delta = 3P/8$. The two strands are therefore not evenly spaced: they are separated by $3/8$ of a turn on one side and $5/8$ on the other, the minor and major grooves.
- The density of the fibers and the number of nucleotides per repeat gave two chains per molecule.

Watson and Crick combined these parameters with base pairing in 1953 ([7.1.11](/7.1.11)). The fiber pattern alone does not determine the direction of the chains or the base pairing; it gave the helix parameters, which any model had to reproduce.

![Fiber diffraction of helices computed with the Cochran–Crick–Vand theory for B-DNA-like parameters: point scatterers (phosphates) on a helix of radius $1.0\,\mathrm{nm}$ and pitch $3.4\,\mathrm{nm}$ with $10$ units per turn, intensities on the layer lines $Z = l/P$ given by $\sum J_n^2(2\pi Rr)$ over the Bessel orders allowed by $l = n + 10m$. (A) A single helix: the strongest spot on each layer line moves outward linearly with $l$, forming the helix cross, and the meridional reflection on layer line $10$ gives the rise of $0.34\,\mathrm{nm}$. (B) Two helices displaced along the axis by $3P/8$, as the two backbones of B-DNA: the fourth layer line disappears. (C) The strand factor $\lvert1 + \mathrm{e}^{2\pi\mathrm{i}l\cdot3/8}\rvert^2$ by which (B) differs from (A); it vanishes for $l = 4$.](./plots/fiber-helix.py)

Fiber diffraction remains the method for systems that form oriented gels or fibers rather than crystals. The structure of tobacco mosaic virus was determined from fiber patterns at $2.9\,\text{Å}$ (Namba, Pattanayek and Stubbs, 1989), muscle fibers are studied by time-resolved fiber diffraction during contraction, and amyloid fibrils give the characteristic cross-β pattern, a meridional reflection at $4.7$–$4.8\,\text{Å}$ (the spacing of strands along the fibril axis) and an equatorial one near $10\,\text{Å}$ (the spacing of the stacked sheets).

## 10.6. Crystallization

### 10.6.1. What Makes a Good Crystal

The resolution of a crystal structure is limited by the order of the crystal: by how identical the molecules are and how precisely they are placed. Both depend on the protein before it is crystallized. Heterogeneity in sequence (proteolysis, heterogeneous termini), in modification (glycosylation, phosphorylation), in conformation (flexible loops and domains) or in oligomeric state broadens the distribution of molecules that the crystal averages. The sample is therefore prepared to be pure (more than $95\,\%$), monodisperse (checked by size-exclusion chromatography or light scattering, [7.6.9](/7.6.9#sec-9.2.5)) and conformationally homogeneous, often by engineering:

- removing flexible termini and loops identified by limited proteolysis, hydrogen–deuterium exchange or prediction, and replacing surface lysines and glutamates by alanines to lower the entropic cost of crystal contacts (surface entropy reduction);
- locking a conformation with a ligand, an inhibitor, a binding partner, or an antibody fragment or nanobody, which also provides additional surfaces for crystal contacts;
- for membrane proteins, choosing a **detergent** that keeps the protein stable, inserting soluble fusion domains such as T4 lysozyme or BRIL into flexible loops, and introducing thermostabilizing mutations; these steps made the structures of **G protein–coupled receptors** possible from 2007 onward.

### 10.6.2. The Phase Diagram and Nucleation

Crystallization is a phase transition of the protein from solution to an ordered solid, and it happens only from a supersaturated solution. At a given temperature, the **solubility** $c_{\mathrm{s}}$ of a protein decreases with the concentration of the precipitant: salts such as ammonium sulfate compete for water and screen charges (salting out), polyethylene glycols (PEG) cause depletion attraction between proteins, and organic solvents such as MPD lower the dielectric constant. The supersaturation $S = c/c_{\mathrm{s}}$ (the **relative supersaturation** of analytical chemistry, [6.4.4](/6.4.4)) is the driving force: the chemical potential of a protein molecule in solution exceeds that in the crystal by $\Delta\mu = k_{\mathrm{B}}T\ln S$.

**Formula 10.6.1 (Classical Nucleation Theory)** A crystalline nucleus of $n$ molecules has free energy

$$
\Delta G(n) = -n\,k_{\mathrm{B}}T\ln S + \gamma' n^{2/3},
$$
where the second term is the surface free energy ($\gamma' = (36\pi)^{1/3}v^{2/3}\gamma$ for a sphere of molecular volume $v$ and interfacial tension $\gamma$). It has a maximum at the critical nucleus

$$
n^* = \left(\frac{2\gamma'}{3k_{\mathrm{B}}T\ln S}\right)^3, \qquad \Delta G^* = \frac{4\gamma'^3}{27(k_{\mathrm{B}}T\ln S)^2},
$$
and the rate of nucleation per unit volume is $J = J_0\exp(-\Delta G^*/k_{\mathrm{B}}T)$.

This is the theory of **homogeneous nucleation** ([6.3](/6.3)) applied to proteins. Its key consequence is the strong dependence of $J$ on $S$ through $(\ln S)^{-2}$ in the exponent: with $\gamma' = 6\,k_{\mathrm{B}}T$, the barrier falls from $67\,k_{\mathrm{B}}T$ at $S = 2$ to $27\,k_{\mathrm{B}}T$ at $S = 3$ and $12\,k_{\mathrm{B}}T$ at $S = 5$, and the rate rises by more than $20$ orders of magnitude. There is therefore a metastable zone of moderate supersaturation in which existing crystals grow but new nuclei practically never form, and a labile zone at higher supersaturation in which nucleation is fast; at still higher supersaturation the protein precipitates as an amorphous solid or separates as a dense liquid. The ideal experiment nucleates a few crystals in the labile zone and then lets them grow slowly in the metastable zone; seeding (transferring crushed crystals into a metastable drop) separates the two steps deliberately. In practice nucleation is usually heterogeneous, on surfaces, impurities or dense liquid droplets, and the "two-step" mechanism through a dense liquid precursor is common for proteins, in line with the liquid–liquid phase separation of [7.6.29](/7.6.29).

![Crystallization. (A) Schematic phase diagram at constant temperature: below the solubility curve the solution is undersaturated; between the solubility and the nucleation boundary lies the metastable zone, where crystals grow but do not nucleate; above it, nucleation (labile zone), and at high supersaturation amorphous precipitation. A vapor-diffusion drop starts undersaturated; as water leaves it, protein and precipitant concentrations rise in proportion until the drop reaches the nucleation zone, where crystals form; their growth lowers the protein concentration toward the solubility curve. (B) Free energy of a nucleus of $n$ molecules for supersaturations $S = 2, 3, 5$ with $\gamma' = 6\,k_{\mathrm{B}}T$ (Formula 10.6.1); dots mark the critical nucleus $n^*$ and the barrier $\Delta G^*$. (C) Relative nucleation rate $\exp(-\Delta G^*/k_{\mathrm{B}}T)$ against $S$: it changes by about $30$ orders of magnitude between $S = 2$ and $S = 8$.](./plots/crystallization.py)

### 10.6.3. Methods and Screening

The commonest method is vapor diffusion. A drop of $0.1$–$2\,\mu\mathrm{L}$ containing protein and precipitant (typically mixed $1:1$ with the reservoir solution) is sealed over a reservoir of the precipitant at about twice the concentration, either hanging from a cover slip (hanging drop) or on a pedestal (sitting drop). Water evaporates from the drop to the reservoir until the vapor pressures are equal, and the concentrations of protein and precipitant in the drop rise slowly together, along a straight line through the origin of the phase diagram. Other methods take other paths: microbatch under oil mixes the components at their final concentrations; dialysis changes the precipitant concentration at constant protein concentration; free-interface diffusion lets protein and precipitant diffuse into each other and scans a gradient. Membrane proteins are often crystallized in the lipidic cubic phase, a bicontinuous lipid–water mesophase in which the protein remains in a membrane and forms layered, well-ordered crystals (bacteriorhodopsin in 1997, many GPCRs).

The conditions that crystallize a given protein cannot be predicted. Crystallization is therefore a search in a space of many variables (precipitant type and concentration, pH, salt, additives, temperature, protein concentration), done with robots in drops of $100\,\mathrm{nL}$. Sparse-matrix screens (Jancarik and Kim, 1991) sample combinations that have worked before, and promising conditions are then optimized by fine grids around them; the process is an optimization in a high-dimensional space with a noisy, rugged objective. A typical soluble protein is screened against several hundred conditions; in the structural genomics projects of the 2000s only about a third of the purified proteins crystallized, and fewer gave diffraction-quality crystals.

### 10.6.4. Derivatives and Ligand Complexes

Experimental phasing (10.9) needs crystals that contain heavy or anomalously scattering atoms at a few well-defined sites. They are introduced in three ways. Heavy-atom compounds (salts of $\ce{Hg}$, $\ce{Pt}$, $\ce{Au}$, $\ce{U}$, lanthanides, and clusters such as $\ce{Ta6Br12^2+}$) are soaked into existing crystals, where they bind to cysteines, histidines, methionines or carboxylates; halide ions (bromide, iodide) and the noble gases xenon and krypton under pressure bind to surface and hydrophobic sites. Selenomethionine is incorporated biosynthetically in place of methionine, by expression in a methionine-auxotrophic strain of *Escherichia coli* or with methionine biosynthesis inhibited, which gives one selenium per methionine at defined positions; it has been the most common route to new structures since the 1990s. Intrinsic metals ($\ce{Fe}$, $\ce{Zn}$, $\ce{Cu}$) and the sulfur atoms of cysteines and methionines can also be used. The same soaking or co-crystallization procedures produce the complexes of a protein with substrates, inhibitors and drug candidates; in structure-based drug design, hundreds of such complexes are determined by soaking fragments into one crystal form.

## 10.7. Data Collection

### 10.7.1. X-Ray Sources and Detectors

Laboratory sources produce the characteristic $\mathrm{K}\alpha$ line of a copper anode ($1.5418\,\text{Å}$) from a rotating anode or a microfocus tube. Most macromolecular data are collected at synchrotrons, where electrons circulating at GeV energies in a storage ring emit **synchrotron radiation** ([6.4.8](/6.4.8#sec-8.6.3)) in bending magnets and in insertion devices (wigglers and undulators, periodic arrays of magnets in which the electrons oscillate and the emitted waves add coherently). An undulator beam is $10^{9}$–$10^{12}$ times brighter than a laboratory tube, tunable in wavelength across absorption edges, and can be focused to a few micrometers. The first diffraction experiment on a protein crystal at a synchrotron was reported in 1976; fourth-generation storage rings with multi-bend achromat lattices (MAX IV in Sweden, the ESRF upgrade, the High Energy Photon Source in Beijing) have increased the brightness by another one to two orders of magnitude. In China, the Shanghai Synchrotron Radiation Facility has provided macromolecular crystallography beamlines since 2009.

Modern detectors are hybrid pixel arrays that count individual photons with no readout noise and frame rates of hundreds of hertz, which allows continuous rotation with very fine slicing ($0.05$–$0.1^\circ$ per frame). The crystal, mounted in a loop on a goniometer, is kept at $100\,\mathrm{K}$ in a stream of cold nitrogen gas.

### 10.7.2. Radiation Damage and Cryocrystallography

X-rays are scattered elastically by a tiny fraction of the atoms they meet; many more photons are absorbed photoelectrically. At $1\,\text{Å}$ the ratio of absorbed to elastically scattered photons in a protein crystal is about $10$, and each absorption releases a photoelectron of about $12\,\mathrm{keV}$ that produces hundreds of ionizations and radicals. The damage is measured by the absorbed dose in grays ($1\,\mathrm{Gy} = 1\,\mathrm{J\,kg^{-1}}$). At room temperature a protein crystal loses its high-resolution diffraction after a few tenths of a megagray; cooled to $100\,\mathrm{K}$, it survives roughly a hundred times longer, because the radicals diffuse much more slowly. The diffracted intensity of a cryocooled crystal falls to half at about $30\,\mathrm{MGy}$ (the Garman limit; Henderson's earlier estimate was $20\,\mathrm{MGy}$). Before global damage is visible, specific damage occurs at particular sites: disulfide bonds break, carboxylates of glutamate and aspartate lose $\ce{CO2}$, metal centres are photoreduced. Structures of redox-active metalloproteins collected with a high dose may therefore show the wrong oxidation state, a problem that X-ray free-electron lasers avoid (10.13).

Cooling requires preventing the water in the crystal from forming crystalline ice, which would destroy the lattice and add ice rings to the pattern. Crystals are transferred briefly into a cryoprotectant (the mother liquor with $15$–$30\,\%$ glycerol, ethylene glycol, low-molecular-weight PEG, sugars or MPD) and plunged into liquid nitrogen or the cold stream, where the solvent vitrifies.

### 10.7.3. The Rotation Method in Practice

A data collection strategy chooses the wavelength, the detector distance, the exposure, the width of each frame and the total rotation. Two geometric constraints guide it. First, the reflections recorded on one frame must not overlap: a reflection is spread over the mosaic spread $\eta$ (plus the beam divergence), and neighbouring lunes from successive planes of the reciprocal lattice perpendicular to the beam are separated by an angle $d/a$, where $a$ is the cell edge along the beam.

**Formula 10.7.1 (Maximum Oscillation Range)** To avoid overlap between neighbouring lunes at resolution $d$, the rotation per frame must satisfy

$$
\Delta\phi_{\max} = \frac{180^\circ}{\pi}\,\frac{d}{a} - \eta.
$$

For $a = 150\,\text{Å}$, $d = 2\,\text{Å}$ and $\eta = 0.3^\circ$, $\Delta\phi_{\max} = 0.46^\circ$; very large cells (ribosomes, viruses) require frames of $0.1^\circ$ or less, which modern detectors provide anyway. The detector distance is set so that the spots at the highest useful resolution fall on the detector and neighbouring spots remain separated ($\text{distance}/\text{spot spacing} \propto a$).

Second, the total rotation must cover the unique part of reciprocal space, which depends on the point group: $180^\circ$ for $P1$ (any start), $180^\circ$ about $\boldsymbol{b}$ or $90^\circ$ in other orientations for monoclinic crystals, $90^\circ$ for orthorhombic, $45$–$90^\circ$ for tetragonal crystals depending on the orientation of the fourfold axis, and less for higher symmetry. Anomalous data need both members of each Friedel pair and require more (typically an extra $2\theta_{\max}$, or $360^\circ$), and high multiplicity (many measurements of each unique reflection) improves the accuracy of the small anomalous differences. Completeness above $95\,\%$, especially at low resolution, is essential, because missing strong low-resolution reflections distort the whole map.

## 10.8. Data Processing and the Statistics of Intensities

### 10.8.1. From Images to Intensities

Data processing converts a few thousand images into a list of indices $hkl$, intensities $I(hkl)$ and their standard uncertainties $\sigma(I)$. It proceeds in steps.

1. Spot finding locates the diffraction spots and converts their detector positions and rotation angles into reciprocal-space vectors with the known geometry.
2. Indexing finds three basis vectors such that all observed vectors are integer combinations of them, by Fourier analysis of the projections of the vectors on many directions (a one-dimensional FFT shows the periodicity along each direction) or by analysing difference vectors. The result is a reduced cell (the Niggli cell) and the orientation of the crystal. The metric symmetry of the reduced cell suggests the possible Bravais lattices, which are tested against the $44$ lattice characters of the International Tables.
3. Refinement of the geometry (crystal orientation, cell, detector distance and tilt, beam centre, mosaic spread) by least squares on the observed spot positions.
4. Integration measures the intensity of each predicted reflection, either by summation (sum of pixel counts in the spot minus a background estimated from surrounding pixels) or by profile fitting (fitting a learned spot profile, which reduces the noise of weak reflections). Corrections for the Lorentz and polarization factors (Formula 10.3.1) and for partially recorded reflections are applied.
5. Scaling puts all observations on a common scale by refining a smooth scale and B-factor as functions of rotation angle (correcting beam decay, absorption, illuminated volume and radiation damage) so that symmetry-equivalent observations agree. It minimizes

   $$
   \Psi = \sum_{\boldsymbol{h}}\sum_{l}w_{\boldsymbol{h}l}\left(I_{\boldsymbol{h}l} - g_{\boldsymbol{h}l}\langle I_{\boldsymbol{h}}\rangle\right)^2,
   $$
   where $I_{\boldsymbol{h}l}$ is the $l$-th observation of unique reflection $\boldsymbol{h}$, $g_{\boldsymbol{h}l}$ its scale factor and $\langle I_{\boldsymbol{h}}\rangle$ the weighted mean. The agreement of equivalents also tests the Laue group, and the systematic absences suggest the space group (10.3.7).
6. Merging averages the equivalent observations, and amplitudes are derived from intensities. Since weak intensities can be measured as negative, $\lvert F\rvert = \sqrt I$ is not used directly; the French–Wilson procedure computes the posterior mean of $\lvert F\rvert$ given the measurement and the Wilson prior (10.8.3).

### 10.8.2. Data Quality

The internal consistency of the data is measured by the spread of equivalent observations.

**Definition 10.8.1 (Merging Statistics)** For unique reflections $\boldsymbol{h}$ measured $n_{\boldsymbol{h}}$ times with intensities $I_{\boldsymbol{h}l}$ and mean $\langle I_{\boldsymbol{h}}\rangle$,

$$
R_{\mathrm{merge}} = \frac{\sum_{\boldsymbol{h}}\sum_l\lvert I_{\boldsymbol{h}l} - \langle I_{\boldsymbol{h}}\rangle\rvert}{\sum_{\boldsymbol{h}}\sum_lI_{\boldsymbol{h}l}}, \quad R_{\mathrm{meas}} = \frac{\sum_{\boldsymbol{h}}\sqrt{\frac{n_{\boldsymbol{h}}}{n_{\boldsymbol{h}} - 1}}\sum_l\lvert I_{\boldsymbol{h}l} - \langle I_{\boldsymbol{h}}\rangle\rvert}{\sum_{\boldsymbol{h}}\sum_lI_{\boldsymbol{h}l}}, \quad R_{\mathrm{pim}} = \frac{\sum_{\boldsymbol{h}}\sqrt{\frac{1}{n_{\boldsymbol{h}} - 1}}\sum_l\lvert I_{\boldsymbol{h}l} - \langle I_{\boldsymbol{h}}\rangle\rvert}{\sum_{\boldsymbol{h}}\sum_lI_{\boldsymbol{h}l}}.
$$
The half-set correlation $CC_{1/2}$ is the Pearson **correlation coefficient** between the mean intensities of two random halves of the observations of each reflection.

$R_{\mathrm{merge}}$, the traditional statistic, has a defect: the deviation from a mean of $n$ values underestimates the spread by the factor $\sqrt{(n-1)/n}$, so $R_{\mathrm{merge}}$ increases with multiplicity even though the merged data improve. $R_{\mathrm{meas}}$ corrects this and measures the precision of single observations; $R_{\mathrm{pim}}$ measures the precision of the merged mean and decreases with multiplicity. The $R$ values are dominated by the strong reflections and become meaningless in the outer shells, where intensities approach zero and $R$ grows above $100\,\%$ even for useful data.

$CC_{1/2}$ has better statistical properties (Karplus and Diederichs, 2012): it is $1$ for perfect data and $0$ for pure noise, and its significance can be tested for the number of reflections in a shell. If the two halves have equal errors, the correlation of the merged data with the noise-free true intensities is

$$
CC^* = \sqrt{\frac{2CC_{1/2}}{1 + CC_{1/2}}},
$$
which can be compared directly with the correlation between the data and a model ($CC_{\mathrm{work}}$, $CC_{\mathrm{free}}$). Data are used to the resolution at which they still contain significant signal, typically where $CC_{1/2}$ drops to about $0.3$ and $\langle I/\sigma(I)\rangle$ of the merged data to about $1$–$2$; weak high-resolution data, if properly weighted, improve the model and do not harm it. $CC_{1/2}$ plays the role of the Fourier shell correlation in cryo-electron microscopy ([7.6.14](/7.6.14)).

![Data-quality statistics from simulated data (Wilson-distributed intensities with $B = 34\,\text{Å}^2$, Poisson noise on signal and background, $3\,\%$ scale error per observation). (A) In resolution shells (multiplicity $4$): the merged $\langle I/\sigma(I)\rangle$ (log scale, left) falls steadily with resolution, while $CC_{1/2}$ and $CC^*$ (right) stay near $1$ until the signal approaches the noise and then drop; dashed lines mark $CC_{1/2} = 0.3$ and $\langle I/\sigma\rangle = 1.5$, which here both suggest a cutoff near $1.7\,\text{Å}$. (B) For the lowest-resolution shell, against multiplicity: $R_{\mathrm{merge}}$ increases with multiplicity (its bias at small $n$), $R_{\mathrm{meas}}$ is independent of it, and $R_{\mathrm{pim}}$, the precision of the merged intensities, falls as $1/\sqrt{n - 1}$.](./plots/data-quality.py)

### 10.8.3. Wilson Statistics

Before any phases are known, the distribution of the intensities already says much about the crystal. Wilson (1942, 1949) treated the atoms as randomly placed in the cell. For a reflection $\boldsymbol{h}$ in an acentric position, the real and imaginary parts of $F = \sum_jf_j\mathrm{e}^{2\pi\mathrm{i}\boldsymbol{h}\cdot\boldsymbol{r}_j}$ are sums of many terms with effectively random phases.

**Theorem 10.8.1 (Wilson Statistics)** For $N$ atoms at random positions, by the **central limit theorem** ([3.1](/3.1)) the real and imaginary parts of $F(\boldsymbol{h})$ are independent Gaussian variables with mean $0$ and variance $\Sigma/2$, $\Sigma = \sum_jf_j^2$. Hence

$$
\langle\lvert F\rvert^2\rangle = \Sigma = \sum_jf_j^2,
$$
and the normalized amplitude $\lvert E\rvert = \lvert F\rvert/\sqrt\Sigma$ follows the **Rayleigh distribution** $p(\lvert E\rvert) = 2\lvert E\rvert\mathrm{e}^{-\lvert E\rvert^2}$, that is, the normalized intensity $z = \lvert E\rvert^2$ is exponentially distributed, $p(z) = \mathrm{e}^{-z}$. For centric reflections, whose structure factors are real, $p(\lvert E\rvert) = \sqrt{2/\pi}\,\mathrm{e}^{-\lvert E\rvert^2/2}$.

The mean intensity therefore depends only on the composition, not on the arrangement, as the phase-swap figure suggested. Its dependence on resolution gives the scale of the data and the overall temperature factor.

**Formula 10.8.1 (Wilson Plot)** With an overall isotropic temperature factor $B$, the mean intensity in a thin shell of resolution is $\langle I\rangle = k\sum_jf_{0,j}^2(s)\,\mathrm{e}^{-2Bs^2}$ with $s = \sin\theta/\lambda$, so

$$
\ln\frac{\langle I\rangle}{\sum_jf_{0,j}^2(s)} = \ln k - 2B\,s^2,
$$
a straight line whose slope gives $B$ (the Wilson B) and whose intercept gives the absolute scale $k$.

For proteins the Wilson plot is linear only beyond about $4\,\text{Å}$; at lower resolution the atoms are not randomly distributed (the solvent is flat, and the protein has secondary structure, which produces a bump near $4$–$5\,\text{Å}$ from the spacing of helices and strands). The distribution of $z$ is used to detect problems: centric and acentric reflections have different second moments, $\langle z^2\rangle = 3$ and $2$, and $\langle\lvert E^2 - 1\rvert\rangle = 0.968$ and $0.736$.

![Wilson statistics of a random-atom model: $400$ carbon atoms at random positions in an orthorhombic cell of $40\times50\times60\,\text{Å}$ with $B = 20\,\text{Å}^2$, structure factors to $2.5\,\text{Å}$. (A) Wilson plot: shell averages of $\ln(\langle I\rangle/\sum f_0^2)$ against $s^2 = (\sin\theta/\lambda)^2$ lie on a straight line of slope $-2B$; the fit returns $B = 20.5\,\text{Å}^2$. (B) Cumulative distributions $N(z)$ of the normalized intensity: acentric data follow $1 - \mathrm{e}^{-z}$ (exponential), centric data (the same atoms with inversion partners, $P\bar1$) follow $\operatorname{erf}\sqrt{z/2}$, with many more weak reflections; averaging pairs of independent intensities, as a perfect twin does, gives $1 - (1 + 2z)\mathrm{e}^{-2z}$ with too few weak reflections.](./plots/wilson.py)

### 10.8.4. Twinning

A twinned crystal consists of domains whose lattices coincide (or nearly so) but whose contents are related by an operation that is not a symmetry of the structure, the twin law. Merohedral twinning is possible when the lattice has higher symmetry than the point group of the structure: a tetragonal lattice of point group $4$ can host domains related by a twofold axis along $\boldsymbol{a}$, which belongs to the lattice symmetry $4/mmm$ but not to the crystal. The measured intensities are then sums of the intensities of twin-related reflections weighted by the domain fractions,

$$
I_{\mathrm{obs}}(\boldsymbol{h}_1) = (1 - \alpha)I(\boldsymbol{h}_1) + \alpha I(\boldsymbol{h}_2), \qquad I_{\mathrm{obs}}(\boldsymbol{h}_2) = \alpha I(\boldsymbol{h}_1) + (1 - \alpha)I(\boldsymbol{h}_2),
$$
with twin fraction $\alpha \le \frac12$. For $\alpha < \frac12$ the true intensities can be recovered by inverting these equations; for a perfect twin ($\alpha = \frac12$) they cannot, and the data look like those of a crystal with the higher symmetry. Twinning is detected statistically: averaging two independent intensities reduces their spread, so $\langle I^2\rangle/\langle I\rangle^2$ falls from $2$ to $1.5$ for a perfect twin (acentric data), there are too few weak reflections (Wilson figure, panel B), and the local $L$ test, based on differences of intensities of nearby reflections, gives $\langle\lvert L\rvert\rangle = \frac12$ for untwinned and $\frac38$ for perfectly twinned data. Twinned data can still be used in refinement with the twin law included in the model.

## 10.9. Experimental Phasing

### 10.9.1. Isomorphous Replacement

Perutz's idea of 1953 was to compare the diffraction of a native protein crystal with that of the same crystal with a few heavy atoms bound. If the derivative is isomorphous with the native crystal (same cell, same positions of all protein atoms), then for every reflection

$$
F_{\mathrm{PH}} = F_{\mathrm{P}} + F_{\mathrm{H}},
$$
where $F_{\mathrm{P}}$ is the structure factor of the protein, $F_{\mathrm{H}}$ that of the heavy atoms alone and $F_{\mathrm{PH}}$ that of the derivative. The amplitudes $\lvert F_{\mathrm{P}}\rvert$ and $\lvert F_{\mathrm{PH}}\rvert$ are measured. The heavy-atom positions, and hence $F_{\mathrm{H}}$ with its phase, are found from the differences: the difference Patterson with coefficients $(\lvert F_{\mathrm{PH}}\rvert - \lvert F_{\mathrm{P}}\rvert)^2$ approximates the Patterson function of the heavy atoms alone (10.4.2), and with a handful of sites it can be solved like that of a small molecule, today mostly by direct methods.

It was widely believed that a few heavy atoms could not change the intensities of a protein measurably. Wilson statistics show why they do: the rms amplitudes add as

$$
\frac{\langle\lvert F_{\mathrm{H}}\rvert^2\rangle^{1/2}}{\langle\lvert F_{\mathrm{P}}\rvert^2\rangle^{1/2}} = \sqrt{\frac{N_{\mathrm{H}}}{N_{\mathrm{P}}}}\,\frac{f_{\mathrm{H}}}{f_{\mathrm{P}}},
$$
so two mercury atoms ($f = 80$) in hemoglobin (about $4400$ non-hydrogen atoms of average $f \approx 6.7$) change the amplitudes by about $25\,\%$ on average (Crick and Magdoff, 1956), easily seen on film. The requirement of isomorphism is the hard part: a change of the cell by $0.5\,\%$ or a small movement of the protein produces intensity changes comparable to the heavy-atom signal at medium resolution.

**Definition 10.9.1 (Isomorphous Replacement)** **Isomorphous replacement** is the determination of protein phases from the differences between the diffraction amplitudes of a native crystal and of one (single isomorphous replacement, SIR) or more (**multiple isomorphous replacement**, MIR) isomorphous heavy-atom derivatives whose heavy-atom substructure has been determined.

For one reflection, $\lvert F_{\mathrm{PH}}\rvert^2 = \lvert F_{\mathrm{P}}\rvert^2 + \lvert F_{\mathrm{H}}\rvert^2 + 2\lvert F_{\mathrm{P}}\rvert\lvert F_{\mathrm{H}}\rvert\cos(\varphi_{\mathrm{P}} - \varphi_{\mathrm{H}})$, so

$$
\varphi_{\mathrm{P}} = \varphi_{\mathrm{H}} \pm \arccos\frac{\lvert F_{\mathrm{PH}}\rvert^2 - \lvert F_{\mathrm{P}}\rvert^2 - \lvert F_{\mathrm{H}}\rvert^2}{2\lvert F_{\mathrm{P}}\rvert\lvert F_{\mathrm{H}}\rvert}. \tag{10.7}
$$
One derivative gives two possible phases, symmetric about $\varphi_{\mathrm{H}}$. Harker's construction (1956) shows this geometrically: draw a circle of radius $\lvert F_{\mathrm{P}}\rvert$ about the origin and a circle of radius $\lvert F_{\mathrm{PH}}\rvert$ about the point $-F_{\mathrm{H}}$; their two intersections are the possible $F_{\mathrm{P}}$. A second derivative with heavy atoms at other sites gives another pair of solutions, one of which coincides with one of the first pair: the true phase.

Real measurements have errors, and the circles do not meet exactly. Blow and Crick (1959) replaced the geometric intersection by a probability. For a trial phase $\varphi$, the lack of closure $\varepsilon(\varphi) = \lvert F_{\mathrm{PH}}\rvert - \lvert\lvert F_{\mathrm{P}}\rvert\mathrm{e}^{\mathrm{i}\varphi} + F_{\mathrm{H}}\rvert$ is assumed Gaussian with variance $E^2$ (errors of measurement and of the heavy-atom model, and lack of isomorphism), so

$$
P(\varphi) \propto \exp\left(-\frac{\varepsilon(\varphi)^2}{2E^2}\right),
$$
and the probabilities from several derivatives multiply. The map is computed with the centroid ("best") structure factor $F_{\mathrm{best}} = m\lvert F_{\mathrm{P}}\rvert\mathrm{e}^{\mathrm{i}\varphi_{\mathrm{best}}}$, where $m\,\mathrm{e}^{\mathrm{i}\varphi_{\mathrm{best}}} = \int P(\varphi)\mathrm{e}^{\mathrm{i}\varphi}\,\mathrm{d}\varphi$; the figure of merit $m = \langle\cos\Delta\varphi\rangle$ is the expected cosine of the phase error ($m = 0.8$ corresponds to about $37^\circ$). The best Fourier minimizes the mean square error of the map. Modern programs refine the heavy-atom parameters and the error model together by maximum likelihood, the same principle used throughout crystallography today (**maximum likelihood estimation**, [3.2](/3.2)).

![Isomorphous replacement. (A) Harker construction for one reflection with $F_{\mathrm{P}} = 100\,\mathrm{e}^{\mathrm{i}60^\circ}$ and two derivatives with $F_{\mathrm{H}1} = 30\,\mathrm{e}^{\mathrm{i}200^\circ}$ and $F_{\mathrm{H}2} = 25\,\mathrm{e}^{\mathrm{i}320^\circ}$: the protein circle (radius $\lvert F_{\mathrm{P}}\rvert$, centre $0$) meets the circle of derivative 1 (radius $\lvert F_{\mathrm{PH}1}\rvert$, centre $-F_{\mathrm{H}1}$) at two points, the true $F_{\mathrm{P}}$ and a false solution near $-20^\circ$; the circle of derivative 2 passes through the true point and resolves the ambiguity. (B) Blow–Crick phase probabilities with a lack-of-closure error $E = 6$: SIR is bimodal (figure of merit $0.79$, best phase $20^\circ$, between the two solutions), MIR is unimodal near the true phase (figure of merit $0.98$, best phase $58^\circ$).](./plots/harker.py)

Kendrew's $6\,\text{Å}$ map of myoglobin (1957) was phased in this way from five derivatives and about $400$ reflections; the $2\,\text{Å}$ structure followed in 1959–1960, the $5.5\,\text{Å}$ map of hemoglobin in 1959, and Perutz and Kendrew received the Nobel Prize in Chemistry in 1962. Lysozyme (1965) was the first enzyme. Isomorphous replacement dominated protein crystallography for three decades; today it is used mainly in combination with anomalous scattering (SIRAS, MIRAS).

### 10.9.2. Anomalous Scattering

The scattering factor of Definition 10.3.1 assumes that the electrons are free. When the photon energy approaches the energy needed to eject an inner-shell electron (an absorption edge), the bound electrons respond resonantly, like a driven damped oscillator near its resonance ([5.1](/5.1)), and the scattering factor becomes complex:

$$
f(S, E) = f_0(S) + f'(E) + \mathrm{i}f''(E). \tag{10.8}
$$
The normal part $f_0$ depends on the scattering angle; the anomalous corrections $f'$ and $f''$ come from the compact inner shells and are nearly independent of angle but depend strongly on the energy. The imaginary part is proportional to the absorption cross-section $\sigma_{\mathrm{a}}$ (by the optical theorem, $f'' = E\sigma_{\mathrm{a}}/(2hcr_{\mathrm{e}})$), so it jumps up at the edge, and it is measured by an X-ray fluorescence scan of the crystal; the real part follows from it by the Kramers–Kronig relation, a consequence of causality,

$$
f'(E) = \frac{2}{\pi}\,\mathrm{P}\!\int_0^\infty\frac{E'f''(E')}{E^2 - E'^2}\,\mathrm{d}E',
$$
which gives a sharp negative minimum of $f'$ at the inflection point of the edge.

**Definition 10.9.2 (Anomalous Scattering)** **Anomalous scattering** (anomalous dispersion, resonant scattering) is the elastic scattering of X-rays with energies near an absorption edge of an atom, described by the wavelength-dependent corrections $f'$ and $f''$ to its scattering factor. A pair of reflections $\boldsymbol{h}$ and $-\boldsymbol{h}$ whose amplitudes differ because of $f''$ is a Bijvoet pair, and the difference $\Delta F_{\pm} = \lvert F(\boldsymbol{h})\rvert - \lvert F(-\boldsymbol{h})\rvert$ is the anomalous (Bijvoet) difference.

The imaginary term breaks Friedel's law (Theorem 10.3.2). Write $F(\boldsymbol{h}) = F_{\mathrm{N}} + \mathrm{i}\kappa F_{\mathrm{A}}$, where $F_{\mathrm{N}}$ includes all normal scattering (including $f_0 + f'$ of the anomalous atoms) and $F_{\mathrm{A}}$ is the normal contribution of the anomalous atoms, $\kappa = f''/(f_0 + f')$. Then $F(-\boldsymbol{h})^* = F_{\mathrm{N}} - \mathrm{i}\kappa F_{\mathrm{A}}$: the anomalous contribution is $90^\circ$ ahead of $F_{\mathrm{A}}$ for $+\boldsymbol{h}$ and behind it for the conjugate of $-\boldsymbol{h}$, and the amplitudes differ unless $F_{\mathrm{N}}$ and $F_{\mathrm{A}}$ are parallel or antiparallel.

**Formula 10.9.1 (Size of the Anomalous Signal)** For $N_{\mathrm{A}}$ anomalous scatterers among $N_{\mathrm{T}}$ atoms of average scattering factor $Z_{\mathrm{eff}} \approx 6.7$ (proteins), the expected relative Bijvoet difference is

$$
\frac{\langle\Delta F_\pm^2\rangle^{1/2}}{\langle\lvert F\rvert^2\rangle^{1/2}} \approx \sqrt{\frac{2N_{\mathrm{A}}}{N_{\mathrm{T}}}}\,\frac{f''}{Z_{\mathrm{eff}}}.
$$

**Example 10.9.1 (Selenomethionine and Sulfur)** A selenomethionine protein with one methionine per $100$ residues has $N_{\mathrm{T}} \approx 780$ non-hydrogen atoms per selenium. At the Se K-edge peak ($\lambda = 0.979\,\text{Å}$, $12.658\,\mathrm{keV}$, $f'' \approx 4$) the Bijvoet ratio is $\sqrt{2/780}\times3.8/6.7 = 2.9\,\%$. The sulfur atoms of a native protein (about $1$ per $30$ residues, $f'' = 0.56$ at $1.54\,\text{Å}$ and about $0.24$ at $1\,\text{Å}$) give $1\,\%$ or less, which requires very accurate data with high multiplicity and long wavelengths ($2$–$3\,\text{Å}$, where $f''$ is larger), the domain of native S-SAD. Since intensities are measured with errors of a few percent, the anomalous signal must be extracted statistically from tens of thousands of reflections.

![Anomalous scattering. (A) Model of the anomalous scattering factors of selenium near its K edge ($12.658\,\mathrm{keV}$): $f''$ rises from about $0.5$ to $3.8$ electrons with a white line just above the edge, and $f'$, its Kramers–Kronig partner, has a sharp minimum of about $-8.5$ at the inflection point. MAD experiments collect data at the peak (maximum $f''$), the inflection (minimum $f'$) and a remote wavelength. (B) Argand diagram of a Bijvoet pair: the anomalous contribution, $90^\circ$ ahead of the normal contribution $F_{\mathrm{A}}$ of the anomalous atoms, adds to $F_{\mathrm{N}}$ with opposite signs for $F(+\boldsymbol{h})$ and $F(-\boldsymbol{h})^*$, so their lengths differ. (C) Expected Bijvoet ratio (Formula 10.9.1) against the number of residues per anomalous atom, for Se at the peak and below the edge and for S at $2.1$ and $1.54\,\text{Å}$; the dashed line marks $1\,\%$.](./plots/anomalous.py)

### 10.9.3. MAD and SAD

In multiwavelength anomalous diffraction, data are collected from one crystal at two to four wavelengths around an absorption edge, chosen to maximize $f''$ (peak), to minimize $f'$ (inflection, giving the largest dispersive differences between wavelengths), and far from the edge (remote). The measured amplitudes depend on the unknown phase difference $\varphi_{\mathrm{T}} - \varphi_{\mathrm{A}}$ through (Karle, 1980; Hendrickson)

$$
\lvert F(\pm\boldsymbol{h}, \lambda)\rvert^2 = \lvert F_{\mathrm{T}}\rvert^2 + a(\lambda)\lvert F_{\mathrm{A}}\rvert^2 + b(\lambda)\lvert F_{\mathrm{T}}\rvert\lvert F_{\mathrm{A}}\rvert\cos(\varphi_{\mathrm{T}} - \varphi_{\mathrm{A}}) \pm c(\lambda)\lvert F_{\mathrm{T}}\rvert\lvert F_{\mathrm{A}}\rvert\sin(\varphi_{\mathrm{T}} - \varphi_{\mathrm{A}}),
$$
with $a = (f'^2 + f''^2)/f_0^2$, $b = 2f'/f_0$, $c = 2f''/f_0$, where $F_{\mathrm{T}}$ is the structure factor without anomalous terms and $F_{\mathrm{A}}$ that of the anomalous atoms with $f_0$. Measurements at several wavelengths and both members of each Bijvoet pair give an overdetermined system for $\lvert F_{\mathrm{T}}\rvert$, $\lvert F_{\mathrm{A}}\rvert$ and $\Delta\varphi$. The anomalous atoms are located from $\lvert F_{\mathrm{A}}\rvert$ by Patterson or direct methods, $\varphi_{\mathrm{A}}$ is computed, and $\varphi_{\mathrm{T}} = \varphi_{\mathrm{A}} + \Delta\varphi$. Because all data come from one crystal, there is no lack of isomorphism. Hendrickson developed MAD with selenomethionine around 1990, and with tunable synchrotron beamlines it became the standard method of the 1990s.

**Definition 10.9.3 (SAD and MAD)** **Single-wavelength anomalous diffraction** (SAD) determines phases from the Bijvoet differences measured at one wavelength, together with the substructure of anomalous scatterers and density modification; **multiwavelength anomalous diffraction** (MAD) uses data collected at several wavelengths near an absorption edge.

SAD is formally like SIR: the Bijvoet difference gives the sine of $\varphi_{\mathrm{T}} - \varphi_{\mathrm{A}}$, so each reflection has two possible phases, symmetric about $\varphi_{\mathrm{A}} + 90^\circ$. The ambiguity is broken by density modification (10.11), which selects the solution that gives a flat solvent and a protein-like density. Since SAD needs only one data set, it minimizes radiation damage, and with accurate data from modern detectors it has largely replaced MAD; it is now the most common method of experimental phasing, with selenium, sulfur, halides or bound metals as scatterers. The anomalous data also fix the hand of the structure (they distinguish the substructure from its mirror image, and $P4_1$ from $P4_3$), and anomalous difference maps identify metal ions and halides in a refined model.

## 10.10. Molecular Replacement

When a structure similar to the unknown one is available, its phases can be borrowed. The search model must be placed in the unit cell of the new crystal in the correct orientation and position, a search over three rotational and three translational parameters, and its calculated structure factors then provide initial phases for the observed amplitudes. Rossmann and Blow proposed the method in 1962, after noting that the subunits of hemoglobin resemble myoglobin.

**Definition 10.10.1 (Molecular Replacement)** **Molecular replacement** is the determination of initial phases for a crystal structure by placing a known or predicted model of the molecule (or of part of it) in the unit cell, in the orientation and position that best explain the observed diffraction amplitudes, and computing the phases from the placed model.

The six-dimensional search is split into two three-dimensional ones by using the Patterson function. The vectors within one molecule (self-vectors) depend only on its orientation and lie near the origin of the Patterson function, within a radius about the size of the molecule; the vectors between molecules depend also on their positions.

**Formula 10.10.1 (Rotation and Translation Functions)** The rotation function measures the overlap of the observed Patterson function with the Patterson function of the model rotated by $\boldsymbol{C}$, within a sphere $U$ around the origin:

$$
R(\boldsymbol{C}) = \int_UP_{\mathrm{obs}}(\boldsymbol{u})\,P_{\mathrm{model}}(\boldsymbol{C}\boldsymbol{u})\,\mathrm{d}^3\boldsymbol{u}.
$$
For the correctly oriented model, the translation function measures the agreement as a function of the position $\boldsymbol{t}$ of the model, for example by the correlation coefficient between observed and calculated intensities, $T(\boldsymbol{t}) = \operatorname{Corr}\left(\lvert F_{\mathrm{obs}}\rvert^2, \lvert F_{\mathrm{calc}}(\boldsymbol{t})\rvert^2\right)$, including all symmetry-related copies.

Both functions are computed efficiently in reciprocal space with FFTs. Current programs (Phaser) replace the overlap functions by maximum-likelihood targets that account for the expected error of the model: the log-likelihood gain (LLG) of a placement measures how much better it explains the data than a random placement, and a translation-function Z-score above $8$ usually indicates a correct solution. Several copies in the asymmetric unit and several domains are placed one after another.

Molecular replacement works when the model is close enough to the target: classically, sequence identity above about $30\,\%$ and a coordinate rmsd below about $1.5$–$2\,\text{Å}$ in the core, with flexible loops and side chains removed. It accounts for most structures in the PDB, because many proteins are solved again with different ligands, mutations or partners. Since 2020, models predicted by AlphaFold and related methods ([7.6.15](/7.6.15)) are accurate enough to solve most new structures by molecular replacement, with the predicted local confidence used to trim unreliable regions and to set the expected B-factors; experimental phasing is now needed mainly for difficult cases, for complexes whose arrangement cannot be predicted and for validation.

Phases dominate the appearance of a map (10.3.4), so a map computed with model phases shows features of the model even where the model is wrong. This model bias is reduced by weighting: the map coefficients $2m\lvert F_{\mathrm{o}}\rvert - D\lvert F_{\mathrm{c}}\rvert$ (with the figure of merit $m$ and the scale $D$ from the $\sigma_A$ method, below) give a map in which missing features appear at about half their weight and wrong features are suppressed, and the difference map with coefficients $m\lvert F_{\mathrm{o}}\rvert - D\lvert F_{\mathrm{c}}\rvert$ shows positive density where atoms are missing and negative density where the model has atoms that are not there. Omit maps, computed after removing a part of the model and refining the rest, test whether a feature (a ligand, a loop) is supported by the data.

## 10.11. Density Modification

Initial phases from experiment or from a model contain large errors, typically $40$–$70^\circ$. Density modification improves them by imposing on the map what is known about electron densities of macromolecular crystals, and alternating between real and reciprocal space.

**Algorithm 10.11.1 (Density Modification)** Start with observed amplitudes $\lvert F_{\mathrm{o}}\rvert$ and initial phases $\varphi^{(0)}$ with weights.

1. Compute the map $\rho^{(n)}$ by Fourier synthesis with weighted coefficients.
2. Modify the map: set the solvent region (determined from the local variance of the density) to a constant value (solvent flattening), rescale the protein region so that its density histogram matches that expected for proteins at this resolution (histogram matching), and average the density over copies related by non-crystallographic symmetry (NCS averaging).
3. Fourier transform the modified map to obtain new structure factors $F_{\mathrm{mod}}$.
4. Combine the phases of $F_{\mathrm{mod}}$ with the observed amplitudes and the original phase information (phase combination, with probability weights), and return to step 1 until convergence.

Solvent flattening is effective because protein crystals contain $30$–$70\,\%$ solvent, which is disordered and therefore flat in the true density: a map with wrong phases has noise everywhere, and flattening the solvent removes a large part of the noise, which in reciprocal space changes all phases at once. The power of the constraint grows with the solvent fraction. NCS averaging is even stronger: with $n$ copies of the molecule in the asymmetric unit, the average of $n$ copies has $\sqrt n$ less noise, and for icosahedral viruses with $60$-fold or higher redundancy, averaging can extend phases from low to high resolution from a very poor start. Density modification is what turns the twofold ambiguity of SAD and SIR into unique phases.

The weights used in all these maps come from a probability model of the errors. If a partial or approximate model is correct in some parts, the probability that the true phase is $\varphi$ given the model phase $\varphi_{\mathrm{c}}$ has the von Mises form $P(\varphi) \propto \exp[X\cos(\varphi - \varphi_{\mathrm{c}})]$ (Sim, 1959), and the figure of merit is

$$
m = \frac{I_1(X)}{I_0(X)}, \qquad X = \frac{2\lvert F_{\mathrm{o}}\rvert\lvert F_{\mathrm{c}}\rvert}{\Sigma_{\mathrm{Q}}},
$$
where $I_0$ and $I_1$ are modified Bessel functions and $\Sigma_{\mathrm{Q}}$ the mean square contribution of the missing part. Luzzati's model of random coordinate errors and Read's $\sigma_A$ method generalize this: $\sigma_A$ is estimated in resolution shells from the agreement of normalized observed and calculated amplitudes, and it gives $m$, $D$ and the map coefficients of 10.10 without needing the true structure.

## 10.12. Model Building, Refinement and Validation

### 10.12.1. Building a Model

An atomic model is interpreted in the electron density: the chain is traced, the sequence is assigned from the shapes of side chains, and the geometry is adjusted to the density. This used to be done by hand in interactive graphics programs (O, Coot) and is now largely automated: programs recognize helices and strands by template matching, place $\mathrm{C}_\alpha$ atoms and main-chain fragments, assign the sequence from side-chain density, and alternate building with refinement (ARP/wARP, Buccaneer, Phenix AutoBuild). At $2.5\,\text{Å}$ and better, with good phases, automated building gives a nearly complete model; at $3.5\,\text{Å}$ and worse it depends on prior knowledge, today often a predicted model that is fitted into the density. Ligands, metals, water molecules and alternative conformations are added in the final stages.

### 10.12.2. Refinement

Refinement adjusts the parameters of the model (coordinates, B-factors, occupancies) to improve the agreement between calculated and observed amplitudes, while keeping the stereochemistry reasonable. The number of parameters is large: four per atom with isotropic B-factors ($x, y, z, B$), nine with anisotropic ones.

**Example 10.12.1 (Observations per Parameter)** Lysozyme has about $1000$ non-hydrogen atoms, so an isotropic model has $4000$ parameters. By Example 10.2.2 there are about $2300$ unique reflections at $3.0\,\text{Å}$, $7800$ at $2.0\,\text{Å}$ and $18\,000$ at $1.5\,\text{Å}$. At $3\,\text{Å}$ there are fewer observations than parameters, at $2\,\text{Å}$ only two per parameter. A protein model refined against X-ray data alone would be underdetermined or badly overfitted at all but atomic resolution.

The deficit is filled with prior knowledge. Bond lengths, bond angles, planarity of peptides and aromatic rings, chirality and non-bonded contacts are known from small-molecule structures (the Engh–Huber library) and enter the refinement as restraints, additional "observations" with a tolerance. The refinement minimizes

$$
E = w\,E_{\mathrm{X\text{-}ray}} + E_{\mathrm{geom}},
$$
where $E_{\mathrm{geom}}$ is a sum of squared deviations from ideal geometry, $w$ a relative weight, and $E_{\mathrm{X\text{-}ray}}$ either a least-squares residual $\sum_{\boldsymbol{h}}w_{\boldsymbol{h}}(\lvert F_{\mathrm{o}}\rvert - k\lvert F_{\mathrm{c}}\rvert)^2$ or, in modern programs (REFMAC, phenix.refine, BUSTER), the negative log-likelihood of the data given the model, which accounts for the errors and incompleteness of the model (**maximum likelihood estimation**). At low resolution the model is further restrained by NCS, by reference structures and by secondary-structure restraints; groups of atoms can be refined as rigid bodies, and collective motions of domains are described by TLS parameters (translation, libration, screw). Refinement by gradient methods has a small radius of convergence; **simulated annealing** in torsion-angle space (Brünger, 1987), a molecular-dynamics simulation at high temperature followed by slow cooling with the X-ray term as an energy ([7.6.9](/7.6.9#sec-9.11)), escapes local minima and corrects errors of several ångströms.

### 10.12.3. The R Factor and the Free R Value

The agreement of model and data is reported as the crystallographic R factor,

$$
R = \frac{\sum_{\boldsymbol{h}}\bigl\lvert\lvert F_{\mathrm{o}}(\boldsymbol{h})\rvert - k\lvert F_{\mathrm{c}}(\boldsymbol{h})\rvert\bigr\rvert}{\sum_{\boldsymbol{h}}\lvert F_{\mathrm{o}}(\boldsymbol{h})\rvert}. \tag{10.9}
$$
For a random structure of the right composition, Wilson statistics give $R = 0.59$ (acentric data); a correct, well-refined protein model has $R \approx 0.15$–$0.25$. The R factor alone cannot tell a correct model from an overfitted one, because adding parameters (more water molecules, alternative conformations, looser restraints) always lowers it, and a sufficiently flexible wrong model can be refined to a respectable $R$.

**Definition 10.12.1 (Free R Value)** The **free R value** $R_{\mathrm{free}}$ (Brünger, 1992) is the R factor computed for a test set of reflections, typically $5\,\%$ chosen at random (at least $500$–$2000$), that are excluded from refinement; the R factor for the remaining reflections is $R_{\mathrm{work}}$.

$R_{\mathrm{free}}$ is **cross-validation** ([3.3](/3.3)) applied to crystallography: it measures how well the model predicts data it has not been fitted to. Overfitting lowers $R_{\mathrm{work}}$ but not $R_{\mathrm{free}}$, which then rises; a change to the model (a new restraint weight, a parameterization of the B-factors, the addition of waters) is accepted only if it lowers $R_{\mathrm{free}}$. For well-refined structures $R_{\mathrm{free}}$ is $0.02$–$0.06$ higher than $R_{\mathrm{work}}$ and, as a rule of thumb, roughly the resolution in ångströms divided by $10$ ($R_{\mathrm{free}} \approx 0.20$ at $2\,\text{Å}$, $0.25$–$0.30$ at $3\,\text{Å}$). The test set must stay the same throughout a project and for all related crystal forms, or its reflections are no longer free.

![Overfitting in a toy refinement. "Observed" structure factors of $18$ atoms in a two-dimensional $20\times20\,\text{Å}$ cell, to $2\,\text{Å}$ (about $160$ unique reflections), with $8\,\%$ noise; $10\,\%$ of the reflections form the test set. The model has $M$ atoms with free occupancies fitted by linear least squares to the working set: first an increasing number of the true atoms (an incomplete model), then the complete model plus atoms at random positions (spurious waters). Adding real structure lowers $R_{\mathrm{work}}$ and $R_{\mathrm{free}}$ together, to the noise level of about $5\,\%$; adding spurious parameters lowers $R_{\mathrm{work}}$ towards zero as $M$ approaches the number of working observations (dashed line), while $R_{\mathrm{free}}$ rises sharply.](./plots/rfree.py)

### 10.12.4. Validation

A crystal structure is a model, and models can be wrong. Validation checks the model against the data and against prior knowledge that was not used, or used only weakly, in refinement.

- Agreement with the data: $R_{\mathrm{work}}$, $R_{\mathrm{free}}$ and their gap; the real-space correlation between the model density and the $2mF_{\mathrm{o}} - DF_{\mathrm{c}}$ map for every residue and ligand; the absence of significant features in the difference map.
- Geometry: rms deviations of bond lengths (about $0.01\,\text{Å}$) and angles (about $1$–$1.5^\circ$) from ideal values. These are restrained and therefore not independent evidence; very small deviations at low resolution indicate over-tight restraints.
- Conformation: the **Ramachandran plot** ([7.1.5](/7.1.5)) is not restrained in most refinements and is a sensitive test; a good structure has more than $98\,\%$ of residues in favoured regions and very few outliers. Side-chain rotamers, the planarity of peptides, cis-peptides, and the packing of atoms (all-atom contacts and clashes, MolProbity) are checked as well.
- B-factors and occupancies: the B-factor of an atom should be similar to those of its bonded neighbours; a ligand with B-factors much higher than the surrounding protein, or modelled into weak density, is suspect.
- Biology and chemistry: the structure should explain the known function, mutations, cross-links and binding data; unexpected differences from related structures need an explanation.

The wwPDB validation report places each deposited structure among others at similar resolution. Errors that pass all automatic tests still occur: in 2006, five papers reporting structures of the **ABC transporter** MsbA and of the multidrug transporter EmrE had to be retracted when it emerged that a home-written data-processing program had swapped two columns of the data, inverting the hand of the maps; the resulting models had the wrong topology, yet had been refined to plausible statistics at low resolution. The case is a reminder that low-resolution models are mostly prior knowledge, and that independent checks, such as comparison with related structures and biochemical data, are part of the method.

The precision of a model is often better than its resolution suggests: coordinates of well-ordered atoms in a $2\,\text{Å}$ structure are typically precise to $0.1$–$0.2\,\text{Å}$ (estimated by Cruickshank's diffraction-component precision index or from Luzzati plots), because each atom is defined by the whole data set and by the restraints, not by one Fourier term.

## 10.13. Beyond the Static Crystal

### 10.13.1. X-Ray Free-Electron Lasers

**Definition 10.13.1 (X-Ray Free-Electron Laser)** An **X-ray free-electron laser** (XFEL) generates X-ray pulses by passing a bunch of electrons accelerated to GeV energies by a linear accelerator through a long undulator, in which the interaction of the electrons with their own radiation groups them into microbunches spaced by the wavelength (self-amplified spontaneous emission), so that they radiate coherently.

In an ordinary undulator the electrons radiate independently and the power grows as the number of electrons $N_{\mathrm{e}}$; in an XFEL the microbunched electrons radiate in phase, and the power grows as $N_{\mathrm{e}}^2$. The pulses last $1$–$50\,\mathrm{fs}$, contain about $10^{12}$ photons, are almost fully transversely coherent and have a peak brightness about $10^9$ times that of a synchrotron. The first hard XFEL, LCLS at Stanford, began operation in 2009, followed by SACLA (Japan, 2011), PAL-XFEL (Korea), SwissFEL, and the European XFEL (2017); in Shanghai, a soft X-ray FEL is operating and the hard X-ray facility SHINE is under construction.

A focused XFEL pulse destroys any sample it hits: the dose reaches gigagrays, the atoms are ionized, and the sample explodes by Coulomb repulsion within about $100\,\mathrm{fs}$. But a pulse of a few femtoseconds is over before the atoms have moved appreciably. This principle of diffraction before destruction (Neutze and colleagues, 2000) means that each pulse records a diffraction pattern of an essentially undamaged sample, after which the sample is gone.

### 10.13.2. Serial Femtosecond Crystallography

**Definition 10.13.2 (Serial Femtosecond Crystallography)** **Serial femtosecond crystallography** (SFX) records diffraction snapshots from a stream of micro- or nanocrystals delivered across the XFEL beam (in a liquid jet, a viscous extruder or on a fixed target), one still image per crystal and pulse, and merges tens of thousands of such snapshots from randomly oriented crystals into one data set.

Each snapshot records only the reflections that happen to touch the Ewald sphere, and only partially, because the crystal is stationary during the pulse; the images are indexed one by one, and the partiality is averaged out by merging very many of them (Monte Carlo integration) or modelled explicitly. The first SFX experiment (Chapman and colleagues, 2011) used nanocrystals of photosystem I. SFX gives structures free of radiation damage, which matters for metalloproteins such as **photosystem II** and cytochrome oxidases, at room temperature, which is closer to physiological conditions and reveals conformational heterogeneity hidden by cryocooling, and from crystals too small for synchrotrons. The serial approach has been transferred to synchrotrons (serial synchrotron crystallography) with micro-focus beams and fast detectors, and to electron diffraction of nanocrystals (microcrystal electron diffraction, [7.6.14](/7.6.14)).

### 10.13.3. Time-Resolved Crystallography

Proteins work by changing their structure, and a crystal structure is an average over time. Time-resolved crystallography triggers a reaction in all molecules of a crystal at once and records the structure at defined delays, in a pump–probe scheme.

- Light-driven proteins are triggered with a laser pulse. Laue crystallography at synchrotrons, with $100\,\mathrm{ps}$ X-ray pulses, followed the dissociation of carbon monoxide from myoglobin and the photocycle of photoactive yellow protein in the 1990s and 2000s. At XFELs the time resolution reaches $100\,\mathrm{fs}$: the isomerization of the chromophore of photoactive yellow protein, the retinal isomerization and proton pumping of bacteriorhodopsin, and the steps of water oxidation in photosystem II (driven by successive flashes) have been followed at near-atomic resolution.
- Enzymes without a natural light switch are triggered by rapidly mixing microcrystals with substrate just before they reach the beam (mix-and-inject), by photocaged substrates, by temperature jumps or electric fields.

The difference electron density between the triggered and the dark state, $\Delta\rho$ with coefficients $\lvert F_{\mathrm{light}}\rvert - \lvert F_{\mathrm{dark}}\rvert$ and dark-state phases, reveals the changes; since only a fraction of the molecules is triggered, intermediate structures are extracted by extrapolation or by singular value decomposition of a time series of difference maps, and the time evolution is fitted with kinetic models of the kind discussed in [7.6.3](/7.6.3). Related approaches, multi-temperature and room-temperature crystallography, ensemble refinement and diffuse scattering, extract the conformational heterogeneity that the static average conceals.

The ultimate goal of XFELs, imaging single molecules without crystals, has not reached atomic resolution: the diffraction of one molecule per pulse is too weak and the orientations unknown. The classification and orientation problems are the same as those solved by single-particle cryo-electron microscopy, which has taken over most of the work for large single particles ([7.6.14](/7.6.14)).

### 10.13.4. Crystallography among the Structural Methods

| | X-ray crystallography | NMR | Cryo-EM | SAXS |
|---|---|---|---|---|
| Sample | ordered crystal | concentrated solution, $\lesssim 50\,\mathrm{kDa}$ (larger with labelling) | vitrified solution, $\gtrsim 50\,\mathrm{kDa}$ | dilute solution, any size |
| Typical resolution | $1$–$3\,\text{Å}$, down to $0.5\,\text{Å}$ | atomic restraints | $2$–$4\,\text{Å}$ | $10$–$30\,\text{Å}$ (shape) |
| Dynamics | averaged; time-resolved with triggers | timescales from ps to s | discrete states by classification | ensembles, kinetics |
| Main difficulty | crystallization, phases | size, overlap of signals | particle size, preferred orientation, heterogeneity | low information content |

Crystallography is the most precise of the methods, works for any size from small peptides to ribosomes and viruses, and is fast once crystals exist, which makes it the method of choice for ligand complexes and drug design. Its limitations are the need for crystals, the static and sometimes perturbed picture (crystal contacts, cryocooling) and the difficulty with flexible and heterogeneous assemblies, where cryo-electron microscopy ([7.6.14](/7.6.14)), NMR ([7.6.13](/7.6.13)) and SAXS ([7.6.9](/7.6.9)) are stronger; the methods are increasingly combined, with predicted models as a common starting point ([7.6.15](/7.6.15)).

China's contributions began with the structure of porcine insulin, solved by a Beijing collaboration at $2.5\,\text{Å}$ in 1971 and refined at $1.8\,\text{Å}$ in 1973, the first protein structure determined in China; since the 2000s, synchrotron beamlines in Shanghai and Beijing and many laboratories have made the country one of the main contributors of structures of membrane proteins and large complexes to the PDB.

## Summary

Crystals and diffraction geometry (10.1–10.2):

- A crystal is a lattice plus a motif; the unit cell has six parameters, and the contents of the asymmetric unit (Definition 10.1.2) are generated by the space group (Definition 10.1.1). Rotations of a lattice have order $1, 2, 3, 4, 6$ (Theorem 10.1.1); chiral macromolecules crystallize only in the $65$ space groups of proper operations. Solvent fills $30$–$65\,\%$ of a protein crystal (Formula 10.1.1, Example 10.1.1).
- Diffraction occurs when the scattering vector equals a reciprocal-lattice vector, $\boldsymbol{S} = \boldsymbol{H}_{hkl}$ (Theorem 10.2.1, Definition 10.2.1); $\boldsymbol{H}_{hkl}$ is normal to the planes $(hkl)$ with $\lvert\boldsymbol{H}\rvert = 1/d$ (Proposition 10.2.1), which gives Bragg's law $2d\sin\theta = \lambda$ (Theorem 10.2.2) and the Ewald construction (Definition 10.2.2). The number of reflections to resolution $d$ is $\frac{4\pi}{3}V/d^3$ (Eq. (10.4), Example 10.2.2).

Intensities, density and phases (10.3–10.5):

| Quantity | Expression | Reference |
|---|---|---|
| Atomic scattering factor | transform of the atom, $f(0) = Z$ | Definition 10.3.1 |
| Structure factor | $F(\boldsymbol{h}) = \sum_jf_j\mathrm{e}^{2\pi\mathrm{i}\boldsymbol{h}\cdot\boldsymbol{x}_j}$ | Definition 10.3.2, Remark 10.3.1 |
| Integrated intensity | $\propto I_0r_{\mathrm{e}}^2\lambda^3V_x\lvert F\rvert^2/V^2$ | Formula 10.3.1 |
| Electron density | $\rho(\boldsymbol{x}) = \frac1V\sum_{\boldsymbol{h}}\lvert F\rvert\cos(2\pi\boldsymbol{h}\cdot\boldsymbol{x} - \varphi)$ | Theorem 10.3.1 |
| Temperature factor | $f\,\mathrm{e}^{-B\sin^2\theta/\lambda^2}$, $B = 8\pi^2\langle u^2\rangle$ | Definition 10.3.3 |
| Friedel's law | $F(-\boldsymbol{h}) = F(\boldsymbol{h})^*$ without anomalous scattering | Theorem 10.3.2 |
| Patterson function | $\frac1V\sum\lvert F\rvert^2\cos 2\pi\boldsymbol{h}\cdot\boldsymbol{u}$ = autocorrelation of $\rho$ | Definition 10.4.1, Theorem 10.4.1 |
| Direct methods | Sayre equation, triplets, tangent formula | Theorem 10.4.2 |
| Helix transform | $J_n(2\pi Rr)$ on layer lines, selection rule $l = vn + um$ | Theorem 10.5.1 |

- The crystal samples the molecular transform at the reciprocal lattice (10.3.2); amplitudes are measured, phases are not, and phases carry most of the structure (10.3.4). Resolution sets what the map shows (10.3.5); fractional translations cause systematic absences (10.3.7).
- Fiber diffraction gave the α helix ($1.5\,\text{Å}$ meridional reflection) and the parameters of B-DNA: $3.4\,\mathrm{nm}$ repeat, $10$ units per turn, radius $1\,\mathrm{nm}$, and a missing fourth layer line from strands offset by $3/8$ of a turn (Definition 10.5.1, 10.5.3).

From crystal to model (10.6–10.13):

| Step | Key physics and quantities | Reference |
|---|---|---|
| Crystallization | supersaturation $S$, barrier $\Delta G^* \propto (\ln S)^{-2}$, metastable zone, vapor diffusion | Formula 10.6.1 |
| Data collection | synchrotrons, $100\,\mathrm{K}$, dose limit $\approx 30\,\mathrm{MGy}$, $\Delta\phi_{\max} = \frac{180^\circ}{\pi}\frac{d}{a} - \eta$ | Formula 10.7.1 |
| Processing | indexing, integration, scaling; $R_{\mathrm{meas}}$, $R_{\mathrm{pim}}$, $CC_{1/2}$, $CC^*$ | Definition 10.8.1 |
| Intensity statistics | $\langle\lvert F\rvert^2\rangle = \sum f^2$, Rayleigh/exponential law, Wilson plot slope $-2B$, twinning tests | Theorem 10.8.1, Formula 10.8.1 |
| Isomorphous replacement | $F_{\mathrm{PH}} = F_{\mathrm{P}} + F_{\mathrm{H}}$, Harker construction, Blow–Crick probabilities, figure of merit | Definition 10.9.1, Eq. (10.7) |
| Anomalous scattering | $f = f_0 + f' + \mathrm{i}f''$, Bijvoet differences $\sim\sqrt{2N_{\mathrm{A}}/N_{\mathrm{T}}}\,f''/Z_{\mathrm{eff}}$; SAD, MAD | Definitions 10.9.2–10.9.3, Formula 10.9.1 |
| Molecular replacement | rotation and translation functions, likelihood; predicted models | Definition 10.10.1, Formula 10.10.1 |
| Density modification | solvent flattening, histogram matching, NCS averaging; $\sigma_A$ weights | Algorithm 10.11.1 |
| Refinement | restraints, likelihood targets, $R$ and $R_{\mathrm{free}}$ (cross-validation) | Example 10.12.1, Definition 10.12.1 |
| Beyond static crystals | XFEL pulses of femtoseconds, diffraction before destruction, SFX, pump–probe | Definitions 10.13.1–10.13.2 |

## Questions

1. A $42\,\mathrm{kDa}$ protein crystallizes in $P2_12_12_1$ with $a = 62$, $b = 78$, $c = 110\,\text{Å}$. How many molecules are there in the asymmetric unit, and what is the solvent content? About how many unique reflections are there to $2.5\,\text{Å}$?

   **Answer** $V = 5.32\times10^5\,\text{Å}^3$ and $P2_12_12_1$ has four equivalent positions. With one molecule per asymmetric unit ($Z = 4$), $V_{\mathrm{M}} = 5.32\times10^5/(4\times42\,000) = 3.17\,\text{Å}^3\,\mathrm{Da}^{-1}$ and $f_{\mathrm{solv}} = 1 - 1.23/3.17 = 0.61$; with two, $V_{\mathrm{M}} = 1.58$ and $f_{\mathrm{solv}} = 0.22$, below the range observed for proteins. One molecule, about $61\,\%$ solvent, is most likely (Formula 10.1.1); a self-rotation function or the Patterson function would confirm the absence of non-crystallographic symmetry. By Eq. (10.4), $N = \frac{4\pi}{3}\times5.32\times10^5/2.5^3 = 1.43\times10^5$ reflections in the full sphere; point group $222$ (order $4$) and Friedel's law reduce this by $8$, to about $17\,800$ unique reflections.

2. A detector of half-width $150\,\mathrm{mm}$ is centred on the beam at $200\,\mathrm{mm}$ from the crystal, and $\lambda = 1.0\,\text{Å}$. What is the highest resolution recorded at the edge of the detector? How close must the detector be to record $1.2\,\text{Å}$ data?

   **Answer** At the edge, $\tan2\theta = 150/200$, so $2\theta = 36.9^\circ$ and $d = \lambda/(2\sin18.4^\circ) = 1.58\,\text{Å}$ (Bragg's law, Theorem 10.2.2). For $d = 1.2\,\text{Å}$, $\sin\theta = 1/2.4$, $2\theta = 49.2^\circ$, and the distance must be at most $150/\tan49.2^\circ = 129\,\mathrm{mm}$. Moving the detector closer increases the background per spot and the risk of overlap for a large cell (Formula 10.7.1); a shorter wavelength is the alternative.

3. An orthorhombic crystal shows the absences $h00$ with $h$ odd, $0k0$ with $k$ odd and $00l$ with $l$ odd, and no others. What is the space group? Why can the absences never distinguish $P4_1$ from $P4_3$?

   **Answer** Three $2_1$ axes along the three axes and a primitive lattice: $P2_12_12_1$ (10.3.7); if only $00l$ were absent it would be $P222_1$, if none $P222$. $P4_1$ and $P4_3$ are mirror images: the screw axes translate by $c/4$ per quarter turn in opposite senses, and both give $00l$ absent unless $l = 4n$. Their diffraction intensities are identical by Friedel's law; only the solved structure (the right hand of the α helices) or anomalous differences distinguish them.

4. By what factor does the average intensity at $2.0\,\text{Å}$ resolution fall when the overall B-factor of a crystal increases from $15$ to $30\,\text{Å}^2$? What rms displacement does $B = 30\,\text{Å}^2$ represent?

   **Answer** $\langle I\rangle \propto \exp(-2Bs^2)$ with $s = \sin\theta/\lambda = 1/(2d) = 0.25\,\text{Å}^{-1}$ (Formula 10.8.1). Increasing $B$ by $15\,\text{Å}^2$ multiplies the intensity by $\exp(-2\times15\times0.0625) = 0.15$, a factor of about $6.5$ weaker, and the resolution limit moves outward accordingly. The rms displacement along one direction is $\sqrt{30/8\pi^2} = 0.62\,\text{Å}$ (Definition 10.3.3).

5. In $P2_1$ (screw axis along $\boldsymbol{b}$), a mercury atom sits at $(0.12, y, 0.31)$. Where is its Harker peak in the Patterson function, and why can its $y$ coordinate not be determined from that peak?

   **Answer** The atom and its symmetry mate $(-x, y + \frac12, -z)$ give the vector $(2x, \frac12, 2z) = (0.24, 0.5, 0.62)$, in the Harker section $v = \frac12$ (10.4.2). Its $y$ coordinate cancels in the difference. Moreover, $y$ is not even defined in absolute terms: in $P2_1$ the origin can be placed anywhere along the $2_1$ axis (a polar axis), so the $y$ coordinate of the first atom is chosen arbitrarily, and those of the other atoms are fixed relative to it by cross-vectors.

6. For one reflection, $\lvert F_{\mathrm{P}}\rvert = 100$, the heavy-atom contribution is $F_{\mathrm{H}} = 30\,\mathrm{e}^{\mathrm{i}200^\circ}$ and $\lvert F_{\mathrm{PH}}\rvert = 79.4$. Find the possible phases of $F_{\mathrm{P}}$.

   **Answer** By Eq. (10.7), $\cos(\varphi_{\mathrm{P}} - \varphi_{\mathrm{H}}) = (79.4^2 - 100^2 - 30^2)/(2\times100\times30) = -0.766$, so $\varphi_{\mathrm{P}} - \varphi_{\mathrm{H}} = \pm140^\circ$ and $\varphi_{\mathrm{P}} = 340^\circ$ or $60^\circ$ ($= -20^\circ$ or $60^\circ$). These are the two intersections of the Harker figure in 10.9.1; a second derivative or the anomalous signal of the same derivative (SIRAS) selects $60^\circ$.

7. A $300$-residue protein is expressed as the selenomethionine variant with five methionines. Estimate the Bijvoet ratio at the Se peak. What does this imply for the data collection?

   **Answer** $N_{\mathrm{T}} \approx 7.8\times300 = 2340$ non-hydrogen atoms, $N_{\mathrm{A}} = 5$, $f'' \approx 3.8$: by Formula 10.9.1, $\sqrt{10/2340}\times3.8/6.7 = 3.7\,\%$ (rms). Individual intensities are measured with errors of a few percent, so the signal must be measured accurately: collect at the peak wavelength found by a fluorescence scan, with high multiplicity (several hundred degrees of rotation, possibly inverse-beam geometry so that Bijvoet mates are measured close in time), with low dose per frame to limit radiation damage, and to the resolution at which the anomalous correlation between half data sets remains significant.

8. The α helix has $3.6$ residues per turn and a pitch of $5.4\,\text{Å}$. Using the selection rule, predict the layer lines and the meridional reflection of an α-helical fiber.

   **Answer** $18$ residues make $5$ turns, so $u = 18$, $v = 5$, the repeat is $c = 27\,\text{Å}$ and the layer lines lie at $Z = l/27\,\text{Å}^{-1}$ with $l = 5n + 18m$ (Theorem 10.5.1). The $J_0$ term, the only one non-zero on the meridian, appears on $l = 18m$, at $Z = 18/27 = 1/1.5\,\text{Å}^{-1}$: a meridional reflection at $1.5\,\text{Å}$, the rise per residue. The strongest off-meridional intensity is on $l = 5$ ($n = 1$), at $Z = 1/5.4\,\text{Å}^{-1}$, the layer line of the pitch, with its first maximum at $2\pi Rr = 1.84$. This is the $1.5\,\text{Å}$ reflection Perutz found in 1951 (10.5.3).

9. With $\gamma' = 6\,k_{\mathrm{B}}T$, by how much does the nucleation barrier change when the supersaturation is raised from $S = 2$ to $S = 4$, and by what factor does the nucleation rate change? What does this mean for setting up crystallization drops?

   **Answer** $\Delta G^* = 4\gamma'^3/(27(\ln S)^2) = 32\,k_{\mathrm{B}}T/(\ln S)^2$ (Formula 10.6.1): $66.6\,k_{\mathrm{B}}T$ at $S = 2$ and $16.7\,k_{\mathrm{B}}T$ at $S = 4$. The rate changes by $\mathrm{e}^{49.9} \approx 5\times10^{21}$. Nucleation is thus practically switched off below a threshold supersaturation and explosive above it: drops slightly too concentrated give showers of microcrystals, slightly too dilute ones nothing. Vapor diffusion slowly crosses the boundary, and seeding into metastable drops decouples nucleation from growth.

10. A $2.0\,\text{Å}$ structure is reported with $R_{\mathrm{work}} = 0.18$ and $R_{\mathrm{free}} = 0.32$. What does the gap suggest, and what would you check? Why must the test set be chosen before any refinement and kept for all later work on the same crystal form?

    **Answer** For a well-refined $2\,\text{Å}$ structure $R_{\mathrm{free}}$ should be about $0.20$–$0.25$ with a gap of $0.02$–$0.06$ (10.12.3). A gap of $0.14$ indicates overfitting (too many parameters, such as many waters or alternative conformations, or loose geometry restraints) or parts of the model that are wrong but have been fitted to the working data. One would check the restraint weights and the B-factor model, the Ramachandran plot and difference maps, real-space correlations residue by residue, possible twinning or a wrong space group, and the test set itself. The test set is free only if no step of model building or refinement has used it; reflections that were once in the working set retain the memory of the model (the model was fitted to them), and their R value no longer measures prediction. Choosing a new test set later therefore gives an optimistic $R_{\mathrm{free}}$.

11. Explain why $R_{\mathrm{merge}}$ increases with the multiplicity of the data even though the merged intensities become more accurate, and which statistic should be used to choose the resolution limit.

    **Answer** $R_{\mathrm{merge}}$ sums deviations of single observations from the mean of $n$ observations; for small $n$ the mean is closer to each observation than the true value is, by the factor $\sqrt{(n-1)/n}$, so $R_{\mathrm{merge}}$ is biased low for small multiplicity and rises toward the precision of single observations as $n$ increases (Definition 10.8.1, data-quality figure). $R_{\mathrm{meas}}$ removes the bias, and $R_{\mathrm{pim}}$ measures the merged data, falling as $1/\sqrt{n-1}$. The resolution limit is best chosen from $CC_{1/2}$ (significant correlation, typically down to about $0.3$) and $\langle I/\sigma(I)\rangle$ of the merged data, ideally confirmed by paired refinement: extending the data is justified if it does not worsen $R_{\mathrm{free}}$ at the previous resolution.

12. (Open question) Why has single-wavelength anomalous diffraction largely replaced both multiple isomorphous replacement and MAD, and why has molecular replacement with predicted models in turn replaced most experimental phasing? What is still lost when phases come only from a model?

    **Answer** MIR needs several derivatives isomorphous with the native crystal, which is laborious and often fails because heavy atoms change the cell; anomalous methods use one crystal and so have perfect isomorphism. MAD needs several data sets from the same crystal at precise wavelengths and suffers from radiation damage between them; SAD needs one data set, and its twofold ambiguity is removed by density modification, which works well with accurate data from photon-counting detectors (10.9.3, 10.11). Predicted models from AlphaFold are now close enough to most targets for molecular replacement (10.10), which needs no derivatives at all. But model phases bias the map toward the model (10.3.4): features absent from the model (a new ligand, an unexpected conformation, a different arrangement of domains) appear only weakly, and errors in the model can survive refinement. Experimental phases give an unbiased map; with model phases, bias must be controlled by $\sigma_A$-weighted maps, omit maps, and validation against $R_{\mathrm{free}}$ and independent data.
