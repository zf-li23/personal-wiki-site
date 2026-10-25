---
title: The Phase Rule and One-Component Systems
description: Phases and the condition for phase equilibrium; number of species, independent reactions, concentration restrictions and the number of components; the variance and the derivation of the Gibbs phase rule, conditional variance and the generalized phase rule; the Clapeyron and Clausius–Clapeyron equations (with the temperature dependence of the enthalpy of vaporization), solid–liquid equilibrium and the effect of external pressure on vapor pressure; first-order and second-order transitions, the Ehrenfest equations and lambda transitions; the phase diagram of water, the triple point and the freezing point, high-pressure ices, CO₂ and supercritical fluids.
source_hash: 39fd535146fa
---

Dissolution, distillation, crystallization, extraction, metallurgy, and even the gel–liquid-crystal transition of a cell membrane are all processes in which a multiphase system approaches equilibrium. The previous chapter dealt with chemical equilibrium; this chapter and the next deal with phase equilibrium. The same thermodynamic principle applies, now to the exchange of matter between phases: at equilibrium, each substance has the same **chemical potential** in every phase in which it is present ([6.3.4](/6.3.4)). We begin with the Gibbs phase rule, a counting rule obeyed by every system at phase equilibrium. It involves no specific substance, yet it tells us how many phases can coexist at most and how many intensive variables are needed to fix the state of a system. We then use the equality of chemical potentials to derive the equation for the two-phase equilibrium line of a pure substance (the Clapeyron equation), which puts the Clausius–Clapeyron equation of [6.1.1](/6.1.1#sec-1.2.2) on a rigorous footing and clarifies its approximations and corrections. Next we classify phase transitions according to the continuity of the derivatives of the chemical potential, which covers the ferromagnetic and superconducting transitions met in physics ([5.3.8](/5.3.8), [5.3.9](/5.3.9)). Finally we learn to read the phase diagram of a one-component system. [6.3.9](/6.3.9) applies the phase rule and the methods of this chapter to two- and three-component systems; the effect of surfaces and curved interfaces on phase equilibrium (the Kelvin equation) is left to [6.3.19](/6.3.19).

## 8.1. Phases and the Condition for Phase Equilibrium

### 8.1.1. Phases and the Number of Phases

**Definition 8.1.1 (Phase)** A part of a system whose physical and chemical properties are completely uniform is called a **phase**. The number of phases coexisting in a system is the number of phases, denoted $P$. A system with only one phase is a homogeneous system; a system with two or more phases is a heterogeneous system.

Phases are separated by well-defined interfaces, across which some properties (density, refractive index, composition, etc.) change abruptly. To count phases we must ask on what scale the substances are mixed:

- Gases: any number of gases can mix at the molecular level, so there is only one gas phase.
- Liquids: depending on their mutual solubility there may be one phase (water and ethanol), two phases (water and benzene) or even three; milk and soy milk are emulsions and colloidal dispersions, not single phases ([6.3.21](/6.3.21)).
- Solids: apart from solid solutions ([6.1.4](/6.1.4)), each solid is a phase. Powders of $\ce{CaCO3(s)}$ and $\ce{CaO(s)}$ remain two phases however uniformly they are mixed; the $\alpha$, $\gamma$ and $\delta$ forms of iron are one phase each; a pile of small ice cubes, or $\ce{CaCO3(s)}$ in large lumps and as powder, is only one phase. The number of phases does not depend on how many pieces a substance is divided into.

### 8.1.2. The Condition for Phase Equilibrium

A multiphase system in thermodynamic equilibrium must simultaneously satisfy thermal equilibrium (equal temperature in all phases), mechanical equilibrium (equal pressure in all phases when the interfaces are planar), phase equilibrium and chemical equilibrium. The condition for phase equilibrium is given by the **chemical potential**: at constant temperature and pressure, if the chemical potentials of substance B differ in phases $\alpha$ and $\beta$, transferring $\mathrm{d}n_{\mathrm{B}}$ from $\alpha$ to $\beta$ changes the Gibbs energy of the system by $\mathrm{d}G = (\mu_{\mathrm{B}}^{\beta} - \mu_{\mathrm{B}}^{\alpha})\,\mathrm{d}n_{\mathrm{B}}$, so matter flows spontaneously from the phase of higher chemical potential to that of lower chemical potential until the two are equal ([6.3.4](/6.3.4)).

**Definition 8.1.2** A state of a multiphase system in which the composition and amount of each phase do not change with time is called **phase equilibrium**.

**Theorem 8.1.1 (Condition for phase equilibrium)** A multiphase system with uniform temperature and pressure is in phase equilibrium if and only if every substance B has the same chemical potential in all the phases in which it is present,

$$
\mu_{\mathrm{B}}^{\alpha} = \mu_{\mathrm{B}}^{\beta} = \cdots .
$$

The condition requires equal chemical potentials only in the phases where the substance is present; it does not require every substance to be present in every phase. For example, when an aqueous sucrose solution is in equilibrium with its vapor, sucrose is nonvolatile and only water satisfies $\mu_{\mathrm{H_2O}}(\mathrm{sln}) = \mu_{\mathrm{H_2O}}(\mathrm{g})$. For a **semipermeable membrane** that passes only $\ce{O2}$, only the chemical potential of $\ce{O2}$ is equal on the two sides, and the pressures on the two sides may differ (§8.2.3).

An important feature of phase equilibrium is that it depends only on intensive properties and not on the amounts of the phases. At $25\,{}^\circ\mathrm{C}$ a glass of water and a drop of water have the same saturated vapor pressure; the boiling point, freezing point and solubility of a solution are all intensive properties. How many intensive variables are needed to describe a system at phase equilibrium is therefore the question of the next section.

## 8.2. The Phase Rule

### 8.2.1. Number of Species and Number of Components

To describe the composition of a system we first have to count the substances in it, but the answer depends on the level of description: pure water can be regarded as containing only $\ce{H2O}$, or as containing three species $\ce{H2O}$, $\ce{H+}$ and $\ce{OH-}$. We need a quantity that does not depend on how the system is described.

**Definition 8.2.1 (Number of components)** Let a system contain $s$ chemical species (the number of species), let there be $r$ independent chemical equilibria among them (the number of independent reactions: reactions that cannot be obtained as linear combinations of the others), and let there be $r'$ concentration restrictions (fixed relations among the concentrations of several species in the same phase; the condition $\sum_{\mathrm{B}} x_{\mathrm{B}} = 1$ in each phase is not counted). Then

$$
C = s - r - r'
$$
is called the **number of components** of the system. It is the minimum number of species needed to specify the composition of all phases at equilibrium, that is, the number of species whose amounts can be varied independently at equilibrium.

A concentration restriction must be an intensive relation within a single phase. It usually comes from the way the system is prepared (reactants charged in stoichiometric ratio, all species produced by the decomposition of a single substance) or from electroneutrality. Some examples:

| System | $s$ | $r$ | $r'$ | $C$ | Remark |
|---|---|---|---|---|---|
| Pure water, counting only $\ce{H2O}$ | 1 | 0 | 0 | 1 | |
| Pure water, counting $\ce{H2O, H+, OH-}$ | 3 | 1 | 1 | 1 | Electroneutrality: $x(\ce{H+}) = x(\ce{OH-})$ |
| $\ce{H2(g) + I2(g) <=> 2HI(g)}$, arbitrary charge | 3 | 1 | 0 | 2 | |
| Same, $\ce{H2}$ and $\ce{I2}$ charged in equal amounts, or produced only by decomposition of $\ce{HI}$ | 3 | 1 | 1 | 1 | $p(\ce{H2}) = p(\ce{I2})$ |
| $\ce{C(s)}$, $\ce{O2}$, $\ce{CO}$, $\ce{CO2}$ | 4 | 2 | 0 | 2 | Only two of the three combustion reactions are independent |
| $\ce{NH4Cl(s)}$ decomposing in an evacuated vessel | 3 | 1 | 1 | 1 | In the gas phase $p(\ce{NH3}) = p(\ce{HCl})$ |
| Same, with an arbitrary amount of $\ce{NH3}$ initially in the vessel | 3 | 1 | 0 | 2 | |
| $\ce{CaCO3(s)}$ decomposing in an evacuated vessel | 3 | 1 | 0 | 2 | $\ce{CaO}$ and $\ce{CO2}$ are not in the same phase |
| Aqueous $\ce{HCN}$ | 5 | 2 | 1 | 2 | $\ce{H2O, H+, OH-, HCN, CN-}$; electroneutrality |

The $\ce{CaO}$ and $\ce{CO2}$ produced by the decomposition of $\ce{CaCO3}$ are equal in amount, but they lie in different phases (solid and gas). "Equal amounts of substance" is not an intensive relation within any phase and does not remove any compositional degree of freedom, so it is not a concentration restriction. Likewise, the ratio of concentrations in two phases given by **Nernst distribution law** ([6.3.6](/6.3.6)) is not a concentration restriction: it is a consequence of the condition for phase equilibrium $\mu_{\mathrm{B}}^{\alpha} = \mu_{\mathrm{B}}^{\beta}$, which is already counted in the derivation of the phase rule (§8.2.2), and counting it again would be double counting.

$C$ does not depend on the level of description: counting one more species also adds one more reaction or one more restriction. In the table above the two ways of counting pure water, and the two ways of counting aqueous $\ce{HCN}$ (as molecules, $\ce{H2O}$ and $\ce{HCN}$ with $C = 2$, or as ions), give the same result.

### 8.2.2. The Variance and the Gibbs Phase Rule

**Definition 8.2.2 (Variance)** The number of intensive variables that can be varied independently within some range without changing the phase state of the system (without making an old phase disappear or a new phase appear) is called the **variance** (number of degrees of freedom) of the system and is denoted $F$. It equals the total number of intensive variables needed to describe the system minus the number of independent relations that these variables must satisfy at equilibrium.

**Theorem 8.2.1 (Phase rule)** For a system in thermal, mechanical, phase and chemical equilibrium whose only external intensive variables are temperature and pressure,

$$
F = C - P + 2.
\tag{8.1}
$$

**Proof** First suppose that all $s$ species are present in all $P$ phases. The intensive variables are the temperature $T$, the pressure $p$ (thermal and mechanical equilibrium make $T$ and $p$ the same in all phases) and the composition of each phase; the composition of each phase is described by $s$ mole fractions, but they sum to 1, so only $s - 1$ are independent. The total number of intensive variables is therefore

$$
2 + P(s - 1).
$$
At equilibrium they are related by the following independent relations:

1. The conditions for phase equilibrium (Theorem 8.1.1): the chemical potential of each substance is equal in the $P$ phases, giving $P - 1$ equalities per substance and $s(P - 1)$ in all. The chemical potential is a function of $T$, $p$ and the composition of the phase, so these are equations among the intensive variables.
2. The conditions for chemical equilibrium: each independent reaction satisfies $\sum_{\mathrm{B}} \nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$, $r$ in all.
3. The $r'$ concentration restrictions.

Hence

$$
F = 2 + P(s - 1) - s(P - 1) - r - r' = (s - r - r') - P + 2 = C - P + 2.
$$

