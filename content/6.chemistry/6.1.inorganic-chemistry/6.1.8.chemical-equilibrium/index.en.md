---
title: Chemical Equilibrium
source_hash: 6abc80c771ef
---

[6.1.6](/6.1.6) gave the criterion for the direction of a reaction: at constant temperature and pressure, with no **non-expansion work**, a reaction with $\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$ can proceed spontaneously. Most reactions, however, do not go to completion but stop at a state in which reactants and products coexist, after which the macroscopic composition no longer changes. This state has two equivalent descriptions. Kinetically ([6.1.7](/6.1.7)), the rates of the forward and reverse reactions are equal; thermodynamically, the **Gibbs free energy** of the system passes through a minimum as a function of the extent of reaction, so that $\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$. This chapter first describes chemical equilibrium and the equilibrium constant (8.1, 8.2), then derives from thermodynamics the reaction isotherm and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ (8.3), which connects the thermodynamic data of Chapter 6 with equilibrium compositions, and finally discusses the effects of concentration, pressure, and temperature on equilibrium (8.4). The standard equilibrium constant and the isotherm of this chapter are the common basis of the four great equilibria that follow (acid–base, complexation, precipitation, and redox, [6.1.9](/6.1.9)–[6.1.12](/6.1.12)). A rigorous treatment of chemical potential, activity coefficients and fugacity, and phase equilibria and the phase rule is given in [Physical Chemistry](/6.3).

## 8.1. Reversible Reactions and Chemical Equilibrium

**Definition 8.1.1** A reaction that can proceed both in the forward and in the reverse direction under the same conditions is called a **reversible reaction**, denoted by $\ce{<=>}$.

Strictly speaking, almost all reactions are reversible, and they differ only in the strength of the tendency of the reverse reaction:

| Reaction | Situation |
|---|---|
| $\ce{2KClO3 ->[MnO2] 2KCl + 3O2}$ (heating) | the product $\ce{O2}$ escapes, so the reaction can go to completion |
| $\ce{Ag+ + Cl- -> AgCl(s)}$ | the tendency of the reverse reaction (dissolution) is very weak, and the reaction goes almost to completion |
| $\ce{CO(g) + H2O(g) <=> CO2(g) + H2(g)}$ | neither direction is complete |
| $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$ | neither direction is complete |
| $\ce{N2O4(g) <=> 2NO2(g)}$ | neither direction is complete |

Put $0.100\,\mathrm{mol\,L^{-1}}$ of $\ce{N2O4}$ (colorless) in a closed vessel at $373\,\mathrm{K}$; it decomposes to $\ce{NO2}$ (red-brown):

| $t/\mathrm{s}$ | 0 | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|---|
| $c(\ce{N2O4})/(\mathrm{mol\,L^{-1}})$ | 0.100 | 0.070 | 0.050 | 0.040 | 0.040 | 0.040 |
| $c(\ce{NO2})/(\mathrm{mol\,L^{-1}})$ | 0 | 0.060 | 0.100 | 0.120 | 0.120 | 0.120 |

The reaction cannot go to completion: at most $0.060\,\mathrm{mol}$ of $\ce{N2O4}$ per liter decomposes. After 60 s the concentrations no longer change, but the reaction has not stopped: the forward reaction continues to form $\ce{NO2}$, and the reverse reaction converts it back to $\ce{N2O4}$ at the same rate.

**Definition 8.1.2 (Chemical Equilibrium)** The state of a closed system at constant temperature (and pressure or volume) in which the rate of the forward reaction of a reversible reaction equals the rate of the reverse reaction is called **chemical equilibrium**.

