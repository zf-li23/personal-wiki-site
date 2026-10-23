---
title: Ideal Liquid Mixtures and Ideal Dilute Solutions
source_hash: d9af9c340230
---

[6.3.4](/6.3.4) established the language of multicomponent systems, namely **partial molar quantities**, the **chemical potential** and the **fugacity**, and gave expressions for the chemical potentials of gases (ideal and real). This chapter applies that language to the liquid phase. The chemical potential of a liquid cannot be measured directly, but when a liquid is in equilibrium with its vapor the chemical potential of each substance is the same in the two phases, so the chemical potential in the liquid can be expressed through the gas phase, and the problem reduces to how the partial pressure of the vapor above a solution varies with composition. Two empirical laws hold in dilute solutions: the solvent obeys Raoult's law, and a volatile solute obeys Henry's law. On this basis we define two idealized kinds of solution, the ideal liquid mixture (5.1) and the ideal dilute solution (5.2), write down the chemical potentials of the components, and from them derive rigorously the colligative properties of dilute solutions (5.3): vapor-pressure lowering, freezing-point depression, boiling-point elevation and osmotic pressure. These results are the starting point for real solutions: [6.3.6](/6.3.6) uses activities to correct for deviations from ideal behavior, [6.3.7](/6.3.7) derives equilibrium constants in solution from chemical potentials, and [6.3.9](/6.3.9) draws binary phase diagrams from Raoult's law; osmotic pressure is also the physical basis of the regulation of water in cells and body fluids.

In this chapter A denotes the solvent and B the solute (or any component of a mixture); the superscript $*$ denotes a pure substance and the superscript $^\circ$ the standard state (**standard pressure** $p^\circ = 10^5\,\mathrm{Pa}$).

## 5.1. Raoult's Law and Ideal Liquid Mixtures

### 5.1.1. Raoult's Law

The **saturated vapor pressure** $p^*_{\mathrm{A}}$ of a pure liquid depends mainly on temperature. When another substance is dissolved in it, the partial pressure of the solvent vapor falls. In 1887 Raoult summarized a large body of data on dilute solutions and obtained *Raoult's law*: at a given temperature, the partial pressure of the solvent vapor over a dilute solution equals the saturated vapor pressure of the pure solvent at the same temperature multiplied by the **mole fraction** of solvent in the solution,

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}. \tag{5.1}
$$

Remarks:

1. For any solution Eq. (5.1) holds strictly as $x_{\mathrm{A}} \to 1$; it is a limiting law, more accurate the more dilute the solution.
2. In computing $x_{\mathrm{A}}$ the molar mass of the solvent is taken as that of its gaseous molecules (for water $18.015\,\mathrm{g\,mol^{-1}}$, even though hydrogen bonds associate molecules in liquid water).
3. The solute may be volatile or nonvolatile; but if the solute dissociates or associates in solution, $x_{\mathrm{A}}$ must be computed from the particles actually present (for electrolyte solutions see [6.3.12](/6.3.12)).
4. Strictly, $p^*_{\mathrm{A}}$ is the saturated vapor pressure of the pure solvent at the same temperature and pressure as the solution; the effect of external pressure on vapor pressure is small ([6.3.8](/6.3.8)) and usually need not be distinguished.

### 5.1.2. Ideal Liquid Mixtures

Experiment shows that in mixtures of liquids of similar structure and properties, each component obeys or nearly obeys Raoult's law over the entire concentration range: water–heavy water (isotopic compounds), d-camphor–l-camphor (optical isomers), o-, m- and p-xylene (structural isomers), benzene–toluene, methanol–ethanol (adjacent homologs). What they have in common is that the interactions among A–A, B–B and A–B molecules are almost the same and the molecules are similar in size: replacing the molecules around a molecule by molecules of the other kind does not change the energy and only increases the number of ways of arranging them.

**Definition 5.1.1 (Ideal Liquid Mixture)** A liquid mixture in which each component obeys Raoult's law over the entire concentration range is called an **ideal liquid mixture** (also called an ideal solution).

For a binary ideal liquid mixture,

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = p^*_{\mathrm{B}}x_{\mathrm{B}}, \qquad p = p_{\mathrm{A}} + p_{\mathrm{B}} = p^*_{\mathrm{A}} + (p^*_{\mathrm{B}} - p^*_{\mathrm{A}})x_{\mathrm{B}}.
$$
The total pressure is a linear function of the liquid-phase composition. If the vapor is an **ideal gas**, by **Dalton's law of partial pressures** the gas-phase composition is

$$
y_{\mathrm{B}} = \frac{p_{\mathrm{B}}}{p} = \frac{p^*_{\mathrm{B}}x_{\mathrm{B}}}{p}, \qquad \frac{y_{\mathrm{B}}}{x_{\mathrm{B}}} = \frac{p^*_{\mathrm{B}}}{p}.
$$
If $p^*_{\mathrm{B}} > p^*_{\mathrm{A}}$ (B more volatile), then $p^*_{\mathrm{B}} > p$ and $y_{\mathrm{B}} > x_{\mathrm{B}}$: the more volatile component is present in the gas phase at a higher proportion than in the liquid phase. This is the basis of distillation and **fractional distillation** ([6.3.9](/6.3.9)).

![Vapor–liquid equilibrium of an ideal liquid mixture (p*_A = 40 kPa, p*_B = 120 kPa): left, partial and total pressures as straight lines against liquid composition; right, the liquid and vapor lines, with the vertical arrow showing the isothermal compression of the vapor in Example 5.1.1](./plots/ideal-pxy.py)

**Example 5.1.1** Liquids A and B form an ideal liquid mixture at room temperature, with $p^*_{\mathrm{A}} = 40.0\,\mathrm{kPa}$ and $p^*_{\mathrm{B}} = 120.0\,\mathrm{kPa}$. Vapor with $y_{\mathrm{A}} = 0.40$ is placed in a cylinder with a piston and compressed slowly at constant temperature. Find the pressure at which liquefaction begins and the composition of the first drop of liquid, and the pressure at which liquefaction is complete and the composition of the last bubble.

**Solution** When liquefaction begins (the dew point) the gas-phase composition is still $y_{\mathrm{A}} = 0.40$. From $x_{\mathrm{A}} = py_{\mathrm{A}}/p^*_{\mathrm{A}}$, $x_{\mathrm{B}} = py_{\mathrm{B}}/p^*_{\mathrm{B}}$ and $x_{\mathrm{A}} + x_{\mathrm{B}} = 1$,

