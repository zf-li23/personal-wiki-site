---
title: Redox Titrations
source_hash: 2001119504d6
---

Redox titrations are based on electron-transfer reactions. They can be used to determine oxidizing or reducing substances directly (iron, copper, hydrogen peroxide, vitamin C, glucose, organic pollutants in water), and also, through a quantitative chemical conversion, substances that are not themselves redox active (calcium via calcium oxalate, magnesium via 8-hydroxyquinoline). [6.1.11](/6.1.11) introduced the **electrode potential** and the **Nernst equation**, and [6.1.12](/6.1.12#sec-12.1) used standard electrode potentials to decide the direction and extent of reactions. In real titration solutions, however, the ionic strength is high and side reactions (precipitation, complex formation, protonation) are present, so standard potentials often lead to wrong conclusions: on the basis of standard potentials $\ce{Cu^2+}$ cannot oxidize $\ce{I-}$, yet the reaction proceeds quantitatively. This chapter applies the method of side-reaction coefficients and conditional constants of [6.4.3](/6.4.3) to electron-transfer reactions. We first introduce the formal potential (Section 5.1) and the conditional equilibrium constant, and discuss the completeness and rate of the reaction (5.2); we then calculate titration curves and choose indicators (5.3); and finally we describe the pretreatment before titration (5.4) and the permanganate, dichromate, and iodine methods (5.5). The chapter is also a direct prerequisite of the potentiometric methods of [6.4.6](/6.4.6): potentiometric titration ([6.4.6](/6.4.6#sec-6.4.5)) measures the titration curves of this chapter with an indicator electrode.

All potentials in this chapter are reduction potentials relative to the standard hydrogen electrode. Standard potentials are taken from the CRC Handbook ($25\,^\circ\mathrm{C}$) and agree with the table in [6.1.11](/6.1.11#sec-11.4.3). The symbol $z$ is the number of electrons transferred in the half-reaction, and $\frac{RT\ln10}{F} = 0.0592\,\mathrm{V}$ at $25\,^\circ\mathrm{C}$. The end-point error is written $E_{\mathrm{t}}$ and is distinguished from the electrode potential $E$ by its subscript.

## 5.1. Formal Potential

### 5.1.1. Characteristics of Redox Titrations

**Definition 5.1.1 (Redox Titration)** A titrimetric method based on an oxidation–reduction reaction is called a **redox titration**.

Compared with acid–base and complexation reactions, the mechanisms of redox reactions are complicated. Many proceed in several steps, some have very large equilibrium constants but are very slow, and some are accompanied by side reactions and have no definite stoichiometry. Whether a redox reaction can be used for titration therefore depends not only on the equilibrium constant but also on the rate, the mechanism, and the reaction conditions (acidity, temperature, catalyst).

### 5.1.2. Formal Potential

The electrode potential of a reversible couple $\mathrm{Ox} + z\ce{e-} \ce{<=>} \mathrm{Red}$ is given by the **Nernst equation** ([6.1.11](/6.1.11#sec-11.5.1)):

$$
E = E^\circ + \frac{RT}{zF}\ln\frac{a_{\mathrm{Ox}}}{a_{\mathrm{Red}}}.
$$
(Only for a reversible couple, one whose electrode reaction is fast enough to establish equilibrium quickly, does the measured potential obey the Nernst equation. The measured potentials of irreversible couples such as $\ce{MnO4-}/\ce{Mn^2+}$, $\ce{Cr2O7^2-}/\ce{Cr^3+}$, and $\ce{S4O6^2-}/\ce{S2O3^2-}$ deviate from the calculated values, but the calculation can still be used to judge the equilibrium.)

In practice what is known are the analytical concentrations $c_{\mathrm{Ox}}$ and $c_{\mathrm{Red}}$ of the oxidized and reduced forms, not their activities. Two relations lie in between. The ionic strength makes the **activity** differ from the concentration, $a = \gamma[\mathrm{Ox}]$, and side reactions make the free concentration of Ox only a fraction of its total concentration, $[\mathrm{Ox}] = c_{\mathrm{Ox}}/\alpha_{\mathrm{Ox}}$ (the **side-reaction coefficient**, [6.4.3](/6.4.3#sec-3.2.1)). Substituting into the Nernst equation gives

$$
E = E^\circ + \frac{RT}{zF}\ln\frac{\gamma_{\mathrm{Ox}}\alpha_{\mathrm{Red}}}{\gamma_{\mathrm{Red}}\alpha_{\mathrm{Ox}}} + \frac{RT}{zF}\ln\frac{c_{\mathrm{Ox}}}{c_{\mathrm{Red}}}.
$$
Under given conditions the first two terms are constant.

**Definition 5.1.2 (Formal Potential)** The actual electrode potential of a couple when the analytical concentrations of the oxidized and reduced forms are both $1\,\mathrm{mol\,L^{-1}}$ (or their ratio is 1) in a medium of given composition (fixed ionic strength, acidity, and concentrations of complexing and precipitating agents),

$$
E^{\circ\prime} = E^\circ + \frac{RT}{zF}\ln\frac{\gamma_{\mathrm{Ox}}\alpha_{\mathrm{Red}}}{\gamma_{\mathrm{Red}}\alpha_{\mathrm{Ox}}} \tag{5.1}
$$
is called the **formal potential** of the couple (also called the conditional potential). Then

$$
E = E^{\circ\prime} + \frac{0.0592\,\mathrm{V}}{z}\lg\frac{c_{\mathrm{Ox}}}{c_{\mathrm{Red}}} \qquad (25\,^\circ\mathrm{C}). \tag{5.2}
$$

When $\ce{H+}$ or $\ce{OH-}$ takes part in the half-reaction, its concentration term is also absorbed into $E^{\circ\prime}$. The relation between the formal potential and the standard potential is the same as that between the **conditional stability constant** and the stability constant in [6.4.3](/6.4.3#sec-3.2.4): known side reactions are absorbed into an apparent constant that is constant only under the given conditions but reflects the redox ability of the couple in the actual solution more accurately than the standard potential does. $E^{\circ\prime}$ is generally determined experimentally; when no experimental value exists, one can use a value for similar conditions, or estimate it from $E^\circ$ and the side-reaction coefficients by Eq. (5.1). Common formal potentials ($25\,^\circ\mathrm{C}$) are:

| Couple | $E^\circ/\mathrm{V}$ | Medium | $E^{\circ\prime}/\mathrm{V}$ |
|---|---|---|---|
| $\ce{Ce^4+}/\ce{Ce^3+}$ | — | $1\,\mathrm{mol\,L^{-1}}$ $\ce{HClO4}$ / $\ce{HNO3}$ / $\ce{H2SO4}$ / HCl | 1.70 / 1.61 / 1.44 / 1.28 |
| $\ce{Fe^3+}/\ce{Fe^2+}$ | 0.771 | $1\,\mathrm{mol\,L^{-1}}$ $\ce{HClO4}$ / HCl / $\ce{H2SO4}$; $2\,\mathrm{mol\,L^{-1}}$ $\ce{H3PO4}$ | 0.73 / 0.70 / 0.68; 0.46 |
| $\ce{Cr2O7^2-}/\ce{Cr^3+}$ | 1.36 | $1\,\mathrm{mol\,L^{-1}}$ HCl / $3\,\mathrm{mol\,L^{-1}}$ HCl | 1.00 / 1.08 |
| $\ce{MnO4-}/\ce{Mn^2+}$ | 1.507 | $1\,\mathrm{mol\,L^{-1}}$ $\ce{HClO4}$ | 1.45 |
| $\ce{I3-}/\ce{I-}$ | 0.536 | $0.5\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ | 0.545 |
| $\ce{Sn^4+}/\ce{Sn^2+}$ | 0.151 | $1\,\mathrm{mol\,L^{-1}}$ HCl | 0.14 |

$\ce{Ce^4+}$ is strongly hydrolyzed in water and coordinated by $\ce{SO4^2-}$ and $\ce{Cl-}$, so a "standard potential" has no clear meaning and only formal potentials are used. Its variation of up to 0.4 V with the medium reflects the different strengths with which anions coordinate Ce(IV): $\ce{ClO4-}$ hardly coordinates, whereas $\ce{SO4^2-}$ coordinates strongly.

### 5.1.3. Factors Affecting the Formal Potential

1. Ionic strength. By Eq. (5.1) the ionic strength changes $\gamma_{\mathrm{Ox}}/\gamma_{\mathrm{Red}}$. When the oxidized and reduced forms have different charges, the activity coefficient of the more highly charged form falls faster with ionic strength (Debye–Hückel theory); for example, the formal potential of $\ce{[Fe(CN)6]^3-}/\ce{[Fe(CN)6]^4-}$ rises markedly with ionic strength. In titration solutions, however, the effect of side reactions is generally far larger than that of ionic strength, so the latter is often neglected and only the side-reaction coefficients are included in Eq. (5.1).

2. Precipitation. If the oxidized form forms a precipitate, $\alpha_{\mathrm{Ox}}$ increases and the potential falls; if the reduced form forms a precipitate, the potential rises.

**Example 5.1.1** Decide whether $\ce{Cu^2+}$ can oxidize $\ce{I-}$. $E^\circ(\ce{Cu^2+}/\ce{Cu+}) = 0.153\,\mathrm{V}$, $E^\circ(\ce{I2}/\ce{I-}) = 0.536\,\mathrm{V}$, and $K_{\mathrm{sp}}(\ce{CuI}) = 1.27\times10^{-12}$.

**Solution** From the standard potentials alone, $0.153 < 0.536$, so $\ce{I2}$ should oxidize $\ce{Cu+}$. But the reduced form $\ce{Cu+}$ forms a CuI precipitate with $\ce{I-}$, with $[\ce{Cu+}] = K_{\mathrm{sp}}/[\ce{I-}]$:

$$
E = 0.153 + 0.0592\lg\frac{[\ce{Cu^2+}][\ce{I-}]}{K_{\mathrm{sp}}(\ce{CuI})}.
$$
For $[\ce{Cu^2+}] = [\ce{I-}] = 1\,\mathrm{mol\,L^{-1}}$, $E^{\circ\prime}(\ce{Cu^2+}/\ce{CuI}) = 0.153 + 0.0592\lg(1/1.27\times10^{-12}) = 0.857\,\mathrm{V}$, much higher than 0.536 V. The reaction $\ce{2Cu^2+ + 4I- -> 2CuI v + I2}$ therefore proceeds quantitatively, which is the basis of the iodometric determination of copper (Section 5.5.3). This is also a quantitative example of the statement in [6.1.11](/6.1.11#sec-11.5.4) that precipitation changes the electrode potential.

3. Complex formation. If the complex of the oxidized form is more stable than that of the reduced form, the potential falls; otherwise it rises.

**Example 5.1.2** In the iodometric determination of $\ce{Cu^2+}$, $\ce{Fe^3+}$ in the sample can also oxidize $\ce{I-}$ ($E^\circ = 0.771\,\mathrm{V} > 0.536\,\mathrm{V}$) and make the result too high. $\ce{F-}$ is added to give $[\ce{F-}] = 0.10\,\mathrm{mol\,L^{-1}}$. Find $E^{\circ\prime}(\ce{Fe^3+}/\ce{Fe^2+})$. For $\ce{Fe^3+}$–$\ce{F-}$, $\lg\beta_1, \lg\beta_2, \lg\beta_3 = 5.28, 9.30, 12.06$, and $\ce{Fe^2+}$ hardly coordinates $\ce{F-}$.

**Solution** $\alpha_{\mathrm{Fe(III)}} = 1 + 10^{5.28 - 1} + 10^{9.30 - 2} + 10^{12.06 - 3} = 10^{9.07}$ and $\alpha_{\mathrm{Fe(II)}} \approx 1$. By Eq. (5.1) (neglecting activity coefficients),

$$
E^{\circ\prime} = 0.771 + 0.0592\lg\frac{1}{10^{9.07}} = 0.771 - 0.537 = 0.23\,\mathrm{V} < 0.536\,\mathrm{V},
$$
so $\ce{Fe^3+}$ can no longer oxidize $\ce{I-}$ and the interference is eliminated. $\ce{Fe^3+}$ forms a colorless complex with $\ce{PO4^3-}$ that acts in the same way; in $\ce{H3PO4}$ medium $E^{\circ\prime}(\ce{Fe^3+}/\ce{Fe^2+})$ falls to about 0.46 V, which is important in the dichromate titration of iron (Section 5.3.4).

4. Acidity. When $\ce{H+}$ or $\ce{OH-}$ takes part in the half-reaction, the acidity enters the Nernst equation directly; when the oxidized or reduced form is a weak acid (base), the acidity also changes $\alpha$ through the acid effect.

**Example 5.1.3** For $\ce{H3AsO4 + 2H+ + 2e- <=> HAsO2 + 2H2O}$, $E^\circ = 0.560\,\mathrm{V}$, and for $\ce{I3- + 2e- <=> 3I-}$, $E^\circ = 0.536\,\mathrm{V}$. Discuss how the direction of the reaction $\ce{H3AsO4 + 3I- + 2H+ <=> HAsO2 + I3- + 2H2O}$ depends on pH.

**Solution** The formal potential of the arsenic couple (absorbing $[\ce{H+}]$ and the distribution fractions $\delta$ of the two arsenic weak acids) is

$$
E^{\circ\prime}(\mathrm{As(V)/As(III)}) = 0.560 - 0.0592\,\mathrm{pH} + \frac{0.0592}{2}\lg\frac{\delta_{\ce{H3AsO4}}}{\delta_{\ce{HAsO2}}}.
$$
The $\ce{I3-}/\ce{I-}$ couple is independent of pH (until $\ce{I2}$ begins to disproportionate above pH 9 or so). The two potentials are equal at pH ≈ 0.4. In more strongly acidic solution (for example $4\,\mathrm{mol\,L^{-1}}$ HCl), As(V) oxidizes $\ce{I-}$ to $\ce{I3-}$. At pH 8 (buffered with $\ce{NaHCO3}$), $\ce{H3AsO4}$ is present mainly as $\ce{HAsO4^2-}$, $\delta_{\ce{H3AsO4}} \approx 10^{-6.8}$, $E^{\circ\prime} \approx -0.11\,\mathrm{V}$, the reaction goes completely to the left, and $\ce{I3-}$ oxidizes As(III) quantitatively. This was the principle of standardizing iodine solutions against $\ce{As2O3}$ as a primary standard ($\ce{As2O3}$ is highly toxic and is now seldom used). That the same reaction runs in opposite directions at different pH is evident at a glance from the [potential–pH diagram](/6.1.12#sec-12.3).

![Formal potential of As(V)/As(III) as a function of pH (including the dissociation of H₃AsO₄ and HAsO₂) and the electrode potential of I₃⁻/I⁻: below pH 0.4 As(V) oxidizes I⁻, and at higher pH I₃⁻ oxidizes As(III)](./plots/arsenic-iodine-ph.py)

## 5.2. Completeness and Rate of the Reaction

### 5.2.1. Conditional Equilibrium Constant

Let the titration reaction consist of two couples:

$$
\mathrm{Ox_1} + z_1\ce{e-} \ce{<=>} \mathrm{Red_1}\ (E^{\circ\prime}_1), \qquad \mathrm{Ox_2} + z_2\ce{e-} \ce{<=>} \mathrm{Red_2}\ (E^{\circ\prime}_2),
$$
where $z$ is the least common multiple of $z_1$ and $z_2$, $p_1 = z/z_1$, and $p_2 = z/z_2$. The overall reaction is

$$
p_1\mathrm{Ox_1} + p_2\mathrm{Red_2} \ce{<=>} p_1\mathrm{Red_1} + p_2\mathrm{Ox_2}.
$$
At equilibrium the potentials of the two couples are equal:

$$
E^{\circ\prime}_1 + \frac{0.0592}{z_1}\lg\frac{c_{\mathrm{Ox_1}}}{c_{\mathrm{Red_1}}} = E^{\circ\prime}_2 + \frac{0.0592}{z_2}\lg\frac{c_{\mathrm{Ox_2}}}{c_{\mathrm{Red_2}}}.
$$
Multiplying both sides by $z$ and rearranging gives the following.

**Definition 5.2.1 (Conditional Equilibrium Constant)** The equilibrium constant of a redox reaction expressed in terms of the analytical concentrations of reactants and products under given conditions,

$$
K' = \frac{c_{\mathrm{Red_1}}^{p_1}c_{\mathrm{Ox_2}}^{p_2}}{c_{\mathrm{Ox_1}}^{p_1}c_{\mathrm{Red_2}}^{p_2}}, \qquad \lg K' = \frac{z\,(E^{\circ\prime}_1 - E^{\circ\prime}_2)}{0.0592\,\mathrm{V}} \tag{5.3}
$$
is called the **conditional equilibrium constant** of the reaction.

It has the same form as the formula of [6.1.12](/6.1.12#sec-12.1.2) for the equilibrium constant from standard potentials, with $E^\circ$ replaced by $E^{\circ\prime}$. The larger the difference $\Delta E^{\circ\prime}$ of the formal potentials, the more complete the reaction. For the titration of $\ce{Fe^2+}$ with $\ce{Ce^4+}$ ($1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$), for example, $\lg K' = (1.44 - 0.68)/0.0592 = 12.8$.

### 5.2.2. Condition for a Complete Reaction

A titration requires the reaction to be more than 99.9% complete at the equivalence point: at least 99.9% of $\mathrm{Ox_1}$ is converted to $\mathrm{Red_1}$ and at least 99.9% of $\mathrm{Red_2}$ to $\mathrm{Ox_2}$, that is, $c_{\mathrm{Red_1}}/c_{\mathrm{Ox_1}} \ge 10^3$ and $c_{\mathrm{Ox_2}}/c_{\mathrm{Red_2}} \ge 10^3$. Substituting into Eq. (5.3),

$$
\lg K' \ge 3(p_1 + p_2), \qquad \Delta E^{\circ\prime} \ge \frac{3(p_1 + p_2)\times0.0592\,\mathrm{V}}{z}. \tag{5.4}
$$
- $z_1 = z_2 = 1$ ($p_1 = p_2 = 1$, $z = 1$): $\lg K' \ge 6$, $\Delta E^{\circ\prime} \ge 0.36\,\mathrm{V}$.
- $z_1 = 1$, $z_2 = 2$ (for example $\ce{2Fe^3+ + Sn^2+ -> 2Fe^2+ + Sn^4+}$, $p_1 = 2$, $p_2 = 1$, $z = 2$): $\lg K' \ge 9$, $\Delta E^{\circ\prime} \ge 0.27\,\mathrm{V}$.
- $z_1 = z_2 = 2$ ($p_1 = p_2 = 1$, $z = 2$): $\lg K' \ge 6$, $\Delta E^{\circ\prime} \ge 0.18\,\mathrm{V}$.

Note that $p_1$ and $p_2$ in Eq. (5.4) are the stoichiometric coefficients in the reaction written in lowest terms, not the numbers of electrons. When $z_1$ and $z_2$ are coprime, $p_1 = z_2$ and $p_2 = z_1$, and the criterion can be written $3(z_1 + z_2)$; for $z_1 = z_2 = 2$, however, this would give the incorrect value 12. The common statement that a reaction whose couples differ in formal potential by more than 0.4 V can be used for titration rounds 0.36 V up and leaves a margin for all these electron numbers. A sufficiently large $\Delta E^{\circ\prime}$ shows only that the reaction can go to completion; whether it can be used for titration also depends on its rate and on the absence of side reactions.

### 5.2.3. Factors Affecting the Reaction Rate

Many redox reactions are thermodynamically complete but slow. For example, $\ce{O2 + 4H+ + 4e- <=> 2H2O}$ has $E^\circ = 1.229\,\mathrm{V}$, so $\ce{Sn^2+}$, $\ce{Fe^2+}$, and $\ce{I-}$ in aqueous solution should be oxidized rapidly by dissolved oxygen; in fact their solutions can be kept for some time. The rate depends first on the reactants themselves (intrinsic factors):

- Reactions that only transfer electrons are fast ($\ce{Ce^4+ + Fe^2+}$); reactions that require bonds to be broken and atoms to be transferred are slow ($\ce{MnO4-}$ and $\ce{Cr2O7^2-}$ lose oxygen when reduced, and reduction of $\ce{O2}$ requires breaking the O=O bond).
- For oxoanions, the higher the oxidation number of the element and the more oxygen atoms coordinated, the slower the reaction tends to be.
- Electrostatic repulsion between ions of the same charge slows a reaction.
- The overall rate of a multistep reaction is determined by the slowest step.

External conditions also matter:

1. Reactant concentration: in general the higher the concentration, the faster the reaction. In the standardization of $\ce{Na2S2O3}$ by iodometry, for example, the reaction $\ce{Cr2O7^2- + 6I- + 14H+ -> 2Cr^3+ + 3I2 + 7H2O}$ is slow, so an excess of KI is added, $[\ce{H+}]$ is kept at $0.2$–$0.4\,\mathrm{mol\,L^{-1}}$, and the solution is left in the dark for about 5 min to complete the reaction.
2. Temperature: in general the rate increases by a factor of 2–4 for every 10 K rise in temperature (the **Arrhenius equation**, [6.1.7](/6.1.7)). The reaction of $\ce{KMnO4}$ with $\ce{C2O4^2-}$ is slow at room temperature and requires heating to $75$–$85\,^\circ\mathrm{C}$; above $90\,^\circ\mathrm{C}$, however, oxalic acid partly decomposes and the result is too high. Volatile ($\ce{I2}$) or air-sensitive ($\ce{Fe^2+}$, $\ce{Sn^2+}$) substances cannot be heated.
3. **Catalyst**: a catalyst changes the reaction pathway and lowers the activation energy. For example, $\ce{Ag+}$ catalyzes the oxidation of $\ce{Mn^2+}$ to $\ce{MnO4-}$ by $\ce{S2O8^2-}$ (Section 5.4).

The reaction of $\ce{MnO4-}$ with $\ce{C2O4^2-}$,

$$
\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 ^ + 8H2O}
$$
is catalyzed by the product $\ce{Mn^2+}$: $\ce{Mn^2+}$ and $\ce{MnO4-}$ first form Mn(III), and the complex of Mn(III) with oxalate then decomposes rapidly to $\ce{CO2}$ and $\ce{Mn^2+}$. The phenomenon in which a reaction product itself catalyzes the reaction is called **autocatalysis**. The rate curve of an autocatalytic reaction is S-shaped: at the beginning there is very little $\ce{Mn^2+}$ and the reaction is slow (the first drop of $\ce{KMnO4}$ takes some time to decolorize), the reaction accelerates sharply as $\ce{Mn^2+}$ accumulates, and it finally slows as the reactants are consumed. No $\ce{Mn^2+}$ need be added in the titration; it is enough to titrate slowly at first and speed up after the first few drops have been decolorized. (The positive feedback of an autocatalytic step is also the origin of chemical oscillations, see [6.3.18](/6.3.18#sec-18.3.2).)

### 5.2.4. Induced Reactions

In the titration of $\ce{Fe^2+}$ with $\ce{KMnO4}$ in HCl medium, too much $\ce{KMnO4}$ is consumed and the result is too high, whereas in the absence of $\ce{Fe^2+}$, $\ce{KMnO4}$ reacts extremely slowly with $\ce{Cl-}$ in dilute HCl. The reason is that the reaction of $\ce{MnO4-}$ with $\ce{Fe^2+}$,

$$
\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}
$$
promotes the otherwise very slow reaction $\ce{2MnO4- + 10Cl- + 16H+ -> 2Mn^2+ + 5Cl2 + 8H2O}$.

**Definition 5.2.2 (Induced Reaction)** The phenomenon in which the progress of one redox reaction accelerates another redox reaction that is slow or does not occur under the same conditions is called induction, and the accelerated reaction is called an **induced reaction**.

In this example $\ce{MnO4-}$ is called the actor, $\ce{Fe^2+}$ the inducer, and $\ce{Cl-}$ the acceptor. The mechanism of induction is that unstable intermediate oxidation states produced in the inducing reaction (here Mn(V), Mn(IV), and Mn(III)) oxidize the acceptor. Induction differs from catalysis: a catalyst is unchanged by the reaction, whereas the inducer takes part in the reaction and is consumed. The error can be eliminated by adding a mixed solution of $\ce{MnSO4}$, $\ce{H3PO4}$, and $\ce{H2SO4}$ (the Zimmermann–Reinhardt reagent). The large amount of $\ce{Mn^2+}$ lowers the potential of the Mn(III)/Mn(II) couple so that Mn(III) can no longer oxidize $\ce{Cl-}$, and $\ce{H3PO4}$ stabilizes Mn(III) by complexation and also forms a colorless complex with $\ce{Fe^3+}$, which makes the end point easier to see.

## 5.3. Titration Curves and Indicators

### 5.3.1. Titration Curves

During a redox titration the concentrations of the oxidized and reduced forms of both couples change continuously as titrant is added, and the potential of the solution changes with them. The potential is plotted against the fraction titrated to give the **titration curve**. After each addition of titrant the reaction reaches equilibrium quickly and the potentials of the two couples are equal, so either can be used for the calculation: before the equivalence point the couple of the analyte (whose two forms are both present in large amounts) is used, and after the equivalence point the couple of the titrant. The titration curve can also be measured directly by potentiometric titration ([6.4.6](/6.4.6#sec-6.4.5)).

Take the titration of $20.00\,\mathrm{mL}$ of $0.1000\,\mathrm{mol\,L^{-1}}$ $\ce{Fe^2+}$ ($1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$) with $0.1000\,\mathrm{mol\,L^{-1}}$ $\ce{Ce(SO4)2}$ as an example. The reaction is $\ce{Ce^4+ + Fe^2+ -> Ce^3+ + Fe^3+}$ with $E^{\circ\prime}(\ce{Ce^4+}/\ce{Ce^3+}) = 1.44\,\mathrm{V}$, $E^{\circ\prime}(\ce{Fe^3+}/\ce{Fe^2+}) = 0.68\,\mathrm{V}$, and $\lg K' = 12.8$, so the reaction is very complete.

1. Before the equivalence point: nearly all the added $\ce{Ce^4+}$ is reduced, $c_{\ce{Ce^4+}}$ is extremely small, and the iron couple is used. At fraction titrated $a$, $c_{\ce{Fe^3+}}/c_{\ce{Fe^2+}} = a/(1 - a)$, and

$$
E = 0.68 + 0.0592\lg\frac{c_{\ce{Fe^3+}}}{c_{\ce{Fe^2+}}}.
$$
At 50% titrated, $E = E^{\circ\prime}_{\ce{Fe}} = 0.68\,\mathrm{V}$; at 99.9%, $E = 0.68 + 0.0592\times3 = 0.86\,\mathrm{V}$. Note that the potential depends only on the ratio of concentrations and not on the concentrations themselves or on dilution.

2. At the equivalence point: the potentials of the two couples are equal, $E_{\mathrm{sp}} = 1.44 + 0.0592\lg(c_{\ce{Ce^4+}}/c_{\ce{Ce^3+}}) = 0.68 + 0.0592\lg(c_{\ce{Fe^3+}}/c_{\ce{Fe^2+}})$. Adding the two expressions and using $c_{\ce{Ce^4+}} = c_{\ce{Fe^2+}}$ and $c_{\ce{Ce^3+}} = c_{\ce{Fe^3+}}$ at the equivalence point, the logarithmic terms cancel and $E_{\mathrm{sp}} = (1.44 + 0.68)/2 = 1.06\,\mathrm{V}$.

3. After the equivalence point: nearly all the $\ce{Fe^2+}$ is oxidized and the cerium couple is used. With a 0.1% excess of $\ce{Ce^4+}$, $c_{\ce{Ce^4+}}/c_{\ce{Ce^3+}} = 10^{-3}$ and $E = 1.44 - 0.0592\times3 = 1.26\,\mathrm{V}$; with a 100% excess, $E = E^{\circ\prime}_{\ce{Ce}} = 1.44\,\mathrm{V}$.

| Fraction titrated/% | 9 | 50 | 91 | 99 | 99.9 | 100 | 100.1 | 101 | 110 | 200 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ratio used | $c_{\ce{Fe^3+}}/c_{\ce{Fe^2+}} = 10^{-1}$ | $10^0$ | $10^1$ | $10^2$ | $10^3$ | — | $c_{\ce{Ce^4+}}/c_{\ce{Ce^3+}} = 10^{-3}$ | $10^{-2}$ | $10^{-1}$ | $10^0$ |
| $E/\mathrm{V}$ | 0.62 | 0.68 | 0.74 | 0.80 | 0.86 | 1.06 | 1.26 | 1.32 | 1.38 | 1.44 |

The titration jump (±0.1% around the equivalence point) extends from 0.86 to 1.26 V, that is, from $E^{\circ\prime}_2 + 3\times0.0592/z_2$ to $E^{\circ\prime}_1 - 3\times0.0592/z_1$; the larger $\Delta E^{\circ\prime}$ is, the larger the jump.

![Titration curve of Fe²⁺ with Ce⁴⁺ (1 mol L⁻¹ H₂SO₄), solved point by point from electron conservation and the Nernst equations of the two couples. The jump is 0.86–1.26 V and the equivalence point is 1.06 V; the colored bands are the transition ranges of ferroin and sodium diphenylamine sulfonate](./plots/ce-fe-titration.py)

### 5.3.2. Equivalence-Point Potential and Asymmetric Titrations

In general, for the reaction of Section 5.2.1, multiplying the Nernst equations of the two couples by $z_1$ and $z_2$ and adding gives

$$
(z_1 + z_2)E = z_1E^{\circ\prime}_1 + z_2E^{\circ\prime}_2 + 0.0592\lg\frac{c_{\mathrm{Ox_1}}c_{\mathrm{Ox_2}}}{c_{\mathrm{Red_1}}c_{\mathrm{Red_2}}}.
$$
At the equivalence point $c_{\mathrm{Ox_1}}/c_{\mathrm{Red_2}} = c_{\mathrm{Red_1}}/c_{\mathrm{Ox_2}} = p_1/p_2$, and the logarithmic term vanishes:

$$
E_{\mathrm{sp}} = \frac{z_1E^{\circ\prime}_1 + z_2E^{\circ\prime}_2}{z_1 + z_2}. \tag{5.5}
$$
Equation (5.5) applies only to symmetric couples, those in which the oxidized and reduced forms have equal stoichiometric coefficients in the half-reaction (for example $\ce{Fe^3+}/\ce{Fe^2+}$, $\ce{Ce^4+}/\ce{Ce^3+}$, $\ce{MnO4-}/\ce{Mn^2+}$); when $\ce{H+}$ takes part, $[\ce{H+}]$ must already have been absorbed into $E^{\circ\prime}$. For asymmetric couples such as $\ce{Cr2O7^2-}/\ce{Cr^3+}$ and $\ce{I3-}/\ce{I-}$, whose two sides have unequal coefficients, $E_{\mathrm{sp}}$ also depends on the concentration.

When $z_1 = z_2$, the equivalence point lies exactly in the middle of the jump; when $z_1 \ne z_2$, it is displaced toward the couple with the larger number of electrons. In the titration of $\ce{Fe^2+}$ with $\ce{KMnO4}$ ($z_1 = 5$, $z_2 = 1$, $\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}$), for example, $E_{\mathrm{sp}} = (5E^{\circ\prime}_{\ce{Mn}} + E^{\circ\prime}_{\ce{Fe}})/6$, which lies close to the potential of permanganate. The titration curve is then asymmetric about the equivalence point, and when the end point is located potentiometrically it cannot simply be taken as the midpoint of the jump.

The effect of the medium on the titration curve can be read directly from the formal potentials. The position of the curve before the equivalence point is determined by $E^{\circ\prime}(\ce{Fe^3+}/\ce{Fe^2+})$: in $\ce{H3PO4}$ medium $\ce{Fe^3+}$ forms stable phosphate complexes, $E^{\circ\prime}$ falls to 0.46 V, the first part of the curve moves down, the start of the jump is lowered, and the jump becomes larger. The position of the curve after the equivalence point is determined by the couple of the titrant.

![Titration curves of Fe²⁺ with KMnO₄ in different media (calculated from the Nernst equation, with E = 1.51 V and [H⁺] = 1 mol L⁻¹ on the titrant side): the equivalence point (dot) is displaced toward the permanganate side; H₃PO₄ lowers the formal potential of Fe(III)/Fe(II) and moves the start of the jump below the transition range of sodium diphenylamine sulfonate (gray band)](./plots/medium-effect-fe.py)

($\ce{MnO4-}/\ce{Mn^2+}$ is an irreversible couple, and the measured potentials after the equivalence point are lower than those calculated from the Nernst equation in the figure, but the part before the equivalence point, which is determined by the reversible iron couple, agrees with experiment.)

### 5.3.3. Indicators for Redox Titrations

1. Redox indicators.

**Definition 5.3.1 (Redox Indicator)** An organic compound that is itself redox active and whose oxidized and reduced forms differ in color, so that it is oxidized or reduced as the potential of the solution changes during the titration and thereby changes color to signal the end point, is called a **redox indicator**.

For $\mathrm{In(Ox)} + z\ce{e-} \ce{<=>} \mathrm{In(Red)}$, $E = E^{\circ\prime}_{\mathrm{In}} + \frac{0.0592}{z}\lg\frac{c_{\mathrm{In(Ox)}}}{c_{\mathrm{In(Red)}}}$. As with the **transition range** $\mathrm{p}K_{\mathrm{a}} \pm 1$ of an **acid–base indicator**, the eye perceives a color change only when the concentration ratio of the two forms changes from 1/10 to 10, so the range of potential over which the color changes is

$$
E^{\circ\prime}_{\mathrm{In}} \pm \frac{0.0592\,\mathrm{V}}{z}. \tag{5.6}
$$
The indicator is chosen so that its transition range falls wholly or partly within the jump and $E^{\circ\prime}_{\mathrm{In}}$ is as close as possible to $E_{\mathrm{sp}}$. Two common ones are:

| Indicator | $E^{\circ\prime}_{\mathrm{In}}/\mathrm{V}$ ($[\ce{H+}] = 1\,\mathrm{mol\,L^{-1}}$) | Reduced → oxidized form | Use |
|---|---|---|---|
| Sodium diphenylamine sulfonate | 0.85 | Colorless → purple-red | $\ce{K2Cr2O7}$ titration of $\ce{Fe^2+}$ (with $\ce{H3PO4}$) |
| 1,10-Phenanthroline–iron(II) (ferroin) | 1.06 | Red → pale blue | $\ce{Ce^4+}$ titration of $\ce{Fe^2+}$; back titration in COD |

```smiles
OS(=O)(=O)c1ccc(Nc2ccccc2)cc1 HIn
c1cnc2c(c1)ccc1cccnc12 phen
```

On oxidation, diphenylamine sulfonic acid first forms the colorless diphenylbenzidine sulfonic acid (irreversibly), which is then oxidized reversibly to a purple-red quinoid product; the indicator itself consumes so little oxidant that this can be neglected. Ferroin is $\ce{[Fe(phen)3]^2+}$, and its potential is much higher than that of $\ce{Fe^3+}/\ce{Fe^2+}$, which is precisely the complexation effect described in Section 5.1.3: the complex of 1,10-phenanthroline with $\ce{Fe^2+}$ is more stable than that with $\ce{Fe^3+}$ (a strong-field low-spin $\mathrm{d}^6$ complex, [6.1.5](/6.1.5#sec-5.5.5)), which raises the potential. The color change of ferroin is reversible and sharp, and it is the ideal indicator for the titration of $\ce{Fe^2+}$ with $\ce{Ce^4+}$, for which $E^{\circ\prime}_{\mathrm{In}}$ equals $E_{\mathrm{sp}}$.

2. Self-indicators.

**Definition 5.3.2 (Self-Indicator)** A substance that is itself colored, either as titrant or as analyte, while the reaction product is colorless or only faintly colored, so that no indicator need be added and its own color change signals the end point, is called a **self-indicator**.

For example, a $\ce{KMnO4}$ solution is purple-red and the reduction product $\ce{Mn^2+}$ is almost colorless; a pink color is visible when the concentration of $\ce{MnO4-}$ reaches about $2\times10^{-6}\,\mathrm{mol\,L^{-1}}$, so permanganate titrations usually need no added indicator.

3. Specific indicators.

**Definition 5.3.3 (Specific Indicator)** A substance that is itself not redox active but forms a colored compound characteristically with a particular oxidation state (or reduced form) of the titrant or analyte, and thereby signals the end point, is called a **specific indicator**.

The most important is starch in iodometry: polyiodide chains such as $\ce{I5-}$ are enclosed in the helical cavity of amylose to form a deep blue inclusion compound, and in the presence of $\ce{I-}$ the blue color is already visible at an $\ce{I2}$ concentration of about $10^{-5}\,\mathrm{mol\,L^{-1}}$; the reaction is reversible and sensitive. Another example is the red complex of $\ce{SCN-}$ with $\ce{Fe^3+}$, which can be used in the titration of $\ce{Ti^3+}$ with $\ce{Fe^3+}$.

### 5.3.4. End-Point Error

Consider a titration of symmetric couples with $z_1 = z_2 = 1$ (for example $\ce{Ce^4+}$ with $\ce{Fe^2+}$), and let the difference between the end-point potential and the equivalence-point potential be $\Delta E = E_{\mathrm{ep}} - E_{\mathrm{sp}}$. At the end point the fraction of excess titrant is $c_{\mathrm{Ox_1}}/c_{\mathrm{Red_1}} = 10^{(E_{\mathrm{ep}} - E^{\circ\prime}_1)/0.0592}$ and the fraction of analyte remaining is $c_{\mathrm{Red_2}}/c_{\mathrm{Ox_2}} = 10^{(E^{\circ\prime}_2 - E_{\mathrm{ep}})/0.0592}$; the difference of the two is the end-point error. Substituting $E_{\mathrm{sp}} = (E^{\circ\prime}_1 + E^{\circ\prime}_2)/2$ gives a result of the same form as the **end-point error formula** of Theorem 2.7.1:

**Formula 5.3.1 (End-Point Error Formula for Redox Titrations)** For $z_1 = z_2 = 1$,

$$
E_{\mathrm{t}} = \frac{10^{\Delta E/0.0592} - 10^{-\Delta E/0.0592}}{10^{\Delta E^{\circ\prime}/(2\times0.0592)}}. \tag{5.7}
$$

The denominator $10^{\Delta E^{\circ\prime}/(2\times0.0592)} = \sqrt{K'}$ plays the same role as $\sqrt{c_{\mathrm{M,sp}}K'_{\mathrm{MY}}}$ in Eq. (3.9). The difference is that the end-point error of a redox titration is independent of concentration, because the potential depends only on the ratio of concentrations.

**Example 5.3.1** In $1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$, $\ce{Fe^2+}$ is titrated with $\ce{Ce^4+}$ using ferroin ($1.06\,\mathrm{V}$) and sodium diphenylamine sulfonate ($0.85\,\mathrm{V}$) as indicators in turn. Calculate the end-point error.

**Solution** $E_{\mathrm{sp}} = 1.06\,\mathrm{V}$, $\Delta E^{\circ\prime} = 0.76\,\mathrm{V}$, and $10^{0.76/0.1184} = 10^{6.42}$. With ferroin $\Delta E = 0$ and $E_{\mathrm{t}} = 0$. With sodium diphenylamine sulfonate $\Delta E = -0.21\,\mathrm{V}$ and

$$
E_{\mathrm{t}} = \frac{10^{-3.55} - 10^{3.55}}{10^{6.42}} = -0.13\%,
$$
so the end point comes early and the error exceeds 0.1%.

**Example 5.3.2** $\ce{Fe^2+}$ is titrated with $\ce{K2Cr2O7}$ using sodium diphenylamine sulfonate ($E^{\circ\prime}_{\mathrm{In}} = 0.85\,\mathrm{V}$) as indicator. Compare the end-point errors with $\ce{H2SO4}$ only ($E^{\circ\prime}_{\ce{Fe}} = 0.68\,\mathrm{V}$) and with added $\ce{H3PO4}$ ($E^{\circ\prime}_{\ce{Fe}} = 0.46\,\mathrm{V}$).

**Solution** The equivalence-point potential is about 0.95 V or higher, the indicator changes color before the equivalence point, and the end-point potential is determined by the iron couple: the fraction of remaining $\ce{Fe^2+}$ is $c_{\ce{Fe^2+}}/c_{\ce{Fe^3+}} = 10^{-(0.85 - E^{\circ\prime}_{\ce{Fe}})/0.0592}$. With $\ce{H2SO4}$ only this is $10^{-2.87} = 0.13\%$, so $E_{\mathrm{t}} = -0.13\%$: at 99.9% titrated the potential is only 0.86 V, the indicator has already changed color, and the end point is premature. With $\ce{H3PO4}$ added the fraction is $10^{-6.59}$, and the error is negligible. $\ce{H3PO4}$ has another function, namely forming a colorless complex with the yellow $\ce{Fe^3+}$ and thereby eliminating its interference with the color of the end point.

## 5.4. Pretreatment Before Titration

### 5.4.1. Preoxidation and Prereduction

The analyte is often present in the sample solution in several oxidation states; after dissolution of an iron ore, for example, both $\ce{Fe^3+}$ and $\ce{Fe^2+}$ are present, whereas one titration can determine only one of them.

**Definition 5.4.1 (Preoxidation)** The step before titration in which the analyte is quantitatively oxidized to a higher oxidation state (so that it can be titrated with a reducing agent) or quantitatively reduced to a lower one (so that it can be titrated with an oxidizing agent) is called **preoxidation** or **prereduction**.

In the determination of total iron, for example, $\ce{SnCl2}$ is used to reduce all the $\ce{Fe^3+}$ to $\ce{Fe^2+}$, which is then titrated in one step with $\ce{K2Cr2O7}$. The reagent used in pretreatment must satisfy the following conditions:

1. The reaction is fast and oxidizes or reduces the analyte quantitatively.
2. The reagent has some selectivity. Metallic zinc ($E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.762\,\mathrm{V}$), for example, is so strong a reducing agent that it also reduces Ti(IV) and others, whereas $\ce{SnCl2}$ ($E^\circ(\ce{Sn^4+}/\ce{Sn^2+}) = 0.151\,\mathrm{V}$) reduces only fairly strong oxidants such as $\ce{Fe^3+}$ and is highly selective.
3. Excess reagent is easily removed: $\ce{H2O2}$ and $\ce{(NH4)2S2O8}$ are decomposed by boiling; $\ce{NaBiO3}$ is insoluble in water and is removed by filtration; excess $\ce{SnCl2}$ is removed with $\ce{HgCl2}$, $\ce{SnCl2 + 2HgCl2 -> SnCl4 + Hg2Cl2 v}$ (a silky white precipitate forms; if gray-black Hg appears, the excess of $\ce{SnCl2}$ was too large, the Hg would reduce the titrant, and the sample must be discarded).

Common preoxidants are $\ce{(NH4)2S2O8}$ (which, catalyzed by $\ce{Ag+}$, oxidizes $\ce{Mn^2+}$ to $\ce{MnO4-}$ and $\ce{Cr^3+}$ to $\ce{Cr2O7^2-}$), $\ce{NaBiO3}$, $\ce{H2O2}$ (which oxidizes Cr(III) to $\ce{CrO4^2-}$ in alkaline solution), and $\ce{KMnO4}$. Common prereductants are $\ce{SnCl2}$, $\ce{TiCl3}$, zinc metal or zinc amalgam reduction columns (the Jones reductor), silver reduction columns (the Walden reductor, with $E \approx 0.22\,\mathrm{V}$ in HCl and better selectivity), and $\ce{SO2}$.

$\ce{HgCl2}$ and $\ce{Hg2Cl2}$ are toxic, and mercury-containing waste pollutes the environment. The current mercury-free method for iron is the combined $\ce{SnCl2}$–$\ce{TiCl3}$ prereduction: most of the $\ce{Fe^3+}$ is first reduced with $\ce{SnCl2}$ and the remainder with $\ce{TiCl3}$, with sodium tungstate as indicator (once the $\ce{Fe^3+}$ is completely reduced, a slight excess of $\ce{Ti^3+}$ reduces W(VI) to blue "tungsten blue"). Dilute $\ce{K2Cr2O7}$ is then added dropwise until the blue color just disappears, which oxidizes the excess $\ce{Ti^3+}$.

### 5.4.2. Destruction of Organic Matter

In the determination of metals in organic samples (biological tissue, food, drugs), the organic matter reacts with the titrant or coordinates the metal ions and must be destroyed first:

1. Dry ashing: the organic matter is oxidized and decomposed by atmospheric oxygen at $400$–$700\,^\circ\mathrm{C}$ in a muffle furnace and the residue is dissolved in acid, or the sample is burned in a closed flask filled with oxygen (oxygen-flask combustion, used for halogens and sulfur in organic compounds). The method is simple and uses little reagent, but volatile elements (Hg, As, Se, and part of Pb) are lost.
2. Wet digestion: the organic matter is decomposed by heating with oxidizing acids ($\ce{HNO3}$–$\ce{H2SO4}$, $\ce{HNO3}$–$\ce{HClO4}$, sometimes with $\ce{H2O2}$). Hot concentrated $\ce{HClO4}$ explodes violently on contact with organic matter, so most of the organic matter must first be oxidized with $\ce{HNO3}$ before $\ce{HClO4}$ is added, and the work must be done in a special fume hood.
3. Microwave digestion: the sample and acids are heated by microwaves in a closed polytetrafluoroethylene vessel, and the high temperature and pressure in the vessel complete the digestion in a few tens of minutes with very little loss by volatilization or contamination. It is the routine method of digesting biological and environmental samples, followed usually by determination by atomic spectrometry ([6.4.8](/6.4.8)) or inductively coupled plasma mass spectrometry.

## 5.5. Common Redox Titrations

### 5.5.1. Permanganometry

**Definition 5.5.1 (Permanganometry)** A redox titration with $\ce{KMnO4}$ as titrant is called **permanganometry** (permanganate titration).

$\ce{KMnO4}$ is a strong oxidant whose oxidizing power and reduction product depend on the acidity:

| Medium | Half-reaction | $E^\circ/\mathrm{V}$ |
|---|---|---|
| Strongly acidic | $\ce{MnO4- + 8H+ + 5e- <=> Mn^2+ + 4H2O}$ | 1.507 |
| Neutral, weakly basic | $\ce{MnO4- + 2H2O + 3e- <=> MnO2 + 4OH-}$ | 0.595 |
| Strongly basic ($[\ce{OH-}] > 2\,\mathrm{mol\,L^{-1}}$) | $\ce{MnO4- + e- <=> MnO4^2-}$ | 0.558 |

The titration is usually carried out in $0.5$–$1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$: if the acidity is insufficient, brown $\ce{MnO2}$ precipitates and the stoichiometry changes. HCl is not used ($\ce{Cl-}$ is oxidized and there is induction, Section 5.2.4), nor is $\ce{HNO3}$ (itself an oxidant). In alkaline solution $\ce{KMnO4}$ oxidizes organic compounds faster than in acidic solution, and this is used for their determination.

Standard solution. Commercial $\ce{KMnO4}$ often contains impurities such as $\ce{MnO2}$, and distilled water contains traces of reducing substances. A $\ce{KMnO4}$ solution is unstable, decomposing by $\ce{4MnO4- + 2H2O -> 4MnO2 v + 3O2 ^ + 4OH-}$, and this decomposition is catalyzed by $\ce{MnO2}$ and light. The standard solution can therefore only be prepared indirectly: a little more than the calculated amount of $\ce{KMnO4}$ is dissolved in water, the solution is heated at a gentle boil for about 1 h (or left in the dark for a week or more) to oxidize the reducing substances completely, the $\ce{MnO2}$ is removed by filtration through a sintered-glass funnel (not filter paper), and the solution is stored in a brown bottle and then standardized.

The **primary standard** commonly used for standardization is $\ce{Na2C2O4}$ (easily purified, stable, and free of water of crystallization); $\ce{H2C2O4*2H2O}$ and pure iron wire can also be used. The standardization reaction is $\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 + 8H2O}$ of Section 5.2.3, and the conditions can be summarized as "three conditions and one end point":

1. Rate: the reaction is very slow at the beginning, so the second drop is added only after the first drop of $\ce{KMnO4}$ has been decolorized; once $\ce{Mn^2+}$ has formed, autocatalysis speeds up the reaction and the titration can be made faster.
2. Temperature: heat to $75$–$85\,^\circ\mathrm{C}$, and not below $60\,^\circ\mathrm{C}$ at the end point; above $90\,^\circ\mathrm{C}$ oxalic acid partly decomposes.
3. Acidity: $0.5$–$1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$.
4. End point: with $\ce{KMnO4}$ as its own indicator, the end point is the appearance of a pink color that persists for 30 s (after a longer time the pink color fades because of reducing substances in the air).

Applications:

1. Direct titration of reducing agents: $\ce{H2O2}$ is titrated directly in $\ce{H2SO4}$ medium at room temperature, $\ce{5H2O2 + 2MnO4- + 6H+ -> 2Mn^2+ + 5O2 ^ + 8H2O}$ ($E^\circ(\ce{O2}/\ce{H2O2}) = 0.695\,\mathrm{V}$); this reaction is also slow at first and speeds up once $\ce{Mn^2+}$ has formed. The classical determination of catalase activity in biochemistry is a titration of the $\ce{H2O2}$ remaining after enzymatic action with $\ce{KMnO4}$. $\ce{Fe^2+}$, $\ce{NO2-}$, As(III), Sb(III), and others can also be titrated directly.
2. Determination of iron: the sample is dissolved in HCl, prereduced with $\ce{SnCl2}$, and titrated after addition of the Zimmermann–Reinhardt reagent (Section 5.2.4).
3. Indirect determination of non-redox substances: in the determination of calcium, for example, $\ce{(NH4)2C2O4}$ is added to the acidic solution, which is then slowly neutralized with ammonia to about pH 4 so that $\ce{CaC2O4}$ separates at low relative supersaturation (the idea of homogeneous precipitation, [6.4.4](/6.4.4#sec-4.3.3)). The precipitate is digested and filtered, the excess oxalate is washed out with cold water, the precipitate is dissolved in dilute $\ce{H2SO4}$, and the $\ce{H2C2O4}$ released is titrated with $\ce{KMnO4}$, with $n(\ce{Ca}) = \frac52 n(\ce{KMnO4})$. The classical determination of serum calcium (the Kramer–Tisdall method) is done in this way. $\ce{Sr^2+}$, $\ce{Ba^2+}$, $\ce{Zn^2+}$, $\ce{Cd^2+}$, $\ce{Pb^2+}$, the rare earths, and other ions that form oxalate precipitates quantitatively can be determined in the same way.
4. Back titration of oxidants: $\ce{MnO2}$, $\ce{PbO2}$, $\ce{K2Cr2O7}$, $\ce{KClO3}$, and others are allowed to react with a known excess of $\ce{Na2C2O4}$, and the remaining oxalate is titrated with $\ce{KMnO4}$.
5. Determination of organic compounds: with excess $\ce{KMnO4}$ in strongly basic solution, glycerol, methanol, formaldehyde, formic acid, phenol, glucose, and others are oxidized quantitatively. For formic acid, for example, $\ce{2MnO4- + HCOO- + 3OH- -> CO3^2- + 2MnO4^2- + 2H2O}$. After the reaction the solution is acidified, so that $\ce{MnO4^2-}$ disproportionates to $\ce{MnO4-}$ and $\ce{MnO2}$, an excess of standard $\ce{Fe^2+}$ solution is added to reduce all the higher oxidation states of manganese to $\ce{Mn^2+}$, and the remaining $\ce{Fe^2+}$ is titrated with $\ce{KMnO4}$. The permanganate index in environmental monitoring is the amount of $\ce{KMnO4}$ consumed in oxidizing a water sample under specified conditions and is used to gauge pollution of surface water by organic and reducing substances.

The advantages of permanganometry are its strong oxidizing power and wide applicability and the fact that generally no indicator need be added. Its drawbacks are that the reagent contains impurities, the solution is not very stable, the reaction mechanism is complicated with many side reactions, the selectivity is poor, and the titration cannot be carried out in HCl medium.

### 5.5.2. Dichromate Titration

**Definition 5.5.2 (Dichromate Titration)** A redox titration with $\ce{K2Cr2O7}$ as titrant is called a **dichromate titration** (dichromatometry).

$\ce{Cr2O7^2- + 14H+ + 6e- <=> 2Cr^3+ + 7H2O}$, $E^\circ = 1.36\,\mathrm{V}$. $\ce{K2Cr2O7}$ is a somewhat weaker oxidant than $\ce{KMnO4}$ but has several outstanding advantages. It is easily purified and, after drying at $140$–$150\,^\circ\mathrm{C}$, can be used as a primary standard to prepare the standard solution directly. Its solutions are very stable and can be stored for a long time. In $1\,\mathrm{mol\,L^{-1}}$ HCl, $E^{\circ\prime} = 1.00\,\mathrm{V}$, which is lower than $E^\circ(\ce{Cl2}/\ce{Cl-}) = 1.358\,\mathrm{V}$, so $\ce{Cl-}$ is not oxidized at room temperature and titrations can be carried out in HCl medium. The drawbacks are that the reduction product $\ce{Cr^3+}$ is green, so an indicator (sodium diphenylamine sulfonate) is needed, and that Cr(VI) is toxic and carcinogenic, so waste solutions must be reduced to Cr(III) before disposal.

1. Determination of iron: this is the most important application of the dichromate titration and the standard method for total iron in iron ore. The sample is dissolved in HCl and prereduced with $\ce{SnCl2}$ (or by the mercury-free $\ce{SnCl2}$–$\ce{TiCl3}$ method), a mixed $\ce{H2SO4}$–$\ce{H3PO4}$ acid is added, and the solution is titrated with standard $\ce{K2Cr2O7}$ solution, with sodium diphenylamine sulfonate as indicator, until the color changes from green to purple:

$$
\ce{6Fe^2+ + Cr2O7^2- + 14H+ -> 6Fe^3+ + 2Cr^3+ + 7H2O}.
$$
The function of $\ce{H3PO4}$ is given in Example 5.3.2: it lowers $E^{\circ\prime}(\ce{Fe^3+}/\ce{Fe^2+})$ so that the color-change point of the indicator falls within the jump, and it complexes the yellow $\ce{Fe^3+}$ so that the end point is easier to see.
2. *Chemical oxygen demand* (COD): in strongly acidic solution, with $\ce{Ag2SO4}$ as catalyst and $\ce{HgSO4}$ to mask $\ce{Cl-}$, the organic matter in a water sample is oxidized by refluxing with excess $\ce{K2Cr2O7}$, and the remaining $\ce{K2Cr2O7}$ is back-titrated with standard ammonium iron(II) sulfate solution, with ferroin as indicator. The result is converted to the mass concentration of $\ce{O2}$ ($\mathrm{mg\,L^{-1}}$) needed to oxidize the same amount of organic matter. It is the main index of organic pollution of wastewater.
3. The reaction of $\ce{Cr2O7^2-}$ with $\ce{Fe^2+}$ can also be used for the indirect determination of oxidants such as $\ce{NO3-}$ (excess $\ce{Fe^2+}$ is added and the remainder back-titrated).

### 5.5.3. Iodometry and Iodimetry

**Definition 5.5.3 (Iodometric Titration)** Redox titration methods that use the oxidizing property of $\ce{I2}$ and the reducing property of $\ce{I-}$ are called **iodometric titrations** (the iodine methods).

The solubility of $\ce{I2}$ in water is very small (about $1.3\times10^{-3}\,\mathrm{mol\,L^{-1}}$), and what is actually used is $\ce{I3-}$ formed by dissolving it in KI solution:

$$
\ce{I3- + 2e- <=> 3I-}, \qquad E^\circ = 0.536\,\mathrm{V}.
$$
(For simplicity this is often written as $\ce{I2}$.) $\ce{I2}$ is a weak oxidant and $\ce{I-}$ a reducing agent of moderate strength, so there are two modes of iodine titration.

**Definition 5.5.4 (Iodimetry)** The method in which a reducing substance whose potential is lower than $E^\circ(\ce{I3-}/\ce{I-})$ is titrated directly with standard $\ce{I2}$ solution is called **iodimetry** (direct iodine titration).

**Definition 5.5.5 (Iodometry)** The method in which an oxidizing substance is allowed to react with excess $\ce{I-}$ to liberate $\ce{I2}$ quantitatively (or a reducing substance is allowed to react with excess $\ce{I2}$), and the liberated (or remaining) $\ce{I2}$ is then titrated with standard $\ce{Na2S2O3}$ solution, is called **iodometry** (indirect iodine titration).

The titration reaction of iodometry is

$$
\ce{I2 + 2S2O3^2- -> 2I- + S4O6^2-}.
$$

Iodimetry can be carried out only in neutral or weakly acidic solution, because $\ce{I2}$ disproportionates in alkaline solution ($\ce{3I2 + 6OH- -> IO3- + 5I- + 3H2O}$). Substances that can be titrated directly include $\ce{S^2-}$, $\ce{SO3^2-}$, $\ce{S2O3^2-}$, As(III), Sn(II), and vitamin C.

Iodometry has a much wider range of application: any oxidant that oxidizes $\ce{I-}$ quantitatively to $\ce{I2}$ ($\ce{Cu^2+}$, $\ce{Cr2O7^2-}$, $\ce{IO3-}$, $\ce{BrO3-}$, $\ce{ClO-}$, $\ce{H2O2}$, $\ce{O2}$, and others) can be determined. Its conditions are:

1. The titration is carried out in neutral or weakly acidic solution. In strongly basic solution $\ce{S2O3^2-}$ is partly oxidized by $\ce{I2}$ to $\ce{SO4^2-}$ ($\ce{S2O3^2- + 4I2 + 10OH- -> 2SO4^2- + 8I- + 5H2O}$), which changes the stoichiometry, and $\ce{I2}$ also disproportionates; in strongly acidic solution $\ce{S2O3^2-}$ decomposes ($\ce{S2O3^2- + 2H+ -> S v + SO2 + H2O}$) and $\ce{I-}$ is easily oxidized by air.
2. Volatilization of $\ce{I2}$ is prevented by adding excess KI (generally 2–3 times the theoretical amount) so that $\ce{I2}$ forms $\ce{I3-}$, by working at room temperature, by carrying out the reaction in an iodine flask, and by not shaking vigorously during the titration.
3. Air oxidation of $\ce{I-}$ ($\ce{4I- + O2 + 4H+ -> 2I2 + 2H2O}$, catalyzed by light, $\ce{Cu^2+}$, and $\ce{NO2-}$) is prevented by keeping the acidity of the solution from being too high, avoiding direct sunlight, and titrating immediately after the $\ce{I2}$ has been liberated.
4. The starch indicator should be added near the end point (when the solution is pale yellow). At high $\ce{I2}$ concentration starch adsorbs a large amount of $\ce{I2}$ and releases it slowly, which delays the end point. In iodimetry the starch can be added at the beginning of the titration, and the end point is a change from colorless to blue.

Standard $\ce{Na2S2O3}$ solution. $\ce{Na2S2O3*5H2O}$ effloresces and is deliquescent and often contains small amounts of impurities, so a standard solution cannot be prepared directly. Its solutions are also unstable: dissolved $\ce{CO2}$ decomposes it, atmospheric $\ce{O2}$ oxidizes it, and sulfur-consuming bacteria decompose it with deposition of sulfur. The solution is therefore prepared with freshly boiled and cooled distilled water (which removes $\ce{CO2}$ and $\ce{O2}$ and kills bacteria), a little $\ce{Na2CO3}$ is added to make it weakly basic (pH 9–10, which inhibits bacteria), and it is stored in a brown bottle for 1–2 weeks until the concentration is stable before it is standardized.

The primary standards used for standardization are $\ce{K2Cr2O7}$ and $\ce{KIO3}$, by the iodometric procedure:

$$
\ce{Cr2O7^2- + 6I- + 14H+ -> 2Cr^3+ + 3I2 + 7H2O}, \qquad \ce{IO3- + 5I- + 6H+ -> 3I2 + 3H2O},
$$
and 1 mol of $\ce{K2Cr2O7}$ or of $\ce{KIO3}$ corresponds to 6 mol of $\ce{Na2S2O3}$. With $\ce{K2Cr2O7}$, excess KI is added at an acidity of $0.2$–$0.4\,\mathrm{mol\,L^{-1}}$ and the solution is left in the dark for 5 min to complete the reaction. It is then diluted with water (which lowers the acidity, reduces air oxidation of $\ce{I-}$, and dilutes the green color of $\ce{Cr^3+}$), titrated with $\ce{Na2S2O3}$ to a pale yellow, and starch is added; titration continues until the blue color disappears and the solution shows the bright green of $\ce{Cr^3+}$. If the solution turns blue again after standing for more than 5 min after the titration, this is due to air oxidation of $\ce{I-}$ and is normal; if it turns blue quickly, the reaction of $\ce{Cr2O7^2-}$ with $\ce{I-}$ was not yet complete and the standardization should be repeated.

**Example 5.5.1** A $0.1226\,\mathrm{g}$ sample of primary-standard $\ce{K2Cr2O7}$ is used to standardize a $\ce{Na2S2O3}$ solution by the procedure above and consumes $25.00\,\mathrm{mL}$. Find $c(\ce{Na2S2O3})$. $M(\ce{K2Cr2O7}) = 294.18\,\mathrm{g\,mol^{-1}}$.

**Solution** $n(\ce{Na2S2O3}) = 6n(\ce{K2Cr2O7}) = 6\times0.1226/294.18 = 2.501\times10^{-3}\,\mathrm{mol}$, and $c = 2.501\times10^{-3}/0.02500 = 0.1000\,\mathrm{mol\,L^{-1}}$.

Applications of the iodine methods:

1. Determination of copper: excess KI is added to a solution at pH 3–4 ($\ce{NH4HF2}$ controls the acidity and at the same time masks $\ce{Fe^3+}$ as $\ce{FeF6^3-}$, Example 5.1.2), $\ce{2Cu^2+ + 4I- -> 2CuI v + I2}$, and the liberated $\ce{I2}$ is titrated with $\ce{Na2S2O3}$, with $n(\ce{Cu^2+}) = n(\ce{S2O3^2-})$. KI must be in excess, since it acts as reducing agent and precipitant and also makes $\ce{I2}$ form $\ce{I3-}$, which ensures that the reaction is complete. The CuI precipitate strongly adsorbs $\ce{I2}$ and makes the result low; near the end point KSCN is added, which converts CuI to the less soluble CuSCN, which adsorbs little $\ce{I2}$, and releases the adsorbed $\ce{I2}$. KSCN must not be added too early, since $\ce{SCN-}$ would reduce $\ce{I2}$ and make the result low.
2. Sulfides and sulfur-containing gases: in weakly acidic solution $\ce{H2S + I2 -> S v + 2H+ + 2I-}$. To prevent loss of $\ce{H2S}$, the sample solution is added to excess acidic iodine solution and the remaining $\ce{I2}$ is back-titrated with $\ce{Na2S2O3}$. Organic sulfur compounds can first be converted to $\ce{H2S}$, absorbed in an ammoniacal zinc salt solution, and determined.
3. Available chlorine in bleaching powder: the main component of bleaching powder is $\ce{CaCl(OCl)}$, and its quality is measured by the amount of chlorine it can release (available chlorine, expressed as the mass fraction of Cl). The sample is dissolved in dilute $\ce{H2SO4}$ and excess KI is added, $\ce{ClO- + 2I- + 2H+ -> I2 + Cl- + H2O}$ ($\ce{ClO2-}$ reacts in the same way: $\ce{ClO2- + 4I- + 4H+ -> 2I2 + Cl- + 2H2O}$), and the liberated $\ce{I2}$ is titrated with $\ce{Na2S2O3}$.
4. Vitamin C (ascorbic acid): the enediol structure is strongly reducing and is oxidized quantitatively by $\ce{I2}$ to dehydroascorbic acid, $\ce{C6H8O6 + I2 -> C6H6O6 + 2HI}$, and is titrated by iodimetry. Ascorbic acid is very easily oxidized in air, especially in alkaline solution, so the sample is dissolved in dilute acetic acid and titrated immediately. This is the usual method for vitamin C in drugs and fruit juices.

```smiles
OC[C@H](O)[C@H]1OC(=O)C(O)=C1O>>OC[C@H](O)[C@H]1OC(=O)C(=O)C1=O
```

5. Glucose and other aldoses: a known excess of standard $\ce{I2}$ solution is added in alkaline solution, and the $\ce{IO-}$ formed by disproportionation of $\ce{I2}$ oxidizes the aldehyde group to a carboxyl group:

$$
\begin{aligned}
&\ce{I2 + 2OH- -> IO- + I- + H2O},\\
&\ce{CH2OH(CHOH)4CHO + IO- + OH- -> CH2OH(CHOH)4COO- + I- + H2O}.
\end{aligned}
$$
The remaining $\ce{IO-}$ disproportionates in alkaline solution to $\ce{IO3-}$ and $\ce{I-}$ ($\ce{3IO- -> IO3- + 2I-}$) and is converted back entirely to $\ce{I2}$ on acidification ($\ce{IO3- + 5I- + 6H+ -> 3I2 + 3H2O}$), which is titrated with $\ce{Na2S2O3}$. One mole of glucose corresponds to 1 mol of $\ce{I2}$. Ketoses (fructose) are not oxidized under these conditions, which allows the aldose in a mixture of aldose and ketose to be determined.
6. Magnesium via 8-hydroxyquinoline (bromometry): $\ce{Mg^2+}$ forms a $\ce{Mg(Ox)2}$ precipitate with 8-hydroxyquinoline (HOx, [6.4.4](/6.4.4#sec-4.3.4)), which is filtered, washed, and dissolved in HCl. A known excess of standard $\ce{KBrO3}$–KBr solution is added, and the $\ce{Br2}$ formed in acid ($\ce{BrO3- + 5Br- + 6H+ -> 3Br2 + 3H2O}$) brominates 8-hydroxyquinoline to give 5,7-dibromo-8-hydroxyquinoline (two $\ce{Br2}$ per HOx). The remaining $\ce{Br2}$ is converted to $\ce{I2}$ by KI and titrated with $\ce{Na2S2O3}$. The stoichiometry is

$$
1\,\ce{Mg^2+} \;\hat{=}\; 2\,\mathrm{HOx} \;\hat{=}\; 4\,\ce{Br2} \;\hat{=}\; \tfrac{4}{3}\,\ce{KBrO3} \;\hat{=}\; 8\,\ce{S2O3^2-},
$$
so that one $\ce{Mg^2+}$ corresponds to eight $\ce{S2O3^2-}$; this amplifies the stoichiometry and suits the determination of small amounts of magnesium. The same method is used for phenol (which gives tribromophenol).
7. Determination of water (Karl Fischer titration): in a medium of methanol and an organic base (pyridine or imidazole), the oxidation of $\ce{SO2}$ by $\ce{I2}$ consumes water quantitatively, $\ce{H2O + I2 + SO2 + CH3OH + 3RN -> [RNH]SO4CH3 + 2[RNH]I}$, and the consumption of iodine measures trace water in the sample. It is the standard method for water in drugs, foods, and solvents; in the current coulometric version $\ce{I2}$ is generated electrolytically, see [6.4.6](/6.4.6#sec-6.5.4).

## Summary

| Topic | Key points |
|---|---|
| Formal potential | $E^{\circ\prime} = E^\circ + \frac{RT}{zF}\ln\frac{\gamma_{\mathrm{Ox}}\alpha_{\mathrm{Red}}}{\gamma_{\mathrm{Red}}\alpha_{\mathrm{Ox}}}$, $E = E^{\circ\prime} + \frac{0.0592}{z}\lg\frac{c_{\mathrm{Ox}}}{c_{\mathrm{Red}}}$; precipitation ($\ce{Cu^2+}/\ce{CuI}$ 0.86 V), complexation ($\ce{Fe^3+}$ with $\ce{F-}$, $\ce{PO4^3-}$), acidity (As(V)/I⁻ reverses with pH), ionic strength |
| Completeness | $\lg K' = z\Delta E^{\circ\prime}/0.0592$; for 99.9%: $\lg K' \ge 3(p_1 + p_2)$, and for 1:1 reactions $\Delta E^{\circ\prime} \ge 0.36\,\mathrm{V}$ |
| Rate | Intrinsic factors (bond breaking, oxidation number, charge); concentration, temperature, catalysts, autocatalysis ($\ce{Mn^2+}$); induced reactions ($\ce{MnO4-}$–$\ce{Fe^2+}$ induces oxidation of $\ce{Cl-}$) |
| Titration curve | Analyte couple before the equivalence point, titrant couple after; for symmetric couples $E_{\mathrm{sp}} = (z_1E^{\circ\prime}_1 + z_2E^{\circ\prime}_2)/(z_1 + z_2)$, displaced toward the larger $z$; the jump is independent of concentration |
| Indicators | Redox indicators $E^{\circ\prime}_{\mathrm{In}} \pm 0.0592/z$ (sodium diphenylamine sulfonate 0.85 V, ferroin 1.06 V); self-indicators ($\ce{KMnO4}$); specific indicators (starch) |
| End-point error | 1:1 symmetric: $E_{\mathrm{t}} = (10^{\Delta E/0.0592} - 10^{-\Delta E/0.0592})/10^{\Delta E^{\circ\prime}/0.1184}$ |
| Pretreatment | Preoxidation and prereduction ($\ce{SnCl2}$–$\ce{HgCl2}$ or the mercury-free $\ce{SnCl2}$–$\ce{TiCl3}$); dry ashing, wet digestion, microwave digestion |
| Three methods | $\ce{KMnO4}$: strong oxidant, self-indicating, indirect preparation, standardization with $\ce{Na2C2O4}$ under "three conditions and one end point", $\ce{H2SO4}$ medium; $\ce{K2Cr2O7}$: primary standard prepared directly, iron titration possible in HCl, COD; iodine methods: iodimetry and iodometry, preparation and standardization of $\ce{Na2S2O3}$, neutral or weakly acidic solution, prevention of volatilization and air oxidation, starch added near the end point |
