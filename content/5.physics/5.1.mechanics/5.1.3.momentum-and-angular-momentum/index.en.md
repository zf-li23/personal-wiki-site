---
title: Momentum and Angular Momentum
description: Impulse and the momentum theorem; the momentum theorem and conservation of momentum for systems of particles; variable-mass systems and the rocket equation; the center of mass, the center-of-mass motion theorem and the center-of-mass frame; angular momentum and torque of a particle and of a system, the angular momentum theorem, conservation of angular momentum and Kepler's second law; the angular momentum theorem in the center-of-mass frame.
source_hash: 74fadff212ac
---

**Newton's second law** ([5.1.2](/5.1.2)) is an instantaneous relation between force and **acceleration**. In many problems we care not about the force at each instant but about its cumulative effect over an interval: the accumulation of force over time changes the momentum of a body, and the accumulation of torque over time changes its angular momentum. In this chapter we derive the momentum theorem and the angular momentum theorem from Newton's laws and extend them to systems of **particles**. The internal forces of a system occur in pairs and cancel in the sum, which yields two conservation laws: the momentum of a system on which no external force acts is conserved, and the angular momentum of a system on which no external torque acts is conserved. They are more widely applicable than Newton's laws and remain valid in relativity ([5.1.8](/5.1.8)) and quantum physics ([5.5](/5.5)); by Noether's theorem they correspond to the translational and rotational symmetry of space, respectively ([5.1.4](/5.1.4)). The **center of mass** ([2.2.12](/2.2.12#def-12.5.1)) is the other central concept of this chapter: the overall motion of a system of particles resembles that of a single particle located at the center of mass and carrying the entire mass. The next chapter, [5.1.4](/5.1.4), discusses the accumulation of force over space (work) and energy, and [5.1.5](/5.1.5) applies the angular momentum theorem of this chapter to rigid bodies.

## 3.1. Impulse, Momentum and the Momentum Theorem for a Particle

### 3.1.1. The Momentum Theorem

**Definition 3.1.1 (Impulse)** The integral of a force $\boldsymbol{F}$ over time from $t_1$ to $t_2$,

$$
\boldsymbol{I} = \int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t,
$$
is called the **impulse** of the force during this interval.

**Definition 3.1.2 (Momentum)** The **momentum** of a particle of mass $m$ and **velocity** $\boldsymbol{v}$ is $\boldsymbol{p} = m\boldsymbol{v}$, with unit $\mathrm{kg\,m\,s^{-1}}$.

**Theorem 3.1.1 (Momentum Theorem for a Particle)** The impulse of the net force on a particle equals the change of its momentum:

$$
\boldsymbol{F} = \frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t}, \qquad \mathrm{d}\boldsymbol{I} = \boldsymbol{F}\,\mathrm{d}t = \mathrm{d}\boldsymbol{p}, \qquad
\boldsymbol{I} = \int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t = \boldsymbol{p}_2 - \boldsymbol{p}_1.
$$
The first two equations are the differential form, and the last is the integral form.

The differential form is the original form of Newton's second law ([5.1.2](/5.1.2#thm-2.1.2)). The advantage of the integral form is that in processes such as collisions and impacts, the force changes violently within a very short time and is hard to measure, whereas the change of momentum is easy to measure. Define the average impact force

$$
\bar{\boldsymbol{F}} = \frac{1}{t_2 - t_1}\int_{t_1}^{t_2}\boldsymbol{F}\,\mathrm{d}t = \frac{\Delta\boldsymbol{p}}{\Delta t};
$$
for the same change of momentum, the shorter the time of action, the greater the average impact force. Landing in a sandpit in the long jump and padding foam in packaging both lengthen the time of action to reduce the force.

**Example 3.1.1** A basketball of mass $m = 0.58\,\mathrm{kg}$ falls freely from a height $h = 2\,\mathrm{m}$ and rebounds from the floor with the same **speed**; the contact time is $\Delta t = 0.019\,\mathrm{s}$. Find the average force of the ball on the floor.

The speed of the ball on reaching the floor is $v = \sqrt{2gh} = \sqrt{2\times9.80\times2}\,\mathrm{m\,s^{-1}} = 6.26\,\mathrm{m\,s^{-1}}$, and the magnitude of the change of momentum across the contact is $2mv$. Neglecting gravity during the contact (about $5.7\,\mathrm{N}$),

$$
\bar F = \frac{2mv}{\Delta t} = \frac{2\times0.58\times6.26}{0.019}\,\mathrm{N} \approx 3.8\times10^2\,\mathrm{N},
$$
about 67 times the weight of the ball. By **Newton's third law**, the average force of the ball on the floor is equal and opposite to this.

**Example 3.1.2** A heavy ball has an identical thin thread tied to its top and to its bottom. The ball is hung from the upper thread, and the lower thread is pulled downward by hand. If the force is applied slowly, the upper thread breaks first: its tension equals the weight of the ball plus the applied force and is always greater than that in the lower thread. If the pull is a sudden jerk, the lower thread breaks first: the time of action is very short and the impulse is small, so the ball hardly has time to move, the stretch (and hence the tension) of the upper thread barely changes, while the tension of the lower thread has already reached the breaking strength within this very short time. Which thread breaks first depends on the magnitude and the speed of the pull, not only on their product.

**Example 3.1.3 (Sailing Against the Wind)** A sailboat can sail obliquely against the wind. Seen from above, the wind blowing on the slanted sail is deflected along the sail, and its momentum changes by $\Delta\boldsymbol{p}$; by the momentum theorem the force of the sail on the wind is in the direction of $\Delta\boldsymbol{p}$, so the force of the wind on the sail is opposite to it, roughly perpendicular to the sail. Resolve this force into a component along the hull and one perpendicular to the hull: the former drives the boat forward, and the latter is balanced by the lateral resistance of the water on the keel. If the sail is properly oriented, the component along the hull points forward, and the boat can advance at some angle against the wind, then reach a point upwind along a zigzag course.

### 3.1.2. Radiation Pressure and Optical Tweezers

Light also carries momentum. A photon of frequency $\nu$ and wavelength $\lambda$ has momentum $p = \dfrac{h\nu}{c} = \dfrac{h}{\lambda}$ ([5.5](/5.5)); when light is absorbed, reflected or refracted by a body, its momentum changes and the body experiences a force, which is the radiation pressure. The radiation pressure of sunlight is extremely small, but a focused laser can exert considerable forces on particles of micrometer and nanometer size.

When a laser beam is refracted by a small transparent particle (with relatively weak reflection), its direction of propagation changes, the momentum of the light changes, and the particle experiences a force in the opposite direction. For a focused beam that is intense at the center and weak at the periphery, the net force on a particle displaced from the focus points toward the focus, so the particle is "trapped" near the focus; this is the optical tweezers. With optical tweezers one can capture and move cells and bacteria, or stretch a DNA molecule to measure its elasticity. Ashkin received the 2018 Nobel Prize in Physics for the invention of optical tweezers and their application to biological systems; work on cooling and trapping atoms with laser light received the 1997 Nobel Prize in Physics (Chu, Cohen-Tannoudji, Phillips).

## 3.2. The Momentum Theorem for a System of Particles

A system composed of several interacting particles is called a system of particles. Forces exerted on particles in the system by bodies outside it are called external forces, and the interaction forces between particles inside the system are called internal forces.

Let particle $i$ be acted on by an external force $\boldsymbol{F}_i$ and by internal forces $\boldsymbol{f}_{ij}$ from particles $j$, and let its momentum be $\boldsymbol{p}_i$. Applying the momentum theorem to each particle,

$$
\Big(\boldsymbol{F}_i + \sum_{j\ne i}\boldsymbol{f}_{ij}\Big)\,\mathrm{d}t = \mathrm{d}\boldsymbol{p}_i.
$$
Sum over all particles. By Newton's third law $\boldsymbol{f}_{ij} = -\boldsymbol{f}_{ji}$, the internal forces cancel in pairs, $\sum_i\sum_{j\ne i}\boldsymbol{f}_{ij} = \boldsymbol{0}$. Write the net external force as $\boldsymbol{F}_{\mathrm{ext}} = \sum_i\boldsymbol{F}_i$ and the total momentum of the system as $\boldsymbol{P} = \sum_i\boldsymbol{p}_i$; then:

**Theorem 3.2.1 (Momentum Theorem for a System of Particles)** The impulse of the net external force on a system of particles equals the change of the total momentum of the system:

$$
\boldsymbol{F}_{\mathrm{ext}} = \frac{\mathrm{d}\boldsymbol{P}}{\mathrm{d}t}, \qquad \int_{t_1}^{t_2}\boldsymbol{F}_{\mathrm{ext}}\,\mathrm{d}t = \boldsymbol{P}_2 - \boldsymbol{P}_1.
$$

The total momentum of the system is determined only by the impulse of the external forces and is independent of the internal forces. Internal forces can transfer momentum within the system but cannot change the total momentum. Applying the momentum theorem for a system of particles therefore allows us to bypass the internal forces, which are often unknown.

## 3.3. Conservation of Momentum

**Theorem 3.3.1 (Law of Conservation of Momentum)** When the net external force on a system of particles is zero, the total momentum of the system does not change with time:

$$
\boldsymbol{F}_{\mathrm{ext}} = \boldsymbol{0} \quad\Longrightarrow\quad \boldsymbol{P} = \sum_i m_i\boldsymbol{v}_i = \text{constant vector}.
$$

Some remarks:

1. In Newtonian mechanics, conservation of momentum is a consequence of Newton's second and third laws. But its range of validity is wider than that of Newton's laws: it remains valid in relativity and quantum physics, and in electromagnetic interactions for which Newton's third law fails (when the momentum of the electromagnetic field is included). It is one of the most fundamental laws of physics, and its root is the translational symmetry of space ([5.1.4](/5.1.4)).
2. The momentum theorem and the conservation of momentum apply only in **inertial frames**; if momentum is conserved in one inertial frame, it is conserved in all other inertial frames (the velocities of all particles differ by the same constant vector, so the total momentum differs by a constant vector).
3. If the net external force is not zero but its component in some direction is zero, the component of the total momentum in that direction is conserved.
4. When the external forces are much smaller than the internal forces and the time of action is very short (as in collisions and explosions), the impulse of the external forces can be neglected and the momentum of the system is approximately conserved.
5. When solving problems with conservation laws, one must specify the system chosen and the process studied, and check the conditions for conservation.

**Example 3.3.1** A wedge of mass $M$ rests on a smooth horizontal plane, and the horizontal width of its incline is $d$. A small block of mass $m$ slides from rest from the top of the incline. Find the distance the wedge moves horizontally when the block reaches the bottom. Is the result the same whether the incline is straight, concave or convex?

Take the block and the wedge as the system. No external force acts on the system horizontally, so the horizontal momentum is conserved, and it is initially zero. Let the horizontal velocities of the block and the wedge at any instant be $v_x$ (positive toward the bottom of the incline) and $-V$; then $mv_x - MV = 0$. Integrating over time, the magnitudes of the horizontal **displacements** of the block and the wedge satisfy $mX_m = MX_M$; the horizontal displacement of the block relative to the wedge is $d$, so $X_m + X_M = d$ and

$$
X_M = \frac{m}{m + M}\,d.
$$
This result is independent of the shape of the incline, as long as the initial relative position of the block and the wedge is the same. If the incline is not smooth, friction is an internal force of the system, the horizontal momentum is still conserved and the result is unchanged (as long as the block can slide to the bottom); if the floor is not smooth, the system is acted on by a horizontal external force, the horizontal momentum is not conserved and the result changes.

## 3.4. Variable-Mass Systems and the Principle of Rocket Flight

At low speeds there are two kinds of variable-mass problems: the mass of the main body increases by accretion (a rolling snowball, a raindrop falling through a cloud), or decreases by ejection (a rocket). In both, the method is to take the main body together with the mass it accretes or ejects during $\mathrm{d}t$ as the system, and apply the momentum theorem to this system of constant mass. We take the rocket as the example below. Momentum and energy at high speeds are treated in [5.1.8](/5.1.8), where the mass is always an invariant mass.

### 3.4.1. A Rocket in Free Space

A rocket flies in free space far from any celestial body and is subject to no external force. Take the ground (an inertial frame) as the **reference frame**, and take the rocket body together with the fuel still remaining in it at time $t$ as the system, with mass $m$ and velocity $v$. Let the gas produced by burning the fuel be ejected backward with constant speed $u$ relative to the rocket.

- At time $t$: the momentum of the system is $mv$.
- At time $t + \mathrm{d}t$: the ejected gas has mass $-\mathrm{d}m > 0$ ($\mathrm{d}m < 0$ is the change of the mass of the rocket) and velocity $v - u$; the remaining part has mass $m + \mathrm{d}m$ and velocity $v + \mathrm{d}v$.

By conservation of momentum,

$$
mv = (m + \mathrm{d}m)(v + \mathrm{d}v) + (-\mathrm{d}m)(v - u).
$$
Neglecting the second-order quantity $\mathrm{d}m\,\mathrm{d}v$ gives $m\,\mathrm{d}v = -u\,\mathrm{d}m$, a **separable equation**. Integrating from the initial state (mass $m_{\mathrm{i}}$, velocity $v_{\mathrm{i}}$) to burnout (mass $m_{\mathrm{f}}$, velocity $v_{\mathrm{f}}$):

**Formula 3.4.1 (Tsiolkovsky Rocket Equation)**

$$
v_{\mathrm{f}} = v_{\mathrm{i}} + u\ln\frac{m_{\mathrm{i}}}{m_{\mathrm{f}}} = v_{\mathrm{i}} + u\ln N,
$$
where $N = m_{\mathrm{i}}/m_{\mathrm{f}}$ is called the mass ratio of the rocket.

The velocity gained by the rocket is independent of how fast the fuel burns and depends only on the exhaust speed and the mass ratio. There are two ways to raise the final velocity:

1. Increase the exhaust speed $u$: among chemical rockets, liquid hydrogen and liquid oxygen engines give the highest, about $4.5\,\mathrm{km\,s^{-1}}$ in vacuum.
2. Increase the mass ratio $N$: the velocity gain grows only logarithmically with $N$, and increasing $N$ indefinitely is not worthwhile for a single-stage rocket, because the mass of the structure (fuel tanks, engines and so on) cannot be shed. Multistage rockets are therefore used, discarding the casing of each stage when its fuel is used up. The final velocity of a three-stage rocket is

$$
v = u_1\ln N_1 + u_2\ln N_2 + u_3\ln N_3,
$$
where $N_k$ is the ratio of the mass of stage $k$ at ignition to its mass at burnout.

### 3.4.2. The Thrust of a Rocket

Take the gas ejected during $\mathrm{d}t$ (mass $-\mathrm{d}m$) as the object. At time $t$ it moves with the rocket, with momentum $-\mathrm{d}m\cdot v$; at time $t + \mathrm{d}t$ its velocity is $v - u$ and its momentum is $-\mathrm{d}m\cdot(v - u)$. By the momentum theorem, the force of the rocket on this gas satisfies

$$
F_{\text{rocket on gas}}\,\mathrm{d}t = -\mathrm{d}m\,(v - u) - (-\mathrm{d}m)\,v = u\,\mathrm{d}m,
$$
that is, the force of the rocket on the gas points backward. By Newton's third law, the thrust of the gas on the rocket points forward, with magnitude

$$
F = u\left\lvert\frac{\mathrm{d}m}{\mathrm{d}t}\right\rvert = uq_m,
$$
where $q_m$ is the mass of exhaust gas ejected per unit time. The thrust equals the product of the exhaust speed and the mass flow rate.

### 3.4.3. Vertical Launch in a Gravitational Field

For a vertical launch near the ground, the system is acted on by the external force $-mg$ (neglecting the variation of $g$ and air resistance). Applying the momentum theorem to the system of Section 3.4.1, $\mathrm{d}(\text{momentum}) = -mg\,\mathrm{d}t$, gives $m\,\mathrm{d}v = -u\,\mathrm{d}m - mg\,\mathrm{d}t$, and integrating gives the velocity of the rocket at time $t$,

$$
v(t) = v_{\mathrm{i}} - gt + u\ln\frac{m_{\mathrm{i}}}{m(t)},
$$
where $m(t)$ is the mass of the rocket and the remaining fuel at time $t$. The condition for the rocket to leave the ground is that the thrust exceed the weight, $uq_m > m_{\mathrm{i}}g$; the longer the burn, the greater the velocity loss $gt$ due to gravity, so launch vehicles burn their fuel as fast as possible.

## 3.5. The Center of Mass

### 3.5.1. Definition of the Center of Mass

**Definition 3.5.1 (Center of Mass)** Let particle $i$ of a system of particles have mass $m_i$ and **position vector** $\boldsymbol{r}_i$, and let the total mass be $m = \sum_im_i$. The point $C$ with position vector

$$
\boldsymbol{r}_C = \frac{\sum_im_i\boldsymbol{r}_i}{m}
$$
is called the **center of mass** of the system. In components, $x_C = \dfrac{\sum_im_ix_i}{m}$, and similarly for $y_C$ and $z_C$.

The position of the center of mass is the mass-weighted average of the positions of the particles, and it does not depend on the choice of origin (when the origin is shifted, $\boldsymbol{r}_C$ and all the $\boldsymbol{r}_i$ change by the same vector). For a body with continuously distributed mass, the sum is replaced by an integral:

$$
\boldsymbol{r}_C = \frac{1}{m}\int\boldsymbol{r}\,\mathrm{d}m, \qquad x_C = \frac1m\int x\,\mathrm{d}m, \ \dots
$$
This is the center of mass defined by a multiple integral in [2.2.12](/2.2.12#def-12.5.1), with $\mathrm{d}m = \rho\,\mathrm{d}V$ (and $\mathrm{d}m = \sigma\,\mathrm{d}S$ or $\lambda\,\mathrm{d}l$ for surface and line distributions).

Some common cases:

- Two particles: the center of mass lies on the line joining them, at distances $r_1$ and $r_2$ from them satisfying $m_1r_1 = m_2r_2$, so it is closer to the more massive particle.
- A body of uniformly distributed mass and symmetric shape (rod, disk, ring, sphere) has its center of mass at the geometric center.
- For a body of modest size, the gravitational acceleration is the same everywhere, the resultant of gravity acts at the center of mass, and the center of mass coincides with the center of gravity.
- The center of mass need not lie in the body: that of a ring, or of a wire bent into an arc, lies outside the body.

**Example 3.5.1** A small disk of radius $r$ is cut out of a uniform disk of radius $R$, with the centers a distance $d$ apart. Find the center of mass of the remaining part.

Take the center $O$ of the large disk as the origin and the $x$ axis pointing to the center $O'$ of the small disk. By symmetry, the center of mass lies on the $x$ axis. Let the surface density be $\sigma$. The remaining disk and the small disk together make up the complete large disk, whose center of mass is at $O$; regard the removed part as a disk of negative mass superposed on the large disk:

$$
x_C = \frac{\sigma\pi R^2\cdot0 - \sigma\pi r^2\cdot d}{\sigma\pi R^2 - \sigma\pi r^2} = -\frac{d}{(R/r)^2 - 1}.
$$
The center of mass is on the other side of $O$, away from the side that was cut out.

**Example 3.5.2** A uniform wire is bent into a semicircle of radius $R$. Find its center of mass.

Take the center of the circle as the origin and the axis of symmetry as the $y$ axis. By symmetry $x_C = 0$. Let the linear density be $\lambda$ and take a small segment subtending angle $\mathrm{d}\theta$, with $\mathrm{d}m = \lambda R\,\mathrm{d}\theta$ and $y = R\sin\theta$; the total mass is $m = \pi R\lambda$:

$$
y_C = \frac{1}{m}\int_0^\pi R\sin\theta\cdot\lambda R\,\mathrm{d}\theta = \frac{2R^2\lambda}{\pi R\lambda} = \frac{2R}{\pi}.
$$
The center of mass is not on the wire.

## 3.6. The Center-of-Mass Motion Theorem

### 3.6.1. The Center-of-Mass Motion Theorem

Differentiating the position vector of the center of mass, its velocity is

$$
\boldsymbol{v}_C = \frac{\mathrm{d}\boldsymbol{r}_C}{\mathrm{d}t} = \frac{\sum_im_i\boldsymbol{v}_i}{m},
$$
the weighted average of the velocities of the particles. The total momentum of the system is then

$$
\boldsymbol{P} = \sum_im_i\boldsymbol{v}_i = m\boldsymbol{v}_C,
$$
equal to the momentum of a single particle carrying the entire mass at the center of mass and moving with the velocity of the center of mass. Substituting into the momentum theorem for a system of particles (Theorem 3.2.1):

**Theorem 3.6.1 (Center-of-Mass Motion Theorem)** The product of the total mass of a system of particles and the acceleration of its center of mass equals the net external force on the system:

$$
\boldsymbol{F}_{\mathrm{ext}} = \frac{\mathrm{d}\boldsymbol{P}}{\mathrm{d}t} = m\frac{\mathrm{d}\boldsymbol{v}_C}{\mathrm{d}t} = m\boldsymbol{a}_C.
$$

The center of mass moves like a single particle located at the center of mass, carrying the entire mass of the system and acted on by all the external forces. What is usually called the "motion of a body" is in fact the motion of its center of mass; this is also the strict meaning of treating a body as a particle ([5.1.1](/5.1.1)). Internal forces do not affect the motion of the center of mass:

- A wrench spinning as it slides on a smooth horizontal surface has a very complicated motion of its points, but its center of mass moves in a straight line at constant speed;
- A diver somersaulting in the air still has a center of mass that follows a parabola;
- When a fireworks shell explodes in the air and the fragments scatter, the center of mass of the whole still follows the original parabola until the fragments land.

**Example 3.6.1** Each rotor blade of a helicopter has length $L = 5.97\,\mathrm{m}$, and may be treated as a thin strip of constant width and uniform thickness. When the rotor turns at $400\,\mathrm{r/min}$, how many times the weight of the blade is the tension at the root of the blade?

The center of mass of the blade is at distance $L/2$ from the axis; it moves in uniform circular motion with **angular velocity** $\omega = 400\times2\pi/60\,\mathrm{rad\,s^{-1}} = 41.9\,\mathrm{rad\,s^{-1}}$, and its acceleration $a_C = \omega^2L/2$ points toward the axis. In the horizontal direction the blade is acted on only by the tension at the root (gravity and aerodynamic forces being neglected by comparison). By the center-of-mass motion theorem,

$$
F = ma_C = m\omega^2\frac L2, \qquad \frac{F}{mg} = \frac{\omega^2L}{2g} = \frac{41.9^2\times5.97}{2\times9.8} \approx 5.3\times10^2.
$$
The tension at the root of the blade is more than five hundred times its weight. Note that the center-of-mass motion theorem is used here in the inertial ground frame, not by solving in the center-of-mass frame.

**Example 3.6.2** A person of mass $m_1 = 50\,\mathrm{kg}$ stands at the bow of a boat of mass $m_2 = 200\,\mathrm{kg}$ and length $l = 4\,\mathrm{m}$; initially both the person and the boat are at rest. Neglecting the resistance of the water, find the distance the boat moves when the person walks to the stern.

The system of person and boat is subject to no horizontal external force, so the horizontal velocity of the center of mass remains zero and its position does not change:

$$
\frac{m_1x_1 + m_2x_2}{m_1 + m_2} = \frac{m_1x'_1 + m_2x'_2}{m_1 + m_2} \quad\Longrightarrow\quad m_1(x_1 - x'_1) = m_2(x'_2 - x_2).
$$
Let the boat move forward (toward the bow) by $d$; then the person moves backward by $l - d$ relative to the ground, so $m_1(l - d) = m_2d$ and

$$
d = \frac{m_1}{m_1 + m_2}\,l = \frac{50}{250}\times4\,\mathrm{m} = 0.8\,\mathrm{m}.
$$

### 3.6.2. Conservation of Momentum and the Motion of the Center of Mass

From $\boldsymbol{P} = m\boldsymbol{v}_C$: when the net external force is zero, $\boldsymbol{a}_C = \boldsymbol{0}$ and $\boldsymbol{v}_C$ is a constant vector; when the component of the net external force in some direction is zero, the component of the center-of-mass velocity in that direction does not change (for example, $\sum_iF_{ix} = 0 \Rightarrow v_{Cx}$ is constant). Conservation of momentum of a system of particles is therefore equivalent to the center of mass moving uniformly in a straight line (or being at rest). Examples 3.3.1 and 3.6.2 treat the same kind of problem in these two ways.

### 3.6.3. The Center-of-Mass Frame

**Definition 3.6.1 (Center-of-Mass Frame)** The reference frame with the center of mass as origin and translating with it is called the **center-of-mass frame**.

When the center of mass accelerates, the center-of-mass frame is a translating **non-inertial frame** (Section 2.6.2 of [5.1.2](/5.1.2)). The complicated motion of a system of particles can be regarded as the combination of two parts:

1. the translation of the whole system with the center of mass, determined by the center-of-mass motion theorem;
2. the motion of the particles relative to the center of mass, to be examined in the center-of-mass frame.

**Theorem 3.6.2 (The Center-of-Mass Frame Is the Zero-Momentum Frame)** In the center-of-mass frame the total momentum of the system of particles is zero: $\sum_im_i\boldsymbol{v}'_i = \boldsymbol{0}$, where $\boldsymbol{v}'_i = \boldsymbol{v}_i - \boldsymbol{v}_C$ is the velocity of particle $i$ relative to the center-of-mass frame.

**Proof** $\sum_im_i\boldsymbol{v}'_i = \sum_im_i\boldsymbol{v}_i - \Big(\sum_im_i\Big)\boldsymbol{v}_C = m\boldsymbol{v}_C - m\boldsymbol{v}_C = \boldsymbol{0}$. Likewise $\sum_im_i\boldsymbol{r}'_i = \boldsymbol{0}$, with $\boldsymbol{r}'_i = \boldsymbol{r}_i - \boldsymbol{r}_C$. $\square$

The center-of-mass frame is therefore also called the zero-momentum frame. For a system of two particles in the center-of-mass frame, the momenta of the two are always equal and opposite, which makes collision problems particularly simple in the center-of-mass frame ([5.1.4](/5.1.4)).

**Example 3.6.3** A long flexible rope of linear density $\lambda$ lies coiled on the ground, and one end is lifted vertically upward by a hand with force $F$. Let the length of the lifted part be $y$. Find $F$ (1) when it is lifted at constant speed $v$; (2) when it is lifted from rest with constant acceleration $a$.

This problem can be treated as a variable-mass problem or with the center-of-mass motion theorem. Take the whole rope (length $l$) as the system, with the origin on the ground and the $y$ axis vertically upward. The center of mass of the lifted part is at $y/2$ and that of the part remaining on the ground is at height zero, so the center-of-mass coordinate of the whole rope is

$$
y_C = \frac{\lambda y\cdot\frac y2 + 0}{\lambda l} = \frac{y^2}{2l}.
$$
The external forces on the whole rope are the tension $F$, the weight $\lambda lg$, and the support force of the ground on the part remaining on the ground, $\lambda(l - y)g$. By the center-of-mass motion theorem,

$$
\lambda l\,\ddot y_C = F + \lambda(l - y)g - \lambda lg = F - \lambda yg, \qquad \ddot y_C = \frac{\dot y^2 + y\ddot y}{l},
$$
so $F = \lambda yg + \lambda(\dot y^2 + y\ddot y)$.

(1) $\dot y = v$, $\ddot y = 0$: $F = \lambda yg + \lambda v^2$. Besides the weight of the lifted part, an extra $\lambda v^2$ is needed to keep giving speed $v$ to segments of rope that were at rest.

(2) $\ddot y = a$, $\dot y^2 = 2ay$: $F = \lambda yg + 3\lambda ya$.

## 3.7. Angular Momentum of a Particle

### 3.7.1. Angular Momentum

For a particle moving about a point, momentum alone does not characterize the strength of the rotation: for the same momentum, the farther from the center of rotation, the greater the "amount of rotation."

**Definition 3.7.1 (Angular Momentum)** Let a particle of mass $m$ have position vector $\boldsymbol{r}$ relative to a reference point $O$ and momentum $\boldsymbol{p} = m\boldsymbol{v}$. Its **angular momentum** about $O$ is

$$
\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p} = \boldsymbol{r}\times(m\boldsymbol{v}).
$$
Its magnitude is $L = rp\sin\alpha = rmv\sin\alpha$ ($\alpha$ is the angle between $\boldsymbol{r}$ and $\boldsymbol{p}$), and its direction is perpendicular to the plane of $\boldsymbol{r}$ and $\boldsymbol{p}$, given by the right-hand rule. The unit is $\mathrm{kg\,m^2\,s^{-1}}$.

The reference point $O$ is a fixed point in the chosen reference frame. For a particle moving with speed $v$ on a circle of radius $R$, the angular momentum about the center has magnitude $L = mvR$ and a fixed direction perpendicular to the plane of the circle. The angular momentum generally depends on the reference point, so a reference point must always be specified. Take a conical pendulum as an example: the pendulum has length $l$, the string makes an angle $\alpha$ with the vertical, and the bob moves in a horizontal circle with speed $v$.

- About the suspension point $O$: $\boldsymbol{r}$ is along the string, has length $l$ and is perpendicular to $\boldsymbol{v}$, so $L_O = lmv$; its direction is perpendicular to the string and the velocity and changes continually as the bob circles the vertical axis.
- About the center $O'$ of the circle: $L_{O'} = mvl\sin\alpha$, directed vertically upward and constant.

