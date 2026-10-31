---
title: "Solution Methods: Calorimetry and Hydrodynamics"
description: Calorimetry of biological macromolecules. Signals and sensitivity; differential scanning calorimetry, excess heat capacity and the fluctuation formula; two-state thermograms, the van 't Hoff to calorimetric enthalpy ratio, multistate deconvolution, irreversible and oligomeric unfolding; the thermodynamic decomposition of stability, cold denaturation, heat capacity and buried surface; mutations and ligands shift T_m, thermal shift assays; isothermal titration calorimetry, the binding isotherm, the Wiseman c value and experimental design; linked protonation and enthalpy–entropy compensation; the main transition of lipid bilayers and the cooperative unit.
---

Every measurement of the stability of a protein or of the strength of a binding interaction is in the end a measurement of a free energy, and free energies are what thermodynamics relates to heat. Most methods infer $\Delta G$ indirectly, from a spectroscopic signal that reports the populations of two states, and then obtain the enthalpy from the temperature dependence of $\Delta G$ through the **van 't Hoff equation**. Calorimetry measures the heat itself. A differential scanning calorimeter records the **heat capacity** of a dilute protein solution as it is heated through unfolding, and its integral is the enthalpy of unfolding with no model assumed; an isothermal titration calorimeter measures the heat released by each small addition of a ligand, and a single experiment gives the stoichiometry, the binding constant and the binding enthalpy. Comparing the calorimetric enthalpy with the one implied by the shape of a transition tests whether the transition is two-state, which no spectroscopic method can do alone.

