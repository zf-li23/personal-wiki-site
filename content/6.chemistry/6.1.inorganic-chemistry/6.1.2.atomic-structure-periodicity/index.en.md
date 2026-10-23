---
title: Atomic Structure and Periodicity
description: The nuclear atom; the hydrogen spectrum, Bohr theory and a review of wave–particle duality; chemical representations of atomic orbitals (real orbitals, radial nodes and nodal planes, electron clouds, angular distribution plots); the four quantum numbers; shielding, effective nuclear charge and Slater's rules, penetration and energy level crossing; electron configurations, periods and groups, blocks; periodic trends of atomic radius, lanthanide contraction, ionization energy, electron affinity and electronegativity.
source_hash: 635df197b49e
---

In a chemical reaction the nucleus is unchanged and only the state of the extranuclear electrons changes, so atomic structure is the starting point for understanding chemical bonds, molecular structure and the properties of the elements. The quantum-mechanical treatment of the hydrogen atom (the solution of the Schrödinger equation, quantum numbers, electron clouds and radial probability distributions, electron spin, the Pauli principle and the basic rules for electron configurations) has already been given systematically in the quantum part of physics ([5.5.3](/5.5.3), [5.5.4](/5.5.4)). Sections 2.1–2.2 of this chapter only review it and concentrate on how atomic orbitals are used in chemistry: real atomic orbitals, angular distribution plots with their signs, nodes and nodal planes, which are the language of valence bond theory and molecular orbital theory in the next chapter ([6.1.3](/6.1.3)). Section 2.3 treats many-electron atoms: how shielding and penetration determine the order of energy levels, and from this the electron configurations and the structure of the periodic table. Section 2.4 uses the effective nuclear charge to explain the periodic variation of atomic radius, ionization energy, electron affinity and electronegativity, regularities that run through all later chapters on the properties of the elements ([6.1.13](/6.1.13)–[6.1.15](/6.1.15)). The self-consistent field method for many-electron atoms, atomic term symbols and relativistic effects belong to structural chemistry ([6.2](/6.2)).

## 2.1. The Nuclear Model of the Atom

In 1803 Dalton proposed the chemical atomic theory: elements consist of indivisible atoms, atoms of the same element have the same mass, and compounds are formed by atoms of different elements combining in simple whole-number ratios. At the end of the 19th century cathode rays (Crookes, 1879), the charge-to-mass ratio of the electron (Thomson, 1897) and the discovery of radioactivity showed that atoms are divisible; Millikan's oil-drop experiment (1909) determined the charge of the electron. Thomson pictured the atom as a sphere of uniformly distributed positive charge with electrons embedded in it (the "plum pudding" model).

