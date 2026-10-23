---
title: Interfacial Phenomena and Surface Thermodynamics
source_hash: facd22fa027b
---

The systems treated in the preceding chapters tacitly assumed that the molecules at interfaces can be neglected: in a glass of water only about $10^{-8}$ of the molecules are at the surface. Once matter is highly dispersed, the situation is different: 1 g of water in the form of one sphere has a surface area of about $5\,\mathrm{cm^2}$ and a surface energy of about $3.5 \times 10^{-5}\,\mathrm{J}$; divided into droplets of radius $1\,\mathrm{nm}$, the surface area grows to about $3000\,\mathrm{m^2}$ and the surface energy to about $220\,\mathrm{J}$, enough to heat that 1 g of water by $50\,\mathrm{K}$. This chapter treats interfaces with the thermodynamics established earlier (the **fundamental equations of thermodynamics**, the **chemical potential** and the **Gibbs–Duhem equation**, [6.3.3](/6.3.3), [6.3.4](/6.3.4)): we first define the surface tension and write the fundamental equations including surface work (19.1); then discuss the additional pressure caused by curved interfaces, the changes of vapor pressure and solubility, and the metastable states and nucleation when a new phase forms (19.2); then follow the measurement of surface tension (19.3), adsorption at solution surfaces and the Gibbs adsorption isotherm (19.4), spreading and monolayers at liquid–liquid interfaces (19.5), wetting at solid–liquid interfaces (19.6), and finally surfactants and micelles (19.7). This chapter is the basis of the next two: a solid surface can lower its surface energy only by adsorption, which is the subject of [6.3.20](/6.3.20); colloids are dispersed systems with significant interfacial energy, treated in [6.3.21](/6.3.21). In biology, the lipid bilayer of the cell membrane, pulmonary surfactant, capillary action in plants and ice-nucleating proteins are all direct applications of the principles of this chapter.

## 19.1. Surface Tension and Surface Gibbs Free Energy

### 19.1.1. Interfaces and Specific Surface Area

**Definition 19.1.1** The transition layer between two phases is called an **interface**. When one of the phases is a gas it is customarily called a **surface**: liquid–gas and solid–gas are surfaces, while liquid–liquid, liquid–solid and solid–solid are interfaces. The surface area per unit mass (or unit volume) of a substance is called the **specific surface area**:

$$
a_{\mathrm{s}} = \frac{A_{\mathrm{s}}}{m} \quad\text{or}\quad a_{\mathrm{s}} = \frac{A_{\mathrm{s}}}{V}.
$$

An interfacial layer is not a surface in the geometric sense but a layer a few molecules thick, in which properties (density, composition, molecular orientation) change continuously from one phase to the other. For a cube of edge $l$ the specific surface area per volume is $a_{\mathrm{s}} = 6/l$, inversely proportional to the linear size: cutting a cube of edge $1\,\mathrm{cm}$ into small cubes of edge $1\,\mathrm{nm}$ increases the specific surface area by a factor of $10^7$. The more highly dispersed a system is (colloids, porous solids, nanomaterials, membrane structures inside cells), the less the contribution of its interfaces can be neglected. The specific surface areas of activated carbon, silica gel and molecular sieves can reach hundreds to thousands of square meters per gram.

### 19.1.2. Surface Work and Surface Tension

A molecule in the interior of a liquid is attracted by the surrounding molecules, and the forces in all directions cancel on average; a molecule in the surface layer is attracted far more strongly from the liquid side than from the gas side, and the resultant force points into the liquid. To move a molecule from the interior to the surface, work must therefore be done against this asymmetric force field, and surface molecules have a higher energy than interior molecules. Macroscopically, a liquid always tends to contract its surface: small droplets are spherical, and a liquid surface is flat in the absence of external forces.

**Definition 19.1.2** The non-volume work done on the system by the surroundings when the surface area is increased reversibly by $\mathrm{d}A_{\mathrm{s}}$ at constant temperature, pressure and composition is called the **surface work**; it is proportional to the increment of area:

$$
\delta W' = \gamma\,\mathrm{d}A_{\mathrm{s}}.
$$

The proportionality coefficient $\gamma$ is the reversible work required to increase the area by one unit, with unit $\mathrm{J\,m^{-2}}$. It also has a mechanical meaning. Dip a metal frame with a sliding crossbar (of length $l$) into a liquid to obtain a liquid film; the film has two surfaces, front and back, and an external force $F$ must be applied to keep the crossbar in equilibrium. Pulling the crossbar out reversibly by $\mathrm{d}x$ increases the surface area by $\mathrm{d}A_{\mathrm{s}} = 2l\,\mathrm{d}x$, and the external force does work $F\,\mathrm{d}x = \gamma \cdot 2l\,\mathrm{d}x$, so $F = 2\gamma l$: there is a contracting force of magnitude $\gamma$ per unit length of the boundary of the surface.

**Definition 19.1.3 (Surface Tension)** The force $\gamma$ per unit length, acting within the liquid surface perpendicular to any boundary line and tending to contract the surface, is called the **surface tension**, with unit $\mathrm{N\,m^{-1}}$. The same quantity between two phases is called the interfacial tension and denoted $\gamma_{\mathrm{lg}}$, $\gamma_{\mathrm{sl}}$, $\gamma_{\mathrm{sg}}$, $\gamma_{\mathrm{ll}}$ and so on.

$\mathrm{J\,m^{-2}} = \mathrm{N\,m^{-1}}$: the surface tension and the reversible work of increasing a unit area are two descriptions of the same quantity, one in terms of force and the other in terms of energy. [5.1.2](/5.1.2) introduced surface tension as a contact force and used it to compute the pressure difference between the inside and outside of a soap bubble; this chapter starts from energy, which allows us to bring it into thermodynamics. For a solid, the surface area can be increased by stretching the existing surface (changing the interatomic distances) or by forming new surface, and the work required differs for the two (the former is called surface stress), so "surface tension equals surface energy" holds strictly only for liquids.

### 19.1.3. Fundamental Equations of Thermodynamics Including Surface Work

Surface work is a kind of non-volume work. For a multicomponent system with variable interfacial area, the **fundamental equations of thermodynamics** ([6.3.4](/6.3.4)) acquire an extra term $\gamma\,\mathrm{d}A_{\mathrm{s}}$:

$$
\begin{aligned}
\mathrm{d}U &= T\,\mathrm{d}S - p\,\mathrm{d}V + \gamma\,\mathrm{d}A_{\mathrm{s}} + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}H &= T\,\mathrm{d}S + V\,\mathrm{d}p + \gamma\,\mathrm{d}A_{\mathrm{s}} + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, \\
\mathrm{d}A &= -S\,\mathrm{d}T - p\,\mathrm{d}V + \gamma\,\mathrm{d}A_{\mathrm{s}} + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}G &= -S\,\mathrm{d}T + V\,\mathrm{d}p + \gamma\,\mathrm{d}A_{\mathrm{s}} + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}.
\end{aligned}
$$

Thus $\gamma$ can be written as the partial derivative of four characteristic functions with respect to area, $\gamma = (\partial U/\partial A_{\mathrm{s}})_{S,V,n} = (\partial H/\partial A_{\mathrm{s}})_{S,p,n} = (\partial A/\partial A_{\mathrm{s}})_{T,V,n} = (\partial G/\partial A_{\mathrm{s}})_{T,p,n}$. The last is the most commonly used in chemistry.

**Definition 19.1.4** At constant temperature, pressure and composition, the rate of change of the Gibbs free energy of the system with the interfacial area,

$$
\gamma = \left(\frac{\partial G}{\partial A_{\mathrm{s}}}\right)_{T,p,n_{\mathrm{B}}}
$$
is called the **specific surface Gibbs free energy**: the excess Gibbs free energy of the molecules per unit interfacial area over the same number of molecules in the bulk phase.

From $\mathrm{d}G = \gamma\,\mathrm{d}A_{\mathrm{s}}$ (constant temperature, pressure and composition), an interface changes spontaneously in the direction in which $\gamma A_{\mathrm{s}}$ decreases: a pure liquid can only reduce its area $A_{\mathrm{s}}$, a solution can also reduce $\gamma$ by changing the composition of the surface layer (19.4), and a solid does so mainly by adsorbing foreign molecules ([6.3.20](/6.3.20)).

### 19.1.4. Factors Affecting Surface Tension

Consider temperature first. From the equality of the mixed partial derivatives of $\mathrm{d}G$ (a Maxwell relation),

$$
\left(\frac{\partial S}{\partial A_{\mathrm{s}}}\right)_{T,p,n} = -\left(\frac{\partial \gamma}{\partial T}\right)_{A_{\mathrm{s}},p,n}.
$$

The left-hand side is the increase of the entropy of the system when a unit area is created (the surface entropy). The molecules of the surface layer are arranged more loosely than in the bulk, so the surface entropy is positive, and the surface tension of almost all liquids decreases with increasing temperature; as the temperature approaches the critical temperature the difference between the two phases disappears and $\gamma \to 0$. When a unit area is created isothermally and reversibly, the system absorbs heat $T(\partial S/\partial A_{\mathrm{s}})$; the surface enthalpy per unit area $h^\sigma = \gamma - T(\partial\gamma/\partial T)$ is greater than $\gamma$, which is just the **Gibbs–Helmholtz equation** applied to a surface.

**Example 19.1.1** At $25\,{}^\circ\mathrm{C}$, water has $\gamma = 71.99\,\mathrm{mN\,m^{-1}}$ and $\mathrm{d}\gamma/\mathrm{d}T \approx -0.15\,\mathrm{mN\,m^{-1}\,K^{-1}}$. The surface entropy is $s^\sigma = 0.15\,\mathrm{mJ\,m^{-2}\,K^{-1}}$; when $1\,\mathrm{m^2}$ of water surface is created isothermally and reversibly, the system absorbs heat $Ts^\sigma = 45\,\mathrm{mJ}$, the surroundings do work $72\,\mathrm{mJ}$, and the surface enthalpy is $h^\sigma = 72 + 45 = 117\,\mathrm{mJ\,m^{-2}}$. If the surface is enlarged adiabatically, the liquid cools.

Far from the critical point the variation of surface tension with temperature is approximately linear. For nonassociated liquids there is an empirical rule:

**Formula 19.1.1 (Eötvös Rule)** $\gamma V_{\mathrm{m}}^{2/3} = k(T_{\mathrm{c}} - T)$, where $V_{\mathrm{m}}$ is the molar volume of the liquid, $T_{\mathrm{c}}$ the critical temperature, and the constant $k \approx 2.1 \times 10^{-7}\,\mathrm{J\,K^{-1}\,mol^{-2/3}}$ is approximately the same for most nonpolar liquids. Ramsay and Shields improved it to $\gamma V_{\mathrm{m}}^{2/3} = k(T_{\mathrm{c}} - T - 6\,\mathrm{K})$.

