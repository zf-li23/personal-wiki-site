---
title: Electromagnetic Induction
description: Faraday's law of induction and Lenz's law, flux linkage and induced charge; motional emf and the Lorentz force; the induced electric field, eddy currents, the betatron and the skin effect; mutual inductance, self-inductance and RL circuits; magnetic field energy and energy density; superconductivity and the Meissner effect.
source_hash: 051e359e0ff6
---

After Ørsted discovered that an electric current produces a magnetic field, it was natural to ask about the inverse effect: can a magnetic field produce a current? After nearly a decade of searching, Faraday discovered electromagnetic induction in 1831: a steady magnetic field produces no current, but a changing magnetic flux does. Electromagnetic induction truly ties the electric and magnetic fields together, and it is the principle of generators, transformers, inductors and wireless charging. This chapter first gives Faraday's law and Lenz's law, which determines the direction, and then analyzes two mechanisms of the induced **electromotive force**: when a **conductor** moves in a magnetic field, the **non-electrostatic force** is the **Lorentz force** (motional emf, [5.3.7](/5.3.7)); when the conductor is at rest and the magnetic field changes, the non-electrostatic force comes from the induced electric field that the changing magnetic field excites in space. The latter is the first of Maxwell's equations ([5.3.10](/5.3.10)). Next we discuss induction in a circuit by itself and between circuits (self-inductance and mutual inductance), from which the energy of the magnetic field is derived; RL circuits and LC circuits correspond to first-order and second-order linear differential equations with constant coefficients, respectively ([2.4](/2.4)). Finally we give a brief introduction to superconductivity; Section 9.7 is optional.

## 9.1. Faraday's Law of Induction

### 9.1.1. The Phenomena of Electromagnetic Induction

Faraday's experiments can be grouped into three kinds: when a bar magnet is inserted into or withdrawn from a coil, a current is produced in the coil, and there is no current when the magnet is at rest relative to the coil; when a current-carrying coil replaces the magnet, a current appears in the other coil when the two coils move relative to each other, or when they are at rest relative to each other and the current in one of them is changed; and when a closed circuit is placed in a steady magnetic field, there is a current in the circuit when a conducting rod slides along the rails. Faraday summarized the situations producing an induced current as five: a moving magnet, a moving **steady current**, a changing magnetic field, a changing current, and a conductor moving in a magnetic field. What they have in common is that the **magnetic flux** through a closed circuit changes.

When the magnetic flux through a closed conducting circuit changes, a current is produced in the circuit whatever the cause of the change; this phenomenon is called *electromagnetic induction*. The current in the circuit is called the induced current, and the electromotive force driving it is called the induced emf. The induced emf is more fundamental than the induced current: when the circuit is open there is no induced current, but the induced emf is still present; the induced current is determined by the induced emf and the **electrical resistance** of the circuit, and has the direction of the induced emf.

### 9.1.2. Faraday's Law of Induction

**Theorem 9.1.1 (Faraday's Law of Induction)** The magnitude of the induced emf in a circuit is proportional to the rate of change of the magnetic flux through the circuit:

$$
\mathcal{E}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}.
$$
Here the positive direction of the emf is taken along the sense of traversal of the circuit $L$, and in the magnetic flux $\Phi=\iint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$ the normal of the surface $S$ is related to the sense of traversal of $L$ by the right-hand rule.

In the SI the constant of proportionality is 1: the unit of magnetic flux, the weber, $\mathrm{Wb}=\mathrm{V\,s}$, is defined in just this way. With the convention above, $\mathcal{E}>0$ means that the induced emf is along the sense of traversal of $L$, and $\mathcal{E}<0$ that it is opposite. The minus sign in the formula expresses the direction of the induced emf, whose physical meaning is given by Lenz's law.

### 9.1.3. Lenz's Law