### 3.7.2. Torque and the Angular Momentum Theorem

Differentiate the angular momentum, using the differentiation rule for the cross product ([2.2.11](/2.2.11#thm-11.3.1)):

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t} = \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}\times\boldsymbol{p} + \boldsymbol{r}\times\frac{\mathrm{d}\boldsymbol{p}}{\mathrm{d}t} = \boldsymbol{v}\times m\boldsymbol{v} + \boldsymbol{r}\times\boldsymbol{F} = \boldsymbol{r}\times\boldsymbol{F}.
$$

**Definition 3.7.2 (Torque)** A force $\boldsymbol{F}$ acts on a particle with position vector $\boldsymbol{r}$ (relative to a reference point $O$). Its **torque** about $O$ is

$$
\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F},
$$
with magnitude $M = rF\sin\alpha = r_0F$, where $r_0 = r\sin\alpha$ is the distance from $O$ to the line of action of the force, called the lever arm. The unit is $\mathrm{N\,m}$.

**Theorem 3.7.1 (Angular Momentum Theorem for a Particle)** The net torque on a particle equals the rate of change of its angular momentum; for the same reference point,

$$
\boldsymbol{M} = \frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t}, \qquad \int_{t_1}^{t_2}\boldsymbol{M}\,\mathrm{d}t = \boldsymbol{L}_2 - \boldsymbol{L}_1.
$$

