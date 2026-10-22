---
title: Multicomponent Systems and the Chemical Potential
source_hash: 76929f8e77cc
---

The first three chapters dealt with systems of constant composition: a fixed amount of a pure substance whose state is fixed by two variables (such as $T$ and $p$). Chemistry, however, is concerned with systems whose composition changes: solutions, gas mixtures, reactions and phase transitions in progress. When the composition can vary, the extensive properties of a system are no longer equal to the sums of the properties of the pure components ($50\,\mathrm{mL}$ of water mixed with $50\,\mathrm{mL}$ of ethanol give less than $100\,\mathrm{mL}$), and the fundamental equations of thermodynamics must acquire a term reflecting the changes in the amounts of substances. This chapter first gives the classification of multicomponent systems and the ways of expressing composition (4.1), and then introduces partial molar quantities and their two basic properties, the additivity formula and the Gibbs–Duhem equation (4.2). The partial molar Gibbs energy is the chemical potential, which extends the four fundamental equations of [6.3.3](/6.3.3) to systems of variable composition and provides a unified criterion for mass transfer (diffusion, phase change, chemical reaction) (4.3). Finally we write the chemical potentials of the various gases and treat real gases with the fugacity (4.4). The content discussed informally in terms of "molar Gibbs energy" in [6.1.8](/6.1.8) acquires its rigorous form here. This chapter is the starting point of solution thermodynamics: the chemical potentials of components in liquid mixtures and dilute solutions ([6.3.5](/6.3.5), [6.3.6](/6.3.6)) are written by means of the gas phase in equilibrium with them; the conditions of chemical equilibrium ([6.3.7](/6.3.7)) and phase equilibrium ([6.3.8](/6.3.8)) are relations among chemical potentials; and the mean activity and electrochemical potential of electrolyte solutions and electrochemistry ([6.3.12](/6.3.12), [6.3.13](/6.3.13)) also start from here. In biology, transmembrane transport and osmosis are likewise driven by differences of chemical potential.

## 4.1. Multicomponent Systems and Their Composition

### 4.1.1. Mixtures and Solutions

A single-component homogeneous system has fixed composition and is a two-variable system. A system containing two or more substances is called a multicomponent system; it may be homogeneous (a solution, a gas mixture) or heterogeneous (a solution and its vapor). This chapter treats multicomponent homogeneous systems, in which each substance is dispersed in the others as molecules, atoms or ions and the composition can vary continuously within some range. By the method of treatment they fall into two classes.

**Definition 4.1.1** A multicomponent homogeneous system in which all components are treated by the same method, obey the same empirical laws and are given the same standard state is called a **mixture**; one in which the components are divided into **solvent** and **solute**, which obey different empirical laws and have different standard states, is called a **solution**.

Mixtures may be gaseous, liquid or solid (**solid solutions**, [6.1.4](/6.1.4)). In a solution, if the components are in different states of aggregation, the liquid substance is usually called the solvent and the gas or solid dissolved in it the solute; if all are liquids, the one in larger amount is generally called the solvent. This distinction is not a property of the substances themselves but a choice of treatment: the same water–ethanol system is treated as a mixture when discussed over the whole range of concentrations, and as a solution when only a little ethanol dissolved in water is discussed.

### 4.1.2. Expressing Composition

Composition is an intensive property of a multicomponent homogeneous system. Four quantities are in common use to describe the content of substance B (A denotes the solvent):

**Definition 4.1.2** Let the amount of substance of B in the system be $n_{\mathrm{B}}$, its mass $m_{\mathrm{B}}$, the volume of the system $V$ and the mass of solvent A $m_{\mathrm{A}}$. The quantities

$$
w_{\mathrm{B}} = \frac{m_{\mathrm{B}}}{\sum_{\mathrm{C}}m_{\mathrm{C}}}, \qquad c_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{V}, \qquad b_{\mathrm{B}} = \frac{n_{\mathrm{B}}}{m_{\mathrm{A}}}
$$
are called the **mass fraction**, the **amount concentration** and the **molality** of B respectively, the last two being commonly expressed in $\mathrm{mol\,L^{-1}}$ and $\mathrm{mol\,kg^{-1}}$.

