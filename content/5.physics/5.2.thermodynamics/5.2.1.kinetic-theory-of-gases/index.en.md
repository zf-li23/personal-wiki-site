---
title: Temperature and the Kinetic Theory of Gases
source_hash: 8a93015ba924
---

Thermal physics studies phenomena related to temperature. Macroscopically, these appear as changes in the temperature, pressure, volume and phase of a body; microscopically, they arise from the perpetual random motion of a very large number of molecules. There are two complementary ways to study them. Thermodynamics starts from a few macroscopic experimental laws and derives general, reliable conclusions by logical reasoning, without any reference to the microscopic structure of matter ([5.2.3](/5.2.3), [5.2.4](/5.2.4)). Statistical mechanics starts from a microscopic model of the molecules and computes macroscopic quantities by statistical methods; it reveals the nature of thermal phenomena, but its conclusions are limited by the model. This chapter is an introduction to the statistical method. We first set up the concepts specific to thermal physics, such as temperature and equilibrium, and then use Newtonian mechanics ([5.1](/5.1)) and probability theory ([3.1](/3.1)) to derive the pressure of an ideal gas, the microscopic meaning of temperature, the equipartition theorem, the Maxwell speed distribution and the Boltzmann distribution. The next chapter, [5.2.2](/5.2.2), treats real gases, which deviate from the ideal gas, and nonequilibrium transport processes. The Boltzmann distribution obtained here will reappear repeatedly in blackbody radiation, lasers and physical chemistry.

## 1.1. Thermodynamic Systems, Equilibrium and Temperature

### 1.1.1. Thermodynamic Systems

**Definition 1.1.1 (Thermodynamic System)** A macroscopic body of finite volume consisting of a very large number of microscopic particles (molecules, atoms, etc.) is called a **thermodynamic system**, or simply a system; the part outside the system that interacts with it is called the **surroundings** (or environment). According to the way a system interacts with its surroundings, systems are classified as follows:

- **Isolated system**: exchanges neither energy nor matter with the surroundings;
- **Closed system**: exchanges energy but not matter with the surroundings;
- **Adiabatic system**: exchanges energy with the surroundings only in the form of **work**, with no heat exchange;
- **Open system**: exchanges both energy and matter with the surroundings.

A system of infinite extent such as the universe, or a system containing only a few particles, is not a thermodynamic system: the former has no definite boundary or surroundings, and the latter has no statistical laws to speak of. The classification above agrees with the usage in physical chemistry (IUPAC).

### 1.1.2. Equilibrium States

**Definition 1.1.2 (Equilibrium State)** If, under fixed external conditions, there are no macroscopic flows of particles or energy inside a system and its macroscopic properties do not change with time, the system is said to be in an **equilibrium state**.

A system that interacts with its surroundings can remain in equilibrium only if the corresponding equilibrium conditions hold:

| Equilibrium condition | Applies when | Requirement at equilibrium |
|---|---|---|
| Mechanical equilibrium | The system interacts mechanically with the surroundings (e.g., a piston) | Internal and external pressures are equal |
| Thermal equilibrium | The system can exchange heat with the surroundings (diathermic wall) | Internal and external temperatures are equal |
| Phase equilibrium | Different phases coexist in the system | In addition to mechanical and thermal equilibrium, there is no net transfer of matter between phases |
| Chemical equilibrium | Chemical reactions or mixing of different components occur in the system | There is no net reaction, and the spatial distribution of each component no longer changes |

An equilibrium state must be distinguished from a *steady state*. Connect the two ends of a metal rod to heat reservoirs at temperatures $T_1$ and $T_2$ ($T_1 \neq T_2$). After a sufficiently long time the temperature at each point of the rod no longer changes, but heat keeps flowing through the rod; this is a steady state, not an equilibrium state. The rod is in equilibrium only if $T_1 = T_2$. Equilibrium is a dynamic balance: macroscopically the system is at rest, while microscopically the molecules continue to move violently, and macroscopic quantities fluctuate only slightly about their mean values.

### 1.1.3. Macroscopic Quantities, Microscopic Quantities and the Equation of State

**Definition 1.1.3** Directly measurable physical quantities that characterize the system as a whole are called **macroscopic quantities**, such as the pressure $p$, volume $V$, temperature $T$, mass and internal energy. Macroscopic quantities are of two kinds: **extensive quantities** are proportional to the size of the system and add up when the system is divided into parts ($V$, mass, internal energy); **intensive quantities** are independent of the size of the system and do not add up ($p$, $T$, density). Physical quantities that describe the motion of a single microscopic particle (the mass $m$ of a molecule, its **velocity** $\boldsymbol{v}$, its diameter $d$) are called **microscopic quantities**; they can generally be measured only indirectly.

The task of statistical mechanics is to express macroscopic quantities as statistical averages of microscopic quantities.

**Definition 1.1.4 (State Variables)** A set of mutually independent macroscopic quantities that describe an equilibrium state of a system is called its **state variables**; a functional relation $f(p, V, T) = 0$ among them is called the **equation of state** of the system.

For a fixed amount of gas, a pair of state variables (say $p, V$) determines an equilibrium state uniquely, and the equation of state then gives the third quantity $T$.

### 1.1.4. The Zeroth Law of Thermodynamics and Temperature

The common equilibrium state reached by two systems after a long contact through a diathermic wall is called thermal equilibrium. Temperature is a physical quantity specific to thermal physics, and its definition rests on the following experimental law.

**Theorem 1.1.1 (Zeroth Law of Thermodynamics)** If systems $A$ and $C$ are in thermal equilibrium, and $B$ and $C$ are in thermal equilibrium, then $A$ and $B$ are also in thermal equilibrium (even if $A$ and $B$ are not in contact).

The zeroth law says that "being in thermal equilibrium" is an equivalence relation (reflexivity and symmetry are obvious from the definition, and the zeroth law provides transitivity). Hence all systems fall into equivalence classes under thermal equilibrium, and each class can be labeled by a number.

**Definition 1.1.5 (Temperature)** The macroscopic property shared by all systems in the same thermal equilibrium state is called the **temperature**: two systems are in thermal equilibrium if and only if their temperatures are equal.

The zeroth law is also the principle of the thermometer: if a thermometer $C$ comes to thermal equilibrium with $A$ and then with $B$ and gives the same reading, then $A$ and $B$ have the same temperature. In the next section we will see that, microscopically, temperature measures how vigorous the thermal motion of the molecules is.

