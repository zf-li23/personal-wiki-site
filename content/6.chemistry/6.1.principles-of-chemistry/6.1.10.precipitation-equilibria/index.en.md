---
title: Precipitation–Dissolution Equilibria
source_hash: 71464b7fdd57
---

Many important chemical processes involve the formation and dissolution of sparingly soluble substances: gravimetric analysis and the separation and identification of ions in analytical chemistry, impurity removal and hydrometallurgy in industry, the formation and removal of boiler scale, the formation of minerals, bone, and teeth in nature, and even the colloidal synthesis of size-uniform semiconductor nanocrystals such as CdS and PbS (whose nucleation and growth are likewise governed by precipitation–dissolution equilibrium and supersaturation). This chapter applies the equilibrium principles of [6.1.8](/6.1.8) to the heterogeneous ionic equilibrium between a solid and its saturated solution. We first define the solubility product and discuss its relation to solubility (10.1), then derive from the comparison of the reaction quotient with the solubility product the criteria for precipitation and dissolution (10.2). Next we discuss the effects of the common ion, of added salt, of acid, and of oxidation–reduction and complexation on the equilibrium (10.3), which draw on the acid–base and complexation equilibria of [6.1.9](/6.1.9), and finally treat fractional precipitation, the conversion of precipitates, and the separation of metal ions (10.4). The quantitative treatment of the effective concentration of ions (activity) and of ionic strength is found in [Physical Chemistry](/6.3); gravimetric analysis, precipitation titration, and systematic qualitative analysis are found in [Analytical Chemistry](/6.4).

As in [6.1.9](/6.1.9), $[\mathrm{B}]$ in an equilibrium-constant expression denotes the relative concentration $[\mathrm{B}]/c^\circ$, and all equilibrium constants are dimensionless standard equilibrium constants. The data are for $25\,^\circ\mathrm{C}$, and the solubility products are taken from the CRC Handbook of Chemistry and Physics.

## 10.1. The Solubility Product

### 10.1.1. Precipitation–Dissolution Equilibrium and the Solubility Product

**Definition 10.1.1** The maximum amount of a solute that can dissolve in a given amount of solvent at a given temperature (that is, the composition of the saturated solution) is called the **solubility** of the solute. In this chapter it is denoted $S$ and expressed in $\mathrm{mol\,L^{-1}}$; handbooks also often give it as grams dissolved per $100\,\mathrm{g}$ of water.

By convention, electrolytes are divided into three classes according to their solubility in water at $25\,^\circ\mathrm{C}$: those above $1\,\mathrm{g}/100\,\mathrm{g}$ water are called soluble, those below $0.01\,\mathrm{g}/100\,\mathrm{g}$ water are called insoluble, and those in between are called slightly soluble.

**Definition 10.1.2** An electrolyte that has very low solubility in water but whose dissolved portion is completely dissociated into ions is called a **sparingly soluble electrolyte** (sparingly soluble strong electrolyte), such as $\ce{AgCl}$, $\ce{BaSO4}$, $\ce{CaCO3}$, and $\ce{Fe(OH)3}$.

When $\ce{BaSO4}$ crystals (solubility $0.000223\,\mathrm{g}/100\,\mathrm{g}$ water) are placed in water, the $\ce{Ba^2+}$ and $\ce{SO4^2-}$ ions at the crystal surface continually enter the solution under the action of water molecules (dissolution), while ions in the solution continually collide with the crystal surface and are deposited again (precipitation). When the dissolution rate exceeds the precipitation rate the solution is unsaturated; when it is smaller the solution is supersaturated; when the two are equal the solution is saturated and a dynamic equilibrium is established (dissolution in the forward direction, precipitation in the reverse):

$$
\ce{BaSO4(s) <=> Ba^2+(aq) + SO4^2-(aq)}.
$$

**Definition 10.1.3** The heterogeneous dynamic equilibrium between the solid of a sparingly soluble electrolyte and the ions produced by its dissociation in the saturated solution is called the **precipitation–dissolution equilibrium**.

**Definition 10.1.4 (Solubility Product)** The standard equilibrium constant of the precipitation–dissolution equilibrium $\ce{A_nB_m(s) <=> n A^{m+}(aq) + m B^{n-}(aq)}$ of a sparingly soluble electrolyte $\ce{A_nB_m}$,

$$
K_{\mathrm{sp}}(\ce{A_nB_m}) = [\ce{A^{m+}}]^n[\ce{B^{n-}}]^m \tag{10.1}
$$
is called the **solubility product** (solubility-product constant) of that electrolyte.

For example, $K_{\mathrm{sp}}(\ce{BaSO4}) = [\ce{Ba^2+}][\ce{SO4^2-}]$, $K_{\mathrm{sp}}(\ce{Mg(OH)2}) = [\ce{Mg^2+}][\ce{OH-}]^2$, and $K_{\mathrm{sp}}(\ce{Fe(OH)3}) = [\ce{Fe^3+}][\ce{OH-}]^3$. Solid $\ce{BaSO4}$ does not appear in the expression because the **activity** of a pure solid is 1 ([6.1.8](/6.1.8)), not because "the concentration of the solid is constant and is absorbed into the constant": writing $K^\circ = [\ce{Ba^2+}][\ce{SO4^2-}]/[\ce{BaSO4}]$ and then absorbing the denominator treats the pure solid as a species in solution. The solubility product says that, at a given temperature, the product of the relative concentrations of the ions in a saturated solution of a sparingly soluble electrolyte, each raised to the power of its stoichiometric number, is a constant. It depends only on the nature of the electrolyte and the temperature.

Like other standard equilibrium constants, the solubility product can be calculated from thermodynamic data. For AgCl, $\Delta_{\mathrm{f}}G^\circ$ ($\mathrm{kJ\,mol^{-1}}$) is $-109.8$ for $\ce{AgCl(s)}$, $77.1$ for $\ce{Ag+(aq)}$, and $-131.2$ for $\ce{Cl-(aq)}$, so $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 77.1 - 131.2 + 109.8 = 55.7\,\mathrm{kJ\,mol^{-1}}$, and by Eq. (8.3)

$$
K_{\mathrm{sp}}(\ce{AgCl}) = \exp\left(-\frac{55.7 \times 10^3}{8.314 \times 298.15}\right) = 1.7 \times 10^{-10},
$$
in agreement with the experimental value $1.8 \times 10^{-10}$.

