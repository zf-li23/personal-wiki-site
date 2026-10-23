---
title: Reversible Cells and Electromotive Force
description: Reversible cells and the three kinds of reversible electrodes; terminal voltage, the compensation method and the standard cell; the Nernst equation from the reaction isotherm, and the relations of the cell potential to ΔrG, K°, ΔrS, ΔrH and the reversible heat; inner and outer potentials and the electrochemical potential, the components of the cell potential and the liquid junction potential; electrode potentials and reference electrodes; concentration cells and the design of cells for given reactions; potentiometric determination of equilibrium constants, activity coefficients, standard electrode potentials, transport numbers and pH; the Fe–H₂O potential–pH diagram; membrane potentials, the resting potential of cells and the glass electrode.
source_hash: 97494b92a34e
---

[6.3.12](/6.3.12) studied the electrolyte solution itself; this chapter studies the equilibrium properties of a cell when the current tends to zero. The chemical reaction in the cell then proceeds reversibly, and the measured cell potential gives the molar Gibbs energy of the reaction directly: $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$. The cell potential can be measured to $10^{-5}\,\mathrm{V}$ or better, so electrochemical measurement is an accurate method for determining $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, $K^\circ$, $\Delta_{\mathrm{r}}S_{\mathrm{m}}$, $\Delta_{\mathrm{r}}H_{\mathrm{m}}$, mean activity coefficients and pH.

[6.1.11](/6.1.11) and [6.1.12](/6.1.12) introduced the basic uses of galvanic cells, cell diagrams, electrode potentials, the Nernst equation, concentration cells and potential–pH diagrams; there concentrations were used in place of activities and the thermodynamic foundations were only sketched. This chapter places those results on the rigorous basis of [6.3.3](/6.3.3) (the Gibbs criterion and the Gibbs–Helmholtz equation), [6.3.6](/6.3.6) (activity) and [6.3.7](/6.3.7) (the reaction isotherm). We write the Nernst equation in terms of activities (13.3), use the electrochemical potential to analyze which interfacial potential differences make up the cell potential (13.4), and discuss systematically the applications of the potentiometric method (13.7) and potential–pH diagrams (13.8). The last section treats membrane potentials: the potential produced by the difference in ion concentrations across a cell membrane underlies nerve impulses and cellular energy conversion. When current flows, the electrodes depart from equilibrium; that is the subject of [6.3.14](/6.3.14).

## 13.1. Reversible Cells and Reversible Electrodes

### 13.1.1. Conditions for Converting Chemical Energy into Electrical Energy

The same reaction $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$ can be carried out in a beaker or in a cell. The initial and final states of the two routes are the same, and so are the changes of the state functions ($\Delta_{\mathrm{r}}G$, $\Delta_{\mathrm{r}}H$, $\Delta_{\mathrm{r}}S$), but the work and heat differ:

| | Thermochemical reaction (in a beaker) | Electrochemical reaction (in a cell) |
|---|---|---|
| Reactants | In direct contact; electrons transferred in collisions | Spatially separated, reacting at two electrodes |
| Path of the electrons | Very short, random | Through the external circuit, directed |
| What determines the rate | Temperature, concentration (activation energy comes from thermal motion) | Also the electrode potential ([6.3.14](/6.3.14)) |
| Form of energy | All released as heat, $W' = 0$, $Q_p = \Delta_{\mathrm{r}}H$ | Electrical work + heat, $Q_p \ne \Delta_{\mathrm{r}}H$ |

Only redox reactions, or reactions containing redox steps (such as precipitation and neutralization reactions, 13.6.2), can be designed as cells, with the path of electron transfer extended into the external circuit.

At constant temperature and pressure, the change in the Gibbs energy of a system is no greater than the **non-expansion work** done on it by the surroundings: $(\Delta_{\mathrm{r}}G)_{T,p} \le W'$, with equality for a reversible process ([6.3.3](/6.3.3), [6.1.6](/6.1.6)). When a cell does electrical work on the surroundings, $W' < 0$. If $z\,\mathrm{mol}$ of electrons pass through the external circuit for an extent of reaction of $1\,\mathrm{mol}$, the quantity of electricity is $zF$, and the electrical work done on the system by the surroundings at a potential difference $U$ between the electrodes is $W' = -zFU$. In reversible discharge the potential difference between the electrodes is the **electromotive force** $E_{\mathrm{cell}}$ of the cell (the $\mathcal{E}$ of [5.3.5](/5.3.5)), so that

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}\quad(\text{reversible}), \qquad -\Delta_{\mathrm{r}}G_{\mathrm{m}} > zFU\quad(\text{irreversible discharge}). \tag{13.1}
$$
In reversible operation the chemical energy $-\Delta_{\mathrm{r}}G_{\mathrm{m}}$ is converted entirely into electrical work; in irreversible operation only part of it is, and the rest is dissipated as heat. Equation (13.1) links a property of the reaction ($\Delta_{\mathrm{r}}G_{\mathrm{m}}$) to a property of the cell ($E_{\mathrm{cell}}$) and is the foundation of this chapter; it holds only for reversible cells.

### 13.1.2. Reversible Cells

**Definition 13.1.1** A cell that satisfies the following two conditions is called a **reversible cell**:

1. Material reversibility: the electrode reactions and the overall reaction on discharge proceed completely in the reverse direction on charging under an opposing applied voltage, so that the system can be restored; there are no irreversible processes such as the junction of two different electrolyte solutions.
2. Energy reversibility: the cell is charged and discharged with the current tending to zero, delivering the maximum electrical work on discharge and consuming the minimum electrical work on charging; there is no dissipation such as Joule heating when current passes through the cell, and the surroundings can also be restored.

For example, in $\ce{Zn} \mid \ce{ZnCl2}(\mathrm{aq}) \mid \ce{AgCl(s)} \mid \ce{Ag}$, the discharge reaction is $\ce{Zn + 2AgCl -> Zn^2+ + 2Cl- + 2Ag}$ and charging exactly reverses it. By contrast, in a Volta cell formed by immersing Zn and Cu in dilute sulfuric acid, $\ce{H2}$ is evolved at the cathode on discharge, whereas on charging it is Cu that dissolves at the anode; the reactions on charge and discharge differ, and the cell is not reversible.

The reversible cell is an idealized limit; it gives the upper bound on the conversion of chemical energy into electrical energy and is a tool for measuring thermodynamic quantities. Strictly, only a single-liquid cell (both electrodes share one electrolyte solution) can be reversible; in a two-liquid cell the diffusion at the junction of the two solutions is irreversible (13.4.6), and after a salt bridge has reduced the liquid junction potential to a negligible value, the cell is treated approximately as reversible.

### 13.1.3. Cell Diagrams and Cell Reactions

The rules for writing a **cell diagram** are given in [6.1.11](/6.1.11): the negative electrode (anode) is written on the left and the positive electrode (cathode) on the right, in the order in which the substances are in contact; $\mid$ denotes a phase boundary, $\parallel$ a salt bridge that has eliminated the liquid junction potential, and $\vdots$ (or a dashed $\mid$) a direct junction of two solutions; substances in the same phase are separated by commas; the temperature (if not stated, $298.15\,\mathrm{K}$), the phase of each substance, the concentration (activity) of solutions and the partial pressures of gases are specified.

The cell reaction is the overall change that occurs at the two electrodes and in the whole cell on discharge: oxidation at the left electrode and reduction at the right electrode, added after the numbers of electrons have been made equal. In writing a cell reaction:

1. The two electrode reactions must involve the same number of electrons; $z$ is the number of electrons transferred when the cell reaction as written proceeds by $1\,\mathrm{mol}$.
2. Do not combine ions into electrolyte molecules arbitrarily; a species can be cancelled between the two sides only if it is in the same phase and the same state.
3. Do not include in the equation species that are not in the cell diagram (except $\ce{H2O}$ in aqueous solution).

| Cell | Electrode reactions | Cell reaction ($z$) |
|---|---|---|
| $\ce{Pt} \mid \ce{H2}(p) \mid \ce{HCl}(b) \mid \ce{AgCl(s)} \mid \ce{Ag}$ | Left $\tfrac12\ce{H2 -> H+ + e-}$; right $\ce{AgCl + e- -> Ag + Cl-}$ | $\tfrac12\ce{H2 + AgCl -> Ag + H+ + Cl-}$ (1) |
| $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{KOH}(b) \mid \ce{O2}(p_2) \mid \ce{Pt}$ | Left $\ce{2H2 + 4OH- -> 4H2O + 4e-}$; right $\ce{O2 + 2H2O + 4e- -> 4OH-}$ | $\ce{2H2 + O2 -> 2H2O}$ (4) |
| $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 0.1) \parallel \ce{Fe^3+}(a = 0.2), \ce{Fe^2+}(a = 0.05) \mid \ce{Pt}$ | Left $\tfrac12\ce{H2 -> H+ + e-}$; right $\ce{Fe^3+ + e- -> Fe^2+}$ | $\tfrac12\ce{H2 + Fe^3+ -> H+ + Fe^2+}$ (1) |
| $\ce{Pt} \mid \ce{O2}(p^\circ) \mid \ce{HCl}(b_1) \parallel \ce{HCl}(b_2) \mid \ce{O2}(p^\circ) \mid \ce{Pt}$ | Left $\ce{H2O -> 2H+}(b_1) + \tfrac12\ce{O2 + 2e-}$; right $\ce{2H+}(b_2) + \tfrac12\ce{O2 + 2e- -> H2O}$ | $\ce{2H+}(b_2) \to \ce{2H+}(b_1)$ (2) |

### 13.1.4. Types of Reversible Electrodes

**Definition 13.1.2** An electrode at which the electrode reaction can proceed reversibly and the exchange current is large enough ([6.3.14](/6.3.14)) for the potential to stabilize at the value given by the Nernst equation is called a **reversible electrode**. According to the phases in which the species taking part in the electrode reaction are found, they are commonly divided into three kinds:

1. **Electrodes of the first kind**: those with a single phase boundary, including metal electrodes formed by a metal immersed in a solution containing its own ions ($\ce{Zn^2+} \mid \ce{Zn}$), amalgam electrodes ($\ce{Na+} \mid \ce{Na(Hg)}$), and gas electrodes, in which a gas adsorbed on an inert metal (Pt) is in contact with the corresponding ions in solution (hydrogen, oxygen and halogen electrodes).
2. **Electrodes of the second kind**: a metal surface covered with a layer of a sparingly soluble salt (or oxide) of the metal and immersed in a solution containing the anion of the sparingly soluble salt (or $\ce{H+}$, $\ce{OH-}$); the species taking part in the electrode reaction are in three phases, for example $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$, $\ce{Cl-} \mid \ce{Hg2Cl2(s)} \mid \ce{Hg}$ and $\ce{OH-} \mid \ce{HgO(s)} \mid \ce{Hg}$.
3. **Redox electrodes** (electrodes of the third kind): an inert metal immersed in a solution containing two oxidation states of the same element; all the species taking part in the electrode reaction are in solution and the metal merely conducts electrons, for example $\ce{Fe^3+}, \ce{Fe^2+} \mid \ce{Pt}$, $\ce{Cr2O7^2-}, \ce{Cr^3+}, \ce{H+} \mid \ce{Pt}$ and the quinhydrone electrode.

