---
title: Rotation of Rigid Bodies
description: Motion of a rigid body and its angular velocity; the law of rotation about a fixed axis and the moment of inertia (parallel- and perpendicular-axis theorems); work, energy and angular momentum conservation for fixed-axis rotation; the relation between angular momentum and angular velocity, precession and nutation; degrees of freedom and Euler angles; plane motion of a rigid body (instantaneous center, rolling without slipping, König's theorem).
source_hash: 12a483b9271a
---

A rigid body is an idealized system of **particles** whose mutual distances never change. Hence all the laws for systems of particles in [5.1.3](/5.1.3) and [5.1.4](/5.1.4) (the **center-of-mass theorem**, the **angular momentum theorem**, the **work–energy principle**) apply to it without change, and the rigidity constraint reduces them to especially simple forms. For rotation about a fixed axis a single angular coordinate suffices; the **dynamics** equation $M=J\alpha$ corresponds one-to-one to **Newton's second law** $F=ma$, with the moment of inertia playing the role of mass. This chapter begins with the **kinematics** of a rigid body (the **angular velocity** does not depend on the base point), then treats the law of rotation about a fixed axis, the computation of moments of inertia, and the work–energy and angular momentum relations. It next discusses precession, which arises when the **angular momentum** is not parallel to the angular velocity, and from there introduces the notion of degrees of freedom. It ends with a short account of the plane motion of a rigid body (rolling). The mathematics used includes the **cross product** ($\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r}$), the **moment of inertia** as an integral ([2.2.12](/2.2.12)), and the principal axes of a **symmetric matrix** (the inertia tensor). The notion of degrees of freedom is used again in the equipartition theorem of thermal physics ([5.2.1](/5.2.1)).

## 5.1. Motion of a Rigid Body

### 5.1.1. The Concept of a Rigid Body

**Definition 5.1.1 (Rigid Body)** A body whose shape and size do not change under any external force is called a **rigid body**; equivalently, it is a system of particles in which the distance between any two points remains constant.

The rigid body is an idealized model: it is infinitely stiff, does not deform under force, and a force acting on it is transmitted instantaneously throughout the body. As a special system of particles it obeys all the laws for such systems, but it also has kinematic and dynamic laws of its own.

### 5.1.2. Forms of Rigid-Body Motion

**Definition 5.1.2** The basic forms of rigid-body motion are:

1. **Translation**: the line joining any two points of the body remains parallel to itself during the motion. All points of a translating body move identically, so the motion of the center of mass is commonly used to represent the translation of the whole body.
2. **Rotation about a fixed point**: one point of the body is fixed, and at each instant the body rotates about some instantaneous axis through that point; if the instantaneous axis is fixed, the motion is **rotation about a fixed axis**.
3. **Plane motion**: all points of the body move parallel to a fixed plane, and the planes of their trajectories are parallel or coincident.
4. **General motion**: unrestricted free motion, which can be decomposed into a translation with a base point $O$ (chosen arbitrarily) and a rotation about the instantaneous axis through $O$.

Different base points give different translational parts, but the rotational part (the angular velocity) is the same: rotation is independent of the choice of base point. For a wheel rolling on the ground, for example, taking the hub as base point gives "translation of the hub plus rotation about the hub", while taking a point on the rim gives "translation of that point plus rotation about it"; the angular velocity is the same in both decompositions.

### 5.1.3. Kinematic Quantities of Rotation About a Fixed Point

**Definition 5.1.3** When a rigid body rotates about a fixed point $O$, the direction of the instantaneous axis and the rate of rotation are described by the **angular velocity** vector $\boldsymbol{\omega}$. It lies along the instantaneous axis, its sense is given by the right-hand rule from the sense of rotation, and its magnitude $\omega=\mathrm{d}\theta/\mathrm{d}t$ is the angular **speed**. The **angular acceleration** is $\boldsymbol{\alpha}=\dfrac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}$.

**Property 5.1.1** Let $\boldsymbol{r}$ be the **position vector** of a point $P$ of the body relative to the base point $O$. Then

$$
\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{r},\qquad
\boldsymbol{a}=\frac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}\times\boldsymbol{r}+\boldsymbol{\omega}\times\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t}=\boldsymbol{\alpha}\times\boldsymbol{r}+\boldsymbol{\omega}\times\boldsymbol{v},
$$
where $\boldsymbol{v}$ has magnitude $\omega r_\perp$ and $r_\perp$ is the distance from $P$ to the instantaneous axis. The term $\boldsymbol{\alpha}\times\boldsymbol{r}$ is the rotational **acceleration**, and $\boldsymbol{\omega}\times\boldsymbol{v}=\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$ points toward the instantaneous axis and is called the axial (centripetal) acceleration.

The angular velocity does not depend on the choice of base point. Let $\boldsymbol{\omega}$ and $\boldsymbol{\omega}'$ be the angular velocities obtained with base points $O$ and $O'$. For any point $P$ of the body,

