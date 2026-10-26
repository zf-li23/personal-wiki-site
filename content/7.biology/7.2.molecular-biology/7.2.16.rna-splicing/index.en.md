---
title: RNA Splicing
description: Split genes and their discovery by R-looping; splice-site and branch-point consensus sequences; the two transesterifications and the lariat intermediate (evidence and kinetics); the spliceosome, its assembly cycle and cryo-EM structures; the snRNA base-pairing network and compensatory-mutation genetics; exon and intron definition, U2AF, SF1 and the Pol II CTD; alternative splicing, SR proteins, hnRNPs and splicing enhancers and silencers, Drosophila sex determination, kinetic coupling to elongation; back-splicing and circular RNA; self-splicing group I and group II introns and tRNA splicing.
---

Most genes of plants and animals are interrupted by **introns**, and **RNA polymerase** II copies them along with the **exons** ([7.2.2](/7.2.2)). Before an mRNA can leave the nucleus, every intron must be cut out and the **exons** joined with single-nucleotide precision: a shift by one nucleotide would change the reading frame of everything downstream. This chapter asks how that is possible when an intron can be tens of kilobases long and the signals that mark its ends are short and degenerate. The answer has four layers, which give the sections of the chapter: the evidence that genes are split (16.1) and the sequences that mark the boundaries (16.2); the chemistry, two transesterifications through a lariat intermediate (16.3); the machine that carries it out, the spliceosome, whose **active site** is built from RNA (16.4–16.5); and the protein factors that decide which sites are used, on which the regulation of alternative splicing rests (16.6–16.7). The chapter ends with **introns** that splice themselves (16.8), which show that the spliceosome is an RNA enzyme dressed in proteins and lead to the **RNA world hypothesis** treated in [7.2.23](/7.2.23). The other processing reactions of a pre-mRNA, capping and polyadenylation, and their coupling to transcription follow in [7.2.17](/7.2.17).

## 16.1. Genes in Pieces

### 16.1.1. The Discovery of Split Genes

Until 1977 genes were thought to be colinear with their mRNAs, as in bacteria. Two groups studying adenovirus, Berget, Moore and Sharp, and Chow, Gelinas, Broker and Roberts, found otherwise by electron microscopy of RNA–DNA hybrids.

**Example 16.1.1 (R-looping reveals introns)** A single-stranded DNA fragment containing an adenovirus late gene (the hexon gene) was hybridized to the mature hexon mRNA under conditions that favor RNA–DNA over DNA–DNA duplexes. If gene and mRNA were colinear, the electron micrograph would show one continuous hybrid. Instead it showed a hybrid with single-stranded DNA loops protruding from it: stretches of the gene with no counterpart in the mRNA, which therefore loop out. The $5'$ end of the mRNA hybridized to three short segments located far upstream (the "tripartite leader"), separated by loops of about $1$, $2.5$ and $9\,\mathrm{kb}$ from each other and from the body of the gene. The same technique applied to cellular genes, such as chicken ovalbumin (seven loops) and mouse β-globin (two), showed that interrupted genes are the rule. Roberts and Sharp received the 1993 Nobel Prize for the discovery.

**Definition 16.1.1 (RNA Splicing)** **RNA splicing** is the removal of introns from a precursor RNA and the joining of the flanking exons; the unspliced transcript is the **pre-mRNA** (or primary transcript) of a protein-coding gene.

A second possibility, that introns are never transcribed, was excluded by the existence of nuclear precursors much longer than mRNA (historically called heterogeneous nuclear RNA, hnRNA) that contain intron sequences and are processed into mRNA, as shown by pulse labeling and later by direct sequencing of nascent RNA. Splicing takes place in the nucleus, mostly while the polymerase is still transcribing the gene ([7.2.17](/7.2.17)).

### 16.1.2. How Many Introns and How Long

| Feature | Typical values |
|---|---|
| Introns per human protein-coding gene | median about 7, mean about 9; from 0 (**histone** genes) to 362 (titin) |
| Human intron length | median about $1.5\,\mathrm{kb}$; from below $70\,\mathrm{nt}$ to more than $1\,\mathrm{Mb}$ |
| Human internal exon length | about $120$–$150\,\mathrm{nt}$, narrowly distributed |
| Budding yeast | about 280 introns among 6000 genes, mostly one per gene, $60$–$1000\,\mathrm{nt}$ |
| Nuclear tRNA genes | 0 or 1 intron of about $10$–$60\,\mathrm{nt}$, always just $3'$ of the anticodon |

Exons are short and uniform while introns vary over five orders of magnitude; this asymmetry shapes how splice sites are recognized in vertebrates (16.6). Because about $95\,\%$ of a typical human pre-mRNA is intron, the cell transcribes and discards about twenty times more RNA than it exports as mRNA.

## 16.2. Splicing Signals

### 16.2.1. Splice Sites and the Branch Point

Comparison of exon–intron junctions in genes and **cDNAs** showed that almost all nuclear introns begin with GU and end with AG (the GU–AG rule; GT–AG in the DNA). The conserved dinucleotides are parts of longer, weakly conserved **consensus sequences**.

**Definition 16.2.1** The exon–intron junction at the $5'$ end of an intron is the **5′ splice site** (donor site), with mammalian consensus $\mathrm{MAG|GURAGU}$ (M = A or C, R = purine, $|$ the junction); the junction at the $3'$ end is the **3′ splice site** (acceptor site), with consensus $\mathrm{YAG|G}$ preceded by a polypyrimidine tract (Y = pyrimidine) of $10$–$20$ nucleotides. The **branch point** is the adenosine within the intron, usually $18$–$40\,\mathrm{nt}$ upstream of the $3'$ splice site, whose $2'$-OH initiates splicing; it lies within a branch-site consensus $\mathrm{YNYURAY}$ in mammals and the invariant $\mathrm{UACUA\underline{A}C}$ in budding yeast.

![The splicing signals of a mammalian intron. A: map of an intron between two exons, with the 5′ splice site (GURAGU), the branch site (YNYURAY, the branch A marked) 18–40 nt upstream of the 3′ splice site, the polypyrimidine tract (Y)n and the 3′ splice site (YAG); above, the proteins of the early complex that recognize each signal (U1 snRNP at the 5′ splice site, SF1 at the branch site, the two subunits of U2AF at the tract and the AG), and below, the yeast consensus. B: sequence logos built from classic percentages of the consensus base at each position (5′ site A64 G73 | G100 U100 A62 A68 G84 U63; branch site U47 N C63 U53 R72 A91 C47; 3′ site C65 A100 G100 after a pyrimidine-rich tract), with the remaining probability shared among the other bases; only the GU and AG are invariant, the branch A is highly conserved, and everything else carries little information](./plots/splice-signals.py)