$$
\frac{1}{p} = \frac{y_{\mathrm{A}}}{p^*_{\mathrm{A}}} + \frac{y_{\mathrm{B}}}{p^*_{\mathrm{B}}} = \frac{0.40}{40.0} + \frac{0.60}{120.0} = 0.0150\,\mathrm{kPa^{-1}}, \qquad p = 66.7\,\mathrm{kPa},
$$
and the first drop of liquid has $x_{\mathrm{A}} = 66.7 \times 0.40/40.0 = 0.667$. When liquefaction is complete (the bubble point) the liquid composition is $x_{\mathrm{A}} = 0.40$, $p = 40.0 \times 0.40 + 120.0 \times 0.60 = 88.0\,\mathrm{kPa}$, and the last bubble has $y_{\mathrm{A}} = 16.0/88.0 = 0.182$. Conversely, when this liquid is vaporized by reducing the pressure, the composition of the first bubble is also $y_{\mathrm{A}} = 0.182$. During the compression the compositions of both phases change: the liquid goes from $x_{\mathrm{A}} = 0.667$ to $0.40$ and the gas from $0.40$ to $0.182$, and the relative amounts of the two phases are given by the **lever rule** ([6.3.9](/6.3.9)).

### 5.1.3. Chemical Potentials of the Components of an Ideal Liquid Mixture

Let the mixture be in equilibrium with its vapor at temperature $T$ and pressure $p$, the vapor being an ideal-gas mixture. The chemical potentials of component B in the two phases are equal ([6.3.4](/6.3.4)),

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu_{\mathrm{B}}(\mathrm{g}) = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ} = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{p^*_{\mathrm{B}}}{p^\circ} + RT\ln x_{\mathrm{B}}.
$$
The sum of the first two terms is the chemical potential of pure liquid B in equilibrium with its vapor, that is, the chemical potential $\mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$ of pure liquid B. Hence

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}. \tag{5.2}
$$

The ideality of the vapor was used in the derivation, but Eq. (5.2) itself involves only the liquid phase. It is better to adopt it as the thermodynamic definition of an ideal liquid mixture: a liquid mixture in which the chemical potentials of all components satisfy Eq. (5.2) over some range of temperature and pressure. From Eq. (5.2), Raoult's law follows immediately when the vapor is an ideal gas; when the vapor is not ideal, Raoult's law remains strictly valid with the partial pressures replaced by **fugacities**.

$\mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$ is not the chemical potential of the standard state. The **standard state** of liquid B is defined as pure liquid at temperature $T$ and pressure $p^\circ$, with chemical potential $\mu^\circ_{\mathrm{B}}(\mathrm{l}, T)$, a function of temperature only. From $(\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m,B}}$,

$$
\mu^*_{\mathrm{B}}(\mathrm{l}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + \int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p,
$$
and substituting into Eq. (5.2):

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + RT\ln x_{\mathrm{B}} + \int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p. \tag{5.3}
$$
The three terms depend only on $T$; on $T$ and composition; and on $T$ and $p$, respectively. The molar volume of a condensed phase is small and the pressure term can usually be neglected: for water $V^*_{\mathrm{m}} = 18\,\mathrm{cm^3\,mol^{-1}}$, and a pressure change of $1\,\mathrm{MPa}$ gives a pressure term of only $18\,\mathrm{J\,mol^{-1}}$, whereas $x_{\mathrm{B}} = 0.5$ at $298\,\mathrm{K}$ gives $RT\ln x_{\mathrm{B}} = -1.7\,\mathrm{kJ\,mol^{-1}}$. When the pressure is not large,

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) \approx \mu^\circ_{\mathrm{B}}(\mathrm{l}, T) + RT\ln x_{\mathrm{B}}.
$$

Eq. (5.2) has exactly the same form as the chemical potential of a component of an ideal-gas mixture, $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(T, p) + RT\ln y_{\mathrm{B}}$ ([6.3.4](/6.3.4)), the chemical potential of the pure substance being replaced by that of the pure liquid. This similarity means that their mixing properties are also the same.

### 5.1.4. Mixing Properties

When amounts $n_{\mathrm{A}}$ of pure liquid A and $n_{\mathrm{B}}$ of pure liquid B are mixed isothermally and isobarically to form an ideal liquid mixture, the changes of the extensive properties are called mixing properties and written $\Delta_{\mathrm{mix}}V$, $\Delta_{\mathrm{mix}}H$, $\Delta_{\mathrm{mix}}S$, $\Delta_{\mathrm{mix}}G$.

**Definition 5.1.2** The change of Gibbs energy when a mixture is formed from pure components at constant temperature and pressure,

$$
\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}} - \sum_{\mathrm{B}}n_{\mathrm{B}}\mu^*_{\mathrm{B}},
$$
is called the **Gibbs energy of mixing**; the other mixing properties are defined analogously.

**Theorem 5.1.1 (Mixing Properties of an Ideal Liquid Mixture)** When an ideal liquid mixture is prepared from pure liquids at constant temperature and pressure,

$$
\Delta_{\mathrm{mix}}V = 0, \qquad \Delta_{\mathrm{mix}}H = 0, \qquad \Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}, \qquad \Delta_{\mathrm{mix}}G = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}.
$$

**Proof** By the additivity formula for partial molar quantities, $\Delta_{\mathrm{mix}}V = \sum_{\mathrm{B}}n_{\mathrm{B}}(V_{\mathrm{B}} - V^*_{\mathrm{m,B}})$. Differentiating Eq. (5.2) with respect to $p$ at constant $T$ and composition, $RT\ln x_{\mathrm{B}}$ is independent of pressure, so $V_{\mathrm{B}} = (\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = (\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m,B}}$ and $\Delta_{\mathrm{mix}}V = 0$.

Dividing both sides of Eq. (5.2) by $T$ and differentiating with respect to $T$, $R\ln x_{\mathrm{B}}$ is independent of temperature; by the partial-molar form of the **Gibbs–Helmholtz equation**, $\left(\frac{\partial(\mu_{\mathrm{B}}/T)}{\partial T}\right)_{p,n} = -\frac{H_{\mathrm{B}}}{T^2}$ ([6.3.3](/6.3.3), [6.3.4](/6.3.4)), one obtains $H_{\mathrm{B}} = H^*_{\mathrm{m,B}}$, so $\Delta_{\mathrm{mix}}H = 0$.

