---
title: Reactions in Solution, Photochemistry and Catalysis
source_hash: ce2e58b88cbf
---

The rate theories of [6.3.16](/6.3.16) treat isolated collisions in the gas phase. Real chemistry, and especially the chemistry of living systems, mostly takes place in solution, is often driven by light, and almost always involves a catalyst. This chapter discusses how these three factors change reaction rates. For reactions in solution (17.1) we must account for the surrounding solvent molecules: the reactants first have to diffuse together, and diffusion itself may be the rate-determining step; reactions between ions are also affected by ionic strength and by the dielectric constant, where we use the Debye–Hückel theory of [6.3.12](/6.3.12) and the transition state theory of [6.3.16](/6.3.16). Photochemistry (17.2) studies excited-state molecules produced by the absorption of photons: their energy comes from light rather than from thermal motion, so they can undergo reactions with $\Delta_{\mathrm{r}}G > 0$, as in photosynthesis; the decay processes of excited states (fluorescence, phosphorescence, quenching) are also the basis of fluorescence spectroscopy, a basic tool of biology. Catalytic kinetics (17.3) makes the qualitative description of catalysts in [6.1.7](/6.1.7#sec-7.3.4) quantitative, and ends with the Michaelis–Menten kinetics of enzymes.

This chapter makes heavy use of the **steady-state approximation** and the **pre-equilibrium approximation** of [6.3.15](/6.3.15): encounter pairs, excited-state molecules and catalyst–substrate complexes are all reactive intermediates in mechanisms. Heterogeneous catalysis requires a knowledge of adsorption on solid surfaces and is treated in [6.3.20](/6.3.20); enzyme inhibition and regulation are left to [biochemistry](/7.1).

## 17.1. Reactions in Solution

### 17.1.1. Solvent Effects and the Cage Effect

**Definition 17.1.1** The influence of the solvent on the rate of a reaction (and on its mechanism) is called the **solvent effect**.

There are two ways to study solvent effects: compare a reaction in solution with the same reaction in the gas phase, or compare it in different solvents. Solvent effects fall roughly into two kinds:

- physical effects: the solvent serves as a medium that transports energy and matter (diffusion); the dielectric properties of the solvent affect the interaction between ions and polar molecules; the ionic strength affects the activities of ions; solvation changes the energies of the reactants and of the activated complex;
- chemical effects: the solvent itself is a catalyst, a reactant or a product (as in hydrolysis and solvolysis).

The solvent affects the rate constant mainly by changing the activation energy. If the solvent has no specific interaction with the reactant molecules and acts only as a medium, the rate constant is close to that in the gas phase. For the first-order decomposition of $\ce{N2O5}$ at $298\,\mathrm{K}$:

| Medium | Gas phase | $\ce{CCl4}$ | $\ce{CHCl3}$ | $\ce{CH3NO2}$ | $\ce{Br2}$ |
|---|---|---|---|---|---|
| $k/(10^{-5}\,\mathrm{s^{-1}})$ | 3.38 | 4.09 | 3.72 | 3.13 | 4.27 |

In all the media the activation energy lies between $100$ and $107\,\mathrm{kJ\,mol^{-1}}$ and $\lg(A/\mathrm{s^{-1}}) \approx 13.5$.

**Definition 17.1.2** Reactant molecules in solution are surrounded by solvent molecules, as if they were in a "cage" made of solvent molecules, and they must push the surrounding solvent molecules aside to diffuse out. This phenomenon is called the **cage effect**. When two reactant molecules diffuse into the same solvent cage they form an **encounter pair** $\{\mathrm{A{:}B}\}$, which collide repeatedly inside the cage until they react or diffuse apart.

The cage effect reduces collisions between molecules that are far apart, but makes a pair that has already met collide about $10^2$ times in one encounter. The two effects roughly cancel, so the overall collision frequency in solution is close to that in the gas phase. For reactions with a large activation energy that need many collisions to occur, the cage effect alone therefore has little influence; for reactions with a very small activation energy that occur almost at every collision, such as radical recombination, the rate is limited by diffusion. The cage effect has a chemical consequence as well: a pair of radicals produced by photolysis or pyrolysis is held in the same cage and has a considerable probability of recombining before they diffuse apart (geminate recombination), so the quantum yield of photolysis in solution is lower than in the gas phase.

### 17.1.2. Diffusion Control and Activation Control

Regard the encounter pair as an intermediate in the mechanism:

$$
\ce{A + B <=>[k_{\mathrm{d}}][k_{-\mathrm{d}}] \{A{:}B\} ->[k_{\mathrm{r}}] P},
$$
where $k_{\mathrm{d}}$ is the rate constant for the formation of the encounter pair by diffusion, $k_{-\mathrm{d}}$ that for the separation of the pair by diffusion, and $k_{\mathrm{r}}$ the rate constant for the reaction of the pair. Applying the steady-state approximation to the encounter pair, $k_{\mathrm{d}}[\ce{A}][\ce{B}] = (k_{-\mathrm{d}} + k_{\mathrm{r}})[\{\ce{A{:}B}\}]$,

$$
v = k_{\mathrm{r}}[\{\ce{A{:}B}\}] = k[\ce{A}][\ce{B}], \qquad k = \frac{k_{\mathrm{d}}k_{\mathrm{r}}}{k_{-\mathrm{d}} + k_{\mathrm{r}}}. \tag{17.1}
$$

**Definition 17.1.3** If $k_{\mathrm{r}} \gg k_{-\mathrm{d}}$, the encounter pair reacts as soon as it forms, $k = k_{\mathrm{d}}$, and the rate is determined by the rate at which the reactants diffuse toward each other; such a reaction is called a **diffusion-controlled reaction**. If $k_{\mathrm{r}} \ll k_{-\mathrm{d}}$, then $k = \frac{k_{\mathrm{d}}}{k_{-\mathrm{d}}}k_{\mathrm{r}} = K_{\mathrm{AB}}k_{\mathrm{r}}$ ($K_{\mathrm{AB}}$ is the equilibrium constant for the formation of the encounter pair), and the rate is determined by the rate at which the encounter pair crosses the energy barrier; such a reaction is called an **activation-controlled reaction**.

Activation control is the result of the pre-equilibrium approximation (the formation and separation of the encounter pair are in fast equilibrium). The solvent then acts only through $K_{\mathrm{AB}}$ and the solvation energy contained in $k_{\mathrm{r}}$, and the rate can be discussed with transition state theory (17.1.4–17.1.6). In a solvent of high viscosity diffusion slows down, and a reaction that was activation-controlled may become diffusion-controlled.

### 17.1.3. Rate Constants of Diffusion-Controlled Reactions

Let A be at rest at the origin, with B molecules diffusing around it with diffusion coefficient $D_{\mathrm{B}}$. As soon as B reaches the sphere of radius $R = r_{\mathrm{AB}} = r_{\mathrm{A}} + r_{\mathrm{B}}$, it forms an encounter pair with A and reacts immediately (a perfectly absorbing sphere). The number density $n(r, t)$ of B satisfies the diffusion equation (the **heat equation**, [2.5.7](/2.5.7)) $\frac{\partial n}{\partial t} = D_{\mathrm{B}}\Delta n$ with boundary conditions

$$
n(R, t) = 0, \qquad n(\infty, t) = n_{\mathrm{B}}^\infty.
$$

In the steady state $\Delta n = 0$. By spherical symmetry only the radial part of the Laplace operator remains ([2.5.5](/2.5.5#sec-5.1.1)), and the **Laplace equation** reduces to an ordinary differential equation

$$
\frac{1}{r^2}\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}n}{\mathrm{d}r}\right) = 0 \quad\Rightarrow\quad n(r) = C_1 + \frac{C_2}{r},
$$
and the boundary conditions give

$$
n(r) = n_{\mathrm{B}}^\infty\left(1 - \frac{R}{r}\right).
$$
By **Fick's law** the flux density of B toward A in the radial direction is $D_{\mathrm{B}}\frac{\mathrm{d}n}{\mathrm{d}r}$, and the total rate of inflow through a sphere of radius $r$ is

