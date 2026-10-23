---
title: The First Law of Thermodynamics
source_hash: 663b6e0dea92
---

The previous two chapters used a molecular model to study the properties of **equilibrium states**; from this chapter on we turn to the methods of thermodynamics, which study the changes of the state of a system starting only from macroscopic experimental laws, without relying on any microscopic model. The core of this chapter is the first law of thermodynamics, the **law of conservation of energy** extended to include thermal phenomena. It generalizes **work** in mechanics ([5.1.4](/5.1.4)) to **thermodynamic systems**, defines **internal energy** through adiabatic work, and then defines heat in terms of internal energy and work. With this law we can compute the work, heat and change of internal energy of an **ideal gas** in various processes, and it leads to the concepts of heat capacity, enthalpy and cycle efficiency; the upper bound on the efficiency of the Carnot cycle prepares the way for the second law of thermodynamics in the next chapter ([5.2.4](/5.2.4)). The concepts of this chapter (internal energy, heat, enthalpy, heat capacity) and its sign conventions are shared with physical chemistry.

## 3.1. Quasi-Static Processes

A change of a system from one equilibrium state to another is called a thermodynamic process, or simply a process. Once a process begins, the original equilibrium is broken; strictly speaking, none of the intermediate states is an equilibrium state, and none can be described by a set of **state variables**. To make use of the properties of equilibrium states, thermodynamics introduces an idealized kind of process.

**Definition 3.1.1 (Quasi-Static Process)** A process in which every state the system passes through is infinitesimally close to an equilibrium state is called a **quasi-static process**; otherwise it is called a non-quasi-static process.

Only an infinitely slow process is strictly quasi-static. "Slow" is relative, and the standard of comparison is the *relaxation time* $\tau$, the time a system needs to return to equilibrium after its equilibrium has been disturbed. If the time $\Delta t$ over which the state variables change appreciably in the process satisfies $\Delta t \gg \tau$, the process can be regarded as quasi-static.

**Example 3.1.1** The relaxation time of the pressure in the cylinder of an internal combustion engine can be estimated by the time a pressure disturbance takes to cross the cylinder: the linear size of the cylinder is $L \sim 10^{-1}\,\mathrm{m}$ and the **mean speed** of the molecules is $\bar v \sim 10^2\,\mathrm{m\,s^{-1}}$, so $\tau_p \sim L/\bar v \sim 10^{-3}\,\mathrm{s}$. One stroke cycle of the piston takes about $10^{-2}\,\mathrm{s}$, an order of magnitude longer than $\tau_p$, so the compression and expansion in the cylinder can be treated approximately as quasi-static processes.

A quasi-static process can be described in a diagram of state variables: a point in the $p$–$V$ diagram represents an equilibrium state, and a curve represents a quasi-static process; the intermediate states of a non-quasi-static process cannot be shown in the diagram.

There are two ways to change the state of a system: doing work and transferring heat.

## 3.2. Work

Let a gas be enclosed in a cylinder with a piston of area $S$. In a quasi-static process the pressure $p$ of the gas is uniform throughout, and when the piston moves by $\mathrm{d}l$ the work done on the gas by the surroundings is $-pS\,\mathrm{d}l = -p\,\mathrm{d}V$.

**Definition 3.2.1 (Pressure–Volume Work)** In a quasi-static process, the infinitesimal work and the work done on the system by the surroundings are
$$
\delta W = -p\,\mathrm{d}V, \qquad W = -\int_{V_1}^{V_2} p\,\mathrm{d}V,
\tag{3.1}
$$
called **pressure–volume work**.

This wiki uses the IUPAC and ISO 80000-5 sign convention uniformly for thermal physics and physical chemistry: both the work $W$ and the heat $Q$ are positive when received by the system, so $W$ is the work done on the system. When the gas expands ($\mathrm{d}V > 0$), $W < 0$ and the work done by the system on the surroundings is $-W > 0$; when the gas is compressed, $W > 0$. In the $p$–$V$ diagram, $-W$ equals the area under the process curve (positive for expansion).

Work is a process quantity: if the initial and final states are the same but the paths differ, the areas under the curves differ, and so does the work. Therefore $\delta W$ is not the **total differential** of any state function, which the notation $\delta$ is meant to remind us; there is no such thing as "the amount of work contained in a system". Besides pressure–volume work, there are also stirring work (shaft work), work done by electric currents, work done by electromagnetic fields and so on, all of which can change the state of a system. Microscopically, doing work converts the energy of the ordered motion of molecules in the surroundings, through collisions, into the energy of the random motion of the molecules of the system.

## 3.3. Internal Energy, Heat and the First Law of Thermodynamics

Thermodynamics is a theory independent of statistical physics. The basic concepts of internal energy and heat were already given microscopically in [5.2.1](/5.2.1); here we redefine them using only macroscopic experiments, without a molecular model, and give ways to measure them.

### 3.3.1. Internal Energy

Separate the system from its surroundings by an adiabatic wall; the state of the system can still be changed by doing work. In the 1840s Joule performed a series of experiments in which a falling weight drove a paddle wheel stirring the water in an adiabatic container, or an electric current passed through a resistor immersed in the water, bringing the water from the same initial state to the same final state. The experiments show that