$\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}(\mu_{\mathrm{B}} - \mu^*_{\mathrm{B}}) = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}$; and from $S_{\mathrm{B}} = -(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = S^*_{\mathrm{m,B}} - R\ln x_{\mathrm{B}}$ one obtains $\Delta_{\mathrm{mix}}S$, which also equals $(\Delta_{\mathrm{mix}}H - \Delta_{\mathrm{mix}}G)/T$. $\square$

From $\Delta_{\mathrm{mix}}V = 0$ and $\Delta_{\mathrm{mix}}H = 0$ it also follows that $\Delta_{\mathrm{mix}}U = \Delta_{\mathrm{mix}}H - p\Delta_{\mathrm{mix}}V = 0$ and $\Delta_{\mathrm{mix}}A = \Delta_{\mathrm{mix}}G$. In short, preparing an ideal liquid mixture has no volume effect and no heat effect, the entropy increases and the Gibbs energy decreases. This is exactly the same as the isothermal, isobaric mixing of ideal gases, and $\Delta_{\mathrm{mix}}S$ is the **entropy of mixing** of [6.3.2](/6.3.2). Its statistical meaning is that molecules A and B can exchange places without change of energy; there are $\binom{N}{N_{\mathrm{A}}}$ ways of arranging $N_{\mathrm{A}}$ molecules A and $N_{\mathrm{B}}$ molecules B on $N$ sites, and the **Boltzmann entropy formula** ([5.2.4](/5.2.4)) together with **Stirling's approximation** gives $\Delta_{\mathrm{mix}}S = -k_{\mathrm{B}}\sum N_{\mathrm{B}}\ln x_{\mathrm{B}}$ ([6.3.10](/6.3.10)). The mixing of an ideal liquid mixture is driven purely by entropy.

![Molar mixing functions of an ideal liquid mixture at 298.15 K: the enthalpy and volume of mixing are zero, TΔmixS and ΔmixG are symmetric about x = 1/2, and ΔmixG,m = −RT ln 2 for equimolar composition](./plots/ideal-mixing-functions.py)

**Example 5.1.2** An ideal liquid mixture is formed from $1\,\mathrm{mol}$ of A and $1\,\mathrm{mol}$ of B at $298.15\,\mathrm{K}$ and atmospheric pressure. Find $\Delta V$, $\Delta H$, $\Delta U$, $\Delta S$ and $\Delta G$ for the mixing.

**Solution** $\Delta_{\mathrm{mix}}V = \Delta_{\mathrm{mix}}H = \Delta_{\mathrm{mix}}U = 0$; $\Delta_{\mathrm{mix}}S = -R(\ln 0.5 + \ln 0.5) = 2R\ln 2 = 11.53\,\mathrm{J\,K^{-1}}$; $\Delta_{\mathrm{mix}}G = -T\Delta_{\mathrm{mix}}S = -3.44\,\mathrm{kJ}$. Conversely, separating this mixture into pure A and pure B at constant temperature and pressure has $\Delta V = \Delta H = \Delta U = 0$, $\Delta S < 0$ and $\Delta G = \Delta A = +3.44\,\mathrm{kJ}$: the separation requires at least $3.44\,\mathrm{kJ}$ of **non-expansion work**.

## 5.2. Henry's Law and Ideal Dilute Solutions

### 5.2.1. Henry's Law

In 1803 Henry studied the solubility of gases in water and obtained *Henry's law*: at a given temperature, the equilibrium partial pressure of a volatile solute over a dilute solution is proportional to its mole fraction in the solution,

$$
p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}. \tag{5.4}
$$
The proportionality coefficient $k_{x,\mathrm{B}}$ is called the *Henry's law constant*; it has the unit Pa and depends on temperature, pressure and the nature of solute and solvent. It is also a limiting law, strictly valid as $x_{\mathrm{B}} \to 0$.

In general $k_{x,\mathrm{B}}$ is not equal to the saturated vapor pressure $p^*_{\mathrm{B}}$ of pure B: $p^*_{\mathrm{B}}$ reflects the tendency of B molecules to escape from pure B, while $k_{x,\mathrm{B}}$ reflects their tendency to escape when surrounded by solvent molecules. If the solvent attracts B more weakly than B molecules attract one another, B escapes more easily from the dilute solution and $k_{x,\mathrm{B}} > p^*_{\mathrm{B}}$; in the opposite case $k_{x,\mathrm{B}} < p^*_{\mathrm{B}}$. In an ideal liquid mixture the two are equal and Henry's law coincides with Raoult's law. $k_{x,\mathrm{B}}$ can be understood as the "vapor pressure" obtained by extrapolating the Henry's law line of the dilute solution to $x_{\mathrm{B}} = 1$: this is a hypothetical state, but it is useful in Section 5.2.3.

In using Henry's law note that:

1. The molecular form of the solute must be the same in the gas phase and in solution. Strong electrolytes (such as HCl in water) do not obey it; for gases such as $\ce{SO2}$, $\ce{NH3}$ and $\ce{CO2}$, which partly react or dissociate in water, $x_{\mathrm{B}}$ counts only the part present as dissolved molecules.
2. At moderate pressures, when several gases dissolve simultaneously the law can be applied to each gas separately (each with its own Henry's law constant), $p_{\mathrm{B}}$ being the partial pressure of that gas.
3. The concentration can also be expressed as the **molality** $b_{\mathrm{B}}$ or the **amount concentration** $c_{\mathrm{B}}$:

$$
p_{\mathrm{B}} = k_{b,\mathrm{B}}\frac{b_{\mathrm{B}}}{b^\circ} = k_{c,\mathrm{B}}\frac{c_{\mathrm{B}}}{c^\circ}, \qquad b^\circ = 1\,\mathrm{mol\,kg^{-1}}, \quad c^\circ = 1\,\mathrm{mol\,L^{-1}}.
$$
In a dilute solution $x_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}} \to \frac{n_{\mathrm{B}}}{n_{\mathrm{A}}} = M_{\mathrm{A}}b_{\mathrm{B}}$ and $c_{\mathrm{B}} \to \rho^*_{\mathrm{A}}b_{\mathrm{B}}$ ($M_{\mathrm{A}}$ and $\rho^*_{\mathrm{A}}$ are the molar mass and density of the solvent); comparing the limiting slopes gives

$$
k_{b,\mathrm{B}} = k_{x,\mathrm{B}}M_{\mathrm{A}}b^\circ, \qquad k_{c,\mathrm{B}} = k_{x,\mathrm{B}}\frac{M_{\mathrm{A}}c^\circ}{\rho^*_{\mathrm{A}}}. \tag{5.5}
$$
The three constants differ in value, though all have the unit Pa, and the conversion is exact (all are limiting slopes at $x_{\mathrm{B}} \to 0$). The literature also often uses the "solubility form" of Henry's law, $c_{\mathrm{B}} = H^{cp}p_{\mathrm{B}}$; the definition must be checked when it is used.

**Example 5.2.1** At $25\,^\circ\mathrm{C}$ the equilibrium mole fraction of $\ce{O2}$ in water at an $\ce{O2}$ partial pressure of $101.325\,\mathrm{kPa}$ is $2.29 \times 10^{-5}$ (CRC Handbook). Find $k_{x}(\ce{O2})$ and the dissolved oxygen in air-saturated water at $101.325\,\mathrm{kPa}$.

**Solution** $k_x = 101.325\,\mathrm{kPa}/(2.29 \times 10^{-5}) = 4.42 \times 10^9\,\mathrm{Pa}$. Air in contact with water is saturated with water vapor, so the partial pressure of dry air is $(101.325 - 3.17)\,\mathrm{kPa}$, of which $p(\ce{O2}) = 0.2095 \times 98.16\,\mathrm{kPa} = 20.6\,\mathrm{kPa}$; then $x(\ce{O2}) = 20.6 \times 10^3/(4.42 \times 10^9) = 4.65 \times 10^{-6}$ and $b = x/M_{\mathrm{A}} = 2.58 \times 10^{-4}\,\mathrm{mol\,kg^{-1}}$, about $8.2\,\mathrm{mg\,L^{-1}}$ (measured $8.3\,\mathrm{mg\,L^{-1}}$). A Henry's law constant of the order of GPa shows that $\ce{O2}$ is very sparingly soluble in water: $k_x \gg p^*$ expresses the weak interaction between solvent and solute. The $\ce{O2}$ dissolved directly in blood plasma also obeys Henry's law and is present in small amounts; the great majority of the oxygen carried by blood is bound to hemoglobin, which is a chemical equilibrium and does not obey Henry's law.

