---
title: Electrostatic Fields
description: Basic properties of electric charge, Coulomb's law, electric field strength and the superposition principle, fields of dipoles and continuous charge distributions, field lines and flux, solid angle and the proof of Gauss's law, and applications of Gauss's law to symmetric charge distributions.
source_hash: 1e4d9c9f3289
---

Electromagnetism studies how charges and currents produce electric and magnetic fields, how these fields act on charges and currents, how electric and magnetic fields convert into each other, and how electromagnetic fields interact with matter. Its viewpoint differs from that of mechanics and thermodynamics. Mechanics follows the motion of individual particles, and thermodynamics treats the random motion of huge numbers of particles statistically. The main actors of electromagnetism are fields: vectors $\boldsymbol{E}(\boldsymbol{r},t)$ and $\boldsymbol{B}(\boldsymbol{r},t)$ defined at every point of space and varying in time, with charged particles serving only as sources of the fields. A **vector field** has two basic global quantities, the **flux** through a surface and the **circulation** along a closed path, together with their local counterparts, the **divergence** and the **curl**; all of these were treated in [2.2.13](/2.2.13) and [2.2.14](/2.2.14). The fundamental laws of electromagnetism are written in terms of exactly these quantities. In this chapter Gauss's law gives the flux of the electrostatic field; the circulation theorem of the next chapter, [5.3.2](/5.3.2), gives its circulation. Together they determine the electrostatic field completely, and in [5.3.10](/5.3.10) they are generalized to Maxwell's equations.

This chapter treats the electric field produced by stationary charges in vacuum, the electrostatic field. We begin with the basic properties of charge and Coulomb's law, introduce the electric field strength and the superposition principle, and compute the fields of an electric dipole and of several continuous charge distributions. We then introduce field lines and electric flux, prove Gauss's law, and use it to find the fields of symmetric charge distributions. Chapters [5.3.3](/5.3.3) and [5.3.4](/5.3.4) treat the electrostatic field in conductors and in dielectrics.

## 1.1. Electric Charge

A body that has acquired the ability to attract light objects, for instance by rubbing, is said to be electrified. This property of matter is called *electric charge*, and the amount of charge is measured in the SI unit coulomb ($\mathrm{C}$). Charge has the following four basic properties.

### 1.1.1. Positive and Negative Charge

There are only two kinds of charge in nature: like charges repel and unlike charges attract (Du Fay, 1733). By Franklin's convention, the proton is positively charged and the electron negatively charged. A macroscopic body usually contains equal amounts of positive and negative charge and is electrically neutral; it becomes charged when this balance is upset, mostly by a transfer of electrons.

### 1.1.2. Charge Quantization

**Property 1.1.1 (Charge Quantization)** The charge of any body is an integer multiple of a basic unit:

$$
q = Ne,\qquad N=0,\pm1,\pm2,\dots
$$

The basic unit $e$ is the charge of the proton and is called the *elementary charge*; the electron has charge $-e$. Millikan's oil-drop experiment (from 1909) was the first to prove accurately that charge changes in discrete steps. Since 2019 the SI has defined the elementary charge to have the exact value

$$
e = 1.602\,176\,634\times10^{-19}\,\mathrm{C}.
$$

Quarks carry fractional charges $\pm\frac13e$ and $\pm\frac23e$, but they are confined inside hadrons, and no free quark has been observed. Because $e$ is so small, macroscopic charge can be treated as varying continuously, which justifies the introduction of charge density in §1.4.

### 1.1.3. Conservation of Charge

**Theorem 1.1.1 (Law of Conservation of Charge)** If no net charge crosses the boundary of a system, the algebraic sum of the positive and negative charges inside the system remains constant.

Conservation of charge is one of the most precisely verified conservation laws known, and it holds in all macroscopic and microscopic processes. Charge can be created and destroyed, but always in pairs: a high-energy photon near a nucleus converts into an electron–positron pair $\gamma\to\mathrm{e}^-+\mathrm{e}^+$, and when an electron and a positron meet they annihilate into photons; in both cases the algebraic sum of the charges is zero before and after. There is a stronger, local form of the law: the decrease of charge in a region equals the charge that flows out through its boundary in the same time, so charge cannot vanish in one place and simultaneously appear far away. The mathematical form of this statement is the continuity equation for current ([5.3.5](/5.3.5)).

### 1.1.4. Relativistic Invariance of Charge

The charge of a particle does not depend on its state of motion: observed from different reference frames, the same charge moves differently but has the same value. One piece of evidence is the electrical neutrality of atoms and molecules. The two protons in a helium nucleus have kinetic energies about $10^6$ times those of the two protons in a hydrogen molecule, yet both systems are exactly neutral, so the charge of a proton cannot depend on its speed. Invariance of charge is the starting point for deriving the magnetic field from the electric field by special relativity ([5.1.8](/5.1.8)), as done in [5.3.7](/5.3.7).

## 1.2. Coulomb's Law

