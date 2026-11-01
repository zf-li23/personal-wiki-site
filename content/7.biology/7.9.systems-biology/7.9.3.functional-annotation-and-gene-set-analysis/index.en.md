---
title: Functional Annotation and Gene-Set Analysis
description: "From gene lists to biological interpretation: the Gene Ontology as a directed acyclic graph with the true-path rule and evidence codes, pathway databases and MSigDB; over-representation analysis with the hypergeometric test, the choice of background, set size, dependence between terms and length bias; gene set enrichment analysis with the running-sum enrichment score, normalized scores, permutation nulls, the leading edge and competitive against self-contained hypotheses; regulator activity from target sets; and the pitfalls of interpretation, illustrated with the airway data."
---

A differential-expression analysis ends with a list of hundreds or thousands of genes ([7.9.2](/7.9.2)). Reading the list gene by gene is slow and selective: one recognizes the genes one already knows. Gene-set analysis asks instead whether genes that share a function, a pathway, a location in the cell or a regulator are changed more than expected by chance, and so turns a gene list into statements about processes. This chapter describes the annotation resources that define the sets (3.1), the two families of tests, over-representation analysis of a list (3.2) and enrichment analysis of a ranking (3.3), the step from gene sets to the regulators that control them (3.4), and the pitfalls of interpretation (3.5), with tools and code in 3.6. The running example is again the airway experiment: which processes do glucocorticoids switch on and off in airway smooth muscle?

The statistics are those of [3.2](/3.2) and [7.7](/7.7): the **hypergeometric distribution** and the **contingency table** for over-representation, permutation tests for enrichment scores, and the **false discovery rate** for the many sets tested ([7.7.20](/7.7.20)). Ontologies are graphs, and a **directed acyclic graph** in particular ([1.4](/1.4)); gene identifiers and sequence databases are in [7.8.2](/7.8.2). Gene sets defined by transcription factors lead to the regulatory networks of [7.9.11](/7.9.11), and sets defined by interactions to the network methods of [7.9.12](/7.9.12).

## 3.1. Annotation Resources

### 3.1.1. The Gene Ontology

An ontology is a controlled vocabulary whose terms are linked by defined relations, so that both people and programs can reason with it.

**Definition 3.1.1 (Gene Ontology)** The **Gene Ontology** (GO) is a controlled vocabulary of terms describing the functions of gene products, in three disjoint aspects, molecular function (the activity of a gene product, such as "protein kinase activity"), biological process (a larger objective accomplished by several activities, such as "response to glucocorticoid") and cellular component (a location or complex, such as "mitochondrial inner membrane"), whose terms are the vertices of a directed acyclic graph with edges for the relations *is_a* (subtype), *part_of* and *regulates*. An annotation links a gene product to a term, with a reference and an evidence code.

In the 2026 release the ontology has about $38\,000$ terms in use: $24\,000$ biological processes, $10\,000$ molecular functions and $4000$ cellular components. A term may have several parents, so the structure is a directed acyclic graph rather than a tree: "cellular response to chemical stimulus" is both a "response to chemical" and a "cellular response to stimulus". The graph is acyclic because no term can be its own ancestor.

The relations make annotations propagate. By the true-path rule, a gene product annotated to a term is implicitly annotated to all its ancestors along *is_a* and *part_of*: a gene involved in the "cellular response to glucocorticoid stimulus" is involved in the "response to glucocorticoid", the "response to steroid hormone", the "response to hormone" and so on up to the root. Annotations are usually stored at the most specific term and propagated when gene sets are built. The consequence for statistics is that the sets of different terms are nested and overlap heavily (3.2.4).

Evidence codes record how an annotation was obtained: from experiments (EXP, IDA direct assay, IMP mutant phenotype, IGI genetic interaction, IPI physical interaction, IEP expression pattern, and their high-throughput variants HDA, HMP and others), from phylogenetic inference (IBA), from sequence similarity (ISS), from author or curator statements (TAS, NAS, IC), or by automatic electronic assignment without curation (IEA). In the human annotation file of 2026, $19\%$ of the $860\,000$ UniProtKB annotations are electronic and $34\%$ come from physical interactions, mostly to the uninformative term "protein binding". Annotation is uneven: well-studied genes carry dozens of annotations and many genes have few or none.

