---
title: Titrimetric Analysis and Acid–Base Titrations
description: Modes of titration, primary standards, titer and calculations; activity and concentration constants; distribution fractions, proton conditions, and exact and approximate formulas for pH; preparation of buffers (ionic-strength corrections, Tris and Good's buffers); indicators and mixed indicators; titration of polyprotic acids and bases and of mixed acids, the double-indicator method; the end-point error formula and criteria for feasibility of titration; the Kjeldahl method and titration of amino acids.
source_hash: f70d8022938a
---

Section [6.1.9](/6.1.9) has already treated the Brønsted–Lowry theory of acids and bases, the pH of weak acids, weak bases, and amphoteric species, buffer solutions, and the simplest titration curves ([9.6](/6.1.9#sec-9.6)). This chapter organizes titration as a quantitative method. We first present the modes and calculations of titrimetric analysis (Section 2.1), then explain when activities must replace concentrations (2.2). On the basis of 6.1.9 we then give the rigorous treatment of acid–base equilibria and the criteria for approximations (2.3), physiological and biochemical buffers (2.4), the choice of indicators (2.5), titration curves of polyprotic systems (2.6), the quantitative formula for the end-point error and the feasibility criteria that follow from it (2.7), and finally applications such as the Kjeldahl method and the titration of amino acids (2.8). The distribution fractions of 2.3 and the end-point error formula of 2.7 form the common framework of the next three chapters: complexometric titration ([6.4.3](/6.4.3)), precipitation titration ([6.4.4](/6.4.4)), and redox titration ([6.4.5](/6.4.5)) merely replace the proton by a metal ion, a precipitant, or an electron, and pH by pM or the electrode potential.

## 2.1. Overview of Titrimetric Analysis

### 2.1.1. Basic Concepts and Modes of Titration

**Titration** is the method in which a **standard solution** is added from a buret to the solution of the analyte until the two have reacted completely according to the stoichiometry, and the content of the analyte is calculated from the concentration and volume of the standard solution ([6.1.9](/6.1.9#sec-9.6.1)). The point at which the two have just reacted completely in the stoichiometric ratio is the **stoichiometric point** (sp), the point at which the indicator changes color and the titration is stopped is the **end point** (ep), and the error caused by the difference between them is the **titration error** (2.7).

**Definition 2.1.1** The reagent solution of accurately known concentration that is added from the buret in a titration is called the **titrant**.

By the type of reaction, titrimetric analysis falls into four classes, to each of which this course devotes one chapter:

| Class | Reaction | Example | In this course |
|---|---|---|---|
| Acid–base titration | Proton transfer | $\ce{H+ + OH- -> H2O}$ | This chapter |
| Complexometric titration | Complex formation | $\ce{Zn^2+ + Y^4- -> ZnY^2-}$ (Y is EDTA) | [6.4.3](/6.4.3) |
| Precipitation titration | Precipitate formation | $\ce{Ag+ + Cl- -> AgCl v}$ | [6.4.4](/6.4.4) |
| Redox titration | Electron transfer | $\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}$ | [6.4.5](/6.4.5) |

A reaction used for titration must go to completion (more than 99.9%) with a definite stoichiometry, be fast enough, and have a simple means of locating the end point. When these conditions are not met, the mode of titration can be changed.

**Definition 2.1.2** Titrating the analyte directly with a standard solution is called **direct titration**; adding a measured excess of one standard solution, and after the reaction is complete titrating the remainder with another standard solution, is called **back titration**; when the analyte cannot react with the titrant in a definite stoichiometry, letting it first react with a suitable reagent that quantitatively liberates another substance, and then titrating that substance, is called **displacement titration**; and when the analyte does not react with the titrant, converting it by other chemical reactions quantitatively into a substance that can be titrated is called **indirect titration**.

- Back titration: $\ce{Al^3+}$ reacts very slowly with EDTA and blocks the indicator, so an excess of standard EDTA is added and the mixture is heated to complete the complexation, and the remaining EDTA is back-titrated with a standard $\ce{Zn^2+}$ solution ([6.4.3](/6.4.3#sec-3.6.2)). Solid samples (for example, $\ce{CaCO3}$ dissolved in an excess of HCl) are also often determined by back titration.
- Displacement titration: the product of the oxidation of $\ce{S2O3^2-}$ by $\ce{K2Cr2O7}$ is not well defined (a mixture of $\ce{S4O6^2-}$ and $\ce{SO4^2-}$), so there is no definite stoichiometry; instead, the dichromate is allowed to react with an excess of KI in acid solution, liberating a stoichiometric amount of $\ce{I2}$, which is titrated with $\ce{Na2S2O3}$ ([6.4.5](/6.4.5#sec-5.5.3)).
- Indirect titration: $\ce{Ca^2+}$ has no redox properties, so it is first precipitated as $\ce{CaC2O4}$, filtered, washed, and dissolved in $\ce{H2SO4}$, and the liberated $\ce{H2C2O4}$ is titrated with $\ce{KMnO4}$.

### 2.1.2. Primary Standards and Standard Solutions

For the preparation of standard solutions and the requirements for a **primary standard** (composition corresponding to its formula, purity above 99.9%, stable, large molar mass, reacting quantitatively), see [6.1.9](/6.1.9#sec-9.6.1): a primary standard can be weighed out directly to make a standard solution, whereas other reagents are first prepared roughly, and the **standardization of a solution** then fixes its concentration. Common primary standards:

| Type of titration | Primary standard | Drying conditions | Standardizes |
|---|---|---|---|
| Acid–base | Anhydrous $\ce{Na2CO3}$ | 270–300 °C | HCl |
| | Borax $\ce{Na2B4O7*10H2O}$ | Stored over a constant-humidity (60% relative humidity) atmosphere to prevent efflorescence | HCl |
| | Potassium hydrogen phthalate $\ce{KHC8H4O4}$ | 105–110 °C | NaOH |
| | Oxalic acid $\ce{H2C2O4*2H2O}$ | Air-dried at room temperature | NaOH, $\ce{KMnO4}$ |
| Complexometric | Zn, $\ce{CaCO3}$ | Zn: oxide film removed with dilute acid; $\ce{CaCO3}$: 110 °C | EDTA |
| Precipitation | NaCl; $\ce{AgNO3}$ | NaCl: 500–600 °C; $\ce{AgNO3}$ stored protected from light | $\ce{AgNO3}$; chloride |
| Redox | $\ce{K2Cr2O7}$ | 140–150 °C | $\ce{Na2S2O3}$, $\ce{Fe^2+}$ |
| | $\ce{Na2C2O4}$ | 105–110 °C | $\ce{KMnO4}$ |
| | $\ce{KIO3}$, $\ce{KBrO3}$ | 130 °C | $\ce{Na2S2O3}$ |

$\ce{As2O3}$ was once a primary standard for iodine solutions but is now seldom used because it is highly toxic. If $\ce{AgNO3}$ is pure enough it can be used directly: to prepare $100.0\,\mathrm{mL}$ of a $0.1000\,\mathrm{mol\,L^{-1}}$ solution, weigh out $0.1000\times0.1000\times169.87 = 1.6987\,\mathrm{g}$, dissolve, and dilute to volume.

The concentration of a standard solution is usually expressed as the amount-of-substance concentration $c_{\mathrm{B}} = n_{\mathrm{B}}/V$, and the elementary entity must be specified ($c(\ce{KMnO4})$ and $c(\tfrac15\ce{KMnO4})$ differ by a factor of 5; on this site the formula unit is always the entity). When the same component is determined in large numbers of samples in industry, the titer is more convenient.

**Definition 2.1.3 (Titer)** The mass of analyte A equivalent to $1\,\mathrm{mL}$ of standard solution B is called the **titer**, denoted $T_{\mathrm{A/B}}$, in units of $\mathrm{g\,mL^{-1}}$. (The symbol $T$ here is the same as for the thermodynamic temperature and is used only in this section.)

Let the titration reaction be $a\mathrm{A} + b\mathrm{B} \to$ products, so that at the stoichiometric point $n_{\mathrm{A}} : n_{\mathrm{B}} = a : b$. When a volume $V_{\mathrm{B}}$ (mL) is consumed, $m_{\mathrm{A}} = \frac ab c_{\mathrm{B}}V_{\mathrm{B}}M_{\mathrm{A}}\times10^{-3}$, and so

$$
T_{\mathrm{A/B}} = \frac{m_{\mathrm{A}}}{V_{\mathrm{B}}} = \frac ab\,c_{\mathrm{B}}M_{\mathrm{A}}\times10^{-3}, \qquad m_{\mathrm{A}} = T_{\mathrm{A/B}}V_{\mathrm{B}}, \tag{2.1}
$$
where $c_{\mathrm{B}}$ is in $\mathrm{mol\,L^{-1}}$ and $M_{\mathrm{A}}$ in $\mathrm{g\,mol^{-1}}$.

### 2.1.3. Calculations in Titrimetric Analysis

The procedure for calculation is to write the relevant reactions, find the stoichiometric relation between analyte and titrant, and then set up the equation. For a sample of mass $m_{\mathrm{s}}$ the mass fraction of the analyte is

$$
w_{\mathrm{A}} = \frac{\frac ab\,c_{\mathrm{B}}V_{\mathrm{B}}M_{\mathrm{A}}}{m_{\mathrm{s}}}. \tag{2.2}
$$
When several reaction steps are involved, the ratio between analyte and final titrant is found from the overall stoichiometry.

**Example 2.1.1** Find the titer of a $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH standard solution with respect to $\ce{H2C2O4}$.

**Solution** $\ce{H2C2O4 + 2NaOH -> Na2C2O4 + 2H2O}$, $a/b = 1/2$, and by Eq. (2.1), $T_{\ce{H2C2O4}/\ce{NaOH}} = \frac12\times0.1000\times90.03\times10^{-3} = 4.502\times10^{-3}\,\mathrm{g\,mL^{-1}}$. $\square$

**Example 2.1.2** The concentration of a $\ce{KMnO4}$ standard solution is $0.02010\,\mathrm{mol\,L^{-1}}$. Find $T_{\ce{Fe}/\ce{KMnO4}}$ and $T_{\ce{Fe2O3}/\ce{KMnO4}}$. A $0.2718\,\mathrm{g}$ sample of iron ore is dissolved, the $\ce{Fe^3+}$ is reduced to $\ce{Fe^2+}$, and the solution is titrated with the above solution, consuming $26.30\,\mathrm{mL}$. Find the mass fractions of Fe and $\ce{Fe2O3}$ in the sample.

**Solution** $\ce{5Fe^2+ + MnO4- + 8H+ -> 5Fe^3+ + Mn^2+ + 4H2O}$, so $n(\ce{Fe}) = 5n(\ce{KMnO4})$ and $n(\ce{Fe2O3}) = \frac52 n(\ce{KMnO4})$.

$$
T_{\ce{Fe}/\ce{KMnO4}} = 5\times0.02010\times55.845\times10^{-3} = 5.612\times10^{-3}\,\mathrm{g\,mL^{-1}}, \qquad T_{\ce{Fe2O3}/\ce{KMnO4}} = \tfrac52\times0.02010\times159.69\times10^{-3} = 8.024\times10^{-3}\,\mathrm{g\,mL^{-1}},
$$
$w(\ce{Fe}) = 5.612\times10^{-3}\times26.30/0.2718 = 54.31\%$ and $w(\ce{Fe2O3}) = 8.024\times10^{-3}\times26.30/0.2718 = 77.65\%$. $\square$

**Example 2.1.3** In the analysis of $0.200\,\mathrm{g}$ of pyrolusite, $50.00\,\mathrm{mL}$ of $0.100\,\mathrm{mol\,L^{-1}}$ ammonium iron(II) sulfate solution is added to reduce $\ce{MnO2}$ to $\ce{Mn^2+}$; after the reaction is complete, the excess $\ce{Fe^2+}$ is back-titrated with $0.0200\,\mathrm{mol\,L^{-1}}$ $\ce{KMnO4}$, consuming $15.0\,\mathrm{mL}$. Express the manganese content as $\ce{Mn3O4}$ and find its mass fraction.

**Solution** The two reactions are $\ce{MnO2 + 2Fe^2+ + 4H+ -> Mn^2+ + 2Fe^3+ + 2H2O}$ and $\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}$. The amount of $\ce{Fe^2+}$ added is $5.00\,\mathrm{mmol}$, and the back titration consumed $5\times0.0200\times15.0 = 1.50\,\mathrm{mmol}$, so $3.50\,\mathrm{mmol}$ reacted with $\ce{MnO2}$, which corresponds to $1.75\,\mathrm{mmol}$ of Mn. Expressed as $\ce{Mn3O4}$ (three Mn per $\ce{Mn3O4}$):

$$
w(\ce{Mn3O4}) = \frac{\frac13\times1.75\times10^{-3}\times228.81}{0.200} = 66.7\%.
$$
The results of analyses of ores and alloys are conventionally reported in the form of a chosen compound, regardless of the form in which the element actually occurs in the sample. $\square$

**Example 2.1.4** Standardize a $\ce{Na2S2O3}$ solution by displacement titration, with $\ce{KBrO3}$ as the primary standard; write the stoichiometric relation.

**Solution** $\ce{BrO3- + 6I- + 6H+ -> 3I2 + Br- + 3H2O}$ and $\ce{I2 + 2S2O3^2- -> 2I- + S4O6^2-}$. The overall stoichiometry is $1\,\ce{BrO3-} \;\hat{=}\; 3\,\ce{I2} \;\hat{=}\; 6\,\ce{S2O3^2-}$, so $c(\ce{Na2S2O3}) = \dfrac{6m(\ce{KBrO3})}{M(\ce{KBrO3})V}$. KI is only an intermediate; an excess is added and need not be measured accurately. $\square$

## 2.2. Activity and Equilibrium Constants

### 2.2.1. Effect of Ionic Strength on Equilibria

When $\ce{KNO3}$ is added to the equilibrium system $\ce{Fe^3+ + SCN- <=> FeSCN^2+}$, the blood-red color becomes lighter, and $[\ce{FeSCN^2+}]/([\ce{Fe^3+}][\ce{SCN-}])$ decreases as the concentration of $\ce{KNO3}$ increases; when $0.05\,\mathrm{mol\,L^{-1}}$ $\ce{KNO3}$ is added to a saturated solution of $\ce{CaSO4}$, the solubility increases markedly. The ions $\ce{K+}$ and $\ce{NO3-}$ take no part in the reaction; through the shielding of their ionic atmospheres they lower the effective concentration, that is, the **activity**, of the reacting ions. The theory of this effect was given in [6.3.12](/6.3.12#sec-12.7); here we state only the results needed in analysis.

The activity of ion $i$ is $a_i = \gamma_ic_i/c^\circ$, where the **activity coefficient** $\gamma_i$ is determined by the **ionic strength** $I = \frac12\sum c_iz_i^2$ of the solution ([6.3.12](/6.3.12#sec-12.6.4)). In dilute aqueous solutions at $25\,^\circ\mathrm{C}$ ($I \lesssim 0.01$) the **Debye–Hückel limiting law** is used, and for $I \lesssim 0.1$ the extended form:

$$
\lg\gamma_i = -0.509\,z_i^2\sqrt I, \qquad \lg\gamma_i = -\frac{0.509\,z_i^2\sqrt I}{1 + B\mathring{a}\sqrt I}, \tag{2.3}
$$
with $I$ inserted as the numerical value in $\mathrm{mol\,L^{-1}}$, $B = 3.29\,\mathrm{nm^{-1}}$ (water at $25\,^\circ\mathrm{C}$), and $\mathring{a}$ the effective ion-size parameter (Kielland's values: $\ce{H+}$ 0.9 nm; $\ce{Li+}$, $\ce{Ca^2+}$, $\ce{Mg^2+}$ 0.6–0.8 nm; $\ce{Na+}$, $\ce{HCO3-}$, $\ce{H2PO4-}$ 0.4–0.45 nm; $\ce{K+}$, $\ce{Cl-}$, $\ce{NO3-}$ 0.3 nm; $\ce{SO4^2-}$, $\ce{HPO4^2-}$ 0.4 nm). When $\mathring{a}$ is not known one may take $B\mathring{a} \approx 1$, or use the Davies equation ([6.3.12](/6.3.12#sec-12.7.5), valid up to $I \approx 0.5$).

Some textbooks interpret the constants in Eq. (2.3) incorrectly: the coefficient $0.509 = A$ is proportional to $(\varepsilon_{\mathrm{r}}T)^{-3/2}$ ($\varepsilon_{\mathrm{r}}$ is the relative permittivity of the solvent), and not "the product of the dispersion of the solvent and the $-2/3$ power of the absolute temperature"; and $\mathring{a} = 900\,\mathrm{pm}$ is only the value for $\ce{H+}$, while most univalent ions lie between 300 and 450 pm.

The regularities of activity coefficients are as follows: the higher the charge of an ion, the larger the departure from ideality ($z_i^2$); at the same ionic strength ions of the same charge have similar $\gamma$; in dilute solutions $\gamma < 1$, but in concentrated electrolyte solutions $\gamma$ may rise again and even exceed 1 (the activity of the solvent is lowered and the ions are partly dehydrated); and for neutral molecules $\gamma \approx 1$.

**Example 2.2.1** Calculate the ionic strength of a mixed solution of $0.30\,\mathrm{mol\,L^{-1}}$ NaCl and $0.20\,\mathrm{mol\,L^{-1}}$ $\ce{Na2SO4}$.

**Solution** $c(\ce{Na+}) = 0.70$, $c(\ce{Cl-}) = 0.30$, $c(\ce{SO4^2-}) = 0.20$, and $I = \frac12(0.70 + 0.30 + 0.20\times4) = 0.90\,\mathrm{mol\,L^{-1}}$. Such a high ionic strength is beyond the range of validity of Eq. (2.3). $\square$

### 2.2.2. Activity Constants and Concentration Constants

For the weak acid $\ce{HA <=> H+ + A-}$ the equilibrium constant can be written in three ways:

$$
K_{\mathrm{a}}^\circ = \frac{a_{\ce{H+}}a_{\ce{A-}}}{a_{\ce{HA}}}, \qquad K_{\mathrm{a}}^{\mathrm{c}} = \frac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]} = K_{\mathrm{a}}^\circ\,\frac{\gamma_{\ce{HA}}}{\gamma_{\ce{H+}}\gamma_{\ce{A-}}}, \qquad K_{\mathrm{a}}^{\mathrm{M}} = \frac{a_{\ce{H+}}[\ce{A-}]}{[\ce{HA}]} = K_{\mathrm{a}}^\circ\,\frac{\gamma_{\ce{HA}}}{\gamma_{\ce{A-}}}.
$$

**Definition 2.2.1** The equilibrium constant $K^\circ$ expressed in the activities of all species (the standard equilibrium constant, also called the activity constant or thermodynamic constant) depends only on temperature; the equilibrium constant $K^{\mathrm{c}}$ expressed in equilibrium concentrations is called the **concentration constant**, and it depends on ionic strength as well; and the constant $K^{\mathrm{M}}$ in which $\ce{H+}$ is expressed as an activity and the other species as concentrations is called the **mixed constant**.

The $K_{\mathrm{a}}$, $K_{\mathrm{sp}}$, and $\beta_n$ in handbooks are generally activity constants for $I \to 0$, or concentration constants with a stated ionic strength (such as $I = 0.1$). The mixed constant is significant because a pH meter measures $a_{\ce{H+}}$ ([9.2.2](/6.1.9#sec-9.2.2)), whereas conservation of amount of substance in titration calculations is expressed with concentrations. A concentration constant is a constant only when both temperature and ionic strength are fixed.

**Example 2.2.2** (1) The mean activity coefficients $\gamma_\pm$ in $0.500\,\mathrm{mol\,L^{-1}}$ and $0.010\,\mathrm{mol\,L^{-1}}$ HCl are 0.757 and 0.904 respectively; find the pH of the two solutions. (2) Find $\mathrm{p}K_{\mathrm{a}}^{\mathrm{c}}$ of acetic acid at $25\,^\circ\mathrm{C}$ and $I = 0.10$.

**Solution** (1) $\mathrm{pH} = -\lg(0.757\times0.500) = 0.42$, compared with 0.30 from the concentration; $\mathrm{pH} = -\lg(0.904\times0.010) = 2.04$, compared with 2.00. The higher the concentration, the larger the activity correction. (2) With the Davies equation, at $I = 0.10$ a univalent ion has $\lg\gamma = -0.509\times\left(\frac{0.316}{1.316} - 0.030\right) = -0.107$; HAc is a neutral molecule with $\gamma \approx 1$, so

$$
\mathrm{p}K_{\mathrm{a}}^{\mathrm{c}} = \mathrm{p}K_{\mathrm{a}}^\circ + \lg\gamma_{\ce{H+}} + \lg\gamma_{\ce{Ac-}} = 4.76 - 0.21 = 4.55.
$$
An ionic strength of 0.1 lowers $\mathrm{p}K_{\mathrm{a}}$ by about 0.2, and the effect is larger for equilibria involving divalent ions ($\lg\gamma$ is four times that of a univalent ion). $\square$

Calculations for acid–base titrations generally neglect activities: a difference of about 0.2 in $\mathrm{p}K$ shifts the pH at the stoichiometric point by only a few tenths and has little effect on the choice of indicator or the estimate of the end-point error. Activities must be considered when calculating or preparing buffer solutions with a definite pH (especially pH standard buffers, 2.4), in solutions of high ionic strength, when ion activities are measured with ion-selective electrodes ([6.4.6](/6.4.6#sec-6.3)), and when thermodynamic constants are derived from measured pH.

## 2.3. Quantitative Treatment of Acid–Base Equilibria

### 2.3.1. Dissociation Constants of Conjugate Acid–Base Pairs

By the **Brønsted–Lowry theory** the dissociation constants of a **conjugate acid–base pair** satisfy $K_{\mathrm{a}}K_{\mathrm{b}} = K_{\mathrm{w}}$ ([Eq. (9.1)](/6.1.9#eq-9.1)). For an $n$-protic acid $\ce{H_nA}$ its successive conjugate bases are paired in reverse order:

$$
K_{\mathrm{a}i}\,K_{\mathrm{b}(n+1-i)} = K_{\mathrm{w}}, \qquad i = 1, \dots, n.
$$
For example, $K_{\mathrm{a}1}$ of $\ce{H3PO4}$ corresponds to $K_{\mathrm{b}3}$ of the weakest conjugate base, $\ce{H2PO4-}$; and for $\ce{HPO4^2-}$ acting as a base (accepting a proton to become $\ce{H2PO4-}$), $\mathrm{p}K_{\mathrm{b}2} = 14.00 - \mathrm{p}K_{\mathrm{a}2} = 14.00 - 7.21 = 6.79$. The constants in this chapter are taken from the CRC Handbook ($25\,^\circ\mathrm{C}$, $I \to 0$) and agree with the table of [6.1.9](/6.1.9#sec-9.3.1): $\ce{H3PO4}$ 2.16, 7.21, 12.32; $\ce{H2CO3}$ 6.35, 10.33; HAc 4.76; $\ce{NH4+}$ 9.25; $\ce{H3BO3}$ 9.27; phthalic acid 2.94, 5.43.

### 2.3.2. Analytical Concentration, Equilibrium Concentration, and Distribution Fractions

**Definition 2.3.1** The sum of the concentrations of all forms in which a solute occurs in solution, that is, the concentration calculated from the amount added in preparing the solution, is called the **analytical concentration**, denoted $c$; the concentration of one particular form (species) in solution at equilibrium is called the **equilibrium concentration**, denoted $[\ ]$.

The two are related by the **distribution fraction** $\delta$ ([6.1.9](/6.1.9#sec-9.3.6)): $[\text{species}] = \delta\cdot c$. For an $n$-protic acid $\ce{H_nA}$, denote the distribution fraction of the species $\ce{H}_{n-j}\mathrm{A}^{j-}$ that has lost $j$ protons by $\delta_j$ ($j = 0, 1, \dots, n$). Eliminating successively with the expressions for the $K_{\mathrm{a}i}$ gives

$$
\delta_j = \frac{[\ce{H+}]^{n-j}\prod_{i=1}^{j}K_{\mathrm{a}i}}{\sum_{k=0}^{n}[\ce{H+}]^{n-k}\prod_{i=1}^{k}K_{\mathrm{a}i}}, \tag{2.4}
$$
where an empty product is taken as 1. For $n = 3$, for example, the denominator is $[\ce{H+}]^3 + K_{\mathrm{a}1}[\ce{H+}]^2 + K_{\mathrm{a}1}K_{\mathrm{a}2}[\ce{H+}] + K_{\mathrm{a}1}K_{\mathrm{a}2}K_{\mathrm{a}3}$, and the numerators are its four terms in turn. (Many textbooks number $\delta$ by the number of protons the species contains, so that $\delta_3$ refers to $\ce{H3PO4}$, the opposite of the convention here; keep this in mind when reading.) From Eq. (2.4): $\sum_j\delta_j = 1$; $\delta$ is a function of $[\ce{H+}]$ and the $K_{\mathrm{a}}$ only, and does not depend on the analytical concentration $c$; and the distribution fractions of two neighboring species are equal at $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}i}$. The three $\mathrm{p}K_{\mathrm{a}}$ of $\ce{H3PO4}$ differ by about 5 units, so different species coexist only slightly: at $\mathrm{pH} = 4.7$, $\delta(\ce{H2PO4-}) = 0.994$ and each of the other two is about 0.003; at $\mathrm{pH} = 9.8$, $\delta(\ce{HPO4^2-}) = 0.994$. This is why phosphoric acid can be titrated stepwise (2.6; the lower half of the figure shows exactly how these distribution fractions change during the titration).

### 2.3.3. Mass Balance, Charge Balance, and Proton Condition

For the definitions of the **mass balance**, the **charge balance**, and the **proton condition**, and the example of $\ce{NaHCO3}$, see [6.1.9](/6.1.9#sec-9.4.3). The proton condition can be obtained by subtracting the charge balance from the mass balance; a more direct way is the reference-level method:

1. Choose as the reference level the starting species that are present in large amounts and take part in proton transfer (including the solvent water);
2. Find all species that have more protons than the reference level and all species that have fewer;
3. The total amount of protons gained equals the total amount lost, with the concentration of each species multiplied by the number of protons by which it differs from the reference level.

**Example 2.3.1** Write the proton conditions of aqueous solutions of $\ce{Na2CO3}$, $\ce{Na2HPO4}$, and $\ce{NH4HCO3}$.

**Solution** $\ce{Na2CO3}$: the reference levels are $\ce{CO3^2-}$ and $\ce{H2O}$; the species that gain protons are $\ce{HCO3-}$ (one), $\ce{H2CO3}$ (two), and $\ce{H3O+}$, and the species that lose a proton is $\ce{OH-}$, so the proton condition is $[\ce{H+}] + [\ce{HCO3-}] + 2[\ce{H2CO3}] = [\ce{OH-}]$. $\ce{Na2HPO4}$: the reference levels are $\ce{HPO4^2-}$ and $\ce{H2O}$, and $[\ce{H+}] + [\ce{H2PO4-}] + 2[\ce{H3PO4}] = [\ce{PO4^3-}] + [\ce{OH-}]$. $\ce{NH4HCO3}$: the reference levels are $\ce{NH4+}$, $\ce{HCO3-}$, and $\ce{H2O}$, and $[\ce{H+}] + [\ce{H2CO3}] = [\ce{NH3}] + [\ce{CO3^2-}] + [\ce{OH-}]$. The $\ce{Na+}$ ion, which takes no part in proton transfer, does not appear in the proton condition. $\square$

### 2.3.4. Exact Formulas for pH and Criteria for Approximations

Expressing each species through $[\ce{H+}]$ and the distribution fractions and substituting into the proton condition gives an exact equation for $[\ce{H+}]$. For a monoprotic weak acid of concentration $c$, the proton condition $[\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ gives

$$
[\ce{H+}] = \frac{K_{\mathrm{a}}c}{[\ce{H+}] + K_{\mathrm{a}}} + \frac{K_{\mathrm{w}}}{[\ce{H+}]}, \qquad [\ce{H+}]^3 + K_{\mathrm{a}}[\ce{H+}]^2 - (K_{\mathrm{a}}c + K_{\mathrm{w}})[\ce{H+}] - K_{\mathrm{a}}K_{\mathrm{w}} = 0. \tag{2.5}
$$
If a relative error of 5% is allowed in the result, two approximations can be made:

1. If $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$, the dissociation of water can be neglected (the $K_{\mathrm{w}}$ term that is dropped is no more than 5% of the retained terms), and Eq. (2.5) reduces to the quadratic equation of 6.1.9, $[\ce{H+}]^2 + K_{\mathrm{a}}[\ce{H+}] - K_{\mathrm{a}}c = 0$;
2. If $c/K_{\mathrm{a}} \ge 105$, the acid dissociates very little, $[\ce{HA}] \approx c$, and $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c + K_{\mathrm{w}}}$;
3. When both conditions are satisfied one obtains the simplest formula $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c}$.

The 105 in the criterion is exactly the value of $c/K_{\mathrm{a}}$ at which the relative error of the simplest formula is 5%: [6.1.9](/6.1.9#sec-9.3.2) showed that the error of the simplest formula is about $1/(2\sqrt{c/K_{\mathrm{a}}})$, and the exact solution of $\sqrt r/\bigl(\tfrac12(\sqrt{1+4r} - 1)\bigr) - 1 = 0.05$ gives $r = c/K_{\mathrm{a}} = 104.9$. Section 6.1.9 adopted the stricter $c/K_{\mathrm{a}} \ge 400$ (error 2.5%); the two are just different conventions for the permitted error.

**Example 2.3.2** Calculate the pH of a $1.0\times10^{-4}\,\mathrm{mol\,L^{-1}}$ solution of $\ce{H3BO3}$ ($\mathrm{p}K_{\mathrm{a}} = 9.27$).

**Solution** $K_{\mathrm{a}}c = 10^{-13.27} = 5.4\times10^{-14} < 20K_{\mathrm{w}}$, so the dissociation of water cannot be neglected; $c/K_{\mathrm{a}} = 10^{5.27} \gg 105$, so $[\ce{HA}] \approx c$. Therefore

$$
[\ce{H+}] = \sqrt{K_{\mathrm{a}}c + K_{\mathrm{w}}} = \sqrt{5.4\times10^{-14} + 1.0\times10^{-14}} = 2.5\times10^{-7}, \qquad \mathrm{pH} = 6.60.
$$
The simplest formula, wrongly applied, gives $\mathrm{pH} = 6.64$, with $[\ce{H+}]$ about 8% too low. $\square$

For the amphoteric species $\ce{NaHA}$ (concentration $c$) the proton condition $[\ce{H+}] + [\ce{H2A}] = [\ce{A^2-}] + [\ce{OH-}]$ gives the exact formula

$$
[\ce{H+}] = \sqrt{\frac{K_{\mathrm{a}1}\bigl(K_{\mathrm{a}2}[\ce{HA-}] + K_{\mathrm{w}}\bigr)}{K_{\mathrm{a}1} + [\ce{HA-}]}}. \tag{2.6}
$$
When the tendencies of $\ce{HA-}$ to gain and lose protons are both weak, $[\ce{HA-}] \approx c$; if in addition $cK_{\mathrm{a}2} \ge 20K_{\mathrm{w}}$, the approximate formula is $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}c/(K_{\mathrm{a}1} + c)}$; and if also $c \ge 20K_{\mathrm{a}1}$, the simplest formula is $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$ ([Eq. (9.4)](/6.1.9#eq-9.4)), where the pH is independent of concentration.

**Example 2.3.3** Calculate the pH of a $0.10\,\mathrm{mol\,L^{-1}}$ solution of potassium hydrogen phthalate (KHP) and compare it with the NIST standard buffer ($0.05\,\mathrm{mol\,kg^{-1}}$ KHP, pH 4.005 at $25\,^\circ\mathrm{C}$).

**Solution** $\mathrm{p}K_{\mathrm{a}1} = 2.94$ and $\mathrm{p}K_{\mathrm{a}2} = 5.43$. Since $cK_{\mathrm{a}2} = 3.7\times10^{-7} \gg 20K_{\mathrm{w}}$ and $c/K_{\mathrm{a}1} = 87 > 20$, the simplest formula applies: $\mathrm{pH} = \frac12(2.94 + 5.43) = 4.19$ (the exact formula gives the same value).

This is 0.18 higher than the standard value, because of activity. In a KHP solution $I \approx c$. A rigorous treatment with activity constants gives $K_{\mathrm{a}1}^\circ = \dfrac{a_{\ce{H+}}\gamma_1[\ce{HA-}]}{[\ce{H2A}]}$ and $K_{\mathrm{a}2}^\circ = \dfrac{a_{\ce{H+}}\gamma_2[\ce{A^2-}]}{\gamma_1[\ce{HA-}]}$ ($\gamma_1$ and $\gamma_2$ are the activity coefficients of the univalent and divalent anions), and substituting into the proton condition $[\ce{H2A}] \approx [\ce{A^2-}]$ gives $a_{\ce{H+}}^2 = K_{\mathrm{a}1}^\circ K_{\mathrm{a}2}^\circ/\gamma_2$, that is,

$$
\mathrm{pH} = \tfrac12(\mathrm{p}K_{\mathrm{a}1}^\circ + \mathrm{p}K_{\mathrm{a}2}^\circ) + \tfrac12\lg\gamma_2.
$$
At $I = 0.05$ the Davies equation gives $\lg\gamma_2 = -0.34$, so $\mathrm{pH} = 4.19 - 0.17 = 4.01$, in agreement with the standard value. $\square$

**Example 2.3.4** In a saturated aqueous solution of $\ce{CO2}$ at room temperature $c(\ce{H2CO3}) \approx 0.040\,\mathrm{mol\,L^{-1}}$ (including dissolved $\ce{CO2}$); find the pH.

**Solution** Since $K_{\mathrm{a}1} \gg K_{\mathrm{a}2}$, the acid is treated as monoprotic; $cK_{\mathrm{a}1} \gg 20K_{\mathrm{w}}$ and $c/K_{\mathrm{a}1} = 9\times10^4 \gg 105$, so $[\ce{H+}] = \sqrt{0.040\times10^{-6.35}}$ and $\mathrm{pH} = 3.87$. This is the pH of the solution at the second stoichiometric point of the titration of a carbonate with HCl (2.6). $\square$

| System | Proton condition | Simplest formula | Conditions (error ≤ 5%) |
|---|---|---|---|
| Monoprotic weak acid HA | $[\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ | $[\ce{H+}] = \sqrt{K_{\mathrm{a}}c}$ | $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$, $c/K_{\mathrm{a}} \ge 105$ |
| Polyprotic weak acid $\ce{H2A}$ | $[\ce{H+}] = [\ce{HA-}] + 2[\ce{A^2-}] + [\ce{OH-}]$ | Same, with $K_{\mathrm{a}1}$ | Also $K_{\mathrm{a}1} \gg K_{\mathrm{a}2}$ (second dissociation neglected) |
| Amphoteric species $\ce{HA-}$ | $[\ce{H+}] + [\ce{H2A}] = [\ce{A^2-}] + [\ce{OH-}]$ | $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$ | $cK_{\mathrm{a}2} \ge 20K_{\mathrm{w}}$, $c \ge 20K_{\mathrm{a}1}$ |
| Buffer solution HA–$\ce{A-}$ | See 2.4 | $[\ce{H+}] = K_{\mathrm{a}}c_{\mathrm{a}}/c_{\mathrm{b}}$ | $c_{\mathrm{a}}, c_{\mathrm{b}} \gg [\ce{H+}], [\ce{OH-}]$ |
| Monoprotic and polyprotic weak bases | As above, with $\ce{H+}$ and $\ce{OH-}$, $K_{\mathrm{a}}$ and $K_{\mathrm{b}}$ interchanged | | |

The value of these approximate formulas lies in estimation and understanding: they show which equilibrium dominates the pH and how it varies with the quantities involved. When an accurate value is needed, or the system is complex (several acids and bases coexisting, or very dilute solutions), the present-day practice is to solve the charge balance numerically for the root ([4.4.4](/4.4.4#sec-4.2.2); 6.1.9 already gave an example in [9.6.2](/6.1.9#sec-9.6.2)). Writing Eq. (2.4) as a function, a short program handles an arbitrary mixture of acids and bases:

```python
import numpy as np
from scipy.optimize import brentq

Kw = 1.0e-14


def fractions(h, Ka):
    """Distribution fractions of H_nA, H_(n-1)A, ..., A at [H+] = h."""
    terms = np.cumprod(np.concatenate(([1.0], np.asarray(Ka) / h)))
    return terms / terms.sum()


def pH(acids, cation=0.0, anion=0.0):
    """acids: list of (total concentration, [Ka1, Ka2, ...], charge of the fully protonated form);
    cation, anion: concentrations of spectator ions such as Na+ and Cl- (charge units)."""
    def balance(p):
        h = 10.0 ** -p
        q = h - Kw / h + cation - anion
        for c, Ka, z0 in acids:
            d = fractions(h, Ka)
            q += c * np.dot(z0 - np.arange(len(d)), d)
        return q
    return brentq(balance, -2.0, 16.0, xtol=1e-12)    # solve in pH: [H+] spans many decades


print(pH([(0.10, [10**-2.94, 10**-5.43], 0)], cation=0.10))                    # KHP: 4.19
print(pH([(0.05, [10**-6.35, 10**-10.33], 0), (0.05, [10**-9.25], +1)]))       # NH4HCO3: 7.78
```

## 2.4. Buffer Solutions

### 2.4.1. The pH of a Buffer Solution

For the principle of the **buffer solution**, the derivation of the **Henderson–Hasselbalch equation** $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}} + \lg(c_{\mathrm{b}}/c_{\mathrm{a}})$, and of the **buffer capacity** (maximum $0.576c$ at $\mathrm{pH} = \mathrm{p}K_{\mathrm{a}}$, effective range $\mathrm{p}K_{\mathrm{a}} \pm 1$), see [6.1.9](/6.1.9#sec-9.5). The pH of a buffer solution depends on the concentration ratio of the conjugate acid–base pair and not on the total volume, so within limits the pH hardly changes on dilution; the buffer capacity, however, is proportional to the total concentration, and dilution lowers the buffering power.

The Henderson–Hasselbalch equation requires $c_{\mathrm{a}}, c_{\mathrm{b}} \gg [\ce{H+}], [\ce{OH-}]$. When this does not hold (very dilute buffers, or a large $K_{\mathrm{a}}$), the mass balance and charge balance give the exact formula

$$
[\ce{H+}] = K_{\mathrm{a}}\,\frac{c_{\mathrm{a}} - [\ce{H+}] + [\ce{OH-}]}{c_{\mathrm{b}} + [\ce{H+}] - [\ce{OH-}]}, \tag{2.7}
$$
in which $[\ce{OH-}]$ may be dropped in an acidic buffer and $[\ce{H+}]$ in a basic one. Besides weak acids and their conjugate bases, amphoteric species at fairly high concentration (such as potassium hydrogen phthalate and borax) and strong acids and bases at high concentration also buffer; the former are often used as pH standard buffers.

**Example 2.4.1** Dissolve 12.43 g of Tris (tris(hydroxymethyl)aminomethane, $M = 121.14\,\mathrm{g\,mol^{-1}}$) and 4.67 g of Tris hydrochloride ($M = 157.60\,\mathrm{g\,mol^{-1}}$) in water and make up to 1 L; find the pH. What is the pH after $12.0\,\mathrm{mL}$ of $1.00\,\mathrm{mol\,L^{-1}}$ HCl is added? ($25\,^\circ\mathrm{C}$, $\mathrm{p}K_{\mathrm{a}}(\ce{TrisH+}) = 8.07$)

**Solution** There are $0.1026\,\mathrm{mol}$ of Tris and $0.0296\,\mathrm{mol}$ of $\ce{TrisH+}$, so $\mathrm{pH} = 8.07 + \lg(0.1026/0.0296) = 8.61$. The $0.0120\,\mathrm{mol}$ of $\ce{H+}$ added converts an equal amount of Tris into $\ce{TrisH+}$; the two become 0.0906 and 0.0416 mol, so $\mathrm{pH} = 8.07 + \lg(0.0906/0.0416) = 8.41$, a decrease of only 0.20. The same HCl added to 1 L of pure water gives a pH of 1.93. $\square$

**Example 2.4.2** What amounts of concentrated ammonia ($14.8\,\mathrm{mol\,L^{-1}}$) and $\ce{NH4Cl}$ are needed to prepare 100 mL of a buffer of pH 10.00 with an $\ce{NH4Cl}$ concentration of $0.200\,\mathrm{mol\,L^{-1}}$?

**Solution** From $\mathrm{pH} = 9.25 + \lg([\ce{NH3}]/[\ce{NH4+}])$, $[\ce{NH3}]/[\ce{NH4+}] = 10^{0.75} = 5.62$ and $[\ce{NH3}] = 1.12\,\mathrm{mol\,L^{-1}}$. This requires $1.12\times100/14.8 = 7.6\,\mathrm{mL}$ of concentrated ammonia and $0.0200\times53.49 = 1.07\,\mathrm{g}$ of $\ce{NH4Cl}$. (At an ionic strength of 0.2 the actual pH will be somewhat lower; for an exact preparation, adjust with a pH meter.) $\square$

**Example 2.4.3** What masses of $\ce{NaH2PO4}$ and $\ce{Na2HPO4}$ are needed to prepare 1 L of a phosphate buffer of ionic strength 0.100 and pH 7.45?

**Solution** Let $[\ce{H2PO4-}] = x$ and $[\ce{HPO4^2-}] = y$; then $[\ce{Na+}] = x + 2y$ and $I = \frac12\bigl[(x + 2y) + x + 4y\bigr] = x + 3y = 0.100$. The pH is the activity of $\ce{H+}$, so

$$
\mathrm{pH} = \mathrm{p}K_{\mathrm{a}2}^\circ + \lg\frac{\gamma_2 y}{\gamma_1 x}.
$$
At $I = 0.100$ the Davies equation gives $\lg\gamma_1 = -0.107$ and $\lg\gamma_2 = -0.428$, so $\lg(y/x) = 7.45 - 7.21 + 0.321 = 0.561$ and $y/x = 3.64$. Solving together with $x + 3y = 0.100$ gives $x = 8.39\,\mathrm{mmol\,L^{-1}}$ and $y = 30.5\,\mathrm{mmol\,L^{-1}}$; this requires $8.39\times10^{-3}\times119.98 = 1.007\,\mathrm{g}$ of $\ce{NaH2PO4}$ and $30.5\times10^{-3}\times141.96 = 4.34\,\mathrm{g}$ of $\ce{Na2HPO4}$. If no activity correction were made and the buffer were prepared with $y/x = 10^{0.24} = 1.74$, the actual pH would be about 7.13, a difference of 0.3: equilibria involving divalent ions are very sensitive to ionic strength. $\square$

### 2.4.2. Common Buffers and pH Standard Buffers

The principle in choosing a buffer system is that $\mathrm{p}K_{\mathrm{a}}$ should be as close as possible to the pH required, and the buffering substance should not react with other components of the system. Common buffering substances ($25\,^\circ\mathrm{C}$, CRC):

| Buffering substance | $\mathrm{p}K_{\mathrm{a}}$ | Buffering substance | $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|
| Aminoacetic acid (glycine) | 2.34, 9.60 | Hexamethylenetetramine (conjugate acid) | 5.15 |
| Chloroacetic acid | 2.87 | Carbonic acid | 6.35, 10.33 |
| Formic acid | 3.75 | Phosphoric acid | 2.16, 7.21, 12.32 |
| Citric acid | 3.13, 4.76, 6.40 | Triethanolamine (conjugate acid) | 7.76 |
| Succinic acid | 4.21, 5.64 | Tris (conjugate acid) | 8.07 |
| Acetic acid | 4.76 | Boric acid | 9.27 |
| | | Ammonia ($\ce{NH4+}$) | 9.25 |

The pH of the standard buffers used to calibrate pH meters is not calculated from the Henderson–Hasselbalch equation but is a conventional value determined with cells without liquid junction and including activity corrections (IUPAC 2002, $25\,^\circ\mathrm{C}$):

| Standard buffer | pH |
|---|---|
| Saturated potassium hydrogen tartrate (about $0.034\,\mathrm{mol\,kg^{-1}}$) | 3.557 |
| Potassium hydrogen phthalate, $0.05\,\mathrm{mol\,kg^{-1}}$ | 4.005 |
| $\ce{KH2PO4}$ and $\ce{Na2HPO4}$, each $0.025\,\mathrm{mol\,kg^{-1}}$ | 6.865 |
| Borax, $0.01\,\mathrm{mol\,kg^{-1}}$ | 9.180 |
| Saturated $\ce{Ca(OH)2}$ | 12.454 |

### 2.4.3. Physiological and Biochemical Buffers

The pH of blood is held at 7.35–7.45, mainly by the open $\ce{CO2}$–$\ce{HCO3-}$ system (apparent $\mathrm{p}K_{\mathrm{a}}' = 6.1$ at $37\,^\circ\mathrm{C}$); for its calculation and physiological regulation see the example of [6.1.9](/6.1.9#sec-9.5.4). In addition, the imidazole groups of histidine in plasma proteins and hemoglobin, and the terminal amino and carboxyl groups, are also effective buffers. A pH below 7.35 is called acidosis (for example, diabetic ketoacidosis and respiratory failure) and a pH above 7.45 alkalosis. Clinically the pH of blood and the partial pressure of $\ce{CO2}$ or the total $\ce{CO2}$ are measured (2.8), and the type of acid–base imbalance is judged from the Henderson–Hasselbalch equation.

Buffers for biochemical experiments must take account not only of pH but also of ionic strength, temperature, and interactions with metal ions and biomolecules:

- Phosphate buffer: $\mathrm{p}K_{\mathrm{a}2} = 7.21$, the closest to physiological pH, with a buffering range of 6.2–8.2 and a very small temperature coefficient. The commonly used phosphate-buffered saline (PBS) contains $137\,\mathrm{mmol\,L^{-1}}$ NaCl, $2.7\,\mathrm{mmol\,L^{-1}}$ KCl, $10\,\mathrm{mmol\,L^{-1}}$ $\ce{Na2HPO4}$, and $1.8\,\mathrm{mmol\,L^{-1}}$ $\ce{KH2PO4}$ at pH 7.4, and is isotonic with body fluids. Its disadvantages are that it forms precipitates with $\ce{Ca^2+}$ and $\ce{Mg^2+}$ and inhibits some enzymes (kinases, phosphatases). As Example 2.4.3 shows, the pH of a phosphate buffer is sensitive to ionic strength, and adding salt or diluting changes it.
- Tris buffer: $\mathrm{p}K_{\mathrm{a}} = 8.07$ ($25\,^\circ\mathrm{C}$), with a buffering range of about 7.1–9.1. It is very soluble, not hygroscopic, absorbs almost no $\ce{CO2}$, does not precipitate $\ce{Ca^2+}$, and does not interfere with most enzymes. It has three disadvantages: the temperature coefficient of $\mathrm{p}K_{\mathrm{a}}$ is large (about $-0.028\,\mathrm{K^{-1}}$), so a solution made to pH 8.0 at $25\,^\circ\mathrm{C}$ has a pH of about 7.7 at $37\,^\circ\mathrm{C}$ and about 8.6 at $4\,^\circ\mathrm{C}$, and the pH should therefore be adjusted at the temperature of use; the buffer capacity decreases rapidly below pH 7.5; and it is a primary amine that reacts with aldehydes and active esters (such as the NHS esters used to label proteins) and can coordinate some metal ions.

These shortcomings of Tris led Good and coworkers (1966) to design a series of zwitterionic buffers systematically.

**Definition 2.4.1 (Good's Buffers)** A class of zwitterionic buffers designed for biological research to the following requirements is called **Good's buffers**: $\mathrm{p}K_{\mathrm{a}}$ between 6 and 8; high water solubility and low permeability through biological membranes; little influence of concentration, ionic strength, and temperature; weak coordination to metal ions; chemical and enzymatic stability; no absorption of ultraviolet–visible light above 230 nm; and ease of preparation and purification.

They are mostly sulfonic-acid-containing amines (N-substituted taurines, or morpholine and piperazine derivatives) and exist as zwitterions at the pH they buffer (2.8.3). The structures are, in order, Tris (1), MES (2), MOPS (3), and HEPES (4):

```smiles
NC(CO)(CO)CO 1
[O-]S(=O)(=O)CC[NH+]1CCOCC1 2
[O-]S(=O)(=O)CCC[NH+]1CCOCC1 3
OCCN1CC[NH+](CCS(=O)(=O)[O-])CC1 4
```

| Buffer | $\mathrm{p}K_{\mathrm{a}}$ ($25\,^\circ\mathrm{C}$) | $\mathrm{d}\,\mathrm{p}K_{\mathrm{a}}/\mathrm{d}T$ / $\mathrm{K^{-1}}$ | Buffering range |
|---|---|---|---|
| MES | 6.27 | $-0.011$ | 5.5–6.7 |
| PIPES | 7.14 | $-0.008$ | 6.1–7.5 |
| MOPS | 7.18 | $-0.011$ | 6.5–7.9 |
| HEPES | 7.56 | $-0.014$ | 6.8–8.2 |
| Tris | 8.07 | $-0.028$ | 7.1–9.1 |
| Phosphate ($\mathrm{p}K_{\mathrm{a}2}$) | 7.21 | $-0.003$ | 6.2–8.2 |

(The $\mathrm{p}K_{\mathrm{a}}$ are thermodynamic values for $I \to 0$ taken from the critically evaluated data of NIST; values such as HEPES 7.5 and MES 6.1 often found in the literature are values at $20\,^\circ\mathrm{C}$ or at a given ionic strength.) HEPES is used in cell culture media, MOPS in denaturing gel electrophoresis of RNA, and MES in protein chromatography near pH 6. Good's buffers are not completely inert either: piperazine-type buffers (HEPES, PIPES) generate free radicals under illumination, and HEPES interferes with the Folin–Lowry method for proteins.

## 2.5. Acid–Base Indicators

### 2.5.1. Principle of Color Change and Transition Range

An **acid–base indicator** is an organic weak acid or weak base whose acid form and base form have different colors; the color of the solution depends on $[\ce{In-}]/[\ce{HIn}] = K_{\mathrm{HIn}}/[\ce{H+}]$, and the theoretical **transition range** is $\mathrm{pH} = \mathrm{p}K_{\mathrm{HIn}} \pm 1$. For the structural changes of phenolphthalein (colorless lactone form ⇌ red quinoid form) and methyl orange (yellow azo form ⇌ red quinoid form) see [6.1.9](/6.1.9#sec-9.2.3). The actual transition range is determined by eye and often deviates from $\mathrm{p}K_{\mathrm{HIn}} \pm 1$, because the human eye is differently sensitive to different colors: the red of methyl orange is more conspicuous than the yellow, and the solution looks red as soon as the red component is about twice the yellow one, so the acidic end of the transition range is only 0.3 below $\mathrm{p}K_{\mathrm{HIn}}$.

| Indicator | $\mathrm{p}K_{\mathrm{HIn}}$ | Transition range | Acid color → base color |
|---|---|---|---|
| Methyl orange | 3.4 | 3.1–4.4 | Red → yellow |
| Bromophenol blue | 4.1 | 3.0–4.6 | Yellow → purple |
| Bromocresol green | 4.9 | 3.8–5.4 | Yellow → blue |
| Methyl red | 5.0 | 4.4–6.2 | Red → yellow |
| Bromothymol blue | 7.1 | 6.0–7.6 | Yellow → blue |
| Phenol red | 7.9 | 6.8–8.4 | Yellow → red |
| Phenolphthalein | 9.1 | 8.2–10.0 | Colorless → red |
| Thymolphthalein | 10.0 | 9.4–10.6 | Colorless → blue |

(The transition range of phenolphthalein is given in different handbooks as 8.0–10.0, 8.0–9.6, or 8.2–10.0; we take 8.2–10.0.) The narrower the transition range, the sharper the end point.

### 2.5.2. Mixed Indicators

**Definition 2.5.1 (Mixed Indicator)** An indicator made by mixing, in a definite proportion, two indicators, or an indicator and a dye whose color does not change with pH, so that complementary colors narrow the transition range and make the color change sharper, is called a **mixed indicator**.

The most common is bromocresol green–methyl red: below pH 5.1 the acid colors of the two (yellow and red) combine to wine red; at pH 5.1 the two colors are complementary and the solution looks gray; and a slightly higher pH turns it green (the blue of bromocresol green with the yellow of methyl red). The end point is only about 0.2 pH unit wide, and the indicator is used for the standardization of HCl with $\ce{Na2CO3}$ and for the titration of the boric acid absorbing solution in the Kjeldahl method (2.8). A mixture of methyl orange and sodium indigo disulfonate (a dye) is of the same kind. Mixing several indicators with different transition ranges gives the universal indicators and pH papers, which change color gradually over the whole pH range.

### 2.5.3. Factors Affecting the Color Change

1. Amount of indicator. The color of a two-color indicator (methyl orange, methyl red) depends only on $[\ce{In-}]/[\ce{HIn}]$ and not on the indicator concentration, but too much indicator makes the color deep and the change less sharp, and the indicator itself consumes titrant. A one-color indicator (phenolphthalein) is colored only in its base form: let $a$ be the lowest concentration at which the eye can see the color; in the region $\mathrm{pH} < \mathrm{p}K_{\mathrm{HIn}}$, $[\ce{In-}] = c_{\ce{HIn}}K_{\mathrm{HIn}}/([\ce{H+}] + K_{\mathrm{HIn}}) \approx c_{\ce{HIn}}K_{\mathrm{HIn}}/[\ce{H+}]$, and the pH at which color first appears is

$$
\mathrm{pH}_{\text{change}} = \mathrm{p}K_{\mathrm{HIn}} + \lg\frac{a}{c_{\ce{HIn}}},
$$
so a tenfold increase of the indicator concentration lowers the transition point by 1 pH unit. In 50–100 mL of solution, 2–3 drops of phenolphthalein change color at about pH 9, and 15–20 drops at about pH 8.
2. Temperature. Temperature changes $K_{\mathrm{HIn}}$ and $K_{\mathrm{w}}$, and the transition range shifts accordingly; titrations are generally carried out at room temperature, and when heating is needed (for example, boiling to remove $\ce{CO2}$) the solution must be cooled before the end point is reached.
3. Solvent and ionic strength. Organic solvents and large amounts of neutral salts change $\mathrm{p}K_{\mathrm{HIn}}$ (2.2) and the absorption of light by the solution.
4. Order of titration. A change in color from light to dark is easier to see than one from dark to light: phenolphthalein (colorless → red) is used when NaOH titrates an acid, and methyl orange (yellow → orange) when HCl titrates a base.

## 2.6. Acid–Base Titration Curves and the Feasibility of Titration

### 2.6.1. Titration of Monoprotic Acids and Bases

For the **titration curves** of the titration of strong and weak acids with strong bases, the calculation of the **titration jump**, and the choice of indicators, see [6.1.9](/6.1.9#sec-9.6.2): the jump for $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH titrating HCl of the same concentration is 4.30–9.70, and for titrating HAc it is 7.76–9.70, with the stoichiometric point at pH 8.73. The principle of choosing an indicator is that its transition range should lie wholly or partly within the jump, and within this condition the closer its transition point to the stoichiometric point the better. We add a few regularities here.

- Strong acid with strong base: each tenfold decrease in concentration shrinks the jump by 1 pH unit at each end, 2 units in all ($1.000\,\mathrm{mol\,L^{-1}}$: 3.30–10.70; $0.01000\,\mathrm{mol\,L^{-1}}$: 5.30–8.70). Concentration is the only factor that determines the size of the jump.
- Weak acid: before the stoichiometric point the solution is a buffer region, and the beginning of the jump, $\mathrm{pH} \approx \mathrm{p}K_{\mathrm{a}} + 3$ (0.1% of the acid remaining), depends only on $K_{\mathrm{a}}$; after the stoichiometric point the curve is the same as for a strong acid and depends on the concentration. Hence each tenfold decrease in $K_{\mathrm{a}}$ or in concentration shrinks the jump by about 1 unit, and the size of the jump is determined by $cK_{\mathrm{a}}$ (figure below). Only indicators that change color in the basic region (phenolphthalein, thymolphthalein) can be used, and methyl orange cannot be used at all.

![Titration of a monoprotic weak acid with NaOH of the same concentration. Left: c = 0.1000 mol/L, different pKa; right: pKa = 7, different concentrations. The gray band marks ±0.1% around the stoichiometric point](./plots/weak-acid-feasibility.py)

The figure shows that when $c_{\mathrm{sp}}K_{\mathrm{a}}$ ($c_{\mathrm{sp}}$ is the analytical concentration of the weak acid at the stoichiometric point) falls to about $10^{-9}$, the jump is already too small to see. From the end-point error formula, 2.7 will give the criterion for accurate titration:

$$
c_{\mathrm{sp}}K_{\mathrm{a}} \ge 10^{-8} \quad(\text{weak acid}), \qquad c_{\mathrm{sp}}K_{\mathrm{b}} \ge 10^{-8} \quad(\text{weak base}). \tag{2.8}
$$
It assumes that the uncertainty in locating the end point is $\pm0.2$ pH unit (the limit of the eye in judging the color of an indicator) and that the permitted end-point error is $\pm0.1\%$. Acids with too small a $K_{\mathrm{a}}$ (such as $\ce{H3BO3}$ and $\ce{NH4+}$) cannot be titrated directly, but they can be strengthened: $\ce{H3BO3}$ forms a complex acid with polyols such as mannitol or glycerol with $\mathrm{p}K_{\mathrm{a}}$ of about 4–5, which can then be titrated with NaOH; $\ce{NH4+}$ reacts with formaldehyde to liberate an equivalent amount of $\ce{H+}$ (the formaldehyde method), or it can be titrated in a nonaqueous solvent.

The titration of a weak base with a strong acid is symmetric. When $0.1000\,\mathrm{mol\,L^{-1}}$ HCl titrates $\ce{NH3}$ of the same concentration, the stoichiometric point is a $0.05000\,\mathrm{mol\,L^{-1}}$ solution of $\ce{NH4Cl}$ with $\mathrm{pH} = 5.28$, and the jump is 6.25–4.30; methyl red (or bromocresol green–methyl red) is used as the indicator, whereas methyl orange lies farther from the stoichiometric point.

### 2.6.2. Titration of Polyprotic Acids

The titration of a polyprotic acid has to answer two questions: whether the $\ce{H+}$ of each dissociation step can be titrated accurately, and whether the steps can be titrated stepwise (the second step begins to be neutralized only after the first has been completely neutralized, so that separate jumps appear on the titration curve). From the derivation of 2.7, the usual criterion for accurate stepwise titration of step $i$ is

$$
c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9} \quad\text{and}\quad \frac{K_{\mathrm{a}i}}{K_{\mathrm{a}(i+1)}} \ge 10^4; \tag{2.9}
$$
the ratio condition corresponds to $\Delta\mathrm{pH} = \pm0.2$ and an end-point error of $\pm1\%$; $c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9}$ corresponds to $\Delta\mathrm{pH} = \pm0.3$ and an error of $\pm0.5\%$ (if only $\pm1\%$ is required, $10^{-10}$ already suffices, and $10^{-9}$ leaves a margin). For a permitted error of $\pm0.5\%$ the ratio required is about $10^5$. When only the total amount is to be determined, Eq. (2.8) is applied to the weakest step $K_{\mathrm{a}n}$. For polyprotic bases, $K_{\mathrm{a}}$ is replaced by $K_{\mathrm{b}}$.

**Example 2.6.1** $20.00\,\mathrm{mL}$ of $0.1000\,\mathrm{mol\,L^{-1}}$ $\ce{H3PO4}$ is titrated with $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH. Decide whether stepwise titration is possible, calculate the pH at each stoichiometric point, and choose indicators.

**Solution** $K_{\mathrm{a}1}/K_{\mathrm{a}2} = 10^{5.05}$ and $K_{\mathrm{a}2}/K_{\mathrm{a}3} = 10^{5.11}$, both greater than $10^4$; at the first stoichiometric point $c_{\mathrm{sp}} = 0.050$ and $c_{\mathrm{sp}}K_{\mathrm{a}1} \gg 10^{-9}$; at the second, $c_{\mathrm{sp}} = 0.033$ and $c_{\mathrm{sp}}K_{\mathrm{a}2} = 2\times10^{-9} > 10^{-9}$; but $c_{\mathrm{sp}}K_{\mathrm{a}3} \approx 1.6\times10^{-14}$, so the third step cannot be titrated directly. The first two steps can therefore be titrated stepwise, and two jumps appear.

The solution at the first stoichiometric point is $0.0500\,\mathrm{mol\,L^{-1}}$ $\ce{NaH2PO4}$. Since $c/K_{\mathrm{a}1} = 7.2$ does not satisfy $c \ge 20K_{\mathrm{a}1}$, the approximate formula of Eq. (2.6), $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}c/(K_{\mathrm{a}1} + c)}$, must be used, giving $\mathrm{pH} = 4.71$ (the simplest formula gives 4.69). Methyl orange (titrated to yellow) or the mixed indicator bromocresol green–methyl orange can be used. The solution at the second stoichiometric point is $0.0333\,\mathrm{mol\,L^{-1}}$ $\ce{Na2HPO4}$; $cK_{\mathrm{a}3} = 1.6\times10^{-14}$ is comparable with $K_{\mathrm{w}}$, so the dissociation of water cannot be neglected, and Eq. (2.6) gives $[\ce{H+}] = \sqrt{K_{\mathrm{a}2}(K_{\mathrm{a}3}c + K_{\mathrm{w}})/c}$ and $\mathrm{pH} = 9.66$ (the 9.77 from the simplest formula is too high). Thymolphthalein (colorless → pale blue) or the mixed indicator phenolphthalein–thymolphthalein can be used; phenolphthalein alone gives an end point that is too early. The pH changes of $\pm1\%$ around the stoichiometric points are 4.17–5.25 and 9.16–10.16, only about 1 unit, so both jumps can reach an accuracy of only about $\pm0.5\%$. The $\ce{H+}$ of the third step can be titrated after $\ce{CaCl2}$ is added to precipitate $\ce{Ca3(PO4)2}$ and release $\ce{H+}$. $\square$

![Titration of H₃PO₄ with NaOH (each 0.1000 mol/L; CRC constants, computed numerically from the charge balance). Top: titration curve and the two stoichiometric points; bottom: distribution fractions of the four species during the titration](./plots/phosphoric-acid-titration.py)

### 2.6.3. Titration of Polyprotic Bases and the Double-Indicator Method

In the titration of $\ce{Na2CO3}$ with HCl, $K_{\mathrm{b}1} = K_{\mathrm{w}}/K_{\mathrm{a}2} = 10^{-3.67}$ for $\ce{CO3^2-}$ and $K_{\mathrm{b}2} = K_{\mathrm{w}}/K_{\mathrm{a}1} = 10^{-7.65}$ for $\ce{HCO3-}$, so $K_{\mathrm{b}1}/K_{\mathrm{b}2} = 10^{3.98}$, slightly less than $10^4$. The curve is very flat near the first stoichiometric point ($\ce{NaHCO3}$, pH 8.34), where the pH changes by only 0.4 unit for $\pm1\%$ around the stoichiometric point (inset of the figure below). The first step therefore cannot be titrated accurately and stepwise: with phenolphthalein (titrating to colorless) or the mixed indicator cresol red–thymol blue (pH 8.3) an accuracy of only about $\pm1\%$ is attainable. The second stoichiometric point is a saturated solution of $\ce{CO2}$ with a pH of about 3.9, and methyl orange (yellow → orange) is used as the indicator; since the $\ce{CO2}$ that accumulates in the solution makes the end point early and not sharp, it is better to use methyl red or bromocresol green–methyl red, titrate until the color changes, boil off the $\ce{CO2}$ (the solution returns to the base color), cool, and titrate again to the end point.

![Titration of 20.00 mL of 0.1000 mol/L Na₂CO₃ with 0.1000 mol/L HCl (closed system). The inset shows the pH within ±2% of the first stoichiometric point, where the change is very gradual](./plots/carbonate-titration.py)

**Definition 2.6.1 (Double-Indicator Method)** The method in which a single portion of the test solution is first titrated with phenolphthalein as indicator to the first end point (volume consumed $V_1$), then methyl orange is added and the titration continued to the second end point (a further volume $V_2$), and the composition of a mixed alkali is established and the content of each component calculated from the relation between $V_1$ and $V_2$, is called the **double-indicator method**.

At the phenolphthalein end point the $\ce{OH-}$ has been neutralized and $\ce{CO3^2-}$ has been converted to $\ce{HCO3-}$; at the methyl orange end point $\ce{HCO3-}$ has been converted to $\ce{CO2}$. Therefore:

| $V_1$ and $V_2$ | Composition | HCl consumed by each component |
|---|---|---|
| $V_1 > V_2 > 0$ | NaOH + $\ce{Na2CO3}$ | NaOH: $V_1 - V_2$; $\ce{Na2CO3}$: $2V_2$ |
| $V_2 > V_1 > 0$ | $\ce{Na2CO3}$ + $\ce{NaHCO3}$ | $\ce{Na2CO3}$: $2V_1$; $\ce{NaHCO3}$: $V_2 - V_1$ |
| $V_1 = V_2$ | $\ce{Na2CO3}$ | $2V_1$ |
| $V_1 = 0$ | $\ce{NaHCO3}$ | $V_2$ |
| $V_2 = 0$ | NaOH | $V_1$ |

**Example 2.6.2** A $0.2000\,\mathrm{g}$ sample of caustic soda is titrated with $0.1000\,\mathrm{mol\,L^{-1}}$ HCl; the phenolphthalein end point consumes $24.00\,\mathrm{mL}$, and after methyl orange is added a further $12.00\,\mathrm{mL}$ is consumed. Find the mass fractions of NaOH and $\ce{Na2CO3}$.

**Solution** Since $V_1 > V_2$, the sample contains NaOH and $\ce{Na2CO3}$. $n(\ce{Na2CO3}) = cV_2 = 1.200\,\mathrm{mmol}$ and $n(\ce{NaOH}) = c(V_1 - V_2) = 1.200\,\mathrm{mmol}$, so

$$
w(\ce{Na2CO3}) = \frac{1.200\times10^{-3}\times105.99}{0.2000} = 63.59\%, \qquad w(\ce{NaOH}) = \frac{1.200\times10^{-3}\times40.00}{0.2000} = 24.00\%.
$$
The double-indicator method is simple, but the first end point is not sharp and the error can reach about 1%. A more accurate method is the barium chloride method: one portion of the solution is titrated with methyl orange for the total alkali; to another portion $\ce{BaCl2}$ is added to precipitate $\ce{CO3^2-}$, and the remaining NaOH is titrated with phenolphthalein. $\square$

### 2.6.4. Titration of Mixed Acids

When two weak acids HA and HB ($K_{\mathrm{HA}} > K_{\mathrm{HB}}$) are mixed, the conditions for titrating them separately at a permitted error of $\pm1\%$ are similar to those for polyprotic acids: $c_{\mathrm{HA}}K_{\mathrm{HA}} \ge 10^{-9}$ and $c_{\mathrm{HA}}K_{\mathrm{HA}}/(c_{\mathrm{HB}}K_{\mathrm{HB}}) \ge 10^4$; if in addition $c_{\mathrm{HB}}K_{\mathrm{HB}} \ge 10^{-9}$, the weaker acid can also be titrated subsequently. The products of concentration and constant appear in the ratio condition because the two acids are independent, and the strength of their competition is determined by $cK$. For a mixture of a strong acid and a weak acid, if $K_{\mathrm{a}}$ of the weak acid is small enough (such as HCl with $\ce{NH4Cl}$, or HCl with $\ce{H3BO3}$), the strong acid can be titrated alone; if the weak acid is fairly strong (such as HCl with HAc), the first jump is very small and only the total can be titrated.

## 2.7. End-Point Error

### 2.7.1. The End-Point Error Formula

The **titration error** (end-point error) is denoted $E_{\mathrm{t}}$: it is the difference between the amount of titrant added at the end point and the amount required by the stoichiometry, expressed as a percentage of the amount of analyte, and a positive value means an excess of titrant. It arises because the end point does not coincide with the stoichiometric point and is a **systematic error** due to the method. We now derive its formula from the proton condition.

When NaOH of concentration $c$ is used to titrate HCl, $c_{\mathrm{ep}}(\ce{NaOH})$ and $c_{\mathrm{ep}}(\ce{HCl})$ in the solution at the end point are the analytical concentrations of the two, and the charge balance $[\ce{Na+}] + [\ce{H+}] = [\ce{Cl-}] + [\ce{OH-}]$ gives

$$
E_{\mathrm{t}} = \frac{c_{\mathrm{ep}}(\ce{NaOH}) - c_{\mathrm{ep}}(\ce{HCl})}{c_{\mathrm{ep}}(\ce{HCl})} = \frac{[\ce{OH-}]_{\mathrm{ep}} - [\ce{H+}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HCl})}. \tag{2.10}
$$
In the titration of a weak acid HA the charge balance is $[\ce{Na+}] + [\ce{H+}] = [\ce{A-}] + [\ce{OH-}]$ with $[\ce{A-}] = c_{\mathrm{ep}}(\ce{HA}) - [\ce{HA}]$; near the stoichiometric point the solution is basic and $[\ce{H+}]$ can be neglected:

$$
E_{\mathrm{t}} = \frac{[\ce{OH-}]_{\mathrm{ep}} - [\ce{HA}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HA})} = \frac{[\ce{OH-}]_{\mathrm{ep}}}{c_{\mathrm{ep}}(\ce{HA})} - \delta_{\ce{HA},\mathrm{ep}}. \tag{2.11}
$$
Equations (2.10) and (2.11) hold for any end point. When the end point is close to the stoichiometric point, expressing them through the difference between the pH at the end point and at the stoichiometric point, $\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{ep}} - \mathrm{pH}_{\mathrm{sp}}$, gives forms that are more convenient to use.

**Theorem 2.7.1 (End-Point Error Formula)** Let the end point be close to the stoichiometric point, let $c_{\mathrm{sp}}$ be the analytical concentration of the analyte at the stoichiometric point, and let $K_{\mathrm{t}}$ be the equilibrium constant of the titration reaction.

1. Strong base titrating strong acid ($K_{\mathrm{t}} = 1/K_{\mathrm{w}}$): $E_{\mathrm{t}} = \dfrac{10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}}{c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}}}$;
2. Strong base titrating a monoprotic weak acid ($\ce{HA + OH- -> A- + H2O}$, $K_{\mathrm{t}} = K_{\mathrm{a}}/K_{\mathrm{w}}$): $E_{\mathrm{t}} = \dfrac{10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}}{\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}}}$;
3. Diprotic acid $\ce{H2A}$ titrated to the first stoichiometric point ($c_{\mathrm{sp}}K_{\mathrm{a}2} \gg K_{\mathrm{w}}$, $c_{\mathrm{sp}} \gg K_{\mathrm{a}1}$): $E_{\mathrm{t}} = (10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}})\sqrt{K_{\mathrm{a}2}/K_{\mathrm{a}1}}$.

For the titration of a strong or weak base with a strong acid, replace $\Delta\mathrm{pH}$ by $-\Delta\mathrm{pH}$ and $K_{\mathrm{a}}$ by $K_{\mathrm{b}}$ in the formulas.

**Proof** (1) At the stoichiometric point $[\ce{H+}]_{\mathrm{sp}} = [\ce{OH-}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{w}}}$, so $[\ce{H+}]_{\mathrm{ep}} = \sqrt{K_{\mathrm{w}}}\,10^{-\Delta\mathrm{pH}}$ and $[\ce{OH-}]_{\mathrm{ep}} = \sqrt{K_{\mathrm{w}}}\,10^{\Delta\mathrm{pH}}$; since the end point is close to the stoichiometric point, $c_{\mathrm{ep}}(\ce{HCl}) \approx c_{\mathrm{sp}}$. Substitute into Eq. (2.10) and note that $\sqrt{K_{\mathrm{w}}} = 1/\sqrt{K_{\mathrm{t}}}$.

(2) At the stoichiometric point the solution is $\ce{A-}$ at $c_{\mathrm{sp}}$, with $[\ce{OH-}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{w}}c_{\mathrm{sp}}/K_{\mathrm{a}}}$; near it $[\ce{A-}] \approx c_{\mathrm{sp}}$ and $[\ce{HA}] = [\ce{H+}]c_{\mathrm{sp}}/K_{\mathrm{a}}$, so $[\ce{HA}]_{\mathrm{sp}} = \dfrac{K_{\mathrm{w}}}{[\ce{OH-}]_{\mathrm{sp}}}\cdot\dfrac{c_{\mathrm{sp}}}{K_{\mathrm{a}}} = [\ce{OH-}]_{\mathrm{sp}}$ (this is just the proton condition at the stoichiometric point). At the end point $[\ce{OH-}]_{\mathrm{ep}} = [\ce{OH-}]_{\mathrm{sp}}10^{\Delta\mathrm{pH}}$ and $[\ce{HA}]_{\mathrm{ep}} = [\ce{HA}]_{\mathrm{sp}}10^{-\Delta\mathrm{pH}} = [\ce{OH-}]_{\mathrm{sp}}10^{-\Delta\mathrm{pH}}$; substituting in Eq. (2.11):

$$
E_{\mathrm{t}} = \frac{[\ce{OH-}]_{\mathrm{sp}}}{c_{\mathrm{sp}}}\bigl(10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}\bigr) = \sqrt{\frac{K_{\mathrm{w}}}{K_{\mathrm{a}}c_{\mathrm{sp}}}}\bigl(10^{\Delta\mathrm{pH}} - 10^{-\Delta\mathrm{pH}}\bigr).
$$

(3) Around the first stoichiometric point the end-point error equals the difference between the $\ce{HA-}$ that has been over-neutralized and the $\ce{H2A}$ that has not been neutralized: $E_{\mathrm{t}} = ([\ce{A^2-}]_{\mathrm{ep}} - [\ce{H2A}]_{\mathrm{ep}})/c_{\mathrm{sp}}$ ($\ce{H+}$ and $\ce{OH-}$ are relatively very small). With $[\ce{HA-}] \approx c_{\mathrm{sp}}$, $[\ce{A^2-}] = K_{\mathrm{a}2}c_{\mathrm{sp}}/[\ce{H+}]$, $[\ce{H2A}] = [\ce{H+}]c_{\mathrm{sp}}/K_{\mathrm{a}1}$, and $[\ce{H+}]_{\mathrm{sp}} = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$ at the stoichiometric point, substitution gives the result. $\square$

These formulas were systematized by Ringbom (1958). Note that the denominators for strong and weak acids differ: $\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}}$ for a weak acid and $c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}}$ for a strong acid, because the pH at the stoichiometric point of a strong acid is independent of concentration. Complexometric titration, with $\Delta\mathrm{pH}$ replaced by $\Delta\mathrm{pM}'$ and $K_{\mathrm{t}}$ by the conditional stability constant, gives a formula of the same form (Formula 3.3.1); the corresponding formula for redox titration is Formula 5.3.1.

![Dependence of the end-point error |Et| of a weak-acid titration on ΔpH (end-point error formula) for different c_sp K_t; the dashed line is |Et| = 0.1%, the dotted line is the visual limit ΔpH = ±0.2](./plots/ringbom-error.py)

### 2.7.2. Criteria Derived from the End-Point Error Formula

Take $\Delta\mathrm{pH} = \pm0.2$, for which $10^{0.2} - 10^{-0.2} = 0.954$.

- Weak acid: $\lvert E_{\mathrm{t}}\rvert \le 0.1\%$ requires $\sqrt{c_{\mathrm{sp}}K_{\mathrm{t}}} \ge 954$, that is, $c_{\mathrm{sp}}K_{\mathrm{t}} \ge 9.1\times10^5$ and $c_{\mathrm{sp}}K_{\mathrm{a}} \ge 9.1\times10^{-9} \approx 10^{-8}$, which is Eq. (2.8). For a permitted $\pm1\%$ it drops to $10^{-10}$; in the figure above the curve for $c_{\mathrm{sp}}K_{\mathrm{t}} = 10^6$ is about 0.1% at $\Delta\mathrm{pH} = \pm0.2$.
- Strong acid: $c_{\mathrm{sp}}\sqrt{K_{\mathrm{t}}} \ge 954$, so $c_{\mathrm{sp}} \ge 9.5\times10^{-5}\,\mathrm{mol\,L^{-1}}$; the concentration of a strong acid or base should not be lower than about $10^{-4}\,\mathrm{mol\,L^{-1}}$.
- Stepwise titration of a polyprotic acid: $\lvert E_{\mathrm{t}}\rvert \le 1\%$ requires $0.954\sqrt{K_{\mathrm{a}2}/K_{\mathrm{a}1}} \le 0.01$, that is, $K_{\mathrm{a}1}/K_{\mathrm{a}2} \ge 9.1\times10^3 \approx 10^4$, which is Eq. (2.9); for $\pm0.5\%$, taking $\Delta\mathrm{pH} = \pm0.3$ gives $K_{\mathrm{a}1}/K_{\mathrm{a}2} \ge 8.9\times10^4 \approx 10^5$.

The end-point error is thus determined by three factors: the completeness of the reaction ($K_{\mathrm{t}}$), the concentration ($c_{\mathrm{sp}}$), and the precision of end-point detection ($\Delta\mathrm{pH}$). With potentiometric titration ([6.4.6](/6.4.6#sec-6.4.5)) $\Delta\mathrm{pH}$ can be reduced to about 0.02, and the corresponding criteria are relaxed by two orders of magnitude.

**Example 2.7.1** $10\,\mathrm{mL}$ of $0.10\,\mathrm{mol\,L^{-1}}$ HCl is titrated with $0.10\,\mathrm{mol\,L^{-1}}$ NaOH with the end point at pH 5.0 (for instance, methyl red titrated to orange); find the end-point error.

**Solution** $c_{\mathrm{ep}}(\ce{HCl}) \approx c_{\mathrm{sp}} = 0.050\,\mathrm{mol\,L^{-1}}$, and by Eq. (2.10),

$$
E_{\mathrm{t}} = \frac{10^{-9.0} - 10^{-5.0}}{0.050} = -0.02\%.
$$
By Theorem 2.7.1 (1), $\Delta\mathrm{pH} = -2.0$ and $E_{\mathrm{t}} = (10^{-2} - 10^{2})/(0.050\times10^7) = -0.02\%$, the same result. $\square$

**Example 2.7.2** $0.1000\,\mathrm{mol\,L^{-1}}$ NaOH is used to titrate HAc of the same concentration, with phenolphthalein (end point pH 9.0) and with methyl orange (end point pH 4.0) as indicators; find the end-point errors.

**Solution** $c_{\mathrm{sp}} = 0.0500$, $\mathrm{pH}_{\mathrm{sp}} = 8.73$, and $c_{\mathrm{sp}}K_{\mathrm{t}} = 0.0500\times1.75\times10^{-5}/10^{-14} = 8.75\times10^7$. Phenolphthalein: $\Delta\mathrm{pH} = 0.27$ and

$$
E_{\mathrm{t}} = \frac{10^{0.27} - 10^{-0.27}}{\sqrt{8.75\times10^7}} = +0.014\%.
$$
Methyl orange: the end point is too far from the stoichiometric point, the assumption of Theorem 2.7.1 ($[\ce{A-}] \approx c_{\mathrm{sp}}$) no longer holds, and Eq. (2.11) must be used directly: $E_{\mathrm{t}} \approx -\delta_{\ce{HAc}} = -\dfrac{10^{-4.0}}{10^{-4.0} + 1.75\times10^{-5}} = -85\%$, that is, only 15% has been neutralized. This shows why an indicator that changes color in the acidic region cannot be used for the titration of a weak acid. $\square$

## 2.8. Applications of Acid–Base Titration

### 2.8.1. Preparation and Standardization of Acid and Base Standard Solutions

Neither HCl nor NaOH can be used to prepare standard solutions directly. They are commonly used at $0.1\,\mathrm{mol\,L^{-1}}$, prepared roughly and then standardized.

- HCl: standardized with anhydrous $\ce{Na2CO3}$, $\ce{Na2CO3 + 2HCl -> 2NaCl + CO2 + H2O}$; the stoichiometric point is at pH about 3.9, and methyl orange or bromocresol green–methyl red is used (near the end point the solution is boiled to remove $\ce{CO2}$). $\ce{Na2CO3}$ is easy to obtain pure, but it is hygroscopic and must be dried at 270–300 °C and stored sealed, and its molar mass is small (105.99), so the weighing error is relatively large. Alternatively borax is used, $\ce{Na2B4O7 + 2HCl + 5H2O -> 4H3BO3 + 2NaCl}$; the stoichiometric point is a $\ce{H3BO3}$ solution at pH about 5.1, and methyl red is used. Borax has a large molar mass (381.37) and is not hygroscopic, but it effloresces and loses water of crystallization when the relative humidity of the air is below 39%, and should be stored at a relative humidity of 60% (in a desiccator containing a saturated solution of NaCl and sucrose).
- NaOH: NaOH is hygroscopic and absorbs $\ce{CO2}$. A concentrated solution of about 50% is first prepared, in which $\ce{Na2CO3}$ is hardly soluble and settles out, and the supernatant is diluted with water that has been boiled to remove $\ce{CO2}$. It is standardized with potassium hydrogen phthalate (molar mass 204.22; pure, not hygroscopic, easy to store; 1:1 reaction), whose stoichiometric point is a phthalate solution at pH about 9.1, with phenolphthalein as indicator; oxalic acid $\ce{H2C2O4*2H2O}$ can also be used.

Whether the $\ce{CO2}$ absorbed by a NaOH solution causes an error depends on the pH of the end point. If the $\ce{CO3^2-}$ formed by absorption of $\ce{CO2}$ is titrated to the methyl orange end point (pH about 4), it consumes two $\ce{H+}$, equivalent to the two $\ce{OH-}$ originally present, and there is no error; if it is titrated to the phenolphthalein end point (pH about 9), $\ce{CO3^2-}$ is converted only to $\ce{HCO3-}$ and consumes one $\ce{H+}$, so the effective concentration is too low. The same indicator should therefore be used for standardizing and for using a NaOH solution, and absorption of $\ce{CO2}$ should be avoided as far as possible.

**Example 2.8.1** $0.5000\,\mathrm{g}$ of pure $\ce{CaCO3}$ is dissolved in $50.00\,\mathrm{mL}$ of HCl solution, and the excess acid is back-titrated with NaOH solution, consuming $6.20\,\mathrm{mL}$; $1\,\mathrm{mL}$ of the NaOH solution is equivalent to $1.010\,\mathrm{mL}$ of the HCl solution. Find the concentrations of the two solutions.

**Solution** The remaining HCl is equivalent to $6.20\times1.010 = 6.26\,\mathrm{mL}$, so the HCl that reacted with $\ce{CaCO3}$ is $50.00 - 6.26 = 43.74\,\mathrm{mL}$. $\ce{CaCO3 + 2HCl -> CaCl2 + CO2 + H2O}$, and $n(\ce{HCl}) = 2n(\ce{CaCO3}) = 2\times0.5000/100.09 = 9.991\,\mathrm{mmol}$, so

$$
c(\ce{HCl}) = \frac{9.991}{43.74} = 0.2284\,\mathrm{mol\,L^{-1}}, \qquad c(\ce{NaOH}) = 1.010\times0.2284 = 0.2307\,\mathrm{mol\,L^{-1}}.
$$
$\square$

### 2.8.2. The Kjeldahl Method

The nitrogen content of proteins is fairly constant (about 16%), so the protein content can be estimated by determining nitrogen; this is one of the most widely used methods in the analysis of foods, feeds, and biological samples.

**Definition 2.8.1 (Kjeldahl Method)** The method in which an organic sample is digested with concentrated sulfuric acid in the presence of a catalyst to convert its nitrogen compounds to $\ce{NH4+}$, $\ce{NH3}$ is distilled off after adding base, and the nitrogen content is determined by acid–base titration after absorption in acid, is called the **Kjeldahl method** (Kjeldahl, 1883).

1. Digestion: the sample is heated with concentrated $\ce{H2SO4}$, with $\ce{K2SO4}$ added to raise the boiling point (to about 380 °C) and $\ce{CuSO4}$ as catalyst (Hg or Se were used formerly and have been abandoned because of toxicity); the organic matter is oxidized to $\ce{CO2}$ and $\ce{H2O}$, and amino and amide nitrogen is converted to $\ce{NH4HSO4}$.
2. Distillation: after the digest has been cooled and diluted, an excess of concentrated NaOH is added, $\ce{NH4+ + OH- -> NH3 ^ + H2O}$, and $\ce{NH3}$ is steam-distilled.
3. Absorption and titration: current practice is to absorb in a 2%–4% solution of $\ce{H3BO3}$, $\ce{NH3 + H3BO3 -> NH4+ + H2BO3-}$, and to titrate the $\ce{H2BO3-}$ formed with standard HCl (indicator bromocresol green–methyl red, end point pH about 5). $\ce{H3BO3}$ is an extremely weak acid, does not interfere with the titration, and need not be measured accurately. The classical practice is to absorb in an excess of standard HCl or $\ce{H2SO4}$ and back-titrate the remaining acid with NaOH (methyl red as indicator), which requires two standard solutions.
4. A blank determination is made at the same time to subtract the nitrogen in the reagents.

The mass fraction of nitrogen is $w(\ce{N}) = \dfrac{c(\ce{HCl})(V - V_{\text{blank}})M(\ce{N})}{m_{\mathrm{s}}}$, and the protein content is $F\cdot w(\ce{N})$, where the conversion factor $F$ is generally taken as 6.25 ($= 100/16$), 6.38 for dairy products, and 5.70 for wheat.

**Example 2.8.2** $0.5000\,\mathrm{g}$ of milk powder is treated by the Kjeldahl method and absorbed in boric acid; titration with $0.1000\,\mathrm{mol\,L^{-1}}$ HCl consumes $14.20\,\mathrm{mL}$, and the blank consumes $0.10\,\mathrm{mL}$. Find the protein content.

**Solution** $w(\ce{N}) = \dfrac{0.1000\times(14.20 - 0.10)\times10^{-3}\times14.007}{0.5000} = 3.950\%$, and the protein content is $6.38\times3.950\% = 25.2\%$. $\square$

The Kjeldahl method determines total organic nitrogen and ammonium nitrogen and cannot distinguish protein nitrogen from other nitrogen-containing substances (nitrate and heterocyclic nitrogen require an additional reduction treatment). The 2008 incident in which melamine ($\ce{C3H6N6}$, 66.6% nitrogen) was added to milk powder to pass as protein exploited exactly this limitation; since then a liquid chromatography–mass spectrometry method for melamine has been added to the testing of dairy products ([6.4.15](/6.4.15#sec-15.5.1)). Modern laboratories also commonly use combustion (the Dumas method) to determine total nitrogen: the sample is burned at high temperature in oxygen, the nitrogenous substances are converted to $\ce{N2}$, which is determined with a thermal conductivity detector ([6.4.13](/6.4.13#sec-13.6.4)); a sample takes a few minutes and no concentrated sulfuric acid is needed.

### 2.8.3. Titration of Amino Acids and the Isoelectric Point

An amino acid contains both an acidic carboxyl group and a basic amino group.

**Definition 2.8.2 (Zwitterion)** An ion that carries both a positively and a negatively charged group within the molecule and has zero net charge is called a **zwitterion** (dipolar ion).

In aqueous solution and in the crystal, amino acids exist mainly as the zwitterion $\ce{H3N^+CHRCOO^-}$ and not as the neutral molecule $\ce{H2NCHRCOOH}$: the carboxyl group ($\mathrm{p}K_{\mathrm{a}}$ about 2) is far more acidic than the ammonium group ($\mathrm{p}K_{\mathrm{a}}$ about 9–10), and a proton moves from the carboxyl group to the amino group. This explains why amino acids have high melting points and dissolve readily in water but poorly in organic solvents. Taking glycine as an example, it exists as the cation (1) in strong acid, as the zwitterion (2) near neutrality, and as the anion (3) in strong base:

```smiles
[NH3+]CC(=O)O 1
[NH3+]CC(=O)[O-] 2
NCC(=O)[O-] 3
```

Regarding the cation $\ce{H2A+}$ as a diprotic acid with $\mathrm{p}K_{\mathrm{a}1} = 2.34$ (carboxyl) and $\mathrm{p}K_{\mathrm{a}2} = 9.60$ (ammonium), the zwitterion $\ce{HA}$ is the amphoteric species of 2.3.4.

**Definition 2.8.3 (Isoelectric Point)** The pH of the solution at which the average net charge of an amino acid or protein molecule is zero is called the **isoelectric point**, denoted pI.

At the isoelectric point $[\ce{H2A+}] = [\ce{A-}]$, and from $K_{\mathrm{a}1}K_{\mathrm{a}2} = [\ce{H+}]^2[\ce{A-}]/[\ce{H2A+}]$,

$$
\mathrm{pI} = \tfrac12(\mathrm{p}K_{\mathrm{a}1} + \mathrm{p}K_{\mathrm{a}2}),
$$
so for glycine $\mathrm{pI} = 5.97$. This is the same as the simplest formula for amphoteric species, $[\ce{H+}] = \sqrt{K_{\mathrm{a}1}K_{\mathrm{a}2}}$: the pH of a solution of pure glycine in water is approximately its isoelectric point. For an amino acid with a dissociable side chain, pI is the mean of the two $\mathrm{p}K_{\mathrm{a}}$ on either side of the zwitterion: for aspartic acid ($\mathrm{p}K_{\mathrm{a}}$ 1.99, 3.90, 9.90) $\mathrm{pI} = \frac12(1.99 + 3.90) = 2.95$, and for lysine (2.16, 9.06, 10.54) $\mathrm{pI} = \frac12(9.06 + 10.54) = 9.80$. The isoelectric point of a protein is determined by all its dissociable side chains together; at the isoelectric point the solubility of a protein is smallest and it does not move in an electric field, which is the basis of isoelectric precipitation and isoelectric focusing electrophoresis ([6.4.14](/6.4.14)).

![Titration of 20.00 mL of 0.1000 mol/L glycine hydrochloride with 0.1000 mol/L NaOH. Top: titration curve; the first stoichiometric point is the isoelectric point. Bottom: distribution fractions of the cation, the zwitterion, and the anion](./plots/glycine-titration.py)

In the titration of glycine hydrochloride with NaOH, the solution at the first stoichiometric point is the zwitterion, its pH equals pI, and the jump is clear; the second step (ammonium group), with $c_{\mathrm{sp}}K_{\mathrm{a}2} \approx 10^{-11}$, cannot be titrated directly. The figure also shows that the two buffer regions are centered on $\mathrm{p}K_{\mathrm{a}1}$ and $\mathrm{p}K_{\mathrm{a}2}$: an amino acid is itself a buffer (the glycine buffers in the table, pH 2.2–3.6 and 8.6–10.6). The amount of amino groups can be determined by the formaldehyde method (Sørensen formol titration): formaldehyde reacts with the amino group so that the ammonium group releases $\ce{H+}$, which can then be titrated with NaOH with phenolphthalein as indicator, a method formerly used to follow the progress of protein hydrolysis; or by nonaqueous titration with $\ce{HClO4}$ in glacial acetic acid, the pharmacopoeial method for determining amino acids.

The determination of total $\ce{CO2}$ in blood (the sum of $\ce{HCO3-}$, dissolved $\ce{CO2}$, and $\ce{H2CO3}$) is also an application of acid–base reactions: acid is added to convert all $\ce{HCO3-}$ to $\ce{CO2}$, and the volume or pressure of the gas released is measured; or an excess of standard HCl is added, the $\ce{CO2}$ is driven off, and the remaining acid is back-titrated with NaOH. Combined with the measured pH and the Henderson–Hasselbalch equation, $[\ce{HCO3-}]$ and the partial pressure of $\ce{CO2}$ can be calculated.

## Summary

| Question | Conclusion |
|---|---|
| Concentration constants and activity constants | $K^{\mathrm{c}}$ varies with ionic strength; activity corrections are needed in preparing buffers, using standard buffers, and using ion-selective electrodes |
| Calculation of pH | Write the exact formula from the proton condition (or charge balance); approximation criteria for 5% error $K_{\mathrm{a}}c \ge 20K_{\mathrm{w}}$, $c/K_{\mathrm{a}} \ge 105$; solve complex systems numerically |
| Choice of buffer | $\mathrm{p}K_{\mathrm{a}}$ close to the pH required; in biochemical work also consider temperature coefficient, ionic strength, metal coordination, and reactivity |
| Choice of indicator | Transition range within the jump, with the transition point as close as possible to the stoichiometric point |
| Whether a monoprotic weak acid (base) can be titrated accurately | $c_{\mathrm{sp}}K_{\mathrm{a}} \ge 10^{-8}$ ($\Delta\mathrm{pH} = \pm0.2$, $\lvert E_{\mathrm{t}}\rvert \le 0.1\%$) |
| Whether a polyprotic acid can be titrated stepwise | $c_{\mathrm{sp}}K_{\mathrm{a}i} \ge 10^{-9}$ and $K_{\mathrm{a}i}/K_{\mathrm{a}(i+1)} \ge 10^4$ ($\pm1\%$) |
| End-point error | Eqs. (2.10) and (2.11) hold generally; when the end point is near the stoichiometric point use the end-point error formula (Theorem 2.7.1) |
