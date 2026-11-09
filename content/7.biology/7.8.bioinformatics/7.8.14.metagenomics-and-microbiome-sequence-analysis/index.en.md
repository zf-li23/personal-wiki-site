---
title: Metagenomics and Microbiome Sequence Analysis
description: "Sequencing communities of microorganisms without culturing them. Amplicon sequencing of the 16S rRNA gene (hypervariable regions, primers, copy-number and primer biases); OTU clustering and amplicon sequence variants by denoising (the DADA2 error model and abundance p-value), chimeras, naive Bayes taxonomic classification and QIIME 2. Shotgun metagenomics: k-mer classification to the lowest common ancestor (Kraken 2, confidence scores), Bayesian re-estimation of abundance (Bracken), marker genes (MetaPhlAn) and the difference between read and cell abundance; metagenome assembly, binning by composition and differential coverage, metagenome-assembled genomes, CheckM completeness and contamination, MIMAG standards; functional profiles and resistance genes. Diversity: richness, Shannon, Simpson and Hill numbers, rarefaction and Chao1, Bray–Curtis, Jaccard and UniFrac, PCoA and PERMANOVA. Compositional data: closure, negative bias of correlations, log-ratios and the Aitchison distance, differential abundance and co-occurrence networks. Applications: clinical metagenomic diagnosis, contamination, the discovery of SARS-CoV-2 and wastewater surveillance."
---

