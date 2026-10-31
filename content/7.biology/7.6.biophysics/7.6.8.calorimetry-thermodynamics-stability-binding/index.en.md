---
title: "Solution Methods: Calorimetry and Hydrodynamics"
description: "Solution methods of molecular biophysics. Calorimetry: signals and sensitivity; differential scanning calorimetry, excess heat capacity and the fluctuation formula; two-state thermograms and the van 't Hoff to calorimetric enthalpy ratio; multistate deconvolution; stability decomposition, cold denaturation, heat capacity and buried surface; T_m shifts and thermal shift assays; isothermal titration calorimetry, the Wiseman c value, linked protonation and enthalpy–entropy compensation; lipid phase transitions. Hydrodynamics: partial specific volume and hydration; friction, hydrodynamic radius and Perrin factors; rotational diffusion and birefringence; sedimentation velocity, the Svedberg and Lamm equations; sedimentation equilibrium, self-association and density gradients; intrinsic viscosity and Simha factors; dynamic light scattering, the Siegert relation and cumulant analysis."
---

Every measurement of the stability of a protein or of the strength of a binding interaction is in the end a measurement of a free energy, and free energies are what thermodynamics relates to heat. Most methods infer $\Delta G$ indirectly, from a spectroscopic signal that reports the populations of two states, and then obtain the enthalpy from the temperature dependence of $\Delta G$ through the **van 't Hoff equation**. Calorimetry measures the heat itself. A differential scanning calorimeter records the **heat capacity** of a dilute protein solution as it is heated through unfolding, and its integral is the enthalpy of unfolding with no model assumed; an isothermal titration calorimeter measures the heat released by each small addition of a ligand, and a single experiment gives the stoichiometry, the binding constant and the binding enthalpy. Comparing the calorimetric enthalpy with the one implied by the shape of a transition tests whether the transition is two-state, which no spectroscopic method can do alone. The second half of the chapter measures motion instead of heat. How fast a macromolecule sediments in a centrifugal field, diffuses, tumbles or thickens a solution depends on its mass, size and shape, and the analytical ultracentrifuge, viscometry and dynamic light scattering turn these dependences into the molar mass, oligomeric state, hydrodynamic radius and degree of elongation of molecules in their working solvent.