Chemical equilibrium is the special case of the **equilibrium state** ([5.2.1](/5.2.1#def-1.1.2)) for a system with chemical reactions, and its characteristics are:

1. Premise: constant temperature, a closed system, a reversible reaction.
2. Condition: the forward and reverse rates are equal; it is a dynamic equilibrium.
3. Sign: the concentrations of all species no longer change with time, and the reaction has reached its maximum extent under the given conditions.
4. Chemical equilibrium is conditional: when the external conditions change, the forward and reverse rates are no longer equal, the original equilibrium is destroyed, and a new equilibrium is established under the new conditions (8.4).

Let us see how the equilibrium constant arises from kinetics. Suppose both the forward and the reverse reactions of $a\mathrm{A} + b\mathrm{B} \ce{<=>} g\mathrm{G} + h\mathrm{H}$ are **elementary reactions**. By the **law of mass action** ([6.1.7](/6.1.7)), at equilibrium

$$
k_+c_{\mathrm{A}}^ac_{\mathrm{B}}^b = k_-c_{\mathrm{G}}^gc_{\mathrm{H}}^h \quad\Longrightarrow\quad \frac{c_{\mathrm{G}}^gc_{\mathrm{H}}^h}{c_{\mathrm{A}}^ac_{\mathrm{B}}^b} = \frac{k_+}{k_-}.
$$
The ratio of concentrations on the left is a constant at a given temperature, independent of the initial concentrations. For a complex reaction, at equilibrium the forward and reverse rates of each of its elementary steps are separately equal (**detailed balance**, a principle that is also the condition for constructing a stationary distribution in Markov chain Monte Carlo, [3.5.9](/3.5.9)), and the overall concentration ratio equals the product of the $k_+/k_-$ of the steps, so the conclusion is the same. Thermodynamics gives a proof that does not depend on the mechanism (8.3).

## 8.2. The Equilibrium Constant

### 8.2.1. The Empirical Equilibrium Constant

Establish the equilibrium $\ce{N2O4 <=> 2NO2}$ at $373\,\mathrm{K}$ from different initial compositions:

| Experiment | Initial $c(\ce{NO2})$ | Initial $c(\ce{N2O4})$ | Equilibrium $[\ce{NO2}]$ | Equilibrium $[\ce{N2O4}]$ | $[\ce{NO2}]^2/[\ce{N2O4}]$ |
|---|---|---|---|---|---|
| 1 | 0.000 | 0.100 | 0.120 | 0.040 | 0.36 |
| 2 | 0.100 | 0.000 | 0.072 | 0.014 | 0.37 |
| 3 | 0.100 | 0.100 | 0.160 | 0.070 | 0.36 |

(Concentrations in $\mathrm{mol\,L^{-1}}$; in this chapter $[\mathrm{B}]$ denotes an equilibrium concentration and $c_{\mathrm{B}}$ the concentration at an arbitrary time.) Whether we start from the forward or the reverse direction, equilibrium is reached in the end and $[\ce{NO2}]^2/[\ce{N2O4}]$ is the same; when the temperature changes, this ratio changes with it.

**Definition 8.2.1** For a reversible reaction $a\mathrm{A} + b\mathrm{B} \ce{<=>} g\mathrm{G} + h\mathrm{H}$ at a given temperature, the ratio of the product of the concentrations of the products, each raised to the power of its coefficient, to the product of the concentrations of the reactants, each raised to the power of its coefficient, is constant at equilibrium; it is called the concentration **equilibrium constant**:

$$
K_c = \frac{[\mathrm{G}]^g[\mathrm{H}]^h}{[\mathrm{A}]^a[\mathrm{B}]^b}.
$$
For gas-phase reactions the equilibrium partial pressures are also often used, giving the pressure equilibrium constant $K_p = \frac{p_{\mathrm{G}}^gp_{\mathrm{H}}^h}{p_{\mathrm{A}}^ap_{\mathrm{B}}^b}$. $K_c$ and $K_p$ are determined by experiment, are collectively called empirical equilibrium constants, depend only on temperature, and generally have units: the unit of $K_c$ is $(\mathrm{mol\,L^{-1}})^{\Delta\nu}$ and that of $K_p$ is $\mathrm{Pa}^{\Delta\nu}$ (or $\mathrm{bar}^{\Delta\nu}$).

Here $\Delta\nu = (g + h) - (a + b)$; for gas-phase reactions we write $\Delta\nu_{\mathrm{g}} = \sum_{\mathrm{B(g)}}\nu_{\mathrm{B}}$, the sum of the **stoichiometric numbers** of the gaseous species. For example, for the synthesis of ammonia $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$, $K_c = \frac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}$, $K_p = \frac{p_{\ce{NH3}}^2}{p_{\ce{N2}}p_{\ce{H2}}^3}$, and $\Delta\nu_{\mathrm{g}} = -2$.

The relation between $K_p$ and $K_c$ follows from the equation of state: for an **ideal gas**, $p_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{V}RT = c_{\mathrm{B}}RT$, and substitution into $K_p$ gives

$$
K_p = K_c(RT)^{\Delta\nu_{\mathrm{g}}}.
$$
For $\Delta\nu_{\mathrm{g}} = 0$, $K_p = K_c$. In calculations the unit of $R$ must match those of the concentration and pressure: with $c$ in $\mathrm{mol\,m^{-3}}$ and $p$ in $\mathrm{Pa}$ take $R = 8.314\,\mathrm{Pa\,m^3\,mol^{-1}\,K^{-1}}$; with $c$ in $\mathrm{mol\,L^{-1}}$ and $p$ in $\mathrm{kPa}$ the numerical value is the same, $R = 8.314\,\mathrm{kPa\,L\,mol^{-1}\,K^{-1}}$; with $p$ in $\mathrm{bar}$, $R = 0.08314\,\mathrm{bar\,L\,mol^{-1}\,K^{-1}}$.

### 8.2.2. Rules for Writing the Equilibrium Constant Expression

1. The expression and the value of the equilibrium constant depend on how the equation is written. At $373\,\mathrm{K}$:

| Equation | $K_c$ | Value |
|---|---|---|
| $\ce{N2O4 <=> 2NO2}$ | $K_{c,1} = \frac{[\ce{NO2}]^2}{[\ce{N2O4}]}$ | $0.36$ |
| $\ce{1/2N2O4 <=> NO2}$ | $K_{c,2} = \frac{[\ce{NO2}]}{[\ce{N2O4}]^{1/2}}$ | $0.60$ |
| $\ce{2NO2 <=> N2O4}$ | $K_{c,3} = \frac{[\ce{N2O4}]}{[\ce{NO2}]^2}$ | $2.78$ |

$K_{c,1} = K_{c,2}^2 = 1/K_{c,3}$: multiplying the equation by $n$ raises the equilibrium constant to the $n$th power, and the equilibrium constants of the forward and reverse reactions are reciprocals of each other. An equilibrium constant must therefore always be given together with its equation.

2. Pure solids, pure liquids, and the solvent (water) present in large excess in dilute solutions do not appear in the expression; their effect is already contained in the equilibrium constant (8.3.1 explains why using the **activity**):

$$
\ce{CaCO3(s) <=> CaO(s) + CO2(g)}: \quad K_p = p_{\ce{CO2}};
$$

$$
\ce{CO2(g) + H2(g) <=> CO(g) + H2O(l)}: \quad K_p = \frac{p_{\ce{CO}}}{p_{\ce{CO2}}p_{\ce{H2}}}; \qquad \ce{CO2(g) + H2(g) <=> CO(g) + H2O(g)}: \quad K_p = \frac{p_{\ce{CO}}p_{\ce{H2O}}}{p_{\ce{CO2}}p_{\ce{H2}}};
$$

$$
\ce{Cr2O7^2- + H2O <=> 2CrO4^2- + 2H+}: \quad K_c = \frac{[\ce{CrO4^2-}]^2[\ce{H+}]^2}{[\ce{Cr2O7^2-}]}.
$$
The expression differs according to whether the substance is a liquid or a gas. In a nonaqueous solvent, if water is a reactant or product its concentration is no longer approximately constant and must appear in the expression, as in the esterification of ethanol with acetic acid: $K_c = \frac{[\ce{CH3COOC2H5}][\ce{H2O}]}{[\ce{C2H5OH}][\ce{CH3COOH}]}$.

3. When several reactions add up to an overall reaction, the equilibrium constant of the overall reaction equals the product of the equilibrium constants of the reactions (the following theorem).

**Theorem 8.2.1 (Rule of Multiple Equilibria)** If reaction (3) = reaction (1) + reaction (2), then $K_3 = K_1K_2$ at the same temperature; if reaction (3) = reaction (1) − reaction (2), then $K_3 = K_1/K_2$.

**Proof** When the reactions are all at equilibrium simultaneously in the same system, the equilibrium concentration of each species is unique. Multiplying the equilibrium constant expressions of (1) and (2), the species that appear as a product in one and a reactant in the other cancel, and the result is exactly the expression of reaction (3). $\square$

For example, $\ce{2NO + O2 <=> 2NO2}$ ($K_1 = \frac{[\ce{NO2}]^2}{[\ce{NO}]^2[\ce{O2}]}$) and $\ce{2NO2 <=> N2O4}$ ($K_2 = \frac{[\ce{N2O4}]}{[\ce{NO2}]^2}$) add up to $\ce{2NO + O2 <=> N2O4}$ with $K_3 = \frac{[\ce{N2O4}]}{[\ce{NO}]^2[\ce{O2}]} = K_1K_2$. With this rule, the equilibrium constant of a reaction that is difficult to measure directly can be found from the equilibrium constants of known reactions. It is the same thing as **Hess's law** ([6.1.6](/6.1.6)) in a different guise: when reactions are added, their $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ add, and since $K^\circ = \mathrm{e}^{-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT}$ (8.3.2), the equilibrium constants multiply.

### 8.2.3. The Standard Equilibrium Constant and the Reaction Quotient

The units of empirical equilibrium constants vary from reaction to reaction, which makes calculations and comparisons inconvenient and prevents a direct link with thermodynamic quantities. Dividing concentrations and partial pressures by the concentration $c^\circ = 1\,\mathrm{mol\,L^{-1}}$ of the **standard state** and the **standard pressure** $p^\circ = 10^5\,\mathrm{Pa}$ ([6.1.6](/6.1.6)), respectively, gives dimensionless relative concentrations and relative partial pressures.

**Definition 8.2.2 (Standard Equilibrium Constant)** For the reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$, at equilibrium

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{[\mathrm{B}]}{c^\circ}\right)^{\nu_{\mathrm{B}}}\ (\text{solutes}) \times \prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}\ (\text{gases}),
$$
with pure solids, pure liquids, and the solvent not appearing (equivalent to taking 1), is called the **standard equilibrium constant**. It is dimensionless and depends only on temperature.

