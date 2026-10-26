---
title: Eukaryotic RNA Polymerases and Their Promoters
description: The three nuclear RNA polymerases (separation by ion-exchange chromatography, nucleolar and nucleoplasmic location, products, α-amanitin sensitivity); subunit composition and homology with the bacterial enzyme, the carboxyl-terminal domain of Rpb1 and the IIA/IIO forms; the structure of Pol II (cleft, clamp, bridge helix, trigger loop, nucleotide selection); class II core promoters (TATA box, BRE, initiator, MTE, DPE; focused and dispersed promoters) and the deletion and linker-scanning experiments that defined them; proximal promoter elements; class I and class III promoters; enhancers and silencers.
---

A bacterium makes all of its RNA with one **RNA polymerase** whose **σ factor** reads the promoter ([7.2.10](/7.2.10)). The eukaryotic nucleus divides this work among three polymerases, each with its own class of genes and its own kind of promoter, and none of them can find a promoter on its own. This chapter describes the enzymes and the DNA signals they respond to: how the three polymerases were separated and assigned to their genes, what their **subunits** and structure reveal about the catalytic mechanism and its kinship with the bacterial enzyme, and how **promoters** of the three classes were dissected by deletion and substitution mutagenesis. The proteins that read these promoters, the general transcription factors, are the subject of [7.2.13](/7.2.13); the gene-specific **activators** that bind enhancers, and the **chromatin** in which all of this happens, follow in [7.2.14](/7.2.14) and [7.2.15](/7.2.15). The methods used throughout (**S1 mapping**, **primer extension**, run-off transcription, footprinting) are described in [7.2.6](/7.2.6).

The question behind all four chapters is the one with which the course lectures on eukaryotic transcription open: every cell of a multicellular organism contains the same genome, yet a neuron and a hepatocyte express different subsets of their roughly 20 000 protein-coding **genes** (typically $10^4$ of them in any one cell type). Gene expression can be regulated at every step from **transcription** to protein degradation, but initiation of transcription is the step regulated most often, because it is the first and most economical point of control: a transcript that is never made costs nothing.

## 12.1. Three Nuclear RNA Polymerases

### 12.1.1. Separation and Localization

The genes for the large ribosomal RNAs are unlike other nuclear genes. They are GC-rich (about $60\%$ GC), present in hundreds to thousands of tandem copies, and transcribed in a separate compartment, the nucleolus. This suggested that **eukaryotes** might have at least two **RNA polymerases**, one for rRNA in the nucleolus and one or more for the other genes in the nucleoplasm.

**Example 12.1.1 (Separation by ion-exchange chromatography)** Roeder and Rutter (1969) applied extracts of sea urchin embryo nuclei to DEAE-Sephadex, an anion exchanger, and eluted the bound proteins with a gradient of increasing ammonium sulfate concentration (**ion-exchange chromatography**). Fractions were assayed for protein ($A_{280}$) and for RNA polymerase activity, measured as the incorporation of labeled UMP into acid-insoluble RNA on a DNA template. Activity eluted in three peaks, named in order of elution RNA polymerases I, II and III. The peaks did not coincide with the major protein peaks: the polymerases are minor proteins, and each peak represents a distinct enzyme, not a different state of one enzyme, as later shown by their subunit compositions and drug sensitivities.

Fractionation of rat liver nuclei located the enzymes: polymerase I was found in the nucleolar fraction, polymerases II and III in the nucleoplasm. The nucleolar location suggested that polymerase I makes rRNA, and in vitro transcription of cloned genes with purified enzymes and nuclear extracts later established the division of labor in the table.

| Polymerase | Location | Products | Share of nuclear transcription (growing cell) |
|---|---|---|---|
| Pol I | nucleolus | the large rRNA precursor (45S in mammals, 47S as first made), processed into 18S, 5.8S and 28S rRNA | up to about $60\%$ |
| Pol II | nucleoplasm | pre-mRNAs (historically "heterogeneous nuclear RNA"), most snRNAs (U1, U2, U4, U5), primary miRNA transcripts, long noncoding and enhancer RNAs | about $20$–$40\%$ |
| Pol III | nucleoplasm | tRNAs, 5S rRNA, U6 snRNA, 7SL RNA (of the signal recognition particle), 7SK RNA, the RNAs of RNase P and RNase MRP, other small RNAs | about $10\%$ |

Pol II makes the most diverse set of products, but in a rapidly growing cell most of the transcriptional effort goes into ribosomes, made by Pol I and Pol III (Example 12.6.2). Two further nuclear polymerases, Pol IV and Pol V, exist only in plants, where they make RNAs that direct **DNA methylation** of repeats ([7.2.15](/7.2.15)). Mitochondria use a single-subunit polymerase related to that of phage T7, a relic of the organelle's separate evolutionary history.

### 12.1.2. α-Amanitin

**Definition 12.1.1** The bicyclic octapeptide toxin of the death cap mushroom *Amanita phalloides* that inhibits eukaryotic RNA polymerases with very different potencies, Pol II most strongly, is called **α-amanitin**.

Lindell and colleagues (1970), Weinmann and Roeder (1974) and later work with purified enzymes measured these potencies (figure, panel B). Mammalian Pol II is inhibited by half at about $0.02\,\mu\mathrm{g\,mL^{-1}}$ of α-amanitin (about $20\,\mathrm{nM}$; $M_{\mathrm{r}} \approx 919$), mammalian Pol III at about $20\,\mu\mathrm{g\,mL^{-1}}$, a thousand times more, and Pol I retains full activity at $200\,\mu\mathrm{g\,mL^{-1}}$. The pattern differs between organisms (the Pol III enzymes of yeast and insects are resistant), but Pol II is always the sensitive enzyme. α-Amanitin does not block nucleotide binding or bond formation; it binds Rpb1 next to the active center (Section 12.3) and slows translocation from thousands of nucleotides per minute to a few.

