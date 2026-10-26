---
title: Chromatin Regulation and Epigenetics
description: Repression by nucleosomes and H1 and antirepression by activators; histone modifications, their writers, erasers and readers (bromodomain, chromodomain), the identification of HATs by activity gels; deacetylases and corepressor complexes (Sin3, NCoR/SMRT, Mad–Max); the steady state of acetylation; ATP-dependent remodeling complexes (SWI/SNF, ISWI, CHD, INO80); ordered recruitment at the IFN-β promoter and the status of the histone-code hypothesis; heterochromatin and silencing (SIR proteins and telomere position effect, H3K9 methylation and HP1, Polycomb); a quantitative model of epigenetic memory by read–write feedback; DNA methylation, CpG islands, maintenance and de novo methylases, TET-mediated demethylation and bisulfite and bisulfite-free sequencing; inheritance and cross-talk of chromatin marks; transcription through nucleosomes and FACT.
---

[7.2.4](/7.2.4) described chromatin as a structure: the **nucleosome**, its positioning, the fibers, loops and domains above it, and the variants and remodelers that change it. This chapter treats chromatin as a regulatory system. It begins with the observation that nucleosomes repress transcription and that activators counteract this repression, then follows the enzymes that write, erase and read covalent marks on histones and DNA, the ATP-driven machines that move nucleosomes, and the order in which all of these act at one well-studied promoter. It then turns to silencing by heterochromatin and to the question that gives epigenetics its name: how a state of gene activity, once established, can be inherited through cell division without a change in DNA sequence. A simple model of read–write feedback shows what such memory requires, and the methods that measure DNA methylation close the loop with the tools of [7.2.6](/7.2.6). The chemical probes that target these enzymes (bromodomain inhibitors, HDAC and methyltransferase inhibitors) and the chemistry of modified bases belong to chemical biology ([6.6](/6.6)) and are only mentioned here.

## 15.1. Histones Repress, Activators Antirepress

**Example 15.1.1 (Repression by nucleosomes and H1)** Laybourn and Kadonaga (1991) reconstituted chromatin on a plasmid carrying the *Drosophila Krüppel* promoter, with purified core histones at about one octamer per $200$ bp, with or without histone H1, and transcribed it in a nuclear extract. Core histones alone reduced basal transcription by about $75\%$ relative to naked DNA; the remaining $25\%$ came from templates on which the promoter happened not to be covered by a core. Adding H1 repressed transcription much further, to a few percent. The sequence-specific factors Sp1 and GAL4-VP16, added before the histones, prevented most of the repression by H1 and also stimulated transcription above the level of naked DNA; the GAGA factor, which binds GA-rich sequences in the *Krüppel* promoter, prevented repression but did not stimulate further.

Activators thus have two separable functions: *antirepression*, preventing or reversing the repression by histones, and true activation, stimulating the transcription machinery ([7.2.14](/7.2.14)). Antirepression is a form of **nucleosome positioning** ([7.2.4](/7.2.4)): activators keep nucleosomes off promoters, either by binding first and excluding them or by recruiting enzymes that move them away, so that nucleosomes end up around rather than on the control regions of active genes. This is the origin of the nucleosome-free regions and DNase I hypersensitive sites of active genes. A special class of activators, pioneer factors (FoxA and others), can bind their sites on the surface of a nucleosome and open chromatin for other factors.

Nucleosomes affect transcription in two ways, and the rest of the chapter is organized around them: the histones themselves can be modified, changing how they interact with DNA, with neighbouring nucleosomes and with other proteins (Sections 15.2–15.3), and nucleosomes can be moved or removed by ATP-dependent machines (Section 15.4).

## 15.2. Histone Modifications and Their Readers

### 15.2.1. Writers, Erasers and Readers

The disordered N-terminal tails of the core histones, about $28\%$ of their mass and exposed on the nucleosome surface ([7.2.4](/7.2.4)), carry most of the modifications, but more than twenty sites in the globular core are modified too. The principal modifications are listed below; each is placed by a "writer" enzyme, removed by an "eraser" and recognized by "reader" domains of other proteins.

| Modification | Residue | Writers | Erasers | Readers |
|---|---|---|---|---|
| Acetylation | Lys | HATs (GCN5/PCAF, p300/CBP, MYST family such as MOF and Tip60); donor acetyl-CoA | HDACs (classes I, II, IV) and sirtuins (class III, $\mathrm{NAD^+}$-dependent) | bromodomain, YEATS, tandem PHD |
| Methylation | Lys (me1, me2, me3); Arg (me1, me2 symmetric or asymmetric) | SET-domain methyltransferases, DOT1L (H3K79); PRMTs for Arg; donor S-adenosylmethionine | LSD1 (FAD-dependent, me1/me2), JmjC demethylases (Fe(II), 2-oxoglutarate) | chromodomain, PHD finger, Tudor, PWWP, MBT, WD40 (EED) |
| Phosphorylation | Ser, Thr (H3S10, H3T3, H2AX S139) | kinases (Aurora B, MSK1/2, ATM/ATR) | phosphatases | 14-3-3, BRCT |
| Ubiquitination | Lys (H2AK119, H2BK120 in humans, K123 in yeast) | PRC1 (RING1B), RNF20/40 (Bre1 in yeast) with Rad6 | deubiquitinases (USP22, BAP1) | specific complexes (e.g., Dot1, PRC2 accessory proteins) |

Acetylation neutralizes the positive charge of lysine, which weakens the binding of the tails to DNA and to the acidic patch of the neighbouring nucleosome; acetylation of H4 K16 alone prevents the compaction of nucleosome arrays in vitro. Methylation does not change the charge; its effects are entirely through readers, which recognize the methyl-lysine through an "aromatic cage" of two to four aromatic side chains (cation–π interactions), and discriminate the degree of methylation and the surrounding sequence. Modifications therefore act by two mechanisms: they change the way histone tails interact with DNA and with neighbouring nucleosomes, and they attract (or repel) proteins that alter chromatin structure and activity.

**Definition 15.2.1** An enzyme that transfers an acetyl group from acetyl-CoA to the ε-amino group of lysine residues in histones is called a **histone acetyltransferase** (HAT). An enzyme that removes these acetyl groups is called a **histone deacetylase** (HDAC).

**Definition 15.2.2** A protein domain of about $110$ residues, a left-handed bundle of four α-helices with a hydrophobic pocket between its loops, that binds acetylated lysine is called a **bromodomain**. A domain of about $50$ residues, with three β-strands packed against a C-terminal helix, that binds methylated lysine through an aromatic cage is called a **chromodomain**.