### 1.1.5. Temperature Scales

A way of assigning numerical values to temperature is called a temperature scale.

1. Ideal gas scale: for a fixed amount of gas, $pV$ depends only on temperature in the limit of vanishing pressure. We define $T \propto \lim_{p\to0} pV$ and assign the triple point of water the value $273.16\,\mathrm{K}$, which gives
   $$
   T = 273.16\,\mathrm{K} \times \lim_{p \to 0}\frac{pV}{(pV)_3},
   $$
   where $(pV)_3$ is the value for the same sample of gas at the triple point. With low-pressure $^3\mathrm{He}$ gas, this scale can be used down to about $0.5\,\mathrm{K}$.
2. *Thermodynamic temperature scale*: a scale independent of any thermometric substance and its thermometric property, defined through Carnot's theorem ([5.2.4](/5.2.4)); it coincides with the ideal gas scale wherever the latter applies. The unit of thermodynamic temperature $T$ is the kelvin ($\mathrm{K}$), one of the SI base units.
3. Celsius scale: $t/{}^\circ\mathrm{C} = T/\mathrm{K} - 273.15$. The triple point of water is about $0.01\,{}^\circ\mathrm{C}$, and the boiling point of water at one standard atmosphere is about $100\,{}^\circ\mathrm{C}$.
4. Fahrenheit scale (in everyday use only in the United States and a few other places): $t_{\mathrm{F}}/{}^\circ\mathrm{F} = \frac{9}{5}\,t/{}^\circ\mathrm{C} + 32$; for example, $100\,{}^\circ\mathrm{F} \approx 37.8\,{}^\circ\mathrm{C}$.

**Remark 1.1.1 (The 2019 SI)** Before 2019, the kelvin was defined as $1/273.16$ of the thermodynamic temperature of the triple point of water, which was exactly $273.16\,\mathrm{K}$. Since May 2019 the kelvin has been defined by fixing the numerical value of the Boltzmann constant:
$$
k_{\mathrm{B}} = 1.380\,649 \times 10^{-23}\,\mathrm{J\,K^{-1}}\quad(\text{exact}),
$$
that is, $1\,\mathrm{K}$ is the change in temperature that changes the thermal energy $k_{\mathrm{B}}T$ by $1.380\,649 \times 10^{-23}\,\mathrm{J}$. The triple point of water has since become a measured value, still about $273.16\,\mathrm{K}$ (with an uncertainty of about $0.1\,\mathrm{mK}$). The Avogadro constant $N_{\mathrm{A}} = 6.022\,140\,76 \times 10^{23}\,\mathrm{mol^{-1}}$ was fixed at the same time, so the molar gas constant $R = N_{\mathrm{A}}k_{\mathrm{B}} = 8.314\,462\,618\ldots\,\mathrm{J\,mol^{-1}\,K^{-1}}$ is also exact.

### 1.1.6. The Ideal Gas Equation of State

**Definition 1.1.6 (Ideal Gas)** A gas that satisfies the equation of state
$$
pV = nRT
$$
strictly in all states is called an **ideal gas**, where $n$ is the amount of substance.

All real gases approach the ideal gas as the pressure tends to zero. In terms of the number of molecules $N = nN_{\mathrm{A}}$ and the number density $n_V = N/V$, the equation of state can also be written as
$$
pV = Nk_{\mathrm{B}}T, \qquad p = n_Vk_{\mathrm{B}}T.
\tag{1.1}
$$
Here the *Boltzmann constant* $k_{\mathrm{B}} = R/N_{\mathrm{A}}$ is the "gas constant per molecule"; it converts temperature into an energy scale for a single molecule: at room temperature $T = 300\,\mathrm{K}$, $k_{\mathrm{B}}T \approx 4.14 \times 10^{-21}\,\mathrm{J} \approx 0.0259\,\mathrm{eV} \approx \frac{1}{40}\,\mathrm{eV}$. If the mass of the gas is $m_{\mathrm{gas}}$ and its molar mass is $M$, then $n = m_{\mathrm{gas}}/M$. At standard conditions ($273.15\,\mathrm{K}$, $101.325\,\mathrm{kPa}$), $n_V \approx 2.69 \times 10^{25}\,\mathrm{m^{-3}}$ (the Loschmidt constant).

## 1.2. Pressure of an Ideal Gas

### 1.2.1. Basic Postulates of the Kinetic Theory of Gases

The kinetic theory of gases starts from three basic postulates: a macroscopic body consists of a very large number of molecules or atoms, with gaps between them; the molecules are in perpetual random motion, called *thermal motion*; and there are interaction forces between molecules.

### 1.2.2. The Microscopic Model of an Ideal Gas

Mechanical assumptions (the laws obeyed by each molecule):

1. The size of a molecule is much smaller than the mean distance between molecules, so a molecule can be treated as a **particle**;
2. Except at the instant of a collision, there is no interaction between molecules or between a molecule and the wall (gravity is neglected);
3. Collisions are perfectly elastic;
4. The motion of the molecules obeys Newtonian mechanics.

Statistical assumptions (for a large number of molecules in equilibrium):

1. In the absence of external fields, a molecule is equally likely to be found anywhere in the container, and the number density is the same everywhere: $n_V = \frac{\mathrm{d}N}{\mathrm{d}V} = \frac{N}{V}$;
2. The direction of a molecular velocity is equally likely to be any direction (isotropy), so
   $$
   \overline{v_x} = \overline{v_y} = \overline{v_z} = 0, \qquad \overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \frac{1}{3}\overline{v^2}.
   $$

Statistical laws have two characteristics. One is stability: the average result of a large number of events is definite. The other is *fluctuation*: individual observations vary about the mean, and the more objects are involved, the smaller the relative fluctuation (of order $1/\sqrt{N}$). The **Galton board** is a vivid demonstration: which slot a single ball falls into is random, yet the distribution of a large number of balls always approaches the same bell-shaped curve; this is the **central limit theorem** at work, as the **binomial distribution** tends to the **normal distribution**.

### 1.2.3. The Pressure Formula