The logo makes a quantitative point. The information content of the three signals together is about $25$–$30$ bits, whereas specifying one $5'$ and one $3'$ site among the roughly $10^5$ candidate positions of a typical intron requires about $2\log_2 10^5 \approx 33$ bits, and the genome is full of sequences that match the consensus as well as real sites do ("pseudo-sites" outnumber real sites by about tenfold). The splice sites therefore cannot be found by their sequence alone; the missing information is supplied by the exon–intron architecture (16.6) and by regulatory sequences and proteins (16.7).

### 16.2.2. Testing the Signals

**Example 16.2.1 (The branch-site sequence designates the 3′ splice site)** Langford and Gallwitz (1983) studied the yeast actin gene, whose intron contains the conserved $\mathrm{UACUAAC}$ about $40\,\mathrm{nt}$ upstream of the $3'$ splice site. Deleting this sequence, or changing it at single positions, abolished splicing; when a copy was moved, splicing used the first AG located an appropriate distance downstream of the new position. The branch-site sequence therefore does two things: it carries the branch nucleotide, and it marks the AG that will serve as the $3'$ splice site. The usual choice is the first AG downstream of the branch point within about $40\,\mathrm{nt}$; the protein Slu7 is required for selecting the correct AG, and without it aberrant AGs within $30\,\mathrm{nt}$ of the branch point are used.

Mutations at splice sites are a frequent cause of inherited disease, which shows that the consensus is functional. In β-thalassemia, a G→A change at the first position of intron 1 of the β-globin gene (IVS1-1) abolishes the $5'$ splice site, and a G→A change at position 110 of the same intron creates a new AG that competes with the normal $3'$ site; in both, the mRNA is misspliced and little β-globin is made. Estimates from exome and clinical sequencing suggest that at least a tenth of pathogenic point mutations act by changing splicing, many of them far from the GU and AG.

### 16.2.3. Minor Introns