| Electrode | Electrode reaction (reduction form) | Remarks |
|---|---|---|
| $\ce{Cu^2+} \mid \ce{Cu}$ | $\ce{Cu^2+ + 2e- <=> Cu}$ | First kind |
| $\ce{Na+} \mid \ce{Na(Hg)}(a)$ | $\ce{Na+ + e- + Hg <=> Na(Hg)}(a)$ | First kind; Na dissolved in mercury has an activity below 1 and does not react violently with water; amalgam electrolysis is one of the methods for preparing reactive metals |
| $\ce{H+} \mid \ce{H2}(p) \mid \ce{Pt}$; $\ce{OH-} \mid \ce{H2}(p) \mid \ce{Pt}$ | $\ce{2H+ + 2e- <=> H2}$; $\ce{2H2O + 2e- <=> H2 + 2OH-}$ | First kind; the electrode reactions in acidic and basic media differ, as do the $E^\circ$ ($0$ and $-0.8277\,\mathrm{V}$) |
| $\ce{OH-} \mid \ce{O2}(p) \mid \ce{Pt}$ | $\ce{O2 + 2H2O + 4e- <=> 4OH-}$ | First kind; $E^\circ = 0.401\,\mathrm{V}$ |
| $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$ | $\ce{AgCl + e- <=> Ag + Cl-}$ | Second kind; $E^\circ = 0.22233\,\mathrm{V}$ |
| $\ce{H+} \mid \ce{Ag2O(s)} \mid \ce{Ag}$ | $\ce{Ag2O + 2H+ + 2e- <=> 2Ag + H2O}$ | Second kind (sparingly soluble oxide) |
| $\ce{Sn^4+}, \ce{Sn^2+} \mid \ce{Pt}$ | $\ce{Sn^4+ + 2e- <=> Sn^2+}$ | Redox electrode |

The significance of electrodes of the second kind is that they are reversible to anions, have stable potentials and are easy to prepare, so they are often used as reference electrodes (13.5.2). A gas electrode must be specified with the partial pressure of the gas; the ion concentration in the solution must not be too low (generally above $10^{-6}$–$10^{-8}\,\mathrm{mol\,L^{-1}}$), otherwise the exchange current is too small and the potential unstable.

## 13.2. Measurement of the Cell Potential

### 13.2.1. Electromotive Force and Terminal Voltage

**Definition 13.2.1** The potential difference between the two electrodes of a cell during discharge is called the **terminal voltage** of the cell, denoted $U$.

Let the electromotive force of the cell be $E_{\mathrm{cell}}$, its internal resistance $R_{\mathrm{i}}$ and the resistance of the external circuit $R_{\mathrm{o}}$. By **Ohm's law** for the complete circuit ([5.3.5](/5.3.5)), $E_{\mathrm{cell}} = I(R_{\mathrm{o}} + R_{\mathrm{i}})$ and $U = IR_{\mathrm{o}}$, so

$$
\frac{U}{E_{\mathrm{cell}}} = \frac{R_{\mathrm{o}}}{R_{\mathrm{o}} + R_{\mathrm{i}}}.
$$
Only as $R_{\mathrm{o}} \to \infty$ ($I \to 0$) does $U \to E_{\mathrm{cell}}$. When a real cell discharges, the terminal voltage is lowered further by electrode polarization ([6.3.14](/6.3.14)), so an ordinary voltmeter measures the terminal voltage, not the electromotive force.

### 13.2.2. The Compensation Method

**Definition 13.2.2** The method of determining the electromotive force by using a working source of adjustable voltage to produce a voltage equal in magnitude and opposite in direction to the electromotive force of the cell under test, so that the current through the cell is zero (the galvanometer reads zero), is called the **compensation method** (potentiometric compensation).

In the classical potentiometer, the working cell $E_{\mathrm{w}}$ sets up a steady potential drop across a uniform slide-wire resistor $AB$. A standard cell of known electromotive force $E_{\mathrm{s}}$ is connected first and the slider adjusted to $H$ until the galvanometer reads zero; the cell under test $E_x$ is then connected and the slider adjusted to $C$ until the galvanometer reads zero, whence $E_x = E_{\mathrm{s}}\cdot\overline{AC}/\overline{AH}$. At balance there is no current in the cell under test, so the conditions for using a reversible cell are met. Today the measurement is usually made with a digital voltmeter or electrometer with an input impedance above $10^{12}\,\Omega$; the current through the cell is below $10^{-12}\,\mathrm{A}$, and the principle is the same: the zero-current condition is unchanged.

The electromotive force is by nature a positive quantity. To make Eq. (13.1) valid for any way of writing a cell, we define $E_{\mathrm{cell}} = E_{\text{right}} - E_{\text{left}}$ (the electrode potential of the right electrode minus that of the left). Then, if the cell reaction as written in the cell diagram proceeds spontaneously, $\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$ and $E_{\mathrm{cell}} > 0$; if $E_{\mathrm{cell}} < 0$, the actual positive and negative electrodes are opposite to those written and the reaction as written proceeds spontaneously in the reverse direction; $E_{\mathrm{cell}} = 0$ means that the reaction is at equilibrium and the cell has no capacity to do work. For example, $\ce{Zn} \mid \ce{Zn^2+} \parallel \ce{Cu^2+} \mid \ce{Cu}$ has $E_{\mathrm{cell}} > 0$, whereas $\ce{Cu} \mid \ce{Cu^2+} \parallel \ce{Zn^2+} \mid \ce{Zn}$ has $E_{\mathrm{cell}} < 0$.

### 13.2.3. The Standard Cell

**Definition 13.2.3** A cell whose electromotive force is known, stable and reproducible, with a very small temperature coefficient, used to calibrate potentiometers, is called a **standard cell**. The most common is the Weston standard cell:

$$
\ce{Cd(Hg)}(w_{\ce{Cd}} = 0.125) \mid \ce{CdSO4 * 8/3H2O(s)} \mid \ce{CdSO4}(\text{saturated}) \mid \ce{Hg2SO4(s)} \mid \ce{Hg(l)}.
$$

The negative electrode reaction is $\ce{Cd(Hg) -> Cd^2+ + 2e-}$, the positive electrode reaction is $\ce{Hg2SO4 + 2e- -> 2Hg + SO4^2-}$, and the cell reaction is $\ce{Cd(Hg) + Hg2SO4 + 8/3H2O -> CdSO4 * 8/3H2O + 2Hg}$. At $20\,^\circ\mathrm{C}$ the electromotive force is about $1.0186\,\mathrm{V}$, with a temperature coefficient of only about $-4\times10^{-5}\,\mathrm{V\,K^{-1}}$.

The reason for its stability can be understood from the phase diagram of [6.3.9](/6.3.9): at room temperature, when the mass fraction of Cd in the Cd–Hg system lies between about 0.05 and 0.14, the system is in the two-phase region of liquid amalgam and solid solution, and the compositions of the two phases are fixed by the temperature independently of the overall composition, so the activity of Cd in the cadmium amalgam is constant; the solution is a saturated solution of $\ce{CdSO4}$ in contact with the solid phase $\ce{CdSO4 * 8/3H2O}$, so its activity is constant too. With the activities of all the substances in the cell reaction constant, the electromotive force is constant.

The Weston cell (1893) served as the material standard of voltage for almost a century. Since 1990 the metrological standard of voltage has been the Josephson effect: a superconducting tunnel junction irradiated by microwaves of frequency $f$ shows quantized voltage steps $U = nf/K_{\mathrm{J}}$. Since the SI was redefined in 2019 in terms of fixed constants, $K_{\mathrm{J}} = 2e/h$ is exact, and the volt is realized directly from a frequency and fundamental constants. The Weston cell has left metrology and is used only in some teaching laboratories and older potentiometers.

## 13.3. Thermodynamics of Cells

### 13.3.1. The Nernst Equation

For any cell reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$, the **reaction isotherm** ([6.3.7](/6.3.7)) gives $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}$.

**Definition 13.3.1** The electromotive force of a cell in which all the substances taking part in the cell reaction are in their respective standard states is called the **standard cell potential** of the cell, denoted $E^\circ_{\mathrm{cell}}$. By Eq. (13.1), $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$, and it is a function of temperature only.

**Theorem 13.3.1 (Nernst Equation)** The electromotive force of a reversible cell is related to the activities of the substances taking part in the cell reaction by

$$
E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{13.2}
$$

**Proof** Imagine $1\,\mathrm{mol}$ of reaction taking place in a very large cell, so that the activities of the substances do not change and the cell delivers a quantity of electricity $zF$. Substitute $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$ and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$ into the reaction isotherm and divide both sides by $-zF$. $\square$

This is the rigorous form of [Theorem 11.5.1 of 6.1.11](/6.1.11#thm-11.5.1): the concentration ratio there is replaced here by activities. For solutes we use $a_{\mathrm{B}} = \gamma_{\mathrm{B}}b_{\mathrm{B}}/b^\circ$; for gases, $p_{\mathrm{B}}/p^\circ$ (for ideal gases; strictly, the fugacity); the activity of a pure solid or pure liquid is 1, and that of the solvent water in dilute solution is approximately 1. The activities of individual ions in an electrolyte solution cannot be measured; in the equation they always occur in electrically neutral combinations, which can be written as $a_\pm$ (Example 13.3.1).

### 13.3.2. The Cell Potential and the Way the Reaction Equation Is Written

The cell potential is an intensive property of the cell and does not depend on how the stoichiometric equation of the cell reaction is written, whereas $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ and $K^\circ$ change with the way it is written. Take $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{OH-} \mid \ce{O2}(p_2) \mid \ce{Pt}$ as an example:

$$
\begin{aligned}
&(1)\ \ce{H2 + 1/2O2 -> H2O}, \quad z = 2, && E_1 = E^\circ_1 - \frac{RT}{2F}\ln\frac{a(\ce{H2O})}{(p_1/p^\circ)(p_2/p^\circ)^{1/2}};\\
&(2)\ \ce{2H2 + O2 -> 2H2O}, \quad z = 4, && E_2 = E^\circ_2 - \frac{RT}{4F}\ln\frac{a(\ce{H2O})^2}{(p_1/p^\circ)^2(p_2/p^\circ)}.
\end{aligned}
$$
Here $\Delta_{\mathrm{r}}G_{\mathrm{m}}(2) = 2\Delta_{\mathrm{r}}G_{\mathrm{m}}(1)$ and $z_2 = 2z_1$, and their ratio $E = -\Delta_{\mathrm{r}}G_{\mathrm{m}}/(zF)$ is unchanged: $E_1 = E_2$ and $E^\circ_1 = E^\circ_2 = 1.229\,\mathrm{V}$.

But if the same overall reaction is carried out in different cells with different ways of electron transfer, the cell potentials differ. The reaction $\ce{Cu^2+ + Cu -> 2Cu+}$ can be designed as two cells:

$$
(1)\ \ce{Cu} \mid \ce{Cu+} \parallel \ce{Cu+}, \ce{Cu^2+} \mid \ce{Pt}\ (z = 1), \qquad (2)\ \ce{Cu} \mid \ce{Cu^2+} \parallel \ce{Cu+}, \ce{Cu^2+} \mid \ce{Pt}\ (z = 2).
$$
The electrode reactions of cell (1) are $\ce{Cu -> Cu+ + e-}$ and $\ce{Cu^2+ + e- -> Cu+}$; those of cell (2) are $\ce{Cu -> Cu^2+ + 2e-}$ and $\ce{2Cu^2+ + 2e- -> 2Cu+}$. The two have the same overall reaction, the same $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, and deliver the same electrical work, but $z_2 = 2z_1$, so $E^\circ_1 = 2E^\circ_2$. From the Latimer diagram of copper in [6.1.12](/6.1.12), $E^\circ_1 = 0.153 - 0.521 = -0.368\,\mathrm{V}$ and $E^\circ_2 = -0.184\,\mathrm{V}$; both are negative: $\ce{Cu+}$ disproportionates in water. (If one computes directly with the tabulated value $E^\circ(\ce{Cu^2+}/\ce{Cu}) = 0.342\,\mathrm{V}$, then $E^\circ_2 = 0.153 - 0.342 = -0.189\,\mathrm{V}$; the 5 mV difference comes from the independent determinations and rounding of the three tabulated values, whereas strict thermodynamics requires $E^\circ(\ce{Cu^2+}/\ce{Cu}) = [E^\circ(\ce{Cu^2+}/\ce{Cu+}) + E^\circ(\ce{Cu+}/\ce{Cu})]/2$.)

**Example 13.3.1** Find the cell potential of the cell $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(b = 0.100\,\mathrm{mol\,kg^{-1}}) \mid \ce{Cl2}(2p^\circ) \mid \ce{Pt}$ at $298.15\,\mathrm{K}$. For $0.100\,\mathrm{mol\,kg^{-1}}$ $\ce{HCl}$, $\gamma_\pm = 0.796$.

**Solution** The cell reaction is $\ce{H2}(p^\circ) + \ce{Cl2}(2p^\circ) \to \ce{2H+ + 2Cl-}$, $z = 2$, $E^\circ_{\mathrm{cell}} = E^\circ(\ce{Cl2}/\ce{Cl-}) - 0 = 1.358\,\mathrm{V}$. We have $a(\ce{H+})a(\ce{Cl-}) = a_\pm^2 = (\gamma_\pm b/b^\circ)^2 = 0.0796^2$, so

$$
E_{\mathrm{cell}} = 1.358\,\mathrm{V} - \frac{0.05916\,\mathrm{V}}{2}\lg\frac{0.0796^4}{1\times2} = 1.358 + 0.139 = 1.497\,\mathrm{V}.
$$
If the reaction is written $\tfrac12\ce{H2} + \tfrac12\ce{Cl2 -> HCl(aq)}$, with $z = 1$, then $E_{\mathrm{cell}} = 1.358 - 0.05916\lg[0.0796^2/2^{1/2}]$, with the same result. Neglecting the activity coefficient gives $1.485\,\mathrm{V}$, an error of 12 mV, which is already a large error in electrochemistry. $\square$

### 13.3.3. Standard Cell Potential and Equilibrium Constant

From $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ = -zFE^\circ_{\mathrm{cell}}$,

$$
\ln K^\circ = \frac{zFE^\circ_{\mathrm{cell}}}{RT}, \qquad \lg K^\circ = \frac{zE^\circ_{\mathrm{cell}}}{0.05916\,\mathrm{V}}\quad(298.15\,\mathrm{K}). \tag{13.3}
$$
$E^\circ_{\mathrm{cell}}$ does not depend on how the equation is written, whereas $z$ and $K^\circ$ do: in cases (1) and (2) above, $K^\circ_2 = (K^\circ_1)^2$. Each increase of $0.1\,\mathrm{V}$ in $E^\circ_{\mathrm{cell}}$ (for $z = 1$) increases $K^\circ$ by a factor of about 50; the Daniell cell, with $z = 2$ and $E^\circ_{\mathrm{cell}} = 1.1\,\mathrm{V}$, corresponds to $K^\circ \approx 10^{37}$ ([6.1.11](/6.1.11)). When the cell potential is zero the cell reaction is at equilibrium, where $\prod a_{\mathrm{B}}^{\nu_{\mathrm{B}}} = K^\circ$, and the Nernst equation is an electrical measure of "how far from equilibrium": $E_{\mathrm{cell}} = (RT/zF)\ln(K^\circ/Q)$.

### 13.3.4. Temperature Coefficient of the Cell Potential and the Entropy and Enthalpy of Reaction

From $(\partial G/\partial T)_p = -S$ ([6.3.3](/6.3.3)), differentiating Eq. (13.1) gives the following.

**Definition 13.3.2** The rate of change of the cell potential with temperature at constant pressure, $(\partial E_{\mathrm{cell}}/\partial T)_p$, is called the **temperature coefficient of the cell potential**.

**Theorem 13.3.2** The molar entropy change, molar enthalpy change and reversible heat of a reversible cell reaction are

$$
\Delta_{\mathrm{r}}S_{\mathrm{m}} = zF\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p, \qquad \Delta_{\mathrm{r}}H_{\mathrm{m}} = -zFE_{\mathrm{cell}} + zFT\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p, \qquad Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} = zFT\left(\frac{\partial E_{\mathrm{cell}}}{\partial T}\right)_p. \tag{13.4}
$$

