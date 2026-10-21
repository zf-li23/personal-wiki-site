---
title: Magnetic Materials in Magnetic Fields
description: Paramagnetic, diamagnetic and ferromagnetic substances; orbital, spin and nuclear magnetic moments, Larmor precession and diamagnetism; magnetization and magnetization current; the magnetic field strength H, its circulation theorem, boundary conditions and magnetic shielding; magnetic domains, magnetization curves, hysteresis loops and the Curie temperature; simple magnetic circuits.
source_hash: 35d2c444a795
---

The preceding chapters dealt with magnetic fields in vacuum. Real magnetic fields always involve matter, and any substance is magnetized in a magnetic field and in turn modifies the field; from this point of view all substances are called magnetic materials. The structure of this chapter runs completely parallel to that of the **dielectrics** in [5.3.4](/5.3.4): we first explain microscopically why matter is magnetized (the magnetic moments of atoms, corresponding to the **electric dipole moments** of molecules), then use the magnetization to describe the degree of magnetization and the magnetization current to describe the contribution of magnetization to the field (corresponding to the **electric polarization** and the **bound charge**), and finally introduce the auxiliary quantity, the magnetic field strength $\boldsymbol{H}$, so that only conduction currents, which can be controlled, appear in the circulation theorem (corresponding to the **electric displacement field** $\boldsymbol{D}$). What differs from dielectrics is the ferromagnetic substance: its magnetization can make the field thousands of times stronger than the applied field, and it depends on the history of magnetization; this is the basis of electromagnets, transformers and permanent magnets. Magnetism is in the end a quantum phenomenon; the classical picture in this chapter is only a usable model, and the quantum theory of electron spin and atomic magnetic moments is given in [5.5.4](/5.5.4). Section 8.6 is optional.

## 8.1. The Effect of Magnetic Materials on the Magnetic Field

Fill a long straight solenoid with a uniform substance; the **magnetic flux density** inside the tube changes from its vacuum value $B_0$ to

$$
B=\mu_{\mathrm{r}}B_0,
$$
where the ratio $\mu_{\mathrm{r}}$ depends only on the substance and is called its *relative permeability*. Here $\boldsymbol{B}$ is the sum of the field $\boldsymbol{B}_0$ of the conduction current and the additional field $\boldsymbol{B}'$ produced by the magnetized substance, $\boldsymbol{B}=\boldsymbol{B}_0+\boldsymbol{B}'$. The phenomenon in which a substance acquires magnetism or its magnetism changes under the action of a magnetic field is called magnetization, and substances that can be magnetized are collectively called *magnetic materials*. According to the size of $\mu_{\mathrm{r}}$, magnetic materials fall into three classes:

| Class | $\mu_{\mathrm{r}}$ | Examples (room temperature, $\chi_{\mathrm{m}}=\mu_{\mathrm{r}}-1$) |
|---|---|---|
| Paramagnetic | slightly greater than 1 | aluminum $2.2\times10^{-5}$, platinum $2.6\times10^{-4}$, liquid oxygen ($90\,\mathrm{K}$) about $3.6\times10^{-3}$ |
| Diamagnetic | slightly less than 1 | water $-9.0\times10^{-6}$, copper $-9.6\times10^{-6}$, silver $-2.4\times10^{-5}$, bismuth $-1.7\times10^{-4}$ |
| Ferromagnetic | much greater than 1 | maximum of $\mu_{\mathrm{r}}$: pure iron about $5\times10^3$, silicon steel $10^3$–$10^4$, permalloy (nickel–iron alloy) up to $10^5$ |

A *paramagnetic substance* slightly strengthens the field and a *diamagnetic substance* slightly weakens it; for both, $\lvert\mu_{\mathrm{r}}-1\rvert$ is only of order $10^{-6}$–$10^{-3}$, and $\mu_{\mathrm{r}}$ is a constant independent of the applied field, so they are linear magnetic materials. A *ferromagnetic substance* strengthens the field greatly, and its $\mu_{\mathrm{r}}$ is not a constant but varies with the field and the history of magnetization (Section 8.5).

## 8.2. Magnetic Moments of Atoms

The magnetism of matter comes from the motion of charges in atoms. The **magnetic moment** of an atom ([5.3.7](/5.3.7)) has three sources: the orbital motion of the electrons around the nucleus, the spin of the electrons, and the magnetic moment of the nucleus.

### 8.2.1. Orbital Magnetic Moment of the Electron

In Bohr's model of the atom, an electron moves with speed $v$ on a circular orbit of radius $r$ around the nucleus, which is equivalent to a circular current

$$
I=\frac{e}{2\pi r/v}=\frac{ev}{2\pi r},
$$
whose magnetic moment has magnitude $m=I\cdot\pi r^2=\frac12evr$. The magnitude of the orbital **angular momentum** of the electron is $L=m_{\mathrm{e}}vr$, and since the electron is negatively charged, the magnetic moment is antiparallel to the angular momentum, so that

$$
\boldsymbol{m}_l=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}.
$$
The ratio of magnetic moment to angular momentum is called the *gyromagnetic ratio*; for the orbital motion of the electron it is $\gamma_l=-e/(2m_{\mathrm{e}})$, in agreement with the result $Q/(2m_0)$ for a rotating charged body in [5.3.7](/5.3.7). In quantum mechanics the components of the orbital angular momentum are integer multiples of $\hbar$, and the corresponding magnetic moments are measured in units of

$$
\mu_{\mathrm{B}}=\frac{e\hbar}{2m_{\mathrm{e}}}\approx9.274\times10^{-24}\,\mathrm{J/T},
$$
called the Bohr magneton ([5.5.4](/5.5.4)).

### 8.2.2. Spin Magnetic Moment of the Electron

