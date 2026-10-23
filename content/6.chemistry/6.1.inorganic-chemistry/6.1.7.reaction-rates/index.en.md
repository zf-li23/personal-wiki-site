---
title: Rates of Chemical Reactions
source_hash: 20e1c9b8a7b7
---

The criterion based on the **Gibbs free energy** in the previous chapter ([6.1.6](/6.1.6)) answers the question "can the reaction proceed spontaneously?" but not "how fast does it proceed?" For $\ce{H2(g) + 1/2O2(g) -> H2O(l)}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -237.1\,\mathrm{kJ\,mol^{-1}}$ and the driving force is large, yet a mixture of hydrogen and oxygen can be kept at room temperature for a long time. For $\ce{2NO2(g) -> N2O4(g)}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -4.7\,\mathrm{kJ\,mol^{-1}}$ and the driving force is small, yet the reaction is complete almost instantly. The study of the rates and mechanisms of chemical reactions and of how they depend on concentration, temperature, catalysts, and other conditions is called *chemical kinetics*. Thermodynamics speaks of possibility and kinetics of actuality: whether a thermodynamically allowed reaction takes place in the required time is decided by kinetics.

This chapter first defines the reaction rate and its measurement (7.1). It then uses collision theory and transition state theory to explain the origin of the rate at the molecular level (7.2, drawing on the **Maxwell speed distribution** and the **mean collision frequency** of 5.2), and finally discusses the effects of concentration, temperature, and catalysts (7.3): rate laws and reaction mechanisms, integrated rate laws (first-order **ordinary differential equations**, [2.4](/2.4)) and radiometric dating, the Arrhenius equation and activation energy, and catalysis. The chemical equilibrium of the next chapter ([6.1.8](/6.1.8)) can be regarded as the state in which the forward and reverse reaction rates are equal. This chapter goes only as far as simple reactions and the qualitative transition state theory; the steady-state approximation, opposing, parallel, and consecutive reactions, chain reactions, the quantitative form of transition state theory (the Eyring equation), and the quantitative treatment of surface catalysis and enzyme kinetics are given in [Physical Chemistry](/6.3).

## 7.1. The Concept of Reaction Rate

### 7.1.1. Average Rate and Instantaneous Rate

As a reaction proceeds, the concentrations of the reactants decrease continuously and those of the products increase. The following table gives experimental data for $\ce{2NO2(g) -> 2NO(g) + O2(g)}$ at $300\,^\circ\mathrm{C}$:

| $t/\mathrm{s}$ | 0 | 50 | 100 | 150 | 200 | 250 | 300 | 350 | 400 |
|---|---|---|---|---|---|---|---|---|---|
| $c(\ce{NO2})/(\mathrm{mol\,L^{-1}})$ | 0.0100 | 0.0079 | 0.0065 | 0.0055 | 0.0048 | 0.0043 | 0.0038 | 0.0034 | 0.0031 |
| $c(\ce{NO})/(\mathrm{mol\,L^{-1}})$ | 0 | 0.0021 | 0.0035 | 0.0045 | 0.0052 | 0.0057 | 0.0062 | 0.0066 | 0.0069 |
| $c(\ce{O2})/(\mathrm{mol\,L^{-1}})$ | 0 | 0.0011 | 0.0018 | 0.0023 | 0.0026 | 0.0029 | 0.0031 | 0.0033 | 0.0035 |

Between $t_1$ and $t_2$, the average reaction rate expressed through the change in concentration of $\ce{O2}$ is $\bar v(\ce{O2}) = \frac{c_2(\ce{O2}) - c_1(\ce{O2})}{t_2 - t_1}$. In the same interval the amount of $\ce{NO2}$ consumed is twice the amount of $\ce{O2}$ formed, so the rates of change expressed through different species differ, but after dividing by the coefficients in the equation they are the same:

$$
-\frac{1}{2}\frac{\Delta c(\ce{NO2})}{\Delta t} = \frac{1}{2}\frac{\Delta c(\ce{NO})}{\Delta t} = \frac{\Delta c(\ce{O2})}{\Delta t}.
$$

From the table, $-\frac{1}{2}\frac{\Delta c(\ce{NO2})}{\Delta t}$ in the intervals 0–50 s, 50–100 s, 100–150 s, 150–200 s, and 200–250 s is $2.1$, $1.4$, $1.0$, $0.7$, and $0.5$ (in units of $10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}}$): the average rate decreases as the reactants are consumed, the intervals are not equal, and the average rate is only a rough description of a period of time.

**Definition 7.1.1** The limit of the average reaction rate as the time interval $\Delta t \to 0$ is called the **instantaneous rate**, that is, the derivative of the concentration with respect to time (divided by the coefficient). On a $c$–$t$ curve it is the absolute value of the slope of the tangent at that moment (divided by the coefficient).

### 7.1.2. Reaction Rate Defined by the Extent of Reaction

For a general reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ (the **stoichiometric number** $\nu_{\mathrm{B}}$ is negative for reactants and positive for products, [6.1.6](/6.1.6)), the change in the amount of substance satisfies $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$, where $\xi$ is the **extent of reaction**. The rate of change of the extent of reaction is therefore independent of the choice of species.

**Definition 7.1.2 (Reaction Rate)** In a constant-volume reaction system, the rate of change of the extent of reaction per unit volume,

$$
v = \frac{1}{V}\frac{\mathrm{d}\xi}{\mathrm{d}t} = \frac{1}{\nu_{\mathrm{B}}}\frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}t}
$$
is called the (chemical) **rate of reaction**, commonly in units of $\mathrm{mol\,L^{-1}\,s^{-1}}$ or $\mathrm{mol\,L^{-1}\,min^{-1}}$. For $a\mathrm{A} + b\mathrm{B} \to y\mathrm{Y} + z\mathrm{Z}$,

$$
v = -\frac{1}{a}\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = -\frac{1}{b}\frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}t} = \frac{1}{y}\frac{\mathrm{d}c_{\mathrm{Y}}}{\mathrm{d}t} = \frac{1}{z}\frac{\mathrm{d}c_{\mathrm{Z}}}{\mathrm{d}t}.
$$

A reaction has only one rate at a given moment, but its value depends on how the equation is written (multiplying the equation by 2 halves $v$). For a single species, $-\mathrm{d}c_{\mathrm{A}}/\mathrm{d}t$ is called the rate of consumption of A and $\mathrm{d}c_{\mathrm{Y}}/\mathrm{d}t$ the rate of formation of Y; they equal $|\nu_{\mathrm{B}}|v$.

### 7.1.3. Measurement of Reaction Rates

Measuring a reaction rate means measuring a set of $c$–$t$ data: samples are taken and analyzed at different times (chemical methods), or a physical quantity proportional to the concentration (pressure, absorbance, conductivity, optical rotation, and so on) is monitored continuously (physical methods, which do not disturb the reaction). On a $c$–$t$ curve, the slope of the tangent at a given moment divided by the coefficient is the instantaneous rate at that moment.

**Example 7.1.1** The experimental data for $\ce{2N2O5 -> 4NO2 + O2(g)}$ in $\ce{CCl4}$ solvent at $40.00\,^\circ\mathrm{C}$ are given below. Find (1) the average reaction rate between 0 and 2400 s and (2) the instantaneous rate at $t = 2700\,\mathrm{s}$.

| $t/\mathrm{s}$ | 0 | 300 | 600 | 900 | 1200 | 1800 | 2400 | 3000 |
|---|---|---|---|---|---|---|---|---|
| $c(\ce{N2O5})/(\mathrm{mol\,L^{-1}})$ | 0.200 | 0.180 | 0.161 | 0.144 | 0.130 | 0.104 | 0.084 | 0.068 |

Solution. (1) $\bar v = -\frac{1}{2}\frac{0.084 - 0.200}{2400 - 0}\,\mathrm{mol\,L^{-1}\,s^{-1}} = 2.42 \times 10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}}$.

(2) Plot $c(\ce{N2O5})$ against $t$ and draw the tangent at $t = 2700\,\mathrm{s}$. A tangent drawn by hand meets the vertical axis at about $0.144$ and the horizontal axis at about $5580\,\mathrm{s}$, so the slope is $\frac{\mathrm{d}c(\ce{N2O5})}{\mathrm{d}t} \approx -\frac{0.144}{5580}\,\mathrm{mol\,L^{-1}\,s^{-1}} = -2.58 \times 10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}}$ and

