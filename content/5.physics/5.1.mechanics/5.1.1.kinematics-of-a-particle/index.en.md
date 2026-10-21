---
title: Kinematics of a Particle
description: Reference frames and the particle model; position, displacement, velocity and acceleration; uniformly accelerated motion and projectiles; tangential and normal acceleration in intrinsic coordinates and angular quantities of circular motion; plane polar coordinates; relative motion and the Galilean velocity transformation.
source_hash: b75edc5a0233
---

Mechanics studies the motion of bodies, that is, the change of their positions with time. This chapter is the first step. *Kinematics* describes motion itself (where a body is at each instant, how fast it moves, and how its velocity changes) without asking why the motion changes; the cause, force, is the subject of the next chapter, [5.1.2](/5.1.2). The language of this description is the calculus of vectors and **vector-valued functions**: position is a vector function of time, and velocity and acceleration are its first and second derivatives ([2.2.11](/2.2.11)). The **inner product** and the **cross product** from vector algebra ([2.2.11](/2.2.11#def-11.1.1)) appear throughout this and the following chapters. We discuss in turn reference frames and the particle model, the description in Cartesian coordinates, uniformly accelerated motion, intrinsic coordinates and circular motion, plane polar coordinates, and finally the transformation of velocities between reference frames, which relativity will correct in [5.1.8](/5.1.8).

## 1.1. Reference Frames

### 1.1.1. The Relativity of Motion

The same body can move quite differently as seen by different observers: a passenger at rest in a train carriage moves at high speed as seen from the ground. To describe motion we must first say "relative to what."

**Definition 1.1.1 (Reference Frame)** A body or system of bodies chosen as the standard of comparison for describing the motion of other bodies is called a **reference frame**.

In kinematics the reference frame may be chosen freely, and the form of a body's motion depends on this choice; this is the relativity of motion. Commonly used reference frames are:

- the solar frame (origin at the center of the Sun, axes pointing to distant stars);
- the geocentric frame (origin at the center of the Earth, axes pointing to distant stars and not rotating with the Earth);
- the ground frame (laboratory frame), attached to the Earth's surface;
- the center-of-mass frame, see [5.1.3](/5.1.3).

To describe motion quantitatively we attach a coordinate system to the reference frame. Once the frame is fixed, the coordinate system can still be chosen at will; the mathematical expression of the motion differs between coordinate systems, but it is the same motion. This chapter uses three coordinate systems:

| Coordinate system | Coordinates | Unit vectors | Suited to |
|---|---|---|---|
| Cartesian | $x, y, z$ | $\boldsymbol{e}_x, \boldsymbol{e}_y, \boldsymbol{e}_z$, independent of time | constant acceleration, such as projectiles |
| Plane polar | $r, \theta$ | $\boldsymbol{e}_r, \boldsymbol{e}_\theta$, varying with the particle's position | acceleration directed toward a fixed point, such as planets orbiting the Sun |
| Intrinsic | path length $s$ | $\boldsymbol{e}_{\mathrm{t}}, \boldsymbol{e}_{\mathrm{n}}$, varying with the particle's position | known trajectory, such as circular motion |

### 1.1.2. Translation, Rotation and the Particle Model

A body is said to undergo *translation* if, while it moves, the line joining any two of its points stays parallel to itself. All points of a translating body follow trajectories of identical shape, merely displaced from one another, so the motion of one point represents the whole body. When a body rotates about a fixed or instantaneous axis, its points move differently and no single point can represent it; rotation describes the motion of a collection of particles and is left to the chapter on rigid bodies, [5.1.5](/5.1.5).

**Definition 1.1.2 (Particle)** When only the mass and position of a body matter and its size and shape are ignored, the body is treated as a geometric point carrying mass, called a **particle**.

The particle is an idealized model. Whether a body can be treated as a particle depends on the problem under study: it can when its size is much smaller than the range of its motion (the Earth orbiting the Sun) or when it only translates, but not when we study the Earth's rotation. Regular shape or slow motion is not the criterion.

### 1.1.3. Translating and Rotating Reference Frames

A reference frame can itself move. A frame whose attached coordinate axes keep a fixed orientation is called a translating frame; one whose axes rotate with time is called a rotating frame. The origin of a translating frame may move along a curve: a spacecraft that revolves around a planet without spinning is a translating frame, since its axes always point in fixed directions. A coordinate system attached to a rotating disk is a rotating frame. The transformation between the two kinds of frames is discussed in Section 1.7 and in [5.1.2](/5.1.2).

## 1.2. The Equation of Motion of a Particle

Choose an origin $O$ in the reference frame and equip it with a set of synchronized clocks; then the position of a particle can be given as a function of time.

**Definition 1.2.1 (Position Vector)** The vector $\boldsymbol{r} = \overrightarrow{OP}$ from the origin $O$ to the particle's position $P$ is called the **position vector** (or radius vector) of the particle. The function of time

$$
\boldsymbol{r} = \boldsymbol{r}(t) = x(t)\,\boldsymbol{e}_x + y(t)\,\boldsymbol{e}_y + z(t)\,\boldsymbol{e}_z
$$
is called the equation of motion of the particle.

The equation of motion is a **vector-valued function**. Eliminating $t$ from the three component equations gives the equation satisfied by the trajectory, called the equation of the path. The equation of motion contains more information than the equation of the path: it gives not only the route the particle follows but also when it reaches each point of the route, and from it the velocity and acceleration can be found.

## 1.3. Displacement, Velocity and Acceleration

### 1.3.1. Displacement and Distance Traveled

**Definition 1.3.1 (Displacement)** The change of the position vector between times $t$ and $t + \Delta t$,

$$
\Delta\boldsymbol{r} = \boldsymbol{r}(t + \Delta t) - \boldsymbol{r}(t),
$$
is called the **displacement** during this interval. Its magnitude $\lvert\Delta\boldsymbol{r}\rvert$ equals the straight-line distance from the initial point $P_1$ to the final point $P_2$, and its direction points from $P_1$ to $P_2$.

The length actually traveled along the trajectory is called the path length and is denoted $\Delta s$. Three quantities must be distinguished:

- $\Delta\boldsymbol{r}$ is a vector; $\lvert\Delta\boldsymbol{r}\rvert$ is the magnitude of the displacement; $\Delta r = \lvert\boldsymbol{r}(t+\Delta t)\rvert - \lvert\boldsymbol{r}(t)\rvert$ is the change in the magnitude of the position vector, that is, the change in the distance from the particle to the origin. In general $\lvert\Delta\boldsymbol{r}\rvert \ne \Delta r$: for a particle moving in a circle about the origin, $\Delta r = 0$ while the displacement is not zero.
- In general $\Delta s \ge \lvert\Delta\boldsymbol{r}\rvert$, since a chord is no longer than its arc; for an infinitesimal process, however, $\mathrm{d}s = \lvert\mathrm{d}\boldsymbol{r}\rvert$ (the differential of **arc length**), while $\lvert\mathrm{d}\boldsymbol{r}\rvert \ne \mathrm{d}r$ still holds.

### 1.3.2. Velocity and Speed

**Definition 1.3.2 (Velocity)** The ratio of the displacement to the time taken, $\bar{\boldsymbol{v}} = \Delta\boldsymbol{r}/\Delta t$, is called the average velocity; the limit as $\Delta t \to 0$,

$$
\boldsymbol{v} = \lim_{\Delta t\to0}\frac{\Delta\boldsymbol{r}}{\Delta t} = \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = \dot{\boldsymbol{r}},
$$
is called the (instantaneous) **velocity** of the particle at time $t$.

Velocity is the derivative of the position vector; it is directed along the tangent to the trajectory at that point, pointing forward along the motion (the **tangent vector**, [2.2.11](/2.2.11#def-11.4.1)).

**Definition 1.3.3 (Speed)** The magnitude of the velocity is called the **speed**:

$$
v = \lvert\boldsymbol{v}\rvert = \frac{\lvert\mathrm{d}\boldsymbol{r}\rvert}{\mathrm{d}t} = \frac{\mathrm{d}s}{\mathrm{d}t}.
$$

Note that $v \ne \dfrac{\mathrm{d}r}{\mathrm{d}t}$: the latter is only the rate of change of the distance from the particle to the origin (the radial velocity of Section 1.6).

### 1.3.3. Acceleration

**Definition 1.3.4 (Acceleration)** The rate of change of velocity with time,

$$
\boldsymbol{a} = \lim_{\Delta t\to0}\frac{\Delta\boldsymbol{v}}{\Delta t} = \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = \frac{\mathrm{d}^2\boldsymbol{r}}{\mathrm{d}t^2} = \ddot{\boldsymbol{r}},
$$
is called the **acceleration** of the particle.

The acceleration points in the direction of the velocity change $\mathrm{d}\boldsymbol{v}$. In general it is not tangent to the trajectory but points toward the inner side of the bend (Section 1.5). Note likewise that $a = \lvert\boldsymbol{a}\rvert = \Big\lvert\dfrac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\Big\rvert \ne \dfrac{\mathrm{d}v}{\mathrm{d}t}$: in uniform circular motion the speed is constant, yet the acceleration is not zero.

The units of velocity and acceleration are $\mathrm{m\,s^{-1}}$ and $\mathrm{m\,s^{-2}}$, respectively.

### 1.3.4. Description in Cartesian Coordinates

The unit vectors $\boldsymbol{e}_x, \boldsymbol{e}_y, \boldsymbol{e}_z$ of a Cartesian system do not change with time, so differentiation acts only on the components:

$$
\boldsymbol{v} = \dot{x}\,\boldsymbol{e}_x + \dot{y}\,\boldsymbol{e}_y + \dot{z}\,\boldsymbol{e}_z, \qquad
\boldsymbol{a} = \ddot{x}\,\boldsymbol{e}_x + \ddot{y}\,\boldsymbol{e}_y + \ddot{z}\,\boldsymbol{e}_z,
$$

$$
v = \sqrt{v_x^2 + v_y^2 + v_z^2}, \qquad \mathrm{d}s = \lvert\mathrm{d}\boldsymbol{r}\rvert = \sqrt{(\mathrm{d}x)^2 + (\mathrm{d}y)^2 + (\mathrm{d}z)^2}.
$$

The motions along the components are mutually independent: the motion in the $x$ direction is determined only by $a_x$ and the initial conditions in the $x$ direction. A complicated motion can therefore be resolved into rectilinear motions along three directions, solved separately and then recombined. This independence is special to Cartesian coordinates; in a coordinate system whose unit vectors vary with position, the components are coupled (Section 1.6).

### 1.3.5. Two Kinds of Kinematic Problems

Kinematic problems fall into two kinds:

1. Given the equation of motion $\boldsymbol{r}(t)$, differentiate successively to obtain $\boldsymbol{v}(t)$ and $\boldsymbol{a}(t)$;
2. Given the acceleration $\boldsymbol{a}(t)$ and the initial conditions $\boldsymbol{r}(t_0) = \boldsymbol{r}_0$, $\boldsymbol{v}(t_0) = \boldsymbol{v}_0$, integrate to find $\boldsymbol{v}(t)$ and $\boldsymbol{r}(t)$:

$$
\boldsymbol{v}(t) = \boldsymbol{v}_0 + \int_{t_0}^{t}\boldsymbol{a}(t')\,\mathrm{d}t', \qquad
\boldsymbol{r}(t) = \boldsymbol{r}_0 + \int_{t_0}^{t}\boldsymbol{v}(t')\,\mathrm{d}t'.
$$

Dynamics ([5.1.2](/5.1.2)) gives the acceleration from the forces, so the second kind of problem is the main problem of mechanics; when the acceleration depends on position and velocity, it becomes an initial value problem for an **ordinary differential equation**. The vector form is convenient for general statements, while quantitative calculation requires a choice of coordinate system (the table in Section 1.1.1).

**Remark 1.3.1 (Differentiation of Vector Functions)** The rules for differentiating sums, scalar multiples, inner products and cross products of vector functions are given in [2.2.11](/2.2.11#thm-11.3.1); note that the order of the factors in a cross product cannot be exchanged. Write a vector as the product of a magnitude and a direction, $\boldsymbol{A} = A\,\boldsymbol{e}_A$ (where $\boldsymbol{e}_A$ is the unit vector along $\boldsymbol{A}$). Then

$$
\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t} = \frac{\mathrm{d}A}{\mathrm{d}t}\,\boldsymbol{e}_A + A\,\frac{\mathrm{d}\boldsymbol{e}_A}{\mathrm{d}t}.
$$
Since $\boldsymbol{e}_A$ always has length 1, $\dfrac{\mathrm{d}\boldsymbol{e}_A}{\mathrm{d}t} \perp \boldsymbol{e}_A$ ([2.2.11](/2.2.11#thm-11.3.2)). The change of a vector thus always consists of two parts: the part along the vector itself comes from the change in magnitude, and the part perpendicular to it comes from the change in direction. The tangential and normal accelerations of Section 1.5 are exactly this decomposition. Two identities used repeatedly later can be verified by expanding in components:

$$
\boldsymbol{A}\cdot(\boldsymbol{B}\times\boldsymbol{C}) = \boldsymbol{B}\cdot(\boldsymbol{C}\times\boldsymbol{A}) = \boldsymbol{C}\cdot(\boldsymbol{A}\times\boldsymbol{B}), \qquad
\boldsymbol{A}\times(\boldsymbol{B}\times\boldsymbol{C}) = \boldsymbol{B}(\boldsymbol{A}\cdot\boldsymbol{C}) - \boldsymbol{C}(\boldsymbol{A}\cdot\boldsymbol{B}).
$$
The former is the scalar triple product, equal to the signed volume of the parallelepiped with edges $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$, that is, the **determinant** of their components; the latter is the expansion of the vector triple product.

## 1.4. Uniformly Accelerated Motion

### 1.4.1. General Formulas

For a constant acceleration vector $\boldsymbol{a}$, take $t_0 = 0$ and integrate $\mathrm{d}\boldsymbol{v} = \boldsymbol{a}\,\mathrm{d}t$ and $\mathrm{d}\boldsymbol{r} = \boldsymbol{v}\,\mathrm{d}t$ in turn:

$$
\boldsymbol{v} = \boldsymbol{v}_0 + \boldsymbol{a}t, \qquad \boldsymbol{r} = \boldsymbol{r}_0 + \boldsymbol{v}_0 t + \frac12\boldsymbol{a}t^2.
$$

The motion takes place in the plane through $\boldsymbol{r}_0$ spanned by $\boldsymbol{v}_0$ and $\boldsymbol{a}$. Depending on whether $\boldsymbol{v}_0$ and $\boldsymbol{a}$ are collinear, there are two cases: rectilinear motion and projectile motion.

### 1.4.2. Uniformly Accelerated Rectilinear Motion

When $\boldsymbol{v}_0$ and $\boldsymbol{a}$ are collinear (or $\boldsymbol{v}_0 = \boldsymbol{0}$), the motion is one-dimensional:

$$
v = v_0 + at, \qquad x = x_0 + v_0 t + \frac12 at^2, \qquad v^2 - v_0^2 = 2a(x - x_0).
$$

**Example 1.4.1** A bungee jumping platform is $55\,\mathrm{m}$ high. Treating the jumper as a body in free fall from zero initial velocity, the speed after falling $55\,\mathrm{m}$ is $v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 55}\,\mathrm{m\,s^{-1}} \approx 33\,\mathrm{m\,s^{-1}}$. This is an upper bound: a real cord begins to stretch and decelerate the jumper before the bottom is reached, and air resistance lowers the speed further.

A real falling body also experiences air resistance. The resistance grows with speed and, after a sufficiently long fall, balances the weight; the body then falls at constant speed, called the terminal velocity. The terminal velocity of raindrops is of the order of a few meters per second (about $9\,\mathrm{m\,s^{-1}}$ for large drops). Calculating the terminal velocity belongs to dynamics; see Example 2.5.3 in [5.1.2](/5.1.2).

### 1.4.3. Projectile Motion

Neglecting air resistance, the acceleration of a projectile is the gravitational acceleration $\boldsymbol{g}$, which is not collinear with the initial velocity. Take the $x$ axis horizontal and the $y$ axis vertically upward, let the initial velocity $v_0$ make an elevation angle $\theta$ with the horizontal, and let the launch point be the origin. By the independence of components, the horizontal motion is uniform and the vertical motion is uniformly accelerated:

$$
x = v_0\cos\theta\,t, \qquad y = v_0\sin\theta\,t - \frac12 gt^2.
$$

- At the highest point $v_y = v_0\sin\theta - gt = 0$, so $t = \dfrac{v_0\sin\theta}{g}$ and the maximum height is $y_{\max} = \dfrac{v_0^2\sin^2\theta}{2g}$.
- The horizontal range, on returning to the original height, is $\dfrac{v_0^2\sin2\theta}{g}$, which is largest for $\theta = 45^\circ$.
- Eliminating $t$ gives the equation of the path

$$
y = x\tan\theta - \frac{g x^2}{2v_0^2\cos^2\theta},
$$
which is a parabola.

![Projectile trajectories for the same initial speed and different elevation angles (neglecting air resistance); the dots mark the highest points. The dashed curve is the envelope of all trajectories, $y = \frac{v_0^2}{2g} - \frac{g x^2}{2 v_0^2}$; every point reachable with this initial speed lies below it](./plots/projectile-trajectories.py)

For a given $x$, maximizing $y$ in the path equation over $\tan\theta$ gives $\tan\theta = \dfrac{v_0^2}{gx}$, and substituting back yields the envelope in the figure (the safety parabola). Real bullets and shells suffer strong air resistance and their trajectories deviate markedly from parabolas (see the numerical solution in [5.1.2](/5.1.2)); long-range ballistic missiles move over a range in which both the magnitude and the direction of the gravitational acceleration change appreciably. The starting point of all these problems, however, is the kinematics above.

**Example 1.4.2** A gun is aimed at an apple on a tree, and at the instant the bullet leaves the muzzle the apple begins to fall freely. Neglecting air resistance, the bullet hits the apple as long as it can reach the apple's horizontal position before the apple reaches the ground. This is easiest to see in the frame of the freely falling apple: in this frame the accelerations of both bullet and apple are $\boldsymbol{g} - \boldsymbol{g} = \boldsymbol{0}$, so the bullet moves uniformly along the line of sight while the apple rests on that line.

## 1.5. Intrinsic Coordinates and Circular Motion

### 1.5.1. Intrinsic Coordinates

When the trajectory is known, the most direct way to describe the position of a particle is by the path length it has traveled along the trajectory.

**Definition 1.5.1 (Intrinsic Coordinates)** On a known trajectory choose a starting point, and use the path length $s(t)$ from the starting point to the particle, measured along the trajectory, as the coordinate. At the particle's position take two unit vectors: the tangential unit vector $\boldsymbol{e}_{\mathrm{t}}$ points along the tangent in the direction of increasing $s$, and the normal unit vector $\boldsymbol{e}_{\mathrm{n}}$ is perpendicular to the tangent and points toward the center of curvature of the trajectory. Such a coordinate system is called **intrinsic coordinates** (also natural coordinates).

The vectors $\boldsymbol{e}_{\mathrm{t}}$ and $\boldsymbol{e}_{\mathrm{n}}$ are attached to the particle's position and change direction with it (and hence with time); this is the fundamental difference from Cartesian coordinates. The velocity is tangent to the path,

$$
\boldsymbol{v} = v\,\boldsymbol{e}_{\mathrm{t}}, \qquad v = \frac{\mathrm{d}s}{\mathrm{d}t}.
$$

To find the acceleration, $\boldsymbol{e}_{\mathrm{t}}$ must also be differentiated (Remark 1.3.1):

$$
\boldsymbol{a} = \frac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + v\,\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t}.
$$

Suppose the tangent turns through an angle $\mathrm{d}\varphi$ while the particle covers $\mathrm{d}s$. The magnitude of $\mathrm{d}\boldsymbol{e}_{\mathrm{t}}$ is $\lvert\boldsymbol{e}_{\mathrm{t}}\rvert\,\mathrm{d}\varphi = \mathrm{d}\varphi$, and its direction is perpendicular to $\boldsymbol{e}_{\mathrm{t}}$ and points to the side toward which the path bends, that is, along $\boldsymbol{e}_{\mathrm{n}}$. By the definition of **curvature**, $\dfrac{\mathrm{d}\varphi}{\mathrm{d}s} = \dfrac1\rho$ (where $\rho$ is the **radius of curvature**, [2.2.7](/2.2.7#def-7.5.3)),

$$
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t} = \frac{\mathrm{d}\varphi}{\mathrm{d}s}\frac{\mathrm{d}s}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{n}} = \frac{v}{\rho}\,\boldsymbol{e}_{\mathrm{n}},
\qquad\text{so}\qquad
\boldsymbol{a} = \frac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + \frac{v^2}{\rho}\,\boldsymbol{e}_{\mathrm{n}}.
$$

**Definition 1.5.2 (Tangential and Normal Acceleration)** The component of the acceleration along the tangent, $\boldsymbol{a}_{\mathrm{t}} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}}$, is called the **tangential acceleration**; the component along the normal, $\boldsymbol{a}_{\mathrm{n}} = \dfrac{v^2}{\rho}\,\boldsymbol{e}_{\mathrm{n}}$, is called the **normal acceleration**.

The tangential acceleration describes the change of speed: the particle speeds up when $\boldsymbol{a}_{\mathrm{t}}$ is parallel to $\boldsymbol{v}$ and slows down when it is antiparallel. The normal acceleration describes the change in direction of the velocity and always points toward the inner side of the bend, so the acceleration can never point to the outer side of the path. Intrinsic coordinates reflect the character of the motion most directly and give a clear physical picture; they are suited to cases where the trajectory is known.

**Example 1.5.1** Find the radius of curvature at the highest point of a projectile's trajectory. At the highest point the velocity is horizontal with magnitude $v_0\cos\theta$, and the gravitational acceleration points vertically downward, exactly along the normal, so the tangential acceleration vanishes. From $a_{\mathrm{n}} = g = \dfrac{v^2}{\rho}$,

$$
\rho = \frac{v_0^2\cos^2\theta}{g}.
$$
Similarly, at the launch point $a_{\mathrm{n}} = g\cos\theta$ and $\rho = \dfrac{v_0^2}{g\cos\theta}$. Finding the radius of curvature from kinematics in this way is much simpler than applying the curvature formula directly to the equation of the path.

**Example 1.5.2 (Electron Energy Analyzer)** A hemispherical electron energy analyzer consists of two concentric hemispherical electrodes; the electric field between them gives an electron entering the gap an acceleration directed toward the center. Let this acceleration be $a_0$ at the central radius $R_0$. An electron entering tangentially with speed $v_0$ can move on the circle of radius $R_0$ and leave through the exit slit only if $\dfrac{v_0^2}{R_0} = a_0$; electrons with greater speed need a greater centripetal acceleration and drift toward the outer electrode, and slower ones toward the inner electrode. The analyzer therefore passes only electrons of a certain energy, and varying the voltage between the electrodes scans the electron energy spectrum. The detailed distribution of the field is treated in the electromagnetism part, [5.3.1](/5.3.1).

### 1.5.2. Angular Quantities of Circular Motion

For a particle moving on a circle of radius $R$, its position is described by the angle $\theta(t)$ between the position vector and a reference direction, and the path length is $s = R\theta$.

A finite angular displacement is not a vector: the result of two finite rotations depends on their order (rotating a book by $90^\circ$ first about the $x$ axis and then about the $y$ axis gives a different result from rotating first about $y$ and then about $x$), so vector addition fails to be commutative. In the language of matrices, rotations in three-dimensional space are represented by **orthogonal matrices** ([2.1.4](/2.1.4)), and matrix multiplication is in general not commutative. The composition of infinitesimal rotations, however, is independent of order (the difference is of second order), so the angular velocity can be defined as a vector.

**Definition 1.5.3 (Angular Velocity)** Suppose a particle turns through an angle $\mathrm{d}\theta$ about an axis in time $\mathrm{d}t$. The vector $\boldsymbol{\omega}$ is called the **angular velocity**: its magnitude is $\omega = \dfrac{\mathrm{d}\theta}{\mathrm{d}t}$, and its direction is along the axis, related to the sense of rotation by the right-hand rule (the direction of the thumb when the fingers of the right hand curl in the sense of rotation).

**Definition 1.5.4 (Angular Acceleration)** The rate of change of angular velocity with time, $\boldsymbol{\alpha} = \dfrac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}$, is called the **angular acceleration**.

For rotation about a fixed axis the direction of $\boldsymbol{\omega}$ does not change, and $\alpha = \dfrac{\mathrm{d}\omega}{\mathrm{d}t} = \dfrac{\mathrm{d}^2\theta}{\mathrm{d}t^2}$. The unit of angular velocity is $\mathrm{rad\,s^{-1}}$ (the radian is a dimensionless unit, and the unit is often written $\mathrm{s^{-1}}$).

Taking the origin on the axis of rotation, the velocity of the particle is

$$
\boldsymbol{v} = \boldsymbol{\omega}\times\boldsymbol{r}, \qquad v = \frac{\mathrm{d}s}{\mathrm{d}t} = R\frac{\mathrm{d}\theta}{\mathrm{d}t} = R\omega.
$$
More generally, any vector $\boldsymbol{A}$ of constant length that rotates with angular velocity $\boldsymbol{\omega}$ satisfies $\dfrac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t} = \boldsymbol{\omega}\times\boldsymbol{A}$; this relation is used repeatedly for rotating frames in [5.1.2](/5.1.2) and for rigid bodies in [5.1.5](/5.1.5).

For circular motion, $\boldsymbol{e}_{\mathrm{t}}$ and $\boldsymbol{e}_{\mathrm{n}}$ are functions of the angle $\theta$ only. When $\theta$ increases by $\Delta\theta$, $\boldsymbol{e}_{\mathrm{t}}$ turns through the same angle, $\lvert\Delta\boldsymbol{e}_{\mathrm{t}}\rvert \approx \Delta\theta$, and its direction tends to $\boldsymbol{e}_{\mathrm{n}}$. Hence

$$
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}\theta} = \boldsymbol{e}_{\mathrm{n}}, \qquad \frac{\mathrm{d}\boldsymbol{e}_{\mathrm{n}}}{\mathrm{d}\theta} = -\boldsymbol{e}_{\mathrm{t}}, \qquad
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t} = \frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}\theta}\frac{\mathrm{d}\theta}{\mathrm{d}t} = \omega\,\boldsymbol{e}_{\mathrm{n}} = \frac{v}{R}\,\boldsymbol{e}_{\mathrm{n}},
$$
and so $\boldsymbol{a} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + \dfrac{v^2}{R}\,\boldsymbol{e}_{\mathrm{n}}$, the special case $\rho = R$ of the general formula in Section 1.5.1. The normal acceleration in circular motion points to the center and is also called the centripetal acceleration.

