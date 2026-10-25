---
title: "Bioenergetics: Free Energy, ATP, and Biological Redox Reactions"
description: Opening of Part II. Catabolism and anabolism and the pathway card; the biochemical standard state, ΔrG′° versus the actual ΔrG in cells, additivity and coupling; phosphoryl group transfer, why ATP hydrolysis is exergonic, the phosphorylation potential in cells, high-energy compounds, ATP as a group donor, transphosphorylations and phosphocreatine; oxidation states of carbon, standard reduction potentials and ΔrG′° = −zFΔE′°; NAD, NADP and the flavoproteins.
---

Part I of this course explained how the structure of biomolecules follows from their chemistry ([7.1.1](/7.1.1)). Part II (7.1.16–7.1.29) asks what cells do with these molecules: how they extract free energy from fuels or light, how they convert nutrients into their own components, and how thousands of reactions are kept in step with each other. The thread announced in [7.1.1](/7.1.1) organizes all of it: energy balance plus feedback control. Every pathway has an energy account (what it consumes and produces in ATP and reducing power), and every pathway has a few steps, far from equilibrium, where its rate is set by activators, inhibitors, covalent modification and hormones. This chapter supplies the energy side of the thread: the biochemical conventions of thermodynamics, the energy currency ATP and the electron carriers NAD, NADP and the flavins. The next chapter ([7.1.17](/7.1.17)) supplies the chemical and regulatory side. The physical chemistry behind both (**Gibbs free energy**, the **equilibrium constant**, **coupled reactions**, the **Nernst equation**) was developed in [6.3.3](/6.3.3)–[6.3.7](/6.3.7) and [6.1.11](/6.1.11); we use it without repeating the derivations and concentrate on the biochemical conventions and the numbers that matter in cells.

## 16.1. Metabolism and Its Two Currencies

### 16.1.1. Catabolism and Anabolism