Solubility products of common sparingly soluble electrolytes ($25\,^\circ\mathrm{C}$):

| Substance | $K_{\mathrm{sp}}$ | Substance | $K_{\mathrm{sp}}$ | Substance | $K_{\mathrm{sp}}$ |
|---|---|---|---|---|---|
| AgCl | $1.8 \times 10^{-10}$ | $\ce{BaSO4}$ | $1.08 \times 10^{-10}$ | $\ce{Mg(OH)2}$ | $5.61 \times 10^{-12}$ |
| AgBr | $5.4 \times 10^{-13}$ | $\ce{BaCO3}$ | $2.58 \times 10^{-9}$ | $\ce{Mn(OH)2}$ | $2.06 \times 10^{-13}$ |
| AgI | $8.5 \times 10^{-17}$ | $\ce{CaSO4}$ | $4.93 \times 10^{-5}$ | $\ce{Fe(OH)2}$ | $4.87 \times 10^{-17}$ |
| $\ce{Ag2CrO4}$ | $1.12 \times 10^{-12}$ | $\ce{CaCO3}$ (calcite) | $3.36 \times 10^{-9}$ | $\ce{Cu(OH)2}$ | $2.2 \times 10^{-20}$ |
| $\ce{PbSO4}$ | $2.53 \times 10^{-8}$ | $\ce{CaF2}$ | $3.45 \times 10^{-11}$ | $\ce{Fe(OH)3}$ | $2.79 \times 10^{-39}$ |

($\ce{Al(OH)3}$ is not listed in the CRC table; this chapter uses the commonly quoted value $1.3 \times 10^{-33}$. The solubility products of hydroxides depend on the crystal form of the precipitate and on how long it has aged, so the data carry considerable uncertainty.)

### 10.1.2. Conversion between Solubility Product and Solubility

Both the solubility and the solubility product express the extent to which a sparingly soluble electrolyte dissolves. Solubility is intuitive and widely applicable, but it is affected by many factors such as temperature, solution composition, pH, and complexation; the solubility product is an equilibrium constant that depends only on temperature, applies to sparingly soluble electrolytes, and, more importantly, represents an equilibrium that can be combined with other equilibria in calculations.

**Example 10.1.1** The solubility of AgCl in pure water at $298\,\mathrm{K}$ is $1.92 \times 10^{-3}\,\mathrm{g\,L^{-1}}$. Find its solubility product.

**Solution** $M(\ce{AgCl}) = 143.32\,\mathrm{g\,mol^{-1}}$, so $S = 1.92 \times 10^{-3}/143.32 = 1.34 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$. All the dissolved AgCl is dissociated, so $[\ce{Ag+}] = [\ce{Cl-}] = S$ and

$$
K_{\mathrm{sp}} = S^2 = (1.34 \times 10^{-5})^2 = 1.8 \times 10^{-10}.
$$

**Example 10.1.2** At $298\,\mathrm{K}$, $K_{\mathrm{sp}}(\ce{Mg(OH)2}) = 5.61 \times 10^{-12}$. Find the solubility of $\ce{Mg(OH)2}$ in water, and the concentrations of $\ce{Mg^2+}$ and $\ce{OH-}$ and the pH of the saturated solution.

**Solution** Let the solubility be $S$; then $[\ce{Mg^2+}] = S$ and $[\ce{OH-}] = 2S$:

$$
K_{\mathrm{sp}} = S(2S)^2 = 4S^3, \qquad S = \sqrt[3]{\frac{5.61 \times 10^{-12}}{4}} = 1.12 \times 10^{-4}\,\mathrm{mol\,L^{-1}}.
$$
So $[\ce{Mg^2+}] = 1.12 \times 10^{-4}$, $[\ce{OH-}] = 2.24 \times 10^{-4}$, and $\mathrm{pH} = 10.35$.

In general, for $\ce{A_nB_m}$, $[\ce{A^{m+}}] = nS$, $[\ce{B^{n-}}] = mS$, and $K_{\mathrm{sp}} = (nS)^n(mS)^m$:

$$
S = \left(\frac{K_{\mathrm{sp}}}{n^nm^m}\right)^{1/(n+m)}. \tag{10.2}
$$

| Type | Examples | $K_{\mathrm{sp}}$ and $S$ |
|---|---|---|
| AB | AgCl, $\ce{BaSO4}$ | $K_{\mathrm{sp}} = S^2$ |
| $\ce{AB2}$, $\ce{A2B}$ | $\ce{Mg(OH)2}$, $\ce{Ag2CrO4}$ | $K_{\mathrm{sp}} = 4S^3$ |
| $\ce{AB3}$ | $\ce{Fe(OH)3}$ | $K_{\mathrm{sp}} = 27S^4$ |
| $\ce{A3B2}$ | $\ce{Ca3(PO4)2}$ | $K_{\mathrm{sp}} = 108S^5$ |

For sparingly soluble electrolytes of the same type, the smaller $K_{\mathrm{sp}}$ is, the smaller the solubility; the $K_{\mathrm{sp}}$ values of different types cannot be compared directly. For example, $K_{\mathrm{sp}}(\ce{Ag2CrO4}) = 1.12 \times 10^{-12}$ is smaller than $K_{\mathrm{sp}}(\ce{AgCl})$, but by Eq. (10.2) $S(\ce{Ag2CrO4}) = 6.5 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$, which is actually larger than $S(\ce{AgCl}) = 1.3 \times 10^{-5}$.

**Remark 10.1.1** Equation (10.2) holds when the dissolved portion is completely dissociated into simple ions and these ions undergo no further reactions. In the following cases it gives a wrong solubility:

- Hydrolysis of ions: the $\ce{CO3^2-}$ produced by the dissolution of $\ce{CaCO3}$ is a fairly strong base ($K_{\mathrm{b1}} = K_{\mathrm{w}}/K_{\mathrm{a2}} = 2.1 \times 10^{-4}$) and is mostly converted to $\ce{HCO3-}$, which shifts the dissolution equilibrium to the right. Taking this acid–base equilibrium into account, one finds in pure water without contact with air $S \approx 1.1 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$ (solution pH about 9.9), about twice $\sqrt{K_{\mathrm{sp}}} = 5.8 \times 10^{-5}$; in contact with atmospheric $\ce{CO2}$ the solubility is larger still. The situation is similar for sulfides, phosphates, and hydroxides, and is especially serious for sulfides (10.3.3).
- Ion association or complexation: a considerable fraction of dissolved $\ce{CaSO4}$ exists as the ion pair $\ce{CaSO4(aq)}$; $\ce{AgCl}$ forms $\ce{[AgCl2]-}$ in high concentrations of $\ce{Cl-}$.
- At higher concentrations the activity coefficients of ions are appreciably less than 1 (10.3.2).