Together with the **mole fraction** $x_{\mathrm{B}} = n_{\mathrm{B}}/\sum_{\mathrm{C}}n_{\mathrm{C}}$ ([6.1.1](/6.1.1); often written $y_{\mathrm{B}}$ for the gas phase) there are four in all. $x_{\mathrm{B}}$, $w_{\mathrm{B}}$ and $b_{\mathrm{B}}$ are fixed by weighing and do not change with temperature; $c_{\mathrm{B}}$ depends on the volume of the solution and varies with temperature. Molality allows accurate preparation and is the most used in electrochemistry and colligative properties, with the standard value $b^\circ = 1\,\mathrm{mol\,kg^{-1}}$; the standard value of the amount concentration is $c^\circ = 1\,\mathrm{mol\,L^{-1}}$ ([6.1.6](/6.1.6#sec-6.3.3)).

For conversions, compute with a convenient quantity of solution. For a two-component solution,

$$
x_{\mathrm{B}} = \frac{b_{\mathrm{B}}M_{\mathrm{A}}}{1 + b_{\mathrm{B}}M_{\mathrm{A}}}, \qquad c_{\mathrm{B}} = \frac{\rho\,b_{\mathrm{B}}}{1 + b_{\mathrm{B}}M_{\mathrm{B}}},
$$
where $\rho$ is the density of the solution and $M$ the molar mass. In a very dilute solution $x_{\mathrm{B}} \approx b_{\mathrm{B}}M_{\mathrm{A}}$ and $c_{\mathrm{B}} \approx \rho_{\mathrm{A}}b_{\mathrm{B}}$, and the various concentrations are proportional to one another; for aqueous solutions $\rho_{\mathrm{A}} \approx 1\,\mathrm{kg\,L^{-1}}$ and the numerical values of $c_{\mathrm{B}}$ and $b_{\mathrm{B}}$ are almost the same.

**Example 4.1.1** A sulfuric acid solution with $w(\ce{H2SO4}) = 5\%$ has density $1.032\,\mathrm{g\,cm^{-3}}$ at $20\,^\circ\mathrm{C}$. Take $100\,\mathrm{g}$ of solution: $n(\ce{H2SO4}) = 5/98.08\,\mathrm{mol} = 0.0510\,\mathrm{mol}$ and $n(\ce{H2O}) = 95/18.015\,\mathrm{mol} = 5.273\,\mathrm{mol}$, so $x = 0.0096$, $b = 0.0510/0.095\,\mathrm{mol\,kg^{-1}} = 0.537\,\mathrm{mol\,kg^{-1}}$ and $c = 0.0510\,\mathrm{mol}/(100\,\mathrm{g}/1.032\,\mathrm{g\,cm^{-3}}) = 0.526\,\mathrm{mol\,L^{-1}}$.

## 4.2. Partial Molar Quantities

### 4.2.1. Nonadditivity of Extensive Properties

For a pure substance $V = nV^*_{\mathrm{m}}(T, p)$: an extensive property equals the amount of substance times the molar quantity (the asterisk denotes a pure substance). A multicomponent system is not like this. The following table gives the volume of $100\,\mathrm{g}$ of water (A)–ethanol (B) solution at $20\,^\circ\mathrm{C}$ and the sum of the volumes of the two pure liquids before mixing (calculated from the density data of the CRC Handbook):

| $w_{\mathrm{B}}$ | $V^*(\text{ethanol})/\mathrm{cm^3}$ | $V^*(\text{water})/\mathrm{cm^3}$ | Sum before mixing$/\mathrm{cm^3}$ | Solution $V/\mathrm{cm^3}$ |
|---|---|---|---|---|
| 20% | 25.34 | 80.14 | 105.48 | 103.24 |
| 40% | 50.68 | 60.11 | 110.79 | 106.93 |
| 60% | 76.02 | 40.07 | 116.09 | 112.22 |
| 80% | 101.36 | 20.04 | 121.40 | 118.56 |

The volume of the solution is always smaller than the sum before mixing, because hydrogen bonds between water and ethanol pack the molecules more tightly. In general the extensive properties of a multicomponent system (except mass and amount of substance) are not equal to the sums of the properties of the pure components. For a homogeneous system of $k$ components an extensive property is therefore a function of $k + 2$ variables, $X = X(T, p, n_1, \dots, n_k)$, and an intensive property a function of $k + 1$ variables ($T$, $p$ and $k - 1$ independent mole fractions).

### 4.2.2. Definition of Partial Molar Quantities

The total differential of $X$ is

$$
\mathrm{d}X = \left(\frac{\partial X}{\partial T}\right)_{p,n}\mathrm{d}T + \left(\frac{\partial X}{\partial p}\right)_{T,n}\mathrm{d}p + \sum_{\mathrm{B}}\left(\frac{\partial X}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}\mathrm{d}n_{\mathrm{B}},
\tag{4.1}
$$
where the subscript $n$ means that the amounts of all substances are held constant and $n_{\mathrm{C}}$ that the amounts of all substances other than B are held constant.

**Definition 4.2.1 (Partial Molar Quantity)** Let $X$ be an extensive property of a multicomponent homogeneous system. The quantity

$$
X_{\mathrm{B}} = \left(\frac{\partial X}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}
$$
is called the **partial molar quantity** of substance B. For $X = V$ it is called the **partial molar volume** $V_{\mathrm{B}}$ of B; likewise there are the partial molar internal energy $U_{\mathrm{B}}$, enthalpy $H_{\mathrm{B}}$, entropy $S_{\mathrm{B}}$, Helmholtz energy $A_{\mathrm{B}}$ and Gibbs energy $G_{\mathrm{B}}$.

The physical meaning of $V_{\mathrm{B}}$ can be stated in two equivalent ways: the rate of change of the volume of the system with the amount of B at constant $T$, $p$ and amounts of the other components; or the increase of volume of the system when $1\,\mathrm{mol}$ of B is added to a very large system of given composition (so that the composition is almost unchanged). In using it note that:

1. Only extensive properties have partial molar quantities; intensive properties such as $C_{p,\mathrm{m}}$ do not.
2. The subscripts must be $T$, $p$, $n_{\mathrm{C}}$. Partial derivatives with respect to $n_{\mathrm{B}}$ at constant $T$, $V$ or $S$, $p$ (such as $(\partial H/\partial n_{\mathrm{B}})_{S,p,n_{\mathrm{C}}}$) are not partial molar quantities.
3. A partial molar quantity is the ratio of two extensive quantities, an intensive property fixed by $T$, $p$ and composition and independent of the size of the system; it is a property of the solution as a whole and not of the B molecules themselves.
4. Partial molar quantities are defined only for homogeneous systems: the total volume of a two-phase (gas and liquid) water–ethanol system has no partial molar volume, but each phase has its own partial molar quantities.
5. For a pure substance $X_{\mathrm{B}} = X^*_{\mathrm{m,B}}$; in general $X_{\mathrm{B}} \ne X^*_{\mathrm{m,B}}$, and it can even be negative. For example, the partial molar volume of $\ce{MgSO4}$ in infinitely dilute aqueous solution is about $-1.4\,\mathrm{cm^3\,mol^{-1}}$: the ions pack the surrounding water molecules more tightly (electrostriction), and adding the salt decreases the total volume of the solution.

### 4.2.3. The Additivity Formula

**Theorem 4.2.1 (Additivity Formula for Partial Molar Quantities)** An extensive property of a multicomponent homogeneous system equals the sum over components of the amount of each component times its partial molar quantity:

$$
X = \sum_{\mathrm{B}}n_{\mathrm{B}}X_{\mathrm{B}}.
\tag{4.2}
$$

**Proof** At constant $T$ and $p$, multiplying the amount of every component by $\lambda$ enlarges the system by a factor $\lambda$ with the composition unchanged: $X(T, p, \lambda n_1, \dots, \lambda n_k) = \lambda X(T, p, n_1, \dots, n_k)$. That is, $X$ is a first-degree **homogeneous function** of $n_1, \dots, n_k$. By Euler's theorem on homogeneous functions ([2.2.10, Theorem 10.7.2](/2.2.10#thm-10.7.2), the case of degree one), $\sum_{\mathrm{B}}n_{\mathrm{B}}(\partial X/\partial n_{\mathrm{B}}) = X$. $\square$

It can also be understood as follows: at constant $T$ and $p$, add the components simultaneously in the proportions of the final composition; the composition stays the same throughout, every $X_{\mathrm{B}}$ is constant, and integrating $\mathrm{d}X = \sum_{\mathrm{B}}X_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ gives Eq. (4.2). Eq. (4.2) shows that partial molar quantities are the only self-consistent way of "apportioning" an extensive property of the system among the components; but $n_{\mathrm{B}}V_{\mathrm{B}}$ is not the volume that B actually occupies in the solution (it can be negative). The same holds for other partial molar quantities, $G = \sum_{\mathrm{B}}n_{\mathrm{B}}G_{\mathrm{B}}$, $H = \sum_{\mathrm{B}}n_{\mathrm{B}}H_{\mathrm{B}}$ and so on, and the relations among defining equations carry over to partial molar quantities, for example $G_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$ (differentiate $G = H - TS$ with respect to $n_{\mathrm{B}}$ at constant $T$, $p$, $n_{\mathrm{C}}$).

Dividing by the total amount of substance $n$ gives the average molar quantity $X_{\mathrm{m}} = X/n = \sum_{\mathrm{B}}x_{\mathrm{B}}X_{\mathrm{B}}$. For a two-component system the partial molar quantities can be found from the $X_{\mathrm{m}}$–$x_{\mathrm{B}}$ curve by the intercept method:

$$
X_{\mathrm{A}} = X_{\mathrm{m}} - x_{\mathrm{B}}\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}, \qquad X_{\mathrm{B}} = X_{\mathrm{m}} + (1 - x_{\mathrm{B}})\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}.
\tag{4.3}
$$
That is, draw the tangent to the curve at the composition $x_{\mathrm{B}}$; its intercepts at $x_{\mathrm{B}} = 0$ and $x_{\mathrm{B}} = 1$ are $X_{\mathrm{A}}$ and $X_{\mathrm{B}}$ respectively. Proof: $X = nX_{\mathrm{m}}(x_{\mathrm{B}})$ and $x_{\mathrm{B}} = n_{\mathrm{B}}/(n_{\mathrm{A}} + n_{\mathrm{B}})$; differentiating with respect to $n_{\mathrm{B}}$ at constant $n_{\mathrm{A}}$, $(\partial x_{\mathrm{B}}/\partial n_{\mathrm{B}})_{n_{\mathrm{A}}} = (1 - x_{\mathrm{B}})/n$, so $X_{\mathrm{B}} = X_{\mathrm{m}} + n\,\frac{\mathrm{d}X_{\mathrm{m}}}{\mathrm{d}x_{\mathrm{B}}}\cdot\frac{1 - x_{\mathrm{B}}}{n}$; $X_{\mathrm{A}}$ follows from the additivity formula $X_{\mathrm{m}} = x_{\mathrm{A}}X_{\mathrm{A}} + x_{\mathrm{B}}X_{\mathrm{B}}$.

