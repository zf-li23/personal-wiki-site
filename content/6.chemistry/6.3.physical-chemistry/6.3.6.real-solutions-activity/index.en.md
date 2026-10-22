---
title: "Real Solutions: Activities and Excess Functions"
source_hash: 9b41c36938b6
---

The two kinds of ideal solution in [6.3.5](/6.3.5) are only limits: an ideal liquid mixture requires the molecules of all components to be nearly identical, and an ideal dilute solution requires the solute to be infinitely dilute. At finite concentrations every real solution deviates from Raoult's law and Henry's law, and the direction and size of the deviation reflect the intermolecular interactions. Lewis's remedy is exactly parallel to the introduction of the **fugacity** for real gases ([6.3.4](/6.3.4)): keep the form of the chemical potential of an ideal solution but replace the concentration by an "effective concentration", the **activity**, so that the departure from ideality is concentrated in the activity coefficient. This chapter first describes the deviations (6.1), then defines the activity and the activity coefficient and discusses the choice of standard state (6.2), and presents methods for measuring activities (6.3). It then describes the nonideality of the solution as a whole by means of excess functions, taking the one-parameter regular solution model as an example (6.4), and finally treats the distribution of a solute between two immiscible solvents and extraction (6.5). Activities are the basis for writing the general equilibrium constant in [6.3.7](/6.3.7); the activities of electrolyte solutions (mean activity, Debye–Hückel theory) are left to [6.3.12](/6.3.12), and the determination of activities from cell potentials is discussed in [6.3.13](/6.3.13).

## 6.1. Deviations from Raoult's Law

In a real liquid mixture, a component whose vapor partial pressure is higher than Raoult's law predicts ($p_{\mathrm{B}} > p^*_{\mathrm{B}}x_{\mathrm{B}}$) is said to show a positive deviation, and one whose partial pressure is lower than predicted shows a negative deviation. In a binary system the two components usually deviate in the same direction, and the total-pressure curve bends upward or downward accordingly; when the deviation is large enough the total pressure passes through a maximum or a minimum, corresponding to an azeotrope ([6.3.9](/6.3.9)).

The molecular origin of the deviation is that the A–B interaction differs from the A–A and B–B interactions:

| Type | Molecular origin | Examples | $\Delta_{\mathrm{mix}}H$ |
|---|---|---|---|
| Positive deviation | The A–B attraction is weaker than the attraction within the pure components; mixing breaks up the association of one component (e.g., hydrogen bonds in an alcohol) | acetone–carbon disulfide, ethanol–water, ethanol–benzene, benzene–cyclohexane | usually positive (endothermic) |
| Negative deviation | The A–B attraction is stronger, or the two components form hydrogen bonds or complexes | chloroform–acetone ($\ce{C-H\cdots O=C}$ hydrogen bond), water–nitric acid, water–HCl | usually negative (exothermic) |

However large the deviation, at the end $x_{\mathrm{A}} \to 1$ the component A always obeys Raoult's law and B always obeys Henry's law; the reverse holds at the other end. The direction of the deviation also determines how the Henry constant compares with the vapor pressure of the pure component: $k_{x,\mathrm{B}} = p^*_{\mathrm{B}}$ for an ideal solution, $k_{x,\mathrm{B}} > p^*_{\mathrm{B}}$ for a positive deviation, and $k_{x,\mathrm{B}} < p^*_{\mathrm{B}}$ for a negative deviation (see the dotted and dashed lines in the figure below). There is still no unified theory that applies to all nonideal solutions; the task of thermodynamics is to describe the deviations clearly by means of a few measurable quantities (activity coefficients or excess functions) and to ensure that these are mutually consistent.

![Vapor pressures given by the one-parameter Margules model (6.4.3), p*_A = 40 kPa, p*_B = 60 kPa: dashed lines show Raoult's law and dotted lines the Henry's law tangents at the two ends; left, positive deviation (the total pressure has a maximum); right, negative deviation](./plots/margules-deviations.py)

## 6.2. Activity and Activity Coefficient

### 6.2.1. Definition

In an ideal liquid mixture $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}$, and in an ideal dilute solution the solute has $\mu_{\mathrm{B}} = \mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$ ([6.3.5](/6.3.5)). For a real solution we keep this form and correct the concentration.

**Definition 6.2.1 (Activity)** Once a reference state for component B has been chosen (at the same temperature and pressure as the solution, with chemical potential $\mu^{\mathrm{ref}}_{\mathrm{B}}(T, p)$), write the chemical potential of B in the solution as

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) + RT\ln a_{\mathrm{B}},
$$
The dimensionless quantity $a_{\mathrm{B}}$ is called the activity of B; the ratio of the activity to the corresponding concentration is called the **activity coefficient** of B. There are two kinds of reference state:

1. Following Raoult's law (for the solvent, or for components of a mixture that are treated on an equal footing): the reference state is pure liquid B at the same temperature and pressure, $\mu^{\mathrm{ref}}_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$, $a_{\mathrm{B}} = \gamma_{\mathrm{B}}x_{\mathrm{B}}$, and $\gamma_{\mathrm{B}} \to 1$ as $x_{\mathrm{B}} \to 1$;
2. Following Henry's law (for solutes): the reference state is the hypothetical state at $x_{\mathrm{B}} = 1$, $b_{\mathrm{B}} = b^\circ$ or $c_{\mathrm{B}} = c^\circ$ in which B would still obey Henry's law, with $a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}x_{\mathrm{B}}$, $a_{b,\mathrm{B}} = \gamma_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ$, $a_{c,\mathrm{B}} = \gamma_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$, and all three activity coefficients tend to 1 as $x_{\mathrm{B}} \to 0$.