Converting a solubility product to a solubility is therefore only an estimate, and is reliable mainly for sparingly soluble salts whose ions do not hydrolyze, such as AgCl and $\ce{BaSO4}$.

## 10.2. The Solubility Product Rule

The solubility product expresses both the tendency of a sparingly soluble electrolyte to dissolve and the ease with which the precipitate forms. In any state, the quantity obtained by substituting the relative concentrations of the ions into the solubility-product expression is the **reaction quotient** ([6.1.8](/6.1.8)) of the dissolution reaction.

**Definition 10.2.1** The product of the relative concentrations of the ions in a solution of a sparingly soluble electrolyte in any state, each raised to the power of its stoichiometric number, $Q = c(\ce{A^{m+}})^n\,c(\ce{B^{n-}})^m$, is called the **ion product**.

**Theorem 10.2.1 (Solubility Product Rule)** For the precipitation–dissolution equilibrium $\ce{A_nB_m(s) <=> n A^{m+} + m B^{n-}}$:

1. $Q = K_{\mathrm{sp}}$: the solution is saturated and at equilibrium;
2. $Q > K_{\mathrm{sp}}$: the solution is supersaturated, and precipitate will form until $Q = K_{\mathrm{sp}}$;
3. $Q < K_{\mathrm{sp}}$: the solution is unsaturated, and any solid present will dissolve until $Q = K_{\mathrm{sp}}$.

**Proof** This is the special case of the reaction-quotient criterion (Theorem 8.3.1 and Eq. (8.3)) for a dissolution reaction: $\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln(Q/K_{\mathrm{sp}})$. When $Q > K_{\mathrm{sp}}$, $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ for dissolution, and the reverse reaction (precipitation) is spontaneous; when $Q < K_{\mathrm{sp}}$, dissolution is spontaneous. $\square$

The **solubility product rule** is the basis for deciding whether a precipitate forms or dissolves. In practice, no precipitate is often seen when $Q$ is only slightly larger than $K_{\mathrm{sp}}$: nucleation of a new phase requires some supersaturation, and too small an amount of precipitate cannot be observed by eye.

**Example 10.2.1** At $25\,^\circ\mathrm{C}$, $0.50\,\mathrm{L}$ of $0.060\,\mathrm{mol\,L^{-1}}$ $\ce{CaCl2}$ solution is added to $1.00\,\mathrm{L}$ of $0.030\,\mathrm{mol\,L^{-1}}$ $\ce{AgNO3}$ solution. Will AgCl precipitate? If so, how many grams form? What is the final $[\ce{Ag+}]$?

**Solution** The total volume after mixing is $1.50\,\mathrm{L}$, so

$$
c(\ce{Ag+}) = \frac{1.00 \times 0.030}{1.50} = 0.020, \qquad c(\ce{Cl-}) = \frac{0.50 \times 2 \times 0.060}{1.50} = 0.040,
$$
and $Q = 0.020 \times 0.040 = 8.0 \times 10^{-4} \gg K_{\mathrm{sp}}(\ce{AgCl}) = 1.8 \times 10^{-10}$, so AgCl precipitates. Since $K_{\mathrm{sp}}$ is very small, we may first assume that all the $\ce{Ag+}$ precipitates and then find the equilibrium from the slight redissolution of the precipitate:

| | $\ce{Ag+}$ | $\ce{Cl-}$ |
|---|---|---|
| After mixing | 0.020 | 0.040 |
| After complete precipitation | 0 | 0.020 |
| Equilibrium | $x$ | $0.020 + x$ |

$K_{\mathrm{sp}} = x(0.020 + x) \approx 0.020x$, so $x = 9.0 \times 10^{-9}\,\mathrm{mol\,L^{-1}}$, confirming that almost all the $\ce{Ag+}$ has precipitated. The amount of AgCl formed is $0.030\,\mathrm{mol}$, that is, $0.030 \times 143.32 = 4.30\,\mathrm{g}$.

## 10.3. Factors Affecting the Precipitation–Dissolution Equilibrium

### 10.3.1. The Common-Ion Effect

When $\ce{BaCl2}$ or $\ce{Na2SO4}$ is added to a saturated solution of $\ce{BaSO4}$, $Q > K_{\mathrm{sp}}$, the equilibrium shifts in the direction of precipitation, and the solubility of $\ce{BaSO4}$ decreases. This is the manifestation, in precipitation–dissolution equilibrium, of the **common-ion effect** of [6.1.9](/6.1.9): adding to a solution of a sparingly soluble electrolyte a readily soluble strong electrolyte that contains the same ion lowers the solubility of the sparingly soluble electrolyte.

**Example 10.3.1** Calculate and compare the solubility of $\ce{CaF2}$ ($K_{\mathrm{sp}} = 3.45 \times 10^{-11}$) at $25\,^\circ\mathrm{C}$ in (1) pure water, (2) $0.010\,\mathrm{mol\,L^{-1}}$ $\ce{Ca(NO3)2}$ solution, and (3) $0.010\,\mathrm{mol\,L^{-1}}$ NaF solution.

**Solution** Let the solubilities in the three cases be $x_1$, $x_2$, and $x_3$ (neglecting the hydrolysis of $\ce{F-}$):

| | $[\ce{Ca^2+}]$ | $[\ce{F-}]$ | Equation |
|---|---|---|---|
| (1) Pure water | $x_1$ | $2x_1$ | $4x_1^3 = K_{\mathrm{sp}}$ |
| (2) $\ce{Ca(NO3)2}$ | $0.010 + x_2$ | $2x_2$ | $(0.010 + x_2)(2x_2)^2 = K_{\mathrm{sp}}$ |
| (3) NaF | $x_3$ | $0.010 + 2x_3$ | $x_3(0.010 + 2x_3)^2 = K_{\mathrm{sp}}$ |

(1) $x_1 = (K_{\mathrm{sp}}/4)^{1/3} = 2.1 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$. (2) $x_2 \ll 0.010$, so $0.010 \times 4x_2^2 = K_{\mathrm{sp}}$ and $x_2 = 2.9 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$. (3) $x_3 \ll 0.005$, so $x_3 = K_{\mathrm{sp}}/0.010^2 = 3.5 \times 10^{-7}\,\mathrm{mol\,L^{-1}}$.