Suppose the container holds a single kind of molecule, each of mass $m$, with total number $N$ and volume $V$. Group the molecules by velocity: let $N_i$ molecules have velocity $\boldsymbol{v}_i$, with number density $n_i = N_i/V$, so that $\sum_i n_i = n_V$. On the wall take an area element $\mathrm{d}A$ perpendicular to the $x$ axis (much larger than a molecular cross section).

1. A molecule with velocity $\boldsymbol{v}_i$ ($v_{ix} > 0$) makes one **elastic collision** with $\mathrm{d}A$; the $x$ component of its **momentum** changes by $-2mv_{ix}$, so by the **impulse–momentum theorem** the **impulse** it delivers to the wall is $2mv_{ix}$.
2. The molecules of this group that can hit $\mathrm{d}A$ within $\mathrm{d}t$ lie in a slanted cylinder with base $\mathrm{d}A$, axis along $\boldsymbol{v}_i$ and height $v_{ix}\,\mathrm{d}t$ perpendicular to the base; there are $n_iv_{ix}\,\mathrm{d}t\,\mathrm{d}A$ of them, and the impulse they deliver to the wall is $\mathrm{d}I_i = 2n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A$.
3. Sum over the groups with $v_{ix} > 0$. By isotropy, half of the molecules have $v_{ix} > 0$ and half have $v_{ix} < 0$, so
   $$
   \mathrm{d}I = \sum_{v_{ix}>0} 2n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A = \sum_i n_imv_{ix}^2\,\mathrm{d}t\,\mathrm{d}A.
   $$
4. Pressure is the average force per unit area:
   $$
   p = \frac{\mathrm{d}I}{\mathrm{d}t\,\mathrm{d}A} = m\sum_i n_iv_{ix}^2 = n_Vm\overline{v_x^2} = \frac{1}{3}n_Vm\overline{v^2}.
   $$

**Formula 1.2.1 (Pressure of an Ideal Gas)** Let $\bar\varepsilon_{\mathrm{t}} = \frac{1}{2}m\overline{v^2}$ denote the mean translational **kinetic energy** of a molecule. Then
$$
p = \frac{1}{3}n_Vm\overline{v^2} = \frac{2}{3}n_V\bar\varepsilon_{\mathrm{t}}.
\tag{1.2}
$$

Pressure is the average effect of a large number of molecules striking the wall; it makes no sense to speak of the "pressure" of a single molecule. Collisions between molecules do not appear in the derivation: in equilibrium they do not change the velocity distribution, but only keep it isotropic.

## 1.3. The Statistical Meaning of Temperature

Comparing the pressure formula (1.2) with the equation of state (1.1), we obtain

**Formula 1.3.1** The mean translational kinetic energy of the molecules of an ideal gas depends only on temperature:
$$
\bar\varepsilon_{\mathrm{t}} = \frac{1}{2}m\overline{v^2} = \frac{3}{2}k_{\mathrm{B}}T.
\tag{1.3}
$$

This is the statistical meaning of temperature: the thermodynamic temperature is a measure of the mean translational kinetic energy of the thermal motion of a large number of molecules. Like pressure, temperature is a statistical concept and is meaningful only for a large number of molecules. From Eq. (1.3), the *root-mean-square speed* of the molecules is
$$
v_{\mathrm{rms}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} = \sqrt{\frac{3RT}{M}} \propto \sqrt{T}.
$$

**Example 1.3.1 (Orders of Magnitude)** At $T = 273\,\mathrm{K}$, $\bar\varepsilon_{\mathrm{t}} = \frac{3}{2}k_{\mathrm{B}}T \approx 5.65 \times 10^{-21}\,\mathrm{J} \approx 3.53 \times 10^{-2}\,\mathrm{eV}$, independent of the kind of molecule; $v_{\mathrm{rms}} \approx 1.84 \times 10^3\,\mathrm{m\,s^{-1}}$ for $\ce{H2}$ and $v_{\mathrm{rms}} \approx 461\,\mathrm{m\,s^{-1}}$ for $\ce{O2}$, of the same order of magnitude as the speed of sound. Chemical bond energies are a few $\mathrm{eV}$, far greater than $k_{\mathrm{B}}T$ at room temperature, so molecular collisions at ordinary temperatures cannot break chemical bonds.

## 1.4. The Equipartition Theorem

### 1.4.1. Degrees of Freedom of a Molecule

A molecule cannot always be treated as a point particle: a diatomic molecule can also rotate and vibrate. The number of independent coordinates needed to specify the configuration of a molecule in space is its number of **degrees of freedom**, denoted $i = t + r + s$, where $t$, $r$, $s$ are the numbers of translational, rotational and vibrational degrees of freedom, respectively.

| Molecule | Examples | $t$ | $r$ | $s$ | $i$ |
|---|---|---|---|---|---|
| Monatomic | $\ce{He}$, $\ce{Ne}$, $\ce{Ar}$ | 3 | 0 | 0 | 3 |
| Diatomic | $\ce{H2}$, $\ce{O2}$, $\ce{CO}$ | 3 | 2 | 1 | 6 |
| Linear polyatomic ($N$ atoms) | $\ce{CO2}$ | 3 | 2 | $3N-5$ | $3N$ |
| Nonlinear polyatomic ($N$ atoms) | $\ce{H2O}$, $\ce{NH3}$ | 3 | 3 | $3N-6$ | $3N$ |

For a diatomic molecule, the coordinates $(x, y, z)$ of the center of mass give 3 translational degrees of freedom, the orientation $(\theta, \phi)$ of the axis gives 2 rotational degrees of freedom (rotation about the axis itself is not counted, since the atoms can be treated as point particles), and the change of the interatomic distance $l$ gives 1 vibrational degree of freedom. A set of $N$ atoms has $3N$ coordinates in all; for a nonlinear molecule, the **rotation about a fixed point** of a **rigid body** requires 3 **Euler angles**, and the remaining $3N - 6$ are vibrations; a linear molecule has only 2 rotational degrees of freedom, and its number of vibrational degrees of freedom is $3N - 5$.

### 1.4.2. The Equipartition Theorem

From Eq. (1.3) and isotropy, $\frac{1}{2}m\overline{v_x^2} = \frac{1}{2}m\overline{v_y^2} = \frac{1}{2}m\overline{v_z^2} = \frac{1}{2}k_{\mathrm{B}}T$: each translational degree of freedom receives on average a kinetic energy $\frac{1}{2}k_{\mathrm{B}}T$. Frequent collisions between molecules constantly exchange energy among translation, rotation and vibration, and at equilibrium no degree of freedom is favored. Hence we have