If the activity remaining at inhibitor concentration $[\mathrm{I}]$ follows a simple binding isotherm with half-inhibitory concentration $\mathrm{IC}_{50}$,
$$
\frac{v}{v_0} = \frac{1}{1 + [\mathrm{I}]/\mathrm{IC}_{50}},
$$
then a concentration well between the $\mathrm{IC}_{50}$ values of two enzymes inhibits one almost completely and spares the other. This is how α-amanitin is used to assign a transcript to its polymerase.

**Example 12.1.2 (Assigning transcripts to polymerases)** Isolated nuclei are allowed to extend their engaged polymerases with labeled nucleotides (the **nuclear run-on assay**) with no toxin, with $1\,\mu\mathrm{g\,mL^{-1}}$ and with $200\,\mu\mathrm{g\,mL^{-1}}$ α-amanitin. At $1\,\mu\mathrm{g\,mL^{-1}}$ Pol II retains $1/(1 + 50) \approx 2\%$ of its activity and Pol III $1/(1 + 0.05) \approx 95\%$; at $200\,\mu\mathrm{g\,mL^{-1}}$ Pol III is reduced to about $9\%$ and Pol I is unaffected. A labeled RNA that disappears at the low concentration is made by Pol II, one that disappears only at the high concentration by Pol III, and one that resists both by Pol I. This is how the 5S rRNA and tRNA genes were assigned to Pol III, and the U6 snRNA gene, unexpectedly, to Pol III rather than to Pol II like the other U snRNAs (Section 12.7).

![Separating and distinguishing the three nuclear RNA polymerases. A: idealized elution profile of a DEAE-Sephadex column (after Roeder and Rutter, 1969): protein absorbance, polymerase activity and the salt gradient; the three activity peaks are polymerases I, II and III and do not coincide with the bulk protein. B: sensitivity to α-amanitin, modeled as single-site inhibition with the half-inhibitory concentrations of the mammalian enzymes (Pol II about 0.02 µg/mL, Pol III about 20 µg/mL, Pol I resistant); the shaded concentrations used in Example 12.1.2 inhibit Pol II alone, or Pol II and Pol III](./plots/polymerase-separation.py)

## 12.2. Subunit Structure

### 12.2.1. Which Polypeptides Are Subunits?

A protein that copurifies with polymerase activity through several columns might be a subunit or a contaminant that sticks to the enzyme. Two approaches settle this. The first is **epitope** tagging: the gene for one putative subunit (Rpb3 in yeast) is replaced by a version encoding an extra short **peptide** (an **epitope**) recognized by a **monoclonal antibody**; cells are grown with $[^{35}\mathrm{S}]$methionine, the enzyme is immunoprecipitated in one step under gentle conditions, and its polypeptides are separated by SDS-PAGE. This gave ten polypeptides (Young and colleagues, 1990); two more, Rpb4 and Rpb7, which dissociate easily, were found by multistep purification of the intact enzyme, giving twelve. The second approach is genetic: each gene is deleted or mutated, and a subunit whose loss abolishes activity or viability is a true component. The three yeast enzymes have $14$ (Pol I), $12$ (Pol II) and $17$ (Pol III) subunits, all with two large subunits of more than $100\,\mathrm{kDa}$.

### 12.2.2. Classes of Subunits

| Class | Pol II subunits | Bacterial counterpart | Remarks |
|---|---|---|---|
| Core | Rpb1, Rpb2, Rpb3, Rpb11 (and Rpb6) | β′, β, the α dimer (Rpb3–Rpb11 heterodimer), ω | Rpb1 and β′ bind DNA; Rpb2 and β lie at the **active site**; Rpb3 and Rpb11 are distant **homologs** of the two α subunits; Rpb6 of ω |
| Common | Rpb5, Rpb6, Rpb8, Rpb10, Rpb12 | (Rpb6 only) | shared by all three nuclear polymerases; Rpb5 is contacted by some activators, Rpb6 helps assembly, Rpb8 has an oligonucleotide-binding fold |
| Stalk | Rpb4–Rpb7 | none | dissociable heterodimer; Rpb4 deletion mutants grow poorly and initiate badly at promoters; Rpb7 is essential; binds the emerging RNA |
| Other | Rpb9 | none | start-site selection and fidelity; a zinc ribbon related to TFIIS |

Pol I and Pol III contain the same five common subunits, their own homologs of the core and stalk, and in addition subunits that resemble general transcription factors of Pol II: Pol I has a TFIIF-like and TFIIE-like heterodimer (A49–A34.5) and a TFIIS-like subunit (A12.2), and Pol III has TFIIF-like (C37–C53) and TFIIE-like (C82–C34–C31) subcomplexes and a TFIIS-like subunit (C11). Functions that Pol II recruits as separate, regulatable factors ([7.2.13](/7.2.13)) are thus built permanently into the other two enzymes, one reason why Pol I and Pol III need fewer factors and are regulated more simply.

### 12.2.3. The Carboxyl-Terminal Domain of Rpb1