$\gamma V_{\mathrm{m}}^{2/3}$ is the surface Gibbs free energy "when one mole of molecules is spread out as a monolayer", and the Eötvös rule says that it grows linearly with $T_{\mathrm{c}} - T$ with a substance-independent proportionality constant; this is a manifestation of the **principle of corresponding states** ([6.3.1](/6.3.1)) for surface properties. For example for benzene at $20\,{}^\circ\mathrm{C}$, $\gamma = 28.9\,\mathrm{mN\,m^{-1}}$, $V_{\mathrm{m}} = 89.4\,\mathrm{cm^3\,mol^{-1}}$ and $T_{\mathrm{c}} = 562\,\mathrm{K}$, and the Ramsay–Shields formula gives $k = 2.2 \times 10^{-7}\,\mathrm{J\,K^{-1}\,mol^{-2/3}}$. Associated liquids such as water and alcohols have distinctly smaller $k$.

The effect of pressure follows from $\mathrm{d}G$: $(\partial\gamma/\partial p)_{T,A_{\mathrm{s}},n} = (\partial V/\partial A_{\mathrm{s}})_{T,p,n}$, which is very small for nearly incompressible liquids. In experiments, $\gamma$ decreases slightly when pressure is applied with an inert gas, mainly as a result of adsorption and dissolution of the gas at the surface and not an effect of pressure itself.

The effect of composition is large, see 19.4.

Finally, surface tension reflects the attraction that must be overcome to bring a molecule to the surface, so it is consistent with the strength of the intermolecular forces: metallic bonds > ionic bonds > polar molecules (**hydrogen bonds**) > nonpolar molecules (**dispersion forces**). The table below gives data near $20\,{}^\circ\mathrm{C}$ (CRC Handbook):

| Liquid | $\gamma/(\mathrm{mN\,m^{-1}})$ | Interface | $\gamma/(\mathrm{mN\,m^{-1}})$ |
|---|---|---|---|
| Mercury ($25\,{}^\circ\mathrm{C}$) | 485 | Water–mercury | 375 |
| Water | 72.8 | Water–$n$-hexane | 51.1 |
| Glycerol | 63.4 | Water–benzene | 35.0 |
| Benzene | 28.9 | Water–$n$-octanol | 8.5 |
| Ethanol | 22.4 | Water–diethyl ether | 10.7 |
| $n$-Hexane | 18.4 | | |

The interfacial tension between two liquids lies between their surface tensions and depends on the difference in polarity: the interfacial tensions of water with $n$-octanol and with diethyl ether are small because the polar groups of the latter can extend into the aqueous phase. For two partially miscible liquids there is an empirical rule:

**Formula 19.1.2 (Antonoff Rule)** The interfacial tension between two liquids is approximately the difference of their surface tensions after mutual saturation: $\gamma_{12} = \lvert\gamma'_1 - \gamma'_2\rvert$.

It holds approximately for many organic liquid–water systems, but is not a general law (it often fails for systems containing surface-active components).

## 19.2. Curved Surfaces

### 19.2.1. Additional Pressure and the Young–Laplace Equation

On a flat liquid surface the surface tension acts along the surface, the pulls from all around cancel, and the pressures on the two sides of the surface are equal. When the surface is curved, the surface tensions at the boundary no longer lie in one plane, and the resultant force points to the concave side (the side of the center of curvature), making the pressure on the concave side higher than on the convex side.

**Definition 19.2.1** The pressure difference across a curved interface, $\Delta p = p_{\text{concave}} - p_{\text{convex}}$, is called the **additional pressure** (Laplace pressure).

**Theorem 19.2.1 (Young–Laplace Equation)** Let the two principal radii of curvature of the interface at a point be $r_1$ and $r_2$ (taken positive when measured from the concave side). Then

$$
\Delta p = \gamma\left(\frac{1}{r_1} + \frac{1}{r_2}\right). \tag{19.1}
$$
For a spherical surface of radius $r$, $\Delta p = 2\gamma/r$.

**Proof** Take a small rectangle on the surface with sides $x$ and $y$, with the **radius of curvature** of the arcs in the two orthogonal sections containing the sides being $r_1$ and $r_2$. Displace the surface along the normal toward the convex side by $\mathrm{d}z$; by similar triangles $x$ becomes $x(1 + \mathrm{d}z/r_1)$ and $y$ becomes $y(1 + \mathrm{d}z/r_2)$, and the increment of area is

$$
\mathrm{d}A_{\mathrm{s}} = xy\left(\frac{1}{r_1} + \frac{1}{r_2}\right)\mathrm{d}z.
$$
The volume on the concave side increases by $\mathrm{d}V = xy\,\mathrm{d}z$. At equilibrium the work done by the pressure difference in moving the interface equals the increment of the surface Gibbs free energy, $\Delta p\,\mathrm{d}V = \gamma\,\mathrm{d}A_{\mathrm{s}}$, and substitution gives Eq. (19.1). For a sphere one can also use $A_{\mathrm{s}} = 4\pi r^2$ and $V = \frac{4}{3}\pi r^3$ directly: $\Delta p = \gamma\,\mathrm{d}A_{\mathrm{s}}/\mathrm{d}V = \gamma \cdot 8\pi r/(4\pi r^2) = 2\gamma/r$. $\square$

Some remarks:

- The additional pressure always points to the center of curvature. The pressure inside a small droplet (a convex surface) is higher than the external pressure, $p_{\text{in}} = p_{\text{out}} + 2\gamma/r$; below a concave meniscus in a capillary the pressure of the liquid is lower than the external pressure. One often takes $r$ positive for a convex surface and negative for a concave one and writes uniformly $p_{\text{liq}} = p_{\text{out}} + 2\gamma/r$.
- The liquid film of a soap bubble has two surfaces, inner and outer, and $\Delta p = 4\gamma/r$. When two soap bubbles of different sizes are connected, the pressure in the smaller one is higher and gas flows to the larger one; the small bubble keeps shrinking until it becomes a spherical cap with the same curvature as the large bubble; this is also why blowing up a balloon is hardest at the start.
- For a plane $r_1 = r_2 = \infty$ and $\Delta p = 0$; for a cylindrical surface $r_2 = \infty$ and $\Delta p = \gamma/r_1$. $1/r_1 + 1/r_2$ is twice the mean curvature of the surface, and in the absence of gravity the mean curvature of an equilibrium interface is the same everywhere; a droplet takes a spherical shape precisely because the sphere has the smallest surface area for a given volume.

**Example 19.2.1** At room temperature water has $\gamma = 72.8\,\mathrm{mN\,m^{-1}}$. For a water drop of radius $1\,\mathrm{mm}$, $\Delta p = 2\gamma/r = 146\,\mathrm{Pa}$; for $r = 10\,\mu\mathrm{m}$, $\Delta p = 14.6\,\mathrm{kPa} \approx 0.15\,p^\circ$; for $r = 10\,\mathrm{nm}$, $\Delta p = 14.6\,\mathrm{MPa} \approx 146\,p^\circ$. The additional pressure of millimeter-sized drops can be neglected, but in nanometer-sized particles it can reach a hundred times the standard pressure, and many properties of liquids and solids change as a result (19.2.3, 19.2.4).

An alveolus is an air sac about $0.2\,\mathrm{mm}$ in diameter whose inner wall is covered with a liquid layer. If the surface tension of this liquid were close to that of plasma (about $50\,\mathrm{mN\,m^{-1}}$), the additional pressure of an alveolus of radius $0.1\,\mathrm{mm}$ would be about $1\,\mathrm{kPa}$, which inhalation would have to overcome additionally, and small alveoli, having a higher pressure, would also expel gas into larger ones and collapse. Pulmonary surfactant (a lipoprotein complex consisting mainly of dipalmitoylphosphatidylcholine) spreads over the liquid surface; on exhalation the alveolus shrinks and the film is compressed, and the surface tension can fall to nearly zero, keeping alveoli of different sizes stable. Premature infants lacking this substance develop respiratory distress syndrome, and one treatment is to supply surfactant to the lungs (for monolayers see 19.5.3).

### 19.2.2. Capillarity

Insert a capillary of radius $R$ into a liquid. If the liquid wets the wall (contact angle $\theta < 90^\circ$, 19.6), the liquid surface in the tube is concave and the pressure below it is lower than that below the liquid surface outside the tube at the same height, so the liquid rises along the tube until the hydrostatic pressure of the liquid column cancels the additional pressure; if it does not wet ($\theta > 90^\circ$), the surface is convex and the liquid falls. This phenomenon in which the additional pressure of a curved liquid surface causes a difference of liquid level inside and outside the tube is called *capillarity*.

Let the concave surface be a spherical surface of radius $r$; the geometry gives $r = R/\cos\theta$. At equilibrium $\Delta p = 2\gamma/r = \Delta\rho\,gh$, where $\Delta\rho = \rho_{\mathrm{l}} - \rho_{\mathrm{g}} \approx \rho_{\mathrm{l}}$, and therefore

$$
h = \frac{2\gamma\cos\theta}{\Delta\rho\,gR}.
$$

