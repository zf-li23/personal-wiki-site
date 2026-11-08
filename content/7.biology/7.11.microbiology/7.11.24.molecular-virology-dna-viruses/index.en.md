---
title: "Molecular Virology I: Genomes, Genetics and DNA Viruses"
---

A virus particle is a device for delivering a genome, and everything a virus does after delivery follows from what that genome is made of. The general anatomy of virions, the steps of the infectious cycle and the logic of the [Baltimore system](/7.11.22) were set out earlier; here we open the genome itself. Two questions organize the chapter. First, how is information packed into nucleic acid molecules that are often a thousand times smaller than the genome of the cell they parasitize, and how do we manipulate that information experimentally? Second, how are DNA genomes copied and read out — how a virus primes synthesis at the ends of its chromosome, how it times transcription so that structural proteins appear only when there are genomes to package, and how it persists for the life of the cell. The strategies of viruses whose genomes are RNA, or that pass through RNA on the way to DNA, are the subject of the [next chapter](/7.11.25).

DNA viruses are also the system in which much of eukaryotic molecular biology was discovered. Origin-dependent DNA replication in a test tube, the cellular replication machinery, RNA splicing, enhancers and the first virus-encoded microRNAs all came out of work on small DNA viruses, because their genomes are tractable where a human chromosome is not.

## 24.1. The Information in a Viral Genome

Viral genomes exhibit almost every chemical arrangement that nucleic acid permits: DNA or RNA; single- or double-stranded; linear, circular or segmented; gapped; of positive, negative or ambisense polarity; with protein or RNA covalently attached to an end. No cellular lineage shows anything like this variety, because a cell must replicate its genome with one machine, whereas each virus lineage is free to encode its own.

**Remark 24.1.1** Two constraints apply to every genome. It must be copied faithfully from end to end, with no loss of terminal sequence, and it must be converted into mRNA that host ribosomes can read. All viruses are parasites of the translation apparatus: no viral genome encodes a ribosome.

![Architectures of DNA virus genomes. Polyomaviruses have a circular double-stranded minichromosome with a single origin; adenoviruses a linear duplex with inverted terminal repeats and a terminal protein on each 5′ end; herpesviruses a large linear duplex with internal and terminal repeats and three origins; poxviruses a linear duplex whose strands are joined by terminal hairpin loops; parvoviruses a linear single strand whose palindromic ends fold into T-shaped hairpins; hepadnaviruses a gapped circle held together by overlapping 5′ ends, with the polymerase on the (−) strand and a capped RNA on the (+) strand.](./plots/genome-architecture.py)

Size spans six orders of magnitude. The smallest non-defective animal virus genomes are the circular single strands of the *Circoviridae* (1.7–2.2 kb) and *Anelloviridae* (2–4 kb); the largest known is the 2.5 Mbp DNA of *Pandoravirus salinus*, which exceeds the gene content of some free-living bacteria. The largest RNA genomes, the 27–31 kb molecules of coronaviruses and the 41 kb of a nidovirus of planarians, are smaller by a factor of sixty, a difference traced in §25.1 to the fidelity of the copying enzymes. Nothing suggests that one size is better than another; each has evolved under relentless selection and each must pay for itself.

**Remark 24.1.2** The penalty for a large genome is a large and stable particle that must nevertheless come apart to release its contents. The particle that carries the 152 kbp genome of herpes simplex virus is built from more than thirty different viral proteins, distributed between the capsid, the tegument and the envelope. The giant viruses escape the geometric limit partly by abandoning strict icosahedral symmetry: the pandoravirus particle is an ovoid roughly 1 μm long.

The ends of linear genomes are where the special structures live, because ends are where replication and packaging fail if nothing is done (§24.3): inverted terminal repeats, covalently attached terminal proteins, palindromes that fold into hairpins, cohesive single-stranded extensions, tandem repeats.

### 24.1.1. Coding strategies

