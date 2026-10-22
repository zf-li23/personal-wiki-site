---
title: Chemical Equilibrium
source_hash: 13361d9461f2
---

[6.1.8](/6.1.8) started from the empirical equilibrium constant and, with the help of ideal-gas and dilute-solution approximations, wrote down the **reaction isotherm** and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$, and discussed the effects of concentration, pressure, and temperature on equilibrium. With the **chemical potential** ([6.3.4](/6.3.4)) and the **activity** ([6.3.6](/6.3.6)) in hand, these results can be derived rigorously for any system. This chapter answers three questions: why a chemical reaction in general cannot go to completion and what the condition for equilibrium is (7.1); how the standard equilibrium constant is defined from chemical potentials and what form it takes for gases, solutions, and heterogeneous reactions (7.2–7.3); and how $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ is obtained and used (7.4). We then revisit the shift of equilibrium within the rigorous framework, including the van 't Hoff equation for $\Delta_{\mathrm{r}}C_p \ne 0$, the fugacity correction at high pressure, and the precise statement of Le Chatelier's principle (7.5). Finally we discuss simultaneous equilibria and coupled reactions, taking biochemical reactions driven by ATP hydrolysis as the example (7.6).

We keep the notation of [6.1.8](/6.1.8). A reaction is written $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ (the **stoichiometric number** $\nu_{\mathrm{B}}$ is positive for products and negative for reactants), the **extent of reaction** is $\xi$, and the activity product in an arbitrary state (the **reaction quotient**) is denoted $Q$ (many textbooks write $J$). $Q$ has the same symbol as heat, but no heat appears in this chapter, so no confusion arises.

## 7.1. The Condition for Chemical Equilibrium

### 7.1.1. Why Reactions Do Not Go to Completion

Consider the ideal-gas reaction $\mathrm{A(g)} \ce{<=>} \mathrm{B(g)}$ at constant temperature and pressure, starting from $1\,\mathrm{mol}$ of A. When the extent of reaction is $\xi$, the Gibbs energy of the system is

$$
G(\xi) = (1 - \xi)\mu_{\mathrm{A}} + \xi\mu_{\mathrm{B}} = \underbrace{(1 - \xi)\mu^*_{\mathrm{A}} + \xi\mu^*_{\mathrm{B}}}_{\text{pure substances, unmixed}} + \underbrace{RT[(1 - \xi)\ln(1 - \xi) + \xi\ln\xi]}_{\Delta_{\mathrm{mix}}G},
$$
where $\mu^*_{\mathrm{B}}$ is the chemical potential of pure B at $T$ and $p$, and the second term uses $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}} + RT\ln x_{\mathrm{B}}$ for an ideal-gas mixture ([6.3.4](/6.3.4)). The first term is a linear function of $\xi$: if reactants and products always stayed pure, $G$ would vary monotonically along a straight line, and the reaction would either go to completion or not proceed at all. The second term is the Gibbs energy of mixing ([6.3.5](/6.3.5)); it is negative for $0 < \xi < 1$ and has slopes $-\infty$ and $+\infty$ at the two ends. Added together, $G(\xi)$ must have a minimum in the interior of $0 < \xi < 1$. Hence, as long as reactants and products can mix, the reaction stops at some composition in which both are present: chemical equilibrium is a consequence of the entropy of mixing.

![Gibbs energy G(ξ) of the ideal-gas isomerization A ⇌ B (ΔrG° = −3.0 kJ/mol, 298.15 K, p°): the dashed line is the unmixed straight line, the dotted curve is the Gibbs energy of mixing, and their sum has a minimum at ξ = K°/(1 + K°)](./plots/gibbs-mixing-extent.py)

The situation differs when reactants and products cannot mix. In $\ce{CaCO3(s) <=> CaO(s) + CO2(g)}$ the two solids are separate pure phases, and at given $T$ and $p_{\ce{CO2}}$ the Gibbs energy $G$ is linear in $\xi$: when $p_{\ce{CO2}}$ is below the decomposition pressure (7.2.3), $\ce{CaCO3}$ decomposes completely; above it, there is no decomposition at all; only when $p_{\ce{CO2}}$ equals the decomposition pressure can the three phases coexist.

### 7.1.2. The Molar Reaction Gibbs Energy

For a multicomponent closed system that does only volume work, $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ ([6.3.4](/6.3.4)). When the extent of reaction changes by $\mathrm{d}\xi$, $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$, so at constant $T$ and $p$, $\mathrm{d}G = \left(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\right)\mathrm{d}\xi$.

**Definition 7.1.1 (Reaction Gibbs Energy)** The rate of change of the Gibbs energy of the system with the extent of reaction at constant temperature and pressure, with no non-volume work,

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \left(\frac{\partial G}{\partial\xi}\right)_{T,p} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} \tag{7.1}
$$
is called the **molar reaction Gibbs energy**, in units of $\mathrm{J\,mol^{-1}}$.

It can be understood in two ways: as the slope of the $G$–$\xi$ curve at the present composition, or as the change in $G$ when $1\,\mathrm{mol}$ of reaction advances in an infinitely large system (so that the composition does not change). The symbol $\Delta$ does not mean "final minus initial": $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is a function of the present state of the system ($T$, $p$, and composition); it is a state quantity, not a process quantity.

By the Gibbs criterion, at constant temperature and pressure with no non-volume work:

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0: \text{the forward reaction is spontaneous}; \qquad \Delta_{\mathrm{r}}G_{\mathrm{m}} = 0: \text{equilibrium}; \qquad \Delta_{\mathrm{r}}G_{\mathrm{m}} > 0: \text{the reverse reaction is spontaneous}.
$$

### 7.1.3. The Equilibrium Condition

**Theorem 7.1.1** The condition for a chemical reaction to be at equilibrium is

$$
\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}^{\mathrm{eq}} = 0. \tag{7.2}
$$
It holds not only at constant temperature and pressure but also under other constraints such as constant temperature and volume, and it applies to heterogeneous reactions.

**Proof** At constant temperature and pressure the result follows from Eq. (7.1) and the minimum of $G$. At constant temperature and volume we use the Helmholtz energy, $\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$; at equilibrium $A$ is a minimum, $(\partial A/\partial\xi)_{T,V} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$, which is the same condition. In an isolated system we use $\mathrm{d}S = \frac{1}{T}\mathrm{d}U + \frac{p}{T}\mathrm{d}V - \frac{1}{T}\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ and the maximum of entropy, and again obtain the same condition. In a multiphase system the chemical potential of a substance is equal in all phases in which it is present (the condition for **phase equilibrium**, [6.3.8](/6.3.8)), so it does not matter which phase's $\mu_{\mathrm{B}}$ is used in the sum. $\square$

