---
title: Magnetic Forces
description: Cyclotron and helical motion of charged particles in magnetic fields and magnetic confinement, the relativity of electric and magnetic fields, the Hall effect and the quantum Hall effect, the Ampère force on a current-carrying wire and the definition of the ampere, the magnetic moment of a current loop and the torque and potential energy in a magnetic field.
source_hash: 6b26dfc7ac6a
---

The previous chapter ([5.3.6](/5.3.6)) discussed how a magnetic field is produced by currents; this chapter discusses how a magnetic field acts on moving charges and currents. There is only one basic law: a charge $q$ with velocity $\boldsymbol{v}$ experiences the **Lorentz force** $q\boldsymbol{v}\times\boldsymbol{B}$. Starting from it, this chapter discusses in turn the motion of a single charged particle (cyclotrons, mass spectrometers, magnetic confinement), two macroscopic manifestations of the force on the many charge carriers in a **conductor** (the Hall effect and the Ampère force on a current-carrying wire), and the torque on a current-carrying coil. A section in the middle uses special relativity ([5.1.8](/5.1.8)) to show that the magnetic and electric forces are manifestations of one interaction in different reference frames. The magnetic moment introduced here is the starting point for understanding the magnetism of matter in the next chapter ([5.3.8](/5.3.8)); the calculation of torque and energy runs completely parallel to that of an **electric dipole** in an electric field ([5.3.2](/5.3.2)).

## 7.1. Motion of Charged Particles in a Magnetic Field

A **point charge** $q$ moving with velocity $\boldsymbol{v}$ in a magnetic field $\boldsymbol{B}$ experiences the force

$$
\boldsymbol{F}=q\boldsymbol{v}\times\boldsymbol{B}.
$$
The magnetic force is always perpendicular to the velocity, so it does no work: it changes the direction of the velocity but not the speed or the kinetic energy. This section considers particles acted on only by the magnetic force in uniform (and slowly varying) magnetic fields.

### 7.1.1. Cyclotron Motion

Let a particle enter a uniform magnetic field with velocity $\boldsymbol{v}\perp\boldsymbol{B}$. The magnitude $qvB$ of the magnetic force is constant and its direction is perpendicular to the velocity, so it supplies the centripetal force for circular motion, $qvB=mv^2/R$; the particle therefore moves uniformly on a circle in the plane perpendicular to $\boldsymbol{B}$,

$$
R=\frac{mv}{qB}=\frac{p}{qB},\qquad T=\frac{2\pi R}{v}=\frac{2\pi m}{qB},\qquad \omega_{\mathrm{c}}=\frac{qB}{m}.
$$
$\omega_{\mathrm{c}}$ is called the *cyclotron frequency*. The essential point is that the period is independent of the speed and the radius: fast particles travel on large circles and slow particles on small circles, but one revolution takes the same time. Viewed along the direction of $\boldsymbol{B}$, a positive charge circles clockwise and a negative charge counterclockwise.

