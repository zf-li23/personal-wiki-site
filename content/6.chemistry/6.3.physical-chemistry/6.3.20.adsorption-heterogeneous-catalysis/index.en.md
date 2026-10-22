---
title: Adsorption on Solid Surfaces and Heterogeneous Catalysis
source_hash: ada92d2b3ac4
---

A liquid can lower its surface Gibbs free energy by contracting its surface and changing its surface composition ([6.3.19](/6.3.19)), but the atoms at a solid surface can hardly move, and the surface energy can be lowered only by capturing molecules from a gas or a solution. This adsorption is the common basis of heterogeneous catalysis, gas separation and purification, drying and decolorization, chromatography and sensing, and is also the method of determining the specific surface area and pore structure of solids. This chapter first introduces the amount adsorbed and adsorption curves (20.1), compares physical adsorption with chemical adsorption and discusses heats of adsorption (20.2); then establishes the Langmuir theory of monolayer adsorption (20.3), extends it to nonuniform surfaces in 20.4 (the Freundlich and Temkin isotherms), and establishes the BET theory of multilayer adsorption (20.5), the standard method for determining specific surface area; next it discusses capillary condensation and pore size distributions in porous solids (20.6, using the **Kelvin equation** of [6.3.19](/6.3.19)) and the kinetics of chemisorption (20.7, using the **effusion** flux of [5.2.1](/5.2.1)); finally it applies these results to the kinetics of gas–solid catalytic reactions (20.8), making the qualitative introduction to **heterogeneous catalysis** in [6.1.7](/6.1.7#sec-7.3.4) quantitative.

## 20.1. Adsorption and the Amount Adsorbed

### 20.1.1. Characteristics of Solid Surfaces

The atoms on a solid surface, like the molecules on a liquid surface, are in an asymmetric force field and also have a surface tension and surface energy, usually much larger than those of liquids (the surface energy of metals is about $1$–$3\,\mathrm{J\,m^{-2}}$, ten to several tens of times that of water). But solid surfaces have their own characteristics:

- Surface atoms move with difficulty, so the surface energy cannot be lowered by reducing the surface area but only by adsorbing foreign molecules;
- The surface is nonuniform: at steps, kinks, vacancies, grain boundaries and impurity atoms the coordination numbers differ, and so do the heat of adsorption, the chemical reactivity and the electronic energy levels;
- The composition and structure of the surface layer can differ from those of the bulk (segregation, reconstruction).

### 20.1.2. Adsorbent, Adsorbate and Amount Adsorbed

**Definition 20.1.1** The enrichment of molecules from a gas or solution on a solid surface is called adsorption on the solid surface, and its reverse is called **desorption**. The solid that adsorbs is called the **adsorbent** and the substance adsorbed the **adsorbate**.

Commonly used adsorbents are activated carbon, silica gel, activated alumina, molecular sieves (zeolites) and metal–organic frameworks; for measuring specific surface area, $\ce{N2}$ (77 K), Ar (87 K), $\ce{CO2}$ (273 K), water vapor or benzene vapor are commonly used as adsorbates. Adsorption equilibrium is reached when the rates of adsorption and desorption are equal, and the amount of adsorbate adsorbed per unit mass of adsorbent is then called the amount adsorbed, expressed as an amount of substance $n^{\mathrm{a}}/m$ ($\mathrm{mol\,g^{-1}}$) or as the gas volume $V^{\mathrm{a}}$ converted to standard conditions ($\mathrm{cm^3\,g^{-1}}$). The "standard conditions" in the adsorption literature still use $273.15\,\mathrm{K}$ and $101.325\,\mathrm{kPa}$, with a molar gas volume of $22.414\,\mathrm{L\,mol^{-1}}$.

There are two main methods of measurement. In the volumetric method, adsorbate is admitted to a system of known volume and the amount adsorbed is calculated from the pressure change before and after adsorption; this is the principle of $\ce{N2}$ adsorption instruments. In the gravimetric method, the increase in mass of the adsorbent after adsorption is weighed directly with a quartz spring balance or a microbalance. Before measurement the adsorbent must be degassed by heating in vacuum to remove gas and water already adsorbed.

### 20.1.3. Adsorption Curves

For a given adsorbent–adsorbate system, the equilibrium amount adsorbed is a function of temperature and pressure, $n^{\mathrm{a}} = f(T, p)$. Fixing one variable gives three kinds of adsorption curves.

**Definition 20.1.2** The curve of the amount adsorbed against equilibrium pressure at constant temperature is called the **adsorption isotherm**; the relation of the amount adsorbed to temperature at constant pressure is called the **adsorption isobar**; the relation of equilibrium pressure to temperature at a constant amount adsorbed is called the **adsorption isostere**.

The three can be converted into one another, and the adsorption isotherm is the most commonly used. Adsorption isobars show that the amount of physical adsorption decreases monotonically with increasing temperature (adsorption is exothermic); chemisorption requires activation, and in the low-temperature region the amount adsorbed may increase with temperature (equilibrium has not yet been reached) and falls because of the exothermicity only at higher temperatures. Adsorption isosteres are used to find the heat of adsorption (20.2.2).

## 20.2. Physical Adsorption and Chemical Adsorption

### 20.2.1. Comparison of the Two Kinds of Adsorption

**Definition 20.2.1** Adsorption in which only **van der Waals forces** act between adsorbate and adsorbent is called **physical adsorption** (physisorption); adsorption in which chemical bonds are formed (with electron transfer or sharing) between the adsorbate and the surface atoms of the adsorbent is called **chemical adsorption** (chemisorption).

| Property | Physical adsorption | Chemical adsorption |
|---|---|---|
| Force | van der Waals forces | Chemical bonding forces |
| Heat of adsorption (absolute value) | Small, close to or slightly larger than the enthalpy of condensation of the adsorbate, generally a few to tens of $\mathrm{kJ\,mol^{-1}}$ | Large, close to the enthalpy of reaction, generally above $40\,\mathrm{kJ\,mol^{-1}}$ and up to several hundred |
| Selectivity | Not selective: any solid can adsorb any gas (at low temperature), only the amounts differ | Selective: only molecules that can bond with the surface are adsorbed |
| Adsorbed layer | Monolayer or multilayer | Monolayer |
| Rate and activation energy | Fast, almost no activation energy needed | Activation energy often needed, rate increases with temperature |
| Reversibility | Reversible, desorbs easily | Often does not desorb easily, and other substances may be obtained on desorption (such as $\ce{O2}$ chemisorbed on carbon desorbing as CO) |
| Temperature range | Low temperature (near the boiling point of the adsorbate) | Higher temperature |
| Spectra | The characteristic bands of the adsorbate are essentially unchanged | New characteristic absorption bands appear |

For example the heat of physical adsorption of $\ce{N2}$ on activated carbon is about $10$–$20\,\mathrm{kJ\,mol^{-1}}$ (the $\Delta_{\mathrm{vap}}H_{\mathrm{m}}$ of $\ce{N2}$ is $5.6\,\mathrm{kJ\,mol^{-1}}$), the heat of dissociative chemisorption of $\ce{H2}$ on Ni is about $90\,\mathrm{kJ\,mol^{-1}}$, and the heat of chemisorption of $\ce{O2}$ on W exceeds $800\,\mathrm{kJ\,mol^{-1}}$. The two kinds of adsorption can occur together: at low temperature $\ce{H2}$ is physically adsorbed on Ni, and at higher temperature it changes into dissociative chemisorption.

### 20.2.2. Thermodynamics of Adsorption

A gas molecule loses all or part of its translational degrees of freedom on adsorption, so the entropy change of the adsorption process is $\Delta S < 0$. Adsorption proceeds spontaneously at constant temperature and pressure, $\Delta G < 0$, so $\Delta H = \Delta G + T\Delta S < 0$: adsorption is generally exothermic, low temperature favors adsorption and raising the temperature causes desorption. (A few cases of dissociative adsorption are exceptions, because the adsorbate can move freely on the surface.)

**Definition 20.2.2** The heat released in the adsorption process is called the **heat of adsorption**. The total heat released when a given amount of adsorbent adsorbs a given amount of gas starting from zero at constant temperature is called the integral heat of adsorption; the ratio of the heat released when a small amount $\mathrm{d}n^{\mathrm{a}}$ is adsorbed after $n^{\mathrm{a}}$ has already been adsorbed to $\mathrm{d}n^{\mathrm{a}}$ is called the differential heat of adsorption. By convention the heat of adsorption is taken as positive and equals the absolute value of the molar enthalpy of adsorption $\Delta_{\mathrm{ads}}H_{\mathrm{m}}$ (which is negative).

The magnitude of the heat of adsorption reflects the strength of adsorption. The differential heat of adsorption generally decreases with increasing coverage: the positions of highest energy are occupied first, and adsorbed molecules also repel each other. The heat of adsorption can be measured directly with a calorimeter or found from adsorption isosteres. At a fixed amount adsorbed, the adsorbed state is in equilibrium with the gas phase, $\mu_{\mathrm{ads}}(T, n^{\mathrm{a}}) = \mu_{\mathrm{g}}(T, p)$, and exactly the same argument as in the derivation of the **Clausius–Clapeyron equation** gives

$$
\left(\frac{\partial\ln p}{\partial T}\right)_{n^{\mathrm{a}}} = -\frac{\Delta_{\mathrm{ads}}H_{\mathrm{m}}}{RT^2}. \tag{20.1}
$$

The heat of adsorption obtained in this way is called the *isosteric heat of adsorption*. $\Delta_{\mathrm{ads}}H_{\mathrm{m}} < 0$, and when the temperature rises the pressure must be increased to maintain the same amount adsorbed.

**Example 20.2.1** For a gas on an adsorbent, at the same amount adsorbed the equilibrium pressure is $1.0\,\mathrm{kPa}$ at $273\,\mathrm{K}$ and $4.0\,\mathrm{kPa}$ at $298\,\mathrm{K}$. Integrating Eq. (20.1),

$$
\Delta_{\mathrm{ads}}H_{\mathrm{m}} = \frac{R\ln(p_2/p_1)}{1/T_2 - 1/T_1} = \frac{8.314 \times \ln 4}{1/298 - 1/273}\,\mathrm{J\,mol^{-1}} = -37.5\,\mathrm{kJ\,mol^{-1}},
$$
a value near the boundary between physical and chemical adsorption, so other evidence (spectra, reversibility) is needed to decide.

### 20.2.3. From Physical Adsorption to Chemical Adsorption

Lennard-Jones (1932) used potential-energy curves to explain the relation between the two kinds of adsorption. Take the adsorption of $\ce{H2}$ on a metal surface as an example: as an intact $\ce{H2}$ molecule approaches the surface it first falls into a shallow van der Waals potential well (physical adsorption); the potential-energy curve for two H atoms bonded to the surface lies, far away, higher than the bond energy of $\ce{H2}$, $436\,\mathrm{kJ\,mol^{-1}}$, but has a much deeper well at short range (dissociative chemisorption). For the molecule to pass from the physically adsorbed state to the chemisorbed state it has to cross the intersection of the two curves. When the intersection lies above zero (the energy of the gas-phase molecule), chemisorption is activated adsorption, and the height of the intersection is the activation energy $E_{\mathrm{a}}$ of adsorption; when the intersection lies below zero, a physically adsorbed molecule can slide directly into the chemisorbed state and chemisorption needs no activation (this is the case for $\ce{H2}$ on clean Ni and Pd). The physically adsorbed state is therefore often the precursor state of chemisorption.

![Lennard-Jones potential-energy diagram for H₂ approaching a metal surface: the shallow physisorption well of the intact molecule (blue) and the deep chemisorption well of two H atoms (red), the latter lying at the H–H bond energy of 436 kJ/mol far from the surface. When the intersection of the two curves lies above zero, its height is the activation energy Ea of dissociative chemisorption](./plots/adsorption-potential.py)

## 20.3. The Langmuir Adsorption Isotherm

### 20.3.1. Basic Assumptions and Derivation

Langmuir (1916) regarded adsorption as the result of gas molecules being temporarily held after colliding with the solid surface, and adsorption equilibrium as a dynamic equilibrium in which the rates of adsorption and desorption are equal. His assumptions are:

1. Adsorption is monolayer: each adsorption site can hold only one molecule, and a gas molecule can be adsorbed only if it hits a vacant site;
2. The solid surface is uniform, all adsorption sites have the same adsorption capacity, and the heat of adsorption is independent of the degree of coverage;
3. There is no interaction between adsorbed molecules, and the probability that a molecule desorbs from the surface is independent of whether the neighboring sites are occupied.

**Definition 20.3.1** The ratio of the number of adsorption sites on the solid surface that are occupied by adsorbate to the total number of adsorption sites is called the **coverage** $\theta$, $0 \le \theta \le 1$. Under the assumption of monolayer adsorption, $\theta = n^{\mathrm{a}}/n^{\mathrm{a}}_{\mathrm{mono}} = V^{\mathrm{a}}/V^{\mathrm{a}}_{\mathrm{mono}}$, where $V^{\mathrm{a}}_{\mathrm{mono}}$ is the amount adsorbed when a complete monolayer is formed (the saturation adsorption).

**Theorem 20.3.1 (Langmuir Adsorption Isotherm)** Under the above assumptions, the equilibrium coverage at pressure $p$ is

$$
\theta = \frac{ap}{1 + ap}, \qquad V^{\mathrm{a}} = \frac{V^{\mathrm{a}}_{\mathrm{mono}}\,ap}{1 + ap}, \tag{20.2}
$$
where $a$ is called the adsorption coefficient and depends only on temperature.

**Proof** Regard adsorption as a reversible "reaction": a gas molecule B combines with an empty adsorption site $\ast$, $\mathrm{B(g)} + \ast \rightleftharpoons \mathrm{B}^\ast$ ($\mathrm{B}^\ast$ denotes adsorbed B). The number of molecules adsorbed per unit time and area is proportional to the frequency of molecular collisions with the surface (proportional to $p$) and to the fraction of vacant sites $1 - \theta$: $r_{\mathrm{a}} = k_{\mathrm{a}}p(1 - \theta)$; the number desorbed is proportional to the occupied fraction: $r_{\mathrm{d}} = k_{\mathrm{d}}\theta$. At equilibrium $r_{\mathrm{a}} = r_{\mathrm{d}}$,

$$
k_{\mathrm{a}}p(1 - \theta) = k_{\mathrm{d}}\theta \quad\Longrightarrow\quad \frac{\theta}{1 - \theta} = ap, \quad a = \frac{k_{\mathrm{a}}}{k_{\mathrm{d}}},
$$
and solving for $\theta$ gives the result. $\square$

$a$ is the equilibrium constant of the adsorption "reaction" and represents the strength of adsorption. The same result can also be derived by statistical thermodynamics ([6.3.10](/6.3.10)): regard the adsorbed molecules as localized particles on $N_{\mathrm{s}}$ sites, find their chemical potential from the partition function of the adsorbed phase and equate it to the chemical potential of the gas phase, and $a$ is then expressed by the ratio of the partition functions of the adsorbed and gas-phase molecules. This derivation requires no assumption about the specific kinetic mechanism, which shows that the Langmuir equation is an equilibrium property.

### 20.3.2. Discussion of the Isotherm

![Left: Langmuir isotherms θ = ap/(1 + ap) for adsorption coefficients a = 0.1, 1, 10 kPa⁻¹; the coverage rises linearly at low pressure and tends to monolayer saturation at high pressure. Right: on log–log axes the slope of the low-pressure part is 1 for molecular adsorption and 1/2 for dissociative adsorption](./plots/langmuir.py)

- At very low pressure or very weak adsorption, $ap \ll 1$ and $\theta \approx ap$: the amount adsorbed is proportional to pressure, corresponding to a two-dimensional **Henry's law**.
- At very high pressure or very strong adsorption, $ap \gg 1$ and $\theta \approx 1$: the monolayer is complete and the amount adsorbed is independent of pressure.
- At intermediate pressure $\theta$ is approximately proportional to $p^{m}$ with $0 < m < 1$.

Rewriting Eq. (20.2) in linear form

$$
\frac{p}{V^{\mathrm{a}}} = \frac{1}{aV^{\mathrm{a}}_{\mathrm{mono}}} + \frac{p}{V^{\mathrm{a}}_{\mathrm{mono}}},
$$
a plot of $p/V^{\mathrm{a}}$ against $p$ is a straight line, and $V^{\mathrm{a}}_{\mathrm{mono}}$ and $a$ are found from its slope and intercept. If the cross-sectional area $\sigma_{\mathrm{m}}$ of the adsorbate molecule is known, the specific surface area of the adsorbent is

$$
a_{\mathrm{s}} = \frac{V^{\mathrm{a}}_{\mathrm{mono}}}{22.414\,\mathrm{L\,mol^{-1}}}N_{\mathrm{A}}\sigma_{\mathrm{m}}.
$$
For $\ce{N2}$ ($\sigma_{\mathrm{m}} = 0.162\,\mathrm{nm^2}$), each $1\,\mathrm{cm^3}$ (at standard conditions) of monolayer adsorption corresponds to a surface of $4.35\,\mathrm{m^2}$.

The adsorption coefficient is an equilibrium constant, and by the van 't Hoff equation ([6.3.7](/6.3.7))

$$
\left(\frac{\partial\ln a}{\partial T}\right)_\theta = \frac{\Delta_{\mathrm{ads}}H_{\mathrm{m}}}{RT^2}, \qquad a = a_0\exp\left(-\frac{\Delta_{\mathrm{ads}}H_{\mathrm{m}}}{RT}\right).
$$
Adsorption is exothermic, so $a$ decreases with increasing temperature and the amount adsorbed at the same pressure falls. In the Langmuir equation the heat of adsorption is independent of the coverage, so the $\Delta_{\mathrm{ads}}H_{\mathrm{m}}$ here is both the integral and the differential enthalpy of adsorption.

The Langmuir equation often applies to chemisorption and to physical adsorption at low pressure, but real surfaces are nonuniform, adsorbed molecules interact with one another, and physical adsorption can also form multilayers, all of which deviate from the Langmuir assumptions. Its value lies in giving a limit with a clear physical picture, and the various isotherms that follow are all obtained by relaxing one of its assumptions.

### 20.3.3. Dissociative Adsorption and Competitive Adsorption

**Definition 20.3.2** Adsorption in which the adsorbate molecule breaks into two or more particles, each occupying one adsorption site, is called **dissociative adsorption**.

Examples are the chemisorption of $\ce{H2}$ on Pt and of $\ce{N2}$ on Fe: $\mathrm{H_2(g)} + 2\ast \rightleftharpoons 2\mathrm{H}^\ast$. Adsorption requires hitting two adjacent vacant sites at once, $r_{\mathrm{a}} = k_{\mathrm{a}}p(1 - \theta)^2$; desorption requires two adsorbed atoms to meet, $r_{\mathrm{d}} = k_{\mathrm{d}}\theta^2$. At equilibrium

$$
\frac{\theta}{1 - \theta} = (ap)^{1/2}, \qquad \theta = \frac{(ap)^{1/2}}{1 + (ap)^{1/2}}.
$$
At low pressure $\theta \propto p^{1/2}$. An experimentally observed proportionality of the amount adsorbed to $p^{1/2}$ at low pressure is therefore evidence that dissociation occurs on adsorption.

**Definition 20.3.3** Adsorption in which two or more adsorbates compete for the same set of adsorption sites at the same time is called **competitive adsorption**.

When gases A and B are adsorbed on the same surface, at equilibrium $\theta_{\mathrm{A}}/(1 - \theta_{\mathrm{A}} - \theta_{\mathrm{B}}) = a_{\mathrm{A}}p_{\mathrm{A}}$ and $\theta_{\mathrm{B}}/(1 - \theta_{\mathrm{A}} - \theta_{\mathrm{B}}) = a_{\mathrm{B}}p_{\mathrm{B}}$, which give

$$
\theta_{\mathrm{A}} = \frac{a_{\mathrm{A}}p_{\mathrm{A}}}{1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}}}, \qquad \theta_{\mathrm{B}} = \frac{a_{\mathrm{B}}p_{\mathrm{B}}}{1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}}}.
$$
For several gases $\theta_{\mathrm{B}} = a_{\mathrm{B}}p_{\mathrm{B}}/(1 + \sum_{\mathrm{C}}a_{\mathrm{C}}p_{\mathrm{C}})$. The presence of B decreases the coverage of A: a strongly adsorbed impurity displaces the reactant from the surface, which is the cause of catalyst poisoning and product inhibition (20.8), and also the basis of gas separation by pressure swing adsorption and of chromatographic separation. Competitive inhibition in biochemistry (the substrate and the inhibitor compete for the active site of an enzyme) has exactly the same mathematical form.