At the same concentration of common ion, $\ce{F-}$ lowers the solubility far more: $[\ce{F-}]$ appears squared in $K_{\mathrm{sp}}$, so the solubility is inversely proportional to the square of the added $\ce{F-}$ concentration, but only to the square root of the added $\ce{Ca^2+}$ concentration.

![Left: solubility of CaF₂ as a function of the added Ca²⁺ or F⁻ concentration (common-ion effect, log–log axes); right: ratio of the solubility of BaSO₄ in KNO₃ solution to that in pure water (salt effect, activity coefficients estimated with the Davies equation)](./plots/common-ion-salt-effect.py)

Practical applications of the common-ion effect:

1. A moderate excess of precipitant is added to precipitate the target ion completely. Because of the precipitation–dissolution equilibrium, the concentration of the precipitated ion in solution cannot be zero; precipitation is generally considered complete when the residual concentration is below $10^{-5}\,\mathrm{mol\,L^{-1}}$ (below $10^{-6}\,\mathrm{mol\,L^{-1}}$ in quantitative analysis). Too large an excess of precipitant may in fact increase the solubility through the salt effect or complexation, and an excess of 20%–50% is usually appropriate.
2. Choosing a wash liquid. If $0.1\,\mathrm{g}$ of $\ce{BaSO4}$ precipitate is washed with $100\,\mathrm{mL}$ of pure water, the loss, assuming saturation, is $S \times 0.1\,\mathrm{L} \times M = 1.04 \times 10^{-5} \times 0.1 \times 233.4 = 2.4 \times 10^{-4}\,\mathrm{g}$ (0.24%); washing with $0.010\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ instead gives $[\ce{Ba^2+}] = K_{\mathrm{sp}}/0.010 = 1.1 \times 10^{-8}$ and a loss of only about $2.5 \times 10^{-7}\,\mathrm{g}$ (neglecting the formation of $\ce{HSO4-}$ does not change the order of magnitude).

### 10.3.2. The Salt Effect

**Definition 10.3.1** The increase in the solubility of a sparingly soluble electrolyte caused by adding to its solution a readily soluble strong electrolyte that neither reacts with it nor has an ion in common with it is called the **salt effect**.

For example, AgCl and $\ce{BaSO4}$ are more soluble in $\ce{KNO3}$ solution than in pure water. The reason lies in the electrostatic interaction between ions: when the ion concentration in the solution increases, each ion is surrounded by more ions of opposite sign than of the same sign, forming an "ionic atmosphere", so that the effective concentration of the ion, its **activity** ([6.1.8](/6.1.8)), is smaller than its concentration, $a = \gamma c/c^\circ$ with activity coefficient $\gamma < 1$. What holds rigorously is the solubility product expressed in activities, $K_{\mathrm{sp}} = a_{\ce{Ba^2+}}a_{\ce{SO4^2-}} = \gamma_{\ce{Ba^2+}}\gamma_{\ce{SO4^2-}}[\ce{Ba^2+}][\ce{SO4^2-}]$; when the activity coefficients decrease, the product of concentrations must increase, and the solubility increases accordingly. Activity coefficients decrease as the total concentration and charge of the ions in solution (the ionic strength) increase, and the higher the ionic charge the greater the decrease and the more pronounced the salt effect: estimated by Debye–Hückel theory (the Davies equation), the solubility of $\ce{BaSO4}$ in $0.010\,\mathrm{mol\,L^{-1}}$ $\ce{KNO3}$ is about 1.5 times that in pure water (right panel above). The theory of the ionic atmosphere and of activity coefficients is found in [Physical Chemistry](/6.3). (The salt effect is sometimes explained by saying that the ionic atmosphere reduces the number of collisions of ions with the precipitate surface, so that the dissolution rate temporarily exceeds the precipitation rate. This is a kinetic argument; the salt effect changes the position of equilibrium and should be explained by activities.)

When a strong electrolyte containing a common ion is added, the common-ion effect and the salt effect are both present. At low concentrations of the common ion the common-ion effect dominates and the solubility decreases; at higher concentrations the salt effect (and possibly complexation) becomes gradually significant. For example, the solubility of $\ce{PbSO4}$ in $\ce{Na2SO4}$ solution first falls rapidly with increasing $\ce{Na2SO4}$ concentration, reaches a minimum near $0.04\,\mathrm{mol\,L^{-1}}$, and then increases gradually. This is one reason why the precipitant should not be added in large excess.

### 10.3.3. The Acid Effect

If the anion of a sparingly soluble electrolyte is the anion of a weak acid or $\ce{OH-}$, adding acid combines the anion with $\ce{H+}$ to form a weak acid or water, lowers the anion concentration so that $Q < K_{\mathrm{sp}}$, and the precipitate dissolves.

**Definition 10.3.2** The influence of the acidity of the solution on the solubility of a sparingly soluble electrolyte is called the **acid effect**: the solubility of sparingly soluble salts of weak acids and of hydroxides increases as the pH of the solution decreases.

Consider first sparingly soluble hydroxides. From $K_{\mathrm{sp}} = [\ce{M^{n+}}][\ce{OH-}]^n$ and $[\ce{OH-}] = K_{\mathrm{w}}/[\ce{H+}]$,

$$
\lg[\ce{M^{n+}}] = \lg K_{\mathrm{sp}} + n\,\mathrm{p}K_{\mathrm{w}} - n\,\mathrm{pH}. \tag{10.3}
$$
In a plot of $\lg[\ce{M^{n+}}]$ against pH, each hydroxide is a straight line of slope $-n$: points on the line are at saturation equilibrium, the region to the left of the line (lower pH) is the unsaturated dissolution region, and the region to the right is the supersaturated precipitation region. Equation (10.3) gives the pH at which a $0.010\,\mathrm{mol\,L^{-1}}$ metal ion begins to precipitate ($[\ce{M^{n+}}] = 10^{-2}$) and at which precipitation is complete ($[\ce{M^{n+}}] = 10^{-5}$):

