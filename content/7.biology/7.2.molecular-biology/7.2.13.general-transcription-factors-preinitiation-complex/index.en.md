---
title: General Transcription Factors and the Preinitiation Complex
description: How the class II preinitiation complex was reconstituted (gel mobility shift and footprinting of the DA, DAB, DABPolF and DABPolFEH complexes; stepwise assembly and holoenzyme pathways; the kinetics of multistep assembly); TBP (minor-groove binding, the saddle and the 80° bend, universality); TAFs (unified nomenclature, recognition of the initiator and DPE, coactivator and enzymatic functions, exceptions such as TRF1 and NC2); TFIIB as a bridge and start-site selector; TFIIH as translocase and CTD kinase, promoter opening and escape; promoter-proximal pausing; the Ser5-to-Ser2 switch of the CTD; TFIIS, backtracking and proofreading; SL1 and UBF for Pol I; TFIIIA, TFIIIB and TFIIIC for Pol III; the role of TBP.
---

Purified eukaryotic RNA polymerases transcribe DNA, but they start at random: none of them recognizes a promoter by itself. Initiation at the sites defined in [7.2.12](/7.2.12) requires a set of proteins, the general transcription factors, which recognize the core promoter, recruit the polymerase, open the DNA and release the enzyme into elongation. This chapter reconstructs the class II preinitiation complex in the order in which its components were discovered and placed, describes what each factor does, follows the polymerase through promoter escape and the first regulated steps of elongation, and then compares the much simpler factor sets of Pol I and Pol III. Three unifying principles emerge at the end, the most important being that one protein, the TATA-binding protein, organizes initiation by all three polymerases. Gene-specific activators, which act by contacting these factors, are the subject of [7.2.14](/7.2.14).

The experimental methods are those of [7.2.6](/7.2.6): the **electrophoretic mobility shift assay**, which detects protein–DNA complexes by their slower migration in a native gel, and **DNase I footprinting**, which shows the stretch of DNA that a bound protein protects. For comparison with the bacterial system, in which a single **σ factor** does most of what these factors do, see [7.2.10](/7.2.10).

## 13.1. Assembly of the Preinitiation Complex

### 13.1.1. Polymerase II Needs Factors

Weil, Luse, Segall and Roeder (1979) found that purified Pol II transcribed a cloned adenovirus gene only nonspecifically, but initiated accurately at its promoter when a crude extract of human cells was added. The extract was fractionated by chromatography on phosphocellulose and other columns, and the activities required in addition to the polymerase were named after the column fractions in which they were found: TFIIA, TFIIB, TFIID, TFIIE, TFIIF and TFIIH ("TF" for transcription factor, "II" for polymerase II). A soluble nuclear extract that supports accurate transcription (Dignam, Lebovitz and Roeder, 1983) became the standard starting material; it is one of the most cited papers in biology.

**Definition 13.1.1** The proteins that, together with an RNA polymerase, are necessary and sufficient for accurate initiation of transcription at a core promoter, and that act at essentially all promoters of that polymerase, are called **general transcription factors**. The complex of a polymerase with its general transcription factors assembled on a promoter, poised to initiate when nucleotides are supplied, is called the **preinitiation complex** (PIC).

General transcription factors are distinguished from gene-specific factors (activators and repressors), which bind particular enhancers and promoter elements and change the rate at which preinitiation complexes form or fire ([7.2.14](/7.2.14)).

| Factor | Subunits (human) | Main functions |
|---|---|---|
| TFIID | TBP and 13–14 TAFs, about $1.2\,\mathrm{MDa}$ | recognizes the TATA box (TBP) and the Inr, MTE and DPE (TAFs); target of activators; histone acetyltransferase, kinase and acetyl-lysine reader (TAF1) |
| TFIIA | 2 (αβ, γ) | stabilizes TBP on DNA; counteracts the inhibitors NC2 and Mot1 |
| TFIIB | 1 (about $33\,\mathrm{kDa}$) | binds TBP and the BREs; bridges to Pol II; selects the start site |
| TFIIF | 2 (RAP74, RAP30) | binds Pol II and escorts it to the promoter; stabilizes the open complex; stimulates elongation |
| TFIIE | 2 (α, β) | recruits TFIIH and stimulates its activities; binds single-stranded DNA |
| TFIIH | 10: a core of 7 (XPB, XPD, p62, p52, p44, p34, p8) and a kinase module of 3 (CDK7, cyclin H, MAT1) | opens the promoter (XPB); phosphorylates Ser5 and Ser7 of the CTD (CDK7); in DNA repair, unwinds damaged DNA (XPD) |

### 13.1.2. The Order of Assembly

**Example 13.1.1 (Four complexes on a gel)** Buratowski, Hahn, Guarente and Sharp (1989) incubated a labeled DNA fragment carrying the adenovirus major late promoter with combinations of purified factors and Pol II and analyzed the complexes by gel mobility shift. TFIID bound first, and its complex was stabilized by TFIIA (complex DA). TFIIB bound only to DA (DAB). Pol II bound only to DAB, and only when it was accompanied by TFIIF (DABPolF). Later work with TFIIE and TFIIH (Flores and Reinberg, 1991, 1992) added them in that order, giving DABPolFEH. Each factor bound only if the previous ones were present, which defined an assembly order: D (with A), B, Pol II with F, E, H.

**Example 13.1.2 (Where each factor sits)** DNase I footprinting of the same complexes showed that TFIID, A and B protect the TATA box region, from about $-42$ to $-17$; adding Pol II and TFIIF extends the protection by about $34$ bases on the nontemplate strand, from $-17$ to about $+17$. The polymerase thus sits downstream of TBP–TFIIB, over the start site, and TFIIB, which binds TBP and Pol II, is the bridge between them.