**Definition 3.7.3 (Angular Impulse)** The integral of torque over time, $\displaystyle\int_{t_1}^{t_2}\boldsymbol{M}\,\mathrm{d}t$, is called the **angular impulse**; it is the cumulative effect of torque over time.

The angular momentum theorem has the same form as the momentum theorem: force $\leftrightarrow$ torque, momentum $\leftrightarrow$ angular momentum, impulse $\leftrightarrow$ angular impulse. Note that torque and angular momentum must be computed about the same reference point.

**Example 3.7.1 (Angular Momentum of a Conical Pendulum)** About the suspension point $O$: the tension $\boldsymbol{F}_{\mathrm{T}}$ in the string passes through $O$, so its torque is zero; the torque of gravity has magnitude $l\sin\alpha\cdot mg$ and is horizontal and nonzero, so $\boldsymbol{L}_O$ changes continually, consistent with the change of direction of $\boldsymbol{L}_O$ with the motion of the bob seen above. About the center $O'$: the torques of the tension and of gravity are equal in magnitude and opposite in direction, so the net torque is zero and both the magnitude and the direction of $\boldsymbol{L}_{O'}$ stay unchanged. Yet the net force on the bob (directed toward the center) is not zero, and the momentum keeps changing. The conditions for conservation of momentum and of angular momentum are evidently different.

