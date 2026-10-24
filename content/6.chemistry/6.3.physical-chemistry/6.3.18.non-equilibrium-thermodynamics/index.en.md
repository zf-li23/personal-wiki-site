---
title: Nonequilibrium Thermodynamics
description: Entropy flow and entropy production, local equilibrium and the entropy balance equation; phenomenological relations in the linear region, Onsager reciprocal relations, cross effects, membrane transport and active transport, the principle of minimum entropy production; dissipative structures far from equilibrium, Brusselator oscillation and Hopf bifurcation, the BZ reaction, Turing patterns; negative entropy flow in living systems.
source_hash: 49ccdb1e4fc3
---

The thermodynamics of the preceding chapters deals only with equilibrium states and with reversible processes that connect them: for irreversible processes it gives only the direction ($\Delta S_{\text{isolated}} > 0$, $\Delta G < 0$) and does not answer "how fast" or "how coupled". Yet almost all the striking phenomena in nature occur under nonequilibrium conditions: heat conduction along a temperature gradient, transport of matter across a membrane, chemical reactions that go on continuously, and also chemical oscillations, spatial patterns and life itself. This chapter extends thermodynamics to nonequilibrium systems. Section 18.1 decomposes the change of entropy into entropy flow and entropy production and, under the local equilibrium hypothesis, writes the entropy balance equation, from which the entropy production is expressed as a sum of "flux × force"; Section 18.2 discusses the near-equilibrium linear region: phenomenological relations, the Onsager reciprocal relations and their microscopic basis, cross effects such as thermoelectricity and thermal diffusion, the equations of membrane transport and active transport across biological membranes, and the principle of minimum entropy production; Section 18.3 enters the far-from-equilibrium nonlinear region and uses the kinetics of the previous three chapters ([6.3.15](/6.3.15)–[6.3.17](/6.3.17)) together with the stability theory of ordinary differential equations ([2.4.11](/2.4.11)) to analyze chemical oscillations and Turing patterns, showing how ordered structures are maintained by continuous dissipation; Section 18.4 returns to living systems and ties in with the **principle of entropy increase** in physics ([5.2.4](/5.2.4#thm-4.6.2)) and with the prelude at the end of [6.3.2](/6.3.2). This is the chapter in which physical chemistry connects most closely with biophysics: a cell is an open system far from equilibrium, and its energy conversion, transport and timekeeping all have to be described in the language developed here.

## 18.1. Entropy Flow and Entropy Production

### 18.1.1. Equilibrium, Steady State and Far from Equilibrium

The development of thermodynamics has gone through roughly three stages:

| Stage | Subject | Core results |
|---|---|---|
| Equilibrium thermodynamics (classical thermodynamics) | Equilibrium states and reversible processes; irreversible processes are only judged for direction | The four laws, state functions, free-energy criteria |
| Linear nonequilibrium thermodynamics | Open systems near equilibrium, with fluxes linear in the forces | Local equilibrium, Onsager reciprocal relations, principle of minimum entropy production |
| Nonlinear nonequilibrium thermodynamics | Open systems far from equilibrium, nonlinear irreversible processes | Stability theory, dissipative structures, fluctuations and bifurcations |

An equilibrium state must be distinguished from a **steady state** ([5.2.1](/5.2.1)): a metal rod whose two ends are connected to heat reservoirs at different temperatures reaches, after a long enough time, a state in which the temperature at each point no longer changes but a heat current always passes through; this is a steady state, not an equilibrium state. An equilibrium state has no macroscopic flow of any kind and produces no entropy; a steady state has to be maintained by a continuous supply from the surroundings and keeps producing entropy inside. The "nonequilibrium steady states" of this chapter are always in this sense.

Nineteenth-century classical thermodynamics left two puzzles. One is that Clausius (1867) extended the principle of entropy increase to the whole universe and drew the conclusion of the "heat death": the entropy of the universe tends to a maximum and all macroscopic change will eventually stop. Boltzmann pointed out that the equilibrium state itself is accompanied by fluctuations; today the premises of this extension, that the universe is a finite isolated system and that an equilibrium state in the usual sense exists, are both unclear (the universe is expanding, and self-gravitating systems have no equilibrium state in the usual sense), and the heat-death argument is only an extrapolation. The other is that a great number of ordered phenomena in nature seem to contradict the idea that "entropy increase means going toward disorder": biological evolution proceeds from the simple to the complex; the patterns of biological membranes, leaves and butterfly wings are regular structures; in chemistry there are *chemical oscillations* (concentrations of components varying periodically with time), Turing structures (periodically distributed in space; Turing, 1952), chemical waves propagating in an unstirred thin layer of solution, and multiple steady states appearing under the same set of external conditions. The key to resolving both puzzles is to distinguish an isolated system from an **open system**: the principle of entropy increase constrains only isolated systems; the entropy of an open system can decrease provided that it exports enough entropy to the environment.

### 18.1.2. Entropy Flow and Entropy Production

For any system, the change of entropy is divided into two parts.

**Definition 18.1.1** The entropy change of a system is written

$$
\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S,
\tag{18.1}
$$
where $\mathrm{d}_{\mathrm{e}}S$ is called the **entropy flow**, the entropy change caused by the exchange of energy and matter between the system and its surroundings, and $\mathrm{d}_{\mathrm{i}}S$ is called the **entropy production**, the entropy change caused by irreversible processes inside the system (heat transfer, diffusion, viscous flow, chemical reactions, an electric current through a resistance, and so on). For a closed system $\mathrm{d}_{\mathrm{e}}S = \delta Q/T$, where $T$ is the temperature at the boundary where the heat crosses; for an open system the entropy brought in by matter must be added, $\mathrm{d}_{\mathrm{e}}S = \delta Q/T + \sum_{\mathrm{B}} S_{\mathrm{B}}\,\mathrm{d}_{\mathrm{e}}n_{\mathrm{B}}$ ($S_{\mathrm{B}}$ is the partial molar entropy and $\mathrm{d}_{\mathrm{e}}n_{\mathrm{B}}$ the amount of substance flowing in from the surroundings).

The entropy flow can be positive or negative: $\mathrm{d}_{\mathrm{e}}S < 0$ when the system releases heat or expels matter of high entropy. The entropy production, on the other hand, is constrained by the second law.

**Theorem 18.1.1** For any process of any system,

$$
\mathrm{d}_{\mathrm{i}}S \ge 0,
\tag{18.2}
$$
with equality only for reversible processes.

For a closed system Eq. (18.2) is the **Clausius inequality** $\mathrm{d}S \ge \delta Q/T$; for an isolated system $\mathrm{d}_{\mathrm{e}}S = 0$ and it reduces to the principle of entropy increase $\mathrm{d}S \ge 0$. Equation (18.2) is therefore the general statement of the second law that is not restricted to isolated systems: it holds for open systems as well, because the system together with the surroundings with which it exchanges matter and energy is isolated, and the exchange itself (when temperature and chemical potential are continuous across the boundary) produces no entropy. Three corollaries follow:

1. Locality: if the system is divided into several parts, the entropy production of each part is nonnegative, and a negative entropy production in one place cannot offset a positive one in another. This is much stronger than "the total entropy production is nonnegative" and is the basis for writing the local form $\sigma \ge 0$ in 18.1.4.
2. Coupling: when several irreversible processes take place at the same place, the entropy production computed for one of them alone may be negative as long as the sum is nonnegative. This is the thermodynamic condition for a process to proceed "against its own driving force"; the active transport of 18.2.5 is an example, and the same reasoning applies to the **coupled reactions** of [6.3.7](/6.3.7).
3. Ordering of open systems: when $\mathrm{d}_{\mathrm{i}}S \ge 0$, as long as $\mathrm{d}_{\mathrm{e}}S < 0$ and $\lvert\mathrm{d}_{\mathrm{e}}S\rvert > \mathrm{d}_{\mathrm{i}}S$, we have $\mathrm{d}S < 0$. In a steady state $\mathrm{d}S = 0$ and $\mathrm{d}_{\mathrm{e}}S = -\mathrm{d}_{\mathrm{i}}S < 0$: to maintain a nonequilibrium steady state, entropy must be continuously exported to the surroundings.

**Example 18.1.1** A conducting rod connects two heat reservoirs at temperatures $T_1$ and $T_2$ ($T_1 > T_2$), and in the steady state the heat passing through per unit time is $\Phi$. Find the rate of entropy production of the rod.

Solution: In the steady state the state of the rod does not change, $\mathrm{d}S/\mathrm{d}t = 0$. The rod gains entropy $\Phi/T_1$ at the high-temperature end and loses entropy $\Phi/T_2$ at the low-temperature end, so the entropy flow is $\mathrm{d}_{\mathrm{e}}S/\mathrm{d}t = \Phi/T_1 - \Phi/T_2 < 0$ and

$$
\frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} = -\frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} = \Phi\left(\frac{1}{T_2} - \frac{1}{T_1}\right) > 0.
$$
The entropy of the rod itself does not change; it "transports" all the entropy produced to the low-temperature reservoir. This is exactly the part of the entropy increase of the large isolated system caused by irreversible heat transfer in [6.3.2](/6.3.2), except that it is now located where the irreversible process occurs, inside the rod.

### 18.1.3. Entropy Production and Affinity of Chemical Reactions

Example 4.3.1 of [6.3.4](/6.3.4) has already shown that a reaction in an adiabatic rigid container exchanges no heat and yet the entropy increases, the entropy gained coming entirely from the irreversibility of the reaction. In general, let only one reaction take place in a closed system with **extent of reaction** $\xi$, and let the system exchange only heat and volume work with the surroundings. From the fundamental equation of a system of variable composition $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ and $\mathrm{d}U = \delta Q - p\,\mathrm{d}V$ (reversible volume work),

$$
\mathrm{d}S = \frac{\delta Q}{T} - \frac{1}{T}\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}\xi .
$$
The first term is the entropy flow and the second the entropy production.

**Definition 18.1.2 (Affinity)** The **affinity** of a reaction is defined as

$$
\mathcal{A} = -\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = -\Delta_{\mathrm{r}}G_{\mathrm{m}},
\tag{18.3}
$$
so that the entropy production of a chemical reaction is $\mathrm{d}_{\mathrm{i}}S = \mathcal{A}\,\mathrm{d}\xi/T \ge 0$.

