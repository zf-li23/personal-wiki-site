---
title: Electrons in Solids
description: Classification of solids; the free electron gas model of metals (three-dimensional potential well, Fermi energy, Fermi velocity and Fermi temperature, density of states); formation of energy bands, periodic potentials and Bloch's theorem, the tight-binding model (an eigenvalue problem for a tridiagonal matrix) and the Kronig–Penney model; filled, valence and conduction bands and the band gap, conductors, semiconductors and insulators; intrinsic semiconductors and holes, n-type and p-type semiconductors; band bending and the current–voltage characteristic of the p–n junction; light-emitting diodes, semiconductor lasers, photovoltaic cells, transistors and the measurement of energy bands.
source_hash: 931bacd8360c
---

The previous chapters studied single particles and the electrons in a single atom. A solid contains of order $10^{23}$ atoms, with interactions among the electrons and between the electrons and the nuclei, and an exact solution is impossible. In this chapter we use two complementary simplified models to understand electrons in solids. The first treats the valence electrons of a metal as an ideal Fermi gas confined in a potential well (§6.1); it uses the **infinite square well** of [5.5.3](/5.5.3) and the **Fermi–Dirac distribution** of [5.5.4](/5.5.4#sec-4.3.3). The second takes into account the periodic potential of the lattice, so that the energy levels of isolated atoms broaden into energy bands (§6.2); the core here is Bloch's theorem, and the tight-binding model turns it into an **eigenvalue** problem for a tridiagonal matrix in linear algebra ([2.1.6](/2.1.6)). Band theory explains the enormous differences in conductivity among conductors, semiconductors and insulators (§6.3) and also the difficulties of the classical theory of **electrical conductance** in [5.3.5](/5.3.5). Sections 6.4–6.6 treat semiconductors, the p–n junction and semiconductor devices, which are the physical basis of digital circuits ([4.9.3](/4.9.3)) and of modern information technology; light-emitting diodes and semiconductor lasers connect with the lasers of the previous chapter ([5.5.5](/5.5.5#sec-5.2)).

## 6.1. Introduction to Solid-State Physics and the Free Electron Gas

### 6.1.1. States of Matter and Classification of Solids

Matter usually exists in three states: solid, liquid and gas. A gas that has been ionized forms an overall electrically neutral collection of ions, electrons and neutral particles called a plasma; a flame contains a partially ionized plasma. The boundaries between states are not always obvious: pitch looks like a solid but is in fact a liquid of extremely high **viscosity**; in the famous "pitch drop experiment" the pitch in the funnel drips about once every ten years.

**Definition 6.1.1** A solid in which atoms (or molecules, or ions) are arranged periodically in space with long-range order is called a **crystal**, such as table salt, metals and silicon; a solid whose atomic arrangement has only short-range order and no long-range periodicity is called an **amorphous solid**, such as glass and rosin. A solid whose atomic arrangement has long-range order but no translational periodicity is called a **quasicrystal**; it can have the fivefold rotational symmetry forbidden to crystals.

Quasicrystals were discovered by Shechtman in 1982 in an aluminum–manganese alloy, for which he received the 2011 Nobel Prize in Chemistry. The periodic structure of a crystal can be determined by **X-ray** diffraction ([5.4.2](/5.4.2#sec-2.5)). Solid-state physics studies how the atoms and electrons in a solid and their interactions determine its physical and chemical properties. Structure affects properties: although both consist of carbon atoms, diamond is a transparent, extremely hard insulator, whereas graphite is an opaque, soft conductor. In this chapter we discuss only electrons in crystals.

### 6.1.2. The Free Electron Gas Model

When metal atoms combine into a crystal, the valence electrons no longer belong to a particular atom but move throughout the crystal, becoming electrons shared by all the atoms, while the remaining ion cores form a periodic lattice.

**Definition 6.1.2 (Free Electron Gas)** The model in which the interaction among the valence electrons and the periodic potential of the ion cores are neglected, and the valence electrons of a metal are regarded as an ideal gas moving freely in a box and obeying the Pauli exclusion principle, is called the **free electron gas** model (the Sommerfeld model); the valence electrons in it are called free electrons.

Why can such a crude model be used? The Coulomb repulsion between electrons is screened by the other electrons and greatly weakened; more importantly, Bloch's theorem in §6.2 shows that a strictly periodic lattice does not scatter electrons, and an electron in a perfect lattice propagates like a free particle, only with a modified relation between energy and momentum. At ordinary temperatures electrons in a metal can hardly escape from the surface (this requires a **work function** $W_0$ of several electron volts), so they can be taken approximately to be in a three-dimensional **infinite square well**.

Let the metal be a cube of side $L$. By **separation of variables** ([2.5.4](/2.5.4)), the **time-independent Schrödinger equation** of the three-dimensional infinite well reduces to three one-dimensional problems, each direction being the one-dimensional well of [5.5.3](/5.5.3#sec-3.2); the **eigenfunctions** are products of **standing waves** in the three directions:

$$
\psi=\Big(\frac2L\Big)^{3/2}\sin\frac{n_x\pi x}{L}\sin\frac{n_y\pi y}{L}\sin\frac{n_z\pi z}{L},\qquad n_x,n_y,n_z=1,2,3,\dots
$$
The corresponding momentum components and energy are

$$
p_x=\frac{\pi\hbar}{L}n_x,\quad p_y=\frac{\pi\hbar}{L}n_y,\quad p_z=\frac{\pi\hbar}{L}n_z,\qquad E=\frac{p^2}{2m_{\mathrm{e}}}=\frac{\pi^2\hbar^2}{2m_{\mathrm{e}}L^2}\big(n_x^2+n_y^2+n_z^2\big).
$$
Different $(n_x,n_y,n_z)$ can give the same energy, so the levels exhibit **degeneracy**.

Set up a "quantum-number space" with $n_x,n_y,n_z$ as coordinate axes; each integer coordinate point in the first octant represents one spatial state, and each point occupies unit volume on average. States of energy $E$ lie on the sphere of radius

$$
R=\sqrt{n_x^2+n_y^2+n_z^2}=\frac{L\sqrt{2m_{\mathrm{e}}E}}{\pi\hbar}.
$$
For large $N$, the number of states with energy below $E$ is the volume of one eighth of the sphere, multiplied by 2 for the two orientations of **electron spin**:

$$
N_{\mathrm{s}}(E)=2\times\frac18\times\frac43\pi R^3=\frac{L^3}{3\pi^2}\Big(\frac{2m_{\mathrm{e}}E}{\hbar^2}\Big)^{3/2}.
$$
It is proportional to the volume $L^3$ and independent of the shape of the well; replacing the infinite well by periodic boundary conditions gives the same result. The number of states per unit volume with energy below $E$ is

$$
n_{\mathrm{s}}(E)=\frac{N_{\mathrm{s}}}{L^3}=\frac{1}{3\pi^2}\Big(\frac{2m_{\mathrm{e}}E}{\hbar^2}\Big)^{3/2}.
\tag{6.1}
$$

### 6.1.3. The Fermi Energy

At $T=0$, electrons fill the states one by one from the lowest, according to the **Pauli exclusion principle** and the **aufbau principle**, one electron per state, until all electrons are placed.

**Definition 6.1.3 (Fermi Energy)** The highest energy level occupied by electrons in a metal at $T=0$ is called the Fermi level, and its energy is called the **Fermi energy**, denoted $E_{\mathrm{F}}$. Let the number density of free electrons be $n$; setting $n_{\mathrm{s}}(E_{\mathrm{F}})=n$ in Eq. (6.1) gives

$$
E_{\mathrm{F}}=\frac{\hbar^2}{2m_{\mathrm{e}}}\big(3\pi^2n\big)^{2/3}.
\tag{6.2}
$$
Correspondingly one defines the **Fermi velocity** $v_{\mathrm{F}}=\sqrt{2E_{\mathrm{F}}/m_{\mathrm{e}}}$ and the **Fermi temperature** $T_{\mathrm{F}}=E_{\mathrm{F}}/k_{\mathrm{B}}$.

The Fermi energy depends only on the number density of free electrons. $E_{\mathrm{F}}$ is just the chemical potential $\mu(0)$ at $T=0$ in the **Fermi–Dirac distribution** (Theorem 4.3.2). In quantum-number space (or momentum space) the states occupied at $T=0$ form a sphere, called the Fermi sphere, whose radius corresponds to the Fermi wave number $k_{\mathrm{F}}=(3\pi^2n)^{1/3}$.

**Example 6.1.1 (Fermi Energy of Copper)** Each copper atom contributes one valence electron, and $n=8.47\times10^{28}\,\mathrm{m^{-3}}$. From Eq. (6.2),

$$
k_{\mathrm{F}}=1.36\times10^{10}\,\mathrm{m^{-1}},\qquad E_{\mathrm{F}}=7.0\,\mathrm{eV},\qquad v_{\mathrm{F}}=1.57\times10^6\,\mathrm{m\,s^{-1}},\qquad T_{\mathrm{F}}=8.2\times10^4\,\mathrm{K}.
$$
For common metals $E_{\mathrm{F}}$ lies between $2$ and $12\,\mathrm{eV}$ (sodium $3.2\,\mathrm{eV}$, aluminum $11.7\,\mathrm{eV}$), $v_{\mathrm{F}}$ is about $10^6\,\mathrm{m\,s^{-1}}$ and $T_{\mathrm{F}}$ is as high as several tens of thousands of kelvin. Even at $T=0$ the electrons in a metal move at about one percent of the speed of light, with mean kinetic energy $\frac35E_{\mathrm{F}}$ (about $4.2\,\mathrm{eV}$ for copper), far greater than the thermal energy $\frac32k_{\mathrm{B}}T\approx0.04\,\mathrm{eV}$ at room temperature. This is a consequence of the Pauli exclusion principle and is completely different from the classical picture.

**Remark 6.1.1** Eq. (6.2) is often miswritten as $E_{\mathrm{F}}=(3\pi^2)^{2/3}\frac{\hbar^2}{2m_{\mathrm{e}}}n^{3/2}$, which has the wrong exponent: from Eq. (6.1), $E_{\mathrm{F}}\propto n^{2/3}$. A dimensional check also reveals this: only $\hbar^2n^{2/3}/m_{\mathrm{e}}$ has the dimension of energy.

### 6.1.4. Density of States and Finite Temperature

**Definition 6.1.4 (Density of States)** The number of quantum states per unit volume per unit energy interval, $g(E)=\dfrac{\mathrm{d}n_{\mathrm{s}}}{\mathrm{d}E}$, is called the **density of states**. From Eq. (6.1), the density of states of the free electron gas is

$$
g(E)=\frac{1}{2\pi^2}\Big(\frac{2m_{\mathrm{e}}}{\hbar^2}\Big)^{3/2}\sqrt E.
\tag{6.3}
$$

At temperature $T$ the mean number of electrons in each state is given by the Fermi–Dirac distribution (Eq. (4.5)); the number of electrons per unit volume with energy between $E$ and $E+\mathrm{d}E$ is $g(E)\bar N(E)\,\mathrm{d}E$, and the electron number density is

$$
n=\int_0^\infty\frac{g(E)\,\mathrm{d}E}{\mathrm{e}^{(E-\mu)/(k_{\mathrm{B}}T)}+1}.
$$
In a metal $k_{\mathrm{B}}T\ll E_{\mathrm{F}}$ (at room temperature $T/T_{\mathrm{F}}\sim10^{-2}$ or less), $\mu\approx E_{\mathrm{F}}$, and the distribution differs little from that at $T=0$: only electrons within a range of a few $k_{\mathrm{B}}T$ around $E_{\mathrm{F}}$ can be thermally excited above $E_{\mathrm{F}}$, while for electrons deeper down all the states above them are already filled, so they cannot absorb energy of order $k_{\mathrm{B}}T$ (figure below).

![Density of states of the free electron gas, g(E) ∝ √E (black line). At T = 0 all states below E_F are occupied (shaded); at finite temperature (for clarity k_BT = 0.06 E_F is used; for a metal at room temperature it is about 0.004 E_F) the occupation changes only within a range of about k_BT around E_F (red line)](./plots/free-electron-dos.py)

This immediately resolves a puzzle of the classical electron theory. By the classical **equipartition theorem** ([5.2.1](/5.2.1)) each free electron should contribute a heat capacity of $\frac32k_{\mathrm{B}}$, so the **molar heat capacity** of a metal should exceed that of an insulator by $\frac32R$, yet experimentally the heat capacities of metals and insulators are almost equal. In the quantum theory only a fraction of about $T/T_{\mathrm{F}}$ of the electrons can be thermally excited, and the heat capacity per electron is $\frac{\pi^2}{2}\frac{T}{T_{\mathrm{F}}}k_{\mathrm{B}}$, only about one percent of the classical value at room temperature; the electronic heat capacity is proportional to $T$ and can be measured at low temperatures. Likewise, only the electrons near the Fermi surface take part in conduction, and they move at the Fermi velocity, so in the **Drude model** of [5.3.5](/5.3.5) the **mean free path** should be computed with $v_{\mathrm{F}}$ rather than with the classical thermal speed.

## 6.2. Energy Bands in Solids

### 6.2.1. From Atomic Levels to Energy Bands

When two identical atoms are far apart, each has the same set of levels. As they approach each other their **wave functions** overlap, and each originally twofold degenerate level splits into two (the bonding and antibonding levels in a molecule, completely analogous to the two **normal modes** of the two coupled pendulums in [5.1.6](/5.1.6)). When $N$ atoms form a solid, the $N$-fold degeneracy of each atomic level is lifted by the interaction and splits into $N$ closely spaced levels.

**Definition 6.2.1 (Energy Band)** When $N$ atoms form a solid, the $N$ extremely closely spaced, approximately continuously distributed levels into which one level of the isolated atom splits are called an **energy band**.

The width $\Delta E$ of a band is determined by the overlap of the wave functions of neighboring atoms and is independent of $N$, typically a few electron volts; for $N\sim10^{23}$ the spacing between adjacent levels within a band is about $\Delta E/N$, small enough to be regarded as continuous. The general rules are:

- the more outer the electrons, the more their wave functions overlap and the wider the band; the bands of inner electrons are very narrow, almost the original atomic levels;
- the smaller the interatomic distance, the wider the band;
- bands may have gaps between them, or may overlap each other.

### 6.2.2. Periodic Potentials and Bloch's Theorem

Electrons in a solid move in the potential produced jointly by the ion cores and the other electrons. In the one-electron approximation each electron feels a potential energy $U(\boldsymbol{r})$ with the periodicity of the lattice. Take one dimension as an example, with lattice constant $a$ and $U(x+a)=U(x)$.

**Theorem 6.2.1 (Bloch's Theorem)** If the potential energy has the lattice periodicity $U(x+a)=U(x)$, the eigenfunctions of the time-independent Schrödinger equation can be taken in the form

$$
\psi_k(x)=\mathrm{e}^{\mathrm{i}kx}u_k(x),\qquad u_k(x+a)=u_k(x),
\tag{6.4}
$$
that is, a plane wave multiplied by a function with the same period as the lattice; equivalently, $\psi_k(x+a)=\mathrm{e}^{\mathrm{i}ka}\psi_k(x)$. In three dimensions, for all lattice translation vectors $\boldsymbol{R}$, $\psi_{\boldsymbol{k}}(\boldsymbol{r})=\mathrm{e}^{\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}u_{\boldsymbol{k}}(\boldsymbol{r})$ with $u_{\boldsymbol{k}}(\boldsymbol{r}+\boldsymbol{R})=u_{\boldsymbol{k}}(\boldsymbol{r})$. Wave functions satisfying Eq. (6.4) are called Bloch waves.

**Proof** Define the translation operator $\hat T\psi(x)=\psi(x+a)$. The kinetic energy operator is invariant under translation and $U$ is periodic, so $\hat T$ commutes with the **Hamiltonian** $\hat H$: $\hat T\hat H\psi=\hat H\hat T\psi$. Just as commuting diagonalizable matrices in finite dimensions admit **simultaneous diagonalization** ([Theorem 6.11.1](/2.1.6#thm-6.11.1)), we may choose the eigenfunctions of $\hat H$ to be eigenfunctions of $\hat T$ as well: $\hat T\psi=\lambda\psi$. Let the crystal consist of $N$ unit cells and impose periodic boundary conditions (the Born–von Kármán condition) $\psi(x+Na)=\psi(x)$; then $\lambda^N=1$, $\lambda=\mathrm{e}^{\mathrm{i}ka}$, and $k=\frac{2\pi}{Na}j$ ($j$ an integer). Setting $u_k(x)=\mathrm{e}^{-\mathrm{i}kx}\psi(x)$, we get $u_k(x+a)=\mathrm{e}^{-\mathrm{i}k(x+a)}\mathrm{e}^{\mathrm{i}ka}\psi(x)=u_k(x)$. $\square$

Bloch's theorem has several immediate consequences:

- $\lvert\psi_k\rvert^2=\lvert u_k\rvert^2$ is a periodic function: the electron has the same probability of being found in every unit cell and no longer belongs to a particular atom. This is the delocalization (sharing) of electrons.
- $k$ and $k+2\pi/a$ give the same $\lambda$, so $k$ can be restricted to $-\pi/a<k\le\pi/a$; this interval is called the first *Brillouin zone* and contains exactly $N$ allowed values of $k$. For each $k$ the equation has a sequence of **eigenvalues** $E_1(k)<E_2(k)<\cdots$, and each $E_n(k)$, varying quasi-continuously with $k$, is an energy band, with $n$ the band index. Each band has $N$ states of $k$, or $2N$ states including spin.
- Bloch waves are stationary states: a perfect periodic lattice does not scatter electrons. The **electrical resistance** of a metal comes from departures from strict periodicity: lattice vibrations (whose strength increases with temperature, so the **electrical resistivity** of a metal rises with temperature), impurities and defects. This answers the question of the mean free path that the classical model of [5.3.5](/5.3.5) could not explain.
- The velocity of an electron in a band is the **group velocity** of the wave packet, $v=\frac1\hbar\frac{\mathrm{d}E}{\mathrm{d}k}$ ([5.1.7](/5.1.7)); under an external force $F$, $\hbar\frac{\mathrm{d}k}{\mathrm{d}t}=F$. Near the bottom of a band $E\approx E_0+\frac{\hbar^2k^2}{2m^*}$ and the electron behaves like a free particle of mass $m^*=\hbar^2/(\mathrm{d}^2E/\mathrm{d}k^2)$; $m^*$ is called the *effective mass* and contains the entire effect of the periodic potential.

**Example 6.2.1 (Kronig–Penney Model)** Take the simplest periodic potential: a row of $\delta$-function **potential barriers** with spacing $a$, $U(x)=\alpha\sum_j\delta(x-ja)$ ($\alpha>0$). Between two barriers the electron is free, $\psi$ is a combination of $\mathrm{e}^{\pm\mathrm{i}qx}$, and $E=\frac{\hbar^2q^2}{2m}$; at a barrier $\psi$ is continuous and $\psi'$ jumps by $\frac{2m\alpha}{\hbar^2}\psi$. Adding the Bloch condition $\psi(x+a)=\mathrm{e}^{\mathrm{i}ka}\psi(x)$, one finds

$$
\cos ka=\cos qa+P\,\frac{\sin qa}{qa},\qquad P=\frac{m\alpha a}{\hbar^2}.
$$
The absolute value of the left side does not exceed 1, so only energies for which the right side falls in $[-1,1]$ are allowed: the allowed energies form bands, with forbidden gaps between them (left of the figure below). The gaps occur at $k=n\pi/a$, that is, $2a=n\lambda$: this is exactly the condition for Bragg reflection of the electron wave by the lattice ([5.4.2](/5.4.2#sec-2.5.3)), where the forward and backward propagating waves superpose to form a standing wave. For $P\to0$ the gaps vanish and we return to the free-electron $E\propto k^2$; for $P\to\infty$ the bands shrink to the levels of isolated wells.

![Kronig–Penney model (P = 3). Left: the right side of the equation as a function of qa; the intervals where its absolute value does not exceed 1 (shaded) give the allowed bands. Right: the energy bands E(k) in the extended-zone scheme (blue) and the free-electron parabola (dashed), interrupted at k = nπ/a; the gray strips are the gaps](./plots/kronig-penney.py)

### 6.2.3. The Tight-Binding Model

Energy bands can also be obtained starting from isolated atoms; this approach is called the *tight-binding model*, and in it Bloch's theorem becomes a concrete computation in linear algebra. Consider a one-dimensional chain of atoms, with the $j$th atom at $x_j=ja$, each atom providing one **atomic orbital** $\phi(x-x_j)$ of energy $\varepsilon_0$. Write the state of the electron as a linear combination of atomic orbitals,

$$
\psi=\sum_jc_j\,\phi(x-x_j),
$$
and consider only the overlap between neighboring atoms: the matrix element for the electron to "hop" from one atom to the next is $-t$ ($t>0$, called the hopping integral). In this basis the matrix of $\hat H$ is a real symmetric tridiagonal matrix, and the time-independent Schrödinger equation becomes a matrix eigenvalue problem:

$$
\begin{bmatrix}
\varepsilon_0 & -t & & \\
-t & \varepsilon_0 & -t & \\
 & \ddots & \ddots & \ddots \\
 & & -t & \varepsilon_0
\end{bmatrix}
\begin{bmatrix} c_1\\ c_2\\ \vdots\\ c_N\end{bmatrix}
=E\begin{bmatrix} c_1\\ c_2\\ \vdots\\ c_N\end{bmatrix}.
$$
The eigenvalues of a real symmetric matrix are real and the eigenvectors can be chosen orthogonal ([2.1.7](/2.1.7#thm-7.1.1)), which corresponds to the energy eigenvalues being real and distinct eigenstates being orthogonal. The eigenvalues of this matrix can be found exactly:

- For an open chain of $N$ atoms: $E_m=\varepsilon_0-2t\cos\frac{m\pi}{N+1}$, $m=1,2,\dots,N$. For $N=1$ there is only the atomic level $\varepsilon_0$; for $N=2$ it splits into $\varepsilon_0\mp t$ (bonding and antibonding); as $N$ increases the $N$ levels gradually fill the interval $[\varepsilon_0-2t,\ \varepsilon_0+2t]$ (left of the figure below).
- For a ring (periodic boundary conditions): the lower-left and upper-right corners of the matrix are also $-t$, and it becomes a circulant matrix whose eigenvectors are the discrete Fourier modes $c_j=\mathrm{e}^{\mathrm{i}kja}/\sqrt N$. Substituting into the equation, $E c_j=\varepsilon_0c_j-t(c_{j+1}+c_{j-1})$, gives the band

$$
E(k)=\varepsilon_0-2t\cos ka,\qquad k=\frac{2\pi}{Na}j,\quad -\frac\pi a<k\le\frac\pi a.
\tag{6.5}
$$
Since $c_j$ is proportional to $\mathrm{e}^{\mathrm{i}kx_j}$, this is precisely the discrete form of Bloch's theorem.

![Tight-binding model. Left: eigenvalues of the tridiagonal matrix of an open atomic chain; as the number of atoms N increases, the N levels fill a band of width 4t. Right: each of two atomic levels broadens into a band E(k) = ε₀ − 2t cos ka (dots are the allowed k on a ring of N = 20); a gap remains between the two bands](./plots/tight-binding.py)

The bandwidth $4t$ is determined by the hopping integral, that is, by the overlap of the wave functions of neighboring atoms; this is the reason for the statement in §6.2.1 that bands are wide for outer electrons and small interatomic distances. Near the band bottom $E\approx\varepsilon_0-2t+ta^2k^2$, and the effective mass is $m^*=\hbar^2/(2ta^2)$: the narrower the band, the "heavier" the electron. Two atomic levels each broaden into a band, and if their separation exceeds the sum of the two half-widths, a gap remains between them. The formula for the open chain can be checked directly with the tridiagonal eigenvalue solver of SciPy ([4.4.3](/4.4.3#sec-3.2.3), [4.4.4](/4.4.4)), the same tool used for the numerical solution of the **Schrödinger equation** in [5.5.3](/5.5.3#sec-3.4.4):

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal

N, eps0, t = 6, 0.0, 1.0
E = eigh_tridiagonal(np.full(N, eps0), np.full(N - 1, -t), eigvals_only=True)
exact = eps0 - 2 * t * np.cos(np.arange(1, N + 1) * np.pi / (N + 1))
print(np.allclose(E, exact))  # True
```

### 6.2.4. Occupation of Electrons in Bands

Electrons fill the bands level by level from the lowest, according to the Pauli exclusion principle and the aufbau principle. Each band has $2N$ states (if the atomic level itself is $g$-fold degenerate, as for a p level with $g=3$, there are $2gN$ states; for example a p band has $6N$ states).

**Definition 6.2.2** According to how they are filled with electrons, bands are classified as:

- **filled band**: a band all of whose levels are filled with electrons;
- partially filled band: a band in which only some levels are occupied;
- **empty band**: a band containing no electrons;
- **valence band**: the band formed by broadening of the levels of the valence electrons, that is, the highest band occupied by electrons at $T=0$ (for semiconductors and insulators the valence band is a filled band);
- **conduction band**: the adjacent band above the valence band, which at $T=0$ contains no electrons (or is partially filled);
- **band gap**: an energy interval between bands in which no electron states exist. The energy difference between the bottom of the conduction band and the top of the valence band is called the energy gap, denoted $E_{\mathrm{g}}$.

Some examples:

- Sodium: each atom has one 3s valence electron, so the $N$ electrons fill only half of the $2N$ states of the 3s band; the band is partially filled, and sodium is a metal.
- Magnesium: each atom has two 3s electrons, which fill the 3s band exactly, but it overlaps the 3p band above, and together they form a partially filled band, so magnesium is also a metal.
- Diamond, silicon, germanium: the four valence electrons of each atom form $\mathrm{sp}^3$-hybridized covalent bonds; the $4N$ bonding states form the valence band and the $4N$ antibonding states form the conduction band, the $4N$ valence electrons fill the valence band exactly, the conduction band is empty, and an energy gap lies between them.

## 6.3. Band-Theory Explanation of Conductivity

### 6.3.1. A Filled Band Does Not Conduct

The resistivities of solids differ enormously: about $10^{-8}\,\Omega\,\mathrm{m}$ for metals, about $10^{-4}$–$10^{7}\,\Omega\,\mathrm{m}$ for semiconductors and above $10^{8}\,\Omega\,\mathrm{m}$ for insulators, spanning more than twenty orders of magnitude. The difference comes from the band structure.

The classical explanation is that electrons gain energy from the electric field and undergo a collective directed motion. The band-theory explanation is that the current comes from an asymmetry in the distribution of electrons in a band. Since $E(k)=E(-k)$, the electron velocities $v=\frac1\hbar\frac{\mathrm{d}E}{\mathrm{d}k}$ in the states $k$ and $-k$ are equal in magnitude and opposite in direction.

- Filled band: all states are occupied, and for every $k$ there is a corresponding $-k$, so the currents cancel. An applied electric field changes the $k$ of every electron at the same rate, but since all states in a filled band are occupied, the electrons can only "exchange" places within the band, the distribution remains symmetric, and a filled band does not conduct.
- Partially filled band: the electric field shifts the distribution of electrons to one side, the contributions of the electrons in the band to the current no longer cancel, and a current flows. The levels in the band are approximately continuous, so a very weak field can cause such intraband transitions.

Hence a solid with a partially filled band conducts; a solid with only filled and empty bands can conduct only when electrons make transitions from the filled band to the empty band, making both bands partially filled.

### 6.3.2. Conductors, Semiconductors and Insulators

**Definition 6.3.1** According to the band structure at $T=0$, solids fall into three classes: a conductor has a partially filled band (or overlapping filled and empty bands); a solid whose valence band is filled and whose energy gap is small (about $0.1$–$2\,\mathrm{eV}$, and above $3\,\mathrm{eV}$ for wide-gap materials) is called a **semiconductor**; a solid whose valence band is filled and whose energy gap is large (several electron volts or more) is called an **insulator**.

| Material | $E_{\mathrm{g}}/\mathrm{eV}$ ($300\,\mathrm{K}$) | Type |
|---|---|---|
| Germanium $\ce{Ge}$ | $0.66$ | semiconductor |
| Silicon $\ce{Si}$ | $1.12$ | semiconductor |
| Gallium arsenide $\ce{GaAs}$ | $1.42$ | semiconductor |
| Gallium nitride $\ce{GaN}$ | $3.4$ | wide-gap semiconductor |
| Diamond $\mathrm{C}$ | $5.5$ | insulator |
| Silicon dioxide $\ce{SiO2}$ | about $9$ | insulator |

The difference between semiconductors and insulators lies only in the size of the energy gap, and there is no sharp boundary. At room temperature $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$, and the probability that an electron is thermally excited across the gap varies as the **Boltzmann factor** $\mathrm{e}^{-E_{\mathrm{g}}/(2k_{\mathrm{B}}T)}$: for $E_{\mathrm{g}}=1\,\mathrm{eV}$ it is about $10^{-9}$, which multiplied by an effective number of states of order $10^{25}$ per cubic meter already produces appreciable numbers of carriers; for $E_{\mathrm{g}}=5\,\mathrm{eV}$ it is almost zero. Electric fields of ordinary strength are also far from sufficient to drive electrons across the large gap of an insulator.

This explains the temperature dependence of resistivity: the number of carriers in a metal does not change with temperature, and as the temperature rises, lattice vibrations strengthen, scattering increases and the resistivity rises; the number of carriers in a semiconductor increases exponentially with temperature, an effect that far outweighs the increase of scattering, so the resistivity falls rapidly as the temperature rises (thermistors exploit this).

## 6.4. Semiconductors

### 6.4.1. Intrinsic Semiconductors and Holes

**Definition 6.4.1** A pure semiconductor without impurities or defects is called an **intrinsic semiconductor**. Under thermal excitation, illumination or an electric field, electrons in the valence band make transitions to the conduction band, and the vacancies left in the valence band are called **holes**.

Both the electrons in the conduction band and the holes in the valence band take part in conduction. When there is one vacancy in the valence band, the motion of the remaining electrons in an electric field can be regarded equivalently as motion of this vacancy in the opposite direction: a hole behaves like a particle with positive charge $+e$ and positive effective mass. In an intrinsic semiconductor electrons and holes are always created in pairs; these are called intrinsic carriers, and their number densities are equal, $n=p=n_{\mathrm{i}}$. For silicon at room temperature $n_{\mathrm{i}}\approx1\times10^{16}\,\mathrm{m^{-3}}$, whereas the number density of silicon atoms is $5\times10^{28}\,\mathrm{m^{-3}}$. $n_{\mathrm{i}}$ increases rapidly with temperature as $T^{3/2}\mathrm{e}^{-E_{\mathrm{g}}/(2k_{\mathrm{B}}T)}$. Thus semiconductors have two conduction mechanisms: electron conduction and hole conduction.

**Example 6.4.1 (Intrinsic Photoconductivity)** When the **photon** energy satisfies $h\nu>E_{\mathrm{g}}$, an electron in the valence band absorbs the photon and makes a transition to the conduction band, producing an electron–hole pair, and the **electrical conductivity** of the semiconductor increases; this is called intrinsic photoconductivity. The energy gap of cadmium sulfide ($\ce{CdS}$) is $2.42\,\mathrm{eV}$, and the longest wavelength that can produce intrinsic photoconductivity is

$$
\lambda_{\max}=\frac{hc}{E_{\mathrm{g}}}=\frac{1240\,\mathrm{eV\,nm}}{2.42\,\mathrm{eV}}=512\,\mathrm{nm}.
$$
Light of longer wavelength cannot make it conduct. $\ce{CdS}$ photoresistors are commonly used in light-controlled switches.

### 6.4.2. Doped Semiconductors

Doping an intrinsic semiconductor with a small amount of impurity changes its conductivity enormously, which is the basis of semiconductor technology.

**Definition 6.4.2** When a small amount of a pentavalent element ($\ce{P}$, $\ce{As}$, etc.) is added to a tetravalent intrinsic semiconductor ($\ce{Si}$, $\ce{Ge}$), the impurity atom has one electron left over after forming covalent bonds with its four neighbors, and this electron is easily ionized into the conduction band. Such an impurity that supplies electrons is called a **donor**, and a semiconductor doped with donors, in which electron conduction predominates, is called an **n-type semiconductor**. The level of the donor lies in the band gap, just below the bottom of the conduction band, and is called the donor level.

The distance $E_{\mathrm{d}}$ between the donor level and the bottom of the conduction band is only about $0.01$–$0.05\,\mathrm{eV}$ ($0.045\,\mathrm{eV}$ for phosphorus in silicon). This can be estimated with the hydrogen-atom model: the extra electron and the impurity ion of charge $+e$ form a "hydrogen-like atom", but it sits in silicon with **relative permittivity** $\varepsilon_{\mathrm{r}}\approx11.7$ and effective mass $m^*\approx0.26m_{\mathrm{e}}$, so the ionization energy is about $13.6\,\mathrm{eV}\times\frac{m^*/m_{\mathrm{e}}}{\varepsilon_{\mathrm{r}}^2}\approx0.026\,\mathrm{eV}$ and the orbital radius is about $\varepsilon_{\mathrm{r}}m_{\mathrm{e}}/m^*\approx45$ times the **Bohr radius** (about $2.4\,\mathrm{nm}$), spanning many lattice spacings (which also shows that treating silicon as a continuous medium is reasonable). At room temperature $k_{\mathrm{B}}T$ is comparable to $E_{\mathrm{d}}$, and almost all donors are ionized.

**Definition 6.4.3** When a small amount of a trivalent element ($\ce{B}$, $\ce{Ga}$, etc.) is added to an intrinsic semiconductor, the impurity atom lacks one electron when bonding with its neighbors and easily captures an electron from the valence band, leaving a hole there. Such an impurity that accepts electrons is called an **acceptor**, and a semiconductor doped with acceptors, in which hole conduction predominates, is called a **p-type semiconductor**. The level of the acceptor lies in the band gap, just above the top of the valence band (at a distance $E_{\mathrm{a}}<0.1\,\mathrm{eV}$), and is called the acceptor level.

Impurities have a very large effect on carrier concentrations. Suppose silicon is doped with donors at a concentration $N_{\mathrm{D}}=10^{24}\,\mathrm{m^{-3}}$ (roughly one phosphorus atom per $5\times10^4$ silicon atoms); at room temperature all donors are ionized, the electron concentration is $n\approx N_{\mathrm{D}}$, which is $10^8$ times the intrinsic concentration. In thermal equilibrium the product of electron and hole concentrations depends only on temperature and the material:

**Formula 6.4.1 (Law of Mass Action)** For a nondegenerate semiconductor in thermal equilibrium,

$$
np=n_{\mathrm{i}}^2.
\tag{6.6}
$$

The hole concentration in the n-type silicon above is therefore $p=n_{\mathrm{i}}^2/n\approx10^{8}\,\mathrm{m^{-3}}$, even much smaller than the intrinsic value: the doped electrons recombine with holes and suppress the concentration of the minority species. In an n-type semiconductor electrons are the majority carriers and holes the minority carriers; in a p-type semiconductor $p\approx N_{\mathrm{A}}$ (the acceptor concentration) and holes are the majority carriers.

| Carrier concentration in silicon at room temperature/$\mathrm{m^{-3}}$ | Intrinsic | n-type ($N_{\mathrm{D}}=10^{24}$) | p-type ($N_{\mathrm{A}}=10^{24}$) |
|---|---|---|---|
| Conduction-band electrons $n$ | $10^{16}$ | $10^{24}$ | $10^{8}$ |
| Valence-band holes $p$ | $10^{16}$ | $10^{8}$ | $10^{24}$ |

### 6.4.3. Compound Semiconductors and Impurity Compensation

Compound semiconductors can also be doped. In the III–V compound $\ce{GaAs}$, adding hexavalent $\ce{Te}$, which replaces pentavalent $\ce{As}$, leaves an extra electron and produces a donor level, giving n-type material; adding divalent $\ce{Zn}$, which replaces trivalent $\ce{Ga}$, leaves one electron short and produces an acceptor level, giving p-type material.

Real semiconductors often contain both donors (concentration $N_{\mathrm{D}}$) and acceptors (concentration $N_{\mathrm{A}}$). The electrons of the donors first fill the acceptor levels, and the two kinds of impurity cancel each other, which is called impurity compensation: for $N_{\mathrm{D}}>N_{\mathrm{A}}$ the material is n-type, with effective donor concentration $N_{\mathrm{D}}-N_{\mathrm{A}}$; for $N_{\mathrm{D}}<N_{\mathrm{A}}$ it is p-type. Using compensation, one can dope part of an n-type semiconductor with a higher concentration of acceptors to turn it p-type, thereby making a p–n junction.

## 6.5. The p–n Junction

### 6.5.1. Formation of the p–n Junction

**Definition 6.5.1 (p–n Junction)** The transition region formed at the interface between a p-type region and an n-type region in the same piece of semiconductor is called a **p–n junction**. The space-charge region near the interface, in which carriers are almost depleted and only ionized impurities remain, is called the **depletion region**; the electric field produced there by the space charge, pointing from the n region to the p region, is called the **built-in electric field** $\boldsymbol{E}_{\mathrm{in}}$.

The p region has many holes and the n region many electrons. Near the interface the majority carriers diffuse toward the other side: electrons diffuse from the n region into the p region and holes from the p region into the n region, where they recombine with the majority carriers. Positively charged ionized donors are thus left on the n side and negatively charged ionized acceptors on the p side, forming the space-charge region and the built-in field. The built-in field prevents further diffusion of the majority carriers and at the same time drives minority carriers to drift in the opposite direction. When diffusion and drift balance, the thickness $d_0$ of the depletion region is about $0.1$–$1\,\mu\mathrm{m}$.

### 6.5.2. Band Bending

Corresponding to the built-in field, there is a **potential difference** $U_0$ across the p–n junction (the n region at the higher **electric potential**), called the built-in potential difference; the **electrostatic potential energy** of an electron in the p region is higher than in the n region by $eU_0$, forming a barrier that hinders electrons from passing from the n region into the p region. The energy bands of the electrons therefore bend with position: the conduction and valence bands of the p region as a whole lie higher than those of the n region by $eU_0$ (left of the figure below).

The magnitude of $U_0$ follows from the equilibrium condition. In equilibrium the ratio of electron concentrations in the n and p regions is determined by the **Boltzmann distribution**, $n_{\mathrm{n}}/n_{\mathrm{p}}=\mathrm{e}^{eU_0/(k_{\mathrm{B}}T)}$; with $n_{\mathrm{n}}\approx N_{\mathrm{D}}$ and $n_{\mathrm{p}}=n_{\mathrm{i}}^2/N_{\mathrm{A}}$, this gives

$$
eU_0=k_{\mathrm{B}}T\ln\frac{N_{\mathrm{A}}N_{\mathrm{D}}}{n_{\mathrm{i}}^2}.
$$
For silicon with $N_{\mathrm{A}}=N_{\mathrm{D}}=10^{23}\,\mathrm{m^{-3}}$, $U_0\approx0.83\,\mathrm{V}$. In the language of statistical physics, in equilibrium the chemical potential of the electrons (the Fermi level) is the same everywhere in the p–n junction, and the band bending is precisely what aligns the Fermi levels on the two sides.

![The p–n junction. Left: band bending in equilibrium; the Fermi level E_F (dashed) is horizontal throughout the junction, the bands of the p region lie eU₀ above those of the n region, and the gray region is the depletion region. Right: current–voltage characteristic of a silicon diode; the forward current increases exponentially with voltage, the reverse direction carries only a tiny saturation current, and breakdown occurs at large reverse voltage (the breakdown voltage is schematic)](./plots/pn-junction.py)

### 6.5.3. Current–Voltage Characteristic

- Forward bias (the p region connected to the positive terminal of the **source of electromotive force** and the n region to the negative terminal): the applied voltage $U$ cancels part of the built-in field, the barrier is lowered to $e(U_0-U)$ and the depletion region narrows. The numbers of electrons passing from the n region over the barrier into the p region, and of holes passing from the p region into the n region, increase as the **Boltzmann factor** $\mathrm{e}^{eU/(k_{\mathrm{B}}T)}$, forming a forward current that grows rapidly with voltage (of order $\mathrm{mA}$ and above).
- Reverse bias (the p region connected to the negative terminal and the n region to the positive terminal): the barrier is raised to $e(U_0+U)$, the depletion region widens, diffusion of the majority carriers is blocked, and only minority carriers drift under the junction field, forming a very small reverse saturation current $I_{\mathrm{s}}$ (of order $\mathrm{nA}$ or less for silicon and of order $\mu\mathrm{A}$ for germanium), which hardly varies with the reverse voltage.

**Formula 6.5.1 (Shockley Diode Equation)** The relation between current and applied voltage for an ideal p–n junction is

$$
I=I_{\mathrm{s}}\big(\mathrm{e}^{eU/(k_{\mathrm{B}}T)}-1\big).
\tag{6.7}
$$

At room temperature $k_{\mathrm{B}}T/e=25.9\,\mathrm{mV}$, and the current increases tenfold for every increase of about $60\,\mathrm{mV}$ in forward voltage, so a silicon diode carries a noticeable forward current at about $0.6$–$0.7\,\mathrm{V}$. The p–n junction conducts in one direction only and its current–voltage characteristic is nonlinear, so it can be used for rectification. When the reverse voltage exceeds a certain value, the strong electric field in the depletion region causes avalanche multiplication of carriers (or makes valence-band electrons tunnel directly into the conduction band), and the reverse current rises sharply; this is called breakdown, and Zener diodes operate in the breakdown region.

## 6.6. Semiconductor Devices

On 23 December 1947, Bardeen and Brattain at Bell Laboratories made the first transistor with amplifying action (the point-contact transistor), and Shockley subsequently proposed the junction transistor; the three shared the 1956 Nobel Prize in Physics. Semiconductor devices have since replaced vacuum tubes, and integrated circuits put hundreds of millions of transistors on a single chip ([4.9.3](/4.9.3#sec-3.1)).

### 6.6.1. Light-Emitting Diodes and Semiconductor Lasers

**Definition 6.6.1** A p–n junction in which, under forward bias, electrons injected from the n region and holes injected from the p region recombine in the junction region and release energy (about $E_{\mathrm{g}}$) in the form of photons is called a **light-emitting diode** (LED).

The wavelength of the emitted light is determined by the energy gap, $\lambda\approx\frac{1240\,\mathrm{nm}}{E_{\mathrm{g}}/\mathrm{eV}}$: $\ce{GaAs}$ emits infrared light of about $870\,\mathrm{nm}$, $\ce{GaAsP}$ emits red light and $\ce{InGaN}$ emits blue light. In silicon the bottom of the conduction band and the top of the valence band are not at the same $k$ (an indirect gap), and lattice vibrations must take part in recombination to conserve momentum, so the luminous efficiency is very low; LEDs are therefore made of direct-gap materials such as $\ce{GaAs}$ and $\ce{GaN}$. Akasaki, Amano and Nakamura invented the efficient blue LED, for which they received the 2014 Nobel Prize in Physics; a blue LED exciting a phosphor gives white-light illumination.

In a heavily doped p–n junction under a sufficiently large forward current, both the number of electrons in the conduction band and the number of holes in the valence band in the junction region are large, and **population inversion** ([5.5.5](/5.5.5#sec-5.2.3)) is established between the bottom of the conduction band and the top of the valence band; using two cleaved faces of the crystal as the mirrors of an **optical resonator** gives a semiconductor laser (laser diode). It is small, efficient and directly modulated by current, and is used in optical-fiber communications, optical-disc read heads and laser pointers.

### 6.6.2. Photovoltaic Cells

When light shines on a p–n junction, photons with energy greater than $E_{\mathrm{g}}$ produce electron–hole pairs near the junction. The built-in field pushes holes toward the p region and electrons toward the n region, so the p region becomes positively and the n region negatively charged, the p region is at a higher potential than the n region, and the p–n junction becomes a source of electromotive force; this is the principle of the photovoltaic cell (solar cell). The open-circuit voltage of a silicon cell is about $0.6$–$0.7\,\mathrm{V}$. In a single-junction cell, photons with energy below $E_{\mathrm{g}}$ cannot be absorbed and the excess energy of photons above $E_{\mathrm{g}}$ becomes heat, so the theoretical efficiency has an upper limit (the Shockley–Queisser limit, about $33\%$); stacking materials of different gaps in a multijunction cell can exceed this limit. The same structure under reverse bias serves as a photodiode that detects optical signals.

### 6.6.3. Transistors

- A bipolar transistor consists of two back-to-back p–n junctions (npn or pnp), and its three regions are called the emitter, base and collector. The base is very thin, and most of the carriers injected from the emitter into the base cross it and reach the collector, so a very small base current $I_{\mathrm{B}}$ can control a much larger collector current $I_{\mathrm{C}}$. For a given transistor $I_{\mathrm{C}}/I_{\mathrm{B}}$ is approximately constant (tens to hundreds), so it can be used as an amplifier.

**Definition 6.6.2 (Field-Effect Transistor)** A transistor in which the electric field produced by a gate voltage controls the width or the existence of a conducting channel between source and drain, and thereby controls the drain current, is called a **field-effect transistor** (FET).

In a junction field-effect transistor, a thin n-type layer forms the conducting channel between source and drain, and the gate is a p-type region forming a p–n junction with the channel. With no gate voltage, electrons flow from the source through the channel to the drain; making the gate potential lower than the source puts the p–n junction under reverse bias, the depletion region widens and the channel narrows, and when the gate voltage is large enough the channel is pinched off and the drain current is cut off. The gate voltage thus switches the current on and off, giving a signal of 1 or 0. The field-effect transistors in today's integrated circuits are metal–oxide–semiconductor field-effect transistors (MOSFETs): a layer of insulating oxide separates the gate from the channel, the gate voltage induces (or removes) a conducting channel at the semiconductor surface, and the gate draws almost no current. **CMOS** circuits built from nMOS and pMOS transistors are the basic structure of digital logic gates ([4.9.3](/4.9.3#sec-3.2)).

### 6.6.4. Measuring Energy Bands

The band structure $E(\boldsymbol{k})$ can be measured directly by angle-resolved photoemission spectroscopy (ARPES), whose principle is the **photoelectric effect** ([5.5.1](/5.5.1#sec-1.2)). The sample is illuminated with monochromatic light of energy $h\nu$ (ultraviolet light or synchrotron radiation), and the kinetic energy $E_{\mathrm{kin}}$ and emission angle $\theta$ of the emitted photoelectrons are measured. By energy conservation, the binding energy of the electron in the solid (measured from the Fermi level) is

$$
E_{\mathrm{B}}=h\nu-E_{\mathrm{kin}}-W_0,
$$
where $W_0$ is the work function; as the electron crosses the surface, the momentum parallel to the surface is conserved, $\hbar k_\parallel=\sqrt{2m_{\mathrm{e}}E_{\mathrm{kin}}}\,\sin\theta$. Measuring angle by angle gives the relation between electron energy and momentum, that is, the band structure. ARPES has become the main tool for studying the electronic structure of new materials such as high-temperature superconductors, graphene and topological insulators (for example $\ce{Bi2Te3}$, whose surface has gapless surface states with a conical dispersion).

## Summary

| Topic | Key points |
|---|---|
| Free electron gas | ideal Fermi gas in a three-dimensional well; $E_{\mathrm{F}}=\frac{\hbar^2}{2m_{\mathrm{e}}}(3\pi^2n)^{2/3}$, a few $\mathrm{eV}$ in metals; $v_{\mathrm{F}}\sim10^6\,\mathrm{m\,s^{-1}}$, $T_{\mathrm{F}}\sim10^4$–$10^5\,\mathrm{K}$; $g(E)\propto\sqrt E$ |
| Bloch's theorem | in a periodic potential $\psi_k=\mathrm{e}^{\mathrm{i}kx}u_k(x)$; bands $E_n(k)$, $k$ restricted to the first Brillouin zone, $2N$ states per band; a perfect lattice does not scatter electrons |
| Tight-binding model | eigenvalue problem of a tridiagonal matrix; $E(k)=\varepsilon_0-2t\cos ka$, bandwidth $4t$ |
| Filling of bands | filled, partially filled, empty, valence and conduction bands, band gap and energy gap $E_{\mathrm{g}}$; a filled band does not conduct |
| Conductivity | conductors have a partially filled band; semiconductors have a small gap ($0.1$–$2\,\mathrm{eV}$), insulators a large one |
| Semiconductors | intrinsic: electrons and holes in pairs, $n=p=n_{\mathrm{i}}$; n-type (donors), p-type (acceptors); $np=n_{\mathrm{i}}^2$ |
| p–n junction | depletion region and built-in field, band bending $eU_0$; $I=I_{\mathrm{s}}(\mathrm{e}^{eU/(k_{\mathrm{B}}T)}-1)$, conduction in one direction |
| Devices | LED and semiconductor laser (light from recombination, $\lambda\approx hc/E_{\mathrm{g}}$), photovoltaic cell, bipolar transistor, field-effect transistor |

## Questions

1. Why does the resistance of a metal increase with temperature while that of a semiconductor decreases?

   **Answer** the number of carriers in a metal is almost constant and scattering by lattice vibrations strengthens with temperature; the number of carriers in a semiconductor increases rapidly with temperature as $\mathrm{e}^{-E_{\mathrm{g}}/(2k_{\mathrm{B}}T)}$.

2. The valence-electron number density of sodium is $2.65\times10^{28}\,\mathrm{m^{-3}}$. Estimate its Fermi energy and Fermi temperature.

   **Answer** from Eq. (6.2), $E_{\mathrm{F}}\approx3.2\,\mathrm{eV}$, $T_{\mathrm{F}}\approx3.8\times10^4\,\mathrm{K}$.

3. According to classical theory the free electrons in a metal should increase the molar heat capacity by $\frac32R$; why is this not observed experimentally?

   **Answer** only electrons within a range of about $k_{\mathrm{B}}T$ near the Fermi level, a fraction of about $T/T_{\mathrm{F}}$, can be thermally excited.

4. Divalent magnesium has two 3s electrons per atom, which exactly fill the 3s band; why is it still a metal?

   **Answer** the 3s band overlaps the 3p band.

5. Why is silicon unsuitable for making light-emitting diodes?

   **Answer** silicon is an indirect-gap semiconductor; recombination of an electron and a hole must also conserve momentum and requires the participation of lattice vibrations, so the probability of radiative recombination is very small.