![Average molar volume of water–ethanol solutions computed from the data in the table above, with the intercept method (left); the changes of the partial molar volumes of the two components relative to the molar volumes of the pure liquids, obtained after fitting the excess volume with a two-parameter Redlich–Kister expression (right). With only four data points the fit is unreliable in the region of very dilute ethanol (x_B < 0.05, not drawn).](./plots/ethanol-water-volume.py)

### 4.2.4. The Gibbs–Duhem Equation

The partial molar quantities of the components are not independent.

**Theorem 4.2.2 (Gibbs–Duhem Equation)** In a multicomponent homogeneous system,

$$
\sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = \left(\frac{\partial X}{\partial T}\right)_{p,n}\mathrm{d}T + \left(\frac{\partial X}{\partial p}\right)_{T,n}\mathrm{d}p.
\tag{4.4}
$$
In particular, at constant $T$ and $p$,

$$
\sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0, \qquad \sum_{\mathrm{B}}x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0.
\tag{4.5}
$$

**Proof** Take the total differential of the additivity formula (4.2): $\mathrm{d}X = \sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} + \sum_{\mathrm{B}}X_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$. Comparison with Eq. (4.1) gives Eq. (4.4). $\square$

The additivity formula is a relation between $X$ and $X_{\mathrm{B}}$ in one state; the Gibbs–Duhem equation constrains how the partial molar quantities change when the composition changes. In a two-component system $x_{\mathrm{A}}\,\mathrm{d}X_{\mathrm{A}} = -x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}}$: when one increases the other must decrease, both have extrema at the same composition, and the magnitudes of the changes are inversely proportional to the mole fractions (right panel of the figure above). Knowing how the partial molar quantity of one component varies with composition allows that of the other to be found; this is also the basis for testing the thermodynamic consistency of experimental data ([6.3.6](/6.3.6)).

**Example 4.2.1** At $298\,\mathrm{K}$ the partial molar volume of $\ce{K2SO4}$ (B) in aqueous solution depends on the molality $b$ as $V_{\mathrm{B}}/(\mathrm{cm^3\,mol^{-1}}) = 32.280 + 18.216\,(b/b^\circ)^{1/2}$. Find the partial molar volume of water (A).

**Solution** From Eq. (4.5), $\mathrm{d}V_{\mathrm{A}} = -(n_{\mathrm{B}}/n_{\mathrm{A}})\,\mathrm{d}V_{\mathrm{B}}$, and $n_{\mathrm{B}}/n_{\mathrm{A}} = bM_{\mathrm{A}}$. Write $\beta = b/b^\circ$; $\mathrm{d}V_{\mathrm{B}} = 9.108\,\beta^{-1/2}\,\mathrm{d}\beta\ \mathrm{cm^3\,mol^{-1}}$, so

$$
V_{\mathrm{A}} - V^*_{\mathrm{m,A}} = -\int_0^{\beta}\beta' b^\circ M_{\mathrm{A}}\cdot 9.108\,\beta'^{-1/2}\,\mathrm{d}\beta' = -6.072\,b^\circ M_{\mathrm{A}}\,\beta^{3/2}\ \mathrm{cm^3\,mol^{-1}},
$$
where $b^\circ M_{\mathrm{A}} = 0.018015$ (dimensionless). With $V^*_{\mathrm{m,A}} = 18.068\,\mathrm{cm^3\,mol^{-1}}$, for example at $b = 0.5\,\mathrm{mol\,kg^{-1}}$, $V_{\mathrm{A}} = (18.068 - 0.039)\,\mathrm{cm^3\,mol^{-1}} = 18.029\,\mathrm{cm^3\,mol^{-1}}$. The partial molar volume of the solute changes greatly (from 32.3 to 45.2), while that of the solvent changes by only two parts per thousand, a consequence of $x_{\mathrm{A}}\gg x_{\mathrm{B}}$. $\square$

## 4.3. The Chemical Potential

### 4.3.1. Definition

**Definition 4.3.1 (Chemical Potential)** The partial molar Gibbs energy of substance B in a multicomponent system,

$$
\mu_{\mathrm{B}} = G_{\mathrm{B}} = \left(\frac{\partial G}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}},
$$
is called the **chemical potential** of B, with the unit $\mathrm{J\,mol^{-1}}$.

