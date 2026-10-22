---
title: Gases, Liquids and Solids
description: Using the ideal gas equation in chemical calculations; partial pressure, Dalton's law and mole fraction; energy distribution and the Boltzmann factor; effusion and Graham's law; real gases, critical parameters, phase diagrams and supercritical fluids; saturated vapor pressure and the Clausius–Clapeyron equation; boiling, supercooling and liquid crystals; crystals, lattices and unit cells, the seven crystal systems and 14 Bravais lattices; amorphous solids.
source_hash: c204c1477cd3
---

The macroscopic properties of matter are determined by the particles that compose it and the interactions between them, so inorganic chemistry begins with the three states of aggregation. In a gas the molecules are far apart and move almost freely; in a liquid they are in contact but can flow past one another; in a crystal the particles are arranged periodically and regularly. The kinetic theory of gases and real gases have already been treated systematically in the thermal physics part of physics ([5.2.1](/5.2.1), [5.2.2](/5.2.2)), so this chapter only reviews them and concentrates on their uses in chemistry: finding amounts of substance and molar masses from the equation of state, partial pressures in gas mixtures, the connection between energy distributions and reaction rates, and isotope separation. For liquids we discuss how the saturated vapor pressure varies with temperature (the Clausius–Clapeyron equation) and phase diagrams, which are an introduction to the phase-equilibrium theory of physical chemistry ([6.3](/6.3)). For solids we introduce the language of lattices and unit cells, which [6.1.4](/6.1.4) then uses to describe metallic, ionic and molecular crystals; the systematic theory of crystal symmetry and diffraction belongs to structural chemistry ([6.2](/6.2)). The Boltzmann factor of this chapter will be used in [6.1.7](/6.1.7) to explain the activation energy, and the condition for phase equilibrium will be fully understood only after Gibbs energy is introduced in [6.1.6](/6.1.6).

## 1.1. Gases

### 1.1.1. The Ideal Gas Equation of State

Four quantities describe the state of a fixed amount of gas: the pressure $p$ (chemists usually call it pressure, with the SI unit $\mathrm{Pa}$), the volume $V$, the temperature $T$ and the amount of substance $n$. Boyle's law ($pV$ is constant at fixed $T$ and $n$), Charles's law ($V \propto T$ at fixed $p$ and $n$) and Avogadro's law (equal volumes of gases at the same temperature and pressure contain equal numbers of molecules, $V \propto n$), established between the 17th and 19th centuries, combine to give the **equation of state** of the **ideal gas** ([5.2.1](/5.2.1#sec-1.1.6)):

$$
pV = nRT, \qquad pV_{\mathrm{m}} = RT,
$$
where $V_{\mathrm{m}} = V/n$ is the molar volume and the molar gas constant is $R = N_{\mathrm{A}}k_{\mathrm{B}} = 8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}$ ($N_{\mathrm{A}}$ and $k_{\mathrm{B}}$ are both defining constants of the SI, so $R$ is exact, $8.314\,462\,618\ldots$). The thermodynamic and Celsius temperatures are related by $T/\mathrm{K} = t/{}^\circ\mathrm{C} + 273.15$. In calculations all quantities are expressed in SI units; in chemistry $\mathrm{kPa}$ and $\mathrm{L}$ are often used, and their product is exactly a joule ($1\,\mathrm{kPa\,L} = 10^3\,\mathrm{Pa} \times 10^{-3}\,\mathrm{m^3} = 1\,\mathrm{J}$), so $R = 8.314\,\mathrm{kPa\,L\,mol^{-1}\,K^{-1}}$ is also convenient.

The ideal gas is a model in which the molecules have no volume of their own and interact only through elastic collisions; it is the limit of real gases as $p \to 0$, and at moderate pressures and not-too-low temperatures real gases approximately obey it (deviations are discussed in Section 1.1.5). Substituting $n = m/M$ ($m$ is the mass of the gas and $M$ its molar mass) gives the two most common variants in chemistry:

$$
M = \frac{mRT}{pV}, \qquad \rho = \frac{m}{V} = \frac{pM}{RT}.
$$
The first gives the molar mass of an unknown gas from weighing and a pressure measurement, and so identifies the gas; the second shows that at the same temperature and pressure the density of a gas is proportional to its molar mass.

**Example 1.1.1** Before preparing NaH from Na and $\ce{H2}$ above $300\,{}^\circ\mathrm{C}$ in the laboratory, the air in the apparatus is displaced with dry $\ce{N2}$ from a cylinder. The cylinder has a volume of $50.0\,\mathrm{L}$, a temperature of $25\,{}^\circ\mathrm{C}$ and a pressure of $15.2\,\mathrm{MPa}$. (1) Find the amount of substance and the mass of $\ce{N2}$ in the cylinder. (2) After five displacements the pressure has fallen to $13.8\,\mathrm{MPa}$; find the average volume of $\ce{N2}$ used per displacement, measured at $25\,{}^\circ\mathrm{C}$ and $0.100\,\mathrm{MPa}$.

Solution: (1) $n_1 = \dfrac{p_1V}{RT} = \dfrac{15.2 \times 10^6\,\mathrm{Pa} \times 50.0 \times 10^{-3}\,\mathrm{m^3}}{8.314\,\mathrm{J\,mol^{-1}\,K^{-1}} \times 298.15\,\mathrm{K}} = 307\,\mathrm{mol}$, $m = n_1M = 307\,\mathrm{mol} \times 28.0\,\mathrm{g\,mol^{-1}} = 8.59\,\mathrm{kg}$.

(2) The $\ce{N2}$ consumed is $\Delta n = \dfrac{(p_1 - p_2)V}{RT} = 28.2\,\mathrm{mol}$, or $5.65\,\mathrm{mol}$ per displacement, whose volume at $0.100\,\mathrm{MPa}$ is $V = \dfrac{\Delta n RT}{5p} = \dfrac{5.65 \times 8.314 \times 298.15}{1.00 \times 10^5}\,\mathrm{m^3} = 0.140\,\mathrm{m^3} = 140\,\mathrm{L}$.

**Example 1.1.2** Argon obtained by fractional distillation of liquid air has a mass of $0.7990\,\mathrm{g}$ and occupies $0.4448\,\mathrm{L}$ at $298.15\,\mathrm{K}$ and $111.46\,\mathrm{kPa}$. Find the molar mass of argon and its density at $0\,{}^\circ\mathrm{C}$ and $101.325\,\mathrm{kPa}$.

Solution: $M = \dfrac{mRT}{pV} = \dfrac{0.7990\,\mathrm{g} \times 8.314\,\mathrm{kPa\,L\,mol^{-1}\,K^{-1}} \times 298.15\,\mathrm{K}}{111.46\,\mathrm{kPa} \times 0.4448\,\mathrm{L}} = 39.95\,\mathrm{g\,mol^{-1}}$, so the relative atomic mass is $A_{\mathrm{r}}(\ce{Ar}) = 39.95$. $\rho = \dfrac{pM}{RT} = \dfrac{101.325 \times 39.95}{8.314 \times 273.15}\,\mathrm{g\,L^{-1}} = 1.782\,\mathrm{g\,L^{-1}}$.