If a substance B is absent from some phase, that phase has one composition variable fewer and there is one chemical-potential equality fewer for B; the two changes cancel and the conclusion is unchanged. $\square$

The phase rule is only a count of variables. It involves no property of any specific substance and therefore holds for every system at phase equilibrium. The price is that it tells us how many independent variables there are, but not which ones they are, nor how the phase state changes with the variables; that requires thermodynamic calculation or experiment, and the results are plotted as phase diagrams. From $F \geq 0$ we obtain $P \leq C + 2$: a system with $C$ components can have at most $C + 2$ coexisting phases. Each additional phase removes one degree of freedom; $F$ is largest when $P = 1$ and $P$ is largest when $F = 0$.

The phase rule was given by Gibbs in a long paper, "On the Equilibrium of Heterogeneous Substances", published in two parts in 1875–1878. This paper of more than three hundred pages, written in an abstract mathematical form and published in the obscure Transactions of the Connecticut Academy of Sciences, became widely known only more than ten years later through the translations by Ostwald (German, 1892) and Le Chatelier (French, 1899), and has since become the basic tool for analyzing multiphase systems in metallurgy, geology and chemical engineering.

### 8.2.3. Conditional Variance and the Generalized Phase Rule

The "2" in Eq. (8.1) stands for temperature and pressure, and it assumes that the temperature and the pressure are each the same in all phases. In practice two kinds of modification are common.

**Definition 8.2.3 (Conditional variance)** The number of degrees of freedom that remain after some intensive variables have been fixed by choice is called the **conditional variance** and is denoted $F^*$. At constant pressure (or constant temperature) $F^* = C - P + 1$; at constant temperature and pressure $F^* = C - P$.

**Theorem 8.2.2 (Generalized phase rule)** If, besides the composition, $n$ external intensive variables are needed to determine the state of the system, then $F = C - P + n$.

