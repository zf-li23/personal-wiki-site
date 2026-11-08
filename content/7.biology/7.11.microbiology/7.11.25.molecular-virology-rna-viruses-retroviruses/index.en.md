---
title: "Molecular Virology II: RNA Viruses and Retroviruses"
---

Cells have no enzyme that copies RNA into RNA. Every virus with an RNA genome must therefore bring or encode one of only two solutions: an RNA-dependent RNA polymerase, or a reverse transcriptase that converts the genome into DNA and hands it to the cell. Everything characteristic of RNA viruses follows from that single fact — their small genomes, their enormous mutation rates, their membranous replication organelles, their capacity to exchange segments and to jump between host species, and the difficulty of making durable vaccines and drugs against them. This chapter treats the three Baltimore classes that copy RNA with RNA (double-stranded, positive-strand and negative-strand genomes, the last including the ambisense viruses) and the two that pass through reverse transcription (retroviruses and hepadnaviruses). The structure of virions, the steps of entry and release, and the classification scheme itself were covered in [7.11.22](/7.11.22); the genetics and the DNA viruses in [7.11.24](/7.11.24).

## 25.1. The Enzyme the Cell Does Not Have

**Definition 25.1.1 (RNA-dependent RNA polymerase)** An *RNA-dependent RNA polymerase* (RdRp) synthesizes RNA on an RNA template. It is encoded by every RNA virus except the retroviruses, and it is carried inside the particle by every virus whose genome cannot be translated on entry.

Viral RdRps were found in the early 1960s as activities in extracts of cells infected with poliovirus or mengovirus that incorporated nucleotides into RNA in the presence of actinomycin D, which blocks all DNA-dependent synthesis. Enzymes of the same kind were then shown to be present inside the particles of negative-strand and double-stranded RNA viruses.

All four classes of nucleic acid polymerase share a catalytic core shaped like a right hand, with the active site in the palm, and a two-metal mechanism in which two conserved aspartates coordinate the magnesium ions. RdRps are distinguished by a closed structure in which fingers and thumb meet above the active site, creating separate tunnels for template entry, nucleotide entry and product exit, and by motif F, which lines the nucleotide tunnel. Motif C carries the Gly-Asp-Asp signature of most positive-strand virus polymerases (Gly-Asp-Asn in nonsegmented negative-strand viruses, Ser-Asp-Asp in influenza virus), and the conserved aspartate of motif A hydrogen bonds to the 2′-OH of the incoming nucleotide, which is how these enzymes select ribonucleotides over deoxyribonucleotides.

![Four ways of starting an RNA chain. (A) De novo initiation: the first two nucleotides are joined on a loop of the thumb domain that acts as a platform (hepatitis C virus, reovirus, bacteriophage φ6); after a short product has been made the platform swings aside and the product leaves. (B) Prime and realign: initiation at an internal residue followed by backward slippage of the nascent strand, so that the 5′ end is unpaired (bunyaviruses, arenaviruses). (C) Protein priming: the polymerase adds UMP to a tyrosine of the small protein VPg, templated by the 3′ poly(A) or by an internal cis-acting replication element, and the protein-linked dinucleotide primes synthesis (picornaviruses). (D) Cap snatching: the polymerase binds a host nuclear pre-mRNA by its cap, an endonuclease in the complex cuts 10–13 nucleotides downstream, and the capped fragment primes mRNA synthesis (influenza virus, bunyaviruses).](./plots/rdrp-initiation.py)

**Remark 25.1.1** Cap snatching solves two problems at once: it provides a primer and it provides the cap that the ribosome requires, without the virus having to encode capping enzymes. Its cost is that influenza virus mRNA synthesis must occur in the nucleus, where nascent host transcripts are available, and is therefore blocked by α-amanitin, which inhibits host RNA polymerase II. The endonuclease sits in the PA subunit of the influenza polymerase and is the target of the drug baloxavir.

The second universal property of these enzymes is that they do not proofread.

## 25.2. Quasispecies and the Error Threshold

