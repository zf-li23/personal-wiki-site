---
title: Colloidal Dispersions and Macromolecular Solutions
source_hash: d5b7c60fcd7b
---

Colloids are the field of application of interface chemistry: the particles of the dispersed phase are small enough that interfacial energy is significant and Brownian motion is pronounced, yet large enough that they no longer form a true solution of dispersed molecules. Milk, blood, ink, paint, fog and smoke, cytoplasm and solutions of biological macromolecules are all colloidal dispersions. This chapter first gives the classification of dispersions and the structure of sols (21.1), and the preparation and aging of sols (21.2); it then discusses three classes of properties: kinetic properties (21.3: Brownian motion, diffusion, sedimentation and ultracentrifugation), optical properties (21.4: light scattering) and electrical properties (21.5: the electric double layer and electrokinetic phenomena); on this basis we understand why sols can be stable and how they coagulate (21.6, DLVO theory); then introduce emulsions and microemulsions (21.7) and gels (21.8); the last topic is the average molar mass, osmotic pressure, viscosity and Donnan equilibrium of macromolecular solutions (21.9). This chapter uses results from many earlier chapters: the surface tension, **Kelvin equation** and **surfactants** of [6.3.19](/6.3.19), the **Debye length** of [6.3.12](/6.3.12), the **osmotic pressure** of [6.3.5](/6.3.5), the random walk and diffusion equation of [2.5.7](/2.5.7), the **central limit theorem** of [3.1.13](/3.1.13), and the **Rayleigh scattering law** of [5.4.3](/5.4.3). Ultracentrifugation, electrophoresis, gels and the Donnan equilibrium are basic tools and concepts of biochemistry and cell biology.

## 21.1. Dispersions

### 21.1.1. Classification of Dispersions

**Definition 21.1.1** A system formed by one or several substances dispersed in another substance in the form of particles is called a **dispersion** (dispersed system); the substance dispersed is called the **dispersed phase** and the continuous medium that holds the dispersed phase is called the **dispersion medium**.

By the size of the particles of the dispersed phase there are three classes. A system whose particles are single molecules or ions with linear size below about $1\,\mathrm{nm}$ is a molecular dispersion, that is, a true solution, which is single-phase and thermodynamically stable. Larger particles make up colloids and coarse dispersions:

**Definition 21.1.2** A dispersion in which the dispersed particles (molecules or aggregates of molecules) have a linear size between about $1\,\mathrm{nm}$ and $1\,\mu\mathrm{m}$ in at least one direction is called a **colloid**. A dispersion whose particles are larger than about $1\,\mu\mathrm{m}$ in all directions is called a **coarse dispersion** (suspensions, coarse emulsions).

This is the IUPAC definition: because it is based on "at least one direction", thin films (one dimension in the colloidal range) and fibers (two dimensions in the colloidal range) are also colloids; the limits are approximate, not strict boundaries. Many textbooks define a colloid as having particles of "radius" $1$–$100\,\mathrm{nm}$, a range that is too narrow and excludes many typical colloids (emulsions, viruses, organelles). The particle size determines the characteristics of a colloid: below $1\,\mu\mathrm{m}$ Brownian motion is sufficient to offset gravitational sedimentation, the particles are shorter than the wavelength of visible light and scatter it strongly, and the specific surface area is so large that interfacial properties dominate.

Classification by the states of aggregation of the dispersed phase and the dispersion medium:

| Dispersed phase / medium | Name | Examples |
|---|---|---|
| Gas / liquid | Foam | Soap foam, beer foam |
| Liquid / liquid | Emulsion | Milk, crude oil, mayonnaise |
| Solid / liquid | Sol, suspension | Gold sol, ferric hydroxide sol, ink, mud |
| Gas / solid | Solid foam | Foamed plastic, pumice |
| Liquid / solid | Solid emulsion | Minerals with liquid inclusions |
| Solid / solid | Solid sol | Ruby glass, photochromic glass, some alloys |
| Liquid / gas | Liquid aerosol | Fog, cloud |
| Solid / gas | Solid aerosol | Smoke, dust, fine particulate matter in smog |

**Definition 21.1.3** A colloid in which solid particles are dispersed in a liquid and the particles move independently of one another is called a **sol**. A sol in which the dispersed phase is sparingly soluble in the dispersion medium, with a distinct phase boundary between the two, is called a **lyophobic sol**; one in which the dispersed phase dissolves spontaneously in the medium is called a **lyophilic sol**.

A lyophilic sol is in fact a macromolecular solution (a solution of proteins, polysaccharides or synthetic polymers), in which the particles are single molecules; it is a true solution and has some colloidal properties only because the molecular size lies in the colloidal range, so it is now generally called a macromolecular solution (21.9). A system in which the dispersed particles are connected into a network and the whole system loses its fluidity is a gel (21.8). In what follows "sol" means a lyophobic sol unless stated otherwise.

### 21.1.2. Characteristics of Lyophobic Sols

A lyophobic sol has three basic characteristics: multiphase character (it has phase boundaries, in contrast to a true solution); high dispersity (small particles and a large specific surface area, in contrast to coarse dispersions); and thermodynamic instability (the huge interface gives the system a high Gibbs free energy, and the particles tend to coalesce and reduce the interface). The formation of a lyophobic sol therefore has two necessary conditions: the solubility of the dispersed phase in the medium must be small, and a stabilizer (usually a small amount of electrolyte, surfactant or polymer) must be present, or the particles would soon coalesce and sediment. A sol is a system that is kinetically stable but thermodynamically unstable, and its "stability" is relative.

### 21.1.3. Structure of the Colloidal Micelle