The value of $n$ requires case-by-case analysis: when the effects of electric, magnetic or gravitational fields cannot be neglected, $n$ is greater than 2; when two parts separated by a semipermeable membrane can have different pressures, the pressure of each part is an independent variable. The properties of condensed systems are insensitive to pressure, so the pressure is often taken as fixed, and then $n = 1$.

**Example 8.2.1** A vessel is divided by a semipermeable membrane that passes only $\ce{O2}$. On the left are $\ce{Ag(s)}$, $\ce{Ag2O(s)}$ and $\ce{O2(g)}$; on the right is a gas mixture of $\ce{O2}$ and $\ce{CCl4}$. Find the variance of the system and the conditional variance at $298\,\mathrm{K}$.

Solution: The species are $\ce{Ag, Ag2O, O2, CCl4}$, so $s = 4$; on the left there is the reaction $\ce{2Ag(s) + 1/2 O2(g) <=> Ag2O(s)}$, so $r = 1$; and $r' = 0$. Hence $C = 3$. The phases are $\ce{Ag(s)}$, $\ce{Ag2O(s)}$, the left gas phase and the right gas phase, so $P = 4$. The pressures on the two sides may differ, so the external intensive variables are $T$, $p_{\text{left}}$ and $p_{\text{right}}$, and $n = 3$. Thus $F = 3 - 4 + 3 = 2$; after the temperature is fixed, $F^* = 1$.

Physically: at a given temperature the pressure of $\ce{O2}$ on the left is fixed by the decomposition equilibrium of $\ce{Ag2O}$ (it is the **decomposition pressure** of $\ce{Ag2O}$, [6.3.7](/6.3.7)); the chemical potentials of $\ce{O2}$ on the two sides of the membrane are equal, so the partial pressure of $\ce{O2}$ on the right is also fixed, but any amount of $\ce{CCl4}$ may be added on the right, so the total pressure (or the mole fraction of $\ce{O2}$) can vary independently, leaving one degree of freedom. If one wrongly used $n = 2$, one would reach the erroneous conclusion $F^* = 3 - 4 + 1 = 0$.

### 8.2.4. Applications of the Phase Rule

**Example 8.2.2** A homogeneous closed one-component system: $F = 1 - 1 + 2 = 2$. Temperature and pressure can vary independently, and other intensive properties such as the molar volume are determined by them (equation of state).

**Example 8.2.3** A pure liquid has a definite boiling point at a given external pressure, whereas a solution does not. For a boiling pure liquid $C = 1$, $P = 2$, and at constant pressure $F^* = 1 - 2 + 1 = 0$. For a boiling two-component solution $C = 2$, $P = 2$ and $F^* = 1$: the boiling point varies with composition, and during boiling it rises as the composition of the liquid changes ([6.3.9](/6.3.9)).

**Example 8.2.4** A saturated aqueous solution of $\ce{NaCl}$ in equilibrium with $\ce{NaCl(s)}$ at $p^\circ$ has $C = 2$, $P = 2$ and $F^* = 2 - 2 + 1 = 1$, so the solubility is a single-valued function of temperature and can be plotted as a solubility curve.

**Example 8.2.5** $\ce{Na2CO3}$ and water form three hydrates, $\ce{Na2CO3.H2O}$, $\ce{Na2CO3.7H2O}$ and $\ce{Na2CO3.10H2O}$. What is the maximum number of hydrates that can coexist in equilibrium with an aqueous $\ce{Na2CO3}$ solution at $p^\circ$?

Solution: The species are $\ce{H2O}$, $\ce{Na2CO3}$ and the three hydrates, so $s = 5$; each hydrate has one formation reaction, so $r = 3$; $C = 5 - 3 = 2$, independent of the number of hydrates. At constant pressure $F^* = 2 - P + 1 = 3 - P \geq 0$, so $P \leq 3$. The solution occupies one phase, so at most two hydrates can coexist with the solution.

## 8.3. Two-Phase Equilibrium of a Pure Substance

For two-phase equilibrium of a pure substance $C = 1$, $P = 2$ and $F = 1$: only one of the temperature and the pressure can vary independently, the equilibrium pressure is a function of temperature, $p = p(T)$, and in the $p$–$T$ diagram it is a curve. Its equation follows directly from the condition for phase equilibrium.

### 8.3.1. The Clapeyron Equation

The chemical potential of a pure substance is its molar Gibbs energy, $\mu^* = G_{\mathrm{m}}$, and by the **fundamental equation of thermodynamics** ([6.3.3](/6.3.3)),

$$
\mathrm{d}\mu^* = -S_{\mathrm{m}}\,\mathrm{d}T + V_{\mathrm{m}}\,\mathrm{d}p .
$$

The slope of a two-phase equilibrium line is given by the *Clapeyron equation*, which Clapeyron obtained in 1834 while extending Carnot's work, and which Clausius later derived rigorously from the second law of thermodynamics.

**Theorem 8.3.1 (Clapeyron equation)** When phases $\alpha$ and $\beta$ of a pure substance coexist in equilibrium, the rate of change of the equilibrium pressure with temperature is

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta_{\mathrm{trs}}S_{\mathrm{m}}}{\Delta_{\mathrm{trs}}V_{\mathrm{m}}} = \frac{\Delta_{\mathrm{trs}}H_{\mathrm{m}}}{T\,\Delta_{\mathrm{trs}}V_{\mathrm{m}}},
\tag{8.2}
$$
where $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = H_{\mathrm{m}}^{\beta} - H_{\mathrm{m}}^{\alpha}$ and $\Delta_{\mathrm{trs}}V_{\mathrm{m}} = V_{\mathrm{m}}^{\beta} - V_{\mathrm{m}}^{\alpha}$ are the molar enthalpy change and molar volume change of the same transition ($\alpha \to \beta$) at temperature $T$ and the equilibrium pressure.

**Proof** At $(T, p)$ the two phases are in equilibrium, $\mu^{\alpha}(T, p) = \mu^{\beta}(T, p)$. Moving along the equilibrium line to the neighboring equilibrium point $(T + \mathrm{d}T, p + \mathrm{d}p)$, the two phases are still in equilibrium, so $\mathrm{d}\mu^{\alpha} = \mathrm{d}\mu^{\beta}$:

$$
-S_{\mathrm{m}}^{\alpha}\,\mathrm{d}T + V_{\mathrm{m}}^{\alpha}\,\mathrm{d}p = -S_{\mathrm{m}}^{\beta}\,\mathrm{d}T + V_{\mathrm{m}}^{\beta}\,\mathrm{d}p ,
$$
that is, $\Delta_{\mathrm{trs}}V_{\mathrm{m}}\,\mathrm{d}p = \Delta_{\mathrm{trs}}S_{\mathrm{m}}\,\mathrm{d}T$. An equilibrium phase transition is a **reversible process** at constant temperature and pressure, with $\Delta_{\mathrm{trs}}S_{\mathrm{m}} = \Delta_{\mathrm{trs}}H_{\mathrm{m}}/T$; substituting gives the result. $\square$

The Clapeyron equation is exact, with no approximation; it applies to any two-phase equilibrium of a pure substance (gas–liquid, gas–solid, liquid–solid, between two crystal forms), provided the transition has an enthalpy change and a volume change. $\Delta_{\mathrm{trs}}H_{\mathrm{m}}$ and $\Delta_{\mathrm{trs}}V_{\mathrm{m}}$ must correspond to the same direction of transition; for a second-order transition with $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = 0$ and $\Delta_{\mathrm{trs}}V_{\mathrm{m}} = 0$, Eq. (8.2) becomes of the type $0/0$ and the Ehrenfest equations must be used instead (§8.4.2).

The **enthalpy of transition** is always positive from the low-temperature phase to the high-temperature phase (melting, vaporization and sublimation are all endothermic), so the sign of the slope of the equilibrium line is determined by $\Delta_{\mathrm{trs}}V_{\mathrm{m}}$: the slope is positive when the high-temperature phase has the larger volume (the melting curves of most substances) and negative when it is smaller (the melting curves of water, Bi, Ga and Si).

### 8.3.2. Gas–Liquid and Gas–Solid Equilibrium

For vaporization and sublimation we make two approximations: the molar volume of the condensed phase is much smaller than that of the gas, $\Delta V_{\mathrm{m}} \approx V_{\mathrm{m}}(\mathrm{g})$; and the vapor is an ideal gas, $V_{\mathrm{m}}(\mathrm{g}) = RT/p$. Substituting into Eq. (8.2) gives the **Clausius–Clapeyron equation** ([Theorem 1.2.2](/6.1.1#thm-1.2.2) of [6.1.1](/6.1.1#sec-1.2.2)):

$$
\frac{\mathrm{d}\ln(p/p^\circ)}{\mathrm{d}T} = \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{RT^2}.
\tag{8.3}
$$

The pressure inside the logarithm is divided by a unit of pressure (here $p^\circ$, which does not affect the derivative). Near the normal boiling point both approximations have errors of only a few percent: at $100\,{}^\circ\mathrm{C}$ the molar volume of liquid water is about $1/1600$ that of the vapor, and the compressibility factor of water vapor is about $0.985$. The closer to the **critical point**, the worse the approximations become; at the critical point $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ and $\Delta V_{\mathrm{m}}$ tend to zero together.

When $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ can be taken as constant, integration gives

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right),
\tag{8.4}
$$
so $\ln p$ is linear in $1/T$; this is the basis for determining the **molar enthalpy of vaporization** from vapor pressures ([6.1.1](/6.1.1) has examples of plotting and regression). Over a wide temperature range the temperature dependence of the enthalpy of vaporization must be taken into account. By **Kirchhoff's law** ([6.3.1](/6.3.1)), over a range in which $\Delta C_{p,\mathrm{m}} = C_{p,\mathrm{m}}(\mathrm{g}) - C_{p,\mathrm{m}}(\mathrm{l})$ may be taken as constant,

$$
\Delta_{\mathrm{vap}}H_{\mathrm{m}}(T) = \Delta H_0 + \Delta C_{p,\mathrm{m}}T, \qquad \Delta H_0 = \Delta_{\mathrm{vap}}H_{\mathrm{m}}(T_1) - \Delta C_{p,\mathrm{m}}T_1 ,
$$
and substituting into Eq. (8.3) and integrating gives

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta H_0}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) + \frac{\Delta C_{p,\mathrm{m}}}{R}\ln\frac{T_2}{T_1}.
\tag{8.5}
$$
In general, empirical equations of the form $\ln p = A - B/T + C\ln T$ come from this integral; precise vapor-pressure data are often fitted with the Antoine equation $\lg p = A - B/(T + C)$.

**Example 8.3.1** The normal boiling point of water is $373.12\,\mathrm{K}$, and at this temperature $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$. Estimate the saturated vapor pressure of water at $30\,{}^\circ\mathrm{C}$ (measured value $4.247\,\mathrm{kPa}$).

Solution: (1) Taking $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ as constant, Eq. (8.4) gives

$$
\ln\frac{p_2}{101.325\,\mathrm{kPa}} = -\frac{40650}{8.314}\left(\frac{1}{303.15} - \frac{1}{373.12}\right) = -3.025, \qquad p_2 = 4.92\,\mathrm{kPa},
$$
which is 16% too high. The reason is that the enthalpy of vaporization is larger at lower temperatures (the actual value at $30\,{}^\circ\mathrm{C}$ is $43.8\,\mathrm{kJ\,mol^{-1}}$); extrapolating from the boiling point to lower temperatures with too small an enthalpy of vaporization makes the vapor pressure fall too little.

(2) Taking $C_{p,\mathrm{m}}(\mathrm{H_2O, g}) = 33.6$ and $C_{p,\mathrm{m}}(\mathrm{H_2O, l}) = 75.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$, so that $\Delta C_{p,\mathrm{m}} = -41.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$, Eq. (8.5) gives $p_2 = 4.38\,\mathrm{kPa}$, and the error drops to 3%. The remaining error comes mainly from the nonideality of water vapor and the temperature dependence of $\Delta C_{p,\mathrm{m}}$.