### 3.7.3. Torque and Angular Momentum About a Fixed Axis

When a rigid body rotates about a fixed axis ([5.1.5](/5.1.5)), only the component along the axis matters. Take the $z$ axis through the reference point $O$, and resolve $\boldsymbol{r}$ and $\boldsymbol{F}$ into components $\boldsymbol{r}_\parallel$, $\boldsymbol{F}_\parallel$ parallel to the $z$ axis and components $\boldsymbol{r}_\perp$, $\boldsymbol{F}_\perp$ perpendicular to it. Since $\boldsymbol{r}_\parallel\times\boldsymbol{F}_\parallel = \boldsymbol{0}$ and both $\boldsymbol{r}_\parallel\times\boldsymbol{F}_\perp$ and $\boldsymbol{r}_\perp\times\boldsymbol{F}_\parallel$ are perpendicular to the $z$ axis,

$$
M_z = (\boldsymbol{r}\times\boldsymbol{F})\cdot\boldsymbol{e}_z = (\boldsymbol{r}_\perp\times\boldsymbol{F}_\perp)\cdot\boldsymbol{e}_z = \pm F_\perp r_\perp\sin\alpha,
$$
where $\alpha$ is the angle between $\boldsymbol{r}_\perp$ and $\boldsymbol{F}_\perp$, and the sign is determined by the sense of rotation through the right-hand rule.