**Proof** $\Delta_{\mathrm{r}}S_{\mathrm{m}} = -(\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}/\partial T)_p = zF(\partial E_{\mathrm{cell}}/\partial T)_p$; $\Delta_{\mathrm{r}}H_{\mathrm{m}} = \Delta_{\mathrm{r}}G_{\mathrm{m}} + T\Delta_{\mathrm{r}}S_{\mathrm{m}}$; the heat of a reversible process is $Q_{\mathrm{r}} = T\Delta S$. The second formula is the **Gibbs–Helmholtz equation** ([6.3.3](/6.3.3)) applied to a cell. $\square$

Some remarks:

- A cell does non-expansion work, so the reversible heat $Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}}$ is not equal to $\Delta_{\mathrm{r}}H_{\mathrm{m}}$. By the first law, at constant pressure $\Delta_{\mathrm{r}}H_{\mathrm{m}} = Q + W'$, and in reversible operation $W' = -zFE_{\mathrm{cell}}$: part of the decrease in enthalpy does electrical work and part is released as heat (or heat is even absorbed from the surroundings to do the electrical work).
- A cell with $(\partial E/\partial T)_p > 0$ absorbs heat from the surroundings in reversible operation ($Q_{\mathrm{r}} > 0$), and its electromotive force increases with temperature; a cell with $(\partial E/\partial T)_p < 0$ releases heat, and its electromotive force decreases with temperature. The electrical work done by a heat-absorbing cell exceeds $-\Delta_{\mathrm{r}}H_{\mathrm{m}}$, and the "heat-to-electricity efficiency" $W'/\Delta_{\mathrm{r}}H_{\mathrm{m}}$ exceeds 100%. This does not violate the second law: the extra energy comes from heat of the surroundings, and the entropy of the system increases.
- For a cell without gas electrodes, the $E$–$T$ relation is approximately linear over a modest temperature range and the temperature coefficient can be measured very accurately, so $\Delta_{\mathrm{r}}H_{\mathrm{m}}$ obtained by the potentiometric method is often more accurate than that from calorimetry, and the method can be used for reactions that are hard to carry out directly in a calorimeter.

**Example 13.3.2** The cell $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{KCl}(\mathrm{aq}) \mid \ce{Hg2Cl2(s)} \mid \ce{Hg(l)}$ has a cell potential of $0.0455\,\mathrm{V}$ and a temperature coefficient of $3.38\times10^{-4}\,\mathrm{V\,K^{-1}}$ at $298.15\,\mathrm{K}$. Find $\Delta_{\mathrm{r}}G_{\mathrm{m}}$, $\Delta_{\mathrm{r}}S_{\mathrm{m}}$, $\Delta_{\mathrm{r}}H_{\mathrm{m}}$ and the reversible heat of the cell reaction, and compare with thermodynamic tables.

**Solution** Left: $\ce{Ag + Cl- -> AgCl + e-}$; right: $\tfrac12\ce{Hg2Cl2 + e- -> Hg + Cl-}$; cell reaction: $\ce{Ag} + \tfrac12\ce{Hg2Cl2 -> AgCl + Hg}$, $z = 1$. No species in solution appears in the reaction and all substances are pure solids or liquids, so $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}}$, independent of the $\ce{KCl}$ concentration ($E^\circ(\ce{Hg2Cl2}/\ce{Hg}) - E^\circ(\ce{AgCl}/\ce{Ag}) = 0.26808 - 0.22233 = 0.04575\,\mathrm{V}$).

$$
\begin{aligned}
\Delta_{\mathrm{r}}G_{\mathrm{m}} &= -96\,485 \times 0.0455\,\mathrm{J\,mol^{-1}} = -4.39\,\mathrm{kJ\,mol^{-1}},\\
\Delta_{\mathrm{r}}S_{\mathrm{m}} &= 96\,485 \times 3.38\times10^{-4}\,\mathrm{J\,mol^{-1}\,K^{-1}} = 32.6\,\mathrm{J\,mol^{-1}\,K^{-1}},\\
\Delta_{\mathrm{r}}H_{\mathrm{m}} &= -4.39 + 298.15\times32.6\times10^{-3} = 5.33\,\mathrm{kJ\,mol^{-1}}, \qquad Q_{\mathrm{r}} = 9.72\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
This is an endothermic reaction, yet it proceeds spontaneously and does work: the driving force is the increase in entropy. In reversible operation the cell absorbs $9.72\,\mathrm{kJ}$ of heat from the surroundings, of which $5.33\,\mathrm{kJ}$ goes into increasing the enthalpy of the system and $4.39\,\mathrm{kJ}$ is converted into electrical work. From the CRC values of $\Delta_{\mathrm{f}}H^\circ$ ($\ce{AgCl}$ $-127.0$, $\ce{Hg2Cl2}$ $-265.4\,\mathrm{kJ\,mol^{-1}}$) we obtain $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 5.7\,\mathrm{kJ\,mol^{-1}}$, and from $S^\circ$ we obtain $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = 33.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$, in agreement within the uncertainty of the data. $\square$

### 13.3.5. Heat Effects of Irreversible Discharge

When the same reaction is carried out under different conditions, $\Delta_{\mathrm{r}}H_{\mathrm{m}}$ is the same but the heat differs. At constant temperature and pressure, $Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} - W'$; when a cell discharges at terminal voltage $U$, $W' = -zFU$, so

$$
Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} + zFU, \qquad U = E_{\mathrm{cell}}:\ Q = Q_{\mathrm{r}};\qquad U = 0\ (\text{short circuit}):\ Q = \Delta_{\mathrm{r}}H_{\mathrm{m}}.
$$

**Example 13.3.3** The amalgams in the cell $\ce{Pb(Hg)}(x_{\ce{Pb}} = 0.0165) \mid \ce{Pb(NO3)2}(\mathrm{aq}) \mid \ce{Pb(Hg)}(x_{\ce{Pb}} = 0.000625)$ may be regarded as **ideal dilute solutions**. (1) Find the cell potential at $25\,^\circ\mathrm{C}$. When $2F$ of electricity is discharged at $25\,^\circ\mathrm{C}$ and $101.325\,\mathrm{kPa}$, find the heat absorbed by the cell for (2) reversible discharge, (3) a short circuit, and (4) a terminal voltage of $0.8E_{\mathrm{cell}}$.

**Solution** (1) Left: $\ce{Pb}(x_1) \to \ce{Pb^2+ + 2e-}$; right: $\ce{Pb^2+ + 2e- ->}\ \ce{Pb}(x_2)$; cell reaction: $\ce{Pb}(x_1) \to \ce{Pb}(x_2)$. This is an electrode concentration cell with $E^\circ_{\mathrm{cell}} = 0$, and

$$
E_{\mathrm{cell}} = -\frac{RT}{2F}\ln\frac{x_2}{x_1} = 0.012\,85\,\mathrm{V}\times\ln\frac{0.0165}{0.000625} = 0.0420\,\mathrm{V}.
$$
(2) In an ideal dilute solution the partial molar enthalpy of the solute is independent of concentration, so $\Delta_{\mathrm{r}}H_{\mathrm{m}} = 0$; $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}} = -8.11\,\mathrm{kJ\,mol^{-1}}$, and $Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}} - \Delta_{\mathrm{r}}G_{\mathrm{m}} = 8.11\,\mathrm{kJ}$ (heat absorbed). (3) In a short circuit $W' = 0$ and $Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} = 0$. (4) $Q = 0 + 2\times96\,485\times0.8\times0.0420\,\mathrm{J} = 6.49\,\mathrm{kJ}$ (heat absorbed).

The driving force of this cell is entirely entropy: Pb "diffuses" from the concentrated to the dilute amalgam. In reversible operation it converts all the heat absorbed from the surroundings into electrical work; in a short circuit it does no work and absorbs no heat, and the entropy increase of $27.2\,\mathrm{J\,K^{-1}}$ is entirely irreversible entropy production. (Many textbooks write the heat here as $\Delta U - (p\Delta V + W_{\mathrm{e}})$ and take work done by the system as positive; with the convention of this book that quantities received by the system are positive, the value is the same.) $\square$