For ideal gases and dilute solutions this definition reduces to the informal notion of activity in [6.1.8](/6.1.8#def-8.3.1); the present chapter gives its rigorous form. When the vapor can be treated as an ideal gas, Definition 6.2.1 is equivalent to the two corrected laws

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}a_{\mathrm{A}} = \gamma_{\mathrm{A}}p^*_{\mathrm{A}}x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}k_{x,\mathrm{B}}x_{\mathrm{B}}. \tag{6.1}
$$
The activity coefficient measures the departure from ideal behavior: relative to Raoult's law, $\gamma_{\mathrm{B}} > 1$ is a positive deviation and $\gamma_{\mathrm{B}} < 1$ a negative deviation, and the larger $\lvert\gamma_{\mathrm{B}} - 1\rvert$, the less ideal the behavior. In general $\gamma_{\mathrm{B}} = \gamma_{\mathrm{B}}(T, p, x_{\mathrm{B}}, x_{\mathrm{C}}, \dots)$, and it is determined mainly by experiment (6.3) or from molecular models (6.4.3), which is one of the central tasks of solution thermodynamics.

The meaning of the activity is that of an "effective concentration": it is the concentration that must be used for the formulas of ideal solutions to remain valid in a real solution. The activity coefficient corresponds to the fugacity coefficient $\varphi_{\mathrm{B}}$: the fugacity corrects the pressure, the activity corrects the concentration.

### 6.2.2. The Four Standard States

When the pressure of the reference state is fixed at $p^\circ$, the reference state becomes a **standard state**, and the chemical potential is a function of temperature only. There are four customary choices:

| Basis of treatment | Standard state ($T$, $p^\circ$) | Activity | Limiting condition | Integrand of the pressure term | Reality |
|---|---|---|---|---|---|
| Raoult's law $p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}}$ | pure liquid B | $a_{\mathrm{B}} = \gamma_{\mathrm{B}}x_{\mathrm{B}}$ | $x_{\mathrm{B}} \to 1$, $\gamma_{\mathrm{B}} \to 1$ | $V^*_{\mathrm{m,B}}$ | real |
| Henry's law ($x$) | $x_{\mathrm{B}} = 1$, still obeying Henry's law | $a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}x_{\mathrm{B}}$ | $x_{\mathrm{B}} \to 0$, $\gamma_{x,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | hypothetical |
| Henry's law ($b$) | $b_{\mathrm{B}} = b^\circ$, still obeying Henry's law | $a_{b,\mathrm{B}} = \gamma_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ$ | $b_{\mathrm{B}} \to 0$, $\gamma_{b,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | hypothetical |
| Henry's law ($c$) | $c_{\mathrm{B}} = c^\circ$, still obeying Henry's law | $a_{c,\mathrm{B}} = \gamma_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$ | $c_{\mathrm{B}} \to 0$, $\gamma_{c,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | hypothetical |

In the standard state both the activity and the activity coefficient equal 1. In an ideal liquid mixture $\gamma_{\mathrm{B}} = 1$ and $a_{\mathrm{B}} = x_{\mathrm{B}}$; in an ideal dilute solution the solvent has $\gamma_{\mathrm{A}} = 1$, all three activity coefficients of the solute equal 1, and the three activities are $x_{\mathrm{B}}$, $b_{\mathrm{B}}/b^\circ$, and $c_{\mathrm{B}}/c^\circ$, respectively.

Two points deserve attention. First, $a = 1$ does not mean that the substance is in its standard state: the standard state also specifies the pressure $p^\circ$ and the purity (or the environment of infinite dilution). In a solution with $x_{\mathrm{A}} = 0.3$ and $a_{\mathrm{A}} = 1$, the chemical potential of A equals that of pure A and its partial vapor pressure equals the saturated vapor pressure of pure A, yet A is not in its standard state, nor is the solution ideal. Second, for a component B treated by Raoult's law, $x_{\mathrm{B}} = 1$ is pure B; when B is treated by Henry's law, even $x_{\mathrm{B}} = 1$ is not the hypothetical standard state, and $\gamma_{x,\mathrm{B}}(x_{\mathrm{B}} = 1) = p^*_{\mathrm{B}}/k_{x,\mathrm{B}}$.

### 6.2.3. Changing the Standard State

For a solution in a given state, $\mu_{\mathrm{B}}$ and $p_{\mathrm{B}}$ are uniquely determined, whereas the activity and the activity coefficient change with the standard (reference) state. By Eq. (6.1), the same $p_{\mathrm{B}}$ can be written as

$$
p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = k_{b,\mathrm{B}}a_{b,\mathrm{B}} = k_{c,\mathrm{B}}a_{c,\mathrm{B}},
$$
so the ratio of the activities in different standard states is a constant equal to $\exp[(\mu^{\mathrm{ref}}_1 - \mu^{\mathrm{ref}}_2)/RT]$. In particular,

$$
\frac{\gamma_{\mathrm{B}}}{\gamma_{x,\mathrm{B}}} = \frac{k_{x,\mathrm{B}}}{p^*_{\mathrm{B}}} = \gamma^{\infty}_{\mathrm{B}}, \qquad \gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}}. \tag{6.2}
$$
In the first relation $\gamma^{\infty}_{\mathrm{B}}$ is the limit at infinite dilution of the activity coefficient defined by Raoult's law (let $x_{\mathrm{B}} \to 0$, so that $\gamma_{x,\mathrm{B}} \to 1$). The second follows from $k_{b,\mathrm{B}} = k_{x,\mathrm{B}}M_{\mathrm{A}}b^\circ$ (Eq. (5.5)) and $M_{\mathrm{A}}b_{\mathrm{B}} = n_{\mathrm{B}}/n_{\mathrm{A}} = x_{\mathrm{B}}/x_{\mathrm{A}}$: $\gamma_{b,\mathrm{B}} = \frac{a_{b,\mathrm{B}}}{b_{\mathrm{B}}/b^\circ} = \frac{a_{x,\mathrm{B}}}{M_{\mathrm{A}}b_{\mathrm{B}}} = \frac{\gamma_{x,\mathrm{B}}x_{\mathrm{B}}}{x_{\mathrm{B}}/x_{\mathrm{A}}}$. Even when the solution is an ideal dilute solution ($\gamma_{x,\mathrm{B}} = 1$), $\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}$ is slightly less than 1; this merely reflects the fact that $b_{\mathrm{B}}$ is not strictly proportional to $x_{\mathrm{B}}$.

**Example 6.2.1** For an aqueous solution of a solute B, the tangent to the vapor pressure–composition curve of B at $x_{\mathrm{B}} \to 0$, extrapolated to $x_{\mathrm{B}} = 1$, gives $k_{x,\mathrm{B}} = 150\,\mathrm{kPa}$, and the saturated vapor pressure of pure B is $p^*_{\mathrm{B}} = 50\,\mathrm{kPa}$. (1) Find the relations among the three activities $a_{\mathrm{B}}$ (Raoult), $a_{x,\mathrm{B}}$, and $a_{b,\mathrm{B}}$. Find the three activities and activity coefficients as (2) $x_{\mathrm{B}} \to 0$ and (3) $x_{\mathrm{B}} \to 1$.

**Solution** (1) From $p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = k_{b,\mathrm{B}}a_{b,\mathrm{B}}$,

$$
\frac{a_{\mathrm{B}}}{a_{x,\mathrm{B}}} = \frac{k_{x,\mathrm{B}}}{p^*_{\mathrm{B}}} = 3, \qquad \frac{a_{x,\mathrm{B}}}{a_{b,\mathrm{B}}} = \frac{k_{b,\mathrm{B}}}{k_{x,\mathrm{B}}} = M_{\mathrm{A}}b^\circ = 0.018015.
$$

(2) As $x_{\mathrm{B}} \to 0$, B obeys Henry's law: $\gamma_{x,\mathrm{B}} = \gamma_{b,\mathrm{B}} = 1$, $a_{x,\mathrm{B}} = x_{\mathrm{B}}$, $a_{b,\mathrm{B}} = b_{\mathrm{B}}/b^\circ$; whereas $a_{\mathrm{B}} = 3x_{\mathrm{B}}$ and $\gamma_{\mathrm{B}} = 3$ (positive deviation).

(3) As $x_{\mathrm{B}} \to 1$, B obeys Raoult's law: $\gamma_{\mathrm{B}} = 1$, $a_{\mathrm{B}} = x_{\mathrm{B}}$; $a_{x,\mathrm{B}} = p^*_{\mathrm{B}}x_{\mathrm{B}}/k_{x,\mathrm{B}} = x_{\mathrm{B}}/3$, $\gamma_{x,\mathrm{B}} = 1/3$; $a_{b,\mathrm{B}} = a_{x,\mathrm{B}}/0.018015 = 18.5x_{\mathrm{B}}$, while $b_{\mathrm{B}} \to \infty$, so $\gamma_{b,\mathrm{B}} \to 0$ (consistent with $\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}} \to 0$ in Eq. (6.2)). The molality scale is suitable only for dilute solutions; in concentrated solutions the activity coefficient loses its intuitive meaning as a measure of the deviation.

### 6.2.4. The General Expression for the Chemical Potential

Expressing the chemical potential of the reference state through the standard state, $\mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$, we obtain the general expression for the chemical potential of any substance:

$$
\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}} + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p. \tag{6.3}
$$

