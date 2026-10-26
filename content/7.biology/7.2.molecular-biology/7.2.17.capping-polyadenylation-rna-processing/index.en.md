---
title: Capping, Polyadenylation and RNA Processing
description: The 5′ cap (structure, cap 0/1/2, the three-enzyme capping pathway, four functions and their evidence, noncanonical NAD caps); 3′-end formation by cleavage and polyadenylation (AAUAAA and downstream elements, CPSF, CstF, PAP, PABPN1, two-phase kinetics, alternative polyadenylation); coupling of processing to transcription through the Pol II CTD; termination of Pol II (allosteric and torpedo models, Xrn2); processing of rRNA and tRNA precursors (45S pathway, snoRNPs, RNase III, RNase P, RNase Z, CCA addition, modified nucleotides); trans-splicing and RNA editing by guide RNAs, ADAR and APOBEC.
---

A eukaryotic **pre-mRNA** is modified at both ends while it is being made: a methylated guanosine is attached to its $5'$ end through an unusual $5'$–$5'$ triphosphate, and its $3'$ end is produced not by termination but by cleavage, followed by the addition of a tail of about 250 adenylates that no gene encodes. Together with **splicing** ([7.2.16](/7.2.16)), these reactions turn a transcript into an exportable, translatable and appropriately long-lived mRNA, and they are coordinated by the **C-terminal domain** of **RNA polymerase** II, which carries the processing enzymes along the gene ([7.2.12](/7.2.12), [7.2.13](/7.2.13)). Cleavage at the poly(A) site also triggers termination of transcription. This chapter treats the two ends of the mRNA (17.1–17.2), the coupling of processing to transcription (17.3) and termination (17.4), then the processing of the stable RNAs, rRNA and tRNA, in bacteria and **eukaryotes** (17.5), and finally the reactions that change an RNA's sequence after transcription: trans-splicing and RNA editing (17.6). What happens to the finished mRNA in the cytoplasm, its stability and its control by small RNAs, follows in [7.2.18](/7.2.18).

## 17.1. The 5′ Cap

### 17.1.1. Structure

By 1974 mRNAs from animal cells and viruses were known to be methylated, with much of the methylation clustered at the $5'$ end. Furuichi, Miura, Shatkin and colleagues worked out the structure with the mRNAs of reovirus and cytoplasmic polyhedrosis virus, which could be labeled and purified in large amounts: digestion with nucleases released a $5'$-terminal fragment with a net charge of about $-5$, resistant to phosphatase, which contained 7-methylguanosine joined to the first transcribed nucleotide through three phosphates.

**Definition 17.1.1 (5′ Cap)** The **5′ cap** of a eukaryotic mRNA is a 7-methylguanosine ($\mathrm{m^7G}$) joined by a $5'$–$5'$ triphosphate bridge to the first transcribed nucleotide, written $\mathrm{m^7G(5')ppp(5')N}$. In cap 0 the first nucleotide is unmethylated; in cap 1 its ribose is $2'$-O-methylated ($\mathrm{m^7GpppN_m}$); in cap 2 the second nucleotide is $2'$-O-methylated as well.

The structure of a cap-1 end beginning with adenosine is:

```smiles
CO[C@@H]1[C@H](O)[C@@H](COP(=O)([O-])OP(=O)([O-])OP(=O)([O-])OC[C@H]2O[C@@H](n3c[n+](C)c4c(=O)[nH]c(N)nc43)[C@H](O)[C@@H]2O)O[C@H]1n1cnc2c(N)ncnc21 m7GpppAm
```

The $\mathrm{m^7G}$ carries a positive charge on its imidazole ring, which is essential for recognition by cap-binding proteins: the methylated base is sandwiched between two aromatic **side chains** of eIF4E, a cation–π interaction that unmethylated guanosine cannot make. Budding yeast mRNAs carry cap 0; mRNAs of vertebrates carry cap 1, often with partial cap 2, and when the first nucleotide is adenosine it is frequently also methylated at $\mathrm{N^6}$ ($\mathrm{m^6A_m}$). The snRNAs made by Pol II acquire a trimethylated cap ($\mathrm{m^{2,2,7}G}$) in the cytoplasm ([7.2.16](/7.2.16)).

### 17.1.2. Synthesis

The first nucleotide of a transcript keeps its $5'$-triphosphate (pppN…), because polymerases start chains with a nucleoside triphosphate ([7.2.10](/7.2.10)). Capping converts this end in three reactions:

1. RNA triphosphatase removes the γ-phosphate: $\mathrm{pppN\cdots} \to \mathrm{ppN\cdots} + \mathrm{P_i}$.
2. Guanylyltransferase transfers GMP from GTP to the diphosphate end, through a covalent enzyme–lysine–GMP intermediate: $\mathrm{E} + \mathrm{GTP} \to \mathrm{E\text{-}pG} + \mathrm{PP_i}$, then $\mathrm{E\text{-}pG} + \mathrm{ppN\cdots} \to \mathrm{G(5')ppp(5')N\cdots} + \mathrm{E}$. The α-phosphate of the bridge comes from GTP; the β- and γ-positions of the bridge are the α- and β-phosphates of the first nucleotide.
3. Guanine-N7 methyltransferase and then cap $2'$-O-methyltransferase transfer methyl groups from **S-adenosylmethionine** to the guanine and to the first nucleotide.

Furuichi, Shatkin and colleagues established the order by synthesizing caps in vitro on model **substrates** such as $\mathrm{pppG_pC}$ and identifying the intermediates ($\mathrm{ppGpC}$, $\mathrm{GpppGpC}$, $\mathrm{m^7GpppGpC}$) by chromatography; labeling with $[\beta\text{-}{}^{32}\mathrm{P}]$ and $[\gamma\text{-}{}^{32}\mathrm{P}]$ nucleotides showed which phosphates are retained. In mammals the triphosphatase and guanylyltransferase are two **domains** of one protein (RNGTT); in yeast they are separate (Cet1 and Ceg1), and the methyltransferase is Abd1. Because the capping enzyme binds the Ser5-phosphorylated CTD (17.3), capping is completed before the RNA is about $25$–$30\,\mathrm{nt}$ long, as soon as its $5'$ end emerges from the polymerase.

### 17.1.3. Functions

The cap has at least four functions, each established by comparing capped and uncapped RNAs:

