---
title: Dielectrics in Electrostatic Fields
description: The effect of dielectrics on electric fields, electronic and orientation polarization, polarization, electric susceptibility and bound charge, the electric displacement and its Gauss's law, interface conditions, capacitors and capacitance, and electrostatic energy in the presence of dielectrics.
source_hash: fa025dfdbf68
---

The previous two chapters studied electrostatic fields in vacuum and in the presence of **conductors**, which contain a large number of free charges and in which the **electric field strength** vanishes at **electrostatic equilibrium**. This chapter studies the other class of matter, insulators, also called dielectrics. A dielectric contains almost no free charges, but its molecules are "stretched" or "turned" by an electric field, and bound charges that cannot move freely appear inside the medium and on its surface. The field of the bound charges only partly cancels the external field, so the field strength in the medium is reduced but not zero. Describing this requires two new macroscopic quantities, the polarization $\boldsymbol{P}$ and the electric displacement $\boldsymbol{D}$; the latter makes **Gauss's law** in a medium involve free charge only. On this basis we discuss capacitors, the most important application of dielectrics, and the electrostatic energy in the presence of dielectrics.

Mathematically, the relation between bound charge and $\boldsymbol{P}$ is a direct application of the **divergence theorem** ([2.2.14](/2.2.14)), and the electric susceptibility of an anisotropic medium is a **symmetric matrix**; the interface conditions, together with the boundary value problems of the previous chapter ([5.3.3](/5.3.3)), determine the electrostatic field in the presence of dielectrics. The next chapter, [5.3.5](/5.3.5), turns to moving charges, that is, steady currents; magnetic materials ([5.3.8](/5.3.8)) are treated in exact parallel to this chapter.

## 4.1. The Effect of Dielectrics on the Electric Field

**Definition 4.1.1 (Dielectric)** A substance that does not conduct electricity, that is, one containing almost no freely moving charges, is called a **dielectric** (insulator).

Demonstration experiment: a parallel-plate capacitor is charged and then disconnected from the source, so that the plate charge $Q$ stays constant, and the voltage between the plates is measured with an electrometer. When a dielectric is inserted, the deflection of the electrometer decreases; when it is removed, the deflection is restored. If the dielectric fills the space between the plates, both the voltage and the field strength are reduced by the factor $1/\varepsilon_{\mathrm{r}}$:

$$
U = \frac{U_0}{\varepsilon_{\mathrm{r}}},\qquad E = \frac{E_0}{\varepsilon_{\mathrm{r}}},
$$
where $\varepsilon_{\mathrm{r}}$ is a constant determined by the dielectric, called the relative permittivity (Definition 4.3.2).

**Definition 4.1.2 (Dielectric Polarization)** The appearance of charges that cannot move freely, inside or on the surface of a dielectric under the action of an electric field, is called **dielectric polarization**, and these charges are called **bound charges** (polarization charges).

Unlike the free charges in a conductor, bound charges are held inside molecules and can only be displaced slightly; their field cannot cancel the external field completely, so the total field strength inside the medium is reduced but not zero.

| Material | $\varepsilon_{\mathrm{r}}$ | Material | $\varepsilon_{\mathrm{r}}$ |
|---|---|---|---|
| Vacuum | $1$ (exact) | Glass | $5$–$10$ |
| Air ($20^\circ\mathrm{C}$, $1\,\mathrm{atm}$) | $1.00054$ | Mica | $4$–$7$ |
| Kerosene | about $2$ | Water ($20^\circ\mathrm{C}$) | $80$ |
| Paper | $2$–$4$ | Titanium dioxide (rutile) | about $100$ |
| Glycerin ($25^\circ\mathrm{C}$) | about $42$ | Barium titanate $\ce{BaTiO3}$ | $10^3$–$10^4$ |

Materials with extremely large $\varepsilon_{\mathrm{r}}$, such as barium titanate, are ferroelectrics: their $\boldsymbol{P}$ is not linear in $\boldsymbol{E}$ and shows a hysteresis loop, similar to ferromagnetic substances ([5.3.8](/5.3.8)).

## 4.2. Polarization of Dielectrics

### 4.2.1. Microscopic Electric Structure of Dielectrics

Molecules consist of nuclei and **electron clouds**. In computing the field produced by a molecule at a distance, all the positive charge in the molecule can be replaced by a **point charge** $q$ at the "center of positive charge" and all the negative charge by a point charge $-q$ at the "center of negative charge". If $\boldsymbol{l}$ is the position vector from the center of negative charge to that of positive charge, the **electric dipole moment** of the molecule is $\boldsymbol{p} = q\boldsymbol{l}$. According to whether these two centers coincide in the absence of an external field, the molecules of dielectrics fall into two classes:

**Definition 4.2.1 (Polar and Nonpolar Molecules)** A molecule whose centers of positive and negative charge coincide in the absence of an external field, so that it has no permanent dipole moment, is called a **nonpolar molecule** (for example $\ce{He}$, $\ce{N2}$, $\ce{CH4}$, $\ce{CO2}$); a molecule whose centers of positive and negative charge do not coincide and which has a permanent dipole moment is called a **polar molecule** (for example $\ce{H2O}$, $\ce{NH3}$, $\ce{HCl}$).

