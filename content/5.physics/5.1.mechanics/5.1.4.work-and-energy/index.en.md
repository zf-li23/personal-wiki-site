---
title: Work and Energy
description: Work and the work-kinetic energy theorem, the work of a pair of forces, conservative forces and potential energy, forces from potential energy and potential energy curves, the work-energy principle and conservation of mechanical energy, central force fields and the effective potential, conservation laws and symmetry, collisions, König's theorem and the two-body problem, the continuity equation and Bernoulli's equation for ideal fluids.
source_hash: c09edd91f230
---

[The previous chapter](/5.1.3) discussed the accumulation of force over time: **impulse** changes **momentum**, and **angular impulse** changes **angular momentum**. This chapter discusses the accumulation of force over space: the integral of a force along a path is work, and work changes kinetic energy. A force whose work is independent of the path can be replaced by a scalar function (the potential energy), which leads to the law of conservation of mechanical energy; together with conservation of momentum and of angular momentum, it forms the three conservation laws of mechanics. Mathematically, work is a **line integral of a vector field**, a conservative force is a **conservative vector field**, the potential energy is a **potential function** (up to a sign), and finding the force from the potential energy means taking a **gradient**; all of this was covered in [2.2.14](/2.2.14), and this chapter stresses the physical meaning: whether each quantity belongs to a **particle** or to a system, and whether it depends on the **reference frame**. The central-force problem uses the two conserved quantities, energy and angular momentum, to reduce the equations of motion to first order, a typical application of the method of **first integrals** ([2.4.14](/2.4.14)). The last two sections apply the work-energy relations to fluids and lead to Bernoulli's equation. The next chapter, [5.1.5](/5.1.5), applies these laws to rigid bodies; the first law of thermodynamics in the thermal physics part ([5.2.3](/5.2.3)) is the extension of the law of conservation of energy to thermal phenomena.

## 4.1. Work

**Definition 4.1.1 (Work)** Let a particle move along a path $L$ from $A$ to $B$ under a force $\boldsymbol{F}$. The **work** done by the force on the particle is the integral along the path of the scalar product of the force and the element of **displacement**:

$$
W_{AB}=\int_{L}\mathrm{d}W=\int_{A}^{B}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=\int_{A}^{B}F\cos\theta\,\lvert\mathrm{d}\boldsymbol{r}\rvert,
$$
where $\theta$ is the angle between $\boldsymbol{F}$ and $\mathrm{d}\boldsymbol{r}$. The SI unit of work is the joule, $1\,\mathrm{J}=1\,\mathrm{N\,m}$.

Work is a **line integral of a vector field**, and three points deserve attention:

- Work is a process quantity, not a state quantity: in general it depends on the path, and one cannot say that "a particle has such and such an amount of work at a certain place."
- Work is a scalar and can be positive or negative: the force does positive work for $0\le\theta<\pi/2$, no work for $\theta=\pi/2$, and negative work for $\pi/2<\theta\le\pi$ (often described as "work done against the force").
- Work depends on the reference frame: the same force corresponds to different displacements in different frames. For example, for a person standing in an elevator moving upward at constant speed, the support force of the elevator does positive work in the ground frame and no work in the elevator frame.

The work done per unit time is called *power*, $P=\dfrac{\mathrm{d}W}{\mathrm{d}t}=\boldsymbol{F}\cdot\boldsymbol{v}$, with unit $\mathrm{W}=\mathrm{J\,s^{-1}}$.

## 4.2. The Work-Kinetic Energy Theorem

**Theorem 4.2.1 (Work-Kinetic Energy Theorem)** In an **inertial frame**, the work done on a particle by the net force equals the change of its kinetic energy:

$$
W_{AB}=E_{\mathrm{k}}(B)-E_{\mathrm{k}}(A)=\Delta E_{\mathrm{k}},\qquad E_{\mathrm{k}}=\frac12mv^2 .
$$

**Proof** By **Newton's second law**, $\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=m\dfrac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\cdot\boldsymbol{v}\,\mathrm{d}t=m\boldsymbol{v}\cdot\mathrm{d}\boldsymbol{v}=\mathrm{d}\Big(\dfrac12mv^2\Big)$; integrating along the path gives the result. $\square$

The quantity $E_{\mathrm{k}}=\frac12mv^2$ is called the *kinetic energy* of the particle, and it is a state quantity. Kinetic energy and work both depend on the reference frame, but the theorem holds in every **inertial frame**; in a **non-inertial frame**, the work of the **inertial forces** must also be included.

**Theorem 4.2.2 (Work-Kinetic Energy Theorem for a System of Particles)** Applying Theorem 4.2.1 to each particle of a system and summing,

$$
W_{\mathrm{ext}}+W_{\mathrm{int}}=\sum_i\Delta E_{\mathrm{k}i},
$$
where $W_{\mathrm{ext}}$ and $W_{\mathrm{int}}$ are the total work done by the external and the internal forces, respectively.

**Remark 4.2.1** Internal forces always occur in pairs and their vector sum is zero, so internal forces do not change the total momentum of the system; but the total work of the internal forces is in general not zero, because the points of application of a pair of internal forces do not necessarily have the same displacement. An exploding bomb, and two people on ice who push each other apart, are examples in which the internal forces do positive work and increase the kinetic energy of the system.

## 4.3. The Work of a Pair of Forces

A pair of forces between two particles consists of forces acting on the two particles separately, equal in magnitude and opposite in direction, $\boldsymbol{f}_1=-\boldsymbol{f}_2$ (action and reaction are the most common pair). Let the elementary displacements of particles $m_1$ and $m_2$ be $\mathrm{d}\boldsymbol{r}_1$ and $\mathrm{d}\boldsymbol{r}_2$. The sum of the elementary works of this pair is