"One gene, one mRNA" is false for most viruses. Compression devices operate at every level of expression, and in general the smaller the genome, the more of them are used at once.

| Level | Device | Examples |
|---|---|---|
| Genome | Overlapping reading frames; information on both strands | hepadnaviruses (more than half the genome read in two frames); polyomaviruses; adenoviruses |
| Transcription | Multiple promoters; nested 3′-coterminal mRNAs | herpesviruses; poxviruses; coronaviruses |
| RNA processing | Alternative splicing; choice among poly(A) sites | adenoviruses, polyomaviruses, papillomaviruses, retroviruses, influenza virus |
| Translation initiation | Leaky scanning; internal ribosome entry; reinitiation | polyomaviruses; picornaviruses; influenza virus |
| Translation elongation | Ribosomal frameshifting; readthrough of a stop codon | coronaviruses, retroviruses; alphaviruses |
| Post-translation | Polyprotein cleaved by viral proteases | picornaviruses, flaviviruses, retroviruses |

**Example 24.1.1** Hepatitis B virus encodes the polymerase, core, surface and X proteins in 3.2 kb by reading the same nucleotides in two frames and by starting the surface protein at three in-frame initiation codons. Any mutation is therefore likely to alter two proteins at once, which constrains the virus and complicates genetic analysis.

:::

A genome sequence, however, is only a parts list. It predicts proteins; it says very little about how the virus interacts with a cell, a host or a population. Metagenomic surveys return enormous numbers of viral sequences whose hosts are unknown and which cannot yet be studied at all — more than 93% of the genes of *Pandoravirus salinus* resemble nothing known.

## 24.2. Viral Genetics and Reverse Genetics

### 24.2.1. Classical genetics

Animal virus genetics began with the plaque assay (Dulbecco, 1952), which made clonal virus stocks and quantitative scoring possible. Mutants were obtained by chemical mutagenesis and selected by phenotype: temperature sensitivity (replication at 33 °C but not at 39 °C), altered plaque size, drug resistance, antibody escape, host range. Two tests then assign function.

**Definition 24.2.1 (Complementation and recombination)** In a cell coinfected with two mutants, complementation is the restoration of growth because each genome supplies the product the other lacks; the progeny remain mutant. Recombination and, for segmented genomes, reassortment produce genomes that are themselves wild type. Mutations that fail to complement define one complementation group, in principle one gene.

**Example 24.2.1** Because the eight segments of an influenza virus genome migrate differently in a polyacrylamide gel, the parental origin of every segment of a reassortant could be read directly from a gel, and a phenotype assigned to a segment, long before sequencing was routine. This is the laboratory version of the process that produces pandemic viruses in nature (§25.9).

### 24.2.2. Infectious clones

**Definition 24.2.2** An *infectious clone* is a double-stranded DNA copy of a viral genome, carried on a plasmid or other vector, from which infectious virus can be recovered after introduction into susceptible cells. Starting from such a clone, any mutation can be designed, built and tested — the approach called reverse genetics, in contrast to classical genetics, which starts from a phenotype and searches for the lesion.

![Reverse genetics for the three classes of RNA genome. (A) A cloned cDNA of poliovirus RNA is transfected directly, or transcribed in vitro from a bacteriophage T7 promoter and the RNA transfected; either way the (+) strand genome starts an infectious cycle. (B) Influenza virus is recovered from eight plasmids, in each of which one segment lies between an RNA polymerase I promoter and terminator, which make the (−) strand vRNA, and an RNA polymerase II promoter and poly(A) signal, which make the mRNA. (C) A virus with a nonsegmented (−) strand genome is rescued from a plasmid encoding a full-length (+) strand antigenome together with plasmids for the nucleoprotein, phosphoprotein and polymerase; the T7 polymerase is supplied by a helper virus or a stable cell line.](./plots/reverse-genetics.py)