$$
\boldsymbol{v}_P=\boldsymbol{v}_O+\boldsymbol{\omega}\times\overrightarrow{OP}=\boldsymbol{v}_{O'}+\boldsymbol{\omega}'\times\overrightarrow{O'P}.
$$
Taking $P=O'$ gives $\boldsymbol{v}_{O'}=\boldsymbol{v}_O+\boldsymbol{\omega}\times\overrightarrow{OO'}$. Substituting back and using $\overrightarrow{OP}=\overrightarrow{OO'}+\overrightarrow{O'P}$ yields $(\boldsymbol{\omega}-\boldsymbol{\omega}')\times\overrightarrow{O'P}=\boldsymbol{0}$ for all $P$, so $\boldsymbol{\omega}'=\boldsymbol{\omega}$. This is why "the angular velocity of a rigid body" is a meaningful notion.

In general $\boldsymbol{\alpha}$ and $\boldsymbol{\omega}$ have different directions, and $\boldsymbol{\alpha}$ need not lie along the instantaneous axis (for a spinning top, for instance, the instantaneous axis itself rotates).

### 5.1.4. Rotation About a Fixed Axis

In rotation about a fixed axis, $\boldsymbol{\omega}$ and $\boldsymbol{\alpha}$ both lie along the fixed axis (taken as the $z$ axis) and reduce to algebraic quantities. A single angular coordinate $\theta$ (measured from some reference direction) fixes the position of the body, with $\omega=\dot\theta$ and $\alpha=\dot\omega=\ddot\theta$; the sign indicates the positive or negative $z$ direction. A point at distance $r_\perp$ from the axis moves in a circle with

$$
v=r_\perp\omega,\qquad a_{\mathrm{t}}=\frac{\mathrm{d}v}{\mathrm{d}t}=r_\perp\alpha,\qquad a_{\mathrm{n}}=r_\perp\omega^2 .
$$
When $\alpha$ is constant (uniformly accelerated rotation), the formulas correspond one-to-one to those of uniformly accelerated rectilinear motion:

$$
\omega=\omega_0+\alpha t,\qquad \theta-\theta_0=\omega_0t+\frac12\alpha t^2,\qquad \omega^2-\omega_0^2=2\alpha(\theta-\theta_0).
$$

## 5.2. The Law of Rotation About a Fixed Axis

Regard the rigid body as a system of particles made up of infinitely many mass elements $\Delta m_i$. For a system of particles, the **angular momentum theorem** ([5.1.3](/5.1.3)) about a fixed point $O$ and about a fixed axis $z$ reads

$$
\boldsymbol{M}_{\mathrm{ext}}=\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t},\qquad M_{\mathrm{ext},z}=\frac{\mathrm{d}L_z}{\mathrm{d}t}.
$$
In rotation about a fixed axis, each mass element $\Delta m_i$ moves in a circle of radius $r_{i\perp}$ in a plane perpendicular to the axis, and its **velocity** $v_i=r_{i\perp}\omega$ is perpendicular to the radius, so

$$
L_z=\sum_i\Delta m_i\,v_ir_{i\perp}=\Big(\sum_i\Delta m_ir_{i\perp}^2\Big)\omega .
$$

**Definition 5.2.1 (Moment of Inertia)** The **moment of inertia** of a rigid body about the $z$ axis is, for a system of particles and for a continuous body respectively,

$$
J_z=\sum_i\Delta m_ir_{i\perp}^2,\qquad J_z=\int_mr_\perp^2\,\mathrm{d}m,
$$
where $r_\perp$ is the distance of the mass element from the axis. Its unit is $\mathrm{kg\,m^2}$.

Thus $L_z=J_z\omega$, and $M_{\mathrm{ext},z}=\sum_iF_{i\perp}r_{i\perp}\sin\varphi_i$ is the sum of the **torques** about the axis due to the components of the external forces in the plane perpendicular to the axis (the torques of the internal forces cancel in pairs).

**Theorem 5.2.1 (Law of Rotation)** For a rigid body rotating about a fixed axis, the net external torque about that axis equals the product of the body's moment of inertia about that axis and its angular acceleration:

$$
M=J\alpha .
$$

Here the subscript $z$ has been dropped. Comparing with Newton's second law, $M\leftrightarrow F$, $J\leftrightarrow m$, $\alpha\leftrightarrow a$: the moment of inertia measures the inertia of a body with respect to rotation.

## 5.3. Computing Moments of Inertia

### 5.3.1. Common Moments of Inertia

The moment of inertia is determined by the mass of the body and by how the mass is distributed relative to the axis (mass $m$, uniformly distributed):

| Body | Axis | $J$ |
|---|---|---|
| Thin ring (radius $R$) | Through the center, perpendicular to the plane of the ring | $mR^2$ |
| Disk or cylinder (radius $R$) | Central axis | $\frac12mR^2$ |
| Thin rod (length $l$) | Through the midpoint, perpendicular to the rod | $\frac1{12}ml^2$ |
| Thin rod (length $l$) | Through one end, perpendicular to the rod | $\frac13ml^2$ |
| Solid sphere (radius $R$) | Diameter | $\frac25mR^2$ |
| Thin spherical shell (radius $R$) | Diameter | $\frac23mR^2$ |

For the thin rod about its midpoint, for example, take the rod along the $x$ axis with linear density $m/l$: $J_C=\int_{-l/2}^{l/2}x^2\frac{m}{l}\,\mathrm{d}x=\frac1{12}ml^2$. The calculation for the sphere is in [Example 12.5.2](/2.2.12#ex-12.5.2).

### 5.3.2. Rules for Computing Moments of Inertia

1. Additivity: for the same axis, the moment of inertia of a body made of several parts is the sum of the moments of inertia of the parts, $J=\sum_iJ_i$.

**Theorem 5.3.1 (Parallel-Axis Theorem)** The moment of inertia $J$ of a rigid body about any axis equals its moment of inertia $J_C$ about the parallel axis through the center of mass plus $md^2$, where $d$ is the distance between the two axes:

$$
J=J_C+md^2 .
$$

**Proof** Take the axis through the center of mass as the $z$ axis, and let the other axis pass through the point $(d,0)$ in the plane perpendicular to the axes. A mass element is at position $(x_i,y_i)$, so

$$
J=\sum_i\Delta m_i\big[(x_i-d)^2+y_i^2\big]=\sum_i\Delta m_i(x_i^2+y_i^2)-2d\sum_i\Delta m_ix_i+d^2\sum_i\Delta m_i=J_C+md^2,
$$
because the center of mass is at the origin, so $\sum_i\Delta m_ix_i=0$. $\square$

It follows that among a family of parallel axes, the axis through the center of mass gives the smallest moment of inertia. For a thin rod about one end, $J_A=\frac1{12}ml^2+m\big(\frac l2\big)^2=\frac13ml^2$.

**Theorem 5.3.2 (Perpendicular-Axis Theorem)** For a thin flat plate, the moment of inertia about the $z$ axis perpendicular to the plate equals the sum of the moments of inertia about two mutually perpendicular $x$ and $y$ axes lying in the plane of the plate and passing through the same point:

$$
J_z=J_x+J_y .
$$

**Proof** For a mass element $\Delta m_i$ of the plate, the squared distance to the $z$ axis is $x_i^2+y_i^2$, and the squared distances to the $x$ and $y$ axes are $y_i^2$ and $x_i^2$ respectively (the plate is thin, so $z_i\approx0$). Hence $J_z=\sum_i\Delta m_i(x_i^2+y_i^2)=J_y+J_x$. $\square$

**Example 5.3.1** Find the moment of inertia of a uniform thin disk about a diameter.

**Solution** We know $J_z=\frac12mR^2$, and by symmetry $J_x=J_y$. The perpendicular-axis theorem gives $J_x=J_y=\frac12J_z=\frac14mR^2$.

**Example 5.3.2** A uniform cylinder has mass $m$, length $l$ and diameter $D$. Find its moment of inertia about an axis $z$ through the center of one end face and perpendicular to the cylinder's axis.

**Solution** Cut the cylinder along its axis into thin disks of thickness $\mathrm{d}x$. The disk at distance $x$ from the end face has mass $\mathrm{d}m=\frac{m}{l}\mathrm{d}x$. By Example 5.3.1, its moment of inertia about its own diameter parallel to $z$ is $\frac14\mathrm{d}m\big(\frac D2\big)^2$; by the parallel-axis theorem, its moment of inertia about the $z$ axis is $\mathrm{d}J_z=\frac14\big(\frac D2\big)^2\mathrm{d}m+x^2\,\mathrm{d}m$. Integrating,

$$
J_z=\int_0^l\Big[\frac{D^2}{16}+x^2\Big]\frac{m}{l}\,\mathrm{d}x=\frac{mD^2}{16}+\frac13ml^2 .
$$
As $D\to0$ this reduces to the result for a thin rod about one end.

## 5.4. Applications of the Law of Rotation

**Example 5.4.1 (Measuring the Moment of Inertia with a Falling Body)** A wheel of radius $R$ can rotate about a smooth horizontal axis $O$. A light string is wound around the rim, and a body of mass $m$ hangs from its lower end. The body is released from rest and is observed to fall a height $h$ in time $t$. The string does not slip on the wheel and does not stretch. Find the moment of inertia $J$ of the wheel about the axis $O$.

**Solution** Let $T$ be the tension in the string. The dynamical relations are $TR=J\alpha$ for the wheel and $mg-T=ma$ for the body. The kinematic relations are $a=\alpha R$ and $h=\frac12at^2$. Solving these together gives

$$
J=\Big(\frac{gt^2}{2h}-1\Big)mR^2 .
$$
Checks: the **dimension of a quantity** is consistent on both sides; for fixed $h$ and $m$, a larger $J$ means slower descent and a larger $t$, which is reasonable; for $J=0$ we get $h=\frac12gt^2$, which is free fall. This is one experimental method for determining a moment of inertia.

## 5.5. Work and Energy in Fixed-Axis Rotation

### 5.5.1. Work Done by a Torque

Suppose a force $\boldsymbol{F}$ acts on a point of the body at distance $r_\perp$ from the axis. When the body turns through $\mathrm{d}\theta$, the **displacement** of the point of application has magnitude $r_\perp\,\mathrm{d}\theta$, and only the tangential component of $\boldsymbol{F}$ in the plane of rotation does **work**:

$$
\mathrm{d}W=F_\perp\cos\varphi\cdot r_\perp\,\mathrm{d}\theta=M\,\mathrm{d}\theta,\qquad W=\int_{\theta_1}^{\theta_2}M\,\mathrm{d}\theta,
$$
where $\varphi$ is the angle between $F_\perp$ and the tangential direction and $M$ is the torque of the force about the axis. This is the accumulation of the torque over angle; the **power** is $P=M\omega$.

In considering the energy of a rigid body, the work of internal forces can be ignored: the work done by a pair of internal forces depends only on the relative displacement of the two particles ([Property 4.3.1](/5.1.4#pty-4.3.1)), and the distance between any two points of a rigid body is constant, so the total work of the internal forces is zero. Only the work of the external forces (external torques) needs to be computed.

### 5.5.2. The Work–Energy Theorem for Fixed-Axis Rotation

By the law of rotation,

$$
W=\int_{\theta_1}^{\theta_2}J\frac{\mathrm{d}\omega}{\mathrm{d}t}\,\mathrm{d}\theta=\int_{\omega_1}^{\omega_2}J\omega\,\mathrm{d}\omega=\frac12J\omega_2^2-\frac12J\omega_1^2 .
$$
The quantity $\frac12J\omega^2$ is called the *rotational kinetic energy* of the body. It is exactly the sum of the **kinetic energies** of the mass elements: $\sum_i\frac12\Delta m_iv_i^2=\frac12\big(\sum_i\Delta m_ir_{i\perp}^2\big)\omega^2=\frac12J\omega^2$.

**Theorem 5.5.1 (Work–Energy Theorem for Fixed-Axis Rotation)** The work done by the net external torque on a body rotating about a fixed axis equals the increase of its rotational kinetic energy:

$$
W=\Delta\Big(\frac12J\omega^2\Big).
$$

### 5.5.3. Gravitational Potential Energy of a Rigid Body

The gravitational **potential energy** of the system consisting of the rigid body and the Earth equals the sum of the gravitational potential energies of the mass elements:

$$
E_{\mathrm{p}}=\sum_i\Delta m_igh_i=mg\frac{\sum_i\Delta m_ih_i}{m}=mgh_C,
$$
which is the gravitational potential energy the body would have if all its mass were concentrated at the center of mass.

### 5.5.4. Examples

For a system containing rigid bodies, the work–energy principle and the **law of conservation of mechanical energy** continue to hold.

**Example 5.5.1** A uniform straight rod $AB$ of mass $m$ and length $l$ can rotate about a smooth horizontal axis $O$, with $AO=l/4$. The rod is released from rest in the horizontal position. Find its angular velocity $\omega$ and the force $\boldsymbol{N}$ exerted on it by the axis when it has swung down to an angle $\theta$ below the horizontal.

**Solution** The center of mass $C$ is at distance $OC=l/4$ from the axis, so by the parallel-axis theorem

$$
J_O=\frac1{12}ml^2+m\Big(\frac l4\Big)^2=\frac7{48}ml^2 .
$$
Only gravity does work on the system of rod and Earth, so the **mechanical energy** is conserved: $\frac12J_O\omega^2-mg\frac l4\sin\theta=0$, and

$$
\omega=\sqrt{\frac{24g\sin\theta}{7l}}=2\sqrt{\frac{6g\sin\theta}{7l}} .
$$
To find the force from the axis we use the **center-of-mass theorem** $\boldsymbol{N}+m\boldsymbol{g}=m\boldsymbol{a}_C$. Let $\boldsymbol{e}_{\mathrm{n}}$ point from $C$ to $O$ and $\boldsymbol{e}_{\mathrm{t}}$ along the direction of motion of the center of mass (perpendicular to the rod, obliquely downward). The center of mass moves in a circle of radius $l/4$, so

$$
a_{C\mathrm{n}}=\omega^2\frac l4=\frac67g\sin\theta,\qquad a_{C\mathrm{t}}=\alpha\frac l4=\frac{mg\frac l4\cos\theta}{J_O}\cdot\frac l4=\frac37g\cos\theta .
$$
The components of gravity along the two directions are $-mg\sin\theta$ and $mg\cos\theta$, hence

$$
N_{\mathrm{n}}-mg\sin\theta=ma_{C\mathrm{n}},\qquad N_{\mathrm{t}}+mg\cos\theta=ma_{C\mathrm{t}},
$$
which give $N_{\mathrm{n}}=\frac{13}7mg\sin\theta$ and $N_{\mathrm{t}}=-\frac47mg\cos\theta$; that is,

$$
\boldsymbol{N}=\frac{13}{7}mg\sin\theta\,\boldsymbol{e}_{\mathrm{n}}-\frac47mg\cos\theta\,\boldsymbol{e}_{\mathrm{t}},\qquad N=\frac{mg}{7}\sqrt{153\sin^2\theta+16} .
$$

## 5.6. The Angular Momentum Theorem for Fixed-Axis Rotation

Integrating the angular momentum theorem about an axis for a system of particles over time and using $L_z=J_z\omega$, we obtain:

**Theorem 5.6.1 (Angular Momentum Theorem for Fixed-Axis Rotation)** The **angular impulse** of the net external torque on a body rotating about a fixed axis equals the change in its angular momentum:

$$
\int_{t_1}^{t_2}M_{\mathrm{ext},z}\,\mathrm{d}t=J_z\omega_2-J_z\omega_1,\qquad M_{\mathrm{ext},z}\,\mathrm{d}t=\mathrm{d}(J_z\omega).
$$
The form $\mathrm{d}(J_z\omega)$ is used so that bodies whose moment of inertia changes (such as a spinning person drawing in the arms) are also covered.

**Theorem 5.6.2 (Conservation of Angular Momentum for Fixed-Axis Rotation)** If $M_{\mathrm{ext},z}=0$, then $L_z=J_z\omega$ remains constant.

In a system whose moment of inertia can change, $\omega$ increases when $J$ decreases: a figure skater spins faster on drawing in the arms, and a diver who tucks the knees completes more somersaults.

The gyroscope is an important application of angular momentum conservation. A rotor spinning at high speed is mounted in a gimbal made of two or three mutually perpendicular frames; the gimbal exerts almost no torque on the rotor, so the rotor's spin axis keeps its direction fixed in space, which can be used for navigation. The "incense burner in the quilt" known in the Western Han dynasty used the same gimbal so that the mouth of the burner always faced upward however it rolled (it relies on gravity keeping the burner body vertical, not on conservation of angular momentum).

**Example 5.6.1 (Two Wheels Brought into Contact)** Two wheels rotate about their own fixed parallel axes, with moments of inertia $J_1$, $J_2$, radii $r_1$, $r_2$ and initial angular velocities $\omega_{10}$, $\omega_{20}$. Their rims are brought into contact, and friction eventually makes them rotate without slipping relative to each other. Can the final angular velocities be found from conservation of angular momentum about an axis?

**Solution** No. Angular momentum can be transferred among the bodies of a system of rigid bodies, and the total angular momentum of the system about an axis is conserved, but it must be the same axis. Here the two wheels rotate about different axes, the torques of the friction forces at the contact point about the two axes do not cancel, and each bearing also supplies an external force, so the total angular momentum of the two wheels about neither axis is conserved.

The correct approach is to apply the angular momentum theorem to each wheel separately. Take the positive sense of rotation of each wheel so that the linear velocities of the two rims at the contact point, $v_1=\omega_1r_1$ and $v_2=\omega_2r_2$, are positive in the same direction. Let $v_1>v_2$ and let the friction force have magnitude $f$; it opposes the motion of wheel 1 and drives wheel 2:

$$
J_1\frac{\mathrm{d}\omega_1}{\mathrm{d}t}=-fr_1,\qquad J_2\frac{\mathrm{d}\omega_2}{\mathrm{d}t}=fr_2 .
$$
Eliminating $f$ gives the conserved quantity $\dfrac{J_1\omega_1}{r_1}+\dfrac{J_2\omega_2}{r_2}$ (which is not an angular momentum). In the final state there is no relative slipping, $\omega_1r_1=\omega_2r_2=v$, and

$$
v=\frac{J_1\omega_{10}/r_1+J_2\omega_{20}/r_2}{J_1/r_1^2+J_2/r_2^2},\qquad \omega_1=\frac v{r_1},\quad\omega_2=\frac v{r_2} .
$$

**Example 5.6.2** A uniform disk of mass $2m$ and radius $R$ can rotate in a vertical plane about a smooth horizontal axis $O$ and is initially at rest. A lump of clay of mass $m$ strikes the highest point $P$ of the disk obliquely with speed $v_0$ and sticks to it; $\boldsymbol{v}_0$ makes an angle $\theta=60^\circ$ with the horizontal. Find the angular velocity $\omega$, the angular acceleration $\alpha$ and the force $\boldsymbol{N}$ exerted by the axis on the disk when $P$ has rotated to the height of $O$ (on the $x$ axis).

**Solution** The process has two stages. In the collision, for the system of clay and disk, the torques of gravity and of the axis force about the axis $O$ vanish at the instant of impact (the axis force passes through $O$; the collision time is so short that the angular impulse of the gravitational torque can be neglected), so angular momentum about $O$ is conserved. Let $\omega_0$ be the angular velocity just after the collision. Only the horizontal component of $\boldsymbol{v}_0$ has a torque about $O$:

$$
Rmv_0\cos\theta=\Big(\frac12\cdot2mR^2+mR^2\Big)\omega_0=2mR^2\omega_0,\qquad \omega_0=\frac{v_0}{4R}.
$$
In the rotation stage, the clay and disk form a single rigid body with $J=2mR^2$. The mechanical energy of the system of clay, disk and Earth is conserved. Taking the gravitational potential energy of the clay to be zero when $P$ is on the $x$ axis,

$$
\frac12J\omega_0^2+mgR=\frac12J\omega^2,\qquad \omega=\frac{\sqrt{v_0^2+16gR}}{4R}.
$$
At this moment the net external torque is $mgR$ (the weight of the disk passes through the axis), so $\alpha=\dfrac{mgR}{2mR^2}=\dfrac{g}{2R}$.

To find the axis force we use the center-of-mass theorem. The center of mass $C$ of the system lies on the line from $O$ to the clay, with $OC=\dfrac{mR}{3m}=\dfrac R3$. The **tangential acceleration** of the center of mass, $a_{C\mathrm{t}}=\alpha R/3$, points in the $-y$ direction, and the **normal acceleration** $a_{C\mathrm{n}}=\omega^2R/3$ points in the $-x$ direction (toward $O$). From $\boldsymbol{N}+3m\boldsymbol{g}=3m\boldsymbol{a}_C$,

$$
N_x=-3m\cdot\frac{\omega^2R}3=-m\Big(\frac{v_0^2}{16R}+g\Big),\qquad N_y-3mg=-3m\cdot\frac{\alpha R}3,\quad N_y=\frac52mg .
$$
$N_x<0$ means that the horizontal component of the axis force points in the $-x$ direction. The same result can be obtained by analyzing the clay and the disk as separate free bodies with Newton's laws.

## 5.7. Precession

### 5.7.1. Relation Between the Angular Momentum and the Angular Velocity of a Rigid Body

The angular momentum $\boldsymbol{L}$ of a rigid body need not have the same direction as its angular velocity $\boldsymbol{\omega}$. Consider, for example, a light rod with a small ball of mass $m$ fixed at each end, whose midpoint $O$ lies on the $z$ axis, with the rod inclined to the $z$ axis and constrained to rotate about it. The angular momentum $\boldsymbol{r}\times m\boldsymbol{v}$ of each ball is perpendicular to the rod and not along the $z$ axis, so the total angular momentum $\boldsymbol{L}_O$ about $O$ is not parallel to $\boldsymbol{\omega}$ and rotates about the $z$ axis together with the rod. Maintaining this rotation requires the bearings to supply a torque continuously (this is why the bearings of an unbalanced rotor experience periodic forces).

In general, about a fixed point $O$,

$$
\boldsymbol{L}=\sum_i\Delta m_i\,\boldsymbol{r}_i\times(\boldsymbol{\omega}\times\boldsymbol{r}_i)=J\boldsymbol{\omega},\qquad
J=\begin{bmatrix}J_{xx}&J_{xy}&J_{xz}\\J_{xy}&J_{yy}&J_{yz}\\J_{xz}&J_{yz}&J_{zz}\end{bmatrix},
$$
where $J_{xx}=\sum\Delta m_i(y_i^2+z_i^2)$, $J_{xy}=-\sum\Delta m_ix_iy_i$, and so on. The matrix $J$ is called the inertia tensor. It is a real **symmetric matrix**, so by the **spectral theorem** ([2.1.7](/2.1.7)) there exist three mutually perpendicular principal axes, the eigenvectors of $J$. For rotation about the $k$-th principal axis, $\boldsymbol{L}=J_k\boldsymbol{\omega}$, so the two are parallel, and the corresponding **eigenvalue** $J_k$ is called a principal moment of inertia. For a body of uniform mass and symmetric geometry, an axis of geometric symmetry is a principal axis: when the body spins about it, the spin angular momentum is parallel to the spin angular velocity.

In the example above, what happens to the rod if the constraint is cut (so that the system is subject to no torque about $O$)? Now $\boldsymbol{L}_O$ is conserved, while $\boldsymbol{\omega}$ is no longer along the $z$ axis: the rod rotates about the direction of $\boldsymbol{L}_O$ (the axis $OO'$ through $O$ perpendicular to the rod).

### 5.7.2. Precession

The phenomenon in which the spin axis of a rapidly spinning body itself rotates about another axis is called *precession*; an example is the slow rotation of the spin axis of a toy top about the vertical.

Consider a symmetric top with fixed support point $O$ and center of mass $C$ on the symmetry axis, $OC=r_C$, the symmetry axis making an angle $\theta$ with the vertical. The top spins rapidly about its symmetry axis with angular velocity $\boldsymbol{\omega}$. At high spin rate the total angular momentum is approximately the spin angular momentum $\boldsymbol{L}=J\boldsymbol{\omega}$, directed along the symmetry axis. The torque of gravity about $O$, $\boldsymbol{M}=\boldsymbol{r}_C\times m\boldsymbol{g}$, is horizontal and perpendicular to $\boldsymbol{L}$. By the angular momentum theorem $\mathrm{d}\boldsymbol{L}=\boldsymbol{M}\,\mathrm{d}t$, we have $\mathrm{d}\boldsymbol{L}\parallel\boldsymbol{M}\perp\boldsymbol{L}$: at each instant $\boldsymbol{L}$ changes only in direction and not in magnitude, and the torque $\boldsymbol{M}$ changes direction accordingly so that this relation always holds. Hence the tip of $\boldsymbol{L}$ moves in a circle in a horizontal plane, and the spin axis rotates about the vertical; the top precesses instead of falling over.

If the spin axis turns through $\mathrm{d}\Theta$ about the vertical in time $\mathrm{d}t$, then $\lvert\mathrm{d}\boldsymbol{L}\rvert=L\sin\theta\,\mathrm{d}\Theta=M\,\mathrm{d}t$, and the angular velocity of precession is

$$
\varOmega=\frac{\mathrm{d}\Theta}{\mathrm{d}t}=\frac{M}{L\sin\theta}=\frac{mgr_C}{J\omega} .
$$
The faster the spin, the slower the precession. Once the precession is steady, the total angular velocity of the body is $\boldsymbol{\omega}+\boldsymbol{\varOmega}$; at high spin rate $\varOmega\ll\omega$, so the total angular velocity is approximately $\boldsymbol{\omega}$, which is precisely the condition for the approximation above to hold. A more exact analysis shows that, in addition to precessing, the spin axis also undergoes a small periodic up-and-down oscillation, called *nutation*.

This gyroscopic effect can be helpful or harmful. When a ship turns, the angular momentum of a rapidly spinning turbine rotor on board must change direction; the bearings must supply the corresponding torque and bear additional forces, which in severe cases can damage them. Conversely, the gyroscopic effect of a large gyrostabilizer can resist the rolling caused by waves and keep the hull steady.

**Example 5.7.1 (Precession of the Earth)** The Earth is approximately an oblate spheroid spinning rapidly about its axis, which makes an angle of about $23.4^\circ$ with the normal to the plane of its orbit (the ecliptic). The gravitational pulls of the Sun and the Moon on the Earth's equatorial bulge are unequal (the nearer side is pulled harder) and produce a torque that makes the Earth's spin axis precess about the normal to the ecliptic with a period of about $2.58\times10^4$ years (the precession of the equinoxes); the Moon contributes about twice as much as the Sun. As a result the direction of the north celestial pole moves slowly among the stars: the present pole star is Polaris ($\alpha$ Ursae Minoris), and in about 12,000 years the north celestial pole will be near Vega ($\alpha$ Lyrae).

### 5.7.3. Degrees of Freedom

**Definition 5.7.1 (Degrees of Freedom)** The number of independent coordinates needed to determine the position (configuration) of a mechanical system in space is called the number of **degrees of freedom** of the system.

The degrees of freedom are directly related to the geometric constraints:

- An unconstrained particle has 3 degrees of freedom, since $x$, $y$ and $z$ are independent. A particle constrained to move on a surface, such as $z=z(x,y)$, has 2; a particle constrained to move on a curve, such as $y=y(x)$, $z=z(x)$, has 1.
- A free rigid body has 6 degrees of freedom. Once three non-collinear points $A$, $B$, $C$ of the body are fixed, the body is completely fixed: after $A$ is fixed the body can still rotate about $A$; after $B$ is also fixed it can still rotate about $AB$; once $C$ is fixed too it cannot move. The three points have 9 coordinates altogether, and the three conditions that the distances $AB$, $BC$, $CA$ are constant reduce the number of independent coordinates by 3, so there are 6 degrees of freedom.

The 6 degrees of freedom of a rigid body split into 3 for the translation of the base point and 3 for the rotation about it. The rotation is usually described by three *Euler angles*: the precession angle $\psi$ (the angle through which the spin axis turns about the fixed axis), the nutation angle $\theta$ (the angle between the spin axis and the fixed axis), and the spin angle $\varphi$ (the angle turned about the spin axis). A constrained rigid body has fewer degrees of freedom: 3 for rotation about a fixed point, 3 for plane motion, and 1 for rotation about a fixed axis.

The degrees of freedom here are the configurational degrees of freedom of a mechanical system. They are a different concept from degrees of freedom in statistics (the number of independent observations minus the number of constraints), although both count "the number of independent variables". The translational, rotational and vibrational degrees of freedom of molecules in thermal physics ([5.2.1](/5.2.1)) are an application of the concept in this section.

## 5.8. Introduction to the Plane Motion of a Rigid Body

### 5.8.1. Basic Concepts and Kinematic Relations

In the plane motion of a rigid body, choose any plane parallel to the planes of the trajectories as the reference plane. All points on any straight line perpendicular to the reference plane move identically, so the motion of the points of the reference plane represents the motion of the whole body. Choose a point of the reference plane as the base point; the line through it perpendicular to the reference plane is called the base axis. The motion of the points of the reference plane decomposes into a translation of the base point (2 degrees of freedom) and a rotation about the base point (1 degree of freedom); the plane motion of the whole body is the translation of the base axis plus the rotation about it. Choosing the center of mass as base point simplifies the analysis of dynamics.

The velocity of any point $A$ of the reference plane is

$$
\boldsymbol{v}_A=\boldsymbol{v}_O+\boldsymbol{\omega}\times\boldsymbol{R},\qquad \boldsymbol{R}=\overrightarrow{OA},
$$
where $\boldsymbol{v}_O$ is the velocity of the base point $O$, and $\boldsymbol{\omega}$ is perpendicular to the reference plane and independent of the choice of base point (Section 5.1.3).

**Definition 5.8.1 (Instantaneous Center)** In the plane motion of a rigid body (with $\omega\ne0$), there is a unique point $P$ in the reference plane whose instantaneous velocity is zero, called the **instantaneous center of rotation**; the line through it perpendicular to the reference plane is called the instantaneous axis.

Taking the instantaneous center as base point, $\boldsymbol{v}_A=\boldsymbol{\omega}\times\boldsymbol{R}$ with $\boldsymbol{R}=\overrightarrow{PA}$ and $\boldsymbol{v}_A\perp\boldsymbol{R}$: at each instant the body moves as if in pure rotation about the instantaneous axis, so choosing the instantaneous center as base point simplifies the analysis of kinematics. The position of the instantaneous center generally changes with time; its velocity is zero, but its acceleration is not necessarily zero; it may lie inside or outside the body. There are two convenient ways to locate the instantaneous center:

1. Given the velocity $\boldsymbol{v}_A$ of one point $A$ and $\boldsymbol{\omega}$: the instantaneous center lies on the line through $A$ perpendicular to $\boldsymbol{v}_A$, at distance $PA=v_A/\omega$, in the direction of $\boldsymbol{\omega}\times\boldsymbol{v}_A$.
2. Given the directions of the velocities of two points $A$ and $B$ (not parallel): draw the perpendiculars to the velocities through $A$ and $B$; their intersection is the instantaneous center.

A uniform cylinder (disk, ring, sphere) that rolls on a plane or curved surface without relative slipping is said to undergo *rolling without slipping*. In this case the contact point $P$ is at rest relative to the surface and is the instantaneous center. If the surface is at rest, the velocity and tangential acceleration of the center of mass $C$ of a rolling body of radius $r$ satisfy

$$
v_C=\omega r,\qquad a_C=\alpha r,
$$
and on a plane $a_C$ is simply the acceleration of the center of mass.

### 5.8.2. Dynamical Relations

1. **Center-of-mass theorem**: $\boldsymbol{F}_{\mathrm{ext}}=m\boldsymbol{a}_C$.
2. Law of rotation about the base axis through the center of mass: $M_{\mathrm{ext},C}=J_C\alpha$. The **center-of-mass frame** is in general not an **inertial frame**, but the translational **inertial force** acts effectively at the center of mass and has zero torque about an axis through it, so the law of rotation keeps its form (see the angular momentum theorem in the center-of-mass frame in [5.1.3](/5.1.3)).
3. About the instantaneous axis: if the acceleration of the instantaneous center is directed along the line joining it to the center of mass, the torque of the inertial force about the instantaneous axis is also zero, so $M_{\mathrm{ext},P}=J_P\alpha$ holds about the instantaneous axis as well. For a uniform cylinder rolling without slipping on a plane, the acceleration of the contact point points toward the center of mass, which satisfies this condition.
4. Angular momentum: about the base axis through the center of mass, $M_{\mathrm{ext},C}=\dfrac{\mathrm{d}L_C}{\mathrm{d}t}$ with $L_C=J_C\omega$; about a fixed axis $O$ parallel to the axis through the center of mass, $L_O=J_C\omega+(\boldsymbol{r}_C\times m\boldsymbol{v}_C)_z$, where $\boldsymbol{r}_C$ is the perpendicular position vector of the center of mass relative to the axis $O$.

**Example 5.8.1** A uniform sphere of mass $m$ and radius $R$ rolls without slipping on a horizontal plane with center-of-mass speed $v_C$. Find its angular momentum about a fixed axis $O$ in the ground perpendicular to the direction of motion. Is it conserved?

**Solution** $L_O=J_C\omega+mv_CR=\frac25mR^2\cdot\frac{v_C}{R}+mv_CR=\frac75mv_CR$ (the two terms have the same direction). When the sphere rolls uniformly, the lines of action of gravity (acting at the center of mass) and of the normal force (acting at the contact point) are both vertical, at the same horizontal distance from the axis $O$ and on opposite sides, so their torques about $O$ cancel and no friction is needed; hence $L_O$ is conserved.

For the energy, by **König's theorem** ([Theorem 4.10.1](/5.1.4#thm-4.10.1)) the kinetic energy of a rigid body equals the translational kinetic energy of the center of mass plus the rotational kinetic energy about the base axis through the center of mass:

$$
E_{\mathrm{k}}=\frac12mv_C^2+\frac12J_C\omega^2 .
$$
Correspondingly, the **work–energy theorem** splits into two parts:

$$
\Delta\Big(\frac12mv_C^2\Big)=\int\boldsymbol{F}_{\mathrm{ext}}\cdot\mathrm{d}\boldsymbol{r}_C,\qquad
\Delta\Big(\frac12J_C\omega^2\Big)=\int M_{\mathrm{ext},C}\,\mathrm{d}\theta,
$$
The change in the translational kinetic energy of the center of mass equals the work done by the external forces "on the center of mass" (force times displacement of the center of mass), and the change in rotational kinetic energy equals the work done by the external torque about the base axis through the center of mass; their sum $\Delta E_{\mathrm{k}}$ equals the total work of the external forces.

**Example 5.8.2** A uniform sphere of mass $m$ and radius $R$ rolls without slipping on a horizontal plane under a horizontal force $F$. The point of application $A$ lies on the line joining the contact point $P$ and the center of mass $C$, with $AC=d$ ($A$ above $C$). Find the static friction force $f$ at the contact point.

**Solution** Let the friction force have the same direction as $F$ (forward). The center-of-mass theorem gives $F+f=ma_C$. Taking the sense of rotation that makes the sphere roll forward as positive, the law of rotation about the axis through the center of mass gives $Fd-fR=J_C\alpha=\frac25mR^2\alpha$. The condition for rolling without slipping is $a_C=R\alpha$. Solving,

$$
f=\frac{5d-2R}{7R}F,\qquad a_C=\frac{5(d+R)}{7mR}F>0,\qquad \alpha=\frac{5(d+R)}{7mR^2}F>0 .
$$
For $d>\frac25R$, $f$ has the same direction as $F$; for $d=\frac25R$, $f=0$ (this is the center of percussion relative to the contact point); for $d<\frac25R$, $f$ is opposite to $F$. The sphere always accelerates forward and accelerates in rotation.

**Example 5.8.3** A cylinder of mass $m$, radius $R$ and moment of inertia $J$ about its central axis starts from rest and rolls without slipping on a fixed incline of inclination $\theta$. (1) Is there a friction force at the contact point? If so, what is its role, and does it do work? (2) Find the velocity $v_C$ of the center of mass, the angular velocity $\omega$ and the friction force $f$ when the cylinder has descended a height $h$.

**Solution** (1) It is not easy to decide directly in the **reference frame** of the incline. In the frame whose base point is the center of mass, the cylinder rotates about a fixed axis, and the torques of gravity and of the normal force of the incline about the axis through the center of mass are both zero; to make the cylinder accelerate in rotation there must be a static friction force, directed up the incline (opposite to the motion of the center of mass), whose torque about the axis through the center of mass is nonzero.

In the frame of the incline, the static friction force does no work: for the elementary displacement of the contact point $O$,

$$
\mathrm{d}W_f=\boldsymbol{f}\cdot\mathrm{d}\boldsymbol{r}_O=\boldsymbol{f}\cdot(\boldsymbol{v}_{O,C}+\boldsymbol{v}_C)\,\mathrm{d}t=f(\omega R-v_C)\,\mathrm{d}t=0,
$$
where $\boldsymbol{v}_{O,C}$ is the velocity of the contact point relative to the center of mass. That is, the friction force does negative work $-fv_C\,\mathrm{d}t$ on the translation of the center of mass, and at the same time its torque does positive work $fR\,\mathrm{d}\theta=fR\omega\,\mathrm{d}t$ on the rotation; the two are equal, so the total work is zero. The role of static friction is to convert part of the translational kinetic energy into rotational kinetic energy.

(2) Conservation of mechanical energy, the center-of-mass theorem and the kinematics of the center of mass give

$$
\frac12mv_C^2+\frac12J\omega^2=mgh,\qquad mg\sin\theta-f=ma_C,\qquad v_C^2=2a_C\frac{h}{\sin\theta},\qquad v_C=\omega R .
$$
Solving,

$$
v_C=\sqrt{\frac{2gh}{1+J/(mR^2)}},\qquad \omega=\frac{v_C}{R},\qquad f=\frac{mg\sin\theta}{1+mR^2/J}.
$$
The friction force can also be found from the center-of-mass theorem, $a_C=R\alpha$, and the law of rotation about the axis through the center of mass, $fR=J\alpha$, or alternatively from the law of rotation about the instantaneous axis, $mgR\sin\theta=J_O\alpha$ (with $J_O=J+mR^2$). The expression for $v_C$ shows that the smaller $J/(mR^2)$ is, the faster the body rolls: released together from the same height, a solid sphere ($\frac25$) reaches the bottom before a solid cylinder ($\frac12$), which reaches it before a thin ring ($1$), independently of mass and radius.

**Example 5.8.4 (The Yo-Yo)** A flat cylinder of mass $m$ and radius $R$ (treated as a uniform disk, $J_C=\frac12mR^2$) has a thin string wound around it, the upper end of the string being held in the hand. (1) With the hand fixed, the cylinder unwinds and descends; find its acceleration and the tension in the string. (2) If the hand pulls upward so that the tension is $T=2mg$, find the upward acceleration of the cylinder and the upward acceleration of the hand.

**Solution** (1) The center-of-mass theorem gives $mg-T=ma_C$, the law of rotation about the axis through the center of mass gives $TR=\frac12mR^2\alpha$, and with no slipping of the string and the hand fixed, $a_C=R\alpha$. Solving, $a_C=\frac23g$ and $T=\frac13mg$.

(2) $T-mg=ma_C$ gives $a_C=g$ (upward); $TR=\frac12mR^2\alpha$ gives $\alpha=4g/R$. The string does not slip on the rim of the cylinder, so the acceleration of the string relative to the center of mass is $a'=R\alpha=4g$ (upward), and the upward acceleration of the hand is $a=a'+a_C=5g$.

## Summary

| Translation (particle) | Rotation about a fixed axis (rigid body) |
|---|---|
| Displacement $\Delta x$, velocity $v$, acceleration $a$ | Angular displacement $\Delta\theta$, angular velocity $\omega$, angular acceleration $\alpha$ |
| Mass $m$ | Moment of inertia $J=\int r_\perp^2\,\mathrm{d}m$ |
| Force $F$, Newton's second law $F=ma$ | Torque $M$, law of rotation $M=J\alpha$ |
| Work $\int F\,\mathrm{d}x$, kinetic energy $\frac12mv^2$ | Work $\int M\,\mathrm{d}\theta$, rotational kinetic energy $\frac12J\omega^2$ |
| Momentum $mv$, impulse $\int F\,\mathrm{d}t$ | Angular momentum $J\omega$, angular impulse $\int M\,\mathrm{d}t$ |
| Conservation of momentum | Conservation of angular momentum about the axis |

Plane motion is the translation of the center of mass (center-of-mass theorem) plus rotation about the axis through the center of mass (law of rotation about that axis), with the kinetic energies adding by König's theorem; the condition for rolling without slipping is $v_C=\omega R$, $a_C=\alpha R$, and static friction does no work.

## Questions

1. How can one measure the moment of inertia of an irregularly shaped object in the laboratory?

   **Answer** the falling-body method of Example 5.4.1; or treat the object as a physical pendulum or torsion pendulum and measure the period of small oscillations ([5.1.6](/5.1.6)), from which $J$ follows.

2. In Example 5.6.2, how should the interaction force between the clay and the disk be handled if the clay and the disk are analyzed as separate free bodies?

   **Answer** after sticking there is an unknown internal force between them; write Newton's equation for the clay and the law of rotation and center-of-mass theorem for the disk separately, and the internal force cancels when they are added, giving the same result as using the center-of-mass theorem for the whole system.