![A part of the Gene Ontology (biological process), from "cellular response to glucocorticoid stimulus" to the root, with is_a edges from child to parent; some parents of the lower terms are omitted. Each term shows the number n of tested airway genes annotated to it after propagation by the true-path rule, and how many (k) are among the 402 genes induced by dexamethasone; colour: one-sided hypergeometric p-value. A gene counted at a term is counted again at every ancestor](./plots/go_dag.py)

### 3.1.2. Pathways and Curated Sets

GO describes functions term by term; pathway databases describe how gene products work together. KEGG draws manually curated maps of metabolism, signaling and disease, with genes mapped to orthology groups across organisms; Reactome organizes human biology into a hierarchy of reactions with explicit participants, complexes and modifications; WikiPathways is community curated. These are usually used as gene sets, ignoring the arrows in the diagrams (3.4).

The Molecular Signatures Database (MSigDB) collects gene sets from these and other sources in collections: positional sets (C1), curated pathways (C2), regulatory target sets of transcription factors and microRNAs (C3), computational modules (C4), GO (C5), oncogenic (C6) and immunologic (C7) signatures, cell-type signatures (C8) and the Hallmark collection (H). The $50$ Hallmark sets (Liberzon and colleagues, 2015) were derived by merging overlapping sets and refining them on expression data into coherent, minimally redundant programs, such as "TNF-alpha signaling via NF-kB", "E2F targets" or "oxidative phosphorylation"; their small number and low overlap make them a good first summary.

### 3.1.3. Identifiers

Before any set can be tested, the genes of the data and of the sets must be matched. Expression data are indexed by Ensembl gene identifiers (ENSG…), annotation by UniProt accessions, Entrez Gene numbers or HGNC symbols, and symbols change: genes are renamed, and old symbols remain in old data sets. Mapping with a versioned table (Ensembl BioMart, HGNC, the annotation packages of Bioconductor) and reporting the number of identifiers that could not be mapped is part of the analysis ([7.8.2](/7.8.2)). Spreadsheet programs that convert symbols such as *SEPT2* or *MARCH1* into dates corrupted thousands of published gene lists, one reason why HGNC renamed these genes in 2020.

## 3.2. Over-Representation Analysis

### 3.2.1. The Test

**Definition 3.2.1** **Over-representation analysis** (ORA) of a gene list tests, for each gene set $S$, whether the list contains more genes of $S$ than expected if the list were a random subset of a background set of genes. With $N$ genes in the background, $K$ of them in the list, $n$ in the set and $k$ in both, the one-sided p-value is the upper tail of the hypergeometric distribution,
$$
p = \mathbb{P}(X \geq k) = \sum_{x = k}^{\min(n, K)} \frac{\binom{n}{x}\binom{N - n}{K - x}}{\binom{N}{K}}, \tag{3.1}
$$
which is the one-sided Fisher exact test of the $2 \times 2$ table of genes classified by "in the list" and "in the set". The enrichment ratio is $k/(Kn/N)$, the observed overlap divided by the expected one.

**Example 3.2.1** A myeloma data set has $1272$ differentially expressed genes among $12\,639$ measured. The GO group for inflammation has $96$ genes, $8$ of them in the list. The expected overlap is $1272 \cdot 96/12\,639 = 9.7$, so the list contains fewer inflammation genes than expected: the enrichment ratio is $0.83$ and the one-sided p-value for enrichment is $\mathbb{P}(X \ge 8) = 0.76$. The p-value for depletion, $\mathbb{P}(X \le 8) = 0.36$, is not significant either. If all four numbers of the table were ten times larger ($80$ of $960$ set genes among $12\,720$ selected of $126\,390$), the ratio would be the same but the depletion would reach $p = 0.039$: significance grows with the size of the counts at a fixed effect, a point that matters for large gene sets (3.2.3).

**Example 3.2.2** In the airway data take as background the $11\,707$ tested genes that have at least one biological-process annotation, and as list the $402$ of them induced by dexamethasone (adjusted $p < 0.05$, more than twofold). Testing the $3013$ biological-process terms with $10$ to $500$ genes in the background, $27$ are significant at an FDR of $0.05$. The strongest are "negative regulation of cell motility" ($22$ of $218$ genes, $7.5$ expected, $p = 5.9\times10^{-6}$), "extracellular matrix organization" ($17$ of $167$), "retinol metabolic process" ($8$ of $37$) and "cellular response to hormone stimulus" ($29$ of $385$). Along the path in the figure, "response to glucocorticoid" contains $10$ of the induced genes against $2.6$ expected ($p = 2.6\times10^{-4}$, FDR $0.034$), and its child "cellular response to glucocorticoid stimulus" $7$ against $1.1$ ($p = 1.1\times10^{-4}$). The $384$ repressed genes give $164$ significant terms, led by neuron projection morphogenesis and axon guidance, developmental programs whose genes are expressed in many non-neural cells.

