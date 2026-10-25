---
title: The Content of the Genome
description: Genome size and gene number across life and the C-value paradox; coding sequence, introns and repetitive DNA (reassociation kinetics, satellites, mini- and microsatellites, LINEs, SINEs, pseudogenes); centromeres, telomeres and replication origins; split genes and open reading frames; overlapping, nested and antisense genes; the classes of noncoding RNA; organelle genomes and horizontal transfer; gene density across species.
---

The genome is the archive of the cell (Definition 1.2.2). Before asking how it is copied and read, we take an inventory of what it contains. The inventory holds surprises that the bacterial picture of a gene did not prepare for: genome size varies more than a hundred-thousand-fold among eukaryotes while gene number varies only tenfold; in the human genome the protein-coding sequence is about one per cent, and nearly half of the DNA descends from mobile elements; genes are interrupted, overlap and are read from both strands. This chapter surveys genome size and gene number (2.1), the classes of sequence that make up a genome (2.2), the elements a chromosome needs in order to be replicated and segregated (2.3), the structure of genes (2.4–2.5), the kinds of RNA that genes produce (2.6), the genomes of organelles and the exchange of genes between lineages (2.7), and how densely genes are packed (2.8). The packaging of this DNA follows in the next two chapters ([7.2.3](/7.2.3), [7.2.4](/7.2.4)); how genomes are sequenced is described in [7.2.6](/7.2.6), and how they are analyzed belongs to [7.8](/7.8).

## 2.1. Genome Size and Gene Number

### 2.1.1. The Range of Genome Sizes

**Definition 2.1.1** The **C value** of an organism is the amount of DNA in its haploid genome, expressed as a mass (picograms) or as a number of base pairs; $1\,\mathrm{pg}$ of DNA corresponds to $978\,\mathrm{Mb}$.

Genomes span an enormous range. Among cellular organisms the smallest are those of insect endosymbionts (about $0.11$–$0.16\,\mathrm{Mb}$, under 200 genes), which rely on their hosts for most functions; the smallest free-living bacteria have about $1.3\,\mathrm{Mb}$ and 1300 genes (*Pelagibacter ubique*). A laboratory-designed minimal bacterial genome (JCVI-syn3.0, 2016) has $531\,\mathrm{kb}$ and 473 genes, of which about 150 had no known function when it was built. Eukaryotic genomes range from about $2.5\,\mathrm{Mb}$ (microsporidian parasites) through $12\,\mathrm{Mb}$ (yeast), $3.1\,\mathrm{Gb}$ (human) and $16\,\mathrm{Gb}$ (onion) to more than $100\,\mathrm{Gb}$ in some lungfishes and about $150\,\mathrm{Gb}$ in the largest plant genomes (*Paris japonica*, the fern *Tmesipteris oblanceolata*).

![Genome size against the number of protein-coding genes on logarithmic axes, for representative bacteria and archaea (green) and eukaryotes (brown); values are approximate and depend on the assembly and annotation. Bacteria and archaea lie close to the dashed line of one gene per kilobase, from the endosymbiont Carsonella to the myxobacterium Sorangium. Eukaryotes lie to the right of the line and spread out: the gene count grows only from about 2000 (the microsporidian Encephalitozoon) to a few tens of thousands, while genome size grows more than ten-thousand-fold; the axolotl has a genome ten times larger than the human genome with a similar number of genes, and the large gene count of wheat reflects its six sets of chromosomes.](./plots/genome-size-genes.py)

### 2.1.2. The C-Value Paradox

In bacteria genome size and gene number are nearly proportional: about one gene per kilobase, with almost 90 % of the DNA coding. In eukaryotes the proportionality fails.

**Definition 2.1.2 (C-Value Paradox)** The **C-value paradox** is the absence of a correlation between the C value of eukaryotes and their biological complexity: organisms of similar complexity can differ greatly in genome size, and simpler organisms can have much larger genomes than complex ones.

The toad *Xenopus laevis* and humans have genomes of about the same size; a cricket has about ten times the DNA of a fruit fly; an onion has five times as much as a human. Since the 1970s the paradox has had a resolution in outline: genome size is dominated not by genes but by noncoding DNA, above all by repetitive sequences and the remains of transposable elements (2.2), and the amount of such DNA varies between lineages for reasons that have little to do with organismal complexity. What remains open is why some lineages accumulate this DNA and others purge it (2.8), which is why some authors prefer to speak of the "C-value enigma". Gene number is a better but still weak indicator of complexity: humans have about as many protein-coding genes as a nematode. Complexity arises from how genes are used (alternative splicing, combinatorial regulation, [7.2.14](/7.2.14), [7.2.16](/7.2.16)), not from how many there are.