**Theorem 9.1.2 (Lenz's Law)** The direction of the induced current in a closed circuit is always such that the magnetic field it excites opposes the change of the magnetic flux that causes the induced current.

A more general statement of *Lenz's law* (1834) is that the effect of the induced current always opposes the cause of the induced current. When a magnet approaches a coil, the induced current in the coil makes the coil repel the magnet and opposes their approach; when the magnet moves away, the induced current makes the two attract and opposes their separation. It is the manifestation of energy conservation in electromagnetic induction: if the induced current had the opposite direction, then once the magnet started to approach it would be accelerated, and the induced current and the kinetic energy would increase without bound at the same time, which would constitute a **perpetual motion machine of the first kind**.

**Example 9.1.1 (Energy Conversion in a Sliding Rod)** A conducting rod of length $l$ slides at constant speed $v$ along two parallel rails in a uniform magnetic field $B$; the rod is perpendicular to the rails, the field is perpendicular to the plane of the rails, and the resistance of the circuit is $R$. The area of the circuit increases by $lv$ per second, the induced emf has magnitude $\mathcal{E}=Blv$, and the current is $I=Blv/R$. The **Ampère force** on the rod has magnitude $F=IlB=B^2l^2v/R$, directed opposite to the velocity (Lenz's law). To maintain uniform motion an external force must do work, with power

$$
Fv=\frac{B^2l^2v^2}{R}=I^2R,
$$
which is exactly the Joule heating power in the circuit: the mechanical work done by the external force is entirely converted into electrical energy by electromagnetic induction, and then into heat.

### 9.1.4. Flux Linkage and Induced Charge

For $N$ turns of a coil in series, the total emf is the sum of the emfs of the individual turns:

$$
\mathcal{E}=-\sum_i\frac{\mathrm{d}\Phi_i}{\mathrm{d}t}=-\frac{\mathrm{d}\Psi}{\mathrm{d}t},\qquad \Psi=\sum_i\Phi_i,
$$
and $\Psi$ is called the *magnetic flux linkage*, the sum of the fluxes through the individual turns. If the flux through every turn is the same, $\Psi=N\Phi$.

In a circuit of resistance $R$ the induced current is $I=\mathcal{E}/R=-\frac1R\frac{\mathrm{d}\Psi}{\mathrm{d}t}$. The charge passing through a cross section of the circuit from time $t_1$ to $t_2$ is

$$
q=\int_{t_1}^{t_2}I\,\mathrm{d}t=-\frac1R\int_{\Psi_1}^{\Psi_2}\mathrm{d}\Psi=\frac{\Psi_1-\Psi_2}{R},
$$
which depends only on the change of the flux linkage and not on how fast it changes. Measuring the charge that has passed gives the change of the flux linkage; this is the principle of the fluxmeter (ballistic galvanometer), and it is the method used in [5.3.8](/5.3.8) to measure the magnetization curve of a **ferromagnetic substance**.

There are two situations in which an induced emf arises: in one, the circuit or part of it moves in a steady magnetic field; in the other, the circuit is at rest and the magnetic field changes with time (the source moves or the current changes). The emf produced in the former case is called motional emf and in the latter induced emf. By the definition of emf ([5.3.5](/5.3.5)), both require a non-electrostatic force, and the next two sections find them in turn.

## 9.2. Motional Emf

The induced emf produced when a conductor moves in a steady magnetic field is called *motional electromotive force*. Let a circuit $L$ move with velocity $\boldsymbol{v}$ (different parts may have different velocities); in time $\mathrm{d}t$ the line element $\mathrm{d}\boldsymbol{l}$ sweeps out the vector area element $(\boldsymbol{v}\,\mathrm{d}t)\times\mathrm{d}\boldsymbol{l}$. By **Gauss's law for magnetism**, the increment of the flux through the circuit equals the flux through the side surface it sweeps out:

$$
\mathrm{d}\Phi=\oint_L\boldsymbol{B}\cdot\big[(\boldsymbol{v}\,\mathrm{d}t)\times\mathrm{d}\boldsymbol{l}\big],\qquad \mathcal{E}_{\mathrm{mot}}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}=-\oint_L\boldsymbol{B}\cdot(\boldsymbol{v}\times\mathrm{d}\boldsymbol{l})=\oint_L(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l},
$$
where the last step used the cyclic property of the scalar triple product.

**Formula 9.2.1 (Motional Emf)** The motional emf produced when a wire $ab$ moves in a steady magnetic field is

$$
\mathcal{E}_{\mathrm{mot}}=\int_a^b(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l}.
$$
When the integral is positive the emf points from $a$ to $b$ (end $b$ is at the higher **electric potential**); when it is negative it points from $b$ to $a$.

The formula itself identifies the non-electrostatic force: the charge carriers in the conductor move with the conductor at velocity $\boldsymbol{v}$ and experience the Lorentz force $q\boldsymbol{v}\times\boldsymbol{B}$, which is equivalent to a non-electrostatic field $\boldsymbol{E}_{\mathrm{K}}=\boldsymbol{v}\times\boldsymbol{B}$, and the emf is its line integral along the wire. If $\boldsymbol{B}$ and $\boldsymbol{v}$ are both constant vectors, $\mathcal{E}_{\mathrm{mot}}=(\boldsymbol{v}\times\boldsymbol{B})\cdot\overrightarrow{ab}$, independent of the shape of the wire.

**Remark 9.2.1 (The Lorentz Force Does No Work, so Why Can It Produce an Emf)** Suppose that in addition to moving with the wire at $\boldsymbol{v}$, a charge carrier moves along the wire with velocity $\boldsymbol{u}$ (this is the current). The total Lorentz force on it is $\boldsymbol{F}=q(\boldsymbol{v}+\boldsymbol{u})\times\boldsymbol{B}$, perpendicular to the resultant velocity $\boldsymbol{v}+\boldsymbol{u}$, so the total power is zero:

$$
\boldsymbol{F}\cdot(\boldsymbol{v}+\boldsymbol{u})=0\quad\Longrightarrow\quad q(\boldsymbol{v}\times\boldsymbol{B})\cdot\boldsymbol{u}=-q(\boldsymbol{u}\times\boldsymbol{B})\cdot\boldsymbol{v}.
$$
The left side is the power with which the component force $q\boldsymbol{v}\times\boldsymbol{B}$ drives the carrier along the wire, that is, the power with which the emf does work on the current; the right side is the negative work done by the other component force $q\boldsymbol{u}\times\boldsymbol{B}$ (macroscopically, the **Ampère force** on the wire), which must be overcome by an external force. The Lorentz force itself therefore does no work; it is only the "bridge" that converts the mechanical work done by the external force into electrical energy, in agreement with the energy analysis of Example 9.1.1.

**Example 9.2.1 (Emf in a Rotating Metal Rod)** A metal rod $OA$ of length $L$ rotates about end $O$ with angular velocity $\boldsymbol{\omega}$ in a uniform magnetic field $\boldsymbol{B}$ perpendicular to the rod, with $\boldsymbol{\omega}$ parallel to $\boldsymbol{B}$. Find the emf in the rod.

**Solution** At distance $l$ from $O$ the velocity is $v=\omega l$, and $\boldsymbol{v}\times\boldsymbol{B}$ points along the rod from $O$ to $A$ ($\boldsymbol{v}=\boldsymbol{\omega}\times\boldsymbol{l}$, $(\boldsymbol{\omega}\times\boldsymbol{l})\times\boldsymbol{B}=\omega B\,\boldsymbol{l}$), with magnitude $\omega lB$. Hence

$$
\mathcal{E}_{OA}=\int_0^L\omega Bl\,\mathrm{d}l=\frac12B\omega L^2,
$$
the emf points from $O$ to $A$, positive charge accumulates at end $A$, and $A$ is at the higher potential. If $\boldsymbol{\omega}$ is opposite to $\boldsymbol{B}$, then $O$ is at the higher potential. Replacing the rod by a metal disk gives a steady emf $\frac12B\omega R^2$ between the axle and the rim of the disk; this is Faraday's disk generator (homopolar generator).

## 9.3. Induced Emf and the Induced Electric Field

### 9.3.1. The Induced Electric Field

The induced emf produced when the circuit is fixed and the magnetic field changes with time is called *induced electromotive force*. By Faraday's law,

$$
\mathcal{E}_{\mathrm{ind}}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}=-\frac{\mathrm{d}}{\mathrm{d}t}\iint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}.
$$
The conductor is at rest, so the carriers experience no Lorentz force; only an electric field can drive charges at rest, and since its circulation is not zero, it is not an electrostatic field. Experiments also show that the induced emf is independent of the material of the circuit. From this Maxwell proposed that a changing magnetic field excites an electric field in the surrounding space, whether or not there is a conductor there; the conducting circuit merely reveals its existence. This electric field is called the *induced electric field*, denoted $\boldsymbol{E}_{\mathrm{ind}}$.