The second example also shows a limit of annotation. *FKBP5*, *TSC22D3*, *PER1* and *ZBTB16*, among the best-known glucocorticoid-induced genes and all in the induced list, are not annotated to "response to glucocorticoid" or to any of its ancestors up to "response to steroid hormone"; the term owes its significance to genes such as *DUSP1*, *KLF9*, *FOXO3*, *ERRFI1* and *CFLAR*. Absence of an annotation is not evidence of absence of the function.

### 3.2.2. The Background

The background must be the set of genes that could have appeared in the list. Every gene that was not measured, not expressed or filtered out before testing has no chance of being in the list, and including such genes in the background inflates the significance of any set enriched in expressed genes.

![Two pitfalls of over-representation analysis (simulation). A: 5000 random lists of 500 genes drawn from the 8000 genes expressed in a tissue, tested for a 'neural' set of 400 genes (300 expressed): against all 20000 genes as background the set appears enriched in most lists; against the expressed genes the p-values are uniform, as they should be. B: at a fixed enrichment ratio of 1.5, the p-value falls steadily with the size of the set](./plots/ora_background.py)

In the simulation of the figure, a list drawn at random from the $8000$ genes expressed in a tissue contains on average $500 \cdot 300/8000 = 18.75$ genes of a set with $300$ expressed members, while the whole-genome background predicts $500 \cdot 400/20\,000 = 10$. Tested against all genes, $79\%$ of the random lists give $p < 0.05$; tested against the expressed genes, $4.2\%$ (the test is discrete, hence slightly below $5\%$). Real analyses show the effect in milder form: with all $17\,474$ protein-coding genes with a biological-process annotation as background instead of the $11\,707$ tested ones, the airway ORA finds $35$ significant terms instead of $27$, and the leading p-values are about five times smaller. Web tools that default to the whole genome make this error easy.

### 3.2.3. Set Size and Generality

At a fixed enrichment ratio the hypergeometric p-value decreases with the size of the set (figure, panel B): with $10\%$ of $12\,000$ genes selected and a ratio of $1.5$, a set of $100$ genes gives $p = 0.07$, one of $500$ genes $p = 2\times10^{-4}$ and one of $2000$ genes $p = 5\times10^{-15}$. Broad terms ("cell cycle", "transcription", "response to stimulus") therefore dominate lists sorted by p-value, although they carry little information. Reporting the enrichment ratio with its p-value, restricting the range of set sizes (for example $10$ to $500$ genes), and preferring compact collections such as the Hallmark sets all help.

### 3.2.4. Dependence Between Terms

Because of the true-path rule, a strong signal at one specific term makes all its ancestors significant as well, and lists of enriched terms are full of near-duplicates (in the figure of 3.1.1 most terms on the path to the root are significant). The tests are positively dependent; the Benjamini–Hochberg procedure remains valid under this kind of dependence, but the list is redundant. Methods that exploit the graph reduce the redundancy: the elim and weight algorithms of topGO (Alexa, Rahnenführer and Lengauer, 2006) test terms from the leaves upward and remove, or down-weight, the genes of significant descendants before testing a parent; other tools cluster significant terms by the overlap of their genes or by semantic similarity and report one representative per cluster.

### 3.2.5. Length Bias

In RNA-seq, the power to detect a change grows with the number of reads, and at equal expression a longer transcript yields more reads. Differentially expressed lists are therefore enriched in long genes, and sets of long genes appear enriched whatever their biology (Oshlack and Wakefield, 2009). GOseq (Young and colleagues, 2010) corrects for this: it estimates the probability weighting function, the probability that a gene is in the list as a function of its length, and replaces the hypergeometric null, in which every gene is equally likely to be selected, by one in which genes are selected with these probabilities (computed by resampling or by the Wallenius noncentral hypergeometric approximation). The same correction applies to any covariate that affects detection, such as expression level or GC content.

