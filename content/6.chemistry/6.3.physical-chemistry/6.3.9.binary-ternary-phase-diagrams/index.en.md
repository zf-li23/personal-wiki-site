---
title: Phase Diagrams of Binary and Ternary Systems
description: Phase-rule analysis of binary systems; p–x and T–x diagrams of ideal liquid mixtures, system points and phase points, the lever rule and fractional distillation; nonideal systems and azeotropes, the Duhem–Margules equation and Konovalov's rules; partially miscible liquids, critical solution temperatures and phase separation in regular solutions, immiscible liquids and steam distillation; thermal analysis and cooling curves, simple eutectic systems and the ideal solubility equation, water–salt systems, congruent and incongruent compounds, solid solutions and zone refining; the seven basic types of phase diagrams and how to read complex ones, the Fe–C diagram; triangular coordinates for ternary systems and extraction.
source_hash: e3bc0dbeef98
---

The previous chapter used the phase rule and the Clapeyron equation to treat one-component systems. This chapter turns to binary systems, the part of phase equilibrium used most in chemical engineering, metallurgy, materials science, and pharmacy: distillation and fractional distillation, extraction, purification by crystallization, and alloy design are all based on phase diagrams. The phase diagram of a binary system can be computed from the solution thermodynamics of the preceding chapters: ideal systems follow **Raoult's law** ([6.3.5](/6.3.5)), nonideal systems are described by **activity coefficients** and the **regular solution** model ([6.3.6](/6.3.6)), and solid–liquid equilibria use the same formula as **freezing-point depression**. The diagrams in this chapter were all computed in this way with Python. For real, complex systems, however, phase diagrams are determined mainly by experiment, and one must learn to read them. The chapter treats gas–liquid, liquid–liquid, and solid–liquid equilibria in turn, then summarizes the rules for reading complex phase diagrams, and finally gives a brief introduction to the triangular coordinates and extraction of ternary systems.

## 9.1. Gas–Liquid Equilibrium of Ideal Liquid Mixtures

### 9.1.1. Phase-Rule Analysis of Binary Systems

For a binary system $C = 2$, and the **phase rule** ([6.3.8](/6.3.8)) gives $F = 4 - P$. For $P = 1$, $F = 3$: the coordinates $T$, $p$, and one composition variable are needed, so the complete phase diagram is three-dimensional. For $F = 0$, $P = 4$, so at most four phases coexist. To draw a plane diagram, one variable is held fixed and the **conditional variance** $F^* = 3 - P$ is used:

| Fixed variable | Plane diagram | Use |
|---|---|---|
| Temperature | $p$–$x$ diagram (vapor pressure–composition) | Corresponds directly to Raoult's law; convenient for theoretical analysis |
| Pressure | $T$–$x$ diagram (boiling point–composition, melting point–composition) | Distillation and crystallization are carried out at constant pressure, so this is the most used |
| Composition | $p$–$T$ diagram | Least used |

On a plane diagram, a single-phase region has $F^* = 2$, a two-phase region has $F^* = 1$, and three coexisting phases have $F^* = 0$ (a horizontal line).

### 9.1.2. The p–x Diagram

Let A and B form an **ideal liquid mixture** with an ideal-gas vapor. By Raoult's law, at constant temperature

$$
p_{\mathrm{A}} = p_{\mathrm{A}}^*x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = p_{\mathrm{B}}^*x_{\mathrm{B}}, \qquad p = p_{\mathrm{A}} + p_{\mathrm{B}} = p_{\mathrm{A}}^* + (p_{\mathrm{B}}^* - p_{\mathrm{A}}^*)\,x_{\mathrm{B}},
\tag{9.1}
$$
where $x$ denotes the liquid composition and $p_{\mathrm{A}}^*$, $p_{\mathrm{B}}^*$ are the **saturated vapor pressures** of the pure liquids. The total pressure is a linear function of the liquid composition; this line is called the liquid line. The vapor composition $y_{\mathrm{B}}$ in equilibrium with it follows from Dalton's law of partial pressures:

$$
y_{\mathrm{B}} = \frac{p_{\mathrm{B}}}{p} = \frac{p_{\mathrm{B}}^*x_{\mathrm{B}}}{p}, \qquad \frac{y_{\mathrm{B}}}{y_{\mathrm{A}}} = \frac{p_{\mathrm{B}}^*}{p_{\mathrm{A}}^*}\cdot\frac{x_{\mathrm{B}}}{x_{\mathrm{A}}}.
$$
If $p_{\mathrm{B}}^* > p_{\mathrm{A}}^*$ (B is the more volatile component), then $y_{\mathrm{B}}/y_{\mathrm{A}} > x_{\mathrm{B}}/x_{\mathrm{A}}$, that is, $y_{\mathrm{B}} > x_{\mathrm{B}}$: the more volatile component is richer in the vapor than in the liquid, which is the basis of every distillation. Solving for $x$ and substituting into Eq. (9.1) gives the relation between the total pressure and the vapor composition,

$$
\frac{1}{p} = \frac{y_{\mathrm{A}}}{p_{\mathrm{A}}^*} + \frac{y_{\mathrm{B}}}{p_{\mathrm{B}}^*},
$$
a curve lying below the liquid line, called the vapor line. Above the liquid line is the liquid region, below the vapor line is the vapor region, and between the two lines is the two-phase gas–liquid region.

### 9.1.3. The T–x Diagram, System Points, and Phase Points

The $T$–$x$ diagram at constant pressure can be measured experimentally (the boiling points of solutions of different compositions and the compositions of the coexisting vapor and liquid at boiling) or computed from the $p$–$x$ relation: for each liquid composition, find the temperature at which the total pressure equals the external pressure $p$. Benzene–toluene is a nearly ideal system, and the figure below shows both of its diagrams computed from the Antoine equation and Raoult's law. In the $T$–$x$ diagram, the more volatile component has the lower boiling point; the liquid line (boiling-point line) lies below and the vapor line (dew-point line) above, and both are curves. The vapor region lies above the two-phase region and the liquid region below it, the reverse of the $p$–$x$ diagram.

