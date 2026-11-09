---
title: "Systems Biology: Questions, Data and Methods"
description: "What systems biology is and why it arose: the limits of component-by-component analysis, hypothesis-driven and data-driven research and the null models that data-driven discovery needs, a short history, the map of omics layers, the kinds of biological networks and the meaning of their edges, the three tasks of reconstruction, interrogation and application, forward and inverse models with identifiability, and the public data and reproducible practice on which the field depends."
---

Twentieth-century molecular biology took living systems apart. It identified the genes, purified the enzymes, solved the structures and traced the pathways one at a time, and its success is the content of most of the preceding courses. Systems biology asks the complementary question: how do these parts, measured all at once and in their natural context, produce the behavior of a cell, a tissue or a patient? The question became practical only when technologies appeared that measure every gene, transcript, protein or metabolite in one experiment. This chapter sets out the questions (1.1), the two modes of research and the statistical discipline that data-driven work requires (1.2), the history of the field (1.3), the layers of omics data and the chapters in which each is treated (1.4), networks and models as the field's central objects (1.5), and the practice of working with public data reproducibly (1.6).

The course has three parts. Chapters 7.9.2–7.9.9 treat the omics measurements: what is measured, how reads or spectra become numbers, and which statistical model fits them. Chapters 7.9.10–7.9.13 treat networks as objects built from such data: interaction maps, regulatory networks inferred from expression, their analysis and their use in medicine and cancer. Chapters 7.9.14–7.9.17 treat the dynamics of networks and the design principles that recur in them. The statistical foundations are in [biostatistics](/7.7), in particular the analysis of high-dimensional data ([7.7.19](/7.7.19)) and large-scale inference ([7.7.20](/7.7.20)); the analysis of sequences, alignments and genomes is in [bioinformatics](/7.8); the general mathematics of networks is in [network science](/1.4.7); the physics of noise, circuits and networks is in [biophysics](/7.6) ([7.6.32](/7.6.32)–[7.6.41](/7.6.41)).

## 1.1. From Components to Systems

### 1.1.1. What Component-by-Component Analysis Achieved

The program of molecular biology can be put in a mechanical metaphor: an organism is like an intricate work of clockwork, and although taking out individual wheels does not reveal the secret of the whole, studying each wheel exactly is an advance over smashing the mechanism and analyzing the debris. The following century bore this program out. Enzyme kinetics ([7.1.7](/7.1.7)), the double helix and the **central dogma** ([7.2.1](/7.2.1)), the structures of proteins ([7.1.5](/7.1.5)), the signaling pathways of the cell ([7.1.14](/7.1.14), [7.1.15](/7.1.15)) and the genetic dissection of development ([7.5](/7.5)) were all obtained by isolating one component, or one pathway, and studying it under controlled conditions. The method is reductionist in the methodological sense: explain a phenomenon by the properties of its parts and their interactions, measured one at a time. It produced effective drugs, vaccines and diagnostics, and it remains the way most mechanisms are proven.

### 1.1.2. What It Left Open

The limits show in the problems that resist it: cancer, aging, chronic inflammatory and degenerative diseases, the response of a patient to a drug. These are not failures of a single part. The list of **hallmarks of cancer** grew from six capabilities (Hanahan and Weinberg, 2000) to ten (2011) and to fourteen with the "emerging hallmarks and enabling characteristics" of 2022 (Hanahan): each revision added properties, such as reprogrammed metabolism, evasion of immune destruction, phenotypic plasticity and the microbiome, that belong to the tumor as a system interacting with its host, not to any one mutated gene ([7.9.13](/7.9.13)).

Three kinds of complexity stand between the parts list and the behavior:

| Level | What makes it complex | Example |
|---|---|---|
| Molecular species and interactions | tens of thousands of genes, many more transcript isoforms and protein forms, thousands of metabolites; new classes (noncoding RNAs, circular RNAs) are still being found | about 20 000 human protein-coding genes, more than 200 000 annotated transcripts |
| Mechanisms | sequence, structure, modification, localization and timing all matter; one molecule plays several roles | a kinase active only when phosphorylated, at the membrane, during one phase of the cycle |
| Organization | molecules form complexes, pathways and cells; cells form tissues, organisms and populations | the same mutation with different effects in different tissues |