Misincorporation frequencies for RdRps are of the order of $10^{-3}$ to $10^{-5}$ per nucleotide, some four orders of magnitude above the rate of a proofreading DNA polymerase. For a 10 kb genome and a rate of $10^{-4}$, each progeny genome carries about one new mutation.

**Definition 25.2.1 (Quasispecies)** A population of RNA virus genomes is not a set of identical sequences but a *quasispecies*: a distribution of related sequences, usually centered on a consensus that may be carried by no individual genome, maintained by mutation and selection and behaving as the unit on which selection acts.

The consequences are familiar: mutants resistant to any single antiviral drug are present in a patient before treatment begins; antibody escape variants are selected within weeks; and the attenuated poliovirus vaccine strains were isolated as spontaneous mutants from an unmutagenized stock.

Mutation cannot increase without limit. If $\mu$ is the per-base error rate and $L$ the genome length, the probability that a genome is copied without error is $\mathrm{e}^{-\mu L}$, and when the selective advantage of the best sequence no longer compensates for that loss the population drifts off the fitness peak and the information in the genome is lost. This is Eigen's error threshold, derived in [Theorem 23.6.1](/7.2.23#thm-23.6.1); the quasispecies as a cloud on a fitness landscape is discussed in [7.10.6](/7.10.6) and [7.6.41](/7.6.41), and is not re-derived here.

![The error threshold in a simple quasispecies model. A master sequence of length $L$ has fitness $1 + s$ and all mutants fitness 1; iterating the mutation–selection recursion to its steady state gives the frequency of the master sequence as a function of the genomic error rate $\mu L$. Above the threshold $\mu L \approx \ln(1+s)$ the master sequence is lost and the population delocalizes. Curves are shown for three selective advantages, with the measured range of RNA virus error rates marked; the right panel shows the inverse relation between per-base error rate and genome size across viruses and cells, with coronaviruses displaced by their proofreading exonuclease.](./plots/quasispecies.py)

**Example 25.2.1** A poliovirus with a single amino acid substitution in the fingers domain of $3\mathrm{D}^{\mathrm{pol}}$ copies RNA more accurately than the wild type. It grows normally in culture but is attenuated in mice and fails to reach the central nervous system, because the narrowed mutant cloud cannot generate the variants needed to cross tissue barriers. A substitution that raises the error rate is also deleterious. The error rate of a successful RNA virus is close to an optimum.

**Remark 25.2.1** The threshold is also a therapeutic strategy. Ribavirin is incorporated in place of any of the four nucleotides and raises the mutation rate; a single round of replication in its presence destroys more than 99% of poliovirus infectivity. Molnupiravir acts on SARS-CoV-2 by the same principle of lethal mutagenesis. Both illustrate why a virus near its error threshold is vulnerable to a small further increase, and why such drugs raise questions about mutagenesis of host nucleic acid and about the variants released from treated patients.

The one known exception among RNA viruses is instructive. The *Nidovirales* — coronaviruses and their relatives — encode in nsp14 a 3′→5′ exonuclease, ExoN. Inactivating it is not lethal but raises the mutation rate 15- to 20-fold, and viruses lacking it are attenuated. Proofreading is almost certainly what permits the 27–31 kb coronavirus genome, the largest known RNA genome, and it also degrades some nucleoside analogues; remdesivir works against SARS-CoV-2 in part because, after incorporation, it causes delayed chain termination at a position that resists excision.

## 25.3. Positive-Strand RNA Viruses

**Definition 25.3.1 (The positive-strand strategy)** In a positive-strand RNA virus the genome has the polarity of mRNA and is translated on entry into the cell; the deproteinized genome is therefore infectious. Replication proceeds in two steps, a full-length (−) strand being made first and then used as the template for many (+) strands.

The two strands are made in very unequal amounts: in poliovirus-infected cells, genomes outnumber their complements by about a hundredfold, because initiation at the 3′ end of the (−) strand template is far more efficient and because the (−) strand resides in a duplex replicative intermediate.

### 25.3.1. Poliovirus

The 7.5 kb genome carries the small protein VPg on its 5′ end, a structured 5′ untranslated region with a cloverleaf that nucleates the replication complex and an internal ribosome entry site that drives cap-independent translation, an internal cis-acting replication element in the coding region, a 3′ pseudoknot and a poly(A) tail.