![Benzene–toluene computed from Raoult's law with Antoine vapor pressures. Left: p–x diagram at 90 °C; the liquid line is straight and lies above the vapor line, and the dashed lines are the partial pressures. Right: T–x diagram at 101.325 kPa; the boiling-point (bubble) line lies below the dew-point line. The tie line a–O–b at 95 °C joins the liquid and vapor compositions in equilibrium with the system point O (overall benzene mole fraction 0.5)](./plots/benzene-toluene.py)

**Definition 9.1.1** A point in a phase diagram that represents the overall composition of the system (at given temperature and pressure) is called the **system point**, and a point that represents the composition of one phase is called a **phase point**. In a single-phase region the system point and the phase point coincide; in a two-phase region the system point lies on the horizontal line joining the two phase points, and this line connecting the phase points of the two equilibrium phases is called a *tie line*.

Heat a liquid of composition $X_{\mathrm{B}}$ at constant pressure, and the system point rises along the vertical line. On reaching the liquid line it begins to boil, and this temperature is called the *bubble point* of the liquid. On further heating, the liquid becomes poorer in the more volatile component B, the liquid point moves along the liquid line toward the A side with an ever higher boiling temperature, and the vapor point moves along the vapor line. On reaching the vapor line the last drop of liquid has evaporated, and this temperature, regarded as a property of a vapor of composition $X_{\mathrm{B}}$, is called its *dew point*. In the two-phase region $F^* = 1$: once the temperature is fixed, the compositions of both phases are fixed, and only the amounts of the two phases change as the system point moves.

### 9.1.4. The Lever Rule

**Theorem 9.1.1 (Lever Rule)** A system of overall composition $X_{\mathrm{B}}$ and total amount $n$ separates into two phases of compositions $x_{\mathrm{B}}$ and $y_{\mathrm{B}}$. The amounts $n_{\mathrm{l}}$ and $n_{\mathrm{g}}$ of the two phases satisfy

$$
n_{\mathrm{l}}\,(X_{\mathrm{B}} - x_{\mathrm{B}}) = n_{\mathrm{g}}\,(y_{\mathrm{B}} - X_{\mathrm{B}}), \qquad \text{that is} \qquad \frac{n_{\mathrm{l}}}{n_{\mathrm{g}}} = \frac{\overline{\mathrm{Ob}}}{\overline{\mathrm{aO}}},
$$
where O, a, and b are the system point and the two phase points, and $\overline{\mathrm{aO}}$ and $\overline{\mathrm{Ob}}$ are the lengths of the segments on the tie line.

**Proof** Conservation of the amount of B gives $nX_{\mathrm{B}} = n_{\mathrm{l}}x_{\mathrm{B}} + n_{\mathrm{g}}y_{\mathrm{B}}$, and conservation of the total amount gives $n = n_{\mathrm{l}} + n_{\mathrm{g}}$. Multiplying the second equation by $X_{\mathrm{B}}$ and subtracting the first gives the result. $\square$

The amounts of the two phases are inversely proportional to the distances from their phase points to the system point, like a lever with the system point as fulcrum. The lever rule is only conservation of mass, so it applies to every two-phase region of every phase diagram (liquid–liquid, solid–liquid, and the tie lines of ternary diagrams); when the abscissa is the mass fraction, the amounts are replaced by the masses of the two phases.

**Example 9.1.1** A and B form an ideal liquid mixture; the boiling points of pure A and pure B are $393\,\mathrm{K}$ and $358\,\mathrm{K}$. At $p^\circ$ a solution of composition $x_{\mathrm{B}} = 0.4$ boils at $373\,\mathrm{K}$, and the vapor composition is $y_{\mathrm{B}} = 0.8$. At $373\,\mathrm{K}$ and $p^\circ$, $90\,\mathrm{mol}$ of B vapor is slowly passed into $10\,\mathrm{mol}$ of liquid A. Describe how the state of the system changes.

**Solution** Temperature and pressure are constant, so the system point moves along the horizontal line at $373\,\mathrm{K}$ from $X_{\mathrm{B}} = 0$ toward $X_{\mathrm{B}} = 90/100 = 0.9$.

1. $0 < X_{\mathrm{B}} < 0.4$: $373\,\mathrm{K}$ is below the boiling points of these solutions, so all the B passed in dissolves in the liquid (the heat of condensation released is removed by the thermostat), and the system consists of the liquid phase only.
2. $X_{\mathrm{B}} = 0.4$ (a total of $6.67\,\mathrm{mol}$ of B passed in): the liquid reaches its bubble point and begins to produce a vapor of composition $y_{\mathrm{B}} = 0.8$.
3. $0.4 < X_{\mathrm{B}} < 0.8$: gas and liquid coexist, with fixed compositions 0.8 and 0.4, and their amounts follow from the lever rule. For example, at $X_{\mathrm{B}} = 0.6$ (a total of $25\,\mathrm{mol}$), $n_{\mathrm{l}}(0.6 - 0.4) = n_{\mathrm{g}}(0.8 - 0.6)$, so each phase is $12.5\,\mathrm{mol}$.
4. $X_{\mathrm{B}} = 0.8$ (a total of $40\,\mathrm{mol}$ of B passed in): the liquid phase disappears, and from there up to $X_{\mathrm{B}} = 0.9$ only the vapor phase is present. The final result is $100\,\mathrm{mol}$ of mixed vapor of composition $y_{\mathrm{B}} = 0.9$.

### 9.1.5. Fractional Distillation

The vapor obtained from a single partial vaporization is only slightly richer in the more volatile component than the liquid. Repeating many times the partial condensation of the vapor and the partial vaporization of the liquid separates the two components; this is called *fractional distillation*. On the $T$–$x$ diagram, each vaporization–condensation step corresponds to drawing a horizontal tie line in the two-phase region and then moving vertically to the phase boundary: the vapor approaches pure B step by step (at the top of the column), and the liquid approaches pure A (at the bottom).

A fractionating column makes this process continuous: the bottom is heated and vapor rises through the column; part of the condensate at the top is returned as reflux and flows down; on each tray the rising vapor contacts the descending liquid and approaches equilibrium with it, which is equivalent to one partial vaporization and one partial condensation. The separation achieved by one gas–liquid equilibrium is called one theoretical plate; the closer the volatilities of the two components (the closer $p_{\mathrm{B}}^*/p_{\mathrm{A}}^*$ is to 1), the more theoretical plates are needed. Petroleum refining, the separation of liquid air into $\ce{O2}$ and $\ce{N2}$, and the enrichment of isotopes (such as $\ce{D2O}$) all rely on fractional distillation.

## 9.2. Gas–Liquid Equilibrium of Nonideal Liquid Mixtures

### 9.2.1. Systems with Small Deviations

Real mixtures show positive deviations from Raoult's law ($p_{\mathrm{B}} > p_{\mathrm{B}}^*x_{\mathrm{B}}$, activity coefficient $\gamma > 1$; the A–B attraction is weaker than the A–A and B–B attractions, as in $\ce{CH3OH}$–$\ce{H2O}$ and $\ce{CCl4}$–$\ce{C6H6}$) or negative deviations ($\gamma < 1$; there are stronger A–B interactions such as hydrogen bonds, as in $\ce{CHCl3}$–acetone). When the deviations are small, the total pressure still lies between $p_{\mathrm{A}}^*$ and $p_{\mathrm{B}}^*$, the liquid line is only slightly convex or concave, the $T$–$x$ diagram resembles that of an ideal system, and fractional distillation can again be used for separation.

### 9.2.2. Azeotropes

For large positive deviations the total pressure in the $p$–$x$ diagram passes through a maximum, and correspondingly the $T$–$x$ diagram has a minimum; for large negative deviations the $p$–$x$ diagram has a minimum and the $T$–$x$ diagram a maximum. At such an extremum the liquid line and the vapor line are tangent.

**Definition 9.2.1 (Azeotrope)** In a constant-pressure $T$–$x$ diagram, the extremum at which the gas and liquid phases have the same composition is called the azeotropic point (a minimum-boiling or maximum-boiling azeotropic point), and a liquid mixture whose composition is that of the azeotropic point is called an **azeotrope**.

Properties of an azeotrope:

1. On boiling, the gas and liquid have the same composition, $x_{\mathrm{B}} = y_{\mathrm{B}}$ (this is proved in Theorem 9.2.2), so it boils at constant temperature like a pure substance, and the composition of the distillate does not change.
2. It is a mixture, not a compound: when the pressure changes, both the temperature and the composition of the azeotropic point change. By the phase rule, two phases coexisting at constant pressure have $F^* = 1$, and the azeotropic condition $x_{\mathrm{B}} = y_{\mathrm{B}}$ gives one more relation, so $F^* = 0$: at a given pressure, both the composition and the boiling point of the azeotrope are fixed.
3. For a system with an azeotrope, ordinary fractional distillation cannot yield both pure components. Such a diagram can be viewed as two diagrams with "small deviations" joined at the azeotropic point: for a minimum-boiling azeotropic system, the azeotrope is obtained at the top of the column and the pure component on the side of the feed composition at the bottom.

![T–x–y diagrams at 101.325 kPa computed from Raoult's law with activity coefficients. Left: ethanol + water (van Laar model), with a minimum-boiling azeotrope at x(ethanol) ≈ 0.92, 78.2 °C (measured: 0.894, 78.15 °C). Right: acetone + chloroform (one-parameter Margules model), with a maximum-boiling azeotrope at x(acetone) ≈ 0.38, 64.3 °C](./plots/azeotropes.py)

| System ($101.325\,\mathrm{kPa}$) | Type | Azeotropic point | Azeotropic composition |
|---|---|---|---|
| Ethanol–water | Minimum-boiling | $78.15\,{}^\circ\mathrm{C}$ | 95.6% ethanol by mass ($x = 0.894$) |
| Acetone–chloroform | Maximum-boiling | $64.5\,{}^\circ\mathrm{C}$ | $x(\text{acetone}) \approx 0.38$ |
| $\ce{HCl}$–water | Maximum-boiling | $108.6\,{}^\circ\mathrm{C}$ | 20.2% $\ce{HCl}$ by mass |
| $\ce{HNO3}$–water | Maximum-boiling | $120.5\,{}^\circ\mathrm{C}$ | 68% $\ce{HNO3}$ by mass |

The azeotropic composition of ethanol–water varies with pressure: it is 98.7% ethanol by mass at $17.3\,\mathrm{kPa}$ and 95.25% at $193.5\,\mathrm{kPa}$, and at sufficiently low pressure the azeotrope disappears. Fractional distillation of a 50% ethanol solution by mass gives 95.6% azeotropic ethanol at the top and water at the bottom. To produce absolute ethanol the azeotrope must be broken: by azeotropic distillation with benzene or cyclohexane as an entrainer (which forms a new ternary minimum-boiling azeotrope that carries off the water), by pressure-swing distillation that exploits the pressure dependence of the azeotropic composition, or by selective adsorption of the water on molecular sieves. The composition of azeotropic hydrochloric acid is precisely fixed at a given pressure and does not change on distillation, so it has been used as a primary standard in acid–base titration.

### 9.2.3. The Duhem–Margules Equation and Konovalov's Rules

Why must the gas and liquid have the same composition at an extremum? The answer comes from the constraint that the **Gibbs–Duhem equation** ([6.3.4](/6.3.4)) places on the vapor pressures of the two components.

**Theorem 9.2.1 (Duhem–Margules Equation)** At constant temperature, for the ideal vapor in equilibrium with a binary liquid mixture (neglecting the effect of the total pressure on the chemical potentials of the liquid, that is, dropping the $V_{\mathrm{m}}\,\mathrm{d}p$ term), the partial pressures of the two components satisfy

$$
x_{\mathrm{A}}\,\mathrm{d}\ln p_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln p_{\mathrm{B}} = 0, \qquad \text{that is} \qquad \left(\frac{\partial\ln p_{\mathrm{A}}}{\partial\ln x_{\mathrm{A}}}\right)_T = \left(\frac{\partial\ln p_{\mathrm{B}}}{\partial\ln x_{\mathrm{B}}}\right)_T.
\tag{9.2}
$$

**Proof** At constant temperature and pressure the Gibbs–Duhem equation of the liquid is $x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}}(\mathrm{l}) + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}}(\mathrm{l}) = 0$. At gas–liquid equilibrium $\mu_{\mathrm{B}}(\mathrm{l}) = \mu_{\mathrm{B}}(\mathrm{g}) = \mu_{\mathrm{B}}^\circ(\mathrm{g}) + RT\ln(p_{\mathrm{B}}/p^\circ)$, so $\mathrm{d}\mu_{\mathrm{B}}(\mathrm{l}) = RT\,\mathrm{d}\ln p_{\mathrm{B}}$, and likewise for A; substitution gives the first form. Dividing by $\mathrm{d}x_{\mathrm{A}} = -\mathrm{d}x_{\mathrm{B}}$ and using $x\,\mathrm{d}\ln p/\mathrm{d}x = \mathrm{d}\ln p/\mathrm{d}\ln x$ gives the second. Strictly, the total pressure in equilibrium with the liquid also changes with composition, and the Gibbs–Duhem equation should contain a term $V_{\mathrm{m}}\,\mathrm{d}p$; the molar volume of a liquid is small, so this term can be neglected. $\square$