The second source of the electron's magnetic moment is its spin. Spin is an intrinsic angular momentum of the electron and must not be thought of as rotation about its own axis; its component along any direction (such as that of an external magnetic field) can take only the values $S_z=m_s\hbar$, $m_s=\pm\frac12$ (see [5.5.4](/5.5.4)). The spin magnetic moment is related to the spin angular momentum by

$$
\boldsymbol{m}_s=-g_{\mathrm{e}}\frac{e}{2m_{\mathrm{e}}}\boldsymbol{S}\approx-\frac{e}{m_{\mathrm{e}}}\boldsymbol{S},\qquad m_{s,z}=\mp\mu_{\mathrm{B}},
$$
where $g_{\mathrm{e}}\approx2.002\,32$ is called the $g$-factor of the electron. The gyromagnetic ratio of spin is about twice that of orbital motion, which classical models cannot account for; $g_{\mathrm{e}}=2$ follows from Dirac's relativistic quantum mechanics, and the small deviation from 2 is calculated precisely in quantum electrodynamics.

### 8.2.3. Nuclear Magnetic Moments

Protons and neutrons also have spin, and the corresponding magnetic moments are written

$$
\boldsymbol{m}=g\frac{e}{2m_{\mathrm{p}}}\boldsymbol{S},\qquad g_{\mathrm{p}}\approx5.586,\qquad g_{\mathrm{n}}\approx-3.826.
$$
The neutron carries no charge yet has a magnetic moment (antiparallel to its spin), which shows that it has internal structure (it is made of charged quarks). The magnetic moment of a nucleus is the composition of the spin magnetic moments of the protons and neutrons and the orbital magnetic moments of the protons; it is written $\boldsymbol{m}=g\frac{e}{2m_{\mathrm{p}}}\boldsymbol{I}$, where $\boldsymbol{I}$ is the spin angular momentum of the nucleus (the usual notation in nuclear physics) and $g$ is determined by the particular nucleus. Because $m_{\mathrm{p}}\approx1836\,m_{\mathrm{e}}$, the unit of nuclear magnetic moments, the nuclear magneton $e\hbar/(2m_{\mathrm{p}})$, is three orders of magnitude smaller than the Bohr magneton, and the contribution of nuclear moments to the magnetism of matter can usually be neglected. But the **precession** of a nuclear moment in a magnetic field (Section 8.2.5) can be measured very precisely: the precession frequency of hydrogen nuclei in a field of $1\,\mathrm{T}$ is $42.58\,\mathrm{MHz}$, and resonance with a radio-frequency field at this frequency is nuclear magnetic resonance (NMR), the basis of the spectroscopic method for determining molecular structure in chemistry and of magnetic resonance imaging (MRI) in medicine.

### 8.2.4. Microscopic Explanation of Paramagnetism and Diamagnetism

The vector sum of the orbital magnetic moments, spin magnetic moments and nuclear moment of all the electrons in a molecule is called the intrinsic magnetic moment $\boldsymbol{m}_{\mathrm{mol}}$ of the molecule. In problems of magnetization, the intrinsic moment of each molecule can be regarded as an equivalent circular current, which is Ampère's hypothesis of molecular currents.

