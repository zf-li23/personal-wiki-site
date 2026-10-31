---
title: Active Matter and Collective Motion
description: "The physics of materials whose constituents consume energy to move or to exert forces: soft-matter background (colloids, liquid crystals, order parameters and topological defects), active Brownian particles and their effective diffusion, the Vicsek model of flocking, the Mermin–Wagner argument and why moving agents can order in two dimensions (Toner–Tu theory), correlations in bird flocks, motility-induced phase separation, active nematics and active gels, bacterial turbulence, and the collective motion and jamming of cells in tissues."
---

A flock of starlings turns as one, a drop of bacterial suspension churns in vortices larger than any bacterium, a mixture of microtubules and kinesin motors flows spontaneously, and the cells of an epithelium stream, swirl and then freeze. In each case the constituents of the material consume energy individually, to swim, to walk along filaments or to contract, and the energy is injected at the smallest scale rather than at the boundaries as in a stirred fluid. Such systems are called active matter. They are out of equilibrium in every volume element, so the theorems that govern equilibrium phases do not apply, and they show phenomena without equilibrium counterparts: long-range order in two dimensions, phase separation without attraction, and spontaneous flow. This chapter introduces the main models and the reasons for their behavior. After the background from soft-matter physics (37.1), we study the simplest active particle (37.2), the flocking transition of the Vicsek model (37.3), why moving agents escape the Mermin–Wagner theorem (37.4), phase separation driven by motility (37.5), active liquid crystals and gels (37.6), and the active matter of cells and tissues (37.7).

The chapter builds on the statistical physics of earlier chapters: **random walks**, **rotational diffusion** and the **Langevin equation** ([7.6.5](/7.6.5)), the hydrodynamics of swimming at low **Reynolds number** ([7.6.22](/7.6.22)), the molecular motors that drive cytoskeletal networks ([7.6.27](/7.6.27)), phase separation in equilibrium ([7.6.29](/7.6.29), [7.2.21](/7.2.21)), and the patterns of reaction–diffusion systems ([7.6.36](/7.6.36)). Tissue mechanics with the **vertex model** and the fluid-to-solid transition of embryonic tissues is treated in [7.5.8](/7.5.8), cell migration and its measurement in [7.6.31](/7.6.31), and the collective behavior of animals from the viewpoint of behavioral ecology in [7.18](/7.18).

## 37.1. Soft Matter Background

### 37.1.1. Colloids and Liquid Crystals

**Definition 37.1.1 (Active Matter)** **Active matter** is matter composed of many interacting units each of which converts stored or ambient free energy into systematic motion or mechanical stress, so that detailed balance is broken locally, at the scale of the units, rather than by boundary conditions or external fields.

Active matter borrows its language from soft-matter physics, the physics of materials whose constituents are large compared with atoms and whose interaction energies are comparable to $k_{\mathrm{B}}T$: colloids, polymers, membranes, foams and **liquid crystals** ([6.1.1](/6.1.1)). Colloidal particles, $10\,\mathrm{nm}$ to $10\,\mu\mathrm{m}$ in size, undergo **Brownian motion**, and weak attractions (for example **depletion forces**, [7.6.23](/7.6.23)) make them aggregate into clusters, gels or crystals. Elongated particles can align without positional order, forming the **nematic phase**, in which rod-like molecules point on average along a common axis, the director $\boldsymbol{n}$, with $\boldsymbol{n}$ and $-\boldsymbol{n}$ equivalent.

Order is measured by order parameters, quantities that vanish in the disordered phase.

**Definition 37.1.2 (Polar and Nematic Order Parameters)** For units with orientations $\boldsymbol{e}_i = (\cos\theta_i, \sin\theta_i)$ in two dimensions, the **polar order parameter** is $\Psi = \lvert N^{-1}\sum_i\boldsymbol{e}_i\rvert$, which detects alignment of heads. The **nematic order parameter** is the traceless symmetric tensor

$$
Q_{\alpha\beta} = \frac1N\sum_i\left(e_{i\alpha}e_{i\beta} - \frac12\delta_{\alpha\beta}\right) = \frac S2\left(2n_\alpha n_\beta - \delta_{\alpha\beta}\right) ,
\tag{37.1}
$$
whose largest eigenvector is the director $\boldsymbol{n}$ and whose scalar order $S = \langle\cos 2(\theta_i - \theta_n)\rangle$ is $1$ for perfect alignment and $0$ for isotropy. It is invariant under $\boldsymbol{e}_i \to -\boldsymbol{e}_i$ and detects alignment of axes. In three dimensions $Q_{\alpha\beta} = S(n_\alpha n_\beta - \delta_{\alpha\beta}/3)$ with $S = \langle P_2(\cos\theta)\rangle$.

Swimming bacteria have a head and a tail and can order in a polar way; a dense suspension of rods, or a network of microtubules pushed apart by motors, has head–tail symmetry at the level of interactions and orders nematically.

### 37.1.2. Topological Defects

An ordered field cannot always be smooth everywhere. In two dimensions the director angle $\varphi(\boldsymbol{x})$ may rotate by a multiple of $\pi$ (for a nematic) or of $2\pi$ (for a polar field) around a point at which the order is lost.

**Definition 37.1.3 (Topological Defect)** A **topological defect** of a two-dimensional orientation field is a point around which the orientation rotates by $2\pi k$ along any closed loop enclosing it, with the topological charge (winding number) $k \neq 0$; $k$ is an integer for polar fields and a multiple of $1/2$ for nematic fields. The charge cannot change under continuous deformation of the field away from the core; defects can only be created or annihilated in pairs of opposite charge.