$$
\mathrm{d}W_{\mathrm{pair}}=\boldsymbol{f}_1\cdot\mathrm{d}\boldsymbol{r}_1+\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_2=\boldsymbol{f}_2\cdot(\mathrm{d}\boldsymbol{r}_2-\mathrm{d}\boldsymbol{r}_1)=\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21},
$$
where $\boldsymbol{r}_{21}=\boldsymbol{r}_2-\boldsymbol{r}_1$ is the **position vector** of $m_2$ relative to $m_1$. From the initial configuration $A$ ($m_1$ at $A_1$, $m_2$ at $A_2$) to the final configuration $B$ ($m_1$ at $B_1$, $m_2$ at $B_2$),

$$
W_{\mathrm{pair}}=\int_A^B\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21}=\int_A^B\boldsymbol{f}_1\cdot\mathrm{d}\boldsymbol{r}_{12}.
$$

**Property 4.3.1** The work of a pair of forces depends only on the relative displacement of the two particles. Therefore:

1. the work of a pair of forces does not depend on the choice of reference frame;
2. when there is no relative displacement between the two particles, or the relative displacement is always perpendicular to the pair of forces, the work of the pair is zero;
3. the work of a pair of sliding friction forces is always negative: sliding friction always opposes the direction of relative sliding, $W_{\mathrm{pair}}=-\int f\,\mathrm{d}s_{\mathrm{rel}}<0$ ($s_{\mathrm{rel}}$ is the path length of the relative sliding). Frictional heating is the result of this negative work of the pair, and the heat produced, $-W_{\mathrm{pair}}$, does not depend on the reference frame.

**Example 4.3.1** A block $m$ slides down a smooth wedge $M$, which rests on a smooth horizontal plane. In the ground frame, the **velocity** $\boldsymbol{v}_m$ of $m$ is not along the incline, so the support force $\boldsymbol{N}$ of the incline on the block is not perpendicular to $\boldsymbol{v}_m$ and $W_N\ne0$; likewise the force $\boldsymbol{N}'$ of the block on the wedge is not perpendicular to the velocity $\boldsymbol{v}_M$ of the wedge, and $W_{N'}\ne0$. But the displacement of $m$ relative to $M$ is along the incline and perpendicular to $\boldsymbol{N}$, so the work of this pair of forces is $W_N+W_{N'}=0$.

## 4.4. Conservative Forces

**Definition 4.4.1 (Conservative Force)** If the work done by a pair of forces is independent of the path along which the two particles move relative to each other and depends only on their initial and final relative positions, the pair of forces is called a **conservative force**. Equivalently, along any closed path $L$ (the relative configuration returning to its original state),

$$
\oint_L\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}=0 .
$$

The two statements are equivalent; this is exactly the equivalence of a "conservative field" and "vanishing closed-path integral" in [Theorem 14.4.1](/2.2.14#thm-14.4.1). A force field $\boldsymbol{f}(\boldsymbol{r})$ is a conservative force if and only if it is a **conservative vector field**.

### 4.4.1. Common Conservative Forces

1. Universal gravitation. A particle $m$ moves from $A$ to $B$ under the gravitational force $\boldsymbol{f}=-\dfrac{GMm}{r^2}\boldsymbol{e}_r$ of a particle $M$. Since $\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{r}=\mathrm{d}r$ (the radial component of the displacement is the increment of $r$),
   $$
   W=\int_A^B\Big(-\frac{GMm}{r^2}\Big)\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{r}=\int_{r_A}^{r_B}\Big(-\frac{GMm}{r^2}\Big)\mathrm{d}r=\frac{GMm}{r_B}-\frac{GMm}{r_A},
   $$
   which depends only on the initial and final distances. The same calculation shows that any central force depending only on distance, $\boldsymbol{f}=f(r)\boldsymbol{e}_r$, is conservative, since $\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}=f(r)\,\mathrm{d}r$ is an exact differential.
2. The elastic force of a spring (one-dimensional): $\boldsymbol{f}=-k(x-x_0)\boldsymbol{e}_x$, where $x-x_0$ is the extension of the spring and $k$ is the spring constant.
3. Gravity: $\boldsymbol{F}=m\boldsymbol{g}$ (the uniform gravitational field near the Earth's surface).

### 4.4.2. Non-Conservative Forces

Forces whose work depends on the path are called non-conservative forces.

- Friction. The work of a pair of sliding friction forces is always negative and converts mechanical energy into heat; such a force is called a *dissipative force*. The work of static friction on a single body can be positive, negative or zero (as for goods carried by a conveyor belt), but there is no relative sliding between a pair of static friction forces, and the sum of their work is zero, so static friction is not a dissipative force.
- Explosive forces and the like: as internal forces they do positive work and convert chemical energy and so on into mechanical energy.

## 4.5. Potential Energy

### 4.5.1. Definition of Potential Energy

The work of a conservative force is independent of the path, so we can introduce a scalar function that depends only on the configuration of the system and use its change in place of the work of the conservative force.

**Definition 4.5.1 (Potential Energy)** In a process taking a system from configuration $A$ to configuration $B$, the work done by the conservative internal forces equals the decrease of the **potential energy** of the system:

$$
E_{\mathrm{p}}(A)-E_{\mathrm{p}}(B)=-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}=\int_A^B\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{r} .
$$
Choosing a configuration $O$ as the zero of potential energy, $E_{\mathrm{p}}(O)=0$, we have $E_{\mathrm{p}}(A)=\int_A^O\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{r}$.

Compared with the **potential function** $\varphi$ of [2.2.14](/2.2.14) ($\nabla\varphi=\boldsymbol{f}$), the potential energy $E_{\mathrm{p}}=-\varphi+C$ differs by a sign: physically one prefers that "the force does positive work" correspond to "the potential energy decreases."

- Potential energy belongs to the whole interacting system, not to a single particle; "the gravitational potential energy of a body" is short for "the potential energy of the system consisting of the body and the Earth."
- Potential energy is defined only through the work of a pair of conservative forces, and the work of a pair of forces does not depend on the reference frame (Property 4.3.1), so potential energy does not depend on the choice of reference frame; neither does the choice of the zero of potential energy.
- Potential energy is determined only up to a constant; it is potential energy differences that have physical meaning.