**Theorem 1.4.1 (Equipartition Theorem)** In an equilibrium state at temperature $T$, according to classical statistics, the average value of each independent quadratic term in the energy of a molecule (the kinetic energy $\frac{1}{2}mv_x^2$ or $\frac{1}{2}J\omega^2$, or the harmonic **potential energy** $\frac{1}{2}kx^2$) is equal to $\frac{1}{2}k_{\mathrm{B}}T$.

A vibrational degree of freedom has both vibrational kinetic energy and vibrational potential energy, and the two quadratic terms together contribute $k_{\mathrm{B}}T$. The mean energy of a molecule is therefore
$$
\bar\varepsilon = \bar\varepsilon_{\mathrm{t}} + \bar\varepsilon_{\mathrm{r}} + \bar\varepsilon_{\mathrm{v}} = \frac{1}{2}(t + r + 2s)\,k_{\mathrm{B}}T.
$$
The proof of the theorem uses the Boltzmann distribution; see Remark 1.7.1. It applies to classical degrees of freedom in gases, liquids and solids. For example, each atom in a solid has 3 vibrational degrees of freedom and a mean energy of $3k_{\mathrm{B}}T$, which gives a molar heat capacity of $3R$ (the Dulong–Petit law).

Equipartition is a result of classical theory. In quantum mechanics, rotational and vibrational energies are discrete: when $k_{\mathrm{B}}T$ is much smaller than the spacing between adjacent levels, that degree of freedom can hardly be excited, and it is said to be "frozen out". Vibrational level spacings typically correspond to temperatures of order $10^3\,\mathrm{K}$ (about $6000\,\mathrm{K}$ for $\ce{H2}$ and about $800\,\mathrm{K}$ for $\ce{Cl2}$), so at ordinary temperatures the vibrations of most molecules are frozen out and the molecules can be treated as rigid ($s = 0$), with mean energy $\bar\varepsilon = \frac{t + r}{2}k_{\mathrm{B}}T$: $\frac{3}{2}k_{\mathrm{B}}T$ for monatomic molecules, $\frac{5}{2}k_{\mathrm{B}}T$ for diatomic and linear molecules, and $3k_{\mathrm{B}}T$ for nonlinear polyatomic molecules.
At still lower temperatures the rotations freeze out as well ($\ce{H2}$ below a few tens of kelvins). This step-like variation of the heat capacity with temperature cannot be explained by classical physics but can be explained by quantized energy levels; see [5.2.3](/5.2.3).

### 1.4.3. Internal Energy of an Ideal Gas

**Definition 1.4.1 (Internal Energy)** The sum of the energies of thermal motion of all the molecules in a system (the kinetic energies of translation, rotation and vibration, and the vibrational potential energy within molecules) and the potential energy of the interactions between molecules is called the **internal energy** of the system, denoted $U$. The internal energy does not include the **mechanical energy** of the system as a whole (the kinetic energy of the motion of its center of mass and its potential energy in external fields).

The energy of molecular thermal motion is determined by temperature, and the intermolecular potential energy is determined by the intermolecular distance, that is, by the volume, so in general $U = U(T, V)$. An ideal gas neglects interactions between molecules, so its internal energy is a function of temperature only:

**Formula 1.4.1 (Internal Energy of an Ideal Gas)** For an ideal gas of amount of substance $n$,
$$
U = N\bar\varepsilon = \frac{t + r + 2s}{2}\,nRT.
\tag{1.4}
$$
For rigid molecules, $U = \frac{i}{2}nRT$ with $i = t + r$.

The zero of internal energy can be chosen arbitrarily; what matters physically is the change in internal energy. In thermodynamics, internal energy will be redefined through adiabatic work ([5.2.3](/5.2.3)), and the two definitions agree.

## 1.5. The Maxwell Speed Distribution

Knowing the root-mean-square speed is not enough to describe a gas: the rates of collisions, effusion and chemical reactions all depend on how many molecules have what **speed**. The statistical distribution of molecular speeds is described by a distribution function; from it one can compute the statistical average of any microscopic quantity, and hence macroscopic quantities.

### 1.5.1. The Speed Distribution Function

Divide the speeds into small intervals, and let $N_i$ molecules have speeds in the $i$th interval $[v_i, v_i + \Delta v_i)$. Such a discrete description depends on how the intervals are chosen and is not convenient for expressing statistical laws. Let the number of molecules with speeds in $[v, v + \mathrm{d}v)$ be $\mathrm{d}N_v$; it is proportional to both the total number $N$ and the interval length $\mathrm{d}v$, with a proportionality factor depending on $v$.

**Definition 1.5.1 (Speed Distribution Function)** The function
$$
f(v) = \frac{\mathrm{d}N_v}{N\,\mathrm{d}v}
$$
is called the **speed distribution function** of the molecules: $f(v)$ is the fraction of the total number of molecules per unit speed interval near the speed $v$. It satisfies the normalization condition
$$
\int_0^{\infty} f(v)\,\mathrm{d}v = 1.
$$

For a single molecule, $f(v)$ is the **probability density function** of its speed (a random variable): $f(v)\,\mathrm{d}v$ is the probability that the molecular speed lies in $[v, v + \mathrm{d}v)$, and the area under the curve $f(v)$ over $[v_1, v_2]$ is the fraction of molecules whose speeds lie in this interval. The average of a microscopic quantity $\phi(v)$ over all molecules is its **expectation**:
$$
\overline{\phi(v)} = \frac{\int \phi(v)\,\mathrm{d}N_v}{N} = \int_0^{\infty}\phi(v)f(v)\,\mathrm{d}v.
$$
The physics literature calls $f(v)$ the "distribution function"; in the terminology of probability theory it is a density, while the distribution function of probability theory means the cumulative distribution function $\int_0^v f(u)\,\mathrm{d}u$.

### 1.5.2. The Maxwell Speed Distribution

**Theorem 1.5.1 (Maxwell Speed Distribution)** For an ideal gas of molecular mass $m$ in an equilibrium state at temperature $T$ (no external field), the speed distribution function of the molecules is
$$
f(v) = 4\pi\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2} v^2\,\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}, \qquad v \ge 0.
\tag{1.5}
$$

