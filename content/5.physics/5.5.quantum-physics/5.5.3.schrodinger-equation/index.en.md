---
title: The Schrödinger Equation
description: The Schrödinger equation and its linearity, the basic postulates of quantum mechanics and the Hamiltonian, stationary states and the energy eigenvalue equation; energy levels, zero-point energy and standing waves of the infinite square well; step potentials and finite barriers, the tunnel effect, the transmission coefficient, alpha decay and the scanning tunneling microscope; equally spaced levels, Hermite polynomials and the probability distribution of the one-dimensional quantum harmonic oscillator.
source_hash: cea384552553
---

The previous two chapters ([5.5.1](/5.5.1), [5.5.2](/5.5.2)) showed that both light and massive particles have **wave–particle duality**, that the state of a particle is described by a **wave function**, and that $\lvert\Psi\rvert^2$ is the probability density of finding the particle. What is still missing is a dynamical law: given the force field in which the particle moves, how does the wave function change with time? The Schrödinger equation of this chapter answers this question, and its role in quantum mechanics is that of **Newton's second law** in classical mechanics. When the potential energy does not depend on time, **separation of variables** ([2.5.4](/2.5.4)) turns it into an **eigenvalue** problem, and the quantization of energy appears as the fact that the equation has physically acceptable solutions only at certain discrete energies; mathematically this is the same thing as a vibrating string having only a series of natural frequencies ([2.5.4](/2.5.4#sec-4.1.3)). Three one-dimensional models then illustrate the basic features of quantum mechanics: the infinite square well (energy quantization and zero-point energy), the potential barrier (the tunnel effect) and the harmonic oscillator (equally spaced levels). The next chapter ([5.5.4](/5.5.4)) treats the three-dimensional hydrogen atom by the same method; the harmonic oscillator is the basis of molecular vibrational spectra ([5.5.5](/5.5.5)) and of lattice vibrations in solids, and the well model is generalized to the free electron gas in metals in [5.5.6](/5.5.6).

## 3.1. The Schrödinger Equation

### 3.1.1. Setting Up the Equation

In early 1926 Schrödinger presented de Broglie's **matter wave** hypothesis at a colloquium in Zurich, and Debye remarked that where there is a wave there should be a **wave equation**. A few weeks later Schrödinger produced the equation. It cannot be derived from more fundamental principles; the following argument is only heuristic. A free particle moving in the $x$ direction with momentum $p$ and energy $E$ corresponds to the plane wave

$$
\Psi(x,t)=A\,\mathrm{e}^{\mathrm{i}(px-Et)/\hbar}.
$$
It satisfies $\mathrm{i}\hbar\,\partial_t\Psi=E\Psi$ and $-\mathrm{i}\hbar\,\partial_x\Psi=p\Psi$, hence $-\hbar^2\partial_x^2\Psi=p^2\Psi$. A nonrelativistic free particle has $E=p^2/(2m)$, so

$$
\mathrm{i}\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2}.
$$
In a potential $U$ the energy is $E=p^2/(2m)+U$, and adding $U\Psi$ on the right gives the general equation. This suggests a correspondence rule: the classical energy and momentum correspond to differential operations acting on the wave function, $E\to\mathrm{i}\hbar\,\partial_t$ and $\boldsymbol{p}\to-\mathrm{i}\hbar\nabla$.

**Theorem 3.1.1 (Schrödinger Equation)** When a particle of mass $m$ moves in a potential $U(\boldsymbol{r},t)$, its wave function satisfies

$$
\mathrm{i}\hbar\frac{\partial\Psi(\boldsymbol{r},t)}{\partial t}=\Big[-\frac{\hbar^2}{2m}\nabla^2+U(\boldsymbol{r},t)\Big]\Psi(\boldsymbol{r},t),
\tag{3.1}
$$
where $\nabla^2=\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}$ is the **Laplace operator**. In one dimension it reads $\mathrm{i}\hbar\,\partial_t\Psi(x,t)=-\frac{\hbar^2}{2m}\partial_x^2\Psi+U(x,t)\Psi$.

**Remark 3.1.1** Equation (3.1) is a basic postulate of quantum mechanics, and its correctness can only be tested by experiment, just as Newton's laws cannot be derived from more fundamental classical principles. It has the following features:

- It is a linear homogeneous equation: if $\Psi_1,\Psi_2$ are solutions, so is $c_1\Psi_1+c_2\Psi_2$ ($c_1,c_2$ arbitrary complex numbers). This is exactly what the **superposition principle of quantum states** requires ([5.5.2](/5.5.2)).
- The equation contains the imaginary unit $\mathrm{i}$, and its solutions are in general complex functions. $\Psi$ itself is not observable; what is observable is the probability density $\lvert\Psi\rvert^2=\Psi^*\Psi$.
- It is first order in time, whereas the classical **wave equation** ([2.5.3](/2.5.3)) is second order in time. Hence once $\Psi(\boldsymbol{r},0)$ at the initial time is given, the later wave function is completely determined: what quantum mechanics determines is the evolution of the **probability amplitude**, not the result of a single measurement.
- It is a nonrelativistic equation (it uses $E=p^2/(2m)$) and does not include the creation and annihilation of particles; fast particles must be treated by relativistic quantum mechanics (the Dirac equation), in which the spin of the electron ([5.5.4](/5.5.4)) appears naturally.