![Length bias in over-representation analysis (simulation, 15000 genes, 10% of them changed twofold independently of length, 3 + 3 negative binomial samples). A: the fraction of genes called changed rises with gene length; line: the fitted probability weighting function. B: p-values for 200 sets of long genes with no true association: hypergeometric p-values are strongly skewed towards zero, p-values from a length-weighted resampling null are close to uniform](./plots/length_bias.py)

## 3.3. Gene Set Enrichment Analysis

### 3.3.1. The Enrichment Score

ORA requires a threshold that splits genes into a list and the rest, discards the information in the size of each change, and misses sets in which many genes change a little. Gene set enrichment analysis (Mootha and colleagues, 2003; Subramanian and colleagues, 2005) uses the whole ranking instead.

**Definition 3.3.1** Let the $N$ genes be ranked by a statistic $r_1 \geq r_2 \geq \cdots \geq r_N$ (for example the Wald statistic of differential expression), and let $S$ be a gene set of size $n$. The running sum of **gene set enrichment analysis** (GSEA) at position $i$ is
$$
\Phi(i) = \sum_{j \le i,\ g_j \in S} \frac{\lvert r_j\rvert^{w}}{N_R} - \sum_{j \le i,\ g_j \notin S} \frac{1}{N - n}, \qquad N_R = \sum_{g_j \in S}\lvert r_j\rvert^{w}, \tag{3.2}
$$
with weight exponent $w$ (usually $1$); the **enrichment score** ES of $S$ is the value of $\Phi(i)$ of largest absolute value.

The running sum starts at zero, rises at each member of the set by its share of the weight, falls by a constant step at each non-member, and returns to zero at the end. ES is large and positive when members concentrate at the top of the ranking, large and negative when they concentrate at the bottom. With $w = 0$ the statistic is the Kolmogorov–Smirnov statistic comparing the positions of members and non-members ([3.2.6](/3.2.6)); $w = 1$ weights members by the size of their change.

The null distribution of ES has no simple form and is obtained by permutation. In phenotype permutation the sample labels are shuffled, the ranking is recomputed and ES recalculated for each permutation; this preserves the correlations between genes and tests a hypothesis about the samples, but needs enough samples to provide many distinct permutations. In gene-set permutation (used in "preranked" analysis), ES is recalculated for random sets of the same size drawn from the ranked list; it works with any number of samples but ignores the correlation between genes, so it is anticonservative for sets of co-regulated genes. To compare sets of different sizes, ES is divided by the mean of the null ES values of the same sign, giving the normalized enrichment score NES, and the FDR is estimated from the distribution of NES over all sets and all permutations.

**Definition 3.3.2** The **leading edge** of a gene set with positive ES is the subset of its members ranked at or before the position where the running sum reaches its maximum (for negative ES, at or after the minimum): the genes that account for the enrichment signal.

**Example 3.3.1** Rank the $18\,865$ airway genes with a symbol and a test result by the Wald statistic of dexamethasone against untreated. For the Hallmark set "TNF-alpha signaling via NF-kB" ($176$ genes in the list) the running sum peaks at rank $1634$ with $\mathrm{ES} = 0.50$; the leading edge has $60$ genes, beginning *DUSP1*, *PER1*, *PTX3*, *DNAJB4*, *IRS2*, *KLF9*, *CEBPD* and including *NFKBIA*. None of $2000$ random gene sets of the same size reached this ES, so $p \le 1/2001$, and $\mathrm{NES} = 1.88$. The null distribution in the figure is bimodal: with $w = 1$ a random set takes its maximum deviation at the top or at the bottom of a ranking whose extreme statistics are large, which is why the null ES values are far from zero.

![GSEA of the airway data for the Hallmark set "TNF-alpha signaling via NF-kB". A: the Wald statistic along the ranked list, from most induced to most repressed. B: positions of the 176 members. C: the running sum (Eq. (3.2)); its maximum is the enrichment score, the shaded region the leading edge. D: ES of 2000 random sets of the same size (histogram) and the observed ES (line)](./plots/gsea_running_sum.py)