Permanent dipole moments of some polar molecules (in units of $10^{-30}\,\mathrm{C\,m}$):

| Molecule | $\ce{H2O}$ | $\ce{NH3}$ | $\ce{HCl}$ | $\ce{SO2}$ | $\ce{CO}$ | $\ce{C2H5OH}$ |
|---|---|---|---|---|---|---|
| $p$ | $6.2$ | $4.9$ | $3.6$ | $5.4$ | $0.37$ | $5.6$ |

Chemistry commonly uses the non-SI unit debye: $1\,\mathrm{D} \approx 3.336\times10^{-30}\,\mathrm{C\,m}$, so the water molecule has $p \approx 1.85\,\mathrm{D}$. Whether a molecule is polar depends on its geometry: $\ce{CO2}$ is linear and the dipole moments of its two $\ce{C=O}$ bonds cancel; $\ce{H2O}$ is bent and they do not.

### 4.2.2. Polarization Mechanisms

**Definition 4.2.2 (Electronic and Orientation Polarization)** Under an external field, the electron cloud of a molecule is distorted relative to the nucleus, the centers of positive and negative charge are pulled apart, and an induced dipole moment along the field appears; this kind of polarization is called **electronic polarization** (displacement polarization). The permanent dipole moments of polar molecules experience a torque from the external field and tend to align along it; this kind of polarization is called **orientation polarization**.

- A nonpolar molecule has only electronic polarization. The induced dipole moment is proportional to the field strength and parallel to it, and is zero without a field.
- Without a field, the orientations of the permanent dipole moments of polar molecules are randomly distributed by thermal motion, and the medium shows no net electric effect macroscopically; with a field, the torque $\boldsymbol{p}\times\boldsymbol{E}$ makes them tend to align with it, while thermal motion opposes the alignment, so orientation polarization depends on temperature. Polar molecules also have electronic polarization, but in a static field orientation polarization dominates.
- In ionic crystals (such as $\ce{NaCl}$, $\ce{BaTiO3}$), the positive and negative ions are displaced relative to each other by the field, which also produces induced dipole moments; this is called ionic polarization.

The macroscopic effect of the three mechanisms is the same: bound charges appear on the end faces of the dielectric.

### 4.2.3. The Polarization Process

Polarization is a self-consistent equilibrium process. The external field $\boldsymbol{E}_0$ (produced by free charges) polarizes the medium, and the bound charges excite an additional field $\boldsymbol{E}'$; by the **superposition principle of electric fields**, the total field in the medium is

$$
\boldsymbol{E} = \boldsymbol{E}_0 + \boldsymbol{E}'.
$$
The total field $\boldsymbol{E}$ in turn determines the degree of polarization, producing new bound charges and a new $\boldsymbol{E}'$, and so on until electrostatic equilibrium is reached. What polarizes the medium is the total field $\boldsymbol{E}$, not the external field $\boldsymbol{E}_0$. We neglect here the back-action of $\boldsymbol{E}'$ on the charge distribution of the sources of the external field; when the sources are conductors this back-action generally cannot be neglected, and the equations must be solved simultaneously (Example 4.5.1).

### 4.2.4. Polarization

**Definition 4.2.3 (Polarization)** The vector sum of the dipole moments of all molecules in a volume element $\Delta V$ near a point of the medium, divided by $\Delta V$,

$$
\boldsymbol{P} = \frac{\sum_i \boldsymbol{p}_i}{\Delta V},
$$
is called the **electric polarization** at that point. Its unit is $\mathrm{C\,m^{-2}}$, the same dimension as surface **charge density**. The volume $\Delta V$ must be macroscopically small (much smaller than the scale over which $\boldsymbol{P}$ varies) and microscopically large (much larger than the intermolecular spacing).

If there are $n$ molecules per unit volume, each with mean dipole moment $\boldsymbol{p}$, then $\boldsymbol{P} = n\boldsymbol{p}$. $\boldsymbol{P}$ reflects both the size of the molecular dipole moments and the degree to which they are ordered, and can be regarded as the response of the dielectric to the total field $\boldsymbol{E}$.

### 4.2.5. Laws of Polarization

**Definition 4.2.4 (Electric Susceptibility)** When the field is not too strong, $\boldsymbol{P}$ is linear in $\boldsymbol{E}$, and such a dielectric is called a **linear dielectric**. For an isotropic linear dielectric,

$$
\boldsymbol{P} = \varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E},\qquad \varepsilon_{\mathrm{r}} = 1 + \chi_{\mathrm{e}},
$$
and the coefficient $\chi_{\mathrm{e}}$ is called the **electric susceptibility**. Both $\chi_{\mathrm{e}}$ and $\varepsilon_{\mathrm{r}}$ are dimensionless, and $\chi_{\mathrm{e}} > 0$, so $\boldsymbol{P}$ is parallel to $\boldsymbol{E}$.

For an anisotropic linear dielectric (such as many crystals), each component of $\boldsymbol{P}$ is a linear combination of the components of $\boldsymbol{E}$:

$$
\begin{bmatrix} P_x \\ P_y \\ P_z \end{bmatrix}
= \varepsilon_0
\begin{bmatrix}
\chi_{xx} & \chi_{xy} & \chi_{xz} \\
\chi_{yx} & \chi_{yy} & \chi_{yz} \\
\chi_{zx} & \chi_{zy} & \chi_{zz}
\end{bmatrix}
\begin{bmatrix} E_x \\ E_y \\ E_z \end{bmatrix},
$$
The susceptibility is a second-rank tensor, and it can be shown to be a **symmetric matrix** (from the existence of an energy). By the **spectral theorem** we can always choose a set of orthogonal axes (the principal axes of the crystal) in which it is diagonal, and the three **eigenvalues** are the susceptibilities along the three principal axes. In general $\boldsymbol{P}$ is not parallel to $\boldsymbol{E}$: the medium polarizes to different degrees in different directions, which is related to the structure and symmetry of the crystal. Birefringence in optics ([5.4.3](/5.4.3)) originates in this anisotropy. In what follows we consider only isotropic linear dielectrics.

### 4.2.6. Bound Charge

Draw any closed surface $S$ in a polarized medium and compute the bound charge in the volume $V$ it encloses. Molecules lying entirely inside or entirely outside $V$ contribute nothing to the net charge in $V$; only molecules cut by $S$ contribute, the positive charge contributing $+q$ and the negative charge $-q$ inside $V$.

Take a surface element $\mathrm{d}S$ on $S$ with outward unit normal $\boldsymbol{e}_{\mathrm{n}}$. The polarization nearby can be regarded as uniform, with all molecular dipole moments $\boldsymbol{p} = q\boldsymbol{l}$ at angle $\theta$ to $\boldsymbol{e}_{\mathrm{n}}$. Construct an oblique cylinder of length $l$ along $\boldsymbol{l}$ with $\mathrm{d}S$ as its midsection; only molecules whose centers lie in this cylinder are cut by $\mathrm{d}S$. For $\theta < \pi/2$, the negative charges of these molecules stay in $V$, and the positive charge moved out of $V$ is

$$
nq\,(l\cos\theta\,\mathrm{d}S) = n\boldsymbol{p}\cdot\boldsymbol{e}_{\mathrm{n}}\,\mathrm{d}S = \boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S},
$$
and the result has the same form for $\theta > \pi/2$. Summing over the whole of $S$ gives:

**Theorem 4.2.1** The bound charge enclosed by any closed surface equals the negative of the **flux** of the polarization through that closed surface:

$$
q'_{\mathrm{enc}} = -\oint_S \boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}.
$$

By the **divergence theorem**, letting $V$ shrink to a point gives the volume density of bound charge; taking a small flat cylindrical surface at the interface between the medium and vacuum gives the surface density:

**Formula 4.2.1 (Bound Charge Density)**

$$
\rho' = -\nabla\cdot\boldsymbol{P},\qquad \sigma' = \boldsymbol{P}\cdot\boldsymbol{e}_{\mathrm{n}} = P_{\mathrm{n}},
$$
where $\boldsymbol{e}_{\mathrm{n}}$ is the unit normal on the surface of the medium pointing from the medium to the outside.

The **divergence** describes the "sources" of a vector field: the lines of $\boldsymbol{P}$ start on negative bound charges and end on positive bound charges. For uniform polarization $\nabla\cdot\boldsymbol{P} = 0$ and bound charge appears only on the surface; for nonuniform polarization there may be bound charge both inside and on the surface.

### 4.2.7. Dielectric Breakdown

**Definition 4.2.5 (Dielectric Breakdown)** When the external field is very strong, the positive and negative charges in molecules may be torn apart and become free charges, and the dielectric loses its insulating property and becomes a conductor; this phenomenon is called **dielectric breakdown**. The maximum field strength a dielectric can withstand is called its **dielectric strength** (breakdown field).

The dielectric strength of air is about $3\,\mathrm{kV\,mm^{-1}}$ ($3\times10^6\,\mathrm{V\,m^{-1}}$); lightning and electric sparks are breakdowns of air; mica and ceramics reach the order of $10^2\,\mathrm{kV\,mm^{-1}}$. The voltage rating of a capacitor is determined by the dielectric strength of the dielectric in it.

## 4.3. Laws of the Electrostatic Field in the Presence of Dielectrics

In the presence of a dielectric, the electrostatic field is produced jointly by the free charges $q_0$ and the bound charges $q'$. All of them are stationary, so **Gauss's law** and the **circulation theorem for the electrostatic field** still hold:

$$
\oint_S \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S} = \frac{q_{0,\mathrm{enc}} + q'_{\mathrm{enc}}}{\varepsilon_0},\qquad \oint_L \boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l} = 0,
$$
where $\boldsymbol{E}$ is the total field strength produced by all the charges.

**Example 4.3.1** The plates of a parallel-plate capacitor are very large, with free surface charge densities $\pm\sigma_0$, and the space between them is filled with a homogeneous isotropic linear dielectric of relative permittivity $\varepsilon_{\mathrm{r}}$. Find the field strength between the plates.

**Solution** The medium is uniformly polarized, and bound charge appears only on its two surfaces adjacent to the plates, with surface densities $\mp\sigma'$ (opposite in sign to the charge on the adjacent plate). The field between the plates is the superposition of the fields of four infinite charged planes:

$$
E = E_0 - E' = \frac{\sigma_0 - \sigma'}{\varepsilon_0}.
$$
Also $\sigma' = P = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)E$, and combining the two gives