![Architecture of the class II preinitiation complex (schematic, not to scale). TBP binds the minor groove of the TATA box and bends the DNA by about 80°; TFIIA and TFIIB clamp TBP from either side, TFIIB contacting the BREs and reaching with its N-terminal domains into Pol II; TFIIF binds the polymerase; TFIIE and TFIIH bind downstream, where the XPB translocase of TFIIH grips the DNA about 20–30 bp downstream of the start site. The DNA is melted from about −9 to +2 in the open complex; the bars below give the footprints of Example 13.1.2](./plots/pic-architecture.py)

The stepwise order is a property of the reaction in vitro. In cells, Pol II is also found in a large complex, often called the Pol II holoenzyme, containing the polymerase, TFIIB, TFIIF, TFIIH and the Mediator coactivator complex (Koleske and Young, 1994), which suggested an alternative pathway in which TFIID (or TBP) binds the promoter and the rest arrives in one step. The two pathways differ in the number of steps that must be completed before initiation, and this has a measurable consequence.

**Formula 13.1.1 (Waiting time for multistep assembly)** If a complex forms through $m$ consecutive irreversible steps, each occurring at rate $k$ (in $\mathrm{s^{-1}}$, a pseudo-first-order rate constant at fixed factor concentrations), the time $T$ to completion is the sum of $m$ independent exponential waiting times; it follows the **Erlang distribution**
$$
\mathbb{P}(T \le t) = 1 - \mathrm{e}^{-kt} \sum_{j=0}^{m-1} \frac{(kt)^j}{j!}, \qquad \mathbb{E}[T] = \frac{m}{k}, \qquad \frac{\sqrt{\operatorname{Var}(T)}}{\mathbb{E}[T]} = \frac{1}{\sqrt{m}}. \tag{13.1}
$$

For $m = 1$ the fraction of completed complexes rises exponentially from time zero; for $m \ge 2$ it rises after a lag and more sharply (figure). A five-step stepwise pathway (D, B, Pol II–F, E, H) and a two-step holoenzyme pathway with the same mean time can therefore be distinguished by the shape of the time course of PIC formation, or of the waiting times between transcription events measured on single molecules, without knowing any individual rate constant. Real steps are reversible and may be partly ordered, so the actual distributions lie between these extremes; single-molecule experiments in nuclear extracts indicate that both routes are used, TFIID and TFIIB binding first and Pol II often arriving together with TFIIF and Mediator.

![Kinetics of preinitiation complex assembly computed with Eq. (13.1). A: fraction of promoters with a complete complex against time for one, two and five sequential steps with the same mean assembly time (10 s): multistep assembly produces a lag and a steeper rise. B: the corresponding distributions of completion times, the gamma (Erlang) densities; their relative width falls as 1/√m](./plots/pic-kinetics.py)

## 13.2. The TATA-Binding Protein

### 13.2.1. Minor-Groove Binding and the Saddle

**Definition 13.2.1** The protein that binds the TATA box through the DNA minor groove and serves as the core of the TATA-recognizing complexes of all three nuclear RNA polymerases is called the **TATA-binding protein** (TBP).

Human TBP has $339$ residues ($38\,\mathrm{kDa}$). Its C-terminal $180$ residues are more than $80\%$ identical between yeast and humans and are sufficient to bind the TATA box; the N-terminal region is variable. That TBP reads the minor groove was shown by base substitution: replacing the A·T pairs of a TATA box by I·C pairs (inosine lacks the 2-amino group of guanine) leaves the pattern of hydrogen-bond donors and acceptors in the minor groove unchanged while changing the major groove, and TBP still binds; most other DNA-binding proteins read the major groove ([7.2.14](/7.2.14)).

Crystal structures of TBP bound to a TATA box (Kim, Geiger and Sigler, 1993; Kim, Nikolov and Burley, 1993) explained this unusual choice. The conserved domain forms a saddle of two similar halves; its concave underside is a ten-stranded antiparallel **β sheet** that sits astride the DNA. Two pairs of phenylalanine side chains intercalate between base pairs at the two ends of the TATA box and kink the DNA; the minor groove is widened and flattened against the sheet, the DNA is partly unwound (by about a third of a turn) and bent by about $80°$ away from the protein. A·T-rich sequences are those that tolerate this distortion most cheaply, which is why the TATA box is AT-rich. The bend brings upstream and downstream DNA closer together, creating a platform on which TFIIA and TFIIB bind on either side.

TBP binds the nearly symmetric TATA box in either orientation. Direction of transcription is imposed by the proteins that bind next: TFIIB, contacting the upstream BRE and asymmetric surfaces of TBP, and TFIIA. This is one reason why promoters with a BRE or a well-matched TATA box initiate predominantly in one direction.

### 13.2.2. TBP Is Used by All Three Polymerases

**Example 13.2.1 (A temperature-sensitive TBP)** Cormack and Struhl (1992) and Schultz, Reeder and Hahn (1992) isolated yeast strains with temperature-sensitive mutations in the gene for TBP. Extracts from mutant cells that had been shifted to the restrictive temperature were defective in transcription from a class II promoter, but also from an rRNA (class I) promoter and from tRNA and 5S rRNA (class III) genes, assayed by S1 mapping; extracts of wild-type cells treated the same way were not. To show that the defects are caused by the mutant TBP and not by some secondary effect of heat treatment, one adds back purified wild-type TBP: it restored transcription by all three polymerases. TBP is a universal transcription factor; a homolog with the same saddle structure works with the archaeal RNA polymerase, which is itself related to Pol II.