The result invites a careless reading: glucocorticoids are anti-inflammatory, so how can they "activate TNF-alpha signaling"? The leading edge answers it. The induced members of the set are *DUSP1* (which dephosphorylates p38 and JNK), *NFKBIA* (IκBα, which retains **NF-κB** in the cytoplasm), *TNFAIP3* (A20), *TNIP1* and *ZFP36* (tristetraprolin), feedback inhibitors that NF-κB itself induces to terminate its response, together with metabolic and circadian genes such as *PER1* and *KLF9* that have glucocorticoid response elements. The glucocorticoid receptor, a **nuclear receptor**, induces these brakes directly, while it represses other members of the same set, among them the chemokine *CCL2*, the cytokine *LIF*, *PTGS2* (cyclooxygenase 2) and *JUN*, which form the cluster of members at the repressed end of the ranking (panel B). A gene set is a list of genes, not a pathway state: "enrichment" of a signaling set means that its members change, in whatever direction and for whatever reason.

### 3.3.2. ORA and GSEA Compared

Testing the $50$ Hallmark sets on the airway data both ways shows how the methods differ. Preranked GSEA finds $24$ sets at an FDR of $0.05$; ORA of the $544$ induced genes (all genes with a symbol as background) finds $17$. TNF-alpha signaling is first in both ($26$ induced genes against $5.1$ expected, $p = 8\times10^{-12}$; $\mathrm{NES} = 1.88$). Oxidative phosphorylation has $\mathrm{NES} = 1.63$ (FDR $0.007$) but only $4$ induced genes against $5.2$ expected: many of its genes rise slightly, none past the threshold. E2F targets, the genes of DNA replication, have $\mathrm{NES} = -1.45$: proliferation genes fall modestly, which a list of induced genes cannot show. The p53 pathway has a negative NES but also an excess of induced genes ($13$ against $5.1$), a set whose members move in both directions.

![Over-representation analysis and GSEA of the 50 Hallmark sets in the airway data. Horizontal: normalized enrichment score of preranked GSEA (orange: positive, blue: negative; filled: FDR < 0.05). Vertical: −log10 p of ORA for the 544 induced genes (ringed: FDR < 0.05; dashed: p = 0.05). Some sets are found only by GSEA (small coordinated shifts, or shifts downward)](./plots/hallmark_ora_gsea.py)

### 3.3.3. Competitive and Self-Contained Hypotheses

Gene-set tests answer one of two different questions (Goeman and Bühlmann, 2007). A competitive test asks whether the genes of the set are more associated with the phenotype than the other genes; ORA and preranked GSEA are competitive, and their unit of sampling is, implicitly, the gene. A self-contained test asks whether any gene of the set is associated with the phenotype at all; it is answered by permuting samples (ROAST, global tests), and its unit of sampling is the sample. The distinction matters because gene-sampling methods treat genes as independent. Genes in a set are often co-regulated, so their statistics are correlated and the effective number of independent observations is smaller than $n$; competitive tests that ignore this, including ORA and preranked GSEA, give p-values that are too small. CAMERA (Wu and Smyth, 2012) estimates the average inter-gene correlation in the set and corrects the variance of the competitive test accordingly. Phenotype permutation preserves the correlation but requires samples: the airway design of four donors, each treated and untreated, allows only $2^4 = 16$ relabelings that respect the pairing (swapping labels within donors), so the smallest attainable p-value is $1/16$.

### 3.3.4. Single-Sample Scores

Sometimes the question is not which sets differ between groups but how active a program is in each sample, for example to correlate a pathway with survival or to compare many conditions. Single-sample methods compute a score per set and sample: ssGSEA computes a GSEA-like running sum on the ranking of genes within one sample (Barbie and colleagues, 2009); GSVA first estimates each gene's distribution across samples, ranks the genes within each sample by how unusual their values are, and computes a Kolmogorov–Smirnov-type score (Hänzelmann, Castelo and Guinney, 2013); AUCell, designed for single cells, scores the area under the recovery curve of the set's genes in each cell's ranking (Aibar and colleagues, 2017). The scores form a matrix of sets by samples that can be analyzed like expression ([7.9.5](/7.9.5), [7.9.13](/7.9.13)).

## 3.4. From Gene Sets to Regulators

