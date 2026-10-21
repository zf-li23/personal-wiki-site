---
title: Conductors in Electrostatic Fields
description: Conditions for electrostatic equilibrium of a conductor, charge distribution and surface field at equilibrium, point discharge, computing electrostatic fields in the presence of conductors, conducting shells and electrostatic shielding, the uniqueness theorem of electrostatics and numerical solution of Laplace's equation, and the method of images (grounded plane and grounded sphere).
source_hash: 15fb796bc521
---

The previous two chapters treated electrostatic fields of given charge distributions in vacuum. Real electric fields always involve matter, which can be classified by its electrical behavior. A conductor contains a large number of charges that are free to move (free electrons in metals, ions in electrolytes); an insulator (dielectric) has almost no freely moving charges; a semiconductor lies between the two; a superconductor has zero resistance and also expels magnetic fields. There are also plasmas, with equal densities of positive and negative charged particles. This chapter treats an isotropic, homogeneous metallic conductor placed in an electrostatic field: the free charges redistribute under the electric force until the field inside the conductor vanishes. The charge distribution on the surface in turn changes the external field; it is not known in advance and has to be determined from the condition that the conductor is an equipotential body. Mathematically this is a **boundary value problem** for Laplace's equation ([2.5.8](/2.5.8)): the uniqueness theorem of §3.5 guarantees that the solution is unique once suitable boundary conditions are given, and the **method of images** of §3.6 exploits this to construct closed-form solutions for special geometries. Dielectrics are left to [5.3.4](/5.3.4); the band-theory explanation of conductors, semiconductors and insulators is in [5.5.6](/5.5.6), and superconductivity in [5.3.9](/5.3.9). Section 3.5 is optional.

## 3.1. Conditions for the Electrostatic Equilibrium of a Conductor

**Definition 3.1.1 (Conductor)** A body containing a large number of freely moving charges is called a **conductor**.

When a metallic conductor is placed in an electric field, the free electrons move in an organized way under the electric force and change the charge distribution on the conductor; the changed charge distribution in turn changes the field. This process continues until the field inside the conductor vanishes everywhere.

**Definition 3.1.2 (Electrostatic Equilibrium)** The state in which there is no macroscopic directed motion of charge inside or on the surface of a conductor and the charge distribution does not change with time is called the **electrostatic equilibrium** of the conductor.

Equilibrium is reached extremely quickly. For a good conductor the charge **relaxation time** is much less than $1\,\mathrm{ns}$ (the estimate from the conductivity is $\varepsilon_0/\sigma\sim10^{-19}\,\mathrm{s}$, but in practice it is limited by the electron collision time, about $10^{-14}\,\mathrm{s}$), so in electrostatic problems conductors can always be taken to be in electrostatic equilibrium.

**Theorem 3.1.1 (Conditions for Electrostatic Equilibrium)** A conductor in electrostatic equilibrium satisfies:

1. the field strength inside the conductor is zero everywhere, $\boldsymbol{E}_{\mathrm{in}}=\boldsymbol{0}$;
2. the field strength near the surface is everywhere perpendicular to the surface.

Equivalently, the conductor is an equipotential body and its surface is an **equipotential surface**.