$$
E = \frac{\sigma_0}{\varepsilon_0\varepsilon_{\mathrm{r}}} = \frac{E_0}{\varepsilon_{\mathrm{r}}},\qquad \sigma' = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\sigma_0 .
$$

This is exactly the experimental result of §4.1. Similarly, when a point charge $Q_0$ is surrounded by an infinite homogeneous linear dielectric, $\boldsymbol{E} = \dfrac{Q_0}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}\boldsymbol{e}_r$. The statement that "the field strength is reduced to $1/\varepsilon_{\mathrm{r}}$" does not hold in general: it requires a homogeneous medium filling the entire space where there is a field, or interfaces of the medium that are all **equipotential surfaces** (in Example 4.3.2 the field outside the medium is not reduced).

### 4.3.1. The Electric Displacement and Its Gauss's Law

In practical problems the known quantities are the free charges (such as the charge on capacitor plates) while the bound charges are unknown, so using Gauss's law for $\boldsymbol{E}$ directly is inconvenient. Substituting Theorem 4.2.1 into Gauss's law for $\boldsymbol{E}$ eliminates $q'_{\mathrm{enc}}$:

$$
\oint_S(\varepsilon_0\boldsymbol{E} + \boldsymbol{P})\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}} .
$$

**Definition 4.3.1 (Electric Displacement)** The vector

$$
\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P}
$$
is called the **electric displacement** (electric displacement field), with unit $\mathrm{C\,m^{-2}}$. This is a general definition, independent of the properties of the medium.

**Theorem 4.3.1 (Gauss's Law for $\boldsymbol{D}$)** The flux of the electric displacement through any closed surface equals the algebraic sum of the free charges enclosed by the surface:

$$
\oint_S\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}},\qquad \nabla\cdot\boldsymbol{D} = \rho_0 .
$$

$\boldsymbol{D}$ is an auxiliary quantity introduced for convenience: what determines the force on a charge is still $\boldsymbol{E}$. The flux of $\boldsymbol{D}$ depends only on free charges, but $\boldsymbol{D}$ itself generally depends on bound charges as well; only when both the charge distribution and the medium have enough symmetry (spherical, cylindrical or planar) can $\boldsymbol{D}$ be found first from Gauss's law for $\boldsymbol{D}$ and then $\boldsymbol{E}$ and $\boldsymbol{P}$.

**Definition 4.3.2 (Relative Permittivity)** For an isotropic linear dielectric,

$$
\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \varepsilon_0\chi_{\mathrm{e}}\boldsymbol{E} = \varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E} = \varepsilon\boldsymbol{E},
$$
where $\varepsilon_{\mathrm{r}} = 1 + \chi_{\mathrm{e}}$ is called the **relative permittivity** (dielectric constant) and $\varepsilon = \varepsilon_0\varepsilon_{\mathrm{r}}$ the **permittivity** of the medium. Then

$$
\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E} = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\boldsymbol{D},
$$
and $\boldsymbol{P}$, $\boldsymbol{E}$ and $\boldsymbol{D}$ are all parallel; in vacuum $\boldsymbol{P} = \boldsymbol{0}$ and $\boldsymbol{D} = \varepsilon_0\boldsymbol{E}$.

### 4.3.2. Distribution of Bound Charge

**Property 4.3.1** In a homogeneous isotropic linear dielectric (whether or not the polarization is uniform), the volume density of bound charge is proportional to the volume density of free charge:

$$
\rho' = -\Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\rho_0 .
$$
Hence where there is no free charge inside the medium there is no bound charge either; if there is no free charge inside the medium, the bound charge is distributed only on the surface of the medium.

**Proof** Since $\varepsilon_{\mathrm{r}}$ is constant, Formula 4.2.1 and Theorem 4.3.1 give $\rho' = -\nabla\cdot\boldsymbol{P} = -\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)\nabla\cdot\boldsymbol{D} = -\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)\rho_0$. $\square$

The bound charge has the opposite sign to the free charge it surrounds and partially screens it. Bound surface charge generally appears at the interface of two different media and at the interface of a medium and a charged conductor. An inhomogeneous medium can be regarded as a collection of many small homogeneous regions, with bound charge at the interfaces between neighboring regions, so bound volume charge can appear inside an inhomogeneous medium.

**Example 4.3.2 (Homogeneous Dielectric Shell)** A conducting sphere of radius $R_1$ carrying charge $q_0$ is surrounded by a homogeneous dielectric shell of outer radius $R_2$ and relative permittivity $\varepsilon_{\mathrm{r}}$. Find $\boldsymbol{E}$ and the distribution of bound charge.

**Solution** Both the charge and the medium are spherically symmetric, so $\boldsymbol{D} = D(r)\boldsymbol{e}_r$. Taking a concentric sphere of radius $r$ outside the conducting sphere, Gauss's law for $\boldsymbol{D}$ gives $4\pi r^2D = q_0$,