The behavior that results from interactions and is absent from the parts in isolation is **emergence**: bistability of a feedback loop ([7.6.33](/7.6.33)), oscillation of the cell cycle ([7.3.20](/7.3.20)), the robustness of chemotaxis to changes in protein levels ([7.6.35](/7.6.35)). Explaining such behavior requires measuring many components at once and describing their interactions quantitatively.

### 1.1.3. A Definition

**Definition 1.1.1 (Systems Biology)** **Systems biology** is the study of biological systems through the measurement, analysis and mathematical modeling of the interactions among many of their components (genes, transcripts, proteins, metabolites, cells) considered together, with the aim of explaining and predicting the behavior of the system as a whole.

The definition, close to that of Leroy Hood, has four practical consequences. The method is integrative: it combines measurements of several kinds of molecules and several levels of organization. It is quantitative: interactions are described by numbers, statistical models and equations, not only by arrows. It is interdisciplinary: biology, statistics, computer science, physics and engineering contribute, and the report of the US National Research Council *A New Biology for the 21st Century* (2009) made this integration the program for the life sciences. And it remains biology: the aim is a biological explanation, usually confirmed by the classical methods of genetics and biochemistry. Holism in this sense does not replace reductionism; it adds the step back from the parts to the whole that reductionism leaves out.

## 1.2. Two Modes of Research

### 1.2.1. Hypothesis-Driven and Data-Driven Research

In hypothesis-driven research a specific, testable hypothesis is stated first ("protein X phosphorylates Y"), and an experiment is designed to refute it. The method is efficient when there are a few good hypotheses. With twenty thousand genes, many interacting, there are too many hypotheses to test one by one and too few to choose among on prior grounds. Data-driven research reverses the order: measure everything in a well-chosen comparison (treated against untreated, tumor against normal tissue, a time course), and let the data suggest which genes, pathways or interactions deserve hypotheses. The second mode does not replace the first. A screen of the transcriptome yields candidates; a knockout, a binding assay or a reporter tests them. The key in both is the question: an unfocused measurement of everything rarely explains anything.

### 1.2.2. Data-Driven Discovery Needs a Null Model

Measuring many variables on few samples makes chance patterns abundant. Omics data are typically "wide": $p$, the number of genes, is in the tens of thousands, and $n$, the number of samples, in the tens or fewer. Any pattern found by scanning $p$ variables must be compared with what scanning would find in data with no pattern at all.

**Example 1.2.1** Take a phenotype measured in $n = 8$ samples and $p = 20\,000$ genes, none of which is related to it. For one gene, the **correlation coefficient** $r$ with the phenotype has, under independence and normality, the density $f(r) \propto (1 - r^2)^{(n-4)/2}$ on $(-1, 1)$, equivalently $r\sqrt{n-2}/\sqrt{1-r^2}$ has a $t$ distribution with $n - 2$ degrees of freedom ([3.1](/3.1)). For $n = 8$ the probability that $\lvert r\rvert > 0.8$ is $0.017$, so about $340$ of the $20\,000$ null genes are expected to correlate with the phenotype more strongly than $0.8$ (the simulation in the figure gave $325$), and the largest $\lvert r\rvert$ among them is expected to be $0.98$. With $n = 100$ samples the largest correlation expected by chance among the same $20\,000$ genes is $0.40$.

![Chance correlations in wide data. A: correlations between a random phenotype and 20000 random genes, each measured in 8 samples (histogram), with the exact null density (line); the shaded tails, beyond |r| = 0.8, hold 1.6% of the genes. B: the largest |r| expected by chance among p independent null genes, for 8, 20 and 100 samples (lines: exact expectation; points: simulation)](./plots/spurious_correlation.py)

