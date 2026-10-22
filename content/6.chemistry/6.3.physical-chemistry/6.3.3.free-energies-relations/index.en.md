---
title: Free Energies and Fundamental Relations
source_hash: 3e71aee0f9cf
---

The **principle of entropy increase** gives the ultimate criterion for the direction and limit of every macroscopic process, but to apply it to a chemical process one must compute the entropy changes of both system and surroundings and regard the two together as an isolated system. The conditions most common in chemistry are constant temperature and volume, or constant temperature and pressure. Starting from the **Clausius inequality**, this chapter constructs two state functions that serve as criteria using only properties of the system itself: the Helmholtz energy $A$ and the **Gibbs energy** $G$ (Section 3.1), and relates them to maximum work and maximum non-expansion work. The second part builds the mathematical structure of thermodynamics: the four fundamental equations and characteristic functions (3.2), the coefficient relations and Maxwell relations (3.3), and from them general relations independent of the particular substance, such as the thermodynamic equation of state and the general formula for $C_p - C_V$ (3.4). Finally we discuss systematically the calculation of $\Delta G$ and $\Delta A$ for various processes (3.5) and the Gibbs–Helmholtz equation for the temperature dependence of $G$ (3.6). The Gibbs energy and the Gibbs criterion were introduced in [6.1.6](/6.1.6#sec-6.4.7); here the derivation and the conditions of validity are completed. The first and second laws and entropy are in [5.2.3](/5.2.3), [5.2.4](/5.2.4) and [6.3.2](/6.3.2); the manipulation of partial derivatives, total differentials and implicit functions is in [2.2.10](/2.2.10). The relations of this chapter are the tools of the chapters that follow: when composition can vary, a chemical-potential term is added ([6.3.4](/6.3.4)); the Gibbs–Helmholtz equation is used for the temperature dependence of equilibrium constants ([6.3.7](/6.3.7)) and the temperature coefficient of cell voltage ([6.3.13](/6.3.13)); and the Clapeyron equation ([6.3.8](/6.3.8)) is the form taken by a Maxwell relation when two phases coexist.

## 3.1. The Helmholtz Energy and Gibbs Energy Criteria

### 3.1.1. Limitations of the Entropy Criterion

The **Clausius inequality** for any process in a closed system is

$$
\mathrm{d}S \ge \frac{\delta Q}{T_{\mathrm{sur}}},
$$
where $T_{\mathrm{sur}}$ is the temperature of the surroundings (reservoir) that exchanges heat with the system, and equality holds for reversible processes. Using it directly to judge direction has three inconveniences. The heat–temperature quotient $\delta Q/T_{\mathrm{sur}}$ of the actual process must be computed. The principle of entropy increase applies only to adiabatic or isolated systems, so for a general process the surroundings must be added to form a large isolated system and the entropy change of the surroundings $\Delta S_{\mathrm{sur}} = -Q/T_{\mathrm{sur}}$ computed. And for a process such as the electrolysis of water, which needs electrical work from outside, the entropy of the large isolated system still increases, so the entropy criterion says only that the process "can occur when driven by electrical work" and does not directly answer whether it can occur spontaneously without electrical work. What is really of interest is two sets of conditions: a closed system at constant temperature and volume, and a closed system at constant temperature and pressure. Under these conditions the effect of the surroundings is completely determined by temperature and pressure, and the Clausius inequality can be rewritten in a form containing only state functions of the system.

### 3.1.2. The Helmholtz Energy

Let a closed system exchange heat with a single reservoir at constant temperature $T_{\mathrm{sur}}$, with the temperatures of the initial and final states of the process both equal to $T_{\mathrm{sur}}$ (the temperature of the system may differ in between, as in a combustion carried out in a thermostat bath). Such a process is called isothermal. Integrating the Clausius inequality gives $Q \le T_{\mathrm{sur}}\Delta S$, and substituting into the first law $\Delta U = Q + W$ ($W$ is the total work done on the system by the surroundings),

$$
W \ge \Delta U - T_{\mathrm{sur}}\Delta S = \Delta U - \Delta(TS),
$$
where the last step uses $T_1 = T_2 = T_{\mathrm{sur}}$. The right-hand side is the change of a state function.

**Definition 3.1.1 (Helmholtz Energy)** The state function

$$
A = U - TS
$$
is called the **Helmholtz energy** of the system (also called the Helmholtz free energy or Helmholtz function), with the unit J.

$A$ is extensive. It has no direct physical meaning in itself, but its change has a definite meaning under isothermal conditions:

**Theorem 3.1.1 (Maximum Work)** For an isothermal process in a closed system,

$$
-W \le -\Delta A, \tag{3.1}
$$
with equality for reversible processes. That is, the work (expansion and non-expansion) that a system can do on the surroundings in an isothermal process is at most equal to the decrease of its Helmholtz energy, and this is attained only in a reversible isothermal process.

This is the basis of the statement that "a reversible isothermal process does the most work": when two processes have the same initial and final states, $\Delta A$ is the same, and for the reversible process $-W_{\mathrm{r}} = -\Delta A$, while for an irreversible process $-W_{\mathrm{ir}} < -\Delta A$. Some textbooks call $A$ the "work function"; this wiki does not use that name, to avoid confusion with the work function of a metal.

Divide the total work into expansion work and **non-expansion work**, $W = -\int p_{\mathrm{ex}}\,\mathrm{d}V + W'$. If the volume of the system is fixed, the expansion work is zero, Eq. (3.1) becomes $W' \ge \Delta A$, and setting $W' = 0$ gives:

**Theorem 3.1.2 (Helmholtz Energy Criterion)** For a closed system at constant temperature and volume without non-expansion work,

$$
\Delta A \le 0 \qquad (< 0 \text{ spontaneous},\ = 0 \text{ equilibrium}).
$$
That is, under these conditions the Helmholtz energy of the system can only decrease, and it reaches a minimum at equilibrium.

### 3.1.3. The Gibbs Energy

Let the process also be isothermal, with constant external pressure equal to the pressures of the initial and final states: $p_{\mathrm{ex}} = p_1 = p_2 = p$. The expansion work is $-p\Delta V = -\Delta(pV)$, and Eq. (3.1) becomes $-\Delta(pV) + W' \ge \Delta A$, that is,

$$
W' \ge \Delta(A + pV) = \Delta(U + pV - TS) = \Delta(H - TS).
$$

**Definition 3.1.2 (Gibbs Energy)** The state function

$$
G = H - TS = A + pV
$$
is called the **Gibbs energy** of the system.

**Theorem 3.1.3 (Maximum Non-Expansion Work)** For an isothermal, isobaric process in a closed system,

$$
-W' \le -\Delta G, \tag{3.2}
$$
with equality for reversible processes. That is, the non-expansion work (electrical work, surface work, and so on) that a system can do on the surroundings in an isothermal, isobaric process is at most equal to the decrease of its Gibbs energy.

**Theorem 3.1.4 (Gibbs Energy Criterion)** For a closed system at constant temperature and pressure without non-expansion work,

$$
\Delta G \le 0 \qquad (< 0 \text{ spontaneous},\ = 0 \text{ equilibrium}),
$$
and the system always changes in the direction of decreasing Gibbs energy, with $G$ at a minimum at equilibrium.

Eq. (3.2) says that $-\Delta G$ is an upper bound on "the part of the energy that can be converted into useful work", not some kind of "chemical energy" contained in the system: $-\Delta G = -\Delta H + T\Delta S$, in which the term $-T\Delta S$ is the heat that must be exchanged with the reservoir in a reversible process. For example, for $\ce{H2(g) + 1/2O2(g) -> H2O(l)}$ at $298.15\,\mathrm{K}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -237.1\,\mathrm{kJ\,mol^{-1}}$ and $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -285.8\,\mathrm{kJ\,mol^{-1}}$; a fuel cell delivers at most $237.1\,\mathrm{kJ}$ of electrical work per mole of reaction, and the remaining $48.7\,\mathrm{kJ}$ must be released to the surroundings as heat even if the process is reversible. Conversely, the **electrolysis** of water has $\Delta G > 0$ and cannot occur spontaneously at constant temperature and pressure; the surroundings must do electrical work of at least $\Delta G$ ($W' \ge \Delta G$). This does not contradict the statement that "the combination of $\ce{H2}$ and $\ce{O2}$ is a spontaneous process": they are the forward and reverse directions of the same reaction.

**Remark 3.1.1** The Clausius inequality holds for every process, electrolysis included: for the electrolysis of water $\Delta S \ge Q/T_{\mathrm{sur}}$ is likewise satisfied, because the electrical work increases the entropy of the large isolated system (which includes the power source). "Spontaneous" means that the process can occur without non-expansion work from the surroundings, and $W' = 0$ in the Helmholtz and Gibbs criteria is the mathematical expression of this meaning.

### 3.1.4. Comparison of the Three Criteria

| Function | System | Condition | Criterion ($<$ irreversible, $=$ reversible) |
|---|---|---|---|
| $S$ | Closed system | Any process | $\Delta S \ge \int \delta Q/T_{\mathrm{sur}}$ |
| $S$ | Isolated or adiabatic system | Any process | $\Delta S \ge 0$ |
| $S$ | System + surroundings | Any process | $\Delta S + \Delta S_{\mathrm{sur}} \ge 0$ |
| $A$ | Closed system | Isothermal | $\Delta A \le W$ |
| $A$ | Closed system | Isothermal, isochoric, $W' = 0$ | $\Delta A \le 0$ |
| $G$ | Closed system | Isothermal, isobaric | $\Delta G \le W'$ |
| $G$ | Closed system | Isothermal, isobaric, $W' = 0$ | $\Delta G \le 0$ |

The entropy criterion is fundamental and the other two are derived from it; the Gibbs criterion is the one most used in chemistry. The conditions must be understood for what they really mean: "isothermal" means that the system is in contact with a single reservoir at constant temperature and the temperatures of the initial and final states equal the temperature of the reservoir, and "isobaric" means that the external pressure is constant and equal to the pressures of the initial and final states. When these conditions are not met, even a computed $\Delta G < 0$ does not show that the process is spontaneous (Examples 3.5.1 and 3.5.4).

## 3.2. The Fundamental Equations of Thermodynamics

### 3.2.1. The Four Fundamental Equations

Consider two neighboring **equilibrium states** of a closed system of constant composition (or in internal chemical and phase equilibrium) doing no non-expansion work. Along a reversible path connecting them, $\delta Q_{\mathrm{r}} = T\,\mathrm{d}S$ and $\delta W_{\mathrm{r}} = -p\,\mathrm{d}V$, and the first law gives $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ ([5.2.4, Eq. 4.5.1](/5.2.4#eq-4.2)). Differentiating $H = U + pV$, $A = U - TS$ and $G = H - TS$ and substituting gives three more equations.

**Theorem 3.2.1 (Fundamental Equations of Thermodynamics)** For a closed system of constant composition that does only expansion work, the state functions at two neighboring equilibrium states satisfy

$$
\begin{aligned}
\mathrm{d}U &= T\,\mathrm{d}S - p\,\mathrm{d}V, \\
\mathrm{d}H &= T\,\mathrm{d}S + V\,\mathrm{d}p, \\
\mathrm{d}A &= -S\,\mathrm{d}T - p\,\mathrm{d}V, \\
\mathrm{d}G &= -S\,\mathrm{d}T + V\,\mathrm{d}p.
\end{aligned}
\tag{3.3}
$$

**Proof** The first equation is shown above. $\mathrm{d}H = \mathrm{d}U + p\,\mathrm{d}V + V\,\mathrm{d}p = T\,\mathrm{d}S + V\,\mathrm{d}p$; $\mathrm{d}A = \mathrm{d}U - T\,\mathrm{d}S - S\,\mathrm{d}T = -S\,\mathrm{d}T - p\,\mathrm{d}V$; $\mathrm{d}G = \mathrm{d}H - T\,\mathrm{d}S - S\,\mathrm{d}T = -S\,\mathrm{d}T + V\,\mathrm{d}p$. $\square$

The conditions of validity of the fundamental equations are often stated vaguely, and two matters should be distinguished:

1. Eq. (3.3) is an identity among state functions. A homogeneous closed system of fixed composition has only two independent variables (a two-variable system), $U$ can be regarded as a function of $S$ and $V$, and Eq. (3.3) is its **total differential**. It therefore holds for any process connecting two equilibrium states, whether or not the process is reversible: an irreversible process with the same initial and final states can be replaced by a reversible path for computing the changes of state functions.
2. Only in a reversible process can the terms be interpreted as heat and work: $T\,\mathrm{d}S = \delta Q$ and $-p\,\mathrm{d}V = \delta W$. In an irreversible process $T\,\mathrm{d}S > \delta Q$ (for the free expansion of an ideal gas into vacuum, for example, $\delta Q = 0$ while $T\,\mathrm{d}S = p\,\mathrm{d}V > 0$).

The condition "constant composition" cannot be dropped. When a chemical reaction or phase transition occurs in the system, $U$ also depends on the amounts of the substances, and a term $\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ must be added ([6.3.4](/6.3.4)). Only when the reaction or transition proceeds under equilibrium conditions (such as reversible vaporization at the normal boiling point) does this term vanish and Eq. (3.3) still hold; the common remark that "a chemical change must be reversible for these equations to be used" refers to precisely this. It also resolves a common puzzle: at constant temperature and pressure $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p = 0$, which seems to mean that the system cannot do non-expansion work, in contradiction with $-\Delta G = -W'_{\max}$. In fact an isothermal, isobaric process that can do non-expansion work on the surroundings (discharge of a battery) necessarily involves a change of composition, for which $\mathrm{d}G = \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}} \neq 0$ and the fourth equation of (3.3) no longer applies.

In a reversible process $\delta Q_{\mathrm{r}} = T\,\mathrm{d}S$, so on a $T$–$S$ diagram the area under the curve of a process is the heat absorbed in the reversible process, and the area enclosed by a reversible cycle is the absolute value of the net heat and net work of one cycle ([5.2.4](/5.2.4#sec-4.9)).

### 3.2.2. Natural Variables and Characteristic Functions

In Eq. (3.3) the differential of each function is expressed through the differentials of two other variables: $U$ corresponds to $(S, V)$, $H$ to $(S, p)$, $A$ to $(T, V)$ and $G$ to $(T, p)$. These variables are called the *natural variables* of the corresponding functions.

**Definition 3.2.1 (Characteristic Function)** A thermodynamic function is called a **characteristic function** if, when expressed in its natural variables, all thermodynamic properties of a homogeneous system can be obtained from it by partial differentiation and algebraic operations alone. $U(S, V)$, $H(S, p)$, $A(T, V)$ and $G(T, p)$ are all characteristic functions.

Taking $G(T, p)$ as an example, from Eq. (3.3):

$$
S = -\left(\frac{\partial G}{\partial T}\right)_p, \quad V = \left(\frac{\partial G}{\partial p}\right)_T, \quad H = G - T\left(\frac{\partial G}{\partial T}\right)_p, \quad A = G - p\left(\frac{\partial G}{\partial p}\right)_T, \quad C_p = -T\left(\frac{\partial^2 G}{\partial T^2}\right)_p.
$$
If one knows, for example, that $G = n[\mu^\circ(T) + RT\ln(p/p^\circ)]$ for $n$ mol of an **ideal gas**, then $V = (\partial G/\partial p)_T$ gives the equation of state $pV = nRT$. The same function loses this property when expressed in variables other than its natural ones: $U(T, V)$ is not a characteristic function, because $(\partial U/\partial T)_V = C_V$ gives only the heat capacity, obtaining $S$ requires integrating $C_V/T$ and introducing an integration constant, and $p$ cannot be obtained from $U(T, V)$ at all.

### 3.2.3. The Legendre Transform

The operations that produce $A(T, V)$, $H(S, p)$ and $G(T, p)$ from $U(S, V)$ have a common mathematical form.

**Definition 3.2.2 (Legendre Transform)** Let $f(x)$ be a differentiable, strictly convex function, so that the slope $\xi = f'(x)$ increases monotonically with $x$ and $x$ can be solved for as a function of $\xi$. The function

$$
g(\xi) = f(x) - \xi x \qquad (\xi = f'(x))
$$
is called the **Legendre transform** of $f$. It satisfies $\mathrm{d}g = -x\,\mathrm{d}\xi$, that is, $g'(\xi) = -x$. When a function of several variables is transformed with respect to one of them, the others are kept as parameters.

Geometrically, the convex curve $y = f(x)$ is determined by all its tangent lines (the curve is the envelope of the family of tangents), and each tangent is determined by its slope $\xi$ and its intercept $f(x) - \xi x$ on the vertical axis. So $g(\xi)$ contains the same information as $f(x)$ and only changes the independent variable: it replaces the original variable by the slope, without losing information as a direct substitution $x = x(\xi)$ would. The convex conjugate $f^*(\xi) = \sup_x[\xi x - f(x)]$ commonly used in mathematics differs from this only by a sign.

In thermodynamics $(\partial U/\partial S)_V = T$, so $A = U - TS$ is the Legendre transform of $U$ with respect to $S$, replacing $S$ by $T$; $(\partial U/\partial V)_S = -p$, so $H = U + pV$ replaces $V$ by $p$; and $G = U - TS + pV$ transforms both variables. $U$ is a convex function of $S$ ($(\partial^2 U/\partial S^2)_V = T/C_V > 0$), which guarantees that the transform is invertible.

![U(S) of one mole of a monatomic ideal gas at fixed volume is a convex function (left). The intercept at S = 0 of the tangent line of slope T is A = U − TS; plotting the intercepts of all tangents as a function of T gives A(T) (right), whose slope is −S. The zeros of U and A are arbitrary.](./plots/legendre-transform.py)

| Function | Definition | Natural variables | Fundamental equation | Use |
|---|---|---|---|---|
| $U$ | — | $S, V$ | $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ | Isolated system; statistical thermodynamics |
| $H$ | $U + pV$ | $S, p$ | $\mathrm{d}H = T\,\mathrm{d}S + V\,\mathrm{d}p$ | Heat at constant pressure $Q_p = \Delta H$ |
| $A$ | $U - TS$ | $T, V$ | $\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V$ | Criterion at constant $T$, $V$; $A = -k_{\mathrm{B}}T\ln Z$ ([6.3.10](/6.3.10)) |
| $G$ | $H - TS$ | $T, p$ | $\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p$ | Criterion at constant $T$, $p$; chemical and phase equilibrium |

In experiments it is $T$ and $p$ that are easy to control, not $S$ and $V$, and this is why chemical thermodynamics is centered on $G$.

## 3.3. Coefficient Relations and Maxwell Relations

### 3.3.1. Coefficient Relations

Regarding $U$ as a function of $S$ and $V$, $\mathrm{d}U = (\partial U/\partial S)_V\,\mathrm{d}S + (\partial U/\partial V)_S\,\mathrm{d}V$; comparing coefficients term by term with Eq. (3.3) gives the coefficient relations:

**Formula 3.3.1 (Coefficient Relations)**

$$
\begin{aligned}
\left(\frac{\partial U}{\partial S}\right)_V &= \left(\frac{\partial H}{\partial S}\right)_p = T, &
\left(\frac{\partial U}{\partial V}\right)_S &= \left(\frac{\partial A}{\partial V}\right)_T = -p, \\
\left(\frac{\partial H}{\partial p}\right)_S &= \left(\frac{\partial G}{\partial p}\right)_T = V, &
\left(\frac{\partial A}{\partial T}\right)_V &= \left(\frac{\partial G}{\partial T}\right)_p = -S.
\end{aligned}
$$

The first relation can be regarded as the definition of the thermodynamic temperature: $T$ is the rate of change of internal energy with entropy at constant volume. These relations hold for any equilibrium state and are often used in proofs and in analyzing problems.

### 3.3.2. Maxwell Relations

**Theorem 3.3.1 (Maxwell Relations)** For a closed system of constant composition,

$$
\begin{aligned}
\left(\frac{\partial T}{\partial V}\right)_S &= -\left(\frac{\partial p}{\partial S}\right)_V, &
\left(\frac{\partial T}{\partial p}\right)_S &= \left(\frac{\partial V}{\partial S}\right)_p, \\
\left(\frac{\partial S}{\partial V}\right)_T &= \left(\frac{\partial p}{\partial T}\right)_V, &
\left(\frac{\partial S}{\partial p}\right)_T &= -\left(\frac{\partial V}{\partial T}\right)_p.
\end{aligned}
\tag{3.4}
$$

**Proof** Take the third relation as an example. $A(T, V)$ has continuous second partial derivatives; from the coefficient relations $(\partial A/\partial T)_V = -S$ and $(\partial A/\partial V)_T = -p$, and since mixed partial derivatives do not depend on the order of differentiation ([2.2.10, Theorem 10.4.1](/2.2.10#thm-10.4.1)),

$$
-\left(\frac{\partial S}{\partial V}\right)_T = \frac{\partial^2 A}{\partial V\,\partial T} = \frac{\partial^2 A}{\partial T\,\partial V} = -\left(\frac{\partial p}{\partial T}\right)_V.
$$
The other three follow from $U$, $H$ and $G$ respectively. $\square$

Put differently, $M\,\mathrm{d}x + N\,\mathrm{d}y$ is the total differential of some function if and only if $(\partial M/\partial y)_x = (\partial N/\partial x)_y$ (the criterion for an **exact differential equation**, [2.2.15, Theorem 15.4.1](/2.2.15#thm-15.4.1)). $\delta Q_{\mathrm{r}}$ does not satisfy this condition; $\mathrm{d}S$, after multiplication by the **integrating factor** $1/T$, does. The Maxwell relations are the direct expression of the fact that $\mathrm{d}U$, $\mathrm{d}H$, $\mathrm{d}A$ and $\mathrm{d}G$ are all total differentials.

A mnemonic: on each side of every relation, the numerator and subscript together are exactly the two pairs of conjugate variables $(T, S)$ and $(p, V)$, with $T$ and $S$, and $p$ and $V$, diagonally opposite; the relations carry a minus sign when the two independent variables (denominator and subscript) are $S$ and $V$ or $T$ and $p$, that is, the two relations obtained from $U(S, V)$ and $G(T, p)$. The use of the Maxwell relations is to replace what is hard to measure by what is easy to measure: the last two relations reduce the variation of entropy with volume and pressure to $p$–$V$–$T$ data, since entropy itself cannot be measured directly.

### 3.3.3. Tools for Manipulating Partial Derivatives

Most thermodynamic proofs use only the following tools: the fundamental equations and definitions; differentiating both sides of an identity, or dividing a differential expression by the differential of another quantity while some variables are held constant; comparing coefficients; and the following three relations. Let $x$, $y$, $z$ be related by a functional relation $F(x, y, z) = 0$ with all partial derivatives nonzero (by the **implicit function theorem**, [2.2.10](/2.2.10#sec-10.8.1)). Then

$$
\left(\frac{\partial x}{\partial y}\right)_z = \frac{1}{(\partial y/\partial x)_z}, \qquad
\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y = -1,
\tag{3.5}
$$
the latter being called the cyclic relation. Proof: any two of $x$, $y$, $z$ can serve as independent variables, $\mathrm{d}x = (\partial x/\partial y)_z\,\mathrm{d}y + (\partial x/\partial z)_y\,\mathrm{d}z$; setting $\mathrm{d}x = 0$ gives $(\partial z/\partial y)_x = -(\partial x/\partial y)_z/(\partial x/\partial z)_y$, and rearranging with the reciprocal relation gives the result. [2.2.10](/2.2.10#sec-10.4.1) has already verified with $pV = RT$ that the product of the three partial derivatives is $-1$. Another commonly used relation is the change of subscript (chain relation): if $z = z(x, y)$ and $y$ in turn varies with $x$ along a path of constant $u$, then

$$
\left(\frac{\partial z}{\partial x}\right)_u = \left(\frac{\partial z}{\partial x}\right)_y + \left(\frac{\partial z}{\partial y}\right)_x\left(\frac{\partial y}{\partial x}\right)_u.
\tag{3.6}
$$

The most commonly used measurable quantities are the following two coefficients.

**Definition 3.3.1** The quantities

$$
\alpha_V = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p, \qquad \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial p}\right)_T
$$
are called the **expansion coefficient** and the **isothermal compressibility** of the substance, with the units $\mathrm{K^{-1}}$ and $\mathrm{Pa^{-1}}$.

By the cyclic relation, $(\partial p/\partial T)_V = -(\partial V/\partial T)_p/(\partial V/\partial p)_T = \alpha_V/\kappa_T$. For an ideal gas $\alpha_V = 1/T$ and $\kappa_T = 1/p$. For liquid water at $25\,^\circ\mathrm{C}$, $\alpha_V = 2.57 \times 10^{-4}\,\mathrm{K^{-1}}$ and $\kappa_T = 4.52 \times 10^{-10}\,\mathrm{Pa^{-1}}$, so to keep the volume of water constant on heating by $1\,\mathrm{K}$ a pressure increase of $\alpha_V/\kappa_T \approx 0.57\,\mathrm{MPa}$ is needed: this is why a sealed container filled with liquid easily bursts when heated.

## 3.4. Applications of the Fundamental Relations

### 3.4.1. The Thermodynamic Equation of State

**Theorem 3.4.1 (Thermodynamic Equation of State)** For any substance,

$$
\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial p}{\partial T}\right)_V - p, \qquad
\left(\frac{\partial H}{\partial p}\right)_T = V - T\left(\frac{\partial V}{\partial T}\right)_p.
\tag{3.7}
$$

**Proof** At constant $T$, dividing $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ by $\mathrm{d}V$ gives $(\partial U/\partial V)_T = T(\partial S/\partial V)_T - p$, and then the Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ is used. The second equation follows in the same way from $\mathrm{d}H = T\,\mathrm{d}S + V\,\mathrm{d}p$ and $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$. $\square$

Eq. (3.7) reduces the variation of internal energy and enthalpy with volume and pressure entirely to the equation of state $p(T, V)$; this is the constraint the second law places on equations of state. Several consequences:

- **Ideal gas**: $(\partial p/\partial T)_V = nR/V$, so $(\partial U/\partial V)_T = nRT/V - p = 0$, and likewise $(\partial H/\partial p)_T = 0$. In [5.2.3](/5.2.3#sec-3.3.4) the statement that "the internal energy of an ideal gas is a function of temperature only" is an empirical conclusion from Joule's experiment; here it is deduced from the equation of state $pV = nRT$ ($T$ the thermodynamic temperature) and the second law.
- van der Waals gas: from $p = nRT/(V - nb) - an^2/V^2$, $(\partial U/\partial V)_T = an^2/V^2$, that is, the $a$ term of the **van der Waals equation** is the **internal pressure** ([6.3.1](/6.3.1)). Also $(\partial C_V/\partial V)_T = T(\partial^2 p/\partial T^2)_V = 0$, so the $C_V$ of a vdW gas is also a function of temperature only, and in isothermal expansion $\Delta U = -an^2(1/V_2 - 1/V_1)$.
- In general, for $U = U(T, V)$ and $H = H(T, p)$,
  $$
  \mathrm{d}U = C_V\,\mathrm{d}T + \left[T\left(\frac{\partial p}{\partial T}\right)_V - p\right]\mathrm{d}V, \qquad \mathrm{d}H = C_p\,\mathrm{d}T + \left[V - T\left(\frac{\partial V}{\partial T}\right)_p\right]\mathrm{d}p,
  $$
  and with an equation of state $\Delta U$ and $\Delta H$ can be computed for any change of state of a real gas; without an equation of state, the experimentally measured $(\partial U/\partial V)_T$ and $(\partial H/\partial p)_T$ can conversely be used to test equations of state.
- **Joule–Thomson coefficient**: $\mu_{\mathrm{JT}} = (\partial T/\partial p)_H = -(\partial H/\partial p)_T/C_p$ (cyclic relation), and substituting Eq. (3.7) gives $\mu_{\mathrm{JT}} = V(T\alpha_V - 1)/C_p$. For an ideal gas $T\alpha_V = 1$ and the temperature is unchanged on throttling; when $T\alpha_V > 1$ throttling cools the gas ([6.3.1](/6.3.1)).

### 3.4.2. The Relation between $C_p$ and $C_V$

**Theorem 3.4.2** For any substance,

$$
C_p - C_V = T\left(\frac{\partial p}{\partial T}\right)_V\left(\frac{\partial V}{\partial T}\right)_p = \frac{TV\alpha_V^2}{\kappa_T}.
\tag{3.8}
$$

**Proof** From $H = U + pV$ and the chain relation (3.6) (differentiating $U(T, V)$ along a path of constant $p$),

$$
C_p - C_V = \left(\frac{\partial U}{\partial T}\right)_p + p\left(\frac{\partial V}{\partial T}\right)_p - \left(\frac{\partial U}{\partial T}\right)_V = \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]\left(\frac{\partial V}{\partial T}\right)_p.
$$
Substituting Eq. (3.7) gives the first equality, and then $(\partial p/\partial T)_V = \alpha_V/\kappa_T$ and $(\partial V/\partial T)_p = V\alpha_V$ give the second. $\square$

The first factor on the right of Eq. (3.8), $(\partial U/\partial V)_T + p$, is the extra energy required for the system to expand in volume on heating at constant pressure: part overcomes intermolecular attraction (the internal pressure) and part does work on the surroundings. From Eq. (3.8):

1. Stability of the equilibrium state requires $\kappa_T > 0$, while $T$, $V$ and $\alpha_V^2$ are all nonnegative, so always $C_p \ge C_V$.
2. When $\alpha_V = 0$, $C_p = C_V$, for example for liquid water at $3.98\,^\circ\mathrm{C}$ (the point of maximum density).
3. As $T \to 0$, $C_p - C_V \to 0$.
4. For an ideal gas $C_p - C_V = nR$, which is Mayer's relation ([5.2.3](/5.2.3#sec-3.4.3)).

For condensed phases $\alpha_V$ is small and $C_p$ and $C_V$ differ little. For liquid water at $25\,^\circ\mathrm{C}$, $V_{\mathrm{m}} = 18.07\,\mathrm{cm^3\,mol^{-1}}$, and substituting the $\alpha_V$ and $\kappa_T$ above gives $C_{p,\mathrm{m}} - C_{V,\mathrm{m}} = 0.79\,\mathrm{J\,mol^{-1}\,K^{-1}}$, only 1% of $C_{p,\mathrm{m}} = 75.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$. The $C_V$ of a condensed phase is very hard to measure directly (keeping the volume constant on heating requires enormous pressures); experiments measure $C_p$, while theory (such as the Debye model of lattice vibrations) gives $C_V$, and Eq. (3.8) is the conversion between them.

![Expansion coefficient of liquid water at 1 bar (left, changing sign at 3.98 °C) and C_p,m − C_V,m (right), computed from Kell's fits for density and compressibility.](./plots/water-cp-cv.py)

### 3.4.3. Pressure Must Fall in Reversible Adiabatic Expansion

**Example 3.4.1** Given the stability conditions of the equilibrium state $(\partial p/\partial V)_T < 0$ and $C_V > 0$, prove that the pressure of any substance falls on reversible adiabatic expansion, that is, $(\partial p/\partial V)_S < 0$.

**Solution** A reversible adiabatic process is an **isentropic process**. By the cyclic and chain relations,

$$
\left(\frac{\partial p}{\partial V}\right)_S = -\frac{(\partial S/\partial V)_p}{(\partial S/\partial p)_V}
= -\frac{(\partial S/\partial T)_p(\partial T/\partial V)_p}{(\partial S/\partial T)_V(\partial T/\partial p)_V}
= \frac{C_p/T}{C_V/T}\cdot\left[-\frac{(\partial p/\partial T)_V}{(\partial V/\partial T)_p}\right]
= \frac{C_p}{C_V}\left(\frac{\partial p}{\partial V}\right)_T,
$$
where $(\partial S/\partial T)_p = C_p/T$, $(\partial S/\partial T)_V = C_V/T$ and the cyclic relation $-(\partial p/\partial T)_V/(\partial V/\partial T)_p = (\partial p/\partial V)_T$ have been used. Since $C_p \ge C_V > 0$ and $(\partial p/\partial V)_T < 0$, $(\partial p/\partial V)_S < 0$. $\square$

The result shows that the ratio of the isothermal compressibility to the adiabatic compressibility $\kappa_S = -\frac{1}{V}(\partial V/\partial p)_S$ is $\kappa_T/\kappa_S = C_p/C_V$. For an ideal gas $C_p/C_V$ is the **heat capacity ratio** $\gamma$, and the adiabat is steeper than the isotherm by a factor $\gamma$ ([5.2.3](/5.2.3#sec-3.5.1)); the conclusion here holds for any substance.

### 3.4.4. Effects of Temperature and Pressure on Thermodynamic Functions

From the fundamental equations, the definitions of the heat capacities, the Maxwell relations and Eq. (3.7), the variations of the state functions with $T$ and $p$ are:

| $X$ | $(\partial X/\partial T)_p$ | $(\partial X/\partial p)_T$ |
|---|---|---|
| $U$ | $C_p - pV\alpha_V$ | $pV\kappa_T - TV\alpha_V$ |
| $H$ | $C_p$ | $V(1 - T\alpha_V)$ |
| $S$ | $C_p/T$ | $-V\alpha_V$ |
| $A$ | $-S - pV\alpha_V$ | $pV\kappa_T$ |
| $G$ | $-S$ | $V$ |

The effect of temperature on all functions is significant and cannot be neglected. The effect of pressure depends on the phase: for gases $V$ is large and $S$, $A$ and $G$ vary markedly with pressure (the $U$ and $H$ of an ideal gas are independent of pressure); for liquids and solids $V$, $\alpha_V$ and $\kappa_T$ are all small, and when the pressure changes little $\Delta U$, $\Delta H$, $\Delta S$, $\Delta A$ and $\Delta G$ can all be taken as approximately zero. For example, when the pressure rises from $1\,\mathrm{bar}$ to $100\,\mathrm{bar}$ at $298\,\mathrm{K}$, $\Delta G = V_{\mathrm{m}}\Delta p \approx 0.18\,\mathrm{kJ}$ for $1\,\mathrm{mol}$ of liquid water, whereas $\Delta G = RT\ln 100 = 11.4\,\mathrm{kJ}$ for $1\,\mathrm{mol}$ of ideal gas.

## 3.5. Calculation of ΔG and ΔA

### 3.5.1. Basic Methods

$\Delta G$ and $\Delta A$ are changes of state functions and depend only on the initial and final states. There are four starting points for calculation:

1. Definitions: for any isothermal process in a closed system, $\Delta G = \Delta H - T\Delta S$ and $\Delta A = \Delta U - T\Delta S$.
2. Fundamental equations: for a simple $pVT$ change at constant composition, $\Delta G = \int(-S\,\mathrm{d}T + V\,\mathrm{d}p)$ and $\Delta A = \int(-S\,\mathrm{d}T - p\,\mathrm{d}V)$.
3. Relations to work: for a reversible isothermal process $\Delta A = W$; for a reversible isothermal, isochoric process $\Delta A = W'$; for a reversible isothermal, isobaric process $\Delta G = W'$.
4. The Gibbs–Helmholtz equation (3.6): from $\Delta G$ at one temperature to $\Delta G$ at another.

Several formulas can often be applied to the same problem; when no formula applies to the actual process, design a path with the same initial and final states made up of reversible steps.

### 3.5.2. Isothermal Processes of Ideal Gases

For an ideal gas at constant temperature $\Delta U = \Delta H = 0$, and from $\mathrm{d}G = V\,\mathrm{d}p$,

$$
\Delta G = \Delta A = nRT\ln\frac{p_2}{p_1} = nRT\ln\frac{V_1}{V_2} = -T\Delta S.
$$
The last equality holds only for isothermal processes: when the temperature changes, $\Delta H \ne 0$ for an ideal gas and $\Delta G \ne -T\Delta S$.

**Example 3.5.1** $1\,\mathrm{mol}$ of ideal gas at $300.2\,\mathrm{K}$ expands from $10p^\circ$ to $p^\circ$ by (1) reversible isothermal expansion and (2) expansion into vacuum. Find $Q$, $W$, $\Delta U$, $\Delta H$, $\Delta S$, $\Delta A$ and $\Delta G$ for the two processes.

**Solution** (1) $\Delta U = \Delta H = 0$; $Q = -W = nRT\ln(p_1/p_2) = 8.314 \times 300.2 \times \ln 10\,\mathrm{J} = 5747\,\mathrm{J}$; $\Delta S = nR\ln(p_1/p_2) = 19.14\,\mathrm{J\,K^{-1}}$; $\Delta G = \Delta A = -T\Delta S = -5747\,\mathrm{J}$, and $\Delta A = W$ (reversible isothermal).

(2) $W = 0$ and $Q = \Delta U = 0$; the changes of the other state functions are the same as in (1).

In process (2) $\Delta G < 0$, but one cannot use this to say by the Gibbs criterion that it is spontaneous: the pressure changes from $10p^\circ$ to $p^\circ$, which does not satisfy the isobaric condition. The entropy criterion for an isolated system must be used: $\Delta S_{\mathrm{sur}} = -Q/T = 0$, $\Delta S + \Delta S_{\mathrm{sur}} = 19.14\,\mathrm{J\,K^{-1}} > 0$, and the process is irreversible and spontaneous.

### 3.5.3. Temperature Changes and Simultaneous Changes of $p$, $V$, $T$

For an isobaric temperature change $\Delta G = -\int_{T_1}^{T_2}S\,\mathrm{d}T$; the integrand is the entropy itself, not an entropy change, so the absolute value of $S$ must be known (obtained from the **third law of thermodynamics** and the **standard molar entropy**):

$$
S(T) = S(T_0) + \int_{T_0}^{T}\frac{C_p}{T}\,\mathrm{d}T.
$$
That is, $\Delta G$ for a temperature change depends not only on the heat capacity but also on the zero of entropy, unlike isothermal processes, for which only entropy changes are used. So when calculating an isothermal phase transition or reaction one should in general not design temperature-changing steps to obtain $\Delta G$ directly (in Solution 1 of Example 3.5.3, $\Delta G$ is composed from $\Delta H$ and $\Delta S$ and not added up step by step).

**Example 3.5.2** Given $S^\circ_{\mathrm{m}}(\mathrm{He}, 298.2\,\mathrm{K}) = 126.06\,\mathrm{J\,mol^{-1}\,K^{-1}}$, find $\Delta G$ for the reversible adiabatic expansion of $1\,\mathrm{mol}$ of He from $298.2\,\mathrm{K}$ and $10p^\circ$ to $p^\circ$ (He treated as an ideal gas, $C_{p,\mathrm{m}} = \frac52 R$).

**Solution** From the reversible adiabatic equation $T^\gamma p^{1-\gamma} = $ constant ($\gamma = 5/3$),

$$
T_2 = T_1\left(\frac{p_2}{p_1}\right)^{(\gamma-1)/\gamma} = 298.2 \times 10^{-0.4}\,\mathrm{K} = 118.7\,\mathrm{K}.
$$
The process is isentropic, and $S$ remains equal to the entropy of the initial state: $S = S^\circ_{\mathrm{m}} + R\ln(p^\circ/10p^\circ) = (126.06 - 19.14)\,\mathrm{J\,K^{-1}} = 106.92\,\mathrm{J\,K^{-1}}$. Then $\Delta(TS) = S\,\Delta T$,

$$
\Delta G = \Delta H - S\,\Delta T = \left[\tfrac52 \times 8.314 \times (-179.5) - 106.92 \times (-179.5)\right]\mathrm{J} = (-3731 + 19193)\,\mathrm{J} = 15.46\,\mathrm{kJ}.
$$
It can also be computed from the fundamental equation: $\Delta G = \int(-S\,\mathrm{d}T + V\,\mathrm{d}p) = -S\Delta T + \int V\,\mathrm{d}p$, and in an isentropic process $\int V\,\mathrm{d}p = \Delta H$, giving the same result. $\square$

Here too $\Delta G > 0$ does not mean the process cannot occur: it is neither isothermal nor isobaric.

### 3.5.4. Phase Transitions

A reversible phase transition at the normal transition point is a reversible isothermal, isobaric process with $W' = 0$, for which $\Delta G = 0$ and $\Delta A = W = -p\Delta V$ ($\approx -nRT$ for vaporization). A phase transition not under phase-equilibrium conditions is irreversible, and a path must be designed.

**Example 3.5.3** Find $\Delta G$ for the complete vaporization of $1\,\mathrm{mol}$ of $\ce{H2O(l)}$ to $\ce{H2O(g)}$ at the same temperature and pressure, $298.15\,\mathrm{K}$ and $p^\circ$. Given $C_{p,\mathrm{m}}(\mathrm{l}) = 75\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $C_{p,\mathrm{m}}(\mathrm{g}) = 33\,\mathrm{J\,mol^{-1}\,K^{-1}}$, the **saturated vapor pressure** of water at $298.15\,\mathrm{K}$ is $3160\,\mathrm{Pa}$, and $\Delta_{\mathrm{vap}}H_{\mathrm{m}}(373.15\,\mathrm{K}) = 40.65\,\mathrm{kJ\,mol^{-1}}$ (for simplicity $373.15\,\mathrm{K}$ and $p^\circ$ are taken as the two-phase equilibrium point).

Solution 1 (finding $\Delta H$ and $\Delta S$ separately): design a path in which liquid water is heated at constant pressure to $373.15\,\mathrm{K}$, vaporized reversibly, and the vapor cooled at constant pressure back to $298.15\,\mathrm{K}$.

$$
\begin{aligned}
\Delta H &= [75 \times 75 + 40650 + 33 \times (-75)]\,\mathrm{J} = 43.80\,\mathrm{kJ}, \\
\Delta S &= \left[75\ln\frac{373.15}{298.15} + \frac{40650}{373.15} + 33\ln\frac{298.15}{373.15}\right]\mathrm{J\,K^{-1}} = 118.36\,\mathrm{J\,K^{-1}}, \\
\Delta G &= \Delta H - T\Delta S = (43800 - 298.15 \times 118.36)\,\mathrm{J} = 8.51\,\mathrm{kJ}.
\end{aligned}
$$
The enthalpy is unfavorable and the entropy favorable, enthalpy dominates, and $\Delta G > 0$: water at $298.15\,\mathrm{K}$ and $p^\circ$ does not vaporize spontaneously into vapor at $p^\circ$.

Solution 2 (isothermal change of pressure): design a path in which liquid water is depressurized from $p^\circ$ to the saturated vapor pressure $3160\,\mathrm{Pa}$, vaporized reversibly at that pressure ($\Delta G = 0$), and the vapor compressed isothermally to $p^\circ$. The variation of $\Delta G$ of the liquid with pressure can be neglected (3.4.4), and the vapor is treated as an ideal gas:

$$
\Delta G \approx \int_{3160\,\mathrm{Pa}}^{p^\circ}V_{\mathrm{m}}(\mathrm{g})\,\mathrm{d}p = RT\ln\frac{p^\circ}{3160\,\mathrm{Pa}} = 8.314 \times 298.15 \times \ln\frac{10^5}{3160}\,\mathrm{J} = 8.56\,\mathrm{kJ}.
$$

Solution 3 (Gibbs–Helmholtz equation): see Example 3.6.1; the result is identical to Solution 1. $\square$

The two results differ by $0.05\,\mathrm{kJ}$, for different reasons: Solutions 1 and 3 assume that the heat capacities of the two phases are constant over $298$–$373\,\mathrm{K}$ and take $1\,\mathrm{bar}$ as the equilibrium pressure at $373.15\,\mathrm{K}$ (the actual boiling point at $1\,\mathrm{bar}$ is $372.76\,\mathrm{K}$); Solution 2 uses only the measured vapor pressure and the approximation that the vapor is an ideal gas, and its data are more direct. From the standard Gibbs energies of formation in the CRC Handbook, $\Delta_{\mathrm{f}}G^\circ(\ce{H2O}, \mathrm{g}) - \Delta_{\mathrm{f}}G^\circ(\ce{H2O}, \mathrm{l}) = (-228.6) - (-237.1) = 8.5\,\mathrm{kJ\,mol^{-1}}$, consistent with both solutions. Solution 2 also shows that the vapor pressure "at $298.15\,\mathrm{K}$" in the problem is not a superfluous condition.

**Example 3.5.4** $1\,\mathrm{mol}$ of liquid benzene evaporates at $343.3\,\mathrm{K}$ into an evacuated container, the final state being benzene vapor at $343.3\,\mathrm{K}$ and $101.325\,\mathrm{kPa}$, with no non-expansion work. Given that the normal boiling point of benzene is $353.3\,\mathrm{K}$, where $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 30.85\,\mathrm{kJ\,mol^{-1}}$, and $C_{p,\mathrm{m}}(\mathrm{l}) = 135.10\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $C_{p,\mathrm{m}}(\mathrm{g}) = 81.76\,\mathrm{J\,mol^{-1}\,K^{-1}}$, find $Q$, $W$, $\Delta U$, $\Delta H$, $\Delta S$, $\Delta A$ and $\Delta G$, and decide the direction of the process.

**Solution** The state functions are calculated along the path "heat the liquid to $353.3\,\mathrm{K}$ → vaporize reversibly → cool the vapor to $343.3\,\mathrm{K}$" (all at $101.325\,\mathrm{kPa}$):

$$
\begin{aligned}
\Delta H &= [30850 + (135.10 - 81.76) \times 10]\,\mathrm{J} = 31.38\,\mathrm{kJ}, \\
\Delta S &= \left[(135.10 - 81.76)\ln\frac{353.3}{343.3} + \frac{30850}{353.3}\right]\mathrm{J\,K^{-1}} = 88.85\,\mathrm{J\,K^{-1}}, \\
\Delta G &= \Delta H - T\Delta S = (31383 - 343.3 \times 88.85)\,\mathrm{J} = 0.88\,\mathrm{kJ}.
\end{aligned}
$$
Neglecting the volume of the liquid and treating the vapor as an ideal gas, $\Delta U = \Delta H - \Delta(pV) \approx \Delta H - nRT = 28.53\,\mathrm{kJ}$ and $\Delta A = \Delta U - T\Delta S = -1.97\,\mathrm{kJ}$. In the actual process of evaporation into vacuum, $W = 0$ and $Q = \Delta U = 28.53\,\mathrm{kJ}$.

Direction: the process is not isobaric, so $\Delta G > 0$ cannot be used to decide. The entropy change of the surroundings is $\Delta S_{\mathrm{sur}} = -Q/T = -83.10\,\mathrm{J\,K^{-1}}$ and the total entropy change $\Delta S + \Delta S_{\mathrm{sur}} = 5.75\,\mathrm{J\,K^{-1}} > 0$, so the process is spontaneous. Another way to see it: taking benzene and the evacuated container together as the system, the process is isothermal, the total volume is constant and $W' = 0$, and the Helmholtz criterion $\Delta A < 0$ gives the same conclusion. $\square$

$\Delta G = 0.88\,\mathrm{kJ} > 0$ also has a meaning: at $343.3\,\mathrm{K}$ the pressure of the final-state vapor is higher than the saturated vapor pressure of benzene. From $\Delta G = RT\ln(p/p^*)$ the vapor pressure of benzene at $343.3\,\mathrm{K}$ is estimated as $p^* \approx 101.3\,\mathrm{kPa} \times \mathrm{e}^{-0.31} \approx 74\,\mathrm{kPa}$, and the final state is a supersaturated vapor.

### 3.5.5. Mixing Processes

For different ideal gases mixing at constant temperature and pressure, $\Delta_{\mathrm{mix}}H = 0$, and from the **entropy of mixing** $\Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}$ ([6.3.2](/6.3.2)),

$$
\Delta_{\mathrm{mix}}G = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}} < 0.
$$
This holds only for the isothermal, isobaric mixing of different ideal gases; for other mixing processes (such as two gases with different initial pressures), first find $\Delta G_{\mathrm{B}}$ of each gas separately and then add. The Gibbs energy of each component in a mixture is described by the chemical potential, and the derivation of the above equation from it is in [6.3.4](/6.3.4).

### 3.5.6. Chemical Reactions

For an isothermal reaction in the standard state, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T)$; $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ at $298.15\,\mathrm{K}$ are obtained from the **standard molar enthalpies of formation** and **standard molar entropies** in handbooks, or directly from the **standard molar Gibbs energies of formation** ([6.1.6](/6.1.6#sec-6.4.8)). Values at other temperatures are obtained by correcting $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ with **Kirchhoff's law** ([6.3.1](/6.3.1)), or with the Gibbs–Helmholtz equation (3.6). $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ under nonstandard conditions and the equilibrium constant are in [6.3.7](/6.3.7).

### 3.5.7. Pressure Effects on Condensed Phases

The variation of $\Delta G$ of condensed phases with pressure is small, but at high enough pressure it can change the stability of phases. From $(\partial\Delta G/\partial p)_T = \Delta V$:

**Example 3.5.5** At $298.15\,\mathrm{K}$ and $p^\circ$, $\Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}} = 2.900\,\mathrm{kJ\,mol^{-1}}$ for $\ce{C(graphite) -> C(diamond)}$ (CRC, consistent with [6.1.14](/6.1.14)), and the densities of diamond and graphite are $3513\,\mathrm{kg\,m^{-3}}$ and $2260\,\mathrm{kg\,m^{-3}}$. At least what pressure must be applied at $298.15\,\mathrm{K}$ before graphite can turn into diamond?

**Solution** $\Delta V_{\mathrm{m}} = M(1/\rho_{\text{diamond}} - 1/\rho_{\text{graphite}}) = 12.011 \times 10^{-3} \times (1/3513 - 1/2260)\,\mathrm{m^3\,mol^{-1}} = -1.896 \times 10^{-6}\,\mathrm{m^3\,mol^{-1}}$. Assuming that $\Delta V_{\mathrm{m}}$ does not vary with pressure,

$$
\Delta_{\mathrm{trs}}G_{\mathrm{m}}(p) = \Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}} + \Delta V_{\mathrm{m}}(p - p^\circ) = 0 \;\Longrightarrow\; p = p^\circ - \frac{\Delta_{\mathrm{trs}}G^\circ_{\mathrm{m}}}{\Delta V_{\mathrm{m}}} = 1.53 \times 10^9\,\mathrm{Pa}.
$$
That is, at room temperature diamond is more stable than graphite only above about $1.5\,\mathrm{GPa}$. $\square$

From $(\partial\Delta G/\partial T)_p = -\Delta S$ ($\Delta_{\mathrm{trs}}S^\circ_{\mathrm{m}} = 2.38 - 5.74 = -3.36\,\mathrm{J\,mol^{-1}\,K^{-1}}$), raising the temperature raises the equilibrium pressure, and the slope of the phase boundary is $\mathrm{d}p/\mathrm{d}T = \Delta S/\Delta V \approx 1.8\,\mathrm{MPa\,K^{-1}}$ (this is the Clapeyron equation of [6.3.8](/6.3.8)). At high temperature $\Delta S$ and $\Delta V$ themselves vary with temperature, and the experimentally measured phase boundary (the Berman–Simon line) is steeper. Thermodynamics shows only that high pressure favors diamond; the activation energy for graphite to transform at ordinary temperature is extremely high, and practical synthesis takes place at $5$–$6\,\mathrm{GPa}$ and $1600$–$2100\,\mathrm{K}$, with molten metals (Fe, Ni, Co) as solvent and catalyst. Diamond grown by low-pressure chemical vapor deposition (CVD) is in a metastable state, which depends on kinetic selectivity of surface reactions and not on a change of the thermodynamic equilibrium.

![Graphite–diamond transition: variation of Δ_trs G_m with pressure at 298.15 K (left, ΔV taken as constant); the two-phase equilibrium line (right): the constant-ΔS, ΔV approximation of this section and the experimental Berman–Simon line, together with the approximate range of industrial high-temperature, high-pressure synthesis.](./plots/graphite-diamond.py)

## 3.6. The Gibbs–Helmholtz Equation

For a chemical reaction only the value of $\Delta_{\mathrm{r}}G$ at one temperature is often known, and the value at other temperatures is wanted.

**Theorem 3.6.1 (Gibbs–Helmholtz Equation)** For any equilibrium state of a closed system of constant composition,

$$
\left[\frac{\partial(G/T)}{\partial T}\right]_p = -\frac{H}{T^2}, \qquad \left[\frac{\partial(A/T)}{\partial T}\right]_V = -\frac{U}{T^2}.
\tag{3.9}
$$
For a process (phase transition, chemical reaction) whose initial and final states have the same temperature and the same pressure,

$$
\left[\frac{\partial(\Delta G/T)}{\partial T}\right]_p = -\frac{\Delta H}{T^2}.
\tag{3.10}
$$

**Proof** By the quotient rule and $(\partial G/\partial T)_p = -S$,

$$
\left[\frac{\partial(G/T)}{\partial T}\right]_p = \frac{T(\partial G/\partial T)_p - G}{T^2} = \frac{-TS - G}{T^2} = -\frac{H}{T^2}.
$$
The case of $A/T$ is the same, using $(\partial A/\partial T)_V = -S$ and $A + TS = U$. For a process, the initial and final states each satisfy Eq. (3.9), and subtracting gives Eq. (3.10). $\square$

Eq. (3.10) can also be written $[\partial(\Delta G/T)/\partial(1/T)]_p = \Delta H$: in a plot of $\Delta G/T$ against $1/T$ the slope is $\Delta H$. The combination $\Delta G/T$ has a direct meaning: at constant temperature and pressure with $W' = 0$, $-\Delta G/T = \Delta S + \Delta S_{\mathrm{sur}}$ is the total entropy change of the large isolated system ([6.1.6](/6.1.6#sec-6.4.7)), so Eq. (3.10) describes the variation of the total entropy change with temperature.

Distinguish $(\partial G/\partial T)_p = -S$ from Eq. (3.9): the former is the temperature coefficient of $G$ itself and requires the absolute value of entropy; the latter is the temperature coefficient of $G/T$ and requires only the enthalpy, and the enthalpy (or $\Delta H$) can be determined calorimetrically. This is why Eq. (3.10) is used to calculate $\Delta G$ at another temperature from $\Delta G$ at one temperature. Integrating at constant pressure:

$$
\frac{\Delta G(T_2)}{T_2} = \frac{\Delta G(T_1)}{T_1} - \int_{T_1}^{T_2}\frac{\Delta H(T)}{T^2}\,\mathrm{d}T.
\tag{3.11}
$$
If $\Delta H$ is independent of temperature, $\Delta G(T_2)/T_2 = \Delta G(T_1)/T_1 + \Delta H(1/T_2 - 1/T_1)$; if $\Delta C_p$ is constant, then by Kirchhoff's law $\Delta H(T) = \Delta H(T_1) + \Delta C_p(T - T_1)$, and substituting into the integral gives

$$
\frac{\Delta G(T_2)}{T_2} = \frac{\Delta G(T_1)}{T_1} + \Delta H(T_1)\left(\frac{1}{T_2} - \frac{1}{T_1}\right) - \Delta C_p\left(\ln\frac{T_2}{T_1} + \frac{T_1}{T_2} - 1\right).
$$

**Example 3.6.1** Use the Gibbs–Helmholtz equation to find $\Delta G$ for the vaporization of water at $298.15\,\mathrm{K}$ in Example 3.5.3.

**Solution** Take $T_1 = 373.15\,\mathrm{K}$ (two-phase equilibrium, $\Delta G(T_1) = 0$), $T_2 = 298.15\,\mathrm{K}$, $\Delta H(T_1) = 40650\,\mathrm{J}$ and $\Delta C_p = (33 - 75)\,\mathrm{J\,K^{-1}} = -42\,\mathrm{J\,K^{-1}}$. Substituting into the equation above:

$$
\frac{\Delta G(T_2)}{T_2} = 40650 \times \left(\frac{1}{298.15} - \frac{1}{373.15}\right) + 42 \times \left(\ln\frac{298.15}{373.15} + \frac{373.15}{298.15} - 1\right) = (27.40 + 1.14)\,\mathrm{J\,K^{-1}},
$$
$\Delta G(T_2) = 298.15 \times 28.54\,\mathrm{J} = 8.51\,\mathrm{kJ}$, the same as in Solution 1 (the two use the same data and approximations). $\square$

Applied to $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$, the Gibbs–Helmholtz equation becomes the van 't Hoff equation for the temperature dependence of the equilibrium constant ([6.3.7](/6.3.7)); applied to $\Delta_{\mathrm{r}}G_{\mathrm{m}} = -zFE_{\mathrm{cell}}$, it gives the reaction enthalpy from the cell voltage and its temperature coefficient ([6.3.13](/6.3.13)).

## Summary

| Content | Relation | Conditions |
|---|---|---|
| Maximum work | $-W \le -\Delta A$ | Closed system, isothermal |
| Maximum non-expansion work | $-W' \le -\Delta G$ | Closed system, isothermal, isobaric |
| Criteria | $\Delta A \le 0$; $\Delta G \le 0$ | Plus constant volume or constant pressure, and $W' = 0$ |
| Fundamental equations | $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ and three others | Closed system of constant composition, $W' = 0$, between neighboring equilibrium states (reversible or not) |
| Maxwell relations | $(\partial S/\partial V)_T = (\partial p/\partial T)_V$, $(\partial S/\partial p)_T = -(\partial V/\partial T)_p$, etc. | Same |
| Thermodynamic equation of state | $(\partial U/\partial V)_T = T(\partial p/\partial T)_V - p$ | Any substance |
| Difference of heat capacities | $C_p - C_V = TV\alpha_V^2/\kappa_T$ | Any substance |
| Gibbs–Helmholtz equation | $[\partial(\Delta G/T)/\partial T]_p = -\Delta H/T^2$ | Same $T$, $p$ in initial and final states |

- The condition of a criterion is that "the temperature (pressure) of the initial and final states equals the temperature (pressure) of the surroundings"; when it is not satisfied the sign of $\Delta G$ cannot be used to judge direction, and one returns to the entropy criterion for an isolated system.
- $U$, $H$, $A$ and $G$ are Legendre transforms of one another, and each is a characteristic function in its natural variables; chemistry centers on $G(T, p)$ because $T$ and $p$ are the easiest to control.
- For an isothermal process $\Delta G = \Delta H - T\Delta S$; when the temperature changes $\Delta G$ depends on the absolute value of entropy, and the Gibbs–Helmholtz equation is used to change temperature.