**Definition 3.7.4 (Torque and Angular Momentum About an Axis)** The projections of the torque $\boldsymbol{M}$ and the angular momentum $\boldsymbol{L}$ on the $z$ axis through the reference point, $M_z = \boldsymbol{M}\cdot\boldsymbol{e}_z$ and $L_z = \boldsymbol{L}\cdot\boldsymbol{e}_z = (\boldsymbol{r}_\perp\times\boldsymbol{p}_\perp)\cdot\boldsymbol{e}_z$, are called the torque of the force about the $z$ axis and the angular momentum of the particle about the $z$ axis, respectively. They do not depend on the position of the reference point on the axis.

Since $\boldsymbol{e}_z$ has a fixed direction, taking the $z$ component of both sides of the angular momentum theorem gives the angular momentum theorem for a particle about a fixed axis,

$$
M_z = \frac{\mathrm{d}L_z}{\mathrm{d}t}.
$$
Forces parallel to the axis and forces passing through the axis have zero torque about the axis.

## 3.8. Conservation of Angular Momentum

**Theorem 3.8.1 (Law of Conservation of Angular Momentum)** When the net torque on a particle is zero, the angular momentum of the particle stays constant:

$$
\boldsymbol{M} = \boldsymbol{0} \quad\Longrightarrow\quad \boldsymbol{L} = \text{constant vector}.
$$
If only the component of the net torque about some axis vanishes, $M_z = 0$, then the angular momentum of the particle about that axis is conserved, and $L_z$ is constant.