| Hydroxide | $\ce{Fe(OH)3}$ | $\ce{Al(OH)3}$ | $\ce{Cu(OH)2}$ | $\ce{Fe(OH)2}$ | $\ce{Mn(OH)2}$ | $\ce{Mg(OH)2}$ |
|---|---|---|---|---|---|---|
| Precipitation begins | 1.8 | 3.7 | 5.2 | 6.8 | 8.7 | 9.4 |
| Precipitation complete | 2.8 | 4.7 | 6.7 | 8.3 | 10.2 | 10.9 |

![Relation between lg[Mⁿ⁺] and pH in saturated solutions of several metal hydroxides: the dissolution region lies to the left of each line and the precipitation region to the right; the dashed line is the branch along which amphoteric Al(OH)₃ dissolves in base to form Al(OH)₄⁻](./plots/hydroxide-solubility.py)

By controlling the pH, some ions can be precipitated while others remain in solution. Consider iron impurities in a copper sulfate solution: the precipitation regions of $\ce{Fe^2+}$ and $\ce{Cu^2+}$ overlap, so they cannot be separated; but if $\ce{Fe^2+}$ is first oxidized to $\ce{Fe^3+}$ with $\ce{H2O2}$ and the pH is then adjusted to about 3.5, $\ce{Fe(OH)3}$ precipitates completely while $\ce{Cu^2+}$ does not. Amphoteric hydroxides ($\ce{Al(OH)3}$, $\ce{Zn(OH)2}$, $\ce{Cr(OH)3}$, $\ce{Sn(OH)2}$) dissolve again in strong base by forming hydroxo complex ions, for example $\ce{Al(OH)3(s) + OH- <=> [Al(OH)4]-}$, whose equilibrium constant is $K = K_{\mathrm{sp}}\beta_4 \approx 1.3$ ($\lg\beta_4(\ce{[Al(OH)4]-}) = 33.0$); the solubility of $\ce{Al(OH)3}$ is therefore smallest near pH 6 and increases markedly below pH 4 and above pH 12.

**Example 10.3.2** To $0.20\,\mathrm{L}$ of $0.50\,\mathrm{mol\,L^{-1}}$ $\ce{MgCl2}$ solution is added an equal volume of $0.10\,\mathrm{mol\,L^{-1}}$ aqueous ammonia. (1) Decide whether $\ce{Mg(OH)2}$ precipitates. (2) What is the minimum mass of solid $\ce{NH4Cl}$ that must be added to prevent $\ce{Mg(OH)2}$ from precipitating (assume no volume change)?

**Solution** (1) After mixing, $c(\ce{Mg^2+}) = 0.25$ and $c(\ce{NH3}) = 0.050$. By Eq. (9.2) of [6.1.9](/6.1.9), $[\ce{OH-}] = \sqrt{K_{\mathrm{b}}c} = \sqrt{1.8 \times 10^{-5} \times 0.050} = 9.5 \times 10^{-4}$, so

$$
Q = 0.25 \times (9.5 \times 10^{-4})^2 = 2.3 \times 10^{-7} > K_{\mathrm{sp}} = 5.61 \times 10^{-12},
$$
and $\ce{Mg(OH)2}$ precipitates.

(2) To prevent precipitation, $[\ce{OH-}] \le \sqrt{K_{\mathrm{sp}}/[\ce{Mg^2+}]} = \sqrt{5.61 \times 10^{-12}/0.25} = 4.7 \times 10^{-6}$. The added $\ce{NH4+}$ and $\ce{NH3}$ form a buffer solution, and from $K_{\mathrm{b}} = [\ce{NH4+}][\ce{OH-}]/[\ce{NH3}]$,

$$
[\ce{NH4+}] \ge \frac{K_{\mathrm{b}}[\ce{NH3}]}{[\ce{OH-}]} = \frac{1.8 \times 10^{-5} \times 0.050}{4.7 \times 10^{-6}} = 0.19.
$$
The required $\ce{NH4Cl}$ is $0.19 \times 0.40\,\mathrm{L} \times 53.49\,\mathrm{g\,mol^{-1}} = 4.1\,\mathrm{g}$. This is the principle by which an $\ce{NH3}$–$\ce{NH4Cl}$ buffer is used in qualitative analysis to precipitate $\ce{Fe^3+}$ and $\ce{Al^3+}$ while $\ce{Mg^2+}$ stays in solution.

Now consider sparingly soluble sulfides. The dissolution of a sulfide in acid can be written as the sum of three equilibria:

$$
\begin{aligned}
\ce{MS(s) &<=> M^2+ + S^2-} && K_{\mathrm{sp}}\\
\ce{S^2- + H+ &<=> HS-} && 1/K_{\mathrm{a2}}\\
\ce{HS- + H+ &<=> H2S(aq)} && 1/K_{\mathrm{a1}}
\end{aligned}
$$
The overall reaction and its equilibrium constant (by the rule of multiple equilibria) are

$$
\ce{MS(s) + 2H+ <=> M^2+ + H2S(aq)}, \qquad K_{\mathrm{spa}} = \frac{[\ce{M^2+}][\ce{H2S}]}{[\ce{H+}]^2} = \frac{K_{\mathrm{sp}}}{K_{\mathrm{a1}}K_{\mathrm{a2}}}. \tag{10.4}
$$
$K_{\mathrm{spa}}$ is called the acid solubility product. According to Remark 9.3.1 of [6.1.9](/6.1.9), the $K_{\mathrm{a2}}$ of $\ce{H2S}$ is very uncertain and $\ce{S^2-}$ is hardly present in water, so a calculation of sulfide dissolution from $K_{\mathrm{sp}}$ and $[\ce{S^2-}]$ gives results that vary by several orders of magnitude with the $K_{\mathrm{a2}}$ chosen. Only the species that actually exist, $\ce{M^2+}$, $\ce{H2S}$, and $\ce{H+}$, appear in Eq. (10.4); $K_{\mathrm{spa}}$ can be determined directly from solubility measurements and does not depend on $K_{\mathrm{a2}}$, which is why modern textbooks treat sulfides directly with $K_{\mathrm{spa}}$. Values of $K_{\mathrm{spa}}$ for freshly precipitated sulfides:

| Sulfide | MnS (flesh-colored) | FeS | ZnS | CdS | PbS | CuS | HgS (black) |
|---|---|---|---|---|---|---|---|
| $K_{\mathrm{spa}}$ | $3 \times 10^{10}$ | $6 \times 10^{2}$ | $3 \times 10^{-2}$ | $8 \times 10^{-7}$ | $3 \times 10^{-7}$ | $6 \times 10^{-16}$ | $2 \times 10^{-32}$ |