The constraint only determines which thermodynamic potential is extremal; it does not change the equilibrium condition itself: Eq. (7.2) is a property of the equilibrium state. Different constraints differ in the position of equilibrium (for example, the equilibrium compositions at constant pressure and at constant volume are different).

## 7.2. The Standard Equilibrium Constant and the Reaction Isotherm

### 7.2.1. Derivation from Chemical Potentials

Substituting the general expression for the chemical potential, $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}}$ (Eq. (6.3) of [6.3.6](/6.3.6), with the pressure term of condensed phases neglected), into Eq. (7.1):

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} + RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln a_{\mathrm{B}}.
$$

**Definition 7.2.1 (Standard Reaction Gibbs Energy)**

$$
\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}}(T)
$$
is called the **standard molar reaction Gibbs energy** of the reaction: the Gibbs energy change for $1\,\mathrm{mol}$ of reaction when all substances are in their respective standard states.

$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ depends only on temperature and on two "subjective" choices: the standard states of the substances and the way the reaction equation is written ($\nu_{\mathrm{B}}$).

**Theorem 7.2.1 (Reaction Isotherm)** For any chemical reaction in any state,

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q, \qquad Q = \prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{7.3}
$$

At equilibrium $\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$, and $Q$ equals a constant that depends only on temperature:

**Definition 7.2.2 (Standard Equilibrium Constant)**

$$
K^\circ(T) = \exp\left(-\frac{\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}}{RT}\right) = \prod_{\mathrm{B}}\left(a_{\mathrm{B}}^{\mathrm{eq}}\right)^{\nu_{\mathrm{B}}}. \tag{7.4}
$$

The first equality is the thermodynamic definition of $K^\circ$; the second relates it to the equilibrium composition. The derivation does not depend on the reaction mechanism, and it does not assume that gases or solutions are ideal: all non-ideality is contained in the activities. Substituting back into Eq. (7.3),

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln\frac{Q}{K^\circ}:
$$
the forward reaction is spontaneous for $Q < K^\circ$, the system is at equilibrium for $Q = K^\circ$, and the reverse reaction is spontaneous for $Q > K^\circ$ (valid at constant $T$ and $p$ or at constant $T$ and $V$).

If the pressure term $\int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$ in the chemical potentials of condensed phases is retained, the equilibrium relation is written rigorously as $K^\circ = \prod_{\mathrm{B}}(a_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}}\exp\left(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p/RT\right)$, and the last factor differs very little from 1 unless the pressure is very high (for an aqueous reaction at $10\,\mathrm{MPa}$ with $\sum\nu_{\mathrm{B}}V_{\mathrm{B}} = 20\,\mathrm{cm^3\,mol^{-1}}$ it is $1.08$). In deep-sea and high-pressure biochemistry this term cannot be neglected.

Properties of $K^\circ$:

1. It is dimensionless and a function of temperature only, independent of pressure and composition (the standard-state pressure is fixed at $p^\circ$).
2. It depends on the choice of standard state: for solution reactions, $K^\circ$ has different numerical values when solutes are expressed on the $x$, $b$, or $c$ scale (7.2.2).
3. It depends on how the equation is written: multiplying the equation by $n$ multiplies $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ by $n$ and raises $K^\circ$ to the $n$th power; the $K^\circ$ values of the forward and reverse reactions are reciprocals; when reactions are added, their $K^\circ$ values are multiplied ([6.1.8](/6.1.8#thm-8.2.1)). Therefore, when $K^\circ$ is quoted, the equation and the temperature must be given with it, and for solution reactions also the standard state.

### 7.2.2. Standard Equilibrium Constants of Various Reactions

The definition of $K^\circ$ is unique; its specific relation to the equilibrium composition depends on the system:

| System | Activity | $K^\circ$ |
|---|---|---|
| Ideal gas | $p_{\mathrm{B}}/p^\circ$ | $\prod(p_{\mathrm{B}}/p^\circ)^{\nu_{\mathrm{B}}}$, the product of equilibrium partial pressures |
| Real gas | $f_{\mathrm{B}}/p^\circ = \varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ$ | $\prod(\varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ)^{\nu_{\mathrm{B}}}$, the product of equilibrium fugacities |
| Ideal liquid mixture | $x_{\mathrm{B}}$ | $\prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$ |
| Ideal dilute solution (all species are solutes) | $x_{\mathrm{B}}$, $b_{\mathrm{B}}/b^\circ$, or $c_{\mathrm{B}}/c^\circ$ | $\prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$, $\prod(b_{\mathrm{B}}/b^\circ)^{\nu_{\mathrm{B}}}$, or $\prod(c_{\mathrm{B}}/c^\circ)^{\nu_{\mathrm{B}}}$ |
| Real solution | $\gamma_{\mathrm{B}}x_{\mathrm{B}}$, etc. | product of equilibrium activities |
| Pure solids or pure liquids participate | pure condensed phase $a = 1$ | contains only gases and solution species |

Remarks:

- When the solvent (such as water) is a reactant or product in solution, by Raoult's law $a_{\ce{H2O}} = \gamma_{\mathrm{A}}x_{\mathrm{A}} \approx 1$, so it is not written into $K^\circ$ in dilute aqueous solutions; in concentrated solutions or non-aqueous solvents it cannot be omitted ([6.1.8](/6.1.8#sec-8.2.2)).
- For the same solution reaction on different solute scales, the conversion between the $K^\circ$ values follows from $\mu^\circ_{b,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln(M_{\mathrm{A}}b^\circ)$ ([6.3.5](/6.3.5)): $K^\circ_x = K^\circ_b(M_{\mathrm{A}}b^\circ)^{\sum\nu_{\mathrm{B}}}$, where the sum runs over solutes only. In aqueous solution $K^\circ$ is usually given with $b^\circ = 1\,\mathrm{mol\,kg^{-1}}$ (or $c^\circ$), which is also the standard state used for hydrated species in thermodynamic data tables.
- The rigorous reason that the activity of a pure solid is 1 is that its reference state is the pure solid itself at the same temperature and pressure, $\mu^*_{\mathrm{B}}(\mathrm{s}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{s}, T) + \int_{p^\circ}^{p}V^*_{\mathrm{m}}\,\mathrm{d}p$; comparing with $\mu^\circ + RT\ln a$, $a = 1$ when the pressure term is negligible.

For example:

$$
\ce{NH4Cl(s) <=> NH3(g) + HCl(g)}: \quad K^\circ = \frac{p_{\ce{NH3}}}{p^\circ}\cdot\frac{p_{\ce{HCl}}}{p^\circ}; \qquad \ce{C2H4(g) + H2O(l) <=> C2H5OH(aq)}: \quad K^\circ = \frac{a_{b}(\ce{C2H5OH})}{p_{\ce{C2H4}}/p^\circ}.
$$
The latter is a heterogeneous equilibrium among a gas phase, a liquid, and a solution: ethylene is treated as an ideal gas, water is the solvent ($a \approx 1$), and ethanol is a solute on the $b$ scale.

### 7.2.3. Decomposition Pressure

**Definition 7.2.3** At a given temperature, when a pure condensed substance decomposes into gases (and other pure condensed phases) and the reaction is at equilibrium, the sum of the partial pressures of the gaseous products is called the **decomposition pressure** of the substance.

Because the activity of a condensed phase is 1, $K^\circ$ contains only the partial pressures of gases, and the decomposition pressure has a fixed value at a given temperature. The decomposition pressure of $\ce{CaCO3}$ is simply the equilibrium pressure of $\ce{CO2}$, $K^\circ = p_{\ce{CO2}}/p^\circ$; $\ce{NH4Cl}$ decomposes into equal amounts of two gases, so the decomposition pressure is $p = 2p_{\ce{NH3}}$ and $K^\circ = (p/2p^\circ)^2$. The temperature at which the decomposition pressure equals the external pressure (for example $101.325\,\mathrm{kPa}$) is called the decomposition temperature.

**Example 7.2.1** From the values of $\Delta_{\mathrm{f}}G^\circ$ at $298.15\,\mathrm{K}$ ($\ce{NH4Cl}$(s) $-202.9$, $\ce{NH3}$(g) $-16.4$, HCl(g) $-95.3\,\mathrm{kJ\,mol^{-1}}$, CRC Handbook), find the decomposition pressure of $\ce{NH4Cl}$ at $298.15\,\mathrm{K}$.

**Solution** $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -16.4 - 95.3 + 202.9 = 91.2\,\mathrm{kJ\,mol^{-1}}$, $K^\circ = \exp(-91200/(8.314 \times 298.15)) = 1.05 \times 10^{-16}$, and $p = 2\sqrt{K^\circ}\,p^\circ = 2.1 \times 10^{-8}\,\mathrm{bar} = 2\,\mathrm{mPa}$. At room temperature $\ce{NH4Cl}$ hardly decomposes; on heating it "sublimes" (its decomposition pressure reaches $1\,\mathrm{atm}$ at about $610\,\mathrm{K}$) and recombines to a solid in the cooler part of the apparatus.

### 7.2.4. Empirical Equilibrium Constants

The products written directly in terms of equilibrium partial pressures, mole fractions, or concentrations, $K_p = \prod p_{\mathrm{B}}^{\nu_{\mathrm{B}}}$, $K_x = \prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$, $K_c = \prod c_{\mathrm{B}}^{\nu_{\mathrm{B}}}$, are called empirical **equilibrium constants** ([6.1.8](/6.1.8#def-8.2.1)) and generally have units. For an ideal-gas reaction, with $\Delta\nu_{\mathrm{g}} = \sum_{\mathrm{B(g)}}\nu_{\mathrm{B}}$,

$$
K^\circ = K_p(p^\circ)^{-\Delta\nu_{\mathrm{g}}} = K_x\left(\frac{p}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}} = K_c\left(\frac{c^\circ RT}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}. \tag{7.5}
$$
$K^\circ$, $K_p$, and $K_c$ depend only on temperature; $K_x$ also depends on the total pressure (when $\Delta\nu_{\mathrm{g}} \ne 0$), and it is through $K_x$ that pressure affects the equilibrium composition (7.5.2). For real gases $K_p$ is no longer constant but varies with pressure.

## 7.3. Calculating Equilibrium Compositions

Two quantities measure the position of equilibrium: the equilibrium **conversion** (the fraction of a reactant that has been converted at equilibrium relative to the amount charged) and the equilibrium yield (the amount of a product at equilibrium as a fraction of the theoretical yield if all the feed were converted). They differ when side reactions occur: the converted feed does not all become the desired product.

The steps for calculating an equilibrium composition are: (1) write the amount of each substance and the total amount in terms of the extent of reaction $\xi$; (2) write the activities (partial pressures, mole fractions, etc.); (3) substitute into $K^\circ$ to obtain an equation in $\xi$ and solve it. The equation is generally of high degree, and numerical root finding is the most convenient approach: the range of $\xi$ is fixed by the requirement that all amounts be nonnegative, and within this interval $\ln Q(\xi)$ increases monotonically (7.5.4), so the root is unique and can be found with `scipy.optimize.brentq` between the endpoints of the interval ([4.4.4](/4.4.4#sec-4.2.2)). When there are several independent reactions, the unknowns are several extents of reaction, and one solves the simultaneous equations with `scipy.optimize.fsolve` or directly minimizes $G$ under constraints (7.6.1).

```python
from scipy.optimize import brentq

K = 6.4e-3          # 1/2 N2 + 3/2 H2 <=> NH3 at 723 K
def residual(x, p):  # x = mol N2 reacted from 1 N2 + 3 H2; p in bar
    return 2 * x * (4 - 2 * x) / (3**1.5 * (1 - x)**2) / p - K

for p in (1, 300):
    x = brentq(residual, 1e-12, 1 - 1e-12, args=(p,))
    print(p, x, 2 * x / (4 - 2 * x))   # conversion and NH3 mole fraction
```

## 7.4. The Standard Reaction Gibbs Energy

### 7.4.1. Meaning, and the Difference from $\Delta_{\mathrm{r}}G_{\mathrm{m}}$

| | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ | $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} = -RT\ln K^\circ$ |
|---|---|---|
| Meaning | driving force of the reaction at the present composition | driving force when all substances are in their standard states; determines the position of equilibrium |
| Depends on | $T$, $p$, composition | $T$ only (and the standard states and the way the equation is written) |
| At equilibrium | equal to zero | generally not zero |
| Use | to decide the direction | to calculate $K^\circ$; to estimate roughly whether a reaction is feasible |

Two common misconceptions: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ is not "$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ at equilibrium" (the latter is zero at equilibrium); and for a gas-phase reaction carried out at $101.325\,\mathrm{kPa}$ (or even $p^\circ$), $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is not equal to $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, because the standard state requires each gas to be at $p^\circ$ by itself, whereas in a mixture the partial pressures are lower than the total pressure. For the same reason $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ cannot be written as $(\partial G/\partial\xi)_{T,p^\circ}$.

### 7.4.2. Methods of Determination

1. From $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$: $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ is obtained from the **standard molar enthalpies of formation** and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ from the **standard molar entropies** ([6.1.6](/6.1.6)), and for other temperatures they are corrected with **Kirchhoff's law** ([6.3.1](/6.3.1)):

$$
\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\Delta_{\mathrm{r}}C_{p,\mathrm{m}}\,\mathrm{d}T, \qquad \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\frac{\Delta_{\mathrm{r}}C_{p,\mathrm{m}}}{T}\,\mathrm{d}T.
$$
One can also convert directly with the **Gibbs–Helmholtz equation** $\frac{\Delta G(T_2)}{T_2} - \frac{\Delta G(T_1)}{T_1} = -\int_{T_1}^{T_2}\frac{\Delta H}{T^2}\,\mathrm{d}T$. For rough estimates, take $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ to be their values at $298.15\,\mathrm{K}$.
2. From the **standard molar Gibbs energies of formation**: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\Delta_{\mathrm{f}}G^\circ_{\mathrm{m}}(\mathrm{B})$ ([6.1.6](/6.1.6#def-6.4.4)). $\Delta_{\mathrm{f}}G^\circ = 0$ for elements in their reference states; species in solution use the $b^\circ$ standard state, and one conventionally sets $\Delta_{\mathrm{f}}G^\circ(\ce{H+}, \mathrm{aq}) = 0$ (positive and negative ions cannot exist separately, so only combinations of ions can be determined; this convention yields a table of values for individual ions).
3. From known reactions: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ obeys **Hess's law** just as $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ does, and the corresponding $K^\circ$ values are multiplied or divided. For example, the equilibrium constant of $\ce{C(s) + 1/2O2(g) -> CO(g)}$ is hard to measure directly (some $\ce{CO2}$ always forms), but it follows from subtracting $\ce{CO + 1/2O2 -> CO2}$ from $\ce{C + O2 -> CO2}$: $K^\circ_3 = K^\circ_1/K^\circ_2$.
4. From the electromotive force of a reversible cell: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$ ([6.1.11](/6.1.11), [6.3.13](/6.3.13)).
5. From spectroscopic data and partition functions ([6.3.11](/6.3.11)).

**Example 7.4.1** Given $\Delta_{\mathrm{f}}G^\circ(\mathrm{s})$ of solid succinic acid at $298.15\,\mathrm{K}$ and the molality of its saturated aqueous solution, $b_{\mathrm{sat}} = 0.715\,\mathrm{mol\,kg^{-1}}$, find $\Delta_{\mathrm{f}}G^\circ(\mathrm{aq})$ of the solute succinic acid (standard state $b^\circ$). This is the key step in calculating the first dissociation constant $\ce{C4H6O4(aq) <=> C4H5O4^-(aq) + H+(aq)}$ from the $\Delta_{\mathrm{f}}G^\circ$ values of the ions.

**Solution** Design the path: $\ce{C4H6O4(s)} \to \ce{C4H6O4}$ in the saturated solution ($b_{\mathrm{sat}}$) $\to \ce{C4H6O4(aq)}$ in the standard state ($b^\circ$). The first step is a solid–liquid equilibrium, $\Delta G_1 = 0$. The second step is a change in solute concentration; neglecting activity coefficients, $\Delta G_2 = RT\ln(b^\circ/b_{\mathrm{sat}}) = 8.314 \times 298.15 \times \ln(1/0.715) = 0.83\,\mathrm{kJ\,mol^{-1}}$. Hence

$$
\Delta_{\mathrm{f}}G^\circ(\mathrm{aq}) = \Delta_{\mathrm{f}}G^\circ(\mathrm{s}) + RT\ln\frac{b^\circ}{b_{\mathrm{sat}}} = \Delta_{\mathrm{f}}G^\circ(\mathrm{s}) + 0.83\,\mathrm{kJ\,mol^{-1}}.
$$
The same idea converts $\Delta_{\mathrm{f}}G^\circ(\mathrm{l})$ of a pure liquid into $\Delta_{\mathrm{f}}G^\circ(\mathrm{g})$ of the gas by means of the saturated vapor pressure: $\Delta_{\mathrm{f}}G^\circ(\mathrm{g}) = \Delta_{\mathrm{f}}G^\circ(\mathrm{l}) + RT\ln(p^\circ/p^*)$. In a $0.7\,\mathrm{mol\,kg^{-1}}$ solution the activity coefficient is not exactly 1, which is the main source of error of the method.

### 7.4.3. Estimating Feasibility from $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$

The direction is decided by $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$. But when $\lvert\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}\rvert$ is large, $RT\ln Q$ cannot change its sign over the usual range of compositions, so $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ can be used for a rough estimate: at $298\,\mathrm{K}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +40\,\mathrm{kJ\,mol^{-1}}$ corresponds to $K^\circ = 1.0 \times 10^{-7}$; for the reaction to proceed forward one needs $Q < 10^{-7}$, which is generally unattainable, so the reaction can be regarded as essentially impossible; for $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < -40\,\mathrm{kJ\,mol^{-1}}$ the reaction essentially goes to completion; reactions in between can be driven in the desired direction by changing conditions (removing products, changing temperature or pressure). This boundary (some textbooks use $41.84\,\mathrm{kJ\,mol^{-1}} = 10\,\mathrm{kcal\,mol^{-1}}$) is only an order-of-magnitude rule of thumb: it depends on how the equation is written (the size of $\nu_{\mathrm{B}}$) and on temperature, and it answers only the question of thermodynamic feasibility, not that of rate.

### 7.4.4. The Turning Temperature

The temperature at which $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = 0$ ($K^\circ = 1$) is called the turning temperature: when $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ have the same sign, the direction of the reaction in the standard state changes there. Neglecting $\Delta_{\mathrm{r}}C_p$, $T_{\text{turn}} \approx \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(298.15\,\mathrm{K})/\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K})$. For the decomposition of $\ce{CaCO3}$ the estimate is $1119\,\mathrm{K}$ (data of [6.1.6 Example 6.4.5](/6.1.6#ex-6.4.5)), whereas the measured temperature at which the $\ce{CO2}$ decomposition pressure reaches $p^\circ$ is about $1170\,\mathrm{K}$; the difference comes from the variation of $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ over a temperature range of nearly $900\,\mathrm{K}$. For a decomposition reaction, the turning temperature is the temperature at which the decomposition pressure equals $p^\circ$.

## 7.5. Factors Affecting Equilibrium

Questions about the shift of equilibrium are in essence questions about the direction of reaction in a "new state": one compares $Q$ in the new state with $K^\circ$ at the new temperature. Temperature mainly changes $K^\circ$; pressure, inert components, and concentrations change $Q$.

### 7.5.1. Temperature

**Theorem 7.5.1 (van 't Hoff Equation)**

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}. \tag{7.6}
$$

**Proof** $\ln K^\circ = -\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT$. Since $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}}(T)$ is a function of temperature only, we apply the Gibbs–Helmholtz equation $\frac{\mathrm{d}(\mu^\circ_{\mathrm{B}}/T)}{\mathrm{d}T} = -\frac{H^\circ_{\mathrm{B}}}{T^2}$ to each substance ($H^\circ_{\mathrm{B}}$ is the molar enthalpy of B in the standard state, or the partial molar enthalpy at infinite dilution for a solute) and sum to get $\frac{\mathrm{d}(\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/T)}{\mathrm{d}T} = -\frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{T^2}$, which is Eq. (7.6). $\square$

This derivation does not assume that $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ is constant and is therefore more general than that of [6.1.8](/6.1.8#thm-8.4.1). There are two cases for integration:

1. $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} \approx 0$ or a small temperature range: $\ln\frac{K^\circ_2}{K^\circ_1} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$, and $\ln K^\circ$ is a straight line in $1/T$.
2. A large temperature range: express $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T)$ by Kirchhoff's law and integrate. If $C_{p,\mathrm{m}} = a + bT + c/T^2$, then $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) = \Delta H_0 + \Delta a\,T + \frac{\Delta b}{2}T^2 - \frac{\Delta c}{T}$ ($\Delta H_0$ is an integration constant fixed by the value at $298.15\,\mathrm{K}$), and substituting into Eq. (7.6) and integrating gives

$$
\ln K^\circ = -\frac{\Delta H_0}{RT} + \frac{\Delta a}{R}\ln T + \frac{\Delta b}{2R}T + \frac{\Delta c}{2RT^2} + I,
$$
where the integration constant $I$ is fixed by $K^\circ$ at one temperature. In practical calculations it is more convenient to integrate $\Delta_{\mathrm{r}}C_{p,\mathrm{m}}$ numerically.

**Example 7.5.1** Using the data of [6.1.8](/6.1.8) ($\Delta_{\mathrm{f}}H^\circ(\ce{NH3}) = -45.9\,\mathrm{kJ\,mol^{-1}}$; $S^\circ_{\mathrm{m}}$: $\ce{NH3}$ 192.8, $\ce{N2}$ 191.6, $\ce{H2}$ $130.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$) and the empirical heat-capacity expressions ($C_{p,\mathrm{m}}/(\mathrm{J\,mol^{-1}\,K^{-1}}) = a + bT + c/T^2$; $\ce{NH3}$: 29.75, $25.10 \times 10^{-3}$, $-1.55 \times 10^5$; $\ce{N2}$: 28.58, $3.77 \times 10^{-3}$, $-0.50 \times 10^5$; $\ce{H2}$: 27.28, $3.26 \times 10^{-3}$, $0.50 \times 10^5$), find $K^\circ$ of $\ce{1/2N2(g) + 3/2H2(g) <=> NH3(g)}$ at $723\,\mathrm{K}$.

**Solution** At $298.15\,\mathrm{K}$, $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -45.9\,\mathrm{kJ\,mol^{-1}}$, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = -99.05\,\mathrm{J\,mol^{-1}\,K^{-1}}$, and $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = -22.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$ ($-12.6$ at $723\,\mathrm{K}$). Integrating Kirchhoff's law numerically: $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -53.1\,\mathrm{kJ\,mol^{-1}}$, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -114.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 29.8\,\mathrm{kJ\,mol^{-1}}$, and $K^\circ = 7.0 \times 10^{-3}$. If $\Delta_{\mathrm{r}}C_p$ is neglected, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -45.9 + 723 \times 0.09905 = 25.7\,\mathrm{kJ\,mol^{-1}}$ and $K^\circ = 1.4 \times 10^{-2}$, too large by a factor of two. The experimental value in the literature at $723\,\mathrm{K}$ is about $6.4 \times 10^{-3}$; an error of $1\,\mathrm{kJ\,mol^{-1}}$ in $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ changes $K^\circ$ by $18\%$ at this temperature, so high-temperature equilibrium constants demand very accurate data.

![van 't Hoff plot for ammonia synthesis (½N₂ + 3/2H₂ ⇌ NH₃): the straight line that neglects ΔrCp and the curve that includes the heat capacities diverge markedly at high temperature (left); temperature dependence of the reaction heat capacity (right)](./plots/ammonia-heat-capacity.py)

Qualitatively, raising the temperature increases $K^\circ$ for an endothermic reaction and decreases it for an exothermic one. A common puzzle: for a reaction with $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} > 0$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} < 0$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ increases with temperature, so does $K^\circ$ decrease? No: what determines $K^\circ$ is $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/T = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/T - \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$, which decreases as $T$ rises, so $K^\circ$ increases, in agreement with the van 't Hoff equation (even though $K^\circ$ remains less than 1). For an exothermic reaction, low temperature favors the equilibrium, but in production one cannot simply keep lowering the temperature: at too low a temperature the reaction is too slow, and a compromise between equilibrium and rate must be made (ammonia synthesis, [6.1.8](/6.1.8)).

### 7.5.2. Pressure

Pressure does not change $K^\circ$ but does change $Q$. For an ideal-gas reaction, by Eq. (7.5), $K_x = K^\circ(p/p^\circ)^{-\Delta\nu_{\mathrm{g}}}$: for $\Delta\nu_{\mathrm{g}} < 0$, raising the pressure increases $K_x$ and shifts the equilibrium toward fewer gas molecules; for $\Delta\nu_{\mathrm{g}} > 0$ the opposite holds; for $\Delta\nu_{\mathrm{g}} = 0$ the equilibrium is unaffected by pressure. Reactions in condensed phases are affected very little, in a direction determined by $\Delta_{\mathrm{r}}V$ (7.5.4), and appreciably only at high pressure (for example the conversion of graphite to diamond, [6.3.3](/6.3.3)).

At high pressure gases are not ideal and fugacities must be used:

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{\varphi_{\mathrm{B}}p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}} = K_x\left(\frac{p}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}\prod_{\mathrm{B}}\varphi_{\mathrm{B}}^{\nu_{\mathrm{B}}}.
$$
The **fugacity coefficients** of the components in a mixture are approximated, according to the **Lewis–Randall rule**, by those of the pure gases at the same temperature and pressure, which are read from generalized fugacity-coefficient charts in terms of reduced variables or calculated from an equation of state ([6.3.4](/6.3.4)).

**Example 7.5.2** At $723\,\mathrm{K}$, $K^\circ = 6.4 \times 10^{-3}$ for $\ce{1/2N2(g) + 3/2H2(g) <=> NH3(g)}$ (the experimental value at the end of Example 7.5.1), and the feed has $n(\ce{N2}) : n(\ce{H2}) = 1 : 3$. (1) With the total pressure kept at $100\,\mathrm{kPa}$, find the equilibrium conversion; (2) at a total pressure of $30\,\mathrm{MPa}$, treating the gases as ideal; (3) at a total pressure of $30\,\mathrm{MPa}$, with fugacity coefficients $\varphi(\ce{N2}) = 1.15$, $\varphi(\ce{H2}) = 1.09$, $\varphi(\ce{NH3}) = 0.87$.

**Solution** Let $x$ mol of $\ce{N2}$ react (per $1\,\mathrm{mol}$ of $\ce{N2}$): $\ce{N2}$ $1 - x$, $\ce{H2}$ $3(1 - x)$, $\ce{NH3}$ $2x$, total $4 - 2x$.

$$
K^\circ = \frac{2x(4 - 2x)}{3^{3/2}(1 - x)^2}\cdot\frac{p^\circ}{p}\cdot\frac{\varphi_{\ce{NH3}}}{\varphi_{\ce{N2}}^{1/2}\varphi_{\ce{H2}}^{3/2}}.
$$
(1) $p = p^\circ$, $\varphi = 1$: $x = 0.0041$, a conversion of $0.41\%$. (2) $p = 300p^\circ$: $x = 0.465$, a conversion of $46.5\%$, $y(\ce{NH3}) = 0.303$. (3) $\prod\varphi_{\mathrm{B}}^{\nu_{\mathrm{B}}} = 0.87/(1.15^{1/2} \times 1.09^{3/2}) = 0.713$, which amounts to enlarging $K_x$ by a factor of $1/0.713 = 1.40$: $x = 0.529$, a conversion of $52.9\%$, $y(\ce{NH3}) = 0.359$. The measured equilibrium ammonia content at $450\,^\circ\mathrm{C}$ and about $30\,\mathrm{MPa}$ is about $36\%$, in agreement with the fugacity-corrected result. The fugacity coefficient of $\ce{NH3}$ is less than 1 (strong intermolecular attraction), whereas those of $\ce{N2}$ and $\ce{H2}$ are greater than 1 (far above their critical temperatures, repulsion dominates); the non-ideality shifts the equilibrium further to the right.

![Equilibrium mole fraction of ammonia versus total pressure at 723 K for a 1 : 3 feed: ideal gas and with the fugacity correction (fugacity coefficients taken at 30 MPa, with ln φ extrapolated linearly in pressure)](./plots/ammonia-fugacity.py)

### 7.5.3. Inert Components

A gas that does not take part in the reaction (such as Ar, $\ce{CH4}$, or water vapor) is called an inert component. At constant temperature and pressure, adding an inert component lowers the partial pressures of the reacting gases by the same factor, which is equivalent to reducing the pressure on the reaction system: the equilibrium shifts toward more gas molecules. At constant temperature and volume, adding an inert component leaves all partial pressures unchanged for an ideal-gas reaction, so the equilibrium does not shift; for high-pressure gases the fugacity coefficients change with the total pressure, and the equilibrium shifts slightly.

**Example 7.5.3** At $900\,\mathrm{K}$, $K^\circ = 2.7$ for the dehydrogenation of ethylbenzene $\ce{C6H5C2H5(g) <=> C6H5C2H3(g) + H2(g)}$. Starting from $1\,\mathrm{mol}$ of ethylbenzene, find the amount of styrene at equilibrium: (a) at a total pressure of $p^\circ$; (b) at a total pressure of $0.1p^\circ$; (c) at a total pressure of $p^\circ$ with $10\,\mathrm{mol}$ of water vapor added.

**Solution** Let $x\,\mathrm{mol}$ of styrene form; ethylbenzene is $1 - x$, $\ce{H2}$ is $x$, and the total is $1 + x + n_{\mathrm{inert}}$.

$$
K^\circ = \frac{x^2}{(1 - x)(1 + x + n_{\mathrm{inert}})}\cdot\frac{p}{p^\circ}.
$$
(a) $n_{\mathrm{inert}} = 0$, $p = p^\circ$: $x^2/(1 - x^2) = 2.7$, $x = 0.85\,\mathrm{mol}$. (b) $p = 0.1p^\circ$: $x = 0.98\,\mathrm{mol}$. (c) $n_{\mathrm{inert}} = 10$: $x = 0.97\,\mathrm{mol}$. Adding water vapor has nearly the same effect as reducing the pressure, and it allows operation at atmospheric pressure, avoiding vacuum equipment and the danger of air leaking in; industrially the steam also supplies heat and suppresses coking.

### 7.5.4. Concentration and Le Chatelier's Principle

Adding a reactant or removing a product decreases $Q$ and shifts the equilibrium forward; industrially one often uses an excess of the cheap feed, or continually removes the product (by crystallization, distillation, or absorption) to raise the conversion of the valuable feed. But adding one reactant at constant pressure does not necessarily shift the equilibrium forward: the added substance also dilutes the other components. [Example 8.4.2 of 6.1.8](/6.1.8#ex-8.4.2) has shown that when $\ce{N2}$ is added at constant temperature and pressure to an ammonia-synthesis equilibrium, the equilibrium actually shifts to the left once $x(\ce{N2}) > 1/2$.

**Example 7.5.4** For $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$ at a certain temperature and total pressure $p^\circ$, the equilibrium amounts are $n(\ce{N2}) = 3.00\,\mathrm{mol}$ and $n(\ce{H2}) = n(\ce{NH3}) = 1.00\,\mathrm{mol}$. At constant temperature and total pressure, (1) add $0.10\,\mathrm{mol}$ of $\ce{N2}$; (2) increase $\ce{H2}$ to $3.10\,\mathrm{mol}$. In which direction does the equilibrium shift?

**Solution** At equilibrium the mole fractions are $0.6$, $0.2$, $0.2$, and $K^\circ = \frac{0.2^2}{0.6 \times 0.2^3} = 8.33$ ($p = p^\circ$). (1) The total is $5.1\,\mathrm{mol}$, $Q = \frac{(1/5.1)^2}{(3.1/5.1)(1/5.1)^3} = 8.39 > K^\circ$, so the equilibrium shifts to the left: here $x(\ce{N2}) = 0.6 > 1/2$. (2) The total is $7.1\,\mathrm{mol}$, $Q = \frac{(1/7.1)^2}{(3/7.1)(3.1/7.1)^3} = 0.564 < K^\circ$, so the equilibrium shifts to the right. When several factors change simultaneously, qualitative rules cannot simply be applied; the reliable method is always to compare $Q$ in the new state with $K^\circ$.

In 1884 Le Chatelier summarized the regularities of equilibrium shift in an empirical principle (**Le Chatelier's principle**, [6.1.8](/6.1.8#sec-8.4.4)). The conditions under which its qualitative statement holds rigorously can be derived from thermodynamics.

**Theorem 7.5.2 (Le Chatelier's Principle)** Let the system be in stable chemical equilibrium at $T$ and $p$. Then

$$
\left(\frac{\partial\xi_{\mathrm{eq}}}{\partial T}\right)_p = \frac{\Delta_{\mathrm{r}}H_{\mathrm{m}}}{TG_{\xi\xi}}, \qquad \left(\frac{\partial\xi_{\mathrm{eq}}}{\partial p}\right)_T = -\frac{\Delta_{\mathrm{r}}V_{\mathrm{m}}}{G_{\xi\xi}}, \qquad G_{\xi\xi} = \left(\frac{\partial^2G}{\partial\xi^2}\right)_{T,p} > 0,
$$
where $\Delta_{\mathrm{r}}H_{\mathrm{m}} = \sum\nu_{\mathrm{B}}H_{\mathrm{B}}$ and $\Delta_{\mathrm{r}}V_{\mathrm{m}} = \sum\nu_{\mathrm{B}}V_{\mathrm{B}}$ are the molar reaction enthalpy and molar reaction volume at the equilibrium composition (sums of partial molar quantities). Hence raising the temperature shifts the equilibrium in the endothermic direction, and raising the pressure shifts it in the direction of decreasing volume.

**Proof** The equilibrium position is determined by $\Delta_{\mathrm{r}}G_{\mathrm{m}}(T, p, \xi_{\mathrm{eq}}) = 0$. Differentiating along the equilibrium line:

$$
\left(\frac{\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}}{\partial T}\right)_{p,\xi}\mathrm{d}T + \left(\frac{\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}}{\partial p}\right)_{T,\xi}\mathrm{d}p + G_{\xi\xi}\,\mathrm{d}\xi_{\mathrm{eq}} = 0.
$$
From $(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = -S_{\mathrm{B}}$ and $(\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = V_{\mathrm{B}}$, the first two coefficients are $-\Delta_{\mathrm{r}}S_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}V_{\mathrm{m}}$; at equilibrium $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}} - T\Delta_{\mathrm{r}}S_{\mathrm{m}} = 0$, so $\Delta_{\mathrm{r}}S_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}}/T$. Substitution gives both formulas. Equilibrium is a minimum of $G$, and stability requires $G_{\xi\xi} > 0$ (for an ideal mixture this always holds because of the convexity of the Gibbs energy of mixing). $\square$