The first infectious clone of an animal virus was made in 1981: cloned poliovirus cDNA, transfected into mammalian cells, yielded infectious virus, demonstrating that the information of an RNA virus survives passage through DNA and bacteria. Deproteinized DNA of polyoma-, papilloma- and adenoviruses is infectious on its own; the much larger herpesvirus and poxvirus genomes are carried in cosmids or bacterial artificial chromosomes, and poxvirus DNA additionally requires helper-supplied early transcription proteins because its promoters are unreadable by cellular RNA polymerase. The genomes of (−) strand and double-stranded RNA viruses are not infectious, since they can be neither translated nor copied by the cell; they are rescued by supplying the viral replication proteins from co-transfected plasmids, an advance that opened genetics for the rhabdoviruses, paramyxoviruses, orthomyxoviruses and reoviruses in the 1990s and 2000s. The eight-plasmid influenza system (2000) and the ten-plasmid reovirus system (2007) are the standard tools.

**Example 24.2.2** Reverse genetics systems for SARS-CoV-2 were reported within weeks of the release of the genome sequence in 2020, assembled from synthetic DNA fragments in yeast or by in vitro ligation and launched from a bacteriophage T7 promoter. They were used immediately to build reporter viruses for drug screening and to test the phenotypes of variant spike substitutions.

### 24.2.3. Dual-use research

**Reverse genetics** also makes it possible to resurrect a virus from sequence alone. The genome of the 1918 pandemic influenza virus was recovered piecewise from fixed autopsy material and from a victim buried in permafrost, and in 2005 the complete virus was reconstructed and shown to be highly virulent in mice; the work established that the 1918 haemagglutinin and the polymerase genes together account for much of that virulence. Experiments of this kind are the standard example of *dual-use research of concern*: the same result that explains a past pandemic also describes how to make a dangerous agent. The practical consequences — containment levels, institutional review of gain-of-function proposals, restraint in publishing enabling detail, and surveillance of synthetic DNA orders — belong with the public-health material in [7.11.35](/7.11.35), but they are a part of molecular virology and not an appendix to it.

## 24.3. Replicating a DNA Genome

All DNA synthesis obeys the same rules: stepwise addition of deoxynucleoside monophosphates to a free 3′-OH, semiconservative copying, initiation at origins, and — the rule that generates all the interesting virology — no DNA polymerase can start a chain de novo. Every viral DNA genome therefore needs a primer, and every linear viral DNA genome needs a solution to the problem that removing the last primer leaves a gap. Chromosomes solve it with telomeres and telomerase; viruses have found at least four other solutions.

**Remark 24.3.1** Duplex DNA is made in one of only two geometries: both strands copied at a replication fork (papilloma-, polyoma- and herpesviruses, and integrated proviruses), or one strand copied continuously while its complement is displaced (adeno-, parvo- and poxviruses). Fork synthesis always starts from an RNA primer; strand-displacement synthesis never does.

![Four solutions to priming and to the end of a linear genome. (A) RNA priming at an internal origin: a primase lays down RNA, both strands are copied at two forks, and the circular genome has no ends to lose (simian virus 40). (B) Protein priming: the adenovirus preterminal protein receives dCMP on a serine hydroxyl from the viral polymerase, and the protein-linked nucleotide primes continuous synthesis from each end, displacing the other strand, which re-forms a duplex origin by annealing of its inverted terminal repeats. (C) Self-priming: the palindromic end of a parvovirus genome folds into a T-shaped hairpin whose 3′-OH primes synthesis; the viral Rep protein nicks the terminal resolution site to allow the end to be copied. (D) Rolling-circle synthesis: a nick in one strand of a circle provides a 3′-OH, the circle is copied repeatedly, and the displaced strand becomes a head-to-tail concatemer that is later cut into genome-length units during packaging.](./plots/priming-solutions.py)

### 24.3.1. Simian virus 40: the cellular machine, borrowed