| Function | Evidence |
|---|---|
| Protects the mRNA from $5'$ **exonucleases** | Furuichi, LaFiandra and Shatkin (1977): reovirus mRNAs injected into *Xenopus* oocytes; capped RNAs survived for hours, uncapped ones ($\mathrm{pppG\cdots}$) were degraded within an hour. Removal of the cap (decapping) is the **committed step** in the decay of many mRNAs ([7.2.18](/7.2.18)) |
| Enhances translation | Capped viral mRNAs are translated much better than uncapped ones in wheat germ and reticulocyte extracts (Both, Banerjee and Shatkin, 1975), and cap analogs such as $\mathrm{m^7GTP}$ inhibit translation by competing for eIF4E, which recruits the ribosome ([7.2.19](/7.2.19)) |
| Mediates export | Hamm and Mattaj (1990): a U1 snRNA gene rearranged to be transcribed by Pol III produced uncapped U1 RNA that stayed in the nucleus, whereas Pol II-transcribed, capped U1 was exported; the nuclear cap-binding complex (CBP80–CBP20) recruits export factors for snRNAs and mRNAs |
| Stimulates splicing of the first **intron** | Capped substrates are spliced better in vitro; depletion of the cap-binding complex reduces removal of the cap-proximal intron, because CBC helps U1 **snRNP** bind the first $5'$ splice site ([7.2.16](/7.2.16)) |

A fifth function was recognized more recently: the $2'$-O-methylation of cap 1 marks an RNA as "self". Innate-immune sensors such as RIG-I and the interferon-induced protein IFIT1 bind RNAs with cap 0 or $5'$-triphosphates, which is why many RNA viruses encode their own cap $2'$-O-methyltransferases, and why therapeutic mRNAs are made with cap-1 analogs.

**Remark 17.1.1 (Noncanonical caps)** Some RNAs carry other nucleotide metabolites at their $5'$ ends. Chen, Liu and colleagues (2009) discovered RNAs capped with **nicotinamide adenine dinucleotide** ($\mathrm{NAD^+}$) in *E. coli*, and NAD caps were later found in yeast, plants and mammals. They are added not by a capping enzyme but by RNA polymerase itself, which uses $\mathrm{NAD^+}$ in place of ATP as the first nucleotide at **promoters** starting with A; they are removed ("deNADding") by NudC in bacteria and by DXO in eukaryotes. Bacteria have no $\mathrm{m^7G}$ cap; their mRNAs keep the $5'$-triphosphate, whose conversion to a monophosphate triggers degradation ([7.2.18](/7.2.18)).

## 17.2. Polyadenylation

### 17.2.1. The Poly(A) Tail

Most mRNAs of eukaryotes and their precursors end in a stretch of adenylates, discovered in 1971 (Darnell; Edmonds; Brawerman) because mRNA bound to oligo(dT) and poly(U) columns, which became the standard way to purify mRNA. Ribosomal and transfer RNAs have no such tail; neither do the replication-dependent **histone** mRNAs, whose $3'$ end is a conserved **stem-loop** produced by a different cleavage reaction guided by U7 snRNP.

**Example 17.2.1 (Measuring tail length)** Labeled mRNA was digested with RNase A (which cuts after pyrimidines) and RNase T1 (after G); only poly(A) survives. Alkaline hydrolysis of the poly(A) gives $\mathrm{AMP}$ from every **residue** except the $3'$-terminal one, which has no $3'$ phosphate and is released as adenosine. The ratio $\mathrm{AMP}/\mathrm{adenosine}$ is therefore the mean tail length; for newly made mammalian mRNA it is about $200$–$250$, in yeast about $70$–$90$. No gene contains runs of T of that length, which showed that the tail is added after transcription by a template-independent enzyme.

**Definition 17.2.1** **Polyadenylation** is the addition of a poly(A) tail to the $3'$ end of an RNA by **poly(A) polymerase** (PAP), which adds AMP residues from ATP without a template; in eukaryotic pre-mRNAs it follows endonucleolytic cleavage of the transcript at the poly(A) site.

The tail increases both the lifetime and the translational efficiency of an mRNA, to degrees that differ between systems. Huez, Marbaix and colleagues (1974) injected globin mRNA with and without its poly(A) into *Xenopus* oocytes: both were translated at first, but synthesis from poly(A)⁻ mRNA declined after a few hours while poly(A)⁺ mRNA continued to be translated, the expected result if the tail protects the mRNA. In reticulocyte lysates, which lack nuclei and in which stability differences are small, poly(A) stimulated translation by promoting the recruitment of mRNA to polysomes (Munroe and Jacobson, 1990). The explanation of both effects is the cytoplasmic poly(A)-binding protein PABPC, which coats the tail, protects it, and binds the initiation factor eIF4G, bringing the two ends of the mRNA together in a closed loop ([7.2.19](/7.2.19)). In the cytoplasm the tail is gradually shortened, and its loss starts the degradation of the mRNA ([7.2.18](/7.2.18)). Polyadenylation is also required for efficient export from the nucleus. In bacteria the role is reversed: short poly(A) tails added by bacterial PAP I promote degradation, by providing a single-stranded platform for $3'$ exonucleases.

### 17.2.2. Signals and Factors

Transcription by Pol II continues beyond the end of the mRNA, so the $3'$ end is made by cutting the growing RNA. The cleavage site is specified by sequences around it.

**Definition 17.2.2** A **polyadenylation signal** is the set of sequences that directs cleavage and polyadenylation of a pre-mRNA; in mammals it consists of the hexamer $\mathrm{AAUAAA}$ (or a variant, most often $\mathrm{AUUAAA}$) located $10$–$30$ nt upstream of the cleavage site, a GU-rich or U-rich downstream element within about $30$ nt downstream of it, and often an upstream $\mathrm{UGUA}$ element.

The hexamer is the most conserved part: point mutations in it (for example $\mathrm{AAUAAA} \to \mathrm{AAUAGA}$ in a human α-thalassemia allele) abolish cleavage and polyadenylation. Cleavage usually occurs after a CA dinucleotide. The downstream element is variable; in the SV40 late signal it lies about $23$–$24$ nt beyond the hexamer, and mutating it reduces efficiency. Plant signals use AAUAAA-like elements more loosely, and yeast signals rarely contain AAUAAA, relying instead on an efficiency element and a positioning element.

The proteins that recognize the signal and cleave the RNA, the cleavage and polyadenylation machinery, are about 20 polypeptides in four complexes:

| Factor | Binds | Role |
|---|---|---|
| CPSF (cleavage and polyadenylation **specificity factor**; CPSF160, WDR33, CPSF30, Fip1, CPSF73, CPSF100) | $\mathrm{AAUAAA}$, through the **zinc fingers** of CPSF30 and WDR33 | Specificity; CPSF73 is the **endonuclease** (a metallo-β-lactamase fold) |
| CstF (cleavage stimulation factor; CstF64, CstF77, CstF50) | GU/U-rich downstream element (CstF64) | Stabilizes the complex; CstF50 binds the CTD |
| CFIm (CFIm25, CFIm68) | $\mathrm{UGUA}$ upstream | Enhances and selects among sites |
| CFIIm (Clp1, Pcf11), symplekin | Pcf11 binds the Ser2-phosphorylated CTD | Required for cleavage and for termination (17.4) |
| PAP, PABPN1 | $3'$ end; poly(A) | Synthesis and length control of the tail |

Pol II itself, through its CTD, is required for efficient cleavage in vitro (Hirose and Manley, 1998), an early sign that $3'$-end processing and transcription are coupled.

### 17.2.3. Two Phases of Tail Synthesis

**Example 17.2.2 (Initiation and elongation of poly(A))** Wickens and colleagues (Sheets and Wickens, 1989; Bienroth, Keller and Wahle, 1993) used substrates that were already cleaved at the poly(A) site and supplied ATP. Polyadenylation occurred in two kinetically distinct phases. In the first, slow phase about 10 A residues were added, and this phase required an intact $\mathrm{AAUAAA}$ and the factor CPSF with PAP; a cleaved substrate with a mutant hexamer was hardly polyadenylated. In the second, fast phase the tail was extended to about $250$ nt; this phase no longer depended on the hexamer but on the oligo(A) itself and on the nuclear poly(A)-binding protein PABPN1 (PAB II), stimulated by CPSF. A substrate with a mutant hexamer that carried a preformed oligo(A) tail of about 10 nt was elongated efficiently. Tail growth stopped at about $250$ nt because PABPN1, once it coats a tail of that length, disrupts the interaction between CPSF and PAP that makes PAP processive.

![Mammalian 3′-end processing. A: the signals around a poly(A) site and the factors that bind them: CFIm on UGUA, CPSF (CPSF30 and WDR33 contacting AAUAAA, CPSF73 the endonuclease) 10–30 nt upstream of the cleavage site after a CA, CstF64 on the GU/U-rich downstream element within 30 nt downstream, with CFIIm and symplekin; after cleavage, PAP extends the upstream fragment and PABPN1 coats the tail. B: a master-equation model of tail synthesis (Formula 17.2.1) with slow initiation (k_i = 0.02 s⁻¹ for the first 10 A), fast elongation (k_e = 2 s⁻¹) and arrest at 250 A: mean tail length against time for the wild-type signal, for a mutant hexamer (k_i 50-fold lower), and for the mutant with a preformed A10 tail; small panels, the distribution of tail lengths of the wild type at 2, 5 and 10 min, which is bimodal: a tail is either still short or already complete](./plots/polyadenylation.py)

**Formula 17.2.1 (Two-phase polyadenylation)** Let $p_n(t)$ be the fraction of RNAs with a tail of $n$ A residues and let each addition occur with rate constant $k_n$, equal to $k_{\mathrm{i}}$ for $n < 10$, to $k_{\mathrm{e}} \gg k_{\mathrm{i}}$ for $10 \le n < 250$, and $0$ for $n = 250$. Then
$$
\frac{\mathrm{d}p_n}{\mathrm{d}t} = k_{n-1}\,p_{n-1} - k_n\,p_n, \qquad n = 0, 1, \dots, 250, \tag{17.1}
$$
with $k_{-1}p_{-1} = 0$. The time to complete a tail is the sum of independent exponential waiting times, with mean $10/k_{\mathrm{i}} + 240/k_{\mathrm{e}}$, dominated by the initiation phase.

Because the elongation phase is fast, few molecules are caught in the middle of it: at any moment a tail is either short or complete, and the distribution of lengths is bimodal, as observed in time courses. A mutation that slows initiation delays the appearance of full-length tails without changing their length, and a preformed oligo(A) bypasses the defect, which is how the two phases were distinguished experimentally.

### 17.2.4. Alternative Polyadenylation

Most human genes, about $70\,\%$, have more than one poly(A) site, and the choice between them is regulated (alternative polyadenylation, APA). When the alternative sites lie in the last **exon**, they produce mRNAs with the same coding sequence and $3'$ untranslated regions of different length; when one lies in an intron, the choice changes the C-terminus of the protein, as for the **immunoglobulin** μ heavy chain ([7.2.16](/7.2.16)). Proliferating cells, activated T cells and many cancer cells use proximal sites more often and so make mRNAs with shorter $3'$ UTRs (Sandberg, Burge and colleagues, 2008), which escape repression by microRNAs and by destabilizing elements located in the lost sequence ([7.2.18](/7.2.18)); neurons tend to use distal sites. The level of CstF64 and CFIm is one determinant: B cells raise CstF64 when they become plasma cells, which favors the weaker upstream site of the μ gene and so the secreted form μs.

## 17.3. Coupling Processing to Transcription

Capping, splicing and polyadenylation take place mostly during transcription. Electron micrographs of **chromatin** spread from *Drosophila* embryos (Beyer and Osheim, 1988) showed nascent RNAs with lariat-like loops and spliceosome-like particles while the polymerase was still on the gene; nascent-RNA sequencing now shows that most introns in mammalian cells are removed within minutes, often before the polymerase reaches the end of the gene.

**Definition 17.3.1** **Cotranscriptional processing** is the modification of an RNA (capping, splicing, cleavage and polyadenylation, editing) while it is still being transcribed and attached to the polymerase.

The carboxyl-terminal domain (CTD) of Rpb1 is the platform for this coupling. McCracken, Bentley and colleagues (1997) expressed α-amanitin-resistant Pol II with a truncated CTD in cells treated with **α-amanitin**: the resulting transcripts were poorly capped, poorly spliced and poorly cleaved and polyadenylated. The processing enzymes bind the CTD directly, and they bind preferentially to particular phosphorylation states, which change along the gene ([7.2.13](/7.2.13)):