The theorem shows that for intensive variables such as temperature and pressure, Le Chatelier's principle is rigorous: the response of the system (heat absorption, volume decrease) "weakens" the external change, with the sign guaranteed by the stability condition $G_{\xi\xi} > 0$. For an ideal gas, $\Delta_{\mathrm{r}}V_{\mathrm{m}} = \Delta\nu_{\mathrm{g}}RT/p$, which recovers the conclusion of 7.5.2. But for an extensive variable such as "the amount of a component added" there is no general rule for the sign: the added substance changes the mole fractions of all components, and the outcome depends on the composition (see the examples above). This is the limitation of the principle, and it shows that it is only a qualitative summary of thermodynamic results.

A catalyst lowers the activation energies of the forward and reverse reactions equally; it does not change $K^\circ$, the equilibrium does not shift, and only the time to reach equilibrium is shortened.

## 7.6. Simultaneous Equilibria and Coupled Reactions

### 7.6.1. Simultaneous Equilibria

**Definition 7.6.1** When several reactions proceed in a system at the same time and some species take part in two or more of them, the state in which all the reactions are at equilibrium simultaneously is called **simultaneous equilibria**.

At equilibrium every independent reaction satisfies its own condition $\sum_{\mathrm{B}}\nu_{\mathrm{B}j}\mu_{\mathrm{B}} = 0$ and thus has its own $K^\circ_j$; the activity of a given species is the same in all the equilibrium-constant expressions. The number of independent reactions equals the rank of the stoichiometric matrix $(\nu_{\mathrm{B}j})$: the other reactions are linear combinations of the independent ones and their equilibrium conditions are satisfied automatically (this number also determines the number of independent components in the phase rule, [6.3.8](/6.3.8)). In calculations one solves for several extents of reaction simultaneously; the equivalent approach is to minimize $G$ directly under the constraints of element conservation, which is precisely the method (Gibbs energy minimization) used for complex equilibrium calculations in chemical engineering and geochemistry.