:::

The lesson recurs throughout the course. A data-driven result is meaningful only against a null model that describes what the same analysis gives without the effect: a null distribution of a test statistic and a correction for the number of tests (**false discovery rate**, [7.7.20](/7.7.20)), a randomized network with the same degrees ([1.4.7](/1.4.7)), permuted sample labels or gene sets ([7.9.3](/7.9.3)). The second requirement is independent confirmation, by a new data set or a targeted experiment. Most omics results are associations: a gene whose expression correlates with survival is not thereby shown to cause it.

## 1.3. A Short History

| Year | Event | Significance |
|---|---|---|
| 1968 | Ludwig von Bertalanffy, *General System Theory* | systems as an object of science across disciplines |
| 1970s | metabolic control analysis (Kacser and Burns; Heinrich and Rapoport) | the first quantitative theory of control distributed over a network ([7.1.17](/7.1.17)) |
| 1995 | first complete genome of a free-living organism (*Haemophilus influenzae*); cDNA microarrays (Schena and colleagues) | genome-wide measurement becomes possible |
| 2000 | Institute for Systems Biology in Seattle (Hood); genetic toggle switch and repressilator | an institutional field; synthetic circuits as tests of design ([7.6.33](/7.6.33)) |
| 2001–2003 | draft and finished human genome; network motifs in transcription networks (Alon and colleagues, 2002) | the parts list of a human; recurring circuit elements ([7.9.15](/7.9.15)) |
| 2003–2012 | ENCODE pilot and main phases; yeast interactome and genetic-interaction maps | functional elements and interaction networks at genome scale |
| 2006–2018 | massively parallel short-read sequencing; RNA-seq (2008); The Cancer Genome Atlas | sequencing replaces hybridization; multi-omics of 33 cancer types |
| 2009 onward | single-cell RNA-seq, droplet methods (2015); Human Cell Atlas (2016); spatial transcriptomics | resolution of individual cells and their positions ([7.9.5](/7.9.5), [7.9.6](/7.9.6)) |
| 2020s | telomere-to-telomere human genome (2022); deep-learning models of sequence and structure | complete reference; prediction from sequence ([7.8](/7.8)) |

The driving force has been technology. The cost of sequencing a human genome fell from the order of $10^8$ dollars for the reference genome to the order of $10^3$ dollars around 2015 and below that since, a decline much faster than that of computing costs, and public archives of raw sequencing data have grown roughly exponentially. Data analysis, storage and interpretation, not data generation, became the bottleneck; how sequencing works is treated in [7.2.6](/7.2.6) and [7.8.9](/7.8.9).

## 1.4. The Map of Omics

**Definition 1.4.1 (Omics)** An **omics** field is the comprehensive measurement and analysis of a complete set of one class of biological entities in a sample: all genes and variants (genomics, the **genome**), all chemical modifications and conformations of chromatin (epigenomics), all transcripts (transcriptomics, the **transcriptome**), all mRNAs being translated (translatomics), all proteins (**proteomics**, the **proteome**), all metabolites (metabolomics), all molecular interactions (interactomics). The complete set of measurable traits of an organism, from morphology and physiology to disease, is its **phenome**.

Each layer answers a different question and has its own technology, noise and statistics. The table and the figure summarize them and point to the chapters.