**Example 13.3.4** A cell with a reversible electromotive force of $1.07\,\mathrm{V}$ is placed in a large thermostat at $20\,^\circ\mathrm{C}$ and short-circuited to discharge $1000\,\mathrm{C}$; the reaction in the cell is the same as in reversible discharge of $1000\,\mathrm{C}$. Find the total entropy change of the cell and the thermostat.

**Solution** In a short circuit $W' = 0$; the cell releases heat $Q = \Delta H$, the thermostat receives $-\Delta H$, and $\Delta S_{\text{bath}} = -\Delta H/T$. The entropy change $\Delta S$ of the cell is independent of the process, so

$$
\Delta S_{\text{total}} = \Delta S - \frac{\Delta H}{T} = -\frac{\Delta G}{T} = \frac{QE_{\mathrm{cell}}}{T} = \frac{1000\,\mathrm{C}\times1.07\,\mathrm{V}}{293.15\,\mathrm{K}} = 3.65\,\mathrm{J\,K^{-1}}.
$$
To find the entropy changes of the cell and of the thermostat separately, the temperature coefficient (which gives $\Delta S$) or the enthalpy of reaction is also needed. $\square$

## 13.4. Interphase Potentials and the Electrochemical Potential

### 13.4.1. Inner, Outer and Surface Potentials

The cell potential is the potential difference measured between two terminals of the same metal. To understand what it is composed of, we must consider the change in energy when a charged particle passes from one phase into another. Imagine moving a test point charge from vacuum at infinity into the interior of phase $\alpha$.

**Definition 13.4.1** The electrical work done in moving a unit positive charge from infinity (in vacuum) to a point just outside the surface of phase $\alpha$ (about $10^{-6}\,\mathrm{m}$, already beyond the range of the image-charge forces at the surface) is called the **outer electric potential** $\psi^\alpha$ of phase $\alpha$ (the Volta potential); the work done in moving it from just outside the surface into the interior is called the **surface electric potential** $\chi^\alpha$ of phase $\alpha$; and their sum $\varphi^\alpha = \psi^\alpha + \chi^\alpha$ is called the **inner electric potential** of phase $\alpha$ (the Galvani potential).

The outer potential is determined by the net charge carried by the phase and can be measured. The surface potential arises from the oriented dipole layer at the surface (the "spill-out" of electrons at a metal surface, the orientation of water molecules at the water surface); it is independent of the net charge on the phase and cannot be measured. Hence the inner potential cannot be measured either. (Here $\chi$ has the same form as the symbol for electronegativity and is used only in this section.)

### 13.4.2. The Electrochemical Potential

When a charged species B (charge number $z_{\mathrm{B}}$) enters phase $\alpha$, in addition to the energy change related to chemical composition, electrical work $z_{\mathrm{B}}F\varphi^\alpha$ (per mole) is done. The two parts cannot be separated experimentally.

**Definition 13.4.2** The **electrochemical potential** of a charged species B in phase $\alpha$ is

$$
\tilde\mu^\alpha_{\mathrm{B}} = \mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\alpha = \mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\psi^\alpha + z_{\mathrm{B}}F\chi^\alpha,
$$
where $\mu^\alpha_{\mathrm{B}}$ is the "chemical" part (the chemical potential of B when phase $\alpha$ carries no net charge and there is no external field). For an uncharged species, $\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}}$.

The electrochemical potential is the generalization of the chemical potential of [6.3.4](/6.3.4) to the presence of an electric field: the fundamental equation of thermodynamics for a charged system of variable composition is $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\tilde\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$. Only $\tilde\mu_{\mathrm{B}}$ has a well-defined physical meaning; splitting it into $\mu_{\mathrm{B}}$ and $z_{\mathrm{B}}F\varphi$ has no operational meaning for a single ion in one phase, which is why the activity of a single ion cannot be measured ([6.3.12](/6.3.12)).

**Theorem 13.4.1 (Electrochemical Potential Criterion)** At constant temperature and pressure, a charged species B transfers spontaneously from the phase of higher electrochemical potential to the phase of lower electrochemical potential; the condition for equilibrium of B between two phases is $\tilde\mu^\alpha_{\mathrm{B}} = \tilde\mu^\beta_{\mathrm{B}}$. When an electrochemical reaction $0 = \sum\nu_{\mathrm{B}}\mathrm{B}$ (including electrons) occurs at a phase boundary, the condition for equilibrium is $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\tilde\mu_{\mathrm{B}} = 0$, and the spontaneous direction is that in which $\sum\nu_{\mathrm{B}}\tilde\mu_{\mathrm{B}} < 0$.

**Proof** As for the chemical potential criterion ([6.3.4](/6.3.4)): when $\mathrm{d}n$ mol of B passes from $\alpha$ to $\beta$, $\mathrm{d}G = (\tilde\mu^\beta_{\mathrm{B}} - \tilde\mu^\alpha_{\mathrm{B}})\,\mathrm{d}n$; a spontaneous process requires $\mathrm{d}G < 0$, and at equilibrium $\mathrm{d}G = 0$. The case of a reaction is the same. $\square$

**Definition 13.4.3** The difference of the inner potentials of two phases, $\Delta^\beta_\alpha\varphi = \varphi^\beta - \varphi^\alpha$, is called the **Galvani potential difference** (inner potential difference) between them; the difference of the outer potentials, $\Delta^\beta_\alpha\psi = \psi^\beta - \psi^\alpha$, is called the **Volta potential difference** (outer potential difference, contact potential difference).

By Theorem 13.4.1, if ion B can pass freely between the two phases and reach equilibrium, then $\mu^\alpha_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\alpha = \mu^\beta_{\mathrm{B}} + z_{\mathrm{B}}F\varphi^\beta$, so that

$$
\Delta^\beta_\alpha\varphi = -\frac{\mu^\beta_{\mathrm{B}} - \mu^\alpha_{\mathrm{B}}}{z_{\mathrm{B}}F}. \tag{13.5}
$$
The inner potential difference between two phases is thus formed by the difference of the chemical potentials of the ion in the two phases: ions cross the interface from the side of higher chemical potential, and the opposite charge left behind forms an electric double layer with them; the resulting potential difference just prevents further transfer. In general, only the Galvani potential difference between two phases of the same composition (the same metal, the same solution) can be measured, because then $\mu^\alpha_{\mathrm{B}} = \mu^\beta_{\mathrm{B}}$ and the difference of electrochemical potentials is just the potential difference.

### 13.4.3. Components of the Cell Potential

In the cell $\ce{Cu}' \mid \ce{Zn} \mid \ce{Zn^2+}(\mathrm{aq}) \parallel \ce{Cu^2+}(\mathrm{aq}) \mid \ce{Cu}$ both ends are copper (the $\ce{Cu}'$ at the left end is a copper lead connected to the Zn), and the measured cell potential is the inner potential difference of the two copper ends, $E_{\mathrm{cell}} = \varphi^{\ce{Cu}} - \varphi^{\ce{Cu}'}$, which is the algebraic sum of the Galvani potential differences at the phase boundaries in the circuit:

$$
E_{\mathrm{cell}} = \Delta^{\ce{Zn}}_{\ce{Cu}'}\varphi + \Delta^{\mathrm{S}}_{\ce{Zn}}\varphi + \Delta^{\mathrm{S'}}_{\mathrm{S}}\varphi + \Delta^{\ce{Cu}}_{\mathrm{S'}}\varphi,
$$
which are, in turn, the potential differences at the metal junction, the Zn/solution interface, the liquid junction (made approximately zero by the salt bridge) and the solution/Cu interface. The Galvani potential difference of a single interface cannot be measured, but their sum can be, and it is completely determined by thermodynamics.

The electrochemical potential allows this to be shown directly. At zero current every interface is at equilibrium. Electrons are in equilibrium between Zn and $\ce{Cu}'$: $\tilde\mu_{\mathrm{e}}(\ce{Zn}) = \tilde\mu_{\mathrm{e}}(\ce{Cu}')$; the reactions at the two electrode interfaces are in equilibrium:

$$
\mu_{\ce{Zn}} = \tilde\mu_{\ce{Zn^2+}}(\mathrm{S}) + 2\tilde\mu_{\mathrm{e}}(\ce{Cu}'), \qquad \tilde\mu_{\ce{Cu^2+}}(\mathrm{S'}) + 2\tilde\mu_{\mathrm{e}}(\ce{Cu}) = \mu_{\ce{Cu}}.
$$
Subtracting the two, and assuming an ideal salt bridge so that $\varphi^{\mathrm{S}} = \varphi^{\mathrm{S'}}$, the $z_{\mathrm{B}}F\varphi$ terms of the ions in solution cancel:

$$
2[\tilde\mu_{\mathrm{e}}(\ce{Cu}) - \tilde\mu_{\mathrm{e}}(\ce{Cu}')] = \mu_{\ce{Cu}} + \mu_{\ce{Zn^2+}} - \mu_{\ce{Zn}} - \mu_{\ce{Cu^2+}} = \Delta_{\mathrm{r}}G_{\mathrm{m}}.
$$
Both ends are the same metal, so the chemical part of the electron's potential is the same, and $\tilde\mu_{\mathrm{e}}(\ce{Cu}) - \tilde\mu_{\mathrm{e}}(\ce{Cu}') = -F(\varphi^{\ce{Cu}} - \varphi^{\ce{Cu}'}) = -FE_{\mathrm{cell}}$, so that $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -2FE_{\mathrm{cell}}$. This recovers Eq. (13.1) from the standpoint of interfacial equilibrium: the cell potential is the difference of the electrochemical potentials of the electrons in the two terminals (that is, the difference of the Fermi levels, [5.5.6](/5.5.6)) divided by $-F$.

### 13.4.4. Metal Contact Potential

When two metals are in contact, electrons flow from the metal with the smaller **work function** to the one with the larger work function until the electrochemical potentials of the electrons on the two sides are equal; an electric double layer forms at the interface, and a Volta potential difference (contact potential difference) appears between the two metals, approximately equal to the difference of their work functions divided by $e$ and as large as a few tenths of a volt. The proof above shows that when leads of the same metal are taken from both ends of the cell, this kind of junction potential is already included in the thermodynamic result and need not be considered separately.

The contact potential itself cannot be measured with a voltmeter: in a closed circuit at uniform temperature the potential differences at the junctions sum to zero. The electromotive force of a thermocouple arises from the **Seebeck effect** caused by a temperature gradient ([5.3.5](/5.3.5)), that is, from the different response of the electron transport in the two metals to the temperature gradient, not from the contact potential itself; a net electromotive force appears in the circuit only when the two junctions are at different temperatures, which is why a thermocouple can measure temperature.

### 13.4.5. The Electrode–Solution Interface

When an electrode is in contact with a solution, an **electric double layer** forms on the two sides of the interface ([6.1.11](/6.1.11)): on the metal side it is the excess charge on the surface (less than 0.1 nm thick); on the solution side it consists of the compact layer next to the electrode (about 0.3–0.5 nm, containing adsorbed ions and oriented water molecules) and the diffuse layer extending into the solution. The thickness of the diffuse layer is the Debye length $\lambda_{\mathrm{D}}$ ([6.3.12](/6.3.12); about 1 nm at $0.1\,\mathrm{mol\,kg^{-1}}$). The potential difference across the compact layer can reach 1 V and the field strength $10^9$–$10^{10}\,\mathrm{V\,m^{-1}}$, three orders of magnitude larger than the breakdown field of air; this is why an electrode can change the activation energy of a reaction with very high efficiency ([6.3.14](/6.3.14)). The solution within the double layer is not electrically neutral; only at the potential of zero charge does the electrode surface carry no excess charge. Models of the double-layer structure (Helmholtz, Gouy–Chapman, Stern) are closely related to the stability of colloids and are discussed systematically in [6.3.21](/6.3.21).

### 13.4.6. The Liquid Junction Potential

The **liquid junction potential** ([6.1.11](/6.1.11)) arises at the junction of two electrolyte solutions of different composition or concentration. Take $\ce{HCl}(b_1) \mid \ce{HCl}(b_2)$ ($b_1 > b_2$) as an example: both $\ce{H+}$ and $\ce{Cl-}$ diffuse from the concentrated side to the dilute side; $\ce{H+}$ is faster, so the dilute side first becomes positively charged; the resulting electric field slows $\ce{H+}$ and accelerates $\ce{Cl-}$, and a steady state in which the two ions diffuse at the same rate is soon reached, with the potential difference at the interface stabilizing at a value denoted $E_{\mathrm{l}} = \varphi_{\text{right}} - \varphi_{\text{left}}$. This is an irreversible steady state; the liquid junction potential disappears only after the two solutions have been in contact so long that their concentrations become equal.

The liquid junction potential can be calculated in the zero-current approximation. When $1\,\mathrm{mol}$ of positive charge passes through the interface from left to right in the cell, $t_+/z_+$ mol of cations move from left (1) to right (2) and $t_-/\lvert z_-\rvert$ mol of anions move from right to left, and the change in Gibbs energy of the process is

$$
\Delta G = \frac{t_+}{z_+}RT\ln\frac{a_+(2)}{a_+(1)} + \frac{t_-}{\lvert z_-\rvert}RT\ln\frac{a_-(1)}{a_-(2)}.
$$
For two concentrations of the same electrolyte, we approximate the activity ratios of the single ions on the two sides by $a_\pm(2)/a_\pm(1)$, and then from $\Delta G = -FE_{\mathrm{l}}$,

$$
E_{\mathrm{l}} = \left(\frac{t_+}{z_+} - \frac{t_-}{\lvert z_-\rvert}\right)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}, \qquad \text{1-1 type:}\ E_{\mathrm{l}} = (t_+ - t_-)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}. \tag{13.6}
$$
Here $t_\pm$ are taken near the interface (the average of the two concentrations). When the cation is faster ($t_+ > t_-$) and the concentrated solution is on the left, $E_{\mathrm{l}} > 0$, in agreement with the qualitative analysis above.

**Example 13.4.1** Estimate the liquid junction potentials at $25\,^\circ\mathrm{C}$ of $\ce{HCl}(0.100\,\mathrm{mol\,kg^{-1}}) \mid \ce{HCl}(0.0100\,\mathrm{mol\,kg^{-1}})$ and of the same concentrations of $\ce{KCl}$ solution. $t(\ce{H+}) = 0.83$ and $t(\ce{K+}) = 0.49$; for both electrolytes take $\gamma_\pm$ approximately as the values for $\ce{HCl}$ in the table of [6.3.12](/6.3.12).

**Solution** $a_\pm(1)/a_\pm(2) = (0.796\times0.100)/(0.905\times0.0100) = 8.80$, and $\lg 8.80 = 0.944$.

$$
E_{\mathrm{l}}(\ce{HCl}) = (0.83 - 0.17)\times0.05916\,\mathrm{V}\times0.944 = 0.037\,\mathrm{V}, \qquad E_{\mathrm{l}}(\ce{KCl}) = (0.49 - 0.51)\times0.05916\times0.944\,\mathrm{V} \approx -1\,\mathrm{mV}.
$$
The liquid junction potential between the $\ce{HCl}$ solutions reaches 37 mV, whereas for $\ce{KCl}$, because $t_+ \approx t_-$, it is only about 1 mV. $\square$

The function of a salt bridge rests on this fact: two solutions are connected by a saturated (about $4.2\,\mathrm{mol\,L^{-1}}$) $\ce{KCl}$ agar gel, forming two liquid junctions at which the migration is carried mainly by the large amounts of $\ce{K+}$ and $\ce{Cl-}$; the two transport numbers are close, so each junction potential is small, and the two have opposite signs, so the sum is generally below 1–2 mV. The requirements for a salt bridge are that the transport numbers of the cation and anion be close, that the concentration be much higher than that of the solutions connected, and that it not react with substances in the solutions (for solutions containing $\ce{Ag+}$, a $\ce{KNO3}$ or $\ce{NH4NO3}$ bridge is used instead).

## 13.5. Electrode Potentials

### 13.5.1. Reduction Electrode Potential on the Hydrogen Scale

The Galvani potential difference of a single electrode cannot be measured, so the electrode potential can only be defined as a relative value: with the **standard hydrogen electrode** $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 1)$ as the left electrode and the electrode under study as the right electrode, the cell potential of this cell is the **electrode potential** $E$ of the electrode under study ([Definition 11.4.4 of 6.1.11](/6.1.11#def-11.4.4), with activities here in place of concentrations). By this convention, reduction occurs at the electrode under study, so the electrode potential is a "reduction potential": the higher $E$ is, the more easily the oxidized form of the couple is reduced; $E^\circ(\ce{H+}/\ce{H2}) = 0$ at any temperature.

**Theorem 13.5.1** For an electrode reaction $\text{oxidized form} + z\ce{e-} \to \text{reduced form}$, that is, $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B} - z\ce{e-}$ (with $\nu_{\mathrm{B}} > 0$ for the reduced form), the electrode potential is

$$
E = E^\circ - \frac{RT}{zF}\ln\prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}} = E^\circ + \frac{RT}{zF}\ln\frac{a_{\text{ox}}}{a_{\text{red}}}. \tag{13.7}
$$

**Proof** The reaction of the cell $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+}(a = 1) \parallel \text{electrode under study}$ is $\text{oxidized form} + \tfrac z2\ce{H2} \to \text{reduced form} + z\ce{H+}$, with $a(\ce{H+}) = 1$ and $p(\ce{H2}) = p^\circ$; substitution into Eq. (13.2) gives the result. $\square$