The 5.2 kbp circular genome of simian virus 40 is replicated almost entirely by cellular proteins. The single viral contribution is large T antigen (LT), which binds pentanucleotide repeats in the 64 bp core origin as two hexamers, distorts the flanking AT-rich element and the early palindrome, and then acts as the replicative 3′→5′ helicase, unwinding the origin together with the single-stranded-DNA-binding protein Rp-A. Polymerase α-primase lays down the primers, Rf-C loads the sliding clamp Pcna, polymerases δ and ε elongate, RNase H and Fen1 remove primers, ligase I seals, and topoisomerases I and II relieve torsional stress and decatenate the daughter circles. The genome is a minichromosome wrapped in cellular nucleosomes, so chromatin must be traversed and reassembled as well.

**Remark 24.3.2** This system, reconstituted in vitro in the 1980s, is how most cellular replication proteins were identified. Mammalian origins are diffuse and difficult to define; the compact viral origin provided the defined substrate that cellular genetics could not.

Papillomaviruses use the same host machinery but need two viral proteins: E1, the helicase, binds the origin with low specificity unless loaded there by the sequence-specific transcriptional regulator E2. Herpesviruses, in contrast, encode their own replication machine — an origin-binding protein (UL9), a two-subunit polymerase with its own processivity factor, a helicase–primase of three subunits and a single-stranded-DNA-binding protein — and run it on three origins (two copies of OriS, one of OriL). Late in infection, herpesvirus replication becomes origin-independent and produces branched concatemers, which are cleaved to unit length as DNA is pumped into preformed capsids.

### 24.3.2. Priming without RNA

In protein priming, used by adenoviruses, by the bacteriophages φ29 and PRD1, and (on an RNA template) by hepadnaviruses and picornaviruses, the viral polymerase links the first dNMP to a serine or tyrosine hydroxyl of a protein. The adenovirus preterminal protein receives dCMP and primes continuous synthesis from each of the two identical origins at the ends of the genome; displaced single strands anneal their inverted terminal repeats into a duplex origin and are copied in a second round. The mature terminal protein left on each 5′ end raises the specific infectivity of the genome by two orders of magnitude, because it helps assemble initiation complexes.

In self-priming, the terminal palindromes of a parvovirus genome fold into a T-shaped hairpin that provides a 3′-OH. Continuous synthesis to the far end produces a duplex in which parental and daughter strands are covalently joined; the Rep 78/68 protein, a site- and strand-specific endonuclease, nicks the terminal resolution site to free a new 3′ end and allow the hairpin sequence itself to be copied. Poxvirus genomes, whose two strands are joined by terminal hairpin loops, use a related nicking and self-priming scheme, though the detailed mechanism of vaccinia virus DNA synthesis is still debated; replication takes place in cytoplasmic factories and, uniquely among animal viruses, uses an entirely virus-encoded enzyme set.

Rolling-circle synthesis, discovered in bacteriophage φX174, converts a nicked circle into a concatemer. Several bacteriophages and the late phase of herpesvirus replication make concatemeric DNA, and the terminase that packages such DNA both measures and cuts it.

### 24.3.3. Fidelity

Viral DNA polymerases, like cellular ones, carry 3′→5′ proofreading exonucleases, and remaining errors are accessible to cellular mismatch repair; mutation rates of large DNA viruses are of the order of $10^{-8}$ per base per round, comparable to those of their hosts and some $10^4$-fold below the rates of RNA viruses (§25.2). Diversity in DNA viruses therefore comes less from misincorporation than from recombination, which is frequent in herpesvirus and poxvirus infections and is in any case mechanistically bound up with their replication.

## 24.4. Small DNA Viruses and the Cell Cycle

A virus that borrows the cellular replication machine can only replicate in a cell that has one. Most cells a virus meets are quiescent, with low concentrations of deoxynucleotides and of replication proteins. Small DNA viruses therefore force the cell into S phase, and they do it by attacking the two controls that normally forbid it: the retinoblastoma protein, which restrains E2F transcription factors, and p53, which arrests or kills a cell whose DNA is being replicated inappropriately.