When the largest subunit of mammalian Pol II was examined by SDS-PAGE, three forms appeared: IIo (about $240\,\mathrm{kDa}$), IIa (about $220\,\mathrm{kDa}$) and IIb (about $180\,\mathrm{kDa}$). IIa is the primary translation product; IIb lacks its C-terminal tail, which is removed by proteolysis during purification; and IIo is IIa with many phosphates on that tail, which slows its migration.

**Definition 12.2.1** The C-terminal tail of Rpb1, consisting of tandem repeats of the heptapeptide $\text{Tyr}_1\text{-Ser}_2\text{-Pro}_3\text{-Thr}_4\text{-Ser}_5\text{-Pro}_6\text{-Ser}_7$ (YSPTSPS), is called the **carboxyl-terminal domain** (CTD) of RNA polymerase II. It has $26$ repeats in budding yeast and $52$ in mammals, the more distal ones deviating from the consensus.

The polymerase with an unphosphorylated CTD (Pol IIA) is the form that joins the preinitiation complex at a promoter; the polymerase with a heavily phosphorylated CTD (Pol IIO) is the form engaged in elongation. Phosphorylation of Ser5 by TFIIH at initiation, and the shift to Ser2 phosphorylation during elongation, are described in [7.2.13](/7.2.13); the phosphorylated CTD then serves as a landing pad for the enzymes that cap, splice and polyadenylate the RNA ([7.2.17](/7.2.17)). Neither Pol I nor Pol III, nor the bacterial enzyme, has such a tail, and only Pol II transcripts are capped and polyadenylated.

**Remark 12.2.1** The CTD is large compared with the rest of the enzyme. Fully extended, $52 \times 7 = 364$ **residues** at about $0.35\,\mathrm{nm}$ per residue span about $130\,\mathrm{nm}$, almost ten times the $15\,\mathrm{nm}$ diameter of the polymerase body; it is intrinsically disordered and acts as a flexible tether. Each heptad has five phosphorylatable residues (Tyr1, Ser2, Thr4, Ser5, Ser7) and two prolines that can be isomerized, so the number of possible modification states is astronomically large; in practice, a few patterns dominate (Ser5 phosphorylation near the start of genes, Ser2 towards their ends), and the idea of a combinatorial "CTD code" read by processing factors refers to these patterns. The number of repeats matters: yeast cells with fewer than about $10$ repeats are not viable, and in mammals the essential number is about $25$–$30$.

## 12.3. The Structure of RNA Polymerase II

### 12.3.1. The Cleft and the Active Center

The crystal structure of yeast Pol II lacking Rpb4–Rpb7 (Pol II$\Delta$4/7) at $2.8$ Å (Cramer, Bushnell and Kornberg, 2001) shows a deep cleft, about $2.5\,\mathrm{nm}$ wide, that accepts the DNA duplex, formed between Rpb1 and Rpb2 and closed on one side by a mobile "clamp". At the floor of the cleft lies the catalytic center: a $\ce{Mg^2+}$ ion held by three invariant aspartates of Rpb1 (the motif NADFDGD), and a second, weakly bound $\ce{Mg^2+}$ that enters with each nucleoside triphosphate. This is the two-metal-ion mechanism shared with the bacterial enzyme ([7.2.10](/7.2.10)) and with **DNA polymerases** ([7.2.7](/7.2.7)): one metal activates the $3'$-OH of the RNA for attack on the α-phosphate of the incoming NTP, the other stabilizes the pentacovalent **transition state** and the leaving pyrophosphate. Kornberg's structures of Pol II and its complexes were recognized with the 2006 Nobel Prize in Chemistry.

The structure of an elongation complex (Gnatt et al., 2001, $3.3$ Å) placed the nucleic acids. Downstream DNA enters the cleft as a duplex and is gripped by "jaws"; the **template strand** turns by about $90°$ at a protein "wall" so that the base at the active site is accessible; a DNA–RNA hybrid of $8$–$9$ bp fills the space above the active site; and the RNA is separated from the template by protein loops (the "lid" and "rudder") and leaves through an exit channel under the clamp. Below the active site, a funnel-shaped opening, pore 1 (the secondary channel), connects the active center to the solvent: it is the probable route of NTP entry, and the channel into which the $3'$ end of the RNA is extruded when the enzyme slides backwards ([7.2.13](/7.2.13)).

Across the cleft, next to the active center, runs a long α-helix of Rpb1, the bridge helix. Flexing of this helix is thought to move the DNA–RNA hybrid by one **base pair** after each bond is formed (translocation). α-Amanitin binds in the funnel beneath the bridge helix and, by fixing the helix and the adjacent trigger loop, prevents translocation (Bushnell et al., 2002): the enzyme can add one nucleotide but then moves on only extremely slowly.

### 12.3.2. Nucleotide Selection and the Trigger Loop

Westover, Bushnell and Kornberg (2004) bound Pol II to a synthetic scaffold, a partly double-stranded template and an RNA terminated with a $3'$-deoxynucleotide that cannot be extended, and soaked the crystals with NTPs. The NTP complementary to the template base occupied the *A site* (the addition or insertion site), base-paired and positioned for catalysis. A noncomplementary NTP was found instead in an adjacent *E site* (entry site), inverted relative to its orientation in the A site. Selection is therefore at least two-step: NTPs sample the E site, rotate into the A site, and are retained only if they pair.