| Substance | Standard state | $a_{\mathrm{B}}$ | Pressure term |
|---|---|---|---|
| Gas | pure ideal gas at $p^\circ$ | $f_{\mathrm{B}}/p^\circ = \varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ$ | none (already contained in the fugacity) |
| Pure liquid, pure solid | pure substance at $p^\circ$ | 1 | $\int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p$ |
| Component of a liquid mixture, solvent | pure liquid at $p^\circ$ | $\gamma_{\mathrm{B}}x_{\mathrm{B}}$ | $\int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p$ |
| Solute | hypothetical state ($x$, $b$, or $c$) | $\gamma_{x,\mathrm{B}}x_{\mathrm{B}}$, etc. | $\int_{p^\circ}^{p}V^{\infty}_{\mathrm{B}}\,\mathrm{d}p$ |

For condensed phases the pressure term can usually be neglected unless the pressure is large, so that $\mu_{\mathrm{B}} \approx \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}}$; this is the form used in [6.3.7](/6.3.7) to derive the equilibrium constant.

Another common convention (the relative activity of IUPAC) absorbs the pressure term into the activity: $a_{\mathrm{B}} = \exp[(\mu_{\mathrm{B}} - \mu^\circ_{\mathrm{B}})/RT]$, in which case a pure liquid at $p \ne p^\circ$ has $a \ne 1$. The two conventions differ by the factor $\exp(\int V\,\mathrm{d}p/RT)$, which for water at $1\,\mathrm{MPa}$ is only $1.007$. Here we follow the convention of placing the reference state at the actual pressure, so that the activity of a pure condensed phase is always 1.

## 6.3. Measurement of Activities

### 6.3.1. The Vapor Pressure Method

If the equilibrium partial pressures above the solution are measured, then by Eq. (6.1)

$$
a_{\mathrm{A}} = \frac{p_{\mathrm{A}}}{p^*_{\mathrm{A}}}, \qquad a_{x,\mathrm{B}} = \frac{p_{\mathrm{B}}}{k_{x,\mathrm{B}}},
$$
where $k_{x,\mathrm{B}}$ is obtained by extrapolating $p_{\mathrm{B}}/x_{\mathrm{B}}$ to $x_{\mathrm{B}} \to 0$. If the vapor is not ideal, the partial pressures are replaced by fugacities. This method applies only to the solvent and to volatile solutes.