### 4.5.2. Several Kinds of Potential Energy

| System | Potential energy | Usual zero |
|---|---|---|
| Universal gravitation between two particles | $E_{\mathrm{p}}(r)=-\dfrac{GMm}{r}$ | $E_{\mathrm{p}}(\infty)=0$ |
| Gravity near the Earth's surface | $E_{\mathrm{p}}(h)=mgh$ | $E_{\mathrm{p}}(0)=0$ ($h$ is the height) |
| Spring | $E_{\mathrm{p}}(x)=\dfrac12k(x-x_0)^2$ | $E_{\mathrm{p}}(x_0)=0$ (natural length) |

## 4.6. Finding Conservative Forces from Potential Energy

### 4.6.1. Conservative Forces from the Potential Energy Function

From Definition 4.5.1, for any elementary displacement $\mathrm{d}\boldsymbol{l}$ we have $\boldsymbol{f}_{\mathrm{c}}\cdot\mathrm{d}\boldsymbol{l}=-\mathrm{d}E_{\mathrm{p}}$. Let $\theta$ be the angle between $\boldsymbol{f}_{\mathrm{c}}$ and the direction $\boldsymbol{l}$; then $f_{\mathrm{c}}\cos\theta\,\mathrm{d}l=-\mathrm{d}E_{\mathrm{p}}$, that is,

$$
f_{\mathrm{c},l}=-\frac{\partial E_{\mathrm{p}}}{\partial l}:
$$
the component of a conservative force along a direction equals the negative of the **directional derivative** of the potential energy along that direction. Taking the $x$, $y$ and $z$ directions in turn,

$$
\boldsymbol{f}_{\mathrm{c}}=-\Big(\frac{\partial E_{\mathrm{p}}}{\partial x}\boldsymbol{e}_x+\frac{\partial E_{\mathrm{p}}}{\partial y}\boldsymbol{e}_y+\frac{\partial E_{\mathrm{p}}}{\partial z}\boldsymbol{e}_z\Big)=-\operatorname{grad}E_{\mathrm{p}}=-\nabla E_{\mathrm{p}},\tag{4.1}
$$
where $\nabla$ is the **nabla operator**. Since the **gradient** points in the direction of fastest increase of a function, a conservative force points in the direction of fastest decrease of the potential energy, with magnitude equal to the rate of change of the potential energy in that direction.

**Example 4.6.1** The elastic potential energy of a spring, $E_{\mathrm{p}}=\frac12k(x-x_0)^2$, gives $\boldsymbol{f}=-\dfrac{\partial E_{\mathrm{p}}}{\partial x}\boldsymbol{e}_x=-k(x-x_0)\boldsymbol{e}_x$; the gravitational potential energy $E_{\mathrm{p}}=-GMm/r$ gives $\boldsymbol{f}=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}r}\boldsymbol{e}_r=-\dfrac{GMm}{r^2}\boldsymbol{e}_r$.

### 4.6.2. Potential Energy Curves

In one dimension, Eq. (4.1) reduces to $f=-\dfrac{\mathrm{d}E_{\mathrm{p}}}{\mathrm{d}x}$: a conservative force points in the direction in which the potential energy decreases, and its magnitude equals the slope of the potential energy curve. The graph of the potential energy as a function of configuration is called the *potential energy curve*, and it shows at a glance the equilibria of the system and their stability.

- A local minimum of the potential energy curve is a stable equilibrium position: a particle slightly displaced experiences a force toward the equilibrium position and makes small oscillations about it ([5.1.6](/5.1.6) will show that such small oscillations are simple harmonic).
- A local maximum is an unstable equilibrium position: a particle slightly displaced experiences a force away from the equilibrium position and moves away from it.
- A stretch of constant potential energy is neutral equilibrium; a position that is a local but not the global minimum is called metastable equilibrium.
- When mechanical energy is conserved, $E_{\mathrm{k}}=E-E_{\mathrm{p}}(x)\ge0$, so the particle can move only in the region $E_{\mathrm{p}}(x)\le E$, and the points where $E_{\mathrm{p}}(x)=E$ are turning points. A region of low potential energy surrounded by regions of higher potential energy (potential barriers) is called a potential well; only when its kinetic energy in well $A$ exceeds the barrier height $\Delta E_1$ can the particle cross the barrier into the adjacent well $B$.