## 2.2. Coding Sequence, Introns and Repetitive DNA

### 2.2.1. The Composition of the Human Genome

The complete (telomere-to-telomere) human genome assembly of 2022 contains about $3.06\,\mathrm{Gb}$. Classified by gene structure, about $1.2\,\%$ is protein-coding sequence and about $1\,\%$ untranslated parts of exons; the introns of protein-coding genes make up about a third; the rest lies outside protein-coding genes. Classified by sequence type, more than half of the genome is repetitive.

![Approximate composition of the human genome classified in two ways. Top: by gene structure, protein-coding exons (1.2 % coding sequence and about 1 % untranslated regions), introns of protein-coding genes (about 36 %) and DNA outside protein-coding genes (intergenic DNA, noncoding-RNA genes, regulatory elements). Bottom: by sequence class, transposon-derived interspersed repeats (LINEs 21 %, SINEs 13 %, LTR retrotransposons 9 %, DNA transposons 4 %, together about 46 %), tandem repeats (satellites and simple repeats, about 8 % in the complete assembly, much of it in centromeres) and non-repetitive DNA (46 %). The two classifications overlap: most repeats lie within introns and intergenic DNA.](./plots/genome-composition.py)

### 2.2.2. Reassociation Kinetics

Repetitive DNA was discovered before DNA sequencing, by measuring how fast denatured genomic DNA re-forms double strands. When DNA is sheared into fragments of a few hundred base pairs and melted, each single strand must find its complementary partner. Reassociation of complementary strands is a **second-order reaction** ([6.3.15](/6.3.15)): if $C$ is the concentration of single-stranded DNA (in moles of nucleotide per liter) and $C_0$ its initial value,

$$
\frac{\mathrm{d}C}{\mathrm{d}t} = -kC^2 \quad\Longrightarrow\quad \frac{C}{C_0} = \frac{1}{1 + kC_0t}.
$$
The single-stranded fraction therefore depends only on the product $C_0t$, and half of the DNA has reassociated at $C_0t_{1/2} = 1/k$. The rate constant is inversely proportional to the complexity $N$ of the DNA, the length of distinct sequence it contains: at a fixed total concentration, the concentration of any particular sequence is proportional to $1/N$. Hence

$$
C_0t_{1/2} \propto N.
$$
For a genome of size $G$ in which a family of sequences is repeated $r$ times, that family has complexity proportional to $G/r$ in a mixture whose total DNA concentration is $C_0$, so it reassociates $r$ times faster than unique sequence. A genome that contains several families gives a curve with several steps, each step having a height equal to the fraction of the genome in the family and a position set by its repetition number (Britten and Kohne, 1968).

![Reassociation (C0t) curves calculated from second-order kinetics, with the C0t axis in units of the half-reassociation value of E. coli DNA. Phage T4 DNA (0.17 Mb) reassociates about 27 times faster than E. coli DNA (4.6 Mb), in proportion to their complexities; both give a single step because their sequences are unique. A model mammalian genome of 3 Gb gives three steps: 10 % highly repetitive DNA (about a million copies per genome) reassociates first, 20 % moderately repetitive DNA (about a thousand copies) next, and the 70 % unique DNA last, about 650 times later than E. coli DNA.](./plots/cot-curves.py)

**Definition 2.2.1 (Repetitive DNA)** **Repetitive DNA** consists of sequences present in many copies per haploid genome. By reassociation kinetics it is divided into **highly repetitive DNA** (short units, about $10^5$–$10^7$ copies, mostly in tandem arrays) and **moderately repetitive DNA** (longer units, about $10$–$10^5$ copies, mostly interspersed); the rest is unique (single-copy) DNA, which contains most protein-coding genes.

### 2.2.3. Tandem Repeats

**Definition 2.2.2** **Satellite DNA** consists of long tandem arrays of a repeat unit, from a few to several hundred base pairs, that can extend over megabases; it is named for the separate "satellite" bands that it forms in cesium chloride density gradients because its base composition differs from that of bulk DNA. **Minisatellites** are tandem arrays of units of about $10$–$60\,\mathrm{bp}$ spanning up to tens of kilobases. **Microsatellites**, or short tandem repeats (STRs), are arrays of units of $1$–$6\,\mathrm{bp}$, typically less than a few hundred base pairs long.

Satellites are concentrated in centromeres and other heterochromatin (2.3); the human α-satellite has a $171\,\mathrm{bp}$ unit. Minisatellites were the basis of the first DNA fingerprints (Jeffreys, 1985). Microsatellites mutate by slippage of the polymerase during replication, which adds or removes units at rates of about $10^{-4}$–$10^{-3}$ per locus per generation, about a million times the point-mutation rate per base pair. Their length polymorphism makes them markers for linkage mapping and forensic identification; expansions of trinucleotide repeats cause diseases such as Huntington disease (more than about 36 CAG repeats in *HTT*).