The solubility of a gas varies with pressure and temperature. By Henry's law, at constant temperature the solubility of a gas is proportional to its partial pressure. At a depth of $30\,\mathrm{m}$ a diver breathes air at about $0.4\,\mathrm{MPa}$, and the $\ce{N2}$ dissolved in blood and tissue is about four times that at the sea surface; if the ascent is too fast the external pressure drops abruptly, the dissolved $\ce{N2}$ cannot be exhaled through the lungs in time, and bubbles form in blood vessels and tissues. This is decompression sickness, which is why the ascent must be slow (or made with stops).

The effect of temperature follows from the chemical potential. Solute B is in equilibrium between gas and solution, $\mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln(p_{\mathrm{B}}/p^\circ) = \mu_{\mathrm{B}}(\mathrm{sln})$; writing the chemical potential of the solute in solution as $\mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$ as in Section 5.2.3 and substituting $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}$ gives

$$
\ln\frac{k_{x,\mathrm{B}}}{p^\circ} = \frac{\mu^*_{x,\mathrm{B}}(T, p) - \mu^\circ_{\mathrm{B}}(\mathrm{g}, T)}{RT}.
$$
Differentiating with respect to $T$ and using the Gibbs–Helmholtz equation,

$$
\frac{\mathrm{d}\ln k_{x,\mathrm{B}}}{\mathrm{d}T} = -\frac{H^{\infty}_{\mathrm{B}} - H^\circ_{\mathrm{m,B}}(\mathrm{g})}{RT^2} = -\frac{\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}}}{RT^2},
$$
where $H^{\infty}_{\mathrm{B}}$ is the partial molar enthalpy of B in infinitely dilute solution and $\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}}$ is the enthalpy change when $1\,\mathrm{mol}$ of gas dissolves in a large amount of solvent. The dissolution of a gas is usually exothermic ($\Delta_{\mathrm{sol}}H^{\infty}_{\mathrm{m}} < 0$), so $k_{x,\mathrm{B}}$ increases with temperature and the solubility at a given partial pressure, $x_{\mathrm{B}} = p_{\mathrm{B}}/k_{x,\mathrm{B}}$, decreases with temperature: warm water holds less dissolved oxygen. The solubility of a solid in an ideal solution, by contrast, increases with temperature: at saturation $\mu^*_{\mathrm{B}}(\mathrm{s}) = \mu^*_{\mathrm{B}}(\mathrm{l}) + RT\ln x_{\mathrm{B}}$, and the same derivation gives $\frac{\mathrm{d}\ln x_{\mathrm{B}}}{\mathrm{d}T} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}}{RT^2} > 0$. This is the freezing-point depression formula of Section 5.3.2 with the roles of solvent and solute exchanged, and it gives the liquidus of eutectic phase diagrams ([6.3.9](/6.3.9)).

### 5.2.2. Ideal Dilute Solutions

**Definition 5.2.1 (Ideal Dilute Solution)** A solution in which, over some concentration range, the solvent obeys Raoult's law and the solute obeys Henry's law is called an **ideal dilute solution**.

This is a limiting model: any nonelectrolyte solution tends to an ideal dilute solution as $x_{\mathrm{B}} \to 0$, but "small concentration" does not guarantee ideality, and electrolyte solutions deviate markedly even when very dilute ([6.3.12](/6.3.12)). The two laws are not independent: if the solute obeys Henry's law over some concentration range, the solvent must obey Raoult's law over the same range.

**Proof** At constant temperature and pressure, by the **Gibbs–Duhem equation**, $x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0$. That the solute obeys Henry's law means $\mu_{\mathrm{B}} = \text{constant} + RT\ln x_{\mathrm{B}}$ (5.2.3), $\mathrm{d}\mu_{\mathrm{B}} = RT\,\mathrm{d}x_{\mathrm{B}}/x_{\mathrm{B}}$, and so

$$
\mathrm{d}\mu_{\mathrm{A}} = -\frac{x_{\mathrm{B}}}{x_{\mathrm{A}}}RT\frac{\mathrm{d}x_{\mathrm{B}}}{x_{\mathrm{B}}} = RT\frac{\mathrm{d}x_{\mathrm{A}}}{x_{\mathrm{A}}}.
$$
Integrating from $x_{\mathrm{A}} = 1$ (pure solvent, $\mu_{\mathrm{A}} = \mu^*_{\mathrm{A}}$) gives $\mu_{\mathrm{A}} = \mu^*_{\mathrm{A}} + RT\ln x_{\mathrm{A}}$, which is Raoult's law. $\square$

The chemical potential of the solvent is the same as that of a component of an ideal liquid mixture:

$$
\mu_{\mathrm{A}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{A}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{A}} = \mu^\circ_{\mathrm{A}}(\mathrm{l}, T) + RT\ln x_{\mathrm{A}} + \int_{p^\circ}^{p}V^*_{\mathrm{m,A}}\,\mathrm{d}p, \tag{5.6}
$$
and the standard state is pure solvent at $T$ and $p^\circ$, a state that really exists.

### 5.2.3. The Chemical Potential of the Solute and the Three Standard States

From the vapor–liquid equilibrium of solute B and Henry's law (5.4),

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu^\circ_{\mathrm{B}}(\mathrm{g}, T) + RT\ln\frac{k_{x,\mathrm{B}}}{p^\circ} + RT\ln x_{\mathrm{B}} \equiv \mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}. \tag{5.7}
$$
$\mu^*_{x,\mathrm{B}}(T, p)$ is the chemical potential of "pure B" with $x_{\mathrm{B}} = 1$ that still obeys Henry's law, whose vapor pressure is $k_{x,\mathrm{B}}$. This is a hypothetical state: the true vapor pressure of pure B is $p^*_{\mathrm{B}}$ and its chemical potential is $\mu^*_{\mathrm{B}}$, the two differing by $RT\ln(k_{x,\mathrm{B}}/p^*_{\mathrm{B}})$. The significance of the hypothetical state is that it retains the properties of B in infinitely dilute solution: every B molecule is surrounded by solvent molecules. Its molar volume and molar enthalpy are therefore the partial molar volume $V^{\infty}_{\mathrm{B}}$ and partial molar enthalpy $H^{\infty}_{\mathrm{B}}$ of B in infinitely dilute solution, not $V^*_{\mathrm{m,B}}$ and $H^*_{\mathrm{m,B}}$ of pure B.

Expressing Henry's law in terms of $b_{\mathrm{B}}$ or $c_{\mathrm{B}}$ gives similarly