The bromodomain (Dhalluin, Zhou and colleagues, 1999) is found in many HATs, in TAF1 (which has two in tandem, [7.2.13](/7.2.13)), in remodelers and in the BET proteins such as BRD4, which bind acetylated chromatin at enhancers and promoters and recruit P-TEFb. The chromodomain of HP1 binds trimethylated H3 K9; that of Polycomb proteins (CBX), trimethylated H3 K27. Small molecules that occupy the acetyl-lysine pocket of BET bromodomains (JQ1 and its successors) displace BRD4 from chromatin and are used as chemical probes and drug candidates ([6.6](/6.6)).

![Histone tail modifications and their readers (schematic). The N-terminal tails of H3 and H4, and the C-terminal tails of H2A and H2B, with the principal sites of acetylation, methylation, phosphorylation and ubiquitination; at right, the main associations of each mark with chromatin states, the reader domains that recognize them, and examples of cross-talk between marks](./plots/histone-marks.py)

The marks correlate with chromatin states in a reproducible way, which is how genome-wide ChIP-seq maps of a few marks are used to annotate genomes:

| Mark | Location | Associated state |
|---|---|---|
| H3K4me3 | promoters, just downstream of the start site | active or poised promoters; read by the PHD finger of TAF3 and by remodelers |
| H3K4me1 | enhancers | active or primed enhancers |
| H3K27ac | promoters and enhancers | active elements (distinguishes active from primed enhancers) |
| H3K36me3 | bodies of transcribed genes, rising toward the $3'$ end | placed cotranscriptionally by Set2/SETD2 bound to Ser2-phosphorylated CTD ([7.2.13](/7.2.13)) |
| H3K79me2 | $5'$ part of gene bodies | transcription (DOT1L) |
| H3K9me3 | pericentromeric repeats, transposons, some genes | constitutive heterochromatin (HP1) |
| H3K27me3 | developmental regulator genes, inactive X | facultative heterochromatin (Polycomb) |
| H4K16ac | active chromatin; the hyperactive male X in *Drosophila* | decompaction; blocks SIR binding in yeast |

### 15.2.2. Finding the Enzymes

**Example 15.2.1 (An activity gel for HATs)** Brownell and Allis (1995) separated proteins from the transcriptionally active macronuclei of *Tetrahymena* by SDS-PAGE in a gel in which histones had been polymerized. After electrophoresis they removed the SDS, let the proteins renature in the gel and incubated the gel with $[^3\mathrm{H}]$acetyl-CoA. A HAT renatured in the gel acetylates the histones around it, and fluorography revealed a single labeled band at $55\,\mathrm{kDa}$ (p55). Microsequencing and cloning (Brownell and colleagues, 1996) showed that p55 is homologous to yeast Gcn5p, a protein known from genetics as a transcriptional coactivator required by acidic activators; recombinant Gcn5p acetylated histones. A coactivator was thus an enzyme that modifies chromatin.

HATs fall into two functional groups. *HAT B* enzymes act in the cytoplasm on newly made histones, acetylating H4 on K5 and K12 to prepare them for deposition by chaperones; these acetyl groups are removed after deposition. *HAT A* enzymes act in the nucleus on histones in chromatin, and their activity correlates with transcription; p55/Gcn5p (in the SAGA complex), p300/CBP and TAF1 ([7.2.13](/7.2.13)) are of this kind. Many HAT A enzymes contain a bromodomain, which lets them bind the product of their own reaction.

The first deacetylase was purified by affinity chromatography on the deacetylase inhibitor trapoxin (Taunton, Hassig and Schreiber, 1996) and turned out to be the human homolog of yeast Rpd3, a protein known from genetics as a transcriptional repressor. The pattern of the HAT story repeated itself: a known regulator was an enzyme acting on histones.

## 15.3. Deacetylation and Corepressors

If acetylation of core histone tails activates, deacetylation should repress. Repressors that bind DNA do not usually carry deacetylase activity themselves; they bind corepressor complexes, which contain HDACs.

**Example 15.3.1 (Mad–Max recruits Sin3 and HDAC)** The bHLH-ZIP protein Max forms heterodimers with Myc, which activates genes at E boxes, and with Mad, which represses the same genes ([7.2.14](/7.2.14)). Laherty, Eisenman and colleagues (1997) found that Mad, through a short N-terminal helix (the Sin3-interaction domain), binds the corepressor mSin3A, which binds the deacetylases HDAC1 and HDAC2: the four proteins coimmunoprecipitated from cells. A Mad1 mutant with a helix-breaking proline in this region (Mad1Pro) failed to bind Sin3A and failed to repress, and the HDAC inhibitor trichostatin A relieved repression by wild-type Mad. Myc–Max, by contrast, recruits HAT-containing complexes. The two dimers compete for the same E boxes, so the balance between proliferation (Myc) and differentiation (Mad) is read out as the acetylation state of target promoters.

The same logic applies to the type II nuclear receptors ([7.2.14](/7.2.14)). Without hormone, the thyroid hormone and retinoic acid receptors bind the corepressors NCoR and SMRT, which bring HDAC3; hormone causes the corepressor to be released and replaced by coactivators with HAT activity (SRC, CBP/p300). Deacetylation restores the positive charge of the tails, lets them bind DNA and neighbouring nucleosomes again, and removes the docking sites for bromodomain proteins. HDACs are grouped into class I (HDAC1, 2, 3, 8; nuclear, in corepressor complexes such as Sin3, NuRD, CoREST and NCoR/SMRT), class II (HDAC4–7, 9, 10), class III (the sirtuins, which use $\mathrm{NAD^+}$ as cosubstrate and so couple deacetylation to the metabolic state of the cell) and class IV (HDAC11). HDAC inhibitors such as vorinostat are used in cancer therapy.

Acetylation is a dynamic balance, not a switch that is set once.

**Formula 15.3.1 (Steady state of acetylation)** If HATs acetylate a site with pseudo-first-order rate constant $k_{\mathrm{a}}$ and HDACs deacetylate it with rate constant $k_{\mathrm{d}}$, the acetylated fraction $a$ obeys $\mathrm{d}a/\mathrm{d}t = k_{\mathrm{a}}(1 - a) - k_{\mathrm{d}}a$, so
$$
a^* = \frac{k_{\mathrm{a}}}{k_{\mathrm{a}} + k_{\mathrm{d}}}, \qquad \tau = \frac{1}{k_{\mathrm{a}} + k_{\mathrm{d}}}, \tag{15.1}
$$
where $\tau$ is the time constant with which $a$ approaches its steady state after a change in either activity.