![Left: vapor pressure of water from 0 to 100 °C on a logarithmic scale, comparing the IAPWS reference curve with Clausius–Clapeyron integrated from the normal boiling point with a constant enthalpy of vaporization and with a temperature-dependent one (Kirchhoff's law). Right: relative errors of the two approximations; the constant-enthalpy form overestimates the pressure by up to 37 % at 0 °C, the Kirchhoff-corrected form by less than 5 %](./plots/clausius-clapeyron-accuracy.py)

Many normal liquids (nonpolar, with unassociated molecules) have similar molar entropies of vaporization at the normal boiling point; **Trouton's rule** ([6.1.1](/6.1.1)) gives $\Delta_{\mathrm{vap}}H_{\mathrm{m}}/T_{\mathrm{b}} \approx 85$–$88\,\mathrm{J\,mol^{-1}\,K^{-1}}$, which can be used to estimate the enthalpy of vaporization when data are lacking. Its meaning is that, at the same vapor density ($1\,\mathrm{atm}$), molecules gain roughly the same "positional freedom" in passing from liquid to gas; hydrogen bonding in water and alcohols makes the liquid more ordered, so the entropy of vaporization is larger.

Replacing the enthalpy of vaporization in Eq. (8.3) by the enthalpy of sublimation gives the vapor-pressure equation of a solid. At the **triple point**, the sublimation curve of ice and the vaporization curve of water have the same pressure, and the ratio of their slopes is

$$
\frac{(\mathrm{d}p/\mathrm{d}T)_{\mathrm{sub}}}{(\mathrm{d}p/\mathrm{d}T)_{\mathrm{vap}}} = \frac{\Delta_{\mathrm{sub}}H_{\mathrm{m}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m}}} = \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m}} + \Delta_{\mathrm{vap}}H_{\mathrm{m}}}{\Delta_{\mathrm{vap}}H_{\mathrm{m}}} = \frac{6.01 + 45.05}{45.05} = 1.13,
$$
so the sublimation curve is steeper; in linear $p$–$T$ coordinates both curves bend upward ($\mathrm{d}p/\mathrm{d}T = p\,\Delta H_{\mathrm{m}}/(RT^2)$ increases with $p$).

### 8.3.3. Solid–Liquid Equilibrium

On melting, $\Delta_{\mathrm{fus}}V_{\mathrm{m}}$ is very small, so Eq. (8.2) gives a very large slope and the melting curve is almost vertical. If $\Delta_{\mathrm{fus}}H_{\mathrm{m}}$ and $\Delta_{\mathrm{fus}}V_{\mathrm{m}}$ can be taken as constant, separating variables and integrating gives

$$
\ln\frac{T_2}{T_1} = \frac{\Delta_{\mathrm{fus}}V_{\mathrm{m}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m}}}(p_2 - p_1),
$$
which for small pressure changes is approximately $\Delta T \approx T\,\Delta_{\mathrm{fus}}V_{\mathrm{m}}\,\Delta p/\Delta_{\mathrm{fus}}H_{\mathrm{m}}$.

**Example 8.3.2** At $0\,{}^\circ\mathrm{C}$ the densities of ice and water are $0.9167$ and $0.99984\,\mathrm{g\,cm^{-3}}$, and $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$. Find the rate of change of the melting point of ice with pressure.

Solution: $\Delta_{\mathrm{fus}}V_{\mathrm{m}} = M(1/\rho_{\mathrm{l}} - 1/\rho_{\mathrm{s}}) = 18.015 \times (1.0002 - 1.0909)\,\mathrm{cm^3\,mol^{-1}} = -1.634\,\mathrm{cm^3\,mol^{-1}}$,

$$
\frac{\mathrm{d}T}{\mathrm{d}p} = \frac{T\,\Delta_{\mathrm{fus}}V_{\mathrm{m}}}{\Delta_{\mathrm{fus}}H_{\mathrm{m}}} = \frac{273.15 \times (-1.634 \times 10^{-6})}{6010}\,\mathrm{K\,Pa^{-1}} = -7.43 \times 10^{-8}\,\mathrm{K\,Pa^{-1}},
$$
that is, for each increase of $1\,\mathrm{MPa}$ (about 10 atm) the melting point falls by about $0.074\,\mathrm{K}$; conversely, a pressure of about $13.5\,\mathrm{MPa}$ is needed to lower the melting point by $1\,\mathrm{K}$.

"The high pressure under the skate blade melts the ice and forms a film of water" is a widely repeated explanation of ice skating, but the numbers of Example 8.3.2 show that it does not hold: a person weighing about $700\,\mathrm{N}$ standing on a blade with a contact area of about $1\,\mathrm{cm^2}$ exerts a pressure of about $7\,\mathrm{MPa}$, which lowers the melting point by only about $0.5\,\mathrm{K}$ and cannot explain why ice is still slippery at $-20\,{}^\circ\mathrm{C}$. The main role is now attributed to the ice surface itself: water molecules at the surface have half as many hydrogen bonds as those in the bulk, so over a wide range of temperatures below the melting point there is a highly mobile surface layer (surface premelting), and frictional heating during sliding strengthens the effect. The structure of the surface layer (whether it can be called a liquid film, and how thick it is) is still under study; friction and spectroscopy experiments by Bonn and coworkers in 2018–2021 indicate that the lubrication comes from highly mobile surface molecules rather than from a macroscopic water film produced by pressure melting.

### 8.3.4. The Effect of External Pressure on Vapor Pressure

When, besides its own vapor, there is an inert gas (for example air) above a liquid that does not dissolve in it, the total pressure $p_{\mathrm{e}}$ on the liquid exceeds the partial pressure $p_{\mathrm{v}}$ of its vapor. The system then contains two components, the liquid and the inert gas, with $C = 2$, $P = 2$ and $F = 2$: the temperature and the total pressure on the liquid can both be changed independently, and the vapor pressure is a function of both, $p_{\mathrm{v}}(T, p_{\mathrm{e}})$. The effect of temperature is described by the Clausius–Clapeyron equation; the effect of external pressure is as follows.

**Theorem 8.3.2** At constant temperature, the saturated vapor pressure of a liquid varies with the pressure on the liquid according to

$$
\left(\frac{\partial p_{\mathrm{v}}}{\partial p_{\mathrm{e}}}\right)_T = \frac{V_{\mathrm{m}}(\mathrm{l})}{V_{\mathrm{m}}(\mathrm{g})};
$$
for an ideal-gas vapor and an incompressible liquid,

$$
\ln\frac{p_{\mathrm{v}}}{p_{\mathrm{v}}^*} = \frac{V_{\mathrm{m}}(\mathrm{l})\,(p_{\mathrm{e}} - p_{\mathrm{v}}^*)}{RT},
\tag{8.6}
$$
where $p_{\mathrm{v}}^*$ is the saturated vapor pressure when the liquid is subject only to its own vapor pressure.

**Proof** At equilibrium $\mu(\mathrm{l}, T, p_{\mathrm{e}}) = \mu(\mathrm{g}, T, p_{\mathrm{v}})$. Changing the external pressure at constant temperature, the changes of the two sides are equal: $V_{\mathrm{m}}(\mathrm{l})\,\mathrm{d}p_{\mathrm{e}} = V_{\mathrm{m}}(\mathrm{g})\,\mathrm{d}p_{\mathrm{v}}$, which is the first relation. Substituting $V_{\mathrm{m}}(\mathrm{g}) = RT/p_{\mathrm{v}}$ gives $\mathrm{d}\ln p_{\mathrm{v}} = V_{\mathrm{m}}(\mathrm{l})\,\mathrm{d}p_{\mathrm{e}}/(RT)$, and integrating from $p_{\mathrm{e}} = p_{\mathrm{v}}^*$ to $p_{\mathrm{e}}$ gives Eq. (8.6). $\square$