| Layer | Measured quantity | Main technologies | Statistics of the readout | Chapter |
|---|---|---|---|---|
| Genome | sequence, variants | short- and long-read sequencing | counts of alleles at sites | [7.8.9](/7.8.9)–[7.8.13](/7.8.13) |
| Epigenome | methylation, accessibility, histone marks, 3D contacts | bisulfite sequencing, ATAC-seq, **ChIP-seq**, Hi-C | counts in peaks or bins; binomial methylation | [7.9.8](/7.9.8) |
| Transcriptome | RNA abundance and isoforms, in bulk, single cells and space | RNA-seq, microarrays | overdispersed counts | [7.9.2](/7.9.2), [7.9.4](/7.9.4)–[7.9.7](/7.9.7) |
| Translatome | ribosome-protected fragments | **ribosome profiling** | counts; ratio to mRNA | [7.9.4](/7.9.4) |
| Proteome | protein abundance, modifications | **mass spectrometry** | intensities with missing values | [7.9.9](/7.9.9) |
| Metabolome | metabolite levels, fluxes | MS coupled to chromatography, **nuclear magnetic resonance** | intensities; isotope labeling | [7.9.9](/7.9.9) |
| Interactome | physical and genetic interactions | two-hybrid, affinity purification, CRISPR screens | binary or scored edges | [7.9.10](/7.9.10) |
| Phenome | traits | imaging, clinical records, wearables | mixed types | [7.7](/7.7) |
| Microbiome | communities of microorganisms | amplicon and shotgun metagenomics | compositional counts | [7.8.14](/7.8.14) |

![The layers of omics data, from genome to phenome. Downward arrows: the flow of genetic information; dashed arrows: regulation by proteins and metabolites of chromatin and transcription, which closes the loop. For each layer: what is measured, the main technologies and the finest resolution in routine use; the interactome links the molecules of the middle layers](./plots/omics_layers.py)

Three axes organize the technologies. Coverage ranges from targeted panels of tens of genes to the whole genome. Resolution ranges from a population of millions of cells to single cells and to positions within a tissue section. Time is rarely measured directly: most omics data are snapshots, and dynamics must be inferred from time courses, from perturbations or from the cell-to-cell variation in one snapshot ([7.9.7](/7.9.7)). The layers are not independent. Transcript and protein levels correlate only moderately across genes, because translation and degradation rates differ ([7.9.4](/7.9.4), [7.9.9](/7.9.9)); integrating layers is therefore informative, not redundant.

**Example 1.4.1** How large is one human genome sequenced at $30\times$ **sequencing coverage**? The haploid genome has $G \approx 3.1\times10^9$ bases, so $30\times$ requires $9.3\times10^{10}$ sequenced bases, or $6.2\times10^8$ reads of $150$ bases ($3.1\times10^8$ read pairs). A FASTQ file ([7.8.1](/7.8.1)) stores one byte for each base and one for its quality value, plus a header of the order of $60$ bytes per read: about $1.9\times10^{11} + 0.4\times10^{11} \approx 2.2\times10^{11}$ bytes, $220$ GB uncompressed for one person. A cohort of $10\,000$ genomes is of the order of petabytes, which is why compressed and reference-based formats, and analysis where the data are stored, became necessary.

## 1.5. Networks and Models

### 1.5.1. Kinds of Networks

The interactions that the definition of systems biology puts at the center are represented as networks: graphs whose vertices are molecules (or genes, cells, diseases) and whose edges are relations between them ([1.4.1](/1.4.1)). What an edge means differs from one kind of network to another, and confusing the meanings is a common error.

| Network | Vertices | Edge means | Type of graph | Main sources | Chapter |
|---|---|---|---|---|---|
| Transcriptional regulatory | transcription factors, target genes | the factor binds the regulatory region and changes transcription | **directed graph**, signed | ChIP-seq, perturbations, footprints | [7.9.11](/7.9.11), [7.9.15](/7.9.15) |
| Protein interaction | proteins | physical binding, direct or within a complex | undirected | two-hybrid, affinity purification | [7.9.10](/7.9.10) |
| Signaling | proteins, second messengers | modification or activation of one by another | directed, signed | biochemistry, phosphoproteomics | [7.9.16](/7.9.16) |
| Metabolic | metabolites and reactions | a metabolite is a substrate or product of a reaction | **bipartite graph**, directed | genome annotation, biochemistry | [7.6.34](/7.6.34), [7.9.14](/7.9.14) |
| Genetic interaction | genes | the double mutant deviates from the expected combination of single mutants | undirected, signed | double-mutant screens | [7.9.10](/7.9.10) |
| Co-expression | genes | expression is correlated across samples | undirected, weighted | expression compendia | [7.9.11](/7.9.11) |
| Disease | diseases, genes | shared genes, or a gene implicated in a disease | bipartite | genetics, literature | [7.9.12](/7.9.12) |