## 20.4. The Freundlich and Temkin Adsorption Isotherms

### 20.4.1. Two Empirical Equations

The Langmuir equation assumes that the heat of adsorption is independent of coverage, whereas the actual differential heat of adsorption always decreases with increasing coverage. Two commonly used empirical equations correspond to two ways in which the heat of adsorption decreases.

**Formula 20.4.1 (Freundlich Adsorption Isotherm)**

$$
\frac{n^{\mathrm{a}}}{m} = kp^{1/n},
$$
where $k$ and $n$ are constants depending on the temperature and the system, with $n > 1$. Taking logarithms, $\lg(n^{\mathrm{a}}/m) = \lg k + \frac{1}{n}\lg p$, and a plot of $\lg(n^{\mathrm{a}}/m)$ against $\lg p$ is a straight line.

The Freundlich equation often fits better than the Langmuir equation over a medium pressure range and applies to physical adsorption, chemisorption and adsorption from solution, but it has no saturation value and cannot be used at high pressure.

**Formula 20.4.2 (Temkin Adsorption Isotherm)**

$$
\theta = \frac{RT}{\alpha}\ln(A_0p),
$$
where $A_0$ is a constant related to the adsorption equilibrium constant and $\alpha$ is related to how fast the heat of adsorption falls with coverage.