It is derived from the velocity distribution; see §1.5.4. The distribution is determined by the competition between two factors: $v^2$ comes from the area of a spherical shell of radius $v$ in velocity space (the larger the speed, the "more" velocity directions are available), while $\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$ suppresses molecules of high energy. Thus $f(v)$ rises from zero, passes through a peak, and then decays rapidly with a long tail.

![Maxwell speed distribution: N2 at three temperatures (left) and different gases at 300 K (right)](./plots/maxwell-speed-distribution.py)

As the temperature rises, the peak moves to the right and becomes lower (the area under the curve is always 1), the fraction of fast molecules increases, and the thermal motion is more vigorous; at a fixed temperature, the larger the molecular mass, the further left and the higher the peak.

### 1.5.3. Three Characteristic Speeds

**Definition 1.5.2** The speed $v_{\mathrm{p}}$ at which $f(v)$ attains its maximum is called the **most probable speed**; the average of the speed, $\bar v = \int_0^\infty vf(v)\,\mathrm{d}v$, is called the **mean speed**.

**Formula 1.5.1** From Eq. (1.5), setting $f'(v_{\mathrm{p}}) = 0$ and computing the moments with the **gamma function** (or the **Gaussian integral**), we obtain
$$
v_{\mathrm{p}} = \sqrt{\frac{2k_{\mathrm{B}}T}{m}} = \sqrt{\frac{2RT}{M}}, \qquad
\bar v = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi m}} = \sqrt{\frac{8RT}{\pi M}}, \qquad
v_{\mathrm{rms}} = \sqrt{\frac{3k_{\mathrm{B}}T}{m}} = \sqrt{\frac{3RT}{M}},
$$
$$
v_{\mathrm{p}} : \bar v : v_{\mathrm{rms}} = \sqrt{2} : \sqrt{8/\pi} : \sqrt{3} \approx 1.41 : 1.60 : 1.73,
$$
and the peak value is $f(v_{\mathrm{p}}) = \sqrt{\frac{8m}{\pi k_{\mathrm{B}}T}}\,\mathrm{e}^{-1} \propto \sqrt{m/T}$.

The value of $v_{\mathrm{rms}}$ computed from the distribution agrees with the result obtained from the pressure formula in §1.3, which is a check of the self-consistency of the theory. The three speeds have different uses: $v_{\mathrm{p}}$ when discussing the speed distribution, $\bar v$ when discussing collisions and effusion, and $v_{\mathrm{rms}}$ when discussing the mean translational kinetic energy.

Using the reduced speed $u = v/v_{\mathrm{p}}$ as the variable, the distribution takes a form independent of the kind of gas and the temperature:
$$
\frac{\mathrm{d}N_v}{N} = \varphi(u)\,\mathrm{d}u, \qquad \varphi(u) = \frac{4}{\sqrt{\pi}}\,u^2\mathrm{e}^{-u^2}.
$$

**Example 1.5.1** For oxygen at $T = 300\,\mathrm{K}$, $v_{\mathrm{p}} \approx 395\,\mathrm{m\,s^{-1}}$. Find the fraction of molecules with speeds between $790$ and $800\,\mathrm{m\,s^{-1}}$.

Solution: $u = 790/395 = 2$ and $\Delta u = 10/395$. The interval is narrow, so
$$
\frac{\Delta N}{N} \approx \frac{4}{\sqrt{\pi}}\,u^2\mathrm{e}^{-u^2}\,\Delta u = \frac{4}{\sqrt{\pi}} \times 4\,\mathrm{e}^{-4} \times \frac{10}{395} \approx 4.2 \times 10^{-3}.
$$
(Integrating exactly over the interval gives $4.0 \times 10^{-3}$; the difference comes from the variation of $f$ within the interval.) A considerable fraction of molecules still have speeds around twice the most probable speed, and this long tail determines the rates of processes that "require large energies," such as chemical reactions.

**Example 1.5.2** Let a hypothetical gas have the speed distribution function $f(v) = av^2$ ($0 \le v \le v_0$) and $f(v) = 0$ ($v > v_0$). Find: (1) the relation between $a$ and $v_0$; (2) the mean speed; (3) the mean speed of the molecules with speeds between $0$ and $v_0/2$.

Solution: (1) By normalization, $\int_0^{v_0} av^2\,\mathrm{d}v = \frac{1}{3}av_0^3 = 1$, so $a = 3/v_0^3$. (2) $\bar v = \int_0^{v_0} v \cdot av^2\,\mathrm{d}v = \frac{a}{4}v_0^4 = \frac{3}{4}v_0$. (3) The mean speed of a subset of the molecules must be divided by the fraction of molecules in that subset, rather than computing $\int_0^{v_0/2} vf(v)\,\mathrm{d}v$ directly:
$$
\bar v' = \frac{\int_0^{v_0/2} vf(v)\,\mathrm{d}v}{\int_0^{v_0/2} f(v)\,\mathrm{d}v} = \frac{\frac{a}{4}(v_0/2)^4}{\frac{a}{3}(v_0/2)^3} = \frac{3}{8}v_0.
$$
This is precisely the **conditional expectation** $\mathbb{E}[v \mid v \le v_0/2]$ of probability theory.

### 1.5.4. The Maxwell Velocity Distribution

The speed distribution does not distinguish directions. In velocity space with coordinates $v_x, v_y, v_z$, let $\mathrm{d}N_{\boldsymbol{v}}$ be the number of molecules whose velocity lies in the volume element $\mathrm{d}^3v = \mathrm{d}v_x\,\mathrm{d}v_y\,\mathrm{d}v_z$ near $\boldsymbol{v}$. The velocity distribution function $F(\boldsymbol{v}) = \frac{\mathrm{d}N_{\boldsymbol{v}}}{N\,\mathrm{d}^3v}$ is the joint probability density of the velocity vector.

**Theorem 1.5.2 (Maxwell Velocity Distribution)** In equilibrium, the velocity distribution function of the molecules of an ideal gas is
$$
F(\boldsymbol{v}) = \left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\mathrm{e}^{-m(v_x^2 + v_y^2 + v_z^2)/(2k_{\mathrm{B}}T)} = g(v_x)\,g(v_y)\,g(v_z),
\qquad g(v_x) = \left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{1/2}\mathrm{e}^{-mv_x^2/(2k_{\mathrm{B}}T)}.
$$