A structure with GTP opposite C in the A site (Wang et al., 2006) revealed the second step. A loop of Rpb1 (roughly residues $1070$–$1100$) folds, only when a matched NTP occupies the A site, into a pair of helices that close over the **substrate**, contact its base, sugar and triphosphate, and stabilize the catalytic geometry. This *trigger loop* links correct pairing to catalysis; mutations in it reduce both the rate and the fidelity of transcription. Together with the **proofreading** by transcript cleavage of [7.2.13](/7.2.13), these steps give Pol II an error rate of the order of $10^{-5}$ per nucleotide in vivo, worse than DNA replication by five orders of magnitude, but adequate for a product that is not inherited and is made in many copies. Where the energy of discrimination comes from, and why successive selection steps multiply their selectivities, is the subject of **kinetic proofreading** ([7.2.19](/7.2.19)).

### 12.3.3. Rpb4–Rpb7 and the Clamp

In the complete twelve-subunit structure, the Rpb4–Rpb7 stalk is wedged against the base of the clamp and restricts its movement. Since a closed cleft cannot admit a straight DNA duplex, this observation implied that promoter DNA cannot simply be lowered into the active site of the complete enzyme: the general transcription factors must position the DNA over the cleft and open it, so that the single-stranded template can be loaded and the clamp can close on it. **Cryo-electron microscopy** of preinitiation complexes has since shown exactly this sequence ([7.2.13](/7.2.13)).

## 12.4. Class II Core Promoters

### 12.4.1. Core and Proximal Promoter

A class II promoter, recognized by Pol II, is conventionally divided into two parts. The core promoter, which spans about $\pm 40$ bp around the start site, is sufficient for accurate initiation at a low (basal) level with purified general transcription factors; the proximal promoter, up to about $250$ bp upstream, contains **binding sites** for gene-specific factors that raise the rate of initiation (Section 12.5).

**Definition 12.4.1** The DNA region of about $80$ bp, extending roughly from $-40$ to $+40$ relative to the transcription start site ($+1$), that binds the general transcription factors and Pol II, directs accurate initiation at a basal level, and determines the position of the start site and the direction of transcription is called the **core promoter**.

The core promoter is modular: it can contain almost any combination of a small set of sequence elements, none of which is present in all promoters.

**Definition 12.4.2** An AT-rich core promoter element with consensus $\mathrm{TATAWAWR}$ (W = A or T, R = A or G) on the nontemplate strand, centered about $25$–$30$ bp upstream of the start site, that is bound by the TATA-binding protein, is called a **TATA box**.

**Definition 12.4.3** A core promoter element that encompasses the transcription start site, with consensus $\mathrm{YYA_{+1}NWYY}$ in mammals ($\mathrm{TCA_{+1}KTY}$ in *Drosophila*; Y = C or T, K = G or T), in which the $\mathrm{A}$ is the first transcribed nucleotide, is called an **initiator** (Inr).

**Definition 12.4.4** A core promoter element located precisely at $+28$ to $+32$ downstream of the initiator, with consensus $\mathrm{RGWYV}$ (V = A, C or G), that acts together with the initiator and is recognized by TFIID, is called a **downstream promoter element** (DPE).

| Element | Position | Consensus | Bound by |
|---|---|---|---|
| BRE$^{\mathrm{u}}$ (upstream TFIIB recognition element) | $-38$ to $-32$ | $\mathrm{SSRCGCC}$ (S = C or G) | TFIIB |
| TATA box | $-31$ to $-24$ | $\mathrm{TATAWAWR}$ | TBP |
| BRE$^{\mathrm{d}}$ (downstream BRE) | $-23$ to $-17$ | $\mathrm{RTDKKKK}$ (D = not C) | TFIIB |
| Inr | $-2$ to $+4$ | $\mathrm{YYANWYY}$ (mammals), $\mathrm{TCAKTY}$ (*Drosophila*) | TFIID (TAF1, TAF2) |
| MTE (motif ten element) | $+18$ to $+29$ | $\mathrm{CSARCSSAACGS}$ | TFIID |
| DPE | $+28$ to $+32$ | $\mathrm{RGWYV}$ | TFIID (TAF6, TAF9) |
| DCE (downstream core element) | three parts near $+6$, $+16$, $+30$ | $\mathrm{CTTC}$, $\mathrm{CTGT}$, $\mathrm{AGC}$ | TFIID (TAF1) |
| TCT motif | $-2$ to $+6$ | $\mathrm{YYCTTTYY}$ | TRF2 (ribosomal protein genes) |

![Promoters of the three nuclear RNA polymerases drawn to scale. A: the class II core promoter elements and their consensus sequences on the nontemplate strand, with the start site at +1 (no promoter has all of them). B: a class I (rRNA) promoter: core element and upstream control element, whose spacing matters. C: the three types of class III promoter: internal box A, intermediate element and box C of the 5S rRNA gene; internal box A and box B of tRNA genes; and the upstream DSE, PSE and TATA box of the U6 snRNA gene](./plots/promoter-maps.py)

The core promoter elements are of three kinds by function. The TATA box and the BREs, upstream, are bound by TBP and TFIIB and fix the position of the polymerase about $30$ bp downstream. The Inr, at the start site, is the actual site of initiation. The MTE and DPE, downstream, act together with the Inr and require exact spacing from it (moving the DPE by a single base pair reduces its activity severalfold), which shows that they are read by one complex, TFIID, spanning the start site ([7.2.13](/7.2.13)).