The Temkin equation is used mainly for chemisorption and holds at medium coverage (it fails at very low or very high coverage). In the kinetic treatment of industrial catalytic reactions such as ammonia synthesis and the water–gas shift it is often used to describe the adsorption of the reactants.

### 20.4.2. Interpretation in Terms of Nonuniform Surfaces

Write the heat of adsorption as a function of coverage, $Q_{\mathrm{a}}(\theta) = -\Delta_{\mathrm{ads}}H_{\mathrm{m}}(\theta) > 0$. Suppose the local equilibrium at coverage $\theta$ can still be written in the Langmuir form, with the heat of adsorption taken at that coverage:

$$
\frac{\theta}{1 - \theta} = a_0p\exp\frac{Q_{\mathrm{a}}(\theta)}{RT}.
$$

If the heat of adsorption falls logarithmically with coverage, $Q_{\mathrm{a}}(\theta) = -Q_{\mathrm{m}}\ln\theta$ ($Q_{\mathrm{m}} > 0$), then $\exp(Q_{\mathrm{a}}/RT) = \theta^{-Q_{\mathrm{m}}/RT}$. When the coverage is not too large, $1 - \theta \approx 1$, so $\theta^{1 + Q_{\mathrm{m}}/RT} = a_0p$,

$$
\theta = (a_0p)^{1/n}, \qquad n = 1 + \frac{Q_{\mathrm{m}}}{RT} > 1,
$$
which is the Freundlich equation. The larger $n$ is, the faster the heat of adsorption falls with coverage and the more nonuniform the surface. An equivalent statement is that the number of sites on the surface with heat of adsorption $Q$ decreases exponentially with $Q$.

If the heat of adsorption falls linearly with coverage, $Q_{\mathrm{a}}(\theta) = Q_0 - \alpha\theta$, taking logarithms,

$$
\ln\frac{\theta}{1 - \theta} = \ln\left(a_0p\,\mathrm{e}^{Q_0/RT}\right) - \frac{\alpha\theta}{RT}.
$$
At medium coverage the left-hand side $\ln[\theta/(1 - \theta)]$ changes very slowly ($\theta$ from 0.2 to 0.8 changes it by only about 2.8), while for $\alpha \gg RT$ both terms on the right are large, so approximately $\alpha\theta/RT \approx \ln(A_0p)$ with $A_0 = a_0\mathrm{e}^{Q_0/RT}$, which is the Temkin equation. The derivation uses "medium coverage", which is exactly its range of validity; 20.7.3 derives these two equations again from kinetics.

### 20.4.3. Adsorption from Solution

When a solid adsorbs a solute from solution (decolorization by activated carbon, wastewater treatment, liquid chromatography), the Langmuir, Freundlich and Temkin equations can still be used for fitting with pressure replaced by concentration, but the solvent is also adsorbed and competes with the solute for adsorption sites, so the process is more complicated than adsorption from the gas phase and there is no general theoretical formula. There are several qualitative rules:

1. Polar adsorbents (silica gel, alumina) preferentially adsorb polar components, and nonpolar adsorbents (activated carbon) preferentially adsorb nonpolar components;
2. The less soluble a solute, the more easily it is adsorbed (Traube's rule also holds for solid–liquid adsorption: the capacity of activated carbon to adsorb fatty acids from aqueous solution increases with chain length);
3. Adsorption is generally exothermic, and the amount adsorbed decreases with increasing temperature.

This is why silica gel rather than activated carbon is often placed in precision instruments as a desiccant: silica gel is a polar adsorbent and preferentially adsorbs the water in the air.

## 20.5. BET Multilayer Adsorption

### 20.5.1. Multilayer Adsorption

**Definition 20.5.1** Adsorption in which the adsorbate forms only one layer of molecules on the adsorbent surface is called **monolayer adsorption**; adsorption that continues on already adsorbed molecules to form multiple layers of molecules is called **multilayer adsorption**.

Chemisorption relies on bonding to the surface and can only be monolayer; physical adsorption relies on van der Waals forces, and adsorbed molecules can likewise attract gas molecules, so multilayers can form near the saturated vapor pressure. Brunauer, Emmett and Teller (1938) extended Langmuir's method to multilayers:

1. The Langmuir assumptions are kept: the surface is uniform and there is no lateral interaction between molecules in the same layer;
2. Adsorption can be multilayer; molecules of the first layer interact directly with the solid, with heat of adsorption $Q_1$; molecules of the second and higher layers interact with molecules of the same kind, and their heat of adsorption is equal to the molar enthalpy of liquefaction $Q_{\mathrm{L}}$ of the adsorbate;
3. Adsorption and desorption in each layer are in dynamic equilibrium, molecules in the $i$th layer can be adsorbed only where molecules of the $(i-1)$th layer are present; with infinitely many layers the outermost layer is in equilibrium with the saturated vapor.

### 20.5.2. The BET Equation

**Theorem 20.5.1 (BET Adsorption Isotherm)** Under the above assumptions, the amount adsorbed at relative pressure $x = p/p^*$ ($p^*$ is the saturated vapor pressure of the adsorbate at the adsorption temperature) is

$$
V^{\mathrm{a}} = \frac{V^{\mathrm{a}}_{\mathrm{mono}}\,c\,x}{(1 - x)[1 + (c - 1)x]}, \qquad c \approx \exp\frac{Q_1 - Q_{\mathrm{L}}}{RT}, \tag{20.3}
$$
where $V^{\mathrm{a}}_{\mathrm{mono}}$ is the monolayer saturation adsorption and $c$ (often written $c_{\mathrm{BET}}$) is the BET constant.

**Proof** Let $s_0$ be the area of the surface that is not covered and $s_i$ the area on which there are exactly $i$ layers of molecules ($i = 1, 2, \dots$). At equilibrium each $s_i$ does not change with time. Between $s_0$ and $s_1$: the rate of adsorption on the bare surface to form the first layer equals the rate of desorption of first-layer molecules,

$$
a_1ps_0 = b_1s_1\mathrm{e}^{-Q_1/RT}.
$$
Similarly, between $s_{i-1}$ and $s_i$, $a_ips_{i-1} = b_is_i\mathrm{e}^{-Q_{\mathrm{L}}/RT}$ ($i \ge 2$). By assumption 2 the properties of the second and higher layers are the same as those of the liquid, and $b_i/a_i = g$ is the same for all $i \ge 2$. Let

$$
y = \frac{a_1}{b_1}p\,\mathrm{e}^{Q_1/RT}, \qquad x = \frac{p}{g}\mathrm{e}^{Q_{\mathrm{L}}/RT}, \qquad c = \frac{y}{x},
$$
so that $s_1 = ys_0$ and $s_i = xs_{i-1} = x^{i-1}s_1 = cx^is_0$. The total area and total amount adsorbed ($v_0$ is the amount of one layer of molecules per unit area) are

$$
A_{\mathrm{s}} = s_0 + \sum_{i=1}^{\infty}s_i = s_0\left(1 + c\sum_{i=1}^{\infty}x^i\right), \qquad V^{\mathrm{a}} = v_0\sum_{i=1}^{\infty}is_i = v_0cs_0\sum_{i=1}^{\infty}ix^i.
$$
For $0 < x < 1$, using the sum of the **geometric series** $\sum_{i\ge1}x^i = x/(1 - x)$ and its termwise derivative $\sum_{i\ge1}ix^i = x/(1 - x)^2$ ([2.2.8](/2.2.8), [2.2.9](/2.2.9)),

$$
\frac{V^{\mathrm{a}}}{v_0A_{\mathrm{s}}} = \frac{cx/(1 - x)^2}{1 + cx/(1 - x)} = \frac{cx}{(1 - x)(1 - x + cx)},
$$
where $v_0A_{\mathrm{s}} = V^{\mathrm{a}}_{\mathrm{mono}}$. Finally we determine the meaning of $x$: as $x \to 1$, $V^{\mathrm{a}} \to \infty$, that is, the adsorbed layer becomes infinitely thick and the outermost layer is the flat surface of the liquid, which can happen only at $p = p^*$; and since $x$ is proportional to $p$, $x = p/p^*$. $c = (a_1b_2/(b_1a_2))\mathrm{e}^{(Q_1 - Q_{\mathrm{L}})/RT}$, and the preceding factor is usually approximated by 1. $\square$

![Left: BET isotherms for cBET = 0.5, 2, 10, 100 (in units of the monolayer saturation adsorption); for large c the curve has a pronounced knee near the monolayer (type II), and for c < 1 it is convex downward throughout (type III); the shaded band is the usual range of validity of BET, 0.05 < p/p* < 0.35. Right: BET linear plot of the N₂ data of Example 20.5.1 with the least-squares line](./plots/bet.py)

### 20.5.3. Determination of Specific Surface Area

Equation (20.3) can be rewritten in linear form

$$
\frac{x}{V^{\mathrm{a}}(1 - x)} = \frac{1}{V^{\mathrm{a}}_{\mathrm{mono}}c} + \frac{c - 1}{V^{\mathrm{a}}_{\mathrm{mono}}c}\,x.
$$
A plot of the left-hand side against $x$ is a straight line, with $V^{\mathrm{a}}_{\mathrm{mono}} = 1/(\text{slope} + \text{intercept})$ and $c = 1 + \text{slope}/\text{intercept}$. The BET equation generally holds only for $0.05 < x < 0.35$: at too low a relative pressure the nonuniformity of the surface is significant, at too high a pressure the assumptions of multilayer adsorption fail, and capillary condensation also occurs in fine pores. The larger $c$ is, the more marked is the knee of the isotherm near the monolayer ("point B"); $c$ for $\ce{N2}$ on most oxides and carbons lies between $50$ and $300$.

**Example 20.5.1** The amounts of $\ce{N2}$ adsorbed by a powder at 77 K (at standard conditions, per gram) are measured as follows; find its specific surface area.

| $x = p/p^*$ | 0.05 | 0.08 | 0.11 | 0.14 | 0.17 | 0.20 | 0.25 | 0.30 |
|---|---|---|---|---|---|---|---|---|
| $V^{\mathrm{a}}/(\mathrm{cm^3\,g^{-1}})$ | 22.38 | 24.00 | 26.05 | 27.29 | 28.64 | 30.01 | 31.97 | 34.85 |

**Solution** Perform a linear **least squares** fit with the linear form of BET:

```python
import numpy as np

# N2 at 77 K: relative pressure x = p/p* and adsorbed volume (cm^3 STP per g)
x = np.array([0.05, 0.08, 0.11, 0.14, 0.17, 0.20, 0.25, 0.30])
V = np.array([22.38, 24.00, 26.05, 27.29, 28.64, 30.01, 31.97, 34.85])

y = x / (V * (1 - x))                     # linear BET form
slope, intercept = np.polyfit(x, y, 1)
V_mono = 1 / (slope + intercept)          # monolayer capacity, cm^3 STP per g
c = 1 + slope / intercept

NA, sigma = 6.02214076e23, 0.162e-18      # molecules per mol; N2 cross-section in m^2
a_s = V_mono * 1e-3 / 22.414 * NA * sigma # specific surface area, m^2 per g
print(f"V_mono = {V_mono:.2f} cm3/g, c = {c:.0f}, a_s = {a_s:.0f} m2/g")
```

```text
V_mono = 24.85 cm3/g, c = 104, a_s = 108 m2/g
```

The specific surface area is about $108\,\mathrm{m^2\,g^{-1}}$. A positive $c = 104$ indicates that the chosen pressure range is reasonable (a negative $c$ indicates that the data points lie outside the range of validity of BET, which is common for microporous materials).

When the number of adsorbed layers is limited (for example in a narrow pore at most $n$ layers can be adsorbed), truncating the above sum to $n$ terms gives the three-constant BET equation:

$$
V^{\mathrm{a}} = \frac{V^{\mathrm{a}}_{\mathrm{mono}}\,cx}{1 - x}\cdot\frac{1 - (n + 1)x^n + nx^{n+1}}{1 + (c - 1)x - cx^{n+1}}.
$$
For $n = 1$ the common factor $(1 - x)^2$ of numerator and denominator cancels, giving $V^{\mathrm{a}} = V^{\mathrm{a}}_{\mathrm{mono}}cx/(1 + cx)$, the Langmuir equation ($ap = cx$); for $n \to \infty$, $x^n \to 0$ and Eq. (20.3) is recovered.

The assumptions of the BET theory have obvious defects: the surface is nonuniform, molecules in the same layer interact, and the heat of adsorption of the second layer is not exactly equal to the enthalpy of liquefaction. It is successful because in the range $0.05$–$0.35$ these errors cancel, and the monolayer capacity obtained agrees fairly well with other methods. The BET method is still the method for determining specific surface area prescribed by the international standard (ISO 9277).

## 20.6. Adsorption on Porous Solids

### 20.6.1. Classification of Pores and Types of Adsorption Isotherms

Adsorbents and catalysts are mostly porous, and the specific surface area comes mainly from the pore walls. IUPAC classifies pores into three classes by pore width (the diameter of a cylindrical pore or the distance between the walls of a slit pore).

**Definition 20.6.1** Pores of width less than $2\,\mathrm{nm}$ are called **micropores**, those of $2$–$50\,\mathrm{nm}$ **mesopores**, and those larger than $50\,\mathrm{nm}$ **macropores**.

In micropores the potential fields of opposite walls overlap, adsorption occurs at very low relative pressure, and it is "pore filling" rather than layer-by-layer adsorption; in mesopores multilayer adsorption occurs first, followed by capillary condensation; adsorption in macropores is similar to that on a flat surface. According to the 2015 IUPAC technical report (Thommes et al.), physical adsorption isotherms are classified into six types (the old five BDDT types plus the stepped type VI, with types I and IV each divided into a and b):

| Type | Shape | Corresponding systems |
|---|---|---|
| I(a), I(b) | Rises steeply at low pressure and soon reaches a plateau | Microporous solids (activated carbon, molecular sieves, MOFs); I(a) has very narrow pores (< about 1 nm), I(b) wider pores including narrow mesopores (< about 2.5 nm). The plateau corresponds to the micropores being filled, not to a completed monolayer |
| II | Knee B at low pressure (monolayer completed), followed by unrestricted growth of multilayer adsorption | Nonporous or macroporous solids; the typical object of the BET method |
| III | Convex downward throughout, no point B | Very weak adsorbent–adsorbate interaction ($c < 1$), such as water on polyethylene |
| IV(a), IV(b) | First part as in type II, steep rise at medium pressure because of capillary condensation, finally a plateau | Mesoporous solids (silica gel, mesoporous silica); IV(a) has a hysteresis loop (for $\ce{N2}$ at 77 K, pore widths above about 4 nm), IV(b) is reversible (narrower mesopores) |
| V | Low-pressure part as in type III, followed by pore filling with hysteresis | Microporous or mesoporous solids with weak interaction, such as water on hydrophobic activated carbon |
| VI | Stepped, each step corresponding to one layer | Layer-by-layer adsorption on highly uniform nonporous surfaces, such as Kr on graphitized carbon black at low temperature |

The old classification described type II as "pores of unequal sizes with capillary condensation" and type I as "micropores below 2.5 nm", both inaccurate: type II corresponds to nonporous or macroporous solids, capillary condensation corresponds to types IV and V, and the upper limit of micropores is 2 nm.

![Schematic of the six types of physical adsorption isotherms of the 2015 IUPAC classification (amount adsorbed against relative pressure): I(a), I(b) for micropores; II for nonporous or macroporous solids, with point B marking the completion of the monolayer; III for weak interaction; IV(a) (with a hysteresis loop, the dashed line being the desorption branch) and reversible IV(b) for mesopores; V for weak interaction plus pore filling; VI for layer-by-layer adsorption on uniform surfaces](./plots/iupac-isotherms.py)

### 20.6.2. Capillary Condensation and Adsorption Hysteresis

When the adsorbate wets the pore wall, the liquid surface in the pore is concave, and by the Kelvin equation the equilibrium vapor pressure over a concave surface is lower than over a flat surface.

**Definition 20.6.2** The phenomenon in a porous solid in which a vapor condenses into liquid in the pores below its saturated vapor pressure is called **capillary condensation**.

Let the liquid surface in the pore be a hemispherical concave surface of radius $r_{\mathrm{K}}$ (the Kelvin radius) with contact angle $\theta_{\mathrm{c}}$; the relative pressure at which condensation occurs is then

$$
\ln\frac{p}{p^*} = -\frac{2\gamma V_{\mathrm{m}}\cos\theta_{\mathrm{c}}}{RTr_{\mathrm{K}}}.
$$

The finer the pore, the lower the relative pressure needed for condensation. Capillary condensation makes the type IV and V isotherms rise steeply at medium pressure, and once the pores are filled with liquid the amount adsorbed no longer increases and a plateau appears.

**Definition 20.6.3** The phenomenon in which, over a certain range of relative pressure, the desorption isotherm does not coincide with the adsorption isotherm and the desorption branch lies above the adsorption branch is called **adsorption hysteresis**, and the region enclosed by the two branches is called the hysteresis loop.

The main causes of hysteresis are:

- The meniscus has a different shape in condensation and in evaporation: in adsorption a liquid film first forms on the wall of a cylindrical pore and the liquid surface is a cylindrical surface (with only one radius of curvature, $\Delta p = \gamma/r$), so condensation occurs only at a higher pressure; in desorption the pore mouth carries a hemispherical meniscus ($2\gamma/r$) and evaporation starts only at a lower pressure.
- Ink-bottle pores: the pore cavity is large and the mouth small; in adsorption the cavity condenses at a higher pressure according to its larger radius, and in desorption the liquid in the cavity can leave only after the small meniscus at the mouth has evaporated (pore blocking), so desorption is delayed to a lower pressure; the connectivity of a pore network has the same effect. When the pore mouth is smaller than a certain size, the liquid in the cavity cavitates directly under excessive tension, and the desorption branch of $\ce{N2}$ at 77 K therefore drops steeply and closes near $p/p^* \approx 0.42$.
- Contact angle hysteresis: the liquid advances in adsorption and recedes in desorption, and the advancing angle is larger than the receding angle.

In 2015 IUPAC divided hysteresis loops into six types, H1, H2(a), H2(b), H3, H4 and H5: the H1 loop is narrow and steep with the two branches nearly parallel, corresponding to cylindrical mesopores of uniform size (such as MCM-41 and SBA-15 synthesized by templating); in H2 the desorption branch is very steep, corresponding to pore blocking and cavitation in ink-bottle pores or pore networks, with (a) and (b) corresponding to narrow and wide distributions of pore-mouth sizes respectively; H3 has no plateau in the high-pressure region and is common for slit pores formed by the packing of plate-like particles and for macropores that are not completely filled; H4 is similar to H3 but has the steep rise of type I at low pressure, and is found in materials combining micropores and mesopores (certain activated carbons and molecular sieves); H5 is rare and corresponds to a structure of open and closed mesopores with partially blocked pore mouths.

### 20.6.3. Pore Size Distribution

**Definition 20.6.4** The distribution $\mathrm{d}V_{\mathrm{p}}/\mathrm{d}r_{\mathrm{p}}$ of the pore volume (or pore surface area) of a porous solid over pore size is called the **pore size distribution**.

The pore size distribution of mesopores is found from the adsorption (or desorption) isotherm on the basis of capillary condensation and the Kelvin equation: each relative pressure corresponds to a Kelvin radius, and the increase in the amount adsorbed when the pressure rises from $p_1$ to $p_2$ is the volume of liquid needed to fill the pores with radius between $r_{\mathrm{K}}(p_1)$ and $r_{\mathrm{K}}(p_2)$. But before condensation occurs a multilayer film of thickness $t$ has already been adsorbed on the pore wall, the Kelvin radius is only the radius of the remaining "core", and the true pore radius is

$$
r_{\mathrm{p}} = r_{\mathrm{K}} + t.
$$
The variation of $t$ with relative pressure (the $t$-curve) is obtained from the isotherm of a nonporous reference material or from an empirical formula (such as the Harkins–Jura formula $t/\mathrm{nm} = 0.1\,[13.99/(0.034 - \lg x)]^{1/2}$). Barrett, Joyner and Halenda (1951) used this to compute the pore size distribution step by step, which is called the BJH method.

**Example 20.6.1** For liquid nitrogen at 77 K, $\gamma = 8.85\,\mathrm{mN\,m^{-1}}$, $V_{\mathrm{m}} = 34.7\,\mathrm{cm^3\,mol^{-1}}$ and $\theta_{\mathrm{c}} = 0$. At $x = 0.70$ on the desorption branch, $r_{\mathrm{K}} = 2\gamma V_{\mathrm{m}}/(RT\ln(1/x)) = 0.959\,\mathrm{nm}/0.357 = 2.7\,\mathrm{nm}$; the Harkins–Jura formula gives $t = 0.86\,\mathrm{nm}$, so $r_{\mathrm{p}} = 3.5\,\mathrm{nm}$, that is, at this pressure mesopores of diameter about $7\,\mathrm{nm}$ are emptied.

The Kelvin equation treats the liquid as a continuum, and for pore sizes below about $4\,\mathrm{nm}$ the BJH method underestimates the pore size (by as much as 20%–30%); capillary condensation does not occur in micropores, and these cases are now handled by fitting isotherms obtained from molecular simulation with density functional theory (DFT).

## 20.7. Kinetics of Chemisorption

### 20.7.1. Collision Flux and Sticking Coefficient

Chemisorption, like a chemical reaction, requires a molecule to hit a vacant active site on the surface, and often requires crossing an energy barrier (20.2.3). The number of molecules colliding with unit area per unit time is the **effusion** flux ([5.2.1](/5.2.1)):

$$
Z_{\mathrm{W}} = \frac{p}{\sqrt{2\pi mk_{\mathrm{B}}T}}.
$$

**Definition 20.7.1** The fraction of the molecules hitting the surface that are adsorbed, $s = r_{\mathrm{a}}/Z_{\mathrm{W}}$, is called the **sticking coefficient**, $0 \le s \le 1$. It depends on the coverage, and its value as $\theta \to 0$ is denoted $s_0$.

The rate of adsorption is thus $r_{\mathrm{a}} = sZ_{\mathrm{W}}$, generally written

$$
r_{\mathrm{a}} = \frac{p}{\sqrt{2\pi mk_{\mathrm{B}}T}}\,\sigma f(\theta)\exp\left(-\frac{E_{\mathrm{a}}(\theta)}{RT}\right),
$$
where $f(\theta)$ is the probability of hitting a vacant site, $\sigma$ is the condensation coefficient (a steric factor) and $E_{\mathrm{a}}(\theta)$ is the activation energy of adsorption. The rate of desorption is $r_{\mathrm{d}} = K f'(\theta)\exp(-E_{\mathrm{d}}(\theta)/RT)$, with $E_{\mathrm{d}}$ the activation energy of desorption, and the difference $E_{\mathrm{d}} - E_{\mathrm{a}}$ of the two is the heat of adsorption.

**Example 20.7.1** For $\ce{N2}$ ($m = 4.65 \times 10^{-26}\,\mathrm{kg}$) at 300 K and $1\,\mathrm{Pa}$, $Z_{\mathrm{W}} = 1/\sqrt{2\pi \times 4.65 \times 10^{-26} \times 1.381 \times 10^{-23} \times 300}\,\mathrm{m^{-2}\,s^{-1}} = 2.9 \times 10^{22}\,\mathrm{m^{-2}\,s^{-1}}$. A monolayer contains about $10^{19}$ adsorption sites per square meter, so if $s = 1$ a layer is completed in about $3\,\mathrm{s}$ at $10^{-4}\,\mathrm{Pa}$. Experiments on clean surfaces must therefore be carried out in ultrahigh vacuum of the order of $10^{-8}\,\mathrm{Pa}$ for the surface to stay clean for several hours. The dissociative sticking coefficient of $\ce{N2}$ on the Fe(111) face is only about $10^{-6}$, and this step is the rate-determining step of ammonia synthesis (20.8.5).

### 20.7.2. The Ideal Adsorbed Layer

When the surface is uniform, the heat of adsorption is the same at all sites and there is no interaction between adsorbed molecules, one speaks of an ideal adsorbed layer. Then $E_{\mathrm{a}}$ and $E_{\mathrm{d}}$ are independent of coverage, $f(\theta) = 1 - \theta$ and $f'(\theta) = \theta$,

$$
\frac{\mathrm{d}\theta}{\mathrm{d}t} = k_{\mathrm{a}}p(1 - \theta) - k_{\mathrm{d}}\theta, \qquad k_{\mathrm{a}} = \frac{\sigma\,\mathrm{e}^{-E_{\mathrm{a}}/RT}}{n_{\mathrm{s}}\sqrt{2\pi mk_{\mathrm{B}}T}}, \quad k_{\mathrm{d}} = \frac{K\mathrm{e}^{-E_{\mathrm{d}}/RT}}{n_{\mathrm{s}}}
$$
($n_{\mathrm{s}}$ is the number of adsorption sites per unit area). This is a first-order linear ordinary differential equation, in which $\theta$ approaches its equilibrium value exponentially with rate constant $k_{\mathrm{a}}p + k_{\mathrm{d}}$; setting $\mathrm{d}\theta/\mathrm{d}t = 0$ returns the Langmuir equation with $a = k_{\mathrm{a}}/k_{\mathrm{d}}$.

### 20.7.3. Real Adsorbed Layers and the Elovich Equation

In a real adsorbed layer the molecules first occupy the energetically most favorable positions (smallest activation energy of adsorption, largest heat of adsorption); as the coverage increases, the activation energy of adsorption rises, that of desorption falls and the heat of adsorption decreases. Suppose both vary linearly with coverage:

$$
E_{\mathrm{a}} = E_{\mathrm{a}}^0 + \alpha\theta, \qquad E_{\mathrm{d}} = E_{\mathrm{d}}^0 - \beta\theta, \qquad Q_{\mathrm{a}} = E_{\mathrm{d}} - E_{\mathrm{a}} = Q_0 - (\alpha + \beta)\theta.
$$
When the coverage changes, the change of the exponential factors is much larger than that of $f(\theta)$, and $f(\theta)$ and $f'(\theta)$ can be treated as constants absorbed into the rate constants:

**Formula 20.7.1 (Elovich Equation)**

$$
\frac{\mathrm{d}\theta}{\mathrm{d}t} = k_{\mathrm{a}}p\exp\left(-\frac{\alpha\theta}{RT}\right) - k_{\mathrm{d}}\exp\left(\frac{\beta\theta}{RT}\right).
$$

Far from equilibrium, where desorption can be neglected, integration gives $\theta = \frac{RT}{\alpha}\ln\left(1 + \frac{\alpha k_{\mathrm{a}}p}{RT}t\right)$: the amount adsorbed grows logarithmically with time, and many chemisorptions (such as $\ce{H2}$ and $\ce{CO}$ on oxides) have this "fast at first, then slower and slower" character. Setting $\mathrm{d}\theta/\mathrm{d}t = 0$,

$$
\frac{(\alpha + \beta)\theta}{RT} = \ln\frac{k_{\mathrm{a}}p}{k_{\mathrm{d}}}, \qquad \theta = \frac{RT}{\alpha + \beta}\ln(A_0p),
$$
which is the Temkin equation (Formula 20.4.2, in which the $\alpha$ corresponds to the $\alpha + \beta$ here). If the activation energies are linear in $\ln\theta$, $E_{\mathrm{a}} = E_{\mathrm{a}}^0 + \alpha\ln\theta$ and $E_{\mathrm{d}} = E_{\mathrm{d}}^0 - \beta\ln\theta$, the same steps give $\theta^{(\alpha + \beta)/RT} = (k_{\mathrm{a}}/k_{\mathrm{d}})p$, the Freundlich equation with $n = (\alpha + \beta)/RT$. Kinetics and the equilibrium derivation of 20.4.2 give the same conclusion: the Langmuir, Temkin and Freundlich equations correspond to a heat of adsorption that is constant, decreases linearly with coverage, and decreases logarithmically with coverage, respectively.

## 20.8. Gas–Solid Catalytic Reactions

### 20.8.1. Heterogeneous Catalysis and Performance Indicators of Catalysts

**Definition 20.8.1 (Heterogeneous Catalysis)** A catalytic reaction in which the catalyst and the reactants are in different phases is called **heterogeneous catalysis**; the most important case is gas-phase or liquid-phase reactions on solid catalysts.

About 80% of the processes in the chemical industry use catalysts, most of them heterogeneous: ammonia and methanol synthesis, catalytic cracking and reforming of petroleum, the oxidation of $\ce{SO2}$ in the sulfuric acid industry, and the three-way catalytic conversion of automobile exhaust. A catalyst speeds up a reaction by providing a pathway of lower activation energy ([6.1.7](/6.1.7#sec-7.3.4)): for example the activation energy of ammonia synthesis falls from $334.7\,\mathrm{kJ\,mol^{-1}}$ to $167.4\,\mathrm{kJ\,mol^{-1}}$ on the $\ce{Fe-Al2O3-K2O}$ catalyst; for more examples see the table in [6.3.17](/6.3.17#sec-17.3.2).

**Definition 20.8.2** The main criteria for evaluating a solid catalyst are:

1. **Catalytic activity**: the ability of the catalyst to speed up the reaction, often expressed as the amount of product formed per unit time per unit mass (or volume, or surface area) of catalyst, $a = m_{\mathrm{p}}/(m_{\mathrm{c}}t)$;
2. Conversion and selectivity (for selectivity see Definition 17.3.1): conversion is the fraction of the reactant fed that has been converted, and selectivity is the fraction of the converted reactant that forms the desired product;
3. Stability and lifetime: the decay of activity with time of use, as well as resistance to poisoning, heat resistance and mechanical strength.

There is also a molecular-level measure of activity independent of the amount of catalyst.

**Definition 20.8.3** The number of molecules converted (or of product molecules formed) per catalytic active site per unit time is called the **turnover frequency** (TOF), with unit $\mathrm{s^{-1}}$.

The TOF makes it possible to compare the same catalyst at different dispersions; it has the same meaning as the **catalytic constant** $k_{\mathrm{cat}}$ of enzymes ([6.3.17](/6.3.17)). The TOF of heterogeneous catalysts is generally $10^{-2}$–$10^2\,\mathrm{s^{-1}}$, and that of enzymes can be as high as $10^6\,\mathrm{s^{-1}}$. In industrial reactors the throughput is also often expressed by the *space velocity*: the volume of reaction gas (converted to standard conditions) passing through unit volume of catalyst per unit time, with unit $\mathrm{h^{-1}}$; its reciprocal is the contact time between reactants and catalyst.

### 20.8.2. Adsorptive Activation and Active Sites

A solid catalyst activates the reactants by chemisorption. The molecular structure changes after adsorption: after $\ce{N2}$ is adsorbed on Fe the N≡N bond is weakened and lengthened and finally dissociates; $\ce{H2}$ dissociates into H atoms on Pt and Ni. That a molecule becomes more reactive through adsorption is called adsorptive activation.

**Definition 20.8.4** The atoms, ions or atomic clusters on a catalyst surface at which the reactants can be activated by adsorption are called **active sites**.

Active sites often make up only a small part of the surface (step and corner atoms, defects, particular bimetallic sites), so the catalytic activity is highly sensitive to the method of catalyst preparation, particle size and impurities. The adsorption of reactants on a catalyst requires a large adsorption rate and a moderate adsorption strength: if adsorption is too weak the reactants are not activated; if it is too strong, intermediates or products occupy the surface and cannot desorb, and the active sites are poisoned. Plotting activity against the adsorption energy of the reactant (or of a key intermediate) gives a "volcano curve" that first rises and then falls, with the catalyst at the peak having a moderate adsorption strength; this is the *Sabatier principle*. For example the activity of ammonia synthesis is highest near Ru and Os (moderate adsorption strength of N), followed by Fe; in the volcano curve of the exchange current density of hydrogen evolution against the metal–H bond energy the platinum-group metals are at the peak ([6.3.14](/6.3.14)). Modern computational chemistry calculates adsorption energies by density functional theory and screens new catalysts on the volcano curve.

Other factors affecting catalyst activity include: the reaction temperature (chemisorption is significant only in a certain temperature range); the dispersion, that is, the fraction of the atoms of a particle that are surface atoms (about 80% of the atoms of a Pt particle of diameter $1\,\mathrm{nm}$ are at the surface, and about 20% at $5\,\mathrm{nm}$), so noble-metal catalysts are usually made as nanoparticles supported on oxides or carbon, the limiting case being atomically dispersed "single-atom catalysts"; impurities and promoters; and the bulk structure, surface composition and pore structure determined by the method of preparation.

### 20.8.3. Reaction Steps and the Controlling Step

A gas–solid catalytic reaction generally comprises five steps:

1. The reactants diffuse from the gas stream to the catalyst surface (including diffusion inside the pores);
2. The reactants are chemisorbed on the surface;
3. The adsorbed species react on the surface;
4. The products desorb from the surface;
5. The products diffuse from the surface into the gas stream.

Steps 1 and 5 are physical mass-transfer processes and steps 2–4 are surface chemical processes. If mass transfer is the slowest, the reaction is in the diffusion-controlled regime and the overall rate is insensitive to temperature (the apparent activation energy is only a few $\mathrm{kJ\,mol^{-1}}$ of diffusion), and increasing the gas velocity or reducing the particle size can speed up the reaction; if the surface process is the slowest, the reaction is in the kinetically controlled regime and the rate is determined by the **rate-determining step** of the surface reaction. For the same reaction the Arrhenius plot often passes from kinetic control to diffusion control in the high-temperature region, with a markedly smaller slope. In what follows we discuss only kinetic control with the surface reaction as the rate-determining step: adsorption and desorption quickly reach equilibrium, and the coverage is given by the Langmuir equation (this is the **pre-equilibrium approximation** applied to the surface).

**Catalyst poisoning** is the phenomenon in which a small amount of a substance markedly lowers or destroys the activity of a catalyst ([6.1.7](/6.1.7#sec-7.3.4)). Poisons are substances that adsorb extremely strongly on the active sites: physical adsorption or weaker chemisorption causes temporary poisoning, and the activity can be restored after the poison is removed; strong chemisorption causes permanent poisoning. For example, in the oxidation of ammonia on a Pt–Rh gauze ($\ce{4NH3 + 5O2 -> 4NO + 6H2O}$, about $1273\,\mathrm{K}$), a volume fraction of only $10^{-7}$ of $\ce{PH3}$ in the feed gas deactivates the catalyst almost completely; sulfur compounds poison the iron catalyst of ammonia synthesis and lead and sulfur poison the three-way catalyst of automobile exhaust, so the feed must be desulfurized and gasoline must be lead-free. This can be understood from competitive adsorption (20.3.3): the $a_{\mathrm{P}}$ of a poison is very large, and even at an extremely small partial pressure $a_{\mathrm{P}}p_{\mathrm{P}}$ is far larger than $a_{\mathrm{A}}p_{\mathrm{A}}$ of the reactant.

### 20.8.4. Unimolecular Surface Reactions

Let the surface reaction $\mathrm{A}^\ast \to \mathrm{B}^\ast$ be the rate-determining step with rapid desorption of the product, $r = k_2\theta_{\mathrm{A}}$. The adsorption of A obeys the Langmuir equation,

$$
r = \frac{k_2a_{\mathrm{A}}p_{\mathrm{A}}}{1 + a_{\mathrm{A}}p_{\mathrm{A}}}.
$$

- At very low pressure or very weak adsorption ($a_{\mathrm{A}}p_{\mathrm{A}} \ll 1$), $r = k_2a_{\mathrm{A}}p_{\mathrm{A}}$ and the reaction behaves as a **first-order reaction**, as in the decomposition of $\ce{PH3}$ on W.
- At very high pressure or very strong adsorption ($a_{\mathrm{A}}p_{\mathrm{A}} \gg 1$), the surface is saturated, $r = k_2$, and the reaction behaves as a **zero-order reaction**, $p_{\mathrm{A}} = p_{\mathrm{A},0} - k_2t$, as in the decomposition of $\ce{NH3}$ on W and of $\ce{HI}$ on Au.
- At intermediate pressure the order lies between 0 and 1.
- When the product B is also adsorbed and desorbs with difficulty, $r = k_2a_{\mathrm{A}}p_{\mathrm{A}}/(1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}})$, the product acts as a poison and the reaction is inhibited. When B is adsorbed very strongly, $r \approx k_2a_{\mathrm{A}}p_{\mathrm{A}}/(a_{\mathrm{B}}p_{\mathrm{B}})$, as in the decomposition of $\ce{NH3}$ on Pt, $r = kp(\ce{NH3})/p(\ce{H2})$.

The order changes with pressure, and so does the apparent activation energy. At low coverage $r = k_2a_{\mathrm{A}}p_{\mathrm{A}}$ with $k_2 \propto \mathrm{e}^{-E_2/RT}$ and $a_{\mathrm{A}} \propto \mathrm{e}^{-\Delta_{\mathrm{ads}}H_{\mathrm{m}}/RT}$, so the **apparent activation energy** is $E_{\mathrm{app}} = E_2 + \Delta_{\mathrm{ads}}H_{\mathrm{m}}$, smaller than the true activation energy of the surface reaction by the heat of adsorption; at high coverage $E_{\mathrm{app}} = E_2$. The larger the heat of adsorption and the more the reactant is "stored" on the surface, the lower the apparent activation energy, which is another way in which a catalyst lowers the activation energy.

### 20.8.5. Bimolecular Surface Reactions

There are two basic mechanisms for a surface reaction of two reactants A and B.

**Definition 20.8.5** The mechanism in which both A and B are adsorbed and the reaction takes place between two adsorbed species at adjacent positions on the surface is called the **Langmuir–Hinshelwood mechanism** (L–H mechanism); the mechanism in which only A is adsorbed and the adsorbed A reacts directly with a B molecule in the gas phase (or physically adsorbed) is called the **Eley–Rideal mechanism** (E–R mechanism).

For the L–H mechanism, $r = k_2\theta_{\mathrm{A}}\theta_{\mathrm{B}}$, with A and B adsorbing competitively,

$$
r = \frac{k_2a_{\mathrm{A}}a_{\mathrm{B}}p_{\mathrm{A}}p_{\mathrm{B}}}{(1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}})^2}.
$$
Keeping $p_{\mathrm{B}}$ constant and increasing $p_{\mathrm{A}}$, the rate first increases and then decreases, with a maximum at $a_{\mathrm{A}}p_{\mathrm{A}} = 1 + a_{\mathrm{B}}p_{\mathrm{B}}$: too much A displaces B from the surface. For the E–R mechanism, $r = k_2\theta_{\mathrm{A}}p_{\mathrm{B}}$,

$$
r = \frac{k_2a_{\mathrm{A}}p_{\mathrm{A}}p_{\mathrm{B}}}{1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}}}
$$
(the $a_{\mathrm{B}}p_{\mathrm{B}}$ term in the denominator arises from nonreactive adsorption of B on the surface, and is dropped if B is not adsorbed). When $p_{\mathrm{A}}$ is increased the rate increases monotonically and tends to the limiting value $k_2p_{\mathrm{B}}$. For very weak adsorption of A, $r \approx k_2a_{\mathrm{A}}p_{\mathrm{A}}p_{\mathrm{B}}$, and for very strong adsorption $r \approx k_2p_{\mathrm{B}}$. Therefore, if the curve of rate against the partial pressure of one reactant shows a maximum, the mechanism can be taken to be L–H.