Increasing the external pressure increases the vapor pressure, but only slightly, because $V_{\mathrm{m}}(\mathrm{l}) \ll V_{\mathrm{m}}(\mathrm{g})$. At $25\,{}^\circ\mathrm{C}$, raising the external pressure on water by $1\,\mathrm{bar}$ increases the vapor pressure by only $0.07\%$; raising it by $10\,\mathrm{MPa}$ increases it by about $7.6\%$. The vapor pressure of a liquid in the presence of air is therefore usually taken as the saturated vapor pressure of the pure liquid. The form of Eq. (8.6) will reappear twice later: the **osmotic pressure** of a solution is the pressure applied on the solution side to raise the chemical potential of the solvent back to the value of the pure solvent ([6.3.5](/6.3.5)); and the additional pressure in a small droplet makes its vapor pressure higher than that of a planar liquid, which is the **Kelvin equation** ([6.3.19](/6.3.19)).

## 8.4. Classification of Phase Transitions

### 8.4.1. First-Order Transitions

At two-phase equilibrium the chemical potentials are equal, but their partial derivatives with respect to $T$ and $p$ are not necessarily equal. In Ehrenfest's classification (1933) one asks which derivative of the chemical potential is discontinuous at the transition point.

**Definition 8.4.1 (First-order transition)** A phase transition at which the chemical potential is continuous but its first partial derivatives

$$
\left(\frac{\partial\mu}{\partial T}\right)_p = -S_{\mathrm{m}}, \qquad \left(\frac{\partial\mu}{\partial p}\right)_T = V_{\mathrm{m}}
$$
change abruptly is called a **first-order phase transition**. A first-order transition has an enthalpy of transition $\Delta_{\mathrm{trs}}H_{\mathrm{m}} = T\,\Delta_{\mathrm{trs}}S_{\mathrm{m}} \neq 0$ and a volume change $\Delta_{\mathrm{trs}}V_{\mathrm{m}} \neq 0$, and the two-phase equilibrium line obeys the Clapeyron equation.

Melting, vaporization, sublimation and most transitions between crystal forms are first-order transitions. On the two sides of a first-order transition point, the $\mu$–$T$ curves of the two phases cross with different slopes: below the transition temperature one phase has the lower chemical potential and is more stable, and above it the other phase is more stable; the continuation of a curve beyond the crossing point corresponds to a metastable state such as a liquid in a state of **supercooling** or a superheated liquid. At the transition point the heat capacity shows a peak in the form of a $\delta$ function (latent heat is absorbed at constant temperature); this is the kind of peak measured by **differential scanning calorimetry** ([6.3.1](/6.3.1)).

### 8.4.2. Second-Order Transitions and the Ehrenfest Equations

**Definition 8.4.2 (Second-order transition)** A phase transition at which the chemical potential and its first partial derivatives are all continuous ($\Delta_{\mathrm{trs}}S_{\mathrm{m}} = 0$, $\Delta_{\mathrm{trs}}V_{\mathrm{m}} = 0$, no enthalpy of transition), while the second partial derivatives

$$
\left(\frac{\partial^2\mu}{\partial T^2}\right)_p = -\frac{C_{p,\mathrm{m}}}{T}, \qquad \left(\frac{\partial^2\mu}{\partial p^2}\right)_T = -V_{\mathrm{m}}\kappa_T, \qquad \frac{\partial^2\mu}{\partial T\,\partial p} = V_{\mathrm{m}}\alpha_V
$$
undergo finite jumps is called a **second-order phase transition**. By extension, a transition at which the $n$th derivative is the first to be discontinuous is called an $n$th-order transition.

Here $\alpha_V$ is the **expansion coefficient** (at constant pressure) and $\kappa_T$ is the **isothermal compressibility** ([6.3.3](/6.3.3)). The equation of a second-order equilibrium line cannot be obtained from the Clapeyron equation; it must start from the condition that $S_{\mathrm{m}}$ and $V_{\mathrm{m}}$ are continuous along the transition line.

**Theorem 8.4.1 (Ehrenfest equations)** Along a second-order transition line,

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta C_{p,\mathrm{m}}}{TV_{\mathrm{m}}\,\Delta\alpha_V}, \qquad \frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta\alpha_V}{\Delta\kappa_T},
$$
where $\Delta$ denotes the difference between the two phases.

**Proof** Regard $S_{\mathrm{m}}$ as a function of $T$ and $p$. By the **Maxwell relations**, $(\partial S_{\mathrm{m}}/\partial p)_T = -(\partial V_{\mathrm{m}}/\partial T)_p = -V_{\mathrm{m}}\alpha_V$,

$$
\mathrm{d}S_{\mathrm{m}} = \frac{C_{p,\mathrm{m}}}{T}\,\mathrm{d}T - V_{\mathrm{m}}\alpha_V\,\mathrm{d}p .
$$
Along the transition line $S_{\mathrm{m}}^{\alpha} = S_{\mathrm{m}}^{\beta}$ holds throughout, so $\mathrm{d}S_{\mathrm{m}}^{\alpha} = \mathrm{d}S_{\mathrm{m}}^{\beta}$; the $V_{\mathrm{m}}$ of the two phases are equal at the transition point, so $\Delta C_{p,\mathrm{m}}\,\mathrm{d}T/T = V_{\mathrm{m}}\,\Delta\alpha_V\,\mathrm{d}p$, which is the first equation. Similarly, $\mathrm{d}V_{\mathrm{m}} = V_{\mathrm{m}}\alpha_V\,\mathrm{d}T - V_{\mathrm{m}}\kappa_T\,\mathrm{d}p$ and $\mathrm{d}V_{\mathrm{m}}^{\alpha} = \mathrm{d}V_{\mathrm{m}}^{\beta}$ give the second. $\square$

The two equations can also be viewed as the result of applying L'Hôpital's rule to the $0/0$ form of the Clapeyron equation $\mathrm{d}p/\mathrm{d}T = \Delta S_{\mathrm{m}}/\Delta V_{\mathrm{m}}$: differentiating numerator and denominator with respect to $T$ gives the first, and with respect to $p$ the second.

### 8.4.3. Continuous Transitions