**Example 12.4.1 (The consensus sequence is a statistical summary)** The TATA box is the core element most similar to the bacterial $-10$ box, and like it, it is a **consensus sequence**, the most common base at each position in an alignment of many promoters, not a sequence that any given promoter must contain. The $T$ and $A$ at its first four positions are highly conserved; the fifth and seventh positions are frequently $T$ instead of $A$, hence the consensus $\mathrm{TATAWAWR}$. The consensus fixes five positions and allows two bases at three others, so in a random sequence with equal base frequencies it matches, on one strand, with probability $(1/4)^5 (1/2)^3 = 1.2 \times 10^{-4}$ per position, that is, about once per $8\,\mathrm{kb}$: TATA-like sequences occur by chance everywhere, and what makes a functional TATA box is its position relative to an Inr and to activator sites.

### 12.4.2. Focused and Dispersed Promoters

Genome-wide mapping of transcript $5'$ ends (by methods such as CAGE that sequence capped RNA ends) has shown that canonical TATA boxes are present in only about $10$–$20\%$ of human promoters. Promoters fall into two broad classes:

| | Focused promoters | Dispersed promoters |
|---|---|---|
| Start sites | one site or a few within a few base pairs | many weak sites over $50$–$100$ bp |
| Elements | TATA box, Inr, DPE, MTE | few defined elements; often a CpG island ([7.2.15](/7.2.15)) |
| Genes | highly regulated, often tissue-specific (keratins in skin, globins in erythroid cells) and developmentally regulated genes | housekeeping genes, constitutively expressed in nearly all cells |
| Proportion | a minority in vertebrates | about two-thirds of vertebrate promoters |

Developmentally regulated genes are not all of the TATA type: many *Drosophila* homeotic genes and genes of the mammalian immune system have TATA-less promoters with an Inr and a DPE. Most mammalian promoters also initiate transcription in both directions (divergent transcription), producing an unstable upstream antisense RNA; only the sense transcript is elongated efficiently and processed.

### 12.4.3. Dissecting a Promoter: What Does the TATA Box Do?

Two classic mutagenesis experiments, on two different promoters, gave two different answers, and both turned out to be right.

**Example 12.4.2 (Deletions of the SV40 early promoter)** Benoist and Chambon (1981) made deletions upstream of the start site of the SV40 early genes and mapped the start sites of the resulting transcripts by **S1 mapping**. Deletions that removed the TATA box did not reduce transcription in vivo, but the transcripts now began at many sites scattered over tens of base pairs. Deletions between the TATA box and the start site shifted the start site downstream by the same amount, keeping the distance from the TATA box to the start site constant. The TATA box therefore positions initiation, about $25$–$30$ bp downstream of its last base.

**Example 12.4.3 (Linker scanning of the thymidine kinase promoter)** McKnight and Kingsbury (1982) systematically replaced successive 10 bp blocks of the herpes simplex virus thymidine kinase (tk) promoter with a synthetic linker, so that each mutant changed the sequence at one place without changing the spacing of the rest (deletion mutants change both). Transcription fell to a few percent when the linker replaced the TATA box (around $-30$), and dropped substantially when it replaced either of two GC boxes (around $-50$ and $-100$) or a CCAAT box (around $-80$); substitutions elsewhere had little effect. In this promoter the TATA box is needed for efficient transcription. The approach is the DNA analog of the alanine scanning of proteins: a uniform substitution reveals which parts of a sequence are essential.

![Two ways of dissecting a class II promoter (idealized data). A: linker scanning of the HSV thymidine kinase promoter: transcription relative to wild type when successive 10 bp blocks are replaced, with dips at the TATA box, the two GC boxes and the CCAAT box (after McKnight and Kingsbury, 1982). B: start-site distributions mapped by S1 protection for the SV40 early promoter with and without its TATA box: removing the TATA box scatters initiation over tens of base pairs without abolishing it (after Benoist and Chambon, 1981)](./plots/promoter-dissection.py)

The two results are reconciled by what binds the TATA box ([7.2.13](/7.2.13)). The TATA box is the site where assembly of the preinitiation complex usually begins: TBP binds it and fixes the position of the polymerase. Where strong upstream elements can recruit TBP indirectly (the SV40 GC boxes and enhancer), the TATA box is dispensable for the amount of transcription but still needed for its precision; where they cannot, it is needed for both. TATA-less promoters still require TBP, which is then held in place by other proteins bound to the Inr, the DPE or upstream elements.

## 12.5. Proximal Promoter Elements

Upstream of the core promoter, within about $250$ bp of the start site, most class II promoters contain one or several binding sites for widely expressed, sequence-specific transcription factors. Two are very common:

- *GC boxes* ($\mathrm{GGGGCGGGG}$, core $\mathrm{GGGCGG}$), bound by Sp1 through three zinc fingers ([7.2.14](/7.2.14)). Sp1 was the first sequence-specific eukaryotic transcription factor purified, by affinity chromatography on a column carrying its binding site (Kadonaga and Tjian, 1986). The SV40 early promoter has six GC boxes in its $21$ bp repeats.
- *CCAAT boxes*, typically at $-60$ to $-100$ in about a third of promoters, bound mainly by the heterotrimeric factor NF-Y (CBF), whose subunits have **histone folds**. CTF/NF-I, originally described as the CCAAT-binding factor, binds a related but distinct sequence.

Proximal elements differ from core elements in being bound by gene-specific rather than general factors, and they differ from enhancers in their position dependence: they usually work in either orientation, but only within a limited distance from the core promoter. The line between proximal elements and enhancers is not sharp; both are binding sites for activators, and their mechanisms of action are the same ([7.2.14](/7.2.14)).

## 12.6. Class I Promoters

### 12.6.1. Architecture