The molecules of a paramagnetic substance have intrinsic moments, of order $10^{-23}\,\mathrm{A\,m^2}$ (about one Bohr magneton), coming mainly from electrons. Without an applied field, thermal motion makes the moments of the molecules completely random, and macroscopically there is no magnetism. When an external field $\boldsymbol{B}_0$ is applied, the molecular moments experience the torque $\boldsymbol{m}_{\mathrm{mol}}\times\boldsymbol{B}_0$ and the potential energy $-\boldsymbol{m}_{\mathrm{mol}}\cdot\boldsymbol{B}_0$, which makes the moments tend to align along the field, while thermal motion destroys this alignment; the result is partial order: the moments have a net average along the field and the field inside the medium is strengthened. Since $m_{\mathrm{mol}}B_0\ll k_{\mathrm{B}}T$ (about $10^{-23}\,\mathrm{J}$ in $1\,\mathrm{T}$, while $k_{\mathrm{B}}T\approx4\times10^{-21}\,\mathrm{J}$ at room temperature), the degree of order is very low, and the **Boltzmann distribution** shows that the average moment is proportional to $m_{\mathrm{mol}}B_0/(k_{\mathrm{B}}T)$, so the susceptibility of a paramagnetic substance is inversely proportional to the temperature, $\chi_{\mathrm{m}}=C/T$ (Curie's law). Macroscopically, a paramagnetic substance behaves like a small magnet placed along the applied field and is attracted by a magnet.

In the molecules of a diamagnetic substance, the orbital and spin moments of the electrons exactly cancel, and the intrinsic moment is zero. In an applied field the orbital motion of every electron acquires an additional moment opposite to the field (Section 8.2.5); the sum of these additional moments is called the induced moment, and it weakens the field inside the medium. A diamagnetic substance behaves like a small magnet placed against the applied field and is repelled by a magnet. The induced moment is almost independent of temperature, so the susceptibility of a diamagnetic substance is also almost independent of temperature.

### 8.2.5. Larmor Precession and the Induced Moment

The orbital magnetic moment of an electron, $\boldsymbol{m}=-\frac{e}{2m_{\mathrm{e}}}\boldsymbol{L}$, experiences the torque $\boldsymbol{m}\times\boldsymbol{B}_0$ in an external field $\boldsymbol{B}_0$. By the **angular momentum theorem**,

$$
\frac{\mathrm{d}\boldsymbol{L}}{\mathrm{d}t}=\boldsymbol{m}\times\boldsymbol{B}_0=\frac{e}{2m_{\mathrm{e}}}\boldsymbol{B}_0\times\boldsymbol{L}.
$$
$\mathrm{d}\boldsymbol{L}$ is always perpendicular to both $\boldsymbol{L}$ and $\boldsymbol{B}_0$, so the torque changes neither the magnitude of the angular momentum nor its angle with $\boldsymbol{B}_0$; it only makes $\boldsymbol{L}$ rotate about $\boldsymbol{B}_0$ with angular velocity

$$
\boldsymbol{\omega}_{\mathrm{L}}=\frac{e}{2m_{\mathrm{e}}}\boldsymbol{B}_0.
$$
This is the same thing as the **precession** of a top under the torque of gravity ([5.1.5](/5.1.5#sec-5.7.2)), and is called *Larmor precession*. In general, a magnetic moment with gyromagnetic ratio $\gamma$ precesses in a magnetic field at $\omega=\lvert\gamma\rvert B$, independent of the angle between the moment and the field; the Larmor frequency of an electron orbit in $1\,\mathrm{T}$ is about $14\,\mathrm{GHz}$, and the nuclear magnetic resonance frequency above was obtained in the same way.

The precession amounts to an additional rotation of the entire electron orbit with angular velocity $\boldsymbol{\omega}_{\mathrm{L}}$ (along $\boldsymbol{B}_0$). The negatively charged electron rotating with its orbit in this way forms an additional circular current, whose magnetic moment is antiparallel to $\boldsymbol{\omega}_{\mathrm{L}}$, namely

$$
\Delta\boldsymbol{m}=-\frac{e^2\overline{\rho^2}}{4m_{\mathrm{e}}}\boldsymbol{B}_0,
$$
where $\overline{\rho^2}$ is the mean square distance of the electron from the axis through the nucleus parallel to $\boldsymbol{B}_0$. Whatever the direction in which the electron originally orbits the nucleus, the additional moment is always opposite to the applied field: this is the origin of diamagnetism. The induced moment is much smaller than the intrinsic moment, so all substances are diamagnetic, but in substances with intrinsic moments diamagnetism is masked by paramagnetism.

**Example 8.2.1 (Diamagnetic Levitation)** A diamagnetic body in a nonuniform magnetic field experiences a force toward the weak-field region. For a medium of susceptibility $\chi_{\mathrm{m}}$ ($\lvert\chi_{\mathrm{m}}\rvert\ll1$), the energy per unit volume in a magnetic field is $-\frac{\chi_{\mathrm{m}}B^2}{2\mu_0}$, and the force per unit volume in the vertical direction is $\frac{\chi_{\mathrm{m}}}{\mu_0}B\frac{\mathrm{d}B}{\mathrm{d}z}$. To levitate a diamagnetic body of density $\rho$ requires

$$
B\Big\lvert\frac{\mathrm{d}B}{\mathrm{d}z}\Big\rvert\ge\frac{\mu_0\rho g}{\lvert\chi_{\mathrm{m}}\rvert}.
$$
For water, $\rho=10^3\,\mathrm{kg/m^3}$ and $\chi_{\mathrm{m}}=-9.0\times10^{-6}$, so the right side is about $1.4\times10^{3}\,\mathrm{T^2/m}$; for example $B\approx16\,\mathrm{T}$ and a **gradient** of about $100\,\mathrm{T/m}$ near the mouth of a magnet. Living organisms consist mainly of diamagnetic substances such as water and proteins, and in 1997 Geim and Berry used just such a strong magnet to levitate a live frog (for which they received the 2000 Ig Nobel Prize in Physics; Geim later shared the 2010 Nobel Prize in Physics with Novoselov for producing graphene by the adhesive-tape exfoliation method).

## 8.3. Magnetization of Magnetic Materials

### 8.3.1. Magnetization

The magnetization of a magnetic material is similar to the polarization of a dielectric: the conduction current $I_0$ produces the external field $\boldsymbol{B}_0$; the magnetized medium produces an additional field $\boldsymbol{B}'$, the total field in the medium is $\boldsymbol{B}=\boldsymbol{B}_0+\boldsymbol{B}'$, and the degree of magnetization is in turn determined by the total field $\boldsymbol{B}$.

**Definition 8.3.1 (Magnetization)** The vector sum of the molecular magnetic moments per unit volume near a point in the medium,

$$
\boldsymbol{M}=\frac{\sum\boldsymbol{m}_{\mathrm{mol}}}{\Delta V}
$$
is called the **magnetization** at that point. $\Delta V$ is macroscopically small (much smaller than the scale over which $\boldsymbol{M}$ changes appreciably) and microscopically large (much larger than the intermolecular spacing). The SI unit of magnetization is $\mathrm{A/m}$, which has the same dimension as the surface **current density**.

$\boldsymbol{M}$ reflects the degree of order in the arrangement of the molecular moments and is the response of the medium to the total magnetic field $\boldsymbol{B}$. Experiments show that for an isotropic linear magnetic material $\boldsymbol{M}$ is proportional to $\boldsymbol{B}$:

$$
\boldsymbol{M}=\frac{\mu_{\mathrm{r}}-1}{\mu_0\mu_{\mathrm{r}}}\boldsymbol{B}.
$$
For a paramagnetic substance $\boldsymbol{M}$ is parallel to $\boldsymbol{B}$, for a diamagnetic substance antiparallel. For a ferromagnetic substance the relation between $\boldsymbol{M}$ and $\boldsymbol{B}$ is nonlinear and multivalued, and the formula above does not apply.

### 8.3.2. Magnetization Current

In a magnetized medium, the ordered arrangement of the molecular currents appears macroscopically as an equivalent current distribution, called the *magnetization current* (also the bound current). As far as producing a magnetic field and being acted on by one are concerned, the magnetization current is completely equivalent to a conduction current; the difference is that it involves no macroscopic motion of charge and produces no Joule heat. Inside a uniformly magnetized medium neighboring molecular currents cancel and only an uncancelled part remains on the surface; when the magnetization is nonuniform there is also magnetization current inside the medium.

We now find the relation between the magnetization current and the magnetization. Take an arbitrary closed path $L$ in the medium and find the magnetization current $I'$ linked with it. Let each molecular current be $i$ with area $S_{\mathrm{mol}}$, magnetic moment $\boldsymbol{m}_{\mathrm{mol}}=iS_{\mathrm{mol}}\boldsymbol{e}_{\mathrm{n}}$, and let the number density of molecules be $n$. Only the molecular currents "threaded" by $L$ are linked once with $L$, and they contribute to $I'$; molecular currents that are not threaded either do not meet $L$ or pass twice through a surface bounded by $L$, and contribute nothing. The centers of the molecular currents threaded by a line element $\mathrm{d}\boldsymbol{l}$ lie in an oblique cylinder with base $S_{\mathrm{mol}}$ and axis $\mathrm{d}\boldsymbol{l}$, of volume $S_{\mathrm{mol}}\,\mathrm{d}l\cos\theta$ ($\theta$ is the angle between $\boldsymbol{e}_{\mathrm{n}}$ and $\mathrm{d}\boldsymbol{l}$), so

$$
\mathrm{d}I'=n\,i\,S_{\mathrm{mol}}\cos\theta\,\mathrm{d}l=\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}.
$$

**Theorem 8.3.1 (Magnetization Current and Magnetization)** The magnetization current linked with any closed loop $L$ (that is, the magnetization current through any surface $S$ bounded by $L$ and related to $L$ by the right-hand rule) is

$$
I'=\oint_L\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}.
$$
The corresponding differential form and the form at an interface are

$$
\boldsymbol{J}'=\nabla\times\boldsymbol{M},\qquad \boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}},
$$
where $\boldsymbol{J}'$ is the volume magnetization current density, $\boldsymbol{K}'$ is the surface magnetization current density on the surface of the medium (magnetization current per unit length, in $\mathrm{A/m}$), and $\boldsymbol{e}_{\mathrm{n}}$ is the outward unit normal of the surface of the medium.

**Proof** By **Stokes' theorem** ([2.2.14](/2.2.14#sec-14.3.1)), $\oint_L\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}=\iint_S(\nabla\times\boldsymbol{M})\cdot\mathrm{d}\boldsymbol{S}$, while $I'=\iint_S\boldsymbol{J}'\cdot\mathrm{d}\boldsymbol{S}$ holds for any surface, so $\boldsymbol{J}'=\nabla\times\boldsymbol{M}$. At the surface of the medium take a flat rectangular loop straddling the surface, with long sides $\Delta l$ along a unit tangent vector $\boldsymbol{e}_{\mathrm{t}}$, one inside the medium and one outside (where $\boldsymbol{M}=\boldsymbol{0}$), and with short sides tending to zero; then $\oint\boldsymbol{M}\cdot\mathrm{d}\boldsymbol{l}=\boldsymbol{M}\cdot\boldsymbol{e}_{\mathrm{t}}\,\Delta l$. For a loop traversed in this way, the normal related to the sense of traversal by the right-hand rule is $\boldsymbol{e}_{\mathrm{t}}\times\boldsymbol{e}_{\mathrm{n}}$, and the surface current through the loop is $\boldsymbol{K}'\cdot(\boldsymbol{e}_{\mathrm{t}}\times\boldsymbol{e}_{\mathrm{n}})\Delta l=(\boldsymbol{e}_{\mathrm{n}}\times\boldsymbol{K}')\cdot\boldsymbol{e}_{\mathrm{t}}\,\Delta l$. Equating the two for all tangent vectors $\boldsymbol{e}_{\mathrm{t}}$ gives the tangential component $\boldsymbol{M}_t=\boldsymbol{e}_{\mathrm{n}}\times\boldsymbol{K}'$; since $\boldsymbol{K}'$ lies along the interface, this is equivalent to $\boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}}$, whose magnitude equals the tangential component of $\boldsymbol{M}$. $\square$