Moderately repetitive DNA also includes repeated genes: the genes for the large rRNA precursor are present in about 400 tandem copies on five human chromosomes, and histone genes form clusters ([7.2.17](/7.2.17)). Segmental duplications, blocks of more than a kilobase duplicated with over 90 % identity, cover about 7 % of the human genome and are hotspots of rearrangement.

### 2.2.4. Interspersed Repeats

Most moderately repetitive DNA in mammals consists of copies of transposable elements, sequences that can move or copy themselves to new positions; their mechanisms are described in [7.2.9](/7.2.9) and their genetic consequences in [7.4](/7.4). Two families of retrotransposons, which copy themselves through an RNA intermediate by reverse transcription (Definition 1.1.2), dominate the human genome.

**Definition 2.2.3** **LINEs** (long interspersed nuclear elements) are autonomous retrotransposons of up to $6$–$8\,\mathrm{kb}$ that encode the reverse transcriptase and endonuclease needed for their own transposition. **SINEs** (short interspersed nuclear elements) are nonautonomous retrotransposons of $100$–$300\,\mathrm{bp}$, derived from small cellular RNAs, that are copied by the enzymes of LINEs.

The human L1 family accounts for about 17 % of the genome in some 500,000 copies, nearly all truncated or mutated; about a hundred full-length copies remain active, and new insertions occasionally cause disease. The Alu family of SINEs, about $300\,\mathrm{bp}$ long and derived from the 7SL RNA of the signal recognition particle, has over a million copies (about 10 % of the genome). LTR retrotransposons, including endogenous retroviruses, make up about 8–9 %, and DNA transposons, which have been inactive in our lineage for tens of millions of years, about 3–4 %.

Transposon-derived DNA was long called "selfish" or "junk" DNA, and most of it probably has no function for the organism. Some copies have been co-opted as promoters, enhancers, exons and even genes (the RAG recombinase and the placental syncytins derive from transposons and retroviruses, [7.2.9](/7.2.9)).

### 2.2.5. Pseudogenes

**Definition 2.2.4 (Pseudogene)** A **pseudogene** is a sequence that resembles a functional gene but cannot produce a functional product, because of mutations that disrupt its reading frame, splicing or promoter. **Unprocessed pseudogenes** arise by duplication of a gene with its introns and subsequent inactivation; **processed pseudogenes** arise by reverse transcription of an mRNA and insertion of the copy into the genome, so they lack introns and promoters and end in an A-rich tract flanked by short direct repeats.

The human genome has about 15,000 pseudogenes, most of them processed copies made by the L1 machinery. A few are transcribed, and some of their transcripts appear to regulate the parent gene, but most are evolving neutrally.

## 2.3. Centromeres, Telomeres and Replication Origins

A linear eukaryotic chromosome needs three kinds of element to be inherited: origins from which it is replicated, a centromere by which it is segregated at division, and telomeres that protect its ends.

### 2.3.1. Centromeres

**Definition 2.3.1 (Centromere)** The **centromere** is the region of a chromosome at which the kinetochore assembles, the protein complex that attaches the chromosome to spindle microtubules and so ensures the equal segregation of sister chromatids at mitosis and of homologues at meiosis.

Centromeres come in two forms. The point centromere of the budding yeast *S. cerevisiae* is defined by sequence: about $125\,\mathrm{bp}$ consisting of three elements (CDEI, an AT-rich CDEII of about $80\,\mathrm{bp}$, and CDEIII), wrapped in a single nucleosome that contains the centromeric histone H3 variant (Cse4 in yeast, CENP-A in humans) and binds one microtubule. Regional centromeres of most other eukaryotes span kilobases to megabases; human centromeres consist of α-satellite arrays of $171\,\mathrm{bp}$ units organized into higher-order repeats over 0.3–5 Mb, the last part of the human genome to be sequenced completely (2022). Their identity is epigenetic rather than sequence-determined: the location of the centromere is marked by CENP-A nucleosomes, and neocentromeres can form on DNA without any α-satellite. Some organisms (the nematode *C. elegans*, many plants and insects) have holocentric chromosomes with kinetochores along their whole length.

### 2.3.2. Telomeres

**Definition 2.3.2 (Telomere)** A **telomere** is the specialized structure at the end of a linear eukaryotic chromosome, consisting of tandem repeats of a short G-rich sequence and the proteins bound to them, that protects the end from degradation and from being recognized as a DNA break, and allows the end to be replicated.

