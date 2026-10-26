---
title: Nucleotide Biosynthesis and Degradation
description: De novo and salvage pathways and PRPP; the origin of the purine ring atoms and the ten steps from PRPP to IMP, its branching to AMP and GMP and their feedback control; pyrimidine synthesis through carbamoyl phosphate synthetase II, aspartate transcarbamoylase, CAD, dihydroorotate dehydrogenase and UMP synthase; NMP and NDP kinases; ribonucleotide reductase, its radical mechanism, classes and two allosteric sites, with a model of dNTP pool balance; thymidylate synthase and the folate cycle; degradation of purines to uric acid and of pyrimidines to β-amino acids; salvage, Lesch–Nyhan syndrome, ADA deficiency and gout; nucleotide metabolism as a target of chemotherapy.
---

Nucleotides are the monomers of **RNA** and **DNA**, the energy currency of the cell (ATP, GTP), parts of **coenzymes** (**NAD**, **FAD**, **coenzyme A**) and of activated intermediates (UDP-glucose, CDP-diacylglycerol), and **second messengers** (**cAMP**, cGMP); their structures and chemistry are in [7.1.11](/7.1.11). This chapter shows how cells make and break them. The logic is the same as for the amino acids in [7.1.27](/7.1.27), from which much of the nitrogen comes: a few precursors of central **metabolism** (ribose 5-phosphate from the **pentose phosphate pathway**, glutamine, glycine, aspartate, bicarbonate and one-carbon units on **tetrahydrofolate**) are assembled at a high cost in ATP, and every pathway is held in check by **feedback inhibition** at its **committed step**. Three features are peculiar to nucleotides. The free bases are not intermediates of their synthesis; the four DNA precursors are made by a single **enzyme**, ribonucleotide reductase, whose radical chemistry and allosteric regulation are among the most remarkable in biochemistry; and because nucleotide pools are tiny compared with the demand of **replication**, the pathways are the targets of many of the oldest anticancer, antiviral, antibacterial and immunosuppressive drugs. The use of nucleotides in replication and repair belongs to molecular biology ([7.2.7](/7.2.7), [7.2.8](/7.2.8)).

## 28.1. Overview

### 28.1.1. De Novo and Salvage Pathways

**Definition 28.1.1 (De Novo and Salvage Pathways)** A **de novo pathway** synthesizes nucleotides from small metabolic precursors: amino acids, ribose 5-phosphate, $\ce{CO2}$, $\ce{NH3}$ and one-carbon units. A **salvage pathway** recycles the free bases and nucleosides released by the breakdown of nucleic acids and nucleotides, or taken up from the diet, by attaching them again to ribose phosphate.

The de novo pathways are nearly identical in all organisms. Both use 5-phosphoribosyl 1-pyrophosphate (PRPP, below) as the donor of ribose phosphate, an amino acid as the core of the ring (glycine for purines, aspartate for pyrimidines), and glutamine as the main donor of amino groups (in five steps; aspartate gives amino groups in two more). The two classes are built in opposite orders:

| | Purines | Pyrimidines |
|---|---|---|
| Ring assembly | atom by atom on ribose 5-phosphate (from PRPP) | ring closed first (orotate), then attached to PRPP |
| First nucleotide with a complete ring | IMP (inosinate) | OMP (orotidylate), then UMP |
| Core amino acid | glycine (C4, C5, N7) | aspartate (N1, C4, C5, C6) |
| Committed step | glutamine–PRPP amidotransferase | CPS II (animals) / aspartate transcarbamoylase (bacteria) |

Free bases (adenine, guanine, uracil, cytosine, thymine) are intermediates only of salvage and degradation. Two further points matter for the cell. The enzymes of de novo synthesis tend to form multienzyme complexes, a recurring theme of metabolism (the **metabolon**), which channel unstable intermediates. And the pools of nucleotides other than ATP are small, about 1% or less of what is needed to replicate the **genome**, so synthesis must keep pace with DNA replication and can limit it; this is why inhibitors of nucleotide synthesis stop proliferating cells first.

### 28.1.2. PRPP

**Definition 28.1.2 (PRPP)** **PRPP** (5-phosphoribosyl 1-pyrophosphate) is α-D-ribose 5-phosphate carrying a pyrophosphate group on C-1, the activated donor of the ribose 5-phosphate unit; it is made by ribose phosphate pyrophosphokinase (PRPP synthetase), which transfers the β,γ-pyrophosphoryl group of ATP to ribose 5-phosphate:

$$
\text{ribose 5-phosphate} + \ce{ATP} \to \text{PRPP} + \ce{AMP}. \tag{28.1}
$$

In every reaction that uses PRPP a nitrogen nucleophile displaces the pyrophosphate at C-1, and the hydrolysis of the released $\mathrm{PP_i}$ makes the transfer irreversible. Besides the purine and pyrimidine nucleotides (de novo and salvage), PRPP supplies the ribose phosphate of histidine and tryptophan (in which the ribose is not retained, [7.1.27](/7.1.27)) and of NAD (from nicotinamide or nicotinate). PRPP synthetase is inhibited by ADP and GDP and by other end products of the pathways that consume PRPP; **mutations** that make it overactive (PRPP synthetase superactivity, X-linked) cause purine overproduction and gout in young men.

## 28.2. Purine Nucleotides

### 28.2.1. Origin of the Ring Atoms

John Buchanan located the origin of each atom of the purine ring in the late 1940s by feeding $^{14}\mathrm{C}$- and $^{15}\mathrm{N}$-labeled compounds to pigeons, which excrete nitrogen as uric acid, a purine that is easily isolated and degraded atom by atom; with G. Robert Greenberg he then worked out the enzymatic steps in the 1950s.

![Origin of the ring atoms of purines and pyrimidines, colored by source. Purine (left, as in IMP): N1 comes from the amino group of aspartate; C2 and C8 from formate, carried as N¹⁰-formyltetrahydrofolate; N3 and N9 from the amide nitrogen of glutamine; C4, C5 and N7 from glycine, which enters as a whole molecule; C6 from bicarbonate. The ring is built on ribose 5-phosphate, attached at N9 from the first step. Pyrimidine (right, as in UMP): C2 from bicarbonate and N3 from the amide of glutamine, both through carbamoyl phosphate; N1, C4, C5 and C6 from aspartate. Ribose 5-phosphate is attached to N1 only after the ring is complete](./plots/nucleotide-atom-origins.py)

### 28.2.2. Ten Steps from PRPP to IMP

**Definition 28.2.1 (IMP)** **IMP** (inosinate, inosine 5′-monophosphate) is the ribonucleotide of the purine base hypoxanthine (6-oxopurine); it is the first intermediate of de novo purine synthesis with a complete purine ring and the common precursor of AMP and GMP.

The purine ring is assembled one or a few atoms at a time on the ribose phosphate (figure below; the steps in Lehninger 8e, Fig. 22-35):