**Formula 1.5.1 (Relations Between Angular and Linear Quantities)** In circular motion of radius $R$,

$$
v = R\omega, \qquad a_{\mathrm{t}} = R\alpha, \qquad a_{\mathrm{n}} = \frac{v^2}{R} = R\omega^2.
$$
In vector form (origin on the axis of rotation): $\boldsymbol{a} = \boldsymbol{\alpha}\times\boldsymbol{r} + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$, where $\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) = -\omega^2\boldsymbol{r}_\perp$ and $\boldsymbol{r}_\perp$ is the vector drawn perpendicularly from the axis to the particle.

These relations are used repeatedly for the rotation of a rigid body about a fixed axis ([5.1.5](/5.1.5)): all points of the body have the same angular quantities, and their linear quantities are proportional to the distance from the axis.

## 1.6. Plane Polar Coordinates

**Definition 1.6.1 (Plane Polar Coordinates)** In a plane choose a pole $O$ and a polar axis. The position of a particle is described by its distance $r$ from the pole and the polar angle $\theta$ (positive counterclockwise from the polar axis). At the particle's position take the radial unit vector $\boldsymbol{e}_r$ (pointing in the direction of increasing $r$) and the transverse unit vector $\boldsymbol{e}_\theta$ (pointing in the direction of increasing $\theta$).

