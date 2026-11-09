---
title: Interactomes and Genetic-Interaction Networks
description: "How networks of molecular interactions are measured: kinds of interactions; binary assays (yeast two-hybrid, protein-fragment complementation, FRET and BRET) and their errors; co-complex methods (affinity purification–mass spectrometry with spoke and matrix models and SAINT-type scoring, co-fractionation, crosslinking) and proximity labeling (BioID, TurboID, APEX, PLA); computational inference from genomic context, phylogenetic profiles, interologs, co-expression, structure and coevolution; integration of evidence in STRING, quality assessment and capture–recapture estimates of interactome size, sampling bias and a SARS-CoV-2 host-interaction map; genetic interactions, SGA and E-MAP, interaction profiles and their clustering; and pooled CRISPR screens with negative binomial counts and robust rank aggregation, combinatorial screens and enhancer epistasis."
---

The previous chapters measured the abundances of molecules; this one measures their relations. A cell's function depends less on the list of its proteins than on which of them bind each other, form complexes, modify each other, and which genes can compensate for the loss of which others. Two kinds of networks record these relations. Physical interaction networks, the interactome, have proteins (and other molecules) as vertices and binding as edges. Genetic interaction networks have genes as vertices and an edge when the phenotype of a double perturbation deviates from what the single perturbations predict, an **epistasis** in the quantitative sense of [7.4.4](/7.4.4#fml-4.3.1). The first describes the machinery, the second its functional logic; the two overlap only partly, and the difference is informative.