Near a defect of charge $k$, $\varphi = k\,\operatorname{atan2}(y, x) + \varphi_0$. The elastic energy of a nematic grows as $\pi Kk^2\ln(R/a)$ with the system size $R$ (with $K$ the Frank elastic constant and $a$ the core size), so defects of charge $\pm1/2$, the smallest possible, are the common ones in nematics: a $+1$ defect splits into two $+1/2$ defects, lowering the energy from $\pi K$ to $2 \times \pi K/4$ times the logarithm. The total charge of the defects in a domain is fixed by its topology: on a sphere it is $+2$ (the hairy-ball theorem), in a disk with tangential anchoring at the edge $+1$.

![Topological defects of a two-dimensional director field n = (cos φ, sin φ), drawn as headless segments; around a defect of charge k the director rotates by 2πk on any loop around the core (dot), φ = k atan2(y, x) + φ₀. A: k = +1/2, the comet-shaped defect, which self-propels along its symmetry axis in extensile active nematics. B: k = −1/2, the three-fold defect, which has no preferred direction and moves only passively. C, D: k = +1, an aster (φ₀ = 0) and a vortex (φ₀ = π/2); in nematics such defects usually split into two +1/2 defects](./plots/nematic-defects.py)

## 37.2. Active Brownian Particles

### 37.2.1. Self-Propulsion with Rotational Noise