**Theorem 9.3.1 (Circulation Theorem for the Induced Electric Field)** The circulation of the induced electric field around any closed circuit equals the negative of the rate of change of the magnetic flux through a surface bounded by the circuit:

$$
\oint_L\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{l}=-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S},\qquad\text{differential form}\quad\nabla\times\boldsymbol{E}_{\mathrm{ind}}=-\frac{\partial\boldsymbol{B}}{\partial t},
$$
where the normal of the surface $S$ is related to the circuit $L$ by the right-hand rule. The induced electric field is not produced by charges, and its flux through any closed surface is zero: $\oiint_S\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$.

The differential form follows from **Stokes' theorem**. The **electric field lines** of the induced electric field are closed curves linked with the **magnetic field lines**, so the induced electric field is also called a vortex electric field. A comparison with the electrostatic field:

| | Electrostatic field | Induced electric field |
|---|---|---|
| Source | static charges | changing magnetic field |
| Flux | $\oiint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=q/\varepsilon_0$, has sources | $\oiint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$, **solenoidal vector field** |
| Circulation | $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=0$, **conservative vector field** | $\oint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{l}=-\frac{\mathrm{d}\Phi}{\mathrm{d}t}$, has curl, nonconservative |
| Electric field lines | start on positive charges and end on negative charges | closed curves |
| Electric potential | can be defined | cannot be defined |
| Action on charge | $q\boldsymbol{E}$ | $q\boldsymbol{E}_{\mathrm{ind}}$ |

In general both kinds of electric field are present in space, and the total field $\boldsymbol{E}=\boldsymbol{E}_{\mathrm{s}}+\boldsymbol{E}_{\mathrm{ind}}$ satisfies $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=-\iint\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}$, which is the law of electromagnetic induction in Maxwell's equations.

**Example 9.3.1 (Induced Electric Field Inside and Outside a Long Straight Solenoid)** An infinitely long straight solenoid of radius $R$ has $n$ turns per unit length and carries a current $I=\alpha t$ ($\alpha$ a constant). Find the induced electric field inside and outside the tube.

**Solution** Inside the tube $\boldsymbol{B}=\mu_0nI\boldsymbol{e}_z$, outside $\boldsymbol{B}=\boldsymbol{0}$, so $\frac{\partial\boldsymbol{B}}{\partial t}=\mu_0n\alpha\boldsymbol{e}_z$ ($r<R$) and zero outside. First determine the direction of $\boldsymbol{E}_{\mathrm{ind}}$ from symmetry. By axial symmetry and translational symmetry along the axis, $\boldsymbol{E}_{\mathrm{ind}}=E_r(r)\boldsymbol{e}_r+E_\varphi(r)\boldsymbol{e}_\varphi+E_z(r)\boldsymbol{e}_z$. Any plane perpendicular to the axis is a mirror plane of the system (the current runs around the circumference and is unchanged by reflection), and $\boldsymbol{E}_{\mathrm{ind}}$ is a **polar vector**, which cannot have a component perpendicular to the mirror on the mirror, so $E_z=0$. Take a closed cylindrical surface coaxial with the solenoid; $\oiint\boldsymbol{E}_{\mathrm{ind}}\cdot\mathrm{d}\boldsymbol{S}=0$ gives $E_r\cdot2\pi rl=0$, so $E_r=0$. Hence $\boldsymbol{E}_{\mathrm{ind}}=E_\varphi(r)\boldsymbol{e}_\varphi$.

Take a coaxial circle of radius $r$ as the loop, traversed along $\boldsymbol{e}_\varphi$; the left side is $E_\varphi\cdot2\pi r$, and the right side is

