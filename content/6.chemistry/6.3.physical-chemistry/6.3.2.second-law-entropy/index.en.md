---
title: The Second Law and Entropy
description: Common features of spontaneous processes and statements of the second law; Carnot's theorem and the Brayton cycle; entropy, the integrating factor and the Clausius inequality; the principle of entropy increase and the entropy change of the surroundings; entropy changes of ideal-gas pVT changes, heat transfer, mixing and phase transitions; the Nernst heat theorem, perfect crystals and the third law, calorimetric entropy and the Debye T³ extrapolation; entropy changes of chemical reactions; entropy and the degradation of energy.
source_hash: 459626e13ea9
---

The first law of thermodynamics states that energy is conserved, but it cannot tell the direction of a process. A gas does not flow spontaneously from low pressure to high pressure, heat does not pass spontaneously from a cold body to a hot one, and the reaction $\ce{H2(g) + 1/2O2(g) -> H2O(l)}$ releases $286\,\mathrm{kJ\,mol^{-1}}$ of heat, yet returning that heat to the water does not decompose it. If energy is conserved, why is there an "energy crisis" at all? The second law of thermodynamics answers these questions. In physics it was built up from the efficiency of heat engines ([5.2.4](/5.2.4)): two statements, Carnot's theorem, Clausius entropy and Boltzmann entropy. This chapter reorganizes the material from the needs of chemistry, with emphasis on calculations that can be carried out: which criterion to use under which conditions, how to design a reversible path for an irreversible process in order to compute its entropy change, and how to obtain the conventional entropies of substances from calorimetric data and the third law, and with them the entropy changes of chemical reactions. The entropy criterion requires that system and surroundings be considered together, which is inconvenient; the next chapter ([6.3.3](/6.3.3)) derives from it the Helmholtz and Gibbs energy criteria, which involve the system alone. The statistical meaning of entropy ($S = k_{\mathrm{B}}\ln\Omega$) is developed quantitatively in [6.3.10](/6.3.10), and entropy production and entropy flux in open systems are treated in [6.3.18](/6.3.18).

## 2.1. Spontaneous Processes and the Second Law

### 2.1.1. Common Features of Spontaneous Processes