(The data are from a table common to general chemistry textbooks, originating in the compilation of Myers (1986). The solubility of sulfides depends strongly on crystal form and aging, so the values are meaningful only as orders of magnitude. The $K_{\mathrm{spa}}$ of crystalline sulfides calculated from $\Delta_{\mathrm{f}}G^\circ$ is generally smaller, for example about $2 \times 10^{-5}$ for sphalerite-type ZnS: a freshly formed precipitate is more soluble than the stable crystal.)

Sulfides with large $K_{\mathrm{spa}}$ (MnS, FeS, ZnS) dissolve in dilute hydrochloric acid; CdS and PbS require more concentrated hydrochloric acid; CuS has an extremely small $K_{\mathrm{spa}}$, and even in $1\,\mathrm{mol\,L^{-1}}$ HCl, $[\ce{Cu^2+}] = K_{\mathrm{spa}}[\ce{H+}]^2/[\ce{H2S}] = 6 \times 10^{-15}$ (with $[\ce{H2S}] = 0.10$ for saturated $\ce{H2S}$), so it does not dissolve in non-oxidizing acids.

### 10.3.4. Dissolution by Oxidation–Reduction

Sulfides with extremely small $K_{\mathrm{spa}}$ can be dissolved by means of redox reactions: an oxidizing agent oxidizes $\ce{H2S}$ (and $\ce{S^2-}$) to elemental sulfur, greatly lowering the effective concentration of sulfur species. CuS, PbS, and Ag₂S dissolve in hot dilute nitric acid:

$$
\ce{3CuS(s) + 8H+ + 2NO3- -> 3Cu^2+ + 2NO ^ + 3S v + 4H2O}.
$$
HgS has an even smaller $K_{\mathrm{spa}}$, and nitric acid cannot dissolve it; aqua regia is required: oxidation ($\ce{HNO3}$) and complexation ($\ce{Cl-}$ forms $\ce{[HgCl4]^2-}$ with $\ce{Hg^2+}$) together lower the concentrations of both ions,

$$
\ce{3HgS + 2HNO3 + 12HCl -> 3H2[HgCl4] + 3S v + 2NO ^ + 4H2O}.
$$
The direction and extent of redox reactions are judged from electrode potentials ([6.1.11](/6.1.11)).

### 10.3.5. The Complexation Effect

**Definition 10.3.3** When a complexing agent that forms soluble complexes with the ions of a sparingly soluble electrolyte is present in solution, the precipitation–dissolution equilibrium shifts toward dissolution, so that the solubility of the electrolyte increases or it dissolves completely; this phenomenon is called the **complexation effect**.

The dissolution of AgCl in aqueous ammonia is a combination of two equilibria (rule of multiple equilibria):

$$
\begin{aligned}
\ce{AgCl(s) &<=> Ag+ + Cl-} && K_{\mathrm{sp}}\\
\ce{Ag+ + 2NH3 &<=> [Ag(NH3)2]+} && \beta_2\\
\ce{AgCl(s) + 2NH3 &<=> [Ag(NH3)2]+ + Cl-} && K = K_{\mathrm{sp}}\beta_2 = \frac{[\ce{[Ag(NH3)2]+}][\ce{Cl-}]}{[\ce{NH3}]^2}
\end{aligned}
$$
$K = 1.8 \times 10^{-10} \times 1.7 \times 10^{7} = 3.1 \times 10^{-3}$ (with $\beta_2$ from [6.1.9](/6.1.9)). In $1.0\,\mathrm{mol\,L^{-1}}$ aqueous ammonia, let the solubility be $S$; then $[\ce{[Ag(NH3)2]+}] \approx [\ce{Cl-}] = S$, $[\ce{NH3}] = 1.0 - 2S$, and $\frac{S}{1.0 - 2S} = \sqrt K = 0.055$, giving $S = 0.050\,\mathrm{mol\,L^{-1}}$, more than three thousand times the solubility in pure water. The same treatment of AgBr and AgI gives:

| Dissolution reaction | $K = K_{\mathrm{sp}}\beta_2$ | Solubility in $1.0\,\mathrm{mol\,L^{-1}}$ complexing agent |
|---|---|---|
| $\ce{AgCl + 2NH3}$ | $3.1 \times 10^{-3}$ | $0.050\,\mathrm{mol\,L^{-1}}$, readily soluble |
| $\ce{AgBr + 2NH3}$ | $9.2 \times 10^{-6}$ | $3.0 \times 10^{-3}\,\mathrm{mol\,L^{-1}}$, slightly soluble |
| $\ce{AgI + 2NH3}$ | $1.4 \times 10^{-9}$ | $3.8 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$, essentially insoluble |
| $\ce{AgBr + 2S2O3^2-}$ | 16 | readily soluble (photographic fixing) |
| $\ce{AgI + 2CN-}$ | $1.1 \times 10^{5}$ | readily soluble |

Whether a precipitate can be dissolved by a complexing agent depends on the product of $K_{\mathrm{sp}}$ and $\beta$: the larger $K_{\mathrm{sp}}$ and the more stable the complex ion, the more readily it dissolves. The differences in the solubility of AgCl, AgBr, and AgI in aqueous ammonia can be used to separate and identify $\ce{Cl-}$, $\ce{Br-}$, and $\ce{I-}$.

![Solubility of AgCl, AgBr, and AgI in aqueous ammonia as a function of the total ammonia concentration (solved numerically from Ksp and the stability constants of Ag(NH₃)⁺ and Ag(NH₃)₂⁺; the slope is close to 1 because the solubility is approximately proportional to [NH₃])](./plots/silver-halide-ammonia.py)

The curves in the figure were obtained by numerically solving the precipitation equilibrium, the two complexation steps, and the mass balance of ammonia simultaneously; at higher ammonia concentrations $S \approx \sqrt K\,c(\ce{NH3})$, a straight line of slope 1 on the log–log plot. Conversely, an excess of the complexing agent must also be watched: when $\ce{Cl-}$ is used to precipitate $\ce{Ag+}$, too large an excess of $\ce{Cl-}$ produces complex ions such as $\ce{[AgCl2]-}$ and the precipitate partly redissolves, which is another reason, besides those in 10.3.1, why the precipitant should not be added in large excess.

## 10.4. Shifting Precipitation–Dissolution Equilibria

### 10.4.1. Fractional Precipitation