These three relations correspond one to one to the relations $q'=-\oiint\boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}$, $\rho'=-\nabla\cdot\boldsymbol{P}$, $\sigma'=\boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}}$ for the polarization charge in dielectrics ([5.3.4](/5.3.4)): in dielectrics one has flux and **divergence**, in magnetic materials circulation and **curl**.

**Example 8.3.1 (Uniform Magnetization in a Long Straight Solenoid)** A long straight solenoid is filled with a uniform isotropic medium that is uniformly magnetized with magnetization $\boldsymbol{M}$ (along the axis). Find the field produced by the medium.

**Solution** Inside the medium the magnetization is uniform, $\nabla\times\boldsymbol{M}=\boldsymbol{0}$, and there is no volume magnetization current. On the lateral surface $\boldsymbol{M}$ is parallel to the surface, and the surface magnetization current density is $K'=M$, circulating around the axis, which is equivalent to a long straight solenoid with current $M$ per unit length. From the field of a long straight solenoid, $B=\mu_0nI$ ([5.3.6](/5.3.6)), the additional field produced by the medium is

$$
\boldsymbol{B}'=\mu_0\boldsymbol{M}.
$$
Here the magnetization current is completely equivalent to the medium.

## 8.4. The Circulation Theorem for H

### 8.4.1. The Magnetic Field Strength

In the presence of a medium the magnetic field is still produced by all currents (the conduction current $I_0$ and the magnetization current $I'$), so the **divergence theorem** for the magnetic field (**Gauss's law for magnetism**) and the circuital law still hold:

$$
\oiint_S\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0,\qquad \oint_L\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{l}=\mu_0\big(I_{0,\mathrm{enc}}+I'_{\mathrm{enc}}\big).
$$
But the magnetization current is not known in advance and itself depends on the field to be found, so the second relation is inconvenient to use directly. Substituting Theorem 8.3.1 and rearranging gives

$$
\oint_L\Big(\frac{\boldsymbol{B}}{\mu_0}-\boldsymbol{M}\Big)\cdot\mathrm{d}\boldsymbol{l}=I_{0,\mathrm{enc}}.
$$

**Definition 8.4.1 (Magnetic Field Strength)** The auxiliary vector

$$
\boldsymbol{H}=\frac{\boldsymbol{B}}{\mu_0}-\boldsymbol{M}
$$
is called the **magnetic field strength**. Its SI unit is $\mathrm{A/m}$; the unit in the CGS system is the oersted, $1\,\mathrm{Oe}=\frac{10^3}{4\pi}\,\mathrm{A/m}\approx79.6\,\mathrm{A/m}$.

**Theorem 8.4.1 (Circulation Theorem for $\boldsymbol{H}$)** The circulation of the magnetic field strength around any closed loop equals the algebraic sum of the conduction currents linked with the loop:

$$
\oint_L\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_{0,\mathrm{enc}},\qquad\text{differential form}\quad\nabla\times\boldsymbol{H}=\boldsymbol{J}_0.
$$

$\boldsymbol{H}=\boldsymbol{B}/\mu_0-\boldsymbol{M}$ is a general definition and also holds for ferromagnetic substances; in vacuum $\boldsymbol{M}=\boldsymbol{0}$ and $\boldsymbol{H}=\boldsymbol{B}/\mu_0$. Note that the circulation of $\boldsymbol{H}$ is determined only by conduction currents, which does not mean that $\boldsymbol{H}$ itself is determined only by conduction currents: the divergence $\nabla\cdot\boldsymbol{H}=-\nabla\cdot\boldsymbol{M}$ is in general not zero. Only in problems of sufficiently high symmetry can $\boldsymbol{H}$ be found from its circulation theorem alone.

### 8.4.2. Isotropic Linear Magnetic Materials

Expressing the experimental law of Section 8.3.1 in terms of $\boldsymbol{H}$: from $\boldsymbol{B}=\mu_0(\boldsymbol{H}+\boldsymbol{M})$ and $\boldsymbol{M}=\frac{\mu_{\mathrm{r}}-1}{\mu_0\mu_{\mathrm{r}}}\boldsymbol{B}$ we obtain

$$
\boldsymbol{M}=\chi_{\mathrm{m}}\boldsymbol{H},\qquad \boldsymbol{B}=\mu_0\mu_{\mathrm{r}}\boldsymbol{H}=\mu\boldsymbol{H},\qquad \mu_{\mathrm{r}}=1+\chi_{\mathrm{m}}.
$$
The dimensionless proportionality coefficient $\chi_{\mathrm{m}}$ is called the *magnetic susceptibility*, and $\mu=\mu_0\mu_{\mathrm{r}}$ is called the *permeability*. For a paramagnetic substance $\chi_{\mathrm{m}}>0$, for a diamagnetic substance $\chi_{\mathrm{m}}<0$. In an isotropic linear medium $\boldsymbol{M}$, $\boldsymbol{B}$ and $\boldsymbol{H}$ have the same direction.

**Property 8.4.1 (Distribution of the Magnetization Current)** In a homogeneous isotropic linear magnetic medium ($\mu_{\mathrm{r}}$ constant, whether or not the magnetization is uniform),

$$
\boldsymbol{J}'=\nabla\times\boldsymbol{M}=\chi_{\mathrm{m}}\nabla\times\boldsymbol{H}=\chi_{\mathrm{m}}\boldsymbol{J}_0.
$$
Hence where there is no conduction current inside the medium there is no volume magnetization current either; if there is no conduction current in the medium, the magnetization current is distributed only on the surface of the medium.

**Example 8.4.1 (A Current-Carrying Magnetic Slab)** An infinite uniform slab of thickness $2h$ ($-h<y<h$) is made of an isotropic linear medium of relative permeability $\mu_{\mathrm{r}}$ and carries a uniform conduction current of density $\boldsymbol{J}_0=J_0\boldsymbol{e}_z$. Find the magnetic field in space and the surface magnetization current on the faces of the slab.

**Solution** Symmetry analysis: the system is invariant under translations in the $x$ and $z$ directions, so the fields depend only on $y$; every plane parallel to the $yz$ plane is a mirror plane of the system, and $\boldsymbol{B}$, as an **axial vector**, must be perpendicular to the mirror, that is, $\boldsymbol{B}=B(y)\boldsymbol{e}_x$; the plane $y=0$ is also a mirror plane, so $B(-y)=-B(y)$. $\boldsymbol{H}$ has the same properties.

In the $xy$ plane take a rectangular loop whose two sides of length $\Delta l$ are parallel to the $x$ axis, at $y$ and $-y$, traversed in the sense related to $\boldsymbol{e}_z$ by the right-hand rule. By the circulation theorem for $\boldsymbol{H}$,

$$
\big[H_x(-y)-H_x(y)\big]\Delta l=-2H_x(y)\,\Delta l=2J_0\min(y,h)\,\Delta l\qquad(y>0),
$$
so

$$
\boldsymbol{H}=\begin{cases}-J_0y\,\boldsymbol{e}_x,&\lvert y\rvert\le h,\\-J_0h\,\operatorname{sgn}(y)\,\boldsymbol{e}_x,&\lvert y\rvert>h,\end{cases}\qquad \boldsymbol{B}=\begin{cases}-\mu_0\mu_{\mathrm{r}}J_0y\,\boldsymbol{e}_x,&\lvert y\rvert\le h,\\-\mu_0J_0h\,\operatorname{sgn}(y)\,\boldsymbol{e}_x,&\lvert y\rvert>h.\end{cases}
$$
Inside the slab $\boldsymbol{M}=(\mu_{\mathrm{r}}-1)\boldsymbol{H}=-(\mu_{\mathrm{r}}-1)J_0y\,\boldsymbol{e}_x$. On the upper surface $\boldsymbol{e}_{\mathrm{n}}=\boldsymbol{e}_y$ and $\boldsymbol{K}'_{\text{top}}=\boldsymbol{M}\times\boldsymbol{e}_y=-(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_z$; on the lower surface $\boldsymbol{e}_{\mathrm{n}}=-\boldsymbol{e}_y$, $\boldsymbol{M}=(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_x$, and again $\boldsymbol{K}'_{\text{bottom}}=-(\mu_{\mathrm{r}}-1)J_0h\,\boldsymbol{e}_z$. The magnetization currents on the two surfaces point the same way and do not add up to zero. This is not a contradiction: inside the slab there is also a volume magnetization current $\boldsymbol{J}'=\nabla\times\boldsymbol{M}=(\mu_{\mathrm{r}}-1)J_0\boldsymbol{e}_z$ (Property 8.4.1), and the volume magnetization current per unit width, $2h(\mu_{\mathrm{r}}-1)J_0$, exactly cancels the $-2(\mu_{\mathrm{r}}-1)J_0h$ of the two surfaces, so the total magnetization current is zero. The field outside the slab is therefore the same as without the medium.

![The magnetic flux density $B_x$ inside and outside a current-carrying magnetic slab (gray region). $\boldsymbol{H}$ is determined only by the conduction current and is the same as the curve for $\mu_{\mathrm{r}}=1$; inside the slab $B$ is increased by the factor $\mu_{\mathrm{r}}$, and at the faces of the slab the tangential component of $B$ jumps while that of $H$ is continuous; the field outside the slab is independent of the medium](./plots/slab-fields.py)

### 8.4.3. Boundary Conditions for the Magnetic Field and Magnetic Shielding

At the interface between two media the magnetic field is in general discontinuous, so the differential equations cannot be used and the boundary conditions must be derived from the integral forms. Let $\boldsymbol{e}_{\mathrm{n}}$ be the unit normal pointing from medium 2 into medium 1.

- Normal component: take a flat cylindrical surface straddling the interface (bases of area $\Delta S$, height tending to zero); $\oiint\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}=0$ gives $(B_{1n}-B_{2n})\Delta S=0$, that is, $B_{1n}=B_{2n}$: the normal component of $\boldsymbol{B}$ is continuous.
- Tangential component: take a flat rectangular loop straddling the interface; the circulation theorem for $\boldsymbol{H}$ gives $\boldsymbol{e}_{\mathrm{n}}\times(\boldsymbol{H}_1-\boldsymbol{H}_2)=\boldsymbol{K}_0$, where $\boldsymbol{K}_0$ is the conduction surface current density on the interface. When there is no conduction current on the interface, $H_{1t}=H_{2t}$: the tangential component of $\boldsymbol{H}$ is continuous.