**Theorem 1.2.1 (Coulomb's Law)** In vacuum, the force between two stationary point charges is proportional to the product of their charges and inversely proportional to the square of the distance between them. It points along the line joining them, repulsive for like charges and attractive for unlike charges. The force exerted by the point charge $q_1$ on $q_2$ is

$$
\boldsymbol{F}_{21}=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{21}^2}\,\boldsymbol{e}_{21}=-\boldsymbol{F}_{12},
$$
where $r_{21}$ is the distance between them and $\boldsymbol{e}_{21}$ is the unit vector pointing from $q_1$ to $q_2$.

A *point charge* is an idealized model of a charged body: when the dimensions of the body are much smaller than the distances under consideration, its shape and charge distribution can be ignored. The constant $\varepsilon_0$ is called the *vacuum permittivity* (also the electric constant),

$$
\varepsilon_0 = 8.854\,187\,8188(14)\times10^{-12}\,\mathrm{F\,m^{-1}},\qquad k=\frac{1}{4\pi\varepsilon_0}\approx8.988\times10^{9}\,\mathrm{N\,m^2\,C^{-2}}.
$$
Before 2019, $\varepsilon_0$ was an exact value derived from the defined value of $\mu_0$ and from $c$. In the current SI, $e$, $h$ and $c$ are exact, and $\varepsilon_0=e^2/(2\alpha hc)$ must be determined through measurements of the fine-structure constant $\alpha$, with a relative uncertainty of about $10^{-10}$. The advantage of writing $4\pi$ into Coulomb's law (called rationalization) is that $4\pi$ then appears only in formulas involving spherical symmetry and no longer in the more fundamental equations (Gauss's law, Maxwell's equations).

Coulomb obtained the law in 1785 with a torsion balance; Robison (1769) and Cavendish (1773, unpublished) had already reached the same conclusion. If the exponent of the distance is written as $2+\delta$, a Cavendish-type experiment tests whether there is an electric field inside a charged conducting shell (see [5.3.3](/5.3.3)), and modern experiments (Williams et al., 1971) found $\delta=0$ to a precision of about $10^{-16}$. The inverse-square law remains valid at atomic and nuclear scales.

Coulomb's law applies under two conditions: the charges are point charges, and the charge exerting the force is at rest relative to the observer (the charge experiencing the force may move). The force between moving charges also contains a magnetic part ([5.3.6](/5.3.6)) and no longer obeys **Newton's third law**; what is conserved is the total momentum of charges and electromagnetic field.

Experiment also shows that the force between two point charges is unaffected by the presence of a third charge. This is the principle of superposition of electric forces. Hence the net force of $n$ point charges $q_1,\dots,q_n$ on a point charge $q_0$ is the vector sum of the forces due to the individual charges:

$$
\boldsymbol{F}=\sum_{i=1}^n\frac{1}{4\pi\varepsilon_0}\frac{q_iq_0}{r_i^2}\,\boldsymbol{e}_{r_i}.
$$
Superposition is an experimental law; it expresses the linearity of the equations of electrostatics (the **superposition principle**), and Coulomb's law together with superposition describes electrostatic interactions completely.

**Example 1.2.1 (Electric Force Versus Gravitation)** Coulomb's law and Newton's law of gravitation are both inverse-square laws. In the hydrogen atom the ratio of the electric force to the gravitational force between the electron and the proton is

$$
\frac{F_{\mathrm{e}}}{F_{\mathrm{g}}}=\frac{e^2}{4\pi\varepsilon_0Gm_{\mathrm{e}}m_{\mathrm{p}}}\approx\frac{2.31\times10^{-28}\,\mathrm{J\,m}}{1.02\times10^{-67}\,\mathrm{J\,m}}\approx2.3\times10^{39},
$$
independent of the distance. The elastic forces and friction between atoms, molecules and macroscopic bodies all originate in the electromagnetic interaction ([5.1.2](/5.1.2)). Gravitation dominates astronomical bodies because the positive and negative charges of macroscopic bodies cancel almost exactly, whereas gravitation is always attractive.

## 1.3. The Electric Field and Electric Field Strength

### 1.3.1. The Electric Field

How is the Coulomb force transmitted across space? One view is action at a distance: two bodies separated by some distance act on each other directly and instantaneously, with no medium and no time delay. Faraday proposed another view: a charge excites an *electric field* in the surrounding space, and this field exerts a force on any other charge in it, a contact action of the form "charge, field, charge". For stationary charges the two views give the same result; when charges move or change, the disturbance propagates through the field at the speed of light $c$ ([5.3.10](/5.3.10)), and only the field view agrees with experiment. The same holds for gravitation: in 2015 LIGO directly detected gravitational waves traveling at the speed of light (Nobel Prize in Physics, 2017).

The field viewpoint has two implications. The first is locality: once the electric field in a small region is known, the force on a charge there is determined, regardless of where the charges producing the field are. The second is materiality: like ordinary matter, the electric field carries energy ([5.3.2](/5.3.2)) and momentum (radiation pressure, [5.3.10](/5.3.10)), although it is not made of atoms or molecules, and fields can be superposed, so several fields can occupy the same space at the same time.