| Stage | CTD state | Factors recruited |
|---|---|---|
| Promoter-proximal (first $\sim 50$ nt) | Ser5-P (TFIIH) | Capping enzyme (triphosphatase–guanylyltransferase) and methyltransferase; Set1 |
| Gene body | Ser2-P rising (P-TEFb), Ser5-P falling | U1 snRNP and **SR proteins**, U2AF; Set2 |
| $3'$ end | High Ser2-P | CstF (CstF50), Pcf11, CPSF; termination factors |

**Chromatin immunoprecipitation** in yeast (Komarnitsky, Cho and Buratowski, 2000) showed this sequence directly: the guanylyltransferase was found only near promoters, together with Ser5-phosphorylated Pol II, while the cap methyltransferase and the polyadenylation factor Hrp1 were present both near and far from the promoter. The arrangement concentrates each enzyme where its substrate appears, a scaffolding strategy that speeds a series of consecutive reactions. Processing in turn feeds back on transcription: the capping enzyme helps release paused Pol II, and splicing factors stimulate elongation.

![Processing during transcription. A: one gene with RNA polymerase II at three stages: near the promoter the CTD, phosphorylated on Ser5, carries the capping enzyme, which caps the RNA before it is 30 nt long; in the gene body the CTD, increasingly phosphorylated on Ser2, delivers U1 snRNP and SR proteins to exons as they emerge; downstream of the poly(A) signal (PAS), CPSF and CstF cleave the RNA, the upstream product is polyadenylated, and the 5′ end of the downstream RNA, still attached to Pol II, is degraded 5′→3′ by Xrn2, which catches the polymerase and releases it. B: the catch-up model of Formula 17.4.1 with cleavage 0.5 min after the PAS is transcribed: the distance at which termination occurs against the speed of Pol II after the PAS, for Xrn2 moving at 5 or 10 kb min⁻¹ (illustrative values); the point marks about 1.7 kb for Pol II at 2 kb min⁻¹](./plots/cotranscriptional.py)

## 17.4. Termination by RNA Polymerase II

### 17.4.1. Termination Depends on Cleavage at the Poly(A) Site

Termination by Pol II was hard to study because the end of the mRNA is not the end of transcription: the polymerase continues for hundreds to thousands of nucleotides, and the downstream RNA is degraded too quickly to be seen. Its position was mapped by **nuclear run-on assays** ([7.2.6](/7.2.6)), in which polymerases engaged at the moment of isolation extend their RNAs with labeled nucleotides; **hybridization** to a series of probes along the gene shows where polymerases are. For the human β-globin gene, run-on signal continued through a region about $1.7\,\mathrm{kb}$ downstream of the poly(A) site and fell off beyond it (Dye and Proudfoot, 2001).

Two results showed that termination depends on the poly(A) signal. Mutation of the $\mathrm{AATAAA}$ of a globin gene abolished termination: polymerases read on into downstream genes (Whitelaw and Proudfoot, 1986; Logan and colleagues, 1987). And in yeast, temperature-sensitive mutations in factors required for cleavage at the poly(A) site (Rna14, Rna15, Pcf11) prevented termination, measured by run-on, whereas mutations in the poly(A) polymerase Pap1, which block tail synthesis but not cleavage, did not (Birse, Proudfoot and colleagues, 1998). Cleavage, not polyadenylation, is coupled to termination.

### 17.4.2. Allosteric and Torpedo Models

Two models were proposed. In the allosteric (antiterminator) model, transcription through the poly(A) signal changes the elongation complex: elongation factors are lost, termination factors are gained, and the polymerase becomes prone to release. In the torpedo model, cleavage at the poly(A) site produces a downstream RNA with a $5'$-monophosphate and no cap, still attached to the polymerase; a $5' \to 3'$ exonuclease enters at this end, degrades the RNA faster than the polymerase makes it, catches up and dislodges the polymerase.

**Definition 17.4.1 (Torpedo Model)** In the **torpedo model** of Pol II termination, the $5' \to 3'$ exonuclease Xrn2 (Rat1 in yeast) loads on the uncapped $5'$ end created by cleavage at the poly(A) site, degrades the nascent RNA that is still being made and, on reaching the polymerase, causes it to dissociate from the template.

Kim, Buratowski and colleagues (2004) in yeast and West, Gromak and Proudfoot (2004) in human cells found that inactivating Rat1 or depleting Xrn2 shifted termination downstream. The current view combines the two models. Transcription of the poly(A) signal recruits the phosphatase PP1 (with its regulatory subunit PNUTS), which dephosphorylates the elongation factor Spt5; this slows Pol II downstream of the poly(A) site, and the slowed polymerase is caught by Xrn2 (Cortazar and colleagues, 2019; Eaton and colleagues, 2020). Neither allosteric slowing nor Xrn2 alone is sufficient for efficient termination at most genes.

**Formula 17.4.1 (Catch-up distance)** Suppose cleavage occurs a time $\tau$ after the polymerase transcribes the poly(A) site, the polymerase then moves at speed $v$, and Xrn2 starts at the cleavage site and degrades the RNA at speed $u > v$. Xrn2 reaches the polymerase at a distance
$$
x^* = v\tau\,\frac{u}{u - v} \tag{17.2}
$$
downstream of the poly(A) site; if $u \le v$, Xrn2 never catches up.

With $v = 2\,\mathrm{kb\,min^{-1}}$, $\tau = 0.5\,\mathrm{min}$ and $u = 5\,\mathrm{kb\,min^{-1}}$, $x^* = 1 \times 5/3 \approx 1.7\,\mathrm{kb}$, the size of the termination zone observed at β-globin. The formula shows why slowing the polymerase matters: $x^*$ falls both through the factor $v\tau$ and because $u/(u-v)$ approaches 1, and a polymerase that elongated as fast as the exonuclease would never be terminated. Termination is thus a kinetic competition, as in bacteria ([7.2.10](/7.2.10)), between elongation and a factor that chases the polymerase along its RNA, here an exonuclease rather than the ρ helicase.

**Remark 17.4.1** For the β-globin gene, Teixeira, Proudfoot and colleagues (2004) reported that a cotranscriptional cleavage (CoTC) element downstream of the poly(A) site is cut autocatalytically, like a ribozyme, providing an entry site for Xrn2 before cleavage at the poly(A) site. CoTC-type cleavage has been found at only a few genes, and whether it is self-catalyzed in vivo is not established; it is not the general mechanism of Pol II termination. Pol I and Pol III terminate differently: Pol III stops at a run of T residues in the nontemplate strand without auxiliary factors, Pol I at sites bound by the termination factor TTF-I.