| Organism | Telomere repeat (G-rich strand, 5′ → 3′) | Length of the array |
|---|---|---|
| Human | TTAGGG | $5$–$15\,\mathrm{kb}$ |
| *Tetrahymena* (ciliate) | TTGGGG | about $0.3\,\mathrm{kb}$ |
| *S. cerevisiae* | TG₁₋₃ (irregular) | about $0.3\,\mathrm{kb}$ |
| *Arabidopsis* | TTTAGGG | $2$–$5\,\mathrm{kb}$ |

The G-rich strand runs $5' \to 3'$ toward the chromosome end and protrudes as a single-stranded overhang of $50$–$300$ nucleotides in humans. In mammals the overhang invades the duplex repeats to form a T loop, and the array is bound by a six-protein complex, shelterin, which prevents the DNA damage response from treating the end as a break. Because the lagging-strand machinery cannot copy the very end of a linear template, telomeres shorten with each round of replication unless they are extended by telomerase, a reverse transcriptase that carries its own RNA template ([7.2.7](/7.2.7)). Human somatic cells without telomerase lose about $50$–$100\,\mathrm{bp}$ per division, which limits their number of divisions. *Drosophila* has no telomerase: its chromosome ends are maintained by specialized retrotransposons that repeatedly insert at the ends, another use of reverse transcription.

### 2.3.3. Replication Origins and Artificial Chromosomes

Replication starts at origins ([7.2.7](/7.2.7)). The *E. coli* chromosome has a single origin, *oriC*, of about $245\,\mathrm{bp}$ containing binding sites for the initiator DnaA and an AT-rich region that melts first; yeast origins (autonomously replicating sequences, ARS) are $100$–$200\,\mathrm{bp}$ elements with an $11\,\mathrm{bp}$ consensus, and the yeast genome has about 400 of them. Human cells use some 30,000–50,000 origins in each S phase, chosen from a larger set of licensed sites, and these origins have no consensus sequence.

These three elements are sufficient to make a chromosome: a yeast artificial chromosome (YAC, 1983) consists of a centromere, an origin and two telomeres plus selectable markers, and propagates inserts of up to about $1\,\mathrm{Mb}$ as a linear chromosome. YACs were used to map the human genome but proved unstable and prone to chimeric inserts; bacterial artificial chromosomes (BACs), single-copy plasmids derived from the F factor that carry $100$–$300\,\mathrm{kb}$, replaced them as the standard large-insert vector ([7.2.5](/7.2.5)). The same principle now operates on the scale of whole genomes: synthetic, redesigned versions of all sixteen chromosomes of *S. cerevisiae* have been built (the Sc2.0 project), and strains carrying several of them together are viable.

## 2.4. Split Genes and the Structure of Genes

### 2.4.1. Exons and Introns

**Definition 2.4.1** An **intron** is a segment of a gene that is transcribed but removed from the primary transcript by splicing; an **exon** is a segment that is retained in the mature RNA. Exons include the coding sequence and the untranslated regions (UTRs) of an mRNA.

Introns were discovered in 1977 in adenovirus and then in cellular genes ([7.2.16](/7.2.16)). They are rare in bacteria and archaea (where self-splicing introns occur in some tRNA and rRNA genes), uncommon in yeast (about 280 of its 6000 genes, mostly with a single short intron) and the rule in vertebrates and plants. A protein-coding gene of a eukaryote has, from 5′ to 3′: a promoter and regulatory elements; the transcription start site; exons containing the 5′ UTR, the coding sequence from the start codon to the stop codon, and the 3′ UTR with the polyadenylation signal; and the introns between the exons.

![Two human genes drawn to the same scale (coordinates from the transcription start site). The β-globin gene HBB has three exons of 142, 223 and 261 bp separated by introns of 130 and 850 bp; the coding sequence (dark) runs from the ATG start codon in exon 1 to the TAA stop codon in exon 3, flanked by a 50-nt 5′ untranslated region and a 132-nt 3′ untranslated region (light) that contains the AATAAA polyadenylation signal. A replication-dependent histone H4 gene has a single exon with a 312-bp coding sequence and short untranslated regions (lengths drawn approximately); its mRNA ends in a stem-loop and is not polyadenylated.](./plots/gene-models.py)

In vertebrates introns are usually much longer than exons. Typical values for human protein-coding genes are a median of about 8 exons (titin has 363), internal exons of about $120$–$150\,\mathrm{bp}$, introns with a median of about $1.5\,\mathrm{kb}$ and a long tail to hundreds of kilobases, and genes with a median length of about $25\,\mathrm{kb}$; the longest genes (*CNTNAP2*, *DMD*) span more than $2\,\mathrm{Mb}$. The seven introns of the chicken ovalbumin gene make up 85 % of its length, while histone genes have none. Exons often correspond to structural or functional domains of the encoded protein, and new proteins have arisen by shuffling exons between genes; intron positions are frequently conserved over hundreds of millions of years.