Isotope-labeling experiments show that many acetyl groups on histones turn over within minutes. If a site is $20\%$ acetylated and relaxes with $\tau = 10\,\mathrm{min}$, Eq. (15.1) gives $k_{\mathrm{a}} = 0.02\,\mathrm{min^{-1}}$ and $k_{\mathrm{d}} = 0.08\,\mathrm{min^{-1}}$; an HDAC inhibitor then raises acetylation toward $100\%$ with time constant $1/k_{\mathrm{a}} = 50\,\mathrm{min}$, which is why treatment of cells with such inhibitors causes global hyperacetylation within an hour or two. Recruiting a HAT to one promoter changes $a^*$ locally in minutes; this is fast enough for signal-responsive genes, but it also means that acetylation by itself cannot store information for long. Long-term memory requires feedback (Section 15.6).

## 15.4. ATP-Dependent Chromatin Remodeling

Acetylation of tails can loosen interactions between nucleosomes, but it leaves the nucleosomes in place. To expose DNA wrapped in a core, the core must be moved, opened or removed, and this requires energy from ATP hydrolysis.

**Definition 15.4.1** A multiprotein complex that uses the energy of ATP hydrolysis, through an ATPase subunit of the SF2 helicase-like superfamily translocating on nucleosomal DNA, to slide nucleosomes along DNA, evict them, or exchange histone dimers, is called a **chromatin remodeling complex** (chromatin remodeler).

The first remodeler was found by yeast genetics. Mutations named *swi* (defective in mating-type SWItching, through loss of *HO* expression) and *snf* (Sucrose NonFermenting, through loss of *SUC2* expression) turned out to affect the same complex, SWI/SNF; and their defects were suppressed by mutations in histone genes or in other chromatin proteins (the *spt* suppressors), showing that SWI/SNF works by counteracting the repressive effect of chromatin. Remodelers are classified by their ATPase:

| Family | ATPase (yeast; human) | Accessory domains | Main activities |
|---|---|---|---|
| SWI/SNF | Swi2/Snf2, Sth1 (RSC); BRG1, BRM (BAF, PBAF complexes) | bromodomain, HSA | sliding and eviction at promoters and enhancers; recruited by activators |
| ISWI | Isw1, Isw2; SNF2H, SNF2L (ACF, NURF, CHRAC) | HAND–SANT–SLIDE | regular spacing of arrays; senses linker length |
| CHD | Chd1; CHD1–9, including Mi-2 (CHD3/4) in NuRD with HDAC1/2 and MBD proteins | tandem chromodomains | spacing; NuRD couples remodeling to deacetylation and repression |
| INO80 | Ino80, Swr1; INO80, SRCAP, p400 | split ATPase, actin-related proteins | exchange of H2A–H2B for H2A.Z–H2B (SWR1) and back (INO80) |

In mammals, BRG1 and BRM associate with nine to twelve BRG1-associated factors (BAFs); one conserved subunit, BAF155/BAF170, has a SANT domain that helps the complex bind histones, and ISWI proteins have SANT and SLIDE domains that bind histone tails and linker DNA. Genes for subunits of BAF complexes are mutated in about $20\%$ of human cancers (*SMARCB1* in rhabdoid tumors, *ARID1A* in many carcinomas).

The ATPase binds nucleosomal DNA about two helical turns from the dyad and translocates on it by one or two base pairs per ATP, pulling DNA in from one side; the resulting bulge or twist propagates around the octamer and emerges as a change in the position of the DNA relative to the core: the nucleosome slides. ISWI and CHD remodelers bind the linker and slide preferentially toward the longer linker, so that arrays become evenly spaced with a length set by the remodeler; SWI/SNF and RSC can slide nucleosomes off the end of DNA or evict them.

**Example 15.4.1 (Remodeling exposes sites at different rates)** Kingston and colleagues (Narlikar and colleagues, 2001) incubated a mononucleosome assembled on labeled DNA with BRG1 and ATP and, at times up to $70\,\mathrm{min}$, tested the accessibility of three restriction sites at different positions in the nucleosome (XhoI, SpeI, PstI). The fraction of uncut DNA declined approximately exponentially for each site, $f(t) = \mathrm{e}^{-kt}$, but with different rate constants. A uniform "loosening" of the nucleosome would expose all sites at the same rate; site-specific rates indicate that remodeling produces distinct altered and moved states of the nucleosome, consistent with sliding of the octamer relative to the DNA and with remodeled conformations different from those reached by spontaneous unwrapping ([7.2.4](/7.2.4)).

The order in which remodelers and HATs arrive differs between genes. At the yeast *HO* gene, chromatin immunoprecipitation over the cell cycle (Cosma, Tanaka and Nasmyth, 1999) showed that the activator Swi5 binds first, then SWI/SNF, then the SAGA complex with Gcn5, which allows the second activator, SBF, to bind, and only then the general transcription factors and Pol II. The next section describes a gene where acetylation comes before remodeling.

## 15.5. Ordered Recruitment at the IFN-β Promoter

At the human interferon-β gene, the enhanceosome ([7.2.14](/7.2.14)) assembles in a nucleosome-free region upstream of the promoter, while a nucleosome (nucleosome II) covers the TATA box and the start site. Thanos and colleagues (Agalioti and colleagues, 2000, 2002; Lomvardas and Thanos, 2001) followed the activation of the gene after Sendai virus infection of HeLa cells by **chromatin immunoprecipitation** with antibodies against factors and against specifically modified histones, followed by PCR of the promoter:

1. The enhanceosome assembles in the first hours after infection.
2. It recruits the HAT GCN5 (with its relative PCAF), which acetylates nucleosome II at H4 K8 and H3 K9. An unidentified kinase phosphorylates H3 S10, which allows GCN5 to acetylate H3 K14.
3. The CBP–Pol II holoenzyme is recruited, CBP binding through its bromodomain and acetylating further.
4. Acetylated H4 K8 recruits SWI/SNF (through the bromodomain of BRG1), which remodels nucleosome II.
5. Acetylated H3 K9 and K14 recruit TFIID through the double bromodomain of TAF1 ([7.2.13](/7.2.13)). TBP binds the TATA box and bends the DNA; the remodeled nucleosome slides about $36$ bp downstream, uncovering the start site, and transcription begins.

![Ordered events at the IFN-β promoter after virus infection (approximate times after Agalioti et al. 2000, 2002, as summarized by Weaver; schematic). Each bar marks when a factor is bound or a histone mark is present at the promoter by chromatin immunoprecipitation; the arrows give the dependencies tested by immunodepletion and histone mutants (Example 15.5.1)](./plots/ifnb-timeline.py)