$$
\boldsymbol{D} = \frac{q_0}{4\pi r^2}\boldsymbol{e}_r\quad(r > R_1),
$$
so that

$$
\boldsymbol{E} = \begin{cases}
\dfrac{q_0}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}\boldsymbol{e}_r, & R_1 < r < R_2,\\[2ex]
\dfrac{q_0}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r, & r > R_2,
\end{cases}
\qquad
\boldsymbol{P} = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi r^2}\boldsymbol{e}_r\quad(R_1 < r < R_2).
$$

The medium is homogeneous with no free charge inside, so by Property 4.3.1, $\rho' = 0$ inside the medium. On the inner surface the normal points from the medium to the conductor, $\boldsymbol{e}_{\mathrm{n}} = -\boldsymbol{e}_r$; on the outer surface $\boldsymbol{e}_{\mathrm{n}} = \boldsymbol{e}_r$. By Formula 4.2.1,

$$
\sigma'_1 = -P(R_1) = -\Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi R_1^2},\qquad
\sigma'_2 = P(R_2) = \Big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\Big)\frac{q_0}{4\pi R_2^2},
$$
and the total bound charges on the inner and outer surfaces are $\mp\big(1 - \frac{1}{\varepsilon_{\mathrm{r}}}\big)q_0$, equal and opposite.

Note that what acts is still $\boldsymbol{E}$: the total field is the superposition of the fields of three uniformly charged spherical surfaces ($q_0$ and the two layers of bound charge). $\boldsymbol{D}$ is continuous beyond $r = R_1$; $\boldsymbol{E}$ and $\boldsymbol{P}$ jump at the two surfaces of the medium because of the bound surface charge there.

![D, E and P versus r for a conducting sphere surrounded by a dielectric shell (ε_r = 3, R₂ = 2R₁): D is continuous, while E and P jump at the surfaces of the medium](./plots/dielectric-shell-field.py)

### 4.3.3. Interface Conditions for the Electrostatic Field

At the interface of two media the field quantities are in general discontinuous. Let the free surface charge density on the interface be $\sigma_0$, let $\boldsymbol{e}_{\mathrm{n}}$ be the unit normal pointing from medium 2 to medium 1, and let $\boldsymbol{e}_{\mathrm{t}}$ be a unit tangent vector of the interface.

- Normal: construct a very flat small cylinder across the interface, with end faces of area $\Delta S$ on the two sides and height tending to zero. By Gauss's law for $\boldsymbol{D}$, $(D_{1\mathrm{n}} - D_{2\mathrm{n}})\Delta S = \sigma_0\Delta S$.
- Tangential: construct a small rectangular loop across the interface, with the two long sides $\Delta l$ on the two sides and the short sides tending to zero. By the circulation theorem, $(E_{1\mathrm{t}} - E_{2\mathrm{t}})\Delta l = 0$.

**Theorem 4.3.2 (Interface Conditions for the Electrostatic Field)**

$$
D_{1\mathrm{n}} - D_{2\mathrm{n}} = \sigma_0,\qquad E_{1\mathrm{t}} = E_{2\mathrm{t}} .
$$
When there is no free charge on the interface, the normal component of $\boldsymbol{D}$ is continuous and the tangential component of $\boldsymbol{E}$ is continuous.

The normal component of $\boldsymbol{E}$ is determined by all the charges, $\varepsilon_0(E_{1\mathrm{n}} - E_{2\mathrm{n}}) = \sigma_0 + \sigma'$, and is in general discontinuous.

For two isotropic linear media with $\sigma_0 = 0$ on the interface, $\varepsilon_1E_{1\mathrm{n}} = \varepsilon_2E_{2\mathrm{n}}$ and $E_{1\mathrm{t}} = E_{2\mathrm{t}}$. Let $\boldsymbol{E}_1$ and $\boldsymbol{E}_2$ make angles $\theta_1$ and $\theta_2$ with the normal; dividing the two relations gives the "**law of refraction**" for **electric field lines**

$$
\frac{\tan\theta_1}{\tan\theta_2} = \frac{\varepsilon_1}{\varepsilon_2} .
$$
For $\varepsilon_1 > \varepsilon_2$, $\theta_1 > \theta_2$: field lines entering a medium of larger permittivity bend away from the normal. These two interface conditions, together with the **Poisson equation** $\nabla\cdot(\varepsilon\nabla\varphi) = -\rho_0$ in the medium, make up the electrostatic boundary value problem in the presence of dielectrics, for which the **uniqueness theorem of electrostatics** ([5.3.3](/5.3.3)) still holds.

![With no free charge on the interface, field lines pass from a medium with ε₂ = ε₀ into a medium with ε₁ = 4ε₀ and bend away from the normal](./plots/field-line-refraction.py)

## 4.4. Capacitors and Capacitance

### 4.4.1. Capacitance of an Isolated Conductor

When an isolated conductor carries charge $Q$, it is an equipotential body with **electric potential** $\varphi$ (taking infinity as the zero). By superposition and the **uniqueness theorem of electrostatics**, when $Q$ is doubled the shape of the charge distribution is unchanged, the surface density doubles everywhere, and the potential doubles as well, so $Q/\varphi$ is a constant depending only on the shape and size of the conductor (and the surrounding medium).