**Example 8.4.2 ("Refraction" of Magnetic Field Lines)** At the interface between two isotropic linear media with no conduction current, the **magnetic field lines** in the media make angles $\theta_1$ and $\theta_2$ with the normal to the interface. From $B_{1n}=B_{2n}$ and $B_{1t}/\mu_1=B_{2t}/\mu_2$,

$$
\frac{\tan\theta_1}{\tan\theta_2}=\frac{B_{1t}/B_{1n}}{B_{2t}/B_{2n}}=\frac{\mu_1}{\mu_2}.
$$
If $\mu_1\gg\mu_2$ (medium 1 is a ferromagnet and medium 2 is air), then as long as $\theta_2$ is not zero, $\theta_1$ is close to $90^\circ$: the field lines in the iron are almost parallel to the interface and run along the iron core, and $B$ in the iron is much larger than $B$ in the air. This is why an iron core can confine field lines within it and guide the magnetic flux, and it is also the principle of magnetostatic shielding: a shield made of a high-permeability material (such as permalloy) provides a path of very low reluctance for the field lines, so that most of the field lines of an external field pass through the wall of the shield and the field inside is greatly weakened. Precision electron-beam instruments, magnetic sensors and old cathode-ray tubes all need such magnetic shielding. Unlike the complete shielding of an electrostatic field by a **conductor**, magnetostatic shielding can only weaken the field and cannot isolate it completely.

## 8.5. Ferromagnetic Substances

### 8.5.1. Magnetic Domains

Iron, cobalt, nickel and many of their alloys and compounds are ferromagnetic. Their magnetism comes mainly from the spin magnetic moments of electrons: between the spins of electrons in neighboring atoms there is a strong interaction that makes them tend to align in parallel. This exchange interaction is a consequence of the indistinguishability of electrons and the Pauli exclusion principle ([5.5.4](/5.5.4)); in essence it is a quantum effect of the electrostatic interaction, and it is much stronger than the classical magnetic interaction between magnetic moments. Below the Curie temperature (Section 8.5.4), the exchange interaction causes many spontaneously magnetized small regions to form inside a ferromagnetic substance; within each region the atomic moments are neatly aligned in the same direction, and such a region is called a *magnetic domain*.

The linear size of a domain is $10^{-6}$–$10^{-3}\,\mathrm{m}$, and a domain contains $10^{12}$–$10^{15}$ atoms. The moments in a domain are aligned along an easy axis of magnetization of the crystal, and different domains have different magnetization directions. That a whole piece of ferromagnet does not spontaneously magnetize as one whole is the result of competition between two energies: if it were magnetized as a whole, the magnetic poles appearing on its surface would produce a strong field outside and the magnetostatic energy would be very high; dividing into domains with different magnetization directions can greatly reduce the magnetostatic energy, but in the transition layers between domains (the domain walls) neighboring moments are not parallel, which costs exchange energy. The balance of the two determines the size and shape of the domains. Without an external field the orientations of the domains are usually random, and macroscopically there is no magnetism. Domains can be observed directly by methods such as the magneto-optical Kerr effect.

When an external field is applied, domains whose magnetization is close to the field direction have lower energy, and motion of the domain walls enlarges these domains and shrinks the others; as the field increases further, the magnetization of the remaining domains rotates toward the field; finally all domains are aligned along the field and the magnetization reaches saturation. In the intermediate stage of magnetization the domain walls move in jumps (pinned by defects in the crystal and then breaking free), and the magnetization changes in small jumps accordingly, producing noise pulses in a coil wound on the sample; this is called the Barkhausen effect, and it directly demonstrates that a ferromagnet is magnetized domain by domain.