In the language of probability theory: the three velocity components are mutually independent, and each follows the **normal distribution** $\mathcal{N}(0, k_{\mathrm{B}}T/m)$. Maxwell's original argument (1860) was exactly this: if the distribution is isotropic ($F$ depends only on $v^2$) and the three components are independent ($F$ is a product of three copies of the same function), then the only integrable solution of the functional equation $g(v_x)g(v_y)g(v_z) = \Phi(v_x^2 + v_y^2 + v_z^2)$ is a Gaussian function; the constants are fixed by $\overline{v_x^2} = k_{\mathrm{B}}T/m$. A more general derivation follows from the Boltzmann distribution (§1.7.3).

From the velocity distribution to the speed distribution: for molecules with speed in $[v, v + \mathrm{d}v)$ and any direction, the endpoint of the velocity vector lies in a spherical shell of radius $v$ and thickness $\mathrm{d}v$ in velocity space. The volume of the shell is $4\pi v^2\,\mathrm{d}v$ and $F$ is constant on it, so
$$
f(v)\,\mathrm{d}v = F(\boldsymbol{v})\cdot 4\pi v^2\,\mathrm{d}v,
$$
which is Eq. (1.5). Put differently, $mv^2/(k_{\mathrm{B}}T)$ is the sum of squares of three independent standard normal variables and follows the **chi-square distribution** $\chi^2_3$; the speed of a two-dimensional gas (such as molecules adsorbed on a surface) follows the **Rayleigh distribution**. The probability density of the translational kinetic energy $\varepsilon = \frac{1}{2}mv^2$ of a molecule is $\frac{2}{\sqrt{\pi}}(k_{\mathrm{B}}T)^{-3/2}\varepsilon^{1/2}\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$, that is, the $\Gamma(\frac{3}{2}, 1/(k_{\mathrm{B}}T))$ distribution, whose mean $\frac{3}{2}k_{\mathrm{B}}T$ agrees with Eq. (1.3).

## 1.6. Experimental Verification of the Maxwell Speed Distribution

### 1.6.1. The Miller–Kusch Experiment

In 1955 Miller and Kusch tested the Maxwell distribution accurately with a molecular beam. Potassium (or thallium) vapor escapes from an oven through a small hole and forms a molecular beam, which strikes a long cylinder rotating with **angular velocity** $\omega$. The cylinder has length $L$ and carries a helical groove on its surface, with the entrance and exit of the groove offset by an angle $\phi$. A molecule can pass through the groove and reach the detector only if the cylinder turns exactly through $\phi$ during the flight time $L/v$ in the groove, so the speed selected is
$$
v = \frac{\omega L}{\phi}, \qquad \Delta v = \frac{\omega L}{\phi^2}\,\Delta\phi = \frac{v}{\phi}\,\Delta\phi,
$$
where $\Delta\phi$ is the angle corresponding to the width of the groove. Varying $\omega$ and measuring the intensity at the detector gives the speed distribution of the molecular beam.

Note that the distribution at the detector is not $f(v)$ itself:

1. The number of molecules escaping through the hole is proportional to $vf(v)$ (faster molecules hit the hole more often; see the wall collision rate below), so the speed distribution in the beam is $\propto v^3\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$;
2. The speed bandwidth transmitted by the selector is $\Delta v \propto v$, which contributes one more factor of $v$.

The detected intensity is therefore $\propto v^4\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$. The experimental data agree with this prediction to within a few percent, which is the most direct verification of the Maxwell distribution.

![Speed distributions in the gas, in an effusive beam and at the detector of a Miller–Kusch selector, in reduced speed](./plots/miller-kusch.py)

### 1.6.2. The Wall Collision Rate

**Definition 1.6.1** The number of molecules striking a unit area of the wall per unit time is called the **wall collision rate** $\Gamma$.

Take an area element $\mathrm{d}A$ perpendicular to the $x$ axis. The molecules with velocity in $\mathrm{d}^3v$ near $\boldsymbol{v}$ and $v_x > 0$ that can hit $\mathrm{d}A$ within $\mathrm{d}t$ lie in a slanted cylinder of volume $v_x\,\mathrm{d}t\,\mathrm{d}A$; there are $n_Vv_x\,\mathrm{d}t\,\mathrm{d}A\,F(\boldsymbol{v})\,\mathrm{d}^3v$ of them. Integrating over $v_y$ and $v_z$ (each gives 1) and over $v_x > 0$:

**Formula 1.6.1**
$$
\Gamma = n_V\int_0^{\infty} v_x\,g(v_x)\,\mathrm{d}v_x = n_V\sqrt{\frac{k_{\mathrm{B}}T}{2\pi m}} = \frac{1}{4}n_V\bar v.
$$

**Example 1.6.1 (Effusion)** A container of volume $V$ holds gas at a constant temperature $T$ and initial pressure $p_0$. There is a small hole of area $\Delta A$ in the wall leading to a vacuum (or to surroundings at a pressure much lower than $p_0$). The hole is much smaller than the mean free path of the molecules ([5.2.2](/5.2.2)), so the molecules "leak out" one by one without forming a macroscopic flow. Find the time required for the pressure to fall to $p_0/2$.

Solution: Let there be $N$ molecules in the container at time $t$. Then $\mathrm{d}N = -\Gamma\,\Delta A\,\mathrm{d}t = -\frac{\bar v\,\Delta A}{4V}N\,\mathrm{d}t$. At constant $T$, $p = Nk_{\mathrm{B}}T/V \propto N$, so
$$
\frac{\mathrm{d}p}{\mathrm{d}t} = -\frac{\bar v\,\Delta A}{4V}\,p, \qquad p(t) = p_0\,\mathrm{e}^{-t/\tau},\quad \tau = \frac{4V}{\bar v\,\Delta A},
$$
which is the exponentially decaying solution of a first-order **linear differential equation**. The time for the pressure to halve is $\Delta t = \tau\ln 2$. For oxygen at $T = 300\,\mathrm{K}$, $\bar v \approx 445\,\mathrm{m\,s^{-1}}$; taking $V = 1\,\mathrm{L}$ and $\Delta A = 0.1\,\mathrm{mm^2}$ gives $\Delta t \approx 62\,\mathrm{s}$.

### 1.6.3. Isotope Separation by Diffusion