There are two ways to have $\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F} = \boldsymbol{0}$: the net force is zero, or the net force always passes through the reference point $O$. In the latter case the line of action of the force always passes through a fixed point; such a force is called a central force ([5.1.4](/5.1.4)), like the gravitational force of the Sun on a planet or the Coulomb force of the nucleus on an electron. A particle moving under a central force conserves its angular momentum about the force center. Like conservation of momentum, conservation of angular momentum is one of the fundamental laws of physics.

**Example 3.8.1 (Kepler's Second Law)** The gravitational force of the Sun on a planet always points toward the Sun, so the angular momentum $\boldsymbol{L} = \boldsymbol{r}\times m\boldsymbol{v}$ of the planet about the Sun is conserved. Two conclusions follow:

1. The direction of $\boldsymbol{L}$ is fixed, and $\boldsymbol{r}$ and $\boldsymbol{v}$ always lie in the same plane perpendicular to $\boldsymbol{L}$; the orbit of the planet is a plane curve.
2. The magnitude of $\boldsymbol{L}$ is constant. The area swept by the position vector of the planet in $\mathrm{d}t$ is that of the triangle with sides $\boldsymbol{r}$ and $\boldsymbol{v}\,\mathrm{d}t$, $\mathrm{d}S = \frac12\lvert\boldsymbol{r}\times\boldsymbol{v}\,\mathrm{d}t\rvert$, so the area swept per unit time (the areal velocity)

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = \frac12rv\sin\alpha = \frac{L}{2m}
$$
is constant: the line joining the planet and the Sun sweeps out equal areas in equal times. This is *Kepler's second law*. In polar coordinates, $\dfrac{\mathrm{d}S}{\mathrm{d}t} = \frac12r^2\dot\theta$, which is the same statement as the vanishing of the transverse component of the acceleration, $a_\theta = \dfrac1r\dfrac{\mathrm{d}}{\mathrm{d}t}(r^2\dot\theta) = 0$, in Section 1.6 of [5.1.1](/5.1.1).

This conclusion uses only that the force is central and is independent of how the force varies with distance; that the orbit is an ellipse (Kepler's first law) depends on the force being inversely proportional to the square of the distance ([5.1.4](/5.1.4)).

![Orbit under an inverse-square central force (eccentricity 0.6), computed numerically with solve_ivp. Left: the sectors swept out by the position vector in equal time intervals have equal areas; near perihelion they are short and wide, near aphelion long and narrow. Right: the speed varies greatly with time while the areal velocity stays constant](./plots/kepler-equal-areas.py)

**Example 3.8.2 (The Disk Structure of Galaxies)** Many galaxies and protoplanetary clouds are flat disks. A qualitative explanation is as follows. Let a slowly rotating mass of matter contract under its own gravity, and take the axis of rotation as the $z$ axis. A part of it of mass $m$ is initially at distance $r_0$ from the axis and moves around the axis with speed $v_0$. The gravitational force points toward the center and its torque about the $z$ axis is approximately zero, so $L_z = mv_0r_0$ is conserved; when it has contracted to distance $r$, its speed is $v = \dfrac{v_0r_0}{r} \propto r^{-1}$, and the centripetal force needed to maintain circular motion is

$$
F_{\mathrm{c}} = \frac{mv^2}{r} \propto r^{-3},
$$
while gravity is approximately $\propto r^{-2}$. As $r$ decreases, the required centripetal force grows faster than gravity, and the radial contraction stops when $F_{\mathrm{c}}$ equals gravity; there is no such limit along the $z$ direction, and matter can continue to contract under gravity. The result is a flat disk rotating about the $z$ axis. In reality, the matter must also dissipate the energy of its motion along the $z$ direction through gas collisions in order to settle onto the plane of the disk. The scales of galaxies are often expressed in parsecs, $1\,\mathrm{pc} = 3.086\times10^{16}\,\mathrm{m}$.

## 3.9. Angular Momentum of a System of Particles

**Definition 3.9.1 (Angular Momentum of a System of Particles)** The angular momentum of a system of particles about a reference point $O$ is the vector sum of the angular momenta of the particles about $O$, $\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times\boldsymbol{p}_i$.

Applying the angular momentum theorem to each particle and summing:

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t} = \sum_i\boldsymbol{r}_i\times\Big(\boldsymbol{F}_i + \sum_{j\ne i}\boldsymbol{f}_{ij}\Big) = \boldsymbol{M}_{\mathrm{ext}} + \boldsymbol{M}_{\mathrm{int}}.
$$
The internal torques are paired: $\boldsymbol{r}_i\times\boldsymbol{f}_{ij} + \boldsymbol{r}_j\times\boldsymbol{f}_{ji} = (\boldsymbol{r}_i - \boldsymbol{r}_j)\times\boldsymbol{f}_{ij}$. When the internal forces act along the line joining the two particles (as do gravitational forces, electrostatic forces, and the forces in light rods and strings), $\boldsymbol{f}_{ij} \parallel \boldsymbol{r}_i - \boldsymbol{r}_j$ and this term vanishes, so $\boldsymbol{M}_{\mathrm{int}} = \boldsymbol{0}$.

**Theorem 3.9.1 (Angular Momentum Theorem for a System of Particles)** The net external torque on a system of particles equals the rate of change of the angular momentum of the system:

$$
\boldsymbol{M}_{\mathrm{ext}} = \sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i = \frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t},
$$
where all the $\boldsymbol{L}_i$ and $\boldsymbol{M}_i$ are computed about the same reference point.