The chemical potential was introduced by Gibbs in 1876. As a partial molar quantity it satisfies the additivity formula and the Gibbs–Duhem equation:

$$
G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}, \qquad \sum_{\mathrm{B}}x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0 \quad (\text{constant } T, p).
$$
The chemical potential of a pure substance is its molar Gibbs energy, $\mu^*_{\mathrm{B}} = G^*_{\mathrm{m,B}}$. Among all partial molar quantities the chemical potential has a special position: it determines the direction in which substances are transferred between phases and between reactants and products (4.3.3).

### 4.3.2. Fundamental Equations for Systems of Variable Composition

Regard $G$ as a function of $T$, $p$, $n_1, \dots, n_k$. At constant composition it satisfies $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p$ ([6.3.3, Theorem 3.2.1](/6.3.3)), so $(\partial G/\partial T)_{p,n} = -S$ and $(\partial G/\partial p)_{T,n} = V$, and hence

$$
\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}.
\tag{4.6}
$$
Differentiating $U = G - pV + TS$, $H = G + TS$ and $A = G - pV$ and substituting Eq. (4.6) gives three more equations:

**Theorem 4.3.1 (Fundamental Equations for Systems of Variable Composition)** For a system that does only expansion work and in which $T$ and $p$ are uniform within each phase,

$$
\begin{aligned}
\mathrm{d}U &= T\,\mathrm{d}S - p\,\mathrm{d}V + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}H &= T\,\mathrm{d}S + V\,\mathrm{d}p + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, \\
\mathrm{d}A &= -S\,\mathrm{d}T - p\,\mathrm{d}V + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}, &
\mathrm{d}G &= -S\,\mathrm{d}T + V\,\mathrm{d}p + \textstyle\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}.
\end{aligned}
\tag{4.7}
$$
Hence the chemical potential has four equivalent representations:

$$
\mu_{\mathrm{B}} = \left(\frac{\partial G}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}} = \left(\frac{\partial U}{\partial n_{\mathrm{B}}}\right)_{S,V,n_{\mathrm{C}}} = \left(\frac{\partial H}{\partial n_{\mathrm{B}}}\right)_{S,p,n_{\mathrm{C}}} = \left(\frac{\partial A}{\partial n_{\mathrm{B}}}\right)_{T,V,n_{\mathrm{C}}}.
$$

The last three are partial derivatives "at constant natural variables of the function and constant amounts of the other components"; they all equal the chemical potential, but none is a partial molar quantity. Only the first is also a partial molar quantity. Unless stated otherwise, the chemical potential means the partial molar Gibbs energy.

On the conditions of validity: Eq. (4.7) applies to open systems; for a closed system undergoing phase change or chemical reaction it applies equally if each phase (or the reaction mixture) is regarded as a subsystem of variable composition ("closed overall, open in parts"). It is an identity between neighboring equilibrium states, and as long as the interior of each phase is in thermal and mechanical equilibrium, whether the transfer of matter between phases or the chemical reaction within a phase is reversible does not affect its validity; the differences among chemical potentials are precisely the source of the irreversibility of these processes. The term $\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ removes the restriction in [6.3.3](/6.3.3) that "the fundamental equations apply only to reversible chemical change": when the composition is unchanged, or the chemical potentials have reached equilibrium ($\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} = 0$), Eq. (4.7) returns to the form for constant composition.

Applying Euler's theorem to $U$ ($U$ is a first-degree homogeneous function of $S$, $V$, $n_{\mathrm{B}}$) also gives $U = TS - pV + \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}$, that is, $G = \sum_{\mathrm{B}}n_{\mathrm{B}}\mu_{\mathrm{B}}$; comparing its differential with Eq. (4.7) gives the general form of the Gibbs–Duhem equation

$$
S\,\mathrm{d}T - V\,\mathrm{d}p + \sum_{\mathrm{B}}n_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0.
\tag{4.8}
$$
It shows that of the $k + 2$ intensive quantities $T$, $p$, $\mu_1, \dots, \mu_k$ in one homogeneous phase, only $k + 1$ are independent, which is the starting point for counting degrees of freedom in the phase rule ([6.3.8](/6.3.8)).

**Example 4.3.1** $\ce{H2}$ and $\ce{O2}$ react to form water vapor in an adiabatic rigid container. In the process $Q = 0$ and $W = 0$, $\mathrm{d}U = 0$ and $\mathrm{d}V = 0$. From Eq. (4.7),

$$
T\,\mathrm{d}S = -\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} = -\Big(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\Big)\mathrm{d}\xi > 0.
$$
With no heat exchange the entropy of the system nevertheless increases: the entropy gained is produced entirely by the irreversibility of the reaction, and $-\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ is the driving force of the reaction (called the **affinity** of the reaction). Wrongly applying $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ for constant composition would give $\mathrm{d}S = 0$. The quantity $-\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}/T$ here is the entropy production due to chemical reaction in [6.3.18](/6.3.18).

### 4.3.3. The Chemical Potential Criterion

Consider first the simplest mass-transfer process. At constant temperature and pressure with $W' = 0$, let an amount $\mathrm{d}n_{\mathrm{B}} > 0$ of substance B be transferred from phase $\alpha$ to phase $\beta$, with everything else unchanged. From Eq. (4.6),

$$
\mathrm{d}G = \mathrm{d}G^\alpha + \mathrm{d}G^\beta = -\mu_{\mathrm{B}}^\alpha\,\mathrm{d}n_{\mathrm{B}} + \mu_{\mathrm{B}}^\beta\,\mathrm{d}n_{\mathrm{B}} = (\mu_{\mathrm{B}}^\beta - \mu_{\mathrm{B}}^\alpha)\,\mathrm{d}n_{\mathrm{B}}.
$$
By the Gibbs criterion, when $\mu_{\mathrm{B}}^\beta < \mu_{\mathrm{B}}^\alpha$, $\mathrm{d}G < 0$ and the transfer is spontaneous; when $\mu_{\mathrm{B}}^\beta = \mu_{\mathrm{B}}^\alpha$ the two phases are in equilibrium; when $\mu_{\mathrm{B}}^\beta > \mu_{\mathrm{B}}^\alpha$ only the reverse process can proceed spontaneously. Matter always flows spontaneously from high chemical potential to low chemical potential, just as heat flows from high to low temperature and gas from high to low pressure; the chemical potential is often called the "escaping tendency" of a substance.

