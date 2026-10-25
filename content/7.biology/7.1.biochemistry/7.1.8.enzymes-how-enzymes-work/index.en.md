---
title: "Enzymes I: How Enzymes Work"
description: What enzymes are and how they are named; cofactors and holoenzymes; rates versus equilibria and the size of enzymatic rate enhancements; binding energy and complementarity to the transition state; entropy reduction, desolvation and induced fit; general acid–base, covalent and metal ion catalysis; chymotrypsin, HIV protease, hexokinase, enolase and penicillin as case studies; pre-steady-state bursts and the pH dependence of activity.
---

Almost every reaction in a cell is catalyzed by an enzyme, and almost every enzyme is a protein. This chapter asks how a protein can accelerate a reaction by factors of $10^5$ to $10^{17}$ while choosing one substrate among many similar molecules. The answer continues the main line of Part I, from chemical properties to structure to function. The same weak interactions that fold a protein ([7.1.2](/7.1.2), [7.1.5](/7.1.5)) and let it bind a ligand ([7.1.7](/7.1.7)) are used by an enzyme to bind its substrate, and above all its transition state. The acidic, basic and nucleophilic side chains catalogued in [7.1.3](/7.1.3#sec-3.2.2) then carry out the chemistry, which is ordinary organic chemistry ([6.5.33](/6.5.33#sec-33.8.3)) done by precisely positioned groups. The physical chemistry of rates and catalysis is taken from [6.3.16](/6.3.16) and [6.3.17](/6.3.17) and not derived again. The quantitative description of enzyme activity (kinetics, inhibition) and its regulation follow in [7.1.9](/7.1.9); every metabolic pathway of Part II ([7.1.16](/7.1.16) onward) is a sequence of the enzymes described here.

## 8.1. An Introduction to Enzymes

### 8.1.1. Enzymes Are Biological Catalysts

Biological catalysis was first recognized in the late eighteenth century in the digestion of meat by stomach secretions. Biochemistry as a science can be dated to 1897, when Eduard Buchner showed that a cell-free yeast extract ferments sugar to alcohol: fermentation needs molecules, not living cells, which ended the vitalism of Pasteur. Frederick Kühne had already named such molecules enzymes (Greek *enzymos*, "leavened"). In 1926 James Sumner crystallized urease and showed that the crystals were protein; work by John Northrop and Moses Kunitz on pepsin and trypsin made the protein nature of enzymes generally accepted by the early 1930s. In the early 1980s Thomas Cech and Sidney Altman found RNA molecules that catalyze reactions, and the peptidyl transferase center of the ribosome turned out to be RNA ([7.2](/7.2)).

**Definition 8.1.1 (Enzyme)** An **enzyme** is a biological macromolecule that catalyzes a chemical reaction. Almost all enzymes are globular proteins; a catalytic RNA is called a **ribozyme**.

An enzyme is a **catalyst** in the sense of [6.1.7](/6.1.7#sec-7.3.4): it is not consumed, and it changes the rate but not the position of equilibrium. Compared with chemical catalysts, enzymes have four distinctive features:

- higher rates: accelerations of $10^5$ to $10^{17}$ (8.2.3);
- greater specificity, for the reaction and for the reactants (the substrates), with almost no side products;
- mild conditions: neutral pH, about $37\,^\circ\mathrm{C}$, aqueous solution;
- capacity for regulation by the concentrations of other molecules, covalent modification and the amount of enzyme ([7.1.9](/7.1.9)).

Catalytic activity depends on the native conformation: denaturation or dissociation into subunits usually abolishes it. Enzymes range in relative molecular mass from about 12 000 to more than $10^6$.

### 8.1.2. Cofactors, Coenzymes and Holoenzymes

Some enzymes need nothing but their amino acid residues. Others require a **cofactor**: one or more inorganic ions, or a **coenzyme**, an organic or metallo-organic molecule; a cofactor bound very tightly or covalently is a **prosthetic group**. These terms were defined for proteins in general in [7.1.3](/7.1.3#sec-3.5.4).

**Definition 8.1.2 (Holoenzyme and Apoenzyme)** The complete, catalytically active enzyme together with its bound coenzyme and metal ions is the **holoenzyme**; its protein part alone is the **apoenzyme** (apoprotein).

Coenzymes act as transient carriers of specific atoms or functional groups, and most are derived from vitamins. The table lists the examples of this chapter; the complete coenzyme–vitamin table, with mechanisms, is in [7.1.17](/7.1.17).

| Metal ion | Enzymes | Coenzyme | Group carried | Vitamin precursor |
|---|---|---|---|---|
| $\ce{Mg^2+}$ | hexokinase, enolase, pyruvate kinase | NAD, NADP | hydride ion ($\ce{H-}$) | niacin ($\mathrm{B_3}$) |
| $\ce{Zn^2+}$ | carbonic anhydrase, alcohol dehydrogenase, carboxypeptidases A and B | FAD | electrons | riboflavin ($\mathrm{B_2}$) |
| $\ce{F\mathrm{e}^2+}$ / $\ce{F\mathrm{e}^3+}$ | cytochrome oxidase, catalase, peroxidase | coenzyme A | acyl groups | pantothenate ($\mathrm{B_5}$) |
| $\ce{Cu^2+}$ | cytochrome oxidase | pyridoxal phosphate | amino groups | pyridoxine ($\mathrm{B_6}$) |
| $\ce{Mn^2+}$ | arginase, ribonucleotide reductase | thiamine pyrophosphate | aldehydes | thiamine ($\mathrm{B_1}$) |
| $\ce{K+}$ | pyruvate kinase | biocytin | $\ce{CO2}$ | biotin ($\mathrm{B_7}$) |
| $\ce{Ni^2+}$ | urease | tetrahydrofolate | one-carbon groups | folate ($\mathrm{B_9}$) |
| Mo | dinitrogenase | coenzyme $\mathrm{B_{12}}$ | H atoms, alkyl groups | cobalamin ($\mathrm{B_{12}}$) |

Lipoate (electrons and acyl groups) is a coenzyme that animals make themselves. Some enzymes are further modified covalently (phosphorylation, glycosylation and others), mostly for regulation ([7.1.9](/7.1.9)).

### 8.1.3. Classification and Nomenclature

Many enzymes are named by adding "-ase" to the substrate or the activity (urease, DNA polymerase); others have historical names (pepsin, lysozyme, trypsin). To remove ambiguity the Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (IUBMB) classifies enzymes by the reaction catalyzed.

**Definition 8.1.3 (EC Number)** Each enzyme is assigned a four-part **EC number** (Enzyme Commission number) and a systematic name that identifies the reaction it catalyzes: class, subclass, sub-subclass and serial number.

| Class | Name | Type of reaction |
|---|---|---|
| 1 | Oxidoreductases | transfer of electrons (hydride ions or H atoms) |
| 2 | Transferases | group transfer |
| 3 | Hydrolases | hydrolysis (transfer of a group to water) |
| 4 | Lyases | cleavage of C–C, C–O, C–N and other bonds by elimination, leaving double bonds or rings, or addition to double bonds |
| 5 | Isomerases | transfer of groups within a molecule to give an isomer |
| 6 | Ligases | formation of C–C, C–S, C–O and C–N bonds by condensations coupled to cleavage of ATP or a similar cofactor |
| 7 | Translocases | movement of ions or molecules across membranes or their separation within membranes (added in 2018) |

**Example 8.1.1** The enzyme catalyzing ATP + D-glucose → ADP + D-glucose 6-phosphate has the systematic name ATP:D-hexose 6-phosphotransferase and the EC number 2.7.1.1: class 2 (transferase), subclass 7 (phosphotransferase), sub-subclass 1 (a hydroxyl group is the acceptor), serial number 1 (D-glucose is the acceptor). Its trivial name is hexokinase.

## 8.2. Rates and Equilibria

### 8.2.1. The Active Site and the Enzyme–Substrate Complex

**Definition 8.2.1 (Active Site and Substrate)** The pocket of an enzyme in which the catalyzed reaction takes place is the **active site**; the molecule bound there and acted upon is the **substrate**. The residues of the active site that take part directly in the chemical transformation are the catalytic groups.

The enzyme–substrate complex ES is the starting point of both the kinetics and the mechanism of an enzyme. Its existence is shown by saturation (at high substrate concentration the rate reaches a maximum because all active sites are filled; [7.1.9](/7.1.9)), by crystal structures of enzyme–substrate complexes (for example cytochrome P-450 with camphor), and by spectroscopic changes on binding (the fluorescence of the pyridoxal phosphate of tryptophan synthase changes when serine and indole bind).

Active sites share a few structural features:

1. they are three-dimensional clefts formed by groups from different parts of the sequence (in lysozyme, residues 35, 52, 62, 63 and 101 line the site);
2. they occupy a small part of the enzyme; most of the chain is a scaffold that holds the catalytic groups in place;
3. they are clefts, often lined by nonpolar residues, from which water can be excluded;
4. substrates are bound by multiple weak interactions (**hydrogen bonds**, ionic interactions, the **hydrophobic effect**);
5. specificity results from the precise arrangement of atoms: the short-range forces require close contact, so a substrate must have a matching shape.

Emil Fischer's lock-and-key model (1894) pictured an active site complementary to its substrate. Daniel Koshland's induced fit (1958, see [7.1.7](/7.1.7#sec-7.1.1)) added that the site often becomes complementary only after the substrate has bound. As 8.3.2 shows, the essential complementarity is to the transition state, not to the substrate.

### 8.2.2. Enzymes Change Rates, Not Equilibria

A simple enzymatic reaction can be written

$$
\ce{E + S <=> ES <=> EP <=> E + P}.
$$
Its energetics are summarized in a reaction coordinate diagram: Gibbs energy against the progress of the reaction. The starting points (S or P under given conditions) are ground states; the top of the barrier, from which decay to S or P is equally likely, is the **transition state** S‡. It is not a chemical species with any lifetime and should not be confused with a **reaction intermediate** such as ES or EP, which occupies a valley of the diagram and lives longer than a molecular vibration (about $10^{-13}\,\mathrm{s}$). When a reaction has several steps, the step with the highest barrier is the **rate-limiting step**; for many enzymes several steps are partially rate-limiting, and which one dominates can change with conditions.

The position of equilibrium depends only on the Gibbs energies of the ground states. With the biochemical standard state (pH 7; [6.3.7](/6.3.7)),

$$
\Delta_{\mathrm{r}}G'^{\circ} = -RT\ln K', \qquad K' = \frac{[\ce{P}]}{[\ce{S}]}\ \text{at equilibrium},
$$
where $K'$ is the **equilibrium constant**. At $25\,^\circ\mathrm{C}$ a factor of ten in $K'$ corresponds to $5.7\,\mathrm{kJ\,mol^{-1}}$: $K' = 10^{-3}, 1, 10^{3}$ give $\Delta_{\mathrm{r}}G'^{\circ} = +17.1, 0, -17.1\,\mathrm{kJ\,mol^{-1}}$. A large negative $\Delta_{\mathrm{r}}G'^{\circ}$ means a favorable equilibrium, not a fast reaction: sucrose and oxygen ($\Delta_{\mathrm{r}}G'^{\circ}$ very negative) can be stored together indefinitely, yet in cells sucrose is oxidized within seconds by a series of enzymes that also capture much of the released energy.

An enzyme lowers the barrier by providing an alternative path through ES and EP; because the ground states of S and P are unchanged, it accelerates the forward and reverse reactions by exactly the same factor and leaves $K'$ unchanged. The energy barriers themselves are essential to life: without them, macromolecules and metabolites would decay spontaneously to simpler forms, and enzymes select which reactions happen.

![Reaction coordinate diagrams with schematic Gibbs energies. A: the uncatalyzed reaction S → P (dashed) passes over a high barrier Δ‡G_uncat; the enzyme-catalyzed reaction passes through the intermediates ES and EP, and its highest barrier, ES‡ relative to ES, is much lower (Δ‡G_cat); the overall Δ_rG'° between S and P is the same for both paths. B: the "stickase" thought experiment. An enzyme complementary to the substrate (red) binds it so tightly that the barrier measured from the deep ES trough is higher than without enzyme; an enzyme complementary to the transition state (green) binds the substrate only moderately and realizes most of the binding energy ΔG_B in the transition state, which lowers the barrier](./plots/reaction-coordinate.py)

### 8.2.3. Activation Gibbs Energy and Rate

The rate of S → P is $v = k[\ce{S}]$ (first order, $k$ in $\mathrm{s^{-1}}$); for two reactants $v = k[\ce{S_1}][\ce{S_2}]$ (second order, $k$ in $\mathrm{M^{-1}\,s^{-1}}$). Transition state theory relates $k$ to the **Gibbs energy of activation** $\Delta^{\ddagger}G$ through the **Eyring equation** ([6.3.16](/6.3.16#sec-16.3.1)):

$$
k = \frac{k_{\mathrm{B}}T}{h}\,\mathrm{e}^{-\Delta^{\ddagger}G/RT}.
$$
The relation is inverse and exponential, and this is the quantitative content of "an enzyme lowers the activation barrier".

**Formula 8.2.1 (Rate Enhancement and Barrier Lowering)** If an enzyme lowers the Gibbs energy of activation by $\Delta\Delta^{\ddagger}G = \Delta^{\ddagger}G_{\mathrm{uncat}} - \Delta^{\ddagger}G_{\mathrm{cat}}$, the rate constants are in the ratio

$$
\frac{k_{\mathrm{cat}}}{k_{\mathrm{uncat}}} = \mathrm{e}^{\Delta\Delta^{\ddagger}G/RT}, \qquad \Delta\Delta^{\ddagger}G = RT\ln 10 \cdot \lg\frac{k_{\mathrm{cat}}}{k_{\mathrm{uncat}}} \approx 5.71\,\mathrm{kJ\,mol^{-1}} \times \lg\frac{k_{\mathrm{cat}}}{k_{\mathrm{uncat}}}\quad (25\,^\circ\mathrm{C}).
$$

**Example 8.2.1** Carboxypeptidase A hydrolyzes the C-terminal peptide bond of proteins. Without enzyme the half-life is about 7.3 years ($2.3\times10^{8}\,\mathrm{s}$, so $k_{\mathrm{uncat}} = \ln 2/t_{1/2} = 3.0\times10^{-9}\,\mathrm{s^{-1}}$); on the enzyme it is about $1.2\,\mathrm{ms}$ ($k = 5.8\times10^{2}\,\mathrm{s^{-1}}$). The enhancement is $1.9\times10^{11}$, a barrier lowering of $11.3 \times 5.71 \approx 64\,\mathrm{kJ\,mol^{-1}}$. Orotidine 5′-monophosphate decarboxylase, an enzyme of pyrimidine synthesis ([7.1.28](/7.1.28)), holds the record: the uncatalyzed decarboxylation has a half-life of 78 million years, the enzymatic one of milliseconds, an enhancement of about $10^{17}$ and $\Delta\Delta^{\ddagger}G \approx 97\,\mathrm{kJ\,mol^{-1}}$.

![Rate enhancements produced by enzymes (k_cat/k_uncat, logarithmic scale, values compiled by Lehninger) and the equivalent lowering of the activation Gibbs energy at 25 °C (top axis, 5.71 kJ/mol per factor of ten). Enhancements range from 10⁵ (cyclophilin, a peptidyl-prolyl isomerase) to 10¹⁷ (OMP decarboxylase), that is, barrier lowerings of about 30 to 100 kJ/mol](./plots/rate-enhancement.py)

## 8.3. Principles of Catalytic Power and Specificity

### 8.3.1. Binding Energy

Where does an enzyme find 30 to 100 kJ/mol? The answer has two interwoven parts. The first is the noncovalent interaction of enzyme and substrate in the ES complex, mediated by the same forces that stabilize protein structure; the second is covalent interactions and other chemical mechanisms of the catalytic groups (8.3.4).

**Definition 8.3.1 (Binding Energy)** The Gibbs energy released by the formation of the weak, noncovalent interactions between an enzyme and its substrate is the **binding energy** $\Delta G_{\mathrm{B}}$.

Each weak interaction contributes about $4$ to $30\,\mathrm{kJ\,mol^{-1}}$ (the energies of [7.1.2](/7.1.2)), so many of them together can provide the 60 to $100\,\mathrm{kJ\,mol^{-1}}$ required by the observed rate enhancements. The need for many precisely positioned interacting groups, and for a cavity that does not collapse, is one reason enzymes are large.

The same binding energy is the source of specificity, the ability to discriminate between a substrate and a competing molecule. If the active site is arranged to make many weak interactions with one substrate in the transition state, it cannot make them with another; a molecule lacking a hydroxyl group that forms a hydrogen bond to a particular Glu is a poorer substrate. Catalysis and specificity are therefore conceptually distinct but experimentally hard to separate. Triose phosphate isomerase ([7.1.18](/7.1.18)) interconverts glyceraldehyde 3-phosphate and dihydroxyacetone phosphate by rearranging C-1 and C-2; yet more than 80% of its rate acceleration is lost with glyceraldehyde as substrate, that is, it comes from interactions with the phosphate group on C-3, far from the bonds that change.

### 8.3.2. Complementarity to the Transition State

An enzyme perfectly complementary to its substrate would be a poor catalyst. In the stickase thought experiment, an imaginary enzyme breaks a magnetized metal stick, which must first be bent (the transition state). A pocket lined with magnets that fits the straight stick holds it straight: the ES complex sits in a deep energy trough, and the barrier from there is higher than without enzyme. A pocket shaped like the bent stick binds the straight stick with only a few magnetic contacts, and the full set of contacts forms only when the stick bends: the binding energy "pays" for the bending (figure in 8.2.2, panel B).

The modern principle, proposed by Michael Polanyi (1921) and J. B. S. Haldane (1930), elaborated by Linus Pauling (1946) and William Jencks (1970s), is that an enzyme is complementary to the transition state of the reaction it catalyzes: some weak interactions are formed in ES, but the full complement forms only in the transition state, and the binding energy released there offsets the Gibbs energy needed to reach it. The groups on the substrate that take part can lie far from the bonds that are broken, as the phosphate of triose phosphate isomerase shows.

**Formula 8.3.1 (Transition-State Binding)** Let $K_{\mathrm{S}} = [\ce{E}][\ce{S}]/[\ce{ES}]$ be the dissociation constant of the substrate and treat the transition states $\mathrm{S^{\ddagger}}$ and $\mathrm{ES^{\ddagger}}$ as being in equilibrium with S and ES, so that $k_{\mathrm{uncat}} \propto [\mathrm{S^{\ddagger}}]/[\ce{S}]$ and $k_{\mathrm{cat}} \propto [\mathrm{ES^{\ddagger}}]/[\ce{ES}]$ with the same factor $k_{\mathrm{B}}T/h$. The thermodynamic cycle through $\ce{E} + \mathrm{S^{\ddagger}} \rightleftharpoons \mathrm{ES^{\ddagger}}$ gives the dissociation constant of the enzyme–transition state complex

$$
K_{\mathrm{TS}} = \frac{[\ce{E}][\mathrm{S^{\ddagger}}]}{[\mathrm{ES^{\ddagger}}]} = K_{\mathrm{S}}\,\frac{k_{\mathrm{uncat}}}{k_{\mathrm{cat}}} \approx \frac{k_{\mathrm{uncat}}}{k_{\mathrm{cat}}/K_{\mathrm{M}}}.
$$
The last form uses the **specificity constant** $k_{\mathrm{cat}}/K_{\mathrm{M}}$ ([6.3.17](/6.3.17#sec-17.3.5)) and $K_{\mathrm{M}} \approx K_{\mathrm{S}}$.

A rate enhancement of $10^{n}$ thus means that the enzyme binds the transition state $10^{n}$ times more tightly than the substrate. For OMP decarboxylase, $k_{\mathrm{uncat}} = 2.8\times10^{-16}\,\mathrm{s^{-1}}$ and $k_{\mathrm{cat}}/K_{\mathrm{M}} \approx 5.6\times10^{7}\,\mathrm{M^{-1}\,s^{-1}}$ give $K_{\mathrm{TS}} \approx 5\times10^{-24}\,\mathrm{M}$, a binding Gibbs energy of about $-133\,\mathrm{kJ\,mol^{-1}}$, far tighter than any ordinary ligand binds a protein. This suggests a strategy for inhibitor design.

**Definition 8.3.2 (Transition-State Analog)** A **transition-state analog** is a stable molecule designed to resemble the transition state (or a high-energy intermediate close to it) of an enzymatic reaction; it binds the enzyme much more tightly than the substrate does.

No stable molecule can mimic a transition state perfectly, but analogs binding $10^2$ to $10^8$ times more tightly than the substrate are known. Phosphoglycolohydroxamate, which resembles the enediolate intermediate of class II aldolase, binds nearly $10^4$ times better than the product dihydroxyacetone phosphate. Transition-state analogs are strong evidence for Pauling's principle and are the basis of drugs such as the HIV protease inhibitors (8.4.2) and of PALA, the inhibitor of aspartate transcarbamoylase ([7.1.9](/7.1.9)). Antibodies raised against transition-state analogs can themselves be catalysts (catalytic antibodies, Lerner and Schultz, 1986), although much weaker ones than enzymes.

### 8.3.3. How Binding Energy Lowers the Barrier

The barrier $\Delta^{\ddagger}G$ includes several physical contributions, and binding energy is used against each of them.

| Barrier | How binding energy overcomes it |
|---|---|
| Entropy of molecules in solution: reacting groups rarely meet in the right orientation | entropy reduction: the substrates are held next to each other and to the catalytic groups in the reactive orientation |
| Solvation shell of hydrogen-bonded water around the substrate | desolvation: enzyme–substrate interactions replace most of the hydrogen bonds to water |
| Distortion (mostly electron redistribution) the substrate must undergo | interactions formed only in the transition state compensate for the unfavorable Gibbs energy of distortion |
| Need for precise alignment of the catalytic groups | induced fit: binding changes the conformation of the enzyme, bringing catalytic groups into position and allowing further interactions in the transition state |

Entropy reduction alone can be large. The reaction of an ester with a carboxylate to form an anhydride is $10^5\,\mathrm{M}$ faster when both groups are in the same molecule (a unimolecular rate constant compared with a bimolecular one, hence the unit: the groups behave as if each were present at $10^5\,\mathrm{M}$, an effective molarity), and $10^8\,\mathrm{M}$ faster when the rotations about the connecting bonds are also frozen. Induced fit can involve a few residues near the active site or the movement of whole domains (hexokinase, 8.4.3), and usually a network of coupled motions throughout the enzyme.

### 8.3.4. Catalytic Groups: Acid–Base, Covalent and Metal Ion Catalysis

Once the substrate is bound, properly positioned functional groups help to break and form bonds. The first two of the following mechanisms involve transient covalent interactions or group transfer, and so differ from catalysis by binding energy.

**Definition 8.3.3 (General Acid–Base Catalysis)** Catalysis by proton transfer mediated by weak acids and bases other than water is **general acid–base catalysis**; catalysis by the $\ce{H3O+}$ and $\ce{OH-}$ of water alone is specific acid–base catalysis.

Many reactions pass through unstable charged intermediates that tend to revert to reactants; donating or removing a proton converts them into species that go on to products. In solution the distinction between specific and general catalysis is made by varying the buffer concentration at constant pH (**acid–base catalysis**, [6.3.17](/6.3.17#sec-17.3.4)). In an active site, where water may be excluded, side chains take its place as proton donors and acceptors, and precise positioning gives rate enhancements of $10^2$ to $10^5$; this type of catalysis occurs in the vast majority of enzymes. The groups and their typical $\mathrm{p}K_{\mathrm{a}}$ values in free amino acids are those of [7.1.3](/7.1.3#sec-3.2.2); in proteins they can be shifted by several units ([7.1.3](/7.1.3#sec-3.4.2)).

| Residue | General acid (proton donor) | General base (proton acceptor) | Typical $\mathrm{p}K_{\mathrm{a}}$ |
|---|---|---|---|
| Asp, Glu | $\ce{-COOH}$ | $\ce{-COO-}$ | about 4 |
| His | imidazolium | imidazole | about 6 |
| Cys | $\ce{-SH}$ | $\ce{-S-}$ | about 8.3 |
| Tyr | $\ce{-OH}$ (phenol) | $\ce{-O-}$ (phenolate) | about 10 |
| Lys | $\ce{-NH3+}$ | $\ce{-NH2}$ | about 10.5 |
| Arg | guanidinium | guanidine | about 12.5 |
| Ser | $\ce{-OH}$ | $\ce{-O-}$ (only when activated, as in 8.4.1) | about 13 or above |

His is the most versatile: with a $\mathrm{p}K_{\mathrm{a}}$ near 6 it is present in both forms at physiological pH and can act as acid and base in successive steps of one mechanism.

**Definition 8.3.4 (Covalent Catalysis)** In **covalent catalysis** a transient covalent bond is formed between the enzyme and the substrate.

For the hydrolysis of A–B by an enzyme with a nucleophilic group X:, the path becomes

$$
\ce{A-B + X: -> A-X + B}, \qquad \ce{A-X + H2O -> A + X: + B}.
$$
The new path catalyzes the reaction only if both of its steps are faster than the uncatalyzed reaction. Nucleophiles include the side chains of Ser, Cys, His, Lys (which forms Schiff bases with carbonyl groups), Asp and Glu, and the functional groups of coenzymes such as pyridoxal phosphate and thiamine pyrophosphate; the covalent complex always reacts further to regenerate the free enzyme. Covalent catalysis is the enzymatic form of familiar organic reactions: the acyl-enzyme of the serine proteases is formed and hydrolyzed by **nucleophilic acyl substitution**, and the Schiff base of class I aldolases is the **enamine** chemistry of [6.5.22](/6.5.22).

**Definition 8.3.5 (Metal Ion Catalysis)** In **metal ion catalysis** a metal ion bound to the enzyme or the substrate takes part in the reaction: by orienting the substrate through ionic interactions, by stabilizing charged transition states and intermediates, or by mediating oxidation–reduction through reversible changes of its oxidation state.

Nearly a third of all known enzymes need one or more metal ions. A bound metal ion can also make a ligand more acidic: the $\ce{Zn^2+}$-bound water of carbonic anhydrase has a $\mathrm{p}K_{\mathrm{a}}$ near 7 instead of 15.7, so the enzyme has a hydroxide nucleophile available at neutral pH. Most enzymes combine several of these strategies, as the examples of 8.4 show.

## 8.4. Examples of Enzymatic Reactions

To understand an enzyme's mechanism completely we would need the sequence of enzyme-bound intermediates, the structure of every intermediate and transition state, the rates of their interconversion, their structural relation to the enzyme and the energy contributed by each interacting group. Only a few enzymes meet these requirements; the following examples are among the best understood.

### 8.4.1. Chymotrypsin: Acylation and Deacylation of a Ser Residue

Bovine pancreatic chymotrypsin ($M_{\mathrm{r}}$ 25 191) is a protease that cleaves peptide bonds on the carboxyl side of aromatic residues (Phe, Trp, Tyr), whose side chains fit a hydrophobic specificity pocket. It consists of three chains linked by disulfide bonds, produced from a single-chain zymogen ([7.1.9](/7.1.9)).

**Definition 8.4.1 (Serine Protease, Catalytic Triad, Oxyanion Hole)** A protease is an enzyme that catalyzes the hydrolytic cleavage of peptide bonds. In a **serine protease** (chymotrypsin, trypsin, elastase, thrombin, subtilisin) the nucleophile is the hydroxyl of an active-site Ser. In chymotrypsin, Ser195, His57 and Asp102 form a hydrogen-bonded network, the **catalytic triad**; the pocket in which the negative charge of the tetrahedral intermediates develops, lined by the backbone amide N–H groups of Gly193 and Ser195, is the **oxyanion hole**.

Chymotrypsin accelerates peptide hydrolysis by at least $10^9$, not by direct attack of water but through a covalent acyl-enzyme intermediate, so the reaction has two phases.

1. Acylation. When the substrate binds, His57 acts as a general base and removes the proton of the Ser195 hydroxyl, whose oxygen attacks the carbonyl carbon of the scissile peptide bond. Asp102 holds His57 in the correct tautomer and orientation. A short-lived **tetrahedral intermediate** forms, its oxyanion stabilized by the two hydrogen bonds of the oxyanion hole; the bond from Gly193 exists only in this intermediate and the transition states leading to and from it, an example of binding energy used through transition-state complementarity. The intermediate collapses, His57 (now a general acid) protonates the leaving amine, and the first product leaves, the acyl group remaining esterified to Ser195. The arrow-pushing mechanism of this phase is drawn in [6.5.33](/6.5.33#sec-33.8.3).
2. Deacylation. Water enters as the second substrate and the steps are repeated with water in place of the amine: His57 deprotonates water, the oxygen attacks the ester carbonyl to give a second tetrahedral intermediate, its collapse releases the carboxylic acid product, and His57 returns the proton to Ser195.

![Deacylation of the acyl-enzyme of chymotrypsin. His57, unprotonated after the acylation phase, acts as a general base and removes a proton from a water molecule, while the water oxygen adds to the ester carbonyl carbon of the acyl-Ser195 intermediate and the C=O π electrons move onto oxygen; Asp102 holds His57 through a hydrogen bond (dashed). The second tetrahedral intermediate carries an oxyanion stabilized by the oxyanion hole; its collapse, with His57 now acting as a general acid, releases the carboxylic acid and regenerates the free Ser195](./plots/chymotrypsin-deacylation.py)

Why is the Ser195 hydroxyl ($\mathrm{p}K_{\mathrm{a}}$ normally above 13) so reactive? Deprotonation by His57 avoids an unstable positive charge on the attacking oxygen. It has been proposed that, on substrate binding, the His57–Asp102 hydrogen bond becomes a short, strong (low-barrier) hydrogen bond that raises the $\mathrm{p}K_{\mathrm{a}}$ of His57 from about 7 to above 12; the size of this effect is still debated, but the importance of the triad is clear from mutants of the bacterial serine protease subtilisin: replacing its catalytic Ser or His by Ala lowers $k_{\mathrm{cat}}$ by a factor of about $10^6$, yet even the enzyme lacking all three triad residues remains some $10^3$ times faster than the uncatalyzed reaction, a measure of what binding and the oxyanion hole contribute on their own.

The first evidence for the acyl-enzyme came from pre-steady-state kinetics. In 1954 B. S. Hartley and B. A. Kilby followed the hydrolysis of the ester *p*-nitrophenyl acetate, a poor substrate (less binding energy, so the reaction is slow enough to follow), by the release of colored *p*-nitrophenol. They observed a rapid burst of just under one *p*-nitrophenol per enzyme molecule, followed by a slower steady rate. The burst is the fast acylation of all enzyme molecules; the steady rate is limited by the slower deacylation.

**Formula 8.4.1 (Burst Kinetics)** For the mechanism $\mathrm{E + S} \rightleftharpoons \mathrm{ES} \xrightarrow{k_2} \text{E-acyl} + \mathrm{P_1}$, $\text{E-acyl} \xrightarrow{k_3} \mathrm{E + P_2}$ at saturating substrate, the first product appears as

$$
[\mathrm{P_1}](t) = [\ce{E}]_0\left[\frac{k_2k_3}{k_2 + k_3}\,t + \left(\frac{k_2}{k_2 + k_3}\right)^{2}\left(1 - \mathrm{e}^{-(k_2 + k_3)t}\right)\right].
$$
After the transient, product forms at the steady-state rate $k_{\mathrm{cat}}[\ce{E}]_0$ with $k_{\mathrm{cat}} = k_2k_3/(k_2 + k_3)$; extrapolated to $t = 0$ the line has the intercept (burst amplitude) $[\ce{E}]_0\,k_2^2/(k_2 + k_3)^2$, which tends to $[\ce{E}]_0$ when $k_2 \gg k_3$.

**Proof** At saturation every enzyme molecule is ES or E-acyl, so $[\ce{ES}] = [\ce{E}]_0 - [\text{E-acyl}]$ and $\mathrm{d}[\text{E-acyl}]/\mathrm{d}t = k_2([\ce{E}]_0 - [\text{E-acyl}]) - k_3[\text{E-acyl}]$, a linear equation ([2.4](/2.4)) with solution $[\text{E-acyl}] = [\ce{E}]_0\frac{k_2}{k_2 + k_3}\left(1 - \mathrm{e}^{-(k_2 + k_3)t}\right)$. Integrating $\mathrm{d}[\mathrm{P_1}]/\mathrm{d}t = k_2[\ce{ES}]$ from 0 gives the result. $\square$

![Simulated burst kinetics for chymotrypsin and p-nitrophenyl acetate (E + S ⇌ ES → E-acyl + P₁ → E + P₂ with k₂ = 0.1 s⁻¹ ≫ k₃ = 0.004 s⁻¹, [S]₀ = 2 mM, K_S = 0.1 mM; illustrative values, integrated numerically with solve_ivp). A: p-nitrophenol against time for three enzyme concentrations: a fast burst is followed by the slow steady-state rate k_cat[E]₀ (dashed lines extrapolated to t = 0). B: the burst amplitudes are proportional to [E]₀ with slope close to 1 (0.92 here, as predicted by Formula 8.4.1), about one product per active site](./plots/chymotrypsin-burst.py)

A burst of about one product per active site means that a step after the release of that product is rate-limiting, and its amplitude counts the active sites (active-site titration). The rates of chymotrypsin also depend on pH in a way that identifies the catalytic groups (8.5).

### 8.4.2. HIV Protease: Transition-State Analogs as Drugs

New drugs are almost always designed to inhibit an enzyme. The human immunodeficiency virus (HIV), the cause of AIDS, is a retrovirus: its RNA genome is copied into DNA by reverse transcriptase, integrated into a host chromosome by integrase, and its proteins are made as large polyproteins that the viral protease cuts into functional pieces ([7.2](/7.2)). These three enzymes are the main drug targets.

There are four major classes of proteases. Serine proteases and cysteine proteases form covalent acyl-enzyme intermediates; aspartyl proteases and metalloproteases do not, and activate a water molecule to attack the peptide bond directly. HIV protease is an aspartyl protease, a homodimer of two 99-residue subunits whose two active-site Asp25 residues (one from each subunit) act as general acid and general base, facilitating the attack of water on the carbonyl group. The resulting tetrahedral intermediate is close in structure and energy to the transition state. The enzyme cleaves most efficiently between Phe and Pro, with a pocket for the aromatic side chain next to the scissile bond.

The HIV protease inhibitors (saquinavir, the first, approved in 1995, ritonavir, indinavir, darunavir and others) share a core: a hydroxyl group that mimics the tetrahedral oxygen of the intermediate, next to a benzyl group that fills the aromatic pocket. They are transition-state analogs (Definition 8.3.2) and bind noncovalently but so tightly that they behave almost as irreversible inhibitors. Combined with inhibitors of reverse transcriptase and integrase, they have turned HIV infection from a fatal disease into a chronic one.

### 8.4.3. Hexokinase: Induced Fit

Yeast hexokinase ($M_{\mathrm{r}}$ 107 862) is a bisubstrate enzyme that transfers the γ-phosphoryl group of ATP (as its $\ce{Mg^2+}$ complex, the form in which ATP and ADP bind to enzymes) to the hydroxyl at C-6 of glucose ([7.1.18](/7.1.18)). This hydroxyl is chemically similar to the hydroxyl of water, and water freely enters the active site, yet hexokinase favors glucose over water as phosphoryl acceptor by a factor of about $10^6$. Hydrolysis of ATP would waste the cell's energy currency.

The discrimination comes from induced fit. Without glucose the enzyme is in an open, inactive conformation, with the active-site side chains out of position. Binding of glucose (but not water) and Mg·ATP makes the two lobes of the U-shaped enzyme close around the substrates, which brings the catalytic groups into place. Xylose, which is one carbon shorter than glucose and cannot be phosphorylated, still induces the closure: adding it increases the rate of ATP hydrolysis, because the enzyme is "tricked" into phosphorylating water. Specificity here lies not in the formation of the ES complex but in the relative rates of the subsequent catalytic steps. Once closed, hexokinase also uses general acid–base catalysis and transition-state stabilization.

### 8.4.4. Enolase: Metal Ion Catalysis

Enolase, a glycolytic enzyme ([7.1.18](/7.1.18)), catalyzes the reversible dehydration of 2-phosphoglycerate to phosphoenolpyruvate:

```smiles
OC[C@@H](OP(=O)([O-])[O-])C(=O)[O-]>>C=C(OP(=O)([O-])[O-])C(=O)[O-].O
```

Yeast enolase ($M_{\mathrm{r}}$ 93 316) is a dimer of 436-residue subunits. The reaction has two steps. First Lys345, a general base, abstracts the proton from C-2; then Glu211, a general acid, protonates the departing hydroxyl group. The C-2 proton is not normally acidic, but the adjacent carboxylate pulls electron density from C-2, and in the active site this carboxylate is coordinated by two $\ce{Mg^2+}$ ions, which greatly enhance the electron withdrawal and lower the $\mathrm{p}K_{\mathrm{a}}$ enough for Lys345 to remove the proton. As the **enolate** intermediate forms, the metal ions also shield the two negative charges on the carboxylate oxygens, stabilizing both the intermediate and the transition state that precedes it. Enolase thus combines metal ion catalysis, general acid–base catalysis and transition-state stabilization.

### 8.4.5. Penicillin: An Irreversible Inhibitor of Transpeptidase

Penicillin, discovered by Alexander Fleming in 1928 and developed as a drug by Howard Florey and Ernst Chain in the early 1940s, blocks the synthesis of peptidoglycan, the cross-linked polymer of the bacterial cell wall ([7.1.10](/7.1.10)). The last cross-linking step is a transpeptidase reaction that uses covalent catalysis like chymotrypsin: an active-site Ser attacks the peptide bond between the two terminal D-Ala residues of a precursor, releasing one D-Ala and forming an acyl-enzyme, which is then attacked by an amino group of a second precursor, cross-linking the two.

Penicillins mimic one conformation of the D-Ala–D-Ala terminus, but the peptide bond is replaced by the strained four-membered **β-lactam** ring (benzylpenicillin, penicillin G, left; D-Ala–D-Ala, right):

```smiles
CC1(C)S[C@@H]2[C@H](NC(=O)Cc3ccccc3)C(=O)N2[C@H]1C(=O)O
C[C@H](C(=O)N[C@H](C)C(=O)[O-])[NH3+]
```

The active-site Ser attacks the β-lactam carbonyl and forms a covalent acyl-enzyme, but the leaving group remains attached through the rest of the bicyclic ring, and the adduct is hydrolyzed so slowly that the enzyme is irreversibly inactivated. Without cross-links the wall cannot resist the osmotic pressure ([7.1.2](/7.1.2)) and most bacteria burst. Resistant bacteria express β-lactamases, serine hydrolases that cleave the β-lactam ring before it reaches the transpeptidase. Clavulanic acid, a suicide inactivator of β-lactamases ([7.1.9](/7.1.9)), forms a covalent adduct with the active-site Ser that rearranges into a more reactive species, which acylates a second nucleophile of the site irreversibly; it is combined with amoxicillin in co-amoxiclav. Bacteria with β-lactamases insensitive to clavulanate have already appeared.

## 8.5. pH Dependence of Enzyme Activity

Enzymes have an optimum pH, or pH range, at which their activity is maximal. Active-site side chains can act as acids or bases only in a particular state of ionization; elsewhere in the protein, deprotonating a group may break an ion pair that stabilizes the active conformation; less often, a group on the substrate is titrated.

**Formula 8.5.1 (Two-p$K_{\mathrm{a}}$ Model)** Suppose that only the form EH of an enzyme, in which group 1 ($\mathrm{p}K_1$) has lost its proton and group 2 ($\mathrm{p}K_2 > \mathrm{p}K_1$) still carries it, is active. With the acid dissociation constants $K_1$, $K_2$ the fraction of enzyme in the active form, and so the rate, is

$$
v = \frac{v_{\mathrm{lim}}}{1 + [\ce{H+}]/K_1 + K_2/[\ce{H+}]},
$$
a bell-shaped curve with its maximum at $\mathrm{pH}_{\mathrm{opt}} = (\mathrm{p}K_1 + \mathrm{p}K_2)/2$, where the active fraction is $1/(1 + 2\cdot10^{(\mathrm{p}K_1 - \mathrm{p}K_2)/2})$.

The maximum follows from minimizing $[\ce{H+}]/K_1 + K_2/[\ce{H+}]$, which gives $[\ce{H+}] = \sqrt{K_1K_2}$. On a logarithmic scale the limbs have slopes $+1$ and $-1$ and their extrapolations meet the plateau at $\mathrm{p}K_1$ and $\mathrm{p}K_2$ (Dixon's construction); when the two $\mathrm{p}K_{\mathrm{a}}$ values are close, the plateau is never reached and the apparent values must be fitted. Each factor is the **Henderson–Hasselbalch equation** of [7.1.2](/7.1.2) applied to one group.

![pH dependence of enzyme activity in the two-pKa model. A: pepsin-like (pK₁ 0.8, pK₂ 2.4) and chymotrypsin-like (pK₁ 7.0, pK₂ 9.0) profiles, with optima at pH 1.6 and 8.0; the pKa values are illustrative, chosen to reproduce the observed optima. Because the pKa values are only 1.6 to 2 units apart, the maximal active fraction is only 0.76 to 0.83. B: the same model on a log scale for well-separated pKa values (5 and 9): the limbs have slopes +1 and −1, and the dashed asymptotes meet the plateau at the two pKa values](./plots/ph-activity.py)

The pH optimum of an enzyme is usually close to the pH of its environment: pepsin of the stomach has its optimum near pH 1.6 (gastric juice has pH 1–2), glucose 6-phosphatase of hepatocytes near 7.8 (cytosol about 7.2), chymotrypsin of the small intestine near 8. The pH profile of chymotrypsin can be dissected. At low (subsaturating) substrate concentration the rate measures $k_{\mathrm{cat}}/K_{\mathrm{M}}$ and the profile is bell-shaped with its optimum at pH 8. Measuring $k_{\mathrm{cat}}$ and $K_{\mathrm{M}}$ separately shows that the rise just above pH 7 is in $k_{\mathrm{cat}}$ and reflects His57, which must be unprotonated to accept the Ser195 proton; the fall above pH 8.5 is in $1/K_{\mathrm{M}}$ and reflects the α-amino group of Ile16 (the N-terminus of the B chain), which must be protonated to form a salt bridge with Asp194 that holds the specificity pocket open.

The $\mathrm{p}K_{\mathrm{a}}$ values read from such profiles must be interpreted with care, because the protein environment shifts them ([7.1.3](/7.1.3#sec-3.4.2)). An activity change near pH 7 often reflects a His, but in acetoacetate decarboxylase an active-site Lys has a $\mathrm{p}K_{\mathrm{a}}$ of 6.6 (10.5 in free lysine) because of nearby positive charges; the unprotonated amine then forms a Schiff base with the substrate.

## Summary

| Structural feature | Chemical property | Function |
|---|---|---|
| Active site: cleft built from distant residues, small part of the protein (Definition 8.2.1) | many weak interactions with precise geometry; water excluded | binding, specificity, desolvation |
| Complementarity to the transition state, not the substrate (8.3.2) | binding energy $\Delta G_{\mathrm{B}}$ (Definition 8.3.1) realized mainly in the transition state | lowers $\Delta^{\ddagger}G$; $K_{\mathrm{TS}} = K_{\mathrm{S}}k_{\mathrm{uncat}}/k_{\mathrm{cat}}$ (Formula 8.3.1); transition-state analogs (Definition 8.3.2) |
| Flexible protein, induced fit | conformational change on binding | aligns catalytic groups; hexokinase discriminates glucose from water by $10^6$ (8.4.3) |
| His, Asp, Glu, Lys, Cys, Tyr side chains | proton donors and acceptors with $\mathrm{p}K_{\mathrm{a}}$ tuned by the environment | general acid–base catalysis, $10^2$–$10^5$ (Definition 8.3.3) |
| Nucleophilic Ser, Cys, Lys; coenzymes | transient covalent bonds | covalent catalysis (Definition 8.3.4): acyl-enzymes, Schiff bases |
| Bound $\ce{Mg^2+}$, $\ce{Zn^2+}$, Fe, Cu | charge stabilization, Lewis acidity, redox | metal ion catalysis (Definition 8.3.5): enolase, carbonic anhydrase |
| Catalytic triad and oxyanion hole (Definition 8.4.1) | activated Ser nucleophile; hydrogen bonds to the tetrahedral oxyanion | chymotrypsin: acylation then rate-limiting deacylation, burst (Formula 8.4.1) |
| Ionizable active-site groups | protonation states | bell-shaped pH profile, optimum $(\mathrm{p}K_1 + \mathrm{p}K_2)/2$ (Formula 8.5.1) |

| Quantity | Value |
|---|---|
| Rate enhancements | $10^5$ (cyclophilin) to $10^{17}$ (OMP decarboxylase) |
| Barrier lowering per factor of 10 in rate, $25\,^\circ\mathrm{C}$ | $RT\ln 10 = 5.71\,\mathrm{kJ\,mol^{-1}}$ (Formula 8.2.1) |
| One weak interaction / total needed | 4–30 / 60–100 $\mathrm{kJ\,mol^{-1}}$ |
| Effective molarity from entropy reduction | up to $10^5$–$10^8\,\mathrm{M}$ |
| Enzymes requiring metal ions | nearly one third |
| EC classes | 7 (oxidoreductases, transferases, hydrolases, lyases, isomerases, ligases, translocases) |
| pH optima | pepsin about 1.6, glucose 6-phosphatase 7.8, chymotrypsin 8 |

## Questions

1. Urease accelerates the hydrolysis of urea at pH 8.0 and $20\,^\circ\mathrm{C}$ by a factor of $10^{14}$. A given amount of urease hydrolyzes a sample of urea completely in 5.0 min. How long would the uncatalyzed hydrolysis take, and by how much does urease lower $\Delta^{\ddagger}G$?

   **Answer** The time scales with the inverse of the rate: $5.0\,\mathrm{min} \times 10^{14} = 5.0\times10^{14}\,\mathrm{min} \approx 9.5\times10^{8}$ years. At $293\,\mathrm{K}$, $\Delta\Delta^{\ddagger}G = RT\ln 10^{14} = 8.314\times10^{-3} \times 293 \times 32.2 \approx 78\,\mathrm{kJ\,mol^{-1}}$.
2. Which of the following does an enzyme that catalyzes S ⇌ P change: (a) the forward rate constant, (b) $K'$, (c) $\Delta^{\ddagger}G$, (d) $\Delta_{\mathrm{r}}G'^{\circ}$, (e) the reverse rate constant?

   **Answer** (a), (c) and (e). The enzyme lowers the barrier and so increases both rate constants by the same factor; $K'$, their ratio, and $\Delta_{\mathrm{r}}G'^{\circ} = -RT\ln K'$ depend only on the ground states and are unchanged.
3. Explain why an enzyme whose active site is perfectly complementary to its substrate would be a poor catalyst, and why a transition-state analog is a better inhibitor than a substrate analog.

   **Answer** Binding energy lowers the Gibbs energy of whatever species it stabilizes. If all interactions are made with the substrate, ES is stabilized as much as the transition state, or more, and the barrier measured from ES is not lowered (it can be raised, as in the stickase with a straight pocket). Catalysis requires the interactions to be stronger in the transition state, so that $K_{\mathrm{TS}} \ll K_{\mathrm{S}}$ (Formula 8.3.1). A molecule resembling the transition state captures this extra binding energy, so it binds far more tightly than the substrate or a substrate analog; for an enzyme with a $10^{10}$-fold enhancement, a perfect analog would bind $10^{10}$ times more tightly than the substrate.
4. In the burst experiment of Hartley and Kilby, how would the curves change if (a) acylation, not deacylation, were rate-limiting ($k_2 \ll k_3$), (b) 20% of the enzyme molecules were inactive?

   **Answer** (a) The burst amplitude $[\ce{E}]_0k_2^2/(k_2 + k_3)^2$ becomes negligible: product appears at a constant rate from the start, and no burst is seen; a burst only shows that a step after the release of the observed product is rate-limiting. (b) Both the amplitude and the steady-state slope fall to 80%, because only active molecules contribute; the amplitude then measures the concentration of active sites, which is how burst experiments are used to titrate enzyme preparations (Hartley and Kilby found slightly less than one product per enzyme molecule for this reason).
5. Hexokinase incubated at $45\,^\circ\mathrm{C}$ loses 50% of its activity in 12 min, but only 3% in the presence of a very high concentration of glucose. Suggest a reason.

   **Answer** Glucose binds and induces the closed conformation, which is stabilized by the additional noncovalent interactions with the substrate. The binding energy adds to the stability of the folded state (ligand binding shifts the folding equilibrium towards the native form, [7.1.6](/7.1.6)), so thermal unfolding is slower; with glucose bound, most enzyme molecules are in the more stable ES form.