$0\,{}^\circ\mathrm{C}$ and $101.325\,\mathrm{kPa}$ was the old "standard temperature and pressure"; the molar volume of an ideal gas there is $22.414\,\mathrm{L\,mol^{-1}}$. The current IUPAC standard pressure is $p^\circ = 100\,\mathrm{kPa}$ (the standard state of [6.1.6](/6.1.6)), at which the molar volume at $0\,{}^\circ\mathrm{C}$ is $22.711\,\mathrm{L\,mol^{-1}}$. When quoting data, check which pressure was used.

### 1.1.2. Gas Mixtures

Air, combustion products and the gases in reaction systems are mostly mixtures. If the components do not react with one another and can all be treated as ideal gases, the mixture is called an ideal gas mixture: the motion of each kind of molecule is unaffected by the others, so each component exerts the same pressure on the walls as if it were present alone.

**Definition 1.1.1 (Partial Pressure and Mole Fraction)** The ratio of the amount of substance $n_{\mathrm{B}}$ of component B in a mixture to the total amount $n = \sum_{\mathrm{B}} n_{\mathrm{B}}$,

$$
x_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{n}, \qquad \sum_{\mathrm{B}} x_{\mathrm{B}} = 1
$$
is called the **mole fraction** of B (also the amount fraction); the **partial pressure** of B in a gas mixture is defined as $p_{\mathrm{B}} = x_{\mathrm{B}}p$, where $p$ is the total pressure of the mixture.

