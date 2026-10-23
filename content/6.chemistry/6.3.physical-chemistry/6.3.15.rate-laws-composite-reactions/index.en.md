---
title: Rate Laws and Composite Reactions
source_hash: 2fd3df555a5e
---

[6.1.7](/6.1.7) gave the framework of chemical kinetics: the **rate of reaction**, the **rate law**, the **elementary reaction** and the **reaction mechanism**, the integrated forms for first- and second-order reactions, the **Arrhenius equation** and the **pre-equilibrium approximation**. This chapter makes that framework systematic and quantitative. A reaction mechanism is a set of ordinary differential equations for the concentrations of the species, and the "phenomenological" part of chemical kinetics comes down to solving, or approximately solving, these equations ([2.4](/2.4)). The integrated forms for simple reactions of integer order (15.2) and the determination of the order from experimental data (15.3) are the simplest cases. The three typical kinds of composite reactions, opposing, parallel and consecutive (15.4), lead to linear systems that can be treated uniformly with the **matrix exponential**. The influence of temperature and the **principle of microscopic reversibility** (15.5) connect kinetics with the chemical equilibrium of [6.3.7](/6.3.7). When the equations are nonlinear and have no analytical solution, the rate-determining step, the **steady-state approximation** and the pre-equilibrium approximation (15.6) use the disparity of time scales to eliminate intermediates; these are the main tools of mechanism derivation (15.7 chain reactions, 15.8 proposing a mechanism). Finally, the relaxation methods for fast reactions (15.9) are a direct application of linearization near the equilibrium point.

The next chapter ([6.3.16](/6.3.16)) calculates rate constants from molecular properties, [6.3.17](/6.3.17) discusses the effects of solvents, light and catalysts, and the chemical oscillations and dissipative structures of [6.3.18](/6.3.18) are built on the nonlinear rate equations of this chapter. We use the notation of this book: the rate of reaction is $v$ (many textbooks write $r$), the rate constant is $k$, the rate constant of the reverse reaction is always written $k_{-1}$, and $[\ce{B}]$ and $c_{\mathrm{B}}$ both denote concentration.

## 15.1. Basic Concepts

### 15.1.1. Expressing the Rate of Reaction

For a reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$, the change of the **extent of reaction** per unit time, $\dot\xi = \mathrm{d}\xi/\mathrm{d}t$, is called the conversion rate; at constant volume, dividing by the volume gives the **rate of reaction** ([6.1.7](/6.1.7#def-7.1.2))

$$
v = \frac{1}{V}\frac{\mathrm{d}\xi}{\mathrm{d}t} = \frac{1}{\nu_{\mathrm{B}}}\frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}t}.
$$

It does not depend on which substance is chosen, but it does depend on how the stoichiometric equation is written. For a complex reaction this relation holds only when the concentrations of intermediates are negligible: if an intermediate accumulates, the quantities $\frac{1}{\nu_{\mathrm{B}}}\frac{\mathrm{d}c_{\mathrm{B}}}{\mathrm{d}t}$ of the various substances are not equal at a given moment. In experiments the rate law is often written in terms of the rate of consumption of one substance, $-\mathrm{d}c_{\mathrm{A}}/\mathrm{d}t = \lvert\nu_{\mathrm{A}}\rvert v$, and the rate constant defined thereby is $k_{\mathrm{A}} = \lvert\nu_{\mathrm{A}}\rvert k$; when one meets a rate constant one must first find out which definition it corresponds to.

Gas-phase reactions can also be expressed in terms of partial pressures, $v_p = \frac{1}{\nu_{\mathrm{B}}}\frac{\mathrm{d}p_{\mathrm{B}}}{\mathrm{d}t}$. For an ideal gas, $p_{\mathrm{B}} = c_{\mathrm{B}}RT$, and at constant temperature $v_p = vRT$; for an $n$th-order reaction, $v = k_cc^n$ and $v_p = k_pp^n$, so that

$$
k_p = k_c(RT)^{1-n}.
$$

For a first-order reaction $k_p = k_c$, and for a second-order reaction $k_c = k_pRT$. The rate of a heterogeneously catalyzed reaction is proportional to the amount of catalyst and is often expressed per unit mass, volume or surface area of catalyst: $\frac{1}{m}\dot\xi$, $\frac{1}{V}\dot\xi$, $\frac{1}{A_{\mathrm{s}}}\dot\xi$ ([6.3.20](/6.3.20)).

### 15.1.2. Measuring Kinetic Curves

The curve of the concentration of a reactant or product against time is called a kinetic curve, and the rate is the slope of its tangent (divided by the stoichiometric number). There are two kinds of measurement methods:

- Chemical methods: samples are taken at fixed times and the reaction is stopped by quenching, dilution, adding an inhibitor or removing the catalyst, followed by chemical analysis. This is simple but hard to make continuous and fast.
- Physical methods: a physical quantity that is quantitatively related to concentration (optical rotation, refractive index, conductivity, electromotive force, dielectric constant, viscosity, absorbance, or spectroscopic signals such as IR, UV-Vis, EPR, NMR and XPS) is measured as a function of time. Measurements can be continuous and in situ, and do not disturb the reaction.

When the initial rate is measured, interference from products and side reactions is smallest, which is the basis of the **method of initial rates**. Mixing takes time (about $1\,\mathrm{s}$ in routine operation), and fast reactions with half-lives shorter than this require special methods (15.9).

### 15.1.3. Elementary Reactions and Overall Reactions