Three consequences follow from Eq. (9.2):

1. $\left(\partial p_{\mathrm{A}}/\partial p_{\mathrm{B}}\right)_T = -x_{\mathrm{B}}p_{\mathrm{A}}/(x_{\mathrm{A}}p_{\mathrm{B}}) < 0$: when the partial pressure of one component increases with composition, that of the other must decrease.
2. If over some concentration range the solvent A obeys Raoult's law, $p_{\mathrm{A}} = p_{\mathrm{A}}^*x_{\mathrm{A}}$, then the left side equals 1 and $\mathrm{d}\ln p_{\mathrm{B}} = \mathrm{d}\ln x_{\mathrm{B}}$; integration gives $p_{\mathrm{B}} = k_{x,\mathrm{B}}x_{\mathrm{B}}$: over the same concentration range the solute must obey **Henry's law**. This is the thermodynamic proof that the two laws of the ideal dilute solution in [6.3.5](/6.3.5) are mutually consistent.
3. From this constraint on the partial pressures one obtains the relation between the total pressure and the compositions of the two phases:

**Theorem 9.2.2 (Konovalov's Rules)** At constant temperature, the total vapor pressure of a binary system and the vapor composition satisfy

$$
\left(\frac{\partial\ln p}{\partial y_{\mathrm{A}}}\right)_T = \frac{y_{\mathrm{A}} - x_{\mathrm{A}}}{y_{\mathrm{A}}(1 - y_{\mathrm{A}})}.
\tag{9.3}
$$
Hence (1) first rule: at a maximum or minimum of the total pressure in the $p$–$x$ diagram (at constant pressure, a minimum or maximum in the $T$–$x$ diagram), $y_{\mathrm{A}} = x_{\mathrm{A}}$, that is, the two phases have the same composition; (2) second rule: if adding A to the vapor raises the total vapor pressure (at constant pressure, lowers the boiling point), then the vapor contains more A than the liquid, $y_{\mathrm{A}} > x_{\mathrm{A}}$; and conversely.

**Proof** Substitute $p_{\mathrm{A}} = y_{\mathrm{A}}p$ and $p_{\mathrm{B}} = y_{\mathrm{B}}p$ into Eq. (9.2):

$$
(x_{\mathrm{A}} + x_{\mathrm{B}})\,\mathrm{d}\ln p + x_{\mathrm{A}}\frac{\mathrm{d}y_{\mathrm{A}}}{y_{\mathrm{A}}} + x_{\mathrm{B}}\frac{\mathrm{d}y_{\mathrm{B}}}{y_{\mathrm{B}}} = 0 .
$$
Using $x_{\mathrm{A}} + x_{\mathrm{B}} = 1$ and $\mathrm{d}y_{\mathrm{B}} = -\mathrm{d}y_{\mathrm{A}}$,

$$
\mathrm{d}\ln p = -\left(\frac{x_{\mathrm{A}}}{y_{\mathrm{A}}} - \frac{x_{\mathrm{B}}}{y_{\mathrm{B}}}\right)\mathrm{d}y_{\mathrm{A}} = \frac{x_{\mathrm{B}}y_{\mathrm{A}} - x_{\mathrm{A}}y_{\mathrm{B}}}{y_{\mathrm{A}}y_{\mathrm{B}}}\,\mathrm{d}y_{\mathrm{A}},
$$
and $x_{\mathrm{B}}y_{\mathrm{A}} - x_{\mathrm{A}}y_{\mathrm{B}} = (1 - x_{\mathrm{A}})y_{\mathrm{A}} - x_{\mathrm{A}}(1 - y_{\mathrm{A}}) = y_{\mathrm{A}} - x_{\mathrm{A}}$, which gives Eq. (9.3). For $0 < y_{\mathrm{A}} < 1$ the denominator is positive, so the derivative vanishes if and only if $y_{\mathrm{A}} = x_{\mathrm{A}}$, and its sign is that of $y_{\mathrm{A}} - x_{\mathrm{A}}$. $\square$

The second rule is the general form of the statement in Section 9.1.2 that the more volatile component is enriched in the vapor: it holds for every nonideal system and does not require Raoult's law.

## 9.3. Liquid–Liquid Equilibrium

### 9.3.1. Partial Miscibility and the Critical Solution Temperature

If the positive deviations of two liquids are large enough, they cannot mix completely over a certain composition range. For example, add isobutanol dropwise to water at $20\,{}^\circ\mathrm{C}$ and $p^\circ$: when the mass fraction of isobutanol is below 8.5% a homogeneous solution results; above 8.5% two layers form, one a solution of isobutanol in water (8.5%) and the other a solution of water in isobutanol (83.6%), and further addition of isobutanol only changes the relative amounts of the two layers; above 83.6% the system is again a single phase. With the two layers coexisting, $C = 2$ and $P = 2$, so at constant temperature and pressure $F^* = 0$ and the compositions of both layers are fixed.

**Definition 9.3.1 (Conjugate Solutions)** When two liquids are partially miscible, the two coexisting liquid layers of different composition are called **conjugate solutions**. As the temperature is raised (or lowered), the compositions of the two layers approach each other and merge into one phase at a certain temperature, which is called the **critical solution temperature** (consolute temperature).

In the solubility diagram ($T$–$x$ diagram) at constant pressure, the two solubility curves enclose a "cap-shaped" two-phase region whose top is the consolute point. The critical solution temperature reflects how strongly the two liquids dissolve in each other. Real systems fall into three types, plus the case of no critical temperature:

| Type | Examples | Critical solution temperature |
|---|---|---|
| Upper critical solution temperature: mutual solubility increases on heating | Water–aniline; water–phenol; water–isobutanol | Water–aniline about $167\,{}^\circ\mathrm{C}$, water–phenol about $66\,{}^\circ\mathrm{C}$ |
| Lower critical solution temperature: mutual solubility increases on cooling | Water–triethylamine | About $18.5\,{}^\circ\mathrm{C}$ |
| Both an upper and a lower critical solution temperature (a closed-loop two-phase region) | Water–nicotine | About $61\,{}^\circ\mathrm{C}$ and $210\,{}^\circ\mathrm{C}$ |
| No critical solution temperature in the liquid range | Water–diethyl ether | — |

A lower critical solution temperature usually occurs in systems with hydrogen bonds between the two kinds of molecules: at low temperature the A–B hydrogen bonds make mixing exothermic ($H^{\mathrm{E}} < 0$) and the liquids mix; but the hydrogen bonds also restrict the relative orientation of the molecules, so the entropy of mixing is smaller than the ideal value ($S^{\mathrm{E}} < 0$), and on heating the $-TS^{\mathrm{E}}$ term dominates and phase separation sets in again.

### 9.3.2. Phase Separation in Regular Solutions

Partial miscibility can be understood quantitatively with the regular solution model of [6.3.6](/6.3.6). Let the **excess Gibbs energy** be $G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$ ($W$ independent of temperature, $S^{\mathrm{E}} = 0$). Then

$$
\frac{\Delta_{\mathrm{mix}}G_{\mathrm{m}}}{RT} = x\ln x + (1 - x)\ln(1 - x) + \frac{W}{RT}\,x(1 - x), \qquad x = x_{\mathrm{B}} .
$$
At constant temperature and pressure the system is in the state of lowest Gibbs energy. If the curve $\Delta_{\mathrm{mix}}G_{\mathrm{m}}(x)$ has a convex-downward stretch (a segment bulging upward), splitting the homogeneous solution into two phases lowers the Gibbs energy. The compositions of the two phases are given by the two points of tangency of the common tangent: a common tangent means that $\mathrm{d}G/\mathrm{d}x$ and the intercept are the same in the two phases, that is, the **chemical potentials** of A and of B are each equal in the two phases.

The curvature is determined by the second derivative:

$$
\frac{1}{RT}\frac{\partial^2\Delta_{\mathrm{mix}}G_{\mathrm{m}}}{\partial x^2} = \frac{1}{x(1 - x)} - \frac{2W}{RT}.
$$
It has its minimum at $x = 1/2$, so for $W/RT > 2$ a region where the curve bulges upward appears in the middle. The critical solution temperature (here an upper one) is

$$
T_{\mathrm{c}} = \frac{W}{2R}.
$$
For the symmetric model, the compositions of the two phases satisfy $\ln\dfrac{x}{1 - x} = \dfrac{W}{RT}(2x - 1)$, the coexistence curve. The curve $T = 2Wx(1 - x)/R$ on which the second derivative vanishes is called the *spinodal*: between the coexistence curve and the spinodal, a homogeneous solution is stable against small fluctuations and phase separation must proceed by nucleation (metastable); inside the spinodal, any small composition fluctuation grows spontaneously (spinodal decomposition).

![Symmetric regular solution. Left: Gibbs energy of mixing against composition for W/RT = 0, 1.5, 2 and 2.8; for W/RT > 2 the curve has two minima and the common tangent gives the compositions of the two coexisting liquids. Right: coexistence curve and spinodal in reduced temperature T/Tc, with Tc = W/(2R) the upper critical solution temperature; a tie line l1–l2 is shown at T/Tc = 0.8](./plots/regular-solution-miscibility.py)

The same thermodynamics (extended to polymers as Flory–Huggins theory) is used to understand liquid–liquid phase separation of proteins and RNA in cells: proteins containing low-complexity sequences separate from the cytoplasm at certain concentrations and temperatures as protein-rich droplets, forming membraneless organelles (biomolecular condensates) such as the nucleolus and stress granules ([7.3](/7.3)).

### 9.3.3. Completely Immiscible Systems and Steam Distillation

If the mutual solubility of two liquids is so small that it can be neglected, then when they coexist each has the same vapor pressure as when alone, and the total vapor pressure above the liquid,

$$
p = p_{\mathrm{A}}^* + p_{\mathrm{B}}^*,
$$
is independent of the relative amounts of the two liquids and exceeds the vapor pressure of either pure component. The boiling point of the mixture is therefore lower than that of either pure component: as long as both liquids are present, the system boils at the temperature at which $p_{\mathrm{A}}^*(T) + p_{\mathrm{B}}^*(T) = p$. Passing steam into an organic substance that is insoluble in water and has a high boiling point or decomposes near its boiling point makes it distill together with the water below $100\,{}^\circ\mathrm{C}$; this method is called *steam distillation*, and it is used to extract plant essential oils and to purify aniline and nitrobenzene, among others.

In the distillate the ratio of the amounts of the two components equals the ratio of their partial pressures, $n_{\mathrm{B}}/n_{\mathrm{A}} = p_{\mathrm{B}}^*/p_{\mathrm{A}}^*$, so the mass ratio is

$$
\frac{m_{\mathrm{B}}}{m_{\mathrm{A}}} = \frac{p_{\mathrm{B}}^*M_{\mathrm{B}}}{p_{\mathrm{A}}^*M_{\mathrm{A}}}.
$$
Although the vapor pressure of the organic substance is small, its molar mass is much larger than that of water, so each unit mass of water distilled carries over a considerable mass of the organic substance.

**Example 9.3.1** The normal boiling point of bromobenzene is $156\,{}^\circ\mathrm{C}$. A calculation with the Antoine equation shows that at $101.325\,\mathrm{kPa}$ a water–bromobenzene mixture boils at $95.3\,{}^\circ\mathrm{C}$, where $p^*(\ce{H2O}) = 85.4\,\mathrm{kPa}$ and $p^*(\ce{C6H5Br}) = 15.9\,\mathrm{kPa}$. In the distillate

$$
\frac{m(\ce{C6H5Br})}{m(\ce{H2O})} = \frac{15.9 \times 157.0}{85.4 \times 18.02} = 1.62,
$$
so distilling $1\,\mathrm{kg}$ of water carries over $1.6\,\mathrm{kg}$ of bromobenzene. The densities differ greatly, so the distillate separates easily into layers.

## 9.4. Solid–Liquid Equilibrium

A binary system whose components are completely miscible as liquids deposits solids on cooling. Solid–liquid equilibrium is insensitive to pressure, so usually only the $T$–$x$ diagram at $p^\circ$ is drawn, with $F^* = 3 - P$ and at most three coexisting phases. According to the miscibility in the solid state, the basic types are: simple eutectic systems, systems forming stable compounds or unstable compounds, and systems forming solid solutions.

### 9.4.1. Thermal Analysis and Cooling Curves

Phase diagrams of metallic systems are determined by thermal analysis: a sample of known composition is heated until it melts and is then cooled slowly and uniformly at constant pressure, while the temperature is recorded as a function of time.

**Definition 9.4.1 (Cooling Curve)** The temperature–time curve of a sample cooled slowly at constant pressure is called the **cooling curve**.

Without a phase change the sample cools smoothly following Newton's law of cooling. When a solid separates, the heat of solidification released offsets part of the heat loss and the slope of the curve decreases (a break appears); when three phases coexist ($F^* = 0$), the temperature stays constant until one phase disappears and the curve shows a horizontal plateau. The phase diagram can be drawn from the temperatures of the breaks and plateaus on the cooling curves of a series of compositions. Water–salt systems near room temperature are determined by the solubility method: solutions of different concentrations are prepared, and the saturation solubility and the freezing point are measured. Modern methods also include **differential scanning calorimetry** ([6.3.1](/6.3.1)) and high-temperature X-ray diffraction.

### 9.4.2. Simple Eutectic Systems

The simplest phase diagram belongs to a system whose components are completely miscible as liquids, completely immiscible as solids, and form no compound. Take Bi–Cd as an example. Below the liquid region there are two freezing-point curves (liquidus curves), giving the compositions of the liquid in equilibrium with pure Bi(s) and pure Cd(s) respectively; they fall as the other component is added (**freezing-point depression**) and meet at a point E. The horizontal line through E is the three-phase equilibrium line of Bi(s), Cd(s), and a liquid of composition E.

**Definition 9.4.2 (Eutectic Point)** The point E where the two freezing-point curves of a simple eutectic system meet is called the **eutectic point**; at this temperature the two solids and a liquid of fixed composition coexist. When the liquid is cooled to E, the two solids separate simultaneously in the proportion of the composition E, and the resulting mixture of two fine crystals is called the **eutectic mixture**.

At the eutectic point $C = 2$, $P = 3$, and $F^* = 0$: both the temperature and the liquid composition are fixed. The eutectic mixture has the lowest melting point, but it is a mechanical mixture of two phases, not a compound: under the microscope a fine structure of alternating crystals of the two kinds can be seen.

The liquidus curves can be calculated thermodynamically.

**Theorem 9.4.1 (Ideal Solubility Equation)** When pure solid B is in equilibrium with an ideal liquid mixture, the mole fraction of B in the liquid satisfies

$$
\ln x_{\mathrm{B}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}}{R}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{f,B}}^*}\right),
\tag{9.4}
$$
where $T_{\mathrm{f,B}}^*$ and $\Delta_{\mathrm{fus}}H_{\mathrm{m,B}}$ are the melting point and molar enthalpy of fusion of pure B (taken as independent of temperature).