### 2.4.2. Open Reading Frames

**Definition 2.4.2 (Open Reading Frame)** An **open reading frame** (ORF) is a stretch of a nucleic-acid sequence, read in one of the three frames of one strand, that begins with a start codon and continues for a number of codons without an in-frame stop codon.

**Example 2.4.1 (Long ORFs are not random)** Three of the 64 codons are stop codons. In a random sequence with equal base frequencies, each codon is a stop with probability $3/64$, so the probability that a given frame stays open for $L$ codons is

$$
\left(\frac{61}{64}\right)^{L} = \mathrm{e}^{L\ln(61/64)} \approx \mathrm{e}^{-0.048L}.
$$
The mean distance between stops is $64/3 \approx 21$ codons; an ORF of 100 codons arises by chance with probability $\mathrm{e}^{-4.8} \approx 0.008$, and one of 300 codons with probability $6\times10^{-7}$. A long ORF is therefore strong evidence of a protein-coding gene, which is how genes are first identified in bacterial genomes, where they are uninterrupted. In eukaryotes the coding sequence is split among exons, so gene prediction must also recognize splice sites and relies on evidence from transcripts and from conservation between species ([7.8](/7.8)).

## 2.5. Overlapping, Nested and Antisense Genes

The template strand of a gene is the one copied by RNA polymerase; the opposite, nontemplate strand has the same sequence as the RNA (with T for U) and is called the coding or sense strand, so the template strand is also the antisense strand. By convention gene sequences are written as the coding strand, $5' \to 3'$. A given stretch of DNA can serve more than one gene:

- Overlapping genes: in small genomes several reading frames can share sequence. The $5386$-nt genome of phage φX174 encodes eleven proteins; gene *E* lies within gene *D* and gene *B* within gene *A*, read in different frames (Sanger and colleagues, 1976–1977). Overlaps are common in viruses and occasional in bacteria and eukaryotes.
- Nested genes: genes can lie inside the introns of other genes, often on the opposite strand; an intron of the human *NF1* gene contains three other genes.
- Antisense and bidirectional transcription: more than 10 % of human genes are arranged head to head with another gene within a kilobase, transcribed from a shared bidirectional promoter, and many genes have natural antisense transcripts, some of which regulate the sense gene (*Xist* and *Tsix* in X inactivation, [7.2.18](/7.2.18)).

Most of the genome is transcribed at some time in some cell, far beyond the annotated genes. Whether this "pervasive transcription" means that most of the genome is functional is disputed. The ENCODE project (2012) reported that about 80 % of the human genome shows some biochemical activity (transcription, protein binding, open chromatin); comparisons of genomes across mammals indicate that only about 5–15 % of the human genome is conserved by purifying selection. The difference reflects two meanings of "function": biochemical activity can occur without any effect on fitness, and evolutionary conservation is the more stringent criterion.

## 2.6. Classes of Noncoding RNA

**Definition 2.6.1 (Noncoding RNA)** A **noncoding RNA** (ncRNA) is an RNA molecule that functions without being translated into protein.

Noncoding RNAs were long thought to be limited to the RNAs of the translation and splicing machinery; small regulatory RNAs (from 1993) and long noncoding RNAs have since been found in large numbers. By mass, a cell's RNA is about 80 % rRNA, 10–15 % tRNA and only 3–5 % mRNA.