A typical example of a second-order transition in the Ehrenfest sense is the transition of a metal to **superconductivity** in zero magnetic field ([5.3.9](/5.3.9#sec-9.7)): at the critical temperature the electrical resistance vanishes, the entropy is continuous and the heat capacity has a finite jump, in agreement with the prediction of BCS theory.

But most transitions of this kind do not fit Ehrenfest's picture. Liquid helium ($^4\mathrm{He}$) changes at $2.17\,\mathrm{K}$ from the ordinary liquid He I to the superfluid He II with no enthalpy of transition, but its heat capacity diverges logarithmically on both sides of the transition point, with a shape like the Greek letter $\lambda$, hence the name lambda transition. The loss of spontaneous magnetization of a ferromagnet at the **Curie temperature** ([5.3.8](/5.3.8#sec-8.5.4)), the order–disorder transition of alloys (such as $\beta$-brass, CuZn) and the transitions of some **liquid crystals** (such as smectic A to nematic) also belong to this class. When the heat capacity diverges, the statement of "a finite jump in the second derivative" no longer applies, so modern literature no longer uses Ehrenfest's higher-order classification and distinguishes only first-order transitions and continuous transitions (the **second-order phase transition** in the broad sense). The former have latent heat and two coexisting phases; in the latter there is no latent heat, a quantity describing the degree of order (the order parameter, such as the spontaneous magnetization or the fraction of the superfluid component) falls continuously to zero at the transition point, fluctuations near the transition point are large, and various properties vary as power laws (critical phenomena). The gas–liquid critical point is a continuous transition point: at the critical point the enthalpy of vaporization and $\Delta V_{\mathrm{m}}$ tend to zero together. The unified theory of critical phenomena (Landau theory and the renormalization group) belongs to statistical physics.

![Schematic molar Gibbs energy (chemical potential), molar entropy and heat capacity against temperature at constant pressure for a first-order transition (kinked μ, entropy jump equal to the enthalpy of transition divided by T, delta-function peak in Cp), an Ehrenfest second-order transition (continuous μ and S, finite jump in Cp) and a lambda transition (Cp diverges on both sides)](./plots/transition-order.py)

When heated, the phospholipid bilayer of a biological membrane changes from an ordered gel phase to a liquid-crystalline phase with disordered hydrocarbon chains (the main transition, about $41\,{}^\circ\mathrm{C}$ for dipalmitoylphosphatidylcholine, DPPC). This is a weak first-order transition, and the sharp endothermic peak measured by differential scanning calorimetry shows that the transition is highly cooperative; cells regulate the length and degree of unsaturation of the fatty acid chains so that the membrane remains fluid at physiological temperature ([7.6](/7.6)).

## 8.5. Phase Diagrams of One-Component Systems

For a one-component system $C = 1$ and $F = 3 - P$. The minimum of $P$ is 1, so $F \leq 2$, and the two variables $p$ and $T$ suffice to show the phase relations completely: the **phase diagram** is a plane figure. $F \geq 0$ gives $P \leq 3$, so at most three phases of a one-component system can coexist.

| Number of phases | Variance | In the $p$–$T$ diagram |
|---|---|---|
| $P = 1$ | $F = 2$ | Area (single-phase region) |
| $P = 2$ | $F = 1$ | Line (two-phase equilibrium line, whose equation is the Clapeyron equation) |
| $P = 3$ | $F = 0$ | Point (triple point) |

### 8.5.1. The Phase Diagram of Water

In the low- and moderate-pressure range the phase diagram of water has three curves that divide the plane into three single-phase regions: ice, liquid water and water vapor:

- The vaporization curve (liquid–gas equilibrium line) is the curve of the **saturated vapor pressure** of water; it extends upward from the triple point and ends at the critical point, $647.096\,\mathrm{K}$ and $22.064\,\mathrm{MPa}$ (IAPWS-95). At the critical point the difference between liquid and gas vanishes and the curve cannot be extended further.
- The sublimation curve (solid–gas equilibrium line) is the saturated vapor pressure curve of ice; near the triple point it is steeper than the vaporization curve (§8.3.2).
- The melting curve (solid–liquid equilibrium line) has a negative slope and is almost vertical (Example 8.3.2): the melting point of ice decreases as the pressure increases. The melting point of ice Ih falls at most to $251.165\,\mathrm{K}$ ($208.6\,\mathrm{MPa}$), after which it meets ice III.
- The extension of the vaporization curve beyond the triple point to lower temperatures is the saturated vapor pressure curve of supercooled water. It lies above the sublimation curve of ice at the same temperature: at the same temperature supercooled water has a higher vapor pressure, and also a higher chemical potential, than ice, so supercooled water is metastable and freezes as soon as a crystal nucleus appears.

![Phase diagram of water on a logarithmic pressure axis computed from the IAPWS correlations: sublimation, vaporization (ending at the critical point 647.096 K, 22.064 MPa) and melting curves; the melting curve of ordinary ice Ih is almost vertical with a negative slope, and at high pressure the melting curves of ices III, V, VI and VII follow (boundaries between the solid phases are omitted). The dashed line is the vapor pressure of supercooled water](./plots/water-phase-diagram.py)

The uses of a phase diagram are to read off, for given conditions, which phase the system is in, and to predict how the phase state changes when conditions change. For example, when ice is heated at constant pressure $p^\circ$ from $-10\,{}^\circ\mathrm{C}$, the representative point moves along a horizontal line and crosses first the melting curve ($0\,{}^\circ\mathrm{C}$, ice and water coexist, $F^* = 0$, and the temperature stays constant until all the ice has melted) and then the vaporization curve ($99.61\,{}^\circ\mathrm{C}$, water and water vapor coexist). When ice is heated at a pressure below that of the triple point, the representative point crosses only the sublimation curve and ice turns directly into water vapor without melting, so a necessary condition for the sublimation of ice is a pressure below the triple-point pressure $611.657\,\mathrm{Pa}$. Freeze-drying makes use of exactly this: a water-containing sample is frozen and the ice is sublimed at a pressure below the triple point; the sample never passes through the liquid state, so the structure and activity of proteins, vaccines, bacterial cultures and foods are preserved.

### 8.5.2. The Triple Point and the Freezing Point

The triple point of water is the only state in which ice, water and water vapor coexist, with $C = 1$, $P = 3$, $F = 0$: $273.16\,\mathrm{K}$ and $611.657\,\mathrm{Pa}$. It is a property of pure water itself and does not change with external conditions, so from 1954 it was used to define the thermodynamic temperature scale (fixed at exactly $273.16\,\mathrm{K}$). The precise measurement by Beattie, Huang Zi-Qing and Benedict in 1938 (the triple point is $0.00981\,{}^\circ\mathrm{C}$ above the ice point) was one of the bases of this choice. Since the SI revision of 2019 the kelvin has been defined by fixing the **Boltzmann constant** $k_{\mathrm{B}}$ ([5.2.1](/5.2.1)); the triple-point temperature has become a measured value, which is still $273.16\,\mathrm{K}$ within the present precision.

The freezing point (ice point) is the temperature at which air-saturated water and ice coexist in equilibrium in air at $101.325\,\mathrm{kPa}$; it is $273.15\,\mathrm{K}$, about $0.0098\,\mathrm{K}$ below the triple point. The system then contains two components, water and air, with $C = 2$, $P = 3$ (ice, water with dissolved air, moist air) and $F = 1$; once the pressure is specified, $F^* = 0$: the freezing point varies with pressure. The difference between the two temperatures has two causes:

1. The pressure increases from $611.657\,\mathrm{Pa}$ to $101.325\,\mathrm{kPa}$, and by Example 8.3.2 the melting point decreases by $7.43 \times 10^{-8}\,\mathrm{K\,Pa^{-1}} \times 1.007 \times 10^{5}\,\mathrm{Pa} = 0.0075\,\mathrm{K}$;
2. Air is dissolved in the water (about $1.3\,\mathrm{mmol\,kg^{-1}}$ at $0\,{}^\circ\mathrm{C}$), and by the **freezing-point depression** of dilute solutions ([6.3.5](/6.3.5)) the melting point falls by a further $1.86 \times 0.0013\,\mathrm{K} = 0.0024\,\mathrm{K}$.

### 8.5.3. Ice at High Pressure

At pressures above about $200\,\mathrm{MPa}$ ordinary hexagonal ice Ih is no longer stable, and the hydrogen-bond network is compressed into denser structures. About 20 crystalline phases of ice have been identified so far (ice Ih, Ic, ice II to ice XIX, etc.); those in contact with liquid water and appearing on the melting curve are ice Ih, III, V, VI and VII. The melting curves of the high-pressure ice phases have positive slopes (all of them are denser than liquid water): ice VI melts at room temperature at about $1\,\mathrm{GPa}$, and ice VII at $10\,\mathrm{GPa}$ does not melt until about $600\,\mathrm{K}$, so "hot ice" exists. These high-pressure ice phases are believed to exist deep inside icy moons such as Ganymede and Titan and in the interiors of some exoplanets.

### 8.5.4. CO₂ and Supercritical Fluids

The phase diagram of $\ce{CO2}$ ([6.1.1](/6.1.1) has a figure) resembles that of water in shape, but its melting curve has a positive slope and its triple-point pressure, $518\,\mathrm{kPa}$, is higher than atmospheric pressure: at normal pressure dry ice sublimes directly at $194.7\,\mathrm{K}$, and liquid $\ce{CO2}$ can exist only under pressure ($\ce{CO2}$ in a cylinder is a liquid at room temperature). The critical point of $\ce{CO2}$ is $304.13\,\mathrm{K}$ and $7.377\,\mathrm{MPa}$.

Above the critical temperature a gas cannot be liquefied however great the pressure; a state with both temperature and pressure above the critical values is a **supercritical fluid** ([6.1.1](/6.1.1)). A supercritical fluid has a density close to that of a liquid and strong dissolving power; a viscosity close to that of a gas and a diffusion coefficient about 10 times that of a liquid, so mass transfer is fast; near the critical point (where the isothermal compressibility is very large) small changes in pressure or temperature change the density and the dissolving power greatly, so the dissolving power can be "switched" by adjusting the pressure. The main applications are:

- Supercritical $\ce{CO2}$ extraction: the critical temperature of $\ce{CO2}$ is close to room temperature, and $\ce{CO2}$ is nontoxic, nonflammable and leaves no residue. It is used to remove caffeine from coffee beans (about $70$–$90\,{}^\circ\mathrm{C}$ and $16$–$20\,\mathrm{MPa}$, reducing the caffeine content from about 3% to about 0.02%) and to extract flavors and pharmaceutical components from hops and plants; on depressurization the solute separates out automatically.
- Supercritical water oxidation: supercritical water ($400$–$600\,{}^\circ\mathrm{C}$, $25$–$40\,\mathrm{MPa}$) has a very small dielectric constant and is completely miscible with organic compounds and oxygen. Organic waste is oxidized to $\ce{CO2}$ and water in about a minute with a removal efficiency above 99.99%, and the heat of reaction can sustain the process; compared with incineration the temperature is much lower and no dioxins or nitrogen oxides are produced.
- Supercritical fluid chromatography, supercritical drying (for preparing aerogels, avoiding the collapse of the porous structure by surface tension during evaporation of a liquid) and polymerization under supercritical conditions.

## Summary

| Topic | Key points |
|---|---|
| Condition for phase equilibrium | Each substance has the same chemical potential in every phase in which it is present |
| Number of components | $C = s - r - r'$; a concentration restriction must be a relation within a single phase; the distribution law and equal amounts of substances in different phases do not count |
| Phase rule | $F = C - P + 2$; at constant pressure or temperature $F^* = C - P + 1$; generalized $F = C - P + n$; $P_{\max} = C + 2$ |
| Clapeyron equation | $\mathrm{d}p/\mathrm{d}T = \Delta_{\mathrm{trs}}H_{\mathrm{m}}/(T\,\Delta_{\mathrm{trs}}V_{\mathrm{m}})$; exact, valid for any first-order transition of a pure substance |
| Clausius–Clapeyron equation | Neglecting the volume of the condensed phase and taking the vapor as ideal: $\mathrm{d}\ln p/\mathrm{d}T = \Delta_{\mathrm{vap}}H_{\mathrm{m}}/(RT^2)$; over a wide temperature range correct with Kirchhoff's law |
| External pressure and vapor pressure | $\ln(p_{\mathrm{v}}/p_{\mathrm{v}}^*) = V_{\mathrm{m}}(\mathrm{l})(p_{\mathrm{e}} - p_{\mathrm{v}}^*)/(RT)$; a very small effect |
| Classification of transitions | First order: abrupt change in $S$ and $V$, latent heat; second order: finite jumps in $C_p$, $\alpha_V$, $\kappa_T$, Ehrenfest equations; modern classification: first-order and continuous |
| Phase diagram of water | Triple point $273.16\,\mathrm{K}$, $611.657\,\mathrm{Pa}$; freezing point $273.15\,\mathrm{K}$; critical point $647.096\,\mathrm{K}$, $22.064\,\mathrm{MPa}$; melting curve with negative slope |