**Proof** At equilibrium $\mu_{\mathrm{B}}^*(\mathrm{s}) = \mu_{\mathrm{B}}(\mathrm{l}) = \mu_{\mathrm{B}}^*(\mathrm{l}) + RT\ln x_{\mathrm{B}}$, so $\ln x_{\mathrm{B}} = -\Delta_{\mathrm{fus}}G_{\mathrm{m,B}}/(RT)$. By the **Gibbs–Helmholtz equation** ([6.3.3](/6.3.3)), $\partial(\Delta_{\mathrm{fus}}G_{\mathrm{m}}/T)/\partial T = -\Delta_{\mathrm{fus}}H_{\mathrm{m}}/T^2$; integrating from $T_{\mathrm{f,B}}^*$ (where $\Delta_{\mathrm{fus}}G_{\mathrm{m}} = 0$) to $T$ gives the result. $\square$

Treating B as the solvent, Eq. (9.4) is the form of the freezing-point depression formula of [6.3.5](/6.3.5) without the dilute-solution approximation; treating B as the solute, it is the solubility of a solid in an ideal solution: it depends only on the melting point and enthalpy of fusion of the solute and not on the nature of the solvent, and a solid with a higher melting point and a larger enthalpy of fusion is less soluble. Applying Eq. (9.4) to each of the two liquidus curves, their intersection satisfies $x_{\mathrm{A}}(T) + x_{\mathrm{B}}(T) = 1$, and the eutectic point can be found with `scipy.optimize.brentq` ([4.4.4](/4.4.4)).