**Example 10.4.1** The concentrations of $\ce{I-}$ and $\ce{Cl-}$ in a solution are both $0.010\,\mathrm{mol\,L^{-1}}$, and $\ce{AgNO3}$ solution is added dropwise (neglect the volume change). Which ion precipitates first? When the second ion begins to precipitate, has the first been completely precipitated? $K_{\mathrm{sp}}(\ce{AgCl}) = 1.8 \times 10^{-10}$ and $K_{\mathrm{sp}}(\ce{AgI}) = 8.5 \times 10^{-17}$.

**Solution** The $[\ce{Ag+}]$ required for each precipitate to begin to form is

$$
\text{AgI: } [\ce{Ag+}] = \frac{8.5 \times 10^{-17}}{0.010} = 8.5 \times 10^{-15}, \qquad \text{AgCl: } [\ce{Ag+}] = \frac{1.8 \times 10^{-10}}{0.010} = 1.8 \times 10^{-8}.
$$
AgI requires a much smaller $[\ce{Ag+}]$ and precipitates first. When AgCl begins to precipitate, $[\ce{Ag+}] = 1.8 \times 10^{-8}$, and at that point

$$
[\ce{I-}] = \frac{8.5 \times 10^{-17}}{1.8 \times 10^{-8}} = 4.7 \times 10^{-9} \ll 10^{-5},
$$
so $\ce{I-}$ was precipitated completely long before, and the two can be separated.

**Definition 10.4.1** The phenomenon in which several ions that form precipitates with the same precipitant are present in a solution and the precipitates form one after another, in the order in which the ion product first reaches the solubility product, is called **fractional precipitation**.

Which precipitates first depends, first, on the magnitude of $K_{\mathrm{sp}}$ and, second, on the concentrations of the ions (and for precipitates of different types, also on the stoichiometry): the one whose ion product first reaches its solubility product precipitates first. The greater the difference in $K_{\mathrm{sp}}$, the more complete the separation. If $[\ce{Cl-}]$ were much larger than $[\ce{I-}]$ in the example above, as in seawater, AgCl might precipitate first. One application of fractional precipitation is the Mohr method in precipitation titration: $\ce{Cl-}$ is titrated with $\ce{AgNO3}$ using $\ce{K2CrO4}$ as indicator; AgCl precipitates first, and the brick-red $\ce{Ag2CrO4}$ appears only after $\ce{Cl-}$ has essentially all precipitated, signaling the end point ([Analytical Chemistry](/6.4)).

### 10.4.2. Conversion of Precipitates

**Definition 10.4.2** The process in which a suitable reagent is added to a solution containing a precipitate so that one precipitate is converted into another is called the **conversion of precipitates**.

The $\ce{CaSO4}$ in boiler scale does not dissolve in acid and is hard to remove. Treating it with $\ce{Na2CO3}$ solution converts it into loose $\ce{CaCO3}$, which dissolves in acid:

$$
\ce{CaSO4(s) + CO3^2- <=> CaCO3(s) + SO4^2-}, \qquad K = \frac{[\ce{SO4^2-}]}{[\ce{CO3^2-}]} = \frac{K_{\mathrm{sp}}(\ce{CaSO4})}{K_{\mathrm{sp}}(\ce{CaCO3})} = \frac{4.93 \times 10^{-5}}{3.36 \times 10^{-9}} = 1.5 \times 10^{4}.
$$
(Multiply numerator and denominator by $[\ce{Ca^2+}]$ to see this.) $K$ is very large, and the conversion is very complete. A precipitate with a larger solubility product is readily converted into one of the same type with a smaller solubility product, and the larger $K$ is, the more easily the conversion proceeds.

Under suitable conditions a precipitate with a smaller solubility product can also be converted into one with a larger solubility product, provided the two $K_{\mathrm{sp}}$ values do not differ too much. For example, $\ce{BaSO4}$, which is insoluble in acid, is treated with saturated $\ce{Na2CO3}$ solution:

$$
\ce{BaSO4(s) + CO3^2- <=> BaCO3(s) + SO4^2-}, \qquad K = \frac{K_{\mathrm{sp}}(\ce{BaSO4})}{K_{\mathrm{sp}}(\ce{BaCO3})} = \frac{1.08 \times 10^{-10}}{2.58 \times 10^{-9}} = 0.042 \approx \frac{1}{24}.
$$
The reaction proceeds to the right as long as $[\ce{CO3^2-}] > 24[\ce{SO4^2-}]$. Treating once with $1\,\mathrm{L}$ of $1.6\,\mathrm{mol\,L^{-1}}$ $\ce{Na2CO3}$, at equilibrium $\frac{x}{1.6 - x} = 0.042$, so $x = 0.064\,\mathrm{mol}$, that is, about $15\,\mathrm{g}$ of $\ce{BaSO4}$ is converted; pouring off the solution and repeating the treatment a few times with fresh $\ce{Na2CO3}$ solution converts it all, and the $\ce{BaCO3}$ can then be dissolved in acid. This is the method of preparing other barium compounds from barite. (Some textbooks take $K_{\mathrm{sp}}(\ce{BaCO3}) = 5.1 \times 10^{-9}$, which gives $K \approx 1/46$; here the CRC data are used consistently.)

### 10.4.3. Separation of Metal Ions

Combining the solubility product rule with the acid effect, metal ions can be precipitated separately as hydroxides or sulfides by controlling the pH. The separation of hydroxides is covered by the table in 10.3.3; sulfides are usually separated with saturated $\ce{H2S}$ solution ($[\ce{H2S}] \approx 0.10\,\mathrm{mol\,L^{-1}}$) as precipitant. From Eq. (10.4),

$$
\lg[\ce{M^2+}] = \lg K_{\mathrm{spa}} - \lg[\ce{H2S}] - 2\,\mathrm{pH} = \lg K_{\mathrm{spa}} + 1 - 2\,\mathrm{pH}:
$$
in a plot of $\lg[\ce{M^2+}]$ against pH, each sulfide is a straight line of slope $-2$, and the smaller $K_{\mathrm{spa}}$ is, the farther to the left the line lies (the sulfide precipitates even in more acidic solution).

![Relation between lg[M²⁺] and pH for several metal sulfides in saturated H₂S solution (calculated from Kspa; the line for CuS lies far to the lower left of the plot): by keeping the pH between two lines, one sulfide can be precipitated completely while the other does not precipitate](./plots/sulfide-separation.py)