### 1.3.2. Electric Field Strength

**Definition 1.3.1 (Electric Field Strength)** Let a stationary **test charge** $q_0$ experience an electric force $\boldsymbol{F}$ at some point of an electric field. The **electric field strength** (field strength for short) at that point is

$$
\boldsymbol{E}=\frac{\boldsymbol{F}}{q_0}.
$$
The test charge must be small enough not to disturb the original charge distribution, and its size must be small enough for it to represent a point.

The field strength at a point equals the force per unit positive charge at that point; it does not depend on the test charge and is a property of the field itself. Its SI unit is $\mathrm{N\,C^{-1}}$, also written $\mathrm{V\,m^{-1}}$ ([5.3.2](/5.3.2)). Conversely, a charge $q$ at a point where the field strength is $\boldsymbol{E}$ experiences the force $\boldsymbol{F}=q\boldsymbol{E}$. Some typical field strengths: the breakdown field of air is about $3\times10^6\,\mathrm{V\,m^{-1}}$, the atmospheric field at the ground in fair weather is about $10^2\,\mathrm{V\,m^{-1}}$, and the field at the electron in a hydrogen atom is about $5\times10^{11}\,\mathrm{V\,m^{-1}}$.

## 1.4. The Field of Point Charges and the Superposition Principle

### 1.4.1. Field of a Point Charge

From Coulomb's law and the definition of field strength, a stationary point charge $q$ (the source charge) produces at the field point $P$ the field strength

$$
\boldsymbol{E}=\frac{q}{4\pi\varepsilon_0r^2}\,\boldsymbol{e}_r,
$$
where $r$ is the distance from $q$ to $P$ and $\boldsymbol{e}_r$ is the unit vector from $q$ to $P$. The field of a point charge is spherically symmetric with magnitude inversely proportional to $r^2$; it points radially outward for $q>0$ and inward for $q<0$.

### 1.4.2. The Superposition Principle for Fields

**Property 1.4.1 (Superposition Principle of Electric Fields)** The field strength produced at a point by a system of point charges is the vector sum of the field strengths produced there by each point charge alone:

$$
\boldsymbol{E}=\sum_i\boldsymbol{E}_i=\sum_i\frac{q_i}{4\pi\varepsilon_0r_i^2}\,\boldsymbol{e}_{r_i}.
$$

It follows directly from the superposition of electric forces and the definition of field strength. For a continuous charge distribution, we divide the body into charge elements, and the sum becomes an integral.

**Definition 1.4.1 (Charge Density)** When charge is distributed continuously over a volume, a surface or a curve, we write the charge element as $\mathrm{d}q=\rho\,\mathrm{d}V$, $\mathrm{d}q=\sigma\,\mathrm{d}S$ or $\mathrm{d}q=\lambda\,\mathrm{d}l$; $\rho$, $\sigma$ and $\lambda$ are called the volume, surface and linear **charge density**, respectively. The field strength of the charged body at $P$ is

$$
\boldsymbol{E}=\int_q\mathrm{d}\boldsymbol{E}=\int_q\frac{\mathrm{d}q}{4\pi\varepsilon_0r^2}\,\boldsymbol{e}_r .
$$

This is a vector integral: we first resolve $\mathrm{d}\boldsymbol{E}$ into components, use symmetry to decide which components cancel, and then integrate the remaining ones. Surface and line charges are models in which the thickness of a charged layer or a charged thread tends to zero; on them the field strength jumps or diverges (§1.7).

### 1.4.3. The Electric Dipole

**Definition 1.4.2 (Electric Dipole)** A system consisting of a pair of equal and opposite point charges $+q$ and $-q$ placed close together is called an **electric dipole**. Let $\boldsymbol{l}$ be the position vector from $-q$ to $+q$. The quantity

$$
\boldsymbol{p}=q\boldsymbol{l}
$$
is called its **electric dipole moment**, with unit $\mathrm{C\,m}$. The concept is used for field points at distances $r\gg l$ from the dipole.

In a polar molecule (such as $\ce{H2O}$, with $p\approx6.2\times10^{-30}\,\mathrm{C\,m}$) the centers of positive and negative charge do not coincide, and from far away it looks like an electric dipole. Both the polarization of dielectrics ([5.3.4](/5.3.4)) and antenna radiation ([5.3.10](/5.3.10)) make use of it.

**Example 1.4.1 (Field on the Axis of a Dipole)** Take the midpoint of the dipole as the origin, and let the field point $P$ lie on the axis on the side of $+q$, at distance $r$ from the midpoint. Both fields point along the axis:

$$
\boldsymbol{E}=\frac{q\boldsymbol{e}_l}{4\pi\varepsilon_0}\Big[\frac{1}{(r-l/2)^2}-\frac{1}{(r+l/2)^2}\Big]=\frac{q\boldsymbol{e}_l}{4\pi\varepsilon_0}\frac{2rl}{(r^2-l^2/4)^2},
$$
where $\boldsymbol{e}_l=\boldsymbol{l}/l$. For $r\gg l$,