![How small DNA viruses push a quiescent cell into S phase. Simian virus 40 large T antigen, adenovirus E1A and papillomavirus E7 all bind the retinoblastoma protein and release E2F, which activates the genes of S phase; large T antigen, adenovirus E1B-55K (with E4orf6) and papillomavirus E6 inactivate or degrade p53, so the resulting replication stress does not trigger arrest or apoptosis. The cell enters S phase, deoxynucleotides and replication proteins accumulate, and the viral genome is replicated; in the absence of a complete productive cycle, the same two lesions are the first steps of transformation.](./plots/s-phase-push.py)

**Example 24.4.1** In human papillomavirus types associated with cervical carcinoma, E7 binds Rb and E6 recruits a cellular ubiquitin ligase that degrades p53. In the normal life of the virus these activities keep differentiating keratinocytes replication-competent, which is where viral genomes are amplified. Integration of the viral DNA into a host chromosome, which is not part of the productive cycle, usually disrupts the E2 gene; loss of E2 repression raises E6 and E7 expression and is a step towards cancer. The cell-biological consequences are those of [7.3.20](/7.3.20) and [7.3.26](/7.3.26) and are not repeated here; tumour viruses as a class return in [7.11.27](/7.11.27).

:::

Not every infection ends in lysis, and viruses that persist must replicate their genomes in step with the cell rather than exponentially. Epstein–Barr virus maintains its episome at a few copies per cell using OriP and the viral protein EBNA-1, which tethers the genome to mitotic chromosomes so that both daughter cells inherit it, and replicates it once per cell cycle with cellular enzymes. Papillomaviruses run three programmes from one genome: establishment, maintenance at 50–100 copies in basal cells, and amplification to thousands of copies in differentiated cells where particles are made.

## 24.5. Transcription: Cascades and Activators

With the exception of the poxviruses, DNA viruses that replicate in the nucleus have their genes transcribed by cellular RNA polymerase II, and their promoters and enhancers are built from binding sites for cellular factors. What the virus adds is timing.

**Definition 24.5.1** The genes of a DNA virus are expressed as a *transcriptional cascade*: *immediate-early* genes, transcribed by the incoming genome using only cellular factors (or a protein carried in the particle), encode regulators; *early* genes encode the replication machinery and proteins that modify the host; *late* genes, which require genome replication, encode structural proteins. The dependence of late transcription on replication couples the supply of capsids to the supply of genomes.