For example, for $\ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$: $E = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln a(\ce{Cl-})$. The standard cell potential is $E^\circ_{\mathrm{cell}} = E^\circ_{\text{right}} - E^\circ_{\text{left}}$; $E^\circ$ is a function of temperature only, and its values at $298.15\,\mathrm{K}$ are in the table of [6.1.11](/6.1.11).

The standard hydrogen electrode requires an $\ce{H+}$ activity of exactly 1, for example $1.184\,\mathrm{mol\,kg^{-1}}$ $\ce{HCl}$ ($\gamma_\pm \approx 0.845$). Its drawbacks are that its preparation and use are very demanding (pure $\ce{H2}$; the platinum black is easily poisoned) and its potential is not stable enough, so reference electrodes are used in routine measurements.

### 13.5.2. Reference Electrodes

The commonly used **reference electrodes** are all electrodes of the second kind, whose potentials depend only on the activity of $\ce{Cl-}$:

| Reference electrode ($25\,^\circ\mathrm{C}$) | $E$ / V (vs SHE) |
|---|---|
| **Calomel electrode** $\ce{Hg} \mid \ce{Hg2Cl2(s)} \mid \ce{KCl}(0.1\,\mathrm{mol\,L^{-1}})$ | 0.3337 |
| Calomel electrode, $\ce{KCl}(1\,\mathrm{mol\,L^{-1}})$ | 0.2801 |
| Saturated calomel electrode (SCE) | 0.2412 |
| $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{KCl}$ (saturated) | 0.197 |
| $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-}(a = 1)$ | 0.22233 |

($E^\circ(\ce{Hg2Cl2}/\ce{Hg}) = 0.26808\,\mathrm{V}$.) The saturated calomel electrode is easy to prepare and has a stable and reliable potential; it was the most widely used reference electrode in laboratories, but it contains mercury and has now largely been replaced by the $\ce{Ag}/\ce{AgCl}$ electrode. Almost all microelectrodes in biology and medicine are $\ce{Ag}/\ce{AgCl}$.

### 13.5.3. Calculating the Cell Potential from Electrode Potentials

There are three equivalent ways to calculate a cell potential: from $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ ($E = -\Delta_{\mathrm{r}}G_{\mathrm{m}}/zF$); from the Nernst equation (13.2) of the cell reaction; and from the two electrode potentials, $E_{\mathrm{cell}} = E_{\text{right}} - E_{\text{left}}$, each electrode potential being calculated for the reduction reaction by Eq. (13.7). The last method rests on the additivity of Gibbs energies: cell reaction = reduction at the right electrode − reduction at the left electrode, and $\Delta_{\mathrm{r}}G_{\mathrm{m}} = (-zFE_{\text{right}}) - (-zFE_{\text{left}})$.

**Example 13.5.1** Write the cell potential of $\ce{Zn} \mid \ce{Zn^2+}(a_1) \parallel \ce{Cu^2+}(a_2) \mid \ce{Cu}$ in two ways.

**Solution** Method 1: $E_{\mathrm{cell}} = \left[E^\circ(\ce{Cu^2+}/\ce{Cu}) + \frac{RT}{2F}\ln a_2\right] - \left[E^\circ(\ce{Zn^2+}/\ce{Zn}) + \frac{RT}{2F}\ln a_1\right]$. Method 2: the cell reaction is $\ce{Zn + Cu^2+ -> Zn^2+ + Cu}$, $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{2F}\ln\frac{a_1}{a_2}$, with $E^\circ_{\mathrm{cell}} = 0.342 - (-0.762) = 1.104\,\mathrm{V}$. The two expressions are the same. $\square$

