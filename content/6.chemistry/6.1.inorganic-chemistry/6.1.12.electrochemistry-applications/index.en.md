---
title: Applications of Electrode Potentials and Electrochemistry
source_hash: 70b0a53c976d
---

[6.1.11](/6.1.11) established the concept of the electrode potential and obtained from thermodynamics $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$ and the **Nernst equation**. In this chapter we use these two relations to solve practical problems in chemistry: comparing the strengths of oxidizing and reducing agents, calculating equilibrium constants of redox reactions, finding solubility products from electromotive forces, and deciding the direction and extent of reactions (12.1). We then plot the standard electrode potentials among the oxidation states of an element as a Latimer diagram and a Frost diagram, from which one can see at a glance which oxidation states are stable and which disproportionate (12.2), and plot electrode potential against pH on the same diagram to decide whether a substance can exist stably in water (12.3). Finally we discuss two technological directions of electrochemistry: electrolysis, in which electrical energy drives nonspontaneous reactions (12.4), and electrochemical power sources, which store chemical energy and convert it to electrical energy on demand (12.5). Latimer and Frost diagrams are the main tools of the descriptive chemistry of the elements in [6.1.13](/6.1.13)–[6.1.15](/6.1.15). The theory of electrode kinetics and overpotential, and corrosion and its prevention, are found in [Physical Chemistry](/6.3); redox titration and potentiometric analysis are found in [Analytical Chemistry](/6.4).

## 12.1. Applications of Electrode Potentials

### 12.1.1. Comparing the Strengths of Oxidizing and Reducing Agents

The smaller (the more negative) the **standard electrode potential**, the stronger the reducing power of the reduced form of the couple; the larger (the more positive), the stronger the oxidizing power of the oxidized form. A table of couples arranged by $E^\circ$ is therefore a table of the order of strength of oxidizing and reducing agents: the oxidized form of the couple with the larger $E^\circ$ can oxidize the reduced form of the couple with the smaller $E^\circ$. When concentrations do not deviate far from the standard state, $E^\circ$ can be used directly for comparison; when they deviate greatly, $E$ is first found from the Nernst equation and then compared.

In complex systems one often needs to oxidize (or reduce) only one component without affecting the others, and one then chooses a reagent whose $E^\circ$ lies between the two.

**Example 12.1.1** In a mixed solution containing $\ce{Cl-}$, $\ce{Br-}$, and $\ce{I-}$, $\ce{I-}$ is to be oxidized to $\ce{I2}$ without oxidizing $\ce{Cl-}$ or $\ce{Br-}$. Which of $\ce{Fe2(SO4)3}$ and $\ce{KMnO4}$ meets this requirement?

**Solution** $E^\circ(\ce{I2}/\ce{I-}) = 0.536\,\mathrm{V}$, $E^\circ(\ce{Br2}/\ce{Br-}) = 1.066\,\mathrm{V}$, $E^\circ(\ce{Cl2}/\ce{Cl-}) = 1.358\,\mathrm{V}$; $E^\circ(\ce{Fe^3+}/\ce{Fe^2+}) = 0.771\,\mathrm{V}$, $E^\circ(\ce{MnO4-}/\ce{Mn^2+}) = 1.507\,\mathrm{V}$. The $E^\circ$ of $\ce{Fe^3+}$ is larger than that of $\ce{I2}/\ce{I-}$ and smaller than the other two, so it can oxidize only $\ce{I-}$; the $E^\circ$ of acidic $\ce{KMnO4}$ is larger than all three and would oxidize all three halide ions. We therefore choose $\ce{Fe2(SO4)3}$: $\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}$. $\square$

### 12.1.2. Calculating Equilibrium Constants of Redox Reactions

Combining $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$ (Eq. (11.1)) with $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$ (Eq. (8.3)) gives $RT\ln K^\circ = zFE^\circ_{\mathrm{cell}}$. At $298.15\,\mathrm{K}$

$$
\lg K^\circ = \frac{zFE^\circ_{\mathrm{cell}}}{RT\ln 10} = \frac{z(E^\circ_+ - E^\circ_-)}{0.05916\,\mathrm{V}}, \tag{12.1}
$$
where $z$ is the (numerical) amount of electrons, in mol, transferred when 1 mol of reaction proceeds as the equation is written, that is, the least common multiple of the numbers of electrons in the two half-reactions. The **standard equilibrium constant** is determined only by the difference of the $E^\circ$ of the two couples and by $z$, and no concentration data are needed.

**Example 12.1.2** Find $K^\circ$ for $\ce{2Ag + 2HI -> 2AgI + H2}$ at $298.15\,\mathrm{K}$. What if the equation is written $\ce{Ag + HI -> AgI + 1/2H2}$?

**Solution** Ag rises from 0 to $+1$ and is the reducing agent; its couple $\ce{AgI}/\ce{Ag}$ ($E^\circ = -0.152\,\mathrm{V}$, 11.5.4 of [6.1.11](/6.1.11)) is the negative electrode; $\ce{H+}$ is reduced, and $\ce{H+}/\ce{H2}$ ($E^\circ = 0$) is the positive electrode, so $E^\circ_{\mathrm{cell}} = 0.152\,\mathrm{V}$. For the first way of writing, $z = 2$:

$$
\lg K^\circ = \frac{2 \times 0.152}{0.05916} = 5.14, \qquad K^\circ = 1.4\times10^5.
$$
For the second, $z = 1$: $\lg K^{\circ\prime} = 2.57$ and $K^{\circ\prime} = 3.7\times10^2 = (K^\circ)^{1/2}$. When the stoichiometric coefficients of the equation change, $E^\circ_{\mathrm{cell}}$ is unchanged, and $z$ and $\lg K^\circ$ change in proportion; this agrees with the rule for writing equilibrium constants ([6.1.8](/6.1.8)). $\square$

Finally, consider the criterion for a reaction to go to completion. It is often said that "a reaction with a standard electromotive force greater than 0.3 V goes essentially to completion", but this statement has a premise. From Eq. (12.1), for $K^\circ \ge 10^n$ we need

$$
E^\circ_{\mathrm{cell}} \ge \frac{0.05916\,\mathrm{V} \times n}{z}.
$$

| Requirement | $z = 1$ | $z = 2$ | $z = 3$ |
|---|---|---|---|
| $K^\circ \ge 10^5$ | $0.30\,\mathrm{V}$ | $0.15\,\mathrm{V}$ | $0.10\,\mathrm{V}$ |
| $K^\circ \ge 10^6$ | $0.35\,\mathrm{V}$ | $0.18\,\mathrm{V}$ | $0.12\,\mathrm{V}$ |

The "0.3 V" is the value for $z = 1$ with $K^\circ \ge 10^5$ taken as "complete"; the larger $z$ is, the smaller the required $E^\circ_{\mathrm{cell}}$. How large $K^\circ$ must be to count as complete also depends on the stoichiometry of the reaction and the degree of conversion required: for a reaction of the type $\mathrm{Ox_1} + \mathrm{Red_2} \to \mathrm{Red_1} + \mathrm{Ox_2}$ (all coefficients 1), mixing equal amounts and requiring both reactants to be 99.9% converted gives $K^\circ = (999/1)^2 \approx 10^6$ at equilibrium. The criterion derived from this for titrimetric analysis is found in [Analytical Chemistry](/6.4).