| Step | Enzyme | Atoms added | Cosubstrates |
|---|---|---|---|
| 1 | glutamine–PRPP amidotransferase (committed step) | N9 | Gln → Glu; $\mathrm{PP_i}$ released |
| 2 | GAR synthetase | C4, C5, N7 | glycine, ATP → ADP + $\mathrm{P_i}$ |
| 3 | GAR transformylase | C8 | $N^{10}$-formyl-THF |
| 4 | FGAM synthetase | N3 | Gln, ATP → ADP + $\mathrm{P_i}$ |
| 5 | AIR synthetase (closes the imidazole ring) | — | ATP → ADP + $\mathrm{P_i}$ |
| 6 | AIR carboxylase | C6 | $\ce{HCO3-}$ |
| 7 | SAICAR synthetase | N1 | aspartate, ATP → ADP + $\mathrm{P_i}$ |
| 8 | SAICAR lyase (adenylosuccinate lyase) | — | fumarate released |
| 9 | AICAR transformylase | C2 | $N^{10}$-formyl-THF |
| 10 | IMP cyclohydrolase (closes the six-membered ring) | — | $\ce{H2O}$ released |

Step 1 attaches the amide nitrogen of glutamine to C-1 of PRPP with inversion of configuration: the α-pyrophosphate is replaced by the β-amino group of 5-phosphoribosylamine (PRA), so that the β-N-glycosidic bond of all nucleotides is set at the start. PRA is very unstable (half-life about 30 s at pH 7.5) and is passed directly to GAR synthetase. In step 2 ATP activates the carboxyl group of glycine as an acyl phosphate, which the amino group of PRA attacks; steps 3–5 add a formyl group, a second nitrogen and close the five-membered ring (5-aminoimidazole ribonucleotide, AIR). The carboxylation in step 6 uses bicarbonate without **biotin**. In bacteria and fungi it takes two steps (an ATP-dependent carboxylation of the exocyclic amino group to $N^5$-CAIR, then a rearrangement); in animals AIR carboxylase carboxylates C-4 directly. Aspartate gives N1 in two steps (7 and 8), condensation and elimination of fumarate, exactly as it gives the second nitrogen of urea in the **urea cycle** ([7.1.22](/7.1.22#sec-22.2.1)); the second formyl group and a dehydrative ring closure complete IMP. The intermediate AICAR is also a by-product of histidine synthesis, and its riboside (AICA riboside) is used experimentally as an **activator** of **AMP-activated protein kinase** ([7.1.29](/7.1.29)), because AICAR (ZMP) mimics AMP.

In animals several steps are carried by multifunctional **proteins** (steps 2, 3 and 5 on one **polypeptide**, steps 9 and 10 on another, steps 6 and 7 on a third). When cells are depleted of purines, the six enzymes of the human pathway cluster reversibly into cytoplasmic bodies, *purinosomes*, often near mitochondria, which are thought to channel the unstable intermediates and to couple the pathway to the supply of ATP, glycine and formate from mitochondria; their structure and physiological importance are still being studied.

Cost: from ribose 5-phosphate to IMP the pathway uses six high-energy phosphate bonds (two in PRPP synthesis, Eq. (28.1), since AMP must be rephosphorylated by **adenylate kinase**, and one ATP in each of steps 2, 4, 5 and 7), two glutamines, one glycine, one aspartate, one bicarbonate and two formyl-THF.

![De novo synthesis of purine and pyrimidine ribonucleotides. Left: the purine pathway from ribose 5-phosphate through PRPP and 5-phosphoribosylamine (the committed step of glutamine–PRPP amidotransferase) and nine further steps to IMP, with the cosubstrates of each step on its arc (GAR, FGAR, FGAM, AIR, CAIR, SAICAR, AICAR, FAICAR are the ribonucleotide intermediates); IMP branches to AMP through adenylosuccinate (ADSS, adenylosuccinate synthetase, with aspartate and GTP; ADSL, adenylosuccinate lyase) and to GMP through XMP (IMPDH, IMP dehydrogenase, NAD⁺; GMP synthetase, glutamine and ATP). Right: the pyrimidine pathway from glutamine and bicarbonate through carbamoyl phosphate (CPS II), N-carbamoylaspartate (ATCase) and dihydroorotate (dihydroorotase), which form the trifunctional CAD protein in animals, to orotate (DHODH, in the inner mitochondrial membrane, passing electrons to ubiquinone), OMP and UMP (OPRT and OMP decarboxylase, the two activities of UMP synthase), then UDP, UTP and CTP. Feedback inhibitors and activators of the regulated steps are in red](./plots/nucleotide-de-novo.py)

### 28.2.3. From IMP to AMP and GMP

IMP branches in two two-step routes (figure above):

- AMP: adenylosuccinate synthetase condenses the amino group of aspartate with C-6 of IMP, activated by GTP (as 6-phosphoryl-IMP); adenylosuccinate lyase, the same enzyme as in step 8, eliminates fumarate. Net: IMP + Asp + GTP → AMP + fumarate + GDP + $\mathrm{P_i}$.
- GMP: IMP dehydrogenase oxidizes C-2 with $\ce{NAD+}$ to xanthylate (XMP); GMP synthetase, a **glutamine amidotransferase**, activates the C-2 oxygen as an adenylate (ATP → AMP + $\mathrm{PP_i}$) and replaces it by the amide nitrogen of glutamine. Net: IMP + $\ce{NAD+}$ + Gln + ATP + $\ce{H2O}$ → GMP + NADH + Glu + AMP + $\mathrm{PP_i}$.

The crossed requirement, GTP to make AMP and ATP to make GMP, is itself a regulatory device: whichever purine is in excess drives the synthesis of the other.

### 28.2.4. Feedback Regulation

Four mechanisms set the total rate of purine synthesis and the ratio of the two products (Lehninger 8e, Fig. 22-37, for *E. coli*; the scheme in animals is similar):

1. Glutamine–PRPP amidotransferase, the committed step, is an **allosteric enzyme** inhibited by IMP, AMP and GMP and activated by its **substrate** PRPP. AMP and GMP inhibit synergistically (at different sites): excess of either partly closes the entrance, excess of both closes it fully.
2. At the branch, AMP inhibits adenylosuccinate synthetase and GMP inhibits IMP dehydrogenase, each without affecting the other branch; if both accumulate, IMP accumulates and inhibits the first step, an example of sequential **feedback inhibition** ([7.1.27](/7.1.27)).
3. The reciprocal use of GTP and ATP (28.2.3) balances the two branches.
4. PRPP synthetase is inhibited by ADP and GDP.

In growing animal cells the pathway is also driven by growth signals: the nutrient-sensing kinase complex **mTORC1** ([7.1.29](/7.1.29)) induces, through the **transcription** factor ATF4, the mitochondrial enzyme MTHFD2 that supplies formate for the formyl-THF of steps 3 and 9, and the oncogenic transcription factor Myc induces several enzymes of both pathways.

## 28.3. Pyrimidine Nucleotides

### 28.3.1. Carbamoyl Phosphate and the Committed Step

The pyrimidine ring is made from **carbamoyl phosphate** and aspartate, and only then attached to ribose phosphate. In animals the **carbamoyl phosphate** for pyrimidines and that for urea are made by two different enzymes in two compartments, so that the two pathways can be regulated independently:

**Definition 28.3.1 (Carbamoyl Phosphate Synthetase II)** **Carbamoyl phosphate synthetase II** (CPS II) is the cytosolic enzyme of animals that makes carbamoyl phosphate for pyrimidine synthesis from bicarbonate, the amide nitrogen of glutamine and two ATP:

$$
\ce{Gln} + \ce{HCO3-} + 2\,\ce{ATP} + \ce{H2O} \to \text{carbamoyl phosphate} + \ce{Glu} + 2\,\ce{ADP} + \mathrm{P_i}. \tag{28.2}
$$

It differs from carbamoyl phosphate synthetase I of the **urea cycle**, which is mitochondrial, uses free $\ce{NH4+}$ and requires N-acetylglutamate ([7.1.22](/7.1.22#sec-22.2.4)).

Bacteria have a single carbamoyl phosphate synthetase for arginine and pyrimidines. The *E. coli* enzyme is the classic example of **substrate channeling**: a glutaminase site in the small **subunit** releases $\ce{NH3}$, which travels through a tunnel almost 10 nm long to the first ATP site, where it attacks carboxyphosphate; the carbamate formed travels on to the second ATP site, where it is phosphorylated. The unstable intermediates (ammonia, carboxyphosphate, carbamate) never meet the solvent.

Aspartate transcarbamoylase (ATCase) transfers the carbamoyl group to the amino group of aspartate, giving N-carbamoylaspartate; this is the first step unique to pyrimidines and the committed step in bacteria. *E. coli* ATCase, with six catalytic and six regulatory subunits, inhibited by CTP and activated by ATP, is the textbook **allosteric enzyme** whose kinetics are analyzed in [7.1.9](/7.1.9#sec-9.5.2). Dihydroorotase then closes the ring by removing water (L-dihydroorotate). In animals the first three enzymes, CPS II, ATCase and dihydroorotase, are **domains** of one 243 kDa polypeptide, the **trifunctional protein** CAD, which forms hexamers; the channeling suggests, here too, that **metabolons** are the rule.

### 28.3.2. From Orotate to UMP and CTP

- Dihydroorotate dehydrogenase (DHODH) oxidizes dihydroorotate to orotate. In animals (and in *E. coli*) it is a **flavoprotein** anchored on the outer face of the inner mitochondrial membrane that passes the electrons to **ubiquinone**, and so to the **respiratory chain** and $\ce{O2}$ ([7.1.23](/7.1.23)); it is the only mitochondrial step of the pathway, and the reason why cells without a functional respiratory chain need uridine to grow. DHODH is the target of leflunomide and teriflunomide, used against rheumatoid arthritis and multiple sclerosis, because activated lymphocytes depend on de novo pyrimidine synthesis.
- Orotate phosphoribosyltransferase (OPRT) attaches ribose 5-phosphate from PRPP to N1, giving orotidylate (OMP), and OMP decarboxylase removes the carboxyl group to give UMP. The decarboxylase uses no **cofactor** and accelerates its reaction about $10^{17}$-fold, the largest rate enhancement known ([7.1.8](/7.1.8#sec-8.3.2)). In animals both activities are on one bifunctional protein, UMP synthase; its inherited deficiency (orotic aciduria) causes megaloblastic anemia and is treated with uridine, which bypasses the block through salvage. Orotic acid also appears in the urine when mitochondrial carbamoyl phosphate overflows into the cytosol in ornithine transcarbamoylase deficiency ([7.1.22](/7.1.22#sec-22.2.5)).
- UMP is phosphorylated to UTP (28.4.1), and CTP synthetase aminates UTP at C-4 with glutamine (or, in bacteria, also $\ce{NH4+}$), activating the C-4 oxygen as an acyl phosphate with ATP. Cytidine nucleotides are therefore made only at the triphosphate level.

Cost from ribose 5-phosphate to UMP: four high-energy phosphate bonds (two in CPS II, two in PRPP), partly repaid by the reducing equivalents of DHODH.

### 28.3.3. Regulation

In bacteria the rate is controlled at ATCase: CTP, the end product, binds the regulatory subunits and shifts the enzyme to the **T state** (increasing $K_{0.5}$ for aspartate), and ATP reverses the effect, a signal that purines, and energy, are available to pair with pyrimidines ([7.1.9](/7.1.9#sec-9.5.2)). In animals the regulated step is CPS II, the first step of CAD: UTP (and UDP) inhibit it, PRPP and ATP activate it. CAD is also phosphorylated by growth-factor and nutrient kinases: ERK (MAP kinase, [7.1.15](/7.1.15)) raises its sensitivity to PRPP and lowers that to UTP as cells enter S phase, and S6 kinase, downstream of mTORC1, activates it so that pyrimidine synthesis keeps pace with **ribosome** biogenesis (both effects reversed by **protein kinase A** and phosphatases). Transcriptional control by Myc completes the picture.

## 28.4. Nucleoside Triphosphates and Deoxyribonucleotides

### 28.4.1. NMP and NDP Kinases

Nucleotides are used in **biosynthesis** as triphosphates (RNA and **DNA polymerases**, CTP for phospholipids, UTP for **sugar nucleotides**). Two classes of kinases convert them:

- Nucleoside monophosphate kinases are specific for the base but not for the sugar: ATP + (d)NMP ⇌ ADP + (d)NDP. **Adenylate kinase** is the one for AMP; UMP–CMP kinase, guanylate kinase and thymidylate kinase handle the others. Rapid rephosphorylation of ADP by **ATP synthase** pulls these reactions forward.
- **Nucleoside diphosphate kinase**, one nonspecific enzyme, converts every (d)NDP to the (d)NTP by a **ping-pong mechanism** through a phosphohistidine: $\mathrm{NTP_D} + \mathrm{NDP_A} \rightleftharpoons \mathrm{NDP_D} + \mathrm{NTP_A}$, with ATP as the usual donor because it is the most abundant triphosphate ([7.1.16](/7.1.16#sec-16.3.5)).

### 28.4.2. Ribonucleotide Reductase

All four DNA precursors are made by reduction of ribonucleotides at C-2′, a reduction at an unactivated carbon for which organic chemistry offers no close analog.

**Definition 28.4.1 (Ribonucleotide Reductase)** **Ribonucleotide reductase** (RNR) is the enzyme that reduces ribonucleotides (in *E. coli* and mammals, the four ribonucleoside diphosphates) to the corresponding 2′-deoxyribonucleotides by a **free radical** mechanism; the electrons come ultimately from NADPH, through thioredoxin (reduced by the flavoprotein thioredoxin reductase) or through glutaredoxin (reduced by glutathione):

$$
\text{NDP} + \text{thioredoxin}(\ce{SH})_2 \to \text{dNDP} + \text{thioredoxin}(\ce{S-S}) + \ce{H2O}. \tag{28.3}
$$

The class I enzyme of *E. coli* and of mammals is an $\alpha_2\beta_2$ complex (figure below). The α subunits (R1; RRM1 in humans) contain the **active sites**, with three essential cysteines, and two kinds of allosteric site; the β subunits (R2; RRM2) contain a diferric centre ($\ce{Fe^3+}$–O–$\ce{Fe^3+}$) that reacts with $\ce{O2}$ to generate a stable tyrosyl radical on Tyr122 and keeps it stable for days. Tyr122 lies about 3.5 nm from the active site; each time a substrate binds, the radical travels to Cys439 of α along a chain of aromatic **residues** by proton-coupled electron transfer, and returns after the reaction. The proposed mechanism (Stubbe):

1. the thiyl radical of Cys439 abstracts the 3′-hydrogen of the ribose;
2. the 3′-radical promotes the loss of the 2′-hydroxyl as water, protonated by Cys225 (the 3′ radical stabilizes the developing cation at C-2′, which becomes a 3′-keto radical);
3. Cys225 and Cys462 deliver the two electrons and the proton that reduce C-2′, forming a disulfide;
4. Cys439 returns the 3′-hydrogen, the radical goes back to Tyr122, and the dNDP leaves; the disulfide is reduced by a pair of cysteines at the flexible C-terminus, which in turn are reduced by **thioredoxin**.

Three classes of RNR differ in how they generate the radical, and are distributed according to the oxygen supply of the organism:

| Class | Radical generator | Oxygen | Substrates | Found in |
|---|---|---|---|---|
| I | diferric (or dimanganese, Mn–Fe) centre and a tyrosyl radical in β | requires $\ce{O2}$ | NDP | **eukaryotes**, many aerobic bacteria |
| II | 5′-deoxyadenosylcobalamin (coenzyme $\mathrm{B_{12}}$) | independent | NDP or NTP | many bacteria and archaea |
| III | glycyl radical installed by an S-adenosylmethionine-dependent radical activase, with an Fe–S cluster | killed by $\ce{O2}$ | NTP; formate or thioredoxin as reductant | strict and facultative anaerobes (*E. coli* when anaerobic) |

The common mechanism (a cysteine thiyl radical abstracting the 3′-hydrogen) and the different, environment-specific ways of making the radical suggest that all three descend from one ancestor that arose before the atmosphere became oxic.

![Class I ribonucleotide reductase and its regulatory logic. Left: the α₂β₂ enzyme (E. coli numbering). Each α subunit carries the active site, where Cys439 becomes a thiyl radical, the specificity site (S) at the α–α interface, and the activity site (A) in the N-terminal ATP cone; each β subunit contains a diferric centre that generates the Tyr122 radical, which is transferred about 3.5 nm to Cys439 at each turnover; electrons come from NADPH through thioredoxin or glutaredoxin. Right: at the activity site ATP activates and dATP inactivates all four reductions (in E. coli dATP induces inactive α₄β₄ rings); at the specificity site ATP or dATP favours reduction of CDP and UDP, dTTP favours GDP and dGTP favours ADP, so that each product calls for the next](./plots/rnr-regulation.py)

### 28.4.3. Allosteric Regulation of Ribonucleotide Reductase

One active site makes four products in proportions that must match the composition of DNA; imbalances of the dNTP pools are mutagenic, because DNA polymerases then misincorporate the excess nucleotide. RNR solves this with two kinds of allosteric site, one regulating total activity and one regulating specificity:

| Site | Effector bound | Effect |
|---|---|---|
| activity site (ATP cone) | ATP | activates all reductions |
| | dATP | inactivates the enzyme (*E. coli*: α₄β₄ rings in which the radical pathway is broken; human: α₆ rings) |
| specificity site | ATP or dATP | favours reduction of CDP and UDP |
| | dTTP | favours GDP (and suppresses CDP and UDP) |
| | dGTP | favours ADP |

The scheme is a sequence: with ATP bound, the enzyme makes the pyrimidine dNTPs; dTTP accumulating at the specificity site switches it to GDP; dGTP switches it to ADP; and dATP, finally, binds the activity site and turns the enzyme off. Every pool thus turns the enzyme toward a pool that is still low, and the final product of the sequence shuts everything down.

**Example 28.4.1 (A Model of dNTP Pool Balance)** Let $a, c, g, t$ be the concentrations of dATP, dCTP, dGTP and dTTP. The four effectors at the specificity site compete for one site, so the fraction of enzyme with effector $X$ bound is $f_X = w_X/(1 + \sum_Y w_Y)$ with weights $w_{\mathrm{ATP}} = [\mathrm{ATP}]/K_{\mathrm{ATP}}$ (taken as 1, since ATP is constant), $w_{\mathrm{dATP}} = a/K_a$, $w_{\mathrm{dTTP}} = t/K_t$, $w_{\mathrm{dGTP}} = g/K_g$. dATP at the activity site leaves a fraction $\phi(a) = 1/(1 + (a/K_I)^2)$ of the enzyme active. With maximal flux $V$, the production rates are

$$
\begin{aligned}
v_C + v_T &= V\phi(a)\,(f_{\mathrm{ATP}} + f_{\mathrm{dATP}}), \qquad v_G = V\phi(a)\,f_{\mathrm{dTTP}}, \qquad v_A = V\phi(a)\,f_{\mathrm{dGTP}},
\end{aligned}
\tag{28.4}
$$
and each pool is consumed by DNA synthesis in proportion to its share $p_X$ of the DNA composition, $\mathrm{d}x/\mathrm{d}t = v_X - D\,p_X\,x/(K + x) - k x$. The parameters (figure below) are illustrative: $K_a = K_g = 2\,\mu\mathrm{M}$, $K_t = 5\,\mu\mathrm{M}$, $K_I = 30\,\mu\mathrm{M}$, $V = 40\,\mu\mathrm{M\,min^{-1}}$, $D = 10\,\mu\mathrm{M\,min^{-1}}$. Starting from empty pools, the four dNTPs settle within about 20 minutes at concentrations of tens of micromolar, close to those measured in proliferating cells, with no pool running away. Adding a constant influx of dATP, as in adenosine deaminase deficiency (28.5.4), raises dATP until the activity site closes, and the three other pools fall by one to two orders of magnitude; adding thymidine raises dTTP, which shifts the specificity toward GDP, and dCTP falls. Both effects are seen in cells: the first kills T lymphocytes in ADA-SCID, the second is the "thymidine block" used to arrest cultured cells at the beginning of S phase.

![Simulation of the model of Example 28.4.1. (A) Starting from empty pools, the feedback loops of the specificity and activity sites bring the four dNTPs to a balanced steady state within about 20 minutes. (B) Steady-state pools against an extra influx of dATP from deoxyadenosine, as in adenosine deaminase deficiency: above a threshold dATP shuts the enzyme down at the activity site and dGTP, dCTP and dTTP collapse (logarithmic scale). (C) Steady-state pools against an extra influx of dTTP from thymidine: dTTP shifts the specificity site toward GDP, dGTP rises and dCTP falls, which stops DNA replication (the thymidine block)](./plots/rnr-pool-model.py)

In mammals the supply of dNTPs is coupled to the cell cycle also by the amount of enzyme: the R2 subunit is made in S phase and degraded in mitosis, and a p53-inducible R2 variant (p53R2) supplies dNTPs for repair in resting cells ([7.2.8](/7.2.8)). Hydroxyurea, which scavenges the tyrosyl radical, and gemcitabine, a difluoro analog of deoxycytidine whose diphosphate inactivates the enzyme, are used against cancer.

### 28.4.4. Thymidylate

DNA contains thymine instead of uracil, and the pathway to thymine involves only deoxyribonucleotides. The precursor of dTMP is dUMP, which comes from dUTP (made from dUDP by NDP kinase, or in bacteria by **deamination** of dCTP) by the action of dUTPase, or in animals mainly from dCMP by dCMP deaminase. dUTPase hydrolyzes dUTP to dUMP and $\mathrm{PP_i}$ and so keeps the dUTP pool very low; otherwise DNA polymerases, which do not distinguish uracil from thymine, would incorporate it.

**Definition 28.4.2 (Thymidylate Synthase and Dihydrofolate Reductase)** **Thymidylate synthase** methylates dUMP at C-5 to dTMP with $N^5,N^{10}$-methylenetetrahydrofolate, which supplies both the one-carbon unit (at the formaldehyde level of oxidation) and, from C-6 of its pteridine ring, the hydride that reduces it to a methyl group, and therefore leaves as 7,8-dihydrofolate (DHF):

$$
\text{dUMP} + N^5,N^{10}\text{-methylene-THF} \to \text{dTMP} + \text{DHF}; \tag{28.5}
$$
then **dihydrofolate reductase** (DHFR) regenerates **tetrahydrofolate** from DHF with **NADPH**. Serine hydroxymethyltransferase (SHMT) then reloads THF with a methylene group from the β carbon of serine (giving glycine), which closes the thymidylate cycle (figure below).

Thymidylate synthase is unusual among THF-dependent enzymes in oxidizing its cofactor, and the cell's whole folate pool would be trapped as DHF without DHFR; the cycle is therefore the only de novo route to thymine and one of the best drug targets in medicine. The mechanism: an active-site cysteine (Cys146 in *E. coli*) adds to C-6 of dUMP, making C-5 nucleophilic; C-5 attacks the iminium ion formed by the opened methylene-THF, giving a covalent enzyme–dUMP–folate ternary complex; abstraction of the C-5 proton eliminates THF and leaves an exocyclic methylene, which receives a hydride from C-6 of the tetrahydropteridine; the enzyme is released by elimination of the cysteine. In plants and in protists (*Plasmodium*, *Leishmania*) TS and DHFR are domains of one bifunctional protein that channels DHF between them.

![The thymidylate cycle and its inhibitors. dUMP is made from dUDP or (in bacteria) dCTP through dUTP, which dUTPase hydrolyzes, or (in animals) from dCMP by dCMP deaminase; thymidine is salvaged by thymidine kinase. Thymidylate synthase (TS) transfers a one-carbon unit and a hydride from N⁵,N¹⁰-methylenetetrahydrofolate to dUMP, giving dTMP and dihydrofolate (DHF); dihydrofolate reductase (DHFR) reduces DHF to tetrahydrofolate (THF) with NADPH, and serine hydroxymethyltransferase (SHMT) regenerates methylene-THF from serine. TS is blocked by FdUMP, formed from 5-fluorouracil, and by the antifolates raltitrexed and pemetrexed; DHFR by methotrexate and aminopterin, the bacterial enzyme selectively by trimethoprim](./plots/thymidylate-cycle.py)

Folate deficiency, probably the most common **vitamin** deficiency worldwide, slows thymidylate synthesis. Uracil is then misincorporated into DNA, and its removal by uracil-DNA glycosylase in **base-excision repair** ([7.2.8](/7.2.8#sec-8.2.2)) produces repeated strand breaks; the result is megaloblastic anemia (large, immature red-cell precursors that cannot complete replication), an increased risk of neural tube defects in the fetus, and perhaps of cancer. For this reason flour is fortified with folic acid in many countries.

**Remark 28.4.1** Ribonucleotide reductase and thymidylate synthase are the two reactions that distinguish DNA from RNA chemically, and in every organism they act on ribonucleotides and on the uracil nucleotide already made: deoxyribonucleotides are made from ribonucleotides, and thymine from uracil, never the other way around. This order of biosynthesis is one of the arguments that RNA preceded DNA as the genetic material, and that the radical chemistry of RNR was the step that allowed a stable DNA archive ([7.2.23](/7.2.23#sec-23.4.2)).

## 28.5. Degradation and Salvage

### 28.5.1. Purines Are Degraded to Uric Acid

Nucleic acids of the diet are hydrolyzed in the intestine by nucleases and **phosphodiesterases** to nucleotides, and these to nucleosides and bases; those of the cells are recycled as they turn over. Purine nucleotides lose their phosphate by 5′-nucleotidases (figure below). Adenosine is deaminated to inosine by adenosine deaminase (ADA), so that the amino group of adenine is removed before the ribose; in muscle, AMP deaminase removes it at the nucleotide level (IMP). Purine nucleoside phosphorylase (PNP) cleaves inosine and guanosine by **phosphorolysis**, giving hypoxanthine and guanine and ribose 1-phosphate (which is recycled through the **pentose phosphate pathway**). Guanine is deaminated to xanthine, so that the guanine amino group is removed after the ribose.

**Definition 28.5.1 (Xanthine Oxidase and Uric Acid)** **Xanthine oxidase** (xanthine oxidoreductase) is the enzyme of liver and intestine that hydroxylates hypoxanthine to xanthine and xanthine to **uric acid** (2,6,8-trioxopurine), the end product of purine catabolism in humans; it is a homodimer each of whose subunits contains a molybdenum (molybdopterin) cofactor, at which the substrate is hydroxylated with oxygen from water, two [2Fe–2S] centres and FAD, which pass the electrons to $\ce{O2}$ (giving $\ce{H2O2}$ and superoxide) or, in its dehydrogenase form, to $\ce{NAD+}$.

Uric acid ($\mathrm{p}K_{\mathrm{a}} \approx 5.4$) is present at pH 7.4 almost entirely as the urate ion. A healthy adult excretes about 0.6 g per day, partly from dietary purines and partly from turnover. Most mammals degrade urate further, and the extent of degradation follows the availability of water, as for the excretion of amino nitrogen ([7.1.22](/7.1.22#sec-22.1.1)):

| End product | Further enzyme | Excreted by |
|---|---|---|
| uric acid | — | primates (humans and apes), birds, reptiles, insects |
| allantoin | urate oxidase (uricase) | most other mammals, some reptiles and gastropods |
| allantoate | allantoinase | bony fishes |
| urea + glyoxylate | allantoicase | amphibians, cartilaginous fishes |
| $\ce{NH4+}$ + $\ce{CO2}$ | urease | marine invertebrates |

Birds, reptiles and insects excrete all their surplus nitrogen as uric acid, made by the purine pathway from glycine, glutamine and aspartate; humans make only the uric acid of purine turnover, and excrete most of their nitrogen as urea. Hominoid apes lost urate oxidase by several independent mutations in the Miocene; their serum urate (about 0.2–0.4 mM) is close to the solubility limit of sodium urate (about 0.4 mM, 6.8 mg/dL, at 37 °C), and among the explanations proposed is the antioxidant activity of urate.

![Catabolism of purine nucleotides and the salvage of their bases. AMP is dephosphorylated to adenosine by 5′-nucleotidase and deaminated to inosine by adenosine deaminase, or first deaminated to IMP by AMP deaminase; purine nucleoside phosphorylase (PNP) cleaves inosine and guanosine by phosphorolysis to hypoxanthine and guanine and ribose 1-phosphate; guanine deaminase converts guanine to xanthine; xanthine oxidase oxidizes hypoxanthine to xanthine and xanthine to uric acid with O₂, the steps blocked by allopurinol (through oxypurinol) and febuxostat. On the right, the further degradation of uric acid by urate oxidase, allantoinase, allantoicase and urease, with the animals for which each product is the excreted form. Dashed green arrows: salvage of hypoxanthine and guanine to IMP and GMP by hypoxanthine–guanine phosphoribosyltransferase (HGPRT) with PRPP](./plots/purine-degradation.py)

### 28.5.2. Pyrimidines Are Degraded to β-Amino Acids

The pyrimidine ring, unlike the purine ring, is opened and its carbons are recovered. Cytidine is deaminated to uridine, and uridine and thymidine are cleaved by phosphorylases to uracil and thymine. Dihydropyrimidine dehydrogenase (DPD) reduces the ring with NADPH, dihydropyrimidinase opens it, and β-ureidopropionase releases $\ce{NH4+}$ and $\ce{CO2}$ (the ammonia ends in urea):

- uracil (and cytosine) → β-alanine → malonate semialdehyde → acetyl-CoA (or **malonyl-CoA**);
- thymine → β-aminoisobutyrate → methylmalonate semialdehyde → propionyl-CoA → methylmalonyl-CoA → succinyl-CoA, a **citric acid cycle** intermediate (the route of odd-chain **fatty acids**, through **methylmalonyl-CoA mutase**, [7.1.21](/7.1.21#sec-21.4.2)).

These pathways contribute little energy: nucleotides are a poor fuel, because their rings are already partly oxidized and rich in nitrogen. They matter in pharmacology: DPD degrades about 80% of an administered dose of 5-fluorouracil, and patients with DPD deficiency (a few percent of Europeans carry reduced-function *DPYD* alleles) suffer severe, sometimes fatal, toxicity from standard doses, for which they are now genotyped before treatment.

### 28.5.3. Salvage Pathways

Free purines released by degradation are largely salvaged in one step by phosphoribosyltransferases that use PRPP, a far cheaper route than de novo synthesis:

$$
\text{base} + \text{PRPP} \to \text{NMP} + \mathrm{PP_i}. \tag{28.6}
$$

Adenine phosphoribosyltransferase (APRT) salvages adenine to AMP; hypoxanthine–guanine phosphoribosyltransferase (HGPRT) salvages hypoxanthine to IMP and guanine to GMP. Mammals do not salvage pyrimidine bases to a significant extent, but they phosphorylate pyrimidine (and purine) nucleosides with nucleoside kinases: uridine–cytidine kinase, thymidine kinase (TK1, cytosolic and S-phase-specific; TK2, mitochondrial) and deoxycytidine kinase, which also activates many nucleoside drugs.

The salvage enzymes are the basis of a classic selection method. In HAT medium (hypoxanthine, aminopterin, thymidine), aminopterin blocks DHFR and with it de novo synthesis of purines and thymidylate, so only cells with both HGPRT and thymidine kinase survive, using the supplied hypoxanthine and thymidine. Fusing HGPRT-deficient myeloma cells with spleen B cells and growing them in HAT selects hybridomas, the source of **monoclonal antibodies** ([7.1.7](/7.1.7)).

**Definition 28.5.2 (Lesch–Nyhan Syndrome)** **Lesch–Nyhan syndrome** is the X-linked inherited deficiency of HGPRT (gene *HPRT1*), seen almost only in boys, in which the failure to salvage hypoxanthine and guanine raises PRPP, accelerates de novo purine synthesis and causes overproduction of uric acid, with gout and kidney stones, together with severe neurological disease: poor motor control, intellectual disability and compulsive self-injury (biting of lips and fingers).

Allopurinol (below) controls the uric acid but not the neurological symptoms, which probably arise from a disturbance of the dopaminergic neurons of the basal ganglia during development; the brain depends especially on salvage, and partial HGPRT deficiency causes gout without the neurological signs.

### 28.5.4. Immunodeficiency and Gout

Two inherited defects of purine degradation selectively kill lymphocytes, which have high activities of deoxynucleoside kinases and low activities of the nucleotidases that would remove deoxynucleotides:

- Adenosine deaminase deficiency causes about 10–15% of cases of severe combined immunodeficiency (ADA-SCID), in which T and B lymphocytes fail to develop. Deoxyadenosine from DNA turnover is phosphorylated in lymphocytes, dATP rises about 100-fold and inhibits ribonucleotide reductase at its activity site (Example 28.4.1), so that the other dNTPs are depleted and DNA cannot be replicated; deoxyadenosine also inactivates S-adenosylhomocysteine hydrolase. Treatment: bone marrow transplantation, enzyme replacement with polyethylene glycol-conjugated ADA, and **gene** therapy. ADA-SCID was the target of the first human gene therapy trial (1990), and an ex vivo gene therapy of autologous stem cells was approved in Europe in 2016.
- Purine nucleoside phosphorylase deficiency raises dGTP in T cells and causes a T-cell immunodeficiency.

**Definition 28.5.3 (Gout)** **Gout** is the disease caused by persistently elevated urate in the blood (hyperuricemia, above about 0.4 mM), in which crystals of monosodium urate deposit in joints, where they trigger acute, very painful inflammation (by activating the NLRP3 inflammasome of macrophages), in tissues (tophi) and in the kidney tubules (stones and nephropathy).

Gout occurs predominantly in men; its old association with "high living" is only partly right. In about 90% of patients the cause is underexcretion of urate by the kidney, in which urate **transporters** (URAT1, GLUT9 and ABCG2) are major genetic determinants, and overproduction (PRPP synthetase superactivity, partial HGPRT deficiency, high cell turnover in leukemias and after chemotherapy, a diet rich in purines, fructose and alcohol) accounts for the rest. The drug allopurinol, developed by Gertrude Elion and George Hitchings, is an isomer of hypoxanthine (structure 2 below, beside hypoxanthine 1) and a substrate of xanthine oxidase, which converts it to oxypurinol (alloxanthine); oxypurinol binds very tightly to the reduced molybdenum centre and inactivates the enzyme, a mechanism-based inhibition. The excreted purines are then hypoxanthine and xanthine, the first of which is much more soluble than uric acid; xanthine is less soluble, which explains the occasional xanthine stones of treated patients (Question 4). Febuxostat, a non-purine inhibitor of xanthine oxidase, uricosuric drugs that block URAT1 (probenecid), and recombinant urate oxidases (rasburicase, pegloticase, used against the tumor lysis syndrome and refractory gout) are the alternatives; colchicine and anti-inflammatory drugs treat the acute attack.

```smiles
O=c1[nH]cnc2[nH]cnc12 1
O=c1[nH]cnc2[nH]ncc12 2
O=c1cc[nH]c(=O)[nH]1 3
O=c1[nH]cc(F)c(=O)[nH]1 4
```

Elion and Hitchings, who shared the 1988 Nobel Prize in Physiology or Medicine with James Black, designed drugs by systematically modifying the bases of nucleic acids: besides allopurinol, 6-mercaptopurine and 6-thioguanine against leukemia, azathioprine for immunosuppression, trimethoprim (with sulfamethoxazole) against bacteria, pyrimethamine against malaria, and acyclovir against herpesviruses, which is activated only in infected cells because only the viral thymidine kinase phosphorylates it.

## 28.6. Chemotherapeutic Targets

Cancer cells, activated lymphocytes, bacteria and parasites that proliferate rapidly need nucleotides faster than most normal cells, and depend more on de novo synthesis; inhibitors of the pathways are therefore among the oldest and most widely used drugs. Uracil (3, above) and 5-fluorouracil (4) illustrate the commonest strategy, a minimal change of a natural substrate.

| Drug | Target | Mechanism | Use |
|---|---|---|---|
| azaserine, acivicin, 6-diazo-5-oxo-L-norleucine | glutamine amidotransferases (Gln–PRPP amidotransferase, FGAM synthetase, CPS II, CTP and GMP synthetases) | glutamine analogs that alkylate the active-site cysteine | experimental (toxic) |
| 6-mercaptopurine, 6-thioguanine, azathioprine | Gln–PRPP amidotransferase, IMP dehydrogenase; DNA | converted by HGPRT to thio-IMP and thio-GMP, which act as feedback inhibitors and are incorporated into DNA | acute lymphoblastic leukemia; immunosuppression |
| mycophenolic acid | IMP dehydrogenase | uncompetitive inhibitor; lymphocytes depend on de novo GMP synthesis | transplantation, autoimmune disease |
| leflunomide, teriflunomide | DHODH | blocks pyrimidine synthesis | rheumatoid arthritis, multiple sclerosis |
| hydroxyurea | RNR (β subunit) | scavenges the tyrosyl radical | myeloproliferative disease; sickle cell disease (raises fetal hemoglobin) |
| gemcitabine | RNR; DNA | difluoro-dCDP inactivates RNR; difluoro-dCTP terminates DNA chains | pancreatic, lung cancer |
| 5-fluorouracil, capecitabine | thymidylate synthase | converted by salvage to FdUMP, a **suicide inactivator** | colorectal, breast, head and neck cancers |
| methotrexate, aminopterin | DHFR | folate analogs, **competitive inhibition** with picomolar **dissociation constants** | leukemia, choriocarcinoma; rheumatoid arthritis (low dose) |
| pemetrexed, raltitrexed | thymidylate synthase (pemetrexed also DHFR, GAR transformylase) | antifolates | mesothelioma, lung cancer |
| trimethoprim | bacterial DHFR | binds the bacterial enzyme about $10^5$ times more tightly than the human enzyme | urinary and other infections (with sulfamethoxazole) |

5-Fluorouracil is a prodrug. Salvage enzymes convert it to the nucleotide FdUMP, which thymidylate synthase accepts: the active-site cysteine adds to C-6 and the covalent ternary complex with methylene-THF forms normally, but the next step, removal of the proton at C-5, is impossible because C-5 carries fluorine, and the complex is trapped; the enzyme inactivates itself, a classic mechanism-based (suicide) inactivation. Leucovorin (5-formyl-THF), given with 5-fluorouracil, stabilizes this ternary complex and enhances the effect. Methotrexate binds DHFR orders of magnitude more tightly than dihydrofolate; high doses are given with leucovorin "rescue", which supplies reduced folate to normal cells after a few hours. The selectivity of all these drugs is only quantitative, a matter of the faster growth of the target cells, and their side effects (anemia, mucositis, immunosuppression, hair loss) are in tissues that also renew rapidly.

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | De novo purine synthesis | De novo pyrimidine synthesis |
|---|---|---|
| Location | cytosol of all cells (liver in particular); enzymes in purinosomes | cytosol (CAD, UMP synthase); DHODH in the inner mitochondrial membrane |
| Net reaction | ribose 5-P + 2 Gln + Gly + Asp + 2 formyl-THF + $\ce{HCO3-}$ → IMP (Eq. (28.1), table in 28.2.2) | Gln + $\ce{HCO3-}$ + Asp + PRPP → UMP (Eq. (28.2)) |
| Energy account | 6 high-energy phosphates to IMP; AMP +1 GTP, GMP +2 ATP equivalents | 4 high-energy phosphates to UMP; DHODH electrons to **ubiquinone** |
| Committed and regulated steps | PRPP synthetase; Gln–PRPP amidotransferase (committed); adenylosuccinate synthetase and IMP dehydrogenase at the branch | CPS II (animals) or ATCase (bacteria) |
| Activators | PRPP (amidotransferase) | PRPP, ATP (CPS II); ATP (bacterial ATCase) |
| Inhibitors | IMP, AMP, GMP (synergistic); AMP ⊣ adenylosuccinate synthetase; GMP ⊣ IMPDH; ADP, GDP ⊣ PRPP synthetase | UTP, UDP (CPS II); CTP (bacterial ATCase) |
| Covalent, hormonal and transcriptional control | mTORC1–ATF4 (MTHFD2, formyl-THF); Myc | ERK and S6K phosphorylate CAD; Myc |
| Opposing pathway | degradation to uric acid (5′-nucleotidase, ADA, PNP, xanthine oxidase); salvage by HGPRT, APRT | degradation to β-alanine and β-aminoisobutyrate (DPD) |
| Coenzymes (vitamins) | THF (folate) | **FMN**, ubiquinone (DHODH) |
| Diseases and drugs | PRPP synthetase superactivity; Lesch–Nyhan; ADA-SCID; gout (allopurinol); 6-mercaptopurine, mycophenolate, antifolates | orotic aciduria; leflunomide; 5-FU, methotrexate (thymidylate) |

| Topic | Key points |
|---|---|
| Logic (28.1) | de novo vs salvage (Definition 28.1.1); PRPP (Definition 28.1.2) donates ribose 5-P; free bases are not intermediates; Gln is the main N donor; pools small |
| Purines (28.2) | ring atoms: N1 Asp, C2 and C8 formyl-THF, N3 and N9 Gln, C4 C5 N7 Gly, C6 $\ce{HCO3-}$; ten steps to IMP (Definition 28.2.1); IMP → AMP (Asp, GTP), → GMP (NAD⁺, Gln, ATP); four feedback controls |
| Pyrimidines (28.3) | CPS II (Definition 28.3.1, Eq. (28.2)) → ATCase → dihydroorotase (CAD) → DHODH (Q) → OPRT + OMP decarboxylase (UMP synthase) → UMP → UTP → CTP; control at CPS II (animals) or ATCase (bacteria) |
| Triphosphates (28.4.1) | base-specific NMP kinases; nonspecific NDP kinase (ping-pong) |
| RNR (28.4.2–28.4.3) | NDP → dNDP with electrons from NADPH via thioredoxin (Definition 28.4.1, Eq. (28.3)); Tyr122 radical, radical transfer to Cys439, 3′-H abstraction; classes I–III; activity site ATP+/dATP−; specificity site ATP/dATP → CDP, UDP; dTTP → GDP; dGTP → ADP (Example 28.4.1) |
| Thymidylate (28.4.4) | dUTPase; TS with methylene-THF as C₁ donor and reductant → DHF; DHFR, SHMT (Definition 28.4.2, Eq. (28.5)); folate deficiency |
| Degradation (28.5.1–28.5.2) | purines → uric acid via ADA, PNP, xanthine oxidase (Definition 28.5.1); species differences; pyrimidines → β-alanine, β-aminoisobutyrate → acetyl-CoA, succinyl-CoA; DPD and 5-FU toxicity |
| Salvage and disease (28.5.3–28.5.4) | APRT, HGPRT, nucleoside kinases; HAT selection; Lesch–Nyhan (Definition 28.5.2); ADA-SCID (dATP ⊣ RNR); gout (Definition 28.5.3), allopurinol → oxypurinol |
| Drugs (28.6) | glutamine analogs; thiopurines; mycophenolate; leflunomide; hydroxyurea, gemcitabine; 5-FU (suicide inactivation of TS); methotrexate, pemetrexed, trimethoprim |

## Questions

1. Which atoms of the purine ring come from the amide nitrogen of glutamine? Predict where the label appears in uric acid excreted by a pigeon fed [¹⁵N-amide]glutamine, and in UMP of cells grown with [4-¹⁴C]aspartate.

   **Answer** Glutamine amide gives N3 and N9 of the purine ring (step 1, attached to PRPP, and step 4, FGAM synthetase), so the label appears at N3 and N9 of uric acid. In pyrimidines aspartate supplies N1, C4, C5 and C6; its C-4 (the β-carboxyl) becomes C-4 of the ring, which bears the carbonyl of UMP. (Its C-1, the α-carboxyl, becomes the carboxyl of orotate, which OMP decarboxylase removes as $\ce{CO2}$, so [1-¹⁴C]aspartate would label orotate but not UMP.)

2. Calculate the number of high-energy phosphate bonds needed to make one AMP and one GMP from ribose 5-phosphate, and compare with the cost of salvaging adenine and guanine.

   **Answer** IMP costs 6 (Eq. (28.1) counts 2 because AMP is rephosphorylated by adenylate kinase; then one ATP in each of steps 2, 4, 5 and 7). AMP: +1 (GTP → GDP) = 7. GMP: +2 (ATP → AMP + PPᵢ, counted as 2) = 8. Salvage by APRT or HGPRT costs only the PRPP, 2 high-energy bonds per nucleotide, and no glutamine, glycine, aspartate or folate. This is why salvage is preferred whenever bases are available, and why its failure (Lesch–Nyhan) is felt in tissues with little capacity for de novo synthesis such as the brain.

3. Patients with adenosine deaminase deficiency have high dATP in their lymphocytes. Explain, using the regulation of ribonucleotide reductase, why this blocks DNA synthesis, and why it does not simply give the cells an excess of one DNA precursor.

   **Answer** dATP binds the activity site (the ATP cone) of RNR, which inactivates the enzyme for all four substrates. The reduction of CDP, UDP and GDP stops, so dCTP, dTTP and dGTP are depleted, and replication stops for lack of three precursors even though one is in excess (Example 28.4.1, figure B). The block cannot be bypassed because RNR is the only source of deoxyribonucleotides other than salvage, which itself depends on deoxynucleosides that the lymphocytes do not have in excess except deoxyadenosine. Lymphocytes are hit selectively because they phosphorylate deoxyadenosine actively and dephosphorylate dAMP poorly.

4. A patient with gout treated with allopurinol develops xanthine stones. The solubilities in urine are: uric acid 0.15 g/L, xanthine 0.05 g/L, hypoxanthine 1.4 g/L. Explain the benefit of the drug and the side effect.

   **Answer** Allopurinol, converted to oxypurinol, inhibits xanthine oxidase at both steps, so the purines are excreted as hypoxanthine and xanthine instead of uric acid. Because the excretion is divided between two compounds, each is below the concentration uric acid would have reached; hypoxanthine is about ten times more soluble than uric acid, and part of it is salvaged by HGPRT and never excreted, which also lowers de novo synthesis through feedback. But xanthine is even less soluble than uric acid; when its concentration in urine exceeds 0.05 g/L (high doses, high purine turnover, little water, or HGPRT deficiency, when hypoxanthine cannot be salvaged), it precipitates. The overall risk of stones is still lower than in untreated gout.

5. Folic acid deficiency causes megaloblastic anemia, and methotrexate causes the same picture. Explain the link with DNA synthesis, and why leucovorin (5-formyl-THF) but not folic acid rescues normal cells after a high dose of methotrexate.

   **Answer** Thymidylate synthase converts methylene-THF to DHF in each turnover, and only DHFR returns it to THF. Without folate (or with DHFR blocked) the THF pool is trapped as DHF or depleted, the formyl-THF for purine synthesis and the methylene-THF for thymidylate are lacking, and dTTP falls; uracil is misincorporated and excised, replication stalls, and the rapidly dividing red-cell precursors grow without dividing (megaloblasts). Folic acid itself must be reduced by DHFR (to DHF and then THF) before it can be used, so it is useless when DHFR is inhibited; leucovorin is already at the THF level and enters the folate cycle beyond the block, replenishing reduced folates in normal tissues.

6. (Open question) Why does every organism make deoxyribonucleotides by reducing ribonucleotides, using an enzyme with radical chemistry that requires oxygen, **cobalamin** or a radical **SAM** enzyme, instead of making deoxyribose first and building nucleotides on it? Discuss in terms of chemistry, evolution and regulation.

   **Answer** Outline: (1) Chemistry: removing a hydroxyl from a secondary alcohol without activation is extremely difficult; a 3′-radical lowers the barrier for loss of the 2′-OH, and only radical chemistry achieves this under physiological conditions, which explains the convergence of three classes on one mechanism with different radical generators. (2) Evolution: if RNA preceded DNA, deoxyribonucleotides had to be derived from the existing ribonucleotides; an independent pathway to deoxyribose would have required a second full set of nucleotide-building enzymes; the order ribonucleotide → deoxyribonucleotide, uracil → thymine (Remark 28.4.1) is a molecular fossil of that history. (3) Regulation: routing all four DNA precursors through one enzyme with two allosteric sites lets the cell balance the pools against each other and couple their total supply to the cell cycle (R2 synthesis in S phase), which a set of four independent pathways could do only with extra cross-regulation. A good answer also notes that deoxyribose 5-phosphate aldolase exists, but works in the degradative direction.