This chapter treats how such networks are measured and how far the measurements can be trusted. We distinguish the kinds of interactions (10.1), describe the experimental methods for binary interactions (10.2) and for complexes and neighborhoods (10.3), computational prediction (10.4), the integration of evidence and the assessment of quality and coverage (10.5), genetic interactions in yeast (10.6) and pooled CRISPR screens in human cells (10.7). The mathematics of networks, their **degree distribution**, **hubs**, **centrality** and **community structure**, is in [1.4.7](/1.4.7); the analysis of biological networks once they are built is in [7.9.12](/7.9.12), and regulatory networks inferred from expression in [7.9.11](/7.9.11). Mass spectrometry, on which several methods here rely, is in [7.9.9](/7.9.9); the genetics of screens in [7.4.19](/7.4.19#sec-19.5).

## 10.1. Kinds of Interactions

**Definition 10.1.1 (Interactome)** The **interactome** of a cell or organism is the complete set of the molecular interactions among its components; in the narrow sense used most often, the set of physical protein–protein interactions, represented as an undirected graph whose vertices are proteins and whose edges are pairs that bind each other directly or as members of a complex.

The word "interaction" covers relations of very different nature, and the meaning of an edge depends on the method that produced it ([7.9.1](/7.9.1#sec-1.5.1)).

| Property | Kinds | Example | Typical method |
|---|---|---|---|
| Nature | physical, genetic, functional | subunits of RNA polymerase; synthetic lethal paralogs; enzymes of one pathway | two-hybrid, AP-MS; double mutants; co-expression, text |
| Directness | direct (binary contact) or indirect (same complex) | a subunit binding its neighbor; two subunits on opposite sides of a complex | two-hybrid; AP-MS |
| Stoichiometry | homomeric, heteromeric | hemoglobin $\alpha_2\beta_2$ | crosslinking, native MS |
| Lifetime | obligate and stable, or transient | ribosome; kinase–substrate | AP-MS; proximity labeling |
| Context | constitutive or conditional | binding that requires phosphorylation or a ligand | condition-specific assays |

Two facts follow. Binary methods and co-complex methods measure different graphs of the same machinery and must not be merged without saying so (10.3.2). And a physical interaction is necessary but not sufficient for function: two proteins that bind in a test tube or in a yeast nucleus may never meet in the cell, because they are expressed in different tissues or compartments. Interactomes are therefore maps of possible interactions; which of them are realized depends on expression, localization and modification in each cell type.

## 10.2. Binary Assays

### 10.2.1. The Yeast Two-Hybrid System

The **yeast two-hybrid** system (Fields and Song, 1989) reconstitutes a transcription factor from two proteins that bind each other. The bait protein is fused to the DNA-binding domain of the yeast activator Gal4 (or LexA), the prey to its activation domain; if bait and prey bind in the yeast nucleus, the activation domain is brought to the promoter of a reporter gene (such as *HIS3*, *ADE2* or *lacZ*), and the yeast grows on selective medium or turns blue. Screens test a bait against a library of preys, or arrays of baits against arrays of preys, and are fully automatable; proteome-scale maps were made for yeast (Uetz and colleagues, 2000; Ito and colleagues, 2001; Yu and colleagues, 2008) and humans, the latest human reference map, HuRI, containing about $53\,000$ interactions among about $8000$ proteins (Luck and colleagues, 2020).

Errors arise in both directions.

| False negatives | False positives |
|---|---|
| the prey is not in the library, or not in frame | baits that activate the reporter alone (autoactivators) |
| proteins misfold or lack their modifications in yeast | "sticky" preys that bind many baits |
| membrane and secreted proteins, which cannot reach the nucleus | binding of proteins that are never co-expressed or co-localized in their own cells |
| interactions that need a third protein | interactions normally prevented by other proteins |
| fusions that block the binding surface | |

Controls are built into modern screens: autoactivating baits are removed before screening, each positive pair is retested in fresh yeast, and only pairs found repeatedly or in both orientations (bait–prey and prey–bait) are kept. Their quality is then measured on reference sets (10.5.2). Systematic Y2H maps are not more error-prone than curated literature (Yu and colleagues, 2008), but they detect only a fraction of all true interactions in any single screen, typically $10$–$30\,\%$ of a reference set, which is why the sensitivity of a screen must be known before its negatives are interpreted.

Variants extend the principle: membrane yeast two-hybrid reconstitutes split ubiquitin at the membrane, yeast one-hybrid tests proteins binding a DNA bait (used for gene regulatory networks, [7.9.11](/7.9.11)), and mammalian two-hybrid systems test pairs in human cells.

### 10.2.2. Complementation and Energy Transfer

Protein-fragment complementation splits a reporter protein into two inactive halves fused to the two candidate partners; binding brings the halves together and restores the reporter. **Bimolecular fluorescence complementation** (BiFC; Hu, Chinenov and Kerppola, 2002) uses halves of a fluorescent protein, whose reassembly is practically irreversible, so BiFC records transient interactions but cannot follow their dissociation, and it shows where in the cell the complex forms. Split luciferase complementation (LCI in plant cells) gives a reversible, quantitative luminescence signal. Split dihydrofolate reductase complementation, read as survival in methotrexate, was used for a proteome-scale map in living yeast cells (Tarassov and colleagues, 2008).

**Förster resonance energy transfer** reports proximity of a donor and an acceptor fluorophore through the $R^{-6}$ dependence of transfer efficiency on distance, measurable only within about $10\,\mathrm{nm}$ ([7.6.11](/7.6.11#sec-11.5.7), [7.6.12](/7.6.12#sec-12.5)); in bioluminescence resonance energy transfer (BRET) the donor is a luciferase, which removes the background excitation of the acceptor. Both work in living cells, are reversible and give kinetics, and are used to validate interactions and to study receptor dimerization and the dynamics of signaling complexes, but not to map proteomes.

## 10.3. Complexes and Neighborhoods

### 10.3.1. Affinity Purification–Mass Spectrometry

**Definition 10.3.1 (Affinity Purification–Mass Spectrometry)** In **affinity purification–mass spectrometry** (AP-MS) a bait protein, tagged (FLAG, HA, Strep, GFP, tandem tags) or recognized by a specific **antibody**, is purified from a cell lysate under conditions that preserve noncovalent binding, and the co-purifying proteins (the preys) are identified and quantified by **tandem mass spectrometry**; the result is the set of proteins associated with the bait directly or through other members of its complexes.

AP-MS is **co-immunoprecipitation** made comprehensive: it detects the preys without knowing them in advance, in the bait's own cell type, with its modifications. Large maps have been produced by expressing tagged baits in human cell lines (the BioPlex network, more than $100\,000$ interactions in HEK293T and HCT116 cells; Huttlin and colleagues, 2021) and in yeast (Gavin and colleagues, 2006; Krogan and colleagues, 2006).

The raw result is noisy: every purification also contains abundant proteins (ribosomal proteins, chaperones, cytoskeleton), proteins sticking to the tag, beads or antibody, and post-lysis associations. Scoring separates specific from background preys by comparing each bait's purification with negative controls (empty tag, unrelated baits). SAINT (significance analysis of interactome; Choi and colleagues, 2011) models the spectral counts or intensities of each prey with a bait as a mixture of a true-interaction distribution and a false-interaction distribution estimated from the controls, and reports the posterior probability that the prey is a true interactor. CompPASS (Sowa and colleagues, 2009) scores preys by their abundance with the bait, their reproducibility and their specificity relative to a large collection of unrelated baits, so that a prey seen with every bait scores low. MiST combines abundance, reproducibility and specificity into one score. Contaminant repositories (the CRAPome) list the background frequency of each protein across many control purifications.

**Example 10.3.1** A purification of a bait identifies prey $X$ with $25$ spectra in each of three replicates, while across $50$ control purifications prey $X$ has a mean of $0.5$ spectra. Under a Poisson background with mean $0.5$, the probability of $25$ or more spectra in one control run is about $10^{-33}$; the prey is specific. A ribosomal protein with $60$ spectra in the bait purification but $40$ on average in the controls is not: its excess is within the variation of an abundant background protein, and its count with the bait is $1.5$ times the background, not $50$ times.

### 10.3.2. From Co-Complex Data to Edges

AP-MS gives sets of proteins, not binary contacts. Two conventions convert a purification into edges.

![From a purified complex to binary edges. A: a hypothetical complex of six subunits with its five direct contacts; the bait B (blue) touches only two of them. B: the spoke model joins the bait to every co-purified prey (5 edges, 2 of them direct contacts, green). C: the matrix model joins every pair of co-purified proteins (15 edges, 5 of them direct contacts). Both say that the proteins share a complex, not which ones touch](./plots/spoke_matrix.py)

In the spoke model the bait is linked to every prey; in the matrix model every pair of co-purified proteins is linked. For a complex of $s$ subunits purified with one bait, the spoke model gives $s - 1$ edges and the matrix model $\binom{s}{2}$, and the physical contacts are a subset of the matrix edges, of size often close to $s - 1$. Spoke expansion makes the baits artificial hubs, matrix expansion turns every complex into a clique and inflates the **clustering coefficient**; either choice changes the topology of the resulting network ([1.4.7](/1.4.7)) and must be stated when network statistics are compared. The structure of complexes, which subunits touch, comes from **crosslinking mass spectrometry**, in which crosslinked peptides identify pairs of residues within the span of the crosslinker (about $10$–$30$ Å for common reagents), and from structural methods.

### 10.3.3. Co-Fractionation

Co-fractionation identifies complexes without tagging any protein: a native lysate is separated by size-exclusion or ion-exchange chromatography into tens to hundreds of fractions, each fraction is analyzed by quantitative mass spectrometry, and proteins whose elution profiles across the fractions are highly correlated are inferred to be in the same complex (Havugimana and colleagues, 2012). Correlation alone is ambiguous (unrelated proteins of the same size co-elute), so profiles are combined with other evidence by classifiers trained on known complexes, and conserved co-elution across species strengthens the inference. Thermal proteome profiling exploits the fact that proteins in a complex often unfold and aggregate at similar temperatures.

### 10.3.4. Proximity Labeling

**Definition 10.3.2 (Proximity Labeling)** In **proximity labeling** a bait protein is fused to an enzyme that converts a substrate into a short-lived reactive species, which covalently tags proteins within a radius of about $10$–$20\,\mathrm{nm}$ in living cells; the tagged proteins, usually biotinylated, are purified with streptavidin under denaturing conditions and identified by mass spectrometry.

The enzymes are promiscuous biotin ligases, which activate **biotin** as biotinyl-AMP (BioID, Roux and colleagues, 2012, labeling over $18$–$24$ hours; TurboID, Branon and colleagues, 2018, evolved to label within $10$ minutes), and engineered ascorbate peroxidase (APEX), which oxidizes biotin-phenol to a phenoxyl radical with a lifetime below a millisecond in the presence of hydrogen peroxide, labeling within one minute. Because labeling happens in intact cells and the purification can be harsh, proximity labeling captures weak and transient interactions and the contents of compartments that dissolve on lysis, such as membraneless organelles, synapses or the surface of an organelle; its result is a neighborhood, not a set of binding partners, and must be compared with controls expressing the enzyme alone in the same compartment. Split versions active only when two halves meet label at contact sites between organelles.

The proximity ligation assay (PLA; Söderberg and colleagues, 2006) detects proximity of two proteins in fixed cells or tissue: two primary antibodies are recognized by secondary antibodies carrying oligonucleotides, which, if within about $40\,\mathrm{nm}$, template the ligation of a circular DNA that is amplified by rolling-circle amplification into a bright spot. It counts interaction events cell by cell in situ, and variants combine it with in situ hybridization to detect proximity of a protein to an RNA.

## 10.4. Computational Inference

Experiments cover only part of the interactome and few species; computation fills in, at the price of predicting functional associations rather than physical contacts.

| Evidence | Principle | First proposed |
|---|---|---|
| Gene neighborhood | genes kept adjacent in many genomes, especially in bacterial **operons**, tend to work together | Dandekar and colleagues, 1998; Overbeek and colleagues, 1999 |
| Gene fusion | two proteins that occur fused into one chain in another organism ("Rosetta stone" proteins) tend to interact | Marcotte and colleagues, 1999; Enright and colleagues, 1999 |
| Phylogenetic profile | proteins gained and lost together across genomes work together (Definition 10.4.1) | Pellegrini and colleagues, 1999 |
| Interologs | interactions transferred between species through **orthologs** | Walhout and colleagues, 2000 |
| Co-expression | genes correlated across many conditions share regulation and often function | Eisen and colleagues, 1998 |
| Coevolution and structure | correlated mutations at interface residues; structural prediction of the complex | Ovchinnikov and colleagues, 2014; Humphreys and colleagues, 2021 |
| Text mining | co-mention in abstracts and full texts | |

**Definition 10.4.1 (Phylogenetic Profile)** The **phylogenetic profile** of a protein is the binary vector (or vector of similarity scores) indicating whether a **homolog** of the protein is present in each of a set of sequenced genomes; proteins with similar profiles across many genomes are predicted to be functionally linked.

Profiles work because proteins of one pathway or complex are useless without each other and are therefore retained or lost together: the flagellar proteins disappear together from nonmotile bacteria. The similarity of two profiles is measured by mutual information, by a **hypergeometric distribution** p-value for the number of genomes containing both, or better by methods that account for the phylogeny, since closely related genomes are not independent observations.

**Coevolution** at the residue level is a stronger signal: residues in contact across an interface mutate in a correlated way, and direct coupling analysis of concatenated alignments of the two families separates direct from transitive correlations. Combined with deep learning structure prediction, this turns sequence alignments into predicted complex structures: screens of all pairs of yeast proteins with coevolution and structure prediction proposed several hundred new complexes (Humphreys and colleagues, 2021), and **AlphaFold** models of complexes (AlphaFold-Multimer and its successors, [7.8.17](/7.8.17)) now assign interface confidences to candidate pairs. Structural predictions identify the interface, not whether the interaction occurs in the cell; they are best used to rank experimental candidates and to explain them.

## 10.5. Integration and Quality

### 10.5.1. Combining Evidence

Databases integrate the many sources. BioGRID and IntAct curate experimentally reported physical and genetic interactions with their methods and references, using controlled vocabularies (the PSI-MI standard). STRING (Szklarczyk and colleagues) integrates experimental data, curated pathways, computational predictions and text mining into one network of functional associations for thousands of organisms, each evidence channel scored by benchmarking against KEGG pathways as a calibration of the probability that two proteins are in the same pathway.

**Formula 10.5.1 (Combining Independent Evidence)** Let $s_1, \dots, s_c$ be the scores of the evidence channels for a protein pair, each an estimated probability of association, and $p$ the prior probability that two random proteins are associated ($0.041$ in STRING). With the prior removed from each channel, $s_i' = \max\{0, (s_i - p)/(1 - p)\}$, the channels are combined as independent pieces of evidence and the prior is added back once:
$$
S' = 1 - \prod_{i=1}^{c} (1 - s_i'), \qquad S = S' + p\,(1 - S'). \tag{10.1}
$$

**Example 10.5.1** In the figure, the pair A–B has co-occurrence $0.35$, co-expression $0.48$, experiments $0.62$ and text mining $0.55$. Removing the prior gives $0.322$, $0.458$, $0.604$ and $0.531$; the product of their complements is $0.678 \times 0.542 \times 0.396 \times 0.469 = 0.068$, so $S' = 0.932$ and $S = 0.932 + 0.041 \times 0.068 = 0.934$. Combining the raw scores without removing the prior would give $0.942$: the prior would be counted four times. No channel is above $0.62$, yet the combined score exceeds the conventional high-confidence threshold of $0.7$.

![Combining evidence channels into one confidence score per protein pair (Formula 10.5.1; illustrative channel scores). A: a small network; each edge carries its combined score; blue: S ≥ 0.7, black: 0.4 ≤ S < 0.7, dashed grey: S < 0.4. B: the channels of the pair A–B and their combination](./plots/string_evidence.py)

:::

Independence is an assumption: text mining partly re-reports the experiments, and co-expression and pathway databases partly reflect each other, so the combination is optimistic when channels share sources. A combined score is a confidence that two proteins are functionally associated, not that they bind; users who need physical interactions select the physical subnetwork or the experimental channel.

### 10.5.2. Measuring Quality

The quality of an interaction data set is measured against reference sets: a positive reference set of well-documented interactions (each supported by several publications and methods) and a random reference set of protein pairs drawn at random, which are almost all non-interacting. Testing both with the same assay estimates its sensitivity (fraction of the positive set detected) and its false positive rate (fraction of the random set detected); with the latter and the prior fraction of true pairs, Bayes' theorem gives the precision of the data set (Braun and colleagues, 2009; Venkatesan and colleagues, 2009). Independent validation of a random sample of the reported interactions by an orthogonal assay measures precision directly. Literature-curated interactions supported by a single publication proved to be no more reliable than systematic screens, and recuration found many of them poorly supported (Cusick and colleagues, 2009).

### 10.5.3. How Large Is the Interactome?

Each screen detects a fraction of the true interactions, so the size of the interactome must be estimated, not counted. The classical tool is capture–recapture.

**Formula 10.5.2 (Capture–Recapture Estimate)** Let two independent screens of the same search space report $n_1$ and $n_2$ interactions with precisions $\pi_1$ and $\pi_2$, and let $m$ interactions be reported by both. If each true interaction is detected by the two screens independently, the number of true interactions is estimated by
$$
\hat N = \frac{(\pi_1 n_1)(\pi_2 n_2)}{m}, \tag{10.2}
$$
the Lincoln–Petersen estimator applied to the true positives of the two screens (false positives of independent screens almost never coincide, so $m$ consists of true interactions).

Equivalently, the sensitivity of screen 2 is estimated as $m/(\pi_1 n_1)$, the fraction of screen 1's true interactions that it recovers, and $\hat N$ is its true positives divided by this sensitivity.

**Example 10.5.2** Two screens report $11\,250$ and $8570$ interactions, with precisions $0.8$ and $0.7$, and share $900$. They contain $9000$ and $6000$ true interactions, and $\hat N = 9000 \times 6000/900 = 60\,000$. Ignoring the false positives would give $11\,250 \times 8570/900 = 107\,000$, an overestimate by $78\%$. In the simulation of the figure, with a true size of $60\,000$, the corrected estimate has a median of $60\,000$ and a $90\%$ range of $57\,300$ to $62\,800$.

![Estimating the size of an interactome from the overlap of two screens (simulation; true size 60 000 interactions, sensitivities 0.15 and 0.10, precisions 0.8 and 0.7). A: the naive estimate n₁n₂/m (orange) and the precision-corrected estimate of Eq. (10.2) (blue) over 400 repetitions; dashed: the true size. B: when interactions differ in how easily any assay detects them (a shared log-normal detectability with SD σ), the screens overlap more than under independence and the estimate falls below the truth](./plots/interactome_size.py)

The independence assumption is the weak point. Some interactions are easy to detect by any assay (stable, abundant, well-folded proteins) and others hard, so screens tend to find the same easy interactions, $m$ is larger than under independence, and $\hat N$ is too small: in the simulation, a shared variation of detectability with $\sigma = 0.6$ on the log scale lowers the median estimate to $41\,800$, and $\sigma = 0.9$ to $29\,000$. Capture–recapture estimates of interactome size are therefore lower bounds, the more so the more similar the two assays are; using screens by different methods reduces but does not remove the problem. The same logic and the same caveat apply to estimating the number of species from overlapping samples in ecology.

### 10.5.4. Sampling and Bias

An interactome map is a sample of the true network, and samples can distort topology. Literature-curated networks are biased towards well-studied proteins: the number of interactions reported for a protein correlates with the number of papers about it, so that "hubs" in curated networks are partly hubs of attention. In systematic screens, only a subset of proteins is tested as bait, and spoke expansion (10.3.2) makes the tested baits hubs. Sampling a subnetwork of a network with a given degree distribution does not in general preserve it: subnets of scale-free networks are not scale-free (Stumpf, Wiuf and May, 2005), and incomplete sampling can make a network with a narrow degree distribution look heavy-tailed or vice versa (Han and colleagues, 2005). Statistical comparisons should therefore use null models that preserve the sampling design, such as **degree-preserving randomization** of the observed network ([1.4.7](/1.4.7#sec-7.4.6)), and claims about the topology of the true interactome, including whether it is a **scale-free network**, deserve skepticism.

### 10.5.5. Case Study: a Host–Pathogen Interaction Map

Viruses depend on host proteins for every step of their life cycle, and the host proteins they bind are candidate drug targets that do not mutate as fast as the virus. In early 2020, $26$ of the $29$ proteins of SARS-CoV-2 were expressed with affinity tags in human HEK293T cells, purified, and their human partners identified by AP-MS; scoring with SAINTexpress and MiST yielded $332$ high-confidence virus–human interactions (Gordon and colleagues, 2020). The human partners were enriched in vesicle trafficking, lipid modification, translation and the regulation of innate immune signaling. Of the human proteins, $66$ were targets of $69$ known compounds (approved drugs, clinical candidates and preclinical molecules); testing them in antiviral assays identified two classes with activity, inhibitors of mRNA translation and ligands of the sigma-1 and sigma-2 receptors. The study illustrates both the speed of the method and its limits: interactions measured in a kidney-derived cell line with overexpressed viral proteins are hypotheses about infected lung cells, and most of the candidate drugs did not reach clinical benefit. Drug–target networks of this kind are analyzed further in [7.9.12](/7.9.12).

## 10.6. Genetic Interactions

### 10.6.1. Definition and Measurement

A genetic interaction between two genes is a deviation of the double-mutant phenotype from the combination of the single-mutant phenotypes. For a quantitative phenotype such as growth rate (fitness, $W$, relative to the wild type), independence is usually defined multiplicatively, and the interaction score $\varepsilon_{ab} = W_{ab} - W_aW_b$ is defined in [7.4.4](/7.4.4#fml-4.3.1): negative scores (aggravating interactions, with **synthetic lethality** as the extreme) and positive scores (alleviating interactions). Negative interactions typically connect genes in parallel, compensating pathways; positive interactions connect genes in the same complex or linear pathway, whose second loss costs nothing once the first has disabled the function.

Measuring $\varepsilon$ for all pairs requires making and phenotyping millions of double mutants. In budding yeast this was achieved by synthetic genetic array (SGA) analysis (Tong and colleagues, 2001): a query strain carrying one deletion is mated robotically with an ordered array of about $5000$ viable deletion strains (and arrays of temperature-sensitive alleles of essential genes), the diploids are sporulated, double-mutant haploids are selected on a series of media, and colony sizes, photographed and measured automatically, give fitness. The epistatic miniarray profile (E-MAP; Schuldiner and colleagues, 2005) applies the same principle to selected sets of a few hundred genes, such as those of the early secretory pathway, with higher precision.

Colony size depends on more than the two mutations: on plate position (colonies at the edge grow larger), on neighbors, on batch and on the linkage between nearby loci, which reduces recombinants. Scoring therefore normalizes for these effects before computing $\varepsilon$, and estimates the single-mutant fitness from the same screens (Baryshnikova and colleagues, 2010).

### 10.6.2. The Global Network

The global yeast genetic-interaction network tested about $23$ million double mutants, almost all pairs of yeast genes, and identified about $550\,000$ negative and $350\,000$ positive interactions (Costanzo and colleagues, 2016). Negative interactions are about ten times more frequent than synthetic lethality alone, and essential genes have many more interactions than nonessential ones. Genes whose products are in the same complex are often joined by positive interactions; genes in compensating pathways by negative ones; and genes with **pleiotropy** (affecting many processes) by many interactions of both signs.

The most powerful use of the network is not the individual edges but the profiles.

**Definition 10.6.1 (Genetic-Interaction Profile)** The **genetic-interaction profile** of a gene is the vector of its interaction scores $\varepsilon$ with all genes of a reference set (the array); the similarity of two profiles, measured by their Pearson **correlation coefficient**, is the profile similarity of the two genes.

Two genes with similar profiles share interaction partners: they buffer, and are buffered by, the same processes, which happens when they act in the same pathway or complex, even if they do not interact with each other. Profile similarity is therefore a measure of functional relatedness that does not require any physical interaction or prior annotation. Clustering genes by profile similarity organizes the genome hierarchically: at high similarity into complexes and pathways (for example the subunits of the Elongator complex or of a sterol-biosynthesis branch), at lower similarity into bioprocesses (DNA replication, Golgi transport, mitochondrial translation), and at the lowest into compartments of the cell (Costanzo and colleagues, 2016). Genes of unknown function placed in such a cluster acquire a functional prediction.

**Example 10.6.1** In the simulation of the figure, $72$ query genes belong to six modules whose members share $70\%$ of a module-specific set of interactions with $300$ array genes. Pairs of genes within a module have a mean profile correlation of $0.35$, pairs from different modules $0.00$; average-linkage **hierarchical clustering** with distance $1 - r$, cut into six clusters, recovers the six modules exactly (purity $1.00$), although the interaction matrix itself, with queries in random order, shows no visible structure.

![Genetic-interaction profiles group genes into modules (simulation). A: interaction scores ε of 72 query genes (six modules of 12, random order) with the first 120 of 300 array genes; red: negative, green: positive. B: the Pearson correlations between query profiles, ordered by average-linkage hierarchical clustering on 1 − r; coloured bar: true module](./plots/gi_profiles.py)

:::

Genetic and physical networks are complementary: genes linked by positive interactions and similar profiles often encode physically interacting proteins, whereas negative interactions mostly join proteins that do not touch. Comparing the two maps identifies "between-pathway" models, in which many negative interactions join two physically defined complexes that back each other up. Interactions also depend on the environment: differential genetic-interaction maps measured under DNA damage or drugs reveal rewiring of the network in response to the condition. Because each double mutant is measured once in a large screen, profile-based inferences are robust to noise in individual scores, much as the regulon-based inference of [7.9.3](/7.9.3#sec-3.4) is robust to noise in individual genes.

## 10.7. CRISPR Screens

### 10.7.1. Pooled Screens

**Definition 10.7.1 (CRISPR Screen)** A **CRISPR screen** is a **genetic screen** in which a population of cells is perturbed with a library of guide RNAs targeting many genes, usually several guides per gene, using **CRISPR–Cas9** knockout, **CRISPR interference** (repression) or **CRISPR activation**; in a **pooled screen** the guides are delivered together by lentiviral transduction at a low multiplicity of infection, the cells are subjected to a selection (proliferation, drug treatment, sorting by a reporter), and the abundance of each guide before and after selection is counted by sequencing the integrated guide sequences.

The design and the sampling of cells per guide are in [7.4.19](/7.4.19#sec-19.5.5); here we treat the analysis. The raw data are counts of each guide in each sample: a negative-selection screen (for genes needed for proliferation or survival) looks for guides depleted over time; a positive-selection screen (resistance to a drug or a toxin) for enriched guides. Genome-wide libraries such as Brunello contain about four guides for each of the $19\,000$ protein-coding genes plus non-targeting controls.

### 10.7.2. From Guide Counts to Gene Scores

**Formula 10.7.1 (Guide-Level Test)** Let $c_{g0}$ and $c_{g1}$ be the counts of guide $g$ in the reference and selected samples, with size factors $s_0, s_1$ (for example the median ratio of counts, as for RNA-seq; [7.9.2](/7.9.2)). The guide's log fold change is $\log_2\big((c_{g1} + 0.5)/s_1\big) - \log_2\big((c_{g0} + 0.5)/s_0\big)$. Under the null hypothesis that the guide has no effect, $c_{g1}$ follows a **negative binomial distribution** with mean $\mu_g = s_1 c_{g0}/s_0$ and variance $\mu_g + \phi\,\mu_g^2$, where the dispersion $\phi$ is estimated from replicates by a mean–variance fit; the one-sided p-value for depletion is the lower tail $\mathbb{P}(C \le c_{g1})$.

Guide-level evidence must be combined per gene. Guides differ in efficiency: some cut poorly or produce in-frame indels that leave a functional protein, some cut at off-target sites, and some cut amplified genomic regions, where multiple double-strand breaks are toxic regardless of the gene (the copy-number effect). A gene should be called a hit when several of its guides are consistently ranked high, not when one guide is extreme.

**Formula 10.7.2 (Robust Rank Aggregation)** Rank all $N$ guides by their p-values and let $r_1 \le \cdots \le r_n$ be the normalized ranks ($\operatorname{rank}/N$) of the $n$ guides of a gene. Under the null hypothesis that the gene's guides are randomly placed in the ranking, the $j$-th smallest of $n$ uniform ranks has the distribution $\mathrm{Beta}(j, n - j + 1)$. The robust rank aggregation score is
$$
\rho = \min_{j \le n'} \; \mathbb{P}\big(U_{(j)} \le r_j\big) = \min_{j \le n'} \; \sum_{l = j}^{n}\binom{n}{l} r_j^{\,l}(1 - r_j)^{n-l}, \tag{10.3}
$$
where in the $\alpha$-RRA variant of MAGeCK (Li and colleagues, 2014) only the $n'$ guides with $r_j \le \alpha$ (for example $\alpha = 0.05$) are considered. The p-value of $\rho$ is obtained by a **permutation test** that assigns random guides to genes, and the **false discovery rate** across genes is controlled by the Benjamini–Hochberg procedure.

The minimum over $j$ asks: is there some number of guides that are all ranked surprisingly high? It does not require all guides to be effective, which makes it robust to inactive guides.

**Example 10.7.1** A gene's four guides have normalized ranks $0.001$, $0.004$, $0.03$ and $0.6$. With $\alpha = 0.05$ the first three are used: $\mathbb{P}(U_{(1)} \le 0.001) = 1 - 0.999^4 = 0.0040$, $\mathbb{P}(U_{(2)} \le 0.004) = 9.5\times10^{-5}$ and $\mathbb{P}(U_{(3)} \le 0.03) = 1.1\times10^{-4}$, so $\rho = 9.5\times10^{-5}$, driven by two guides near the top. The fourth guide, perhaps inactive, does not dilute the evidence, as it would in a mean of fold changes.

**Example 10.7.2** In the simulated screen of the figure ($2000$ genes, $4$ guides each, $100$ essential genes, $15\%$ inactive guides, and $84$ guides of nonessential genes that deplete through toxic off-target cutting), $\alpha$-RRA with permutation p-values calls $66$ genes at an FDR of $0.05$: $64$ essential genes and $2$ others. One of the two false hits has two off-target guides, the other a single strongly depleted one: for a single extreme guide, $\rho = 1 - (1 - r_1)^4 \approx 4r_1$, so robust rank aggregation, like the mean, can be driven by one guide. Ranking genes by the median guide fold change, which needs at least two concordant guides, gives the best precision–recall curve in this simulation (average precision $0.96$, against $0.93$ for the mean and $0.91$ for RRA). The top RRA p-values reach the floor $1/20\,001$ of the $20\,000$ permutations. In practice, analyses require hits to be supported by at least two guides and remove guides with predicted off-target sites or in amplified regions.

![A pooled CRISPR knockout screen for essential genes (simulation; 2000 genes × 4 guides, 100 essential genes, 15% inactive guides, 1% toxic off-target guides among nonessential genes; negative binomial counts). A: guide log2 fold changes. B: gene-level −log10 p of α-robust rank aggregation against the median guide fold change; red: essential genes; dashed: FDR 0.05. C: precision–recall curves for ranking genes by the RRA score and by the mean and median guide fold changes](./plots/crispr_screen.py)

:::

Other methods model the problem differently. BAGEL (Hart and Moffat, 2016) computes a Bayes factor of each gene's fold changes against the distributions of reference essential and nonessential genes. MAGeCK-MLE fits a negative binomial generalized linear model with guide efficiencies to several conditions jointly. CERES and its successor Chronos, used in the Cancer Dependency Map (DepMap) of more than a thousand cancer cell lines, model the time course of guide depletion with a gene effect, a guide efficiency and a copy-number term, which removes the copy-number artifact and makes gene effects comparable across lines ([7.9.13](/7.9.13)). The same analysis applied to many cell lines yields co-essentiality: genes whose dependency profiles across lines are correlated tend to be in the same complex or pathway, a human analogue of genetic-interaction profiles (Definition 10.6.1).

### 10.7.3. Combinatorial Screens and Enhancer Epistasis

Libraries in which each vector carries two guides measure genetic interactions directly in human cells: the fitness effect of the pair is compared with the product of the single effects, exactly as in yeast (Horlbeck and colleagues, 2018, with CRISPRi in leukemia cells). Combinatorial screens are limited by the square of the library size, and are therefore designed around candidate sets, such as paralog pairs, which are often synthetically lethal, or drug targets.

The same logic applies to noncoding elements. The *MYC* oncogene is regulated by several distal **enhancers** spread over megabases. Targeting single enhancers and pairs of enhancers by CRISPRi in a pooled proliferation screen, and measuring the epistasis between enhancer pairs, showed that the enhancers form a hierarchical network in which some pairs act synergistically and others additively (Lin and colleagues, 2022); a regularized regression on chromatin features predicted the synergistic pairs from their physical contacts in three-dimensional chromatin and their co-occupancy by the coactivator BRD4 ([7.9.8](/7.9.8)). Robustness of gene expression to the loss of single enhancers, and the redundancy that it implies, is thus a genetic-interaction phenomenon at the level of regulatory DNA.

Pooled screens can also read richer phenotypes. Sorting cells by a fluorescent reporter screens for regulators of one gene; optical pooled screens image cells and read their guides by in situ sequencing; and Perturb-seq reads both the guide and the whole transcriptome of each cell by single-cell RNA sequencing ([7.9.5](/7.9.5)), turning a screen into a map of the transcriptional consequences of each perturbation, the data from which regulatory networks are inferred in [7.9.11](/7.9.11).

## Summary

| Network | Edge means | Main methods | Main errors | Section |
|---|---|---|---|---|
| Binary physical | direct contact | yeast two-hybrid, complementation, FRET/BRET | low sensitivity per screen; autoactivators, non-physiological pairs | 10.2 |
| Co-complex | same complex | AP-MS (Definition 10.3.1), co-fractionation, crosslinking | background binders; spoke/matrix conventions | 10.3 |
| Proximity | same neighborhood | BioID, TurboID, APEX (Definition 10.3.2), PLA | compartment background | 10.3 |
| Functional association | same pathway | genomic context, phylogenetic profiles (Definition 10.4.1), co-expression, text; STRING | correlated channels; not physical | 10.4–10.5 |
| Genetic | phenotype of double ≠ combination of singles | SGA, E-MAP, combinatorial CRISPR | colony-size artifacts; condition dependence | 10.6 |
| Gene–phenotype | perturbation changes fitness or reporter | pooled CRISPR screens (Definition 10.7.1) | inactive and off-target guides, copy number | 10.7 |

- The interactome (Definition 10.1.1) is a union of different graphs; the meaning of an edge depends on the method, and maps record possible rather than realized interactions (10.1).
- AP-MS is scored against controls (SAINT, CompPASS; Example 10.3.1), and co-complex data become edges by the spoke or matrix model, with consequences for topology (10.3.2).
- Independent evidence is combined with the prior removed, Eq. (10.1) (Example 10.5.1: four moderate channels give $0.93$); quality is measured with positive and random reference sets; capture–recapture, Eq. (10.2), estimates interactome size (Example 10.5.2) but is a lower bound when detectability is shared; sampling and study bias distort topology (10.5).
- Genetic interactions are deviations from multiplicative fitness ([7.4.4](/7.4.4#fml-4.3.1)); the yeast network of about $900\,000$ interactions organizes genes hierarchically through profile similarity (Definition 10.6.1, Example 10.6.1).
- Pooled CRISPR screens are analyzed by negative binomial guide tests (Formula 10.7.1) and rank aggregation (Formula 10.7.2, Example 10.7.1); robustness to single guides requires concordance of several guides (Example 10.7.2); combinatorial and enhancer screens extend genetic interactions to human cells and regulatory DNA (10.7.3).

## Questions

1. A yeast two-hybrid screen and an AP-MS study of the same human complex of $8$ subunits report $7$ and $28$ interactions respectively. Explain how both can be correct.

   **Answer** They measure different graphs. Y2H detects direct binary contacts; a complex of $8$ subunits held together by a chain or tree of contacts has at least $7$ of them. AP-MS reports co-membership: with several subunits used as baits and matrix expansion, every pair of the $8$ is linked, $\binom{8}{2} = 28$ edges, of which only the direct contacts (perhaps $7$–$12$) are physical. Neither is wrong; the network built from them must state which kind of edge it contains, and combining them naively would overcount contacts.

2. Why are autoactivating baits a problem in yeast two-hybrid screens, and how are they handled? What is the analogous problem in AP-MS?

   **Answer** An autoactivating bait (for example a transcription factor with its own activation domain) activates the reporter without any prey, so every prey would appear to interact. Such baits are detected by testing the bait alone against an empty prey vector and are removed or truncated to remove the activation domain before screening. In AP-MS the analogous problem is background binding: proteins that bind the tag, the beads or the antibody, or are abundant in every lysate, appear in every purification; they are handled by negative controls and specificity-based scores (SAINT, CompPASS, CRAPome frequencies).

3. Two independent Y2H screens of the same search space report $3000$ and $2400$ interactions with precisions $0.9$ and $0.85$, and share $270$ interactions. Estimate the number of interactions in the search space and the sensitivity of each screen. Is the estimate likely to be too high or too low?

   **Answer** True positives: $2700$ and $2040$. $\hat N = 2700 \times 2040/270 = 20\,400$ (Eq. (10.2)). Sensitivities: $2700/20\,400 = 0.13$ and $2040/20\,400 = 0.10$. Both screens use the same assay, so interactions that suit Y2H (soluble, nuclear-compatible, well-folded proteins) are found by both, making the overlap larger than under independence; the estimate is probably too low, a lower bound (Example 10.5.2, figure panel B).

4. Compute the STRING-style combined score for a pair with channel scores $0.5$ (co-expression) and $0.5$ (text mining), and explain why combining them may still overstate the evidence.

   **Answer** With $p = 0.041$: $s' = (0.5 - 0.041)/0.959 = 0.4786$ for both; $S' = 1 - 0.5214^2 = 0.7281$; $S = 0.7281 + 0.041 \times 0.2719 = 0.739$. The formula assumes independent channels, but text mining often reports co-expression results, and genes co-mentioned in papers are often studied together because they are co-expressed; correlated evidence is counted twice, so the combined score is optimistic.

5. A bait purification yields prey $Y$ with spectral counts $8$, $11$ and $9$ in three replicates; in $20$ control purifications prey $Y$ has counts with mean $6$ and variance $20$. Is $Y$ a specific interactor? Explain what information is missing.

   **Answer** The mean with the bait, $9.3$, is only $1.6$ times the control mean, and the controls are overdispersed (variance $20$ against mean $6$, so a negative binomial with large spread). Under a negative binomial with mean $6$ and variance $20$ ($r = 36/14 = 2.57$), counts of $9$–$11$ are common (probability of $\geq 9$ in one run about $0.24$), so the evidence of specificity is weak. Missing information: normalization of counts to the total amount of material in each run, the abundance of the bait itself, whether the prey is enriched in a quantitative (SILAC or label-free intensity) comparison with matched controls, and validation by reciprocal purification (using $Y$ as bait) or an orthogonal assay.

6. Explain why two genes in the same protein complex typically have a positive genetic interaction and highly similar genetic-interaction profiles, although they may show no physical interaction in a two-hybrid assay.

   **Answer** If the complex needs both subunits, losing either inactivates it; losing the second after the first adds no further defect, so $W_{ab} \approx W_a \approx W_b$, which exceeds the multiplicative expectation $W_aW_b$: $\varepsilon > 0$ ([7.4.4](/7.4.4#fml-4.3.1)). Both deletions remove the same function, so both mutants interact with the same genes elsewhere (those that buffer the complex's function): their profiles are similar. Two-hybrid detects only direct contacts, and the two subunits may be on opposite sides of the complex, may need other subunits to bind, or may misfold in yeast as fusions.

7. In a genome-wide CRISPR knockout screen in a cancer cell line, guides targeting genes in a highly amplified region on chromosome 8 are all depleted, including guides against genes not expressed in the line. Explain the artifact and how analyses correct for it.

   **Answer** Each guide targeting an amplified region cuts many copies of the region, creating many double-strand breaks, which activate DNA-damage responses and reduce proliferation regardless of the gene targeted. The depletion therefore reflects copy number, not gene function; the telltale sign is depletion of unexpressed genes and of intergenic guides in the same region. Corrections: model guide depletion with a copy-number term (CERES, Chronos), use CRISPRi (which does not cut) or compare with guides targeting intergenic sites in the region, and require expression of the gene for an essentiality call.

8. A gene has four guides with normalized ranks $0.02$, $0.03$, $0.04$ and $0.05$; another has ranks $0.0002$, $0.5$, $0.6$ and $0.9$. Compute the $\alpha$-RRA scores with $\alpha = 0.05$ and discuss which gene you would trust more as a hit.

   **Answer** Gene 1: $\mathbb{P}(U_{(1)} \le 0.02) = 1 - 0.98^4 = 0.0776$; $\mathbb{P}(U_{(2)} \le 0.03) = 1 - 0.97^4 - 4 \times 0.03 \times 0.97^3 = 0.0052$; $\mathbb{P}(U_{(3)} \le 0.04) = 4 \times 0.04^3 \times 0.96 + 0.04^4 = 2.5\times10^{-4}$; $\mathbb{P}(U_{(4)} \le 0.05) = 0.05^4 = 6.3\times10^{-6}$; $\rho_1 = 6.3\times10^{-6}$. Gene 2: only the first guide has $r \le 0.05$: $\rho_2 = 1 - 0.9998^4 = 8.0\times10^{-4}$. Gene 1 scores better and is more trustworthy: four concordant guides, each moderately depleted, are unlikely by chance and unlikely to share an artifact; gene 2 rests on one guide, which could be an off-target or copy-number effect (Example 10.7.2). Validation with independent guides or another modality (CRISPRi, rescue with a cDNA) is needed for gene 2.

9. Design a screen to find genes whose loss is synthetically lethal with loss of *BRCA1* in human cells, and explain how to distinguish synthetic lethality from general essentiality.

   **Answer** Use isogenic cell lines, *BRCA1*-deficient and *BRCA1*-proficient (for example a knockout and its parental line, or a deficient line with *BRCA1* re-expressed), and perform the same genome-wide pooled knockout screen in both at high coverage (several hundred cells per guide), with replicates, sampling guides at the start and after about $14$–$21$ days. For each gene estimate the depletion in both lines (Formula 10.7.1, gene scores by RRA or a GLM) and test the difference, the interaction between gene and genotype. Genes depleted in both lines are generally essential; synthetic-lethal candidates are depleted significantly more in the deficient line. The known positive control is *PARP1*, whose inhibition is synthetically lethal with BRCA deficiency ([7.9.13](/7.9.13)). Candidates are validated with independent guides, inhibitors and rescue experiments.

10. Why might a co-fractionation experiment report two unrelated enzymes of similar size as a complex, and which additional evidence would you require?

    **Answer** Size-exclusion separates by hydrodynamic size: two unrelated proteins (or complexes) of similar size elute in the same fractions and have correlated profiles without binding. Ion-exchange fractionation separates by charge and gives an orthogonal profile, so co-elution in several orthogonal separations is stronger evidence; conservation of co-elution across species, crosslinking mass spectrometry, reciprocal AP-MS, prior knowledge (known complexes as a training set for a classifier) and a predicted interface (structure prediction) would all be required to call a complex.

11. A study reports that a curated protein interaction network is scale-free and that its hubs are more often essential genes. Give two reasons to doubt the first claim and one test of the second that controls for study bias.

    **Answer** First claim: curated networks are samples biased towards well-studied proteins, whose many reported interactions reflect research attention; and subsampling a network distorts its degree distribution (Stumpf, Wiuf and May, 2005), so the observed distribution may not reflect the true one; the power-law fit itself should be tested rigorously ([1.4.7](/1.4.7)). Second claim: well-studied genes are also more often known to be essential, so attention could create the correlation. Test it in a systematic, unbiased map (for example a proteome-scale Y2H in which every protein was tested as bait and prey), or include the number of publications as a covariate in a logistic regression of essentiality on degree, or compare with degree-preserving randomized networks ([1.4.7](/1.4.7#sec-7.4.6)).

12. (Open question) How would you combine physical interactions, genetic-interaction profiles and CRISPR co-essentiality to assign a function to an uncharacterized human gene?

    **Answer** A possible strategy: (i) collect its physical partners from AP-MS (BioPlex), proximity labeling and HuRI, and its predicted complex structures; (ii) compute its co-essentiality profile across DepMap cell lines and find the genes with the most correlated dependency profiles, which, like yeast genetic-interaction profiles, point to shared pathways; (iii) check whether the physical partners and co-essential genes are enriched in a common pathway or complex (over-representation with the correct background, [7.9.3](/7.9.3)); (iv) look for agreement: a gene that binds members of a complex and shares their dependency profile is likely a new subunit or regulator; (v) test the prediction experimentally, for example by knocking out the gene and measuring the stability or activity of the complex, by Perturb-seq comparison of its transcriptional knockout signature with those of known members, and by localization. Agreement between independent kinds of evidence is the key, since each kind alone has known artifacts.