**Theorem 1.1.1 (Dalton's Law of Partial Pressures)** In an ideal gas mixture the partial pressure of component B equals the pressure it would exert if it alone occupied the whole volume of the mixture at the same temperature,

$$
p_{\mathrm{B}} = \frac{n_{\mathrm{B}}RT}{V},
$$
and the total pressure is the sum of the partial pressures: $p = \sum_{\mathrm{B}} p_{\mathrm{B}}$.

**Proof** The mixture as a whole obeys $pV = nRT$, so $p_{\mathrm{B}} = x_{\mathrm{B}}p = \dfrac{n_{\mathrm{B}}}{n}\cdot\dfrac{nRT}{V} = \dfrac{n_{\mathrm{B}}RT}{V}$; summing over B and using $\sum_{\mathrm{B}} x_{\mathrm{B}} = 1$ gives $\sum_{\mathrm{B}} p_{\mathrm{B}} = p$. $\square$

The definition $p_{\mathrm{B}} = x_{\mathrm{B}}p$ applies to any gas mixture, whereas the interpretation "the pressure when alone in the whole volume" holds only for ideal gas mixtures. From the viewpoint of kinetic theory, the root of Dalton's law is that the pressure of an ideal gas depends only on the number of molecules per unit volume and the temperature ($p = n_Vk_{\mathrm{B}}T$), not on the kind of molecule. Partial pressure is the basic variable in discussing gas-phase chemical equilibrium ([6.1.8](/6.1.8)).

**Example 1.1.3 (Collection over Water)** A mixture of $\ce{KClO3}$ and $\ce{MnO2}$ is heated and the mass of solid decreases by $0.480\,\mathrm{g}$; $0.377\,\mathrm{L}$ of oxygen is collected over water at $294\,\mathrm{K}$ with the atmospheric pressure at $99.6\,\mathrm{kPa}$, the saturated vapor pressure of water at this temperature being $2.48\,\mathrm{kPa}$. Find the molar mass of $\ce{O2}$.

Solution: The collection bottle contains a mixture of $\ce{O2}$ and water vapor, and when the liquid levels inside and outside the bottle are equal the total pressure equals the atmospheric pressure, so $p(\ce{O2}) = 99.6 - 2.48 = 97.1\,\mathrm{kPa}$,

$$
n(\ce{O2}) = \frac{97.1\,\mathrm{kPa} \times 0.377\,\mathrm{L}}{8.314\,\mathrm{kPa\,L\,mol^{-1}\,K^{-1}} \times 294\,\mathrm{K}} = 0.0150\,\mathrm{mol}, \qquad M(\ce{O2}) = \frac{0.480\,\mathrm{g}}{0.0150\,\mathrm{mol}} = 32.0\,\mathrm{g\,mol^{-1}}.
$$

### 1.1.3. Kinetic Theory and Energy Distribution

The kinetic theory of gases ([5.2.1](/5.2.1)) derives the pressure formula $pV = \frac{1}{3}Nm\overline{v^2}$ from the microscopic model of the ideal gas; comparison with the equation of state gives the statistical meaning of temperature: the mean translational kinetic energy of a molecule is $\frac{1}{2}m\overline{v^2} = \frac{3}{2}k_{\mathrm{B}}T$. Molecular speeds follow the **Maxwell speed distribution**, and the three characteristic speeds are ([5.2.1](/5.2.1#sec-1.5.3))

$$
v_{\mathrm{p}} = \sqrt{\frac{2RT}{M}}, \qquad \bar v = \sqrt{\frac{8RT}{\pi M}}, \qquad v_{\mathrm{rms}} = \sqrt{\frac{3RT}{M}},
$$
the **most probable speed**, the mean speed and the **root-mean-square speed**, whose ratio is about $1 : 1.13 : 1.22$. In these formulas $M$ must be in $\mathrm{kg\,mol^{-1}}$. Kinetic theory also explains the three gas laws: a smaller volume increases the number of molecules per unit volume and so the frequency of wall collisions (Boyle's law); a higher temperature raises the mean kinetic energy, so at constant pressure the volume must increase (Charles's law); and the pressure depends only on the number density and the temperature (Avogadro's law and Dalton's law).

**Example 1.1.4** Find the root-mean-square speeds of He and $\ce{N2}$ at $298\,\mathrm{K}$.

Solution: $v_{\mathrm{rms}}(\ce{He}) = \sqrt{\dfrac{3 \times 8.314 \times 298}{4.003 \times 10^{-3}}}\,\mathrm{m\,s^{-1}} = 1.36 \times 10^3\,\mathrm{m\,s^{-1}}$, $v_{\mathrm{rms}}(\ce{N2}) = \sqrt{\dfrac{3 \times 8.314 \times 298}{28.01 \times 10^{-3}}}\,\mathrm{m\,s^{-1}} = 515\,\mathrm{m\,s^{-1}}$. At the same temperature, molecules of larger molar mass move more slowly, $v_{\mathrm{rms}} \propto M^{-1/2}$.

More important in chemistry is the distribution of molecular energies. Chemical reactions and the evaporation of liquids require molecules with sufficiently high energy, so what matters is the fraction of molecules with energy not lower than a threshold $E_0$. According to the **Boltzmann distribution** ([5.2.1](/5.2.1#sec-1.7.2)), the relative probability of a state of energy $E$ is proportional to the **Boltzmann factor** $\mathrm{e}^{-E/(k_{\mathrm{B}}T)}$; in chemistry energies are often given per mole, $E/(k_{\mathrm{B}}T) = E_{\mathrm{m}}/(RT)$, and below $E$ is understood as a molar energy and the exponent is written $\mathrm{e}^{-E/(RT)}$.

**Formula 1.1.1 (Fraction of Molecules with Energy Not Below $E_0$)** (1) If the energy of a molecule is a sum of two quadratic terms (such as the translational kinetic energy of a molecule moving in a plane, or the relative kinetic energy of two molecules along one direction in collision theory), the energy distribution is $f(E) = \frac{1}{RT}\mathrm{e}^{-E/(RT)}$ and

$$
\frac{N(E \ge E_0)}{N} = \int_{E_0}^{\infty} f(E)\,\mathrm{d}E = \mathrm{e}^{-E_0/(RT)}.
$$
(2) The distribution of three-dimensional translational kinetic energy is $f(E) = \frac{2}{\sqrt{\pi}}(RT)^{-3/2}E^{1/2}\mathrm{e}^{-E/(RT)}$, and with $x = E_0/(RT)$,

$$
\frac{N(E \ge E_0)}{N} = \operatorname{erfc}\sqrt{x} + 2\sqrt{\frac{x}{\pi}}\,\mathrm{e}^{-x} \approx 2\sqrt{\frac{x}{\pi}}\,\mathrm{e}^{-x} \quad (x \gg 1).
$$

Case (1) is the precise meaning of the commonly quoted "simplified form of the Maxwell–Boltzmann distribution law" $f_{E_0} = \mathrm{e}^{-E_0/(RT)}$; in (2) the prefactor $2\sqrt{x/\pi}$ varies only slowly with temperature, so in both cases the temperature dependence of the fraction of high-energy molecules is dominated by the Boltzmann factor $\mathrm{e}^{-E_0/(RT)}$.

**Example 1.1.5** Take $E_0 = 50\,\mathrm{kJ\,mol^{-1}}$ and compare the fractions of molecules with energy not below $E_0$ at $298\,\mathrm{K}$ and $308\,\mathrm{K}$.

Solution: At $298.15\,\mathrm{K}$, $x = 20.17$ and $\mathrm{e}^{-x} = 1.74 \times 10^{-9}$; at $308.15\,\mathrm{K}$, $x = 19.52$ and $\mathrm{e}^{-x} = 3.35 \times 10^{-9}$. A temperature rise of only $10\,\mathrm{K}$ (an increase of just $3\%$ in the mean kinetic energy) almost doubles the fraction of high-energy molecules (by the three-dimensional formula, a factor of $1.9$). This is why the rate of many reactions increases by a factor of 2–4 for every $10\,\mathrm{K}$ rise; [6.1.7](/6.1.7) will develop the activation energy and the Arrhenius equation from it.

![Distribution of molecular translational energy at two temperatures. The shaded tails are the fractions with E ≥ E0 = 50 kJ/mol; the inset shows that a 10 K rise nearly doubles this fraction](./plots/energy-distribution.py)

### 1.1.4. Diffusion and Effusion

Gas molecules move incessantly and at random, so different gases mix completely and matter migrates from regions of high concentration to regions of low concentration; this is diffusion. Macroscopic diffusion proceeds through a large number of collisions, and its rate is determined by the diffusion coefficient $D = \frac{1}{3}\bar v\bar\lambda$ (**Fick's law**, [5.2.2](/5.2.2#sec-2.4.3)), which depends both on the molecular speed and on the **mean free path**, that is, on the size of the molecules and the kind of surrounding gas. Another, simpler process depends only on the molecular speed:

**Definition 1.1.2** The escape of gas molecules through a small hole in a wall, where the size of the hole is much smaller than the mean free path of the molecules so that the molecules do not collide with one another while passing through, is called **effusion**.

In effusion, the number of molecules passing through the hole per unit time equals the **wall collision rate** times the area of the hole, $\Gamma A = \frac{1}{4}n_V\bar vA$. At the same temperature and pressure two gases have the same $n_V$, so the ratio of their effusion rates is the ratio of their mean speeds, and $\bar v \propto M^{-1/2}$.

**Theorem 1.1.2 (Graham's Law)** At the same temperature and pressure, the ratio of the effusion rates of two gases equals the inverse of the square root of the ratio of their molar masses (or densities):

$$
\frac{r_{\mathrm{A}}}{r_{\mathrm{B}}} = \sqrt{\frac{M_{\mathrm{B}}}{M_{\mathrm{A}}}} = \sqrt{\frac{\rho_{\mathrm{B}}}{\rho_{\mathrm{A}}}}.
$$

Graham obtained this rule experimentally (studying diffusion in 1833 and effusion in 1846) and originally stated it as "the rate of diffusion of a gas is inversely proportional to the square root of its density". By the derivation above it holds strictly for effusion; all three characteristic speeds are proportional to $\sqrt{T/M}$, so the result is the same whichever speed is used. The rate of macroscopic diffusion also depends on the collision cross sections of the molecules and on the surrounding gas, and can be estimated by Graham's law only approximately. A classic demonstration places cotton plugs soaked in concentrated aqueous ammonia and concentrated hydrochloric acid at the two ends of a glass tube; $\ce{NH3(g) + HCl(g) -> NH4Cl(s)}$ forms a ring of white smoke in the tube. By Graham's law $\sqrt{M(\ce{HCl})/M(\ce{NH3})} = \sqrt{36.46/17.03} = 1.46$, so the ring should form at about $59\%$ of the tube length from the ammonia end; it is indeed closer to the HCl end, but the two gases diffuse through air rather than effuse, and the actual position deviates from this estimate.

**Example 1.1.6 (Separation of Uranium Isotopes)** Compare the densities and effusion rates of $^{235}\mathrm{UF_6}$, $^{238}\mathrm{UF_6}$ and $\ce{H2}$ at $100.0\,\mathrm{kPa}$ and $100.0\,{}^\circ\mathrm{C}$.

Solution: $\rho = pM/(RT)$ with $RT = 8.314 \times 373.15\,\mathrm{J\,mol^{-1}} = 3102\,\mathrm{J\,mol^{-1}}$,

$$
\rho(^{235}\mathrm{UF_6}) = \frac{100.0 \times 349.0}{3102}\,\mathrm{g\,L^{-1}} = 11.25\,\mathrm{g\,L^{-1}}, \quad \rho(^{238}\mathrm{UF_6}) = 11.35\,\mathrm{g\,L^{-1}}, \quad \rho(\ce{H2}) = 0.06498\,\mathrm{g\,L^{-1}}.
$$
The ratio of effusion rates is $r(\ce{H2}) : r(^{235}\mathrm{UF_6}) : r(^{238}\mathrm{UF_6}) = 1 : 0.07600 : 0.07568$, and the ratio of the two $\ce{UF6}$ species is only $\sqrt{352.0/349.0} = 1.0043$. Each pass through a porous membrane raises the abundance ratio of $^{235}\mathrm{U}$ by only $0.43\%$, so enriching from the natural abundance of $0.71\%$ to about $3\%$ for nuclear fuel requires several hundred stages in series (see the uranium enrichment example in [5.2.1](/5.2.1#sec-1.6.3)). Gaseous diffusion consumes enormous amounts of electricity and has now been replaced by gas centrifuges.

### 1.1.5. Real Gases and Critical Phenomena

The deviation of a real gas from ideal behavior can be measured by the *compressibility factor* $Z = pV_{\mathrm{m}}/(RT)$, which is $1$ for an ideal gas. The deviations have two sources: the molecules have a volume of their own, and at high pressure the incompressible part of the volume cannot be neglected, giving $Z > 1$; and the molecules attract one another, so molecules striking the wall are pulled back by those inside and the observed pressure is smaller, giving $Z < 1$. van der Waals corrected for both with two parameters, obtaining the **van der Waals equation** (derivation in [5.2.2](/5.2.2#sec-2.2.3)):

$$
\left(p + \frac{an^2}{V^2}\right)(V - nb) = nRT,
$$
where $a$ is related to the attraction between molecules and $b$ to the volume of the molecules themselves (about four times the intrinsic volume of $1\,\mathrm{mol}$ of molecules); both are determined experimentally. The larger and more polar the molecules, the larger $a$: for $\ce{He}$, $a = 0.00346\,\mathrm{Pa\,m^6\,mol^{-2}}$, for $\ce{N2}$ it is $0.137$ and for $\ce{H2O}$ it is $0.554$.

**Example 1.1.7** Calculate the pressure of $1.50\,\mathrm{mol}$ of $\ce{SO2}$ occupying $20.0\,\mathrm{L}$ at $30\,{}^\circ\mathrm{C}$ using the ideal gas equation and the van der Waals equation, and find the relative deviation; what happens when the volume is compressed to $2.00\,\mathrm{L}$? (For $\ce{SO2}$, $a = 0.6865\,\mathrm{Pa\,m^6\,mol^{-2}} = 686.5\,\mathrm{kPa\,L^2\,mol^{-2}}$ and $b = 0.05679\,\mathrm{L\,mol^{-1}}$.)

Solution: $nRT = 1.50 \times 8.314 \times 303.15\,\mathrm{J} = 3781\,\mathrm{J}$. At $V = 20.0\,\mathrm{L}$ the ideal gas gives $p_1 = 3781/20.0 = 189\,\mathrm{kPa}$; the van der Waals equation gives

$$
p_2 = \frac{nRT}{V - nb} - \frac{an^2}{V^2} = \frac{3781}{20.0 - 0.0852} - \frac{686.5 \times 1.50^2}{20.0^2} = 189.8 - 3.9 = 186\,\mathrm{kPa},
$$
and the relative deviation is $(p_1 - p_2)/p_2 = 1.6\%$. At $V = 2.00\,\mathrm{L}$, $p_1 = 1.89 \times 10^3\,\mathrm{kPa}$ and $p_2 = 1974 - 386 = 1.59 \times 10^3\,\mathrm{kPa}$, so the relative deviation grows to $19\%$: the denser the gas, the more important the attraction correction.

Lowering the temperature weakens thermal motion and raising the pressure brings the molecules closer together, and both favor condensation of the gas to a liquid by intermolecular attraction. Above a certain temperature, however, no pressure, however large, can liquefy the gas; this temperature is the **critical temperature** $T_{\mathrm{c}}$ (the temperature of the **critical point**, [5.2.2](/5.2.2#sec-2.1)).

**Definition 1.1.3** The lowest pressure needed to liquefy a gas at the critical temperature is called the **critical pressure** $p_{\mathrm{c}}$; the volume occupied by $1\,\mathrm{mol}$ of the substance at the critical temperature and critical pressure is called the **critical volume** $V_{\mathrm{m,c}}$ (critical molar volume).

| Substance | $T_{\mathrm{c}}/\mathrm{K}$ | $p_{\mathrm{c}}/\mathrm{MPa}$ | Substance | $T_{\mathrm{c}}/\mathrm{K}$ | $p_{\mathrm{c}}/\mathrm{MPa}$ |
|---|---|---|---|---|---|
| $\ce{He}$ | 5.20 | 0.227 | $\ce{CH4}$ | 190.6 | 4.60 |
| $\ce{H2}$ | 33.1 | 1.30 | $\ce{CO2}$ | 304.1 | 7.38 |
| $\ce{N2}$ | 126.2 | 3.40 | $\ce{NH3}$ | 405.4 | 11.3 |
| $\ce{O2}$ | 154.6 | 5.04 | $\ce{H2O}$ | 647.1 | 22.06 |

The stronger the intermolecular attraction, the higher the critical temperature. The critical temperatures of $\ce{NH3}$ and $\ce{CO2}$ are above room temperature, so they can be liquefied by compression at room temperature (liquid ammonia and liquid $\ce{CO2}$ in cylinders); $\ce{N2}$ and $\ce{O2}$ must first be cooled below their critical temperatures before they can be liquefied, which is the basis of air separation. The critical volume of $\ce{CO2}$ is about $94\,\mathrm{cm^3\,mol^{-1}}$.

The relations among the gas, liquid and solid states can be drawn in one diagram:

**Definition 1.1.4 (Phase Diagram)** A diagram with temperature and pressure as coordinates that shows which phase of a pure substance is stable under each set of conditions and which phases can coexist in equilibrium is called the **phase diagram** of the substance. The lines in the diagram are two-phase equilibrium lines (the liquid–gas line is the saturated vapor pressure curve, the solid–gas line is the sublimation curve and the solid–liquid line is the melting curve), and the three lines meet at one point at which the solid, liquid and gas phases coexist in equilibrium at a particular temperature and pressure, called the **triple point**.

![Phase diagram of CO2 (schematic; logarithmic pressure axis). At 101.325 kPa solid CO2 sublimes at 194.7 K instead of melting, because the triple-point pressure (518 kPa) is higher than atmospheric pressure](./plots/co2-phase-diagram.py)

The triple point of $\ce{CO2}$ is at $216.6\,\mathrm{K}$ and $518\,\mathrm{kPa}$, above atmospheric pressure, so at ordinary pressure solid $\ce{CO2}$ (dry ice) does not melt but sublimes directly at $194.7\,\mathrm{K}$ ($-78.5\,{}^\circ\mathrm{C}$) and can be used as a refrigerant. The triple point of water is at $273.16\,\mathrm{K}$ and $611.7\,\mathrm{Pa}$, and at ordinary pressure ice melts first; the melting curve of water has a negative slope (ice is less dense than water, and pressure makes ice melt), whereas that of $\ce{CO2}$, like that of most substances, has a positive slope. The liquid–gas line ends at the critical point ($\ce{CO2}$: $304.1\,\mathrm{K}$, $7.38\,\mathrm{MPa}$), beyond which there is no distinction between liquid and gas.

**Definition 1.1.5** A state whose temperature and pressure are respectively above the critical temperature and the critical pressure is called a **supercritical fluid**.

The density of a supercritical fluid is close to that of a liquid, so it has liquid-like solvent power; its viscosity and diffusion coefficient are close to those of a gas, so it penetrates well; and near the critical point a small change in temperature or pressure changes the density and solvent power greatly. Supercritical $\ce{CO2}$ is nontoxic, nonflammable and has mild critical conditions; it is used to extract caffeine from coffee beans and flavors and pharmaceutical components from plants (supercritical extraction), and on depressurization the $\ce{CO2}$ becomes a gas so that solute and solvent separate automatically and no solvent residue remains. The general theory of phase diagrams (the Gibbs phase rule, two-component systems) belongs to [6.3](/6.3).

## 1.2. Liquids

In a liquid the molecules are in contact and the intermolecular forces are much greater than in a gas: a liquid has a definite volume but no fixed shape, is hard to compress, and its volume is hardly affected by temperature and pressure; the molecules can move relative to one another, so a liquid can flow, has **viscosity** and surface tension, and different liquids can diffuse slowly into one another. The theory of liquids is harder than that of gases and of crystals, and this section discusses only the transitions to the gas and solid phases.

### 1.2.1. Evaporation and Saturated Vapor Pressure

Molecules at the surface of a liquid that have sufficient kinetic energy can overcome the attraction of the surrounding molecules and escape from the surface; this is evaporation. The fraction of molecules with high enough energy is very small and is dominated by the Boltzmann factor $\mathrm{e}^{-E_0/(RT)}$ (Section 1.1.3), so evaporation speeds up rapidly as the temperature rises; evaporation removes high-energy molecules, so the mean kinetic energy of the remaining liquid decreases and the liquid cools (the principle of cooling by sweating).

In a closed container the molecules that have evaporated also strike the surface and condense. Evaporation and condensation proceed simultaneously and independently, and when their rates are equal the system reaches dynamic equilibrium (phase equilibrium); the vapor is then called saturated vapor, and its pressure is the **saturated vapor pressure** of the liquid at that temperature (vapor pressure for short, [5.2.2](/5.2.2#sec-2.1)). At a given temperature the saturated vapor pressure is a characteristic constant of the liquid, independent of the amount of liquid and of the volume occupied by the vapor: compressing the vapor only makes more of it condense, and the pressure stays the same. The weaker the intermolecular attraction, the more volatile the liquid and the higher its vapor pressure at the same temperature (at $25\,{}^\circ\mathrm{C}$: diethyl ether $71.7\,\mathrm{kPa}$, ethanol $7.9\,\mathrm{kPa}$, water $3.17\,\mathrm{kPa}$).

### 1.2.2. The Clausius–Clapeyron Equation

Evaporation absorbs heat, and the quantity that measures this heat is:

**Definition 1.2.1** The heat absorbed when $1\,\mathrm{mol}$ of liquid evaporates to vapor at the same temperature and pressure, at a given temperature and the corresponding saturated vapor pressure (equal to the molar enthalpy change of this process), is called the **molar enthalpy of vaporization** (heat of vaporization), written $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$.

The heat absorbed at constant pressure equals the increase in the **enthalpy** of the system ([5.2.3](/5.2.3#sec-3.5.5)), so the enthalpy of vaporization can be measured directly by calorimetry. For water $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ is $44.0\,\mathrm{kJ\,mol^{-1}}$ at $25\,{}^\circ\mathrm{C}$ and $40.7\,\mathrm{kJ\,mol^{-1}}$ at $100\,{}^\circ\mathrm{C}$: the higher the temperature, the more alike liquid and vapor become and the smaller the enthalpy of vaporization, which is zero at the critical point. The quantitative dependence of vapor pressure on temperature follows from the condition for two-phase equilibrium. Here we make advance use of the **Gibbs energy** $G = H - TS$ and its properties, which are introduced formally only in [6.1.6](/6.1.6): at constant temperature and pressure, the condition for two phases of a pure substance to coexist in equilibrium is that their molar Gibbs energies are equal, $G_{\mathrm{m}}(\mathrm{l}) = G_{\mathrm{m}}(\mathrm{g})$ (a rigorous argument requires the chemical potential and belongs to [6.3](/6.3)).

**Theorem 1.2.1 (Clapeyron Equation)** When two phases $\alpha$ and $\beta$ of a pure substance coexist in equilibrium, the rate of change of the equilibrium pressure with temperature is

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta H_{\mathrm{m}}}{T\,\Delta V_{\mathrm{m}}},
$$
where $\Delta H_{\mathrm{m}}$ and $\Delta V_{\mathrm{m}}$ are the enthalpy change and volume change when $1\,\mathrm{mol}$ of the substance passes from phase $\alpha$ to phase $\beta$.

**Proof** From $G = U + pV - TS$ and $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ for a reversible process (the **first law of thermodynamics** together with $\delta Q_{\mathrm{rev}} = T\,\mathrm{d}S$, [5.2.4](/5.2.4)) we obtain $\mathrm{d}G_{\mathrm{m}} = -S_{\mathrm{m}}\,\mathrm{d}T + V_{\mathrm{m}}\,\mathrm{d}p$. Along the two-phase equilibrium line the $G_{\mathrm{m}}$ of the two phases are always equal, so their changes are equal as well:

$$
-S_{\mathrm{m}}^{\alpha}\,\mathrm{d}T + V_{\mathrm{m}}^{\alpha}\,\mathrm{d}p = -S_{\mathrm{m}}^{\beta}\,\mathrm{d}T + V_{\mathrm{m}}^{\beta}\,\mathrm{d}p \quad\Longrightarrow\quad \frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta S_{\mathrm{m}}}{\Delta V_{\mathrm{m}}}.
$$
The phase transition proceeds reversibly at constant temperature and pressure, so the heat absorbed equals the enthalpy change, $\Delta S_{\mathrm{m}} = \Delta H_{\mathrm{m}}/T$, and substitution gives the result. $\square$

The Clapeyron equation holds for vaporization, sublimation and melting. For melting $\Delta V_{\mathrm{m}}$ is very small and $\mathrm{d}p/\mathrm{d}T$ is very large, so the melting curve is almost vertical; when water freezes its volume increases, $\Delta_{\mathrm{fus}}V_{\mathrm{m}} < 0$, so the melting curve of water has a negative slope (in the phase diagram the melting point of ice decreases as pressure increases). For vaporization and sublimation it can be simplified further:

**Theorem 1.2.2 (Clausius–Clapeyron Equation)** Suppose the vapor can be treated as an ideal gas and the molar volume of the liquid (or solid) is negligible compared with that of the vapor. Then

$$
\frac{\mathrm{d}\ln p}{\mathrm{d}T} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{RT^2};
$$
and if $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ can be regarded as constant over the temperature range considered,

$$
\ln p = -\frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{R}\cdot\frac{1}{T} + C, \qquad \ln\frac{p_2}{p_1} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right).
\tag{1.1}
$$

**Proof** $\Delta V_{\mathrm{m}} = V_{\mathrm{m}}(\mathrm{g}) - V_{\mathrm{m}}(\mathrm{l}) \approx V_{\mathrm{m}}(\mathrm{g}) = RT/p$, and substitution into the Clapeyron equation gives $\dfrac{1}{p}\dfrac{\mathrm{d}p}{\mathrm{d}T} = \dfrac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{RT^2}$. This is a separable first-order differential equation ([2.4](/2.4)); when $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ is constant, integrating both sides gives Eq. (1.1). $\square$

Equation (1.1) shows that $\ln p$ is linear in $1/T$ with slope $-\Delta_{\mathrm{vap}}H_{\mathrm{m}}/R$: measuring the vapor pressure at several temperatures and plotting (or performing a linear regression) gives the enthalpy of vaporization. Textbooks often write it with common logarithms, $\lg p = -\dfrac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{2.303R}\cdot\dfrac{1}{T} + B$ ($2.303 = \ln 10$). The actual $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ decreases slowly with temperature, and accurate vapor pressure data are often fitted by the empirical Antoine equation $\lg p = A - \frac{B}{T + C}$, which over a not-too-wide temperature range is almost indistinguishable from the straight line. Replacing $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ by the molar enthalpy of sublimation $\Delta_{\mathrm{sub}}H_{\mathrm{m}}$, the same formula describes the vapor pressure of a solid (the sublimation curve in the phase diagram).

![ln(p/kPa) against 1000 K/T for water, ethanol and benzene, computed from Antoine equations. The lines are nearly straight with slope −ΔvapHm/R; the dashed line p = 101.325 kPa crosses them at the normal boiling points](./plots/vapor-pressure.py)

**Example 1.2.1** The normal boiling point of phenol is $455.1\,\mathrm{K}$ and $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 48.14\,\mathrm{kJ\,mol^{-1}}$. At what temperature does phenol boil when the external pressure is reduced to $13.33\,\mathrm{kPa}$?

Solution: Assume $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ is constant over this temperature range. From Eq. (1.1),

$$
\frac{1}{T_2} = \frac{1}{T_1} - \frac{R}{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}\ln\frac{p_2}{p_1} = \frac{1}{455.1\,\mathrm{K}} - \frac{8.314}{48140}\ln\frac{13.33}{101.325}\,\mathrm{K^{-1}} = 2.548 \times 10^{-3}\,\mathrm{K^{-1}},
$$
so $T_2 = 392\,\mathrm{K}$. Vacuum distillation makes use of exactly this, distilling substances that have high boiling points or decompose on heating at lower temperatures.

**Example 1.2.2** The vapor pressures of water at $25\,{}^\circ\mathrm{C}$ and $100\,{}^\circ\mathrm{C}$ are $3.17\,\mathrm{kPa}$ and $101.325\,\mathrm{kPa}$ respectively; estimate the molar enthalpy of vaporization of water from them.

Solution: $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = \dfrac{R\ln(p_2/p_1)}{1/T_1 - 1/T_2} = \dfrac{8.314 \times \ln 31.96}{1/298.15 - 1/373.15}\,\mathrm{J\,mol^{-1}} = 42.7\,\mathrm{kJ\,mol^{-1}}$, which lies between the actual values $44.0$ and $40.7\,\mathrm{kJ\,mol^{-1}}$ at the two end temperatures and is the average over this temperature interval.

For many nonpolar liquids the molar entropy of vaporization at the normal boiling point, $\Delta_{\mathrm{vap}}H_{\mathrm{m}}/T_{\mathrm{b}}$, is close to $85$–$88\,\mathrm{J\,mol^{-1}\,K^{-1}}$; this empirical rule is called *Trouton's rule*, for example benzene $30.7\,\mathrm{kJ\,mol^{-1}}/353.2\,\mathrm{K} = 87\,\mathrm{J\,mol^{-1}\,K^{-1}}$; water ($109$) and ethanol ($110$) are clearly larger because hydrogen bonds in the liquid ([6.1.4](/6.1.4)) make the liquid state more ordered.

### 1.2.3. Boiling and Freezing

When a liquid is heated its vapor pressure rises with temperature; when the vapor pressure grows to equal the external pressure, bubbles can also form inside the liquid and vaporization proceeds violently throughout the liquid; this is boiling.

**Definition 1.2.2** The temperature at which the saturated vapor pressure of a liquid equals the external pressure is called the **boiling point** of the liquid at that pressure; the boiling point at an external pressure of $101.325\,\mathrm{kPa}$ is called the **normal boiling point**.

The normal boiling point of water is $99.97\,{}^\circ\mathrm{C}$ (usually written $100\,{}^\circ\mathrm{C}$); the standard boiling point recommended by IUPAC uses an external pressure of $100\,\mathrm{kPa}$, and for water it is $99.61\,{}^\circ\mathrm{C}$. The boiling point varies with the external pressure: at high altitudes the air pressure is low and the boiling point of water is below $100\,{}^\circ\mathrm{C}$; a pressure cooker raises the pressure inside and hence the boiling point; vacuum distillation lowers the boiling point (Example 1.2.1). If heating continues during boiling, all the heat absorbed by the liquid goes into vaporization and the temperature stays at the boiling point.

The formation of bubbles requires "nucleation sites" (tiny bubbles on the wall, impurities). A pure liquid heated in a smooth container can exceed its boiling point without boiling, which is called superheating; once a bubble forms in a superheated liquid, it boils suddenly and violently (bumping). Adding boiling chips (porous ceramic pieces) in laboratory distillation or reflux provides nucleation sites and prevents bumping.

When a liquid is cooled, crystals begin to form at the freezing point (the melting point at the same pressure); freezing releases heat and the temperature stays constant until all the liquid has solidified. The growth of crystals also requires "crystallization centers":

**Definition 1.2.3** The phenomenon in which a liquid is cooled below its freezing point without solidifying is called **supercooling**, and such a liquid is called a supercooled liquid.

The purer the liquid and the more smoothly it is cooled, the more easily it supercools: tiny water droplets can be supercooled to about $-40\,{}^\circ\mathrm{C}$, and supercooled water droplets are abundant in high-altitude clouds, which is why cloud seeding for artificial rain scatters seed crystals such as silver iodide into them. Superheated and supercooled liquids are both metastable: they can persist for some time if undisturbed, and once a bubble or seed crystal is introduced they change rapidly to the stable state and release (supercooled) or absorb (superheated) the corresponding latent heat.

### 1.2.4. Liquid Crystals

In 1888 the Austrian botanist Reinitzer found that cholesteryl benzoate ($\ce{C6H5CO2C27H45}$) melts at $145.5\,{}^\circ\mathrm{C}$ to a cloudy liquid and becomes a clear liquid only at $178.5\,{}^\circ\mathrm{C}$; Lehmann then found that the optical properties of the cloudy liquid are anisotropic, like those of a crystal.

**Definition 1.2.4** Some substances under certain conditions are in a state intermediate between a crystal and a liquid: they flow like a liquid, yet the orientation of the molecules (and sometimes also their positions) retains a degree of long-range order, and optical, electrical and other properties are anisotropic. This state is called the **liquid crystal** state.

Liquid crystal phases exist between the melting point and the clearing point: at the melting point the solid changes into a cloudy liquid crystal, and at the clearing point the liquid crystal changes into a transparent isotropic liquid. By the way they form, liquid crystals are divided into thermotropic ones (formed by a pure substance in a certain temperature range) and lyotropic ones (formed by amphiphilic molecules dissolved in a solvent in a certain concentration range, such as soap solutions and the lipid bilayers of cell membranes). Thermotropic liquid crystals fall into three classes by the degree of order in the arrangement of the molecules:

| Type | Molecular arrangement | Features and uses |
|---|---|---|
| *nematic phase* | Long axes roughly parallel, positions disordered | Low viscosity and rapid response to electric fields; the main material of liquid crystal displays |
| *smectic phase* | Long axes parallel, arranged in layers, positions within layers disordered | Highest degree of order, close to a crystal |
| *cholesteric phase* | Molecules parallel within each layer, with the orientation rotating from layer to layer into a helix | The pitch is comparable to the wavelength of visible light and the color changes with temperature; used in temperature-sensing materials |

Molecules that form liquid crystals are mostly rod-shaped, with a rigid core of benzene rings and similar groups in the middle and polar groups or flexible alkyl chains at one or both ends. 4-Cyano-4'-pentylbiphenyl (5CB), commonly used in displays, is nematic between $22.5$ and $35\,{}^\circ\mathrm{C}$:

```smiles
CCCCCc1ccc(cc1)-c1ccc(cc1)C#N 5CB
```

The dielectric constant of liquid crystal molecules is anisotropic, and an applied electric field can change the orientation of the molecules and thereby the effect of the liquid crystal layer on polarized light (for polarized light see [5.4.3](/5.4.3)): a layer of liquid crystal sandwiched between two polarizers lets a voltage control the brightness of each pixel, which is the principle of the liquid crystal display.

## 1.3. Solids

Solids fall into two broad classes, crystals and amorphous solids.

### 1.3.1. Crystals and Amorphous Solids

A **crystal** is a solid in which atoms, ions or molecules are arranged periodically and repeatedly in space according to a definite rule ([5.5.6](/5.5.6#sec-6.1.1)), whereas in an **amorphous solid** the particles have no long-range periodic arrangement. A solid made of a single crystal throughout is called a *single crystal*, such as quartz and single-crystal silicon; one made of many tiny grains of different orientations is called a *polycrystal*, and metals and ceramics are usually polycrystalline.

Crystals were first understood as "solids with the shape of a regular polyhedron". In 1690 Huygens conjectured that the external shape of a crystal comes from an ordered arrangement of its particles; at the end of the 18th century Haüy proposed that a crystal is built by stacking many identical small parallelepipeds without gaps; in the 19th century Bravais and others developed the lattice theory; and the discovery of X-ray diffraction in 1912 directly confirmed the periodic internal structure of crystals. As a result of the periodic arrangement, crystals have the following common characteristics:

1. Regular geometric shape. Under suitable conditions a crystal spontaneously grows into a polyhedron bounded by crystal faces. The shape and size of crystals of one substance vary with growth conditions, but the angles between corresponding faces remain constant; this is the *law of constancy of interfacial angles*, proposed by Steno in 1669.
2. A fixed melting point. On heating to the melting point the periodic structure collapses as a whole and the crystal melts at constant temperature; an amorphous solid softens gradually over a range of temperature.
3. Anisotropy. The particles are arranged differently along different directions in a crystal, so thermal conductivity, electrical conductivity, optical properties and mechanical strength vary with direction: the electrical conductivity of graphite along the layers is thousands of times that perpendicular to them, and mica cleaves very easily along its cleavage planes. Amorphous solids are isotropic.
4. X-ray diffraction. The spacing of particles in a crystal (about $0.1\,\mathrm{nm}$) is comparable to the wavelength of X-rays, so a crystal is a natural three-dimensional diffraction grating and produces diffraction patterns such as **Laue spots**; the diffraction directions are determined by the spacings of the **families of lattice planes** (the Bragg equation, [5.4.2](/5.4.2#sec-2.5)). This is the main method of determining crystal structures.

### 1.3.2. Lattices and Unit Cells

Take the NaCl crystal as an example: $\ce{Na+}$ and $\ce{Cl-}$ alternate and repeat periodically without end along three mutually perpendicular directions. To describe this periodicity we must separate "what is repeated" from "how it is repeated".

**Definition 1.3.1** The smallest group of particles (atoms, ions, molecules or groups of atoms) that repeats periodically in a crystal, such that translating it repeatedly generates the whole crystal, is called the **structural motif**. Abstracting each motif to a geometric point (the corresponding position in each motif), the arrangement of these points in space is called the **crystal lattice** (space lattice), and its points are called lattice points.

The surroundings of every lattice point are identical, and translation of the lattice along any vector joining two lattice points brings it into coincidence with itself. A crystal structure is thus a lattice plus a structural motif: placing one motif at each lattice point reconstructs the crystal structure. The motif of NaCl is one $\ce{Na+}$ plus one $\ce{Cl-}$ (not a single ion, since the positions of $\ce{Na+}$ and $\ce{Cl-}$ cannot be interchanged by translation). The lattice is a mathematical abstraction of periodicity, corresponding to translational symmetry in group theory; it is not the same as "the positions of the atoms", and lattice points can coincide with atoms only in simple metals in which each motif contains a single atom.

A lattice can be generated by three non-coplanar basis translation vectors $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$, with lattice points at $u\boldsymbol{a} + v\boldsymbol{b} + w\boldsymbol{c}$ ($u, v, w$ integers). Parallelepipeds with edges $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ stacked without gaps fill the whole lattice.

**Definition 1.3.2** A parallelepiped chosen from the lattice by the rules below, together with the motif it contains, is called a **unit cell** of the crystal; its three edge lengths $a, b, c$ and three angles $\alpha$ (between $\boldsymbol{b}$ and $\boldsymbol{c}$), $\beta$ (between $\boldsymbol{c}$ and $\boldsymbol{a}$) and $\gamma$ (between $\boldsymbol{a}$ and $\boldsymbol{b}$) are called the **lattice parameters**, which determine the size and shape of the cell.

A lattice admits infinitely many choices of parallelepiped. Bravais's rules for the choice are, in order of priority:

1. the symmetry of the parallelepiped is the same as the symmetry of the whole lattice;
2. subject to this, the number of right angles between edges is as large as possible;
3. subject to this, the volume is as small as possible.

A cell with lattice points only at the corners is called a *primitive cell*, written P; each primitive cell contains exactly one lattice point. To satisfy rule 1 it is sometimes necessary to choose a non-primitive cell that also has lattice points at the body center, face centers or base centers. When counting the particles actually contained in a unit cell, each is apportioned according to its position: a particle at a corner is shared by 8 cells and counts as $\frac{1}{8}$; one on an edge counts as $\frac{1}{4}$; one on a face counts as $\frac{1}{2}$; one inside the cell counts as 1. For example, in the cubic unit cell of NaCl, $\ce{Cl-}$ lies at the 8 corners and 6 face centers, giving $8 \times \frac{1}{8} + 6 \times \frac{1}{2} = 4$; $\ce{Na+}$ lies at the midpoints of the 12 edges and the body center, giving $12 \times \frac{1}{4} + 1 = 4$.

### 1.3.3. The Seven Crystal Systems and 14 Bravais Lattices

Crystals are classified by symmetry. The shape of the unit cell is determined by the symmetry: for example, a crystal with four threefold axes must have a cubic cell.

**Definition 1.3.3** According to the characteristic symmetry elements a crystal possesses, crystals are divided into 7 classes, called the 7 **crystal systems**; the lattice parameters of each crystal system satisfy certain restrictions:

| Crystal system | Lattice parameters | Characteristic symmetry elements | Examples |
|---|---|---|---|
| Cubic | $a = b = c$, $\alpha = \beta = \gamma = 90^\circ$ | Four threefold axes | Cu, NaCl |
| Tetragonal | $a = b \ne c$, $\alpha = \beta = \gamma = 90^\circ$ | One fourfold axis | White tin (Sn), rutile $\ce{TiO2}$ |
| Orthorhombic | $a \ne b \ne c$, $\alpha = \beta = \gamma = 90^\circ$ | Three mutually perpendicular twofold axes or two mutually perpendicular mirror planes | $\ce{I2}$, $\ce{BaCO3}$ |
| Trigonal | $a = b = c$, $\alpha = \beta = \gamma \ne 90^\circ$ (rhombohedral cell) | One threefold axis | As, $\ce{Al2O3}$, $\alpha$-quartz |
| Hexagonal | $a = b \ne c$, $\alpha = \beta = 90^\circ$, $\gamma = 120^\circ$ | One sixfold axis | Mg, CuS |
| Monoclinic | $a \ne b \ne c$, $\alpha = \gamma = 90^\circ \ne \beta$ | One twofold axis or one mirror plane | $\ce{KClO3}$ |
| Triclinic | $a \ne b \ne c$, $\alpha \ne \beta \ne \gamma$ | None (or only a center of symmetry) | $\ce{K2Cr2O7}$ |

The "$\ne$" in the table means "not restricted by symmetry, generally unequal". The crystal system is defined by symmetry and the relations among lattice parameters are its consequence, so the converse does not necessarily hold (for example, an orthorhombic crystal with $a = b$ by accident is still orthorhombic). Trigonal crystals are also often described by a hexagonal cell.

In each crystal system, besides the primitive cell, some also admit centered non-primitive cells without destroying the symmetry of the system:

**Definition 1.3.4** Distinguished by crystal system and centering type (primitive P, body-centered I, face-centered F, base-centered C, rhombohedral R), there are 14 different lattices in three-dimensional space, called the 14 **Bravais lattices**.

| Crystal system | Bravais lattices |
|---|---|
| Cubic | Primitive cubic cP, body-centered cubic cI, face-centered cubic cF |
| Tetragonal | Primitive tetragonal tP, body-centered tetragonal tI |
| Orthorhombic | Primitive orthorhombic oP, base-centered orthorhombic oC, body-centered orthorhombic oI, face-centered orthorhombic oF |
| Hexagonal | Primitive hexagonal hP |
| Trigonal | Rhombohedral hR |
| Monoclinic | Primitive monoclinic mP, base-centered monoclinic mC |
| Triclinic | Primitive triclinic aP |

![The 14 Bravais lattices (conventional cells); lattice points at the corners are shown in grey, centring points in colour](./plots/bravais-lattices.py)

Not every combination of the 7 crystal systems with the 4 centering types gives a new lattice. For example, "base-centered tetragonal" can be re-described by a primitive tetragonal cell of half the volume, identical to tP; "base-centered cubic" destroys the four threefold axes and is not a cubic lattice. Frankenheim (1842) listed 15 lattices, and Bravais (1848) proved that two of them are the same, leaving 14.

**Example 1.3.1** The lattices and structural motifs of several AB-type and $\mathrm{AB_2}$-type ionic crystals:

| Crystal | Bravais lattice | Structural motif | Ions per unit cell |
|---|---|---|---|
| NaCl | Face-centered cubic | 1 $\ce{Na+}$ + 1 $\ce{Cl-}$ | 4 $\ce{Na+}$, 4 $\ce{Cl-}$ |
| CsCl | Primitive cubic | 1 $\ce{Cs+}$ + 1 $\ce{Cl-}$ | 1 $\ce{Cs+}$, 1 $\ce{Cl-}$ |
| Cubic ZnS | Face-centered cubic | 1 $\ce{Zn^2+}$ + 1 $\ce{S^2-}$ | 4 $\ce{Zn^2+}$, 4 $\ce{S^2-}$ |
| $\ce{CaF2}$ | Face-centered cubic | 1 $\ce{Ca^2+}$ + 2 $\ce{F-}$ | 4 $\ce{Ca^2+}$, 8 $\ce{F-}$ |

In the CsCl cell $\ce{Cs+}$ is at the body center and $\ce{Cl-}$ at the corners, which looks like a body-centered cubic cell, but the ions at the body center and at the corners differ and cannot be brought into coincidence by translation, so its lattice is primitive cubic. The geometry and coordination of these structures are discussed in detail in [6.1.4](/6.1.4); point groups, space groups, Miller indices and the quantitative treatment of diffraction belong to [6.2](/6.2).

### 1.3.4. Amorphous Solids

An amorphous solid has no regular external shape, and the arrangement of its particles follows a rule only within a few atoms (short-range order) and has no periodicity over larger distances (long-range disorder); structurally it resembles a "frozen liquid". Take $\ce{SiO2}$ as an example: in both quartz crystal and quartz glass each Si is bonded to 4 O atoms forming a tetrahedron and each O links two Si, so the short-range structure is the same; but in the quartz crystal these tetrahedra are linked periodically, whereas in quartz glass they form a random network. An amorphous solid therefore has no fixed melting point but softens gradually over a range of temperature (the glass transition); it is isotropic, and its X-ray diffraction gives only diffuse rings without sharp diffraction spots.

The amorphous state is usually metastable thermodynamically and crystallizes slowly on prolonged heating (the "devitrification" of glass). Amorphous materials have various uses: quartz glass has a small coefficient of expansion, is heat resistant and transmits ultraviolet light; amorphous silicon is used in thin-film solar cells; metallic glasses (amorphous alloys) are obtained by rapid quenching of a melt, have no grain boundaries, and show high strength, corrosion resistance and low magnetic losses.

## Summary

| Topic | Key points |
|---|---|
| Ideal gas | $pV = nRT$; $M = mRT/(pV)$, $\rho = pM/(RT)$ |
| Gas mixtures | $x_{\mathrm{B}} = n_{\mathrm{B}}/n$, $p_{\mathrm{B}} = x_{\mathrm{B}}p = n_{\mathrm{B}}RT/V$, $p = \sum p_{\mathrm{B}}$ |
| Energy distribution | The fraction of molecules with energy not below $E_0$ is dominated by $\mathrm{e}^{-E_0/(RT)}$ |
| Effusion | $r_{\mathrm{A}}/r_{\mathrm{B}} = \sqrt{M_{\mathrm{B}}/M_{\mathrm{A}}}$ |
| Real gases | van der Waals equation; critical temperature, critical pressure, critical volume; phase diagram, triple point, supercritical fluid |
| Vapor pressure | $\ln(p_2/p_1) = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$; a liquid boils when its vapor pressure equals the external pressure |
| Crystals | Crystal structure = lattice + structural motif; lattice parameters $a, b, c, \alpha, \beta, \gamma$; 7 crystal systems, 14 Bravais lattices |