**Metabolism**, the entire set of enzyme-catalyzed transformations in an organism ([7.1.1](/7.1.1#sec-1.3.3)), has two directions.

**Definition 16.1.1 (Catabolism and Anabolism)** **Catabolism** is the degradative part of metabolism, in which organic nutrients (carbohydrates, fats, proteins) are converted into smaller, simpler end products ($\ce{CO2}$, $\ce{NH3}$, lactate, ethanol) with release of free energy, part of which is conserved as ATP and as reduced electron carriers (NADH, NADPH, $\ce{FADH2}$). **Anabolism** (biosynthesis) is the synthetic part, in which small precursors are built up into larger, more complex molecules (proteins, nucleic acids, polysaccharides, lipids) with input of free energy, supplied by ATP and NADPH.

Catabolism proceeds in three stages, which converge:

1. Stage I: the macromolecules of food or of the cell's own stores are hydrolyzed (or phosphorolyzed) to their building blocks: polysaccharides to hexoses, triacylglycerols to fatty acids and glycerol, proteins to amino acids. Almost no free energy is conserved.
2. Stage II: the building blocks are degraded to a few common intermediates, above all acetyl-CoA; some ATP and NADH are formed (glycolysis, 7.1.18; β oxidation, 7.1.21; amino acid oxidation, 7.1.22).
3. Stage III: the acetyl group is oxidized to $\ce{CO2}$ in the citric acid cycle (7.1.20), and the electrons collected as NADH and $\ce{FADH2}$ flow to $\ce{O2}$ in the respiratory chain, which drives most ATP synthesis (oxidative phosphorylation, 7.1.23).

Anabolism diverges from a small number of precursors (pyruvate, acetyl-CoA, citric acid cycle intermediates, ribose 5-phosphate) to thousands of products. Catabolic and anabolic routes between the same two compounds are never the simple reverse of each other: at least one step differs, so that each direction can be regulated separately and each is thermodynamically favorable in its own direction (7.1.17, 7.1.19). The two directions are often in different compartments (fatty acid oxidation in the mitochondrial matrix, fatty acid synthesis in the cytosol). Besides linear pathways there are converging (catabolic), diverging (anabolic) and cyclic ones (the citric acid cycle, the urea cycle), in which one starting component is regenerated in every turn.

![Catabolism and anabolism are coupled through two currencies. Left: the three stages of catabolism converge from proteins, polysaccharides and lipids (stage I, hydrolysis to amino acids, hexoses, fatty acids and glycerol) through a few intermediates, above all acetyl-CoA (stage II), to the citric acid cycle and oxidative phosphorylation (stage III), which end in CO₂, H₂O and NH₃. Right: anabolism diverges from a few precursors to the macromolecules of the cell. Centre: the free energy released by catabolism is passed on as ATP (from ADP + Pᵢ) and as reducing power, NADH (mainly used for ATP synthesis) and NADPH (used for reductive biosynthesis); their consumption drives biosynthesis, transport across membranes, movement and other work, and regenerates ADP and NADP⁺](./plots/energy-coupling.py)

### 16.1.2. ATP and NAD(P)H

The coupling between the two directions runs through a few carrier molecules. ATP carries free energy as a high phosphoryl group transfer potential (16.3); NADH and NADPH carry reducing power, electrons at a low reduction potential (16.4–16.5); acetyl-CoA carries activated acyl groups. Catabolism regenerates them, anabolism and work consume them, and their concentrations are held far from equilibrium, so that consuming them is always strongly exergonic. Most of Part II can be read as the bookkeeping of these carriers: for each pathway, how many ATP and how many NAD(P)H it consumes or produces per molecule of substrate.

The golden age of the subject, from the 1920s to the 1960s, worked out glycolysis, the citric acid cycle, oxidative phosphorylation and glycogen metabolism and the role of ATP, and earned some fifteen Nobel Prizes. Metabolism has had a revival since about 2010: mass spectrometry measures hundreds of metabolites at once (metabolomics), isotope tracers measure fluxes in living tissues, and altered metabolism turned out to be central to cancer, diabetes and immunity.

### 16.1.3. The Pathway Card

To keep the detail of Part II in order, each chapter summarizes each pathway on a card with the same fields. The fields answer the question asked of every pathway in [7.1.1](/7.1.1): where does it run, what is its net reaction and energy account, which step is committed and far from equilibrium, who activates and who inhibits it, and how is the opposing pathway switched off.

| Field | What it records |
|---|---|
| Location | organisms, tissues and compartment (cytosol, matrix, ER, chloroplast) |
| Net reaction | input → output, balanced for the carriers (ATP, NAD(P)H, CoA) |
| Energy account | ATP and NAD(P)H per substrate; $\Delta_{\mathrm{r}}G'^{\circ}$ and the actual $\Delta_{\mathrm{r}}G$ in the cell |
| Committed and regulated steps | the steps far from equilibrium (7.1.17), first the committed step |
| Activators / inhibitors | allosteric effectors of the regulated enzymes; feedback and feedforward |
| Covalent, hormonal and transcriptional control | phosphorylation and its hormones (insulin, glucagon, epinephrine), induction of enzymes |
| Opposing pathway | the reverse route, the enzymes unique to it, and how the two are regulated reciprocally |
| Coenzymes (vitamins) | the coenzymes required and their vitamin precursors (table in [7.1.17](/7.1.17#sec-17.2)) |
| Diseases and drugs | inherited defects, deficiency diseases, inhibitors used as drugs or poisons |

The first card, for glycolysis, is in [7.1.18](/7.1.18); the card of every pathway is collected again in the course summary (7.1.30).

## 16.2. Bioenergetics and Thermodynamics

**Definition 16.2.1 (Bioenergetics)** **Bioenergetics** is the quantitative study of the energy transductions in living cells (the conversions of one form of energy into another) and of the chemical processes underlying them.

Cells need energy to build and maintain their ordered structures, to move, to maintain concentration and electrical gradients across their membranes, in some cases to keep a body temperature or to emit light. Biological energy transformations obey the **first law of thermodynamics** and the **second law of thermodynamics** like any other ([5.2](/5.2), [6.3.2](/6.3.2)). Living organisms are **open systems** that create internal order by exporting entropy to their surroundings: they take up free energy as nutrients or light and return an equal amount of energy as heat and as low-energy products, operating in a **dynamic steady state** far from equilibrium ([7.1.1](/7.1.1#sec-1.3.1), [6.3.18](/6.3.18#sec-18.4.2)). Cells are isothermal and nearly isobaric. Heat can do work only when it flows from a hotter to a colder body, so heat is not a source of energy for cells; the energy they can and must use is Gibbs free energy, $G$, and the quantity that decides the direction of every reaction in a cell is $\Delta G = \Delta H - T\Delta S$. Lavoisier's remark that respiration "is nothing but a slow combustion of carbon and hydrogen" is right about the chemistry; the difference is that the cell carries out the combustion in many small steps, catalyzed by enzymes at body temperature, and conserves a large part of the free energy instead of releasing it as heat.

### 16.2.1. The Biochemical Standard State

The **standard reaction Gibbs energy** $\Delta_{\mathrm{r}}G^\circ$ of chemistry refers to unit activity of every species, including $\ce{H+}$ (pH 0) and the solvent ([6.3.7](/6.3.7#sec-7.2)). Biochemical reactions take place in buffered water near pH 7, with water at 55.5 M and with $\ce{Mg^2+}$ bound to most phosphorylated compounds. Biochemists therefore use a different reference state.

**Definition 16.2.2 (Biochemical Standard State)** In the **biochemical standard state**, every reactant and product other than $\ce{H+}$, $\ce{H2O}$ and $\ce{Mg^2+}$ is at 1 M (gases at 101.3 kPa), the pH is 7 ($[\ce{H+}] = 10^{-7}\,\mathrm{M}$), the free $\ce{Mg^2+}$ concentration is 1 mM, and the temperature is usually $25\,^\circ\mathrm{C}$. The concentrations of $\ce{H+}$, $\ce{H2O}$ and $\ce{Mg^2+}$ do not appear in the equilibrium expression; they are absorbed into the **standard transformed constants**, written with a prime: the standard transformed reaction Gibbs energy $\Delta_{\mathrm{r}}G'^{\circ}$, the apparent equilibrium constant $K'$, and the standard transformed reduction potential $E'^{\circ}$ (16.4).

Lehninger writes $\Delta G'^{\circ}$, many other books $\Delta G^{\circ\prime}$, and [6.3.7](/6.3.7#sec-7.6.2) $\Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}}$; all denote the same quantity, written here $\Delta_{\mathrm{r}}G'^{\circ}$. The relation to the equilibrium constant has the familiar form,

$$
\Delta_{\mathrm{r}}G'^{\circ} = -RT\ln K', \tag{16.1}
$$
and because a factor of 10 in $K'$ corresponds to $RT\ln 10 = 5.71\,\mathrm{kJ\,mol^{-1}}$ at $25\,^\circ\mathrm{C}$ ($5.94\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$), small differences in $\Delta_{\mathrm{r}}G'^{\circ}$ mean large differences in the position of equilibrium:

| $K'$ | $10^{3}$ | $10^{2}$ | $10$ | $1$ | $10^{-1}$ | $10^{-2}$ | $10^{-3}$ | $10^{-5}$ |
|---|---|---|---|---|---|---|---|---|
| $\Delta_{\mathrm{r}}G'^{\circ}/(\mathrm{kJ\,mol^{-1}})$ at $25\,^\circ\mathrm{C}$ | $-17.1$ | $-11.4$ | $-5.7$ | $0$ | $+5.7$ | $+11.4$ | $+17.1$ | $+28.5$ |

The two standard states differ only for reactions in which $\ce{H+}$ (or $\ce{Mg^2+}$) is consumed or released. For a reaction that releases $\nu_{\ce{H+}}$ protons, $\Delta_{\mathrm{r}}G'^{\circ} = \Delta_{\mathrm{r}}G^\circ + \nu_{\ce{H+}}RT\ln 10^{-7}$ ([6.3.7](/6.3.7#sec-7.6.2)): at $25\,^\circ\mathrm{C}$, each proton released makes $\Delta_{\mathrm{r}}G'^{\circ}$ more negative than $\Delta_{\mathrm{r}}G^\circ$ by $40.0\,\mathrm{kJ\,mol^{-1}}$. This is a change of reference, not of chemistry: the actual $\Delta_{\mathrm{r}}G$ in a given solution is the same whichever standard state is used.

**Example 16.2.1** Phosphoglucomutase interconverts glucose 1-phosphate and glucose 6-phosphate. Starting from 20 mM glucose 1-phosphate at pH 7 and $25\,^\circ\mathrm{C}$, the equilibrium mixture contains 1.0 mM glucose 1-phosphate and 19 mM glucose 6-phosphate. Then $K' = 19$ and $\Delta_{\mathrm{r}}G'^{\circ} = -(2.479\,\mathrm{kJ\,mol^{-1}})\ln 19 = -7.3\,\mathrm{kJ\,mol^{-1}}$: formation of glucose 6-phosphate is favorable, and the reverse reaction has $+7.3\,\mathrm{kJ\,mol^{-1}}$.

A table of $\Delta_{\mathrm{r}}G'^{\circ}$ values shows a pattern that recurs throughout metabolism (values from Lehninger 8e, Table 13-4):

| Reaction type | Example | $\Delta_{\mathrm{r}}G'^{\circ}/(\mathrm{kJ\,mol^{-1}})$ |
|---|---|---|
| Hydrolysis of acid anhydrides | ATP + $\ce{H2O}$ → ADP + $\mathrm{P_i}$; ATP + $\ce{H2O}$ → AMP + $\mathrm{PP_i}$; $\mathrm{PP_i}$ + $\ce{H2O}$ → 2 $\mathrm{P_i}$ | $-30.5$; $-45.6$; $-19.2$ |
| Hydrolysis of esters | glucose 6-phosphate + $\ce{H2O}$ → glucose + $\mathrm{P_i}$ | $-13.8$ |
| Hydrolysis of amides and peptides | glutamine + $\ce{H2O}$ → glutamate + $\ce{NH4+}$; glycylglycine + $\ce{H2O}$ → 2 glycine | $-14.2$; $-9.2$ |
| Hydrolysis of glycosides | maltose + $\ce{H2O}$ → 2 glucose | $-15.5$ |
| Rearrangements | fructose 6-phosphate → glucose 6-phosphate | $-1.7$ |
| Elimination of water | malate → fumarate + $\ce{H2O}$ | $+3.1$ |
| Complete oxidation | glucose + 6 $\ce{O2}$ → 6 $\ce{CO2}$ + 6 $\ce{H2O}$; palmitate + 23 $\ce{O2}$ → 16 $\ce{CO2}$ + 16 $\ce{H2O}$ | $-2840$; $-9770$ |

Hydrolysis of simple esters, amides and glycosides, rearrangements and eliminations have small $\Delta_{\mathrm{r}}G'^{\circ}$; hydrolysis of acid anhydrides is strongly exergonic, and complete oxidation of fuels releases very large amounts of free energy, which cells take in many small portions.

### 16.2.2. The Actual Gibbs Energy Change in Cells

$\Delta_{\mathrm{r}}G'^{\circ}$ is a constant of a reaction; it says which way the reaction runs when every component is at 1 M. No component of a cell is at 1 M, and the quantity that decides the direction of a reaction in the cell is the actual reaction Gibbs energy, given by the reaction isotherm of [6.3.7](/6.3.7#sec-7.2).

**Definition 16.2.3 (Mass-Action Ratio)** For a reaction $a\ce{A} + b\ce{B} \rightleftharpoons c\ce{C} + d\ce{D}$, the ratio of the actual concentrations $Q = [\ce{C}]^c[\ce{D}]^d/([\ce{A}]^a[\ce{B}]^b)$ (each concentration divided by the standard concentration 1 M, and omitting $\ce{H+}$, $\ce{H2O}$ and $\ce{Mg^2+}$) is called the **mass-action ratio**.

**Formula 16.2.1 (Actual Reaction Gibbs Energy)**

$$
\Delta_{\mathrm{r}}G = \Delta_{\mathrm{r}}G'^{\circ} + RT\ln Q = RT\ln\frac{Q}{K'}. \tag{16.2}
$$
A reaction proceeds spontaneously in the forward direction if $\Delta_{\mathrm{r}}G < 0$, that is if $Q < K'$; it is at equilibrium when $Q = K'$.

Three consequences are used throughout Part II.

- The criterion is $\Delta_{\mathrm{r}}G$, not $\Delta_{\mathrm{r}}G'^{\circ}$. A reaction with a positive $\Delta_{\mathrm{r}}G'^{\circ}$ runs forward if its products are removed fast enough to keep $Q$ below $K'$; this is **Le Chatelier's principle** in quantitative form. The aldolase reaction of glycolysis has $\Delta_{\mathrm{r}}G'^{\circ} = +23.8\,\mathrm{kJ\,mol^{-1}}$ ($K' \approx 10^{-4}\,\mathrm{M}$) and yet runs forward in every cell, because its two products are kept at micromolar concentrations (7.1.18).
- Reactions that change the number of molecules depend strongly on dilution. For A ⇌ B + C at concentrations near 1 mM, the extra factor $10^{-3}$ in $Q$ contributes $RT\ln 10^{-3} = -17.8\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$. Cleavages, hydrolyses and the release of $\mathrm{P_i}$ are therefore more favorable in the cell than their $\Delta_{\mathrm{r}}G'^{\circ}$ suggests, condensations less.
- Thermodynamics says where a reaction can go, not how fast. Firewood and $\ce{O2}$, sucrose and $\ce{O2}$, ATP and water are all far from equilibrium and yet stable for years, because the uncatalyzed reactions have large activation Gibbs energies ([7.1.8](/7.1.8#sec-8.2.2)). In cells, enzymes choose which of the many favorable reactions happen and how fast.

### 16.2.3. Additivity and Coupling

Gibbs energy is a state function, so the $\Delta_{\mathrm{r}}G'^{\circ}$ of sequential reactions add, and the equilibrium constants multiply. For two reactions that share an intermediate, A ⇌ B and B ⇌ C, the overall reaction A ⇌ C has $\Delta_{\mathrm{r}}G'^{\circ}_{\mathrm{sum}} = \Delta_{\mathrm{r}}G'^{\circ}_1 + \Delta_{\mathrm{r}}G'^{\circ}_2$ and $K'_{\mathrm{sum}} = K'_1K'_2$. This is how an endergonic reaction is driven by an exergonic one. The standard example, the phosphorylation of glucose by hexokinase, was worked out in [7.1.1](/7.1.1#sec-1.3.2) and [6.3.7](/6.3.7#sec-7.6.2): glucose + $\mathrm{P_i}$ → glucose 6-phosphate ($+13.8\,\mathrm{kJ\,mol^{-1}}$, $K' = 3.9 \times 10^{-3}\,\mathrm{M^{-1}}$) plus ATP hydrolysis ($-30.5\,\mathrm{kJ\,mol^{-1}}$, $K' = 2 \times 10^{5}\,\mathrm{M}$) gives glucose + ATP → glucose 6-phosphate + ADP ($-16.7\,\mathrm{kJ\,mol^{-1}}$, $K' = 7.8 \times 10^{2}$).

Two points are easily missed. First, the coupling is chemical, not arithmetic: hexokinase transfers the phosphoryl group directly from ATP to glucose, and the two partial reactions never occur separately. A reaction mixture that contains an ATPase and an unfavorable reaction side by side does not drive anything; the two reactions must share an intermediate or a molecular machine (**coupled reactions**, [6.3.7](/6.3.7#sec-7.6.2); for incomplete coupling see [6.3.18](/6.3.18#sec-18.2.5)). Second, the driving force supplied by ATP is set by the cellular, not the standard, value of its hydrolysis Gibbs energy (16.3.2). Coupling one ATP whose hydrolysis has $\Delta_{\mathrm{r}}G \approx -50\,\mathrm{kJ\,mol^{-1}}$ in the cell multiplies the attainable ratio [products]/[reactants] of the driven reaction by $\mathrm{e}^{50/2.58} \approx 3 \times 10^{8}$ at $37\,^\circ\mathrm{C}$; coupling $n$ ATP multiplies it by about $10^{8n}$. This is why biosynthetic pathways can be made essentially irreversible by spending one or two ATP more than the bare stoichiometry requires.

## 16.3. Phosphoryl Group Transfers and ATP

### 16.3.1. Why ATP Hydrolysis Is Strongly Exergonic

ATP (adenosine 5′-triphosphate) contains one phosphate ester bond (to C-5′ of ribose, the α phosphate) and two phosphoanhydride bonds (α–β and β–γ). At pH 7 it carries about four negative charges.

```smiles
Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]1O ATP
```

The large negative $\Delta_{\mathrm{r}}G'^{\circ}$ for hydrolysis of the terminal phosphoanhydride, $-30.5\,\mathrm{kJ\,mol^{-1}}$, comes from the difference between the reactants and the products, not from any special energy in the bond (breaking a bond always requires energy; the much-used term "high-energy phosphate bond" is a misnomer, see [6.3.7](/6.3.7#sec-7.6.2)). Four factors stabilize the products relative to ATP:

1. Charge separation: hydrolysis relieves the electrostatic repulsion between the negatively charged phosphates.
2. Resonance: $\mathrm{P_i}$ is a **resonance hybrid** in which the four P–O bonds share the double-bond character equally; the terminal phosphate in ATP has fewer resonance forms.
3. Ionization: at pH 7 the products ionize further, $\ce{ATP^4- + H2O -> ADP^3- + HPO4^2- + H+}$, and the low $[\ce{H+}]$ pulls the reaction forward.
4. Solvation: the products are more strongly hydrated than ATP.

Inside cells, ATP and ADP are complexed with $\ce{Mg^2+}$, which partly shields their charges and fixes the conformation of the phosphates; for most enzymes that use ATP the true substrate is $\ce{MgATP^2-}$, and $\Delta_{\mathrm{r}}G'^{\circ}$ is defined at 1 mM free $\ce{Mg^2+}$. Equally important is a kinetic property: although ATP is thermodynamically unstable in water, its uncatalyzed hydrolysis is slow, because the electron-rich phosphoryl groups repel nucleophiles. ATP therefore does not give up its phosphoryl groups to water or to the hundreds of other possible acceptors in the cell; it does so only where an enzyme lowers the barrier, and by regulating these enzymes the cell controls where its energy goes.

### 16.3.2. The Phosphorylation Potential

**Definition 16.3.1 (Phosphorylation Potential)** The actual Gibbs energy of ATP hydrolysis under the conditions in a cell, $\Delta G_{\mathrm{p}} = \Delta_{\mathrm{r}}G'^{\circ} + RT\ln([\mathrm{ADP}][\mathrm{P_i}]/[\mathrm{ATP}])$, is called the **phosphorylation potential**.

**Example 16.3.1** In human erythrocytes, [ATP] = 2.25 mM, [ADP] = 0.25 mM and [$\mathrm{P_i}$] = 1.65 mM. At $37\,^\circ\mathrm{C}$ ($RT = 2.58\,\mathrm{kJ\,mol^{-1}}$),

$$
\Delta G_{\mathrm{p}} = -30.5 + 2.58\ln\frac{(0.25 \times 10^{-3})(1.65 \times 10^{-3})}{2.25 \times 10^{-3}} = -30.5 + 2.58 \times (-8.60) = -52.7\,\mathrm{kJ\,mol^{-1}}.
$$
Synthesizing ATP under the same conditions requires $+52.7\,\mathrm{kJ\,mol^{-1}}$. The same calculation with the total concentrations measured in other cells (Lehninger 8e, Table 13-5) gives:

| Cell | [ATP] / mM | [ADP] / mM | [$\mathrm{P_i}$] / mM | [ATP]/[ADP] | $\Delta G_{\mathrm{p}}$ / ($\mathrm{kJ\,mol^{-1}}$) |
|---|---|---|---|---|---|
| Rat hepatocyte | 3.38 | 1.32 | 4.8 | 2.6 | $-46.7$ |
| Rat myocyte | 8.05 | 0.93 | 8.05 | 8.7 | $-48.5$ |
| Rat neuron | 2.59 | 0.73 | 2.72 | 3.5 | $-49.0$ |
| Human erythrocyte | 2.25 | 0.25 | 1.65 | 9.0 | $-52.7$ |

These are lower limits. Much of the ADP in a cell is bound to proteins, and the free concentration, which is what counts thermodynamically, is much lower: in resting muscle it is estimated at 1 to 37 µM, and with 25 µM the phosphorylation potential becomes $-58\,\mathrm{kJ\,mol^{-1}}$. A value of $-50$ to $-65\,\mathrm{kJ\,mol^{-1}}$ is typical of living cells.

The equilibrium of ATP hydrolysis lies very far to the side of ADP: with $K' \approx 1.4 \times 10^{5}\,\mathrm{M}$ at $37\,^\circ\mathrm{C}$ and 1.65 mM $\mathrm{P_i}$, equilibrium would be reached at [ATP]/[ADP] $\approx 10^{-8}$, whereas the erythrocyte maintains a ratio of 9. The cell is therefore displaced from equilibrium by a factor of about $10^{9}$, and this displacement, not the chemistry of ATP alone, is what makes ATP useful. If the ATP level drops, not only is there less fuel, the fuel itself loses its strength, because $\Delta G_{\mathrm{p}}$ becomes less negative. Much of the regulation described in Part II exists to keep the ratio [ATP]/([ADP][$\mathrm{P_i}$]) high (7.1.17).

![The phosphorylation potential. A: actual Gibbs energy of ATP hydrolysis at 37 °C against the mass-action ratio Q = [ADP][Pᵢ]/[ATP] (logarithmic scale); the line meets zero at equilibrium (Q = K′ ≈ 1.4 × 10⁵ M), and the points mark the ratios computed from the total nucleotide concentrations of four cell types, all between −46 and −53 kJ mol⁻¹, far from equilibrium. The standard value, −30.5 kJ mol⁻¹, corresponds to Q = 1 M. B: phosphorylation potential of the same cells and of resting muscle with the estimated free ADP concentration (25 µM), compared with the standard value](./plots/atp-hydrolysis-dg.py)

ATP is not a storage form of energy. A resting adult turns over roughly his or her body mass of ATP (about 40 kg) per day, and during strenuous exercise several times more, while the amount of ATP present in the body at any moment is only of the order of 100 g; a given ATP molecule is consumed within about a minute of its formation. The concentration of ATP stays constant because its synthesis matches its consumption, a dynamic steady state. Longer-term stores are glycogen and fat, and in muscle the short-term buffer phosphocreatine (16.3.5).

### 16.3.3. Other Compounds with High Phosphoryl Group Transfer Potential

ATP is not the compound with the largest Gibbs energy of hydrolysis. Several intermediates of catabolism have even larger values (Lehninger 8e, Table 13-6):

| Compound (hydrolysis product) | $\Delta_{\mathrm{r}}G'^{\circ}/(\mathrm{kJ\,mol^{-1}})$ | Source of the large negative value |
|---|---|---|
| Phosphoenolpyruvate (pyruvate + $\mathrm{P_i}$) | $-61.9$ | the enol product tautomerizes to the far more stable keto form |
| 1,3-Bisphosphoglycerate (3-phosphoglycerate + $\mathrm{P_i}$) | $-49.3$ | acyl phosphate (mixed anhydride); the carboxylic acid product ionizes and is resonance-stabilized |
| Phosphocreatine (creatine + $\mathrm{P_i}$) | $-43.0$ | P–N bond; resonance of the guanidinium group of creatine |
| ADP (AMP + $\mathrm{P_i}$) | $-32.8$ | phosphoanhydride, as ATP |
| ATP (ADP + $\mathrm{P_i}$) | $-30.5$ | phosphoanhydride |
| ATP (AMP + $\mathrm{PP_i}$) | $-45.6$ | phosphoanhydride; $\mathrm{PP_i}$ is then hydrolyzed |
| Acetyl-CoA (acetate + CoA) | $-31.4$ | thioester: little resonance stabilization of the reactant |
| $\mathrm{PP_i}$ (2 $\mathrm{P_i}$) | $-19.2$ | phosphoanhydride |
| Glucose 1-phosphate (glucose + $\mathrm{P_i}$) | $-20.9$ | phosphate ester (of a hemiacetal) |
| Fructose 6-phosphate | $-15.9$ | phosphate ester |
| AMP (adenosine + $\mathrm{P_i}$) | $-14.2$ | phosphate ester |
| Glucose 6-phosphate | $-13.8$ | phosphate ester |
| Glycerol 3-phosphate | $-9.2$ | phosphate ester |

```smiles
C=C(OP(=O)([O-])[O-])C(=O)[O-] PEP
O=C(OP(=O)([O-])[O-])[C@H](O)COP(=O)([O-])[O-] 1,3-BPG
CN(CC(=O)[O-])C(=[NH2+])NP(=O)([O-])[O-] PCr
```

The reasons are always the same: the products are more stable than the reactant because hydrolysis relieves electrostatic repulsion (ATP), because the products ionize (ATP, acyl phosphates, thioesters), because a product tautomerizes (PEP; **keto–enol tautomerism**, [6.5.21](/6.5.21)) or because the products have more resonance forms (creatine, carboxylates, $\mathrm{P_i}$). In a **thioester** the overlap between the sulfur 3p orbitals and the C=O π system is poor, so the reactant lacks the resonance stabilization of an oxygen ester, while the hydrolysis products (carboxylate and thiol) are as stable as those of an ester; thioesters therefore have large negative Gibbs energies of hydrolysis and activate acyl groups for transfer and condensation ([6.5.22](/6.5.22#sec-22.10.2)).

**Definition 16.3.2 (High-Energy Compound and Phosphoryl Group Transfer Potential)** A compound whose hydrolysis has $\Delta_{\mathrm{r}}G'^{\circ}$ more negative than about $-25\,\mathrm{kJ\,mol^{-1}}$ is called a **high-energy compound**; those with less negative values are low-energy compounds. The **phosphoryl group transfer potential** of a phosphorylated compound is $-\Delta_{\mathrm{r}}G'^{\circ}$ of its hydrolysis: the higher it is, the more readily the compound donates its phosphoryl group to an acceptor.

Any phosphorylated compound can be made by phosphoryl transfer from a compound of higher transfer potential. PEP has a higher potential than ATP, and the direct transfer catalyzed by pyruvate kinase is strongly favorable:

$$
\begin{aligned}
&\text{PEP} + \ce{H2O} \to \text{pyruvate} + \mathrm{P_i} && -61.9\,\mathrm{kJ\,mol^{-1}} \\
&\ce{ADP} + \mathrm{P_i} \to \ce{ATP} + \ce{H2O} && +30.5\,\mathrm{kJ\,mol^{-1}} \\
&\text{PEP} + \ce{ADP} \to \text{pyruvate} + \ce{ATP} && -31.4\,\mathrm{kJ\,mol^{-1}}
\end{aligned}
$$
ATP is in the middle of the scale. It can accept phosphoryl groups from the high-energy intermediates of catabolism (PEP and 1,3-bisphosphoglycerate in glycolysis, succinyl-CoA in the citric acid cycle via GTP) and donate them to low-energy acceptors such as glucose or glycerol, converting them into more reactive phosphate esters. This intermediate position is what makes it the universal carrier of phosphoryl groups, the energy currency that Lipmann and Kalckar recognized in 1941.

![Phosphoryl group transfer potential. Phosphorylated compounds ranked by the standard Gibbs energy of hydrolysis of their donor phosphoryl group (vertical axis, more negative upward). Phosphoryl groups flow downhill, from the high-energy intermediates of catabolism (phosphoenolpyruvate, 1,3-bisphosphoglycerate) to ADP, and from ATP to low-energy acceptors (glucose, glycerol), catalyzed by kinases; phosphocreatine exchanges phosphoryl groups with ADP in both directions through creatine kinase. The dashed line at −25 kJ mol⁻¹ separates "high-energy" from "low-energy" compounds](./plots/phosphoryl-transfer-potential.py)

### 16.3.4. ATP Provides Energy by Group Transfer

Reactions are often written as if ATP were simply hydrolyzed alongside them ("driven by ATP hydrolysis"). Hydrolysis by itself only liberates heat, which cannot drive a chemical reaction in an isothermal system. In almost every ATP-dependent reaction ATP takes part covalently: a part of it is first transferred to the substrate or to an enzyme residue, raising its free energy (activating it), and in a second step this part is displaced. In glutamine synthetase, for example, the phosphoryl group goes first to glutamate, giving γ-glutamyl phosphate, which ammonia then attacks, releasing $\mathrm{P_i}$:

$$
\begin{aligned}
&\text{glutamate} + \ce{ATP} \to \gamma\text{-glutamyl phosphate} + \ce{ADP} \\
&\gamma\text{-glutamyl phosphate} + \ce{NH3} \to \text{glutamine} + \mathrm{P_i}
\end{aligned}
$$
The reactions of ATP are nucleophilic displacements (**SN2 reactions**) at one of its three phosphorus atoms, and the position of attack determines the group transferred:

| Position attacked | Group transferred | Leaving group | Example |
|---|---|---|---|
| γ-P | phosphoryl, $\ce{-PO3^2-}$ | ADP | kinases (hexokinase, glutamine synthetase, protein kinases) |
| β-P | pyrophosphoryl | AMP | synthesis of 5-phosphoribosyl 1-pyrophosphate (PRPP, 7.1.28) |
| α-P | adenylyl (AMP) | $\mathrm{PP_i}$ | activation of fatty acids (7.1.21) and amino acids (aminoacyl-tRNA synthetases, [7.2](/7.2)) |

$^{18}\mathrm{O}$-labeling shows that the bridging oxygen in the product comes from the attacking nucleophile, so what is transferred is a phosphoryl group, not a phosphate. Adenylylation is the most powerful way of using ATP: hydrolysis of the α–β bond releases more free energy ($-45.6\,\mathrm{kJ\,mol^{-1}}$) than that of the β–γ bond, and the $\mathrm{PP_i}$ formed is hydrolyzed by the ubiquitous inorganic pyrophosphatase ($-19.2\,\mathrm{kJ\,mol^{-1}}$), so that both phosphoanhydride bonds are spent, ATP + 2 $\ce{H2O}$ → AMP + 2 $\mathrm{P_i}$ ($-64.8\,\mathrm{kJ\,mol^{-1}}$). The activation of a fatty acid, whose direct condensation with CoA is endergonic, proceeds through a fatty acyl adenylate and is made effectively irreversible in this way. The polymerization of nucleic acids, in which nucleoside triphosphates add nucleotidyl units and release $\mathrm{PP_i}$, follows the same principle ([7.2.7](/7.2.7)).

The firefly uses an adenylylation to make light (**bioluminescence**): luciferase converts its substrate luciferin and ATP to luciferyl adenylate and $\mathrm{PP_i}$; the adenylate reacts with $\ce{O2}$ to an excited oxyluciferin that emits a photon as it returns to the ground state. Because the light intensity is proportional to the amount of ATP, purified luciferin and luciferase measure ATP down to a few picomoles, the basis of cell-viability and hygiene assays and of luciferase reporter genes.

Only a few processes use the energy of ATP hydrolysis without covalent transfer to the substrate. Motor proteins (myosin, kinesin, dynein), the chaperonins, helicases and many AAA+ ATPases bind ATP noncovalently and use its hydrolysis and the release of ADP and $\mathrm{P_i}$ to cycle between conformations, as G proteins do with GTP (7.1.14). Ion pumps such as the $\ce{Na+}/\ce{K+}$-ATPase are phosphorylated themselves (on an Asp residue) and use the cycle of phosphorylation and dephosphorylation of the enzyme to pump ions (7.1.13). In the human kidney and brain as much as two-thirds of the energy consumed at rest is used to pump $\ce{Na+}$ and $\ce{K+}$.

### 16.3.5. Transphosphorylations between Nucleotides

All nucleoside triphosphates and deoxynucleoside triphosphates have essentially the same phosphoanhydride energetics as ATP. ATP made by catabolism keeps them phosphorylated through a set of kinases.

**Definition 16.3.3 (Nucleoside Diphosphate Kinase and Adenylate Kinase)** **Nucleoside diphosphate kinase** catalyzes ATP + NDP ⇌ ADP + NTP (and the same with dNDP), with $\Delta_{\mathrm{r}}G'^{\circ} \approx 0$; it is nonspecific for the base and acts through a phospho-His intermediate (a **ping-pong mechanism**, [7.1.9](/7.1.9#sec-9.2.1)). **Adenylate kinase** (myokinase) catalyzes the reversible reaction 2 ADP ⇌ ATP + AMP, $\Delta_{\mathrm{r}}G'^{\circ} \approx 0$.

Because [ATP]/[ADP] is high in cells, nucleoside diphosphate kinase runs in the direction of NTP synthesis. Adenylate kinase recovers a phosphoryl group from ADP when ATP is used rapidly (in contracting muscle) and regenerates ADP from AMP afterwards. Its equilibrium links [AMP] to the square of [ADP], which makes AMP a sensitive signal of the energy state of the cell (7.1.17).

**Definition 16.3.4 (Phosphocreatine)** **Phosphocreatine** (creatine phosphate, PCr) is the phosphorylated guanidino compound that serves in vertebrate muscle and brain as a reservoir of phosphoryl groups for rapid regeneration of ATP; creatine kinase catalyzes ADP + PCr ⇌ ATP + creatine, $\Delta_{\mathrm{r}}G'^{\circ} = -12.5\,\mathrm{kJ\,mol^{-1}}$. Compounds with this function are called phosphagens (arginine phosphate in many invertebrates).

Skeletal muscle contains about 30 mM PCr, roughly four times its ATP, and other tissues 5–10 mM. When contraction begins, the ATP present supports a sprint for only a couple of seconds; PCr, kept near equilibrium with ATP by the fast creatine kinase reaction, holds [ATP] nearly constant for several seconds more, while glycolysis (seconds to minutes) and oxidative phosphorylation (minutes and longer) accelerate. When demand falls, ATP from catabolism refills the PCr store by the reverse reaction. Creatine kinase isozymes in mitochondria and in the myofibrils also carry phosphoryl groups from the sites of ATP synthesis to the sites of use (the phosphocreatine shuttle; 7.1.29).

## 16.4. Biological Oxidation–Reduction Reactions

### 16.4.1. Electron Flow and Half-Reactions

The flow of electrons in **redox reactions** is responsible, directly or indirectly, for all the work done by living organisms. In a battery, electrons flow spontaneously through a wire from the chemical species of low electron affinity to the one of high affinity, driven by the **electromotive force**, and a motor in the circuit converts part of the energy into work. In a cell the source of electrons is a reduced fuel such as glucose; as it is oxidized, the electrons flow through a series of carriers to an acceptor of high affinity, usually $\ce{O2}$, and membrane-bound proteins convert the energy of this flow into a proton gradient that drives ATP synthesis (7.1.23) or flagellar rotation. Each redox reaction can be written as two half-reactions, each a conjugate **redox pair** (electron donor ⇌ $n\,\ce{e-}$ + electron acceptor; [6.1.11](/6.1.11#sec-11.1.4)), just as an acid–base reaction combines two conjugate acid–base pairs.

Electrons are transferred in four ways in cells: directly as electrons (between metal ions, as from $\ce{F\mathrm{e}^2+}$ to $\ce{Cu^2+}$ in cytochrome oxidase); as hydrogen atoms (a proton and an electron: $\ce{AH2 + B -> A + BH2}$); as a hydride ion ($\ce{:H-}$, two electrons and a proton), in the NAD-linked dehydrogenases; and by direct combination with oxygen, in which an oxygen atom is incorporated into the product (oxygenases). The neutral term reducing equivalent designates one electron equivalent in any of these forms.

### 16.4.2. Oxidation States of Carbon

Carbon occurs in living matter in oxidation states from −4 to +4. Because C is more electronegative than H and less than O, a carbon atom is oxidized as it loses bonds to hydrogen and gains bonds to oxygen (oxidation numbers, [6.1.11](/6.1.11#sec-11.1.1)); the conversion of an alkane $\ce{-CH2-CH2-}$ to an alkene $\ce{-CH=CH-}$ is an oxidation although no oxygen is involved, and in biology oxidation is often synonymous with dehydrogenation, catalyzed by dehydrogenases.

| Compound | $\ce{CH4}$ | $\ce{CH3-CH3}$ | $\ce{CH2=CH2}$ | $\ce{CH3OH}$ | $\ce{HCHO}$ | $\ce{HCOOH}$ | $\ce{CO2}$ |
|---|---|---|---|---|---|---|---|
| Oxidation number of C | −4 | −3 | −2 | −2 | 0 | +2 | +4 |
| Biological analogue | methane (archaea) | fatty acyl chain $\ce{-CH2-}$ (−2) | unsaturated chain | alcohol | aldehyde (sugar C-1) | carboxylic acid | end product |

The more reduced a fuel, the more electrons it can deliver to $\ce{O2}$ per carbon and the more free energy its complete oxidation releases: the mean oxidation number of carbon is about −1.75 in palmitate and 0 in glucose, which is why fat yields more than twice as much energy per gram as carbohydrate ([7.1.12](/7.1.12#sec-12.3.2)).

### 16.4.3. Standard Reduction Potentials

The tendency of the oxidized member of a redox pair to accept electrons is measured by its reduction potential. The **standard reduction potential** $E^\circ$ of a pair is measured against the standard hydrogen electrode, $\ce{H+ + e- -> 1/2 H2}$, assigned $0.000\,\mathrm{V}$ at pH 0 ([6.1.11](/6.1.11#sec-11.4.2)). Biochemists again use pH 7: the standard transformed reduction potential $E'^{\circ}$ is the potential of the pair with both members at 1 M and pH 7, measured against the standard (pH 0) hydrogen electrode. On this scale the hydrogen electrode itself at pH 7 has $E'^{\circ} = -(RT/F)\ln 10^{7} = -0.414\,\mathrm{V}$. When two pairs are connected, electrons flow to the one with the more positive potential.

| Half-reaction (written as a reduction) | $E'^{\circ}/\mathrm{V}$ |
|---|---|
| $\tfrac12\ce{O2} + 2\ce{H+} + 2\ce{e-} \to \ce{H2O}$ | $+0.816$ |
| $\ce{F\mathrm{e}^3+ + e- -> F\mathrm{e}^2+}$ | $+0.771$ |
| $\ce{NO3- + 2H+ + 2e- -> NO2- + H2O}$ | $+0.421$ |
| cytochrome $a_3$ ($\ce{F\mathrm{e}^3+}$) + $\ce{e-}$ → cytochrome $a_3$ ($\ce{F\mathrm{e}^2+}$) | $+0.35$ |
| $\ce{O2 + 2H+ + 2e- -> H2O2}$ | $+0.295$ |
| cytochrome $c$ ($\ce{F\mathrm{e}^3+}$) + $\ce{e-}$ → cytochrome $c$ ($\ce{F\mathrm{e}^2+}$) | $+0.254$ |
| cytochrome $b$ ($\ce{F\mathrm{e}^3+}$) + $\ce{e-}$ → cytochrome $b$ ($\ce{F\mathrm{e}^2+}$) | $+0.077$ |
| ubiquinone + $2\ce{H+} + 2\ce{e-}$ → ubiquinol | $+0.045$ |
| fumarate + $2\ce{H+} + 2\ce{e-}$ → succinate | $+0.031$ |
| oxaloacetate + $2\ce{H+} + 2\ce{e-}$ → malate | $-0.166$ |
| pyruvate + $2\ce{H+} + 2\ce{e-}$ → lactate | $-0.185$ |
| acetaldehyde + $2\ce{H+} + 2\ce{e-}$ → ethanol | $-0.197$ |
| $\ce{FAD} + 2\ce{H+} + 2\ce{e-} \to \ce{FADH2}$ (free FAD) | $-0.219$ |
| lipoic acid + $2\ce{H+} + 2\ce{e-}$ → dihydrolipoic acid | $-0.29$ |
| $\ce{NAD+} + \ce{H+} + 2\ce{e-} \to \ce{NADH}$ | $-0.320$ |
| $\ce{NADP+} + \ce{H+} + 2\ce{e-} \to \ce{NADPH}$ | $-0.324$ |
| acetoacetate + $2\ce{H+} + 2\ce{e-}$ → β-hydroxybutyrate | $-0.346$ |
| α-ketoglutarate + $\ce{CO2}$ + $2\ce{H+} + 2\ce{e-}$ → isocitrate | $-0.38$ |
| $2\ce{H+} + 2\ce{e-} \to \ce{H2}$ (at pH 7) | $-0.414$ |
| ferredoxin ($\ce{F\mathrm{e}^3+}$) + $\ce{e-}$ → ferredoxin ($\ce{F\mathrm{e}^2+}$) | $-0.432$ |

(Values from Lehninger 8e, Table 13-7.) The actual potential depends on the ratio of the concentrations of the two members by the **Nernst equation** ([6.1.11](/6.1.11#sec-11.5.1), [6.3.13](/6.3.13#sec-13.3.1)):

$$
E = E'^{\circ} + \frac{RT}{zF}\ln\frac{[\text{electron acceptor}]}{[\text{electron donor}]}, \tag{16.3}
$$
where $z$ is the number of electrons transferred; at $25\,^\circ\mathrm{C}$, $RT/F = 25.7\,\mathrm{mV}$.

### 16.4.4. Reduction Potentials and Gibbs Energy

For a redox reaction in which $z$ electrons pass from the donor pair to the acceptor pair, with $\Delta E'^{\circ} = E'^{\circ}(\text{acceptor}) - E'^{\circ}(\text{donor})$ (the convention is always acceptor minus donor),

**Formula 16.4.1**

$$
\Delta_{\mathrm{r}}G'^{\circ} = -zF\,\Delta E'^{\circ}, \qquad \Delta_{\mathrm{r}}G = -zF\,\Delta E, \tag{16.4}
$$
with the **Faraday constant** $F = 96.485\,\mathrm{kJ\,V^{-1}\,mol^{-1}}$ (the relation between electromotive force and Gibbs energy of [6.1.11](/6.1.11#sec-11.4.5)).

**Example 16.4.1** In alcoholic fermentation, NADH reduces acetaldehyde: acetaldehyde + NADH + $\ce{H+}$ → ethanol + $\ce{NAD+}$. Acetaldehyde is the acceptor, so $\Delta E'^{\circ} = -0.197 - (-0.320) = 0.123\,\mathrm{V}$ and $\Delta_{\mathrm{r}}G'^{\circ} = -2 \times 96.5 \times 0.123 = -23.7\,\mathrm{kJ\,mol^{-1}}$. With [acetaldehyde] = [NADH] = 1.00 M and [ethanol] = [$\ce{NAD+}$] = 0.100 M at $25\,^\circ\mathrm{C}$, $\Delta_{\mathrm{r}}G = -23.7 + 2.48\ln 0.01 = -35.1\,\mathrm{kJ\,mol^{-1}}$.

**Example 16.4.2** The span from NADH to $\ce{O2}$ is the largest in aerobic metabolism: $\Delta E'^{\circ} = 0.816 - (-0.320) = 1.136\,\mathrm{V}$, so NADH + $\ce{H+}$ + $\tfrac12\ce{O2}$ → $\ce{NAD+}$ + $\ce{H2O}$ has $\Delta_{\mathrm{r}}G'^{\circ} = -2 \times 96.5 \times 1.136 = -219\,\mathrm{kJ\,mol^{-1}}$, enough in principle for several ATP. The respiratory chain releases this free energy in steps between carriers of increasing potential (NADH → flavin → ubiquinone → cytochromes → $\ce{O2}$), each step large enough to pump protons (7.1.23).

![The redox tower. Standard transformed reduction potentials E′° of biologically important redox pairs at pH 7 (left axis), with strong reductants at the bottom and strong oxidants at the top; electrons flow spontaneously upward. The right axis gives the corresponding standard Gibbs energy for the transfer of two electrons to O₂, ΔrG′° = −2F(0.816 V − E′°). The arrow from NAD⁺/NADH to O₂/H₂O spans 1.136 V, or −219 kJ mol⁻¹; the respiratory chain (7.1.23) divides this drop among carriers of intermediate potential (FMN, ubiquinone, cytochromes)](./plots/redox-tower.py)

Complete oxidation of glucose, glucose + 6 $\ce{O2}$ → 6 $\ce{CO2}$ + 6 $\ce{H2O}$, transfers 24 electrons and has $\Delta_{\mathrm{r}}G'^{\circ} = -2840\,\mathrm{kJ\,mol^{-1}}$, far more than the 50–60 kJ needed to make one ATP in a cell. Cells do not oxidize glucose in one step; they remove its electrons in a series of dehydrogenations, each of which releases free energy of the same order as that needed for ATP synthesis, and channel the electrons into a few universal carriers.

## 16.5. Universal Electron Carriers

The hundreds of enzymes that catalyze cellular oxidations transfer the electrons of their substrates to a few kinds of carriers: the soluble nicotinamide nucleotides NAD and NADP, the flavin nucleotides FMN and FAD bound to flavoproteins, the lipid-soluble quinones (ubiquinone and plastoquinone) in membranes, and the iron–sulfur proteins and cytochromes. Quinones, iron–sulfur clusters and cytochromes are treated with the respiratory chain and photosynthesis (7.1.23–7.1.24).

### 16.5.1. NAD and NADP

**Definition 16.5.1 (Nicotinamide Nucleotides)** **Nicotinamide adenine dinucleotide** (NAD; oxidized form $\ce{NAD+}$, reduced form NADH) consists of two nucleotides, nicotinamide mononucleotide and AMP, joined through their phosphates by a phosphoanhydride bond. **Nicotinamide adenine dinucleotide phosphate** (NADP; $\ce{NADP+}$ and NADPH) carries an additional phosphate on the 2′-hydroxyl of the adenosine ribose. Both accept a hydride ion at C-4 of the nicotinamide ring.

```smiles
NC(=O)c1ccc[n+](c1)[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])OC[C@H]2O[C@@H](n3cnc4c(N)ncnc43)[C@H](O)[C@@H]2O)[C@@H](O)[C@H]1O NAD+
```

When a substrate is dehydrogenated, it gives up two hydrogen atoms: one is transferred as a hydride ion (two electrons and a proton) to C-4 of the nicotinamide ring, the other is released into solution as $\ce{H+}$:

$$
\ce{NAD+} + 2\ce{e-} + 2\ce{H+} \to \ce{NADH} + \ce{H+}, \qquad \ce{AH2} + \ce{NAD+} \rightleftharpoons \ce{A} + \ce{NADH} + \ce{H+}.
$$
The reduction converts the aromatic pyridinium ring, with a fixed positive charge on nitrogen, into a 1,4-dihydropyridine without charge (the plus sign in $\ce{NAD+}$ refers to this nitrogen, not to the net charge of the molecule, which is negative). The two hydrogens at C-4 of NADH are prochiral, and each dehydrogenase adds and removes the hydride stereospecifically on one face of the ring: A-side (pro-R) enzymes include alcohol dehydrogenase and lactate dehydrogenase, B-side (pro-S) enzymes glyceraldehyde 3-phosphate dehydrogenase.

```smiles
NC(=O)c1ccc[n+](C)c1>>NC(=O)C1=CN(C)C=CC1
```

(Nicotinamide ring with the ribose replaced by a methyl group: oxidized, aromatic pyridinium; reduced, 1,4-dihydropyridine with $\ce{CH2}$ at C-4.)

Reduced NADH and NADPH absorb at 340 nm (molar absorption coefficient about $6.2 \times 10^{3}\,\mathrm{M^{-1}\,cm^{-1}}$), the oxidized forms do not. Following the absorbance at 340 nm (**Beer–Lambert law**, [6.3.17](/6.3.17)) is the standard assay of dehydrogenases, and of other enzymes coupled to them; NADH also fluoresces (emission near 460 nm), which allows its redox state to be imaged in living cells.

The two coenzymes have different jobs, and the cell keeps them in two pools with opposite redox states:

- NAD functions mainly in oxidations, as part of catabolism. In the cytosol of liver cells the free ratio $[\ce{NAD+}]/[\mathrm{NADH}]$ is about 700–1000 (and about 5–10 in the mitochondrial matrix), favoring transfer of a hydride from substrates to $\ce{NAD+}$.
- NADP functions in reductions, as part of anabolism. The free ratio $[\ce{NADP+}]/[\mathrm{NADPH}]$ in the cytosol is about 0.01, favoring transfer of a hydride from NADPH to substrates.

With the Nernst equation these ratios translate into potentials. At $37\,^\circ\mathrm{C}$ ($RT/2F = 13.4\,\mathrm{mV}$), the cytosolic NAD pool sits at $E \approx -0.320 + 0.0134\ln 700 = -0.23\,\mathrm{V}$ and the NADP pool at $E \approx -0.324 + 0.0134\ln 0.01 = -0.39\,\mathrm{V}$. Although the two coenzymes have the same $E'^{\circ}$, the electrons in NADPH are about 0.15 V more reducing, worth about $30\,\mathrm{kJ}$ per mole of hydride: a cell can oxidize fuels with $\ce{NAD+}$ and reduce precursors with NADPH in the same compartment because the enzymes discriminate between the two coenzymes by the extra 2′-phosphate. Fuel oxidations (of pyruvate, fatty acids, α-keto acids) also take place mainly in the mitochondrial matrix and reductive syntheses (of fatty acids) in the cytosol. The total concentration of NAD (both forms) is of the order of 0.1–1 mM in mammalian cells, and that of NADP somewhat lower; much of it is bound to enzymes.

NAD and NADP are bound loosely and diffuse from one dehydrogenase to another; most of these enzymes bind the coenzyme with a conserved Rossmann fold (two βαβαβ units). In yeast fermentation, glyceraldehyde 3-phosphate dehydrogenase reduces $\ce{NAD+}$ and alcohol dehydrogenase reoxidizes the NADH; the sum, glyceraldehyde 3-phosphate + acetaldehyde → 3-phosphoglycerate + ethanol, involves no net change in NAD, which acts catalytically and is recycled many times. The ratios $[\ce{NAD+}]/[\mathrm{NADH}]$ and $[\ce{NADP+}]/[\mathrm{NADPH}]$ are themselves signals: both forms act as allosteric effectors of enzymes of catabolism (7.1.17). Some important NAD(P)-linked dehydrogenases (Lehninger 8e, Table 19-1), each treated in its chapter:

| Reaction | Coenzyme | Location | Chapter |
|---|---|---|---|
| glyceraldehyde 3-phosphate + $\mathrm{P_i}$ ⇌ 1,3-bisphosphoglycerate | NAD | cytosol | 7.1.18 |
| lactate ⇌ pyruvate | NAD | cytosol | 7.1.18 |
| pyruvate + CoA → acetyl-CoA + $\ce{CO2}$ | NAD | matrix | 7.1.20 |
| isocitrate → α-ketoglutarate + $\ce{CO2}$ | NAD (matrix), NADP (matrix and cytosol) | matrix, cytosol | 7.1.20 |
| α-ketoglutarate + CoA → succinyl-CoA + $\ce{CO2}$ | NAD | matrix | 7.1.20 |
| malate ⇌ oxaloacetate | NAD | matrix and cytosol | 7.1.20, 7.1.23 |
| β-hydroxyacyl-CoA ⇌ β-ketoacyl-CoA | NAD | matrix | 7.1.21 |
| glutamate + $\ce{H2O}$ ⇌ α-ketoglutarate + $\ce{NH4+}$ | NAD or NADP | matrix | 7.1.22 |
| glucose 6-phosphate → 6-phosphoglucono-δ-lactone | NADP | cytosol | 7.1.18 |

NAD also has functions outside redox chemistry, in which it is consumed as a substrate. Bacterial DNA ligases take the AMP that activates a nick from NAD ([7.2.7](/7.2.7)). ADP-ribosyltransferases transfer its ADP-ribose to proteins: poly(ADP-ribose) polymerases mark DNA damage, and cholera toxin ADP-ribosylates the G protein $\mathrm{G_s}$ of intestinal cells, locking it in the active state and causing massive loss of water (7.1.14). The sirtuins deacetylate Lys residues of histones and metabolic enzymes in a reaction that consumes NAD, so that their activity follows the NAD level of the cell, a link between energy state and gene expression.

The nicotinamide ring comes from the vitamin niacin (nicotinic acid, vitamin $\mathrm{B_3}$), which humans also make in small amounts from tryptophan. Niacin deficiency impairs all NAD(P)-dependent dehydrogenases and causes pellagra ("rough skin"), with the "three Ds": dermatitis, diarrhea and dementia, and finally death. Pellagra was common where maize, poor in tryptophan and in available niacin, was the staple (about 100 000 cases and 10 000 deaths in the southern United States in 1912–1916); Goldberger showed around 1920 that it is a dietary disease, and Elvehjem identified nicotinic acid as the cure in 1937. Today it is seen mainly in chronic alcoholics, whose absorption of niacin is impaired.

### 16.5.2. Flavin Nucleotides and Flavoproteins

**Definition 16.5.2 (Flavin Nucleotides and Flavoproteins)** **Flavin mononucleotide** (FMN, riboflavin 5′-phosphate) and **flavin adenine dinucleotide** (FAD, FMN joined to AMP by a phosphoanhydride bond) are coenzymes derived from the vitamin riboflavin ($\mathrm{B_2}$), whose isoalloxazine ring accepts one or two electrons with protons. A **flavoprotein** is an enzyme that uses FMN or FAD as a coenzyme, usually bound very tightly as a **prosthetic group**.

```smiles
Cc1cc2nc3c(=O)[nH]c(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)COP(=O)([O-])[O-])c2cc1C FMN
Cc1cc2Nc3c(=O)[nH]c(=O)[nH]c3N(C[C@H](O)[C@H](O)[C@H](O)COP(=O)([O-])[O-])c2cc1C FMNH2
```

The flavin differs from the nicotinamide coenzymes in three ways that determine where flavoproteins are used.

- One or two electrons: the isoalloxazine ring accepts two hydrogen atoms (two electrons and two protons) at N-1 and N-5 to give $\ce{FADH2}$ (or $\ce{FMNH2}$), or one hydrogen atom to give the stable radical, the **semiquinone** (FADH•). A flavin can therefore take two electrons from NADH or from a C–C bond and pass them one at a time to an iron–sulfur cluster or a heme, which accept only one electron each; flavoproteins are the junction between two-electron and one-electron chemistry (Complex I and Complex II of the respiratory chain, 7.1.23).
- Tight binding: most flavins are bound so tightly that they never leave the enzyme, and in some enzymes (succinate dehydrogenase) FAD is attached covalently to a His residue. The flavoprotein holds the electrons temporarily while it passes them from the substrate to an acceptor.
- A tunable potential: protein binding shifts the reduction potential of the flavin, from $-0.219\,\mathrm{V}$ for free FAD to values between about $-0.40$ and $+0.06\,\mathrm{V}$ in different flavoproteins. Succinate dehydrogenase, whose FAD is near $0\,\mathrm{V}$, can therefore accept electrons from succinate ($E'^{\circ} = +0.031\,\mathrm{V}$), whereas the transfer to free FAD would have $\Delta_{\mathrm{r}}G'^{\circ} = -2F(-0.219 - 0.031) = +48\,\mathrm{kJ\,mol^{-1}}$ and the transfer to $\ce{NAD+}$ $+68\,\mathrm{kJ\,mol^{-1}}$.

The redox states also differ in color: oxidized flavins are yellow, with absorption maxima near 370 and 450 nm; full reduction bleaches the 450 nm band; the neutral semiquinone is blue (absorbing near 580–600 nm) and the anionic semiquinone red (near 480 nm). These changes are used to follow flavoprotein reactions, and the blue-light photoreceptors of plants and animals (cryptochromes, phototropins) use the photochemistry of the oxidized flavin. Riboflavin deficiency (ariboflavinosis) causes inflammation of the lips and tongue and cracks at the corners of the mouth; it is rarely isolated, because riboflavin occurs widely in food.

Electrons collected as NADH and as reduced flavins in the catabolic pathways of 7.1.18–7.1.22 are passed to the respiratory chain in the inner mitochondrial membrane (or the plasma membrane of bacteria), where their flow to $\ce{O2}$ drives ATP synthesis (7.1.23).

## Summary

The energy side of Part II rests on a few relations and numbers.

| Topic | Key relation or value | Meaning |
|---|---|---|
| Catabolism and anabolism (Definition 16.1.1) | three converging stages of catabolism; diverging anabolism | coupled by ATP and NAD(P)H; opposing routes differ in at least one step |
| Biochemical standard state (Definition 16.2.2) | pH 7, 1 mM free $\ce{Mg^2+}$, $\ce{H2O}$ omitted; $\Delta_{\mathrm{r}}G'^{\circ} = -RT\ln K'$ (Eq. (16.1)) | 5.71 kJ mol⁻¹ per factor 10 in $K'$ at 25 °C; each released $\ce{H+}$ shifts $\Delta_{\mathrm{r}}G'^{\circ}$ by −40 kJ mol⁻¹ relative to $\Delta_{\mathrm{r}}G^\circ$ |
| Actual Gibbs energy (Formula 16.2.1) | $\Delta_{\mathrm{r}}G = RT\ln(Q/K')$, mass-action ratio $Q$ (Definition 16.2.3) | the criterion of direction in the cell; dilution favors cleavage (−17.8 kJ mol⁻¹ per extra product at 1 mM) |
| Coupling | $\Delta_{\mathrm{r}}G'^{\circ}$ add, $K'$ multiply; one ATP ≈ factor $10^{8}$ in the cell | requires a shared intermediate (group transfer) |
| ATP hydrolysis | $\Delta_{\mathrm{r}}G'^{\circ} = -30.5$; $\Delta G_{\mathrm{p}} = -47$ to $-65\,\mathrm{kJ\,mol^{-1}}$ in cells (Definition 16.3.1, Example 16.3.1) | charge separation, resonance, ionization, solvation; kinetically stable; [ATP]/[ADP] held ~$10^{9}$ times above equilibrium |
| Transfer potential (Definition 16.3.2) | PEP −61.9 > 1,3-BPG −49.3 > PCr −43.0 > ATP −30.5 > G6P −13.8 | ATP carries phosphoryl groups from catabolic donors to acceptors |
| Group transfer (16.3.4) | γ: phosphoryl; β: pyrophosphoryl; α: adenylyl + $\mathrm{PP_i}$ hydrolysis (−64.8 kJ mol⁻¹ in total) | ATP acts covalently; direct hydrolysis only for conformational work |
| Nucleotide kinases (Definitions 16.3.3, 16.3.4) | NDP kinase; adenylate kinase 2 ADP ⇌ ATP + AMP; creatine kinase −12.5 kJ mol⁻¹ | all NTPs kept charged; AMP as signal; PCr buffers [ATP] in muscle |
| Redox | $E'^{\circ}$ at pH 7 (H electrode −0.414 V); Nernst Eq. (16.3); $\Delta_{\mathrm{r}}G'^{\circ} = -zF\Delta E'^{\circ}$ (Formula 16.4.1) | NADH → $\ce{O2}$: 1.136 V, −219 kJ mol⁻¹ (Example 16.4.2) |
| NAD and NADP (Definition 16.5.1) | hydride at C-4; 340 nm; $E'^{\circ} \approx -0.32\,\mathrm{V}$; cytosolic $[\ce{NAD+}]/[\mathrm{NADH}] \approx 10^{3}$, $[\ce{NADP+}]/[\mathrm{NADPH}] \approx 10^{-2}$ | NAD for catabolic oxidations, NADPH for reductive biosynthesis; niacin, pellagra |
| Flavoproteins (Definition 16.5.2) | FMN, FAD from riboflavin; 1 or 2 electrons, semiquinone; $E'^{\circ}$ set by the protein | bridge between 2-electron and 1-electron carriers |

## Questions

1. The reaction fructose 1,6-bisphosphate ⇌ dihydroxyacetone phosphate + glyceraldehyde 3-phosphate has $\Delta_{\mathrm{r}}G'^{\circ} = +23.8\,\mathrm{kJ\,mol^{-1}}$ at $25\,^\circ\mathrm{C}$. (a) Calculate $K'$. (b) If [fructose 1,6-bisphosphate] = 50 µM, what is the largest concentration of the two products (assumed equal) at which the reaction still proceeds forward? (c) Why is this reaction so much more favorable at low concentrations than an isomerization with the same $\Delta_{\mathrm{r}}G'^{\circ}$?

   **Answer** (a) $K' = \mathrm{e}^{-23.8/2.479} = \mathrm{e}^{-9.60} = 6.8 \times 10^{-5}\,\mathrm{M}$. (b) The reaction proceeds forward while $Q = x^2/(5 \times 10^{-5}) < K'$, that is $x < \sqrt{6.8 \times 10^{-5} \times 5 \times 10^{-5}} = 5.8 \times 10^{-5}\,\mathrm{M}$, about 58 µM. (c) One molecule gives two: $Q$ contains one more concentration factor in the numerator, so at concentrations of order $10^{-5}$–$10^{-4}\,\mathrm{M}$ the term $RT\ln Q$ is lowered by $RT\ln 10^{-4.5} \approx -26\,\mathrm{kJ\,mol^{-1}}$ relative to the standard state. An isomerization has the same number of molecules on both sides, and its $Q$ does not depend on the overall dilution.

2. Compute the phosphorylation potential in a cell with [ATP] = 5 mM, [ADP] = 0.5 mM and [$\mathrm{P_i}$] = 5 mM at $37\,^\circ\mathrm{C}$. What would it be if the cell let [ATP] fall to 2 mM, the total adenine nucleotide staying constant (assume AMP negligible)?

   **Answer** $\Delta G_{\mathrm{p}} = -30.5 + 2.58\ln(0.5 \times 10^{-3} \times 5 \times 10^{-3}/5 \times 10^{-3}) = -30.5 + 2.58 \times (-7.60) = -50.1\,\mathrm{kJ\,mol^{-1}}$. With [ATP] = 2 mM and [ADP] = 3.5 mM: $-30.5 + 2.58\ln(3.5 \times 10^{-3} \times 5 \times 10^{-3}/2 \times 10^{-3}) = -30.5 + 2.58 \times (-4.74) = -42.7\,\mathrm{kJ\,mol^{-1}}$. Every ATP-dependent reaction would lose about 7 kJ mol⁻¹ of driving force, a factor of about 20 in the attainable product ratio, besides the kinetic effect of less saturated enzymes; this is why cells defend [ATP]/[ADP] so strongly.

3. Explain why the hydrolysis of phosphoenolpyruvate releases twice as much free energy as that of glucose 6-phosphate, although both are phosphate esters.

   **Answer** Hydrolysis of glucose 6-phosphate gives glucose, a stable alcohol, and $\mathrm{P_i}$; the gain comes mainly from the resonance and solvation of $\mathrm{P_i}$. Hydrolysis of PEP gives $\mathrm{P_i}$ and the enol of pyruvate, which immediately tautomerizes to the keto form, a far more stable species (the keto–enol equilibrium of pyruvate lies strongly on the keto side); the reactant has only the enol form available. The tautomerization contributes most of the difference, $-61.9$ against $-13.8\,\mathrm{kJ\,mol^{-1}}$.

4. Activation of a fatty acid, fatty acid + CoA + ATP → fatty acyl-CoA + AMP + $\mathrm{PP_i}$, has a small $\Delta_{\mathrm{r}}G'^{\circ}$. Using the values of 16.3, explain why the cell spends "two high-energy bonds" on it and why the reaction is nevertheless written with a single arrow.

   **Answer** Formation of the thioester from the free acid is endergonic by about $+31\,\mathrm{kJ\,mol^{-1}}$ (the reverse of thioester hydrolysis, $-31.4$), while ATP → AMP + $\mathrm{PP_i}$ provides $-45.6$; the sum is only about $-15\,\mathrm{kJ\,mol^{-1}}$. Pyrophosphatase hydrolyzes the $\mathrm{PP_i}$ ($-19.2$), giving about $-34\,\mathrm{kJ\,mol^{-1}}$ overall, $K' \sim 10^{6}$; in the cell, where [$\mathrm{PP_i}$] is kept very low, the reaction is effectively irreversible. The energy is coupled through a covalent intermediate, the acyl adenylate, formed by attack of the carboxylate on the α phosphorus.

5. Calculate $\Delta_{\mathrm{r}}G'^{\circ}$ for the oxidation of succinate by ubiquinone (succinate + Q → fumarate + $\ce{QH2}$) and for the oxidation of malate by $\ce{NAD+}$. The citric acid cycle oxidizes both; why does it use different acceptors?

   **Answer** Succinate/Q: $\Delta E'^{\circ} = 0.045 - 0.031 = 0.014\,\mathrm{V}$, $\Delta_{\mathrm{r}}G'^{\circ} = -2 \times 96.5 \times 0.014 = -2.7\,\mathrm{kJ\,mol^{-1}}$. Malate/$\ce{NAD+}$: $\Delta E'^{\circ} = -0.320 - (-0.166) = -0.154\,\mathrm{V}$, $\Delta_{\mathrm{r}}G'^{\circ} = +29.7\,\mathrm{kJ\,mol^{-1}}$ (driven forward in the cycle by the removal of oxaloacetate by citrate synthase). Oxidation of a $\ce{-CH2-CH2-}$ group to $\ce{-CH=CH-}$ has a potential near 0 V, too positive for $\ce{NAD+}$ (it would need $+68\,\mathrm{kJ\,mol^{-1}}$); a protein-bound FAD with $E'^{\circ}$ near 0 V and ubiquinone can accept these electrons. The more reducing alcohol-to-ketone oxidation of malate can use $\ce{NAD+}$, which delivers its electrons to the respiratory chain at a lower potential and so yields more ATP.

6. (Open question) Red blood cells have no mitochondria. Using the Nernst equation, estimate how the potential of the cytosolic NAD pool would change if the free $[\ce{NAD+}]/[\mathrm{NADH}]$ ratio fell from 700 to 7 (as in severe hypoxia), and discuss what this means for glyceraldehyde 3-phosphate dehydrogenase and lactate dehydrogenase.

   **Answer** Outline: $E = E'^{\circ} + (RT/2F)\ln([\ce{NAD+}]/[\mathrm{NADH}])$; a hundredfold fall changes $E$ by $-13.4\,\mathrm{mV} \times \ln 100 = -62\,\mathrm{mV}$, from about $-0.23$ to $-0.29\,\mathrm{V}$, equivalent to $+12\,\mathrm{kJ\,mol^{-1}}$ for every reaction that reduces $\ce{NAD+}$. The glyceraldehyde 3-phosphate dehydrogenase step, near equilibrium in the cell, would be pushed backward and glycolysis would slow unless NADH is reoxidized. Lactate dehydrogenase, which oxidizes NADH with pyruvate, becomes more favorable; it is the pathway that keeps $[\ce{NAD+}]/[\mathrm{NADH}]$ high in cells without respiration (7.1.18). In erythrocytes, which always depend on this, the ratio is set by the lactate/pyruvate ratio through the near-equilibrium LDH reaction.