## 13.3. TBP-Associated Factors

### 13.3.1. TAFs and Their Names

**Definition 13.3.1** The proteins that associate tightly with TBP to form TFIID (and, with other sets, SL1 and TFIIIB) are called **TBP-associated factors** (TAFs).

TFIID contains $13$–$14$ TAFs, most of them conserved from yeast to humans. They were first named after their apparent molecular masses in kilodaltons, with a subscript for the polymerase (TAF$_{\mathrm{II}}$250, TAF$_{\mathrm{II}}$150), so that homologous proteins had different names in each species. A unified nomenclature (Tora, 2002) numbers them from TAF1 to TAF15 in order of decreasing size of the human protein; the older names, used in much of the classic literature and in the course slides, translate as follows.

| Unified name | Human | *Drosophila* | Yeast | Notes |
|---|---|---|---|---|
| TAF1 | TAF$_{\mathrm{II}}$250 | TAF$_{\mathrm{II}}$230 | Taf145 | largest subunit; scaffold; HAT, kinase; double bromodomain (in humans) |
| TAF2 | TAF$_{\mathrm{II}}$150 | TAF$_{\mathrm{II}}$150 | Taf150 | contacts the Inr with TAF1 |
| TAF4 | TAF$_{\mathrm{II}}$130/135 | TAF$_{\mathrm{II}}$110 | Taf48 | glutamine-rich region; target of Sp1 |
| TAF5 | TAF$_{\mathrm{II}}$100 | TAF$_{\mathrm{II}}$80 | Taf90 | WD40 repeats; also in SAGA |
| TAF6 | TAF$_{\mathrm{II}}$80 | TAF$_{\mathrm{II}}$60 | Taf60 | histone fold (H4-like); DPE contact |
| TAF9 | TAF$_{\mathrm{II}}$31/32 | TAF$_{\mathrm{II}}$40 | Taf17 | histone fold (H3-like); DPE contact; target of VP16 and p53 |

Five of the TAFs pair through **histone folds** ([7.2.4](/7.2.4)), TAF6 with TAF9 resembling H4 with H3, which once suggested that TFIID might contain a histone-like octamer that wraps DNA. Cryo-electron microscopy of human TFIID (Nogales and colleagues, 2016–2021) shows instead a flexible horseshoe of three lobes that binds the core promoter over about $60$ bp, contacting the TATA box through TBP, the Inr through TAF1 and TAF2, and the downstream elements through TAF1, TAF2, TAF6 and TAF9, and then hands TBP over to the DNA. Several TAFs (TAF5, TAF6, TAF9, TAF10, TAF12) are shared with the coactivator complex SAGA, which can also deliver TBP to promoters.

### 13.3.2. What TAFs Do

1. *Recognition of core elements other than the TATA box.* Purified TBP and TFIID support transcription equally well from a promoter with only a TATA box, but TFIID is much more active on a promoter that also has an Inr and a downstream element. In photo-cross-linking experiments, a template with 5-bromodeoxyuridine incorporated near the start site was irradiated with TFIID bound; TAF1 and TAF2 became cross-linked, TBP alone did not (Verrijzer, Tjian and colleagues, 1995). A ternary complex of TBP, TAF1 and TAF2 gave a footprint over the Inr and downstream region in addition to the TATA box, whereas TBP protected only the TATA box. TAFs therefore extend the footprint of TFIID to about $+35$ and allow TBP to work at TATA-less promoters; the DPE is contacted by TAF6 and TAF9.
2. *Coactivator function.* Activators contact TAFs: Sp1 contacts TAF4 (TAF$_{\mathrm{II}}$110 in *Drosophila*, TAF$_{\mathrm{II}}$130 in humans), the acidic activation domain of VP16 and the tumor suppressor p53 contact TAF9 ([7.2.14](/7.2.14)). Different combinations of TAFs are needed to respond to different activators.
3. *Enzymatic activities.* TAF1 is a protein kinase (it phosphorylates itself and the RAP74 subunit of TFIIF), a **histone acetyltransferase** ([7.2.15](/7.2.15)) and a ubiquitin-conjugating enzyme for histone H1. Its tandem pair of bromodomains binds histone tails acetylated at two neighbouring lysines, which links TFIID recruitment to the acetylation of promoter nucleosomes ([7.2.15](/7.2.15)).

### 13.3.3. Exceptions to Universality

Neither TAFs nor even TBP are required everywhere.

- In yeast, inactivating Taf145 (TAF1) with temperature-sensitive mutations reduced transcription of only a minority of genes (Walker and colleagues; Moqtaderi and colleagues, 1996). Because SAGA can deliver TBP, this was long taken to mean that most yeast genes do not need TFIID. Later experiments that depleted TFIID or SAGA rapidly and measured newly made RNA rather than steady-state mRNA (2017–2019) showed that both complexes contribute at nearly all yeast genes; the earlier result reflected slow inactivation and the buffering of mRNA levels ([7.2.18](/7.2.18)).
- Metazoa have TBP-related factors. TRF1 in *Drosophila* initiates from a TC box upstream of the TATA-dependent promoter of the *tudor* gene, so that the two promoters, $77$ bp apart, use different TBPs. TRF2 (TBPL1), which does not bind the TATA box, drives the TCT-motif promoters of ribosomal protein genes and some histone genes. In vertebrate oocytes TBP is replaced by TBPL2.
- NC2 (negative cofactor 2, a heterodimer of histone-fold proteins) binds TBP–DNA and blocks TFIIB; it represses transcription from TATA-containing promoters but stimulates transcription from DPE-dependent promoters (Willy, Kadonaga and colleagues, 2000), one of several factors that let the core promoter type determine the response to regulators.