The standard electrode potentials of related couples cannot be added or subtracted directly; they must be combined through $\Delta_{\mathrm{r}}G^\circ = -zFE^\circ$ ([Theorem 12.2.1 of 6.1.12](/6.1.12#thm-12.2.1)): $E^\circ$ is intensive, and it is $zE^\circ$ that is additive.

## 13.6. Classification and Design of Cells

### 13.6.1. Chemical Cells and Concentration Cells

| Type | Cell reaction | Example | Cell potential |
|---|---|---|---|
| Chemical cell without liquid junction (single-liquid cell) | Chemical change | $\ce{Zn} \mid \ce{ZnCl2}(b) \mid \ce{AgCl(s)} \mid \ce{Ag}$ | $E^\circ - \frac{RT}{2F}\ln a(\ce{ZnCl2})$, $a(\ce{ZnCl2}) = a_\pm^3$ |
| Chemical cell with liquid junction | Chemical change | $\ce{Zn} \mid \ce{ZnSO4} \vdots \ce{CuSO4} \mid \ce{Cu}$ | Calculated value + liquid junction potential; usually eliminated with a salt bridge |
| Electrode concentration cell | Electrode substance transferred from one concentration (partial pressure) to another | $\ce{Pt} \mid \ce{H2}(p_1) \mid \ce{HCl} \mid \ce{H2}(p_2) \mid \ce{Pt}$; amalgam concentration cell (Example 13.3.3) | $E^\circ = 0$, $E = \frac{RT}{2F}\ln\frac{p_1}{p_2}$ |
| Electrolyte concentration cell (without transference) | Electrolyte transferred from one concentration to another | Two single-liquid cells back to back: $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \mid \ce{H2} \mid \ce{Pt} \mid \ce{H2} \mid \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$ | $\frac{2RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$ |
| Electrolyte concentration cell (with transference) | Same, through a liquid junction | $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \vdots \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$ | $2t_+\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$ (13.7.5) |

A **concentration cell** ([Definition 11.5.1 of 6.1.11](/6.1.11#def-11.5.1)) has $E^\circ_{\mathrm{cell}} = 0$, and its driving force is entirely the transfer of substance from high to low activity, that is, the entropy of mixing. For example, the cell $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(\mathrm{aq}) \mid \ce{H2}(0.1p^\circ) \mid \ce{Pt}$ has the cell reaction $\ce{H2}(p^\circ) \to \ce{H2}(0.1p^\circ)$ and $E_{\mathrm{cell}} = \frac{RT}{2F}\ln10 = 0.0296\,\mathrm{V}$. If an electrolyte concentration cell is used without a salt bridge, the measured cell potential exceeds the value calculated from the electrode reactions by the liquid junction potential: the method of calculating the cell potential above applies only to reversible cells.

### 13.6.2. Designing a Cell for a Given Reaction

The steps for designing a cell for a given reaction are: (1) find the species oxidized and reduced in the reaction (for a reaction with no change in oxidation state, add the same substance to both sides to construct oxidation and reduction half-reactions); (2) put the oxidized couple as the left electrode and the reduced couple as the right electrode; (3) write the cell diagram, then write the cell reaction from the cell and check that it agrees with the original reaction.

| Reaction | Cell |
|---|---|
| $\ce{H2 + Cl2 -> 2HCl(aq)}$ | $\ce{Pt} \mid \ce{H2} \mid \ce{HCl}(\mathrm{aq}) \mid \ce{Cl2} \mid \ce{Pt}$ |
| $\ce{Zn + 2Cu^2+ -> Zn^2+ + 2Cu+}$ | $\ce{Zn} \mid \ce{Zn^2+} \parallel \ce{Cu^2+}, \ce{Cu+} \mid \ce{Pt}$ |
| $\ce{AgCl(s) + I- -> AgI(s) + Cl-}$ (adding Ag to both sides: $\ce{Ag + I- -> AgI + e-}$, $\ce{AgCl + e- -> Ag + Cl-}$) | $\ce{Ag} \mid \ce{AgI(s)} \mid \ce{I-} \parallel \ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$ |
| $\ce{Ag+ + Cl- -> AgCl(s)}$ | $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{Cl-} \parallel \ce{Ag+} \mid \ce{Ag}$ |
| $\ce{H2O -> H+ + OH-}$ (adding $\tfrac12\ce{H2}$ to both sides) | $\ce{Pt} \mid \ce{H2}(p) \mid \ce{H+} \parallel \ce{OH-} \mid \ce{H2}(p) \mid \ce{Pt}$ |
| $\ce{HgO(s) -> Hg(l) + 1/2O2}$ | The reverse of $\ce{Pt} \mid \ce{O2}(p) \mid \ce{NaOH}(\mathrm{aq}) \mid \ce{HgO(s)} \mid \ce{Hg}$ |

The last row can be used to measure the decomposition pressure of $\ce{HgO}$: both electrodes of the cell $\ce{Pt} \mid \ce{O2} \mid \ce{NaOH}(\mathrm{aq}) \mid \ce{HgO(s)} \mid \ce{Hg}$ are reversible to $\ce{OH-}$ ($\ce{O2 + 2H2O + 4e- -> 4OH-}$, $\ce{HgO + H2O + 2e- -> Hg + 2OH-}$), and the cell reaction $\ce{Hg + 1/2O2 -> HgO}$ contains no species of the solution, so $E$ is independent of the concentration of the base; in $\ce{H2SO4}$ the $\ce{HgO}$ would dissolve and in pure water the conductivity is too poor, so neither is suitable.

## 13.7. Applications of the Potentiometric Method

**Definition 13.7.1** The method of designing a suitable reversible cell, measuring its cell potential accurately and from it determining thermodynamic quantities, equilibrium constants, activity coefficients, pH and so on is called the **potentiometric method**.

The advantage of the potentiometric method is its high precision, which permits the determination of very small or very large equilibrium constants; its limitation is that it applies only to reactions that can be designed as reversible cells. The general procedure is to design the cell, prepare it and measure $E_{\mathrm{cell}}$, and calculate the desired quantity from $E_{\mathrm{cell}}$.

### 13.7.1. Equilibrium Constants

By Eq. (13.3), a measured or tabulated $E^\circ_{\mathrm{cell}}$ gives $K^\circ$.

**Example 13.7.1** Find the ion product of water and the solubility product of $\ce{AgCl}$ at $25\,^\circ\mathrm{C}$ from standard electrode potentials.

**Solution** (1) The cell is $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{H+} \parallel \ce{OH-} \mid \ce{H2}(p^\circ) \mid \ce{Pt}$, with right electrode reaction $\ce{H2O + e- -> 1/2H2 + OH-}$ and left electrode reaction $\tfrac12\ce{H2 -> H+ + e-}$; the cell reaction is $\ce{H2O -> H+ + OH-}$, $z = 1$, and $E^\circ_{\mathrm{cell}} = E^\circ(\ce{H2O}/\ce{H2}, \ce{OH-}) - 0 = -0.8277\,\mathrm{V}$, so

$$
K_{\mathrm{w}} = \exp\frac{FE^\circ_{\mathrm{cell}}}{RT} = \exp\left(-\frac{0.8277}{0.025\,693}\right) = \exp(-32.22) = 1.02\times10^{-14}.
$$
(2) For the cell $\ce{Ag} \mid \ce{Ag+} \parallel \ce{Cl-} \mid \ce{AgCl(s)} \mid \ce{Ag}$, the cell reaction is $\ce{AgCl -> Ag+ + Cl-}$, $E^\circ_{\mathrm{cell}} = 0.22233 - 0.7996 = -0.5773\,\mathrm{V}$, and $K_{\mathrm{sp}} = \exp(-0.5773/0.025\,693) = 1.75\times10^{-10}$, in agreement with the $1.8\times10^{-10}$ of [6.1.10](/6.1.10). Note that only the dissolution equilibrium of $\ce{AgCl}$ may appear in the cell designed; in a cell such as $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl} \mid \ce{Cl2} \mid \ce{Pt}$, the cell reaction is the formation of $\ce{AgCl}$ and what is obtained is $\Delta_{\mathrm{f}}G^\circ(\ce{AgCl})$. $\square$

### 13.7.2. Entropy and Enthalpy Changes of Reactions

By Theorem 13.3.2, measuring $E_{\mathrm{cell}}$ at several temperatures and finding the temperature coefficient gives $\Delta_{\mathrm{r}}S_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}H_{\mathrm{m}}$ (Example 13.3.2). Compared with calorimetry, the potentiometric method measures an equilibrium property, is not limited by the reaction rate, and is often more precise; the same data also give $\Delta_{\mathrm{r}}G_{\mathrm{m}}$, and the three are self-consistent.

### 13.7.3. Mean Activity Coefficients

In a single-liquid cell whose cell reaction involves only one electrolyte, the cell potential gives the mean activity of that electrolyte directly. The most classical is the Harned cell

$$
\ce{Pt} \mid \ce{H2}(p^\circ) \mid \ce{HCl}(b) \mid \ce{AgCl(s)} \mid \ce{Ag},
$$
with cell reaction $\tfrac12\ce{H2 + AgCl -> Ag + H+ + Cl-}$, $z = 1$, and

$$
E_{\mathrm{cell}} = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln[a(\ce{H+})a(\ce{Cl-})] = E^\circ(\ce{AgCl}/\ce{Ag}) - \frac{2RT}{F}\ln\frac{\gamma_\pm b}{b^\circ}. \tag{13.8}
$$
When $E^\circ$ is known, a measured $E_{\mathrm{cell}}$ gives $\gamma_\pm$. Similarly, the cell reaction of $\ce{Cu} \mid \ce{CuCl2}(b) \mid \text{calomel electrode}$ is $\ce{Cu + Hg2Cl2 -> Cu^2+ + 2Cl- + 2Hg}$, with $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{2F}\ln[4\gamma_\pm^3(b/b^\circ)^3]$, from which $\gamma_\pm$ of $\ce{CuCl2}$ is found.

**Example 13.7.2** In a Harned cell at $25\,^\circ\mathrm{C}$ with $b = 0.0100\,\mathrm{mol\,kg^{-1}}$, the measured cell potential is $E_{\mathrm{cell}} = 0.4640\,\mathrm{V}$. Find $\gamma_\pm$.

**Solution** By Eq. (13.8), $\lg(\gamma_\pm b/b^\circ) = (0.22233 - 0.4640)/(2\times0.05916) = -2.0425$, $\gamma_\pm b/b^\circ = 9.07\times10^{-3}$, and $\gamma_\pm = 0.907$ (tabulated value 0.905). $\square$

### 13.7.4. Determination of Standard Electrode Potentials

$E^\circ$ cannot be measured directly: an ionic solution in the standard state is a hypothetical state. The method is to measure the cell potentials of a series of dilute solutions and extrapolate to infinite dilution. Rewrite Eq. (13.8) as

$$
E' \equiv E_{\mathrm{cell}} + \frac{2RT}{F}\ln\frac{b}{b^\circ} = E^\circ - \frac{2RT}{F}\ln\gamma_\pm.
$$
Everything on the left is measurable, and as $b \to 0$, $\gamma_\pm \to 1$ and $E' \to E^\circ$. But when $E'$ is plotted against $b$, the curve has an infinite slope at $b \to 0$ and cannot be extrapolated accurately. By the Debye–Hückel limiting law ([Theorem 12.7.1 of 6.3.12](/6.3.12#thm-12.7.1)), in dilute solution $\ln\gamma_\pm = -A\ln10\sqrt{b/b^\circ}$, so that

$$
E' = E^\circ + \frac{2RT\ln10}{F}A\sqrt{b/b^\circ} = E^\circ + 0.0602\,\mathrm{V}\times\sqrt{b/b^\circ},
$$
and $E'$ is a straight line in $\sqrt b$ with a slope given by theory, so the extrapolation is highly accurate; this is why the plot against $\sqrt b$ is customary. In practice, a least-squares fit with the extended Debye–Hückel equation plus a linear term is used; Harned and Ehlers (1932–1933) obtained in this way $E^\circ(\ce{AgCl}/\ce{Ag}) = 0.2224\,\mathrm{V}$, which differs by less than $0.1\,\mathrm{mV}$ from the current CRC value of $0.22233\,\mathrm{V}$ (the tables of 13.1.4 and 13.5.2). The standard thermodynamic functions of all ions ultimately depend on extrapolations of this kind.

![Determination of E°(AgCl/Ag) with the Harned cell Pt | H₂ | HCl(b) | AgCl | Ag (25 °C; cell potentials back-calculated from the CRC mean activity coefficients of HCl). Left: the cell potential rises as HCl is diluted; right: E' = E + (2RT/F)ln(b/b°) plotted against √b approaches the Debye–Hückel limiting slope (dashed) in dilute solution, and the least-squares fit of the extended equation extrapolates to 0.2223 V at b → 0](./plots/harned-extrapolation.py)

### 13.7.5. Determination of Transport Numbers

Compare electrolyte concentration cells with and without transference for the same pair of concentrations. The net change of the cell without transference (the fourth row of the table in 13.6.1) is the transfer of $1\,\mathrm{mol}$ of $\ce{HCl}$ from $b_1$ to $b_2$, with $E_{\text{without}} = \frac{2RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$. In the cell with transference, $\ce{Ag} \mid \ce{AgCl} \mid \ce{HCl}(b_1) \vdots \ce{HCl}(b_2) \mid \ce{AgCl} \mid \ce{Ag}$, both electrodes are reversible to $\ce{Cl-}$, and the electrode reactions "transfer" $1\,\mathrm{mol}$ of $\ce{Cl-}$ from left to right, contributing $\frac{RT}{F}\ln\frac{a_-(1)}{a_-(2)}$; adding the liquid junction potential of Eq. (13.6),

$$
E_{\text{with}} = \frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}\left[1 + (t_+ - t_-)\right] = 2t_+\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}, \qquad t_+ = \frac{E_{\text{with}}}{E_{\text{without}}}.
$$
The physical meaning is that when current passes through the liquid junction only the fraction $t_+$ of the charge is carried to the right by $\ce{H+}$, and the net result is the transfer of $t_+$ mol of $\ce{HCl}$ from left to right. This is the third method for measuring transport numbers (for the other two see [6.3.12](/6.3.12)).

### 13.7.6. Determination of pH

**Definition 13.7.2** An electrode whose potential varies with the activity of a particular ion in solution according to the Nernst equation and which is used to determine the activity of that ion is called an **indicator electrode**. In use it forms a cell with a reference electrode.

The definition $\mathrm{pH} = -\lg a(\ce{H+})$ involves the activity of a single ion and cannot be determined rigorously by thermodynamics. What is used in practice is the IUPAC operational definition: a cell is formed from an $\ce{H+}$ indicator electrode and a reference electrode, and the unknown solution X and a standard buffer solution S of known pH are measured in turn,

$$
\mathrm{pH(X)} = \mathrm{pH(S)} - \frac{E_{\mathrm{X}} - E_{\mathrm{S}}}{RT\ln10/F},
$$
where $E$ is the cell potential "indicator electrode − reference electrode". The pH of standard buffer solutions is determined with Harned-type cells without liquid junction, with the activity coefficient of the single $\ce{Cl-}$ ion estimated by convention (the Bates–Guggenheim convention) from the Debye–Hückel equation; at $25\,^\circ\mathrm{C}$, the pH is 4.005 for $0.05\,\mathrm{mol\,kg^{-1}}$ potassium hydrogen phthalate, 6.865 for the equimolal phosphate buffer ($0.025\,\mathrm{mol\,kg^{-1}}$ each) and 9.180 for $0.01\,\mathrm{mol\,kg^{-1}}$ borax.

The hydrogen electrode was the first indicator electrode: $\ce{Pt} \mid \ce{H2}(p^\circ) \mid \text{solution under study} \parallel \text{saturated calomel electrode}$, with $E_{\mathrm{cell}} = 0.2412\,\mathrm{V} + 0.05916\,\mathrm{V}\times\mathrm{pH}$ ($25\,^\circ\mathrm{C}$, liquid junction potential neglected). The hydrogen electrode is accurate but needs pure hydrogen, its platinum is easily poisoned, and it cannot be used in solutions containing oxidizing agents. Today almost only the glass electrode (13.9.3) is used.

## 13.8. Potential–pH Diagrams

### 13.8.1. Three Kinds of Lines

A **potential–pH diagram** (Pourbaix diagram, [Definition 12.3.1 of 6.1.12](/6.1.12#def-12.3.1)) plots on the $E$–pH plane the equilibria among the species of an element in water; each line is the position of an equilibrium at a given temperature and given activities of the other species, and each region is the stability region of one species. M. Pourbaix drew such diagrams for almost all the elements in the 1940s–1960s, and they are a basic tool in corrosion science, hydrometallurgy and geochemistry. The lines fall into three kinds according to the reactions involved:

| Reaction | Line | Example |
|---|---|---|
| Redox reaction without $\ce{H+}$ ($\ce{OH-}$) | Horizontal line, $E$ independent of pH | $\ce{Fe^3+ + e- <=> Fe^2+}$ |
| Non-redox reaction involving $\ce{H+}$ | Vertical line at a fixed pH (independent of $E$) | $\ce{Fe2O3 + 6H+ <=> 2Fe^3+ + 3H2O}$ |
| Redox reaction involving $\ce{H+}$ | Sloping line, slope $-0.05916\,m/z\,\mathrm{V}$ | $\ce{Fe2O3 + 6H+ + 2e- <=> 2Fe^2+ + 3H2O}$ |

For $\text{oxidized form} + m\ce{H+} + z\ce{e-} \to \text{reduced form}$, $E = E^\circ - \frac{0.05916\,\mathrm{V}}{z}\lg\frac{a_{\text{red}}}{a_{\text{ox}}} - \frac{0.05916\,\mathrm{V}\cdot m}{z}\mathrm{pH}$. Except for vertical lines, the region above a line is the stability region of the oxidized form and the region below that of the reduced form; to the left of a vertical line is the dissolved (acidic) form and to the right the precipitated (basic) form. The stability region of water (line a, $E = -0.0592\,\mathrm{pH}$, and line b, $E = 1.229 - 0.0592\,\mathrm{pH}$ at $p = p^\circ$, [6.1.12](/6.1.12)) is the most basic diagram, and these two lines are drawn on all other potential–pH diagrams.

### 13.8.2. The Fe–H₂O System

Take $298.15\,\mathrm{K}$ and an activity of $10^{-6}$ for the iron species in solution (the customary boundary of "insoluble" in corrosion science), and consider Fe, $\ce{Fe^2+}$, $\ce{Fe^3+}$, hematite $\ce{Fe2O3}$ and magnetite $\ce{Fe3O4}$. The data are $E^\circ(\ce{Fe^2+}/\ce{Fe}) = -0.447\,\mathrm{V}$ and $E^\circ(\ce{Fe^3+}/\ce{Fe^2+}) = 0.771\,\mathrm{V}$ (CRC table of standard electrode potentials, as in [6.1.11](/6.1.11)), from which $\Delta_{\mathrm{f}}G^\circ(\ce{Fe^2+}) = -86.3$ and $\Delta_{\mathrm{f}}G^\circ(\ce{Fe^3+}) = -11.9\,\mathrm{kJ\,mol^{-1}}$ are obtained; $\Delta_{\mathrm{f}}G^\circ(\ce{Fe2O3}) = -742.2$, $\Delta_{\mathrm{f}}G^\circ(\ce{Fe3O4}) = -1015.4$ and $\Delta_{\mathrm{f}}G^\circ(\ce{H2O, l}) = -237.1\,\mathrm{kJ\,mol^{-1}}$ (CRC thermodynamic tables).

$$
\begin{aligned}
&\text{c}\quad \ce{Fe2O3 + 6H+ <=> 2Fe^3+ + 3H2O}, && \Delta_{\mathrm{r}}G^\circ = 7.2\,\mathrm{kJ\,mol^{-1}},\ \lg K^\circ = -1.26,\ \mathrm{pH} = \tfrac16(\lg K^\circ - 2\lg a) = 1.79;\\
&\text{d}\quad \ce{Fe^3+ + e- <=> Fe^2+}, && E = 0.771\,\mathrm{V};\\
&\text{e}\quad \ce{Fe^2+ + 2e- <=> Fe}, && E = -0.447 + 0.02958\lg10^{-6} = -0.624\,\mathrm{V};\\
&\text{f}\quad \ce{Fe2O3 + 6H+ + 2e- <=> 2Fe^2+ + 3H2O}, && E^\circ = 0.734\,\mathrm{V},\ E = 1.089 - 0.1775\,\mathrm{pH};\\
&\text{g}\quad \ce{Fe3O4 + 8H+ + 2e- <=> 3Fe^2+ + 4H2O}, && E^\circ = 0.994\,\mathrm{V},\ E = 1.526 - 0.2366\,\mathrm{pH};\\
&\text{h}\quad \ce{3Fe2O3 + 2H+ + 2e- <=> 2Fe3O4 + H2O}, && E = 0.214 - 0.0592\,\mathrm{pH};\\
&\text{i}\quad \ce{Fe3O4 + 8H+ + 8e- <=> 3Fe + 4H2O}, && E = -0.087 - 0.0592\,\mathrm{pH}.
\end{aligned}
$$
Lines d, f and c meet at pH 1.79; f, g and h meet at pH 7.40; e, g and i meet at pH 9.09. Because all the lines are computed from the same set of Gibbs energies, the intersections are automatically consistent (for example, f at pH 1.79 equals exactly 0.771 V).

Some values in textbooks (pH 1.76 for line c, $1.083 - 0.1773\,\mathrm{pH}$ for line f, $-0.618\,\mathrm{V}$ for line e) come from older data such as $E^\circ(\ce{Fe^2+}/\ce{Fe}) = -0.440\,\mathrm{V}$ and disagree with current CRC values; here everything is computed from the current values. In simplified diagrams only $\ce{Fe2O3}$ is considered; with $\ce{Fe3O4}$ added, a narrow band of magnetite appears in the neutral to basic region. It should also be noted that the CRC thermodynamic table gives $\Delta_{\mathrm{f}}G^\circ(\ce{Fe^2+}) = -78.9\,\mathrm{kJ\,mol^{-1}}$, which corresponds to $E^\circ = -0.41\,\mathrm{V}$ and is inconsistent with the $-0.447\,\mathrm{V}$ of the $E^\circ$ table (a well-known discrepancy in the thermodynamic data of iron); we take the $E^\circ$ table as authoritative throughout, which does not change the structure of the diagram, but shifts line e by about 40 mV. Above pH 13, soluble hydroxo complex ions such as $\ce{HFeO2-}$ should also be considered; they are omitted from the figure.

![Potential–pH diagram of the Fe–H₂O system at 298.15 K (activity of iron species in solution 10⁻⁶, calculated from CRC values of E° and ΔfG°): the stability region of Fe is the region of immunity, those of Fe²⁺ and Fe³⁺ are the region of corrosion, and those of Fe₂O₃ and Fe₃O₄ are the region of passivation; the dashed lines a and b are the boundaries of the stability region of water](./plots/fe-pourbaix.py)

### 13.8.3. Applications and Limitations of Potential–pH Diagrams

A potential–pH diagram is an equilibrium diagram of electrochemistry and serves the same purpose as a phase diagram: one diagram gives the relative stabilities of all the species under given conditions, from which the possibility of their interconversion can be judged. The rule is that, of two lines, the oxidized form of the upper line and the reduced form of the lower line cannot coexist stably, and the reaction $(\text{oxidized form})_{\text{upper}} + (\text{reduced form})_{\text{lower}} \to (\text{oxidized form})_{\text{lower}} + (\text{reduced form})_{\text{upper}}$ must occur, because the electrode potential of the upper couple is higher.

For iron, the diagram divides the $E$–pH plane into three kinds of region:

- Immunity region (Fe stable): iron does not corrode. The stability region of Fe lies entirely below line a, which shows that iron is not thermodynamically stable in water at any pH and is oxidized by $\ce{H+}$ or water.
- Corrosion region ($\ce{Fe^2+}$, $\ce{Fe^3+}$ stable): iron dissolves. In acidic solution, Fe is coupled with $\ce{H+}$/$\ce{H2}$ (line a), giving hydrogen-evolution corrosion; in neutral oxygen-containing water, line b is far above the stability region of Fe, and $\ce{O2}$ oxidizes Fe to $\ce{Fe^2+}$ and then to $\ce{Fe2O3}$ (the main component of rust is the hydrated oxide $\ce{FeO(OH)}$, represented in the diagram by $\ce{Fe2O3}$).
- Passivation region ($\ce{Fe2O3}$, $\ce{Fe3O4}$ stable): when a dense oxide film forms on the surface, the metal is protected (**passivation**).

Three ideas of electrochemical protection can be read from this: lower the potential into the immunity region (cathodic protection and sacrificial anode protection), raise the potential into the passivation region (anodic protection), and adjust the pH to bring the system into the passivation region (for example, by adding alkali to boiler water); see [6.3.14](/6.3.14).

The limitations of potential–pH diagrams: they give only thermodynamic possibility, not rates; whether the oxide film in the passivation region actually protects the metal depends on the structure of the film (a $\ce{Fe2O3}$ film is loose and porous and protects poorly, whereas chromium oxide films are dense, which is why stainless steel resists corrosion); the lines depend on the assumed ion activities, the temperature and the species considered, and in the presence of ligands ($\ce{Cl-}$, $\ce{NH3}$) the diagram changes markedly.

## 13.9. Membrane Potentials and Ion-Selective Electrodes

### 13.9.1. Membrane Equilibrium and Membrane Potential

Many membranes are selectively permeable to ions: a cell membrane at rest admits mainly $\ce{K+}$, and certain glass membranes respond only to $\ce{H+}$. Suppose a membrane permeable only to ion B separates two solutions, with B at the higher activity on the left. B then passes to the right, so that the right side becomes positively charged (if B is a cation) and the left side negatively charged, and an electric double layer forms on the two sides of the membrane; the electric field produced prevents further passage of B, and eventually passage stops macroscopically.

**Definition 13.9.1** The state in which, in the solutions on the two sides of a selectively permeable membrane, the electrochemical potentials of the ion that can pass through the membrane are equal on both sides and there is no longer a net passage macroscopically is called **membrane equilibrium**; at membrane equilibrium the inner potential difference of the solutions on the two sides of the membrane, $E_{\mathrm{m}} = \varphi_{\text{right}} - \varphi_{\text{left}}$, is called the **membrane potential**.

By Theorem 13.4.1, at membrane equilibrium $\mu_{\mathrm{B},\text{left}} + z_{\mathrm{B}}F\varphi_{\text{left}} = \mu_{\mathrm{B},\text{right}} + z_{\mathrm{B}}F\varphi_{\text{right}}$, so

$$
E_{\mathrm{m}} = \varphi_{\text{right}} - \varphi_{\text{left}} = \frac{\mu_{\mathrm{B},\text{left}} - \mu_{\mathrm{B},\text{right}}}{z_{\mathrm{B}}F} = \frac{RT}{z_{\mathrm{B}}F}\ln\frac{a_{\mathrm{B},\text{left}}}{a_{\mathrm{B},\text{right}}}. \tag{13.9}
$$
It has the same form as the cell potential of a concentration cell ([6.1.11](/6.1.11)), but there is no electrode reaction, only the selective passage of ions: the membrane itself acts as a "selective electrode". The amount of ions passing through the membrane is minute: establishing a membrane potential of $100\,\mathrm{mV}$ requires the transfer of only about $10^{-6}$ of the ions on the two sides (the specific capacitance of the membrane is about $1\,\mu\mathrm{F\,cm^{-2}}$), so the composition and electroneutrality of the solutions are hardly affected.

### 13.9.2. The Resting Potential of Cells

The ion concentrations inside and outside a cell differ greatly (typical values for a mammalian neuron: $\ce{K+}$ 140 inside and 5 $\mathrm{mmol\,L^{-1}}$ outside; $\ce{Na+}$ 12 inside and 145 $\mathrm{mmol\,L^{-1}}$ outside); this gradient is maintained by the Na⁺/K⁺ pump, which consumes ATP. In biology the membrane potential is defined as the potential of the inside of the cell relative to the outside, $E_{\mathrm{m}} = \varphi_{\text{in}} - \varphi_{\text{out}}$. If the membrane were permeable to $\ce{K+}$ only, then by Eq. (13.9) (left = outside, right = inside), with $RT/F = 26.7\,\mathrm{mV}$ at $37\,^\circ\mathrm{C}$,

$$
E_{\ce{K}} = 26.7\,\mathrm{mV}\times\ln\frac{5}{140} = -89\,\mathrm{mV}, \qquad E_{\ce{Na}} = 26.7\,\mathrm{mV}\times\ln\frac{145}{12} = +67\,\mathrm{mV}.
$$
These values are called the equilibrium potentials (Nernst potentials) of the ions. The measured resting potential is about $-70\,\mathrm{mV}$, close to $E_{\ce{K}}$ and displaced toward $E_{\ce{Na}}$, because the resting membrane is far more permeable to $\ce{K+}$ than to $\ce{Na+}$, but not impermeable to it; when several ions permeate simultaneously, the membrane potential is a steady state rather than an equilibrium state and is described by the Goldman–Hodgkin–Katz equation, see [Neurobiology](/7.16) and [Biophysics](/7.5). During an action potential the $\ce{Na+}$ channels open and the membrane potential quickly approaches $E_{\ce{Na}}$; the proton gradient across the inner mitochondrial membrane (a membrane potential of about $-150$ to $-180\,\mathrm{mV}$ plus a pH difference) drives the synthesis of ATP, and its thermodynamics is just the electrochemical potential of this section. If macromolecular ions (proteins) that cannot pass through the membrane are also present on the two sides, a Donnan equilibrium is established, see [6.3.21](/6.3.21).

### 13.9.3. The Glass Electrode and Ion-Selective Electrodes

**Definition 13.9.2** An indicator electrode whose potential responds to the activity of a single ion in solution according to the Nernst equation and which is used to determine the activity of that ion is called an **ion-selective electrode**; its sensing element is usually a selective membrane. An ion-selective electrode whose sensing membrane is a thin film of special glass that responds selectively to $\ce{H+}$ is called a **glass electrode**.

A glass electrode is a thin-walled glass bulb containing an $\ce{HCl}$ solution (of fixed activity) and an internal $\ce{Ag}/\ce{AgCl}$ reference electrode: $\ce{Ag} \mid \ce{AgCl(s)} \mid \ce{HCl}(\text{inner}) \mid \text{glass membrane} \mid \text{solution under study}$. The glass surface absorbs water to form a hydrated gel layer in which $\ce{Na+}$ is exchanged with $\ce{H+}$ from the solution; the $\ce{H+}$ exchange equilibria at the two surfaces of the membrane make it equivalent to a membrane responding only to $\ce{H+}$. The potential of the electrode is the potential of the internal reference electrode plus the membrane potential:

$$
E_{\mathrm{g}} = E(\ce{AgCl}/\ce{Ag}) - \frac{RT}{F}\ln a(\ce{Cl-}, \text{inner}) + \frac{RT}{F}\ln\frac{a(\ce{H+}, \text{outer})}{a(\ce{H+}, \text{inner})} = E^\circ_{\mathrm{g}} - \frac{RT\ln10}{F}\mathrm{pH},
$$
where $E^\circ_{\mathrm{g}}$ includes the internal reference electrode, the internal solution, the asymmetry potential of the glass membrane and so on; for a given electrode it is a function of temperature only, but it differs from electrode to electrode and drifts with time. Therefore, after the glass electrode is combined with a reference electrode to form a cell ($E_{\mathrm{cell}} = E_{\text{ref}} - E_{\mathrm{g}} = E_{\text{ref}} - E^\circ_{\mathrm{g}} + 0.05916\,\mathrm{V}\times\mathrm{pH}$ at $25\,^\circ\mathrm{C}$), it must be calibrated with two standard buffer solutions, and the pH is then read according to the operational definition of 13.7.6. This is the pH meter. The resistance of the glass membrane is very high (of the order of $10^8\,\Omega$), so a pH meter must have a very high input impedance. The glass electrode is not disturbed by oxidizing agents, reducing agents or colloids, but above pH 12 it also responds to $\ce{Na+}$ (the alkaline error), and in strong acids it also deviates (the acid error).

Changing the material of the sensing membrane gives other ion-selective electrodes: $\ce{LaF3}$ single-crystal membrane ($\ce{F-}$), $\ce{Ag2S}$ membrane ($\ce{Ag+}$, $\ce{S^2-}$), and PVC membranes containing valinomycin ($\ce{K+}$; valinomycin is a natural ionophore that binds $\ce{K+}$ selectively). Potentiometric analysis with ion-selective electrodes and the clinical determination of electrolytes in blood are treated in [Analytical Chemistry](/6.4).

## Summary

| Topic | Key points |
|---|---|
| Reversible cells | Material reversibility + energy reversibility ($I \to 0$); $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$; three kinds of reversible electrodes |
| Measurement | $U = E_{\mathrm{cell}}R_{\mathrm{o}}/(R_{\mathrm{o}} + R_{\mathrm{i}})$; compensation method (zero current); the Weston standard cell has been replaced by the Josephson voltage standard |
| Nernst equation | $E_{\mathrm{cell}} = E^\circ_{\mathrm{cell}} - \frac{RT}{zF}\ln\prod a_{\mathrm{B}}^{\nu_{\mathrm{B}}}$; $E$ is independent of the way the equation is written, whereas $\Delta_{\mathrm{r}}G$, $K^\circ$ and $z$ depend on it; $\ln K^\circ = zFE^\circ_{\mathrm{cell}}/RT$ |
| Temperature coefficient | $\Delta_{\mathrm{r}}S_{\mathrm{m}} = zF(\partial E/\partial T)_p$, $\Delta_{\mathrm{r}}H_{\mathrm{m}} = -zFE + zFT(\partial E/\partial T)_p$, $Q_{\mathrm{r}} = T\Delta_{\mathrm{r}}S_{\mathrm{m}} \ne \Delta_{\mathrm{r}}H_{\mathrm{m}}$; on discharge at terminal voltage $U$, $Q = \Delta_{\mathrm{r}}H_{\mathrm{m}} + zFU$ |
| Electrochemical potential | $\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}} + z_{\mathrm{B}}F\varphi$; equilibrium $\tilde\mu^\alpha = \tilde\mu^\beta$; cell potential = sum of the Galvani potential differences at the interfaces = difference of the electrochemical potentials of electrons at the two terminals divided by $-F$ |
| Liquid junction potential | $E_{\mathrm{l}} = (t_+ - t_-)\frac{RT}{F}\ln\frac{a_\pm(1)}{a_\pm(2)}$ (1-1 type); $\ce{KCl}$ salt bridge |
| Electrode potential | Cell potential of the cell with SHE as the left electrode; $E = E^\circ + \frac{RT}{zF}\ln\frac{a_{\text{ox}}}{a_{\text{red}}}$; $E_{\mathrm{cell}} = E_{\text{right}} - E_{\text{left}}$; reference electrodes SCE 0.2412 V, Ag/AgCl (saturated KCl) 0.197 V |
| Potentiometric method | $K_{\mathrm{w}}$, $K_{\mathrm{sp}}$; $\Delta_{\mathrm{r}}S$, $\Delta_{\mathrm{r}}H$; $\gamma_\pm$ (Harned cell); extrapolation of $E^\circ$ against $\sqrt b$; $t_+ = E_{\text{with}}/E_{\text{without}}$; operational definition of pH |
| Potential–pH diagrams | Horizontal, vertical and sloping lines; Fe: $\ce{Fe2O3}/\ce{Fe^3+}$ at pH 1.79, $\ce{Fe^2+}/\ce{Fe}$ at $-0.624\,\mathrm{V}$ ($a = 10^{-6}$); immunity, corrosion and passivation regions |
| Membrane potential | $E_{\mathrm{m}} = \frac{RT}{z_{\mathrm{B}}F}\ln\frac{a_{\text{left}}}{a_{\text{right}}}$; $E_{\ce{K}} \approx -89\,\mathrm{mV}$; glass electrode $E_{\mathrm{g}} = E^\circ_{\mathrm{g}} - 0.05916\,\mathrm{V}\times\mathrm{pH}$ |

## Questions

1. Can the electromotive force of a reversible cell be measured with an ordinary voltmeter?

   **Answer** No. A voltmeter draws a finite current and measures the terminal voltage; the compensation method or an electrometer of high input impedance must be used.

2. Does the cell potential depend on the stoichiometric coefficients of the cell reaction? Does $z$ affect $E$?

   **Answer** No; $z$ changes in proportion to $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ and their ratio $E$ is unchanged. But if the same overall reaction proceeds through different electrode reactions, $z$ differs and so does $E$, 13.3.2.

3. What cell should be designed to measure the solubility product of $\ce{AgCl}$?

   **Answer** $\ce{Ag} \mid \ce{AgNO3}(\mathrm{aq}) \parallel \ce{HCl}(\mathrm{aq}) \mid \ce{AgCl(s)} \mid \ce{Ag}$; the cell reaction $\ce{Ag+ + Cl- -> AgCl}$ is the reverse of the dissolution equilibrium, Example 13.7.1.

4. By what methods can the standard equilibrium constant of a cell reaction be found?

   **Answer** Thermodynamics: from $\Delta_{\mathrm{f}}G^\circ$ or from $\Delta_{\mathrm{r}}H^\circ$ and $\Delta_{\mathrm{r}}S^\circ$; electrochemistry: from $E^\circ_{\mathrm{cell}}$; statistical mechanics: from partition functions, [6.3.11](/6.3.11); kinetics: from the ratio of the forward and reverse rate constants, [6.3.15](/6.3.15).

5. Why is $E'$ extrapolated against $\sqrt b$ rather than $b$?

   **Answer** By the Debye–Hückel limiting law, $\ln\gamma_\pm \propto \sqrt b$ in dilute solution, so $E'$ is a straight line in $\sqrt b$ with a known slope.

6. Can an endothermic cell reaction proceed spontaneously and do work?

   **Answer** Yes, provided $\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0$; part of the energy for the work comes from heat of the surroundings, Example 13.3.2.
