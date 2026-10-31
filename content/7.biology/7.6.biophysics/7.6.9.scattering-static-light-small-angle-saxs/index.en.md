---
title: "Scattering: Static Light Scattering, Small-Angle Scattering and Biological SAXS"
description: Elastic scattering by macromolecules in solution and biological SAXS. The induced dipole and Rayleigh's formula in SI units; the scattering vector; static light scattering, the Rayleigh ratio and the absolute molar mass, concentration fluctuations and the second virial coefficient, the weight-average molar mass and the Zimm plot; the scattering amplitude as a Fourier transform, the Debye formula, form factor and interparticle structure factor; the radius of gyration and the Guinier approximation; the pair-distance distribution function; Porod's law and the invariant; X-ray and neutron contrast, H/D contrast variation, the Stuhrmann relation and the nucleosome; Shannon channels; SAXS beamlines, absolute calibration with water, samples, radiation damage and buffer subtraction; molar mass from I(0), Porod volume and volume of correlation; Kratky plots; the indirect Fourier transform with Tikhonov regularization; scattering from atomic models, ab initio bead models by simulated annealing, rigid-body and ensemble modeling; RNA structure from SAXS; time-resolved SAXS; SAXS in integrative structural biology.
---

A beam of light, X-rays or neutrons passing through a solution of macromolecules is scattered a little in every direction. The scattered intensity and its dependence on angle are among the most direct measurements of what a macromolecule is in solution: how heavy it is, how large, what shape it has, whether it is folded or disordered, and whether its copies attract or repel one another. This chapter first develops the theory common to all these measurements and then turns it into the practice of biological small-angle X-ray scattering (BioSAXS).