Human cells have about $400$ copies of the rRNA genes (rDNA), in tandem arrays on the short arms of the five acrocentric chromosomes (13, 14, 15, 21 and 22), where they form the nucleolus organizer regions. Each $43\,\mathrm{kb}$ repeat contains a $13\,\mathrm{kb}$ transcription unit for the precursor of 18S, 5.8S and 28S rRNA and a $30\,\mathrm{kb}$ intergenic spacer. Class I promoters are poorly conserved in sequence between species (a human rRNA promoter is not used by mouse extracts), but their architecture is conserved: a core element surrounding the start site and an upstream control element about $100$ bp further upstream.

**Example 12.6.1 (Spacing between the two elements matters)** Linker-scanning mutagenesis of the human rRNA promoter by Tjian and colleagues identified the core element between $-45$ and $+20$ and the upstream control element between $-156$ and $-107$; mutations in the core element abolished transcription, those in the upstream element reduced it. Changing the distance between the elements had graded effects: deleting $16$ bp reduced transcription to $40\%$ and deleting $44$ bp to $10\%$; inserting $28$ bp had no effect, but inserting $49$ bp reduced it to $30\%$. The two elements are therefore read by factors that interact with each other across a fixed stretch of DNA, as the factors of [7.2.13](/7.2.13) confirm: UBF binds both elements and loops the DNA between them, and SL1 bridges UBF and Pol I.

### 12.6.2. How Fast Must rRNA Genes Be Transcribed?

**Example 12.6.2 (Ribosome production)** A HeLa cell contains about $10^7$ ribosomes and divides about once a day, so it must make about $10^7/1440\,\mathrm{min} \approx 7000$ ribosomes per minute. Electron micrographs of spread nucleolar chromatin ("Miller spreads") show active rRNA genes densely packed with polymerases, about $100$ to $125$ per $13\,\mathrm{kb}$ gene, one every $d \approx 100$–$130$ bp, with nascent transcripts growing in length along the gene ("Christmas trees"). If polymerases elongate at $v \approx 60$–$90\,\mathrm{nt\,s^{-1}}$ and keep this spacing, a new polymerase must initiate on each gene every
$$
\frac{d}{v} \approx \frac{120\,\mathrm{nt}}{80\,\mathrm{nt\,s^{-1}}} \approx 1.5\,\mathrm{s}.
$$
Only about half of the rDNA copies are active (the rest are silenced as **heterochromatin**), so $200$ active genes each initiating every $1.5\,\mathrm{s}$ produce about $130$ precursors per second, or $8000$ per minute, matching the requirement. Two features of rRNA synthesis follow from this estimate: rRNA genes must be present in many copies, and their promoters must reinitiate at nearly the maximum rate allowed by the footprint of a polymerase. This is why ribosome synthesis is regulated mainly by controlling the initiation rate of Pol I (through its initiation factor TIF-IA, which responds to nutrients and growth signals) and the number of active rDNA copies.

## 12.7. Class III Promoters

Pol III transcribes short genes, most of them shorter than $300$ bp, and terminates without a **hairpin** at a run of four or more T residues on the **nontemplate strand**. Its promoters are of three types.

**Example 12.7.1 (An internal promoter)** Brown and colleagues (Sakonju, Bogenhagen and Brown, 1980) made deletions into the *Xenopus laevis* 5S rRNA gene from either end and transcribed the mutants in oocyte nuclear extracts. The entire $5'$-flanking region could be removed with little effect on transcription, which then started at a vector sequence the same distance upstream of the internal region; but deletions that entered the gene beyond about $+50$ from the $5'$ side, or beyond about $+83$ from the $3'$ side, abolished transcription. The promoter therefore lies inside the gene, between $+50$ and $+83$. Systematic point mutagenesis (Roeder and colleagues) resolved it into three sensitive regions, box A, an intermediate element and box C.

| Type | Genes | Promoter elements | Factors ([7.2.13](/7.2.13)) |
|---|---|---|---|
| 1 | 5S rRNA | internal: box A ($+50$ to $+64$), intermediate element ($+67$ to $+72$), box C ($+80$ to $+90$) | TFIIIA, TFIIIC, TFIIIB |
| 2 | tRNAs, 7SL RNA (weak), Alu and other **SINEs** | internal: box A (near $+10$ to $+20$) and box B ($30$–$60$ bp further downstream), which encode parts of the D and T arms of tRNA | TFIIIC, TFIIIB |
| 3 | U6 snRNA, 7SK RNA, RNase P (H1) and MRP RNAs | upstream only: distal sequence element (DSE, about $-240$), proximal sequence element (PSE, about $-55$) and TATA box (about $-25$) | SNAPc, TFIIIB (with Brf2), Oct-1 at the DSE |

Internal promoters have a curious consequence: the promoter is transcribed as part of the RNA, so tRNA and 5S rRNA sequences are constrained both by the function of the RNA and by the binding of transcription factors to the gene. Some genes combine both arrangements. Ullu and Weiner (1985) found that the 7SL RNA gene has a weak internal promoter but requires its $5'$-flanking region for high-level transcription. This explains why the hundreds of 7SL **pseudogenes** and the roughly one million copies of the related Alu **SINEs** in the human genome are poorly transcribed: they carry the internal promoter but lack the upstream element.