**Example 10.4.2** The concentrations of $\ce{Zn^2+}$ and $\ce{Mn^2+}$ in a solution are both $0.10\,\mathrm{mol\,L^{-1}}$, and $\ce{H2S}$ is passed in until saturation. Within what pH range must the solution be kept so that ZnS precipitates completely while MnS does not precipitate?

**Solution** By Eq. (10.4), $[\ce{M^2+}] = K_{\mathrm{spa}}[\ce{H+}]^2/[\ce{H2S}]$: the lower the acidity, the less $\ce{M^2+}$ can remain in solution. Complete precipitation of ZnS requires $[\ce{Zn^2+}] \le 10^{-5}$:

$$
[\ce{H+}] \le \sqrt{\frac{10^{-5} \times [\ce{H2S}]}{K_{\mathrm{spa}}(\ce{ZnS})}} = \sqrt{\frac{10^{-5} \times 0.10}{3 \times 10^{-2}}} = 5.8 \times 10^{-3}, \qquad \mathrm{pH} \ge 2.2.
$$
For MnS not to precipitate, the solution must not be supersaturated at $[\ce{Mn^2+}] = 0.10$:

$$
[\ce{H+}] \ge \sqrt{\frac{0.10 \times 0.10}{3 \times 10^{10}}} = 5.8 \times 10^{-7}, \qquad \mathrm{pH} \le 6.2.
$$
With the pH controlled between 2.2 and 6.2 (for example with an HAc–NaAc buffer), ZnS precipitates completely while MnS does not.

The same calculation for the separation of $\ce{Cd^2+}$ and $\ce{Zn^2+}$ (each $0.10\,\mathrm{mol\,L^{-1}}$) shows that complete precipitation of CdS requires $[\ce{H+}] \le 1.1\,\mathrm{mol\,L^{-1}}$ and non-precipitation of ZnS requires $[\ce{H+}] \ge 0.58\,\mathrm{mol\,L^{-1}}$, a very narrow window. In actual qualitative analysis, CdS, PbS, CuS, HgS, and so on are precipitated by passing $\ce{H2S}$ into about $0.3\,\mathrm{mol\,L^{-1}}$ HCl (the hydrogen sulfide group). By the data in the table above, ZnS is already supersaturated under these conditions (the $[\ce{Zn^2+}]$ allowed to remain in solution is only about $0.03\,\mathrm{mol\,L^{-1}}$), but ZnS nucleates very slowly from acidic solution and does not precipitate in the usual working time: the separation exploits differences in rate as well as in equilibrium. This again shows that sulfide data can be used only as order-of-magnitude estimates. The systematic grouping scheme of qualitative analysis is found in [Analytical Chemistry](/6.4).

## Questions

1. Why can $\ce{BaSO4}$ be used as a contrast agent for the digestive tract (a "barium meal") while $\ce{BaCO3}$ cannot, although their $K_{\mathrm{sp}}$ values differ by only a factor of about 24?
   Answer: Gastric acid (about $0.1\,\mathrm{mol\,L^{-1}}$ HCl) converts $\ce{CO3^2-}$ to $\ce{CO2}$, so $\ce{BaCO3}$ dissolves through the acid effect and releases toxic $\ce{Ba^2+}$; $\ce{SO4^2-}$ is an extremely weak base ($\mathrm{p}K_{\mathrm{a}}$ of $\ce{HSO4-}$ is 1.99), and the solubility of $\ce{BaSO4}$ is hardly affected by gastric acid.
2. Tooth enamel is mainly hydroxyapatite, $\ce{Ca5(PO4)3OH}$. Why do acids in the mouth after eating sugar corrode teeth, while fluoride toothpaste prevents caries?
   Answer: Acid combines with $\ce{OH-}$ and $\ce{PO4^3-}$, and the acid effect dissolves hydroxyapatite; $\ce{F-}$ replaces $\ce{OH-}$ to form fluorapatite, $\ce{Ca5(PO4)3F}$, which is less soluble and whose anions do not react with acid (conversion of precipitates).
3. AgCl dissolves in aqueous ammonia; why does AgI not? What reagent can dissolve AgI?
   Answer: The equilibrium constant $K_{\mathrm{sp}}\beta_2$ of the dissolution reaction is only $1.4 \times 10^{-9}$ for AgI (10.3.5). A softer base ligand that binds $\ce{Ag+}$ more strongly is required, such as $\ce{CN-}$ ($K \approx 10^5$).

## Summary

| Topic | Key points |
|---|---|
| Solubility product | $K_{\mathrm{sp}} = [\ce{A^{m+}}]^n[\ce{B^{n-}}]^m$, with no pure solid in the expression; can be calculated from $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K_{\mathrm{sp}}$ |
| Solubility | $S = (K_{\mathrm{sp}}/n^nm^m)^{1/(n+m)}$, valid only when the ions do not hydrolyze, associate, or complex; $K_{\mathrm{sp}}$ of precipitates of different types cannot be compared directly |
| Solubility product rule | $Q > K_{\mathrm{sp}}$ precipitation, $Q = K_{\mathrm{sp}}$ saturation, $Q < K_{\mathrm{sp}}$ dissolution; precipitation is complete when the residual concentration is $< 10^{-5}\,\mathrm{mol\,L^{-1}}$ |
| Common-ion and salt effects | A common ion lowers the solubility; an unrelated strong electrolyte raises it by lowering the activity coefficients |
| Acid effect | Hydroxides: $\lg[\ce{M^{n+}}] = \lg K_{\mathrm{sp}} + n\,\mathrm{p}K_{\mathrm{w}} - n\,\mathrm{pH}$; sulfides: $K_{\mathrm{spa}} = [\ce{M^2+}][\ce{H2S}]/[\ce{H+}]^2$, without going through $[\ce{S^2-}]$ |
| Oxidation–reduction and complexation | Oxidizing and complexing agents lower the effective concentration of ions and dissolve the precipitate; for dissolution by complexation $K = K_{\mathrm{sp}}\beta_n$ |
| Fractional precipitation | The ion whose ion product first reaches the solubility product precipitates first |
| Conversion of precipitates | $K = K_{\mathrm{sp}}(\text{old})/K_{\mathrm{sp}}(\text{new})$ (same type); conversion toward the less soluble precipitate is easy, and the reverse is also possible when the $K_{\mathrm{sp}}$ values do not differ much |
| Separation of ions | Control the pH so that hydroxides or sulfides precipitate stepwise |