### 8.5.2. Magnetization Curves

The relation between $\boldsymbol{B}$ and $\boldsymbol{H}$ in a ferromagnetic substance is nonlinear and not single-valued. One can still formally write $B=\mu_0\mu_{\mathrm{r}}H$, but $\mu_{\mathrm{r}}$ is neither constant nor uniquely determined by $H$.

Measurement method: make the material under test into a ring and wind it tightly with a coil of $n$ turns per unit length carrying current $I_0$. By the circulation theorem for $\boldsymbol{H}$ and the symmetry of the ring, $H=nI_0$ inside the ring; a secondary coil is wound as well and connected to a ballistic galvanometer or fluxmeter, and the change of the **magnetic flux** $\Phi$ ([5.3.9](/5.3.9)) is found from the charge passing through the secondary coil when the current changes, which gives $B=\Phi/S$. Changing $I_0$ point by point gives the relation between $B$ and $H$.

Starting from a completely unmagnetized state ($H=0$, $B=0$) and increasing $H$ gives the initial magnetization curve: at first $B$ increases slowly (reversible domain-wall motion), then rapidly (irreversible domain-wall motion), and finally levels off (domain rotation); after the saturation flux density $B_{\mathrm{s}}$ is reached, $B$ grows only slowly as $\mu_0H$. Correspondingly, $\mu_{\mathrm{r}}=B/(\mu_0H)$ increases from its initial value $\mu_{\mathrm{i}}$ to a maximum $\mu_{\mathrm{m}}$ and then decreases with saturation.

### 8.5.3. Hysteresis Loops

After magnetizing to saturation and then decreasing $H$, $B$ does not return along the initial magnetization curve but lags behind the change of $H$; this is called hysteresis. When $H$ has decreased to zero, $B$ still retains a value $B_{\mathrm{r}}$, called the remanent flux density, or *remanence* for short; to reduce $B$ to zero a reverse field $-H_{\mathrm{c}}$ must be applied, and $H_{\mathrm{c}}$ is called the *coercivity*. Continuing to magnetize in the reverse direction to saturation and then magnetizing in the forward direction again, the $B$–$H$ curve forms a closed curve called the *hysteresis loop*. Hysteresis arises from the irreversibility of domain-wall motion.

![Hysteresis loops of ferromagnetic substances (simplified model). Left: a soft magnetic material, with a narrow loop; the dashed line is the initial magnetization curve, and the remanence $B_{\mathrm{r}}$ and coercivity $H_{\mathrm{c}}$ are marked; right: a hard magnetic material, with a coercivity thousands of times larger (note the units of the horizontal axis) and a wide loop](./plots/hysteresis-loops.py)

In one cycle of magnetization, the work done by the surroundings per unit volume of the ferromagnetic substance equals the area enclosed by the hysteresis loop, $\oint H\,\mathrm{d}B$ (the magnetic field energy of [5.3.9](/5.3.9)); this energy is finally turned into heat and is called the hysteresis loss. According to the shape of the loop, ferromagnetic materials fall into two classes:

| | Soft magnetic materials | Hard magnetic materials |
|---|---|---|
| Coercivity $H_{\mathrm{c}}$ | small, $<10^2\,\mathrm{A/m}$, below $1\,\mathrm{A/m}$ for permalloy | large, $10^4$–$10^6\,\mathrm{A/m}$ |
| Hysteresis loop | narrow, high permeability, low hysteresis loss | wide, large remanence ($0.1$–$1.4\,\mathrm{T}$) |
| Examples | pure iron, silicon steel, permalloy, soft ferrites | carbon steel, tungsten steel, alnico, neodymium–iron–boron |
| Uses | cores of transformers, motors and AC electromagnets | permanent magnets, magnetic recording media |

### 8.5.4. The Curie Temperature

As the temperature rises, thermal motion destroys the neat alignment of the moments within the domains, and the spontaneous magnetization decreases. When the temperature exceeds a certain **critical temperature** $T_{\mathrm{C}}$, the spontaneous magnetization vanishes, the domains disintegrate, and the ferromagnetic substance becomes paramagnetic; on cooling below $T_{\mathrm{C}}$ ferromagnetism returns. $T_{\mathrm{C}}$ is called the *Curie temperature*, also the Curie point. The Curie temperatures of several ferromagnets: iron $1043\,\mathrm{K}$ ($770\,^\circ\mathrm{C}$), cobalt $1388\,\mathrm{K}$ ($1115\,^\circ\mathrm{C}$), nickel $627\,\mathrm{K}$ ($354\,^\circ\mathrm{C}$). Above $T_{\mathrm{C}}$ the susceptibility approximately obeys the Curie–Weiss law $\chi_{\mathrm{m}}=C/(T-T_{\mathrm{C}})$. The appearance and disappearance of ferromagnetism is a phase transition, similar to the behavior of a liquid near the **critical point**.

Besides ferromagnetism, the exchange interaction can also make neighboring moments align antiparallel: if the antiparallel moments are equal, the macroscopic moment is zero, which is called antiferromagnetism (for example $\ce{MnO}$); if they are unequal, there is still a macroscopic moment, which is called ferrimagnetism, and ferrites (such as $\ce{Fe3O4}$) belong to this class; they are commonly used soft magnetic materials in high-frequency circuits.

## 8.6. Simple Magnetic Circuits

After an iron core is magnetized, almost all the field lines are concentrated in the core (Section 8.4.3), and the core guides the magnetic flux just as a wire guides current. The path through which the field lines are concentrated is called a *magnetic circuit*.

Consider a toroidal iron core of cross-sectional area $S$, mean length $l$ and permeability $\mu$, with a narrow air gap of length $\delta$ cut in it and a coil of $N$ turns carrying current $I$ wound on it. Neglecting leakage flux, the flux $\Phi=BS$ is the same in the core and in the gap ($B_n$ is continuous). The circulation theorem for $\boldsymbol{H}$ along the core gives