**Property 3.3.1** When a system goes from the same initial state to the same final state by any adiabatic process, the work $W_{\mathrm{ad}}$ done on the system by the surroundings is the same, independent of the manner of doing work and of the intermediate process.

The adiabatic work therefore depends only on the initial and final states, and can be used to define a state function.

**Definition 3.3.1** There exists a function $U$ depending only on the state of the system such that, when the system goes from state 1 to state 2 by an adiabatic process,
$$
U_2 - U_1 = W_{\mathrm{ad}},
$$
and $U$ is called the **internal energy** of the system.

This definition also gives a way of measuring the internal energy (measuring the adiabatic work), which determines it only up to an additive constant. It is consistent with the microscopic definition in [5.2.1](/5.2.1) (the sum of the energy of molecular **thermal motion** and the interaction **potential energy**).

### 3.3.2. Heat

The state of a system can also be changed without doing work, simply by a **temperature** difference with the surroundings, for example by putting a cup of cold water on a hot stove.

**Definition 3.3.2 (Heat)** The energy transferred between a system and its surroundings because of a temperature difference is called **heat**, denoted $Q$. When a system changes from state 1 to state 2 while the surroundings do work $W$ on it, the heat absorbed by the system is defined as
$$
Q = (U_2 - U_1) - W.
$$
$Q > 0$ means that the system absorbs heat and $Q < 0$ means that it releases heat.

In a process with heat transfer but no work, $Q = U_2 - U_1$. Microscopically, heat transfer is the passage of the energy of random molecular motion from a hotter body to a colder one through collisions. Like work, heat is a process quantity, and to say "how much heat a body contains" is wrong. Historically heat was measured in calories, $1\,\mathrm{cal} = 4.184\,\mathrm{J}$ (thermochemical calorie); Joule's experiments established the equivalence of heat and work, and now heat and work are both measured in joules ($\mathrm{J}$).

### 3.3.3. The First Law of Thermodynamics

**Theorem 3.3.1 (First Law of Thermodynamics)** When a system changes from one equilibrium state to another, the increase in its internal energy equals the sum of the work done on the system by the surroundings and the heat absorbed by the system from the surroundings:
$$
\Delta U = Q + W.
\tag{3.2}
$$
For an infinitesimal process, $\mathrm{d}U = \delta Q + \delta W$; for a quasi-static process with only pressure–volume work, $\mathrm{d}U = \delta Q - p\,\mathrm{d}V$.

The first law of thermodynamics is the law of conservation and transformation of energy including thermal phenomena, and applies to any process of any system, including non-quasi-static processes (in a non-quasi-static process $W$ cannot be computed as $-\int p\,\mathrm{d}V$, but it can still be computed from the work actually done by the surroundings). The internal energy $U$ is a state function and $W$ is a process quantity, so $Q = \Delta U - W$ is also a process quantity; neither $\delta Q$ nor $\delta W$ is a total differential, but their sum $\mathrm{d}U$ is.

**Remark 3.3.1 (The Convention in Physics Textbooks)** Many physics textbooks (including the textbook of this course) use the work done by the system on the surroundings, $W' = -W$, and write the first law as $Q = \Delta U + W'$, read as "the heat absorbed by the system equals the increase in internal energy plus the work done by the system on the surroundings", with pressure–volume work $W' = \int p\,\mathrm{d}V$. The physical content of the two forms is identical; this wiki uses Eq. (3.2) throughout, in agreement with chemistry and the ISO standards.

In the past, people tried to build machines that keep doing work on the surroundings without consuming energy, that is, a *perpetual motion machine of the first kind*. The first law of thermodynamics shows that for a machine operating in cycles, $\Delta U = 0$ when it returns to its initial state, and the work done on the surroundings is $-W = Q$: no work can be done without absorbing heat, so a perpetual motion machine of the first kind cannot be built.

### 3.3.4. Joule's Free Expansion Experiment

In 1845 Joule performed a free expansion experiment on a gas: two containers connected by a tube with a valve, one holding compressed air and the other evacuated, were immersed in water. When the valve was opened, the air rushed into the evacuated container; after equilibrium was reached, the water temperature was measured and found to be unchanged.

Analysis: the gas expands into a vacuum, so the surroundings do no work on the gas, $W = 0$; the water temperature is unchanged, so there is no net heat exchange between gas and water, $Q = 0$. By the first law, $\Delta U = 0$. The volume of the gas changed, its temperature did not, and its internal energy did not, which shows that