**Definition 4.4.1 (Capacitance)** The ratio of the charge $Q$ on an isolated conductor to its potential $\varphi$,

$$
C = \frac{Q}{\varphi},
$$
is called the **capacitance** of the isolated conductor. The unit is the farad, $1\,\mathrm{F} = 1\,\mathrm{C\,V^{-1}}$; $\mu\mathrm{F}$ and $\mathrm{pF}$ are commonly used. The dimension of capacitance is $\dim C = \mathsf{L}^{-2}\,\mathsf{M}^{-1}\,\mathsf{T}^{4}\,\mathsf{I}^{2}$.

Capacitance is the charge needed to raise the potential of the conductor by one unit, that is, the ability of the conductor to "hold" charge. For an isolated conducting sphere of radius $R$, $\varphi = \dfrac{Q}{4\pi\varepsilon_0R}$,

$$
C = 4\pi\varepsilon_0R .
$$
A conducting sphere with a capacitance of $1\,\mathrm{F}$ would have a radius of about $9\times10^9\,\mathrm{m}$, 1400 times the radius of the earth; the capacitance of the earth itself is only about $7\times10^{-4}\,\mathrm{F}$. The capacitance of an isolated conductor is generally very small, and its potential is affected by surrounding charged bodies.

### 4.4.2. Capacitors

**Definition 4.4.2 (Capacitor)** A conductor surrounded by a conducting shell, so that by **electrostatic shielding** the field between them is unaffected by the exterior, forms a **capacitor**, and the two conductors are called its plates. When the plates carry equal and opposite charges $\pm Q$, the voltage $U$ between the plates is proportional to $Q$, and the capacitance of the capacitor is defined as

$$
C = \frac{Q}{U} .
$$
Capacitance depends only on the structure of the capacitor (the shape, size and relative position of the plates and the medium between them) and not on whether it is charged. Real capacitors (such as parallel-plate ones) are not completely closed, but when the plate separation is much smaller than the plate size, the field is concentrated between the plates and external influences can be neglected.

General procedure for finding the capacitance: let the plates carry $\pm Q$, find $\boldsymbol{D}$ and $\boldsymbol{E}$ from Gauss's law for $\boldsymbol{D}$, integrate to get $U = \int_+^-\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{l}$, and then find $C = Q/U$.

**Formula 4.4.1 (Capacitances of Common Capacitors)** With the space between the plates filled with a medium of relative permittivity $\varepsilon_{\mathrm{r}}$:

| Capacitor | Field | Capacitance |
|---|---|---|
| Parallel-plate (area $S$, separation $d$) | $E = \dfrac{Q}{\varepsilon_0\varepsilon_{\mathrm{r}}S}$ | $C = \dfrac{\varepsilon_0\varepsilon_{\mathrm{r}}S}{d}$ |
| Cylindrical (radii $R_1 < R_2$, length $L \gg R_2$) | $E = \dfrac{Q}{2\pi\varepsilon_0\varepsilon_{\mathrm{r}}Lr}$ | $C = \dfrac{2\pi\varepsilon_0\varepsilon_{\mathrm{r}}L}{\ln(R_2/R_1)}$ |
| Spherical (radii $R_1 < R_2$) | $E = \dfrac{Q}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2}$ | $C = \dfrac{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}R_1R_2}{R_2 - R_1}$ |

For the spherical capacitor, for example, $U = \displaystyle\int_{R_1}^{R_2}\frac{Q\,\mathrm{d}r}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}r^2} = \frac{Q}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}}\Big(\frac1{R_1} - \frac1{R_2}\Big)$, which gives the entry in the table. As $R_2 \to \infty$ it reduces to the capacitance of an isolated conducting sphere (times $\varepsilon_{\mathrm{r}}$); for $R_2 - R_1 = d \ll R_1$, $C \approx \varepsilon_0\varepsilon_{\mathrm{r}}\cdot4\pi R_1^2/d$, the parallel-plate formula. All three formulas show that filling with a dielectric increases the capacitance to $\varepsilon_{\mathrm{r}}$ times its vacuum value, the main reason for using dielectrics in capacitors (another is to raise the voltage rating).

The cell membrane is a biological example of this model: a lipid bilayer about $5\,\mathrm{nm}$ thick, with conducting solutions on both sides, forms a parallel-plate capacitor with a capacitance of about $1\,\mu\mathrm{F\,cm^{-2}}$ per unit area; the propagation of nerve impulses involves the charging and discharging of this capacitance (for RC circuits see [5.3.5](/5.3.5)).

### 4.4.3. Capacitors in Series and in Parallel

**Formula 4.4.2** For $n$ capacitors in parallel, the voltages are equal and the charges add; in series, the charges are equal (the intermediate plates acquire equal and opposite induced charges) and the voltages add:

$$
C_{\mathrm{par}} = \sum_{i=1}^nC_i,\qquad \frac{1}{C_{\mathrm{ser}}} = \sum_{i=1}^n\frac{1}{C_i} .
$$

Connecting in parallel increases the capacitance, but the voltage rating of the bank is limited by that of the capacitor with the lowest rating; connecting in series decreases the capacitance, but the total voltage is shared among the capacitors, so the bank can withstand a higher voltage than a single capacitor (the voltage divides as $U_i \propto 1/C_i$, and the smallest capacitance takes the largest voltage).