$$
v = -\frac{1}{2}\frac{\mathrm{d}c(\ce{N2O5})}{\mathrm{d}t} \approx 1.29 \times 10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}},
$$
of the same order of magnitude as the average rate in (1). A tangent drawn by hand has a large error; a more reliable procedure is to determine the form of the rate law first and then fit the whole data set (7.3.2). The curve in the figure below is the fit for a first-order reaction, and the slope of the tangent obtained from it is $-2.72 \times 10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}}$.

![Left: concentration–time data for the decomposition of N₂O₅ in CCl₄, the first-order fit, and the tangent at t = 2700 s; right: least-squares line of ln c against t, whose slope gives the rate constant](./plots/n2o5-decay.py)

## 7.2. Theories of Reaction Rates

Why are some reactions fast and others slow? Take the reaction that removes pollutants from automobile exhaust, $\ce{CO(g) + NO(g) -> CO2(g) + 1/2N2(g)}$: $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} \approx -345\,\mathrm{kJ\,mol^{-1}}$ is thermodynamically very favorable, but the rate is very small without a catalyst. For the aging of rubber and the spoiling of food, on the other hand, we want to slow things down. To control a rate, we must first understand it at the molecular level.

### 7.2.1. Collision Theory

*Collision theory* regards a gas-phase bimolecular reaction as a collision between molecules: the reactant molecules must meet in order to react, but not every collision leads to reaction. It writes the reaction rate as a product of three factors.

