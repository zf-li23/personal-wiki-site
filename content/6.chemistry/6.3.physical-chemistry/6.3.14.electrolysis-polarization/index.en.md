---
title: Electrolysis and Polarization
description: Decomposition voltage and the electrochemical window; electrode polarization and the signed overpotential, exchange current density, concentration, activation and ohmic polarization, and the three-electrode cell; the Butler–Volmer equation from the transition-state picture, the Tafel equation and charge-transfer resistance, and the hydrogen evolution reaction; the diffusion layer and the limiting current, the Cottrell equation from the diffusion equation, polarography and the Ilkovič equation; deposition and separation of metals, and electrosynthesis; electrochemical corrosion, the corrosion potential and protection; performance parameters of electrochemical power sources, intercalation reactions, lithium-ion batteries and fuel cells.
source_hash: d864c8ede0a0
---

[6.3.13](/6.3.13) studied the equilibrium of electrodes when the current tends to zero: the potential of each electrode is determined by the Nernst equation, and the cell potential by $\Delta_{\mathrm{r}}G_{\mathrm{m}}$. Real electrolysis and battery discharge involve a finite current, so electrode reactions must proceed at a finite rate and the electrode potentials depart from their equilibrium values; this phenomenon is called polarization. Electrolysis requires a higher voltage than the thermodynamic value, and a discharging battery delivers a lower voltage than its electromotive force; in both cases the difference is caused by polarization. This chapter is about electrochemical kinetics. We first discuss the minimum voltage required for electrolysis (14.1) and the kinds of polarization (14.2); we then derive the relation between current and overpotential from the transition-state picture, namely the Butler–Volmer and Tafel equations (14.3), and the limiting current set by mass transport together with the Cottrell equation (14.4); finally we discuss applications to electrolysis (14.5), corrosion (14.6) and electrochemical power sources (14.7).

[6.1.12](/6.1.12) gave qualitative descriptions of the decomposition voltage, overpotential, Faraday's laws of electrolysis and common electrochemical power sources; here we give the quantitative theory. The kinetic part uses the **transition state**, **activation energy** and **Arrhenius equation** of [6.1.7](/6.1.7); the mass-transport part uses the solution of the heat equation on a half-line in [2.5.7](/2.5.7) and the [error function](/2.5.6). General rate theories are developed in [6.3.15](/6.3.15)–[6.3.16](/6.3.16); the electrode reaction is among the easiest cases in which the activation energy can be "tuned" by an applied potential: changing the electrode potential by $0.1\,\mathrm{V}$ changes the reaction rate by almost an order of magnitude.

## 14.1. Decomposition Voltage and the Electrochemical Window

### 14.1.1. Decomposition Voltage