**Example 9.4.1** Bi: $T_{\mathrm{f}}^* = 544.55\,\mathrm{K}$, $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 11.30\,\mathrm{kJ\,mol^{-1}}$; Cd: $T_{\mathrm{f}}^* = 594.22\,\mathrm{K}$, $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.21\,\mathrm{kJ\,mol^{-1}}$. The ideal solubility equation gives a eutectic point of $408\,\mathrm{K}$ at $x(\mathrm{Cd}) = 0.565$ (41% Cd by mass). The measured eutectic point is about $419\,\mathrm{K}$ ($146\,{}^\circ\mathrm{C}$) at about 40% Cd by mass: the composition agrees very well, while the temperature is about $10\,\mathrm{K}$ too low, which indicates that liquid Bi–Cd deviates positively from an ideal solution.

![Bi–Cd simple eutectic system. Left: liquidus curves computed from the ideal solubility equation; they meet at the eutectic point E (408 K in the ideal model, about 419 K measured), and the horizontal line through E is the three-phase line Bi(s) + Cd(s) + liquid E. Right: simulated cooling curves for pure Bi, x(Cd) = 0.20, the eutectic composition, 0.80 and pure Cd: pure metals and the eutectic show only a plateau, the other mixtures show a break at the liquidus followed by the eutectic plateau](./plots/bi-cd-eutectic.py)

Reading the phase diagram from the cooling curves (right panel): pure Bi and pure Cd show a horizontal plateau on cooling to the melting point ($C = 1$, $P = 2$, $F^* = 0$). The sample with $x(\mathrm{Cd}) = 0.20$ begins to deposit Bi(s) at the liquidus temperature ($F^* = 1$, a break), the liquid composition moves along the liquidus toward E, and on reaching the eutectic temperature Cd(s) also separates, with three phases coexisting and a plateau whose length is proportional to the amount of eutectic mixture. A sample of exactly the eutectic composition has no break and only one plateau, and looks like a pure substance.

### 9.4.3. Water–Salt Systems