Now consider a chemical reaction $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$. When the extent of reaction changes by $\mathrm{d}\xi$, $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$ (for the **extent of reaction** and **stoichiometric number** see [6.1.6](/6.1.6#sec-6.3.2)), and at constant temperature and pressure $\mathrm{d}G = (\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}})\,\mathrm{d}\xi$. The reaction proceeds spontaneously in the direction in which $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}\xi < 0$, and at equilibrium $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$: the chemical potentials (weighted by stoichiometric numbers) of the product side and the reactant side are equal.

At constant temperature and volume one uses $\mathrm{d}A$, and at constant entropy and volume or constant entropy and pressure $\mathrm{d}U$ or $\mathrm{d}H$; Eq. (4.7) gives the same conclusion.

**Theorem 4.3.2 (Chemical Potential Criterion)** With $W' = 0$ and one of the pairs $(T, p)$, $(T, V)$, $(S, V)$, $(S, p)$ held constant, mass-transfer processes within the system (diffusion, phase change, chemical reaction) satisfy

$$
\sum_{\alpha}\sum_{\mathrm{B}}\mu_{\mathrm{B}}^\alpha\,\mathrm{d}n_{\mathrm{B}}^\alpha \le 0 \qquad (< 0 \text{ spontaneous},\ = 0 \text{ equilibrium}),
$$
the sum running over all phases $\alpha$ and the substances B in them.

If $T$, $p$, $V$ and $S$ all vary, can the chemical potential still be used? It can, but one must return to the entropy criterion. Let an isolated system consist of two parts $\alpha$ and $\beta$ that can exchange energy, volume and substance B. From Eq. (4.7) write $\mathrm{d}S = (\mathrm{d}U + p\,\mathrm{d}V - \sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}})/T$ and use $\mathrm{d}U^\beta = -\mathrm{d}U^\alpha$, $\mathrm{d}V^\beta = -\mathrm{d}V^\alpha$, $\mathrm{d}n_{\mathrm{B}}^\beta = -\mathrm{d}n_{\mathrm{B}}^\alpha$:

$$
\mathrm{d}S = \left(\frac{1}{T^\alpha} - \frac{1}{T^\beta}\right)\mathrm{d}U^\alpha + \left(\frac{p^\alpha}{T^\alpha} - \frac{p^\beta}{T^\beta}\right)\mathrm{d}V^\alpha - \left(\frac{\mu_{\mathrm{B}}^\alpha}{T^\alpha} - \frac{\mu_{\mathrm{B}}^\beta}{T^\beta}\right)\mathrm{d}n_{\mathrm{B}}^\alpha.
$$
At equilibrium the entropy is a maximum and the coefficients of the three independently varying quantities must all vanish: $T^\alpha = T^\beta$ (thermal equilibrium), $p^\alpha = p^\beta$ (mechanical equilibrium) and $\mu_{\mathrm{B}}^\alpha = \mu_{\mathrm{B}}^\beta$ (material equilibrium). When the temperatures of the two parts are equal, the increase of entropy requires substance to be transferred to the side of lower $\mu_{\mathrm{B}}$, in agreement with Theorem 4.3.2. If the two parts are separated by a rigid wall (such as a semipermeable membrane with different pressures on its two sides), the second condition does not appear, and at equilibrium the pressures may be unequal; this is the origin of osmotic pressure ([6.3.5](/6.3.5)).

To summarize: when $W' = 0$ the chemical potential is the unified criterion for all mass-transfer processes; the condition for equilibrium is that each substance has the same chemical potential in all the phases in which it is present, and that $\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$ for each independent reaction. These two statements are the common basis for the treatment of phase equilibrium and chemical equilibrium later. Transport of matter across biological membranes is the same: passive diffusion down the gradient of chemical potential (for ions, of electrochemical potential, [6.3.13](/6.3.13)) is spontaneous, while active transport against the gradient must be coupled to a process with $\Delta G < 0$ such as ATP hydrolysis ([6.3.18](/6.3.18)).

### 4.3.4. Dependence of the Chemical Potential on Temperature and Pressure

**Theorem 4.3.3** At constant composition,

$$
\left(\frac{\partial\mu_{\mathrm{B}}}{\partial p}\right)_{T,n} = V_{\mathrm{B}}, \qquad \left(\frac{\partial\mu_{\mathrm{B}}}{\partial T}\right)_{p,n} = -S_{\mathrm{B}}, \qquad \left[\frac{\partial(\mu_{\mathrm{B}}/T)}{\partial T}\right]_{p,n} = -\frac{H_{\mathrm{B}}}{T^2}.
\tag{4.9}
$$

**Proof** By Eq. (4.6), $\mathrm{d}G$ is a total differential in $T$, $p$, $n_{\mathrm{B}}$, and mixed second derivatives do not depend on the order:

$$
\left(\frac{\partial\mu_{\mathrm{B}}}{\partial p}\right)_{T,n} = \frac{\partial^2 G}{\partial p\,\partial n_{\mathrm{B}}} = \left[\frac{\partial}{\partial n_{\mathrm{B}}}\left(\frac{\partial G}{\partial p}\right)_{T,n}\right]_{T,p,n_{\mathrm{C}}} = \left(\frac{\partial V}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}} = V_{\mathrm{B}}.
$$
The second follows likewise. The third is proved as the Gibbs–Helmholtz equation is, using $\mu_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$. $\square$

Compare with the relations for pure substances ([6.3.3](/6.3.3), 3.4.4): replacing the molar quantities in the pure-substance relations by partial molar quantities gives the relations for component B in a mixture.