$$
\boldsymbol{E}\approx\frac{2\boldsymbol{p}}{4\pi\varepsilon_0r^3}.
$$

**Example 1.4.2 (Field on the Perpendicular Bisector of a Dipole)** Let the field point lie on the perpendicular bisector at distance $r$ from the midpoint. Each charge produces a field of magnitude $\frac{q}{4\pi\varepsilon_0(r^2+l^2/4)}$; the components perpendicular to the axis cancel and those along the axis add, pointing opposite to $\boldsymbol{p}$:

$$
\boldsymbol{E}=-\frac{\boldsymbol{p}}{4\pi\varepsilon_0(r^2+l^2/4)^{3/2}}\approx-\frac{\boldsymbol{p}}{4\pi\varepsilon_0r^3}\quad(r\gg l).
$$

For a field point in a general position, we resolve $\boldsymbol{p}$ into a component $p\cos\theta$ along $\boldsymbol{e}_r$ and a component $p\sin\theta$ perpendicular to $\boldsymbol{e}_r$ ($\theta$ is the angle between $\boldsymbol{r}$ and $\boldsymbol{p}$). The field point then lies on the axis of one of these "partial dipoles" and on the perpendicular bisector of the other, and superposing Examples 1.4.1 and 1.4.2 gives the following formula.

**Formula 1.4.1 (Field of an Electric Dipole)**

$$
\boldsymbol{E}=\frac{1}{4\pi\varepsilon_0r^3}\big[3(\boldsymbol{p}\cdot\boldsymbol{e}_r)\boldsymbol{e}_r-\boldsymbol{p}\big],\qquad E_r=\frac{2p\cos\theta}{4\pi\varepsilon_0r^3},\quad E_\theta=\frac{p\sin\theta}{4\pi\varepsilon_0r^3}\qquad(r\gg l).
$$

The field of a dipole is inversely proportional to $r^3$ and decays faster than that of a point charge, because from far away the fields of $+q$ and $-q$ almost cancel. The field depends on $q$ and $l$ only through the product $p=ql$, so the dipole moment is the only parameter that characterizes an electric dipole. In [5.3.2](/5.3.2), Formula 1.4.1 will be derived more simply from the potential.

**Example 1.4.3 (Torque on a Dipole in a Uniform External Field)** Place an electric dipole in a uniform electric field $\boldsymbol{E}$. The charges $+q$ and $-q$ experience forces $\pm q\boldsymbol{E}$; the net force is zero, but the forces form a couple. With the midpoint as reference point and $\boldsymbol{r}_\pm=\pm\boldsymbol{l}/2$, the torque is

$$
\boldsymbol{M}=\boldsymbol{r}_+\times q\boldsymbol{E}+\boldsymbol{r}_-\times(-q\boldsymbol{E})=q\boldsymbol{l}\times\boldsymbol{E}=\boldsymbol{p}\times\boldsymbol{E},\qquad M=pE\sin\theta .
$$
The torque turns $\boldsymbol{p}$ toward the direction of the external field; the equilibrium with $\boldsymbol{p}$ parallel to $\boldsymbol{E}$ is stable. In a nonuniform field the dipole experiences, besides the torque, a net force $\boldsymbol{F}=(\boldsymbol{p}\cdot\nabla)\boldsymbol{E}$ that pulls it toward the region of larger field strength. This is why a charged body attracts light objects: the light object is polarized into an electric dipole and then attracted by the nonuniform field.

### 1.4.4. The Far Field of an Arbitrary Charge System

When the distance $r$ from the field point to a charge system is much larger than the size of the system, choose any point $O$ inside the system as the origin. The leading parts of the field are, in order:

- If the total charge $Q=\sum q_i\ne0$, the field is approximately that of a point charge $Q$ at $O$, $E\propto r^{-2}$.
- If $Q=0$ but the dipole moment $\boldsymbol{p}=\sum q_i\boldsymbol{r}_i\ne\boldsymbol{0}$ (in which case $\boldsymbol{p}$ does not depend on the choice of origin), the field is dominated by that of an electric dipole, $E\propto r^{-3}$.
- If $\boldsymbol{p}$ also vanishes, we look next at the quadrupole moment, $E\propto r^{-4}$, and so on.

This is the multipole expansion. Its mathematical basis is $\frac{1}{\lvert\boldsymbol{r}-\boldsymbol{r}'\rvert}=\sum_{l\ge0}\frac{r'^l}{r^{l+1}}P_l(\cos\gamma)$ ($r'<r$, where $\gamma$ is the angle between $\boldsymbol{r}$ and $\boldsymbol{r}'$), whose coefficients are exactly the **Legendre polynomials** $P_l$ ([2.5.5](/2.5.5)).

### 1.4.5. Fields of Continuous Charge Distributions

**Example 1.4.4 (Field on the Axis of a Uniformly Charged Annulus)** An annulus (inner radius $R_1$, outer radius $R_2$) is uniformly charged with surface charge density $\sigma$. Find the field strength on the axis at distance $x$ from the center.