The phase diagram of a water–salt system has the same shape as that of a simple eutectic system: the left freezing-point curve is the freezing-point line of the salt solution, and the right curve is the solubility curve of the salt (the melting point of the salt is very high, and the curve cannot be extended to it because it is limited by the boiling point of water). For example, the eutectic point of $\ce{(NH4)2SO4}$–$\ce{H2O}$ is $254.9\,\mathrm{K}$ ($-18.3\,{}^\circ\mathrm{C}$) at a salt mass fraction of 39.8%. The diagram has two uses:

- Preparing freezing mixtures: when ice and salt are mixed, the system tends toward the eutectic point as long as both solids are present, so an ice–salt bath stably maintains the eutectic temperature.
- Designing crystallization processes: an unsaturated solution is cooled below the solubility curve to deposit pure salt, and not below the eutectic point (otherwise ice and salt separate together); a solution more dilute than the eutectic composition deposits ice first on cooling and must first be concentrated by evaporation.

De-icing of roads in winter is also based on the water–salt phase diagram. $\ce{NaCl}$–$\ce{H2O}$ actually forms the unstable hydrate $\ce{NaCl.2H2O}$ (which decomposes above $0.1\,{}^\circ\mathrm{C}$, Section 9.4.5), with a eutectic point of $-21.2\,{}^\circ\mathrm{C}$ (23.3% $\ce{NaCl}$ by mass, the solid phases being ice and $\ce{NaCl.2H2O}$); the eutectic point of $\ce{CaCl2}$–$\ce{H2O}$ is as low as about $-50\,{}^\circ\mathrm{C}$. After salt is spread, as long as the air temperature is above the eutectic point, ice in contact with salt melts to brine until the brine is diluted to the freezing-point line at that temperature; in practice the rate of melting also depends on kinetics, and $\ce{NaCl}$ is already very ineffective below about $-10\,{}^\circ\mathrm{C}$. Chloride salts corrode vehicles and reinforcing steel and harm roadside plants and soil, so there are alternative de-icers such as calcium magnesium acetate and potassium acetate, as well as "de-icing" pavements with slow-release de-icing material mixed into the asphalt.

### 9.4.4. Systems Forming Stable Compounds

Two solids may form one or several compounds. If a compound does not decompose on heating until it melts, so that the liquid and solid have the same composition on melting, it is called a stable compound.

**Definition 9.4.3 (Congruent Melting Point)** The melting point of a compound that melts to a liquid of the same composition is called its **congruent melting point**, and such a compound is called a compound with a congruent melting point (a stable compound).

In the phase diagram a stable compound C is a vertical line, and the liquidus has a maximum at the composition of C (the congruent melting point D). The whole diagram can be regarded as the simple eutectic diagrams A–C and C–B placed side by side, with two eutectic points. If the compound partly dissociates in the liquid, the maximum is rounded; the less dissociation, the sharper the maximum. Phenol–aniline (forming a 1∶1 compound) and $\ce{CuCl}$–$\ce{FeCl3}$ belong to this type; $\ce{H2O}$–$\ce{H2SO4}$ forms three stable hydrates, $\ce{H2SO4.H2O}$, $\ce{H2SO4.2H2O}$, and $\ce{H2SO4.4H2O}$, and its phase diagram is composed of four simple eutectic diagrams.

![Schematic solid–liquid phase diagrams built from ideal-solubility liquidus curves. (a) A compound C = AB with a congruent melting point D: the diagram is two simple eutectic diagrams side by side. (b) A compound with an incongruent melting point: C decomposes at the peritectic temperature D into solid A and liquid M; E is the eutectic. (c) Complete solid solubility, computed for Cu–Ni as ideal solid and liquid solutions (a lens between liquidus and solidus). (d) Partial solid solubility with a eutectic: two terminal solid solutions α and β separated by solvus lines](./plots/solid-liquid-types.py)

The transport of concentrated sulfuric acid in winter shows the use of reading phase diagrams: sulfuric acid of 98% by mass lies on the liquidus of $\ce{H2SO4}$ with a freezing point above $0\,{}^\circ\mathrm{C}$, so it freezes in pipes in winter; acid of about 93% by mass is close to the eutectic point between $\ce{H2SO4}$ and $\ce{H2SO4.H2O}$ with a freezing point below $-25\,{}^\circ\mathrm{C}$, so sulfuric acid transported in winter is usually adjusted to about 93%.

**Example 9.4.2** In a system forming a stable compound C, two solutions M and N lie at the same temperature on the liquidus curves on the two sides of the compound, and both are in equilibrium with C(s). If they are poured together, will conjugate solutions form?

**Solution** No. Conjugate solutions require $\mu_{\mathrm{A}}(\mathrm{M}) = \mu_{\mathrm{A}}(\mathrm{N})$ and $\mu_{\mathrm{B}}(\mathrm{M}) = \mu_{\mathrm{B}}(\mathrm{N})$, whereas M and N satisfy only $\mu_{\mathrm{A}}(\mathrm{M}) + \mu_{\mathrm{B}}(\mathrm{M}) = \mu_{\mathrm{C}} = \mu_{\mathrm{A}}(\mathrm{N}) + \mu_{\mathrm{B}}(\mathrm{N})$ (each is in chemical equilibrium with C). M and N are not in equilibrium with each other. After mixing, the system point lies between M and N, in the two-phase region $\mathrm{l} + \mathrm{C(s)}$ at that temperature, and the result is that solid C separates, leaving one liquid phase.

### 9.4.5. Systems Forming Unstable Compounds

If a compound decomposes before melting into a solid and a liquid of different composition, it is called an unstable compound. For example, the $\ce{CaF2}$–$\ce{CaCl2}$ system forms $\ce{CaF2.CaCl2}$, which decomposes on heating to about $737\,{}^\circ\mathrm{C}$:

$$
\ce{CaF2.CaCl2(s) -> CaF2(s) + melt}\;(x(\ce{CaCl2}) = 0.6).
$$

**Definition 9.4.4 (Incongruent Melting Point)** The temperature at which a compound decomposes into a solid and a liquid of different composition is called its **incongruent melting point** (peritectic temperature), and such a compound is called an unstable compound; this decomposition and its reverse (solid A reacting with liquid M to form compound C) is called a **peritectic reaction**.

At the incongruent melting point, $\ce{A(s)}$, $\ce{C(s)}$, and the liquid M coexist with $F^* = 0$, and in the phase diagram this is a horizontal line D–M, but the liquid point M lies at one end of this line instead of in the middle as at a eutectic point. It can be understood as the "hidden" congruent melting point of the compound being covered by the liquidus of A: the melting point of A is so high that its liquidus intersects that of the compound before the compound melts.

The phase diagram can be used to design the preparation of compound C: if the melt composition lies between M and E, C is the first solid to separate on cooling, and the solid obtained before E is reached is pure C. If the melt composition lies to the left of M, A(s) separates first on cooling, and at the peritectic temperature A(s) reacts with the melt to form C; but the C formed coats the A crystals and prevents the melt from continuing to contact A, so the peritectic reaction cannot go to completion (the peritectic phenomenon), and the product is a solid with a core of A coated with C. Thus when solid phases take part, the equilibrium state given by the phase diagram may not be reached in a finite time.

### 9.4.6. Solid Solutions

Two components that dissolve in each other in the solid state to form a single solid phase give a **solid solution** ([6.1.4](/6.1.4)). By structure there are two kinds: in a substitutional solid solution the two kinds of particles have similar sizes (atomic radii generally differing by no more than 15%, the Hume-Rothery rule) and replace each other in the lattice, as in Cu–Ni and Au–Ag; in an interstitial solid solution the solute particles are much smaller (a radius ratio to the solvent atoms below about 0.59) and fit into the interstices of the solvent lattice, as C dissolved in Fe or Ni. Pure metals generally have low strength and hardness and are very ductile; forming a solid solution markedly increases strength and hardness (solid-solution strengthening). Bronze (Sn in Cu), brass (Zn in Cu), and silver coinage (Cu in Ag) are all solid-solution **alloys**.