The edges of the first four kinds are physical or causal; those of the last three are functional or statistical. A co-expression edge says that two genes vary together, which may mean that one regulates the other, that both are regulated by a third, or that both are specific to a cell type whose proportion varies among samples. A genetic-interaction edge (an instance of **epistasis**, [7.4.4](/7.4.4)) may join genes whose products never touch, for example two parallel pathways whose loss is tolerated singly but not together, the case of **synthetic lethality**.

![Four kinds of biological network and the meaning of their edges. A: transcriptional regulation in *E. coli*, directed and signed: CRP and AraC activate the araBAD operon (green), CRP also activates the lac operon, which LacI represses (red). B: a protein-interaction network, undirected, with a hub (orange). C: a metabolic network as a bipartite graph of metabolites and reactions (blue: hexokinase, phosphoglucose isomerase, phosphofructokinase), with ATP and ADP as co-substrates. D: a genetic-interaction network, signed: negative interactions (red, dashed: the double mutant is sicker than expected) and positive ones (green)](./plots/network_types.py)

Large biological networks share statistical features, among them a broad **degree distribution** with a few highly connected **hubs**, short paths and local clustering; whether particular networks are **scale-free networks** is debated. These properties, and the random-graph models used as null models for them, are the subject of [network science](/1.4.7); here and in [7.6.34](/7.6.34) we use them.

### 1.5.2. The Three Tasks

Most work in systems biology falls into three tasks:

1. Reconstruction: building a network from data, by measuring interactions directly ([7.9.10](/7.9.10)) or by inferring them from the covariation of measured quantities ([7.9.11](/7.9.11)).
2. Interrogation: analyzing the network, its topology, its key vertices and modules, its dynamics, and validating predictions experimentally ([7.9.12](/7.9.12), [7.9.14](/7.9.14)–[7.9.17](/7.9.17)).
3. Application: using the network to explain a mechanism, to find drug targets or biomarkers, or to design new circuits ([7.9.13](/7.9.13), [7.9.17](/7.9.17)).

A typical disease study runs from the bedside to the bench and back: tissue samples from patients and models in animals or cell lines are profiled at several molecular levels, the data are analyzed and integrated, a disease-specific network is reconstructed, its key regulators are predicted and then tested by perturbing them in the models.

![The working cycle of systems biology: a question fixes the perturbations and measurements; omics profiling, statistics and integration lead to a reconstructed network, which is interrogated and modeled; predictions are tested by experiments that refine the question. The reconstructed network also suggests directly which perturbation to make next (dashed)](./plots/workflow.py)

### 1.5.3. Forward and Inverse Models

A network diagram becomes a model when its edges are given mathematical form: rate laws in an **ordinary differential equation**, logical rules in a Boolean network, conditional distributions in a statistical model. Two directions of reasoning use such a model.

**Definition 1.5.1** A **forward model** computes the behavior of a system (trajectories, steady states, the distribution of observations) from its structure and parameters. An **inverse model** runs the other way: it infers the structure or the parameters of a system from observations of its behavior, usually by maximizing a likelihood or minimizing a discrepancy between model and data.

Forward modeling answers "what would happen if": simulating the effect of a knockout, a drug dose or a change in a feedback strength. Inverse modeling, also called reverse engineering in systems biology, answers "what must the system be like to have produced these data". Network inference from expression data ([7.9.11](/7.9.11)) and fitting rate constants to time courses ([7.9.14](/7.9.14)) are inverse problems. They are usually harder than forward ones: different parameters or wirings may explain the same data equally well.