![Left: rate of a unimolecular surface reaction, r = kap/(1 + ap), first order at low pressure and zero order at high pressure. Right: rate of a bimolecular surface reaction as a function of pA at fixed pB (each normalized to its maximum): the rate of the Langmuir–Hinshelwood mechanism has a maximum at aApA = 1 + aBpB, while that of the Eley–Rideal mechanism rises monotonically to a plateau](./plots/surface-kinetics.py)

Most heterogeneous catalytic reactions proceed by the L–H mechanism, for example the oxidation of CO on Pt ($\ce{2CO + O2 -> 2CO2}$, with dissociative adsorption of O): when the partial pressure of CO is too high it covers the surface, $\ce{O2}$ cannot adsorb dissociatively and the rate falls instead, which is what happens during the cold start of an automobile catalytic converter. A true E–R mechanism is rare and is seen mostly in the reactions of highly active atoms or radicals with an adsorbed layer, such as a gas-phase H atom directly abstracting an adsorbed H atom on a Cu surface to form $\ce{H2}$.

Ammonia synthesis is the best understood heterogeneous catalytic reaction. Ertl determined its elementary steps on iron surfaces by the methods of surface science in ultrahigh vacuum:

$$
\begin{aligned}
&\mathrm{N_2(g)} + \ast \rightleftharpoons \mathrm{N_2}^\ast, \qquad \mathrm{N_2}^\ast + \ast \to 2\mathrm{N}^\ast\ (\text{rate-determining step}), \qquad \mathrm{H_2(g)} + 2\ast \rightleftharpoons 2\mathrm{H}^\ast, \\
&\mathrm{N}^\ast + \mathrm{H}^\ast \rightleftharpoons \mathrm{NH}^\ast + \ast, \qquad \mathrm{NH}^\ast + \mathrm{H}^\ast \rightleftharpoons \mathrm{NH_2}^\ast + \ast, \\
&\mathrm{NH_2}^\ast + \mathrm{H}^\ast \rightleftharpoons \mathrm{NH_3}^\ast + \ast, \qquad \mathrm{NH_3}^\ast \rightleftharpoons \mathrm{NH_3(g)} + \ast.
\end{aligned}
$$
The slowest step is the dissociative adsorption of $\ce{N2}$ (sticking coefficient about $10^{-6}$, 20.7.1), and the potassium promoter increases the electron density at the surface and promotes the dissociation of $\ce{N2}$. He measured the energy of every step, drew the complete energy diagram, and on this basis reproduced quantitatively the yield of industrial reactors; for this work he received the 2007 Nobel Prize in Chemistry.