The height of rise is inversely proportional to the tube radius (Jurin's law). For $\theta < 90^\circ$, $h > 0$, and for $\theta > 90^\circ$, $h < 0$ (mercury falls in a glass tube).

**Example 19.2.2** Water at $20\,{}^\circ\mathrm{C}$ ($\gamma = 72.8\,\mathrm{mN\,m^{-1}}$, $\rho = 998\,\mathrm{kg\,m^{-3}}$, $\theta \approx 0$) rises in a clean glass tube of inner radius $0.1\,\mathrm{mm}$ by $h = 2 \times 0.0728/(998 \times 9.81 \times 10^{-4})\,\mathrm{m} = 0.149\,\mathrm{m}$.

The fine pores in soil form a network of capillaries along which groundwater rises to the surface layer and evaporates; hoeing cuts the capillaries of the surface layer and reduces water loss, which is the principle of "hoeing to conserve soil moisture". The xylem vessels of plants have radii of about $10$–$100\,\mu\mathrm{m}$, and capillary action can lift water only tens of centimeters to a little more than a meter; water transport in tall trees depends mainly on the negative pressure created in the water column by transpiration from the leaves (the cohesion–tension theory), but the menisci in the nanometer-sized pores of the mesophyll cell walls can bear such negative pressure, again by virtue of the Young–Laplace equation: the finer the pore, the larger the pressure difference the meniscus can support.

### 19.2.3. The Kelvin Equation

The pressure inside a small droplet is higher than that of the liquid below a flat surface, and the **chemical potential** of a liquid increases with pressure ($(\partial\mu/\partial p)_T = V_{\mathrm{m}}$), so a small droplet evaporates more easily and its saturated vapor pressure is higher than that of a flat surface.

**Theorem 19.2.2 (Kelvin Equation)** At temperature $T$, the ratio of the saturated vapor pressure $p_r$ of a droplet of radius $r$ to the saturated vapor pressure $p^*$ of a flat surface is

$$
\ln\frac{p_r}{p^*} = \frac{2\gamma V_{\mathrm{m}}}{RTr} = \frac{2\gamma M}{\rho RTr}, \tag{19.2}
$$
where $V_{\mathrm{m}}$, $M$ and $\rho$ are the molar volume, molar mass and density of the liquid. For a convex surface $r > 0$ and $p_r > p^*$; for a concave surface (such as a wetting meniscus in a capillary or a gas bubble in a liquid) $r < 0$ and $p_r < p^*$.

**Proof** Method 1 (a designed path). Compare two processes: (1) the liquid with a flat surface evaporates into vapor at $p^*$, $\Delta G_1 = 0$; (2) a small droplet evaporates at its saturated vapor pressure $p_r$, $\Delta G_2 = 0$. Transferring 1 mol of liquid from the flat surface into the small droplet increases the pressure on the liquid by $2\gamma/r$, $\Delta G = \int V_{\mathrm{m}}\,\mathrm{d}p = 2\gamma V_{\mathrm{m}}/r$ (the liquid is incompressible); changing 1 mol of ideal gas from $p_r$ to $p^*$ gives $\Delta G = RT\ln(p^*/p_r)$. The four steps form a cycle with total $\Delta G = 0$, that is, $2\gamma V_{\mathrm{m}}/r + RT\ln(p^*/p_r) = 0$.

Method 2 (equality of chemical potentials). When a droplet is in equilibrium with its vapor, the pressure inside the droplet is $p_r + 2\gamma/r$ and the equilibrium condition is $\mu_{\mathrm{l}}(T, p_r + 2\gamma/r) = \mu_{\mathrm{g}}(T, p_r)$; for a flat surface in equilibrium with vapor $\mu_{\mathrm{l}}(T, p^*) = \mu_{\mathrm{g}}(T, p^*)$. Subtracting the two,


$$
V_{\mathrm{m}}\left(p_r - p^* + \frac{2\gamma}{r}\right) = RT\ln\frac{p_r}{p^*}.
$$
The term $V_{\mathrm{m}}(p_r - p^*)$ on the left-hand side is exactly the effect of external pressure on vapor pressure in [6.3.8](/6.3.8#sec-8.3.4), which is negligible compared with $2\gamma V_{\mathrm{m}}/r$, and Eq. (19.2) follows. $\square$

**Example 19.2.3** For water at $25\,{}^\circ\mathrm{C}$, $2\gamma V_{\mathrm{m}}/(RT) = 2 \times 0.0720 \times 1.807 \times 10^{-5}/(8.314 \times 298.15)\,\mathrm{m} = 1.05\,\mathrm{nm}$.

| $r/\mathrm{nm}$ | 1000 | 100 | 10 | 1 | $-10$ (concave) |
|---|---|---|---|---|---|
| $p_r/p^*$ | 1.001 | 1.011 | 1.11 | 2.86 | 0.90 |

The effect becomes significant only for radii below about $10\,\mathrm{nm}$; a "droplet" of $r = 1\,\mathrm{nm}$ contains only about 140 molecules, the macroscopic $\gamma$ is no longer fully applicable, and the Kelvin equation gives only the order of magnitude.

The Kelvin equation also holds for volatile solids ($\gamma$ replaced by $\gamma_{\mathrm{sg}}$): fine particles of iodine or camphor sublime faster. The vapor pressure over a concave surface is lower than over a flat surface, so in a porous solid the vapor can condense in fine pores below the saturated vapor pressure; this is **capillary condensation** ([6.3.20](/6.3.20)) and is one reason why fine-pored silica gel can take up water from unsaturated air.

### 19.2.4. Solubility and Melting Point of Small Particles

The smaller a solid particle, the larger the additional pressure inside it and the higher the chemical potential of the substance in it, so its solubility is larger and its melting point lower.

**Theorem 19.2.3 (Ostwald–Freundlich Equation)** For an ideal solution (or ideal dilute solution), the ratio of the solubility $x_r$ of a crystal particle of radius $r$ to the solubility $x_\infty$ of a bulk crystal is

$$
\ln\frac{x_r}{x_\infty} = \frac{2\gamma_{\mathrm{sl}}V_{\mathrm{m}}(\mathrm{s})}{RTr},
$$
where $\gamma_{\mathrm{sl}}$ is the solid–liquid interfacial tension and $V_{\mathrm{m}}(\mathrm{s})$ the molar volume of the solid.

**Proof** At solubility equilibrium the chemical potential of B in the solid equals that of B in solution. For the particle, $\mu_{\mathrm{B}}(\mathrm{s}, T, p + 2\gamma_{\mathrm{sl}}/r) = \mu_{\mathrm{B}}^*(\mathrm{l}, T, p) + RT\ln x_r$; for the bulk crystal, $\mu_{\mathrm{B}}(\mathrm{s}, T, p) = \mu_{\mathrm{B}}^*(\mathrm{l}, T, p) + RT\ln x_\infty$. Subtracting, the difference on the left is $V_{\mathrm{m}}(\mathrm{s}) \cdot 2\gamma_{\mathrm{sl}}/r$, which gives the result. $\square$

For $\gamma_{\mathrm{sl}} \approx 0.1\,\mathrm{J\,m^{-2}}$ and $V_{\mathrm{m}}(\mathrm{s}) = 50\,\mathrm{cm^3\,mol^{-1}}$, $2\gamma_{\mathrm{sl}}V_{\mathrm{m}}/(RT) = 4.0\,\mathrm{nm}$ at $25\,{}^\circ\mathrm{C}$: the solubility of particles of radius $10\,\mathrm{nm}$ is about 1.5 times that of a large crystal, and that of particles of radius $1\,\mu\mathrm{m}$ is larger by only 0.4%. Hence when freshly precipitated particles are of unequal size, the small particles dissolve and the large ones grow, and the precipitate becomes coarser on "aging", which makes filtration easier; the aging of sols (**Ostwald ripening**, [6.3.21](/6.3.21)) has the same cause. The form $V_{\mathrm{m}}(\mathrm{s})/r$ is the same as in the Kelvin equation; the two are manifestations of the same physical effect in different equilibria.

**Theorem 19.2.4 (Gibbs–Thomson Equation)** The melting point $T_{\mathrm{m}}(r)$ of a solid particle of radius $r$ and the melting point $T_{\mathrm{m}}$ of the bulk solid satisfy

$$
\ln\frac{T_{\mathrm{m}}(r)}{T_{\mathrm{m}}} = -\frac{2\gamma_{\mathrm{sl}}V_{\mathrm{m}}(\mathrm{s})}{\Delta_{\mathrm{fus}}H_{\mathrm{m}}\,r},
$$
that is, $\Delta T_{\mathrm{m}}/T_{\mathrm{m}} \approx -2\gamma_{\mathrm{sl}}V_{\mathrm{m}}(\mathrm{s})/(\Delta_{\mathrm{fus}}H_{\mathrm{m}}\,r)$: the smaller the particle, the lower the melting point.

**Proof** A particle is in equilibrium with its melt: $\mu(\mathrm{s}, T, p + 2\gamma_{\mathrm{sl}}/r) = \mu(\mathrm{l}, T, p)$. At constant external pressure, let $r$ vary; the equilibrium temperature varies with it, and the differentials of the two sides are equal: $-S_{\mathrm{m}}(\mathrm{s})\,\mathrm{d}T + V_{\mathrm{m}}(\mathrm{s})\,\mathrm{d}(2\gamma_{\mathrm{sl}}/r) = -S_{\mathrm{m}}(\mathrm{l})\,\mathrm{d}T$, that is, $\Delta_{\mathrm{fus}}S_{\mathrm{m}}\,\mathrm{d}T = -V_{\mathrm{m}}(\mathrm{s})\,\mathrm{d}(2\gamma_{\mathrm{sl}}/r)$. Substituting $\Delta_{\mathrm{fus}}S_{\mathrm{m}} = \Delta_{\mathrm{fus}}H_{\mathrm{m}}/T$, neglecting the temperature dependence of $\gamma_{\mathrm{sl}}$ and $\Delta_{\mathrm{fus}}H_{\mathrm{m}}$, and integrating from $r = \infty$ ($T = T_{\mathrm{m}}$) to $r$ gives the result. $\square$

For gold, $\gamma_{\mathrm{sl}} \approx 0.27\,\mathrm{J\,m^{-2}}$, $V_{\mathrm{m}} = 10.2\,\mathrm{cm^3\,mol^{-1}}$, $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 12.55\,\mathrm{kJ\,mol^{-1}}$ and $T_{\mathrm{m}} = 1337\,\mathrm{K}$; the melting point of a gold particle of radius $2\,\mathrm{nm}$ is estimated to be lowered by two or three hundred kelvins, consistent in order of magnitude with the results measured by Buffat and Borel (1976) with electron diffraction. The lowering of the melting point is one reason why nanomaterials sinter easily and why their properties vary with size. The same relation also explains the lowering of the freezing point of liquids in porous media: water in silica-gel channels a few nanometers wide freezes only below $-10\,{}^\circ\mathrm{C}$ (thermoporometry determines pore sizes from this melting-point depression).

### 19.2.5. Metastable States and Nucleation

A phase transition always produces a new phase, and the new phase is initially always an extremely small particle: condensation of vapor starts from tiny droplets, boiling of a liquid from tiny bubbles, and crystallization from tiny nuclei. By 19.2.3 and 19.2.4 the chemical potential of these small particles is higher than that of the bulk new phase, so under normal phase-transition conditions the new phase cannot appear, and the system can cross the phase-equilibrium line and remain in the original phase. Such a state is called a metastable state; the supersaturated vapor and superheated liquid on the van der Waals isotherm in physics are already examples ([5.2.2](/5.2.2#sec-2.2)).

- Supersaturated vapor: the pressure of the vapor already exceeds the saturated vapor pressure over a flat surface but is still lower than the vapor pressure of the small droplets that form first, and condensation cannot begin. Dust, ions or larger droplets in the air can serve as condensation nuclei; artificial rain-making seeds a supersaturated cloud layer with silver iodide or dry ice to supply condensation nuclei or to freeze the water vapor.
- Superheated liquid: for a bubble to form inside the liquid, the vapor pressure in the bubble must reach $p_{\text{out}} + 2\gamma/r$ (plus the hydrostatic pressure of the liquid column), while the vapor pressure over a concave surface is according to the Kelvin equation even lower, so the liquid cannot boil even at the normal boiling point. By the **Clausius–Clapeyron equation** the liquid must be heated to a higher temperature before its vapor pressure reaches this value, and once a bubble forms it vaporizes violently (bumping). Adding boiling chips or a capillary supplies ready-made bubble nuclei.
- Supercooled liquid (**supercooling**, [6.1.1](/6.1.1)): by the Gibbs–Thomson equation the melting point of small nuclei is lower than the normal freezing point, and when the temperature falls to the freezing point the nuclei still cannot exist stably. Pure water can be supercooled to about $-40\,{}^\circ\mathrm{C}$ (experiments report values between $-38$ and $-46\,{}^\circ\mathrm{C}$, depending on droplet size and cooling rate) before homogeneous freezing occurs.
- Supersaturated solution: similarly, by the Ostwald–Freundlich equation a solution must be supersaturated to a certain degree before crystals precipitate.

Metastable states are a hysteresis of phase transitions, and the common cause is that creating a new phase first requires paying the energy of the new interface. This can be shown quantitatively with the Gibbs free energy.

**Definition 19.2.2** The process in which crystal nuclei of a new phase form spontaneously inside a uniform metastable phase through fluctuations of thermal motion is called **homogeneous nucleation**; the process in which nuclei form on container walls, impurity particles or existing interfaces is called **heterogeneous nucleation**.

Suppose a spherical nucleus of radius $r$ forms in a liquid with supercooling $\Delta T$. The bulk part lowers the Gibbs free energy by $\lvert\Delta G_V\rvert$ per unit volume of new phase, where $\Delta G_V = \Delta_{\mathrm{trs}}G_{\mathrm{m}}/V_{\mathrm{m}} \approx -\Delta_{\mathrm{fus}}H_{\mathrm{m}}\Delta T/(T_{\mathrm{m}}V_{\mathrm{m}}) < 0$ (the molar Gibbs free energy change of freezing of the supercooled liquid divided by the molar volume of the new phase; the entropy change of freezing of supercooled water was computed in [6.3.2](/6.3.2)); the new interface raises the Gibbs free energy by $4\pi r^2\gamma_{\mathrm{sl}}$. Therefore

$$
\Delta G(r) = 4\pi r^2\gamma_{\mathrm{sl}} + \frac{4}{3}\pi r^3\Delta G_V.
$$

**Theorem 19.2.5 (Critical Radius)** $\Delta G(r)$ has a maximum at the critical radius

$$
r_{\mathrm{c}} = \frac{2\gamma_{\mathrm{sl}}}{\lvert\Delta G_V\rvert}
$$
with the value $\Delta G^* = \dfrac{16\pi\gamma_{\mathrm{sl}}^3}{3\Delta G_V^2} = \dfrac{1}{3}\cdot 4\pi r_{\mathrm{c}}^2\gamma_{\mathrm{sl}}$. The growth of a nucleus with $r < r_{\mathrm{c}}$ increases $\Delta G$, so it tends to redissolve; the growth of a nucleus with $r > r_{\mathrm{c}}$ decreases $\Delta G$, and it can grow spontaneously.

**Proof** Set $\mathrm{d}\Delta G/\mathrm{d}r = 8\pi r\gamma_{\mathrm{sl}} + 4\pi r^2\Delta G_V = 0$, which gives $r_{\mathrm{c}} = -2\gamma_{\mathrm{sl}}/\Delta G_V$, and substitution back gives $\Delta G^*$; $\mathrm{d}^2\Delta G/\mathrm{d}r^2 = 8\pi\gamma_{\mathrm{sl}} + 8\pi r\Delta G_V$ equals $-8\pi\gamma_{\mathrm{sl}} < 0$ at $r_{\mathrm{c}}$, so this is a maximum. $\square$

$r_{\mathrm{c}}$ is exactly the radius of a nucleus whose melting point, according to the Gibbs–Thomson equation, equals the present temperature: the critical nucleus is in unstable equilibrium with the liquid. $\Delta G^*$ is the energy barrier of nucleation, and according to classical nucleation theory the number of critical nuclei formed per unit volume and unit time is $J = J_0\exp(-\Delta G^*/k_{\mathrm{B}}T)$. Since $\Delta G^* \propto 1/\Delta T^2$, the nucleation rate rises sharply from almost zero near a certain supercooling, which is why homogeneous nucleation has a fairly definite "limit of supercooling".

![Gibbs free energy of forming a spherical ice nucleus in supercooled water as a function of radius, for supercoolings of 10, 20 and 40 K (γsl = 0.030 J/m²). The maxima, marked by dots, lie at the critical radius rc = 2γsl/|ΔGV|; as the supercooling increases both rc and the barrier height fall sharply](./plots/nucleation.py)

In heterogeneous nucleation the nucleus attaches to a solid surface in the shape of a spherical cap (contact angle $\theta$, 19.6), the area of new interface needed is reduced, and the barrier falls to $\Delta G^*_{\text{het}} = \Delta G^* f(\theta)$ with $f(\theta) = \frac{1}{4}(2 + \cos\theta)(1 - \cos\theta)^2 \le 1$; surfaces that the new phase can wet (small $\theta$) are effective nucleating agents. The crystal lattice of silver iodide is close to that of ice, and it is a very good ice nucleus; the outer membrane of some bacteria (such as *Pseudomonas syringae*) carries ice-nucleating proteins that make water freeze at about $-2\,{}^\circ\mathrm{C}$, thereby injuring plant tissue. Conversely, the antifreeze proteins of polar fishes and insects adsorb on the surface of ice crystals, so that ice can grow only between the adsorption sites with highly curved interfaces; by the Gibbs–Thomson equation such ice crystals have a lower melting point, and the growth of the ice crystals is thus inhibited. Adding seed crystals in industrial crystallization and rubbing the wall of a vessel with a glass rod in the laboratory both provide sites for heterogeneous nucleation.

## 19.3. Measurement of Surface Tension

The measurement methods fall into two classes: static methods, which measure the equilibrium surface tension, and dynamic methods, which measure the variation of the surface tension of a newly formed surface with time (important for surfactant solutions, since surface adsorption takes time). The commonly used methods are as follows:

| Method | Principle | Formula | Remarks |
|---|---|---|---|
| Capillary rise | The hydrostatic pressure of the liquid column balances the additional pressure | $\gamma = \frac{1}{2}\Delta\rho\,gRh$ ($\theta = 0$) | One of the most accurate methods; the liquid surface is not exactly a hemisphere, and the Rayleigh correction $\gamma = \frac{1}{2}\Delta\rho\,gRh\left(1 + \frac{R}{3h} - 0.1288\frac{R^2}{h^2} + 0.1312\frac{R^3}{h^3}\right)$ is used |
| Maximum bubble pressure | A bubble is pushed out of a capillary tip into the liquid; when the bubble is a hemisphere its radius of curvature is smallest (equal to the tube radius $R$) and the pressure difference is largest | $\gamma = \frac{1}{2}R\,\Delta p_{\max}$ | In practice the instrument constant is calibrated with water of known $\gamma$; varying the bubbling rate gives the dynamic surface tension |
| Plate method (Wilhelmy method) | A thin plate (roughened platinum) is immersed vertically at the liquid surface and the pull of the liquid surface on it is measured | $F = \gamma l_{\mathrm{p}}\cos\theta$, $\theta \approx 0$ | $l_{\mathrm{p}}$ is the perimeter of the plate; a static method that does not need to pull off the liquid surface and is suited for continuous recording; the film balance (19.5.3) uses it |
| Ring method (du Noüy method) | A platinum ring is pulled up from the liquid surface and the maximum pull before the liquid film breaks is measured | $F_{\max} = 2\pi(r_{\mathrm{i}} + r_{\mathrm{o}})\gamma f$ | $r_{\mathrm{i}}$ and $r_{\mathrm{o}}$ are the inner and outer radii of the ring; the film pulled up is not vertical and an empirical correction factor $f$ (Harkins–Jordan table) is used |
| Drop weight (drop volume) method | When a drop falls from a tube tip, its weight equals the surface tension along the perimeter of the tip | $mg = 2\pi R\gamma f$ | Tate's law; only part of the drop falls off, and the Harkins–Brown correction factor $f$ is used |
| Pendant drop and sessile drop methods | The profile of a drop is photographed and fitted with the shape determined jointly by the Young–Laplace equation and gravity | Numerical fitting | The standard method of modern contact angle meters; needs little sample and can measure high-temperature melts and interfacial tensions |

## 19.4. Adsorption at Solution Surfaces

### 19.4.1. Effect of Solutes on Surface Tension

A pure liquid can lower its surface Gibbs free energy only by reducing its surface; a solution can also change the composition of the surface layer. The effects of solutes on the surface tension of water fall roughly into three classes:

1. The surface tension rises slightly with increasing concentration (approximately linearly): inorganic salts, inorganic acids and bases, and polyhydroxy compounds such as sucrose and mannitol. These solutes interact with water more strongly than water molecules interact with each other, and tend to stay in the interior of the solution.
2. The surface tension decreases gradually with increasing concentration: polar organic compounds of low molecular weight, such as alcohols, aldehydes, carboxylic acids, esters and amines.
3. A small amount lowers the surface tension sharply, and beyond a certain concentration it hardly changes any more: amphiphilic compounds with fairly long carbon chains (generally 8 carbons or more), such as long-chain carboxylates, alkyl sulfates and sulfonates, quaternary ammonium salts and polyoxyethylene ethers, that is, surfactants (19.7).

**Definition 19.4.1** A solute that lowers the surface tension of the solvent is called a **surface-active substance**; a solute that raises the surface tension is called a **surface-inactive substance**.

The dilute solutions of class 2 solutes are often described by an empirical formula:

**Formula 19.4.1 (Szyszkowski Equation)**

$$
\gamma_0 - \gamma = b\gamma_0\ln\left(1 + \frac{c}{K}\right),
$$
where $\gamma_0$ is the surface tension of pure water and $c$ the solute concentration; $b$ is related to the polar group and is approximately the same within a homologous series (about 0.18 for normal fatty acids), and $K$ is related to the carbon chain length.

In a homologous series each additional $\ce{CH2}$ reduces $K$ to about $1/3$ of its former value, that is, the concentration required for the same lowering of surface tension is reduced to about $1/3$; this is *Traube's rule*. It shows that the Gibbs free energy decreases by about $RT\ln 3 \approx 2.7\,\mathrm{kJ\,mol^{-1}}$ when each $\ce{CH2}$ is transferred from water to the surface, and that surface activity comes from the hydrophobic effect of the carbon chain.

### 19.4.2. Surface Excess and the Gibbs Dividing Surface

Solutes that lower the surface tension tend to be enriched at the surface, since the Gibbs free energy of the system is then lower; solutes that raise the surface tension tend to leave the surface.

**Definition 19.4.2** The phenomenon in which the concentration of a substance in the interfacial layer between two phases differs from that in the interior of the bulk phase is called **adsorption**. When the concentration of the solute in the interfacial layer is higher than in the bulk, it is called **positive adsorption**; when it is lower, **negative adsorption**.

The interfacial layer is only a few molecules thick and the concentration in it varies continuously, so a "surface concentration" cannot be defined directly. Gibbs (1878) replaced the real interfacial layer by an imaginary geometric surface and attributed the effects of the interface to "excess quantities".

**Definition 19.4.3** Choose in the interfacial layer a geometric surface parallel to the interface, and assume that the two phases $\alpha$ and $\beta$ on either side keep the uniform composition of their respective bulk phases right up to this surface; this surface is called the **Gibbs dividing surface**. The difference between the actual total amount $n_{\mathrm{B}}$ of substance B in the system and the amount contained in the two imaginary phases,

$$
n_{\mathrm{B}}^\sigma = n_{\mathrm{B}} - c_{\mathrm{B}}^\alpha V^\alpha - c_{\mathrm{B}}^\beta V^\beta
$$
is called the surface excess amount of B, and the surface excess amount per unit area, $\Gamma_{\mathrm{B}} = n_{\mathrm{B}}^\sigma/A_{\mathrm{s}}$, is called the **surface excess** (amount adsorbed) of B, with unit $\mathrm{mol\,m^{-2}}$.

The value of $\Gamma_{\mathrm{B}}$ depends on the position of the dividing surface. For a solution the dividing surface is usually placed where the surface excess of the solvent A is zero ($\Gamma_{\mathrm{A}} = 0$), and the surface excess of the solute is then called the relative surface excess, denoted $\Gamma_{\mathrm{B}}^{(\mathrm{A})}$. It no longer depends on any arbitrary choice, and its meaning is the amount of B contained in a unit area of the surface layer in excess of what a bulk solution containing the same amount of solvent would contain. $\Gamma_{\mathrm{B}}^{(\mathrm{A})} > 0$ is positive adsorption and $< 0$ is negative adsorption.

### 19.4.3. The Gibbs Adsorption Isotherm

The surface excess can be found from the variation of the surface tension with concentration, which is the most important result of surface thermodynamics.

**Theorem 19.4.1 (Gibbs Adsorption Isotherm)** For a binary solution at constant temperature and pressure,

$$
\Gamma_{\mathrm{B}}^{(\mathrm{A})} = -\left(\frac{\partial\gamma}{\partial\mu_{\mathrm{B}}}\right)_{T,p} = -\frac{a_{\mathrm{B}}}{RT}\left(\frac{\partial\gamma}{\partial a_{\mathrm{B}}}\right)_{T,p}. \tag{19.3}
$$
For an **ideal dilute solution** $a_{\mathrm{B}}$ can be replaced by $c_{\mathrm{B}}/c^\circ$ (or $b_{\mathrm{B}}/b^\circ$), and $\Gamma_{\mathrm{B}}^{(\mathrm{A})} = -\dfrac{c_{\mathrm{B}}}{RT}\left(\dfrac{\partial\gamma}{\partial c_{\mathrm{B}}}\right)_{T,p}$.

**Proof** Take a layer containing the whole inhomogeneous region as the "surface phase" $\sigma$, which contains solvent $n_{\mathrm{A}}^\sigma$ and solute $n_{\mathrm{B}}^\sigma$ and has area $A_{\mathrm{s}}$. At equilibrium the chemical potentials of the substances in the surface phase equal those in the bulk phases, and the fundamental equation of the surface phase is

$$
\mathrm{d}G^\sigma = -S^\sigma\,\mathrm{d}T + V^\sigma\,\mathrm{d}p + \mu_{\mathrm{A}}\,\mathrm{d}n_{\mathrm{A}}^\sigma + \mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}^\sigma + \gamma\,\mathrm{d}A_{\mathrm{s}}.
$$
At constant temperature and pressure, enlarging a surface of the same structure by a factor of two doubles $n_{\mathrm{A}}^\sigma$, $n_{\mathrm{B}}^\sigma$, $A_{\mathrm{s}}$ and $G^\sigma$, so $G^\sigma$ is a first-degree **homogeneous function** of $(n_{\mathrm{A}}^\sigma, n_{\mathrm{B}}^\sigma, A_{\mathrm{s}})$. By Euler's theorem on homogeneous functions ([Theorem 10.7.2](/2.2.10#thm-10.7.2)),

$$
G^\sigma = n_{\mathrm{A}}^\sigma\mu_{\mathrm{A}} + n_{\mathrm{B}}^\sigma\mu_{\mathrm{B}} + \gamma A_{\mathrm{s}}.
$$
Taking the total differential and subtracting the fundamental equation gives the Gibbs–Duhem equation of the surface phase

$$
S^\sigma\,\mathrm{d}T - V^\sigma\,\mathrm{d}p + n_{\mathrm{A}}^\sigma\,\mathrm{d}\mu_{\mathrm{A}} + n_{\mathrm{B}}^\sigma\,\mathrm{d}\mu_{\mathrm{B}} + A_{\mathrm{s}}\,\mathrm{d}\gamma = 0.
$$
At constant temperature and pressure, $n_{\mathrm{A}}^\sigma\,\mathrm{d}\mu_{\mathrm{A}} + n_{\mathrm{B}}^\sigma\,\mathrm{d}\mu_{\mathrm{B}} + A_{\mathrm{s}}\,\mathrm{d}\gamma = 0$. On the other hand, the **Gibbs–Duhem equation** of the bulk solution (containing $n_{\mathrm{A}}$ and $n_{\mathrm{B}}$) gives $\mathrm{d}\mu_{\mathrm{A}} = -(n_{\mathrm{B}}/n_{\mathrm{A}})\,\mathrm{d}\mu_{\mathrm{B}}$. Substituting to eliminate $\mathrm{d}\mu_{\mathrm{A}}$,

$$
\frac{1}{A_{\mathrm{s}}}\left(n_{\mathrm{B}}^\sigma - n_{\mathrm{A}}^\sigma\frac{n_{\mathrm{B}}}{n_{\mathrm{A}}}\right) = -\left(\frac{\partial\gamma}{\partial\mu_{\mathrm{B}}}\right)_{T,p}.
$$
The left-hand side is exactly the amount of B (per unit area) in the surface layer in excess of what a bulk solution containing the same amount of solvent would contain, that is, $\Gamma_{\mathrm{B}}^{(\mathrm{A})}$. It does not depend on the chosen thickness of the surface layer: if the layer is made thicker, the added part is bulk solution, $n_{\mathrm{A}}^\sigma$ and $n_{\mathrm{B}}^\sigma$ increase together in the proportion of the bulk phase, and the difference in the parentheses is unchanged. Finally $\mu_{\mathrm{B}} = \mu_{\mathrm{B}}^\circ + RT\ln a_{\mathrm{B}}$ gives $\mathrm{d}\mu_{\mathrm{B}} = RT\,\mathrm{d}a_{\mathrm{B}}/a_{\mathrm{B}}$. $\square$

The meaning of the Gibbs adsorption isotherm:

- When $(\partial\gamma/\partial c_{\mathrm{B}})_{T,p} < 0$, $\Gamma > 0$: the solute is positively adsorbed, that is, surface-active substances are enriched at the surface; when $(\partial\gamma/\partial c_{\mathrm{B}})_{T,p} > 0$, $\Gamma < 0$: negative adsorption, and the solvent is relatively enriched at the surface. In short, a species that lowers the surface tension is always relatively concentrated at the surface.
- It is a rigorous thermodynamic result that does not depend on any molecular model, and it also applies to liquid–liquid, solid–liquid and solid–gas interfaces if $\gamma$ is replaced by the corresponding interfacial tension. But the interfacial tension of a solid cannot be measured reliably, so the amount adsorbed on a solid surface has to be measured directly ([6.3.20](/6.3.20)).
- The surface excess can be found from the $\gamma$–$c$ curve: by differentiating an empirical formula (such as the Szyszkowski equation) or by drawing tangents to the experimental curve. $\Gamma$ can also be measured directly by radioactive tracers, neutron reflection, or scraping off the surface layer (McBain's "microtome" experiment), and the results agree with the Gibbs isotherm.
- An ionic solute dissociates in water into two kinds of ions, both adsorbed at the surface. For a 1-1 ionic surfactant (without added salt), $\Gamma = -\frac{1}{2RT}(\partial\gamma/\partial\ln c)_{T,p}$; in the presence of a large amount of salt with the same counterion the factor $\frac{1}{2}$ disappears.

### 19.4.4. Saturation Adsorption and Molecular Cross-Sectional Area

Substituting the Szyszkowski equation into the Gibbs adsorption isotherm, $\partial\gamma/\partial c = -b\gamma_0/(K + c)$,

$$
\Gamma = \frac{b\gamma_0}{RT}\cdot\frac{c}{K + c} = \Gamma_\infty\frac{c}{K + c}, \qquad \Gamma_\infty = \frac{b\gamma_0}{RT}.
$$
At low concentration $\Gamma$ is proportional to $c$, and at high concentration it tends to the constant $\Gamma_\infty$, called the saturation adsorption: the solute molecules have pushed the solvent away from the surface and formed a close-packed monolayer at the surface. This expression has the same form as the **Langmuir adsorption isotherm** of solid surfaces ([6.3.20](/6.3.20)), and the Szyszkowski equation is just the law of variation of $\gamma$ with concentration when surface adsorption obeys the Langmuir form. From $\Gamma_\infty$ the area occupied by each molecule at the surface is $a_\infty = 1/(\Gamma_\infty N_{\mathrm{A}})$.

**Example 19.4.1** For the homologous series of normal fatty acids in aqueous solution at $25\,{}^\circ\mathrm{C}$, $b = 0.179$ and $\gamma_0 = 72.0\,\mathrm{mN\,m^{-1}}$, so $\Gamma_\infty = 0.179 \times 0.0720/(8.314 \times 298.15)\,\mathrm{mol\,m^{-2}} = 5.2\,\mu\mathrm{mol\,m^{-2}}$ and $a_\infty = 1/(5.2 \times 10^{-6} \times 6.022 \times 10^{23})\,\mathrm{m^2} = 0.32\,\mathrm{nm^2}$. That $\Gamma_\infty$ is independent of carbon-chain length shows that in the saturated adsorbed layer the molecules stand upright with the polar group toward the water and the carbon chain toward the air, and the area occupied is determined by the cross sections of the polar group and the carbon chain; it is slightly larger than the area of close-packed long-chain fatty acids in insoluble monolayers (about $0.20\,\mathrm{nm^2}$, 19.5.3), showing that the soluble short-chain molecules are not completely close-packed in the saturated adsorbed layer.

![Left: surface tension of aqueous solutions of three homologous surface-active solutes calculated from the Szyszkowski equation (b = 0.179, K = 0.09, 0.03, 0.01 mol/L; each additional CH2 reduces K to about 1/3). Right: the surface excess obtained from the Gibbs adsorption isotherm, rising linearly at low concentration, with all homologs tending to the same saturation value Γ∞ = bγ0/RT](./plots/gibbs-adsorption.py)

## 19.5. Liquid–Liquid Interfaces and Monolayers

### 19.5.1. Spreading

When a drop of a liquid insoluble in water (liquid 1) is placed on the surface of water (liquid 2), it may remain as a lens-shaped drop or spread into a thin film. Spreading replaces a unit area of the liquid 2–gas interface by a liquid 1–gas interface and a liquid 1–liquid 2 interface, and at constant temperature and pressure

$$
\frac{\Delta G}{A_{\mathrm{s}}} = \gamma_1 + \gamma_{12} - \gamma_2.
$$

**Definition 19.5.1** $S_{1/2} = \gamma_2 - \gamma_1 - \gamma_{12} = -\Delta G/A_{\mathrm{s}}$ is called the **spreading coefficient** of liquid 1 on liquid (or solid) 2. For $S \ge 0$ spreading occurs spontaneously, and for $S < 0$ liquid 1 forms drops.

For example, at $20\,{}^\circ\mathrm{C}$ the initial spreading coefficient of benzene on water is $S = 72.8 - 28.9 - 35.0 = 8.9\,\mathrm{mN\,m^{-1}} > 0$ and that of $n$-hexane is $72.8 - 18.4 - 51.1 = 3.3\,\mathrm{mN\,m^{-1}} > 0$, and both can spread on a clean water surface. But after the spread liquid and the water have become mutually saturated, the surface tension of the water drops and the "final spreading coefficient" becomes negative, so the spread film contracts again into lens-shaped drops coexisting with a monolayer. An organic liquid of low surface tension can generally spread on the surface of water, which has a high surface tension; conversely, water cannot spread on an oil surface.

### 19.5.2. Insoluble Monolayers and Surface Pressure

In 1774 Franklin poured a teaspoon of oil on the surface of a pond near London and found that the oil spread rapidly and calmed the waves over about half an acre of water; he did not calculate the thickness of the oil layer. More than a century later Rayleigh (1890) estimated from the volume of oil and the area of spreading that the thickness of the oil film was about 1–2 nm, comparable to the size of a molecule; Pockels invented in her own kitchen a trough for measuring oil films on water (1891), and Langmuir (1917) used an improved trough to show that such films are only one molecule thick, and obtained the cross-sectional areas of the molecules from the area of the films.

**Definition 19.5.2** A film only one molecule thick formed when amphiphilic molecules sparingly soluble in water (long-chain fatty acids, alcohols, phospholipids) or certain polymers are spread on a water surface is called a **monolayer**.

The polar groups of the molecules in the film extend into the water, and the carbon chains point toward the air. The surface tension $\gamma$ of a water surface covered with a monolayer is lower than $\gamma_0$ of pure water. Place a movable float at the edge of the film, with the film on one side and pure water on the other; the float is pulled by $\gamma_0 l$ on the pure-water side and by $\gamma l$ on the film side, and the net force $(\gamma_0 - \gamma)l$ pushes the float toward the pure-water side, as if the film exerted a two-dimensional pressure on the float.

**Definition 19.5.3** The push per unit length of the float,

$$
\Pi^{\mathrm{s}} = \gamma_0 - \gamma
$$
is called the **surface pressure** of the monolayer, with unit $\mathrm{N\,m^{-1}}$.

### 19.5.3. The Film Balance and the $\Pi^{\mathrm{s}}$–$a$ Curve

The Langmuir film balance is a shallow trough filled with water; movable barriers enclose the surface film and change its area, and the surface pressure is measured with a float–torsion balance or a Wilhelmy plate (19.3) with a precision of up to $10^{-5}\,\mathrm{N\,m^{-1}}$. The number $N$ of film-forming molecules spread on the water and the film area $A_{\mathrm{s}}$ are known, and the area per molecule is $a = A_{\mathrm{s}}/N$. Compressing the film and recording the variation of $\Pi^{\mathrm{s}}$ with $a$ (the $\Pi^{\mathrm{s}}$–$a$ isotherm), we can see two-dimensional "phase transitions":

- When the area per molecule is very large the film is a two-dimensional gas and obeys the two-dimensional ideal gas equation $\Pi^{\mathrm{s}}a = k_{\mathrm{B}}T$ (at $25\,{}^\circ\mathrm{C}$ and $a = 10\,\mathrm{nm^2}$, $\Pi^{\mathrm{s}} \approx 0.4\,\mathrm{mN\,m^{-1}}$). This is the two-dimensional counterpart of $\Gamma \propto c$ and $\gamma_0 - \gamma \propto c$ in dilute solutions from the Gibbs isotherm: $\Pi^{\mathrm{s}} = \Gamma RT$.
- On further compression a plateau with almost constant surface pressure appears, which is the coexistence of two-dimensional gas and liquid phases, similar to the isotherms of real gases in [6.3.1](/6.3.1); then come the liquid-expanded film and the liquid-condensed film.
- Further compression gives a solid film, and $\Pi^{\mathrm{s}}$ rises steeply as $a$ decreases. Extrapolating to $\Pi^{\mathrm{s}} = 0$ gives the limiting cross-sectional area of the molecule: about $0.20\,\mathrm{nm^2}$ for stearic acid, independent of the carbon-chain length and exactly the cross-sectional area of an upright carbon chain. At still higher pressure the film collapses into multilayers.

**Definition 19.5.4** A mono- or multilayer film obtained by transferring a monolayer, compressed on the water surface to a given surface pressure, layer by layer onto a solid substrate by vertical dipping or horizontal contact, with the oriented arrangement of the molecules preserved, is called a **Langmuir–Blodgett film** (LB film).

By changing the direction and order of dipping one obtains Y-type multilayers with head-to-head and tail-to-tail alternating molecules, or X-type and Z-type multilayers with molecules all pointing the same way. LB films allow the thickness and molecular arrangement to be controlled precisely and are used in sensors, molecular electronic devices and surface modification.

Monolayers are a classical model for the study of biological membranes. Gorter and Grendel (1925) extracted the lipids from erythrocyte membranes and spread them as a monolayer on a film balance, found that its area was about twice the surface area of the erythrocytes, and on this basis proposed that the cell membrane is a lipid bilayer. Lipid molecules on a film balance likewise show the liquid-expanded and liquid-condensed states, corresponding to the liquid-crystalline and gel states of bilayers (the gel–liquid-crystal transition mentioned in [6.3.8](/6.3.8)). Pulmonary surfactant (19.2.1) is repeatedly compressed and expanded in breathing, and its $\Pi^{\mathrm{s}}$–$a$ curve shows marked hysteresis; on compression the surface pressure can reach about $70\,\mathrm{mN\,m^{-1}}$, that is, the surface tension approaches zero.

## 19.6. Solid–Liquid Interfaces and Wetting

### 19.6.1. Adhesion, Immersion and Spreading

**Definition 19.6.1** The process in which a solid–gas interface is replaced by a solid–liquid interface when a liquid comes into contact with a solid is called **wetting**.

According to the process, wetting is divided into three kinds (each interface taken per unit area, at constant temperature and pressure). Adhesion: the liquid–gas and solid–gas interfaces disappear and a solid–liquid interface forms, $\Delta G_{\mathrm{a}} = \gamma_{\mathrm{sl}} - \gamma_{\mathrm{lg}} - \gamma_{\mathrm{sg}}$. Immersion: a solid is immersed in a liquid, the solid–gas interface is replaced by a solid–liquid interface and the area of the liquid surface is unchanged, $\Delta G_{\mathrm{i}} = \gamma_{\mathrm{sl}} - \gamma_{\mathrm{sg}}$. Spreading: a liquid spreads over a solid surface, the solid–gas interface is replaced by a solid–liquid interface and an equal area of liquid–gas interface is created at the same time, $\Delta G_{\mathrm{s}} = \gamma_{\mathrm{sl}} + \gamma_{\mathrm{lg}} - \gamma_{\mathrm{sg}}$.

**Definition 19.6.2** The work required at constant temperature and pressure to separate a unit area of solid–liquid interface reversibly into a solid–gas and a liquid–gas surface,

$$
W_{\mathrm{a}} = -\Delta G_{\mathrm{a}} = \gamma_{\mathrm{sg}} + \gamma_{\mathrm{lg}} - \gamma_{\mathrm{sl}}
$$
is called the **work of adhesion**; the work $W_{\mathrm{c}} = 2\gamma_{\mathrm{lg}}$ required to separate a liquid column of unit cross-sectional area reversibly into two liquid surfaces is called the **work of cohesion** of the liquid; the decrease of the Gibbs free energy when a unit area of solid is immersed in a liquid, $W_{\mathrm{i}} = -\Delta G_{\mathrm{i}} = \gamma_{\mathrm{sg}} - \gamma_{\mathrm{sl}}$, is called the **work of immersion** (also called the adhesion tension).

The decrease of the Gibbs free energy in spreading is the spreading coefficient (Definition 19.5.1): $S = -\Delta G_{\mathrm{s}} = \gamma_{\mathrm{sg}} - \gamma_{\mathrm{lg}} - \gamma_{\mathrm{sl}} = W_{\mathrm{a}} - W_{\mathrm{c}}$. Here, following the IUPAC convention, $W_{\mathrm{a}}$, $W_{\mathrm{i}}$ and $S$ all equal the decrease of the Gibbs free energy of the corresponding process, and the process is spontaneous when they are positive (many textbooks call $\Delta G$ itself the work of adhesion, with the opposite sign). $S = W_{\mathrm{a}} - W_{\mathrm{c}}$ has an intuitive meaning: when the adhesion of the liquid to the solid is stronger than the cohesion of the liquid itself, the liquid spreads on the solid.

### 19.6.2. Contact Angle and the Young Equation

Of the three interfacial tensions, $\gamma_{\mathrm{sg}}$ and $\gamma_{\mathrm{sl}}$ cannot be measured directly, and the degree of wetting has to be expressed in terms of measurable quantities.

**Definition 19.6.3** When a drop on a solid surface reaches equilibrium, the angle $\theta$ at the junction of the gas, liquid and solid phases between the tangent to the liquid–gas interface and the solid–liquid interface (measured through the liquid) is called the **contact angle**, $0^\circ \le \theta \le 180^\circ$.

**Theorem 19.6.1 (Young Equation)** At equilibrium

$$
\gamma_{\mathrm{sg}} = \gamma_{\mathrm{sl}} + \gamma_{\mathrm{lg}}\cos\theta. \tag{19.4}
$$

**Proof** Let the three-phase contact line move outward along the solid surface by $\mathrm{d}x$ (per unit length of contact line): the solid–liquid interface increases by $\mathrm{d}x$, the solid–gas interface decreases by $\mathrm{d}x$ and the liquid–gas interface increases by $\cos\theta\,\mathrm{d}x$. At equilibrium $\mathrm{d}G = (\gamma_{\mathrm{sl}} - \gamma_{\mathrm{sg}} + \gamma_{\mathrm{lg}}\cos\theta)\,\mathrm{d}x = 0$. It can also be viewed as the balance of the components of the three surface tensions along the solid surface at the contact line. $\square$

Substituting the Young equation into the three kinds of work gives expressions containing only measurable quantities (the Young–Dupré equation):

$$
W_{\mathrm{a}} = \gamma_{\mathrm{lg}}(1 + \cos\theta), \qquad W_{\mathrm{i}} = \gamma_{\mathrm{lg}}\cos\theta, \qquad S = \gamma_{\mathrm{lg}}(\cos\theta - 1).
$$

| Contact angle | Adhesion | Immersion | Spreading | Common description |
|---|---|---|---|---|
| $\theta = 0^\circ$ | Spontaneous | Spontaneous | $S \ge 0$ ($S = 0$ gives $\theta = 0^\circ$ by the Young equation; for $S > 0$, i.e. $\gamma_{\mathrm{sg}} - \gamma_{\mathrm{sl}} > \gamma_{\mathrm{lg}}$, there is no equilibrium contact angle and the liquid spreads completely) | Complete wetting |
| $0^\circ < \theta \le 90^\circ$ | Spontaneous | Spontaneous | Not possible | Wetting |
| $90^\circ < \theta < 180^\circ$ | Spontaneous | Not possible | Not possible | Nonwetting |
| $\theta = 180^\circ$ | $W_{\mathrm{a}} = 0$ | Not possible | Not possible | Complete nonwetting |

For example water wets clean glass ($\theta \approx 0$) and does not wet paraffin wax ($\theta \approx 110^\circ$); mercury does not wet glass ($\theta \approx 140^\circ$). Real surfaces are not ideal: the contact angle measured as a drop advances (the advancing angle) is larger than that measured as it recedes (the receding angle), and this contact angle hysteresis arises from roughness and chemical inhomogeneity of the surface; it allows a raindrop to hang on an inclined glass pane without sliding off.

### 19.6.3. Rough Surfaces and Superhydrophobicity

On a rough or microstructured surface, the apparent contact angle $\theta^*$ differs from the intrinsic contact angle $\theta$ on a smooth surface. When the liquid completely fills the grooves of the surface (the Wenzel state), the real solid–liquid interfacial area is $r_{\mathrm{f}}$ times the apparent area (roughness factor $r_{\mathrm{f}} \ge 1$), and $\cos\theta^* = r_{\mathrm{f}}\cos\theta$: roughening makes a hydrophilic surface more hydrophilic and a hydrophobic one more hydrophobic. When the drop rests on air trapped in the grooves (the Cassie–Baxter state), only an area fraction $\varphi_{\mathrm{s}}$ is in contact with the solid, and $\cos\theta^* = \varphi_{\mathrm{s}}(1 + \cos\theta) - 1$.

**Definition 19.6.4** The phenomenon in which the apparent contact angle of water is larger than $150^\circ$ and the sliding angle is smaller than about $10^\circ$ is called **superhydrophobicity**.

The surface of a lotus leaf has micrometer-sized papillae, which are covered in turn with nanometer-sized wax crystals, and water drops are in the Cassie–Baxter state. If the intrinsic contact angle of the wax is $110^\circ$ and $\varphi_{\mathrm{s}} = 0.1$, then $\cos\theta^* = 0.1 \times (1 - 0.342) - 1 = -0.934$ and $\theta^* = 159^\circ$. The water drop is almost spherical, the contact angle hysteresis is very small, and the drop rolls off at the slightest tilt, carrying away dust: the "lotus effect". Superhydrophobic surfaces are used in self-cleaning glass and coatings, anti-icing, anticorrosion and oil–water separation; the legs of water striders and the wings of some insects are also superhydrophobic.

## 19.7. Surfactants

### 19.7.1. Molecular Structure and Classification

**Definition 19.7.1** A substance that, added in small amount, markedly lowers the surface tension of water (or the oil–water interfacial tension) is called a **surfactant**. Surfactants are **amphiphiles**: one end of the molecule is a polar hydrophilic group and the other end is a nonpolar hydrophobic group (lipophilic group, usually a hydrocarbon chain of 8–18 carbons).

According to whether the hydrophilic group dissociates in water and the charge it carries, they are classified as follows:

| Type | Hydrophilic group | Examples |
|---|---|---|
| Anionic | Carboxylate, sulfate ester, sulfonate | Soap (sodium fatty acid salts), sodium dodecyl sulfate (SDS, 1), sodium dodecylbenzenesulfonate |
| Cationic | Quaternary ammonium | Cetyltrimethylammonium bromide (CTAB, 2), often used as a disinfectant and a fabric softener |
| Zwitterionic | Groups containing both positive and negative charges | Dodecyldimethylbetaine (3), lecithin |
| Nonionic | Polyoxyethylene chain, polyol | Polyoxyethylene ether $\ce{C12E8}$ (4), Triton X-100, Tween and Span |

```smiles
CCCCCCCCCCCCOS(=O)(=O)[O-].[Na+] 1
CCCCCCCCCCCCCCCC[N+](C)(C)C.[Br-] 2
CCCCCCCCCCCC[N+](C)(C)CC(=O)[O-] 3
CCCCCCCCCCCCOCCOCCOCCOCCOCCOCCOCCOCCO 4
```

$\ce{C_mE_n}$ stands for $\ce{C_mH_{2m+1}(OCH2CH2)_nOH}$. Surface-active substances in living organisms include phospholipids, bile salts (which help to emulsify and absorb fats), glycolipids and pulmonary surfactant.

### 19.7.2. Efficiency and Effectiveness

The performance of a surfactant is described by two quantities: the efficiency, the concentration needed to lower the surface tension of water to a given value (commonly a lowering of $20\,\mathrm{mN\,m^{-1}}$), where a lower concentration means a higher efficiency; and the effectiveness, the lowest value to which it can bring the surface tension of water, that is, the surface tension at the critical micelle concentration. The longer the hydrophobic chain, the higher the efficiency (Traube's rule); when the hydrophobic chain is branched or has unsaturated bonds, the efficiency decreases but the effectiveness increases, because such molecules pack more loosely at the surface, but their hydrophobic part, with a larger cross section, covers the water surface more effectively.

### 19.7.3. Micelles and the Critical Micelle Concentration

As the concentration of a surfactant solution increases, the amount adsorbed at the surface grows until a close-packed monolayer forms (saturation adsorption); on further increase of concentration the excess molecules aggregate inside the solution, with their hydrophobic chains together and their hydrophilic groups outward, forming aggregates.

**Definition 19.7.2** An ordered aggregate formed by association of surfactant molecules in solution, with the hydrophobic groups inside and the hydrophilic groups outside, is called a **micelle**; the concentration at which micelles begin to form in large numbers is called the **critical micelle concentration** (CMC). In nonpolar solvents, surfactant molecules aggregate with the hydrophilic groups inside and the hydrophobic groups outside, which is called a **reverse micelle**.

Note that a micelle in this sense must not be confused with the colloidal micelle, the structural unit of a sol consisting of a colloidal particle together with its diffuse layer ([6.3.21](/6.3.21)), which is not an aggregate of surfactant molecules.

Near the CMC many properties of the solution change their course: the surface tension no longer decreases (the monomer concentration no longer increases), the slope of the conductivity against concentration becomes smaller (micelles bind part of the counterions and also migrate more slowly), the osmotic pressure and the freezing-point depression almost stop increasing (a micelle contains tens to a hundred molecules and counts as only one particle), the solubilization of hydrophobic dyes begins, and the intensity of light scattering rises abruptly. Determining the turning points of these properties is a way to measure the CMC.

![Schematic variation of four properties of an aqueous solution of sodium dodecyl sulfate at the critical micelle concentration (about 8.2 mmol/L at 25 °C, dashed line): the surface tension no longer decreases, the slope of the conductivity becomes smaller, the osmotic pressure hardly increases any more, and the solubility of a hydrophobic dye begins to increase](./plots/cmc-properties.py)

At $25\,{}^\circ\mathrm{C}$ the CMC of SDS is about $8.2\,\mathrm{mmol\,L^{-1}}$, that of CTAB about $0.9\,\mathrm{mmol\,L^{-1}}$ and that of $\ce{C12E8}$ about $0.1\,\mathrm{mmol\,L^{-1}}$. The CMC of nonionic surfactants is much lower because there is no electrostatic repulsion between the hydrophilic groups. In a homologous series each additional $\ce{CH2}$ in the hydrophobic chain reduces the CMC of ionic surfactants to about $1/2$ and that of nonionic ones to about $1/3$.

The driving force of micellization is the hydrophobic effect. Regarding the micelle as a "pseudo-phase", at equilibrium between monomers and micelles $\Delta G^\circ_{\mathrm{mic}} \approx RT\ln x_{\mathrm{CMC}}$ (nonionic, with $x_{\mathrm{CMC}}$ the mole fraction at the CMC): for $\ce{C12E8}$, $x_{\mathrm{CMC}} = 1.1 \times 10^{-4}/55.5 = 2.0 \times 10^{-6}$ and $\Delta G^\circ_{\mathrm{mic}} \approx -32\,\mathrm{kJ\,mol^{-1}}$. At room temperature the enthalpy change of micellization is very small, and the main contribution is the entropy increase: the water molecules originally arranged in an ordered way around the hydrocarbon chain are released on micellization.

The shape of a micelle depends on the geometry of the molecule. Let the volume of the hydrophobic chain be $v$, its maximum extended length $l_{\mathrm{c}}$ and the area occupied by the hydrophilic group at the surface of the aggregate $a_0$, and define the packing parameter $P = v/(a_0l_{\mathrm{c}})$: for $P < 1/3$ spherical micelles form (single-chain SDS), for $1/3 < P < 1/2$ rod-like micelles, for $1/2 < P < 1$ bilayers (double-chain phospholipids, hence vesicles and cell membranes), and for $P > 1$ reverse micelles. At still higher concentrations the micelles further arrange into liquid-crystalline phases such as hexagonal and lamellar phases.

### 19.7.4. The Hydrophile–Lipophile Balance

The uses of a surfactant depend on the relative strength of its hydrophilicity and lipophilicity.

**Definition 19.7.3** For nonionic surfactants Griffin defined the **hydrophile–lipophile balance** (HLB value)

$$
\mathrm{HLB} = 20 \times \frac{M_{\mathrm{h}}}{M},
$$
where $M_{\mathrm{h}}$ is the molar mass of the hydrophilic part and $M$ the molar mass of the molecule.

Paraffin wax, which has no hydrophilic group, has HLB = 0, polyethylene glycol, which consists entirely of hydrophilic groups, has HLB = 20, and nonionic surfactants lie in between. For example, for $\ce{C12E8}$ ($M = 538.7\,\mathrm{g\,mol^{-1}}$, of which the $\ce{(OCH2CH2)8OH}$ part is $369.4\,\mathrm{g\,mol^{-1}}$), $\mathrm{HLB} = 20 \times 369.4/538.7 = 13.7$. For ionic surfactants it can be estimated by Davies' group-contribution method (for SDS about 40). The uses chosen by HLB value are:

| HLB | Use |
|---|---|
| 1.5–3 | Antifoaming agent |
| 3–6 | W/O emulsifier |
| 7–9 | Wetting agent |
| 8–18 | O/W emulsifier |
| 13–15 | Detergent |
| 15–18 | Solubilizer |

### 19.7.5. The Krafft Point and the Cloud Point

The solubility of an ionic surfactant increases slowly with temperature and then rises steeply beyond a certain temperature. The reason is that at low temperature the solubility is below the CMC and only monomers are present in solution; when the temperature rises to the point at which the solubility reaches the CMC, micelles start to form, and since micelles can hold a large number of molecules the solubility "suddenly" increases.

**Definition 19.7.4** The temperature at which the solubility of an ionic surfactant equals its critical micelle concentration is called the **Krafft point**. Below the Krafft point micelles cannot form.

The longer the carbon chain of a homologous series, the higher the Krafft point. The Krafft point of SDS is about $16\,{}^\circ\mathrm{C}$, so solutions of SDS and electrophoresis buffers containing SDS precipitate crystals in winter; that of CTAB is about $25\,{}^\circ\mathrm{C}$. Ionic surfactants should be used above the Krafft point.

Nonionic surfactants behave in the opposite way. The polyoxyethylene chain dissolves in water through hydrogen bonds between the ether oxygens and water, and when the temperature rises the hydrogen bonds are broken and the solubility decreases.

**Definition 19.7.5** The temperature at which a solution of a nonionic surfactant begins to turn cloudy on heating (separating into a surfactant-rich and a surfactant-poor liquid phase) is called the **cloud point**.

The longer the polyoxyethylene chain (the larger the EO number), the stronger the hydrophilicity and the higher the cloud point; the longer the hydrophobic chain, the lower the cloud point. For example the cloud points of $\ce{C12E5}$, $\ce{C12E6}$ and $\ce{C12E8}$ are about $31$, $51$ and $78\,{}^\circ\mathrm{C}$. This phase separation is a liquid–liquid equilibrium with a lower critical solution temperature ([6.3.9](/6.3.9)); in biochemistry the cloud-point phase separation of Triton X-114 (cloud point about $23\,{}^\circ\mathrm{C}$) is used to separate membrane proteins from water-soluble proteins.

### 19.7.6. Actions of Surfactants

Wetting. Surfactants lower $\gamma_{\mathrm{lg}}$ and adsorb on solid surfaces to change $\gamma_{\mathrm{sl}}$, thereby changing the contact angle. A wetting agent added to pesticides makes the spray spread on hydrophobic leaf surfaces; in mineral flotation a collector is added, whose polar group adsorbs on the surface of mineral particles with the hydrophobic group outward, so that the particles become hydrophobic, attach to bubbles and float up, while the gangue remains in the water.

Foaming.

**Definition 19.7.6** A dispersed system in which gas is dispersed in a liquid and separated by liquid films is called a **foam**.

A foam has an enormous gas–liquid interface and is thermodynamically unstable. Three liquid films meet along a line at $120^\circ$, and these lines are channels in the liquid film (Plateau borders); four Plateau borders meet at a point at tetrahedral angles (Plateau's laws). The liquid surface of a Plateau border is concave, so by the Young–Laplace equation the pressure of the liquid in it is lower than in the flat film, and liquid flows from the film into the border and drains under gravity, making the film thinner until it breaks; the pressure in small bubbles is high, and gas diffuses through the film into larger bubbles, so the foam gradually coarsens. Surfactants stabilize the film: when a part of the film is thinned, the surface excess there decreases and the surface tension rises, creating a surface-tension gradient that pulls liquid back (the Gibbs–Marangoni effect). Foaming is used in flotation, foam fire extinguishing and foamed plastics; in vacuum distillation, fermentation and sewage treatment an antifoaming agent has to be added.

Solubilization.

**Definition 19.7.7** The phenomenon in which an organic substance sparingly soluble in water dissolves in surfactant micelles, markedly increasing its apparent solubility in water, is called **solubilization**.

The solubilizate is not dispersed in water in molecular form but enters the core or palisade layer of the micelles, so the **colligative properties** of the solution are almost unchanged after solubilization and the micelles swell slightly. Solubilization lowers the chemical potential of the solubilized substance and is a spontaneous process that gives a thermodynamically stable system. In biochemistry the micelles of detergents (SDS, Triton X-100, dodecyl maltoside) enclose the hydrophobic parts of membrane proteins and "dissolve" them out of the lipid bilayer for purification and structural study.

Emulsification. Surfactants allow one liquid to be stably dispersed in another in the form of droplets; see [6.3.21](/6.3.21).

Washing. Dirt (D) adheres to the surface of a solid (s), and the work of adhesion required to separate them in water (w) is $W_{\mathrm{a}} = \gamma_{\mathrm{sw}} + \gamma_{\mathrm{Dw}} - \gamma_{\mathrm{sD}}$. The detergent adsorbs at the solid–water and dirt–water interfaces and lowers $\gamma_{\mathrm{sw}}$ and $\gamma_{\mathrm{Dw}}$, so the work of adhesion is reduced, the dirt is rolled up and detached under mechanical action, and is then emulsified, solubilized and dispersed in the water; the surfactant adsorbed on the clean surface and on the dirt particles also prevents the dirt from redepositing. A good detergent should therefore have good wetting properties, markedly lower interfacial tension, and a certain capacity for solubilization and dispersion.

Preparation of nanomaterials. The core of a reverse micelle in oil is a nanometer-sized "water pool". When two reverse micelle solutions, containing the reactants A and B respectively, are mixed, the micelles collide and exchange contents, the reaction takes place in the water pools, and the product nucleates and grows in them, the particle size being limited by the size of the pools. Varying the ratio of water to surfactant controls the particle size, and the method is used to prepare nanoparticles of metals, semiconductors and oxides.

## Summary

| Topic | Key points |
|---|---|
| Surface tension | $\gamma = (\partial G/\partial A_{\mathrm{s}})_{T,p,n}$, unit $\mathrm{N\,m^{-1}} = \mathrm{J\,m^{-2}}$; $(\partial S/\partial A_{\mathrm{s}})_{T,p} = -(\partial\gamma/\partial T)$, $\gamma$ decreases with increasing $T$; Eötvös rule $\gamma V_{\mathrm{m}}^{2/3} = k(T_{\mathrm{c}} - T)$ |
| Young–Laplace equation | $\Delta p = \gamma(1/r_1 + 1/r_2)$; sphere $2\gamma/r$, soap bubble $4\gamma/r$; capillary rise $h = 2\gamma\cos\theta/(\Delta\rho\,gR)$ |
| Kelvin equation | $\ln(p_r/p^*) = 2\gamma V_{\mathrm{m}}/(RTr)$; convex surface $p_r > p^*$, concave surface $p_r < p^*$ |
| Small particles | Solubility $\ln(x_r/x_\infty) = 2\gamma_{\mathrm{sl}}V_{\mathrm{m}}/(RTr)$; melting point $\ln(T_{\mathrm{m}}(r)/T_{\mathrm{m}}) = -2\gamma_{\mathrm{sl}}V_{\mathrm{m}}/(\Delta_{\mathrm{fus}}H_{\mathrm{m}}r)$ |
| Nucleation | $\Delta G = 4\pi r^2\gamma + \frac{4}{3}\pi r^3\Delta G_V$; $r_{\mathrm{c}} = 2\gamma/\lvert\Delta G_V\rvert$, $\Delta G^* = 16\pi\gamma^3/(3\Delta G_V^2)$; the barrier of heterogeneous nucleation is multiplied by $f(\theta) \le 1$ |
| Gibbs adsorption isotherm | $\Gamma_{\mathrm{B}}^{(\mathrm{A})} = -(a_{\mathrm{B}}/RT)(\partial\gamma/\partial a_{\mathrm{B}})_{T,p}$; solutes that lower $\gamma$ are positively adsorbed; combined with the Szyszkowski equation, $\Gamma = \Gamma_\infty c/(K + c)$ |
| Monolayers | Surface pressure $\Pi^{\mathrm{s}} = \gamma_0 - \gamma$; two-dimensional ideal gas $\Pi^{\mathrm{s}}a = k_{\mathrm{B}}T$; limiting area of stearic acid $0.20\,\mathrm{nm^2}$ |
| Wetting (IUPAC) | Young equation $\gamma_{\mathrm{sg}} = \gamma_{\mathrm{sl}} + \gamma_{\mathrm{lg}}\cos\theta$; $W_{\mathrm{a}} = \gamma_{\mathrm{lg}}(1 + \cos\theta)$, $W_{\mathrm{i}} = \gamma_{\mathrm{lg}}\cos\theta$, $S = \gamma_{\mathrm{lg}}(\cos\theta - 1)$ |
| Surfactants | Amphiphiles; properties change abruptly at the CMC; the packing parameter determines micelle shape; HLB $= 20M_{\mathrm{h}}/M$; ionic ones have a Krafft point, nonionic ones a cloud point (the larger the EO number, the higher the cloud point) |

## Questions

1. By what routes do a pure liquid, a solution and a solid lower their surface Gibbs free energy?

   **Answer** A pure liquid can only reduce its surface area; a solution can also change the surface composition through surface adsorption, with surface-active substances positively adsorbed and surface-inactive substances negatively adsorbed; the surface atoms of a solid cannot move, and a solid relies mainly on adsorbing gas or solution molecules ([6.3.20](/6.3.20)).

2. When the adsorption of a solute at the surface of a solution is positive, the surface tension rises with increasing solute concentration. Is this correct?

   **Answer** No. By the Gibbs adsorption isotherm, $\Gamma > 0$ corresponds to $(\partial\gamma/\partial c)_{T,p} < 0$, and the surface tension decreases with increasing concentration; solutes that raise the surface tension are negatively adsorbed.

3. Why, after the stopcock is opened in a glass tube with a soap bubble at each end, does the small bubble become smaller and the large bubble larger?

   **Answer** The additional pressure $4\gamma/r$ of the small bubble is larger, and gas flows from the small bubble to the large one; as the small bubble shrinks its curvature increases further, so the process accelerates by itself until the small bubble is only a spherical cap with the same radius of curvature as the large bubble.

4. Which metastable state do artificial rain-making and bumping respectively exploit or avoid?

   **Answer** Artificial rain-making seeds supersaturated water vapor with condensation nuclei or ice nuclei and removes the supersaturation; bumping is the sudden vaporization of a superheated liquid and can be avoided by adding boiling chips to provide bubble nuclei.