The timing was striking: in ChIP, H4 K8 was acetylated from about $3$ to $8\,\mathrm{h}$ after infection, H4 K12 only briefly at $6\,\mathrm{h}$, H3 S10 phosphorylation rose from about $3\,\mathrm{h}$ and peaked at $6\,\mathrm{h}$, H3 K14 acetylation began at about $6\,\mathrm{h}$, coinciding exactly with the recruitment of TBP, and H3 K9 acetylation began earlier and lasted at least $19\,\mathrm{h}$. H4 K5 and K16 were not acetylated at all. The pattern of modification is specific in sites and in time.

**Example 15.5.1 (Which mark recruits which factor)** To test the dependencies, the enhanceosome was assembled on an immobilized IFN-β promoter and incubated with nuclear extracts. Extracts immunodepleted of GCN5/PCAF failed to acetylate H4 K8, whereas extracts depleted of CBP/p300 or of the SWI/SNF ATPase BRG1/BRM still did (control blots showed that each depletion removed only its target). In chromatin reconstituted on the promoter from recombinant histones, acetylation (acetyl-CoA plus enhanceosome) was required to recruit both BRG1 and TAF1. With mutant histones in which one residue was replaced by alanine:

| Mutant histone | BRG1 (SWI/SNF) recruited | TAF1 (TFIID) recruited | Interpretation |
|---|---|---|---|
| H4 K8A | no | no | H4 K8ac recruits SWI/SNF, which is needed for TFIID |
| H3 K9A, H3 K14A | yes | no | H3 K9ac and K14ac recruit TFIID |
| H3 S10A | yes | no | S10 phosphorylation is needed for K14 acetylation |
| H4 K5A (not acetylated in vivo) | yes | yes | control |

The model drawn from these experiments is that information flows from the enhancer to the nucleosome, not the reverse: the DNA sequence of the enhancer determines which activators assemble; the activators determine which enzymes arrive; the enzymes write a specific combination of marks; and the marks recruit the next set of complexes.

**Remark 15.5.1 (The histone-code hypothesis today)** The *histone code* hypothesis (Strahl and Allis, 2000; Jenuwein and Allis, 2001) proposed that combinations of histone modifications constitute a code, read by effector proteins, that specifies downstream chromatin states, extending the information in the DNA sequence. Two decades later the evidence supports parts of the idea and not others. Combinatorial reading is real: many readers are multivalent (the double bromodomain of TAF1 reads two acetylated lysines; BPTF reads H3K4me3 and H4K16ac at once), and marks influence each other (cross-talk, Section 15.8). But a code in the strict sense, a fixed dictionary from combinations to outcomes, has not been found; the same mark can have different consequences in different contexts, and many marks are consequences rather than causes of transcription. In *Drosophila*, replacing all replication-dependent H3 genes by versions with arginine at K4 had little effect on transcription in the tissues examined (Hödl and Basler, 2012), whereas the same replacement at K27 reproduced the derepression of Polycomb target genes (Pengelly, Müller and colleagues, 2013). H3K27 methylation is therefore causal for Polycomb silencing, while H3K4 trimethylation, the most reliable mark of active promoters, is largely a consequence of transcription. "Histone language" with context-dependent meanings describes the current view better than "code".

## 15.6. Heterochromatin and Silencing

### 15.6.1. Position Effects

**Definition 15.6.1** A change in the expression of a gene caused by a change of its location in the genome, without a change in its own sequence, typically by placing it next to heterochromatin, is called a **position effect**. When the silencing occurs in some cells and not others, and the choice is inherited by the descendants of each cell, it is called *position-effect variegation*.

Position-effect variegation was discovered in *Drosophila* (Muller, 1930): an X-ray-induced inversion, *In(1)w*^m4, moves the *white* gene, needed for red eye pigment, next to pericentromeric heterochromatin, and the eyes become mottled, with red and white patches each descended from a single cell whose choice was then inherited. Genetic screens for suppressors and enhancers of variegation, *Su(var)* and *E(var)* mutations, identified many heterochromatin proteins, including HP1 (encoded by *Su(var)2-5*) and the H3 K9 methyltransferase Su(var)3-9. In budding yeast, Gottschling and colleagues (1990) found the analogous telomere position effect: a *URA3* gene placed next to a telomere was silenced in some cells and expressed in others, as shown by colonies that grew either on medium lacking uracil (expressing) or on 5-fluoro-orotic acid, which kills *URA3*-expressing cells.

### 15.6.2. Silencing in Yeast: SIR Proteins

Budding yeast silences its telomeres and the silent mating-type loci *HML* and *HMR*, which carry copies of the mating-type genes that must not be expressed. Silencing depends on the SIR proteins (Silent Information Regulators):

1. A sequence-specific protein nucleates silencing: Rap1 binds the telomeric $\mathrm{TG_{1-3}}$ repeats; at *HML* and *HMR*, Rap1, Abf1 and the origin recognition complex bind silencer elements (E and I).
2. Rap1 recruits Sir3 and Sir4; Sir4 brings Sir2.
3. Sir2, an $\mathrm{NAD^+}$-dependent deacetylase (the founding sirtuin), deacetylates H4 K16 (and H3 K9 and K14) on adjacent nucleosomes.
4. Sir3 and Sir4 bind the deacetylated H3 and H4 tails of these nucleosomes, bringing more Sir2, which deacetylates the next nucleosomes.

Silencing spreads in this way a few kilobases from the telomere (about $3\,\mathrm{kb}$ in typical experiments) until it meets a barrier. Acetylation of H4 K16 by the HAT Sas2, which prevents the binding of Sir3, and the histone variant H2A.Z limit the spread: acetylation promotes gene activity partly by blocking heterochromatin formation.

### 15.6.3. H3K9 Methylation, HP1 and Polycomb

In most eukaryotes other than budding yeast, heterochromatin is marked by methylation. Constitutive heterochromatin, at pericentromeric satellites and transposons, carries H3 K9 trimethylation placed by Suv39h (Clr4 in fission yeast; Rea, Jenuwein and colleagues, 2000). The chromodomain of HP1 binds H3K9me3, and HP1, a dimer, binds Suv39h, which methylates K9 of a neighbouring nucleosome; Suv39h and Clr4 also have chromodomains that bind their own product. Methylated nucleosomes thus recruit enzymes that methylate more nucleosomes, a read–write feedback that propagates the repressed state along the chromatin until a boundary stops it. HP1 also forms liquid-like condensates that may help compact heterochromatin ([7.2.21](/7.2.21)). In fission yeast, nucleation of centromeric heterochromatin is directed by small RNAs through the RNAi machinery ([7.2.18](/7.2.18)).