For example, the chlorination of titanium dioxide ($298.15\,\mathrm{K}$, CRC data):

$$
\begin{aligned}
&(1)\ \ce{TiO2(s) + 2Cl2(g) -> TiCl4(l) + O2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +151.6\,\mathrm{kJ\,mol^{-1}}, \\
&(2)\ \ce{C(s) + O2(g) -> CO2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -394.4\,\mathrm{kJ\,mol^{-1}}, \\
&(3) = (1) + (2)\ \ce{TiO2(s) + C(s) + 2Cl2(g) -> TiCl4(l) + CO2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -242.8\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
Reaction (1) alone is thermodynamically unfavorable, but once carbon is added the overall reaction (3) is highly favorable; this is the industrial route from rutile to $\ce{TiCl4}$ (and then to titanium). It is often said that reaction (2) "drives" reaction (1), but thermodynamically this is a simultaneous equilibrium: in the presence of hot carbon the partial pressure of $\ce{O2}$ is held extremely low, $Q$ of reaction (1) is extremely small, and its own $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$ is already negative; the two reactions each proceed spontaneously to the right, and the role of carbon is to remove the product $\ce{O2}$ continually.

### 7.6.2. Coupled Reactions

**Definition 7.6.2** Two reactions that are linked through a common intermediate or the same reaction mechanism, so that one of them can proceed only together with the other in a fixed ratio, are called **coupled reactions**. By means of a reaction with a very negative $\Delta_{\mathrm{r}}G_{\mathrm{m}}$, a reaction with $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ can be made to proceed.

Thermodynamics requires only that the coupled overall reaction satisfy $\Delta_{\mathrm{r}}G_{\mathrm{m}}(1) + \Delta_{\mathrm{r}}G_{\mathrm{m}}(2) < 0$ (counted in the coupled stoichiometric ratio). "Coupling" itself is a mechanistic fact that thermodynamics cannot guarantee: two reactions proceeding separately in the same vessel do not drive each other; a common intermediate (such as a phosphorylated substrate) or a molecular machine is needed to lock their progress together. When the coupling is incomplete, the ratio of the two reaction rates can vary, a situation that belongs to the coupling of fluxes in non-equilibrium thermodynamics ([6.3.18](/6.3.18)).

The most important coupling in living organisms is the hydrolysis of ATP. In biochemistry one uses the biochemical standard state: $\mathrm{pH} = 7$ (that is, $a_{\ce{H+}} = 10^{-7}$ rather than 1), the activity of water taken as 1, and fixed $\ce{Mg^2+}$ concentration and ionic strength; the corresponding standard molar reaction Gibbs energy is written $\Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}}$. For a reaction in which $\ce{H+}$ takes part, $\Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + \nu_{\ce{H+}}RT\ln 10^{-7}$; this is merely a change of standard state ([6.3.6](/6.3.6)), and the form of the isotherm is unchanged.

$$
\begin{aligned}
&\text{ATP} + \ce{H2O} \longrightarrow \text{ADP} + \mathrm{P_i}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = -30.5\,\mathrm{kJ\,mol^{-1}}, \\
&\text{glucose} + \mathrm{P_i} \longrightarrow \text{glucose 6-phosphate} + \ce{H2O}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = +13.8\,\mathrm{kJ\,mol^{-1}}, \\
&\text{glucose} + \text{ATP} \longrightarrow \text{glucose 6-phosphate} + \text{ADP}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = -16.7\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
($\mathrm{P_i}$ is inorganic phosphate.) The first step of glycolysis is catalyzed by hexokinase, and the phosphoryl group is transferred directly from ATP to glucose: the enzyme combines "ATP hydrolysis" and "glucose phosphorylation" into a single reaction, so that the phosphorylation alone ($K^{\circ\prime} = 4 \times 10^{-3}$) becomes a favorable reaction with $K^{\circ\prime} = 8 \times 10^2$. The coupling here is stoichiometric: the two "half-reactions" never occur separately.

The driving force in the cell is determined by actual concentrations. Taking the human erythrocyte as an example, with $[\text{ATP}] = 2.25\,\mathrm{mmol\,L^{-1}}$, $[\text{ADP}] = 0.25\,\mathrm{mmol\,L^{-1}}$, and $[\mathrm{P_i}] = 1.65\,\mathrm{mmol\,L^{-1}}$, at $37\,^\circ\mathrm{C}$

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} + RT\ln\frac{[\text{ADP}][\mathrm{P_i}]}{[\text{ATP}]\,c^\circ} = -30.5 + 2.58\ln\frac{0.25 \times 10^{-3} \times 1.65 \times 10^{-3}}{2.25 \times 10^{-3}} = -52.7\,\mathrm{kJ\,mol^{-1}},
$$
much more negative than the standard value: the cell continually regenerates ATP through respiration, keeping the ATP/ADP ratio far from equilibrium (at the above $[\mathrm{P_i}]$, the equilibrium $[\text{ATP}]/[\text{ADP}]$ would be only about $10^{-8}$, whereas in the cell it is about 9), so the driving force of ATP hydrolysis stays at about $-50\,\mathrm{kJ\,mol^{-1}}$. Living systems are open systems and maintain this state far from equilibrium by a continuous flow of matter and energy ([6.3.18](/6.3.18)). The commonly mentioned "high-energy phosphate bond" is a misnomer: $-30.5\,\mathrm{kJ\,mol^{-1}}$ is the Gibbs energy change of the entire reaction in aqueous solution, arising from the resonance stabilization of the products, the relief of charge repulsion, and solvation, and not from energy stored in a particular bond (breaking a bond is always endothermic).