## Summary

| Topic | Key points |
|---|---|
| Thermodynamics of adsorption | $\Delta S < 0$, $\Delta G < 0 \Rightarrow \Delta H < 0$; isosteric heat of adsorption $(\partial\ln p/\partial T)_{n^{\mathrm{a}}} = -\Delta_{\mathrm{ads}}H_{\mathrm{m}}/(RT^2)$ |
| Physical and chemical adsorption | van der Waals forces, heat of adsorption a few to tens of $\mathrm{kJ\,mol^{-1}}$, multilayer, nonselective; chemical bonds, heat of adsorption generally $> 40\,\mathrm{kJ\,mol^{-1}}$, monolayer, selective, often activated |
| Langmuir equation | Monolayer, uniform surface, no interaction; $\theta = ap/(1 + ap)$; dissociative adsorption $\theta/(1 - \theta) = (ap)^{1/2}$; competitive adsorption $\theta_{\mathrm{B}} = a_{\mathrm{B}}p_{\mathrm{B}}/(1 + \sum a_{\mathrm{C}}p_{\mathrm{C}})$ |
| Freundlich and Temkin equations | $n^{\mathrm{a}}/m = kp^{1/n}$ (heat of adsorption falls logarithmically); $\theta = (RT/\alpha)\ln(A_0p)$ (falls linearly, medium coverage) |
| BET equation | $V^{\mathrm{a}} = V^{\mathrm{a}}_{\mathrm{mono}}cx/[(1 - x)(1 - x + cx)]$, $x = p/p^*$; valid for $0.05 < x < 0.35$; cross-sectional area of $\ce{N2}$ $0.162\,\mathrm{nm^2}$ |
| Porous solids | Micropores < 2 nm, mesopores 2–50 nm, macropores > 50 nm; six IUPAC isotherm types; capillary condensation $\ln(p/p^*) = -2\gamma V_{\mathrm{m}}\cos\theta_{\mathrm{c}}/(RTr_{\mathrm{K}})$; $r_{\mathrm{p}} = r_{\mathrm{K}} + t$ |
| Kinetics of adsorption | $Z_{\mathrm{W}} = p/\sqrt{2\pi mk_{\mathrm{B}}T}$; sticking coefficient; Elovich equation $\mathrm{d}\theta/\mathrm{d}t = k_{\mathrm{a}}p\,\mathrm{e}^{-\alpha\theta/RT} - k_{\mathrm{d}}\mathrm{e}^{\beta\theta/RT}$ |
| Catalysts | Activity, selectivity, stability, TOF, space velocity; Sabatier principle and the volcano curve; poisoning is strong competitive adsorption of the poison |
| Kinetics of surface reactions | Unimolecular $r = k_2ap/(1 + ap)$ (first order → zero order); L–H $r = k_2a_{\mathrm{A}}a_{\mathrm{B}}p_{\mathrm{A}}p_{\mathrm{B}}/(1 + a_{\mathrm{A}}p_{\mathrm{A}} + a_{\mathrm{B}}p_{\mathrm{B}})^2$ has a maximum; E–R tends monotonically to saturation |