## 13.4. TFIIB: Bridge and Start-Site Selector

Human TFIIB, cloned and expressed by Reinberg and colleagues (1991), has two parts. Its C-terminal core domain, two cyclin-like repeats, binds the TBP–DNA complex and the BREs above and below the TATA box. Its N-terminal region, a zinc ribbon followed by a "B-reader" helix and a "B-linker", binds Pol II at the dock domain and reaches through the polymerase toward the active center (crystal structure of a Pol II–TFIIB complex, Kornberg and colleagues, 2004). TFIIB thus links the TATA box to the polymerase with a fixed geometry. This explains the constant distance of $25$–$30$ bp between the TATA box and the start site in metazoan promoters (Example 12.4.2): TBP–TFIIB places the active center coarsely, and the B-reader, near the template strand in the open complex, positions the start site finely at an Inr-like sequence.

In budding yeast the start site lies $40$–$120$ bp downstream of the TATA box. The PIC assembles at the same distance as in other eukaryotes, opens the DNA and then scans downstream, with the polymerase pulling DNA into the complex, until a favorable initiator sequence is found; mutations in TFIIB (the *sua7* mutations) and in Pol II (Rpb9) shift the start sites, showing that the two proteins together select them.

## 13.5. TFIIH: Opening, CTD Phosphorylation and Promoter Escape

### 13.5.1. Two Enzymes in One Factor

TFIIH is the last general transcription factor to join the PIC and the only one with enzymatic activities required for initiation: a DNA-dependent ATPase in the XPB subunit and a protein kinase, CDK7, in the kinase module. Its other ATPase, XPD, is a $5' \to 3'$ helicase. Several TFIIH subunits were identified as products of genes mutated in the human DNA-repair disorders xeroderma pigmentosum (XPB, XPD) and trichothiodystrophy (p8), and TFIIH is a core component of **nucleotide-excision repair** ([7.2.8](/7.2.8)), where its helicase opens the DNA around a lesion. The dual role explains **transcription-coupled repair**: a Pol II stalled at a lesion is the signal that recruits the repair machinery.

**Example 13.5.1 (TFIIH phosphorylates the CTD)** Preinitiation complexes assembled with Pol IIA on a labeled promoter fragment were incubated with ATP and analyzed by gel mobility shift. Only when TFIIH was present did ATP shift the mobility of the complex, and Western blots showed the conversion of the largest subunit from IIa to IIo, which TFIIE enhanced. Purified TFIIH phosphorylated Pol IIA and IIO but not Pol IIB, which lacks the CTD; after chymotrypsin cleavage, which releases the CTD, the label was found in the CTD fragment (Lu, Reinberg and colleagues, 1992). The kinase was later identified as CDK7, which phosphorylates Ser5 (and Ser7) of the heptad repeat.

### 13.5.2. Opening the Promoter

How TFIIH opens the DNA has been revised. The yeast homolog of XPB (Rad25, also called Ssl2) unwinds DNA in an ATP-dependent helicase assay, and TFIIH was therefore thought to unwind the start site as a conventional helicase. Three later findings changed this picture:

1. Pol II is the only nuclear polymerase whose promoter opening requires ATP hydrolysis, and only on linear templates. On negatively **supercoiled** templates, in which the strain of the duplex favors opening ([7.2.3](/7.2.3)), TBP, TFIIB and Pol II initiate without TFIIE, TFIIH or ATP (Parvin and Sharp, 1993); this is why some early experiments concluded that TFIIE and TFIIH are needed not for opening but only for promoter clearance.
2. The helicase activity of XPB and the helicase and ATPase activities of XPD are dispensable for transcription; the ATPase of XPB is essential.
3. Cryo-EM structures of the PIC (Nogales and colleagues, 2016; Cramer and colleagues, 2016–2017) place XPB not at the start site but on downstream DNA, about $20$–$30$ bp downstream. XPB is a double-stranded DNA translocase: anchored to the rest of the PIC, it pumps downstream DNA into the polymerase cleft, while TBP and TFIIB hold the upstream DNA. The DNA in between is thereby underwound until it melts, from about $-9$ to $+2$, and the template strand drops into the active site.

**Definition 13.5.1** The transition in which RNA polymerase, having initiated, breaks its contacts with the promoter and the factors bound there and moves downstream as a stable elongation complex is called **promoter clearance** (promoter escape).

As the first nucleotides are added, the open region expands downstream (**scrunching**, as in bacteria, [7.2.10](/7.2.10)), and short transcripts are released (**abortive initiation**). When the RNA is about $10$ nt long the upstream part of the bubble reanneals, TFIIH is no longer required and the complex is committed to escape; by a transcript length of about $30$ nt the polymerase has become a stable elongation complex. Phosphorylation of Ser5 helps release Pol II from Mediator and from the PIC, and TFIIE and TFIIH dissociate, while TBP, TFIIA and part of TFIIB, TFIID and Mediator remain at the promoter as a scaffold for the next round of initiation.

### 13.5.3. Promoter-Proximal Pausing