Take a charge element $\mathrm{d}q=\sigma r_\perp\,\mathrm{d}r_\perp\,\mathrm{d}\phi$ at radius $r_\perp$, of width $\mathrm{d}r_\perp$ and angular width $\mathrm{d}\phi$. By symmetry, the components of the elements' fields perpendicular to the axis cancel in pairs, leaving only the component along the axis (the $x$ direction), $\mathrm{d}E_x=\frac{\mathrm{d}q}{4\pi\varepsilon_0r^2}\cos\theta$, where $r^2=x^2+r_\perp^2$ and $\cos\theta=x/r$. Hence

$$
E_x=\int_0^{2\pi}\!\!\int_{R_1}^{R_2}\frac{\sigma x\,r_\perp\,\mathrm{d}r_\perp\,\mathrm{d}\phi}{4\pi\varepsilon_0(x^2+r_\perp^2)^{3/2}}=\frac{\sigma x}{2\varepsilon_0}\Big[\frac{1}{\sqrt{x^2+R_1^2}}-\frac{1}{\sqrt{x^2+R_2^2}}\Big].
$$

Checks: the dimensions are correct; $E=0$ at $x=0$, as symmetry requires; and for $\lvert x\rvert\gg R_2$, using $\frac{1}{\sqrt{x^2+R^2}}\approx\frac{1}{\lvert x\rvert}\big(1-\frac{R^2}{2x^2}\big)$, we get

$$
E_x\approx\frac{\sigma(R_2^2-R_1^2)}{4\varepsilon_0x^2}\cdot\frac{x}{\lvert x\rvert}=\frac{q}{4\pi\varepsilon_0x^2}\cdot\frac{x}{\lvert x\rvert},\qquad q=\sigma\pi(R_2^2-R_1^2),
$$
so from far away the annulus looks like a point charge. Two special cases:

1. A uniformly charged disk ($R_1\to0$, $R_2=R$): $E_x=\dfrac{\sigma}{2\varepsilon_0}\Big[\dfrac{x}{\lvert x\rvert}-\dfrac{x}{\sqrt{x^2+R^2}}\Big]$. As $x\to0^\pm$ on the two sides of the disk, $E_x\to\pm\frac{\sigma}{2\varepsilon_0}$, a jump of $\sigma/\varepsilon_0$.
2. An infinite uniformly charged plane ($R_1\to0$, $R_2\to\infty$):

$$
\boldsymbol{E}=\frac{\sigma}{2\varepsilon_0}\,\boldsymbol{e}_{\mathrm{n}},
$$
which has the same magnitude everywhere, points perpendicular to the plane, and is opposite on the two sides ($\boldsymbol{e}_{\mathrm{n}}$ is the unit normal pointing from the plane toward the side of the field point). In §1.7 this result will be obtained more simply from Gauss's law.

## 1.5. Electric Field Lines and Electric Flux

### 1.5.1. Electric Field Lines

**Definition 1.5.1 (Electric Field Line)** In an electric field, draw a family of directed curves such that the tangent at every point gives the direction of the field strength there and the density of the curves represents its magnitude: the number of curves crossing a unit area perpendicular to the field equals the field strength at that place,

$$
E=\frac{\mathrm{d}N}{\mathrm{d}S_\perp}.
$$
These curves are called **electric field lines**.

Field lines are a geometric tool for describing a field, not physically existing lines (they are the integral curves of a **vector field**). Field lines of an electrostatic field have the following properties: they start on positive charges (or at infinity) and end on negative charges (or at infinity), and are not interrupted where there is no charge; no two field lines intersect, because the field has only one direction at each point; and they do not close on themselves (proved in [5.3.2](/5.3.2)). Field lines are in general not the trajectories of charged particles either: the electric force determines the direction of the acceleration, not of the velocity, and the two coincide only in special cases, such as straight field lines and particles released from rest.

![Electric field lines. Left: an electric dipole, with field lines leaving the positive charge and ending on the negative charge. Right: two equal positive charges, with all field lines extending to infinity; the field vanishes at the midpoint of the line joining the charges, where the field lines separate](./plots/field-lines.py)

### 1.5.2. Electric Flux

**Definition 1.5.2 (Electric Flux)** The number of field lines passing through a surface $S$ is called the **electric flux** through that surface:

$$
\Phi_{\mathrm{e}}=\iint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S},\qquad\mathrm{d}\Phi_{\mathrm{e}}=\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=E\cos\theta\,\mathrm{d}S=E\,\mathrm{d}S_\perp=\mathrm{d}N,
$$
where $\mathrm{d}\boldsymbol{S}=\boldsymbol{e}_{\mathrm{n}}\,\mathrm{d}S$ is the oriented area element and $\theta$ is the angle between $\boldsymbol{E}$ and the normal of the element. For a closed surface the outward normal is taken as positive, and we write $\Phi_{\mathrm{e}}=\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}$.