### 12.1.3. Determining Solubility Products

The ion concentrations of sparingly soluble salts are extremely low and hard to measure directly, but a cell can be designed whose cell reaction is exactly the formation (or dissolution) of the precipitate, so that $K^\circ$, the reciprocal of the **solubility product** (or the solubility product itself), can be found from the electromotive force.

**Example 12.1.3** From $E^\circ(\ce{Ag+}/\ce{Ag}) = 0.7996\,\mathrm{V}$ and $E^\circ(\ce{AgCl}/\ce{Ag}) = 0.2223\,\mathrm{V}$, find the solubility product of $\ce{AgCl}$ at $298.15\,\mathrm{K}$.

**Solution** Taking $\ce{Ag+ + e- -> Ag}$ as the positive-electrode reaction and $\ce{AgCl + e- -> Ag + Cl-}$ as the negative-electrode reaction, their difference is $\ce{Ag+ + Cl- -> AgCl(s)}$, with $z = 1$:

$$
\lg K^\circ = \frac{0.7996 - 0.2223}{0.05916} = 9.758, \qquad K^\circ = 5.73\times10^9, \qquad K_{\mathrm{sp}} = \frac{1}{K^\circ} = 1.75\times10^{-10},
$$
in agreement with the value $1.8\times10^{-10}$ obtained from the solubility in [6.1.10](/6.1.10). $\square$

**Example 12.1.4** At $298.15\,\mathrm{K}$ the electromotive force of the galvanic cell $(-)\ \ce{Pb} \mid \ce{PbSO4(s)} \mid \ce{SO4^2-}(1\,\mathrm{mol\,L^{-1}}) \parallel \ce{Sn^2+}(1\,\mathrm{mol\,L^{-1}}) \mid \ce{Sn}\ (+)$ is $0.22\,\mathrm{V}$. Given $E^\circ(\ce{Sn^2+}/\ce{Sn}) = -0.138\,\mathrm{V}$ and $E^\circ(\ce{Pb^2+}/\ce{Pb}) = -0.126\,\mathrm{V}$, find $K_{\mathrm{sp}}(\ce{PbSO4})$.

**Solution** The electrode potential of the negative electrode is $E^\circ(\ce{PbSO4}/\ce{Pb}) = E^\circ(\ce{Sn^2+}/\ce{Sn}) - E_{\mathrm{cell}} = -0.138 - 0.22 = -0.358\,\mathrm{V}$. The negative electrode can be regarded as a $\ce{Pb^2+}/\ce{Pb}$ electrode in which $[\ce{Pb^2+}]$ is fixed by the dissolution equilibrium of $\ce{PbSO4}$: at $[\ce{SO4^2-}] = 1$, $[\ce{Pb^2+}] = K_{\mathrm{sp}}$, so

$$
-0.358 = -0.126 + \frac{0.05916}{2}\lg K_{\mathrm{sp}}, \qquad \lg K_{\mathrm{sp}} = -7.84, \qquad K_{\mathrm{sp}} = 1.4\times10^{-8}.
$$
The value obtained from the solubility is $2.5\times10^{-8}$, a difference of less than a factor of two. $\lg K_{\mathrm{sp}}$ is very sensitive to the electromotive force (for $z = 2$, each $0.01\,\mathrm{V}$ corresponds to a factor of 2.2 in $K_{\mathrm{sp}}$), so an electromotive force with two significant figures gives only the order of magnitude of $K_{\mathrm{sp}}$; an accurate determination also requires activities in place of concentrations. $\square$

The same method can be used to find **stability constants**: $\lg\beta_4$ follows from the difference between $E^\circ([\ce{Cu(NH3)4}]^{2+}/\ce{Cu})$ and $E^\circ(\ce{Cu^2+}/\ce{Cu})$ (11.5.4 of [6.1.11](/6.1.11)), and one can also find the dissociation constants of weak acids and the ion product of water.

### 12.1.4. Deciding the Direction and Extent of Reactions

For the equation as written, take the couple containing the oxidizing agent as the positive electrode and that containing the reducing agent as the negative electrode: the forward reaction is spontaneous when $E_{\mathrm{cell}} > 0$ and the reverse reaction is spontaneous when $E_{\mathrm{cell}} < 0$. When all substances are in their standard states, $E^\circ$ is used; otherwise the Nernst equation is first used to find $E$ for the two electrodes.

**Example 12.1.5** Why can $\ce{FeCl3}$ solution dissolve copper (as in etching printed circuit boards)?

**Solution** For $\ce{2Fe^3+ + Cu -> 2Fe^2+ + Cu^2+}$, the positive electrode is $\ce{Fe^3+}/\ce{Fe^2+}$ ($0.771\,\mathrm{V}$) and the negative electrode is $\ce{Cu^2+}/\ce{Cu}$ ($0.342\,\mathrm{V}$), so $E^\circ_{\mathrm{cell}} = 0.429\,\mathrm{V} > 0$ and the forward reaction is spontaneous; with $z = 2$, $\lg K^\circ = 2 \times 0.429/0.05916 = 14.5$, and the reaction goes essentially to completion. $\square$

**Example 12.1.6** Decide the direction of $\ce{Pb^2+ + Sn -> Pb + Sn^2+}$ under standard conditions, and when $[\ce{Pb^2+}] = 0.10\,\mathrm{mol\,L^{-1}}$ and $[\ce{Sn^2+}] = 1.0\,\mathrm{mol\,L^{-1}}$.

**Solution** The positive electrode is $\ce{Pb^2+}/\ce{Pb}$ ($-0.126\,\mathrm{V}$) and the negative electrode is $\ce{Sn^2+}/\ce{Sn}$ ($-0.138\,\mathrm{V}$). Under standard conditions $E^\circ_{\mathrm{cell}} = 0.012\,\mathrm{V} > 0$ and the forward reaction is spontaneous. Under the nonstandard conditions

$$
E(\ce{Pb^2+}/\ce{Pb}) = -0.126 + \frac{0.05916}{2}\lg 0.10 = -0.156\,\mathrm{V}, \qquad E_{\mathrm{cell}} = -0.156 - (-0.138) = -0.018\,\mathrm{V} < 0,
$$
so the reaction proceeds in the reverse direction: Pb displaces Sn from $\ce{Sn^2+}$. When the $E^\circ$ values of two couples differ very little ($K^\circ = 10^{0.41} \approx 2.5$), a change in concentration is enough to reverse the direction of the reaction. $\square$

**Example 12.1.7** Decide the direction of $\ce{H3AsO4 + 2I- + 2H+ <=> H3AsO3 + I2 + H2O}$ under standard conditions and at $[\ce{H+}] = 10^{-8}\,\mathrm{mol\,L^{-1}}$ (all other species still at $1\,\mathrm{mol\,L^{-1}}$).