(The concept of affinity was introduced by De Donder in the 1920s, with IUPAC symbol $A$; this chapter writes $\mathcal{A}$ to avoid confusion with the Helmholtz free energy.) Equation (18.3) shows that $\mathcal{A}$ and the reaction rate $\mathrm{d}\xi/\mathrm{d}t$ must have the same sign: when $\mathcal{A} > 0$ the reaction can proceed only in the forward direction, and at equilibrium $\mathcal{A} = 0$. By the **reaction isotherm**, $\mathcal{A} = RT\ln(K^\circ/Q)$, where $Q$ is the reaction quotient. $\mathcal{A}$ differs from $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ only in sign but has a more general meaning: $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ as a criterion requires constant temperature and pressure, whereas $\mathcal{A}\,\mathrm{d}\xi/T$ is the entropy production under any conditions. At constant temperature and pressure, $T\,\mathrm{d}_{\mathrm{i}}S = \mathcal{A}\,\mathrm{d}\xi = -\mathrm{d}G$: the decrease of the **Gibbs free energy** is $T$ times the entropy production, so the Gibbs free energy criterion of [6.3.3](/6.3.3#sec-3.1.3) is a special case of Theorem 18.1.1.

When several reactions proceed simultaneously, $\mathrm{d}_{\mathrm{i}}S = \sum_r \mathcal{A}_r\,\mathrm{d}\xi_r/T \ge 0$; by Corollary 2, one of the reactions may have $\mathcal{A}_r\,\mathrm{d}\xi_r < 0$, that is, proceed against its own affinity, provided that it is mechanistically coupled to another reaction (such as phosphorylation driven by ATP hydrolysis).

### 18.1.4. The Local Equilibrium Hypothesis

Thermodynamic quantities ($T$, $p$, $\mu_{\mathrm{B}}$, $S$) are defined for equilibrium states. In a nonequilibrium system the temperature and the concentrations vary with position and time, and an assumption is needed to use them.

**Definition 18.1.3 (Local Equilibrium Hypothesis)** Divide the macroscopic system into many small volume elements, each macroscopically small enough that its properties can be regarded as uniform, and microscopically large enough to contain a large number of molecules so that fluctuations can be neglected (relative fluctuations $\propto N^{-1/2}$). If the relaxation time $\tau_{\text{micro}}$ within a volume element, the observation time scale $t$ and the relaxation time $\tau_{\text{macro}}$ of the whole system toward equilibrium satisfy

$$
\tau_{\text{micro}} \ll t \ll \tau_{\text{macro}},
$$
it is assumed that every volume element is in an equilibrium state at every moment, its state being determined by the local $T(\boldsymbol{r}, t)$, $p(\boldsymbol{r}, t)$, $c_{\mathrm{B}}(\boldsymbol{r}, t)$, and that the local thermodynamic functions satisfy all the relations of equilibrium states, in particular the Gibbs relation

$$
T\,\mathrm{d}s = \mathrm{d}u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}c_{\mathrm{B}},
\tag{18.4}
$$
where $s$ and $u$ are the entropy and internal energy per unit volume and $c_{\mathrm{B}}$ is the amount concentration (for an incompressible dilute solution, or when the volume change is neglected).

The condition for local equilibrium is that the relative change of the macroscopic quantities be small on the scale of molecular collisions (the **mean free path** in a gas, a few molecular diameters in a liquid), for example $\bar\lambda\,\lvert\nabla T\rvert/T \ll 1$, and that the macroscopic quantities hardly change during the collision time of molecules. For the common transport processes this is easily satisfied: even for a temperature gradient of $10^3\,\mathrm{K\,cm^{-1}}$ the temperature difference over one mean free path (about $0.1\,\mu\mathrm{m}$) of a gas at ordinary pressure is only $10^{-2}\,\mathrm{K}$. It fails in processes such as shock waves, extremely dilute gases and ultrafast laser excitation.

For chemical reactions, local equilibrium only requires that the reaction be much slower than the exchange of energy, so that the velocity distribution and the energy-level distribution of the reacting molecules remain equilibrium (Boltzmann) distributions; it does not require the reaction to be close to chemical equilibrium: a reaction with a large affinity, far from chemical equilibrium, still satisfies local equilibrium as long as it is not extremely fast. The "linearity" of the next section does require closeness to chemical equilibrium, and the two should not be confused.

### 18.1.5. The Entropy Balance Equation

Under local equilibrium we can write the local entropy budget and find the explicit form of the entropy production. Entropy is an extensive quantity, and its change in each volume element has two sources: the entropy flow through the surface and the entropy production inside.

**Definition 18.1.4** The local entropy balance equation is written

$$
\frac{\partial s}{\partial t} = -\nabla\cdot\boldsymbol{J}_S + \sigma,
\tag{18.5}
$$
where $\boldsymbol{J}_S$ is called the entropy flux density and $\sigma$ the rate of entropy production (per unit volume); the second law requires $\sigma \ge 0$. The rate of entropy production of the whole system is $P = \mathrm{d}_{\mathrm{i}}S/\mathrm{d}t = \int_V \sigma\,\mathrm{d}V$.

We derive $\boldsymbol{J}_S$ and $\sigma$ for a fluid at rest in which heat conduction, diffusion and chemical reactions are present together (convection and viscosity are not considered; mechanical equilibrium holds). The local conservation of energy and of matter is written

$$
\frac{\partial u}{\partial t} = -\nabla\cdot\boldsymbol{J}_u, \qquad
\frac{\partial c_{\mathrm{B}}}{\partial t} = -\nabla\cdot\boldsymbol{J}_{\mathrm{B}} + \sum_r \nu_{\mathrm{B}r}v_r,
$$
where $\boldsymbol{J}_u$ is the energy flux density, $\boldsymbol{J}_{\mathrm{B}}$ is the flux density of matter B ($\mathrm{mol\,m^{-2}\,s^{-1}}$) and $v_r$ is the **reaction rate** of the $r$th reaction per unit volume. Substituting these into the time derivative of Eq. (18.4):

$$
\frac{\partial s}{\partial t} = \frac{1}{T}\frac{\partial u}{\partial t} - \sum_{\mathrm{B}}\frac{\mu_{\mathrm{B}}}{T}\frac{\partial c_{\mathrm{B}}}{\partial t}
= -\frac{1}{T}\nabla\cdot\boldsymbol{J}_u + \sum_{\mathrm{B}}\frac{\mu_{\mathrm{B}}}{T}\nabla\cdot\boldsymbol{J}_{\mathrm{B}} - \sum_r\frac{v_r}{T}\sum_{\mathrm{B}}\nu_{\mathrm{B}r}\mu_{\mathrm{B}} .
$$
Using $f\,\nabla\cdot\boldsymbol{J} = \nabla\cdot(f\boldsymbol{J}) - \boldsymbol{J}\cdot\nabla f$ to move the divergence outside in the first two terms, and Eq. (18.3):

$$
\frac{\partial s}{\partial t} = -\nabla\cdot\left(\frac{\boldsymbol{J}_u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}}{T}\right)
+ \boldsymbol{J}_u\cdot\nabla\frac{1}{T} + \sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot\left(-\nabla\frac{\mu_{\mathrm{B}}}{T}\right) + \sum_r v_r\frac{\mathcal{A}_r}{T}.
$$
Comparing with Eq. (18.5), the divergence term is the entropy flow and the rest is the entropy production:

$$
\boldsymbol{J}_S = \frac{1}{T}\Big(\boldsymbol{J}_u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\Big), \qquad
\sigma = \boldsymbol{J}_u\cdot\nabla\frac{1}{T} + \sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot\left(-\nabla\frac{\mu_{\mathrm{B}}}{T}\right) + \sum_r v_r\frac{\mathcal{A}_r}{T}.
\tag{18.6}
$$

The entropy flow is carried by the energy flow and the matter flow; the entropy production is a sum of products, each term being a "flux" multiplied by the "gradient" that causes it. This structure is general.

**Definition 18.1.5** Write the rate of entropy production in bilinear form

$$
\sigma = \sum_k J_k X_k,
\tag{18.7}
$$
where $J_k$ is called a **thermodynamic flux**, which describes how fast the irreversible process goes, and $X_k$, multiplied with it, is called the **thermodynamic force** conjugate to $J_k$, which describes the inhomogeneity that drives the process or the degree of departure from equilibrium. At equilibrium all forces and fluxes vanish simultaneously.

| Irreversible process | Flux $J_k$ | Conjugate force $X_k$ | Tensor rank |
|---|---|---|---|
| Heat conduction | Energy (heat) flux density $\boldsymbol{J}_q$ | $\nabla(1/T) = -\nabla T/T^2$ | Vector |
| Diffusion (isothermal) | Matter flux density $\boldsymbol{J}_{\mathrm{B}}$ | $-\nabla\mu_{\mathrm{B}}/T$ | Vector |
| Ion migration, electric conduction (isothermal) | $\boldsymbol{J}_{\mathrm{B}}$ or current density $\boldsymbol{J}_{\mathrm{e}}$ | $-\nabla\tilde\mu_{\mathrm{B}}/T$ or $\boldsymbol{E}/T$ | Vector |
| Chemical reaction | Reaction rate $v_r$ | $\mathcal{A}_r/T$ | Scalar |
| Viscous flow | Viscous stress tensor | Velocity gradient (symmetric part) $/T$ | Second-rank tensor |

For charged components the chemical potential in the diffusion force must be replaced by the **electrochemical potential** $\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}} + z_{\mathrm{B}}F\varphi$ ([6.3.13](/6.3.13)): at constant temperature the entropy production of ions is $\sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot(-\nabla\tilde\mu_{\mathrm{B}})/T$, in which the electric-potential-gradient terms together give $\boldsymbol{J}_{\mathrm{e}}\cdot\boldsymbol{E}/T$, that is, the Joule heat divided by the temperature. The division into fluxes and forces is not unique: for example one can use as flux the "heat flow" $\boldsymbol{J}_q' = \boldsymbol{J}_u - \sum_{\mathrm{B}}H_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}$ obtained by subtracting the enthalpy carried by matter, and the diffusion force becomes $-(\nabla\mu_{\mathrm{B}})_T/T$; as long as $\sigma$ is unchanged, the different choices are physically equivalent.

## 18.2. Linear Nonequilibrium Thermodynamics

### 18.2.1. Phenomenological Relations

At equilibrium $X_k = 0$ and $J_k = 0$. Not far from equilibrium, expand each flux in a Taylor series in all the forces and keep only the first-order terms:

**Definition 18.2.1** The linear relations in the near-equilibrium region

$$
J_k = \sum_l L_{kl}X_l
\tag{18.8}
$$
are called linear phenomenological relations, and the coefficients $L_{kl}$ are called **phenomenological coefficients**: $L_{kk}$ describes the direct effect of the force $X_k$ on its conjugate flux, and $L_{kl}$ ($k \ne l$) describes the cross effect of the force $X_l$ on another flux. The phenomenological coefficients may depend on the local state ($T$, $p$, composition) but not on the forces.

The familiar transport laws are all special cases with direct effects only:

- Heat conduction: $\boldsymbol{J}_q = L_{qq}\nabla(1/T) = -(L_{qq}/T^2)\nabla T$, which is **Fourier's law**, with thermal conductivity $\kappa = L_{qq}/T^2$ ([5.2.2](/5.2.2#sec-2.4)).
- Diffusion: for an isothermal ideal dilute solution, $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}} + RT\ln(c_{\mathrm{B}}/c^\circ)$ and $\boldsymbol{J}_{\mathrm{B}} = -L_{\mathrm{BB}}\nabla\mu_{\mathrm{B}}/T = -(L_{\mathrm{BB}}R/c_{\mathrm{B}})\nabla c_{\mathrm{B}}$, which is **Fick's law**, with diffusion coefficient $D = L_{\mathrm{BB}}R/c_{\mathrm{B}}$. Using the gradient of the chemical potential rather than that of the concentration as the driving force gives a unified explanation of diffusion in nonideal solutions and of "uphill diffusion" against the concentration gradient (which occurs in phase-separating mixtures).
- Electric conduction: $\boldsymbol{J}_{\mathrm{e}} = (L_{\mathrm{ee}}/T)\boldsymbol{E}$, the differential form of **Ohm's law**.

The second law restricts the phenomenological coefficients: for any forces, $\sigma = \sum_{k,l}L_{kl}X_kX_l \ge 0$. This is a **quadratic form** in $X$, so the symmetric part $\frac12(L + L^{\mathsf T})$ of $L$ must be a **positive semidefinite matrix** ([2.1.7](/2.1.7#sec-7.3)). In particular $L_{kk} \ge 0$ (thermal conductivity, diffusion coefficient and conductance are all positive), and $L_{kk}L_{ll} \ge \frac14(L_{kl} + L_{lk})^2$: the size of a cross coefficient is bounded by the direct coefficients.

The linear region of a chemical reaction is narrow. For an elementary reaction $\ce{A <=> B}$ the ratio of the forward and reverse rates is fixed by the **principle of detailed balance**: $v_+/v_- = \exp(\mathcal{A}/RT)$ (at equilibrium $\mathcal{A} = 0$ and $v_+ = v_-$; for an ideal solution $v_+/v_- = (k_+/k_-)(c_{\mathrm{A}}/c_{\mathrm{B}}) = K^\circ/Q$). The net rate is therefore

$$
v = v_+ - v_- = v_+\left(1 - \mathrm{e}^{-\mathcal{A}/RT}\right) \approx \frac{v_{\mathrm{eq}}}{R}\,\frac{\mathcal{A}}{T}\qquad(\lvert\mathcal{A}\rvert \ll RT),
\tag{18.9}
$$
where $v_{\mathrm{eq}}$ is the rate of the forward (reverse) reaction at equilibrium. Only when $\lvert\mathcal{A}\rvert$ is much smaller than $RT$ ($2.5\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$) is the reaction rate proportional to the affinity, with $L = v_{\mathrm{eq}}/R$. The affinity of ATP hydrolysis in a cell is about $50\,\mathrm{kJ\,mol^{-1}}$ ([6.3.7](/6.3.7#sec-7.6.2)), 20 times $RT$ and far outside the linear region. In contrast, heat conduction and diffusion remain linear under gradients that are macroscopically very large, because on the molecular scale these gradients are extremely small (18.1.4). The conclusions of linear nonequilibrium thermodynamics apply widely to transport processes, but to chemical reactions only close to equilibrium.

### 18.2.2. Onsager Reciprocal Relations

There is a general symmetry among the coefficients of cross effects.

**Theorem 18.2.1 (Onsager Reciprocal Relations)** If the fluxes and forces are chosen according to Eq. (18.7) (independent of one another, with $\sigma = \sum J_kX_k$), then in the absence of a magnetic field and for a system that does not rotate, the matrix of phenomenological coefficients is symmetric:

$$
L_{kl} = L_{lk}.
\tag{18.10}
$$
In the presence of a magnetic field $\boldsymbol{B}$ (or for rotation with angular velocity $\boldsymbol{\omega}$), $L_{kl}(\boldsymbol{B}) = L_{lk}(-\boldsymbol{B})$ (the Onsager–Casimir relations; if a variable changes sign under time reversal, the corresponding sign must also be included).

Onsager proved this result in 1931 and received the 1968 Nobel Prize in Chemistry for it. Its significance is that the ability of the force $X_l$ to cause the flux $J_k$ equals the ability of the force $X_k$ to cause the flux $J_l$. Two cross effects that look entirely unrelated (such as the Seebeck effect and the Peltier effect in thermoelectricity, 18.2.3) are described by the same coefficient, and the number of independent coefficients is reduced from $n^2$ to $n(n+1)/2$.

The reciprocal relations cannot be derived from macroscopic thermodynamics; they rest on the time-reversal symmetry of microscopic mechanics and on the theory of equilibrium fluctuations. The idea of the derivation is as follows.

Let $\alpha_1, \dots, \alpha_n$ be the deviations of a set of macroscopic variables from their equilibrium values (such as the differences in energy or in amount of substance between two parts). Near equilibrium the entropy of the system can be expanded as

$$
\Delta S = -\frac12\sum_{i,j}g_{ij}\alpha_i\alpha_j,
$$
where $g = (g_{ij})$ is symmetric and positive definite (equilibrium is a maximum of entropy). The rate of entropy production is $\mathrm{d}\Delta S/\mathrm{d}t = \sum_i \dot\alpha_i X_i$ with $X_i = \partial\Delta S/\partial\alpha_i = -\sum_j g_{ij}\alpha_j$, so $J_i = \dot\alpha_i$ and $X_i$ form a set of conjugate fluxes and forces.

1. Equilibrium fluctuations: by the **Boltzmann entropy formula** $S = k_{\mathrm{B}}\ln\Omega$ ([5.2.4](/5.2.4#fml-4.8.1)), the probability of the macroscopic state with deviation $\boldsymbol{\alpha}$ is $\propto \Omega \propto \exp(\Delta S/k_{\mathrm{B}})$ (Einstein's fluctuation formula), a multivariate normal distribution. Integration by parts gives $\langle\alpha_iX_j\rangle = -k_{\mathrm{B}}\delta_{ij}$:

$$
\langle \alpha_i X_j\rangle = \int \alpha_i\,\frac{\partial \Delta S}{\partial\alpha_j}\,\frac{\mathrm{e}^{\Delta S/k_{\mathrm{B}}}}{Z}\,\mathrm{d}\boldsymbol{\alpha}
= k_{\mathrm{B}}\int \alpha_i\,\frac{\partial}{\partial\alpha_j}\frac{\mathrm{e}^{\Delta S/k_{\mathrm{B}}}}{Z}\,\mathrm{d}\boldsymbol{\alpha}
= -k_{\mathrm{B}}\delta_{ij}.
$$
2. Regression hypothesis: a deviation produced by a spontaneous fluctuation decays on average according to the macroscopic phenomenological law; that is, given the initial deviation, $\langle\dot\alpha_i\rangle = \sum_k L_{ik}X_k$.
3. Microscopic reversibility: the equations of motion of the molecules are invariant under time reversal, so in an equilibrium state the probability of "$\alpha_i$ appearing first and $\alpha_j$ appearing after a time $\tau$" equals that of "$\alpha_j$ first and $\alpha_i$ after $\tau$" (for variables that do not change sign under time reversal); hence $\langle\alpha_i(0)\alpha_j(\tau)\rangle = \langle\alpha_j(0)\alpha_i(\tau)\rangle$.

Differentiating with respect to $\tau$ and letting $\tau \to 0^+$ gives $\langle\alpha_i\dot\alpha_j\rangle = \langle\alpha_j\dot\alpha_i\rangle$. Substituting items 2 and 1:

$$
\sum_k L_{jk}\langle\alpha_iX_k\rangle = \sum_k L_{ik}\langle\alpha_jX_k\rangle
\quad\Longrightarrow\quad -k_{\mathrm{B}}L_{ji} = -k_{\mathrm{B}}L_{ij}.
$$
This is Eq. (18.10). The equations of motion of charged particles in a magnetic field are invariant under time reversal only if $\boldsymbol{B}$ is reversed at the same time, which gives the Onsager–Casimir form. The same line of thought gives a direct link between the phenomenological coefficients and equilibrium fluctuations (the Green–Kubo formula): $L_{ij} = \frac{1}{k_{\mathrm{B}}}\int_0^\infty \langle J_i(0)J_j(t)\rangle\,\mathrm{d}t$; the size of the dissipation is determined by the time correlation of spontaneous fluctuations at equilibrium. The Einstein relation $D = k_{\mathrm{B}}T/f$ ($f$ is the friction coefficient) between the diffusion coefficient and the friction coefficient of **Brownian motion** ([6.3.21](/6.3.21)) is the earliest example; these are collectively called the fluctuation–dissipation theorem.

**Example 18.2.1** The triangular reactions $\ce{A <=> B}$ (1), $\ce{B <=> C}$ (2) and $\ce{C <=> A}$ (3) take place in a closed ideal solution close to equilibrium. Verify the reciprocal relation.

Solution: The three affinities satisfy $\mathcal{A}_1 + \mathcal{A}_2 + \mathcal{A}_3 = 0$ (going around the cycle back to A), so only two are independent. By Eq. (18.9), the net rate of each reaction is $v_r = \ell_r\mathcal{A}_r/T$ with $\ell_r = v_{r,\mathrm{eq}}/R > 0$; detailed balance is used here: at equilibrium the forward and reverse rates of every reaction are separately equal, so each $v_r$ depends only on its own $\mathcal{A}_r$. The entropy production is

$$
T\sigma = v_1\mathcal{A}_1 + v_2\mathcal{A}_2 + v_3\mathcal{A}_3 = (v_1 - v_3)\mathcal{A}_1 + (v_2 - v_3)\mathcal{A}_2 ,
$$
so the independent fluxes are $J_1 = v_1 - v_3$, $J_2 = v_2 - v_3$ and the conjugate forces are $X_1 = \mathcal{A}_1/T$, $X_2 = \mathcal{A}_2/T$. Substituting $\mathcal{A}_3 = -\mathcal{A}_1 - \mathcal{A}_2$:

$$
J_1 = (\ell_1 + \ell_3)X_1 + \ell_3X_2, \qquad J_2 = \ell_3X_1 + (\ell_2 + \ell_3)X_2 ,
$$
and the cross coefficients are $L_{12} = L_{21} = \ell_3$. If a net cyclic flow $\ce{A -> B -> C -> A}$ were allowed to exist at equilibrium (violating detailed balance), this symmetry would not hold. Onsager used precisely this example to show the connection between the reciprocal relations and detailed balance (the **principle of microscopic reversibility**, [6.3.15](/6.3.15)).

A final general restriction comes from symmetry.

**Theorem 18.2.2 (Curie Principle)** In an isotropic medium there is no linear coupling between fluxes and forces of different tensor rank.

(Stated without proof.) The reason is that in an isotropic medium the phenomenological coefficients are invariant under arbitrary rotations, and a scalar force (such as an affinity) multiplied by an invariant coefficient cannot produce a directed vector flux. Hence in an isotropic solution a chemical reaction cannot directly drive diffusion, whereas heat conduction and diffusion (both vectors) can be coupled. This has an important consequence for biology: for a cell to use a chemical reaction (a scalar) to drive directed transport across a membrane (a vector), an anisotropic structure is needed, namely proteins embedded in the membrane with a definite orientation. The ion pumps of 18.2.5 are exactly such structures.

### 18.2.3. Cross Effects: Thermoelectric Effects and Thermal Diffusion

Consider first thermoelectric effects. When a temperature gradient and an electric current are present together in a conductor (one-dimensional, vector notation omitted), take the heat flux $J_q$ and the current density $J_{\mathrm{e}}$ as the fluxes, with conjugate forces $\partial_x(1/T)$ and $-\partial_x\varphi/T$ (here $\varphi$ is understood as the electrochemical potential of the electrons divided by the charge, whose difference is what a voltmeter measures):

$$
J_q = L_{qq}\,\partial_x\frac1T + L_{q\mathrm{e}}\left(-\frac{\partial_x\varphi}{T}\right), \qquad
J_{\mathrm{e}} = L_{\mathrm{e}q}\,\partial_x\frac1T + L_{\mathrm{ee}}\left(-\frac{\partial_x\varphi}{T}\right).
$$

- *Peltier effect*: at uniform temperature ($\partial_xT = 0$) the electric current carries a heat flux $J_q = (L_{q\mathrm{e}}/L_{\mathrm{ee}})J_{\mathrm{e}}$, and the proportionality coefficient $\Pi = L_{q\mathrm{e}}/L_{\mathrm{ee}}$ is called the Peltier coefficient; at the junction of two conductors $\Pi$ is discontinuous, so heat is absorbed or released, which is the principle of semiconductor cooling plates.
- **Seebeck effect** ([5.3.5](/5.3.5#sec-5.4.3)): in open circuit ($J_{\mathrm{e}} = 0$) a temperature gradient produces a potential gradient. From the second equation, $L_{\mathrm{ee}}\partial_x\varphi/T = L_{\mathrm{e}q}\partial_x(1/T) = -L_{\mathrm{e}q}\partial_xT/T^2$, that is, $\partial_x\varphi = -\alpha_{\mathrm{S}}\,\partial_xT$ with Seebeck coefficient $\alpha_{\mathrm{S}} = L_{\mathrm{e}q}/(TL_{\mathrm{ee}})$.

By the Onsager relation $L_{q\mathrm{e}} = L_{\mathrm{e}q}$,

$$
\Pi = T\alpha_{\mathrm{S}} .
\tag{18.11}
$$
This is the second Thomson relation, obtained by W. Thomson (Kelvin) in 1854 with an argument that forcibly separates the reversible and irreversible parts; Onsager's theory gave it a rigorous basis, and it has been confirmed by measurements on many metals and semiconductors. Equation (18.11) connects an electrical measurement (the open-circuit voltage) with a thermal measurement (the heat absorbed or released at a junction) and is the most classical test of the reciprocal relations.

Thermal diffusion and the Dufour effect are another pair of cross effects. When a temperature gradient is applied to a binary mixture, a concentration gradient appears even if the composition was initially uniform, one component accumulating at the cold end; this is called *thermal diffusion* or the Soret effect. Its reciprocal effect is heat flow caused by a concentration gradient (the Dufour effect). In the steady state with $J_{\mathrm{B}} = 0$, the composition difference caused by thermal diffusion is proportional to the temperature difference, with a proportionality coefficient (the Soret coefficient) typically only of the order of $10^{-3}$–$10^{-2}\,\mathrm{K^{-1}}$, but it can be amplified cumulatively in a thermal diffusion column, which was used for isotope separation. In solution, the directed motion of charged colloidal particles and biological macromolecules along a temperature gradient is called thermophoresis, which is used in biochemistry to determine binding constants between molecules (microscale thermophoresis).

Similar cross effects include the electrokinetic phenomena: an electric field drives a liquid through a capillary or a porous plug (**electroosmosis**), and a pressure-driven flow produces a potential difference (streaming potential); the coefficients of the two also satisfy a reciprocal relation (the Saxén relation, [6.3.21](/6.3.21)).

### 18.2.4. Membrane Transport: The Kedem–Katchalsky Equations

Biological and artificial membranes let water pass and also let solutes pass to different degrees; a **semipermeable membrane** is only the ideal limit. Consider a membrane separating two dilute aqueous solutions of the same solute s at the same temperature, with pressure difference $\Delta p$ across the membrane and difference of **osmotic pressure** $\Delta\varPi = RT\Delta c_{\mathrm{s}}$ ([6.3.5](/6.3.5#sec-5.3.4)). The dissipation function per unit membrane area, $\Phi = T\sigma$ (integrated over the thickness of the membrane), is

$$
\Phi = J_{\mathrm{w}}\Delta\mu_{\mathrm{w}} + J_{\mathrm{s}}\Delta\mu_{\mathrm{s}},
$$
where $J_{\mathrm{w}}$ and $J_{\mathrm{s}}$ are the matter flux densities of water and solute, and $\Delta\mu$ is the difference of the chemical potential between the two sides of the membrane (the higher side minus the lower, consistent with the positive direction of the flow). In dilute solution $\Delta\mu_{\mathrm{w}} = V_{\mathrm{w}}(\Delta p - \Delta\varPi)$ and $\Delta\mu_{\mathrm{s}} = V_{\mathrm{s}}\Delta p + \Delta\varPi/\bar c_{\mathrm{s}}$ ($V$ is the partial molar volume and $\bar c_{\mathrm{s}}$ the logarithmic mean of the concentrations on the two sides, approximately the arithmetic mean). Substituting and regrouping:

$$
\Phi = \underbrace{(J_{\mathrm{w}}V_{\mathrm{w}} + J_{\mathrm{s}}V_{\mathrm{s}})}_{J_V}\Delta p + \underbrace{\left(\frac{J_{\mathrm{s}}}{\bar c_{\mathrm{s}}} - J_{\mathrm{w}}V_{\mathrm{w}}\right)}_{J_{\mathrm{D}}}\Delta\varPi .
$$
$J_V$ is the volume flow (volume flow rate per unit area) and $J_{\mathrm{D}}$ is the "exchange flow" of the solute relative to water. Writing the phenomenological relations in this set of fluxes and forces and using the Onsager relation $L_{p\mathrm{D}} = L_{\mathrm{D}p}$:

$$
J_V = L_p\Delta p + L_{p\mathrm{D}}\Delta\varPi, \qquad J_{\mathrm{D}} = L_{p\mathrm{D}}\Delta p + L_{\mathrm{D}}\Delta\varPi .
$$
Define the *reflection coefficient* $\sigma_{\mathrm{r}} = -L_{p\mathrm{D}}/L_p$ (Staverman, 1951; it is usually written $\sigma$, here a subscript is added to avoid confusion with the entropy production); the first equation becomes

$$
J_V = L_p(\Delta p - \sigma_{\mathrm{r}}\Delta\varPi).
\tag{18.12}
$$
Eliminating $\Delta p$ in the second equation with $\Delta p = J_V/L_p + \sigma_{\mathrm{r}}\Delta\varPi$ gives $J_{\mathrm{D}} = -\sigma_{\mathrm{r}}J_V + (L_{\mathrm{D}} - \sigma_{\mathrm{r}}^2L_p)\Delta\varPi$; then with $J_{\mathrm{s}} \approx \bar c_{\mathrm{s}}(J_V + J_{\mathrm{D}})$ (in dilute solution $J_V \approx J_{\mathrm{w}}V_{\mathrm{w}}$),

$$
J_{\mathrm{s}} = \omega\,\Delta\varPi + (1 - \sigma_{\mathrm{r}})\bar c_{\mathrm{s}}J_V, \qquad \omega = \bar c_{\mathrm{s}}(L_{\mathrm{D}} - \sigma_{\mathrm{r}}^2L_p).
\tag{18.13}
$$
Equations (18.12) and (18.13) were obtained by Kedem and Katchalsky in 1958 and are called the *Kedem–Katchalsky equations*. The transport properties of the membrane are described by three measurable coefficients: the hydraulic permeability $L_p$, the reflection coefficient $\sigma_{\mathrm{r}}$ and the solute permeability $\omega$; without the reciprocal relation four would be needed. The second law ($L_pL_{\mathrm{D}} \ge L_{p\mathrm{D}}^2$) guarantees $\omega \ge 0$.

- $\sigma_{\mathrm{r}} = 1$: the membrane does not let any solute through ($\omega = 0$), and the volume flow stops at $\Delta p = \Delta\varPi$, which is van 't Hoff's osmotic equilibrium; this is the ideal limit of **reverse osmosis**.
- $\sigma_{\mathrm{r}} = 0$: the membrane has no selectivity for the solute, which passes along with the water flow and produces no effective osmotic pressure.
- $0 < \sigma_{\mathrm{r}} < 1$: the effective osmotic pressure is only $\sigma_{\mathrm{r}}\Delta\varPi$. The capillary wall has $\sigma_{\mathrm{r}}$ close to 0 for small solutes and close to 1 for plasma albumin, so it is the osmotic pressure of proteins (colloid osmotic pressure) that determines the exchange of water between plasma and interstitial fluid; the Starling equation of physiology, $J_V = L_p[(p_{\mathrm{c}} - p_{\mathrm{i}}) - \sigma_{\mathrm{r}}(\varPi_{\mathrm{c}} - \varPi_{\mathrm{i}})]$, is exactly Eq. (18.12).

### 18.2.5. Energy Coupling and Active Transport

Corollary 2 says that a process can proceed against its own driving force as long as it is coupled to another process. The linear theory makes this quantitative. Consider two coupled processes:

$$
J_1 = L_{11}X_1 + L_{12}X_2, \qquad J_2 = L_{12}X_1 + L_{22}X_2 ,
$$
with process 1 "downhill" ($J_1X_1 > 0$) and process 2 driven "uphill" ($J_2X_2 < 0$). The total entropy production is $\sigma = J_1X_1 + J_2X_2 \ge 0$, so the output of the uphill process cannot exceed the input of the downhill process.

**Definition 18.2.2** The quantity

$$
q = \frac{L_{12}}{\sqrt{L_{11}L_{22}}}, \qquad \lvert q\rvert \le 1
$$
is called the **degree of coupling** of the two processes; the efficiency of energy conversion is $\eta = -J_2X_2/(J_1X_1)$.

($\lvert q\rvert \le 1$ follows from the positive semidefiniteness of $L$.) Introducing the reduced force ratio $x = \sqrt{L_{22}/L_{11}}\,X_2/X_1$, direct substitution gives

$$
\eta = -\frac{x(x + q)}{1 + qx}.
$$
For $q > 0$ there is output only when $-q < x < 0$: at $x = 0$ there is no resistance and no work is done; at $x = -q$ the uphill flux stops (the "static head", as when an ion pump no longer transports a net amount at the maximum gradient). Finding the extremum with respect to $x$, the maximum efficiency is

$$
\eta_{\max} = \frac{q^2}{\left(1 + \sqrt{1 - q^2}\right)^2},
$$
attained at $x = (\sqrt{1 - q^2} - 1)/q$ (Kedem and Caplan, 1965). Only complete coupling ($q = 1$) can reach $\eta \to 1$, but then the fluxes tend to zero: high efficiency and high power cannot be had together, for the same reason that the efficiency of a Carnot engine reaches its upper limit only when the engine runs infinitely slowly.

![Efficiency of a linear two-flux energy converter: left, efficiency against the reduced force ratio for different degrees of coupling; right, maximum efficiency against the degree of coupling](./plots/coupling-efficiency.py)

The movement of matter across a membrane down its own electrochemical potential gradient is passive transport and occurs spontaneously; movement against the electrochemical potential gradient is called *active transport* and must be coupled to a process with positive entropy production. By the Curie principle, this coupling can occur only in oriented membrane proteins. The most important example is the $\ce{Na+}$/$\ce{K+}$-ATPase (the sodium–potassium pump, discovered by Skou, Nobel Prize in Chemistry 1997): for each ATP hydrolyzed it pumps 3 $\ce{Na+}$ out of the cell and 2 $\ce{K+}$ into the cell, both ions moving against their electrochemical potential gradients.

**Example 18.2.2** Typical concentrations inside and outside a mammalian cell are $[\ce{Na+}]_{\text{in}} = 12\,\mathrm{mmol\,L^{-1}}$, $[\ce{Na+}]_{\text{out}} = 145\,\mathrm{mmol\,L^{-1}}$, $[\ce{K+}]_{\text{in}} = 140\,\mathrm{mmol\,L^{-1}}$, $[\ce{K+}]_{\text{out}} = 4\,\mathrm{mmol\,L^{-1}}$, with **membrane potential** $\varphi_{\text{in}} - \varphi_{\text{out}} = -70\,\mathrm{mV}$ and $T = 310\,\mathrm{K}$. Estimate the minimum Gibbs free energy required per cycle of the sodium–potassium pump and compare it with the free energy supplied by ATP hydrolysis (concentrations replace activities).

Solution: $RT = 2.58\,\mathrm{kJ\,mol^{-1}}$ and $F\times 0.070\,\mathrm{V} = 6.75\,\mathrm{kJ\,mol^{-1}}$. Moving 1 mol of $\ce{Na+}$ from inside to outside increases the electrochemical potential by

$$
\Delta\tilde\mu_{\ce{Na+}} = RT\ln\frac{145}{12} + F(\varphi_{\text{out}} - \varphi_{\text{in}}) = 6.42 + 6.75 = 13.2\,\mathrm{kJ\,mol^{-1}};
$$
moving 1 mol of $\ce{K+}$ from outside to inside,

$$
\Delta\tilde\mu_{\ce{K+}} = RT\ln\frac{140}{4} + F(\varphi_{\text{in}} - \varphi_{\text{out}}) = 9.16 - 6.75 = 2.4\,\mathrm{kJ\,mol^{-1}}.
$$
Each cycle requires $3 \times 13.2 + 2 \times 2.4 = 44.4\,\mathrm{kJ\,mol^{-1}}$. By [6.3.7](/6.3.7#sec-7.6.2), the $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ of ATP hydrolysis in cells is about $-52.7\,\mathrm{kJ\,mol^{-1}}$ (erythrocytes, $37\,^\circ\mathrm{C}$), enough to drive a cycle, with a thermodynamic efficiency of about $44.4/52.7 \approx 84\%$, close to but not exceeding 1, so the second law is satisfied. Although the concentration gradient of $\ce{K+}$ is large, it is almost canceled by the membrane potential, and most of the free energy of the pump is spent on $\ce{Na+}$; each cycle moves a net positive charge out, so the pump itself also contributes to the membrane potential (an electrogenic pump).

The electrochemical potential gradient of $\ce{Na+}$ established by the sodium–potassium pump is in turn used to drive other transport, called *secondary active transport*. The $\ce{Na+}$–glucose symporter of the small intestinal epithelium takes 2 $\ce{Na+}$ into the cell for each glucose molecule transported; with the data of Example 18.2.2, the electrochemical potential drops by $13.2\,\mathrm{kJ\,mol^{-1}}$ per $\ce{Na+}$ entering, $26.4\,\mathrm{kJ\,mol^{-1}}$ for the two, and the ratio of glucose concentrations inside and outside the cell can reach up to $\exp(26.4/2.58) \approx 3\times10^4$. In mitochondria and chloroplasts, the electron transport chain pumps $\ce{H+}$ across the inner membrane, and the transmembrane electrochemical potential difference of $\ce{H+}$ (the proton-motive force) then drives ATP synthase to make ATP (Mitchell's chemiosmotic theory, Nobel Prize in Chemistry 1978): a reaction drives a flow, and the flow drives another reaction in turn; bioenergetics is just such a chain of couplings.

In biophysics, linear equations of the form of Eq. (18.8) (with electrochemical potential differences and affinities as forces) are often used to describe ion pumps and transporters, and are called linear energy converters. It should be noted that the affinity of ATP hydrolysis is about $20RT$ and strictly speaking lies far outside the linear region (18.2.1), so the linear equations can only be used as an empirical linearization near the actual working point; a molecular-level description requires kinetic models of the cycle (each step satisfying detailed balance, with a net flux through the whole cycle driven by ATP).

### 18.2.6. The Principle of Minimum Entropy Production

In the linear region, a nonequilibrium steady state has a variational property. Let the system have $n$ forces, of which $X_1, \dots, X_m$ are fixed by the boundary conditions (for example the temperatures of the two heat reservoirs, or the concentrations on the two sides of a membrane) and the remaining $X_{m+1}, \dots, X_n$ can adjust freely.

**Theorem 18.2.3 (Principle of Minimum Entropy Production)** If the phenomenological coefficients are constants and satisfy the Onsager reciprocal relations, then with $X_1, \dots, X_m$ fixed, the steady state in which the free fluxes vanish ($J_k = 0$, $k > m$) is exactly the state in which the rate of entropy production $P = \sum_{k,l}L_{kl}X_kX_l$ is a minimum with respect to the free forces.

**Proof** Differentiate with respect to the free forces $X_k$ ($k > m$):

$$
\frac{\partial P}{\partial X_k} = \sum_l (L_{kl} + L_{lk})X_l = 2\sum_l L_{kl}X_l = 2J_k ,
$$
where the second equality uses $L_{kl} = L_{lk}$. The stationary point of $P$ is therefore the state with $J_k = 0$ ($k > m$); $P$ is a positive semidefinite quadratic form (positive definite in the free forces), so the stationary point is a minimum. $\square$

For example, in two coupled processes with $X_1$ fixed and $X_2$ free, the steady state $J_2 = 0$ gives $X_2 = -(L_{12}/L_{22})X_1$, and then $P = (L_{11} - L_{12}^2/L_{22})X_1^2$ is a minimum. The steady state of thermal diffusion (temperature gradient fixed, matter flux zero, concentration gradient adjusting itself) is such a state. Prigogine proposed this principle in 1945 and further proved that under the same conditions $\mathrm{d}P/\mathrm{d}t \le 0$: $P$ is a **Lyapunov function** ([2.4.11](/2.4.11#sec-11.4)) of the steady state, so a nonequilibrium steady state in the linear region is stable and returns to the steady state after a deviation.

The conditions of validity of this principle must be kept in mind:

1. The system is in the linear region, and the phenomenological coefficients can be regarded as constants within the range considered. For example, for the steady temperature distribution in a conducting rod: if $L_{qq} = \kappa T^2$ is constant, the distribution given by minimum entropy production agrees with the steady solution of the heat equation; if actually $\kappa$ is constant (closer to reality for larger temperature differences), the linear steady temperature profile does not strictly minimize $P$, and the two differ by higher-order small quantities in the temperature difference.
2. The reciprocal relations hold (the key step in the proof).
3. The boundary conditions do not change with time.

Far from equilibrium there is no generally valid extremum principle of this kind: a steady state need not minimize entropy production, and may be unstable. Statements such as the "principle of maximum entropy production" are only empirical hypotheses for certain systems and have no general proof. Another corollary of the linear region is more important: since a steady state there is always stable, no new ordered structure can appear spontaneously in the linear region, and the uniform steady state that extends continuously from the equilibrium state, the *thermodynamic branch*, does not become unstable. To obtain ordered structures one must be far from equilibrium.

## 18.3. Far from Equilibrium: Dissipative Structures

### 18.3.1. Stability and Dissipative Structures

In the near-equilibrium region the stability of a steady state is guaranteed by the second variation of the entropy. Glansdorff and Prigogine (1971) extended this to steady states far from equilibrium: under local equilibrium, the second-order deviation $\delta^2 s$ of the entropy from the steady state is always negative definite, $-\delta^2 s$ can serve as a Lyapunov function, and

$$
\frac12\frac{\partial}{\partial t}\delta^2 s = \sum_k \delta J_k\,\delta X_k
$$
(stated without proof), the right-hand side being called the *excess entropy production*. If $\sum\delta J_k\delta X_k > 0$ for all small perturbations, the steady state is stable; where it can become negative the steady state may become unstable. In the linear region $\sum\delta J\delta X = \sum L_{kl}\delta X_k\delta X_l \ge 0$ and the state is always stable. Far from equilibrium, if the reaction network contains positive feedback, most typically *autocatalysis*, in which a product accelerates its own formation, as in $\ce{A + X -> 2X}$, or two substances catalyze each other, the excess entropy production can be negative. As the distance from equilibrium (measured by control parameters such as the concentrations of supplied substances and the energy flux from outside) increases, the original uniform steady state then becomes unstable at some critical value, and the system bifurcates to a new state: concentrations oscillate in time, form a pattern in space, or switch among several steady states.

**Definition 18.3.1 (Dissipative Structure)** An ordered state in time or space that an open system far from equilibrium forms and maintains through nonlinear internal processes, by continuously exchanging energy and matter with its surroundings, is called a **dissipative structure**.

The concept of dissipative structures was proposed by Prigogine (Nobel Prize in Chemistry 1977) and has four elements: an open system; far from equilibrium (a control parameter beyond its critical value); nonlinear interactions (autocatalysis, feedback); and fluctuations (at the instability, tiny **fluctuations** select the concrete form of the new state, such as the position of a pattern or the phase of an oscillation). A dissipative structure is fundamentally different from an equilibrium structure such as a crystal: a crystal is a minimum of the Gibbs free energy and persists when its connection with the surroundings is cut, whereas a dissipative structure is maintained by continuous entropy production and, when the supply of matter and energy is cut off, decays back to the uniform equilibrium state. "Nonequilibrium is a source of order" (Prigogine) means exactly this: under certain conditions a closed system spontaneously goes from order to disorder, while an open system far from equilibrium can spontaneously go from disorder to order. A physical example is Rayleigh–Bénard convection: a liquid layer heated from below forms regular hexagonal convection cells when the temperature difference exceeds a critical value; examples in chemistry and biology are the chemical oscillations, chemical waves and Turing patterns below.

One point is easily misunderstood: in a closed system a chemical reaction can show transient oscillations (such as the BZ reaction carried out in a beaker), but this does not violate the second law. At constant temperature and pressure $G$ of a closed system decreases monotonically, and what oscillates is only the concentrations of intermediates, not $G$; when the reactants are used up and the system approaches equilibrium the oscillations must cease. More rigorously, near equilibrium, in the relaxation equation $\dot{\boldsymbol{\alpha}} = -Lg\boldsymbol{\alpha}$ obtained from Eq. (18.8) and the reciprocal relations, $L$ is symmetric positive semidefinite and $g$ symmetric positive definite, so $Lg$ is similar to the symmetric matrix $g^{1/2}Lg^{1/2}$ and all **eigenvalues** are nonnegative real numbers: near equilibrium there is only monotonic relaxation, and not even damped oscillation occurs. Sustained chemical oscillations can occur only in open systems far from equilibrium into which matter is continuously supplied.

### 18.3.2. Chemical Oscillation: The Brusselator

The *Brusselator* is a model proposed by Prigogine and Lefever (1968) in Brussels that illustrates the conditions for chemical oscillation with the simplest mechanism:

$$
\begin{aligned}
&\ce{A -> X}, && k_1, \\
&\ce{2X + Y -> 3X}, && k_2, \\
&\ce{B + X -> Y + D}, && k_3, \\
&\ce{X -> E}, && k_4 .
\end{aligned}
$$
The overall reaction is $\ce{A + B -> D + E}$; $\ce{A}$ and $\ce{B}$ are continuously replenished from outside with constant concentrations, and the products $\ce{D}$ and $\ce{E}$ are continuously removed, so the system is open. The second step is a termolecular autocatalytic step (in real oscillating reactions autocatalysis is built up from several elementary steps). All steps are treated as irreversible, which amounts to the system being infinitely far from equilibrium. Treating each step as an **elementary reaction**, the **rate equations** of X and Y follow from the **law of mass action**:

$$
\frac{\mathrm{d}[\ce{X}]}{\mathrm{d}t} = k_1[\ce{A}] - k_3[\ce{B}][\ce{X}] + k_2[\ce{X}]^2[\ce{Y}] - k_4[\ce{X}], \qquad
\frac{\mathrm{d}[\ce{Y}]}{\mathrm{d}t} = k_3[\ce{B}][\ce{X}] - k_2[\ce{X}]^2[\ce{Y}].
$$
Let $\tau = k_4t$, $[\ce{X}] = \sqrt{k_4/k_2}\,x$, $[\ce{Y}] = \sqrt{k_4/k_2}\,y$; the equations become the dimensionless form with only two parameters

$$
\dot x = a - (b + 1)x + x^2y, \qquad \dot y = bx - x^2y,
\tag{18.14}
$$
where $a = (k_1[\ce{A}]/k_4)\sqrt{k_2/k_4}$, $b = k_3[\ce{B}]/k_4$, and the dot denotes differentiation with respect to $\tau$.

**Example 18.3.1** Find the steady state of Eq. (18.14) and analyze its stability.

Solution: Setting the right-hand sides to zero, the second equation gives $x^2y = bx$, and substituting into the first gives $a - x = 0$; the unique steady state (**equilibrium point**) is $(x^*, y^*) = (a, b/a)$. The **Jacobian matrix** at this point is

$$
J = \begin{bmatrix} b - 1 & a^2 \\ -b & -a^2 \end{bmatrix}, \qquad
\operatorname{tr}J = b - 1 - a^2, \qquad \det J = a^2 > 0 .
$$
By the linearization criterion (Lyapunov's first method, [2.4.11](/2.4.11#sec-11.3)), when $\det J > 0$ the steady state is asymptotically stable if $\operatorname{tr}J < 0$ and unstable if $\operatorname{tr}J > 0$. The steady state is therefore stable for

$$
b < b_{\mathrm{c}} = 1 + a^2
$$
and unstable for $b > b_{\mathrm{c}}$. At $b = b_{\mathrm{c}}$ the pair of complex conjugate eigenvalues $\lambda = \frac12\operatorname{tr}J \pm \mathrm{i}\sqrt{\det J - (\operatorname{tr}J)^2/4}$ of $J$ crosses the imaginary axis with speed $\mathrm{d}(\operatorname{Re}\lambda)/\mathrm{d}b = \frac12 \ne 0$, which is exactly the condition for a Hopf bifurcation ([2.4.11](/2.4.11#sec-11.6.4)). At the bifurcation point the eigenvalues are $\pm\mathrm{i}a$, and the small-amplitude oscillation produced has period about $2\pi/a$.

For $b > b_{\mathrm{c}}$ the steady state is unstable, but the trajectories do not run off to infinity: one can construct a bounded region in the phase plane that contains the steady state and that trajectories enter and never leave; the only equilibrium point in the region is unstable, so by [the Poincaré–Bendixson theorem of 2.4.11](/2.4.11#thm-11.6.1) the region contains a closed orbit, that is, a stable **limit cycle**. Numerical computation shows that it is the unique limit cycle and attracts all nearby trajectories: whatever the initial concentrations, the system finally enters an oscillation of the same amplitude and period. This is the essential difference between chemical oscillation and an undamped harmonic oscillator (or the Lotka–Volterra model): for the latter the amplitude is determined by the initial conditions and does not recover after a perturbation; the amplitude and period of a limit cycle are determined by the system itself and form a robust "chemical clock".

![Behavior of the Brusselator (a = 1) on the two sides of the Hopf point: concentrations against time (top); trajectories, nullclines and limit cycle in the phase plane (bottom)](./plots/brusselator-oscillation.py)

The figure also shows the shape of the oscillation at larger $b$: $y$ accumulates slowly, while $x$ bursts suddenly through autocatalysis and falls back rapidly; this "slow accumulation, fast release" relaxation oscillation is a common feature of many chemical and biological oscillators. The bifurcation diagram shows how the amplitude varies with the control parameter: just after $b$ passes $b_{\mathrm{c}}$ the amplitude grows continuously from zero (roughly $\propto\sqrt{b - b_{\mathrm{c}}}$, a supercritical Hopf bifurcation), and the period grows from the value $2\pi/a$ of the linear theory.

![Hopf bifurcation of the Brusselator (a = 1): maximum and minimum of x on the attractor against b (left); period of the limit cycle against b (right)](./plots/brusselator-bifurcation.py)

From the thermodynamic point of view, the control parameter $b \propto [\ce{B}]$ measures how far the system is from equilibrium: for $b < b_{\mathrm{c}}$ the system stays on the thermodynamic branch, where the entropy production may be large but the system is macroscopically uniform and at rest; for $b > b_{\mathrm{c}}$ the thermodynamic branch becomes unstable and oscillation appears. If all four steps were written as reversible and $\ce{A}$, $\ce{B}$, $\ce{D}$, $\ce{E}$ were brought near their equilibrium proportions, the oscillation would disappear, by the argument at the end of 18.3.1.

### 18.3.3. The BZ Reaction and Biological Oscillations

In 1951 Belousov discovered that when citric acid is oxidized by potassium bromate in sulfuric acid with cerium ion as catalyst, the color of the solution changes periodically between colorless ($\ce{Ce^3+}$) and yellow ($\ce{Ce^4+}$). It was then widely believed that this violated the second law, his paper was rejected, and it was published only in 1959, as an abstract. In the 1960s Zhabotinsky replaced citric acid by malonic acid and later used ferroin (red/blue) as catalyst and indicator, making the phenomenon clearly visible; such reactions are collectively called the *Belousov–Zhabotinsky reaction*, or BZ reaction for short. Field, Kőrös and Noyes (1972) gave its mechanism (the FKN mechanism), which can be summarized in three processes:

1. Process A: when the concentration of $\ce{Br-}$ is high, bromate is reduced by $\ce{Br-}$, $\ce{BrO3- + 2Br- + 3H+ -> 3HOBr}$ (via intermediates such as $\ce{HBrO2}$), consuming $\ce{Br-}$;
2. Process B: when $\ce{Br-}$ drops below a critical concentration, the autocatalytic formation of bromous acid $\ce{HBrO2}$ takes over, with net reaction $\ce{BrO3- + HBrO2 + 3H+ + 2Ce^3+ -> 2HBrO2 + 2Ce^4+ + H2O}$; $\ce{HBrO2}$ grows exponentially and the catalyst is rapidly oxidized (a sudden color change);
3. Process C: $\ce{Ce^4+}$ oxidizes malonic acid and its brominated derivatives and is reduced to $\ce{Ce^3+}$, releasing $\ce{Br-}$; once $\ce{Br-}$ has accumulated, process A dominates again and suppresses the autocatalysis.

$\ce{Br-}$ acts as a delayed negative feedback and $\ce{HBrO2}$ supplies the autocatalytic positive feedback; together they give oscillation. The Oregonator model, obtained by simplifying the FKN mechanism to five steps, is mathematically of the same kind as the Brusselator. In an unstirred thin layer of solution, a local autocatalytic burst is passed on to neighboring regions by diffusion and forms outward-propagating concentric waves (target waves) and spiral waves, the "Zhabotinsky patterns". Waves in such excitable media are common in biology: spiral waves in cardiac muscle are related to arrhythmia, and cAMP signals form spiral waves when *Dictyostelium discoideum* aggregates.

Oscillations in living organisms are equally common. In yeast cells and their extracts the concentrations of glycolytic intermediates (such as NADH) oscillate with periods of tens of seconds to minutes, called *glycolytic oscillation*. The key is phosphofructokinase (PFK): its product ADP (and the AMP formed from it) is an allosteric activator of the enzyme, forming an autocatalytic-type positive feedback. Other examples include oscillations of the intracellular $\ce{Ca^2+}$ concentration, the cell cycle, and the circadian clock formed by delayed negative feedback of gene transcription and translation. Their mathematical structure is the same as that of the Brusselator: an open system (with a continuous supply of glucose and ATP), far from equilibrium, with nonlinear feedback, and oscillation appears when a control parameter crosses a Hopf bifurcation; the continuous dissipation of energy is the price paid for a biological clock to keep running. A systematic mathematical discussion is in [Systems Biology](/7.9).

### 18.3.4. Turing Patterns

In his 1952 paper "The Chemical Basis of Morphogenesis", Turing proposed that if two interacting substances diffuse at sufficiently different rates, a uniform state that is stable to begin with can become unstable because of diffusion and spontaneously form a stationary spatially periodic pattern. This is counterintuitive, since diffusion normally makes everything uniform. Placing the Brusselator in space, with X and Y diffusing at the same time, gives the **reaction-diffusion equations**

$$
\frac{\partial x}{\partial t} = a - (b + 1)x + x^2y + D_x\Delta x, \qquad
\frac{\partial y}{\partial t} = bx - x^2y + D_y\Delta y .
\tag{18.15}
$$
Add to the uniform steady state $(a, b/a)$ a perturbation proportional to $\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r} + \lambda t}$; the growth rate $\lambda$ is an eigenvalue of the matrix $J - q^2\operatorname{diag}(D_x, D_y)$ ($q = \lvert\boldsymbol{q}\rvert$). It was derived in [2.5.7](/2.5.7#sec-7.5.2) that when $\operatorname{tr}J < 0$ and $\det J > 0$ (the uniform system is stable), instability occurs when

$$
h(q^2) = D_xD_yq^4 - (D_yJ_{11} + D_xJ_{22})q^2 + \det J
$$
becomes negative for some $q$, the condition being $D_yJ_{11} + D_xJ_{22} > 2\sqrt{D_xD_y\det J}$.

**Example 18.3.2** Find the condition for the Turing instability of the Brusselator and the characteristic wavelength of the pattern.

Solution: $J_{11} = b - 1$, $J_{22} = -a^2$ and $\det J = a^2$. The condition becomes $D_y(b - 1) - D_xa^2 > 2a\sqrt{D_xD_y}$; dividing both sides by $D_y$ and writing $\eta = \sqrt{D_x/D_y}$:

$$
b - 1 > 2a\eta + a^2\eta^2 \quad\Longleftrightarrow\quad b > b_{\mathrm{T}} = (1 + a\eta)^2 .
$$
At the threshold the minimum of $h$ is at $q_{\mathrm{c}}^2 = \sqrt{\det J/(D_xD_y)} = a/\sqrt{D_xD_y}$, and the characteristic wavelength of the pattern is $2\pi/q_{\mathrm{c}}$, determined by the reaction rates and diffusion coefficients and independent of the size of the container. For the Turing instability to appear before the Hopf instability ($b_{\mathrm{T}} < b_{\mathrm{c}} = 1 + a^2$) we need $(1 + a\eta)^2 < 1 + a^2$, that is, $\eta < (\sqrt{1 + a^2} - 1)/a$: the inhibitor Y must diffuse much faster than the activator X. Taking $a = 4.5$, $D_x = 2$ and $D_y = 16$ gives $\eta = 0.354$ and $b_{\mathrm{T}} = 6.71$, far below $b_{\mathrm{c}} = 21.25$.

![Turing instability of the Brusselator (a = 4.5, Dx = 2, Dy = 16): growth rate of perturbations against wavenumber for different b (left); two-dimensional pattern grown from tiny random perturbations at b = 7.5 (right)](./plots/brusselator-turing.py)

Physically, X is a slowly diffusing autocatalytic "activator" and Y a rapidly diffusing "inhibitor" (the growth of X consumes Y, and the decrease of Y in turn limits X): a local fluctuation of X amplifies itself, while the deficit of Y that it causes diffuses quickly to the surroundings and inhibits X there, so that peaks with a definite spacing form. The two-dimensional simulation in the figure starts from the uniform state with a random perturbation of $10^{-2}$ and grows into a "labyrinth" pattern of interwoven stripes and spots; the detailed arrangement of the pattern is determined by the initial fluctuations and the wavelength by $q_{\mathrm{c}}$, which is exactly the feature of dissipative structures: "triggered by fluctuations, selected by the system".

The experimental confirmation of Turing patterns came nearly 40 years later: the difficulty is that the diffusion coefficients of small molecules in solution are all close to each other (about $10^{-9}\,\mathrm{m^2\,s^{-1}}$). In 1990 De Kepper and coworkers obtained the first stable Turing patterns in a gel reactor with the chlorite–iodide–malonic acid (CIMA) reaction: iodide ion forms a complex with the starch in the gel, which greatly slows its effective diffusion and satisfies the condition on the difference of diffusion coefficients. In biology, the Turing mechanism (or its generalizations: intercellular signaling, mechanical feedback) is used to explain the patterns on animal coats and fish skin, the spacing of hair follicle and feather primordia, and the periodic arrangement of digit bones; the "activator" and "inhibitor" in these systems are often secreted signaling proteins, or the interacting cells themselves. Pattern formation in development is discussed in [Developmental Biology](/7.5), and patterns in predator–prey systems in [Ecology](/7.19).

## 18.4. Thermodynamics of Living Systems

### 18.4.1. Life Feeds on Negative Entropy

In *What Is Life?* (1944) Schrödinger wrote that "life feeds on negative entropy": an organism offsets its own entropy production and maintains a highly ordered state by continually drawing *negentropy* from the environment, that is, by exporting entropy to the environment. In the language of this chapter an organism is an open system in a nonequilibrium steady state:

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = \frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} + \frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} \approx 0, \qquad \frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} > 0, \qquad \frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} < 0 .
$$
It takes in matter of low entropy (carbohydrates, $\ce{O2}$) and expels matter of high entropy ($\ce{CO2}$, water and other excreta) and heat. Take the complete oxidation of glucose as an example ($298\,\mathrm{K}$ standard state, CRC data): $\ce{C6H12O6(s) + 6O2(g) -> 6CO2(g) + 6H2O(l)}$, $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -2803\,\mathrm{kJ\,mol^{-1}}$, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = +259\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -2879\,\mathrm{kJ\,mol^{-1}}$. If all this free energy is dissipated, each mole of glucose produces at $310\,\mathrm{K}$ an entropy of about $2879/310 \approx 9.3\,\mathrm{kJ\,K^{-1}}$, of which the entropy increase of the matter itself is only $0.26\,\mathrm{kJ\,K^{-1}}$ and the vast majority is exported to the environment in the form of heat ($\lvert\Delta H\rvert/T$). Evidently the main way in which an organism exports entropy is by releasing heat, and the source of "negative entropy" is the usable Gibbs free energy in food. The basal metabolic power of a resting adult is about $100\,\mathrm{W}$, corresponding to a rate of entropy production of about $100/310 \approx 0.3\,\mathrm{W\,K^{-1}}$.

The food chain starts with photosynthesis, $\ce{6CO2(g) + 6H2O(l) -> C6H12O6(s) + 6O2(g)}$, $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = -259\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +2879\,\mathrm{kJ\,mol^{-1}}$: it is driven by light ($W' \ne 0$) and produces matter of low entropy and high free energy. The "negative entropy" of photosynthesis ultimately comes from solar radiation: the Earth absorbs radiation from the solar surface at about $5800\,\mathrm{K}$ and emits the same amount of energy as infrared **thermal radiation** at about $255\,\mathrm{K}$; the entropy flow of radiation is $\frac43E/T$, so for every $1\,\mathrm{J}$ of energy absorbed and re-emitted the Earth exports a net entropy of about $\frac43(1/255 - 1/5800) \approx 5\times10^{-3}\,\mathrm{J\,K^{-1}}$ to space. The atmospheric circulation, the water cycle and all the activities of life on Earth take place between this exit of entropy and the Sun, the entrance of low entropy.

### 18.4.2. The Cell: An Open System Far from Equilibrium

The nonequilibrium nature of a cell can be seen at every level:

- Energy currency: the ATP/ADP concentration ratio is maintained about $10^9$ times above its equilibrium value ([6.3.7](/6.3.7#sec-7.6.2)), and the affinity of ATP hydrolysis, about $50\,\mathrm{kJ\,mol^{-1}}$, is the unified "force" that drives other processes.
- Transport: transmembrane ion gradients and the membrane potential (18.2.5) are nonequilibrium steady states maintained by ion pumps; a nerve impulse is the rapid local release of this stored electrochemical potential energy, and the resting potential has to be restored by the sodium–potassium pump continuously dissipating ATP.
- Timing and patterns: biological oscillations and patterns in development (18.3) are all dissipative structures.
- Accuracy: Hopfield (1974) pointed out that the error rates of protein synthesis and DNA replication (about $10^{-4}$ and below $10^{-8}$) are far lower than the equilibrium discrimination $\mathrm{e}^{-\Delta\Delta G/RT}$ that the difference $\Delta\Delta G$ of the binding free energies of the correct and incorrect substrates alone could achieve. Cells let the substrate pass through several "proofreading" steps by means of irreversible steps that consume GTP or ATP, called *kinetic proofreading*; the discrimination of the individual steps multiplies, at the cost of energy dissipation. The trade-off among accuracy, speed and dissipation is a central problem of contemporary biophysics.

### 18.4.3. Entropy and Information

The word "entropy" now has three meanings:

1. Clausius entropy: the state function defined by $\mathrm{d}S = \delta Q_{\mathrm{r}}/T$, which determines the direction of macroscopic processes ([5.2.4](/5.2.4), [6.3.2](/6.3.2));
2. Boltzmann entropy: $S = k_{\mathrm{B}}\ln\Omega$, which measures the number of microstates corresponding to a macrostate, that is, the degree of disorder ([5.2.4](/5.2.4#fml-4.8.1), [6.3.10](/6.3.10));
3. Shannon entropy (1948): $H = -\sum_i p_i\log_2 p_i$, which measures the uncertainty about the state of a system, that is, the amount of information needed to obtain complete knowledge ([4.5.6](/4.5.6)); its generalization to quantum systems is the von Neumann entropy.

The three are unified in statistical mechanics: the Gibbs entropy $S = -k_{\mathrm{B}}\sum_i p_i\ln p_i$ equals the Clausius entropy for the equilibrium distribution, reduces to the Boltzmann entropy for equal probabilities, and differs from the Shannon entropy only by a factor $k_{\mathrm{B}}\ln 2$. The processing of information therefore has a thermodynamic cost. *Landauer's principle*, proposed in 1961, states that erasing 1 bit of information at temperature $T$ dissipates at least $k_{\mathrm{B}}T\ln 2$ of heat to the environment (about $3\times10^{-21}\,\mathrm{J}$ at $310\,\mathrm{K}$, roughly $1/30$ of the free energy of ATP hydrolysis). This principle resolves the paradox of "Maxwell's demon": in order to sort the molecules the demon must record, and eventually erase, information, and the entropy thereby produced is no less than the entropy by which it reduces that of the gas. A cell that senses its environment, replicates genetic information and makes decisions operates above this thermodynamic lower bound; from this point of view life is both a dissipative structure and a machine that processes information at the cost of energy dissipation.

## Summary

| Topic | Key points |
|---|---|
| Entropy flow and entropy production | $\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S$; $\mathrm{d}_{\mathrm{i}}S \ge 0$ holds for any system and also locally; the entropy of an open system can decrease as long as the negative entropy flow is large enough |
| Chemical reactions | Affinity $\mathcal{A} = -\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$, entropy production $\mathcal{A}\,\mathrm{d}\xi/T$; at constant temperature and pressure $T\,\mathrm{d}_{\mathrm{i}}S = -\mathrm{d}G$ |
| Local equilibrium and entropy balance | $\partial s/\partial t = -\nabla\cdot\boldsymbol{J}_S + \sigma$, $\sigma = \sum J_kX_k \ge 0$; forces: $\nabla(1/T)$, $-\nabla\mu_{\mathrm{B}}/T$, $\boldsymbol{E}/T$, $\mathcal{A}/T$ |
| Linear region | $J_k = \sum L_{kl}X_l$, the symmetric part of $L$ is positive semidefinite; chemical reactions are linear only for $\lvert\mathcal{A}\rvert \ll RT$ |
| Onsager reciprocal relations | $L_{kl} = L_{lk}$ ($L_{kl}(\boldsymbol{B}) = L_{lk}(-\boldsymbol{B})$ in a magnetic field), based on microscopic reversibility and regression of fluctuations; example: $\Pi = T\alpha_{\mathrm{S}}$ |
| Curie principle | In isotropic media tensors of different rank do not couple; driving directed transport by a chemical reaction requires oriented membrane proteins |
| Membrane transport | $J_V = L_p(\Delta p - \sigma_{\mathrm{r}}\Delta\varPi)$, $J_{\mathrm{s}} = \omega\Delta\varPi + (1 - \sigma_{\mathrm{r}})\bar c_{\mathrm{s}}J_V$ |
| Energy coupling | Degree of coupling $q = L_{12}/\sqrt{L_{11}L_{22}}$, $\eta_{\max} = q^2/(1 + \sqrt{1 - q^2})^2$; sodium–potassium pump about $44\,\mathrm{kJ\,mol^{-1}}$ against ATP about $53\,\mathrm{kJ\,mol^{-1}}$ |
| Principle of minimum entropy production | In the linear region with constant coefficients, reciprocal relations and steady boundary conditions, the steady state minimizes $P$ and is stable; no ordered structure arises in the linear region |
| Dissipative structures | Open, far from equilibrium, nonlinear (autocatalysis), fluctuations; maintained by continuous dissipation |
| Brusselator | Steady state $(a, b/a)$; Hopf bifurcation at $b > 1 + a^2$ with a stable limit cycle |
| Turing patterns | $b > (1 + a\sqrt{D_x/D_y})^2$; wavelength $2\pi/q_{\mathrm{c}}$, $q_{\mathrm{c}}^2 = a/\sqrt{D_xD_y}$; the inhibitor must diffuse much faster |
| Living systems | Open systems in nonequilibrium steady states; entropy is exported mainly as heat; ATP, ion gradients, oscillations and proofreading all cost dissipation |

## Questions

1. A cup of hot water cools at room temperature and its entropy decreases. Analyze this process using $\mathrm{d}_{\mathrm{e}}S$ and $\mathrm{d}_{\mathrm{i}}S$ and indicate where the entropy production occurs.

   **Answer** Take the water as the system, with a roughly uniform temperature $T_{\mathrm{w}}$. The water releases heat, $\delta Q < 0$, so the entropy flow is $\mathrm{d}_{\mathrm{e}}S = \delta Q/T_{\mathrm{w}} < 0$; temperature differences inside the water are small, so $\mathrm{d}_{\mathrm{i}}S \approx 0$ and $\mathrm{d}S \approx \delta Q/T_{\mathrm{w}} < 0$, in no conflict with Theorem 18.1.1. The entropy is produced where the temperature drops from $T_{\mathrm{w}}$ to the room temperature $T_0$, that is, in the wall of the cup and in the air boundary layer above the water surface and outside the cup: just as for the conducting rod of Example 18.1.1, this layer produces entropy $\lvert\delta Q\rvert(1/T_0 - 1/T_{\mathrm{w}}) > 0$ for every $\lvert\delta Q\rvert$ of heat passed through it. The entropy gained by the surroundings, $\lvert\delta Q\rvert/T_0$, exceeds the entropy lost by the water, and the total entropy of water, boundary layer and surroundings increases.

2. Why is the Gibbs free energy criterion a special case of Theorem 18.1.1? How should the entropy production be written at constant temperature and volume when the non-volume work is nonzero (such as the electrical work done by a discharging battery)?

   **Answer** For a closed system at constant temperature and pressure with only volume work, $\delta Q = \mathrm{d}H$ and $\mathrm{d}_{\mathrm{e}}S = \mathrm{d}H/T$, so $T\,\mathrm{d}_{\mathrm{i}}S = T\,\mathrm{d}S - \mathrm{d}H = -\mathrm{d}G$; the statement $\mathrm{d}_{\mathrm{i}}S \ge 0$ is exactly $\mathrm{d}G \le 0$, which is the relation $T\,\mathrm{d}_{\mathrm{i}}S = \mathcal{A}\,\mathrm{d}\xi = -\mathrm{d}G$ of Section 18.1.3.

   At constant temperature and volume, with non-volume work $\delta W'$ done on the system by the surroundings, $\mathrm{d}U = \delta Q + \delta W'$ and $\mathrm{d}_{\mathrm{e}}S = \delta Q/T$, so

   $$
   T\,\mathrm{d}_{\mathrm{i}}S = T\,\mathrm{d}S - \mathrm{d}U + \delta W' = -\mathrm{d}A + \delta W' \ge 0 .
   $$
   For a cell in which a single reaction takes place, $-\mathrm{d}A = \mathcal{A}\,\mathrm{d}\xi$ at constant $T$ and $V$; on discharge the cell does electrical work $zFE_{\mathrm{cell}}\,\mathrm{d}\xi$ on the external circuit, i.e. $\delta W' = -zFE_{\mathrm{cell}}\,\mathrm{d}\xi$, and therefore

   $$
   \mathrm{d}_{\mathrm{i}}S = \frac{(\mathcal{A} - zFE_{\mathrm{cell}})\,\mathrm{d}\xi}{T} \ge 0 ,
   $$
   where $E_{\mathrm{cell}}$ is the voltage across the terminals during operation. In reversible discharge (current tending to zero) $E_{\mathrm{cell}} = \mathcal{A}/(zF)$, the entropy production vanishes and the electrical work is maximal, equal to $-\Delta A$; the larger the current, the lower the voltage and the larger the part of $\mathcal{A}$ dissipated as Joule heat and overpotential.

3. For $\ce{A <=> B}$ at $298\,\mathrm{K}$ let $\mathcal{A} = 5\,\mathrm{kJ\,mol^{-1}}$. Compute $v/v_+$ with the exact form of Eq. (18.9) and with the linear approximation; how large is the relative error of the linear approximation?

   **Answer** $\mathcal{A}/RT = 5000/(8.314 \times 298.15) = 2.017$. The exact form gives $v/v_+ = 1 - \mathrm{e}^{-2.017} = 0.867$; the linear approximation (taking $v_+$ as $v_{\mathrm{eq}}$ and $1 - \mathrm{e}^{-x} \approx x$) gives $v/v_+ \approx 2.017$, a relative error of $(2.017 - 0.867)/0.867 \approx 133\%$. The linear approximation even gives $v > v_+$, which is impossible (the reverse rate cannot be negative): $\mathcal{A} = 5\,\mathrm{kJ\,mol^{-1}}$ is about $2RT$, already outside the linear region.

4. If a transporter accompanies each glucose transported by only 1 $\ce{Na+}$, what is the maximum ratio of glucose concentrations inside and outside the cell, with the data of Example 18.2.2?

   **Answer** Glucose is uncharged, so at equilibrium its chemical potential difference $RT\ln(c_{\text{in}}/c_{\text{out}})$ equals the drop of the electrochemical potential of one $\ce{Na+}$ entering the cell, $13.2\,\mathrm{kJ\,mol^{-1}}$; hence $c_{\text{in}}/c_{\text{out}} \le \exp(13.2/2.58) \approx 1.7\times10^2$. This is two orders of magnitude below the value of about $3\times10^4$ for 2 $\ce{Na+}$: the stoichiometry enters the exponent, which is why the transporter of the intestinal epithelium uses a 2:1 stoichiometry.

5. For the Brusselator with $a = 2$, at what value of $b$ does the Hopf bifurcation occur? What is the approximate period of the oscillation near the bifurcation point (in dimensionless time)?

   **Answer** $b_{\mathrm{c}} = 1 + a^2 = 5$. At the bifurcation point the eigenvalues are $\pm\mathrm{i}a = \pm 2\mathrm{i}$, so the period is about $2\pi/a = \pi \approx 3.14$. A numerical integration confirms this: the period of the limit cycle is $3.19$ at $b = 5.05$ and grows to $3.98$ at $b = 5.5$, consistent with the statement in Section 18.3.2 that the period starts from $2\pi/a$ and increases.

6. Why do Turing patterns require the inhibitor to diffuse faster than the activator? If $D_x = D_y$, can the Brusselator show a Turing instability?

   **Answer** The activator X is autocatalytic ($J_{11} > 0$), so a local fluctuation amplifies itself; for it to form isolated peaks rather than grow everywhere, the inhibitor must carry its suppressing effect quickly to the neighborhood ("short-range activation, long-range inhibition"), which requires $D_y > D_x$. Mathematically, stability of the homogeneous system requires $\operatorname{tr}J = J_{11} + J_{22} < 0$, while the Turing instability requires $D_yJ_{11} + D_xJ_{22} > 0$; both can hold only if $D_y/D_x > -J_{22}/J_{11} > 1$.

   If $D_x = D_y = D$, the eigenvalues of $J - q^2DI$ are those of $J$ shifted by $-Dq^2$, so every mode with $q \ne 0$ decays faster than the homogeneous mode and no Turing instability is possible. The result of Example 18.3.2 shows the same: with $\eta = 1$, $b_{\mathrm{T}} = (1 + a)^2 > 1 + a^2 = b_{\mathrm{c}}$, so as $b$ increases the Hopf instability always comes first.