**Example 1.5.1** A gene switched on at $t = 0$ is produced at rate $\beta$ and degraded at rate $\alpha x$: $\dot x = \beta - \alpha x$, $x(0) = 0$. The forward solution is $x(t) = (\beta/\alpha)(1 - \mathrm{e}^{-\alpha t})$, rising with initial slope $\beta$ to the steady state $\beta/\alpha$ with time constant $1/\alpha$. For the inverse problem, suppose $x$ is measured with $10\%$ noise. If the time course covers several time constants, both the plateau $\beta/\alpha$ and the approach to it are seen, and both parameters are bounded. If only the first part of the rise is measured ($t \le 1$ for $\alpha = 0.5$), then $x(t) \approx \beta t - \tfrac12\alpha\beta t^2$ is nearly linear: $\beta$ is determined, $\alpha$ is not, and the residual sum of squares is almost flat along the $\alpha$ axis (figure, panel C). The parameter is practically non-identifiable for this design, a property of the experiment and not of the model ([7.9.14](/7.9.14)).

![Forward and inverse problems for gene induction, dx/dt = β − αx. A: trajectories for three parameter sets (forward problem) and two noisy data sets simulated from α = 0.5, β = 1: a full time course (circles) and early points only (squares). B, C: the inverse problem, the residual sum of squares over the (α, β) plane, with contours at 2, 4 and 8 times its minimum (cross: true value; dot: least-squares estimate). The full time course bounds both parameters; the early points determine only β](./plots/forward_inverse.py)

## 1.6. Public Data and Reproducible Analysis

### 1.6.1. Where the Data Are

Omics data are shared as a matter of course, and reusing public data is a large part of the field. The archives form layers:

| Layer | Content | Examples |
|---|---|---|
| Raw data | reads with quality values, mass spectra | Sequence Read Archive (SRA), European Nucleotide Archive (ENA), Genome Sequence Archive (GSA, China), PRIDE (proteomics) |
| Processed data with metadata | count or intensity matrices, sample descriptions | Gene Expression Omnibus (GEO), ArrayExpress |
| Consortium resources | uniformly processed data of a defined scope | ENCODE (functional elements), TCGA (cancer), GTEx (normal tissues), Human Cell Atlas, Human Protein Atlas, DepMap (cancer dependencies) |
| Knowledge bases | curated annotations and interactions | Gene Ontology, KEGG, Reactome, STRING ([7.9.3](/7.9.3), [7.9.10](/7.9.10)) |

A study deposited in these archives is reached through a chain of accession numbers: a BioProject (PRJNA…) groups the study, a GEO series (GSE…) holds its processed data and sample descriptions (GSM…), and SRA experiments and runs (SRX…, SRR…) hold the reads. The data used in the next chapter, for example, are GEO series GSE52778, with one SRR run per sample. Gene and genome databases, identifiers and coordinates are treated in [7.8.2](/7.8.2).

### 1.6.2. Software

Two open ecosystems carry most of the analysis. Bioconductor, founded in 2001, provides several thousand R packages for genomic data, with common data structures and two releases a year; DESeq2, edgeR and limma for differential expression are among them. scverse is a Python consortium around the AnnData data structure for annotated matrices, with Scanpy for single-cell analysis, Squidpy and SpatialData for spatial data and scvi-tools for probabilistic models ([7.9.5](/7.9.5), [7.9.6](/7.9.6)); statistical methods of Bioconductor are reimplemented in Python where needed (pydeseq2, decoupler). Command-line tools written in C, C++ or Rust do the heavy steps of alignment and quantification ([7.8.10](/7.8.10)), and workflow managers (Snakemake, Nextflow) chain them. This course writes analyses in Python and names the R equivalents.

### 1.6.3. Rules of Practice

Reproducibility means that the same data and code give the same result, and that another person can rerun the analysis. A few rules carry most of the weight:

1. Before analyzing data, know how they were produced and check their quality: base and mapping quality, the signal at known loci, whether replicates cluster together, comparison with similar public samples ([7.9.2](/7.9.2)).
2. Keep raw data unchanged and every step from raw data to figure in code, with software versions recorded (an environment file or container) and random seeds fixed.
3. Record where every number in a paper or report comes from: which data, which code, which parameters.
4. Consider alternative explanations of every pattern: batch, cell-type composition, sample quality, the choice of background ([7.9.3](/7.9.3)).
5. Seek independent confirmation: a second data set, a different technology, a targeted experiment.