Consider the electrolysis of a $0.5\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ solution with platinum electrodes: the cathode reaction is $\ce{2H+ + 2e- -> H2}$, the anode reaction is $\ce{H2O -> 2H+ + 1/2O2 + 2e-}$, and the overall reaction is $\ce{H2O -> H2 + 1/2O2}$. The applied voltage $U$ is increased gradually while the current $I$ is measured: at first the current is very small and hardly increases with voltage; beyond a certain voltage, bubbles form continuously at the electrodes and the current rises linearly with voltage. Extrapolating the linear part to $I = 0$ gives the **decomposition voltage** ([Definition 12.4.2 of 6.1.12](/6.1.12#def-12.4.2)) $U_{\mathrm{d}}$.

**Definition 14.1.1 (Decomposition Voltage)** The minimum applied voltage required to sustain electrolysis is called the **decomposition voltage**; the electromotive force of the reversible cell formed by the electrolysis products is called the theoretical decomposition voltage.

A small current also flows below the decomposition voltage: the small amounts of $\ce{H2}$ and $\ce{O2}$ formed at the electrodes dissolve in the solution and form a galvanic cell whose electromotive force opposes the applied voltage (a back emf), and the products diffuse continually into the bulk and must be replenished, which gives a very small "residual current". When the applied voltage is raised until the partial pressures of the products reach the external pressure and the gases can escape as bubbles, the back emf no longer increases and the current rises sharply with voltage.

| Electrolyte ($c = 1/z\,\mathrm{mol\,L^{-1}}$, $25\,^\circ\mathrm{C}$, Pt electrodes) | Products | Theoretical decomposition voltage/V | Measured decomposition voltage/V |
|---|---|---|---|
| $\ce{H2SO4}$ | $\ce{H2} + \ce{O2}$ | 1.23 | 1.67 |
| $\ce{HNO3}$ | $\ce{H2} + \ce{O2}$ | 1.23 | 1.69 |
| $\ce{NaOH}$ | $\ce{H2} + \ce{O2}$ | 1.23 | 1.69 |

The electrolysis of these three solutions is essentially the electrolysis of water, with a theoretical decomposition voltage of $1.229\,\mathrm{V}$ independent of the electrolyte; the measured values are all about $1.7\,\mathrm{V}$, and the excess of about $0.45\,\mathrm{V}$ is mainly the overpotential of $\ce{O2}$ and $\ce{H2}$ on platinum, together with the voltage drop across the resistance of the solution. The decomposition voltage is an empirical quantity obtained by extrapolation, not a strict thermodynamic one; it depends on the electrode material, the state of the electrode surface and the mode of measurement.

### 14.1.2. Electrical Work When Current Flows

In reversible operation the electrical work done on the system by the surroundings is $W'_{\mathrm{r}} = -zFE_{\mathrm{cell}}$ ([6.3.13](/6.3.13)); in irreversible operation at terminal voltage $U$, $W'_{\mathrm{ir}} = -zFU$. From $\Delta_{\mathrm{r}}G \le W'$:

- Galvanic cell discharge: $-W'$ is the work done by the cell on the surroundings, $U < E_{\mathrm{cell}}$, and the electrical work obtained is smaller than $-\Delta_{\mathrm{r}}G_{\mathrm{m}}$;
- Electrolysis: $W' > 0$ is work done by the surroundings on the system, $U > \lvert E_{\mathrm{cell}}\rvert$, and the electrical work consumed is greater than $\Delta_{\mathrm{r}}G_{\mathrm{m}}$.

In both cases $W'_{\mathrm{ir}} > W'_{\mathrm{r}}$: irreversibility always costs additional electrical work (or yields less), and the difference is dissipated as heat, corresponding to entropy production. The larger the current, the larger the deviation, so electrochemical devices always involve a compromise between power (current) and efficiency.

### 14.1.3. The Electrochemical Window

**Definition 14.1.2** The range of electrode potentials within which an electrolyte (solvent plus salt) is neither oxidized nor reduced at an electrode is called the **electrochemical window** of the electrolyte. Beyond the upper limit of the window the electrolyte is oxidized at the positive electrode; below the lower limit it is reduced at the negative electrode.

The thermodynamic window of water is the $1.23\,\mathrm{V}$ between lines a and b of the potential–pH diagram of [6.1.12](/6.1.12); because of the overpotentials for $\ce{H2}$ and $\ce{O2}$ evolution, the window actually usable is about $2\,\mathrm{V}$. This limits the voltage of aqueous batteries (the lead–acid cell, at about $2.0\,\mathrm{V}$, is near the limit). For a lithium-ion battery to reach $3.6$–$4\,\mathrm{V}$, organic carbonate electrolytes with a wider electrochemical window must be used.

Goodenough explained the meaning of the window in terms of electron energy levels: the window of an electrolyte is determined by the energy difference between its lowest unoccupied orbital (**LUMO**) and its highest occupied orbital (**HOMO**) ([6.1.3](/6.1.3)). If the electrochemical potential of electrons in the negative electrode (the Fermi level) is higher than the LUMO of the electrolyte, electrons are transferred to the electrolyte and reduce it; if the electrochemical potential of the positive electrode is lower than the HOMO of the electrolyte, electrons are taken from the electrolyte and oxidize it. A thermodynamically stable battery requires the electrochemical potentials of both electrodes to lie within the window, so the battery voltage cannot exceed the width of the window. The graphite negative electrode of a lithium-ion battery (about $0.1\,\mathrm{V}$ vs $\ce{Li+}/\ce{Li}$) actually lies below the reduction limit of carbonate electrolytes; it operates stably because on first charging the electrolyte is reduced and forms on the surface of the negative electrode a solid–electrolyte interphase (SEI) film that conducts $\ce{Li+}$ but not electrons and kinetically prevents further reduction, which is a form of passivation. (In the battery field, the negative electrode is called the anode and the positive electrode the cathode according to the reactions on discharge, the opposite of the usage for electrolytic cells; keep this in mind when reading the literature.)

## 14.2. Polarization and Overpotential

### 14.2.1. Polarization and Overpotential

**Definition 14.2.1** The departure of the electrode potential from its equilibrium value when a net current passes through an electrode is called **electrode polarization**.

**Definition 14.2.2 (Overpotential)** The difference between the potential $E$ of an electrode when current flows and the equilibrium potential $E_{\mathrm{eq}}$ of the same electrode at zero current (given by the Nernst equation),

$$
\eta = E - E_{\mathrm{eq}},
$$
is called the overpotential of the electrode.

By this signed IUPAC definition, $\eta > 0$ at an anode (oxidation) and $\eta < 0$ at a cathode (reduction): for oxidation to proceed at a finite rate the electrode potential must be above the equilibrium value, and for reduction to proceed it must be below it. This holds in electrolytic cells and galvanic cells alike: polarization always raises the potential of the anode and lowers that of the cathode. [6.1.12](/6.1.12) uses the same definition; many textbooks take the absolute value of the overpotential, $\eta = \lvert E - E_{\mathrm{eq}}\rvert$, which differs only by a sign, but the kinetic equations are simpler with the signed definition.

The overpotential is the driving force of the electrode reaction, just as $-\Delta_{\mathrm{r}}G$ is the driving force of a chemical reaction: $F\eta$ is the additional Gibbs energy supplied to force $1\,\mathrm{mol}$ of electrons to transfer at the electrode. Take a $\ce{Cu} \mid \ce{CuSO4}$ electrode as an example: at equilibrium, copper dissolves and deposits at equal rates and the net current is zero; if the electrode potential is lowered artificially, deposition is faster than dissolution, the net current is a cathodic current, $\ce{Cu^2+ + 2e- -> Cu}$ proceeds on balance, and the reaction rate is proportional to the current (Faraday's law); raising the electrode potential has the opposite effect.

### 14.2.2. Exchange Current Density

**Definition 14.2.3** At equilibrium the current densities of the forward (anodic) and reverse (cathodic) reactions of an electrode are equal in magnitude and opposite in direction, and the net current is zero; the magnitude $j_0$ of the current density in either direction at this point is called the **exchange current density** of the electrode reaction.

An equilibrium electrode is in dynamic equilibrium, and $j_0$ measures how fast this dynamic exchange is. An electrode with a large $j_0$ (such as $\ce{H+}/\ce{H2}$ on Pt, about $10\,\mathrm{A\,m^{-2}}$) needs only a small overpotential to pass a given current, is not easily polarized, and its potential is not easily changed by small outside disturbances; an electrode with a small $j_0$ (such as $\ce{H+}/\ce{H2}$ on Hg, about $10^{-8}\,\mathrm{A\,m^{-2}}$) is severely polarized by even a small current. Therefore a stable reversible electrode (reference electrode, indicator electrode) requires that $j_0$ be large enough and that the concentration of the ions taking part in the electrode reaction not be too small (generally above $10^{-6}\,\mathrm{mol\,L^{-1}}$); otherwise $j_0$ is too small and reactions of impurities determine the potential. The $j_0$ of different reactions and different electrode materials can differ by more than ten orders of magnitude, which is exactly the subject of electrocatalysis.

### 14.2.3. Steps of an Electrode Process

An electrode reaction is a heterogeneous reaction occurring at the electrode–solution interface and always comprises several steps in series:

1. Mass transport in solution: the reactant migrates, diffuses and is convected from the bulk of the solution to the neighborhood of the electrode surface;
2. Preceding surface conversion: the reactant is adsorbed on the electrode surface, or undergoes a chemical reaction in the layer of solution near the surface (such as the dissociation of a complex ion);
3. Electron transfer: the reactant gains or loses electrons at the electrode surface;
4. Subsequent surface conversion: the product desorbs, crystallizes (a metal deposit enters the lattice), or undergoes a chemical reaction near the surface and forms bubbles;
5. Mass transport in solution: a soluble product is transported from the electrode surface to the bulk of the solution (in intercalation reactions, the product diffuses into the interior of the solid electrode).

For example, $\ce{Fe^3+ + e- -> Fe^2+}$ is an electron transfer with mass transport in solution at both ends; $\ce{Cu^2+ + 2e- -> Cu}$ has mass transport only at the front end; $\ce{H+ + e- -> H_{ad}}$ includes adsorption; and for $\ce{MnO2 + xLi+ + xe- -> Li_xMnO2}$ the product diffuses into the solid. The overall rate is determined by the slowest step (the rate-determining step), which gives rise to different kinds of polarization.

### 14.2.4. Kinds of Polarization

**Definition 14.2.4** According to the rate-determining step, electrode polarization is divided into:

1. **Concentration polarization**: mass transport is slow, so the concentration of reactant (product) near the electrode surface differs from that in the bulk, and the electrode potential departs from the equilibrium value according to the Nernst equation;
2. **Activation polarization** (electrochemical polarization): the electron-transfer step is slow, and additional driving force is needed to overcome the activation barrier;
3. **Ohmic polarization** (resistance polarization): a voltage drop $IR$ appears when current passes through parts that have ohmic resistance, such as the electrolyte solution, films on the electrode surface and the leads.

The direction of concentration polarization can be seen directly from the Nernst equation. When a copper electrode is the anode, the $\ce{Cu^2+}$ produced by $\ce{Cu -> Cu^2+ + 2e-}$ has no time to diffuse away, the surface concentration is higher than that in the bulk, and $E = E^\circ + \frac{RT}{2F}\ln a_{\mathrm{s}}(\ce{Cu^2+})$ is higher than the equilibrium potential; when it is the cathode, the surface $\ce{Cu^2+}$ is consumed, its concentration is lower than in the bulk, and the potential is lower than the equilibrium value. Stirring and raising the temperature and the concentration reduce concentration polarization; raising the conductivity of the electrolyte and shortening the electrode separation reduce ohmic polarization; activation polarization is reduced by electrocatalysts (which raise $j_0$). In real electrode processes several kinds of polarization often coexist, and the total overpotential is their sum.

### 14.2.5. Measurement of Polarization

**Definition 14.2.5** A measuring cell composed of a **working electrode** (the object of study), a **counter electrode** (also called the auxiliary electrode, forming the current circuit with the working electrode) and a reference electrode is called a **three-electrode cell**. Current flows between the working electrode and the counter electrode, and the potential of the working electrode is measured against a reference electrode through which almost no current passes.

No current flows in the reference electrode, so it is not polarized and its potential is constant; polarization at the counter electrode does not affect the measurement. The reference electrode is often connected through a Luggin capillary that brings the point of measurement close to the surface of the working electrode, to reduce the ohmic voltage drop in the solution between them. A modern potentiostat uses negative feedback to control the potential of the working electrode relative to the reference electrode and measures the current at the same time; it is the basic instrument of electrochemical research.

**Definition 14.2.6** The curve relating the electrode potential (or overpotential) to the current density through the electrode is called the **polarization curve** of the electrode.

### 14.2.6. Polarization in Electrolytic Cells and Galvanic Cells

In both electrolytic and galvanic cells, polarization raises the anode potential and lowers the cathode potential, but its effects on the two kinds of device are opposite.

- In an electrolytic cell the anode is the positive electrode. The cell voltage is $U = E_{\text{an}} - E_{\text{cat}} + IR = (E_{\text{an,eq}} - E_{\text{cat,eq}}) + \eta_{\text{an}} - \eta_{\text{cat}} + IR$. With $\eta_{\text{an}} > 0$ and $\eta_{\text{cat}} < 0$, polarization of both electrodes increases the required voltage, and the larger the current, the higher the cell voltage.
- In a galvanic cell the cathode is the positive electrode. The terminal voltage is $U = E_{\text{cat}} - E_{\text{an}} - IR = E_{\mathrm{cell}} + \eta_{\text{cat}} - \eta_{\text{an}} - IR$; polarization of both electrodes reduces the terminal voltage, and the larger the discharge current, the lower the terminal voltage.

On an $E$–$j$ diagram, the anodic polarization curve of an electrolytic cell lies to the right of (at higher potential than) the cathodic polarization curve, and the potential difference between them increases with current; in a galvanic cell the opposite is true: the curve of the positive electrode (cathode) lies on the right, and the two approach each other as the current increases. The main factors affecting the overpotential are: current density (the larger it is, the larger the overpotential); electrode material and surface condition ($j_0$ can differ by many orders of magnitude); the substance deposited (the overpotential for gas evolution is generally much larger than for metal deposition); temperature (raising it increases $j_0$ and decreases the overpotential); and the composition and concentration of the electrolyte (which affect mass transport and the structure of the double layer).

## 14.3. Kinetics of Electrode Reactions

### 14.3.1. Effect of Electrode Potential on the Activation Energy

Consider the one-electron electrode reaction $\ce{O + e- <=> R}$, and suppose for the moment that mass transport is fast enough for the surface concentrations to equal the bulk concentrations $c^*_{\mathrm{O}}$, $c^*_{\mathrm{R}}$. In the picture of **transition state theory** ([6.1.7](/6.1.7), in detail [6.3.16](/6.3.16)), along the reaction coordinate from $\mathrm{O} + \mathrm{e}^-$ (the electron being in the electrode) through the transition state to R, the forward and reverse reactions each have an activation Gibbs energy. When the electrode potential changes by $\Delta E$, the electrochemical potential of electrons in the electrode changes by $-F\Delta E$ ([6.3.13](/6.3.13)), so the Gibbs energy of the initial state $\mathrm{O} + \mathrm{e}^-$ relative to R changes by $-F\Delta E$. The transition state lies between the two, and its Gibbs energy changes by only a fraction of this.

**Definition 14.3.1** The fraction of the total change $F\Delta E$ in the reaction Gibbs energy that appears as a change in the activation Gibbs energy of the electrode reaction when the electrode potential changes is called the **transfer coefficient**: $\alpha_{\mathrm{a}}$ for the anodic direction and $\alpha_{\mathrm{c}}$ for the cathodic direction,

$$
\Delta^\ddagger G_{\mathrm{c}} = \Delta^\ddagger G_{\mathrm{c},0} + \alpha_{\mathrm{c}}F(E - E^{\circ\prime}), \qquad \Delta^\ddagger G_{\mathrm{a}} = \Delta^\ddagger G_{\mathrm{a},0} - \alpha_{\mathrm{a}}F(E - E^{\circ\prime}),
$$
where $E^{\circ\prime}$ is the formal potential of the couple (the "standard" potential when concentrations replace activities). For a one-electron elementary step $\alpha_{\mathrm{a}} + \alpha_{\mathrm{c}} = 1$, and usually $\alpha_{\mathrm{a}} \approx \alpha_{\mathrm{c}} \approx 0.5$.

The transfer coefficient is a measure of the position of the **transition state**, and is analogous to the Brønsted–Evans–Polanyi relation ([6.3.16](/6.3.16)): the more the transition state resembles the product, the closer $\alpha_{\mathrm{c}}$ is to 1. Raising the potential lowers the barrier of the anodic reaction by $\alpha_{\mathrm{a}}F\Delta E$ and raises that of the cathodic reaction by $\alpha_{\mathrm{c}}F\Delta E$. At $25\,^\circ\mathrm{C}$, $F/RT = 38.9\,\mathrm{V^{-1}}$, and $\alpha = 0.5$ with $\Delta E = 0.1\,\mathrm{V}$ changes the barrier by $4.8\,\mathrm{kJ\,mol^{-1}}$ and the rate by a factor of 7.

### 14.3.2. The Butler–Volmer Equation

Let $f = F/RT$. From the Arrhenius form (or transition-state theory), the rate constants of the cathodic and anodic reactions are

$$
k_{\mathrm{c}} = k^\circ\exp[-\alpha_{\mathrm{c}}f(E - E^{\circ\prime})], \qquad k_{\mathrm{a}} = k^\circ\exp[\alpha_{\mathrm{a}}f(E - E^{\circ\prime})],
$$
where $k^\circ$ (unit $\mathrm{m\,s^{-1}}$) is the common value of the two at $E = E^{\circ\prime}$ and is called the standard rate constant. The rate of an electrode reaction is the rate per unit area ($\mathrm{mol\,m^{-2}\,s^{-1}}$) and equals the rate constant times the concentration of reactant at the electrode surface; multiplied by $F$ it is the current density. Taking the anodic current as positive,

$$
j = j_{\mathrm{a}} + j_{\mathrm{c}} = Fk_{\mathrm{a}}c_{\mathrm{R}}(0) - Fk_{\mathrm{c}}c_{\mathrm{O}}(0). \tag{14.1}
$$

**Corollary 14.3.1** When the net current is zero and the surface concentrations equal the bulk concentrations, the electrode potential satisfies the Nernst equation $E_{\mathrm{eq}} = E^{\circ\prime} + \frac{RT}{F}\ln\frac{c^*_{\mathrm{O}}}{c^*_{\mathrm{R}}}$, and the exchange current density is

$$
j_0 = Fk^\circ(c^*_{\mathrm{O}})^{\alpha_{\mathrm{a}}}(c^*_{\mathrm{R}})^{\alpha_{\mathrm{c}}}.
$$

**Proof** $j = 0$ gives $k_{\mathrm{a}}c^*_{\mathrm{R}} = k_{\mathrm{c}}c^*_{\mathrm{O}}$, that is, $\exp[(\alpha_{\mathrm{a}} + \alpha_{\mathrm{c}})f(E_{\mathrm{eq}} - E^{\circ\prime})] = c^*_{\mathrm{O}}/c^*_{\mathrm{R}}$, and $\alpha_{\mathrm{a}} + \alpha_{\mathrm{c}} = 1$ gives the Nernst equation. Substituting back, $j_0 = Fk_{\mathrm{c}}c^*_{\mathrm{O}} = Fk^\circ c^*_{\mathrm{O}}(c^*_{\mathrm{O}}/c^*_{\mathrm{R}})^{-\alpha_{\mathrm{c}}} = Fk^\circ(c^*_{\mathrm{O}})^{1-\alpha_{\mathrm{c}}}(c^*_{\mathrm{R}})^{\alpha_{\mathrm{c}}}$. $\square$

At zero current the kinetics returns to thermodynamics: the equilibrium potential is independent of the rate constants, which is a manifestation of the **principle of microscopic reversibility** ([6.3.15](/6.3.15)). The exchange current density depends on concentration, so $j_0$ must be quoted with the solution composition; it is $k^\circ$ that is the kinetic parameter of the electrode reaction itself.

**Theorem 14.3.1 (Butler–Volmer Equation)** In terms of the overpotential $\eta = E - E_{\mathrm{eq}}$,

$$
j = j_0\left[\frac{c_{\mathrm{R}}(0)}{c^*_{\mathrm{R}}}\exp(\alpha_{\mathrm{a}}f\eta) - \frac{c_{\mathrm{O}}(0)}{c^*_{\mathrm{O}}}\exp(-\alpha_{\mathrm{c}}f\eta)\right]. \tag{14.2}
$$
When mass transport is fast enough (the surface concentrations equal the bulk concentrations),

$$
j = j_0\left[\exp\left(\frac{\alpha_{\mathrm{a}}F\eta}{RT}\right) - \exp\left(-\frac{\alpha_{\mathrm{c}}F\eta}{RT}\right)\right]. \tag{14.3}
$$

**Proof** Substitute $E - E^{\circ\prime} = \eta + (E_{\mathrm{eq}} - E^{\circ\prime})$ into $k_{\mathrm{a}}$: $Fk_{\mathrm{a}}c^*_{\mathrm{R}} = Fk^\circ c^*_{\mathrm{R}}(c^*_{\mathrm{O}}/c^*_{\mathrm{R}})^{\alpha_{\mathrm{a}}}\exp(\alpha_{\mathrm{a}}f\eta) = j_0\exp(\alpha_{\mathrm{a}}f\eta)$; similarly $Fk_{\mathrm{c}}c^*_{\mathrm{O}} = j_0\exp(-\alpha_{\mathrm{c}}f\eta)$. Substituting into Eq. (14.1) and writing $c(0)$ as $c^*\cdot c(0)/c^*$ gives Eq. (14.2). $\square$

This equation was established by Butler (1924) and by Erdey-Grúz and Volmer (1930). The two terms of Eq. (14.3) are the anodic and cathodic partial currents, and the net current is their difference. If a multi-electron electrode reaction is controlled by a one-electron step, Eq. (14.3) keeps its form, but $\alpha_{\mathrm{a}}$ and $\alpha_{\mathrm{c}}$ become apparent transfer coefficients whose sum is not necessarily 1.

![Butler–Volmer kinetics at 25 °C (O + e⁻ = R, anodic current positive). Left: net current and anodic and cathodic partial currents, the asymmetric case α_a = 0.3, and the current approaching a limiting value when mass transport is limited (|j_L| = 20 j₀); right: Tafel plot, in which beyond |η| ≈ 0.12 V both branches become straight lines with a slope of 0.118 V per decade of current, and near η = 0 there is a linear region in which current is proportional to overpotential](./plots/butler-volmer.py)

### 14.3.3. High Overpotential: The Tafel Equation

**Corollary 14.3.2 (Tafel Equation)** When $\eta \gg RT/F$ (anodic polarization), the second term of Eq. (14.3) may be neglected, and

$$
\eta = -\frac{RT}{\alpha_{\mathrm{a}}F}\ln j_0 + \frac{RT}{\alpha_{\mathrm{a}}F}\ln j, \qquad \text{that is,} \quad \eta = a + b\lg j, \quad b = \frac{2.303RT}{\alpha_{\mathrm{a}}F};
$$
for cathodic polarization ($-\eta \gg RT/F$) one likewise has $\lvert\eta\rvert = a + b\lg\lvert j\rvert$, with $b = 2.303RT/(\alpha_{\mathrm{c}}F)$.

Tafel (1905) found this relation experimentally in studying hydrogen evolution, twenty years before the Butler–Volmer theory. For $\alpha = 0.5$ at $25\,^\circ\mathrm{C}$, $b = 0.118\,\mathrm{V}$: each tenfold increase of current increases the overpotential by about $0.12\,\mathrm{V}$. For $\alpha_{\mathrm{a}} + \alpha_{\mathrm{c}} = 1$ the ratio of the reverse current to the forward current is $\exp(-f\lvert\eta\rvert)$, which is below 1% for $\lvert\eta\rvert > 0.12\,\mathrm{V}$, so the Tafel approximation holds. Extrapolating the Tafel line to $\eta = 0$, the intercept gives $\lg j_0$ and the slope gives $\alpha$; this is the standard method for determining electrode kinetic parameters. At still larger currents, mass transport cannot keep up, and the polarization curve departs from the straight line toward the limiting current (14.4).

### 14.3.4. Low Overpotential: Charge-Transfer Resistance

When $\lvert\eta\rvert \ll RT/F$ (within about $10\,\mathrm{mV}$), expanding the exponentials to first order gives $j = j_0F\eta/RT$, so the current is proportional to the overpotential.

**Definition 14.3.2** The ratio of the overpotential to the current density at small overpotential,

$$
R_{\mathrm{ct}} = \frac{\eta}{j} = \frac{RT}{Fj_0},
$$
is called the **charge-transfer resistance** of the electrode reaction (unit $\Omega\,\mathrm{m^2}$).

It has the form of Ohm's law but is not a true resistance: it reflects the kinetics of electron transfer, holds only in the linear region, and is inversely proportional to $j_0$. For $j_0 = 1\,\mathrm{A\,m^{-2}}$, $R_{\mathrm{ct}} = 0.0257\,\Omega\,\mathrm{m^2}$. $R_{\mathrm{ct}}$ can be measured by linear polarization or by AC impedance spectroscopy, the latter separating it from the double-layer capacitance, the solution resistance and the diffusion impedance, and it is a common tool for corrosion monitoring and battery diagnostics.

**Definition 14.3.3** An electrode whose exchange current density tends to zero, so that no charge crosses the interface over a fairly wide range of potentials and the applied potential serves only to change the charge of the double layer, is called an **ideally polarizable electrode**.

A mercury electrode in $\ce{KCl}$ solution approximates an ideally polarizable electrode over a range of about $2\,\mathrm{V}$ and behaves like a capacitor, which is why it is used in studying the structure of the double layer and in polarography. The opposite extreme is the ideal nonpolarizable electrode, whose exchange current density tends to infinity: its potential hardly changes when current passes, and a good reference electrode approaches this case. An electrode with a very small $j_0$ is called easily polarizable, and one with a very large $j_0$ approximates a reversible electrode.

### 14.3.5. The Hydrogen Evolution Reaction

**Definition 14.3.4** The electrode reaction in which $\ce{H+}$ (in acidic solution) or $\ce{H2O}$ (in neutral and basic solutions) is reduced to $\ce{H2}$ at a cathode is called the **hydrogen evolution reaction** (HER): $\ce{2H+ + 2e- -> H2}$ or $\ce{2H2O + 2e- -> H2 + 2OH-}$.

Hydrogen evolution is the most studied electrode reaction; it is the cathode reaction of water electrolysis for hydrogen production, and a side reaction in metal electrodeposition, corrosion and the charging of lead–acid batteries. The overpotential of hydrogen evolution on all metals obeys the Tafel relation, with the constant $b$ about $0.10$–$0.14\,\mathrm{V}$, whereas $a$ (the overpotential at $\lvert j\rvert = 1\,\mathrm{A\,cm^{-2}}$) differs greatly; by $a$, metals fall into three classes:

| Class | $a$/V | Metals |
|---|---|---|
| High overpotential | 1.0–1.5 | Pb, Cd, Hg, Tl, Zn, Ga, Bi, Sn |
| Intermediate overpotential | 0.5–0.7 | Fe, Co, Ni, Cu, W, Au |
| Low overpotential | 0.1–0.3 | Pt, Pd, Ru and other platinum-group metals |

The mechanism of hydrogen evolution comprises the following steps (M denotes an adsorption site on the electrode surface; acidic solution):

$$
\begin{aligned}
&\text{Volmer step (electrochemical adsorption):} && \ce{M + H+ + e- -> M-H},\\
&\text{Tafel step (recombination desorption):} && \ce{2M-H -> 2M + H2},\\
&\text{Heyrovsky step (electrochemical desorption):} && \ce{M-H + H+ + e- -> M + H2}.
\end{aligned}
$$
The overall reaction can proceed by the Volmer–Tafel or the Volmer–Heyrovsky route, and which step is rate-determining fixes the Tafel slope: $b \approx 118\,\mathrm{mV}$ when the Volmer step is rate-determining, about $40\,\mathrm{mV}$ for the Heyrovsky step and about $30\,\mathrm{mV}$ for the Tafel step ($25\,^\circ\mathrm{C}$). On high-overpotential metals such as mercury and lead the Volmer step (the discharge step) is usually slow; on platinum in acid $b \approx 30\,\mathrm{mV}$ and the recombination step is rate-determining. Measuring the Tafel slope is an important basis for inferring the mechanism of an electrode reaction.

The main determinant of the rate of hydrogen evolution is the strength of hydrogen adsorption on the electrode surface. If adsorption is too weak (Hg, Pb), the barrier of the Volmer step is high; if it is too strong (W, Mo), the M–H formed is too stable and hard to desorb. A plot of $\lg j_0$ against the strength of the metal–hydrogen bond gives a "volcano curve", high in the middle and low on both sides, with the platinum-group metals near the top: this is a typical example of the **Sabatier principle** in heterogeneous catalysis ([6.3.20](/6.3.20)). Hydrogen adsorbed on platinum can be measured by cyclic voltammetry: at potentials more positive than the reversible hydrogen electrode, hydrogen adsorbs on Pt as a monolayer (underpotential deposition); saturated adsorbed hydrogen on polycrystalline platinum corresponds to a charge of about $210\,\mu\mathrm{C\,cm^{-2}}$, equivalent to one H atom per surface Pt atom, and is often used to determine the real surface area of platinum electrodes; the adsorption peaks occur at different positions on different crystal faces ((100), (110), (111)), reflecting differences in adsorption strength. The search for cheap hydrogen evolution catalysts to replace platinum (such as the edge sites of $\ce{MoS2}$ and transition-metal phosphides) is one of the central problems of hydrogen production by water electrolysis.

## 14.4. Concentration Polarization and the Limiting Current

### 14.4.1. The Diffusion Layer and the Limiting Diffusion Current

In a stirred solution, convection keeps the concentration in the bulk uniform, but a thin layer of solution adjacent to the electrode is almost motionless, and matter can cross it only by diffusion. Nernst approximated this layer as a diffusion layer of thickness $\delta$ (usually $10$–$100\,\mu\mathrm{m}$), within which the concentration varies linearly. For the cathode reaction $\ce{O + ze- -> R}$ (with a large amount of supporting electrolyte added, so that the electromigration of O is negligible), at steady state the diffusion flux to the surface equals the reaction rate, and by **Fick's law** the magnitude of the current density is

$$
\lvert j\rvert = zFD_{\mathrm{O}}\frac{c^*_{\mathrm{O}} - c_{\mathrm{O}}(0)}{\delta}.
$$
Increasing the overpotential lowers the surface concentration $c_{\mathrm{O}}(0)$ and increases the current; when $c_{\mathrm{O}}(0) \to 0$ the concentration gradient is at its maximum and the current no longer increases with potential.

**Definition 14.4.1** The maximum current (density) set by the rate of diffusion when the reactant concentration at the electrode surface has dropped to zero,

$$
\lvert j_{\mathrm{L}}\rvert = \frac{zFD_{\mathrm{O}}c^*_{\mathrm{O}}}{\delta},
$$
is called the **limiting current** (limiting diffusion current).

For $D = 1\times10^{-9}\,\mathrm{m^2\,s^{-1}}$, $c^* = 1\,\mathrm{mmol\,L^{-1}}$, $\delta = 50\,\mu\mathrm{m}$ and $z = 1$, $\lvert j_{\mathrm{L}}\rvert = 1.9\,\mathrm{A\,m^{-2}}$. The limiting current is proportional to the concentration and is the basis of quantitative electroanalysis. From $c_{\mathrm{O}}(0)/c^*_{\mathrm{O}} = 1 - j/j_{\mathrm{L}}$, if electron transfer is fast (the electrode is in the "reversible" state, with the surface concentrations satisfying the Nernst equation) and the product is a pure metal ($a_{\mathrm{R}} = 1$), the concentration overpotential is

$$
\eta_{\text{conc}} = \frac{RT}{zF}\ln\frac{c_{\mathrm{O}}(0)}{c^*_{\mathrm{O}}} = \frac{RT}{zF}\ln\left(1 - \frac{j}{j_{\mathrm{L}}}\right), \tag{14.4}
$$
which tends to negative infinity as $j$ approaches $j_{\mathrm{L}}$; the electrode potential then keeps falling until another electrode reaction (such as hydrogen evolution) begins. When electron transfer is not fast, substituting $c(0)/c^*$ into Eq. (14.2) gives the complete polarization curve containing both activation and concentration polarization.

### 14.4.2. Potential Step and the Cottrell Equation

In an unstirred solution the diffusion layer is not fixed but extends into the solution with time. Let a planar electrode be immersed in a quiescent solution containing only O (concentration $c^*$) and a large amount of supporting electrolyte, and at $t = 0$ let the electrode potential be stepped into the limiting-current region, so that the concentration of O at the electrode surface drops to zero immediately.

**Theorem 14.4.1 (Cottrell Equation)** Under conditions of semi-infinite linear diffusion, the current density after a potential step is

$$
\lvert j(t)\rvert = zFc^*\sqrt{\frac{D}{\pi t}}.
$$

**Proof** The concentration $c(x, t)$ of O satisfies the one-dimensional **diffusion equation** $c_t = Dc_{xx}$ ($x > 0$, [2.5.1](/2.5.1)), with initial condition $c(x, 0) = c^*$ and boundary conditions $c(0, t) = 0$ and $c(\infty, t) = c^*$. Let $u = c/c^*$; this is exactly [Example 7.3.1 of 2.5.7](/2.5.7#ex-7.3.1) (a semi-infinite rod with initial temperature 1 and the end held at 0), and the method of reflection gives

$$
c(x, t) = c^*\operatorname{erf}\left(\frac{x}{2\sqrt{Dt}}\right).
$$
From $\frac{\mathrm{d}}{\mathrm{d}s}\operatorname{erf}s = \frac{2}{\sqrt\pi}\mathrm{e}^{-s^2}$, the concentration gradient at the surface is $(\partial c/\partial x)_{x=0} = c^*/\sqrt{\pi Dt}$. The current density is $zF$ times the flux $D(\partial c/\partial x)_{x=0}$ reaching the surface, which gives the result. $\square$

The current decays as $t^{-1/2}$: after the reactant near the surface is depleted, the depletion layer extends into the solution as $\sqrt{Dt}$ and the gradient decreases accordingly. The tangent to the concentration profile at $x = 0$ meets $c = c^*$ at $\delta(t) = \sqrt{\pi Dt}$, which is the meaning of the "diffusion layer thickness" in the transient case, and substituting it into the steady-state formula of 14.4.1 also gives the Cottrell equation. A plot of $\lvert j\rvert$ against $t^{-1/2}$ is a straight line through the origin, and the diffusion coefficient $D$ can be determined from its slope (chronoamperometry). As $t \to \infty$ the current tends to zero, so a planar electrode in quiescent solution has no steady-state limiting current; in practice natural convection stops the extension of the diffusion layer after a few seconds to a few tens of seconds.

![Semi-infinite linear diffusion at a planar electrode after a potential step to the diffusion limit (D = 1.0×10⁻⁹ m² s⁻¹, c* = 1 mol m⁻³, z = 1). Left: concentration profiles c/c* = erf(x/2√(Dt)) at different times, the dashed line being the tangent at x = 0, which meets c = c* at δ = √(πDt); right: the Cottrell current decays as t^(−1/2), and in the inset |j| is a straight line through the origin against t^(−1/2)](./plots/cottrell.py)

### 14.4.3. Polarography

**Definition 14.4.2** The electroanalytical method in which a dropping mercury electrode is used as the working electrode, the electrode potential is varied linearly in a quiescent solution, and the current–potential curve (polarogram) is recorded, with quantitative analysis from the magnitude of the diffusion current and qualitative analysis from the half-wave potential, is called **polarography**.

Polarography was invented by Heyrovský in 1922 (Nobel Prize in Chemistry, 1959). The dropping mercury electrode is a mercury drop that flows from a fine glass capillary and falls periodically. It has two advantages: the overpotential of hydrogen on mercury is very large, so the reduction of metal ions can be measured at very negative potentials without interference from hydrogen evolution; and each drop provides a fresh, reproducible surface that does not accumulate reaction products. Take $\ce{Cd^2+ + 2e- -> Cd(Hg)}$ as an example: when the applied potential is more positive, only a small residual current flows; as the potential becomes negative enough for $\ce{Cd^2+}$ to begin to be reduced, the current rises; as it becomes still more negative, the surface concentration of $\ce{Cd^2+}$ falls to zero and the current reaches a plateau limited by diffusion. The height of the plateau (the limiting diffusion current $I_{\mathrm{d}}$) is proportional to the concentration; the potential at which the current is half of the plateau is called the half-wave potential $E_{1/2}$, which is approximately equal to the formal potential of the couple and can be used to identify the substance.

The mercury drop keeps growing, so its surface area increases with time while the diffusion layer extends; extending the Cottrell treatment to a growing spherical surface gives the Ilkovič equation (1934): the mean diffusion current over the life of a drop is

$$
\bar I_{\mathrm{d}} = 607\,zD^{1/2}m^{2/3}t_{\mathrm{d}}^{1/6}c,
$$
where $\bar I_{\mathrm{d}}$ is in $\mu\mathrm{A}$, $D$ in $\mathrm{cm^2\,s^{-1}}$, the mercury flow rate $m$ in $\mathrm{mg\,s^{-1}}$, the drop time $t_{\mathrm{d}}$ in s and the concentration $c$ in $\mathrm{mmol\,L^{-1}}$. Unlike the Cottrell equation (the transient current at a planar electrode), the Ilkovič equation describes the current of each drop at a periodically renewed electrode, so the diffusion current in polarography has a steady mean value. Because of the toxicity of mercury, classical polarography has largely been replaced by cyclic voltammetry, pulse voltammetry and stripping voltammetry at solid electrodes, but their theoretical basis, diffusion-controlled current, is the same as that of polarography ([Analytical Chemistry](/6.4)).

## 14.5. Applications of Electrolysis

### 14.5.1. Advantages and Disadvantages of Overpotential

Overpotential increases the energy consumption of electrolysis and lowers the output voltage of batteries, and from the standpoint of energy utilization it should be minimized: the chlor-alkali industry replaced graphite with titanium anodes coated with $\ce{RuO2}$–$\ce{TiO2}$ (dimensionally stable anodes, DSA), which lowers the overpotential of $\ce{Cl2}$ evolution by about $0.2$–$0.3\,\mathrm{V}$, saves about 10% of the electricity, and eliminates electrode wear. But in many cases the overpotential is beneficial or even essential.

- Electrowinning of zinc: $\ce{ZnS}$ is roasted to $\ce{ZnO}$ and leached with sulfuric acid to give a $\ce{ZnSO4}$ solution, which is electrolyzed to give Zn at the cathode. $E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.762\,\mathrm{V}$ is far below $\ce{H+}/\ce{H2}$, and thermodynamically $\ce{H2}$ should evolve at the cathode; but at industrial current densities (about $400$–$600\,\mathrm{A\,m^{-2}}$) the overpotential of $\ce{H2}$ on Zn is about $-1.0\,\mathrm{V}$, the actual potential of hydrogen evolution falls below the deposition potential of Zn, Zn is deposited preferentially, and the current efficiency is about 90%.
- Charging a lead–acid battery: the potential of the negative-electrode reaction $\ce{PbSO4 + H+ + 2e- -> Pb + HSO4-}$ (about $-0.36\,\mathrm{V}$) is below the equilibrium potential of hydrogen evolution, and that $\ce{PbSO4}$ is mainly reduced during charging rather than $\ce{H2}$ being evolved depends on the large overpotential of hydrogen on lead (Tafel constant $a \approx 1.5\,\mathrm{V}$). At the positive electrode likewise one relies on the overpotential of $\ce{O2}$ on $\ce{PbO2}$.
- Electroplating: $E^\circ(\ce{Cr^3+}/\ce{Cr}) = -0.744\,\mathrm{V}$, whereas in neutral solution $E(\ce{H+}/\ce{H2}) = -0.41\,\mathrm{V}$; chromium plating can proceed only because of the overpotential of hydrogen evolution; even so, the current efficiency of traditional hexavalent chromium plating is only 10%–25%, and most of the current goes to hydrogen evolution. Hexavalent chromium is highly toxic and is being replaced by trivalent chromium baths.

### 14.5.2. Order of Deposition of Metals and Their Separation

When a solution containing several metal ions is electrolyzed, the reaction at the cathode is the reduction with the highest actual deposition potential (the equilibrium potential plus the overpotential, the higher potential having priority); the reaction at the anode is the oxidation with the lowest actual deposition potential. As the reaction proceeds, the ion concentration falls and the deposition potential becomes steadily more negative; when it drops to the deposition potential of the second metal, the second metal begins to deposit. The residual concentration of the first metal at that point is determined by the condition that the two potentials be equal, from which one can judge whether the two metals can be separated.

**Example 14.5.1** A solution containing $0.10\,\mathrm{mol\,L^{-1}}$ each of $\ce{CuSO4}$ and $\ce{ZnSO4}$ and $0.10\,\mathrm{mol\,L^{-1}}$ $\ce{H2SO4}$ is electrolyzed between Pt electrodes ($25\,^\circ\mathrm{C}$). The overpotential of $\ce{H2}$ is $-1.0\,\mathrm{V}$ on Cu and $-1.3\,\mathrm{V}$ on Zn, and negligible on Pt; neglect the overpotential of $\ce{O2}$ and $IR$, take concentrations in place of activities, and assume that $\ce{H2SO4}$ is completely dissociated. (1) Which substance is deposited first? What initial voltage is required? (2) What is the voltage when the second metal begins to deposit? What is the residual concentration of the first metal? (3) At what voltage does $\ce{H2}$ begin to evolve?

**Solution** (1) Initially $[\ce{H+}] = 0.20\,\mathrm{mol\,L^{-1}}$. The deposition potentials of the cathode reactions are:

$$
\begin{aligned}
E(\ce{Cu^2+}/\ce{Cu}) &= 0.342 + 0.02958\lg0.10 = 0.312\,\mathrm{V},\\
E(\ce{Zn^2+}/\ce{Zn}) &= -0.762 + 0.02958\lg0.10 = -0.792\,\mathrm{V},\\
E(\ce{H+}/\ce{H2}, \text{on Pt}) &= 0.05916\lg0.20 = -0.041\,\mathrm{V}.
\end{aligned}
$$
Cu has the highest deposition potential, so it deposits first and soon covers the Pt surface; thereafter $\ce{H2}$ must evolve on Cu, and its potential drops to $-0.041 - 1.0 = -1.04\,\mathrm{V}$. At the anode, $\ce{H2O -> 2H+ + 1/2O2 + 2e-}$ has $E = 1.229 + 0.05916\lg0.20 = 1.188\,\mathrm{V}$. The initial voltage is $U = 1.188 - 0.312 = 0.876\,\mathrm{V}$.

(2) For each mole of Cu deposited, the anode produces $2\,\mathrm{mol}$ of $\ce{H+}$; when the Cu is exhausted $[\ce{H+}] = 0.40\,\mathrm{mol\,L^{-1}}$, and the deposition potential of $\ce{H2}$ on Cu is $0.05916\lg0.40 - 1.0 = -1.02\,\mathrm{V}$, still below the $-0.792\,\mathrm{V}$ of Zn, so Zn is the next to deposit. The cathode potential is then $-0.792\,\mathrm{V}$, and the residual $\ce{Cu^2+}$ satisfies $0.342 + 0.02958\lg[\ce{Cu^2+}] = -0.792$, giving $[\ce{Cu^2+}] = 4.6\times10^{-39}\,\mathrm{mol\,L^{-1}}$: the copper has been completely separated. At the anode $E = 1.229 + 0.05916\lg0.40 = 1.205\,\mathrm{V}$, and $U = 1.205 + 0.792 = 1.997\,\mathrm{V}$.

(3) During the deposition of Zn, $[\ce{H+}]$ continues to rise and is $0.60\,\mathrm{mol\,L^{-1}}$ when Zn is essentially all deposited; the deposition potential of $\ce{H2}$ on Zn is $0.05916\lg0.60 - 1.3 = -1.313\,\mathrm{V}$; when the cathode potential falls to this value, hydrogen evolution begins, and the residual $\ce{Zn^2+}$ satisfies $-0.762 + 0.02958\lg[\ce{Zn^2+}] = -1.313$, giving $[\ce{Zn^2+}] = 2.3\times10^{-19}\,\mathrm{mol\,L^{-1}}$. At the anode $E = 1.229 + 0.05916\lg0.60 = 1.216\,\mathrm{V}$, and $U = 1.216 + 1.313 = 2.53\,\mathrm{V}$.

(Calculations with the older data $E^\circ(\ce{Cu^2+}/\ce{Cu}) = 0.337\,\mathrm{V}$ and $E^\circ(\ce{Zn^2+}/\ce{Zn}) = -0.763\,\mathrm{V}$ give slightly different numbers, with the same conclusions.) $\square$

In practical electrolysis, separation is generally considered complete when the ion concentration has fallen below $10^{-6}\,\mathrm{mol\,L^{-1}}$; for $z = 2$ this requires the deposition potentials of the two metals to differ by about $0.15\,\mathrm{V}$ or more. Electrolysis with control of the cathode potential (rather than the cell voltage) is the basis of controlled-potential coulometry and electrogravimetric analysis in analytical chemistry.

### 14.5.3. Electrosynthesis

**Definition 14.5.1** The preparation of chemical substances by electrolysis is called **electrosynthesis** (electrochemical synthesis).

Products of electrosynthesis include reactive metals (molten-salt electrolysis of Na, Mg and Al), strong oxidants ($\ce{KMnO4}$, $\ce{K2Cr2O7}$, persulfates, $\ce{KClO4}$), chlor-alkali products ($\ce{NaOH}$, $\ce{Cl2}$, $\ce{H2}$), fluorine-containing compounds (electrochemical fluorination) and organic compounds. Its advantages are that reactions proceed at ordinary temperature and pressure, the driving force and selectivity are controlled precisely through the electrode potential, the electron is the "cleanest reagent", and the products are easily separated with little pollution; its disadvantages are high energy consumption and equipment and management costs, and the capacity of a reactor is limited by the electrode area. As renewable electricity becomes cheaper, electrosynthesis is regarded as the main route to the "electrification" of the chemical industry.

The most successful example of organic electrosynthesis is the electroreductive dimerization of acrylonitrile to adiponitrile (the raw material of nylon-66; commissioned by Monsanto in 1965):

```smiles
C=CC#N.C=CC#N>>N#CCCCCC#N
```

The cathode reaction is $\ce{2CH2=CHCN + 2H+ + 2e- -> NC(CH2)4CN}$, the anode reaction is $\ce{H2O -> 1/2O2 + 2H+ + 2e-}$, and the overall reaction is $\ce{2CH2=CHCN + H2O -> NC(CH2)4CN + 1/2O2}$. The key to the cathode reaction is that, on a Pb or Cd cathode with a high $\ce{H2}$ overpotential and with a quaternary ammonium salt to suppress protonation, the radical anions formed by adding electrons to acrylonitrile dimerize rather than being hydrogenated directly to propionitrile. Another research direction is the synthesis of ammonia from $\ce{N2}$ and $\ce{H2}$ (or $\ce{H2O}$) at atmospheric pressure in a solid proton-conductor electrolysis cell, for example $\ce{H2}(\ce{Pd}) \mid \text{SCY (Yb-doped } \ce{SrCeO3}\text{)} \mid \ce{N2}(\ce{Pd})$: the anode reaction is $\ce{3H2 -> 6H+ + 6e-}$ and the cathode reaction is $\ce{N2 + 6H+ + 6e- -> 2NH3}$. The current densities of such cells are currently very low (below $2\,\mathrm{mA\,cm^{-2}}$), and the reduction of $\ce{N2}$ competes with hydrogen evolution, so they are far from practical.

## 14.6. Corrosion and Protection of Metals

### 14.6.1. Electrochemical Corrosion

**Definition 14.6.1** The destruction of a metal in contact with an electrolyte solution through an electrochemical process in which anodic dissolution and cathodic reduction occur simultaneously is called **electrochemical corrosion**. When the cathode reaction is the reduction of $\ce{H+}$ (or $\ce{H2O}$), it is called **hydrogen-evolution corrosion**; when it is the reduction of dissolved oxygen ($\ce{O2 + 4H+ + 4e- -> 2H2O}$ or $\ce{O2 + 2H2O + 4e- -> 4OH-}$), it is called **oxygen-absorption corrosion**.

For example, iron in contact with copper and immersed in water forms a short-circuited galvanic cell (a corrosion cell): iron is the anode, $\ce{Fe -> Fe^2+ + 2e-}$; the copper surface is the cathode, with $\ce{2H+ + 2e- -> H2}$ in acidic solution and $\ce{O2 + 2H2O + 4e- -> 4OH-}$ in neutral aerated water. Even a uniform piece of metal has many microcells formed by impurities at the surface, grain boundaries, stress and small differences in composition. The potential of the oxygen electrode rises with the partial pressure of oxygen, $E = 1.229\,\mathrm{V} + \frac{RT}{4F}\ln[(p_{\ce{O2}}/p^\circ)a(\ce{H+})^4]$; for an iron pile partly immersed in water, the part near the water surface, where the oxygen supply is plentiful, becomes the cathode, and the oxygen-starved part under water becomes the anode and is corroded. This is a kind of concentration cell, called differential aeration corrosion. Corrosion in crevices, under deposits and below the waterline of ship hulls are all of this type.

### 14.6.2. Corrosion Potential and Corrosion Current

On a corroding piece of metal, the anodic and cathodic reactions proceed simultaneously on the same surface with no external current, so the anodic and cathodic currents are equal in magnitude and the metal is at a steady potential.

**Definition 14.6.2** The electrode potential at which a metal corrodes spontaneously in a corrosive medium, with the anodic dissolution current equal in magnitude to the cathodic reduction current, is called the **corrosion potential** (mixed potential) $E_{\operatorname{Corr}}$, and the anodic current density at that point is called the corrosion current density $j_{\operatorname{Corr}}$.

The corrosion potential is not the equilibrium potential of any couple but lies between the equilibrium potential of metal dissolution and that of the cathode reaction, and is determined by the intersection of the two polarization curves: plot the anodic and cathodic Tafel lines with $\lg\lvert j\rvert$ as abscissa and $E$ as ordinate; the intersection gives $E_{\operatorname{Corr}}$ and $j_{\operatorname{Corr}}$, and such a diagram is called an Evans diagram. The diagram shows the factors that influence the corrosion rate: the higher the equilibrium potential of the cathode reaction (the stronger the oxidant), the larger the $j_0$ of the two reactions and the smaller the Tafel slopes, the larger the current at the intersection and the faster the corrosion. In neutral water the solubility of $\ce{O2}$ is only about $0.25\,\mathrm{mmol\,L^{-1}}$, and oxygen-absorption corrosion is often controlled by the diffusion of $\ce{O2}$ to the metal surface; the corrosion current is then the limiting diffusion current of oxygen: stirring or flow accelerates corrosion, whereas the nature of the metal itself has little effect.

The corrosion current can be converted into a corrosion rate. For iron, by Faraday's law a corrosion current of $1\,\mathrm{A\,m^{-2}}$ corresponds to $\frac{55.85 \times 3.156\times10^7}{2\times96\,485}\,\mathrm{g\,m^{-2}} = 9.1\,\mathrm{kg\,m^{-2}}$ per year, that is, a thinning of about $1.2\,\mathrm{mm}$ per year.

![Evans diagrams for the corrosion of iron (25 °C, schematic Tafel parameters). Left: deaerated acidic solution (pH 1), in which both the anodic dissolution of iron and the reduction of H⁺ are activation-controlled, and the intersection of the two Tafel lines gives the corrosion potential and the corrosion current; right: neutral aerated water, in which the reduction of O₂ is diffusion-controlled and the corrosion current equals the limiting diffusion current of O₂](./plots/evans-diagram.py)

### 14.6.3. Protection Against Corrosion

The Fe–H₂O potential–pH diagram of [6.3.13](/6.3.13) and the Evans diagram above suggest approaches to protection: bring the metal into the immunity or passivation region, or slow the anodic and cathodic reactions.

1. Use of corrosion-resistant materials: Cr in stainless steel (above 12% by mass) forms a dense $\ce{Cr2O3}$ passive film on the surface; titanium and aluminum also resist corrosion by their oxide films.
2. Protective coatings: nonmetallic coatings such as paint, enamel and plastics, and metal layers applied by electroplating or hot dipping. A metal more active than the substrate (zinc-coated iron) still protects the substrate as an anode after the coating is damaged; a metal less active than the substrate (tin-coated iron), once damaged, accelerates the corrosion of the substrate instead.
3. Electrochemical protection:

**Definition 14.6.3** The method of connecting to the metal to be protected a metal of lower electrode potential (Zn, Mg, Al alloys), so that the protected metal becomes the cathode of a corrosion cell and is protected while the other metal is consumed gradually as the anode, is called **sacrificial anode protection**; the method of connecting the metal to be protected to the negative terminal of an external DC source so that its potential falls into the immunity region (cathodic polarization) is called **cathodic protection** (impressed current cathodic protection).

The two have the same principle: the potential of the metal is lowered to near or below its equilibrium potential, so that the rate of anodic dissolution is negligible. The criterion for protection of steel in soil and seawater is usually a potential of $-0.85\,\mathrm{V}$ (relative to a $\ce{Cu}/\ce{CuSO4}$ reference electrode, about $-0.53\,\mathrm{V}$ vs SHE). Ship hulls, offshore platforms, underground pipelines and storage tanks generally use these two methods. Another approach is anodic protection: for metals that can be passivated (stainless steel and titanium, in media such as sulfuric acid), an external source raises the potential into the passivation region and holds it there, and the anodic current falls to a very small passivation-maintaining current; this requires accurate control of the potential, otherwise the system enters the transpassive region.

4. Corrosion inhibitors:

**Definition 14.6.4** A substance that markedly lowers the corrosion rate of a metal when added in a small amount to the corrosive medium is called a **corrosion inhibitor**.

Inhibitors either adsorb on the metal surface and hinder the anodic or cathodic reaction (organic amines and benzotriazole for copper), or promote the formation of passive films (chromates, nitrites, molybdates), or remove the corrosive agent (sodium sulfite or hydrazine added to boiler water to remove oxygen). According to whether they act on the anodic or the cathodic reaction, they are classified as anodic, cathodic or mixed.

## 14.7. Electrochemical Power Sources

### 14.7.1. Performance Parameters

For the definitions of **electrochemical power source**, **primary cell** and **secondary cell** and the reactions of common cells, see [6.1.12](/6.1.12). Electrochemical power sources serve as power generation devices (fuel cells, which raise the efficiency of fuel utilization), energy storage devices (lithium-ion batteries and flow batteries, working with renewable energy and the grid) and mobile power supplies (electronic devices, electric vehicles). The main parameters for evaluating a battery are:

- Capacity: the quantity of electricity a battery can deliver on discharge, in $\mathrm{A\,h}$ ($1\,\mathrm{A\,h} = 3600\,\mathrm{C}$). The energy stored equals the capacity times the average discharge voltage ($\mathrm{W\,h}$).
- Rate: the ratio of the charge or discharge current to the rated capacity, denoted C. A $10\,\mathrm{A\,h}$ battery discharged at $5\,\mathrm{A}$ is at a rate of $0.5\mathrm{C}$ (2-hour rate). The higher the rate, the greater the polarization and the less capacity is delivered.
- Power density: the maximum power per unit mass (or volume) a battery can deliver, in $\mathrm{W\,kg^{-1}}$ or $\mathrm{W\,L^{-1}}$, determined by the internal resistance and polarization.
- Cycle life: the number of charge–discharge cycles before the capacity decays to a given fraction (such as 80%) of its initial value.

**Definition 14.7.1** The quantity of electricity that a unit mass of electrode active material can deliver is called the **specific capacity**; its theoretical value is

$$
C = \frac{zF}{3.6M}\ \mathrm{mA\,h\,g^{-1}},
$$
where $z$ is the number of electrons transferred per mole of active material and $M$ is its molar mass ($\mathrm{g\,mol^{-1}}$); $3.6 = 3600\,\mathrm{C\,(A\,h)^{-1}}/1000$. The electrical energy stored per unit mass (or volume) of a battery is called the **specific energy** (gravimetric energy density), in $\mathrm{W\,h\,kg^{-1}}$; it equals the product of the specific capacity and the average voltage.

For example, the theoretical specific capacity of $\ce{LiCoO2}$ ($M = 97.87\,\mathrm{g\,mol^{-1}}$) is $96\,485/(3.6\times97.87) = 274\,\mathrm{mA\,h\,g^{-1}}$, but removing too much lithium destabilizes the layered structure, and in practice only about 0.5–0.6 Li is used, about $140$–$180\,\mathrm{mA\,h\,g^{-1}}$; graphite (as $\ce{LiC6}$, per gram of carbon) gives $372\,\mathrm{mA\,h\,g^{-1}}$; lithium metal gives $3860\,\mathrm{mA\,h\,g^{-1}}$. The ways to raise the specific energy are to raise the specific capacity of the electrode materials (light elements, multi-electron reactions) and to raise the potential difference between the positive and negative electrodes, the latter being limited by the electrochemical window of the electrolyte (14.1.3).

The curve of voltage against capacity when a battery is charged and discharged at constant current is called the charge–discharge curve. Differentiating it and plotting $\mathrm{d}Q/\mathrm{d}E$ (or $\mathrm{d}x/\mathrm{d}E$) against potential gives the differential capacity curve; from $x = \int_0^t I\,\mathrm{d}t$ and the potential scan rate $v = \mathrm{d}E/\mathrm{d}t$, $\mathrm{d}x/\mathrm{d}E = I/v$, so it is equivalent to the cyclic voltammogram at a slow scan rate, and the peaks on the curve correspond to the individual electrochemical reaction steps or phase transitions of the electrode material.

### 14.7.2. Intercalation Reactions

**Definition 14.7.2** An electrode reaction in which guest ions (such as $\ce{Li+}$, $\ce{Na+}$, $\ce{H+}$) together with electrons enter (or leave) the vacancies or interlayer spaces of a host lattice reversibly, with the host structure remaining essentially unchanged, is called an **intercalation reaction**: $x\ce{A+} + \langle\mathrm{H}\rangle + x\ce{e-} \rightleftharpoons \mathrm{A}_x\langle\mathrm{H}\rangle$.

Both electrodes of a lithium-ion battery undergo intercalation reactions ([6.1.12](/6.1.12)), for example at the positive electrode $\ce{Li_{1-x}CoO2} + x\ce{Li+} + x\ce{e-} \rightleftharpoons \ce{LiCoO2}$ and at the negative electrode $\ce{C6} + x\ce{Li+} + x\ce{e-} \rightleftharpoons \ce{Li_xC6}$. Unlike the pure solid phases of fixed composition in the Nernst equation, the guest content $x$ of an intercalation compound varies continuously, and the electrode potential varies with it.

The simplest model is the lattice gas: guests are distributed over $N$ equivalent sites in the host, with $x$ the fractional occupancy. In the ideal case the mixing entropy of the guests gives $\mu_{\mathrm{A}} = \mu^\circ + RT\ln\frac{x}{1-x}$ (the statistical method of [6.3.10](/6.3.10), with the same mathematics as Langmuir adsorption in [6.3.20](/6.3.20)); adding a mean-field interaction between neighboring guests (a regular solution, [6.3.6](/6.3.6)), $E = -(\mu_{\mathrm{A}} - \mu_{\ce{Li}})/F$ gives

$$
E = E^\circ - \frac{RT}{F}\ln\frac{x}{1-x} + f\left(x - \frac12\right), \tag{14.5}
$$
where $f$ reflects the effective interaction between guests. For $f = 0$ the $E$–$x$ curve is an inclined S-shape and the differential capacity curve is a broad peak; the larger $f$ is, the flatter the curve near $x = 1/2$ and the narrower the peak. For $f > 4RT/F$ ($0.103\,\mathrm{V}$ at $25\,^\circ\mathrm{C}$), $E(x)$ is no longer monotonic, the homogeneous solid solution is unstable, and it separates into a lithium-poor and a lithium-rich phase; this is the same as the appearance of a two-phase region in partially miscible binary liquid systems in [6.3.9](/6.3.9). When the two phases coexist, the chemical potential of the guest is constant, the charge–discharge curve shows a voltage plateau, and the differential capacity curve shows a sharp peak. $\ce{LiFePO4}$ is exactly such a two-phase reaction ($\ce{FePO4}$ and $\ce{LiFePO4}$ coexisting), so it has a very flat discharge plateau at about $3.4\,\mathrm{V}$; lithium intercalation into graphite passes through several staged structures and shows several steps.

![Lattice-gas (regular solution) model of an intercalation electrode at 25 °C: left, the equilibrium potential as a function of the intercalation amount x, with the curve flatter for larger f, and for f = 0.20 V > 4RT/F two-phase separation occurs and the potential becomes a plateau at E° (the dotted line is the unstable homogeneous solution); right, the corresponding differential capacity curve −dx/dE, in which the two-phase reaction shows as a sharp peak](./plots/intercalation.py)

### 14.7.3. Electrode Materials of Lithium-Ion Batteries

The potential of a positive-electrode material is determined by the redox energy levels of the transition-metal ion and is also influenced by the crystal structure and the coordinating anion: for example, for the same $\ce{Fe^3+}/\ce{Fe^2+}$ couple, the potential in a $\ce{PO4^3-}$ framework is much higher than in an oxide because of the inductive effect (the strong covalency of the P–O bond weakens the Fe–O bond).

| Material | Structure | Average potential / V (vs $\ce{Li+}/\ce{Li}$) | Practical specific capacity / ($\mathrm{mA\,h\,g^{-1}}$) | Features |
|---|---|---|---|---|
| $\ce{LiCoO2}$ (LCO) | Layered | 3.9 | 150–180 (theoretical 274) | High volumetric energy density, cobalt is expensive |
| Ternary materials such as $\ce{LiNi_{0.8}Mn_{0.1}Co_{0.1}O2}$ (NMC811) | Layered | 3.7–3.8 | 190–210 | Mainstream in electric vehicles; the more nickel, the higher the capacity and the lower the stability |
| $\ce{LiNi_{0.8}Co_{0.15}Al_{0.05}O2}$ (NCA) | Layered | 3.7 | about 200 | High energy |
| $\ce{LiMn2O4}$ (LMO) | Spinel | 4.0–4.1 | 110–120 (theoretical 148) | Cheap, good rate capability, Mn dissolves at high temperature |
| $\ce{LiFePO4}$ (LFP) | Olivine | 3.4 | about 160 (theoretical 170) | Safe, long life, cobalt-free; energy storage and electric vehicles |
| $\ce{LiCoPO4}$ | Olivine | 4.8 | Under research | High voltage, beyond the window of conventional electrolytes |
| Graphite (negative) | Layered | about 0.1 | 340–360 (theoretical 372) | Mainstream negative electrode |
| Silicon (negative) | Alloying | about 0.4 | Theoretical about 3600 | Volume change up to 300%, mixed in small amounts with graphite |
| $\ce{Li4Ti5O12}$ (LTO, negative) | Spinel | 1.55 | about 165 | Zero strain, high safety, high rate capability, low voltage |

The specific energy of present cells is about $160$–$200\,\mathrm{W\,h\,kg^{-1}}$ for LFP and about $250$–$300\,\mathrm{W\,h\,kg^{-1}}$ for high-nickel ternary materials.

Another type of electrode reaction is the conversion reaction, $\ce{MX + n Li+ + n e- -> M + Li_nX}$, in which the host structure is destroyed completely; the capacity is large but the reversibility is poor. The positive-electrode reaction of the Li–S battery, $\ce{S8 + 16Li+ + 16e- -> 8Li2S}$ (theoretical specific capacity $1672\,\mathrm{mA\,h\,g^{-1}}$, average voltage about $2.1\,\mathrm{V}$), is one example: sulfur and $\ce{Li2S}$ are both electronic insulators, and the intermediate lithium polysulfides dissolve in the electrolyte and "shuttle" between the two electrodes, causing capacity fade; supporting the sulfur in porous carbon can partly alleviate this.

### 14.7.4. Fuel Cells

**Definition 14.7.3** An electrochemical device in which a fuel ($\ce{H2}$, methanol, natural gas, etc.) and an oxidant (usually $\ce{O2}$ from the air) are supplied continuously to the electrodes from outside and the chemical energy of combustion of the fuel is converted directly into electrical energy is called a **fuel cell**.

A fuel cell is not limited by the Carnot efficiency ([6.3.2](/6.3.2)): the maximum efficiency of $\ce{H2 + 1/2O2 -> H2O(l)}$ at $25\,^\circ\mathrm{C}$ is $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = 237.1/285.8 = 83\%$. In practice, the exchange current density for $\ce{O2}$ reduction is very small, the operating voltage is about $0.6$–$0.8\,\mathrm{V}$ (electromotive force $1.23\,\mathrm{V}$), and the electrical efficiency is about 40%–60%.

| Type | Electrolyte | Operating temperature | Main applications |
|---|---|---|---|
| Proton-exchange membrane fuel cell (PEMFC) | Perfluorosulfonic acid membrane (conducts $\ce{H+}$) | 60–80 °C (high-temperature type 120–200 °C) | Vehicles, portable power; fast start-up, needs Pt catalyst and pure $\ce{H2}$ |
| Alkaline fuel cell (AFC) | KOH solution or anion-exchange membrane | 60–90 °C | Space (Apollo, Space Shuttle); sensitive to $\ce{CO2}$ |
| Phosphoric acid fuel cell (PAFC) | Concentrated $\ce{H3PO4}$ | about 200 °C | Stationary power plants, few new installations now |
| Molten carbonate fuel cell (MCFC) | Molten $\ce{Li2CO3}$–$\ce{K2CO3}$ (conducts $\ce{CO3^2-}$) | about 650 °C | Large power plants, can use natural gas |
| Solid oxide fuel cell (SOFC) | Yttria-stabilized zirconia YSZ (conducts $\ce{O^2-}$) | 600–1000 °C | Combined heat and power; flexible fuel, high efficiency, slow start-up |

The direct methanol fuel cell uses methanol in place of hydrogen: the anode reaction is $\ce{CH3OH + H2O -> CO2 + 6H+ + 6e-}$, the cathode reaction is $\tfrac32\ce{O2 + 6H+ + 6e- -> 3H2O}$, and the overall reaction is $\ce{CH3OH + 3/2O2 -> CO2 + 2H2O}$, with $E^\circ = 1.21\,\mathrm{V}$. Methanol is a liquid and easy to store and transport, but the anode reaction is slow (the intermediate CO poisons Pt, and a Pt–Ru alloy is needed), and methanol also crosses the membrane to the cathode, so the power density is low and it is used only for low-power sources.

### 14.7.5. Bioelectrochemistry

Many reactions in living organisms are electrochemical in nature: in the mitochondrial respiratory chain and in photosynthesis, electrons are passed along a series of redox centers and drive protons across the membrane, and the electrochemical potential gradient thus formed drives the synthesis of ATP (the membrane potential of [6.3.13](/6.3.13)). Electrochemical methods are also used in biological measurement: a blood glucose meter uses a glucose oxidase electrode to measure the current (the limiting current is proportional to the glucose concentration), and ion-selective electrodes measure electrolytes in blood; biofuel cells with enzymes or microorganisms as catalysts are still at the research stage.

## Summary

| Topic | Key points |
|---|---|
| Decomposition voltage | Minimum voltage for sustained electrolysis; measured = theoretical + overpotential + $IR$; for water electrolysis, theoretical 1.23 V, measured about 1.7 V |
| Electrochemical window | Range of potentials within which the electrolyte is neither oxidized nor reduced; LUMO/HOMO; kinetic passivation by the SEI film |
| Overpotential | $\eta = E - E_{\mathrm{eq}}$, positive at the anode and negative at the cathode; concentration, activation and ohmic polarization; measured with a three-electrode cell |
| Exchange current density | Unidirectional current density at equilibrium, $j_0 = Fk^\circ(c^*_{\mathrm{O}})^{\alpha_{\mathrm{a}}}(c^*_{\mathrm{R}})^{\alpha_{\mathrm{c}}}$; at $j = 0$ the Nernst equation is recovered |
| Butler–Volmer | $j = j_0[\mathrm{e}^{\alpha_{\mathrm{a}}F\eta/RT} - \mathrm{e}^{-\alpha_{\mathrm{c}}F\eta/RT}]$; large $\lvert\eta\rvert$: Tafel $\lvert\eta\rvert = a + b\lg\lvert j\rvert$, $b = 2.303RT/(\alpha F) \approx 0.118\,\mathrm{V}$; small $\lvert\eta\rvert$: $R_{\mathrm{ct}} = RT/(Fj_0)$ |
| Hydrogen evolution | Volmer, Tafel and Heyrovsky steps; high-, intermediate- and low-overpotential metals; volcano curve |
| Mass transport | Steady state $\lvert j_{\mathrm{L}}\rvert = zFDc^*/\delta$; $\eta_{\text{conc}} = \frac{RT}{zF}\ln(1 - j/j_{\mathrm{L}})$; potential step: Cottrell $\lvert j\rvert = zFc^*\sqrt{D/(\pi t)}$; polarography: Ilkovič equation |
| Applications of electrolysis | The higher deposition potential deposits first at the cathode; residual concentration fixed by equality of potentials; overpotential exploited in zinc electrowinning, charging and plating; electrosynthesis |
| Corrosion | Hydrogen-evolution and oxygen-absorption corrosion; $E_{\operatorname{Corr}}$ determined by the intersection of the anodic and cathodic polarization curves (Evans diagram); sacrificial anodes, impressed current cathodic protection, anodic protection, inhibitors |
| Electrochemical power sources | Specific capacity $C = zF/(3.6M)\,\mathrm{mA\,h\,g^{-1}}$; intercalation $E = E^\circ - \frac{RT}{F}\ln\frac{x}{1-x} + f(x - \frac12)$, two-phase plateau for $f > 4RT/F$; maximum efficiency of a fuel cell $\Delta_{\mathrm{r}}G/\Delta_{\mathrm{r}}H$ |

## Questions

1. Why does polarization raise the anode potential and lower the cathode potential in both electrolytic and galvanic cells? Why are its effects on the two kinds of device opposite?

   **Answer** For the anode to oxidize at a finite rate it needs $\eta > 0$, and the cathode the opposite. The anode of an electrolytic cell is the positive electrode, so polarization increases the cell voltage; the anode of a galvanic cell is the negative electrode, so polarization decreases the terminal voltage.

2. Why is an electrode with a large exchange current density suitable as a reference electrode?

   **Answer** When a small current passes, its overpotential is very small, its potential is stable, and it is not easily disturbed by reactions of impurities.

3. What can be inferred from Tafel slopes of $b = 0.12\,\mathrm{V}$ and $b = 0.03\,\mathrm{V}$, respectively?

   **Answer** The former corresponds to control by the first electron-transfer step with $\alpha \approx 0.5$; the latter to control by a chemical step following electron transfer (such as the recombination of H), 14.3.5.

4. Why can the diffusion current at a planar electrode in quiescent solution not reach a steady state? Why can the dropping mercury electrode give a steady mean current?

   **Answer** The Cottrell current decays as $t^{-1/2}$ to zero; the dropping mercury electrode renews the surface and the diffusion layer periodically.

5. After the coating is damaged, which rusts more readily, zinc-coated iron or tin-coated iron?

   **Answer** Tin-coated iron: the potential of Sn is higher than that of Fe, so Fe becomes the anode at the damaged spot.

6. Why does $\ce{LiFePO4}$ have a flat discharge plateau, whereas the discharge voltage of $\ce{LiCoO2}$ falls gradually with capacity?

   **Answer** The former is a two-phase reaction with constant chemical potential of the guest; the latter is a solid-solution reaction over most of the range, with the potential varying continuously with $x$, Eq. (14.5).