A process that can proceed by itself under given environmental conditions without work from the surroundings is called a **spontaneous process** ([6.1.6, Definition 6.4.1](/6.1.6#def-6.4.1)); what is ordinarily called the "direction of a process" is the direction of spontaneous processes. Water flows from high to low, heat passes from a hot body to a cold one, and solutes diffuse from regions of high concentration to regions of low concentration. Every spontaneous process has a definite direction, and its reverse cannot proceed by itself.

Take $1\,\mathrm{m^3}$ of $\ce{N2}$ at $273\,\mathrm{K}$ and $4\,\mathrm{kPa}$ as an example. Expansion into vacuum to $1\,\mathrm{kPa}$ (volume $4\,\mathrm{m^3}$) is spontaneous, with $W = Q = 0$. To restore the gas, it can be compressed isothermally against a constant external pressure of $4\,\mathrm{kPa}$; the surroundings do work $W = 4\,\mathrm{kPa} \times 3\,\mathrm{m^3} = 12\,\mathrm{kJ}$ and the system gives $12\,\mathrm{kJ}$ of heat to the reservoir. The system is restored, but the surroundings have "lost work and gained heat"; the surroundings can be restored only if this $12\,\mathrm{kJ}$ of heat is converted entirely back into work with no other change. The common features of spontaneous processes are:

1. A spontaneous process proceeds in one direction, from nonequilibrium toward equilibrium, and its limit is the equilibrium state.
2. A spontaneous process has the capacity to do work ([6.1.6](/6.1.6#sec-6.4.1)); a device can be designed to use it to deliver work.
3. Spontaneous processes are all **irreversible processes**: without exception, the surroundings must pay a price to make them go back.

The irreversibility of every spontaneous process can be reduced to one fact: work can be converted entirely into heat at no cost, but heat cannot be converted entirely into work at no cost. Note that it is not that heat cannot be entirely converted into work (in reversible isothermal expansion of an ideal gas all the absorbed heat is turned into work), but that doing so necessarily leaves other changes (here, the increase in volume of the gas).

### 2.1.2. Statements of the Second Law

The **second law of thermodynamics** has several equivalent statements ([5.2.4, Theorem 4.2.1](/5.2.4#thm-4.2.1)):

- The **Clausius statement**: heat cannot pass from a colder body to a hotter body without causing other changes.
- The **Kelvin statement**: it is impossible to take heat from a single reservoir and convert it completely into work without other changes.
- The Ostwald statement: a **perpetual motion machine of the second kind** is impossible.

They summarize a great body of experience, and their equivalence is proved by contradiction ([5.2.4](/5.2.4#sec-4.2.2)). Any irreversible process can, by a suitable path, be linked to the irreversibility of the conversion between heat and work, so the second law can be used to judge the direction of any process. But using the verbal statements directly takes great skill; we need a quantitative criterion, and this starts from the efficiency of heat engines.

A heat engine working cyclically between two reservoirs absorbs heat $Q_1 > 0$ from the high-temperature reservoir $T_{\mathrm{h}}$, releases heat $Q_2 < 0$ to the low-temperature reservoir $T_{\mathrm{c}}$, and does work $-W = Q_1 + Q_2$ on the surroundings; its efficiency is $\eta = -W/Q_1 = 1 + Q_2/Q_1$. **Carnot's theorem** ([5.2.4, Theorem 4.4.1](/5.2.4#thm-4.4.1)) says that among all heat engines working between the same two reservoirs the reversible engine has the highest efficiency, and that all reversible engines have the same efficiency, independent of the working substance, equal to the efficiency of the **Carnot cycle**. In mathematical form:

$$
1 + \frac{Q_2}{Q_1} \le 1 - \frac{T_{\mathrm{c}}}{T_{\mathrm{h}}} \quad\Longleftrightarrow\quad \frac{Q_1}{T_{\mathrm{h}}} + \frac{Q_2}{T_{\mathrm{c}}} \le 0,
\tag{2.1}
$$

with equality for reversible cycles and inequality for irreversible ones. Its practical meaning is that it gives an upper bound on the efficiency of heat engines and shows that the fundamental way to raise efficiency is to increase the temperature difference between the two reservoirs; its theoretical meaning is that Clausius discovered entropy from it.

**Example 2.1.1 (Brayton Cycle)** A gas turbine works on the Brayton cycle: (1) the compressor takes in ambient air at temperature $T_1$ and compresses it adiabatically to $T_{\mathrm{comp}}$; (2) the compressed air is heated at constant pressure in the combustion chamber to $T_2$; (3) the hot, high-pressure gas expands adiabatically through the turbine, doing work, and cools to $T_3$; (4) the exhaust releases heat at low pressure at constant pressure and returns to $T_1$. Treating air as an ideal gas and every step as reversible, find the efficiency of the cycle. For given $T_1$ and combustion-chamber temperature $T_2$, what is the highest efficiency that can be reached?

Solution: In the two isobaric processes the heat absorbed is $Q_1 = nC_{p,\mathrm{m}}(T_2 - T_{\mathrm{comp}})$ and the heat released is $Q_2 = -nC_{p,\mathrm{m}}(T_3 - T_1)$. The two adiabatic processes take place between the same two pressures, so from the adiabatic equation $T^\gamma p^{1-\gamma} = $ constant ([6.3.1](/6.3.1)), $T_{\mathrm{comp}}/T_1 = T_2/T_3 = (p_{\text{high}}/p_{\text{low}})^{(\gamma-1)/\gamma}$, that is, $T_3 = T_1T_2/T_{\mathrm{comp}}$. Then

$$
\eta = 1 + \frac{Q_2}{Q_1} = 1 - \frac{T_3 - T_1}{T_2 - T_{\mathrm{comp}}} = 1 - \frac{T_1}{T_{\mathrm{comp}}}.
$$

The efficiency is determined by the compression ratio alone. $T_{\mathrm{comp}}$ cannot exceed the combustion-chamber temperature $T_2$, so $\eta < 1 - T_1/T_2$: as $T_{\mathrm{comp}} \to T_2$ the efficiency tends to the Carnot efficiency for operation between $T_1$ and $T_2$, but then the combustion chamber hardly heats the air any more, and the net work per mole of air, $nC_{p,\mathrm{m}}[(T_2 - T_3) - (T_{\mathrm{comp}} - T_1)]$, tends to zero. The "maximum efficiency $1 - T_1/T_2$" is therefore an unattainable upper bound; in practical design the operating point of interest is that of maximum net work. Extremizing with respect to $T_{\mathrm{comp}}$ gives $T_{\mathrm{comp}} = \sqrt{T_1T_2}$, at which $\eta = 1 - \sqrt{T_1/T_2}$. For $T_1 = 300\,\mathrm{K}$ and $T_2 = 1500\,\mathrm{K}$ the Carnot limit is $0.80$, the efficiency at maximum net work is $0.55$, and the compression ratio is about $17$. The efficiency of the Brayton cycle is below the Carnot efficiency because it absorbs heat over one range of temperatures and releases heat over another, instead of exchanging heat only with two isothermal reservoirs.

![Ideal Brayton cycle between ambient 300 K and burner 1500 K: the efficiency rises towards the Carnot limit as the compression outlet temperature Tcomp approaches T2, while the net work per mole of air vanishes there; the work is largest at Tcomp = √(T1T2)](./plots/brayton-cycle.py)

## 2.2. Entropy and the Clausius Inequality

### 2.2.1. Entropy

For a reversible cycle between two reservoirs, Eq. (2.1) gives a vanishing sum of "heat–temperature quotients": $Q_1/T_{\mathrm{h}} + Q_2/T_{\mathrm{c}} = 0$. Any reversible cycle can be assembled from many small Carnot cycles (the common adiabat of neighboring small cycles is traversed once in each direction, and the contributions cancel); in the limit of infinitely many small cycles one obtains the **Clausius equality** ([5.2.4, Theorem 4.5.1](/5.2.4#thm-4.5.1))

$$
\oint\left(\frac{\delta Q}{T}\right)_{\mathrm{r}} = 0.
$$

Let a system go from state A to state B along a reversible path $\mathrm{R}_1$ and return to A along another reversible path $\mathrm{R}_2$. Then $\int_{\mathrm{A}}^{\mathrm{B}}(\delta Q/T)_{\mathrm{R}_1} = \int_{\mathrm{A}}^{\mathrm{B}}(\delta Q/T)_{\mathrm{R}_2}$: the sum of the heat–temperature quotients for a reversible process between two equilibrium states is independent of path. There is therefore a state function, which Clausius named **entropy** in 1865 ([5.2.4, Definition 4.5.1](/5.2.4#def-4.5.1)):

$$
\mathrm{d}S = \frac{\delta Q_{\mathrm{r}}}{T}, \qquad \Delta S = S_2 - S_1 = \int_1^2\frac{\delta Q_{\mathrm{r}}}{T}.
\tag{2.2}
$$

In the language of differential equations, $\delta Q_{\mathrm{r}}$ is not a total differential and $1/T$ is its **integrating factor** ([2.2.15, Definition 15.4.2](/2.2.15#def-15.4.2)). For an ideal gas, for example, $\delta Q_{\mathrm{r}} = \mathrm{d}U - \delta W_{\mathrm{r}} = C_V\,\mathrm{d}T + \frac{nRT}{V}\,\mathrm{d}V$; the cross derivatives are $\partial C_V/\partial V = 0$ and $\partial(nRT/V)/\partial T = nR/V$, which are unequal, so $\delta Q_{\mathrm{r}}$ is the total differential of no function. After division by $T$,

$$
\frac{\delta Q_{\mathrm{r}}}{T} = \frac{C_V}{T}\,\mathrm{d}T + \frac{nR}{V}\,\mathrm{d}V, \qquad \frac{\partial}{\partial V}\left(\frac{C_V}{T}\right) = 0 = \frac{\partial}{\partial T}\left(\frac{nR}{V}\right),
$$

the condition for a total differential is satisfied, and the expression is $\mathrm{d}S$. The content of the second law can be summarized thus: for any system, $\delta Q_{\mathrm{r}}$ has an integrating factor $1/T$ that depends only on temperature and is the same for all substances.

About entropy: it is the fundamental state function of the second law, an extensive quantity with the unit $\mathrm{J\,K^{-1}}$. A system undergoing any process (reversible or irreversible) has a definite entropy change, numerically equal to the sum of the heat–temperature quotients along any reversible path between the initial and final states. The heat–temperature quotient of an irreversible process, however, is not equal to the entropy change; the relation between them is considered next.

### 2.2.2. The Clausius Inequality

By Eq. (2.1), for an irreversible cycle between two reservoirs $Q_1/T_{\mathrm{h}} + Q_2/T_{\mathrm{c}} < 0$; generalizing to an arbitrary irreversible cycle in contact with a series of reservoirs, $\sum_i\delta Q_i/T_i < 0$, where $T_i$ is the temperature of the reservoir that exchanges heat $\delta Q_i$ with the system. Let a system go from state 1 to state 2 by an irreversible process and return to 1 by a reversible process, forming an irreversible cycle:

$$
\int_1^2\left(\frac{\delta Q}{T_{\mathrm{sur}}}\right)_{\mathrm{ir}} + \int_2^1\left(\frac{\delta Q}{T}\right)_{\mathrm{r}} < 0 \quad\Longrightarrow\quad \Delta S = S_2 - S_1 > \int_1^2\left(\frac{\delta Q}{T_{\mathrm{sur}}}\right)_{\mathrm{ir}}.
$$

Together with the reversible case this is the **Clausius inequality** ([5.2.4, Theorem 4.6.1](/5.2.4#thm-4.6.1)):

$$
\Delta S \ge \int_1^2\frac{\delta Q}{T_{\mathrm{sur}}}, \qquad \mathrm{d}S \ge \frac{\delta Q}{T_{\mathrm{sur}}} \qquad (> \text{irreversible},\ = \text{reversible}).
\tag{2.3}
$$

Points to note about Eq. (2.3):

1. It relates the entropy change of any process in a closed system to the heat–temperature quotient. It is the mathematical expression of the second law and is equivalent to the impossibility of a perpetual motion machine of the second kind: in a closed system no process can occur whose entropy change is less than the heat–temperature quotient.
2. The denominator $T_{\mathrm{sur}}$ is the temperature of the surroundings (the reservoir). In an irreversible process the system may have no uniform temperature at all; only for the equality (a reversible process), where $T_{\mathrm{sur}} = T$, can it be interpreted as the temperature of the system.
3. Use: comparing the entropy change of a process with the heat–temperature quotient shows whether the process is irreversible ($>$), reversible ($=$) or impossible ($<$). The drawback is that both $\Delta S$ and the heat–temperature quotient must be computed, and the latter depends on the process, so the calculation is often troublesome.

### 2.2.3. The Principle of Entropy Increase and the Entropy Criterion

For an adiabatic system $\delta Q = 0$, and Eq. (2.3) becomes

$$
\Delta S_{\text{adiabatic}} \ge 0 \qquad (> \text{irreversible},\ = \text{reversible}):
$$

the entropy of an adiabatic system cannot decrease. This is the **principle of entropy increase** ([5.2.4, Theorem 4.6.2](/5.2.4#thm-4.6.2)); a reversible adiabatic process is an **isentropic process**. An **isolated system** is of course adiabatic, and an irreversible process occurring in an isolated system is not driven from outside and must be spontaneous, so

$$
\Delta S_{\text{isolated}} \ge 0 \qquad (> \text{spontaneous},\ = \text{reversible, that is, equilibrium}).
$$

Processes in an isolated system always proceed in the direction of increasing entropy, and the limit is the equilibrium state in which the entropy reaches its maximum. This entropy criterion settles both the direction and the limit of processes in an isolated system; macroscopically, entropy is the measure of the stability of an isolated system.

Real systems are seldom isolated. The remedy is to combine the system and the surroundings that interact with it into one "large isolated system":

$$
\Delta S_{\text{isolated}} = \Delta S_{\text{system}} + \Delta S_{\text{surroundings}} \ge 0.
$$

The surroundings are usually a huge reservoir at temperature $T_{\mathrm{sur}}$ (the atmosphere, a thermostat bath); a finite flow of heat into or out of it changes neither its temperature nor its internal equilibrium, so for the surroundings themselves such heat transfer can always be regarded as reversible, and the heat absorbed by the surroundings is the actual heat released by the system, $-Q_{\text{system}}$. Therefore

$$
\Delta S_{\text{surroundings}} = \frac{Q_{\text{surroundings}}}{T_{\mathrm{sur}}} = -\frac{Q_{\text{system}}}{T_{\mathrm{sur}}}.
\tag{2.4}
$$

Here $Q_{\text{system}}$ is the heat of the actual process, not the heat of the reversible path designed for computing the entropy change of the system. Substituting Eq. (2.4) into the entropy criterion gives $\Delta S_{\text{system}} - Q_{\text{system}}/T_{\mathrm{sur}} \ge 0$, which agrees with the Clausius inequality (2.3) (for constant $T_{\mathrm{sur}}$). The scope of the three criteria:

| Criterion | Form | Applies to |
|---|---|---|
| Clausius inequality | $\Delta S \ge \int\delta Q/T_{\mathrm{sur}}$ | Any process in a closed system: decides reversibility |
| Principle of entropy increase | $\Delta S \ge 0$ | Adiabatic system: decides reversibility |
| Entropy criterion | $\Delta S_{\text{system}} + \Delta S_{\text{surroundings}} \ge 0$ | Isolated system (or system plus surroundings): decides spontaneity and equilibrium |

## 2.3. Calculation of Entropy Changes

### 2.3.1. Basic Method

By Eq. (2.2), an entropy change can be calculated only along a reversible path: if the process is reversible, use $\Delta S = \int\delta Q_{\mathrm{r}}/T$ directly; if the process is irreversible, design a reversible path between the same initial and final states (made up of isothermal, isobaric and isochoric reversible steps and reversible phase transitions) and calculate along it. Entropy is extensive, and the entropy change of a complex system is the sum of the entropy changes of its parts. The processes to be calculated fall into three kinds: simple physical changes ($pVT$ changes, heat transfer), complex physical changes (mixing, phase transitions) and chemical reactions (Section 2.4.3).

### 2.3.2. Simple $pVT$ Changes

For a reversible isothermal process $\Delta S = Q_{\mathrm{r}}/T$; for an ideal gas $Q_{\mathrm{r}} = -W_{\mathrm{r}} = nRT\ln(V_2/V_1)$. For a simple temperature change at constant volume or constant pressure, $\delta Q_{\mathrm{r}} = C_V\,\mathrm{d}T$ or $C_p\,\mathrm{d}T$:

$$
\Delta S = \int_{T_1}^{T_2}\frac{C_V}{T}\,\mathrm{d}T \quad(\text{isochoric}), \qquad \Delta S = \int_{T_1}^{T_2}\frac{C_p}{T}\,\mathrm{d}T \quad(\text{isobaric}),
$$

that is, $(\partial S/\partial T)_V = C_V/T$ and $(\partial S/\partial T)_p = C_p/T$: entropy increases with temperature, by $C/T$ per kelvin. For constant heat capacity $\Delta S = C\ln(T_2/T_1)$. These two formulas hold equally for condensed phases and real gases. When $p$, $V$ and $T$ of an ideal gas all change, design two steps: first isothermal and then isobaric (or first isothermal and then isochoric, or first isobaric and then isochoric), which gives

$$
\Delta S = nR\ln\frac{p_1}{p_2} + nC_{p,\mathrm{m}}\ln\frac{T_2}{T_1} = nR\ln\frac{V_2}{V_1} + nC_{V,\mathrm{m}}\ln\frac{T_2}{T_1} = nC_{p,\mathrm{m}}\ln\frac{V_2}{V_1} + nC_{V,\mathrm{m}}\ln\frac{p_2}{p_1}
\tag{2.5}
$$

(for constant $C_{V,\mathrm{m}}$). The three forms are interconverted by $pV = nRT$ and need not be memorized; it suffices to master the method of designing paths. For any isothermal process of an ideal gas (reversible or not), $\Delta S = nR\ln(p_1/p_2)$.

**Example 2.3.1** $1\,\mathrm{mol}$ of He (ideal gas, $C_{V,\mathrm{m}} = \frac{3}{2}R$) goes from $273.15\,\mathrm{K}$ and $1\,\mathrm{MPa}$ to $100\,\mathrm{kPa}$ by each of the following processes: (1) reversible isothermal; (2) isothermal expansion against a constant external pressure of $100\,\mathrm{kPa}$; (3) cooling at constant volume; (4) reversible adiabatic; (5) adiabatic expansion against a constant external pressure of $100\,\mathrm{kPa}$. Find the entropy change of each process.

Solution: (1) $\Delta S = R\ln(p_1/p_2) = R\ln 10 = 19.14\,\mathrm{J\,K^{-1}}$.

(2) The final state is the same as in (1), and entropy is a state function, so $\Delta S = 19.14\,\mathrm{J\,K^{-1}}$. The heat of the actual process is $Q = -W = p_2(V_2 - V_1) = RT(1 - p_2/p_1) = 2044\,\mathrm{J}$, and the heat–temperature quotient is $Q/T = 7.48\,\mathrm{J\,K^{-1}} < \Delta S$, so the process is irreversible. The entropy change of the surroundings is $-Q/T = -7.48\,\mathrm{J\,K^{-1}}$ and the entropy of the isolated system increases by $11.66\,\mathrm{J\,K^{-1}}$; in process (1), by contrast, the entropy change of the surroundings is $-19.14\,\mathrm{J\,K^{-1}}$ and the total entropy change is zero.

(3) At constant volume the pressure falls to one tenth, $T_2 = 27.3\,\mathrm{K}$, and $\Delta S = C_{V,\mathrm{m}}\ln(T_2/T_1) = \frac{3}{2}R\ln 0.1 = -28.72\,\mathrm{J\,K^{-1}}$.

(4) Reversible adiabatic, $\Delta S = 0$.

(5) By the method of [6.3.1, Example 1.4.1](/6.3.1#sec-1.4.3), $T_2 = \frac{C_{V,\mathrm{m}} + Rp_2/p_1}{C_{p,\mathrm{m}}}T_1 = 174.8\,\mathrm{K}$. Design a path: first expand reversibly and isothermally at $273.15\,\mathrm{K}$ to $100\,\mathrm{kPa}$, then cool reversibly at constant pressure to $174.8\,\mathrm{K}$. By Eq. (2.5),

$$
\Delta S = R\ln 10 + \frac{5}{2}R\ln\frac{174.8}{273.15} = 19.14 - 9.28 = 9.87\,\mathrm{J\,K^{-1}} > 0.
$$

The entropy of the adiabatic process increases and the process is irreversible, in agreement with the principle of entropy increase.

This example explains the conclusion of [6.3.1](/6.3.1#sec-1.4.3) that "starting from the same initial state, reversible and irreversible adiabatic processes cannot reach the same final state": for the former $\Delta S = 0$ and for the latter $\Delta S > 0$, so the entropies of the two final states differ. For expansion to the same final pressure, since $(\partial S/\partial T)_p = C_p/T > 0$, the final state of larger entropy has the higher temperature, $T_{2,\mathrm{ir}} > T_{2,\mathrm{r}}$; and since $W = \Delta U = nC_{V,\mathrm{m}}(T_2 - T_1)$, reversible adiabatic expansion cools the gas most and does the most work.

### 2.3.3. Heat Transfer

**Example 2.3.2** An adiabatic container is divided by a fixed adiabatic partition into two parts containing $1\,\mathrm{mol}$ of He ($200\,\mathrm{K}$) and $1\,\mathrm{mol}$ of $\ce{H2}$ ($300\,\mathrm{K}$), both at $100\,\mathrm{kPa}$. The partition is replaced by a fixed aluminum plate (heat conducting, with negligible heat capacity). Find $\Delta H$ and $\Delta S$ after equilibrium is reached. For He $C_{V,\mathrm{m}} = \frac{3}{2}R$, and for $\ce{H2}$ $C_{V,\mathrm{m}} = \frac{5}{2}R$.

Solution: First determine the final state. Taking the two gases as the system, $Q = 0$ and $W = 0$, so $\Delta U = \Delta U(\mathrm{He}) + \Delta U(\ce{H2}) = 0$:

$$
\tfrac{3}{2}R(T_2 - 200\,\mathrm{K}) + \tfrac{5}{2}R(T_2 - 300\,\mathrm{K}) = 0, \qquad T_2 = 262.5\,\mathrm{K}.
$$

Both gases undergo a temperature change at constant volume:

$$
\begin{aligned}
\Delta H &= \tfrac{5}{2}R(262.5 - 200)\,\mathrm{K} + \tfrac{7}{2}R(262.5 - 300)\,\mathrm{K} = 207.9\,\mathrm{J},\\
\Delta S &= \tfrac{3}{2}R\ln\frac{262.5}{200} + \tfrac{5}{2}R\ln\frac{262.5}{300} = 3.39 - 2.78 = 0.62\,\mathrm{J\,K^{-1}} > 0.
\end{aligned}
$$

The system is isolated and its entropy increases: heat conduction is a spontaneous irreversible process. Note that for the isolated system $\Delta U = 0$ but $\Delta H \ne 0$: $\Delta H = \Delta U + V\Delta p$, and the pressure has changed on both sides.

In general, for two identical bodies of isobaric heat capacity $C_p$ at temperatures $T_{\mathrm{h}}$ and $T_{\mathrm{c}}$, which reach $T_2 = (T_{\mathrm{h}} + T_{\mathrm{c}})/2$ after contact,

$$
\Delta S = C_p\ln\frac{T_2}{T_{\mathrm{h}}} + C_p\ln\frac{T_2}{T_{\mathrm{c}}} = C_p\ln\frac{(T_{\mathrm{h}} + T_{\mathrm{c}})^2}{4T_{\mathrm{h}}T_{\mathrm{c}}} > 0,
$$

and by the arithmetic–geometric mean inequality $\Delta S > 0$ whenever $T_{\mathrm{h}} \ne T_{\mathrm{c}}$: heat transfer across a finite temperature difference is always irreversible.

**Example 2.3.3** The system and initial state are those of Example 2.3.2, but the partition is replaced by a heat-conducting ideal piston that can move without friction. Find $\Delta S$.

Solution: Again $Q = 0$ and $W = 0$ (taking the two gases as the system, the piston is internal) and $\Delta U = 0$; the internal energy of an ideal gas depends only on temperature, so $T_2 = 262.5\,\mathrm{K}$ as in Example 2.3.2. The difference is that in the final state the pressures on the two sides are equal. The total volume is $V = R(200 + 300)\,\mathrm{K}/p^\circ = 0.04157\,\mathrm{m^3}$ and the final pressure is $p_2 = 2RT_2/V = 105.0\,\mathrm{kPa}$. For each gas $p$, $V$ and $T$ have all changed; by the first form of Eq. (2.5),

$$
\begin{aligned}
\Delta S(\mathrm{He}) &= \tfrac{5}{2}R\ln\frac{262.5}{200} - R\ln\frac{105.0}{100} = 5.65 - 0.41 = 5.24\,\mathrm{J\,K^{-1}},\\
\Delta S(\ce{H2}) &= \tfrac{7}{2}R\ln\frac{262.5}{300} - R\ln\frac{105.0}{100} = -3.89 - 0.41 = -4.29\,\mathrm{J\,K^{-1}},
\end{aligned}
$$

and $\Delta S = 0.96\,\mathrm{J\,K^{-1}}$. The excess over Example 2.3.2 comes from the irreversible motion of the piston driven by the pressure imbalance.

### 2.3.4. Entropy of Mixing

The mixing of different gases is an irreversible process, and to calculate the entropy change a reversible path must again be designed (for example with ideal semipermeable membranes that pass only one gas, [6.3.4](/6.3.4)). In an ideal-gas mixture the molecules of the components do not affect one another: the properties of each gas are the same as if it alone occupied the whole container, and the extensive properties of the mixture ($U$, $H$, $S$, and so on, except the volume) are the sums over the components. The entropy of mixing is therefore the sum of the entropy changes of the components, each changing separately from its initial state to its state in the mixture. When mixing at constant temperature and pressure, component B goes from pressure $p$ to the partial pressure $p_{\mathrm{B}} = x_{\mathrm{B}}p$, with $\Delta S_{\mathrm{B}} = n_{\mathrm{B}}R\ln(p/p_{\mathrm{B}}) = -n_{\mathrm{B}}R\ln x_{\mathrm{B}}$.

**Definition 2.3.1 (Entropy of Mixing)** The entropy change of the system when pure substances, each at the same temperature and pressure, are mixed to form a mixture is called the **entropy of mixing**, written $\Delta_{\mathrm{mix}}S$. For ideal gases,

$$
\Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}.
\tag{2.6}
$$

Since $x_{\mathrm{B}} < 1$, $\Delta_{\mathrm{mix}}S > 0$. For equal amounts of two gases, $\Delta_{\mathrm{mix}}S_{\mathrm{m}} = R\ln 2 = 5.76\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per mole of mixture. The statistical interpretation of Eq. (2.6) is that after mixing the space available to each molecule has expanded and the number of microstates has increased ([5.2.4](/5.2.4#sec-4.8)). It depends only on composition and not on the kind of gas; but for two portions of the same gas the entropy change on "mixing" is zero, because the macroscopic state of the system is the same before and after the partition is removed (the Gibbs paradox, whose resolution lies in the indistinguishability of identical particles, see [6.3.10](/6.3.10)). The same formula applies to ideal liquid mixtures ([6.3.5](/6.3.5)).

For gases at different temperatures and pressures the calculation is again done component by component: determine the final state of each gas (temperature, its partial pressure in the mixture or the volume it occupies), compute each with Eq. (2.5) and add.

**Example 2.3.4** The system and initial state are those of Example 2.3.2, and the partition is simply removed. Find $\Delta S$.

Solution: $Q = 0$ and $W = 0$, and $T_2 = 262.5\,\mathrm{K}$ is unchanged. He expands from $V_{\mathrm{He}} = R(200\,\mathrm{K})/p^\circ = 0.01663\,\mathrm{m^3}$ to the whole container $V = 0.04157\,\mathrm{m^3}$, and $\ce{H2}$ from $0.02494\,\mathrm{m^3}$ to $V$. By the second form of Eq. (2.5),

$$
\begin{aligned}
\Delta S &= \left(\tfrac{3}{2}R\ln\frac{262.5}{200} + R\ln\frac{0.04157}{0.01663}\right) + \left(\tfrac{5}{2}R\ln\frac{262.5}{300} + R\ln\frac{0.04157}{0.02494}\right)\\
&= (3.39 + 7.62) + (-2.78 + 4.25) = 12.48\,\mathrm{J\,K^{-1}}.
\end{aligned}
$$

Of this, $0.62\,\mathrm{J\,K^{-1}}$ comes from heat transfer (as in Example 2.3.2) and $11.86\,\mathrm{J\,K^{-1}}$ from mixing.

**Example 2.3.5** At $273.15\,\mathrm{K}$, $2\,\mathrm{mol}$ of $\ce{N2}$ ($10^5\,\mathrm{Pa}$) and $1\,\mathrm{mol}$ of $\ce{O2}$ ($10^4\,\mathrm{Pa}$) are held on the two sides of a container; the partition is removed and the gases mix isothermally. Find $\Delta S$.

Solution: $V(\ce{N2}) = 2RT/10^5\,\mathrm{Pa} = 0.0454\,\mathrm{m^3}$, $V(\ce{O2}) = RT/10^4\,\mathrm{Pa} = 0.2271\,\mathrm{m^3}$, and the total volume is $0.2725\,\mathrm{m^3}$. Each gas expands isothermally to the total volume:

$$
\Delta S = 2R\ln\frac{0.2725}{0.0454} + R\ln\frac{0.2725}{0.2271} = 2R\ln 6 + R\ln 1.2 = 29.79 + 1.52 = 31.31\,\mathrm{J\,K^{-1}}.
$$

Most of the entropy change here comes from the expansion of $\ce{N2}$ and not from "mixing" itself: the two gases have different initial pressures, so Eq. (2.6) cannot be used directly.

### 2.3.5. Entropy Change of Phase Transitions

A reversible phase transition takes place at the temperature and pressure of two-phase equilibrium, generally with $W' = 0$ and $Q_{\mathrm{r}} = Q_p = \Delta_{\mathrm{trs}}H$, so

$$
\Delta_{\mathrm{trs}}S = \frac{\Delta_{\mathrm{trs}}H}{T_{\mathrm{trs}}},
$$

where $\Delta_{\mathrm{trs}}H$ is the reversible **enthalpy of transition** and $T_{\mathrm{trs}}$ the temperature of the reversible transition. Melting, vaporization and sublimation all absorb heat and increase the entropy; the molar entropy of vaporization at the normal boiling point is about $85$–$88\,\mathrm{J\,mol^{-1}\,K^{-1}}$ for many nonpolar liquids (**Trouton's rule**, [6.1.1](/6.1.1)). The entropy change of an irreversible phase transition is calculated by designing a path that contains one reversible phase transition.

**Example 2.3.6** At $273.15\,\mathrm{K}$ the molar enthalpy of fusion of ice is $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$, and between $263.15$ and $273.15\,\mathrm{K}$ the $C_{p,\mathrm{m}}$ of $\ce{H2O(l)}$ and $\ce{H2O(s)}$ are $75.3$ and $37.6\,\mathrm{J\,mol^{-1}\,K^{-1}}$ respectively. Calculate the entropy change on freezing $1\,\mathrm{mol}$ of water at $100\,\mathrm{kPa}$ (1) at $273.15\,\mathrm{K}$ and (2) at $263.15\,\mathrm{K}$, and decide whether process (2) can occur spontaneously.

Solution: (1) Reversible phase transition: $\Delta S = -\Delta_{\mathrm{fus}}H_{\mathrm{m}}/T = -6010/273.15 = -22.0\,\mathrm{J\,K^{-1}}$. A decrease of entropy does not mean that the process cannot occur: the system is not isolated and the principle of entropy increase cannot be applied to it directly; this is a reversible process, the entropy of the surroundings increases by $22.0\,\mathrm{J\,K^{-1}}$, and the total entropy change is zero.

(2) Freezing of supercooled water is an irreversible phase transition. Design a path: heat the supercooled water reversibly at constant pressure to $273.15\,\mathrm{K}$, freeze it reversibly, and cool the ice reversibly at constant pressure to $263.15\,\mathrm{K}$.

$$
\Delta S_{\text{system}} = 75.3\ln\frac{273.15}{263.15} - \frac{6010}{273.15} + 37.6\ln\frac{263.15}{273.15} = 2.81 - 22.00 - 1.40 = -20.6\,\mathrm{J\,K^{-1}}.
$$

To judge the direction the entropy change of the surroundings must be calculated. The actual process takes place at $263.15\,\mathrm{K}$ at constant pressure, and the heat released by the system is the enthalpy of freezing at $263.15\,\mathrm{K}$; by Kirchhoff's law ([6.3.1, Theorem 1.7.1](/6.3.1#thm-1.7.1)),

$$
\Delta H(263.15\,\mathrm{K}) = -6010 + (37.6 - 75.3)(263.15 - 273.15) = -5633\,\mathrm{J},
$$

and by Eq. (2.4), $\Delta S_{\text{surroundings}} = 5633/263.15 = 21.41\,\mathrm{J\,K^{-1}}$,

$$
\Delta S_{\text{isolated}} = -20.6 + 21.41 = +0.81\,\mathrm{J\,K^{-1}} > 0,
$$

so freezing of supercooled water is a spontaneous irreversible process. The entropy of the system decreases, but the heat released on freezing increases the entropy of the surroundings by more. One can also use the Clausius inequality directly: $\Delta S = -20.6\,\mathrm{J\,K^{-1}} > Q/T_{\mathrm{sur}} = -21.41\,\mathrm{J\,K^{-1}}$, so the process is irreversible.

![Freezing of 1 mol of water at 100 kPa as a function of temperature: the entropy decrease of the water and the entropy increase of the surroundings nearly cancel; their sum is positive below 273.15 K (freezing is spontaneous) and negative above it (melting is spontaneous)](./plots/supercooled-freezing.py)

The figure above extends Example 2.3.6 to other temperatures: $\Delta S_{\text{isolated}}$ vanishes only at $273.15\,\mathrm{K}$, the temperature of two-phase equilibrium, and the farther from the equilibrium temperature, the greater the driving force for freezing (or melting). Multiplying $\Delta S_{\text{isolated}}$ by $-T$ gives the $\Delta G$ of the next chapter ([6.3.3](/6.3.3)).

**Example 2.3.7** $1\,\mathrm{mol}$ of water evaporates into an evacuated container at the normal boiling point ($373.12\,\mathrm{K}$, $101.325\,\mathrm{kPa}$), the final state being water vapor at the same temperature and pressure. Find $\Delta S$ and $\Delta S_{\text{surroundings}}$, and decide whether the process can occur spontaneously. $\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$.

Solution: The initial and final states are those of the reversible phase transition, so $\Delta S = 40650/373.12 = 108.95\,\mathrm{J\,K^{-1}}$. In the actual process of evaporation into vacuum, $W = 0$ and $Q = \Delta U = \Delta H - \Delta(pV) \approx \Delta H - RT = 37.55\,\mathrm{kJ}$,

$$
\Delta S_{\text{surroundings}} = -\frac{37550}{373.12} = -100.63\,\mathrm{J\,K^{-1}}, \qquad \Delta S_{\text{isolated}} = 8.31\,\mathrm{J\,K^{-1}} > 0,
$$

and the process is spontaneous. $\Delta S_{\text{isolated}}$ is exactly $R$: compared with reversible evaporation, evaporation into vacuum does less work by $pV = RT$ and absorbs the same amount less heat.

## 2.4. The Third Law and Conventional Entropies

The entropy change of a chemical reaction, $\Delta_{\mathrm{r}}S_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}S_{\mathrm{m}}(\mathrm{B})$, requires the entropy of each substance, whereas Eq. (2.2) gives only changes of entropy. Reactants and products consist of different substances and cannot be converted into one another by $pVT$ changes, so a common zero of entropy must be chosen for all substances. This zero is given by the third law of thermodynamics.

### 2.4.1. The Nernst Heat Theorem and the Third Law

In 1902 Richards measured the electromotive forces of some galvanic-cell reactions at low temperatures and found that as the temperature falls, $\Delta G$ and $\Delta H$ of the reaction come closer and closer. From this Nernst proposed in 1906:

**Theorem 2.4.1 (Nernst Heat Theorem)** For an isothermal process in a condensed system (including chemical reactions), the entropy change tends to zero as the temperature tends to $0\,\mathrm{K}$:

$$
\lim_{T \to 0\,\mathrm{K}}(\Delta S)_T = 0.
$$

This means that at $0\,\mathrm{K}$ the entropies of all condensed substances (relative to other condensed substances made up of the same elements) are the same. Planck went further in 1911 and assumed that at $0\,\mathrm{K}$ the entropy of every pure condensed substance is zero. The assumption has counterexamples: the entropy of glassy glycerol near $0\,\mathrm{K}$ exceeds that of the crystal by about $19\,\mathrm{J\,mol^{-1}\,K^{-1}}$, so both cannot be zero. In 1920 Lewis and Gibson pointed out that Planck's assumption applies only to perfect crystals.

**Definition 2.4.1 (Perfect Crystal)** A crystal of a pure substance in which the atoms or molecules have only one ordered arrangement in the lattice is called a **perfect crystal**.

**Theorem 2.4.2 (Third Law of Thermodynamics)** At $0\,\mathrm{K}$ the entropy of a perfect crystal of any pure substance is zero: $\lim_{T \to 0\,\mathrm{K}}S(\text{perfect crystal}) = 0$.

This is the Planck–Lewis statement of the **third law of thermodynamics** ([6.1.6, Theorem 6.4.1](/6.1.6#thm-6.4.1)). From the statistical point of view, at $0\,\mathrm{K}$ all particles of a perfect crystal are in the ground state, there is only one microstate, and $S = k_{\mathrm{B}}\ln 1 = 0$. Glasses and crystals with disordered arrangements (CO, $\ce{N2O}$, ice) still have some entropy at $0\,\mathrm{K}$, called the **residual entropy** ([6.3.11](/6.3.11)). Another statement of the third law is that "it is impossible to cool a body to $0\,\mathrm{K}$ in a finite number of steps" (the unattainability of absolute zero); in thermodynamics the two statements can be derived from each other.

### 2.4.2. Conventional Entropy and Calorimetric Entropy

**Definition 2.4.2 (Conventional Entropy)** Taking the entropy of a perfect crystal at $0\,\mathrm{K}$ to be zero, the entropy of a pure substance B in the state $(T, p)$, that is, the entropy change when B goes from the perfect crystal at $0\,\mathrm{K}$ to that state, is called the **conventional entropy** (third-law entropy) of B in that state:

$$
S_{\mathrm{B}}(T, p) = \Delta S_{\mathrm{B}}(0\,\mathrm{K},\ \text{perfect crystal} \to T, p).
$$
The conventional entropy calculated along this path from measurements of low-temperature heat capacities and enthalpies of transition is called the **calorimetric entropy**. The conventional entropy of $1\,\mathrm{mol}$ of substance in its standard state is the **standard molar entropy** $S^\circ_{\mathrm{m}}(T)$ ([6.1.6, Definition 6.4.2](/6.1.6#def-6.4.2)); the values at $298.15\,\mathrm{K}$ can be looked up in tables.

For example, the conventional entropy of $\ce{H2O(g)}$ at $423\,\mathrm{K}$ is the sum of the entropy changes of the following series of steps: heating ice from $0\,\mathrm{K}$ to $273.15\,\mathrm{K}$, melting, heating the liquid water to the normal boiling point, vaporization, and heating the vapor to $423\,\mathrm{K}$:

$$
S_{\mathrm{m}}(T) = \int_0^{T_{\mathrm{fus}}}\frac{C_{p,\mathrm{m}}(\mathrm{s})}{T}\,\mathrm{d}T + \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m}}}{T_{\mathrm{fus}}} + \int_{T_{\mathrm{fus}}}^{T_{\mathrm{b}}}\frac{C_{p,\mathrm{m}}(\mathrm{l})}{T}\,\mathrm{d}T + \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{T_{\mathrm{b}}} + \int_{T_{\mathrm{b}}}^{T}\frac{C_{p,\mathrm{m}}(\mathrm{g})}{T}\,\mathrm{d}T.
\tag{2.7}
$$

If the solid has a crystal-form transition, the corresponding entropy of transition must be added. The integrals in Eq. (2.7) must be evaluated numerically from measured heat-capacity data: formerly by finding areas on a $C_{p,\mathrm{m}}/T$–$T$ plot (graphical integration), now by interpolating the data and applying the trapezoidal or Simpson rule (`scipy.integrate`, [4.4.4](/4.4.4)).

Below $20\,\mathrm{K}$ the heat capacity of a crystal is hard to measure accurately and must be extrapolated. At low temperatures the heat capacity of nonmetallic crystals obeys the *Debye T³ law*:

$$
C_{V,\mathrm{m}} = \frac{12\pi^4}{5}R\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3 = aT^3 \qquad (T \ll \Theta_{\mathrm{D}}),
$$

where $\Theta_{\mathrm{D}}$ is the Debye temperature of the crystal and $a$ a parameter characteristic of the crystal (for metals the electronic contribution $\gamma_{\mathrm{e}}T$ must be added). At low temperatures $C_p \approx C_V$ for solids. If the lowest temperature of measurement is $T^*$, the entropy of the segment from $0$ to $T^*$ is

$$
S_{\mathrm{m}}(T^*) = \int_0^{T^*}\frac{aT^3}{T}\,\mathrm{d}T = \frac{aT^{*3}}{3} = \frac{C_{p,\mathrm{m}}(T^*)}{3},
$$

so only the heat capacity at $T^*$ need be measured, without knowing $\Theta_{\mathrm{D}}$.

**Example 2.4.1** Estimate the calorimetric entropy of water vapor at $423.15\,\mathrm{K}$ and $101.325\,\mathrm{kPa}$.

Solution: Integration of the low-temperature heat capacity of ice (numerical, with $T^3$ extrapolation below $10\,\mathrm{K}$) gives $S_{\mathrm{m}}(\text{ice}, 273.15\,\mathrm{K}) = 38.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$; melting adds $6010/273.15 = 22.0$; liquid water from $273.15$ to $373.12\,\mathrm{K}$ ($C_{p,\mathrm{m}} = 75.3$) adds $23.5$; vaporization adds $40650/373.12 = 108.9$; water vapor from $373.12$ to $423.15\,\mathrm{K}$ ($C_{p,\mathrm{m}} \approx 33.8$) adds $4.3$. The total is $S_{\mathrm{m}} \approx 196.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$; converting to the standard pressure adds $R\ln(101.325/100) = 0.11$. Vaporization accounts for more than half of the total entropy: the entropy of a gas is far greater than that of a condensed phase.

![Calorimetric entropy of water from 0 K to 423 K (approximate heat capacities). Upper panel: Cp,m/T, whose area gives the heating contributions; lower panel: Sm(T), with jumps of ΔfusH/Tfus at the melting point and ΔvapH/Tb at the boiling point](./plots/water-entropy.py)

The entropy of $\ce{H2O(g)}$ calculated from spectroscopic data and statistical thermodynamics (about $200.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$ at $423\,\mathrm{K}$) is $3$–$4\,\mathrm{J\,mol^{-1}\,K^{-1}}$ larger than the calorimetric entropy above. The difference comes mainly from the disorder in the positions of the hydrogen atoms in ice: ice is not a perfect crystal and has at $0\,\mathrm{K}$ a residual entropy of about $R\ln\frac{3}{2} = 3.4\,\mathrm{J\,mol^{-1}\,K^{-1}}$ (Pauling, 1935), which calorimetry cannot detect. The $S^\circ_{\mathrm{m}}$ in thermodynamic data tables already includes it ([6.3.11](/6.3.11)).

### 2.4.3. Entropy Changes of Chemical Reactions

At $298.15\,\mathrm{K}$, with all substances in their standard states, the entropy change is calculated directly from standard molar entropies ([6.1.6](/6.1.6#sec-6.4.5)):

$$
\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) = \sum_{\mathrm{B}}\nu_{\mathrm{B}}S^\circ_{\mathrm{m}}(\mathrm{B}, 298.15\,\mathrm{K}).
$$

As for the reaction enthalpy, the reaction model "the reaction goes to completion, and reactants and products do not mix" is used. For the entropy change of a reaction at another temperature, a path is designed as for Kirchhoff's law: the reactants go from $T$ to $298.15\,\mathrm{K}$, react, and the products return to $T$. If no substance undergoes a phase transition between $298.15\,\mathrm{K}$ and $T$,

$$
\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}\,\mathrm{d}T,
\qquad
\left(\frac{\partial\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}}{\partial T}\right)_p = \frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}.
\tag{2.8}
$$

If there are phase transitions, integrate piecewise and add the entropies of transition; at nonstandard pressures, the effect of pressure on entropy is included in addition ($-R\ln(p/p^\circ)$ for an ideal gas). From Kirchhoff's law and Eq. (2.8), if $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = 0$ over a temperature range, both $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ are independent of temperature, and $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ is a linear function of temperature.

**Example 2.4.2** For ammonia synthesis $\ce{N2(g) + 3H2(g) -> 2NH3(g)}$, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) = 2(192.8) - 191.6 - 3(130.7) = -198.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$. Using the heat-capacity parameters in the table of [6.3.1](/6.3.1#sec-1.3.2), find the value at $723\,\mathrm{K}$.

Solution: $\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}} = \Delta a + \Delta b\,T + \Delta c'/T^2$ with $\Delta a = -50.92$, $\Delta b = 36.65 \times 10^{-3}$, $\Delta c' = -4.10 \times 10^5$ ([6.3.1, Example 1.7.1](/6.3.1#sec-1.7.3)).

$$
\int_{298.15}^{723}\frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}\,\mathrm{d}T = \Delta a\ln\frac{723}{298.15} + \Delta b(723 - 298.15) - \frac{\Delta c'}{2}\left(\frac{1}{723^2} - \frac{1}{298.15^2}\right) = -31.4\,\mathrm{J\,mol^{-1}\,K^{-1}},
$$

and $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -229.5\,\mathrm{J\,mol^{-1}\,K^{-1}}$. The entropy decreases, so high temperature is unfavorable for ammonia synthesis; together with $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(723\,\mathrm{K})$ of Example 1.7.1, it allows the equilibrium constant at this temperature to be computed ([6.3.7](/6.3.7)).

## 2.5. Entropy and the Degradation of Energy

The first law says that after a real process the total amount of energy is unchanged; the second law says that after an irreversible process the total entropy has increased. The total amount of energy has not changed, but the increase of entropy makes part of the energy lose its capacity to do work; this is called **energy degradation** ([5.2.4](/5.2.4#sec-4.10)).

Consider three reservoirs with $T_{\mathrm{A}} > T_{\mathrm{B}} > T_{\mathrm{C}}$, where $T_{\mathrm{C}}$ is the lowest available temperature (the environment). When the heat $Q$ is in the reservoir at $T_{\mathrm{A}}$, a reversible engine working between $T_{\mathrm{A}}$ and $T_{\mathrm{C}}$ can deliver at most the work $W_1 = Q(1 - T_{\mathrm{C}}/T_{\mathrm{A}})$. If $Q$ is first transferred irreversibly from $T_{\mathrm{A}}$ to $T_{\mathrm{B}}$ and then used between $T_{\mathrm{B}}$ and $T_{\mathrm{C}}$, at most $W_2 = Q(1 - T_{\mathrm{C}}/T_{\mathrm{B}})$ can be obtained. The difference is

$$
W_1 - W_2 = T_{\mathrm{C}}\left(\frac{Q}{T_{\mathrm{B}}} - \frac{Q}{T_{\mathrm{A}}}\right) = T_{\mathrm{C}}\,\Delta S_{\text{isolated}} > 0,
$$

where $Q/T_{\mathrm{B}} - Q/T_{\mathrm{A}}$ is precisely the total entropy change caused by this irreversible heat transfer. The result is general: when an irreversible process increases the entropy of an isolated system by $\Delta S_{\text{isolated}}$, an amount of energy $T_0\Delta S_{\text{isolated}}$ passes from a form that can do work to a form that cannot ($T_0$ is the environmental temperature, [5.2.4, Eq. 4.10.1](/5.2.4#sec-4.10)). It can therefore be said that the entropy change of an isolated system measures the extent to which its energy has become unavailable.

Energy thus differs in "quality": work is the highest-quality energy and can be converted entirely into heat unconditionally; the quality of heat falls as temperature falls, and for the same quantity of heat, the higher the temperature, the greater the part that can be converted into work. Real processes in nature always proceed in the direction of decreasing quality of energy, and the "energy crisis" refers to the decrease of available energy and not of the total amount of energy.

In principle the entropy criterion settles the question of the direction of processes, but it is inconvenient to use for three reasons: using the Clausius inequality requires computing both $\Delta S$ and the heat–temperature quotient; the principle of entropy increase applies only to adiabatic or isolated systems; and combining system and surroundings into a large isolated system sometimes answers a different question. In the electrolysis of water, for example, including the power source in the large isolated system leads to the conclusion that "the whole process is spontaneous", which does not directly answer the question whether water can decompose by itself. Most processes in chemistry take place at constant temperature and volume or at constant temperature and pressure, and the next chapter ([6.3.3](/6.3.3)) derives from the Clausius inequality the Helmholtz energy and Gibbs energy criteria, which are expressed through properties of the system alone.

Finally, the principle of entropy increase holds only for isolated systems. For a general system the change of entropy can be divided into two parts: the entropy flux associated with the exchange of energy and matter with the surroundings, and the entropy produced by irreversible processes inside the system; the former can be positive or negative, and the latter is never negative. If enough "negative entropy" flows in from the surroundings, the entropy of an open system can decrease, and the system can spontaneously go from disorder to order. Living organisms are exactly such open systems: they take in food of low entropy (or absorb sunlight) and discharge waste and heat of high entropy, maintaining and developing highly ordered structures, which is what Schrödinger meant by "life feeds on negative entropy". Ordered structures far from equilibrium such as chemical oscillations and Turing patterns also belong to this class. These topics make up non-equilibrium thermodynamics and are discussed systematically in [6.3.18](/6.3.18), after chemical kinetics has been studied.

## Summary

| Process | Entropy change | Conditions |
|---|---|---|
| Ideal gas, isothermal | $nR\ln(V_2/V_1) = nR\ln(p_1/p_2)$ | Reversible or not |
| Temperature change at constant volume or pressure | $\int C_V\,\mathrm{d}T/T$, $\int C_p\,\mathrm{d}T/T$ | No phase transition or reaction |
| Ideal gas $pVT$ change | Eq. (2.5) | Constant $C_{V,\mathrm{m}}$ |
| Ideal gases mixing at constant $T$ and $p$ | $-R\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$ | Different gases |
| Reversible phase transition | $\Delta_{\mathrm{trs}}H/T_{\mathrm{trs}}$ | $T$, $p$ of two-phase equilibrium |
| Surroundings | $-Q_{\text{system}}/T_{\mathrm{sur}}$ | Surroundings a large reservoir, $Q$ the actual heat |
| Reaction | $\sum\nu_{\mathrm{B}}S^\circ_{\mathrm{m}}(\mathrm{B})$, temperature correction by Eq. (2.8) | Reaction model, no phase transition |

## Questions

1. True or false: (A) all spontaneous processes are irreversible; (B) all irreversible processes are spontaneous; (C) work can be converted entirely into heat, but heat cannot be converted entirely into work; (D) the entropy change of a system in a spontaneous process is always greater than zero; (E) a reversible adiabatic process is an isentropic process.
   Answer: A and E are true. B is false: an irreversible compression driven by work from the surroundings is not spontaneous. C is false: heat can be converted entirely into work, but necessarily with other changes (as in isothermal expansion of an ideal gas). D is false: only the entropy of an isolated system must increase in a spontaneous process; in Example 2.3.6 the freezing of supercooled water is spontaneous, yet the entropy of the system decreases.
2. Someone says: "The combination of hydrogen and oxygen into water at room temperature is spontaneous, so $\Delta S > Q/T$; then the electrolysis of water at room temperature has $\Delta S < Q/T$." Is this correct?
   Answer: No. The Clausius inequality gives $\Delta S > Q/T_{\mathrm{sur}}$ for every real (irreversible) process; although electrolysis of water needs electrical work from the surroundings to proceed, it is still an irreversible process and $\Delta S > Q/T_{\mathrm{sur}}$. A process with $\Delta S < Q/T_{\mathrm{sur}}$ cannot occur.
3. True or false: (A) if the $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ of a reaction is independent of temperature over a temperature range, then $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ is also independent of temperature; (B) a system has an entropy change between initial and final states only if it passes through a reversible process; (C) the third law says that the entropy of any crystal at $0\,\mathrm{K}$ is zero.
   Answer: A is true (both are guaranteed by $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = 0$). B is false: entropy is a state function, every process has an entropy change, which must however be computed along a reversible path. C is false: it applies only to perfect crystals.
4. In an adiabatic container, $1\,\mathrm{mol}$ of He ($400\,\mathrm{K}$, $5p^\circ$) and $1\,\mathrm{mol}$ of $\ce{H2}$ ($200\,\mathrm{K}$, $10p^\circ$) are separated by a fixed adiabatic partition. After the partition is removed, find the final temperature, $\Delta S$ and $\Delta H$.
   Answer: $\Delta U = 0$ gives $T = 275\,\mathrm{K}$. The ratio of initial volumes is $V_{\mathrm{He}} : V_{\ce{H2}} = 4 : 1$, and each gas expands to the total volume: $\Delta S(\mathrm{He}) = \frac{3}{2}R\ln\frac{275}{400} + R\ln\frac{1}{0.8} = -2.82\,\mathrm{J\,K^{-1}}$, $\Delta S(\ce{H2}) = \frac{5}{2}R\ln\frac{275}{200} + R\ln\frac{1}{0.2} = 20.00\,\mathrm{J\,K^{-1}}$, $\Delta S = 17.18\,\mathrm{J\,K^{-1}}$; $\Delta H = \frac{5}{2}R(275 - 400) + \frac{7}{2}R(275 - 200) = -415.7\,\mathrm{J}$.