The type 3 promoters of the U6 and U2 snRNA genes illustrate how the choice of polymerase is encoded. Both have a DSE and a PSE, but U6 has a TATA box and is transcribed by Pol III, whereas U2 has none and is transcribed by Pol II. Inserting a TATA box into the U2 promoter converts it into a Pol III promoter, and destroying the TATA box of the U6 promoter converts it into a Pol II promoter (Lobo and Hernandez, 1989; Mattaj and colleagues, 1988). Type 3 promoters need no sequence inside the transcribed region and start at a defined nucleotide (a G for U6), and transcription ends at a run of T: this is why the U6 and H1 promoters are used to express short hairpin RNAs and the guide RNAs of CRISPR systems ([7.2.24](/7.2.24)).

## 12.8. Enhancers and Silencers

**Definition 12.8.1** A DNA element that increases transcription from a promoter in *cis* (on the same DNA molecule) largely independently of its orientation and of its position, upstream, downstream or within the gene, and often at a distance of many kilobases, is called an **enhancer**. A DNA element with the same properties that decreases transcription is called a **silencer**.

Enhancers were discovered in viruses. A $72$ bp repeated sequence of SV40, placed on a **plasmid** in either orientation, upstream or downstream of a rabbit β-globin gene, and more than $3\,\mathrm{kb}$ away from it, increased transcription of the gene about $200$-fold in transfected cells (Banerji, Rusconi and Schaffner, 1981). The first cellular enhancer was found in an **intron** of an **immunoglobulin** heavy-chain gene.

**Example 12.8.1 (An immunoglobulin enhancer)** Gillies, Tonegawa and colleagues (1983) transfected a rearranged mouse immunoglobulin $\gamma 2\mathrm{b}$ heavy-chain gene into myeloma cells and measured its mRNA by **Northern blot**. Deleting an $XbaI$ fragment from the intron between the joining (J) segment and the constant region reduced transcription drastically. When the fragment was reinserted in the reverse orientation, or moved upstream of the promoter, transcription was restored: the region contained an element that stimulated transcription from a nearby promoter independently of its position and orientation, an enhancer. The enhancer worked only in B-lymphocyte-derived cells, the first indication that enhancers confer cell-type specificity.

Enhancers act through the proteins bound to them, activators, which contact coactivators and the general transcription factors at the promoter and stimulate assembly of the preinitiation complex; how they do so over large distances is the subject of [7.2.14](/7.2.14). Three properties of enhancers deserve emphasis:

1. *Cell-type specificity.* An enhancer is active only where its activators are present, and enhancers, more than promoters, determine where and when a gene is expressed. Many genes have several enhancers, each driving expression in a different tissue or developmental stage.
2. *Distance.* Enhancers can act over very long distances, usually within the same **topologically associating domain** ([7.2.4](/7.2.4)). The limb enhancer of the *Sonic hedgehog* gene (ZRS) lies about $1\,\mathrm{Mb}$ away, in an intron of another gene; point mutations in it cause extra digits.
3. *Number.* Biochemical marks of active enhancers (the histone modification H3K27ac and H3K4me1, binding of the coactivator p300, accessibility, short bidirectional "enhancer RNAs") identify about a million candidate regulatory elements in the human genome, far more than there are genes ([7.2.15](/7.2.15)).

Silencers work by recruiting repressors and corepressors that modify chromatin or block activators. In non-neuronal mammalian cells, for example, the repressor REST binds a $21$ bp silencer (RE1) in many neuronal genes and recruits histone-deacetylating corepressors that keep them off ([7.2.15](/7.2.15)); in yeast, silencers flank the silent mating-type loci. Some elements act as enhancers or silencers depending on what is bound to them: a thyroid-hormone response element bound by the unliganded receptor represses, and the same element with the liganded receptor activates ([7.2.14](/7.2.14)).

## Summary

| Topic | Key facts |
|---|---|
| Three polymerases | separated on DEAE-Sephadex (Example 12.1.1); Pol I nucleolar, rRNA precursor; Pol II pre-mRNA, most snRNAs, miRNA and lncRNA; Pol III tRNA, 5S rRNA, U6, 7SL, 7SK |
| α-Amanitin (Definition 12.1.1) | $\mathrm{IC}_{50}$: Pol II $0.02\,\mu\mathrm{g\,mL^{-1}}$, Pol III $20\,\mu\mathrm{g\,mL^{-1}}$, Pol I resistant; $v/v_0 = 1/(1 + [\mathrm{I}]/\mathrm{IC}_{50})$ assigns transcripts to polymerases (Example 12.1.2); blocks translocation |
| Subunits | 14, 12, 17 subunits; Rpb1, Rpb2, Rpb3–Rpb11, Rpb6 homologous to β′, β, α₂, ω; five common subunits; Rpb4–Rpb7 stalk; Pol I and Pol III contain TFIIF-, TFIIE- and TFIIS-like subunits |
| CTD (Definition 12.2.1) | YSPTSPS repeats: $26$ in yeast, $52$ in mammals; IIa (unphosphorylated, joins promoters), IIo (phosphorylated, elongates), IIb (CTD removed) |
| Structure | cleft and clamp; two $\ce{Mg^2+}$ (NADFDGD); $8$–$9$ bp hybrid; bridge helix and α-amanitin; E site and A site; trigger loop closes on a matched NTP; error rate about $10^{-5}$ |
| Core promoter (Definition 12.4.1) | BRE$^{\mathrm{u}}$, TATA box (Definition 12.4.2, $-31$ to $-24$), BRE$^{\mathrm{d}}$, Inr (Definition 12.4.3), MTE, DPE (Definition 12.4.4, $+28$ to $+32$); focused versus dispersed promoters; TATA in only $10$–$20\%$ |
| TATA box function | positions the start site $25$–$30$ bp downstream (SV40 deletions, Example 12.4.2) and is needed for efficiency in some promoters (tk linker scanning, Example 12.4.3) |
| Proximal elements | GC box (Sp1), CCAAT box (NF-Y); orientation-independent but position-dependent |
| Class I | core element ($-45$ to $+20$) and upstream control element ($-156$ to $-107$), spacing-dependent (Example 12.6.1); initiation every $1.5\,\mathrm{s}$ per active gene (Example 12.6.2) |
| Class III | type 1 (box A, IE, box C), type 2 (box A, box B), type 3 (DSE, PSE, TATA); TATA box makes U2 a Pol III promoter; poly(T) terminator |
| Enhancers and silencers (Definition 12.8.1) | position- and orientation-independent; SV40 72 bp repeat, immunoglobulin intron enhancer (Example 12.8.1); cell-type specific; act within TADs, up to $1\,\mathrm{Mb}$ |