$$
I = 4\pi r^2D_{\mathrm{B}}\frac{\mathrm{d}n}{\mathrm{d}r} = 4\pi r^2D_{\mathrm{B}}\frac{n_{\mathrm{B}}^\infty R}{r^2} = 4\pi D_{\mathrm{B}}Rn_{\mathrm{B}}^\infty,
$$
independent of $r$ (there is no accumulation in the steady state). Each A molecule reacts with $I$ B molecules per unit time. In fact A also moves; the diffusion coefficient of the relative displacement of two independently Brownian particles is $D_{\mathrm{A}} + D_{\mathrm{B}}$ (variances of independent random variables add), so $D_{\mathrm{B}}$ is replaced by $D_{\mathrm{A}} + D_{\mathrm{B}}$. Multiplying by the number density of A and converting to molar concentrations gives:

**Theorem 17.1.1 (Smoluchowski Equation)** The rate constant of a diffusion-controlled reaction is

$$
k_{\mathrm{d}} = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})r_{\mathrm{AB}}N_{\mathrm{A}}. \tag{17.2}
$$

How long does it take to establish the steady state? The time-dependent solution is $n(r, t) = n_{\mathrm{B}}^\infty\left[1 - \frac{R}{r}\operatorname{erfc}\frac{r - R}{2\sqrt{Dt}}\right]$ (the **error function**; it is solved in the same way as the half-line problem of [2.5.7](/2.5.7#sec-7.3)), from which $k(t) = 4\pi DR\left(1 + \frac{R}{\sqrt{\pi Dt}}\right)N_{\mathrm{A}}$: at the initial moment the B molecules near A have not yet been consumed and the rate is larger, and after $t \gg R^2/D$ it approaches the steady-state value. For $R = 0.5\,\mathrm{nm}$ and $D = 10^{-9}\,\mathrm{m^2\,s^{-1}}$, $R^2/D \approx 0.25\,\mathrm{ns}$, so the steady-state value can be used in ordinary experiments.

To estimate the diffusion coefficient from the properties of the solvent, we need the following relation.

**Theorem 17.1.2 (Stokes–Einstein Equation)** The diffusion coefficient of a spherical particle of radius $r$ in a solvent of viscosity $\eta$ is

$$
D = \frac{k_{\mathrm{B}}T}{6\pi\eta r}.
$$

It has two ingredients. The Einstein relation $D = k_{\mathrm{B}}T/f$ connects the diffusion coefficient with the friction coefficient $f$ (the ratio of drag force to velocity): under an external force $F$ the drift velocity of the particle is $F/f$, and at equilibrium the drift flux balances the diffusion flux while the concentration obeys the **Boltzmann distribution**, which yields this relation (for the derivation and a discussion of Brownian motion see [6.3.21](/6.3.21)). The other ingredient is the Stokes drag $F = 6\pi\eta rv$ on a sphere moving slowly in a viscous fluid ([5.1.2](/5.1.2#sec-2.3)), that is, $f = 6\pi\eta r$. For particles of molecular size hydrodynamics is only approximate, and the diffusion coefficients of small molecules in water often deviate from this formula by up to a factor of two, but the order of magnitude and the variation with viscosity and temperature are correct.

Substituting into Eq. (17.2),

$$
k_{\mathrm{d}} = 4\pi N_{\mathrm{A}}\frac{k_{\mathrm{B}}T}{6\pi\eta}\left(\frac{1}{r_{\mathrm{A}}} + \frac{1}{r_{\mathrm{B}}}\right)(r_{\mathrm{A}} + r_{\mathrm{B}}) = \frac{2RT}{3\eta}\frac{(r_{\mathrm{A}} + r_{\mathrm{B}})^2}{r_{\mathrm{A}}r_{\mathrm{B}}}.
$$
For $r_{\mathrm{A}} = r_{\mathrm{B}}$ (the factor $(r_{\mathrm{A}} + r_{\mathrm{B}})^2/(r_{\mathrm{A}}r_{\mathrm{B}})$ has its minimum value 4 at $r_{\mathrm{A}} = r_{\mathrm{B}}$ and is close to 4 for molecules of not very different sizes),

$$
k_{\mathrm{d}} \approx \frac{8RT}{3\eta}.
$$
The molecular size cancels completely: larger molecules diffuse more slowly, but the "target" is also larger. Per pair of molecules the rate constant is $8k_{\mathrm{B}}T/(3\eta)$; multiplying by $N_{\mathrm{A}}$ gives the molar value used here. For water at $25\,^\circ\mathrm{C}$, $\eta = 0.890\,\mathrm{mPa\,s}$,

$$
k_{\mathrm{d}} = \frac{8 \times 8.314 \times 298.15}{3 \times 0.890 \times 10^{-3}}\,\mathrm{m^3\,mol^{-1}\,s^{-1}} = 7.4 \times 10^9\,\mathrm{L\,mol^{-1}\,s^{-1}}.
$$
This is the upper limit of the rate constant of a bimolecular reaction between neutral molecules in solution. A reaction with a measured value close to $10^9$–$10^{10}\,\mathrm{L\,mol^{-1}\,s^{-1}}$ can be judged to be diffusion-controlled, such as radical recombination, oxygen quenching of fluorescence (17.2.5) and the "perfect" enzyme (17.3.5). Oppositely charged ions attract each other and the rate constant can be larger (the Debye correction to the Smoluchowski formula); the value $1.4 \times 10^{11}\,\mathrm{L\,mol^{-1}\,s^{-1}}$ of $\ce{H+ + OH-}$ ([6.3.15](/6.3.15#sec-15.9.2)) also benefits from the relay of the proton along hydrogen bonds. The apparent activation energy of a diffusion-controlled reaction is the activation energy of viscosity, about $10$–$20\,\mathrm{kJ\,mol^{-1}}$ for water and most organic solvents.

### 17.1.4. Effect of Ionic Strength: The Primary Salt Effect

**Definition 17.1.4** The influence of the ionic strength of a dilute solution on the rate constant of a reaction between ions is called the **primary kinetic salt effect**.

Consider $\ce{A^{z_A} + B^{z_B} <=> X^{\ddagger(z_A + z_B)} -> P}$. In transition state theory the pre-equilibrium must be expressed in terms of activities:

$$
K^{\ddagger\circ} = \frac{(c^{\ddagger}/c^\circ)\gamma^{\ddagger}}{(c_{\mathrm{A}}/c^\circ)\gamma_{\mathrm{A}}(c_{\mathrm{B}}/c^\circ)\gamma_{\mathrm{B}}}, \qquad v = \frac{k_{\mathrm{B}}T}{h}c^{\ddagger} = \frac{k_{\mathrm{B}}T}{h}\frac{K^{\ddagger\circ}}{c^\circ}\frac{\gamma_{\mathrm{A}}\gamma_{\mathrm{B}}}{\gamma^{\ddagger}}c_{\mathrm{A}}c_{\mathrm{B}},
$$
so that

$$
k = k_0\frac{\gamma_{\mathrm{A}}\gamma_{\mathrm{B}}}{\gamma^{\ddagger}}, \qquad k_0 = \frac{k_{\mathrm{B}}T}{h}\frac{K^{\ddagger\circ}}{c^\circ},
$$
where $k_0$ is the rate constant at infinite dilution (all **activity coefficients** equal 1). In dilute solution we use the **Debye–Hückel limiting law** ([6.3.12](/6.3.12)) $\lg\gamma_i = -Az_i^2\sqrt{I_b/b^\circ}$, the charge of the activated complex being $z_{\mathrm{A}} + z_{\mathrm{B}}$:

**Theorem 17.1.3 (Brønsted–Bjerrum Equation)** The rate constant of an ionic reaction in dilute solution satisfies

$$
\lg\frac{k}{k_0} = -A\left[z_{\mathrm{A}}^2 + z_{\mathrm{B}}^2 - (z_{\mathrm{A}} + z_{\mathrm{B}})^2\right]\sqrt{I_b/b^\circ} = 2Az_{\mathrm{A}}z_{\mathrm{B}}\sqrt{I_b/b^\circ}, \tag{17.3}
$$
with $A = 0.509$ in aqueous solution at $25\,^\circ\mathrm{C}$.

![Primary kinetic salt effect in aqueous solution at 25 °C: lg(k/k0) is linear in the square root of the ionic strength with slope 2AzAzB; the shaded region lies beyond the range of the Debye–Hückel limiting law (about I_b < 0.01 mol/kg)](./plots/kinetic-salt-effect.py)

- $z_{\mathrm{A}}z_{\mathrm{B}} > 0$ (ions of the same sign): $k$ increases with ionic strength (positive salt effect). The activated complex has a higher charge, and the stabilization by the ionic atmosphere (the decrease of the activity coefficient) is larger for it than for the reactants.
- $z_{\mathrm{A}}z_{\mathrm{B}} < 0$ (ions of opposite signs): $k$ decreases with ionic strength (negative salt effect).
- One reactant is a neutral molecule: the ionic strength does not affect $k$ (within the range of the limiting law).

Classical verifications (Brønsted, La Mer and others): $[\ce{Co(NH3)5Br}]^{2+} + \ce{Hg^2+}$ ($z_{\mathrm{A}}z_{\mathrm{B}} = 4$), $\ce{S2O8^2- + I-}$ ($+2$), the acid-catalyzed inversion of sucrose ($0$) and $[\ce{Co(NH3)5Br}]^{2+} + \ce{OH-}$ ($-2$); the slopes all agree with Eq. (17.3). Equation (17.3) holds quantitatively only for $I_b \lesssim 0.01\,\mathrm{mol\,kg^{-1}}$; at higher concentrations the extended Debye–Hückel equation must be used. Conversely, measuring the variation of the rate constant with ionic strength allows us to determine the product of the charges of the two ions in the rate-determining step, which is one means of inferring a mechanism. The primary kinetic salt effect has the same origin as the **salt effect** of [6.1.10](/6.1.10) (ionic strength increases the solubility of a sparingly soluble salt): in both cases the ionic atmosphere lowers the activities of the ions. At low ionic strength, adding a salt that does not take part in the reaction changes the concentration of the catalytic ion by shifting the dissociation equilibrium of a weak electrolyte (such as a buffer); this is called the secondary salt effect and is different from the primary salt effect.

### 17.1.5. Effect of the Dielectric Constant

The electrostatic interaction between ions depends on the **relative permittivity** $\varepsilon_{\mathrm{r}}$ of the solvent. In the simplest "two-sphere" model, two ions with charges $z_{\mathrm{A}}e$ and $z_{\mathrm{B}}e$ approach from infinity to a distance $a$ to form the activated complex, which requires work $\frac{z_{\mathrm{A}}z_{\mathrm{B}}e^2}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}a}$ in the medium (**Coulomb's law**). This work is included in the Gibbs free energy of activation,

$$
\ln k = \ln k_{\infty} - \frac{z_{\mathrm{A}}z_{\mathrm{B}}e^2N_{\mathrm{A}}}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}aRT},
$$
where $k_\infty$ is the rate constant in the hypothetical limit $\varepsilon_{\mathrm{r}} \to \infty$ (no electrostatic interaction between the ions). (The Gaussian-units form often seen in the literature has no $4\pi\varepsilon_0$; the reference state of $k_\infty$ is $\varepsilon_{\mathrm{r}} \to \infty$, not infinite dilution.) $\ln k$ is linear in $1/\varepsilon_{\mathrm{r}}$: ions of the same sign react more slowly in a solvent of small dielectric constant, and ions of opposite signs react faster. Take $z_{\mathrm{A}}z_{\mathrm{B}} = -1$, $a = 0.3\,\mathrm{nm}$ and water at $25\,^\circ\mathrm{C}$ ($\varepsilon_{\mathrm{r}} = 78.4$): the electrostatic term is $2.4$, so electrostatic attraction increases the rate constant by a factor of about 10; in a solvent whose $\varepsilon_{\mathrm{r}}$ is only half that of water the increase is about a factor of 100.

### 17.1.6. Solvent Polarity and Solvation

The solvent solvates the reactants and the activated complex to different degrees, which changes the activation energy:

- If the activated complex (or the product) is more polar than the reactants, a polar solvent stabilizes it more strongly, the activation energy decreases and $k$ increases; otherwise $k$ decreases.
- If the activated complex is solvated to a greater degree than the reactants, the solvent lowers the activation energy; if the reactants are solvated more, the activation energy increases.

The Menshutkin reaction (a tertiary amine and an alkyl halide give a quaternary ammonium salt) produces an ion pair from two neutral molecules, and the activated complex has a large charge separation:

```smiles
CCN(CC)CC (C2H5)3N
CCI C2H5I
CC[N+](CC)(CC)CC.[I-] (C2H5)4N+I-
```

Data for it in different solvents at $373\,\mathrm{K}$:

| Solvent | Hexane | Toluene | Benzene | Nitrobenzene |
|---|---|---|---|---|
| $k/(10^{-5}\,\mathrm{L\,mol^{-1}\,s^{-1}})$ | 0.5 | 25.3 | 39.8 | 138.3 |
| $E_{\mathrm{a}}/(\mathrm{kJ\,mol^{-1}})$ | 66.9 | 54.4 | 47.7 | 48.5 |
| $\lg(A/(\mathrm{L\,mol^{-1}\,s^{-1}}))$ | 4.0 | 4.0 | 3.3 | 3.9 |

From nonpolar hexane to polar nitrobenzene the rate constant increases by nearly a factor of 300, mainly because of the decrease in activation energy. The pre-exponential factor is very small ($10^{3}$–$10^{4}$, far below the value of about $10^{11}$ of collision theory), corresponding to a very negative entropy of activation: the activated complex orients the surrounding solvent molecules, which is exactly the entropic cost of solvation.

## 17.2. Photochemical Reactions

### 17.2.1. Characteristics of Photochemical Reactions

**Definition 17.2.1** A chemical reaction caused by the absorption of a **photon** by a molecule is called a **photochemical reaction**; in contrast, a reaction whose activation energy is supplied by the thermal motion of molecules is called a thermal reaction.

Photosynthesis $\ce{6CO2 + 6H2O ->[h\nu] C6H12O6 + 6O2}$, the exposure of $\ce{AgBr}$ in photographic film, and the ozone depletion initiated in the stratosphere by $\ce{CFCl3 ->[h\nu] CFCl2 + Cl}$ ($\ce{Cl + O3 -> ClO + O2}$, $\ce{ClO + O -> Cl + O2}$, with the Cl atom as a catalyst) are all photochemical reactions.

The energy of a photon is $\varepsilon = h\nu = hc/\lambda$ ([5.5.1](/5.5.1)); the energy of 1 mol of photons is

$$
E_{\mathrm{m}} = N_{\mathrm{A}}\frac{hc}{\lambda} = \frac{0.1196\,\mathrm{J\,m\,mol^{-1}}}{\lambda}.
$$
The energy of 1 mol of photons used to be called 1 "einstein"; it is not an SI unit, and this site simply writes "1 mol of photons" ($N_{\mathrm{A}}$, $h$ and $c$ are all exact values).

| Light | $\lambda/\mathrm{nm}$ | Energy of 1 mol of photons $/(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|
| Ultraviolet | 150–400 | 800–300 |
| Visible | 400–700 | 300–170 |
| Near infrared | 700–2500 | 170–48 |

Chemical bond energies are mostly $150$–$500\,\mathrm{kJ\,mol^{-1}}$, and the electronic transitions of molecules also lie in the ultraviolet and visible regions, so generally only ultraviolet and visible light can cause photochemical reactions; infrared photons can only excite vibrations.

The main differences between photochemical and thermal reactions:

1. Thermodynamics: at constant temperature and pressure $\Delta_{\mathrm{r}}G \le W'$ (the non-volume work received by the system, [6.3.3](/6.3.3)). In a thermal reaction $W' = 0$ and only $\Delta_{\mathrm{r}}G < 0$ is possible; in a photochemical reaction the absorbed light does work on the system ($W' > 0$) and $\Delta_{\mathrm{r}}G$ may be greater than zero. For photosynthesis $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} \approx +2879\,\mathrm{kJ\,mol^{-1}}$ (per mole of glucose, [6.3.18](/6.3.18#sec-18.4.1)), driven by the light energy absorbed by chlorophyll.
2. The activation energy comes from photons; the rate depends mainly on the intensity of the absorbed light and is little affected by temperature.
3. The reaction is wavelength-selective: only light that can be absorbed by the reactant (or a photosensitizer) and has sufficient energy is effective.
4. The reacting species are electronically excited molecules, whose structure, acidity and basicity, and reactivity all differ from those of the ground state.

### 17.2.2. Basic Laws of Photochemistry

**Theorem 17.2.1 (First Law of Photochemistry)** Only light absorbed by a system can cause a photochemical reaction (the Grotthuss–Draper law, 1817–1841).

**Theorem 17.2.2 (Second Law of Photochemistry)** In the primary process of a photochemical reaction, one molecule absorbs one photon and is activated (the Stark–Einstein law, 1908–1912).

The second law holds only for the primary process and only for ordinary light intensities: with intense lasers two-photon absorption can occur (two-photon fluorescence microscopy makes use of this).

**Definition 17.2.2** The process in which a substance absorbs a photon and goes from the ground state to an excited state (or dissociates directly) is called the **primary photochemical process**, for example $\ce{Hg ->[h\nu] Hg^*}$ and $\ce{Br2 ->[h\nu] 2Br}$. The various physical and chemical processes that the products of the primary process (excited molecules, atoms, radicals) subsequently undergo are called secondary processes.

**Definition 17.2.3 (Beer–Lambert Law)** When parallel monochromatic light of intensity $I_0$ passes through a homogeneous absorbing medium of concentration $c$ and path length $l$, the transmitted intensity $I$ satisfies

$$
A = \lg\frac{I_0}{I} = \varepsilon cl,
$$
which is called the **Beer–Lambert law**. $A$ is called the (decadic) **absorbance** and $\varepsilon$ the **molar absorption coefficient** (unit $\mathrm{L\,mol^{-1}\,cm^{-1}}$); it depends on the substance, the wavelength, the temperature and the solvent.

This law follows from a simple differential equation: the fraction of light absorbed in a thin layer of thickness $\mathrm{d}x$ is proportional to the number of absorbing molecules in the layer, $-\mathrm{d}I = \kappa cI\,\mathrm{d}x$, and integration gives $I = I_0\mathrm{e}^{-\kappa cl}$ with $\kappa = \varepsilon\ln 10$ ($\kappa$ is the Napierian molar absorption coefficient). The absorbed intensity is $I_0 - I = I_0(1 - 10^{-\varepsilon cl})$; the amount of photons absorbed per unit volume and unit time is denoted $I_{\mathrm{a}}$ and plays the role of a "reactant" in photochemical rate equations. The Beer–Lambert law fails at very high concentrations, when molecules associate, or when the light is not monochromatic; it is the basis of the quantitative analysis by absorption spectroscopy ([6.4](/6.4)).

### 17.2.3. Quantum Yield

Not every absorbed photon causes a reaction, and a primary process that does lead to reaction may trigger a series of secondary reactions.

**Definition 17.2.4** The ratio of the number of reactant molecules that react (or of product molecules formed) to the number of photons absorbed is called the **quantum yield**:

$$
\Phi = \frac{\text{number of molecules reacting}}{\text{number of photons absorbed}} = \frac{\text{amount of reactant consumed}}{\text{amount of photons absorbed}}, \qquad \Phi' = \frac{\text{amount of product formed}}{\text{amount of photons absorbed}}.
$$
In kinetics it is often written $\Phi = v/I_{\mathrm{a}}$.

$\Phi$ and $\Phi'$ can differ. The mechanism of the photolysis of HBr, $\ce{2HBr ->[h\nu] H2 + Br2}$ ($\lambda \approx 200\,\mathrm{nm}$), is

$$
\ce{HBr ->[h\nu] H + Br}, \qquad \ce{H + HBr -> H2 + Br}, \qquad \ce{2Br + M -> Br2 + M},
$$
so each absorbed photon consumes 2 HBr and produces 1 $\ce{H2}$: $\Phi(\ce{HBr}) = 2$, $\Phi'(\ce{H2}) = 1$. $\Phi > 1$ indicates a chain reaction or some other amplification in the secondary processes: in the photochemical reaction of $\ce{H2}$ with $\ce{Cl2}$ ([6.3.15](/6.3.15#sec-15.7.2)) a chain initiated by one photon can produce $10^6$ HCl molecules. $\Phi < 1$ indicates that some excited molecules lose their energy through physical processes before reacting, or that the primary products recombine in the cage (17.1.1).

### 17.2.4. Excited States and the Jablonski Diagram

**Definition 17.2.5** When the total electron spin quantum number of a molecule is $S$, the $z$ component of the total spin angular momentum has $2S + 1$ possible values, and $2S + 1$ is called the **spin multiplicity**. A state in which all electrons are paired ($S = 0$, multiplicity 1) is called a **singlet state**, denoted $\mathrm{S}_0$ (ground state), $\mathrm{S}_1$, $\mathrm{S}_2$, …; a state with two unpaired electrons of parallel spin ($S = 1$, multiplicity 3) is called a **triplet state**, denoted $\mathrm{T}_1$, $\mathrm{T}_2$, …

The ground state of most stable molecules is a singlet ($\ce{O2}$ is the famous exception, with a triplet ground state). For the same electronic configuration the triplet state lies lower in energy than the singlet: two electrons with parallel spins avoid each other because of the Pauli principle (**electron spin**, [5.5.4](/5.5.4#sec-4.2.3); in atoms this is Hund's rule) and repel each other less. Electric dipole transitions require the spin to be unchanged (a **selection rule**), so the absorption $\mathrm{S}_0 \to \mathrm{S}_1$ is strong whereas $\mathrm{S}_0 \to \mathrm{T}_1$ hardly occurs; triplet states arise mainly by "crossing" from singlet states.

**Definition 17.2.6** A diagram that shows the electronic states of a molecule (arranged by multiplicity) together with their vibrational levels as an energy-level diagram, and uses arrows to represent the radiative and nonradiative processes that follow the absorption of a photon, is called a **Jablonski diagram**. The processes in the diagram are:

- **Vibrational relaxation**: within the same electronic state, a molecule in a higher vibrational level transfers the excess vibrational energy to solvent molecules by collisions and drops to the lowest vibrational level of that electronic state.
- **Internal conversion**: a nonradiative transition between two electronic states of the same multiplicity, from a low vibrational level of the higher electronic state to a high vibrational level of the lower electronic state at the same energy, such as $\mathrm{S}_2 \to \mathrm{S}_1$.
- **Intersystem crossing**: a nonradiative transition between electronic states of different multiplicity, such as $\mathrm{S}_1 \to \mathrm{T}_1$ and $\mathrm{T}_1 \to \mathrm{S}_0$. It is spin-forbidden and occurs through spin–orbit coupling, which heavy atoms (Br, I, transition metals) speed up.
- **Fluorescence**: radiation emitted in the transition from $\mathrm{S}_1$ back to $\mathrm{S}_0$ (multiplicity unchanged).
- **Phosphorescence**: radiation emitted in the transition from $\mathrm{T}_1$ back to $\mathrm{S}_0$ (multiplicity changed).

![Jablonski diagram: vibrational levels of the singlet states S0, S1, S2 and the triplet states T1, T2, with absorption, vibrational relaxation, internal conversion, intersystem crossing (ISC), fluorescence and phosphorescence; typical time scales are indicated](./plots/jablonski-diagram.py)

The vast differences in time scale determine the fate of the excited state. Absorption takes about $10^{-15}\,\mathrm{s}$ (the nuclei have no time to move: the Franck–Condon principle), while vibrational relaxation and internal conversion $\mathrm{S}_n \to \mathrm{S}_1$ take about $10^{-12}\,\mathrm{s}$; so whatever level is excited, light emission and chemical reaction almost always start from the lowest vibrational level of $\mathrm{S}_1$ or $\mathrm{T}_1$, an empirical rule known as *Kasha's rule*. The fluorescence lifetime is about $10^{-9}$–$10^{-6}\,\mathrm{s}$ (nanoseconds for most organic molecules), and fluorescence disappears as soon as the light source is switched off; the fluorescence wavelength is longer than that of the absorbed light (the Stokes shift) because vibrational relaxation and solvent reorganization after absorption consume part of the energy. Phosphorescence is spin-forbidden and has a much longer lifetime, from about $10^{-4}\,\mathrm{s}$ to seconds or even longer; because of the long triplet lifetime, triplets are mostly quenched in solution, and phosphorescence often has to be observed in rigid media at low temperature. Both fluorescence and phosphorescence are "cold light" and have nothing to do with the thermal radiation of hot bodies.

### 17.2.5. Quenching, Sensitization and the Stern–Volmer Equation

**Definition 17.2.7** The process in which an excited molecule $\ce{A^*}$ interacts with another molecule Q, loses its excitation energy and returns to the ground state without emitting light is called **quenching**, and Q is called the quencher. Quenching proceeds by energy transfer, electron transfer, promotion of intersystem crossing and so on; oxygen (with a triplet ground state), iodide ion and heavy-atom compounds are common quenchers.

Energy transfer $\ce{A^* + D -> A + D^*}$ is quenching for A and sensitization for D.

Suppose that $\ce{A^*}$ in the $\mathrm{S}_1$ state has three decay pathways: fluorescence (rate constant $k_{\mathrm{f}}$), nonradiative decay (internal conversion and intersystem crossing, $k_{\mathrm{nr}}$) and quenching by Q ($k_{\mathrm{q}}[\ce{Q}]$). Under constant illumination the steady-state approximation for $\ce{A^*}$ gives $I_{\mathrm{a}} = (k_{\mathrm{f}} + k_{\mathrm{nr}} + k_{\mathrm{q}}[\ce{Q}])[\ce{A^*}]$, and the quantum yield of fluorescence is

$$
\Phi_{\mathrm{f}} = \frac{k_{\mathrm{f}}[\ce{A^*}]}{I_{\mathrm{a}}} = \frac{k_{\mathrm{f}}}{k_{\mathrm{f}} + k_{\mathrm{nr}} + k_{\mathrm{q}}[\ce{Q}]}.
$$
Without quencher $\Phi_{\mathrm{f}}^0 = k_{\mathrm{f}}\tau_0$, where $\tau_0 = 1/(k_{\mathrm{f}} + k_{\mathrm{nr}})$ is the intrinsic lifetime of the excited state. Dividing the two:

**Theorem 17.2.3 (Stern–Volmer Equation)** For collisional (dynamic) quenching, the fluorescence intensity $F$ (proportional to $\Phi_{\mathrm{f}}$) and the lifetime $\tau$ satisfy

$$
\frac{F_0}{F} = \frac{\tau_0}{\tau} = 1 + k_{\mathrm{q}}\tau_0[\ce{Q}] = 1 + K_{\mathrm{SV}}[\ce{Q}],
$$
where $K_{\mathrm{SV}} = k_{\mathrm{q}}\tau_0$ is called the Stern–Volmer constant.

A plot of $F_0/F$ against $[\ce{Q}]$ is a straight line with slope $K_{\mathrm{SV}}$; measuring $\tau_0$ with a pulsed laser then gives the bimolecular rate constant $k_{\mathrm{q}}$ of quenching. The fluorescence lifetime is only nanoseconds, and the quencher must diffuse to the excited molecule within that time, so $k_{\mathrm{q}}$ is often close to the upper limit of $10^{10}\,\mathrm{L\,mol^{-1}\,s^{-1}}$ for diffusion control (17.1.3); fluorescence quenching is therefore a probe of the rate at which molecules meet in solution. If the quencher first forms a nonluminescent complex with the ground-state molecule (static quenching, binding constant $K_{\mathrm{s}}$), then $F_0/F = (1 + K_{\mathrm{SV}}[\ce{Q}])(1 + K_{\mathrm{s}}[\ce{Q}])$ curves upward, while the lifetime ratio $\tau_0/\tau$ still reflects only the dynamic part; comparing the intensity data with the lifetime data distinguishes the two mechanisms.

![Stern–Volmer plot (simulated data, 2% noise): for dynamic quenching both F0/F and τ0/τ are straight lines in [Q], and the least-squares KSV is close to the true value of 40 L/mol; when static quenching is also present, F0/F curves upward while τ0/τ is unchanged](./plots/stern-volmer.py)

In biophysics, the extent to which tryptophan fluorescence in a protein is quenched by iodide ion or acrylamide reflects whether it is exposed to the solvent; the efficiency of fluorescence resonance energy transfer (FRET) falls off with the sixth power of the distance between donor and acceptor, and is used as an "optical ruler" for measuring intramolecular distances of $1$–$10\,\mathrm{nm}$.

**Definition 17.2.8** A reactant that is itself insensitive to light and cannot absorb a certain light directly reacts after another substance, which absorbs that light, transfers the energy to the reactant and is itself unchanged by the reaction, has been added. This process is called **photosensitization**, and the added substance is called a **photosensitizer**.

Example: the dissociation energy of $\ce{H2}$ is $436\,\mathrm{kJ\,mol^{-1}}$ and the energy of $253.7\,\mathrm{nm}$ ultraviolet photons is $471.5\,\mathrm{kJ\,mol^{-1}}$, which is sufficient, but $\ce{H2}$ does not absorb at this wavelength (its absorption lies in the vacuum ultraviolet below $110\,\mathrm{nm}$), and irradiation cannot dissociate it. After adding mercury vapor,

$$
\ce{Hg ->[h\nu] Hg^*}, \qquad \ce{Hg^* + H2 -> Hg + 2H},
$$
mercury is the photosensitizer. What decides whether light can act is first of all absorption (the first law), not just the photon energy. In photosynthesis, pigments such as chlorophyll absorb visible light and pass the energy to the reaction center, where electron transfer converts the light energy into chemical energy; the pigments themselves are not consumed, and this is the most important photosensitized system in nature. In a dye-sensitized solar cell, the dye adsorbed on $\ce{TiO2}$ is excited by light and injects an electron into the conduction band of the semiconductor, and is then reduced by $\ce{I-}/\ce{I3-}$ in the electrolyte, which is the same principle.

### 17.2.6. Rate Equations of Photochemical Reactions

The rate of the primary process depends only on the rate of light absorption: $v_1 = \Phi_1I_{\mathrm{a}}$ (usually $\Phi_1 = 1$), independent of reactant concentration (zero order); secondary processes are treated as thermal reactions. Take the photolysis of HI, $\ce{2HI ->[h\nu] H2 + I2}$, as an example, with the mechanism

$$
\ce{HI ->[h\nu] H + I}\ (I_{\mathrm{a}}), \qquad \ce{H + HI ->[k_2] H2 + I}, \qquad \ce{2I + M ->[k_3] I2 + M}.
$$
Applying the steady-state approximation to H, $I_{\mathrm{a}} = k_2[\ce{H}][\ce{HI}]$,

$$
-\frac{\mathrm{d}[\ce{HI}]}{\mathrm{d}t} = I_{\mathrm{a}} + k_2[\ce{H}][\ce{HI}] = 2I_{\mathrm{a}}, \qquad \Phi(\ce{HI}) = 2.
$$

### 17.2.7. Photostationary States

**Definition 17.2.9** For an opposing reaction whose forward direction is photochemical and whose reverse direction is thermal, the steady state reached under constant illumination when the forward and reverse rates are equal is called the **photostationary state** (photochemical equilibrium).

Anthracene dimerizes in solution under light, and the dimer decomposes back to anthracene when heated in the dark:

```smiles
c1ccc2cc3ccccc3cc2c1 C14H10
c1ccc2c(c1)C1c3ccccc3C2C2c3ccccc3C1c1ccccc12 C28H20
```

$\ce{2C14H10 ->[h\nu] C28H20}$ with $v_1 = k_1I_{\mathrm{a}}$; $\ce{C28H20 ->[k_2] 2C14H10}$ with $v_2 = k_2[\ce{C28H20}]$. In the photostationary state $k_1I_{\mathrm{a}} = k_2[\ce{C28H20}]$,

$$
[\ce{C28H20}]_{\mathrm{ss}} = \frac{k_1}{k_2}I_{\mathrm{a}}.
$$
The concentration of the dimer is proportional to the absorbed light intensity; at a given light intensity (with the light fully absorbed) it is independent of the concentration of anthracene.

The differences between a photostationary state and thermal equilibrium:

1. A photostationary state is a nonequilibrium steady state maintained by a continuous supply of energy from outside; when the illumination stops the system returns to thermal equilibrium. It does not satisfy $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$, and the "equilibrium constant" varies with the light intensity.
2. A photochemical reaction can drive the system in the direction of $\Delta_{\mathrm{r}}G > 0$ (17.2.1), so the composition of the photostationary state can be far from the thermal equilibrium composition.
3. The temperature coefficient of a photochemical rate constant is small and sometimes negative; thermal reactions are strongly affected by temperature.
4. The forward reaction in a photostationary state is a reaction of excited molecules, and the thermal reaction is a reaction of ground-state molecules.

The photostationary state is a simple example of the nonequilibrium steady states discussed in [6.3.18](/6.3.18); the photoisomerization of retinal in vision and the photoconversion of plant phytochrome between two configurations both depend on photostationary states.

### 17.2.8. Chemiluminescence

**Definition 17.2.10** The light emitted when a chemical reaction produces a product in an electronically excited state and the excited state returns to the ground state is called **chemiluminescence**.

Chemiluminescence can be regarded as the reverse of a photochemical reaction: chemical energy is converted into light energy. It requires that the energy released by the reaction be sufficient to produce an electronically excited state (about $170$–$300\,\mathrm{kJ\,mol^{-1}}$ for visible light) and that there be a pathway that concentrates the energy in one product molecule. In a glow stick, a diaryl oxalate is oxidized by $\ce{H2O2}$ to the high-energy intermediate 1,2-dioxetanedione, which gives its energy to the added fluorescent dye as it decomposes into two $\ce{CO2}$ molecules; the color of the light emitted by the dye determines the color of the glow stick (9,10-bis(phenylethynyl)anthracene is green, rhodamine B is red). The bioluminescence of fireflies is produced by the oxidation of luciferin catalyzed by luciferase, and is used as a reporter gene in molecular biology. The infrared radiation emitted by vibrationally excited products of a reaction is called infrared chemiluminescence, and is a tool for studying the partition of reaction energy ([6.3.16](/6.3.16#sec-16.5)).

## 17.3. Kinetics of Catalytic Reactions

### 17.3.1. General Properties of Catalysts

The definitions of **catalyst** and **catalysis** are given in [6.1.7](/6.1.7#def-7.3.6); the research of W. Ostwald between 1888 and 1905 made the concept explicit (for which he received the 1909 Nobel Prize in Chemistry). According to the phase in which the catalyst and the reactants are found, catalysis is divided into **homogeneous catalysis**, **heterogeneous catalysis** ([6.3.20](/6.3.20)) and **enzyme catalysis**; according to the mechanism of action there are acid–base catalysis, coordination (complex) catalysis, redox catalysis and so on. The general properties of catalysts are:

1. The catalyst takes part in the reaction and changes its mechanism, lowering the apparent activation energy (in most cases) or raising the pre-exponential factor (in a few cases), so that $k_{\text{cat}} \gg k_{\text{uncat}}$.
2. The amount and chemical nature of the catalyst are unchanged by the reaction, but its physical properties (particle size, crystal form, surface state) may change.
3. A catalyst cannot change the direction or the extent of a reaction: it cannot make a reaction with $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ occur, nor does it change the equilibrium constant. By detailed balance ([6.3.15](/6.3.15#sec-15.5.2)), $k_1/k_{-1} = K^\circ(c^\circ)^{\sum\nu_{\mathrm{B}}}$ is independent of the catalyst, so a catalyst speeds up the forward and the reverse reaction by the same factor and only shortens the time needed to reach equilibrium.
4. Catalysts are selective; a small amount of impurity can markedly enhance or weaken the catalytic action.

**Definition 17.3.1** When the same reactant can give several products, the fraction of the feed converted into the desired product relative to the total amount of feed converted is called the **selectivity** of the catalyst:

$$
\text{selectivity} = \frac{\text{amount of feed A converted to the desired product}}{\text{total amount of feed A converted}} \times 100\%.
$$
A substance that has no or only a small catalytic activity itself but, added in small amount, markedly improves the activity, selectivity or stability of a catalyst is called a **promoter**, such as $\ce{K2O}$ (an electronic promoter) and $\ce{Al2O3}$ (a structural promoter that prevents sintering of the iron microcrystals) in the iron catalyst for ammonia synthesis.

An impurity that lowers or destroys the activity of a catalyst is called a poison, and the phenomenon is **catalyst poisoning** ([6.1.7](/6.1.7#sec-7.3.4)).

### 17.3.2. Lowering of the Activation Energy and Change of the Activation Entropy by Catalysts

Let the uncatalyzed elementary reaction $\ce{A + B -> AB}$ have activation energy $E_0$. With a catalyst K added, the mechanism is

$$
\ce{A + K <=>[k_1][k_{-1}] AK}\ \ (\text{fast equilibrium}), \qquad \ce{AK + B ->[k_2] AB + K}\ \ (\text{slow}).
$$
By the pre-equilibrium approximation, $[\ce{AK}] = \frac{k_1}{k_{-1}}[\ce{A}][\ce{K}]$,

$$
v = k_2[\ce{AK}][\ce{B}] = \frac{k_1k_2}{k_{-1}}[\ce{K}][\ce{A}][\ce{B}] = k[\ce{A}][\ce{B}], \qquad k = \frac{k_1k_2}{k_{-1}}[\ce{K}],
$$
and the apparent activation energy is $E_{\mathrm{a}} = E_1 + E_2 - E_{-1}$ (the **apparent activation energy**, [6.3.15](/6.3.15#def-15.5.1)). If it is smaller than $E_0$, the catalyzed reaction is faster. The rate is proportional to the concentration of the catalyst, which is often experimental evidence that "the catalyst takes part in the reaction and forms an intermediate compound"; since the catalyst itself appears in the rate equation, the reaction order may also change. The activation energies ($\mathrm{kJ\,mol^{-1}}$) of some reactions with and without catalyst:

| Reaction | Uncatalyzed | Catalyzed | Catalyst |
|---|---|---|---|
| $\ce{2HI -> H2 + I2}$ | 184.1 | 104.6 | Au |
| $\ce{2H2O -> 2H2 + O2}$ | 244.8 | 136.0 | Pt |
| $\ce{2N2O -> 2N2 + O2}$ | 245 | 134.0 | Pt |
| $\ce{3H2 + N2 -> 2NH3}$ | 334.7 | 167.4 | $\ce{Fe-Al2O3-K2O}$ |

In some catalytic reactions the activation energy decreases only a little but the rate increases greatly; the same reaction on different catalysts may have similar activation energies but very different rates. This is explained by the entropy of activation: from the Eyring equation ([6.3.16](/6.3.16#sec-16.3.2)), $k \propto \mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\mathrm{e}^{-\Delta^{\ddagger}H^\circ/RT}$, and if the catalyst reduces the entropy loss of the activated complex (for example by pre-binding the reactants in a suitable position and orientation), it accelerates the reaction by increasing the pre-exponential factor.

### 17.3.3. General Mechanism of Homogeneous Catalysis

In **homogeneous catalysis**, the reactant (substrate S) is activated by forming an intermediate X with a catalytic active center of definite structure ($\ce{H+}$, $\ce{OH-}$, the central metal of a complex, some group of an enzyme), and X then reacts to give the product and regenerates the catalyst:

$$
\ce{S + C <=>[k_1][k_{-1}] X + Y}, \qquad \ce{X + W ->[k_2] P + Z},
$$
$v = k_2[\ce{X}][\ce{W}]$. There are two treatments according to the nature of the intermediate X:

- Arrhenius-type intermediate ($k_2[\ce{W}] \ll k_{-1}[\ce{Y}]$): the first step is in fast equilibrium and the pre-equilibrium approximation applies. Let $K = k_1/k_{-1}$. If $[\ce{S}]_0 \gg [\ce{C}]_0$, conservation of the catalyst $[\ce{C}] + [\ce{X}] = [\ce{C}]_0$ gives

  $$
  [\ce{X}] = \frac{K[\ce{S}]_0[\ce{C}]_0}{[\ce{Y}] + K[\ce{S}]_0}, \qquad v = \frac{k_2K[\ce{S}]_0[\ce{C}]_0[\ce{W}]}{K[\ce{S}]_0 + [\ce{Y}]};
  $$
  if $[\ce{S}]_0 \ll [\ce{C}]_0$, conservation of the substrate gives $v = \frac{k_2K[\ce{S}]_0[\ce{C}]_0[\ce{W}]}{K[\ce{C}]_0 + [\ce{Y}]}$. Such intermediates are fairly stable, have appreciable concentrations and lie below the reactants in energy.
- van 't Hoff-type intermediate ($k_2[\ce{W}] \gg k_{-1}[\ce{Y}]$): the intermediate is converted rapidly as soon as it forms, its concentration is very small and the steady-state approximation applies; it lies above the reactants in energy.

Enzyme catalysis (17.3.5) is the special case $[\ce{S}]_0 \gg [\ce{C}]_0$, and the two treatments give the two derivations of the Michaelis–Menten equation.

### 17.3.4. Acid–Base Catalysis

**Definition 17.3.2** A reaction catalyzed by $\ce{H+}$ and $\ce{OH-}$ (in the generalized sense, by Brønsted acids and bases) is called **acid–base catalysis**. In acid catalysis the substrate first accepts a proton to form a reactive protonated intermediate $\ce{SH+}$, which is then converted to the product with release of the proton; in base catalysis the substrate first loses a proton (or combines with $\ce{OH-}$).

When catalysis is by $\ce{H+}$ and $\ce{OH-}$ only (specific acid–base catalysis), the pseudo-first-order rate constant in aqueous solution is

$$
k = k_0 + k_{\ce{H+}}[\ce{H+}] + k_{\ce{OH-}}[\ce{OH-}] = k_0 + k_{\ce{H+}}[\ce{H+}] + \frac{k_{\ce{OH-}}K_{\mathrm{w}}}{[\ce{H+}]},
$$
where $k_0$ is the uncatalyzed (water-catalyzed) rate constant and $K_{\mathrm{w}}$ is the **ionic product of water** (in terms of concentrations). In a plot of $\lg k$ against pH the slope is $-1$ in the acidic region and $+1$ in the basic region, and there may be a plateau of $k_0$ in between. $\frac{\mathrm{d}k}{\mathrm{d}[\ce{H+}]} = 0$ gives the minimum

$$
[\ce{H+}]_{\min} = \sqrt{\frac{k_{\ce{OH-}}K_{\mathrm{w}}}{k_{\ce{H+}}}}, \qquad \text{that is}\quad k_{\ce{H+}}[\ce{H+}]_{\min} = k_{\ce{OH-}}[\ce{OH-}]_{\min}.
$$
Conversely, from measured $k_{\ce{H+}}$, $k_{\ce{OH-}}$ and the $[\ce{H+}]_{\min}$ at the rate minimum one has $K_{\mathrm{w}} = k_{\ce{H+}}[\ce{H+}]_{\min}^2/k_{\ce{OH-}}$: in 1893 Wijs determined the ionic product of water in this way from the hydrolysis of ethyl acetate.

![Rate–pH profile of specific acid–base catalysis (parameters close to the hydrolysis of ethyl acetate at 25 °C: kH+ = 1.1 × 10⁻⁴, kOH− = 0.11 L mol⁻¹ s⁻¹); the slopes are −1 in the acidic region and +1 in the basic region, and the minimum is at pH ≈ 5.5](./plots/acid-base-ph-profile.py)

When other weak acids HA and weak bases $\ce{A-}$ in solution (such as a buffer) can also catalyze (general acid–base catalysis), $k$ contains further terms such as $k_{\ce{HA}}[\ce{HA}] + k_{\ce{A-}}[\ce{A-}]$; varying the buffer concentration at constant pH distinguishes specific from general acid–base catalysis. The catalytic power of an acid is related to its strength.

**Theorem 17.3.1 (Brønsted Catalysis Law)** Within a family of reactions, the catalytic rate constant of a general acid HA and its **acid dissociation constant** satisfy

$$
k_{\ce{HA}} = G_{\mathrm{a}}K_{\mathrm{a}}^{\alpha}, \qquad k_{\ce{A-}} = G_{\mathrm{b}}K_{\mathrm{b}}^{\beta},
$$
where $G_{\mathrm{a}}$, $G_{\mathrm{b}}$ are constants and $0 < \alpha, \beta < 1$.

The exponents $\alpha$ and $\beta$ cannot be omitted. Taking logarithms, $\lg k_{\ce{HA}} = \alpha\lg K_{\mathrm{a}} + \lg G_{\mathrm{a}}$: the change in the Gibbs free energy of activation is a fraction $\alpha$ of the change in the reaction Gibbs free energy. This is the earliest linear free-energy relationship; $\alpha$ close to 0 means that little proton transfer has occurred in the transition state (an "early" transition state), and close to 1 that the proton is almost completely transferred. The active centers of enzymes make extensive use of general acid–base catalysis (for example the imidazole group of histidine, $\mathrm{p}K_{\mathrm{a}} \approx 6$–$7$, which can act as an acid or a base at physiological pH).

### 17.3.5. Enzyme Catalysis: Michaelis–Menten Kinetics

The characteristics of **enzyme catalysis** are given in [6.1.7](/6.1.7#sec-7.3.4): high specificity, high efficiency and mild conditions, combining features of homogeneous and heterogeneous catalysis (the enzyme molecule is dissolved in the solution, but the reaction occurs at an active center on the surface of the molecule). The rate of an enzyme-catalyzed reaction as a function of substrate concentration is a saturation curve, and the simplest mechanism, proposed by Michaelis and Menten (1913) and by Briggs and Haldane (1925), is

$$
\ce{E + S <=>[k_1][k_{-1}] ES ->[k_2] E + P},
$$
where E is the enzyme and ES the enzyme–substrate complex. Let the total enzyme concentration be $[\ce{E}]_0$ with $[\ce{S}] \gg [\ce{E}]_0$ (the consumption of substrate is negligible), and measure the initial rate $v = k_2[\ce{ES}]$.

Briggs–Haldane derivation: apply the steady-state approximation to ES, $k_1[\ce{E}][\ce{S}] = (k_{-1} + k_2)[\ce{ES}]$; conservation of the enzyme $[\ce{E}] = [\ce{E}]_0 - [\ce{ES}]$ then gives $[\ce{ES}] = \frac{[\ce{E}]_0[\ce{S}]}{K_{\mathrm{M}} + [\ce{S}]}$.

**Theorem 17.3.2 (Michaelis–Menten Equation)** Under the above conditions,

$$
v = \frac{k_{\mathrm{cat}}[\ce{E}]_0[\ce{S}]}{K_{\mathrm{M}} + [\ce{S}]} = \frac{v_{\max}[\ce{S}]}{K_{\mathrm{M}} + [\ce{S}]}, \qquad K_{\mathrm{M}} = \frac{k_{-1} + k_2}{k_1}, \tag{17.4}
$$
where $k_{\mathrm{cat}} = k_2$ and $v_{\max} = k_{\mathrm{cat}}[\ce{E}]_0$.

**Definition 17.3.3** In Eq. (17.4), $K_{\mathrm{M}} = \frac{k_{-1} + k_2}{k_1}$ is called the **Michaelis constant**; it equals the substrate concentration at which the rate reaches $v_{\max}/2$. When the enzyme is saturated with substrate, the number of substrate molecules converted per active center per unit time, $k_{\mathrm{cat}} = v_{\max}/[\ce{E}]_0$, is called the **catalytic constant** (turnover number).

The original derivation of Michaelis and Menten used the pre-equilibrium approximation: assuming that $\ce{E + S <=> ES}$ is in fast equilibrium ($k_2 \ll k_{-1}$) gives an equation of the same form, with $K_{\mathrm{M}}$ replaced by the dissociation constant $K_{\mathrm{S}} = k_{-1}/k_1$ of ES. The relation between the two derivations is exactly the steady state versus pre-equilibrium discussed in [6.3.15](/6.3.15#sec-15.6.2): $K_{\mathrm{M}} = K_{\mathrm{S}} + k_2/k_1 \ge K_{\mathrm{S}}$, and only when $k_2 \ll k_{-1}$ is $K_{\mathrm{M}}$ a measure of the affinity of the substrate for the enzyme; in general it is inaccurate to interpret $K_{\mathrm{M}}$ directly as a "dissociation constant". The steady-state approximation is valid for an enzyme when $[\ce{E}]_0 \ll [\ce{S}]_0 + K_{\mathrm{M}}$ (the Segel criterion); some enzymes in cells have concentrations comparable to their substrates, and a more complete treatment is then needed.

The reaction order varies with substrate concentration:

- $[\ce{S}] \ll K_{\mathrm{M}}$: $v = \frac{k_{\mathrm{cat}}}{K_{\mathrm{M}}}[\ce{E}]_0[\ce{S}]$, first order in the substrate. $k_{\mathrm{cat}}/K_{\mathrm{M}}$ is the apparent second-order rate constant for the reaction of free enzyme with substrate and is called the *specificity constant*; it cannot exceed the rate constant $10^8$–$10^9\,\mathrm{L\,mol^{-1}\,s^{-1}}$ for the enzyme and the substrate to meet by diffusion (17.1.3). The $k_{\mathrm{cat}}/K_{\mathrm{M}}$ of triosephosphate isomerase and acetylcholinesterase is already close to this upper limit; such enzymes are called "catalytically perfect", and their rates are diffusion-controlled.
- $[\ce{S}] \gg K_{\mathrm{M}}$: $v = v_{\max}$, zero order in the substrate; the active centers of the enzyme are saturated, in agreement with the zero-order reaction discussed in [6.1.7](/6.1.7#sec-7.3.2).
- $[\ce{S}] = K_{\mathrm{M}}$: $v = v_{\max}/2$.

The range of $k_{\mathrm{cat}}$ is wide, from about $0.5\,\mathrm{s^{-1}}$ for lysozyme to about $10^6\,\mathrm{s^{-1}}$ for carbonic anhydrase; $K_{\mathrm{M}}$ is mostly between $10^{-6}$ and $10^{-2}\,\mathrm{mol\,L^{-1}}$.

**Definition 17.3.4** Writing Eq. (17.4) in reciprocal form

$$
\frac{1}{v} = \frac{K_{\mathrm{M}}}{v_{\max}}\cdot\frac{1}{[\ce{S}]} + \frac{1}{v_{\max}},
$$
the method of plotting $1/v$ against $1/[\ce{S}]$ as a straight line and obtaining the parameters from the intercept $1/v_{\max}$ on the vertical axis and the intercept $-1/K_{\mathrm{M}}$ on the horizontal axis is called the **Lineweaver–Burk plot** (double-reciprocal plot).

The double-reciprocal plot is intuitive and helps to distinguish different types of enzyme inhibition ([7.1](/7.1)), but it is a poor method of parameter estimation. The problem is the same as the linearization problem discussed in [6.3.15](/6.3.15#sec-15.3.4): at low substrate concentrations $v$ is small and its relative error is large; taking reciprocals magnifies the errors of these points sharply, and they also lie at the far end of the line and have the greatest influence on the slope. The standard practice today is to apply **nonlinear regression** ([3.3](/3.3)) directly to Eq. (17.4), using `scipy.optimize.curve_fit` ([4.4.4](/4.4.4#sec-4.2.3)) to obtain $v_{\max}$ and $K_{\mathrm{M}}$ together with their standard errors. The figure below compares the two methods.

![Michaelis–Menten kinetics (vmax = 1, KM = 2, simulated data with a constant absolute noise of 0.03 vmax). Left: nonlinear fit and Lineweaver–Burk fit of one data set; middle: the double-reciprocal plot, with the low-concentration points at the far end; right: KM estimated by the two methods in 2000 simulated experiments, where the Lineweaver–Burk distribution is much wider and has a long tail](./plots/michaelis-menten-fit.py)

Temperature and pH also affect enzymes markedly: on heating, the reaction first speeds up according to the Arrhenius equation, and beyond a certain temperature the spatial structure of the enzyme is destroyed (denaturation) and the activity falls rapidly, hence the optimum temperature (the "increase then decrease" type in the table of [6.3.15](/6.3.15#sec-15.5.1)); the protonation state of the ionizable groups in the active center makes the activity a bell-shaped function of pH, with an optimum pH. Enzyme inhibition, allosteric regulation and multi-substrate mechanisms belong to biochemistry.

## Summary

| Topic | Key points |
|---|---|
| Encounter-pair mechanism | $k = \frac{k_{\mathrm{d}}k_{\mathrm{r}}}{k_{-\mathrm{d}} + k_{\mathrm{r}}}$; diffusion control $k = k_{\mathrm{d}}$, activation control $k = K_{\mathrm{AB}}k_{\mathrm{r}}$ |
| Diffusion-controlled rate constant | Spherically symmetric steady-state diffusion gives $k_{\mathrm{d}} = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})r_{\mathrm{AB}}N_{\mathrm{A}}$; Stokes–Einstein $D = k_{\mathrm{B}}T/(6\pi\eta r)$ gives $k_{\mathrm{d}} \approx 8RT/(3\eta)$ (about $7 \times 10^9\,\mathrm{L\,mol^{-1}\,s^{-1}}$ in water) |
| Primary salt effect | $\lg(k/k_0) = 2Az_{\mathrm{A}}z_{\mathrm{B}}\sqrt{I_b/b^\circ}$ (dilute solution) |
| Dielectric constant | $\ln k = \ln k_\infty - \frac{z_{\mathrm{A}}z_{\mathrm{B}}e^2N_{\mathrm{A}}}{4\pi\varepsilon_0\varepsilon_{\mathrm{r}}aRT}$ |
| Laws of photochemistry | Only absorbed light is effective; in the primary process one photon activates one molecule; $A = \lg(I_0/I) = \varepsilon cl$ |
| Quantum yield | $\Phi = v/I_{\mathrm{a}}$; $\Phi > 1$ means a chain reaction, $\Phi < 1$ physical deactivation |
| Excited states | Singlet, triplet; vibrational relaxation, internal conversion, intersystem crossing, fluorescence (ns), phosphorescence ($10^{-4}\,\mathrm{s}$ to seconds and longer) |
| Stern–Volmer | $F_0/F = \tau_0/\tau = 1 + k_{\mathrm{q}}\tau_0[\ce{Q}]$ |
| Photostationary state | Steady state of photochemical and thermal reactions; the composition varies with light intensity; not thermal equilibrium |
| Catalysts | Do not change the equilibrium; $E_{\mathrm{a}} = E_1 + E_2 - E_{-1}$; may also change the activation entropy; selectivity, promoters, poisons |
| Acid–base catalysis | $k = k_0 + k_{\ce{H+}}[\ce{H+}] + k_{\ce{OH-}}[\ce{OH-}]$, with a minimum in the rate–pH profile; Brønsted law $k_{\ce{HA}} = G_{\mathrm{a}}K_{\mathrm{a}}^{\alpha}$ |
| Enzyme catalysis | $v = \frac{k_{\mathrm{cat}}[\ce{E}]_0[\ce{S}]}{K_{\mathrm{M}} + [\ce{S}]}$, $K_{\mathrm{M}} = \frac{k_{-1} + k_2}{k_1}$; fit the parameters by nonlinear regression, not by the double-reciprocal plot |

## Questions

1. Why is the rate constant of a diffusion-controlled reaction almost independent of the size of the reactant molecules?

   **Answer** $k_{\mathrm{d}} \propto (D_{\mathrm{A}} + D_{\mathrm{B}})r_{\mathrm{AB}}$ and $D \propto 1/r$: the larger a molecule, the more slowly it diffuses, but the larger its collision radius, and the two effects approximately cancel.

2. The rate constant of an ionic reaction decreases as the ionic strength increases. What is the relation between the charges of the two ions in the rate-determining step?

   **Answer** $z_{\mathrm{A}}z_{\mathrm{B}} < 0$, ions of opposite sign; the value of $z_{\mathrm{A}}z_{\mathrm{B}}$ can also be estimated from the slope of $\lg(k/k_0)$ against $\sqrt{I_b}$.

3. The $\Delta_{\mathrm{r}}G$ of a photochemical reaction can be greater than zero. Does this violate the second law of thermodynamics?

   **Answer** No. In $\Delta_{\mathrm{r}}G \le W'$ the $W'$ is the work done on the system by the light; the entropy of the whole system including the light source still increases.

4. How can fluorescence lifetime measurements be used to distinguish dynamic from static quenching?

   **Answer** Dynamic quenching shortens the lifetime according to the Stern–Volmer equation; static quenching only reduces the number of luminescent molecules, and the lifetime of the remaining luminescent molecules is unchanged.