These are the **polar coordinates** ([2.2.7](/2.2.7)) equipped with unit vectors that vary with position. The vectors $\boldsymbol{e}_r = \cos\theta\,\boldsymbol{e}_x + \sin\theta\,\boldsymbol{e}_y$ and $\boldsymbol{e}_\theta = -\sin\theta\,\boldsymbol{e}_x + \cos\theta\,\boldsymbol{e}_y$ depend only on $\theta$, not on $r$, and direct differentiation gives

$$
\frac{\mathrm{d}\boldsymbol{e}_r}{\mathrm{d}\theta} = \boldsymbol{e}_\theta, \qquad \frac{\mathrm{d}\boldsymbol{e}_\theta}{\mathrm{d}\theta} = -\boldsymbol{e}_r.
$$

The position vector is $\boldsymbol{r} = r\,\boldsymbol{e}_r$. Differentiating with respect to time with the chain rule, $\dfrac{\mathrm{d}\boldsymbol{e}_r}{\mathrm{d}t} = \dot\theta\,\boldsymbol{e}_\theta$ and $\dfrac{\mathrm{d}\boldsymbol{e}_\theta}{\mathrm{d}t} = -\dot\theta\,\boldsymbol{e}_r$, we obtain

$$
\boldsymbol{v} = \dot r\,\boldsymbol{e}_r + r\dot\theta\,\boldsymbol{e}_\theta, \qquad
\boldsymbol{a} = (\ddot r - r\dot\theta^2)\,\boldsymbol{e}_r + (r\ddot\theta + 2\dot r\dot\theta)\,\boldsymbol{e}_\theta.
$$