These conclusions are the mechanical version of the stability theory of **equilibrium points** in [2.4.11](/2.4.11): the equilibrium points of the equation $m\ddot x=-E_{\mathrm{p}}'(x)$ are the points where $E_{\mathrm{p}}'=0$; if $E_{\mathrm{p}}$ has a strict local minimum at $x_0$, the mechanical energy $E(x,\dot x)-E_{\mathrm{p}}(x_0)$ is positive definite and constant along trajectories, which is precisely a **Lyapunov function**, and [Theorem 11.4.1](/2.4.11#thm-11.4.1) gives stability (the Lagrange–Dirichlet theorem).

**Example 4.6.2 (Potential Energy Curve of a Diatomic Molecule)** The potential energy $E_{\mathrm{p}}(r)$ between two atoms has a minimum at the internuclear distance $r=r_0$. At $r=r_0$, $f=0$ and this is the equilibrium position; for $r>r_0$, $f=-\mathrm{d}E_{\mathrm{p}}/\mathrm{d}r<0$, an attraction; for $r<r_0$, $f>0$, a repulsion. A commonly used model is the Lennard-Jones potential

$$
E_{\mathrm{p}}(r)=4\varepsilon\Big[\Big(\frac{\sigma}{r}\Big)^{12}-\Big(\frac{\sigma}{r}\Big)^{6}\Big],
$$
which has its minimum $-\varepsilon$ at $r_0=2^{1/6}\sigma$, where $\varepsilon$ is the depth of the potential well. The small oscillation of the molecule about $r_0$ is the molecular vibration; in real diatomic molecules the contribution of the electrons must be computed by quantum mechanics, and the Lennard-Jones potential is better suited to describing the interaction between atoms of noble gases (molecular forces and real gases are discussed in [5.2.2](/5.2.2)).

![Lennard-Jones potential energy E_p(r) and the corresponding force f(r) = -dE_p/dr in reduced units; the minimum at r0 = 2^(1/6) sigma is the equilibrium separation, the force is repulsive for r < r0 and attractive for r > r0](./plots/lennard-jones.py)

## 4.7. The Work-Energy Principle and Conservation of Mechanical Energy

### 4.7.1. The Work-Energy Principle

Divide the internal forces of a system of particles into conservative and non-conservative internal forces, $W_{\mathrm{int}}=W_{\mathrm{c,int}}+W_{\mathrm{nc,int}}$, and write $W_{\mathrm{c,int}}$ as the decrease of potential energy using Definition 4.5.1; Theorem 4.2.2 then becomes

$$
W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=\big[E_{\mathrm{k}}(B)+E_{\mathrm{p}}(B)\big]-\big[E_{\mathrm{k}}(A)+E_{\mathrm{p}}(A)\big].
$$

**Theorem 4.7.1 (Work-Energy Principle)** Define the *mechanical energy* of a system as $E=E_{\mathrm{k}}+E_{\mathrm{p}}$. Then in an inertial frame, the sum of the work of the external forces and of the non-conservative internal forces equals the change of the mechanical energy of the system:

$$
W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=E(B)-E(A),\qquad \mathrm{d}W_{\mathrm{ext}}+\mathrm{d}W_{\mathrm{nc,int}}=\mathrm{d}E .
$$

The work-kinetic energy theorem and the work-energy principle are two ways of writing the same law: the former counts the work of the conservative internal forces as work, the latter counts it in the potential energy, and it must not be counted twice.

### 4.7.2. Conservation of Mechanical Energy

**Theorem 4.7.2 (Law of Conservation of Mechanical Energy)** If $\mathrm{d}W_{\mathrm{ext}}=0$ and $\mathrm{d}W_{\mathrm{nc,int}}=0$, that is, only conservative internal forces do work, then the mechanical energy of the system stays constant, $E=\text{const}$.

The mechanical energy of an isolated conservative system is conserved. Then $\Delta E_{\mathrm{k}}=-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}$: when the conservative internal forces do positive work, potential energy is converted into kinetic energy, and when they do negative work, kinetic energy is converted into potential energy; the interconversion of potential and kinetic energy is realized and measured by the work of the conservative internal forces. Since the work of external forces depends on the reference frame, whether mechanical energy is conserved also depends on the choice of inertial frame: a system whose mechanical energy is conserved in one inertial frame may have external forces doing work in another.

### 4.7.3. The General Law of Conservation of Energy

Considering all kinds of physical phenomena and including energy of all forms (thermal, electromagnetic, chemical, nuclear and so on), we have

**Theorem 4.7.3 (Law of Conservation of Energy)** Whatever changes an isolated system undergoes, the sum of all forms of energy of the system remains constant.

The conservation of mechanical energy is the manifestation of the law of conservation of energy within mechanical motion: the mechanical energy lost when dissipative forces do work does not disappear but is converted into other forms of energy such as internal energy. The first law of thermodynamics ([5.2.3](/5.2.3)) is its quantitative statement for thermal phenomena.

### 4.7.4. An Example Combining Conservation Laws

**Example 4.7.1** A wedge of mass $M$ rests on a smooth horizontal plane, and its incline is smooth. A block of mass $m$ with horizontal initial velocity $v$ slides up the incline from its bottom (the bottom joins the horizontal plane smoothly, and the block does not leave the incline). Find the maximum height $h_{\max}$ reached by the block.

**Solution** Take $m$, $M$ and the Earth as the system: the external force (the support force of the ground) does no work and no non-conservative internal force does work, so mechanical energy is conserved. At $h=h_{\max}$ the block is at rest relative to the incline, and both have the same horizontal velocity $V$. Take the ground as the zero of gravitational potential energy:

$$
\frac12mv^2=\frac12(m+M)V^2+mgh_{\max}.
$$
For $m+M$, no external force acts horizontally, so by the **law of conservation of momentum** the horizontal momentum is conserved: $mv=(m+M)V$. Solving the two equations together,

$$
h_{\max}=\frac{M}{M+m}\cdot\frac{v^2}{2g}.
$$
Check of plausibility: the **quantity dimension** is correct; as $m/M\to0$ the wedge does not move and $mgh_{\max}=\frac12mv^2$, as expected.

### 4.7.5. Motion of a Particle in a Central Force Field

A force whose direction is always toward (or away from) a fixed center is called a *central force*; a central force depending only on distance, $\boldsymbol{F}=f(r)\boldsymbol{e}_r$ ($\boldsymbol{e}_r$ is the radial unit vector with the force center as origin), defines a central force field, as do universal gravitation and the Coulomb force. By Section 4.4.1, a central force field is a conservative force field, with potential energy $E_{\mathrm{p}}(r)=\int_r^{r_0}f(r)\,\mathrm{d}r+E_{\mathrm{p}}(r_0)$.

The **torque** of a central force about the force center is zero, and a particle moving in a central force field has two conserved quantities:

- by the **law of conservation of angular momentum**, $\boldsymbol{L}=\boldsymbol{r}\times m\boldsymbol{v}$ is a constant vector, so the motion lies in a plane through the force center perpendicular to $\boldsymbol{L}$ ([5.1.3](/5.1.3));
- the mechanical energy is conserved, and $E$ is constant.

In the plane of motion take **polar coordinates** $(r,\theta)$, with $\boldsymbol{r}=r\boldsymbol{e}_r$ and $\boldsymbol{v}=\dot r\boldsymbol{e}_r+r\dot\theta\boldsymbol{e}_\theta$. From $\boldsymbol{L}=r\boldsymbol{e}_r\times m(\dot r\boldsymbol{e}_r+r\dot\theta\boldsymbol{e}_\theta)=mr^2\dot\theta\,(\boldsymbol{e}_r\times\boldsymbol{e}_\theta)$ and conservation of mechanical energy,