**Property 3.3.2** The internal energy of an ideal gas is a function of temperature only: $U = U(T)$, independent of volume (Joule's law).

Joule's experiment was not very accurate (the heat capacity of the water is much larger than that of the gas). More accurate experiments show that the temperature of a real gas changes slightly after free expansion, so its internal energy depends on volume (§3.5.4); Joule's law holds strictly only in the limit of vanishing pressure, that is, for an ideal gas. This agrees with the conclusion of the kinetic theory ([5.2.1](/5.2.1), Formula 1.4.1).

## 3.4. Heat Capacity

### 3.4.1. Heat Capacity and Molar Heat Capacity

**Definition 3.4.1 (Heat Capacity)** If a system absorbs heat $\delta Q$ when its temperature rises by $\mathrm{d}T$ in a given process, then
$$
C = \frac{\delta Q}{\mathrm{d}T}
$$
is called the **heat capacity** of the system in that process, with unit $\mathrm{J\,K^{-1}}$. The heat capacities at constant volume and at constant pressure are called the heat capacity at constant volume $C_V$ and the heat capacity at constant pressure $C_p$, respectively. The heat capacity of $1\,\mathrm{mol}$ of a substance is called the **molar heat capacity**, $C_{\mathrm{m}} = C/n$, with the corresponding $C_{V,\mathrm{m}}$ and $C_{p,\mathrm{m}}$; the heat capacity per unit mass of a substance is called the specific heat capacity $c$.

Heat is a process quantity, so the heat capacity depends on the process; it generally varies with temperature and is determined by experiment. If the temperature change is small, it can be treated as a constant.

### 3.4.2. Internal Energy of an Ideal Gas

In an isochoric process $\delta W = 0$, so by the first law $\mathrm{d}U = \delta Q_V = nC_{V,\mathrm{m}}\,\mathrm{d}T$. For any process, the change of internal energy depends only on the initial and final states, so we may choose a convenient path: from $(T, V)$ first heat at constant volume to $(T + \mathrm{d}T, V)$, then change isothermally to the final state. The internal energy of an ideal gas is independent of volume, so $\mathrm{d}U = 0$ on the isothermal segment, and therefore

**Formula 3.4.1** For an ideal gas in any process,
$$
\mathrm{d}U = nC_{V,\mathrm{m}}\,\mathrm{d}T, \qquad \Delta U = nC_{V,\mathrm{m}}\Delta T\quad(C_{V,\mathrm{m}}\ \text{const}).
$$

Here $C_{V,\mathrm{m}}$ is merely a coefficient: the equation above holds for any process, isobaric, adiabatic or otherwise, and should not be read as "the change of internal energy in an isochoric process".

### 3.4.3. Mayer's Relation

For a quasi-static isobaric process of an ideal gas, $\delta Q_p = nC_{p,\mathrm{m}}\,\mathrm{d}T$, $\mathrm{d}U = nC_{V,\mathrm{m}}\,\mathrm{d}T$ and $\delta W = -p\,\mathrm{d}V = -\mathrm{d}(pV) = -nR\,\mathrm{d}T$. By the first law, $\delta Q_p = \mathrm{d}U - \delta W$:

**Formula 3.4.2 (Mayer's Relation)**
$$
C_{p,\mathrm{m}} - C_{V,\mathrm{m}} = R.
$$

When the gas is heated at constant pressure, the heat it absorbs goes not only into raising the internal energy but also into the work $nR\,\mathrm{d}T$ done on the surroundings, so $C_{p,\mathrm{m}} > C_{V,\mathrm{m}}$. We define the *heat capacity ratio*
$$
\gamma = \frac{C_p}{C_V} = \frac{C_{p,\mathrm{m}}}{C_{V,\mathrm{m}}} > 1.
$$

### 3.4.4. Classical Theory and Quantization of Heat Capacity

By the **equipartition theorem**, an ideal gas of rigid molecules has $U = \frac{i}{2}nRT$ ([5.2.1](/5.2.1), Formula 1.4.1), so
$$
C_{V,\mathrm{m}} = \frac{i}{2}R, \qquad C_{p,\mathrm{m}} = \frac{i + 2}{2}R, \qquad \gamma = \frac{i + 2}{i}.
$$

| Gas | $i$ | $C_{V,\mathrm{m}}$ | $C_{p,\mathrm{m}}$ | $\gamma$ (theory) | $\gamma$ (experiment at room temperature, approx.) |
|---|---|---|---|---|---|
| Monatomic ($\ce{He}$, $\ce{Ar}$) | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ | $1.67$ | $1.67$ |
| Diatomic ($\ce{N2}$, $\ce{O2}$) | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ | $1.40$ | $1.40$ |
| Nonlinear polyatomic ($\ce{H2O}$ vapor, $\ce{CH4}$) | 6 | $3R$ | $4R$ | $1.33$ | $1.31$–$1.33$ |

At room temperature, monatomic gases agree very well with the theory, and diatomic and polyatomic gases somewhat less well. Over a wide temperature range, $C_{V,\mathrm{m}}$, $C_{p,\mathrm{m}}$ and $\gamma$ all vary with temperature, which classical theory cannot explain. In quantum mechanics the rotational and vibrational energies are discrete, and the corresponding **degrees of freedom** are excited only when $k_{\mathrm{B}}T$ is comparable to the level spacing. Take $\ce{H2}$ as an example: the characteristic temperature of rotation is about $85\,\mathrm{K}$ and that of vibration about $6300\,\mathrm{K}$, so $C_{V,\mathrm{m}}/R$ is $\frac{3}{2}$ at low temperature and $\frac{5}{2}$ at room temperature, and approaches $\frac{7}{2}$ only above several thousand kelvins (in fact $\ce{H2}$ begins to dissociate before that).

![Molar heat capacity of an H2-like diatomic gas: rigid-rotor and harmonic-oscillator model](./plots/h2-heat-capacity.py)

The model in the figure treats the molecule as a rigid rotor plus a harmonic oscillator, and uses the **Boltzmann distribution** ([5.2.1](/5.2.1), Theorem 1.7.1) to compute the mean energy of each level. Real $\ce{H2}$ also has the difference between ortho- and parahydrogen at low temperatures (a statistical effect of nuclear spin), so the details differ slightly from the figure. The steps in the heat capacity are among the earliest evidence for the quantization of energy ([5.5](/5.5)).

**Example 3.4.1** A container with rigid adiabatic walls is divided into two parts by a fixed stop and a heat-conducting, gas-tight, frictionless piston; the parts contain $\ce{He}$ with amount of substance $n_1$ at temperature $T_1$ and $\ce{O2}$ with $n_2$ at temperature $T_2$, respectively. The stop is removed, and the piston can move and conduct heat. Find the temperature after equilibrium is reached.

Solution: In the process, $\ce{He}$ and $\ce{O2}$ exchange both heat and work, but the whole formed by the two parts exchanges neither heat nor work with the surroundings (the walls are rigid and adiabatic), so the internal energy of the whole is unchanged:
$$
n_1C_{V,\mathrm{m}}^{\ce{He}}(T - T_1) + n_2C_{V,\mathrm{m}}^{\ce{O2}}(T - T_2) = 0, \qquad C_{V,\mathrm{m}}^{\ce{He}} = \tfrac{3}{2}R,\ C_{V,\mathrm{m}}^{\ce{O2}} = \tfrac{5}{2}R,
$$
$$
T = \frac{3n_1T_1 + 5n_2T_2}{3n_1 + 5n_2}.
$$
We need not know how the piston moves or how much heat and work are exchanged between the two parts: with a suitable choice of system, the first law can often bypass the details of the process.

## 3.5. Adiabatic Processes

**Definition 3.5.1** A process in which a system exchanges no heat with its surroundings is called an **adiabatic process**.

Processes in a system surrounded by good thermal insulation, and processes that occur so quickly that there is no time to exchange heat with the surroundings (such as the compression and expansion of the gas in a sound wave, or the expansion of the burning gas in an internal combustion engine), can be regarded approximately as adiabatic processes. In an adiabatic process $\delta Q = 0$ and $\mathrm{d}U = \delta W$: all the work done by the surroundings is converted into internal energy.

### 3.5.1. Quasi-Static Adiabatic Processes of an Ideal Gas

From the first law and the **equation of state**,
$$
nC_{V,\mathrm{m}}\,\mathrm{d}T = -p\,\mathrm{d}V, \qquad p\,\mathrm{d}V + V\,\mathrm{d}p = nR\,\mathrm{d}T = n(C_{p,\mathrm{m}} - C_{V,\mathrm{m}})\,\mathrm{d}T.
$$
Eliminating $\mathrm{d}T$ gives $C_{V,\mathrm{m}}V\,\mathrm{d}p = -C_{p,\mathrm{m}}p\,\mathrm{d}V$, that is, $\frac{\mathrm{d}p}{p} = -\gamma\frac{\mathrm{d}V}{V}$. Integrating with $\gamma$ treated as a constant:

**Formula 3.5.1 (Adiabatic Process Equations)** A quasi-static adiabatic process of an ideal gas satisfies
$$
pV^\gamma = \text{const}, \qquad TV^{\gamma - 1} = \text{const}, \qquad p^{\gamma - 1}T^{-\gamma} = \text{const}.
\tag{3.3}
$$

The first equation is also called Poisson's equation, and the last two follow from the first and the equation of state. The work done by the surroundings in an adiabatic process can be computed in two ways: by direct integration,
$$
W = -\int_{V_1}^{V_2}\frac{p_1V_1^\gamma}{V^\gamma}\,\mathrm{d}V = \frac{p_2V_2 - p_1V_1}{\gamma - 1};
$$
or from the first law, $W = \Delta U = nC_{V,\mathrm{m}}(T_2 - T_1)$. Using $pV = nRT$ and $C_{V,\mathrm{m}} = R/(\gamma - 1)$ one can verify that the two agree. In adiabatic expansion $W < 0$: the gas does work at the expense of its internal energy, and its temperature falls; in adiabatic compression the temperature rises (a diesel engine ignites by compression, with a compression ratio of about $15$–$20$).

In the $p$–$V$ diagram, at a given point the slope of the adiabat, $-\gamma p/V$, is $\gamma$ times the slope of the isotherm, $-p/V$, so the adiabat is steeper than the isotherm. In the molecular picture: in isothermal expansion only the decrease of the number density $n_V$ lowers the pressure; in adiabatic expansion $n_V$ decreases and, in addition, the loss of internal energy lowers the temperature, so both factors lower the pressure ($p = n_Vk_{\mathrm{B}}T$).

![Isotherm and adiabat through the same state (left) and the Carnot cycle of a monatomic ideal gas (right)](./plots/carnot-cycle-pv.py)

### 3.5.2. Polytropic Processes

**Definition 3.5.2** A quasi-static process in which the heat capacity remains constant is called a **polytropic process**.

For an ideal gas, let the molar heat capacity $C_{\mathrm{m}}$ be constant. Repeating the derivation of §3.5.1 (replacing $\delta Q = 0$ by $\delta Q = nC_{\mathrm{m}}\,\mathrm{d}T$) gives the equation of the polytropic process
$$
pV^k = \text{const}, \qquad k = \frac{C_{\mathrm{m}} - C_{p,\mathrm{m}}}{C_{\mathrm{m}} - C_{V,\mathrm{m}}},
$$
where $k$ is called the polytropic index; conversely $C_{\mathrm{m}} = C_{V,\mathrm{m}}\frac{k - \gamma}{k - 1}$. Common processes are all special cases of polytropic processes: $k = 0$ is the isobaric process ($C_{\mathrm{m}} = C_{p,\mathrm{m}}$), $k = 1$ the isothermal process ($C_{\mathrm{m}} = \infty$), $k = \gamma$ the adiabatic process ($C_{\mathrm{m}} = 0$), and $k \to \infty$ the isochoric process ($C_{\mathrm{m}} = C_{V,\mathrm{m}}$). For $1 < k < \gamma$, $C_{\mathrm{m}} < 0$: the gas does more work in expansion than the heat it absorbs, so it absorbs heat while its temperature falls. The compression of a real gas in a compressor lies between isothermal and adiabatic, and is often described by a polytropic process with $1 < k < \gamma$.

### 3.5.3. Comparison of the Processes of an Ideal Gas

For an ideal gas of amount of substance $n$ in a quasi-static process ($W$ is the work done on the gas by the surroundings and $Q$ is the heat absorbed by the gas):

| Process | Process equation | $\Delta U$ | $W$ | $Q$ | Molar heat capacity |
|---|---|---|---|---|---|
| Isochoric | $V = \text{const}$ | $nC_{V,\mathrm{m}}\Delta T$ | $0$ | $nC_{V,\mathrm{m}}\Delta T$ | $C_{V,\mathrm{m}}$ |
| Isobaric | $p = \text{const}$ | $nC_{V,\mathrm{m}}\Delta T$ | $-p\Delta V = -nR\Delta T$ | $nC_{p,\mathrm{m}}\Delta T$ | $C_{p,\mathrm{m}}$ |
| Isothermal | $pV = \text{const}$ | $0$ | $-nRT\ln\frac{V_2}{V_1} = -nRT\ln\frac{p_1}{p_2}$ | $nRT\ln\frac{V_2}{V_1}$ | $\infty$ |
| Adiabatic | $pV^\gamma = \text{const}$ | $nC_{V,\mathrm{m}}\Delta T$ | $\frac{p_2V_2 - p_1V_1}{\gamma - 1} = nC_{V,\mathrm{m}}\Delta T$ | $0$ | $0$ |
| Polytropic | $pV^k = \text{const}$ | $nC_{V,\mathrm{m}}\Delta T$ | $\frac{p_2V_2 - p_1V_1}{k - 1} = \frac{nR\Delta T}{k - 1}$ | $nC_{\mathrm{m}}\Delta T$ | $C_{V,\mathrm{m}}\frac{k - \gamma}{k - 1}$ |

Every row satisfies $\Delta U = Q + W$, which can be used as a mutual check.

### 3.5.4. Adiabatic Free Expansion

A rigid adiabatic container is divided into two halves by a partition; one half holds gas and the other is a vacuum. When the partition is removed, the gas quickly fills the whole container. In the process $Q = 0$ (adiabatic walls) and $W = 0$ (expansion into a vacuum, with no work done by the surroundings), so by the first law $U_1 = U_2$.

- Ideal gas: the internal energy depends only on temperature, so $T_2 = T_1$. But this is not an isothermal process: the intermediate states are not equilibrium states and have no definite temperature at all.
- Real gas: when the intermolecular force is mainly attractive, expansion increases the intermolecular potential energy and decreases the **kinetic energy**, so $T_2 < T_1$; when it is mainly repulsive, $T_2 > T_1$. For a van der Waals gas, the invariance of $U = nC_{V,\mathrm{m}}T - \frac{n^2a}{V}$ ([5.2.2](/5.2.2)) gives $T_2 - T_1 = -\frac{na}{C_{V,\mathrm{m}}}\left(\frac{1}{V_1} - \frac{1}{V_2}\right) < 0$.

**Example 3.5.1** An ideal gas undergoes adiabatic free expansion from $V_1$ to $V_2 = 2V_1$. Find the final pressure.

Solution: Using the adiabatic process equation to get $p_2 = p_1(V_1/V_2)^\gamma = p_1/2^\gamma$ is wrong: free expansion is not a quasi-static process, and Eq. (3.3) does not apply. The correct way is to use the equation of state: $T_2 = T_1$, so $p_2 = p_1V_1/V_2 = p_1/2$.

A quasi-static isothermal expansion from $V_1$ to $2V_1$ with the same initial and final temperatures (the partition moving slowly to the right) is different: $\Delta U = 0$, $W = -nRT\ln 2 < 0$ and $Q = nRT\ln 2 > 0$; the gas absorbs heat and does work on the surroundings. Thus adiabatic free expansion, quasi-static isothermal expansion and quasi-static adiabatic expansion are three different processes: the first two have the same initial and final states but different $Q$ and $W$, and the last two have different final states.

### 3.5.5. The Throttling Process and Enthalpy

**Definition 3.5.3** The process in which a gas flows continuously under adiabatic conditions from the high-pressure side through a porous plug (or a small hole, or a valve) to the low-pressure side is called a **throttling process**; the pressures $p_1 > p_2$ on the two sides are kept constant.

Consider a fixed amount of gas whose internal energy and volume on the high-pressure side before throttling are $U_1$ and $V_1$, and $U_2$ and $V_2$ on the low-pressure side after throttling. The gas on the left pushes it through the porous plug, doing work $p_1V_1$ on it; it pushes away the gas in front of it on the right, so the work done on it by the surroundings is $-p_2V_2$. The process is adiabatic, $Q = 0$, so by the first law
$$
U_2 - U_1 = p_1V_1 - p_2V_2, \qquad \text{i.e.}\qquad U_1 + p_1V_1 = U_2 + p_2V_2.
$$

**Definition 3.5.4 (Enthalpy)** The state function
$$
H = U + pV
$$
is called the **enthalpy** of the system.

Adiabatic throttling is therefore an isenthalpic process: $H_1 = H_2$. The enthalpy of an ideal gas, $H = U(T) + nRT$, depends only on temperature, so the temperature does not change in throttling; the temperature of a real gas generally changes after throttling, which is called the *Joule–Thomson effect*, discovered by Joule and Thomson (Kelvin) in 1852. A drop in temperature is called the positive effect and can be used for refrigeration and the liquefaction of gases (Linde's method of liquefying air); a rise in temperature is called the negative effect. A given gas shows the positive effect only below its inversion temperature: the inversion temperatures of $\ce{N2}$ and $\ce{O2}$ are far above room temperature, so they can be cooled directly by throttling, whereas $\ce{H2}$ (about $200\,\mathrm{K}$) and $\ce{He}$ (about $40\,\mathrm{K}$) must be precooled first. The Joule–Thomson effect is much more sensitive than free expansion, and its existence shows that the enthalpy (internal energy) of a real gas depends on pressure (volume), that is, that there are interactions between molecules.

The importance of enthalpy lies in isobaric processes. In a quasi-static isobaric process with only pressure–volume work,
$$
\delta Q_p = \mathrm{d}U + p\,\mathrm{d}V = \mathrm{d}(U + pV) = \mathrm{d}H,
$$
that is, the heat absorbed in an isobaric process equals the increase of enthalpy; correspondingly, the heat absorbed in an isochoric process equals the increase of internal energy, $\delta Q_V = \mathrm{d}U$. Therefore

**Formula 3.5.2**
$$
C_V = \left(\frac{\partial U}{\partial T}\right)_V, \qquad C_p = \left(\frac{\partial H}{\partial T}\right)_p.
$$

Most chemical reactions take place in open vessels, that is, at constant pressure, so the heat of reaction is expressed by the enthalpy change $\Delta_{\mathrm{r}}H$; this is the main use of enthalpy in physical chemistry.

## 3.6. Cyclic Processes

**Definition 3.6.1 (Thermodynamic Cycle)** The whole process in which a system (such as the working substance of a heat engine) returns to its initial state after a series of changes is called a **thermodynamic cycle**.

After one cycle the internal energy of the system is unchanged: $\Delta U = 0$. If all stages are quasi-static, the cycle can be represented by a closed curve in the $p$–$V$ diagram, and the absolute value of the net work $W$ done on the system by the surroundings equals the area enclosed by the curve. The thermodynamic cycle of a thermal power plant is an example: water absorbs heat in the boiler and becomes high-temperature, high-pressure steam, which drives the turbine to do work, releases heat in the condenser and condenses into water, and is pumped back to the boiler.

In a cycle, the system exchanges heat with a series of heat reservoirs. Let the total heat absorbed by the system from the high-temperature reservoirs be $Q_1$ and that from the low-temperature reservoirs be $Q_2$ (both counted with sign, so that released heat is negative). Then $\Delta U = Q_1 + Q_2 + W = 0$, and the net work done by the system on the surroundings is $-W = Q_1 + Q_2$.

**Definition 3.6.2** A cycle traversed clockwise in the $p$–$V$ diagram is called a forward cycle (heat engine cycle): $Q_1 > 0$, $Q_2 < 0$, $-W > 0$. The **thermal efficiency** of a heat engine is
$$
\eta = \frac{-W}{Q_1} = \frac{Q_1 + Q_2}{Q_1} = 1 - \frac{\lvert Q_2\rvert}{Q_1}.
$$
A cycle traversed counterclockwise is called a reverse cycle (refrigeration cycle): the surroundings do work $W > 0$, the system absorbs heat $Q_2 > 0$ from the low-temperature reservoir and releases heat $\lvert Q_1\rvert = Q_2 + W$ to the high-temperature reservoir. The **coefficient of performance** of a refrigerator is
$$
\varepsilon = \frac{Q_2}{W} = \frac{Q_2}{\lvert Q_1\rvert - Q_2}.
$$

The efficiency of a heat engine is always less than 1, while the coefficient of performance of a refrigerator can exceed 1. Efficiencies of actual heat engines: early steam engines about ten-odd percent, gasoline engines about $25\%$–$35\%$, large diesel engines more than $45\%$, and combined-cycle gas–steam power plants about $60\%$.

**Example 3.6.1 (Heat Capacity Can Be Negative)** In the $p$–$V$ diagram, state 1 lies on the isotherm at temperature $T_1$; the adiabat through 1 meets the isotherm at a lower temperature $T_2$ at state 4; on the isotherm at $T_2$, state 2 lies to the left of 4 (smaller volume) and state 3 lies to the right of 4 (larger volume). Consider the three straight-line processes of an ideal gas from 2, 4 and 3, respectively, to 1, and determine the sign of their heat capacities.

Solution: In all three processes the temperature rises from $T_2$ to $T_1$, so $\mathrm{d}T > 0$; $\Delta U$ is the same and positive, and the sign of the heat capacity is the same as that of $Q$.

- $4 \to 1$ is adiabatic, $Q_{41} = 0$, so $C = 0$.
- $2 \to 1$: the area under the straight line $2 \to 1$ is smaller than that under the adiabat $4 \to 1$, so the work done by the surroundings satisfies $W_{21} < W_{41}$, hence $Q_{21} = \Delta U - W_{21} > \Delta U - W_{41} = 0$; the gas absorbs heat and $C > 0$.
- $3 \to 1$: the work done by the surroundings satisfies $W_{31} > W_{41}$, so $Q_{31} < 0$: the temperature rises, yet heat is released, and $C < 0$.

The result can also be judged with cycles: $1 \to 4 \to 3 \to 1$ is traversed counterclockwise in the $p$–$V$ diagram, so it is a reverse cycle with negative net heat absorbed; $1 \to 4$ is adiabatic and $4 \to 3$ is an isothermal expansion that absorbs heat, so $3 \to 1$ must release heat. Similarly, $1 \to 4 \to 2 \to 1$ is a forward cycle with positive net heat absorbed, and $4 \to 2$ is an isothermal compression that releases heat, so $2 \to 1$ must absorb heat.

## 3.7. The Carnot Cycle

**Definition 3.7.1 (Carnot Cycle)** A quasi-static cycle in which the working substance exchanges heat only with two constant-temperature reservoirs and there is no dissipation such as friction is called a **Carnot cycle**; it consists of two isotherms and two adiabats. A heat engine operating on a Carnot cycle is called a Carnot engine.

Take an ideal gas as the working substance, let the temperature of the high-temperature reservoir be $T_1$ and that of the low-temperature reservoir $T_2$, and let the cycle be $1 \to 2$ (isothermal expansion at $T_1$) $\to 3$ (adiabatic expansion) $\to 4$ (isothermal compression at $T_2$) $\to 1$ (adiabatic compression), as in the right panel of the figure above. The heats absorbed by the working substance in the two isothermal processes are
$$
Q_1 = nRT_1\ln\frac{V_2}{V_1} > 0, \qquad Q_2 = nRT_2\ln\frac{V_4}{V_3} < 0.
$$
The two adiabatic processes satisfy $T_1V_2^{\gamma - 1} = T_2V_3^{\gamma - 1}$ and $T_1V_1^{\gamma - 1} = T_2V_4^{\gamma - 1}$; dividing the two gives the closure condition $\frac{V_2}{V_1} = \frac{V_3}{V_4}$. Hence

**Formula 3.7.1 (Efficiency of the Carnot Engine)**
$$
\frac{Q_1}{T_1} + \frac{Q_2}{T_2} = 0, \qquad \eta_{\mathrm{C}} = 1 - \frac{\lvert Q_2\rvert}{Q_1} = 1 - \frac{T_2}{T_1}.
$$

Discussion:

1. The efficiency of a Carnot engine is determined only by the temperatures of the two reservoirs, independent of the kind of working substance and of the volumes of expansion (here it is proved only for an ideal gas; for the general proof see Carnot's theorem in [5.2.4](/5.2.4)).
2. It points out the direction for improving the efficiency of heat engines: raise the temperature $T_1$ of the high-temperature reservoir and lower the temperature $T_2$ of the low-temperature reservoir. The low-temperature reservoir is usually the environment (the atmosphere or river water), so in practice only $T_1$ can be raised, which is why modern power plants pursue high-temperature, high-pressure steam.
3. The temperature of the low-temperature reservoir cannot be $0\,\mathrm{K}$, so $\eta_{\mathrm{C}} < 1$: a heat engine cannot avoid releasing heat to a low-temperature reservoir, so at least two reservoirs are needed.
4. From the standpoint of energy conservation, $\eta = 1$ (turning all the absorbed heat into work) would not violate the first law, yet it cannot be achieved in practice. This shows that there is another law independent of the first law, namely the second law of thermodynamics ([5.2.4](/5.2.4)).

The relation $\frac{Q_1}{T_1} + \frac{Q_2}{T_2} = 0$ seems to be merely a by-product of the calculation; in the next chapter we will see that it generalizes to the Clausius equality, from which entropy is defined.

## 3.8. Refrigeration Cycles

Running a Carnot cycle in reverse gives a Carnot refrigerator: the surroundings do work $W$, and the working substance absorbs heat $Q_2$ from the low-temperature reservoir at $T_2$ and releases heat $\lvert Q_1\rvert$ to the high-temperature reservoir at $T_1$. By Formula 3.7.1, $\lvert Q_1\rvert/Q_2 = T_1/T_2$, so

**Formula 3.8.1 (Coefficient of Performance of a Carnot Refrigerator)**
$$
\varepsilon_{\mathrm{C}} = \frac{Q_2}{\lvert Q_1\rvert - Q_2} = \frac{T_2}{T_1 - T_2}.
$$

The coefficient of performance need not be less than 1. Taking room temperature $T_1 = 293\,\mathrm{K}$:

| $T_2/\mathrm{K}$ | 273 | 223 | 100 | 5 | 1 |
|---|---|---|---|---|---|
| $\varepsilon_{\mathrm{C}}$ | 13.6 | 3.2 | 0.52 | 0.017 | 0.0034 |

The lower the temperature of the low-temperature reservoir, the smaller the coefficient of performance and the harder the refrigeration: to extract $1\,\mathrm{J}$ of heat from a body at $1\,\mathrm{K}$, at least about $300\,\mathrm{J}$ of work must be done. The coefficient of performance of an ordinary household refrigerator is about 2–7. The same machine used to heat a room is a heat pump, whose heating coefficient $\lvert Q_1\rvert/W = T_1/(T_1 - T_2)$ is always greater than 1: a heat pump delivers more heat into the room than the electrical energy it consumes. This does not violate energy conservation, since the surplus is carried from the low-temperature reservoir outdoors.

## Summary

- A quasi-static process (Definition 3.1.1) can be drawn as a curve on a state diagram; the pressure–volume work is $W = -\int p\,\mathrm{d}V$ (Eq. (3.1)). Work and heat are process quantities, while the internal energy $U$ is a state function defined through adiabatic work (Definition 3.3.1).
- First law of thermodynamics (Theorem 3.3.1): $\Delta U = Q + W$, with both $Q$ and $W$ counted positive when received by the system (Eq. (3.2); for the convention of physics textbooks see Remark 3.3.1).
- The internal energy of an ideal gas depends only on temperature (Property 3.3.2), and $\mathrm{d}U = nC_{V,\mathrm{m}}\,\mathrm{d}T$ in any process (Formula 3.4.1); Mayer's relation $C_{p,\mathrm{m}} - C_{V,\mathrm{m}} = R$ (Formula 3.4.2), $\gamma = C_p/C_V$.
- Quasi-static adiabatic process: $pV^\gamma = \text{const}$ (Eq. (3.3)); the polytropic process $pV^k = \text{const}$ unifies the isobaric ($k = 0$), isothermal ($k = 1$), adiabatic ($k = \gamma$) and isochoric ($k \to \infty$) processes; $\Delta U$, $W$ and $Q$ for each are listed in the table of §3.5.3.
- Adiabatic free expansion is not quasi-static, and the temperature of an ideal gas does not change; throttling is isenthalpic, $H = U + pV$ (Definition 3.5.4), and real gases show the Joule–Thomson effect. $C_V = (\partial U/\partial T)_V$, $C_p = (\partial H/\partial T)_p$ (Formula 3.5.2).
- Cycles: engine efficiency $\eta = -W/Q_1 = 1 - \lvert Q_2\rvert/Q_1$, coefficient of performance $\varepsilon = Q_2/W$ (Definition 3.6.2). The Carnot cycle (Definition 3.7.1) has $\eta_{\mathrm{C}} = 1 - T_2/T_1$ (Formula 3.7.1) and $\varepsilon_{\mathrm{C}} = T_2/(T_1 - T_2)$ (Formula 3.8.1); the relation $Q_1/T_1 + Q_2/T_2 = 0$ is the starting point for entropy in the next chapter.

## Questions

1. Why is $C_{p,\mathrm{m}} > C_{V,\mathrm{m}}$? Why is the difference very small for solids and liquids?

   **Answer** in isobaric heating, work $p\,\mathrm{d}V$ must be done on the surroundings; the thermal expansion of solids and liquids is very small, so this work can be neglected.

2. In a closed, adiabatic room, the refrigerator door is opened and the refrigerator is left running. How does the temperature of the room change?

   **Answer** take the room as the system; the power supply does work $W > 0$ on it, $Q = 0$, so $\Delta U = W > 0$ and the temperature rises.