**Solution** $E^\circ(\ce{H3AsO4}/\ce{H3AsO3}) = 0.560\,\mathrm{V}$ (for $\ce{H3AsO4 + 2H+ + 2e- <=> H3AsO3 + H2O}$) and $E^\circ(\ce{I2}/\ce{I-}) = 0.536\,\mathrm{V}$. Under standard conditions $E^\circ_{\mathrm{cell}} = 0.024\,\mathrm{V} > 0$ and the forward reaction is spontaneous. At $[\ce{H+}] = 10^{-8}$ the potential of $\ce{I2}/\ce{I-}$ is unchanged, whereas

$$
E(\ce{H3AsO4}/\ce{H3AsO3}) = 0.560 + \frac{0.05916}{2}\lg(10^{-8})^2 = 0.087\,\mathrm{V}, \qquad E_{\mathrm{cell}} = 0.087 - 0.536 = -0.449\,\mathrm{V} < 0,
$$
and the reaction proceeds in the reverse direction: in weakly basic solution $\ce{I2}$ oxidizes $\ce{H3AsO3}$ to arsenic acid. This is exploited in analytical chemistry, where arsenite is determined with a standard $\ce{I2}$ solution under weakly basic conditions buffered by $\ce{NaHCO3}$, while in strong acid arsenic acid oxidizes $\ce{I-}$. $\square$

### 12.1.5. Limitations of the Applications

1. The electrode potential indicates only the feasibility and extent of a reaction, not its rate. For example, $E^\circ(\ce{S2O8^2-}/\ce{SO4^2-}) = 2.010\,\mathrm{V}$ is far larger than $E^\circ(\ce{MnO4-}/\ce{Mn^2+}) = 1.507\,\mathrm{V}$, and thermodynamically $\ce{S2O8^2-}$ can oxidize $\ce{Mn^2+}$ to $\ce{MnO4-}$, but the reaction is extremely slow and needs $\ce{Ag+}$ as a **catalyst**:

   $$
   \ce{5S2O8^2- + 2Mn^2+ + 8H2O ->[Ag+] 2MnO4- + 10SO4^2- + 16H+}.
   $$
   As another example, $E^\circ(\ce{Li+}/\ce{Li}) = -3.040\,\mathrm{V}$ is more negative than $E^\circ(\ce{Na+}/\ce{Na}) = -2.71\,\mathrm{V}$, so the driving force of the reaction of Li with water is greater, yet in practice it is much slower than that of Na. Li has a high melting point ($180.5\,^\circ\mathrm{C}$) and the heat released does not melt it, whereas Na ($98\,^\circ\mathrm{C}$) melts into a ball whose surface is constantly renewed; $\ce{LiOH}$ is poorly soluble and coats the metal surface, hindering the reaction. The especially negative $E^\circ$ of Li comes mainly from the very large hydration enthalpy of the very small $\ce{Li+}$ ion, which is a stabilization of the product side, whereas the reaction rate depends on the activation process, and both the sublimation enthalpy and the ionization energy of Li are larger than those of Na. Questions of reaction rate are treated by chemical kinetics ([6.1.7](/6.1.7)).
2. Applicable only to aqueous solutions: the tabulated $E^\circ$ are data for aqueous solution at $298.15\,\mathrm{K}$ and cannot be applied directly to nonaqueous solutions, high temperatures, or solid-state reactions (the reduction of metal oxides at high temperature is judged from $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, [6.1.6](/6.1.6)).
3. When concentrations deviate far from the standard state, the Nernst equation must be used, especially for oxoanions whose electrode reactions involve $\ce{H+}$ or $\ce{OH-}$ ($\ce{KMnO4}$, $\ce{K2Cr2O7}$, $\ce{H3AsO4}$, and so on), for which the acidity must be considered (Example 12.1.7); the same holds when precipitates or complexes form.
4. $E^\circ$ is an intensive quantity and is independent of the stoichiometric coefficients of the electrode reaction, whereas the equilibrium constant changes with the way the equation is written (Example 12.1.2).

## 12.2. Latimer Diagrams

### 12.2.1. Latimer Diagrams

Many elements have several oxidation states, which form couples in pairs. Arranging the standard electrode potentials of these couples on one diagram according to oxidation state is far more illuminating than consulting a table.

**Definition 12.2.1 (Latimer Diagram)** A diagram in which the oxidation states of an element are arranged from left to right in order of decreasing oxidation number, with adjacent species joined by a line (or arrow) labeled with the standard electrode potential of that couple, is called a **Latimer diagram**. The medium is stated: $E^\circ_{\mathrm{A}}$ denotes acidic solution ($[\ce{H+}] = 1\,\mathrm{mol\,L^{-1}}$) and $E^\circ_{\mathrm{B}}$ denotes basic solution ($[\ce{OH-}] = 1\,\mathrm{mol\,L^{-1}}$).

The Latimer diagram of manganese ($298.15\,\mathrm{K}$, in V; arrows point in the direction of reduction):

$$
E^\circ_{\mathrm{A}}:\quad \ce{MnO4^- ->[0.56] MnO4^2- ->[2.26] MnO2 ->[0.95] Mn^3+ ->[1.51] Mn^2+ ->[-1.18] Mn}
$$

$$
E^\circ_{\mathrm{B}}:\quad \ce{MnO4^- ->[0.56] MnO4^2- ->[0.60] MnO2 ->[-0.20] Mn(OH)3 ->[0.10] Mn(OH)2 ->[-1.56] Mn}
$$
Couples between nonadjacent species are also often marked on the diagram (drawn above or below the main line), such as, in acidic solution, $E^\circ(\ce{MnO4-}/\ce{MnO2}) = 1.68\,\mathrm{V}$, $E^\circ(\ce{MnO4-}/\ce{Mn^2+}) = 1.51\,\mathrm{V}$, and $E^\circ(\ce{MnO2}/\ce{Mn^2+}) = 1.23\,\mathrm{V}$; and in basic solution $E^\circ(\ce{MnO4-}/\ce{MnO2}) = 0.59\,\mathrm{V}$ and $E^\circ(\ce{MnO2}/\ce{Mn(OH)2}) = -0.05\,\mathrm{V}$. They can be calculated from the adjacent couples (12.2.2).

Comparing the two rows, the potential of the same couple is generally much higher in acidic than in basic solution (except for the couples below $\ce{MnO2}$): oxoanions are strong oxidizing agents in acidic solution, while low oxidation states ($\ce{Mn(OH)2}$) are fairly strong reducing agents in basic solution and are readily oxidized by air.

### 12.2.2. Finding the Standard Potential of an Unknown Couple from Adjacent Couples

**Theorem 12.2.1** Let A, B, and C be three oxidation states of the same element, and let the numbers of electrons transferred and the standard electrode potentials of the couples A/B and B/C be $z_1, E^\circ_1$ and $z_2, E^\circ_2$. Then the standard electrode potential of the couple A/C is

$$
E^\circ_3 = \frac{z_1E^\circ_1 + z_2E^\circ_2}{z_1 + z_2}. \tag{12.2}
$$
In general, if A is reduced to X through $i$ adjacent couples, then $E^\circ(\mathrm{A}/\mathrm{X}) = \dfrac{z_1E^\circ_1 + z_2E^\circ_2 + \cdots + z_iE^\circ_i}{z_1 + z_2 + \cdots + z_i}$.