## Questions

1. Which of the following statements agree with the basic assumptions of the Langmuir adsorption theory: (A) the solid surface is uniform and all sites have the same adsorption capacity; (B) adsorption can be monolayer or multilayer; (C) adsorbed molecules interact with one another; (D) adsorption equilibrium is a dynamic equilibrium?

   A and D. The Langmuir theory assumes monolayer adsorption without interaction between adsorbed molecules, so their probability of desorption is not affected by the surrounding molecules.
2. The adsorption of oxygen on a solid surface proceeds very slowly at 400 K and still more slowly at 350 K. Is this mainly physical or chemical adsorption?

   Chemical adsorption. Physical adsorption needs almost no activation energy and is fast and insensitive to temperature; adsorption that is slow and speeds up as the temperature rises shows that an activation energy is needed.
3. Why does the BET method for measuring specific surface area use $\ce{N2}$ as adsorbate at the temperature of liquid nitrogen rather than at room temperature?

   Room temperature is far above the critical temperature of $\ce{N2}$, the amount of physical adsorption is extremely small and no multilayer can form; at the boiling point of $\ce{N2}$ (77 K), $p/p^*$ can be varied between 0 and 1, physical adsorption is significant, and $\ce{N2}$ is not chemisorbed.
4. Explain from competitive adsorption why a reaction following the L–H mechanism often has a reactant ratio at which the rate is maximal.

   The two reactants compete for the same active sites, and the rate is proportional to $\theta_{\mathrm{A}}\theta_{\mathrm{B}}$; too much of either displaces the other from the surface, and at fixed $p_{\mathrm{B}}$ the product $\theta_{\mathrm{A}}\theta_{\mathrm{B}}$ is largest at $a_{\mathrm{A}}p_{\mathrm{A}} = 1 + a_{\mathrm{B}}p_{\mathrm{B}}$ (where $\theta_{\mathrm{A}} = 1/2$).