Facultative heterochromatin, which silences developmental regulator genes such as the *Hox* genes in cells where they must stay off, and one X chromosome in female mammals, is made by Polycomb group proteins. Polycomb repressive complex 2 (PRC2, with the methyltransferase EZH2) trimethylates H3 K27; its subunit EED binds H3K27me3 through an aromatic cage, and this binding allosterically activates EZH2, again a read–write loop (Margueron, Reinberg and colleagues, 2009). PRC1 monoubiquitinates H2A K119 and compacts chromatin; its CBX subunits read H3K27me3 through chromodomains. Trithorax group proteins, the H3K4 methyltransferases of the MLL/COMPASS family, maintain the active state of the same genes in the cells where they are on.

| | Constitutive heterochromatin | Facultative heterochromatin |
|---|---|---|
| Where | pericentromeres, telomeres, transposons; the same in all cells | developmental genes, inactive X; differs between cell types |
| Mark | H3K9me3 (+ DNA methylation in mammals) | H3K27me3, H2AK119ub1 |
| Writers | Suv39h1/2, SETDB1 (recruited to transposons by KRAB zinc-finger proteins) | PRC2 (EZH2), PRC1 (RING1B) |
| Readers | HP1 (chromodomain) | CBX (chromodomain), EED |
| Counteracted by | H3K9 demethylases (JMJD2), H4K16 acetylation | Trithorax (H3K4 methylation), UTX (H3K27 demethylase) |

### 15.6.4. A Model of Epigenetic Memory

Read–write feedback can store information only if it overcomes the noise of random conversions and the dilution of marks at each replication. Dodd, Sneppen, Thon and colleagues (2007) captured this in a minimal model.

**Example 15.6.1 (The Dodd model)** Consider $N$ nucleosomes, each in one of three states, modified for silencing ($M$), unmodified ($U$) or modified for activity ($A$). Repeatedly pick a nucleosome $n_1$ at random. With probability $\alpha$, a *recruited* conversion occurs: pick a second nucleosome $n_2$ at random from the region; if $n_2$ is $M$, move $n_1$ one step toward $M$ ($A \to U$ or $U \to M$), and if $n_2$ is $A$, one step toward $A$ (a $U$ nucleosome recruits nothing). With probability $1 - \alpha$, a *noisy* conversion moves $n_1$ one step to a randomly chosen neighbouring state. Replication is modeled by replacing each nucleosome with a $U$ nucleosome with probability $1/2$ at each cell division. The ratio $F = \alpha/(1 - \alpha)$ measures the strength of feedback.

Simulations (figure) show that for weak feedback ($F \lesssim 1$) the region fluctuates around a mixed state and remembers nothing, whereas above a threshold of a few (about $F = 4$ for the $60$ nucleosomes of the figure; the threshold depends on the size of the region and the frequency of division) it is bistable: it stays almost entirely $M$ or almost entirely $A$ for many cell generations, recovers from the halving of marks at each replication, and switches between the two states only rarely. Two features are essential: recruitment must be long-range (any modified nucleosome in the region can recruit, not only immediate neighbours, which corresponds to looping of the chromatin fiber or the spreading of reader–writer complexes in three dimensions), and it must be cooperative in the sense that converting $A$ to $M$ requires passing through $U$, so that two recruited steps are needed. With nearest-neighbour recruitment only, or with a direct $A \to M$ conversion, stable memory is lost. The model explains why silencing is all-or-none and variegated, why it is inherited, and why nucleation sites (silencers, Polycomb response elements) are needed to establish it but not always to maintain it.

![Epigenetic memory from read–write feedback, simulated with the model of Example 15.6.1 (N = 60 nucleosomes; one cell division with random loss of half of the marks every 100 sweeps, marked at the top). A: with weak feedback (F = 1) the fraction of M nucleosomes fluctuates around intermediate values. B: with strong feedback (F = 4) the region is bistable, mostly M or mostly A, recovers after each division and switches rarely. C: distributions of the difference between the M and A fractions over long simulations: unimodal for F = 1, bimodal for F = 4](./plots/epigenetic-memory.py)

## 15.7. DNA Methylation

### 15.7.1. 5-Methylcytosine and CpG Islands

**DNA methylation**, the transfer of a methyl group from S-adenosylmethionine to the C5 position of cytosine (forming 5-methylcytosine, 5mC) or to the exocyclic amino groups of adenine or cytosine by DNA methyltransferases, was introduced with the chemistry of the methylated bases in [7.1.11](/7.1.11). In mammals it occurs almost exclusively at cytosines followed by guanine (CpG dinucleotides), symmetrically on both strands. In bacteria, methylation of adenine (Dam, at GATC) and of cytosine protects DNA from restriction enzymes (the **restriction–modification system**, [7.2.5](/7.2.5)) and marks the parental strand for mismatch repair ([7.2.8](/7.2.8)). In mammals, $70$–$80\%$ of the roughly $28$ million CpGs of the haploid genome are methylated, and CpG is the rarest dinucleotide: it occurs at only about a quarter of the frequency expected from the base composition. The deficit is a consequence of methylation itself. Deamination of cytosine gives uracil, which is recognized and removed by **base-excision repair**, but deamination of 5mC gives thymine, and the resulting T·G mismatch is repaired less efficiently; over evolutionary time methylated CpGs have mutated to TpG and CpA, and CpG transitions are the most frequent point mutations in human genetic disease.

**Definition 15.7.1** A stretch of DNA, at least $200$ bp long (in stricter definitions $500$ bp), with a GC content above $50\%$ and a ratio of observed to expected CpG frequency above $0.6$, that has escaped the general depletion of CpG because it is not methylated in the germline, is called a **CpG island** (Gardiner-Garden and Frommer, 1987).

The human genome has about $25\,000$–$30\,000$ CpG islands. They mark about $60$–$70\%$ of promoters, including those of almost all housekeeping genes, and most of them are unmethylated in all cells regardless of whether the gene is expressed; they correspond to the dispersed, TATA-less promoters of [7.2.12](/7.2.12). Promoter CpG islands become methylated, and their genes stably silenced, in a few special cases: imprinted genes (Example 14.7.1), genes on the inactive X chromosome, some germline-specific genes, and, abnormally, tumor-suppressor genes in cancer cells, where hypermethylation of the CpG islands of genes such as *CDKN2A* and *MLH1* is an alternative to mutation.

Methylation represses transcription in two ways. It prevents the binding of some transcription factors whose sites contain CpG (CTCF at the *H19* imprinting control region, Example 14.7.1), and it recruits methyl-CpG-binding domain (MBD) proteins, such as MeCP2 (whose mutation causes Rett syndrome) and MBD2, which bring corepressor complexes with HDACs (Sin3, NuRD). Methylation, deacetylation and H3K9 methylation reinforce each other, and densely methylated promoters are in nucleosome-dense, inaccessible chromatin. Methylation in the bodies of transcribed genes, by contrast, is common in active genes and does not repress.