$$
\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=Hl+H_\delta\delta=\frac{\Phi}{\mu S}l+\frac{\Phi}{\mu_0S}\delta=NI,
$$
so

$$
\Phi=\frac{NI}{R_{\mathrm{m}}+R_{\mathrm{m}\delta}},\qquad R_{\mathrm{m}}=\frac{l}{\mu S},\qquad R_{\mathrm{m}\delta}=\frac{\delta}{\mu_0S}.
$$
$\mathcal{E}_{\mathrm{m}}=NI$ is called the *magnetomotive force* and $R_{\mathrm{m}}=l/(\mu S)$ is called the *reluctance*. This is completely analogous to a circuit containing an **electromotive force** ([5.3.5](/5.3.5)):

| Magnetic circuit | Electric circuit |
|---|---|
| magnetomotive force $\mathcal{E}_{\mathrm{m}}=NI$ | emf $\mathcal{E}$ |
| magnetic flux $\Phi$ | current $I$ |
| reluctance $R_{\mathrm{m}}=\dfrac{l}{\mu_0\mu_{\mathrm{r}}S}$ | resistance $R=\dfrac{l}{\sigma S}$ |
| permeability $\mu$ | conductivity $\sigma$ |

The reluctances of magnetic circuits in series add, and the permeances (reciprocals of reluctance) of magnetic circuits in parallel add. The reluctance of an air gap equals that of a core of length $\mu_{\mathrm{r}}\delta$: if $\mu_{\mathrm{r}}=10^3$, the reluctance of a $1\,\mathrm{mm}$ gap equals that of a $1\,\mathrm{m}$ length of core, so an air gap has a large effect on a magnetic circuit. Calculations for magnetic circuits are approximate: the $\mu$ of the core varies with $B$, so practical calculations must consult the magnetization curve, and some of the flux always leaks out of the core.

## Summary

| | Dielectrics | Magnetic materials |
|---|---|---|
| Microscopic origin | molecular electric dipole moment | molecular magnetic moment (orbital, spin, nuclear) |
| Description | polarization $\boldsymbol{P}$ | magnetization $\boldsymbol{M}$ |
| Bound sources | $\rho'=-\nabla\cdot\boldsymbol{P}$, $\sigma'=\boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}}$ | $\boldsymbol{J}'=\nabla\times\boldsymbol{M}$, $\boldsymbol{K}'=\boldsymbol{M}\times\boldsymbol{e}_{\mathrm{n}}$ |
| Auxiliary quantity | $\boldsymbol{D}=\varepsilon_0\boldsymbol{E}+\boldsymbol{P}$ | $\boldsymbol{H}=\boldsymbol{B}/\mu_0-\boldsymbol{M}$ |
| Law | $\oiint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S}=q_0$ | $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=I_0$ |
| Linear media | $\boldsymbol{P}=\varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E}$, $\boldsymbol{D}=\varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E}$ | $\boldsymbol{M}=\chi_{\mathrm{m}}\boldsymbol{H}$, $\boldsymbol{B}=\mu_0\mu_{\mathrm{r}}\boldsymbol{H}$ |
| Boundary conditions | $D_{1n}=D_{2n}$, $E_{1t}=E_{2t}$ | $B_{1n}=B_{2n}$, $H_{1t}=H_{2t}$ |
| Nonlinear | ferroelectrics | ferromagnetic substances (domains, hysteresis, Curie temperature) |

The correspondence in the table is formal: physically the fundamental field corresponding to $\boldsymbol{E}$ is $\boldsymbol{B}$ (both appear in the **Lorentz force**), and $\boldsymbol{D}$ and $\boldsymbol{H}$ are both auxiliary quantities. For a paramagnetic substance $\chi_{\mathrm{m}}>0$ and is inversely proportional to temperature; for a diamagnetic substance $\chi_{\mathrm{m}}<0$ and is almost independent of temperature.

## Questions

1. Why can a magnet attract a piece of iron that has not been magnetized?
   Hint: The iron is magnetized in the nonuniform field of the magnet; its moment is parallel to the field, and the force $\nabla(\boldsymbol{m}\cdot\boldsymbol{B})$ points toward the strong-field region.
2. The permeability of paramagnetic and ferromagnetic substances depends markedly on temperature, while that of diamagnetic substances is almost independent of temperature. Why?
   Hint: Paramagnetism and ferromagnetism are both orientational order of intrinsic moments, which thermal motion destroys; diamagnetism comes from the induced moment produced by Larmor precession and has nothing to do with the thermal motion of the molecules.
3. There is no conduction current in a short cylindrical permanent magnet magnetized uniformly along its axis, and the circulation theorem for $\boldsymbol{H}$ gives $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{l}=0$. Can one conclude that $\boldsymbol{H}=\boldsymbol{0}$?
   Hint: No. The circulation of $\boldsymbol{H}$ is zero, but its divergence $-\nabla\cdot\boldsymbol{M}$ is nonzero on the two end faces (equivalent to "magnetic charge"); $\boldsymbol{H}$ exists both inside and outside the magnet, and inside the magnet $\boldsymbol{H}$ is antiparallel to $\boldsymbol{M}$ (the demagnetizing field).
4. Why do magnetic domains exist inside a ferromagnet?
   Hint: See Section 8.5.1: dividing into domains lowers the magnetostatic energy, while the domain walls cost exchange energy, and the two compete.
5. Why is the core of a transformer made of a soft magnetic material, while permanent magnets are made of hard magnetic materials?
   Hint: A core is magnetized repeatedly, and the hysteresis loss is proportional to the area of the loop, so a soft magnetic material with a narrow loop is needed; a permanent magnet must retain a large remanence after the external field is removed and must resist demagnetization, so a hard magnetic material with large remanence and large coercivity is needed.