![The transcriptional cascade. (A) Timelines for simian virus 40, human adenovirus and herpes simplex virus 1, marking the onset of viral DNA synthesis and the regulators that drive each transition: large T antigen for the two-phase polyomavirus programme; E1A then the E2 products and the IVa2–major late switch for adenovirus; the virion protein VP16, then ICP4 and ICP0, for the three-phase herpesvirus programme. (B) A minimal kinetic model of the same logic: an immediate-early regulator activates early proteins, early proteins replicate the genome, and the template number multiplied by the late promoter's dependence on replication sets late protein synthesis; the simulation reproduces the observed order and the sharp late burst.](./plots/transcription-cascade.py)

The three best-studied programmes illustrate how little the strategies have in common mechanistically. Simian virus 40 has one early and one late transcription unit; synthesis of large T antigen inevitably leads to the late phase, since the same protein starts DNA synthesis and activates late transcription. Adenovirus expresses the immediate-early E1A proteins first; they activate all early units, including E2, which encodes the replication proteins, while accumulation of progeny genomes relieves repression of the IVa2 gene and switches on the major late promoter. Herpes simplex virus 1 carries its first activator in the particle: VP16, a tegument protein, has one of the strongest known acidic activation domains but cannot bind DNA, and reaches immediate-early promoters only through the cellular proteins Oct-1 and HCF-1. The immediate-early products ICP4 and ICP0 then drive early and late transcription and repress their own.

**Remark 24.5.1** Viral activators that do not themselves bind DNA were a surprise when they were found, and they were the first clear evidence that cells contain coactivators — proteins that regulate transcription by contacting other proteins. Adenovirus E1A, which binds Rb, p300/CBP and components of the mediator and chromatin machinery but no specific DNA sequence, remains a standard probe of these complexes.

Poxviruses, replicating in the cytoplasm, must bring everything: a multisubunit DNA-dependent RNA polymerase, capping and polyadenylation enzymes, and stage-specific transcription factors, with early transcription occurring inside the partly uncoated core and intermediate and late stages following genome replication. Many viruses also shut off host gene expression — the herpesvirus virion host shutoff protein degrades cellular mRNA, poxviruses decap it — which both frees the translation apparatus and blunts innate responses.

## 24.6. Making Many mRNAs from One Genome

### 24.6.1. The discovery of splicing

In 1977 two groups, studying how adenovirus late mRNAs are made, hybridized them to viral DNA and looked at the hybrids in the electron microscope. The 5′ ends of several different mRNAs did not pair with the DNA adjacent to their coding sequences; instead, three short segments from three widely separated positions in the genome were joined to the body of each mRNA. The same 11-nucleotide capped 5′ sequence had already been found on several late mRNAs. The conclusion — that an mRNA can be assembled from noncontiguous pieces of a transcription unit — was immediately shown to apply to cellular genes as well, and the discovery was recognized by the Nobel Prize in Physiology or Medicine in 1993. The mechanism and the spliceosome belong to [7.2.16](/7.2.16); the point here is that viruses provided the substrate in which a universal feature of eukaryotic gene expression was visible.

![Alternative processing of adenovirus pre-mRNA. The major late transcription unit is a single promoter whose primary transcript carries the tripartite leader and extends over most of the genome; choice among five poly(A) sites and among the 3′ splice sites within each family yields about twenty mRNAs, each with the same leader and a different body. Below, the immediate-early E1A transcription unit produces the 13S, 12S and 9S mRNAs by alternative 5′ splice-site choice within one coding sequence, so that one gene makes proteins with different regulatory functions.](./plots/adenovirus-splicing.py)

### 24.6.2. Alternative processing

Choice among splice sites and among poly(A) sites is the main way nuclear DNA viruses expand their coding capacity and regulate the ratio of their products. The adenovirus major late unit yields about twenty mRNAs from one promoter. The E1A unit yields the 13S and 12S mRNAs, whose products share most of their sequence but differ in the ability to activate transcription. Polyomaviruses make large and small T antigens from one early unit; papillomaviruses and retroviruses depend on alternative splicing throughout. Because splicing is a cellular process — no viral genome encodes a spliceosome — the pattern of mRNAs a virus makes can depend on the differentiation state of the cell, which is one mechanism of tissue tropism.

### 24.6.3. Small RNAs and modified RNA

Viral genomes also encode microRNAs, first found in 2004 in cells latently infected with Epstein–Barr virus. They are attractive regulators for a virus: they occupy almost no coding space and, unlike proteins, present no peptides for cytotoxic T cells to recognize. Polyomaviruses encode a single pre-miRNA, processed into two miRNAs, that cleaves the mRNA for large T antigen; limiting the concentration of this protein restrains genome replication and reduces killing of infected cells by T cells specific for large T antigen, and appears to help the archetype BK virus establish persistent infection of the urinary tract. Herpesviruses encode many more. About a dozen miRNAs are made in cells latently infected by human herpesvirus 8 (Kaposi's sarcoma-associated herpesvirus), processed from transcripts of the latency promoters, and they lower the concentrations of cellular mRNAs for proteins of cell-cycle control, apoptosis and immune signalling, including the cyclin-dependent kinase inhibitor p21. Cellular miRNAs act in both directions: miRNA-155 is induced by Epstein–Barr virus and contributes to B-cell proliferation, whereas the hepatocyte-specific miRNA-122 binds the 5′ end of the hepatitis C virus genome and is required for its replication, which is the basis of an antisense therapeutic strategy. The general biology of microRNAs is in [7.2.18](/7.2.18).

Viral RNAs also carry the same covalent modifications as cellular RNAs. N⁶-methyladenosine marks are deposited on the transcripts of herpesviruses, on the genomes of flaviviruses such as Zika virus, and on retroviral RNA, and they change RNA stability, splicing, export and recognition by innate sensors; methods and interpretation are those of [7.9.4](/7.9.4).

## 24.7. Latency and Persistence

**Definition 24.7.1** In a *latent* infection the viral genome is maintained in the cell with little or no production of progeny virus and with expression restricted to a small set of genes, and the full productive programme can be restored by *reactivation*. Latency is not the same as a slow or chronic productive infection, in which particles are made continuously.

Herpesviruses are the paradigm. Herpes simplex virus 1 persists in sensory neurons as a circular, chromatinized episome; of more than 80 genes, essentially only the latency-associated transcript is made, and the lytic promoters are packed in repressive chromatin. Stress, through pathways that include glucocorticoid signalling, reactivates the programme — one of the viral origins, OriL, is activated and the other repressed in differentiated neurons exposed to glucocorticoid, which suggests how the transition is biased. Epstein–Barr virus persists in memory B cells and runs several distinct latency programmes, each with its own set of expressed genes and its own associated malignancies, and commits to the productive cycle when the sequence-specific activator Zta is made.

A second route to persistence is integration. Retroviral proviruses and, accidentally, the genomes of papillomaviruses and of adeno-associated virus can become part of a host chromosome, where they are replicated by the cell. Integrated viral DNA is a recognized target of cellular defence: KRAB zinc-finger proteins with the corepressor TRIM28, histone methyltransferases and DNA methylation silence it, which is why retroviral vectors are prone to transcriptional silencing (§25.7) and why reactivation of an endogenous element requires loss of that repression.

Finally, the largest DNA viruses blur the line this chapter has drawn. The giant viruses of amoebae encode translation factors, aminoacyl-tRNA synthetases and metabolic enzymes, and replicate in cytoplasmic factories that resemble a nucleus; they carry their own satellite viruses. Their biology and the taxonomic and evolutionary arguments they have provoked belong to [7.11.26](/7.11.26).

## Summary

- A viral genome can be DNA or RNA, single- or double-stranded, linear, circular, segmented or gapped, and the arrangement dictates the route to mRNA. Two requirements are universal: complete copying and production of translatable mRNA (Remark 24.1.1).
- Coding capacity is expanded by overlapping frames, multiple promoters, alternative splicing and polyadenylation, leaky scanning, frameshifting, readthrough and polyprotein processing; the smaller the genome, the denser the compression (Example 24.1.1).
- Classical virus genetics rests on conditional lethal mutants, complementation and recombination or reassortment (Definition 24.2.1). Infectious clones replaced it with reverse genetics (Definition 24.2.2), available now for every class of genome, including rescue of (−) strand and double-stranded RNA viruses from plasmids. The same technology reconstructed the 1918 influenza virus and raised the problem of dual-use research.
- No DNA polymerase starts de novo, so each DNA virus solves priming and the end problem: RNA primers at internal origins on circular genomes, protein priming with strand displacement, self-priming hairpins with terminal resolution, or rolling-circle synthesis into concatemers (Remark 24.3.1). Simian virus 40 borrows the whole cellular machine behind one viral origin-binding helicase; herpesviruses encode their own; poxviruses encode everything and work in the cytoplasm.
- Small DNA viruses must create their own S phase, and do so by neutralizing Rb and p53 — activities that are also the first steps of transformation (Example 24.4.1).
- Transcription proceeds as an immediate-early → early → late cascade, with late expression conditional on genome replication (Definition 24.5.1); the activators may be carried in the particle (VP16), may act only through cellular proteins (E1A, VP16) or may be sequence-specific (Zta, ICP4).
- Adenovirus mRNAs revealed splicing (1977; Nobel Prize 1993). Alternative splicing and poly(A) site choice, virus-encoded miRNAs and m⁶A modification all tune the output of a compact genome.
- Latency (Definition 24.7.1) maintains the genome as a silenced episome or an integrated, epigenetically repressed provirus, with reactivation restoring the productive programme.

## Questions

1. A linear double-stranded DNA genome is replicated at a fork from an internal RNA primer. Show that this cannot by itself produce a complete copy, and state two different ways viruses avoid the problem.

   **Answer** Removal of the RNA primer at the 5′ end of each lagging strand leaves a gap that no DNA polymerase can fill, because there is no upstream 3′-OH; each round would shorten the genome. Viruses avoid it by not having ends (circular genomes, or circularization before replication), by priming at the ends with a protein (adenovirus pre-terminal protein) or a hairpin (parvoviruses) and displacing the other strand, by joining the strands with terminal hairpin loops (poxviruses), or by making concatemers (rolling circle, recombination) from which unit-length genomes are cut during packaging.

2. Why is the genome of a (−) strand RNA virus not infectious when transfected into cells, whereas the DNA of a polyomavirus and the RNA of poliovirus are? What does the answer imply for the design of reverse genetics systems?

   **Answer** A (+) strand RNA genome is itself mRNA and is translated on arrival, producing the polymerase; polyomavirus DNA is transcribed by cellular RNA polymerase II. A (−) strand genome can neither be translated nor copied by any cellular enzyme, and in the particle it exists only as a nucleoprotein with the polymerase bound. Rescue therefore requires that the cell be supplied simultaneously with a full-length (+) strand antigenome and with plasmids expressing the nucleoprotein, the phosphoprotein and the large polymerase subunit, so that an authentic nucleocapsid can assemble.

3. Adenovirus E1A binds no specific DNA sequence, yet it is required for transcription of all the early genes. How can a protein activate transcription without binding DNA, and what did this teach cell biologists?

   **Answer** E1A is recruited to promoters by interacting with cellular DNA-binding proteins and coactivators, and it liberates E2F by binding Rb, so the cellular factors already assembled at viral and cellular promoters become active. The existence of such viral regulators was the first strong evidence that cells themselves contain coactivators and corepressors that work entirely through protein–protein contacts, a class of proteins now central to the understanding of transcription.

4. A mutant simian virus 40 whose pre-miRNA hairpin is disrupted (without changing the overlapping protein-coding sequence) replicates normally in cultured cells. Why might this result be misleading about the function of a viral miRNA, and what experiment would test the alternative?

   **Answer** The miRNA limits the concentration of large T antigen; its advantage is not faster growth but lower antigen load and so less killing of the infected cell by cytotoxic T lymphocytes, plus restrained replication during establishment of persistence — neither is scored by yield in a permissive cell line. One tests it in the relevant context: infect primary cells of the natural target tissue with the archetype virus rather than a laboratory-adapted variant and measure early protein, genome copies and yield over time, and measure the susceptibility of infected cells to T cells specific for the early protein. Such experiments with BK virus in primary renal epithelial cells show the predicted effect, which the laboratory-adapted strains conceal.

5. Explain why late gene expression in DNA viruses is generally made dependent on genome replication, and give two different molecular implementations of this dependence.

   **Answer** Structural proteins are needed in large amounts and only when there are genomes to package; making them early would waste resources, and empty or prematurely filled capsids would be assembled. Implementations: in simian virus 40 the same protein, large T antigen, initiates DNA synthesis and activates the late promoter, so the two are coupled through one regulator; in adenovirus the accumulation of progeny genomes relieves repression of the IVa2 gene and only then is the major late promoter fully active, so the template number itself is the signal. In herpesviruses, true late promoters are simply inactive on the parental genome and are transcribed only from newly replicated, less chromatinized DNA.