| Class | Size | Function | Chapter |
|---|---|---|---|
| rRNA | Bacteria 5S, 16S, 23S ($120$, $1540$, $2900\,\mathrm{nt}$); eukaryotes 5S, 5.8S, 18S, 28S (up to $5000\,\mathrm{nt}$) | Structure of the ribosome; catalysis of peptide-bond formation | [7.2.17](/7.2.17), [7.2.19](/7.2.19) |
| tRNA | $73$–$93\,\mathrm{nt}$ | Adaptor between codon and amino acid | [7.2.19](/7.2.19) |
| snRNA | $100$–$200\,\mathrm{nt}$ | Components of the spliceosome (U1, U2, U4, U5, U6) | [7.2.16](/7.2.16) |
| snoRNA | $60$–$300\,\mathrm{nt}$ | Guide 2′-O-methylation (box C/D) and pseudouridylation (box H/ACA) of rRNA and snRNA | [7.2.17](/7.2.17) |
| RNase P RNA, SRP RNA, telomerase RNA, 7SK RNA | $300$–$500\,\mathrm{nt}$ | tRNA processing (catalytic), protein targeting, telomere template, control of transcription elongation | [7.2.17](/7.2.17), [7.2.7](/7.2.7), [7.2.13](/7.2.13) |
| miRNA, siRNA | $21$–$24\,\mathrm{nt}$ | Guide Argonaute proteins to target RNAs: repression, cleavage | [7.2.18](/7.2.18) |
| piRNA | $24$–$31\,\mathrm{nt}$ | Silence transposons in the germ line | [7.2.18](/7.2.18) |
| lncRNA | More than $200\,\mathrm{nt}$, often kilobases | Diverse: chromatin regulation (*Xist*, $17\,\mathrm{kb}$), scaffolds of nuclear bodies, regulation of nearby genes | [7.2.18](/7.2.18) |
| circRNA | Hundreds of nucleotides | Products of back-splicing; most functions unknown | [7.2.16](/7.2.16) |
| Bacterial sRNA, 6S RNA, tmRNA, CRISPR RNA | $50$–$400\,\mathrm{nt}$ | Post-transcriptional regulation, regulation of RNA polymerase, rescue of stalled ribosomes, immunity | [7.2.18](/7.2.18), [7.2.24](/7.2.24) |

Riboswitches, which are RNA structures in the untranslated regions of bacterial mRNAs that bind metabolites and control expression of the same mRNA, are regulatory parts of mRNAs rather than separate noncoding genes ([7.2.18](/7.2.18)). Current human annotations list about 20,000 lncRNA genes and some 2000 miRNA precursors, but these numbers are much less certain than the count of protein-coding genes, and the function of most lncRNAs remains to be shown.

## 2.7. Organelle Genomes and Horizontal Gene Transfer

### 2.7.1. Mitochondrial and Chloroplast DNA

Mitochondria and chloroplasts descend from bacteria that became endosymbionts of an ancestral eukaryotic cell, and they keep small genomes of their own. Human mitochondrial DNA is a circle of $16{,}569\,\mathrm{bp}$ present in hundreds to thousands of copies per cell. It is extremely compact: it encodes 13 proteins (all subunits of the respiratory complexes and ATP synthase, [7.1.23](/7.1.23)), 2 rRNAs and 22 tRNAs, has no introns and almost no intergenic DNA apart from a control region of about $1\,\mathrm{kb}$ that contains the origin of one strand and the promoters. Both strands are transcribed into long polycistronic RNAs, which are cut at the tRNAs that punctuate the genes. Mitochondria use a slightly different genetic code (in vertebrate mitochondria UGA codes for Trp, AUA for Met, and AGA and AGG are stops; [7.2.19](/7.2.19)). Mitochondrial DNA is inherited from the mother, and a cell can contain a mixture of mutant and normal copies (heteroplasmy).

Organelle genomes vary widely: yeast mtDNA is about $86\,\mathrm{kb}$ with introns, plant mtDNAs range from about $200\,\mathrm{kb}$ to more than $10\,\mathrm{Mb}$ and are full of noncoding and foreign DNA, and chloroplast genomes are circles of $120$–$160\,\mathrm{kb}$ with about 100–130 genes. In every case most organelle proteins are encoded in the nucleus: of the more than 1100 proteins of a human mitochondrion, only 13 are made from mtDNA. During evolution the endosymbionts' genes were transferred to the nucleus, and the transfer continues: fragments of mtDNA and cpDNA are found inserted throughout nuclear genomes.

### 2.7.2. Horizontal Gene Transfer

Genes can also pass between unrelated organisms. In bacteria and archaea this horizontal (lateral) gene transfer is common: DNA enters cells by transformation (uptake of free DNA), transduction (carried by phages) and conjugation (transfer of plasmids and conjugative elements between cells) ([7.11](/7.11)). Genes for antibiotic resistance, toxins and new metabolic pathways spread this way, often clustered in genomic islands whose base composition differs from the rest of the chromosome. Plasmids, small circular DNAs that replicate independently of the chromosome, range from a few kilobases to more than a megabase. As a result, strains of one bacterial species can differ in hundreds of genes, and the set of genes found across a species (its pan-genome) far exceeds the genes of any one strain. In eukaryotes horizontal transfer is rare apart from the endosymbiotic transfers, but not absent.

## 2.8. Gene Density Across Species

**Example 2.8.1 (Genes per millimeter of DNA)** One millimeter of B-DNA contains $10^{-3}\,\mathrm{m}/(0.34\times10^{-9}\,\mathrm{m}) \approx 2.9\times10^6\,\mathrm{bp}$. *E. coli*, with 4300 genes in $4.64\,\mathrm{Mb}$, has about $930$ genes per megabase or $2700$ per millimeter; the human genome, with 20,000 protein-coding genes in $3.1\,\mathrm{Gb}$, has about $6.5$ per megabase or $19$ per millimeter.