The two components of the velocity, $v_r = \dot r$ and $v_\theta = r\dot\theta$, are called the radial velocity and the transverse velocity. Unlike in Cartesian coordinates, these two orthogonal partial motions are not independent in their description: the transverse velocity contains $r$, and every component of the acceleration contains derivatives of both $r$ and $\theta$. The transverse component of the acceleration can be written $a_\theta = \dfrac1r\dfrac{\mathrm{d}}{\mathrm{d}t}(r^2\dot\theta)$, so in a motion whose acceleration always points to the pole (motion under a central force), $r^2\dot\theta$ is conserved; this is Kepler's second law in [5.1.3](/5.1.3). When $r$ is constant, the formula reduces to the result for circular motion, $\boldsymbol{a} = -r\dot\theta^2\boldsymbol{e}_r + r\ddot\theta\,\boldsymbol{e}_\theta$.

**Example 1.6.1** A winch on the shore reels in a rope at constant speed $v_0$, pulling a boat on the water. The pulley $O$ is at height $h$ above the water. Find the speed of the boat when the rope makes an angle $\theta$ with the vertical.

Take the pulley $O$ as the pole of a polar coordinate system, with $r$ the length of rope from the pulley to the boat. Reeling in gives $\dot r = -v_0$, that is, $v_r = -v_0$. From the geometry, $\cos\theta = h/r$; differentiating both sides with respect to time,