### 15.7.2. Maintenance, De Novo Methylation and Demethylation

Because CpG is palindromic, a methylated CpG is methylated on both strands, and after replication each daughter duplex carries a hemimethylated site: methyl on the parental strand, none on the new strand. Holliday and Pugh, and Riggs (1975), proposed that an enzyme that methylates hemimethylated sites, but not unmethylated ones, would copy the pattern semiconservatively, as DNA is copied. This enzyme is DNMT1. It is recruited to replication foci by UHRF1, whose SRA domain flips the 5mC of a hemimethylated CpG out of the helix and whose other domains bind H3K9me3 and ubiquitinate H3 to activate DNMT1, a link between DNA and histone methylation. New patterns are written by the de novo methyltransferases DNMT3A and DNMT3B (with the inactive cofactor DNMT3L), whose ADD domain is repelled by H3K4 methylation (which protects active CpG-island promoters) and whose PWWP domain binds H3K36me3 (which directs methylation to gene bodies).

Demethylation is either passive, by failure of maintenance during successive replications, or active. The TET dioxygenases (Tahiliani, Rao and colleagues, 2009) oxidize 5mC to 5-hydroxymethylcytosine (5hmC), 5-formylcytosine and 5-carboxylcytosine; the last two are removed by the **DNA glycosylase** TDG, and base-excision repair restores an unmodified C. In mammalian development methylation is reprogrammed twice: the paternal genome is actively demethylated in the zygote and the maternal genome passively in the first cleavages, and the primordial germ cells erase almost all methylation, including the imprints, which are then reestablished according to the sex of the germline. Plants methylate cytosine in CG, CHG and CHH contexts and direct methylation to repeats with small RNAs made by Pol IV and Pol V ([7.2.12](/7.2.12)); *Drosophila* and budding yeast have essentially no cytosine methylation.

**Formula 15.7.1 (Site-independent copying of methylation)** Let a CpG site be methylated with probability $m_t$ in generation $t$. After replication the site is maintained with probability $\mu$ if it was methylated, and an unmethylated site (including one that failed maintenance) is methylated de novo with probability $\delta$. Then
$$
m_{t+1} = \mu m_t + \delta\,(1 - \mu m_t), \qquad m^* = \frac{\delta}{1 - \mu(1 - \delta)}, \qquad m_t - m^* = \lambda^t (m_0 - m^*),\ \ \lambda = \mu(1 - \delta). \tag{15.2}
$$

With measured maintenance efficiencies of about $\mu = 0.95$–$0.99$ per site per division and $\delta$ of a few percent, $\lambda$ is about $0.9$–$0.95$: a site that is fully methylated or fully unmethylated forgets its initial state within some ten to twenty divisions, and every site tends to the same intermediate value. Real CpG islands do not behave like this: they stay either almost fully methylated or almost fully unmethylated for the lifetime of an organism. The resolution is the same as for histone marks: methylation is not copied site by site, but collaboratively, with methylation at neighbouring CpGs and the associated histone marks stimulating maintenance and de novo methylation (and unmethylated islands protected by H3K4 methylation and TET enzymes), which creates two stable states of the whole island, as in the Dodd model (figure, panel B).

### 15.7.3. Measuring DNA Methylation

| Method | Principle | Output |
|---|---|---|
| Methylation-sensitive restriction | **isoschizomers** HpaII and MspI both cut CCGG; HpaII is blocked by methylation of the internal C, MspI is not ([7.2.5](/7.2.5)) | methylation at a few sites, by Southern blot or PCR |
| Antibody capture (MeDIP) | an antibody against 5mC precipitates methylated fragments, followed by qPCR or sequencing | regional methylation level |
| Bisulfite sequencing | sodium bisulfite deaminates C to U but leaves 5mC (which reacts about a hundred times more slowly) unchanged; after PCR, U is read as T (Frommer and colleagues, 1992) | methylation of every C at single-base resolution, genome-wide (WGBS) or at enriched regions (RRBS) |
| Bisulfite-free conversion | enzymatic: TET2 oxidation protects 5mC/5hmC and APOBEC3A deaminates unmodified C (EM-seq); TET oxidation followed by pyridine borane reduction converts 5mC to a base read as T (TAPS) | single-base resolution with less DNA damage |
| Direct detection | nanopore current or polymerase kinetics in SMRT sequencing differ for modified bases ([7.2.6](/7.2.6)) | 5mC, 5hmC and 6mA on single long molecules |

Bisulfite treatment degrades most of the DNA and cannot distinguish 5mC from 5hmC, which also resists conversion; variants that add an oxidation step (oxBS-seq) or protect 5hmC (TAB-seq) separate the two. The conversion chemistry itself, and its bisulfite-free alternatives, are topics of chemical biology ([6.6](/6.6)).

![DNA methylation and its measurement. A: bisulfite conversion read out by sequencing: in a CpG-containing sequence, unmethylated C becomes U and then T after PCR, whereas 5mC remains C; comparing the converted read with the reference identifies the methylated sites. B: site-independent copying of methylation, Eq. (15.2): methylation levels of initially fully methylated and fully unmethylated sites over cell divisions for two sets of maintenance and de novo efficiencies; both converge on the same intermediate level, so long-term memory requires collaborative, region-level feedback](./plots/dna-methylation.py)

## 15.8. Epigenetic Inheritance and Cross-Talk

**Definition 15.8.1** The study of changes in gene function that are heritable through mitosis (and in some cases meiosis) and that cannot be explained by changes in DNA sequence is called **epigenetics**; the states themselves are called epigenetic.

Waddington (1942) coined the term for the processes by which genotype produces phenotype during development, picturing a cell rolling down a branching "epigenetic landscape"; the molecular definition above dates from the 1990s. Four mechanisms can carry an epigenetic state through cell division:

1. *Methylation of DNA*, copied at hemimethylated sites by DNMT1 (Section 15.7).
2. *Histone modifications with read–write feedback.* Parental H3–H4 tetramers, with their marks, are distributed between the daughter duplexes at the replication fork ([7.2.4](/7.2.4)), so each daughter starts with half the marks; reader–writer enzymes (PRC2 with EED, Clr4 and Suv39h with their chromodomains) restore the full pattern (Example 15.6.1). Experiments in fission yeast in which heterochromatin was induced by tethering Clr4 to an ectopic site and the tether was then removed (Audergon, Allshire and colleagues; Ragunathan, Moazed and colleagues, 2015) showed that H3K9 methylation alone can propagate silencing for many generations, but only when the demethylase Epe1 is absent: inheritance is a competition between read–write feedback and erasure.
3. *Self-sustaining transcription factor circuits*, in which a factor activates its own gene (positive feedback) and remains on after the inducing signal is gone; this is a property of the regulatory network rather than of chromatin ([7.2.22](/7.2.22), [7.9](/7.9)).
4. *Self-templating protein conformations*, such as yeast prions ([7.1.6](/7.1.6)).

Inheritance across generations of organisms is common in plants, where methylation states (epialleles) can persist for many generations: the peloric (radially symmetric) flowers of a natural *Linaria vulgaris* variant described by Linnaeus are caused by heritable methylation and silencing of the *Lcyc* gene, not by a mutation (Cubas, Vincent and Coen, 1999). In mammals, the two waves of reprogramming erase most marks, and well-documented transgenerational effects are rare; an exception is the mouse *agouti viable yellow* allele, whose expression, controlled by the methylation of an inserted retrotransposon, varies between genetically identical littermates and is influenced by the maternal diet.

Marks influence each other. The best-studied example of cross-talk between histones is in yeast: monoubiquitination of H2B K123 (by Rad6 with Bre1) is required for the methylation of H3 K4 by the COMPASS complex (Set1) and of H3 K79 by Dot1; the *htb1-K123R* mutation abolishes both (Sun and Allis, 2002; Briggs, Strahl and colleagues, 2002). The modification of one histone thus controls the modification of another in the same nucleosome (listed in the figure of Section 15.2). Other examples have appeared above: phosphorylation of H3 S10 enabling acetylation of K14 (Section 15.5), H3K4 methylation repelling DNMT3 and H3K9me3 recruiting UHRF1 and DNMT1 (Section 15.7), and H3K36 methylation in gene bodies recruiting the deacetylase complex Rpd3S, which removes acetylation behind the polymerase and prevents initiation at cryptic promoters inside genes (Carrozza, Workman and colleagues, 2005).

## 15.9. Transcription Through Nucleosomes: FACT

Nucleosomes in the body of a gene are obstacles to an elongating polymerase. In vitro, Pol II alone stalls at a nucleosome, while in cells it transcribes chromatin almost as fast as naked DNA. A factor that facilitates transcription through nucleosomes, FACT (facilitates chromatin transcription), was purified from human cells by its ability to allow Pol II to transcribe chromatin templates (Orphanides, Reinberg and colleagues, 1998). FACT has two subunits: Spt16, which binds H2A–H2B dimers and needs its acidic C-terminal region for activity, and SSRP1 (Pob3 in yeast), which binds H3–H4.

**Example 15.9.1 (FACT removes and restores an H2A–H2B dimer)** In vitro, FACT stimulated the loss of one H2A–H2B dimer from nucleosomes being transcribed, producing a hexasome through which the polymerase passes readily (Belotserkovskaya, Reinberg and colleagues, 2003). FACT also acts as a histone chaperone that adds the dimer back to the hexasome after the polymerase has passed, so that the nucleosome is restored and its old histones, with their marks, are largely retained. In *Drosophila* polytene chromosomes, FACT is recruited within minutes to heat-shock loci after induction and travels with the elongating polymerase, downstream of the activator bound at the promoter (Saunders, Lis and colleagues, 2003).

Single-molecule experiments show how the polymerase passes a nucleosome. Pol II does not actively peel the DNA off the octamer; it waits for the DNA ahead of it to unwrap spontaneously and then advances, a Brownian ratchet. Because the equilibrium constant for spontaneous exposure falls from about $10^{-2}$ near the edge of the core to about $10^{-4}$ near the dyad ([7.2.4](/7.2.4)), the polymerase pauses most strongly in the middle of the nucleosome, and its average speed through the core is much lower than on naked DNA; factors that destabilize the nucleosome (FACT, acetylation, the histone variant H2A.Z, and a second polymerase following closely behind) raise the probability of exposure and the speed. Behind the polymerase, chaperones (FACT, Spt6) restore nucleosomes and Set2–H3K36me3–Rpd3S removes acetylation, returning the chromatin of the gene body to a closed state that suppresses spurious initiation.

## Summary

| Topic | Key facts |
|---|---|
| Repression and antirepression | core histones repress basal transcription about $75\%$, H1 much more; Sp1 and GAL4-VP16 antirepress and activate, GAGA factor antirepresses (Example 15.1.1); pioneer factors |
| Modifications | acetylation, methylation, phosphorylation, ubiquitination; writers, erasers, readers; HAT and HDAC (Definition 15.2.1), bromodomain and chromodomain (Definition 15.2.2); H3K4me3 promoters, H3K4me1 and H3K27ac enhancers, H3K36me3 gene bodies, H3K9me3 and H3K27me3 heterochromatin |
| Discovery | HAT activity gel, p55 = Gcn5p (Example 15.2.1); HDAC1 = Rpd3 homolog |
| Corepressors | Mad–Max → Sin3 → HDAC1/2 (Example 15.3.1); unliganded nuclear receptors → NCoR/SMRT → HDAC3; sirtuins use $\mathrm{NAD^+}$; acetylation steady state $a^* = k_{\mathrm{a}}/(k_{\mathrm{a}} + k_{\mathrm{d}})$, Eq. (15.1) |
| Remodelers (Definition 15.4.1) | SWI/SNF, ISWI, CHD, INO80 families; sliding, spacing, eviction, H2A.Z exchange; site-specific exposure rates (Example 15.4.1); order differs between genes (*HO* versus IFN-β) |
| IFN-β promoter | enhanceosome → GCN5 (H4K8ac, H3K9ac; S10ph → K14ac) → CBP–Pol II → SWI/SNF (via H4K8ac) → TFIID (via H3K9ac, K14ac) → nucleosome slides 36 bp (Example 15.5.1); histone code as context-dependent language (Remark 15.5.1) |
| Heterochromatin | position effect (Definition 15.6.1), PEV and telomere position effect; Rap1 → Sir3/Sir4/Sir2, H4K16 deacetylation, spreading; H3K9me3–HP1–Suv39h read–write; Polycomb PRC2 (EED feedback) and PRC1 |
| Memory | Dodd model: long-range, cooperative recruitment above a threshold feedback ratio $F$ gives bistable, heritable states (Example 15.6.1) |
| DNA methylation | 5mC at CpG, $70$–$80\%$ methylated, CpG depleted by deamination; CpG islands (Definition 15.7.1) unmethylated at most promoters; DNMT1–UHRF1 maintenance, DNMT3 de novo, TET–TDG demethylation; site-independent copying forgets, Eq. (15.2); bisulfite, enzymatic and direct methods |
| Epigenetics (Definition 15.8.1) | DNA methylation, histone marks with read–write feedback, transcription-factor feedback, prions; tethering experiments; plant epialleles; cross-talk (H2Bub → H3K4/K79me; H3K36me3 → Rpd3S) |
| FACT | Spt16–SSRP1; removes and restores an H2A–H2B dimer (Example 15.9.1); Pol II passes nucleosomes as a Brownian ratchet |