## Summary

| Topic | Key points |
|---|---|
| Nature of equilibrium | $G(\xi)$ = linear term + $\Delta_{\mathrm{mix}}G$; mixing puts the minimum in the interior; reactions among pure condensed phases can go to completion |
| Equilibrium condition | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = (\partial G/\partial\xi)_{T,p} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$, independent of the constraint, valid for multiple phases |
| Isotherm and $K^\circ$ | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$; $K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT) = \prod(a_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}}$; depends on $T$, the standard state, and the way the equation is written, not on pressure |
| Various systems | gases $f/p^\circ$, solutions $\gamma x$ or $\gamma b/b^\circ$, pure condensed phases $a = 1$; decomposition pressure; $K^\circ = K_x(p/p^\circ)^{\Delta\nu_{\mathrm{g}}}$ |
| $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ | from $\Delta H^\circ - T\Delta S^\circ$ (Kirchhoff correction), $\Delta_{\mathrm{f}}G^\circ$, combination of reactions, EMF, partition functions; $\pm 40\,\mathrm{kJ\,mol^{-1}}$ as a rough guide; turning temperature $\Delta H^\circ/\Delta S^\circ$ |
| Temperature | $\mathrm{d}\ln K^\circ/\mathrm{d}T = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/RT^2$; include $\Delta_{\mathrm{r}}C_p$ over wide temperature ranges |
| Pressure and inert components | change $Q$, not $K^\circ$; use fugacities at high pressure; adding an inert component at constant pressure is equivalent to reducing the pressure |
| Le Chatelier's principle | rigorous for $T$ and $p$: $(\partial\xi/\partial T)_p \propto \Delta_{\mathrm{r}}H$, $(\partial\xi/\partial p)_T \propto -\Delta_{\mathrm{r}}V$; no general rule for added components |
| Simultaneous equilibria and coupling | each independent reaction satisfies its own equilibrium condition; coupling needs a common intermediate or mechanism and a negative overall $\Delta_{\mathrm{r}}G$; ATP hydrolysis is about $-50\,\mathrm{kJ\,mol^{-1}}$ in the cell |