**Proof** The half-reactions A $+\, z_1\ce{e-} \to$ B and B $+\, z_2\ce{e-} \to$ C add to give A $+\, (z_1 + z_2)\ce{e-} \to$ C. Combining each half-reaction with the standard hydrogen electrode into a cell gives $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ$. The **Gibbs energy** is a state function, and when reactions are added their $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ add (as in **Hess's law**):

$$
-(z_1 + z_2)FE^\circ_3 = -z_1FE^\circ_1 - z_2FE^\circ_2,
$$
and dividing both sides by $-(z_1 + z_2)F$ gives the result. The generalization to $i$ couples is the same. $\square$

Note that what is added is $zE^\circ$ (a quantity proportional to $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$), not the potentials themselves: $E^\circ$ is an intensive quantity and cannot be added. For example, in acidic solution $E^\circ(\ce{MnO2}/\ce{Mn^2+}) = (1 \times 0.95 + 1 \times 1.51)/2 = 1.23\,\mathrm{V}$ and $E^\circ(\ce{MnO4-}/\ce{Mn^2+}) = (1 \times 0.56 + 2 \times 2.26 + 1 \times 0.95 + 1 \times 1.51)/5 = 1.51\,\mathrm{V}$.

**Example 12.2.1** In basic solution $E^\circ_{\mathrm{B}}(\ce{IO-}/\ce{I-}) = 0.485\,\mathrm{V}$ and $E^\circ(\ce{I2}/\ce{I-}) = 0.536\,\mathrm{V}$. Find $E^\circ_{\mathrm{B}}(\ce{IO-}/\ce{I2})$.

**Solution** Per I atom: $\ce{IO-}$ ($+1$) $\to \tfrac{1}{2}\ce{I2}$ (0), $z_1 = 1$; $\tfrac{1}{2}\ce{I2} \to \ce{I-}$ ($-1$), $z_2 = 1$; $\ce{IO-} \to \ce{I-}$, $z_3 = 2$. By Eq. (12.2),

$$
E^\circ(\ce{IO-}/\ce{I2}) = \frac{2 \times 0.485 - 1 \times 0.536}{1} = 0.43\,\mathrm{V}. \qquad \square
$$
Since $E^\circ(\ce{I2}/\ce{I-}) = 0.536\,\mathrm{V} > E^\circ(\ce{IO-}/\ce{I2}) = 0.43\,\mathrm{V}$, $\ce{I2}$ disproportionates in basic solution (next section).

### 12.2.3. Deciding Whether Disproportionation Can Occur

Consider three adjacent species in a Latimer diagram, A $\xrightarrow{E^\circ_{\text{left}}}$ B $\xrightarrow{E^\circ_{\text{right}}}$ C (oxidation number decreasing from left to right). The disproportionation of B to A and C can be regarded as B acting simultaneously as oxidizing and reducing agent: B is reduced to C, with the couple B/C as the positive electrode, and B is oxidized to A, with the couple A/B as the negative electrode. Thus $E^\circ_{\mathrm{cell}} = E^\circ_{\text{right}} - E^\circ_{\text{left}}$.

**Theorem 12.2.2 (Criterion for Disproportionation)** In the Latimer diagram A $\xrightarrow{E^\circ_{\text{left}}}$ B $\xrightarrow{E^\circ_{\text{right}}}$ C, if $E^\circ_{\text{right}} > E^\circ_{\text{left}}$, B spontaneously undergoes **disproportionation** to A and C under standard conditions; if $E^\circ_{\text{right}} < E^\circ_{\text{left}}$, B does not disproportionate, and A and C spontaneously undergo **comproportionation** to give B.

The Latimer diagram of copper in acidic solution is $\ce{Cu^2+ ->[0.153] Cu+ ->[0.521] Cu}$. Since $E^\circ_{\text{right}} = 0.521\,\mathrm{V} > E^\circ_{\text{left}} = 0.153\,\mathrm{V}$, $\ce{Cu+}$ is unstable in aqueous solution:

$$
\ce{2Cu+ -> Cu + Cu^2+}, \qquad \lg K^\circ = \frac{0.521 - 0.153}{0.05916} = 6.22, \quad K^\circ = 1.7\times10^6.
$$
Cu(I) can exist stably only when sparingly soluble compounds ($\ce{CuI}$, $\ce{CuCl}$) or stable complexes ($[\ce{CuCl2}]^-$, $[\ce{Cu(CN)2}]^-$) form and make $[\ce{Cu+}]$ extremely low ([6.1.15](/6.1.15)).

In the Latimer diagram of iron, $\ce{Fe^3+ ->[0.771] Fe^2+ ->[-0.447] Fe}$, $E^\circ_{\text{right}} < E^\circ_{\text{left}}$, so $\ce{Fe^2+}$ does not disproportionate; instead $\ce{Fe^3+}$ and Fe undergo comproportionation, $\ce{2Fe^3+ + Fe -> 3Fe^2+}$. When $\ce{FeSO4}$ solution is stored in the laboratory, an iron nail is added to make use of this reaction, reducing back any $\ce{Fe^3+}$ formed by air oxidation.

Similarly, in the acidic Latimer diagram of manganese, both $\ce{MnO4^2-}$ ($2.26 > 0.56$) and $\ce{Mn^3+}$ ($1.51 > 0.95$) disproportionate, so manganate can exist only in strong base and $\ce{Mn^3+}$ is unstable in aqueous solution (table of disproportionation reactions in [6.1.11](/6.1.11)). In basic solution the potentials on either side of $\ce{MnO4^2-}$ ($0.60$ and $0.56\,\mathrm{V}$) are almost equal, the tendency to disproportionate is very small, and increasing $[\ce{OH-}]$ stabilizes it.

### 12.2.4. Frost Diagrams

The numbers in a Latimer diagram must be compared pair by pair, which is not very intuitive when an element has many oxidation states. Drawing them as a graph makes the overall pattern easier to see.

**Definition 12.2.2 (Frost Diagram)** A plot in which the species of an element in a given medium are drawn as points, with the oxidation number $N$ as abscissa and $NE^\circ$ (in V) for the couple $\mathrm{X}(N)/\mathrm{X}(0)$ as ordinate, and the points are joined in sequence, is called a **Frost diagram** (oxidation state diagram).

$NE^\circ$ is called the volt equivalent; since $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ$, it equals $-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/F$, where $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ is the standard Gibbs energy change for the reduction of $\mathrm{X}(N)$ to the element $\mathrm{X}(0)$. The lower the ordinate, therefore, the more stable the species relative to the element (with $\ce{H+}/\ce{H2}$ as the reference). By Theorem 12.2.1, starting from the element and adding up the $zE^\circ$ of adjacent couples in turn gives the ordinate of each point. How to read a Frost diagram:

1. The slope of a line is the standard electrode potential of that couple: the line through the points $(N_1, N_1E^\circ_1)$ and $(N_2, N_2E^\circ_2)$ has slope $\frac{N_2E^\circ_2 - N_1E^\circ_1}{N_2 - N_1} = E^\circ(\mathrm{X}(N_2)/\mathrm{X}(N_1))$. The greater the slope, the stronger the oxidizing agent that the species of higher oxidation state is; with a negative slope, the species of lower oxidation state is a reducing agent.
2. The lowest point is the most stable oxidation state.
3. A species lying above the line joining its two neighbors (a convex point) disproportionates: its Gibbs energy is higher than the proportionate average of the species on either side.
4. A species lying below the line (a concave point) is the product of comproportionation of the species on either side and is stable toward disproportionation.

![Frost diagrams of manganese in acidic (pH 0) and basic (pH 14) solution: in acid Mn²⁺ is the most stable, and MnO₄²⁻ and Mn³⁺ lie above the lines joining their neighbors and disproportionate; the line from MnO₂ to MnO₄⁻ is steep, so the high oxidation states are strong oxidizing agents. In base MnO₂ and Mn(OH)₂ are lowest, the whole curve is much flatter, and the oxidizing power of the high oxidation states is greatly weakened](./plots/manganese-frost.py)

In the acidic Frost diagram of manganese, $\ce{Mn^2+}$ is the lowest point, so in acidic solution all oxidation states of manganese tend ultimately toward $\ce{Mn^2+}$; $\ce{MnO4^2-}$ ($N = 6$) lies clearly above the line joining $\ce{MnO2}$ and $\ce{MnO4-}$, and $\ce{Mn^3+}$ lies above the line joining $\ce{Mn^2+}$ and $\ce{MnO2}$, so both disproportionate, in agreement with the conclusion of 12.2.3. The basic Frost diagram is much flatter, with $\ce{Mn(OH)3}$ slightly above the line joining its neighbors; $\ce{MnO4^2-}$ lies almost on the line joining $\ce{MnO2}$ and $\ce{MnO4-}$, and its tendency to disproportionate is very small. The Frost diagram of an element changes drastically with pH, for the same reason as in 11.5.3 of [6.1.11](/6.1.11): the electrode reactions of oxygen-containing species involve $\ce{H+}$ or $\ce{OH-}$. [6.1.13](/6.1.13)–[6.1.15](/6.1.15) use Frost diagrams to compare the stability of oxidation states across groups of elements.

## 12.3. Potential–pH Diagrams

### 12.3.1. Potential–pH Diagrams and the Stability Region of Water

The electrode potentials of many couples vary with pH. Plotting them on one diagram at fixed temperature and fixed concentrations of the other species shows directly which species can coexist at a given pH.

**Definition 12.3.1 (Potential–pH Diagram)** A diagram constructed at constant temperature and fixed concentrations (or partial pressures) of the species, with the electrode potential of a couple as ordinate and the pH of the solution as abscissa, is called a **potential–pH diagram** (Pourbaix diagram).

The most basic potential–pH diagram is the stability region of water itself. Water can be reduced (releasing $\ce{H2}$) and also oxidized (releasing $\ce{O2}$). With $p_{\ce{H2}} = p_{\ce{O2}} = p^\circ$, at $298.15\,\mathrm{K}$

$$
\begin{aligned}
&\text{line a: }\ \ce{2H+ + 2e- <=> H2}, && E = 0 + \frac{0.05916\,\mathrm{V}}{2}\lg[\ce{H+}]^2 = -0.0592\,\mathrm{V}\times\mathrm{pH};\\
&\text{line b: }\ \ce{O2 + 4H+ + 4e- <=> 2H2O}, && E = 1.229\,\mathrm{V} + \frac{0.05916\,\mathrm{V}}{4}\lg[\ce{H+}]^4 = 1.229\,\mathrm{V} - 0.0592\,\mathrm{V}\times\mathrm{pH}.
\end{aligned}
$$
The two lines are parallel and are $1.229\,\mathrm{V}$ apart (the electromotive force corresponding to the $\Delta_{\mathrm{f}}G^\circ$ of water).

- Any point on line b represents equilibrium between $\ce{O2}$ and $\ce{H2O}$ at that pH. A couple with an electrode potential above line b has an oxidized form that can oxidize water, releasing $\ce{O2}$; the region above line b is the stability region of $\ce{O2}$.
- Any point on line a represents equilibrium between $\ce{H+}$ and $\ce{H2}$ at that pH. A couple with an electrode potential below line a has a reduced form that can reduce water ($\ce{H+}$), releasing $\ce{H2}$; the region below line a is the stability region of $\ce{H2}$.
- Between lines a and b lies the region of thermodynamic stability of $\ce{H2O}$: oxidizing and reducing agents with electrode potentials in this region can exist stably in water. In neutral solution (pH 7) this interval is $-0.41$ to $0.82\,\mathrm{V}$.

In reality the decomposition of water also has kinetic barriers: evolving $\ce{H2}$ and $\ce{O2}$ at an electrode both require the electrode potential to depart from its equilibrium value by a certain amount (the **overpotential**, 12.4.2: lower for $\ce{H2}$ evolution, higher for $\ce{O2}$ evolution). The actual stability region is therefore wider than that between lines a and b, and in the diagram two dashed lines c and d indicate it (each extended by about $0.5\,\mathrm{V}$; the exact values depend on the electrode material and the current density). For example, $E^\circ(\ce{Cl2}/\ce{Cl-}) = 1.358\,\mathrm{V}$ lies above line b at pH 0, so $\ce{Cl2}$ can in theory oxidize water, but the reaction is very slow and chlorine water can be kept for some time; the same is true of $\ce{KMnO4}$ solution.

![Potential–pH diagram of water (298.15 K, p(H₂) = p(O₂) = p°): between lines a and b is the region of thermodynamic stability of water, and the dashed lines c and d indicate the range extended by overpotential; the potentials of F₂/F⁻ and Na⁺/Na are independent of pH and are horizontal lines, far above line d and far below line c respectively](./plots/water-stability.py)

### 12.3.2. Judging the Stability of Substances in Water

**Example 12.3.1** Decide whether $\ce{F2}$ and $\ce{Na}$ can exist stably in water.

**Solution** For $\ce{F2 + 2e- <=> 2F-}$, $E^\circ = 2.866\,\mathrm{V}$; for $\ce{Na+ + e- <=> Na}$, $E^\circ = -2.71\,\mathrm{V}$. Neither electrode reaction involves $\ce{H+}$ or $\ce{OH-}$, so the potentials are independent of pH and are horizontal lines on the diagram. The former lies above line b and also above line d; the latter lies below line a and also below line c. Even allowing for the stability region extended by overpotential, $\ce{F2}$ and Na cannot exist stably in aqueous solution at any pH: $\ce{F2}$ oxidizes water ($\ce{2F2 + 2H2O -> 4HF + O2}$) and is itself reduced to $\ce{F-}$; Na reduces water ($\ce{2Na + 2H2O -> 2NaOH + H2}$) and is itself oxidized to $\ce{Na+}$. $\square$

For systems containing metals, drawing on the potential–pH diagram the equilibrium lines among the species of the metal (metal, ions, hydroxides, oxoanions) allows one to delineate the immunity, corrosion, and passivation regions of the metal. This is the basic tool for discussing metal corrosion, hydrometallurgy, and geochemistry, and a systematic treatment is found in [Physical Chemistry](/6.3).

## 12.4. Electrolysis

### 12.4.1. Galvanic Cells and Electrolytic Cells

Ni and $\ce{Cl2}$ can form the galvanic cell $(-)\ \ce{Ni} \mid \ce{Ni^2+} \parallel \ce{Cl-} \mid \ce{Cl2}(p^\circ) \mid \ce{Pt}\ (+)$, with cell reaction $\ce{Ni + Cl2 -> Ni^2+ + 2Cl-}$,

$$
E^\circ_{\mathrm{cell}} = 1.358 - (-0.257) = 1.615\,\mathrm{V}, \qquad \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -2 \times 96\,485 \times 1.615\,\mathrm{J\,mol^{-1}} = -311.6\,\mathrm{kJ\,mol^{-1}},
$$
so the forward reaction is spontaneous. The reverse reaction $\ce{Ni^2+ + 2Cl- -> Ni + Cl2}$ cannot occur spontaneously; to force it, the apparatus must be changed into an **electrolytic cell**, with a direct-current voltage greater than $1.615\,\mathrm{V}$ applied between the electrodes to overcome the cell's own electromotive force (the back electromotive force).

**Definition 12.4.1 (Electrolysis)** The process in which, under an applied direct-current voltage, oxidation and reduction occur at the two electrodes in an electrolyte solution or molten electrolyte is called **electrolysis**.

In an electrolytic cell the electrode connected to the positive terminal of the power source is the anode, where oxidation occurs, and the one connected to the negative terminal is the cathode, where reduction occurs. In the example above the cathode reaction is $\ce{Ni^2+ + 2e- -> Ni}$ and the anode reaction is $\ce{2Cl- -> Cl2 + 2e-}$. The electrolysis reaction and the cell reaction are exact reverses of each other; although both are electrochemical reactions, the correspondence between positive/negative polarity and anode/cathode is opposite:

| | **Galvanic cell** | **Electrolytic cell** |
|---|---|---|
| Energy conversion | chemical energy → electrical energy | electrical energy → chemical energy |
| Reaction | $\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$, spontaneous | $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$, forced |
| Anode (oxidation) | negative electrode | positive electrode |
| Cathode (reduction) | positive electrode | negative electrode |
| Electron flow (external circuit) | out of the negative electrode | from the negative terminal of the source into the cathode |

### 12.4.2. Decomposition Voltage and Overpotential

**Definition 12.4.2 (Decomposition Voltage)** The minimum applied voltage necessary for an electrolyte solution to begin to undergo sustained electrolysis is called the **decomposition voltage**. The electromotive force (reversible electromotive force) of the galvanic cell formed by the electrolysis products is called the theoretical decomposition voltage.

The theoretical decomposition voltage in the example above is $1.615\,\mathrm{V}$ (standard conditions). The actual decomposition voltage is always larger than the theoretical value. For example, for the electrolysis of $1\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ solution (that is, of water) at platinum electrodes, the theoretical decomposition voltage is $1.23\,\mathrm{V}$ and the actual value is about $1.7\,\mathrm{V}$. Besides the voltage drop $IR$ caused by the resistance of the electrolyte and contact resistance, the main reason is the overpotential at the electrodes.

**Definition 12.4.3 (Overpotential)** When current flows, the difference between the actual potential $E$ of an electrode and its equilibrium potential $E_{\mathrm{eq}}$ (the value calculated from the Nernst equation)

$$
\eta = E - E_{\mathrm{eq}}
$$
is called the **overpotential** of that electrode.

With this signed IUPAC definition, $\eta > 0$ at an anode (oxidation) and $\eta < 0$ at a cathode (reduction): to drive oxidation at a finite rate the electrode potential must be raised above its equilibrium value, and to drive reduction it must be lowered below it. Many textbooks take the absolute value and define the overpotential as a positive quantity.

Overpotential arises from the finite rate of the electrode reaction itself (electron transfer and bubble formation must cross energy barriers, like the **activation energy** of a reaction) and from concentration changes near the electrode surface. Its magnitude $\lvert\eta\rvert$ varies with electrode material, current density, and temperature: it is larger when gases are evolved and smaller when metals are deposited; the overpotential for $\ce{H2}$ evolution is very small on Pt and very large on Hg, Pb, and Zn. The anode potential is raised by $\eta_{\text{anode}}$ and the cathode potential lowered by $\lvert\eta_{\text{cathode}}\rvert$, so

$$
E_{\text{decomp., actual}} = E_{\text{decomp., theoretical}} + \eta_{\text{anode}} - \eta_{\text{cathode}} + IR = E_{\text{decomp., theoretical}} + \eta_{\text{anode}} + \lvert\eta_{\text{cathode}}\rvert + IR.
$$
Overpotential has both advantages and disadvantages. It wastes electrical energy, but it also makes possible some electrolyses that are thermodynamically unfavorable: $E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.762\,\mathrm{V}$ is far lower than that of $\ce{H+}/\ce{H2}$, yet because the overpotential for $\ce{H2}$ evolution on Zn is large in magnitude, zinc can still be obtained by electrolysis of acidic $\ce{ZnSO4}$ solution; in the electrolysis of brine, although the equilibrium potential of $\ce{O2}/\ce{H2O}$ is lower than that of $\ce{Cl2}/\ce{Cl-}$, the overpotential of $\ce{O2}$ is larger, and $\ce{Cl2}$ is mainly evolved at the anode. The quantitative theory of overpotential (the Tafel and Butler–Volmer equations) is found in [Physical Chemistry](/6.3).

### 12.4.3. Faraday's Laws of Electrolysis

In 1833–1834 Faraday found experimentally that the amount of substance deposited or dissolved at an electrode during electrolysis is proportional to the quantity of charge passed and independent of other factors.

**Theorem 12.4.1 (Faraday's Laws of Electrolysis)** In electrolysis, the amount of substance B that reacts at an electrode is proportional to the charge $Q = It$ passed through the electrode:

$$
n_{\mathrm{B}} = \frac{Q}{zF}, \qquad m_{\mathrm{B}} = \frac{MQ}{zF} = \frac{MIt}{zF},
$$
where $z$ is the number of electrons gained or lost per B in the electrode reaction, $M$ is the molar mass of B, and $F$ is the **Faraday constant**.

| Half-reaction | Mass of 1 mol of product/g | Charge required/C |
|---|---|---|
| $\ce{Na+ + e- -> Na}$ | 22.99 | $1 \times 96\,485$ |
| $\ce{Mg^2+ + 2e- -> Mg}$ | 24.31 | $2 \times 96\,485$ |
| $\ce{Al^3+ + 3e- -> Al}$ | 26.98 | $3 \times 96\,485$ |

Faraday's laws predate the discovery of the electron (J. J. Thomson, 1897) by more than half a century; from today's viewpoint they say only that each ion gains or loses an integral number of electrons at the electrode, so $F$ is the charge of 1 mol of electrons, $N_{\mathrm{A}}e$ (11.4.5 of [6.1.11](/6.1.11)). Historically, it was from the ratio of $F$ to the value of $e$ measured by Millikan that an accurate value of the Avogadro constant was obtained.

The Faraday constant gives the theoretical upper limit of the product obtainable from a given charge. In real electrolysis, side reactions (such as the evolution of $\ce{H2}$ at the cathode), redissolution of the product, or leakage of current mean that less product is obtained than the theoretical amount.

**Definition 12.4.4 (Current Efficiency)** The ratio of the amount of product actually obtained in electrolysis to the theoretical amount calculated from Faraday's laws is called the **current efficiency** (Faradaic efficiency).

**Example 12.4.1** A $\ce{CuSO4}$ solution is electrolyzed for $4.50\,\mathrm{h}$ with a current of $10.0\,\mathrm{A}$, and $50.0\,\mathrm{g}$ of copper is obtained at the cathode. Find the current efficiency.

**Solution** $Q = It = 10.0\,\mathrm{A} \times 4.50 \times 3600\,\mathrm{s} = 1.62\times10^5\,\mathrm{C}$. For $\ce{Cu^2+ + 2e- -> Cu}$, $z = 2$, so

$$
m_{\text{theoretical}} = \frac{63.55\,\mathrm{g\,mol^{-1}} \times 1.62\times10^5\,\mathrm{C}}{2 \times 96\,485\,\mathrm{C\,mol^{-1}}} = 53.4\,\mathrm{g}, \qquad \text{current efficiency} = \frac{50.0}{53.4} = 93.6\%. \qquad \square
$$

## 12.5. Electrochemical Power Sources

**Definition 12.5.1 (Electrochemical Power Source)** A practical device that converts chemical energy directly into electrical energy through a redox reaction is called an **electrochemical power source** (battery). A battery that cannot be restored by recharging after discharge and can be used only once is called a **primary cell**; a battery that can be restored by charging after discharge (an applied current drives the cell reaction in reverse, that is, electrolysis) and used repeatedly is called a **secondary cell** (storage battery, rechargeable battery).

The main criteria for evaluating a battery are voltage (determined by $E_{\mathrm{cell}}$, and lower than the electromotive force during discharge because of internal resistance and overpotential), specific energy (the electrical energy stored per unit mass or volume, $\mathrm{W\,h\,kg^{-1}}$), power, cycle life, and safety. A high voltage requires a high electrode potential for the positive electrode material and a low one for the negative; a high specific energy requires electrode materials of small molar mass that transfer many electrons per mole. This is why lithium ($E^\circ = -3.040\,\mathrm{V}$, $M = 6.94\,\mathrm{g\,mol^{-1}}$) is an ideal negative electrode material.

### 12.5.1. Primary Cells

| Cell | Negative-electrode reaction | Positive-electrode reaction | Voltage |
|---|---|---|---|
| Zinc–carbon dry cell (Leclanché cell) | $\ce{Zn -> Zn^2+ + 2e-}$ | $\ce{2MnO2 + 2NH4+ + 2e- -> 2MnO(OH) + 2NH3}$ | about $1.5\,\mathrm{V}$ |
| Alkaline zinc–manganese dioxide cell | $\ce{Zn + 2OH- -> ZnO + H2O + 2e-}$ | $\ce{MnO2 + H2O + e- -> MnO(OH) + OH-}$ | about $1.5\,\mathrm{V}$ |
| Lithium–manganese dioxide cell | $\ce{Li -> Li+ + e-}$ | $\ce{MnO2 + Li+ + e- -> LiMnO2}$ | about $3\,\mathrm{V}$ |

- The zinc–carbon dry cell has a zinc can as the negative electrode and a carbon rod as the positive electrode, and the electrolyte is a paste of $\ce{NH4Cl}$, $\ce{ZnCl2}$, $\ce{MnO2}$, and carbon powder. $\ce{MnO2}$ is reduced directly at the positive electrode, without going through a step in which $\ce{H2}$ is evolved; the $\ce{NH3}$ formed at the positive electrode combines with the $\ce{Zn^2+}$ formed at the negative electrode into complexes such as $[\ce{Zn(NH3)2}]\ce{Cl2}$. It is inexpensive, but its voltage falls gradually during discharge, and it has been gradually replaced by the alkaline cell.
- The alkaline zinc–manganese dioxide cell has a zinc powder paste as the negative electrode, $\ce{MnO2}$ and graphite powder as the positive electrode, and concentrated $\ce{KOH}$ solution as the electrolyte. Zinc powder has a large surface area and $\ce{OH-}$ conducts well, so the capacity and high-current discharge performance are much better than those of the dry cell. In early cells the zinc powder was amalgamated to suppress corrosion of the zinc and hydrogen evolution; current alkaline cells are mercury-free.
- The lithium–manganese dioxide cell has metallic lithium as the negative electrode and $\ce{MnO2}$ as the positive electrode, with a nonaqueous organic electrolyte (lithium reacts violently with water). In the cell reaction $\ce{Li + MnO2 -> LiMnO2}$, $\ce{Li+}$ is inserted into the crystal lattice of $\ce{MnO2}$; the cell has a high voltage, a high specific energy, and low self-discharge, and is often used for coin cells and cameras.

### 12.5.2. Lead–Acid, Nickel–Cadmium, and Nickel–Metal Hydride Cells

| Cell | Negative-electrode reaction (discharge) | Positive-electrode reaction (discharge) | Voltage |
|---|---|---|---|
| Lead–acid battery | $\ce{Pb + HSO4- -> PbSO4 + H+ + 2e-}$ | $\ce{PbO2 + 3H+ + HSO4- + 2e- -> PbSO4 + 2H2O}$ | about $2.0\,\mathrm{V}$ |
| Nickel–cadmium cell | $\ce{Cd + 2OH- -> Cd(OH)2 + 2e-}$ | $\ce{NiO(OH) + H2O + e- -> Ni(OH)2 + OH-}$ | about $1.2\,\mathrm{V}$ |
| Nickel–metal hydride cell | $\ce{MH + OH- -> M + H2O + e-}$ | $\ce{NiO(OH) + H2O + e- -> Ni(OH)2 + OH-}$ | about $1.2\,\mathrm{V}$ |

The overall reactions of the cells (to the right is discharge, to the left is charge):

$$
\begin{aligned}
&\text{lead–acid:} && \ce{Pb + PbO2 + 2H+ + 2HSO4- <=> 2PbSO4 + 2H2O},\\
&\text{nickel–cadmium:} && \ce{Cd + 2NiO(OH) + 2H2O <=> Cd(OH)2 + 2Ni(OH)2},\\
&\text{nickel–metal hydride:} && \ce{MH + NiO(OH) <=> M + Ni(OH)2}.
\end{aligned}
$$

- The lead–acid battery has spongy lead as the negative electrode, $\ce{PbO2}$ as the positive electrode, and dilute sulfuric acid as the electrolyte. During discharge $\ce{PbSO4}$ forms at both electrodes, sulfuric acid is consumed, and the density falls, so the state of charge can be judged from the density of the electrolyte; the open-circuit voltage is about $2.0$–$2.1\,\mathrm{V}$ and varies with the sulfuric acid concentration. Its specific energy is low, but it is inexpensive, performs well at high current, and is easy to recycle, and it is still widely used for starting automobiles and for backup power.
- The nickel–cadmium cell has spongy cadmium as the negative electrode, nickel oxyhydroxide $\ce{NiO(OH)}$ as the positive electrode, and $\ce{KOH}$ solution as the electrolyte. It has a long cycle life, tolerates overcharge and overdischarge, and performs well at low temperature, but it has a memory effect and cadmium is toxic, so it has been largely phased out of consumer products.
- The nickel–metal hydride cell uses a hydrogen-absorbing alloy M (such as an $\ce{LaNi5}$-type alloy) instead of cadmium as the negative electrode; on charging, hydrogen enters the alloy lattice as atoms to form MH, and on discharge it is oxidized. The positive electrode is the same as in the nickel–cadmium cell. It contains no cadmium and has a higher specific energy; it was widely used in portable devices and is now mainly used in hybrid vehicles.

### 12.5.3. Lithium-Ion Batteries

**Definition 12.5.2 (Lithium-Ion Battery)** A secondary cell in which both electrodes are materials that can reversibly insert and extract $\ce{Li+}$, so that on charging and discharging $\ce{Li+}$ shuttles between the electrodes through a nonaqueous electrolyte while electrons flow through the external circuit, is called a **lithium-ion battery**.

Take the lithium cobalt oxide–graphite cell, the first to be commercialized (1991), as an example (discharge to the right):

$$
\begin{aligned}
&\text{negative electrode:} && \mathrm{Li}_x\mathrm{C}_6 \to 6\,\mathrm{C} + x\,\mathrm{Li}^+ + x\,\mathrm{e}^-,\\
&\text{positive electrode:} && \mathrm{Li}_{1-x}\mathrm{CoO}_2 + x\,\mathrm{Li}^+ + x\,\mathrm{e}^- \to \mathrm{LiCoO}_2,\\
&\text{overall:} && \mathrm{Li}_x\mathrm{C}_6 + \mathrm{Li}_{1-x}\mathrm{CoO}_2 \rightleftharpoons 6\,\mathrm{C} + \mathrm{LiCoO}_2 \quad (0 < x < 1).
\end{aligned}
$$
There is never any metallic lithium in the cell, and $\ce{Li+}$ merely "rocks" back and forth between two layered or framework structures, so it is also called a rocking-chair battery. The voltage is about $3.7\,\mathrm{V}$, and the specific energy is two to three times that of nickel–metal hydride cells.

Present-day lithium-ion batteries are distinguished mainly by their positive electrode material:

| Positive electrode material | Structure | Average voltage | Characteristics and uses |
|---|---|---|---|
| $\ce{LiCoO2}$ (LCO) | layered | about $3.7\,\mathrm{V}$ | high volumetric specific energy; cobalt is expensive; used in mobile phones and other small electronic devices |
| $\mathrm{LiNi}_x\mathrm{Mn}_y\mathrm{Co}_z\mathrm{O}_2$ ($x + y + z = 1$, NMC) | layered | about $3.6$–$3.7\,\mathrm{V}$ | nickel and manganese partly replace cobalt; high specific energy; one of the mainstream choices for electric vehicles |
| $\ce{LiFePO4}$ (LFP) | olivine | about $3.2\,\mathrm{V}$ | lower specific energy, but good thermal stability, long cycle life, and no cobalt; used in electric vehicles and energy storage stations |

The negative electrode is usually graphite, in which $\ce{Li+}$ is inserted between the layers, reaching the composition $\ce{LiC6}$ when full. On the first charge, the organic electrolyte is reduced at the negative electrode surface, forming a layer that conducts $\ce{Li+}$ but not electrons, the solid electrolyte interphase (SEI); it prevents further decomposition of the electrolyte and is the key to stable cycling of the cell. The electrolyte is commonly a carbonate solution of $\ce{LiPF6}$, which is flammable and may cause thermal runaway on overcharge or short circuit, the root of the safety problems of lithium-ion batteries.

Batteries containing cadmium or mercury have been restricted or phased out by regulations in many countries because of heavy-metal pollution; the lead, cobalt, nickel, and lithium in spent batteries should all be recycled. The structure and electrochemical performance of electrode materials and the kinetics of electrode processes are found in [Physical Chemistry](/6.3).

## Summary

| Topic | Key points |
|---|---|
| Equilibrium constants | $\lg K^\circ = zE^\circ_{\mathrm{cell}}/(0.05916\,\mathrm{V})$ (298.15 K); $K^\circ$ changes with the way the equation is written, $E^\circ$ does not; the "0.3 V" criterion holds only for $z = 1$ and $K^\circ \ge 10^5$ |
| Other applications | Comparing oxidizing and reducing power, choosing reagents, determining $K_{\mathrm{sp}}$ and $\beta$, deciding direction; indicates only possibility, not rate |
| Latimer diagrams | $E^\circ = \sum z_iE^\circ_i/\sum z_i$ (what is added is $zE^\circ$); the middle species disproportionates when $E^\circ_{\text{right}} > E^\circ_{\text{left}}$ |
| Frost diagrams | Ordinate $NE^\circ$; slope of a line = $E^\circ$ of the couple; the lowest point is the most stable; convex points disproportionate, concave points are formed by comproportionation |
| Potential–pH diagrams | Stability region of water: $-0.0592\,\mathrm{pH} < E/\mathrm{V} < 1.229 - 0.0592\,\mathrm{pH}$; overpotential enlarges the actual stability region |
| Electrolysis | Oxidation at the anode, reduction at the cathode; actual decomposition voltage = theoretical value + overpotential + $IR$; $m = MIt/(zF)$; current efficiency |
| Electrochemical power sources | Primary cells (zinc–carbon, alkaline zinc–manganese dioxide, lithium–manganese dioxide); secondary cells (lead–acid, nickel–cadmium, nickel–metal hydride, lithium-ion); lithium-ion batteries rely on insertion and extraction of $\ce{Li+}$ at the electrodes |

## Questions

1. Why can the $E^\circ$ values of adjacent couples in a Latimer diagram not simply be added to obtain the $E^\circ$ of a nonadjacent couple?

   **Answer** $E^\circ$ is an intensive quantity; what can be added is $zE^\circ$, which is proportional to $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, and the sum is then divided by the total number of electrons.

2. Use the Frost diagram of manganese to explain why $\ce{KMnO4}$ is reduced to $\ce{Mn^2+}$ in acidic solution but usually only to $\ce{MnO2}$ in basic solution.

   **Answer** In the acidic diagram $\ce{Mn^2+}$ is the lowest point; in the basic diagram $\ce{MnO2}$ is the lowest point ($\ce{Mn(OH)2}$ is close to it), and the line from $\ce{MnO4-}$ to $\ce{MnO2}$ is already quite flat, so the driving force for reduction beyond $\ce{MnO2}$ is small.

3. Why is $\ce{H2}$ rather than Na obtained at the cathode in the electrolysis of aqueous $\ce{NaCl}$?

   **Answer** $E^\circ(\ce{Na+}/\ce{Na}) = -2.71\,\mathrm{V}$ is far below the potential at which water is reduced (about $-0.41\,\mathrm{V}$ in neutral solution, only about $-1\,\mathrm{V}$ even with overpotential), so water is reduced preferentially. Sodium can be obtained only with a mercury cathode (Na dissolves in mercury to form an amalgam, which shifts the potential positively, and the overpotential of $\ce{H2}$ on mercury is very large) or by electrolysis of molten $\ce{NaCl}$.