The thermodynamics used here (the **Gibbs–Helmholtz equation**, **enthalpy**, **entropy** and heat capacity) is that of [6.3](/6.3), and calorimeters were introduced in [6.3.1](/6.3.1#sec-1.7); the **two-state model** of unfolding, the **protein stability curve** and chemical denaturation were derived in [7.1.6](/7.1.6#sec-6.2). This chapter is about measurement: what a calorimeter records, how the records are analyzed, what the numbers mean physically, and how experiments are designed. The same quantities return in the folding chapter ([7.6.22](/7.6.22)), in molecular recognition ([7.6.25](/7.6.25)) and, for the lipid phase transition, in the physics of membranes ([7.6.33](/7.6.33)).

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

**Example 8.5.1** The main transition of multilamellar DPPC vesicles has $\Delta T_{1/2} \approx 0.1\,\mathrm{K}$. Formula 8.5.1 gives $\Delta H_{\mathrm{vH}} = 3.525 \times 8.314 \times 314.55^2/0.1\,\mathrm{J\,mol^{-1}} = 2.9\times10^4\,\mathrm{kJ\,mol^{-1}}$, and with $\Delta H_{\mathrm{cal}} = 36\,\mathrm{kJ\,mol^{-1}}$ the cooperative unit is $n \approx 800$ lipids: patches of a few hundred square nanometers of bilayer melt as a whole. Anything that disturbs the packing (small vesicles with strongly curved bilayers, impurities, cholesterol, membrane proteins) broadens the peak and reduces $n$; above about $30$ mol % cholesterol the transition is no longer detectable, because cholesterol creates the liquid-ordered phase in which chains are ordered but mobile ([7.6.33](/7.6.33)).

Cells keep their membranes near or above this transition by adjusting the length and saturation of their fatty acids, a response called homeoviscous adaptation: bacteria grown at lower temperature incorporate more unsaturated or branched chains, so that the transition of their membrane lipids stays below the growth temperature.

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

   **Answer** Formula 8.4.4: $n_{\ce{H+}} = (-16 + 50)/(47.45 - 3.6) = 0.78$, and $\Delta H_{\mathrm{b}} = -50 - 0.78 \times 3.6 = -52.8\,\mathrm{kJ\,mol^{-1}}$. A fractional number means a group whose $\mathrm{p}K_{\mathrm{a}}$ shifts across the working pH on binding. To identify it: repeat the measurement at several pH values (the uptake peaks near the average of the free and bound $\mathrm{p}K_{\mathrm{a}}$), mutate candidate His, Asp, Glu or Lys residues near the site and check whether the uptake disappears, or measure $\mathrm{p}K_{\mathrm{a}}$ values directly by NMR titration ([7.6.18](/7.6.18)).

8. (Open) Simulate in your head, or with a few lines of Python, a series of $20$ complexes whose $\Delta H$ values are random between $-100$ and $0\,\mathrm{kJ\,mol^{-1}}$ and whose $\Delta G$ values are random between $-50$ and $-20\,\mathrm{kJ\,mol^{-1}}$, independently. What is the slope of $T\Delta S$ against $\Delta H$? What does this imply for claims of enthalpy–entropy compensation?

   **Answer** $T\Delta S = \Delta H - \Delta G$, and since $\Delta H$ varies over $100\,\mathrm{kJ\,mol^{-1}}$ while $\Delta G$ varies over only $30$ (with variances $833$ and $75$), the regression of $T\Delta S$ on $\Delta H$ has slope $1 - \operatorname{Cov}(\Delta G, \Delta H)/\operatorname{Var}(\Delta H) \approx 1$ and a correlation coefficient of about $0.96$, with no physics at all. A compensation claim is meaningful only if the range of $\Delta G$ is not limited by the method, if errors are propagated (preferably by plotting $\Delta G$ against $\Delta H$, which are measured independently), and if the slope differs significantly from what independent random values produce.

9. Dimyristoylphosphatidylcholine (DMPC) has its main transition at $24\,^\circ\mathrm{C}$ with $\Delta H_{\mathrm{cal}} = 25\,\mathrm{kJ\,mol^{-1}}$. If the peak of multilamellar vesicles is $0.2\,\mathrm{K}$ wide, how large is the cooperative unit? How would incorporating a transmembrane peptide at $2$ mol % change the thermogram, and why?

   **Answer** $\Delta H_{\mathrm{vH}} = 3.525 \times 8.314 \times 297.15^2/0.2 = 1.29\times10^4\,\mathrm{kJ\,mol^{-1}}$, $n = 12\,900/25 \approx 520$ lipids. A transmembrane peptide disrupts the packing of its neighbors and acts as a defect: the peak broadens (smaller cooperative unit), its area decreases if boundary lipids no longer take part in the transition, and $T_{\mathrm{m}}$ shifts up or down depending on whether the peptide's hydrophobic length is longer or shorter than the bilayer thickness (hydrophobic mismatch, [7.6.33](/7.6.33)).

10. In a thermal shift screen a fragment raises the $T_{\mathrm{m}}$ of a protein ($T_{\mathrm{m}} = 330\,\mathrm{K}$, $\Delta H_{\mathrm{m}} = 400\,\mathrm{kJ\,mol^{-1}}$) by $8\,\mathrm{K}$ at $100\,\mu\mathrm{M}$. Estimate its $K_{\mathrm{d}}$ and list the assumptions.

    **Answer** From Formula 8.3.3, $\ln(1 + [\mathrm{L}]/K_{\mathrm{d}}) \approx \Delta T_{\mathrm{m}}\Delta H_{\mathrm{m}}/(RT_{\mathrm{m}}^2) = 8 \times 400\,000/(8.314 \times 330^2) = 3.53$, so $[\mathrm{L}]/K_{\mathrm{d}} \approx 33$ and $K_{\mathrm{d}} \approx 3\,\mu\mathrm{M}$ at $T_{\mathrm{m}}'$. Assumptions: binding only to the native state, ligand in large excess over protein, $K_{\mathrm{d}}$ independent of temperature (otherwise it refers to about $65\,^\circ\mathrm{C}$, not to room temperature), the small-shift approximation (the exact equation gives a somewhat larger ratio), and no effect of the dye. The estimate is therefore good to a factor of a few; ITC would be the next step.

11. Proteins from thermophiles reach higher $T_{\mathrm{m}}$ in three ways: a higher maximal stability, a flatter stability curve (smaller $\Delta C_p$), or a curve shifted to higher temperature. Starting from the protein of Example 8.3.1 ($T_S = 279.6\,\mathrm{K}$, $\Delta G_{\max} = 28.9\,\mathrm{kJ\,mol^{-1}}$, $\Delta C_p = 6\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$), compute $T_{\mathrm{m}}$ when (a) $\Delta G_{\max}$ is doubled, (b) $\Delta C_p$ is reduced to $4$, (c) $T_S$ is raised by $15\,\mathrm{K}$, each change alone.

    **Answer** Around its maximum the stability curve can be written $\Delta G(T) = \Delta G_{\max} - \Delta C_p\,[T\ln(T/T_S) - (T - T_S)]$, since $\Delta S(T_S) = 0$ and $\Delta H(T_S) = \Delta G_{\max}$. Solving $\Delta G = 0$ numerically: the original protein has $T_{\mathrm{m}} = 60.0\,^\circ\mathrm{C}$; (a) doubling $\Delta G_{\max}$ gives $83.0\,^\circ\mathrm{C}$; (b) $\Delta C_p = 4$ gives $72.4\,^\circ\mathrm{C}$ (and also lowers $T_c$ from $-43.8$ to $-54.6\,^\circ\mathrm{C}$, widening the whole curve); (c) shifting $T_S$ by $15\,\mathrm{K}$ gives $76.3\,^\circ\mathrm{C}$. Each mechanism is found in real thermophilic proteins, often in combination; comparisons of homologs show that a modest increase of $\Delta G_{\max}$ by a few ion pairs or a more compact core is the most common, and that the stability at the growth temperature of the organism is similar for mesophilic and thermophilic homologs.
