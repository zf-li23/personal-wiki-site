---
title: Electrons in Atoms
description: The hydrogen spectrum and Bohr's theory; the quantum-mechanical hydrogen atom (angular momentum, energy levels and degeneracy, electron clouds and radial probability); fine structure, the Zeeman effect, the Stern–Gerlach experiment, electron spin, spin–orbit coupling, term symbols and alkali-metal levels; identical particles, fermions and bosons, the Pauli exclusion principle, Fermi–Dirac and Bose–Einstein distributions; electron configurations of atoms; a summary of quantum mechanics.
source_hash: 960d50ad7eb5
---

Atomic spectra are where quantum theory began, and they were its first real test. From Balmer's empirical formula for the hydrogen spectrum in 1885, through Bohr's atomic theory of 1913, the matrix mechanics of Heisenberg and Born and the wave mechanics of Schrödinger in 1925–1926, to the **Heisenberg uncertainty relation** of 1927 and the debates at the fifth Solvay Conference, the development of quantum mechanics revolved almost entirely around the electron in the atom. In this chapter we first solve the hydrogen atom with the methods of the previous chapter ([5.5.3](/5.5.3)): in spherical coordinates the **time-independent Schrödinger equation** separates, the angular part is the mathematical **spherical harmonics** ([2.5.5](/2.5.5#sec-5.4.2)), and the radial part gives the energy levels; the results of Bohr's theory are contained automatically. We then introduce electron spin (§4.2) and the symmetry of identical particles (§4.3), and use the Pauli exclusion principle to explain the electron configurations behind the periodic table (§4.4). The Fermi–Dirac and Bose–Einstein distributions of §4.3 are the quantum generalizations of Maxwell–Boltzmann statistics ([5.2.1](/5.2.1)) and are needed for the theory of metals and semiconductors in [5.5.6](/5.5.6); the electronic structure of atoms is also the physical basis of atomic structure and chemical bonding in chemistry. Section 4.5 summarizes the whole of quantum mechanics as treated here.

## 4.1. The Hydrogen Atom

### 4.1.1. Empirical Regularities of the Hydrogen Spectrum

The hydrogen atom is the simplest atom, and its spectrum is directly related to its electron energy levels. In the mid-nineteenth century Ångström measured several lines of the visible spectrum from a hydrogen discharge tube (a red line at $656.3\,\mathrm{nm}$, a blue-green line at $486.1\,\mathrm{nm}$, and two violet lines at $434.0\,\mathrm{nm}$ and $410.2\,\mathrm{nm}$, all wavelengths in air). In 1885 Balmer, a Swiss secondary-school mathematics teacher, found that they satisfy

$$
\lambda=B\frac{n^2}{n^2-4},\qquad n=3,4,5,\dots,\qquad B=364.56\,\mathrm{nm}.
$$
In terms of the wave number $\tilde\nu=1/\lambda$ this reads $\tilde\nu=\frac4B\big(\frac1{2^2}-\frac1{n^2}\big)$. Rydberg generalized it to the following form.

**Formula 4.1.1 (Rydberg Formula)** The wave numbers of all lines in the hydrogen spectrum are

$$
\tilde\nu=\frac1\lambda=R\Big(\frac1{n_{\mathrm{f}}^2}-\frac1{n_{\mathrm{i}}^2}\Big),\qquad n_{\mathrm{f}}=1,2,3,\dots,\quad n_{\mathrm{i}}=n_{\mathrm{f}}+1,n_{\mathrm{f}}+2,\dots
\tag{4.1}
$$
where $R=4/B$ is the *Rydberg constant*; the experimental value for hydrogen is $R_{\mathrm{H}}=1.096\,776\times10^7\,\mathrm{m^{-1}}$.

Lines with the same $n_{\mathrm{f}}$ form a spectral series:

| $n_{\mathrm{f}}$ | Series | Region | Year discovered |
|---|---|---|---|
| 1 | Lyman series | ultraviolet | 1906–1914 |
| 2 | *Balmer series* | visible and near ultraviolet | 1885 |
| 3 | Paschen series | infrared | 1908 |
| 4 | Brackett series | infrared | 1922 |
| 5 | Pfund series | infrared | 1924 |
| 6 | Humphreys series | far infrared | 1953 |

As $n_{\mathrm{i}}\to\infty$ each series approaches a series limit $R/n_{\mathrm{f}}^2$. That the wave number of a line is always the difference of two terms (the "combination principle") suggests that the atom has a set of discrete energy states and that spectral lines come from transitions between them.

### 4.1.2. Evolution of the Atomic Model

At the beginning of the nineteenth century Dalton regarded atoms as indivisible solid spheres. In 1897 J. J. Thomson measured the charge-to-mass ratio of cathode-ray particles and discovered the electron; he then proposed the "plum pudding" model, in which electrons are embedded in a uniformly distributed positive charge. In 1909 Geiger and Marsden bombarded gold foil with α particles and found that a few were scattered through large angles, which the plum pudding model could not explain. In 1911 Rutherford accordingly proposed the nuclear model: all of the positive charge and almost all of the mass of the atom are concentrated in a very small nucleus, with the electrons moving around it.

The nuclear model is fundamentally at odds with classical electromagnetism. An electron orbiting the nucleus is accelerated and would continuously radiate **electromagnetic waves** ([5.3.10](/5.3.10)); losing energy, it would spiral into the nucleus in about $10^{-11}\,\mathrm{s}$ according to classical theory, radiating at a continuously changing frequency. Real atoms, however, are stable and emit discrete spectral lines.

### 4.1.3. Bohr's Theory

In 1913 Bohr applied Planck's quantum hypothesis to Rutherford's nuclear model and proposed the *Bohr model* of the hydrogen atom, later called the old quantum theory.

**Property 4.1.1 (Bohr's Postulates)**

1. Stationary states: the electron can move around the nucleus only in certain circular orbits; the atom is then in a stationary state of definite energy and does not radiate electromagnetic waves.
2. Frequency condition: when the atom makes a transition from a stationary state of energy $E_{\mathrm{i}}$ to one of energy $E_{\mathrm{f}}$, it emits ($E_{\mathrm{i}}>E_{\mathrm{f}}$) or absorbs a **photon** of frequency $\nu=\lvert E_{\mathrm{i}}-E_{\mathrm{f}}\rvert/h$.
3. Quantization condition: the **angular momentum** of the electron in a stationary orbit is an integer multiple of $\hbar$, $L=m_{\mathrm{e}}vr=n\hbar$, $n=1,2,3,\dots$

Let the Coulomb force provide the centripetal force, $\frac{m_{\mathrm{e}}v^2}{r}=\frac{e^2}{4\pi\varepsilon_0r^2}$. Combining this with $m_{\mathrm{e}}vr=n\hbar$ gives the orbital radius and energy

$$
r_n=n^2a_0,\quad a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_{\mathrm{e}}e^2}=5.29\times10^{-11}\,\mathrm{m};\qquad E_n=-\frac{e^2}{8\pi\varepsilon_0r_n}=\frac{E_1}{n^2},\quad E_1=-\frac{m_{\mathrm{e}}e^4}{2(4\pi\varepsilon_0)^2\hbar^2}=-13.6\,\mathrm{eV}.
\tag{4.2}
$$
The quantity $a_0$ is called the **Bohr radius**; it gives the order of magnitude of the size of an atom. The energy $\lvert E_1\rvert=13.6\,\mathrm{eV}$ is the ionization energy of hydrogen. By the frequency condition, the wave number of light emitted in a transition from $n_{\mathrm{i}}$ to $n_{\mathrm{f}}$ is

$$
\tilde\nu=\frac{E_{n_{\mathrm{i}}}-E_{n_{\mathrm{f}}}}{hc}=\frac{m_{\mathrm{e}}e^4}{8\varepsilon_0^2h^3c}\Big(\frac1{n_{\mathrm{f}}^2}-\frac1{n_{\mathrm{i}}^2}\Big),
$$
which is exactly the Rydberg formula (4.1) and gives the theoretical value of the Rydberg constant, $R_\infty=\frac{m_{\mathrm{e}}e^4}{8\varepsilon_0^2h^3c}=1.097\,373\,157\times10^7\,\mathrm{m^{-1}}$. The subscript $\infty$ means that the nucleus is assumed to be at rest (infinite mass). To account for the motion of the nucleus, $m_{\mathrm{e}}$ must be replaced by the **reduced mass** of the electron and proton ([5.1.4](/5.1.4)), giving $R_{\mathrm{H}}=R_\infty/(1+m_{\mathrm{e}}/m_{\mathrm{p}})=1.096\,776\times10^7\,\mathrm{m^{-1}}$, in agreement with the spectroscopic measurement. The remaining relative difference is only of order $10^{-5}$ and comes from smaller effects such as fine structure (§4.2).

![Energy levels of hydrogen, E_n = -13.6 eV/n², and the first four spectral series: Lyman (transitions to n = 1, ultraviolet), Balmer (n = 2, visible), Paschen and Brackett (n = 3, 4, infrared)](./plots/hydrogen-levels.py)

An ion with a single electron and nuclear charge $Z$ ($\ce{He+}$, $\ce{Li^2+}$, $\ce{Be^3+}$, etc.) is called a hydrogen-like ion. Replacing $e^2$ by $Ze^2$ in the above gives $r_n=n^2a_0/Z$ and $E_n=-13.6\,\mathrm{eV}\cdot Z^2/n^2$.

Bohr's theory can be assessed as follows. It successfully computes the wavelengths in the spectra of hydrogen and hydrogen-like ions, but it cannot give the intensities of the lines, nor explain fine structure or the spectra of many-electron atoms (even helium, with only two electrons). It is also logically inconsistent: it uses classical mechanics to compute circular orbits while arbitrarily decreeing that the accelerated electron does not radiate; the quantization of angular momentum is imposed by hand; and it says nothing about how the electron passes between two stationary states (Rutherford asked how the electron "knows in advance" which orbit to jump to). Even so, the stationary states, energy levels, frequency condition and quantization of angular momentum of Bohr's theory remain correct concepts today; only the picture of definite electron orbits was rejected by quantum mechanics. Bohr received the 1922 Nobel Prize in Physics for this work, and the institute he founded in Copenhagen became the center of quantum mechanics.

### 4.1.4. Quantum-Mechanical Treatment of the Hydrogen Atom

The electron in a hydrogen atom moves in the Coulomb field of the nucleus, with potential energy $U(r)=-\frac{e^2}{4\pi\varepsilon_0r}$ depending only on the distance (a central field). The time-independent Schrödinger equation is

$$
-\frac{\hbar^2}{2m_{\mathrm{e}}}\nabla^2\psi-\frac{e^2}{4\pi\varepsilon_0r}\psi=E\psi.
$$
Since the potential is spherically symmetric, we use spherical coordinates $(r,\theta,\varphi)$. In these coordinates the **Laplace operator** can be written as ([2.5.5](/2.5.5#sec-5.1.1))

$$
\nabla^2=\frac1{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial}{\partial r}\Big)-\frac{\hat L^2}{\hbar^2r^2},\qquad
\hat L^2=-\hbar^2\Big[\frac1{\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial}{\partial\theta}\Big)+\frac1{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\Big],
$$
where $\hat L^2$ is the operator of the squared orbital angular momentum $\hat{\boldsymbol{L}}^2=(\hat{\boldsymbol{r}}\times\hat{\boldsymbol{p}})^2$ and acts only on the angles. The operator of the $z$ component of angular momentum is $\hat L_z=-\mathrm{i}\hbar\,\partial/\partial\varphi$. Using **separation of variables**, we set $\psi(r,\theta,\varphi)=R(r)Y(\theta,\varphi)$, and the equation splits into an angular and a radial part.

Consider the angular part first. The eigenvalue equation $-\mathrm{i}\hbar\,\mathrm{d}\Phi/\mathrm{d}\varphi=L_z\Phi$ for $\hat L_z$ has the solution $\Phi=\mathrm{e}^{\mathrm{i}L_z\varphi/\hbar}$. The **wave function** must be single-valued, $\Phi(\varphi+2\pi)=\Phi(\varphi)$, so $L_z=m_l\hbar$ with $m_l$ an integer. The operators $\hat L^2$ and $\hat L_z$ have common **eigenfunctions**, whose eigenvalue equations

$$
\hat L^2Y=\lambda\hbar^2Y,\qquad \hat L_zY=m_l\hbar Y
$$
are precisely the **eigenvalue** problem on the sphere treated in [2.5.5](/2.5.5#sec-5.4.2): solutions bounded at the poles exist only for $\lambda=l(l+1)$ with $l\ge\lvert m_l\rvert$, and they are the **spherical harmonics** $Y_l^{m_l}(\theta,\varphi)\propto P_l^{\lvert m_l\rvert}(\cos\theta)\,\mathrm{e}^{\mathrm{i}m_l\varphi}$ (where $P_l^{\lvert m_l\rvert}$ are the **associated Legendre functions**). The spherical harmonics are orthonormal on the sphere: $\int Y_l^{m*}Y_{l'}^{m'}\,\mathrm{d}\Omega=\delta_{ll'}\delta_{mm'}$. For example,

$$
Y_0^0=\frac1{\sqrt{4\pi}},\qquad Y_1^0=\sqrt{\frac3{4\pi}}\cos\theta,\qquad Y_1^{\pm1}=\mp\sqrt{\frac3{8\pi}}\sin\theta\,\mathrm{e}^{\pm\mathrm{i}\varphi}.
$$

**Theorem 4.1.1 (Quantization of Orbital Angular Momentum)** In a central field, the magnitude and the $z$ component of the orbital angular momentum of an electron can take only the values

$$
L=\sqrt{l(l+1)}\,\hbar,\quad l=0,1,2,\dots;\qquad L_z=m_l\hbar,\quad m_l=0,\pm1,\dots,\pm l.
\tag{4.3}
$$

For a given $l$, $L_z$ has $2l+1$ possible values; that is, the angular momentum has only $2l+1$ possible orientations in space ($\cos\theta=m_l/\sqrt{l(l+1)}$). This is called *space quantization*. For $l=2$, for instance, $L=\sqrt6\,\hbar$ and $L_z=0,\pm\hbar,\pm2\hbar$, giving 5 orientations. Because $\lvert L_z\rvert<L$ (for $l\ge1$), $\boldsymbol{L}$ can never point exactly along the $z$ axis; $L_x$ and $L_y$ are uncertain, and $\boldsymbol{L}$ may be pictured as lying on a cone about the $z$ axis.

Now the radial part. Substituting $\psi=RY_l^{m_l}$ gives the radial equation

$$
-\frac{\hbar^2}{2m_{\mathrm{e}}}\frac1{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\Big(r^2\frac{\mathrm{d}R}{\mathrm{d}r}\Big)+\Big[\frac{l(l+1)\hbar^2}{2m_{\mathrm{e}}r^2}-\frac{e^2}{4\pi\varepsilon_0r}\Big]R=ER.
$$
The first term in the brackets is the "centrifugal potential energy", and the bracket as a whole is the **effective potential** $\frac{L^2}{2mr^2}+U(r)$ of the classical central-force problem ([5.1.4](/5.1.4)), with $L^2$ replaced by $l(l+1)\hbar^2$. We seek **bound state** solutions with $E<0$, requiring $R$ to be finite at $r=0$ and to tend to zero as $r\to\infty$. The result is:

**Theorem 4.1.2 (Energy Levels of the Hydrogen Atom)** The bound-state energies of the hydrogen atom can take only the values

$$
E_n=-\frac{m_{\mathrm{e}}e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac1{n^2}=-\frac{13.6\,\mathrm{eV}}{n^2},\qquad n=1,2,3,\dots,
\tag{4.4}
$$
and the angular quantum number must satisfy $l\le n-1$.

This coincides exactly with Bohr's result (4.2), but here the quantization is a natural consequence of the equation and the standard conditions rather than an imposed assumption. The radial function $R_{nl}$ has $n-l-1$ nodes; the first few are

$$
R_{10}=\frac2{a_0^{3/2}}\mathrm{e}^{-r/a_0},\qquad
R_{20}=\frac1{2\sqrt2\,a_0^{3/2}}\Big(2-\frac r{a_0}\Big)\mathrm{e}^{-r/(2a_0)},\qquad
R_{21}=\frac1{2\sqrt6\,a_0^{3/2}}\frac r{a_0}\mathrm{e}^{-r/(2a_0)}.
$$

**Definition 4.1.1 (Quantum Numbers)** A stationary state of the electron in a hydrogen atom, $\psi_{nlm_l}=R_{nl}(r)Y_l^{m_l}(\theta,\varphi)$, is specified by three quantum numbers:

| Quantum number | Values | Determines |
|---|---|---|
| **Principal quantum number** $n$ | $1,2,3,\dots$ | energy $E_n=-13.6\,\mathrm{eV}/n^2$ |
| **Azimuthal quantum number** (orbital quantum number) $l$ | $0,1,\dots,n-1$ | magnitude of orbital angular momentum $L=\sqrt{l(l+1)}\hbar$ |
| **Magnetic quantum number** $m_l$ | $0,\pm1,\dots,\pm l$ | $z$ component of orbital angular momentum $L_z=m_l\hbar$ |

The energy depends only on the principal quantum number: for a given $n$ there are $\sum_{l=0}^{n-1}(2l+1)=n^2$ distinct states with the same energy. When several linearly independent states have the same energy, the level is said to exhibit *degeneracy*, and the states are called degenerate states. The degeneracy in $m_l$ comes from the spherical symmetry of the potential (no direction in space is special); the degeneracy in $l$ is specific to the Coulomb potential $1/r$ and is lifted in many-electron atoms such as the alkali metals (§4.2.5). By spectroscopic convention, states with $l=0,1,2,3,\dots$ are denoted s, p, d, f, …, and combined with the principal quantum number as 1s, 2s, 2p, 3d, and so on.

### 4.1.5. Electron Clouds and Probability Distributions

In quantum mechanics the electron has no definite orbit; we can only give the probability of finding it at each place. The quantity $\lvert\psi_{nlm_l}(r,\theta,\varphi)\rvert^2$ is the probability density of finding the electron at $(r,\theta,\varphi)$; representing this distribution by the density of dots gives the familiar picture of the *electron cloud*. In chemistry the one-electron spatial wave function $\psi_{nlm_l}$ is called an **atomic orbital**; here "orbital" means a probability distribution, not the circular orbit of the Bohr model. Since $R$ and $Y$ are normalized separately,

$$
\int\lvert\psi\rvert^2\,\mathrm{d}V=\int_0^\infty\lvert R_{nl}\rvert^2r^2\,\mathrm{d}r\int\lvert Y_l^{m_l}\rvert^2\,\mathrm{d}\Omega=1,\qquad \mathrm{d}\Omega=\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi.
$$

Consider the angular distribution first. The probability of finding the electron in the solid angle $\mathrm{d}\Omega$ in the direction $(\theta,\varphi)$ is $\lvert Y_l^{m_l}\rvert^2\mathrm{d}\Omega$. It is independent of $\varphi$, so the electron cloud is always rotationally symmetric about the $z$ axis. The distribution of an s electron ($l=0$) is spherically symmetric; for p electrons, $\lvert Y_1^0\rvert^2\propto\cos^2\theta$ ($m_l=0$) is concentrated on both sides along the $z$ axis, whereas $\lvert Y_1^{\pm1}\rvert^2\propto\sin^2\theta$ ($m_l=\pm1$) is concentrated near the $xy$ plane.

**Definition 4.1.2 (Radial Probability Density)** The probability of finding the electron in the spherical shell between radii $r$ and $r+\mathrm{d}r$ is $P_{nl}(r)\,\mathrm{d}r$, where

$$
P_{nl}(r)=\lvert R_{nl}(r)\rvert^2r^2
$$
is called the **radial probability density**.

![Radial probability densities r²R_nl² for the states n = 1, 2, 3 of hydrogen (in units of a_0). States with l = n - 1 have a single maximum, located at r = n²a_0, the orbital radius of the Bohr model; the other states have n - l - 1 nodes](./plots/radial-distribution.py)

For the ground state 1s, $P_{10}=\frac{4r^2}{a_0^3}\mathrm{e}^{-2r/a_0}$ has its maximum at $r=a_0$: the electron is most likely to be found in a shell of unit thickness at the Bohr radius, yet it has some probability of being found at any radius (the mean radius is $\frac32a_0$). In general, states with $l=n-1$ (2p, 3d, …) have a single maximum, exactly at $r=n^2a_0$; this is the quantum-mechanical counterpart of the Bohr orbit. For a given $n$, the smaller $l$ is, the closer the inner small peaks of the radial distribution lie to the nucleus, which is important for the energy levels of many-electron atoms (§4.2.5).

## 4.2. Electron Spin and Spin–Orbit Coupling

### 4.2.1. Fine Structure and the Zeeman Effect

With spectrometers of higher resolution, many spectral lines of atoms turn out to consist of two or more closely spaced lines. This is called the *fine structure* of the spectrum. The best known example is the yellow D line of sodium, a doublet with wavelengths $589.0\,\mathrm{nm}$ and $589.6\,\mathrm{nm}$. The three quantum numbers $(n,l,m_l)$ alone cannot explain fine structure.

Another clue comes from magnetic fields. An electron orbiting the nucleus is equivalent to a circular current and has an orbital **magnetic moment**. Classically, the magnetic moment of an orbital motion with charge $-e$ and mass $m_{\mathrm{e}}$ is proportional to the angular momentum, $\boldsymbol{\mu}=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}$ ([5.3.8](/5.3.8)); this relation continues to hold in quantum mechanics, so that $\mu_z=-m_l\mu_{\mathrm{B}}$.

**Definition 4.2.1 (Bohr Magneton)** The constant

$$
\mu_{\mathrm{B}}=\frac{e\hbar}{2m_{\mathrm{e}}}=9.274\times10^{-24}\,\mathrm{J/T}=5.788\times10^{-5}\,\mathrm{eV/T}
$$
is called the **Bohr magneton**; it is the natural unit of atomic magnetic moments.

In an external magnetic field $\boldsymbol{B}$ along the $z$ direction, the additional energy of the magnetic moment is

$$
E_B=-\boldsymbol{\mu}\cdot\boldsymbol{B}=m_l\mu_{\mathrm{B}}B,\qquad m_l=0,\pm1,\dots,\pm l,
$$
so an energy level splits into $2l+1$ equally spaced levels, and a spectral line splits into several lines accordingly. When the light source is placed in a strong magnetic field, a spectral line splits into several closely spaced lines; this is the *Zeeman effect*, discovered by Zeeman in 1896. In a field of $1\,\mathrm{T}$ the splitting $\mu_{\mathrm{B}}B$ is only about $6\times10^{-5}\,\mathrm{eV}$. Since transitions occur only between levels with $\Delta m_l=0,\pm1$, this theory predicts that every line splits into three (the normal Zeeman effect). But as early as 1897 Preston found that most lines split into other numbers of components, with different spacings (the anomalous Zeeman effect), which likewise calls for additional **degrees of freedom** to explain.

### 4.2.2. The Stern–Gerlach Experiment

In 1922 Stern and Gerlach tested the space quantization of angular momentum directly with an atomic beam, in what is now called the *Stern–Gerlach experiment*. In a magnetic field that is inhomogeneous along the $z$ direction, the potential energy $-\mu_zB_z$ of a magnetic moment varies with position, and the atoms experience a force

$$
F_z=\mu_z\frac{\partial B_z}{\partial z}.
$$
If $\mu_z$ can take only a few discrete values, the beam splits into several beams after passing through the field and deposits on the screen as several discrete traces rather than the continuous smear predicted classically. In the experiment the beam of silver atoms did split into an upper and a lower beam, demonstrating space quantization. Separating beams of atoms in a specific state is still a common "state selection" technique in atomic physics.

The result, however, also posed a new contradiction. The outermost shell of a silver atom contains a single 5s electron, and the angular momenta and magnetic moments of the inner electrons cancel completely, so the orbital angular momentum of the atom is $l=0$ and $\mu_z$ should have the single value 0: the beam should not split. Even for nonzero orbital angular momentum the number of components $2l+1$ is odd, not 2. A similar experiment on ground-state hydrogen (1927) also gave two beams. Thus the description of the electron in an atom by $(n,l,m_l)$ is incomplete.

### 4.2.3. Electron Spin

In 1925 Uhlenbeck and Goudsmit proposed that besides its orbital motion the electron has an intrinsic angular momentum, its spin, and an associated spin magnetic moment; the electron is negatively charged, so the spin magnetic moment is opposite to the spin angular momentum.

The picture of the electron as a small spinning ball cannot be maintained: with the classical electron radius $2.8\times10^{-15}\,\mathrm{m}$, obtaining an angular momentum of order $\hbar/2$ would require a surface speed tens of times the speed of light. Electron spin has no classical counterpart; it is an intrinsic property of the electron, like mass and charge. All angular momenta in quantum mechanics obey the same quantization rules, so an analogy with orbital angular momentum is possible.

**Definition 4.2.2 (Electron Spin)** The intrinsic angular momentum $\boldsymbol{S}$ of the electron is called its **electron spin**. Its magnitude and $z$ component are

$$
S=\sqrt{s(s+1)}\,\hbar=\frac{\sqrt3}2\hbar,\qquad S_z=m_s\hbar,\quad m_s=\pm\frac12,
$$
where $s=\frac12$ is called the **spin quantum number** and $m_s$ the **spin magnetic quantum number**.

By analogy with the $2l+1$ values of $m_l$, $m_s$ should have $2s+1$ values; the Stern–Gerlach experiment shows only two, so $2s+1=2$ and $s=\frac12$, which is not an integer. The $z$ component of the spin magnetic moment is $\mu_{s,z}=-g_{\mathrm{e}}m_s\mu_{\mathrm{B}}\approx\mp\mu_{\mathrm{B}}$ with $g_{\mathrm{e}}\approx2.002$ ([5.3.8](/5.3.8#sec-8.2.2)): the ratio of magnetic moment to angular momentum for spin is twice that for orbital motion. The splitting of the silver beam into two in the magnetic field corresponds precisely to the two orientations $m_s=\pm\frac12$ of the 5s electron. In 1928 Dirac's relativistic quantum mechanics derived electron spin and $g_{\mathrm{e}}=2$ theoretically.

### 4.2.4. Spin–Orbit Coupling and Term Symbols

The electron has both orbital angular momentum $\boldsymbol{L}$ and spin angular momentum $\boldsymbol{S}$, and its state is related to the total angular momentum

$$
\boldsymbol{J}=\boldsymbol{L}+\boldsymbol{S}.
$$
The combination of the two angular momenta results from the magnetic interaction between them (see below) and is called *spin–orbit coupling*. $\boldsymbol{J}$ is also quantized:

$$
J=\sqrt{j(j+1)}\,\hbar,\qquad j=l\pm\frac12\ (l\ge1),\quad j=\frac12\ (l=0);\qquad J_z=m_j\hbar,\quad m_j=-j,\dots,j,
$$
and $j$ is called the total angular momentum quantum number. For $l=1$, for instance, $L=\sqrt2\hbar$ and $j=\frac32$ or $\frac12$, with $J=\frac{\sqrt{15}}2\hbar$ or $\frac{\sqrt3}2\hbar$; in the classical vector model, $\boldsymbol{L}$ and $\boldsymbol{S}$ are roughly "parallel" or "antiparallel".

**Definition 4.2.3 (Term Symbol)** The energy state of an atom is denoted by the symbol

$$
n\,{}^{2s+1}L_j
$$
which is called the **term symbol**. Here $n$ is the principal quantum number; $L$ is the letter code of the orbital angular momentum quantum number, with $l=0,1,2,3,\dots$ written $\mathrm{S},\mathrm{P},\mathrm{D},\mathrm{F},\dots$ (upright capital letters); the left superscript $2s+1$ is the spin multiplicity, and the right subscript is $j$.

For example, the state with $n=3$, $l=1$, $s=\frac12$, $j=\frac32$ is written $3\,{}^2\mathrm{P}_{3/2}$. For a single valence electron $2s+1=2$ (a doublet). In many-electron atoms, $L$, $S$ and $J$ in the term symbol are the total orbital angular momentum, total spin and total angular momentum quantum numbers obtained by combining the individual electrons (LS coupling), with the same notation.

### 4.2.5. Energy Levels of Alkali-Metal Atoms

Alkali-metal atoms such as lithium, sodium and potassium have a single valence electron in the outermost shell; the inner electrons and the nucleus form an *atomic core* of net charge $+e$. This structure resembles that of the hydrogen atom, so the spectra of the alkali metals resemble that of hydrogen as well. The difference is that their energy levels depend not only on $n$ but also on $l$, for two reasons:

- Orbital penetration: for electrons with small $l$ (especially s electrons) the radial distribution has small inner peaks reaching into the atomic core (the figure in §4.1.5), where the electron feels a nuclear charge larger than $+e$ and its energy is accordingly lowered.
- Core polarization: the valence electron repels the electrons in the core, displacing the center of negative charge of the core from the nucleus, so that the core becomes an **electric dipole** pointing toward the valence electron and exerts an additional attraction on it, which also lowers its energy.

Both effects make the valence electron feel more positive charge, so its energy is lower than that of the hydrogen level with the same $n$. The energy levels of alkali metals are often written

$$
E_{nl}=-\frac{13.6\,\mathrm{eV}}{(n-\Delta_l)^2},
$$
where $\Delta_l$ is called the *quantum defect* and is larger for smaller $l$. For sodium, $\Delta_{\mathrm{s}}\approx1.37$, $\Delta_{\mathrm{p}}\approx0.88$, $\Delta_{\mathrm{d}}\approx0.01$; the ionization energy of the 3s ground state is then $13.6/(3-1.37)^2\,\mathrm{eV}\approx5.1\,\mathrm{eV}$, in agreement with the experimental value $5.14\,\mathrm{eV}$. A d electron hardly penetrates the core, and its energy is almost the same as in hydrogen.

Fine structure arises from spin–orbit coupling. In the rest frame of the electron, the nucleus moves around it and produces a magnetic field $\boldsymbol{B}$. The spin magnetic moment of the electron has an additional energy in this field, $E_{\mathrm{so}}=-\boldsymbol{\mu}_s\cdot\boldsymbol{B}\approx\pm\mu_{\mathrm{B}}B$ (the spin–orbit coupling energy, a relativistic effect), so each level with $l\ge1$ splits into two according to $j=l\pm\frac12$, and the corresponding spectral line splits into two. The sodium 3P level splits into $3\,{}^2\mathrm{P}_{3/2}$ and $3\,{}^2\mathrm{P}_{1/2}$; transitions to the ground state $3\,{}^2\mathrm{S}_{1/2}$ ($l=0$, no splitting) emit the D2 line ($589.0\,\mathrm{nm}$) and the D1 line ($589.6\,\mathrm{nm}$), respectively. The energy difference between the two is

$$
\Delta E=hc\Big(\frac1{\lambda_2}-\frac1{\lambda_1}\Big)\approx2.1\times10^{-3}\,\mathrm{eV},
$$
equivalent to the valence electron sitting in an internal magnetic field of about $18\,\mathrm{T}$. The fine-structure splitting grows rapidly with atomic number: for the $n=2$ level of hydrogen it is only $4.5\times10^{-5}\,\mathrm{eV}$. The doublets of the alkali metals were also among the grounds on which Uhlenbeck and Goudsmit proposed the spin hypothesis.

## 4.3. Identical Particles and the Pauli Exclusion Principle

### 4.3.1. Indistinguishability of Microscopic Particles

**Definition 4.3.1 (Identical Particles)** Microscopic particles whose intrinsic properties (mass, charge, spin, etc.) are exactly the same are called **identical particles**, for example all electrons or all protons.

Classical particles, even if exactly alike, can be told apart by following their individual orbits. Quantum particles have no definite orbits: once the wave functions of two electrons overlap, it is impossible to tell which is which. Identical particles are indistinguishable. Hence exchanging two particles leaves the physical state, and therefore the probability density, unchanged:

$$
\lvert\psi(1,2)\rvert^2=\lvert\psi(2,1)\rvert^2,
$$
where 1 and 2 stand for all the coordinates (position and spin) of the two particles. It follows that $\psi(2,1)=\pm\psi(1,2)$: the wave function of a system of identical particles can only be symmetric under exchange (sign $+$) or antisymmetric under exchange (sign $-$).

Let us construct the wave function of a two-particle system from single-particle wave functions. Let the single-particle states be $A$ and $B$. Then $\psi_A(1)\psi_B(2)$ and $\psi_A(2)\psi_B(1)$ both satisfy the two-particle **Schrödinger equation** (neglecting interactions), but neither has a definite exchange symmetry. Since the two occur with equal probability, the wave function of the system should be their equal-weight superposition:

$$
\psi_{\mathrm{S}}(1,2)=\frac1{\sqrt2}\big[\psi_A(1)\psi_B(2)+\psi_A(2)\psi_B(1)\big],\qquad
\psi_{\mathrm{A}}(1,2)=\frac1{\sqrt2}\big[\psi_A(1)\psi_B(2)-\psi_A(2)\psi_B(1)\big].
$$

### 4.3.2. Fermions and Bosons

**Definition 4.3.2** Particles whose spin quantum number $s$ is a half-integer ($\frac12,\frac32,\dots$) are called **fermions**; the wave function of a system of fermions is antisymmetric under exchange. Particles with $s$ zero or an integer are called **bosons**; the wave function of a system of bosons is symmetric under exchange.

This connection between spin and symmetry is an experimental fact; Pauli proved it in 1940 from relativistic quantum field theory (the spin–statistics theorem). Fermions with $s=\frac12$ include the electron, proton, neutron, neutrino, muon, quarks, and the $\ce{^3He}$ nucleus; the $\Delta$ baryon has $s=\frac32$. Bosons include the photon ($s=1$), π and K mesons ($s=0$), the $\ce{^4He}$ nucleus ($s=0$) and the deuteron ($s=1$). A composite particle made of an even number of fermions is a boson, and one made of an odd number is a fermion; thus the $\ce{^4He}$ atom is a boson and the $\ce{^3He}$ atom is a fermion, and the two kinds of liquid helium behave completely differently at low temperatures.

**Theorem 4.3.1 (Pauli Exclusion Principle)** Two (or more) identical fermions cannot occupy the same single-particle state.

**Proof** Set $A=B$. The antisymmetric wave function $\psi_{\mathrm{A}}(1,2)=\frac1{\sqrt2}[\psi_A(1)\psi_A(2)-\psi_A(2)\psi_A(1)]=0$, so such a state does not exist. The antisymmetric wave function of $N$ fermions can be written as a determinant whose entries are $\psi_{A_i}(j)$ (the Slater determinant); if two single-particle states coincide, two rows are equal and the determinant vanishes. $\square$

The symmetric wave function of bosons does not vanish for $A=B$: any number of bosons can occupy the same single-particle state, free of the restriction of the exclusion principle, and identical bosons even tend to cluster in the same state. Photons are bosons, and a large number of photons can be in the same state, forming a macroscopic classical light wave; a laser ([5.5.5](/5.5.5)) is such a state. Electrons are fermions and cannot crowd into the same state, so there is no "classical electron wave", and electron **interference** can appear only as the interference of the **probability amplitude** of a single electron.

Antisymmetry also makes two electrons with parallel spins avoid each other in space, which affects their electrostatic interaction energy. This purely quantum "exchange interaction" is the origin of the covalent bond, Hund's rule (§4.4.3) and ferromagnetism ([5.3.8](/5.3.8)).

### 4.3.3. Fermi–Dirac and Bose–Einstein Statistics

Classical Maxwell–Boltzmann statistics treats particles as distinguishable. Once indistinguishability and the exclusion principle are taken into account, quantum statistics gives the mean number of particles in each single-particle state in equilibrium.

**Theorem 4.3.2 (Fermi–Dirac Distribution)** In equilibrium at temperature $T$, in an **ideal gas** of identical fermions, the mean number of particles in a single-particle state of energy $E$ is

$$
\bar N(E)=\frac1{\mathrm{e}^{(E-\mu)/(k_{\mathrm{B}}T)}+1},
\tag{4.5}
$$
where the chemical potential $\mu=\mu(T)$ is determined by the total number of particles.

By the exclusion principle, $0\le\bar N\le1$. At $T=0$, $\bar N$ is a step: all states with $E<\mu(0)$ are occupied and all states with $E>\mu(0)$ are empty; $E_{\mathrm{F}}=\mu(0)$ is called the **Fermi energy** ([5.5.6](/5.5.6)). At moderate temperatures ($k_{\mathrm{B}}T\ll E_{\mathrm{F}}$) we have $\mu\approx E_{\mathrm{F}}$; thermal excitation energies are only of order $k_{\mathrm{B}}T$, so only particles within a range of width about $k_{\mathrm{B}}T$ around $E_{\mathrm{F}}$ can be excited to higher states, and the corners of the step are rounded into a transition band. For $k_{\mathrm{B}}T\gg E_{\mathrm{F}}$ the step disappears completely. The $E_{\mathrm{F}}$ of electrons in a metal is a few electron volts, far larger than $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$ at room temperature, so the electron gas in a metal is almost in its $T=0$ state at room temperature. This explains the very small electronic specific heat, which classical theory could not account for.

**Theorem 4.3.3 (Bose–Einstein Distribution)** Under the same conditions, in an ideal gas of identical bosons, the mean number of particles in a single-particle state of energy $E$ is

$$
\bar N(E)=\frac1{\mathrm{e}^{(E-\mu)/(k_{\mathrm{B}}T)}-1}.
\tag{4.6}
$$

For every state we need $0\le\bar N<\infty$, so $\mu$ must be smaller than the lowest single-particle energy $E_0$; taking $E_0=0$, we have $\mu<0$. At fixed particle number density, as the temperature decreases $\mu$ approaches 0 from below, and the occupation of the ground state, $\bar N_0=1/(\mathrm{e}^{-\mu/(k_{\mathrm{B}}T)}-1)$, grows rapidly. Theory shows that there is a **critical temperature** $T_{\mathrm{c}}$,

$$
k_{\mathrm{B}}T_{\mathrm{c}}=\frac{2\pi\hbar^2}{m}\Big(\frac{n}{2.612}\Big)^{2/3},
$$
below which a macroscopic number of particles gather in the same lowest-energy state; as $T\to0$ all particles are in the ground state. This phenomenon is called *Bose–Einstein condensation* (BEC) and was predicted by Einstein in 1925. For dilute atomic gases $T_{\mathrm{c}}$ is only of order $10^{-7}\,\mathrm{K}$. In 1995 Cornell and Wieman, using rubidium atoms cooled by laser cooling and evaporative cooling, and Ketterle, using sodium atoms, achieved BEC independently; the three shared the 2001 Nobel Prize in Physics. In a BEC a large number of atoms are in the same quantum state, and their **matter waves** are coherent like laser light, which can be used to build atom interferometers and precision quantum frequency standards; the superfluidity of liquid helium is also closely related to BEC.

Finally, consider the classical limit. If $E-\mu\gg k_{\mathrm{B}}T$, the $\pm1$ in the denominators of both distributions can be neglected:

$$
\bar N(E)\approx\mathrm{e}^{\mu/(k_{\mathrm{B}}T)}\,\mathrm{e}^{-E/(k_{\mathrm{B}}T)},
$$
which is precisely the classical **Boltzmann factor**: quantum statistics passes over into Maxwell–Boltzmann statistics (the **Boltzmann distribution**, [5.2.1](/5.2.1)). This condition is equivalent to $\bar N\ll1$: on average there is much less than one particle per state, so particles rarely have a chance to be in the same state and the effects of indistinguishability can be neglected. Quantitatively, the condition is that the number density $n$ and the thermal **de Broglie wavelength** $\lambda_{\mathrm{th}}=h/\sqrt{2\pi mk_{\mathrm{B}}T}$ satisfy $n\lambda_{\mathrm{th}}^3\ll1$; that is, the mean spacing between particles is much larger than their de Broglie wavelength. For nitrogen at normal temperature and pressure $n\lambda_{\mathrm{th}}^3\approx2\times10^{-7}$ and classical statistics applies perfectly; the free electrons in a metal, having small mass and high density, have $n\lambda_{\mathrm{th}}^3\sim10^4$ at room temperature and must be treated with Fermi–Dirac statistics.

![Left: the Fermi–Dirac distribution at several temperatures (with μ ≈ E_F); it is a step at T = 0, and as the temperature rises the region of width about k_BT around E_F is rounded. Right: the three distributions as functions of (E - μ)/k_BT (logarithmic scale); they coincide for E - μ ≫ k_BT](./plots/quantum-statistics.py)

## 4.4. Electron Configurations of Atoms

### 4.4.1. The Four Quantum Numbers

Each electron in a many-electron atom can be regarded approximately as moving independently in the average central field formed by the nucleus and the other electrons, and its state is completely described by four quantum numbers $(n,l,m_l,m_s)$:

| Quantum number | Values | Physical meaning |
|---|---|---|
| Principal quantum number $n$ | $1,2,3,\dots$ | the main factor determining the energy |
| Azimuthal quantum number $l$ | $0,1,\dots,n-1$ | orbital angular momentum $L=\sqrt{l(l+1)}\hbar$; strongly affects the energy, smaller $l$ giving lower energy |
| Magnetic quantum number $m_l$ | $0,\pm1,\dots,\pm l$ | $L_z=m_l\hbar$; causes splitting of levels in a magnetic field |
| Spin magnetic quantum number $m_s$ | $\pm\frac12$ | $S_z=m_s\hbar$; produces fine structure |

### 4.4.2. The Pauli Exclusion Principle and Shells

Applied to the electrons in an atom, the Pauli exclusion principle gives Pauli's original formulation of 1925: no two electrons in an atom can have the same four quantum numbers $(n,l,m_l,m_s)$.

**Definition 4.4.1** The electron states in an atom with the same principal quantum number $n$ form an **electron shell**; the shells $n=1,2,3,4,5,\dots$ are denoted K, L, M, N, O, … in turn. The states with the same $n$ and $l$ form a **subshell**, denoted s, p, d, f, g, … in turn.

In a subshell $m_l$ takes $2l+1$ values and $m_s$ takes 2 values, so it can hold at most $2(2l+1)$ electrons: 2, 6, 10 and 14 for the s, p, d and f subshells, respectively. The $n$th shell can hold at most

$$
Z_n=\sum_{l=0}^{n-1}2(2l+1)=2n^2
$$
electrons: 2, 8, 18 and 32 for the K, L, M and N shells. The numbers of electrons in the subshells of an atom are called its *electron configuration*, written $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^6\cdots$, where the superscript is the number of electrons in that subshell.

### 4.4.3. The Aufbau Principle and Hund's Rule

In the ground state of an atom, electrons preferentially occupy the states of lowest energy, as long as the exclusion principle is not violated; this is called the *aufbau principle*. In many-electron atoms the energy of a subshell depends on $l$ as well as $n$ (orbital penetration, §4.2.5), so the order of filling is not always to fill one shell completely before the next:

$$
1\mathrm{s}<2\mathrm{s}<2\mathrm{p}<3\mathrm{s}<3\mathrm{p}<4\mathrm{s}<3\mathrm{d}<4\mathrm{p}<5\mathrm{s}<4\mathrm{d}<5\mathrm{p}<6\mathrm{s}<4\mathrm{f}<5\mathrm{d}<6\mathrm{p}<7\mathrm{s}<5\mathrm{f}<\cdots
$$
This order can be summarized by the Madelung rule: subshells are filled in order of increasing $n+l$, and for equal $n+l$ the one with smaller $n$ is filled first. The Chinese chemist Xu Guangxian gave another approximate rule: the energy of a subshell increases with $n+0.7l$. For example, $n+0.7l=4.4$ for 3d, larger than $4.0$ for 4s, so the last electron of potassium and calcium goes into 4s rather than 3d. From this order it also follows that any shell holds at most 8 electrons when it is the outermost shell and at most 18 when it is the next-to-outermost.

*Hund's rule*: when electrons fill a set of degenerate orbitals of equal energy (such as the three 2p orbitals), they first occupy different orbitals singly with parallel spins, and only then pair up; this maximizes the total spin and minimizes the energy, and its origin is the exchange interaction of §4.3.2. For example, the three 2p electrons of the nitrogen atom $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^3$ occupy three different orbitals with parallel spins. Equivalent orbitals that are completely filled ($\mathrm{p}^6$, $\mathrm{d}^{10}$, $\mathrm{f}^{14}$), half-filled ($\mathrm{p}^3$, $\mathrm{d}^5$, $\mathrm{f}^7$) or empty are relatively stable (a special case of Hund's rule), which explains some exceptions to the filling order:

- Chromium ($Z=24$): $1\mathrm{s}^2\,2\mathrm{s}^2\,2\mathrm{p}^6\,3\mathrm{s}^2\,3\mathrm{p}^6\,3\mathrm{d}^5\,4\mathrm{s}^1$, that is, $[\ce{Ar}]\,3\mathrm{d}^5\,4\mathrm{s}^1$, rather than $3\mathrm{d}^4\,4\mathrm{s}^2$ as the order would suggest;
- Copper ($Z=29$): $[\ce{Ar}]\,3\mathrm{d}^{10}\,4\mathrm{s}^1$, rather than $3\mathrm{d}^9\,4\mathrm{s}^2$.

This is how the structure of the periodic table arises: each period begins with a new s subshell and ends when the p subshell is filled (a noble gas); in periods 4 and 5 the d subshell is inserted (the transition elements), and in periods 6 and 7 the f subshell is inserted as well (the lanthanides and actinides). Elements in the same group have the same valence-electron configuration and hence similar chemical properties. This is one of the most important contributions of quantum mechanics to chemistry.

## 4.5. Summary of Quantum Mechanics

### 4.5.1. Basic Concepts and Methods

The main content of the quantum mechanics part ([5.5.1](/5.5.1) through this chapter) can be summarized as follows:

- two important concepts: **wave–particle duality** and quantization;
- one important relation: the **Heisenberg uncertainty relation**;
- two basic postulates: the statistical interpretation of the wave function and the Schrödinger equation ([5.5.3](/5.5.3));
- two basic principles: the **superposition principle of quantum states** and the Pauli exclusion principle;
- one key constant: the **Planck constant** $h$; one important effect: the **tunnel effect**;
- three important experiments: **diffraction** of electrons by crystals, single-slit diffraction and double-slit interference of electrons, and the Stern–Gerlach experiment.

Quantum mechanics treats problems as follows:

1. The state of a system is described by a wave function (probability amplitude) $\Psi$.
2. Mechanical quantities are represented by Hermitian operators, obtained by "operatorizing" the classical quantities ($\boldsymbol{p}\to-\mathrm{i}\hbar\nabla$), such as the **Hamiltonian** $\hat H$ and the angular momentum operators $\hat L^2$, $\hat L_z$.
3. The eigenvalue equation of a quantity $A$ is $\hat A\psi_n=A_n\psi_n$; solving it under the standard conditions on the wave function gives the **eigenvalues** $A_n$ and eigenfunctions $\psi_n$, and the values that the quantity can take are precisely these eigenvalues.
4. When the system is in an eigenstate of $\hat A$, a measurement of $A$ gives the definite value $A_n$; when it is in a superposition of eigenstates $\Psi=\sum_nC_n\psi_n$ (with $\psi_n$ orthonormal), the probability of obtaining $A_n$ is $\lvert C_n\rvert^2$, so $A$ has the definite mean value

$$
\langle A\rangle=\sum_n\lvert C_n\rvert^2A_n=\int\Psi^*\hat A\Psi\,\mathrm{d}x.
$$

### 4.5.2. Quantum Physics and Classical Physics

When $h\to0$ (macroscopic processes whose action is much larger than $h$) or the quantum number $n\to\infty$, the conclusions of quantum physics approach those of classical physics. This is the **correspondence principle** ([5.5.3](/5.5.3)). For instance, the energy levels of a particle in a square well tend to a continuum and the probability distribution becomes uniform as $n\to\infty$; the effect of the uncertainty relation on macroscopic bodies is far smaller than the measurement accuracy; and the probability distribution of a harmonic oscillator with a large quantum number approaches the classical one. Quantum mechanics does not negate classical physics but determines its range of validity.

### 4.5.3. The Debate on the Interpretation of Quantum Mechanics

The Copenhagen school, represented by Bohr, Heisenberg, Born and Pauli, holds that:

1. Wave and particle aspects are complementary: they never appear in the same measurement, but both are necessary for a complete description of microscopic phenomena. This is the *complementarity principle*.
2. Quantum mechanics is a statistical theory; the uncertainty relation is a manifestation of the wave nature of particles and is in principle unavoidable.
3. The present form of quantum mechanics and its interpretation are complete.

Opponents, represented by Einstein, de Broglie and Schrödinger, held that the statistical interpretation of the wave function makes sense only for an ensemble of many particles (Einstein: "God does not play dice"), that quantum mechanics is not complete, and that one should look further for the unified nature of waves and particles.

At the sixth Solvay Conference in 1930, Einstein proposed the "photon box" thought experiment to refute the energy–time uncertainty relation. A box is filled with radiation, and a shutter in its wall, controlled by a clock inside the box, opens for a very short time at a precise moment to release one photon. Weighing the box before and after the release gives, through the **mass–energy relation** $E=mc^2$, the energy of the photon exactly, so that $\Delta E$ and $\Delta t$ seem to be simultaneously arbitrarily small. After a sleepless night Bohr replied: weighing the box requires measuring its position in a gravitational field, and the uncertainty in position makes the momentum of the box uncertain; moreover, according to general relativity the rate of a clock in a gravitational field depends on its height, so the uncertainty in position introduces an uncertainty in the clock reading, and together the two give exactly $\Delta E\,\Delta t\gtrsim h$. Einstein never again questioned the internal consistency of the uncertainty relation, but always maintained that quantum mechanics is not the final theory.

In 1935 Einstein, Podolsky and Rosen argued, with a thought experiment on two entangled particles (the EPR paradox), that quantum mechanics is incomplete. In 1964 Bell proved that any local hidden-variable theory must obey an inequality (Bell's inequality), whereas quantum mechanics predicts that it is violated in some situations, turning the philosophical dispute into a testable question. From Clauser (1972) and Aspect (1982) to the experiments of 2015 that closed the main loopholes, the results all violate Bell's inequality and agree with quantum mechanics; Aspect, Clauser and Zeilinger received the 2022 Nobel Prize in Physics for this work. Different views of the interpretation of quantum mechanics remain today, but they all make the same predictions for every observable result, and so far no experiment contradicts the predictions of quantum mechanics.

## Summary

| Topic | Main results |
|---|---|
| Hydrogen atom | $E_n=-13.6\,\mathrm{eV}/n^2$; $L=\sqrt{l(l+1)}\hbar$, $l\le n-1$; $L_z=m_l\hbar$, $\lvert m_l\rvert\le l$; degeneracy of a level $n^2$ ($2n^2$ with spin) |
| Electron spin | $s=\frac12$, $S=\frac{\sqrt3}2\hbar$, $S_z=\pm\frac12\hbar$; $\mu_{\mathrm{B}}=e\hbar/(2m_{\mathrm{e}})$ |
| Spin–orbit coupling | $\boldsymbol{J}=\boldsymbol{L}+\boldsymbol{S}$, $j=l\pm\frac12$; term symbol $n\,{}^{2s+1}L_j$; fine structure |
| Identical particles | fermions (half-integer spin): antisymmetric wave function, Pauli exclusion principle and Fermi–Dirac distribution; bosons (integer spin): symmetric wave function, Bose–Einstein distribution |
| Electron configuration | four quantum numbers $(n,l,m_l,m_s)$; a subshell holds $2(2l+1)$ and a shell $2n^2$ electrons; aufbau principle and Hund's rule |

## Questions

1. Why does a beam of ground-state silver atoms ($l=0$) split into two beams, rather than one or three, in the Stern–Gerlach experiment?
   Hint: the splitting comes from the spin of the 5s valence electron, with the two orientations $m_s=\pm\frac12$; the number of components due to orbital angular momentum, $2l+1$, is always odd.
2. How are the electrons of a copper atom ($Z=29$) arranged?
   Hint: $[\ce{Ar}]\,3\mathrm{d}^{10}\,4\mathrm{s}^1$; a filled 3d subshell is more stable than $3\mathrm{d}^9\,4\mathrm{s}^2$.
3. How many states (including spin) does the level of principal quantum number $n$ have in the hydrogen atom? Do these states still have the same energy in alkali-metal atoms?
   Hint: $2n^2$. In the alkali metals levels of different $l$ are separated by orbital penetration and core polarization, and levels with $l\ge1$ are further split into two according to $j$ by spin–orbit coupling.
4. Why can air molecules at room temperature be treated with classical statistics, whereas the electrons in a metal cannot?
   Hint: compare $n\lambda_{\mathrm{th}}^3$; electrons have small mass and hence a large thermal wavelength, and the electron density in a metal is high, so $n\lambda_{\mathrm{th}}^3\gg1$.