$$
mr^2\dot\theta=L,\qquad \frac12m\big(\dot r^2+r^2\dot\theta^2\big)+E_{\mathrm{p}}(r)=E .
$$
Eliminating $\dot\theta$ gives an equation containing only $r$,

$$
\frac12m\dot r^2+\frac{L^2}{2mr^2}+E_{\mathrm{p}}(r)=E.\tag{4.2}
$$
These two first-order equations can replace Newton's equations (two second-order equations): the conserved quantities reduce the order of the equations by one, which is exactly the role of a **first integral**. The constants $L$ and $E$ are determined by the initial conditions $\boldsymbol{r}_0$, $\boldsymbol{v}_0$, with $L=\lvert\boldsymbol{r}_0\times m\boldsymbol{v}_0\rvert$ and $E=\frac12mv_0^2+E_{\mathrm{p}}(r_0)$; the initial conditions together with the form of the potential energy function determine the character of the orbit: whether it is closed, and its shape, size and orientation.

In Eq. (4.2), $\frac12m\dot r^2$ is the radial kinetic energy, and $\dfrac{L^2}{2mr^2}$ is the kinetic energy of the transverse motion, which grows as $r$ decreases and acts like the potential energy of a repulsive force; it is called the centrifugal potential energy. The quantity

$$
E_{\mathrm{eff}}(r)=\frac{L^2}{2mr^2}+E_{\mathrm{p}}(r)
$$
is called the *effective potential*. Along the radial direction, the particle then moves like a one-dimensional particle in the conservative potential $E_{\mathrm{eff}}(r)$, with radial kinetic energy and effective potential converting into each other, and it can be analyzed with the potential energy curves of Section 4.6.2.

For universal gravitation, $E_{\mathrm{eff}}(r)=\dfrac{L^2}{2mr^2}-\dfrac{GMm}{r}$. At perihelion and aphelion $\dot r=0$, the effective potential equals the total mechanical energy, and $r$ satisfies

$$
r^2+\frac{GMm}{E}r-\frac{L^2}{2mE}=0 .
$$

- $E=E_{\mathrm{eff,min}}$: there is only one solution $r=r_0$, a circular orbit;
- $E_{\mathrm{eff,min}}<E<0$: two positive roots, $r_{\min}\le r\le r_{\max}$, an elliptical orbit, a bound state;
- $E=0$: only one positive root, a parabolic orbit; the particle just escapes and has zero kinetic energy at infinity;
- $E>0$: one positive root, a hyperbolic orbit; the particle is unbound and still has kinetic energy at infinity.

The effective potential only gives the range of variation of $r$; that the orbit is a conic section (a closed ellipse) is a special property of the inverse-square force, and follows by eliminating $t$ between Eq. (4.2) and $mr^2\dot\theta=L$ and integrating.

![Left: effective potential E_eff(r) = L^2/(2 m r^2) - G M m / r for fixed angular momentum, with energy levels of a circular orbit, an ellipse (r_min to r_max), the parabolic case E = 0 and a hyperbola; right: orbits launched from the same point with velocity perpendicular to the radius and increasing speed (circle, ellipse, parabola, hyperbola)](./plots/effective-potential.py)

Once the potential energy function is fixed, changing the initial conditions changes the orbit. For example, a spacecraft moves in a uniform circular orbit around the Earth with **speed** $v_0$ and ejects gas radially outward (or inward) for a very short time, acquiring a small velocity $\alpha v_0$ directed toward (or away from) the Earth's center. At the instant of ejection the position vector is unchanged and the tangential velocity is unchanged, so the angular momentum $L$ is unchanged while the mechanical energy increases by $\frac12m\alpha^2v_0^2$: the new orbit is an ellipse through the point of ejection, the ellipses for the two ejection directions are radially symmetric about the point of ejection, with the perigee of one before the point of ejection and that of the other after it.

![A ship on a circular orbit receives a small radial velocity kick alpha v0 (alpha = 0.3) at the marked point; the dashed and dotted ellipses are the new orbits for an inward and an outward kick, both with the same angular momentum as the circle](./plots/orbit-kick.py)