For example, for $a\mathrm{A(aq)} + b\mathrm{B(aq)} \ce{<=>} g\mathrm{G(aq)} + h\mathrm{H(aq)}$, $K^\circ = \frac{([\mathrm{G}]/c^\circ)^g([\mathrm{H}]/c^\circ)^h}{([\mathrm{A}]/c^\circ)^a([\mathrm{B}]/c^\circ)^b}$, and for $\ce{CaCO3(s) <=> CaO(s) + CO2(g)}$, $K^\circ = p_{\ce{CO2}}/p^\circ$. Since $c^\circ = 1\,\mathrm{mol\,L^{-1}}$, the $K^\circ$ of a reaction in solution is numerically equal to $K_c$ in units of $\mathrm{mol\,L^{-1}}$. Gas-phase reactions are different:

$$
K^\circ = K_p(p^\circ)^{-\Delta\nu_{\mathrm{g}}} = K_c\left(\frac{c^\circ RT}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}.
$$

**Example 8.2.1** Find $K^\circ$ for $\ce{N2O4(g) <=> 2NO2(g)}$ at $373\,\mathrm{K}$.

Solution. $K_c = 0.36\,\mathrm{mol\,L^{-1}} = 360\,\mathrm{mol\,m^{-3}}$ and $\Delta\nu_{\mathrm{g}} = 1$, so

$$
K^\circ = \frac{K_cRT}{p^\circ} = \frac{360 \times 8.314 \times 373}{10^5} = 11.
$$
The values of $K^\circ$ and $K_c$ for a gas-phase reaction can differ greatly and must not be mixed up.

The equilibrium constant describes only the equilibrium state. For a system at an arbitrary moment (not necessarily at equilibrium), a ratio of the same form can be written.

**Definition 8.2.3 (Reaction Quotient)** The quantity obtained by replacing the equilibrium concentrations and equilibrium partial pressures in the expression of the standard equilibrium constant by the concentrations $c_{\mathrm{B}}$ and partial pressures $p_{\mathrm{B}}$ at an arbitrary moment,

$$
Q = \prod_{\mathrm{B}}\left(\frac{c_{\mathrm{B}}}{c^\circ}\right)^{\nu_{\mathrm{B}}}\prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}
$$
is called the **reaction quotient**. At equilibrium $Q = K^\circ$.

The reaction quotient criterion: when $Q < K^\circ$ the products are relatively deficient and the reaction proceeds in the forward direction; when $Q = K^\circ$ the system is at equilibrium; when $Q > K^\circ$ the reaction proceeds in the reverse direction. This criterion is proved rigorously from thermodynamics in 8.3.2. In this wiki the reaction quotient is denoted $Q$, the same symbol as heat, and the two are distinguished by context.

### 8.2.4. Significance of the Equilibrium Constant

The equilibrium constant can first be used to judge the extent of a reaction. Equilibrium is the maximum extent to which a reversible reaction proceeds under given conditions, and the size of $K^\circ$ reflects the proportion of products at equilibrium. Below, $K^\circ$ at $298.15\,\mathrm{K}$ is calculated from the **standard molar Gibbs energy of formation** of [6.1.6](/6.1.6) using Eq. (8.3) of 8.3.2:

- $\ce{2Cl(g) <=> Cl2(g)}$, $K^\circ \approx 8 \times 10^{36}$. If $p_{\ce{Cl2}} = p^\circ$, at equilibrium $p_{\ce{Cl}}/p^\circ = (K^\circ)^{-1/2} \approx 4 \times 10^{-19}$: the chlorine atoms combine almost entirely into molecules.
- $\ce{N2(g) + O2(g) <=> 2NO(g)}$, $K^\circ \approx 2 \times 10^{-31}$. If $p_{\ce{N2}} = p_{\ce{O2}} = p^\circ$, at equilibrium $p_{\ce{NO}}/p^\circ \approx 4.5 \times 10^{-16}$: at room temperature $\ce{N2}$ and $\ce{O2}$ hardly combine, and conversely NO is thermodynamically unstable (its persistence in the atmosphere is for kinetic reasons).
- $\ce{N2O4(g) <=> 2NO2(g)}$, $K^\circ \approx 0.15$ (11 at $373\,\mathrm{K}$, Example 8.2.1): the amounts of reactant and product do not differ greatly, and neither can be neglected.

Roughly, when $K^\circ > 10^7$ the forward reaction goes quite to completion, and when $K^\circ < 10^{-7}$ the forward reaction hardly proceeds; in between are typical reversible reactions. This is only an order-of-magnitude guide, since the actual equilibrium composition also depends on how the equation is written, the coefficients of the species, and the initial composition.

The equilibrium constant says only to what maximum extent a reaction may proceed, not how long it takes to reach equilibrium. $K^\circ \approx 7.5 \times 10^{24}$ for $\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$ at $298.15\,\mathrm{K}$ (Example 8.3.1), yet the reaction hardly takes place at room temperature, and industrially a $\ce{V2O5}$ catalyst and heating to $400$–$600\,^\circ\mathrm{C}$ are required. Conversely, a reaction with a very small $K^\circ$ can also be made to go more nearly to completion by changing conditions (removing products, changing the temperature).

The equilibrium constant can also be used to calculate equilibrium compositions: given $K^\circ$ and the initial composition, the equilibrium composition can be found. The quantity that measures the extent to which a reactant has been converted is the conversion.

**Definition 8.2.4** The percentage of the initial amount of a reactant that has been converted is called the **conversion**:

$$
\alpha = \frac{\text{initial amount of reactant} - \text{equilibrium amount of reactant}}{\text{initial amount of reactant}} \times 100\%.
$$
The conversion at equilibrium is the maximum conversion under the given conditions and is called the equilibrium conversion.

**Example 8.2.2** For $\ce{CO2(g) + H2(g) <=> CO(g) + H2O(g)}$ at $1473\,\mathrm{K}$, $K^\circ = 2.3$. (1) The initial concentrations of $\ce{CO2}$ and $\ce{H2}$ are both $0.010\,\mathrm{mol\,L^{-1}}$; find the equilibrium conversion of $\ce{CO2}$. (2) If the initial concentration of $\ce{H2}$ is changed to $0.020\,\mathrm{mol\,L^{-1}}$ with everything else unchanged, what is the conversion?

Solution. For this reaction $\Delta\nu_{\mathrm{g}} = 0$, the ratio of partial pressures equals the ratio of concentrations, and $K^\circ$ can be calculated directly with concentrations. Let the equilibrium concentration of CO be $x$ (in $\mathrm{mol\,L^{-1}}$).

| | $\ce{CO2}$ | $\ce{H2}$ | $\ce{CO}$ | $\ce{H2O}$ |
|---|---|---|---|---|
| Initial | 0.010 | 0.010 | 0 | 0 |
| Equilibrium | $0.010 - x$ | $0.010 - x$ | $x$ | $x$ |

(1) $K^\circ = \frac{[\ce{CO}][\ce{H2O}]}{[\ce{CO2}][\ce{H2}]} = \frac{x^2}{(0.010 - x)^2} = 2.3$; taking the square root, $\frac{x}{0.010 - x} = 1.517$ and $x = 0.0060$. $[\ce{CO2}] = 0.0040\,\mathrm{mol\,L^{-1}}$ and the conversion is $60\%$.

(2) $\frac{x^2}{(0.010 - x)(0.020 - x)} = 2.3$, which rearranges to $1.3x^2 - 0.069x + 4.6 \times 10^{-4} = 0$; the root with $0 < x < 0.010$ is $x = 0.0078$. $[\ce{CO2}] = 0.0022\,\mathrm{mol\,L^{-1}}$ and the conversion is $78\%$.

With the equilibrium constant unchanged, increasing the concentration of one reactant ($\ce{H2}$) raises the conversion of the other ($\ce{CO2}$): the conversion depends on the initial composition, whereas the equilibrium constant depends only on temperature. In industry the cheap reactant is often used in excess to raise the conversion of the valuable one (8.4.1).

## 8.3. The Standard Equilibrium Constant and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$

### 8.3.1. The Reaction Isotherm

The Gibbs criterion of [6.1.6](/6.1.6) uses $\Delta_{\mathrm{r}}G_{\mathrm{m}}$, the rate of change of the Gibbs energy as the reaction proceeds at a given composition, whereas the tables give $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ for all species in their standard states. The relation between the two is the isotherm of this section. We derive it first for ideal gases and then extend it to solutions.