## Questions

1. A labeled RNA made in isolated nuclei is unaffected by $1\,\mu\mathrm{g\,mL^{-1}}$ α-amanitin but reduced by $90\%$ at $200\,\mu\mathrm{g\,mL^{-1}}$. Which polymerase makes it? Would the same experiment work in yeast nuclei?

   **Answer** Pol II would be inhibited by about $98\%$ at $1\,\mu\mathrm{g\,mL^{-1}}$, so the RNA is not a Pol II product; Pol III would retain about $1/(1 + 200/20) \approx 9\%$ of its activity at $200\,\mu\mathrm{g\,mL^{-1}}$, consistent with the $90\%$ reduction, and Pol I would be unaffected. The RNA is therefore made by Pol III. In yeast the experiment would not distinguish Pol III from Pol I, because yeast Pol III is resistant to α-amanitin; one would use temperature-sensitive mutants of polymerase-specific subunits instead.
2. Why do deletion mutants and linker-scanning mutants of a promoter give different information? Design a linker scan for a $120$ bp promoter.

   **Answer** A deletion removes a sequence and also brings the remaining sequences closer together, so a loss of activity may be due to the missing element or to the changed spacing (as for class I promoters, Example 12.6.1); deletions also cannot test an internal element without removing everything on one side. A linker scan replaces one block at a time with an unrelated sequence of the same length, preserving all distances. For a $120$ bp promoter one would make twelve mutants, each replacing a successive $10$ bp block (for example $-120$ to $-111$, $-110$ to $-101$, …, $-10$ to $-1$), measure transcription of each relative to wild type by primer extension or S1 mapping with an internal control, and look for the blocks whose replacement reduces activity.
3. A promoter has a DPE but no TATA box. Predict the effect of inserting $1$ bp between the Inr and the DPE, and of inserting $5$ bp $50$ bp upstream of the Inr. Explain.

   **Answer** The DPE works only at a precise distance from the Inr because both are contacted by one complex, TFIID (TAF1, TAF2 at the Inr, TAF6 and TAF9 at the DPE); a $1$ bp insertion displaces the DPE by a third of a helical turn and is expected to reduce transcription severalfold. An insertion $50$ bp upstream lies outside the core promoter, in the proximal region, where elements tolerate changes of spacing of a few base pairs; little effect is expected unless it disrupts a binding site.
4. Inserting a TATA box into the U2 snRNA promoter makes it a Pol III promoter. What does this suggest about the protein that binds the TATA box and the factors that bind the PSE?

   **Answer** The PSE is bound by the same factor (SNAPc) in both genes and can recruit either polymerase; the TATA box decides between them. Since TBP is used by both Pol II and Pol III, the decision cannot depend on TBP alone: it depends on the TBP-containing complex assembled at the TATA box, TFIIIB (TBP, Brf2, Bdp1) for Pol III versus TFIID or TBP with TFIIB for Pol II, which in turn is determined by the combination of the PSE-bound SNAPc with a TATA box. This is an example of TBP's specificity being governed by its associated proteins ([7.2.13](/7.2.13)).
5. Using Example 12.6.2, how many polymerases are on one active rRNA gene at a time, and how long does one polymerase take to transcribe it? What limits the rate of rRNA synthesis per gene?

   **Answer** A $13\,\mathrm{kb}$ gene with one polymerase per $120$ bp carries about $110$ polymerases. At $80\,\mathrm{nt\,s^{-1}}$ a polymerase needs $13\,000/80 \approx 160\,\mathrm{s}$, almost three minutes, to traverse it. The output per gene is the initiation frequency, $v/d$; since $d$ cannot be smaller than the footprint of a polymerase on DNA (about $35$–$40$ bp) and the observed spacing is only about three times that, rRNA genes operate close to their maximum capacity, and cells increase rRNA output mainly by activating more gene copies and keeping initiation at its maximum.
6. An enhancer placed $3\,\mathrm{kb}$ downstream of a gene in either orientation stimulates its transcription 50-fold in liver cells but not in fibroblasts. A $1\,\mathrm{kb}$ fragment inserted between the enhancer and the promoter abolishes the stimulation. Suggest what the fragment contains.

   **Answer** The enhancer behaves normally (position and orientation independence, cell-type specificity through liver activators). A fragment that blocks enhancement only when placed between enhancer and promoter, without itself repressing the promoter, is an enhancer-blocking insulator, typically a binding site for CTCF that creates a loop boundary ([7.2.14](/7.2.14)). A silencer would be expected to repress regardless of its position between or outside the enhancer–promoter pair; testing the fragment when placed upstream of both elements distinguishes the two.