**Definition 25.3.2 (Polyprotein)** The genome is translated as one long open reading frame into a *polyprotein*, which is cleaved by viral proteases, mostly $2\mathrm{A}^{\mathrm{pro}}$ and $3\mathrm{C}^{\mathrm{pro}}$/$3\mathrm{CD}^{\mathrm{pro}}$, into the structural and non-structural proteins. Because all products are made in equimolar amounts, regulation of their relative concentrations occurs through the order and rate of processing rather than through transcription.

Cleavage intermediates have their own functions: $3\mathrm{CD}^{\mathrm{pro}}$ is a protease and an RNA-binding protein that, with cellular poly(rC)-binding protein 2 and poly(A)-binding protein 1, forms a circular ribonucleoprotein that is required to start (−) strand synthesis, but it cannot polymerize RNA until it is cleaved to $3\mathrm{D}^{\mathrm{pol}}$. Uridylylation of VPg by $3\mathrm{D}^{\mathrm{pol}}$, templated by the cis-acting replication element or by the poly(A) tail, supplies the primer.

Replication occurs on membranes. Poliovirus proteins 2BC and 3A remodel the secretory pathway into clusters of single- and double-membrane vesicles with properties of autophagosomes; flaviviruses invaginate the endoplasmic reticulum into vesicles connected to the cytoplasm by a pore; coronaviruses build double-membrane vesicles and convoluted membranes continuous with the endoplasmic reticulum. These replication organelles concentrate the components, keep ribosomes and polymerases from colliding on the same template, and hide double-stranded RNA from the innate sensors of the cell ([7.11.27](/7.11.27)).

### 25.3.2. Subgenomic mRNAs and the coronaviruses

Making all proteins from one polyprotein wastes capacity when structural proteins are needed in far greater amounts than enzymes. Most positive-strand viruses therefore make smaller mRNAs as well.

**Definition 25.3.3 (Subgenomic mRNA)** A *subgenomic mRNA* is a viral mRNA shorter than the genome, made during infection from a full-length template and translated into a subset of the viral proteins — typically the structural proteins, which are required in large amounts late in infection.

In alphaviruses, an internal initiation site on the (−) strand produces one 26S subgenomic mRNA encoding the structural polyprotein, while the genome itself encodes the replicase. Successive cleavages of the alphavirus nonstructural polyprotein produce three polymerases of different template specificity, so that the processing state of one precursor acts as a clock for the switch from (−) strand to (+) strand and subgenomic synthesis.

Coronaviruses and arteriviruses — the order *Nidovirales*, from *nidus*, a nest — make a nested set of 3′-coterminal subgenomic mRNAs by a discontinuous mechanism during (−) strand synthesis. The polymerase copies the 3′ end of the genome, and at each of a set of transcription-regulating sequences it may detach and re-anneal at the complementary sequence at the 3′ end of the leader, completing a (−) strand that carries the leader; these subgenome-length (−) strands then template the mRNAs. Each mRNA is translated essentially only from its 5′-most open reading frame, so one nested set expresses a dozen genes.

![Expression of a coronavirus genome. The 5′ two-thirds of the genome is translated into polyproteins pp1a and, after a −1 ribosomal frameshift at a slippery sequence and pseudoknot, pp1ab; viral proteases cut them into sixteen non-structural proteins, among them the polymerase nsp12, the helicase nsp13 and the proofreading exonuclease nsp14. These build the double-membrane replication organelle, in which discontinuous (−) strand synthesis at the transcription-regulating sequences generates a nested set of subgenomic mRNAs for the structural and accessory proteins.](./plots/coronavirus-expression.py)

## 25.4. Negative-Strand RNA Viruses

**Definition 25.4.1 (The negative-strand strategy)** In a negative-strand RNA virus the genome is complementary to mRNA, cannot be translated, and is never naked: it is wound along its length with nucleoprotein into a helical nucleocapsid that, with the polymerase, is the actual template. The particle must therefore carry an RdRp, and the deproteinized genome is not infectious.