First consider how the Gibbs energy of a single ideal gas varies with pressure. For a closed system doing only pressure–volume work, from the fundamental thermodynamic relation $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ ([5.2.4](/5.2.4#eq-4.2)) and $G = H - TS = U + pV - TS$,

$$
\mathrm{d}G = \mathrm{d}U + p\,\mathrm{d}V + V\,\mathrm{d}p - T\,\mathrm{d}S - S\,\mathrm{d}T = V\,\mathrm{d}p - S\,\mathrm{d}T.
$$
At constant temperature $\mathrm{d}G = V\,\mathrm{d}p$. For $1\,\mathrm{mol}$ of ideal gas, $V_{\mathrm{m}} = RT/p$, and integrating from $p^\circ$ to $p$,

$$
G_{\mathrm{m}}(T, p) = G^\circ_{\mathrm{m}}(T) + RT\ln\frac{p}{p^\circ},
$$
where $G^\circ_{\mathrm{m}}(T)$ is the molar Gibbs energy of the gas at the standard pressure. The higher the pressure, the higher the Gibbs energy: a gas has a spontaneous tendency to expand toward lower pressure.

Now consider a mixture of ideal gases. Ideal gas molecules do not interact, so each gas in the mixture behaves as if it alone occupied the whole container with a pressure equal to its **partial pressure** $p_{\mathrm{B}}$ (**Dalton's law of partial pressures**, [6.1.1](/6.1.1)). The molar Gibbs energy of component B is therefore

$$
G_{\mathrm{B}} = G^\circ_{\mathrm{m,B}}(T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ}. \tag{8.1}
$$
(Strictly speaking, the molar Gibbs energy of a component of a mixture is a partial molar quantity, the chemical potential $\mu_{\mathrm{B}}$; Eq. (8.1) holds for ideal gas mixtures, and the general proof is in [Physical Chemistry](/6.3).)

The Gibbs energy of the system is $G = \sum_{\mathrm{B}}n_{\mathrm{B}}G_{\mathrm{B}}$. When the extent of reaction increases by $\mathrm{d}\xi$, $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$, and at constant temperature and pressure

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \left(\frac{\partial G}{\partial\xi}\right)_{T,p} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}G_{\mathrm{B}}.
$$
($G_{\mathrm{B}}$ itself also varies with composition, but the weighted sum of these variations is zero, the Gibbs–Duhem relation, see [Physical Chemistry](/6.3).) $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is the slope of the $G$–$\xi$ curve, with unit $\mathrm{J\,mol^{-1}}$, where "mol" means per mole of extent of reaction. Substituting Eq. (8.1):

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}G^\circ_{\mathrm{m,B}} + RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln\frac{p_{\mathrm{B}}}{p^\circ} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln\prod_{\mathrm{B}}\left(\frac{p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}}.
$$
The last product is precisely the reaction quotient $Q$.

For solutes in solution and for pure condensed phases a relation of the same form as Eq. (8.1) can be written, with the relative partial pressure replaced by another dimensionless quantity:

**Definition 8.3.1** When the molar Gibbs energy (chemical potential) of a species B is written as $G_{\mathrm{B}} = G^\circ_{\mathrm{m,B}} + RT\ln a_{\mathrm{B}}$, the dimensionless quantity $a_{\mathrm{B}}$ is called the **activity** (relative activity) of B. For an ideal gas $a_{\mathrm{B}} = p_{\mathrm{B}}/p^\circ$; for a solute in an ideal dilute solution $a_{\mathrm{B}} \approx c_{\mathrm{B}}/c^\circ$; for pure solids, pure liquids, and the solvent of a dilute solution $a_{\mathrm{B}} \approx 1$.

Activity is an "effective relative concentration". In real solutions $a_{\mathrm{B}} = \gamma_{\mathrm{B}}c_{\mathrm{B}}/c^\circ$, where the activity coefficient $\gamma_{\mathrm{B}}$ reflects deviations from ideal behavior due to interionic interactions and so on, and $\gamma_{\mathrm{B}} \to 1$ in dilute solutions ([Physical Chemistry](/6.3)); real gases use the fugacity in place of the partial pressure. The Gibbs energy of pure solids and pure liquids hardly varies with pressure near the standard pressure, so $a = 1$: this is why they do not appear in the equilibrium constant in 8.2.2. In this course everything is treated in the ideal limit: relative partial pressures for gases and relative concentrations for solutes.

**Theorem 8.3.1 (Reaction Isotherm)** At constant temperature and pressure, the molar Gibbs energy change of the reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ is

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q, \qquad Q = \prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{8.2}
$$

In the ideal limit $Q$ is the reaction quotient of Definition 8.2.3. $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ depends only on temperature and can be calculated from thermodynamic data; $RT\ln Q$ reflects the effect of the actual composition. The isotherm gives $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ at any composition and thus the direction of the reaction.

### 8.3.2. The Standard Equilibrium Constant and the Standard Molar Gibbs Energy of Reaction

At equilibrium $G$ is at a minimum, $\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$, and $Q = K^\circ$. From Eq. (8.2):

**Formula 8.3.1**

$$
\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ, \qquad K^\circ = \exp\left(-\frac{\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}}{RT}\right). \tag{8.3}
$$

This result shows that the value of $Q$ at equilibrium is determined only by $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T)$ and is independent of the initial composition, which is exactly the equilibrium constant found empirically in 8.2. It proves thermodynamically that the equilibrium constant exists, without relying on the reaction mechanism. Substituting Eq. (8.3) back into Eq. (8.2):

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln\frac{Q}{K^\circ}.
$$
Hence $Q < K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$ (forward reaction spontaneous), $Q = K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$ (equilibrium), and $Q > K^\circ \iff \Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ (reverse reaction spontaneous): the reaction quotient criterion and the Gibbs criterion are the same criterion.

**Remark 8.3.1** It is $\Delta_{\mathrm{r}}G_{\mathrm{m}}$, not $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, that decides the direction of a reaction. $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < 0$ says only that $K^\circ > 1$, or that the forward reaction is spontaneous when all species are in their standard states ($Q = 1$); at the actual composition, a reaction with $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < 0$ will also proceed in the reverse direction as long as $Q > K^\circ$. When the magnitude of $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ is large, however, $K^\circ$ is extremely large or extremely small, and ordinary changes of composition are not enough to change the direction: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -40\,\mathrm{kJ\,mol^{-1}}$ corresponds to $K^\circ \approx 10^7$ at $298\,\mathrm{K}$, so $|\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}| > 40\,\mathrm{kJ\,mol^{-1}}$ is commonly used as a rough criterion that a reaction is essentially complete or essentially does not proceed.