Code assistants based on language models write analysis scripts quickly. The rules apply to their output with greater force: run the code on data whose answer is known, inspect intermediate results, and check that each function does what its name suggests, since a plausible but wrong analysis is harder to notice than a broken one.

## Summary

- Molecular biology explained components one at a time (1.1.1); diseases and other system-level behaviors, including **emergence**, motivate studying many components together (1.1.2). Systems biology measures, analyzes and models the interactions of many components to explain the behavior of the whole (Definition 1.1.1).
- Hypothesis-driven and data-driven research complement each other (1.2.1). In wide data ($p \gg n$) chance patterns abound: with $n = 8$ samples about $1.7\%$ of null genes correlate with a phenotype beyond $\lvert r\rvert = 0.8$ (Example 1.2.1). Data-driven results need a null model and independent confirmation (1.2.2).
- The field grew with technology: genome sequencing, microarrays, high-throughput sequencing, single-cell and spatial methods (1.3).
- Omics fields measure complete sets of one class of entities, from genome to phenome (Definition 1.4.1); each layer has its own technology, readout statistics and chapter (table in 1.4). A $30\times$ human genome is about $2\times10^{11}$ bytes of raw reads (Example 1.4.1).
- Networks represent interactions; their edges may be physical, causal, functional or statistical, and must be read accordingly (1.5.1). The three tasks are reconstruction, interrogation and application (1.5.2).
- A forward model predicts behavior from parameters, an inverse model infers parameters or structure from data (Definition 1.5.1); identifiability depends on the experimental design (Example 1.5.1).
- Public archives (SRA, GEO, consortium resources), open software (Bioconductor, scverse) and rules of practice (quality control, code for every step, alternative explanations, confirmation) make analyses reusable and reproducible (1.6).

## Questions

1. Why can the list of all parts of a cell not, by itself, explain its behavior? Give two examples from earlier courses.

   **Answer** Behavior depends on how the parts interact: the signs, strengths and timing of interactions, and the structure of the network they form. A genetic toggle switch is built from two ordinary repressors; its bistability and memory appear only from the mutual repression with sufficiently cooperative binding ([7.6.33](/7.6.33)). The robust adaptation of bacterial chemotaxis does not reside in any one protein but in the integral feedback of the methylation system ([7.6.35](/7.6.35)). In both cases a parts list without the interaction structure and its parameters predicts nothing about the behavior.

2. A study measures the expression of $20\,000$ genes in $10$ tumors and reports the gene most correlated with tumor size, with $r = 0.85$. Is this evidence of an association?

   **Answer** Not by itself. Under the null hypothesis of no association, for $n = 10$ the statistic $r\sqrt{8}/\sqrt{1-r^2}$ has a $t_8$ distribution; $r = 0.85$ gives $t = 4.56$ and a two-sided **p-value** of about $1.9\times10^{-3}$. Among $20\,000$ null genes about $37$ would reach this level by chance, and the expected largest $\lvert r\rvert$ is above $0.9$. The gene must be judged against the distribution of the maximum, or with a multiple-testing correction, and confirmed in independent samples.

3. Which omics layer, and which technology, would you use to find (a) the proteins whose phosphorylation changes within five minutes of growth-factor stimulation, (b) the genes whose transcription is directly controlled by a transcription factor, (c) the cell types that change in proportion in an inflamed tissue?

   **Answer** (a) The proteome, specifically the phosphoproteome, by mass spectrometry after enrichment of phosphopeptides; transcript levels change too slowly and do not report modification ([7.9.9](/7.9.9)). (b) Binding by ChIP-seq or a related method combined with a perturbation of the factor and RNA-seq: binding alone does not prove regulation, and expression changes alone do not prove directness ([7.9.8](/7.9.8), [7.9.11](/7.9.11)). (c) Single-cell RNA-seq, or spatial transcriptomics if the location matters; bulk measurements confound proportions with expression per cell ([7.9.5](/7.9.5), [7.9.6](/7.9.6)).