$$
-\sin\theta\,\dot\theta = -\frac{h}{r^2}\dot r \quad\Longrightarrow\quad v_\theta = r\dot\theta = \frac{h\dot r}{r\sin\theta} = -\frac{\cos\theta}{\sin\theta}\,v_0,
$$

$$
v = \sqrt{v_r^2 + v_\theta^2} = \frac{v_0}{\sin\theta}.
$$
The boat's velocity is horizontal, and its component along the rope equals the reeling speed $v_0$, so $v\sin\theta = v_0$: the boat moves faster than the rope, and ever faster as it nears the shore. A common mistake is to treat the reeling velocity as a component of the boat's velocity, giving $v = v_0\sin\theta$.

## 1.7. Relative Motion

### 1.7.1. Absolute, Relative and Transport Motion

How are the observations of the same particle in different reference frames related?

**Definition 1.7.1 (Absolute, Relative and Transport Motion)** Take two reference frames and call one the fixed frame $S$ and the other the moving frame $S'$. The motion of the particle relative to $S$ is called the absolute motion, and its velocity $\boldsymbol{v}$ is called the **absolute velocity**; the motion of the particle relative to $S'$ is called the relative motion, and its velocity $\boldsymbol{v}'$ is called the **relative velocity**; the motion of $S'$ relative to $S$ is called the transport motion, and the velocity $\boldsymbol{u}$, relative to $S$, of the point of $S'$ that coincides with the particle is called the **transport velocity**.