## Questions

1. In Example 15.1.1, why does reconstituted chromatin with one octamer per $200$ bp still give $25\%$ of the transcription of naked DNA? Predict the effect of adding an activator after rather than before the histones.

   **Answer** Nucleosomes are deposited without regard to sequence in this reconstitution, so on a fraction of the templates (about a quarter) the core promoter lies in a linker or uncovered stretch and remains accessible; only templates whose promoters are covered are repressed. If the activator is added after assembly, it must compete with a nucleosome already bound: factors that cannot bind nucleosomal sites (most activators) would fail to antirepress unless a remodeler or HAT is present, while pioneer factors could bind. Preincubation of the activator with DNA lets it exclude nucleosomes from its site (preemptive antirepression), which is why order matters in such experiments.
2. Using Eq. (15.1), a promoter site is $10\%$ acetylated with $k_{\mathrm{d}} = 0.2\,\mathrm{min^{-1}}$. An activator recruits a HAT that raises $k_{\mathrm{a}}$ tenfold. What are the new steady state and the time to reach it?

   **Answer** Initially $a^* = 0.1 = k_{\mathrm{a}}/(k_{\mathrm{a}} + 0.2)$, so $k_{\mathrm{a}} = 0.022\,\mathrm{min^{-1}}$. Tenfold: $k_{\mathrm{a}} = 0.22$, $a^* = 0.22/0.42 \approx 0.52$, reached with $\tau = 1/0.42 \approx 2.4\,\mathrm{min}$. Acetylation responds within minutes, and when the activator leaves, it decays back just as quickly; acetylation alone does not store memory.
3. In the IFN-β experiments, how do the H4 K8A and H3 K14A mutants show that SWI/SNF recruitment precedes and is required for TFIID recruitment, rather than the reverse?

   **Answer** H4 K8A abolishes recruitment of both BRG1 and TAF1, while H3 K14A (and K9A) abolishes recruitment of TAF1 only, with BRG1 still recruited. If TFIID were needed to bring SWI/SNF, the H3 K14A mutant, which cannot recruit TFIID, should also lose SWI/SNF; it does not. If SWI/SNF were dispensable for TFIID, the H4 K8A mutant, which loses SWI/SNF, might still recruit TFIID through the intact H3 K9/K14 marks; it does not. Hence SWI/SNF binding (through H4K8ac) is upstream of, and required for, TFIID binding (which also needs H3K9ac and K14ac).
4. Explain how H4 K16 acetylation acts as a boundary to Sir-mediated silencing in yeast, and predict the phenotype of a *sas2* deletion for genes near telomeres.

   **Answer** Silencing spreads because Sir2 deacetylates H4 K16 and Sir3 binds deacetylated H4 tails, recruiting more Sir2. Sas2 acetylates H4 K16 throughout euchromatin; an acetylated K16 cannot bind Sir3, so a zone of high Sas2 activity stops the spread. In a *sas2* deletion, H4 K16 is hypoacetylated near the boundary, Sir proteins spread further from the telomere, and genes in the subtelomeric region that are normally expressed become silenced (the silenced domain expands), while silencing at the core of the telomere is little changed.
5. In the Dodd model, why does direct conversion $A \to M$, without passing through $U$, destroy bistability?

   **Answer** Bistability requires that a single random or recruited event cannot by itself switch a nucleosome between the two extreme states, so that the majority state can repair defects faster than they accumulate. With two-step conversion, a nucleosome in the minority state must be pushed twice in the same direction before it reinforces the minority, while the majority recruits it back after one step; the effective recruitment is cooperative, giving the strong nonlinearity needed for two stable states. With direct conversion each recruitment event is a full switch, the dynamics become effectively linear in the fractions (like a voter model), and the region drifts between states without a barrier: memory is lost.
6. Use Eq. (15.2) with $\mu = 0.98$ and $\delta = 0.02$ to find the steady-state methylation level and the number of divisions after which an initially fully methylated site has lost half of its excess over this level. What does this imply for imprinted genes, which keep their methylation for the lifetime of an organism?

   **Answer** $m^* = 0.02/(1 - 0.98 \times 0.98) = 0.02/0.0396 \approx 0.51$, and $\lambda = 0.98 \times 0.98 = 0.9604$; the excess halves after $\ln 2/(-\ln 0.9604) \approx 17$ divisions. A human body involves tens of divisions in many lineages, so site-independent copying would erase imprints within a lifetime and make methylated and unmethylated alleles converge. The persistence of imprints implies collaborative maintenance (neighbouring CpGs and histone marks reinforcing each other, UHRF1 binding H3K9me3, protection of unmethylated alleles by bound factors and H3K4 methylation), which creates bistability at the level of the whole control region.
7. A CpG in a promoter is read as C in a bisulfite sequencing read, and as C in an oxBS read (in which 5hmC is first oxidized to 5fC, which is converted by bisulfite). What is the modification? What if it were C after bisulfite but T after oxBS?

   **Answer** Bisulfite converts unmodified C (and 5fC, 5caC) to U, read as T, but leaves 5mC and 5hmC as C. A C in both reads means the base was 5mC, which oxidation by the oxBS reagent does not affect. A C after bisulfite but T after oxBS means the base was 5hmC: protected in standard bisulfite, but converted after oxidation to 5fC. The difference between the two readouts at each CpG gives the 5hmC level.
8. Why is a polymerase expected to pause near the dyad of a nucleosome rather than at its entry, and how could a second, closely following polymerase help the first?

   **Answer** If the polymerase advances only when the DNA ahead has spontaneously unwrapped, its rate of advance at each position is proportional to the probability of exposure there, which falls from about $10^{-2}$ near the entry to about $10^{-4}$ near the dyad (where both gyres hold the DNA). The longest dwells are therefore in the middle of the core. A trailing polymerase prevents the leading one from backtracking and, by displacing DNA behind it, reduces the number of contacts the octamer can reestablish, so the leading polymerase advances more often; several polymerases in a convoy pass nucleosomes faster than a single one, as observed in vitro.