$$
\mu_{\mathrm{B}}(\mathrm{sln}) = \mu^*_{b,\mathrm{B}}(T, p) + RT\ln\frac{b_{\mathrm{B}}}{b^\circ} = \mu^*_{c,\mathrm{B}}(T, p) + RT\ln\frac{c_{\mathrm{B}}}{c^\circ},
$$
with the reference states being the hypothetical solutions at $b_{\mathrm{B}} = b^\circ$ and $c_{\mathrm{B}} = c^\circ$ that still obey Henry's law. When the pressure is specified as $p^\circ$, these reference states are the three **standard states** of the solute, with chemical potentials written $\mu^\circ_{x,\mathrm{B}}(T)$, $\mu^\circ_{b,\mathrm{B}}(T)$ and $\mu^\circ_{c,\mathrm{B}}(T)$; for example,

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^\circ_{b,\mathrm{B}}(T) + RT\ln\frac{b_{\mathrm{B}}}{b^\circ} + \int_{p^\circ}^{p}V^{\infty}_{\mathrm{B}}\,\mathrm{d}p. \tag{5.8}
$$

| Concentration scale | Chemical potential | Standard state ($T$, $p^\circ$) | Real? |
|---|---|---|---|
| Solvent $x_{\mathrm{A}}$ | $\mu^\circ_{\mathrm{A}}(\mathrm{l}, T) + RT\ln x_{\mathrm{A}}$ | Pure solvent A | Real |
| Solute $x_{\mathrm{B}}$ | $\mu^\circ_{x,\mathrm{B}}(T) + RT\ln x_{\mathrm{B}}$ | B at $x_{\mathrm{B}} = 1$ obeying Henry's law | Hypothetical |
| Solute $b_{\mathrm{B}}$ | $\mu^\circ_{b,\mathrm{B}}(T) + RT\ln(b_{\mathrm{B}}/b^\circ)$ | $b_{\mathrm{B}} = 1\,\mathrm{mol\,kg^{-1}}$ obeying Henry's law | Hypothetical |
| Solute $c_{\mathrm{B}}$ | $\mu^\circ_{c,\mathrm{B}}(T) + RT\ln(c_{\mathrm{B}}/c^\circ)$ | $c_{\mathrm{B}} = 1\,\mathrm{mol\,L^{-1}}$ obeying Henry's law | Hypothetical |

(The pressure terms are omitted from the table.) For a solution in a given state the chemical potential of the solute has only one value, and the three expressions differ only in how it is divided into "standard chemical potential plus concentration term". Since $x_{\mathrm{B}} \to M_{\mathrm{A}}b_{\mathrm{B}}$ in dilute solution, comparing the three expressions gives

$$
\mu^\circ_{b,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln(M_{\mathrm{A}}b^\circ), \qquad \mu^\circ_{c,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln\frac{M_{\mathrm{A}}c^\circ}{\rho^*_{\mathrm{A}}},
$$
in agreement with Eq. (5.5). In aqueous solution $M_{\mathrm{A}}b^\circ = 0.018015$ and at $298.15\,\mathrm{K}$ $RT\ln(M_{\mathrm{A}}b^\circ) = -9.96\,\mathrm{kJ\,mol^{-1}}$: with different standard states the standard chemical potentials can differ by nearly $10\,\mathrm{kJ\,mol^{-1}}$, so thermodynamic data in solution (such as the $\Delta_{\mathrm{f}}G^\circ$ of hydrated species in the tables of [6.1.6](/6.1.6)) must state the standard state used, usually $b^\circ$.

The expressions for solute and solvent differ in three ways: the standard state (the solvent's is a real pure liquid, the solute's a hypothetical state); the integrand of the pressure term ($V^*_{\mathrm{m,A}}$ versus $V^{\infty}_{\mathrm{B}}$); and the solute has several equivalent forms.

## 5.3. Colligative Properties of Dilute Solutions

At a given temperature and pressure, certain properties of dilute solutions depend only on the number of solute particles and not on the nature of the solute; they are called *colligative properties*: *vapor-pressure lowering*, *freezing-point depression*, *boiling-point elevation* and osmotic pressure. Their common root is the lowering of the chemical potential of the solvent by the solute: $\mu_{\mathrm{A}} - \mu^*_{\mathrm{A}} = RT\ln x_{\mathrm{A}} < 0$, where the amount of lowering depends only on $x_{\mathrm{A}}$ and comes from the entropy of mixing, independently of the energy of the solute molecules.

Plotting the chemical potential of the solvent against temperature at constant pressure (with slope $(\partial\mu/\partial T)_p = -S_{\mathrm{m}}$, gas > liquid > solid), after the liquid line is shifted down by $RT\ln x_{\mathrm{A}}$ its intersections with the solid and gas lines move to lower and higher temperatures respectively, and the freezing-point depression and boiling-point elevation are plain to see. The premise is that the solute does not enter the solid or gas phases: the solute is nonvolatile and only pure solvent crystallizes on freezing.

![Schematic of the chemical potential of a solvent against temperature at constant pressure: the solute shifts the liquid line down by RT ln x_A (exaggerated in the figure); its intersection with the solid line moves to a lower temperature (freezing-point depression) and its intersection with the gas line to a higher temperature (boiling-point elevation)](./plots/colligative-mu-t.py)

### 5.3.1. Vapor-Pressure Lowering

When the solute is nonvolatile, the vapor pressure of the solution is the partial pressure of the solvent. By Raoult's law,

$$
\Delta p = p^*_{\mathrm{A}} - p_{\mathrm{A}} = p^*_{\mathrm{A}}(1 - x_{\mathrm{A}}) = p^*_{\mathrm{A}}x_{\mathrm{B}},
$$
and the relative vapor-pressure lowering $\Delta p/p^*_{\mathrm{A}}$ equals the mole fraction of solute. When the solute is volatile, the partial pressure of the solvent still falls according to Raoult's law, but the total vapor pressure may rise.

### 5.3.2. Freezing-Point Depression

The freezing point is the temperature at which solid and liquid coexist in equilibrium at a given pressure. If it is pure solid solvent A that separates on cooling the solution (no **solid solution** is formed), the freezing point $T_{\mathrm{f}}$ of the solution is lower than $T^*_{\mathrm{f}}$ of the pure solvent: freezing-point depression.

**Theorem 5.3.1** For an ideal liquid mixture or ideal dilute solution from which only pure solid solvent A separates at the freezing point, with the molar enthalpy of fusion $\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}$ of the solvent independent of temperature between $T_{\mathrm{f}}$ and $T^*_{\mathrm{f}}$,

$$
\ln x_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}}\right). \tag{5.9}
$$
For a very dilute solution ($x_{\mathrm{B}} \ll 1$),