Actual space missions are designed in just this way. The ISEE-3 probe, launched in 1978, was originally stationed on a halo orbit near the Sun–Earth L1 point; in 1982–1983, after a series of burns and five lunar flybys (changing orbit with the Moon's gravity), it left the Earth–Moon system and was renamed ICE. In 1985 it passed through the tail of comet Giacobini–Zinner (the first spacecraft to pass through a comet tail), in 1986 it observed Halley's comet from a distance, and in 2014 it returned to the vicinity of the Earth.

## 4.8. The Significance of Conservation Laws

The three conservation laws of momentum, angular momentum and energy are all more general than Newton's laws: they remain valid in domains where Newtonian mechanics fails (high speeds, microscopic particles). Their root is the symmetry of space and time:

| Conservation law | Corresponding symmetry |
|---|---|
| Conservation of momentum | translational symmetry of space (homogeneity of space) |
| Conservation of angular momentum | rotational symmetry of space (isotropy of space) |
| Conservation of energy | translational symmetry of time (homogeneity of time) |

This correspondence is called *Noether's theorem*: every continuous symmetry of the laws of physics corresponds to a conserved quantity (E. Noether, 1918). Its rigorous statement requires analytical mechanics, in which the equations of motion follow from the variation of the action (the **Euler–Lagrange equation**, [2.4.13](/2.4.13)); if the Lagrangian is invariant under a continuous transformation, there is a corresponding first integral.

## 4.9. Collisions

A collision is a process in which two or more bodies interact strongly within a very short time. In treating collision problems, one is concerned only with the change in the state of motion before and after the collision and ignores the details of the process; since the collision time is very short and the internal forces are very large, the impulse of external forces (such as gravity and friction) can usually be neglected and the momentum of the system is conserved.

**Definition 4.9.1** A collision in which the total kinetic energy of the system is unchanged is called an **elastic collision**; a collision in which kinetic energy is lost is called an **inelastic collision**; a collision after which the two bodies move with the same velocity is called a **perfectly inelastic collision**, and it has the largest loss of kinetic energy.

**Example 4.9.1 (One-Dimensional Elastic Collision)** Two balls of masses $m_1$ and $m_2$ move along the same line, with velocities $v_{10}$, $v_{20}$ before the collision and $v_1$, $v_2$ after it (components along the same positive direction). Conservation of momentum and of kinetic energy give

$$
m_1v_{10}+m_2v_{20}=m_1v_1+m_2v_2,\qquad \frac12m_1v_{10}^2+\frac12m_2v_{20}^2=\frac12m_1v_1^2+\frac12m_2v_2^2 .
$$
Write the two equations as $m_1(v_{10}-v_1)=m_2(v_2-v_{20})$ and $m_1(v_{10}^2-v_1^2)=m_2(v_2^2-v_{20}^2)$ and divide one by the other to get $v_{10}+v_1=v_{20}+v_2$, that is, $v_2-v_1=v_{10}-v_{20}$: in an elastic collision the **relative velocity** keeps its magnitude and reverses its direction. Solving,

$$
v_1=\frac{m_1-m_2}{m_1+m_2}v_{10}+\frac{2m_2}{m_1+m_2}v_{20},\qquad
v_2=\frac{m_2-m_1}{m_1+m_2}v_{20}+\frac{2m_1}{m_1+m_2}v_{10}.
$$

- $m_1=m_2$: $v_1=v_{20}$ and $v_2=v_{10}$; the two balls exchange velocities.
- $m_2\gg m_1$ and $v_{20}=0$: $v_1\approx-v_{10}$ and $v_2\approx0$; the small ball bounces back with its original speed.

A general one-dimensional collision is usually described by the coefficient of restitution $e=\dfrac{v_2-v_1}{v_{10}-v_{20}}$: $e=1$ for an elastic collision, $e=0$ for a perfectly inelastic collision, and $0<e<1$ for an inelastic collision. The kinetic energy lost in a perfectly inelastic collision is given in Section 4.10.3.

## 4.10. Work-Energy Relations in the Center-of-Mass Frame

### 4.10.1. König's Theorem

Let the total mass of a system of particles be $m=\sum_im_i$ and the velocity of its center of mass $\boldsymbol{v}_C$. In the **center-of-mass frame** $S'$ the velocities of the particles are $\boldsymbol{v}_i'$ with $\sum_im_i\boldsymbol{v}_i'=\boldsymbol{0}$; in the inertial frame $S$, $\boldsymbol{v}_i=\boldsymbol{v}_i'+\boldsymbol{v}_C$.

**Theorem 4.10.1 (König's Theorem)** The kinetic energy of a system of particles in an inertial frame equals its kinetic energy in the center-of-mass frame plus the kinetic energy of the center of mass:

$$
E_{\mathrm{k}}=E_{\mathrm{k}}'+E_{\mathrm{k}C},\qquad E_{\mathrm{k}}'=\sum_i\frac12m_iv_i'^2,\quad E_{\mathrm{k}C}=\frac12mv_C^2 .
$$

**Proof**

$$
E_{\mathrm{k}}=\sum_i\frac12m_i(\boldsymbol{v}_i'+\boldsymbol{v}_C)\cdot(\boldsymbol{v}_i'+\boldsymbol{v}_C)=\sum_i\frac12m_iv_i'^2+\Big(\sum_im_i\boldsymbol{v}_i'\Big)\cdot\boldsymbol{v}_C+\frac12\Big(\sum_im_i\Big)v_C^2,
$$
and the middle term vanishes. $\square$

### 4.10.2. The Work-Energy Principle in the Center-of-Mass Frame

**Theorem 4.10.2** In the center-of-mass frame, the work-energy principle and the law of conservation of mechanical energy still hold, and in the same form as in an inertial frame, whether or not the center-of-mass frame is inertial:

$$
\mathrm{d}W_{\mathrm{ext}}'+\mathrm{d}W_{\mathrm{nc,int}}'=\mathrm{d}E',\qquad W_{\mathrm{ext}}'+W_{\mathrm{nc,int}}'=\Delta E' .
$$

**Proof** This is evident when the center-of-mass frame is inertial. If the center-of-mass frame has **acceleration** $\boldsymbol{a}_C$, the work of the translational **inertial forces** $-m_i\boldsymbol{a}_C$ must also be included:

$$
\mathrm{d}W_{\mathrm{in}}'=\sum_i(-m_i\boldsymbol{a}_C)\cdot\mathrm{d}\boldsymbol{r}_i'=-\boldsymbol{a}_C\cdot\Big(\sum_im_i\boldsymbol{v}_i'\Big)\mathrm{d}t=-\boldsymbol{a}_C\cdot m\boldsymbol{v}_C'\,\mathrm{d}t=0,
$$
because the center of mass is at rest in the center-of-mass frame, $\boldsymbol{v}_C'=\boldsymbol{0}$. $\square$

Hence, if $\mathrm{d}W_{\mathrm{ext}}'=0$ and $\mathrm{d}W_{\mathrm{nc,int}}'=0$, the mechanical energy $E'$ in the center-of-mass frame is conserved.

### 4.10.3. Kinetic Energy of a Two-Particle System in the Center-of-Mass Frame

For two particles, $\boldsymbol{v}_C=\dfrac{m_1\boldsymbol{v}_1+m_2\boldsymbol{v}_2}{m_1+m_2}$, and by König's theorem

$$
E_{\mathrm{k}}'=E_{\mathrm{k}}-E_{\mathrm{k}C}=\frac12m_1v_1^2+\frac12m_2v_2^2-\frac{(m_1\boldsymbol{v}_1+m_2\boldsymbol{v}_2)^2}{2(m_1+m_2)}=\frac12\frac{m_1m_2}{m_1+m_2}\lvert\boldsymbol{v}_2-\boldsymbol{v}_1\rvert^2 .
$$

**Definition 4.10.1 (Reduced Mass)** The **reduced mass** of two particles is $\mu=\dfrac{m_1m_2}{m_1+m_2}$.

Write the **relative velocity** as $\boldsymbol{v}_{\mathrm{r}}=\boldsymbol{v}_2-\boldsymbol{v}_1$; then the kinetic energy of the two-particle system in the center-of-mass frame is $E_{\mathrm{k}}'=\frac12\mu v_{\mathrm{r}}^2$. In a perfectly inelastic collision the two bodies are at rest relative to each other afterward, while the kinetic energy $E_{\mathrm{k}C}$ of the center of mass is unchanged by conservation of momentum, so the kinetic energy lost is exactly $\frac12\mu v_{\mathrm{r}}^2$, the entire kinetic energy before the collision in the center-of-mass frame.

## 4.11. The Two-Body Problem

The problem of two bodies moving solely under their mutual interaction is called the *two-body problem*; examples are the scattering of an $\alpha$ particle by a nucleus, a planet orbiting the Sun, and binary stars. It can be reduced to a one-body problem.

Suppose the force between the two particles is a central force, and let $\boldsymbol{r}=\boldsymbol{r}_1-\boldsymbol{r}_2$ be the position vector of $m_1$ relative to $m_2$. In an inertial frame

$$
m_1\ddot{\boldsymbol{r}}_1=f(r)\boldsymbol{e}_r,\qquad m_2\ddot{\boldsymbol{r}}_2=-f(r)\boldsymbol{e}_r .
$$
Multiply the first equation by $m_2$ and the second by $m_1$ and subtract to get $m_1m_2(\ddot{\boldsymbol{r}}_1-\ddot{\boldsymbol{r}}_2)=(m_1+m_2)f(r)\boldsymbol{e}_r$, that is,

$$
\mu\ddot{\boldsymbol{r}}=f(r)\boldsymbol{e}_r .
$$

The motion of $m_1$ relative to $m_2$ is equivalent to the motion of a particle of mass $\mu$ acted on by the same force in the translating frame of $m_2$ (with $m_2$ as origin). This frame is not inertial, but once $m_1$ is replaced by $\mu$, Newton's second law still applies, and so do the theorems on momentum, angular momentum and energy: replacing $m_1$ by $\mu$ exactly accounts for the inertial force $-m_1\ddot{\boldsymbol{r}}_2$ acting on $m_1$. The original problem is thus decomposed into the uniform motion of the center of mass and the relative motion. For $m_2\gg m_1$, $\mu\approx m_1$, and we return to the case of a fixed force center (Section 4.7.5).

**Example 4.11.1** A proton moves head-on toward another proton at rest from far away with speed $v_0$. Find the distance of closest approach $r_{\min}$.

**Solution** Take the proton at rest as the origin. The reduced mass is $\mu=m_{\mathrm{p}}/2$, the interaction is the Coulomb repulsion, and the potential energy is $\dfrac{e^2}{4\pi\varepsilon_0r}$ ([5.3.1](/5.3.1)). In a head-on collision the angular momentum is zero and the relative velocity vanishes at closest approach; conservation of energy gives

$$
\frac12\mu v_0^2=\frac{e^2}{4\pi\varepsilon_0r_{\min}},\qquad r_{\min}=\frac{e^2}{\pi\varepsilon_0m_{\mathrm{p}}v_0^2} .
$$
This agrees with the equation of conservation of energy in the center-of-mass frame: at closest approach both protons are at rest relative to the center of mass, the kinetic energy of the center of mass is unchanged, and only the kinetic energy $\frac12\mu v_0^2$ in the center-of-mass frame can be converted into potential energy.

**Example 4.11.2** On a smooth horizontal plane, two small balls $m_1$ and $m_2$ are connected by a light string of length $l$. Initially the string is taut and the velocities $v_1$ and $v_2$ of the balls are in the same direction and perpendicular to the string. Find the tension $T$ in the string at this moment.

**Solution** In the translating frame of $m_2$, $m_1$ moves in a circle of radius $l$ about $m_2$ with relative speed $\lvert v_1-v_2\rvert$; write Newton's second law with the reduced mass:

$$
T=\mu\frac{(v_1-v_2)^2}{l}=\frac{m_1m_2}{m_1+m_2}\cdot\frac{(v_1-v_2)^2}{l}.
$$

## 4.12. Steady Flow of Fluids

A fluid is a special system of particles that can flow. As the simplest model, a fluid that is incompressible and has no viscosity (no internal friction between its parts, which can flow freely relative to one another) is called an *ideal fluid*.

**Definition 4.12.1** A flow in which the flow velocity at each point of the fluid does not change with time is called **steady flow**. In steady flow, a curve everywhere tangent to the flow velocity is called a **streamline**, and a thin tube bounded by streamlines is called a **stream tube**; fluid does not cross the side walls of a stream tube.

**Theorem 4.12.1 (Continuity Equation)** For steady flow of an ideal fluid, the flow velocities at any two cross sections $S_1$ and $S_2$ of the same stream tube satisfy

$$
S_1v_1=S_2v_2 .
$$

**Proof** The volume of fluid $S_1v_1\Delta t$ flowing through $S_1$ in $\Delta t$ must equal the volume $S_2v_2\Delta t$ flowing through $S_2$ (the fluid is incompressible, no fluid crosses the sides of the tube, and the volume of fluid between the two cross sections stays constant). $\square$

For a compressible fluid, conservation of mass gives $\rho_1S_1v_1=\rho_2S_2v_2$. The continuity equation is one form of conservation of mass; its differential form $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\boldsymbol{v})=0$ is the **conservation law** of [2.5.2](/2.5.2), obtained from the integral form by the **divergence theorem**.

## 4.13. Bernoulli's Equation

We use the work-energy principle to study the relation among pressure, flow velocity and height in steady flow. Take a segment of ideal fluid in a stream tube between cross sections $S_1$ and $S_2$, which moves in time $\Delta t$ to lie between $S_1'$ and $S_2'$. Since the flow is steady, the state of the fluid between $S_1'$ and $S_2$ is unchanged, and the net effect is that a mass $\Delta m=\rho S_1v_1\Delta t=\rho S_2v_2\Delta t$ of fluid has moved from section 1 (height $h_1$, flow velocity $v_1$, pressure $p_1$) to section 2. An ideal fluid has no viscosity, so no non-conservative internal force does work; among the external forces, the pressure forces at the two ends do work $p_1S_1v_1\Delta t-p_2S_2v_2\Delta t=(p_1-p_2)\Delta m/\rho$, and the pressure on the side walls is perpendicular to the flow and does no work. Taking the fluid and the Earth as the system, the work-energy principle gives

$$
\frac{(p_1-p_2)\Delta m}{\rho}=\Delta m\Big[\Big(\frac12v_2^2+gh_2\Big)-\Big(\frac12v_1^2+gh_1\Big)\Big].
$$

**Theorem 4.13.1 (Bernoulli's Equation)** For steady flow of an ideal fluid, along the same streamline

$$
p+\frac12\rho v^2+\rho gh=\text{const}.
$$

Bernoulli's equation is the law of conservation of mechanical energy for an ideal fluid: $\frac12\rho v^2$ and $\rho gh$ are the kinetic energy and gravitational potential energy per unit volume of fluid, and $p$ is the energy per unit volume that can be transferred by the work of pressure.

**Example 4.13.1 (Efflux Speed from a Small Hole)** An open bucket stands at rest with water depth $h$; find the flow velocity at the outlet after the tap at the bottom is opened. The water surface and the outlet are both in contact with the atmosphere at pressure $p_0$; the cross section of the bucket is much larger than that of the outlet, so by the continuity equation the speed at which the surface descends is approximately zero. Along the streamline from the surface to the outlet,

$$
p_0+\rho gh=p_0+\frac12\rho v^2,\qquad v=\sqrt{2gh},
$$
the same as the speed of a particle falling freely from height $h$ (Torricelli's law).

**Example 4.13.2 (Low Pressure Where the Flow Is Fast)** In a horizontal stream tube $h$ is the same everywhere, and $p_1+\frac12\rho v_1^2=p_2+\frac12\rho v_2^2$. By the continuity equation, the flow velocity is greater where the cross section is smaller, and the pressure is therefore lower. The Venturi flowmeter measures the flow rate from the pressure difference between two cross sections.

Several phenomena are often explained qualitatively by "low pressure where the flow is fast":

- Lift on a wing: the wing accelerates the air flow above it and decelerates the flow below, so the pressure above is lower than below. This statement is not wrong in itself, but the popular explanation that "the two streams of air must arrive at the trailing edge at the same time, so the one above is faster" is incorrect; a complete explanation of lift must take into account the deflection of the air flow by the wing (circulation).
- Two ships sailing side by side tend to approach each other: the water between the ships flows faster relative to the ships and is at lower pressure, so each ship experiences a net force toward the other.
- A spinning football ("banana kick") flies along a curve: the spin makes the air speeds on the two sides relative to the ball different, the pressure is lower on the side of higher speed, and the ball curves toward that side (the Magnus effect). The spin entrains the air through viscosity, so this is only a semi-quantitative explanation.

## Summary

| Concept or law | Content | Object | Relation to the reference frame |
|---|---|---|---|
| Work | $W=\int\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}$ | force and particle | depends |
| Work of a pair of forces | $W=\int\boldsymbol{f}_2\cdot\mathrm{d}\boldsymbol{r}_{21}$ | two particles | independent |
| Work-kinetic energy theorem | $W_{\mathrm{ext}}+W_{\mathrm{int}}=\Delta E_{\mathrm{k}}$ | particle, system of particles | holds in inertial frames |
| Potential energy | $-\Delta E_{\mathrm{p}}=W_{\mathrm{c,int}}$, $\boldsymbol{f}_{\mathrm{c}}=-\nabla E_{\mathrm{p}}$ | system | independent |
| Work-energy principle | $W_{\mathrm{ext}}+W_{\mathrm{nc,int}}=\Delta E$ | system | holds in inertial and center-of-mass frames |
| Conservation of mechanical energy | $E$ constant when only conservative internal forces do work | system | whether it is conserved depends on the choice of inertial frame |
| König's theorem | $E_{\mathrm{k}}=E_{\mathrm{k}}'+\frac12mv_C^2$ | system of particles | links inertial and center-of-mass frames |
| Bernoulli's equation | $p+\frac12\rho v^2+\rho gh=\text{const}$ | steady flow of an ideal fluid | the frame in which the fluid is at rest |

## Questions

1. Does the calculation of work depend on the reference frame? What about potential energy?

   **Answer** Work depends on the reference frame; potential energy is defined by the work of a pair of conservative forces and does not depend on the reference frame.

2. Does the conservation of mechanical energy depend on the choice of inertial frame?

   **Answer** Yes. For example, when a body slides down a smooth incline in a carriage moving at constant velocity, the support force of the incline does no work in the carriage frame and mechanical energy is conserved; in the ground frame the support force does work and the mechanical energy of the system (body plus Earth) is not conserved, unless the carriage is included in the system.

3. Does frictional heating depend on the reference frame?

   **Answer** No; it equals the negative of the work of the pair of sliding friction forces.

4. In Example 4.7.1, how does the force of the block on the ground vary while the block slides up?

   **Answer** The block has a downward vertical component of acceleration (it decelerates while rising), the vertical momentum of the system is decreasing, so the support force of the ground is smaller than $(m+M)g$.