## 17.5. Processing of rRNA and tRNA

### 17.5.1. Ribosomal RNA

All rRNAs except the eukaryotic 5S rRNA are cut out of long precursors, so that equal amounts of the rRNAs of the two ribosomal subunits are made.

In *E. coli*, each of the seven *rrn* operons is transcribed by the single bacterial RNA polymerase (there is no separate rRNA polymerase in bacteria) into a precursor of about $5.5\,\mathrm{kb}$ (sedimenting at 30S) containing 16S rRNA, one or two spacer tRNAs, 23S rRNA and 5S rRNA, sometimes with further tRNAs at the $3'$ end. The 16S and 23S sequences each lie within a long stem formed by pairing of their flanking sequences; RNase III, an endonuclease specific for double-stranded RNA, cuts in these stems and releases the precursors of 16S and 23S rRNA, RNase E acts near 5S rRNA, RNase P makes the $5'$ ends of the tRNAs, and other nucleases trim the mature ends during ribosome assembly. In *rnc* mutants lacking RNase III the 30S precursor accumulates.

In eukaryotes, Pol I transcribes the rRNA genes in the nucleolus into one precursor ([7.2.12](/7.2.12)), $47\mathrm{S}$ in humans (about $13.3\,\mathrm{kb}$), containing, in the order found in all eukaryotes, the $5'$ external transcribed spacer (ETS), 18S rRNA, internal transcribed spacer 1 (ITS1), 5.8S rRNA, ITS2, 28S rRNA (25S in yeast) and the $3'$ ETS. Pulse–chase labeling of HeLa cells (Penman, Darnell and colleagues), in which host RNA synthesis was simplified by poliovirus infection, revealed the intermediates. In the main human pathway the ETSs are removed ($45\mathrm{S} \to 41\mathrm{S}$), a cleavage in ITS1 splits 41S into the 21S precursor of 18S rRNA and the 32S precursor of 5.8S and 28S, and cleavages in ITS2 release the 5.8S rRNA, which stays base-paired to the 28S rRNA. 5S rRNA is made separately by Pol III.

![Processing of stable RNAs. A: the human 47S/45S pre-rRNA (13.3 kb, Pol I), with the 5′ external transcribed spacer, 18S, ITS1, 5.8S, ITS2, 28S and 3′ ETS; removal of the ETSs gives 41S, cleavage in ITS1 gives the 21S precursor of 18S and the 32S precursor of 5.8S and 28S, and cleavage in ITS2 releases 5.8S rRNA, which remains base-paired to 28S. B: an E. coli rrn transcript (about 5.5 kb): RNase III cuts in the stems that enclose 16S and 23S rRNA, RNase P makes the 5′ end of the spacer tRNA, and RNase E cuts near 5S rRNA. C: maturation of a eukaryotic pre-tRNA: RNase P removes the 5′ leader, RNase Z the 3′ trailer, the CCA-adding enzyme adds CCA, the intron next to the anticodon is spliced, and bases are modified](./plots/rrna-trna-processing.py)

Eukaryotic rRNA processing requires about 200 proteins and many small nucleolar RNAs, and it is coupled to ribosome assembly. The snoRNAs act as guides.

**Definition 17.5.1 (snoRNA)** A **small nucleolar RNA** (snoRNA) is a noncoding RNA of $60$–$300\,\mathrm{nt}$ that, in a ribonucleoprotein (snoRNP), guides the modification of specific nucleotides in rRNA (and snRNA) by base pairing, or participates in pre-rRNA cleavage. Box C/D snoRNAs guide $2'$-O-methylation by the methyltransferase fibrillarin at the nucleotide paired $5$ positions upstream of the D (or D′) box; box H/ACA snoRNAs guide the conversion of uridine to pseudouridine by dyskerin.

Human rRNA carries about $100$ $2'$-O-methyl groups and about $100$ pseudouridines, clustered in functionally important regions of the ribosome. Most vertebrate snoRNAs are encoded in introns of other genes and are released from the debranched lariats. A few snoRNAs, such as U3, do not guide modification but pair with the pre-rRNA to direct the early cleavages that release 18S rRNA, within a large complex called the small-subunit processome; the related ribozyme RNase MRP cuts in ITS1.

### 17.5.2. Transfer RNA

Transfer RNAs are made as precursors with extra sequences at both ends; in bacteria several tRNAs, or tRNAs and rRNAs, may share one precursor, which is first cut into single-tRNA pieces by RNase III and RNase E. Eukaryotic pre-tRNAs, made by Pol III, contain one tRNA each. Maturation then has the same steps in all organisms:

1. $5'$ end. RNase P (Definition 17.5.2) makes a single endonucleolytic cut that releases the $5'$ leader and leaves the mature $5'$ end with a phosphate.
2. $3'$ end. In *E. coli*, the endonuclease RNase E cuts in the trailer and several exonucleases trim back: RNase II and polynucleotide phosphorylase remove most extra nucleotides and stop about two nucleotides short, and RNase PH and RNase T remove the last ones (RNase T the very last). In eukaryotes and many bacteria a single endonuclease, RNase Z, cuts at the mature $3'$ end.
3. CCA. All tRNAs end in CCA, to which the amino acid is attached. In eukaryotes and in many bacterial tRNAs the CCA is not encoded and is added by tRNA nucleotidyltransferase (CCA-adding enzyme), which adds C, C and A from CTP and ATP without a nucleic-acid template, using its own protein structure to select each nucleotide; in *E. coli* the CCA is encoded in all tRNA genes, and the enzyme repairs damaged ends.
4. Introns. Some eukaryotic pre-tRNAs have an intron next to the anticodon, removed by a splicing endonuclease and a ligase ([7.2.16](/7.2.16)).
5. Modification. About $10$–$15\,\%$ of the nucleotides of a tRNA are modified; over 100 different modifications are known in RNA, more than half in tRNA. Examples are pseudouridine ($\Psi$) in the TΨC loop, dihydrouridine (D) in the D loop, ribothymidine, inosine at the wobble position 34 of some anticodons ([7.2.19](/7.2.19)), and hypermodified purines next to the anticodon (queuosine, wybutosine) that stabilize codon pairing.