| Organism | Genome | Protein-coding genes | Genes per Mb | Coding fraction |
|---|---|---|---|---|
| *E. coli* | $4.6\,\mathrm{Mb}$ | 4300 | 930 | about 88 % |
| *S. cerevisiae* | $12\,\mathrm{Mb}$ | 6000 | 500 | about 70 % |
| *C. elegans* | $100\,\mathrm{Mb}$ | 20,000 | 200 | about 25 % |
| *D. melanogaster* | $144\,\mathrm{Mb}$ | 13,900 | 97 | about 15 % |
| Pufferfish (*Takifugu*) | $390\,\mathrm{Mb}$ | 21,000 | 54 | about 10 % |
| Human | $3.1\,\mathrm{Gb}$ | 20,000 | 6.5 | about 1.2 % |
| Maize | $2.3\,\mathrm{Gb}$ | 39,000 | 17 | about 2 % |

Gene density also varies within a genome. Human chromosome 19 carries about 1500 protein-coding genes in $59\,\mathrm{Mb}$ (25 per megabase), whereas chromosomes 13 and 18 carry about 320 genes in $114\,\mathrm{Mb}$ and about 270 in $80\,\mathrm{Mb}$ (3 per megabase); it is probably no coincidence that trisomies 13, 18 and 21, of the three autosomes with the fewest genes, are the only autosomal trisomies regularly seen in live births. Gene-rich regions are GC-rich and lie in the nuclear interior; gene deserts of more than half a megabase without genes are common, and some contain enhancers that control distant genes.

Why do some lineages carry so much noncoding DNA? One influential hypothesis (Lynch and Conery, 2003) relates genome expansion to population size. An extra transposon copy or a longer intron is only very slightly harmful, with a selection coefficient $s$ perhaps of order $10^{-6}$ or smaller. Selection can remove such a variant only if $s$ exceeds about $1/N_{\mathrm{e}}$, where $N_{\mathrm{e}}$ is the effective population size; otherwise its fate is decided by random drift. Multicellular eukaryotes have small effective populations ($N_{\mathrm{e}} \approx 10^4$–$10^6$), so slightly harmful insertions can drift to fixation and genomes grow; bacteria have enormous ones ($N_{\mathrm{e}} \gtrsim 10^8$) and, helped by a bias of their genomes toward deletions, stay compact. The hypothesis explains the broad contrast between prokaryotes and multicellular eukaryotes, though not every difference in genome size among related species ([7.10](/7.10)).

## Summary

| Topic | Key points |
|---|---|
| Genome size (Definition 2.1.1) | Bacteria $0.1$–$13\,\mathrm{Mb}$ with about one gene per kb; eukaryotes $2.5\,\mathrm{Mb}$ to $150\,\mathrm{Gb}$ with $2000$–$40{,}000$ genes (human $3.1\,\mathrm{Gb}$, about $20{,}000$) |
| C-value paradox (Definition 2.1.2) | Genome size does not track complexity; it is dominated by noncoding, mostly repetitive DNA |
| Human genome | Coding $1.2\,\%$, UTRs about $1\,\%$, introns about a third; transposon-derived DNA about $46\,\%$, tandem repeats about $8\,\%$ |
| Reassociation kinetics | Second-order: $C/C_0 = 1/(1 + kC_0t)$, $C_0t_{1/2} \propto$ complexity; a family repeated $r$ times reassociates $r$ times faster; highly repetitive, moderately repetitive, unique DNA (Definition 2.2.1) |
| Tandem repeats (Definition 2.2.2) | Satellites (centromeres, heterochromatin), minisatellites (DNA fingerprints), microsatellites (slippage, STR markers, repeat-expansion diseases) |
| Interspersed repeats (Definition 2.2.3) | LINE-1 about $17\,\%$, Alu about $10\,\%$ (over $10^6$ copies), LTR elements $8$–$9\,\%$, DNA transposons $3$–$4\,\%$; pseudogenes, processed and unprocessed (Definition 2.2.4) |
| Chromosomal elements | Centromere (Definition 2.3.1): point (yeast, $125\,\mathrm{bp}$) or regional (α-satellite, epigenetic CENP-A); telomere (Definition 2.3.2): TTAGGG repeats, overhang, shelterin, telomerase; origins: one in *E. coli*, about 400 in yeast, $3$–$5\times10^4$ in human cells; artificial chromosomes |
| Genes | Exons and introns (Definition 2.4.1); median human gene about $25\,\mathrm{kb}$ with about 8 exons; ORF (Definition 2.4.2): by chance an ORF of $L$ codons has probability $(61/64)^L$ (Example 2.4.1) |
| Overlap | Overlapping reading frames (φX174), nested genes, bidirectional promoters, antisense transcripts; pervasive transcription versus conservation (5–15 % constrained) |
| Noncoding RNA (Definition 2.6.1) | rRNA, tRNA, snRNA, snoRNA, RNase P RNA, miRNA, siRNA, piRNA, lncRNA, circRNA, bacterial sRNA; rRNA about 80 % of RNA mass |
| Organelles | Human mtDNA $16{,}569\,\mathrm{bp}$, 37 genes (13 proteins, 2 rRNAs, 22 tRNAs), variant code; most organelle proteins nuclear-encoded; horizontal transfer common in bacteria |
| Gene density | 930 per Mb in *E. coli*, 6.5 per Mb in humans (19 per mm, Example 2.8.1); chromosome 19 versus 13 and 18; drift-barrier hypothesis |