4. Two genes are joined by an edge in a co-expression network built from $500$ tissue samples. List three mechanisms that could produce the edge, and an experiment that distinguishes them.

   **Answer** One gene regulates the other (directly, or through intermediates); both are regulated by a common factor; both are expressed in the same cell type, whose proportion varies among the samples. Perturbing one gene (knockdown or CRISPR inhibition) and measuring the other separates the first from the other two; analyzing single cells, or adjusting for estimated cell-type proportions, tests the third; ChIP-seq of candidate regulators tests the second.

5. Why is a metabolic network naturally a bipartite graph? What is lost if it is drawn as a graph of metabolites only, with an edge between substrate and product?

   **Answer** A reaction relates several substrates to several products jointly, with fixed stoichiometry, so the natural objects are two kinds of vertex, metabolites and reactions, with edges from substrates to a reaction and from it to products ([7.6.34](/7.6.34)). Projecting onto metabolites loses which metabolites react together and in what proportions, and it turns currency metabolites such as ATP, which take part in hundreds of reactions, into huge spurious hubs that create short paths with no biochemical meaning.

6. In Example 1.5.1, what measurement schedule would you choose to estimate both $\alpha$ and $\beta$ well, if the degradation rate is expected to lie between $0.1$ and $1\ \mathrm{h}^{-1}$?

   **Answer** The data must cover the rise and the plateau, that is several time constants $1/\alpha$ for the slowest plausible $\alpha$: up to about $3/0.1 = 30$ h, with points concentrated where the curve bends (around $1/\alpha$, between $1$ and $10$ h), for example logarithmically spaced times from $0.25$ to $30$ h. Early points fix $\beta$, late points fix $\beta/\alpha$, and together they fix $\alpha$. Alternatively, a shut-off experiment (stop production and follow the decay) measures $\alpha$ directly.

7. Estimate the raw data volume of a bulk RNA-seq experiment with $12$ samples at $30$ million read pairs each, $2\times100$ bases.

   **Answer** Each sample has $6\times10^7$ reads of $100$ bases, $6\times10^9$ bases. At about two bytes per base plus about $60$ bytes per read, that is $1.2\times10^{10} + 0.36\times10^{10} \approx 1.6\times10^{10}$ bytes, $16$ GB per sample uncompressed, about $190$ GB for the experiment; gzip compression reduces it severalfold. The count matrix that results, $60\,000$ genes by $12$ samples, is a few megabytes: quantification compresses the data by four orders of magnitude.

8. A colleague proposes to download all public RNA-seq data of a tissue, combine them, and look for genes whose expression differs between men and women. What are the main pitfalls, and how would you address them?

   **Answer** Batch effects: studies differ in library protocol, read length, sequencer and processing, and if the proportion of men differs between studies, study and sex are confounded ([7.9.2](/7.9.2)); the remedy is to reprocess all raw data with one pipeline and to model study as a covariate, keeping only studies that contain both sexes. Metadata errors: recorded sex should be checked against the expression of Y-chromosome genes and of *XIST*. Composition: differences in cell-type proportions or in tissue sampling can mimic expression differences; deconvolution or single-cell references help. Multiple testing across tens of thousands of genes requires FDR control, and results should be replicated in an independent cohort.

9. Explain why "systems biology is biology, not mathematics or computation" is consistent with its reliance on mathematical models.

   **Answer** The models are tools for answering biological questions: they make the consequences of an assumed mechanism explicit and testable, and they show which measurements would discriminate between mechanisms. A model is judged by whether it explains and predicts biological observations and survives experimental tests, not by its mathematical interest. Mathematics and computation are as necessary to systems biology as they are to physics, but the object of study, and the final arbiter, is the living system.