Electric flux is the **flux** of the electric field, mathematically a **flux integral** ([2.2.13](/2.2.13)). It refers to a surface, not to a point; it is an algebraic quantity that can be positive or negative. For a closed surface, $\Phi_{\mathrm{e}}>0$ means a net outflow of field lines and $\Phi_{\mathrm{e}}<0$ a net inflow.

## 1.6. Gauss's Law

### 1.6.1. Solid Angle

**Definition 1.6.1 (Solid Angle)** Let $\mathrm{d}\boldsymbol{S}$ be an oriented area element at distance $r$ from a point $O$ (with dimensions much smaller than $r$), and let $\boldsymbol{e}_r$ be the unit vector from $O$ toward the element. The **solid angle** subtended by the element at $O$ is

$$
\mathrm{d}\Omega=\frac{\mathrm{d}\boldsymbol{S}\cdot\boldsymbol{e}_r}{r^2}=\frac{\mathrm{d}S\cos\theta}{r^2}=\frac{\mathrm{d}S_\perp}{r^2},
$$
that is, the area of the projection of the element onto the unit sphere centered at $O$. Its unit is the steradian ($\mathrm{sr}$), and it is dimensionless.

The solid angle is the three-dimensional generalization of the plane angle. By definition, $\mathrm{d}\Omega$ depends only on the "apparent area" of the element as seen from $O$, not on its distance or tilt; it also carries a sign. For a closed surface $S$ (outward normal positive):

- If $O$ lies inside $S$, the elements of $S$ correspond one-to-one along rays from $O$ to the elements of a small sphere $S_0$ (radius $r_0$) centered at $O$, with the same $\mathrm{d}\Omega$, so $\Omega=\oiint_S\frac{\mathrm{d}\boldsymbol{S}\cdot\boldsymbol{e}_r}{r^2}=\frac{1}{r_0^2}\oiint_{S_0}\mathrm{d}S_0=4\pi$.
- If $O$ lies outside $S$, every small cone from $O$ meets $S$ an even number of times, alternately entering and leaving, and the two values of $\mathrm{d}\Omega$ have equal magnitude and opposite sign, so $\Omega=0$.