"Fixed" and "moving" are only relative names; the two frames are on an equal footing. We first discuss the case in which $S'$ translates relative to $S$. All points of $S'$ then have the same velocity, and the transport velocity is the velocity of the origin $O'$ of $S'$.

### 1.7.2. The Galilean Velocity Transformation

Let the position vector of $O'$ relative to $O$ be $\boldsymbol{r}_0$, and let the position vectors of the particle relative to $O$ and $O'$ be $\boldsymbol{r}$ and $\boldsymbol{r}'$; then $\boldsymbol{r} = \boldsymbol{r}' + \boldsymbol{r}_0$. Differentiating with respect to time gives:

**Theorem 1.7.1 (Galilean Velocity Transformation)** Let the moving frame $S'$ translate relative to $S$ with transport velocity $\boldsymbol{u} = \dot{\boldsymbol{r}}_0$ and transport acceleration $\boldsymbol{a}_0 = \dot{\boldsymbol{u}}$. Then

$$
\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}, \qquad \boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{a}_0.
$$
In particular, when $S'$ moves relative to $S$ with constant velocity, $\boldsymbol{a} = \boldsymbol{a}'$: the accelerations measured in the two frames are the same.

Some remarks:

1. These relations presuppose the classical absolute space and time. The relation $\boldsymbol{r} = \boldsymbol{r}' + \boldsymbol{r}_0$ assumes that length measurements are independent of the frame (absoluteness of space); differentiating with respect to $t$ to obtain the relations for velocity and acceleration assumes that the two frames use the same time, $t = t'$ (absoluteness of time). They are excellent approximations for $u \ll c$ ($c$ is the speed of light in vacuum); when $u$ approaches $c$ they must be replaced by the relativistic velocity transformation of [5.1.8](/5.1.8).
2. The composition and resolution of velocities should not be confused with the Galilean velocity transformation. The former writes one vector as the sum of several vectors in a single reference frame and is always valid; the latter relates measurements in two reference frames and holds only approximately at low speeds.
3. When $S'$ translates relative to $S$, the transport velocity $\boldsymbol{u}$ and transport acceleration $\boldsymbol{a}_0$ do not depend on the particle's position in $S'$. If $S'$ rotates uniformly relative to $S$, then $\boldsymbol{u} = \boldsymbol{\omega}\times\boldsymbol{r}$ depends on the particle's position; the velocity transformation $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$ still holds, but in the acceleration transformation, besides the transport acceleration, there is an additional term, the Coriolis acceleration $2\boldsymbol{\omega}\times\boldsymbol{v}'$. Its origin and physical effects are discussed in Section 2.6 of [5.1.2](/5.1.2).