**Definition 17.5.2 (RNase P)** **RNase P** is the ribonucleoprotein endonuclease that cleaves the $5'$ leader from precursor tRNAs; in bacteria its RNA subunit (M1 RNA in *E. coli*, $377\,\mathrm{nt}$) is the catalyst and the protein subunit (C5, $14\,\mathrm{kDa}$) an accessory factor.

**Example 17.5.1 (The RNA of RNase P is the catalyst)** Guerrier-Takada, Altman, Pace and colleagues (1983) separated the RNA and protein of *E. coli* RNase P. At the physiological $10\,\mathrm{mM}$ $\ce{Mg^2+}$ neither subunit alone cut pre-tRNA, but at high $\ce{Mg^2+}$ ($60\,\mathrm{mM}$) and high salt the M1 RNA alone cleaved pre-tRNA accurately and with multiple turnover; the protein is needed under cellular conditions, where it neutralizes repulsion between the negatively charged RNA enzyme and its substrate and contacts the leader. M1 RNA was the first RNA enzyme found to act on another molecule, a true ribozyme. Eukaryotic nuclear RNase P has a homologous RNA with about ten proteins, and the RNA is still catalytic; but human mitochondria and plant organelles use a protein-only RNase P (PRORP), which shows that the RNA catalyst could be replaced by a protein during evolution.

## 17.6. Trans-Splicing and RNA Editing

### 17.6.1. Trans-Splicing

**Definition 17.6.1 (Trans-Splicing)** **Trans-splicing** is splicing that joins exons from two separate RNA molecules; in the common spliced-leader type, a short leader exon from a dedicated small RNA (the SL RNA) is joined to the $5'$ end of many different pre-mRNAs.

In trypanosomes, every mRNA begins with the same 39-nt spliced leader (first described as 35 nt, Boothroyd and Cross, 1982, in the mRNA of the variant surface glycoprotein; the leader was absent from the gene). The leader is the $5'$ exon of the SL RNA, about $140\,\mathrm{nt}$, encoded by some 200 tandem gene copies; its $3'$ part is a half-intron with a $5'$ splice site. The pre-mRNAs carry a branch point and a $3'$ splice site but no $5'$ splice site upstream. The branch A of the pre-mRNA attacks the $5'$ splice site of the SL RNA, forming a Y-shaped (branched but not circular) intermediate instead of a lariat; the $3'$-OH of the leader then attacks the $3'$ splice site. The chemistry is that of *cis* splicing, and the SL RNA acts as both exon donor and an snRNA. Trypanosomes transcribe their genes as long polycistronic units, and trans-splicing, coupled to polyadenylation of the upstream gene, cuts them into individual mRNAs. In *Caenorhabditis elegans* about $70\,\%$ of mRNAs are trans-spliced to SL1, and the downstream genes of its operons (about $15\,\%$ of genes) receive the SL2 leader, which separates them from the polycistronic precursor.

### 17.6.2. Editing by Guide RNAs

**Definition 17.6.2 (RNA Editing)** **RNA editing** is any change of the nucleotide sequence of an RNA after transcription other than splicing and end processing: insertion or deletion of nucleotides, or conversion of one base to another.

Benne and colleagues (1986) found that the mitochondrial mRNA for cytochrome oxidase subunit II of trypanosomes contains four U residues absent from the gene, which correct a frameshift. In other trypanosome mitochondrial mRNAs editing is far more extensive: in the mRNA for subunit III of *Trypanosoma brucei* (Feagin and colleagues, 1988), 407 U residues are inserted and 19 deleted, so that more than half of the mature mRNA is not encoded in the gene ("pan-editing"); the genes, which cannot be translated as they stand, are called cryptogenes. The information comes from short guide RNAs (gRNAs), $50$–$70\,\mathrm{nt}$, encoded in the minicircles of the mitochondrial (kinetoplast) DNA.

The mechanism, worked out by Stuart, Simpson and colleagues, is as follows (figure). The $5'$ anchor of a gRNA pairs with the mRNA just $3'$ of the region to be edited. Where the gRNA has an A or G with no partner in the mRNA, an endonuclease of the editosome cuts the mRNA; a terminal uridylyltransferase (TUTase) adds U residues from UTP to the $3'$ end of the upstream fragment until they pair with the gRNA (G·U pairs allowed); and an RNA ligase rejoins the fragments. Deletion uses the same cut and ligation, but a U-specific $3' \to 5'$ exonuclease removes U residues that have no partner. Partially edited mRNAs are always edited at their $3'$ part and not their $5'$ part, so editing proceeds $3' \to 5'$, each gRNA creating the sequence to which the next gRNA's anchor pairs.

![RNA editing. A: guide-RNA-directed U insertion in trypanosome mitochondria (illustrative sequences). The 5′ anchor of the guide RNA pairs with the mRNA 3′ of the editing site; three unpaired A residues in the guide specify the insertion; the editosome cuts the mRNA, TUTase adds three U residues from UTP, and RNA ligase rejoins the fragments, producing an mRNA fully paired with the guide; deletion uses the same cut and ligation with a U-specific exonuclease. B: editing by deamination. ADAR2 converts A to inosine at the Q/R site of the glutamate-receptor GluA2 mRNA, turning the glutamine codon CAG into CIG, read as CGG (arginine); APOBEC1 converts C to U at codon 2153 of apolipoprotein B mRNA in the intestine, turning CAA (glutamine) into the stop codon UAA, so that the intestine makes apoB-48 and the liver, with unedited mRNA, apoB-100](./plots/rna-editing.py)

### 17.6.3. Editing by Deamination

In animals, editing is mostly the deamination of single bases. Adenosine deaminases acting on RNA (ADARs) convert adenosine to inosine in double-stranded regions; inosine pairs like G, so it is read as G by ribosomes and by reverse transcriptase.

**Example 17.6.1 (The Q/R site of GluA2)** The mRNA of the AMPA-type glutamate receptor subunit GluA2 (GluR-B) is edited by ADAR2 at a single adenosine in the codon CAG for glutamine 607, which lies in a double-stranded region formed by pairing of the exon with the downstream intron; the edited codon CIG is read as CGG, arginine. Nearly 100 % of GluA2 mRNA in the brain is edited at this site. The arginine, in the pore of the channel, makes AMPA receptors containing GluA2 impermeable to $\ce{Ca^2+}$. Mice lacking ADAR2 develop seizures and die within three weeks of birth; Higuchi, Seeburg and colleagues (2000) rescued them completely by a knock-in allele of GluA2 that encodes arginine in the DNA. The essential function of ADAR2 is therefore the editing of this one site.