Take the AgI sol formed by the reaction of $\ce{AgNO3}$ with KI as an example. When KI is in excess, the surface of the microcrystals formed by the aggregation of many AgI molecules preferentially adsorbs $\ce{I-}$, which has the same composition as the crystal (Fajans' rule), and becomes negatively charged; of the $\ce{K+}$ ions in the solution, acting as counterions, some are adsorbed tightly near the surface and the rest are distributed diffusely in the surrounding medium.

**Definition 21.1.4** The microcrystalline core $(\ce{AgI})_m$ formed by the aggregation of many molecules in a sol is called the **colloidal nucleus**; the nucleus together with the ions adsorbed on its surface and the counterions in the compact layer forms the **colloidal particle**, which moves as a whole in the medium; the colloidal particle together with the counterions in its surrounding diffuse layer forms an electrically neutral structural unit called the **colloidal micelle**.

With KI in excess and with $\ce{AgNO3}$ in excess, the structure of the colloidal micelle is written respectively

$$
\underbrace{[(\ce{AgI})_m\cdot n\ce{I-}\cdot(n-x)\ce{K+}]^{x-}}_{\text{colloidal particle}}\cdot x\ce{K+}, \qquad [(\ce{AgI})_m\cdot n\ce{Ag+}\cdot(n-x)\ce{NO3-}]^{x+}\cdot x\ce{NO3-},
$$
where $m$, $n$ and $x$ are not definite numbers, and the colloidal micelles in the same sol differ in size. When a sol is said to be charged, it is the colloidal particle that is charged; the colloidal micelle as a whole is electrically neutral. The interface between the colloidal particle and the diffuse layer is the slipping plane of electrokinetic phenomena (21.5.3). Note that the colloidal micelle must not be confused with the micelle formed by the association of surfactants ([6.3.19](/6.3.19)); they are two different concepts.

The shape of the colloidal particles strongly affects the properties of a sol: sols of spherical particles (AgI, gold sol) flow well, while sols of rod-like or plate-like particles ($\ce{V2O5}$, clay, tobacco mosaic virus) have a high viscosity, form gels easily, and show thixotropy and flow birefringence.

## 21.2. Preparation, Purification and Aging of Sols

### 21.2.1. Dispersion and Condensation Methods

To prepare a sol is to bring the size of the dispersed particles into the colloidal range and to add a suitable stabilizer. There are two classes of methods:

- Dispersion methods (top-down): bulk material is dispersed into colloidal particles. Mechanical dispersion (colloid mill, jet milling); peptization, in which a small amount of electrolyte is added as a stabilizer to a fresh precipitate to redisperse it, as when a little $\ce{FeCl3}$ is added to a precipitate of $\ce{Fe(OH)3}$; ultrasonic dispersion, mostly for preparing emulsions; the arc method, in which an electric arc is struck between two metal electrodes in a liquid and the evaporated metal condenses into a gold, silver or platinum sol.
- Condensation methods (bottom-up): molecules or ions are made to aggregate into colloidal particles. Chemical condensation produces a supersaturated solution of a sparingly soluble substance by a chemical reaction, as in the hydrolysis of $\ce{FeCl3}$ in boiling water to give a $\ce{Fe(OH)3}$ sol and the reduction of $\ce{HAuCl4}$ by sodium citrate to give a gold sol; physical condensation, as when metal vapor is passed into cold water; change of solvent, as when an ethanol solution of sulfur is poured into water, in which sulfur has an extremely small solubility, and precipitates as a sol. Vapor deposition (evaporating a substance by heating in an inert gas or with a laser and condensing it) is a common method of preparing nanopowders.

### 21.2.2. Purification of Sols

The excess electrolyte formed in preparation can serve as a stabilizer in small amounts, but too much compresses the double layer and coagulates the sol (21.6), and it must be removed.

**Definition 21.2.1** The method of separating a sol from pure solvent by a semipermeable membrane that lets only small molecules and ions pass and not colloidal particles, so that impurities diffuse out through the membrane, is called **dialysis**; the method of using a semipermeable membrane as a filter, so that under a pressure difference the medium and small-molecule impurities pass through and the colloidal particles remain on the membrane, is called **ultrafiltration**.

Applying an electric field across the semipermeable membrane to make ions migrate directionally can speed up dialysis, which is called electrodialysis; electrodialysis and ultrafiltration can also be combined. The artificial kidney (hemodialysis) is a medical application of dialysis: blood flows inside hollow-fiber membranes with dialysate outside, small molecules such as urea and creatinine and excess electrolytes pass through the membrane and are removed, and proteins and blood cells remain in the blood. In biochemistry, dialysis bags and ultrafiltration centrifuge tubes are used to desalt protein solutions, change buffers and concentrate them.

### 21.2.3. Nucleation, Growth and Aging

Preparing a sol by condensation goes through two stages, the formation and the growth of nuclei ([6.3.19](/6.3.19#sec-19.2.5)). von Weimarn pointed out that, with solute concentration $c$ and solubility $c_{\mathrm{s}}$, the nucleation rate depends on the relative supersaturation $(c - c_{\mathrm{s}})/c_{\mathrm{s}}$, whereas the crystal growth rate $r_2 = DA_{\mathrm{s}}(c - c_{\mathrm{s}})/\delta$ ($D$ is the diffusion coefficient, $A_{\mathrm{s}}$ the crystal surface area and $\delta$ the thickness of the diffusion layer) is determined by the diffusion of the solute. When the relative supersaturation is large, nucleation dominates, a large number of nuclei form instantly, the solute is quickly used up, and a large number of fine particles result, which favors the formation of a sol; when the relative supersaturation is small, nucleation is slow and growth dominates, and a small number of larger crystals precipitate. In analytical chemistry, to obtain crystalline precipitates of large particles that are easy to filter, the precipitant is added slowly to a dilute, hot solution to lower the relative supersaturation, which is just the opposite of the conditions for preparing a sol. To obtain particles of uniform size, nucleation must occur within a short time and afterward only growth and no further nucleation (the LaMer model).

The particles of a sol gradually become larger on standing. By the **Ostwald–Freundlich equation** the solubility of small particles is greater than that of large ones, and in the same solution a solution that is saturated with respect to small particles is already supersaturated with respect to large ones.

**Definition 21.2.2** The process in a dispersion in which, because the solubility (or vapor pressure) of small particles is higher than that of large ones, substance is transferred from small particles through the medium to large particles, so that small particles gradually disappear and large ones grow, is called **Ostwald ripening**.

This is the main cause of the aging of sols (particles becoming larger and finally precipitating); it also makes small droplets in emulsions disappear, foams coarsen ([6.3.19](/6.3.19)), and the ice crystals in ice cream grow larger on long standing. The "digestion" of precipitates in analytical chemistry also uses this process. Theory (Lifshitz–Slyozov–Wagner) gives a mean particle diameter whose cube grows linearly with time.

## 21.3. Kinetic Properties

### 21.3.1. Brownian Motion

In 1827 the botanist Brown observed under the microscope that tiny particles that escaped from pollen grains and were suspended in water moved ceaselessly and irregularly; he repeated the experiment with powders of inorganic substances and saw the same motion, thereby excluding the explanation by a "vital force".

**Definition 21.3.1** The perpetual irregular motion of microscopic particles suspended in a fluid, caused by the random collisions of molecules of the medium, is called **Brownian motion**.

The smaller the particle, the higher the temperature and the lower the viscosity of the medium, the more violent the Brownian motion; it does not weaken with time. The cause is that molecules of the medium strike the particle from all directions; when the particle is very small, the impacts from different directions do not cancel at a given instant and the particle moves under the resultant force; when the particle is very large (larger than about $5\,\mu\mathrm{m}$), the resultant force of the impacts is negligible compared with the inertia of the particle and Brownian motion can no longer be seen. Einstein (1905) and Smoluchowski (1906) explained Brownian motion quantitatively by statistical methods. Each displacement of the particle is the result of a large number of independent collisions, and successive displacements are independent, so the trajectory of the particle is a random walk ([2.5.7](/2.5.7#sec-7.5.1)).

**Theorem 21.3.1 (Einstein–Smoluchowski Relation)** In time $t$, the displacement $x$ of a Brownian particle along any direction follows a **normal distribution** with zero mean, and its variance (mean square displacement) is

$$
\overline{x^2} = 2Dt, \tag{21.1}
$$
where the diffusion coefficient $D = k_{\mathrm{B}}T/f$ and $f$ is the friction coefficient of the particle moving in the medium (the ratio of resistance to velocity). For a spherical particle of radius $r$, $f = 6\pi\eta r$ (Stokes drag), so

$$
\overline{x^2} = \frac{k_{\mathrm{B}}T}{3\pi\eta r}t = \frac{RT}{N_{\mathrm{A}}}\cdot\frac{t}{3\pi\eta r}.
$$
In three-dimensional space $\overline{r^2} = 6Dt$.

**Proof** Suppose the particle makes an independent step along the $x$ direction every interval $\tau$, with the step length having mean zero and variance $h^2$. The displacement at $t = n\tau$ is the sum of $n$ independent identically distributed steps, and by the **central limit theorem** ([3.1.13](/3.1.13)), for large $n$, $x$ approximately follows $\mathcal{N}(0, nh^2) = \mathcal{N}(0, 2Dt)$ with $D = h^2/(2\tau)$. This is exactly the fundamental solution of the diffusion equation (the heat kernel): a large number of particles starting from the origin at the same time have a concentration that diffuses according to Fick's second law ([2.5.7](/2.5.7#sec-7.5.1)), so $D$ is the macroscopic diffusion coefficient.

Next find $D$. Einstein's argument is as follows: suppose the particles reach an equilibrium distribution under an external force $F$; by the **Boltzmann distribution** $c(x) \propto \exp(-U(x)/k_{\mathrm{B}}T)$ with $F = -\mathrm{d}U/\mathrm{d}x$, so $\mathrm{d}c/\mathrm{d}x = cF/(k_{\mathrm{B}}T)$. At equilibrium the drift flux $cF/f$ caused by the external force and the diffusion flux $-D\,\mathrm{d}c/\mathrm{d}x$ cancel: $cF/f = DcF/(k_{\mathrm{B}}T)$, and hence $D = k_{\mathrm{B}}T/f$. Substituting the Stokes drag gives the result. $\square$

$D = k_{\mathrm{B}}T/(6\pi\eta r)$ is the **Stokes–Einstein equation** ([6.3.17](/6.3.17)). The significance of this result is that it connects the macroscopic, measurable $\overline{x^2}$, $\eta$ and $r$ with the Boltzmann constant (and therefore with the Avogadro constant). Perrin (1908) followed particles of gamboge and mastic under a microscope and, using this relation and sedimentation equilibrium (21.3.3), measured $N_{\mathrm{A}} \approx 6 \times 10^{23}\,\mathrm{mol^{-1}}$, in agreement with other methods, providing decisive evidence for the real existence of molecules, for which he received the 1926 Nobel Prize in Physics.

**Example 21.3.1** In water at $25\,{}^\circ\mathrm{C}$ ($\eta = 0.890\,\mathrm{mPa\,s}$) a spherical particle of radius $100\,\mathrm{nm}$ has $D = 1.381 \times 10^{-23} \times 298.15/(6\pi \times 0.890 \times 10^{-3} \times 10^{-7})\,\mathrm{m^2\,s^{-1}} = 2.45 \times 10^{-12}\,\mathrm{m^2\,s^{-1}}$. The root-mean-square displacement along $x$ in 1 s is $\sqrt{2Dt} = 2.2\,\mu\mathrm{m}$, and in 1 min it is $17\,\mu\mathrm{m}$: the displacement is proportional to the square root of time, not to time.

![Left: three simulated two-dimensional trajectories, each 10 s long, of a spherical particle of radius 100 nm in water at 25 °C (a Gaussian step every 0.01 s, D = kBT/(6πηr) = 2.45 μm²/s). Right: the mean square displacement averaged over 2000 such particles grows linearly with time, in agreement with the Einstein–Smoluchowski relation ⟨r²⟩ = 4Dt](./plots/brownian.py)

### 21.3.2. Diffusion

When there is a concentration gradient in a sol, Brownian motion causes a net migration of colloidal particles from the concentrated to the dilute region; this is diffusion, which obeys **Fick's law** ([5.2.2](/5.2.2)): the amount of particles passing through unit cross section per unit time is $J = -D\,\mathrm{d}c/\mathrm{d}x$. The diffusion coefficients of colloidal particles are several orders of magnitude smaller than those of small molecules (about $10^{-9}\,\mathrm{m^2\,s^{-1}}$ for small molecules in water, $10^{-11}$–$10^{-13}\,\mathrm{m^2\,s^{-1}}$ for colloidal particles), so colloidal particles diffuse slowly and cannot pass through a semipermeable membrane. Once $D$ is measured, the Stokes–Einstein equation gives the hydrodynamic radius of the particle, which is the principle of particle sizing by dynamic light scattering (21.4.3). For nonspherical particles or solvated macromolecules the radius obtained from $D$ is an equivalent hydrodynamic radius.

### 21.3.3. Sedimentation and Sedimentation Equilibrium

**Definition 21.3.2** The downward (outward) motion of particles of the dispersed phase in a gravitational or centrifugal field is called **sedimentation**.

A spherical particle of radius $r$ and density $\rho_{\mathrm{p}}$ in a medium of density $\rho_0$ and viscosity $\eta$ is subject to the difference between gravity and buoyancy, $\frac{4}{3}\pi r^3(\rho_{\mathrm{p}} - \rho_0)g$, and the Stokes drag $6\pi\eta rv$. When the two balance, the particle sinks at constant velocity,

$$
v = \frac{2r^2(\rho_{\mathrm{p}} - \rho_0)g}{9\eta}.
$$
Measuring the sedimentation velocity gives the particle radius, which is the basis of sedimentation analysis of particle size distributions; conversely, measuring the falling velocity of a small sphere of known radius and density gives the **viscosity** of a liquid (the falling-ball viscometer).

**Example 21.3.2** In water at $20\,{}^\circ\mathrm{C}$ the sedimentation velocity of a gold particle of radius $10\,\mathrm{nm}$ ($\rho_{\mathrm{p}} = 19.3\,\mathrm{g\,cm^{-3}}$) is $v = 2 \times 10^{-16} \times 18.3 \times 10^3 \times 9.81/(9 \times 1.00 \times 10^{-3})\,\mathrm{m\,s^{-1}} = 4.0 \times 10^{-9}\,\mathrm{m\,s^{-1}}$, so it sinks only about $0.35\,\mathrm{mm}$ a day, whereas the root-mean-square displacement from Brownian motion in 1 s is already about $7\,\mu\mathrm{m}$: sedimentation is completely offset by diffusion, which is the kinetic stability of a sol.

**Definition 21.3.3** Sedimentation increases the concentration in the lower part, and diffusion makes the particles migrate upward again; the state in which the two rates are equal and the concentration distribution no longer changes with time is called **sedimentation equilibrium**.

At sedimentation equilibrium the sum of the sedimentation flux $cv$ and the upward diffusion flux $-D\,\mathrm{d}c/\mathrm{d}h$ per unit cross section at height $h$ is zero. Substituting $v$ and $D = k_{\mathrm{B}}T/(6\pi\eta r)$,

$$
\frac{\mathrm{d}\ln c}{\mathrm{d}h} = -\frac{\frac{4}{3}\pi r^3(\rho_{\mathrm{p}} - \rho_0)g}{k_{\mathrm{B}}T}, \qquad \ln\frac{c_2}{c_1} = -\frac{\frac{4}{3}\pi r^3(\rho_{\mathrm{p}} - \rho_0)gN_{\mathrm{A}}}{RT}(h_2 - h_1).
$$
This is exactly the Boltzmann distribution in a gravitational field (the isothermal barometric formula of the atmosphere, [5.2.1](/5.2.1#sec-1.7)), with the molecular mass replaced by the particle mass corrected for buoyancy, so it is independent of the viscosity of the medium. For the gold particles of Example 21.3.2, the characteristic height over which the concentration falls to $1/\mathrm{e}$ is $k_{\mathrm{B}}T/(m_{\mathrm{eff}}g) \approx 5.4\,\mathrm{mm}$; when the radius increases to $100\,\mathrm{nm}$ the characteristic height shortens to $5.4\,\mu\mathrm{m}$ and the particles are almost all at the bottom. Perrin counted mastic particles at different heights and found $N_{\mathrm{A}}$ from this formula.

### 21.3.4. Ultracentrifugation

Colloidal particles and biological macromolecules sediment too slowly in a gravitational field, and a centrifugal field is needed. In the 1920s Svedberg invented the ultracentrifuge, with a speed of tens of thousands of revolutions per minute and a centrifugal acceleration $\omega^2x$ of up to several hundred thousand times the acceleration of gravity ($x$ is the distance from the axis of rotation).

**Definition 21.3.4** The method of making particles sediment in the centrifugal field produced by an ultracentrifuge running at tens of thousands of revolutions per minute, in order to determine their molar mass, size and shape or to separate them, is called **ultracentrifugation**.

The sedimentation equilibrium method: when sedimentation equilibrium is reached in the centrifugal field, replace $g$ in the above formula by $\omega^2x$ and integrate ($\int\omega^2x\,\mathrm{d}x = \frac{1}{2}\omega^2x^2$); for a macromolecule of molar mass $M$ and partial specific volume $\bar v$ (the increase in volume of the solution per unit mass of solute),

$$
M = \frac{2RT\ln(c_2/c_1)}{(1 - \bar v\rho_0)\,\omega^2(x_2^2 - x_1^2)}.
$$

This follows from thermodynamic equilibrium and requires no knowledge of the molecular shape, but a long time is needed to reach equilibrium.

The sedimentation velocity method: when a particle sediments at constant velocity in the centrifugal field, $m(1 - \bar v\rho_0)\omega^2x = fv$.

**Definition 21.3.5** The sedimentation velocity per unit centrifugal acceleration, $s = v/(\omega^2x)$, is called the **sedimentation coefficient**, with unit the Svedberg ($1\,\mathrm{S} = 10^{-13}\,\mathrm{s}$).

Substituting $f = k_{\mathrm{B}}T/D$ gives the Svedberg equation

$$
M = \frac{sRT}{D(1 - \bar v\rho_0)}.
$$
The molar mass can be found from the sedimentation coefficient and the diffusion coefficient, independently of the molecular shape.

**Example 21.3.3** For hemoglobin in water at $20\,{}^\circ\mathrm{C}$, $s = 4.5\,\mathrm{S}$, $D = 6.9 \times 10^{-11}\,\mathrm{m^2\,s^{-1}}$, $\bar v = 0.749\,\mathrm{cm^3\,g^{-1}}$ and $\rho_0 = 0.998\,\mathrm{g\,cm^{-3}}$. $M = 4.5 \times 10^{-13} \times 8.314 \times 293.15/(6.9 \times 10^{-11} \times 0.2525)\,\mathrm{kg\,mol^{-1}} = 63\,\mathrm{kg\,mol^{-1}}$, close to the $64.5\,\mathrm{kg\,mol^{-1}}$ calculated from the amino acid sequence. It was by ultracentrifugation that Svedberg first showed that proteins are macromolecules of definite molar mass and not colloidal aggregates of indefinite composition (Nobel Prize in Chemistry 1926).

Sedimentation coefficients are widely used in biology as the names of particles: the ribosome of prokaryotes is 70S and consists of the two subunits 50S and 30S, and that of eukaryotes is 80S (60S + 40S). $s$ depends on mass and shape, so the values cannot be added. Density-gradient centrifugation (Meselson and Stahl in 1958 used a CsCl gradient to distinguish DNA containing $^{15}\mathrm{N}$ from that containing $^{14}\mathrm{N}$, proving the semiconservative replication of DNA) and differential centrifugation for separating organelles are both applications of ultracentrifugation.

### 21.3.5. Osmotic Pressure

Colloidal particles cannot pass through a semipermeable membrane, and there is also an **osmotic pressure** between a sol and the pure medium, which can be estimated with the formula for dilute solutions $\varPi = (n/V)RT$, where $n/V$ is the amount concentration of colloidal particles. The concentration of a lyophobic sol cannot be very large and the colloidal particles are aggregates of many molecules, so the number of particles is small and the measured osmotic pressure and the other colligative properties are very small: for a gold sol of $1\,\mathrm{g\,L^{-1}}$ with particles of radius $10\,\mathrm{nm}$ the particle concentration is only $2 \times 10^{-8}\,\mathrm{mol\,L^{-1}}$ and the osmotic pressure about $0.05\,\mathrm{Pa}$. Macromolecular solutions can be made fairly concentrated, and the osmotic pressure method is the classical method for determining their number-average molar mass (21.9.3).

## 21.4. Optical Properties

### 21.4.1. The Tyndall Effect

When a beam of light enters a dispersion, reflection, refraction, scattering and absorption can occur. When the particles are much larger than the wavelength of the incident light (coarse dispersions), reflection and refraction dominate and the system is turbid and opaque; when the particles are smaller than the wavelength, scattering dominates and every particle becomes a source emitting secondary light waves in all directions.

**Definition 21.4.1** The phenomenon in which a luminous path can be seen from the side when a beam of light passes through a sol is called the **Tyndall effect**.

The Tyndall effect is the result of the scattering of light by colloidal particles. For a true solution the optical inhomogeneity between molecules and solvent is extremely small and the scattered light is very weak; coarse dispersions are turbid because reflection dominates. The Tyndall effect is therefore the simplest way of distinguishing a sol from a true solution. The "beams of light" seen in daily life (sunlight through a forest or a window, searchlight beams) are the result of scattering by aerosols in the air. Zsigmondy used scattered light to design the ultramicroscope (1903, observing in dark field the light spots scattered by colloidal particles), which can count colloidal particles invisible to the naked eye and observe their Brownian motion, for which he received the 1925 Nobel Prize in Chemistry.

### 21.4.2. Rayleigh Scattering

When the particle size is much smaller than the wavelength (about $< \lambda/10$) and the particles are nonconducting and nonabsorbing, the scattering obeys the **Rayleigh scattering law** ([5.4.3](/5.4.3#sec-3.4.2)). Written in the form for colloids, for $\nu$ particles of volume $V$ per unit volume the total intensity of the scattered light is

$$
I = \frac{24\pi^3\nu V^2}{\lambda^4}\left(\frac{n_1^2 - n_2^2}{n_1^2 + 2n_2^2}\right)^2 I_0,
$$
where $I_0$ is the incident intensity and $n_1$, $n_2$ are the refractive indices of the dispersed phase and the dispersion medium. Several conclusions follow:

- The scattered intensity is inversely proportional to the fourth power of the wavelength: the shorter the wavelength of the incident light, the stronger the scattering. Under white light the scattered light of a sol is bluish violet and the transmitted light orange-red; the blue of the sky and the red of the setting sun have the same explanation.
- The larger the difference between the refractive indices of the dispersed phase and the dispersion medium, the stronger the scattering. The refractive index difference of a macromolecular solution is very small and the Tyndall effect is very weak.
- The scattered intensity is proportional to the number of particles per unit volume and to the square of the particle volume. At a given (mass) concentration $c$, $\nu V \propto c$, so $I \propto cV \propto cr^3$: at the same concentration the larger the particles, the stronger the scattering (within the Rayleigh range). By comparing the scattered intensities of two sols, knowing the concentration or the particle size of one, the other can be found; this is turbidimetry and the nephelometer.

The color of a gold sol does not come from scattering but from absorption: the free electrons of gold nanoparticles oscillate collectively in the optical field (surface plasmon resonance) and absorb green light strongly at about $520\,\mathrm{nm}$, so a gold sol of small particles is red; when the particles become larger or aggregate the absorption peak shifts to the red and the color turns purple and blue. The red glass of medieval churches and the red line of antigen test strips both use gold nanoparticles.

**Definition 21.4.2** After light passes through a sample of length $l$, the transmitted intensity is attenuated by scattering according to $I_{\mathrm{t}} = I_0\mathrm{e}^{-\tau l}$, and the coefficient $\tau$ is called the **turbidity**.

The physical meaning of turbidity is the reciprocal of the path length over which the transmitted intensity falls to $1/\mathrm{e}$ of the incident intensity. It has the same form as the Beer–Lambert law, but the attenuation comes from scattering and not from absorption.

### 21.4.3. Dynamic Light Scattering

Brownian motion keeps changing the positions of the scattering particles, the interference among the light scattered by the individual particles fluctuates accordingly, and the scattered intensity flickers rapidly on time scales of microseconds to milliseconds. The smaller the particles the faster they move and the faster the flicker.

**Definition 21.4.3** The method of measuring the fluctuations of the scattered intensity with time and finding the diffusion coefficient and size of the particles from the decay rate of its autocorrelation function is called **dynamic light scattering** (DLS).

For monodisperse particles the field autocorrelation function decays as $\exp(-Dq^2\tau)$, with scattering vector $q = (4\pi n/\lambda)\sin(\vartheta/2)$ ($\vartheta$ is the scattering angle and $n$ the refractive index of the medium). $D$ is found from the decay rate and the hydrodynamic radius then follows from the Stokes–Einstein equation. The measuring range of DLS is about $1\,\mathrm{nm}$–$1\,\mu\mathrm{m}$, and a measurement takes only a few minutes; it is a routine method for determining the sizes of nanoparticles, protein aggregates and liposomes, and is complementary to static light scattering, which measures the average scattered intensity (to find the weight-average molar mass, 21.9.2).

## 21.5. Electrical Properties

### 21.5.1. Origin of the Charge on Colloidal Particles

Colloidal particles are usually charged, for several reasons:

- Adsorption: colloidal particles have a large specific surface area and preferentially adsorb ions of the medium with the same or a similar composition (Fajans' rule). In an AgI sol, for example, the particle adsorbs $\ce{Ag+}$ and is positively charged when $\ce{AgNO3}$ is in excess, and adsorbs $\ce{I-}$ and is negatively charged when KI is in excess. The ions that determine the surface charge are called potential-determining ions.
- Ionization: groups on the surface of the particle dissociate in the medium. The silanol groups $\ce{Si-OH}$ on the surface of silica gel release $\ce{H+}$ and the surface is negatively charged in neutral and alkaline solutions; the carboxyl and amino groups on the surface of a protein dissociate or bind protons according to pH, so that it is positively charged below the isoelectric point and negatively charged above it.
- Isomorphous substitution: in the lattice of clay minerals $\ce{Al^3+}$ is replaced by $\ce{Mg^2+}$ and $\ce{Si^4+}$ by $\ce{Al^3+}$, the lattice becomes negatively charged, and this is why clay is negatively charged and can retain nutrients such as $\ce{K+}$ and $\ce{NH4+}$ in soil.
- Unequal dissolution: when an ionic crystal is sparingly soluble, cations and anions dissolve or diffuse at different rates, and an excess of one kind of ion is left on the surface of the particle.

### 21.5.2. Models of the Electric Double Layer

An **electric double layer** forms between the surface of a charged colloidal particle and the surrounding medium ([6.1.11](/6.1.11#def-11.4.1)), the same as at an electrode–solution interface. The models describing it have gone through three stages.

**Definition 21.5.1** Helmholtz (1853) assumed that the surface charge and the counterions in solution each form a layer, like the two plates of a parallel-plate capacitor, separated by a distance $d$ of about one ionic radius; this model is called the **Helmholtz double-layer model**.

In this model the potential of the double layer falls linearly between the two layers, and the capacitance per unit area is $C = \varepsilon_{\mathrm{r}}\varepsilon_0/d$ (**permittivity**, [5.3.4](/5.3.4)). For $d = 0.3\,\mathrm{nm}$ and $\varepsilon_{\mathrm{r}} \approx 6$ for water in the compact layer, $C \approx 18\,\mu\mathrm{F\,cm^{-2}}$, in agreement in order of magnitude with measurements on mercury electrodes. But it cannot explain why the capacitance varies with electrolyte concentration and potential, nor can it explain electrokinetic phenomena: according to it, the solution outside the plate is electrically neutral and a moving particle would not carry a potential difference with it.

Counterions are acted on at the same time by electrostatic attraction and by thermal motion, and they do not line up in a neat layer but are denser near the surface and gradually sparser outward, forming a diffuse layer.

**Definition 21.5.2** Gouy (1910) and Chapman (1913) regarded the distribution of ions in the diffuse layer as a Boltzmann distribution in the electrostatic field and determined the potential distribution from the Poisson–Boltzmann equation; this model is called the **Gouy–Chapman model**.

Let the potential of a planar charged surface be $\psi_0$, and let the solution contain a $z$:$z$ symmetric electrolyte of concentration (number density) $n_\infty$. The ions obey the Boltzmann distribution $n_\pm = n_\infty\exp(\mp ze\psi/k_{\mathrm{B}}T)$, and substituting into the **Poisson equation** $\mathrm{d}^2\psi/\mathrm{d}x^2 = -\rho_{\mathrm{e}}/\varepsilon$ ($\varepsilon = \varepsilon_{\mathrm{r}}\varepsilon_0$),

$$
\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = \frac{2zen_\infty}{\varepsilon}\sinh\frac{ze\psi}{k_{\mathrm{B}}T}.
$$

**Theorem 21.5.1** Under the boundary conditions $\psi(0) = \psi_0$, and $\psi \to 0$, $\mathrm{d}\psi/\mathrm{d}x \to 0$ as $x \to \infty$, the solution of this equation is

$$
\tanh\frac{ze\psi}{4k_{\mathrm{B}}T} = \tanh\frac{ze\psi_0}{4k_{\mathrm{B}}T}\,\mathrm{e}^{-x/\lambda_{\mathrm{D}}}, \qquad \lambda_{\mathrm{D}} = \sqrt{\frac{\varepsilon k_{\mathrm{B}}T}{2n_\infty z^2e^2}}.
$$
When the surface potential is low ($\lvert ze\psi_0\rvert \ll 4k_{\mathrm{B}}T$, about $\lvert\psi_0\rvert < 25\,\mathrm{mV}$ for a 1-1 electrolyte at $25\,{}^\circ\mathrm{C}$), $\psi = \psi_0\mathrm{e}^{-x/\lambda_{\mathrm{D}}}$. The relation between the surface charge density and the surface potential is $\sigma = \sqrt{8n_\infty\varepsilon k_{\mathrm{B}}T}\,\sinh\dfrac{ze\psi_0}{2k_{\mathrm{B}}T}$ (the Grahame equation).

**Proof** Let $y = ze\psi/(k_{\mathrm{B}}T)$; the equation becomes $y'' = \lambda_{\mathrm{D}}^{-2}\sinh y$. Multiplying both sides by $2y'$ and integrating, with $y = y' = 0$ at infinity, gives $y'^2 = 2\lambda_{\mathrm{D}}^{-2}(\cosh y - 1) = 4\lambda_{\mathrm{D}}^{-2}\sinh^2(y/2)$. For $\psi_0 > 0$ the potential decreases with $x$, and we take $y' = -2\lambda_{\mathrm{D}}^{-1}\sinh(y/2)$. Separating variables, $\int\mathrm{d}y/\sinh(y/2) = 2\ln\tanh(y/4)$, so $\ln\tanh(y/4) - \ln\tanh(y_0/4) = -x/\lambda_{\mathrm{D}}$, which is the first formula. For small $y$, $\tanh(y/4) \approx y/4$ and the exponential decay follows. The surface charge and the charge of the diffuse layer are equal in magnitude and opposite in sign, and by Gauss's theorem $\sigma = -\varepsilon(\mathrm{d}\psi/\mathrm{d}x)_{x=0}$; substituting $y'(0)$ gives the Grahame equation. $\square$

$\lambda_{\mathrm{D}}$ is the **Debye length** ([6.3.12](/6.3.12)), the effective thickness of the diffuse layer; it is the same quantity as the radius of the ionic atmosphere, since both are solutions of the same Poisson–Boltzmann equation. In an aqueous 1-1 electrolyte solution at $25\,{}^\circ\mathrm{C}$, $\lambda_{\mathrm{D}} = 0.304\,\mathrm{nm}/\sqrt{c/(\mathrm{mol\,L^{-1}})}$: about $9.6\,\mathrm{nm}$ at $1\,\mathrm{mmol\,L^{-1}}$, about $1\,\mathrm{nm}$ at $0.1\,\mathrm{mol\,L^{-1}}$, and about $0.8\,\mathrm{nm}$ in physiological saline (about $0.15\,\mathrm{mol\,L^{-1}}$). The larger the electrolyte concentration and the higher the valence (the larger the **ionic strength**), the thinner the diffuse layer.

![Potential in the diffuse layer near a surface with ψ0 = 100 mV in a 1-1 electrolyte at 25 °C, computed from the nonlinear Gouy–Chapman solution for concentrations of 1, 10 and 100 mmol/L (Debye lengths 9.6, 3.0, 0.96 nm); the dotted lines are the linearized exponential decay ψ0 exp(−x/λD), which overestimates the potential when ψ0 is not small](./plots/gouy-chapman.py)

The Gouy–Chapman model treats the ions as point charges and, at high potential, gives unreasonably high ion concentrations right next to the surface and a double-layer capacitance that is too large.

**Definition 21.5.3** Stern (1924) divided the double layer into two parts: a layer right next to the surface with a thickness of about the radius of a hydrated ion (the Stern layer, in which the counterions are strongly adsorbed and the potential falls approximately linearly), and the diffuse layer outside it, which obeys the Gouy–Chapman distribution; the boundary between the two, the closest plane that the centers of hydrated counterions can reach, is called the **outer Helmholtz plane** (OHP). This model is called the **Stern model**.

The double-layer capacitance of the Stern model is the compact-layer capacitance and the diffuse-layer capacitance in series: at high electrolyte concentration the diffuse layer is very thin and its capacitance very large, so the total capacitance is determined by the compact layer and is close to the Helmholtz model; at low concentration it is determined by the diffuse layer and is close to the Gouy–Chapman model. It also allows specifically adsorbed ions to enter the compact layer, even making the potential at the outer side of the compact layer opposite in sign to the surface potential.

### 21.5.3. Thermodynamic Potential and the ζ Potential

When a colloidal particle moves, the ions in the compact layer and some solvent molecules move together with it, while the more distant ions in the diffuse layer stay behind in the medium.

**Definition 21.5.4** The boundary between the liquid layer that moves together with a colloidal particle and the medium when the particle moves is called the **slipping plane**; the potential difference between the slipping plane and the bulk of the solution is called the **zeta potential** (electrokinetic potential, ζ potential).

The ζ potential is different from the potential of the solid surface relative to the bulk of the solution (the thermodynamic potential $\psi_0$): $\psi_0$ is located at the surface of the colloidal nucleus and is determined by the activity of the potential-determining ions in the solution in equilibrium with the solid (for AgI, $\psi_0$ varies with $\lg a(\ce{Ag+})$ according to the Nernst relation); the ζ potential is located at the slipping plane, which lies a short distance outside the OHP, so the ζ potential is only a part of the thermodynamic potential and in general $\lvert\zeta\rvert < \lvert\psi_0\rvert$. The magnitude of the ζ potential reflects the degree to which the colloidal particle is charged, and its sign is the sign of the charge on the particle.

The ζ potential is very sensitive to electrolytes in the medium. Adding electrolyte compresses the diffuse layer (the Debye length decreases), lowers the potential at the slipping plane and reduces the absolute value of the ζ potential; when the diffuse layer is compressed to coincide with the slipping plane, ζ = 0 and the colloidal particle is in the isoelectric state. Adding counterions of high valence or ones that adsorb specifically, which enter the compact layer, can change the sign of the ζ potential. The ζ potential of a protein varies with pH and is zero at the isoelectric point. Empirically, an aqueous sol is fairly stable when $\lvert\zeta\rvert$ exceeds about $30\,\mathrm{mV}$.

### 21.5.4. Electrokinetic Phenomena

**Definition 21.5.5** The phenomena in which the dispersed phase and the dispersion medium move relative to each other under an applied electric field, or in which a potential difference arises when they move relative to each other under an applied force, are collectively called **electrokinetic phenomena**. There are four specific ones:

1. **Electrophoresis**: under an applied electric field, charged colloidal particles (or macromolecules) move directionally in the dispersion medium;
2. **Electroosmosis**: under an applied electric field, the dispersion medium moves directionally relative to a stationary charged surface (a capillary wall, a porous plug);
3. **Sedimentation potential**: the potential difference produced in the direction of sedimentation when charged particles of the dispersed phase sediment in a gravitational or centrifugal field;
4. **Streaming potential**: the potential difference produced between the two ends of a porous plug or capillary when a liquid flows through it under a pressure difference.

In electrophoresis and electroosmosis an electric field causes motion, and in sedimentation and streaming potentials motion produces an electric field; the two groups are inverse processes of each other, both originate in the relative motion on the two sides of the slipping plane and are determined by the same ζ potential.

**Definition 21.5.6** The electrophoretic velocity of a colloidal particle per unit electric field strength, $u_{\mathrm{E}} = v/E$, is called the **electrophoretic mobility**.

**Theorem 21.5.2 (Smoluchowski Formula)** For a very thin double layer ($\lambda_{\mathrm{D}} \ll$ particle radius $a$),

$$
u_{\mathrm{E}} = \frac{\varepsilon_{\mathrm{r}}\varepsilon_0\zeta}{\eta},
$$
independent of the size and shape of the particle. For a very thick double layer ($\lambda_{\mathrm{D}} \gg a$) the Hückel formula $u_{\mathrm{E}} = 2\varepsilon_{\mathrm{r}}\varepsilon_0\zeta/(3\eta)$ applies; the intermediate case is bridged between the two by the Henry function.

**Proof** (thin double layer) Near the surface of the particle the double layer can be regarded as planar. In the reference frame moving with the particle, the tangential electric field $E$ acts on the charges of the diffuse layer and is balanced by the viscous force of the liquid: $\eta\,\mathrm{d}^2v/\mathrm{d}x^2 = -\rho_{\mathrm{e}}E = \varepsilon(\mathrm{d}^2\psi/\mathrm{d}x^2)E$ (using the Poisson equation). At $x \to \infty$, $\mathrm{d}v/\mathrm{d}x = \mathrm{d}\psi/\mathrm{d}x = 0$, and one integration gives $\eta\,\mathrm{d}v/\mathrm{d}x = \varepsilon E\,\mathrm{d}\psi/\mathrm{d}x$; at the slipping plane $v = 0$ and $\psi = \zeta$, far away $\psi = 0$, and a second integration gives the velocity of the distant liquid relative to the particle, $v_\infty = -\varepsilon\zeta E/\eta$. The particle therefore moves relative to the liquid with velocity $\varepsilon\zeta E/\eta$. $\square$

**Example 21.5.1** In water at $25\,{}^\circ\mathrm{C}$ ($\varepsilon_{\mathrm{r}} = 78.4$, $\eta = 0.890\,\mathrm{mPa\,s}$), a colloidal particle with $\zeta = -30\,\mathrm{mV}$ has $u_{\mathrm{E}} = 78.4 \times 8.854 \times 10^{-12} \times (-0.030)/(0.890 \times 10^{-3})\,\mathrm{m^2\,V^{-1}\,s^{-1}} = -2.3 \times 10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}$ and moves about $23\,\mu\mathrm{m}$ per second in a field of $1000\,\mathrm{V\,m^{-1}}$, of the same order as the **ionic mobility** of small ions ([6.3.12](/6.3.12), about $5 \times 10^{-8}\,\mathrm{m^2\,V^{-1}\,s^{-1}}$). Measuring the electrophoretic mobility is the main method of measuring the ζ potential (modern instruments use laser Doppler electrophoresis).

Electrophoresis is a basic method for separating biological macromolecules, but the situation differs from molecule to molecule. DNA carries one negative phosphate charge per nucleotide, so both its charge and its friction coefficient are proportional to its length, and in free solution DNA of all lengths (above a few hundred base pairs) has almost the same electrophoretic mobility and cannot be separated by size; electrophoresis must be carried out in an agarose or polyacrylamide gel (21.8), where the sieving action of the gel network makes long chains move slowly and short chains fast. Proteins are different: their charge varies with amino acid composition and pH, and their mobility in free solution depends on both charge and size (hydrodynamic radius), so electrophoretic mobility is related to molecular size. To separate proteins by size one can use SDS–polyacrylamide gel electrophoresis: SDS binds to the denatured polypeptide chain in a roughly constant proportion (about 1.4 g SDS per gram of protein), masking the intrinsic charge of the protein and giving all proteins similar charge-to-mass ratios, so that the mobility is determined mainly by sieving in the gel; to separate by charge, isoelectric focusing is used, in which proteins migrate in a pH gradient and stop at their isoelectric points. In capillary electrophoresis the electroosmotic flow caused by the negatively charged quartz wall pushes all components toward the cathode, and the components are then separated by their electrophoretic mobilities. Electroosmosis is also used for the purification of sols and the dewatering of clay and peat; flowing or sedimenting water droplets in oil pipelines and tanks can produce very high streaming and sedimentation potentials and sparks, so grounding against static electricity is necessary.

## 21.6. Stability and Coagulation of Sols

### 21.6.1. Reasons for the Stability of Sols

Lyophobic sols are thermodynamically unstable but can be kept for a long time (the gold sol prepared by Faraday in 1857 is still on display at the Royal Institution in Britain). Their stability has three sources:

- Kinetic stability: the particles are small, Brownian motion is vigorous, and sedimentation in a gravitational field is difficult (Example 21.3.2).
- Stability against coalescence: between particles there are both van der Waals attraction and the electrostatic repulsion caused by the overlap of double layers. When two particles are far apart repulsion dominates, and a potential barrier must be crossed for them to coalesce (21.6.3). This is the main reason for the stability of lyophobic sols.
- Solvation layer: the ions and counterions on the surface of the colloidal particle are solvated and form a solvation film around the particle, which acts as a mechanical obstacle when particles approach.

**Definition 21.6.1** The process in a sol in which particles coalesce, grow larger and finally sediment out of the medium is called **coagulation**.

### 21.6.2. Coagulation by Electrolytes

A small amount of electrolyte is a stabilizer of a sol: the adsorption of potential-determining ions charges the particles. With more electrolyte, the counterions compress the diffuse layer, the ζ potential and the repulsive barrier fall, the sol coagulates, and the electrolyte has become the coagulant.

**Definition 21.6.2** The lowest concentration of electrolyte needed under given conditions to make a sol coagulate markedly within a given time is called the **critical coagulation concentration**; its reciprocal is called the coagulating power.

The coagulating power of electrolytes follows several rules. First, the ions that act mainly are those of charge opposite to that of the colloidal particles (counterions), and their valence has the greatest influence.

**Definition 21.6.3** For electrolytes whose counterions are monovalent, divalent and trivalent, the ratio of the critical coagulation concentrations is about $100 : 1.6 : 0.14$, that is, the critical coagulation concentration is roughly inversely proportional to the sixth power of the counterion valence, $(1/1)^6 : (1/2)^6 : (1/3)^6$. This rule is called the **Schulze–Hardy rule**.

For example, for a negatively charged $\ce{As2S3}$ sol the critical coagulation concentration is about $50\,\mathrm{mmol\,L^{-1}}$ for NaCl, KCl and $\ce{KNO3}$, about $0.7\,\mathrm{mmol\,L^{-1}}$ for $\ce{MgCl2}$, $\ce{CaCl2}$ and $\ce{BaCl2}$, and about $0.09\,\mathrm{mmol\,L^{-1}}$ for $\ce{AlCl3}$. Second, counterions of the same valence also differ in coagulating power.

**Definition 21.6.4** The order in which counterions of the same valence are arranged by coagulating power is called the **lyotropic series** (Hofmeister series). For negatively charged sols the coagulating power of monovalent cations is $\ce{H+} > \ce{Cs+} > \ce{Rb+} > \ce{NH4+} > \ce{K+} > \ce{Na+} > \ce{Li+}$; for positively charged sols the coagulating power of monovalent anions is $\ce{F-} > \ce{Cl-} > \ce{Br-} > \ce{NO3-} > \ce{I-}$.

The order of the cations is the same as the order of hydrated ionic radius from small to large: the smaller the hydrated radius, the more easily the ion approaches the surface of the colloidal particle and enters the compact layer ($\ce{H+}$ comes first because of its special adsorption). Hofmeister first (1888) discovered this kind of ion order in the salting-out of proteins, and it likewise affects the solubility and stability of proteins and the selectivity of ion-exchange resins. There are several further rules:

- The higher the valence of the ions with the same sign as the colloidal particle (co-ions), the weaker the coagulating power; organic ions (surfactant ions, dye ions) have a very strong coagulating power because of their strong adsorption.
- Irregular coagulation: when a counterion of high valence or an organic counterion is gradually added to a sol, a small amount coagulates the sol, a little more redisperses the precipitate with the colloidal particles carrying the opposite charge, and still more coagulates it again. The reason is that the specific adsorption of these ions first lowers the ζ potential to zero, then reverses it, and finally the double layer is compressed.
- Mutual coagulation: mixing two sols with opposite charges also causes coagulation, which is most complete when the charges just neutralize. The colloidal particles of one sol can be regarded as high-valence "giant ions" added to the other sol. Water purification with alum is the mutual coagulation of the positive $\ce{Al(OH)3}$ sol with the negatively charged clay colloidal particles in the water.

Polymers have two opposite effects on sols.

**Definition 21.6.5** The action by which a small amount of added polymer causes several colloidal particles of a sol to be adsorbed and bridged by the same polymer chain and to form a loose flocculent precipitate is called **flocculation**; the action by which a sufficient amount of added polymer has its adsorbed layer completely enclose the colloidal particles and prevent them from approaching and coalescing is called **steric stabilization**.

Flocculation has an optimum dosage that depends on the chain length, charge and groups of the polymer, and polyacrylamide flocculants are widely used in water treatment and mineral processing. Sterically stabilized sols tolerate more electrolyte and higher temperature, show the properties of lyophilic sols, and can be redispersed after precipitation; the protection of gold and silver sols by gelatin and gum arabic (protective colloids), and the PEG modification of the surface of drug nanoparticles (to prolong the circulation time in the blood), both use steric stabilization.

### 21.6.3. DLVO Theory

Derjaguin and Landau (1941) and Verwey and Overbeek (1948) independently put forward a quantitative theory of the stability of sols.

**Definition 21.6.6** The theory that takes the interaction energy between two colloidal particles as the sum of the van der Waals attraction energy and the electrostatic repulsion energy caused by the overlap of the double layers, and judges the stability of a sol from the variation of the total interaction energy with the distance between particles, is called the **DLVO theory**.

The attraction energy comes from the sum of the **van der Waals forces** (mainly **dispersion forces**) among all the molecules making up the two particles. The attraction potential energy between two molecules decays with the sixth power of the distance, but after integration over two macroscopic particles it decays much more slowly. For two spheres of radius $r$ with closest surface separation $H \ll r$,

$$
V_{\mathrm{A}} = -\frac{A_{\mathrm{H}}r}{12H},
$$
where $A_{\mathrm{H}}$ is called the *Hamaker constant*, determined by the polarizabilities of the two materials and the medium, about $10^{-20}$–$10^{-19}\,\mathrm{J}$ for colloids in water. The repulsion energy comes from the overlap of the diffuse layers of the two particles: the ion concentration in the overlap region rises and produces an osmotic pressure that pushes the particles apart. For weak overlap of the diffuse layers, $\lambda_{\mathrm{D}} \ll r$,

$$
V_{\mathrm{R}} = \frac{64\pi rn_\infty k_{\mathrm{B}}T\gamma_0^2}{\kappa^2}\mathrm{e}^{-\kappa H}, \qquad \kappa = \frac{1}{\lambda_{\mathrm{D}}}, \quad \gamma_0 = \tanh\frac{ze\psi_{\mathrm{d}}}{4k_{\mathrm{B}}T},
$$
where $\psi_{\mathrm{d}}$ is the potential at the beginning of the diffuse layer (the OHP). The total interaction energy is $V = V_{\mathrm{A}} + V_{\mathrm{R}}$: the attraction energy dominates at very short and very long distances ($1/H$ decays more slowly than an exponential) and the repulsion energy dominates at intermediate distances, so $V(H)$ has a deep primary minimum at very short distance (particle contact and coalescence), a barrier at intermediate distance, and possibly a shallow secondary minimum at larger distance.

![DLVO interaction energy of two spheres of radius 100 nm (Hamaker constant 2 × 10⁻²⁰ J, diffuse-layer potential 35 mV) in a 1-1 electrolyte at 25 °C, for concentrations of 1, 10, 50, 111 and 300 mmol/L: at low concentration the barrier is as high as tens of kBT, falls as the double layer is compressed, and disappears at the critical coagulation concentration (about 111 mmol/L for this set of parameters), where the curve is tangent to the zero line with zero slope](./plots/dlvo.py)

When the barrier is much higher than $k_{\mathrm{B}}T$ (tens of $k_{\mathrm{B}}T$), thermally moving particles can hardly cross it and the sol is stable. As the electrolyte concentration increases, $\kappa$ increases, the repulsion energy decays faster and the barrier falls; when the barrier disappears the particles coalesce at the first contact and the sol coagulates rapidly. When the secondary minimum is deep (large particles, medium electrolyte concentration), the particles can aggregate loosely at a larger distance; this aggregation is reversible, and gentle stirring or dilution disperses them again.

**Theorem 21.6.1** The condition for the barrier to just disappear is $V = 0$ and $\mathrm{d}V/\mathrm{d}H = 0$, which gives $\kappa H = 1$, and the corresponding electrolyte number density (the critical coagulation concentration) is

$$
n_{\mathrm{c}} = \frac{73\,728\,\pi^2\varepsilon^3(k_{\mathrm{B}}T)^5\gamma_0^4}{\mathrm{e}^2A_{\mathrm{H}}^2e^6z^6},
$$
where $\mathrm{e}$ is the base of natural logarithms, $e$ is the elementary charge and $\varepsilon = \varepsilon_{\mathrm{r}}\varepsilon_0$. At high surface potential $\gamma_0 \to 1$ and $n_{\mathrm{c}} \propto z^{-6}$, which is the Schulze–Hardy rule.

**Proof** Write $V = B\mathrm{e}^{-\kappa H} - A_{\mathrm{H}}r/(12H)$ with $B = 64\pi rn_\infty k_{\mathrm{B}}T\gamma_0^2/\kappa^2$. $V = 0$ gives $B\mathrm{e}^{-\kappa H} = A_{\mathrm{H}}r/(12H)$; $\mathrm{d}V/\mathrm{d}H = -\kappa B\mathrm{e}^{-\kappa H} + A_{\mathrm{H}}r/(12H^2) = 0$. Substituting the former into the latter, $-\kappa/H + 1/H^2 = 0$, that is, $\kappa H = 1$. Substituting back into the former, $B\mathrm{e}^{-1} = A_{\mathrm{H}}r\kappa/12$, that is,

$$
n_\infty = \frac{\mathrm{e}A_{\mathrm{H}}\kappa^3}{768\pi k_{\mathrm{B}}T\gamma_0^2}.
$$
Substituting $\kappa^2 = 2n_\infty z^2e^2/(\varepsilon k_{\mathrm{B}}T)$ and $\kappa^3 = (2z^2e^2/(\varepsilon k_{\mathrm{B}}T))^{3/2}n_\infty^{3/2}$ and solving for $n_\infty$ gives the result. $\square$

The particle radius $r$ cancels in the result, so the critical coagulation concentration is independent of particle size, in agreement with experiment. At low surface potential $\gamma_0 \approx ze\psi_{\mathrm{d}}/(4k_{\mathrm{B}}T)$ and $n_{\mathrm{c}} \propto \psi_{\mathrm{d}}^4/z^2$, so the influence of valence weakens; the actual variation of the critical coagulation concentration of sols with valence often lies between $z^{-2}$ and $z^{-6}$, and the specific adsorption of counterions of high valence also lowers $\psi_{\mathrm{d}}$ and makes ions of high valence still stronger coagulants. DLVO theory also explains most phenomena other than the lyotropic series, but it does not take into account hydration, steric hindrance and ion specificity, and these "non-DLVO forces" are important at short distances. The stability of protein solutions at low salt through electrostatic repulsion and their salting-out at high salt can also be understood in part with DLVO theory.

## 21.7. Emulsions and Microemulsions

**Definition 21.7.1** A dispersion formed by one liquid dispersed in the form of droplets in another liquid immiscible with it is called an **emulsion**. The dispersed liquid is called the internal phase and the other liquid the external phase. Oil dispersed in water is called oil-in-water (O/W) and water dispersed in oil water-in-oil (W/O).

The droplet diameter of emulsions is generally above $0.1\,\mu\mathrm{m}$ (often $0.1$–$10\,\mu\mathrm{m}$); emulsions have an enormous oil–water interface, are thermodynamically unstable, and finally separate into two layers by creaming, flocculation, coalescence and Ostwald ripening. Milk, soy milk and mayonnaise are of the O/W type, while butter and the water-containing emulsions in crude oil are mostly of the W/O type.

**Definition 21.7.2** A third substance that keeps an emulsion stable for a certain time is called an **emulsifier**.

Commonly used emulsifiers are surfactants, natural products such as proteins, phospholipids (lecithin) and gums, and solid powders. The actions of an emulsifier are: lowering the oil–water interfacial tension and reducing the work needed for dispersion; forming a protective film of some strength on the surface of the droplets (the oriented-wedge theory: the end of the emulsifier molecule with the larger cross section points toward the external phase); an ionic emulsifier charges the droplets and forms an electric double layer; and solid microparticles adsorbed at the oil–water interface form a "suit of armor" (a Pickering emulsion): hydrophilic particles that are well wetted by water (contact angle below $90^\circ$) make water the external phase and give the O/W type, and the reverse gives the W/O type.

The type of an emulsion is mainly determined by the emulsifier. Bancroft's rule says that the phase in which the emulsifier is more soluble becomes the external phase: hydrophilic emulsifiers with a **hydrophile–lipophile balance** of 8–18 (sodium soaps, $\ce{C12E8}$) give the O/W type, and lipophilic emulsifiers with 3–6 (calcium soaps, Span) give the W/O type ([6.3.19](/6.3.19#sec-19.7.4)). The type can be identified by dilution (an emulsion that can be diluted with water is O/W), by dyeing (a water-soluble dye colors the external phase of an O/W emulsion), and by conductivity (an O/W emulsion conducts well).

The conversion of an O/W emulsion into a W/O one, or the reverse, is called inversion of the emulsion (phase inversion), and can be brought about by adding an emulsifier of the opposite type (for example adding $\ce{CaCl2}$ to an O/W emulsion stabilized by sodium soap, which forms calcium soap), or by changing the volume ratio of the two phases or the temperature; an emulsion with a nonionic emulsifier inverts at a certain temperature (the phase inversion temperature, related to the cloud point). The process of making an emulsion separate into two layers is called demulsification: a substance that destroys the protective film of the emulsifier is added, or physical methods such as centrifugation, heating, filtration and a high-voltage electric field are used. Crude oil must be demulsified, dewatered and desalted with a high-voltage electric field before processing.

**Definition 21.7.3** A thermodynamically stable transparent or translucent dispersion formed spontaneously from oil and water under the action of a surfactant (usually together with a cosurfactant, such as an alcohol of medium chain length) is called a **microemulsion**.

A microemulsion differs from an emulsion and the two must not be confused: the droplet diameter of a microemulsion is about $10$–$100\,\mathrm{nm}$, it is transparent, the oil–water interfacial tension falls below $10^{-3}\,\mathrm{mN\,m^{-1}}$, and it forms spontaneously and is stable for a long time; it can also be a bicontinuous structure in which both oil and water are continuous. An emulsion is a turbid system that is kinetically stable and can be formed only by supplying energy through stirring, homogenization or ultrasound. A system in between, with droplets of $20$–$200\,\mathrm{nm}$ and thermodynamically unstable, is called a nanoemulsion. Microemulsions are used in tertiary oil recovery, as carriers of drugs and cosmetics, and in the preparation of nanoparticles by the reverse micelle method ([6.3.19](/6.3.19#sec-19.7.6)).

## 21.8. Gels

**Definition 21.8.1** A dispersion in which the dispersed particles or macromolecules are connected into a three-dimensional network throughout the system, with the dispersion medium filling the network and the whole system having lost its fluidity and acquired a certain elasticity, is called a **gel**. A gel whose dispersion medium is water is called a **hydrogel**; one from which the liquid has been removed by methods such as supercritical drying while the network structure is retained, so that the dispersion medium is a gas, is called an **aerogel**.

There are two routes to prepare gels: dry macromolecules absorb solvent and swell to form a gel (such as gelatin, agar and polyacrylamide in water); or a solution or sol, under suitable conditions (lowering the temperature, changing the pH, adding electrolyte, crosslinking reactions), has its dispersed particles linked together, that is, gelation (such as the cooling of a gelatin solution and the gelation of a silicic acid sol into silica gel). According to the nature of the network there are two classes: elastic gels formed by crosslinking flexible linear macromolecules, for which dehydration and water uptake are reversible (gelatin, agar, rubber); and rigid gels formed by connecting rigid particles, which become xerogels on dehydration and generally cannot absorb water to recover their original state (silica gel, alumina gel).

The main properties of gels are swelling, syneresis and thixotropy. An elastic gel increases in volume when it absorbs liquid and exerts a swelling pressure on the container that restrains it; the swelling pressure of dry seeds in water can split rocks. When a gel stands, the network gradually tightens and liquid separates from the gel, which is called syneresis (shrinkage with expulsion of liquid), as in the retraction of a blood clot with release of serum and the release of whey from yogurt.

**Definition 21.8.2** The property of certain gels of turning into a flowing sol on stirring or shaking and returning to a gel on standing is called **thixotropy**.

The reason is that the network structure is weak (plate-like or rod-like particles connected by weak interactions), is destroyed by mechanical action and forms again on standing. Drilling mud (bentonite), paint and tomato ketchup are thixotropic. Small molecules and ions diffuse in a hydrogel almost as fast as in water, whereas macromolecules are subject to the sieving action of the network, which is the basis of gel electrophoresis (21.5.4) and gel filtration chromatography; precipitation reactions carried out in a gel can also form periodic precipitation rings (Liesegang rings).

Aerogels consist almost entirely of air (porosities of over 99%); silica aerogel is one of the solids of lowest density, has an extremely low thermal conductivity, and is used for thermal insulation and for capturing cosmic dust on spacecraft. In preparation one must avoid the additional pressure of the meniscus of the liquid collapsing the network during drying, so the liquid in the pores is first converted to a supercritical fluid and then removed ([6.3.8](/6.3.8#sec-8.5.4)). In living organisms the extracellular matrix, mucus, the vitreous body and cartilage are all hydrogels; the cytoskeletal network of the cytoplasm also gives it the properties of a gel. Hydrogels are also used in soft contact lenses, wound dressings, tissue engineering scaffolds and sustained drug release.

## 21.9. Macromolecular Solutions and the Donnan Equilibrium

### 21.9.1. Characteristics of Macromolecular Solutions

**Definition 21.9.1** A homogeneous solution formed by natural or synthetic polymers of very high molar mass (generally above $10^4\,\mathrm{g\,mol^{-1}}$) dissolved as single molecules in a solvent is called a **macromolecular solution**.

The size of macromolecules lies in the colloidal range, and they share some properties with sols: the particle size is about $1\,\mathrm{nm}$–$1\,\mu\mathrm{m}$, they diffuse slowly and cannot pass through a semipermeable membrane. But in essence they are true solutions, fundamentally different from sols:

| Property | Macromolecular solution | Lyophobic sol |
|---|---|---|
| Particles | Single macromolecules | Aggregates of many molecules |
| Phase | Homogeneous, no phase boundary | Multiphase, with phase boundaries |
| Thermodynamics | Stable, dissolves spontaneously, dissolution is reversible | Unstable, needs a stabilizer, generally irreversible after coagulation |
| Tyndall effect | Weak (small refractive index difference) | Strong |
| Viscosity | High (molecules extended and solvated) | Low, close to that of the medium |
| Toward electrolytes | Insensitive, salting-out only with large amounts of electrolyte | Very sensitive, coagulated by small amounts of electrolyte |

### 21.9.2. Average Molar Mass

Synthetic polymers are always mixtures of molecules with different degrees of polymerization, and natural polymers (polysaccharides) often are too, so one can speak only of an average molar mass, and the result depends on how the average is taken. Let the sample contain $n_i$ moles of molecules of molar mass $M_i$, with mass $m_i = n_iM_i$.

**Definition 21.9.2** The quantities

$$
\bar M_{\mathrm{n}} = \frac{\sum_in_iM_i}{\sum_in_i}, \qquad \bar M_{\mathrm{w}} = \frac{\sum_in_iM_i^2}{\sum_in_iM_i} = \frac{\sum_im_iM_i}{\sum_im_i}, \qquad \bar M_z = \frac{\sum_in_iM_i^3}{\sum_in_iM_i^2}, \qquad \bar M_\eta = \left(\frac{\sum_in_iM_i^{1+\alpha}}{\sum_in_iM_i}\right)^{1/\alpha}
$$
are called respectively the **number-average molar mass** (averaged over the number of molecules), the **weight-average molar mass** (averaged over mass), the **Z-average molar mass** and the **viscosity-average molar mass** ($\alpha$ is the exponent in the Mark–Houwink equation, 21.9.4).

Different methods of measurement give different averages: colligative properties (osmotic pressure) and end-group analysis count the number of molecules and give $\bar M_{\mathrm{n}}$; the scattered intensity in static light scattering is proportional to $\sum_ic_iM_i$ and gives $\bar M_{\mathrm{w}}$; sedimentation equilibrium gives $\bar M_{\mathrm{w}}$ and $\bar M_z$; viscometry gives $\bar M_\eta$. Nowadays size-exclusion chromatography (gel permeation chromatography) is commonly used to measure the whole molar mass distribution. For a general polydisperse sample, $\bar M_{\mathrm{n}} \le \bar M_\eta \le \bar M_{\mathrm{w}} \le \bar M_z$ ($0 < \alpha < 1$), with equality only for a monodisperse sample. The ratio $Đ = \bar M_{\mathrm{w}}/\bar M_{\mathrm{n}} \ge 1$ is called the molar mass dispersity (the name recommended by IUPAC, formerly the polydispersity index; not to be confused with the dispersion of a catalyst), and measures the breadth of the distribution: $\bar M_{\mathrm{w}}/\bar M_{\mathrm{n}} - 1$ is exactly the ratio of the variance of the number distribution to $\bar M_{\mathrm{n}}^2$. Proteins and DNA are monodisperse ($Đ = 1$); the "most probable distribution" of step-growth polymerization has $Đ = 2$; living polymerization can give samples with $Đ < 1.1$.

![Schulz–Zimm (gamma-type) molar mass distribution with number-average molar mass 50 kg/mol and dispersity 2, the vertical axis being the mass fraction per unit molar mass, with the four averages marked: Mn = 50, Mη = 93 (Mark–Houwink exponent α = 0.7), Mw = 100, Mz = 150 kg/mol](./plots/molar-mass.py)

### 21.9.3. Osmotic Pressure and the Virial Expansion

The osmotic pressure of macromolecular solutions is considerable and is the classical method of determining $\bar M_{\mathrm{n}}$ ([6.3.5](/6.3.5)). But macromolecular solutions deviate from ideal dilute solutions already at very low concentration: the volume occupied by a flexible long chain is far greater than its own volume, and both the repulsion between chains (excluded volume) and the segment–solvent interactions are strong. We therefore expand the **osmotic pressure** as a power series in the mass concentration $c$ (unit $\mathrm{g\,L^{-1}}$, that is, $\mathrm{kg\,m^{-3}}$),

$$
\frac{\varPi}{c} = RT\left(\frac{1}{\bar M_{\mathrm{n}}} + A_2c + A_3c^2 + \cdots\right), \tag{21.2}
$$
completely analogous to the virial equation of real gases ([6.3.1](/6.3.1)); $A_2$ and $A_3$ are called the second and third osmotic **virial coefficients**. Plotting $\varPi/c$ against $c$ and extrapolating to $c \to 0$, $\bar M_{\mathrm{n}}$ is obtained from the intercept and $A_2$ from the slope.

**Example 21.9.1** The osmotic pressure of a polymer in a good solvent is measured at $25\,{}^\circ\mathrm{C}$:

| $c/(\mathrm{g\,L^{-1}})$ | 2.0 | 4.0 | 6.0 | 8.0 |
|---|---|---|---|---|
| $\varPi/\mathrm{Pa}$ | 54.5 | 119.0 | 193.4 | 277.6 |

The values of $\varPi/c$ are 27.25, 29.75, 32.23, 34.70 $\mathrm{Pa\,L\,g^{-1}}$ in turn, a straight line against $c$ with intercept $24.78\,\mathrm{Pa\,L\,g^{-1}} = 24.78\,\mathrm{J\,kg^{-1}}$ and slope $1.242\,\mathrm{J\,m^3\,kg^{-2}}$. Hence $\bar M_{\mathrm{n}} = RT/\text{intercept} = 2479/24.78\,\mathrm{kg\,mol^{-1}} = 100\,\mathrm{kg\,mol^{-1}}$ and $A_2 = \text{slope}/RT = 5.0 \times 10^{-4}\,\mathrm{mol\,m^3\,kg^{-2}}$. If the solution were treated as an ideal dilute solution, the single point at $c = 8\,\mathrm{g\,L^{-1}}$ would give a molar mass of only $71\,\mathrm{kg\,mol^{-1}}$.

$A_2$ reflects the "quality" of the solvent. Flory and Huggins (1942) treated a polymer solution as a mixture of chains and solvent molecules on a lattice and obtained the *Flory–Huggins theory*: the Gibbs free energy of mixing is

$$
\Delta_{\mathrm{mix}}G = RT(n_1\ln\phi_1 + n_2\ln\phi_2 + \chi n_1\phi_2),
$$
where $\phi_1$ and $\phi_2$ are the volume fractions of solvent and polymer and $\chi$ is the interaction parameter between segments and solvent. The first two terms are the entropy of mixing; because a macromolecule consists of many connected segments, it is much smaller than the entropy of mixing of a mixture of small molecules with the same volume fractions, which is the origin of the nonideality of systems close to athermal solutions mentioned in [6.3.6](/6.3.6). This gives $A_2 = (\tfrac{1}{2} - \chi)\bar v^2/V_{\mathrm{m},1}$ ($\bar v$ is the partial specific volume of the polymer and $V_{\mathrm{m},1}$ the molar volume of the solvent). For $\chi < \tfrac{1}{2}$, $A_2 > 0$: a good solvent, in which the chains are extended; for $\chi = \tfrac{1}{2}$, $A_2 = 0$: the solution behaves like an ideal solution at this temperature (the θ temperature), called a θ solvent, in which the excluded-volume effect of the chain is just canceled by the attraction between segments; for $\chi > \tfrac{1}{2}$, $A_2 < 0$: a poor solvent, from which the polymer may precipitate. The $A_2$ of protein solutions is also used to judge whether the interaction between proteins is repulsive or attractive, and the conditions for crystallization.

### 21.9.4. Viscometry

The viscosity of a macromolecular solution is much larger than that of the pure solvent and depends on the size and shape of the macromolecules, so molar mass can be determined from viscosity. Let the viscosity of the pure solvent be $\eta_0$, that of the solution $\eta$ and the mass concentration $c$, and define:

- the relative viscosity $\eta_{\mathrm{r}} = \eta/\eta_0$;
- the specific viscosity $\eta_{\mathrm{sp}} = (\eta - \eta_0)/\eta_0 = \eta_{\mathrm{r}} - 1$, the fractional increase in viscosity due to the macromolecules;
- the reduced viscosity $\eta_{\mathrm{sp}}/c$ and the inherent viscosity $\ln\eta_{\mathrm{r}}/c$, both with the unit of reciprocal concentration.

**Definition 21.9.3** The limit of the reduced viscosity as the concentration tends to zero,

$$
[\eta] = \lim_{c\to0}\frac{\eta_{\mathrm{sp}}}{c} = \lim_{c\to0}\frac{\ln\eta_{\mathrm{r}}}{c}
$$
is called the **intrinsic viscosity**. It eliminates the influence of interactions among macromolecules and reflects the ability of a single macromolecule to increase the viscosity of the solution.

Experimentally, $\eta_{\mathrm{r}}$ is measured at several concentrations with a capillary viscometer (the efflux time is proportional to viscosity), two straight lines are drawn according to the Huggins equation $\eta_{\mathrm{sp}}/c = [\eta] + k_{\mathrm{H}}[\eta]^2c$ and the Kraemer equation $\ln\eta_{\mathrm{r}}/c = [\eta] - k_{\mathrm{K}}[\eta]^2c$, and extrapolated to $c = 0$, where they meet at the same point, which is $[\eta]$.

**Formula 21.9.1 (Mark–Houwink Equation)** At a given temperature, the relation between the intrinsic viscosity and the molar mass of the same polymer in the same solvent is

$$
[\eta] = KM^\alpha,
$$
where $K$ and $\alpha$ are calibrated with samples of known molar mass.

The exponent $\alpha$ reflects the conformation of the macromolecule in solution: compact spherical particles have $\alpha = 0$ (Einstein's viscosity law $\eta = \eta_0(1 + 2.5\phi)$, with $[\eta]$ independent of $M$; the $[\eta]$ of globular proteins is about $3$–$4\,\mathrm{mL\,g^{-1}}$); random coils in a θ solvent have $\alpha = 0.5$; extended flexible chains in a good solvent have $\alpha = 0.6$–$0.8$; for rigid rod-like molecules (long fragments of DNA, tobacco mosaic virus) $\alpha$ can reach $1.8$. Viscometry needs simple equipment and is precise, and is the most commonly used method in industry for determining the molar mass of polymers; it gives the viscosity-average molar mass $\bar M_\eta$.

### 21.9.5. The Donnan Equilibrium

**Definition 21.9.4** A polymer that dissociates in solution into a macromolecular ion carrying many charges and many small counterions is called a **polyelectrolyte**.

Proteins, nucleic acids, hyaluronic acid and heparin among the polysaccharides, and sodium polyacrylate are all polyelectrolytes. When a solution of a polyelectrolyte is separated from a solution of a small-molecule electrolyte by a semipermeable membrane, the macromolecular ions cannot pass through the membrane but the small ions can; for each side to remain electrically neutral, the small ions are distributed unevenly on the two sides of the membrane at equilibrium.

**Definition 21.9.5** When there are macromolecular ions on one side of a membrane that cannot pass through it, the equilibrium of the uneven distribution that the small ions able to pass through the membrane reach on the two sides is called the **Donnan equilibrium**.

Let the inside of the membrane (left) hold the sodium salt of a protein $\ce{Na_zP}$ at concentration $c_2$, completely dissociated into $\ce{P^{z-}}$ and $z$ $\ce{Na+}$, and the outside (right) hold NaCl at concentration $c_1$, with equal volumes on the two sides. At equilibrium NaCl of concentration $x$ has entered the left side from the right:

| | Left (inside the membrane) | Right (outside the membrane) |
|---|---|---|
| $\ce{P^{z-}}$ | $c_2$ | 0 |
| $\ce{Na+}$ | $zc_2 + x$ | $c_1 - x$ |
| $\ce{Cl-}$ | $x$ | $c_1 - x$ |

**Theorem 21.9.1** In dilute solution (activity coefficients taken as 1), at the Donnan equilibrium

$$
[\ce{Na+}]_{\text{left}}[\ce{Cl-}]_{\text{left}} = [\ce{Na+}]_{\text{right}}[\ce{Cl-}]_{\text{right}}, \qquad x = \frac{c_1^2}{zc_2 + 2c_1},
$$
and the osmotic pressure is

$$
\varPi = \frac{zc_2^2 + 2c_1c_2 + z^2c_2^2}{zc_2 + 2c_1}RT.
$$

**Proof** NaCl can pass through the membrane, and at equilibrium its chemical potentials on the two sides are equal: $\mu(\ce{NaCl}, \text{left}) = \mu(\ce{NaCl}, \text{right})$. From the chemical potential of an electrolyte $\mu = \mu^\circ + RT\ln(a_{\ce{Na+}}a_{\ce{Cl-}})$ ([6.3.12](/6.3.12)), $a_{\ce{Na+}}a_{\ce{Cl-}}$ is equal on both sides, and taking activity coefficients as 1 gives the first formula. (Equivalently, the electrochemical potential of each kind of ion is equal on the two sides, and there is a Donnan potential difference between the two sides.) Substituting the concentrations in the table, $(zc_2 + x)x = (c_1 - x)^2$, and solving gives $x$. The osmotic pressure is determined by the difference of the total solute particle concentrations on the two sides: $\varPi = RT[(c_2 + zc_2 + 2x) - 2(c_1 - x)] = RT(c_2 + zc_2 - 2c_1 + 4x)$, and substituting $x$ and simplifying gives the result. $\square$

Two limiting cases:

- Without added salt ($c_1 \to 0$): $\varPi = (z + 1)c_2RT$, the counterions also contribute to the osmotic pressure, and the molar mass calculated from it is only $1/(z + 1)$ of the true value; for an uncharged macromolecule $\varPi = c_2RT$.
- Salt concentration much larger than that of the macromolecule ($c_1 \gg zc_2$): $\varPi \to c_2RT$ and the Donnan effect is suppressed. Therefore, when the molar mass of a protein is measured by osmotic pressure, one works near the isoelectric point and adds sufficient salt outside the membrane.

**Example 21.9.2** A protein sodium salt with $c_2 = 1\,\mathrm{mmol\,L^{-1}}$ and $z = 20$, with NaCl of $c_1 = 10\,\mathrm{mmol\,L^{-1}}$ outside the membrane. $x = 100/(20 + 20)\,\mathrm{mmol\,L^{-1}} = 2.5\,\mathrm{mmol\,L^{-1}}$; at equilibrium, inside the membrane $[\ce{Na+}] = 22.5$ and $[\ce{Cl-}] = 2.5$, and outside both are $7.5\,\mathrm{mmol\,L^{-1}}$. The concentration of $\ce{Na+}$ inside the membrane is 3 times that outside, and that of $\ce{Cl-}$ is $1/3$. The osmotic pressure corresponds to an ideal solute of $11\,\mathrm{mmol\,L^{-1}}$, $\varPi = 27\,\mathrm{kPa}$ at $25\,{}^\circ\mathrm{C}$, whereas the protein itself contributes only $2.5\,\mathrm{kPa}$. The potential difference across the two sides (the Donnan potential) is $\varphi_{\text{left}} - \varphi_{\text{right}} = (RT/F)\ln([\ce{Na+}]_{\text{right}}/[\ce{Na+}]_{\text{left}}) = 25.7\,\mathrm{mV} \times \ln(1/3) = -28\,\mathrm{mV}$, negative inside the membrane.

The Donnan equilibrium is important in physiology. Cells contain large amounts of negatively charged proteins and nucleic acids that cannot pass through the cell membrane; by the Donnan equilibrium the total ion concentration inside the cell would be higher than outside, water would keep flowing in by osmosis, and the cell would burst; the cell keeps pumping out $\ce{Na+}$ with the $\ce{Na+}$/$\ce{K+}$-ATPase, so that $\ce{Na+}$ effectively cannot permeate freely, and thus maintains a stable volume (the pump–leak model). The proteins in blood plasma (mainly albumin) cannot pass through the capillary wall and produce a colloid osmotic pressure of about $3.3\,\mathrm{kPa}$ ($25\,\mathrm{mmHg}$), which together with the hydrostatic pressure in the capillary determines the exchange of water between plasma and interstitial fluid (the Starling principle); in hypoproteinemia the colloid osmotic pressure falls and causes edema. For a general discussion of the **membrane potential** and **membrane equilibrium** see [6.3.13](/6.3.13).

## Summary

| Topic | Key points |
|---|---|
| Dispersions | Colloid: about $1\,\mathrm{nm}$–$1\,\mu\mathrm{m}$ in at least one dimension; lyophobic sols are multiphase, highly dispersed and thermodynamically unstable; colloidal micelle $[(\ce{AgI})_m\cdot n\ce{I-}\cdot(n-x)\ce{K+}]^{x-}\cdot x\ce{K+}$ |
| Aging | Small particles have a higher solubility (Ostwald–Freundlich); Ostwald ripening makes particles grow |
| Brownian motion | $\overline{x^2} = 2Dt$, $D = k_{\mathrm{B}}T/f = k_{\mathrm{B}}T/(6\pi\eta r)$; random walk + central limit theorem; Perrin's measurement of $N_{\mathrm{A}}$ |
| Sedimentation | $v = 2r^2\Delta\rho g/(9\eta)$; sedimentation equilibrium is the Boltzmann distribution in a gravitational field; ultracentrifugation: $M = 2RT\ln(c_2/c_1)/[(1 - \bar v\rho_0)\omega^2(x_2^2 - x_1^2)]$, Svedberg equation $M = sRT/[D(1 - \bar v\rho_0)]$ |
| Optical properties | Tyndall effect; Rayleigh: $I \propto \nu V^2/\lambda^4$; turbidity $I_{\mathrm{t}} = I_0\mathrm{e}^{-\tau l}$; DLS finds $D$ from intensity fluctuations |
| Double layer | Helmholtz (parallel-plate capacitor) → Gouy–Chapman (Poisson–Boltzmann, $\psi \approx \psi_0\mathrm{e}^{-x/\lambda_{\mathrm{D}}}$) → Stern (compact layer + diffuse layer); the ζ potential is the potential at the slipping plane |
| Electrokinetic phenomena | Electrophoresis, electroosmosis, sedimentation potential, streaming potential; Smoluchowski $u_{\mathrm{E}} = \varepsilon_{\mathrm{r}}\varepsilon_0\zeta/\eta$, Hückel $2\varepsilon_{\mathrm{r}}\varepsilon_0\zeta/(3\eta)$ |
| Stability and coagulation | Critical coagulation concentration; Schulze–Hardy rule $z^{-6}$; lyotropic series; flocculation and steric stabilization; DLVO: $V = -A_{\mathrm{H}}r/(12H) + V_{\mathrm{R}}$, critical condition $\kappa H = 1$ |
| Emulsions | O/W, W/O; Bancroft's rule and HLB; emulsions are kinetically stable and microemulsions thermodynamically stable (droplets 10–100 nm) |
| Macromolecular solutions | $\bar M_{\mathrm{n}} \le \bar M_\eta \le \bar M_{\mathrm{w}} \le \bar M_z$; $\varPi/c = RT(1/\bar M_{\mathrm{n}} + A_2c + \cdots)$; $A_2 = (\frac{1}{2} - \chi)\bar v^2/V_{\mathrm{m},1}$; $[\eta] = KM^\alpha$ |
| Donnan equilibrium | $[\ce{Na+}]_{\text{in}}[\ce{Cl-}]_{\text{in}} = [\ce{Na+}]_{\text{out}}[\ce{Cl-}]_{\text{out}}$; without salt $\varPi = (z + 1)c_2RT$, with a large amount of salt $\varPi \to c_2RT$ |

## Questions

1. Why is the sky blue on a clear day and a cloud white? Explain with the optical properties of sols.

   Atmospheric molecules and fine aerosol particles are much smaller than the wavelength of light, the scattering obeys Rayleigh's law, and blue light is scattered most strongly; the water droplets in a cloud have diameters of about $10\,\mu\mathrm{m}$, far larger than the wavelength, and scatter all wavelengths about equally, so a cloud is white.
2. An AgI sol is prepared from $\ce{AgNO3}$ and a slight excess of KI. To which electrode do the colloidal particles move in electrophoresis? Which of NaCl, $\ce{MgSO4}$ and $\ce{AlCl3}$ coagulates it most effectively?

   With excess KI the colloidal particles adsorb $\ce{I-}$ and are negatively charged, so they move toward the anode. The ions that cause coagulation are the cations, $\ce{Al^3+}$ has the highest valence, and $\ce{AlCl3}$ is the most effective.
3. Does the electrophoretic mobility of a protein in free solution depend on molecular size? Why must DNA be electrophoresed in a gel to be separated by size?

   It does: the mobility of a protein depends on charge and hydrodynamic radius, both of which vary from protein to protein. Both the charge and the friction coefficient of DNA are proportional to chain length, so in free solution the mobility is almost independent of length, and separation by size is possible only in a gel, through the sieving action of the network.
4. When the molar mass of a protein is determined by osmotic pressure, why is the measurement made near the isoelectric point and with a fairly concentrated salt solution outside the membrane?

   Near the isoelectric point the net charge of the protein is close to zero and $z$ is small; adding a large amount of salt so that $c_1 \gg zc_2$ suppresses the Donnan effect, the osmotic pressure tends to $c_2RT$, and the molar mass calculated from it is then the true one.