## 4.5. Electrostatic Energy in the Presence of Dielectrics

### 4.5.1. Energy Stored in a Capacitor

In charging a capacitor, an external agent (such as a source) moves charge from one plate to the other against the electric force, and this work is stored in the capacitor as **electrostatic energy**. At some instant of charging, the plates carry charge $q$ and voltage $u = q/C$; moving a further $\mathrm{d}q$ from the negative plate to the positive plate takes work $u\,\mathrm{d}q$ from the external force. Charging from $0$ to $Q$:

**Formula 4.5.1 (Energy of a Capacitor)**

$$
W = \int_0^Q\frac{q}{C}\,\mathrm{d}q = \frac{Q^2}{2C} = \frac12CU^2 = \frac12QU .
$$
In discharging, the work done by the electric force equals the decrease of this energy.

### 4.5.2. Energy Density

Take a parallel-plate capacitor, whose field between the plates is uniform, $U = Ed$, $C = \varepsilon S/d$:

$$
W = \frac12CU^2 = \frac12\frac{\varepsilon S}{d}(Ed)^2 = \frac12\varepsilon E^2\cdot(Sd) .
$$
$Sd$ is the volume occupied by the field, so the field energy per unit volume is $\frac12\varepsilon E^2 = \frac12ED$. This conclusion holds for general linear media (including anisotropic linear media):

**Formula 4.5.2 (Energy Density of the Electric Field)**

$$
w_{\mathrm{e}} = \frac12\boldsymbol{E}\cdot\boldsymbol{D},\qquad W = \int_V w_{\mathrm{e}}\,\mathrm{d}V = \int_V\frac12\boldsymbol{E}\cdot\boldsymbol{D}\,\mathrm{d}V .
$$
In an isotropic linear medium $w_{\mathrm{e}} = \frac12\varepsilon E^2$, and in vacuum $w_{\mathrm{e}} = \frac12\varepsilon_0E^2$, consistent with the result of [5.3.2](/5.3.2).

Compared with vacuum, the extra part in $w_{\mathrm{e}} = \frac12\varepsilon_0E^2 + \frac12\boldsymbol{E}\cdot\boldsymbol{P}$ is the work done in polarizing the medium: in a dielectric, not only does the field store energy, but energy is also absorbed and stored in the process of polarization.

**Example 4.5.1 (Conducting Sphere Half Immersed in Oil)** A conducting sphere of radius $R$ carries charge $Q$ and is half immersed in oil of relative permittivity $\varepsilon_{\mathrm{r}} = 3.0$, the other half being in air (take $\varepsilon_{\mathrm{r}} = 1$); the oil surface is an infinite plane through the center of the sphere. Find: (1) the free charges $Q_1$ and $Q_2$ on the upper hemisphere (in air) and the lower hemisphere (in oil); (2) the surface density of bound charge in the oil next to the lower hemisphere.

**Solution** (1) Method one: guess the solution and then use the **uniqueness theorem of electrostatics** to show it is the only one. In the presence of dielectrics, the conditions determining the solution include, besides the total charge and equipotential condition of the conductor, the shape, position and $\varepsilon_{\mathrm{r}}$ of the dielectric and the interface conditions at its boundary. Assume that the field is still spherically symmetric,

$$
\boldsymbol{E} = \frac{Q^*}{4\pi\varepsilon_0r^2}\boldsymbol{e}_r,
$$
where $Q^*$ is the sum of the free charge on the sphere and the bound charge adjacent to it (the same for both halves). This field satisfies: the conducting sphere is an equipotential body; at the air–oil interface $\boldsymbol{E}$ is radial and tangent to the interface, $E_{\mathrm{t}}$ is continuous and $D_{\mathrm{n}} = 0$ is continuous. The remaining condition is that the total charge of the sphere is $Q$. By Gauss's law for $\boldsymbol{D}$ on a concentric sphere enclosing the conductor,

$$
\varepsilon_0\frac{Q^*}{4\pi\varepsilon_0R^2}\cdot2\pi R^2 + \varepsilon_0\varepsilon_{\mathrm{r}}\frac{Q^*}{4\pi\varepsilon_0R^2}\cdot2\pi R^2 = Q
\quad\Longrightarrow\quad Q^* = \frac{2Q}{1 + \varepsilon_{\mathrm{r}}} .
$$
The free charge on the upper hemisphere equals the flux of $D$ through the upper hemisphere, and similarly for the lower hemisphere:

$$
Q_1 = \frac{Q^*}{2} = \frac{Q}{1 + \varepsilon_{\mathrm{r}}} = \frac{Q}{4},\qquad Q_2 = \frac{\varepsilon_{\mathrm{r}}Q^*}{2} = \frac{\varepsilon_{\mathrm{r}}Q}{1 + \varepsilon_{\mathrm{r}}} = \frac{3Q}{4} .
$$

