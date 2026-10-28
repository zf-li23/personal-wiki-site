---
title: Genomes, Genomic Variation and Positional Cloning
description: Genomes from a geneticist's viewpoint and the variation between them. Physical maps and shotgun assembly with the Lander–Waterman model, repeats, long reads, the complete human genome and pangenomes; annotation (the statistics of open reading frames, codon bias, conservation, cDNA and RNA sequencing); gene families and the fates of duplicate genes, the globin genes, de novo genes, synteny; BLAST E-values; ancient DNA. Then SNPs, indels, short tandem repeats, copy-number and structural variants; genotyping, DNA fingerprinting and preimplantation diagnosis; LOD scores for phase-known and phase-unknown families and the threshold of 3; positional cloning of the Huntington, cystic fibrosis and NF1 genes; and the diagnosis of Mendelian disease by exome and genome sequencing.
---

Classical genetics located genes by the phenotypes of their mutant alleles and by recombination between them ([7.4.8](/7.4.8)). Genomics reads the DNA itself. The two meet in this chapter. Its first part looks at whole genomes as a geneticist does: how a genome sequence is assembled from fragments and how reliable that is, how genes are found in it, and how gene families arise by duplication; the composition of genomes and the chemistry of sequencing are described in [7.2.2](/7.2.2) and [7.2.6](/7.2.6), and the algorithms of assembly and alignment in [7.8](/7.8). Its second part turns to the differences between genomes. Most of the millions of differences between two people have no effect, but each is a marker: inherited like an allele, it can be followed through families and used to locate the mutations that cause disease. The statistical tool is the LOD score, a likelihood ratio ([3.2.5](/3.2.5#sec-5.3)) applied to the recombination fraction, and the procedure built on it is positional cloning, which found the genes for Huntington disease, cystic fibrosis and hundreds of other disorders before exome sequencing made direct searches possible. The population genetics of the same variants, their frequencies and associations, follows in [7.4.22](/7.4.22) and [7.4.25](/7.4.25).

## 14.1. From Genetic Maps to Sequences

A **genetic map** orders loci by recombination frequency; a **physical map** ([7.4.8](/7.4.8)) places landmarks at known distances in base pairs. Before whole-genome sequencing, physical maps were built from overlapping clones. A genome was cut into fragments of $100$–$200\,\mathrm{kb}$, cloned in **bacterial artificial chromosomes** (BACs), and the clones were ordered by shared landmarks (restriction fragments, sequence-tagged sites detected by PCR). From the overlapping clones, a minimal tiling path, the smallest set of clones that covers a chromosome, was chosen and each clone was sequenced separately. This clone-by-clone strategy of the public Human Genome Project (draft 2001, "finished" 2004) was slow but anchored every piece of sequence on the map; the competing whole-genome shotgun strategy of Celera (2001) sequenced random fragments of the whole genome at once and relied on computation to put them together.

Genetic map, physical map and sequence are now one coordinate system: each genetic marker has a sequence and hence a position in base pairs, and plotting genetic against physical position (a Marey map, [7.4.8](/7.4.8#sec-8.8)) shows how the rate of crossing over varies along each chromosome.

## 14.2. Assembling a Genome

### 14.2.1. Shotgun Sequencing and Coverage

**Definition 14.2.1 (Shotgun Sequencing, Contig and Scaffold)** In **shotgun sequencing** many copies of a genome are broken into random fragments that are sequenced independently; the reads are then assembled by their overlaps into a consensus sequence. A **contig** is a contiguous sequence assembled from overlapping reads without gaps; a **scaffold** is an ordered and oriented set of contigs, separated by gaps of estimated size, that are known to be adjacent from paired reads, long reads or maps.

How many reads are needed? If reads are placed at random, each base is covered by a number of reads that is approximately Poisson with mean equal to the **sequencing coverage** $c$ ([7.2.6](/7.2.6#sec-6.9)), and an assembly fails where no read, or no sufficiently overlapping pair of reads, spans a point.

**Formula 14.2.1 (Lander–Waterman Model)** Let $N$ reads of length $L$ be placed uniformly at random on a genome of length $G \gg L$, with coverage $c = NL/G$, and let two overlapping reads be joined only if they overlap by at least $T$ bases; put $\sigma = 1 - T/L$. Then (a) the expected fraction of the genome not covered by any read is $\mathrm{e}^{-c}$; (b) the expected number of contigs is

$$
N\,\mathrm{e}^{-c\sigma} = \frac{cG}{L}\,\mathrm{e}^{-c\sigma};
$$
(c) the expected number of contigs is greatest at $c = 1/\sigma$ and then falls exponentially with $c$.

**Proof** (a) A given base is covered by a read if the read starts in the $L$ bases before it; the number of such reads is binomial with $N$ trials and probability $L/G$, approximately $\mathrm{Poi}(c)$, which is zero with probability $\mathrm{e}^{-c}$. (b) Order the reads by their start positions. A read is the last read of its contig if no other read starts within the next $L - T$ bases, i.e. within the part of it that would give an overlap of at least $T$; the number of starts in an interval of length $L\sigma$ is approximately $\mathrm{Poi}(c\sigma)$, so the probability is $\mathrm{e}^{-c\sigma}$. Each contig has exactly one last read, so the expected number of contigs is $N\mathrm{e}^{-c\sigma}$. (c) Differentiating $c\,\mathrm{e}^{-c\sigma}$ gives a maximum at $c = 1/\sigma$. $\square$

![The Lander–Waterman model (Formula 14.2.1). A: the fraction of the genome not covered by any read falls as e^(−c) with the coverage c (line; circles: means of 20 simulated sets of random reads on a circular genome of 1 Mb). B: the number of contigs, for reads of 1 kb joined by overlaps of at least 100 bases, rises at low coverage (more reads, more islands), is greatest at c = 1/σ ≈ 1.1, and then falls exponentially as the islands merge](./plots/lander-waterman.py)

**Example 14.2.1** A bacterial genome of $5\,\mathrm{Mb}$ is sequenced with $150$-base reads to coverage $8\times$, and reads are joined if they overlap by at least $30$ bases ($\sigma = 0.8$). The number of reads is $N = cG/L \approx 2.7 \times 10^5$, the expected number of contigs $N\mathrm{e}^{-6.4} \approx 440$, and the number of bases not covered $G\mathrm{e}^{-8} \approx 1\,700$. At $30\times$, the model predicts fewer than one contig gap, yet real short-read assemblies of bacteria still have tens of contigs: the model ignores repeats.

### 14.2.2. Repeats, Long Reads and the Complete Human Genome

A repeat longer than the reads cannot be assembled: reads from its copies are identical, so the assembler cannot tell which unique flank joins which. In complex genomes, where about half of the sequence is repetitive ([7.2.2](/7.2.2#sec-2.2.1)), repeats rather than coverage limit assembly. Three solutions are used. Paired-end and mate-pair reads, from the two ends of fragments of known size, span repeats shorter than the fragment and order the contigs into scaffolds. Long reads, of $10$–$100\,\mathrm{kb}$ or more from single-molecule real-time sequencing and nanopore sequencing ([7.2.6](/7.2.6#sec-6.7.3)), span most repeats outright. And maps (BACs, optical maps, Hi-C contacts) order the scaffolds along chromosomes.

The reference genome of 2004 left about $8\,\%$ of the human genome unsequenced: the centromeric satellite arrays, the short arms of the acrocentric chromosomes with the rRNA genes, and large segmental duplications. The Telomere-to-Telomere Consortium (2022) assembled the first complete sequence, of a hydatidiform mole (CHM13, with two identical paternal haploid genomes, so that no heterozygosity confuses the assembly), with highly accurate long reads and ultra-long nanopore reads of over $100\,\mathrm{kb}$. It added about $200\,\mathrm{Mb}$, mostly satellites and duplications, and about 2 000 predicted genes, 99 of them protein-coding.

### 14.2.3. Reference Bias and Pangenomes

A single reference genome represents one haplotype of one or a few people. Reads from segments that are missing or highly divergent in the reference map poorly or not at all, so variants in them are missed or miscalled (reference bias), and sequences present in other people but absent from the reference are invisible.

**Definition 14.2.2 (Pangenome)** A **pangenome** is the set of all sequences present in the genomes of a group of individuals (a species or a population), usually represented as a graph whose paths are the individual genomes; it comprises a core shared by all and a variable part present in some.

Bacterial pangenomes are large: two strains of *E. coli* may share only about half of their genes, the rest being acquired by **horizontal gene transfer** ([7.4.10](/7.4.10)). The first human pangenome reference (2023), from 47 phased diploid genomes, added about $119\,\mathrm{Mb}$ of sequence not in the linear reference and reduced the error rate of variant calling, especially of structural variants.

## 14.3. Finding Genes: Annotation

**Definition 14.3.1 (Genome Annotation)** **Genome annotation** is the identification of the functional elements of a genome sequence, above all the positions and exon–intron structures of genes and their products, and the attachment of biological information to them.

### 14.3.1. Long Open Reading Frames Are Signals

An **open reading frame** ([7.2.2](/7.2.2#sec-2.4.2)) is a run of codons without a stop codon. In random sequence, stop codons appear frequently, so a long ORF is unlikely to occur by chance.

**Formula 14.3.1 (Open Reading Frames in Random Sequence)** In random sequence with equal base frequencies, each codon is one of the three stop codons with probability $3/64$, independently. The length $K$, in codons, of an ORF (the run between two stops in one frame) is geometric: $\mathbb{P}(K \ge k) = (61/64)^k$, with mean $61/3 \approx 20$ codons. A random sequence of $G$ base pairs contains in its six reading frames about $6 \cdot \frac{G}{3} \cdot \frac{3}{64}\,(61/64)^k = \frac{3G}{32}(61/64)^k$ ORFs of at least $k$ codons.

![ORF lengths in random sequence (Formula 14.3.1). A: the fraction of ORFs (stop to stop) longer than k codons in 3 Mb of random sequence in all six frames (circles) follows the geometric law (61/64)^k (line). B: the expected number of chance ORFs of at least k codons in a random sequence the size of the human genome; about 2.4 million exceed 100 codons and about 160 exceed 300 codons. In bacteria, without introns, an ORF of 100 codons is a good candidate gene; in humans, coding exons average only about 50 codons (dotted line), so exons cannot be recognized by length alone](./plots/orf-lengths.py)

In a bacterial genome of $5\,\mathrm{Mb}$, Formula 14.3.1 predicts about $3\,900$ chance ORFs of 100 codons or more and only about $350$ of 150 codons, against about $4\,500$ real genes with a median length of about 300 codons, so a scan for long ORFs finds most bacterial genes. In vertebrates the method fails: coding exons are short, separated by introns that average several kilobases, and genes occupy about $40\,\%$ of the genome while coding sequence is only about $1.2\,\%$. Gene finders therefore combine several kinds of evidence.

- Signals of gene structure: splice donor and acceptor consensus sequences, start and stop codons, polyadenylation signals, CpG islands near promoters.
- Codon bias: each species uses its synonymous codons (**synonymous codon**, [7.2.19](/7.2.19)) with characteristic frequencies, which correlate with the abundance of the corresponding tRNAs, most strongly in highly expressed genes. A predicted ORF whose codon usage matches the species' pattern is more likely to be a real gene.
- Conservation (14.3.2).
- Transcripts (14.3.3).

### 14.3.2. Conservation Reveals Function

Functional sequences evolve more slowly than nonfunctional ones, because most mutations in them are harmful and are removed by selection (purifying selection, [7.4.23](/7.4.23)). A sequence that is similar in distant species is therefore probably functional. The similarity is not chance: for two unrelated random sequences, a particular 50 bp segment matches exactly with probability $(1/4)^{50} \approx 8 \times 10^{-31}$; the statistics of similarity scores in database searches are in 14.5. Comparisons of 240 mammalian genomes (the Zoonomia project, 2023) found that about $10\,\%$ of the human genome is evolutionarily constrained, roughly eight times the coding fraction: most constrained bases lie outside exons, in enhancers, promoters and noncoding RNA genes. Conservation is also the strongest single predictor of the effect of a missense variant (14.11).

### 14.3.3. Transcripts and Alternative Splicing

The most direct evidence of a gene is its RNA. A **cDNA library** ([7.2.5](/7.2.5)) made from the mRNA of a tissue contains clones of the genes expressed there, in proportion to their expression, and without introns; aligning a cDNA (**complementary DNA**) to the genome reveals the exon–intron structure. Expressed sequence tags (ESTs), single reads from the 5′ or 3′ ends of many cDNA clones, were the first large-scale evidence of transcribed regions (1990s); RNA sequencing (RNA-seq) of many tissues, and long-read sequencing of full-length transcripts, have replaced them. Because cDNA libraries reflect expression, rare transcripts and genes expressed only in some cells are easily missed, and libraries from many tissues and developmental stages are needed.

**Alternative splicing** ([7.2.16](/7.2.16)) complicates annotation: about $95\,\%$ of human multi-exon genes produce more than one spliced isoform, so a gene is not one ORF but a set of transcripts. The current human annotation (GENCODE) lists about $20\,000$ protein-coding genes with on average about ten annotated transcripts each, and about as many long noncoding RNA genes, whose functions are mostly unknown.

## 14.4. Genome Architecture and Gene Families

### 14.4.1. The Human Genome in Numbers

The haploid human genome has about $3.1 \times 10^9$ base pairs ($3.06\,\mathrm{Gb}$ in the complete assembly) and about $20\,000$ protein-coding genes. The often quoted larger numbers, 27 000 or more, are older estimates that counted gene predictions without evidence; the number has fallen as annotation improved. Genes are not evenly spread: gene-rich regions such as 17q, 19 and the light G bands contrast with gene deserts of several megabases ([7.3.17](/7.3.17#sec-17.4.2)).

### 14.4.2. Gene Families and the Fates of Duplicates

**Definition 14.4.1 (Gene Family)** A **gene family** is a group of genes in a genome that are related in sequence, and usually in function, because they descend by duplication and divergence from a common ancestral gene. Members of a family in one genome are paralogs; the corresponding genes in different species, descended from one gene of their last common ancestor, are orthologs (both defined in [7.1.4](/7.1.4)).

Duplicates arise by unequal crossing over (Definition 15.3.1), by duplication of chromosome segments (segmental duplications, often by non-allelic homologous recombination), by retrotransposition of an mRNA (retrogenes, which lack introns), and by whole-genome duplication ([7.4.16](/7.4.16)). Immediately after a duplication, the two copies are redundant, and mutations that disable either one are neutral. Most duplicates are therefore lost, by deletion or by becoming a **pseudogene** ([7.2.2](/7.2.2#sec-2.2.5)); in humans the half-life of a duplicate is of the order of a few million years. The copies that are kept are kept for one of three reasons.

**Definition 14.4.2 (Neofunctionalization and Subfunctionalization)** After a gene duplication, **neofunctionalization** is the acquisition by one copy of a new function by mutation, while the other keeps the ancestral function. **Subfunctionalization** is the partition of the ancestral functions between the copies, each losing by complementary degenerative mutations some of the functions (for example some of the tissue-specific enhancers) that the other retains, so that both become necessary. Copies may also be kept simply because more product is useful (dosage selection), as for histone and rRNA genes, or because losing one would upset the balance of a complex (dosage balance, Definition 16.2.3).

Subfunctionalization (the duplication–degeneration–complementation model of Force and Lynch, 1999) explains why so many duplicates survive without obvious new functions: if a gene has several independent regulatory modules, each copy losing a different module is a likely outcome of neutral mutations, and once that has happened both copies are needed. The two zebrafish *engrailed-1* genes, which divided the expression domains of the single mouse gene between them, were the first example. Neofunctionalization is rarer but more consequential: the antifreeze glycoprotein of Antarctic fish arose from a duplicated trypsinogen gene, and the visual opsins of primates gained trichromatic vision by duplication of the X-linked opsin gene ([7.4.13](/7.4.13#sec-13.5)).

**Example 14.4.1 (The Globin Genes)** The globins that carry oxygen in red cells form two clusters. The α-like genes lie on 16p13.3 and the β-like genes on 11p15.4; the two families derive from a duplication of an ancestral globin gene about 450 million years ago, followed by separation onto different chromosomes, and myoglobin and the neuroglobin and cytoglobin genes are older relatives. Each cluster then expanded by tandem duplication: the β cluster contains the embryonic ε, two fetal γ genes ($^{\mathrm{G}}\gamma$ and $^{\mathrm{A}}\gamma$, which differ at one codon and arose by a duplication about 35 million years ago in primates), the pseudogene ψβ, and the adult δ and β genes. The genes are arranged in the order of their expression in development, from 5′ (embryonic) to 3′ (adult), and are controlled by a shared upstream locus control region ([7.2.15](/7.2.15)). Unequal crossing over between the duplicated α genes is the main cause of α-thalassemia (deletion of one or both α genes on a chromosome), and between δ and β it produces δβ fusion genes (hemoglobin Lepore).

![The human globin gene clusters (schematic, not to scale). The α-like cluster on chromosome 16 and the β-like cluster on chromosome 11, with their upstream regulatory regions (MCS-R2 and the locus control region), genes colored by the stage at which they are expressed; ψ marks pseudogenes. In both clusters the order of genes from 5′ to 3′ matches the order of their expression in development. The hemoglobin tetramers of each stage are listed below](./plots/globin-clusters.py)

### 14.4.3. De Novo Genes

Not every gene comes from an older gene.

**Definition 14.4.3 (De Novo Gene)** A **de novo gene** is a gene that has arisen from previously noncoding sequence, by acquiring transcription and an open reading frame, rather than by duplication of an existing gene; it has no homologs outside a group of closely related species.

Comparative genomics of yeasts, flies and primates has found tens to hundreds of such genes per lineage; they are typically short, with few exons, expressed at low levels and often in the testis. The steps can be reconstructed by comparing orthologous noncoding sequences in related species: a region becomes transcribed (perhaps through a nearby transposon-derived promoter), and a random ORF in the transcript gains a start codon or loses a stop. Formula 14.3.1 explains why most de novo proteins are small: random ORFs are short. Many genes without detectable homologs ("orphan genes") are, however, old genes that have diverged beyond recognition. The sex-determining gene *csd* of honey bees ([7.4.6](/7.4.6)) shows the other route to a new gene: it arose by duplication of the gene *feminizer* (*fem*) in the lineage of *Apis* and evolved rapidly into a gene with a new function, not de novo.

### 14.4.4. Synteny

**Definition 14.4.4 (Synteny)** Two loci are **syntenic** if they lie on the same chromosome. In comparative genomics, *conserved synteny* refers to blocks of genes that lie together, and usually in the same order (collinearity), in the genomes of different species, because they descend from one ancestral chromosome segment.

Human and mouse genomes can be cut into about 300 conserved blocks, separated by the breakpoints of rearrangements that occurred in the two lineages since their common ancestor about 90 million years ago ([7.4.15](/7.4.15#sec-15.6)). Conserved synteny identifies orthologs among paralogs and lets a gene mapped in one species be found in another: a disease gene mapped to a human region suggests candidate genes from the syntenic mouse region, and vice versa.

## 14.5. Tools: Similarity Searches and Genome Browsers

The basic tool of genome analysis is the search for sequences similar to a query. BLAST (Basic Local Alignment Search Tool, Altschul and colleagues, 1990) finds local alignments quickly by starting from short exact word matches and extending them; the algorithm is described in [7.8](/7.8). Its output is useful only with a measure of how likely the similarity is to arise by chance.

**Formula 14.5.1 (Expected Number of Chance Hits)** For a query of length $m$ searched against a database of total length $n$, the expected number of distinct local alignments with score at least $S$ between unrelated random sequences is

$$
E = K m n\,\mathrm{e}^{-\lambda S},
$$
where $K$ and $\lambda$ depend on the scoring system and the residue frequencies (Karlin and Altschul, 1990). The number of chance hits with score at least $S$ is approximately Poisson with mean $E$, so the probability of at least one such hit is $1 - \mathrm{e}^{-E}$, close to $E$ when $E$ is small.

The $E$-value depends on the size of the database: the same alignment is more significant in a small database than in a large one. Since the score needed for a given $E$ grows only logarithmically with $mn$, $S = \lambda^{-1}\ln(Kmn/E)$, searches remain sensitive as databases grow. A hit with $E < 10^{-5}$ is usually taken as evidence of homology (common descent); homology itself is a yes-or-no statement, and "percent homology" is a misnomer for percent identity.

Genome browsers (the UCSC Genome Browser, Ensembl, and species databases such as FlyBase) display the reference sequence with tracks for gene models, transcripts, conservation, variants and regulatory data, and are the usual place where the information of this chapter is combined.

## 14.6. Ancient DNA

DNA survives in bones for tens of thousands of years in cold conditions, but degraded into fragments of about 40–60 base pairs and chemically damaged: cytosines at the single-stranded ends of fragments are deaminated to uracil, which is read as thymine, so that ancient sequences show an excess of C→T differences near their 5′ ends. This damage pattern, together with short fragment length, distinguishes authentic ancient DNA from modern contamination, which in bone samples is usually overwhelmingly bacterial and human. Svante Pääbo and his colleagues began with mitochondrial DNA, present in thousands of copies per cell (1997, Neanderthal), developed clean-room and library methods for single damaged molecules, and published a draft Neanderthal genome in 2010. The same year, a genome from a finger bone found in Denisova Cave revealed a previously unknown group of archaic humans, the Denisovans. Comparisons showed that people outside Africa carry about $2\,\%$ Neanderthal DNA from interbreeding about 50 000–60 000 years ago, and that people of Oceania carry several percent of Denisovan DNA; some introgressed alleles were favored by selection, such as an *EPAS1* haplotype of Denisovan origin that helps Tibetans live at high altitude. Pääbo received the Nobel Prize in 2022. The population genetics of human ancestry is continued in [7.4.23](/7.4.23).

## 14.7. Genomic Variation

### 14.7.1. Classes of Variants

Any two human genomes differ at about one site in 1 000 to 1 500 base pairs. A variant at which two or more alleles are each present at an appreciable frequency in a population is a **genetic polymorphism** ([7.4.3](/7.4.3)); the term is often used for all variants regardless of frequency.

**Definition 14.7.1 (Classes of Genomic Variants)** A **single nucleotide polymorphism** (SNP; single nucleotide variant when rare) is a variant at a single base pair. An **indel** (deletion–insertion polymorphism, DIP) is the insertion or deletion of a short sequence, from one to about 50 base pairs. A **short tandem repeat** polymorphism varies in the number of tandem copies of a unit of 1–6 base pairs (a microsatellite, [7.2.2](/7.2.2#sec-2.2.3); simple sequence repeat, SSR). A **copy-number variant** (CNV) varies in the number of copies of a segment of more than about $1\,\mathrm{kb}$, and a **structural variant** (SV) is any variant of more than about 50 base pairs, including CNVs, inversions, translocations and insertions of transposable elements.

![Classes of DNA sequence variants (schematic). A: a single-nucleotide polymorphism, T in the reference and in haplotype 1, C in haplotype 2. B: an indel, here a deletion of three bases. C: a short tandem repeat (CAT)n with three units in the reference, six in haplotype 1 and two in haplotype 2. D: a copy-number variant of a larger segment C (0, 1 or 2 copies per haplotype), created by unequal crossing over or non-allelic homologous recombination](./plots/variant-types.py)

| Class | Number in one genome (relative to the reference) | Main origin | Typical mutation rate |
|---|---|---|---|
| SNPs | about 4–5 million | replication errors, deamination, damage | $1.2 \times 10^{-8}$ per bp per generation |
| Short indels | about 0.5–0.6 million | slippage, repair | about $10^{-9}$ per bp per generation |
| Short tandem repeats | variable at tens of thousands of loci | replication slippage | $10^{-4}$–$10^{-3}$ per locus per generation |
| Structural variants and CNVs | about 2 000–25 000 (depending on method), affecting $10$–$20\,\mathrm{Mb}$ | NAHR, end joining, retrotransposition | about $10^{-2}$ new SVs per genome per generation (many kinds) |

The numbers are from the 1000 Genomes Project (2015) and long-read studies; the larger SV numbers come from long-read sequencing, which detects many insertions and repeat-mediated variants invisible to short reads. A general rule holds: the smaller the variant, the more numerous its class, but the larger classes affect more base pairs in total. Only a small fraction of variants affect phenotype; a typical genome has about $10\,000$ variants that change amino acids and about 100–200 that truncate proteins, mostly in one copy and in nonessential genes. Most SNPs are biallelic, because the mutation rate per base is so low that the same site rarely mutates twice in the history of a population; each SNP therefore records one mutation in one ancestral genome. Comparison with the chimpanzee identifies the ancestral allele (the one shared with chimpanzees) and the derived allele.

Copy-number variation affects whole genes. The olfactory receptor genes, the largest gene family of mammals (about 400 functional genes and as many pseudogenes in humans), vary greatly in copy number and in the presence of intact alleles, which explains part of the variation in people's ability to smell particular odors. The amylase gene *AMY1* varies from 2 to 15 copies per diploid genome, and populations with starch-rich diets have more copies on average.

### 14.7.2. Variants as Markers

Most variants are anonymous: they have no effect, but they are inherited in Mendelian fashion and their positions are known. They are ideal genetic markers. SNPs are the most numerous and easiest to type in large numbers, but have only two alleles; STRs have many alleles and high heterozygosity, so that almost every meiosis is informative for them (14.9), at the cost of a high mutation rate. The large majority of variants of all classes are anonymous signposts, and the challenge of human genetics is to find, among millions of them, the few that matter for a disease or trait; the opportunity is that the anonymous ones mark where to look.

## 14.8. Detecting Variants

### 14.8.1. Genotyping

**Definition 14.8.1 (Genotyping)** **Genotyping** is the determination of the alleles present at specific variable sites of an individual's genome.

Methods match the class of variant. Indels and STRs change the length of a PCR product (**polymerase chain reaction**) and are typed by electrophoresis; SNPs are typed by sequencing the PCR product, by allele-specific hybridization or by primer extension. Genotyping arrays carry hundreds of thousands to millions of allele-specific oligonucleotides (20–40 bases) attached to a surface; under stringent conditions a probe hybridizes to only one allele, and the ratio of the fluorescent signals from the probes for the two alleles gives the genotype. Arrays are cheap enough to genotype millions of people (the basis of genome-wide association studies, [7.4.25](/7.4.25), and of consumer genomics); their intensities also detect CNVs. Exome and genome sequencing detect all classes of variant at once, at a higher cost ([7.2.6](/7.2.6)).

### 14.8.2. DNA Fingerprinting

**Definition 14.8.2 (DNA Fingerprinting)** **DNA fingerprinting** (DNA profiling) is the identification of individuals, or of their relatives, from their genotypes at a set of highly polymorphic loci, usually short tandem repeats.

The first DNA fingerprints (Alec Jeffreys, 1985) used minisatellites detected by Southern blotting. Forensic profiles now use multiplex PCR of STR loci with tetranucleotide repeats: the primers for each locus are labeled with fluorescent dyes of different colors, the products of all loci are separated in one capillary, and the size of each product gives the number of repeat units. The United States database (CODIS) used 13 core loci until 2017 and 20 since; most countries use similar sets.

![A simulated multiplex STR profile of two people at four loci, typed in one capillary with two dye colors. Each person has one peak per locus if homozygous (vWA 16/16 in person 1, FGA 22/22 in person 2, twice the height) and two if heterozygous; alleles are named by the number of repeat units and differ by 4 bp. The small peaks one repeat unit shorter are stutter products of polymerase slippage during PCR](./plots/str-electropherogram.py)

The power of a profile comes from multiplying many small probabilities. If two unrelated people share the genotype at one locus with probability about $0.1$, and the loci are unlinked and their genotypes independent, they share all 13 with probability $10^{-13}$, much less than one over the number of people alive. The calculation of the match probability from allele frequencies under Hardy–Weinberg proportions, with corrections for population structure and relatives, is in [7.4.22](/7.4.22). Relatives share alleles **identical by descent** ([7.4.7](/7.4.7)) and match much more often, which is how familial searching and the identification of remains by relatives work.

### 14.8.3. Preimplantation Genetic Diagnosis

**Definition 14.8.3 (Preimplantation Genetic Diagnosis)** **Preimplantation genetic diagnosis** (preimplantation genetic testing, PGT) is the genotyping of one or a few cells removed from embryos produced by in vitro fertilization, or of polar bodies ([7.4.5](/7.4.5#sec-5.6)), in order to transfer only embryos without a familial mutation (PGT-M), without an unbalanced rearrangement (PGT-SR, [7.4.15](/7.4.15)) or without aneuploidy (PGT-A, [7.4.16](/7.4.16)).

The main technical risk is that amplification from a single cell fails for one allele (allele dropout), so a heterozygous embryo appears homozygous. Typing linked markers on both sides of the mutation, with known phase in the family, guards against it: the marker **haplotypes** reveal which parental chromosome the embryo received even if the mutation itself drops out.

**Example 14.8.1** A man heterozygous for the dominant Huntington disease allele and his partner undergo PGT-M. An embryo has prior probability $1/2$ of carrying the allele. Testing one cell, the mutant allele is detected if present except for allele dropout, with probability $0.05$. If the test shows no mutant allele, by **Bayes' theorem** the probability that the embryo nevertheless carries it is

$$
\frac{\frac12 \cdot 0.05}{\frac12 \cdot 0.05 + \frac12 \cdot 1} = \frac{0.05}{1.05} \approx 0.048.
$$
Adding two linked markers with known phase, each with independent dropout probability $0.05$ and no recombination with the mutation, an embryo is misclassified only if the mutation and both markers drop out for the same chromosome: $0.05^3 \approx 1.3 \times 10^{-4}$, ignoring recombination. With recombination between a marker and the gene at frequency $r$, the markers on both sides make a misdiagnosis require a double recombinant or coincident dropouts.

## 14.9. Linkage Analysis in Human Families: The LOD Score

### 14.9.1. Informative Meioses and Phase

In experimental organisms, the recombination frequency between two loci is measured with a testcross. In humans, the geneticist must use the families that exist. The idea is the same as in [7.4.8](/7.4.8): follow one locus by the disease phenotype and the other by genotyping a marker, and count how often the two are separated in a meiosis. Two complications arise: not every meiosis can be scored, and the phase of the parent is often unknown.

**Definition 14.9.1 (Informative Meiosis and Phase)** A meiosis is an **informative meiosis** for linkage between two loci if the parent in whom it occurs is heterozygous at both loci and the offspring's genotype reveals which allele at each locus was transmitted, so that the offspring can be classified as parental or recombinant. The **linkage phase** (or simply phase) of a double heterozygote is the arrangement of its alleles on its two homologues (coupling or repulsion, [7.4.8](/7.4.8)); it is known if it can be inferred from the genotypes of the parent's own parents, and unknown otherwise.

A meiosis of a parent homozygous at the marker is uninformative, because every child receives the same marker allele; a child of two parents with the same heterozygous genotype ($1/2 \times 1/2$) is uninformative if it is also $1/2$, because either parent could have given either allele. Markers with many alleles (STRs) are therefore more useful in small families than SNPs. In the pedigree below, the phase of the affected father is known from his own father, and his wife is homozygous at the marker, so every meiosis in the father is informative.

![A dominant disease (fully penetrant) segregating with a two-allele SNP. The affected father (II-1) received the disease allele together with marker allele G from his affected father, so his phase is known: disease with G, normal with T. His wife is T/T, so the allele each child received from him is known. Seven children are parental (affected with G, or unaffected with T) and one (III-8, unaffected with G) is recombinant, which gives a LOD score of 1.10 at θ = 1/8](./plots/marker-pedigree.py)

### 14.9.2. The LOD Score

**Definition 14.9.2 (LOD Score)** For a pedigree and a recombination fraction $\theta$ between two loci, the **LOD score** (logarithm of the odds) is

$$
Z(\theta) = \log_{10}\frac{\mathbb{P}(\text{pedigree data} \mid \theta)}{\mathbb{P}(\text{pedigree data} \mid \theta = \tfrac12)},
$$
the decimal logarithm of the likelihood ratio ([3.2.5](/3.2.5)) of linkage at $\theta$ against no linkage.

**Formula 14.9.1 (LOD Score with Known Phase)** If a pedigree contains $n$ informative meioses of known phase, of which $R$ are recombinant, then

$$
Z(\theta) = \log_{10}\frac{\theta^{R}(1 - \theta)^{n - R}}{(1/2)^{n}},
$$
which is maximized at $\hat\theta = R/n$, the **maximum likelihood estimation** of the recombination fraction ([3.2.3](/3.2.3)).

**Proof** Given the phase, each informative meiosis is recombinant with probability $\theta$ and parental with probability $1 - \theta$, independently, so the likelihood is $\theta^R(1 - \theta)^{n-R}$, and under no linkage $(1/2)^n$. The derivative of $R\ln\theta + (n - R)\ln(1 - \theta)$ vanishes at $\theta = R/n$. $\square$

**Example 14.9.1** For the pedigree above, eight meioses, the sequence of children P P P P P P P R: $Z(\theta) = \log_{10}\bigl[\theta(1 - \theta)^7 \cdot 2^8\bigr]$. At $\hat\theta = 1/8$, $Z = \log_{10}\bigl[0.125 \times 0.875^7 \times 256\bigr] = \log_{10} 12.6 = 1.10$; at $\theta = 0.05$ it is $0.95$, at $\theta = 0.2$ it is $1.03$. The data are about 13 times more likely under linkage at $\theta = 1/8$ than under independent assortment: suggestive, not conclusive.

**Formula 14.9.2 (LOD Score with Unknown Phase)** If the phase of the doubly heterozygous parent is unknown and the two phases are equally likely a priori, then for $n$ informative meioses of which $k$ are of one type and $n - k$ of the other,

$$
Z(\theta) = \log_{10}\frac{\tfrac12\bigl[\theta^{k}(1 - \theta)^{n - k} + \theta^{n - k}(1 - \theta)^{k}\bigr]}{(1/2)^{n}}.
$$

**Proof** By the **law of total probability** over the two phases: under one phase the $k$ children of one type are recombinant, under the other the $n - k$ children of the other type are. Without linkage the phase does not matter. $\square$

Unknown phase costs information: a sibship of six children all of one type gives, at $\theta = 0$, $Z = \log_{10}(\frac12 \cdot 2^6) = 1.51$ instead of $\log_{10}2^6 = 1.81$. For complex pedigrees, with unknown genotypes, several generations and incomplete penetrance, the likelihood is computed by summing over all possible genotypes of all individuals (the Elston–Stewart and Lander–Green algorithms, implemented in linkage software); the logic is that of Formulas 14.9.1 and 14.9.2.

### 14.9.3. Combining Families and the Threshold of 3

Because families are independent, their likelihoods multiply and their LOD scores add: $Z(\theta) = \sum_j Z_j(\theta)$. This is what made human linkage mapping possible, since most families are too small to establish linkage alone.

![LOD score curves (Formulas 14.9.1, 14.9.2). Family 1: phase known, 1 recombinant in 8 meioses. Family 2: phase unknown, 6 meioses all of one type. Family 3: phase known, 1 recombinant in 10. No family alone reaches the threshold of 3, but their sum does, with a maximum near θ = 0.08; values below −2 exclude linkage at the corresponding θ](./plots/lod-curves.py)

By convention, linkage is accepted if the maximum LOD score is at least $3$, and rejected for values of $\theta$ at which $Z(\theta) \le -2$. The threshold of 3 is much stricter than the $p < 0.05$ of a single test, for a Bayesian reason.

**Proposition 14.9.1 (Why a LOD of 3)** Let the prior probability that a random marker is linked to a disease gene (within measurable distance) be $\pi$; for the human genome, with 22 autosomes of total genetic length about 35 morgans, $\pi \approx 1/50$. If the data give a likelihood ratio $10^{Z}$ for linkage, the posterior probability of linkage is

$$
\mathbb{P}(\text{linked} \mid \text{data}) = \frac{\pi\,10^{Z}}{\pi\,10^{Z} + 1 - \pi}.
$$
For $Z = 3$ and $\pi = 1/50$ this is about $0.95$; for $Z = 2$, only about $0.67$.

**Proof** By Bayes' theorem in odds form, posterior odds = prior odds × likelihood ratio $= \frac{\pi}{1-\pi}\,10^Z$; for $\pi = 0.02$ and $Z = 3$ the posterior odds are $1000/49 \approx 20$, a probability of $0.953$. $\square$

A LOD of 3 thus corresponds to a false-positive rate of about $5\,\%$ among declared linkages, the analog of $p = 0.05$ after correcting for the low prior; the statistical framework is that of [3.2.5](/3.2.5) and, in its Bayesian form, of [3.4](/3.4). In a genome-wide scan with many markers the threshold for significant linkage is usually set at $3.3$ for this reason.

**Example 14.9.2 (Huntington Disease)** In 1983 James Gusella, Nancy Wexler and colleagues typed restriction fragment length polymorphisms in a large Venezuelan kindred and an American family with Huntington disease. The twelfth marker they tried, G8, gave a maximum LOD score above 8 at $\theta \approx 0$ on chromosome 4p: the first human disease gene mapped with an anonymous DNA marker, by remarkable luck. It took ten more years to identify the gene, *HTT*, and its CAG expansion ([7.4.12](/7.4.12#sec-12.6)), by positional cloning.

## 14.10. Positional Cloning

**Definition 14.10.1 (Positional Cloning and Candidate Gene)** **Positional cloning** is the identification of a gene from its chromosomal position, determined by linkage, without prior knowledge of its product: the gene is localized by linkage to markers, the region is narrowed by recombinants and other evidence, the genes in it are identified, and the causal one is proven by finding mutations in patients. A **candidate gene** is a gene whose position or known function makes it a plausible cause of a phenotype.

**Algorithm 14.10.1 (Positional Cloning)**
1. Collect families in which the disease segregates and confirm the mode of inheritance ([7.4.7](/7.4.7)).
2. Genotype markers across the genome and compute LOD scores (Formulas 14.9.1, 14.9.2); a maximum $Z \ge 3$ localizes the gene to an interval of typically $10$–$20\,\mathrm{cM}$.
3. Narrow the interval with more markers and families: the closest recombinants on each side define the minimal region; **linkage disequilibrium** with a common founder mutation ([7.4.22](/7.4.22)) and chromosomal rearrangements in rare patients can narrow it further.
4. List the genes in the region (formerly by cloning and cDNA selection, now from the annotated genome, 14.3), prioritizing candidates by expression in the affected tissue and by function.
5. Sequence the candidates in patients and controls; the causal gene carries mutations that segregate with the disease, are absent from unaffected people, and are predicted or shown to disrupt function, and independent mutations are found in unrelated families (allelic heterogeneity).
6. Confirm by functional tests or animal models.

The cystic fibrosis gene *CFTR* was found this way in 1989 (Tsui, Riordan, Collins and colleagues): linkage to markers on 7q31 (1985), a region of about $500\,\mathrm{kb}$ narrowed by recombinants and linkage disequilibrium, cloned by chromosome walking and jumping, with a three-base deletion in exon 10 (p.Phe508del, about $70\,\%$ of the mutant alleles in Europeans) in a gene expressed in sweat glands and lungs and encoding a chloride channel. The neurofibromatosis type 1 gene *NF1* on 17q11.2 (1990) was found faster because two patients carried balanced translocations with breakpoints in the gene. The approach found about 100 disease genes by 1995 and several thousand since.

Positional cloning has limits. Linkage needs families with several affected members and meioses informative at the markers, so it fails for diseases that are rarely inherited (lethal or sterile phenotypes, most new dominant mutations) and for complex traits, where many genes each have small effects and LOD scores are low ([7.4.25](/7.4.25)). Genetic heterogeneity, the same phenotype caused by different genes in different families (**genetic heterogeneity**, [7.4.4](/7.4.4)), adds positive LOD scores from linked families to negative ones from unlinked families and can hide linkage entirely; tests allowing for a proportion of linked families (the HLOD) address this.

## 14.11. Mendelian Disease in the Sequencing Era

**Definition 14.11.1 (Exome Sequencing)** **Exome sequencing** is the sequencing of the protein-coding exons of a genome (about $1$–$2\,\%$ of it, some $30$–$60\,\mathrm{Mb}$ with flanking sequence), captured from fragmented genomic DNA by hybridization to probes before sequencing.

Since about 2010, exome and genome sequencing have replaced positional cloning for most Mendelian diseases. Instead of locating the gene by recombination, the analysis sequences every gene of a patient and filters the variants by frequency, predicted effect and inheritance. About half of the protein-coding genes known to cause Mendelian diseases have been found this way, and in children with severe undiagnosed conditions exome or genome sequencing gives a molecular diagnosis in about $25$–$40\,\%$ of cases.

![Filtering the variants of a patient to find the cause of a rare Mendelian disease (typical numbers for one individual; they depend on ancestry, capture and filters). Each step removes variants that cannot explain the disease: noncoding variants (in a first pass), variants common in the population, variants that do not change the protein, and variants inconsistent with the inheritance in the family; the few remaining candidates are judged by the match between the gene and the phenotype and by functional and replication evidence](./plots/variant-filtering.py)

Two designs are especially powerful.

- Trios. For sporadic severe disorders, which are often caused by new dominant mutations, the patient and both parents are sequenced. Each person carries about 60–80 new single-nucleotide mutations (at $1.2 \times 10^{-8}$ per base pair per generation over $6.2 \times 10^9$ base pairs; most from the father, [7.4.12](/7.4.12#sec-12.5)), of which on average about one falls in a coding exon; a damaging new mutation in a gene already linked to similar disorders is then very likely causal. Developmental disorders were found to be mostly due to such mutations (the Deciphering Developmental Disorders study, 2017).
- Families and consanguinity. In a recessive disease of a consanguineous family, the causal variant lies in a long run of homozygosity shared by the affected children, which combines the logic of positional cloning (homozygosity mapping) with sequencing.

The interpretation of variants is the hard part. A variant is classified by the guidelines of the American College of Medical Genetics and Genomics (2015) into five categories, pathogenic, likely pathogenic, of uncertain significance, likely benign and benign, by combining population frequency (a variant too common for the disease's prevalence cannot cause it), segregation in families, de novo occurrence, computational predictions, functional data and the prior knowledge about the gene. Many variants remain of uncertain significance; systematic functional assays of every possible variant in a gene (saturation genome editing, [7.4.19](/7.4.19)) are now resolving them gene by gene.

## Summary

| Topic | Tool | Key formula or number |
|---|---|---|
| Assembly (14.2) | shotgun reads, contigs, scaffolds (Definition 14.2.1) | uncovered $\mathrm{e}^{-c}$; contigs $N\mathrm{e}^{-c\sigma}$ (Formula 14.2.1); repeats limit assembly; T2T 2022; pangenome (Definition 14.2.2) |
| Annotation (14.3) | ORFs, codon bias, conservation, cDNA/RNA-seq | random ORF length geometric, $\mathbb{P}(K \ge k) = (61/64)^k$ (Formula 14.3.1); about $20\,000$ protein-coding genes |
| Gene families (14.4) | duplication and divergence (Definition 14.4.1) | fates: loss, neofunctionalization, subfunctionalization (Definition 14.4.2); globins (Example 14.4.1); de novo genes (Definition 14.4.3); synteny (Definition 14.4.4) |
| Similarity (14.5) | BLAST | $E = Kmn\,\mathrm{e}^{-\lambda S}$ (Formula 14.5.1) |
| Variation (14.7) | SNP, indel, STR, CNV, SV (Definition 14.7.1) | 4–5 million SNPs per genome; smaller classes more numerous |
| Detection (14.8) | genotyping, fingerprinting, PGT (Definitions 14.8.1–14.8.3) | match probability $\prod_i p_i$; dropout and Bayes (Example 14.8.1) |
| Linkage (14.9) | LOD score (Definition 14.9.2) | phase known $\log_{10}[\theta^R(1-\theta)^{n-R}2^n]$ (Formula 14.9.1); phase unknown (Formula 14.9.2); add across families; $Z \ge 3$ ≈ posterior $0.95$ (Proposition 14.9.1); $Z \le -2$ excludes |
| Positional cloning (14.10) | linkage → interval → candidates → mutations (Algorithm 14.10.1) | HD (1983/1993), CF (1989), NF1 (1990) |
| Sequencing era (14.11) | exome/genome (Definition 14.11.1), trios, filtering | about one coding de novo mutation per person; ACMG five classes |

## Questions

1. A $5\,\mathrm{Mb}$ bacterial genome is sequenced with $150$-base reads at $8\times$ coverage; reads are joined if they overlap by $30$ bases or more. Use Formula 14.2.1 to estimate (a) the number of reads, (b) the number of uncovered bases, (c) the number of contigs. (d) Why do real assemblies at $100\times$ still have tens of contigs?

   **Answer** (a) $N = cG/L = 8 \times 5 \times 10^6/150 \approx 2.67 \times 10^5$. (b) $G\mathrm{e}^{-8} \approx 5 \times 10^6 \times 3.35 \times 10^{-4} \approx 1\,700$ bases. (c) $\sigma = 0.8$, $N\mathrm{e}^{-6.4} \approx 2.67 \times 10^5 \times 1.66 \times 10^{-3} \approx 440$. (d) Repeats longer than the reads (rRNA operons of about $5\,\mathrm{kb}$, IS elements) cannot be resolved by overlaps, whatever the coverage; long reads that span them close the assembly.
2. How many ORFs of at least 150 codons are expected by chance in the six frames of a random $5\,\mathrm{Mb}$ sequence with equal base frequencies? Real bacterial genes average about 300 codons. Would an ORF of 80 codons be a convincing gene prediction?

   **Answer** $\frac{3G}{32}(61/64)^{150} = 4.69 \times 10^5 \times 7.46 \times 10^{-4} \approx 350$. For $k = 80$, $(61/64)^{80} = 0.0215$, giving about $10\,000$ chance ORFs, more than the number of real genes, so length alone is not convincing; codon usage, a ribosome-binding site, conservation in related species or transcript and protein evidence are needed.
3. Explain why the number of contigs in Formula 14.2.1 first rises and then falls as coverage increases, and find the coverage at which it is largest for $\sigma = 0.9$.

   **Answer** At low coverage most reads are isolated, so each new read adds a contig; at higher coverage new reads mostly join existing contigs and close gaps, and the probability that a read ends a contig, $\mathrm{e}^{-c\sigma}$, falls exponentially. The product $c\,\mathrm{e}^{-c\sigma}$ is largest at $c = 1/\sigma = 1.11$.
4. With $K = 0.1$ and $\lambda = 0.3$ (per score unit), a query of 300 residues is searched against a database of $10^9$ residues. What score is needed for $E = 10^{-3}$? By how much must the score rise if the database grows tenfold?

   **Answer** $S = \lambda^{-1}\ln(Kmn/E) = \ln(3 \times 10^{10}/10^{-3})/0.3 = \ln(3 \times 10^{13})/0.3 = 31.03/0.3 \approx 103$. A tenfold larger database adds $\ln 10/\lambda = 7.7$ score units.
5. In a family with a dominant disease, the affected father's phase is known; of 10 informative meioses, 2 are recombinant. Compute $\hat\theta$ and $Z(\hat\theta)$, and $Z(0.1)$.

   **Answer** $\hat\theta = 0.2$. $Z(0.2) = \log_{10}[0.2^2 \times 0.8^8 \times 2^{10}] = \log_{10}(0.04 \times 0.1678 \times 1024) = \log_{10}6.87 = 0.84$. $Z(0.1) = \log_{10}[0.01 \times 0.9^8 \times 1024] = \log_{10}4.41 = 0.64$.
6. A dominant disease is studied in families with two-generation pedigrees: an affected parent of unknown phase and five children, all informative. In each family all five children are of one type (all affected children have one marker allele, all unaffected the other). How many such families are needed to exceed a LOD of 3 at $\theta = 0$?

   **Answer** Each family gives $Z(0) = \log_{10}(\frac12 \cdot 2^5) = \log_{10}16 = 1.20$ (Formula 14.9.2). Two families give $2.41$, three give $3.61$: three families are needed. With known phase, each would give $\log_{10}32 = 1.51$, and two would suffice.
7. Using Proposition 14.9.1 with a prior probability of linkage of $1/50$, compute the posterior probability of linkage for $Z = 2$, $Z = 3$ and $Z = 4$. Why is the conventional threshold for X-linked loci lower (about 2)?

   **Answer** Posterior odds $= 10^Z/49$: $Z = 2$: $100/49 = 2.04$, probability $0.67$; $Z = 3$: $20.4$, $0.953$; $Z = 4$: $204$, $0.995$. For a disease known to be X-linked, the prior probability that a random X marker is linked is much higher (the X is only about 1.8 morgans long in females, so $\pi$ is roughly $1/4$–$1/5$), so a smaller likelihood ratio gives the same posterior.
8. In a pedigree, the father is $1/2$ at an STR marker and affected with a dominant disease; the mother is $1/2$ too and unaffected. A child is $1/2$ and affected. Is this child informative for linkage in the father? What about a child who is $1/1$?

   **Answer** The $1/2$ child is not informative: it could have received $1$ from the father and $2$ from the mother or the reverse, so we do not know which paternal allele it got. The $1/1$ child received $1$ from each parent, so its paternal allele is known and the meiosis is informative (given the father's phase, it is parental or recombinant).
9. In a forensic case, the profile of a suspect matches a crime-scene sample at 20 unlinked STR loci, at each of which the genotype frequency in the population is about $0.05$. (a) What is the random match probability? (b) Why must the calculation be changed if the suspect has a brother who could also be the source?

   **Answer** (a) $0.05^{20} \approx 10^{-26}$. (b) Brothers share each parental allele identically by descent with probability $1/2$, so they have the same genotype at a locus with probability at least $1/4$ (both alleles IBD) plus chance matches; the match probability for a brother is roughly $(1/4 + \dots)^{20}$, about $10^{-10}$ or larger, far higher than for an unrelated person ([7.4.7](/7.4.7)).
10. An embryo of a couple at risk of a dominant disease (one parent heterozygous) tests negative for the mutation in a single-cell test with allele dropout probability $0.1$. What is the probability that the embryo carries the mutation? How does the result change if a linked marker with known phase and independent dropout probability $0.1$ also shows the normal haplotype (assume no recombination)?

    **Answer** One test: $\frac{0.5 \times 0.1}{0.5 \times 0.1 + 0.5} = 0.091$. With the marker: both must drop out, $0.1^2 = 0.01$; $\frac{0.5 \times 0.01}{0.5 \times 0.01 + 0.5} = 0.0099$, about $1\,\%$.
11. Estimate the expected number of new single-nucleotide mutations in a child's diploid genome, and how many fall in coding sequence, using a rate of $1.2 \times 10^{-8}$ per base pair per generation, a diploid genome of $6.2 \times 10^9$ base pairs and a coding fraction of $1.2\,\%$. How does a trio design use this number?

    **Answer** $1.2 \times 10^{-8} \times 6.2 \times 10^9 \approx 74$ new mutations, of which $74 \times 0.012 \approx 0.9$ are coding. Since a child has on average only about one coding de novo mutation, finding a damaging de novo mutation in a gene known to cause similar disorders is strong evidence: the chance of such a coincidence by accident is small, and recurrence of de novo mutations in the same gene in unrelated patients can be tested statistically against this background rate.
12. Two affected siblings with a rare recessive disease (nonconsanguineous parents) are exome-sequenced. In the first sibling, 20 genes carry two rare protein-altering variants each (possible compound heterozygotes). How many of these genes are expected also to be biallelic in the second sibling by chance? What does this filter assume?

    **Answer** At any locus, two siblings inherit the same pair of parental chromosomes with probability $1/4$. For the 19 genes that are not causal, about $19/4 \approx 5$ will also be biallelic in the second sibling, so with the true gene about 6 remain: sharing reduces the candidates about fourfold. The filter assumes full penetrance and the same cause in both siblings (no phenocopy or locus heterogeneity within the family), and that the variants in each gene are on different chromosomes (in trans), which parental genotypes can confirm.
13. Why does a duplicate gene whose ancestral version had two independent tissue-specific enhancers often end up with both copies retained, even though neither copy gains a new function?

    **Answer** After duplication the copies are redundant. A mutation destroying enhancer 1 in copy A and one destroying enhancer 2 in copy B are both neutral when they occur, but once both have happened, each copy is required in one tissue, so both are preserved by selection: subfunctionalization (Definition 14.4.2). The probability of this outcome is substantial when loss-of-function mutations in the regulatory modules are much more frequent than mutations that inactivate the coding sequence, because then the first copy to be fixed for a regulatory loss commits the other copy to keeping that module.