### 3.1.2. Postulates of Quantum Mechanics and the Hamiltonian

**Property 3.1.1 (Postulates of Quantum Mechanics)** Nonrelativistic quantum mechanics rests on the following postulates:

1. The state of a microscopic system is completely described by a normalized wave function $\Psi(\boldsymbol{r},t)$, and $\lvert\Psi\rvert^2$ is the probability density of finding the particle at $\boldsymbol{r}$.
2. The change of the wave function with time obeys the Schrödinger equation (3.1).
3. Each mechanical quantity (observable) is represented by a linear Hermitian operator, for example position $\hat x=x$ and momentum $\hat{\boldsymbol{p}}=-\mathrm{i}\hbar\nabla$.
4. The only possible results of a measurement of a mechanical quantity $A$ are the **eigenvalues** of its operator $\hat A$, and the probability of obtaining each eigenvalue is determined by the coefficients in the expansion of the wave function in **eigenfunctions** ([5.5.4](/5.5.4#sec-4.5.1)).

These operators are the **Hermitian operators** of inner product spaces ([2.1.13](/2.1.13)): for the inner product $\langle f,g\rangle=\int f^*g\,\mathrm{d}V$ of square-integrable functions they satisfy $\langle f,\hat Ag\rangle=\langle\hat Af,g\rangle$. By the results of linear algebra, their eigenvalues are all real and eigenfunctions belonging to different eigenvalues are mutually orthogonal, which is the mathematical guarantee that measurement results are real numbers.

**Definition 3.1.1 (Hamiltonian)** The operator

$$
\hat H=\frac{\hat{\boldsymbol{p}}^2}{2m}+U(\boldsymbol{r},t)=-\frac{\hbar^2}{2m}\nabla^2+U(\boldsymbol{r},t)
$$
is called the **Hamiltonian** (Hamiltonian operator) of the particle; when $U$ does not depend explicitly on time, it is the energy operator. In terms of the Hamiltonian, the Schrödinger equation is written

$$
\mathrm{i}\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi.
\tag{3.2}
$$

The Hamiltonian is the operator version of the Hamilton function of classical mechanics (the energy expressed in terms of momenta and coordinates); it should not be confused with the **nabla operator** $\nabla$ of vector analysis ([2.2](/2.2)). In classical mechanics the cause that changes the state of motion of a particle is force; in quantum mechanics what determines the evolution of the wave function is the Hamiltonian. All the influences of the surroundings on the particle, including microscopic interactions that cannot be expressed as "forces", are summarized in the potential function $U$. In what follows we consider only the case in which $U$ does not change with time.

### 3.1.3. Stationary States and the Energy Eigenvalue Equation

Let $U=U(\boldsymbol{r})$ not depend explicitly on $t$. Using **separation of variables**, set $\Psi(\boldsymbol{r},t)=\psi(\boldsymbol{r})T(t)$, substitute into Eq. (3.2) and divide by $\psi T$:

$$
\mathrm{i}\hbar\frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}t}=\frac{1}{\psi}\hat H\psi.
$$
The left side depends only on $t$ and the right side only on $\boldsymbol{r}$, so both equal the same constant, denoted $E$ (it has the dimension of energy). This gives two equations: $\mathrm{i}\hbar\,\mathrm{d}T/\mathrm{d}t=ET$, with solution $T=C\mathrm{e}^{-\mathrm{i}Et/\hbar}$ (an oscillating factor); and

**Definition 3.1.2 (Time-Independent Schrödinger Equation)** The equation

$$
\hat H\psi=-\frac{\hbar^2}{2m}\nabla^2\psi+U(\boldsymbol{r})\psi=E\psi
\tag{3.3}
$$
is called the **time-independent Schrödinger equation**, also called the **energy eigenvalue equation**. The constants $E$ for which it has solutions satisfying the physical conditions are called energy eigenvalues, and the corresponding solutions $\psi_E$ are called energy eigenfunctions. In one dimension it is often written

$$
\psi''(x)+\frac{2m}{\hbar^2}\big[E-U(x)\big]\psi(x)=0.
\tag{3.4}
$$