A gene set defined by a transcription factor, its regulon, turns enrichment into a statement about regulation: if the targets of a factor change coherently, the factor's activity probably changed, even if its own mRNA did not. Sets of targets come from ChIP-seq peaks near genes, from motifs in promoters and enhancers ([7.8.8](/7.8.8)), from perturbation experiments, and from curated literature; DoRothEA and its successor CollecTRI grade human regulons by confidence. Activity estimation methods score each factor in each sample from the expression of its targets, taking the sign of each interaction into account (activated targets up and repressed targets down both count as activation): VIPER uses an analytic rank-based enrichment of the regulon, and the decoupler framework (Badia-i-Mompel and colleagues, 2022) runs this and simpler methods (weighted means, univariate linear models) on any collection of signed sets. PROGENy does the same for signaling pathways with footprints, genes that respond to perturbation of a pathway rather than its members, which are often regulated post-translationally. A factor whose activity explains a whole expression program is a candidate master regulator ([7.9.11](/7.9.11)).

Pathway topology methods go a step further and use the diagrams themselves. Signaling pathway impact analysis (SPIA; Tarca and colleagues, 2009), for example, combines the over-representation of a pathway's genes with a perturbation score that propagates the observed fold changes along the activating and inhibiting edges of the pathway graph. Such methods depend on the correctness of the diagrams, which summarize many cell types and conditions, and on whether transcript levels reflect the activity of signaling proteins at all; network-based methods are developed in [7.9.12](/7.9.12).

## 3.5. Interpretation and Pitfalls

| Pitfall | What goes wrong | Remedy |
|---|---|---|
| Wrong background | genes that could not appear in the list inflate significance | background = genes tested (expressed, passing filters) |
| Size and generality | large, vague terms dominate | report enrichment ratios; restrict set sizes; compact collections |
| Redundancy | ancestors and siblings of one signal fill the list | graph-aware methods, clustering of terms |
| Detection bias | long or highly expressed genes are detected more easily | covariate-weighted nulls (GOseq) |
| Inter-gene correlation | gene-sampling tests are anticonservative | sample permutation, CAMERA |
| Annotation bias | well-studied genes carry more annotations; famous pathways are enriched in every list | prefer experimental evidence codes; interpret absence cautiously |
| Composition | differences in cell-type proportions produce enrichment of cell-type signatures | estimate proportions; single-cell data ([7.9.5](/7.9.5)) |
| Circularity | testing a list for the sets used to build it | use independent data or sets |
| Over-reading names | a set's name is not a pathway state | look at the leading-edge genes and their direction |

Beyond these, alternative explanations should be considered before a biological one. A study of a brain disease finds "synaptic transmission" enriched among changed genes: is this the disease, or more neurons in the patients' samples, or a background of all human genes when only brain-expressed genes could change? Enrichment results are hypotheses about processes, to be tested like any other.

Displays of results should show effect, significance and size together: dot plots with the enrichment ratio or NES on one axis, the adjusted p-value as colour and the set size as dot size; enrichment plots like the one of 3.3.1 for single sets; heatmaps of sets across conditions or time points; and the changed genes coloured on a pathway map (KEGG, Reactome) to see which branches move.

## 3.6. Tools

| Tool | Methods | Environment |
|---|---|---|
| clusterProfiler | ORA and GSEA for GO, KEGG, Reactome, MSigDB; term clustering and plots | R / Bioconductor |
| fgsea | fast preranked GSEA with adaptive permutation | R |
| topGO, goseq | graph-aware GO tests; length-bias correction | R / Bioconductor |
| limma (camera, roast) | competitive and self-contained tests with correlation | R / Bioconductor |
| GSVA | single-sample scores (GSVA, ssGSEA) | R / Bioconductor |
| GSEApy | GSEA, preranked GSEA, ssGSEA, Enrichr client | Python |
| decoupler | regulator and pathway activity from signed sets (VIPER, ULM, weighted means) | Python, R |
| WebGestalt, g:Profiler, Enrichr, DAVID, KOBAS | ORA and related methods through a web interface | web |

ORA and preranked GSEA are short enough to write directly, which makes their assumptions visible:

```python
import numpy as np
from scipy import stats

def ora(genes, gene_set, background):
    """One-sided hypergeometric test (Eq. 3.1); all arguments are sets of gene symbols."""
    genes, gene_set = genes & background, gene_set & background
    N, K, n, k = len(background), len(genes), len(gene_set), len(genes & gene_set)
    return k, K * n / N, stats.hypergeom.sf(k - 1, N, n, K)

def enrichment_score(ranked_stats, in_set, w=1.0):
    """ranked_stats: statistics sorted in decreasing order; in_set: boolean mask (Eq. 3.2)."""
    hit = np.where(in_set, np.abs(ranked_stats) ** w, 0.0)
    run = np.cumsum(hit / hit.sum() - (~in_set) / (~in_set).sum())
    i = np.argmax(np.abs(run))
    return run[i], i                     # ES and the end of the leading edge

def preranked_gsea(ranked_stats, in_set, n_perm=2000, seed=0):
    rng = np.random.default_rng(seed)
    es, _ = enrichment_score(ranked_stats, in_set)
    null = np.empty(n_perm)
    for b in range(n_perm):              # gene-set permutation: random sets of the same size
        null[b] = enrichment_score(ranked_stats, rng.permutation(in_set))[0]
    same = null[np.sign(null) == np.sign(es)]
    p = (1 + np.sum(np.abs(same) >= abs(es))) / (1 + len(same))
    return es, es / np.abs(same).mean(), p   # ES, NES, p
```

## Summary

- The Gene Ontology (Definition 3.1.1) describes molecular functions, biological processes and cellular components as a directed acyclic graph; by the true-path rule annotations propagate to all ancestors, so term sets are nested; evidence codes and uneven annotation qualify every result (3.1.1). Pathway databases and MSigDB, with its $50$ Hallmark sets, supply curated sets; identifiers must be mapped carefully (3.1.2–3.1.3).
- Over-representation analysis (Definition 3.2.1) uses the hypergeometric tail, Eq. (3.1). In Example 3.2.1 the overlap is below expectation; in the airway data induced genes are enriched in $27$ biological-process terms, including the response to glucocorticoid, from which classic targets such as *FKBP5* are missing (Example 3.2.2).
- The background must be the genes that could be selected (in the simulation $79\%$ against $4.2\%$ false positives); large sets reach significance at small ratios; dependence between terms calls for graph-aware methods; length bias calls for weighted nulls (3.2.2–3.2.5).
- GSEA computes the enrichment score from a weighted running sum along the ranking (Definition 3.3.1, Eq. (3.2)) and assesses it by phenotype or gene-set permutation, with NES and FDR across sets; the leading edge (Definition 3.3.2) identifies the genes behind it. For TNF-alpha signaling in the airway data, $\mathrm{ES} = 0.50$, $\mathrm{NES} = 1.88$, with a leading edge of feedback inhibitors (Example 3.3.1).
- GSEA detects coordinated small shifts and decreases missed by ORA of a list (oxidative phosphorylation, E2F targets; 3.3.2). Competitive tests treat genes as sampling units and are anticonservative under inter-gene correlation; self-contained tests permute samples (3.3.3). ssGSEA, GSVA and AUCell score sets per sample (3.3.4).
- Signed target sets give regulator and pathway activities (VIPER, decoupler, PROGENy); topology methods use pathway graphs (3.4).
- Results are hypotheses about processes: check background, size, redundancy, detection and annotation biases, composition and circularity, and read the leading-edge genes (3.5).

## Questions

1. A gene is annotated by a curator to "cellular response to glucocorticoid stimulus" only. To how many of the terms in the figure of 3.1.1 does it belong after propagation, and why must the propagation be done before ORA?

   **Answer** Following is_a edges upward in the figure: cellular response to glucocorticoid stimulus, response to glucocorticoid, response to corticosteroid, response to steroid hormone, response to lipid, response to hormone, response to chemical, response to endogenous stimulus, response to stimulus and biological_process, that is $10$ terms (in the full ontology also further parents, such as cellular response to corticosteroid and to hormone stimulus). Without propagation the gene would be missing from the sets of the general terms, which would then be tested with incomplete membership: a term's set must contain every gene that has the function, whether it was annotated directly or through a more specific child.

2. Compute the ORA p-value for a set of $40$ genes of which $9$ are in a list of $600$ genes, with a background of $15\,000$ genes. What is the enrichment ratio?

   **Answer** The expected overlap is $600 \cdot 40/15\,000 = 1.6$, so the ratio is $9/1.6 = 5.6$. The hypergeometric tail $\mathbb{P}(X \ge 9)$ with $N = 15\,000$, $n = 40$, $K = 600$ is about $2.2\times10^{-5}$ (`scipy.stats.hypergeom.sf(8, 15000, 40, 600)`); the binomial approximation with $p = 0.04$ and $40$ trials gives a similar value.