## Questions

1. For the reaction $\ce{2H2(g) + O2(g) <=> 2H2O(g)}$, if the amounts of the three substances are in the ratios $1:1:1$ and $2:1:2$, with other conditions the same, which of $K^\circ$, $Q$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ are the same?
   Answer: $K^\circ$ and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ depend only on temperature and are the same; $Q$ and $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ vary with composition and are different.
2. Is it correct that "if different standard states are chosen, $\mu^\circ_{\mathrm{B}}$ differs, so $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ differs, but $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is the same"? Is it correct that "if the equilibrium has shifted, the equilibrium constant must have changed"?
   Answer: The former is correct, since $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ is determined by the state of the system; the latter is wrong, since changing the pressure or concentration can shift the equilibrium while $K^\circ$ stays the same.
3. Can one say that every chemical reaction has a chemical equilibrium, that the equilibrium constant of a reaction that "cannot occur" is zero, and that that of a reaction that "goes to completion" is infinite?
   Answer: No. $K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT)$ is always a finite positive number, though it can be very large or very small. On the other hand, when reactants and products are all pure condensed phases that do not mix (7.1.1), the system has no composition to adjust, and apart from the temperature at which $K^\circ$ happens to equal 1 there is no equilibrium state: the reaction either goes to completion or does not proceed.