Why does $G$ have a minimum between $0 < \xi < 1$ rather than at pure reactants or pure products? Take $\ce{N2O4 <=> 2NO2}$: if reactants and products each stayed pure and unmixed, $G$ would vary linearly with $\xi$ and the system would run to the end with lower $G$. In reality they mix: the slope of $RT\ln(p_{\mathrm{B}}/p^\circ)$ in Eq. (8.1) tends to $-\infty$ as $\xi \to 0$ and $\xi \to 1$ because of the **entropy** of mixing; it makes the $G$–$\xi$ curve bend downward at both ends, and the minimum lies in the middle. Chemical equilibrium therefore always has reactants and products coexisting; only when $K^\circ$ is very large or very small does the minimum lie very close to one end.

![Gibbs energy of the system as a function of the extent of reaction, starting from 1 mol of N₂O₄ at 298.15 K and total pressure p°: the dashed line is the straight line for no mixing, the solid line bends downward because of mixing, the minimum is the equilibrium, and the slopes on either side give the sign of ΔrGm](./plots/gibbs-extent.py)

In the figure the system starts from 1 mol of $\ce{N2O4}$ at a constant total pressure $p^\circ$, and the equilibrium condition is $K^\circ = \frac{(p_{\ce{NO2}}/p^\circ)^2}{p_{\ce{N2O4}}/p^\circ} = \frac{4\xi^2}{1 - \xi^2}$. At $298.15\,\mathrm{K}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 4.73\,\mathrm{kJ\,mol^{-1}}$ and $K^\circ = 0.148$, which gives $\xi_{\mathrm{eq}} = \sqrt{K^\circ/(4 + K^\circ)} = 0.189\,\mathrm{mol}$, that is, about $19\%$ of the $\ce{N2O4}$ decomposes: a reaction with $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} > 0$ also proceeds to some extent.

**Example 8.3.1** Find $K^\circ$ for $\ce{2SO2(g) + O2(g) <=> 2SO3(g)}$ at $298.15\,\mathrm{K}$. Given $\Delta_{\mathrm{f}}G^\circ(\ce{SO2}, \mathrm{g}) = -300.1\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{f}}G^\circ(\ce{SO3}, \mathrm{g}) = -371.1\,\mathrm{kJ\,mol^{-1}}$.

Solution. $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 2 \times (-371.1) - 2 \times (-300.1) - 0 = -142.0\,\mathrm{kJ\,mol^{-1}}$ ($\Delta_{\mathrm{f}}G^\circ = 0$ for the element $\ce{O2}$). From Eq. (8.3),

$$
\ln K^\circ = \frac{142.0 \times 10^3}{8.314 \times 298.15} = 57.28, \qquad K^\circ = 7.5 \times 10^{24}.
$$

## 8.4. Shifts of Chemical Equilibrium

The process in which a change of conditions destroys an existing equilibrium and the system establishes a new equilibrium under the new conditions is called a shift of the equilibrium. From $\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln(Q/K^\circ)$ there are only two ways to disturb an equilibrium:

- change $Q$ with $K^\circ$ unchanged: change the concentration, pressure, or volume;
- change $K^\circ$: change the temperature ($\ln K^\circ = -\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT$).

In either case, to find the direction of the shift we need only compare the new $Q$ with $K^\circ$.

### 8.4.1. Concentration

At constant temperature and volume, increasing the concentration of a reactant or decreasing that of a product gives $Q < K^\circ$ and the equilibrium shifts in the forward direction until $Q$ again equals $K^\circ$; the opposite change shifts it in the reverse direction. Industrial applications:

- $\ce{2SO2 + O2 <=> 2SO3}$: the equation calls for $\ce{SO2}$ and $\ce{O2}$ in the ratio $1 : 0.5$, but about $1 : 1.6$ is used in practice (excess air) to raise the conversion of $\ce{SO2}$.
- $\ce{CO + H2O <=> H2 + CO2}$ (the water–gas shift): steam is used in excess to raise the conversion of CO.
- $\ce{Fe3O4(s) + 4H2(g) <=> 3Fe(s) + 4H2O(g)}$: water vapor is continuously removed so that $\ce{Fe3O4}$ is reduced completely.

### 8.4.2. Pressure

Pressure has little effect on reactions involving only liquids and solids. For reactions involving gases, consider compressing the volume at constant temperature to $1/x$ of its original value; all partial pressures become $x$ times as large and the reaction quotient becomes

$$
Q' = x^{\Delta\nu_{\mathrm{g}}}K^\circ.
$$

1. $\Delta\nu_{\mathrm{g}} \ne 0$: for the synthesis of ammonia, $\Delta\nu_{\mathrm{g}} = -2$, so doubling the pressure ($x = 2$) gives $Q' = \frac{1}{4}K^\circ < K^\circ$ and the equilibrium shifts forward, whereas halving the pressure ($x = \frac{1}{2}$) gives $Q' = 4K^\circ$ and the equilibrium shifts backward. Increasing the pressure shifts the equilibrium in the direction of fewer gas molecules; decreasing the pressure shifts it in the direction of more gas molecules.
2. $\Delta\nu_{\mathrm{g}} = 0$: for example, $\ce{CO(g) + H2O(g) <=> H2(g) + CO2(g)}$ has $Q' = K^\circ$, and changing the total pressure has no effect on the equilibrium.

When a gas that does not take part in the reaction (such as Ar) is added to an ammonia synthesis system already at equilibrium, the outcome depends on the conditions:

- Constant temperature and volume: the total pressure increases, but the amounts of the reacting gases and the volume are unchanged, so the partial pressures are unchanged, $Q = K^\circ$, and the equilibrium does not shift. Adding an inert gas to double the total pressure therefore does not shift the ammonia equilibrium.
- Constant temperature and pressure: the volume increases and the partial pressures of the reacting gases all decrease in the same proportion, which is equivalent to reducing the pressure on the reaction system, and the equilibrium shifts toward more gas molecules (the reverse direction for ammonia synthesis). This is why the Ar and $\ce{CH4}$ that accumulate in the ammonia synthesis feed gas must be vented periodically.

What determines the equilibrium is the partial pressures of the reacting gases, not the total pressure.

### 8.4.3. Temperature

When the temperature changes, $K^\circ$ itself changes. From $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$,

$$
\ln K^\circ = -\frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT} + \frac{\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}}{R}. \tag{8.4}
$$

**Theorem 8.4.1 (van 't Hoff Equation)** The rate of change of the standard equilibrium constant with temperature is

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}.
$$
If the temperature range is small, $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ can be regarded as constant, and

$$
\ln\frac{K^\circ_2}{K^\circ_1} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right). \tag{8.5}
$$

**Proof** Under the approximation that $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ do not vary with temperature (that is, neglecting the difference $\Delta_{\mathrm{r}}C_p$ of the heat capacities of products and reactants), differentiating Eq. (8.4) gives the differential form; writing Eq. (8.4) at the two temperatures $T_1$ and $T_2$ and subtracting, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ cancels and Eq. (8.5) follows. The differential form itself does not need this approximation; it is a direct consequence of the Gibbs–Helmholtz equation $\left(\frac{\partial(G/T)}{\partial T}\right)_p = -\frac{H}{T^2}$ ([Physical Chemistry](/6.3)). $\square$

The van 't Hoff equation has the same form as the Arrhenius equation ([6.1.7](/6.1.7#def-7.3.5)), and this is no accident: for an elementary reaction $K = k_+/k_-$, and taking logarithms and differentiating with respect to $T$ gives $\frac{\mathrm{d}\ln K}{\mathrm{d}T} = \frac{E_{\mathrm{a}} - E_{\mathrm{a}}'}{RT^2}$, consistent with $\Delta_{\mathrm{r}}H_{\mathrm{m}} \approx E_{\mathrm{a}} - E_{\mathrm{a}}'$ on the potential energy diagram.

By Eq. (8.4), a plot of $\ln K^\circ$ against $1/T$ (a van 't Hoff plot) is a straight line with slope $-\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/R$ and intercept $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}/R$: measuring equilibrium constants at different temperatures gives the standard enthalpy and entropy changes of the reaction, which is a way to determine $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ without a calorimeter.

- Exothermic reactions ($\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} < 0$): raising the temperature decreases $K^\circ$ and shifts the equilibrium in the reverse direction; lowering the temperature shifts it in the forward direction.
- Endothermic reactions ($\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} > 0$): raising the temperature increases $K^\circ$ and shifts the equilibrium in the forward direction.

In short, raising the temperature shifts the equilibrium in the endothermic direction and lowering it shifts the equilibrium in the exothermic direction. Unlike concentration and pressure, a change of temperature changes the equilibrium constant itself.

**Example 8.4.1** Consider the synthesis of ammonia $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$. From $\Delta_{\mathrm{f}}H^\circ(\ce{NH3}, \mathrm{g}) = -45.9\,\mathrm{kJ\,mol^{-1}}$ and the standard molar entropies $S^\circ_{\mathrm{m}}(\ce{NH3}) = 192.8$, $S^\circ_{\mathrm{m}}(\ce{N2}) = 191.6$, and $S^\circ_{\mathrm{m}}(\ce{H2}) = 130.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$, estimate $K^\circ$ at $473\,\mathrm{K}$ and $573\,\mathrm{K}$.

Solution. $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 2 \times (-45.9) = -91.8\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = 2 \times 192.8 - 191.6 - 3 \times 130.7 = -198.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$. Neglecting their variation with temperature, from Eq. (8.4):

$$
473\,\mathrm{K}: \quad \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -91.8 + 473 \times 0.1981 = 1.9\,\mathrm{kJ\,mol^{-1}}, \qquad K^\circ_1 = \mathrm{e}^{-1900/(8.314 \times 473)} = 0.62.
$$
Then from Eq. (8.5),

$$
\ln\frac{K^\circ_2}{0.62} = \frac{-91.8 \times 10^3}{8.314}\left(\frac{1}{473} - \frac{1}{573}\right) = -4.07, \qquad K^\circ_2 = 1.0 \times 10^{-2}.
$$
A 100 K rise reduces $K^\circ$ to about $1/60$ of its value: lower temperature favors the formation of ammonia ($K^\circ \approx 5 \times 10^5$ at $298\,\mathrm{K}$).

At low temperature, however, the reaction is too slow. The industrial Haber–Bosch process uses $400$–$500\,^\circ\mathrm{C}$, $10$–$30\,\mathrm{MPa}$, and an iron catalyst: the higher temperature ensures a sufficient rate, the high pressure compensates for the lower equilibrium yield at high temperature, and the unreacted gas is recycled after the ammonia is separated. This is a typical example of a compromise between thermodynamics and kinetics.