When a mixture of molecules of two isotopes effuses through a porous membrane, the wall collision rate is $\Gamma \propto n_V\bar v \propto n_V/\sqrt{m}$, so the lighter molecules pass through in greater numbers. Let the number densities of the two kinds of molecules be $n_1, n_2$ and their masses $m_1 < m_2$. The factor by which the abundance ratio is enhanced after one effusion step (the single-stage separation factor) is
$$
\alpha = \frac{(n_1/n_2)_{\mathrm{after}}}{(n_1/n_2)_{\mathrm{before}}} = \frac{\bar v_1}{\bar v_2} = \sqrt{\frac{m_2}{m_1}}.
$$

**Example 1.6.2 (Uranium Enrichment)** The abundance of $^{235}\mathrm{U}$ in natural uranium is $0.71\%$, while fuel for nuclear power plants requires about $3\%$. Use effusion of $\ce{UF6}$ gas (fluorine has only one stable isotope, $^{19}\mathrm{F}$, so the mass difference between the two kinds of molecules comes only from uranium):
$$
\alpha = \sqrt{\frac{238 + 6 \times 19}{235 + 6 \times 19}} = \sqrt{\frac{352}{349}} \approx 1.0043.
$$
The abundance ratio must be raised from $0.71/99.29 = 7.15 \times 10^{-3}$ to $3/97 = 3.09 \times 10^{-2}$, a factor of $4.33$, so the number of stages $N_{\mathrm{s}}$ required satisfies $\alpha^{N_{\mathrm{s}}} = 4.33$:
$$
N_{\mathrm{s}} = \frac{\ln 4.33}{\ln 1.0043} \approx 3.4 \times 10^2.
$$
Reaching weapons grade (about $90\%$) would require about $1.7 \times 10^3$ stages. This is an idealized estimate; the actual single-stage separation factor is closer to 1 and many more stages are needed. Gaseous diffusion plants consume enormous amounts of electricity and have all been shut down; present-day uranium enrichment relies mainly on gas centrifuges, whose principle is given in Example 1.7.1.

## 1.7. The Boltzmann Distribution

### 1.7.1. Distribution of the Number Density in a Gravitational Field

Thermal motion tends to distribute molecules uniformly, while gravity pulls them toward the bottom; the competition between the two produces a definite distribution at equilibrium. Let the atmosphere have the same temperature $T$ everywhere, and let the molecular mass be $m$. Take a thin layer of gas between heights $z$ and $z + \mathrm{d}z$ with base area $S$. Mechanical equilibrium requires $(p + \mathrm{d}p)S + mgn_VS\,\mathrm{d}z = pS$, that is, $\mathrm{d}p = -mgn_V\,\mathrm{d}z$. With $p = n_Vk_{\mathrm{B}}T$,
$$
\frac{\mathrm{d}n_V}{n_V} = -\frac{mg}{k_{\mathrm{B}}T}\,\mathrm{d}z.
$$

**Formula 1.7.1 (Isothermal Barometric Formula)** Let the number density and pressure at $z = 0$ be $n_0$ and $p_0$. Then
$$
n_V(z) = n_0\,\mathrm{e}^{-mgz/(k_{\mathrm{B}}T)}, \qquad p(z) = p_0\,\mathrm{e}^{-mgz/(k_{\mathrm{B}}T)} = p_0\,\mathrm{e}^{-Mgz/(RT)}.
$$

The characteristic height $H = RT/(Mg)$ is about $8.4\,\mathrm{km}$ for air ($M \approx 29\,\mathrm{g\,mol^{-1}}$, $T \approx 288\,\mathrm{K}$): the pressure drops by a factor of $1/\mathrm{e}$ for every $8.4\,\mathrm{km}$ of ascent. Height can thus be estimated from the pressure (the principle of the altimeter); in reality the temperature of the atmosphere varies with height, so the formula is only approximate.

### 1.7.2. The Boltzmann Distribution Law

It is no accident that the gravitational potential energy $mgz$ appears in the exponent. Let a molecule be in an arbitrary conservative external field with potential energy $\varepsilon_{\mathrm{p}}(\boldsymbol{r})$. Then

**Theorem 1.7.1 (Boltzmann Distribution)** In an equilibrium state at temperature $T$, the number of molecules in the volume element $\mathrm{d}^3r = \mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ near $\boldsymbol{r}$ is
$$
\mathrm{d}N_{\boldsymbol{r}} = n_0\,\mathrm{e}^{-\varepsilon_{\mathrm{p}}(\boldsymbol{r})/(k_{\mathrm{B}}T)}\,\mathrm{d}^3r,
$$
where $n_0$ is the number density where $\varepsilon_{\mathrm{p}} = 0$. More generally, in equilibrium the probability that a system is in a microscopic state of energy $\varepsilon$ is proportional to $\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$.

The factor $\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}$ is called the *Boltzmann factor*. It says that the higher the energy of a state, the harder it is to occupy, and the yardstick for "high" and "low" is $k_{\mathrm{B}}T$: a state with $\varepsilon \ll k_{\mathrm{B}}T$ is almost as easy to occupy as the ground state, while a state with $\varepsilon \gg k_{\mathrm{B}}T$ is almost empty. Summing the Boltzmann factors over all states gives the partition function $Z = \sum_s \mathrm{e}^{-\varepsilon_s/(k_{\mathrm{B}}T)}$, from which all thermodynamic quantities can be obtained; sampling from the Boltzmann distribution by Monte Carlo methods was the original purpose of the Metropolis algorithm ([3.5.9](/3.5.9)).

**Example 1.7.1 (Rotating Container and Centrifugal Separation)** A cylinder containing gas rotates uniformly about a vertical axis with angular velocity $\omega$. In the **reference frame** rotating with the cylinder, a molecule experiences the **centrifugal force** $m\omega^2r$, with the corresponding potential energy $\varepsilon_{\mathrm{p}}(r) = -\int_0^r m\omega^2r'\,\mathrm{d}r' = -\frac{1}{2}m\omega^2r^2$ (zero on the axis). By the Boltzmann distribution,
$$
n_V(r) = n_0\,\mathrm{e}^{m\omega^2r^2/(2k_{\mathrm{B}}T)},
$$
and the molecules concentrate toward the wall of the cylinder. The ratio of the abundance ratios of the two isotopic molecules at radius $r$ and on the axis is $\mathrm{e}^{(m_2 - m_1)\omega^2r^2/(2k_{\mathrm{B}}T)}$, which depends only on the mass difference $m_2 - m_1$, whereas the separation factor of the effusion method depends on the square root of the mass ratio. For $\ce{UF6}$, when the linear speed $\omega r$ at the wall reaches several hundred meters per second, the single-stage separation factor can exceed 1.1, far greater than the value 1.0043 for effusion; this is why gas centrifuges replaced diffusion.