Most microorganisms have never been grown in a laboratory, yet their DNA can be extracted from a gram of soil, a milliliter of seawater or a stool sample and sequenced directly. *Metagenomics* turns the questions of microbial ecology and infectious disease, which organisms are present, in what proportions, with which genes, and how communities differ between conditions, into problems of sequence analysis. Its methods are the linear-structure methods of this course applied to mixtures: classification of reads by alignment-free $k$-mer matching and naive Bayes models, phylogenetic placement on the **phylogenetic tree** of the 16S rRNA gene ([7.8.6](/7.8.6#sec-6.8.1)), assembly of many genomes at once ([7.8.11](/7.8.11)) and their separation by sequence composition ([7.8.7](/7.8.7#sec-7.1.2)). What is new is the statistics of the result: counts of taxa in a sample are relative, not absolute, and the analysis of such *compositional* data has its own pitfalls. The chapter treats amplicon sequencing, shotgun metagenomics, diversity, compositional data analysis and applications to diagnosis and surveillance. The biology of microorganisms and their communities belongs to microbiology ([7.11](/7.11)) and ecology ([7.19](/7.19)); count models and multiple testing are in [7.7.20](/7.7.20), multivariate ordination in [3.4.6](/3.4.6), and the integration of microbiome data with other omics and networks in systems biology ([7.9.1](/7.9.1)).

## 14.1. Microbial Communities and Their Sequences

### 14.1.1. Two Kinds of Data

**Definition 14.1.1 (Metagenomics and Microbiome)** **Metagenomics** is the study of the genetic material recovered directly from an environmental or host-associated sample, containing many organisms, without isolating and culturing them. The **microbiome** of a habitat is its community of microorganisms (bacteria, archaea, fungi, protists and viruses) together with their genomes, gene products and the surrounding environmental conditions; the organisms alone are its *microbiota*.

Two sequencing strategies dominate, and they answer different questions.

| | Amplicon sequencing | Shotgun metagenomics |
|---|---|---|
| What is sequenced | PCR products of one marker gene (16S rRNA for bacteria and archaea, ITS for fungi, 18S for eukaryotes) | random fragments of all DNA in the sample |
| Reads per sample | $10^4$–$10^5$ | $10^6$–$10^8$ |
| Resolution | genus, sometimes species | species and strains; genes and genomes |
| Answers | who is there, in what proportions | who is there and what they can do (genes, pathways); new genomes |
| Biases | primer mismatches, PCR, gene copy number | genome size, reference databases, host DNA |
| Cost | low; thousands of samples | higher; host-rich samples need much depth |

Metatranscriptomics (RNA) measures which genes are expressed, and metaproteomics and metabolomics measure products ([7.9.9](/7.9.9)); they share the analysis problems below.

### 14.1.2. The 16S rRNA Gene

The gene for the RNA of the small ribosomal subunit (about $1500$ nt in bacteria) is present in every bacterium and archaeon, evolves slowly enough to be aligned across all of them, and was the molecule with which Woese and Fox found the archaea ([7.8.6](/7.8.6#sec-6.8.1)). Its sequence alternates between conserved regions, constrained by the structure of the **ribosome**, and nine hypervariable regions V1–V9 that differ among taxa. Universal primers in the conserved regions amplify a variable stretch from almost all bacteria in one reaction.

**Definition 14.1.2 (Amplicon Sequencing)** **Amplicon sequencing** is the sequencing of PCR products amplified from a sample with primers that bind conserved sites flanking a variable region of a marker gene; the reads are copies of the marker from the organisms present, and their relative frequencies estimate the composition of the community.

![The 16S rRNA gene in *Escherichia coli* numbering. Conserved regions (red) alternate with the hypervariable regions V1–V9 (yellow). Below, three common amplicons and their primers: the V4 region (515F–806R), the standard of the Earth Microbiome Project, read by 2 × 150 or 2 × 250 paired reads that overlap completely; V3–V4 (341F–805R), read by 2 × 300 reads overlapping in the middle; and the full-length gene (27F–1492R), read as single HiFi reads, which resolves more species](./plots/rrna-16s.py)

Amplicon data are biased in ways that no downstream analysis can remove completely. Primers match some taxa worse than others, and the original 806R primer, for example, underestimated the SAR11 clade of marine bacteria until it was modified. PCR amplifies some templates faster and creates chimeras (§14.2.3). The number of 16S copies per genome ranges from $1$ to about $15$ among bacteria (rrnDB), so read proportions overweight taxa with many copies; corrections from predicted copy numbers are uncertain. And the short V4 region often cannot separate species of the same genus: *Escherichia* and *Shigella*, for instance, are not distinguished by it. Amplicon sequencing is thus best at comparing samples processed in the same way, less good at absolute statements about one sample.

## 14.2. Amplicon Sequence Analysis

### 14.2.1. Operational Taxonomic Units

Reads of one amplicon from one organism differ by sequencing and PCR errors, and reads from different strains of one species may differ by a few true variants. The first generation of pipelines (QIIME 1, mothur, UPARSE) grouped reads by similarity.

**Definition 14.2.1 (Operational Taxonomic Unit)** An **operational taxonomic unit** (OTU) is a cluster of marker sequences grouped by a fixed threshold of pairwise **sequence identity**, conventionally $97\,\%$, and used as a proxy for a taxon.

OTUs are computed by greedy **sequence clustering** ([7.8.4](/7.8.4#sec-4.7.2)): sequences sorted by abundance are compared with existing centroids and join the first within the threshold, or found a new cluster. The $97\,\%$ threshold dates from the observation that strains with less than $97\,\%$ identical full-length 16S genes rarely belong to the same species by DNA–DNA hybridization (Stackebrandt and Goebel 1994); later analyses suggest about $99\,\%$ for full-length genes and $100\,\%$ for V4 as better species proxies (Edgar 2018). OTUs have three problems: errors above $3\,\%$ in a read create spurious OTUs; true variants within $3\,\%$ are merged; and clusters depend on the data set and the order of the sequences, so OTUs from two studies cannot be compared without reclustering.

### 14.2.2. Amplicon Sequence Variants

**Definition 14.2.2 (Amplicon Sequence Variant)** An **amplicon sequence variant** (ASV) is an exact biological sequence inferred from amplicon reads by a denoising algorithm, which models sequencing errors and accepts a sequence as real only if its abundance cannot be explained as errors from more abundant sequences.

ASVs are reproducible labels, the sequences themselves, comparable across studies, and they resolve single-nucleotide differences. The most widely used denoiser, DADA2 (Callahan and colleagues 2016), combines an error model learned from the data with a test on abundances.

**Algorithm 14.2.1 (DADA2 Denoising)** Input: the unique sequences of a sample (after quality filtering by expected errors, [Formula 9.2.1](/7.8.9#fml-9.2.1), and trimming of primers) with their abundances and quality profiles, and an error model giving the probability of each substitution as a function of quality.

1. Start with one partition, all sequences assigned to the most abundant sequence as its center.
2. For each sequence $i$ in a partition with center $j$, compute $\lambda_{ji}$, the probability that a read of $j$ is converted into $i$: the product over positions of the error probabilities of the substitutions (and of no error elsewhere), given the qualities. The number of copies of $i$ produced from the $a_j$ reads of $j$ is then approximately Poisson with mean $a_j\lambda_{ji}$.
3. The *abundance p-value* of $i$, the probability of seeing at least its abundance $a_i$ given that it was seen at all, is
   $$
   p_i = \frac{\mathbb{P}(X \geq a_i)}{\mathbb{P}(X \geq 1)}, \qquad X \sim \mathrm{Poi}(a_j\lambda_{ji}).
   $$
4. If the smallest $p_i$ is below a threshold $\Omega_A$ (default $10^{-40}$, small because the test is applied to very many sequences), make that sequence the center of a new partition and reassign every sequence to the center most likely to have produced it.
5. Repeat 2–4 until no $p_i$ is below $\Omega_A$; the centers are the ASVs and the partition sizes their abundances.

The error model is learned by alternating: denoise with a current model, then re-estimate the substitution rates for each quality score from the differences between reads and their assigned centers (smoothed across qualities), until it converges. Learning from the run itself captures its specific error profile. Other denoisers (UNOISE3, Deblur) use fixed error profiles and abundance ratios instead of p-values; all of them discard sequences seen once, which cannot be distinguished from errors.

**Example 14.2.1** Reads of $250$ nt at Q$35$ throughout have error probability $10^{-3.5} = 3.2\times10^{-4}$ per base, and a particular substitution occurs at a given base with about a third of that. For a variant differing at one position, $\lambda = (3.2\times10^{-4}/3)(1 - 3.2\times10^{-4})^{249} = 9.7\times10^{-5}$. A parent with $a_j = 10\,000$ reads produces on average $0.97$ copies of the variant by error. If the variant has $a_i = 20$ reads, $p = \mathbb{P}(X \geq 20)/\mathbb{P}(X \geq 1) = 1.6\times10^{-19}$: very unlikely to be error, but not below $10^{-40}$, so DADA2 keeps it in the parent's partition. At $30$ reads, $p = 1.1\times10^{-33}$, still above the threshold; at $35$, $p = 2.4\times10^{-41}$, and the variant becomes an ASV. With a parent of $10^5$ reads it needs $76$ reads. The strict threshold protects against false ASVs from the most abundant sequences, at the cost of missing rare true variants next to them.

![The abundance p-value of DADA2 for a variant one substitution away from a parent (250-nt reads at Q35, λ = 9.7 × 10⁻⁵). A: log₁₀ p-value against the variant's abundance for parents of 10³, 10⁴ and 10⁵ reads; the dashed line is the default threshold Ω_A = 10⁻⁴⁰, crossed at 22, 35 and 76 reads. B: the minimum abundance for a new ASV against parent abundance; it is about 12 reads even for small parents, and grows roughly in proportion to the expected number of error copies once that exceeds one](./plots/dada2-pvalue.py)

### 14.2.3. Chimeras

During PCR an incompletely extended strand can prime on a different template in the next cycle, producing a hybrid whose $5'$ part comes from one organism and $3'$ part from another. Such PCR chimeras are abundant enough to pass denoising, and they are new sequences that do not exist in nature. They are recognized because their parents are present and more abundant: a sequence is flagged as a *bimera* if it can be reconstructed exactly by joining a left segment of one more abundant ASV to the right segment of another (DADA2's `removeBimeraDenovo`, UCHIME). The fraction of reads removed is commonly several percent, and higher after many PCR cycles; keeping cycle numbers low is the experimental remedy.

### 14.2.4. Taxonomic Classification

ASVs are named by comparison with reference databases of classified 16S sequences: SILVA, the Genome Taxonomy Database (GTDB, which defines taxa from whole-genome phylogenies), and RDP; UNITE for fungal ITS. The standard method is the **naive Bayes classifier** of the RDP Classifier (Wang and colleagues 2007), applied to $k$-mer "words".

**Formula 14.2.1 (Naive Bayes Classification of a Marker Sequence)** Let a reference set of $N$ sequences be labeled with genera, let $n(w)$ be the number of reference sequences containing the word $w$ ($8$-mers), and for genus $g$ with $M_g$ sequences let $m_g(w)$ be the number of them containing $w$. With the smoothed prior $P_w = (n(w) + 0.5)/(N + 1)$, the word probabilities are

$$
\mathbb{P}(w \mid g) = \frac{m_g(w) + P_w}{M_g + 1},
$$

and a query with word set $W$ is assigned to the genus maximizing $\sum_{w \in W}\log\mathbb{P}(w \mid g)$ (equal genus priors). The words of a sequence are treated as independent, which they are not, but the classification works because only the ranking matters. Confidence is assessed by a bootstrap: in each of $100$ replicates a random eighth of the words is drawn and classified, and the fraction of replicates that agree with the full assignment is reported for each rank; the assignment is truncated at the deepest rank with confidence above a threshold (often $80\,\%$, or $50\,\%$ for short reads).

The scikit-learn implementation in QIIME 2 trains the same kind of classifier on the region amplified by the study's primers, which improves accuracy because the classifier then sees only words that can occur. Species-level names are added only for exact matches, and even then only where the region separates species.

### 14.2.5. A Workflow

```bash
# QIIME 2: import demultiplexed paired reads, denoise with DADA2, classify, build a tree, compute diversity
qiime tools import --type 'SampleData[PairedEndSequencesWithQuality]' \
      --input-path manifest.tsv --input-format PairedEndFastqManifestPhred33V2 --output-path demux.qza
qiime dada2 denoise-paired --i-demultiplexed-seqs demux.qza --p-trim-left-f 19 --p-trim-left-r 20 \
      --p-trunc-len-f 240 --p-trunc-len-r 200 --o-table table.qza --o-representative-sequences asv.qza \
      --o-denoising-stats stats.qza
qiime feature-classifier classify-sklearn --i-classifier silva-138-515-806-nb.qza --i-reads asv.qza \
      --o-classification taxonomy.qza
qiime phylogeny align-to-tree-mafft-fasttree --i-sequences asv.qza --o-alignment aln.qza \
      --o-masked-alignment masked.qza --o-tree unrooted.qza --o-rooted-tree rooted.qza
qiime diversity core-metrics-phylogenetic --i-phylogeny rooted.qza --i-table table.qza \
      --p-sampling-depth 10000 --m-metadata-file metadata.tsv --output-dir core-metrics
```

The trimming lengths remove the primers ($19$ and $20$ nt for 515F and 806R) and truncate the reads where quality drops, while leaving enough overlap (at least $12$ nt beyond the amplicon length) for the mates to be merged. The tree, built here by MAFFT and FastTree ([7.8.6](/7.8.6#sec-6.7)) or by placing ASVs into a reference tree, is needed for phylogenetic diversity measures (§14.4.3). Negative controls (extraction blanks and PCR water) and a mock community of known composition are sequenced in the same run: the first reveal contaminants, the second measures the biases of the whole procedure.

## 14.3. Shotgun Metagenomics

### 14.3.1. Classifying Reads by k-mers

A shotgun metagenome is a mixture of reads from thousands of genomes, plus the host's. Aligning $10^7$ reads against all reference genomes is slow; most read classifiers instead use exact $k$-mer matches, the principle of the hash-table indexes of [7.8.10](/7.8.10#sec-10.2.1).

**Definition 14.3.1 (Lowest Common Ancestor)** In a rooted taxonomy, the **lowest common ancestor** (LCA) of a set of taxa is the deepest node that is an ancestor of (or equal to) all of them. A $k$-mer that occurs in genomes of several taxa is labeled with their LCA: a $k$-mer found in all *Escherichia coli* and *Salmonella enterica* genomes but in no other is labeled with their family, Enterobacteriaceae.

**Algorithm 14.3.1 (Kraken-Style Read Classification)** Database: for every $k$-mer (or minimizer, [7.8.10](/7.8.10#sec-10.3.2)) of the reference genomes, store the LCA of the taxa containing it in a hash table. For a read:

1. Look up each of its $k$-mers; count the hits to each taxon, ignoring $k$-mers not in the database.
2. For each root-to-leaf path in the subtree of hit taxa, sum the hits on its nodes; assign the read to the leaf of the highest-scoring path (if several tie, to their LCA).
3. Optionally require a confidence: if the fraction of the read's $k$-mers that hit the assigned taxon or its descendants is below a threshold, move the label up the path until the fraction is reached.

Kraken 2 (Wood and colleagues 2019) uses $k = 35$ with minimizers of length $31$ and stores only the LCA in a compact hash table, so a database of tens of thousands of genomes fits in memory and classification runs at millions of reads per minute. Its weaknesses follow from the design: a read from an organism absent from the database is assigned to whatever relative contributes its $k$-mers, or to a high rank, and contaminated reference genomes (with human or vector sequence) create false hits.

**Example 14.3.1** A read has $30$ minimizers; $6$ hit *E. coli*, $2$ *S. enterica*, $10$ Enterobacteriaceae and $3$ Bacteria, and $9$ are not in the database. The path to *E. coli* scores $3 + 10 + 6 = 19$, that to *S. enterica* $15$, and those to the two Bacillales species $3$, so the read is labeled *E. coli*. With a confidence threshold of $0.7$, the fraction of minimizers in the clade of *E. coli* is $6/30 = 0.2$, in Enterobacteriaceae $18/30 = 0.6$ and in Bacteria $21/30 = 0.7$, so the read is labeled Bacteria: higher confidence thresholds trade resolution for precision.

![Kraken-style classification of one read. A: its 30 minimizers colored by the taxon stored for each in the database (white: not in the database). B: the hits on the taxonomy; the root-to-leaf path scores are 19 for *Escherichia coli*, 15 for *Salmonella enterica* and 3 for the Bacillales species, so the read is assigned to *E. coli*; with a confidence threshold of 0.7 it is assigned to Bacteria, the first node whose clade holds 70 % of the minimizers](./plots/kraken-lca.py)

:::

Many reads are assigned above species level, because closely related species share most of their $k$-mers. Abundance estimates at species level must redistribute them.

**Formula 14.3.1 (Bayesian Redistribution of Reads)** Let $\theta_{st}$ be the probability that a read from species $s$ is classified at taxon $t$ (estimated by classifying simulated reads from the reference genomes of $s$). If $R_s$ reads are classified at the species $s$ itself, the number of reads from $s$ is estimated by $\hat N_s = R_s/\theta_{ss}$, and the $R_t$ reads at a higher taxon $t$ are divided among the species below it in proportion to the expected contributions:

$$
\hat N_s^{(t)} = R_t\,\frac{\theta_{st}\hat N_s}{\sum_{s' \subset t}\theta_{s't}\hat N_{s'}}.
$$

This is the idea of Bracken (Lu and colleagues 2017): Bayes' rule with the species abundances as prior and the classification probabilities as likelihood.

**Example 14.3.2** In a sample with $1600$ reads from *E. coli* and $400$ from *Shigella flexneri*, suppose half of the *E. coli* reads and $80\,\%$ of the *Shigella* reads are classified only at their common genus level. The classifier reports $800$ reads for *E. coli*, $80$ for *Shigella* and $1120$ above them, so species-level counts alone suggest $91\,\%$ *E. coli*. Redistribution gives $\hat N = 800/0.5 = 1600$ and $80/0.2 = 400$; the $1120$ higher reads are divided in proportion $0.5\times1600 : 0.8\times400 = 800 : 320$, which restores the true $1600$ and $400$ ($80\,\%$ and $20\,\%$).

### 14.3.2. Marker Genes and the Meaning of Abundance

MetaPhlAn (now version 4) takes another route: from about a million genomes and metagenome-assembled genomes it selects genes present in all members of one clade and absent from all others, aligns reads only to these markers, and estimates the abundance of each clade from the mean coverage of its markers. It is fast, has few false positives, and reports organisms not in culture collections through species-level genome bins defined from assembled metagenomes; it misses organisms whose markers are not in its database.

The two approaches estimate different quantities. A classifier that counts reads estimates the fraction of DNA from each taxon, which is proportional to the number of cells times the genome length; marker coverage estimates the fraction of genome copies, closer to the fraction of cells.

**Formula 14.3.2 (Read Abundance and Cell Abundance)** If taxon $s$ has relative cell abundance $c_s$ and genome length $L_s$, its expected fraction of reads is

$$
r_s = \frac{c_sL_s}{\sum_{s'} c_{s'}L_{s'}}, \qquad\text{so}\qquad c_s = \frac{r_s/L_s}{\sum_{s'} r_{s'}/L_{s'}}.
$$

**Example 14.3.3** Two species with equal numbers of cells and genomes of $2$ and $6\,\mathrm{Mb}$ contribute $25\,\%$ and $75\,\%$ of the reads. Comparing a read-based and a marker-based profile of the same sample without this correction gives apparent threefold disagreements; viruses, with genomes of kilobases, are underrepresented among reads relative to their particle numbers by orders of magnitude.

### 14.3.3. Assembly

Assembly of metagenomes uses the de Bruijn graph methods of [7.8.11](/7.8.11) with adaptations for mixtures: coverage differs by orders of magnitude between genomes, so coverage-based filtering of errors must be local; strains of one species differ at a few percent of positions, creating bubbles that a single-genome assembler would resolve wrongly; and repeated elements (rRNA operons, transposons, **plasmids**) are shared between genomes. metaSPAdes and MEGAHIT (fast and memory-efficient, using iterated $k$-mer sizes) are standard for short reads, metaFlye and hifiasm-meta for long reads, which assemble many genomes into single circular contigs. Contigs are annotated by gene prediction in metagenome mode (Prodigal, [7.8.7](/7.8.7)) and by searches with DIAMOND or HMMER against protein databases ([7.8.4](/7.8.4#sec-4.7.1), [7.8.5](/7.8.5)).

### 14.3.4. Binning and Metagenome-Assembled Genomes

An assembly yields thousands of **contigs** from different genomes. Grouping them by genome uses two signals. Composition: the frequencies of short words, especially tetranucleotides, are a genomic signature that is similar across one genome and differs between species ([7.8.7](/7.8.7#sec-7.1.2)); it becomes reliable for contigs longer than a few kilobases. Coverage: all contigs of one genome have about the same **sequencing coverage** in a sample, and across several samples their coverages rise and fall together as the organism's abundance changes, a signal that separates even species of identical composition.

**Definition 14.3.2 (Binning and Metagenome-Assembled Genome)** **Binning** is the grouping of contigs (or reads) of a metagenome into bins, each intended to contain the sequences of one genome, by sequence composition, coverage across samples and assembly-graph connections. A **metagenome-assembled genome** (MAG) is a bin of sufficient estimated quality, treated as a draft genome of a population of closely related cells.

Binners differ in how they combine the signals: MetaBAT 2 computes probabilistic distances from tetranucleotide frequencies and coverage and partitions a graph of contigs; CONCOCT fits a **Gaussian mixture model**; VAMB and SemiBin learn embeddings with neural networks. Ensemble tools (DAS Tool) choose the best bins from several binners.

![Binning by composition and coverage (simulated: six genomes, 40–120 contigs each, points sized by contig length). Contigs are colored by the bin found by k-means on standardized GC content and log coverage in two samples. A: GC content against coverage in sample 1: genomes 4 and 5 have nearly the same composition and abundance and overlap completely. B: coverages in the two samples, where the two separate because their abundances change differently between samples. With both samples the bins are 99.9 % pure and each holds all of its genome; with GC and one sample only, purity falls to 87.7 %. Real binners use the 136 tetranucleotide frequencies rather than GC alone, and many samples](./plots/binning.py)

**Formula 14.3.3 (Completeness and Contamination)** Let $\mathcal{M}$ be a set of marker genes expected to be present exactly once in every genome of the lineage of a bin, and let $c_g$ be the number of copies of marker $g$ found in the bin. Then

$$
\text{completeness} = \frac{\lvert\{g \in \mathcal{M} : c_g \geq 1\}\rvert}{\lvert\mathcal{M}\rvert}, \qquad \text{contamination} = \frac{\sum_{g \in \mathcal{M}} \max(c_g - 1, 0)}{\lvert\mathcal{M}\rvert}.
$$

CheckM (Parks and colleagues 2015) uses lineage-specific sets of such genes, grouped into sets that occur together on chromosomes so that neighboring genes are not counted twice; CheckM2 predicts both quantities with a machine-learning model trained on genomes with simulated gaps and contamination, which also works for lineages with few reference genomes.

**Example 14.3.4** A bin contains $112$ of $120$ single-copy markers once, $4$ twice and lacks $4$. Its completeness is $116/120 = 96.7\,\%$ and its contamination $4/120 = 3.3\,\%$. By the minimum information standards for MAGs (MIMAG; Bowers and colleagues 2017) it is a medium-quality draft unless its rRNA genes are present: high quality requires more than $90\,\%$ completeness, less than $5\,\%$ contamination, the 23S, 16S and 5S rRNA genes and at least $18$ tRNAs; medium quality at least $50\,\%$ completeness and less than $10\,\%$ contamination. rRNA operons are often missing from short-read MAGs because they are repeated in the genome and collapse in assembly.

:::

MAGs have changed microbiology: hundreds of thousands of them from human guts, oceans and soils have added whole phyla of uncultured organisms to the tree of life, and the Genome Taxonomy Database classifies them by their position in a genome phylogeny (GTDB-Tk). A MAG is a consensus of a population, not one cell: strain variation is averaged, and mobile elements and plasmids, with coverage and composition different from the chromosome, are often missing.

### 14.3.5. Functional Profiles

What a community can do is read from its genes. HUMAnN (Huttenhower laboratory) maps reads first to the pangenomes of the species detected by MetaPhlAn and then, by translated search with DIAMOND, to UniRef90 protein clusters, and combines gene families into pathway abundances (MetaCyc), stratified by contributing species. Antimicrobial resistance genes are identified against curated databases (CARD with its Resistance Gene Identifier, ResFinder); because many resistance genes travel on plasmids by **horizontal gene transfer** ([7.4.10](/7.4.10)), linking a gene to its host requires long reads, Hi-C (which crosslinks DNA within one cell, [7.8.11](/7.8.11)) or careful assembly.

```bash
# Shotgun metagenome: remove host reads, classify, profile, assemble, bin, assess
bowtie2 -x GRCh38 -1 r1.fq.gz -2 r2.fq.gz --very-sensitive --un-conc-gz nonhost.fq.gz -S /dev/null -p 16
kraken2 --db k2_standard --paired nonhost.fq.1.gz nonhost.fq.2.gz --confidence 0.1 \
        --report sample.k2report --output sample.k2out --threads 16
bracken -d k2_standard -i sample.k2report -r 150 -l S -o sample.bracken     # species abundances
metaphlan nonhost.fq.1.gz,nonhost.fq.2.gz --input_type fastq --nproc 16 -o sample.mpa.txt
megahit -1 nonhost.fq.1.gz -2 nonhost.fq.2.gz -o asm -t 16
# map reads of every sample to the contigs, then bin by composition and differential coverage
jgi_summarize_bam_contig_depths --outputDepth depth.txt sample*.sorted.bam
metabat2 -i asm/final.contigs.fa -a depth.txt -m 2500 -o bins/bin
checkm2 predict --input bins -x fa --output-directory checkm2 --threads 16
gtdbtk classify_wf --genome_dir bins -x fa --out_dir gtdbtk --cpus 16
```

## 14.4. Diversity

### 14.4.1. Alpha Diversity

Ecologists describe a community by how many kinds of organisms it contains and how evenly they are represented.

**Definition 14.4.1 (Alpha Diversity)** The **alpha diversity** of a sample is a measure of the diversity within it, computed from the relative abundances $p_1, \dots, p_S$ of its $S$ taxa: the **richness** $S$; the **Shannon index** $H = -\sum_i p_i\ln p_i$; the **Simpson index** $\lambda = \sum_i p_i^2$, the probability that two reads drawn at random belong to the same taxon, usually reported as $1 - \lambda$ (Gini–Simpson) or $1/\lambda$ (inverse Simpson); and phylogenetic diversity, the total branch length of the tree spanning the taxa (Faith 1992).

The indices weigh rare taxa differently and are measured in different units; they are unified by one family.

**Formula 14.4.1 (Hill Numbers)** The *Hill number* of order $q \geq 0$ is

$$
{}^qD = \Bigl(\sum_{i=1}^S p_i^q\Bigr)^{1/(1-q)}, \qquad {}^1D = \lim_{q\to1}{}^qD = \mathrm{e}^{\mathsf H},
$$

so ${}^0D = S$, ${}^1D = \mathrm{e}^{\mathsf H}$ and ${}^2D = 1/\lambda$. ${}^qD$ is the *effective number of taxa*: a community of ${}^qD$ equally abundant taxa has the same index; it decreases with $q$, and the faster it does, the more uneven the community (Hill 1973; Jost 2006).

**Example 14.4.1** A sample with counts $50, 25, 15, 7, 3$ of five taxa has $p = (0.50, 0.25, 0.15, 0.07, 0.03)$. Then $S = 5$, $H = 1.269$ (${}^1D = 3.56$ effective taxa), $\lambda = 0.341$ (${}^2D = 2.93$, Gini–Simpson $0.659$), and Pielou's evenness $H/\ln S = 0.789$. Halving the counts of the three rarest taxa would barely change ${}^2D$ but would change $H$ more, and $S$ not at all unless a taxon is lost; which index to report depends on whether rare taxa matter for the question.

### 14.4.2. Sampling Depth and Rarefaction

Observed richness grows with the number of reads: a sample sequenced deeper shows more rare taxa. Comparing richness between samples of different depth is therefore meaningless without adjustment.

**Definition 14.4.2 (Rarefaction Curve)** The **rarefaction curve** of a sample is the expected number of taxa observed in a random subsample of $n$ of its reads, as a function of $n$. For a sample of $N$ reads with $N_i$ reads of taxon $i$ (Hurlbert 1971),

$$
\mathbb{E}[S_n] = \sum_{i=1}^{S}\left[1 - \binom{N - N_i}{n}\Bigl/\binom{N}{n}\right].
$$

A curve that flattens indicates that further sequencing would find few new taxa. The total richness, including unseen taxa, is estimated from the numbers of rare taxa: with $f_1$ taxa seen once and $f_2$ seen twice, the Chao1 estimator is $\hat S = S_{\mathrm{obs}} + f_1^2/(2f_2)$, a lower bound on the true richness (Chao 1984). With $S_{\mathrm{obs}} = 120$, $f_1 = 30$ and $f_2 = 15$, $\hat S = 120 + 900/30 = 150$. Since singletons in amplicon data are removed by denoising (§14.2.2), Chao1 is unreliable for ASV tables; it is meaningful for read-level counts.

![Rarefaction of two simulated communities (log-normal abundances, 20 000 reads each). A: expected taxa observed in subsamples of n reads (Definition 14.4.2); dashed lines are the true richness, 150 and 1500. Community 1 is nearly saturated (149 taxa observed, Chao1 149), community 2 is not (1401 observed, Chao1 1453). At 100 reads the samples show 52 and 91 taxa, at 1000 reads 120 and 536: comparisons at equal depth preserve the ordering, raw comparisons at unequal depth do not. B: Hill numbers against order q; the effective number of taxa falls from 149 to 75 and 51 (q = 0, 1, 2) in community 1 and from 1401 to 745 and 441 in community 2](./plots/rarefaction.py)

**Example 14.4.2** For the five-taxon sample of Example 14.4.1 ($N = 100$), the expected richness in subsamples of $5$, $10$, $20$ and $50$ reads is $2.76$, $3.58$, $4.27$ and $4.87$: the rarest taxon, with $3$ reads, is found in a subsample of $10$ with probability $1 - \binom{97}{10}/\binom{100}{10} = 0.27$.

:::

*Rarefying*, randomly subsampling every sample to the same depth before analysis, makes richness comparable but discards data and adds random noise; for differential abundance it loses power and is not recommended (McMurdie and Holmes 2014), while for diversity comparisons it remains common, with repeated subsampling or coverage-based standardization (comparing samples at equal estimated completeness, Chao and Jost 2012) as better alternatives.

### 14.4.3. Beta Diversity

**Definition 14.4.3 (Beta Diversity)** The **beta diversity** of a set of samples is the variation of composition among them, quantified by a dissimilarity between each pair of samples. For abundance vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ of two samples:

- the **Bray–Curtis dissimilarity** $\mathrm{BC} = 1 - 2\sum_i\min(x_i, y_i)\big/\sum_i(x_i + y_i)$, computed on relative abundances, is $0$ for identical compositions and $1$ for samples sharing no taxa;
- the **Jaccard distance** $1 - \lvert A \cap B\rvert/\lvert A \cup B\rvert$ between the sets $A$, $B$ of taxa present uses only presence and absence;
- **UniFrac** (Lozupone and Knight 2005) uses the phylogenetic tree of the taxa: the unweighted version is the fraction of the total branch length of the tree that leads to taxa of only one of the two samples; the weighted version sums branch lengths $b_k$ times the difference in the fraction of each sample's abundance below them, $\sum_k b_k\lvert p_{A,k} - p_{B,k}\rvert$, normalized.

UniFrac counts two samples as similar if their taxa are close relatives even when the ASVs differ, which is often biologically appropriate; presence–absence measures emphasize rare taxa, abundance-weighted measures the dominant ones.

**Example 14.4.3** Two samples with counts $(10, 20, 30, 40)$ and $(20, 20, 10, 50)$ of four taxa share $\sum\min = 10 + 20 + 10 + 40 = 80$ of $200$ reads, so $\mathrm{BC} = 1 - 160/200 = 0.20$. Both contain all four taxa, so their Jaccard distance is $0$. The Aitchison distance of §14.5.2 is $1.31$.

### 14.4.4. Ordination and PERMANOVA

Dissimilarity matrices are displayed by **principal coordinates analysis**, which is **classical multidimensional scaling** of the matrix ([3.4.6](/3.4.6#sec-6.2.3)): double-center $-\tfrac12 d_{ij}^2$ and take the leading eigenvectors scaled by the square roots of their eigenvalues. Bray–Curtis and UniFrac are not Euclidean distances, so some eigenvalues are negative and the shares of "variance explained" are computed from the positive ones; non-metric multidimensional scaling, which preserves only ranks of dissimilarities, is the common alternative. Whether groups of samples differ is tested directly on the dissimilarities.

**Formula 14.4.2 (PERMANOVA)** For $N$ samples in $a$ groups of sizes $n_1, \dots, n_a$ with dissimilarities $d_{ij}$, let

$$
\mathrm{SS}_{\mathrm{T}} = \frac{1}{N}\sum_{i<j} d_{ij}^2, \qquad \mathrm{SS}_{\mathrm{W}} = \sum_{g=1}^a\frac{1}{n_g}\sum_{\substack{i<j\\ i,j \in g}} d_{ij}^2, \qquad F = \frac{(\mathrm{SS}_{\mathrm{T}} - \mathrm{SS}_{\mathrm{W}})/(a - 1)}{\mathrm{SS}_{\mathrm{W}}/(N - a)}.
$$

For Euclidean distances this is the $F$ statistic of one-way ANOVA on the coordinates; for other dissimilarities its null distribution is obtained by a **permutation test**: the group labels are permuted (within strata such as subjects, when samples are paired), $F$ is recomputed, and the $p$-value is the fraction of permutations with $F$ at least the observed value (Anderson 2001).

![Beta diversity of two simulated groups of 20 samples (60 taxa; in group 2 six abundant taxa are twice and six others half as abundant). A: PCoA of Bray–Curtis dissimilarities; the axes carry 18 % and 12 % of the positive eigenvalues, and 9 of the 40 eigenvalues are negative. B: PERMANOVA: the observed pseudo-F of 6.4 lies beyond all 999 permuted values (p = 0.001, the smallest value possible with 999 permutations)](./plots/pcoa.py)

PERMANOVA tests whether group centroids differ in the space defined by the dissimilarity, but it is also sensitive to differences in spread: a group whose samples vary more can produce a significant $F$ with equal centroids, particularly with unbalanced designs. A test of homogeneity of dispersions (PERMDISP) is run alongside, and differences in sequencing depth, which change dissimilarities, must be ruled out as the cause.

## 14.5. Compositional Data

### 14.5.1. Closure

A sequencing run produces a fixed number of reads, divided among samples by pooling and among taxa by their share of the DNA. A sample's read counts therefore tell us only the *relative* abundances: if every organism in a sample doubled, the counts would not change.

**Definition 14.5.1 (Compositional Data)** **Compositional data** are vectors $\boldsymbol{x} = (x_1, \dots, x_D)$ of positive parts that carry only relative information: $\boldsymbol{x}$ and $c\boldsymbol{x}$ represent the same composition for every $c > 0$. They are represented on the simplex by the closure $\mathcal{C}(\boldsymbol{x}) = \boldsymbol{x}/\sum_j x_j$ (Aitchison 1986).

Microbiome counts, RNA-seq counts and cell-type proportions ([7.9.5](/7.9.5)) are compositional. Two consequences follow.

**Theorem 14.5.1 (Covariances of Closed Data)** If $\boldsymbol{p} = (p_1, \dots, p_D)$ are random proportions with $\sum_j p_j = 1$, then for each $i$

$$
\sum_{j=1}^D \operatorname{Cov}(p_i, p_j) = 0,
$$

so each part's variance is balanced by negative covariances with the others. If all parts have the same variance and the same pairwise correlation $\rho$, then $\rho = -1/(D - 1)$.

**Proof** $\sum_j\operatorname{Cov}(p_i, p_j) = \operatorname{Cov}\bigl(p_i, \sum_j p_j\bigr) = \operatorname{Cov}(p_i, 1) = 0$. With equal variances $\sigma^2$ and correlations $\rho$, the sum is $\sigma^2 + (D - 1)\rho\sigma^2 = 0$. $\square$

Correlations between relative abundances are therefore biased toward negative values whatever the true relations of the absolute abundances, strongly when there are few taxa or one taxon dominates (Pearson's "spurious correlation", 1897). And changes are confounded: a change in one taxon changes the proportions of all.

**Example 14.5.1** Four taxa each have $100$ units of absolute abundance, so each has proportion $0.25$. Taxon D then grows tenfold while A, B and C are unchanged: the proportions become $100/1300 = 0.077$ for A, B and C and $0.769$ for D. A per-taxon test on proportions would report that A, B and C "decreased" more than threefold. The ratios $x_A/x_B$, $x_A/x_C$ and $x_B/x_C$ are $1$ before and after: ratios between parts are the only quantities that the data determine and that are unaffected by changes in other parts.

![Pitfalls of compositional data. A: four taxa of equal absolute abundance; after a tenfold bloom of D, the relative abundances of A–C fall from 0.25 to 0.077 although their absolute abundances did not change. B: 500 samples of five taxa with independent log-normal absolute abundances: the proportions of taxa 1 and 2 are correlated with r = −0.45, their absolute abundances with r = −0.04. C: mean correlation between proportions of independent, identically distributed taxa against the number of taxa, with the value −1/(D − 1) of Theorem 14.5.1](./plots/compositional.py)

### 14.5.2. Log-Ratios

Aitchison's solution is to analyze log-ratios, which are invariant to the unknown total.

**Definition 14.5.2 (Centered Log-Ratio Transformation and Aitchison Distance)** The **centered log-ratio transformation** of a composition $\boldsymbol{x}$ with geometric mean $g(\boldsymbol{x}) = (\prod_j x_j)^{1/D}$ is

$$
\operatorname{clr}(\boldsymbol{x}) = \Bigl(\ln\frac{x_1}{g(\boldsymbol{x})}, \dots, \ln\frac{x_D}{g(\boldsymbol{x})}\Bigr),
$$
and the **Aitchison distance** between two compositions is the Euclidean distance between their clr vectors.

The clr vector is unchanged when $\boldsymbol{x}$ is multiplied by a constant (the factor cancels in each ratio), so analyses on clr values do not depend on sequencing depth; its components sum to zero, so it lives in a $(D - 1)$-dimensional subspace, and Theorem 14.5.1 applies to it as well. Its value for one taxon is relative to the geometric mean of all, which changes when other taxa change, so a clr difference is not an absolute change either: no transformation can recover absolute abundances from relative data. The additive log-ratio $\ln(x_j/x_D)$ against a reference part $D$, and isometric log-ratios built on balances between groups of parts (for example, along the phylogenetic tree), are the other standard coordinates; PCA on clr values is a principal component analysis in the Aitchison geometry, and PERMANOVA with the Aitchison distance is a common alternative to Bray–Curtis.

Logarithms require positive values, but microbiome tables are mostly zeros: a taxon may be absent, or present below detection. A pseudocount (adding $0.5$ or $1$ to every count) is the common fix, and results can depend on its size; model-based approaches treat counts as draws from a **multinomial distribution** with probabilities from a **Dirichlet distribution**, and work with the posterior distribution of the proportions instead of the zeros (ALDEx2).

### 14.5.3. Differential Abundance

Testing which taxa differ between groups is the microbiome analog of differential expression ([7.9.2](/7.9.2)), with stronger compositional effects because a few taxa often dominate and their changes shift all proportions. The methods differ in their assumptions:

| Method | Model | Assumption needed to interpret changes |
|---|---|---|
| ALDEx2 | Monte Carlo samples from Dirichlet posteriors of the proportions, clr, then $t$ or Wilcoxon tests, averaged | changes relative to the geometric mean; most taxa unchanged |
| ANCOM, ANCOM-BC | log-ratio tests of each taxon against all others; ANCOM-BC estimates sample-specific biases of sampling fractions in a linear model | most taxa unchanged |
| DESeq2, edgeR, corncob | negative binomial or beta-binomial counts with normalization by size factors ([7.7.20](/7.7.20)) | a stable reference set of taxa |
| MaAsLin 2 | linear models on transformed relative abundances with covariates | interpretation in relative terms |

All of them need some assumption equivalent to "most taxa do not change", because composition alone cannot determine absolute changes. On the same data sets they give strikingly different lists of significant taxa (Nearing and colleagues 2022, comparing $14$ methods on $38$ data sets), so results should be checked with more than one method and with the raw data. The more fundamental solution is to measure the total: counting cells by flow cytometry or adding a known amount of a spike-in organism or synthetic DNA to each sample turns relative into absolute abundances (quantitative microbiome profiling; Vandeputte and colleagues 2017), and changes in total microbial load turn out to drive many reported differences. **Batch effects** from extraction kits and sequencing runs are as strong as in other omics and are handled by design and by including batch in the model. Because thousands of taxa are tested, $p$-values are adjusted to control the **false discovery rate**.

### 14.5.4. Co-Occurrence Networks

Taxa that rise and fall together across samples may interact (cooperate, share a niche) and those with opposite patterns may compete. Co-occurrence networks connect taxa by measures of association, and they are analyzed with the methods of network science ([1.4.7](/1.4.7)) and systems biology ([7.9](/7.9)). Correlations of proportions are biased by Theorem 14.5.1, so methods work on log-ratios:

**Formula 14.5.1 (Variance of Log-Ratios)** If the log absolute abundances $y_i = \ln x_i$ have variances $\omega_i^2$ and correlations $\rho_{ij}$, then the variance of a log-ratio, which can be computed from the relative data, is

$$
t_{ij} = \operatorname{Var}\Bigl(\ln\frac{x_i}{x_j}\Bigr) = \omega_i^2 + \omega_j^2 - 2\rho_{ij}\omega_i\omega_j.
$$

A small $t_{ij}$ means that the two taxa are proportional across samples. SparCC (Friedman and Alm 2012) solves these equations for the $\omega_i$ and $\rho_{ij}$ under the assumption that most correlations are near zero; SPIEC-EASI (Kurtz and colleagues 2015) applies the graphical lasso or neighborhood selection to clr-transformed data, estimating a sparse network of conditional dependences rather than correlations ([7.9.11](/7.9.11#sec-11.3.2)). Even then, edges are statistical associations: shared responses to the environment, the host or a third taxon produce them without interaction, and network inference needs many more samples than taxa to be stable.

## 14.6. Applications

### 14.6.1. Clinical Metagenomic Diagnosis

Metagenomic next-generation sequencing (mNGS) of cerebrospinal fluid, blood, respiratory samples or tissue detects pathogens without a prior hypothesis: bacteria, viruses, fungi and parasites in one test. In a widely cited case, a boy with severe combined immunodeficiency and encephalitis of unknown cause was diagnosed with neuroleptospirosis from reads of *Leptospira* in his cerebrospinal fluid and recovered after treatment with penicillin (Wilson and colleagues 2014). Clinical mNGS has to solve problems that research metagenomics can often ignore:

- Host reads make up more than $99\,\%$ of most samples, so the pathogen may be represented by a few reads; host depletion (before sequencing, or by alignment to the human **reference genome** and removal afterward, as in the pipeline above) and depth determine sensitivity.
- Reagents and laboratories contain microbial DNA (the "kitome"), which dominates samples of low biomass (Salter and colleagues 2014). Every batch includes negative controls; a taxon is reported only if it exceeds the controls by a set ratio of reads per million, and statistical methods identify contaminants as taxa whose abundance is inversely related to the sample's total DNA or that are prevalent in controls (decontam; Davis and colleagues 2018).
- Interpretation requires knowing what is normally present: a skin commensal in blood may be contamination, a virus may be latent rather than causal.

### 14.6.2. Viruses: Discovery and Surveillance

Viruses lack universal marker genes, so shotgun sequencing is the main way to find them. SARS-CoV-2 was identified in this way: total RNA from the bronchoalveolar lavage fluid of a patient in Wuhan was sequenced, the reads were assembled de novo with MEGAHIT, and the longest contig was a new betacoronavirus genome of about $30\,\mathrm{kb}$, related to bat SARS-like coronaviruses (Wu and colleagues 2020; GenBank MN908947, [7.8.2](/7.8.2)). Its analysis then continued with the methods of the earlier chapters: assembly and variant calling ([7.8.11](/7.8.11), [7.8.12](/7.8.12)) and phylogenetics with lineage nomenclature ([7.8.6](/7.8.6#sec-6.8.3)).

During the pandemic, sequencing of wastewater became a means of tracking lineages in a whole population. A sample contains a mixture of lineages, and its reads give the frequency of each defining mutation; the lineage proportions are estimated by de-mixing.

**Formula 14.6.1 (Lineage De-Mixing)** Let $B$ be the binary matrix whose entry $B_{ml}$ is $1$ if lineage $l$ carries mutation $m$ (its "barcode", from the phylogeny), and let $\boldsymbol{f}$ be the observed frequencies of the mutations in the sample. The lineage proportions $\boldsymbol{w}$ solve

$$
\min_{\boldsymbol{w}}\ \lVert B\boldsymbol{w} - \boldsymbol{f}\rVert \quad\text{subject to}\quad w_l \geq 0,\ \sum_l w_l = 1,
$$

a constrained regression on the simplex (least squares or least absolute deviations, weighted by depth, in programs such as Freyja).

**Example 14.6.1** Three lineages are distinguished by six mutations with barcodes (rows: mutations) $(1,1,0)$, $(1,0,0)$, $(0,1,1)$, $(0,0,1)$, $(1,1,1)$, $(0,1,0)$. A sample with true proportions $(0.6, 0.3, 0.1)$ and sampling noise gives observed frequencies $(0.92, 0.57, 0.41, 0.10, 0.98, 0.32)$. Constrained least squares gives $\hat{\boldsymbol{w}} = (0.583, 0.325, 0.092)$, close to the truth; a lineage carrying no unique mutation could not be separated from the others, which is why barcodes are chosen from mutations that distinguish the lineages of interest.

## Summary

| Topic | Key points |
|---|---|
| Data | metagenomics and the microbiome (Definition 14.1.1); amplicon sequencing of a marker (Definition 14.1.2) against shotgun sequencing of all DNA; 16S V regions and primers; primer, PCR and copy-number biases |
| Amplicon analysis | OTUs at $97\,\%$ (Definition 14.2.1) replaced by ASVs (Definition 14.2.2); DADA2's error model and abundance p-value with $\Omega_A = 10^{-40}$ (Algorithm 14.2.1, Example 14.2.1); chimeras as bimeras of abundant parents; naive Bayes on $8$-mers with bootstrap confidence (Formula 14.2.1); controls and mock communities |
| Read classification | $k$-mers labeled with their LCA (Definition 14.3.1); root-to-leaf path scores and confidence (Algorithm 14.3.1, Example 14.3.1); Bayesian redistribution of higher-rank reads (Formula 14.3.1, Example 14.3.2); marker genes; reads $\propto$ cells $\times$ genome length (Formula 14.3.2) |
| Genomes from mixtures | metagenome assembly; binning by tetranucleotides and differential coverage (Definition 14.3.2); MAGs; completeness and contamination from single-copy markers (Formula 14.3.3, Example 14.3.4), MIMAG thresholds; functional and resistance profiles |
| Diversity | alpha: richness, Shannon, Simpson (Definition 14.4.1) unified as Hill numbers (Formula 14.4.1, Example 14.4.1); rarefaction curves and Chao1 (Definition 14.4.2, Example 14.4.2); beta: Bray–Curtis, Jaccard, UniFrac (Definition 14.4.3, Example 14.4.3); PCoA; PERMANOVA by permutation (Formula 14.4.2) and dispersion |
| Compositional data | only ratios are determined (Definition 14.5.1); closed covariances sum to zero, correlations biased to $-1/(D-1)$ (Theorem 14.5.1, Example 14.5.1); clr and the Aitchison distance (Definition 14.5.2); zeros; differential abundance needs an assumption or absolute measurement; log-ratio variances for networks (Formula 14.5.1) |
| Applications | clinical mNGS, host depletion, contamination and controls; discovery of SARS-CoV-2 by metagenomic assembly; wastewater lineage de-mixing on the simplex (Formula 14.6.1, Example 14.6.1) |

## Questions

1. Why can a $97\,\%$ OTU contain several species, and why can a single species give rise to several OTUs? How do ASVs change each problem?

   **Answer** Closely related species often differ at fewer than $3\,\%$ of positions in a short region (for example V4 within Enterobacteriaceae), so they fall into one OTU. Conversely, reads with errors above $3\,\%$, or strains of one species with divergent 16S copies, can seed extra OTUs, especially with greedy clustering whose outcome depends on sequence order. ASVs resolve single-nucleotide differences, so the first problem shrinks to cases where the region is truly identical; the second becomes explicit: a genome with several different 16S copies gives several ASVs in fixed ratios (for example $6:1$), which can be recognized, while errors are removed by the error model rather than by a threshold.

2. Using the DADA2 model of Example 14.2.1, how many reads must a one-substitution variant of a sequence with $1000$ reads have to become an ASV? Why does the required abundance grow with the parent's abundance?

   **Answer** With $a_j = 1000$, the expected number of error copies is $1000 \times 9.7\times10^{-5} = 0.097$, and the conditional Poisson p-value first falls below $10^{-40}$ at $22$ reads (the figure). The more reads the parent has, the more copies of each one-substitution error it generates ($a_j\lambda$), so an observed abundance that would be extraordinary next to a small parent is expected next to a large one; the variant must exceed the larger expectation by a margin that makes the p-value tiny. Abundant true variants next to very abundant sequences (for example two 16S copies of one genome) may still be merged.

3. A read has $40$ $k$-mers in a Kraken database: $5$ to species A, $8$ to species B, $15$ to the genus containing A and B, $2$ to the family, and $10$ unclassified. Which species is assigned, and with what label at confidence thresholds $0.5$ and $0.6$?

   **Answer** Path to A: $2 + 15 + 5 = 22$; to B: $2 + 15 + 8 = 25$; so the read is labeled B. The clade fractions are B: $8/40 = 0.2$; genus: $(15 + 5 + 8)/40 = 0.7$; family: $30/40 = 0.75$. At threshold $0.5$ or $0.6$, B's clade fails, the genus passes ($0.7$), so the label is the genus in both cases.

4. A sample contains equal numbers of cells of *Escherichia coli* (genome $5\,\mathrm{Mb}$) and *Mycoplasma pneumoniae* (genome $0.8\,\mathrm{Mb}$). What fractions of reads do they contribute? What would a marker-gene profiler report, ideally?

   **Answer** By Formula 14.3.2, reads are in proportion $5 : 0.8$, so $5/5.8 = 86.2\,\%$ and $13.8\,\%$. A marker-gene profiler measures coverage of single-copy markers, which is proportional to genome copies, and would ideally report $50\,\%$ each. A read-based profile must divide by genome length to estimate cell fractions.

5. Explain why tetranucleotide frequencies separate genomes and why they fail for short contigs. Why does adding samples help more than adding a longer word length?

   **Answer** Each genome has a characteristic, genome-wide word composition shaped by mutational biases, codon usage and DNA repair, similar in all its regions ([7.8.7](/7.8.7#sec-7.1.2)); different species differ in it. A contig of length $\ell$ contains about $\ell$ tetranucleotides spread over $136$ canonical words, so with $\ell = 1000$ each word is counted only about $7$ times and the sampling noise of the frequencies (about $1/\sqrt{7} \approx 40\,\%$) swamps the differences between genomes; longer words make this worse ($512$ canonical 5-mers). Coverage across samples adds independent dimensions in which genomes with different abundance dynamics separate, whatever their composition; with $10$–$100$ samples, coverage profiles separate even strains of similar composition, as genomes 4 and 5 in the binning figure.

6. A MAG has $93\,\%$ completeness, $7\,\%$ contamination and no 16S gene. Classify it by MIMAG and suggest why the 16S gene is missing and how contamination might arise.

   **Answer** Completeness above $90\,\%$ but contamination of $7\,\%$ ($\geq 5\,\%$) and no rRNA genes: medium quality (it meets $\geq 50\,\%$ and $< 10\,\%$). rRNA operons are present in several nearly identical copies and conserved across species, so short-read assemblers collapse them into short contigs with high coverage and mixed composition, which binners do not assign. Contamination arises from contigs of a related strain or species with similar composition and correlated coverage, or from shared mobile elements; refinement by examining duplicated markers and coverage outliers, or by long reads, can remove it.

7. Compute the Shannon index, inverse Simpson and richness of a sample with relative abundances $(0.9, 0.05, 0.05)$ and of one with $(1/3, 1/3, 1/3)$. Which Hill number differs most between them, and why?

   **Answer** First: $H = -(0.9\ln0.9 + 2\cdot0.05\ln0.05) = 0.0948 + 0.2996 = 0.394$, ${}^1D = 1.48$; $\lambda = 0.81 + 0.0025 + 0.0025 = 0.815$, ${}^2D = 1.23$; $S = 3$. Second: $H = \ln 3 = 1.099$, ${}^1D = 3$, ${}^2D = 3$, $S = 3$. Richness is identical; the ratio is largest for ${}^2D$ ($3/1.23 = 2.4$), because higher orders weigh abundant taxa most and the first community is dominated by one taxon.

8. Prove that the clr transformation is invariant to the total, and show that the Aitchison distance between $(1, 2, 4)$ and $(2, 4, 8)$ is zero while their Bray–Curtis dissimilarity on raw counts is not.

   **Answer** $\operatorname{clr}(c\boldsymbol{x})_i = \ln\bigl(cx_i/(c\,g(\boldsymbol{x}))\bigr) = \operatorname{clr}(\boldsymbol{x})_i$, because $g(c\boldsymbol{x}) = (\prod cx_j)^{1/D} = c\,g(\boldsymbol{x})$. The second vector is twice the first, so their clr vectors and their Aitchison distance are $0$. On raw counts, $\sum\min = 1 + 2 + 4 = 7$ and $\sum(x + y) = 21$, so $\mathrm{BC} = 1 - 14/21 = 0.33$: raw-count dissimilarities mix composition with depth, which is why Bray–Curtis is computed on relative abundances (where it is $0$ here) or after rarefying.

9. In a study, the relative abundance of *Bacteroides* is lower in patients than in controls, and the total bacterial load (by flow cytometry) is $50\,\%$ higher in patients. Could the absolute abundance of *Bacteroides* be unchanged? What is it in patients, relative to controls, if its relative abundance fell from $0.30$ to $0.20$?

   **Answer** Absolute abundance = relative abundance × total load. Controls: $0.30 \times L$; patients: $0.20 \times 1.5L = 0.30L$. So the absolute abundance is unchanged; the fall in relative abundance is due entirely to growth of other taxa. Without the load measurement the two explanations cannot be distinguished, which is the core of the compositional problem (Example 14.5.1).

10. (Design) You want to know whether a new antibiotic changes the gut microbiome of patients, and whether resistance genes increase. Design the sampling, sequencing and analysis.

    **Answer** Sampling: stool from each patient before, during and after treatment, with untreated controls; standardized collection and storage; extraction blanks, PCR negatives and a mock community in every batch; spike-in or flow cytometry for total load. Sequencing: 16S V4 amplicons for all samples (cheap, many time points) and shotgun metagenomes ($\geq 10^7$ read pairs) for a subset, for species-level profiles, MAGs and resistance genes. Analysis: DADA2 ASVs and taxonomy; shotgun profiles by MetaPhlAn and Kraken 2 with Bracken; alpha diversity at equal depth or by coverage-based standardization; beta diversity by Bray–Curtis or UniFrac, PCoA and PERMANOVA with permutations restricted within patients (paired design) and a dispersion test; differential abundance with two compositional methods, modeling patient as a random effect, interpreted with absolute loads; resistance genes against CARD with abundance normalized per genome equivalent (per single-copy marker), and long reads or Hi-C on selected samples to link genes to hosts and plasmids. Control the FDR across taxa and genes.

11. (Analysis) An mNGS assay of cerebrospinal fluid from a patient finds $12$ reads per million of *Ralstonia* and $3$ reads per million of herpes simplex virus 1. The extraction blank of the same batch contains $15$ reads per million of *Ralstonia* and none of HSV-1. How do you interpret the results?

    **Answer** *Ralstonia* is a common reagent and water contaminant (part of the kitome), and the patient sample has no more of it than the blank, so it is most likely contamination and should not be reported. HSV-1 is absent from the control, is a known cause of encephalitis, and even a few reads per million can be significant in cerebrospinal fluid, which has little host DNA from which reads are drawn; it should be reported as a likely pathogen and confirmed by a specific PCR, and the reads checked to cover several regions of the viral genome rather than one repeated sequence.

12. In the lineage de-mixing of Example 14.6.1, suppose a fourth lineage appears that carries exactly the mutations of lineage 2 plus a new mutation not in the barcode matrix. What happens to the estimates, and how is this detected?

    **Answer** The new lineage's reads match lineage 2 at every barcode mutation, so its share is attributed to lineage 2: the estimates stay internally consistent and the residual does not reveal it. It is detected only through the new mutation, which appears in the sample at a frequency not explained by any known lineage; surveillance pipelines therefore report unexplained mutations, and barcode matrices are updated from clinical genomes as lineages emerge.