| Pure substance B | B in a mixture |
|---|---|
| $(\partial G^*_{\mathrm{m}}/\partial p)_T = V^*_{\mathrm{m}}$ | $(\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = V_{\mathrm{B}}$ |
| $(\partial G^*_{\mathrm{m}}/\partial T)_p = -S^*_{\mathrm{m}}$ | $(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = -S_{\mathrm{B}}$ |
| $[\partial(G^*_{\mathrm{m}}/T)/\partial T]_p = -H^*_{\mathrm{m}}/T^2$ | $[\partial(\mu_{\mathrm{B}}/T)/\partial T]_{p,n} = -H_{\mathrm{B}}/T^2$ |
| $G^*_{\mathrm{m}} = H^*_{\mathrm{m}} - TS^*_{\mathrm{m}}$ | $\mu_{\mathrm{B}} = H_{\mathrm{B}} - TS_{\mathrm{B}}$ |

In general $V_{\mathrm{B}} > 0$ and $S_{\mathrm{B}} > 0$, so raising the pressure raises the chemical potential and raising the temperature lowers it. For the phases of a pure substance, $-S_{\mathrm{m}}$ is the slope of the $\mu^*$–$T$ curve, and since $S_{\mathrm{m}}(\mathrm{g}) > S_{\mathrm{m}}(\mathrm{l}) > S_{\mathrm{m}}(\mathrm{s})$, the line for the gas is the steepest and that for the solid the flattest. At each temperature the phase of lowest chemical potential is the stable phase, and the intersection of two lines is the temperature of two-phase equilibrium (melting point, boiling point); the curves all bend downward, because $(\partial^2\mu^*/\partial T^2)_p = -C_{p,\mathrm{m}}/T < 0$. Raising the pressure shifts each line upward by $V_{\mathrm{m}}\Delta p$: the gas line shifts the most, so the boiling point rises; the molar volume of liquid water is smaller than that of ice, so on compression the liquid line shifts up less than the solid line and the melting point falls ([6.3.8](/6.3.8)).

![Chemical potentials of the phases of pure water as functions of temperature (computed from CRC entropy and heat-capacity data, with the zero taken at the melting point). At 1 bar the intersections of the three lines give the melting and boiling points; when the pressure is raised to 10 bar only the gas line shifts up noticeably, and the boiling point rises to about 456 K (measured 453 K).](./plots/mu-temperature.py)

**Example 4.3.2** Let the normal boiling point of water be $T_{\mathrm{b}}$ ($373.12\,\mathrm{K}$). Compare the chemical potentials of water in the following states: (1) liquid water at $T_{\mathrm{b}}$ and $101.325\,\mathrm{kPa}$ and (2) water vapor at the same temperature and pressure; (3) liquid water at $T_{\mathrm{b}}$ and $202.65\,\mathrm{kPa}$ and (4) water vapor at the same temperature and pressure; (5) liquid water at $T_{\mathrm{b}} + 1\,\mathrm{K}$ and $101.325\,\mathrm{kPa}$ and (6) water vapor at the same temperature and pressure.

**Solution** At $T_{\mathrm{b}}$ and $101.325\,\mathrm{kPa}$ liquid water and water vapor are in two-phase equilibrium, $\mu_1 = \mu_2$. On isothermal compression, $\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$, and $V^*_{\mathrm{m}}(\mathrm{g}) \gg V^*_{\mathrm{m}}(\mathrm{l})$, so $\mu_4 - \mu_2 > \mu_3 - \mu_1 > 0$ and $\mu_3 < \mu_4$: at high pressure the liquid is stable. On isobaric heating, $\mathrm{d}\mu^* = -S^*_{\mathrm{m}}\,\mathrm{d}T$, and $S^*_{\mathrm{m}}(\mathrm{g}) > S^*_{\mathrm{m}}(\mathrm{l})$, so both chemical potentials fall but that of the vapor falls more, $\mu_5 > \mu_6$: above the boiling point the gas is stable. $\square$

## 4.4. Chemical Potentials of Gases

The absolute value of a chemical potential cannot be determined (it contains the zero of internal energy); only the difference between different states of the same substance can be. A **standard state** ([6.1.6](/6.1.6#sec-6.3.3)) is therefore chosen for each substance, and the chemical potential in any state is written as "chemical potential in the standard state plus a computable correction".

### 4.4.1. Pure Ideal Gases

The standard state of a gas is the pure ideal gas at temperature $T$ and the **standard pressure** $p^\circ = 10^5\,\mathrm{Pa}$; its chemical potential is written $\mu^\circ_{\mathrm{B}}(T)$, called the standard chemical potential, a function of temperature only. For a pure ideal gas at constant temperature $(\partial\mu^*_{\mathrm{B}}/\partial p)_T = V^*_{\mathrm{m}} = RT/p$, and integrating from $p^\circ$ to $p$,

$$
\mu^*_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{p}{p^\circ}.
\tag{4.10}
$$
$RT\ln(p/p^\circ)$ is the difference between the chemical potentials of pure ideal gas B at $(T, p)$ and in the standard state.

### 4.4.2. Ideal-Gas Mixtures

Imagine a container divided by a membrane permeable only to B into two parts: on one side an ideal-gas mixture at temperature $T$, total pressure $p$ and composition $x_{\mathrm{B}}$, on the other pure B. At equilibrium the chemical potentials of B on the two sides are equal, and experiment shows (for an ideal-gas mixture it can also be deduced from the absence of intermolecular interactions) that the pressure on the pure-B side then equals the **partial pressure** of B in the mixture, $p_{\mathrm{B}} = px_{\mathrm{B}}$. From Eq. (4.10),

$$
\mu_{\mathrm{B}}(T, p, x_{\mathrm{B}}) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{p_{\mathrm{B}}}{p^\circ} = \mu^*_{\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}.
\tag{4.11}
$$
Here $\mu^\circ_{\mathrm{B}}(T)$ is still the standard chemical potential of pure B at $T$ and $p^\circ$, and $\mu^*_{\mathrm{B}}(T, p)$ is the chemical potential of pure B at the temperature and total pressure of the mixture. The chemical potential of B in the mixture is lower than that of pure B at the same temperature and pressure by $RT\ln(1/x_{\mathrm{B}})$; this lowering is the reason mixing is spontaneous.

**Example 4.4.1** Use chemical potentials to find $\Delta_{\mathrm{mix}}G$, $\Delta_{\mathrm{mix}}S$, $\Delta_{\mathrm{mix}}H$ and $\Delta_{\mathrm{mix}}V$ for the isothermal, isobaric mixing of ideal gases A and B.

**Solution** From the additivity formula and Eq. (4.11),

$$
\Delta_{\mathrm{mix}}G = (n_{\mathrm{A}}\mu_{\mathrm{A}} + n_{\mathrm{B}}\mu_{\mathrm{B}}) - (n_{\mathrm{A}}\mu^*_{\mathrm{A}} + n_{\mathrm{B}}\mu^*_{\mathrm{B}}) = RT(n_{\mathrm{A}}\ln x_{\mathrm{A}} + n_{\mathrm{B}}\ln x_{\mathrm{B}}).
$$
Differentiating with respect to $T$ gives the **entropy of mixing** $\Delta_{\mathrm{mix}}S = -(\partial\Delta_{\mathrm{mix}}G/\partial T)_{p,n} = -R(n_{\mathrm{A}}\ln x_{\mathrm{A}} + n_{\mathrm{B}}\ln x_{\mathrm{B}})$; differentiating with respect to $p$, $\Delta_{\mathrm{mix}}V = (\partial\Delta_{\mathrm{mix}}G/\partial p)_{T,n} = 0$ ($x_{\mathrm{B}}$ is independent of $p$); $\Delta_{\mathrm{mix}}H = \Delta_{\mathrm{mix}}G + T\Delta_{\mathrm{mix}}S = 0$ and $\Delta_{\mathrm{mix}}U = 0$. These agree with the results obtained directly from entropy in [6.3.2](/6.3.2). $\square$

The isothermal, isobaric mixing of ideal gases neither absorbs nor releases heat and leaves the volume unchanged; the driving force is entirely entropy. The same form of result will appear for ideal liquid mixtures ([6.3.5](/6.3.5)).

### 4.4.3. Real Gases: Fugacity and the Fugacity Coefficient

For a real gas $V^*_{\mathrm{m}} \ne RT/p$ and Eq. (4.10) no longer holds. The equations of state of real gases take various forms and none is universally valid; if $\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$ were integrated directly with some equation of state, the expression for the chemical potential would change with the equation of state. Lewis (1901) retained the form of Eq. (4.10) and put all the effects of departure from ideality into a "corrected pressure".

**Definition 4.4.1** When the chemical potential of a pure real gas B is written

$$
\mu^*_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{f}{p^\circ}, \qquad \lim_{p\to 0}\frac{f}{p} = 1,
\tag{4.12}
$$
the quantity $f$, which has the dimensions of pressure, is called the **fugacity** of the gas; $\varphi = f/p$ is called the **fugacity coefficient**, a dimensionless quantity.

Several remarks:

1. The standard state is still the pure ideal gas at $T$ and $p^\circ$; for a real gas it is a hypothetical state and not the real gas at $p^\circ$. $RT\ln(f/p^\circ)$ is the difference between the chemical potentials of the real gas at $(T, p)$ and in the hypothetical standard state.
2. The limiting condition in the definition fixes the zero of $f$: as the pressure tends to zero all gases tend to ideal gases and $\varphi \to 1$. For an ideal gas $\varphi = 1$ and $f = p$.
3. $\varphi$ is a function of $T$, $p$ and the nature of the gas, not a characteristic constant of the gas; it expresses how far the real gas departs thermodynamically from an ideal gas.
4. The fugacity is called a "corrected pressure", but $fV = nRT$ does not hold in general: $f$ replaces $p$ only in the expression for the chemical potential and does not satisfy the equation of state of the ideal gas.

The fugacity coefficient is related in a definite way to the **compressibility factor** $Z = pV_{\mathrm{m}}/(RT)$ ([6.1.1](/6.1.1)):

**Theorem 4.4.1** The fugacity coefficient of a pure real gas at temperature $T$ is

$$
\ln\varphi = \int_0^p\frac{Z - 1}{p'}\,\mathrm{d}p'.
\tag{4.13}
$$

**Proof** At constant temperature, Eq. (4.12) gives $\mathrm{d}\mu^* = RT\,\mathrm{d}\ln f$, and also $\mathrm{d}\mu^* = V^*_{\mathrm{m}}\,\mathrm{d}p$. Subtracting $RT\,\mathrm{d}\ln p = (RT/p)\,\mathrm{d}p$ for the ideal gas,

$$
RT\,\mathrm{d}\ln\frac{f}{p} = \left(V^*_{\mathrm{m}} - \frac{RT}{p}\right)\mathrm{d}p = RT\,\frac{Z - 1}{p}\,\mathrm{d}p.
$$
Integrating from $p' \to 0$ ($\ln\varphi \to 0$) to $p$ gives the result. $\square$

Thus $\varphi < 1$ in the pressure range where attraction dominates and $Z < 1$, and $\varphi$ gradually exceeds 1 when repulsion dominates and $Z > 1$; $\ln\varphi$ equals the area under the $(Z - 1)/p$ curve (graphical method). There are three ways of finding fugacities: integration with an equation of state (analytically or numerically); graphical integration of experimental $p$–$V$–$T$ data; and the corresponding-states method.

For the **van der Waals equation**, Eq. (4.13) can be integrated in closed form. In terms of the **reduced variables** $T_{\mathrm{r}} = T/T_{\mathrm{c}}$ and $p_{\mathrm{r}} = p/p_{\mathrm{c}}$, write $\mathcal{A} = 27p_{\mathrm{r}}/(64T_{\mathrm{r}}^2)$ and $\mathcal{B} = p_{\mathrm{r}}/(8T_{\mathrm{r}})$; the compressibility factor is a root of the cubic equation $Z^3 - (1 + \mathcal{B})Z^2 + \mathcal{A}Z - \mathcal{A}\mathcal{B} = 0$, and

$$
\ln\varphi = Z - 1 - \ln(Z - \mathcal{B}) - \frac{\mathcal{A}}{Z}.
$$
$\varphi$ depends only on $T_{\mathrm{r}}$ and $p_{\mathrm{r}}$: this is the expression of the **principle of corresponding states** ([6.3.1](/6.3.1)) for fugacity. In practice different gases in the same reduced state have approximately the same fugacity coefficient, which can be read from a generalized fugacity-coefficient chart (Newton chart); the vdW equation gives the qualitative shape of such charts, though quantitatively it overestimates the effect of attraction. Eq. (4.13) can also be integrated numerically directly (`scipy.integrate.quad`, [4.4.4](/4.4.4#sec-4.3.1)), and the two methods agree:

```python
import numpy as np
from scipy.integrate import quad

def Z_vdw(pr, Tr):
    """Gas-like root of the reduced van der Waals cubic."""
    A, B = 27 * pr / (64 * Tr**2), pr / (8 * Tr)
    r = np.roots([1, -(1 + B), A, -A * B])
    return r[np.abs(r.imag) < 1e-9].real.max()

Tr, pr = 1.2, 1.0
ln_phi, _ = quad(lambda p: (Z_vdw(p, Tr) - 1) / p, 1e-12, pr)
print(np.exp(ln_phi))  # 0.816
```

![Fugacity coefficient (left) and compressibility factor (right) of a van der Waals gas as functions of reduced pressure. When T_r is below the Boyle temperature (27/8 = 3.375 for a vdW gas), attraction dominates at low pressure and φ < 1; at high pressure repulsion dominates and φ rises again.](./plots/vdw-fugacity.py)

**Example 4.4.2** A real gas changes isothermally from $p_1$ to $p_2$. Find $\Delta G$; can $\Delta S = nR\ln(f_1/f_2)$ be used for the entropy change?

**Solution** $\Delta G = n(\mu_2^* - \mu_1^*) = nRT\ln(f_2/f_1)$, which has the same form as $nRT\ln(p_2/p_1)$ for an ideal gas. But the entropy change cannot simply copy $\Delta S = -\Delta G/T$ of the ideal gas: that relation depends on $\Delta H = 0$, whereas for a real gas $\Delta H \ne 0$ in an isothermal pressure change ([6.3.3, Theorem 3.4.1](/6.3.3)). The correct approach is to use $S^*_{\mathrm{m}} = -(\partial\mu^*/\partial T)_p$:

$$
S^*_{\mathrm{m}}(T, p) = S^\circ_{\mathrm{m}}(T) - R\ln\frac{p}{p^\circ} - R\ln\varphi - RT\left(\frac{\partial\ln\varphi}{\partial T}\right)_p,
$$
where the last term comes from the dependence of $\varphi$ on temperature. So $\Delta S = nR\ln(f_1/f_2)$ is wrong unless $\varphi$ is independent of temperature. $\square$

### 4.4.4. Real-Gas Mixtures and the Lewis–Randall Rule

The chemical potential of component B in a real-gas mixture is likewise written

$$
\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln\frac{f_{\mathrm{B}}}{p^\circ}, \qquad f_{\mathrm{B}} = \varphi_{\mathrm{B}}p_{\mathrm{B}}, \qquad \lim_{p\to 0}\varphi_{\mathrm{B}} = 1,
\tag{4.14}
$$
where $f_{\mathrm{B}}$ and $\varphi_{\mathrm{B}}$ are the fugacity and fugacity coefficient of B in the mixture, $p_{\mathrm{B}} = px_{\mathrm{B}}$ is the partial pressure, and $\mu^\circ_{\mathrm{B}}$ is still the chemical potential of ideal-gas B at $p^\circ$. Strictly, $\varphi_{\mathrm{B}}$ depends on the composition of the mixture and must be obtained from the equation of state of the mixture. In the absence of such data the following approximation is used.

**Definition 4.4.2 (Lewis–Randall Rule)** The approximation

$$
f_{\mathrm{B}}(T, p, x_{\mathrm{B}}) = x_{\mathrm{B}}f^*_{\mathrm{B}}(T, p), \quad \text{that is}\quad \varphi_{\mathrm{B}} = \varphi^*_{\mathrm{B}}(T, p)
$$
is called the **Lewis–Randall rule**, where $f^*_{\mathrm{B}}$ and $\varphi^*_{\mathrm{B}}$ are the fugacity and fugacity coefficient of pure B at the temperature and total pressure of the mixture.

The rule amounts to treating the mixture as an ideal mixture of real gases: it takes into account the temperature, the pressure and the nature of B itself, but ignores the interactions between unlike molecules and the differences between like and unlike molecules. Strictly it applies only to gases whose molecules are similar in size and interactions (such as $\ce{N2}$–$\ce{O2}$), or to a component present in high proportion; for mixtures of very different polarity (such as $\ce{H2}$–$\ce{NH3}$) the error is considerable.

**Example 4.4.3** Estimate the fugacities of $\ce{O2}$ ($x = 0.21$) and $\ce{N2}$ ($x = 0.79$) in air at $298\,\mathrm{K}$ and $10^7\,\mathrm{Pa}$.

**Solution** By the Lewis–Randall rule, $f(\ce{O2}) = 0.21\,f^*(\ce{O2}, 298\,\mathrm{K}, 10^7\,\mathrm{Pa})$. For $\ce{O2}$, $T_{\mathrm{c}} = 154.58\,\mathrm{K}$ and $p_{\mathrm{c}} = 5.043\,\mathrm{MPa}$, and the reduced state is $T_{\mathrm{r}} = 1.93$, $p_{\mathrm{r}} = 1.98$; the reduced vdW equation gives $\varphi^* \approx 0.91$, so $f(\ce{O2}) \approx 0.21 \times 0.91 \times 10\,\mathrm{MPa} = 1.9\,\mathrm{MPa}$. For $\ce{N2}$, $T_{\mathrm{c}} = 126.19\,\mathrm{K}$ and $p_{\mathrm{c}} = 3.396\,\mathrm{MPa}$, $T_{\mathrm{r}} = 2.36$, $p_{\mathrm{r}} = 2.94$, $\varphi^* \approx 0.95$, and $f(\ce{N2}) \approx 0.79 \times 0.95 \times 10\,\mathrm{MPa} = 7.5\,\mathrm{MPa}$. The vdW equation overestimates the departure, and an accurate equation of state gives a $\varphi^*$ closer to 1; so does the value from a generalized fugacity-coefficient chart. $\square$

## Summary

| System | Chemical potential | Standard state |
|---|---|---|
| Pure ideal gas | $\mu^* = \mu^\circ(T) + RT\ln(p/p^\circ)$ | Pure ideal gas, $T$, $p^\circ$ |
| Ideal-gas mixture | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln(p_{\mathrm{B}}/p^\circ) = \mu^*_{\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$ | Same |
| Pure real gas | $\mu^* = \mu^\circ(T) + RT\ln(f/p^\circ)$, $f = \varphi p$ | Same (hypothetical state) |
| Real-gas mixture | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln(f_{\mathrm{B}}/p^\circ)$, $f_{\mathrm{B}} = \varphi_{\mathrm{B}}p_{\mathrm{B}}$ | Same (hypothetical state) |

- A partial molar quantity $X_{\mathrm{B}} = (\partial X/\partial n_{\mathrm{B}})_{T,p,n_{\mathrm{C}}}$ is an intensive property; the additivity formula $X = \sum n_{\mathrm{B}}X_{\mathrm{B}}$ describes one state, and the Gibbs–Duhem equation $\sum x_{\mathrm{B}}\,\mathrm{d}X_{\mathrm{B}} = 0$ (constant $T$, $p$) constrains changes of composition.
- The chemical potential is $\mu_{\mathrm{B}} = G_{\mathrm{B}}$; for variable composition the fundamental equations acquire $\sum\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$. When $W' = 0$, substances flow from high chemical potential to low; at equilibrium each substance has the same chemical potential in all phases, and $\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$ for each reaction.
- $(\partial\mu_{\mathrm{B}}/\partial p)_T = V_{\mathrm{B}}$ and $(\partial\mu_{\mathrm{B}}/\partial T)_p = -S_{\mathrm{B}}$; the intersections of the $\mu^*$–$T$ curves of the phases of a pure substance are the transition points.
- Fugacity retains the form of the chemical potential of the ideal gas, $\ln\varphi = \int_0^p (Z - 1)\,\mathrm{d}p/p$; the chemical potentials of components in liquid mixtures and solutions will be written by means of the vapor in equilibrium with them ([6.3.5](/6.3.5)).