**Example 1.7.1** Raindrops fall vertically, and a cyclist needs only a sheet of plastic over the chest to stay dry. Let the velocity of the raindrops relative to the ground be $\boldsymbol{v}_{\mathrm{R}}$ (vertically downward) and that of the cyclist relative to the ground be $\boldsymbol{v}_{\mathrm{B}}$ (horizontally forward). Taking the cyclist as the moving frame, the transport velocity is $\boldsymbol{v}_{\mathrm{B}}$, and the velocity of the raindrops relative to the cyclist is

$$
\boldsymbol{v}' = \boldsymbol{v}_{\mathrm{R}} - \boldsymbol{v}_{\mathrm{B}},
$$
directed backward and downward, at an angle $\arctan(v_{\mathrm{B}}/v_{\mathrm{R}})$ to the vertical. To the cyclist the rain comes slanting in from the front, so covering the chest suffices.

**Example 1.7.2** A wheel of radius $R$ rolls without slipping on a horizontal plane: at every instant the contact point $P$ of the wheel with the ground has zero velocity relative to the ground. The velocity of the wheel center $C$ relative to the ground is $\boldsymbol{v}_C$. (1) Show that the velocity of $P$ relative to the center is $-\boldsymbol{v}_C$. (2) Find the velocity, relative to the ground, of an arbitrary point $A$ on the rim, with the position of $A$ given by $\theta = \angle ACP$.