For fast particles the radius formula $R=p/(qB)$ still holds, but $p$ must be the **relativistic momentum** $p=\gamma mv$ ([5.1.8](/5.1.8#sec-8.7)); the cyclotron frequency becomes $\omega=qB/(\gamma m)$ and decreases as the energy increases. A practical formula often used in high-energy physics is $pc\,[\mathrm{GeV}]\approx0.3\,B\,[\mathrm{T}]\,R\,[\mathrm{m}]$ ($q=e$): measuring the radius of curvature of a track gives the momentum of the particle.

### 7.1.2. Cyclotrons and Mass Spectrometers

The *cyclotron* (Lawrence, 1932) exploits the fact that the period of revolution is independent of speed. Two hollow D-shaped metal boxes are placed in a uniform magnetic field, and an alternating voltage whose frequency equals the cyclotron frequency is applied across the gap between them. Inside the boxes (no electric field) the particle moves on semicircles, and each time it crosses the gap the voltage has just reversed, so the particle is accelerated once every half revolution; as its speed grows the radius grows, but the time per half revolution stays the same, so the acceleration continues in synchrony. The radius $R$ of the D-boxes determines the final speed and kinetic energy:

$$
v_{\max}=\frac{qBR}{m},\qquad E_{\mathrm{k}}=\frac{q^2B^2R^2}{2m}.
$$

**Example 7.1.1 (Energy Limit of a Cyclotron)** Take $B=1\,\mathrm{T}$ and $R=1\,\mathrm{m}$. For a proton, $p=eBR$ and $pc=e\,B\,R\,c\approx300\,\mathrm{MeV}$; the energy–momentum relation ([5.1.8](/5.1.8#sec-8.9.3)) gives the kinetic energy $E_{\mathrm{k}}=\sqrt{(pc)^2+(m_{\mathrm{p}}c^2)^2}-m_{\mathrm{p}}c^2\approx47\,\mathrm{MeV}$ ($48\,\mathrm{MeV}$ by the nonrelativistic formula), and $v\approx0.3c$. Here $\gamma\approx1.05$, the cyclotron frequency is already about 5% lower than at low speed, and the particle gradually falls behind the phase of the accelerating voltage. A classical fixed-frequency cyclotron can therefore accelerate protons only to about $20\,\mathrm{MeV}$; higher energies require lowering the voltage frequency as the energy rises (the synchrocyclotron), making $B$ increase with radius (the isochronous cyclotron), or letting the particles move on a circular orbit of fixed radius while $B$ is increased in synchrony (the synchrotron).

The *mass spectrometer* distinguishes masses by magnetic deflection. The ions first pass through a velocity selector in which the electric field $\boldsymbol{E}$ and the magnetic field $\boldsymbol{B}$ are perpendicular to each other; only ions for which the electric and magnetic forces balance ($qE=qvB$) pass straight through, all with speed $v=E/B$. After entering another magnetic field $B'$ they move on semicircles of radius $R=mv/(qB')\propto m/q$. Isotopes of the same charge land at different positions on the plate, so one can measure the masses and abundances of isotopes or separate them.

### 7.1.3. Helical Motion and Magnetic Focusing

If the velocity makes an angle $\theta$ with the uniform magnetic field, resolve it into a component parallel to $\boldsymbol{B}$, $v_\parallel=v\cos\theta$, and a perpendicular component $v_\perp=v\sin\theta$. The magnetic force depends only on $v_\perp$, so the particle circles in the perpendicular plane with radius $R=mv_\perp/(qB)$ and period $T=2\pi m/(qB)$ while moving uniformly along the field; the trajectory is a helix with pitch

$$
h=v_\parallel T=\frac{2\pi mv\cos\theta}{qB}.
$$
For a beam of particles of equal speed emitted from one point at small angles $\theta$ to $\boldsymbol{B}$, $\cos\theta\approx1$ and all particles have approximately the same pitch; although they advance along different helices, after one period they converge again at one point. This is *magnetic focusing*, on which the magnetic lenses in electron microscopes are based (they use the nonuniform field of a short coil).

### 7.1.4. Magnetic Confinement

A particle spirals along a **magnetic field line**, and its cyclotron radius $R=mv_\perp/(qB)$ decreases as $B$ increases: in a strong field (of order $1\,\mathrm{T}$) a charged particle is "tied" to a very thin bundle of field lines and cannot move freely across them; this is transverse confinement. Longitudinal confinement relies on a nonuniform field. In a region where the field increases from weak to strong, the field lines converge toward the axis and $\boldsymbol{B}$ has a radial component pointing toward the axis; its **cross product** with the cyclotron velocity gives an axial force pointing toward the weak-field region, which decelerates the longitudinal motion of the particle and may even reflect it. Such a strong-field region is called a *magnetic mirror*; a configuration with a mirror at each end is called a magnetic bottle and can confine particles to move back and forth between the two mirrors. Using this method to confine high-temperature plasma is called *magnetic confinement*, and it is one of the basic ideas of research on controlled thermonuclear fusion (the tokamak achieves confinement with a toroidal field configuration).

**Remark 7.1.1 (Reflection Condition of a Magnetic Mirror)** When the field varies slowly along the particle's orbit (changing little within one cyclotron period), the magnetic moment of the cyclotron motion (the magnetic moment defined in [§7.5](#sec-7.5), applied to the cyclotron orbit), $\frac{mv_\perp^2}{2B}$, is approximately conserved, and is called an adiabatic invariant; moreover, since the magnetic force does no work, $v_\perp^2+v_\parallel^2=v^2$ is constant. For a particle whose velocity makes the angle $\theta_0$ with the field where the field is $B_0$, at a place with larger $B$ we have $\sin^2\theta=\sin^2\theta_0\cdot B/B_0$, and when $B=B_0/\sin^2\theta_0$, $v_\parallel=0$ and the particle is reflected there. If the strongest field in the bottle is $B_{\max}$, particles with $\sin^2\theta_0<B_0/B_{\max}$ (those whose velocity is almost along the field lines) are not reflected and escape, so a magnetic mirror always leaks to some extent.

![Left: helical motion of a charged particle in a uniform magnetic field, with constant pitch; right: numerically computed motion of a particle in a magnetic bottle (gray lines are field lines, pitch angle 50° at the center): the particle is reflected where the field is stronger near the two ends, and the cyclotron radius decreases as the field strengthens](./plots/charged-particle-trajectories.py)

The Earth's magnetic field is a natural magnetic bottle: the field increases from above the equator toward the poles and can trap protons and electrons from cosmic rays and the solar wind, forming the van Allen radiation belts around the Earth (discovered by satellites in 1958; the inner belt consists mainly of high-energy protons and the outer belt mainly of high-energy electrons). Near the geomagnetic poles the field lines are almost perpendicular to the ground, and charged particles can precipitate along them into the upper atmosphere, where they collide with oxygen atoms and nitrogen molecules and excite them to emit light; this is the aurora (the green line of atomic oxygen at $557.7\,\mathrm{nm}$ is the most common).

## 7.2. The Relativity and Unity of Electric and Magnetic Fields

When both electric and magnetic fields are present, the force on a moving charge is the sum of the electric force and the magnetic force:

**Formula 7.2.1 (Lorentz Force Law)**

$$
\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}.
$$

The magnetic force depends on the velocity of the charge, and the velocity depends on the reference frame. In a frame in which the charge is instantaneously at rest, the magnetic force vanishes; but physical results (for example, whether the charge hits a screen at some place) cannot depend on the choice of reference frame. This means that the electric and magnetic fields themselves must also transform from frame to frame. A simple example shows this.

**Example 7.2.1 (Electric and Magnetic Fields of a Moving Charged Plane)** An infinite uniformly charged plane (the $xz$ plane) and a point charge $q$ above it ($y>0$) move together with velocity $u$ in the $x$ direction. In the comoving frame S′ the plane is at rest; let its surface **charge density** be $\sigma$; then there is only the electrostatic field $E'_y=\frac{\sigma}{2\varepsilon_0}$, and the force on $q$ is $F'_y=qE'_y=\frac{q\sigma}{2\varepsilon_0}$.

In frame S, electric charge is a relativistic invariant ([5.3.1](/5.3.1)), and the plane undergoes **length contraction** along the $x$ direction, so its surface charge density becomes $\gamma\sigma$ ($\gamma$ is the **Lorentz factor**); at the same time the moving charges constitute a surface current, with surface **current density** $\gamma\sigma u$. In S there is therefore both an electric field and a magnetic field (the field of an infinite plane current is $\mu_0K/2$, [5.3.6](/5.3.6)):

$$
E_y=\frac{\gamma\sigma}{2\varepsilon_0},\qquad B_z=\frac{\mu_0}{2}\gamma\sigma u=\frac{uE_y}{c^2},\qquad\text{that is}\quad\boldsymbol{B}=\frac{\boldsymbol{u}\times\boldsymbol{E}}{c^2},
$$
where $\varepsilon_0\mu_0=1/c^2$ was used. The force on $q$ in S is

$$
F_y=q(E_y-uB_z)=\frac{q\gamma\sigma}{2\varepsilon_0}\Big(1-\frac{u^2}{c^2}\Big)=\frac{q\sigma}{2\varepsilon_0\gamma}=\frac{F'_y}{\gamma}.
$$
This is exactly what the relativistic transformation of force ([5.1.8](/5.1.8#sec-8.11)) requires: for the force measured in the rest frame of the particle, in a frame in which the particle moves with velocity $u$, the component along the motion is unchanged and the perpendicular component becomes $1/\gamma$ of its original value. Conversely, if in S one considered only the electric force $qE_y$, one would obtain $\gamma F'_y$, contradicting the transformation of force: the magnetic force is exactly what is needed to ensure that the **principle of relativity** holds.

In general, let frame S′ move with velocity $v$ in the $x$ direction relative to S; the **Lorentz transformation** and the transformation of force yield the transformation of the electromagnetic field:

$$
\begin{aligned}
E'_x&=E_x, & E'_y&=\gamma(E_y-vB_z), & E'_z&=\gamma(E_z+vB_y),\\
B'_x&=B_x, & B'_y&=\gamma\Big(B_y+\frac{v}{c^2}E_z\Big), & B'_z&=\gamma\Big(B_z-\frac{v}{c^2}E_y\Big).
\end{aligned}
$$
The components along the motion are unchanged, and the perpendicular components mix with each other. A purely electric field in one **inertial frame** is observed to have both electric and magnetic fields in another, and vice versa; the electric and magnetic fields are different aspects of one electromagnetic field, and how it is divided between them depends on the reference frame. $\boldsymbol{E}\cdot\boldsymbol{B}$ and $E^2-c^2B^2$ are invariant under the transformation, so if in some inertial frame there is only an electric field ($\boldsymbol{B}=\boldsymbol{0}$), then $E>cB$ in every inertial frame.

**Remark 7.2.1 (Why the Magnetic Force Is Usually Much Smaller Than the Electric Force)** For two point charges moving in parallel with the same speed $v$, one finds that the ratio of the magnetic force to the electric force between them is $F_{\mathrm{m}}/F_{\mathrm{e}}=v^2/c^2$. The drift speed of electrons in a wire is only of order $10^{-4}\,\mathrm{m/s}$, so $v^2/c^2\sim10^{-25}$, yet the magnetic force between current-carrying wires is easily observed. The reason is that wires are electrically neutral: the electric forces of the positive and negative charges cancel exactly, and only this "relativistic correction" remains. In this sense magnetic phenomena are a necessary consequence of the **law of conservation of charge**, the invariance of charge, and special relativity (Purcell's textbook on electromagnetism develops the subject in this way).

## 7.3. The Hall Effect

### 7.3.1. The Hall Effect and the Hall Voltage

In 1879 Hall discovered that when a thin current-carrying conducting or semiconducting strip is placed in a magnetic field perpendicular to the current, a transverse **potential difference** appears between the two sides of the strip, in the direction perpendicular to both the current and the field. This phenomenon is called the *Hall effect*, and the transverse potential difference is called the Hall voltage $U_{\mathrm{H}}$.

Let the strip lie along the current, with width $h$ (the direction in which the Hall voltage is measured) and thickness $b$ (along the magnetic field), and let the charge carriers have charge $q$, number density $n$ and **drift velocity** $\boldsymbol{v}$, so that the current is $I=nqvhb$. The carriers are deflected to one side by the magnetic force $q\boldsymbol{v}\times\boldsymbol{B}$, so charges of opposite signs accumulate on the two sides and produce a transverse electric field $E_{\mathrm{H}}$; when the transverse electric force balances the magnetic force,

$$
qE_{\mathrm{H}}=qvB,
$$
subsequent carriers are no longer deflected and a steady state is reached. Hence

$$
U_{\mathrm{H}}=E_{\mathrm{H}}h=vBh=\frac{1}{nq}\frac{IB}{b}=K_{\mathrm{H}}\frac{IB}{b},\qquad K_{\mathrm{H}}=\frac{1}{nq}.
$$
$K_{\mathrm{H}}$ is called the *Hall coefficient* (usually written $R_{\mathrm{H}}$ in the international literature), and $U_{\mathrm{H}}/I=B/(nqb)$ is called the Hall **resistance**.

The Hall effect has two main uses. First, the sign of $U_{\mathrm{H}}$ is determined by the sign of the carrier charge (for the same current direction, positive and negative carriers are deflected to the same side but accumulate charges of opposite signs), so measuring the sign of $U_{\mathrm{H}}$ identifies the type of carrier, and measuring the magnitude of $K_{\mathrm{H}}$ gives the number density $n$ of carriers. This is the experimental evidence for the existence of positively charged "holes" in semiconductors ([5.5.6](/5.5.6)). Second, when $K_{\mathrm{H}}$ is known, $U_{\mathrm{H}}$ measures the magnetic field (Hall probes, also used in the electronic compass of a mobile phone and in position sensors of brushless motors), or measures a large current through the magnetic field it produces.

**Example 7.3.1 (Hall Voltage in a Metal and in a Semiconductor)** The free-electron number density of copper is $n\approx8.5\times10^{28}\,\mathrm{m^{-3}}$. A copper strip of thickness $b=0.1\,\mathrm{mm}$ carries $I=10\,\mathrm{A}$ in a field $B=1\,\mathrm{T}$:

$$
U_{\mathrm{H}}=\frac{IB}{neb}=\frac{10\times1}{8.5\times10^{28}\times1.6\times10^{-19}\times10^{-4}}\,\mathrm{V}\approx7\,\mu\mathrm{V}.
$$
The carrier number density of a doped semiconductor can be as low as $10^{21}\,\mathrm{m^{-3}}$; a strip of the same thickness needs only $I=1\,\mathrm{mA}$ and $B=0.1\,\mathrm{T}$ to give a Hall voltage of about $6\,\mathrm{mV}$. This is why Hall elements are made of semiconductors.

### 7.3.2. The Quantum Hall Effect

In 1980 von Klitzing discovered that at very low temperature (about $1\,\mathrm{K}$) and in a strong field (about $10\,\mathrm{T}$), the Hall resistance of a two-dimensional electron gas at a semiconductor interface is no longer proportional to $B$ but shows a series of plateaus as $B$ increases:

$$
R_{\mathrm{H}}=\frac{R_{\mathrm{K}}}{\nu},\qquad \nu=1,2,3,\dots,\qquad R_{\mathrm{K}}=\frac{h}{e^2}=25\,812.807\,45\ldots\,\Omega.
$$
This is called the *quantum Hall effect*, and $R_{\mathrm{K}}$ is called the *von Klitzing constant*; von Klitzing received the 1985 Nobel Prize in Physics for it. The values of the plateaus are determined only by fundamental constants and are independent of the material, shape and impurities of the sample; plateau values measured in different laboratories agree to a relative precision of $10^{-10}$. Their origin lies in the discrete energy levels (Landau levels) formed by two-dimensional electrons in a strong field and in the topological properties of the wave functions. Hence from 1990 the conventional value $R_{\mathrm{K\text{-}90}}=25\,812.807\,\Omega$ was used internationally to realize the unit of resistance, the ohm. After the 2019 SI defined $h$ and $e$ as exact values, $R_{\mathrm{K}}=h/e^2$ itself became exact, and the quantum Hall resistance realizes the SI ohm directly.

In 1982 Tsui and Störmer found plateaus at fractional $\nu$ (such as $\frac13$, $\frac25$) in even purer samples, the fractional quantum Hall effect; Laughlin's theory shows that it arises from a collective state formed by strong correlations among the electrons, whose quasiparticles carry fractional charge (such as $e/3$, confirmed by current-noise experiments in 1997), and the three shared the 1998 Nobel Prize in Physics. In 2013 the group of Qikun Xue observed the quantum anomalous Hall effect, which needs no external magnetic field, in a magnetic topological-insulator thin film.

## 7.4. Magnetic Force on a Current-Carrying Wire

### 7.4.1. The Ampère Force

The current in a wire is the directed motion of charge carriers, and each carrier experiences the **Lorentz force** $q\boldsymbol{v}\times\boldsymbol{B}$; these forces are transmitted to the wire through the interaction of the carriers with the lattice and appear macroscopically as a force on the wire. Let the cross-sectional area of the wire be $S$, and the carriers have number density $n$, charge $q$ and drift velocity $\boldsymbol{v}$ (in the same direction as the line element $\mathrm{d}\boldsymbol{l}$). A length $\mathrm{d}l$ of wire contains $nS\,\mathrm{d}l$ carriers, and the sum of the forces on them is

$$
\mathrm{d}\boldsymbol{F}=nS\,\mathrm{d}l\,q\boldsymbol{v}\times\boldsymbol{B}=nqvS\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}=I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B},
$$
where $I=nqvS$.

**Theorem 7.4.1 (Ampère Force Law)** The force of a magnetic field on a current element $I\,\mathrm{d}\boldsymbol{l}$ is $\mathrm{d}\boldsymbol{F}=I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$, and the magnetic force on a current-carrying wire $L$ is

$$
\boldsymbol{F}=\int_LI\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}.
$$

The force of a magnetic field on a current is called the *Ampère force*. It is the working principle of electric motors, loudspeakers, galvanometers and so on. Two more recent examples: in an electromagnetic railgun, a current of megaamperes flows through two parallel rails and a conducting slider between them (or the plasma behind the slider) to form a circuit, and the Ampère force of the magnetic field of the rail currents on the slider current accelerates a projectile to several kilometers per second within milliseconds; in magnetohydrodynamic propulsion, a current passes transversely through the seawater in a duct and experiences an Ampère force in a perpendicular magnetic field, expelling the water along the duct and propelling the ship (the Japanese experimental ship Yamato-1, 1992), with no propeller or transmission parts.

**Example 7.4.1 (A Curved Wire in a Uniform Magnetic Field)** A wire $ab$ of arbitrary shape carries a current $I$ in a uniform magnetic field $\boldsymbol{B}$. Since $\boldsymbol{B}$ is a constant vector,

$$
\boldsymbol{F}=\int_a^bI\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}=I\Big(\int_a^b\mathrm{d}\boldsymbol{l}\Big)\times\boldsymbol{B}=I\,\overrightarrow{ab}\times\boldsymbol{B},
$$
with magnitude $F=I\,\lvert ab\rvert\,B\sin\theta$ ($\theta$ is the angle between $\overrightarrow{ab}$ and $\boldsymbol{B}$): the force on the curved wire is the same as on the straight wire joining its two ends. If $a$ and $b$ coincide, $\boldsymbol{F}=\boldsymbol{0}$: the total magnetic force on a closed current-carrying loop in a uniform field is zero (but the torque is in general not zero, see [§7.5](#sec-7.5)).

### 7.4.2. Force Between Parallel Currents and the Definition of the Ampere

**Example 7.4.2 (Force Between Parallel Straight Current-Carrying Wires)** Two parallel infinitely long straight wires in vacuum, a distance $d$ apart, carry currents $I_1$ and $I_2$. The field of $I_1$ at wire 2 is $B_1=\frac{\mu_0I_1}{2\pi d}$ ([5.3.6](/5.3.6)), perpendicular to the plane of the two wires, so wire 2 experiences a force per unit length

$$
\frac{\mathrm{d}F_2}{\mathrm{d}l}=B_1I_2=\frac{\mu_0I_1I_2}{2\pi d},
$$
lying in the plane of the two wires and perpendicular to them. Likewise, wire 1 experiences a force per unit length of the same magnitude and opposite direction. The wires attract each other when the currents are parallel and repel each other when they are antiparallel.

Before 2019 the SI used precisely this result to define the unit of current, the ampere (A): if two infinitely long parallel straight wires of negligible cross section, $1\,\mathrm{m}$ apart in vacuum, carry equal **steady currents** and the force per meter of length is $2\times10^{-7}\,\mathrm{N}$, then the current is $1\,\mathrm{A}$. This definition is equivalent to fixing $\mu_0=4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ as an exact value.

**Remark 7.4.1 (The 2019 SI)** From 20 May 2019 the SI defines the ampere by fixing the numerical value of the **elementary charge**, $e=1.602\,176\,634\times10^{-19}\,\mathrm{C}$: $1\,\mathrm{A}$ is the current of $1/(1.602\,176\,634\times10^{-19})$ elementary charges per second. Then $\mu_0$ is no longer a defined value but must be determined by measuring the fine-structure constant $\alpha$ ($\mu_0=2\alpha h/(e^2c)$):

$$
\mu_0=1.256\,637\,061\,27(20)\times10^{-6}\,\mathrm{N\,A^{-2}},
$$
which differs from $4\pi\times10^{-7}\,\mathrm{N\,A^{-2}}$ by a relative amount of order $10^{-10}$, and $4\pi\times10^{-7}$ is still used in everyday calculations. $\varepsilon_0=1/(\mu_0c^2)$ likewise becomes a measured value ([5.3.1](/5.3.1)).

## 7.5. Torque on a Current-Carrying Coil in a Uniform Magnetic Field

### 7.5.1. Magnetic Moment and Magnetic Torque

By Example 7.4.1, the net force on a closed coil in a uniform magnetic field is zero, but the forces on the various sides are not collinear, so the coil experiences a torque. Consider a rectangular coil with sides $l_1$ and $l_2$ carrying current $I$, free to rotate about a central axis parallel to the $l_2$ sides, with the field $\boldsymbol{B}$ perpendicular to the axis. The forces on the two $l_1$ sides are equal in magnitude, opposite in direction and collinear, so they cancel; the two $l_2$ sides are perpendicular to $\boldsymbol{B}$ and each experiences a force of magnitude $F=Il_2B$, in opposite directions, forming a couple. Let the angle between the normal to the plane of the coil (related to the current by the right-hand rule) and $\boldsymbol{B}$ be $\theta$; the lever arm of the couple is $l_1\sin\theta$, and the magnitude of the torque is

$$
M=Il_2B\cdot l_1\sin\theta=ISB\sin\theta,
$$
where $S=l_1l_2$ is the area of the coil. The torque depends on the coil only through the product $IS$, which leads to the introduction of a vector describing the magnetic properties of a current-carrying coil.

**Definition 7.5.1 (Magnetic Moment)** The **magnetic moment** of a planar coil of area $S$ carrying current $I$ is

$$
\boldsymbol{m}=IS\boldsymbol{e}_{\mathrm{n}},
$$
where $\boldsymbol{e}_{\mathrm{n}}$ is the unit normal vector of the plane of the coil, related to the sense of the current by the right-hand rule (when the fingers of the right hand curl along the current, the thumb points along $\boldsymbol{e}_{\mathrm{n}}$). The magnetic moment of a coil of $N$ turns is $NIS\boldsymbol{e}_{\mathrm{n}}$. The SI unit of magnetic moment is $\mathrm{A\,m^2}$ (also written $\mathrm{J/T}$).

The magnetic moment is also called the *magnetic dipole moment*: the field produced by a small coil at a distance has the same form as the electric field of an electric dipole (the field on the axis of a circular current in [5.3.6](/5.3.6)), and the coil is a **magnetic dipole**. In terms of the magnetic moment, the torque is

**Formula 7.5.1 (Magnetic Torque on a Current-Carrying Coil)**

$$
\boldsymbol{M}=\boldsymbol{m}\times\boldsymbol{B}.
$$

This result holds for a planar coil of any shape (any coil can be divided into many small rectangular coils, and the currents on the common sides of neighboring coils are opposite and cancel), and has exactly the same form as the torque $\boldsymbol{M}=\boldsymbol{p}\times\boldsymbol{E}$ on an electric dipole in a uniform electric field. The torque turns the coil toward the position where the magnetic moment is parallel to the field ($\theta=0$, stable equilibrium), that is, in the direction that increases the **magnetic flux** through the coil (computed along $\boldsymbol{e}_{\mathrm{n}}$).

The rotor of a DC motor is a current-carrying coil in a magnetic field; a commutator reverses the current as the coil passes the equilibrium position, so that the direction of the torque stays the same and the coil keeps rotating. In a moving-coil galvanometer, the magnetic torque on the coil balances the elastic torque of the hairspring, and the deflection angle is proportional to the current.

### 7.5.2. Potential Energy of a Magnetic Moment in a Uniform Magnetic Field

Let a coil with magnetic moment $\boldsymbol{m}$ be rotated in a uniform magnetic field from angle $\theta_1$ to $\theta_2$ with the current held fixed (the work done by the **source of electromotive force** maintaining the current is not considered). The work done by the external torque against the magnetic torque is

$$
A=\int_{\theta_1}^{\theta_2}mB\sin\theta\,\mathrm{d}\theta=mB(\cos\theta_1-\cos\theta_2).
$$
Taking the zero of potential energy where the moment is perpendicular to the field ($\theta=\pi/2$), the potential energy of a magnetic moment in a uniform field is

$$
E_{\mathrm{p}}=-mB\cos\theta=-\boldsymbol{m}\cdot\boldsymbol{B},
$$
corresponding to the **electrostatic potential energy** $E_{\mathrm{p}}=-\boldsymbol{p}\cdot\boldsymbol{E}$ of an electric dipole. The potential energy is lowest at $\theta=0$ and highest at $\theta=\pi$. In a nonuniform field, besides the torque the magnetic moment experiences a force $\boldsymbol{F}=\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$ ($\boldsymbol{m}$ held fixed), and a moment parallel to the field is pulled toward the strong-field region. This is why paramagnetic substances are attracted by a magnet and why an atomic beam splits in the Stern–Gerlach experiment ([5.5.4](/5.5.4)); the energy difference $2mB$ between different orientations of a magnetic moment in a field is the basis of nuclear magnetic resonance ([5.3.8](/5.3.8)).

**Example 7.5.1 (Magnetic Moment and Torque of a Rotating Charged Disk)** A plastic disk of radius $R$ is uniformly charged with surface charge density $\sigma$, rotates with angular velocity $\omega$ about the axis through its center perpendicular to its face, and is placed in a uniform magnetic field $\boldsymbol{B}$ perpendicular to the axis. Find the torque on the disk.

**Solution** Divide the disk into thin concentric rings. The ring of radius $r$ and width $\mathrm{d}r$ carries charge $\mathrm{d}q=\sigma\cdot2\pi r\,\mathrm{d}r$; in each revolution (time $2\pi/\omega$) this charge passes any cross section of the ring once, so the equivalent current and magnetic moment are

$$
\mathrm{d}I=\frac{\omega}{2\pi}\,\mathrm{d}q=\sigma\omega r\,\mathrm{d}r,\qquad \mathrm{d}m=\pi r^2\,\mathrm{d}I=\pi\sigma\omega r^3\,\mathrm{d}r.
$$
The moments of all rings point in the same direction (along $\boldsymbol{\omega}$ for $\sigma>0$), and integration gives

$$
m=\int_0^R\pi\sigma\omega r^3\,\mathrm{d}r=\frac{\pi\sigma\omega R^4}{4}.
$$
Since $\boldsymbol{m}\perp\boldsymbol{B}$, the magnitude of the torque is $M=mB=\frac14\pi\sigma\omega BR^4$, directed along $\boldsymbol{m}\times\boldsymbol{B}$, perpendicular to the axis and to the field.

**Remark 7.5.1 (Magnetic Moment and Angular Momentum)** Let the mass of the disk be $m_0$ and its total charge $Q=\sigma\pi R^2$; its **angular momentum** is $L=\frac12m_0R^2\omega$, so that

$$
\frac{m}{L}=\frac{\pi\sigma\omega R^4/4}{m_0R^2\omega/2}=\frac{Q}{2m_0}.
$$
As long as the distributions of charge and mass are proportional, any rotating charged body has $\boldsymbol{m}=\frac{Q}{2m_0}\boldsymbol{L}$. The next chapter ([5.3.8](/5.3.8)) shows that the ratio of the magnetic moment of the orbital motion of an electron to its angular momentum is exactly $-e/(2m_{\mathrm{e}})$, while for the electron spin this ratio is about twice as large, a quantum effect that the classical picture cannot explain. Because the magnetic moment is proportional to the angular momentum, the magnetic torque $\boldsymbol{m}\times\boldsymbol{B}$ in a field makes the angular momentum undergo **precession** about the field rather than turning the moment directly toward the field, just as the torque of gravity makes a top precess ([5.1.5](/5.1.5#sec-5.7.2)).

## Summary

- A moving charge experiences the **Lorentz force** $\boldsymbol{F}=q\boldsymbol{E}+q\boldsymbol{v}\times\boldsymbol{B}$; the magnetic force does no work. In a uniform field a particle moves in a circle or a helix with $R=p/(qB)$, and in the nonrelativistic case $T=2\pi m/(qB)$ is independent of the speed.
- Electric and magnetic fields transform from one reference frame to another; the magnetic force is a necessary consequence of the principle of relativity.
- The Hall voltage is $U_{\mathrm{H}}=IB/(nqb)$, and its sign identifies the type of carrier; the Hall resistance of a two-dimensional electron gas is quantized as $h/(\nu e^2)$.
- A current element experiences the Ampère force $I\,\mathrm{d}\boldsymbol{l}\times\boldsymbol{B}$; parallel currents in the same direction attract, with force per unit length $\mu_0I_1I_2/(2\pi d)$. Since 2019 the ampere has been defined through the elementary charge.
- The magnetic moment of a current-carrying coil is $\boldsymbol{m}=IS\boldsymbol{e}_{\mathrm{n}}$; in a uniform field it experiences the torque $\boldsymbol{m}\times\boldsymbol{B}$ and has potential energy $-\boldsymbol{m}\cdot\boldsymbol{B}$, in one-to-one correspondence with the electric dipole.

## Questions

1. A beam of electrons is accelerated from rest through a voltage $U$ and then enters a uniform magnetic field perpendicularly. How do the cyclotron radius and period change when the voltage is doubled (nonrelativistic case)?
   Hint: $v\propto\sqrt U$, so the radius $R=mv/(eB)$ becomes $\sqrt2$ times as large; the period $2\pi m/(eB)$ is unchanged.
2. Can a magnetic field set a charged particle at rest into motion? Can a steady magnetic field change the kinetic energy of a charged particle?
   Hint: Neither. A charge at rest experiences no magnetic force; the force of a steady magnetic field is perpendicular to the velocity and does no work. A changing magnetic field, however, produces an electric field ([5.3.9](/5.3.9)), which can accelerate particles, as in the betatron.
3. The net force on a closed current-carrying coil in a uniform magnetic field is zero. What about in a nonuniform field?
   Hint: In general it is not zero; the force is $\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$. A small coil whose moment is parallel to the field is pulled toward the strong-field region, for example a bar magnet attracting a small current-carrying coil.
4. The Hall voltage measured in a semiconductor sample has the opposite sign to that expected for conduction by electrons. What does this show?
   Hint: The majority carriers are positively charged; the sample is a p-type semiconductor and the carriers are holes ([5.5.6](/5.5.6)).