![Ammonia synthesis: left, van 't Hoff plot of ln K° against 1/T, where the line for an exothermic reaction has a positive slope; right, the equilibrium mole fraction of ammonia as a function of temperature and total pressure for N₂ and H₂ fed in the ratio 1 : 3 (ideal gases, estimate neglecting ΔrCp)](./plots/ammonia-equilibrium.py)

The right panel is obtained by solving for the equilibrium composition with the values of $K^\circ(T)$ of Example 8.4.1: let $\xi$ mol of the $1\,\mathrm{mol}$ of $\ce{N2}$ react in a mixture with $3\,\mathrm{mol}$ of $\ce{H2}$, so that the total amount is $4 - 2\xi$; substitute in $K^\circ = \frac{x_{\ce{NH3}}^2}{x_{\ce{N2}}x_{\ce{H2}}^3}\left(\frac{p}{p^\circ}\right)^{-2}$ and solve for $\xi$ by numerical root finding (for example `scipy.optimize.brentq`, [4.4.4](/4.4.4#sec-4.2.2)). The deviations of real gases at high pressure and $\Delta_{\mathrm{r}}C_p$ make the actual values differ slightly from those in the figure, but the trends are the same.

### 8.4.4. Le Chatelier's Principle

The conclusions above can be summarized in *Le Chatelier's principle*: if one of the conditions of a system at equilibrium (concentration, pressure, or temperature) is changed, the equilibrium shifts in the direction that counteracts the change. Specifically: increasing the concentration of a reactant shifts the equilibrium in the direction that consumes the reactant; increasing the pressure shifts it toward fewer gas molecules; raising the temperature shifts it in the endothermic direction.

Le Chatelier's principle is a qualitative empirical rule and may give wrong predictions when conditions are complicated; the reliable criterion is always the comparison of $Q$ with $K^\circ$.

**Example 8.4.2** At constant temperature and pressure, a little more $\ce{N2}$ is added to an ammonia synthesis system already at equilibrium. Does the equilibrium necessarily shift toward the formation of $\ce{NH3}$?

Solution. At constant pressure the partial pressure of each species is $p_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{n}p$ ($n$ is the total amount of substance), so

$$
Q = \frac{(p_{\ce{NH3}}/p^\circ)^2}{(p_{\ce{N2}}/p^\circ)(p_{\ce{H2}}/p^\circ)^3} = \frac{n_{\ce{NH3}}^2\,n^2}{n_{\ce{N2}}\,n_{\ce{H2}}^3}\left(\frac{p^\circ}{p}\right)^2.
$$
When $\mathrm{d}n_{\ce{N2}}$ is added, $n$ also increases by $\mathrm{d}n_{\ce{N2}}$, and

$$
\frac{\partial\ln Q}{\partial n_{\ce{N2}}} = \frac{2}{n} - \frac{1}{n_{\ce{N2}}},
$$
which is positive when $x_{\ce{N2}} = n_{\ce{N2}}/n > \frac{1}{2}$: adding $\ce{N2}$ makes $Q > K^\circ$, and the equilibrium shifts instead toward the decomposition of ammonia. The reason is that although adding $\ce{N2}$ increases the partial pressure of $\ce{N2}$, it also dilutes $\ce{H2}$ and $\ce{NH3}$, and $\ce{H2}$ appears to the third power in $Q$. Only when $x_{\ce{N2}} < \frac{1}{2}$ (including the usual case of a 1 : 3 feed) does adding $\ce{N2}$ shift the equilibrium forward. At constant volume, adding $\ce{N2}$ does not change the other partial pressures, and the equilibrium always shifts forward.

A catalyst accelerates the forward and reverse reactions equally ([6.1.7](/6.1.7)) and does not change $K^\circ$, so it does not shift the equilibrium and only shortens the time needed to reach it.

## Questions

1. Given $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -4.73\,\mathrm{kJ\,mol^{-1}}$ for $\ce{2NO2(g) <=> N2O4(g)}$ at $298\,\mathrm{K}$, in which direction does the reaction proceed when a gas mixture with $p_{\ce{NO2}} = p_{\ce{N2O4}} = 50\,\mathrm{kPa}$ is placed in a container?
   Answer: $K^\circ = \mathrm{e}^{4730/(8.314 \times 298)} = 6.7$ and $Q = \frac{0.5}{0.5^2} = 2 < K^\circ$, so the reaction proceeds toward the formation of $\ce{N2O4}$.
2. Why is it wrong to say that "the larger $K^\circ$ is, the faster the reaction"?
   Answer: $K^\circ$ is determined by $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ and is a thermodynamic quantity; the rate is determined by the activation energy and is a kinetic quantity. $K^\circ \approx 10^{25}$ for $\ce{2SO2 + O2}$, yet the reaction hardly proceeds at room temperature.
3. For an endothermic reaction, raising the temperature accelerates both the forward and the reverse reaction. Why does the equilibrium still shift in the forward direction?
   Answer: From $K = k_+/k_-$ and $E_{\mathrm{a}} - E_{\mathrm{a}}' = \Delta_{\mathrm{r}}H_{\mathrm{m}} > 0$, the forward reaction has the larger activation energy and $k_+$ increases faster with temperature ([6.1.7](/6.1.7)), so $K$ increases.

## Summary

| Topic | Key points |
|---|---|
| Chemical equilibrium | dynamic equilibrium with equal forward and reverse rates; $G$ is at a minimum with respect to $\xi$, $\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$ |
| Equilibrium constant | $K_c$ and $K_p$ have units, $K_p = K_c(RT)^{\Delta\nu_{\mathrm{g}}}$; $K^\circ$ uses relative concentrations and relative partial pressures and is dimensionless, $K^\circ = K_c(c^\circ RT/p^\circ)^{\Delta\nu_{\mathrm{g}}}$ |
| Writing rules | depends on how the equation is written; pure solids, pure liquids, and the solvent of dilute solutions are omitted; when reactions add, equilibrium constants multiply |
| Reaction quotient | $Q < K^\circ$ forward, $Q = K^\circ$ equilibrium, $Q > K^\circ$ reverse |
| Isotherm | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q = RT\ln(Q/K^\circ)$; $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ |
| Concentration and pressure | change $Q$ but not $K^\circ$; increasing the pressure shifts the equilibrium toward fewer gas molecules; an inert gas added at constant volume does not shift it, and at constant pressure is equivalent to lowering the pressure |
| Temperature | changes $K^\circ$: $\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}$; raising the temperature shifts the equilibrium in the endothermic direction |
| Le Chatelier's principle | the equilibrium shifts in the direction that counteracts the change; a qualitative rule, the comparison of $Q$ with $K^\circ$ is decisive; a catalyst does not affect the equilibrium |