ADAR1 edits thousands of sites, mostly in Alu repeats that form double-stranded structures in human $3'$ UTRs; this editing marks cellular double-stranded RNA as self, and without ADAR1 the RNA sensor MDA5 triggers an interferon response, which is why ADAR1 deficiency causes an autoimmune disease (Aicardi–Goutières syndrome). Cytidine deaminases of the APOBEC family convert C to U. APOBEC1, with the cofactor A1CF, edits codon 2153 of apolipoprotein B mRNA in the small intestine, CAA (glutamine) to UAA (stop); the intestine makes apoB-48, the N-terminal $48\,\%$ of the protein, which forms chylomicrons, while the liver, without editing, makes the full apoB-100 (4536 amino acids) of very-low-density lipoprotein. In plant mitochondria and chloroplasts, hundreds of C-to-U edits are directed by pentatricopeptide-repeat (PPR) proteins, which recognize RNA sequences with a modular protein code. The enzymes and principles of base editing in RNA and DNA have become tools for correcting mutations ([7.2.24](/7.2.24)).

## Summary

| Topic | Key points |
|---|---|
| Cap (Definition 17.1.1) | $\mathrm{m^7G(5')ppp(5')N}$; cap 0 (yeast), cap 1, cap 2, $\mathrm{m^6A_m}$; triphosphatase, guanylyltransferase (enzyme–GMP), N7- and $2'$-O-methyltransferases with SAM, done by $\sim 30\,\mathrm{nt}$; functions: stability, translation (eIF4E), export (CBC; Hamm and Mattaj), first-intron splicing, self marker; NAD caps made by polymerase (Remark 17.1.1) |
| Poly(A) (Definitions 17.2.1–17.2.2) | About $250$ A in mammals; AMP/adenosine ratio (Example 17.2.1); stability and translation via PABPC; AAUAAA $10$–$30$ nt upstream of cleavage, GU/U-rich DSE, UGUA; CPSF, CstF, CFIm, CFIIm, PAP, PABPN1 |
| Tail kinetics (Example 17.2.2, Formula 17.2.1) | Slow AAUAAA/CPSF-dependent initiation (about 10 A), fast PABPN1-dependent elongation to about $250$, then length control; Eq. (17.1); bimodal tail lengths; APA in about $70\,\%$ of genes, short $3'$ UTRs in proliferating cells |
| Coupling (Definition 17.3.1) | CTD truncation impairs all three reactions; Ser5-P recruits capping enzyme, Ser2-P splicing and $3'$-end factors; ChIP of yeast factors along genes |
| Termination (Definition 17.4.1, Formula 17.4.1) | Run-on: polymerases continue $\sim 1.7\,\mathrm{kb}$ past the β-globin poly(A) site; requires AAUAAA and cleavage factors, not PAP; Xrn2/Rat1 torpedo plus PP1–PNUTS slowing of Pol II; $x^* = v\tau u/(u-v)$; CoTC limited (Remark 17.4.1) |
| rRNA (Definition 17.5.1) | *E. coli* 30S precursor (one RNA polymerase), RNase III in flanking stems; human 47S/45S → 41S → 21S + 32S → 18S, 5.8S, 28S; box C/D and H/ACA snoRNPs for $2'$-O-methylation and pseudouridylation; U3, RNase MRP |
| tRNA (Definition 17.5.2, Example 17.5.1) | RNase P (RNA catalytic: M1 RNA), $3'$ trimming (RNase E, II, PNPase, PH, T; RNase Z), CCA addition without template, intron removal, $\sim 10$–$15\,\%$ modified nucleotides; protein-only PRORP in mitochondria |
| Trans-splicing (Definition 17.6.1) | Trypanosome 39-nt spliced leader from SL RNA; Y-shaped intermediate; resolves polycistronic transcripts; SL1/SL2 in *C. elegans* |
| Editing (Definition 17.6.2, Example 17.6.1) | Kinetoplastid gRNAs: cut, TUTase or exonuclease, ligate; $3' \to 5'$; COIII 407 U inserted; ADAR A→I (GluA2 Q/R, Alu, self RNA); APOBEC1 C→U (apoB-48/100); PPR proteins in plant organelles |

## Questions

1. Which phosphates of GTP and of the primary transcript end up in the triphosphate bridge of the cap? Design a labeling experiment that would distinguish the actual pathway from one in which the guanylyltransferase transfers GDP to a monophosphate RNA end.

   **Answer** The bridge contains the α-phosphate of GTP and the α- and β-phosphates of the first nucleotide of the transcript; the γ-phosphate of the transcript is removed by the triphosphatase and the β- and γ-phosphates of GTP leave as pyrophosphate. Label the transcript with $[\beta\text{-}{}^{32}\mathrm{P}]$ (by initiating with $[\beta\text{-}{}^{32}\mathrm{P}]$GTP or ATP): in the actual pathway the label is retained in the cap, whereas in a GDP-transfer pathway acting on a $5'$-monophosphate end the β-phosphate of the transcript would have been removed and the label would be lost. Conversely, $[\beta\text{-}{}^{32}\mathrm{P}]$GTP as capping donor labels the cap only in the GDP-transfer scheme; in the actual pathway the label leaves as $\mathrm{PP_i}$. Furuichi and colleagues used this logic with $\mathrm{ppGpC}$ and $\mathrm{pppGpC}$ substrates.

2. An mRNA made in vitro with a cap analog that lacks the N7-methyl group is injected into a cell. Predict its stability and translation compared with a normally capped mRNA, and explain why vaccine mRNAs are made with cap-1 analogs rather than cap 0.

   **Answer** An unmethylated $\mathrm{GpppN}$ end still protects the RNA from $5'$ exonucleases that require a $5'$-monophosphate, so the RNA is more stable than a triphosphate RNA, but eIF4E binds unmethylated caps very weakly because the cation–π stacking requires the positive charge of $\mathrm{m^7G}$; the mRNA is therefore poorly translated (in cells it may also be methylated by cytoplasmic enzymes or decapped by DXO, which removes incomplete caps). Cap 0 is recognized by eIF4E, but it is also recognized as non-self by IFIT1 and RIG-I, which inhibit translation and trigger interferon responses; $2'$-O-methylation of the first nucleotide (cap 1) avoids this recognition, so cap-1 mRNAs are translated better and are less inflammatory.