$$
\Delta T_{\mathrm{f}} = T^*_{\mathrm{f}} - T_{\mathrm{f}} = K_{\mathrm{f}}b_{\mathrm{B}}, \qquad K_{\mathrm{f}} = \frac{R(T^*_{\mathrm{f}})^2M_{\mathrm{A}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}. \tag{5.10}
$$

**Proof** At the freezing point solid and liquid are in equilibrium, $\mu_{\mathrm{A}}(\mathrm{sln}, T, p, x_{\mathrm{A}}) = \mu^*_{\mathrm{A}}(\mathrm{s}, T, p)$. Substituting Eq. (5.6):

$$
\ln x_{\mathrm{A}} = \frac{\mu^*_{\mathrm{A}}(\mathrm{s}) - \mu^*_{\mathrm{A}}(\mathrm{l})}{RT} = -\frac{\Delta_{\mathrm{fus}}G_{\mathrm{m,A}}(T)}{RT},
$$
where $\Delta_{\mathrm{fus}}G_{\mathrm{m,A}}(T)$ is the molar Gibbs energy change on melting pure A at temperature $T$. This equation holds at every freezing point, that is, it fixes the functional relation between the freezing point $T$ and the composition $x_{\mathrm{A}}$. Differentiating with respect to $T$ at constant pressure, by the Gibbs–Helmholtz equation $\frac{\mathrm{d}(\Delta G/T)}{\mathrm{d}T} = -\frac{\Delta H}{T^2}$,

$$
\frac{\mathrm{d}\ln x_{\mathrm{A}}}{\mathrm{d}T} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{RT^2}.
$$
Integrating from pure solvent ($x_{\mathrm{A}} = 1$, $T = T^*_{\mathrm{f}}$) to the solution ($x_{\mathrm{A}}$, $T_{\mathrm{f}}$), for constant enthalpy of fusion, gives Eq. (5.9).

In a dilute solution $\ln x_{\mathrm{A}} = \ln(1 - x_{\mathrm{B}}) = -x_{\mathrm{B}} - \frac{x_{\mathrm{B}}^2}{2} - \cdots \approx -x_{\mathrm{B}}$ and $\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}} = \frac{\Delta T_{\mathrm{f}}}{T_{\mathrm{f}}T^*_{\mathrm{f}}} \approx \frac{\Delta T_{\mathrm{f}}}{(T^*_{\mathrm{f}})^2}$, so $x_{\mathrm{B}} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}\Delta T_{\mathrm{f}}}{R(T^*_{\mathrm{f}})^2}$; then $x_{\mathrm{B}} \approx n_{\mathrm{B}}/n_{\mathrm{A}} = M_{\mathrm{A}}b_{\mathrm{B}}$ gives Eq. (5.10). $\square$

$K_{\mathrm{f}}$ is called the *cryoscopic constant* and depends only on the solvent. For water, $T^*_{\mathrm{f}} = 273.15\,\mathrm{K}$, $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$ and $K_{\mathrm{f}} = 1.86\,\mathrm{K\,kg\,mol^{-1}}$; for benzene, $T^*_{\mathrm{f}} = 278.7\,\mathrm{K}$, $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 9.87\,\mathrm{kJ\,mol^{-1}}$ and $K_{\mathrm{f}} = 5.11\,\mathrm{K\,kg\,mol^{-1}}$. Solvents with a small enthalpy of fusion, a high melting point and a large molar mass (such as camphor, $K_{\mathrm{f}} \approx 40\,\mathrm{K\,kg\,mol^{-1}}$) show a more marked freezing-point depression.

The two approximations in Eq. (5.10) (the logarithmic expansion and $T_{\mathrm{f}} \approx T^*_{\mathrm{f}}$) together amount to about 1.5% at $b_{\mathrm{B}} = 1\,\mathrm{mol\,kg^{-1}}$ (the linear law gives $1.86\,\mathrm{K}$ and the integrated formula $1.83\,\mathrm{K}$); at higher concentrations the variation of the enthalpy of fusion with temperature ($\Delta_{\mathrm{fus}}C_p = C_{p,\mathrm{m}}(\mathrm{l}) - C_{p,\mathrm{m}}(\mathrm{s})$, **Kirchhoff's law**, [6.3.1](/6.3.1)) and the nonideality of the solution itself ([6.3.6](/6.3.6)) must also be considered.

![Freezing-point depression of water (solution treated as ideal): comparison of the linear law K_f b, the integrated formula (constant enthalpy of fusion) and the integrated formula including ΔfusCp; at 4 mol/kg the three give 7.4, 7.0 and 7.2 K respectively](./plots/freezing-point-depression.py)

Applications:

1. Determination of molar mass: from $\Delta T_{\mathrm{f}}$ and the mass of solute one finds $b_{\mathrm{B}}$ and hence $M_{\mathrm{B}}$ (glucose, amino acids, adrenaline, and so on). If the solute associates or dissociates in solution, what is measured is an "apparent molar mass", from which association and dissociation can be studied.
2. Determination of the total concentration of all solute particles in a solution: the freezing point of human serum is about $-0.56\,^\circ\mathrm{C}$, giving $b = 0.56/1.86 = 0.30\,\mathrm{mol\,kg^{-1}}$, called clinically the osmolality (about $300\,\mathrm{mOsm\,kg^{-1}}$), with all ions and molecules counted. The freezing point of seawater is about $-1.9\,^\circ\mathrm{C}$, corresponding to about $1.0\,\mathrm{mol\,kg^{-1}}$ of solute particles.
3. Testing purity: impurities lower the melting point and widen the melting range, which is the basis of using melting points to judge purity in organic chemistry.
4. Antifreeze: automobile antifreeze (aqueous ethylene glycol) and salting of roads. Cold-hardy plants convert starch to soluble sugars at low temperature, raising the concentration of the cell sap, which both lowers the freezing point and reduces freezing inside cells; this is why cabbage that has been through frost is sweeter. The antifreeze proteins of some polar fish, however, are not a colligative effect: they adsorb on the surface of ice crystals and prevent their growth, and at very low concentrations lower the freezing point by about $1\,\mathrm{K}$, far more than colligative effects would predict.

### 5.3.3. Boiling-Point Elevation

The boiling point is the temperature at which the vapor pressure of a liquid equals the external pressure. When the solute is nonvolatile, the vapor pressure of the solution is lower than that of the pure solvent, and the temperature must rise higher to reach the external pressure: boiling-point elevation.

**Theorem 5.3.2** For an ideal dilute solution of a nonvolatile solute, with the **molar enthalpy of vaporization** $\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}$ of the solvent constant,