## Questions

1. A eukaryotic DNA sample gives a reassociation curve with two steps of equal height, the first at $C_0t = 0.01$ and the second at $C_0t = 1000$ (in any consistent units). What can you conclude?

   **Answer** Half of the DNA belongs to a family that reassociates $10^5$ times faster than the other half. Both halves have the same total concentration, so the ratio of their $C_0t_{1/2}$ values is the ratio of their complexities: the fast component is $10^5$ times less complex. If the slow component is unique DNA, the fast component consists of sequences repeated about $10^5$ times; with the genome size known, the complexity of each component (the length of its repeat unit times the number of distinct units) follows from comparison with a standard such as *E. coli* DNA.

2. Why are microsatellites useful for forensic identification, while single-nucleotide polymorphisms dominate genome-wide association studies?

   **Answer** Microsatellites mutate by replication slippage at about $10^{-4}$–$10^{-3}$ per generation, so each locus has many alleles (different numbers of repeats), and a panel of about 20 loci gives a combination that is practically unique to an individual. They are measured by amplifying each locus and determining fragment lengths. SNPs have only two alleles each and are individually much less informative, but there are millions of them throughout the genome, they are stable over generations, and they can be typed in parallel on arrays or by sequencing, which suits association mapping across the whole genome.

3. In a random sequence with base frequencies $\mathbb{P}(\mathrm{A}) = \mathbb{P}(\mathrm{T}) = 0.3$ and $\mathbb{P}(\mathrm{G}) = \mathbb{P}(\mathrm{C}) = 0.2$, what is the probability that a codon is a stop codon (TAA, TAG, TGA)? How does the expected length of chance ORFs change compared with Example 2.4.1?

   **Answer** $\mathbb{P}(\mathrm{TAA}) = 0.3^3 = 0.027$, $\mathbb{P}(\mathrm{TAG}) = \mathbb{P}(\mathrm{TGA}) = 0.3\times0.3\times0.2 = 0.018$, total $0.063$, compared with $3/64 = 0.047$ for equal frequencies. The mean distance between stops falls from 21 to about 16 codons, and chance ORFs become shorter. Conversely, in GC-rich genomes stops are rarer and long chance ORFs more common, so gene finders must be calibrated to the base composition (some bacterial genomes have over 70 % GC).

4. A woman carries a mitochondrial mutation in 30 % of her mtDNA molecules. Explain why her children may have very different proportions of the mutant DNA.

   **Answer** Mitochondrial DNA is inherited only from the mother, and during the development of oocytes the number of mtDNA molecules passes through a bottleneck: the mtDNA of a mature oocyte (about $10^5$ copies) descends from a much smaller number of founder molecules. Random sampling of founders, like genetic drift in a small population, makes the mutant fraction in each oocyte vary widely around the mother's 30 %, so one child can inherit almost none and another a large majority; the disease appears when the mutant fraction in a tissue exceeds a threshold.

5. The human α-satellite is a $171\,\mathrm{bp}$ unit repeated in arrays of several megabases. Why were centromeres the last regions of the human genome to be assembled, and what does the existence of neocentromeres say about how centromeres are specified?

   **Answer** Assembly joins sequencing reads by their overlaps; when the same unit and its higher-order repeats recur thousands of times with near-identical sequence, short reads cannot be placed uniquely, so the arrays remained gaps until long reads of tens of kilobases or more, spanning unique variants within the arrays, became available (complete assembly in 2022). Neocentromeres, which form on ordinary DNA lacking α-satellite and are then inherited stably, show that centromere position is specified epigenetically, by the deposition of CENP-A nucleosomes at the existing centromere in each cell cycle, rather than by the satellite sequence itself.
