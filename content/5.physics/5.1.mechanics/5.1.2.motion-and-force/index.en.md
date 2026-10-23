---
title: Motion and Force
description: Newton's laws of motion and inertial frames; the defining constants of the 2019 SI and dimensional analysis; common forces and the four fundamental interactions; applications of Newton's laws; inertial forces in translating and rotating non-inertial frames, the equivalence principle, tides, the centrifugal force and the Coriolis force.
source_hash: c9fbf921cf82
---

The previous chapter, [5.1.1](/5.1.1), only described motion; this chapter discusses the causes of changes in motion. *Dynamics* studies how the interactions (forces) between bodies determine the **acceleration** of a body. Newton's laws of motion are the foundation of classical mechanics, and the momentum theorem ([5.1.3](/5.1.3)), the work-energy theorem and energy conservation ([5.1.4](/5.1.4)), and the law of rotation of rigid bodies ([5.1.5](/5.1.5)) in the following chapters are all consequences of them. We first state the three laws and the concept of an inertial frame, then introduce the International System of Units and dimensions, the common forces and the four fundamental interactions, and use worked examples to show the general procedure for solving problems with Newton's laws; the equations one writes down are often a **differential equation** ([2.2.15](/2.2.15)), which can be solved analytically or numerically ([4.4.4](/4.4.4)). Finally we discuss non-inertial frames: in an accelerating or rotating **reference frame** we introduce inertial forces so that Newton's laws can still be used, which explains weightlessness, the tides, the variation of gravity with latitude, and the many phenomena of the Coriolis force.

## 2.1. Newton's Laws of Motion