The nucleoprotein binds the RNA in a positively charged groove between its two lobes, keeping it single-stranded and protected; the polymerase displaces it transiently as it reads. One consequence is that replication and encapsidation are inseparable: a (+) strand antigenome exists only inside a nucleocapsid.

### 25.4.1. Nonsegmented genomes

In vesicular stomatitis virus the five genes lie in a fixed order between a 3′ leader and the 5′ end. The polymerase, one L protein with four P proteins, enters at the 3′ end and transcribes by a start–stop mechanism: it initiates at a gene start signal, elongates, polyadenylates by stuttering on a run of seven U residues in the template, terminates, and reinitiates at the next gene with about 70–80% efficiency. The product is a gradient of mRNA abundances, N > P > M > G > L, set by the gene order, and the gene order was in fact mapped by ultraviolet irradiation long before sequencing: the dose needed to abolish synthesis of an mRNA corresponds to the size of its gene plus everything 3′ of it.

Switching from transcription to replication requires the polymerase to ignore the gene junctions. The switch is made by the concentration of soluble N protein, kept assembly-competent by P: when N–P complexes are abundant they encapsidate the nascent (+) strand, the seven A residues cannot slip on the template, and the polymerase reads through to make a full-length antigenome. Paramyxovirus genomes obey the rule of six — their length must be a multiple of six nucleotides, because each nucleoprotein monomer binds exactly six.

### 25.4.2. Segmented genomes and influenza virus

Influenza A virus carries eight nucleocapsids, each with a copy of the heterotrimeric polymerase (PB1 the polymerase, PB2 the cap-binding subunit, PA the endonuclease). Three kinds of RNA are made: the (−) strand vRNA genome, the capped and polyadenylated mRNAs, and the full-length (+) strand cRNA that serves as the replication intermediate. mRNA synthesis is primed by cap snatching, and its 3′ end is made by reiterative copying of a short U stretch, because the polymerase remains bound to the 5′ end of the template and eventually cannot pull it further. Replication, by contrast, is unprimed and must read through the polyadenylation signal, which again requires newly made nucleoprotein. Influenza virus is one of the few RNA viruses that replicate in the nucleus, which is a consequence of cap snatching and also allows the M and NS mRNAs to be spliced by the host spliceosome.