In 1909–1911 Geiger and Marsden bombarded gold foil with $\alpha$ particles and found that a very few $\alpha$ particles were scattered through large angles or even bounced back, and Rutherford accordingly proposed the nuclear model of the atom: at the center of the atom is a very small nucleus that holds all the positive charge and almost all the mass (the radius of the nucleus is about $10^{-15}$–$10^{-14}\,\mathrm{m}$, only one ten-thousandth of that of the atom), and the electrons move in the large space outside the nucleus. In 1913 Moseley measured the **characteristic X-rays** of the elements and found that the frequency of the $\mathrm{K}_\alpha$ line satisfies $\sqrt{\nu} \propto Z - 1$ (**Moseley's law**, [5.5.5](/5.5.5#sec-5.1.3)), which established that the nuclear charge number is the position of the element in the periodic table, the *atomic number* $Z$. Rutherford then established the concept of the proton (1919–1920) and Chadwick discovered the neutron (1932): an atom consists of a nucleus of protons and neutrons and the electrons outside it. Atoms with the same number of protons but different numbers of neutrons are *isotopes* of one another, and their chemical properties are almost identical.

The nuclear model brought a new difficulty: according to classical electrodynamics an electron orbiting the nucleus is accelerated and should radiate electromagnetic waves continuously, lose energy and spiral into the nucleus within about $10^{-11}\,\mathrm{s}$; the light emitted by atoms should also have a continuous spectrum. In fact atoms are stable and their spectra are line spectra. Resolving this contradiction required quantum theory.

## 2.2. The Motion of Electrons Outside the Nucleus

### 2.2.1. The Hydrogen Spectrum and Bohr Theory

The emission spectrum of the hydrogen atom consists of a series of discrete lines, four of them in the visible region ($\mathrm{H}_\alpha$ $656.3\,\mathrm{nm}$, $\mathrm{H}_\beta$ $486.1\,\mathrm{nm}$, $\mathrm{H}_\gamma$ $434.0\,\mathrm{nm}$, $\mathrm{H}_\delta$ $410.2\,\mathrm{nm}$). Balmer (1885) found that their wavelengths satisfy $\lambda = B\,\frac{n^2}{n^2 - 4}$ ($B = 364.56\,\mathrm{nm}$, $n = 3, 4, 5, 6$), and Rydberg (1888–1890) generalized it to a formula valid for all spectral series:

$$
\frac{1}{\lambda} = R_{\mathrm{H}}\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \qquad n_2 > n_1,
$$
where $R_{\mathrm{H}} = 1.0968 \times 10^7\,\mathrm{m^{-1}}$ is the **Rydberg constant** of hydrogen. The values $n_1 = 1, 2, 3, 4, 5$ correspond to the Lyman series in the ultraviolet, the **Balmer series** in the visible, and the Paschen, Brackett and Pfund series in the infrared ([5.5.4](/5.5.4#sec-4.1.1)).

Bohr (1913) combined Planck's energy quantization with Rutherford's nuclear model, assuming that the electron can move without radiating only on circular orbits with angular momentum $m_{\mathrm{e}}vr = n\hbar$, and that in a transition between two stationary states it emits or absorbs a photon of energy $h\nu = E_2 - E_1$ (the **Bohr model**, [5.5.4](/5.5.4#sec-4.1.3)). For a one-electron atom of nuclear charge $Z$ (hydrogen and hydrogen-like ions $\ce{He+}$, $\ce{Li^2+}$, etc.) the orbit radius and energy are

$$
r_n = \frac{n^2}{Z}a_0, \qquad E_n = -\frac{Z^2}{n^2} \times 13.6\,\mathrm{eV} = -\frac{Z^2}{n^2} \times 1312\,\mathrm{kJ\,mol^{-1}},
$$
where the **Bohr radius** is $a_0 = 52.9\,\mathrm{pm}$; chemists commonly use molar energies, and $1\,\mathrm{eV}$ corresponds to $96.485\,\mathrm{kJ\,mol^{-1}}$. For the hydrogen atom $E_1 = -1312\,\mathrm{kJ\,mol^{-1}}$, $E_2 = -328.0\,\mathrm{kJ\,mol^{-1}}$ and $E_3 = -145.8\,\mathrm{kJ\,mol^{-1}}$.

Bohr theory successfully explained the spectra of hydrogen and hydrogen-like ions, calculated the Rydberg constant and introduced the concept of energy levels; but it cannot explain the spectra of many-electron atoms, the fine structure of spectral lines or their splitting in a magnetic field. Its fundamental flaw is that quantization conditions are imposed artificially on a classical picture of orbits, without recognizing the wave nature of the electron.

**Example 2.2.1** Find the ionization energy of hydrogen from the hydrogen spectrum.

Solution: The series limit of the Lyman series ($n_1 = 1$, $n_2 \to \infty$) corresponds to moving the electron from the ground state to infinity, $\tilde\nu = R_{\mathrm{H}}$, and the frequency is $\nu = R_{\mathrm{H}}c = 1.0968 \times 10^7\,\mathrm{m^{-1}} \times 2.9979 \times 10^8\,\mathrm{m\,s^{-1}} = 3.288 \times 10^{15}\,\mathrm{s^{-1}}$. The ionization energy of one atom is $h\nu = 2.179 \times 10^{-18}\,\mathrm{J}$, and multiplying by $N_{\mathrm{A}}$ gives $1312\,\mathrm{kJ\,mol^{-1}}$ ($13.6\,\mathrm{eV}$). Similarly $E_n = -2.179 \times 10^{-18}\,\mathrm{J}/n^2$.

### 2.2.2. Wave–Particle Duality and the Uncertainty Relation

Light is both a wave and made of **photons** ($E = h\nu$, $p = h/\lambda$); de Broglie (1924) proposed that material particles also have wave properties, a particle of momentum $p = mv$ corresponding to a **matter wave** of wavelength $\lambda = h/(mv)$, a prediction confirmed by the electron diffraction experiment of Davisson and Germer (1927) ([5.5.2](/5.5.2#sec-2.1)). **Wave–particle duality** is the fundamental characteristic of microscopic particles.

**Example 2.2.2** What are the **de Broglie wavelengths** of an electron with speed $5.9 \times 10^5\,\mathrm{m\,s^{-1}}$ and a bullet of mass $10\,\mathrm{g}$ with speed $1000\,\mathrm{m\,s^{-1}}$?

Solution: For the electron $\lambda = \dfrac{6.626 \times 10^{-34}}{9.109 \times 10^{-31} \times 5.9 \times 10^5}\,\mathrm{m} = 1.23 \times 10^{-9}\,\mathrm{m} = 1.23\,\mathrm{nm}$, of the same order as the distances between atoms in crystals, so electrons can be diffracted by crystals; for the bullet $\lambda = 6.6 \times 10^{-35}\,\mathrm{m}$, too small to observe, and the wave nature of macroscopic objects can be neglected.

The **Heisenberg uncertainty relation** (1927) $\Delta x\,\Delta p_x \ge \hbar/2$ ($= h/(4\pi)$) states that the position and momentum of a particle cannot both have definite values at the same time ([5.5.2](/5.5.2#sec-2.3)). An electron in an atom is confined to a region of $\Delta x \approx 0.1\,\mathrm{nm}$, so the uncertainty in its velocity is at least $\Delta v \ge \frac{h}{4\pi m_{\mathrm{e}}\Delta x} \approx 6 \times 10^5\,\mathrm{m\,s^{-1}}$, of the same order as the speed of the electron in the hydrogen atom (about $2.2 \times 10^6\,\mathrm{m\,s^{-1}}$). The electrons in atoms therefore cannot have definite orbits as in the Bohr model, and their motion can only be characterized by wave functions that describe probability distributions.

### 2.2.3. Wave Functions and Atomic Orbitals

The state of a microscopic particle is described by the **wave function** $\psi$, where $\lvert\psi\rvert^2$ is the probability density of finding the particle at a point in space; stationary-state wave functions satisfy the time-independent **Schrödinger equation** ([5.5.3](/5.5.3)). In the hydrogen atom and hydrogen-like ions the potential energy of the electron, $V = -\frac{Ze^2}{4\pi\varepsilon_0 r}$, is spherically symmetric, and the equation is solved by **separation of variables** in spherical coordinates $(r, \theta, \varphi)$ ([5.5.4](/5.5.4#sec-4.1.4)); the wave function factorizes into a radial part and an angular part:

$$
\psi_{n,l,m_l}(r, \theta, \varphi) = R_{n,l}(r)\,Y_{l,m_l}(\theta, \varphi),
$$
where $Y_{l,m_l}$ is one of the **spherical harmonics**. For the solutions to be physically meaningful (single-valued, finite and normalizable) the three parameters can take only certain integer values: the principal quantum number $n = 1, 2, 3, \dots$, the azimuthal quantum number $l = 0, 1, \dots, n - 1$ and the magnetic quantum number $m_l = 0, \pm1, \dots, \pm l$. Each allowed set $(n, l, m_l)$ corresponds to one wave function and one energy $E_n = -13.6\,\mathrm{eV} \times Z^2/n^2$. Such a one-electron wave function is called an **atomic orbital** in chemistry: it is a function that represents one state of motion of the electron, not the circular path of the Bohr model. The orbitals with $l = 0, 1, 2, 3$ are called s, p, d and f orbitals respectively (from the names of spectral series: sharp, principal, diffuse, fundamental) and, written together with $n$, 1s, 2p, 3d and so on.

The wave functions with $m_l \ne 0$ contain the factor $\mathrm{e}^{\mathrm{i}m_l\varphi}$ and are complex, for example $Y_{1,\pm1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,\mathrm{e}^{\pm\mathrm{i}\varphi}$. Orbitals with the same $n$ and $l$ but different $m_l$ show **degeneracy**, and any **linear combination** of wave functions of the same energy is still a solution of the Schrödinger equation with the same energy. Combining the pair of complex functions with $m_l = \pm\lvert m_l\rvert$ gives real functions with a definite orientation in space:

**Definition 2.2.1** The real functions obtained as linear combinations of a pair of complex atomic orbitals with $m_l$ and $-m_l$ are called **real atomic orbitals**. For the p orbitals,

$$
\mathrm{p}_z = \psi_{n,1,0}, \qquad \mathrm{p}_x = \frac{1}{\sqrt{2}}\left(\psi_{n,1,-1} - \psi_{n,1,1}\right), \qquad \mathrm{p}_y = \frac{\mathrm{i}}{\sqrt{2}}\left(\psi_{n,1,-1} + \psi_{n,1,1}\right),
$$
and their angular parts are proportional to $\cos\theta = z/r$, $\sin\theta\cos\varphi = x/r$ and $\sin\theta\sin\varphi = y/r$ respectively.

The orbitals drawn in chemistry and used in bonding theory are real atomic orbitals. Their angular parts can be written concisely in Cartesian coordinates, and the subscripts come from these expressions:

| Orbital | Angular part $Y(\theta, \varphi)$ | Origin |
|---|---|---|
| s | $\sqrt{1/(4\pi)}$ | $m_l = 0$ |
| $\mathrm{p}_z$ | $\sqrt{3/(4\pi)}\;z/r$ | $m_l = 0$ |
| $\mathrm{p}_x$, $\mathrm{p}_y$ | $\sqrt{3/(4\pi)}\;x/r$, $\sqrt{3/(4\pi)}\;y/r$ | $m_l = \pm1$ |
| $\mathrm{d}_{z^2}$ | $\sqrt{5/(16\pi)}\;(3z^2 - r^2)/r^2$ | $m_l = 0$ |
| $\mathrm{d}_{xz}$, $\mathrm{d}_{yz}$ | $\sqrt{15/(4\pi)}\;xz/r^2$, $\sqrt{15/(4\pi)}\;yz/r^2$ | $m_l = \pm1$ |
| $\mathrm{d}_{xy}$, $\mathrm{d}_{x^2-y^2}$ | $\sqrt{15/(4\pi)}\;xy/r^2$, $\sqrt{15/(16\pi)}\;(x^2 - y^2)/r^2$ | $m_l = \pm2$ |

Real orbitals still have definite $n$, $l$ and energy, but except for the orbitals with $m_l = 0$ they no longer have a definite $m_l$: $\mathrm{p}_x$ is not an "$m_l = 1$ orbital" but a superposition of the two states $m_l = \pm1$. The seven real f orbitals can be constructed in the same way, with more complicated shapes. Each shell has $n^2$ orbitals: 1 in the s subshell, 3 in the p subshell, 5 in the d subshell and 7 in the f subshell.

### 2.2.4. Probability Density, Electron Clouds and Radial Distribution

$\lvert\psi\rvert^2$ is the probability per unit volume of finding the electron near a point outside the nucleus, that is, the probability density; representing the spatial distribution of the probability density by the density of dots gives a picture called the **electron cloud** ([5.5.4](/5.5.4#sec-4.1.5)). The s electron cloud is spherically symmetric, a p cloud is dumbbell-shaped along a coordinate axis, and most d clouds are four-lobed, like petals.

When only the distance of the electron from the nucleus matters, the probability is integrated over angles. The probability of finding the electron in a thin spherical shell between radius $r$ and $r + \mathrm{d}r$ is $P_{nl}(r)\,\mathrm{d}r$, where the **radial probability density** is $P_{nl}(r) = r^2R_{nl}^2(r)$, often called the radial distribution function in Chinese textbooks and written $D(r)$; for an s orbital $\lvert\psi\rvert^2 = R^2/(4\pi)$, so $D(r) = 4\pi r^2\lvert\psi\rvert^2$, the area of the shell times the probability density. The radial probability densities of the states of the hydrogen atom are shown in the figures of [5.5.4](/5.5.4#sec-4.1.5).

The probability density of a 1s electron is largest at the nucleus, yet its radial probability density is largest at $r = a_0$; there is no contradiction: the closer to the nucleus, the larger $\lvert\psi\rvert^2$ but the smaller the volume $4\pi r^2\,\mathrm{d}r$ of the shell, while the farther from the nucleus, the larger the shell but the smaller $\lvert\psi\rvert^2$, which decreases as $\mathrm{e}^{-2r/a_0}$. The product of these two opposing factors has its maximum at $a_0$, which is exactly the Bohr radius.

Where the wave function is zero, the probability of finding the electron is zero. The zeros of $\psi = R(r)Y(\theta, \varphi)$ are of two kinds:

**Definition 2.2.2** The zeros of the radial function $R_{nl}(r)$ are spherical surfaces centered on the nucleus, called **radial nodes** (radial nodal surfaces), of which there are $n - l - 1$; the zeros of the angular function $Y(\theta, \varphi)$ are planes or conical surfaces through the nucleus, called **nodal planes** (angular nodes), of which there are $l$. The total number of nodes of an orbital is $n - 1$.

For example, the 2s orbital has one radial node ($r = 2a_0$) and 3s has two ($r = 1.90a_0$ and $7.10a_0$); the nodal plane of the $\mathrm{p}_z$ orbital is the $xy$ plane, and those of $\mathrm{p}_x$ and $\mathrm{p}_y$ are the $yz$ and $xz$ planes; the two nodal planes of $\mathrm{d}_{xy}$ are the $xz$ and $yz$ planes, those of $\mathrm{d}_{x^2-y^2}$ are the two planes $x = \pm y$, while the two angular nodes of $\mathrm{d}_{z^2}$ are conical surfaces of apex angle $2 \times 54.7^\circ$ ($3\cos^2\theta = 1$). The more nodes, the more rapidly the wave function oscillates and the greater the kinetic energy, the same rule as for standing waves in a one-dimensional potential well ([5.5.3](/5.5.3)).

![Wave functions ψ of hydrogen orbitals in the xz plane (red positive, blue negative; length unit a0). Radial nodes appear as circles (2s, 3s, 3p) and nodal planes or cones as straight lines through the nucleus (2p, 3p, 3d)](./plots/orbital-maps.py)

The radial probability density reflects the layered distribution of electrons: the larger $n$, the farther the main peak from the nucleus. An orbital with $l = n - 1$ (1s, 2p, 3d, …) has only one maximum, at $r = n^2a_0$ (for hydrogen, 2p at $212\,\mathrm{pm}$ and 3d at $476\,\mathrm{pm}$); the outermost maximum of the other orbitals is farther out, about $5.2a_0$ for 2s and about $13.1a_0$ for 3s. At the same time, for the same $n$ the smaller $l$ is, the more small peaks the radial distribution has inside the main peak and the closer to the nucleus it extends:

**Definition 2.2.3** The phenomenon in which the radial distribution of an outer electron extends partly into the region occupied by inner electrons and close to the nucleus is called the **penetration effect**. Within the same shell the order of penetrating power is $n\mathrm{s} > n\mathrm{p} > n\mathrm{d} > n\mathrm{f}$.

In the hydrogen atom penetration does not affect the energy (the energy depends only on $n$); in many-electron atoms penetration reduces the shielding of an electron by inner electrons and is the cause of the splitting and crossing of energy levels (Section 2.3.1).

### 2.2.5. Angular Distribution Plots

The angular part of the wave function, $Y(\theta, \varphi)$, depends only on $l$ and $m_l$ and not on $n$: the angular parts of 2p, 3p and 4p are the same. The angular distribution plot of an atomic orbital is drawn as follows: from the origin draw rays in all directions and on each ray mark the point at a distance equal to $\lvert Y(\theta, \varphi)\rvert$ in that direction; all these points form a surface, and each part of the surface is labeled with the sign of $Y$. For example, for $\mathrm{p}_z$, $Y = \sqrt{3/(4\pi)}\cos\theta$, which in any plane containing the $z$ axis is two circles tangent at the origin (in three dimensions, two tangent spheres), positive above and negative below.

Plotting $\lvert Y\rvert^2$ in the same way gives the angular distribution plot of the electron cloud. The two kinds of plot differ in two respects: the electron cloud plot has no signs; and squaring makes the directions with smaller $\lvert Y\rvert$ relatively smaller, so the lobes of the electron cloud plot are "thinner" than those of the orbital plot and more concentrated in the direction of the maximum.

![Angular distributions in the xz plane: the orbital angular function Y (top, with signs) and the electron-cloud angular function |Y|² (bottom) for s, pz, dz² and dxz](./plots/angular-distribution.py)

![Angular distribution surfaces |Y(θ, φ)| of the three real p orbitals and five real d orbitals, coloured by the sign of Y (red positive, blue negative)](./plots/real-orbitals-3d.py)

Two points should be noted about these plots:

1. The "+" and "−" on the angular distribution plot are the sign (phase) of the wave function in that region and do not indicate positive or negative charge. Their significance appears in bonding: when parts of two atomic orbitals of the same sign overlap, the wave functions add and the electron density between the nuclei increases, forming a chemical bond; when parts of opposite sign overlap, they cancel ([6.1.3](/6.1.3)). A wave function multiplied overall by $-1$ describes the same state, so only relative signs are meaningful.
2. The angular distribution plot shows only how the wave function varies with direction, and is not the actual shape of the electron cloud. The spatial distribution of the electron cloud is determined by the radial and angular parts together: the angular distribution plots of 2p and 3p are identical, but each lobe of the 3p electron cloud is divided by a radial node into an inner and an outer layer (the $\psi$ contour plots above). Taking the angular distribution plot for the actual shape of the electron cloud is a common misconception.

### 2.2.6. The Four Quantum Numbers

The three quantum numbers $n$, $l$ and $m_l$ determine an atomic orbital. To explain the fine structure of spectra and the **Stern–Gerlach experiment** (1922), Uhlenbeck and Goudsmit (1925) proposed **electron spin**, which introduces a fourth quantum number, the **spin magnetic quantum number** $m_s$ ([5.5.4](/5.5.4#sec-4.4.1)). The four quantum numbers completely determine the state of motion of an electron in an atom:

| Quantum number | Values | Physical meaning | Chemical meaning |
|---|---|---|---|
| **Principal quantum number** $n$ | $1, 2, 3, \dots$ | Determines the energy of the hydrogen atom; determines the mean distance of the electron from the nucleus | Electron shell: $n = 1, 2, 3, 4, 5, 6, 7$ are labeled K, L, M, N, O, P, Q; the main factor determining the energy in many-electron atoms |
| **Azimuthal quantum number** $l$ | $0, 1, \dots, n - 1$ | Orbital angular momentum $L = \sqrt{l(l+1)}\,\hbar$ | Subshell s, p, d, f; determines the shape of the orbital; affects the energy in many-electron atoms, $E_{n\mathrm{s}} < E_{n\mathrm{p}} < E_{n\mathrm{d}} < E_{n\mathrm{f}}$ for the same $n$ |
| **Magnetic quantum number** $m_l$ | $0, \pm1, \dots, \pm l$ | $z$ component of the orbital angular momentum $L_z = m_l\hbar$ | Orientation of the orbital in space, with $2l + 1$ orbitals in each subshell; independent of energy in the absence of an external magnetic field |
| Spin magnetic quantum number $m_s$ | $+\frac{1}{2}$, $-\frac{1}{2}$ | $z$ component of the spin angular momentum $S_z = m_s\hbar$ | Two spin states, often denoted ↑ and ↓ |

(Some textbooks write $m_l$ as $m$.) In the absence of an external magnetic field the $2l + 1$ orbitals of one subshell have the same energy and are called degenerate (equivalent) orbitals; in an external magnetic field their energies differ slightly (the **Zeeman effect**). By the Pauli principle (Section 2.3.2) each orbital holds at most two electrons of opposite spin, so the s, p, d and f subshells hold at most 2, 6, 10 and 14 electrons respectively, and shell $n$ holds at most $2n^2$.

**Example 2.2.3** Which of the following combinations of quantum numbers $(n, l, m_l, m_s)$ are not allowed? (a) $(2, 1, 0, +\frac{1}{2})$; (b) $(2, 2, -1, -\frac{1}{2})$; (c) $(3, 0, +1, +\frac{1}{2})$; (d) $(4, 3, -3, -\frac{1}{2})$.

Solution: In (b) $l$ must be less than $n$; in (c) $m_l$ can only be 0 when $l = 0$. (a) is a 2p electron and (d) is a 4f electron, both allowed.

## 2.3. Electron Configurations and the Periodic System

### 2.3.1. Energy Levels in Many-Electron Atoms

In a many-electron atom each electron is attracted by the nucleus and repelled by the other electrons, and the Schrödinger equation cannot be solved exactly. The usual approximation is to average the effect of the other electrons on a given electron into a spherically symmetric potential field, in which each electron moves independently in the field of the nucleus and this average field. In this approximation the state of an electron can still be labeled by $n$, $l$, $m_l$ and $m_s$, and the angular parts of the orbitals are the same as for hydrogen, but the energy depends on $l$ as well as on $n$.

**Definition 2.3.1** In a many-electron atom, the electron clouds of the other electrons cancel part of the attraction of the nucleus for a given electron, which amounts to reducing the nuclear charge felt by that electron; this effect is called the **shielding effect**. The nuclear charge felt by the electron is called the **effective nuclear charge** $Z_{\mathrm{eff}}$, and its difference from the nuclear charge $Z$ is called the **shielding constant** $\sigma$:

$$
Z_{\mathrm{eff}} = Z - \sigma.
$$
The potential energy of the electron is then approximately $V = -\frac{Z_{\mathrm{eff}}e^2}{4\pi\varepsilon_0 r}$ and the orbital energy takes the approximate hydrogen-like form $E \approx -13.6\,\mathrm{eV} \times Z_{\mathrm{eff}}^2/n^2$.

The strength of shielding depends on the number of shielding electrons and their orbitals, and also on the orbital of the electron being shielded: inner electrons shield outer electrons strongly, electrons in the same shell shield one another weakly, and outer electrons hardly shield inner electrons at all. The He atom is the simplest example: the electron in $\ce{He+}$ feels the whole nuclear charge and its ionization energy is $54.42\,\mathrm{eV}$ ($8.719 \times 10^{-18}\,\mathrm{J}$, $5250\,\mathrm{kJ\,mol^{-1}}$); in the He atom the two 1s electrons shield each other, and the first ionization energy is only $24.59\,\mathrm{eV}$ ($3.939 \times 10^{-18}\,\mathrm{J}$, $2372\,\mathrm{kJ\,mol^{-1}}$).

Slater (1930) summarized a set of empirical rules for estimating shielding constants:

**Definition 2.3.2 (Slater's Rules)** Group the atomic orbitals in the following order:

$$
(1\mathrm{s}),\ (2\mathrm{s}, 2\mathrm{p}),\ (3\mathrm{s}, 3\mathrm{p}),\ (3\mathrm{d}),\ (4\mathrm{s}, 4\mathrm{p}),\ (4\mathrm{d}),\ (4\mathrm{f}),\ (5\mathrm{s}, 5\mathrm{p}),\ \dots
$$
The shielding constant $\sigma$ of the electron being shielded is the sum of the contributions of all the other electrons:

1. Electrons in groups to the right (outside) of the group of the shielded electron contribute 0;
2. Each other electron in the same group contributes 0.35 (0.30 within the 1s group);
3. If the shielded electron is an s or p electron, each electron with principal quantum number one smaller contributes 0.85, and each electron in still lower shells contributes 1.00;
4. If the shielded electron is a d or f electron, each electron in the groups to its left (inside) contributes 1.00.

Slater's rules also specify that for $n \ge 4$ the $n$ in the orbital energy formula is replaced by the effective principal quantum number $n^*$ ($n^* = 3.7, 4.0, 4.2$ for $n = 4, 5, 6$). They are only a rough estimate, but are sufficient to explain many qualitative regularities.

**Example 2.3.1** Estimate the first ionization energy of He using Slater's rules.

Solution: Each 1s electron is shielded by the other, $\sigma = 0.30$ and $Z_{\mathrm{eff}} = 1.70$. The energy of the He atom is $E(\ce{He}) \approx 2 \times (-13.6 \times 1.70^2)\,\mathrm{eV} = -78.6\,\mathrm{eV}$ (experiment $-79.0\,\mathrm{eV}$) and the energy of $\ce{He+}$ is $E(\ce{He+}) = -13.6 \times 2^2\,\mathrm{eV} = -54.4\,\mathrm{eV}$, so $I_1 = E(\ce{He+}) - E(\ce{He}) \approx 24.2\,\mathrm{eV}$, close to the experimental value of $24.59\,\mathrm{eV}$. Note that the ionization energy is the difference between the total energies of two states and is not equal to the negative of the orbital energy of a single electron.

**Example 2.3.2** Calculate the effective nuclear charges and orbital energies of the 3s, 3d and 4s electrons in the Sc atom ($Z = 21$, $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^6\,3\mathrm{s}^2\,3\mathrm{p}^6\,3\mathrm{d}^1\,4\mathrm{s}^2$).

Solution: The grouping is $(1\mathrm{s})^2\,(2\mathrm{s}, 2\mathrm{p})^8\,(3\mathrm{s}, 3\mathrm{p})^8\,(3\mathrm{d})^1\,(4\mathrm{s}, 4\mathrm{p})^2$.

- 3s: $\sigma = 7 \times 0.35 + 8 \times 0.85 + 2 \times 1.00 = 11.25$, $Z_{\mathrm{eff}} = 9.75$, $E_{3\mathrm{s}} \approx -13.6 \times 9.75^2/3^2\,\mathrm{eV} = -144\,\mathrm{eV}$;
- 3d: $\sigma = 18 \times 1.00 = 18.00$, $Z_{\mathrm{eff}} = 3.00$, $E_{3\mathrm{d}} \approx -13.6 \times 3.00^2/3^2\,\mathrm{eV} = -13.6\,\mathrm{eV}$;
- 4s: $\sigma = 1 \times 0.35 + 9 \times 0.85 + 10 \times 1.00 = 18.00$, $Z_{\mathrm{eff}} = 3.00$, $E_{4\mathrm{s}} \approx -13.6 \times 3.00^2/3.7^2\,\mathrm{eV} = -8.9\,\mathrm{eV}$.

The inner 3s electron is shielded little and has a much lower energy; in Sc the energy of 3d is already lower than that of 4s.

Within the same shell, s electrons penetrate strongly and are shielded somewhat less than p electrons. Slater's rules do not distinguish s from p in the same group, but effective nuclear charges calculated from Hartree–Fock wave functions (Clementi and Raimondi, 1963) show this difference:

| Element | B | C | N | O | F | Ne |
|---|---|---|---|---|---|---|
| $Z$ | 5 | 6 | 7 | 8 | 9 | 10 |
| $Z_{\mathrm{eff}}$ (Slater, 2s and 2p) | 2.60 | 3.25 | 3.90 | 4.55 | 5.20 | 5.85 |
| $Z_{\mathrm{eff}}(2\mathrm{s})$ (Clementi) | 2.58 | 3.22 | 3.85 | 4.49 | 5.13 | 5.76 |
| $Z_{\mathrm{eff}}(2\mathrm{p})$ (Clementi) | 2.42 | 3.14 | 3.83 | 4.45 | 5.10 | 5.76 |

From C to N the $Z_{\mathrm{eff}}$ of 2p increases by 0.69, but from N to O only by 0.62: the additional 2p electron of O must enter a 2p orbital that already holds an electron, and the repulsion between two electrons in the same orbital is stronger, so more of the increase in nuclear charge is cancelled.

Penetration and shielding together determine the order of energy levels in many-electron atoms. For the same $n$, the smaller $l$ is, the stronger the penetration, the weaker the shielding and the lower the energy, so the levels of one shell split into $E_{n\mathrm{s}} < E_{n\mathrm{p}} < E_{n\mathrm{d}} < E_{n\mathrm{f}}$ (energy level splitting). When the penetration effect is strong enough, the energy of an orbital with larger $n$ can even be lower than that of one with smaller $n$:

**Definition 2.3.3** The phenomenon in many-electron atoms in which an orbital with a larger principal quantum number and a smaller angular momentum quantum number has a lower energy than one with a smaller principal quantum number and a larger angular momentum quantum number, for example $E_{4\mathrm{s}} < E_{3\mathrm{d}}$, $E_{5\mathrm{s}} < E_{4\mathrm{d}}$ and $E_{6\mathrm{s}} < E_{4\mathrm{f}} < E_{5\mathrm{d}}$, is called **energy level crossing**.

From spectroscopic data Pauling summarized an approximate energy level diagram of many-electron atomic orbitals, which divides the orbitals in order of increasing energy into 7 energy-level groups, with similar energies within a group and larger gaps between groups:

| Energy-level group | Orbitals | Electron capacity | Corresponding period |
|---|---|---|---|
| 1 | 1s | 2 | Period 1 (2 elements) |
| 2 | 2s 2p | 8 | Period 2 (8) |
| 3 | 3s 3p | 8 | Period 3 (8) |
| 4 | 4s 3d 4p | 18 | Period 4 (18) |
| 5 | 5s 4d 5p | 18 | Period 5 (18) |
| 6 | 6s 4f 5d 6p | 32 | Period 6 (32) |
| 7 | 7s 5f 6d 7p | 32 | Period 7 (32) |

This order agrees with the Madelung rule of [5.5.4](/5.5.4#sec-4.4.3) (filling in order of $n + l$) and with the $n + 0.7l$ rule of Xu Guangxian. The M shell can hold up to 18 electrons, yet Period 3 has only 8 elements, precisely because 3d belongs to the fourth energy-level group: after 3p is filled, the next electron enters the lower-lying 4s. The division into energy-level groups is the essential reason why the periodic table is divided into periods.

Two points should be noted about the Pauling diagram. First, it applies only to many-electron atoms; in hydrogen and hydrogen-like ions the energy depends only on $n$, with no level splitting or crossing. Second, strictly speaking it is a diagram of the order in which electrons fill the orbitals in ground-state atoms, not the true order of orbital energies in any given atom. The Cotton diagram shows how the orbital energies vary with atomic number:

- Only for $Z = 1$ are the orbitals of the same $n$ degenerate; in all other atoms the levels split;
- The energies of all orbitals decrease as $Z$ increases, because the nuclear charge increases;
- The energy of the 3d orbitals falls with $Z$ faster than that of 4s: in K and Ca $E_{4\mathrm{s}} < E_{3\mathrm{d}}$, and from Sc onward $E_{3\mathrm{d}} < E_{4\mathrm{s}}$ (Example 2.3.2). In K and Ca the 3d orbitals are still empty, their main peak lies outside the inner electrons and is almost completely shielded, and the small penetrating peak of 4s dominates; from Sc onward 3d begins to be filled, the nuclear charge increases while the 3d electrons shield one another very weakly, and the main peak of 3d takes over.

A question therefore arises: if the energy of 3d is lower than that of 4s in Sc, why is the valence configuration of Sc $3\mathrm{d}^1\,4\mathrm{s}^2$ and not $3\mathrm{d}^3$ or $3\mathrm{d}^2\,4\mathrm{s}^1$? The reason is that the configuration of an atom is determined by its total energy, which is not the sum of the orbital energies of the electrons: the 3d orbitals are much more compact than 4s, and putting electrons into 3d greatly increases the repulsion between electrons, while the 4s orbital is diffuse and the repulsion between two 4s electrons is small. Overall, $3\mathrm{d}^1\,4\mathrm{s}^2$ has the lowest total energy. In cations there are fewer electrons for the same nuclear charge and 3d is stabilized further, so transition metals always lose their 4s electrons first, and the configurations of ions such as $\ce{Sc^3+}$ and $\ce{Ti^2+}$ are $[\ce{Ar}]\,3\mathrm{d}^n$. A quantitative treatment requires self-consistent field calculations ([6.2](/6.2)).

### 2.3.2. Rules for Electron Configurations

The ground-state **electron configuration** of an atom is determined by three principles ([5.5.4](/5.5.4#sec-4.4.2)): the **Pauli exclusion principle** (no two electrons in an atom have all four quantum numbers identical, so each orbital holds at most two electrons of opposite spin); the **aufbau principle** (subject to the Pauli principle, electrons fill the orbitals in the order of the Pauling diagram, also called the building-up principle); and **Hund's rule** (electrons entering a set of degenerate orbitals occupy different orbitals as far as possible with parallel spins, [5.5.4](/5.5.4#sec-4.4.3)). Hund's rule is also an expression of the lowest-energy principle: when one electron is already in an orbital, another electron entering the same orbital must overcome the pairing energy. It also follows that equivalent orbitals that are completely filled ($\mathrm{p}^6$, $\mathrm{d}^{10}$, $\mathrm{f}^{14}$), half-filled ($\mathrm{p}^3$, $\mathrm{d}^5$, $\mathrm{f}^7$) or empty are relatively stable.

When writing electron configurations, the inner part identical to that of the preceding noble gas is often written as the **atomic core**, for example C is $[\ce{He}]\,2\mathrm{s}^2\,2\mathrm{p}^2$ and K is $[\ce{Ar}]\,4\mathrm{s}^1$. For transition elements the orbitals are written in order of principal quantum number, so Ti is written $[\ce{Ar}]\,3\mathrm{d}^2\,4\mathrm{s}^2$ rather than in filling order as $[\ce{Ar}]\,4\mathrm{s}^2\,3\mathrm{d}^2$. Orbital diagrams show Hund's rule more clearly; for example the three 2p electrons of N occupy three orbitals: $2\mathrm{p}$ ↑ ↑ ↑; the $2\mathrm{p}^4$ of O is ↑↓ ↑ ↑.

The ground-state configurations determined by spectroscopic experiments have some exceptions to the predictions of the aufbau principle:

| Element | By filling order | Actual configuration |
|---|---|---|
| Cr | $[\ce{Ar}]\,3\mathrm{d}^4\,4\mathrm{s}^2$ | $[\ce{Ar}]\,3\mathrm{d}^5\,4\mathrm{s}^1$ |
| Cu | $[\ce{Ar}]\,3\mathrm{d}^9\,4\mathrm{s}^2$ | $[\ce{Ar}]\,3\mathrm{d}^{10}\,4\mathrm{s}^1$ |
| Mo | $[\ce{Kr}]\,4\mathrm{d}^4\,5\mathrm{s}^2$ | $[\ce{Kr}]\,4\mathrm{d}^5\,5\mathrm{s}^1$ |
| Pd | $[\ce{Kr}]\,4\mathrm{d}^8\,5\mathrm{s}^2$ | $[\ce{Kr}]\,4\mathrm{d}^{10}$ |
| Ag | $[\ce{Kr}]\,4\mathrm{d}^9\,5\mathrm{s}^2$ | $[\ce{Kr}]\,4\mathrm{d}^{10}\,5\mathrm{s}^1$ |
| Au | $[\ce{Xe}]\,4\mathrm{f}^{14}\,5\mathrm{d}^9\,6\mathrm{s}^2$ | $[\ce{Xe}]\,4\mathrm{f}^{14}\,5\mathrm{d}^{10}\,6\mathrm{s}^1$ |

The exceptions of Cr, Cu and others can be understood from the stability of half-filled and filled subshells; but this is only an empirical rule and does not hold universally: W, in the same group as Cr and Mo, is $[\ce{Xe}]\,4\mathrm{f}^{14}\,5\mathrm{d}^4\,6\mathrm{s}^2$, and Nb ($4\mathrm{d}^4\,5\mathrm{s}^1$) and Ru ($4\mathrm{d}^7\,5\mathrm{s}^1$) in Period 5 also deviate from the filling order. When the energies of $n\mathrm{s}$ and $(n-1)\mathrm{d}$ are close, a delicate balance of various factors decides the configuration.

**Example 2.3.3** Write the ground-state electron configurations of Ti, $\ce{Ti^3+}$, Ni, $\ce{Ni^2+}$, Fe and $\ce{Fe^3+}$.

Solution: Ti is $[\ce{Ar}]\,3\mathrm{d}^2\,4\mathrm{s}^2$; on losing three electrons the two 4s electrons are lost first and then one 3d electron, so $\ce{Ti^3+}$ is $[\ce{Ar}]\,3\mathrm{d}^1$. Ni is $[\ce{Ar}]\,3\mathrm{d}^8\,4\mathrm{s}^2$ and $\ce{Ni^2+}$ is $[\ce{Ar}]\,3\mathrm{d}^8$. Fe is $[\ce{Ar}]\,3\mathrm{d}^6\,4\mathrm{s}^2$, $\ce{Fe^2+}$ is $[\ce{Ar}]\,3\mathrm{d}^6$ and $\ce{Fe^3+}$ is $[\ce{Ar}]\,3\mathrm{d}^5$ (half-filled, a stabilizing factor for $\ce{Fe^3+}$).

### 2.3.3. Electronic Structure and the Periodic System

The properties of the elements vary periodically with increasing atomic number, a regularity called the periodic law (Mendeleev, 1869). Its origin is the periodicity of the electronic structure of atoms: each period begins with a new s subshell and ends when the p subshell is filled (the noble gases; He is $1\mathrm{s}^2$), the number of the period equals the number of electron shells of the atoms in that period, and the number of elements in each period equals the capacity of the corresponding energy-level group: 2, 8, 8, 18, 18, 32, 32. In Period 6 the 14 elements after $\ce{La}$ fill 4f in turn (the filling order is $6\mathrm{s} \to 4\mathrm{f} \to 5\mathrm{d} \to 6\mathrm{p}$), and in Period 7 the 14 elements after Ac fill 5f in turn.

The chemical properties of an element are determined mainly by the electrons that take part in bonding:

**Definition 2.3.4** The electrons in an atom that can take part in forming chemical bonds are called **valence electrons**; the subshells containing them make up the valence shell, and their configuration is called the valence electron configuration: the $n\mathrm{s}\,n\mathrm{p}$ electrons for main-group elements, the $(n-1)\mathrm{d}\,n\mathrm{s}$ electrons for transition elements, and for lanthanoids and actinoids also the $(n-2)\mathrm{f}$ electrons.

According to the subshell into which the last electron is placed, the periodic table is divided into five blocks:

| Block | Groups | Valence electron configuration |
|---|---|---|
| s block | Groups 1 and 2 (and He) | $n\mathrm{s}^{1\text{–}2}$ |
| p block | Groups 13–18 | $n\mathrm{s}^2\,n\mathrm{p}^{1\text{–}6}$ (except He) |
| d block | Groups 3–10 | $(n-1)\mathrm{d}^{1\text{–}9}\,n\mathrm{s}^{1\text{–}2}$ (Pd is $4\mathrm{d}^{10}$) |
| ds block | Groups 11 and 12 | $(n-1)\mathrm{d}^{10}\,n\mathrm{s}^{1\text{–}2}$ |
| f block | Lanthanoids, actinoids | $(n-2)\mathrm{f}^{0\text{–}14}\,(n-1)\mathrm{d}^{0\text{–}2}\,n\mathrm{s}^2$ |

The ds block is the usual division in Chinese textbooks; IUPAC counts Groups 11 and 12 as part of the d block.

![Blocks of the periodic table: s block (groups 1–2 and He), p block (13–18), d block (3–10), ds block (11–12) and f block (lanthanoids and actinoids). Above the columns are the IUPAC group numbers 1–18 and the traditional A/B labels](./plots/periodic-table-blocks.py)

**Definition 2.3.5** The elements of the s and p blocks (Groups 1, 2 and 13–18) are called **main-group elements**. Elements whose atoms have an incompletely filled d subshell, or that can form cations with an incompletely filled d subshell, are called **transition elements** (transition metals), that is, Groups 3–11; Chinese textbooks customarily call the d and ds blocks together (Groups 3–12) the transition elements. The 15 elements from La to Lu are called **lanthanoids** and the 15 elements from Ac to Lr **actinoids**; their last electron mostly enters the $(n-2)\mathrm{f}$ subshell, and they are also called **inner transition elements**.

Groups of the periodic table are numbered in two ways. IUPAC recommends numbering the 18 columns as Groups 1–18; the traditional Chinese-textbook notation labels main groups A and subgroups B (groups IA–VIIIA in older Chinese textbooks), and the correspondence is:

| IUPAC | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8–10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A/B group | IA | IIA | IIIB | IVB | VB | VIB | VIIB | VIII | IB | IIB | IIIA | IVA | VA | VIA | VIIA | 0 (VIIIA) |

The position of an element in the periodic table can be determined from its valence electron configuration:

- Main-group elements: number of valence electrons = number of the A group = maximum oxidation number (except O and F); the IUPAC group number is the number of $n\mathrm{s}$ electrons in the s block, or $10 +$ the number of valence electrons in the p block.
- Groups 3–7 (IIIB–VIIB): group number = total number of $(n-1)\mathrm{d} + n\mathrm{s}$ electrons; the number of $(n-1)\mathrm{d}\,n\mathrm{s}$ electrons in Groups 8–10 (VIII) is 8–10; the group number of Groups 11 and 12 (IB, IIB) is $10 +$ the number of $n\mathrm{s}$ electrons.

**Example 2.3.4** S ($Z = 16$) has the configuration $[\ce{Ne}]\,3\mathrm{s}^2\,3\mathrm{p}^4$ with 6 valence electrons, and lies in Period 3, Group 16 (VIA), with maximum oxidation number +6. Mn ($Z = 25$) is $[\ce{Ar}]\,3\mathrm{d}^5\,4\mathrm{s}^2$ with 7 valence electrons, Period 4, Group 7 (VIIB), maximum oxidation number +7 ($\ce{MnO4-}$). Cd ($Z = 48$) is $[\ce{Kr}]\,4\mathrm{d}^{10}\,5\mathrm{s}^2$, Period 5, Group 12 (IIB).

**Example 2.3.5** To which group, or which element, does an element with each of the following valence electron descriptions belong? (1) three p electrons in the valence shell; (2) a filled 3d orbital and two electrons in the 4s orbital; (3) two electrons with $n = 4$, $l = 0$ and eight electrons with $n = 3$, $l = 2$.

Solution: (1) $n\mathrm{s}^2\,n\mathrm{p}^3$, Group 15 (VA); (2) $3\mathrm{d}^{10}\,4\mathrm{s}^2$, Zn; (3) $3\mathrm{d}^8\,4\mathrm{s}^2$, Ni.

## 2.4. Periodicity of the Basic Properties of the Elements

The electronic structure of atoms varies periodically, and the atomic parameters directly related to it (atomic radius, ionization energy, electron affinity and electronegativity) also vary periodically. They can be explained in a unified way by two factors: the number of electron shells ($n$) and the effective nuclear charge $Z_{\mathrm{eff}}$ felt by the valence electrons.

![Periodic trends for Z = 1–56: atomic radius (covalent single-bond radii for most elements), first ionization energy, electron affinity (open circles: anion not stable, plotted at zero) and Pauling electronegativity. Vertical lines mark the noble gases](./plots/periodic-trends.py)

### 2.4.1. Atomic Radius

An electron cloud has no definite boundary, so an isolated atom has no well-defined radius; atomic radii are all defined from internuclear distances in some bonded state, and according to the mode of bonding there are three kinds:

**Definition 2.4.1** The size of an atom defined from internuclear distances is called the **atomic radius**. Half the internuclear distance when two atoms of the same element are joined by a single covalent bond is called the **covalent radius** (for example the internuclear distance in $\ce{Cl2}$ is $199\,\mathrm{pm}$, so the covalent radius of Cl is $99\,\mathrm{pm}$); half the distance between the nuclei of two adjacent atoms in a metallic crystal is called the **metallic radius**; and when two atoms touch one another with only van der Waals forces ([6.1.4](/6.1.4)) between them and no bond, half the internuclear distance is called the **van der Waals radius** (for example in solid noble gases, or between atoms of adjacent molecules in molecular crystals).

The van der Waals radius of an element is clearly larger than its covalent radius (for Cl $175\,\mathrm{pm}$ against $99\,\mathrm{pm}$), and the same kind of radius must be used when comparing atomic sizes. The periodic variation of atomic radius is as follows:

- Across a period from left to right the atomic radius generally decreases: the number of shells is unchanged, the effective nuclear charge increases and the attraction of the nucleus for the outer electrons becomes stronger. The decrease is largest for main-group elements (about $10\,\mathrm{pm}$ on average between neighbors in short periods), because the added electron is in the outermost shell, shields the electrons of the same shell little and so $Z_{\mathrm{eff}}$ increases quickly; it is smaller for transition elements (about $4\,\mathrm{pm}$), where the added electron is in the penultimate shell $(n-1)\mathrm{d}$ and shields the outermost $n\mathrm{s}$ electrons more strongly; and it is smallest for inner transition elements (about $1\,\mathrm{pm}$ between neighboring lanthanoids), where the added electron is in the third shell from the outside, $(n-2)\mathrm{f}$, and shielding is stronger still. When $\mathrm{d}^{10}$ is completely filled (Zn, Cd, Hg) the radius increases slightly.
- Down a group the number of shells increases and the atomic radius increases. The increase is marked for main-group elements; for transition elements it occurs from Period 4 to Period 5, while the radii in Periods 5 and 6 are almost equal, a consequence of the lanthanide contraction.
- The radii of the noble gases are van der Waals radii and cannot be compared directly with the covalent radii of the other elements of the same period.

**Definition 2.4.2** The gradual, slow decrease of the atomic and ionic radii of the lanthanoids from La to Lu with increasing nuclear charge is called the **lanthanide contraction**.

The metallic radius of the lanthanoids decreases from $187.7\,\mathrm{pm}$ for La to $173.4\,\mathrm{pm}$ for Lu, about $14\,\mathrm{pm}$ in all (Eu and Yb are divalent in the metals and have anomalously large radii); the ionic radius of $\ce{Ln^3+}$ (six-coordinate) decreases from $103\,\mathrm{pm}$ for $\ce{La^3+}$ to $86\,\mathrm{pm}$ for $\ce{Lu^3+}$, about $17\,\mathrm{pm}$ in all. Each step is small, but the accumulated effect is considerable and has two consequences:

1. Within the lanthanoids: the radii of neighboring elements are very close and their chemical properties are similar; they occur together in nature and are very difficult to separate from one another (the separation of the rare-earth elements is discussed in [6.1.15](/6.1.15)).
2. For the elements after the lanthanoids: the transition elements of Period 6 have one more electron shell than those of the same group in Period 5 and should be markedly larger, but the lanthanide contraction exactly cancels this increase. So the radii of Zr and Hf (metallic radii $160$ and $159\,\mathrm{pm}$), Nb and Ta (both $146\,\mathrm{pm}$) and Mo and W are almost equal and their properties are extremely similar; they occur together in nature and are difficult to separate.

### 2.4.2. Ionization Energy

**Definition 2.4.3** The minimum energy required for a gaseous atom in its ground state to lose one electron and become a gaseous +1 ion is called the **first ionization energy** $I_1$ of the element; the energy required for the +1 gaseous ion to lose another electron is called the second ionization energy $I_2$, and so on. In chemistry ionization energies are given per $1\,\mathrm{mol}$, in $\mathrm{kJ\,mol^{-1}}$:

$$
\ce{Li(g) -> Li+(g) + e-}, \quad I_1 = 520.2\,\mathrm{kJ\,mol^{-1}}; \qquad \ce{Li+(g) -> Li^2+(g) + e-}, \quad I_2 = 7298.1\,\mathrm{kJ\,mol^{-1}}.
$$

The *successive ionization energies* defined in this way always increase ($I_1 < I_2 < I_3 < \cdots$): the more positive charge an ion carries, the harder it is to remove the remaining electrons. A sudden jump at some stage reveals the shell structure: $I_2$ of Li is 14 times $I_1$ because the second electron must be removed from the inner 1s shell; $I_1$, $I_2$ and $I_3$ of Mg are $738$, $1451$ and $7733\,\mathrm{kJ\,mol^{-1}}$, with the jump at $I_3$, which is why Mg is +2 in its compounds.

The periodicity of ionization energy (figure above):

- Across a period from left to right the ionization energy generally increases, with the smallest $I_1$ for Group 1 and the largest for the noble gases, in agreement with the decrease in atomic radius and the increase in $Z_{\mathrm{eff}}$. For transition elements $Z_{\mathrm{eff}}$ does not increase much and the ionization energy increases only slightly.
- Down a main group the atomic radius increases and the ionization energy decreases.
- The curve has two regular "sawtooth" features. In Period 2, Be ($899.5\,\mathrm{kJ\,mol^{-1}}$) > B ($800.6$): B loses a 2p electron, which penetrates less and has higher energy; N ($1402.3$) > O ($1313.9$): the 2p electron lost by O shares an orbital with another electron and experiences additional repulsion, and after its loss the configuration becomes the half-filled $2\mathrm{p}^3$. In Period 3, Mg > Al and P > S for the same reasons.
- $I_1$ of H ($1312\,\mathrm{kJ\,mol^{-1}}$) is much larger than that of Na ($495.8$): the 1s electron of H is close to the nucleus and there are no inner electrons to shield it.

### 2.4.3. Electron Affinity

**Definition 2.4.4** The energy released when a gaseous atom in its ground state gains one electron to form a gaseous −1 ion is called the (first) **electron affinity** $E_{\mathrm{ea}}$ of the element:

$$
\ce{X(g) + e- -> X-(g)}, \qquad E_{\mathrm{ea}} = E(\ce{X}) - E(\ce{X-}).
$$
$E_{\mathrm{ea}} > 0$ means that the anion is more stable than the atom plus a free electron (energy is released).

This is the current IUPAC sign convention. Some textbooks use the enthalpy change of this process, the *electron gain enthalpy* $\Delta_{\mathrm{eg}}H \approx -E_{\mathrm{ea}}$, which is negative when the process is exothermic and has the same magnitude as $E_{\mathrm{ea}}$ with the opposite sign (the two also differ by $\frac{5}{2}RT \approx 6\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$, usually neglected); check the convention before reading data. Some examples: $E_{\mathrm{ea}}(\ce{F}) = 328$, $E_{\mathrm{ea}}(\ce{Cl}) = 349$, $E_{\mathrm{ea}}(\ce{Br}) = 325$, $E_{\mathrm{ea}}(\ce{O}) = 141$, $E_{\mathrm{ea}}(\ce{S}) = 200$ and $E_{\mathrm{ea}}(\ce{H}) = 73\,\mathrm{kJ\,mol^{-1}}$.

The energy released when an anion gains a further electron is called the *second electron affinity* $E_{\mathrm{ea},2}$. An anion repels an incoming electron, so the second electron affinity is always negative (endothermic), for example $E_{\mathrm{ea},2} \approx -844\,\mathrm{kJ\,mol^{-1}}$ for $\ce{O-(g) + e- -> O^2-(g)}$. Gaseous $\ce{O^2-}$ is not stable, and this value can be estimated only indirectly from the Born–Haber cycle ([6.1.6](/6.1.6)), with different sources differing by as much as $100\,\mathrm{kJ\,mol^{-1}}$; $\ce{O^2-}$ can exist stably in ionic crystals because the lattice enthalpy compensates for this energy.

The electron affinity reflects how easily an atom gains an electron: atoms of large nuclear charge and small radius attract electrons strongly, have large electron affinities and are strongly nonmetallic. Its periodicity is less regular than that of the ionization energy:

- Across a period from left to right it generally increases, with the halogens largest. The anions of the noble gases (closed shells), of Be and Mg ($n\mathrm{s}^2$, the electron must enter the higher-energy $n\mathrm{p}$) and of N (half-filled $2\mathrm{p}^3$) are unstable, and their electron affinities are negative or near zero; this is consistent with Be, which has a larger nuclear charge than Li, having a smaller electron affinity (Li has $60\,\mathrm{kJ\,mol^{-1}}$), and with the electron affinity of N being smaller than that of C ($122\,\mathrm{kJ\,mol^{-1}}$).
- Down a group it generally decreases, but Period 2 is an exception: $E_{\mathrm{ea}}(\ce{F}) < E_{\mathrm{ea}}(\ce{Cl})$ and $E_{\mathrm{ea}}(\ce{O}) < E_{\mathrm{ea}}(\ce{S})$. F and O have very small radii, the electron density in the 2p subshell is very high and the incoming electron experiences strong repulsion. The element with the largest electron affinity is therefore Cl, not F, the most reactive nonmetal.

### 2.4.4. Electronegativity

Ionization energy and electron affinity describe the ability of an isolated atom to lose or gain an electron. In chemistry the ability of an atom in a molecule to attract bonding electrons matters more, and this requires another quantity:

**Definition 2.4.5** The relative measure of the ability of an atom in a molecule to attract bonding electrons is called the **electronegativity** $\chi$ of the element.

Pauling (1932) defined the first electronegativity scale from bond energies. If atoms A and B attract electrons equally, the bond energy of A–B should be close to the mean of the A–A and B–B bond energies; in fact the energy of a heteronuclear bond is always larger, and the excess

$$
\Delta = D(\ce{A-B}) - \frac{1}{2}\left[D(\ce{A-A}) + D(\ce{B-B})\right]
$$
comes from the stabilization due to the ionic character produced when the electrons shift toward one atom; the larger the electronegativity difference, the larger $\Delta$. Pauling stipulated

$$
\lvert\chi_{\mathrm{A}} - \chi_{\mathrm{B}}\rvert = \sqrt{\Delta/\mathrm{eV}} = 0.102\sqrt{\Delta/(\mathrm{kJ\,mol^{-1}})}.
$$
This fixes only differences of electronegativity, and a reference point must also be chosen: Pauling originally took F as about 4.0, and the current values (Allred, 1961, recalculated with more bond energy data) take H as 2.20, which gives F as 3.98.

**Example 2.4.1** Given the bond energies $D(\ce{H-H}) = 436$, $D(\ce{Cl-Cl}) = 242$ and $D(\ce{H-Cl}) = 432\,\mathrm{kJ\,mol^{-1}}$, find the electronegativity difference between H and Cl.

Solution: $\Delta = 432 - \frac{1}{2}(436 + 242) = 93\,\mathrm{kJ\,mol^{-1}}$, $\lvert\chi_{\mathrm{Cl}} - \chi_{\mathrm{H}}\rvert = 0.102\sqrt{93} = 0.98$, in agreement with $3.16 - 2.20 = 0.96$ from the table.

Mulliken (1934) gave another, more direct definition: the ability of an atom to attract electrons is related both to how easily it loses electrons (ionization energy) and to how easily it gains them (electron affinity), and the average of the two is taken as the *Mulliken electronegativity*: $\chi_{\mathrm{M}} = \frac{1}{2}(I_1 + E_{\mathrm{ea}})$ (in eV). For example F gives $\frac{1}{2}(17.42 + 3.40) = 10.41\,\mathrm{eV}$ and Cl gives $8.29\,\mathrm{eV}$. The Mulliken and Pauling electronegativities are roughly linearly related; there are also other scales, such as the Allred–Rochow scale based on effective nuclear charge and covalent radius. Different scales give different values and must not be mixed. The following table gives the Pauling electronegativities of the main-group elements (CRC Handbook):

| 1 | 2 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|
| H 2.20 | | | | | | |
| Li 0.98 | Be 1.57 | B 2.04 | C 2.55 | N 3.04 | O 3.44 | F 3.98 |
| Na 0.93 | Mg 1.31 | Al 1.61 | Si 1.90 | P 2.19 | S 2.58 | Cl 3.16 |
| K 0.82 | Ca 1.00 | Ga 1.81 | Ge 2.01 | As 2.18 | Se 2.55 | Br 2.96 |
| Rb 0.82 | Sr 0.95 | In 1.78 | Sn 1.96 | Sb 2.05 | Te 2.10 | I 2.66 |
| Cs 0.79 | Ba 0.89 | Tl 1.62 | Pb 2.33 | Bi 2.02 | | |

Electronegativity increases across a period from left to right and decreases down a group, with F the largest and Cs and Fr the smallest. Roughly speaking, metals mostly have electronegativities below 2.0 and nonmetals above 2.0, but this boundary is not strict (H is 2.20 and is a nonmetal, Au is 2.54). Electronegativity is the basis for judging the polarity and type of bonds and for assigning oxidation numbers: the larger the electronegativity difference between two atoms, the more polar the bond, and a very large difference gives an ionic bond ([6.1.3](/6.1.3)).

## Summary

- From the nuclear model to quantum mechanics: Bohr's theory gives $E_n = -\frac{Z^2}{n^2} \times 13.6\,\mathrm{eV}$ for one-electron atoms and explains the hydrogen spectrum, but it cannot be extended to many-electron atoms; electrons show wave–particle duality, and their states are described by wave functions (atomic orbitals).
- An atomic orbital is fixed by $n$, $l$ and $m_l$; adding $m_s$ fixes the state of one electron completely. The s, p, d and f subshells have 1, 3, 5 and 7 orbitals, and shell $n$ holds at most $2n^2$ electrons. There are $n - l - 1$ radial nodes and $l$ nodal planes (angular nodes) (Definition 2.2.2); penetration (Definition 2.2.3) orders the energies within a shell as $E_{n\mathrm{s}} < E_{n\mathrm{p}} < E_{n\mathrm{d}} < E_{n\mathrm{f}}$.
- Many-electron atoms: shielding and the effective nuclear charge $Z_{\mathrm{eff}} = Z - \sigma$ (Definition 2.3.1), estimated with Slater's rules (Definition 2.3.2); penetration and shielding together cause energy-level crossing (Definition 2.3.3).
- The ground-state electron configuration follows from the Pauli exclusion principle, the aufbau principle (Pauling's energy-level diagram) and Hund's rule; exceptions such as Cr and Cu are empirical. The valence configuration fixes an element's place in the periodic table: the period number is the principal quantum number of the outermost shell, and there are five blocks s, p, d, ds and f (Definition 2.3.4, Definition 2.3.5).
- The periodic trends in atomic properties can all be explained by the number of shells and $Z_{\mathrm{eff}}$:

| Property | Across a period (left to right) | Down a group | Key points |
|---|---|---|---|
| Atomic radius (Definition 2.4.1) | Decreases | Increases | Compare radii of the same kind; the lanthanide contraction (Definition 2.4.2) makes transition elements of the same group in periods 5 and 6 nearly equal in size |
| First ionization energy $I_1$ (Definition 2.4.3) | Generally increases | Decreases | Dips from group 2 to 13 and from group 15 to 16; jumps in successive ionization energies reveal the shells |
| Electron affinity $E_{\mathrm{ea}}$ (Definition 2.4.4) | Generally increases, largest for the halogens | Generally decreases | Period 2 is anomalous: $E_{\mathrm{ea}}(\ce{F}) < E_{\mathrm{ea}}(\ce{Cl})$; the second electron affinity is always negative |
| Electronegativity $\chi$ (Definition 2.4.5) | Increases | Decreases | The Pauling scale is defined from bond energies; F is the largest (3.98) |

## Questions

1. True or false? Explain. (1) All elements with valence configuration $n\mathrm{s}^1$ are alkali metals; (2) the valence configuration of all elements of Groups 8–10 (Group VIII) is $(n-1)\mathrm{d}^6\,n\mathrm{s}^2$; (3) the first transition series fills 4s before 3d, so on losing electrons it loses 3d first; (4) because of the lanthanide contraction, the atomic radii of all Period 6 elements are smaller than those of the same group in Period 5; (5) $\ce{O(g) + e- -> O-(g)}$ and $\ce{O-(g) + e- -> O^2-(g)}$ are both exothermic; (6) F is the most reactive nonmetal, so its electron affinity is the largest; (7) the ionization energy of a metal starts from the solid metal.

   **Answer** All are false. (1) H ($1\mathrm{s}^1$), Cr ($3\mathrm{d}^5\,4\mathrm{s}^1$), Cu ($3\mathrm{d}^{10}\,4\mathrm{s}^1$) and others also have it. (2) Only Fe is $3\mathrm{d}^6\,4\mathrm{s}^2$; Co is $3\mathrm{d}^7\,4\mathrm{s}^2$, Ni is $3\mathrm{d}^8\,4\mathrm{s}^2$, Ru is $4\mathrm{d}^7\,5\mathrm{s}^1$ and Pd is $4\mathrm{d}^{10}$. (3) The filling order reflects the total energy of the ground-state configuration; on losing electrons, 4s is always lost first (Section 2.3.1). (4) The lanthanide contraction only makes the radii of the transition elements after the lanthanoids similar to those of the same group in the previous period; for main-group elements (such as Cs > Rb and Pb > Sn) the radius still increases markedly. (5) The second step is endothermic. (6) Cl has the largest electron affinity. (7) The initial state of the ionization energy is the gaseous atom in its ground state.

2. $\ce{F-}$ and Ne have the same electron configuration; is the energy required to remove an electron from each the same?

   **Answer** No. The nuclear charge of Ne is 10 and that of $\ce{F-}$ is 9; the ionization energy of Ne ($2081\,\mathrm{kJ\,mol^{-1}}$) is far larger than the energy needed to remove an electron from $\ce{F-}$, which is the electron affinity of F ($328\,\mathrm{kJ\,mol^{-1}}$).

3. Can ionization energy be used to measure the ability of an atom in a molecule to attract electrons?

   **Answer** Not entirely. Ionization energy describes only how easily an isolated atom loses an electron; in a molecule an atom also competes with other atoms for the bonding electrons, so electronegativity is needed; the Mulliken electronegativity combines the ionization energy with the electron affinity.