3. Using Formula 17.2.1, compute the mean time to complete a tail with $k_{\mathrm{i}} = 0.02\,\mathrm{s^{-1}}$ and $k_{\mathrm{e}} = 2\,\mathrm{s^{-1}}$. What fraction of this time is spent in the initiation phase, and why are tails of intermediate length (say $50$–$200$ A) rare in a time course?

   **Answer** The mean is $10/0.02 + 240/2 = 500 + 120 = 620\,\mathrm{s} \approx 10\,\mathrm{min}$, of which $500/620 \approx 81\,\%$ is spent adding the first ten residues. The elongation phase lasts on average only $2\,\mathrm{min}$ and its duration varies little relative to its mean (240 sequential steps; the coefficient of variation of a sum of $n$ equal exponential steps is $1/\sqrt n \approx 0.065$), whereas molecules enter it at widely different times. At any time only the small fraction of molecules that entered elongation within the past $2\,\mathrm{min}$ are of intermediate length; the rest are either still in the slow phase (short tails) or complete. The distribution is therefore bimodal.

4. In a cell line, a 20-fold increase in CstF64 is found to shorten the $3'$ UTRs of many mRNAs. Explain the mechanism and predict the effect on mRNAs that are targets of microRNAs whose sites lie in the distal part of the $3'$ UTR.

   **Answer** CstF64 binds the downstream elements of poly(A) signals and stabilizes CPSF binding. Proximal poly(A) sites in $3'$ UTRs are often weaker (non-canonical hexamers, weak downstream elements) than distal ones; because they are transcribed first, raising the concentration of a limiting factor increases the chance that the proximal site is recognized and cleaved before the polymerase reaches the distal site, a kinetic competition like that of Eq. (16.2). Shorter $3'$ UTRs lack the distal microRNA sites and destabilizing elements, so these mRNAs escape repression: their levels and translation increase, typically by up to a few-fold, which is one way in which proliferating and cancer cells raise the expression of growth-promoting genes.

5. Using Eq. (17.2), estimate the catch-up distance when Pol II continues at $2\,\mathrm{kb\,min^{-1}}$ after the poly(A) site and when PP1 slows it to $0.5\,\mathrm{kb\,min^{-1}}$, with $\tau = 0.5\,\mathrm{min}$ and $u = 5\,\mathrm{kb\,min^{-1}}$. What happens in cells depleted of Xrn2, and why does read-through transcription matter for neighboring genes?

   **Answer** At $v = 2$: $x^* = 2 \times 0.5 \times 5/3 \approx 1.7\,\mathrm{kb}$. At $v = 0.5$: $x^* = 0.5 \times 0.5 \times 5/4.5 \approx 0.28\,\mathrm{kb}$, about six times shorter. Without Xrn2 the polymerase is not caught; termination then depends on slower, less efficient mechanisms, and polymerases travel many kilobases further. Read-through polymerases can transcribe into downstream genes, interfering with their promoters (transcriptional interference), and on the opposite strand they can produce antisense RNA; in compact genomes, as in yeast, efficient termination is essential to keep neighboring genes independent.

6. *E. coli* mutants lacking RNase III are viable, although they accumulate the 30S rRNA precursor. What does this suggest about the requirement for RNase III cleavage in ribosome assembly? What would you predict for a mutant lacking the RNA subunit of RNase P?

   **Answer** Viability shows that the RNase III cuts are not essential: other nucleases (RNase E, RNase G and exonucleases) can process the precursor by alternative routes, slowly, and ribosome subunits can assemble on unprocessed or partially processed rRNA, with the final trimming of the mature ends occurring during or after assembly. The phenotype is slow growth. RNase P, in contrast, is the only enzyme that makes the mature $5'$ ends of all tRNAs; tRNAs with $5'$ leaders cannot be aminoacylated efficiently or used in translation. A mutant lacking M1 RNA is therefore inviable, and the gene (*rnpB*) is essential; temperature-sensitive mutants accumulate tRNA precursors at the restrictive temperature.

7. In trypanosome mitochondria, a gRNA has the sequence (written $3' \to 5'$ under the mRNA) $\mathrm{\ldots CAGGAAACUA\ldots}$ opposite an mRNA region $5'$-$\mathrm{\ldots GUCC\,|\,GAU\ldots}$-$3'$, where $|$ is the cleavage site and the bases flanking it are paired. How many U residues will be inserted, and what is the edited sequence? Why must editing proceed $3' \to 5'$?

   **Answer** The gRNA residues $\mathrm{CAGG}$ pair with mRNA $\mathrm{GUCC}$, and $\mathrm{CUA}$ with $\mathrm{GAU}$; between them the guide has $\mathrm{AAA}$ with no partner in the mRNA. The editosome cuts at $|$, TUTase adds three U residues to the upstream fragment, which pair with the three A residues, and ligase joins the pieces: the edited mRNA reads $5'$-$\mathrm{GUCCUUUGAU}$-$3'$. Editing proceeds $3' \to 5'$ because each gRNA's $5'$ anchor must pair with mRNA sequence that already has its final form; the anchor of the next gRNA pairs with the sequence just created by the previous one, located upstream ($5'$) of the anchor of the first, so each round of editing creates the binding site for the next.

8. A mouse is engineered so that the GluA2 gene encodes arginine at the Q/R site in its DNA and the editing site is removed. The mouse is viable even without ADAR2. Is RNA editing at this site then necessary? Discuss what this experiment says about why editing exists, rather than the arginine codon being encoded in the genome.

   **Answer** In this engineered mouse, editing at the Q/R site is unnecessary: the phenotype of ADAR2 deficiency is entirely due to the lack of arginine at this one position, and genomic encoding of arginine suffices. The experiment shows that editing is not required for the function of the edited protein. Why editing persists is an evolutionary question: possible reasons include regulation (editing levels differ between cell types and stages for many sites, although not for Q/R, which is near 100 % edited in adults and lower in development), historical contingency (an editing system that edits many sites can maintain an essential edit once the genomic G has mutated to A, because selection no longer acts on the DNA), and the editing system's other roles (ADAR1 marking self RNA). Mice with genomic arginine are viable but show subtle differences, so editing might also allow fine control in some cells.