![Influenza virus RNA synthesis and reassortment. Left: a vRNP contains one (−) strand segment coated with nucleoprotein and the PB1–PB2–PA polymerase bound to both ends. PB2 binds a host cap, PA cleaves 10–13 nucleotides downstream, and PB1 extends the capped primer into mRNA, which terminates by stuttering on the template's U track; replication proceeds without a primer through a full-length cRNA and requires free nucleoprotein. Right: a cell infected by two viruses packages segments from either parent, so that progeny carry new combinations — the molecular event behind antigenic shift.](./plots/influenza-rna.py)

Arenaviruses and some bunyaviruses are ambisense: one segment encodes one protein in the (−) sense and another in the (+) sense of the complementary strand, with transcription of each terminating at an intergenic hairpin, so that the second gene of each pair can be expressed only after a full-length antigenome has been made. The arrangement is a transcriptional timer built into the genome's polarity.

## 25.5. Double-Stranded RNA Viruses and Defective Particles

Double-stranded RNA cannot be translated and is the most potent trigger of innate antiviral sensing, so these viruses never expose it. The reovirus core — ten to twelve genome segments, each with its own polymerase molecule anchored under a fivefold vertex — is a transcription machine: mRNAs are synthesized inside the particle and extruded through channels at the vertices, capped on the way out. Progeny (+) strands are then packaged into new subviral particles, one copy of each segment, and each is copied once inside them to regenerate the duplex. Replication is thus conservative: the parental duplex is retained and the (+) strand released is the new template. Rotaviruses, the main cause of severe childhood gastroenteritis, release several mRNAs simultaneously through the vertex channels; no double-stranded RNA virus has more segments than there are fivefold vertices.

**Definition 25.5.1 (Defective interfering particle)** A *defective interfering particle* contains a genome with a large internal deletion that retains the signals for replication and packaging. It cannot replicate alone, but in a cell coinfected with the parental virus it is replicated by the proteins the helper supplies, and because it is shorter it outcompetes the full-length genome for the replication machinery and depresses the yield of infectious virus.

Defective interfering particles arise from template switching and accumulate under conditions of high multiplicity of infection or serial undiluted passage, which are easy to achieve in the laboratory and rare in nature. They are a major source of irreproducibility in virus stocks; they are also potent activators of interferon, and engineered defective genomes are being examined as antiviral agents.

## 25.6. Reverse Transcription and Integration

**Definition 25.6.1 (Retrovirus)** A *retrovirus* is an enveloped virus whose particle contains two copies of a (+) strand RNA genome and a reverse transcriptase, and whose genome is copied into double-stranded DNA and inserted into a chromosome of the host cell.

Back-to-back reports from the laboratories of Howard Temin and David Baltimore in 1970 demonstrated an RNA-directed DNA polymerase inside retrovirus particles; the Nobel Prize followed in 1975. The immediate consequence was the amendment of the central dogma to allow the flow of information from RNA to DNA; **reverse transcriptase** also became one of the standard tools of molecular biology. The mechanism of the enzyme and of retrotransposition is treated in [7.2.9](/7.2.9) and [7.4.17](/7.4.17); what follows is the viral pathway.

### 25.6.1. Two jumps make the long terminal repeats

The particle contains two genome copies held together by base pairing near their 5′ ends — retroviruses are said to be pseudodiploid, since only one provirus normally results — together with about 50 to 100 molecules of reverse transcriptase, nucleocapsid protein bound along the RNA, and a specific cellular tRNA annealed to the primer-binding site.

![Reverse transcription of a retroviral genome. (1) Synthesis of (−) strand DNA starts from the 3′ end of the tRNA primer at the primer-binding site near the 5′ end of the genome and stops after about a hundred nucleotides; RNase H degrades the copied RNA. (2) The first jump anneals the R sequence of this (−) strong-stop DNA to the r sequence at the 3′ end of a genome, and synthesis continues the length of the template. (3) A polypurine tract resistant to RNase H primes (+) strand synthesis, which copies the first eighteen nucleotides of the tRNA. (4) After removal of both primers the second jump anneals the complementary primer-binding sequences, and strand-displacement synthesis completes a linear duplex in which the sequences u3-r-u5 appear at both ends as long terminal repeats.](./plots/reverse-transcription.py)

**Definition 25.6.2 (Long terminal repeat)** The *long terminal repeat* (LTR) is the sequence U3-R-U5 that is generated at both ends of the DNA product by the two template exchanges, from sequences present only once at each end of the RNA. The left LTR contains the promoter and enhancer that cellular RNA polymerase II uses to transcribe the integrated genome; the right LTR supplies the polyadenylation signal.

Because reverse transcription uses two templates and exchanges between them whenever the enzyme pauses or meets a break, recombination is very frequent — the copy-choice mechanism that generates mosaic genomes and new circulating forms of HIV-1. Reverse transcriptase has no proofreading activity, so retroviruses sit in the same mutational regime as the RNA viruses of §25.2.

### 25.6.2. Integration

**Definition 25.6.3 (Integrase and provirus)** *Integrase* (IN) is the viral recombinase, related to bacterial transposases, that inserts the viral DNA into host DNA; the inserted copy is the *provirus*. Retroviruses are the only animal viruses that encode such an enzyme.

Integration has three steps. A tetramer of IN assembled on the two DNA ends — the intasome — removes two nucleotides from each 3′ end, exposing a conserved CA-3′-OH; the two processed ends then attack phosphodiester bonds on opposite strands of the target, 4 to 6 bp apart, in a concerted transesterification; and cellular repair enzymes fill the resulting gaps, which produces the short direct repeat of host sequence that flanks every provirus. Because processing requires complete, correctly made ends, defective DNA molecules are largely excluded.

Integration is not random. HIV-1 integrates preferentially within the bodies of actively transcribed genes, murine leukemia virus near transcription start sites, and the difference lies in which cellular protein tethers the intasome to chromatin: LEDGF/p75, which reads the H3K36me3 mark of transcribed genes, for lentiviruses, and the bromodomain proteins Brd2–4, which read acetylated histones at promoters, for gammaretroviruses. The consequences are practical: tethering-site preference determines the risk of insertional activation of a proto-oncogene by a retroviral vector, which is why self-inactivating lentiviral vectors have displaced gammaretroviral ones in gene therapy, and the IN–LEDGF interface is itself a drug target.

### 25.6.3. Expression, assembly and maturation

The provirus is transcribed by host RNA polymerase II into a single pre-mRNA, which is used in three ways: unspliced as the genome and as the mRNA for Gag and Gag-Pol, singly spliced as the mRNA for the envelope glycoprotein, and in complex retroviruses multiply spliced for the regulatory proteins. The ratio of Gag to Gag-Pol, about 20:1, is set by a −1 ribosomal frameshift (or, in some genera, readthrough of a stop codon), which guarantees that each particle receives few enzyme molecules and many structural ones. Particles assemble at the membrane around a dimer of genomic RNA selected by the packaging signal, bud, and only then mature: the viral protease cleaves Gag and Gag-Pol, the capsid rearranges into its mature shell, and the particle becomes infectious. Each of these steps — entry, reverse transcription, integration, proteolytic maturation — is the target of a class of antiretroviral drug ([7.11.28](/7.11.28)).

**Remark 25.6.1** HIV-1 produces of the order of $10^{10}$ virions per day in an untreated patient, with a mutation rate near $3 \times 10^{-5}$ per base per cycle and a genome of about $10^4$ bases. Every single-nucleotide change therefore arises many times each day, and monotherapy fails within weeks; combination therapy works because the simultaneous appearance of three or four specific mutations in one genome is correspondingly improbable. This is the quasispecies argument of §25.2 applied to clinical practice.

## 25.7. Hepadnaviruses: a DNA Genome Made by Reverse Transcription

Hepatitis B virus has a 3.2 kb gapped circular DNA genome and no integrase, yet it replicates entirely by reverse transcription — the mirror image of the retroviral strategy.

![The hepatitis B virus replication cycle inside one cell. The incoming gapped genome is repaired in the nucleus into covalently closed circular DNA, which acquires histones and persists as a minichromosome; host RNA polymerase II transcribes from it the 3.5 kb pregenomic RNA, which is capped, polyadenylated and terminally redundant. In the cytoplasm the P protein binds the ε stem-loop at the 5′ end of its own transcript, which drives packaging into a core particle; P primes (−) strand DNA synthesis on a tyrosine of its terminal-protein domain, the RNA template is degraded by its RNase H domain except for a capped 5′ fragment that is translocated to prime (+) strand synthesis, and the incomplete (+) strand leaves the gap found in the virion. Core particles either bud into the endoplasmic reticulum and are secreted, or return their DNA to the nucleus to increase the pool of covalently closed circular DNA.](./plots/hbv-cccdna.py)

| | Retroviruses | Hepadnaviruses |
|---|---|---|
| Genome in the particle | RNA, pseudodiploid | DNA, incomplete duplex |
| Template RNA also serves as | genome and mRNA for Gag, Gag-Pol | pregenomic RNA and mRNA for C and P |
| Enzyme molecules per core | 50–100 | 1 |
| Primer for the (−) strand | host tRNA | the P protein itself |
| Primer for the (+) strand | internal RNase H product (polypurine tract) | capped 5′ fragment, translocated |
| Where reverse transcription occurs | in the entering core, before integration | in the assembling core, before release |
| Persistent form | integrated provirus | nuclear covalently closed circular DNA |

**Remark 25.7.1** Covalently closed circular DNA is why hepatitis B infection is rarely cured. Nucleoside analogues such as tenofovir block reverse transcription and suppress viremia almost completely, but they do not touch the existing minichromosomes, which persist for the life of the hepatocyte and resume transcription when treatment stops. Integration of fragments of the genome into host chromosomes occurs as an accident, contributes no replication intermediates, and is a step in hepatocellular carcinogenesis.

## 25.8. Variation and the Evolution of RNA Viruses

Three mechanisms generate the variation on which selection acts, and they differ in grain.

| Mechanism | What is exchanged | Where it happens | Consequence |
|---|---|---|---|
| Misincorporation | single nucleotides | every round of copying | the quasispecies; drug and antibody escape; antigenic drift |
| Recombination (copy choice) | blocks of sequence | coinfected cells, during (−) strand synthesis or reverse transcription | mosaic genomes; new HIV-1 circulating forms; recombination between vaccine and wild enteroviruses |
| Reassortment | whole segments | coinfected cells, at packaging | abrupt change in a surface protein — antigenic shift in influenza virus |

Recombination requires that two genomes be copied in one complex, and is correspondingly frequent in retroviruses, where the particle is diploid, and in picornaviruses, where 10–20% of genomes may recombine in one growth cycle. Recombinants of the live attenuated poliovirus vaccine with other enteroviruses of the gut are readily isolated, and can regain the ability to spread. Recombination can also create pathogens: in bovine viral diarrhea virus, insertion of a cellular ubiquitin sequence that adds a protease cleavage site converts a non-cytopathic virus into a cytopathic, lethal one.

Reassortment is restricted to segmented genomes but needs no sequence similarity. A cell coinfected with two influenza A viruses can package any combination of the eight segments, and the introduction of a hemagglutinin to which the human population has no immunity is the molecular definition of **antigenic shift**. Cross-species transmission, the surveillance that detects it and the molecular epidemiology that reconstructs it belong to [7.11.27](/7.11.27).

Finally, the rate of change is not the same along every part of a genome, and the selective regime can be read from the sequences themselves: the ratio $d_\mathrm{N}/d_\mathrm{S}$ (see [7.10.23](/7.10.23)) exceeds 1 at the antibody-binding sites of influenza hemagglutinin and the HIV-1 envelope, the signature of selection by host immunity, while the polymerase genes are strongly constrained. The same machinery of molecular evolution, run on viral genomes sampled through an outbreak, gives both the dates of divergence and the identity of the amino acid changes that mattered. The clinical consequences — why influenza vaccines are reformulated, why HIV-1 and hepatitis C vaccines are hard, why single-drug therapy fails — are taken up in [7.11.28](/7.11.28).

## Summary

- No cell can copy RNA with RNA, so every RNA virus encodes an RdRp (Definition 25.1.1) or a reverse transcriptase. RdRps have a closed right-hand fold and start chains de novo, by prime-and-realign, from a protein primer (VPg) or from a snatched cellular cap.
- RdRps do not proofread; error rates of $10^{-3}$ to $10^{-5}$ per nucleotide make every population a quasispecies (Definition 25.2.1), set an upper limit on genome length through the error threshold ([Theorem 23.6.1](/7.2.23#thm-23.6.1)), and make lethal mutagenesis a drug strategy. The coronavirus proofreading exonuclease nsp14 is the exception that allows a 30 kb RNA genome.
- **Positive-strand RNA viruses** (Definition 25.3.1) translate their genome on entry, usually as a polyprotein (Definition 25.3.2), and replicate on remodeled membranes; many also make subgenomic mRNAs (Definition 25.3.3), which the coronaviruses produce as a nested set by discontinuous (−) strand synthesis.
- **Negative-strand RNA viruses** (Definition 25.4.1) use their genome as a template only as a nucleocapsid. Nonsegmented viruses transcribe by start–stop from one 3′ entry site, giving a gradient of mRNAs, and switch to replication when free nucleoprotein is abundant; influenza virus snatches caps in the nucleus and makes vRNA, cRNA and mRNA.
- Double-stranded RNA viruses transcribe inside the capsid and replicate conservatively in newly assembled subviral particles, never exposing duplex RNA. Deleted genomes that retain replication and packaging signals become defective interfering particles (Definition 25.5.1).
- Retroviruses (Definition 25.6.1) convert their diploid RNA genome into DNA by two template jumps that create the long terminal repeats (Definition 25.6.2), and integrase inserts the DNA as a provirus (Definition 25.6.3) at sites chosen by cellular tethering proteins. Expression uses alternative splicing and ribosomal frameshifting; the protease acts only after budding.
- Hepadnaviruses reverse transcribe a pregenomic RNA inside the assembling core, using the polymerase itself as the primer, and persist as nuclear covalently closed circular DNA, which current drugs do not eliminate.
- Point mutation, copy-choice recombination and reassortment generate variation at three different grains; the last is the mechanism of antigenic shift.

## Questions

1. The deproteinized genome of poliovirus is infectious, that of influenza virus is not, and that of a retrovirus is not either, although it is a (+) strand RNA. Explain each case.

   **Answer** Poliovirus RNA has the polarity of mRNA and carries an internal ribosome entry site, so ribosomes translate it and make the polymerase. Influenza virus RNA is (−) sense, cannot be translated, and can be copied by no cellular enzyme; it is also inert unless assembled with nucleoprotein and polymerase. Retroviral RNA is (+) sense but is not used as mRNA on entry: it must first be reverse transcribed and integrated, and the particle's reverse transcriptase, which is absent from naked RNA, is required.

2. Coronaviruses have both the largest RNA genome known and the only RNA-virus proofreading exonuclease. Explain the connection quantitatively, and state one consequence for antiviral therapy.

   **Answer** With error rate $\mu$ per base and genome length $L$, the fraction of error-free copies is $\mathrm{e}^{-\mu L}$; at a typical RdRp rate of $10^{-4}$, a 30 kb genome would receive about three mutations per copy and the population would exceed the error threshold. ExoN lowers $\mu$ by a factor of 15–20, bringing $\mu L$ back to order unity and making the large genome viable. The same exonuclease excises many nucleoside analogues, so useful drugs must evade it — remdesivir does so by causing delayed chain termination rather than immediate termination.

3. Vesicular stomatitis virus makes five mRNAs in the fixed abundance order N > P > M > G > L from a single polymerase entry site. Explain the mechanism, and describe how one would map the gene order without sequencing.

   **Answer** The polymerase enters only at the 3′ end and transcribes by start–stop: after each gene it polyadenylates by stuttering, terminates and reinitiates at the next gene start with about 70–80% efficiency, so abundance decreases geometrically along the genome. Ultraviolet irradiation maps the order: pyrimidine dimers block the polymerase, so the target size for abolishing a given mRNA is its own gene plus all sequence 3′ of it. Plotting the inactivation dose for each mRNA ranks the genes by distance from the 3′ end.

4. Reverse transcription begins near the 5′ end of the genome and runs out of template after about 100 nucleotides. Why is this apparently wasteful start necessary?

   **Answer** The u3 and u5 sequences are present once each, at opposite ends of the genomic RNA, but the DNA product must carry both at both ends, since the promoter and enhancer (in U3) must lie upstream of the transcription start and the polyadenylation signal (in R/U5) downstream. Starting at the primer-binding site near the 5′ end produces (−) strong-stop DNA whose R sequence can anneal to the r at the 3′ end of a genome; this first jump translocates u5 to the far end. The second jump, through the complementary primer-binding sequences, does the same for u3. The two exchanges therefore duplicate and reposition the control signals, generating identical long terminal repeats.

5. A patient with chronic hepatitis B takes tenofovir for five years; serum viral DNA is undetectable throughout, but viremia returns within months of stopping. Explain in molecular terms, and say what a curative drug would have to do.

   **Answer** Tenofovir is a nucleotide analogue that blocks the reverse transcription of pregenomic RNA into (−) strand DNA inside core particles, so no new genomes and no new virions are made. It does not act on the covalently closed circular DNA already present in hepatocyte nuclei, which is a stable, chromatinized minichromosome replicated by nothing and degraded only slowly, and which can also be replenished from the few remaining cores. When the drug is withdrawn, transcription from that pool restarts the cycle. A curative agent would have to eliminate or permanently silence the covalently closed circular DNA — by targeted nuclease cleavage, by epigenetic silencing, or by immune clearance of the infected hepatocytes.