[6.1.7](/6.1.7#def-7.3.2) defined the **elementary reaction**, the **complex reaction**, the **reaction mechanism** and the **molecularity**. A reaction consisting of a single elementary reaction is called a simple reaction, such as the Diels–Alder addition of butadiene and ethylene to give cyclohexene; an ordinary stoichiometric equation is only an overall reaction, which states the quantitative relation among the substances taking part but not how the reaction occurs. The three reactions with similar stoichiometric equations

$$
\ce{H2 + I2 -> 2HI}, \qquad \ce{H2 + Cl2 -> 2HCl}, \qquad \ce{H2 + Br2 -> 2HBr}
$$
have entirely different mechanisms and rate laws (M is a third body that only transfers energy and may be any molecule or the wall):

| Reaction | Mechanism | Experimental rate law |
|---|---|---|
| $\ce{H2 + I2}$ | $\ce{I2 + M <=> 2I + M}$ (fast); $\ce{H2 + 2I -> 2HI}$ (slow) | $v = k[\ce{H2}][\ce{I2}]$ |
| $\ce{H2 + Cl2}$ | $\ce{Cl2 + M -> 2Cl + M}$; $\ce{Cl + H2 -> HCl + H}$; $\ce{H + Cl2 -> HCl + Cl}$; $\ce{2Cl + M -> Cl2 + M}$ | $v = k[\ce{H2}][\ce{Cl2}]^{1/2}$ |
| $\ce{H2 + Br2}$ | As above, plus $\ce{H + HBr -> H2 + Br}$ | $v = \dfrac{k[\ce{H2}][\ce{Br2}]^{1/2}}{1 + k'[\ce{HBr}]/[\ce{Br2}]}$ |

The latter two are chain reactions, whose rate laws will be derived from the mechanisms in 15.7. The way to write an elementary reaction is unique ($\ce{2I -> I2}$ cannot be written $\ce{I -> 1/2I2}$); bimolecular reactions are the most common, termolecular reactions are rare, and elementary reactions of molecularity four or higher have not been found.

## 15.2. Simple Reactions of Integer Order

### 15.2.1. Rate Laws and Order

[6.1.7](/6.1.7#def-7.3.1) defined the rate law of power-function form $v = kc_{\mathrm{A}}^{\alpha}c_{\mathrm{B}}^{\beta}\cdots$, the **order of reaction** $n = \alpha + \beta + \cdots$ and the **rate constant**; for an elementary reaction the **law of mass action** gives an order equal to the stoichiometric coefficient. Two supplementary remarks:

1. The law of mass action holds for ideal systems; in nonideal solutions the more accurate form is $v = ka_{\mathrm{A}}^{\alpha}a_{\mathrm{B}}^{\beta}$ (in terms of **activity**), or the activity coefficients are absorbed into the rate constant (this is how the primary kinetic salt effect is treated in [6.3.17](/6.3.17)).
2. The order is an empirical quantity; it may be an integer, a fraction, zero or negative, and may not exist at all (as for $\ce{H2 + Br2}$). Order and molecularity are different concepts: the former refers to the rate law and the latter to elementary reactions, and the two are numerically equal only for elementary reactions.

The unit of the rate constant is determined by the order: the unit of $k$ for an $n$th-order reaction is $(\mathrm{mol\,L^{-1}})^{1-n}\,\mathrm{s^{-1}}$.

### 15.2.2. Integrated Rate Laws of $n$th-Order Reactions

When there is only one reactant (or when the reactant concentrations are in stoichiometric ratio), the rate law is $-\frac{\mathrm{d}c}{\mathrm{d}t} = kc^n$. The integrated forms for zeroth, first and second order are in [6.1.7](/6.1.7#sec-7.3.2); the general case is as follows.

**Formula 15.2.1 ($n$th-Order Reaction)** Let $-\frac{\mathrm{d}c}{\mathrm{d}t} = kc^n$, $c(0) = c_0$, $n \ne 1$. Separating variables and integrating gives

$$
\frac{1}{c^{n-1}} - \frac{1}{c_0^{n-1}} = (n-1)kt, \qquad t_{1/2} = \frac{2^{n-1} - 1}{(n-1)kc_0^{n-1}}.
$$

As $n \to 1$, $\frac{2^{n-1}-1}{n-1} \to \ln 2$, and we recover the first-order result $t_{1/2} = \ln 2/k$. The relation of the half-life to the initial concentration, $t_{1/2} \propto c_0^{1-n}$, is a convenient basis for judging the order: for a first-order reaction it is independent of $c_0$, for a second-order reaction it is inversely proportional to $c_0$, and for a zeroth-order reaction it is proportional to $c_0$.

For a second-order reaction $\ce{A + B -> P}$ with initial concentrations $a \ne b$, $\frac{\mathrm{d}x}{\mathrm{d}t} = k(a-x)(b-x)$, and integration by partial fractions gives

$$
\frac{1}{a-b}\ln\frac{b(a-x)}{a(b-x)} = kt,
$$
that is, $\ln\frac{c_{\mathrm{A}}}{c_{\mathrm{B}}}$ against $t$ is a straight line of slope $(a-b)k$. In this case there is no single half-life for the whole reaction; A and B each have their own.

**Definition 15.2.1 (Third-Order Reaction)** A reaction whose rate is proportional to the cube of the concentration is called a **third-order reaction**. Typical gas-phase examples are the reactions involving NO, $\ce{2NO + O2 -> 2NO2}$ and $\ce{2NO + Cl2 -> 2NOCl}$, and the recombination of atoms with a third body, $\ce{I + I + M -> I2 + M}$.

When the three reactants have equal initial concentrations, $-\frac{\mathrm{d}c}{\mathrm{d}t} = kc^3$, and Formula 15.2.1 ($n = 3$) gives

$$
\frac{1}{2c^2} - \frac{1}{2c_0^2} = kt, \qquad t_{1/2} = \frac{3}{2kc_0^2}.
$$

The rate constant of $\ce{2NO + O2}$ decreases as the temperature rises; it is not an elementary termolecular reaction, and 15.5.4 explains this by pre-equilibrium.

### 15.2.3. Examples

**Example 15.2.1 (First-Order Reaction Followed by Total Pressure)** A gas-phase first-order reaction $\ce{A(g) -> B(g) + C(g)}$ is carried out in a constant-volume vessel, starting with A only, at pressure $p_0 = 101.325\,\mathrm{kPa}$. Find how the total pressure $p$ varies with time.

**Solution** At time $t$, $p_{\mathrm{A}} = p_0 - x$ and $p_{\mathrm{B}} = p_{\mathrm{C}} = x$, so the total pressure is $p = p_0 + x$ and $p_{\mathrm{A}} = 2p_0 - p$. For a first-order reaction $k_p = k_c = k$ and $\ln\frac{p_{\mathrm{A}}}{p_0} = -kt$, that is,

$$
\ln\frac{2p_0 - p}{p_0} = -kt, \qquad p = p_0\left(2 - \mathrm{e}^{-kt}\right).
$$
A plot of $\ln(2p_0 - p)$ against $t$ is a straight line of slope $-k$. Following a reaction by the total pressure requires that the number of gas molecules differ before and after reaction and that there be no side reactions.

**Example 15.2.2 (Thermal Decomposition of $\ce{N2O}$)** The half-life of $\ce{2N2O(g) -> 2N2(g) + O2(g)}$ is inversely proportional to the initial pressure. At $970\,\mathrm{K}$, $p_0 = 39.2\,\mathrm{kPa}$ and $t_{1/2} = 1529\,\mathrm{s}$; at $1030\,\mathrm{K}$, $p_0 = 48.0\,\mathrm{kPa}$ and $t_{1/2} = 212\,\mathrm{s}$. (1) Find $k_p$ at the two temperatures (defined by $-\mathrm{d}p_{\ce{N2O}}/\mathrm{d}t = k_pp_{\ce{N2O}}^2$); (2) find the activation energy; (3) at $1030\,\mathrm{K}$ and $p_0 = 53.3\,\mathrm{kPa}$, how long does it take for the total pressure to reach $64.0\,\mathrm{kPa}$?

**Solution** (1) $t_{1/2} \propto 1/p_0$ shows that the reaction is second order, and $t_{1/2} = 1/(k_pp_0)$:

$$
k_p(970\,\mathrm{K}) = \frac{1}{1529 \times 39.2 \times 10^3}\,\mathrm{Pa^{-1}\,s^{-1}} = 1.67 \times 10^{-8}\,\mathrm{Pa^{-1}\,s^{-1}}, \qquad k_p(1030\,\mathrm{K}) = 9.83 \times 10^{-8}\,\mathrm{Pa^{-1}\,s^{-1}}.
$$
In concentration units, $k_c = k_pRT = 9.83 \times 10^{-8} \times 8.314 \times 1030\,\mathrm{m^3\,mol^{-1}\,s^{-1}} = 0.84\,\mathrm{L\,mol^{-1}\,s^{-1}}$ ($1030\,\mathrm{K}$).

(2) The factor $T$ in $k_c = k_pRT$ makes the activation energies of the two kinds of rate constant differ by $RT$; calculating from $k_p$,

$$
E_{\mathrm{a}} \approx R\,\frac{\ln(k_2/k_1)}{1/T_1 - 1/T_2} = 8.314 \times \frac{\ln(9.83/1.67)}{1/970 - 1/1030}\,\mathrm{J\,mol^{-1}} = 245\,\mathrm{kJ\,mol^{-1}},
$$
in agreement with the activation energy of the uncatalyzed decomposition of $\ce{N2O}$ in the table of [6.1.7](/6.1.7#sec-7.3.4) (calculating from $k_c$ adds about $RT \approx 8\,\mathrm{kJ\,mol^{-1}}$, within the precision of the data).

(3) When the partial pressure of $\ce{N2O}$ consumed is $y$, $y$ of $\ce{N2}$ and $y/2$ of $\ce{O2}$ are formed, and the total pressure is $p = p_0 + y/2$. At $p = 64.0\,\mathrm{kPa}$, $y = 21.4\,\mathrm{kPa}$ and $p_{\ce{N2O}} = 31.9\,\mathrm{kPa}$. From the integrated second-order law,

$$
t = \frac{1}{k_p}\left(\frac{1}{p_{\ce{N2O}}} - \frac{1}{p_0}\right) = \frac{1}{9.83 \times 10^{-8}}\left(\frac{1}{31.9 \times 10^3} - \frac{1}{53.3 \times 10^3}\right)\,\mathrm{s} = 128\,\mathrm{s}.
$$

### 15.2.4. Summary

| Order | Differential form | Integrated form | Linear relation | $t_{1/2}$ | Unit of $k$ |
|---|---|---|---|---|---|
| 0 | $-\dot c = k$ | $c = c_0 - kt$ | $c$–$t$ | $\frac{c_0}{2k}$ | $\mathrm{mol\,L^{-1}\,s^{-1}}$ |
| 1 | $-\dot c = kc$ | $\ln\frac{c_0}{c} = kt$ | $\ln c$–$t$ | $\frac{\ln 2}{k}$ | $\mathrm{s^{-1}}$ |
| 2 | $-\dot c = kc^2$ | $\frac1c - \frac1{c_0} = kt$ | $\frac1c$–$t$ | $\frac{1}{kc_0}$ | $\mathrm{L\,mol^{-1}\,s^{-1}}$ |
| 3 | $-\dot c = kc^3$ | $\frac{1}{2c^2} - \frac{1}{2c_0^2} = kt$ | $\frac{1}{c^2}$–$t$ | $\frac{3}{2kc_0^2}$ | $\mathrm{L^2\,mol^{-2}\,s^{-1}}$ |
| $n$ | $-\dot c = kc^n$ | $\frac{1}{c^{n-1}} - \frac{1}{c_0^{n-1}} = (n-1)kt$ | $\frac{1}{c^{n-1}}$–$t$ | $\frac{2^{n-1}-1}{(n-1)kc_0^{n-1}}$ | $(\mathrm{mol\,L^{-1}})^{1-n}\,\mathrm{s^{-1}}$ |

A zeroth-order reaction ends at $t = c_0/k$; reactions of all other orders cannot go to completion in finite time.

## 15.3. Determining the Order of Reaction

Determining the rate law means determining the order and the rate constant. There are two experimental designs: measuring the $c$–$t$ curve of one sample, or using a set of samples with different initial concentrations; and there are two ways of treating the data: with the integrated form or with the differential form.

### 15.3.1. The Integral Method and the Half-Life Method

**Definition 15.3.1** The method of determining the order on the basis of the integrated rate law is called the **integral method**: in the graphical version, the data are plotted according to the linear relations of the table for each order, the order giving a straight line is the one sought, and the slope gives $k$; in the trial version, the data are substituted into the integrated law of each order to calculate $k$, and the order for which $k$ is constant is the one sought (the two are essentially the same). The method of determining the order from the relation between half-life and initial concentration, $t_{1/2} = Bc_0^{1-n}$, is called the **half-life method**:

$$
\lg t_{1/2} = (1-n)\lg c_0 + \lg B,
$$
$\lg t_{1/2}$ plotted against $\lg c_0$ has slope $1-n$; with only two sets of data, $n = 1 + \frac{\lg(t_{1/2}/t_{1/2}')}{\lg(c_0'/c_0)}$.

The integral method requires one to guess the order first; when the data cover a narrow range, several orders may all "approximate a straight line", and fractional orders are hard to judge. The half-life method needs no guess and can use a single $c$–$t$ curve: read from different starting points the time for the concentration to fall to a half, and again to a half, and so on, and each segment can be regarded as an experiment with a different initial concentration.

### 15.3.2. The Differential Method and the Method of Initial Rates

**Definition 15.3.2** The method of determining the order on the basis of the differential rate law is called the **differential method**: the rate $v$ at each time is found from the $c$–$t$ curve, and the plot of $\lg v$ against $\lg c$ according to

$$
\lg v = n\lg c + \lg k
$$
has slope $n$ and intercept $\lg k$.

Tangents at different points of one curve give the order with respect to time; if the product retards or accelerates the reaction, it differs from the order with respect to concentration obtained from initial rates, and the latter is the "true" order. The **method of initial rates** ([6.1.7](/6.1.7#sec-7.3.1)) measures the initial rates $v_0 = kc_0^n$ of a set of samples with different initial concentrations and obtains $n$ from the slope of $\lg v_0$ against $\lg c_0$; when the initial concentration is doubled successively (the "doubling method"), $v_0$ staying unchanged, doubling and increasing fourfold correspond to $n = 0, 1, 2$, respectively. The difficulty of the differential method is that differentiation amplifies noise; today one generally differentiates a smoothed or fitted curve, or fits the integrated law directly (see 15.3.4).

### 15.3.3. The Isolation Method

When the rate law contains several reactants, $v = kc_{\mathrm{A}}^{\alpha}c_{\mathrm{B}}^{\beta}c_{\mathrm{C}}^{\gamma}$ is a function of several variables, and one must find a way to reduce it to a function of one variable in order to determine the partial orders one by one.

**Definition 15.3.3** The method in which all reactants except A are in large excess ($c_{\mathrm{B},0}, c_{\mathrm{C},0} \gg c_{\mathrm{A},0}$), so that their concentrations remain approximately constant during the reaction and the rate law reduces to $v = k'c_{\mathrm{A}}^{\alpha}$ with $k' = kc_{\mathrm{B},0}^{\beta}c_{\mathrm{C},0}^{\gamma}$, thus determining $\alpha$ separately, is called the **isolation method** (Ostwald's isolation method). When $\alpha = 1$, the first-order reaction obtained in this way is called a **pseudo-first-order reaction**.

The acid-catalyzed hydrolysis of sucrose in a large excess of water and the saponification of an ester in a large excess of base are pseudo-first-order reactions. Changing the concentration of the excess substance B and measuring $k'$ again gives $\beta$ from the slope of $\lg k'$ against $\lg c_{\mathrm{B},0}$.

**Example 15.3.1** Two sets of experiments are done on $\ce{A + 2B -> P}$ at $298\,\mathrm{K}$: (1) $c_{\mathrm{A},0} = c_{\mathrm{B},0}/2 = 40\,\mathrm{mol\,m^{-3}}$, and $c_{\mathrm{A}}$ falls linearly with time, $c_{\mathrm{A}} = 40, 35, 30, 25, 20\,\mathrm{mol\,m^{-3}}$ at $t = 0, 2.5, 5.0, 7.5, 10\,\mathrm{min}$; (2) $c_{\mathrm{A},0} = c_{\mathrm{B},0}/200 = 40\,\mathrm{mol\,m^{-3}}$, and the time for A to be consumed by half is constant. Find the rate law $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = kc_{\mathrm{A}}^{\alpha}c_{\mathrm{B}}^{\beta}$.

**Solution** In experiment (1) the reactants are in stoichiometric ratio, so $c_{\mathrm{B}} = 2c_{\mathrm{A}}$ throughout the reaction, and the rate law reduces to $-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = 2^{\beta}kc_{\mathrm{A}}^{\alpha+\beta}$. The $c_{\mathrm{A}}$–$t$ plot is a straight line, so $\alpha + \beta = 0$ and $2^{\beta}k = 2\,\mathrm{mol\,m^{-3}\,min^{-1}}$. In experiment (2), B is in large excess, $c_{\mathrm{B}} \approx 8000\,\mathrm{mol\,m^{-3}}$, and this is the isolation method for A; the half-life is independent of concentration, so $\alpha = 1$, hence $\beta = -1$ and $k = 4\,\mathrm{mol\,m^{-3}\,min^{-1}}$:

$$
-\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = (4\,\mathrm{mol\,m^{-3}\,min^{-1}})\,\frac{c_{\mathrm{A}}}{c_{\mathrm{B}}}.
$$
The order in B is negative, so B retards the reaction; such a rate law shows that the reaction is not elementary.

### 15.3.4. Determining Rate Parameters by Fitting

Linearized plots are intuitive but statistically unsatisfactory. Suppose the measured concentrations carry an absolute error $\sigma$ of roughly constant size; after taking logarithms the error of $\ln c$ is about $\sigma/c$: the points at late times, where the concentration is small and the error is amplified, carry the same weight in an ordinary **least squares** fit of $\ln c$ against $t$ as the early points. The transformation $1/c$ is worse still. A better approach is to perform **nonlinear regression** ([3.3](/3.3)) directly on the integrated law $c(t; k, n, c_0)$, using `scipy.optimize.curve_fit` in Python ([4.4.4](/4.4.4#sec-4.2.3)), which also gives the standard errors of the parameters; the order itself can also be treated as a parameter to be estimated. When the mechanism is complicated and has no analytical integrated form, one can embed the numerical solution of the ordinary differential equations (`solve_ivp`) in the objective function of the fit, which is the general method of modern kinetic data treatment. The Michaelis–Menten fit in 15.6 and [6.3.17](/6.3.17) provides two examples.

## 15.4. Typical Composite Reactions

The mechanisms of complex reactions are extremely varied, but there are only three basic ways of combining elementary reactions: opposing, parallel and consecutive. In what follows, first-order (1-1 order) reactions are taken as examples; the rate equations are then linear and can be solved exactly.

### 15.4.1. Opposing Reactions

**Definition 15.4.1** A reaction in which both the forward and reverse directions proceed at appreciable rates is called an **opposing reaction**.

For a 1-1 order opposing reaction $\ce{A <=>[k_1][k_{-1}] B}$, with $[\ce{A}] = a$ and $[\ce{B}] = 0$ at $t = 0$, and with the concentration of B equal to $x$,

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = k_1(a - x) - k_{-1}x.
$$
At equilibrium $\frac{\mathrm{d}x}{\mathrm{d}t} = 0$ and $k_1(a - x_{\mathrm{eq}}) = k_{-1}x_{\mathrm{eq}}$, that is, $x_{\mathrm{eq}} = \frac{k_1a}{k_1 + k_{-1}}$, so the rate equation can be written $\frac{\mathrm{d}x}{\mathrm{d}t} = (k_1 + k_{-1})(x_{\mathrm{eq}} - x)$, and integration gives

$$
\ln\frac{x_{\mathrm{eq}}}{x_{\mathrm{eq}} - x} = (k_1 + k_{-1})t. \tag{15.1}
$$

An opposing reaction approaches equilibrium in the same way as a first-order reaction, but the "rate constant" is the sum of the forward and reverse rate constants: the deviation from equilibrium, $x_{\mathrm{eq}} - x$, decays at the rate $k_1 + k_{-1}$. The slope of $\ln(x_{\mathrm{eq}} - x)$ against $t$ gives $k_1 + k_{-1}$, and the equilibrium composition gives $\frac{k_1}{k_{-1}} = \frac{x_{\mathrm{eq}}}{a - x_{\mathrm{eq}}} = K$; solving the two together gives $k_1$ and $k_{-1}$. When $k_1 \gg k_{-1}$, $x_{\mathrm{eq}} \approx a$, and Eq. (15.1) reduces to the one-way first-order reaction.

The relation $\frac{k_1}{k_{-1}} = K$ for an opposing reaction (proved in general in 15.5.2) also links the effect of temperature: $\frac{\mathrm{d}\ln(k_1/k_{-1})}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}$ (for reactions in solution; for gas-phase reactions replace $H$ by $U$, see 15.5.2). For an endothermic reaction, raising the temperature increases $k_1$ more than $k_{-1}$, and both equilibrium and rate favor the forward reaction; for an exothermic reaction, raising the temperature speeds up the reaction but lowers the equilibrium conversion.

### 15.4.2. Parallel Reactions

**Definition 15.4.2** Reactions in which the reactant undergoes two or more different reactions at the same time to give different products are called **parallel reactions** (competing reactions); the one that gives the desired product is called the main reaction, and the others are side reactions.

For 1-1 order parallel reactions $\ce{A ->[k_1] B}$ and $\ce{A ->[k_2] C}$, with $[\ce{B}] = x$ and $[\ce{C}] = y$,

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = k_1(a - x - y), \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = k_2(a - x - y), \qquad -\frac{\mathrm{d}(a - x - y)}{\mathrm{d}t} = (k_1 + k_2)(a - x - y).
$$
The third equation shows that the consumption of A is a first-order reaction with rate constant $k_1 + k_2$: $\ln\frac{a}{a - x - y} = (k_1 + k_2)t$. Dividing the first two gives $\frac{\mathrm{d}x}{\mathrm{d}y} = \frac{k_1}{k_2}$, and integration gives

$$
\frac{x}{y} = \frac{k_1}{k_2},
$$
that is, for parallel reactions of the same order the ratio of the product concentrations equals the ratio of the rate constants at all times. The slope of $\ln[\ce{A}]$ against $t$ gives $k_1 + k_2$, and the product ratio gives $k_1/k_2$.

The product ratio can be changed only by changing $k_1/k_2$: $\frac{\mathrm{d}\ln(k_1/k_2)}{\mathrm{d}T} = \frac{E_{\mathrm{a},1} - E_{\mathrm{a},2}}{RT^2}$, so raising the temperature favors the reaction with the larger activation energy ([6.1.7](/6.1.7#sec-7.3.3)); alternatively a selective catalyst ([6.3.17](/6.3.17)) can be used to change the rate constant of one of the reactions. When the two parallel reactions have different orders, the reactant concentration also affects the product ratio.

### 15.4.3. Consecutive Reactions

**Definition 15.4.3** Reactions that proceed one after another, the product of the earlier step being the reactant of the next, are called **consecutive reactions**.

For 1-1 order consecutive reactions $\ce{A ->[k_1] B ->[k_2] C}$ with only A (concentration $a$) at $t = 0$, and $[\ce{A}] = x$, $[\ce{B}] = y$, $[\ce{C}] = z$, $x + y + z = a$:

$$
-\frac{\mathrm{d}x}{\mathrm{d}t} = k_1x, \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = k_1x - k_2y, \qquad \frac{\mathrm{d}z}{\mathrm{d}t} = k_2y.
$$
The first equation gives $x = a\mathrm{e}^{-k_1t}$; substituting into the second gives the first-order linear equation $\dot y + k_2y = k_1a\mathrm{e}^{-k_1t}$, which by variation of constants ([2.4.3](/2.4.3)) has the solution (for $k_1 \ne k_2$)

$$
y = \frac{k_1a}{k_2 - k_1}\left(\mathrm{e}^{-k_1t} - \mathrm{e}^{-k_2t}\right), \qquad z = a\left(1 - \frac{k_2}{k_2 - k_1}\mathrm{e}^{-k_1t} + \frac{k_1}{k_2 - k_1}\mathrm{e}^{-k_2t}\right).
$$

The concentration of the intermediate B first rises and then falls. Setting $\frac{\mathrm{d}y}{\mathrm{d}t} = 0$ gives its maximum:

$$
t_{\max} = \frac{\ln(k_2/k_1)}{k_2 - k_1}, \qquad y_{\max} = a\left(\frac{k_1}{k_2}\right)^{k_2/(k_2 - k_1)}.
$$
In the limit $k_1 = k_2$, $y = k_1at\,\mathrm{e}^{-k_1t}$, $t_{\max} = 1/k_1$ and $y_{\max} = a/\mathrm{e}$. If B is the desired product, the reaction should be stopped near $t_{\max}$. The formation curve of the product C has an induction period at the beginning: C is hardly formed before B has accumulated.

![Concentration curves of the 1-1 order consecutive reaction A → B → C (computed with the matrix exponential) for k2/k1 = 0.2, 1, 5, 50, with dots marking the maximum of the intermediate; for k2 ≫ k1 B always stays small and its concentration is approximately in a steady state](./plots/consecutive-reactions.py)

When the rate constants of the two steps differ greatly:

- $k_1 \ll k_2$: $y \approx \frac{k_1}{k_2}a\mathrm{e}^{-k_1t}$, and the rate of formation of the product, $k_2y \approx k_1a\mathrm{e}^{-k_1t}$, is determined by the first step;
- $k_2 \ll k_1$: A is quickly all converted into B, after which $\frac{\mathrm{d}z}{\mathrm{d}t} \approx k_2a\mathrm{e}^{-k_2t}$, determined by the second step.

The overall rate is determined by the slowest step, which is the **rate-determining step** ([6.1.7](/6.1.7#sec-7.3.1)), like a "bottleneck" in a pipe.

### 15.4.4. A Unified Treatment: Linear Systems and the Matrix Exponential

The three kinds of reactions, and any network composed of first-order reactions, can be written as a linear system with constant coefficients for the concentration vector $\boldsymbol{c}$, $\dot{\boldsymbol{c}} = K\boldsymbol{c}$, whose solution is $\boldsymbol{c}(t) = \mathrm{e}^{tK}\boldsymbol{c}(0)$ (the **matrix exponential**, [2.4.8](/2.4.8#def-8.4.1)). For the consecutive reaction, for example,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\begin{bmatrix}x\\y\\z\end{bmatrix} = \begin{bmatrix}-k_1&0&0\\k_1&-k_2&0\\0&k_2&0\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix},
$$
and the **eigenvalues** of the rate matrix $K$ are $0, -k_1, -k_2$, so the solution is a linear combination of $1$, $\mathrm{e}^{-k_1t}$ and $\mathrm{e}^{-k_2t}$ ([2.4.8](/2.4.8#sec-8.5)), which is exactly the result above; when $k_1 = k_2$ the eigenvalues coincide, the matrix is not diagonalizable, and $t\mathrm{e}^{-k_1t}$ appears in the solution. In general each column of $K$ sums to zero (conservation of matter), so 0 is always an eigenvalue, with the equilibrium composition as the corresponding eigenvector; the other eigenvalues have negative real parts (and are all real when detailed balance, 15.5.2, is satisfied), and their reciprocals give the time scales on which the system approaches equilibrium. The nonzero eigenvalue $-(k_1 + k_{-1})$ of the matrix $K = \begin{bmatrix}-k_1&k_{-1}\\k_1&-k_{-1}\end{bmatrix}$ of the opposing reaction is the decay rate of Eq. (15.1). This viewpoint will be used again in 15.6 (separation of time scales) and 15.9 (relaxation). Numerically, `scipy.linalg.expm` computes the matrix exponential directly (as was done for the figure above).

## 15.5. Effect of Temperature and the Activation Energy

### 15.5.1. Types of Dependence of Rate on Temperature

The **van 't Hoff rule**, the **Arrhenius equation**, the **activation energy** and Tolman's statistical interpretation of the activation energy are in [6.1.7](/6.1.7#sec-7.3.3). The Arrhenius equation applies to most reactions over a not too wide temperature range; both collision theory and transition state theory show that the pre-exponential factor itself varies slowly with temperature, and over a very wide temperature range $\ln k$ against $1/T$ curves and is often rewritten $k = AT^m\mathrm{e}^{-E_0/RT}$. The variation of rate with temperature in experiments falls roughly into the following types:

| Type | Characteristic | Example |
|---|---|---|
| Arrhenius type | $k$ increases exponentially with $T$ | Most reactions |
| Explosive type | The rate increases sharply at a certain temperature | Branched-chain reactions, thermal explosion (15.7) |
| Rise then fall | There is an optimum temperature | Heterogeneous catalysis (adsorption falls with temperature), enzyme catalysis (denaturation at high temperature, [6.3.17](/6.3.17)) |
| Complex type | On raising the temperature the rate first rises, then falls, then rises again | Oxidation of carbon (side reactions take part in between) |
| Anomalous type | $k$ decreases as $T$ rises | $\ce{2NO + O2 -> 2NO2}$ (15.5.4) |

### 15.5.2. The Principle of Microscopic Reversibility and Detailed Balance

The equations of mechanics are invariant under time reversal $t \to -t$, $\boldsymbol{v} \to -\boldsymbol{v}$: every mechanical process has a completely reversed process. Applying this to elementary reactions:

**Theorem 15.5.1 (Principle of Microscopic Reversibility)** The reverse of an elementary reaction is also an elementary reaction; the forward and reverse reactions pass through the same intermediate state (the transition state) and proceed in opposite directions along the same reaction path.

From it follows macroscopically the next principle, which is a result of statistical mechanics and holds universally under thermodynamic equilibrium.

**Theorem 15.5.2 (Principle of Detailed Balance)** When a system is at equilibrium, the forward rate of every elementary reaction equals its reverse rate, and not merely is the net rate of formation of each species zero.

**Corollary 15.5.1** For an elementary reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$, the ratio of the forward and reverse rate constants equals the equilibrium constant expressed in concentrations:

$$
\frac{k_1}{k_{-1}} = \prod_{\mathrm{B}}(c_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}} = K^\circ(c^\circ)^{\sum\nu_{\mathrm{B}}} \quad\text{(ideal solution)}, \qquad \frac{k_1}{k_{-1}} = K^\circ\left(\frac{p^\circ}{RT}\right)^{\sum\nu_{\mathrm{B}}} \quad\text{(ideal gas)}.
$$

**Proof** By detailed balance, at equilibrium $k_1\prod_{\nu_{\mathrm{B}}<0}(c_{\mathrm{B}}^{\mathrm{eq}})^{\lvert\nu_{\mathrm{B}}\rvert} = k_{-1}\prod_{\nu_{\mathrm{B}}>0}(c_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}}$ (law of mass action), and rearranging gives the first equality. In an ideal solution $K^\circ = \prod(c_{\mathrm{B}}^{\mathrm{eq}}/c^\circ)^{\nu_{\mathrm{B}}}$; for an ideal gas $K^\circ = \prod(p_{\mathrm{B}}^{\mathrm{eq}}/p^\circ)^{\nu_{\mathrm{B}}}$, and substituting $p_{\mathrm{B}} = c_{\mathrm{B}}RT$ gives the result ([6.3.7](/6.3.7)). $\square$

**Corollary 15.5.2** The difference of the forward and reverse activation energies of an elementary reaction is $E_{\mathrm{a},1} - E_{\mathrm{a},-1} = \Delta_{\mathrm{r}}U_{\mathrm{m}}$; for a condensed-phase reaction $\Delta_{\mathrm{r}}U_{\mathrm{m}} \approx \Delta_{\mathrm{r}}H_{\mathrm{m}}$, and for an ideal-gas reaction $\Delta_{\mathrm{r}}U_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}} - \sum\nu_{\mathrm{B}}RT$.

**Proof** Take the logarithm of Corollary 15.5.1 and differentiate with respect to $T$, using the definition of the activation energy $E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T}$ and the **van 't Hoff equation** $\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}$. In solution $c^\circ$ does not vary with temperature, giving $E_{\mathrm{a},1} - E_{\mathrm{a},-1} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$; in the gas phase there is an extra term $-\sum\nu_{\mathrm{B}}\frac{\mathrm{d}\ln T}{\mathrm{d}T} = -\frac{\sum\nu_{\mathrm{B}}}{T}$,

$$
\frac{E_{\mathrm{a},1} - E_{\mathrm{a},-1}}{RT^2} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - \sum\nu_{\mathrm{B}}RT}{RT^2} = \frac{\Delta_{\mathrm{r}}U^\circ_{\mathrm{m}}}{RT^2}. \qquad \square
$$

This is the exact form of "$\Delta_{\mathrm{r}}H_{\mathrm{m}} \approx E_{\mathrm{a}} - E_{\mathrm{a}}'$" in [6.1.7](/6.1.7#sec-7.2.2). Detailed balance has a less obvious consequence as well: for a cycle $\ce{A <=> B <=> C <=> A}$, equilibrium with each step separately in balance requires $k_{\mathrm{AB}}k_{\mathrm{BC}}k_{\mathrm{CA}} = k_{\mathrm{BA}}k_{\mathrm{CB}}k_{\mathrm{AC}}$ (the Wegscheider condition); otherwise the system would contain a never-ending circulating flow, in contradiction with the second law of thermodynamics. Circulating flows do exist in nonequilibrium steady states, for example in molecular motors and ion pumps driven by ATP hydrolysis, where detailed balance is broken by an external chemical potential difference; the derivation of the **Onsager reciprocal relations** is likewise based on microscopic reversibility ([6.3.18](/6.3.18)).

### 15.5.3. Different Demands of Thermodynamics and Kinetics on Temperature

For an exothermic reaction, $K^\circ$ decreases as the temperature rises (the van 't Hoff equation) and the equilibrium conversion falls; but the activation energy is always positive, and raising the temperature always speeds up the reaction. Industrial practice must take both into account: ammonia synthesis $\ce{N2 + 3H2 <=> 2NH3}$ is exothermic, so low temperature favors equilibrium, but at low temperature the rate is too slow even with an iron catalyst, and industrially the process operates at $400$–$500\,^\circ\mathrm{C}$ and $15$–$30\,\mathrm{MPa}$, high pressure compensating the loss in equilibrium, with ammonia condensed out and unreacted gas recycled. For a reversible exothermic reaction, at fixed conversion the rate has a maximum with respect to temperature (the optimum temperature), and reactors are often designed with stepwise cooling. For an endothermic reaction, raising the temperature favors both equilibrium and rate.

### 15.5.4. Apparent Activation Energy of Composite Reactions

**Definition 15.5.1** The activation energy obtained from the apparent rate constant of a composite reaction by $E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T}$ is called the **apparent activation energy** (experimental activation energy).

If the apparent rate constant is a product of powers of the rate constants of elementary reactions, $k = \prod_ik_i^{m_i}$, then $E_{\mathrm{a}} = \sum_im_iE_{\mathrm{a},i}$ and $A = \prod_iA_i^{m_i}$. The pre-equilibrium mechanism of $\ce{H2 + I2}$ ([6.1.7](/6.1.7#sec-7.3.1)) gives $k = k_1k_2/k_{-1}$, so

$$
E_{\mathrm{a}} = E_{\mathrm{a},1} + E_{\mathrm{a},2} - E_{\mathrm{a},-1}, \qquad A = \frac{A_1A_2}{A_{-1}}.
$$

The apparent activation energy is the algebraic sum of the activation energies of the elementary steps; it no longer has the meaning of an energy barrier and can even be negative. One mechanism of $\ce{2NO + O2 -> 2NO2}$ is $\ce{2NO <=> N2O2}$ (fast equilibrium, $\Delta_{\mathrm{r}}H < 0$), $\ce{N2O2 + O2 -> 2NO2}$ (slow), with $k = K_1k_2$ and $E_{\mathrm{a}} = \Delta_{\mathrm{r}}H_1 + E_{\mathrm{a},2}$; the exothermic pre-equilibrium makes $E_{\mathrm{a}} < 0$, which is the anomalous type in the table of 15.5.1: raising the temperature lowers the equilibrium concentration of the dimer faster than it increases $k_2$.

### 15.5.5. Determining the Activation Energy

Measure $k$ at a series of temperatures and fit a least-squares straight line to $\ln k$ against $1/T$; the slope is $-E_{\mathrm{a}}/R$ ([6.1.7](/6.1.7#sec-7.3.3)). With only two temperatures (Example 15.2.2) the error is hard to estimate. As in 15.3.4, a better approach is a direct nonlinear fit of $k(T)$, or a fit of all the $c(t, T)$ data at all temperatures together with the Arrhenius parameters; when $\ln A$ and $E_{\mathrm{a}}$ are fitted they are highly correlated, and the correlation is often reduced by centering the temperature as $1/T - 1/\bar T$. The activation energy of an elementary reaction can be roughly estimated from bond energies (such as Hirschfelder's rule: for exothermic reactions of a radical with a molecule, $E_{\mathrm{a}} \approx 0.055$ times the energy of the bond broken), and accurate values require quantum-chemical calculation of the potential energy surface ([6.3.16](/6.3.16)).

**Example 15.5.1** Two reactions have activation energies of $60$ and $150\,\mathrm{kJ\,mol^{-1}}$. By what factor does each rate constant increase when the temperature is raised from $373\,\mathrm{K}$ to $473\,\mathrm{K}$?

**Solution** From $\ln\frac{k(T_2)}{k(T_1)} = \frac{E_{\mathrm{a}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$ with $\frac{1}{373} - \frac{1}{473} = 5.67 \times 10^{-4}\,\mathrm{K^{-1}}$, the increase is $\mathrm{e}^{4.09} \approx 60$-fold for $E_{\mathrm{a}} = 60\,\mathrm{kJ\,mol^{-1}}$ and $\mathrm{e}^{10.2} \approx 2.8 \times 10^4$-fold for $150\,\mathrm{kJ\,mol^{-1}}$. If the activation energy of the main reaction is larger than that of the side reaction, raising the temperature suppresses the side reaction; otherwise the temperature should be lowered.

## 15.6. Approximation Methods

As soon as one step of a mechanism is second order or higher, the system of rate equations generally has no analytical solution. But the rate constants of the steps of a mechanism often differ by several orders of magnitude, and this can be used to simplify the system.

### 15.6.1. The Rate-Determining Step and the Steady-State Approximation

If in a consecutive reaction one step is much slower than the others, the overall rate equals the rate of that step, and the fast steps after it do not affect the rate (the **rate-determining step** approximation, 15.4.3). For example, for $\ce{A + B -> C}$ (slow), $\ce{C -> D}$ (fast) and $\ce{D -> E}$ (fast), $v \approx k_1[\ce{A}][\ce{B}]$.

In the consecutive reaction figure, when $k_2 \gg k_1$ the concentration of the intermediate B always remains very small, and after a very short initial period its rate of formation and rate of consumption are almost equal: $y \approx \frac{k_1}{k_2}x$, $\frac{\mathrm{d}y}{\mathrm{d}t} = -k_1y$, which is smaller than the rate of formation $k_1x$ and the rate of consumption $k_2y$ by a factor of $k_2/k_1$. Generalizing this observation gives the most important approximation in kinetics.

**Definition 15.6.1 (Steady-State Approximation)** For a reactive intermediate of a mechanism (radical, atom, excited molecule, enzyme–substrate complex, etc.), after a brief initial induction period, the derivative of its concentration with respect to time is set equal to zero:

$$
\frac{\mathrm{d}[\mathrm{I}]}{\mathrm{d}t} \approx 0,
$$
so that the concentration of the intermediate is expressed by an algebraic equation as a function of the concentrations of reactants and products. This treatment is called the **steady-state approximation** (quasi-steady-state approximation).

The steady-state approximation does not say that the concentration of the intermediate is constant (it changes as the reactants are consumed), but that its rate of change is far smaller than its rates of formation and consumption, so it "follows" the concentrations of the reactants. It applies when the lifetime $\tau_{\mathrm{I}}$ of the intermediate (the reciprocal of the sum of the rate constants for its consumption) is much shorter than the time scale of change of the reactant concentrations; its concentration is then necessarily very small.

### 15.6.2. Relation Between the Steady-State and Pre-Equilibrium Approximations

Take the mechanism

$$
\ce{A <=>[k_1][k_{-1}] C}, \qquad \ce{C + B ->[k_2] P}
$$
as an example, with $v = \frac{\mathrm{d}[\ce{P}]}{\mathrm{d}t} = k_2[\ce{C}][\ce{B}]$.

Steady-state approximation: $\frac{\mathrm{d}[\ce{C}]}{\mathrm{d}t} = k_1[\ce{A}] - k_{-1}[\ce{C}] - k_2[\ce{C}][\ce{B}] = 0$,

$$
[\ce{C}] = \frac{k_1[\ce{A}]}{k_{-1} + k_2[\ce{B}]}, \qquad v_{\mathrm{SS}} = \frac{k_1k_2[\ce{A}][\ce{B}]}{k_{-1} + k_2[\ce{B}]}. \tag{15.2}
$$

The **pre-equilibrium approximation** ([6.1.7](/6.1.7#sec-7.3.1), also called the equilibrium assumption): the forward and reverse reactions of the first step are both much faster than the second step, and the first step is approximately at equilibrium, $[\ce{C}] = K[\ce{A}]$ with $K = k_1/k_{-1}$,

$$
v_{\mathrm{PE}} = \frac{k_1k_2}{k_{-1}}[\ce{A}][\ce{B}]. \tag{15.3}
$$

Comparing the two:

- When $k_{-1} \gg k_2[\ce{B}]$ (the intermediate returns to the reactant much faster than it forms product), Eq. (15.2) reduces to Eq. (15.3); the second step is rate-determining and the pre-equilibrium holds.
- When $k_{-1} \ll k_2[\ce{B}]$, Eq. (15.2) reduces to $v = k_1[\ce{A}]$: the first step is rate-determining, the fast reactions after it need not be considered, and the rate is independent of B.
- When the two are comparable, only the steady-state approximation gives the correct result, and the order of the rate in B varies between 0 and 1.

It is often said that "the steady-state assumption is fundamental and the equilibrium assumption is a special case of it". This holds when the concentration of the intermediate is small ($K \ll 1$) but is not universal: if $k_1$ and $k_{-1}$ are both much larger than $k_2[\ce{B}]$ and $K = k_1/k_{-1}$ is not small, the intermediate accumulates in large amounts, the steady-state approximation no longer applies, and the pre-equilibrium approximation still holds, except that the conservation relation $[\ce{A}] + [\ce{C}] = [\ce{A}]_{\mathrm{tot}}$ must then be taken into account, giving $v = \frac{k_2K}{1 + K}[\ce{A}]_{\mathrm{tot}}[\ce{B}]$. The conditions of applicability of the two approximations differ: the steady-state approximation requires a short-lived intermediate, and the pre-equilibrium approximation requires that the relaxation of the earlier step be much faster than that of the later one. When both can be used, the derivation by pre-equilibrium is simpler; in choosing the substance with which to express the rate, preference goes to the one that appears in the rate-determining step and occurs least often in the mechanism.

![Comparison of the full equations of the mechanism A ⇌ C, C + B → P (k2' = k2[B]; solved numerically with the implicit Radau method) with the two approximations. Left: k−1 ≫ k2', both approximations are close to the exact solution; middle: k−1 ≪ k2', the pre-equilibrium approximation fails completely and the steady-state approximation remains accurate; right: in the first case the intermediate concentration enters the quasi-steady state after an induction period of about 1/(k−1 + k2') and then follows the fall of [A]](./plots/steady-state-vs-full.py)

### 15.6.3. Separation of Time Scales and Stiffness

The mathematical essence of the steady-state approximation is the separation of fast and slow variables. The concentration of the intermediate approaches its quasi-steady value at the rate $k_{-1} + k_2[\ce{B}]$, and the reactant is consumed at the rate $v_{\mathrm{SS}}/[\ce{A}]$; the ratio of the two rates is the ratio of the two **eigenvalues** of the Jacobian matrix of the linearized system. When the ratio is large, the system exhibits **stiffness** ([4.4.4](/4.4.4#sec-4.3.3)): for stability, explicit methods (such as RK45, the default of `solve_ivp`) must take steps far smaller than the fast time scale, and the cost is proportional to the stiffness ratio; implicit methods (Radau, BDF, LSODA) can integrate with steps of the slow time scale. The steady-state approximation "eliminates" the fast variable, making the system nonstiff and often analytically solvable, at the price of losing detail in the induction period. The figure above was computed with `solve_ivp(..., method="Radau")`. The mechanisms of combustion chemistry and atmospheric chemistry contain hundreds or thousands of elementary reactions with stiffness ratios up to $10^{10}$, and numerical solution of the full system together with selective use of the steady-state approximation is everyday work in these fields.

## 15.7. Chain Reactions

### 15.7.1. Characteristics of Chain Reactions

**Definition 15.7.1** A reaction in which an active species (a radical or an atom) produced by heat, light, radiation or an initiator causes reactant molecules to undergo a series of successive reactions, the active species being continually regenerated so that the reaction proceeds automatically like a chain, is called a **chain reaction**; the active species that carries the reaction forward is called a **chain carrier**. A chain reaction comprises three stages:

1. **Chain initiation**: a stable molecule absorbs energy (heat, light or an initiator) and decomposes into chain carriers, as in $\ce{Cl2 + M -> 2Cl + M}$. This step breaks a chemical bond and has the largest activation energy, comparable to the bond energy broken.
2. **Chain propagation**: a chain carrier reacts with a stable molecule, forming product and at the same time a new chain carrier, as in $\ce{Cl + H2 -> HCl + H}$ and $\ce{H + Cl2 -> HCl + Cl}$. The activation energy of the reaction of a radical with a molecule is very small, so this step is fast and is repeated many times.
3. **Chain termination**: two chain carriers collide and combine into a stable molecule (a third body is needed to carry away energy), or collide with the wall and are deactivated, as in $\ce{2Cl + M -> Cl2 + M}$.

**Definition 15.7.2** An atom or group of atoms with an unpaired electron is called a **radical** (free radical), such as $\ce{Cl.}$, $\ce{H.}$, $\ce{CH3.}$ and $\ce{.OH}$. They are highly reactive and short-lived and are the chain carriers of chain reactions.

The number of propagation steps caused by one initiation is called the chain length. Chain carriers are sensitive to the wall and to impurities: changing the shape or material of the vessel, or adding a small amount of a radical scavenger (such as NO or phenolic antioxidants), may change the rate markedly; this is an experimental characteristic of chain reactions.

**Definition 15.7.3** A chain reaction in which each chain carrier consumed in propagation yields only one new chain carrier, so that the number of chain carriers remains constant, is called a **straight-chain reaction**; a chain reaction in which each chain carrier consumed yields two or more new chain carriers is called a **branched-chain reaction**.

### 15.7.2. A Straight-Chain Reaction: $\ce{H2 + Cl2}$

The experimental result is $-\frac{\mathrm{d}[\ce{H2}]}{\mathrm{d}t} = k[\ce{H2}][\ce{Cl2}]^{1/2}$. The mechanism and the activation energy of each step ($\mathrm{kJ\,mol^{-1}}$) are:

$$
\begin{aligned}
&(1)\ \ce{Cl2 + M ->[k_1] 2Cl + M} && E_1 = 243\\
&(2)\ \ce{Cl + H2 ->[k_2] HCl + H} && E_2 = 24\\
&(3)\ \ce{H + Cl2 ->[k_3] HCl + Cl} && E_3 = 13\\
&(4)\ \ce{2Cl + M ->[k_4] Cl2 + M} && E_4 = 0
\end{aligned}
$$

Apply the steady-state approximation to Cl and H (the concentration of M is included in the rate constants and omitted):

$$
\frac{\mathrm{d}[\ce{Cl}]}{\mathrm{d}t} = 2k_1[\ce{Cl2}] - k_2[\ce{Cl}][\ce{H2}] + k_3[\ce{H}][\ce{Cl2}] - 2k_4[\ce{Cl}]^2 = 0, \qquad \frac{\mathrm{d}[\ce{H}]}{\mathrm{d}t} = k_2[\ce{Cl}][\ce{H2}] - k_3[\ce{H}][\ce{Cl2}] = 0.
$$
Adding the two, the two propagation terms cancel: $k_1[\ce{Cl2}] = k_4[\ce{Cl}]^2$, that is, the rate of initiation equals the rate of termination, a general feature of the steady state of a straight-chain reaction. Thus $[\ce{Cl}] = (k_1/k_4)^{1/2}[\ce{Cl2}]^{1/2}$, and

$$
-\frac{\mathrm{d}[\ce{H2}]}{\mathrm{d}t} = k_2[\ce{Cl}][\ce{H2}] = k_2\left(\frac{k_1}{k_4}\right)^{1/2}[\ce{H2}][\ce{Cl2}]^{1/2},
$$
in agreement with experiment. The apparent activation energy is $E_{\mathrm{a}} = E_2 + \frac12(E_1 - E_4) = 145\,\mathrm{kJ\,mol^{-1}}$, much smaller than the bond energy of $\ce{Cl2}$. If $\ce{H2}$ and $\ce{Cl2}$ reacted directly by a four-centre molecular mechanism, $E_{\mathrm{a}} \approx 200\,\mathrm{kJ\,mol^{-1}}$ would be estimated; if the chain started from the dissociation of $\ce{H2}$, the initiation step would need $435\,\mathrm{kJ\,mol^{-1}}$. The chain pathway starting from the dissociation of $\ce{Cl2}$, which has the smallest bond energy, has the lowest activation energy, so the reaction proceeds by it. $\ce{H2 + Cl2}$ can explode in light, because photoinitiation produces a large number of Cl atoms and the chain length can reach $10^6$ ([6.3.17](/6.3.17)).

### 15.7.3. A Straight-Chain Reaction: $\ce{H2 + Br2}$

The rate law measured by Bodenstein and Lind in 1907 is

$$
\frac{\mathrm{d}[\ce{HBr}]}{\mathrm{d}t} = \frac{k[\ce{H2}][\ce{Br2}]^{1/2}}{1 + k'[\ce{HBr}]/[\ce{Br2}]},
$$
in which the product HBr inhibits the reaction and $\ce{Br2}$ weakens this inhibition; the mechanism was proposed only twelve years later, independently by Christiansen, Herzfeld and Polanyi:

$$
\begin{aligned}
&(1)\ \ce{Br2 + M ->[k_1] 2Br + M} &&\text{chain initiation}\\
&(2)\ \ce{Br + H2 ->[k_2] HBr + H} &&\text{chain propagation}\\
&(3)\ \ce{H + Br2 ->[k_3] HBr + Br} &&\text{chain propagation}\\
&(4)\ \ce{H + HBr ->[k_4] H2 + Br} &&\text{inhibition}\\
&(5)\ \ce{2Br + M ->[k_5] Br2 + M} &&\text{chain termination}
\end{aligned}
$$

Apply the steady-state approximation to H and Br:

$$
\frac{\mathrm{d}[\ce{H}]}{\mathrm{d}t} = k_2[\ce{Br}][\ce{H2}] - k_3[\ce{H}][\ce{Br2}] - k_4[\ce{H}][\ce{HBr}] = 0, \tag{15.4}
$$

$$
\frac{\mathrm{d}[\ce{Br}]}{\mathrm{d}t} = 2k_1[\ce{Br2}][\ce{M}] - k_2[\ce{Br}][\ce{H2}] + k_3[\ce{H}][\ce{Br2}] + k_4[\ce{H}][\ce{HBr}] - 2k_5[\ce{Br}]^2[\ce{M}] = 0. \tag{15.5}
$$

Adding Eqs. (15.4) and (15.5), all the propagation and inhibition terms cancel, $k_1[\ce{Br2}] = k_5[\ce{Br}]^2$, and the concentration of the third body drops out too:

$$
[\ce{Br}] = \left(\frac{k_1}{k_5}\right)^{1/2}[\ce{Br2}]^{1/2}.
$$
From Eq. (15.4),

$$
[\ce{H}] = \frac{k_2[\ce{Br}][\ce{H2}]}{k_3[\ce{Br2}] + k_4[\ce{HBr}]}.
$$
HBr is formed by steps (2) and (3) and consumed by step (4): $\frac{\mathrm{d}[\ce{HBr}]}{\mathrm{d}t} = k_2[\ce{Br}][\ce{H2}] + k_3[\ce{H}][\ce{Br2}] - k_4[\ce{H}][\ce{HBr}]$. Using Eq. (15.4) to replace the first term by $k_3[\ce{H}][\ce{Br2}] + k_4[\ce{H}][\ce{HBr}]$ gives $\frac{\mathrm{d}[\ce{HBr}]}{\mathrm{d}t} = 2k_3[\ce{H}][\ce{Br2}]$, and substituting $[\ce{H}]$ and $[\ce{Br}]$,

$$
\frac{\mathrm{d}[\ce{HBr}]}{\mathrm{d}t} = \frac{2k_2k_3[\ce{Br}][\ce{H2}][\ce{Br2}]}{k_3[\ce{Br2}] + k_4[\ce{HBr}]} = \frac{2k_2(k_1/k_5)^{1/2}[\ce{H2}][\ce{Br2}]^{1/2}}{1 + \dfrac{k_4[\ce{HBr}]}{k_3[\ce{Br2}]}},
$$
the same as the experimental law, with $k = 2k_2(k_1/k_5)^{1/2}$ and $k' = k_4/k_3$ (the experimental value is about $0.12$ and almost independent of temperature, indicating $E_3 \approx E_4$).

There are chemical reasons for the choice of steps in the mechanism (bond energies $D(\ce{H-H}) = 436$, $D(\ce{H-Br}) = 366$, $D(\ce{Br-Br}) = 193\,\mathrm{kJ\,mol^{-1}}$):

- Only the dissociation of $\ce{Br2}$ is considered for initiation; the bond energy of $\ce{H2}$ is much larger, and $\ce{H2 + M -> 2H + M}$ can be neglected.
- Step (2) is endothermic by about $70\,\mathrm{kJ\,mol^{-1}}$ and is the slowest step of the chain, so Br is the chain carrier of highest concentration, and only the recombination $\ce{2Br}$ is considered for termination. $\ce{Br + HBr -> Br2 + H}$ is endothermic by $173\,\mathrm{kJ\,mol^{-1}}$ and can be neglected.
- The H atom is very reactive and reacts exothermically with both $\ce{Br2}$ and HBr: step (4) competes with step (3) for H atoms and turns H back into the less reactive Br, which is the origin of the inhibition by HBr; the ratio $k_4[\ce{HBr}]/(k_3[\ce{Br2}])$ expresses the relative speed of the two competitors, so $\ce{Br2}$ can offset the inhibition by HBr.
- At the beginning of the reaction $[\ce{HBr}] \approx 0$, the rate is of order $\frac12$ in $\ce{Br2}$, the same form as for $\ce{H2 + Cl2}$.

The case of $\ce{H2 + I2}$ is different: the reaction of an I atom with $\ce{H2}$ is too endothermic, the chain cannot propagate, and the reaction proceeds by the mechanism in the table of 15.1.3. Treating the I atom by the steady-state approximation, $\frac{\mathrm{d}[\ce{I}]}{\mathrm{d}t} = 2k_1[\ce{I2}] - 2k_{-1}[\ce{I}]^2 - 2k_2[\ce{I}]^2[\ce{H2}] = 0$, gives $\frac12\frac{\mathrm{d}[\ce{HI}]}{\mathrm{d}t} = \frac{k_1k_2[\ce{I2}][\ce{H2}]}{k_{-1} + k_2[\ce{H2}]}$; for $k_{-1} \gg k_2[\ce{H2}]$ it reduces to the pre-equilibrium result $\frac{k_1k_2}{k_{-1}}[\ce{H2}][\ce{I2}]$.

### 15.7.4. Branched-Chain Reactions and Explosion Limits

The reaction of $\ce{H2 + O2}$ is the typical branched-chain reaction. After chain initiation produces H atoms,

$$
\ce{H + O2 -> OH + O}, \qquad \ce{O + H2 -> OH + H}, \qquad \ce{OH + H2 -> H2O + H},
$$
each of the first two steps consumes one chain carrier and generates two; the third step is carried out twice, and together with the first two, one H atom becomes three, that is, $\ce{H + O2 + 3H2 -> 2H2O + 3H}$. The number of chain carriers grows geometrically, and if termination cannot keep up, the reaction rate increases without bound in a very short time and a branched-chain explosion occurs.

Let the number density of chain carriers be $n$, the rate of initiation $w_0$, and the probabilities per unit time that a chain carrier branches and terminates $f$ and $g$, respectively. Then $\frac{\mathrm{d}n}{\mathrm{d}t} = w_0 + (f - g)n$:

- $g > f$: $n$ tends to the steady value $\frac{w_0}{g - f}$ and the reaction proceeds smoothly;
- $f > g$: $n \propto \mathrm{e}^{(f-g)t}$ grows exponentially and an explosion occurs.

$f = g$ is the critical condition for explosion. The probability of branching increases mainly with temperature ($\ce{H + O2 -> OH + O}$ is endothermic, with an activation energy of about $70\,\mathrm{kJ\,mol^{-1}}$), whereas the probability of termination varies with pressure in a complicated way, so whether an explosion occurs depends on temperature and pressure.

**Definition 15.7.4** The boundaries of the pressure interval within which an explosion occurs at a given temperature are called the **explosion limits**.

![Schematic of the explosion limits of a stoichiometric H2 + O2 mixture (log pressure against temperature): the "explosion peninsula" between the first and second limits is the region of branched-chain explosion, and above the third limit is the region of thermal explosion; only the shape is indicated, not measured data](./plots/explosion-limits.py)

1. First limit (lower explosion limit): at very low pressure, chain carriers diffuse to the wall and are deactivated before they collide with molecules and branch (termination at the wall, with a rate proportional to the diffusion coefficient and inversely proportional to pressure); $g > f$ and there is no explosion. The lower limit depends on the size and material of the vessel.
2. Between the first and second limits: termination at the wall weakens, branching exceeds termination, and an explosion occurs.
3. Second limit (upper explosion limit): as the pressure increases, the three-body recombination $\ce{H + O2 + M -> HO2 + M}$ speeds up (its rate is proportional to the square of the pressure, one pressure factor more than the branching $\ce{H + O2}$), the $\ce{HO2}$ formed is unreactive, the chain is terminated, and again there is no explosion. The upper limit rises with temperature and is independent of the vessel.
4. Third limit: at still higher pressure $\ce{HO2}$ also takes part in chain propagation, more heat is released, and a thermal explosion occurs.

Below about $730\,\mathrm{K}$, a stoichiometric mixture does not undergo a branched-chain explosion at any pressure (the exact temperature depends on the vessel).

**Definition 15.7.5** The explosion that occurs when an exothermic reaction proceeds in a confined space, the heat released cannot escape in time, and the temperature rises, the rate increases further and more heat is released until the rate increases without bound, is called a **thermal explosion**.

Semenov's analysis of the heat balance: the rate of heat generation increases with temperature according to the Arrhenius law $\propto \mathrm{e}^{-E_{\mathrm{a}}/RT}$, and the rate of heat loss is proportional to the temperature difference $T - T_0$. When the two curves intersect, the system stops at a stable steady state; criticality is reached when the two curves are just tangent, at which the temperature rise is about $RT_0^2/E_{\mathrm{a}}$ (only about $20\,\mathrm{K}$ for $E_{\mathrm{a}} = 150\,\mathrm{kJ\,mol^{-1}}$ and $T_0 = 600\,\mathrm{K}$). This is a saddle-node bifurcation: when a parameter (wall temperature, pressure) crosses its critical value, the stable steady state disappears ([2.4.11](/2.4.11)). Thermal runaway of a similar kind is also the root of the safety problem of lithium-ion batteries.

## 15.8. Proposing a Reaction Mechanism

### 15.8.1. General Steps

1. Write the stoichiometric equation of the reaction and determine the products (including by-products).
2. Determine the rate law by experiment and the order for each substance.
3. Measure the activation energy.
4. Detect intermediates and determine their composition by electron paramagnetic resonance (EPR, which detects radicals), nuclear magnetic resonance, mass spectrometry and transient spectroscopy in flash photolysis; if a radical lives too short a time, add a spin trap to convert it into a stable radical adduct for detection, or use isotopic labeling to trace the fate of atoms.
5. Propose a mechanism on the basis of chemical knowledge (bond energies, molecularity, steric factors).
6. Derive the rate law from the mechanism using approximations such as the rate-determining step, the steady state and pre-equilibrium, and compare it with experiment.
7. Calculate the apparent activation energy from the activation energies of the elementary steps and compare it with experiment.
8. If both agree, the mechanism is basically reasonable; otherwise modify it. Agreement shows only that the mechanism is "possibly" correct: the same rate law can be obtained from different mechanisms ([6.1.7](/6.1.7#sec-7.3.1), Question 4), and a mechanism can only be refuted and never finally proved.

### 15.8.2. Example: Thermal Decomposition of Ethane

$\ce{C2H6 -> C2H4 + H2}$ is a first-order reaction with $E_{\mathrm{a}} = 284.5\,\mathrm{kJ\,mol^{-1}}$, and $\ce{CH3}$ and $\ce{C2H5}$ radicals are detected.

**Definition 15.8.1 (Rice–Herzfeld Mechanism)** The free-radical chain mechanism of the thermal decomposition of organic compounds, in which the weakest bond in the molecule breaks to produce radicals (initiation), the radicals abstract hydrogen atoms from the molecule and the radicals so formed decompose into products and new radicals (propagation), and radicals recombine (termination), is called the **Rice–Herzfeld mechanism** (1934).

The Rice–Herzfeld mechanism of ethane and the activation energy of each step ($\mathrm{kJ\,mol^{-1}}$) are:

$$
\begin{aligned}
&(1)\ \ce{C2H6 ->[k_1] 2CH3} && 351.5\\
&(2)\ \ce{CH3 + C2H6 ->[k_2] CH4 + C2H5} && 33.5\\
&(3)\ \ce{C2H5 ->[k_3] C2H4 + H} && 167\\
&(4)\ \ce{H + C2H6 ->[k_4] H2 + C2H5} && 29.3\\
&(5)\ \ce{H + C2H5 ->[k_5] C2H6} && 0
\end{aligned}
$$

Apply the steady-state approximation to the three radicals (write $[\ce{C2H6}] = c$): $\ce{CH3}$ is formed only by (1) and consumed by (2), so $[\ce{CH3}] = 2k_1/k_2$. The steady-state equations for $\ce{C2H5}$ and H are

$$
k_2[\ce{CH3}]c - k_3[\ce{C2H5}] + k_4[\ce{H}]c - k_5[\ce{H}][\ce{C2H5}] = 0, \qquad k_3[\ce{C2H5}] - k_4[\ce{H}]c - k_5[\ce{H}][\ce{C2H5}] = 0
$$
and adding them gives $2k_1c = 2k_5[\ce{H}][\ce{C2H5}]$ (initiation = termination). Substituting $[\ce{H}] = \frac{k_1c}{k_5[\ce{C2H5}]}$ into the second equation gives a quadratic equation for $[\ce{C2H5}]$,

$$
k_3k_5[\ce{C2H5}]^2 - k_1k_5c[\ce{C2H5}] - k_1k_4c^2 = 0.
$$
Initiation is much slower than propagation ($k_1$ is very small and the chain is very long), so the linear term can be dropped, $[\ce{C2H5}] \approx \left(\frac{k_1k_4}{k_3k_5}\right)^{1/2}c$. The rate of formation of ethylene is

$$
v = k_3[\ce{C2H5}] = \left(\frac{k_1k_3k_4}{k_5}\right)^{1/2}[\ce{C2H6}],
$$
a first-order reaction, with apparent activation energy $E_{\mathrm{a}} = \frac12(E_1 + E_3 + E_4 - E_5) = 274\,\mathrm{kJ\,mol^{-1}}$, which agrees essentially with the experimental value of $284.5\,\mathrm{kJ\,mol^{-1}}$.

### 15.8.3. Example: Diazotization of Aniline

$\ce{H+ + HNO2 + C6H5NH2 -> C6H5N2+ + 2H2O}$, catalyzed by $\ce{Br-}$:

```smiles
Nc1ccccc1 C6H5NH2
N#[N+]c1ccccc1 C6H5N2+
```

The experimental rate law is $v = k[\ce{H+}][\ce{HNO2}][\ce{Br-}]$, independent of the concentration of aniline. A possible mechanism is:

$$
\begin{aligned}
&(1)\ \ce{H+ + HNO2 <=>[k_1][k_{-1}] H2NO2+} &&\text{fast equilibrium}\\
&(2)\ \ce{H2NO2+ + Br- ->[k_2] ONBr + H2O} &&\text{slow}\\
&(3)\ \ce{ONBr + C6H5NH2 ->[k_3] C6H5N2+ + H2O + Br-} &&\text{fast}
\end{aligned}
$$

The rate-determining step (2) gives $v = k_2[\ce{H2NO2+}][\ce{Br-}]$; from the pre-equilibrium $[\ce{H2NO2+}] = \frac{k_1}{k_{-1}}[\ce{H+}][\ce{HNO2}]$,

$$
v = \frac{k_1k_2}{k_{-1}}[\ce{H+}][\ce{HNO2}][\ce{Br-}].
$$
Aniline appears only in the fast reaction after the rate-determining step, so it does not appear in the rate law; $\ce{Br-}$ is consumed in (2) and regenerated in (3), so it is a catalyst, yet it appears in the rate law.

## 15.9. Fast Reactions and Relaxation Methods

### 15.9.1. The Limit of Mixing

The conventional method "mix, react, measure $c$–$t$" requires the reaction time to be much longer than the mixing time. For acid–base neutralization, electron transfer, and the binding of enzymes to substrates, the half-lives are below a millisecond, and the reaction is over before mixing is complete. There are two ways to measure such reactions: shorten the mixing time, or do not mix at all.

**Definition 15.9.1** The method in which two reactant solutions are forced by drive syringes into a mixing chamber and mixed within a few milliseconds, the flow is then stopped abruptly, and the change of concentration with time after the stop is monitored by spectroscopy or other means, is called the **stopped-flow method**. The dead time is about $1\,\mathrm{ms}$; it is suitable for reactions with half-lives of milliseconds or longer and is the routine technique of enzyme kinetics.

### 15.9.2. Relaxation Methods

**Definition 15.9.2** The method in which a fast opposing reaction at equilibrium is subjected to a sudden small perturbation (a jump in temperature, pressure or electric field), so that the system departs from equilibrium under the new conditions, and the process of its approach to the new equilibrium (relaxation) is measured and the rate constants are obtained from the speed of relaxation, is called the **relaxation method** (chemical relaxation). The method in which the temperature of the solution is raised by several kelvin within microseconds or nanoseconds by discharging a capacitor or by a laser pulse is called the **temperature-jump method**.

Relaxation methods need no mixing, and the time resolution is limited only by the speed of the perturbation itself. When the perturbation is small, the equations of the system can be linearized near the new equilibrium point ([2.4.11](/2.4.11#sec-11.3)), and the deviation decays exponentially.

**Formula 15.9.1 (Relaxation Time of a 1-1 Order Opposing Reaction)** For $\ce{A <=>[k_1][k_{-1}] B}$, let the concentration of B at the new equilibrium after the perturbation be $x_{\mathrm{eq}}$ and the deviation $\Delta x = x - x_{\mathrm{eq}}$. From $\frac{\mathrm{d}x}{\mathrm{d}t} = k_1(a - x) - k_{-1}x$ and the equilibrium condition $k_1(a - x_{\mathrm{eq}}) = k_{-1}x_{\mathrm{eq}}$,

$$
\frac{\mathrm{d}\Delta x}{\mathrm{d}t} = -(k_1 + k_{-1})\Delta x, \qquad \Delta x = \Delta x_0\,\mathrm{e}^{-t/\tau}, \qquad \frac{1}{\tau} = k_1 + k_{-1}.
$$
The time $\tau$ for the deviation to fall to $1/\mathrm{e}$ of its initial value is called the **relaxation time**.

From $\tau$ one obtains $k_1 + k_{-1}$, and the equilibrium constant $K = k_1/k_{-1}$ (which can be determined by conventional methods) then gives $k_1$ and $k_{-1}$ separately. This result is the same as Eq. (15.1), except that the "perturbation" there was the start from pure A.

For $\ce{A + B <=>[k_1][k_{-1}] C}$, let $[\ce{C}] = [\ce{C}]_{\mathrm{eq}} + \Delta x$, so that $[\ce{A}] = [\ce{A}]_{\mathrm{eq}} - \Delta x$ and $[\ce{B}] = [\ce{B}]_{\mathrm{eq}} - \Delta x$:

$$
\frac{\mathrm{d}\Delta x}{\mathrm{d}t} = k_1([\ce{A}]_{\mathrm{eq}} - \Delta x)([\ce{B}]_{\mathrm{eq}} - \Delta x) - k_{-1}([\ce{C}]_{\mathrm{eq}} + \Delta x) \approx -\left[k_1([\ce{A}]_{\mathrm{eq}} + [\ce{B}]_{\mathrm{eq}}) + k_{-1}\right]\Delta x,
$$
where the equilibrium condition was used and the $(\Delta x)^2$ term dropped, so $\frac{1}{\tau} = k_1([\ce{A}]_{\mathrm{eq}} + [\ce{B}]_{\mathrm{eq}}) + k_{-1}$. Measuring $\tau$ at different total concentrations and plotting $1/\tau$ against $[\ce{A}]_{\mathrm{eq}} + [\ce{B}]_{\mathrm{eq}}$ gives $k_1$ as the slope and $k_{-1}$ as the intercept. For opposing reactions of different orders the relation between $\tau$ and the rate constants differs and must be derived case by case; when a mechanism comprises several steps there are several relaxation times, corresponding to the several eigenvalues of the linearized matrix (15.4.4).

![Temperature-jump experiment for A + B ⇌ C (k1 = 1.0 × 10⁹ L mol⁻¹ s⁻¹, k−1 = 1.0 × 10⁴ s⁻¹): left, the relaxation of [C] to the new equilibrium after the jump; right, the logarithmic decay of the deviation; the full nonlinear equation and the exp(−t/τ) from linearization almost coincide](./plots/temperature-jump.py)

**Example 15.9.1** Eigen measured by the electric-field jump method the rate constant of $\ce{H+ + OH- -> H2O}$ at $25\,^\circ\mathrm{C}$, $k_1 = 1.4 \times 10^{11}\,\mathrm{L\,mol^{-1}\,s^{-1}}$. What is the relaxation time of pure water?

**Solution** The rate constant of the reverse reaction (dissociation of water) is $k_{-1} = k_1K_{\mathrm{w}}/[\ce{H2O}] \approx 1.4 \times 10^{11} \times 10^{-14}/55.3\,\mathrm{s^{-1}} \approx 2.5 \times 10^{-5}\,\mathrm{s^{-1}}$, which can be neglected. With $[\ce{H+}]_{\mathrm{eq}} = [\ce{OH-}]_{\mathrm{eq}} = 1.0 \times 10^{-7}\,\mathrm{mol\,L^{-1}}$,

$$
\tau = \frac{1}{k_1([\ce{H+}] + [\ce{OH-}])} = \frac{1}{1.4 \times 10^{11} \times 2.0 \times 10^{-7}}\,\mathrm{s} \approx 36\,\mu\mathrm{s}.
$$
This is one of the fastest bimolecular reactions in solution known, an order of magnitude larger than the general estimate of the diffusion-controlled rate constant in [6.3.17](/6.3.17), because the two ions attract each other and the proton can be "relayed" along the hydrogen-bond network by the Grotthuss mechanism.

### 15.9.3. Flash Photolysis

**Definition 15.9.3** The method in which a single intense, short flash of light (nowadays a pulsed laser) photolyzes molecules to produce a high concentration of radicals, atoms or excited molecules, and the decay of the concentration of these transient species is then monitored by absorption spectroscopy or the like, is called **flash photolysis**.

Flash photolysis was developed by Norrish and Porter in 1949; Eigen (relaxation methods) and Norrish and Porter (flash photolysis) shared the 1967 Nobel Prize in Chemistry. The intensity of the flash is very high and can produce concentrations of transient species many times higher than in conventional reactions, so that many intermediates never seen before were directly detected for the first time. Flash lamps were used at first, with microsecond time resolution; nanosecond and picosecond lasers pushed it to the time scale of molecular vibration, the femtochemistry mentioned in [6.3.16](/6.3.16). The connection between flash photolysis and photochemistry is in [6.3.17](/6.3.17).

| Method | Time range | Principle |
|---|---|---|
| Conventional mixing | $> 10\,\mathrm{s}$ | Sampling or continuous monitoring after mixing |
| Stopped flow | $10^{-3}$–$10\,\mathrm{s}$ | Flow stopped after rapid mixing |
| Temperature jump, pressure jump | $10^{-8}$–$1\,\mathrm{s}$ | Relaxation observed after perturbing equilibrium |
| Flash photolysis | $10^{-12}$–$10^{-3}\,\mathrm{s}$ (down to $10^{-14}\,\mathrm{s}$ with lasers) | Light pulse produces transient species |

## Summary

| Topic | Key points |
|---|---|
| $n$th-order reactions | $\frac{1}{c^{n-1}} - \frac{1}{c_0^{n-1}} = (n-1)kt$, $t_{1/2} \propto c_0^{1-n}$; $k_p = k_c(RT)^{1-n}$ |
| Determining the order | Integral, half-life, differential, initial-rate and isolation methods; prefer direct nonlinear fitting |
| Opposing reactions | The deviation from equilibrium decays at $k_1 + k_{-1}$; $k_1/k_{-1} = K$ |
| Parallel reactions | For equal orders the product ratio is $k_1/k_2$, adjusted by temperature and catalyst |
| Consecutive reactions | The intermediate has a maximum at $t_{\max} = \frac{\ln(k_2/k_1)}{k_2 - k_1}$; the slowest step is rate-determining |
| Linear networks | $\dot{\boldsymbol{c}} = K\boldsymbol{c}$, $\boldsymbol{c}(t) = \mathrm{e}^{tK}\boldsymbol{c}(0)$, the eigenvalues give the time scales |
| Detailed balance | At equilibrium the forward and reverse rates of every elementary step are equal; $k_1/k_{-1} = K_c$, $E_{\mathrm{a},1} - E_{\mathrm{a},-1} = \Delta_{\mathrm{r}}U_{\mathrm{m}}$ |
| Apparent activation energy | Algebraic sum of the activation energies of the steps, can be negative |
| Approximation methods | Rate-determining step; steady-state approximation (short-lived intermediate); pre-equilibrium approximation (fast equilibrium of an earlier step); mathematically a separation of fast and slow variables, corresponding to stiff systems |
| Chain reactions | Initiation, propagation, termination; in a straight-chain steady state initiation = termination; in $\ce{H2 + Br2}$ the inhibition by HBr comes from the competition of $\ce{H + HBr}$ and $\ce{H + Br2}$ |
| Branching and explosion | $\dot n = w_0 + (f - g)n$; three explosion limits; thermal explosion |
| Fast reactions | Stopped flow; relaxation $1/\tau = k_1 + k_{-1}$ (linearized); flash photolysis |

## Questions

1. For the 2-2 order parallel reactions $\ce{A ->[k_1] B}$ and $\ce{A ->[k_2] C}$ (both second order in A) with $E_{\mathrm{a},1} > E_{\mathrm{a},2}$, starting from pure A, which of the following measures can change the ratio of the products B and C? (1) raising the temperature; (2) prolonging the reaction time; (3) adding a suitable catalyst; (4) lowering the temperature; (5) raising the initial concentration of A.

   **Answer** (1), (3) and (4). The two reactions have the same order, $[\ce{B}]/[\ce{C}] = k_1/k_2$ depends only on temperature and catalyst, and time and initial concentration do not change this ratio.

2. For a given reaction, can adding a catalyst change the order of reaction?

   **Answer** It can. The catalyst changes the mechanism, the rate law may be entirely different, and the catalyst itself often appears in the rate law ($\ce{Br-}$ in 15.8.3).

3. Why is the rate of a chain reaction sensitive to the shape and wall material of the vessel?

   **Answer** Chain carriers can be deactivated at the wall, and the rate of termination at the wall depends on the specific surface area and the nature of the wall; for branched-chain reactions the first explosion limit is determined by termination at the wall.

4. Does a negative apparent activation energy of a reaction contradict the statement that "the activation energy is an energy barrier"?

   **Answer** It does not. The activation energy of an elementary reaction is positive; the apparent activation energy is the algebraic sum of the activation energies of the steps and can be negative when the pre-equilibrium is exothermic (15.5.4).