Method two: the capacitance method. The upper and lower parts can be regarded as two "hemispherical capacitors" in parallel, with the conducting sphere and infinity as plates, with the same voltage. The capacitances of half an isolated conducting sphere are $C_1 = 2\pi\varepsilon_0R$ and $C_2 = 2\pi\varepsilon_0\varepsilon_{\mathrm{r}}R$, and the charge divides in proportion to capacitance: $Q_1 = \dfrac{C_1}{C_1 + C_2}Q = \dfrac{Q}{1 + \varepsilon_{\mathrm{r}}}$, the same as method one.

(2) In the oil next to the sphere, $\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E}$, and the normal of the medium surface points from the oil to the conductor, $\boldsymbol{e}_{\mathrm{n}} = -\boldsymbol{e}_r$:

$$
\sigma' = -\varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\frac{Q^*}{4\pi\varepsilon_0R^2} = -\frac{\varepsilon_{\mathrm{r}} - 1}{\varepsilon_{\mathrm{r}} + 1}\cdot\frac{Q}{2\pi R^2} = -\frac{Q}{4\pi R^2} .
$$
The total bound charge next to the lower hemisphere is $\sigma'\cdot2\pi R^2 = -\frac{\varepsilon_{\mathrm{r}} - 1}{\varepsilon_{\mathrm{r}} + 1}Q$, and its sum with $Q_2$ equals exactly $Q_1$: the total charge (free plus bound) on the two hemispheres is equal, which is why the field remains spherically symmetric.

## Summary

| Quantity or law | Expression | Remark |
|---|---|---|
| Polarization | $\boldsymbol{P} = \sum\boldsymbol{p}_i/\Delta V$ | Isotropic linear medium: $\boldsymbol{P} = \varepsilon_0(\varepsilon_{\mathrm{r}} - 1)\boldsymbol{E}$ |
| Bound charge | $q'_{\mathrm{enc}} = -\oint\boldsymbol{P}\cdot\mathrm{d}\boldsymbol{S}$, $\rho' = -\nabla\cdot\boldsymbol{P}$, $\sigma' = P_{\mathrm{n}}$ | $\boldsymbol{e}_{\mathrm{n}}$ points from the medium to the outside |
| Electric displacement | $\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P}$ | Isotropic linear medium: $\boldsymbol{D} = \varepsilon_0\varepsilon_{\mathrm{r}}\boldsymbol{E}$ |
| Gauss's law for $\boldsymbol{D}$ | $\oint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{S} = q_{0,\mathrm{enc}}$, $\nabla\cdot\boldsymbol{D} = \rho_0$ | Free charge only |
| Interface conditions | $D_{1\mathrm{n}} - D_{2\mathrm{n}} = \sigma_0$, $E_{1\mathrm{t}} = E_{2\mathrm{t}}$ | $\boldsymbol{e}_{\mathrm{n}}$ points from 2 to 1 |
| Capacitance | $C = Q/U$ | Depends only on structure; add in parallel, reciprocals add in series |
| Energy | $W = \frac{Q^2}{2C} = \frac12CU^2$, $w_{\mathrm{e}} = \frac12\boldsymbol{E}\cdot\boldsymbol{D}$ | Linear media |

## Questions

1. When the charges on the two plates of a capacitor are not equal and opposite (say $Q_1$ and $Q_2$), how is the capacitance computed from $C = Q/U$?

   **Answer** capacitance is a structural parameter independent of the charging state. For a parallel-plate capacitor, superposition gives the field between the plates $E = \frac{Q_1 - Q_2}{2\varepsilon_0S}$, which depends only on half the difference of the charges; with $Q = \frac{Q_1 - Q_2}{2}$ we still have $U = Q/C$. The same holds for unequal charges of the same sign: the extra $\frac{Q_1 + Q_2}{2}$ is distributed on the outer sides of the two plates and does not affect the voltage between them.

2. Use the circulation theorem for the electrostatic field to show that the field at the edge of a parallel-plate capacitor cannot drop abruptly from a uniform value to zero.

   **Answer** take a rectangular loop with one long side between the plates parallel to the field and the other outside, where the field is zero, and the two short sides perpendicular to the plates. If the field dropped abruptly to zero at the edge, the loop integral would equal $El \ne 0$, contradicting the circulation theorem. So there must be a fringing field that weakens gradually.

3. Why can the field inside a conductor be zero while the field inside a dielectric can be nonzero?

   **Answer** free charges in a conductor can move any distance and keep moving as long as there is a field inside, until the external field is canceled completely; bound charges in a dielectric are held in molecules and can only be displaced slightly, the degree of polarization is determined by the total field, and at equilibrium the total field is nonzero.

4. Does the circulation theorem for $\boldsymbol{E}$ hold in the presence of dielectrics? Must the loop integral of $\boldsymbol{D}$ vanish?

   **Answer** the circulation theorem for $\boldsymbol{E}$ holds because all the charges are stationary. The loop integral of $\boldsymbol{D}$ need not vanish: at the interface of two media $E_{\mathrm{t}}$ is continuous, so $D_{\mathrm{t}} = \varepsilon E_{\mathrm{t}}$ is discontinuous, and on a rectangular loop across the interface $\oint\boldsymbol{D}\cdot\mathrm{d}\boldsymbol{l} = (\varepsilon_1 - \varepsilon_2)E_{\mathrm{t}}\Delta l \ne 0$.