**Example 6.3.1** At $30\,^\circ\mathrm{C}$, $p^*_{\mathrm{A}} = 40\,\mathrm{kPa}$ and $p^*_{\mathrm{B}} = 120\,\mathrm{kPa}$. A real liquid mixture with $x_{\mathrm{A}} = 0.5$ is in equilibrium with its vapor at a total pressure of $100\,\mathrm{kPa}$, and $\gamma_{\mathrm{A}} = 1.1$. Find $\gamma_{\mathrm{B}}$ and the vapor composition $y_{\mathrm{A}}$.

**Solution** $p_{\mathrm{A}} = \gamma_{\mathrm{A}}p^*_{\mathrm{A}}x_{\mathrm{A}} = 1.1 \times 40 \times 0.5 = 22\,\mathrm{kPa}$, $p_{\mathrm{B}} = 100 - 22 = 78\,\mathrm{kPa}$, $\gamma_{\mathrm{B}} = 78/(120 \times 0.5) = 1.3$; $y_{\mathrm{A}} = 22/100 = 0.22$. Both activity coefficients exceed 1, so the system shows positive deviations.

### 6.3.2. The Colligative Property Method

The formulas for freezing-point depression and osmotic pressure in [6.3.5](/6.3.5) use only the chemical potential of the solvent; for a real solution, replacing $x_{\mathrm{A}}$ by $a_{\mathrm{A}}$ leaves the derivation unchanged:

$$
\ln a_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}}\right), \qquad \ln a_{\mathrm{A}} = -\frac{\varPi V^*_{\mathrm{m,A}}}{RT}. \tag{6.4}
$$
Measuring the freezing point or the osmotic pressure thus gives the activity of the solvent. The former gives the activity at the freezing point; converting it to other temperatures requires $H^{\mathrm{E}}$ (6.4). This method yields directly only the activity of the solvent; the activity of the solute (especially a nonvolatile one) is obtained from the Gibbs–Duhem equation below.

### 6.3.3. The Gibbs–Duhem Equation Method

At constant temperature and pressure, substitute $\mathrm{d}\mu_{\mathrm{B}} = RT\,\mathrm{d}\ln a_{\mathrm{B}}$ into the **Gibbs–Duhem equation** of a binary solution, $x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0$ (the chemical potential of the reference state is constant at constant temperature and pressure, whatever the choice of standard state):

$$
x_{\mathrm{A}}\,\mathrm{d}\ln a_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln a_{\mathrm{B}} = 0.
$$
Substituting further $a = \gamma x$ and using $x_{\mathrm{A}}\,\mathrm{d}\ln x_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln x_{\mathrm{B}} = \mathrm{d}x_{\mathrm{A}} + \mathrm{d}x_{\mathrm{B}} = 0$, we obtain

$$
x_{\mathrm{A}}\,\mathrm{d}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln\gamma_{\mathrm{B}} = 0. \tag{6.5}
$$
It holds whether B is treated by Raoult's law or by Henry's law (the two $\ln\gamma$ differ only by a constant, Eq. (6.2)). Hence, if the variation of the activity coefficient of one component with composition is known, that of the other can be found by integration:

$$
\ln\gamma_{\mathrm{B}}(x_{\mathrm{B}}) = -\int_{1}^{x_{\mathrm{B}}}\frac{x_{\mathrm{A}}}{x_{\mathrm{B}}}\frac{\mathrm{d}\ln\gamma_{\mathrm{A}}}{\mathrm{d}x_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} \quad (\text{Raoult's law}), \qquad \ln\gamma_{x,\mathrm{B}}(x_{\mathrm{B}}) = -\int_{0}^{x_{\mathrm{B}}}\frac{x_{\mathrm{A}}}{x_{\mathrm{B}}}\frac{\mathrm{d}\ln\gamma_{\mathrm{A}}}{\mathrm{d}x_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} \quad (\text{Henry's law}).
$$
The latter integral converges at $x_{\mathrm{B}} \to 0$ because $\ln\gamma_{\mathrm{A}}$ tends to zero there like $x_{\mathrm{B}}^2$ (the solvent obeys Raoult's law to one order higher than the solute obeys Henry's law). Graphical integration was used in the past; today we integrate numerically: the measured $\ln\gamma_{\mathrm{A}}$ is first smoothed by a polynomial fit, then differentiated and integrated (`numpy.polyfit` or `scipy.integrate.cumulative_trapezoid`, [4.4.4](/4.4.4#sec-4.3.1)).

![ln γ_B obtained by numerical Gibbs–Duhem integration of smoothed "measured" values of γ_A (a two-parameter Margules model plus 1% noise); it nearly coincides with the true value of the model](./plots/gibbs-duhem-integration.py)

If the activity coefficients of both components have been measured, they must satisfy Eq. (6.5), which is called thermodynamic consistency. Eq. (6.5) also shows that, at constant temperature and pressure, if $\mu_{\mathrm{A}}$ (or $a_{\mathrm{A}}$) increases as the composition changes, then $\mu_{\mathrm{B}}$ (or $a_{\mathrm{B}}$) must decrease. A global test is given in 6.4.1.

In electrolyte solutions, positive and negative ions cannot exist independently, so the activity is expressed as a mean activity, determined mainly by the cell potential method ([6.3.13](/6.3.13)).

## 6.4. Excess Functions

### 6.4.1. Definition and Properties

The activity coefficient describes the nonideality of an individual component; the nonideality of the solution as a whole is described by excess functions.

**Definition 6.4.1 (Excess Function)** At given temperature, pressure, and composition, the mixing function of the real solution minus the mixing function of an ideal liquid mixture of the same composition is called the excess function:

$$
V^{\mathrm{E}} = \Delta_{\mathrm{mix}}V - \Delta_{\mathrm{mix}}V^{\mathrm{id}}, \quad H^{\mathrm{E}} = \Delta_{\mathrm{mix}}H - \Delta_{\mathrm{mix}}H^{\mathrm{id}}, \quad S^{\mathrm{E}} = \Delta_{\mathrm{mix}}S - \Delta_{\mathrm{mix}}S^{\mathrm{id}}, \quad G^{\mathrm{E}} = \Delta_{\mathrm{mix}}G - \Delta_{\mathrm{mix}}G^{\mathrm{id}}.
$$
Here $G^{\mathrm{E}}$ is called the **excess Gibbs energy**.

Since $\Delta_{\mathrm{mix}}V^{\mathrm{id}} = \Delta_{\mathrm{mix}}H^{\mathrm{id}} = 0$ (Theorem 5.1.1), $V^{\mathrm{E}}$ and $H^{\mathrm{E}}$ are just the actual volume and enthalpy of mixing and can be measured directly with a dilatometer and a calorimeter. The excess functions satisfy the same relations as ordinary thermodynamic functions ($G^{\mathrm{E}} = H^{\mathrm{E}} - TS^{\mathrm{E}}$, etc.), because the ideal parts already satisfy them separately.

**Theorem 6.4.1** When the reference states of all components are chosen according to Raoult's law,

$$
G^{\mathrm{E}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}, \qquad RT\ln\gamma_{\mathrm{B}} = \left(\frac{\partial G^{\mathrm{E}}}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}, \tag{6.6}
$$
and

$$
V^{\mathrm{E}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial p}\right)_{T,x}, \qquad H^{\mathrm{E}} = -RT^2\sum_{\mathrm{B}}n_{\mathrm{B}}\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial T}\right)_{p,x}, \qquad S^{\mathrm{E}} = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\left[\ln\gamma_{\mathrm{B}} + T\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial T}\right)_{p,x}\right].
$$

