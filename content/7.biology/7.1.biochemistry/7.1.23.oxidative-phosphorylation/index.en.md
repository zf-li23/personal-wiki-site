---
title: Oxidative Phosphorylation
description: The mitochondrial respiratory chain, its carriers and the four complexes (Complex I, Complex II and other flavoproteins, Complex III and the Q cycle, Complex IV), respirasomes and reactive oxygen species; chemiosmotic coupling and the proton-motive force with its evidence; ATP synthase, the binding-change mechanism and rotational catalysis, c-ring stoichiometry and the P/O ratio, the adenine nucleotide and phosphate carriers and the NADH shuttles; acceptor control, IF1, hypoxia and the coordinated regulation of ATP-producing pathways; thermogenesis, steroid hydroxylation, apoptosis and the mitochondrial genome; alternative respiratory pathways of plants and bacteria; the pathway card of oxidative phosphorylation.
---

Oxidative phosphorylation is the final stage of **catabolism** in aerobic organisms. The oxidations of **glycolysis** (7.1.18), the **pyruvate dehydrogenase complex** and the **citric acid cycle** ([7.1.20](/7.1.20)), **β oxidation** ([7.1.21](/7.1.21)) and amino acid degradation ([7.1.22](/7.1.22)) collect electrons as **NADH** and as reduced flavins; here these electrons flow through a chain of membrane-bound carriers to $\ce{O2}$, and the free energy released, $-219\,\mathrm{kJ\,mol^{-1}}$ per NADH under standard conditions ([7.1.16](/7.1.16#sec-16.4.4)), is used to make most of the ATP of a nonphotosynthetic cell: about 26 of the 30 to 32 ATP obtained from one glucose. The chapter is organized around one idea, the chemiosmotic theory of Peter Mitchell: electron transfer pumps protons across a membrane, and the electrochemical gradient of protons drives ATP synthesis by a rotary **enzyme**. The same principle drives **photophosphorylation** in chloroplasts and bacteria ([7.1.24](/7.1.24)), and the transport and motility that use the proton gradient directly. The thermodynamics of redox reactions and of the electrochemical potential is in [6.1.11](/6.1.11), [6.3.13](/6.3.13) and [7.1.16](/7.1.16); the energetics of coupled flows in the language of non-equilibrium thermodynamics is in [6.3.18](/6.3.18#sec-18.2.5); the **F-type ATPase** as a class of **transporters** was introduced in [7.1.13](/7.1.13#sec-13.5.3).

## 23.1. The Mitochondrial Respiratory Chain

### 23.1.1. Mitochondria

Eugene Kennedy and Albert Lehninger showed in 1948 that mitochondria are the site of oxidative phosphorylation in **eukaryotes**. A mitochondrion has two membranes. The outer membrane is permeable to small molecules and ions ($M_{\mathrm{r}}$ below about 5000), which pass through porins (the voltage-dependent anion channel, VDAC). The inner membrane is impermeable to most small molecules and ions, including $\ce{H+}$; species cross it only on specific transporters. It is folded into cristae, which carry the respiratory chain and ATP synthase; a liver mitochondrion has more than 10 000 sets of them, and heart mitochondria, with more profuse cristae, about three times as many per mitochondrion. The matrix, enclosed by the inner membrane, contains the **pyruvate dehydrogenase complex**, the enzymes of the **citric acid cycle**, of **β oxidation** and of amino acid oxidation: all the pathways of fuel oxidation except glycolysis. Mitochondria are not static beans; they form networks that divide by fission and join by fusion, and damaged ones are removed by mitophagy. Their bacterial origin (**endosymbiotic theory**, [7.1.1](/7.1.1)) is evident in their double membrane, their own **genome** and **ribosomes** (23.5.4), and in the close similarity of their respiratory chain and ATP synthase to those of bacteria.

The two sides of the inner membrane are named by their charge in the respiring state: the matrix is the N side (negative and alkaline), the intermembrane space the P side (positive and acidic); the intermembrane space is in equilibrium with the cytosol for small molecules.

### 23.1.2. Electron Carriers

Most electrons enter the chain from NAD-linked dehydrogenases (pyruvate, isocitrate, α-ketoglutarate and malate dehydrogenases, β-hydroxyacyl-CoA dehydrogenase, glutamate dehydrogenase) and from **flavoproteins**. Five kinds of carriers act in the chain: the nicotinamide nucleotides and the **flavoproteins** of [7.1.16](/7.1.16#sec-16.5), and three more.

**Definition 23.1.1 (Respiratory Chain)** The **respiratory chain** (electron-transport chain) is the series of electron carriers in the inner mitochondrial membrane (or the plasma membrane of bacteria) that transfers electrons from NADH and from reduced flavoproteins to $\ce{O2}$, organized into four complexes and two mobile carriers, ubiquinone and cytochrome c.

**Definition 23.1.2 (Ubiquinone)** **Ubiquinone** (coenzyme Q, Q) is a lipid-soluble benzoquinone with a long isoprenoid side chain (10 isoprene units in humans, $\mathrm{Q_{10}}$) that diffuses within the inner membrane; it accepts one electron to form the semiquinone radical ($\mathrm{QH^{\bullet}}$, or $\mathrm{Q^{\bullet -}}$) and two electrons and two protons to form ubiquinol ($\ce{QH2}$).

```smiles
COC1=C(OC)C(=O)C(C)=C(CC=C(C)C)C1=O Q
COc1c(O)c(C)c(CC=C(C)C)c(O)c1OC QH2
```

(Ubiquinone with one isoprene unit, $\mathrm{Q_1}$, is drawn.) Because it carries both electrons and protons, and because it can act at the junction between a two-electron donor and one-electron acceptors, ubiquinone is the carrier that couples electron flow to proton movement in Complex III.

**Definition 23.1.3 (Cytochrome)** A **cytochrome** is a protein with one or more **heme** groups ([7.1.7](/7.1.7#sec-7.2.1)) whose iron cycles between $\ce{Fe^3+}$ and $\ce{Fe^2+}$, transferring one electron; mitochondria contain cytochromes of types a, b and c, which differ in the substituents of the porphyrin and are recognized by the longest-wavelength absorption band of the reduced form, near 600, 560 and 550 nm.

The **hemes** of a and b cytochromes are bound tightly but noncovalently; the heme of c-type cytochromes is attached covalently through thioether bonds to two Cys **residues**. Heme a carries a long **isoprenoid** tail. The **protein** environment sets the reduction potential of each heme, which is why the cytochromes of one chain can have different $E'^{\circ}$. Most cytochromes are **integral membrane proteins**; cytochrome c is a small soluble protein of the intermembrane space.

**Definition 23.1.4 (Iron–Sulfur Protein)** An **iron–sulfur protein** contains iron coordinated by inorganic sulfide and by the sulfur atoms of Cys residues, in clusters of one, two or four iron atoms ([2Fe–2S], [4Fe–4S]); each cluster transfers one electron. In the Rieske proteins one iron of a [2Fe–2S] cluster is coordinated by two His instead of two Cys.

The reduction potentials of Fe–S clusters span $-0.65$ to $+0.45\,\mathrm{V}$; at least eight function in mitochondrial electron transfer. Complex IV contains, in addition, copper ions ($\mathrm{Cu_A}$, a binuclear center, and $\mathrm{Cu_B}$).

### 23.1.3. Determining the Order of the Carriers

The sequence of the carriers was established by four independent methods.

1. Standard reduction potentials. Electrons flow spontaneously from carriers of lower to carriers of higher $E'^{\circ}$; the potentials (figure below) give NADH → **FMN** → Q → cytochrome b → $c_1$ → c → a → $a_3$ → $\ce{O2}$. The actual potentials in the cell depend on the ratios of oxidized to reduced forms (the **Nernst equation**, [7.1.16](/7.1.16#sec-16.4.3)), so this order is a guide, not a proof.
2. Oxidation kinetics. The chain is fully reduced in the absence of $\ce{O2}$; when $\ce{O2}$ is admitted, the carrier nearest to $\ce{O2}$ is oxidized first, the next one second, and so on, which rapid spectrophotometry follows through the distinct absorption bands of the cytochromes.
3. Inhibitors. With an electron donor and $\ce{O2}$ present, an inhibitor of one step leaves the carriers before it fully reduced and those after it fully oxidized (a "crossover point"); rotenone, antimycin A and cyanide each give a characteristic pattern (Table in 23.2.4).
4. Isolation of complexes. Gentle detergent extraction of the inner membrane separates four complexes, each of which catalyzes a part of the overall reaction with specific donors and acceptors: NADH → Q (Complex I), succinate → Q (Complex II), $\ce{QH2}$ → cytochrome c (Complex III), cytochrome c → $\ce{O2}$ (Complex IV).

![The respiratory chain on the redox scale. Standard transformed reduction potentials E′° of the carriers in the order of electron flow (Lehninger 8e, Tables 13-7 and 19-2); electrons move upward, from NADH (−0.320 V) to O₂/H₂O (+0.816 V). The three proton-pumping segments are shaded; for each, the drop in potential, the standard Gibbs energy per pair of electrons, ΔG′° = −2FΔE′°, and the number of protons moved across the membrane per pair are given. Succinate enters at the level of ubiquinone through Complex II, which does not pump protons. The right axis gives the standard Gibbs energy for transferring two electrons from each level to O₂](./plots/respiratory-chain-tower.py)

| Complex | Name | Mass (kDa), **subunits** (mammals; bacteria) | **Prosthetic groups** | Reaction (per 2 e⁻) |
|---|---|---|---|---|
| I | NADH:ubiquinone oxidoreductase (NADH dehydrogenase) | ~1000, 45 (14) | FMN, 8–9 Fe–S | NADH + 5 $\ce{H+_N}$ + Q → $\ce{NAD+}$ + $\ce{QH2}$ + 4 $\ce{H+_P}$ |
| II | succinate dehydrogenase | 140, 4 | **FAD**, 3 Fe–S, heme b | succinate + Q → fumarate + $\ce{QH2}$ |
| III | ubiquinone:cytochrome c oxidoreductase (cytochrome $bc_1$ complex) | 250, 11 per monomer (3) | hemes $b_{\mathrm{L}}$, $b_{\mathrm{H}}$, $c_1$; Rieske [2Fe–2S] | $\ce{QH2}$ + 2 cyt c(ox) + 2 $\ce{H+_N}$ → Q + 2 cyt c(red) + 4 $\ce{H+_P}$ |
| — | cytochrome c | 13, 1 | heme c | mobile carrier in the intermembrane space |
| IV | cytochrome oxidase | 204, 13 per monomer (3–4) | hemes a, $a_3$; $\mathrm{Cu_A}$, $\mathrm{Cu_B}$ | 2 cyt c(red) + 4 $\ce{H+_N}$ + ½ $\ce{O2}$ → 2 cyt c(ox) + 2 $\ce{H+_P}$ + $\ce{H2O}$ |

(Data from Lehninger 8e, Table 19-3; the mass of mammalian Complex I from **cryo-EM** structures.)

**Definition 23.1.5 (Complexes I–IV)** The four electron-transferring complexes of the respiratory chain are **Complex I** (NADH:ubiquinone oxidoreductase), **Complex II** (succinate dehydrogenase), **Complex III** (ubiquinone:cytochrome c oxidoreductase, the cytochrome $bc_1$ complex) and **Complex IV** (cytochrome c oxidase); ATP synthase is sometimes called Complex V.

### 23.1.4. Complex I: NADH to Ubiquinone

Complex I is L-shaped: a hydrophilic arm projects into the matrix, a membrane arm lies in the inner membrane. NADH transfers a hydride to FMN at the tip of the matrix arm; FMN, the junction between two-electron and one-electron chemistry, passes the electrons one at a time along a chain of seven Fe–S clusters, about 90 Å long, to cluster N2 near the membrane, which reduces ubiquinone bound in a long tunnel at the base of the arm. The reaction is vectorial:

$$
\ce{NADH} + 5\,\ce{H+_N} + \ce{Q} \to \ce{NAD+} + \ce{QH2} + 4\,\ce{H+_P}, \tag{23.1}
$$
one $\ce{H+}$ and the hydride from NADH reducing Q, and four protons moved from the matrix to the intermembrane space.

The 14 core subunits conserved from bacteria to mammals contain all redox centers; 31 supernumerary subunits of the mammalian enzyme assemble and stabilize it. Three subunits of the membrane arm (ND2, ND4 and ND5 in mammals) are homologous to $\ce{Na+}/\ce{H+}$ **antiporters** and each carries a proton half-channel pair; a fourth path lies near the quinone site. The quinone site is some 30 Å from the nearest proton path, so the coupling must be indirect. In the current model, derived from crystal and cryo-EM structures since 2013, the reduction of Q and its movement in the tunnel change the charge state of a cluster of acidic residues at the quinone site; this electrostatic and conformational change propagates along a central axis of charged residues through the membrane arm and drives proton transfer in the four paths, so that the free energy of one strongly exergonic redox step is divided into four packets. The details, including the exact sequence of protonations, are still being worked out. Inhibitors (rotenone, the barbiturate amytal, piericidin A) block electron transfer from N2 to Q.

Complex I operates close to equilibrium in respiring mitochondria: with $\Delta E \approx 0.36\,\mathrm{V}$ ($-70\,\mathrm{kJ\,mol^{-1}}$ per pair, standard values) and four protons each costing about $19\,\mathrm{kJ\,mol^{-1}}$ (23.2.2), little free energy is left. When the ubiquinone pool is highly reduced and the proton-motive force high (for example when succinate, accumulated during ischemia, is oxidized rapidly on reperfusion), Complex I runs backward, reducing $\ce{NAD+}$ with electrons from $\ce{QH2}$ (reverse electron transport), and leaks electrons to $\ce{O2}$ (23.1.9).

### 23.1.5. Complex II and Other Flavoproteins That Reduce Ubiquinone

Complex II is succinate dehydrogenase, the only membrane-bound enzyme of the **citric acid cycle** ([7.1.20](/7.1.20)). Subunits A and B extend into the matrix: A binds succinate and a covalently bound FAD, B contains three Fe–S clusters; subunits C and D span the membrane and bind heme b and the quinone. Electrons travel about 40 Å from succinate to Q in steps of no more than 11 Å, short enough for fast tunneling. The heme b is not on the main path; it reduces the leakage of electrons to $\ce{O2}$. Because $E'^{\circ}$(fumarate/succinate) $= +0.031\,\mathrm{V}$ is close to that of Q, Complex II does not pump protons; the electrons pump protons only in Complexes III and IV. **Mutations** in Complex II subunits near heme b or the Q site cause hereditary paraganglioma and pheochromocytoma; the accumulated succinate inhibits α-ketoglutarate-dependent dioxygenases, among them the prolyl hydroxylases that mark HIF-1α for degradation (23.4.3), so that succinate acts as an **oncometabolite**.

Three other flavoproteins also reduce ubiquinone directly. Acyl-CoA dehydrogenase, the first enzyme of β oxidation, passes electrons through the electron-transferring flavoprotein (ETF) and ETF:ubiquinone oxidoreductase ([7.1.21](/7.1.21)); glycerol 3-phosphate dehydrogenase on the outer face of the inner membrane oxidizes glycerol 3-phosphate from the cytosol (23.3.7); dihydroorotate dehydrogenase of pyrimidine synthesis ([7.1.28](/7.1.28)) feeds electrons into the Q pool. All these electrons bypass Complex I.

### 23.1.6. Complex III and the Q Cycle

Complex III couples the transfer of electrons from ubiquinol to cytochrome c with the movement of protons from the matrix to the intermembrane space. It is a dimer; each monomer has 11 subunits in mammals, of which three form the functional core: cytochrome b, with two hemes ($b_{\mathrm{L}}$ near the P side and $b_{\mathrm{H}}$ near the N side), the Rieske iron–sulfur protein, and cytochrome $c_1$. The complex has two quinone-binding sites on opposite sides of the membrane: $\mathrm{Q_P}$ (also $\mathrm{Q_o}$), near the P side, where $\ce{QH2}$ is oxidized, and $\mathrm{Q_N}$ ($\mathrm{Q_i}$), near the N side, where Q is reduced.

**Definition 23.1.6 (Q Cycle)** The **Q cycle** is the mechanism of Complex III (and of the cytochrome $b_6f$ complex) by which the oxidation of ubiquinol at the $\mathrm{Q_P}$ site is split between two paths: one electron goes through the Rieske Fe–S center to cytochrome $c_1$ and cytochrome c, the other through hemes $b_{\mathrm{L}}$ and $b_{\mathrm{H}}$ to a ubiquinone at the $\mathrm{Q_N}$ site; two ubiquinol oxidations reduce one ubiquinone to ubiquinol at $\mathrm{Q_N}$, so that per two electrons delivered to cytochrome c, four protons are released on the P side and two are taken up from the N side:

$$
\ce{QH2} + 2\,\text{cyt }c(\mathrm{ox}) + 2\,\ce{H+_N} \to \ce{Q} + 2\,\text{cyt }c(\mathrm{red}) + 4\,\ce{H+_P}. \tag{23.2}
$$

The cycle runs in two stages. In each, one $\ce{QH2}$ at $\mathrm{Q_P}$ gives up two protons to the intermembrane space and two electrons that take different paths. In the first stage the b-heme electron reduces a Q at $\mathrm{Q_N}$ to the semiquinone; in the second it completes the reduction to $\ce{QH2}$ with two protons from the matrix. The net result per two electrons is: two $\ce{QH2}$ oxidized, one regenerated, four protons out, two in. The cycle solves the problem of passing electrons from a two-electron carrier to the one-electron hemes, and it doubles the number of protons moved, because ubiquinone itself carries protons across the membrane (Mitchell's "redox loop"). The bifurcation at $\mathrm{Q_P}$ is enforced by the Rieske protein, whose head **domain** swings between the quinol site and cytochrome $c_1$; if both electrons of the quinol went to the high-potential chain, no energy would be conserved by the b hemes. Antimycin A binds at $\mathrm{Q_N}$, myxothiazol and stigmatellin at $\mathrm{Q_P}$. Cytochrome c, reduced by $c_1$, diffuses in the intermembrane space to Complex IV.

### 23.1.7. Complex IV: Cytochrome c to O₂

Complex IV, cytochrome oxidase, is a dimer of 13-subunit monomers in mammals (3 or 4 subunits in bacteria, still able to pump protons). Subunit II contains the binuclear $\mathrm{Cu_A}$ center, which accepts electrons from cytochrome c on the P side; subunit I contains heme a and the binuclear center of heme $a_3$ and $\mathrm{Cu_B}$, where $\ce{O2}$ is bound and reduced; subunit III is needed for rapid proton movement. Electrons flow cytochrome c → $\mathrm{Cu_A}$ → heme a → heme $a_3$–$\mathrm{Cu_B}$ → $\ce{O2}$. The four electrons needed to reduce one $\ce{O2}$ arrive one at a time; the partially reduced intermediates (a peroxy and a ferryl species) stay bound to the binuclear center until two waters are released, so that very little superoxide or peroxide escapes. For each $\ce{O2}$ the enzyme takes up four "**substrate**" protons from the matrix to form water and pumps four more across the membrane, through two proton-conducting channels (the D and K channels):

$$
4\,\text{cyt }c(\mathrm{red}) + 8\,\ce{H+_N} + \ce{O2} \to 4\,\text{cyt }c(\mathrm{ox}) + 4\,\ce{H+_P} + 2\,\ce{H2O}. \tag{23.3}
$$

The consumption of matrix protons for water formation contributes to the gradient as much as pumping does: both remove positive charge from the N side. Cyanide, azide, hydrogen sulfide and carbon monoxide inhibit Complex IV by binding to heme $a_3$; cyanide poisoning stops respiration in seconds.

### 23.1.8. Respirasomes and the Overall Stoichiometry

The complexes are not distributed at random. Complexes I, III and IV associate into supercomplexes, the largest of which ($\mathrm{I_1III_2IV_1}$) has been resolved by cryo-EM; Complex II is generally free. In bovine heart the ratio of Complexes I : II : III : IV is about 1.1 : 1.3 : 3.0 : 6.7.

**Definition 23.1.7 (Respirasome)** A **respirasome** is a supercomplex of the respiratory chain containing Complexes I, III and IV, able to transfer electrons from NADH to $\ce{O2}$.

The function of respirasomes is still debated: they may stabilize Complex I and limit the production of reactive oxygen species; there is little evidence that they channel ubiquinone or cytochrome c, which exchange freely with the pools in the membrane and the intermembrane space.

Summing Eqs. (23.1)–(23.3), per pair of electrons from NADH four protons are pumped by Complex I, four by Complex III and two by Complex IV:

$$
\ce{NADH} + 11\,\ce{H+_N} + \tfrac12\ce{O2} \to \ce{NAD+} + 10\,\ce{H+_P} + \ce{H2O}, \tag{23.4}
$$
and per succinate (through Complex II), six. The figure shows the whole chain with its electron and proton paths.

![The inner mitochondrial membrane, matrix (N side) below. Complex I takes electrons from NADH at the tip of its matrix arm and passes them through FMN and a chain of Fe–S clusters to ubiquinone, pumping 4 H⁺ through its membrane arm; Complex II feeds electrons from succinate into the ubiquinone pool without pumping; ubiquinol diffuses to Complex III, which in the Q cycle takes up 2 H⁺ from the matrix at the Qₙ site, releases 4 H⁺ at the Qₚ site and reduces cytochrome c; cytochrome c carries single electrons to the CuA center of Complex IV, which reduces O₂ to water and pumps 2 H⁺ (all per pair of electrons). Protons return through the Fₒ part of ATP synthase (bovine c₈ ring, 8/3 H⁺ per ATP); the adenine nucleotide translocase (ANT) exchanges matrix ATP⁴⁻ for cytosolic ADP³⁻, and the phosphate carrier (PiC) imports H₂PO₄⁻ with one H⁺](./plots/inner-membrane-complexes.py)

### 23.1.9. Reactive Oxygen Species

**Definition 23.1.8 (Reactive Oxygen Species)** **Reactive oxygen species** (ROS) are partially reduced or excited forms of oxygen more reactive than $\ce{O2}$: the superoxide radical $\ce{O2^{\bullet -}}$, hydrogen peroxide $\ce{H2O2}$, the hydroxyl radical $\ce{HO^{\bullet}}$ and singlet oxygen.

Single electrons leak from the chain to $\ce{O2}$, mainly from the flavin of Complex I and from the semiquinone at the $\mathrm{Q_P}$ site of Complex III, forming **superoxide**; 0.2–2% of the $\ce{O2}$ consumed may be converted. Leakage is high when the chain is highly reduced and the proton-motive force large: when no ADP is available, when $\ce{O2}$ is scarce, or during reverse electron transport. Superoxide dismutase (MnSOD in the matrix, CuZnSOD in the intermembrane space and cytosol) converts it to $\ce{H2O2}$ ($2\,\ce{O2^{\bullet -}} + 2\,\ce{H+} \to \ce{H2O2} + \ce{O2}$); glutathione peroxidase and peroxiredoxins reduce $\ce{H2O2}$ to water with glutathione and **thioredoxin**, which are regenerated with **NADPH** from the **pentose phosphate pathway** ([7.1.18](/7.1.18#sec-18.6.1)) or from nicotinamide nucleotide transhydrogenase in the matrix. Superoxide also releases $\ce{Fe^2+}$ from the [4Fe–4S] cluster of aconitase, and $\ce{Fe^2+}$ with $\ce{H2O2}$ forms the hydroxyl radical (Fenton reaction), which damages **lipids**, proteins and **DNA**. At low levels, mitochondrial $\ce{H2O2}$ is a signal, for example of hypoxia (23.4.3).

## 23.2. Chemiosmotic Coupling

### 23.2.1. Oxidation and Phosphorylation Are Obligately Coupled

The operational definition of coupling comes from experiments with isolated mitochondria in an oxygen electrode. Mitochondria suspended with ADP and $\mathrm{P_i}$ consume little $\ce{O2}$ until an oxidizable substrate is added; with substrate but no ADP, they also respire slowly; only with both does respiration become fast, and ATP is made. Inhibitors of electron transfer (cyanide, antimycin A) stop both respiration and ATP synthesis, as expected; but inhibitors of ATP synthase (oligomycin, venturicidin), which do not touch the electron carriers, also stop respiration. Electron flow and phosphorylation are obligately coupled: neither proceeds without the other. Uncouplers such as 2,4-dinitrophenol (DNP) break this dependence, so that respiration runs at its maximal rate without ATP synthesis.

**Definition 23.2.1 (Oxidative Phosphorylation)** **Oxidative phosphorylation** is the synthesis of ATP from ADP and $\mathrm{P_i}$ driven by the transfer of electrons from NADH or reduced flavoproteins to $\ce{O2}$ through the respiratory chain, coupled through a transmembrane proton gradient; it is distinguished from **substrate-level phosphorylation** ([7.1.18](/7.1.18#sec-18.2.3)) and from photophosphorylation ([7.1.24](/7.1.24)).

**Definition 23.2.2 (Respiratory Control)** The dependence of the rate of respiration of coupled mitochondria on the availability of ADP, the acceptor of $\mathrm{P_i}$, is called **respiratory control** or **acceptor control**; the **respiratory control ratio** is the rate of $\ce{O2}$ consumption with ADP (state 3) divided by the rate after the ADP has been phosphorylated (state 4).

![Simulated oxygen-electrode trace of isolated mitochondria oxidizing glutamate and malate. Adding substrate starts slow respiration (state 2); each pulse of ADP (150 nmol) gives fast respiration (state 3) until it has been phosphorylated, when respiration returns to the slow, leak-limited rate (state 4); the O₂ consumed in each burst measures the ADP/O ratio. Oligomycin, which blocks the proton channel of ATP synthase, holds respiration at the leak rate whatever the ADP; the uncoupler DNP lets protons return without ATP synthesis, and respiration becomes maximal until the O₂ is exhausted; cyanide blocks Complex IV. Model: O₂ consumption J = J₄ + (J₃ − J₄)[ADP]/(K + [ADP]), each O₂ above the leak rate phosphorylating 2 × 2.5 ADP; J₄ = 8, J₃ = 55 and J(DNP) = 75 nmol O₂ min⁻¹ mL⁻¹, K = 15 µM; the respiratory control ratio is about 7](./plots/oxygen-electrode.py)

### 23.2.2. The Chemiosmotic Theory and the Proton-Motive Force

In the 1950s most biochemists looked for a high-energy chemical intermediate that would couple oxidation to phosphorylation, as 1,3-bisphosphoglycerate does in glycolysis; none was ever found. Peter Mitchell proposed in 1961 that the intermediate is not a molecule but a gradient.

**Definition 23.2.3 (Chemiosmotic Theory)** The **chemiosmotic theory** holds that the free energy of electron transfer in the respiratory chain is conserved by pumping protons from the matrix across the inner membrane, which is impermeable to them, creating an electrochemical gradient of protons; protons flowing back down this gradient through ATP synthase drive the synthesis of ATP. The same mechanism couples electron transfer to ATP synthesis in chloroplasts and bacteria, and the gradient also drives transport and motility.

The free energy stored in the gradient is the difference of the **electrochemical potential** of $\ce{H+}$ between the two sides ([6.3.13](/6.3.13#sec-13.4.2), Formula 13.3.1 of [7.1.13](/7.1.13#sec-13.3.1)). We write the membrane potential as $\Delta\varphi = \varphi_{\mathrm{P}} - \varphi_{\mathrm{N}} > 0$ and the pH difference as $\Delta\mathrm{pH} = \mathrm{pH_N} - \mathrm{pH_P} > 0$ (Lehninger writes $\Delta\psi$ for $\Delta\varphi$).

**Definition 23.2.4 (Proton-Motive Force)** The **proton-motive force** is the free energy released when one mole of protons returns from the P side to the N side of a coupling membrane,

$$
\Delta\tilde\mu_{\mathrm{H^+}} = F\,\Delta\varphi + 2.303\,RT\,\Delta\mathrm{pH}, \tag{23.5}
$$
in $\mathrm{kJ\,mol^{-1}}$; expressed as a potential, $\Delta p = \Delta\tilde\mu_{\mathrm{H^+}}/F = \Delta\varphi + (2.303\,RT/F)\,\Delta\mathrm{pH}$, in volts (the p of $\Delta p$ is not a pressure). At $37\,^\circ\mathrm{C}$, $2.303\,RT/F = 61.5\,\mathrm{mV}$ per pH unit.

**Example 23.2.1** In actively respiring mitochondria $\Delta\varphi \approx 0.15$–$0.20\,\mathrm{V}$ and the matrix is about 0.75 pH units more alkaline than the intermembrane space. With $\Delta\varphi = 0.15\,\mathrm{V}$ at $37\,^\circ\mathrm{C}$,

$$
\Delta\tilde\mu_{\mathrm{H^+}} = (96.5\,\mathrm{kJ\,V^{-1}\,mol^{-1}})(0.15\,\mathrm{V}) + (5.94\,\mathrm{kJ\,mol^{-1}})(0.75) = 14.5 + 4.5 = 19\,\mathrm{kJ\,mol^{-1}},
$$
or $\Delta p \approx 0.20\,\mathrm{V}$; three quarters of it is electrical. Ten protons per NADH store about $190\,\mathrm{kJ}$, most of the $220\,\mathrm{kJ}$ released by the oxidation of NADH under standard conditions. In chloroplasts, where counterion movements collapse most of the membrane potential, the gradient is mainly a pH difference of about 3 units ([7.1.24](/7.1.24)).

A gradient of this size explains the stoichiometry of ATP synthesis. The **phosphorylation potential** in the matrix is about $+50\,\mathrm{kJ\,mol^{-1}}$ (Definition 16.3.1 of [7.1.16](/7.1.16#sec-16.3.2)); at $19\,\mathrm{kJ}$ per proton at least $50/19 \approx 2.6$ protons must pass through the synthase for each ATP, close to the $8/3$ of a mammalian c ring (23.3.5): the enzyme works not far from equilibrium, and indeed it can run backward as an ATP-driven proton pump when the gradient collapses (23.4.2). The coupling of a scalar reaction to a vectorial flow, and the requirement that the coupled pair produce entropy, are discussed in general terms in [6.3.18](/6.3.18#sec-18.2.5).

![Energetics and stoichiometry of chemiosmotic coupling. A: free energy released per mole of protons returning across the membrane, split into its electrical part FΔφ and its chemical part 2.303RTΔpH (Eq. (23.5)), for respiring mitochondria (Δφ = 0.15 or 0.20 V, ΔpH = 0.75, 37 °C) and for illuminated chloroplasts (ΔpH ≈ 3, small Δφ, 25 °C); mitochondria store the gradient mainly as a potential, chloroplasts as a pH difference. B: protons that pass through Fₒ per ATP, c/3, for the c-ring sizes measured in different organisms, and the P/O ratios predicted for mitochondria with one extra proton per ATP for transport (Eq. (23.6)), for NADH (10 H⁺ per pair) and succinate (6 H⁺)](./plots/p-o-ratio.py)

### 23.2.3. The Evidence

Each element of the theory has been tested.

- A closed membrane is required. Membrane fragments obtained by detergent or by shearing still transfer electrons from NADH or succinate to $\ce{O2}$, but make no ATP; vesicles that reseal (submitochondrial particles) recover phosphorylation.
- Protons are pumped. When respiration is started in a weakly buffered suspension, the medium acidifies; more protons are ejected with NADH-linked substrates than with succinate.
- Dissipating the gradient uncouples. Hydrophobic weak acids carry protons across the membrane and abolish ATP synthesis while respiration continues; **ionophores** collapse the gradient in other ways.
- An artificial gradient drives ATP synthesis without electron transfer. Mitochondria equilibrated at pH 9 in 0.1 M KCl and transferred to pH 7 with the $\ce{K+}$ **ionophore** valinomycin (which creates a membrane potential, matrix negative, as $\ce{K+}$ leaves) make ATP from ADP and $\mathrm{P_i}$; André Jagendorf's "acid bath" experiment (1966) showed the same for thylakoids, which make ATP in the dark after a jump of the external pH from 4 to 8 ([7.1.24](/7.1.24)). Reconstituted vesicles containing only bacteriorhodopsin, a light-driven proton pump of halobacteria, and a mitochondrial ATP synthase make ATP in the light (Racker and Stoeckenius, 1974).

**Definition 23.2.5 (Uncoupler)** An **uncoupler** is an agent that dissipates the proton-motive force without passing through ATP synthase, so that electron transfer continues without ATP synthesis; chemical uncouplers such as 2,4-dinitrophenol (DNP) and carbonyl cyanide p-trifluoromethoxyphenylhydrazone (FCCP) are lipid-soluble weak acids that carry protons across the membrane.

```smiles
Oc1ccc([N+](=O)[O-])cc1[N+](=O)[O-] DNP
FC(F)(F)Oc1ccc(NN=C(C#N)C#N)cc1 FCCP
```

The phenoxide of DNP is stabilized by resonance with the nitro groups, so that both the protonated acid and its anion are lipid-soluble and diffuse through the membrane: the acid enters the matrix, releases its proton, and the anion returns, driven by the membrane potential. In the 1930s DNP was sold as a slimming drug; it raises the metabolic rate by forcing fuel oxidation to compensate for the lost ATP, and fatal hyperthermia led to its withdrawal (it is still sold illegally). Mitchell received the Nobel Prize in Chemistry in 1978; the theory unified oxidative phosphorylation, photophosphorylation, active transport across membranes and the rotation of bacterial flagella.

### 23.2.4. Agents That Interfere with Oxidative Phosphorylation

| Type of interference | Agent | Target and mode of action |
|---|---|---|
| inhibition of electron transfer | rotenone, amytal, piericidin A | Complex I: block transfer from Fe–S (N2) to ubiquinone |
| | malonate | Complex II: competitive inhibitor of succinate oxidation |
| | antimycin A | Complex III, $\mathrm{Q_N}$ site: block transfer from heme $b_{\mathrm{H}}$ to Q |
| | myxothiazol, stigmatellin | Complex III, $\mathrm{Q_P}$ site: block transfer from $\ce{QH2}$ to the Rieske center |
| | cyanide, azide, CO, $\ce{H2S}$ | Complex IV: bind to heme $a_3$ |
| inhibition of ATP synthase | oligomycin, venturicidin | $\mathrm{F_o}$ proton channel |
| | DCCD (dicyclohexylcarbodiimide) | covalently modifies the essential carboxylate of the c subunits |
| | aurovertin | $\mathrm{F_1}$ |
| uncoupling | DNP, FCCP | lipid-soluble proton carriers |
| | valinomycin | $\ce{K+}$ ionophore, collapses $\Delta\varphi$ |
| | UCP1 (thermogenin) | physiological proton leak in brown fat (23.5.1) |
| inhibition of ATP/ADP exchange | atractyloside, bongkrekic acid | adenine nucleotide translocase (locked in the cytosol-facing and matrix-facing states) |

(After Lehninger 8e, Table 19-4.)

## 23.3. ATP Synthase

### 23.3.1. F₁ and Fₒ

Efraim Racker found in 1960 that the knob-like particles lining the matrix face of the inner membrane in electron micrographs could be removed by agitation: stripped vesicles still transferred electrons but leaked protons and made no ATP; the solubilized knobs hydrolyzed ATP (hence the name $\mathrm{F_1}$-ATPase), and adding them back restored the coupling. $\mathrm{F_1}$ was the first coupling factor identified.

**Definition 23.3.1 (ATP Synthase)** **ATP synthase** (F-type ATPase acting in the direction of synthesis, $\mathrm{F_oF_1}$, Complex V) is the enzyme of the inner mitochondrial membrane, the thylakoid membrane and the bacterial plasma membrane that synthesizes ATP from ADP and $\mathrm{P_i}$ driven by the flow of protons (in some bacteria $\ce{Na+}$) from the P to the N side. It consists of the peripheral $\mathrm{F_1}$ ($\alpha_3\beta_3\gamma\delta\varepsilon$), which carries the three catalytic sites on the β subunits, and the integral $\mathrm{F_o}$ ($a\,b_2\,c_n$, $n = 8$–$17$), whose ring of c subunits rotates past the stationary a subunit.

$\mathrm{F_1}$ is a flattened sphere, about 8 by 10 nm, in which three α and three β subunits alternate like the segments of an orange around the γ subunit, a long coiled-coil shaft. The c subunits, each a hairpin of two transmembrane helices, form a ring with an essential carboxylate (Glu in bovine mitochondria, Asp in *E. coli*) in the middle of the membrane; the γ and ε subunits form a foot that stands firmly on the ring. Subunit a, beside the ring, provides two half-channels, one open to each side of the membrane. The two b subunits and δ (called OSCP, the oligomycin-sensitivity conferring protein, in mitochondria) form the peripheral stalk, a stator that holds $\alpha_3\beta_3$ against the rotation of γ. In mitochondria the synthase forms dimers, whose rows bend the membrane and shape the cristae.

### 23.3.2. ATP Is Stabilized on the Surface of F₁

Paul Boyer's isotope-exchange experiments revealed the energetic peculiarity of the enzyme. When isolated $\mathrm{F_1}$ hydrolyzes ATP in $\mathrm{H_2{}^{18}O}$, the released $\mathrm{P_i}$ contains not one but three or four $^{18}\mathrm{O}$: the terminal phosphoanhydride bond is broken and re-formed many times before $\mathrm{P_i}$ leaves. On the enzyme surface the reaction $\mathrm{ADP} + \mathrm{P_i} \rightleftharpoons \mathrm{ATP} + \ce{H2O}$ is near equilibrium: measured rate constants of hydrolysis and synthesis, $10$ and $24\,\mathrm{s^{-1}}$, give $K'_{\mathrm{eq}} \approx 2.4$ and $\Delta G'^{\circ} \approx 0$, in contrast to $-30.5\,\mathrm{kJ\,mol^{-1}}$ in solution. The enzyme binds ATP with $K_{\mathrm{d}} \le 10^{-12}\,\mathrm{M}$ and ADP with $K_{\mathrm{d}} \approx 10^{-5}\,\mathrm{M}$; the difference, $RT\ln 10^{7} \approx 40\,\mathrm{kJ\,mol^{-1}}$, is **binding energy** ([7.1.8](/7.1.8#sec-8.3.1)) that pays for the formation of the bond. What requires energy is not making ATP but releasing it: the proton-motive force is needed to drive the tightly bound ATP off the enzyme. In the reaction-coordinate diagram of ATP synthase, the highest barrier is product release, not the chemical transition state.

### 23.3.3. The Binding-Change Mechanism and Rotational Catalysis

Crystal structures of bovine $\mathrm{F_1}$ (John Walker, 1994) showed that the three β subunits, identical in sequence, have three different conformations: one binds an ATP analog, one ADP, and one is empty. The asymmetric γ shaft contacts the three αβ pairs differently.

**Definition 23.3.2 (Binding-Change Mechanism)** In the **binding-change mechanism** (Boyer), the three catalytic sites of $\mathrm{F_1}$ are at any moment in three different conformations, β-ADP (loose, binding ADP and $\mathrm{P_i}$), β-ATP (tight, binding ATP so strongly that bound ADP + $\mathrm{P_i}$ and ATP interconvert) and β-empty (open, with very low affinity for ATP), and each site passes through the three conformations in turn; energy is used to change the conformations, which releases ATP and binds the substrates, not to form the phosphoanhydride bond.

**Definition 23.3.3 (Rotational Catalysis)** **Rotational catalysis** is the coupling, in ATP synthase, of the rotation of the c ring and the attached γε subunits, driven by protons passing through $\mathrm{F_o}$, to the binding changes in $\mathrm{F_1}$: each 120° rotation of γ converts the β-ATP site into β-empty, the β-ADP site into β-ATP and the β-empty site into β-ADP, so that one turn makes three ATP.

The three β subunits are coupled: when γ forces one into the β-empty conformation, its neighbors must adopt the other two. The model predicted that γ rotates in one direction during synthesis and in the other during hydrolysis. In 1997 Hiroyuki Noji, Ryohei Yasuda, Masasuke Yoshida and Kazuhiko Kinosita attached a fluorescent actin filament to γ of an immobilized $\alpha_3\beta_3\gamma$ and watched it rotate when ATP was added; at low ATP concentration the rotation proceeds in discrete 120° steps, one per ATP, with an efficiency of converting the free energy of ATP hydrolysis into mechanical work near 100%. With the whole $\mathrm{F_oF_1}$ the c ring rotates with γ. Boyer and Walker shared the Nobel Prize in Chemistry in 1997 (with Jens Skou, for the $\ce{Na+}/\ce{K+}$-ATPase). The enzyme has since been treated as a molecular motor, and its torque (about 40 pN nm) and stepping kinetics are analyzed in biophysics ([7.6.28](/7.6.28#sec-28.2)).

![Binding-change mechanism and rotational catalysis. A: F₁ viewed from the membrane, with three α (gray) and three β subunits (pink) around the γ shaft (green), whose protrusion faces the open β subunit. In each 120° step the loose site with ADP + Pᵢ closes into the tight site with ATP, the tight site opens and releases ATP, and the open site binds ADP + Pᵢ; one turn makes three ATP. B: simulated single-molecule rotation of F₁ hydrolyzing ATP at three low concentrations, as in the actin-filament experiments: γ turns in 120° steps separated by exponentially distributed dwells whose mean, 1/(k_on[ATP]), falls as [ATP] rises (k_on = 3 × 10⁷ M⁻¹ s⁻¹; random seed 0)](./plots/binding-change.py)

### 23.3.4. How Proton Flow Turns the c Ring

The rotation of $\mathrm{F_o}$ is driven by the protonation and deprotonation of the c-ring carboxylates at the interface with subunit a. A proton entering from the P side through one half-channel of subunit a protonates the carboxylate of the c subunit facing it; the now neutral carboxylate can move into the **lipid bilayer** as the ring turns. After almost a full turn, the subunit reaches the second half-channel, which opens to the N side, where the proton is released into the alkaline matrix; a conserved Arg of subunit a, between the two half-channels, attracts the deprotonated carboxylate and prevents protons from leaking directly across. Brownian rotation of the ring is thus rectified by the proton gradient into unidirectional rotation (a Brownian ratchet, [6.3.21](/6.3.21)). Each c subunit carries one proton per turn, so $n$ protons turn the ring once and make three ATP. In intact mitochondria the rotor turns about 100 times per second.

### 23.3.5. Stoichiometry: The P/O Ratio

**Definition 23.3.4 (P/O Ratio)** The **P/O ratio** is the number of ATP molecules formed from ADP and $\mathrm{P_i}$ per oxygen atom reduced to water (per pair of electrons transferred to $\tfrac12\ce{O2}$), for a given electron donor.

Because coupling goes through a proton gradient, there is no reason for the P/O ratio to be an integer. It depends on two numbers: the protons pumped per pair of electrons (10 from NADH, 6 from succinate, Eq. (23.4)) and the protons used per ATP. The latter is $n/3$ for the synthase (one turn, $n$ protons, three ATP) plus one for the transport of $\mathrm{P_i}$ into the matrix and the export of ATP (23.3.6):

**Formula 23.3.1 (P/O Ratio from the c Ring)**

$$
\frac{\mathrm{H^+}}{\mathrm{ATP}} = \frac{n}{3} + 1, \qquad \mathrm{P/O} = \frac{\mathrm{H^+\ pumped\ per\ 2\,\mathrm{e}^-}}{n/3 + 1}. \tag{23.6}
$$

**Example 23.3.1** Bovine mitochondria have $n = 8$: $8/3 + 1 = 3.7$ protons per ATP, so the P/O ratio is $10/3.7 = 2.7$ for NADH and $6/3.7 = 1.6$ for succinate. Yeast mitochondria, with $n = 10$, need $4.3$ protons per ATP and have P/O ratios of $2.3$ and $1.4$. The values 2.5 and 1.5 used in most textbooks, and in this course, correspond to 4 protons per ATP; they lie within the range of these estimates and of the measured ratios. In chloroplasts, with $n = 14$, $14/3 = 4.7$ protons pass through $\mathrm{F_o}$ for each ATP ([7.1.24](/7.1.24)).

The earlier integral values of 3 and 2 were based on the assumption of a chemical intermediate and on measurements that did not correct for proton leaks. The c-ring sizes found so far range from 8 (all animal mitochondria examined) to 17 (*Burkholderia pseudomallei*); a larger ring gives a lower ATP yield per proton but can make ATP against a smaller proton-motive force, a trade-off between yield and thermodynamic driving force.

### 23.3.6. Transport of ADP, ATP and Phosphate

ATP is made in the matrix but used mainly in the cytosol. Two transporters of the inner membrane, together consuming the equivalent of one proton per ATP, connect the two compartments.

- The adenine nucleotide translocase (ANT, ADP/ATP carrier) is an antiporter that exchanges cytosolic $\mathrm{ADP^{3-}}$ for matrix $\mathrm{ATP^{4-}}$. Each exchange moves one net negative charge outward, so it is driven by the membrane potential (matrix negative). The translocase, one of the most abundant proteins of the inner membrane, is inhibited by atractyloside (from a Mediterranean thistle) and bongkrekic acid.
- The phosphate carrier (PiC) catalyzes the electroneutral **symport** of $\mathrm{H_2PO_4^-}$ and $\ce{H+}$ into the matrix, driven by the pH gradient.

The synthase and the two carriers can be isolated as one complex, the ATP synthasome. ATP and ADP cross the outer membrane through VDAC. In muscle and brain, mitochondrial creatine kinase in the intermembrane space transfers the phosphoryl group of exported ATP to creatine, and **phosphocreatine** carries it to the sites of use (the phosphocreatine shuttle, [7.1.16](/7.1.16#sec-16.3.5)).

### 23.3.7. Shuttles for Cytosolic NADH

The NADH dehydrogenase of the inner membrane of animal mitochondria accepts electrons only from matrix NADH, and the membrane is impermeable to NADH; the NADH formed by glycolysis is reoxidized by shuttles that carry its reducing equivalents into the matrix.

**Definition 23.3.5 (Malate–Aspartate Shuttle)** In the **malate–aspartate shuttle** of liver, kidney and heart, cytosolic malate dehydrogenase reduces oxaloacetate with NADH; the malate enters the matrix in exchange for α-ketoglutarate (malate–α-ketoglutarate antiporter) and is reoxidized by matrix malate dehydrogenase, forming NADH; the oxaloacetate is transaminated to aspartate, which leaves the matrix in exchange for glutamate (glutamate–aspartate antiporter) and is transaminated back to oxaloacetate in the cytosol.

**Definition 23.3.6 (Glycerol 3-Phosphate Shuttle)** In the **glycerol 3-phosphate shuttle** of skeletal muscle and brain, cytosolic glycerol 3-phosphate dehydrogenase reduces dihydroxyacetone phosphate with NADH, and a flavoprotein isozyme on the outer face of the inner membrane reoxidizes glycerol 3-phosphate, passing the electrons through its FAD to ubiquinone.

![The two shuttles for cytosolic NADH. A: malate–aspartate shuttle. Cytosolic malate dehydrogenase (MDH) reduces oxaloacetate with NADH; malate enters the matrix in exchange for α-ketoglutarate and is reoxidized by matrix MDH, giving NADH for Complex I; oxaloacetate is transaminated by aspartate aminotransferase (AAT) to aspartate, which leaves in exchange for glutamate and is transaminated back to oxaloacetate in the cytosol. All steps are reversible, and the shuttle runs inward only while cytosolic NADH/NAD⁺ is higher than in the matrix, which the glutamate–aspartate antiporter, driven by the membrane potential, ensures. B: glycerol 3-phosphate shuttle. Cytosolic glycerol 3-phosphate dehydrogenase (G3PDH) reduces dihydroxyacetone phosphate (DHAP); the mitochondrial isozyme on the outer face of the inner membrane passes the electrons through FAD to ubiquinone, bypassing Complex I, so that each cytosolic NADH yields about one ATP less](./plots/nadh-shuttles.py)

The malate–aspartate shuttle is reversible, but the glutamate–aspartate antiporter, which imports a proton with glutamate and is therefore **electrogenic**, makes it run inward against a more reduced matrix NAD pool; it delivers cytosolic NADH to Complex I, about 2.5 ATP per NADH. The glycerol 3-phosphate shuttle is irreversible and works even when the matrix is highly reduced, but its electrons enter at ubiquinone and yield about 1.5 ATP. Plant mitochondria have an external NADH dehydrogenase that transfers electrons from cytosolic NADH directly to ubiquinone (23.6). The choice of shuttle explains the two totals of the energy account of glucose:

| Process | Direct product | ATP |
|---|---|---|
| glycolysis | 2 NADH (cytosolic) | 3 or 5 |
| | 2 ATP | 2 |
| pyruvate oxidation (two per glucose) | 2 NADH (matrix) | 5 |
| citric acid cycle (two turns) | 6 NADH (matrix) | 15 |
| | 2 $\ce{FADH2}$ | 3 |
| | 2 ATP or GTP | 2 |
| total per glucose | | 30 or 32 |

(Lehninger 8e, Table 19-5, with P/O = 2.5 and 1.5. The first total applies with the glycerol 3-phosphate shuttle, the second with the malate–aspartate shuttle.) With $\Delta_{\mathrm{r}}G'^{\circ} = -2840\,\mathrm{kJ\,mol^{-1}}$ for the oxidation of glucose and about $50\,\mathrm{kJ\,mol^{-1}}$ for making ATP in a cell, 32 ATP conserve some 56% of the free energy.

The same ledger can be followed in free energy. The 10 NADH and 2 FADH₂ of one glucose would release about 2495 kJ if their electrons went straight to $\ce{O2}$ (Example 16.4.2; 151 kJ for each succinate), and substrate-level phosphorylation has already made 4 ATP; the reactions of glycolysis and the cycle release the remaining 145 kJ as heat. The chain pumps $10 \times 10 + 2 \times 6 = 112$ protons, which at about 19 kJ each (Example 23.2.1) store 2128 kJ; ATP synthase and the carriers then turn the gradient into 28 ATP. Each conversion is incomplete, and the losses appear as heat: these are the calories that keep a mammal warm. Because the stoichiometry is not an integer, the total depends on how many protons an ATP costs: with the bovine c₈ ring (3.7 per ATP) and no proton leak, the yield would be 34 ATP and the efficiency 61%; in intact cells the leak, about a fifth of resting respiration (Rolfe and Brown, 1997), brings the realized yield down to about 30.

![Where the free energy of one glucose goes in aerobic respiration (malate–aspartate shuttle; ATP worth 50 kJ/mol in the cell). A: of the 2840 kJ/mol released by complete oxidation, 145 kJ is lost as heat in glycolysis, pyruvate oxidation and the citric acid cycle, whose electrons end up in 10 NADH and 2 FADH₂ (2495 kJ) beside 4 ATP from substrate-level phosphorylation; the respiratory chain pumps 112 protons, storing 2128 kJ (367 kJ heat); ATP synthase converts the gradient into 28 ATP (728 kJ heat), so 32 ATP, 1600 kJ or 56 %, are kept. B: ATP per glucose and efficiency against the protons used per ATP (n/3 + 1) for the two shuttles; bovine c₈ ring 3.7, textbook value 4, yeast c₁₀ ring 4.3](./plots/glucose-energy-budget.py)

## 23.4. Regulation of Oxidative Phosphorylation

### 23.4.1. Acceptor Control and the Mass-Action Ratio

The rate of respiration in most tissues is set by the availability of ADP, as in the oxygen-electrode experiment (Definition 23.2.2); in some tissues the respiratory control ratio is 10 or more. In the language of [7.1.17](/7.1.17#sec-17.4.4), oxidative phosphorylation is the supply block of a supply–demand system whose linking intermediate is the ATP/ADP couple. When work (contraction, protein synthesis, ion pumping) consumes ATP, the **mass-action ratio** $[\mathrm{ATP}]/([\mathrm{ADP}][\mathrm{P_i}])$ falls slightly, ADP and $\mathrm{P_i}$ enter the matrix, the synthase lets protons in, the proton-motive force falls a little, and the respiratory chain, now less opposed by the gradient, transfers electrons faster, until the ratio is restored. Because the response is so sensitive, the ratio varies little even with large changes in demand: ATP is made only as fast as it is used. **Metabolic control analysis** shows that control of the flux of respiration is shared among the substrate supply, the respiratory chain, the synthase, the carriers and the proton leak, rather than held by one step.

### 23.4.2. IF1 Prevents ATP Hydrolysis during Hypoxia

When $\ce{O2}$ is lacking (a heart attack, a stroke), electron transfer stops and the proton-motive force collapses; ATP synthase would then run in reverse, hydrolyzing ATP made by glycolysis to pump protons out. A small protein, IF1 (84 residues, intrinsically disordered on its own), prevents this. It is active as a dimer, which forms below about pH 6.5, as the cell acidifies with lactic acid; each dimer binds two $\mathrm{F_1}$ at their αβ interfaces and blocks them. When aerobic **metabolism** resumes and the pH rises, the dimer dissociates. Many tumors express IF1 at high levels.

### 23.4.3. Hypoxia and HIF-1

In hypoxic cells the input of electrons exceeds their transfer to $\ce{O2}$, and ROS production rises. The **transcription** factor HIF-1 (hypoxia-inducible factor), whose α subunit is hydroxylated on two Pro residues by $\ce{O2}$-dependent prolyl hydroxylases and degraded when $\ce{O2}$ is abundant, accumulates in hypoxia and induces glucose transporters and glycolytic enzymes (the program behind the **Warburg effect**, [7.1.18](/7.1.18#sec-18.4.4)), lactate dehydrogenase, PDH kinase, which phosphorylates and inactivates the pyruvate dehydrogenase complex and so limits the supply of NADH and $\ce{FADH2}$ to the chain, and the subunit COX4-2 of Complex IV, which replaces COX4-1 (degraded by a protease that HIF-1 also induces) and makes the oxidase work better at low $\ce{O2}$. The discovery of this oxygen-sensing pathway earned William Kaelin, Peter Ratcliffe and Gregg Semenza the Nobel Prize in Physiology or Medicine in 2019.

### 23.4.4. Coordinated Regulation of the ATP-Producing Pathways

Glycolysis, pyruvate oxidation, the citric acid cycle and oxidative phosphorylation are regulated together by the adenine nucleotides and NADH. High [ATP] (low [ADP] and [AMP]) slows all four: ATP inhibits PFK-1 and pyruvate kinase ([7.1.18](/7.1.18#sec-18.5)) and the pyruvate dehydrogenase complex; NADH and acetyl-CoA inhibit pyruvate dehydrogenase; a high [NADH]/[$\ce{NAD+}$] ratio slows the dehydrogenases of the citric acid cycle ([7.1.20](/7.1.20)); citrate, exported from mitochondria when the cycle idles, inhibits PFK-1 together with ATP more than either alone. When ATP is consumed, the rise of ADP, AMP and $\mathrm{P_i}$ accelerates all of them at once, so that the supply of pyruvate, acetyl-CoA and reduced carriers follows the demand of the respiratory chain. In the longer term, the number of mitochondria and the amount of each complex are adjusted by transcription (PGC-1α in exercise and cold, HIF-1 in hypoxia, [7.1.29](/7.1.29)).

## 23.5. Mitochondria beyond ATP Synthesis

### 23.5.1. Thermogenesis in Brown Adipose Tissue

Respiration slows when ATP is plentiful, with one instructive exception.

**Definition 23.5.1 (Brown Adipose Tissue and Thermogenin)** **Brown adipose tissue** (BAT) is a thermogenic adipose tissue of newborn and hibernating mammals and of cold-adapted adults, whose cells are rich in mitochondria (and hence in cytochromes, which give the brown colour) containing **thermogenin**, uncoupling protein 1 (UCP1), a carrier of the inner membrane that lets protons return to the matrix without passing through ATP synthase, so that the energy of fuel oxidation is released as heat.

UCP1 belongs to the mitochondrial carrier family, like the adenine nucleotide translocase. It is activated by long-chain **fatty acids**, which it is thought to transport as anions, the fatty acids flipping back in their protonated form (or which it binds as **cofactors** of proton transport), and inhibited by purine nucleotides (GDP, ATP). In the cold, norepinephrine from sympathetic nerves acts on β₃-adrenergic **receptors** of brown adipocytes, **cAMP** and **PKA** activate lipolysis ([7.1.14](/7.1.14), [7.1.21](/7.1.21)), and the released fatty acids both activate UCP1 and serve as fuel. Adults retain active brown fat in the neck and around the great vessels, and "beige" adipocytes with UCP1 appear in white fat after prolonged cold; their capacity to dissipate energy is studied in relation to obesity ([7.1.29](/7.1.29)). Heat is also made without UCP1, for example by a **futile cycle** in which mitochondrial creatine kinase phosphorylates creatine with exported ATP and the phosphocreatine is hydrolyzed (a **substrate cycle**, [7.1.17](/7.1.17#sec-17.3.4)); thermogenic plants use a different route (23.6).

### 23.5.2. Steroid Hydroxylation by Cytochrome P-450

Mitochondria of the adrenal cortex, gonads and placenta are the site of several hydroxylations of steroid synthesis, including the cleavage of the **cholesterol** **side chain** to pregnenolone, the first step of all **steroid hormones** ([7.1.26](/7.1.26)), and the 1α-hydroxylation of **vitamin** D in the kidney. These are catalyzed by **cytochrome P-450** monooxygenases of the inner membrane, named for the 450 nm absorption band of their CO complex, which incorporate one atom of $\ce{O2}$ into the substrate and reduce the other to water: $\ce{R-H} + \ce{O2} + \mathrm{NADPH} + \ce{H+} \to \ce{R-OH} + \ce{H2O} + \ce{NADP+}$. Electrons travel from NADPH to the flavoprotein adrenodoxin reductase, then one at a time through the [2Fe–2S] protein adrenodoxin to the P-450 heme. The much larger family of P-450 enzymes of the endoplasmic reticulum, which hydroxylate drugs and other xenobiotics, receives its electrons from a different reductase.

### 23.5.3. Mitochondria in Apoptosis

Mitochondria are central to the intrinsic pathway of **apoptosis** ([7.1.15](/7.1.15#sec-15.6.3)). Stress signals (DNA damage, growth-factor withdrawal, ROS) activate the pro-apoptotic Bcl-2 family proteins Bax and Bak, which oligomerize in the outer membrane and permeabilize it (mitochondrial outer membrane permeabilization); cytochrome c is released from the intermembrane space into the cytosol. There it binds Apaf-1, which assembles into the heptameric apoptosome that activates procaspase-9; caspase-9 starts the cascade of executioner **caspases**. Anti-apoptotic members of the family (Bcl-2, Bcl-xL) bind and restrain Bax and Bak. (Older accounts attributed the release mainly to a permeability transition pore of the inner membrane, which participates in necrotic rather than apoptotic death.) Cytochrome c thus has two unrelated functions, a case of moonlighting.

### 23.5.4. The Mitochondrial Genome and Its Diseases

Human mitochondrial DNA is a circular duplex of 16 569 bp, present in several copies per mitochondrion and hundreds to thousands per cell. Its 37 **genes** encode 13 subunits of the respiratory chain and ATP synthase, 2 rRNAs and 22 **tRNAs**; mitochondria have their own ribosomes and a slightly different **genetic code** (7.2). The other proteins of the organelle, about 1200, are encoded in the nucleus and imported.

| Complex | Subunits | Encoded by mtDNA |
|---|---|---|
| I | 45 | 7 (ND1–ND6, ND4L) |
| II | 4 | 0 |
| III | 11 | 1 (cytochrome b) |
| IV | 13 | 3 (COI–COIII) |
| V (ATP synthase) | 17 kinds (28 **polypeptides** with a c₈ ring) | 2 (ATP6, ATP8) |

(Subunit numbers from Lehninger 8e, Table 19-6, except Complex V, whose count is from recent structures.) Complex II, encoded entirely by nuclear genes, is the only complex not affected by mtDNA mutations, which is why patients with Complex I defects can still oxidize succinate.

Mitochondria are inherited from the mother: the egg contains $10^{5}$–$10^{6}$ mitochondria, the sperm about a hundred, which are destroyed after fertilization. Mitochondrial DNA is exposed to ROS and less well repaired than nuclear DNA, so mutations accumulate during life (one theory of aging). Because a cell contains many genomes, a mutant can coexist with the wild type.

**Definition 23.5.2 (Heteroplasmy)** **Heteroplasmy** is the presence of more than one mitochondrial genotype in a cell, tissue or individual; homoplasmy, the presence of only one.

The fraction of mutant genomes drifts during cell divisions, which partition mitochondria at random, and varies among tissues and among siblings; a biochemical defect appears when the mutant fraction exceeds a threshold, and tissues that depend most on oxidative phosphorylation (neurons, skeletal and heart muscle, pancreatic β cells) are affected first. The transmission and the population genetics of heteroplasmy are treated in 7.4.

- Leber hereditary optic neuropathy (LHON): a point mutation in ND4 (Arg340 to His) or in other Complex I or cytochrome b genes, usually homoplasmic, causes loss of central vision in young adults, mostly men.
- Myoclonic epilepsy with ragged-red fibers (MERRF): a mutation in the $\mathrm{tRNA^{Lys}}$ gene (m.8344A>G) impairs the synthesis of all mtDNA-encoded proteins; muscle fibers accumulate abnormal mitochondria with paracrystalline inclusions.
- A mutation in $\mathrm{tRNA^{Leu}}$ (m.3243A>G) causes MELAS (mitochondrial encephalomyopathy, lactic **acidosis** and stroke-like episodes) or, at lower heteroplasmy, maternally inherited **diabetes** and deafness (MIDD): β cells cannot raise [ATP] enough to close their ATP-sensitive $\ce{K+}$ channels and secrete **insulin** ([7.1.29](/7.1.29)).
- Mutations in ATP6 affect the proton pore of ATP synthase (NARP and Leigh syndrome).

Mitochondrial replacement ("three-parent") techniques transfer the nuclear genome of an affected mother into an enucleated donor egg with healthy mitochondria; they have been permitted in the United Kingdom since 2015, and the first children were born. Mutations in any of the nuclear genes for mitochondrial proteins or their assembly factors also cause mitochondrial disease, with Mendelian inheritance.

## 23.6. Alternative Respiratory Pathways

Plant mitochondria have the standard chain and, in addition, routes that bypass its proton pumps. A rotenone-insensitive internal NADH dehydrogenase passes electrons from matrix NADH to ubiquinone without pumping; external NADH dehydrogenases oxidize cytosolic NAD(P)H at the outer face of the inner membrane; and the alternative oxidase, a diiron protein, transfers electrons from ubiquinol directly to $\ce{O2}$, bypassing Complexes III and IV, and is insensitive to cyanide and antimycin. Electrons that take these routes conserve little energy, which is released as heat. Arum lilies and the eastern skunk cabbage (*Symplocarpus foetidus*) use this to heat their spadix by up to 20–40 °C above ambient temperature, which volatilizes odors of carrion or dung that attract pollinating flies and beetles, and lets the skunk cabbage melt through snow. More generally, the alternative oxidase protects plants from overreduction of the ubiquinone pool and ROS production when the chain is saturated, for example in strong light, when the chloroplasts export reducing equivalents.

Bacteria carry their respiratory chain in the plasma membrane and pump protons out of the cell; $\mathrm{F_1}$ faces the cytosol. Their chains are modular and branched: *E. coli* has a proton-pumping NADH dehydrogenase homologous to Complex I and a nonpumping one, several dehydrogenases feeding ubiquinone or menaquinone, and two terminal quinol oxidases with different affinities for $\ce{O2}$ (cytochrome $bo_3$, which pumps protons, for high $\ce{O2}$, and cytochrome bd, which does not, for low $\ce{O2}$), and under anaerobic conditions it uses nitrate, fumarate or other acceptors. The proton-motive force of bacteria also drives the uptake of nutrients by symport (lactose permease, [7.1.13](/7.1.13#sec-13.5.5)) and the rotation of the flagella, whose motor is a "proton turbine" turned directly by the flow of protons rather than by ATP. That bacterial respiratory chains resemble the mitochondrial one supports the endosymbiotic origin of mitochondria from α-proteobacteria, and suggests that chemiosmotic coupling arose before the eukaryotic cell.

## Summary

The pathway card of oxidative phosphorylation ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Oxidative phosphorylation |
|---|---|
| Location | inner mitochondrial membrane (cristae) of eukaryotes; plasma membrane of aerobic bacteria |
| Net reaction | NADH + $\ce{H+}$ + ½ $\ce{O2}$ + ~2.5 ADP + ~2.5 $\mathrm{P_i}$ → $\ce{NAD+}$ + ~2.5 ATP + $\ce{H2O}$; per $\ce{FADH2}$ (via Q) ~1.5 ATP |
| Energy account | NADH → $\ce{O2}$: $\Delta E'^{\circ} = 1.136\,\mathrm{V}$, $\Delta_{\mathrm{r}}G'^{\circ} = -219\,\mathrm{kJ\,mol^{-1}}$; 10 $\ce{H+}$ pumped (4 + 4 + 2, Eq. (23.4)), $\Delta\tilde\mu_{\mathrm{H^+}} \approx 19\,\mathrm{kJ\,mol^{-1}}$ (Example 23.2.1); $n/3 + 1$ $\ce{H+}$ per ATP (Formula 23.3.1); 30–32 ATP per glucose |
| Committed and regulated steps | Complex IV (far from equilibrium); Complex I and ATP synthase near equilibrium; flux control shared |
| Activators | ADP and $\mathrm{P_i}$ (acceptor control, Definition 23.2.2); $\ce{Ca^2+}$ activates matrix dehydrogenases |
| Inhibitors | high [ATP]/([ADP][$\mathrm{P_i}$]), high proton-motive force; IF1 in hypoxia (blocks reverse ATP hydrolysis); drugs and poisons in 23.2.4 |
| Covalent, hormonal and transcriptional control | HIF-1 (PDH kinase, COX4-2) in hypoxia; PGC-1α (mitochondrial biogenesis); norepinephrine → UCP1 in brown fat |
| Opposing pathway | none in mitochondria; ATP synthase runs backward as a proton pump when the gradient collapses (prevented by IF1); photophosphorylation uses the same synthase ([7.1.24](/7.1.24)) |
| **Coenzymes** (vitamins) | NAD (niacin), FMN and FAD (riboflavin), ubiquinone (synthesized), hemes, Fe–S, Cu |
| Diseases and drugs | LHON, MERRF, MELAS/MIDD, Leigh syndrome, heteroplasmy; paraganglioma (Complex II); cyanide, CO, rotenone, antimycin; DNP; atractyloside |

| Topic | Key points |
|---|---|
| Carriers (Definitions 23.1.1–23.1.4) | NAD, flavoproteins, ubiquinone (mobile, 1 or 2 e⁻ + H⁺), cytochromes a, b, c (one e⁻, 600/560/550 nm), Fe–S, Cu; order from E′°, oxidation kinetics, inhibitors, isolated complexes |
| Complexes (Definition 23.1.5) | I: NADH → Q, FMN + Fe–S chain, 4 H⁺ by long-range coupling, reversible; II: succinate → Q, no pumping; III: Q cycle (Definition 23.1.6), 4 H⁺ out, 2 in; IV: cyt c → O₂, 2 pumped + 2 substrate H⁺ per pair |
| Organization (Definition 23.1.7) | respirasomes I₁III₂IV₁; Q and cyt c pools; ROS (Definition 23.1.8) from Complexes I and III, SOD, peroxidases, NADPH |
| Chemiosmotic coupling (Definitions 23.2.1–23.2.5) | obligate coupling, acceptor control; Δμ̃(H⁺) = FΔφ + 2.303RTΔpH (Eq. (23.5)); evidence: closed vesicles, proton ejection, uncouplers, artificial gradients |
| ATP synthase (Definitions 23.3.1–23.3.3) | F₁ α₃β₃γδε + Fₒ ab₂cₙ; ΔG′° ≈ 0 on the enzyme, energy used for ATP release; β-ADP → β-ATP → β-empty per 120°; c-ring protonation at subunit a, Brownian ratchet |
| Stoichiometry (Definition 23.3.4, Formula 23.3.1) | P/O = 10/(n/3 + 1) for NADH; 2.7 (n = 8) to 2.3 (n = 10), textbook 2.5; succinate 1.5 |
| Transport and shuttles (Definitions 23.3.5, 23.3.6) | ANT (electrogenic ATP⁴⁻/ADP³⁻), PiC (H⁺ symport); malate–aspartate (2.5 ATP) vs glycerol 3-phosphate (1.5 ATP) |
| Regulation (23.4) | ADP availability; **mass-action ratio** nearly constant; IF1; HIF-1; concerted control of glycolysis, PDH, cycle |
| Other roles (23.5, 23.6) | UCP1 thermogenesis (Definition 23.5.1); P-450 steroid hydroxylation; cytochrome c in **apoptosis**; mtDNA: 13 proteins, maternal inheritance, heteroplasmy (Definition 23.5.2); alternative oxidase; bacterial chains |

## Questions

1. Predict the redox state (mostly reduced or mostly oxidized) of NADH, ubiquinone, cytochrome c and cytochrome $a_3$ in respiring mitochondria with abundant substrate and $\ce{O2}$ after the addition of (a) rotenone, (b) antimycin A, (c) cyanide.

   **Answer** Carriers before the block become reduced, those after it oxidized. (a) Rotenone blocks Complex I between N2 and Q: NADH reduced; Q, cytochrome c and $a_3$ oxidized. (b) Antimycin A blocks the $\mathrm{Q_N}$ site of Complex III: NADH and Q (and heme $b_{\mathrm{H}}$) reduced; cytochrome c and $a_3$ oxidized (the Q cycle is blocked, and the $\mathrm{Q_P}$ site cannot turn over without the b-heme path). (c) Cyanide blocks heme $a_3$: all carriers, including cytochrome c and $a_3$, reduced. Rotenone-treated mitochondria still respire on succinate, which enters at Q; with antimycin or cyanide no substrate supports respiration (except artificial donors to cytochrome c after antimycin).

2. Calculate the proton-motive force (in $\mathrm{kJ\,mol^{-1}}$ and in volts) of mitochondria with $\Delta\varphi = 0.18\,\mathrm{V}$ and $\Delta\mathrm{pH} = 0.5$ at $37\,^\circ\mathrm{C}$. What is the minimal number of protons needed to make one ATP if the phosphorylation potential is $+55\,\mathrm{kJ\,mol^{-1}}$? Compare with the bovine c ring.

   **Answer** $\Delta\tilde\mu_{\mathrm{H^+}} = 96.5 \times 0.18 + 5.94 \times 0.5 = 17.4 + 3.0 = 20.3\,\mathrm{kJ\,mol^{-1}}$, $\Delta p = 0.21\,\mathrm{V}$. At least $55/20.3 = 2.7$ protons must pass the synthase per ATP. The bovine ring uses $8/3 = 2.67$ through $\mathrm{F_o}$, plus one for transport, $3.67$ in total; the energy supplied, $3.67 \times 20.3 = 74\,\mathrm{kJ}$, exceeds the $55\,\mathrm{kJ}$ stored in ATP by about a third, the driving force that keeps the overall process running forward. The synthase itself, with $2.67 \times 20.3 = 54\,\mathrm{kJ}$, works close to equilibrium.

3. Isolated mitochondria oxidizing succinate in the presence of rotenone consume 40 nmol of $\ce{O2}$ while phosphorylating an added pulse of 120 nmol ADP. (a) What is the ADP/O ratio? (b) What value would you expect with glutamate and malate? (c) Why is rotenone added with succinate?

   **Answer** (a) 40 nmol $\ce{O2}$ = 80 nmol O atoms; ADP/O = 120/80 = 1.5. (b) About 2.5 (NADH-linked substrates send electrons through Complex I, which adds four protons per pair: 10 instead of 6). (c) Succinate oxidation produces fumarate and malate, which malate dehydrogenase would convert to oxaloacetate with formation of NADH; rotenone prevents the oxidation of this NADH through Complex I, so that all electrons enter at Complex II and the measured ratio belongs to succinate alone (it also prevents reverse electron transport).

4. Valinomycin added to respiring mitochondria in a $\ce{K+}$-containing medium decreases ATP synthesis, increases $\ce{O2}$ consumption and increases the pH gradient across the inner membrane. Explain each effect. Is valinomycin an inhibitor or an uncoupler?

   **Answer** Valinomycin carries $\ce{K+}$ across the membrane; $\ce{K+}$ enters the matrix down the membrane potential, which collapses $\Delta\varphi$, the larger component of the proton-motive force. Respiration, no longer opposed by the gradient, accelerates; with $\Delta\varphi$ gone, the pumps move protons outward without a counterbalancing field, and $\Delta\mathrm{pH}$ rises, but not enough to restore the total proton-motive force, so ATP synthesis falls. Free energy of electron transfer is dissipated as heat: valinomycin is an uncoupler (it does not block any carrier).

5. (Open question) Design an experiment, using isolated brown-fat mitochondria and the oxygen electrode, that distinguishes the regulation of UCP1 by fatty acids and by purine nucleotides, and predict the results.

   **Answer** Outline: incubate mitochondria (in the presence of albumin to remove endogenous fatty acids) with a respiratory substrate and oligomycin, so that respiration measures proton leak only. Add a long-chain fatty acid such as palmitate: respiration should rise severalfold (UCP1 activated), and the membrane potential, measured with a potentiometric dye or a TPP⁺ electrode, should fall. Add GDP: respiration should fall back to the low basal leak and the potential recover; adding more fatty acid should overcome the GDP inhibition partially, as expected for competing regulators. Controls: white-fat or liver mitochondria (no UCP1), or mitochondria from UCP1-knockout mice, should show no fatty-acid-stimulated, GDP-sensitive leak; an uncoupler (FCCP) at the end gives the maximal respiratory capacity. A patient whose UCP1 is not inhibited by nucleotides would have permanently uncoupled brown fat, with increased heat production and energy expenditure.

6. Why do mammals with an 8-subunit c ring obtain more ATP per NADH than yeast with a 10-subunit ring? Is a small c ring always advantageous?

   **Answer** One turn of the ring makes three ATP and costs $n$ protons; a smaller ring makes each ATP cheaper ($n/3$ protons), so the same ten protons pumped per NADH make $10/3.7 = 2.7$ ATP with $n = 8$ and $10/4.3 = 2.3$ with $n = 10$ (Formula 23.3.1). The price is thermodynamic: fewer protons per ATP means that each proton must supply more free energy, $\Delta G_{\mathrm{p}}/(n/3)$, so a small ring needs a large proton-motive force. Organisms that live with a small gradient (chloroplasts, whose pmf is mostly a pH difference that the lumen cannot increase without damage, or alkaliphilic bacteria such as *Bacillus* TA2.A1 with $n = 13$) use larger rings, trading yield for the ability to make ATP at all.