**Theorem 3.9.2 (Conservation of Angular Momentum of a System of Particles)** When the net external torque on a system of particles is zero, the total angular momentum of the system is conserved; when the component of the net external torque in some direction is zero, the component of the total angular momentum in that direction is conserved.

Conservation of momentum and conservation of angular momentum of a system are independent: the former requires zero net external force, the latter zero net external torque. A pair of forces that are equal, opposite and not collinear (a couple) has zero net force but nonzero torque; a central force has zero torque about the force center but nonzero net force. So each can hold without the other.

**Example 3.9.1** A light rod of length $l$ is fixed at its upper end at the point $O$ by a smooth pivot, and a small ball of mass $m_1$ is attached to its lower end. A small ball of mass $m_2$ strikes the midpoint of the rod with horizontal velocity $v_0$ and sticks to it. Find the angular velocity $\omega$ of the rod after the collision.

Take $m_1$ (together with the rod) and $m_2$ as the system. During the collision, gravity and the force of the pivot both pass through $O$ (the rod is vertical at the collision), so their torque about $O$ is zero and the angular momentum of the system about $O$ is conserved:

$$
\frac l2\,m_2v_0 = l\cdot m_1\omega l + \frac l2\cdot m_2\omega\frac l2 \quad\Longrightarrow\quad \omega = \frac{2m_2}{4m_1 + m_2}\,\frac{v_0}{l}.
$$
The horizontal momentum of the system is not conserved in the collision: the momentum after the collision, $m_1\omega l + m_2\omega\frac l2 = \dfrac{2m_1 + m_2}{4m_1 + m_2}\,m_2v_0 < m_2v_0$, so the pivot exerts a backward impulse on the rod during the collision.

**Example 3.9.2** On a smooth horizontal plane, two small balls of masses $m_1$ and $m_2$ are connected by a light rod of length $l$ and placed at rest. A small ball of mass $m_3$ with velocity $v_0$ perpendicular to the rod strikes the midpoint $O$ of the rod in an elastic collision. Find the velocities of the three balls just after the collision, and the center-of-mass velocity of the system of $m_1$ and $m_2$.

Take the three balls and the rod as the system; no external force acts in the horizontal plane. Just after the collision the velocities $v_1$ and $v_2$ of $m_1$ and $m_2$ are both along the direction of $v_0$; let $m_3$ rebound with speed $v_3$ ($v_3 < 0$ means it continues forward).

- Elastic collision, conservation of kinetic energy: $\frac12m_3v_0^2 = \frac12m_1v_1^2 + \frac12m_2v_2^2 + \frac12m_3v_3^2$;
- Conservation of momentum along $v_0$: $m_3v_0 = m_1v_1 + m_2v_2 - m_3v_3$;
- Conservation of angular momentum about the fixed point coinciding with $O$ (taking out of the page as positive); the velocity of $m_3$ passes through $O$ both before and after: $0 = -m_1v_1\frac l2 + m_2v_2\frac l2$, that is, $m_1v_1 = m_2v_2$.

One can also write conservation of angular momentum about the fixed point coinciding with the center of mass $C$, with the same result. Solving together, with $D = 4m_1m_2 + (m_1 + m_2)m_3$,

$$
v_1 = \frac{4m_2m_3}{D}v_0, \qquad v_2 = \frac{4m_1m_3}{D}v_0, \qquad v_3 = \frac{4m_1m_2 - (m_1 + m_2)m_3}{D}v_0,
$$

$$
v_C = \frac{m_1v_1 + m_2v_2}{m_1 + m_2} = \frac{8m_1m_2m_3}{(m_1 + m_2)D}v_0.
$$
If $m_1 \ne m_2$, then $v_1 \ne v_2$, and after the collision the rod both translates with the center of mass and rotates about it, with angular velocity $\omega = \dfrac{\lvert v_1 - v_2\rvert}{l} = \dfrac{4m_3\lvert m_2 - m_1\rvert}{Dl}v_0$.

Comparison of momentum and angular momentum:

| | Momentum | Angular momentum |
|---|---|---|
| Definition | $\boldsymbol{P} = \sum_im_i\boldsymbol{v}_i$, a vector | $\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times\boldsymbol{p}_i$, a vector |
| Reference point | not needed | must be specified |
| Cause of change | net external force, independent of internal forces | net external torque, independent of internal torques |
| Condition for conservation | $\sum_i\boldsymbol{F}_i = \boldsymbol{0}$ | $\sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i = \boldsymbol{0}$ |
| Relation to the center of mass | $\boldsymbol{P} = m\boldsymbol{v}_C$ | $\boldsymbol{L} = \boldsymbol{r}_C\times m\boldsymbol{v}_C + \boldsymbol{L}'$ (Section 3.10) |
| In the center-of-mass frame | total momentum is zero | the angular momentum theorem about the center of mass holds (Section 3.10) |

## 3.10. The Angular Momentum Theorem in the Center-of-Mass Frame

### 3.10.1. Angular Momentum in the Center-of-Mass Frame

Let $O$ be a fixed point in the inertial frame $S$, let $\boldsymbol{r}_i$ and $\boldsymbol{r}_C$ be the position vectors of particle $i$ and of the center of mass relative to $O$, and let $\boldsymbol{r}'_i = \boldsymbol{r}_i - \boldsymbol{r}_C$ and $\boldsymbol{v}'_i = \boldsymbol{v}_i - \boldsymbol{v}_C$ be the position vector and velocity of particle $i$ relative to the center of mass. Consider three angular momenta:

- in $S$, the angular momentum of the system about $O$, $\boldsymbol{L} = \sum_i\boldsymbol{r}_i\times m_i\boldsymbol{v}_i$;
- in $S$, the angular momentum about $O$ with the whole mass concentrated at the center of mass, $\boldsymbol{L}_C = \boldsymbol{r}_C\times m\boldsymbol{v}_C = \boldsymbol{r}_C\times\boldsymbol{P}$;
- in the center-of-mass frame, the angular momentum of the system about the center of mass, $\boldsymbol{L}' = \sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{v}'_i$.

**Theorem 3.10.1** $\boldsymbol{L} = \boldsymbol{L}_C + \boldsymbol{L}'$: the angular momentum of a system of particles about a fixed point equals the sum of the angular momentum of the center of mass (orbital angular momentum) and the angular momentum of the system about the center of mass (spin angular momentum).