**Theorem 2.1.1 (Newton's First Law)** Every body remains at rest or in uniform rectilinear motion until the action of other bodies forces it to change that state.

The first law is also called the law of inertia. The property of a body to keep its state of motion is called inertia; the first law states qualitatively that force is the cause of changes in the state of motion, not the cause of its maintenance. It also specifies the reference frames in which the laws apply:

**Definition 2.1.1 (Inertial Frame)** A reference frame in which Newton's first law holds is called an **inertial frame**. A reference frame moving with constant velocity relative to an inertial frame is also an inertial frame; a reference frame accelerating relative to an inertial frame is called a **non-inertial frame**.

**Theorem 2.1.2 (Newton's Second Law)** The net external force on a body equals the rate of change of its momentum:

$$
\boldsymbol{F} = \frac{\mathrm{d}(m\boldsymbol{v})}{\mathrm{d}t}.
$$
For constant mass $m$, $\boldsymbol{F} = m\boldsymbol{a}$.

Here $m\boldsymbol{v}$ is the momentum of the body ([5.1.3](/5.1.3)).

**Definition 2.1.2 (Inertial Mass)** The mass $m$ in the second law measures the inertia of a body (under the same force, the larger the mass, the smaller the acceleration) and is called the **inertial mass**.

**Theorem 2.1.3 (Newton's Third Law)** The action and reaction forces between two bodies are equal in magnitude and opposite in direction, and act along the same line:

$$
\boldsymbol{F}_{12} = -\boldsymbol{F}_{21},
$$
where $\boldsymbol{F}_{12}$ is the force exerted by body 2 on body 1.

The action and reaction forces act on two different bodies and cannot cancel each other; they appear simultaneously and are of the same nature (both gravitational, both elastic, or both frictional).

Some remarks on Newton's laws:

1. Newton's laws hold only in inertial frames; when they are used in a non-inertial frame, inertial forces must be introduced (Section 2.6).
2. The laws apply to a **particle**. A general body can be regarded as a collection of particles (a system of particles); applying Newton's laws to each particle and summing gives the laws for systems of particles and rigid bodies ([5.1.3](/5.1.3), [5.1.5](/5.1.5)), which is why Newton's laws have universal significance.
3. The laws apply to the low-speed motion of macroscopic bodies in weak gravitational fields. When the **speed** approaches the speed of light, special relativity is needed ([5.1.8](/5.1.8)): the form $\boldsymbol{F} = \mathrm{d}\boldsymbol{p}/\mathrm{d}t$ of the second law is kept, but the momentum is no longer $m\boldsymbol{v}$ and $\boldsymbol{F} = m\boldsymbol{a}$ no longer holds; microscopic particles require quantum mechanics ([5.5](/5.5)).
4. The third law holds strictly for contact forces; for interactions transmitted through fields (such as the electromagnetic force between moving charges), the two forces may not be strictly equal and opposite, in which case it is the total momentum of the bodies and the field that is conserved ([5.3](/5.3)).

The three laws above are together called *Newton's laws of motion*.

## 2.2. SI Units and Dimensions

### 2.2.1. The International System of Units

The numerical value of a physical quantity depends on the unit chosen. The International System of Units (SI) selects seven base units, from which all other units are derived. Since 20 May 2019, the SI no longer defines units by material standards (such as the International Prototype of the Kilogram kept in Paris); instead it fixes seven physical constants at exact values, and all units are derived from these defining constants:

| Defining constant | Exact value | Main unit defined |
|---|---|---|
| Hyperfine transition frequency of the $^{133}\mathrm{Cs}$ ground state $\Delta\nu_{\mathrm{Cs}}$ | $9\,192\,631\,770\,\mathrm{Hz}$ | second $\mathrm{s}$ |
| Speed of light in vacuum $c$ | $299\,792\,458\,\mathrm{m\,s^{-1}}$ | meter $\mathrm{m}$ |
| Planck constant $h$ | $6.626\,070\,15\times10^{-34}\,\mathrm{J\,s}$ | kilogram $\mathrm{kg}$ |
| Elementary charge $e$ | $1.602\,176\,634\times10^{-19}\,\mathrm{C}$ | ampere $\mathrm{A}$ |
| Boltzmann constant $k_{\mathrm{B}}$ | $1.380\,649\times10^{-23}\,\mathrm{J\,K^{-1}}$ | kelvin $\mathrm{K}$ |
| Avogadro constant $N_{\mathrm{A}}$ | $6.022\,140\,76\times10^{23}\,\mathrm{mol^{-1}}$ | mole $\mathrm{mol}$ |
| Luminous efficacy $K_{\mathrm{cd}}$ of monochromatic radiation of frequency $540\times10^{12}\,\mathrm{Hz}$ | $683\,\mathrm{lm\,W^{-1}}$ | candela $\mathrm{cd}$ |

The three base units of mechanics are therefore: $1\,\mathrm{s}$ is $9\,192\,631\,770$ periods of the radiation corresponding to the hyperfine transition of the $^{133}\mathrm{Cs}$ ground state; $1\,\mathrm{m}$ is the distance light travels in vacuum in $1/299\,792\,458\,\mathrm{s}$; the kilogram is fixed by the numerical value of $h$ ($\mathrm{J\,s} = \mathrm{kg\,m^2\,s^{-1}}$) together with the definitions of the second and the meter, and is realized in practice with devices such as the Kibble balance. The constants $k_{\mathrm{B}}$, $e$ and $N_{\mathrm{A}}$ used in thermodynamics and electromagnetism are likewise exact ([5.2.1](/5.2.1), [5.3.1](/5.3.1)).

### 2.2.2. Dimensions

**Definition 2.2.1 (Dimension of a Quantity)** Disregarding numerical factors, the expression of a physical quantity $Q$ as a product of powers of the base quantities is called the **dimension of a quantity** $Q$, written $\dim Q$. The base quantities in mechanics are length, mass and time, with dimensions written $\mathsf{L}$, $\mathsf{M}$, $\mathsf{T}$:

$$
\dim Q = \mathsf{L}^{\alpha}\,\mathsf{M}^{\beta}\,\mathsf{T}^{\gamma}.
$$
A quantity all of whose exponents are zero is called a dimensionless quantity (a quantity of dimension one), $\dim Q = 1$.

For example, $\dim v = \mathsf{L}\,\mathsf{T}^{-1}$ and $\dim F = \mathsf{L}\,\mathsf{M}\,\mathsf{T}^{-2}$. The seven base dimensions of the SI are $\mathsf{L}, \mathsf{M}, \mathsf{T}, \mathsf{I}, \Theta, \mathsf{N}, \mathsf{J}$ (length, mass, time, electric current, thermodynamic temperature, amount of substance, luminous intensity). Textbooks often write the dimension as $[Q]$; this site follows ISO 80000-1 and writes $\dim Q$.

The basic use of dimensions is to check equations: only quantities of the same dimension can be added, subtracted or equated, and the arguments of exponential, trigonometric and logarithmic functions must be dimensionless. This also allows dimensional analysis, which yields the form of relations between physical quantities without solving any equation.

**Example 2.2.1** The period $T$ of a simple pendulum may depend on the length $l$, the mass $m$ of the bob and the gravitational acceleration $g$. Set $T = C\,l^{a}m^{b}g^{c}$ ($C$ is a dimensionless constant) and compare dimensions: $\mathsf{T} = \mathsf{L}^{a + c}\,\mathsf{M}^{b}\,\mathsf{T}^{-2c}$, which gives $b = 0$, $c = -\frac12$, $a = \frac12$, that is,

$$
T = C\sqrt{\frac{l}{g}}.
$$
The period is independent of the mass. The constant $C = 2\pi$ (for small amplitudes) must be found from dynamics ([5.1.6](/5.1.6)); dimensional analysis also cannot tell whether the period depends on the dimensionless amplitude angle.

## 2.3. Some Common Forces

1. Gravity: the weight of a body of mass $m$ near the Earth's surface is $m\boldsymbol{g}$. Strictly speaking, it is the resultant of the Earth's gravitational attraction and the centrifugal force due to the Earth's rotation (Example 2.6.4).
2. Elastic force: the force exerted on a contacting body by a deformed body trying to recover its shape, including the normal force (support force) $F_{\mathrm{N}}$, the tension in a rope $F_{\mathrm{T}}$ and the force of a spring. Within the elastic limit, the force of a spring obeys Hooke's law $F = -k\,\Delta x$, where $k$ is the spring constant and $\Delta x$ is the extension.
3. Friction: the force between bodies in contact that opposes relative motion or the tendency to relative motion. The magnitude of static friction is determined by the other forces and the state of motion, with maximum value $\mu_{\mathrm{s}}F_{\mathrm{N}}$; kinetic friction is $F_{\mathrm{f}} = \mu_{\mathrm{k}}F_{\mathrm{N}}$, usually with $\mu_{\mathrm{k}} < \mu_{\mathrm{s}}$.
4. Fluid resistance (drag): the force on a body moving in a fluid, directed opposite to the **relative velocity**. At very low speeds the drag is proportional to the speed (for a small sphere of radius $r$ in a fluid of viscosity $\eta$, Stokes' formula $F = 6\pi\eta rv$); at higher speeds it is approximately proportional to the square of the speed, $F = \frac12 C\rho Av^2$, where $\rho$ is the density of the fluid, $A$ is the frontal area of the body and $C$ is the dimensionless drag coefficient.
5. Surface tension: the pull between two adjacent parts of a liquid surface layer, acting in the surface and perpendicular to the dividing line, with magnitude proportional to the length $l$ of the line, $F = \gamma l$, where $\gamma$ is the surface tension coefficient (unit $\mathrm{N\,m^{-1}}$). A liquid film has two surfaces, and the pull is $2\gamma l$.

Apart from gravity, these macroscopic forces all originate in the electromagnetic interaction between atoms and molecules. The forces produced by shear and torsion of solids are treated under elastic deformation in [5.1.7](/5.1.7).

## 2.4. The Four Fundamental Interactions

**Definition 2.4.1 (Fundamental Interaction)** As far as is known, all interactions in nature can be reduced to four **fundamental interactions**: the gravitational, electromagnetic, weak and strong interactions.

| Interaction | Relative strength (order of magnitude) | Range | Mediator | Examples |
|---|---|---|---|---|
| Strong | $1$ | $\sim10^{-15}\,\mathrm{m}$ | gluon | binds quarks into protons and neutrons; the nuclear force is its residual effect |
| Electromagnetic | $10^{-2}$ | infinite | photon | structure of atoms and molecules; macroscopic forces such as elastic force and friction |
| Weak | $10^{-6}$ | $\sim10^{-18}\,\mathrm{m}$ | $\mathrm{W}^{\pm}$, $\mathrm{Z}^0$ bosons | $\beta$ decay; nuclear fusion in the Sun |
| Gravitational | $10^{-39}$ | infinite | (hypothetical graviton) | gravity; motion of celestial bodies |

The relative strength depends on how the comparison is made and on the energy of the particles; the table gives only orders of magnitude at low energy. Gravity is the weakest of the four interactions yet dominates the motion of celestial bodies, because it is only attractive and cannot be screened, while the positive and negative charges of macroscopic bodies cancel almost completely. At high energies the electromagnetic and weak interactions are unified as the electroweak interaction (Glashow, Weinberg, Salam). In general relativity, gravity is understood as an effect of the curvature of spacetime (Section 2.6.3).

## 2.5. Applications of Newton's Laws

The general procedure for solving problems with Newton's laws is:

1. Choose the object: decide which body to study and, if necessary, isolate it from its surroundings (free body);
2. Examine the motion: analyze its state of motion and write down the acceleration (the **kinematics** of [5.1.1](/5.1.1));
3. Identify the forces: draw all the external forces on it;
4. Set up the equations: write the component form of Newton's second law in the chosen coordinate system, often supplemented by kinematic relations or geometric constraints;
5. Check the result: verify that dimensions, special cases and trends are reasonable.

**Example 2.5.1 (Pressure Difference Across a Soap Bubble)** A spherical soap bubble of radius $R$ has surface tension coefficient $\gamma$ of the soap solution. Find how much the pressure $p_{\mathrm{in}}$ inside the bubble exceeds the outside atmospheric pressure $p_0$.

Take the right half of the bubble as the object. In the horizontal direction it is acted on by three forces: the force $F_{\mathrm{ext}}$ of the outside atmosphere (to the left), the force $F_{\mathrm{in}}$ of the gas inside (to the right), and the surface tension $F_{\mathrm{surf}}$ exerted by the left hemisphere across the dividing circle (to the left). By symmetry the vertical components of the pressure forces cancel. Take an area element on the sphere, $\mathrm{d}S = R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$ ($\theta$ measured from the horizontal axis); the horizontal component of the pressure force on it is $p\cos\theta\,\mathrm{d}S$, and integrating gives

$$
F_{\mathrm{ext}} = \int p_0\cos\theta\,\mathrm{d}S = p_0\,\pi R^2, \qquad F_{\mathrm{in}} = p_{\mathrm{in}}\,\pi R^2,
$$
that is, the resultant force of a uniform pressure on a curved surface equals the pressure times the area of the surface's projection in the perpendicular direction. The soap film has an inner and an outer surface, so $F_{\mathrm{surf}} = 2\gamma\cdot2\pi R$. At equilibrium $F_{\mathrm{in}} = F_{\mathrm{ext}} + F_{\mathrm{surf}}$, hence

$$
p_{\mathrm{in}} - p_0 = \frac{4\gamma}{R}.
$$
A liquid drop has only one surface, and the pressure difference is $2\gamma/R$ (Laplace's formula). The smaller the bubble, the higher the internal pressure: when two bubbles of different sizes are connected, the small one shrinks and the large one expands.

**Example 2.5.2 (Rotating Bucket)** A cylindrical bucket rotates about its vertical symmetry axis with constant **angular velocity** $\omega$, and the water in it is at rest relative to the bucket. Find the shape of the water surface.

1. Choose the object: a small piece of water of mass $m$ on the surface, at distance $r$ from the axis.
2. Examine the motion: it moves in uniform circular motion, with acceleration $\omega^2 r$ toward the axis.
3. Identify the forces: gravity $mg$ and the force $F_{\mathrm{N}}$ of the rest of the water on it, perpendicular to the surface. Let the normal of the surface make an angle $\theta$ with the vertical.
4. Set up the equations:

$$
F_{\mathrm{N}}\cos\theta - mg = 0, \qquad F_{\mathrm{N}}\sin\theta = m\omega^2 r,
$$
supplemented by the geometric relation that the slope of the surface is $\dfrac{\mathrm{d}z}{\mathrm{d}r} = \tan\theta$. Combining the three equations gives $\dfrac{\mathrm{d}z}{\mathrm{d}r} = \dfrac{\omega^2}{g}r$, a **separable equation**, and integrating gives

$$
z = \frac{\omega^2}{2g}r^2 + z_0.
$$
The water surface is a paraboloid of revolution, and $z_0$ is the height of the surface on the axis. Let the depth of the water at rest be $h$ and the radius of the bucket be $R$; conservation of the volume of water, $\int_0^R z\cdot2\pi r\,\mathrm{d}r = \pi R^2h$, gives $z_0 = h - \dfrac{\omega^2R^2}{4g}$.

5. Check the result: $\dim\dfrac{\omega^2r^2}{g} = \dfrac{\mathsf{T}^{-2}\mathsf{L}^2}{\mathsf{L}\,\mathsf{T}^{-2}} = \mathsf{L}$, consistent with $z$; for $\omega = 0$, $z = h$ and the surface is horizontal; the larger $\omega$ is, the lower the center and the higher the edge.

This example shows that, besides the dynamical equations, one often needs supplementary kinematic equations or geometric constraints (here the relation between the slope of the surface and the direction of the normal).

**Example 2.5.3 (Terminal Velocity)** A body of mass $m$ falls vertically from rest in air.

If the resistance is proportional to the speed, $F = bv$, then taking downward as positive, $m\dfrac{\mathrm{d}v}{\mathrm{d}t} = mg - bv$. This is a first-order **linear differential equation** ([2.2.15](/2.2.15)), and its solution satisfying $v(0) = 0$ is

$$
v(t) = v_{\mathrm{T}}\left(1 - \mathrm{e}^{-t/\tau}\right), \qquad v_{\mathrm{T}} = \frac{mg}{b}, \qquad \tau = \frac{m}{b} = \frac{v_{\mathrm{T}}}{g}.
$$
If the resistance is proportional to the square of the speed, $F = \frac12C\rho Av^2$, the equation $m\dfrac{\mathrm{d}v}{\mathrm{d}t} = mg - \frac12C\rho Av^2$ is a **separable equation**, with solution

$$
v(t) = v_{\mathrm{T}}\tanh\frac{gt}{v_{\mathrm{T}}}, \qquad v_{\mathrm{T}} = \sqrt{\frac{2mg}{C\rho A}}.
$$
In both cases the speed increases monotonically and approaches the limiting value $v_{\mathrm{T}}$, at which the resistance balances gravity and the body falls at constant speed. This limiting speed is called the *terminal velocity*. From the expression for $v_{\mathrm{T}}$, a larger body of the same shape has a larger terminal velocity: $m \propto r^3$ and $A \propto r^2$, so $v_{\mathrm{T}} \propto \sqrt{r}$.

For a projectile subject to both gravity and quadratic drag, the equations for the two components are coupled through $\lvert\boldsymbol{v}\rvert$ and have no elementary solution; they can be solved numerically with `scipy.integrate.solve_ivp` (the initial value problem of [4.4.4](/4.4.4)).

![Left: speed of a body falling from rest under linear and quadratic drag, with horizontal axis $gt/v_{\mathrm{T}}$; both approach the terminal velocity. Right: numerical trajectories of a body thrown at $50\,\mathrm{m\,s^{-1}}$ and $45^\circ$ for different terminal velocities (that is, different drag magnitudes); drag shortens the range and makes the trajectory asymmetric, with the descent steeper than the ascent](./plots/air-resistance.py)

## 2.6. Dynamics in Non-Inertial Frames

### 2.6.1. Inertial Frames as an Approximation

Newton's laws hold only in inertial frames. In a railway carriage accelerating relative to the ground, a small ball on a smooth table experiences no horizontal force yet accelerates backward relative to the carriage: Newton's laws do not hold in the frame of the carriage.

There is no strictly inertial frame in nature; all commonly used frames have some acceleration:

| Reference frame | Source of the acceleration | Magnitude of the acceleration |
|---|---|---|
| Ground frame | Earth's rotation (at the equator) | $3.4\times10^{-2}\,\mathrm{m\,s^{-2}}$ |
| Geocentric frame | Earth's revolution around the Sun | $6\times10^{-3}\,\mathrm{m\,s^{-2}}$ |
| Solar frame | Sun's motion around the center of the Galaxy | $2\times10^{-10}\,\mathrm{m\,s^{-2}}$ |

Whether a reference frame can be treated as inertial therefore depends on the accuracy required by the problem. To use Newton's laws in an accelerating frame, they must be modified.

### 2.6.2. Translating Non-Inertial Frames and Inertial Forces

Let $S$ be an inertial frame and let $S'$ be a frame in **translation** relative to $S$ with acceleration $\boldsymbol{a}_0$. In $S$ a particle satisfies $\boldsymbol{F} = m\boldsymbol{a}$. By the Galilean transformation ([5.1.1](/5.1.1#thm-1.7.1)), the acceleration of the particle in $S'$ is $\boldsymbol{a}' = \boldsymbol{a} - \boldsymbol{a}_0$; force and mass do not change with the reference frame, so $\boldsymbol{F} \ne m\boldsymbol{a}'$. But

$$
\boldsymbol{F} = m\boldsymbol{a} = m\boldsymbol{a}' + m\boldsymbol{a}_0 \quad\Longrightarrow\quad \boldsymbol{F} - m\boldsymbol{a}_0 = m\boldsymbol{a}'.
$$

**Definition 2.6.1 (Inertial Force)** In a translating non-inertial frame of acceleration $\boldsymbol{a}_0$, the quantity

$$
\boldsymbol{F}_{\mathrm{in}} = -m\boldsymbol{a}_0,
$$
introduced for a particle of mass $m$, is called the translational **inertial force**. In this frame, then, $\boldsymbol{F} + \boldsymbol{F}_{\mathrm{in}} = m\boldsymbol{a}'$, and Newton's second law holds in form.

The inertial force is an additional force introduced because of the accelerated motion of the reference frame itself; in essence it is a manifestation of the inertia of bodies. It is not an interaction between bodies: no body exerts it and it has no reaction force, yet it has real effects in a non-inertial frame. When a car brakes hard, the passengers lurch forward; in the language of inertial forces, they experience a forward inertial force.

### 2.6.3. The Equivalence Principle

The translational inertial force $-m\boldsymbol{a}_0$ is proportional to mass, just like gravity. In a spaceship far from any celestial body, accelerating with $\boldsymbol{a}_0 = -\boldsymbol{g}$, all bodies "experience" an inertial force $m\boldsymbol{g}$, which cannot be distinguished from the gravitational force $m\boldsymbol{g}$ experienced in a spaceship at rest on the ground; conversely, in a spaceship in free fall in a gravitational field, gravity and the inertial force cancel, all bodies are weightless, and the situation cannot be distinguished from that in an inertial frame far from celestial bodies.

This indistinguishability presupposes that the inertial mass (the $m$ in the second law) equals the gravitational mass (the $m$ in the law of universal gravitation). From Eötvös's torsion balance experiments to the MICROSCOPE satellite experiment of 2017–2022, the relative deviation of their ratio from 1 has been bounded below the order of $10^{-15}$. Einstein raised this to a principle: in a sufficiently small region of spacetime, the physical effects of a uniform gravitational field and of a uniformly accelerating reference frame are completely equivalent. This is called the *equivalence principle*, and it is the starting point of general relativity.

**Example 2.6.1** A railway carriage accelerates horizontally with acceleration $\boldsymbol{a}_0$, and a simple pendulum of length $l$ hangs in it. In the frame of the carriage, the bob is acted on by gravity $m\boldsymbol{g}$, the tension in the string and the inertial force $-m\boldsymbol{a}_0$. The resultant of gravity and the inertial force amounts to an "effective gravity" $m\boldsymbol{g}_{\mathrm{eff}} = m(\boldsymbol{g} - \boldsymbol{a}_0)$ of magnitude $mg_{\mathrm{eff}} = m\sqrt{g^2 + a_0^2}$. The equilibrium position of the pendulum therefore deviates backward from the vertical by

$$
\theta = \arctan\frac{a_0}{g},
$$
and the period of small oscillations changes from $2\pi\sqrt{l/g}$ to

$$
T = 2\pi\sqrt{\frac{l}{\sqrt{g^2 + a_0^2}}}.
$$

**Example 2.6.2 (Weightlessness)** A box of mass $M$ falls vertically in free fall, and a small ball of mass $m$ hangs inside from a light string of length $l$ ($M \gg m$, so the ball does not affect the motion of the box). While the box is in free fall, the inertial force $-m\boldsymbol{g}$ on the ball in the frame of the box cancels gravity, and the ball is acted on by the tension only. If at release the ball has a **velocity** $v$ relative to the box perpendicular to the string, it moves in uniform circular motion of speed $v$ about the suspension point, with the tension $mv^2/l$ providing the centripetal force; if it is at rest relative to the box, it stays at rest. Seen from the ground, the motion of the ball is the superposition of this uniform circular motion and the free fall of the box.

**Example 2.6.3** A wedge of mass $M$ and inclination $\theta$ rests on a smooth horizontal plane, and a block of mass $m$ slides down its smooth incline. Find the acceleration of the wedge.

Let the force of the block on the wedge be $F'_{\mathrm{N}}$; it is perpendicular to the incline, and its horizontal component pushes the wedge:

$$
Ma_M = F'_{\mathrm{N}}\sin\theta.
$$
Analyze the block in the frame of the wedge: it is acted on by gravity $mg$, the support force of the incline $F_{\mathrm{N}} = F'_{\mathrm{N}}$ and the inertial force $ma_M$ (horizontal, pointing away from the direction of motion of the wedge). The block moves along the incline, so it has no acceleration along the normal to the incline:

$$
F_{\mathrm{N}} + ma_M\sin\theta - mg\cos\theta = 0.
$$
Solving the two equations together,

$$
a_M = \frac{g\sin\theta\cos\theta}{M/m + \sin^2\theta}.
$$
Check: as $M \to \infty$, $a_M \to 0$ and the wedge does not move; as $\theta \to 0$ or $\theta \to \pi/2$, $a_M \to 0$, which is also reasonable. Working in the frame of the wedge avoids writing down the complicated acceleration of the block in the ground frame.

### 2.6.4. Tides

The sea rises and falls twice a day. Why is there a high tide simultaneously on the side facing the Moon and on the side facing away from it? Why is the Moon's effect larger than that of the Sun, whose mass is much greater?

The reference frame with origin at the center of the Earth and translating with it (the geocentric frame) has an acceleration $\boldsymbol{a}_0$ under the Moon's gravitational attraction, equal to the gravitational acceleration due to the Moon at the Earth's center. In this frame, seawater of mass $m$ on the Earth is acted on, besides the Earth's attraction, by the Moon's attraction and the inertial force $-m\boldsymbol{a}_0$. The Moon's attraction decreases with distance and so differs in magnitude and direction at different places on the Earth, while the inertial force is the same everywhere:

- On the side facing the Moon, the Moon's attraction exceeds its value at the Earth's center, and the resultant points away from the Earth's center toward the Moon;
- On the side facing away from the Moon, the Moon's attraction is smaller than its value at the Earth's center, and the resultant points away from the Moon, again away from the Earth's center;
- On the two sides perpendicular to the Earth–Moon line, the resultant points toward the Earth's center.

This residual force, produced by the non-uniformity of the gravitational field, is called the tidal force. It raises the sea surface at the two ends of the Earth–Moon line and lowers it on the sides, so as the Earth rotates once, a given place experiences two high tides and two low tides. Along the line, the tidal acceleration at distance $R$ from the Earth's center is approximately $\dfrac{2GM_{\mathrm{M}}R}{r^3}$ ($M_{\mathrm{M}}$ is the mass of the Moon and $r$ the Earth–Moon distance); it is inversely proportional to $r^3$, rather than to $r^2$ as gravity is. According to the equilibrium tide theory (which assumes that the seawater has enough time to reach equilibrium), the height difference between high and low tide is

$$
\Delta h = \frac32\,\frac{M}{M_{\mathrm{E}}}\left(\frac{R_{\mathrm{E}}}{r}\right)^3R_{\mathrm{E}},
$$
where $M$ and $r$ are the mass of the celestial body and its distance from the Earth's center, and $M_{\mathrm{E}}$, $R_{\mathrm{E}}$ are the mass and radius of the Earth. Substituting the data, the Moon gives $\Delta h_{\mathrm{M}} \approx 0.54\,\mathrm{m}$ and the Sun gives $\Delta h_{\mathrm{S}} \approx 0.25\,\mathrm{m}$: the mass of the Sun is $2.7\times10^7$ times that of the Moon, but its distance is about 390 times greater, and after cubing the Moon's effect is about 2.2 times the Sun's.

The two effects add according to the relative positions. At new moon and full moon, the Sun, Earth and Moon are almost in a line, the two bulges coincide, and spring tides result; at the first and last quarters the two bulges are perpendicular and partly cancel, giving neap tides. Actual tidal ranges are also strongly affected by coastlines and seafloor topography: the tidal bore at the mouth of the Qiantang River and the tidal range of the Bay of Fundy in Canada (up to about $16\,\mathrm{m}$) are far larger than the equilibrium estimate, owing to the amplification of tidal waves by the shape of the bay. The triggering of a few faults already in a critical state by tidal stress has been reported, but it cannot be used to predict earthquakes.

### 2.6.5. The Centrifugal Force in a Uniformly Rotating Frame

Let the frame $S'$ rotate with constant angular velocity $\boldsymbol{\omega}$ about a fixed axis relative to the inertial frame $S$. First consider a particle at rest in $S'$ at distance $r$ from the axis. In $S$ it moves in uniform circular motion, and the net force $\boldsymbol{f}$ on it provides the **centripetal acceleration**: $\boldsymbol{f} = -m\omega^2\boldsymbol{r}_\perp$, where $\boldsymbol{r}_\perp$ is the vector drawn perpendicularly from the axis to the particle. In $S'$ the particle is at rest, $\boldsymbol{a}' = \boldsymbol{0}$, yet $\boldsymbol{f} \ne \boldsymbol{0}$.

**Definition 2.6.2 (Centrifugal Force)** In a frame rotating uniformly with angular velocity $\boldsymbol{\omega}$, the quantity

$$
\boldsymbol{F}_{\mathrm{cf}} = m\omega^2\boldsymbol{r}_\perp = -m\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}),
$$
introduced for a particle of mass $m$, is called the **centrifugal force**, where $\boldsymbol{r}$ is the **position vector** of the particle relative to a point on the axis.

Then $\boldsymbol{f} + \boldsymbol{F}_{\mathrm{cf}} = \boldsymbol{0} = m\boldsymbol{a}'$: seen in $S'$, the real force on the particle balances the centrifugal force, so the particle is at rest. The centrifugal force is not the reaction to the centripetal force: the reaction to the centripetal force acts on the body that exerts it, whereas the centrifugal force acts on the particle itself.

**Example 2.6.4 (Gravitational Acceleration and Latitude)** Take the ground rotating with the Earth as the reference frame. A body on the ground is acted on, besides the Earth's attraction $\boldsymbol{F}_{\mathrm{g}}$, by the centrifugal force $m\omega^2R\cos\varphi$, directed outward perpendicular to the Earth's axis ($R$ is the radius of the Earth, $\varphi$ the latitude and $\omega$ the angular velocity of the Earth's rotation). What we call gravity is the resultant of the two. Treating the Earth as a uniform sphere, the gravitational acceleration is $g_0 = \dfrac{GM_{\mathrm{E}}}{R^2} \approx 9.83\,\mathrm{m\,s^{-2}}$, while $a_0 = R\omega^2 \approx 0.034\,\mathrm{m\,s^{-2}} \ll g_0$. The component of the centrifugal acceleration along the direction toward the Earth's center is $a_0\cos^2\varphi$; to first order in $a_0/g_0$,

$$
g \approx g_0\left(1 - \frac{a_0}{g_0}\cos^2\varphi\right) = g_0 - a_0\cos^2\varphi.
$$
Thus $g$ is smallest at the equator and largest at the poles. The direction of gravity (the plumb line) also deviates slightly from the direction to the Earth's center, with a maximum deviation of about $0.1^\circ$ at latitude $45^\circ$. The measured difference between the equator and the poles (about $9.780$ and $9.832\,\mathrm{m\,s^{-2}}$, a difference of $0.052\,\mathrm{m\,s^{-2}}$) is larger than $a_0$; the rest comes from the Earth's oblateness: the equator is farther from the Earth's center.

### 2.6.6. The Coriolis Force

For a particle moving relative to a rotating frame, the centrifugal force alone is not enough. Consider first a special case: a turntable rotates counterclockwise with constant angular velocity $\omega$, and on it is a smooth circular groove centered on the axis with radius $r$, in which a particle moves in uniform circular motion with relative speed $v'$ in the sense of rotation. In the inertial frame $S$, the speed of the particle is $v' + \omega r$, and the force of the groove wall on it, directed toward the center, is

$$
F = m\frac{(v' + \omega r)^2}{r} = m\frac{v'^2}{r} + 2mv'\omega + m\omega^2r.
$$
In the rotating frame $S'$, the particle moves in uniform circular motion with speed $v'$ and centripetal acceleration $a' = v'^2/r$. Hence $F - 2mv'\omega - m\omega^2r = ma'$: in $S'$, besides the centrifugal force $m\omega^2r$, there is another inertial force, directed away from the center, of magnitude $2mv'\omega$.

In general, the rate of change of a vector observed in a rotating frame differs from that in an inertial frame. Let $\boldsymbol{A}$ be any vector, resolved along the axes of $S'$; an observer in $S'$ sees only the change of the components, $\left(\dfrac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_{S'}$. In $S$, the axes of $S'$ themselves rotate with angular velocity $\boldsymbol{\omega}$, and the rate of change of the unit vectors is $\boldsymbol{\omega}\times\boldsymbol{e}'_i$ (Section 1.5.2 of [5.1.1](/5.1.1)), so

$$
\left(\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_S = \left(\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t}\right)_{S'} + \boldsymbol{\omega}\times\boldsymbol{A}.
$$

**Theorem 2.6.1 (Acceleration Transformation in a Rotating Frame)** Let $S'$ rotate with constant angular velocity $\boldsymbol{\omega}$ about a fixed axis through the origin relative to the inertial frame $S$, and let the position vector, velocity and acceleration of a particle in $S'$ be $\boldsymbol{r}$, $\boldsymbol{v}'$ and $\boldsymbol{a}'$. Then its velocity and acceleration in $S$ are

$$
\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}, \qquad
\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) + 2\boldsymbol{\omega}\times\boldsymbol{v}'.
$$

**Proof** Applying the relation above to $\boldsymbol{A} = \boldsymbol{r}$ gives $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}$. Applying it once more to $\boldsymbol{A} = \boldsymbol{v}$, with $\boldsymbol{\omega}$ a constant vector:

$$
\boldsymbol{a} = \left(\frac{\mathrm{d}}{\mathrm{d}t}\right)_{S'}(\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r}) + \boldsymbol{\omega}\times(\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{r})
= \boldsymbol{a}' + \boldsymbol{\omega}\times\boldsymbol{v}' + \boldsymbol{\omega}\times\boldsymbol{v}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}). \quad\square
$$

The three terms are named as follows: $\boldsymbol{a}$ is the absolute acceleration, $\boldsymbol{a}'$ is the relative acceleration, $\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$ is the transport acceleration (the centripetal acceleration of the point of $S'$ coinciding with the particle), and $2\boldsymbol{\omega}\times\boldsymbol{v}'$ is called the *Coriolis acceleration*. It appears only when the particle moves relative to the rotating frame, and is precisely the term, foreshadowed in [5.1.1](/5.1.1), that is absent from the transformation between translating frames. Multiplying the theorem by $m$ and rearranging gives the equation of dynamics in the rotating frame:

**Definition 2.6.3 (Coriolis Force)** The inertial force

$$
\boldsymbol{F}_{\mathrm{C}} = 2m\boldsymbol{v}'\times\boldsymbol{\omega} = -2m\boldsymbol{\omega}\times\boldsymbol{v}'
$$
introduced, in a frame rotating uniformly with angular velocity $\boldsymbol{\omega}$, for a particle of mass $m$ moving with velocity $\boldsymbol{v}'$ relative to that frame, is called the **Coriolis force**. In the rotating frame,

$$
\boldsymbol{F} + m\omega^2\boldsymbol{r}_\perp + 2m\boldsymbol{v}'\times\boldsymbol{\omega} = m\boldsymbol{a}'.
$$

The Coriolis force is perpendicular to the relative velocity, so it changes only the direction of motion and does no work. In the groove example above, $\boldsymbol{v}'$ is along the sense of rotation and $2m\boldsymbol{v}'\times\boldsymbol{\omega}$ points away from the center with magnitude $2mv'\omega$, in agreement with the direct calculation.

![A small block sliding on a smooth turntable. Left: in the inertial frame it moves in a straight line; right: seen from the counterclockwise rotating turntable, its path curves to the right, the combined result of the centrifugal force and the Coriolis force](./plots/coriolis-deflection.py)

The Earth is a rotating frame, with $\omega = 7.29\times10^{-5}\,\mathrm{rad\,s^{-1}}$. Although the Coriolis force is small, its effects are significant in motions over large scales or long times:

- A body moving horizontally in the Northern Hemisphere experiences a Coriolis force pointing to the right of its direction of motion, and to the left in the Southern Hemisphere.
- Trade winds near the equator: air flowing from the subtropics toward the equator is deflected to the right in the Northern Hemisphere and becomes the northeast trade wind, and is deflected to the left in the Southern Hemisphere and becomes the southeast trade wind.
- Tropical cyclones: air converging on a low-pressure center is deflected to the right, so typhoons in the Northern Hemisphere rotate counterclockwise and cyclones in the Southern Hemisphere rotate clockwise. The direction in which a bathtub drains is determined mainly by the initial disturbance and the shape of the container; the Coriolis force has a negligible influence.
- Eastward deflection of falling bodies: a body falling vertically experiences an eastward Coriolis force (Example 2.6.5).
- The heavier erosion of the right bank of rivers in the Northern Hemisphere and the greater wear of the right-hand rail of double-track railways are also often attributed to the Coriolis force, but these effects are tiny and are often masked by other factors.

**Example 2.6.5 (Eastward Deflection of a Falling Body)** At latitude $\varphi$, a body falls freely from rest from height $h$, with air resistance neglected. Take local coordinates with the $x$ axis pointing east, the $y$ axis north and the $z$ axis vertically upward, so that $\boldsymbol{\omega} = \omega(\cos\varphi\,\boldsymbol{e}_y + \sin\varphi\,\boldsymbol{e}_z)$. The Coriolis force is much smaller than gravity; to first approximation take $\boldsymbol{v}' \approx -gt\,\boldsymbol{e}_z$, so that

$$
-2\boldsymbol{\omega}\times\boldsymbol{v}' = 2\omega gt\cos\varphi\,(\boldsymbol{e}_y\times\boldsymbol{e}_z) = 2\omega gt\cos\varphi\,\boldsymbol{e}_x,
$$
that is, the Coriolis acceleration points east. Integrating twice gives the eastward deflection at landing

$$
x = \frac13\omega gt^3\cos\varphi = \frac13\omega\cos\varphi\sqrt{\frac{8h^3}{g}}.
$$
For $h = 100\,\mathrm{m}$ and $\varphi = 40^\circ$, $x \approx 1.7\,\mathrm{cm}$. In the inertial frame, this is because a body at a height has a larger linear velocity due to the Earth's rotation than the ground, so as it falls it "runs ahead" to the east of its starting point on the ground.

**Example 2.6.6 (Foucault Pendulum)** In 1851, Foucault demonstrated the rotation of the Earth in Paris with a simple pendulum $67\,\mathrm{m}$ long: the plane of oscillation turns slowly clockwise relative to the ground (Northern Hemisphere, seen from above). In the inertial frame, the direction of the plane of oscillation stays fixed (only gravity and tension act, both lying in the plane), and it is the ground that rotates beneath it. At latitude $\varphi$, the component of the Earth's angular velocity along the local vertical is $\omega\sin\varphi$, so the time for the plane of oscillation to turn once is

$$
T = \frac{T_0}{\sin\varphi},
$$
where $T_0 \approx 23.93\,\mathrm{h}$ is the time for one rotation of the Earth relative to the stars (the sidereal day). In Paris ($\varphi \approx 48.9^\circ$), $T \approx 31.8\,\mathrm{h}$; in Beijing ($\varphi \approx 39.9^\circ$), $T \approx 37.3\,\mathrm{h}$; at the poles $T = T_0$, and at the equator the plane of oscillation does not turn. In the ground frame, this is the result of the horizontal component of the Coriolis force on the bob deflecting the plane of oscillation.

## Summary

| Topic | Key points |
|---|---|
| Newton's laws of motion | The first law gives the concepts of inertia and force and defines inertial frames; the second law $\boldsymbol{F} = \dfrac{\mathrm{d}(m\boldsymbol{v})}{\mathrm{d}t}$; the third law $\boldsymbol{F}_{12} = -\boldsymbol{F}_{21}$ |
| Units and dimensions | The 2019 SI is fixed by seven defining constants; $\dim F = \mathsf{L}\,\mathsf{M}\,\mathsf{T}^{-2}$, and both sides of an equation must have the same dimension |
| Problem-solving procedure | Choose the object, examine the motion, identify the forces, set up the equations, check the result |
| Translating non-inertial frames | Inertial force $\boldsymbol{F}_{\mathrm{in}} = -m\boldsymbol{a}_0$; the equivalence principle |
| Rotating frames | Centrifugal force $m\omega^2\boldsymbol{r}_\perp$, Coriolis force $2m\boldsymbol{v}'\times\boldsymbol{\omega}$; $\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) + 2\boldsymbol{\omega}\times\boldsymbol{v}'$ |

## Questions

1. A body is pressed against a rough vertical wall by a horizontal force $F$ and stays at rest. How does the static friction on the body change as $F$ gradually increases?

   **Answer** It does not change; it always equals the weight of the body. Static friction is determined by the equilibrium condition, and what increases with $F$ is only the maximum static friction $\mu_{\mathrm{s}}F$.

2. A spring with mass is hung at its upper end from a string and is in equilibrium. Is the extension the same in every segment of the spring? How does the spring move at the instant the string is cut?

   **Answer** The higher a segment, the more weight below it it must bear and the greater its extension. At the instant of cutting, the deformation of the spring has no time to change; the elastic force on the lower end still balances gravity, so it stays at rest, while the upper end is acted on by a downward elastic force and gravity, with acceleration greater than $g$; the spring begins to contract from the upper end, and the acceleration of the center of mass of the whole spring is always $g$ (the center-of-mass motion theorem of [5.1.3](/5.1.3)).

3. Which causes larger tides, the Sun or the Moon?

   **Answer** The Moon. The tidal force is proportional to the mass of the body and inversely proportional to the cube of its distance (Section 2.6.4).