The theory begins with a single particle much smaller than the wavelength, whose scattering is **Rayleigh scattering** ([5.4.3](/5.4.3#sec-3.4.2)), and turns it into static light scattering, the standard method for absolute molar masses (9.1–9.2). It then lets the particle be comparable to the wavelength: the waves scattered by different parts interfere, and the angular pattern becomes the **Fourier transform** of the particle's structure, averaged over orientations (9.3). Three regions of the curve give three kinds of information: its beginning the radius of gyration (9.4), its whole the distribution of internal distances (9.5), and its tail the surface and volume (9.6). The contrast between particle and solvent, which can be tuned for neutrons by mixing H₂O and D₂O, lets one see the components of a complex separately (9.7). The same Fourier relation underlies **diffraction** ([5.4.2](/5.4.2#sec-2.3.7)); in a crystal the molecules are ordered, the orientational average disappears and the transform is sampled at the points of a lattice, which is the subject of X-ray crystallography in the next chapter ([7.6.10](/7.6.10)). The fluctuating part of the scattered light, **dynamic light scattering**, measures diffusion and is treated with the hydrodynamic methods in [7.6.8](/7.6.8).

The second half follows a SAXS measurement from what a curve can tell (9.8), the instrument and the sample (9.9) and the primary analysis of the curve (9.10) to three-dimensional modeling (9.11), and then treats two applications in which SAXS is especially strong, RNA (9.12) and time-resolved studies of folding (9.13), before placing it among the other methods (9.14). SAXS gives low-resolution information, but it works in solution, under nearly any condition of buffer, temperature or ligand, for particles from a few kilodaltons to hundreds of megadaltons, in minutes of beam time, and it can follow changes down to microseconds. It is therefore used where the high-resolution methods are weak: for flexible and **intrinsically disordered proteins**, for RNA, for transient complexes and for kinetics, and, increasingly, to test models obtained by crystallography ([7.6.10](/7.6.10)), **nuclear magnetic resonance** ([7.6.13](/7.6.13)), **cryo-electron microscopy** ([7.6.14](/7.6.14)) or prediction ([7.6.15](/7.6.15)) against the molecule as it exists in solution. The overview of structure determination in [7.1.6](/7.1.6#sec-6.6) is the starting point.

## 9.1. Scattering by Small Particles

### 9.1.1. Kinds of Scattering

Light entering matter drives the electrons of every atom into forced oscillation, and each oscillating charge radiates a secondary wave. What is observed is the superposition of these secondary waves. Two distinctions organize the possibilities.

The first concerns energy. In *elastic scattering* the scattered radiation has the frequency of the incident radiation; in *inelastic scattering* it does not. The elastic scattering of light by particles much smaller than the wavelength is Rayleigh scattering, and by larger particles Mie scattering; the inelastic scattering in which molecular vibrations shift the frequency is **Raman scattering** (7.6.11, [6.4.11](/6.4.11)); the inelastic scattering of X-rays by nearly free electrons is **Compton scattering**. Rayleigh scattering of visible light is about $10^{-3}$–$10^{-5}$ of the incident intensity and Raman scattering another three to four orders of magnitude weaker. This chapter deals only with elastic scattering.

The second concerns order and size. The secondary waves from different scatterers interfere, and the result depends on the wavelength $\lambda$, the particle dimension $d$ and the arrangement of the particles:

| Sample | $\lambda \gg d$ | $\lambda \lesssim d$ |
|---|---|---|
| Perfect crystal (rigid, periodic) | waves cancel in all directions except forward (a perfect crystal is transparent) | sharp diffraction maxima in discrete directions: crystallography |
| Gas, liquid, solution (random, moving) | scattering in all directions, intensity set by the number and polarizability of the particles: static light scattering | intensity concentrated in a cone of small angles, its angular profile set by size and shape: small-angle scattering |

In a dilute solution the particles are randomly placed and move, so the waves scattered by different particles have random phases and their intensities add; only the waves scattered by different parts of the same particle interfere. That is the regime of this chapter.

**Definition 9.1.1 (Small-Angle Scattering)** *Small-angle scattering* (SAS) is the elastic scattering of radiation by a sample containing inhomogeneities of nanometer size, recorded at small scattering angles (for X-rays of wavelength $0.1$–$0.2\,\mathrm{nm}$, typically $0.1^\circ$–$5^\circ$). With X-rays scattered by electrons it is called *small-angle X-ray scattering* (SAXS); with neutrons scattered by atomic nuclei, *small-angle neutron scattering* (SANS).

Visible light cannot reveal the shape of a protein: its wavelength is a hundred times the size of the molecule, and all parts scatter in phase. Ultraviolet light below about $300\,\mathrm{nm}$ is absorbed by proteins, nucleic acids and the solvent itself; matter becomes transparent again only for X-rays, whose wavelength of about $0.1\,\mathrm{nm}$ is smaller than a protein. Neutrons with a **de Broglie wavelength** of the same order are the second probe. Their interaction with matter is different, which is the basis of contrast variation (9.7).

### 9.1.2. The Induced Dipole

Let a particle much smaller than the wavelength be placed at the origin in a linearly polarized plane wave $\boldsymbol{E} = \boldsymbol{E}_0\cos(\omega t - kx)$, with $k = 2\pi/\lambda$. The field displaces the electron cloud relative to the nuclei and induces an **electric dipole moment** $\boldsymbol{p} = \alpha\boldsymbol{E}$; the constant $\alpha$ is the **polarizability** of the particle (an **induced dipole**). Since the particle is small, the whole electron cloud feels the same field, and the dipole oscillates as $\boldsymbol{p}(t) = \alpha\boldsymbol{E}_0\cos\omega t$. An oscillating dipole radiates ([5.3.10](/5.3.10#sec-10.4.2)); at a distance $r \gg \lambda$, in a direction making the angle $\phi$ with the dipole, the radiated field has amplitude

$$
E_{\mathrm{s}} = \frac{\omega^2 \alpha E_0 \sin\phi}{4\pi\varepsilon_0 c^2 r} = \frac{k^2 \alpha E_0\sin\phi}{4\pi\varepsilon_0 r}.
$$

**Formula 9.1.1 (Rayleigh Scattering by a Small Particle)** The intensity scattered by a particle of polarizability $\alpha$, at distance $r$ and angle $\phi$ from the direction of the incident field, is

$$
\frac{I_{\mathrm{s}}}{I_0} = \frac{E_{\mathrm{s}}^2}{E_0^2} = \frac{\pi^2\alpha^2}{\varepsilon_0^2\lambda^4 r^2}\sin^2\phi. \tag{9.1}
$$
For unpolarized incident light, the average over the directions of $\boldsymbol{E}_0$ in the plane perpendicular to the beam replaces $\sin^2\phi$ by $(1 + \cos^2\theta)/2$, where $\theta$ is the scattering angle between the incident and scattered directions.

The factor $\lambda^{-4}$ is the **Rayleigh scattering law**. The angular factors are those of dipole radiation: polarized light is not scattered along the direction of its field, and unpolarized light scattered at $90^\circ$ is fully polarized (Figure below, panel B). Modern instruments use a laser polarized perpendicular to the plane in which the detectors lie, so that $\sin\phi = 1$ at every detector.

**Remark 9.1.1 (Units)** Older texts write Eq. (9.1) in Gaussian units, $I_{\mathrm{s}}/I_0 = 16\pi^4\alpha'^2\sin^2\phi/(\lambda^4r^2)$, with the polarizability volume $\alpha' = \alpha/(4\pi\varepsilon_0)$ (dimension of a volume). The two forms are identical. In the final working formula of static light scattering, Eq. (9.4), the polarizability is replaced by a measured refractive-index increment and $\varepsilon_0$ cancels, so the instrument constant $K$ is the same in both systems.

### 9.1.3. The Scattering Vector

Let the incident wave have wave vector $\boldsymbol{k}_{\mathrm{i}}$ and the scattered wave reaching the detector $\boldsymbol{k}_{\mathrm{s}}$. In elastic scattering both have length $k = 2\pi/\lambda$, where $\lambda$ is the wavelength in the medium ($\lambda = \lambda_0/n$ for light in a solvent of refractive index $n$; $n = 1$ for X-rays and neutrons to an accuracy of $10^{-6}$).

**Definition 9.1.2 (Scattering Vector)** The *scattering vector* (momentum transfer) is $\boldsymbol{q} = \boldsymbol{k}_{\mathrm{s}} - \boldsymbol{k}_{\mathrm{i}}$. For elastic scattering through the angle $\theta$ its length is

$$
q = \frac{4\pi n\sin(\theta/2)}{\lambda_0}. \tag{9.2}
$$

The vector diagram of panel A of the figure shows why $q$ is the natural variable. Two volume elements at $\boldsymbol{0}$ and $\boldsymbol{r}$ scatter waves whose paths to a distant detector differ by $(\boldsymbol{s}_1 - \boldsymbol{s}_0)\cdot\boldsymbol{r}$, where $\boldsymbol{s}_0$, $\boldsymbol{s}_1$ are unit vectors along the incident and scattered directions. The phase difference is $k(\boldsymbol{s}_1 - \boldsymbol{s}_0)\cdot\boldsymbol{r} = \boldsymbol{q}\cdot\boldsymbol{r}$. The scattering pattern therefore depends on the wavelength and the angle only through $q$, and a structural feature of length $d$ makes itself felt at $q \approx 2\pi/d$. In X-ray work the scattering angle is usually written $2\theta$, so that $q = 4\pi\sin\theta/\lambda$ (and the same quantity appears in Bragg's law, 7.6.10); in this chapter $\theta$ is the full angle throughout. Some authors use $s = 2\sin(\theta/2)/\lambda = q/2\pi$ instead of $q$.

![Geometry of elastic scattering. A: a plane wave (wave vector k_i, blue wavefronts) is scattered by two volume elements at O and at r towards a distant detector (direction of k_s). The path difference of the two rays is the difference of the projections of r on the scattered and incident directions, (s1 − s0)·r, and the phase difference is q·r with the scattering vector q = k_s − k_i; for elastic scattering through the angle θ the triangle of wave vectors gives q = 4π sin(θ/2)/λ. B: angular distribution of the intensity scattered in the scattering plane by a particle much smaller than the wavelength: incident light polarized perpendicular to the plane (isotropic), polarized in the plane (cos²θ, zero at 90°), and unpolarized, (1 + cos²θ)/2](./plots/scattering-geometry.py)

| Radiation | $\lambda_0$ | Typical $q$ range | Length scales $2\pi/q$ |
|---|---|---|---|
| Visible light (multi-angle detector, water) | $400$–$700\,\mathrm{nm}$ | $0.003$–$0.03\,\mathrm{nm^{-1}}$ | $0.2$–$2\,\mu\mathrm{m}$ |
| X-rays (SAXS) | $0.1$–$0.15\,\mathrm{nm}$ | $0.05$–$5\,\mathrm{nm^{-1}}$ | $1$–$100\,\mathrm{nm}$ |
| Cold neutrons (SANS) | $0.5$–$1\,\mathrm{nm}$ | $0.02$–$5\,\mathrm{nm^{-1}}$ | $1$–$300\,\mathrm{nm}$ |

## 9.2. Static Light Scattering

Measuring the time-averaged intensity of light scattered by a solution, as a function of angle and concentration, is *static light scattering* (SLS; with lasers and many detectors, multi-angle light scattering, MALS). Because the polarizability of a macromolecule is proportional to its mass, the scattered intensity reports the molar mass directly, without any calibration by standards.

### 9.2.1. Molar Mass from the Rayleigh Ratio

**Definition 9.2.1 (Rayleigh Ratio)** For a scattering volume $V$ illuminated with intensity $I_0$, observed at angle $\theta$ and distance $r$, the *Rayleigh ratio* is

$$
R_\theta = \frac{I_{\mathrm{s}}(\theta)\, r^2}{I_0 V},
$$
the scattered intensity per unit solid angle, per unit incident intensity and per unit scattering volume (unit $\mathrm{cm^{-1}}$). For solutions, $R_\theta$ denotes the excess over the pure solvent.

The polarizability of a dissolved macromolecule is obtained from the refractive index. For a dilute suspension of $N$ particles per unit volume, $n^2 - n_0^2 = N\alpha/\varepsilon_0$, where $n_0$ is the refractive index of the solvent and $\alpha$ the excess polarizability of a particle over the solvent it displaces. Writing $n^2 - n_0^2 \approx 2n_0(\mathrm{d}n/\mathrm{d}c)c$ with the mass concentration $c$ and the *refractive-index increment* $\mathrm{d}n/\mathrm{d}c$, and $N = cN_{\mathrm{A}}/M$,

$$
\alpha = \frac{2\varepsilon_0 n_0 M}{N_{\mathrm{A}}}\,\frac{\mathrm{d}n}{\mathrm{d}c}. \tag{9.3}
$$

**Formula 9.2.1 (Molar Mass by Static Light Scattering)** For an ideal dilute solution of particles small compared with the wavelength, illuminated by light of vacuum wavelength $\lambda_0$ polarized perpendicular to the scattering plane, Eqs. (9.1) and (9.3) give, for $N$ independent particles per unit volume,

$$
R_\theta = K c M, \qquad K = \frac{4\pi^2 n_0^2}{N_{\mathrm{A}}\lambda_0^4}\left(\frac{\mathrm{d}n}{\mathrm{d}c}\right)^2. \tag{9.4}
$$
For unpolarized light, $K$ is half as large and $R_\theta$ is conventionally divided by $(1 + \cos^2\theta)$.

The scattered intensity is proportional to the product $cM$: at a given mass concentration, a heavier particle scatters more, because the $M/m$ smaller particles that would have the same mass scatter incoherently (intensities add, $\propto N\alpha^2 \propto (c/M)M^2$), whereas one large particle scatters coherently. Every quantity in $K$ is measurable: $n_0$, $\lambda_0$ and $\mathrm{d}n/\mathrm{d}c$, which for unmodified proteins is nearly universal, $0.185$–$0.19\,\mathrm{mL\,g^{-1}}$ in water at visible wavelengths (it depends on the refractive index of the amino acids, which vary little on average); nucleic acids have about $0.17\,\mathrm{mL\,g^{-1}}$, carbohydrates about $0.145\,\mathrm{mL\,g^{-1}}$, and detergents and lipids still other values, which is the basis of conjugate analysis of glycoproteins and membrane proteins in detergent.

**Example 9.2.1 (Bovine Serum Albumin)** With $\lambda_0 = 658\,\mathrm{nm}$, $n_0 = 1.330$ and $\mathrm{d}n/\mathrm{d}c = 0.185\,\mathrm{mL\,g^{-1}}$,

$$
K = \frac{4\pi^2 (1.330)^2 (0.185)^2}{(6.022\times10^{23}\,\mathrm{mol^{-1}})(6.58\times10^{-5}\,\mathrm{cm})^4} = 2.12\times10^{-7}\,\mathrm{mol\,cm^2\,g^{-2}}.
$$
A solution of the $66.4\,\mathrm{kDa}$ monomer at $1\,\mathrm{mg\,mL^{-1}}$ ($c = 10^{-3}\,\mathrm{g\,mL^{-1}}$) gives $R_\theta = KcM = 1.4\times10^{-5}\,\mathrm{cm^{-1}}$, about the Rayleigh ratio of pure toluene, the usual calibration standard; the covalent dimer, present at a few percent in commercial albumin, scatters twice as much per gram. Because the signal is weighted by mass, dust is fatal: a particle of $1\,\mu\mathrm{m}$ diameter has a mass of about $3\times10^{11}\,\mathrm{Da}$, and even after interference has reduced its scattering at $90^\circ$ a thousandfold, a mass fraction of $10^{-4}$ of such particles scatters as much as the protein: samples and buffers are filtered ($0.1$–$0.22\,\mu\mathrm{m}$) or, more commonly, the light scattering detector is placed after a chromatography column.

### 9.2.2. Concentration Fluctuations and the Second Virial Coefficient

A solution is not a gas of independent particles. Einstein (1910) and Debye (1944) regarded the scattering of a liquid mixture as coming from thermal fluctuations of the composition in volume elements small compared with the wavelength. This view includes the interactions automatically.

**Theorem 9.2.1 (Fluctuation Theory of Solution Scattering)** The excess Rayleigh ratio of a solution at small $q$ is

$$
R_0 = K c\,\frac{RT}{(\partial\varPi/\partial c)_{T}}, \tag{9.5}
$$
where $\varPi$ is the **osmotic pressure**. With the virial expansion $\varPi/c = RT(1/M + A_2c + \cdots)$ ([6.3.21](/6.3.21#sec-21.9.3)),

$$
\frac{Kc}{R_0} = \frac{1}{M} + 2A_2c + \cdots. \tag{9.6}
$$

**Proof** Divide the solution into cells of volume $\delta V$, small compared with $\lambda$ but containing many molecules. A fluctuation $\delta c$ of the mass concentration in a cell changes its polarizability by $\delta\alpha = 2\varepsilon_0 n_0(\mathrm{d}n/\mathrm{d}c)\,\delta c\,\delta V$ (Eq. (9.3) per unit volume). Fluctuations in different cells are uncorrelated, so their scattered intensities add, and by Eq. (9.1) with $\sin\phi = 1$,

$$
R_0 = \frac{1}{\delta V}\cdot\frac{\pi^2\langle\delta\alpha^2\rangle}{\varepsilon_0^2\lambda_0^4} = \frac{4\pi^2n_0^2}{\lambda_0^4}\left(\frac{\mathrm{d}n}{\mathrm{d}c}\right)^2\langle\delta c^2\rangle\,\delta V.
$$
The cell exchanges solute with its surroundings at constant solvent chemical potential, so the number $N$ of solute molecules in it fluctuates with $\langle\delta N^2\rangle = k_{\mathrm{B}}T(\partial N/\partial\mu)$, where $\mu$ is the solute **chemical potential**. The Gibbs–Duhem relation at constant $T$ and solvent potential gives $\mathrm{d}\varPi = (N/\delta V)\,\mathrm{d}\mu$, so $\partial N/\partial\mu = N/(\partial\varPi/\partial(N/\delta V))$. Converting $N/\delta V$ to the mass concentration $c = NM/(N_{\mathrm{A}}\delta V)$ gives $\langle\delta c^2\rangle\,\delta V = k_{\mathrm{B}}T c/(\partial\varPi/\partial c)$, and with $k_{\mathrm{B}} = R/N_{\mathrm{A}}$ the result is Eq. (9.5). For an ideal solution, $\partial\varPi/\partial c = RT/M$ and Eq. (9.5) reduces to Eq. (9.4). $\square$

The second **virial coefficient** $A_2$ measures the net interaction between two solute molecules: $A_2 > 0$ for repulsion (excluded volume, like charges at low ionic strength, [7.6.6](/7.6.6)), $A_2 < 0$ for net attraction. Repulsion suppresses concentration fluctuations and lowers the scattering; attraction enhances them. This is why $Kc/R$ must be extrapolated to $c = 0$ to obtain $M$, and why $A_2$, which light scattering measures directly, is used to choose conditions for protein crystallization (slightly negative $A_2$, the "crystallization slot") and to screen protein formulations for aggregation.

### 9.2.3. Mixtures and the Weight-Average Molar Mass

For a mixture of species with mass concentrations $c_i$ and molar masses $M_i$ (all with the same $\mathrm{d}n/\mathrm{d}c$), the intensities add:

**Formula 9.2.2 (Mixtures)**

$$
R_\theta = K\sum_i c_iM_i = K c\,\bar M_{\mathrm{w}}, \qquad \bar M_{\mathrm{w}} = \frac{\sum_i c_iM_i}{\sum_i c_i},
$$
so static light scattering of a mixture measures the **mass-average molar mass** $\bar M_{\mathrm{w}}$ ([6.3.21](/6.3.21#sec-21.9.2)), and the radius of gyration obtained from the angular dependence (9.2.4) is the z-average.

A monomer–dimer equilibrium thus shows up as an apparent molar mass that increases with concentration from $M$ towards $2M$; the classic example, the reversible dissociation of hemocyanin subunits at low concentration, is visible as a downturn of $\bar M_{\mathrm{w}}$ on dilution. Because $\bar M_{\mathrm{w}}$ weights the heavy species, a $1\,\%$ (by mass) contamination by a hundredfold larger aggregate increases the apparent mass by $100\,\%$.

### 9.2.4. Angular Dependence and the Zimm Plot

When the particle is not small compared with $\lambda$, the waves from its parts interfere and the intensity falls with angle. Anticipating the general result (Theorem 9.4.1), the angular factor at small $q$ is $P(q) \approx 1 - q^2R_{\mathrm{g}}^2/3$, with the radius of gyration $R_{\mathrm{g}}$ of the particle.

**Formula 9.2.3 (Zimm Equation)** For a dilute solution of large particles,

$$
\frac{Kc}{R_\theta} = \frac{1}{\bar M_{\mathrm{w}}P(q)} + 2A_2c \approx \frac{1}{\bar M_{\mathrm{w}}}\left(1 + \frac{q^2R_{\mathrm{g}}^2}{3}\right) + 2A_2c. \tag{9.7}
$$

**Definition 9.2.2 (Zimm Plot)** A *Zimm plot* (Zimm, 1948) displays $Kc/R_\theta$, measured at several angles and concentrations, against $q^2 + kc$, where $k$ is an arbitrary constant chosen to spread the data. Extrapolating each concentration series to $\theta = 0$ and each angle series to $c = 0$ gives two limiting lines with the common intercept $1/\bar M_{\mathrm{w}}$; the slope of the $c = 0$ line is $R_{\mathrm{g}}^2/(3\bar M_{\mathrm{w}})$ and that of the $\theta = 0$ line is $2A_2$ (in units of the abscissa).

![Simulated Zimm plot of a large assembly (Mw = 2.0 × 10⁶ g/mol, Rg = 40 nm, A₂ = 2.0 × 10⁻⁴ mol mL g⁻²) measured at 11 angles from 30° to 150° with a 658 nm laser in water, at four concentrations, with 0.4 % noise. Colored points and dashed lines: one concentration each, extrapolated to θ = 0; grey dashed lines: one angle each, extrapolated to c = 0. The two limiting lines (black, c → 0; green, θ → 0) share the intercept 1/Mw, and their slopes give Rg²/(3Mw) and 2A₂. A global least-squares fit of Eq. (9.7) recovers the three parameters (upper left)](./plots/zimm-plot.py)

A single measurement thus yields the three parameters $\bar M_{\mathrm{w}}$, $R_{\mathrm{g}}$ and $A_2$. The angular dependence, however, is measurable only for large particles. With $\lambda_0 = 658\,\mathrm{nm}$ in water, the largest accessible $q$ (at $\theta \approx 160^\circ$) is $0.025\,\mathrm{nm^{-1}}$, and $q^2R_{\mathrm{g}}^2/3$ there is $2\,\%$ for $R_{\mathrm{g}} = 10\,\mathrm{nm}$ and $0.04\,\%$ for lysozyme ($R_{\mathrm{g}} \approx 1.4\,\mathrm{nm}$). Light scattering gives the radius of gyration of viruses, large assemblies, polymers and aggregates, roughly $R_{\mathrm{g}} \gtrsim 10\,\mathrm{nm}$; for ordinary proteins it gives only the mass, and the size and shape require X-rays.

### 9.2.5. Light Scattering after Size-Exclusion Chromatography

In practice the light scattering detector is placed after a **size-exclusion chromatography** column, together with an ultraviolet absorbance or differential refractive-index detector that measures $c$ in each elution slice (SEC–MALS). Equation (9.4) then gives $M$ slice by slice: $M = R_\theta/(Kc)$, with $A_2$ negligible at the low concentrations eluting from the column.

**Example 9.2.2 (Absolute versus Apparent Molar Mass)** Size-exclusion chromatography alone separates molecules by their hydrodynamic size; a molar mass read from a calibration curve of globular standards assumes that the unknown has the same shape and density as the standards. A protein unfolded in denaturant elutes much earlier than the native protein, as if it were several times heavier, and an elongated or glycosylated protein, an **intrinsically disordered protein**, or a membrane protein carrying a detergent micelle are equally misjudged. The ratio of light scattering to concentration signal is the same for the native and the unfolded protein, because $R_\theta/(Kc) = M$ does not depend on shape: static light scattering measures an absolute molar mass. SEC–MALS is therefore the standard way to determine the oligomeric state of a protein in solution, the stoichiometry of a complex and the mass of the protein part of a glycoprotein or a detergent-solubilized membrane protein.

**Remark 9.2.1 (Requirements and Errors)** The sample must not absorb or fluoresce at the laser wavelength; $\mathrm{d}n/\mathrm{d}c$ must be known (an error of $2\,\%$ in it gives $4\,\%$ in $M$ if $c$ is measured by absorbance (since $K \propto (\mathrm{d}n/\mathrm{d}c)^2$), but only $2\,\%$ if $c$ is measured by refractive index (then $c = \Delta n/(\mathrm{d}n/\mathrm{d}c)$ and one factor cancels)); and every particle larger than the molecules of interest must be removed, since the signal grows as $M$. For particles with $R_{\mathrm{g}}$ of a few tens of nanometers, the $P(q)$ correction is necessary even at $90^\circ$: for $R_{\mathrm{g}} = 15\,\mathrm{nm}$ and $\lambda_0 = 500\,\mathrm{nm}$, $P \approx 0.96$, and ignoring it underestimates $M$ by $4\,\%$. With these precautions, molar masses of proteins are determined to within a few percent.

## 9.3. Interference within a Particle

### 9.3.1. The Scattering Amplitude Is a Fourier Transform

X-rays are scattered by electrons. A free electron in the field of an unpolarized beam scatters, per unit solid angle, the intensity given by the Thomson formula,

$$
\frac{\mathrm{d}\sigma}{\mathrm{d}\Omega} = r_{\mathrm{e}}^2\,\frac{1 + \cos^2\theta}{2}, \qquad r_{\mathrm{e}} = \frac{\mathrm{e}^2}{4\pi\varepsilon_0 m_{\mathrm{e}}c^2} = 2.818\times10^{-15}\,\mathrm{m}.
$$
The classical electron radius $r_{\mathrm{e}}$ is the scattering length of one electron, the amplitude of its scattered wave at unit distance. At small angles the polarization factor is $1$, and every electron, wherever it is, scatters with the same amplitude; the only difference between the waves from different electrons is their phase $\boldsymbol{q}\cdot\boldsymbol{r}_j$ (9.1.3).

**Formula 9.3.1 (Scattering Amplitude)** The amplitude scattered by a particle with scattering-length density $\rho(\boldsymbol{r})$ (for X-rays, $r_{\mathrm{e}}$ times the electron density), immersed in a solvent of uniform density $\rho_{\mathrm{s}}$, is

$$
A(\boldsymbol{q}) = \int_{V}\Delta\rho(\boldsymbol{r})\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r}, \qquad \Delta\rho = \rho - \rho_{\mathrm{s}}, \tag{9.8}
$$
and the intensity is $I(\boldsymbol{q}) = \lvert A(\boldsymbol{q})\rvert^2$ (per particle, in units of scattering cross-section per solid angle). For discrete scatterers with scattering lengths $f_j$ at $\boldsymbol{r}_j$, $A(\boldsymbol{q}) = \sum_j f_j\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}_j}$.

The amplitude is the three-dimensional **Fourier transform** of the excess density ([2.5.6](/2.5.6)). This is the far-field (Fraunhofer) condition again: in **Fraunhofer diffraction** the amplitude is the transform of the aperture function ([5.4.2](/5.4.2#sec-2.3.7)), here it is the transform of the particle. Only the contrast $\Delta\rho$ scatters: a uniform medium sends all its secondary waves forward, and a particle with the same density as the solvent is invisible. The detector, however, records $\lvert A\rvert^2$, and the phase of $A(\boldsymbol{q})$ is lost. Two consequences follow at once. Moving the origin by $\boldsymbol{a}$ multiplies $A$ by $\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{a}}$ and leaves $I$ unchanged: the intensity carries no information about where the particle is, only about the distances within it. And since $I(\boldsymbol{q}) = \int\int\Delta\rho(\boldsymbol{r})\Delta\rho(\boldsymbol{r}')\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot(\boldsymbol{r} - \boldsymbol{r}')}$, the intensity is the Fourier transform of the autocorrelation of $\Delta\rho$ (the **convolution theorem**). The loss of phases is the **phase problem** of crystallography (7.6.10); in solution scattering a second loss, that of orientation, is added.

### 9.3.2. Orientational Averaging and the Debye Formula

Molecules in solution tumble. Each orientation contributes its $\lvert A(\boldsymbol{q})\rvert^2$, and the measured intensity is the average over all orientations, which depends only on $q = \lvert\boldsymbol{q}\rvert$: the two-dimensional pattern on the detector is a set of concentric rings, and the information is a one-dimensional curve $I(q)$.

**Theorem 9.3.1 (Debye Scattering Equation)** For a rigid particle of scatterers with scattering lengths $f_j$ at mutual distances $r_{jk} = \lvert\boldsymbol{r}_j - \boldsymbol{r}_k\rvert$, the orientationally averaged intensity is

$$
I(q) = \sum_{j}\sum_{k} f_jf_k\,\frac{\sin(qr_{jk})}{qr_{jk}}, \tag{9.9}
$$
with the term $j = k$ equal to $f_j^2$.

**Proof** By Formula 9.3.1, $I(\boldsymbol{q}) = \sum_j\sum_k f_jf_k\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}_{jk}}$ with $\boldsymbol{r}_{jk} = \boldsymbol{r}_j - \boldsymbol{r}_k$. Averaging over orientations of the particle is the same as averaging $\boldsymbol{q}$ over a sphere of radius $q$ for fixed $\boldsymbol{r}_{jk}$. With $\gamma$ the angle between $\boldsymbol{q}$ and $\boldsymbol{r}_{jk}$,

$$
\left\langle\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\right\rangle = \frac{1}{4\pi}\int_0^{2\pi}\!\!\int_0^{\pi}\mathrm{e}^{-\mathrm{i}qr\cos\gamma}\sin\gamma\,\mathrm{d}\gamma\,\mathrm{d}\varphi = \frac12\int_{-1}^{1}\mathrm{e}^{-\mathrm{i}qru}\,\mathrm{d}u = \frac{\sin qr}{qr}. \qquad \square
$$

Debye derived Eq. (9.9) in 1915 for the scattering of X-rays by gas molecules; it is exact for any rigid particle and is the basis of programs that compute the scattering of atomic models (9.11.1). For the continuous density, the same average turns Formula 9.3.1 into

$$
I(q) = 4\pi\int_0^{\infty}r^2\gamma(r)\,\frac{\sin qr}{qr}\,\mathrm{d}r, \qquad \gamma(r) = \left\langle\int\Delta\rho(\boldsymbol{u})\,\Delta\rho(\boldsymbol{u} + \boldsymbol{r})\,\mathrm{d}^3\boldsymbol{u}\right\rangle_{\Omega}, \tag{9.10}
$$
where $\gamma(r)$ is the orientationally averaged autocorrelation function of the contrast.

### 9.3.3. The Form Factor

**Definition 9.3.1 (Form Factor)** The *form factor* of a particle is its normalized scattering curve $P(q) = I(q)/I(0)$, with $P(0) = 1$. For a particle of uniform contrast $\Delta\rho$ and volume $V$, $I(q) = (\Delta\rho V)^2 P(q)$, and $P(q) = \langle\lvert F(\boldsymbol{q})\rvert^2\rangle_\Omega$ with the amplitude form factor $F(\boldsymbol{q}) = V^{-1}\int_V\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r}$. In the light scattering literature the same function is called the particle scattering factor $P(\theta)$.

The forward intensity $I(0) = (\Delta\rho V)^2$ is the square of the total excess scattering length: particles with more excess electrons scatter more strongly, quadratically in their mass. At $q = 0$ all waves are in phase. As $q$ grows, the waves from the two ends of the particle lose step first, and $P(q)$ falls; the curve encodes shape.

**Example 9.3.1 (Sphere)** For a uniform sphere of radius $R$, $F$ depends only on $q$, and integrating in spherical shells,

$$
F(q) = \frac{3}{R^3}\int_0^R r^2\frac{\sin qr}{qr}\,\mathrm{d}r = \frac{3(\sin qR - qR\cos qR)}{(qR)^3}.
$$
$P(q) = F^2$ has its first zero at $qR = 4.493$ (the first root of $\tan x = x$), then a series of maxima falling as $q^{-4}$. Real proteins are not uniform spheres, but their curves show the same first decay; the side maxima are smeared by the irregular shape and by the spread of sizes.

![Scattering curves I(q)/I(0) of four bodies of uniform density, computed with the Debye formula (Theorem 9.3.1) from points of a cubic lattice filling each body: a solid sphere of radius 50 Å, a hollow sphere (shell from 40 to 50 Å), a rod (cylinder of radius 10 Å and length 200 Å) and a dumbbell (two spheres of radius 25 Å with centres 70 Å apart). The dashed curve is the exact form factor of the solid sphere, which the Debye sum reproduces, including the first minimum at qR = 4.493. Dotted guides: π/(qL), the intermediate region of a long rod, and 9/[2(qR)⁴], the Porod envelope of the sphere (Theorem 9.6.1). Bodies of different shape differ most at qR between 2 and 10](./plots/debye-shapes.py)

The figure shows what the curves can and cannot tell. At small $q$ all curves start alike (9.4); they separate once $q$ exceeds the inverse size. The rod shows an extended region where $I \propto q^{-1}$, characteristic of a one-dimensional object; the hollow sphere decays faster than the solid one of the same outer radius because its mass is farther from the centre; the dumbbell shows a shoulder from the interference between its two lobes.

**Remark 9.3.1 (Polydispersity)** A sample with a distribution $n(R)$ of sizes scatters $I(q) = \int n(R)\,I(q;R)\,\mathrm{d}R$, an incoherent sum. Since $I(0;R) \propto R^6$, the large particles dominate; the minima of the individual curves fall at different $q$ and are smeared out. A sharp first minimum is therefore a sign of a monodisperse sample of compact particles (viruses, ferritin), and its absence is not by itself a sign of irregular shape.

### 9.3.4. The Interparticle Structure Factor

In a concentrated solution the positions of different particles are correlated, and the waves from different particles interfere as well.

**Definition 9.3.2 (Interparticle Structure Factor)** For $N$ identical, spherically symmetric particles in a volume $V$ (number density $n = N/V$) with radial distribution function $g(r)$, the scattered intensity factorizes as $I(q) = nI_1(q)S(q)$, where $I_1$ is the intensity of one particle and

$$
S(q) = 1 + 4\pi n\int_0^{\infty}r^2[g(r) - 1]\,\frac{\sin qr}{qr}\,\mathrm{d}r
$$
is the *interparticle structure factor*. For nonspherical particles the factorization holds approximately.

In a dilute solution $g(r) = 1$ beyond contact and $S = 1$. Repulsion (positive $A_2$) creates a correlation hole around each particle and lowers $S$ at small $q$; attraction raises it. At $q = 0$ the structure factor is fixed by thermodynamics, $S(0) = k_{\mathrm{B}}T(\partial n/\partial\varPi)_T \approx 1/(1 + 2A_2Mc)$, and this is exactly the factor by which Theorem 9.2.1 corrects $R_0$: static light scattering and small-angle scattering at $q \to 0$ measure the same quantity. In SAXS of proteins, interparticle effects are a nuisance to be removed (9.10.1) by measuring a concentration series and extrapolating to $c = 0$, or by adding salt to screen electrostatic repulsion. In crystallography, "structure factor" means something else: the Fourier coefficient $F_{hkl}$ of the electron density of the unit cell, the crystalline analogue of the amplitude $A(\boldsymbol{q})$ of Eq. (9.8) (7.6.10).

## 9.4. The Guinier Region

### 9.4.1. Radius of Gyration

**Definition 9.4.1 (Radius of Gyration)** The *radius of gyration* of a particle with contrast $\Delta\rho(\boldsymbol{r})$ is the root-mean-square distance from its centre of scattering length $\boldsymbol{r}_{\mathrm{c}} = \int\boldsymbol{r}\,\Delta\rho\,\mathrm{d}^3\boldsymbol{r}/\int\Delta\rho\,\mathrm{d}^3\boldsymbol{r}$, weighted by the contrast:

$$
R_{\mathrm{g}}^2 = \frac{\int\lvert\boldsymbol{r} - \boldsymbol{r}_{\mathrm{c}}\rvert^2\,\Delta\rho(\boldsymbol{r})\,\mathrm{d}^3\boldsymbol{r}}{\int\Delta\rho(\boldsymbol{r})\,\mathrm{d}^3\boldsymbol{r}}.
$$
For a particle of uniform density it is a purely geometric quantity, the radius of gyration of mechanics with mass replaced by volume.

**Proposition 9.4.1 (Radius of Gyration from Pair Distances)** For scatterers $f_j$ at $\boldsymbol{r}_j$ with $F = \sum_jf_j$,

$$
R_{\mathrm{g}}^2 = \frac{1}{2F^2}\sum_j\sum_k f_jf_k\,r_{jk}^2.
$$

**Proof** Write $\boldsymbol{r}_j - \boldsymbol{r}_k = (\boldsymbol{r}_j - \boldsymbol{r}_{\mathrm{c}}) - (\boldsymbol{r}_k - \boldsymbol{r}_{\mathrm{c}})$ and expand the square. The two squared terms each give $F\sum_jf_j\lvert\boldsymbol{r}_j - \boldsymbol{r}_{\mathrm{c}}\rvert^2 = F^2R_{\mathrm{g}}^2$; the cross term is $-2\left(\sum_jf_j(\boldsymbol{r}_j - \boldsymbol{r}_{\mathrm{c}})\right)\cdot\left(\sum_kf_k(\boldsymbol{r}_k - \boldsymbol{r}_{\mathrm{c}})\right) = 0$ by the definition of $\boldsymbol{r}_{\mathrm{c}}$. $\square$

| Body (uniform) | $R_{\mathrm{g}}^2$ |
|---|---|
| Solid sphere, radius $R$ | $\frac35R^2$ |
| Thin spherical shell, radius $R$ | $R^2$ |
| Hollow sphere, radii $R_1 < R_2$ | $\frac35\,\dfrac{R_2^5 - R_1^5}{R_2^3 - R_1^3}$ |
| Ellipsoid, semi-axes $a, b, c$ | $\frac15(a^2 + b^2 + c^2)$ |
| Cylinder, radius $R$, length $L$ | $\frac{R^2}{2} + \frac{L^2}{12}$ (thin rod: $L^2/12$; thin disc: $R^2/2$) |
| Gaussian (ideal) chain of $N$ segments of length $b$ | $\frac{Nb^2}{6}$ ([7.6.21](/7.6.21)) |

The radius of gyration is a composite size: a sphere, a hollow shell and a rod can share the same $R_{\mathrm{g}}$. For a compact globular protein of molar mass $M$ and partial specific volume $\bar v \approx 0.74\,\mathrm{cm^3\,g^{-1}}$, treated as a sphere, $R = 0.66\,M^{1/3}$ and $R_{\mathrm{g}} = 0.51\,M^{1/3}$ ($R$ and $R_{\mathrm{g}}$ in ångström, $M$ in dalton), so lysozyme ($14.3\,\mathrm{kDa}$) has $R_{\mathrm{g}} \approx 12.5\,\text{Å}$ by this estimate and $14$–$15\,\text{Å}$ measured (the difference reflects the hydration shell and the departure from a sphere); an unfolded chain of the same length has $R_{\mathrm{g}}$ of about $35\,\text{Å}$ (9.10.3).

### 9.4.2. The Guinier Approximation

**Theorem 9.4.1 (Guinier Approximation)** At small $q$, the scattering curve of any particle is

$$
I(q) = I(0)\left(1 - \frac{q^2R_{\mathrm{g}}^2}{3} + O(q^4)\right) \approx I(0)\,\mathrm{e}^{-q^2R_{\mathrm{g}}^2/3}. \tag{9.11}
$$
A plot of $\ln I$ against $q^2$ (a *Guinier plot*) is therefore linear at small $q$, with slope $-R_{\mathrm{g}}^2/3$ and intercept $\ln I(0)$.

**Proof** Expand the sinc function in Eq. (9.9), $\sin x/x = 1 - x^2/6 + x^4/120 - \cdots$:

$$
I(q) = \sum_j\sum_kf_jf_k - \frac{q^2}{6}\sum_j\sum_kf_jf_kr_{jk}^2 + \frac{q^4}{120}\sum_j\sum_kf_jf_kr_{jk}^4 - \cdots.
$$
The first sum is $F^2 = I(0)$, and by Proposition 9.4.1 the second is $2F^2R_{\mathrm{g}}^2$; hence $I(q) = I(0)(1 - q^2R_{\mathrm{g}}^2/3 + O(q^4))$. The exponential $\mathrm{e}^{-q^2R_{\mathrm{g}}^2/3}$ has the same expansion to order $q^2$. $\square$

The theorem is remarkable for what it does not require: the particle may have any shape and any internal structure, and the orientation need not be known. Guinier (1939), studying X-ray scattering by precipitates in alloys, noticed that the exponential form is accurate well beyond the first two terms; the reason is that the $q^4$ terms of the exponential, $R_{\mathrm{g}}^4/18$, and of the true curve, $\langle r_{jk}^4\rangle/120$, are close for compact bodies.

**Remark 9.4.1 (Range of Validity)** How far the linear region extends depends on shape (panel B of the figure). For a sphere the Guinier approximation is accurate to $2.5\,\%$ up to $qR_{\mathrm{g}} = 1.3$; for elongated or flexible particles the curve bends upward earlier ($7\,\%$ at $qR_{\mathrm{g}} = 1.3$ for a cylinder of axial ratio $7.5$ and for a Gaussian chain), so the fit is limited to $qR_{\mathrm{g}} \le 0.8$–$1.0$. The fit also needs several points at the smallest angles, which requires $q_{\min} \lesssim \pi/D_{\max}$ for a particle of maximum dimension $D_{\max}$.

![The Guinier approximation. A: Guinier plots ln[I(q)/I(0)] against q² for a solid sphere (R = 25 Å, Rg = 19.4 Å) and an elongated cylinder (radius 10 Å, length 150 Å, Rg = 43.9 Å), with the Guinier lines of slope −Rg²/3 (dashed); circles and squares mark qRg = 1.3 and 0.8. The sphere follows its line far beyond qRg = 1.3; the cylinder departs from it early. B: relative error of the Guinier approximation against qRg for the sphere, the cylinder, a thin disc (radius 50 Å, thickness 4 Å) and a Gaussian chain (Debye function); dotted lines at qRg = 0.8 and 1.3](./plots/guinier.py)

**Example 9.4.1 (A Guinier Analysis)** A protein solution gives, for $q$ between $0.010$ and $0.060\,\text{Å}^{-1}$, a straight Guinier plot with slope $-133\,\text{Å}^2$. Then $R_{\mathrm{g}} = \sqrt{3 \times 133} = 20.0\,\text{Å}$, and $q_{\max}R_{\mathrm{g}} = 1.2$, inside the range for a globular particle. If the protein were a uniform sphere, its radius would be $R_{\mathrm{g}}/\sqrt{0.6} = 25.8\,\text{Å}$, its volume $7.2\times10^4\,\text{Å}^3$ and, with $\bar v = 0.74\,\mathrm{cm^3\,g^{-1}}$, its molar mass $59\,\mathrm{kDa}$. Comparing this with the mass from $I(0)$ (9.10.2) or from SEC–MALS tells whether the protein is compact, elongated, or an oligomer.

**Formula 9.4.1 (Guinier Approximations for Rods and Discs)** For a long rod with cross-section radius of gyration $R_{\mathrm{c}}$ (for a solid cylinder $R_{\mathrm{c}}^2 = R^2/2$) and length $L$, in the range $1/L \ll q \ll 1/R_{\mathrm{c}}$,

$$
I(q) \approx I(0)\,\frac{\pi}{qL}\,\mathrm{e}^{-q^2R_{\mathrm{c}}^2/2},
$$
so that $\ln[qI(q)]$ is linear in $q^2$ with slope $-R_{\mathrm{c}}^2/2$; for a flat particle of thickness $T$, $\ln[q^2I(q)]$ is linear in $q^2$ with slope $-T^2/12$.

## 9.5. The Pair-Distance Distribution Function

The intensity is the transform of a function of distance alone (Eq. (9.10)). Inverting the transform gives that function, which is easier to read than $I(q)$.

**Definition 9.5.1 (Pair-Distance Distribution Function)** The *pair-distance distribution function* (PDDF) of a particle is $p(r) = r^2\gamma(r)$, with $\gamma$ the orientationally averaged autocorrelation function of the contrast (Eq. (9.10)). For discrete scatterers, $p(r)\,\mathrm{d}r$ is proportional to the sum of the products $f_jf_k$ over all pairs whose distance lies in $[r, r + \mathrm{d}r]$: for a uniform particle, $p(r)$ is the histogram of all distances between pairs of volume elements.

**Theorem 9.5.1 (PDDF and Scattering Curve)** The scattering curve and the PDDF are related by the sine transforms

$$
I(q) = 4\pi\int_0^{D_{\max}}p(r)\,\frac{\sin qr}{qr}\,\mathrm{d}r, \qquad p(r) = \frac{r}{2\pi^2}\int_0^{\infty}q\,I(q)\sin(qr)\,\mathrm{d}q. \tag{9.12}
$$
Moreover $p(0) = 0$, $p(r) = 0$ for $r \ge D_{\max}$ (the largest dimension of the particle), and

$$
I(0) = 4\pi\int_0^{D_{\max}}p(r)\,\mathrm{d}r, \qquad R_{\mathrm{g}}^2 = \frac{\int_0^{D_{\max}}r^2p(r)\,\mathrm{d}r}{2\int_0^{D_{\max}}p(r)\,\mathrm{d}r}. \tag{9.13}
$$

**Proof** The first relation is Eq. (9.10). The function $\gamma(\boldsymbol{r})$, before orientational averaging, has $I(\boldsymbol{q})$ as its Fourier transform, so the inverse transform is $\gamma(\boldsymbol{r}) = (2\pi)^{-3}\int I(\boldsymbol{q})\,\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{q}$; for isotropic functions, the same angular integral as in Theorem 9.3.1 gives $\gamma(r) = (2\pi^2)^{-1}\int_0^{\infty}q^2I(q)\,\sin(qr)/(qr)\,\mathrm{d}q$, and multiplying by $r^2$ gives the second relation. $\gamma$ is finite at $r = 0$, so $p(0) = 0$, and two points of the particle are never farther apart than $D_{\max}$. Setting $q = 0$ in the first relation gives $I(0)$; expanding the sinc to second order and comparing with Theorem 9.4.1 gives $R_{\mathrm{g}}^2$. $\square$

Equation (9.13) gives a second determination of $R_{\mathrm{g}}$ which uses the whole curve rather than its first few points and is less sensitive to the smallest-angle data, which are the most affected by aggregation or beamstop scatter. In practice $p(r)$ cannot be obtained by applying the second integral of Eq. (9.12) to data that are noisy and known only between $q_{\min}$ and $q_{\max}$: the truncated transform oscillates. It is obtained by the indirect Fourier transform described in 9.10.4.

**Example 9.5.1 (Reading a PDDF)** For a uniform sphere of radius $R$, the distance histogram is $p(r) \propto r^2\left(1 - \frac{3r}{4R} + \frac{r^3}{16R^3}\right)$ for $0 \le r \le 2R$: a symmetric bell with its maximum near $r = R$. Elongated particles have a maximum at small $r$ (about the diameter of the cross-section) and a long, nearly linear tail to $D_{\max}$; hollow particles have their maximum shifted towards $D_{\max}$; a particle made of two well-separated domains has a second maximum at the inter-domain distance. The PDDF thus distinguishes shapes that have the same $R_{\mathrm{g}}$, and changes in it report conformational changes: the opening of a two-domain enzyme on binding a ligand, or the dimerization of a protein in two different arrangements.

![Pair-distance distribution functions p(r), normalized to unit area, of the four bodies of the previous figure, from the histogram of distances between 3000 points placed at random in each. The radius of gyration computed from p(r) with Eq. (9.13) is given in the legend (exact values 38.7, 45.5, 58.2 and 40.0 Å). Dashed: the exact p(r) of the solid sphere. The sphere gives a symmetric bell ending at Dmax = 2R; the hollow sphere is skewed towards Dmax; the rod has a peak at about its diameter and a long linear tail to Dmax ≈ L; the dumbbell has a second peak at the distance between its lobes](./plots/pddf-shapes.py)

## 9.6. The Porod Region and the Invariant

At large $q$ the scattering is dominated by the shortest distances in the particle, those across its surface.

**Theorem 9.6.1 (Porod's Law)** For a particle of uniform contrast $\Delta\rho$ bounded by a smooth, sharp surface of area $S$, the intensity at large $q$ ($qD \gg 1$ for every dimension $D$ of the particle) decays as

$$
I(q) \simeq \frac{2\pi(\Delta\rho)^2S}{q^4}. \tag{9.14}
$$

**Proof** (for a sphere) For $qR \gg 1$, $F(q) = 3(\sin qR - qR\cos qR)/(qR)^3 \approx -3\cos(qR)/(qR)^2$, so $P(q) \approx 9\cos^2(qR)/(qR)^4$. The curve oscillates; averaged over an oscillation, $\langle\cos^2\rangle = 1/2$ and $I(q) = (\Delta\rho V)^2P(q) \approx (\Delta\rho)^2\left(\frac43\pi R^3\right)^2\frac{9}{2q^4R^4} = \frac{8\pi^2R^2(\Delta\rho)^2}{q^4} = \frac{2\pi(\Delta\rho)^2(4\pi R^2)}{q^4}$. For a general body the result follows from the expansion $\gamma(r) = (\Delta\rho)^2V\left(1 - \frac{S}{4V}r + \cdots\right)$ of the autocorrelation at small $r$, whose linear term, inserted in Eq. (9.10), produces the $q^{-4}$ tail. $\square$

**Remark 9.6.1 (Power Laws)** The exponent of the decay reports the dimensionality of the scatterer. In the intermediate range between the inverse length and the inverse thickness, a rod gives $I \propto q^{-1}$ (Formula 9.4.1), a thin disc or bilayer $q^{-2}$, a Gaussian chain $q^{-2}$ and a swollen chain in a good solvent $q^{-5/3}$; a mass fractal of dimension $d_{\mathrm{f}}$ gives $q^{-d_{\mathrm{f}}}$, and a rough surface of fractal dimension $d_{\mathrm{s}}$ gives $q^{-(6 - d_{\mathrm{s}})}$. For a compact protein, the Porod region begins at $q \approx 0.1$–$0.2\,\text{Å}^{-1}$, where the atomic structure, the hydration shell and errors of buffer subtraction start to matter; the law is therefore used qualitatively, often as a Porod–Debye plot of $q^4I(q)$ against $q^4$, which reaches a plateau for compact, well-folded particles and not for flexible ones.

**Definition 9.6.1 (Porod Invariant)** The *Porod invariant* of a scattering curve is

$$
Q = \int_0^{\infty}q^2I(q)\,\mathrm{d}q.
$$
For a particle of uniform contrast, $Q = 2\pi^2(\Delta\rho)^2V$ (from Eq. (9.12) at $r = 0$, since $\gamma(0) = \int(\Delta\rho)^2\,\mathrm{d}^3\boldsymbol{r} = (\Delta\rho)^2V$): it measures the total mean-square contrast and does not depend on the shape.

**Formula 9.6.1 (Porod Volume)** Since $I(0) = (\Delta\rho V)^2$ for a uniform particle, the ratio

$$
V_{\mathrm{P}} = \frac{2\pi^2I(0)}{Q} \tag{9.15}
$$
is the volume of the particle, obtained from the shape of the curve alone: neither the concentration nor the absolute scale of the intensity nor the contrast is needed.

The *Porod volume* of a protein includes the tightly bound hydration and is larger than the dry volume $\bar vM/N_{\mathrm{A}}$; empirically it is about $1.6$–$1.7\,\mathrm{nm^3}$ per kilodalton (9.10.2). In practice $Q$ is computed from the data up to $q \approx 0.2$–$0.3\,\text{Å}^{-1}$ after subtracting a constant that represents the scattering from internal density fluctuations, and the result is accurate to about $10$–$20\,\%$.

**Remark 9.6.2 (Babinet's Principle)** The intensity depends on the contrast only through $(\Delta\rho)^2$. A particle of density $\rho_{\mathrm{s}} + \Delta\rho$ in solvent $\rho_{\mathrm{s}}$ and a hole of the same shape, of density $\rho_{\mathrm{s}} - \Delta\rho$, scatter identically: the sign of the contrast cannot be seen in a single measurement. This is the scattering version of Babinet's principle for complementary screens in optics. Only when the contrast of one component is changed relative to another, as in 9.7, does the sign matter.

## 9.7. Contrast and Contrast Variation

### 9.7.1. X-Ray Contrast

**Definition 9.7.1 (Scattering Length Density)** The *scattering length density* (SLD) of a material is the sum of the scattering lengths $b_i$ of its atoms per unit volume, $\rho = \sum_ib_i/V$. For X-rays, $b_i = Z_ir_{\mathrm{e}}$ at small angles ($Z_i$ the number of electrons), so $\rho_{\mathrm{X}} = r_{\mathrm{e}}\rho_{\mathrm{el}}$ with the electron density $\rho_{\mathrm{el}}$.

| Material | Electron density / $(\mathrm{e}\,\text{Å}^{-3})$ | X-ray SLD / $(10^{10}\,\mathrm{cm^{-2}})$ |
|---|---|---|
| Water | $0.334$ | $9.4$ |
| Protein (average) | $0.42$–$0.44$ | $12$ |
| Nucleic acid | about $0.55$ | about $15.5$ |
| Lipid hydrocarbon chains | about $0.30$ | about $8.5$ |
| $50\,\%$ (by mass) sucrose solution | about $0.40$ | about $11$ |

The contrast of a protein in water is small, $\Delta\rho_{\mathrm{el}} \approx 0.1\,\mathrm{e}\,\text{Å}^{-3}$, and that of a nucleic acid about twice as large; a nucleic acid therefore scatters about four times more strongly per unit volume, and in a protein–RNA complex the curve is weighted towards the RNA. The only way to change X-ray contrast is to change the solvent: adding sucrose or glycerol raises its electron density, and about $65\,\%$ sucrose matches proteins. Such high concentrations change viscosity and may perturb the sample, so X-ray contrast variation is used less than its neutron counterpart, which changes the contrast by isotopic substitution.

### 9.7.2. Neutron Scattering Lengths and H/D Contrast

Neutrons are scattered by nuclei through the strong interaction. The scattering length is a nuclear property that varies irregularly from isotope to isotope and can be negative (a phase shift of $\pi$ relative to the usual sign):

| Nucleus | $^1\mathrm{H}$ | $^2\mathrm{H}$ (D) | $^{12}\mathrm{C}$ | $^{14}\mathrm{N}$ | $^{16}\mathrm{O}$ | $^{31}\mathrm{P}$ |
|---|---|---|---|---|---|---|
| $b$ / fm | $-3.74$ | $6.67$ | $6.65$ | $9.36$ | $5.80$ | $5.13$ |

Hydrogen and deuterium, chemically almost identical, differ in sign. A solvent mixture with a fraction $x$ of D₂O has

**Formula 9.7.1 (SLD of H₂O/D₂O Mixtures)**

$$
\rho_{\mathrm{s}}(x) = (1 - x)\rho_{\ce{H2O}} + x\rho_{\ce{D2O}}, \qquad \rho_{\ce{H2O}} = -0.56, \quad \rho_{\ce{D2O}} = 6.36 \quad (10^{10}\,\mathrm{cm^{-2}}),
$$
spanning a range that contains the SLDs of all biological macromolecules. The SLD of a macromolecule itself rises with $x$, because its exchangeable hydrogens (on $\ce{N}$, $\ce{O}$ and $\ce{S}$) take the isotope of the solvent.

**Definition 9.7.2 (Contrast Variation)** *Contrast variation* is the measurement of small-angle scattering of the same particle at several solvent scattering-length densities, so that components with different SLDs contribute with different weights. The solvent composition at which the SLD of a component equals that of the solvent is its *match point*; at the match point the component is invisible and the measured curve is that of the rest of the particle (in the same positions it occupies in the complex).

Proteins are matched at about $42\,\%$ D₂O and nucleic acids at about $65$–$70\,\%$, lipids at about $10$–$15\,\%$; a perdeuterated protein (grown in D₂O medium) has an SLD above that of D₂O and is never matched. Specific deuteration of one subunit of a complex, or of a lipid nanodisc around a membrane protein, makes that component stand out or disappear. Neutrons bring two further advantages: they deposit little energy, so there is essentially no radiation damage; and hydrogen has a very large incoherent cross-section, which gives a flat background that is reduced by working in D₂O. Their drawback is flux: neutron sources are orders of magnitude weaker than synchrotrons, and SANS needs more sample and more time than SAXS.

![Contrast variation with neutrons. A: neutron scattering-length densities against the D₂O fraction of the solvent: the H₂O/D₂O solvent (black, from −0.56 to 6.36 × 10¹⁰ cm⁻²) and typical values for protein, nucleic acid, perdeuterated protein and phospholipid, whose SLDs rise with x because of exchangeable hydrogens. Circles: match points, at which a component has the SLD of the solvent and becomes invisible (protein about 42 %, nucleic acid about 67 %, lipid about 13 %; the deuterated protein is never matched). B: Stuhrmann plot of a model particle resembling a nucleosome core, a protein sphere (radius 32 Å) inside a concentric DNA shell (46–50 Å). Rg² is linear in the reciprocal mean contrast with positive slope, because the component with higher SLD lies outside; at the protein match point only the DNA is seen (Rg = 48.1 Å), at the DNA match point only the protein (Rg = 24.8 Å); squares: measurements in H₂O and in D₂O](./plots/contrast-variation.py)

### 9.7.3. The Stuhrmann Relation and the Nucleosome

How does the measured radius of gyration change with contrast? Write the SLD of a particle as $\rho(\boldsymbol{r}) = \bar\rho + \rho_{\mathrm{F}}(\boldsymbol{r})$, a mean value plus internal fluctuations with zero mean over the particle volume; the contrast is $\Delta\rho(\boldsymbol{r}) = \Delta\bar\rho + \rho_{\mathrm{F}}(\boldsymbol{r})$, where only the mean contrast $\Delta\bar\rho = \bar\rho - \rho_{\mathrm{s}}$ depends on the solvent.

**Formula 9.7.2 (Stuhrmann Relation)** Inserting this contrast into Definition 9.4.1 gives

$$
R_{\mathrm{g}}^2 = R_{\mathrm{m}}^2 + \frac{\alpha}{\Delta\bar\rho} - \frac{\beta}{\Delta\bar\rho^2}, \qquad \alpha = \frac{1}{V}\int\rho_{\mathrm{F}}(\boldsymbol{r})\,r^2\,\mathrm{d}^3\boldsymbol{r}, \quad \beta = \frac{1}{V^2}\left\lvert\int\rho_{\mathrm{F}}(\boldsymbol{r})\,\boldsymbol{r}\,\mathrm{d}^3\boldsymbol{r}\right\rvert^2,
$$
where $\boldsymbol{r}$ is measured from the centre of the particle's volume and $R_{\mathrm{m}}$ is the radius of gyration of the shape at infinite contrast.

The sign of $\alpha$ tells where the dense component lies: $\alpha > 0$ if the component of higher SLD is at the periphery, $\alpha < 0$ if it is inside. $\beta \ge 0$ measures the separation of the centres of the two components and vanishes when they coincide. A plot of $R_{\mathrm{g}}^2$ against $1/\Delta\bar\rho$ (a Stuhrmann plot) from a few D₂O fractions gives all three parameters.

**Example 9.7.1 (Where Is the DNA in a Nucleosome?)** In the mid-1970s, before any high-resolution structure was available, it was not known whether the DNA of the **nucleosome** ([7.2.4](/7.2.4)) lay inside a protein shell, outside a protein core, or intermixed with it. Neutron scattering of **nucleosome core particles** (Baldwin, Bradbury, Pardon and colleagues) at several H₂O/D₂O ratios answered the question. The Stuhrmann plot had a positive slope, so the component of higher SLD, the DNA, is on the outside. Measured near the protein match point, where only the DNA is seen, the radius of gyration was about $50\,\text{Å}$; near the DNA match point, where only the **histone octamer** is seen, it was about $30\,\text{Å}$. These numbers fit DNA wound in a superhelix of radius about $45\,\text{Å}$ around a protein core, the arrangement confirmed by the crystal structure of the core particle in 1997, with $147\,\mathrm{bp}$ in $1.65$ left-handed turns. The model of panel B of the figure, with a protein sphere inside a DNA shell, reproduces the linear Stuhrmann plot with positive slope ($\beta = 0$, since the two centres coincide).

## 9.8. What a SAXS Curve Can Tell

A curve $I(q)$ is measured, after subtraction of the solvent, from $q_{\min} \approx 0.005$–$0.01\,\text{Å}^{-1}$ to $q_{\max} \approx 0.3$–$0.5\,\text{Å}^{-1}$. Each region views the particle at a different resolution, roughly $d = 2\pi/q$:

| $q$ / $\text{Å}^{-1}$ | $d = 2\pi/q$ | Information |
|---|---|---|
| below $0.01$ | above $60\,\text{nm}$ | aggregates, interparticle interference |
| $0.01$–$0.1$ | $6$–$60\,\text{nm}$ | $I(0)$, $R_{\mathrm{g}}$ (Guinier region), overall shape |
| $0.1$–$0.3$ | $2$–$6\,\text{nm}$ | domain arrangement, compactness, flexibility (Kratky region) |
| $0.3$–$1$ (WAXS) | $0.6$–$2\,\text{nm}$ | internal structure: packing of helices and sheets, fold |
| above $1$ | below $0.6\,\text{nm}$ | secondary structure, solvent shell (wide-angle scattering) |

How much does such a curve determine? By the sampling theorem, a function vanishing outside $[0, D_{\max}]$, such as $p(r)$, is fixed by the values of its transform at intervals $\Delta q = \pi/D_{\max}$.

**Definition 9.8.1 (Shannon Channels)** The number of *Shannon channels* of a scattering curve measured from $q_{\min}$ to $q_{\max}$ for a particle of maximum dimension $D_{\max}$ is

$$
N_{\mathrm{s}} = \frac{D_{\max}(q_{\max} - q_{\min})}{\pi},
$$
the number of independent parameters that the curve can determine, in the absence of noise.

For lysozyme ($D_{\max} \approx 45\,\text{Å}$) measured to $q_{\max} = 0.35\,\text{Å}^{-1}$, $N_{\mathrm{s}} \approx 5$; for a ribosome ($D_{\max} \approx 250\,\text{Å}$), $N_{\mathrm{s}} \approx 25$. Noise reduces the useful number further, typically to $5$–$15$ for proteins. These numbers state the limits of the method: SAXS can decide between a few hypotheses (monomer or dimer, compact or extended, closed or open, which of several predicted arrangements of known domains), but it cannot determine thousands of coordinates on its own. Every three-dimensional model built from SAXS alone relies on additional assumptions that must be stated.

| | SAXS | X-ray crystallography | Solution NMR | Single-particle cryo-EM |
|---|---|---|---|---|
| Sample | solution, $10$–$50\,\mu\mathrm{L}$ at $0.5$–$10\,\mathrm{mg\,mL^{-1}}$ | crystal | solution, isotope-labeled, $0.1$–$1\,\mathrm{mM}$ | vitrified solution, micrograms |
| Size range | from $\sim 5\,\mathrm{kDa}$ to $\mathrm{GDa}$ | no upper limit | up to $\sim 50\,\mathrm{kDa}$ for full structures | best above $\sim 50\,\mathrm{kDa}$ |
| Resolution | $1$–$3\,\mathrm{nm}$ (shape) | $0.1$–$0.3\,\mathrm{nm}$ | atomic (ensemble) | $0.2$–$0.5\,\mathrm{nm}$ |
| Time to a result | hours to days | weeks to years | months | weeks to months |
| Dynamics | ensembles; kinetics from $\mu\mathrm{s}$ | static (time-averaged) | ps–s motions | discrete states |

## 9.9. Instrument and Sample

### 9.9.1. The Beamline

Most biological SAXS is done at synchrotrons, which provide **synchrotron radiation** of high flux in a small, nearly parallel beam. An undulator source, a monochromator (usually a double crystal selecting $\lambda \approx 1\,\text{Å}$, about $12\,\mathrm{keV}$) and a set of slits produce a beam of $10^{12}$–$10^{13}$ photons per second, a fraction of a millimeter wide. The sample flows through a quartz capillary of about $1\,\mathrm{mm}$ diameter; the scattered photons travel through an evacuated flight tube (air scatters) to a photon-counting pixel detector, while the direct beam, many orders of magnitude more intense than the scattering, is stopped by a beamstop that measures the transmitted intensity. Laboratory instruments with copper anodes ($\lambda = 1.54\,\text{Å}$) or liquid-metal-jet sources give data of useful quality on concentrated samples in an hour, and are used for screening.

![Schematic of a solution SAXS experiment (not to scale). An undulator beam is monochromatized and collimated by slits, passes through the sample flowing in a capillary (often directly from a size-exclusion column), and is stopped by a beamstop; the rays scattered through angles θ cross an evacuated flight tube to an area detector, where the scattering of the randomly oriented molecules forms concentric rings. Azimuthal averaging of the rings gives the one-dimensional curve I(q). With λ = 1 Å and a sample–detector distance of 3 m, a beamstop of 5 mm radius and a detector edge 200 mm from the beam set q_min = 0.010 Å⁻¹ and q_max = 0.42 Å⁻¹](./plots/saxs-setup.py)

**Example 9.9.1 (The q Range from the Geometry)** A pixel at distance $\varrho$ from the beam centre on a detector at distance $L$ from the sample records the scattering angle $\theta = \arctan(\varrho/L)$ and hence $q = 4\pi\sin(\theta/2)/\lambda$ (Definition 9.1.2). For $\lambda = 1.0\,\text{Å}$ and $L = 3\,\mathrm{m}$, the edge of a beamstop of radius $5\,\mathrm{mm}$ gives $q_{\min} = 0.010\,\text{Å}^{-1}$ and the detector edge at $200\,\mathrm{mm}$ gives $q_{\max} = 0.42\,\text{Å}^{-1}$. A particle with $D_{\max} = 300\,\text{Å}$ needs $q_{\min} \le \pi/D_{\max} = 0.0105\,\text{Å}^{-1}$ to have its first Shannon channel measured, just met; larger particles need a longer flight tube or a smaller beamstop. Since $q_{\max}/q_{\min} \approx \varrho_{\max}/\varrho_{\min}$, one geometry covers about a factor of $40$ in $q$; WAXS uses a second detector closer to the sample.

### 9.9.2. Absolute Calibration with Water

The radial average of the two-dimensional image is converted to the differential scattering cross-section per unit volume, $\mathrm{d}\Sigma/\mathrm{d}\Omega$ in $\mathrm{cm^{-1}}$, the X-ray counterpart of the Rayleigh ratio (Definition 9.2.1); this "absolute scale" is what makes $I(0)$ a measure of molar mass (9.10.2). The standard is pure water, whose small-angle scattering is flat and is known from thermodynamics.

**Formula 9.9.1 (Forward Scattering of a Liquid)** The forward scattering of a one-component liquid with X-ray scattering-length density $\rho_{\mathrm{X}}$ (Definition 9.7.1) and **isothermal compressibility** $\kappa_T$ is

$$
\frac{\mathrm{d}\Sigma}{\mathrm{d}\Omega}(0) = \rho_{\mathrm{X}}^2\,k_{\mathrm{B}}T\,\kappa_T.
$$
It arises from thermal fluctuations of the number of molecules in volume elements, $\langle\delta N^2\rangle = \langle N\rangle n k_{\mathrm{B}}T\kappa_T$ ($n$ the number density), in exactly the way solute fluctuations give the scattering of a solution (Theorem 9.2.1).

For water at $20\,^\circ\mathrm{C}$, $\rho_{\mathrm{X}} = r_{\mathrm{e}} \times 0.3337\,\mathrm{e}\,\text{Å}^{-3} = 9.40\times10^{10}\,\mathrm{cm^{-2}}$ and $\kappa_T = 4.59\times10^{-10}\,\mathrm{Pa^{-1}}$, so $k_{\mathrm{B}}T\kappa_T = 1.86\times10^{-24}\,\mathrm{cm^3}$ and $\mathrm{d}\Sigma/\mathrm{d}\Omega(0) = 1.64\times10^{-2}\,\mathrm{cm^{-1}}$, in agreement with the measured $1.632\times10^{-2}\,\mathrm{cm^{-1}}$. Recording water and the empty capillary under the conditions of the experiment calibrates the instrument; secondary standards (glassy carbon, or proteins of known molar mass) are also used.

### 9.9.3. The Sample

The analysis of 9.10 assumes a monodisperse solution of identical, non-interacting particles. The sample must approach this ideal:

- Purity and monodispersity: above $95\,\%$ pure, with no aggregates. A $1\,\%$ (by mass) admixture of a 50-mer contributes as much forward scattering as half of the monomers (Formula 9.2.2). Dynamic light scattering ([7.6.8](/7.6.8)) and SEC–MALS (9.2.5) are used beforehand; today most data are collected by SEC–SAXS, with the capillary fed directly from a size-exclusion column so that each frame contains only the species of one elution slice.
- A matched buffer: the solvent must be identical to that of the sample (from dialysis or from the column flow-through), because the protein signal at high $q$ is a fraction of a percent of the solvent scattering (9.9.4).
- A concentration series ($0.5$–$10\,\mathrm{mg\,mL^{-1}}$) to detect concentration-dependent association or interparticle interference (the interparticle structure factor, Definition 9.3.2) and to extrapolate to $c = 0$; salt (about $150\,\mathrm{mM}$) screens electrostatic repulsion.
- An accurate concentration, for the molar mass from $I(0)$ (9.10.2).
- Protection against radiation damage: X-rays ionize water, and the radicals cause aggregation or fragmentation of the sample within seconds of exposure at a synchrotron. The beam is spread over a flowing sample, the exposure is divided into many short frames that are compared before averaging (frames that differ are discarded), and radical scavengers (glycerol at $2$–$5\,\%$, ascorbate, dithiothreitol) are added. The tolerable dose is of the order of kilograys, depending strongly on the sample and buffer.

### 9.9.4. Buffer Subtraction

The measured intensity of the sample is the sum of the solvent scattering, reduced by the volume fraction $\phi$ the solute displaces, and the scattering of the solute:

$$
I(q) = \frac{I_{\mathrm{sample}}(q)}{T_{\mathrm{sample}}} - (1 - \phi)\frac{I_{\mathrm{buffer}}(q)}{T_{\mathrm{buffer}}},
$$
where $T$ are the measured transmissions and both curves are normalized to the incident flux and exposure time ($\phi = \bar vc$ is about $0.001$ per $\mathrm{mg\,mL^{-1}}$ and is often neglected).

The difficulty is one of numbers. Water alone scatters $0.0163\,\mathrm{cm^{-1}}$, and the capillary and parasitic scattering add more; a $14\,\mathrm{kDa}$ protein at $2\,\mathrm{mg\,mL^{-1}}$ scatters $0.02\,\mathrm{cm^{-1}}$ at $q = 0$, but only about $10^{-4}\,\mathrm{cm^{-1}}$ at $q = 0.3\,\text{Å}^{-1}$, a few tenths of a percent of the total. An error of $0.3\,\%$ in the relative scaling of buffer and sample, from a transmission measurement, a drift of the beam or a slightly different buffer, then changes the high-$q$ signal by about its own size (panel B of the figure). Because the Kratky plot (9.10.3) multiplies by $q^2$, under-subtraction produces a rising tail that looks like unfolding and over-subtraction a tail falling below zero. A rising tail in a Kratky plot is therefore first checked against the buffer, and the Porod–Debye plot (Remark 9.6.1) and the stability of the result to small changes of the buffer scale are standard checks.

![Buffer subtraction and first checks (simulated data on the absolute scale). A: sample, buffer and difference for a 14 kDa protein at 2 mg/mL; the buffer (water, capillary and parasitic scattering) dominates at all q, and at q = 0.3 Å⁻¹ the protein is about 0.3 % of the measured intensity. B: Kratky representation q²I(q) of the difference after correct subtraction and after scaling the buffer by 0.997 or 1.003: a 0.3 % error changes the high-q region as much as the signal itself, producing a false rise or a negative tail. C: Guinier plots of the monodisperse protein (linear), with 1 % by mass of large aggregates (upturn at small q) and with repulsive interparticle interference (downturn at small q)](./plots/buffer-subtraction.py)

## 9.10. Primary Analysis

### 9.10.1. Guinier Analysis and the Quality of the Data

The first analysis is a Guinier fit (Theorem 9.4.1) over $q_{\min} \le q \le 1.3/R_{\mathrm{g}}$ (for compact particles; $0.8/R_{\mathrm{g}}$ for elongated ones, Remark 9.4.1). It returns $I(0)$ and $R_{\mathrm{g}}$, and its residuals diagnose the sample (panel C of the figure above):

| Guinier plot at small $q$ | Cause | Remedy |
|---|---|---|
| linear | monodisperse, non-interacting | — |
| upturn | aggregates or attractive interactions ($S(q) > 1$) | SEC–SAXS, centrifugation, change of buffer |
| downturn | repulsive interactions ($S(q) < 1$) | lower concentration, more salt, extrapolation to $c = 0$ |
| $R_{\mathrm{g}}$ and $I(0)/c$ change with concentration | association or interference | concentration series, extrapolation |
| $R_{\mathrm{g}}$ grows from frame to frame | radiation damage | shorter exposure, flow, scavengers |

The radius of gyration is then compared with the value from the PDDF (9.10.4), which uses the whole curve; agreement to a few percent is expected for a good data set.

### 9.10.2. Molar Mass and Volume

The forward intensity on an absolute scale gives the molar mass, just as the Rayleigh ratio does in light scattering (Formula 9.2.1). For $N$ particles per unit volume, each of excess scattering length $\Delta\rho V$, $I(0) = N(\Delta\rho V)^2$; with $N = cN_{\mathrm{A}}/M$ and $V = \bar vM/N_{\mathrm{A}}$,

**Formula 9.10.1 (Molar Mass from the Forward Intensity)**

$$
M = \frac{N_{\mathrm{A}}\,I(0)}{c\,\Delta\rho_M^2}, \qquad \Delta\rho_M = \Delta\rho\,\bar v,
$$
where $\Delta\rho_M$ is the excess scattering length per unit mass. For an average protein, $\Delta\rho_M = 2.09\times10^{10}\,\mathrm{cm\,g^{-1}}$, so that

$$
M/\mathrm{kDa} = 1385\,\frac{I(0)/\mathrm{cm^{-1}}}{c/(\mathrm{mg\,mL^{-1}})}.
$$
Relative to a standard protein measured under the same conditions, $M = M_{\mathrm{st}}\,[I(0)/c]/[I(0)/c]_{\mathrm{st}}$.

For example, the simulated lysozyme of the figure in 9.9.4, $I(0) = 0.0207\,\mathrm{cm^{-1}}$ at $2.0\,\mathrm{mg\,mL^{-1}}$, gives $1385 \times 0.0207/2.0 = 14.3\,\mathrm{kDa}$. The constant applies to proteins of average composition: nucleic acids have a larger $\Delta\rho_M$ (about twice the electron contrast, Definition 9.7.1, and a smaller $\bar v$), glycoproteins and detergent complexes different ones. The main errors are those of the concentration (an error in the extinction coefficient goes directly into $M$), of $\bar v$ (squared), and of residual interparticle interference; the best determinations are accurate to about $10\,\%$, enough to decide the oligomeric state, which is often the main question.

Two methods avoid the concentration altogether. The Porod volume $V_{\mathrm{P}} = 2\pi^2I(0)/Q$ (Formula 9.6.1) of a compact protein, which includes the bound water, is about $1.6\,\mathrm{nm^3}$ per kilodalton (the dry volume is $\bar v/N_{\mathrm{A}} = 1.23\,\mathrm{nm^3}$ per kilodalton). And a second invariant, proposed by Rambo and Tainer (2013), does not even require the particle to be compact:

**Definition 9.10.1 (Volume of Correlation)** The *volume of correlation* of a scattering curve is

$$
V_{\mathrm{c}} = \frac{I(0)}{\int_0^{\infty}q\,I(q)\,\mathrm{d}q},
$$
with the dimension of an area; the ratio $Q_R = V_{\mathrm{c}}^2/R_{\mathrm{g}}$ (dimension of a volume) is proportional to the molar mass, with an empirically calibrated constant ($M \propto Q_R$ for proteins and $M \propto Q_R^{\,k}$ with $k \approx 0.8$ for RNA).

Unlike $Q = \int q^2I\,\mathrm{d}q$, the integral $\int qI\,\mathrm{d}q$ converges for flexible particles (whose tails fall as $q^{-2}$), and both $V_{\mathrm{c}}$ and $Q_R$ are independent of concentration and of the absolute scale.

### 9.10.3. Kratky Plots: Folded or Disordered?

The Porod region distinguishes a compact particle, whose intensity falls as $q^{-4}$, from a flexible chain, whose intensity falls as $q^{-2}$ or more slowly (Remark 9.6.1). Multiplying by $q^2$ magnifies the difference.

**Definition 9.10.2 (Kratky Plot)** The *Kratky plot* (after Otto Kratky, who introduced it for synthetic polymers) displays $q^2I(q)$ against $q$. The *dimensionless Kratky plot* displays $(qR_{\mathrm{g}})^2I(q)/I(0)$ against $qR_{\mathrm{g}}$, which removes the dependence on size and concentration.

**Formula 9.10.2 (Debye Function of a Gaussian Chain)** For a Gaussian (ideal) chain of radius of gyration $R_{\mathrm{g}}$, the orientationally averaged form factor, obtained from the Debye formula with Gaussian distributions of all inter-segment distances, is

$$
\frac{I(q)}{I(0)} = \frac{2\left(\mathrm{e}^{-x} - 1 + x\right)}{x^2}, \qquad x = q^2R_{\mathrm{g}}^2.
$$

**Proposition 9.10.1 (Landmarks of the Dimensionless Kratky Plot)** (a) If $I(q)/I(0) = \mathrm{e}^{-q^2R_{\mathrm{g}}^2/3}$ (the Guinier function), the dimensionless Kratky plot has its maximum at $qR_{\mathrm{g}} = \sqrt3$ with value $3/\mathrm{e} = 1.104$. (b) For a Gaussian chain it rises monotonically to the plateau $2$ as $qR_{\mathrm{g}} \to \infty$.

**Proof** (a) Let $y = x^2\mathrm{e}^{-x^2/3}$ with $x = qR_{\mathrm{g}}$; $y' = 2x\,\mathrm{e}^{-x^2/3}(1 - x^2/3)$ vanishes at $x = \sqrt3$, where $y = 3\mathrm{e}^{-1}$. (b) With $u = x^2$, Formula 9.10.2 gives $(qR_{\mathrm{g}})^2I/I(0) = 2(\mathrm{e}^{-u} - 1 + u)/u = 2 - 2(1 - \mathrm{e}^{-u})/u$, increasing in $u$ and tending to $2$. $\square$

A folded, globular protein therefore gives a bell-shaped Kratky plot with a maximum near $(\sqrt3, 1.1)$ and a return towards zero, whatever its size; a uniform sphere peaks at $qR_{\mathrm{g}} \approx 1.6$ with height $1.03$. Elongation and multiple domains shift the peak to larger $qR_{\mathrm{g}}$ and raise it. An unfolded protein or an **intrinsically disordered protein** gives a plateau, and a real chain, which is locally stiff (its segments are short rods over the **persistence length**, as in the **worm-like chain**), gives a curve that keeps rising at large $q$. A multidomain protein with flexible linkers shows a peak followed by an elevated tail. These patterns are read qualitatively, but they are among the most useful single results of SAXS: whether a protein, a mutant, or a protein under given conditions is folded, partly folded or disordered.

![Kratky plots of model particles, normalized to I(0) = 1. A: q²I(q)/I(0) against q for a folded protein modeled as a sphere and as a prolate ellipsoid (axial ratio 1:1:3), both with Rg = 15 Å, a Gaussian chain (Debye function, Rg = 30 Å) and an unfolded chain of 100 residues (an ensemble of 300 conformations of a freely rotating chain of 3.8 Å bonds, scattering computed with the Debye formula). The folded particles give bells, the Gaussian chain a plateau, the locally stiff chain a continuing rise. B: the same curves in the dimensionless Kratky plot (qRg)²I(q)/I(0) against qRg; dotted lines mark the maximum (√3, 3/e) of the Guinier function and the plateau 2 of the Gaussian chain](./plots/kratky.py)

**Example 9.10.1 (A Riboswitch Folding on Its Ligand)** Kratky plots show the folding of RNA as clearly as that of proteins. The aptamer domain of the adenine-sensing **riboswitch** ([7.2.18](/7.2.18)), a 71-nucleotide three-way junction, gives in the presence of EDTA (which removes divalent ions) a Kratky curve that rises at large $q$, as for an extended, flexible molecule of partially paired helices; with $\ce{Mg^2+}$ and adenine it gives a bell with a pronounced maximum, the signature of a compact tertiary structure in which the two hairpin loops dock onto each other (Wang and colleagues, 2009). Titrations of $\ce{Mg^2+}$ or ligand, followed by $R_{\mathrm{g}}$ and the Kratky plot, give the thermodynamics of compaction.

### 9.10.4. The Indirect Fourier Transform

The PDDF $p(r)$ follows from $I(q)$ by a sine transform (Theorem 9.5.1), but the integral over $q$ from $0$ to $\infty$ cannot be evaluated from data that are noisy, binned and known only between $q_{\min}$ and $q_{\max}$: truncation produces oscillations and a negative tail, and noise is amplified at all $r$. The problem is ill-posed in the sense of Hadamard: many different $p(r)$ fit the data within the errors. Glatter (1977) inverted the direction of the calculation.

**Definition 9.10.3 (Indirect Fourier Transform)** The *indirect Fourier transform* (IFT) determines $p(r)$ not by transforming the data but by fitting them: $p(r)$ is represented by a finite set of parameters on $[0, D_{\max}]$, transformed forward with Eq. (9.12) to a model curve, and the parameters are chosen to fit the measured $I(q)$ under a smoothness constraint.

**Algorithm 9.10.1 (Indirect Fourier Transform with Tikhonov Regularization)**

1. Choose a trial $D_{\max}$ and represent $p$ by its values $p_k = p(r_k)$ on a grid $0 < r_1 < \cdots < r_K < D_{\max}$, with $p(0) = p(D_{\max}) = 0$.
2. Build the transform matrix $T_{ik} = 4\pi\,\Delta r\,\sin(q_ir_k)/(q_ir_k)$, so that the model curve is $T\boldsymbol{p}$ (smearing by the beam profile, if any, is included in $T$).
3. Minimize
   $$
   \Phi(\boldsymbol{p}) = \sum_i\frac{\left[I(q_i) - (T\boldsymbol{p})_i\right]^2}{\sigma_i^2} + \lambda\lVert L\boldsymbol{p}\rVert^2,
   $$
   where $\sigma_i$ are the errors of the data and $L$ is the matrix of second differences, so that the second term penalizes curvature. The minimizer solves the linear equations $(T^{\mathsf T}W^2T + \lambda L^{\mathsf T}L)\boldsymbol{p} = T^{\mathsf T}W^2\boldsymbol{I}$ with $W = \operatorname{diag}(1/\sigma_i)$ (optionally with the constraint $\boldsymbol{p} \ge \boldsymbol{0}$).
4. Choose $\lambda$: the largest value for which the misfit $\chi^2/N$ is still about $1$ (a discrepancy principle), or by criteria such as the L-curve, generalized cross-validation or a Bayesian evidence.
5. Repeat for several $D_{\max}$: a correct $D_{\max}$ lets $p(r)$ approach zero smoothly; one too small forces an abrupt cut, one too large produces a long tail oscillating about zero.
6. Report $I(0)$ and $R_{\mathrm{g}}$ from Eq. (9.13) and compare them with the Guinier values.

The second term is a **regularization** in the sense of Tikhonov: it adds prior knowledge, here that $p(r)$ is smooth and confined to $[0, D_{\max}]$, to select one solution among the many that fit equally well. The figure shows the effect of the weight: with $\lambda$ too small the fit is perfect and $p(r)$ oscillates wildly, with $\lambda$ too large the fit is visibly poor and $p(r)$ oversmoothed, and over a wide intermediate range the data are fitted to within their errors and $p(r)$ reproduces the truth. The program GNOM (Svergun, 1992) implements this scheme with additional "perceptual" criteria for $\lambda$ and $D_{\max}$ and is the most widely used; Bayesian versions (BIFT) choose both automatically and give error bands.

![Indirect Fourier transformation of simulated data for a two-domain protein (two touching spheres of radii 22 and 16 Å, Dmax = 76 Å), with errors from 0.5 % at small q to about 10 % at q_max. A: data and fits with three regularization weights. B: the recovered p(r) against the true distance distribution (grey): for λ = 10² the fit is as good as for λ = 10⁷ but p(r) oscillates; λ = 10¹² oversmooths and misfits the data (χ²/N ≫ 1); the direct transform of the truncated data (dotted) has a spurious negative tail. C: misfit χ²/N and the error of p(r) against λ: the misfit stays near 1 over many decades while the error of p(r) (known only in a simulation) falls; the best λ is near the largest one that does not yet raise χ²](./plots/ift.py)

## 9.11. Modeling

### 9.11.1. Scattering from Atomic Models

Given an atomic model, from a crystal structure, an NMR ensemble or a prediction, the most direct use of SAXS is to compute the curve the model should give and compare it with the data. The Debye formula (Theorem 9.3.1) is exact for atoms in vacuum, but in solution three contributions must be combined: the atoms, the solvent they exclude, and a hydration shell that is denser than bulk water.

**Formula 9.11.1 (Solution Scattering of an Atomic Model)** The scattering of a macromolecule in solution is computed as

$$
I(q) = \left\langle\left\lvert A_{\mathrm{a}}(\boldsymbol{q}) - \rho_{\mathrm{s}}A_{\mathrm{c}}(\boldsymbol{q}) + \delta\rho_{\mathrm{b}}A_{\mathrm{b}}(\boldsymbol{q})\right\rvert^2\right\rangle_{\Omega},
$$
where $A_{\mathrm{a}}$ is the amplitude of the atoms in vacuum (with atomic form factors $f_j(q)$), $A_{\mathrm{c}}$ that of the excluded volume (dummy atoms filling the volume of each atom), $A_{\mathrm{b}}$ that of a hydration shell about $3\,\text{Å}$ thick, and $\delta\rho_{\mathrm{b}}$ the excess density of the shell over bulk solvent.

CRYSOL (Svergun, Barberato and Koch, 1995) expands the three amplitudes in spherical harmonics, which makes the orientational average fast, and fits two parameters, the excluded volume and $\delta\rho_{\mathrm{b}}$ (typically about $10\,\%$ of the water density, $0.03\,\mathrm{e}\,\text{Å}^{-3}$). FoXS uses a Debye sum with implicit hydration; explicit-solvent methods (AXES, WAXSiS) compute the solvent from molecular dynamics and are needed in the wide-angle range. The agreement is measured by

$$
\chi^2 = \frac{1}{N - 1}\sum_{i=1}^{N}\left[\frac{I_{\exp}(q_i) - kI_{\mathrm{model}}(q_i)}{\sigma_i}\right]^2,
$$
with the scale factor $k$ fitted. Such comparisons answer questions that are often decisive: whether a crystal structure (affected by lattice contacts) or a predicted structure represents the molecule in solution, whether the biological assembly is the dimer seen in the crystal or another one, whether missing loops or termini are disordered, and which of several candidate models fits. Their limitation is the limitation of SAXS: different models can give the same curve, and a good $\chi^2$ supports a model without proving it.

### 9.11.2. Ab Initio Shape Reconstruction

Without an atomic model, one may still ask what shape is consistent with the curve. Since the curve has only $N_{\mathrm{s}}$ independent parameters, the shape must be represented with few degrees of freedom or with strong restraints.

**Definition 9.11.1 (Ab Initio Shape Reconstruction)** *Ab initio shape reconstruction* is the determination, from a solution scattering curve alone, of a low-resolution three-dimensional model of the particle, usually a set of beads (dummy atoms) of uniform density or a density map, whose computed scattering fits the data, subject to restraints of compactness and connectivity.

**Algorithm 9.11.1 (Bead Modeling by Simulated Annealing)** (after DAMMIN, Svergun, 1999)

1. Fill a search volume (a sphere of diameter $D_{\max}$) with $N$ densely packed beads of radius $r_0 \ll D_{\max}$, typically $10^3$–$10^4$.
2. A configuration $X$ assigns each bead to the particle or to the solvent (or, for complexes, to one of several phases with different contrasts).
3. Compute the scattering of the particle beads (by spherical harmonics or by the Debye formula, updated incrementally when one bead changes).
4. Define the goal function $f(X) = \chi^2(X) + \alpha P(X)$, where the penalty $P$ favors compact, connected bodies: it grows with the number of beads having few particle neighbors (looseness), with the number of disconnected pieces and, optionally, with deviations from a given symmetry or anisometry.
5. Starting from a random configuration at a high "temperature" $T$, change one randomly chosen bead and accept the change if $f$ decreases or, if it increases by $\Delta f$, with probability $\mathrm{e}^{-\Delta f/T}$ (the Metropolis criterion); after a fixed number of attempts, lower $T$ by a constant factor (for example $0.9$); stop when no further improvement is accepted.
6. Repeat from 10–20 random starts. Superimpose the models, quantify their mutual differences by the normalized spatial discrepancy (NSD), average them and filter the average to the most populated volume.

*Simulated annealing* (Kirkpatrick, Gelatt and Vecchi, 1983) borrows from the physics of cooling: at high $T$ the configuration wanders freely, which lets it escape local minima, and slow cooling lets it settle into a low minimum of $f$. The acceptance rule is that of the **Metropolis algorithm** ([3.5.9](/3.5.9)): at fixed $T$ the configurations are sampled with probability proportional to $\mathrm{e}^{-f/T}$. Related programs use the same principle with other representations: GASBOR a chain of dummy residues with the spacing of $\mathrm{C}_\alpha$ atoms, DAMMIF a faster unconstrained bead model, MONSA several phases fitted simultaneously to SAXS and SANS curves at different contrasts (9.7), and DENSS an electron-density map obtained by iterative phase retrieval.

![A two-dimensional toy version of Algorithm 9.11.1. A flat particle of 59 beads (L-shaped, two lobes; yellow) on a square grid of spacing 5 Å inside a search disc of diameter Dmax = 75 Å; its curve, computed with the Debye formula for a flat particle tumbling in three dimensions, with 2 % noise, serves as the data. Three annealing runs from different random seeds (purple) minimize χ² plus penalties for looseness and disconnection. All three fit the data within the noise (bottom left) and reproduce the size and the two-lobed, bent shape, but differ in detail and in orientation, since rotations and mirror images give the same curve. Bottom right: the goal function during annealing (all attempted steps)](./plots/bead-annealing.py)

The toy model shows the central caution: the curve constrains the shape, not the beads. Mirror images (enantiomorphs) always give the same curve, because $\Delta\rho$ is real and so $\lvert A(-\boldsymbol{q})\rvert = \lvert A(\boldsymbol{q})\rvert$, and the handedness of a SAXS envelope is therefore undetermined; different runs may find genuinely different shapes when the data contain few Shannon channels, and an NSD near $1$ or below among runs, together with an assessment of the ambiguity of the curve (how many different shapes of a reference set it fits), is required before an envelope is interpreted. Envelopes are most valuable for what they exclude, and when a known structure, a domain or a complex, can be docked into them.

### 9.11.3. Rigid-Body and Hybrid Modeling

When high-resolution structures of the parts (domains, subunits, RNA helices) are known and only their arrangement is not, the problem has few unknowns, six per rigid body, and SAXS determines it much better. Rigid-body programs (SASREF, CORAL with missing linkers and loops modeled as chains of dummy residues, BUNCH) search translations and rotations of the parts to fit one or several curves (from deletion mutants, or SAXS and SANS at different contrasts), subject to restraints: the covalent connectivity of linkers, no steric clashes, symmetry, and distances from crosslinking, FRET or mutagenesis. The same strategy, extended to many kinds of data, is integrative structural modeling (7.6.15).

### 9.11.4. Flexible Systems and Ensembles

A flexible protein in solution is not one structure but a distribution, and SAXS measures the average of the curves of all its conformations:

**Formula 9.11.2 (Ensemble Scattering)** For an ensemble of conformations $k$ with population fractions $w_k$ (by mass),

$$
I(q) = \sum_kw_kI_k(q), \qquad \sum_kw_k = 1,
$$
and the Guinier radius of gyration of the mixture is the intensity-weighted mean, $R_{\mathrm{g}}^2 = \sum_kw_kI_k(0)R_{\mathrm{g},k}^2/\sum_kw_kI_k(0)$.

The ensemble optimization method (EOM; Bernadó, Svergun and colleagues, 2007) generates a large pool of conformations, for example with random-coil linkers between folded domains or for a whole disordered protein, and selects, by a genetic algorithm, a subensemble whose averaged curve fits the data; the distribution of $R_{\mathrm{g}}$ (or $D_{\max}$) in the selected ensemble, compared with that of the pool, tells whether the protein is more compact or more extended than a random chain. Maximum-entropy and Bayesian reweighting of molecular dynamics ensembles serve the same purpose with less arbitrariness. The degeneracy is severe: an ensemble average of curves contains even less information than one curve, so ensemble results are best stated as distributions of a few global parameters, and combined with NMR (chemical shifts, paramagnetic relaxation enhancements, residual dipolar couplings) or single-molecule FRET (7.6.12) where possible.

## 9.12. SAXS of RNA

RNA is where SAXS has contributed most to structural biology relative to the other methods. Structured RNAs regulate translation (**riboswitches**, viral elements), catalyze reactions (**ribozymes**, the ribosome) and scaffold complexes, but they are hard to crystallize (they are flexible, negatively charged and conformationally heterogeneous), their phases are difficult to obtain, NMR is limited to roughly $50$–$60$ nucleotides for a complete structure, and single-particle cryo-EM to large RNAs or complexes; RNA-only structures make up only about $1$–$2\,\%$ of the Protein Data Bank. Four features make RNA suitable for SAXS:

- High contrast: the electron density of RNA ($0.55\,\mathrm{e}\,\text{Å}^{-3}$, Definition 9.7.1) gives about four times the signal of a protein of the same volume.
- A predictable building block: secondary structure is predicted well from sequence and probing data, most nucleotides of structured RNAs are in A-form duplexes of known geometry, and the tertiary structure is largely the packing of these helices.
- A switch: folding is driven by $\ce{Mg^2+}$, so the same molecule can be measured unfolded, collapsed and folded (Example 9.10.1).
- Solution conditions: the conformational ensembles that RNA function relies on are seen directly.

Several strategies exploit these features. Three-dimensional prediction programs (MC-Fold/MC-Sym and others) generate thousands of candidate structures, and SAXS selects those that fit the curve. Large RNAs are divided into parts whose envelopes or structures are determined separately and then assembled with restraints (the divide-and-conquer approach, used for the Varkud satellite ribozyme by Lipfert and colleagues, 2008). Most powerfully, SAXS is combined with NMR residual dipolar couplings, which give the orientations of helices relative to a common frame but not their positions, while SAXS gives the global shape: the combination determined the global structure of the 71-nucleotide adenine riboswitch aptamer in solution with a backbone deviation of about $3\,\text{Å}$ from the crystal structure (Wang and colleagues, 2009), and is a general route to RNA structures too large for NMR and too flexible for crystals (7.6.13).

**Example 9.12.1 (Two Viral RNA Elements)** The $102$-nucleotide translational enhancer in the $3'$ untranslated region of turnip crinkle virus RNA, which binds the ribosome, gave a SAXS envelope with the shape of a tRNA, and a model built into it showed a tRNA-like fold: the viral RNA mimics a tRNA to recruit the ribosome (Zuo and colleagues, 2010). The $233$-nucleotide Rev response element (RRE) of HIV-1, to which the viral Rev protein binds as an oligomer to export unspliced viral RNA from the nucleus, gave an envelope with an unusual "A"-shaped topology (Fang and colleagues, 2013): two legs, carrying the known high-affinity Rev-binding sites, are held at a distance comparable to the spacing of the RNA-binding helices in a Rev dimer, which suggested how the RNA's architecture organizes the assembly of Rev on it. In both cases the low-resolution shape, interpreted with known secondary structure, answered a functional question that no other method had answered.

## 9.13. Time-Resolved SAXS

Because a SAXS frame can be collected in milliseconds at a synchrotron, the same quantities, $R_{\mathrm{g}}$, $I(0)$, the Kratky plot and the PDDF, can be followed during a reaction. A reaction is started in one of several ways:

| Trigger | Time resolution | Examples |
|---|---|---|
| stopped-flow mixing | dead time about $1\,\mathrm{ms}$ | $\ce{Mg^2+}$-induced RNA folding, protein folding by denaturant dilution, assembly |
| continuous-flow mixing (turbulent or microfluidic) | $50$–$500\,\mu\mathrm{s}$ | early collapse of proteins and RNA |
| temperature jump (infrared laser) | microseconds | folding and unfolding near the transition |
| laser pump, X-ray probe | about $100\,\mathrm{ps}$ at synchrotrons, femtoseconds at X-ray free-electron lasers | photoactive proteins, ligand photodissociation in myoglobin and hemoglobin |

Continuous-flow experiments (Akiyama and colleagues, 2002, on cytochrome c; Russell and colleagues, 2002, on a ribozyme) showed that chains collapse within a fraction of a millisecond, before their tertiary structure forms. In stopped-flow experiments each frame is short and noisy, so high flux is essential, and the analysis is global: the time series of curves is decomposed by singular value decomposition into a few basis curves, and the amplitudes of the significant components, or the derived $R_{\mathrm{g}}(t)$ and $I(0)(t)$, are fitted by kinetic models.

**Formula 9.13.1 (Multiexponential Relaxation and Model Selection)** For a sequential reaction with first-order steps, an observable relaxes as a sum of exponentials,

$$
R_{\mathrm{g}}(t) = R_{\mathrm{g},\infty} + \sum_{j=1}^{m}A_j\,\mathrm{e}^{-t/\tau_j},
$$
and the number $m$ of phases is chosen by comparing fits with a criterion that penalizes parameters, such as the Bayesian information criterion $\mathrm{BIC} = \chi^2 + k\ln n$ for $k$ parameters and $n$ data points.

**Example 9.13.1 (The Multistage Collapse of a Ribozyme)** Roh, Woodson and colleagues (2010) followed the $\ce{Mg^2+}$-induced folding of the *Azoarcus* **group I intron** ribozyme ([7.2.16](/7.2.16#sec-16.8)), about $200$ nucleotides, by stopped-flow SAXS. The radius of gyration decreased in more than one phase: a fast, nonspecific compaction within milliseconds, as the added cations neutralize the backbone and the helices come together, followed by slower stages in which the native tertiary contacts form, visible as changes of the Kratky curve from a broad to a sharp peak. The figure illustrates the analysis with simulated data: a single exponential cannot describe a two-phase collapse, and the residuals and the information criterion select the two-phase model.

![Fitting a multistage collapse (simulated data with illustrative parameters, not a published data set). A: radius of gyration of a ribozyme of about 200 nt after a stopped-flow jump of Mg²⁺ at t = 0 (dead time 1 ms), from Guinier fits of successive frames (points, ±0.6 Å), with least-squares fits of one exponential and of two exponentials (fast collapse with τ₁ ≈ 4 ms, slower compaction to the native state with τ₂ ≈ 140 ms; true values 4 and 150 ms). B: normalized residuals: the single exponential leaves large systematic deviations, the double exponential leaves random ones, and the Bayesian information criterion falls from about 620 to about 60](./plots/tr-saxs.py)

## 9.14. SAXS in Integrative Structural Biology

SAXS is rarely the only method used on a system, and most of its value now lies in combination:

- With crystallography: deciding which of the assemblies in a crystal is the biological one, detecting conformational differences between crystal and solution, and placing flexible parts missing from the electron density.
- With NMR: residual dipolar couplings and paramagnetic relaxation enhancements give local orientations and distances, SAXS the global shape (9.12).
- With cryo-EM: SAXS reports the flexible regions and the conformational ensemble that classification may average out, and checks that a complex is intact in solution before grids are prepared.
- With prediction and simulation: computed curves test predicted structures of multidomain proteins and complexes (7.6.15), especially the relative positions of domains and the extent of disordered segments, where prediction is least reliable; molecular dynamics ensembles are refined against the data.
- With SANS: contrast variation (9.7) separates the components of protein–nucleic acid and protein–lipid complexes; X-rays and neutrons together constrain multiphase models.

Data and models are deposited in the Small Angle Scattering Biological Data Bank (SASBDB), and community guidelines (Trewhella and colleagues, 2017) specify what a publication must report: the sample and its monodispersity, the concentration series or SEC profile, the Guinier fit with its range and residuals, $I(0)$ and the derived molar mass, the PDDF with $D_{\max}$, the model, its $\chi^2$ and the ambiguity of ab initio reconstructions. With these standards, SAXS gives in a day an answer that is limited in resolution but unusually trustworthy about the molecule in solution.

## Summary

Principles of scattering (9.1–9.7):

- Elastic scattering by particles small compared with the wavelength is dipole scattering: $I_{\mathrm{s}}/I_0 = \pi^2\alpha^2\sin^2\phi/(\varepsilon_0^2\lambda^4r^2)$ (Formula 9.1.1). The scattering vector $\boldsymbol{q} = \boldsymbol{k}_{\mathrm{s}} - \boldsymbol{k}_{\mathrm{i}}$, $q = 4\pi n\sin(\theta/2)/\lambda_0$ (Definition 9.1.2), sets the resolution $2\pi/q$.
- Static light scattering: $R_\theta = KcM$ with $K = 4\pi^2n_0^2(\mathrm{d}n/\mathrm{d}c)^2/(N_{\mathrm{A}}\lambda_0^4)$ (Formula 9.2.1) gives an absolute molar mass, independent of shape (Example 9.2.2). Thermodynamic fluctuation theory gives $Kc/R_0 = 1/M + 2A_2c$ (Theorem 9.2.1); mixtures give $\bar M_{\mathrm{w}}$ (Formula 9.2.2); the Zimm equation and plot give $\bar M_{\mathrm{w}}$, $R_{\mathrm{g}}$ (for $R_{\mathrm{g}} \gtrsim 10\,\mathrm{nm}$) and $A_2$ together (Formula 9.2.3, Definition 9.2.2).
- The scattering amplitude is the Fourier transform of the contrast, $A(\boldsymbol{q}) = \int\Delta\rho\,\mathrm{e}^{-\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}}\,\mathrm{d}^3\boldsymbol{r}$ (Formula 9.3.1); phases and, in solution, orientations are lost, leaving the Debye formula $I(q) = \sum\sum f_jf_k\sin(qr_{jk})/(qr_{jk})$ (Theorem 9.3.1), the form factor (Definition 9.3.1) and, for concentrated solutions, the interparticle structure factor $S(q)$ (Definition 9.3.2).

| Region of the curve | Law | Information |
|---|---|---|
| $q \to 0$ | $I(0) = (\Delta\rho V)^2 \propto cM$ | molar mass, oligomeric state |
| Guinier, $qR_{\mathrm{g}} \lesssim 1.3$ (globular), $\lesssim 0.8$ (elongated) | $I \approx I(0)\,\mathrm{e}^{-q^2R_{\mathrm{g}}^2/3}$ (Theorem 9.4.1) | radius of gyration (Definition 9.4.1) |
| Whole curve | $p(r) = \frac{r}{2\pi^2}\int qI\sin(qr)\,\mathrm{d}q$ (Theorem 9.5.1) | distance distribution, $D_{\max}$, shape class |
| Intermediate | $q^{-1}$ rods, $q^{-2}$ discs and Gaussian chains (Remark 9.6.1) | dimensionality, flexibility |
| Porod, $qD \gg 1$ | $I \simeq 2\pi(\Delta\rho)^2S/q^4$ (Theorem 9.6.1) | surface; with $Q = \int q^2I\,\mathrm{d}q = 2\pi^2(\Delta\rho)^2V$, the volume $V_{\mathrm{P}} = 2\pi^2I(0)/Q$ (Formula 9.6.1) |

- Contrast: X-rays see electron density (protein $0.43$, nucleic acid $0.55$, water $0.334\,\mathrm{e}\,\text{Å}^{-3}$); neutrons see nuclear scattering lengths, with $b_{\mathrm{H}} < 0 < b_{\mathrm{D}}$ (Definition 9.7.1, Formula 9.7.1). Contrast variation in H₂O/D₂O matches proteins at about $42\,\%$ and nucleic acids at about $65$–$70\,\%$ D₂O (Definition 9.7.2), and the Stuhrmann relation (Formula 9.7.2) locates the components: the DNA of the nucleosome lies outside the histone core (Example 9.7.1). The sign of the contrast is invisible in one measurement (Remark 9.6.2).

Biological SAXS in practice (9.8–9.14):

- Information content: a curve from $q_{\min}$ to $q_{\max}$ contains $N_{\mathrm{s}} = D_{\max}(q_{\max} - q_{\min})/\pi$ independent parameters, typically $5$–$25$ (Definition 9.8.1); SAXS decides between hypotheses and determines a few global parameters, and every three-dimensional model needs restraints.
- Measurement: synchrotron or laboratory beamline, $q$ set by the geometry (Example 9.9.1); absolute scale from water, $\mathrm{d}\Sigma/\mathrm{d}\Omega(0) = \rho_{\mathrm{X}}^2k_{\mathrm{B}}T\kappa_T = 1.63\times10^{-2}\,\mathrm{cm^{-1}}$ at $20\,^\circ\mathrm{C}$ (Formula 9.9.1); monodisperse samples (SEC–SAXS), matched buffer, concentration series, control of radiation damage (9.9.3); buffer subtraction at the level of $0.1\,\%$, since the high-$q$ signal is a fraction of a percent of the background (9.9.4).

| Analysis | Result | Reference |
|---|---|---|
| Guinier fit, $qR_{\mathrm{g}} \le 1.3$ | $R_{\mathrm{g}}$, $I(0)$; aggregation and interactions from curvature | 9.10.1 |
| Forward intensity | $M/\mathrm{kDa} = 1385\,I(0)/c$ for proteins, $\pm10\,\%$ | Formula 9.10.1 |
| Porod volume, volume of correlation | $V_{\mathrm{P}} \approx 1.6\,\mathrm{nm^3\,kDa^{-1}}$; $Q_R = V_{\mathrm{c}}^2/R_{\mathrm{g}} \propto M$ without concentration | 9.10.2, Definition 9.10.1 |
| Kratky plot | folded (bell, maximum near $(\sqrt3, 1.1)$) or disordered (plateau $2$, rise) | Definition 9.10.2, Proposition 9.10.1 |
| Indirect Fourier transform | $p(r)$, $D_{\max}$, $R_{\mathrm{g}}$ by regularized fitting | Algorithm 9.10.1 |
| Atomic models | $\chi^2$ test of crystal, NMR or predicted structures, with hydration shell | Formula 9.11.1 |
| Ab initio | bead models by simulated annealing, averaged, ambiguity assessed; handedness undetermined | Algorithm 9.11.1 |
| Rigid body, ensembles | arrangement of known parts; distributions of $R_{\mathrm{g}}$ for flexible systems | 9.11.3, Formula 9.11.2 |

- RNA: high contrast, A-form building blocks and $\ce{Mg^2+}$-dependent folding make SAXS, alone or with NMR residual dipolar couplings, a main route to global RNA structure (9.12, Example 9.12.1).
- Kinetics: stopped-flow, continuous-flow, temperature-jump and pump–probe SAXS follow folding and conformational change from picoseconds to seconds; multiexponential fits with model selection (Formula 9.13.1) reveal multistage collapse (Example 9.13.1).

## Questions

1. SEC–MALS of a protein preparation (laser $658\,\mathrm{nm}$, $\mathrm{d}n/\mathrm{d}c = 0.185\,\mathrm{mL\,g^{-1}}$, $n_0 = 1.330$) gives, at the top of the main peak, $c = 1.0\,\mathrm{mg\,mL^{-1}}$ and $R_\theta = 2.8\times10^{-5}\,\mathrm{cm^{-1}}$. The sequence predicts $66\,\mathrm{kDa}$. What is the oligomeric state? Why does the result not depend on where the peak elutes?

   **Answer** With $K = 2.12\times10^{-7}\,\mathrm{mol\,cm^2\,g^{-2}}$ (Example 9.2.1), $M = R_\theta/(Kc) = 2.8\times10^{-5}/(2.12\times10^{-7}\times10^{-3}) = 1.32\times10^{5}\,\mathrm{g\,mol^{-1}}$, a dimer. At this low concentration $2A_2c$ is negligible compared with $1/M$ (for $A_2 \sim 10^{-4}\,\mathrm{mol\,mL\,g^{-2}}$, $2A_2c = 2\times10^{-7}$ against $1/M = 7.6\times10^{-6}$, a $3\,\%$ correction), and for a $132\,\mathrm{kDa}$ protein $P(q) = 1$ to better than $0.1\,\%$. The elution volume depends on hydrodynamic size, hence on shape; $R_\theta/(Kc)$ depends only on mass (Formula 9.2.1), so an elongated dimer would be assigned the same mass.

2. Explain, with numbers, why multi-angle light scattering at $658\,\mathrm{nm}$ gives the molar mass but not the radius of gyration of lysozyme ($R_{\mathrm{g}} = 1.4\,\mathrm{nm}$), whereas SAXS gives both. What range of $q$ does a Guinier analysis of lysozyme need?

   **Answer** The largest $q$ of light in water is about $4\pi\times1.33\times\sin 80^\circ/658\,\mathrm{nm} = 0.025\,\mathrm{nm^{-1}}$, where $q^2R_{\mathrm{g}}^2/3 = 4\times10^{-4}$: the angular variation is $0.04\,\%$, far below the precision of the measurement. Visible light sees lysozyme as a point. The Guinier region requires $qR_{\mathrm{g}}$ up to about $1$, i.e. $q \approx 0.7\,\mathrm{nm^{-1}} = 0.07\,\text{Å}^{-1}$, which with $\lambda = 0.1\,\mathrm{nm}$ X-rays corresponds to $\theta = 2\arcsin(q\lambda/4\pi) \approx 0.6^\circ$; several data points below this, from $q_{\min} \approx 0.01\,\text{Å}^{-1}$, are needed.

3. Two identical atoms (scattering length $f$) are held at a distance $d$. Using the Debye formula, find the orientationally averaged intensity, its value at $q = 0$ and as $q \to \infty$, and the position of its first minimum. For $d = 50\,\text{Å}$, where is that minimum?

   **Answer** Equation (9.9) with two scatterers: $I(q) = 2f^2[1 + \sin(qd)/(qd)]$. At $q = 0$, $I = 4f^2$ (coherent: amplitudes add); for $q \to \infty$, $I \to 2f^2$ (incoherent: intensities add). The minima of $\sin x/x$ satisfy $\tan x = x$, the first at $x = 4.493$, where $\sin x/x = -0.217$, so $I_{\min} = 1.57f^2$. For $d = 50\,\text{Å}$, $q = 4.493/50 = 0.090\,\text{Å}^{-1}$. The same reasoning explains the shoulder of the dumbbell in the figure of 9.3.3.

4. A Guinier plot has slope $-133\,\text{Å}^2$ up to $q = 0.060\,\text{Å}^{-1}$. A second sample, measured over the same range, gives a plot that curves upward at the smallest $q$, and a third one that curves downward. Interpret all three.

   **Answer** First sample: $R_{\mathrm{g}} = 20.0\,\text{Å}$, $q_{\max}R_{\mathrm{g}} = 1.2$, a valid analysis (Example 9.4.1). Upward curvature at small $q$ means excess intensity at the largest distances, the signature of a small fraction of aggregates (which contribute $\propto cM$ and have large $R_{\mathrm{g}}$) or of attractive interparticle interactions, $S(q) > 1$ at small $q$. Downward curvature means a deficit at small $q$: repulsive interactions, $S(q) < 1$ (Definition 9.3.2). Both are removed by measuring a concentration series and extrapolating to $c = 0$, and aggregates also by size-exclusion chromatography in line with the measurement.

5. Show that the Porod invariant of a uniform particle does not depend on its shape, and use Formula 9.6.1: a protein gives $I(0) = 0.020\,\mathrm{cm^{-1}}$ and $Q = 4.0\times10^{-6}\,\mathrm{cm^{-1}\,\text{Å}^{-3}}$. What is its Porod volume, and why is neither the concentration nor the absolute calibration needed?

   **Answer** By Eq. (9.12), $p(r) = r^2\gamma(r)$ and $\gamma(0) = (2\pi^2)^{-1}\int q^2I\,\mathrm{d}q$, so $Q = 2\pi^2\gamma(0)$; and $\gamma(0) = \int(\Delta\rho)^2\,\mathrm{d}^3\boldsymbol{r} = (\Delta\rho)^2V$, the integral of the square of the contrast, which does not depend on how the volume is shaped. Then $V_{\mathrm{P}} = 2\pi^2I(0)/Q = 2\times9.87\times0.020/(4.0\times10^{-6}) = 9.9\times10^4\,\text{Å}^3 = 99\,\mathrm{nm^3}$. Both $I(0)$ and $Q$ are proportional to the number of particles, to the absolute scale and to $(\Delta\rho)^2$; these factors cancel in the ratio.

6. Why are SANS experiments on proteins often done in D₂O rather than H₂O? Compare the contrast of a protein (SLD $1.8$ in H₂O, $3.1$ in D₂O, in $10^{10}\,\mathrm{cm^{-2}}$) in the two solvents, and name a second, independent reason.

   **Answer** In H₂O the contrast is $1.8 - (-0.56) = 2.36$; in D₂O it is $3.1 - 6.36 = -3.26$. The intensity is proportional to $(\Delta\rho)^2$ (the sign is invisible, Remark 9.6.2), so D₂O gives $(3.26/2.36)^2 = 1.9$ times more coherent signal. Independently, $^1\mathrm{H}$ has an incoherent scattering cross-section of about $80\,\mathrm{b}$, against about $2\,\mathrm{b}$ for D, so an H₂O sample produces a large flat background (and attenuates the beam); D₂O reduces it by an order of magnitude and improves the signal-to-noise ratio at high $q$.

7. (Experimental design) You want to determine the arrangement of a protein (40 kDa) and an RNA (30 kDa) in a 1:1 complex by SANS. Which solvent compositions would you use, what would you expect to see at each, and how could deuteration of the protein improve the experiment?

   **Answer** Measure at about $42\,\%$ D₂O (protein matched: the curve is that of the RNA as it sits in the complex), at about $65$–$70\,\%$ (RNA matched: the protein alone), and at two or three further compositions including $0$ and $100\,\%$ to construct a Stuhrmann plot. The radii of gyration of the components, compared with those of the free molecules, show whether either changes conformation on binding; the sign of $\alpha$ tells which component is on the outside, and $\beta$, the separation of their centres; with the curves of both components one can model their shapes and relative positions jointly. Perdeuterating the protein (grown in D₂O medium) raises its SLD above that of D₂O; then in $100\,\%$ D₂O the RNA is nearly matched against the solvent while the protein is strongly visible, and in about $70\,\%$ D₂O the contrast between the two components is maximal, which separates them more cleanly than natural-abundance contrast variation.

8. A Zimm analysis of a large assembly gives an intercept $5.0\times10^{-7}\,\mathrm{mol\,g^{-1}}$, a slope of the $c = 0$ line of $2.67\times10^{-4}\,\mathrm{mol\,g^{-1}\,nm^2}$ against $q^2$, and a slope of the $\theta = 0$ line of $4.0\times10^{-4}\,\mathrm{mol\,mL\,g^{-2}}$ against $c$. Find $\bar M_{\mathrm{w}}$, $R_{\mathrm{g}}$ and $A_2$. If the assembly were a uniform sphere of density $1.35\,\mathrm{g\,cm^{-3}}$, what $R_{\mathrm{g}}$ would you expect, and what do you conclude?

   **Answer** $\bar M_{\mathrm{w}} = 1/(5.0\times10^{-7}) = 2.0\times10^6\,\mathrm{g\,mol^{-1}}$; $R_{\mathrm{g}}^2 = 3\bar M_{\mathrm{w}}\times\text{slope} = 3\times2.0\times10^6\times2.67\times10^{-4} = 1.60\times10^3\,\mathrm{nm^2}$, $R_{\mathrm{g}} = 40\,\mathrm{nm}$; $A_2 = 4.0\times10^{-4}/2 = 2.0\times10^{-4}\,\mathrm{mol\,mL\,g^{-2}}$ (repulsive). A compact sphere of this mass has volume $2.0\times10^6/(6.02\times10^{23}\times1.35)\,\mathrm{cm^3} = 2.46\times10^{-18}\,\mathrm{cm^3} = 2.46\times10^{3}\,\mathrm{nm^3}$, radius $8.4\,\mathrm{nm}$ and $R_{\mathrm{g}} = 6.5\,\mathrm{nm}$. The measured $40\,\mathrm{nm}$ is six times larger: the assembly is highly extended (a long filament, a branched or a loosely packed structure), not a compact globule.

9. A protein forms a dimer. Compare the change of $I(0)$ (at the same mass concentration) with the change of $R_{\mathrm{g}}$ if (a) two spheres of radius $R$ touch, (b) the dimer is a sphere of twice the volume. Which quantity is the more sensitive indicator of oligomerization?

   **Answer** $I(0) \propto cM$ doubles in both cases. (a) Two touching spheres with centres $2R$ apart: by the parallel-axis theorem $R_{\mathrm{g}}^2 = \frac35R^2 + R^2 = 1.6R^2$, so $R_{\mathrm{g}}$ grows by $\sqrt{1.6/0.6} = 1.63$. (b) A sphere of twice the volume has radius $2^{1/3}R$, so $R_{\mathrm{g}}$ grows only by $1.26$. The geometric size of an assembly grows more slowly than its mass, and in a partial dimerization the z-averaged $R_{\mathrm{g}}$ changes even less; $I(0)$ (on an absolute scale and with known concentration) is the more direct indicator of the oligomeric state, $R_{\mathrm{g}}$ and $p(r)$ then tell how the subunits are arranged.

10. Why can small-angle scattering of a solution, unlike crystallography, never give an atomic structure on its own? List what is lost between the electron density $\rho(\boldsymbol{r})$ and the measured curve $I(q)$, and estimate how many independent numbers a curve measured to $q_{\max} = 0.3\,\text{Å}^{-1}$ contains for a particle with $D_{\max} = 100\,\text{Å}$.

    **Answer** Three things are lost: the phases of $A(\boldsymbol{q})$ (only $\lvert A\rvert^2$ is measured, Formula 9.3.1); the orientations, since the tumbling average reduces the three-dimensional $\lvert A(\boldsymbol{q})\rvert^2$ to a one-dimensional function of $q$ (Theorem 9.3.1); and the high-resolution information, since $q_{\max}$ is small and the signal falls as $q^{-4}$. A crystal keeps the orientations and amplifies the signal at discrete reciprocal-lattice points to atomic resolution, so only the phases must be recovered (7.6.10). By the sampling theorem a function confined to $[0, D_{\max}]$ is determined by its transform at intervals $\pi/D_{\max}$ in $q$, so the curve contains about $N_{\mathrm{s}} = D_{\max}q_{\max}/\pi = 100\times0.3/\pi \approx 10$ independent parameters (the number of Shannon channels, Definition 9.8.1). Ten numbers can fix size, shape and the arrangement of a few domains, not thousands of atomic coordinates.

11. A beamline uses $\lambda = 1.0\,\text{Å}$, a sample–detector distance of $2\,\mathrm{m}$, a beamstop of radius $4\,\mathrm{mm}$ and a detector extending $150\,\mathrm{mm}$ from the beam. What $q$ range does it cover? Is it suitable for a particle with $D_{\max} = 300\,\text{Å}$, and what would you change?

    **Answer** $q_{\min} = 4\pi\sin[\tfrac12\arctan(4/2000)]/1.0 = 0.0126\,\text{Å}^{-1}$ and $q_{\max} = 4\pi\sin[\tfrac12\arctan(150/2000)] = 0.47\,\text{Å}^{-1}$. For $D_{\max} = 300\,\text{Å}$ the first Shannon channel lies at $\pi/D_{\max} = 0.0105\,\text{Å}^{-1}$, below $q_{\min}$; the Guinier region ($qR_{\mathrm{g}} \le 1.3$, with $R_{\mathrm{g}}$ of perhaps $100\,\text{Å}$, so $q \le 0.013\,\text{Å}^{-1}$) is barely touched. Increase $L$ (at $4\,\mathrm{m}$, $q_{\min}$ halves to $0.0063\,\text{Å}^{-1}$, at the cost of $q_{\max}$), use a smaller beamstop, or a longer wavelength.

12. SEC–SAXS of a protein whose sequence gives $18.5\,\mathrm{kDa}$ yields, at the peak, $I(0) = 0.0405\,\mathrm{cm^{-1}}$ at $c = 1.5\,\mathrm{mg\,mL^{-1}}$ (measured by UV absorbance in line). What is the oligomeric state? List three sources of error in this number and their sizes.

    **Answer** $M = 1385 \times 0.0405/1.5 = 37.4\,\mathrm{kDa}$, a dimer. Errors: the concentration, through the extinction coefficient computed from the sequence (a few percent, more if the protein has few aromatic residues) and through dilution on the column; $\Delta\rho_M$, which assumes average protein composition and $\bar v = 0.74\,\mathrm{cm^3\,g^{-1}}$ (enters squared; a glycoprotein or bound ligand changes it); and residual interparticle interference or aggregation, reduced by the low concentration in SEC. Together about $10\,\%$, small compared with the factor of $2$ between monomer and dimer; the Porod volume and $Q_R$ (Definition 9.10.1) give independent, concentration-free checks.

13. Using Formula 9.9.1, estimate the forward scattering of water at $4\,^\circ\mathrm{C}$ ($\kappa_T = 4.95\times10^{-10}\,\mathrm{Pa^{-1}}$, density $1.000\,\mathrm{g\,mL^{-1}}$) and at $20\,^\circ\mathrm{C}$ ($\kappa_T = 4.59\times10^{-10}\,\mathrm{Pa^{-1}}$, $0.998\,\mathrm{g\,mL^{-1}}$). Why must the calibration be made at the temperature of the experiment, and why does water scatter at all if it is a homogeneous liquid?

    **Answer** Water has $10$ electrons per $18.015\,\mathrm{g\,mol^{-1}}$: at $20\,^\circ\mathrm{C}$ the electron density is $0.3337\,\mathrm{e}\,\text{Å}^{-3}$, $\rho_{\mathrm{X}} = 9.40\times10^{10}\,\mathrm{cm^{-2}}$, $k_{\mathrm{B}}T\kappa_T = 1.381\times10^{-23} \times 293.15 \times 4.59\times10^{-10}\,\mathrm{m^3} = 1.86\times10^{-24}\,\mathrm{cm^3}$, and $I(0) = 1.64\times10^{-2}\,\mathrm{cm^{-1}}$. At $4\,^\circ\mathrm{C}$: $0.3343\,\mathrm{e}\,\text{Å}^{-3}$, $k_{\mathrm{B}}T\kappa_T = 1.89\times10^{-24}\,\mathrm{cm^3}$, $I(0) = 1.68\times10^{-2}\,\mathrm{cm^{-1}}$, $2\,\%$ higher (water's compressibility has a minimum near $46\,^\circ\mathrm{C}$). A $2\,\%$ calibration error is a $2\,\%$ error in every molar mass. Water scatters because it is homogeneous only on average: thermal motion creates fluctuations of the number of molecules in each small volume, whose mean square is set by the compressibility; an incompressible liquid would not scatter at $q = 0$.

14. Three proteins give the following Kratky plots: (a) a bell with a maximum at $q = 0.11\,\text{Å}^{-1}$ that returns nearly to zero by $0.3\,\text{Å}^{-1}$; (b) a curve that rises to a plateau and keeps rising slowly; (c) a bell followed by a tail that stays at about half of the peak height. Interpret each, state what you would check before believing (b) and (c), and estimate $R_{\mathrm{g}}$ for (a) if it is globular.

    **Answer** (a) A compact, folded protein; for a globular particle the dimensionless maximum lies near $qR_{\mathrm{g}} = \sqrt3$ (Proposition 9.10.1), so $R_{\mathrm{g}} \approx 1.73/0.11 = 16\,\text{Å}$ (a uniform sphere would peak at $1.6/R_{\mathrm{g}}$, giving $15\,\text{Å}$). (b) A disordered or unfolded chain: the plateau corresponds to Gaussian-chain statistics at intermediate $q$, the continued rise to local stiffness of the chain (rod-like segments over the persistence length). (c) A folded core with disordered tails or flexible linkers between domains. Before believing (b) or (c), check the buffer subtraction (a $0.3\,\%$ under-subtraction creates such a tail, figure in 9.9.4), compare with a Porod–Debye plot, and confirm by an independent method (NMR chemical shifts, circular dichroism, or the ratio of $R_{\mathrm{g}}$ to the value expected for a compact protein of the measured mass).

15. Show that a Gaussian chain never produces a maximum in the dimensionless Kratky plot, and compute $(qR_{\mathrm{g}})^2I/I(0)$ for it at $qR_{\mathrm{g}} = 1$, $\sqrt3$ and $3$. Compare with the Guinier function at the same points.

    **Answer** With $u = (qR_{\mathrm{g}})^2$, Formula 9.10.2 gives $y = 2 - 2(1 - \mathrm{e}^{-u})/u$, whose derivative $2[1 - (1 + u)\mathrm{e}^{-u}]/u^2$ is positive for $u > 0$ (since $\mathrm{e}^u > 1 + u$): $y$ increases monotonically to $2$, without a maximum. Values: $u = 1$: $2 - 2 \times 0.632 = 0.736$; $u = 3$: $2 - 2 \times 0.950/3 = 1.367$; $u = 9$: $2 - 2 \times 1.000/9 = 1.778$. The Guinier function $u\,\mathrm{e}^{-u/3}$ gives $0.717$, $1.104$ (its maximum) and $0.448$: the two agree at small $qR_{\mathrm{g}}$ (both start as $u - u^2/3$) and differ by a factor of four at $qR_{\mathrm{g}} = 3$, which is why the Kratky region, not the Guinier region, distinguishes folded from disordered.

16. Why can $p(r)$ not be obtained simply by numerical integration of the data with Eq. (9.12)? Explain in terms of information what the regularization term of Algorithm 9.10.1 adds, and how an incorrect $D_{\max}$ shows itself.

    **Answer** The data are known only on $[q_{\min}, q_{\max}]$; the missing small-$q$ part carries the largest distances and the missing large-$q$ part the fine structure, and cutting the integral multiplies the true transform by a window whose sine transform oscillates, so the result has ripples and a negative tail; noise at large $q$, multiplied by $q$, is amplified at all $r$. Mathematically the inversion is ill-posed: with about $N_{\mathrm{s}}$ independent parameters in the data, a $p(r)$ on many grid points is underdetermined, and infinitely many solutions fit within the errors (panel C of the figure, where $\chi^2$ is flat over ten decades of $\lambda$). The regularization adds prior information, that $p(r)$ is smooth, vanishes at $0$ and beyond $D_{\max}$, and (optionally) is non-negative, which selects the smoothest of the acceptable solutions. Too small a $D_{\max}$ forces $p(r)$ to drop abruptly to zero with a poor fit at small $q$; too large a $D_{\max}$ leaves a tail oscillating about zero or a long, nearly flat extension.

17. In ab initio bead modeling, why are ten or more independent runs made, and why can no SAXS envelope tell a left-handed from a right-handed particle? What would you do to decide the handedness of a complex?

    **Answer** Each run converges to one of many configurations that fit the data within the noise (the toy figure in 9.11.2 shows three different solutions); comparing many runs measures the reproducibility of the features (NSD), and averaging retains only what is common. The handedness is undetermined because the scattering-length density is real, so $A(-\boldsymbol{q}) = A(\boldsymbol{q})^*$ and $\lvert A\rvert^2$ is centrosymmetric; the mirror image of a particle has the intensity $\lvert A(-\boldsymbol{q})\rvert^2$, which equals $\lvert A(\boldsymbol{q})\rvert^2$, and after orientational averaging the two curves are identical. The handedness must come from other information: docking subunits of known (chiral) atomic structure into the envelope, distance restraints from crosslinking or FRET between identified sites, or an electron microscopy map.

18. A disordered protein is thought to be an equal-mass mixture of a compact state ($R_{\mathrm{g}} = 25\,\text{Å}$) and an extended state ($R_{\mathrm{g}} = 45\,\text{Å}$). What radius of gyration does a Guinier fit give? Why does the result differ from the mean of the two radii, and what other data would distinguish this two-state mixture from a single broad ensemble with the same average?

    **Answer** Both states have the same mass and contrast, so $I_k(0)$ are equal and by Formula 9.11.2 $R_{\mathrm{g}}^2 = (25^2 + 45^2)/2 = 1325\,\text{Å}^2$, $R_{\mathrm{g}} = 36.4\,\text{Å}$, larger than the mean $35\,\text{Å}$ because the Guinier fit averages $R_{\mathrm{g}}^2$, not $R_{\mathrm{g}}$ (and weights by $I(0) \propto M$ when masses differ). The shape of the curve beyond the Guinier region differs between a bimodal and a unimodal ensemble only slightly; better discrimination comes from varying conditions (temperature, denaturant, ligand) to shift the populations with an isosbestic-like behaviour in the curves, from SEC–SAXS if the states separate, and from single-molecule FRET (7.6.12), which shows the distribution of distances molecule by molecule.

19. In a stopped-flow SAXS experiment the radius of gyration of an RNA falls from $67\,\text{Å}$ at $1\,\mathrm{ms}$ to $42\,\text{Å}$ at $5\,\mathrm{s}$. A single exponential gives $\mathrm{BIC} = 619$ (3 parameters) and two exponentials $\mathrm{BIC} = 61$ (5 parameters) for $45$ points. Which model is preferred and why? What does the existence of a fast phase complete within a few milliseconds suggest physically, and which additional observable would test whether the intermediate is compact but non-native?

    **Answer** The two-exponential model: its BIC is lower by about $560$, far more than the penalty $2\ln 45 = 7.6$ for its two extra parameters; the single exponential leaves systematic residuals (figure in 9.13). The fast phase, faster than the formation of specific tertiary contacts, is a nonspecific collapse driven by the neutralization of the phosphate charges by $\ce{Mg^2+}$ (counterion-induced compaction), followed by the slower search for the native structure. The Kratky plot of the intermediate (compact but less peaked, or with a residual tail) and its PDDF, compared with those of the native state, test whether it is compact but non-native; so do chemical or hydroxyl-radical footprinting at the same times, which report the formation of specific contacts.

20. (Experimental design) A two-domain enzyme is proposed to close around its substrate. Design a SAXS experiment to test the proposal and to estimate the fraction of closed molecules at a given substrate concentration, using a crystal structure of the open form and a predicted model of the closed form. What controls are essential?

    **Answer** Purify the enzyme to monodispersity and measure by SEC–SAXS (or a concentration series with extrapolation) without substrate and with saturating substrate or a non-hydrolyzable analogue, then at several intermediate concentrations. Compare $R_{\mathrm{g}}$, $D_{\max}$ and $p(r)$: closure should reduce both and sharpen the PDDF. Compute the curves of the open and closed models with Formula 9.11.1 and fit each data set by $I = w\,I_{\mathrm{closed}} + (1 - w)I_{\mathrm{open}}$ (Formula 9.11.2) to obtain the closed fraction $w$ as a function of substrate concentration, which can be fitted by a binding model. Controls: identical buffers for sample and blank, including the substrate (which scatters and changes the solvent density); confirmation that $I(0)/c$ does not change (no ligand-induced oligomerization); checks for radiation damage frame by frame; and a test of whether the two-state model is sufficient (residuals, or a model with a third, partly closed state). Agreement of the fitted $w$ with an independent measurement (FRET between the domains, or enzyme kinetics) strengthens the conclusion.