When both the liquid and the solid are completely miscible, the shape of the phase diagram is the same as that of ideal or nonideal gas–liquid diagrams: a liquidus and a solidus enclose a "lens"-shaped two-phase region (Cu–Ni, Au–Ag), or a minimum-melting point appears (Au–Cu). If the liquid and the solid solution are both ideal solutions, writing $\mu_i^*(\mathrm{s}) + RT\ln x_i^{\mathrm{s}} = \mu_i^*(\mathrm{l}) + RT\ln x_i^{\mathrm{l}}$ for each component gives

$$
\frac{x_i^{\mathrm{l}}}{x_i^{\mathrm{s}}} = \exp\left[-\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m},i}}{R}\left(\frac{1}{T} - \frac{1}{T_{\mathrm{f},i}^*}\right)\right], \qquad i = \mathrm{A}, \mathrm{B},
$$
and together with $\sum_i x_i^{\mathrm{l}} = \sum_i x_i^{\mathrm{s}} = 1$ the compositions of the two phases at each temperature can be solved for (panel (c) of the figure above).

On cooling, the first solid solution to separate is rich in the high-melting component, and as the temperature falls the composition of the equilibrium solid changes along the solidus. But atoms diffuse slowly in solids, and the crystals already formed have no time to adjust their composition; as a result the composition within a crystal is nonuniform, with the first-formed core rich in the high-melting component. Because the solid–liquid interface is unstable, the crystals often grow dendritically; this is called *coring* (dendritic segregation). Holding the alloy for some time at a temperature close to its melting point so that the composition becomes uniform by diffusion is annealing; cooling the high-temperature solid rapidly so that the high-temperature structure is retained at low temperature is quenching.

When the components are completely miscible as liquids and partially miscible as solids, there is a single-phase solid-solution region on each side ($\alpha$: B dissolved in A, $\beta$: A dissolved in B), and in the middle a cap-shaped two-phase region ($\alpha + \beta$) similar to liquid–liquid partial miscibility. There are two kinds of such diagrams:

- Eutectic type (the melting points of the components differ little, as in Ag–Cu): on the three-phase line $\mathrm{l(E)} \rightleftharpoons \alpha + \beta$ (panel (d) above); the eutectic point of Ag–Cu is $779\,{}^\circ\mathrm{C}$.
- Peritectic type (the melting points of the components differ greatly, as in Hg–Cd): on the three-phase line $\alpha \rightleftharpoons \mathrm{l} + \beta$ or $\mathrm{l} + \alpha \rightleftharpoons \beta$, and the temperature of the three-phase line is the peritectic temperature.

The negative electrode of the Weston **standard cell** ([6.3.13](/6.3.13)) is a cadmium amalgam containing 5%–14% Cd by mass, which makes use of the Hg–Cd phase diagram: at room temperature this composition range lies in the two-phase region where liquid amalgam and a solid solution coexist, so at constant temperature and pressure $F^* = 0$ and the compositions of both phases are fixed. The activity of cadmium, and with it the electrode potential, is therefore fixed independently of the overall composition of the amalgam; even if some cadmium in the amalgam is consumed during use, the potential does not change.

### 9.4.7. Zone Refining

Solid-solution phase diagrams also provide a method of preparing ultrapure materials. Suppose an impurity B lowers the melting point of the host A. On the A side the solid in equilibrium with the liquid contains less impurity than the liquid: $k = x_{\mathrm{B}}^{\mathrm{s}}/x_{\mathrm{B}}^{\mathrm{l}} < 1$ (the segregation coefficient). A narrow heater ring melts a rod of material locally, and the molten zone is moved slowly along the rod: the front of the molten zone continually melts in fresh material and its rear continually resolidifies, the solid that freezes out is purer than the melt, and the impurity is swept with the molten zone to one end of the rod. This method is called *zone refining*; its principle is similar to fractional distillation, and repeating the pass many times is equivalent to many theoretical plates. In 1952 Pfann used it to purify germanium to an impurity level of the order of $10^{-10}$, which helped launch the semiconductor industry; today it is used to prepare metals and semiconductor materials of purity above 99.999999% ("eight nines") and to purify organic compounds.

## 9.5. Reading Complex Phase Diagrams

### 9.5.1. The Seven Basic Types

According to the miscibility of the high-temperature and low-temperature phases, binary $T$–$x$ phase diagrams can be classified into seven basic shapes.

| No. | Miscibility of the high- and low-temperature phases | Examples |
|---|---|---|
| ① | Both completely miscible, low-temperature phase ideal or nearly ideal | Gas–liquid diagram of an ideal liquid mixture; completely miscible solid solution (Cu–Ni) |
| ② | Both completely miscible, low-temperature phase with large deviations | Azeotrope (ethanol–water); solid solution with a minimum melting point (Au–Cu) |
| ③ | Partially miscible at low temperature, only the cap region is seen | Partially miscible liquid pair (water–aniline) or solid pair |
| ④ | High-temperature phase completely miscible, low-temperature phase completely immiscible | Simple eutectic system (Bi–Cd); gas–liquid diagram of a completely immiscible liquid pair (benzene–water) |
| ⑤ | Formation of a stable compound | Phenol–aniline, $\ce{H2O}$–$\ce{H2SO4}$ |
| ⑥ | Formation of an unstable compound | $\ce{CaF2}$–$\ce{CaCl2}$ |
| ⑦ | High-temperature phase completely miscible, low-temperature phase partially miscible | Partially miscible solid solution (Ag–Cu, Hg–Cd); gas–liquid diagram of partially miscible liquids |

These basic diagrams evolve continuously into one another: in ⑦, letting the mutual solubility decrease to zero gives ④, and increasing it to complete miscibility gives ②; in ⑤, as the melting point of component A is gradually raised, the congruent melting point of the compound is covered by the liquidus of A and becomes an incongruent melting point (⑤→⑥); a solid solution of ② that separates into two phases at low temperature is a combination of ② and ③, giving ⑦.

### 9.5.2. Structural Rules of Phase Diagrams

Complex phase diagrams (such as Mg–Sn and $\ce{MgO}$–$\ce{SiO2}$) are all assembled from basic diagrams. The following rules are used in reading them:

1. A vertical line represents a pure substance or a compound (a compound has a fixed composition).
2. A horizontal line represents a three-phase line ($F^* = 0$): the three phase points on the line are generally the two endpoints and the point where the line meets another curve, and the three phases are the phases that appear in the regions adjacent above and below this line.
3. Curves are all two-phase equilibrium lines, and the points on a curve are phase points.
4. The two phases coexisting in a two-phase region are determined by the two single-phase regions (or vertical lines representing pure substances) adjacent to it on the left and right, and obey the lever rule.
5. Two regions adjacent in the vertical direction generally differ in the number of phases by one (crossing a phase boundary makes only one phase appear or disappear).

To read a diagram, first find all single-phase regions (liquid region, solid-solution regions, and the vertical lines of pure substances and compounds), then use rule 4 to determine which two phases make up each two-phase region, and finally find the three phase points on the three-phase lines. When using the diagram, walk down the vertical line of the system point from the top, and you can say what separates at each step of cooling and what shape the cooling curve has.

### 9.5.3. The Fe–C Phase Diagram