**Proof** Substitute $\boldsymbol{r}_i = \boldsymbol{r}'_i + \boldsymbol{r}_C$ and $\boldsymbol{v}_i = \boldsymbol{v}'_i + \boldsymbol{v}_C$ and expand:

$$
\boldsymbol{L} = \sum_im_i\boldsymbol{r}'_i\times\boldsymbol{v}'_i + \Big(\sum_im_i\boldsymbol{r}'_i\Big)\times\boldsymbol{v}_C + \boldsymbol{r}_C\times\sum_im_i\boldsymbol{v}'_i + m\,\boldsymbol{r}_C\times\boldsymbol{v}_C.
$$
By Theorem 3.6.2, $\sum_im_i\boldsymbol{r}'_i = \boldsymbol{0}$ and $\sum_im_i\boldsymbol{v}'_i = \boldsymbol{0}$, so the middle two terms vanish. $\square$

By the same reasoning, $\boldsymbol{L}' = \sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{v}_i$: in computing the angular momentum about the center of mass, using the velocity relative to the center of mass or relative to $S$ gives the same result.

### 3.10.2. The Angular Momentum Theorem About the Center of Mass

Differentiate $\boldsymbol{L}' = \boldsymbol{L} - \boldsymbol{r}_C\times\boldsymbol{P}$, using Theorem 3.9.1 and the momentum theorem for a system of particles, and noting that $\dot{\boldsymbol{r}}_C\times\boldsymbol{P} = \boldsymbol{v}_C\times m\boldsymbol{v}_C = \boldsymbol{0}$:

$$
\frac{\mathrm{d}\boldsymbol{L}'}{\mathrm{d}t} = \sum_i\boldsymbol{r}_i\times\boldsymbol{F}_i - \boldsymbol{r}_C\times\sum_i\boldsymbol{F}_i = \sum_i(\boldsymbol{r}_i - \boldsymbol{r}_C)\times\boldsymbol{F}_i = \sum_i\boldsymbol{r}'_i\times\boldsymbol{F}_i.
$$

**Theorem 3.10.2 (Angular Momentum Theorem About the Center of Mass)** In the center-of-mass frame, the net torque about the center of mass of the external forces on a system of particles equals the rate of change of the angular momentum of the system about the center of mass:

$$
\boldsymbol{M}'_{\mathrm{ext}} = \sum_i\boldsymbol{r}'_i\times\boldsymbol{F}_i = \frac{\mathrm{d}\boldsymbol{L}'}{\mathrm{d}t}.
$$
This theorem holds whether or not the center-of-mass frame is inertial.

This is not obvious: when the center of mass accelerates with $\boldsymbol{a}_C$, the center-of-mass frame is a translating non-inertial frame and each particle experiences an **inertial force** $-m_i\boldsymbol{a}_C$. But the net torque of these inertial forces about the center of mass is

$$
\boldsymbol{M}_{\mathrm{in}} = \sum_i\boldsymbol{r}'_i\times(-m_i\boldsymbol{a}_C) = -\Big(\sum_im_i\boldsymbol{r}'_i\Big)\times\boldsymbol{a}_C = \boldsymbol{0},
$$
for the same reason that the net torque about the center of mass of the gravitational forces on the particles in a uniform gravitational field is zero: the inertial force $-m_i\boldsymbol{a}_C$ is proportional to mass and has the same direction everywhere, and so is equivalent to a uniform "gravity" acting at the center of mass.

The motion of a system of particles can therefore be treated completely in two parts: the motion of the center of mass is determined by the center-of-mass motion theorem (Theorem 3.6.1), and the rotation about the center of mass by the angular momentum theorem about the center of mass; both involve only external forces. This is precisely the method [5.1.5](/5.1.5) uses for the planar motion of rigid bodies (such as rolling).

## Summary

| Topic | Key points |
|---|---|
| Momentum theorem | Particle $\boldsymbol{F} = \mathrm{d}\boldsymbol{p}/\mathrm{d}t$; system $\boldsymbol{F}_{\mathrm{ext}} = \mathrm{d}\boldsymbol{P}/\mathrm{d}t$, internal forces do not change the total momentum |
| Conservation of momentum | $\boldsymbol{F}_{\mathrm{ext}} = \boldsymbol{0} \Rightarrow \boldsymbol{P}$ conserved; may hold by components; approximately conserved in collisions |
| Rockets | $v_{\mathrm{f}} = v_{\mathrm{i}} + u\ln(m_{\mathrm{i}}/m_{\mathrm{f}})$; thrust $uq_m$ |
| Center of mass | $\boldsymbol{r}_C = \sum m_i\boldsymbol{r}_i/m$; $\boldsymbol{P} = m\boldsymbol{v}_C$; $\boldsymbol{F}_{\mathrm{ext}} = m\boldsymbol{a}_C$; the center-of-mass frame is the zero-momentum frame |
| Angular momentum theorem | $\boldsymbol{L} = \boldsymbol{r}\times\boldsymbol{p}$, $\boldsymbol{M} = \boldsymbol{r}\times\boldsymbol{F}$, $\boldsymbol{M}_{\mathrm{ext}} = \mathrm{d}\boldsymbol{L}/\mathrm{d}t$, about the same reference point |
| Conservation of angular momentum | $\boldsymbol{M}_{\mathrm{ext}} = \boldsymbol{0} \Rightarrow \boldsymbol{L}$ conserved; central forces; Kepler's second law |
| Center-of-mass frame | $\boldsymbol{L} = \boldsymbol{r}_C\times\boldsymbol{P} + \boldsymbol{L}'$; $\boldsymbol{M}'_{\mathrm{ext}} = \mathrm{d}\boldsymbol{L}'/\mathrm{d}t$ holds also for a non-inertial center-of-mass frame |

## Questions

1. A small ball rests on a sheet of paper on a table, and the paper is pulled quickly out to the right. Which way does the ball move?

   **Answer** To the right. The friction of the paper on the ball points to the right, so by the center-of-mass motion theorem the center of mass of the ball accelerates to the right relative to the table, even though it slides to the left relative to the paper (and begins to roll backward).

2. Can the center of mass lie outside the body?

   **Answer** Yes, as for a ring or a semicircular wire (Example 3.5.2).

3. Regard a system of particles at some instant as a whole. What is the net torque about the center of mass of the gravitational forces on the particles? Use this to explain why the torque of the inertial forces about the center of mass is zero.

   **Answer** It is zero in a uniform gravitational field, because $\sum_i\boldsymbol{r}'_i\times m_i\boldsymbol{g} = \big(\sum_im_i\boldsymbol{r}'_i\big)\times\boldsymbol{g} = \boldsymbol{0}$; the inertial forces $-m_i\boldsymbol{a}_C$ have exactly the same structure (Section 3.10.2).