(1) Collision frequency. Treat the molecules as hard spheres of diameters $d_{\mathrm{A}}$ and $d_{\mathrm{B}}$; they collide when their centers come within $d_{\mathrm{AB}} = \frac{1}{2}(d_{\mathrm{A}} + d_{\mathrm{B}})$ of each other, and the **collision cross section** is $\sigma = \pi d_{\mathrm{AB}}^2$. By the same method as for the **mean collision frequency** of one molecule in [5.2.2](/5.2.2#def-2.3.1), an A molecule collides with B molecules $\sigma\bar v_{\mathrm{rel}}n_{\mathrm{B}}$ times per unit time, so the total number of A–B collisions per unit volume and unit time is

$$
Z_{\mathrm{AB}} = \sigma\bar v_{\mathrm{rel}}\,n_{\mathrm{A}}n_{\mathrm{B}}, \qquad \bar v_{\mathrm{rel}} = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}},
$$
where $n_{\mathrm{A}}, n_{\mathrm{B}}$ are number densities. The relative motion of two molecules is equivalent to the motion of a single particle whose mass is the **reduced mass** $\mu = \frac{m_{\mathrm{A}}m_{\mathrm{B}}}{m_{\mathrm{A}} + m_{\mathrm{B}}}$, and replacing $m$ by $\mu$ in the **Maxwell speed distribution** ([5.2.1](/5.2.1#thm-1.5.1)) gives the mean relative speed $\bar v_{\mathrm{rel}}$. For collisions between like molecules, to avoid counting each collision twice, $Z_{\mathrm{AA}} = \frac{1}{2}\sigma\bar v_{\mathrm{rel}}n_{\mathrm{A}}^2$ and $\mu = m/2$. The collision frequency is proportional to the product of the concentrations, which is why the rate increases with concentration.

(2) Energy factor. Only collisions with a sufficiently large relative kinetic energy along the line of centers can overcome the repulsion between the nuclei and between the electrons, break the old bonds, and form the new ones.

**Definition 7.2.1** A collision that leads to reaction is called an **effective collision**. Collision theory assumes that only a collision whose relative translational energy along the line of centers is no less than a critical value $E_{\mathrm{c}}$ (per mole) can be effective; a molecule whose energy meets this requirement is called an **activated molecule**, and the energy required to turn ordinary molecules into activated molecules is called the **activation energy**, denoted $E_{\mathrm{a}}$. Its exact definition and physical meaning are given in 7.3.3.

From the **Boltzmann distribution** one can calculate (the derivation is in [Physical Chemistry](/6.3)) that the fraction of collisions whose relative kinetic energy along the line of centers is no less than $E_{\mathrm{c}}$ is exactly the **Boltzmann factor** $f = \mathrm{e}^{-E_{\mathrm{c}}/RT}$ (with $k_{\mathrm{B}}$ replaced by $R$ for molar quantities).

(3) Steric factor. Sufficient energy is still not enough; the molecules must also meet in a favorable orientation. In $\ce{NO2 + CO -> NO + CO2}$, an O atom can be transferred only when the C end of $\ce{CO}$ strikes an O atom of $\ce{NO2}$; in the gas-phase reaction of $\ce{HCl}$ with $\ce{NH3}$, the H end of $\ce{HCl}$ can approach the lone pair on N only through a narrow "window".

**Definition 7.2.2** The ratio of the number of effective collisions to the number of collisions with sufficient energy is called the **steric factor** (probability factor), denoted $P$, with $0 < P \le 1$.

For atoms and small molecules of simple structure $P$ is close to 1, and for molecules of complex structure it can be as small as $10^{-3}$–$10^{-6}$.

Together, the three factors give the number of reactions per unit volume and unit time, $PZ_{\mathrm{AB}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$. Converting number density to concentration, $n = N_{\mathrm{A}}c$, and dividing by $N_{\mathrm{A}}$ to convert to amount of substance,

$$
v = P\sigma\bar v_{\mathrm{rel}}N_{\mathrm{A}}\,\mathrm{e}^{-E_{\mathrm{c}}/RT}\,c_{\mathrm{A}}c_{\mathrm{B}} = k\,c_{\mathrm{A}}c_{\mathrm{B}}, \qquad k = P\sigma\bar v_{\mathrm{rel}}N_{\mathrm{A}}\,\mathrm{e}^{-E_{\mathrm{c}}/RT}.
$$

Collision theory thus predicts that the rate of a bimolecular reaction is proportional to the product of the concentrations of the two reactants (the law of mass action of 7.3.1) and that the rate constant increases approximately exponentially with temperature (the Arrhenius equation of 7.3.3).

**Example 7.2.1 (Order of Magnitude)** For $\ce{2HI(g) -> H2(g) + I2(g)}$ at $973\,\mathrm{K}$, $c(\ce{HI}) = 1.0 \times 10^{-3}\,\mathrm{mol\,L^{-1}}$, that is, $n = 6.0 \times 10^{23}\,\mathrm{m^{-3}}$. Take the collision diameter of $\ce{HI}$ as $d \approx 0.35\,\mathrm{nm}$ and $\mu = m(\ce{HI})/2$; then $\bar v_{\mathrm{rel}} \approx 570\,\mathrm{m\,s^{-1}}$ and $Z_{\mathrm{AA}} \approx 4 \times 10^{31}\,\mathrm{m^{-3}\,s^{-1}} = 4 \times 10^{28}\,\mathrm{L^{-1}\,s^{-1}}$. If every collision led to reaction, $v = Z_{\mathrm{AA}}/N_{\mathrm{A}} \approx 6 \times 10^4\,\mathrm{mol\,L^{-1}\,s^{-1}}$, and $10^{-3}\,\mathrm{mol\,L^{-1}}$ of $\ce{HI}$ would decompose completely in less than $10^{-7}\,\mathrm{s}$, which is clearly contrary to fact. The activation energy of this reaction is about $184\,\mathrm{kJ\,mol^{-1}}$, and the energy factor is $\mathrm{e}^{-184100/(8.314 \times 973)} \approx 1.3 \times 10^{-10}$: the great majority of collisions are ineffective, and the rate falls to the order of $10^{-5}\,\mathrm{mol\,L^{-1}\,s^{-1}}$.

Collision theory is intuitive, but neither $E_{\mathrm{c}}$ nor $P$ can be calculated from the theory; both must be determined by experiment. Nor does it say how the chemical bonds change in the course of the reaction.

### 7.2.2. Transition State Theory

*Transition state theory* looks at a reaction from the change in potential energy within the molecular system. Take $\ce{A + B-C -> A-B + C}$: as A approaches B–C, the A–B bond gradually forms and the B–C bond gradually weakens, and the potential energy of the system first rises. It is highest at the configuration $\mathrm{A\cdots B\cdots C}$; thereafter the A–B bond continues to form and the potential energy falls to the level of the products. Plotting the potential energy against a variable representing the progress of the reaction gives the potential energy diagram of the reaction.

**Definition 7.2.3** The progress variable that describes the conversion of reactants into products along the path of lowest energy is called the **reaction coordinate**. The atomic configuration at the highest potential energy along the reaction coordinate is called the **transition state** (also the activated complex), denoted $\ddagger$; it is a maximum on the potential energy surface along the reaction coordinate but a minimum in all other directions (a saddle point), and its lifetime is only that of a molecular vibration (about $10^{-13}\,\mathrm{s}$). The species corresponding to a potential energy minimum between two transition states on the path of a complex reaction is called a **reaction intermediate**; it has a definite structure and a finite lifetime and can sometimes be detected or even isolated.

The basic picture of transition state theory is the following:

1. Reactant molecules acquire energy through collisions, the kinetic energy of the molecules is converted into potential energy of the system, and the transition state forms.
2. In the transition state the old bonds are partly broken and the new bonds partly formed; it is extremely unstable and can decompose either into products or back into reactants.
3. The reaction rate depends on the concentration of the transition state and on the rate at which it crosses the energy barrier and decomposes into products.

![Left: potential energy diagram of a one-step elementary reaction, with the activation energies of the forward and reverse reactions and the reaction enthalpy marked, and the dashed line showing the path with the lower barrier produced by a catalyst; right: a two-step reaction through an intermediate, where the second transition state is the highest and the second step is rate-determining](./plots/potential-energy-diagram.py)

On the potential energy diagram, the activation energy $E_{\mathrm{a}}$ of the forward reaction is the potential energy difference between the transition state and the reactants, and the activation energy $E_{\mathrm{a}}'$ of the reverse reaction is that between the transition state and the products. The forward and reverse reactions pass through the same transition state, so the difference between the two is approximately the **molar enthalpy of reaction**:

$$
\Delta_{\mathrm{r}}H_{\mathrm{m}} \approx E_{\mathrm{a}} - E_{\mathrm{a}}'.
$$

$\Delta_{\mathrm{r}}H_{\mathrm{m}} < 0$ is an exothermic reaction and $\Delta_{\mathrm{r}}H_{\mathrm{m}} > 0$ an endothermic one. Since $E_{\mathrm{a}}' \ge 0$, the activation energy of an endothermic reaction is at least equal to its reaction enthalpy. The reaction rate depends on the height of the energy barrier and not on the height difference between the reactant and product valleys; the latter determines the equilibrium ([6.1.8](/6.1.8)).

There are three outcomes of a collision: molecules without activation collide, have insufficient energy, and return to the valley; activated molecules collide in an unfavorable orientation and deviate from the reaction path; activated molecules collide in a favorable orientation, cross the barrier, and form products.

## 7.3. Factors Affecting the Rate of Reaction

The reaction rate depends first of all on the nature of the reactants themselves (internal factors: bond strengths and molecular structure). The main external factors are concentration, temperature, catalysts, and, for heterogeneous reactions, the contact area. White phosphorus oxidizes slowly in air and burns violently in pure oxygen; this is the effect of concentration: the higher the concentration of the reactants, the more frequent the collisions.

### 7.3.1. Concentration: Rate Laws and Reaction Mechanisms

In the data for $\ce{N2O5(g) -> 2NO2(g) + 1/2O2(g)}$, the ratio of the reaction rate to $c(\ce{N2O5})$ stays constant at all times:

| $t/\mathrm{min}$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $c(\ce{N2O5})/(\mathrm{mol\,L^{-1}})$ | 0.160 | 0.113 | 0.080 | 0.056 | 0.040 |
| $v/(\mathrm{mol\,L^{-1}\,min^{-1}})$ | 0.056 | 0.039 | 0.028 | 0.020 | 0.014 |

That is, $v = k\,c(\ce{N2O5})$ with $k \approx 0.35\,\mathrm{min^{-1}}$.

**Definition 7.3.1 (Rate Law)** An expression that relates the reaction rate to the concentrations at a given temperature is called a **rate law**. The rate law of many reactions has the power-law form

$$
v = k\,c_{\mathrm{A}}^{\alpha}c_{\mathrm{B}}^{\beta}\cdots,
$$
The proportionality coefficient $k$ is called the **rate constant**, the reaction rate when all concentrations are unity (also the specific rate); the exponents $\alpha$ and $\beta$ are called the **order of reaction** with respect to A and B (partial orders), and $n = \alpha + \beta + \cdots$ is called the overall order of the reaction.

Notes on rate laws:

1. The order is in general not equal to the coefficient in the equation; it may be positive, negative, an integer, or a fraction, and must be determined by experiment. Reactions of the same form can have quite different rate laws: $v = kc(\ce{H2})c(\ce{I2})$ for $\ce{H2 + I2 -> 2HI}$, $v = kc(\ce{H2})c(\ce{Cl2})^{1/2}$ for $\ce{H2 + Cl2 -> 2HCl}$ (a chain reaction), and the rate law of $\ce{H2 + Br2 -> 2HBr}$ is not even of power-law form.
2. The concentration terms in a rate law may include products or catalysts (for example, the decomposition of $\ce{O3}$ in this section is of order $-1$ in $\ce{O2}$).
3. $k$ reflects the internal factors of the reaction and is independent of concentration, but varies with temperature (7.3.3).
4. The unit of $k$ depends on the overall order so that $v$ has the unit $\mathrm{mol\,L^{-1}\,s^{-1}}$:

| Overall order | Rate law | Unit of $k$ |
|---|---|---|
| 0 | $v = k$ | $\mathrm{mol\,L^{-1}\,s^{-1}}$ |
| 1 | $v = kc_{\mathrm{A}}$ | $\mathrm{s^{-1}}$ |
| 2 | $v = kc_{\mathrm{A}}^2$ or $kc_{\mathrm{A}}c_{\mathrm{B}}$ | $\mathrm{L\,mol^{-1}\,s^{-1}}$ |
| 3 | $v = kc_{\mathrm{A}}^2c_{\mathrm{B}}$, etc. | $\mathrm{L^2\,mol^{-2}\,s^{-1}}$ |

The overall order of a reaction can be read from the unit of $k$.

The most direct way to determine the rate law is the *method of initial rates*: prepare a series of reaction mixtures with different initial compositions, change the concentration of only one reactant while keeping the others fixed, and measure the instantaneous rate at $t = 0$ (the initial rate). At the initial moment the product concentrations are zero, the reverse and side reactions can be neglected, and the concentrations are the known prepared values.

**Example 7.3.1** The initial rates of $\ce{2NO(g) + 2H2(g) -> N2(g) + 2H2O(g)}$ were measured at $1073\,\mathrm{K}$:

| Experiment | $c_0(\ce{H2})/(\mathrm{mol\,L^{-1}})$ | $c_0(\ce{NO})/(\mathrm{mol\,L^{-1}})$ | $v_0/(\mathrm{mol\,L^{-1}\,s^{-1}})$ |
|---|---|---|---|
| 1 | 0.0060 | 0.0010 | $7.9 \times 10^{-7}$ |
| 2 | 0.0060 | 0.0020 | $3.2 \times 10^{-6}$ |
| 3 | 0.0060 | 0.0040 | $1.3 \times 10^{-5}$ |
| 4 | 0.0030 | 0.0040 | $6.4 \times 10^{-6}$ |
| 5 | 0.0015 | 0.0040 | $3.2 \times 10^{-6}$ |

Find the rate law and the rate constant.

Solution. Let $v_0 = k\,c_0(\ce{NO})^{\alpha}c_0(\ce{H2})^{\beta}$. In experiments 1–3, $c_0(\ce{H2})$ is constant and each doubling of $c_0(\ce{NO})$ increases $v_0$ by a factor of 4: $\alpha = \log_2\frac{3.2 \times 10^{-6}}{7.9 \times 10^{-7}} \approx 2$. In experiments 3–5, $c_0(\ce{NO})$ is constant and each halving of $c_0(\ce{H2})$ also halves $v_0$: $\beta = 1$. Hence $v = k\,c(\ce{NO})^2c(\ce{H2})$ and the overall order is 3. Substituting the data of experiment 1,

$$
k = \frac{7.9 \times 10^{-7}}{(0.0010)^2 \times 0.0060}\,\mathrm{L^2\,mol^{-2}\,s^{-1}} = 1.3 \times 10^2\,\mathrm{L^2\,mol^{-2}\,s^{-1}}.
$$
That the reaction is first order in $\ce{H2}$ rather than second order as in the equation shows that it does not take place in one step.

Collision theory describes reactions that take place in one step. The experimental rate law often does not correspond to the equation, because most reactions proceed in several steps.

**Definition 7.3.2** A reaction in which reactant particles (molecules, atoms, ions, or radicals) are converted directly into products in a single effective collision is called an **elementary reaction** (elementary step), such as $\ce{NO2 + CO -> NO + CO2}$ and $\ce{2NO2 -> 2NO + O2}$. A reaction consisting of two or more elementary reactions is called a **complex reaction** (nonelementary reaction); the series of elementary reactions that make up a complex reaction is called its **reaction mechanism**.

If the forward reaction is elementary, the reverse reaction is also elementary and passes through the same transition state (the principle of microscopic reversibility).

**Theorem 7.3.1 (Law of Mass Action)** The rate of an elementary reaction $a\mathrm{A} + b\mathrm{B} \to$ products is proportional to the product of the concentrations of the reactants, each raised to the power of its coefficient:

$$
v = k\,c_{\mathrm{A}}^{a}c_{\mathrm{B}}^{b}.
$$

This is precisely the conclusion of collision theory: for a bimolecular reaction in one step the rate is proportional to the collision frequency of the two kinds of molecules, that is, to $c_{\mathrm{A}}c_{\mathrm{B}}$. The Norwegian chemists Guldberg and Waage first proposed the concept of "mass action" in 1864–1867 (then for chemical equilibrium), and van 't Hoff gave its kinetic form in 1884. The law of mass action applies only to elementary reactions; for a complex reaction the rate law cannot be written down directly from the overall equation.

**Definition 7.3.3** The number of particles that collide simultaneously and react in an elementary reaction is called its **molecularity**. According to molecularity, elementary reactions are unimolecular (such as $\ce{SO2Cl2 -> SO2 + Cl2}$), bimolecular (such as $\ce{NO2 + CO -> NO + CO2}$), or termolecular (such as $\ce{H2 + I + I -> 2HI}$ and $\ce{HOBr + H+ + Br- -> H2O + Br2}$).

The probability of three particles colliding at once is already very small, and no elementary reactions of four or more molecules have been found. Molecularity is a microscopic description of the mechanism, meaningful only for elementary reactions, with values 1, 2, or 3; the order of reaction is a macroscopic experimental quantity, and every reaction with a rate law of power-law form has an order. For an elementary reaction the two are numerically equal; conversely, agreement of the measured order with the coefficients does not prove that a reaction is elementary ($\ce{H2 + I2 -> 2HI}$ is an example, see below).

**Example 7.3.2** Write the rate laws of the following elementary reactions and state their orders and molecularities: (1) $\ce{SO2Cl2 -> SO2 + Cl2}$; (2) $\ce{NO2 + CO -> NO + CO2}$; (3) $\ce{2NO2 -> 2NO + O2}$.

Solution. (1) $v = kc(\ce{SO2Cl2})$, first order, unimolecular; (2) $v = kc(\ce{NO2})c(\ce{CO})$, second order, bimolecular; (3) $v = kc(\ce{NO2})^2$, second order, bimolecular.

When a complex reaction consists of elementary steps in series and one step is much slower than the others, the overall rate is approximately equal to the rate of this step. This step is called the *rate-determining step* (also the rate-limiting step), and on the potential energy diagram it corresponds to the highest transition state. The fast steps before the rate-determining step are often reversible and much faster than the rate-determining step in both directions, so they remain approximately at equilibrium; expressing the concentration of the intermediate in the rate-determining step through the equilibrium relation gives the rate law of the overall reaction. This treatment is called the *pre-equilibrium approximation*.

**Example 7.3.3** The mechanism of $\ce{H2 + I2 -> 2HI}$ is believed to be

1. $\ce{I2 <=> 2I}$ (fast, with rate constants $k_1$ and $k_{-1}$ for the forward and reverse reactions);
2. $\ce{H2 + 2I -> 2HI}$ (slow, rate constant $k_2$).

Find the rate law.

Solution. The overall rate equals the rate of the rate-determining step (2), and by the law of mass action $v = k_2c(\ce{H2})c(\ce{I})^2$. The concentration of the intermediate I atoms is unknown, but both the forward and reverse reactions of step (1) are much faster than step (2) and are approximately at equilibrium: $k_1c(\ce{I2}) = k_{-1}c(\ce{I})^2$, that is,

$$
c(\ce{I})^2 = \frac{k_1}{k_{-1}}c(\ce{I2}).
$$
Substitution gives

$$
v = \frac{k_1k_2}{k_{-1}}c(\ce{H2})c(\ce{I2}) = k\,c(\ce{H2})c(\ce{I2}), \qquad k = \frac{k_1k_2}{k_{-1}}.
$$
This agrees with the experimental rate law. The approximation holds if the recombination of I atoms (the $k_{-1}$ step) is much faster than their consumption by $\ce{H2}$ (the $k_2$ step), that is, $k_{-1} \gg k_2c(\ce{H2})$. From $k = k_1k_2/k_{-1}$ and the Arrhenius equation of 7.3.3, the apparent activation energy is $E_{\mathrm{a}} = E_{\mathrm{a},1} + E_{\mathrm{a},2} - E_{\mathrm{a},-1}$.

$\ce{H2 + I2}$ was long regarded as the classic bimolecular elementary reaction (Bodenstein, 1890s), and only photochemical experiments in the 1960s showed that I atoms take part. This shows that the rate law is only a necessary condition for testing a mechanism: if the rate law derived from a mechanism disagrees with experiment, the mechanism must be wrong; if it agrees, the mechanism is only possibly correct.

**Example 7.3.4** The mechanism of the decomposition of ozone, $\ce{2O3 -> 3O2}$, is

1. $\ce{O3 <=> O2 + O}$ (fast, rate constants $k_1$ and $k_{-1}$);
2. $\ce{O + O3 -> 2O2}$ (slow, rate constant $k_2$).

Which of the following rate laws is consistent with this mechanism? (a) $kc(\ce{O3})^2$; (b) $kc(\ce{O3})c(\ce{O})$; (c) $kc(\ce{O3})^2c(\ce{O2})$; (d) $kc(\ce{O3})^2c(\ce{O2})^{-1}$.

Solution. The rate-determining step gives $v = k_2c(\ce{O})c(\ce{O3})$. From the pre-equilibrium $K_1 = \frac{k_1}{k_{-1}} = \frac{c(\ce{O2})c(\ce{O})}{c(\ce{O3})}$ we get $c(\ce{O}) = K_1\frac{c(\ce{O3})}{c(\ce{O2})}$, so

$$
v = k_2K_1\frac{c(\ce{O3})^2}{c(\ce{O2})},
$$
and the answer is (d). Rate law (b) contains the concentration of the intermediate O, which cannot be tested directly by experiment. The product $\ce{O2}$ appears in the denominator: it shifts the pre-equilibrium to the left and lowers the concentration of O atoms, so $\ce{O2}$ inhibits the decomposition of ozone.

**Example 7.3.5** The experimental rate law of $\ce{C2H4Br2 + 3KI -> C2H4 + 2KBr + KI3}$ is $v = kc(\ce{C2H4Br2})c(\ce{KI})$. $\ce{K+}$ does not take part, and the ionic equation is $\ce{C2H4Br2 + 3I- -> C2H4 + 2Br- + I3-}$. A mechanism consistent with experiment is

1. $\ce{C2H4Br2 + I- -> C2H4 + IBr + Br-}$ (slow);
2. $\ce{IBr + I- -> I2 + Br-}$ (fast);
3. $\ce{I2 + I- -> I3-}$ (fast).

Adding the three steps gives the overall reaction; the rate-determining step (1) is a bimolecular elementary reaction and gives $v = kc(\ce{C2H4Br2})c(\ce{I-})$, in agreement with experiment. The coefficient of $\ce{I-}$ in the overall reaction is 3, yet the rate law is only first order in it: fast steps after the rate-determining step do not affect the rate.

The pre-equilibrium approximation and the more general steady-state approximation both exploit the great disparity between the time scales of fast and slow steps to eliminate the intermediates. The same disparity makes the system of differential equations for such mechanisms a **stiffness** problem, so direct numerical integration requires implicit methods ([4.4.4](/4.4.4#sec-4.3.3)). The steady-state approximation and the general treatment of consecutive, parallel, and opposing reactions are given in [Physical Chemistry](/6.3).

### 7.3.2. Concentration as a Function of Time

A rate law relates concentration to rate (the differential form); in practice we more often need concentration as a function of time, that is, we integrate the rate law as an ordinary differential equation for $c(t)$. This section treats reactions with a single reactant A and a rate law $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = k_{\mathrm{A}}c_{\mathrm{A}}^n$ (for $a\mathrm{A} \to$ products, $k_{\mathrm{A}} = ak$ by Definition 7.1.2; for $a = 1$ the two are the same, and below we write simply $k$). Denote the initial concentration by $c_{\mathrm{A},0}$.

**Definition 7.3.4** The time required for the concentration of a reactant to fall to half its initial value is called the **half-life** of the reaction, denoted $t_{1/2}$. Reactions of overall order 0, 1, and 2 are called **zeroth-order**, **first-order**, and **second-order reactions**, respectively.

**Formula 7.3.1 (First-Order Reaction)** $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = kc_{\mathrm{A}}$ is a **separable equation** ([2.4.3](/2.4.3#sec-3.1)): $\frac{\mathrm{d}c_{\mathrm{A}}}{c_{\mathrm{A}}} = -k\,\mathrm{d}t$, and integrating from $0$ to $t$ gives

$$
\ln\frac{c_{\mathrm{A}}}{c_{\mathrm{A},0}} = -kt, \qquad c_{\mathrm{A}} = c_{\mathrm{A},0}\mathrm{e}^{-kt}, \qquad t_{1/2} = \frac{\ln 2}{k} \approx \frac{0.693}{k}.
$$

$\ln c_{\mathrm{A}}$ is linear in $t$ with slope $-k$. The half-life of a first-order reaction is independent of the initial concentration: whatever the starting amount, half remains after each $t_{1/2}$. The unit of $k$ is an inverse time, and $1/k$ is called the time constant (lifetime). Common first-order reactions include radioactive decay, the decay of excited molecules, many decomposition reactions (such as that of $\ce{N2O5}$), and the acid-catalyzed hydrolysis of sucrose (with water in large excess, apparently first order).

**Formula 7.3.2 (Second-Order Reaction)** $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = kc_{\mathrm{A}}^2$; separating variables and integrating gives

$$
\frac{1}{c_{\mathrm{A}}} - \frac{1}{c_{\mathrm{A},0}} = kt, \qquad t_{1/2} = \frac{1}{kc_{\mathrm{A},0}}.
$$

**Formula 7.3.3 (Zeroth-Order Reaction)** $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = k$; integrating gives $c_{\mathrm{A}} = c_{\mathrm{A},0} - kt$ ($t \le c_{\mathrm{A},0}/k$) and $t_{1/2} = \frac{c_{\mathrm{A},0}}{2k}$. Zeroth-order reactions mostly occur on catalyst surfaces: when the surface is saturated with reactant, the rate depends only on the number of active sites and not on the gas-phase concentration. Enzymes in the presence of excess substrate (7.3.4) and the metabolism of ethanol in the human body are also approximately zeroth order.

| Order | Integrated law | Linear plot | Slope | $t_{1/2}$ | Unit of $k$ |
|---|---|---|---|---|---|
| 0 | $c_{\mathrm{A}} = c_{\mathrm{A},0} - kt$ | $c_{\mathrm{A}}$–$t$ | $-k$ | $\frac{c_{\mathrm{A},0}}{2k}$ | $\mathrm{mol\,L^{-1}\,s^{-1}}$ |
| 1 | $\ln c_{\mathrm{A}} = \ln c_{\mathrm{A},0} - kt$ | $\ln c_{\mathrm{A}}$–$t$ | $-k$ | $\frac{\ln 2}{k}$ | $\mathrm{s^{-1}}$ |
| 2 | $\frac{1}{c_{\mathrm{A}}} = \frac{1}{c_{\mathrm{A},0}} + kt$ | $\frac{1}{c_{\mathrm{A}}}$–$t$ | $k$ | $\frac{1}{kc_{\mathrm{A},0}}$ | $\mathrm{L\,mol^{-1}\,s^{-1}}$ |

This table gives a graphical method for determining the order from $c$–$t$ data: plot $c$, $\ln c$, and $1/c$ against $t$; whichever is a straight line indicates the corresponding order, and the slope of the line gives $k$. The dependence of the half-life on the initial concentration is also different in the three cases (proportional to $c_0$, independent of it, inversely proportional to it), so whether successive half-lives are equal can also be used to determine the order.

![Concentration–time curves for zeroth-, first-, and second-order reactions with the same initial concentration and initial rate (dashed line: half the initial concentration), and the three linearized plots](./plots/integrated-rate-laws.py)

**Example 7.3.6 (Rate Constant by Least Squares)** Plotting $\ln c(\ce{N2O5})$ against $t$ for the data of Example 7.1.1, the eight points lie almost on a straight line, so the decomposition of $\ce{N2O5}$ in $\ce{CCl4}$ is first order. Fitting the line $\ln c = \ln c_0 - k_{\ce{N2O5}}t$ by **least squares** (the **simple linear regression model**, [3.3.2](/3.3.2#sec-2.2)) gives $k_{\ce{N2O5}} = (3.61 \pm 0.01) \times 10^{-4}\,\mathrm{s^{-1}}$ (the value after $\pm$ is the standard error), and the rate constant of Definition 7.1.2 is $k = k_{\ce{N2O5}}/2$. This is much more reliable than drawing a tangent by hand on the curve, since the whole data set takes part in the estimate. The fit is done on the logarithmic scale, which implicitly assumes that the relative errors of the concentrations are roughly equal. Interpolating the activation energy found in Example 7.3.10 from the rate constants at $25\,^\circ\mathrm{C}$ and $45\,^\circ\mathrm{C}$ to $40\,^\circ\mathrm{C}$ gives $3.4 \times 10^{-4}\,\mathrm{s^{-1}}$, in agreement with the fitted value.

```python
import numpy as np

t = np.array([0, 300, 600, 900, 1200, 1800, 2400, 3000])   # s
c = np.array([0.200, 0.180, 0.161, 0.144, 0.130, 0.104, 0.084, 0.068])   # mol/L
slope, intercept = np.polyfit(t, np.log(c), 1)
print(-slope)   # 3.61e-04 s^-1
```

The decay of radioactive nuclides is a strictly first-order process: the probability per unit time that each nucleus decays is a constant $k$ (the decay constant), independent of the "age" of the nucleus, so the lifetime of a single nucleus follows an **exponential distribution** ([3.1.4](/3.1.4#def-4.2.3)), which is its **memorylessness**; the number $N$ of a large number of nuclei satisfies $\frac{\mathrm{d}N}{\mathrm{d}t} = -kN$ and $N = N_0\mathrm{e}^{-kt}$. The decay constant is almost unaffected by temperature, pressure, and chemical state, so radioactive nuclides are natural "clocks". The method of estimating the age of a sample from the present amount of a radioactive nuclide in it and the amount of its decay product is called *radiometric dating*:

$$
t = \frac{1}{k}\ln\frac{N_0}{N} = \frac{t_{1/2}}{\ln 2}\ln\frac{N_0}{N}.
$$

| Nuclide | Half-life | Nuclide | Half-life |
|---|---|---|---|
| $^{238}\mathrm{U}$ | $4.47 \times 10^9\,\mathrm{a}$ | $^{239}\mathrm{Pu}$ | $2.41 \times 10^4\,\mathrm{a}$ |
| $^{235}\mathrm{U}$ | $7.04 \times 10^8\,\mathrm{a}$ | $^{137}\mathrm{Cs}$ | $30.1\,\mathrm{a}$ |
| $^{232}\mathrm{Th}$ | $1.40 \times 10^{10}\,\mathrm{a}$ | $^{90}\mathrm{Sr}$ | $28.8\,\mathrm{a}$ |
| $^{40}\mathrm{K}$ | $1.25 \times 10^9\,\mathrm{a}$ | $^{131}\mathrm{I}$ | $8.02\,\mathrm{d}$ |
| $^{14}\mathrm{C}$ | $5.70 \times 10^3\,\mathrm{a}$ | | |

The left columns are naturally occurring radionuclides and the right columns are artificial nuclides (fission products and reactor products).

Radiocarbon dating. Neutrons produced by cosmic rays react with $^{14}\mathrm{N}$ in the upper atmosphere, $\ce{^{14}_{7}N + ^{1}_{0}n -> ^{14}_{6}C + ^{1}_{1}H}$, and $^{14}\mathrm{C}$ returns to $^{14}\mathrm{N}$ by $\beta^-$ decay. Production and decay keep the abundance of $^{14}\mathrm{C}$ in atmospheric $\ce{CO2}$ approximately constant. Plants take up carbon through photosynthesis and animals through the food chain, so the $^{14}\mathrm{C}/^{12}\mathrm{C}$ ratio in living organisms is the same as in the atmosphere; after death no more is replenished and $^{14}\mathrm{C}$ decays with $t_{1/2} \approx 5700\,\mathrm{a}$, so measuring the remaining fraction gives the time of death, applicable to samples up to about 50 000 years old. Libby established the method around 1949 and received the Nobel Prize in Chemistry in 1960. Because the atmospheric $^{14}\mathrm{C}$ abundance was not strictly constant historically (nor in the twentieth century, with the burning of fossil fuels and nuclear tests), accurate ages require conversion with a calibration curve built from independently dated samples such as tree rings. Older rocks are dated with long-lived nuclides such as $^{238}\mathrm{U} \to {}^{206}\mathrm{Pb}$ and $^{40}\mathrm{K} \to {}^{40}\mathrm{Ar}$.

**Example 7.3.7** A rock is found to contain $0.275\,\mathrm{mg}$ of $^{206}\mathrm{Pb}$ for every $1.000\,\mathrm{mg}$ of $^{238}\mathrm{U}$. Assuming that the rock contained no $^{206}\mathrm{Pb}$ when it formed and has been closed since, find its age.

Solution. $^{238}\mathrm{U}$ decays through a series of steps to $^{206}\mathrm{Pb}$, and the half-lives of the intermediate nuclides are all much shorter than that of $^{238}\mathrm{U}$, so the whole decay chain can be treated as one step. Each $^{238}\mathrm{U}$ atom yields one $^{206}\mathrm{Pb}$ atom, so $0.275\,\mathrm{mg}$ of lead corresponds to $0.275 \times \frac{238}{206}\,\mathrm{mg} = 0.318\,\mathrm{mg}$ of uranium, and the original uranium in the rock was $N_0 = 1.318\,\mathrm{mg}$ (relative amount).

$$
t = \frac{4.47 \times 10^9\,\mathrm{a}}{0.693}\ln\frac{1.318}{1.000} = 1.8 \times 10^9\,\mathrm{a}.
$$

**Example 7.3.8** $1.000\,\mathrm{g}$ of $^{90}\mathrm{Sr}$ is reduced to $0.952\,\mathrm{g}$ after 2 years. Find (1) the half-life and (2) the mass remaining after 5 years.

Solution. (1) $t_{1/2} = \frac{t\ln 2}{\ln(N_0/N)} = \frac{2 \times 0.693}{\ln(1.000/0.952)}\,\mathrm{a} = 28.2\,\mathrm{a}$. (2) $N = 1.000\,\mathrm{g} \times \mathrm{e}^{-0.693 \times 5/28.2} = 0.884\,\mathrm{g}$.

**Example 7.3.9** At $20\,^\circ\mathrm{C}$ in dilute NaOH solution, $\ce{2H2O2(aq) -> 2H2O(l) + O2(g)}$ is first order, $-\frac{\mathrm{d}c(\ce{H2O2})}{\mathrm{d}t} = k\,c(\ce{H2O2})$, with $k = 1.06 \times 10^{-3}\,\mathrm{min^{-1}}$. The initial concentration is $0.020\,\mathrm{mol\,L^{-1}}$. Find (1) the concentration after 100 min and (2) the half-life.

Solution. (1) $c = 0.020\,\mathrm{mol\,L^{-1}} \times \mathrm{e}^{-1.06 \times 10^{-3} \times 100} = 0.018\,\mathrm{mol\,L^{-1}}$. (2) $t_{1/2} = \frac{0.693}{1.06 \times 10^{-3}\,\mathrm{min^{-1}}} = 654\,\mathrm{min}$.

### 7.3.3. Temperature: The Arrhenius Equation

The effect of temperature on the reaction rate is usually much larger than that of concentration, and it appears mainly in the rate constant $k$. In 1884 van 't Hoff found empirically that $\ln k$ is linear in $1/T$; in 1889 Arrhenius, studying the hydrolysis of sucrose, gave its physical interpretation and introduced the concept of activated molecules.

**Definition 7.3.5 (Arrhenius Equation)** The empirical relation between the rate constant and temperature,

$$
k = A\,\mathrm{e}^{-E_{\mathrm{a}}/RT} \tag{7.1}
$$
is called the **Arrhenius equation**, where $E_{\mathrm{a}}$ is called the (experimental) activation energy and $A$ the **pre-exponential factor** (frequency factor), with the same unit as $k$. Over a modest temperature range both can be regarded as constants. In general the activation energy is defined (IUPAC) by

$$
E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T};
$$
when $E_{\mathrm{a}}$ is independent of temperature, integration gives Eq. (7.1).

Taking the logarithm of Eq. (7.1) gives $\ln k = \ln A - \frac{E_{\mathrm{a}}}{RT}$: a plot of $\ln k$ against $1/T$ (an Arrhenius plot) is a straight line with slope $-E_{\mathrm{a}}/R$ and intercept $\ln A$. Fitting this line by least squares to the values of $k$ at several temperatures is the standard method for determining the activation energy. With data at only two temperatures, subtracting the two equations gives

$$
\ln\frac{k_2}{k_1} = \frac{E_{\mathrm{a}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right). \tag{7.2}
$$

Equation (7.2) can be used to find the activation energy from the rate constants at two temperatures, or to find the rate constant at another temperature from the activation energy.

**Example 7.3.10** The rate constants for the decomposition of $\ce{N2O5}$ in $\ce{CCl4}$ are $4.69 \times 10^{-5}\,\mathrm{s^{-1}}$ at $298.15\,\mathrm{K}$ and $6.29 \times 10^{-4}\,\mathrm{s^{-1}}$ at $318.15\,\mathrm{K}$. Find the activation energy.

Solution. From Eq. (7.2),

$$
E_{\mathrm{a}} = R\frac{T_1T_2}{T_2 - T_1}\ln\frac{k_2}{k_1} = 8.314 \times \frac{298.15 \times 318.15}{20.00} \times \ln\frac{6.29 \times 10^{-4}}{4.69 \times 10^{-5}}\,\mathrm{J\,mol^{-1}} = 102\,\mathrm{kJ\,mol^{-1}}.
$$

**Example 7.3.11** The activation energy of $\ce{PH3(g) + B2H6(g) -> PH3BH3(g) + BH3(g)}$ is $48.0\,\mathrm{kJ\,mol^{-1}}$. At what temperature is the rate constant twice its value at $298\,\mathrm{K}$?

Solution. From Eq. (7.2), $\frac{1}{T_2} = \frac{1}{298\,\mathrm{K}} - \frac{R\ln 2}{E_{\mathrm{a}}} = 3.3557 \times 10^{-3}\,\mathrm{K^{-1}} - 1.2006 \times 10^{-4}\,\mathrm{K^{-1}}$, so $T_2 = 309\,\mathrm{K}$: a rise of about 11 K doubles the rate constant.

The activation energy in collision theory is a critical value of the energy (Definition 7.2.1), whereas $E_{\mathrm{a}}$ in the Arrhenius equation is an experimental quantity defined through $k(T)$. The connection between them is given by the following theorem, which also corrects the common statement that "the activation energy is the difference between the minimum energy of an effective collision and the average energy".

**Theorem 7.3.2 (Tolman's Interpretation)** Let the reactant molecules occupy states $i$ (energy $\varepsilon_i$, degeneracy $g_i$) according to the **Boltzmann distribution**, and let the rate constant for reaction of molecules in state $i$ be a temperature-independent $k_i$. Then

$$
E_{\mathrm{a}} = N_{\mathrm{A}}\left(\langle\varepsilon\rangle_{\mathrm{react}} - \langle\varepsilon\rangle\right),
$$
that is, the activation energy equals the difference (per mole) between the average energy of the molecules that react and the average energy of all reactant molecules.

**Proof** Let $\beta = 1/k_{\mathrm{B}}T$. The overall rate constant is the average of the rate constants of the states weighted by the Boltzmann distribution:

$$
k = \frac{\sum_i k_ig_i\mathrm{e}^{-\beta\varepsilon_i}}{\sum_i g_i\mathrm{e}^{-\beta\varepsilon_i}}.
$$
Differentiating with respect to $\beta$, $\frac{\mathrm{d}}{\mathrm{d}\beta}\ln\sum_i k_ig_i\mathrm{e}^{-\beta\varepsilon_i} = -\frac{\sum_i\varepsilon_ik_ig_i\mathrm{e}^{-\beta\varepsilon_i}}{\sum_ik_ig_i\mathrm{e}^{-\beta\varepsilon_i}} = -\langle\varepsilon\rangle_{\mathrm{react}}$, where the weight $k_ig_i\mathrm{e}^{-\beta\varepsilon_i}$ is proportional to the number of molecules reacting from state $i$ per unit time, so $\langle\varepsilon\rangle_{\mathrm{react}}$ is the average energy of the molecules that react; similarly $\frac{\mathrm{d}}{\mathrm{d}\beta}\ln\sum_ig_i\mathrm{e}^{-\beta\varepsilon_i} = -\langle\varepsilon\rangle$. Hence $\frac{\mathrm{d}\ln k}{\mathrm{d}\beta} = -\langle\varepsilon\rangle_{\mathrm{react}} + \langle\varepsilon\rangle$. With $\frac{\mathrm{d}\beta}{\mathrm{d}T} = -\frac{1}{k_{\mathrm{B}}T^2}$,

$$
E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T} = N_{\mathrm{A}}k_{\mathrm{B}}T^2 \cdot \frac{\langle\varepsilon\rangle_{\mathrm{react}} - \langle\varepsilon\rangle}{k_{\mathrm{B}}T^2} = N_{\mathrm{A}}\left(\langle\varepsilon\rangle_{\mathrm{react}} - \langle\varepsilon\rangle\right). \qquad \square
$$

Since molecules of higher energy react faster, $\langle\varepsilon\rangle_{\mathrm{react}} > \langle\varepsilon\rangle$ and so $E_{\mathrm{a}} > 0$. According to collision theory, $k \propto \bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT} \propto T^{1/2}\mathrm{e}^{-E_{\mathrm{c}}/RT}$, and substituting into the definition gives $E_{\mathrm{a}} = E_{\mathrm{c}} + \frac{1}{2}RT$: the experimental activation energy differs very little from the critical energy ($\frac{1}{2}RT = 1.2\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$), and the two are usually not distinguished.

The effect of the activation energy on the reaction rate can be seen from Eq. (7.1):

1. The larger the activation energy, the smaller $k$. For example, in the synthesis of ammonia $\ce{N2 + 3H2 -> 2NH3}$, $E_{\mathrm{a}} \approx 335\,\mathrm{kJ\,mol^{-1}}$ without a catalyst and about $167\,\mathrm{kJ\,mol^{-1}}$ with an $\ce{Fe-Al2O3-K2O}$ catalyst. With the pre-exponential factor unchanged, at $673\,\mathrm{K}$ $\frac{k_{\mathrm{cat}}}{k} = \mathrm{e}^{(334.7 - 167.4) \times 10^3/(8.314 \times 673)} \approx 9.7 \times 10^{12}$.
2. The larger the activation energy, the more sensitive the rate constant to temperature (the steeper the Arrhenius line). On going from $300\,\mathrm{K}$ to $400\,\mathrm{K}$, $k$ increases by a factor of about $2.3 \times 10^4$ for a reaction with $E_{\mathrm{a}} = 100\,\mathrm{kJ\,mol^{-1}}$ and by about $5 \times 10^8$ for one with $E_{\mathrm{a}} = 200\,\mathrm{kJ\,mol^{-1}}$. Raising the temperature therefore favors reactions of large activation energy: when several competing reactions occur together, a higher temperature increases the share of the reaction with the larger activation energy.

![Left: Arrhenius plots for three reactions with different activation energies (the same rate constant at 300 K), with slope −Ea/R; right: the factor by which the rate constant increases relative to 300 K as a function of temperature, with the factor for a 10 K rise given in the legend](./plots/arrhenius-sensitivity.py)

The effect of temperature can be understood intuitively from the energy distribution of the molecules. When the temperature rises, the energy distribution shifts to the right as a whole and broadens; the average energy increases little, but the fraction of molecules with energy above $E_{\mathrm{a}}$ (the tail of the distribution) increases manyfold: for $E_{\mathrm{a}} = 50\,\mathrm{kJ\,mol^{-1}}$, on going from $300\,\mathrm{K}$ to $310\,\mathrm{K}$ the mean kinetic energy increases by only about $3\%$, but the fraction of activated molecules almost doubles.

![Maxwell–Boltzmann distribution of molecular translational energy at 300 K and 310 K: left, linear axes, where the two curves almost coincide; right, logarithmic axes, where the shaded region is the molecules with energy above Ea = 50 kJ/mol, whose fraction roughly doubles](./plots/energy-distribution.py)

This leads to a rough empirical rule, the *van 't Hoff rule*: near room temperature, each 10 K rise in temperature increases the reaction rate by a factor of 2–4, that is, $\frac{k(T + 10\,\mathrm{K})}{k(T)} \approx 2\text{–}4$. By Eq. (7.2), near $300\,\mathrm{K}$ this corresponds to $E_{\mathrm{a}} \approx 50$–$110\,\mathrm{kJ\,mol^{-1}}$, which is the range of many common reactions; for reactions of larger activation energy the factor is also larger. By this rule, a reaction that is complete in 1 minute at $400\,\mathrm{K}$ requires $2^{10}$–$4^{10}$ minutes at $300\,\mathrm{K}$, that is, about 17 hours to 2 years. Refrigeration of food and the faster cooking in a pressure cooker rest on this principle.

### 7.3.4. Catalysts

**Definition 7.3.6** A substance that changes the reaction rate significantly when added in small amounts, while its own amount and chemical nature remain unchanged before and after the reaction, is called a **catalyst**; the effect of a catalyst in changing the reaction rate is called **catalysis**.

Catalysts that speed up reactions are the most common, and "catalyst" ordinarily means these. Substances that slow down reactions (such as the antioxidants that prevent the aging of rubber and the antioxidants in food) are conventionally called negative catalysts, but most of them are consumed in the reaction, and IUPAC calls them *inhibitors*. A substance that has little catalytic activity itself but significantly improves the performance of a catalyst is called a promoter, such as $\ce{K2O}$ and $\ce{Al2O3}$ in the iron catalyst for ammonia synthesis.

A catalyst takes part in the reaction, forms an unstable intermediate with the reactants, and then releases the product and is regenerated; it changes the reaction path, and the new path has a lower activation energy (for the potential energy diagram see 7.2.2). For example, the catalysis of the decomposition of $\ce{H2O2}$ by $\ce{I-}$:

$\ce{H2O2 + I- -> H2O + IO-}$ (slow), $\ce{H2O2 + IO- -> H2O + O2 + I-}$ (fast); on adding the two steps, $\ce{I-}$ cancels and the overall reaction remains $\ce{2H2O2 -> 2H2O + O2}$. Activation energies of some reactions with and without a catalyst are:

| Reaction | Uncatalyzed $E_{\mathrm{a}}/(\mathrm{kJ\,mol^{-1}})$ | Catalyzed $E_{\mathrm{a}}/(\mathrm{kJ\,mol^{-1}})$ | Catalyst |
|---|---|---|---|
| $\ce{2HI -> H2 + I2}$ | 184 | 105 | Au |
| $\ce{2N2O -> 2N2 + O2}$ | 245 | 121; 134 | Au; Pt |
| $\ce{3H2 + N2 -> 2NH3}$ | 335 | 167 | $\ce{Fe-Al2O3-K2O}$ |
| $\ce{2NH3 -> 3H2 + N2}$ | 335 | 163 | W |

Catalysts have the following characteristics:

1. A catalyst can only accelerate a reaction that is thermodynamically possible; it cannot make a reaction with $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ occur.
2. A catalyst does not change the initial and final states of the reaction and therefore does not change $\Delta_{\mathrm{r}}H_{\mathrm{m}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$, or the equilibrium constant; it cannot change the direction of the reaction and only shortens the time to reach equilibrium.
3. A catalyst accelerates the forward and reverse reactions by the same factor. For a one-step elementary reaction, at equilibrium the forward and reverse rates are equal, $k_+\prod c_{\mathrm{reactants}} = k_-\prod c_{\mathrm{products}}$, so the equilibrium constant is $K = k_+/k_-$ ([6.1.8](/6.1.8)); since a catalyst does not change $K$, it can only increase $k_+$ and $k_-$ by the same factor. On the potential energy diagram this is because the barriers of the forward and reverse reactions are lowered by the same amount ($E_{\mathrm{a}} - E_{\mathrm{a}}' = \Delta_{\mathrm{r}}H_{\mathrm{m}}$ is unchanged). A catalyst that accelerates dehydrogenation therefore also accelerates hydrogenation, and the catalyst for ammonia synthesis is also a catalyst for the decomposition of ammonia.
4. Catalysts are selective: with the same reactants, different catalysts can give different products. This is the most important value of catalysts in the chemical industry: the thermodynamically most favorable product is not necessarily the desired one. For example, the oxidation of ethylene ($250\,^\circ\mathrm{C}$):

| Product | Catalyst | Standard equilibrium constant (order of magnitude) |
|---|---|---|
| ethylene oxide | Ag | $10^6$ |
| acetaldehyde $\ce{CH3CHO}$ | Pd | $10^{18}$ |
| $\ce{CO2 + H2O}$ (complete oxidation) | — | $10^{130}$ |

Complete oxidation is overwhelmingly favored thermodynamically, but an Ag catalyst gives ethylene oxide, whose equilibrium constant is much smaller: the selectivity comes from kinetics, not from thermodynamics.

5. A catalyst is active only under certain conditions. A substance that greatly lowers or destroys the activity of a catalyst when added in small amounts is called a poison, and the phenomenon is called *catalyst poisoning*. For example, traces of phosphorus-, sulfur-, and arsenic-containing impurities in the feed gas deactivate the Pt catalyst for the oxidation of ammonia to nitric acid, and the catalysts in automobile exhaust systems are poisoned by the lead in leaded gasoline, one reason why leaded gasoline was phased out.

**Definition 7.3.7** A catalytic reaction in which the catalyst and the reactants are in the same phase is called **homogeneous catalysis**, such as the catalysis of the decomposition of $\ce{H2O2}$ by $\ce{I-}$ and of the hydrolysis of ethylene oxide to ethylene glycol by $\ce{H2SO4}$. A catalytic reaction in which the catalyst and the reactants are in different phases (usually the catalyst is a solid and the reactants are gases or liquids) is called **heterogeneous catalysis**.

Heterogeneous catalysis is the mainstay of the chemical industry: ammonia synthesis ($\ce{N2 + 3H2 <=> 2NH3}$, Fe catalyst), ammonia oxidation ($\ce{4NH3 + 5O2 -> 4NO + 6H2O}$, Pt–Rh gauze), and the three-way catalytic converter for automobile exhaust (Pt–Pd–Rh, which simultaneously oxidizes CO and hydrocarbons and reduces NO, as in $\ce{2CO + 2NO -> 2CO2 + N2}$, the reaction at the start of this section). The steps of heterogeneous catalysis are diffusion of the reactants to the surface, adsorption, reaction on the surface, desorption of the products, and diffusion away; when the active sites of the surface are saturated, the reaction appears zeroth order (7.3.2). The quantitative treatment of surface adsorption and surface reaction kinetics is given in [Physical Chemistry](/6.3).

Enzymes are the catalysts of living organisms; the great majority are proteins (a few are RNA, called ribozymes), and the reactants of an enzyme-catalyzed reaction are called substrates. The characteristics of *enzyme catalysis* are:

- High specificity: an enzyme catalyzes the reaction of only one substrate or one class of substrates of similar structure, and the substrate and the active site of the enzyme are complementary in shape and chemical properties.
- High efficiency: enzymes can accelerate reactions by factors of $10^6$–$10^{17}$, far more than ordinary chemical catalysts.
- Mild conditions: ordinary temperature, ordinary pressure, and nearly neutral pH, but sensitivity to temperature and pH; high temperature denatures and inactivates the enzyme.

The rate of an enzyme-catalyzed reaction as a function of substrate concentration is a saturation curve: approximately first order at low substrate concentration and tending to zeroth order at high concentration (the active sites of the enzyme are saturated), described by the Michaelis–Menten equation; a method for fitting its parameters to experimental data is given in [4.4.4](/4.4.4#sec-4.2.3). The derivation of this equation (pre-equilibrium or steady-state approximation) and enzyme kinetics are treated in [Physical Chemistry](/6.3) and [Biochemistry](/7.1).

## Summary

| Topic | Key points |
|---|---|
| Reaction rate | $v = \frac{1}{V}\frac{\mathrm{d}\xi}{\mathrm{d}t} = \frac{1}{\nu_{\mathrm{B}}}\frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}t}$; a reaction has only one rate; measured from tangents to the $c$–$t$ curve or by fitting |
| Collision theory | $v = PZ_{\mathrm{AB}}\mathrm{e}^{-E_{\mathrm{c}}/RT}/N_{\mathrm{A}}$: collision frequency × energy factor × steric factor |
| Transition state theory | the reaction passes through the transition state of highest potential energy; $\Delta_{\mathrm{r}}H_{\mathrm{m}} \approx E_{\mathrm{a}} - E_{\mathrm{a}}'$; the rate depends on the height of the barrier |
| Rate law | $v = kc_{\mathrm{A}}^\alpha c_{\mathrm{B}}^\beta$, orders determined by experiment (method of initial rates); the law of mass action applies only to elementary reactions |
| Reaction mechanism | the rate of a complex reaction is determined by the rate-determining step; the pre-equilibrium approximation eliminates intermediates; agreement of the rate law is a necessary condition for a correct mechanism |
| Integrated rate laws | orders 0, 1, 2: $c$, $\ln c$, $1/c$ against $t$ are straight lines; for first-order reactions $t_{1/2} = \ln 2/k$ is independent of concentration, which is used in radiometric dating |
| Temperature | $k = A\mathrm{e}^{-E_{\mathrm{a}}/RT}$; $E_{\mathrm{a}} = RT^2\,\mathrm{d}\ln k/\mathrm{d}T$ is the difference between the average energy of reacting molecules and of all molecules; about 2–4 times per 10 K |
| Catalysts | change the path and lower the activation energy; do not change $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ or the equilibrium constant and accelerate the forward and reverse reactions equally; selective, subject to poisoning; homogeneous, heterogeneous, and enzyme catalysis |

## Questions

1. Which of the following relations for the reaction $\ce{2W + X -> Y + Z}$ are correct? (a) $-\frac{\mathrm{d}c_{\mathrm{X}}}{\mathrm{d}t} = \frac{\mathrm{d}c_{\mathrm{Y}}}{\mathrm{d}t}$; (b) $-\frac{\mathrm{d}c_{\mathrm{X}}}{\mathrm{d}t} = -\frac{\mathrm{d}c_{\mathrm{W}}}{\mathrm{d}t}$; (c) $\frac{\mathrm{d}c_{\mathrm{Z}}}{\mathrm{d}t} = \frac{\mathrm{d}c_{\mathrm{Y}}}{\mathrm{d}t}$; (d) $\frac{\mathrm{d}c_{\mathrm{Z}}}{\mathrm{d}t} = -\frac{\mathrm{d}c_{\mathrm{W}}}{\mathrm{d}t}$.

   **Answer** (a) and (c) are correct. W is consumed twice as fast as X, so (b) and (d) are off by a factor of 2; the correct form is $\frac{\mathrm{d}c_{\mathrm{Z}}}{\mathrm{d}t} = -\frac{1}{2}\frac{\mathrm{d}c_{\mathrm{W}}}{\mathrm{d}t}$.

2. On the potential energy diagram of a two-step reaction, how do we distinguish a reaction intermediate from a transition state?

   **Answer** An intermediate lies in the valley between two barriers (a local minimum of the potential energy), and a transition state lies at the top of a barrier (a maximum along the reaction coordinate). An intermediate has a definite lifetime and can in principle be detected; a transition state is merely an instantaneous configuration.

3. The unit of the rate constant of a reaction is $\mathrm{L\,mol^{-1}\,s^{-1}}$. How does its half-life depend on the initial concentration?

   **Answer** The unit shows that the overall order is 2; with a single reactant, $t_{1/2} = 1/(kc_0)$, inversely proportional to the initial concentration.

4. Why does "the order of reaction equals the sum of the coefficients" not prove that a reaction is elementary?

   **Answer** Different mechanisms can give the same rate law; for example, the atomic mechanism of $\ce{H2 + I2}$ gives $v = kc(\ce{H2})c(\ce{I2})$ under the pre-equilibrium approximation (Example 7.3.3).