$$
\ln x_{\mathrm{A}} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{b}}} - \frac{1}{T^*_{\mathrm{b}}}\right), \qquad \Delta T_{\mathrm{b}} = T_{\mathrm{b}} - T^*_{\mathrm{b}} = K_{\mathrm{b}}b_{\mathrm{B}}, \quad K_{\mathrm{b}} = \frac{R(T^*_{\mathrm{b}})^2M_{\mathrm{A}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}. \tag{5.11}
$$

**Proof** At the boiling point the solvent is in equilibrium between the solution and the pure vapor (there is no solute in the vapor), $\mu_{\mathrm{A}}(\mathrm{sln}, T, p) = \mu^*_{\mathrm{A}}(\mathrm{g}, T, p)$,

$$
\ln x_{\mathrm{A}} = \frac{\mu^*_{\mathrm{A}}(\mathrm{g}) - \mu^*_{\mathrm{A}}(\mathrm{l})}{RT} = \frac{\Delta_{\mathrm{vap}}G_{\mathrm{m,A}}(T)}{RT}.
$$
By the Gibbs–Helmholtz equation, $\frac{\mathrm{d}\ln x_{\mathrm{A}}}{\mathrm{d}T} = -\frac{\Delta_{\mathrm{vap}}H_{\mathrm{m,A}}}{RT^2}$, and integrating from $x_{\mathrm{A}} = 1$, $T = T^*_{\mathrm{b}}$ gives the first equation. The dilute-solution approximations are the same as in Section 5.3.2: $-\ln x_{\mathrm{A}} \approx x_{\mathrm{B}} \approx M_{\mathrm{A}}b_{\mathrm{B}}$ and $T_{\mathrm{b}}T^*_{\mathrm{b}} \approx (T^*_{\mathrm{b}})^2$. $\square$

This is the same result as the **Clausius–Clapeyron equation** ([6.1.1](/6.1.1)) seen in two ways: Raoult's law shifts the whole vapor-pressure curve down by $\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}}$, and the slope of the vapor-pressure curve, $\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}p}{RT^2}$, converts this pressure difference to a temperature difference $\Delta T_{\mathrm{b}} = \Delta p/(\mathrm{d}p/\mathrm{d}T)$, with the same result.

$K_{\mathrm{b}}$ is called the *ebullioscopic constant*. For water at $101.325\,\mathrm{kPa}$, $T^*_{\mathrm{b}} = 373.12\,\mathrm{K}$, $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$ and $K_{\mathrm{b}} = 0.513\,\mathrm{K\,kg\,mol^{-1}}$, only about a quarter of $K_{\mathrm{f}}$ (because the enthalpy of vaporization is large), so the boiling-point method is less sensitive than the freezing-point method. Note that the statement "the boiling point of a dilute solution is always higher than that of the pure solvent" holds only for nonvolatile solutes; the boiling point of aqueous ethanol is lower than that of water.

### 5.3.4. Osmotic Pressure

A membrane that lets solvent molecules through but not solute molecules is called a *semipermeable membrane*. If pure solvent and a solution are separated by a semipermeable membrane, solvent passes spontaneously through the membrane into the solution side and raises the level of the solution; this is osmosis. The reason is that at the same temperature and pressure $\mu^*_{\mathrm{A}}(T, p) > \mu_{\mathrm{A}}(\mathrm{sln}, T, p)$. Osmosis can be prevented by applying an extra pressure $\varPi$ on the solution side: raising the pressure raises the chemical potential of the solvent in the solution ($(\partial\mu_{\mathrm{A}}/\partial p)_T = V_{\mathrm{A}} > 0$), and osmotic equilibrium is reached when it equals the chemical potential of the pure solvent.

**Definition 5.3.1** When pure solvent and a solution separated by a semipermeable membrane are in osmotic equilibrium, the pressure $\varPi$ by which the solution side must exceed the pure-solvent side is called the **osmotic pressure** of the solution:

$$
\mu^*_{\mathrm{A}}(\mathrm{l}, T, p) = \mu_{\mathrm{A}}(\mathrm{sln}, T, p + \varPi, x_{\mathrm{A}}).
$$

By this definition the osmotic pressure is a property of the solution itself; every solution has one, though it is not manifested without a semipermeable membrane.

**Theorem 5.3.3** For an ideal liquid mixture or ideal dilute solution, if the solvent is incompressible,

$$
\varPi V^*_{\mathrm{m,A}} = -RT\ln x_{\mathrm{A}}; \tag{5.12}
$$
for an ideal dilute solution ($x_{\mathrm{B}} \ll 1$) this becomes approximately van 't Hoff's osmotic pressure formula

$$
\varPi = c_{\mathrm{B}}RT. \tag{5.13}
$$

**Proof** From Eq. (5.6), $\mu_{\mathrm{A}}(\mathrm{sln}, T, p + \varPi) = \mu^*_{\mathrm{A}}(\mathrm{l}, T, p + \varPi) + RT\ln x_{\mathrm{A}}$, and $\mu^*_{\mathrm{A}}(\mathrm{l}, T, p + \varPi) - \mu^*_{\mathrm{A}}(\mathrm{l}, T, p) = \int_p^{p+\varPi}V^*_{\mathrm{m,A}}\,\mathrm{d}p = \varPi V^*_{\mathrm{m,A}}$. Substituting in the condition for osmotic equilibrium gives Eq. (5.12). In a dilute solution $-\ln x_{\mathrm{A}} \approx x_{\mathrm{B}} \approx n_{\mathrm{B}}/n_{\mathrm{A}}$, and $n_{\mathrm{A}}V^*_{\mathrm{m,A}} \approx V$ (the volume of the solution), so $\varPi \approx n_{\mathrm{B}}RT/V = c_{\mathrm{B}}RT$. $\square$

Eq. (5.13) was proposed by van 't Hoff in 1886 and has the same form as the equation of state of the ideal gas, but the solute molecules do not "strike" the semipermeable membrane as gas molecules do: the osmotic pressure arises from the lowering of the chemical potential of the solvent, that is, from the entropy of mixing. In it the unit of $c_{\mathrm{B}}$ is $\mathrm{mol\,m^{-3}}$. For electrolytes, $c_{\mathrm{B}}$ must be replaced by the total concentration of all solute particles.

**Example 5.3.1** Find the four colligative properties of a nonelectrolyte aqueous solution with $b_{\mathrm{B}} = 0.001\,\mathrm{mol\,kg^{-1}}$ at $25\,^\circ\mathrm{C}$. Given $p^*(\ce{H2O}) = 3.17\,\mathrm{kPa}$.

**Solution** $x_{\mathrm{B}} \approx M_{\mathrm{A}}b_{\mathrm{B}} = 1.80 \times 10^{-5}$ and $\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}} = 0.057\,\mathrm{Pa}$; $\Delta T_{\mathrm{f}} = 1.86 \times 10^{-3}\,\mathrm{K}$; $\Delta T_{\mathrm{b}} = 5.1 \times 10^{-4}\,\mathrm{K}$; $c_{\mathrm{B}} \approx \rho^*_{\mathrm{A}}b_{\mathrm{B}} = 0.997\,\mathrm{mol\,m^{-3}}$ and $\varPi = 0.997 \times 8.314 \times 298.15 = 2.47\,\mathrm{kPa}$, equivalent to a column of water about $25\,\mathrm{cm}$ high. Of the four colligative properties the osmotic pressure is the most marked, so the osmotic-pressure method is suited to determining the molar mass of macromolecules: for a protein solution of $1\,\mathrm{g\,L^{-1}}$ with molar mass $10^5\,\mathrm{g\,mol^{-1}}$, $\varPi \approx 25\,\mathrm{Pa}$ can still be measured accurately, whereas the freezing point falls by only $2 \times 10^{-5}\,\mathrm{K}$. Macromolecular solutions deviate from ideality early, and in practice one plots $\varPi/c = RT(1/M + A_2c + \cdots)$ and extrapolates to $c \to 0$ ([6.3.21](/6.3.21)); what is measured is the number-average molar mass.