The simplest active unit is a particle that moves at constant speed along its own axis, which diffuses in orientation. Synthetic Janus colloids, half coated with platinum and propelled by the decomposition of hydrogen peroxide, are close realizations; swimming bacteria with run-and-tumble motility ([7.6.35](/7.6.35#sec-35.4)) differ in the way they reorient, but behave alike on long scales.

**Definition 37.2.1 (Active Brownian Particle)** An **active Brownian particle** in two dimensions has position $\boldsymbol{r}$ and orientation $\theta$, obeying the overdamped Langevin equations

$$
\dot{\boldsymbol{r}} = v_0\boldsymbol{e}(\theta) + \sqrt{2D_{\mathrm{t}}}\,\boldsymbol{\xi}(t), \qquad \dot\theta = \sqrt{2D_{\mathrm{r}}}\,\eta(t),
\tag{37.2}
$$
with self-propulsion speed $v_0$, $\boldsymbol{e} = (\cos\theta, \sin\theta)$, translational and rotational diffusion coefficients $D_{\mathrm{t}}$ and $D_{\mathrm{r}}$, and independent Gaussian white noises $\boldsymbol{\xi}$, $\eta$ of unit strength. The persistence time is $\tau_{\mathrm{r}} = 1/D_{\mathrm{r}}$ and the persistence length $\ell_{\mathrm{p}} = v_0\tau_{\mathrm{r}}$.

**Theorem 37.2.1 (Mean Squared Displacement of an Active Brownian Particle)** In two dimensions,

$$
\left\langle\lvert\boldsymbol{r}(t) - \boldsymbol{r}(0)\rvert^2\right\rangle = 4D_{\mathrm{t}}t + 2v_0^2\tau_{\mathrm{r}}\left[t - \tau_{\mathrm{r}}\left(1 - \mathrm{e}^{-t/\tau_{\mathrm{r}}}\right)\right] .
\tag{37.3}
$$
For $t \ll \tau_{\mathrm{r}}$ the active part is ballistic, $v_0^2t^2$; for $t \gg \tau_{\mathrm{r}}$ the motion is diffusive with the effective diffusion coefficient

$$
D_{\mathrm{eff}} = D_{\mathrm{t}} + \frac{v_0^2\tau_{\mathrm{r}}}{2} .
\tag{37.4}
$$

**Proof** The orientation performs Brownian motion on the circle, so $\theta(t) - \theta(s)$ is Gaussian with variance $2D_{\mathrm{r}}\lvert t - s\rvert$, and $\langle\boldsymbol{e}(t)\cdot\boldsymbol{e}(s)\rangle = \langle\cos(\theta(t) - \theta(s))\rangle = \mathrm{e}^{-D_{\mathrm{r}}\lvert t - s\rvert}$ (the characteristic function of a Gaussian). The displacement is the sum of the independent active and passive parts; the passive part contributes $4D_{\mathrm{t}}t$, and the active part

$$
v_0^2\int_0^t\!\!\int_0^t\mathrm{e}^{-\lvert s - s'\rvert/\tau_{\mathrm{r}}}\,\mathrm{d}s\,\mathrm{d}s' = 2v_0^2\tau_{\mathrm{r}}\left[t - \tau_{\mathrm{r}}\left(1 - \mathrm{e}^{-t/\tau_{\mathrm{r}}}\right)\right] .
$$
Expanding for small $t$ gives $v_0^2t^2$; for large $t$, $2v_0^2\tau_{\mathrm{r}}t = 4(v_0^2\tau_{\mathrm{r}}/2)t$. $\square$

In three dimensions $\langle\boldsymbol{e}(t)\cdot\boldsymbol{e}(0)\rangle = \mathrm{e}^{-2D_{\mathrm{r}}t}$ and $D_{\mathrm{eff}} = D_{\mathrm{t}} + v_0^2/(6D_{\mathrm{r}})$; for run-and-tumble motion with tumble rate $\lambda$ and uniform reorientation, $D_{\mathrm{eff}} = v_0^2/(3\lambda)$, the persistent random walk of [7.6.5](/7.6.5#sec-5.1.2).

**Example 37.2.1** A Janus colloid of radius $1\,\mu\mathrm{m}$ in water swimming at $v_0 = 5\,\mu\mathrm{m\,s^{-1}}$ has $D_{\mathrm{t}} = k_{\mathrm{B}}T/6\pi\eta a = 0.22\,\mu\mathrm{m^2\,s^{-1}}$ and, by Formula 5.3.2 of [7.6.5](/7.6.5), $D_{\mathrm{r}} = k_{\mathrm{B}}T/8\pi\eta a^3 = 0.16\,\mathrm{s^{-1}}$, so $\tau_{\mathrm{r}} \approx 6\,\mathrm{s}$ and $D_{\mathrm{eff}} \approx 0.22 + 25 \times 6/2 \approx 75\,\mu\mathrm{m^2\,s^{-1}}$ in two dimensions: activity increases the diffusion coefficient three hundredfold. The **Péclet number** $\mathrm{Pe} = v_0a/D_{\mathrm{t}} \approx 23$ compares propulsion with thermal motion. An active particle in a harmonic trap is not distributed as $\mathrm{e}^{-U/k_{\mathrm{B}}T_{\mathrm{eff}}}$ for any temperature when $\ell_{\mathrm{p}}$ exceeds the trap size: it accumulates at the edges, where it pushes against the confining force until it reorients. This failure of an effective temperature is the simplest sign that active systems are not thermal.

![Active Brownian particles in two dimensions (Definition 37.2.1, v₀ = 1, τ_r = 1, D_t = 0.01). A: tracks of four active particles and one passive particle (dark) with the same translational diffusion, each for 20 τ_r. B: mean squared displacement of 500 particles (points) and Eq. (37.3) (line): ballistic for t ≪ τ_r, diffusive with D_eff = D_t + v₀²τ_r/2 for t ≫ τ_r; the dashed line is passive diffusion, two orders of magnitude slower](./plots/abp-msd.py)

## 37.3. Flocking: The Vicsek Model

### 37.3.1. The Model

In 1995 Vicsek and colleagues asked what minimal rule produces the collective motion of flocks, schools and swarms. Earlier computer animations of flocks (Reynolds, 1987) had used three rules: avoid collisions, match the velocity of neighbors, and stay close to them. Vicsek kept only the second, with noise.

**Definition 37.3.1 (Vicsek Model)** The **Vicsek model** consists of $N$ point particles moving at constant speed $v_0$ in a periodic box. At each time step every particle adopts the mean direction of all particles within a distance $R$ (itself included), perturbed by noise, and moves:

$$
\theta_i(t + 1) = \arg\left(\sum_{\lvert\boldsymbol{r}_j - \boldsymbol{r}_i\rvert < R}\mathrm{e}^{\mathrm{i}\theta_j(t)}\right) + \eta\,\xi_i(t), \qquad \boldsymbol{r}_i(t + 1) = \boldsymbol{r}_i(t) + v_0\boldsymbol{e}(\theta_i(t + 1)),
\tag{37.5}
$$
with $\xi_i$ independent and uniform on $[-1/2, 1/2]$. The control parameters are the noise amplitude $\eta$ and the density $\rho$; the order is measured by the polar order parameter $\Psi$ (Definition 37.1.2).

At low noise or high density the particles move collectively, $\Psi$ close to one; at high noise they move independently, $\Psi \approx N^{-1/2}$. In small systems the transition looks continuous, which Vicsek and colleagues interpreted as a critical point. Larger simulations showed that it is discontinuous: near the transition the ordered phase breaks up into dense bands of aligned particles that travel through a disordered gas, and the transition is a liquid–gas-like phase separation in which the bands are the liquid (Grégoire and Chaté, 2004; Solon, Chaté and Tailleur, 2015). The mechanism is a feedback between density and order: alignment is stronger where particles are denser, and ordered particles carry density with them.

![The Vicsek model (Definition 37.3.1; N = 400, box side 10, R = 1, v₀ = 0.3 per step). A, B: snapshots after 800 steps at noise η = 0.5, where the particles move together, and η = 4, where they move independently. C: polar order parameter against noise for N = 100 and 400 at the same density: in such small systems order decreases smoothly with noise; the larger system is more sensitive, the beginning of the discontinuous transition seen in large simulations](./plots/vicsek.py)

### 37.3.2. Correlations in Real Flocks

Measurements of the three-dimensional positions and velocities of thousands of starlings in flocks over Rome (Ballerini and colleagues, 2008; Cavagna and colleagues, 2010) gave two results. Each bird interacts with a fixed number of neighbors, about six or seven, rather than with all birds within a fixed distance: the interaction is topological, which keeps a flock cohesive when its density changes. And the fluctuations of the velocities around the mean, $\delta\boldsymbol{v}_i = \boldsymbol{v}_i - \bar{\boldsymbol{v}}$, are correlated over the whole flock.

**Definition 37.3.2 (Correlation Function and Correlation Length of a Flock)** The connected velocity correlation function of a flock is $C(r) = \langle\delta\boldsymbol{v}_i\cdot\delta\boldsymbol{v}_j\rangle_{r_{ij} \approx r}/\langle\delta\boldsymbol{v}^2\rangle$, the average over pairs of birds at distance $r$; its first zero defines the correlation length $\xi$.

In starling flocks $\xi$ was proportional to the size of the flock, about a third of its linear size, for flocks from $10$ to $100\,\mathrm{m}$ across: the correlations are scale-free. A change of direction of a few birds, for example in response to a predator, can therefore propagate through the whole flock. Scale-free correlations of fluctuations are a property of systems at a critical point, and of systems with a spontaneously broken continuous symmetry, in which the transverse fluctuations of the order parameter are soft modes (Goldstone modes) with no characteristic length. A moving flock is of the second kind; whether flocks are in addition tuned close to a critical point, as some have argued, remains debated. The related idea of self-organized criticality, that driven systems with local rules can evolve by themselves to a critical state, was introduced with the sandpile model of Bak, Tang and Wiesenfeld (1987), in which avalanches of all sizes follow a power law; its relevance to living systems (neuronal avalanches, flocks) is an active and contested field.

## 37.4. Why Walking Beats Pointing

### 37.4.1. The Mermin–Wagner Argument

Consider agents that do not move but align their directions with neighbors in the presence of noise, like spins of a two-dimensional XY magnet. Long-range order would require that all directions agree over arbitrarily large distances.

**Definition 37.4.1 (Mermin–Wagner Theorem)** The **Mermin–Wagner theorem** states that in thermal equilibrium at nonzero temperature, a continuous symmetry cannot be spontaneously broken in dimensions $d \le 2$ by a system with short-range interactions (Mermin and Wagner, 1966; Hohenberg, 1967).

The reason can be seen from a calculation with the small fluctuations of the angle.

**Theorem 37.4.1 (Angular Fluctuations of Fixed Aligning Agents)** Let small deviations $\theta(\boldsymbol{x}, t)$ of the direction from the mean obey the noisy diffusion equation $\partial_t\theta = K\nabla^2\theta + \zeta$, with white noise $\langle\zeta(\boldsymbol{x}, t)\zeta(\boldsymbol{x}', t')\rangle = 2\Gamma\delta(\boldsymbol{x} - \boldsymbol{x}')\delta(t - t')$, in a two-dimensional system of size $L$ and microscopic cutoff $a$. In the stationary state

$$
\langle\theta^2\rangle = \frac{\Gamma}{2\pi K}\ln\frac La ,
\tag{37.6}
$$
which diverges with the system size, so the polar order $\langle\cos\theta\rangle \approx \mathrm{e}^{-\langle\theta^2\rangle/2} = (a/L)^{\Gamma/4\pi K}$ vanishes for $L \to \infty$.

**Proof** In Fourier space each mode is an Ornstein–Uhlenbeck process ([7.6.5](/7.6.5#sec-5.4.2)), $\partial_t\theta_{\boldsymbol{q}} = -Kq^2\theta_{\boldsymbol{q}} + \zeta_{\boldsymbol{q}}$, with stationary variance $\langle\lvert\theta_{\boldsymbol{q}}\rvert^2\rangle = \Gamma/(Kq^2)$ per unit area. Summing over modes, $\langle\theta^2\rangle = \int\frac{\mathrm{d}^2q}{(2\pi)^2}\frac{\Gamma}{Kq^2} = \frac{\Gamma}{2\pi K}\int_{2\pi/L}^{2\pi/a}\frac{\mathrm{d}q}{q} = \frac{\Gamma}{2\pi K}\ln\frac La$. For Gaussian $\theta$, $\langle\cos\theta\rangle = \mathrm{e}^{-\langle\theta^2\rangle/2}$. $\square$

In $d$ dimensions the integral is $\int q^{d-3}\,\mathrm{d}q$, which converges at small $q$ for $d > 2$: in three dimensions, fixed aligning agents order. The divergence comes from long-wavelength modes, slow rotations of large regions, which cost little alignment because neighbors still agree locally. In equilibrium $\Gamma/K = k_{\mathrm{B}}T/J$, the ratio of temperature to coupling. A counting argument gives the same result: an agent's angle accumulates noise of variance $\propto t$, and information spreads diffusively, so after time $t$ the error has been averaged over the $N(t) \propto t^{d/2}$ agents within distance $\sqrt t$; the residual variance $t/N(t) \propto t^{1 - d/2}$ grows without bound for $d < 2$ and logarithmically for $d = 2$.

### 37.4.2. Toner–Tu Theory

Vicsek's agents order in two dimensions, so motion must change the argument. Toner and Tu (1995, 1998) wrote down the most general hydrodynamic equations for the density $\rho(\boldsymbol{x}, t)$ and the coarse-grained velocity $\boldsymbol{v}(\boldsymbol{x}, t)$ of a polar active fluid consistent with its symmetries: rotational invariance, conservation of the number of agents, and no Galilean invariance (the agents move relative to a medium or substrate that defines a frame).

**Definition 37.4.2 (Toner–Tu Equations)** The **Toner–Tu theory** describes a flock by the equations

$$
\partial_t\rho + \nabla\cdot(\rho\boldsymbol{v}) = 0, \qquad \partial_t\boldsymbol{v} + \lambda_1(\boldsymbol{v}\cdot\nabla)\boldsymbol{v} = \alpha\boldsymbol{v} - \beta\lvert\boldsymbol{v}\rvert^2\boldsymbol{v} - \nabla P(\rho) + D_{\mathrm{v}}\nabla^2\boldsymbol{v} + \dots + \boldsymbol{f},
\tag{37.7}
$$
with a pressure $P(\rho)$, viscosity-like terms (only the simplest is shown), noise $\boldsymbol{f}$, and coefficients $\alpha$ and $\beta > 0$ that set a preferred speed $\lvert\boldsymbol{v}\rvert = \sqrt{\alpha/\beta}$ in the ordered phase ($\alpha > 0$). The coefficient $\lambda_1$ of the convective term is not fixed at $1$ because the flock moves relative to a medium.

The equations resemble the Navier–Stokes equations ([7.6.22](/7.6.22)) with an active term $\alpha\boldsymbol{v} - \beta\lvert\boldsymbol{v}\rvert^2\boldsymbol{v}$ that makes a nonzero speed the preferred state, like the Landau free energy of a ferromagnet below its critical temperature; maintaining it requires a constant input of energy.

The key effect is the coupling between orientation and motion. A fluctuation $\delta\theta$ of direction produces a velocity component $v_0\delta\theta$ perpendicular to the mean motion, which carries agents sideways. Information about direction therefore spreads perpendicular to the motion not by diffusion but by advection, faster than $\sqrt t$, and each agent's direction is averaged with many more neighbors than in the fixed case. A heuristic version of Toner's argument estimates the exponents. Let $w(t)$ be the lateral distance (perpendicular to the mean velocity) over which agents have exchanged information after time $t$, and $\ell_\parallel \propto \sqrt t$ the distance along the mean velocity, where transport is still diffusive. The variance of an agent's angle is the accumulated noise, $\propto t$, averaged over the $\ell_\parallel w^{d-1}$ agents in this region:

$$
\langle\delta\theta^2\rangle \propto \frac{t}{\sqrt t\,w^{d-1}} = \sqrt t\,w^{1-d} .
$$
Lateral spreading is driven by the lateral velocity fluctuations, $w \propto v_0\langle\delta\theta^2\rangle^{1/2}t$. Combining the two, $w^{(d+1)/2} \propto t^{5/4}$, so $w \propto t^{5/(2(d+1))}$, and in two dimensions $w \propto t^{5/6}$, superdiffusive, and $\langle\delta\theta^2\rangle \propto t^{1/2 - 5/6} = t^{-1/3} \to 0$: the angular fluctuations decrease as larger regions are averaged, and long-range polar order exists in two dimensions. Toner and Tu obtained the same exponents from a renormalization-group calculation, which they believed exact in $d = 2$; later work showed that additional nonlinearities spoil the exactness, and simulations give slightly different exponents (Toner, 2012; Mahault, Ginelli and Chaté, 2019), but the conclusion stands.

The simulation in the figure applies the same alignment rule to agents fixed on a lattice and to moving agents at equal noise and equal numbers of neighbors: order decays steadily with system size in the first case and persists in the second. Moving flocks also show giant number fluctuations: the standard deviation of the number of agents in a region grows faster than $\sqrt{\bar N}$, as $\bar N^{0.8}$ in two-dimensional flocks and in bacterial swarms (Zhang, Be'er, Florin and Swinney, 2010), because density is advected by the soft orientational modes.

![Why walking beats pointing. The same alignment rule (mean direction of neighbors within distance 1, plus noise uniform on [−η/2, η/2] with η = 2.8) applied to agents fixed on a square lattice (four nearest neighbors) and to agents moving at speed 2 in the direction they point (the Vicsek model at density 1.6, a similar number of neighbors). A: polar order parameter in the stationary state against the number of agents: for fixed agents it decreases with system size, as Theorem 37.4.1 predicts; for moving agents it stays nearly constant. B: directions of fixed agents on a 48 × 48 lattice (cyclic colour scale): patches of similar direction that wander, on a background of strong local noise](./plots/walking-vs-pointing.py)

## 37.5. Motility-Induced Phase Separation

### 37.5.1. Phase Separation Without Attraction

In equilibrium, a fluid separates into dense and dilute phases only if its particles attract: in the regular-solution or Flory–Huggins free energy, the mixing entropy competes with an interaction energy, and the uniform state becomes unstable inside the spinodal, where $\partial^2f/\partial\phi^2 < 0$ (**spinodal decomposition**, [7.2.21](/7.2.21), [7.6.29](/7.6.29)). Active particles can phase-separate with purely repulsive interactions. If particles slow down where they are crowded, because they collide with each other or because they sense the local density (quorum sensing), they accumulate where they are slow; accumulation slows them further. This positive feedback is enough.

**Definition 37.5.1 (Motility-Induced Phase Separation)** **Motility-induced phase separation** is the separation of self-propelled particles without attractive interactions into a dense and a dilute phase, caused by a decrease of the propulsion speed with local density.

**Theorem 37.5.1 (Instability Criterion of Motility-Induced Phase Separation)** Let active Brownian particles in two dimensions have a speed $v(\rho)$ that depends on the local density and negligible translational diffusion. On scales large compared with the persistence length, the density obeys

$$
\partial_t\rho = \nabla\cdot\left[\frac{v(\rho)}{2D_{\mathrm{r}}}\nabla\bigl(v(\rho)\rho\bigr)\right] ,
\tag{37.8}
$$
and the uniform state of density $\rho_0$ is unstable if and only if

$$
\frac{v'(\rho_0)}{v(\rho_0)} < -\frac{1}{\rho_0}, \quad\text{that is}\quad \frac{\mathrm{d}(\rho v)}{\mathrm{d}\rho}\bigg|_{\rho_0} < 0 .
\tag{37.9}
$$

**Proof** Equation (37.8) is obtained from the Fokker–Planck equation for $P(\boldsymbol{r}, \theta, t)$, $\partial_tP = -\nabla\cdot[v\boldsymbol{e}(\theta)P] + D_{\mathrm{r}}\partial_\theta^2P$, by expanding $P$ in angular harmonics: the density $\rho$ is the zeroth harmonic and the polarization $\boldsymbol{p} = \int\boldsymbol{e}P\,\mathrm{d}\theta$ the first, which relaxes at rate $D_{\mathrm{r}}$ to $\boldsymbol{p} \approx -\nabla(v\rho)/(2D_{\mathrm{r}})$ on long time scales (higher harmonics neglected); inserting this into $\partial_t\rho = -\nabla\cdot(v\boldsymbol{p})$ gives Eq. (37.8) (Tailleur and Cates, 2008; Cates and Tailleur, 2015). We take it as given. Linearizing about $\rho_0$, $\nabla(v\rho) = (v + \rho v')\nabla\delta\rho$, so $\partial_t\delta\rho = D_{\mathrm{eff}}\nabla^2\delta\rho$ with $D_{\mathrm{eff}} = v(v + \rho_0v')/(2D_{\mathrm{r}})$. A negative diffusion coefficient makes every mode $\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{x}}$ grow at rate $\lvert D_{\mathrm{eff}}\rvert q^2$; since $v > 0$, this happens exactly when $v + \rho_0v' < 0$. $\square$

The condition is the analog of a spinodal: the quantity $\ln(\rho v(\rho))$ plays the role of a chemical potential, and the dense and dilute coexisting densities can be computed by an analog of the common-tangent construction (with corrections that make the active binodals differ from the equilibrium ones; Solon and colleagues, 2018). For colliding particles without quorum sensing, $v(\rho) \approx v_0(1 - \rho/\rho^*)$ for some jamming density $\rho^*$, and the instability sets in at $\rho_0 > \rho^*/2$ when the persistence length is long enough (Péclet numbers above about $50$ in simulations of repulsive disks; Fily and Marchetti, 2012).

![Motility-induced phase separation of active Brownian particles with density-dependent speed v(ρ) = v₀ exp(−ρ/ρ*) and no attraction (2000 particles, box side 40, v₀ = 1, D_r = 0.05, density counted within radius 2; snapshots after 100 rotational times). A: ρ₀/ρ* = 0.6: the suspension stays homogeneous. B: ρ₀/ρ* = 2: dense, slow clusters form spontaneously and coarsen in a dilute, fast gas. C: the effective diffusion coefficient D_eff = v(v + ρv′)/(2D_r) of Theorem 37.5.1, negative (shaded) for ρ > ρ*, where v′/v < −1/ρ; the dots mark the densities of A and B](./plots/mips.py)

### 37.5.2. Biological Examples

Motility-induced aggregation has been engineered in bacteria. Liu and colleagues (2011) built *E. coli* that secrete a small signaling molecule and reduce their motility when its concentration is high; growing colonies of such cells formed periodic stripes of high density, as the theory predicts for density-dependent motility coupled to growth (Fu and colleagues, 2012). In the soil bacterium *Myxococcus xanthus*, which glides on surfaces, starvation triggers aggregation into fruiting bodies, and tracking of single cells showed that the aggregation follows from changes in the cells' speed and reversal frequency as a motility-induced phase separation, without chemotaxis (Liu and colleagues, 2019). The aggregation of starving *Dictyostelium*, in contrast, is driven by chemotaxis to cAMP ([7.5.13](/7.5.13)).

## 37.6. Active Nematics and Active Gels

### 37.6.1. Active Stress

A suspension of microtubule bundles cross-linked by clusters of kinesin motors, supplied with ATP, slides adjacent bundles past each other and extends them along their length (Sanchez, Chen, DeCamp, Heymann and Dogic, 2012). When it is confined to an oil–water interface, it forms a two-dimensional nematic that never comes to rest: bundles bend, buckle and fracture, pairs of $\pm1/2$ defects are created continuously, the $+1/2$ defects swim through the layer, and defects annihilate in pairs. The flow is chaotic, a state called active turbulence, although the Reynolds number is tiny.

**Definition 37.6.1 (Active Nematic)** An **active nematic** is a nematic liquid crystal whose units exert force dipoles on the surrounding medium, producing an active stress proportional to the nematic order parameter, $\sigma^{\mathrm{a}}_{\alpha\beta} = -\zeta Q_{\alpha\beta}$; it is extensile for $\zeta > 0$ (units push fluid out along their axis, as microtubule–kinesin bundles and pusher bacteria do) and contractile for $\zeta < 0$ (actomyosin).

Two consequences of the active stress follow from its form. First, a uniform aligned state exerts no force, because the force density is $\boldsymbol{f} = \nabla\cdot\sigma^{\mathrm{a}} = -\zeta\nabla\cdot Q$, but any distortion of the director produces a force and hence flow. For an extensile nematic, the flow produced by a bend amplifies the bend; for a contractile one, splay is amplified. Simha and Ramaswamy (2002) showed that in a bulk fluid without friction the aligned state of an active nematic is unstable at arbitrarily small activity, the generic instability of active liquid crystals. Elasticity stabilizes short wavelengths: comparing the active stress $\zeta$ with the elastic stress $K/\ell^2$ (with $K$ the Frank constant) defines the active length

$$
\ell_{\mathrm{a}} = \sqrt{K/\lvert\zeta\rvert} ,
$$
which sets the size of vortices and the spacing of defects in active turbulence, typically tens of micrometers in microtubule–kinesin layers and increasing as the ATP concentration, and with it the activity, is lowered.

Second, the defects acquire motion. The flow around a $+1/2$ defect is asymmetric because the defect is: the active force at its core points along its symmetry axis, and the defect self-propels, toward its head in extensile and toward its tail in contractile systems. The three-fold symmetric $-1/2$ defect experiences no net active force and moves only by being pushed or attracted. Active nematics are thus fluids of self-propelled $+1/2$ and passive $-1/2$ quasi-particles, created and annihilated in pairs.

### 37.6.2. Defects in Cells and Tissues

Monolayers of elongated cells are nematics. In epithelial monolayers (MDCK cells), cells are extruded preferentially at $+1/2$ defects, where the compressive stress is concentrated (Saw and colleagues, 2017); in cultures of neural progenitor cells, cells accumulate at $+1/2$ defects and leave $-1/2$ defects, forming mounds (Kawaguchi, Kageyama and Sano, 2017). In regenerating *Hydra*, the nematic order of the supracellular actomyosin fibers carries defects whose positions predict where the head and the foot will form, the organizing centers of the body plan (Maroudas-Sacks and colleagues, 2021). The actomyosin cortex of cells is a contractile active gel, whose gradients of contractility drive cortical flows that polarize the *Caenorhabditis elegans* zygote ([7.6.36](/7.6.36#sec-36.4.2)) and shape tissues during gastrulation and convergent extension ([7.5.8](/7.5.8#sec-8.9)).

## 37.7. Active Matter in Bacteria and Tissues

### 37.7.1. Bacterial Turbulence

Dense suspensions of swimming bacteria such as *Bacillus subtilis*, at volume fractions of about $10\,\%$ and more, form jets and vortices whose size, tens of micrometers, is independent of the size of the container and much larger than a bacterium (Dombrowski and colleagues, 2004; Wensink and colleagues, 2012). The flows mix the suspension and increase the transport of oxygen and nutrients. Bacteria are pushers ([7.6.22](/7.6.22)), whose far-field flow is that of an extensile force dipole, so a suspension of aligned bacteria is an active nematic with polar units; the hydrodynamic interactions between swimmers, long-ranged at low Reynolds number, drive the instability. Confining the suspension stabilizes it: in a circular well of about $70\,\mu\mathrm{m}$ diameter, bacteria organize into a single stable vortex, with a counter-rotating boundary layer near the wall (Wioland and colleagues, 2013).

### 37.7.2. Cells in Tissues: Flowing and Jamming

Epithelial monolayers migrate collectively during wound closure and development, with cells moving at about $10$–$50\,\mu\mathrm{m\,h^{-1}}$, in swirls spanning many cells and with traction forces transmitted across the sheet over distances of many cell diameters ([7.6.31](/7.6.31)). As density increases, the motion slows and becomes dynamically heterogeneous, like a supercooled liquid approaching a glass, and eventually arrests (Angelini and colleagues, 2011). Packings of frictionless hard particles jam when their packing fraction reaches about $0.84$ in two dimensions and $0.64$ in three; in confluent tissues, where there are no gaps, a different control parameter applies. In the vertex model of a tissue ([7.5.8](/7.5.8#sec-8.10)), with energy $E = \sum_i[K_A(A_i - A_0)^2 + K_P(P_i - P_0)^2]$ for cell areas $A_i$ and perimeters $P_i$, the tissue is solid when the target shape index $p_0 = P_0/\sqrt{A_0}$ is below about $3.81$ and fluid above it, independently of density (Bi, Lopez, Schwarz and Manning, 2015). Adding self-propulsion of cells, as in self-propelled Voronoi models, makes the tissue fluid at lower $p_0$, so that motility and cell shape together set the state of the tissue. The prediction that the average observed cell shape index is close to $3.81$ at the transition was confirmed in airway epithelia from asthmatic and non-asthmatic donors, which unjam when compressed (Park and colleagues, 2015). The physics of how tissues flow and freeze during development is treated in [7.5.8](/7.5.8#sec-8.10).

## Summary

| System | Key result | Where |
|---|---|---|
| Order parameters | polar $\Psi = \lvert\langle\boldsymbol{e}\rangle\rvert$; nematic $Q = \frac S2(2\boldsymbol{n}\boldsymbol{n} - I)$; defects of charge $\pm1/2$ in nematics | Definitions 37.1.1–37.1.3 |
| Active Brownian particle | MSD ballistic then diffusive, $D_{\mathrm{eff}} = D_{\mathrm{t}} + v_0^2\tau_{\mathrm{r}}/2$ (2D) | Definition 37.2.1, Theorem 37.2.1 |
| Vicsek model | alignment with noise; order–disorder transition, discontinuous with traveling bands | Definition 37.3.1 |
| Flocks | topological interactions; scale-free velocity correlations, $\xi \propto$ flock size | Definition 37.3.2 |
| Fixed agents | $\langle\theta^2\rangle = (\Gamma/2\pi K)\ln(L/a)$: no long-range order in 2D | Definition 37.4.1, Theorem 37.4.1 |
| Moving agents | Toner–Tu: lateral spreading $w \propto t^{5/6}$, $\langle\delta\theta^2\rangle \propto t^{-1/3}$: long-range order in 2D; giant number fluctuations | Definition 37.4.2 |
| MIPS | $\partial_t\rho = \nabla\cdot[(v/2D_{\mathrm{r}})\nabla(v\rho)]$; unstable when $(\rho v)' < 0$ | Definition 37.5.1, Theorem 37.5.1 |
| Active nematics | active stress $-\zeta Q$; generic instability; active length $\sqrt{K/\lvert\zeta\rvert}$; self-propelled $+1/2$ defects | Definition 37.6.1 |
| Tissues | rigidity transition of the vertex model at $p_0 \approx 3.81$; motility fluidizes; extrusion at $+1/2$ defects | 37.6.2, 37.7.2 |

- Energy injected at the scale of each unit breaks detailed balance locally; active systems therefore have no effective temperature in general, and equilibrium theorems (Mermin–Wagner, the need for attraction to phase-separate) do not constrain them.
- Coupling of orientation to motion (flocks), of speed to density (MIPS) and of stress to orientation (active nematics) are the three basic feedbacks, and each produces a characteristic new phenomenon.

## Questions

1. Show that the polar order parameter of $N$ agents with independent, uniformly distributed directions has $\langle\Psi^2\rangle = 1/N$. Why must the order parameter in a simulation be compared at several system sizes before concluding that a phase is ordered?

   **Answer** $\Psi^2 = N^{-2}\sum_{i,j}\boldsymbol{e}_i\cdot\boldsymbol{e}_j$; the cross terms average to zero and the $N$ diagonal terms are $1$, so $\langle\Psi^2\rangle = N/N^2 = 1/N$. A disordered finite system therefore has $\Psi \sim N^{-1/2}$, not zero, and a system with quasi-long-range order (Theorem 37.4.1) has $\Psi \sim N^{-\eta}$ with a small exponent, which looks ordered at any fixed size. Only the dependence on $N$ distinguishes true order ($\Psi$ tends to a nonzero constant), quasi-order (slow power law) and disorder ($N^{-1/2}$).

2. *E. coli* swims at $25\,\mu\mathrm{m\,s^{-1}}$ with runs of $1\,\mathrm{s}$ and reorients randomly at each tumble. Compute its diffusion coefficient in three dimensions and the time after which its motion becomes diffusive, and compare with the Brownian diffusion of a $1\,\mu\mathrm{m}$ particle.

   **Answer** For run-and-tumble with uniform reorientation, $D_{\mathrm{eff}} = v_0^2/(3\lambda) = 625/3 \approx 210\,\mu\mathrm{m^2\,s^{-1}}$; the crossover from ballistic to diffusive is at $t \approx 1/\lambda = 1\,\mathrm{s}$ (a few seconds if the mean turning angle of $68^\circ$ is included, which raises $D_{\mathrm{eff}}$ by $1/(1 - \cos 68^\circ) \approx 1.6$). A passive $1\,\mu\mathrm{m}$ sphere has $D = k_{\mathrm{B}}T/(6\pi\eta a) \approx 0.4\,\mu\mathrm{m^2\,s^{-1}}$ (radius $0.5\,\mu\mathrm{m}$), so swimming increases diffusion about $500$-fold.

3. In Theorem 37.4.1, estimate $\langle\cos\theta\rangle$ for a lattice of $10^3 \times 10^3$ agents and of $10^6 \times 10^6$ agents if $\Gamma/K = 0.5$. Why do two-dimensional magnets nevertheless appear ordered in experiments?

   **Answer** The exponent is $\Gamma/(4\pi K) = 0.040$; $(a/L)^{0.040} = (10^{-3})^{0.04} = 0.76$ and $(10^{-6})^{0.04} = 0.58$. Order decays, but extremely slowly: a two-dimensional system of macroscopic size retains substantial order at low noise. Real two-dimensional magnets also have weak anisotropies and interlayer couplings that break the continuous symmetry and allow true order, and the logarithm makes finite sizes matter little. The Mermin–Wagner theorem is a statement about the limit $L \to \infty$.

4. Derive Eq. (37.9) for the speed law $v(\rho) = v_0(1 - \rho/\rho^*)$ and find the spinodal density. What happens to the dense phase as $\rho \to \rho^*$?

   **Answer** $v + \rho v' = v_0(1 - \rho/\rho^*) - v_0\rho/\rho^* = v_0(1 - 2\rho/\rho^*)$, negative for $\rho > \rho^*/2$: the spinodal is at $\rho^*/2$. As density approaches $\rho^*$ the particles stop, so the dense phase is an arrested cluster whose boundary exchanges particles with the gas: particles arriving from the gas are trapped until they rotate away, at rate $D_{\mathrm{r}}$. The cluster size is set by the balance of arrival (proportional to the gas density and $v_0$) and escape (proportional to $D_{\mathrm{r}}$ and the perimeter).

5. A bacterial suspension forms vortices of $50\,\mu\mathrm{m}$ at a given concentration. If the activity (swimming speed times density) is doubled at constant elasticity, how should the vortex size change according to the active length? Propose an experiment.

   **Answer** $\ell_{\mathrm{a}} = \sqrt{K/\lvert\zeta\rvert}$, so doubling $\zeta$ reduces it by $\sqrt2$, to about $35\,\mu\mathrm{m}$. In practice the speed of bacteria can be varied by oxygen (they stop when oxygen is exhausted) or with light-powered swimmers (*E. coli* expressing proteorhodopsin), and the vortex size measured by particle image velocimetry as the correlation length of the velocity field. For bacteria, measurements suggest that the vortex size depends only weakly on activity (Wensink and colleagues, 2012), which indicates that the length is set partly by the length and steric interactions of the bacteria, not by the active–elastic balance alone; the experiment tests which picture applies.

6. Explain why a $+1/2$ defect in an extensile active nematic moves, while a $-1/2$ defect does not, using the symmetry of the director field.

   **Answer** The active force density is $\boldsymbol{f} = -\zeta\nabla\cdot Q$. For $\varphi = k\theta$, the director field of a $+1/2$ defect has one mirror axis (the comet's axis); averaging $\nabla\cdot Q$ over a region around the core gives a vector along this axis, so the active force has a net component along it and drives the defect (and the fluid) in that direction. The $-1/2$ defect has three-fold rotational symmetry; any vector averaged over a three-fold symmetric configuration vanishes, so there is no net self-propulsion. The direction of motion of the $+1/2$ defect reverses with the sign of $\zeta$.

7. A starling flock of $1000$ birds is $40\,\mathrm{m}$ across with a correlation length of $12\,\mathrm{m}$, and a second flock of $8000$ birds at the same density is $80\,\mathrm{m}$ across. If correlations are scale-free, what correlation length do you expect for the second flock, and what would you expect if they had a fixed range?

   **Answer** Scale-free correlations give $\xi \propto L$: $\xi \approx 12 \times 80/40 = 24\,\mathrm{m}$. With a fixed range, $\xi$ would stay at $12\,\mathrm{m}$, independent of flock size. Cavagna and colleagues found the first behavior: $\xi$ was about one third of the flock size over a tenfold range of sizes.

8. Show that the vertex-model energy is minimized for a regular hexagon when $p_0$ equals the shape index of a regular hexagon, and compute that value. Why is a tissue with $p_0 = 3.9$ fluid?

   **Answer** A regular hexagon of area $A$ has side $s$ with $A = (3\sqrt3/2)s^2$ and perimeter $6s$, so $P/\sqrt A = 6/\sqrt{3\sqrt3/2} = 3.72$. If $p_0 < 3.72$ (and $A = A_0$), cells cannot reach their target perimeter and are under tension; the network resists shear, a solid. As $p_0$ increases past about $3.81$ (the value found in simulations of disordered networks, larger than for a perfect hexagon because of disorder), cells can reach their target perimeters in many shapes, the energy barriers to neighbor exchanges (T1 transitions) vanish, and the tissue flows. At $p_0 = 3.9$ there is a continuum of zero-energy deformations, so the tissue cannot sustain a shear stress: it is fluid.

9. (Open) Is a flock of birds "active matter" in the same sense as a microtubule–kinesin layer? Discuss what is gained and lost by modeling animals as self-propelled particles.

   **Answer** Both consist of units that convert energy into motion and interact locally, so the hydrodynamic theory based on symmetries and conservation laws (Toner–Tu) applies to both on large scales, and its predictions (long-range order in two dimensions, giant number fluctuations, propagation of orientational waves) do not depend on microscopic details; this universality is the gain. Lost are the cognitive and evolutionary aspects: birds use vision with a finite number of neighbors (topological interactions), anticipate, have inertia that matters for turning waves, and their rules were shaped by predation. Microscopic models must then include these, and some properties (the speed of information transfer during turns, measured by Attanasi and colleagues, 2014) require extending the theory with inertial spin dynamics. The modeling question is which features of the collective behavior are universal and which reflect the biology of the individuals ([7.18](/7.18)).