**Proof** $\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}(\mu_{\mathrm{B}} - \mu^*_{\mathrm{B}}) = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln a_{\mathrm{B}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}} + RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$, and the first term is $\Delta_{\mathrm{mix}}G^{\mathrm{id}}$, which gives the first equation. $G^{\mathrm{E}}$ is the sum of the partial molar quantities $RT\ln\gamma_{\mathrm{B}} = \mu_{\mathrm{B}} - \mu^{\mathrm{id}}_{\mathrm{B}}$, so the second equation follows from the definition of partial molar quantities. The remaining three follow from $V^{\mathrm{E}} = (\partial G^{\mathrm{E}}/\partial p)_{T,n}$, $H^{\mathrm{E}} = -T^2[\partial(G^{\mathrm{E}}/T)/\partial T]_{p,n}$ (the Gibbs–Helmholtz equation), and $S^{\mathrm{E}} = -(\partial G^{\mathrm{E}}/\partial T)_{p,n}$, respectively. $\square$

Equation (6.6) shows that $G^{\mathrm{E}}(T, p, n_{\mathrm{A}}, n_{\mathrm{B}}, \dots)$ is a "generating function" of all the activity coefficients: given a model for $G^{\mathrm{E}}$, taking partial derivatives yields the activity coefficient of each component, and these automatically satisfy the Gibbs–Duhem equation. This is the standard way of constructing solution models. Equation (6.6) also yields a global consistency test: in a binary system $G^{\mathrm{E}}_{\mathrm{m}}/RT = x_{\mathrm{A}}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$ vanishes at both $x_{\mathrm{B}} = 0$ and $1$, and by Eq. (6.5) its derivative with respect to $x_{\mathrm{B}}$ is $\ln(\gamma_{\mathrm{B}}/\gamma_{\mathrm{A}})$, so isothermal data must satisfy

$$
\int_0^1\ln\frac{\gamma_{\mathrm{A}}}{\gamma_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} = 0
$$
(the area test). The areas enclosed above and below the axis by the curve of $\ln(\gamma_{\mathrm{A}}/\gamma_{\mathrm{B}})$ against $x_{\mathrm{B}}$ must be equal.

Excess functions are often used to extract information on intermolecular interactions. In the chloroform–acetone system $H^{\mathrm{E}} < 0$ (hydrogen-bond formation is exothermic) and $S^{\mathrm{E}}$ is also negative (hydrogen bonding makes the molecular arrangement more ordered); $\lvert H^{\mathrm{E}}\rvert$ exceeds $\lvert G^{\mathrm{E}}\rvert$, so the enthalpy and entropy effects partly cancel. The same idea applied to spectroscopy gives the "excess spectrum": the spectrum of the real mixture minus the composition-weighted spectra of the pure components, which reveals interactions that appear or disappear on mixing.

### 6.4.2. Regular Solutions and Athermal Solutions

Since $G^{\mathrm{E}} = H^{\mathrm{E}} - TS^{\mathrm{E}}$, the nonideality may arise from the enthalpy or from the entropy. There are two extreme cases:

**Definition 6.4.2** A solution with $S^{\mathrm{E}} = 0$ (the entropy of mixing is the same as for an ideal solution) but $H^{\mathrm{E}} \ne 0$ is called a **regular solution**; then $G^{\mathrm{E}} = H^{\mathrm{E}}$ and the nonideality comes entirely from the thermal effect of mixing. A solution with $H^{\mathrm{E}} = 0$ but $S^{\mathrm{E}} \ne 0$ is called an **athermal solution**; then $G^{\mathrm{E}} = -TS^{\mathrm{E}}$ and the nonideality comes entirely from entropy.