$$
-\iint_S\frac{\partial\boldsymbol{B}}{\partial t}\cdot\mathrm{d}\boldsymbol{S}=\begin{cases}-\mu_0n\alpha\,\pi r^2,&r<R,\\-\mu_0n\alpha\,\pi R^2,&r>R,\end{cases}
\qquad\text{so}\qquad
E_\varphi=\begin{cases}-\dfrac12\mu_0n\alpha\,r,&r<R,\\[2mm]-\dfrac{\mu_0n\alpha R^2}{2r},&r>R.\end{cases}
$$
The minus sign means that the induced electric field circulates opposite to the current (Lenz's law). The **electric field strength** is proportional to $r$ inside the tube and inversely proportional to $r$ outside: although there is no magnetic field outside the solenoid, there is an induced electric field. In terms of a general $\frac{\mathrm{d}B}{\mathrm{d}t}$, $E=\frac r2\frac{\mathrm{d}B}{\mathrm{d}t}$ ($r<R$) and $E=\frac{R^2}{2r}\frac{\mathrm{d}B}{\mathrm{d}t}$ ($r>R$).

![Left: the induced electric field lines when the magnetic field points into the page and increases uniformly; they are circles concentric with the solenoid (the blue region is the cross section of the solenoid); right: the magnitude of the induced electric field versus distance from the axis, proportional to $r$ inside the tube and inversely proportional to $r$ outside](./plots/solenoid-induced-field.py)

### 9.3.2. Eddy Currents

When a bulk conductor is in a changing magnetic field, the induced electric field drives closed induced currents inside the conductor, called *eddy currents*. The resistance of a bulk conductor is small, so eddy currents can be large.

- Heating: in a cylindrical conductor, if the magnetic field varies uniformly along the axis, the induced electric field at radius $r$ is $E\propto r$ and the heating power per unit volume $\sigma E^2\propto r^2$, so the outer layers heat more; together with the skin effect of Section 9.3.4, the heating at the surface is even more concentrated, which suits the surface hardening of metal parts. A high-frequency induction furnace uses eddy currents to melt metal in a crucible without contact with the charge, which is convenient for melting in vacuum. An induction cooktop uses an alternating magnetic field to produce eddy currents in the bottom of the pot to heat it.
- Electromagnetic damping: when a conductor moves in a magnetic field, the Ampère force on the eddy currents opposes the motion (Lenz's law), which is used for damping the pointers of meters and for eddy-current braking of trains.
- Reducing eddy currents: the cores of transformers and motors are built of mutually insulated silicon-steel laminations parallel to the direction of the field, which cut the eddy-current paths perpendicular to the field; and since silicon steel has a rather high **electrical resistivity**, the eddy-current loss is greatly reduced.

### 9.3.3. The Betatron

The *betatron* accelerates electrons with the induced electric field. A toroidal vacuum chamber is placed between the poles of an electromagnet, which carries an alternating current; the changing magnetic field on the one hand produces an induced electric field along the circular orbit that accelerates the electrons, and on the other hand makes the electrons move on a circular orbit of radius $R$. What condition keeps the orbit radius constant? The momentum $p$ of the electron and the field $B_R$ at the orbit satisfy $p=eB_RR$ (valid also in the relativistic case). The induced electric field along the orbit has magnitude $E=\frac{1}{2\pi R}\frac{\mathrm{d}\Phi}{\mathrm{d}t}$, with $\Phi=\pi R^2\bar B$, where $\bar B$ is the average **magnetic flux density** over the area enclosed by the orbit; hence

$$
\frac{\mathrm{d}p}{\mathrm{d}t}=eE=\frac{eR}{2}\frac{\mathrm{d}\bar B}{\mathrm{d}t}=eR\frac{\mathrm{d}B_R}{\mathrm{d}t}\qquad\Longrightarrow\qquad B_R=\frac12\bar B,
$$
that is, the field at the orbit must be half the average field inside the orbit (the "two-to-one condition"), which is achieved by the shape of the pole faces. The electrons are accelerated only during the quarter period in which the alternating field increases, and are extracted at its end. The first betatron was built by Kerst in 1940 with an energy of $2.3\,\mathrm{MeV}$, and the largest model (1950) reached about $300\,\mathrm{MeV}$. Electron accelerators of higher energy use the synchrotron instead: synchrotron radiation was first observed in 1947 at the $70\,\mathrm{MeV}$ electron synchrotron of General Electric ([5.3.10](/5.3.10)).

### 9.3.4. The Skin Effect

A direct current is uniformly distributed over the cross section of a wire, but a high-frequency alternating current concentrates near the surface of the wire, with the **current density** larger the closer to the surface; this is called the *skin effect*. Qualitatively, the alternating current produces an alternating magnetic field inside the wire, and the induced electric field it produces is opposite to the current near the center of the wire and in the same direction as the current near the surface, so that the current at the center is weakened and that at the surface strengthened; the higher the frequency, the stronger the induced field and the more pronounced the effect.

A quantitative treatment requires Maxwell's equations: in a good conductor the **displacement current** is neglected, and eliminating $\boldsymbol{E}$ from $\nabla\times\boldsymbol{H}=\sigma\boldsymbol{E}$ and $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$ gives $\Delta\boldsymbol{B}=\mu\sigma\,\partial\boldsymbol{B}/\partial t$, a diffusion equation of the same type as the heat conduction equation ([2.5.7](/2.5.7)). Solving it near a flat surface for an alternating field of frequency $\omega$, the amplitude of the current density decays exponentially with depth $d$:

$$
J(d)=J_0\,\mathrm{e}^{-d/\delta},\qquad \delta=\sqrt{\frac{2}{\omega\mu\sigma}}=\frac{1}{\sqrt{\pi f\mu\sigma}},
$$
and $\delta$ is called the skin depth. For copper ($\sigma=5.96\times10^7\,\mathrm{S/m}$), $\delta\approx9.2\,\mathrm{mm}$ at $50\,\mathrm{Hz}$, about $66\,\mu\mathrm{m}$ at $1\,\mathrm{MHz}$ and about $2\,\mu\mathrm{m}$ at $1\,\mathrm{GHz}$. High-frequency circuits therefore use stranded wire made of many thin insulated strands, or hollow copper tubes, and microwave components need only be silver-plated on the surface.

### 9.3.5. The Relativity of Motional and Induced Emf

The distinction between motional and induced emf depends on the reference frame. When the magnet is at rest and the coil moves, in the frame of the magnet the charges in the coil experience the Lorentz force $q\boldsymbol{v}\times\boldsymbol{B}$, and the emf is motional; in the frame of the coil the charges are at rest, the motion of the magnet makes the magnetic field in space change, the charges experience the force of the induced electric field, and the emf is induced. The two descriptions give the same emf, which is exactly the result of the transformation of the electric and magnetic fields between reference frames ([5.3.7](/5.3.7#sec-7.2)). Einstein's 1905 paper on special relativity, "On the Electrodynamics of Moving Bodies", opens with precisely this example: Maxwell's theory explains the two cases asymmetrically, whereas the observable phenomenon depends only on the relative motion.

## 9.4. Mutual Inductance

### 9.4.1. The Coefficient of Mutual Inductance

For two neighboring coils 1 and 2, the magnetic field produced by the current $i_1$ in coil 1 passes through coil 2 and forms a flux linkage $\Psi_{21}$ in it. By the **Biot–Savart law** the field is proportional to the current, so $\Psi_{21}$ is proportional to $i_1$:

$$
\Psi_{21}=M_{21}i_1,\qquad \Psi_{12}=M_{12}i_2.
$$
It can be shown (Section 9.6) that $M_{12}=M_{21}=M$, called the coefficient of mutual inductance of the two coils, or the *mutual inductance* for short. It is determined by the sizes, shapes, numbers of turns, relative position of the two coils and the surrounding medium, and as long as there is no ferromagnetic substance near the coils, it is independent of the currents. The SI unit of mutual inductance is the henry, $1\,\mathrm{H}=1\,\mathrm{Wb/A}$.

When $i_1$ changes, a mutual-induction emf is produced in coil 2, and vice versa:

$$
\mathcal{E}_{21}=-M\frac{\mathrm{d}i_1}{\mathrm{d}t},\qquad \mathcal{E}_{12}=-M\frac{\mathrm{d}i_2}{\mathrm{d}t},
$$
where by convention the positive direction of the emf in each coil and the positive direction of the current in the other coil are both related to the positive direction of the flux by the right-hand rule.

In calculating $M$ one may choose whichever side is convenient: assume $i_1$ and find $\Psi_{21}$, or assume $i_2$ and find $\Psi_{12}$; the results are the same.

**Example 9.4.1 (Mutual Inductance of Coaxial Long Solenoids)** On a long straight solenoid 1 of length $l$ and cross-sectional area $S$, another coil 2 of the same length is wound tightly, with $n_1$ and $n_2$ turns per unit length, respectively. Let coil 1 carry current $i_1$; inside the tube $B_1=\mu_0n_1i_1$, the flux through each turn of coil 2 is $B_1S$, and $\Psi_{21}=n_2l\cdot\mu_0n_1i_1S$, so

$$
M=\mu_0n_1n_2lS=\mu_0n_1n_2V.
$$
The self-inductances of the two coils (Section 9.5) are $L_1=\mu_0n_1^2V$ and $L_2=\mu_0n_2^2V$, so $M=\sqrt{L_1L_2}$. In general $M=k\sqrt{L_1L_2}$, where $0\le k\le1$ is called the coupling coefficient, and $k=1$ means that all the flux of one coil passes through the other coil (no leakage flux).

Transformers, instrument transformers and wireless charging all use mutual inductance: in an ideal transformer the two coils are wound on the same closed iron core, the flux per turn is the same, and the ratio of the voltages on the two sides equals the ratio of the numbers of turns.

## 9.5. Self-Inductance

### 9.5.1. The Coefficient of Self-Inductance

When the current in a circuit changes, the flux linkage of the magnetic field it produces through the circuit itself also changes, and an induced emf is produced in the circuit; this is called self-induction, and the corresponding emf the self-induced emf. If the shape and size of the coil do not change and there is no ferromagnetic substance nearby, the flux linkage is proportional to the current:

$$
\Psi=Li,\qquad \mathcal{E}_L=-L\frac{\mathrm{d}i}{\mathrm{d}t},
$$
and $L$ is called the coefficient of self-induction of the circuit, or the *self-inductance* or inductance for short; its unit is also the henry. Here the positive direction of the flux linkage is related to that of the current by the right-hand rule, which ensures $L>0$; the positive direction of $\mathcal{E}_L$ is taken along that of the current. The minus sign means that the self-induced emf always opposes the change of the current in the circuit itself.

**Example 9.5.1 (Self-Inductance of a Long Straight Solenoid)** A long straight solenoid of length $l$, cross-sectional area $S$ and $n$ turns per unit length is filled with a linear medium of **permeability** $\mu$. Then $B=\mu ni$, $\Psi=nl\cdot BS=\mu n^2lSi$, so

$$
L=\mu n^2V,\qquad V=lS.
$$
The self-inductance is proportional to the volume of the tube and to the square of the turn density; inserting an iron core can increase the self-inductance a thousandfold.

### 9.5.2. RL Circuits

Since $\mathcal{E}_L=-L\,\mathrm{d}i/\mathrm{d}t$, if the current changed abruptly the self-induced emf would be infinite, so the current in an inductor cannot change abruptly (compare: the voltage across a **capacitor** cannot change abruptly). For alternating current, the higher the frequency, the faster the current changes and the larger the self-induced emf, so an inductor "passes direct current and blocks alternating current", while a capacitor "passes alternating current and blocks direct current".

**Example 9.5.2 (Transient in an RL Circuit)** A **source of electromotive force** with emf $\mathcal{E}$ (internal resistance neglected), a resistance $R$ and a self-inductance $L$ are connected in series, and the switch is closed at $t=0$. By **Kirchhoff's voltage law**,

$$
\mathcal{E}-L\frac{\mathrm{d}i}{\mathrm{d}t}=Ri.
$$
This is a first-order **linear differential equation** with constant coefficients ([2.4.3](/2.4.3#sec-3.2)); with the initial condition $i(0)=0$ the solution is

$$
i=\frac{\mathcal{E}}{R}\big(1-\mathrm{e}^{-t/\tau}\big),\qquad\tau=\frac LR.
$$
The current grows gradually from zero to the steady value $\mathcal{E}/R$, and $\tau$ is called the **time constant** of the RL circuit: after a time $\tau$ the current reaches $1-\mathrm{e}^{-1}\approx63\%$ of its steady value, and after $5\tau$ more than 99%. Once the current is steady, if $L$ and $R$ are connected into a loop at the moment the source is removed, then from $L\frac{\mathrm{d}i}{\mathrm{d}t}+Ri=0$ the current decays as $i=\frac{\mathcal{E}}{R}\mathrm{e}^{-t/\tau}$ and does not disappear at once.

![Left: the growth of the current in an RL circuit after the source is connected and its decay after the source is removed, with time in units of $\tau=L/R$; right: the charge on the capacitor in a series RLC circuit with initial charge $q_0$; the three curves correspond to underdamping, critical damping and overdamping](./plots/rl-rlc-circuits.py)

A common demonstration: a bulb $D_1$ is connected in parallel with an inductor $L$ (with a very small DC resistance) across a source, and in the steady state the current $I_L$ in the coil is greater than the current $I_R$ in the bulb. At the instant the source is disconnected the current in the coil cannot change abruptly and can only flow through the bulb, so the current in the bulb suddenly increases from $I_R$ to $I_L$ and then decays gradually; the bulb therefore flashes brightly before going out. The energy of the flash comes from the magnetic field energy stored in the coil (Section 9.6).

**Remark 9.5.1 (LC Oscillating Circuit)** Connect a capacitor $C$ charged to $q_0$ with an inductor $L$ into a loop; from $L\frac{\mathrm{d}i}{\mathrm{d}t}+\frac qC=0$ and $i=\frac{\mathrm{d}q}{\mathrm{d}t}$,

$$
\frac{\mathrm{d}^2q}{\mathrm{d}t^2}+\frac{1}{LC}q=0,
$$
exactly the same as the equation of a mass on a spring: the charge undergoes **simple harmonic motion** with **angular frequency** $\omega_0=1/\sqrt{LC}$, and electric field energy and magnetic field energy convert into each other periodically, corresponding to the potential and kinetic energy of the oscillator ([5.1.6](/5.1.6)). With a resistance $R$ in series in the loop, the equation becomes $L\ddot q+R\dot q+q/C=0$, a second-order linear equation with constant coefficients ([2.4.9](/2.4.9#sec-9.4)), and $R$ acts as damping: for $R<2\sqrt{L/C}$ the motion is **damped oscillation**, for $R=2\sqrt{L/C}$ it is critically damped, and for $R>2\sqrt{L/C}$ overdamped; the **quality factor** is $Q=\frac1R\sqrt{L/C}$. Adding an alternating source gives **forced oscillation**, and series resonance is exactly the principle of tuning a radio. The LC circuit is the basic circuit for producing electromagnetic oscillations, and "opening it up" turns it into an antenna that emits electromagnetic waves ([5.3.10](/5.3.10)).

## 9.6. Energy of the Magnetic Field

### 9.6.1. Self-Inductance Energy

In the demonstration above, that the bulb can still flash after the source is disconnected shows that energy is stored in the current-carrying coil. While the current rises from $0$ to $I$ after the source is connected, the source must do work against the self-induced emf, doing work $-\mathcal{E}_Li\,\mathrm{d}t=Li\,\mathrm{d}i$ in time $\mathrm{d}t$, and the total work is

$$
W_{\mathrm{m}}=\int_0^ILi\,\mathrm{d}i=\frac12LI^2.
$$
This work is converted into the magnetic energy of the coil and is released completely through the self-induced emf when the current vanishes. It corresponds to the electric energy $\frac12CU^2$ of a capacitor.

### 9.6.2. Energy Density of the Magnetic Field

For a long straight solenoid, $B=\mu nI$ and $L=\mu n^2V$, so

$$
W_{\mathrm{m}}=\frac12\mu n^2VI^2=\frac{B^2}{2\mu}V.
$$
The magnetic field is uniformly distributed within the volume $V$, and the energy should also be uniformly distributed in the space occupied by the field. This suggests regarding the energy as stored in the magnetic field.

**Formula 9.6.1 (Energy Density of the Magnetic Field)** In a linear **magnetic material** (not a ferromagnetic substance), the energy density of the magnetic field is

$$
w_{\mathrm{m}}=\frac{B^2}{2\mu}=\frac12BH=\frac12\boldsymbol{B}\cdot\boldsymbol{H},
$$
and the magnetic field energy in a volume $V$ is $W_{\mathrm{m}}=\iiint_V\frac12\boldsymbol{B}\cdot\boldsymbol{H}\,\mathrm{d}V$.

This result holds for general linear media and nonuniform magnetic fields, and corresponds to the **energy density of the electric field** $\frac12\boldsymbol{E}\cdot\boldsymbol{D}$ ([5.3.4](/5.3.4)). For a ferromagnetic substance, the work done by the surroundings per unit volume as $H$ increases from $0$ is $\int H\,\mathrm{d}B$, which depends on the process; this is the hysteresis loss of [5.3.8](/5.3.8). From the point of view of energy, the current in an inductor cannot change abruptly because the magnetic field energy cannot change abruptly, as otherwise the power would be infinite. Conversely, every current system has a definite magnetic field energy, and the self-inductance can also be calculated from the energy:

$$
L=\frac{2W_{\mathrm{m}}}{I^2}.
$$

**Example 9.6.1 (Self-Inductance of a Coaxial Cable)** A coaxial cable consists of a solid cylindrical conductor of radius $R_1$ and a thin cylindrical shell of radius $R_2$; a current $I$ flows uniformly along the inner conductor and returns along the outer shell, and the medium and conductors have $\mu_{\mathrm{r}}=1$. Find the self-inductance per unit length.

**Solution** By **Ampère's circuital law**, inside the inner conductor ($r<R_1$) $H=\frac{Ir}{2\pi R_1^2}$, between the two conductors $H=\frac{I}{2\pi r}$, and outside the shell $H=0$. The magnetic field energy per unit length is

$$
\frac{W_{\mathrm{m}}}{l}=\int_0^{R_1}\frac{\mu_0}{2}\Big(\frac{Ir}{2\pi R_1^2}\Big)^2 2\pi r\,\mathrm{d}r+\int_{R_1}^{R_2}\frac{\mu_0}{2}\Big(\frac{I}{2\pi r}\Big)^2 2\pi r\,\mathrm{d}r=\frac{\mu_0I^2}{16\pi}+\frac{\mu_0I^2}{4\pi}\ln\frac{R_2}{R_1},
$$
so the self-inductance per unit length is

$$
\frac Ll=\frac{\mu_0}{8\pi}+\frac{\mu_0}{2\pi}\ln\frac{R_2}{R_1}.
$$
The first term comes from the field inside the inner conductor. At high frequencies the current concentrates on the surface of the inner conductor (skin effect), and this term disappears.

### 9.6.3. Mutual Inductance Energy

When two coils carry currents $I_1$ and $I_2$, the total energy of the magnetic field is

$$
W_{\mathrm{m}}=\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2.
$$
Derivation: first raise the current in coil 1 from $0$ to $I_1$ (no current in coil 2), the source doing work $\frac12L_1I_1^2$; then keep $I_1$ fixed and raise the current in coil 2 from $0$ to $I_2$, the source of coil 2 doing work $\frac12L_2I_2^2$; at the same time the change of the current in coil 2 produces a mutual-induction emf in coil 1, and to keep $I_1$ constant the source of coil 1 must do work against it, $\int I_1M_{12}\,\mathrm{d}i_2=M_{12}I_1I_2$. If the order in which the two coils are energized is exchanged, the cross term $M_{21}I_1I_2$ is obtained in the same way. The final state of the field is the same, and the energy is independent of the process, so $M_{12}=M_{21}$, which proves the symmetry of mutual inductance stated in Section 9.4. The cross term $MI_1I_2$ is called the mutual inductance energy and may be positive or negative; from $W_{\mathrm{m}}\ge0$ for all $I_1,I_2$ one also obtains $M^2\le L_1L_2$, that is, $k\le1$.

## 9.7. Introduction to Superconductivity

### 9.7.1. The Discovery of Superconductivity

In 1908 Kamerlingh Onnes first liquefied helium at Leiden and reached a low temperature of $4.2\,\mathrm{K}$. In 1911 he found that the electrical resistance of mercury suddenly vanishes when it is cooled to about $4.2\,\mathrm{K}$. The phenomenon in which the electrical resistance of a substance vanishes completely at low temperature is called *superconductivity*, a conductor in this state is called a superconductor, and the temperature at which the resistance vanishes is called the superconducting **critical temperature** $T_{\mathrm{c}}$. Onnes received the 1913 Nobel Prize in Physics for his research in low-temperature physics.

### 9.7.2. Two Basic Properties of Superconductors

- Zero resistance: in a superconductor $R=0$; when there is a current the voltage across it is zero, and inside it $\boldsymbol{E}=\boldsymbol{0}$ always. A current excited in a superconducting ring can flow on without decay (persistent current); experiments observed no decrease over several years, from which one infers that its resistivity is more than 15 orders of magnitude smaller than that of copper at room temperature (about $1.7\times10^{-8}\,\Omega\,\mathrm{m}$).
- Perfect diamagnetism: in 1933 Meissner and Ochsenfeld discovered that when a superconductor is in the superconducting state, the magnetic flux density inside it is always zero, and a magnetic field originally inside is expelled when it becomes superconducting; this is called the *Meissner effect*. The field is expelled by the superconducting current in a thin layer at the surface of the superconductor (of order $0.1\,\mu\mathrm{m}$, called the penetration depth), whose field inside the body exactly cancels the external field. Equivalent to an ideal **diamagnet** with $\chi_{\mathrm{m}}=-1$, a superconductor can levitate stably above a magnet.

These two properties are independent of each other, and to decide experimentally whether a material is a superconductor, both are required. A conductor with only zero resistance is called a perfect conductor: from $\boldsymbol{E}=\boldsymbol{0}$ and $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$, the magnetic field inside a perfect conductor cannot change but need not be zero, and its state depends on its history (cooling first and then applying a field leaves no field inside; applying a field first and then cooling "freezes" the field inside). A superconductor has no field inside whatever the order, so the superconducting state is a thermodynamic state uniquely determined by temperature and magnetic field.

### 9.7.3. Critical Parameters

The superconducting state exists only under certain conditions:

1. Critical temperature $T_{\mathrm{c}}$: for $T<T_{\mathrm{c}}$ the resistance is zero.
2. Critical magnetic field $B_{\mathrm{c}}$: the superconducting state is destroyed when the external field exceeds $B_{\mathrm{c}}$. Empirically $B_{\mathrm{c}}(T)\approx B_{\mathrm{c}}(0)\big[1-(T/T_{\mathrm{c}})^2\big]$.
3. Critical current density $J_{\mathrm{c}}$: the magnetic field of the current can also destroy superconductivity, so the current density in a superconductor cannot exceed $J_{\mathrm{c}}$, which also decreases with rising temperature. The $J_{\mathrm{c}}$ of practical superconducting films can reach $10^{10}\,\mathrm{A/m^2}$.

The description above is of type I superconductors (most pure metals). Type II superconductors (most alloys and compounds) are in a mixed state between two critical fields: the magnetic field penetrates the body in quantized flux lines (each carrying a flux quantum $h/(2e)$) while the rest remains superconducting, so they can keep zero resistance in very strong fields. The superconducting magnets of hospital magnetic resonance imagers and of the Large Hadron Collider use type II superconductors (niobium–titanium and niobium–tin alloys).

### 9.7.4. A Brief History and the Present State

| Year | Event |
|---|---|
| 1911 | Onnes discovers superconductivity in mercury (Nobel Prize 1913) |
| 1933 | Meissner effect |
| 1957 | Microscopic theory of Bardeen, Cooper and Schrieffer (BCS theory): electrons form Cooper pairs through their interaction with lattice vibrations (Nobel Prize 1972) |
| 1962 | Josephson predicts superconducting tunneling (the Josephson effect); Nobel Prize 1973, shared with Esaki and Giaever |
| 1986 | Bednorz and Müller discover copper-oxide high-temperature superconductors (about $35\,\mathrm{K}$; Nobel Prize 1987) |
| 1987 | Yttrium barium copper oxide ($T_{\mathrm{c}}\approx92\,\mathrm{K}$; found independently by Paul Chu and Maw-Kuen Wu, and by Zhongxian Zhao and colleagues), the first above the liquid-nitrogen temperature of $77\,\mathrm{K}$ |
| 1993–1994 | Mercury-based copper oxides, $T_{\mathrm{c}}\approx133$–$138\,\mathrm{K}$ at ambient pressure and about $164\,\mathrm{K}$ under pressure, still the ambient-pressure record |
| 2001, 2008 | Magnesium diboride ($39\,\mathrm{K}$) and iron-based superconductors (Hideo Hosono et al.; bulk maximum about $55\,\mathrm{K}$) |
| 2003 | Nobel Prize to Abrikosov, Ginzburg and Leggett for the theory of superconductors and superfluids |
| 2015–2019 | Hydrides under high pressure: hydrogen sulfide about $203\,\mathrm{K}$ (about $150\,\mathrm{GPa}$), lanthanum decahydride about $250\,\mathrm{K}$ (about $170\,\mathrm{GPa}$) |
| 2023 | The nickel oxide $\ce{La3Ni2O7}$ at about $80\,\mathrm{K}$ under about $14\,\mathrm{GPa}$ |

Room-temperature superconductivity at ambient pressure has not yet been achieved, and several reports claiming to have found it could not be reproduced. The mechanism of high-temperature superconductors such as the copper oxides also remains an open problem in condensed-matter physics. Applications of superconductivity include strong magnets (magnetic resonance imaging, accelerators, fusion devices), superconducting maglev trains, superconducting power transmission and fault-current limiters, as well as superconducting quantum interference devices (SQUIDs, which can measure fields of order $10^{-15}\,\mathrm{T}$) based on the Josephson effect, and superconducting qubits.

## Summary

- Faraday's law $\mathcal{E}=-\mathrm{d}\Psi/\mathrm{d}t$; Lenz's law determines the direction and is required by energy conservation.
- Motional emf $\int(\boldsymbol{v}\times\boldsymbol{B})\cdot\mathrm{d}\boldsymbol{l}$, the non-electrostatic force being the Lorentz force; induced emf comes from the induced electric field, $\nabla\times\boldsymbol{E}=-\partial\boldsymbol{B}/\partial t$, which is a solenoidal vortex field. The distinction between the two depends on the reference frame.
- Mutual inductance $\Psi_{21}=Mi_1$, $M_{12}=M_{21}$; self-inductance $\Psi=Li$, and $L=\mu n^2V$ for a long straight solenoid. The **time constant** of an RL circuit is $L/R$ and the angular frequency of an LC circuit is $1/\sqrt{LC}$.
- Magnetic energy $\frac12LI^2$, energy density $\frac12\boldsymbol{B}\cdot\boldsymbol{H}$; the total magnetic energy of two coils is $\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2$.
- Superconductors: zero resistance and perfect diamagnetism (the Meissner effect), limited by the critical temperature, critical magnetic field and critical current density.

## Questions

1. What is the working principle of an induction cooktop? Why is an ordinary aluminum pot unsuitable for it?

   **Answer** The high-frequency alternating current in the coil produces eddy currents in the bottom of the pot, which heat it. Iron is a ferromagnetic substance with a small skin depth, so the eddy currents concentrate in a very thin surface layer, the equivalent resistance is large, and the heating is efficient; aluminum has a low resistivity and is not ferromagnetic, so the skin depth is large, the equivalent resistance is small, and for the same induced current less heat is produced (some newer cooktops use higher frequencies to heat aluminum pots).

2. Why is the core of a transformer made of thin sheets coated with insulating varnish and separated from one another? How should the sheets be arranged?

   **Answer** To reduce eddy-current loss. The sheets are placed parallel to the direction of the field, and the paths of the eddy currents (closed loops in planes perpendicular to the field) are cut by the insulating layers.

3. The rates of change of the magnetic flux through an iron ring and an aluminum ring of the same size are equal. Are the induced emfs, induced currents and induced electric fields in the two rings the same?

   **Answer** The induced electric field is determined by the change of the magnetic field and is independent of the material of the ring, so the induced emfs are equal; the resistances differ, so the induced currents differ (neglecting the magnetic field of the induced currents themselves).

4. The centers of three small coils lie on a straight line, close to one another. How should they be placed so that the mutual inductance between every pair is zero?

   **Answer** Make the axes of the three coils mutually perpendicular, with the axis of one coil along the line joining the centers. Small coils can be regarded as **magnetic dipoles**; the field of the coil whose axis lies along the line is parallel to the line at the other two coils and does not pass through them; the axes of the other two coils are both perpendicular to the line, and the field of each at the other is parallel to its own axis and perpendicular to the axis of the other.

5. How do a perfect conductor and a superconductor differ when cooled in a magnetic field?

   **Answer** See Section 9.7.2. If the field is applied first and the sample is then cooled, a perfect conductor freezes the field inside the body, while a superconductor expels it.