### 1.7.3. The Maxwell–Boltzmann Distribution

Considering position and velocity together, the number of molecules in $\mathrm{d}^3r$ near $\boldsymbol{r}$ with velocity in $\mathrm{d}^3v$ near $\boldsymbol{v}$ is
$$
\mathrm{d}N = n_0\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\mathrm{e}^{-\varepsilon/(k_{\mathrm{B}}T)}\,\mathrm{d}^3r\,\mathrm{d}^3v, \qquad \varepsilon = \frac{1}{2}mv^2 + \varepsilon_{\mathrm{p}}(\boldsymbol{r}),
$$
called the Maxwell–Boltzmann distribution. It is the application of the Boltzmann distribution to the total energy of a molecule (kinetic plus potential): integrating over $\boldsymbol{r}$ recovers the Maxwell velocity distribution, and integrating over $\boldsymbol{v}$ recovers Theorem 1.7.1. The position distribution and the velocity distribution of the molecules are independent, so in a gravitational field the gas has the same temperature and the same velocity distribution at every height, differing only in number density.

**Remark 1.7.1 (Proof of the Equipartition Theorem)** Suppose the energy of a molecule contains a term $a\xi^2$ ($\xi$ being a velocity component, an angular velocity or a vibrational coordinate, with $a > 0$) that is added to the remaining terms. By the Boltzmann distribution, the probability density of $\xi$ is proportional to $\mathrm{e}^{-a\xi^2/(k_{\mathrm{B}}T)}$, that is, the **normal distribution** $\mathcal{N}(0, k_{\mathrm{B}}T/(2a))$, so
$$
\overline{a\xi^2} = a \cdot \frac{k_{\mathrm{B}}T}{2a} = \frac{1}{2}k_{\mathrm{B}}T,
$$
independent of $a$. This is the **equipartition theorem**. It depends on two points: the energy is a quadratic function of $\xi$, and $\xi$ can take continuous values. The latter fails in quantum mechanics, which gives rise to the "freezing out" of degrees of freedom.

**Example 1.7.2 (Populations of Atomic Energy Levels)** The ground-state energy of the hydrogen atom is $E_1 = -13.6\,\mathrm{eV}$ and the first excited state has $E_2 = E_1/4 = -3.4\,\mathrm{eV}$, so $\Delta E = 10.2\,\mathrm{eV}$. At room temperature $T = 300\,\mathrm{K}$, $k_{\mathrm{B}}T \approx 0.0259\,\mathrm{eV}$, and the ratio of the numbers of atoms in the two levels (per state) is
$$
\frac{N_2}{N_1} = \mathrm{e}^{-\Delta E/(k_{\mathrm{B}}T)} \approx \mathrm{e}^{-394} \approx 10^{-171}.
$$
The first excited level has 4 orbital states while the ground level has only 1 (spin not counted), so the total population of the level must be multiplied by the degeneracy ratio 4; the conclusion is unchanged: at room temperature the number of atoms in the excited state is negligible, and almost all atoms are in the ground state. To make the excited state more populated than the ground state (population inversion, the condition for lasing), the system must be driven away from equilibrium with energy from outside.

## Summary

| Topic | Result |
|---|---|
| Equation of state | $pV = nRT$, $p = n_Vk_{\mathrm{B}}T$, $R = N_{\mathrm{A}}k_{\mathrm{B}}$ |
| Pressure formula | $p = \frac{1}{3}n_Vm\overline{v^2} = \frac{2}{3}n_V\bar\varepsilon_{\mathrm{t}}$ |
| Statistical meaning of temperature | $\bar\varepsilon_{\mathrm{t}} = \frac{3}{2}k_{\mathrm{B}}T$ |
| Equipartition | $\frac{1}{2}k_{\mathrm{B}}T$ per quadratic term; $\bar\varepsilon = \frac{1}{2}(t + r + 2s)k_{\mathrm{B}}T$; ideal gas $U = \frac{t + r + 2s}{2}nRT$ |
| Maxwell speed distribution | $f(v) = 4\pi\left(\frac{m}{2\pi k_{\mathrm{B}}T}\right)^{3/2}v^2\mathrm{e}^{-mv^2/(2k_{\mathrm{B}}T)}$; velocity components are independent and follow $\mathcal{N}(0, k_{\mathrm{B}}T/m)$ |
| Characteristic speeds | $v_{\mathrm{p}} = \sqrt{2k_{\mathrm{B}}T/m}$, $\bar v = \sqrt{8k_{\mathrm{B}}T/(\pi m)}$, $v_{\mathrm{rms}} = \sqrt{3k_{\mathrm{B}}T/m}$ |
| Wall collision rate | $\Gamma = \frac{1}{4}n_V\bar v$ |
| Boltzmann distribution | $\mathrm{d}N_{\boldsymbol{r}} = n_0\mathrm{e}^{-\varepsilon_{\mathrm{p}}/(k_{\mathrm{B}}T)}\mathrm{d}^3r$; isothermal barometric formula $p = p_0\mathrm{e}^{-Mgz/(RT)}$ |

## Questions

1. At a fixed temperature, how do the Maxwell speed distribution curves of two gases with molecular masses $m_2 > m_1$ differ?

   **Answer** $v_{\mathrm{p}} \propto 1/\sqrt{m}$, so the peak moves left; $f(v_{\mathrm{p}}) \propto \sqrt{m}$, so the peak is higher; the areas under both curves are 1.

2. At room temperature, which has the larger mean translational kinetic energy, an $\ce{N2}$ or an $\ce{O2}$ molecule in air? Which has the larger root-mean-square speed?

   **Answer** the mean translational kinetic energy depends only on temperature, so they are equal; $v_{\mathrm{rms}} \propto 1/\sqrt{M}$, so that of $\ce{N2}$ is slightly larger.