By Theorem 6.4.1, $S^{\mathrm{E}} = 0$ in a regular solution means that $RT\ln\gamma_{\mathrm{B}}$ does not vary with temperature (at fixed composition), so $\ln\gamma_{\mathrm{B}} \propto 1/T$; $H^{\mathrm{E}} = 0$ in an athermal solution means that $\ln\gamma_{\mathrm{B}}$ is independent of temperature. Mixtures of nonpolar liquids whose molecules are of similar size and interact only through dispersion forces are close to regular solutions (Hildebrand's regular solution theory); systems whose molecules differ greatly in size but have similar interactions (such as solutions of polymers in their monomer or in similar small molecules) are close to athermal solutions, their nonideality arising from the difference in the number of ways in which large and small molecules can be arranged (Flory–Huggins theory, [6.3.21](/6.3.21)).

### 6.4.3. The One-Parameter Margules Model

The simplest regular-solution model takes

$$
G^{\mathrm{E}} = W\frac{n_{\mathrm{A}}n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}}, \qquad G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}},
$$
where $W$ is a parameter independent of composition.

**Theorem 6.4.2 (Margules Equations)** In this model

$$
\ln\gamma_{\mathrm{A}} = \frac{W}{RT}x_{\mathrm{B}}^2, \qquad \ln\gamma_{\mathrm{B}} = \frac{W}{RT}x_{\mathrm{A}}^2. \tag{6.7}
$$
Equations (6.7) are the one-parameter Margules equations.

**Proof** By Eq. (6.6), $RT\ln\gamma_{\mathrm{A}} = \frac{\partial}{\partial n_{\mathrm{A}}}\frac{Wn_{\mathrm{A}}n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}} = \frac{Wn_{\mathrm{B}}(n_{\mathrm{A}} + n_{\mathrm{B}}) - Wn_{\mathrm{A}}n_{\mathrm{B}}}{(n_{\mathrm{A}} + n_{\mathrm{B}})^2} = Wx_{\mathrm{B}}^2$, and $\ln\gamma_{\mathrm{B}}$ follows in the same way. $\square$

One verifies directly that Eqs. (6.7) satisfy the Gibbs–Duhem equation: $x_{\mathrm{A}}\,\mathrm{d}(x_{\mathrm{B}}^2) + x_{\mathrm{B}}\,\mathrm{d}(x_{\mathrm{A}}^2) = 2x_{\mathrm{A}}x_{\mathrm{B}}(\mathrm{d}x_{\mathrm{B}} + \mathrm{d}x_{\mathrm{A}}) = 0$. Properties of the model:

- $W > 0$ gives a positive deviation and $W < 0$ a negative deviation; the $\ln\gamma$ curves of the two components are mirror images of each other, the infinite-dilution value is $\gamma^{\infty} = \mathrm{e}^{W/RT}$, and the Henry constant is $k_{x,\mathrm{B}} = p^*_{\mathrm{B}}\mathrm{e}^{W/RT}$ (Eq. (6.2)).
- If $W$ is independent of temperature, $H^{\mathrm{E}} = G^{\mathrm{E}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$ and $S^{\mathrm{E}} = 0$, so the solution is regular.
- A lattice model gives $W$ a molecular meaning: each molecule has $z$ nearest neighbors, the interaction energies of A–A, B–B, and A–B pairs are $\varepsilon_{\mathrm{AA}}$, $\varepsilon_{\mathrm{BB}}$, and $\varepsilon_{\mathrm{AB}}$ (negative for attraction), and for random mixing $W = zN_{\mathrm{A}}\left[\varepsilon_{\mathrm{AB}} - \frac{1}{2}(\varepsilon_{\mathrm{AA}} + \varepsilon_{\mathrm{BB}})\right]$. When the attraction between unlike molecules is weaker than the average attraction between like molecules, $W > 0$.
- For $W > 2RT$, $\Delta_{\mathrm{mix}}G_{\mathrm{m}} = RT(x_{\mathrm{A}}\ln x_{\mathrm{A}} + x_{\mathrm{B}}\ln x_{\mathrm{B}}) + Wx_{\mathrm{A}}x_{\mathrm{B}}$ is convex upward near $x = 1/2$ and the solution separates into two liquid phases; the critical temperature $T_{\mathrm{c}} = W/(2R)$ is the **critical solution temperature** ([6.3.9](/6.3.9)).

![Activity coefficients (Raoult's-law convention) in the one-parameter Margules model: ln γ > 0 for a positive deviation and ln γ < 0 for a negative deviation; the curves of the two components are mirror images](./plots/margules-activity-coefficients.py)

Real systems often need two parameters: $\ln\gamma_{\mathrm{A}} = x_{\mathrm{B}}^2[A_{\mathrm{AB}} + 2(A_{\mathrm{BA}} - A_{\mathrm{AB}})x_{\mathrm{A}}]$ and $\ln\gamma_{\mathrm{B}} = x_{\mathrm{A}}^2[A_{\mathrm{BA}} + 2(A_{\mathrm{AB}} - A_{\mathrm{BA}})x_{\mathrm{B}}]$ (the two-parameter Margules equations, with $A_{\mathrm{AB}} = \ln\gamma^{\infty}_{\mathrm{A}}$ and $A_{\mathrm{BA}} = \ln\gamma^{\infty}_{\mathrm{B}}$); in engineering practice local-composition models such as Wilson, NRTL, and UNIQUAC are more common, all of which start from an expression for $G^{\mathrm{E}}$ and obtain the activity coefficients from Eq. (6.6).

## 6.5. The Distribution Law and Extraction

### 6.5.1. Nernst's Distribution Law

Experiment shows that when a substance dissolves in two immiscible liquids that are in contact at a given temperature and pressure, the ratio of its concentrations in the two phases at equilibrium is constant over a range of low concentrations. Thermodynamics provides a proof of this rule and the conditions for its validity.

**Theorem 6.5.1 (Nernst Distribution Law)** At given temperature and pressure, when a solute B is in equilibrium between two immiscible liquid phases $\alpha$ and $\beta$,

$$
\frac{a_{\mathrm{B}}(\alpha)}{a_{\mathrm{B}}(\beta)} = \exp\frac{\mu^{\mathrm{ref}}_{\mathrm{B}}(\beta) - \mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha)}{RT} = K(T, p);
$$
when both phases are ideal dilute solutions,

$$
\frac{c_{\mathrm{B}}(\alpha)}{c_{\mathrm{B}}(\beta)} = K \quad\text{or}\quad \frac{b_{\mathrm{B}}(\alpha)}{b_{\mathrm{B}}(\beta)} = K'. \tag{6.8}
$$

**Proof** At equilibrium the chemical potentials of B in the two phases are equal: $\mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha) + RT\ln a_{\mathrm{B}}(\alpha) = \mu^{\mathrm{ref}}_{\mathrm{B}}(\beta) + RT\ln a_{\mathrm{B}}(\beta)$. In both phases the reference state of B is chosen according to Henry's law; the chemical potential of the reference state depends only on $T$, $p$, and the solvent, so the ratio of the activities is a constant. In an ideal dilute solution the activity equals the relative concentration. $\square$

The ratio $K$ is called the *partition coefficient*. Several remarks follow:

1. The reference states of B in the two phases differ (the solvents differ, and so do the hypothetical states), $\mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha) \ne \mu^{\mathrm{ref}}_{\mathrm{B}}(\beta)$. Hence at equilibrium the chemical potentials of B in the two phases are equal, but the concentrations (and even the activities) are not. If the two phases share one vapor phase, then $p_{\mathrm{B}} = k_{\mathrm{B},\alpha}a_{\mathrm{B}}(\alpha) = k_{\mathrm{B},\beta}a_{\mathrm{B}}(\beta)$ gives $K = k_{\mathrm{B},\beta}/k_{\mathrm{B},\alpha}$: B is more concentrated in the phase with the smaller Henry constant (the solvent that attracts it more strongly).
2. The distribution law holds only for the part of the solute that has the same molecular form in both phases. Benzoic acid exists mainly as the monomer in water but is largely associated into dimers in benzene: for the monomer $c_{\mathrm{B}}(\text{water})/c_{\mathrm{B}}(\text{benzene, monomer}) = K$, and the dimerization equilibrium gives $c_{\ce{B2}}/c_{\mathrm{B}}^2 = K_{\mathrm{d}}$; if nearly all of the solute in benzene is dimer, the total concentration is $c(\text{benzene}) \approx c_{\ce{B2}}$, so $c(\text{water})/\sqrt{c(\text{benzene})}$ is constant. Dissociation is treated similarly.
3. The partition coefficient is of great importance in medicinal chemistry: the logarithm $\lg P$ of the partition coefficient $P$ of a drug between $n$-octanol and water is the standard measure of its lipophilicity and determines whether it can cross the lipid bilayer of a cell membrane; an orally administered drug should generally have $\lg P$ no greater than about 5 (one of Lipinski's rules). The retention in reversed-phase chromatography and the accumulation of pollutants in organisms are also governed by partition coefficients.

### 6.5.2. Extraction

Removing a solute from a solution by means of another solvent that is immiscible with the original one is called *extraction*. The distribution law gives the efficiency of extraction.

Let a volume $V$ of aqueous solution contain solute in amount $m_0$, and extract it each time with a volume $V_{\mathrm{e}}$ of organic solvent, the partition coefficient being $K = c(\text{organic phase})/c(\text{aqueous phase})$. After the first extraction the amount remaining in the aqueous phase is $m_1$:

$$
\frac{(m_0 - m_1)/V_{\mathrm{e}}}{m_1/V} = K \quad\Longrightarrow\quad m_1 = m_0\frac{V}{V + KV_{\mathrm{e}}}.
$$
After $n$ repetitions, $m_n = m_0\left(\frac{V}{V + KV_{\mathrm{e}}}\right)^n$.

**Proposition 6.5.1** For a fixed total volume $V_{\mathrm{e}}$ of extractant, the amount remaining after $n$ extractions (each with $V_{\mathrm{e}}/n$)

$$
m_n = m_0\left(1 + \frac{KV_{\mathrm{e}}}{nV}\right)^{-n}
$$
decreases monotonically with $n$ and tends to $m_0\exp(-KV_{\mathrm{e}}/V)$ as $n \to \infty$.

**Proof** Let $u = KV_{\mathrm{e}}/V > 0$. Then $(1 + u/n)^n$ increases monotonically with $n$ and tends to $\mathrm{e}^u$ (differentiate $f(t) = t\ln(1 + u/t)$: $f'(t) = \ln(1 + s) - \frac{s}{1 + s} > 0$, where $s = u/t$), so $m_n$ decreases monotonically and tends to $m_0\mathrm{e}^{-u}$. $\square$

For example, with $K = 4$, $V = 100\,\mathrm{mL}$, and $V_{\mathrm{e}} = 30\,\mathrm{mL}$: one extraction leaves $1/(1 + 1.2) = 45.5\%$; three extractions of $10\,\mathrm{mL}$ each leave $(1/1.4)^3 = 36.4\%$; the limit for infinitely many extractions is $\mathrm{e}^{-1.2} = 30.1\%$. Extracting "several times with small portions" is better than "once with the whole amount", but the gain diminishes as the number of extractions increases.

![Solute remaining in the aqueous phase as a function of the number of extractions for a fixed total amount of extractant (K = 4, V = 100 mL, V_e = 30 mL); the dashed line is the limit e^{−KV_e/V} as n → ∞](./plots/extraction.py)

## 6.6. Comprehensive Examples

**Example 6.6.1** At $298\,\mathrm{K}$ the osmotic pressure of an aqueous NaCl solution is $2p^\circ$. Find $\Delta G$ for the process

$$
1\,\mathrm{mol}\ \ce{H2O}(\text{solution}, 298\,\mathrm{K}, p^\circ) \longrightarrow 1\,\mathrm{mol}\ \ce{H2O}(\mathrm{l}, 298\,\mathrm{K}, p^\circ).
$$
The amount of solution is so large that removing $1\,\mathrm{mol}$ of water does not change its composition.

**Solution** Method 1: take pure water at $298\,\mathrm{K}$ and $p^\circ$ as the reference state; then $\Delta G = \mu^*_{\mathrm{A}} - \mu_{\mathrm{A}} = -RT\ln a_{\mathrm{A}}$. By Eq. (6.4), $-RT\ln a_{\mathrm{A}} = \varPi V^*_{\mathrm{m,A}} = 2 \times 10^5\,\mathrm{Pa} \times 18.07 \times 10^{-6}\,\mathrm{m^3\,mol^{-1}} = 3.6\,\mathrm{J\,mol^{-1}}$.

Method 2: design a path. First compress the solution from $p^\circ$ to $3p^\circ$: $\Delta\mu_{\mathrm{I}} = \int_{p^\circ}^{3p^\circ}V_{\mathrm{A}}\,\mathrm{d}p \approx V^*_{\mathrm{m,A}} \cdot 2p^\circ = 3.6\,\mathrm{J\,mol^{-1}}$ (in a dilute solution $V_{\mathrm{A}} \approx V^*_{\mathrm{m,A}}$); the solution is then exactly in osmotic equilibrium with pure water at $p^\circ$, and water passes through the semipermeable membrane to the pure-water side with $\Delta\mu_{\mathrm{II}} = 0$. Adding the two steps gives $\Delta G = 3.6\,\mathrm{J}$.

Since $\Delta G > 0$, the removal of pure water from the solution cannot occur spontaneously. At constant temperature and pressure it requires at least $3.6\,\mathrm{J}$ of non-expansion work, which is the minimum work of reverse osmosis ([6.3.5](/6.3.5)).

**Example 6.6.2** A substance is in distribution equilibrium between immiscible liquids $\alpha$ and $\beta$; in phase $\alpha$ it exists as B and in phase $\beta$ as $\ce{B2}$. Which of the following relations hold: (a) $\mu_\alpha(\mathrm{B}) = \mu_\beta(\ce{B2})$; (b) $2\mu_\alpha(\mathrm{B}) = \mu_\beta(\ce{B2})$; (c) $a_\alpha^2(\mathrm{B})/a_\beta(\ce{B2}) = K$; (d) $\mathrm{d}\ln a_\alpha^2(\mathrm{B}) = \mathrm{d}\ln a_\beta(\ce{B2})$ at constant temperature and pressure?

**Solution** This is in fact a chemical equilibrium across phases, $2\mathrm{B}(\alpha) \ce{<=>} \ce{B2}(\beta)$, whose equilibrium condition is $\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$ ([6.3.7](/6.3.7)), that is, (b); substituting the expressions for the chemical potentials gives (c); differentiating (b) gives (d). (a) does not hold. The distribution law, Eq. (6.8), is just the special case of this equilibrium in which the molecular form is the same in both phases.

## Summary

| Topic | Key points |
|---|---|
| Deviations | Positive deviation: weaker A–B attraction or broken association, $\gamma > 1$, $k_{x} > p^*$; negative deviation is the opposite |
| Activity | $\mu_{\mathrm{B}} = \mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) + RT\ln a_{\mathrm{B}}$; Raoult reference state (pure liquid) and Henry reference states (three hypothetical states for $x$, $b$, $c$); the activity depends on the reference state, the chemical potential does not |
| Conversion | $\gamma_{\mathrm{B}}/\gamma_{x,\mathrm{B}} = k_{x,\mathrm{B}}/p^*_{\mathrm{B}} = \gamma^{\infty}_{\mathrm{B}}$; $\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}}$ |
| General expression | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}} + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$; pure condensed phase $a = 1$, gas $a = f/p^\circ$ |
| Measurement | Vapor pressure method; colligative property method (solvent); Gibbs–Duhem integration $x_{\mathrm{A}}\,\mathrm{d}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln\gamma_{\mathrm{B}} = 0$ (solute, thermodynamic consistency); cell potential method (electrolytes) |
| Excess functions | $G^{\mathrm{E}} = RT\sum n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$, $RT\ln\gamma_{\mathrm{B}} = \partial G^{\mathrm{E}}/\partial n_{\mathrm{B}}$; $V^{\mathrm{E}} = \Delta_{\mathrm{mix}}V$, $H^{\mathrm{E}} = \Delta_{\mathrm{mix}}H$ |
| Models | Regular solution $S^{\mathrm{E}} = 0$, athermal solution $H^{\mathrm{E}} = 0$; Margules: $G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$, $\ln\gamma_{\mathrm{A}} = Wx_{\mathrm{B}}^2/RT$; phase separation for $W > 2RT$ |
| Distribution and extraction | $a(\alpha)/a(\beta) = K$; in dilute solutions the concentration ratio is constant, valid only for the same molecular form; several small extractions are more effective than one large one, with the remaining amount $\to m_0\mathrm{e}^{-KV_{\mathrm{e}}/V}$ |