About $0.35\,\%$ of human introns (some 700) belong to a second class, the U12-type introns, with longer and more stringent consensus sequences ($5'$ $\mathrm{|AUAUCCUU}$ or $\mathrm{|GUAUCCUU}$, branch site $\mathrm{UCCUUAAC}$, and no polypyrimidine tract); many end in AU–AC instead of GU–AG. They are removed by the minor spliceosome, in which U11, U12, U4atac and U6atac snRNAs replace U1, U2, U4 and U6, while U5 is shared. The two spliceosomes use the same chemistry and the same RNA–RNA interactions (16.5), which is itself evidence that these interactions are mechanistically central.

## 16.3. The Splicing Reaction

### 16.3.1. Two Transesterifications

**Definition 16.3.1 (Lariat)** In nuclear pre-mRNA splicing, the excised intron is released as a **lariat**: a loop closed by a $2'$–$5'$ phosphodiester bond between the guanosine at the $5'$ end of the intron and the branch-point adenosine, which is also linked $3'$–$5'$ to the next nucleotide and $5'$–$3'$ to the previous one, with a tail running to the $3'$ end of the intron.

Splicing occurs in two steps, each a transesterification, the exchange of one phosphodiester bond for another without hydrolysis.

1. The $2'$-OH of the branch-point adenosine attacks the phosphate at the $5'$ splice site. Exon 1 is released with a $3'$-OH, and the $5'$ end of the intron becomes joined to the branch A, giving the lariat intermediate (intron–exon 2).
2. The $3'$-OH of exon 1 attacks the phosphate at the $3'$ splice site. The exons are joined, and the intron is released as a lariat with a free $3'$-OH.

![The splicing reaction. A: the two transesterifications. In step 1 the 2′-OH of the branch adenosine attacks the phosphate (grey) at the 5′ splice site, freeing exon 1 with a 3′-OH and forming the lariat intermediate, in which the 5′ G of the intron is joined 2′→5′ to the branched A; in step 2 the 3′-OH of exon 1 attacks the phosphate at the 3′ splice site (red), which becomes the phosphate between the joined exons, and the lariat intron is released with a 3′-OH. B: sequential first-order kinetics of Formula 16.3.1 with k₁ = 0.05 min⁻¹ and k₂ = 0.1 min⁻¹ (illustrative): the mRNA appears after a lag, and the intermediates rise and fall with a maximum at t_max = ln(k₂/k₁)/(k₂ − k₁) ≈ 14 min](./plots/two-step-splicing.py)

Each step breaks one phosphodiester bond and makes one, so the number of bonds is conserved and the chemistry needs no external energy; the ATP consumed by splicing (several molecules per intron) drives the assembly and rearrangements of the spliceosome, not bond formation. Each step is an in-line, $\mathrm{S_N2}$-type attack on phosphorus: experiments with stereospecifically substituted phosphorothioates showed inversion of configuration at the phosphorus in each step (Moore and Sharp, 1993), as expected for two separate one-step transesterifications and not for a covalent enzyme intermediate. The two steps take place in different conformations of one active site (16.5).

### 16.3.2. Evidence for the Lariat

**Example 16.3.1 (The branched intermediate)** Grabowski, Padgett and Sharp (1984), and Ruskin, Krainer, Maniatis and Green (1984), spliced labeled adenovirus or globin pre-mRNA in nuclear extracts and separated the products by gel electrophoresis. Besides the precursor and the spliced product, two RNAs appeared: one with the size of exon 1, and one that migrated anomalously, much more slowly than its length predicted in a $10\,\%$ gel and differently in a $4\,\%$ gel, as circular and branched molecules do; the anomalous species appeared first and then declined while a second anomalous species, the free intron, accumulated. The lariat model made four predictions, all confirmed:

| Prediction | Test |
|---|---|
| The excised intron has a $3'$-OH | It can be labeled at its $3'$ end by enzymes that require a free $3'$-OH |
| The phosphate between the joined exons comes from the $3'$ splice site | A **substrate** labeled with $\alpha$-${}^{32}\mathrm{P}$ in the first nucleotide of exon 2 gave spliced RNA in which the label was on the nucleotide joined to exon 1 |
| The intron and the intermediate contain a branched nucleotide with $2'$, $3'$ and $5'$ bonds | Complete digestion with RNase T2 or P1, which cut only $3'$–$5'$ bonds, released a nuclease-resistant core: an A carrying phosphates on its $2'$, $3'$ and $5'$ positions |
| The branch joins the $5'$ end of the intron to a site within the intron | A debranching activity converted the lariat to a linear molecule; **primer extension** on the intermediate stopped at the branch point, about $30\,\mathrm{nt}$ upstream of the $3'$ splice site |

The kinetics of such a time course is that of two consecutive first-order steps.

**Formula 16.3.1 (Kinetics of the lariat intermediate)** If pre-mRNA $\mathrm{P}$ is converted to the intermediates $\mathrm{I}$ with rate constant $k_1$ and these to products $\mathrm{S}$ with rate constant $k_2$ ($k_1 \ne k_2$), the fractions starting from $\mathrm{P}(0) = 1$ are
$$
\mathrm{P}(t) = \mathrm{e}^{-k_1 t}, \qquad \mathrm{I}(t) = \frac{k_1}{k_2 - k_1}\left(\mathrm{e}^{-k_1 t} - \mathrm{e}^{-k_2 t}\right), \qquad \mathrm{S}(t) = 1 - \mathrm{P}(t) - \mathrm{I}(t), \tag{16.1}
$$
and the intermediates peak at $t_{\max} = \ln(k_2/k_1)/(k_2 - k_1)$.

This is the **consecutive reaction** of chemical kinetics ([6.3.15](/6.3.15)). It explains two features of in vitro splicing: the lag before spliced product appears ($\mathrm{S}(t) \approx k_1 k_2 t^2/2$ at short times) and the transient accumulation of intermediates, which is larger when the second step is slow. Mutations that block step 2 (at the $3'$ splice site AG, or in the factors Prp16 and Slu7) leave the intermediates stranded, which is how the two steps were separated genetically.

## 16.4. The Spliceosome

### 16.4.1. Small Nuclear Ribonucleoproteins

**Definition 16.4.1 (snRNP)** A **small nuclear ribonucleoprotein** (snRNP, "snurp") is a complex of one small nuclear RNA (snRNA, $100$–$200\,\mathrm{nt}$, uridine rich) with a ring of seven Sm proteins (Lsm proteins for U6) and proteins specific to that particle. U1, U2, U4, U5 and U6 snRNPs carry out the splicing of U2-type introns.

The Sm proteins form a doughnut-shaped heptameric ring around a single-stranded Sm site of the snRNA (consensus $\mathrm{AU_{4\text{–}6}G}$); the crystal structure of U1 snRNP (Pomeranz Krummel, Nagai and colleagues, 2009) showed the Sm ring with the U1-specific proteins U1-70K, U1-A and U1-C attached. The snRNAs U1, U2, U4 and U5 are made by Pol II, receive an $\mathrm{m^7G}$ cap, are exported to the cytoplasm, where the Sm ring is assembled and the cap is hypermethylated to $\mathrm{m^{2,2,7}G}$, and are reimported; U6 is made by Pol III ([7.2.12](/7.2.12)), keeps a $5'$-triphosphate (later capped by a γ-methyl group) and never leaves the nucleus. Systemic lupus erythematosus patients make antibodies against Sm proteins; such antibodies, which inhibit splicing in vitro, were how Lerner and Steitz (1979) first linked snRNPs to splicing.

**Definition 16.4.2 (Spliceosome)** The **spliceosome** is the large ribonucleoprotein complex, assembled on each intron from the snRNPs and more than a hundred other proteins, that catalyzes pre-mRNA splicing; it sediments at about $40\mathrm{S}$ in yeast and $60\mathrm{S}$ in mammals.

Spliceosomes were first detected as complexes of labeled pre-mRNA in nuclear extracts that sedimented at $40\mathrm{S}$ (yeast; Brody and Abelson, 1985) or $50$–$60\mathrm{S}$ (mammals; Grabowski, Seiler and Sharp, 1985); a pre-mRNA with a mutant $5'$ splice site formed the complex much less efficiently, and the complex contained the splicing intermediates. Proteomic analyses of purified spliceosomes identify about $150$–$300$ proteins, depending on the stage and on how loosely bound proteins are counted.

### 16.4.2. The Spliceosome Cycle

The spliceosome is not a preformed machine that binds introns. It is assembled stepwise on each intron, rearranged at each step by eight ATP-dependent RNA **helicases** of the DEAD/DEAH-box families, and disassembled after the reaction.

| Complex (mammalian name; yeast) | What happens | Driving factor |
|---|---|---|
| E (commitment complex, CC) | U1 snRNP pairs with the $5'$ splice site; SF1 (yeast BBP) binds the branch site; U2AF65 (yeast Mud2) binds the pyrimidine tract and U2AF35 the AG | none (ATP independent) |
| A (prespliceosome) | U2 snRNP pairs with the branch site, bulging out the branch A; SF1 is displaced | Prp5, UAP56 (ATP) |
| pre-B, B | The U4/U6·U5 tri-snRNP joins | Prp28 transfers the $5'$ site from U1 to U6 |
| $\mathrm{B^{act}}$ | Brr2 unwinds U4 from U6; U1 and U4 leave; U6 pairs with the $5'$ site and with U2 to form the catalytic core; the Prp19 complex (NTC) joins | Brr2 (ATP) |
| $\mathrm{B^*}$ → C | Step 1 | Prp2 (ATP) |
| $\mathrm{C^*}$ → P | Rearrangement and step 2 | Prp16, then Prp22 (ATP) |
| ILS | mRNA released; intron-lariat spliceosome disassembled; lariat debranched by Dbr1 and degraded; snRNPs recycled | Prp22, Prp43 (ATP) |

![The spliceosome. A: the assembly cycle of the major spliceosome on one intron, from the early (E) complex through complexes A, B, Bact, C and P to the intron-lariat spliceosome (ILS), with the DEAD/DEAH-box ATPases that drive each transition; the snRNPs are recycled for the next intron. B: base pairing in the activated spliceosome (schematic): U6 snRNA pairs with the 5′ end of the intron through its ACAGA box and with U2 snRNA in helix I, U2 pairs with the branch site and leaves the branch adenosine bulged out as the nucleophile, U6 forms an internal stem-loop (ISL) that binds the catalytic Mg²⁺ ions, and loop 1 of U5 snRNA holds the ends of both exons for step 2](./plots/spliceosome.py)

The repeated rearrangements are thought to serve fidelity as well as assembly. Each helicase acts as a timer: a substrate that reacts slowly at a given stage, because its splice site pairs poorly, is more likely to be rejected by the helicase that ends that stage and discarded, a form of **kinetic proofreading** ([6.3.18](/6.3.18)) demonstrated for Prp16 and Prp22 by Staley, Guthrie and colleagues. Splicing is correspondingly slow: in vivo an intron is removed within about $0.5$–$10\,\mathrm{min}$ of its transcription.

### 16.4.3. Structures

**Cryo-electron microscopy** has determined structures of the spliceosome in almost every stage of the cycle. The first atomic structure, of the intron-lariat spliceosome of *Schizosaccharomyces pombe* at $3.6\,\text{Å}$ (Yan, Shi and colleagues, 2015), contained 37 proteins, three snRNAs (U2, U5, U6) and the lariat, about $1.3\,\mathrm{MDa}$; the U4/U6·U5 tri-snRNP of budding yeast at $3.8\,\text{Å}$ (Wan, Shi and colleagues, 2016; Nguyen, Nagai and colleagues, 2016) and human complexes such as $\mathrm{C^*}$ (Zhang, Shi and colleagues, 2017) followed. The structures show that the protein Prp8, the largest and most conserved spliceosomal protein, forms a scaffold that holds the U5 and U6 snRNAs and the splice sites, and that the catalytic center is made of RNA: U6 snRNA binds two $\ce{Mg^2+}$ ions through phosphates of its internal **stem-loop**, positioned against the reacting phosphodiester as in a group II intron (16.8). Fica, Staley, Piccirilli and colleagues (2013) had shown by metal-rescue experiments with phosphorothioate-substituted U6 that these U6 phosphates coordinate the catalytic metals in both steps. The spliceosome is therefore a **ribozyme** ([7.1.8](/7.1.8)) whose RNA catalytic core is assembled, held and remodeled by proteins.

## 16.5. The snRNA Base-Pairing Network

The snRNAs recognize the splicing signals and each other by base pairing, and these interactions change during the cycle. Each was proved by the same genetic logic: a mutation in the pre-mRNA that disrupts a proposed **base pair** blocks splicing, and a compensatory mutation in the snRNA that restores the pair restores splicing, whereas the snRNA mutation alone does not help (allele-specific suppression, as for **σ factors** in [7.2.10](/7.2.10)).

**Example 16.5.1 (U1 snRNA pairs with the 5′ splice site)** The $5'$ end of U1 snRNA, $3'$-$\mathrm{GUCCAUUCA}$-$5'$, is complementary to the $5'$ splice-site consensus $\mathrm{CAG|GUAAGU}$ (Lerner and Steitz; Rogers and Wall, 1980). Zhuang and Weiner (1986) tested this with the adenovirus E1A gene, whose pre-mRNA can be spliced at two alternative $5'$ sites to give 12S and 13S mRNAs. A mutation in the 12S $5'$ site that weakened its pairing with U1 abolished 12S splicing in transfected cells (measured by RNase protection, [7.2.6](/7.2.6)); coexpression of a mutant U1 snRNA with the compensating base change restored 12S splicing, while wild-type U1 did not. A second mutation that could also be compensated in U1 was not rescued: pairing with U1 is necessary but not sufficient, because the $5'$ site is also read later by U6.

**Example 16.5.2 (U2 snRNA pairs with the branch site)** Parker, Siliciano and Guthrie (1987) used a yeast intron fused to *HIS4*, so that splicing allowed growth without histidine. Mutations in the branch-site sequence $\mathrm{UACUAAC}$ reduced splicing and growth; compensatory mutations in the complementary region of U2 snRNA ($\mathrm{GUAGUA}$, which pairs with $\mathrm{UACUAC}$ and leaves the branch A unpaired) restored splicing of the mutant intron. The bulged A, pushed out of the U2–branch-site helix, is exactly the nucleotide whose $2'$-OH attacks in step 1.

The other interactions were found in the same way and by cross-linking with photoreactive nucleotides (4-thiouridine) placed in the pre-mRNA:

| snRNA | Pairs with | Role |
|---|---|---|
| U1 | $5'$ splice site (exon $-3$ to intron $+6$) | First recognition of the $5'$ site (E complex); released at activation |
| U2 | Branch site; U6 (helices I and II) | Bulges the branch A; positions it next to the $5'$ site through helix I |
| U4 | U6 (stems I and II) | Holds U6 inactive until activation; U6 bases that pair with U4 in stem I later pair with U2 in helix I, which is why U4 must be removed |
| U5 | Last nucleotides of exon 1 and first of exon 2 (loop 1, non-Watson–Crick contacts) | Aligns the two exons for step 2 |
| U6 | Intron $+4$ to $+6$ (invariant $\mathrm{ACA}$ of the ACAGA box with $\mathrm{UGU}$); U2; internal stem-loop | Replaces U1 at the $5'$ site; binds the catalytic $\ce{Mg^2+}$ |

The network explains several otherwise puzzling facts. The $5'$ splice site is read twice, first by U1 and then by U6, which is a **proofreading** step. The exchange of partners (U4/U6 to U2/U6, U1 to U6 at the $5'$ site) is the actual activation of the spliceosome and is driven by helicases. And U6, the most conserved snRNA, forms the core of the active site together with U2, in an arrangement that closely resembles domains V and VI of group II self-splicing introns (16.8).

## 16.6. Finding the Sites: Exon Definition, Intron Definition and the CTD

### 16.6.1. Bridging Across Introns and Exons

snRNPs alone do not have the specificity and affinity to find splice sites; proteins of the E complex bind to the signals and to each other and so pair the right $5'$ site with the right branch point and $3'$ site.

**Example 16.6.1 (A protein bridge across the intron)** In yeast, the branchpoint bridging protein BBP binds the branch-site RNA. Abovich and Rosbash (1997) found by synthetic-lethal genetic screens and by **yeast two-hybrid** assays ([7.2.14](/7.2.14)) that BBP also binds Prp40, a protein of U1 snRNP at the $5'$ splice site, and Mud2, which binds near the $3'$ end of the intron. BBP thus forms a protein bridge between the two ends of the intron before any snRNA–snRNA interaction exists. Its mammalian counterpart SF1 binds the branch site, and U2AF65 (the Mud2 **homolog**) binds the pyrimidine tract while its partner U2AF35 contacts the AG of the $3'$ splice site.

**Definition 16.6.1** When the splicing machinery is first assembled across an exon, by interactions between factors at the $3'$ splice site upstream of the exon and the $5'$ splice site downstream of it, the mode of recognition is **exon definition**; when it is assembled across an intron, it is **intron definition**.

Vertebrate exons are short (about $140\,\mathrm{nt}$) and introns long, so the sites on the two sides of an exon are close and are recognized together (Robberson, Cote and Berget, 1990): in vertebrates, a mutation in the $5'$ site downstream of an exon often causes that whole exon to be skipped, rather than the intron to be retained, because the exon is no longer defined. Yeast and *Drosophila* introns are short, often shorter than the flanking exons, and are recognized by intron definition; mutations then cause intron retention. After an exon has been defined, its neighboring exons must still be joined across the intron, by a switch from cross-exon to cross-intron complexes.

### 16.6.2. The CTD Couples Splicing to Transcription

**Example 16.6.2 (The CTD stimulates exon definition)** Zeng and Berget (2000) added the **carboxyl-terminal domain** (CTD) of Pol II ([7.2.12](/7.2.12)), as a fusion with glutathione-*S*-transferase (CTD–GST), to in vitro splicing reactions. The phosphorylated CTD stimulated splicing of substrates that require exon definition (a substrate with a complete second exon ending in a $5'$ splice site) by about 3- to 5-fold, but did not stimulate substrates that can be spliced by intron definition, nor substrates whose downstream exon was incomplete. The CTD therefore helps to assemble factors across exons; in vivo it binds splicing factors through its Ser2-phosphorylated repeats ([7.2.13](/7.2.13)), so that the factors are delivered to each exon as it emerges from the polymerase.

Because splicing is mostly cotranscriptional, the position of an intron in the gene matters. The first intron is removed efficiently only when the pre-mRNA has a cap, which is bound by the cap-binding complex (CBC) that helps U1 bind the first $5'$ site; the last intron is removed efficiently only when a functional polyadenylation signal is present, which defines the terminal exon ([7.2.17](/7.2.17)). After splicing, the spliceosome deposits an exon junction complex (EJC, Definition 16.6.2) about $20$–$24\,\mathrm{nt}$ upstream of each exon–exon junction; the EJC marks the mRNA as spliced, stimulates its export and translation, and is the signal by which premature stop codons are detected ([7.2.18](/7.2.18)).

**Definition 16.6.2 (Exon Junction Complex)** The **exon junction complex** is a protein complex (core eIF4AIII, MAGOH, Y14 and CASC3) deposited by the spliceosome about $20$–$24$ nucleotides upstream of exon–exon junctions of a spliced mRNA, independently of sequence, and removed by the first translating ribosome.

## 16.7. Alternative Splicing

### 16.7.1. One Gene, Several Proteins

**Definition 16.7.1 (Alternative Splicing)** **Alternative splicing** is the production of two or more mature mRNAs from one pre-mRNA by different choices of splice sites.

The first case was the mouse **immunoglobulin** μ heavy chain (Early, Hood and colleagues; Alt, Baltimore and colleagues, 1980): one gene gives the membrane-bound form μm, whose C-terminus has a hydrophobic membrane anchor, in B cells, and the secreted form μs, without the anchor, in plasma cells, by the choice between an internal $5'$ splice site and a polyadenylation site upstream of it. The basic patterns are shown in the figure. Two further types change the ends of the mRNA: alternative **promoters** give alternative first exons, and alternative polyadenylation sites give alternative last exons (as for μm/μs and for the rat calcitonin gene, which makes calcitonin in the thyroid and calcitonin gene-related **peptide**, CGRP, in neurons).

Alternative splicing is the rule, not the exception. Deep sequencing of human **transcriptomes** (Pan, Blencowe and colleagues; Wang, Burge and colleagues, 2008) found that about $95\,\%$ of multi-exon genes produce more than one isoform, most of them differing between tissues. The extreme is the *Drosophila* gene *Dscam*, a cell-surface **receptor** of neurons: its exons 4, 6, 9 and 17 are chosen from mutually exclusive clusters of 12, 48, 33 and 2 alternatives, so that the gene can produce $12 \times 48 \times 33 \times 2 = 38\,016$ isoforms, used to give each neuron a distinct surface identity. Not every alternative mRNA makes a protein: many alternative exons introduce premature stop codons and target the mRNA for decay ([7.2.18](/7.2.18)), so that splicing can also switch a gene off.

**Remark 16.7.1** The statement in some lecture notes that about $5\,\%$ of eukaryotic pre-mRNAs are alternatively spliced reflects estimates from the 1990s, based on a few cDNA comparisons; the current value for human multi-exon genes is about $95\,\%$, although for many genes one isoform dominates.

### 16.7.2. Regulators: SR Proteins and hnRNPs

Whether an exon is included depends on how well its splice sites are recognized, and that is regulated by proteins bound to short sequences in the exons and introns.

**Definition 16.7.2** An **exonic splicing enhancer** (ESE) is a short sequence within an exon that stimulates the use of the adjacent splice sites, typically by binding an SR protein; an **exonic splicing silencer** (ESS) is one that inhibits them, typically by binding an hnRNP protein. Intronic splicing enhancers and silencers (ISE, ISS) act from within introns.

**Definition 16.7.3 (SR Protein)** An **SR protein** is a member of a family of RNA-binding proteins with one or two RNA-recognition motifs (RRMs) and a C-terminal domain rich in alternating serine and arginine (the RS domain), which binds exonic enhancers and recruits U1 snRNP and U2AF to the adjacent splice sites; SR proteins are now named SRSF1–SRSF12.

**Example 16.7.1 (One SR protein suffices for commitment)** Fu (1993) preincubated human β-globin pre-mRNA with the SR protein SC35 (SRSF2) and then challenged it with a large excess of competitor RNA before adding nuclear extract. Without preincubation the competitor sequestered the splicing factors and splicing failed; after preincubation with SC35 alone, splicing proceeded, about 40-fold better than without SC35: SC35 had committed the pre-mRNA to splicing. Commitment was fast (within a minute), occurred even on ice and without ATP or $\ce{Mg^2+}$, and was specific: of several SR proteins, SC35 worked best on β-globin, while on HIV *tat* pre-mRNA only SF2/ASF (SRSF1) caused commitment. Different pre-mRNAs thus depend on different SR proteins, which is a basis for tissue-specific splicing, since SR protein levels differ between tissues.

Heterogeneous nuclear ribonucleoproteins (hnRNPs), the abundant proteins that coat nascent pre-mRNA, often act oppositely. hnRNP A1, bound to an ESS in the third exon of HIV *tat*, represses the use of the exon by at least three mechanisms, each supported at different exons: cooperative spreading of A1 molecules from the **silencer** along the exon, which blocks the binding of SR proteins and U2AF; binding to sites on both sides of an exon, which loops the exon out; and direct competition with U2AF or SR proteins for the splice sites. The final choice is a balance of positive and negative factors, and the "splicing code" that predicts it from sequence is now learned by neural-network models trained on transcriptome data.

The same principle has become a therapy. In spinal muscular atrophy, the *SMN1* gene is lost, and its **paralog** *SMN2* cannot compensate because a silent C→T change in exon 7 weakens an ESE and creates an ESS, so that exon 7 is usually skipped. The antisense oligonucleotide nusinersen (approved in 2016) pairs with an intronic silencer (ISS-N1) in intron 7, blocks the binding of hnRNP A1/A2 there, and restores exon 7 inclusion and SMN protein.

### 16.7.3. Sex Determination in *Drosophila*

**Example 16.7.2 (A cascade of regulated splicing)** The sex of a fruit fly is determined by a cascade of three genes whose pre-mRNAs are alternatively spliced: *Sxl* (Sex lethal), *tra* (transformer) and *dsx* (doublesex).

1. In females, which have two X chromosomes, a dose-dependent early promoter produces Sxl protein. Sxl binds the pre-mRNA of its own gene and causes the skipping of a male-specific exon that contains a stop codon, so that female cells keep making Sxl (positive autoregulation, a memory of the early decision).
2. Sxl binds the polypyrimidine tract of the default $3'$ splice site in the first intron of *tra* pre-mRNA, blocks U2AF there, and forces the use of a downstream, female-specific $3'$ site; only this mRNA encodes functional Tra. In males, without Sxl, the default site is used and the mRNA contains a stop codon.
3. Tra, with the constitutive SR protein Tra-2, binds six copies of a 13-nt repeat in exon 4 of *dsx* pre-mRNA, about $300\,\mathrm{nt}$ downstream of a weak female-specific $3'$ splice site, and activates that site, so the female mRNA includes exon 4 and is polyadenylated after it (Dsx-F). In males exon 4 is skipped, and the mRNA ends with exons 5 and 6 (Dsx-M). The two Dsx proteins are transcription factors with the same DNA-binding domain and different C-termini, which activate female or male differentiation genes.

The cascade combines a **repressor** of a $3'$ splice site (Sxl, an RRM protein of the hnRNP type, not an SR protein), an **activator** through an **enhancer** (Tra and Tra-2, SR-type proteins) and a default pathway. The statement that both Sxl and Tra are SR proteins is incorrect; only Tra and Tra-2 have RS domains.

### 16.7.4. Kinetic Coupling to Elongation

Because exons are recognized while the polymerase is still moving, the speed of the polymerase can influence the choice between sites. A weak site that is transcribed earlier has a head start over a strong competing site that appears later, and the head start lasts as long as it takes the polymerase to reach the competitor.

**Formula 16.7.1 (Window of opportunity)** Let the weak $3'$ splice site of a cassette exon be committed to splicing with rate constant $k$ from the moment it is transcribed, and let the competing strong $3'$ splice site of the downstream exon, a distance $d$ further along the gene, be committed with rate constant $k_{\mathrm{s}}$ once it is transcribed by a polymerase moving at speed $v$. The fraction of transcripts that include the exon is
$$
\Psi = 1 - \mathrm{e}^{-kd/v} + \mathrm{e}^{-kd/v}\,\frac{k}{k + k_{\mathrm{s}}}. \tag{16.2}
$$
The first two terms are the probability of commitment during the window $d/v$; the last term is the chance of winning the competition after it.

Slower elongation lengthens the window and raises inclusion of exons with weak upstream sites. De la Mata, Kornblihtt and colleagues (2003) tested this with a mutant Pol II subunit (C4) that elongates about twice as slowly: in transfected cells, inclusion of the alternative EDI exon of fibronectin rose several-fold, and inhibitors of elongation had the same effect; conversely, ultraviolet irradiation, which hyperphosphorylates the CTD and slows elongation, changes splicing of many genes. The model also predicts that the effect depends on intron length and on **chromatin**, which slows the polymerase over nucleosome-dense exons ([7.2.15](/7.2.15)). Recruitment of splicing factors by the CTD (Example 16.6.2) and kinetic competition are two complementary forms of the coupling of splicing to transcription.

![Alternative splicing. A: six patterns drawn as pre-mRNAs with constitutive (dark) and alternatively used (light) regions; the junctions above each pre-mRNA make one isoform and those below the other: constitutive splicing, a cassette exon included or skipped, mutually exclusive exons, alternative 5′ splice sites, alternative 3′ splice sites, and intron retention. B: the window-of-opportunity model, Eq. (16.2), for a cassette exon whose competitor lies 2 kb downstream (k_s = 0.1 s⁻¹), with two values of the commitment rate constant k of its weak site; the shaded band marks typical Pol II elongation rates, filled points the inclusion at 3 kb min⁻¹ and open points at half that speed, as for a slow polymerase mutant](./plots/alternative-splicing.py)

### 16.7.5. Back-Splicing and Circular RNA

Occasionally the spliceosome joins a downstream $5'$ splice site to an upstream $3'$ splice site, so that an exon (or several) is closed into a ring by a $3'$–$5'$ phosphodiester bond. Back-splicing is favored when the flanking introns contain inverted repeats, such as Alu elements in primates, that pair and bring the sites together.

**Definition 16.7.4 (Circular RNA)** A **circular RNA** (circRNA) is a covalently closed single-stranded RNA produced by back-splicing, in which the $5'$ splice site of an exon is joined to the $3'$ splice site of the same or an upstream exon.

Thousands of circRNAs are found in human cells, usually at a few percent of the level of the linear mRNA from the same gene; lacking ends, they resist exonucleases and are long-lived. A few have clear functions: the circRNA CDR1as (ciRS-7) has about 70 binding sites for the microRNA miR-7 and is abundant in neurons, and its loss in mice alters miR-7 levels and brain function ([7.2.18](/7.2.18)). Most circRNAs are probably by-products of splicing.

## 16.8. Self-Splicing RNAs

### 16.8.1. Group I Introns

**Example 16.8.1 (An intron that removes itself)** The nuclear pre-rRNA of the ciliate *Tetrahymena thermophila* contains a 413-nt intron in its 26S rRNA sequence. Cech and colleagues (1981–1982) found that the intron was excised in vitro from precursor made in isolated nuclei, and then from precursor transcribed from a cloned gene by bacterial RNA polymerase, in the complete absence of nuclear proteins. Splicing required only $\ce{Mg^2+}$, monovalent salt and a guanosine nucleotide (GTP, GMP or guanosine; not other nucleotides), and the excised intron carried an extra G at its $5'$ end. Precursor treated with proteinase, SDS and phenol still spliced. Exon ligation was confirmed by reverse transcription and sequencing across the junction. The RNA itself was the catalyst; Cech shared the 1989 Nobel Prize with Altman, who had shown the same for the RNA of RNase P ([7.2.17](/7.2.17)).

**Definition 16.8.1 (Self-Splicing Intron)** A **self-splicing intron** is an intron that catalyzes its own excision in vitro without proteins. In a **group I intron**, the $3'$-OH of an exogenous guanosine bound in the intron's G-binding site attacks the $5'$ splice site; in a **group II intron**, the $2'$-OH of a bulged adenosine within the intron attacks the $5'$ splice site, forming a lariat.

In a group I intron, step 1 attaches the guanosine to the $5'$ end of the intron and frees exon 1 with a $3'$-OH; in step 2 the $3'$-OH of exon 1 attacks the phosphate after the last nucleotide of the intron (always a G, called ωG, which occupies the same G-binding site), joining the exons and releasing the linear intron. The intron then cyclizes twice, losing short oligonucleotides, and a shortened form, the L-19 IVS, acts as a true enzyme with multiple turnover ([7.2.23](/7.2.23)). The catalytic core is a conserved set of about ten paired helices (P1–P10) folded into a compact tertiary structure that positions two metal ions at the reacting phosphate. In vivo, many group I introns are helped by proteins, some encoded by the intron itself (maturases), which stabilize the fold. Group I introns occur in rRNA, tRNA and mRNA genes of organelles, bacteriophages and bacteria and in nuclear rRNA genes of protists and fungi; some encode homing endonucleases that make them mobile.

### 16.8.2. Group II Introns and the Origin of the Spliceosome

Group II introns are found in organellar genes of fungi, plants and algae and in bacteria. Their chemistry is that of the spliceosome: a lariat intermediate, a branch A with $2'$, $3'$ and $5'$ linkages, and two transesterifications. Their six helical domains include domain VI, which carries the bulged branch A, and domain V, a short hairpin with a catalytic AGC triad that binds two $\ce{Mg^2+}$ ions. Crystal structures of a group II intron (Toor, Pyle and colleagues, 2008) and the later cryo-EM structures of the spliceosome showed that domain V superimposes on the U6 internal stem-loop and U2–U6 helix I, with the same metal ions in the same places. This resemblance supports the view that nuclear introns and the snRNAs descend from group II introns that invaded early eukaryotic genomes: the self-splicing intron was broken into pieces, the snRNAs, that act in *trans* on many introns, and these introns lost the domains that the snRNAs now supply. Mobile group II introns encode a reverse transcriptase that lets the excised lariat insert itself into DNA by reverse splicing; such retroelements are also thought to be ancestors of non-LTR retrotransposons and telomerase ([7.2.9](/7.2.9)).

### 16.8.3. Four Classes of Introns

| Class | Where | First attack | Intermediate | Catalyst |
|---|---|---|---|---|
| Group I | Organelles, phages, bacteria, protist and fungal nuclear rRNA | $3'$-OH of free guanosine | None (linear intron) | Intron RNA (two $\ce{Mg^2+}$) |
| Group II | Organelles of fungi and plants, bacteria | $2'$-OH of bulged A in the intron | Lariat | Intron RNA (domain V) |
| Spliceosomal (U2- and U12-type) | Nuclear pre-mRNAs of eukaryotes | $2'$-OH of branch A | Lariat | snRNAs U2/U6 (or U12/U6atac) with Prp8 and other proteins |
| tRNA introns | Nuclear tRNA genes of eukaryotes; archaea | Protein endonuclease | $2',3'$-cyclic phosphate and $5'$-OH ends | Splicing endonuclease and RNA ligase (proteins) |

tRNA splicing differs chemically from the other three, which all use transesterification. The tRNA-splicing endonuclease recognizes the shape of the pre-tRNA, not an intron sequence, and cuts at both ends of the intron, which lies just $3'$ of the anticodon; the two tRNA halves, with a $2',3'$-cyclic phosphate and a $5'$-OH, are joined by an RNA ligase. In yeast the ligase Trl1 uses ATP and GTP and leaves a $2'$-phosphate at the junction, which is removed by a separate phosphotransferase; in vertebrates and archaea the ligase RtcB joins the ends directly using GTP. The same ligase splices the mRNA of the transcription factor XBP1 during the unfolded-protein response, after the endonuclease IRE1 has cut out a 26-nt intron in the cytoplasm.

## Summary

| Topic | Key points |
|---|---|
| Split genes (Definition 16.1.1) | R-looping of adenovirus and ovalbumin (Example 16.1.1); human genes: median about 7 introns, introns median $1.5\,\mathrm{kb}$, exons about $140\,\mathrm{nt}$; about $95\,\%$ of a pre-mRNA is intron |
| Signals (Definition 16.2.1) | $5'$ $\mathrm{MAG|GURAGU}$, branch $\mathrm{YNYURAY}$ ($\mathrm{UACUAAC}$ in yeast) $18$–$40\,\mathrm{nt}$ upstream of $3'$ $\mathrm{(Y)_nYAG|G}$; branch site designates the AG (Example 16.2.1); signals carry too little information alone; U12-type minor introns |
| Chemistry (Definition 16.3.1) | Two transesterifications: branch $2'$-OH attacks $5'$ site, then exon $3'$-OH attacks $3'$ site; no net bond change, inversion at P; lariat evidence (Example 16.3.1); consecutive kinetics Eq. (16.1) |
| Spliceosome (Definitions 16.4.1–16.4.2) | U1, U2, U4, U5, U6 snRNPs with Sm/Lsm rings; assembled per intron E → A → B → $\mathrm{B^{act}}$ → C → P → ILS, driven by eight helicases that also proofread; cryo-EM: Prp8 scaffold, U6-bound $\ce{Mg^2+}$, a ribozyme |
| RNA network (Examples 16.5.1–16.5.2) | Compensatory mutations: U1 and then U6 pair with the $5'$ site, U2 with the branch site (bulged A), U2–U6 helix I, U4 sequesters U6, U5 aligns exons |
| Site recognition (Definitions 16.6.1–16.6.2) | BBP/SF1–U1–Mud2/U2AF bridges (Example 16.6.1); exon definition in vertebrates, intron definition in yeast; CTD stimulates exon definition (Example 16.6.2); cap and poly(A) needed for first and last introns; EJC |
| Alternative splicing (Definitions 16.7.1–16.7.4) | μm/μs; about $95\,\%$ of human multi-exon genes; *Dscam* 38016 isoforms; ESE/SR proteins versus ESS/hnRNPs (Example 16.7.1); nusinersen; *Sxl* → *tra* → *dsx* (Example 16.7.2); window of opportunity Eq. (16.2); back-splicing and circRNA |
| Self-splicing (Definition 16.8.1) | Group I: exogenous G, linear intron (Example 16.8.1); group II: lariat, domain V ≈ U6 ISL, ancestors of the spliceosome; tRNA introns cut by protein endonuclease and joined by ligase |

## Questions

1. The information content of the $5'$ splice site, branch site and $3'$ splice site together is about $25$–$30$ bits. Estimate how many sequences that match the consensus as well as an average real site would occur by chance in a $20\,\mathrm{kb}$ intron, and explain what additional information the cell uses.

   **Answer** A site with $I$ bits of information is matched by chance about once every $2^I$ positions. The $5'$ splice site alone carries about $8$–$9$ bits, so a $20\,\mathrm{kb}$ intron contains about $2\times10^4/2^{8.5} \approx 50$ sequences as good as an average real $5'$ site, and similarly dozens of candidate $3'$ sites with branch sites (about $10$–$15$ bits for the branch site, tract and AG together, giving a few to tens of matches). Exactly one pair is used. The extra information comes from architecture (exon definition pairs a $3'$ and a $5'$ site separated by about $50$–$300\,\mathrm{nt}$, the usual exon size; pseudo-exons are usually too long or too short), from enhancers and silencers bound by SR proteins and hnRNPs, from the order of transcription and the CTD (sites are presented in sequence as they emerge), and from proofreading by spliceosomal helicases.

2. In the experiment of Example 16.3.1, the substrate was labeled with ${}^{32}\mathrm{P}$ only in the phosphate at the $3'$ splice site (between the last intron nucleotide and the first nucleotide of exon 2). Where does the label end up under the lariat model, and where would it end up if the intron were removed as in RtcB-type tRNA splicing, by two endonucleolytic cuts that leave $2',3'$-cyclic phosphates on the upstream fragments and $5'$-OH ends downstream, followed by ligation?

   **Answer** In the lariat model, step 1 does not touch the $3'$ splice-site phosphate, so after step 1 the label is still between the intron and exon 2 in the lariat intermediate. In step 2 the $3'$-OH of exon 1 attacks this phosphate and the intron leaves with a $3'$-OH, so the labeled phosphate becomes the bond between exons 1 and 2. In the endonuclease–ligase scheme, the cut at the $3'$ splice site leaves the labeled phosphate on the $3'$ end of the intron (as a cyclic phosphate), exon 2 receives a $5'$-OH, and the junction phosphate is the cyclic phosphate of exon 1, which comes from the $5'$ splice site. The spliced RNA would then be unlabeled and the excised intron labeled. Finding the label in the exon junction, and a $3'$-OH on the excised intron, therefore distinguishes transesterification from cleavage and ligation.

3. Using Eq. (16.1), show that the maximal fraction of intermediates is $\mathrm{I}_{\max} = (k_1/k_2)^{k_2/(k_2-k_1)}$ and evaluate it for $k_2/k_1 = 2$ and $k_2/k_1 = 0.2$. Why do mutants that slow step 2 accumulate intermediates?

   **Answer** At $t_{\max}$, $\mathrm{d}\mathrm{I}/\mathrm{d}t = 0$ gives $k_1\mathrm{e}^{-k_1 t} = k_2\mathrm{e}^{-k_2 t}$, so $\mathrm{e}^{-k_2 t_{\max}} = (k_1/k_2)\mathrm{e}^{-k_1 t_{\max}}$ and $\mathrm{I}_{\max} = \frac{k_1}{k_2-k_1}\mathrm{e}^{-k_1 t_{\max}}(1 - k_1/k_2) = (k_1/k_2)\mathrm{e}^{-k_1 t_{\max}}$. With $t_{\max} = \ln(k_2/k_1)/(k_2-k_1)$, $\mathrm{e}^{-k_1 t_{\max}} = (k_1/k_2)^{k_1/(k_2-k_1)}$, hence $\mathrm{I}_{\max} = (k_1/k_2)^{k_2/(k_2-k_1)}$. For $k_2/k_1 = 2$: $(1/2)^2 = 0.25$, the curve of the figure. For $k_2/k_1 = 0.2$: $k_1/k_2 = 5$ and $k_2/(k_2-k_1) = 0.2/(0.2-1) = -0.25$, so $\mathrm{I}_{\max} = 5^{-0.25} \approx 0.67$. When step 2 is slow, intermediates form faster than they are consumed and approach the full amount of RNA; a block of step 2 strands them completely.

4. A patient's β-globin gene carries a G→A mutation at position $+1$ of intron 2. Predict the consequences for splicing in erythroid cells, and how they would differ if the same mutation occurred in a short intron of a yeast gene.

   **Answer** Loss of the invariant G at the $5'$ splice site abolishes pairing with U1 and U6 at that site. In vertebrates, which define exons, the most common result is skipping of the upstream exon (exon 2 is no longer defined because its downstream $5'$ site is lost), sometimes the use of a cryptic $5'$ site nearby, and less often retention of intron 2. Each product changes the reading frame or introduces a premature stop codon, so the mRNAs are degraded by nonsense-mediated decay and little β-globin is made (β⁰-thalassemia). In yeast, which uses intron definition for short introns, the usual result is retention of the intron, and the unspliced pre-mRNA is retained in the nucleus or degraded.

5. Explain why the U4–U6 interaction must be disrupted before step 1, using the overlap between the U6 nucleotides that pair with U4 and those that pair with U2. What would a mutation that stabilizes U4–U6 pairing do, and how could a compensating mutation elsewhere rescue it?

   **Answer** The U6 nucleotides that form stem I with U4 are the same ones that, after activation, pair with U2 in helix I and form part of the catalytic internal stem-loop; while U4 is bound, U6 cannot adopt its active structure. U4 is thus a chaperone and an inhibitor, released by the helicase Brr2 at the B → $\mathrm{B^{act}}$ transition. A hyperstabilizing mutation in stem I would slow or block activation (cold-sensitive phenotypes are typical, because low temperature further stabilizes the helix); it could be suppressed by a mutation in U4 that weakens stem I again, or by a hyperactive Brr2 that unwinds it faster, which is the type of suppressor genetics that defined these interactions.

6. Use Eq. (16.2) to compute the inclusion of a cassette exon with $k = 0.005\,\mathrm{s^{-1}}$, $k_{\mathrm{s}} = 0.1\,\mathrm{s^{-1}}$ and $d = 2\,\mathrm{kb}$ at elongation rates of $3$ and $1.5\,\mathrm{kb\,min^{-1}}$. What if the intron downstream of the exon were $20\,\mathrm{kb}$ long?

   **Answer** At $3\,\mathrm{kb\,min^{-1}} = 50\,\mathrm{nt\,s^{-1}}$ the window is $d/v = 40\,\mathrm{s}$, $kd/v = 0.2$, $\mathrm{e}^{-0.2} = 0.819$, and $\Psi = 1 - 0.819 + 0.819 \times 0.005/0.105 = 0.181 + 0.039 = 0.22$. At half the speed the window is $80\,\mathrm{s}$, $\mathrm{e}^{-0.4} = 0.670$, $\Psi = 0.330 + 0.032 = 0.36$: inclusion rises by about two-thirds. With $d = 20\,\mathrm{kb}$ the window is $400\,\mathrm{s}$ even at the normal speed, $\mathrm{e}^{-2} = 0.135$ and $\Psi \approx 0.87$; halving the speed then gives $\Psi \approx 0.98$, a small change. Kinetic coupling is therefore strongest for exons followed by short introns and weak upstream sites, as observed.

7. Female *Drosophila* lacking functional *tra* develop as males, but males carrying a *tra* cDNA that encodes the female protein develop as females. Explain both results with Example 16.7.2, and predict the phenotype of an XX fly lacking *dsx* entirely.

   **Answer** Without functional Tra, *dsx* pre-mRNA follows the default (male) pattern even in XX flies, so Dsx-M is made and the fly develops male somatic characteristics (XX pseudomales). A cDNA encoding female Tra bypasses the splicing step regulated by Sxl, so Tra and Tra-2 activate the female $3'$ splice site of *dsx* in XY flies, Dsx-F is made, and the fly develops as a female. Without *dsx*, neither Dsx-F nor Dsx-M is present; XX (and XY) flies develop as intersexes, with a mixture of male and female features, because the two Dsx isoforms are needed to repress the genes of the opposite sex. The phenotypes show that the cascade is linear, with *dsx* the output and *tra* the regulated switch.

8. Group I introns need an exogenous guanosine, group II introns do not. How does this difference determine the form of the excised intron, and which of the two do spliceosomal introns resemble? Give two pieces of evidence that the resemblance reflects common ancestry rather than convergence.

   **Answer** In group I splicing the nucleophile of step 1 is an external guanosine, so the $5'$ end of the intron becomes joined to that guanosine and the intron is released as a linear molecule (which may later cyclize). In group II splicing the nucleophile is the $2'$-OH of an adenosine within the intron, so the intron's $5'$ end becomes joined to its own interior, forming a lariat. Spliceosomal introns resemble group II introns. Evidence for common ancestry: (1) the catalytic structures superimpose: U6 ISL and U2–U6 helix I correspond to domain V, with the same two $\ce{Mg^2+}$ ions coordinated by equivalent phosphates, and the bulged branch A of the U2–branch-site helix corresponds to the bulged A of domain VI; (2) Prp8, the central spliceosomal protein, contains a reverse-transcriptase-like and an endonuclease-like domain related to those of the maturases encoded by group II introns; in addition, fragments of group II introns can splice in *trans* when supplied as separate RNAs, showing how a self-splicing intron could be split into snRNA-like pieces.