**Example 5.3.2** The osmotic pressure of human blood at $37\,^\circ\mathrm{C}$ is $776\,\mathrm{kPa}$. Treating an aqueous NaCl solution as an ideal dilute solution with NaCl completely dissociated, find the molality of the NaCl solution isotonic with blood.

**Solution** The total concentration of solute particles is $c = \varPi/RT = 776 \times 10^3/(8.314 \times 310.15) = 301\,\mathrm{mol\,m^{-3}}$; each NaCl gives two ions, so $c(\ce{NaCl}) = 150\,\mathrm{mol\,m^{-3}}$ and $b(\ce{NaCl}) \approx c/\rho^*_{\mathrm{A}} = 0.150\,\mathrm{mol\,kg^{-1}}$, that is, $8.8\,\mathrm{g}$ of NaCl per kilogram of water. Medical physiological saline is $0.9\%$ (mass fraction, about $9\,\mathrm{g}$ of NaCl per liter of solution): real NaCl solutions are not ideal, and interactions between ions reduce the effective number of particles to about 0.93 of the ideal value (the osmotic coefficient, [6.3.12](/6.3.12)), so the concentration must be slightly higher than the ideal estimate. Compare with the freezing point of serum in Section 5.3.2: particles at $0.30\,\mathrm{mol\,kg^{-1}}$ give an osmotic pressure of about $770\,\mathrm{kPa}$ at $37\,^\circ\mathrm{C}$, and the two determinations agree.

The role of osmotic pressure in biology:

- The cell membrane is permeable to water and impermeable to many solutes and approximates a semipermeable membrane. Red blood cells placed in pure water absorb water and burst (hemolysis), and placed in concentrated brine lose water and shrink, so intravenous infusions must use isotonic solutions ($0.9\%$ NaCl or $5\%$ glucose).
- The proteins in plasma (mainly albumin) cannot pass through the capillary wall and produce a colloid osmotic pressure of about $3.3\,\mathrm{kPa}$ ($25\,\mathrm{mmHg}$), which together with the hydrostatic pressure in the capillaries determines the formation and return of tissue fluid. When plasma protein is too low, return of tissue fluid decreases and causes edema.
- The turgor of plant cells and the opening and closing of stomata are regulated by osmosis; the rise of water in tall trees is driven mainly by the negative pressure (tension) created in the xylem by transpiration from the leaves, while the osmotic pressure of the roots (root pressure) is only about $0.1$–$0.2\,\mathrm{MPa}$, not enough to send water up to a crown a hundred meters high.

If a pressure greater than $\varPi$ is applied to the solution side, solvent flows from the solution to the pure-solvent side, which is called *reverse osmosis*. It is used for seawater desalination, concentration of solutions and wastewater treatment. The osmotic pressure of seawater (salinity about $35\,\mathrm{g\,kg^{-1}}$) is about $2.7\,\mathrm{MPa}$, and the minimum work to extract $1\,\mathrm{m^3}$ of fresh water from seawater is about $\varPi V \approx 2.7\,\mathrm{MJ} = 0.75\,\mathrm{kWh}$ (as the recovery tends to zero); modern reverse-osmosis plants consume about $3\,\mathrm{kWh\,m^{-3}}$. Conversely, the osmotic pressure difference between river water and seawater can also be used to generate power (pressure-retarded osmosis), the theoretical energy obtainable per cubic meter of fresh water being likewise about $0.75\,\mathrm{kWh}$.

## Summary

| Content | Main points |
|---|---|
| Raoult's law | $p_{\mathrm{A}} = p^*_{\mathrm{A}}x_{\mathrm{A}}$, solvent, limiting law for $x_{\mathrm{A}} \to 1$ |
| Henry's law | $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}} = k_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ = k_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$, volatile solute, same molecular form; $k_{x,\mathrm{B}} \ne p^*_{\mathrm{B}}$ |
| Ideal liquid mixture | Every component obeys Raoult's law over the whole concentration range; $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}$; $\Delta_{\mathrm{mix}}V = \Delta_{\mathrm{mix}}H = 0$, $\Delta_{\mathrm{mix}}S = -R\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$, $\Delta_{\mathrm{mix}}G = RT\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$ |
| Ideal dilute solution | Solvent obeys Raoult's law, solute obeys Henry's law (each implies the other by the Gibbs–Duhem equation) |
| Standard states of the solute | Three hypothetical states, $x_{\mathrm{B}} = 1$, $b^\circ$, $c^\circ$: same chemical potential, different standard chemical potentials; the pressure term uses $V^{\infty}_{\mathrm{B}}$ |
| Colligative properties | From $\mu_{\mathrm{A}} - \mu^*_{\mathrm{A}} = RT\ln x_{\mathrm{A}}$; $\Delta p = p^*_{\mathrm{A}}x_{\mathrm{B}}$, $\Delta T_{\mathrm{f}} = K_{\mathrm{f}}b_{\mathrm{B}}$, $\Delta T_{\mathrm{b}} = K_{\mathrm{b}}b_{\mathrm{B}}$, $\varPi = c_{\mathrm{B}}RT$; exact forms $\ln x_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H}{R}(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}})$, $\varPi V^*_{\mathrm{m,A}} = -RT\ln x_{\mathrm{A}}$ |
| Conditions | Freezing-point depression: only pure solvent separates; boiling-point elevation and vapor-pressure lowering: nonvolatile solute; osmotic pressure: membrane passes only solvent; electrolytes counted by total number of particles |

## Questions

1. If two liquids can be mixed in any proportion, must they form an ideal liquid mixture? Must the total vapor pressure of a binary ideal liquid mixture exceed the saturated vapor pressure of either pure component?

   **Answer** Neither is necessary. Water and ethanol mix in any proportion but deviate markedly from Raoult's law ([6.3.6](/6.3.6)); conversely, $\Delta_{\mathrm{mix}}G < 0$ for an ideal liquid mixture at all compositions, so such liquids must mix in any proportion. The total pressure of an ideal liquid mixture lies between the vapor pressures of the two pure components.

2. A glass of pure water and a glass of sugar water are placed under an evacuated glass bell jar at constant temperature. What happens after a long enough time?

   **Answer** The vapor pressure of pure water is higher than the partial pressure of water over the sugar water, so water keeps evaporating from the pure-water glass and condensing in the sugar-water glass until the pure-water glass is dry (or until the sugar water has been diluted to the same vapor pressure as pure water, which is impossible for a nonvolatile solute).

3. Which of the four colligative properties of an ideal dilute solution also hold for a volatile solute?

   **Answer** Freezing-point depression (as long as pure solid solvent separates) and osmotic pressure (as long as the semipermeable membrane does not let the solute through) depend only on the chemical potential of the solvent in the solution and hold equally for volatile solutes; the formulas for vapor-pressure lowering and boiling-point elevation require a nonvolatile solute.