**Proof** If $\boldsymbol{E}\ne\boldsymbol{0}$ somewhere inside, the free charges there would move in an organized way; if the field at the surface had a tangential component, the surface charges would move along the surface. Both contradict equilibrium. The **potential difference** between any two points in the conductor is $\int\boldsymbol{E}_{\mathrm{in}}\cdot\mathrm{d}\boldsymbol{l}=0$, so the conductor is an equipotential body; along any tangent direction on the surface $\mathrm{d}\varphi=-\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}=0$, so the surface is an equipotential surface, consistent with the field being perpendicular to equipotential surfaces ([Property 2.3.2](/5.3.2#pty-2.3.2)). $\square$

The equilibrium conditions follow from the structural feature that a conductor has free charges, together with the requirement of equilibrium, and are independent of the shape of the conductor.

## 3.2. Charge Distribution on a Conductor in Equilibrium

**Property 3.2.1** In electrostatic equilibrium, the net charge is zero everywhere inside the conductor, and any charge carried by the conductor can only be distributed on its surface.

**Proof** Take any closed surface $S$ inside the conductor. On it $\boldsymbol{E}_{\mathrm{in}}=\boldsymbol{0}$, so by **Gauss's law** $\iiint_V\rho\,\mathrm{d}V=\varepsilon_0\oiint_S\boldsymbol{E}_{\mathrm{in}}\cdot\mathrm{d}\boldsymbol{S}=0$. Since $S$ can be arbitrarily small, $\rho=0$ everywhere inside the conductor. The same follows directly from the differential form $\rho=\varepsilon_0\nabla\cdot\boldsymbol{E}_{\mathrm{in}}=0$. $\square$

**Property 3.2.2 (Field at the Surface of a Conductor)** Let the surface **charge density** at some point of the conductor surface be $\sigma$, and let $\boldsymbol{e}_{\mathrm{n}}$ be the unit normal there pointing from the inside to the outside of the conductor. Then the field strength just outside the surface is

$$
\boldsymbol{E}=\frac{\sigma}{\varepsilon_0}\,\boldsymbol{e}_{\mathrm{n}}.
$$

**Proof** Take as the Gaussian surface a small flat cylinder straddling the conductor surface, with two end faces of area $\Delta S$ parallel to the surface. On the end face inside the conductor $\boldsymbol{E}=\boldsymbol{0}$; the height of the lateral surface tends to zero, so its flux tends to zero; on the outer end face the field is perpendicular to the surface and the flux is $E_{\mathrm{n}}\Delta S$. By **Gauss's law**, $E_{\mathrm{n}}\Delta S=\sigma\Delta S/\varepsilon_0$. $\square$

Note that $\boldsymbol{E}$ here is the field produced jointly by all charges (the charges everywhere on the conductor and the charges outside it), not only by the charge inside the flat cylinder. The charge on the small surface element itself produces a field $\frac{\sigma}{2\varepsilon_0}$ on each side ([Example 1.7.3](/5.3.1#ex-1.7.3)), and the remaining charges produce $\frac{\sigma}{2\varepsilon_0}\boldsymbol{e}_{\mathrm{n}}$ there; the two cancel inside the conductor and add outside. The force on the element is therefore due to the field of the remaining charges, and the force per unit area (the electrostatic pressure) is

$$
\frac{\boldsymbol{F}}{\Delta S}=\sigma\cdot\frac{\sigma}{2\varepsilon_0}\boldsymbol{e}_{\mathrm{n}}=\frac{\sigma^2}{2\varepsilon_0}\boldsymbol{e}_{\mathrm{n}}=\frac12\varepsilon_0E^2\,\boldsymbol{e}_{\mathrm{n}},
$$
which points out of the conductor regardless of the sign of $\sigma$, and whose magnitude equals the **energy density of the electric field** at the surface ([Formula 2.7.1](/5.3.2#fml-2.7.1)).

The surface charge density on an isolated charged conductor depends on the shape of the surface: it is large where the surface is protruding and sharp (large positive curvature), smaller where it is flatter, and smallest in recesses. This is required by the equipotential condition. Model the conductor by two conducting spheres of radii $a>b$ and charges $Q$, $q$, far apart and joined by a thin wire. The spheres have the same potential, $\frac{Q}{4\pi\varepsilon_0a}=\frac{q}{4\pi\varepsilon_0b}$, so

$$
\frac{\sigma_a}{\sigma_b}=\frac{Q/(4\pi a^2)}{q/(4\pi b^2)}=\frac{b}{a},
$$
and the surface charge density is inversely proportional to the radius: the field at the surface of the smaller sphere (larger curvature) is stronger. For conductors of general shape there is no simple quantitative relation between $\sigma$ and curvature, but this trend always holds.

The field near the tip of a charged conductor is very strong and can ionize the nearby air (the breakdown field of air is about $3\times10^6\,\mathrm{V\,m^{-1}}$). Of the ions produced, those with sign opposite to the tip are drawn toward it and neutralize its charge, while those with the same sign are repelled, forming an "electric wind". This phenomenon is called *point discharge*. Its applications and the protective measures against it include:

- Lightning rod (air terminal): its purpose is not to "avert lightning" but to attract the lightning stroke to itself with its tip and then conduct the charge into the ground through a grounding wire, sparing the building;
- Electrostatic precipitation: dust particles are charged in the point-discharge region and then collected on electrodes;
- Static dischargers on the trailing edges of aircraft wings: they gradually release the charge accumulated by friction in flight into the air;
- Electrodes of high-voltage equipment and joints of transmission lines are made as smooth spheres to reduce the energy loss caused by point discharge (corona discharge).

The Van de Graaff generator uses another result: the inner surface of a conducting shell carries no charge (§3.4). A belt carries charge into the metal shell and, on contact with the inner surface, all of it moves to the outer surface, so charge can be delivered to the shell continuously until the field at the outer surface reaches the breakdown field of air, and voltages of several million volts can be reached.

## 3.3. Analysis and Computation of Electrostatic Fields with Conductors

To find the electrostatic field in the presence of conductors we use:

- the basic laws of the electrostatic field: the **superposition principle of electric fields**, Gauss's law and the circulation theorem;
- the **law of conservation of charge**: the total charge of an isolated conductor is constant;
- the equilibrium conditions: $\boldsymbol{E}=\boldsymbol{0}$ inside the conductor, or the conductor is an equipotential body.

The basic idea is to find the surface charge distribution on the conductor such that the total field produced by all charges vanishes at every point inside the conductor.

**Example 3.3.1 (Conducting Slab Near a Charged Plane)** An uncharged infinite conducting slab is placed parallel to an infinite uniformly charged plane of surface charge density $\sigma_0$. Find the surface charge densities $\sigma_1$ (on the side near the charged plane) and $\sigma_2$ of the two surfaces of the slab.

By symmetry the induced charges are uniformly distributed on the two surfaces, each of which is an infinite charged plane. The **law of conservation of charge** gives $\sigma_1+\sigma_2=0$. At any point inside the conductor the fields of the three charged surfaces (positive when pointing from the charged plane toward the slab) sum to zero:

$$
\frac{\sigma_0}{2\varepsilon_0}+\frac{\sigma_1}{2\varepsilon_0}-\frac{\sigma_2}{2\varepsilon_0}=0 .
$$
Solving the two equations gives $\sigma_1=-\frac{\sigma_0}{2}$, $\sigma_2=\frac{\sigma_0}{2}$. The field between the charged plane and the slab is $\frac{\sigma_0}{2\varepsilon_0}$ (by Property 3.2.2, $\lvert\sigma_1\rvert/\varepsilon_0$), and the field outside the slab is $\sigma_2/\varepsilon_0=\frac{\sigma_0}{2\varepsilon_0}$, both the same as without the slab: the fields of the two induced charge layers, equal and opposite, cancel outside the conductor.

If the slab is grounded, we obtain a different equilibrium state: the slab has the same potential as the earth (far away), there is no field on the outer side of the slab, and $\sigma_2=0$. Conservation of charge no longer applies (charge can flow through the ground wire), and the condition that the field inside the conductor vanish gives $\sigma_1=-\sigma_0$. The field between the charged plane and the slab is then $\frac{\sigma_0}{\varepsilon_0}$, and zero outside the slab.

## 3.4. Conducting Shells and Electrostatic Shielding

A closed conducting shell has an inner surface $S_{\mathrm{in}}$ and an outer surface $S_{\mathrm{out}}$, which divide space into the cavity and the exterior.

### 3.4.1. No Charge in the Cavity

**Theorem 3.4.1** If there is no charge in the cavity of a conducting shell, then regardless of whether the shell itself is charged and whether there are charges outside, in electrostatic equilibrium the field in the cavity is zero everywhere and the inner surface of the cavity carries no charge anywhere.

**Proof** Take a closed surface $S$ in the conductor enclosing the cavity. The field on it is zero, so by Gauss's law the total charge inside $S$ is zero, that is, the algebraic sum of the charge on the inner surface is $\oiint_{S_{\mathrm{in}}}\sigma\,\mathrm{d}S=0$. If $\sigma\ne0$ somewhere on the inner surface, the inner surface must carry both positive and negative charge, and the cavity would contain **electric field lines** starting on positive charges and ending on negative charges; along such a line from conductor to conductor the **electric potential** decreases, contradicting the fact that the conductor is an equipotential body. Hence $\sigma=0$ everywhere on the inner surface, the cavity has no field lines, and $\boldsymbol{E}=\boldsymbol{0}$. $\square$

The proof does not use whether the shell is charged or whether there are charges outside. So the net charge on the shell and the charges induced by outside charges are distributed only on the outer surface; however the magnitude and position of the outside charges change, the charge distribution on the outer surface adjusts so that their total field in the cavity (and in the conductor) always vanishes. This result is also the most precise method for testing the inverse-square law of **Coulomb's law** ([5.3.1](/5.3.1#sec-1.2)): if the exponent were not 2, there would be a field inside a charged conducting shell.

### 3.4.2. Charge in the Cavity

**Theorem 3.4.2** If the cavity of a conducting shell contains a charge $q$, then in electrostatic equilibrium the inner surface of the cavity carries charge $-q$, and the field in the cavity is in general nonzero.

**Proof** Take a closed surface in the conductor enclosing the cavity. The field on it is zero, so by Gauss's law $q+q_{\mathrm{in\,surf}}=0$, that is, the inner surface carries $q_{\mathrm{in\,surf}}=-q$. $\square$

If the shell originally carries charge $Q$, then by conservation of charge the outer surface carries $Q+q$. The field distribution obeys the following rules:

- the total field of the cavity charge and the inner-surface charge vanishes outside the inner surface (in the conductor and outside the cavity);
- the total field of the outer-surface charge and the exterior charges vanishes inside the outer surface (in the conductor and in the cavity).

Hence the field in the cavity is determined only by $q$ and the inner-surface charge, and the field outside only by the outer-surface charge and the exterior charges. Changing the position of the charge in the cavity changes only the charge distribution on the inner surface and does not affect the exterior; but when the magnitude of $q$ changes, the outer-surface charge $Q+q$ changes accordingly and so does the exterior field. An ungrounded conducting shell therefore cannot shield the exterior from the effect of charges in the cavity.

**Example 3.4.1 (Off-Center Point Charge in a Conducting Spherical Shell)** The outer surface of an uncharged conducting shell is a sphere of radius $R$, and a **point charge** $q$ sits off-center in the cavity (which need not be spherical). What is the field outside?

By the rules above, the exterior field is determined only by the outer-surface charge and is independent of the shape of the cavity and of the position of $q$ in it. The outer surface carries charge $q$ and there are no other charges outside, so the distribution of the outer-surface charge is determined only by the shape of the outer surface: on a sphere it is uniform. The field outside is therefore $\boldsymbol{E}=\frac{q}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r$, with $r$ measured from the center $O$ of the sphere, not from the position of $q$. The charge distribution on the inner surface is nonuniform, with larger $\lvert\sigma\rvert$ near $q$.

### 3.4.3. Grounded Shells and Electrostatic Shielding

**Theorem 3.4.3** A grounded closed conducting shell shields the exterior from the effect of charges inside: the electric field outside the shell is determined only by the exterior charges and is independent of the magnitude and position of the charges in the cavity.

**Proof** The conditions that determine the solution in the exterior region are: the magnitudes and positions of the exterior charges are given; $\varphi=0$ on the outer surface (grounded); and $\varphi=0$ at infinity. None of these depends on the charges in the cavity, and by the uniqueness theorem of §3.5 the field outside is uniquely determined by them. $\square$

**Definition 3.4.1 (Electrostatic Shielding)** The use of a conducting shell to keep a region of space free from the influence of external electric fields, or to keep the charges inside a region from influencing the exterior, is called **electrostatic shielding**.

A closed conducting shell (grounded or not) shields the cavity from the effect of exterior charges (Theorem 3.4.1); a grounded closed shell also shields the exterior from the effect of charges in the cavity (Theorem 3.4.3). Practical shields often use metal mesh instead of a closed metal shell, and the shielding remains very good when the mesh size is much smaller than the distances of interest. This is the Faraday cage: a person sitting in a metal cage is not harmed by the strong fields of discharges outside it, and for the same reason the occupants of a car or aircraft are safe when it is struck by lightning. The metal casings of precision instruments and the outer metal braid of coaxial cables act as electrostatic shields. For time-varying electromagnetic fields, shielding also relies on eddy currents and the skin effect ([5.3.9](/5.3.9)).

## 3.5. The Uniqueness Theorem of Electrostatics

### 3.5.1. Boundary Value Problems in Electrostatics

Consider a typical electrostatics problem. A region $V$ is bounded by a surface $S$ ($S$ may also be a sphere at infinity); inside $V$ there are some given charges and several conductors, whose shapes and positions and the boundary surface are all fixed. In the part of $V$ outside the conductors the potential satisfies the **Poisson equation** ([5.3.2](/5.3.2#sec-2.4.2))

$$
\Delta\varphi=-\frac{\rho}{\varepsilon_0}.
$$
Once $\varphi$ is found, the field strength follows from $\boldsymbol{E}=-\nabla\varphi$. To make the solution definite, boundary conditions must also be given: on the boundary surface $S$ either the potential (the **Dirichlet boundary condition**) or the normal derivative of the potential $\frac{\partial\varphi}{\partial n}=-E_{\mathrm{n}}$ (the **Neumann boundary condition**); on the surface of each conductor, which is an equipotential body, either its potential or its total charge $Q_k=-\varepsilon_0\oiint_{S_k}\frac{\partial\varphi}{\partial n}\,\mathrm{d}S$ ($\boldsymbol{e}_{\mathrm{n}}$ pointing out of the conductor) is given.

### 3.5.2. The Uniqueness Theorem

**Theorem 3.5.1 (Uniqueness Theorem of Electrostatics)** In the region described above, suppose the charge distribution $\rho$ is given, and also

- the potential, or the normal derivative of the potential, on the outer boundary surface $S$;
- the potential of each conductor, or the total charge of each conductor (potentials may be given for some conductors and total charges for others).

Then the electrostatic field in the region is uniquely determined, and so is the charge distribution on the conductor surfaces; the potential is also unique, except that it may differ by a constant when only normal derivatives and total charges are given.

**Proof** Let $\varphi_1$ and $\varphi_2$ both satisfy these conditions, and let $\psi=\varphi_1-\varphi_2$. Outside the conductors $\Delta\psi=0$; on each conductor surface $\psi$ is constant and either $\psi=0$ (potential given) or $\oiint\frac{\partial\psi}{\partial n}\,\mathrm{d}S=0$ (total charge given); on the outer boundary $\psi=0$ or $\frac{\partial\psi}{\partial n}=0$. Hence $\oiint\psi\frac{\partial\psi}{\partial n}\,\mathrm{d}S=0$ over the whole boundary ($\psi$ is constant on a conductor surface and can be taken out of the integral). By **Green's first identity** ([Theorem 14.5.2](/2.2.14#thm-14.5.2) with $f=g=\psi$),

$$
\iiint\lvert\nabla\psi\rvert^2\,\mathrm{d}V=\oiint\psi\frac{\partial\psi}{\partial n}\,\mathrm{d}S-\iiint\psi\Delta\psi\,\mathrm{d}V=0,
$$
so $\nabla\psi=\boldsymbol{0}$ and $\boldsymbol{E}_1=\boldsymbol{E}_2$. If the potential is given on any part of the boundary, $\psi$ vanishes there, and then $\psi\equiv0$. $\square$

This is the physical generalization of the uniqueness of the Dirichlet and Neumann problems in [2.5.8](/2.5.8) ([Theorem 8.1.2](/2.5.8#thm-8.1.2)): conductors supply a new kind of boundary condition, "equipotential with given total flux".

The uniqueness theorem is significant in two ways:

- It identifies the relation between the conditions that determine the solution and the electrostatic field: given the charge distribution and the boundary conditions above, the electrostatic field is completely determined. The results on conducting shells in §3.4 can all be derived from it.
- It allows "guessing the solution": any solution that satisfies the equation and all the conditions, however it was obtained, is the unique correct solution. The method of images (§3.6) works in just this way.

Note that the uniqueness theorem says that one set of conditions has only one solution; two different sets of conditions (different problems) may happen to give the same solution, but that is a relation between the two problems and cannot be explained by the uniqueness theorem.

The uniqueness theorem is also the basis of numerical methods: divide the region into a grid and replace the **Laplace operator** by finite differences, which gives a large sparse system of linear equations ([4.4.4](/4.4.4)) whose solution approximates the unique potential. The figure below is the field around an L-shaped electrode held at potential 1 in a grounded square box, found by this method: the field lines are perpendicular to the electrode surface, the field is strongest near the protruding corners and weakest near the re-entrant corner, in agreement with the qualitative conclusion of §3.2.

![Numerical solution of Laplace's equation by finite differences: an L-shaped electrode at potential 1 in a grounded square box. Left: equipotential lines and field lines, with the field lines everywhere perpendicular to the electrode and the box walls; right: logarithm of the field strength, strongest at the convex corners and weakest at the re-entrant corner and the box corners](./plots/laplace-box.py)

## 3.6. The Method of Images

### 3.6.1. Principle of the Method

The method of images (the **method of images** used in 2.5.8 to construct Green's functions) rests on the uniqueness theorem. If a very thin conducting sheet is placed on an equipotential surface of the original field and brought to the potential that surface originally had, the field is not affected at all. Conversely, if fictitious charges of suitable magnitude and position are placed in the region occupied by the conductor so that the conductor surface becomes exactly the original equipotential surface, then in the region outside the conductor these charges act exactly as the conductor does. These fictitious charges are called *image charges*.

The principle for placing image charges is not to destroy the original conditions determining the solution:

1. the image charges must lie outside the region of interest (otherwise they would change the charge distribution in the region and hence the **Poisson equation**);
2. the total field of the original and image charges must satisfy the original boundary conditions.

The image charges then replace the unknown induced charges on the boundary in their effect on the region, and the problem reduces to finding the field of a few point charges. More than one image charge may be needed, and image charges cannot be found in every case.

### 3.6.2. Grounded Conducting Plane

**Example 3.6.1 (Point Charge Near a Grounded Infinite Conducting Plane)** A point charge $q$ lies at $(0,0,a)$ and $z=0$ is an infinite grounded conducting plane. Find the field in the region $z>0$ and the induced charge on the plane.

Conditions: in $z>0$ there is only the point charge $q$; $\varphi=0$ on $z=0$; $\varphi=0$ at infinity. By the uniqueness theorem the solution in $z>0$ is unique. Remove the conductor and place an image charge $q'=-q$ at $(0,0,-a)$. A point on $z=0$ is equidistant from $q$ and $q'$, so $\varphi=0$ there and the original conditions are unchanged. The potential in $z>0$ is therefore

$$
\varphi=\frac{q}{4\pi\varepsilon_0}\Big(\frac1{r}-\frac1{r'}\Big),
$$
where $r$ and $r'$ are the distances from the field point to $q$ and $q'$. On the conducting plane at distance $s$ from the foot of the perpendicular, the parallel components of the fields of $q$ and $q'$ cancel and the normal components add:

$$
\boldsymbol{E}=-\frac{qa}{2\pi\varepsilon_0(a^2+s^2)^{3/2}}\boldsymbol{e}_z,\qquad\sigma=\varepsilon_0E_z=-\frac{qa}{2\pi(a^2+s^2)^{3/2}}.
$$
The total induced charge is $\int_0^\infty\sigma\cdot2\pi s\,\mathrm{d}s=-q$: all the field lines from $q$ end on the conducting plane. The charge $q$ is attracted by the plane with a force equal to that exerted by the image charge, $\frac{q^2}{4\pi\varepsilon_0(2a)^2}$. Note that $\sigma=-q\,K$, where $K=\frac{a}{2\pi(a^2+s^2)^{3/2}}$ is exactly the Poisson kernel of the half-space ([Eq. (8.6)](/2.5.8#eq-8.6) in [2.5.8](/2.5.8#sec-8.3.2), $n=3$).

### 3.6.3. Grounded Conducting Sphere

**Example 3.6.2 (Point Charge Outside a Grounded Conducting Sphere)** A point charge $q$ lies outside a grounded conducting sphere of radius $R$, at distance $l$ from the center $O$. Find the potential outside the sphere.

Conditions: the exterior charge is given; $\varphi=0$ on the sphere; $\varphi=0$ at infinity. By symmetry, try an image charge $q'$ inside the sphere on the line $OA$ at distance $l'$ from $O$. The potential outside is

$$
\varphi=\frac{1}{4\pi\varepsilon_0}\Big(\frac{q}{r}+\frac{q'}{r'}\Big).
$$
It automatically satisfies the condition at infinity. For it to vanish on the sphere we need $r'/r$ to be the constant $-q'/q$ on the sphere. By the Apollonius property of the sphere, when $l'=R^2/l$ the ratio of the distances from any point of the sphere to the image point and to $q$ is the constant $R/l$, so

$$
q'=-\frac{R}{l}q,\qquad l'=\frac{R^2}{l},\qquad\varphi=\frac{q}{4\pi\varepsilon_0}\Big(\frac1r-\frac{R}{l}\frac1{r'}\Big).
$$
By the uniqueness theorem this is the potential outside the sphere. The total induced charge on the sphere equals $q'=-\frac{R}{l}q$, smaller in magnitude than $q$ (some of the field lines outside the sphere extend to infinity). This is exactly the Green's function of the ball in [2.5.8](/2.5.8#sec-8.3.3): the image point is the inversion of $q$ in the sphere, and the strength of the image charge is $-R/l$.

If the sphere is insulated and carries charge $Q$ instead of being grounded, place in addition an image charge $Q-q'=Q+\frac{R}{l}q$ at the center: it keeps the sphere an equipotential and makes the total charge of the sphere $Q$.

![Method of images. Left: a point charge above a grounded conducting plane; the equipotential lines (colored) and field lines (gray) coincide in the upper half-space with those of the charge q and the image charge −q. Middle: a point charge outside a grounded conducting sphere (l = 2R); the image charge −qR/l sits at the inverse point R²/l, with some field lines ending on the sphere and the rest extending to infinity. Right: induced surface charge density on the conducting plane, with total −q](./plots/image-charges.py)

**Example 3.6.3 (Conducting Sphere in a Uniform Field)** [Example 5.4.2](/2.5.5#ex-5.4.2) in [2.5.5](/2.5.5) used separation of variables to find the potential outside a grounded conducting sphere (radius $R$) in a uniform field $\boldsymbol{E}_0=E_0\boldsymbol{e}_z$, $\varphi=-E_0\Big(r-\frac{R^3}{r^2}\Big)\cos\theta$. The second term is the potential of an **electric dipole** at the center with **electric dipole moment** $\boldsymbol{p}=4\pi\varepsilon_0R^3\boldsymbol{E}_0$ ([Example 2.3.1](/5.3.2#ex-2.3.1)); it is the "image" for this problem. The induced charge on the sphere is $\sigma=-\varepsilon_0\frac{\partial\varphi}{\partial r}\Big|_{r=R}=3\varepsilon_0E_0\cos\theta$, with zero total, so an insulated uncharged conducting sphere gives the same result.

## Questions

1. Is the field inside a conductor in electrostatic equilibrium zero only for spherical conductors?
   Hint: no. For a conductor of any shape the field inside is zero in electrostatic equilibrium; this is the equilibrium condition and is independent of the shape.
2. After an isolated conductor is given a positive charge, does its mass increase, decrease or stay the same?
   Hint: it decreases. Becoming positively charged means losing electrons, but the decrease (each electron has mass $9.1\times10^{-31}\,\mathrm{kg}$) is minuscule.
3. When a charged body is brought near a conducting shell, is the field that the body alone produces in the cavity zero? How does electrostatic shielding come about?
   Hint: it is not zero. The body induces charge on the outer surface, and the field of the induced charge in the cavity exactly cancels that of the body; shielding is the result of this superposition.
4. A point charge is placed at the center of an isolated conducting spherical shell. Is the charge distribution on the inner and outer surfaces uniform? What if the charge is off-center?
   Hint: at the center both surfaces are uniform; off-center the inner surface is nonuniform while the outer surface is still uniform (Example 3.4.1).
5. The field is stronger where the surface of a charged conductor has greater curvature. Starting at a point $a$ on a conductor, go along a field line for some distance, then go perpendicular to the field lines onto another field line, follow it back to a point $b$ on the conductor, and finally return to $a$ along the conductor surface. The field at $a$ is stronger than at $b$. Is the circulation along this closed path nonzero, violating the circulation theorem?
   Hint: no. The segment perpendicular to the field lines lies on an equipotential surface, and the integrals along the two field-line segments both equal the potential difference between the conductor and this equipotential surface, so they are equal; the field is stronger at $a$, but that segment is also shorter (the equipotential surfaces are denser there). The integrals along the conductor surface and along the perpendicular segment vanish, so the total circulation is zero.
6. Find the image charges for the following problems, or show that they do not exist: (1) a point charge $q$ inside the right angle formed by two perpendicular grounded conducting half-planes; (2) an infinitely long uniformly charged line (linear density $\lambda$) parallel to a grounded conducting plane; (3) a point charge inside the $270^\circ$ angle formed by two grounded conducting half-planes; (4) a point charge midway between two parallel grounded conducting plates; (5) a point charge $q$ outside an insulated conducting sphere carrying charge $Q$.
   Hint: (1) Three image charges: the mirror images $-q$, $-q$ in the two planes, and $+q$ at the point symmetric about the line of intersection. (2) The mirror image $-\lambda$ in the plane. (3) No finite set of point image charges exists: only when the angle between the planes is $\pi/n$ ($n$ a positive integer) can the problem be solved with $2n-1$ image charges. (4) Infinitely many image charges are needed: place $-q,+q,-q,\dots$ alternately at $\pm2d,\pm4d,\pm6d,\dots$ ($d$ is the distance from the charge to each plate). (5) Put $-\frac{R}{l}q$ at $\frac{R^2}{l}$ and $Q+\frac{R}{l}q$ at the center of the sphere.