The heat treatment of steel and iron is based on the Fe–C phase diagram, which is a combination of several basic diagrams. The usual diagram is the Fe–$\ce{Fe3C}$ (cementite) metastable diagram ($\ce{Fe3C}$ is thermodynamically less stable than graphite but decomposes extremely slowly); the abscissa is the mass fraction of C, running to the composition of cementite, 6.69%, at the right end. The single-phase regions are the liquid, $\delta$ ferrite (body-centered cubic), austenite $\gamma$ (face-centered cubic), and ferrite $\alpha$ (body-centered cubic), all of which are interstitial solid solutions of C in Fe, and the compound $\ce{Fe3C}$. Current values of the characteristic points:

| Characteristic point | Temperature | Mass fraction of C | Reaction |
|---|---|---|---|
| Peritectic point | $1495\,{}^\circ\mathrm{C}$ | 0.17% | $\delta + \mathrm{l} \to \gamma$ |
| Eutectic point | $1148\,{}^\circ\mathrm{C}$ | 4.30% | $\mathrm{l} \to \gamma + \ce{Fe3C}$ (ledeburite) |
| Maximum carbon solubility of austenite | $1148\,{}^\circ\mathrm{C}$ | 2.11% | Boundary between steel ($< 2.11\%$) and cast iron ($> 2.11\%$) |
| Eutectoid point | $727\,{}^\circ\mathrm{C}$ | 0.77% | $\gamma \to \alpha + \ce{Fe3C}$ (pearlite) |
| Maximum carbon solubility of ferrite | $727\,{}^\circ\mathrm{C}$ | 0.0218% | |

The eutectoid reaction has the same form as the eutectic reaction, except that none of the three phases is a liquid: one solid phase decomposes into two solid phases, controlled by diffusion in the solid, giving a lamellar structure of alternating layers of the two phases. At $770\,{}^\circ\mathrm{C}$ there is also the magnetic transition of ferrite, the **Curie temperature** of iron ([5.3.8](/5.3.8#sec-8.5.4)); it is a continuous phase transition ([6.3.8](/6.3.8)) and forms no new phase region in the diagram.

## 9.6. Ternary Systems

### 9.6.1. Equilateral Triangular Coordinates

For a ternary system $C = 3$ and $F = 5 - P$: at most five phases coexist, and for one phase $F = 4$. At constant temperature or constant pressure, $F^* = 4 - P$ and the phase diagram must be a three-dimensional triangular prism (the base representing composition and the height temperature or pressure); at constant temperature and pressure, $F^* = 3 - P$, a single-phase region has two composition variables, and the diagram can be drawn in a plane.

The composition of a ternary system is usually represented in an equilateral triangle (the Gibbs triangle): the three vertices represent pure A, B, and C, the three sides represent the three binary systems, and points inside the triangle represent ternary systems. Take the height of the triangle as 1. By Viviani's theorem the sum of the distances from any point inside the triangle to the three sides equals 1, so the distances from the point to the sides BC, CA, and AB can represent $x_{\mathrm{A}}$, $x_{\mathrm{B}}$, and $x_{\mathrm{C}}$ (or mass fractions). In practice, draw through the point lines parallel to the three sides, and their intersections with the sides give the contents of the three components. Triangular coordinates have the following properties:

1. On a line parallel to one side, the content of the component represented by the opposite vertex is constant.
2. On a line through one vertex, the ratio of the contents of the other two components is constant; when pure component is added to (or removed from) the system, the system point moves along the line joining the vertex of that component and the original system point.
3. When two systems are mixed, the new system point lies on the line joining the two points, at a position given by the lever rule; when three systems are mixed, the new system point is at the centroid (weighted by amount of substance) of the triangle formed by the three points.

![Equilateral triangular coordinates. Left: reading the composition of point O (x_A = 0.2, x_B = 0.3, x_C = 0.5) with lines parallel to the three sides. Right: a partially miscible three-liquid system A + C with solute B, computed from a ternary regular-solution model; the binodal curve encloses the two-liquid region, the tie lines slope upward to the right because B prefers the C-rich phase, and they shrink to the plait point](./plots/ternary-extraction.py)

### 9.6.2. Ternary Liquid Systems with Partial Miscibility, and Extraction

The most common ternary phase diagram involves a pair of partially miscible liquids A and C (such as water and chloroform) plus a solute B (such as acetic acid) that is completely miscible with both. On the A–C side the two liquids separate into layers only over a middle composition range; as B is added the mutual solubility of the two layers gradually increases, and the two-phase region shrinks in the triangle to a region enclosed by the solubility curve (binodal curve). Each system point in the two-phase region separates into two conjugate liquid layers given by the two ends of a tie line, and the amounts of the two layers follow from the lever rule. The tie lines become shorter toward the top and finally shrink to a point, called the *plait point*, at which the two liquid layers have the same composition, corresponding to the consolute point of a binary system. In the two-phase region $P = 2$ and at constant temperature and pressure $F^* = 1$: once the content of B in one layer is given, the compositions of both layers are fixed, which is the phase-rule statement of the **Nernst distribution law** ([6.3.6](/6.3.6)). That the tie lines are not parallel to the side AC shows that the solute has different concentrations in the two layers; the tilt points toward the layer richer in B, and the slope reflects the magnitude of the **partition coefficient**.

**Extraction** ([6.3.6](/6.3.6)) makes use of such diagrams: the extractant C is added to a solution of B in A (the feed), the system point moves along the line from the feed point to the vertex C into the two-phase region, and separates into a C-rich extract phase and an A-rich raffinate phase; distilling the C off from the extract phase and recovering it gives concentrated B. The phase diagram determines the amount of extractant needed (the system point must enter the two-phase region), the compositions and amounts of the two phases after each extraction stage, and the number of stages needed for multistage extraction. The distribution law of [6.3.6](/6.3.6) already gives the result of such calculations for dilute solutions; the triangular diagram applies when the solute concentration is large and the mutual solubility of the two solvents cannot be neglected. Two-salt–water systems (separating two salts by the dependence of salt solubility on temperature and on the second salt) are also analyzed with triangular diagrams and are not treated further here.

## Summary

| Topic | Key points |
|---|---|
| Phase rule | Binary $F = 4 - P$, at constant pressure or temperature $F^* = 3 - P$; ternary at constant $T$ and $p$, $F^* = 3 - P$ |
| Ideal gas–liquid equilibrium | $p = p_{\mathrm{A}}^* + (p_{\mathrm{B}}^* - p_{\mathrm{A}}^*)x_{\mathrm{B}}$; the more volatile component is enriched in the vapor |
| Lever rule | $n_{\mathrm{l}}(X_{\mathrm{B}} - x_{\mathrm{B}}) = n_{\mathrm{g}}(y_{\mathrm{B}} - X_{\mathrm{B}})$, conservation of mass, valid in any two-phase region |
| Nonideal gas–liquid equilibrium | Large deviations give a minimum or maximum azeotropic point; azeotrope $x = y$, not completely separable by ordinary fractional distillation |
| Duhem–Margules and Konovalov | $x_{\mathrm{A}}\,\mathrm{d}\ln p_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln p_{\mathrm{B}} = 0$; at an extremum $x = y$; when adding a component raises the total pressure, that component is enriched in the vapor |
| Liquid–liquid equilibrium | Conjugate solutions, critical solution temperature; regular solution $T_{\mathrm{c}} = W/(2R)$; immiscible systems $p = p_{\mathrm{A}}^* + p_{\mathrm{B}}^*$, steam distillation |
| Solid–liquid equilibrium | Cooling curves; eutectic point (three phases, $F^* = 0$); ideal solubility equation; congruent and incongruent melting points; solid solutions, coring, zone refining |
| Rules for reading diagrams | Vertical lines are pure substances or compounds, horizontal lines are three-phase lines, curves are two-phase lines, adjacent regions differ by one phase |
| Ternary systems | Gibbs triangle; binodal curve, tie lines, plait point; extraction |