(1) Let $S'$ be the frame translating with the wheel center, so that the transport velocity is $\boldsymbol{v}_C$. By the Galilean velocity transformation, the velocity of $P$ relative to the ground is $\boldsymbol{v}_P = \boldsymbol{v}'_P + \boldsymbol{v}_C$; the no-slip condition is $\boldsymbol{v}_P = \boldsymbol{0}$, so $\boldsymbol{v}'_P = -\boldsymbol{v}_C$.

(2) In $S'$ the wheel moves in a circle about $C$. By (1), all points on the rim have speed $v_C$ relative to $C$, that is, the angular velocity is $\omega = v_C/R$. The velocity $\boldsymbol{v}'_A$ of $A$ relative to $C$ has magnitude $v_C$ and is perpendicular to $CA$, so $\boldsymbol{v}_A = \boldsymbol{v}'_A + \boldsymbol{v}_C$ is the sum of two vectors, both of magnitude $v_C$, with angle $\pi - \theta$ between them:

$$
v_A = 2v_C\sin\frac{\theta}{2}.
$$
Alternatively, take $P$ as the reference point: $P$ is instantaneously at rest, and at this instant the wheel is equivalent to one rotating about $P$ ($P$ is the instantaneous center of rotation, see [5.1.5](/5.1.5)) with the same angular velocity $\omega = v_C/R$, so $v_A = \omega\cdot\overline{PA} = \dfrac{v_C}{R}\cdot 2R\sin\dfrac\theta2$, directed perpendicular to $PA$. The speed at the highest point ($\theta = \pi$) is $2v_C$, and at the contact point it is zero.

![The path of a point on the rim of a wheel rolling without slipping is a cycloid. The figure shows the velocities of points on the rim at one instant (arrows, scaled down); each is perpendicular to the line joining the point to the contact point P, with magnitude proportional to the distance from P](./plots/cycloid-velocities.py)

## Summary

| Topic | Key points |
|---|---|
| Two kinds of problems | $\boldsymbol{r}(t) \xrightarrow{\text{differentiate}} \boldsymbol{v}(t) \xrightarrow{\text{differentiate}} \boldsymbol{a}(t)$; from $\boldsymbol{a}$ and the initial conditions $\boldsymbol{r}_0$, $\boldsymbol{v}_0$, integrate to find the motion |
| Cartesian coordinates | Unit vectors constant, components independent; uniformly accelerated motion $\boldsymbol{r} = \boldsymbol{r}_0 + \boldsymbol{v}_0t + \frac12\boldsymbol{a}t^2$ |
| Intrinsic coordinates | $\boldsymbol{a} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\boldsymbol{e}_{\mathrm{t}} + \dfrac{v^2}{\rho}\boldsymbol{e}_{\mathrm{n}}$: the tangential part changes the speed, the normal part changes the direction |
| Circular motion | $\omega = \dot\theta$, $\alpha = \dot\omega$; $v = R\omega$, $a_{\mathrm{t}} = R\alpha$, $a_{\mathrm{n}} = R\omega^2$ |
| Plane polar coordinates | $\boldsymbol{v} = \dot r\boldsymbol{e}_r + r\dot\theta\boldsymbol{e}_\theta$; $\boldsymbol{a} = (\ddot r - r\dot\theta^2)\boldsymbol{e}_r + (r\ddot\theta + 2\dot r\dot\theta)\boldsymbol{e}_\theta$ |
| Relative motion | Between translating frames $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$, $\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{a}_0$; based on absolute space and time, valid only at low speeds |

## Questions

1. A particle moves in a plane with $x = x(t)$, $y = y(t)$. One person first computes $r = \sqrt{x^2 + y^2}$ and then uses $v = \dot r$, $a = \ddot r$ for the magnitudes of the velocity and acceleration; another uses $v = \sqrt{\dot x^2 + \dot y^2}$, $a = \sqrt{\ddot x^2 + \ddot y^2}$. Which method is correct?
   Hint: The second is correct. $\dot r$ is only the radial velocity and omits the transverse velocity $r\dot\theta$; nor is $\ddot r$ the magnitude of the acceleration (Section 1.6).
2. At some instant a particle has velocity $\boldsymbol{v}$. In which directions can its acceleration point?
   Hint: Given only the velocity at one instant, the acceleration can point in any direction. The component of the acceleration along $\boldsymbol{v}$ determines whether the speed increases or decreases, and the component perpendicular to $\boldsymbol{v}$ determines to which side the path bends and how sharply ($\rho = v^2/a_{\mathrm{n}}$). Conversely, if the trajectory near this point is known, the acceleration cannot point to the outer side of the bend.
3. A planet moves on an elliptical orbit, with its acceleration always directed toward the focus occupied by the Sun. Does its speed increase or decrease as it moves from aphelion to perihelion?
   Hint: The projection of the acceleration on the velocity is the tangential acceleration. From aphelion to perihelion the distance to the Sun decreases, the velocity makes an acute angle with the acceleration directed toward the Sun, and the speed increases; the reverse holds from perihelion to aphelion.
4. Is the acceleration of a particle in circular motion necessarily perpendicular to its velocity?
   Hint: No. Only in uniform circular motion, where the tangential acceleration is zero, does the acceleration point to the center.