The thermodynamics used here (the **Gibbs–Helmholtz equation**, **enthalpy**, **entropy** and heat capacity) is that of [6.3](/6.3), and calorimeters were introduced in [6.3.1](/6.3.1#sec-1.7); the **two-state model** of unfolding, the **protein stability curve** and chemical denaturation were derived in [7.1.6](/7.1.6#sec-6.2). The hydrodynamics rests on Brownian motion and the Stokes–Einstein equation ([6.3.21](/6.3.21), [7.6.5](/7.6.5)). This chapter is about measurement: what a calorimeter or a centrifuge records, how the records are analyzed, what the numbers mean physically, and how experiments are designed. The same quantities return in the folding chapter ([7.6.16](/7.6.16)), in molecular recognition ([7.6.17](/7.6.17)) and, for the lipid phase transition, in the physics of membranes ([7.6.24](/7.6.24)); static light scattering and small-angle scattering, which measure the average rather than the fluctuations of scattered light, follow in [7.6.9](/7.6.9), and low-Reynolds-number hydrodynamics in [7.6.22](/7.6.22).

## 8.1. Measuring Heat in Solution

### 8.1.1. Signals and Sensitivity

Biological calorimetry is difficult because the heats are tiny compared with the heat capacity of the solvent.

**Example 8.1.1** A $1\,\mathrm{mL}$ cell contains a $1\,\mathrm{mg\,mL^{-1}}$ solution of a $20\,\mathrm{kDa}$ protein, $5\times10^{-8}\,\mathrm{mol}$. Unfolding with $\Delta_{\mathrm{U}}H = 300\,\mathrm{kJ\,mol^{-1}}$ absorbs $15\,\mathrm{mJ}$, spread over about $10\,\mathrm{K}$. At the peak, the excess heat capacity of a two-state protein is $\Delta H^2/(4RT_{\mathrm{m}}^2) = 24\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$ (Formula 8.2.2), so the protein adds $1.2\,\mathrm{mJ\,K^{-1}}$ to the $4.2\,\mathrm{J\,K^{-1}}$ of the water in the cell: three parts in ten thousand. Scanning at $1\,\mathrm{K\,min^{-1}}$ the extra heating power is $1.2\,\mathrm{mJ\,K^{-1}} \times \tfrac{1}{60}\,\mathrm{K\,s^{-1}} = 20\,\mu\mathrm{W}$.

Instruments that resolve fractions of a microwatt therefore never measure the absolute heat capacity of a sample. They measure the difference between a sample cell and a reference cell filled with the same buffer, held at the same temperature by feedback heaters inside an adiabatic shield, so that everything except the solute cancels.

### 8.1.2. The Differential Scanning Calorimeter

In a differential scanning calorimeter (**differential scanning calorimetry**, DSC) two identical cells of $0.1$–$0.5\,\mathrm{mL}$ are heated at a constant rate $\beta = \mathrm{d}T/\mathrm{d}t$, typically $0.5$–$2\,\mathrm{K\,min^{-1}}$, and slightly pressurized (to about $0.3\,\mathrm{MPa}$) so that dissolved gas does not form bubbles. A thermopile measures the temperature difference between the cells, and a feedback heater supplies the extra power $\Delta P$ that keeps it at zero.

**Definition 8.1.1 (Excess Heat Capacity)** The difference between the heat capacity of the solution and that of the same volume of buffer, divided by the amount of solute, is the apparent molar heat capacity of the solute; its part that exceeds the heat capacity of the native state (the native baseline) is the **excess heat capacity**,

$$
C_{p,\mathrm{ex}}(T) = \frac{\Delta P(T)}{\beta\, n} - C_{p,\mathrm{N}}(T),
$$
where $n$ is the amount of solute in the cell. The integral of $C_{p,\mathrm{ex}}$ over the transition, after the baseline is subtracted, is the calorimetric enthalpy $\Delta H_{\mathrm{cal}}$.

A measurement consists of buffer–buffer scans, which define the instrumental baseline, followed by buffer–sample scans; the difference is converted to molar heat capacity with the protein concentration, which is therefore one of the main sources of error (a $5\,\%$ error in concentration is a $5\,\%$ error in $\Delta H_{\mathrm{cal}}$). A second scan of the same sample after cooling shows whether the transition is reversible: proteins that aggregate after unfolding give a smaller or no peak on rescanning.

## 8.2. Differential Scanning Calorimetry of Protein Unfolding

### 8.2.1. Heat Capacity as Enthalpy Fluctuation

A calorimeter is a fluctuation meter. The connection is a basic result of statistical mechanics.

**Theorem 8.2.1 (Heat Capacity and Enthalpy Fluctuations)** For a system at constant pressure in equilibrium with a heat bath at temperature $T$,

$$
C_p = \left(\frac{\partial\langle H\rangle}{\partial T}\right)_p = \frac{\langle H^2\rangle - \langle H\rangle^2}{k_{\mathrm{B}}T^2} \geq 0 .
$$

**Proof** In the isothermal–isobaric ensemble the states $j$ have enthalpies $H_j$ and probabilities $p_j = \mathrm{e}^{-\beta H_j}/\Delta$ with $\Delta = \sum_j \mathrm{e}^{-\beta H_j}$ and $\beta = 1/k_{\mathrm{B}}T$ (the **partition function** of this ensemble). Then $\langle H\rangle = -\partial\ln\Delta/\partial\beta$ and

$$
\frac{\partial\langle H\rangle}{\partial\beta} = -\frac{\partial^2\ln\Delta}{\partial\beta^2} = -\left(\langle H^2\rangle - \langle H\rangle^2\right).
$$
Since $\partial\beta/\partial T = -1/(k_{\mathrm{B}}T^2)$, $C_p = \partial\langle H\rangle/\partial T = (\langle H^2\rangle - \langle H\rangle^2)/(k_{\mathrm{B}}T^2)$, a variance divided by a positive number. $\square$

For a protein solution the theorem has a direct reading. Away from a transition the heat capacity comes from small fluctuations of the native or unfolded state. Inside a transition, molecules jump between N and U, whose enthalpies differ by $\Delta H$, and these large fluctuations of the enthalpy appear as the heat-capacity peak.

**Formula 8.2.1 (Two-State Thermogram)** For N ⇌ U with $K = [\mathrm{U}]/[\mathrm{N}] = \mathrm{e}^{-\Delta_{\mathrm{U}}G/RT}$, $f = K/(1 + K)$ and $\Delta_{\mathrm{U}}H(T) = \Delta H_{\mathrm{m}} + \Delta C_p(T - T_{\mathrm{m}})$, the molar enthalpy is $\langle H\rangle = H_{\mathrm{N}} + f\,\Delta_{\mathrm{U}}H$, and the excess heat capacity is

$$
C_{p,\mathrm{ex}}(T) = f\,\Delta C_p + f(1 - f)\,\frac{\Delta_{\mathrm{U}}H(T)^2}{RT^2}.
$$
The first term is the progress baseline, which moves from the native to the unfolded baseline in proportion to the extent of unfolding; the second is the transition peak, the variance $f(1-f)\Delta H^2$ of Theorem 8.2.1 divided by $RT^2$.

The derivative $\mathrm{d}f/\mathrm{d}T = f(1-f)\,\Delta_{\mathrm{U}}H/(RT^2)$ that produces the peak is the van 't Hoff equation for $K$. The peak is highest close to $T_{\mathrm{m}}$, where $f = 1/2$, with height $\Delta H_{\mathrm{m}}^2/(4RT_{\mathrm{m}}^2)$, and its area is $\Delta H$: a protein with a larger unfolding enthalpy gives a peak that is both larger and narrower.

![Excess heat capacity of protein unfolding. A: a two-state protein (Tm = 60 °C, ΔHm = 350 kJ/mol, ΔCp = 6 kJ mol⁻¹ K⁻¹) from Formula 8.2.1; the shaded area above the progress baseline f ΔCp (dashed) is the calorimetric enthalpy, and the baseline steps by ΔCp between the native and unfolded states (dotted). B: three proteins with the same calorimetric enthalpy, 400 kJ per mole of polypeptide chains, analyzed in the same way: a single two-state domain; two independent two-state domains melting at 55 and 65 °C; a dimer that dissociates as it unfolds (N₂ ⇌ 2U, 50 µM chains). The van 't Hoff enthalpy from the peak height (Formula 8.2.2) divided by the calorimetric enthalpy is 1, 0.38 and 1.37. C: a simulated scan with sloping native baseline and Gaussian noise, fitted by nonlinear least squares with Formula 8.2.1 plus a linear baseline: the fit recovers Tm, ΔHm and ΔCp](./plots/dsc-thermograms.py)

### 8.2.2. The van 't Hoff Enthalpy

The shape of a transition and its area are two independent measures of the enthalpy. If the transition really is a two-state transition of the molecule whose concentration was used to normalize the data, they agree.

**Definition 8.2.1 (van 't Hoff Enthalpy)** The **van 't Hoff enthalpy** $\Delta H_{\mathrm{vH}}$ of a transition is the enthalpy that a two-state model must have to reproduce the observed temperature dependence of the populations, $\Delta H_{\mathrm{vH}} = RT^2\,\mathrm{d}\ln K/\mathrm{d}T$ evaluated at the midpoint; it is obtained from the shape of a transition curve or of a heat-capacity peak, independently of its area.

**Formula 8.2.2 (Ratio Test for Two-State Behavior)** If the excess heat-capacity peak has height $C_{\max}$ above the progress baseline at $T_{\max}$ and area $\Delta H_{\mathrm{cal}}$ (per mole of chains), then

$$
\Delta H_{\mathrm{vH}} = \frac{4RT_{\max}^2\,C_{\max}}{\Delta H_{\mathrm{cal}}}, \qquad r = \frac{\Delta H_{\mathrm{vH}}}{\Delta H_{\mathrm{cal}}} .
$$
A two-state transition has $r = 1$; $r < 1$ means that the molecule unfolds in more than one cooperative step (intermediates or independent domains); $r > 1$ means that the cooperative unit is larger than the chain (oligomers that dissociate on unfolding, or aggregation).

For two-state behavior the peak height is $\Delta H^2/(4RT_{\mathrm{m}}^2)$ and the formula returns $\Delta H$; for any other process it defines $\Delta H_{\mathrm{vH}}$ as the enthalpy of the hypothetical two-state process with the same peak. The ratio $1/r$ is a rough count of the cooperative units into which a chain melts: in panel B of the figure two equal domains give $r = 0.38$. Peter Privalov's DSC studies of the 1970s and 1980s used this test to show that small single-domain proteins are two-state to within the precision of the measurement ($r = 1.00 \pm 0.05$), while larger proteins melt domain by domain.

**Example 8.2.1** A $50\,\mathrm{kDa}$ protein gives $\Delta H_{\mathrm{cal}} = 600\,\mathrm{kJ\,mol^{-1}}$ and a peak of $25\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$ at $55\,^\circ\mathrm{C}$. Then $\Delta H_{\mathrm{vH}} = 4 \times 8.314 \times 328.15^2 \times 25\,000/600\,000\,\mathrm{J\,mol^{-1}} = 149\,\mathrm{kJ\,mol^{-1}}$ and $r = 0.25$: the protein does not unfold in one step, and a likely interpretation is three or four domains of similar stability whose transitions overlap.

### 8.2.3. Multistate Transitions and Deconvolution

When a transition is not two-state, the thermogram still contains the complete thermodynamics of the system, because it measures $\mathrm{d}\langle H\rangle/\mathrm{d}T$ and $\langle H\rangle$ determines the partition function.

**Formula 8.2.3 (Deconvolution of a Thermogram)** For states $i = 0, 1, \dots$ with equilibrium constants $K_i = \mathrm{e}^{-\Delta G_i/RT}$ relative to the native state ($K_0 = 1$), the partition function is $Q(T) = \sum_i K_i(T)$, the populations are $p_i = K_i/Q$, and

$$
\langle\Delta H\rangle(T) = \sum_i p_i\,\Delta H_i = RT^2\,\frac{\mathrm{d}\ln Q}{\mathrm{d}T}, \qquad
\langle\Delta H\rangle(T) = \int_{T_0}^{T} C_{p,\mathrm{ex}}\,\mathrm{d}T', \qquad
\ln Q(T) = \int_{T_0}^{T} \frac{\langle\Delta H\rangle(T')}{RT'^2}\,\mathrm{d}T' .
$$

Integrating a measured thermogram twice therefore gives $Q(T)$ without a model (Ernesto Freire and Rodney Biltonen, 1978). The number of states, their enthalpies and their populations follow by analyzing $Q$: if $\ln Q$ is fitted by a sum of exponentials in $1/T$, each term is a state. In practice the analysis is done by fitting models with a few states (sequential N ⇌ I ⇌ U, or independent domains with $Q = \prod_k(1 + K_k)$) directly to $C_{p,\mathrm{ex}}$; the deconvolution principle explains why such fits are meaningful.

### 8.2.4. Irreversible and Oligomeric Unfolding

Two complications are common in practice.

- *Irreversibility.* Many proteins aggregate or are chemically modified after they unfold. In the Lumry–Eyring scheme $\mathrm{N} \rightleftharpoons \mathrm{U} \to \mathrm{F}$, the final state F is formed irreversibly with rate constant $k$. If $k$ is slow compared with the scan, equilibrium thermodynamics still describes the peak; if it is fast, the apparent $T_{\mathrm{m}}$ depends on the scan rate and the peak is asymmetric. Two tests are a rescan after cooling and a series of scan rates; a $T_{\mathrm{m}}$ that rises with scan rate indicates kinetic control.
- *Dissociation.* For a dimer that unfolds as $\mathrm{N}_2 \rightleftharpoons 2\mathrm{U}$, the equilibrium constant $K = [\mathrm{U}]^2/[\mathrm{N}_2]$ has units of concentration, so the transition midpoint depends on the total concentration $C_{\mathrm{t}}$ of chains: at $f = 1/2$, $K = C_{\mathrm{t}}$, and $T_{\mathrm{m}}$ rises with concentration (by mass action, dilution favors dissociation). The transition is also sharper than that of a monomer with the same enthalpy per chain, which is the origin of $r > 1$ (panel B of the figure).

## 8.3. Stability, Heat Capacity and Buried Surface

### 8.3.1. The Thermodynamic Decomposition of Stability

The stability curve of [7.1.6](/7.1.6#sec-6.2.2) is the difference of two large and steeply temperature-dependent terms. With a constant $\Delta C_p$, the integrated Gibbs–Helmholtz equation ([Formula 6.2.1 of 7.1.6](/7.1.6#sec-6.2.2)) gives three characteristic temperatures besides $T_{\mathrm{m}}$.

**Formula 8.3.1 (Characteristic Temperatures of a Stability Curve)** For a protein with $T_{\mathrm{m}}$, $\Delta H_{\mathrm{m}}$ and constant $\Delta C_p > 0$:

$$
T_H = T_{\mathrm{m}} - \frac{\Delta H_{\mathrm{m}}}{\Delta C_p} \quad (\Delta_{\mathrm{U}}H = 0), \qquad
T_S = T_{\mathrm{m}}\,\exp\!\left(-\frac{\Delta H_{\mathrm{m}}}{T_{\mathrm{m}}\Delta C_p}\right) \quad (\Delta_{\mathrm{U}}S = 0), \qquad
\Delta_{\mathrm{U}}G(T_S) = \Delta C_p\,(T_S - T_H),
$$
and $T_S$ is the temperature of maximal stability. Below $T_S$ the unfolded state is favored by enthalpy and disfavored by entropy, above it the reverse.

The last relation follows from $\Delta G = \Delta H - T\Delta S$ at $T_S$, where $\Delta S = 0$ and $\Delta H = \Delta C_p(T_S - T_H)$. It shows that the maximal stability is set by the heat capacity and by how far apart $T_S$ and $T_H$ are, which is a few kelvin: $\Delta G_{\max}$ is a small residue of the large enthalpy and entropy.

![Thermodynamic decomposition of protein stability. A: unfolding enthalpy, entropy term and Gibbs energy of a protein with Tm = 60 °C, ΔHm = 350 kJ/mol and ΔCp = 6 kJ mol⁻¹ K⁻¹ (Formula 8.3.1). The enthalpy (red) and the entropy term (blue) change by hundreds of kJ/mol over the range and nearly cancel; ΔH = 0 at T_H = 1.7 °C and ΔS = 0 at T_S = 6.5 °C, where the stability is maximal (29 kJ/mol); ΔG = 0 at Tm and at the cold-denaturation temperature T_c = −44 °C. B: the same protein and a mutant destabilized by 5 kJ/mol at all temperatures: Tm falls by 5.0 K, close to the estimate ΔΔG·Tm/ΔHm = 4.8 K of Formula 8.3.2, and T_c rises by 4.4 K](./plots/stability-thermodynamics.py)

**Example 8.3.1** For the protein of the figure, $T_H = 333.15 - 350/6 = 274.8\,\mathrm{K}$ ($1.7\,^\circ\mathrm{C}$), $T_S = 333.15\,\mathrm{e}^{-350/(333.15\times6)} = 279.6\,\mathrm{K}$ ($6.5\,^\circ\mathrm{C}$) and $\Delta G_{\max} = 6 \times (279.6 - 274.8) = 29\,\mathrm{kJ\,mol^{-1}}$. At $37\,^\circ\mathrm{C}$, $\Delta_{\mathrm{U}}H = 350 + 6 \times (310.15 - 333.15) = 212\,\mathrm{kJ\,mol^{-1}}$ while $\Delta_{\mathrm{U}}G = 19\,\mathrm{kJ\,mol^{-1}}$: the stability is $9\,\%$ of the enthalpy.

The curvature of the stability curve forces a second crossing of zero below $T_S$.

**Definition 8.3.1 (Cold Denaturation)** **Cold denaturation** is the unfolding of a protein on cooling, at the lower temperature $T_c$ where its stability curve crosses zero again; it occurs because $\Delta_{\mathrm{U}}C_p > 0$ makes $\Delta_{\mathrm{U}}H$ negative below $T_H$, so that unfolding becomes enthalpically favorable at low temperature.

For most proteins $T_c$ lies below the freezing point of water, and cold denaturation was first observed calorimetrically by Privalov and colleagues in 1986 for myoglobin in the presence of moderate concentrations of denaturant, which raise $T_c$ and lower $T_{\mathrm{m}}$ until both transitions fall in the accessible range. Some proteins cold-denature without additives: the yeast frataxin homolog Yfh1 unfolds below about $5\,^\circ\mathrm{C}$ in low-salt buffer. Physically, cold denaturation is the hydrophobic effect run backwards: the ordering of water around exposed nonpolar groups, which makes their exposure entropically costly at room temperature, becomes enthalpically favorable at low temperature (**hydrophobic effect**, [7.1.2](/7.1.2)).

### 8.3.2. Heat Capacity and Accessible Surface

The positive $\Delta_{\mathrm{U}}C_p$ of unfolding is mainly a property of water. Transferring nonpolar compounds (benzene, alkanes) from the liquid hydrocarbon or the gas phase into water increases the heat capacity of the system, and transferring polar compounds (amides) decreases it, in proportion to the surface area of the solute that is exposed to water. Treating a protein as a collection of such groups (the liquid-hydrocarbon model, with a correction for polar groups) gives empirical relations between $\Delta C_p$ and the change in solvent-accessible surface area $\Delta\mathrm{ASA}$ computed from the structure.

**Formula 8.3.2 (Heat Capacity and Buried Surface)** With $\Delta\mathrm{ASA}$ in $\text{Å}^2$ and $\Delta C_p$ in $\mathrm{J\,mol^{-1}\,K^{-1}}$ (the original coefficients in $\mathrm{cal}$ multiplied by $4.184$):

$$
\Delta C_p \approx 1.34\,\Delta\mathrm{ASA}_{\mathrm{np}} - 0.59\,\Delta\mathrm{ASA}_{\mathrm{pol}} \quad \text{(Spolar, Livingstone and Record, 1992)},
$$
$$
\Delta C_p \approx 1.88\,\Delta\mathrm{ASA}_{\mathrm{np}} - 1.09\,\Delta\mathrm{ASA}_{\mathrm{pol}} \quad \text{(Murphy and Freire, 1992)},
$$
where np and pol denote nonpolar (carbon) and polar (nitrogen and oxygen) surface. For whole proteins, Myers, Pace and Scholtz (*Protein Science* 4, 2138, 1995) found $\Delta\mathrm{ASA} \approx -907 + 93N$ for $N$ residues and $\Delta_{\mathrm{U}}C_p \approx -1\,050 + 0.79\,\Delta\mathrm{ASA}$; the denaturant $m$-values ([7.1.6](/7.1.6#sec-6.2.3)) are likewise linear in $\Delta\mathrm{ASA}$.

**Example 8.3.2** For $N = 100$ residues, $\Delta\mathrm{ASA} = -907 + 9\,300 = 8\,393\,\text{Å}^2$ and $\Delta_{\mathrm{U}}C_p = -1\,050 + 0.79 \times 8\,393 = 5.6\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$, or $56\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per residue, the average quoted in [7.1.6](/7.1.6#sec-6.2.2) ($10$–$18\,\mathrm{cal}$, that is $42$–$75\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per residue). Proteins with disulfide bonds fall below the line, because cross-links keep the unfolded state more compact and reduce the surface that it exposes.

The same relations apply to binding. When two proteins associate, both lose accessible surface, so binding has $\Delta C_p < 0$; a measured $\Delta C_p$ of binding can therefore be compared with the surface buried in a crystal structure of the complex. A $\Delta C_p$ much more negative than the buried surface predicts suggests that binding is coupled to folding of part of the chain (Spolar and Record, 1994), as happens for many DNA-binding proteins.

### 8.3.3. Mutations and Ligands Shift the Melting Temperature

Because $\Delta_{\mathrm{U}}G$ crosses zero at $T_{\mathrm{m}}$ with slope $-\Delta S_{\mathrm{m}} = -\Delta H_{\mathrm{m}}/T_{\mathrm{m}}$, a small change in stability shifts $T_{\mathrm{m}}$ in proportion.

**Formula 8.3.3 (Stability Change from a Shift in T_m)** If a mutation or a solution condition changes the unfolding Gibbs energy by $\Delta\Delta G$ near $T_{\mathrm{m}}$ and leaves the enthalpy and heat capacity nearly unchanged,

$$
\Delta T_{\mathrm{m}} \approx \frac{T_{\mathrm{m}}\,\Delta\Delta G}{\Delta H_{\mathrm{m}}}, \qquad\text{equivalently}\qquad \Delta\Delta G(T_{\mathrm{m}}) \approx \Delta S_{\mathrm{m}}\,\Delta T_{\mathrm{m}}
$$
(Becktel and Schellman, 1987). A ligand that binds only the native state with dissociation constant $K_{\mathrm{d}}$, at a free concentration $[\mathrm{L}]$ much larger than the protein concentration, multiplies the native population by $1 + [\mathrm{L}]/K_{\mathrm{d}}$, so that the new midpoint $T_{\mathrm{m}}'$ solves

$$
\Delta_{\mathrm{U}}G(T_{\mathrm{m}}') + RT_{\mathrm{m}}'\ln\!\left(1 + \frac{[\mathrm{L}]}{K_{\mathrm{d}}}\right) = 0, \qquad \Delta T_{\mathrm{m}} \approx \frac{RT_{\mathrm{m}}^2}{\Delta H_{\mathrm{m}}}\ln\!\left(1 + \frac{[\mathrm{L}]}{K_{\mathrm{d}}}\right).
$$

**Example 8.3.3** For the protein of the figures ($T_{\mathrm{m}} = 333.15\,\mathrm{K}$, $\Delta H_{\mathrm{m}} = 350\,\mathrm{kJ\,mol^{-1}}$), $RT_{\mathrm{m}}^2/\Delta H_{\mathrm{m}} = 2.6\,\mathrm{K}$. A ligand at $100$ times its $K_{\mathrm{d}}$ raises $T_{\mathrm{m}}$ by $2.6 \times \ln 101 = 12.2\,\mathrm{K}$ by the approximation and $11.5\,\mathrm{K}$ by the exact equation (the stability curve bends). Each factor of ten in $[\mathrm{L}]/K_{\mathrm{d}}$ adds only about $5$–$6\,\mathrm{K}$, so a shift in $T_{\mathrm{m}}$ is a logarithmic and rather insensitive measure of affinity.

This is the basis of the thermal shift assay, used to screen thousands of ligands or buffer conditions with microliters of protein.

**Definition 8.3.2 (Differential Scanning Fluorimetry)** **Differential scanning fluorimetry** (the thermal shift assay) follows the thermal unfolding of a protein by the fluorescence of a dye, such as SYPRO Orange, that fluoresces when bound to exposed hydrophobic surface (or by the intrinsic fluorescence of tryptophan), in a real-time PCR instrument, and reports the shift of $T_{\mathrm{m}}$ caused by ligands or solution conditions.

The assay ranks binders but does not measure $K_{\mathrm{d}}$ without the enthalpy and heat capacity of unfolding and the temperature dependence of binding, and the dye itself can bind some proteins or ligands. Calorimetry and DSF are complementary: DSC gives the full thermodynamics of a few samples, DSF the relative stability of many.

![Linked equilibria seen by calorimetry. A: apparent binding enthalpy measured by ITC in seven buffers of different ionization enthalpy (values at 25 °C), for two simulated complexes with the same intrinsic binding enthalpy (−60 kJ/mol) that take up 0.73 or 0.02 protons on binding (with experimental scatter); straight-line fits by Formula 8.4.4 recover the number of protons from the slope and the intrinsic enthalpy from the intercept. B: thermal shift: fraction unfolded of the protein of §8.3.1 at ratios [L]/K_d = 0 to 1000 of a ligand that binds only the native state. C: shift of Tm against [L]/K_d from the exact condition of Formula 8.3.3 (solid) and its small-shift approximation (dashed); the shift grows only logarithmically with ligand concentration](./plots/linkage-thermal-shift.py)

## 8.4. Isothermal Titration Calorimetry

### 8.4.1. The Instrument

**Definition 8.4.1 (Isothermal Titration Calorimetry)** **Isothermal titration calorimetry** (ITC) measures the heat absorbed or released when a ligand solution is injected in small portions into a solution of a macromolecule held at constant temperature; the heat of each injection, plotted against the molar ratio of total ligand to total macromolecule, is the binding isotherm, from which the stoichiometry $n$, the association constant $K_{\mathrm{a}}$ and the binding enthalpy $\Delta H_{\mathrm{b}}$ are obtained in a single experiment.

The sample cell ($0.2$–$1.4\,\mathrm{mL}$) and a reference cell filled with water or buffer sit in an adiabatic jacket. A constant small power heats the reference, and a feedback circuit supplies to the sample whatever power keeps the two at the same temperature. After each injection from a motor-driven syringe that also stirs the cell, an exothermic binding reaction warms the sample and the feedback power falls; the downward peak in the power trace, integrated over time, is the heat of that injection. As the macromolecule becomes saturated, the heats fall to the small heat of dilution of the ligand, which is measured separately by injecting ligand into buffer and subtracted.

### 8.4.2. The Binding Isotherm

For $n$ identical and independent sites per macromolecule M, the concentration of occupied sites $[\mathrm{ML}]$ in the cell follows from $K_{\mathrm{a}} = [\mathrm{ML}]/([\mathrm{L}]\,(n[\mathrm{M}]_{\mathrm{t}} - [\mathrm{ML}]))$ and the conservation of ligand, $[\mathrm{L}]_{\mathrm{t}} = [\mathrm{L}] + [\mathrm{ML}]$.

**Formula 8.4.1 (Bound Ligand)**

$$
[\mathrm{ML}] = \frac{1}{2}\left[n[\mathrm{M}]_{\mathrm{t}} + [\mathrm{L}]_{\mathrm{t}} + \frac{1}{K_{\mathrm{a}}} - \sqrt{\left(n[\mathrm{M}]_{\mathrm{t}} + [\mathrm{L}]_{\mathrm{t}} + \frac{1}{K_{\mathrm{a}}}\right)^2 - 4n[\mathrm{M}]_{\mathrm{t}}[\mathrm{L}]_{\mathrm{t}}}\,\right],
$$
the root of the binding quadratic that lies between $0$ and $\min(n[\mathrm{M}]_{\mathrm{t}}, [\mathrm{L}]_{\mathrm{t}})$.

The total heat released in the cell of volume $V_0$ is $Q = V_0\,\Delta H_{\mathrm{b}}\,[\mathrm{ML}]$. Commercial cells are completely filled, so each injection of volume $\delta v_i$ displaces the same volume of solution out of the active cell; with cumulative injected volume $v_i$, the standard model takes $[\mathrm{M}]_{\mathrm{t}} = M_0(1 - v_i/2V_0)/(1 + v_i/2V_0)$ and $[\mathrm{L}]_{\mathrm{t}} = L_0(v_i/V_0)(1 - v_i/2V_0)$.

**Formula 8.4.2 (Heat of an Injection)** The heat of injection $i$, corrected for the displaced volume, is

$$
\delta Q_i = Q_i - Q_{i-1} + \frac{\delta v_i}{V_0}\,\frac{Q_i + Q_{i-1}}{2}.
$$

In the limit of small injections the normalized heat per mole of injected ligand has a closed form that shows which parameter controls the shape. Write $X_R = [\mathrm{L}]_{\mathrm{t}}/[\mathrm{M}]_{\mathrm{t}}$ for the molar ratio and define the dimensionless number below.

**Definition 8.4.2 (Wiseman c Value)** The **Wiseman c value** of a titration is $c = nK_{\mathrm{a}}[\mathrm{M}]_{\mathrm{t}}$, the product of the association constant and the concentration of binding sites in the cell; it is the ratio of the site concentration to the dissociation constant.

**Formula 8.4.3 (Wiseman Isotherm)** With $r = 1/c$,

$$
\frac{1}{V_0}\frac{\mathrm{d}Q}{\mathrm{d}[\mathrm{L}]_{\mathrm{t}}} = \Delta H_{\mathrm{b}}\left[\frac{1}{2} + \frac{1 - X_R/n - r}{2\sqrt{(1 + X_R/n + r)^2 - 4X_R/n}}\right]
$$
(Wiseman, Williston, Brandts and Lin, 1989).

The heat per mole of injectant starts near $\Delta H_{\mathrm{b}}$, when almost every injected ligand binds, falls through an inflection at $X_R = n$ and approaches zero at saturation. Only $c$ and $n$ set the shape; $\Delta H_{\mathrm{b}}$ scales it. Near the equivalence point the width of the transition is proportional to $1/\sqrt{c}$.

![Isothermal titration calorimetry of 1:1 binding (200 µL cell, 20 µM macromolecule, 220 µM ligand in the syringe, a 0.4 µL first injection followed by 19 injections of 2 µL, ΔH_b = −45 kJ/mol). A: simulated raw power trace at c = 50: each exothermic injection produces a downward peak that relaxes with the instrument time constant, and the peaks shrink as the sites fill. B: integrated, normalized isotherms (Formulas 8.4.1–8.4.2) for Wiseman c from 0.5 to 5000: at c = 0.5 the curve is too shallow to define n or ΔH; at c ≥ 500 it is a step whose height gives ΔH_b and whose position gives n, but whose steepness no longer depends on K. C: nonlinear least-squares fits of noisy data (0.15 µJ per injection) at c = 50 and c = 5000: both give n and ΔH_b precisely, but K_d is determined to ±3 % at c = 50 and only to ±80 % (a factor of two) at c = 5000](./plots/itc-isotherms.py)

### 8.4.3. Designing a Titration

The c value decides what an experiment can measure (panel B of the figure).

- $1 < c < 1\,000$ (best $10$–$100$): the isotherm is sigmoidal, and $n$, $K_{\mathrm{a}}$ and $\Delta H_{\mathrm{b}}$ are all determined.
- $c \gg 1\,000$: the curve is a step; $n$ and $\Delta H_{\mathrm{b}}$ are accurate, but $K_{\mathrm{a}}$ only has a lower bound. Tight binders are measured by displacement titration: the macromolecule is preloaded with a weaker competitor B, and the apparent constant $K_{\mathrm{a,app}} = K_{\mathrm{a}}/(1 + K_{\mathrm{a,B}}[\mathrm{B}])$ is brought into the window.
- $c < 1$: the curve is shallow and $n$, $K_{\mathrm{a}}$ and $\Delta H_{\mathrm{b}}$ are correlated. Weak binding can still be measured if $n$ is known and fixed, and if the titration goes to a large excess of ligand (molar ratios of $10$ or more), so that much of the binding curve is covered (Turnbull and Daranas, 2003).

The heat must also be measurable: each injection should release at least ten times the noise, typically $\gtrsim 1\,\mu\mathrm{J}$ on modern instruments. Ligand and macromolecule must be in identical buffer (usually by dialysis of the protein and dissolution of the ligand in the dialysate), because the heat of mixing slightly different buffers can exceed the heat of binding.

**Example 8.4.1** To measure $K_{\mathrm{d}} = 100\,\mathrm{nM}$ ($K_{\mathrm{a}} = 10^7\,\mathrm{M^{-1}}$) with $c = 100$ one needs $[\mathrm{M}]_{\mathrm{t}} = c/K_{\mathrm{a}} = 10\,\mu\mathrm{M}$ of sites and a syringe concentration of about $10$–$15$ times that, $110\,\mu\mathrm{M}$, to reach a molar ratio of $2$ in $40\,\mu\mathrm{L}$. With $\Delta H_{\mathrm{b}} = -20\,\mathrm{kJ\,mol^{-1}}$, an early $2\,\mu\mathrm{L}$ injection releases $2\times10^{-6}\,\mathrm{L} \times 110\times10^{-6}\,\mathrm{M} \times 20\,\mathrm{kJ\,mol^{-1}} = 4.4\,\mu\mathrm{J}$, comfortably above a noise of $0.1$–$0.2\,\mu\mathrm{J}$. For $K_{\mathrm{d}} = 1\,\mathrm{nM}$ the same $c$ would require $0.1\,\mu\mathrm{M}$ protein and heats of $0.04\,\mu\mathrm{J}$, below the noise: a displacement titration is needed.

### 8.4.4. From n, K and ΔH to the Full Thermodynamics

From one titration, $\Delta G_{\mathrm{b}} = -RT\ln(K_{\mathrm{a}}c^\circ)$ and $\Delta S_{\mathrm{b}} = (\Delta H_{\mathrm{b}} - \Delta G_{\mathrm{b}})/T$; titrations at several temperatures give $\Delta C_{p,\mathrm{b}} = \mathrm{d}\Delta H_{\mathrm{b}}/\mathrm{d}T$. The calorimetric $\Delta H_{\mathrm{b}}$ is usually far more precise than the van 't Hoff enthalpy obtained from the temperature dependence of $K_{\mathrm{a}}$, and disagreement between the two (beyond their errors) signals coupled processes, most often protonation or conformational change.

Pierce, Raman and Nall (1999) used ITC to compare two monoclonal antibodies that bind different epitopes of cytochrome c (antibody 2B5 near Pro44, 5F8 near Lys60). Both bind with a free energy that hardly changes with temperature, but for different reasons: for 2B5 the binding enthalpy and entropy change strongly with temperature and compensate (a large negative $\Delta C_p$, as expected for a binding surface that buries much nonpolar area), whereas for 5F8 both are nearly temperature-independent. Two interfaces with similar affinity can thus have entirely different thermodynamic signatures, which only calorimetry reveals.

### 8.4.5. Linked Protonation

If binding changes the $\mathrm{p}K_{\mathrm{a}}$ of a group on either partner, protons are taken up from or released to the buffer during binding, and the buffer's own ionization adds its enthalpy to the measured heat.

**Formula 8.4.4 (Linked Protonation)** If $n_{\ce{H+}}$ protons are taken up per binding event in a buffer of ionization enthalpy $\Delta H_{\mathrm{ion}}$, the measured enthalpy is

$$
\Delta H_{\mathrm{app}} = \Delta H_{\mathrm{b}} + n_{\ce{H+}}\,\Delta H_{\mathrm{ion}},
$$
so a plot of $\Delta H_{\mathrm{app}}$ against $\Delta H_{\mathrm{ion}}$ for several buffers at the same pH is a straight line with slope $n_{\ce{H+}}$ and intercept $\Delta H_{\mathrm{b}}$; for two buffers, $n_{\ce{H+}} = (\Delta H_{\mathrm{app,1}} - \Delta H_{\mathrm{app,2}})/(\Delta H_{\mathrm{ion,1}} - \Delta H_{\mathrm{ion,2}})$.

The ionization enthalpies of common **buffers** at $25\,^\circ\mathrm{C}$ span a wide range: acetate $-0.4$, phosphate (second $\mathrm{p}K_{\mathrm{a}}$) $3.6$, PIPES $11.2$, HEPES $20.4$, MOPS $21.1$, imidazole $36.6$ and Tris $47.5\,\mathrm{kJ\,mol^{-1}}$ (among the **Good's buffers**, HEPES and MOPS are intermediate). Tris and phosphate are therefore the usual pair for this test. For the antibody 2B5, binding measured in Tris and phosphate gave $n_{\ce{H+}} = 0.73$, attributed to the protonation of His33 of cytochrome c near the epitope, while 5F8 took up essentially none ($0.02$). The intrinsic $\Delta H_{\mathrm{b}}$, not the apparent one, is the quantity to compare between complexes; and since buffer ionization also has a heat capacity, linked protonation contributes to the apparent $\Delta C_p$ as well.

### 8.4.6. Enthalpy–Entropy Compensation

**Definition 8.4.3 (Enthalpy–Entropy Compensation)** **Enthalpy–entropy compensation** is the observation that, across a series of related binding or unfolding reactions (ligand analogs, mutants, temperatures), changes in $\Delta H$ are largely offset by changes in $T\Delta S$, so that $\Delta G$ varies much less than either.

Part of this is physics. Whenever a reaction has a large $\Delta C_p$, $\Delta H$ and $T\Delta S$ change with temperature by almost the same amount, since $\mathrm{d}\Delta H/\mathrm{d}T = \Delta C_p$ and $T\,\mathrm{d}\Delta S/\mathrm{d}T = \Delta C_p$, so $\Delta G$ is nearly constant over a range of temperatures (panel A of the figure in §8.3.1); and a tighter interface that gains enthalpy also restricts more motion and loses entropy. Part of it is an artifact that must be excluded before the physics is claimed: $T\Delta S$ is never measured independently but computed as $\Delta H - \Delta G$, so errors in $\Delta H$ appear in $T\Delta S$ with the same sign; and ITC measures $K_{\mathrm{a}}$ only within a window of about $10^3$–$10^9\,\mathrm{M^{-1}}$, which confines $\Delta G$ to about $-17$ to $-51\,\mathrm{kJ\,mol^{-1}}$. If $\Delta H$ varies over $100\,\mathrm{kJ\,mol^{-1}}$ in a series while $\Delta G$ is confined to this window, a plot of $T\Delta S$ against $\Delta H$ has a slope close to one for any data whatever.

## 8.5. Phase Transitions of Lipid Bilayers

A phospholipid bilayer (a **lipid bilayer** of one lipid species) melts cooperatively from an ordered gel phase with stretched hydrocarbon chains to a fluid liquid-crystalline phase with disordered chains (the main transition, a weak **first-order phase transition**, [6.3.8](/6.3.8)). DSC was the method that established its thermodynamics. For dipalmitoylphosphatidylcholine (DPPC) the main transition lies at $41.4\,^\circ\mathrm{C}$ with $\Delta H_{\mathrm{cal}} \approx 36\,\mathrm{kJ\,mol^{-1}}$ of lipid, preceded at about $35\,^\circ\mathrm{C}$ by a small pretransition to a rippled gel phase; the main transition temperature rises by about $15\,\mathrm{K}$ for every two $\ce{CH2}$ groups (DMPC, 14 carbons, $24\,^\circ\mathrm{C}$; DPPC, 16, $41\,^\circ\mathrm{C}$; DSPC, 18, $55\,^\circ\mathrm{C}$) and falls sharply with a cis double bond.

A lipid bilayer is not a molecule, but the ratio test of Formula 8.2.2 still measures its cooperativity: $\Delta H_{\mathrm{cal}}$ is per mole of lipid, while the width of the peak reports the enthalpy of the unit that melts as one.

**Definition 8.5.1 (Cooperative Unit)** The **cooperative unit** of a transition is the number of molecules that change state together, $n = \Delta H_{\mathrm{vH}}/\Delta H_{\mathrm{cal}}$ with $\Delta H_{\mathrm{cal}}$ per mole of molecules.

**Formula 8.5.1 (Width of a Two-State Peak)** For a two-state transition with van 't Hoff enthalpy $\Delta H_{\mathrm{vH}}$, the full width of the excess heat-capacity peak at half its height is

$$
\Delta T_{1/2} = \frac{2\ln(3 + 2\sqrt2)\,RT_{\mathrm{m}}^2}{\Delta H_{\mathrm{vH}}} = \frac{3.525\,RT_{\mathrm{m}}^2}{\Delta H_{\mathrm{vH}}} .
$$

**Proof** The peak is proportional to $f(1-f) = K/(1+K)^2$ with $\ln K = (\Delta H_{\mathrm{vH}}/R)(1/T_{\mathrm{m}} - 1/T) \approx \Delta H_{\mathrm{vH}}(T - T_{\mathrm{m}})/(RT_{\mathrm{m}}^2)$. Its maximum $1/4$ is at $K = 1$, and $K/(1+K)^2 = 1/8$ when $K^2 - 6K + 1 = 0$, that is $K = 3 \pm 2\sqrt2$. The two half-height points are therefore at $\ln K = \pm\ln(3 + 2\sqrt2) = \pm 1.763$, separated by $3.525$ in $\ln K$, which corresponds to $\Delta T_{1/2} = 3.525\,RT_{\mathrm{m}}^2/\Delta H_{\mathrm{vH}}$. $\square$

![The main transition of a phospholipid bilayer and the size of the cooperative unit. A: excess heat capacity per mole of lipid for cooperative units of n = 20, 100 and 500 lipids that melt as one (two-state model with ΔH_vH = n ΔH_cal; Tm = 41.4 °C and ΔH_cal = 36 kJ/mol, the values of DPPC): the area is the same for all three, while the height grows and the width falls in proportion to n. B: full width at half height against n (Formula 8.5.1); the main transition of multilamellar DPPC vesicles, about 0.1 K wide, corresponds to a cooperative unit of about 800 lipids, while transitions broadened to 1 or 3 K correspond to units of tens of lipids](./plots/lipid-dsc.py)

**Example 8.5.1** The main transition of multilamellar DPPC vesicles has $\Delta T_{1/2} \approx 0.1\,\mathrm{K}$. Formula 8.5.1 gives $\Delta H_{\mathrm{vH}} = 3.525 \times 8.314 \times 314.55^2/0.1\,\mathrm{J\,mol^{-1}} = 2.9\times10^4\,\mathrm{kJ\,mol^{-1}}$, and with $\Delta H_{\mathrm{cal}} = 36\,\mathrm{kJ\,mol^{-1}}$ the cooperative unit is $n \approx 800$ lipids: patches of a few hundred square nanometers of bilayer melt as a whole. Anything that disturbs the packing (small vesicles with strongly curved bilayers, impurities, cholesterol, membrane proteins) broadens the peak and reduces $n$; above about $30$ mol % cholesterol the transition is no longer detectable, because cholesterol creates the liquid-ordered phase in which chains are ordered but mobile ([7.6.24](/7.6.24)).

Cells keep their membranes near or above this transition by adjusting the length and saturation of their fatty acids, a response called homeoviscous adaptation: bacteria grown at lower temperature incorporate more unsaturated or branched chains, so that the transition of their membrane lipids stays below the growth temperature.

## 8.6. Macromolecules in Water: Volume and Hydration

The second half of this chapter turns from heat to motion. A macromolecule in solution responds to a force (gravity, a centrifugal field, the shear of a flowing solvent, thermal kicks) by moving against the friction of the water, and the friction depends on its size and shape. Hydrodynamic methods (sedimentation, diffusion, viscosity and dynamic light scattering) measure this response, and combined with one another they give the molar mass, the size and the shape of molecules in their native solvent. The physical principles of **Brownian motion**, **sedimentation** and light scattering by colloids were introduced in [6.3.21](/6.3.21); here they become quantitative tools for biological macromolecules.

A dissolved macromolecule occupies more than its "dry" volume, for two reasons: the volume it excludes from the solvent is set by its van der Waals surface plus the gaps between it and the first layer of water, and that first layer itself is perturbed. Water within about $1\,\mathrm{nm}$ of a protein surface has slower rotational and translational dynamics than bulk water; individual water molecules exchange in and out of the layer in picoseconds to nanoseconds, but on average the layer moves with the protein.

**Definition 8.6.1 (Partial Specific Volume)** The **partial specific volume** $\bar v$ of a solute is the increase of the volume of a solution per unit mass of solute added, at infinite dilution and constant temperature and pressure, $\bar v = (\partial V/\partial m_2)_{T,p,m_1}$. Its reciprocal is the effective density of the solute in that solvent.

For proteins $\bar v \approx 0.70$–$0.75\,\mathrm{mL\,g^{-1}}$ (density about $1.35\,\mathrm{g\,mL^{-1}}$, Formula 7.6.1 of [7.6.7](/7.6.7)), and it can be computed to within about $1\,\%$ from the amino-acid composition by adding residue volumes (the method of Cohn and Edsall); for nucleic acids, whose phosphates bind water and counterions tightly, $\bar v \approx 0.5$–$0.55\,\mathrm{mL\,g^{-1}}$, and for lipids and detergents $0.9$–$1.0\,\mathrm{mL\,g^{-1}}$.

**Formula 8.6.1 (Hydrated Volume)** A macromolecule of molar mass $M$ carrying $\delta$ grams of bound water per gram (typically $\delta \approx 0.3$–$0.4$ for proteins) has the hydrated volume

$$
V_{\mathrm{h}} = \frac{M}{N_{\mathrm{A}}}\left(\bar v + \delta\,\bar v_1\right),
$$
where $\bar v_1 \approx 1\,\mathrm{mL\,g^{-1}}$ is the specific volume of water.

With $\delta = 0.35$ the hydrated volume of a protein is about $1.5$ times the anhydrous one, and its radius about $1.14$ times larger. Hydration and shape both increase the friction of a molecule, and separating the two is the central problem of classical hydrodynamics (§8.10.2).

## 8.7. Friction and Shape

### 8.7.1. Friction at Low Reynolds Number

A protein that moves at velocity $v$ through water experiences a drag force proportional to $v$ and to the **viscosity** of the water. Its inertia is irrelevant: the Reynolds number is of order $10^{-10}$, and after a force is removed the protein stops within picoseconds ([7.6.22](/7.6.22)). The motion is governed by the balance of the applied force and the friction.

**Definition 8.7.1 (Frictional Coefficient)** The **frictional coefficient** $f$ of a particle is the ratio of the drag force to the velocity of steady translation through a solvent, $F_{\mathrm{drag}} = -fv$. For a sphere of radius $R$ with no slip at its surface, $f_0 = 6\pi\eta R$ (Stokes' law), where $\eta$ is the viscosity of the solvent.

The same friction governs Brownian motion, through the Einstein relation $D = k_{\mathrm{B}}T/f$; for a sphere this is the **Stokes–Einstein equation** $D = k_{\mathrm{B}}T/(6\pi\eta R)$ ([6.3.21](/6.3.21#sec-21.3.1), [7.6.5](/7.6.5)). Any measured $f$ or $D$ can therefore be expressed as the radius of an equivalent sphere.

**Definition 8.7.2 (Hydrodynamic Radius)** The **hydrodynamic radius** (Stokes radius) $R_{\mathrm{h}}$ of a particle is the radius of the sphere that has the same translational frictional coefficient, $R_{\mathrm{h}} = f/(6\pi\eta) = k_{\mathrm{B}}T/(6\pi\eta D)$.

### 8.7.2. The Frictional Ratio and the Perrin Factor

The *frictional ratio* $f/f_0$ compares the measured frictional coefficient with that of a sphere of the same mass and anhydrous volume, $f_0 = 6\pi\eta R_0$ with $R_0 = (3M\bar v/4\pi N_{\mathrm{A}})^{1/3}$. It factors into a contribution of hydration, which enlarges the sphere, and a contribution of shape: $f/f_0 = (f/f_{\mathrm{h}})(f_{\mathrm{h}}/f_0)$, with $f_{\mathrm{h}}/f_0 = (V_{\mathrm{h}}/V_0)^{1/3} = (1 + \delta\bar v_1/\bar v)^{1/3}$. For the shape factor Francis Perrin (1934, 1936) solved the friction of ellipsoids of revolution exactly.

**Definition 8.7.3 (Perrin Factor)** The **Perrin factor** $F = f_{\mathrm{e}}/f_{\mathrm{s}}$ is the ratio of the translational frictional coefficient of an ellipsoid of revolution to that of a sphere of the same volume, averaged over orientations; it depends only on the axial ratio.

**Formula 8.7.1 (Perrin's Equations)** For a prolate ellipsoid (semi-axes $a > b = b$, axial ratio $p = a/b > 1$) and an oblate ellipsoid ($a < b$, $p = a/b < 1$),

$$
F_{\text{prolate}} = \frac{\sqrt{p^2 - 1}}{p^{1/3}\ln\!\left(p + \sqrt{p^2 - 1}\right)}, \qquad
F_{\text{oblate}} = \frac{\sqrt{1 - p^2}}{p^{1/3}\arctan\!\left(\sqrt{1 - p^2}/p\right)} .
$$

Both tend to $1$ as $p \to 1$. The friction grows only slowly with elongation: a prolate ellipsoid with $p = 10$ has $F = 1.54$, one with $p = 50$ has $F = 2.95$, and disks of the same axial ratio have somewhat less friction than rods.

![Shape, friction and viscosity. A: Perrin factor of prolate (green) and oblate (red) ellipsoids of revolution relative to a sphere of equal volume (Formula 8.7.1); the band marks the frictional ratios of typical globular proteins, which include hydration. B: Simha factor of the intrinsic viscosity for the same ellipsoids (large-axial-ratio expansions, drawn for axial ratios of 5 and more; 2.5 for a sphere): viscosity is far more sensitive to elongation than friction. C: sedimentation coefficients s₂₀,w of proteins and of tobacco mosaic virus against molar mass, with the lines of spheres of anhydrous protein volume (v̄ = 0.73 mL/g) and frictional ratios from 1 to 3; the frictional ratio of each molecule, computed from its s and M with Formula 8.8.1, is given in parentheses. Compact enzymes lie at 1.15–1.35; fibrinogen, myosin and the TMV rod lie far above](./plots/shape-friction.py)

**Example 8.7.1** For lysozyme ($M = 14.3\,\mathrm{kDa}$, $\bar v = 0.703\,\mathrm{mL\,g^{-1}}$, $s_{20,\mathrm{w}} = 1.91\,\mathrm{S}$) the Svedberg relation (Formula 8.8.1) gives $f = M(1 - \bar v\rho)/(N_{\mathrm{A}}s) = 3.8\times10^{-11}\,\mathrm{kg\,s^{-1}}$, a hydrodynamic radius of $2.0\,\mathrm{nm}$. The anhydrous sphere has $R_0 = 1.60\,\mathrm{nm}$, so $f/f_0 = 1.26$. With $\delta = 0.35$, hydration alone accounts for $f_{\mathrm{h}}/f_0 = (1 + 0.35/0.703)^{1/3} = 1.14$, leaving a shape factor of $1.10$, which by Formula 8.7.1 corresponds to a prolate axial ratio of about $3$. The crystal structure of lysozyme is indeed an ellipsoid of about $4.5 \times 3 \times 3\,\mathrm{nm}$. The analysis is only as good as the assumed $\delta$: with no hydration the same data would imply an axial ratio of about $5$.

### 8.7.3. Rotational Friction and Diffusion

A particle also tumbles. Rotation at angular velocity $\Omega$ is opposed by a torque $-f_{\mathrm{r}}\Omega$, and the rotational diffusion coefficient is $D_{\mathrm{r}} = k_{\mathrm{B}}T/f_{\mathrm{r}}$, the angular counterpart of the Einstein relation.

**Formula 8.7.2 (Rotational Friction of a Sphere and a Rod)** For a sphere of radius $R$,

$$
f_{\mathrm{r}} = 8\pi\eta R^3 = 6\eta V, \qquad \tau_{\mathrm{c}} = \frac{1}{6D_{\mathrm{r}}} = \frac{4\pi\eta R^3}{3k_{\mathrm{B}}T} = \frac{\eta V}{k_{\mathrm{B}}T},
$$
where $\tau_{\mathrm{c}}$ is the rotational correlation time of a vector fixed in the particle (the decay time of the second Legendre polynomial of its orientation, measured by fluorescence anisotropy and NMR relaxation). For a rigid rod of length $L$ and diameter $d$ rotating about a short axis (Tirado and García de la Torre, 1980),

$$
D_{\mathrm{r}} = \frac{3k_{\mathrm{B}}T\left(\ln p + \delta_\perp\right)}{\pi\eta L^3}, \qquad p = L/d, \quad \delta_\perp \approx -0.662 + \frac{0.917}{p} - \frac{0.050}{p^2}.
$$

Rotational friction scales with the cube of the size, translational friction only linearly, which makes rotation the more sensitive probe of size and, for rods, of length.

**Example 8.7.2** A protein with $R_{\mathrm{h}} = 1.9\,\mathrm{nm}$ in water at $25\,^\circ\mathrm{C}$ ($\eta = 0.89\,\mathrm{mPa\,s}$) has $\tau_{\mathrm{c}} = \eta V/k_{\mathrm{B}}T = 0.89\times10^{-3} \times 2.87\times10^{-26}/4.11\times10^{-21}\,\mathrm{s} = 6.2\,\mathrm{ns}$, close to the measured rotational correlation time of lysozyme. A tobacco mosaic virus rod ($L = 300\,\mathrm{nm}$, $d = 18\,\mathrm{nm}$, $p = 16.7$) has $D_{\mathrm{r}} = 3 \times 4.05\times10^{-21} \times (2.81 - 0.61)/(\pi \times 1.0\times10^{-3} \times 2.7\times10^{-20})\,\mathrm{s^{-1}} = 320\,\mathrm{s^{-1}}$ at $20\,^\circ\mathrm{C}$, in agreement with the measured value of about $330\,\mathrm{s^{-1}}$; its orientation relaxes in $1/(6D_{\mathrm{r}}) = 0.5\,\mathrm{ms}$.

### 8.7.4. Birefringence

Elongated particles are optically anisotropic: their polarizability is larger along the long axis. In a solution of randomly oriented particles this averages out, but if the particles are partly aligned the solution becomes birefringent (**birefringence**, [5.4](/5.4)). The degree of alignment that a field or a flow can maintain against rotational diffusion measures $D_{\mathrm{r}}$.

**Definition 8.7.4 (Flow Birefringence)** **Flow birefringence** is the birefringence of a solution of anisotropic particles sheared between two concentric cylinders rotating at different speeds: the velocity gradient $G$ tends to align the particles, rotational diffusion to randomize them. As the dimensionless shear rate $\alpha = G/D_{\mathrm{r}}$ increases from zero, the extinction angle between the optic axis of the solution and the flow lines falls from $45^\circ$ (for rigid rods, to first order, $\chi \approx \pi/4 - \alpha/12$ in radians) and the birefringence grows.

In electric birefringence a short pulse of a strong electric field aligns particles that carry a permanent or induced dipole, and after the pulse the birefringence decays as $\exp(-6D_{\mathrm{r}}t)$, giving $D_{\mathrm{r}}$ directly (for TMV, a decay time of $0.5\,\mathrm{ms}$). Such measurements gave the first lengths of DNA fragments, viruses and muscle proteins in solution; today the same rotational dynamics are measured more often by time-resolved fluorescence anisotropy ([7.6.11](/7.6.11)) and NMR relaxation ([7.6.13](/7.6.13)).

## 8.8. Sedimentation Velocity

### 8.8.1. The Sedimentation Coefficient

In a centrifuge spinning at angular velocity $\omega$, a particle at radius $r$ feels the centrifugal force $m\omega^2 r$, the buoyant force $-m\bar v\rho\,\omega^2 r$ of the displaced solvent (density $\rho$) and the friction $-f\,\mathrm{d}r/\mathrm{d}t$. Within microseconds these balance, and the particle moves outward at a constant velocity per unit field.

**Formula 8.8.1 (Sedimentation Coefficient)** The steady sedimentation velocity per unit centrifugal acceleration is

$$
s = \frac{\mathrm{d}r/\mathrm{d}t}{\omega^2 r} = \frac{M(1 - \bar v\rho)}{N_{\mathrm{A}}f},
$$
measured in svedbergs ($1\,\mathrm{S} = 10^{-13}\,\mathrm{s}$); $M(1 - \bar v\rho)$ is the buoyant molar mass.

(**sedimentation coefficient**, [6.3.21](/6.3.21#sec-21.3.4).) Because $f$ depends on shape, $s$ alone does not give $M$. Combining it with $D = k_{\mathrm{B}}T/f$, measured independently or from the same experiment, eliminates the friction.

**Definition 8.8.1 (Svedberg Equation)** The **Svedberg equation** gives the molar mass from the sedimentation and diffusion coefficients of the same species under the same conditions,

$$
M = \frac{sRT}{D(1 - \bar v\rho)} .
$$

For compact particles of constant density $f \propto M^{1/3}$, so $s \propto M^{2/3}$ (panel C of the previous figure); the familiar ribosomal "S values" are therefore not additive. The $30\mathrm{S}$ ($0.85\,\mathrm{MDa}$) and $50\mathrm{S}$ ($1.45\,\mathrm{MDa}$) subunits of the bacterial ribosome form a $2.3\,\mathrm{MDa}$ particle whose sedimentation coefficient, if it were as compact as the large subunit, would be $50 \times (2.3/1.45)^{2/3} = 68\,\mathrm{S}$: close to the measured $70\mathrm{S}$, not $80\mathrm{S}$.

Measured values depend on temperature and solvent through $\eta$ and $\rho$, and are converted to standard conditions (water at $20\,^\circ\mathrm{C}$):

$$
s_{20,\mathrm{w}} = s_{T,\mathrm{b}}\,\frac{\eta_{T,\mathrm{b}}}{\eta_{20,\mathrm{w}}}\,\frac{1 - \bar v\rho_{20,\mathrm{w}}}{1 - \bar v\rho_{T,\mathrm{b}}}, \qquad
D_{20,\mathrm{w}} = D_{T,\mathrm{b}}\,\frac{293.15\,\mathrm{K}}{T}\,\frac{\eta_{T,\mathrm{b}}}{\eta_{20,\mathrm{w}}} .
$$
Both also depend on concentration, through hydrodynamic interactions (the backflow of solvent displaced by sedimenting neighbors slows each particle) and thermodynamic nonideality; for proteins $s = s^0/(1 + k_s c)$ with $k_s$ of order $0.01\,\mathrm{L\,g^{-1}}$, larger for elongated molecules, so values are extrapolated to zero concentration.

### 8.8.2. The Analytical Ultracentrifuge and the Lamm Equation

The analytical ultracentrifuge (**ultracentrifugation**) spins a sector-shaped cell at up to $60\,000\,\mathrm{rpm}$ ($\omega^2 r \approx 2.6\times10^5\,g$) and records the radial concentration profile every few minutes by absorbance at a chosen wavelength (selective for proteins at $280\,\mathrm{nm}$, nucleic acids at $260\,\mathrm{nm}$ or labeled molecules) or by Rayleigh interference, which measures the refractive-index increment of all solutes with high precision. The sector shape keeps the radial walls along the field, so that molecules do not collide with them. In a sedimentation-velocity run the solution is initially uniform; the macromolecules move out from the meniscus, leaving pure solvent behind, and a boundary forms that moves at the rate set by $s$ and spreads by diffusion.

**Definition 8.8.2 (Lamm Equation)** The **Lamm equation** describes the evolution of the concentration $c(r, t)$ of a sedimenting species in a sector-shaped cell under a centrifugal field:

$$
\frac{\partial c}{\partial t} = \frac{1}{r}\frac{\partial}{\partial r}\left[r\left(D\frac{\partial c}{\partial r} - s\omega^2 r c\right)\right],
$$
with no flux through the meniscus $r_m$ and the bottom $r_b$ (Ole Lamm, 1929).

The equation is the continuity equation for the radial flux $J = s\omega^2 r c - D\,\partial c/\partial r$ (sedimentation outward, diffusion down the gradient) in cylindrical geometry. It has no closed solution for finite cells and is solved numerically; two exact consequences are useful in practice.

**Formula 8.8.2 (Boundary Motion and Radial Dilution)** In the plateau region beyond the boundary, where $\partial c/\partial r = 0$, the concentration decreases with time as

$$
c_{\mathrm{p}}(t) = c_0\,\mathrm{e}^{-2s\omega^2 t},
$$
and the boundary (the second moment of the gradient, or approximately its midpoint) moves as $\ln(r_{\mathrm{b}}(t)/r_m) = s\int_0^t \omega^2\,\mathrm{d}t'$.

**Proof** In the plateau, $\partial c/\partial t = -(1/r)\,\partial(s\omega^2 r^2 c)/\partial r = -2s\omega^2 c$, which integrates to the exponential. A point that moves with velocity $s\omega^2 r$ satisfies $\mathrm{d}\ln r/\mathrm{d}t = s\omega^2$. $\square$

The plateau dilutes because the sector widens with radius: the same molecules spread over a growing area. After one hour at $50\,000\,\mathrm{rpm}$ a $4.4\,\mathrm{S}$ protein has diluted by $8\,\%$.

![Sedimentation velocity: the Lamm equation solved numerically. A: forces on a particle in the sector-shaped cell of an analytical ultracentrifuge. B: concentration profiles every 10 min for a mixture of a monomer (4.4 S, D = 6.0 × 10⁻⁷ cm²/s, 70 % of the mass) and a dimer (6.7 S, 4.7 × 10⁻⁷ cm²/s, 30 %) at 50 000 rpm, computed by finite volumes with no-flux walls; the boundaries move outward and broaden, the plateau decreases by radial dilution (Formula 8.8.2), and material piles up at the bottom. C: the apparent distribution of sedimentation coefficients g(s*) obtained from the 60-min profile by the change of variable s* = ln(r/r_m)/(ω²t); the two species appear as two overlapping peaks centered near their true s values (dotted), broadened by diffusion](./plots/lamm-sedimentation.py)

### 8.8.3. Analysis of Sedimentation Velocity Data

Modern analysis fits the Lamm equation to the entire set of profiles. In the $c(s)$ method (Peter Schuck, 2000) the data are represented as a superposition of Lamm solutions for a grid of $s$ values, each with $D$ derived from $s$ through a common frictional ratio; the amplitudes are found by least squares with maximum-entropy or Tikhonov **regularization**, because the inversion is ill-conditioned. The result is a distribution $c(s)$ in which diffusion broadening has been removed, so that species differing by $10$–$20\,\%$ in $s$ are resolved. From the best-fit frictional ratio and the position of a peak one obtains $M$ (the Svedberg equation in disguise), and from the areas the composition, without any separation step. Simpler model-free transformations, such as the time-derivative $g(s^*)$ of panel C, show the same information with diffusion broadening included.

Sedimentation velocity is the method of choice to answer three questions about a purified protein: is it homogeneous, what is its oligomeric state, and is it aggregated? It uses $0.1$–$1\,\mathrm{mg\,mL^{-1}}$ in $0.4\,\mathrm{mL}$, works in any buffer and needs no matrix or calibration standards.

## 8.9. Sedimentation Equilibrium

### 8.9.1. The Equilibrium Distribution

At lower speed and after long enough time, sedimentation and diffusion balance at every radius (**sedimentation equilibrium**, [6.3.21](/6.3.21#sec-21.3.3)). Setting the flux of the Lamm equation to zero, $s\omega^2 r c = D\,\mathrm{d}c/\mathrm{d}r$, and replacing $s/D$ by the Svedberg equation gives a distribution that depends on the buoyant molar mass only.

**Formula 8.9.1 (Sedimentation Equilibrium of an Ideal Species)**

$$
c(r) = c(r_0)\,\exp\!\left[\sigma\,\frac{r^2 - r_0^2}{2}\right], \qquad \sigma = \frac{M(1 - \bar v\rho)\,\omega^2}{RT},
$$
so that $\ln c$ is linear in $\xi = (r^2 - r_0^2)/2$ with slope $\sigma$, the reduced molar mass.

This is the **Boltzmann distribution** in the centrifugal potential $-\tfrac12 m(1 - \bar v\rho)\omega^2 r^2$, and it contains neither $f$ nor $D$: equilibrium gives the molar mass independently of shape, with an accuracy of a few percent, at the cost of time. The approach to equilibrium is governed by diffusion across the column of height $L = r_b - r_m$, with a characteristic time of order $L^2/D$: for a $3\,\mathrm{mm}$ column and $D = 6\times10^{-7}\,\mathrm{cm^2\,s^{-1}}$, $L^2/D = 1.5\times10^5\,\mathrm{s}$, so equilibrium takes about a day. The speed is chosen so that $\sigma L r$ is about $1$–$3$, which gives a concentration ratio between bottom and top of $3$–$20$ (for $50\,\mathrm{kDa}$ at $12\,000\,\mathrm{rpm}$, $\sigma = 0.87\,\mathrm{cm^{-2}}$).

### 8.9.2. Self-Association and Nonideality

If a protein exists in several reversibly interconverting oligomeric states, each species $i$ has its own exponential with $\sigma_i = i\sigma_1$, and the law of mass action links their concentrations at each radius.

**Formula 8.9.2 (Self-Associating System)** For monomer ⇌ $i$-mer equilibria with association constants $K_{1,i} = c_i/c_1^i$ (in mass concentration units),

$$
c(r) = \sum_i K_{1,i}\,c_1(r_0)^i\,\mathrm{e}^{i\sigma_1\xi}, \qquad
M_{w,\mathrm{app}}(r) = \frac{RT}{(1 - \bar v\rho)\,\omega^2}\,\frac{\mathrm{d}\ln c}{\mathrm{d}\xi},
$$
where $M_{w,\mathrm{app}}$ is the weight-average molar mass of the material at radius $r$; it rises with the local concentration for an associating system and falls for a nonideal one (positive second **virial coefficient** $B$, with $M_{\mathrm{app}} \approx M/(1 + 2BMc)$).

Fitting several profiles at different loading concentrations and speeds with Formula 8.9.2 gives the stoichiometry and the association constants, typically for $K_{\mathrm{d}}$ between $10\,\mathrm{nM}$ and $1\,\mathrm{mM}$. A heterogeneous mixture of non-interacting species also curves $\ln c$ upward, but its apparent molar mass does not depend on the loading concentration, which distinguishes it from reversible association.

![Sedimentation equilibrium at 12 000 rpm (column 6.90–7.20 cm, v̄ = 0.73 mL/g, loading 1 g/L). A: equilibrium profiles of a 50 kDa monomer, a 100 kDa dimer, a reversible monomer–dimer system (association constant 2 L/g) and a nonideal monomer (second virial coefficient BM = 0.05 L/g). B: ln c against ξ = (r² − r₀²)/2: each ideal species gives a straight line of slope σ (Formula 8.9.1); the associating system curves upward and the nonideal one downward. C: apparent weight-average molar mass from the local slope (Formula 8.9.2) against the local concentration: constant for the ideal species, rising from about 60 toward 100 kDa for the monomer–dimer system, falling below 50 kDa for the nonideal monomer](./plots/sed-equilibrium.py)

### 8.9.3. Density-Gradient Equilibrium

In a concentrated solution of a dense salt such as CsCl, the centrifugal field itself creates a density gradient, and a macromolecule comes to rest where the solution density equals its buoyant density $1/\bar v$. Near that point the buoyancy factor is $1 - \bar v\rho(r) \approx -\bar v\,(\mathrm{d}\rho/\mathrm{d}r)(r - r_0)$, the potential is harmonic, and the band is Gaussian.

**Formula 8.9.3 (Width of an Equilibrium Density-Gradient Band)** A species of molar mass $M$ banding at $r_0$ in a gradient $\mathrm{d}\rho/\mathrm{d}r$ forms a Gaussian band with variance

$$
\sigma_r^2 = \frac{RT}{M\,\bar v\,\omega^2 r_0\,(\mathrm{d}\rho/\mathrm{d}r)}
$$
(Meselson, Stahl and Vinograd, 1957).

**Example 8.9.1** DNA fragments of $10^7\,\mathrm{g\,mol^{-1}}$ ($15\,\mathrm{kb}$) in CsCl at $44\,770\,\mathrm{rpm}$ band at $r_0 \approx 6.6\,\mathrm{cm}$ where $\mathrm{d}\rho/\mathrm{d}r \approx 0.12\,\mathrm{g\,cm^{-4}}$, with $\bar v = 1/1.71\,\mathrm{cm^3\,g^{-1}}$: $\sigma_r^2 = 2.48\times10^{10}/(10^7 \times 0.585 \times 2.2\times10^7 \times 6.6 \times 0.12)\,\mathrm{cm^2} = 2.4\times10^{-4}\,\mathrm{cm^2}$, a band about $0.15\,\mathrm{mm}$ wide. Fully $^{15}\mathrm{N}$-labeled DNA is denser by $0.014\,\mathrm{g\,cm^{-3}}$, which shifts its band by $0.014/0.12 = 1.2\,\mathrm{mm}$, eight standard deviations. This is why the Meselson–Stahl experiment could resolve heavy, hybrid and light DNA as three sharp bands ([7.2.7](/7.2.7#sec-7.1.2)). Preformed sucrose gradients, used to separate ribosomal subunits and polysomes by rate rather than by density, are the preparative cousin of sedimentation velocity.

## 8.10. Viscosity

### 8.10.1. Intrinsic Viscosity

Particles suspended in a flowing liquid disturb the flow around them and increase the energy it dissipates. Einstein showed in 1906 (correcting his own numerical error in 1911) that rigid spheres at volume fraction $\varphi$ increase the viscosity to $\eta = \eta_0(1 + 2.5\varphi)$, independently of their size. For macromolecules the volume fraction is $\varphi = c\,v_{\mathrm{h}}$, with $v_{\mathrm{h}} = N_{\mathrm{A}}V_{\mathrm{h}}/M$ the hydrated specific volume, and the effect per unit concentration at infinite dilution is the **intrinsic viscosity** ([6.3.21](/6.3.21#sec-21.9.4)).

**Formula 8.10.1 (Intrinsic Viscosity of Rigid Particles)**

$$
[\eta] = \lim_{c \to 0}\frac{\eta - \eta_0}{\eta_0\,c} = \nu\,v_{\mathrm{h}} = \nu\,\frac{N_{\mathrm{A}}V_{\mathrm{h}}}{M},
$$
where the Simha factor $\nu$ depends only on shape: $\nu = 2.5$ for spheres (Einstein), and for elongated ellipsoids it grows roughly as $p^2/\ln p$ (Simha, 1940; panel B of the shape figure).

For a compact protein $[\eta] \approx 2.5 \times (0.73 + 0.35) \approx 2.7\,\mathrm{mL\,g^{-1}}$, independent of $M$; measured values for globular proteins are $3$–$4\,\mathrm{mL\,g^{-1}}$, whereas fibrinogen has $[\eta] \approx 27$ and myosin about $220\,\mathrm{mL\,g^{-1}}$. Because $\nu$ is so sensitive to elongation, viscosity was historically the strongest evidence that molecules such as myosin, collagen and DNA are long rods. It is measured simply with a capillary viscometer, from the ratio of flow times of solution and solvent at several concentrations.

### 8.10.2. Combining Measurements: The Scheraga–Mandelkern Parameter

Each hydrodynamic quantity depends on both hydration and shape. One might hope to separate them by combining two measurements, for example $s$ and $[\eta]$, from which the hydrated volume cancels in the Scheraga–Mandelkern combination

$$
\beta = \frac{N_{\mathrm{A}}\,s\,[\eta]^{1/3}\,\eta_0}{M^{2/3}(1 - \bar v\rho)} = \frac{(N_{\mathrm{A}}\,\nu)^{1/3}}{(162\pi^2)^{1/3}\,F} ,
$$
which depends on shape only. Unfortunately $\beta$ varies only from $2.12\times10^6$ for a sphere (in the customary cgs units with $[\eta]$ in $\mathrm{dL\,g^{-1}}$) to about $2.5\times10^6$ for very long prolate ellipsoids, well within the errors of real data, and it cannot distinguish prolate from oblate shapes. The lesson, learned in the 1950s, is that hydrodynamic data constrain one combination of hydration and shape well and the other poorly. The modern solution is to compute hydrodynamic properties from atomic structures (bead and shell models of the molecular surface, with programs such as HYDROPRO), so that hydrodynamics tests a structural model rather than determining a shape by itself.

### 8.10.3. Flexible Chains

For flexible polymers the intrinsic viscosity grows with molar mass, because a coil is mostly solvent and its hydrodynamic volume grows faster than its mass. The Mark–Houwink exponent $a$ in $[\eta] = KM^a$ (**Mark–Houwink equation**) is $0$ for compact spheres, $0.5$ for random coils in a theta solvent, about $0.8$ in a good solvent and up to $1.8$ for rigid rods. Unfolded proteins in $6\,\mathrm{M}$ guanidinium chloride follow $[\eta] \approx 0.72\,N^{0.66}\,\mathrm{mL\,g^{-1}}$ for $N$ residues (Tanford, 1967), the behavior of random coils with excluded volume, and their hydrodynamic radii scale as $R_{\mathrm{h}} \propto N^{0.57}$, in contrast to $N^{1/3}$ for folded proteins. These scaling laws, and their meaning in terms of polymer physics, are developed in [7.6.21](/7.6.21) and applied to intrinsically disordered proteins in [7.6.16](/7.6.16).

## 8.11. Dynamic Light Scattering

### 8.11.1. Intensity Fluctuations and Diffusion

Light scattered by a dilute solution is the sum of waves from all illuminated particles. Its intensity at a detector depends on their relative phases, which change as the particles diffuse; the intensity therefore fluctuates on the time scale on which particles move by about one wavelength, from microseconds to milliseconds (**dynamic light scattering**, DLS, [6.3.21](/6.3.21#sec-21.4.3)). The average intensity is the subject of static light scattering ([7.6.9](/7.6.9)); DLS analyzes its fluctuations.

The scattered field from $N$ particles at positions $\boldsymbol{r}_j(t)$ is $E(t) \propto \sum_j \mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r}_j(t)}$, where the scattering vector $\boldsymbol{q}$ is the difference between the scattered and incident wave vectors, of magnitude

$$
q = \frac{4\pi n}{\lambda_0}\sin\frac{\theta}{2},
$$
with $n$ the refractive index of the solvent, $\lambda_0$ the vacuum wavelength and $\theta$ the scattering angle.

**Theorem 8.11.1 (Field Autocorrelation of Brownian Particles)** For $N$ independent particles diffusing with coefficient $D$, the normalized field autocorrelation function is

$$
g_1(\tau) = \frac{\langle E^*(t)E(t+\tau)\rangle}{\langle\lvert E\rvert^2\rangle} = \mathrm{e}^{-\Gamma\tau}, \qquad \Gamma = q^2 D .
$$

**Proof** Cross terms $j \ne k$ average to zero because the positions of different particles are independent and uniformly distributed, so $\langle E^*(t)E(t+\tau)\rangle \propto N\langle\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\Delta\boldsymbol{r}}\rangle$, with $\Delta\boldsymbol{r}$ the displacement of one particle in time $\tau$. Its component along $\boldsymbol{q}$ is normally distributed with mean zero and variance $2D\tau$ ([7.6.5](/7.6.5)), and for a **normal distribution** $\mathbb{E}[\mathrm{e}^{\mathrm{i}qX}] = \mathrm{e}^{-q^2\sigma^2/2}$ (its characteristic function, [3.1](/3.1)). Hence $g_1(\tau) = \mathrm{e}^{-q^2 D\tau}$. $\square$

A correlator measures the intensity, not the field. Because $E$ is a sum of many independent random phasors, it is a complex Gaussian random variable by the **central limit theorem**, and its fourth moments are determined by its second moments.

**Theorem 8.11.2 (Siegert Relation)** If the scattered field is a complex Gaussian process, the normalized intensity autocorrelation function is

$$
g_2(\tau) = \frac{\langle I(t)I(t+\tau)\rangle}{\langle I\rangle^2} = 1 + \beta\,\lvert g_1(\tau)\rvert^2 ,
$$
where the coherence factor $\beta \le 1$ is set by the number of speckles seen by the detector ($\beta = 1$ for a single coherence area). For Brownian particles $g_2(\tau) - 1 = \beta\,\mathrm{e}^{-2q^2D\tau}$.

**Proof** For a zero-mean complex Gaussian field, Isserlis' theorem gives $\langle E_1^*E_1E_2^*E_2\rangle = \langle E_1^*E_1\rangle\langle E_2^*E_2\rangle + \langle E_1^*E_2\rangle\langle E_2^*E_1\rangle$ (the pairing $\langle E_1E_2\rangle$ vanishes because the phases are uniform). With $E_1 = E(t)$, $E_2 = E(t+\tau)$ this is $\langle I\rangle^2(1 + \lvert g_1(\tau)\rvert^2)$; a finite detector averages over several speckles and reduces the fluctuating part by $\beta$. $\square$

The intensity correlation therefore decays at $2\Gamma$, twice the rate of the field correlation. The often-quoted expression $A(\tau) = A_0\exp[-(8\pi^2n^2/\lambda^2)\sin^2(\theta/2)\,D\tau]$ for the autocorrelation of intensity fluctuations decays at $q^2D/2$ and is too slow by a factor of four.

**Example 8.11.1** A He–Ne laser ($633\,\mathrm{nm}$) at $90^\circ$ in water ($n = 1.332$) gives $q = 4\pi \times 1.332 \times 0.707/633\,\mathrm{nm} = 1.87\times10^7\,\mathrm{m^{-1}}$. For a protein with $R_{\mathrm{h}} = 7\,\mathrm{nm}$ at $25\,^\circ\mathrm{C}$, $D = k_{\mathrm{B}}T/(6\pi\eta R_{\mathrm{h}}) = 3.5\times10^{-11}\,\mathrm{m^2\,s^{-1}}$ and $1/\Gamma = 1/(q^2D) = 82\,\mu\mathrm{s}$; the intensity correlation decays with a time constant of $41\,\mu\mathrm{s}$. A $100\,\mathrm{nm}$ particle decays in $1.2\,\mathrm{ms}$, a $2\,\mathrm{nm}$ peptide in $23\,\mu\mathrm{s}$.

![Dynamic light scattering. A, B: a direct simulation in which 400 independent particles diffuse along the scattering vector and the scattered field is the sum of their phase factors (time in units of 1/Γ). A: the intensity fluctuates as an exponentially distributed speckle. B: the computed intensity autocorrelation g₂ − 1 and field autocorrelation |g₁| follow e^(−2Γτ) and e^(−Γτ), confirming Theorem 8.11.1 and the Siegert relation (Theorem 8.11.2). C: g₂ − 1 for spheres of hydrodynamic radius 2, 7 and 100 nm in water at 25 °C (633 nm, 90°, coherence factor 0.9). D: a sample containing 99.9 % by mass of 5 nm particles and 0.1 % of 100 nm aggregates: because scattering per unit mass grows with molar mass, the aggregates contribute about 80 % of the intensity, and the first two cumulants of the decay-rate distribution give an intensity-weighted radius of 20 nm and a polydispersity index of 2.4](./plots/dls-correlation.py)

### 8.11.2. Data Analysis and Polydispersity

For a mixture of species, $g_1(\tau) = \int G(\Gamma)\,\mathrm{e}^{-\Gamma\tau}\,\mathrm{d}\Gamma$ is the **Laplace transform** of the intensity-weighted distribution of decay rates. Inverting it is ill-posed: exponentials with different rates are nearly linearly dependent, and noise allows many distributions. Two approaches are standard.

**Formula 8.11.1 (Cumulant Expansion)** The logarithm of the field correlation function is expanded in the cumulants of $G(\Gamma)$:

$$
\ln g_1(\tau) = -\bar\Gamma\tau + \frac{\mu_2}{2!}\tau^2 - \frac{\mu_3}{3!}\tau^3 + \cdots, \qquad \mathrm{PDI} = \frac{\mu_2}{\bar\Gamma^2},
$$
where $\bar\Gamma$ is the intensity-weighted mean decay rate, which gives the z-average diffusion coefficient $\bar\Gamma/q^2$ and the corresponding $R_{\mathrm{h}}$, and the polydispersity index PDI is the relative variance of the decay rates (below about $0.1$ for a monodisperse protein).

The second approach is a regularized inverse Laplace transform (the CONTIN program of Stephen Provencher, 1982), which returns a smooth size distribution and can resolve two species whose radii differ by a factor of $2$–$3$ or more, but not closer ones (a difference in molar mass of a factor of $8$–$30$ for compact particles).

The weighting is the main pitfall of DLS. In the Rayleigh regime the intensity scattered per unit mass concentration is proportional to the molar mass, so for compact particles to $R^3$, and per particle to $R^6$. A trace of aggregate, invisible in a gel or a sedimentation profile, can dominate the correlation function (panel D of the figure). This makes DLS an exquisitely sensitive test for aggregation, and a poor method for quantifying a minor large species; size distributions should be reported as intensity distributions or converted to mass with an assumed shape. Samples must be filtered or centrifuged to remove dust, and the viscosity and temperature must be known, since both enter the Stokes–Einstein conversion.

### 8.11.3. Hydrodynamic Radius and Radius of Gyration

DLS gives $R_{\mathrm{h}}$, a measure of friction; static scattering and small-angle X-ray scattering give the radius of gyration $R_{\mathrm{g}}$, the root-mean-square distance of the mass from its center ([7.6.9](/7.6.9)). Their ratio is a shape indicator independent of the absolute size: $R_{\mathrm{g}}/R_{\mathrm{h}} = \sqrt{3/5} = 0.775$ for a homogeneous sphere, about $1$ for a hollow sphere, about $1.5$ for a random coil, and more than $2$ for long rods. Compact proteins have $R_{\mathrm{g}}/R_{\mathrm{h}}$ around $0.75$–$0.8$, because the hydration layer enlarges $R_{\mathrm{h}}$ slightly more than $R_{\mathrm{g}}$.

## 8.12. Choosing a Solution Method

| Method | Measures | Gives | Range and sample | Main limitation |
|---|---|---|---|---|
| DSC | $C_p(T)$ | $\Delta H_{\mathrm{cal}}$, $T_{\mathrm{m}}$, $\Delta C_p$, $\Delta H_{\mathrm{vH}}/\Delta H_{\mathrm{cal}}$ | $0.2$–$2\,\mathrm{mg\,mL^{-1}}$, $0.3\,\mathrm{mL}$ | irreversible unfolding, concentration errors |
| ITC | heat per injection | $n$, $K_{\mathrm{a}}$, $\Delta H_{\mathrm{b}}$, $\Delta C_p$ | $K_{\mathrm{a}} \approx 10^3$–$10^9\,\mathrm{M^{-1}}$ (more by displacement), $\mu\mathrm{M}$ protein | heat of dilution, buffer matching, linked protonation |
| DSF | fluorescence vs $T$ | $T_{\mathrm{m}}$ shifts | microliters, high throughput | indirect, dye artifacts |
| Sedimentation velocity | $c(r, t)$ | $s$, $c(s)$, $f/f_0$, $M$ (with $D$) | $10^3$–$10^9\,\mathrm{Da}$, $0.01$–$10\,\mathrm{mg\,mL^{-1}}$ | shape and hydration coupled in $f$ |
| Sedimentation equilibrium | $c(r)$ at equilibrium | $M$ independent of shape, $K_{\mathrm{d}}$ of self-association, $B$ | hours to days | slow; needs $\bar v$ |
| Viscometry | flow time | $[\eta]$, elongation | mg quantities | insensitive for compact molecules |
| DLS | intensity fluctuations | $D$, $R_{\mathrm{h}}$, polydispersity | $0.5\,\mathrm{nm}$–$2\,\mu\mathrm{m}$, $\mu\mathrm{L}$ | intensity weighting, dust |
| Birefringence, anisotropy | orientation relaxation | $D_{\mathrm{r}}$, length of rods | ns (anisotropy) to ms (birefringence) | needs anisotropic optics or labels |

Hydrodynamic methods and calorimetry complement the structural methods that follow. They do not give atomic coordinates, but they report the state of molecules in the solution in which they work, at concentrations where interactions can be measured, and they test whether a structure determined in a crystal, on a grid or by prediction is the one present in solution.

## Summary

| Quantity or method | Key relation | Use and limits |
|---|---|---|
| Sensitivity | protein adds $\sim 10^{-4}$ of the solution heat capacity; $\mu\mathrm{W}$ power signals | differential cells, matched buffers (Example 8.1.1) |
| Excess heat capacity | $C_{p,\mathrm{ex}} = \Delta P/(\beta n) - C_{p,\mathrm{N}}$; $\Delta H_{\mathrm{cal}} = \int C_{p,\mathrm{ex}}\,\mathrm{d}T$ | Definition 8.1.1 |
| Fluctuation formula | $C_p = \langle\delta H^2\rangle/(k_{\mathrm{B}}T^2) \ge 0$ | Theorem 8.2.1 |
| Two-state thermogram | $f\Delta C_p + f(1-f)\Delta H^2/RT^2$; peak $\Delta H^2/(4RT_{\mathrm{m}}^2)$ | Formula 8.2.1 |
| Ratio test | $\Delta H_{\mathrm{vH}} = 4RT_{\max}^2C_{\max}/\Delta H_{\mathrm{cal}}$; $r = 1$ two-state, $<1$ intermediates, $>1$ oligomers | Definition 8.2.1, Formula 8.2.2 |
| Deconvolution | $\ln Q = \iint C_{p,\mathrm{ex}}/RT^2$ | Formula 8.2.3 |
| Stability curve | $T_H$, $T_S$, $\Delta G_{\max} = \Delta C_p(T_S - T_H)$; cold denaturation at $T_c$ | Formula 8.3.1, Definition 8.3.1 |
| Heat capacity and surface | $\Delta C_p \approx 1.3$–$1.9\,\Delta\mathrm{ASA}_{\mathrm{np}} - 0.6$–$1.1\,\Delta\mathrm{ASA}_{\mathrm{pol}}$ (J/(mol K) per Å²); $\approx 56\,\mathrm{J\,mol^{-1}\,K^{-1}}$ per residue | Formula 8.3.2 |
| Shifts of $T_{\mathrm{m}}$ | $\Delta T_{\mathrm{m}} \approx T_{\mathrm{m}}\Delta\Delta G/\Delta H_{\mathrm{m}}$; ligands: $(RT_{\mathrm{m}}^2/\Delta H_{\mathrm{m}})\ln(1 + [\mathrm{L}]/K_{\mathrm{d}})$ | Formula 8.3.3, DSF (Definition 8.3.2) |
| ITC | quadratic for $[\mathrm{ML}]$; displaced-volume heats; Wiseman isotherm | Definition 8.4.1, Formulas 8.4.1–8.4.3 |
| Wiseman $c$ | $c = nK_{\mathrm{a}}[\mathrm{M}]_{\mathrm{t}}$; $K$ measurable for $1 < c < 1\,000$ | Definition 8.4.2; displacement for tight binders |
| Linked protonation | $\Delta H_{\mathrm{app}} = \Delta H_{\mathrm{b}} + n_{\ce{H+}}\Delta H_{\mathrm{ion}}$ | Formula 8.4.4; Tris vs phosphate |
| Compensation | $\Delta H$ and $T\Delta S$ offset; partly physical ($\Delta C_p$), partly an artifact of correlated errors and the ITC window | Definition 8.4.3 |
| Lipid main transition | $\Delta T_{1/2} = 3.525\,RT_{\mathrm{m}}^2/\Delta H_{\mathrm{vH}}$; DPPC: $41.4\,^\circ\mathrm{C}$, $36\,\mathrm{kJ/mol}$, $n \approx 800$ | Definition 8.5.1, Formula 8.5.1 |
| Volume and hydration | $\bar v \approx 0.73\,\mathrm{mL/g}$ (proteins); $V_{\mathrm{h}} = M(\bar v + \delta\bar v_1)/N_{\mathrm{A}}$, $\delta \approx 0.35$ | Definition 8.6.1, Formula 8.6.1 |
| Friction | $f_0 = 6\pi\eta R$, $D = k_{\mathrm{B}}T/f$, $R_{\mathrm{h}} = k_{\mathrm{B}}T/6\pi\eta D$; $f/f_0$ = hydration × Perrin factor | Definitions 8.7.1–8.7.3, Formula 8.7.1, Example 8.7.1 |
| Rotation | $\tau_{\mathrm{c}} = \eta V/k_{\mathrm{B}}T$ ($6\,\mathrm{ns}$ for lysozyme); rods $D_{\mathrm{r}} \propto \ln p/L^3$; birefringence decay $\mathrm{e}^{-6D_{\mathrm{r}}t}$ | Formula 8.7.2, Definition 8.7.4 |
| Sedimentation velocity | $s = M(1-\bar v\rho)/N_{\mathrm{A}}f$; $M = sRT/D(1-\bar v\rho)$; Lamm equation; plateau $c_0\mathrm{e}^{-2s\omega^2t}$; $s \propto M^{2/3}$ | Formulas 8.8.1–8.8.2, Definitions 8.8.1–8.8.2 |
| Sedimentation equilibrium | $\ln c$ linear in $(r^2 - r_0^2)/2$ with slope $M(1-\bar v\rho)\omega^2/RT$; association curves up, nonideality down; density-gradient band $\sigma_r^2 = RT/(M\bar v\omega^2 r_0\,\mathrm{d}\rho/\mathrm{d}r)$ | Formulas 8.9.1–8.9.3 |
| Viscosity | $[\eta] = \nu v_{\mathrm{h}}$, $\nu = 2.5$ (sphere), $\propto p^2/\ln p$ (rods); Scheraga–Mandelkern $\beta$ nearly shape-independent | Formula 8.10.1, §8.10.2 |
| Dynamic light scattering | $q = (4\pi n/\lambda_0)\sin(\theta/2)$; $g_1 = \mathrm{e}^{-q^2D\tau}$; $g_2 = 1 + \beta g_1^2$; cumulants give $R_{\mathrm{h}}$ (z-average) and PDI; intensity weighting $\propto R^6$ per particle | Theorems 8.11.1–8.11.2, Formula 8.11.1 |
| Shape indicator | $R_{\mathrm{g}}/R_{\mathrm{h}}$: $0.775$ sphere, $\approx 1.5$ coil, $> 2$ rod | §8.11.3 |

## Questions

1. A $0.5\,\mathrm{mL}$ DSC cell contains lysozyme ($14.3\,\mathrm{kDa}$) at $0.5\,\mathrm{mg\,mL^{-1}}$; it unfolds at $75\,^\circ\mathrm{C}$ with $\Delta H = 450\,\mathrm{kJ\,mol^{-1}}$. Estimate the total heat of unfolding and the peak excess power at a scan rate of $1\,\mathrm{K\,min^{-1}}$.

   **Answer** Amount: $0.5\times10^{-3}\,\mathrm{L} \times 0.5\,\mathrm{g\,L^{-1}}/14\,300\,\mathrm{g\,mol^{-1}} = 1.75\times10^{-8}\,\mathrm{mol}$; heat $1.75\times10^{-8} \times 450\,000 = 7.9\,\mathrm{mJ}$. Peak molar excess heat capacity $\Delta H^2/(4RT_{\mathrm{m}}^2) = 450\,000^2/(4 \times 8.314 \times 348.15^2) = 50\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$, so the sample adds $0.88\,\mathrm{mJ\,K^{-1}}$ and the peak power is $0.88\,\mathrm{mJ\,K^{-1}} \times \tfrac{1}{60}\,\mathrm{K\,s^{-1}} = 15\,\mu\mathrm{W}$.

2. Use Theorem 8.2.1 to explain why the heat capacity of a protein solution cannot dip below the baselines anywhere during a reversible equilibrium transition, and what it means if a measured thermogram shows an exothermic dip after the endothermic peak.

   **Answer** The heat capacity is a variance divided by $k_{\mathrm{B}}T^2$, so in equilibrium it cannot be negative, and the excess over a smooth interpolated baseline (the progress baseline) is $f(1-f)\Delta H^2/RT^2 \ge 0$. An exothermic dip means the system is not in equilibrium: typically the unfolded protein aggregates (aggregation releases heat), an irreversible process that the equilibrium formula does not describe. The rescan and scan-rate tests of §8.2.4 confirm it.

3. A dimeric protein unfolds as $\mathrm{N_2} \rightleftharpoons 2\mathrm{U}$ with $\Delta H = 600\,\mathrm{kJ}$ per mole of dimer. Show that the midpoint temperature depends on the total chain concentration $C_{\mathrm{t}}$, and estimate how much $T_{\mathrm{m}}$ changes for a tenfold increase of $C_{\mathrm{t}}$ near $T_{\mathrm{m}} = 330\,\mathrm{K}$.

   **Answer** With $f$ the fraction of chains unfolded, $[\mathrm{U}] = fC_{\mathrm{t}}$ and $[\mathrm{N_2}] = (1-f)C_{\mathrm{t}}/2$, so $K = 2C_{\mathrm{t}}f^2/(1-f)$, and at $f = 1/2$, $K(T_{\mathrm{m}}) = C_{\mathrm{t}}$. By the van 't Hoff equation $\mathrm{d}\ln K/\mathrm{d}(1/T) = -\Delta H/R$, so $\Delta(1/T_{\mathrm{m}}) = -(R/\Delta H)\Delta\ln C_{\mathrm{t}}$ and $\Delta T_{\mathrm{m}} \approx (RT_{\mathrm{m}}^2/\Delta H)\ln 10 = 8.314 \times 330^2/600\,000 \times 2.303 = 3.5\,\mathrm{K}$, an increase with concentration. A concentration-dependent $T_{\mathrm{m}}$ is a direct diagnostic of dissociation coupled to unfolding.

4. A protein has $T_{\mathrm{m}} = 50\,^\circ\mathrm{C}$, $\Delta H_{\mathrm{m}} = 250\,\mathrm{kJ\,mol^{-1}}$ and $\Delta C_p = 8\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$. Compute $T_H$, $T_S$, the maximal stability and the cold-denaturation temperature. Would you expect to see cold denaturation in an ordinary experiment?

   **Answer** $T_H = 323.15 - 250/8 = 291.9\,\mathrm{K}$ ($18.8\,^\circ\mathrm{C}$); $T_S = 323.15\,\mathrm{e}^{-250/(323.15\times8)} = 293.4\,\mathrm{K}$ ($20.2\,^\circ\mathrm{C}$); $\Delta G_{\max} = 8 \times (293.4 - 291.9) = 11.7\,\mathrm{kJ\,mol^{-1}}$. Solving $\Delta G(T) = 0$ below $T_S$ numerically gives $T_c = 264.6\,\mathrm{K}$ ($-8.6\,^\circ\mathrm{C}$): below the freezing point, but close enough that a modest destabilization (a mutation, or $1$–$2\,\mathrm{M}$ urea) would bring cold denaturation above $0\,^\circ\mathrm{C}$. The large $\Delta C_p$ relative to $\Delta H$ is what makes the curve so narrow.

5. Using the relations of Myers, Pace and Scholtz, predict $\Delta_{\mathrm{U}}C_p$ for a $150$-residue protein. If its DSC peak is at $65\,^\circ\mathrm{C}$ with $\Delta H_{\mathrm{m}} = 500\,\mathrm{kJ\,mol^{-1}}$, what is its unfolding enthalpy at $25\,^\circ\mathrm{C}$?

   **Answer** $\Delta\mathrm{ASA} = -907 + 93 \times 150 = 13\,043\,\text{Å}^2$; $\Delta C_p = (-251 + 0.19 \times 13\,043) \times 4.184\,\mathrm{J\,mol^{-1}\,K^{-1}} = 9.3\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$. Then $\Delta H(25\,^\circ\mathrm{C}) = 500 + 9.3 \times (298.15 - 338.15) = 500 - 372 = 128\,\mathrm{kJ\,mol^{-1}}$: a quarter of the value at $T_{\mathrm{m}}$. The enthalpy of unfolding depends so strongly on temperature that values must always be quoted with their temperature.

6. Design an ITC experiment for a protein–ligand pair with expected $K_{\mathrm{d}} \approx 2\,\mu\mathrm{M}$ and $\Delta H_{\mathrm{b}} \approx -15\,\mathrm{kJ\,mol^{-1}}$ in a $200\,\mu\mathrm{L}$ cell. Choose the cell and syringe concentrations and check that the first injections give enough heat.

   **Answer** For $c = 20$, $[\mathrm{M}]_{\mathrm{t}} = cK_{\mathrm{d}} = 40\,\mu\mathrm{M}$ of sites; to reach a molar ratio of about $2$ with $40\,\mu\mathrm{L}$ of injections into $200\,\mu\mathrm{L}$, the syringe needs about $10$ times that, $400$–$450\,\mu\mathrm{M}$. A $2\,\mu\mathrm{L}$ injection of $450\,\mu\mathrm{M}$ ligand delivers $0.9\,\mathrm{nmol}$; if most of it binds early in the titration, the heat is $0.9\times10^{-9} \times 15\,000 = 13.5\,\mu\mathrm{J}$, about a hundred times the noise. Buffer matching is critical at these concentrations, and a ligand-into-buffer blank must be subtracted.

7. Binding of an inhibitor gives $\Delta H_{\mathrm{app}} = -50\,\mathrm{kJ\,mol^{-1}}$ in phosphate and $-16\,\mathrm{kJ\,mol^{-1}}$ in Tris at the same pH. How many protons are taken up, what is the intrinsic binding enthalpy, and what experiment would identify the group that is protonated?

   **Answer** Formula 8.4.4: $n_{\ce{H+}} = (-16 + 50)/(47.45 - 3.6) = 0.78$, and $\Delta H_{\mathrm{b}} = -50 - 0.78 \times 3.6 = -52.8\,\mathrm{kJ\,mol^{-1}}$. A fractional number means a group whose $\mathrm{p}K_{\mathrm{a}}$ shifts across the working pH on binding. To identify it: repeat the measurement at several pH values (the uptake peaks near the average of the free and bound $\mathrm{p}K_{\mathrm{a}}$), mutate candidate His, Asp, Glu or Lys residues near the site and check whether the uptake disappears, or measure $\mathrm{p}K_{\mathrm{a}}$ values directly by NMR titration ([7.6.13](/7.6.13)).

8. (Open) Simulate in your head, or with a few lines of Python, a series of $20$ complexes whose $\Delta H$ values are random between $-100$ and $0\,\mathrm{kJ\,mol^{-1}}$ and whose $\Delta G$ values are random between $-50$ and $-20\,\mathrm{kJ\,mol^{-1}}$, independently. What is the slope of $T\Delta S$ against $\Delta H$? What does this imply for claims of enthalpy–entropy compensation?

   **Answer** $T\Delta S = \Delta H - \Delta G$, and since $\Delta H$ varies over $100\,\mathrm{kJ\,mol^{-1}}$ while $\Delta G$ varies over only $30$ (with variances $833$ and $75$), the regression of $T\Delta S$ on $\Delta H$ has slope $1 - \operatorname{Cov}(\Delta G, \Delta H)/\operatorname{Var}(\Delta H) \approx 1$ and a correlation coefficient of about $0.96$, with no physics at all. A compensation claim is meaningful only if the range of $\Delta G$ is not limited by the method, if errors are propagated (preferably by plotting $\Delta G$ against $\Delta H$, which are measured independently), and if the slope differs significantly from what independent random values produce.

9. Dimyristoylphosphatidylcholine (DMPC) has its main transition at $24\,^\circ\mathrm{C}$ with $\Delta H_{\mathrm{cal}} = 25\,\mathrm{kJ\,mol^{-1}}$. If the peak of multilamellar vesicles is $0.2\,\mathrm{K}$ wide, how large is the cooperative unit? How would incorporating a transmembrane peptide at $2$ mol % change the thermogram, and why?

   **Answer** $\Delta H_{\mathrm{vH}} = 3.525 \times 8.314 \times 297.15^2/0.2 = 1.29\times10^4\,\mathrm{kJ\,mol^{-1}}$, $n = 12\,900/25 \approx 520$ lipids. A transmembrane peptide disrupts the packing of its neighbors and acts as a defect: the peak broadens (smaller cooperative unit), its area decreases if boundary lipids no longer take part in the transition, and $T_{\mathrm{m}}$ shifts up or down depending on whether the peptide's hydrophobic length is longer or shorter than the bilayer thickness (hydrophobic mismatch, [7.6.24](/7.6.24)).

10. In a thermal shift screen a fragment raises the $T_{\mathrm{m}}$ of a protein ($T_{\mathrm{m}} = 330\,\mathrm{K}$, $\Delta H_{\mathrm{m}} = 400\,\mathrm{kJ\,mol^{-1}}$) by $8\,\mathrm{K}$ at $100\,\mu\mathrm{M}$. Estimate its $K_{\mathrm{d}}$ and list the assumptions.

    **Answer** From Formula 8.3.3, $\ln(1 + [\mathrm{L}]/K_{\mathrm{d}}) \approx \Delta T_{\mathrm{m}}\Delta H_{\mathrm{m}}/(RT_{\mathrm{m}}^2) = 8 \times 400\,000/(8.314 \times 330^2) = 3.53$, so $[\mathrm{L}]/K_{\mathrm{d}} \approx 33$ and $K_{\mathrm{d}} \approx 3\,\mu\mathrm{M}$ at $T_{\mathrm{m}}'$. Assumptions: binding only to the native state, ligand in large excess over protein, $K_{\mathrm{d}}$ independent of temperature (otherwise it refers to about $65\,^\circ\mathrm{C}$, not to room temperature), the small-shift approximation (the exact equation gives a somewhat larger ratio), and no effect of the dye. The estimate is therefore good to a factor of a few; ITC would be the next step.

11. Proteins from thermophiles reach higher $T_{\mathrm{m}}$ in three ways: a higher maximal stability, a flatter stability curve (smaller $\Delta C_p$), or a curve shifted to higher temperature. Starting from the protein of Example 8.3.1 ($T_S = 279.6\,\mathrm{K}$, $\Delta G_{\max} = 28.9\,\mathrm{kJ\,mol^{-1}}$, $\Delta C_p = 6\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$), compute $T_{\mathrm{m}}$ when (a) $\Delta G_{\max}$ is doubled, (b) $\Delta C_p$ is reduced to $4$, (c) $T_S$ is raised by $15\,\mathrm{K}$, each change alone.

    **Answer** Around its maximum the stability curve can be written $\Delta G(T) = \Delta G_{\max} - \Delta C_p\,[T\ln(T/T_S) - (T - T_S)]$, since $\Delta S(T_S) = 0$ and $\Delta H(T_S) = \Delta G_{\max}$. Solving $\Delta G = 0$ numerically: the original protein has $T_{\mathrm{m}} = 60.0\,^\circ\mathrm{C}$; (a) doubling $\Delta G_{\max}$ gives $83.0\,^\circ\mathrm{C}$; (b) $\Delta C_p = 4$ gives $72.4\,^\circ\mathrm{C}$ (and also lowers $T_c$ from $-43.8$ to $-54.6\,^\circ\mathrm{C}$, widening the whole curve); (c) shifting $T_S$ by $15\,\mathrm{K}$ gives $76.3\,^\circ\mathrm{C}$. Each mechanism is found in real thermophilic proteins, often in combination; comparisons of homologs show that a modest increase of $\Delta G_{\max}$ by a few ion pairs or a more compact core is the most common, and that the stability at the growth temperature of the organism is similar for mesophilic and thermophilic homologs.

12. The boundary of a $4.4\,\mathrm{S}$ protein starts at the meniscus ($6.0\,\mathrm{cm}$). How long does it take to reach $7.0\,\mathrm{cm}$ at $40\,000$ and at $60\,000\,\mathrm{rpm}$, and by how much has the plateau diluted by then?

    **Answer** From Formula 8.8.2, $t = \ln(7.0/6.0)/(s\omega^2)$. At $40\,000\,\mathrm{rpm}$, $\omega = 4\,189\,\mathrm{s^{-1}}$, $s\omega^2 = 7.7\times10^{-6}\,\mathrm{s^{-1}}$ and $t = 0.154/7.7\times10^{-6} = 2.0\times10^4\,\mathrm{s} = 5.5\,\mathrm{h}$; at $60\,000\,\mathrm{rpm}$, $(2.25$ times faster$)$ $2.5\,\mathrm{h}$. In both cases the plateau has diluted by $\mathrm{e}^{-2 \times 0.154} = 0.73$, that is to $(6.0/7.0)^2$: radial dilution depends only on how far the boundary has moved.

13. Catalase has $s_{20,\mathrm{w}} = 11.3\,\mathrm{S}$, $D_{20,\mathrm{w}} = 4.1\times10^{-7}\,\mathrm{cm^2\,s^{-1}}$ and $\bar v = 0.73\,\mathrm{mL\,g^{-1}}$. Compute its molar mass, hydrodynamic radius and frictional ratio, and compare with the tetramer of $60\,\mathrm{kDa}$ subunits.

    **Answer** Svedberg equation: $M = sRT/(D(1 - \bar v\rho)) = 11.3\times10^{-13} \times 8.314 \times 293.15/(4.1\times10^{-11} \times 0.271) = 248\,\mathrm{kg\,mol^{-1}}$, a tetramer of about $62\,\mathrm{kDa}$ subunits. $R_{\mathrm{h}} = k_{\mathrm{B}}T/(6\pi\eta D) = 4.05\times10^{-21}/(6\pi \times 1.002\times10^{-3} \times 4.1\times10^{-11}) = 5.2\,\mathrm{nm}$; the anhydrous sphere has $R_0 = (3M\bar v/4\pi N_{\mathrm{A}})^{1/3} = 4.1\,\mathrm{nm}$, so $f/f_0 = 1.27$: a compact, slightly asymmetric and hydrated particle (panel C of the shape figure).

14. A DLS instrument measures at $173^\circ$ (backscattering) with a $633\,\mathrm{nm}$ laser. The intensity correlation of a protein solution at $25\,^\circ\mathrm{C}$ decays as $\mathrm{e}^{-\tau/50\,\mu\mathrm{s}}$. What is $R_{\mathrm{h}}$? What would be obtained if the decay were wrongly attributed to $g_1$?

    **Answer** $q = 4\pi \times 1.332\sin(86.5^\circ)/633\,\mathrm{nm} = 2.64\times10^7\,\mathrm{m^{-1}}$. By the Siegert relation $g_2 - 1 \propto \mathrm{e}^{-2\Gamma\tau}$, so $2\Gamma = 1/(50\,\mu\mathrm{s})$, $\Gamma = 10^4\,\mathrm{s^{-1}}$, $D = \Gamma/q^2 = 1.44\times10^{-11}\,\mathrm{m^2\,s^{-1}}$ and $R_{\mathrm{h}} = k_{\mathrm{B}}T/(6\pi\eta D) = 17\,\mathrm{nm}$. Taking the measured decay rate as $\Gamma$ would halve $D$ and double the radius to $34\,\mathrm{nm}$; using the incorrect $q^2/2$ convention would give a fourfold error.

15. A protein that should be a $45\,\mathrm{kDa}$ monomer gives, at sedimentation equilibrium at $15\,000\,\mathrm{rpm}$ and $20\,^\circ\mathrm{C}$ ($\bar v = 0.74\,\mathrm{mL\,g^{-1}}$), a straight $\ln c$ versus $\xi$ plot with slope $1.20\,\mathrm{cm^{-2}}$ at a loading of $0.3\,\mathrm{g\,L^{-1}}$ and an upward-curved plot whose limiting slope at the bottom of the cell is $2.0\,\mathrm{cm^{-2}}$ at $3\,\mathrm{g\,L^{-1}}$. Interpret.

    **Answer** Formula 8.9.1: $M = \sigma RT/((1 - \bar v\rho)\omega^2) = 1.20\times10^4\,\mathrm{m^{-2}} \times 8.314 \times 293.15/(0.261 \times 1\,571^2) = 45\,\mathrm{kg\,mol^{-1}}$: at low concentration the protein is a monomer. At higher concentration the local apparent molar mass rises to about $2.0/1.2 \times 45 = 75\,\mathrm{kDa}$ at the bottom, and the curvature together with its dependence on loading concentration indicates reversible self-association (probably monomer–dimer, with $K_{\mathrm{d}}$ of the order of the local concentrations, $\sim 10$–$50\,\mu\mathrm{M}$). A global fit of both data sets with Formula 8.9.2 would give the stoichiometry and $K_{\mathrm{d}}$; a sedimentation-velocity run would show a single reaction boundary whose $s$ increases with concentration.

16. (Open) A purified enzyme looks homogeneous on a denaturing gel, but its DLS gives $R_{\mathrm{h}} = 9\,\mathrm{nm}$ with PDI $0.45$, while the crystal structure of the expected dimer predicts $R_{\mathrm{h}} \approx 4\,\mathrm{nm}$. Design a set of solution measurements to decide what is in the tube.

    **Answer** The DLS result is intensity-weighted, so a small mass fraction of large aggregates can explain it (panel D of the DLS figure). First, centrifuge or filter and remeasure, and do sedimentation velocity: the $c(s)$ distribution gives the mass fractions of dimer, higher oligomers and aggregates directly. Size-exclusion chromatography with multi-angle static light scattering ([7.6.9](/7.6.9)) gives the absolute molar mass of each eluting species. If the main species is the dimer, compare its $s$ and $R_{\mathrm{h}}$ with values computed from the crystal structure (HYDROPRO) to confirm that its solution shape matches; DSC or DSF would show whether the aggregates form because the protein is marginally stable in this buffer, and a buffer screen by DSF could find better conditions.