Mathematically, Eq. (3.3) has solutions for every $E$; physically, however, the wave function must satisfy the standard conditions: single-valued, finite (square-integrable), continuous, and with continuous derivative wherever $U$ is finite. Only certain particular values of $E$ make the solution satisfy these conditions, exactly as the boundary conditions in a **Sturm–Liouville problem** ([2.4.12](/2.4.12#sec-12.5)) select a sequence of eigenvalues.

**Definition 3.1.3 (Stationary State)** A state of definite energy $E$,

$$
\Psi_E(\boldsymbol{r},t)=\psi_E(\boldsymbol{r})\,\mathrm{e}^{-\mathrm{i}Et/\hbar},
$$
is called a **stationary state**. The probability density of a stationary state, $\lvert\Psi_E\rvert^2=\lvert\psi_E\rvert^2$, does not change with time, which is the meaning of the word "stationary".

The energy eigenvalues may be discrete (as for a particle bound in a potential well) or continuous (as for a free particle). Suppose the eigenvalues are discrete, $E_1,E_2,\dots$, with eigenfunctions $\psi_1,\psi_2,\dots$. By linearity the general solution of the Schrödinger equation is a superposition of stationary states

$$
\Psi(\boldsymbol{r},t)=\sum_n C_n\,\psi_n(\boldsymbol{r})\,\mathrm{e}^{-\mathrm{i}E_nt/\hbar},
\tag{3.5}
$$
where the complex constants $C_n$ are determined by expanding the initial wave function in eigenfunctions, $\Psi(\boldsymbol{r},0)=\sum_n C_n\psi_n$ (**eigenfunction expansion**, [2.5.4](/2.5.4#sec-4.4.1)). The energy of a superposed state is uncertain, and its probability density in general changes with time. Solving the energy eigenvalue equation is therefore the most basic calculation in quantum mechanics. We use the one-dimensional equation (3.4) to discuss two kinds of problems:

- Eigenvalue problems: given $U(x)$, find the energy eigenvalues $E_n$ and eigenfunctions $\psi_n$ of a bound particle (Sections 3.2 and 3.4).
- Scattering problems: given the energy $E$ of the incident particle, find the probability that it passes through a potential barrier (Section 3.3).

## 3.2. A Particle in an Infinite Square Well

### 3.2.1. The Model and Its Solution

The free electrons in a metal can move freely inside it but can hardly escape from the surface: near the surface there is a potential step a few electron volts high. Idealizing the step as infinitely high gives the simplest model of binding.

**Definition 3.2.1 (Infinite Square Well)** The potential

$$
U(x)=\begin{cases}0, & \lvert x\rvert<a/2,\\ \infty, & \lvert x\rvert\ge a/2\end{cases}
$$
is called an **infinite square well** of width $a$.

Outside the well $U=\infty$, the particle cannot appear there, and $\psi=0$. Inside the well $U=0$, and Eq. (3.4) becomes $\psi''+k^2\psi=0$ with $k=\sqrt{2mE}/\hbar$ (for $E\le0$ there is only the zero solution, see below), with general solution $\psi=A\sin(kx+\delta)$. The wave function is continuous at the walls, so $\psi(\pm a/2)=0$:

$$
\sin\Big(\frac{ka}{2}+\delta\Big)=0,\qquad \sin\Big(-\frac{ka}{2}+\delta\Big)=0.
$$
These give $ka/2+\delta=l_1\pi$ and $-ka/2+\delta=l_2\pi$, and adding them gives $\delta=l\pi/2$ ($l$ an integer). Disregarding signs, which do not affect $\lvert\psi\rvert^2$, there are only two cases: for $\delta=0$, $\psi=A\sin kx$ is an odd function, and $\sin(ka/2)=0$ gives $ka=n\pi$, $n=2,4,6,\dots$; for $\delta=\pi/2$, $\psi=A\cos kx$ is an even function, and $\cos(ka/2)=0$ gives $ka=n\pi$, $n=1,3,5,\dots$. The value $n=0$ gives $\psi\equiv0$, which is not a physical state. Combining the two, $ka=n\pi$, $n=1,2,3,\dots$.

### 3.2.2. Energy Eigenvalues and Zero-Point Energy

From $k^2=2mE/\hbar^2$ and $k=n\pi/a$,

$$
E_n=\frac{\pi^2\hbar^2}{2ma^2}\,n^2,\qquad n=1,2,3,\dots
\tag{3.6}
$$

The energy of a particle bound in the well can take only a series of discrete values, which is the quantization of energy; each energy value corresponds to an energy level, and $n$ is called the quantum number. A state in a potential well, a harmonic oscillator or an atom, in which the particle cannot escape to infinity, is called a *bound state*, and the energies of bound states are always discrete.

The lowest energy $E_1=\pi^2\hbar^2/(2ma^2)>0$ is called the *zero-point energy*: the particle cannot rest at the bottom of the well. This is a result peculiar to quantum mechanics and can be understood from the **Heisenberg uncertainty relation**: the particle is confined to a width $a$, $\Delta x\sim a$, so its momentum cannot be exactly zero, $\Delta p_x\gtrsim\hbar/a$, and the kinetic energy is at least of the order of $\hbar^2/(ma^2)$, consistent with $E_1$. For the same reason no solution with $E=0$ exists.

The spacing of adjacent levels is

$$
\Delta E_n=E_{n+1}-E_n=\frac{\pi^2\hbar^2}{2ma^2}(2n+1),\qquad \frac{\Delta E_n}{E_n}=\frac{2n+1}{n^2}\approx\frac{2}{n}\quad(n\gg1).
$$
The higher the level, the larger the spacing, but the smaller the relative spacing. The wider the well and the heavier the particle, the denser the levels.

**Example 3.2.1 (Microscopic and Macroscopic Wells)** (1) For an electron in a well of width $a=1\,\mathrm{nm}$, $E_1=\frac{h^2}{8m_{\mathrm{e}}a^2}\approx6.0\times10^{-20}\,\mathrm{J}\approx0.38\,\mathrm{eV}$, of the same order as energies in atoms, and the quantization is very pronounced. (2) For a ball of mass $1\,\mathrm{g}$ in a box of width $a=1\,\mathrm{cm}$, $E_1\approx5.5\times10^{-61}\,\mathrm{J}$; if it moves at $1\,\mathrm{mm/s}$, its kinetic energy $5\times10^{-10}\,\mathrm{J}$ corresponds to $n\approx3\times10^{25}$, the relative level spacing is $2/n\sim10^{-25}$, and the energy can be regarded as completely continuous.

### 3.2.3. Standing Waves and Eigenfunctions

By the de Broglie relation, the magnitude of the momentum of a particle in the $n$th level is $p_n=\sqrt{2mE_n}=n\pi\hbar/a$ and its wavelength is $\lambda_n=h/p_n=2a/n$; that is, the width of the well is exactly an integer multiple of half a wavelength. This is exactly the same as the **standing waves** on a string fixed at both ends ([5.1.7](/5.1.7)): the walls are **nodes**, and each energy eigenstate corresponds to a standing wave of a particular wavelength. Conversely, one may say that the quantization of energy in a well is the inevitable result of the **de Broglie waves** forming stable standing waves.

From the **normalization condition** $\int_{-a/2}^{a/2}\lvert\psi_n\rvert^2\,\mathrm{d}x=A^2\cdot\frac a2=1$ we get $A=\sqrt{2/a}$, so

$$
\psi_n(x)=\begin{cases}\sqrt{\dfrac2a}\cos\dfrac{n\pi x}{a}, & n=1,3,5,\dots,\\[2ex] \sqrt{\dfrac2a}\sin\dfrac{n\pi x}{a}, & n=2,4,6,\dots,\end{cases}\qquad \lvert x\rvert<\frac a2,
\tag{3.7}
$$
and $\psi_n=0$ outside the well. The corresponding stationary state is $\Psi_n=\psi_n\mathrm{e}^{-\mathrm{i}E_nt/\hbar}$, and the probability density $\lvert\psi_n\rvert^2$ does not change with time. The eigenfunctions have the following properties:

- Parity: the potential is symmetric about $x=0$, so each eigenfunction is either even ($n$ odd) or odd ($n$ even), and the ground state is even.
- Number of nodes: $\psi_n$ has $n-1$ zeros inside the well, and the higher the energy, the more zeros (the Sturm oscillation theorem, [2.4.12](/2.4.12#sec-12.5.2)).
- Orthonormality: $\int\psi_m\psi_n\,\mathrm{d}x=\delta_{mn}$, and $\{\psi_n\}$ is complete: this is the Fourier sine–cosine series on $[-a/2,a/2]$.

![The infinite square well. Left: the first four eigenfunctions ψ_n, each drawn at the height of its level E_n = n²E_1; the nth has n - 1 nodes, and the walls are nodes. Right: probability densities for n = 1, 2, 20 compared with the uniform distribution of a classical particle (dashed line)](./plots/infinite-well.py)

The quantum probability distribution is quite different from the classical one: a classical particle moves back and forth in the well at constant speed and spends the same time everywhere, so its probability density is uniform, $1/a$; the ground-state particle is most likely to be found at the center of the well, and for $n=2$ the probability of finding the particle at the center is zero. For large $n$ the oscillations of $\lvert\psi_n\rvert^2$ become denser and denser, and its average over any interval of finite width tends to $1/a$, in agreement with the classical result.

**Definition 3.2.2** The tendency of the behavior of a quantum system to approach the results of classical physics in the limit of large quantum numbers is called the **correspondence principle** (Bohr's correspondence principle).

The correspondence principle is a guiding principle that Bohr put forward in establishing the old quantum theory ([5.5.4](/5.5.4)); it requires the new theory to reproduce classical results in the range where classical physics has been tested, just as special relativity reduces to Newtonian mechanics for $v\ll c$.

## 3.3. Barrier Penetration

### 3.3.1. The Step Barrier

At the junction of a metal and a semiconductor, and near the surface of an atomic nucleus, the potential energy rises to form a *potential barrier*. The simplest barrier is the step potential:

$$
U(x)=\begin{cases}0, & x<0\ \text{(I)},\\ U_0, & x>0\ \text{(II)}.\end{cases}
$$
Let a particle of energy $E<U_0$ be incident from the left. A classical particle reaching $x=0$ can only be totally reflected, because in region II its kinetic energy $E-U_0$ would be negative. A quantum particle is a wave, and the situation is different. Let

$$
k=\frac{\sqrt{2mE}}{\hbar},\qquad \kappa=\frac{\sqrt{2m(U_0-E)}}{\hbar}.
$$
Equation (3.4) becomes $\psi''+k^2\psi=0$ in region I and $\psi''-\kappa^2\psi=0$ in region II, with general solutions

$$
\psi_{\mathrm{I}}=A\mathrm{e}^{\mathrm{i}kx}+B\mathrm{e}^{-\mathrm{i}kx},\qquad \psi_{\mathrm{II}}=C\mathrm{e}^{-\kappa x}+D\mathrm{e}^{\kappa x}.
$$
Here $\psi_{\mathrm{I}}$ is a superposition of an incident and a reflected wave (a wave-type solution); $\psi$ must be finite as $x\to+\infty$, so $D=0$ and $\psi_{\mathrm{II}}=C\mathrm{e}^{-\kappa x}$ is an exponentially decaying solution. Continuity of $\psi$ and $\psi'$ at $x=0$ gives $A+B=C$ and $\mathrm{i}k(A-B)=-\kappa C$, whose solution is

$$
\frac BA=\frac{k-\mathrm{i}\kappa}{k+\mathrm{i}\kappa},\qquad \frac CA=\frac{2k}{k+\mathrm{i}\kappa}.
$$
Since $\lvert B/A\rvert=1$, the particle is in the end totally reflected, as classically; but $C\ne0$, and the probability density of finding the particle inside the barrier,

$$
\lvert\psi_{\mathrm{II}}(x)\rvert^2=\lvert C\rvert^2\mathrm{e}^{-2\kappa x},
$$
is not zero; it decays exponentially over the penetration depth $1/(2\kappa)$. The higher the barrier (the larger $U_0-E$), the faster the decay. For an electron with $U_0-E=5\,\mathrm{eV}$, $\kappa\approx1.15\times10^{10}\,\mathrm{m^{-1}}$ and the penetration depth is less than $0.05\,\mathrm{nm}$. It is in just this way that the electrons in a metal "leak" slightly out of the surface and form a very thin layer of electron gas outside it.

### 3.3.2. A Barrier of Finite Width and the Tunnel Effect

If the barrier has only a finite width $a$, with $U=U_0$ for $0<x<a$ and $U=0$ elsewhere, the decaying wave still has nonzero amplitude when it reaches the right boundary of the barrier and can continue in region III as a plane wave $F\mathrm{e}^{\mathrm{i}kx}$. A particle with energy lower than the height of the barrier has a certain probability of passing through it; this is called the *tunnel effect*, also called barrier penetration.

**Definition 3.3.1 (Transmission Coefficient)** The ratio of the probability currents of the transmitted and the incident wave, $T=\lvert F/A\rvert^2$ (the potential energy is the same on both sides, so the speeds are equal), is called the **transmission coefficient** of the barrier; it is the probability that an incident particle passes through the barrier.

Requiring $\psi,\psi'$ to be continuous at $x=0$ and at $x=a$ gives a system of linear equations for $B,C,D,F$, whose solution is

$$
T=\Big[1+\frac{U_0^2\sinh^2(\kappa a)}{4E(U_0-E)}\Big]^{-1}.
\tag{3.8}
$$
For $\kappa a\gg1$, $\sinh\kappa a\approx\frac12\mathrm{e}^{\kappa a}$, so

$$
T\approx\frac{16E(U_0-E)}{U_0^2}\,\mathrm{e}^{-2\kappa a}\sim\mathrm{e}^{-2\kappa a}=\exp\Big[-\frac{2a}{\hbar}\sqrt{2m(U_0-E)}\Big].
\tag{3.9}
$$
The prefactor is of order 1, and the transmission coefficient is determined mainly by the exponential: it is extremely sensitive to the barrier width $a$, the particle mass $m$ and the "missing energy" $U_0-E$. For a barrier of irregular shape one can divide it into many narrow strips, and approximately $T\approx\exp\big[-\frac2\hbar\int\sqrt{2m(U(x)-E)}\,\mathrm{d}x\big]$, with the integral over the region where $U>E$ (the WKB approximation).

![A rectangular barrier. Left: probability density of a scattering state for E = U_0/2 and κa = 1.8: the incident and reflected waves interfere and produce oscillations, the density decays exponentially inside the barrier and is constant in the transmitted region. Right: transmission coefficient of an electron versus barrier width (logarithmic scale); solid line: exact formula (3.8), dashed line: e^{-2κa}](./plots/tunneling.py)

**Example 3.3.1 (Transmission Coefficient of an Electron)** Let $U_0-E=5\,\mathrm{eV}$, so $\kappa\approx1.15\times10^{10}\,\mathrm{m^{-1}}$. For $a=0.1\,\mathrm{nm}$, $\mathrm{e}^{-2\kappa a}\approx0.10$; for $a=0.5\,\mathrm{nm}$ it is about $10^{-5}$; for $a=1\,\mathrm{nm}$ about $10^{-10}$. Thus once the barrier is a few nanometers wide, the tunneling of electrons is almost negligible; for macroscopic objects (large $m$, large $a$), $T$ is in practice exactly zero, and the quantum conclusion goes over into the classical one.

**Remark 3.3.1** A particle passing through a barrier does not contradict energy conservation. The statement that "the particle has negative kinetic energy inside the barrier" assumes that the particle has definite position and momentum at the same time, which is just what the **Heisenberg uncertainty relation** denies: finding the particle inside the barrier means that the position uncertainty is $\Delta x\lesssim a$, and the momentum and energy are correspondingly uncertain. The estimate with $\Delta E\approx p\Delta p/m$ is only a qualitative picture; the reliable conclusion is Eq. (3.8).

### 3.3.3. Applications of the Tunnel Effect

The earliest application of the tunnel effect was the explanation of the alpha decay of atomic nuclei. An alpha particle inside the nucleus is bound by the short-range nuclear force and outside it is subject to the long-range Coulomb repulsion (**Coulomb's law**); the combined barrier near the nuclear surface is as high as about $30\,\mathrm{MeV}$. For example, the alpha particle emitted in $\ce{^{238}U -> ^{234}Th + ^{4}He}$ has an energy of only $4.27\,\mathrm{MeV}$ and classically cannot escape. In 1928 Gamow, and independently Condon and Gurney, explained alpha decay by the tunnel effect: the alpha particle strikes the barrier from inside the nucleus about $10^{21}$ times per second, and each time it passes through with the extremely small probability $T$. Because $T$ depends exponentially on $E$, when the alpha-particle energy differs by less than a factor of two, the half-life can range from less than a microsecond to more than $10^{10}$ years ($4.5\times10^9$ years for $\ce{^{238}U}$); this is exactly the Geiger–Nuttall law found experimentally, and theory and experiment agree.

The tunnel diode (Esaki, 1957), field emission from metals, and the writing and erasing of flash memory by charge passing through a thin oxide layer all use the tunneling of electrons.

The *scanning tunneling microscope* (STM) was invented by Binnig and Rohrer in 1981, for which they shared the 1986 Nobel Prize in Physics with Ruska, the inventor of the electron microscope. The tip of a conducting probe is at a distance $d\sim1\,\mathrm{nm}$ from the sample surface, and the vacuum between them is a barrier; when a bias voltage $U$ is applied, electrons tunnel and form a tunneling current

$$
i\propto U\,\mathrm{e}^{-A\sqrt{\phi}\,d},\qquad A=\frac{2\sqrt{2m_{\mathrm{e}}}}{\hbar}\approx10.25\,\mathrm{nm^{-1}\,eV^{-1/2}},
$$
where $\phi$ is the average barrier height of the surface (of the order of the **work function**, about $4\,\mathrm{eV}$). A change of $d$ by $0.1\,\mathrm{nm}$ then changes the current by about an order of magnitude. A piezoelectric ceramic drives the tip across the surface while a feedback circuit keeps the current constant, and the rise and fall of the tip traces out the atomic-scale topography of the surface (lateral resolution about $0.1\,\mathrm{nm}$). What an STM actually measures is the distribution of $\lvert\psi\rvert^2$ of the electrons near the surface; it can also use the tip to move atoms adsorbed on the surface one by one (such as $\ce{Xe}$ atoms on a $\ce{Ni}$ surface), and it is widely used in surface physics, materials science, chemistry and biology.

## 3.4. The One-Dimensional Harmonic Oscillator

### 3.4.1. The Time-Independent Schrödinger Equation

Near a stable equilibrium position any potential energy can be approximated by a parabola (expanding the minimum of the **potential energy curve** to second order), so the harmonic oscillator is one of the most important models in physics: the vibrations of atoms in molecules, lattice vibrations in crystals and every mode of the electromagnetic field are harmonic oscillators. The energy of a classical harmonic oscillator can take continuous values, but with such a model one cannot explain **blackbody** radiation ([5.5.1](/5.5.1)) or the specific heat of solids at low temperatures; the energy of the oscillator must be quantized.

Take the equilibrium position as the origin and the zero of potential energy. The potential energy of a harmonic oscillator of mass $m$ and spring constant $k$ is $U=\frac12kx^2=\frac12m\omega^2x^2$, where $\omega=\sqrt{k/m}$ is the angular frequency of the classical **simple harmonic motion** ([5.1.6](/5.1.6)). Such a quantum system is called a *quantum harmonic oscillator*. The time-independent Schrödinger equation is

$$
-\frac{\hbar^2}{2m}\psi''+\frac12m\omega^2x^2\psi=E\psi.
$$
Introduce the dimensionless coordinate and energy

$$
\xi=\alpha x,\quad \alpha=\sqrt{\frac{m\omega}{\hbar}},\qquad \lambda=\frac{2E}{\hbar\omega},
$$
and the equation becomes $\psi''(\xi)+(\lambda-\xi^2)\psi=0$. For large $\lvert\xi\rvert$, $\psi\approx\mathrm{e}^{\pm\xi^2/2}$, and finiteness requires $\mathrm{e}^{-\xi^2/2}$. Setting $\psi=H(\xi)\mathrm{e}^{-\xi^2/2}$ gives Hermite's equation

$$
H''-2\xi H'+(\lambda-1)H=0.
$$
Using the **power series** method ([2.4.10](/2.4.10)), the coefficients of $H=\sum c_j\xi^j$ satisfy $c_{j+2}=\frac{2j+1-\lambda}{(j+1)(j+2)}c_j$. If the series does not terminate, $H$ grows like $\mathrm{e}^{\xi^2}$ as $\lvert\xi\rvert\to\infty$ and $\psi$ cannot be normalized; so the series must terminate at some term, that is, $\lambda=2n+1$, $n=0,1,2,\dots$. A terminating series is a polynomial of degree $n$, and with a suitable constant factor it is the *Hermite polynomials*

$$
H_0=1,\quad H_1=2\xi,\quad H_2=4\xi^2-2,\quad H_3=8\xi^3-12\xi,\quad\dots,\qquad H_n(\xi)=(-1)^n\mathrm{e}^{\xi^2}\frac{\mathrm{d}^n}{\mathrm{d}\xi^n}\mathrm{e}^{-\xi^2}.
$$

### 3.4.2. Quantization of Energy

From $\lambda=2E/(\hbar\omega)=2n+1$ we get

$$
E_n=\Big(n+\frac12\Big)\hbar\omega=\Big(n+\frac12\Big)h\nu,\qquad n=0,1,2,\dots
\tag{3.10}
$$

- The levels are equally spaced, with spacing $\hbar\omega$ determined only by the classical vibration frequency. This is exactly the "**energy quantum**" $h\nu$ that Planck assumed to explain blackbody radiation ([5.5.1](/5.5.1)); quantum mechanics also gives the zero-point energy that Planck did not have.
- The zero-point energy $E_0=\frac12\hbar\omega$ is consistent with the **Heisenberg uncertainty relation**. In the ground state $\langle x\rangle=\langle p\rangle=0$, so $E=\frac{(\Delta p)^2}{2m}+\frac12m\omega^2(\Delta x)^2$; by $\Delta x\,\Delta p\ge\hbar/2$ and the inequality of arithmetic and geometric means, $E\ge2\sqrt{\frac{(\Delta p)^2}{2m}\cdot\frac{m\omega^2(\Delta x)^2}{2}}=\omega\,\Delta x\,\Delta p\ge\frac12\hbar\omega$, and the ground state attains equality.
- Molecular vibration: the vibrational quantum $\hbar\omega$ of a diatomic molecule is usually between $0.1$ and $0.5\,\mathrm{eV}$ (about $0.52\,\mathrm{eV}$ for $\ce{H2}$ and $0.27\,\mathrm{eV}$ for $\ce{CO}$), much larger than $k_{\mathrm{B}}T\approx0.026\,\mathrm{eV}$ at room temperature. Almost all molecules are in the vibrational ground state, the vibrational **degrees of freedom** do not contribute to the heat capacity, and the molecules can be treated as rigid. This is why the classical **equipartition theorem** gives the wrong heat capacity of a diatomic gas at ordinary temperatures ([5.2.1](/5.2.1)).
- Macroscopic limit: for a spring oscillator of mass $0.1\,\mathrm{kg}$ and spring constant $10\,\mathrm{N/m}$ ($\omega=10\,\mathrm{s^{-1}}$) oscillating with amplitude $1\,\mathrm{cm}$, the energy $5\times10^{-4}\,\mathrm{J}$ corresponds to $n\approx5\times10^{29}$, the quantization of energy is completely unobservable, in accord with the correspondence principle.

### 3.4.3. Wave Functions and Probability Densities

The normalized eigenfunctions are

$$
\psi_n(x)=\Big(\frac{\alpha}{2^nn!\sqrt\pi}\Big)^{1/2}H_n(\alpha x)\,\mathrm{e}^{-\alpha^2x^2/2},
\tag{3.11}
$$
for example $\psi_0=\big(\frac{\alpha}{\sqrt\pi}\big)^{1/2}\mathrm{e}^{-\alpha^2x^2/2}$ and $\psi_1=\big(\frac{\alpha}{2\sqrt\pi}\big)^{1/2}2\alpha x\,\mathrm{e}^{-\alpha^2x^2/2}$. As for the square well, $\psi_n$ has the same parity as $n$, has $n$ nodes, and the $\psi_n$ form an orthonormal complete system of functions.

![The one-dimensional harmonic oscillator. Left: the first five eigenfunctions drawn at the heights of the levels E_n = (n + 1/2)ħω; the gray line is the potential U = mω²x²/2 and dotted lines mark the classical range of motion. Right: probability density for n = 11 compared with that of the classical oscillator (dashed line); vertical lines mark the classical turning points](./plots/harmonic-oscillator.py)

For small quantum numbers the probability distribution is completely different from that of the classical oscillator. The ground-state probability density

$$
\lvert\psi_0(x)\rvert^2=\frac{\alpha}{\sqrt\pi}\mathrm{e}^{-\alpha^2x^2}
$$
is a **normal distribution** ([3.1](/3.1)) with mean 0 and variance $\frac{1}{2\alpha^2}=\frac{\hbar}{2m\omega}$, with its maximum at $x=0$. A classical oscillator, in contrast, has its greatest speed at the equilibrium position, where it stays the shortest time and is least likely to be found, and near the turning points $\pm A$ its speed is zero and it is most likely to be found; its probability density is $\frac{1}{\pi\sqrt{A^2-x^2}}$.

Another difference is that the quantum oscillator also has probability in the classically forbidden region $\lvert x\rvert>A_n$ ($U>E$, $A_n=\sqrt{2n+1}/\alpha$), another manifestation of the tunnel effect: the probability for the ground-state particle to be in the forbidden region is $\operatorname{erfc}(1)\approx0.16$. As the quantum number increases, the oscillations of $\lvert\psi_n\rvert^2$ become denser, and on average the distribution approaches the classical one (right panel of the figure above, $n=11$), which is again an expression of the correspondence principle.

### 3.4.4. Numerical Solution

Few potentials can be solved analytically. For a general one-dimensional potential $U(x)$, one can discretize $x$ on a grid of step $h$ and replace the second derivative by the central difference $\psi''(x_j)\approx(\psi_{j+1}-2\psi_j+\psi_{j-1})/h^2$; the time-independent Schrödinger equation then becomes an eigenvalue problem for a real symmetric tridiagonal matrix, which can be solved with the symmetric eigenvalue solver of SciPy ([4.4.3](/4.4.3#sec-3.2.3), [4.4.4](/4.4.4)). We test the method on the harmonic oscillator (take $\hbar=m=\omega=1$, so the exact values are $n+\frac12$):

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal

# Units: hbar = m = omega = 1, so E_n should equal n + 1/2.
L, N = 10.0, 2000                       # grid on [-L, L], Phi = 0 at both ends
x, h = np.linspace(-L, L, N + 2, retstep=True)
x = x[1:-1]                              # interior points
diag = 1 / h**2 + 0.5 * x**2             # -1/2 Phi'' by central differences, plus U(x)
off = np.full(N - 1, -0.5 / h**2)
E, Phi = eigh_tridiagonal(diag, off, select="i", select_range=(0, 4))
print(np.round(E, 6))
```

```text
[0.499997 1.499984 2.499959 3.499922 4.499872]
```

The error is about $10^{-5}$ and decreases as $h^2$. The condition $\psi=0$ at the endpoints of the interval amounts to placing infinitely high walls at $\pm L$; as long as $L$ is much larger than the classical range of motion, it has almost no effect on the low-lying levels. Replacing `0.5 * x**2` by another potential function, the same program finds the energy levels of any one-dimensional well.

## Summary

| Model | Levels | Main conclusions |
|---|---|---|
| Infinite square well (width $a$) | $E_n=\dfrac{\pi^2\hbar^2}{2ma^2}n^2$, $n=1,2,\dots$ | Energy quantization, zero-point energy, standing waves, classical behavior as $n\to\infty$ |
| Potential barrier (height $U_0$, width $a$) | Continuous | Tunnel effect, $T\sim\mathrm{e}^{-2\kappa a}$, $\kappa=\sqrt{2m(U_0-E)}/\hbar$ |
| Harmonic oscillator (angular frequency $\omega$) | $E_n=(n+\frac12)\hbar\omega$, $n=0,1,2,\dots$ | Equally spaced levels, zero-point energy $\frac12\hbar\omega$, ground state a normal distribution |

- The Schrödinger equation $\mathrm{i}\hbar\,\partial_t\Psi=\hat H\Psi$ is a linear first-order equation; when the potential does not depend on time, separating variables gives the energy eigenvalue equation $\hat H\psi=E\psi$ and the stationary states $\psi\,\mathrm{e}^{-\mathrm{i}Et/\hbar}$, and the general solution is a superposition of stationary states.
- The quantization of energy of bound states comes from the standard conditions on the wave function (single-valued, finite, continuous); mathematically it is the fact that a boundary value problem has only discrete eigenvalues.

## Questions

1. Is the Schrödinger equation rigorously derived?
   Hint: no. The argument in Section 3.1.1 only shows that it is compatible with the plane wave of a free particle; it is a basic postulate, tested by experiment.
2. How does the Schrödinger equation guarantee that wave functions obey the superposition principle?
   Hint: the equation is linear and homogeneous in $\Psi$, so linear combinations of solutions are again solutions.
3. For a particle in the ground state of an infinite square well and of a harmonic oscillator, how many points other than the boundary have zero probability density? What about the $n$th excited state?
   Hint: the ground state has no nodes; $\psi_n$ of the square well has $n-1$ nodes, and $\psi_n$ of the oscillator has $n$ nodes (the oscillator is numbered from $n=0$), so in both cases the $k$th excited state has $k$ nodes.
4. In an infinite well of width $2a$ the bottom of the right half is raised by $U_0$ ($E>U_0$). On which side is the wavelength larger? On which side is the amplitude of the wave function larger?
   Hint: on the right the kinetic energy $E-U_0$ is smaller, so the momentum is smaller and the wavelength larger; the particle moves more slowly on the right and stays longer there, so the amplitude is also larger.
5. Compare the classical and quantum one-dimensional harmonic oscillators.
   Hint: continuous versus equally spaced discrete energies; minimum energy zero versus zero-point energy $\frac12\hbar\omega$; probability largest at the two ends versus ground state largest at the center; particle cannot enter versus can enter the region $U>E$.