These two statements are the geometric interpretation of the result in [Example 14.2.6](/2.2.14#ex-14.2.6) that the flux of $\boldsymbol{e}_r/r^2$ through a closed surface is $4\pi$ or $0$.

### 1.6.2. Gauss's Law

**Theorem 1.6.1 (Gauss's Law)** In an electrostatic field, the electric flux through any closed surface $S$ equals the algebraic sum of the charges enclosed by the surface divided by $\varepsilon_0$:

$$
\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\frac{q_{\mathrm{enc}}}{\varepsilon_0}=\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V,
$$
where $V$ is the region enclosed by $S$. The closed surface $S$ is often called a Gaussian surface.

**Proof** We proceed in four steps.

1. A point charge $q$ and a sphere $S_0$ centered on $q$: the field strength is everywhere along the outward normal and has the same magnitude, so $\Phi_{\mathrm{e}}=\frac{q}{4\pi\varepsilon_0r^2}\cdot4\pi r^2=\frac{q}{\varepsilon_0}$, independent of the radius $r$. This means that the field lines of a point charge are continuous in space.
2. A point charge $q$ and an arbitrary closed surface $S$: $\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\frac{q}{4\pi\varepsilon_0}\frac{\boldsymbol{e}_r\cdot\mathrm{d}\boldsymbol{S}}{r^2}=\frac{q}{4\pi\varepsilon_0}\mathrm{d}\Omega$, so by the result on solid angles $\Phi_{\mathrm{e}}=q/\varepsilon_0$ ($q$ inside $S$) or $0$ ($q$ outside $S$).
3. A system of point charges: by the superposition principle, $\Phi_{\mathrm{e}}=\sum_i\oiint_S\boldsymbol{E}_i\cdot\mathrm{d}\boldsymbol{S}$. Charges outside $S$ contribute zero and each charge inside contributes $q_i/\varepsilon_0$, so $\Phi_{\mathrm{e}}=\sum_{\text{inside}}q_i/\varepsilon_0=q_{\mathrm{enc}}/\varepsilon_0$.
4. A continuous distribution: divide the body into charge elements; the sum in step 3 becomes the integral $\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V$. $\square$

**Theorem 1.6.2 (Differential Form of Gauss's Law)** Wherever the charge density $\rho$ is continuous,

$$
\nabla\cdot\boldsymbol{E}=\frac{\rho}{\varepsilon_0}.
$$

**Proof** By the **divergence theorem** ([Theorem 14.2.1](/2.2.14#thm-14.2.1)), $\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=\iiint_V\nabla\cdot\boldsymbol{E}\,\mathrm{d}V$. This equals $\frac{1}{\varepsilon_0}\iiint_V\rho\,\mathrm{d}V$ for every region $V$, and the integrands are continuous, so they are equal everywhere. $\square$

Here $\nabla$ is the **nabla operator**. By the interpretation in [Theorem 14.2.2](/2.2.14#thm-14.2.2), the **divergence** is the outward flux per unit volume, so the differential form says that the sources of the electrostatic field are the points where the charge density is nonzero. For a point charge, $\nabla\cdot\frac{\boldsymbol{e}_r}{r^2}=4\pi\delta(\boldsymbol{r})$; that is, the charge density of a point charge is the **Dirac delta function** $q\,\delta(\boldsymbol{r})$.

Some remarks on Gauss's law:

- Gauss's law is a necessary consequence of the inverse-square law (together with superposition): step 1 of the proof uses the fact that the field strength is inversely proportional to $r^2$. If the exponent in Coulomb's law were not 2, the flux in step 1 would depend on $r$ and the theorem would fail. Gravitation is also an inverse-square law, so the gravitational field obeys a Gauss law of the same form ([Example 14.5.1](/2.2.14#ex-14.5.1)).
- The flux is determined only by the algebraic sum of the charges inside the Gaussian surface; it does not depend on how the charge inside is distributed, nor on charges outside. The $\boldsymbol{E}$ in the formula, however, is the total field of all charges, inside and outside.
- A Gaussian surface is a geometric surface, so charges inside and outside it can always be told apart; if charge lies exactly on the surface, the surface should be shifted slightly.
- Gauss's law also holds for moving charges and time-varying electric fields and is one of Maxwell's equations ([5.3.10](/5.3.10)), whereas Coulomb's law holds only for stationary charges. In this sense Gauss's law is derived from Coulomb's law but is more general.

Gauss's law shows that the electrostatic field has sources: charges are the sources of the field, and field lines begin on positive charges and end on negative charges. In a region with field but no charge, $\nabla\cdot\boldsymbol{E}=0$ and the field lines are continuous. Gauss's law gives only half of the properties of the electrostatic field; the other half, that its field lines do not close, is the circulation theorem of [5.3.2](/5.3.2).

## 1.7. Applications of Gauss's Law

When the charge distribution has enough symmetry, we can choose a suitable Gaussian surface so that $\boldsymbol{E}$ comes out of the integral and the field strength follows directly from Gauss's law. There are three common types of symmetry:

| Symmetry | Charged body | Gaussian surface |
|---|---|---|
| Spherical | Uniformly charged ball, spherical shell, spherical surface (point charge) | Concentric sphere |
| Cylindrical | Infinitely long uniformly charged cylinder, cylindrical surface, line | Coaxial cylinder |
| Planar | Infinite uniformly charged slab, plane | Cylinder perpendicular to the plane |

**Example 1.7.1 (Uniformly Charged Spherical Shell)** A spherical shell with inner radius $R_1$ and outer radius $R_2$ is uniformly charged with volume charge density $\rho$ and total charge $q=\frac{4\pi}{3}\rho(R_2^3-R_1^3)$. Find the field strength everywhere.

First we analyze the symmetry. For any field point $P$, charge elements can be chosen in pairs symmetric about the line $OP$, and their fields add up along $OP$; since the charge distribution is invariant under arbitrary rotations about the center, $\boldsymbol{E}=E(r)\boldsymbol{e}_r$. Take the concentric sphere of radius $r$ as the Gaussian surface: $\oiint_S\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=4\pi r^2E(r)=q_{\mathrm{enc}}/\varepsilon_0$, so

$$
E(r)=\frac{q_{\mathrm{enc}}}{4\pi\varepsilon_0r^2}=\begin{cases}0,&r<R_1,\\[1mm]\dfrac{\rho}{3\varepsilon_0}\Big(r-\dfrac{R_1^3}{r^2}\Big),&R_1<r<R_2,\\[3mm]\dfrac{q}{4\pi\varepsilon_0r^2},&r>R_2.\end{cases}
$$
Outside the shell the field is the same as that of a point charge at the center carrying all the charge; the field in the cavity is zero. Two special cases:

1. A uniformly charged ball ($R_1=0$, total charge $Q$, radius $R$): inside, $\boldsymbol{E}=\dfrac{\rho\boldsymbol{r}}{3\varepsilon_0}=\dfrac{Q\boldsymbol{r}}{4\pi\varepsilon_0R^3}$, proportional to $r$; outside, the field is that of a point charge.
2. A uniformly charged spherical surface ($R_1=R_2=R$ with $q$ fixed): $E=0$ inside and the field is that of a point charge outside. At $r=R$ the field strength jumps from $0$ to $\frac{q}{4\pi\varepsilon_0R^2}=\frac{\sigma}{\varepsilon_0}$; the jump results from neglecting the thickness of the charge layer. In general, across a charged surface of surface charge density $\sigma$, the normal component of the field strength jumps by $\sigma/\varepsilon_0$ (apply Gauss's law to a flat cylindrical Gaussian surface straddling the charged surface).

![Field strength E(r) of a uniformly charged ball, shell and spherical surface (same total charge Q, same outer radius R₂). Outside, all three coincide with the field of a point charge Q at the center (dashed line); inside the ball E is proportional to r, and for the spherical surface it jumps at r = R₂](./plots/sphere-fields.py)

**Example 1.7.2 (Infinitely Long Uniformly Charged Line)** The linear charge density is $\lambda$. By axial symmetry, $\boldsymbol{E}=E(r)\boldsymbol{e}_r$, with $\boldsymbol{e}_r$ perpendicular to the line and pointing outward. Take a coaxial cylinder of radius $r$ and length $l$ as the Gaussian surface. On the two end faces $\boldsymbol{E}\perp\mathrm{d}\boldsymbol{S}$, so the flux vanishes; on the lateral surface $\boldsymbol{E}$ is parallel to $\mathrm{d}\boldsymbol{S}$ and of constant magnitude, giving flux $E\cdot2\pi rl$. By Gauss's law $E\cdot2\pi rl=\lambda l/\varepsilon_0$, so

$$
\boldsymbol{E}=\frac{\lambda}{2\pi\varepsilon_0r}\,\boldsymbol{e}_r .
$$
The field strength is inversely proportional to $r$. As $r\to0$, $E\to\infty$, which shows that very close to the wire the geometric model of a charged line fails and the thickness of the wire must be taken into account.

**Example 1.7.3 (Infinite Uniformly Charged Plane)** The surface charge density is $\sigma$. By planar symmetry the field is perpendicular to the plane, with equal magnitude and opposite direction at symmetric points on the two sides. Take as the Gaussian surface a cylinder whose axis is perpendicular to the plane and whose two end faces (area $\Delta S$) lie symmetrically on both sides of the plane. The lateral flux vanishes, so $2E\Delta S=\sigma\Delta S/\varepsilon_0$ and $E=\frac{\sigma}{2\varepsilon_0}$, in agreement with Example 1.4.4. For two parallel infinite planes carrying $+\sigma$ and $-\sigma$, the superposition principle gives $E=\frac{\sigma}{2\varepsilon_0}+\frac{\sigma}{2\varepsilon_0}=\frac{\sigma}{\varepsilon_0}$ between the planes, directed from the positive to the negative plane, and zero outside. This is exactly the field of a parallel-plate capacitor ([5.3.4](/5.3.4)).

Procedure for finding a field with Gauss's law:

1. Analyze the symmetry of the charge distribution to determine the direction of the field and the coordinate it depends on.
2. Choose a Gaussian surface: the field point must lie on it; on the part where the field is to be found, $\boldsymbol{E}$ must be parallel to $\mathrm{d}\boldsymbol{S}$ and of constant magnitude, so that $\oiint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}=E\oiint\mathrm{d}S$; on the remaining parts, $\boldsymbol{E}=\boldsymbol{0}$ or $\boldsymbol{E}\perp\mathrm{d}\boldsymbol{S}$.
3. Obtain the field distribution from Gauss's law.
4. When the symmetry is insufficient (a finite charged line, a charged disk), Gauss's law still holds but cannot by itself determine the field, and we must return to the superposition principle.

## Questions

1. Why does the far field of an electric dipole not obey the inverse-square law?
   Hint: the fields of $+q$ and $-q$ almost cancel at large distances, and what remains is their difference, which amounts to a derivative of the point-charge field and so carries an extra factor $1/r$ (§1.4.4).
2. Can electric field lines intersect? Can they be tangent to each other?
   Hint: neither (except at points where the field vanishes). Intersection or tangency would mean that the field has two directions at the common point.
3. Why can the field lines of an electrostatic field not close?
   Hint: for a closed field line the circulation $\oint\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}>0$ along it, contradicting the circulation theorem of the electrostatic field ([5.3.2](/5.3.2)).
4. What is the relation between Gauss's law and Coulomb's law?
   Hint: for stationary charges, Gauss's law follows from Coulomb's law and superposition; conversely, Gauss's law together with the spherical symmetry of the field of a point charge gives Coulomb's law. But Gauss's law also holds for moving charges, for which Coulomb's law fails.
5. Two large parallel plates a distance $d$ apart, each of area $S$, carry charges $+q$ and $-q$. One person says that by Coulomb's law the force between the plates is $\frac{q^2}{4\pi\varepsilon_0d^2}$; another says the field between the plates is $\frac{q}{\varepsilon_0S}$ and hence the force is $\frac{q^2}{\varepsilon_0S}$; a third says the field of one plate at the other is $\frac{q}{2\varepsilon_0S}$ and hence the force is $\frac{q^2}{2\varepsilon_0S}$. Which is right?
   Hint: the third. The plates cannot be treated as point charges ($d\ll\sqrt S$), so the first is wrong; the field $\frac{q}{\varepsilon_0S}$ between the plates includes the field of the plate being acted on, and the field of a charged body exerts no net force on itself, so the second is wrong.
6. A circular hole of radius $R$ is cut out of an infinite uniformly charged plane of surface charge density $\sigma$. Find the field on the axis of the hole.
   Hint: in Example 1.4.4 set $R_1=R$ and $R_2\to\infty$ to get $E_x=\dfrac{\sigma x}{2\varepsilon_0\sqrt{x^2+R^2}}$; alternatively, take the field of the infinite plane minus that of a disk of radius $R$.