3. A researcher submits $300$ genes differentially expressed in the liver to a web tool that uses all $20\,000$ human genes as background, and finds "lipid metabolic process" enriched with $p = 10^{-6}$. What would you check, and why?

   **Answer** Whether the enrichment survives the correct background, the genes expressed and tested in the liver: lipid metabolism genes are highly expressed in hepatocytes, so any list of liver-expressed genes is enriched in them (3.2.2). One should rerun the test with the tested genes as background, inspect the enrichment ratio and the genes in the overlap, and ask whether the direction (up or down) and the specific genes make sense, for example by comparing with a random list of the same size drawn from the expressed genes.

4. Why is a GSEA result for a set of $15$ genes with $\mathrm{ES} = 0.8$ not directly comparable to one for a set of $400$ genes with $\mathrm{ES} = 0.4$? How is the comparison made?

   **Answer** The null distribution of ES depends on the set size: small random sets fluctuate more and reach large ES by chance more easily, large random sets have ES closer to (but, with $w = 1$, not at) zero. The comparison is made after normalization, $\mathrm{NES} = \mathrm{ES}/\mathbb{E}[\mathrm{ES}_{\text{null}} \mid \text{same sign}]$, computed from permutations for each set separately, and through the FDR estimated from the NES distribution over all sets. The small set's ES of $0.8$ might have a smaller NES than the large set's $0.4$.

5. In Example 3.3.1, what is the probability that the observed ES would not be exceeded by any of $2000$ random sets if the true permutation p-value were $0.002$? What does this say about reporting $p \le 1/2001$?

   **Answer** If each random set exceeds the observed ES independently with probability $0.002$, the chance that none of $2000$ does is $(1 - 0.002)^{2000} \approx \mathrm{e}^{-4} = 0.018$. So "no random set exceeded it" is strong but not conclusive evidence that $p < 0.002$; the estimate $1/2001$ is a bound limited by the number of permutations, and smaller p-values require more permutations (adaptive schemes such as fgsea's) or an approximation of the null tail. Gene-set permutation also ignores inter-gene correlation, so the true p-value of the competitive hypothesis is larger than this bound suggests (3.3.3).

6. Explain why ORA of the induced genes cannot find the decrease of E2F targets in the airway data, and design an ORA that would.

   **Answer** The E2F targets fall modestly; few of them are among the induced genes (here $3$ against $5.6$ expected), so a test of the induced list finds nothing or at most a weak depletion. Testing the list of repressed genes (adjusted $p < 0.05$, $\log_2\mathrm{FC} < 0$, perhaps without a fold-change cutoff, since the changes are small) asks the right question; even then a strict threshold may leave too few genes, which is the situation where GSEA, using the whole ranking, is more powerful.

7. A self-contained gene-set test with sample permutation is applied to a paired design with $5$ donors. What is the smallest possible p-value? How would you obtain smaller p-values for a set of interest?

   **Answer** Respecting the pairing, the labels can only be swapped within donors: $2^5 = 32$ relabelings including the observed one, so the smallest p-value is $1/32 \approx 0.031$, too large to survive correction over many sets. Smaller p-values require either more samples, or a parametric self-contained test (for example ROAST, which rotates residuals of a linear model instead of permuting and can generate many more null samples), or a competitive test that accounts for inter-gene correlation (CAMERA), each with its own assumptions.

8. A GSEA of a tumor-versus-normal comparison finds "interferon gamma response" and "allograft rejection" strongly enriched. Give a biological and a compositional explanation, and an analysis that separates them.

   **Answer** Biologically, tumor cells or the tissue might respond to interferon, for example in an inflamed tumor. Compositionally, tumors may contain more immune cells (T cells, macrophages) than normal tissue, and the immune cells express these genes regardless of any change in their state. Estimating cell-type proportions by deconvolution with single-cell references and including them as covariates, comparing within purified populations, or using single-cell or spatial data ([7.9.5](/7.9.5), [7.9.6](/7.9.6)) distinguishes a change of state from a change of composition.

9. Why do VIPER-like activity estimates use the sign of each regulatory interaction, and what goes wrong if the signs are ignored?

   **Answer** A factor that activates some targets and represses others changes the expression of the two groups in opposite directions. Ignoring signs, the two groups cancel in a directional score, or, with absolute values, any perturbation of the targets is read as activation. With signs, the activity is the agreement of the observed changes with the expected direction of each interaction, which also distinguishes activation from inhibition of the factor. The quality of the estimate depends on correct signs and on the regulon containing direct targets.