In metazoa, Pol II that has escaped often stops again $20$–$60$ nt downstream of the start site. This was discovered at the *Drosophila* heat-shock gene *hsp70*, where UV cross-linking and run-on experiments showed an engaged polymerase near $+20$ to $+40$ before heat shock (Gilmour and Lis, 1986; Rougvie and Lis, 1988), ready to transcribe within seconds of induction. Genome-wide nascent-RNA methods (GRO-seq, PRO-seq) show that pausing occurs at most active and many inactive genes of flies and mammals. The paused polymerase is held by two factors, DSIF (Spt4–Spt5) and NELF, and released by the kinase P-TEFb (CDK9 with cyclin T), which phosphorylates NELF (which then leaves), Spt5 (which becomes a positive elongation factor) and Ser2 of the CTD. Much of P-TEFb is held inactive in a complex with the Pol III product 7SK RNA ([7.2.12](/7.2.12)) and the protein HEXIM; it is released from this complex and brought to genes by the bromodomain protein BRD4, by activators such as c-Myc and NF-κB, and, at the HIV promoter, by the viral Tat protein. The release of paused polymerase is thus a second regulated step after PIC assembly.

**Example 13.5.2 (The pausing index)** ChIP-seq ([7.2.6](/7.2.6)) of Pol II at a paused gene shows a sharp peak near the promoter and a low density over the gene body. Let $J$ be the flux of polymerases through the gene (polymerases per second), $k_{\mathrm{r}}$ the rate constant for release from the pause, and $v$ the elongation rate. At steady state the number of paused polymerases is $J/k_{\mathrm{r}}$, and a window of $w$ bp in the gene body contains $Jw/v$ polymerases. The ratio of the two signals, the *pausing index*, is
$$
\mathrm{PI} = \frac{J/k_{\mathrm{r}}}{Jw/v} = \frac{v}{k_{\mathrm{r}}\,w},
$$
independent of the flux. With $v = 2\,\mathrm{kb\,min^{-1}} \approx 33\,\mathrm{nt\,s^{-1}}$, a pause lifetime $1/k_{\mathrm{r}} = 5\,\mathrm{min}$ and $w = 300\,\mathrm{bp}$, $\mathrm{PI} = 33 \times 300/300 \approx 33$, within the range of $10$–$100$ observed for paused genes. The same calculation shows why the pausing index alone cannot tell whether a gene is regulated at pause release: a gene with a long pause and a high initiation rate and a gene with a long pause and a low initiation rate have the same index; measuring $J$ requires the gene-body density or the nascent-RNA output.

## 13.6. Elongation

### 13.6.1. The CTD Phosphorylation Cycle

Phosphorylation of the CTD changes along a gene. Chromatin immunoprecipitation with antibodies specific for each phosphoserine (Komarnitsky, Cho and Buratowski, 2000) showed that Ser5-phosphorylated Pol II is concentrated near the promoter and declines downstream, while Ser2 phosphorylation increases toward the $3'$ end. The kinases and phosphatases responsible are:

| Mark | Placed by | Removed by | Read by (examples) |
|---|---|---|---|
| Ser5-P (promoter-proximal) | CDK7 of TFIIH (Kin28 in yeast) | Ssu72, Rtr1 | capping enzyme ([7.2.17](/7.2.17)); Set1 (H3K4 methylation, [7.2.15](/7.2.15)) |
| Ser2-P (gene body, $3'$ end) | CDK9 of P-TEFb (metazoa); Ctk1 and Bur1 (yeast) | Fcp1 | splicing and polyadenylation factors ([7.2.16](/7.2.16), [7.2.17](/7.2.17)); Set2 (H3K36 methylation) |
| Ser7-P | CDK7 | Ssu72 | snRNA $3'$ processing (Integrator) |

If Ser2 phosphorylation is lost during elongation, the polymerase pauses until it is rephosphorylated. After termination the CTD is dephosphorylated completely, so that the polymerase can return to a promoter as Pol IIA. The cycle couples transcription to RNA processing: each processing machine is recruited to the polymerase at the stage of transcription at which its substrate appears (figure, panel A).

Elongation by Pol II in vivo proceeds at about $1$–$4\,\mathrm{kb\,min^{-1}}$. At $2.4\,\mathrm{kb\,min^{-1}}$ the $2.2\,\mathrm{Mb}$ human dystrophin gene takes $2.2 \times 10^6/2.4 \times 10^3 \approx 900\,\mathrm{min}$, about $15\,\mathrm{h}$, to transcribe, in agreement with the $16\,\mathrm{h}$ measured directly (Tennyson, Klamut and Worton, 1995). For long genes, elongation rather than initiation sets the delay between a signal and the appearance of the mRNA.

### 13.6.2. TFIIS, Backtracking and Proofreading

Eukaryotes control transcription mainly at initiation, but elongation is also regulated. TFIIS, isolated from HeLa cells as a factor that stimulates transcription by Pol II (Reinberg and Roeder, 1987), had no effect on initiation but stimulated elongation when added to preinitiated complexes. Its mechanism became clear from the behavior of polymerase at pause sites.

**Definition 13.6.1** The reverse sliding of an RNA polymerase along the template and the RNA, by which the RNA–DNA hybrid moves upstream and the $3'$ end of the RNA is extruded from the active site into the secondary channel, is called **transcriptional backtracking**.

Polymerases do not move at a uniform rate. At sequences that destabilize the RNA–DNA hybrid, a polymerase can backtrack by a few nucleotides and resume after diffusing forward again. If it backtracks too far, typically by more than about $10$ nt, it cannot recover on its own: it is arrested. TFIIS rescues an arrested polymerase. Its C-terminal zinc-ribbon domain inserts through pore 1 ([7.2.12](/7.2.12)), and a β-hairpin at its tip carries two acidic residues that complete a second metal-binding site in the active center (structure of the Pol II–TFIIS complex, Kettenberger, Armache and Cramer, 2003). This converts the polymerase's weak intrinsic RNA cleavage activity into a fast one: the extruded RNA is cut off, a new $3'$-OH is positioned in the active site, and transcription resumes. The bacterial factors GreA and GreB work the same way ([7.2.10](/7.2.10)).

The same reaction corrects errors. A misincorporated nucleotide destabilizes the $3'$ end of the hybrid and favors backtracking by one position; cleavage then removes a dinucleotide containing the error, and the polymerase tries again (Thomas, Platas and Hawley, 1998). Whether an error is removed is decided by a kinetic competition.

**Formula 13.6.1 (Proofreading by transcript cleavage)** After a misincorporation, let the polymerase extend the mismatched end with rate constant $k_{\mathrm{ext}}$ (which seals the error into the RNA) or backtrack and cleave it with rate constant $k_{\mathrm{c}}$. The probability that the error is removed is $k_{\mathrm{c}}/(k_{\mathrm{c}} + k_{\mathrm{ext}})$, and the error rate is reduced from the misincorporation frequency $\varepsilon_0$ to
$$
\varepsilon = \varepsilon_0\,\frac{k_{\mathrm{ext}}}{k_{\mathrm{c}} + k_{\mathrm{ext}}}. \tag{13.2}
$$
Proofreading is effective because extension from a mismatched end is slow: if $k_{\mathrm{ext}}$ is $10^{-2}$ of the rate of normal elongation, a cleavage rate even a few percent of normal elongation removes most errors. TFIIS raises $k_{\mathrm{c}}$ and so lowers $\varepsilon$; the same equation shows the cost, since a fraction of correctly made RNA ends is also cleaved and resynthesized (figure, panel B).

![Control of Pol II after initiation (idealized models). A: Pol II density along a paused gene (ChIP-like profile with a promoter-proximal peak and a uniform gene-body level; pausing index from Example 13.5.2) and the fractions of polymerase phosphorylated on Ser5 and Ser2 of the CTD, modeled as exponential loss of Ser5-P and gain of Ser2-P with distance. B: proofreading by transcript cleavage, Eq. (13.2): the factor by which errors are reduced against the cleavage rate constant, for extension from a mismatch 100 and 1000 times slower than normal elongation; TFIIS raises the cleavage rate](./plots/elongation-control.py)

## 13.7. Factors for Polymerases I and III

### 13.7.1. Class I: SL1 and UBF

Pol I needs only two factors in mammals.

- *SL1* (selectivity factor 1; TIF-IB in mouse), isolated from HeLa cells for its ability to direct Pol I to initiate accurately on a human rRNA template, binds the core element and recruits the polymerase. Immunoprecipitation with antibodies against TBP brought down SL1 activity together with three (later four) TAFs distinct from those of TFIID (Comai, Tanese and Tjian, 1992), now called TAF1A–TAF1D (formerly TAF$_{\mathrm{I}}$48, TAF$_{\mathrm{I}}$63, TAF$_{\mathrm{I}}$110, TAF$_{\mathrm{I}}$41). Fully functional SL1 can be reconstituted from TBP and these TAFs, and TAF$_{\mathrm{I}}$s and TAF$_{\mathrm{II}}$s compete for binding to TBP: the same TBP is directed to class I or class II promoters by the TAFs it carries. SL1 is responsible for the species specificity of class I promoters (Section 12.6).
- *UBF* (upstream binding factor), a protein of $97\,\mathrm{kDa}$ (with a $94\,\mathrm{kDa}$ splice variant), binds both the upstream control element and the core element through several HMG boxes and bends the DNA into a loop of almost one full turn. In footprinting experiments (Bell, Tjian and colleagues, 1988) SL1 produced no footprint on its own but enhanced and extended the footprint of UBF over both elements; in transcription, SL1 was required for basal activity and UBF stimulated it, even on templates lacking the upstream element. The reliance on UBF varies between organisms.

A third factor, TIF-IA (RRN3), binds Pol I and connects it to SL1; its activity is controlled by nutrient and growth-factor signaling, which is how the rate of ribosome synthesis (Example 12.6.2) is matched to growth.

### 13.7.2. Class III: TFIIIA, TFIIIB and TFIIIC

**Example 13.7.1 (TFIIIB stays, TFIIIC can go)** Kassavetis, Geiduschek and colleagues (1990) assembled TFIIIC and TFIIIB on a yeast tRNA gene. TFIIIC alone gave a footprint over boxes A and B inside the gene; adding TFIIIB extended the footprint upstream of the start site, to about $-40$. Treatment with heparin, a polyanion that strips most proteins from DNA, removed TFIIIC but left TFIIIB bound upstream, and the TFIIIB–DNA complex alone directed Pol III to the correct start site for many rounds of transcription. A complex stalled after a 17 nt transcript by withholding a nucleotide still showed the TFIIIB footprint, so TFIIIB stays at the promoter while the polymerase transcribes.

| Factor | Composition | Role |
|---|---|---|
| TFIIIA | one protein with nine $\mathrm{Cys_2His_2}$ **zinc fingers** ([7.2.14](/7.2.14)) | binds the internal promoter of 5S rRNA genes only (and 5S rRNA itself); the first eukaryotic transcription factor discovered (Engelke, Roeder and colleagues, 1980) |
| TFIIIC | six subunits, about $600\,\mathrm{kDa}$ in yeast | binds box A (τA lobe) and box B (τB lobe), joined by a flexible linker so that it can span boxes $30$–$90$ bp apart; assembly factor that positions TFIIIB |
| TFIIIB | TBP, Brf1 (TFIIB-related) and Bdp1 | binds about $40$ bp upstream of the start site without sequence specificity; recruits Pol III; remains bound for repeated rounds |
| SNAPc | five subunits | binds the PSE of type 3 promoters; with TFIIIB containing Brf2 instead of Brf1 |

The order of assembly is the reverse of the logic for Pol II: TFIIIC (with TFIIIA at 5S rRNA genes) binds the internal promoter first and serves as the center around which the complex organizes; TFIIIB is then placed upstream, and only TFIIIB contacts the polymerase. Pol III then transcribes, terminates at a run of T residues and is recaptured efficiently by the same gene ("facilitated recycling"). TFIIIA also binds 5S rRNA; in *Xenopus* oocytes most TFIIIA is stored in a particle with 5S rRNA, so that accumulation of the product limits the factor needed for its own synthesis.

## 13.8. Three Unifying Principles

The three systems look different, but they share an organization (course slides after Weaver):

1. *Assembly begins with an assembly factor* that recognizes a specific sequence in the promoter and recruits the rest: TBP (in TFIID) at TATA-containing class II promoters, TAFs at TATA-less class II promoters, UBF and SL1 at class I promoters, TFIIIC (and TFIIIA) at internal class III promoters, SNAPc at type 3 class III promoters.
2. *TBP plays an organizing role at nearly all promoters*, even where it does not bind first and does not contact a TATA box, by being part of the complex that contacts the polymerase: TFIID–TFIIB for Pol II, SL1 for Pol I, TFIIIB for Pol III.
3. *The specificity of TBP is governed by the proteins associated with it*: TFIID TAFs for class II, SL1 TAFs for class I, Brf1 or Brf2 and Bdp1 for class III. The TFIIB-related proteins (TFIIB, Brf1 and Brf2, and the Rrn7 subunit of the yeast Pol I core factor) form a family, all of which bridge TBP to their polymerase.

| | Class I | Class II | Class III |
|---|---|---|---|
| Assembly factor | UBF (and SL1) | TFIID (TBP, TAFs) | TFIIIC (TFIIIA for 5S), SNAPc |
| TBP-containing factor | SL1 (TBP + TAF1A–D) | TFIID | TFIIIB (TBP + Brf1/Brf2 + Bdp1) |
| TFIIB-like protein | Rrn7 / TAF1B | TFIIB | Brf1, Brf2 |
| Factor-like subunits built into the polymerase | A49–A34.5 (TFIIF/E-like), A12.2 (TFIIS-like) | none (separate TFIIF, TFIIE, TFIIS) | C37–C53 (TFIIF-like), C82–C34–C31 (TFIIE-like), C11 (TFIIS-like) |
| Promoter opening | no ATP needed | XPB translocase, ATP | no ATP needed |

The last two rows explain why Pol II needs the largest set of separate factors: its promoters are the most diverse and most regulated, and functions that are fixed in the other two polymerases are separate, dissociable proteins in the Pol II system, each a potential point of regulation. The archaeal system, with TBP, a TFIIB homolog (TFB) and a polymerase related to Pol II, is the simplest version of this design and probably resembles the ancestor of all three.

## Summary

| Topic | Key facts |
|---|---|
| General factors and PIC (Definition 13.1.1) | TFIIA, B, D, E, F, H with Pol II; order D(A) → B → Pol II–F → E → H by gel shift (Example 13.1.1); footprints $-42$ to $-17$ (DAB), extended to $+17$ by Pol II–F (Example 13.1.2); stepwise and holoenzyme pathways; Erlang waiting times, Eq. (13.1) |
| TBP (Definition 13.2.1) | $38\,\mathrm{kDa}$, conserved C-terminal $180$ residues; minor groove (I·C substitution); saddle of β-sheet, phenylalanine intercalation, $80°$ bend; universal for Pol I, II, III (ts TBP, Example 13.2.1) |
| TAFs (Definition 13.3.1) | 13–14 in TFIID; TAF1 (TAF$_{\mathrm{II}}$250), TAF2 (TAF$_{\mathrm{II}}$150) contact Inr and downstream DNA; TAF6–TAF9 histone-fold pair at the DPE; coactivator targets (Sp1–TAF4, VP16–TAF9); TAF1 HAT, kinase, double bromodomain; exceptions TRF1, TRF2, NC2 |
| TFIIB | C-terminal core on TBP and BRE, N-terminal zinc ribbon and B-reader in Pol II; TATA-to-start distance $25$–$30$ bp; start-site scanning in budding yeast |
| TFIIH | 10 subunits; XPB translocase opens DNA from $-9$ to $+2$ by pumping downstream DNA; CDK7 phosphorylates Ser5 (Example 13.5.1); XPD helicase in nucleotide-excision repair; promoter clearance (Definition 13.5.1) at about $10$ nt |
| Pausing | $20$–$60$ nt downstream; DSIF, NELF, P-TEFb (CDK9), 7SK–HEXIM; pausing index $v/(k_{\mathrm{r}}w)$ (Example 13.5.2) |
| CTD cycle | Ser5-P near promoters (CDK7), Ser2-P toward $3'$ ends (CDK9, Ctk1); recruits processing factors; elongation $1$–$4\,\mathrm{kb\,min^{-1}}$ (dystrophin: $16\,\mathrm{h}$) |
| TFIIS | transcriptional backtracking (Definition 13.6.1), arrest rescue by stimulated cleavage through pore 1; proofreading $\varepsilon = \varepsilon_0 k_{\mathrm{ext}}/(k_{\mathrm{c}} + k_{\mathrm{ext}})$, Eq. (13.2) |
| Class I | SL1 (TBP + TAF1A–D, species specificity), UBF (HMG boxes, loops DNA), TIF-IA |
| Class III | TFIIIA (9 zinc fingers, 5S only), TFIIIC (boxes A and B), TFIIIB (TBP, Brf1, Bdp1; stays bound, Example 13.7.1), SNAPc |
| Unifying principles | assembly factor first; TBP organizes all three systems; TBP's partners determine specificity |

## Questions

1. In the gel shift experiment of Example 13.1.1, what result would show that TFIIB binds TBP–DNA directly rather than binding Pol II first and bringing it to the promoter?

   **Answer** TFIIB alone with Pol II and DNA should give no promoter complex, while TFIID (or TBP) plus TFIIB without polymerase should give a distinct, more slowly migrating DAB complex. The observation that DAB forms in the absence of Pol II, and that Pol II–F binds only to DAB, shows that TFIIB binds the TBP–DNA complex first; footprinting adds that the protected region of DAB is still confined to the TATA region ($-42$ to $-17$).
2. A promoter takes on average $20\,\mathrm{s}$ to form a complete PIC. Compare the probability that a PIC has formed by $5\,\mathrm{s}$ for a one-step and a five-step assembly with this mean.

   **Answer** One step: $k = 1/20\,\mathrm{s^{-1}}$, $\mathbb{P}(T \le 5) = 1 - \mathrm{e}^{-0.25} \approx 0.22$. Five steps: $k = 5/20 = 0.25\,\mathrm{s^{-1}}$, $kt = 1.25$, and by Eq. (13.1) $\mathbb{P} = 1 - \mathrm{e}^{-1.25}(1 + 1.25 + 0.78 + 0.33 + 0.10) = 1 - 0.2865 \times 3.459 \approx 0.009$. Multistep assembly almost never finishes early; its completion times cluster around the mean (relative standard deviation $1/\sqrt 5 \approx 0.45$ instead of $1$).
3. Why does TBP bind the minor groove, and what experiment showed it? Why are TATA boxes AT-rich?

   **Answer** TBP recognizes DNA not by reading base-specific hydrogen-bonding patterns in the major groove but by deforming the DNA: its β-sheet saddle binds a widened, flattened minor groove, and phenylalanines intercalate to kink it. Replacing A·T by I·C pairs, which preserves the minor-groove pattern (no 2-amino group) but alters the major groove, did not reduce binding. A·T-rich DNA is the easiest to unstack, unwind and bend, so the free-energy cost of the distortion is lowest at AT-rich sequences; the TATA consensus reflects deformability as much as chemical recognition.
4. Explain how XPB can open the DNA at the start site while bound $20$–$30$ bp downstream of it.

   **Answer** XPB is a double-stranded DNA translocase. Because the PIC holds the upstream DNA fixed through TBP–TFIIB, translocation of XPB along the downstream DNA, which threads the DNA into the polymerase, rotates the duplex between the two anchor points; the DNA in between becomes underwound (a local negative twist, [7.2.3](/7.2.3)) until about one turn melts at the start site. Consistently, negatively supercoiled templates, which already carry the required underwinding, open without TFIIH and ATP.
5. A ChIP-seq experiment shows that a drug that inhibits CDK9 increases the pausing index of a gene from $20$ to $200$, whereas the gene-body density of Pol II falls tenfold. Interpret this with the model of Example 13.5.2.

   **Answer** The index $v/(k_{\mathrm{r}}w)$ rises tenfold if $k_{\mathrm{r}}$ falls tenfold (CDK9, as P-TEFb, is needed for pause release). The gene-body density, $J/v$, falls tenfold, so the flux $J$ falls tenfold: release from the pause has become rate-limiting for the whole gene. The number of paused polymerases, $J/k_{\mathrm{r}}$, is then roughly unchanged, which is what one expects if a paused polymerase also prevents new initiation, so that the pause site is kept occupied whatever its lifetime.
6. Using Eq. (13.2), estimate the improvement in fidelity provided by TFIIS-stimulated cleavage if extension from a mismatch occurs at $0.3\,\mathrm{s^{-1}}$, intrinsic cleavage at $0.03\,\mathrm{s^{-1}}$, and TFIIS raises cleavage to $3\,\mathrm{s^{-1}}$.

   **Answer** Without TFIIS, $\varepsilon/\varepsilon_0 = 0.3/(0.03 + 0.3) \approx 0.91$: only about $9\%$ of errors are removed. With TFIIS, $\varepsilon/\varepsilon_0 = 0.3/(3 + 0.3) \approx 0.09$: errors are reduced to about $0.1\,\varepsilon_0$, a tenfold improvement over the intrinsic enzyme. Since normal elongation runs at about $30\,\mathrm{s^{-1}}$, correct ends rarely backtrack long enough to be cleaved, so the cost in wasted synthesis is small.
7. Why can TFIIIB direct multiple rounds of transcription after TFIIIC has been stripped off, whereas a Pol II promoter needs its activators to keep reinitiating?

   **Answer** TFIIIC is an assembly factor: its only job is to position TFIIIB upstream of the start site, and TFIIIB, once placed, is an extremely stable complex that alone contacts and recruits Pol III. Pol III genes are mostly constitutive, and their output depends on the stability of TFIIIB and on facilitated recycling. At Pol II promoters only a scaffold (TFIID, TFIIA, part of TFIIB, Mediator) remains after escape; Pol II, TFIIF, TFIIE and TFIIH must be recruited again for every round, and this recruitment is where activators act, which is what makes class II transcription regulatable.
