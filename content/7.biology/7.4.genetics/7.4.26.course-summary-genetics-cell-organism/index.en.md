---
title: "Course Summary: Genetics from Cell to Organism"
description: "The course assembled into one picture: an index of every calculation tool with its numbered formula or algorithm; a decision tree for the mode of inheritance; the chain of genetic inference from segregation to function and the lineages of genetic method; how cell biology, genetics and development form one system; an assessment of the claim that genetics is simple and finished; an index of the quantitative models and a table of diseases by genetic mechanism."
---

The preceding twenty-five chapters followed **genes** from one cross to whole populations: how **alleles** segregate and assort, how they interact, where they lie, how they change, how they are switched on and off across generations, and how their variation adds up to the variation of complex traits. This chapter adds no new mechanism. It collects the calculation tools of the course in one index (26.1), turns the recognition of inheritance patterns into one decision procedure (26.2), reconstructs the chain of reasoning by which genetics goes from a **phenotype** to a gene and its function and the lineages of method that carry it (26.3), places the course between **cell biology** ([7.3](/7.3)) and developmental biology ([7.5](/7.5)) (26.4), and asks whether genetics is as simple, and as finished, as it is often said to be (26.5). It ends with an index of the quantitative models and a table of diseases arranged by genetic mechanism (26.6). The statistical methods used throughout are developed in [3.1](/3.1) and [3.2](/3.2); the molecular basis of genes, **mutation** and recombination is in [7.2](/7.2); the evolutionary consequences continue in [7.10](/7.10), and the statistical and computational treatment of genomic data in [7.7](/7.7) and [7.8](/7.8).

## 26.1. The Calculation Toolbox

### 26.1.1. An Index of Methods

Almost every genetic inference is a calculation on counts. The table lists the tools of the course in the order of the chapters, each with the numbered object that states it; the right column is what the tool is used for.

| Question | Tool | Key relation | Object |
|---|---|---|---|
| How many progeny or **genomes** are needed? | at least one success in $n$ trials | $n \ge \ln(1-\gamma)/\ln(1-p)$; coverage $1 - \mathrm{e}^{-Np}$ | Formulas 1.6.1, 1.2.1 |
| Probability of a **genotype** in a cross | **law of segregation**, **law of independent assortment**; product and sum rules | **locus** by locus; $2^n$ gametes, $3^n$ genotypes | Formulas 2.4.1, 2.4.2, Algorithm 2.4.1 |
| Exactly $k$ of $n$ progeny in a class | binomial and multinomial | $\binom{n}{k}p^k(1-p)^{n-k}$ | Formula 2.4.3 |
| Does a ratio fit? | χ² goodness of fit | $\sum(O-E)^2/E$, $k-1$ df | Formula 2.5.1, Algorithm 2.5.1 |
| Genotype of a dominant $\mathrm{F}_2$ plant | conditioning | $\mathbb{P}(Yy \mid \text{dominant}) = 2/3$ | Formula 2.2.1 |
| Lethality and reduced viability | renormalizing | $q_jv_j/\sum q_iv_i$; 2:1, 6:3:2:1 | Formulas 3.4.1, 4.8.1 |
| Incomplete **penetrance** | Bayes | $\mathbb{P}(G \mid \text{unaffected})$; $\pi = 1 - \mathrm{e}^{-m}$ | Formulas 3.5.1, 3.5.2 |
| Two genes, one trait | merged classes of 9:3:3:1 | 9:3:4, 9:7, 12:3:1, 13:3, 15:1, 9:6:1 | Formula 4.2.1, Algorithm 4.8.1 |
| Same gene or different genes? | **complementation test** | **complementation groups** as connected components | Algorithms 4.4.1, 13.1.1 |
| Interaction of two mutations | multiplicative **expectation** | $\varepsilon_{ab} = W_{ab} - W_aW_b$ | Formula 4.3.1 |
| Polygenic classes | $\mathrm{Bin}(2n, 1/2)$ | extreme class $4^{-n}$ | Formula 4.6.1 |
| **X-linked** crosses and frequencies | criss-cross; males $q$, females $q^2$ | exceptional progeny $e = s/(2-s)$ | Algorithm 6.4.1, Formulas 6.4.1, 6.4.2 |
| Mode of inheritance in a **pedigree** | elimination of hypotheses | male-to-male transmission excludes X **linkage** | Algorithm 7.2.1 |
| Genetic risk | chain of transmission; Bayesian table | **carrier** after $k$ unaffected sons $1/(1+2^k)$ | Algorithms 7.3.1, 7.4.1, Formulas 7.4.1, 7.4.2 |
| **Inbreeding coefficient** | path counting | $F = \sum (1/2)^n(1 + F_A)$; first cousins $1/16$ | Formula 7.5.1 |
| Recessive disease in a child of relatives | mixture of IBD and non-IBD | $q^2 + Fq(1-q)$ | Formula 7.5.2 |
| Linkage and map distance | **recombination frequency**; three-point **testcross** | $r = (\mathrm{SCO} + \mathrm{DCO})/n$; $C = \mathrm{DCO}/r_1r_2$ | Definition 8.3.1, Algorithm 8.4.1, Definition 8.4.3 |
| From $r$ to distance | **mapping function** | Haldane $d = -\tfrac12\ln(1-2r)$; Kosambi | Formulas 8.3.1, 8.5.1, 8.5.2 |
| Estimating $r$ | testcross, square root, MLE from an $\mathrm{F}_2$ | $\hat r = R/n$, $\operatorname{se} = \sqrt{\hat r(1-\hat r)/n}$ | Formulas 8.6.1–8.6.3, Algorithm 8.7.1 |
| Tetrads | PD, NPD, T; MII patterns | $r = (\mathrm{NPD} + \tfrac12\mathrm{T})/n$; Perkins $50(\mathrm{T} + 6\,\mathrm{NPD})/n$; **centromere** $\tfrac12\%\mathrm{MII}$ | Formulas 9.2.1–9.3.3 |
| Bacterial maps | time of entry, **cotransduction** | $C = (1 - d/L)^3$ | Formulas 10.4.1, 10.5.1, Algorithms 10.4.1, 10.5.1 |
| **Heteroplasmy** across generations | binomial sampling of $N$ units | $\operatorname{Var}(h_t) = h_0(1-h_0)[1-(1-1/N)^t]$ | Formulas 11.4.1, 11.5.1 |
| Spread of an endosymbiont | frequency recursion | threshold $\hat p = s_{\mathrm{f}}/s_{\mathrm{h}}$ | Formula 11.6.2 |
| **Mutation rate** from cultures | **fluctuation test** | $\mathbb{P}(r=0) = \mathrm{e}^{-m}$, $\hat\mu = \hat m/N_t$ | Formula 12.4.1, Algorithm 12.4.1 |
| Dominant negative alleles | random assembly | active fraction $(1-f)^n$ | Formula 12.3.1 |
| Fine structure | phage crosses, deletion intervals | $\mathrm{RF} = 2K/B$; unseen sites $n_1^2/2n_2$ | Formulas 13.2.1, 13.2.2, Algorithm 13.2.1 |
| Genome assembly | Lander–Waterman | uncovered $\mathrm{e}^{-c}$, **contigs** $N\mathrm{e}^{-c\sigma}$ | Formula 14.2.1 |
| Linkage in human families | **LOD score** | $\log_{10}[\theta^R(1-\theta)^{n-R}2^n]$; $Z \ge 3$ | Formulas 14.9.1, 14.9.2, Proposition 14.9.1 |
| Products of rearrangements | crossover in a loop; quadrivalent segregation | unbalanced $u = \tfrac12(1-\mathrm{e}^{-2d})$; **pseudolinkage** $r_1 + r_2 - 2r_1r_2$ | Formulas 15.4.1, 15.5.1–15.5.3 |
| Aneuploids and polyploids | segregation of three or four homologues | trisomic $1:2:2:1$; duplex selfed $35:1$; triploid euploid $2^{1-x}$ | Formulas 16.3.1, 16.4.1, 16.5.1, 16.5.2 |
| Selfish elements | copy number, drive | $n^* = (u - v - a)/b$; drive equilibrium | Formulas 17.6.1, 17.6.2, 19.6.1 |
| **Epialleles** | two-state **Markov chain** | $\pi = \beta/(\alpha + \beta)$ | Formula 18.7.1 |
| Screens and breeding schemes | Poisson saturation; low MOI | missed genes $\mathrm{e}^{-\lambda}$; $1/4$ experimental animals | Formulas 19.4.1, 19.4.2, 19.5.1, 19.5.2 |
| Mapping a **mutant** by sequencing | **allele frequency** in a pool | $1 - r(d)$ peaks at the gene | Formula 20.2.1 |
| Hereditary versus sporadic **tumors** | Poisson two-hit model | $m_1 = N\mu t$, $m_2 \approx N(\mu t)^2$ | Formula 21.3.1 |
| Population genotype frequencies | **Hardy–Weinberg equilibrium** | $p^2:2pq:q^2$; carriers $\approx 2\sqrt{Q}$ | Theorem 22.2.1, Formula 22.2.1, Algorithm 22.2.1 |
| ABO and other multiallelic loci | Bernstein; gene counting (EM) | $\hat r = \sqrt{\bar O}$ | Formula 22.2.2, Algorithm 22.2.2 |
| Two loci | **linkage disequilibrium** | $D_t = (1-r)^tD_0$ | Theorem 22.3.1 |
| Inbreeding and subdivision | $F$; **Wahlund effect** | $p^2 + Fpq$; deficit $2\operatorname{Var}(p)$ | Formula 22.4.1, Theorem 22.4.1 |
| Forensic and paternity evidence | **likelihood ratio** | product rule with $\theta$; $\mathrm{PI} = t/p_i$ | Formulas 22.5.1, 22.5.2 |
| Mutation, migration, selection | one-generation recursions | $\Delta q \approx -sq^2$ or $-hsq$; $t \approx \tfrac1s\ln(p_tq_0/p_0q_t)$ | Formulas 23.1.1, 23.2.1, Theorem 23.3.1, Formulas 23.3.1–23.3.3 |
| Balanced polymorphism | **heterozygote advantage**; **mutation–selection balance** | $\hat q = s_1/(s_1+s_2)$; $\sqrt{\mu/s}$, $\mu/hs$ | Theorems 23.3.2, 23.4.1 |
| Mutation rate from incidence | Haldane's indirect method | $\mu \approx \tfrac12(1-f)I$ | Formula 23.4.1 |
| Drift | **Wright–Fisher model**; **effective population size** | $H_t = H_0(1 - 1/2N)^t$; $N_e$ of a sex ratio | Theorem 23.5.1, Formula 23.5.1 |
| Fate of a new mutation | diffusion | $u(p) = (1-\mathrm{e}^{-4N_esp})/(1-\mathrm{e}^{-4N_es})$ | Theorem 23.6.1 |
| Neutral evolution | substitution and diversity | $k = \mu$; $\theta = 4N_e\mu$ | Theorem 23.7.1, Formula 23.7.1 |
| Number of loci behind a trait | Castle–Wright | $n = (\bar P_1 - \bar P_2)^2/8(V_{F_2} - V_{F_1})$ | Formula 24.1.1 |
| Heritability | **variance** components; relatives; twins | $V_A = 2pq\alpha^2$; $b_{O\cdot\bar P} = h^2$; $h^2 = 2(r_{\mathrm{MZ}} - r_{\mathrm{DZ}})$ | Formula 24.2.1, Theorem 24.3.1, Formulas 24.4.1–24.4.3 |
| **Response to selection** | **breeder's equation** | $R = h^2S = ih^2\sigma_P$ | Theorem 24.5.1, Formula 24.5.1 |
| **Threshold traits** | **liability** | $h^2 \approx (t - t_R)/(r\mu_{\mathrm{aff}})$ | Formula 24.6.1 |
| QTL in crosses | marker classes; interval mapping | $(1 - 2r)\delta$; permutation threshold | Formula 25.1.1, Algorithm 25.1.1 |
| **Genome-wide association study** | allelic χ², **odds ratio**, threshold, power | $p < 5\times10^{-8}$; $\lambda = N\cdot 2pq\beta^2/\sigma^2$ | Formulas 25.3.1–25.3.3 |
| From signal to variant | **fine-mapping**; **Mendelian randomization** | PIP from approximate **Bayes factors**; Wald ratio | Formulas 25.4.1, 25.4.2 |
| Prediction | **polygenic score** | $R^2 \approx h^2/(1 + M_e/Nh^2)$ | Formula 25.6.1 |

### 26.1.2. Four Recurring Mathematical Ideas

The table is long, but its entries are built from four ideas, which the figure arranges as a dependency graph.

1. Independent transmission with probability one half. Every gamete of a **heterozygote** carries each allele with probability $1/2$, independently of other unlinked loci and of other gametes. The product rule (Formula 2.4.1), the binomial (Formula 2.4.3), Hardy–Weinberg proportions (Theorem 22.2.1), the coefficient of $(1/2)^n$ in the path method (Formula 7.5.1) and the genetic **covariance** of relatives (Formula 24.4.1) are all consequences of this one assumption, and most of the departures studied in the course (linkage, drive, imprinting, maternal and organellar inheritance) are departures from it.
2. Poisson counts and the zero term. Crossovers along a **chromosome** (Formula 8.5.1), mutations in a growing culture (Formula 12.4.1), hits in a mutagenesis screen (Formulas 1.2.1, 19.5.1), second hits in a retina (Formula 21.3.1), reads on a genome (Formula 14.2.1) and vectors in a cell (Formula 19.5.2) are counted by a **Poisson distribution**, and the useful quantity is almost always the probability of zero, $\mathrm{e}^{-m}$: no crossover, no mutant, no hit, a gap.
3. Likelihood. Estimating $r$ from an $\mathrm{F}_2$ (Formula 8.6.3), the **LOD score** (Formula 14.9.1), the paternity index (Formula 22.5.2), gene counting by EM (Algorithm 22.2.2) and **fine-mapping** (Formula 25.4.1) all compare the probability of the data under alternative hypotheses, and Bayesian risk (Algorithm 7.4.1) adds a prior. **Maximum likelihood estimation** and **Bayes' theorem** are the general forms ([3.2](/3.2)).
4. Recursions over generations. Allele frequencies under selection (Theorem 23.3.1), mutation (Formula 23.1.1), migration (Formula 23.2.1), drive (Formula 17.6.2) and **cytoplasmic incompatibility** (Formula 11.6.2), the decay of **linkage disequilibrium** (Theorem 22.3.1) and of **heterozygosity** under inbreeding (Formula 22.4.2) and drift (Theorem 23.5.1), and the methylation state of an epiallele (Formula 18.7.1) are maps $x_{t+1} = f(x_t)$, linear or nonlinear, deterministic or a **Markov chain**.

![How the formulas of the course depend on one another, in four blocks. Transmission (7.4.2–7.4.7): the product and sum rules generate the binomial and multinomial, the modified dihybrid ratios that the χ² test checks, Bayesian risk and the path method for inbreeding. Mapping (7.4.8–7.4.14): Mather's formula and the bound r ≤ 1/2 lead to the Haldane and Kosambi mapping functions and to tetrad frequencies; the estimation of r and the three-point testcross lead to the LOD score. Populations (7.4.22–7.4.23): Hardy–Weinberg proportions underlie inbreeding, the selection recursion and mutation–selection balance, and drift. Quantitative traits (7.4.24–7.4.25): the polygenic binomial and additive and dominance variance lead to the covariance of relatives and the breeder's equation; indirect association leads to GWAS power and polygenic scores. Dashed arrows cross between blocks: binomial sampling gives likelihoods of r and genetic drift; Bayesian reasoning gives the LOD threshold; the path method gives the inbreeding coefficient of a population; recombination frequency sets the decay of linkage disequilibrium, which makes indirect association possible; and genotype frequencies give the additive variance](./plots/formula-map.py)

### 26.1.3. Combining the Tools

Real problems use several tools at once. The two examples below combine chapters that were written separately.

**Example 26.1.1 (An Isolated Case of an X-Linked Lethal)** A woman's only brother has Duchenne muscular dystrophy; there is no other family history, and the disease prevents reproduction ($f \approx 0$). She has two unaffected sons. What is the risk that her next son is affected?

1. Prior for the mother. At mutation–selection balance for an X-linked lethal, one third of affected males carry a new mutation that arose in their mother's germ line, and two thirds received an allele carried by the mother (Formula 23.4.1). So the mother is a carrier with probability $2/3$.
2. Prior for the woman. If her mother is a carrier, she inherited the allele with probability $1/2$: prior $2/3 \times 1/2 = 1/3$ (new mutations in her own conception are negligible).
3. Conditioning on two unaffected sons (Algorithm 7.4.1): joint probabilities $\tfrac13 \cdot \tfrac14 = \tfrac1{12}$ (carrier) and $\tfrac23 \cdot 1 = \tfrac{8}{12}$ (noncarrier), so the posterior is $1/9$ (Formula 7.4.1 with $\pi = 1/3$).
4. Risk for the next son: $\tfrac19 \times \tfrac12 = \tfrac1{18} \approx 5.6\,\%$.

The answer joins **population genetics** (the prior) and Bayesian **pedigree** analysis (the conditioning); a carrier test of the woman, with its detection rate, would enter as one more column of the same table.

**Example 26.1.2 (One Cross, Three Questions)** A dihybrid $\mathrm{F}_2$ of 320 plants gives 182 colored, 61 of a second color and 77 white. (a) The total is close to a multiple of 16, and the classes fit $9:3:4$ (expected 180, 60, 80): $\chi^2 = 0.15$ with 2 df, $p = 0.93$ (Formula 2.5.1); the merged class $3 + 1$ means **recessive epistasis** (Formula 4.2.1). (b) The hypothesis predicts a testcross ratio $1:1:2$ and that one third of the colored $\mathrm{F}_2$ plants breed true for the second locus, which is a second, independent test (Algorithm 4.8.1). (c) If the two genes were linked in **coupling**, the white class would no longer be $4/16$ and the colored classes would not be in $3:1$ within the non-white plants; the ratio itself therefore also tests independent assortment, but weakly, and a testcross with the $2\times2$ test of Algorithm 8.7.1 is the right design for linkage.

## 26.2. Deciding the Mode of Inheritance

Most problems in transmission genetics begin with the same question: what kind of inheritance does this trait have? The course answered it in pieces (Algorithms 4.8.1, 6.4.1, 7.2.1, 11.1.1, 15.1.1, 18.2.1). Assembled, they form one procedure.

**Algorithm 26.2.1 (Mode of Inheritance from Crosses)**

1. Make **reciprocal crosses**. If the $\mathrm{F}_1$ are the same, the determinant is nuclear and its transmission does not depend on the sex of the parent: go to step 2. If they differ, go to step 4.
2. Count the classes of the $\mathrm{F}_2$ or of the testcross and reduce them to a ratio with $T$ parts. $T = 4$ ($3:1$, $1:2:1$; $2:1$ with a recessive lethal) means one gene; $T = 16$ means two, with the classes of $9:3:3:1$ possibly merged (Algorithm 4.8.1); $T = 64$ three. A continuous distribution means many genes and calls for variance components (7.4.24).
3. For two genes, make a testcross. Four classes in equal frequencies mean independent assortment; an excess of the parental classes means **linkage**, and the recombinant fraction is the **recombination frequency** (Algorithm 8.4.1 for three loci). Test with the $2\times2$ χ² (Algorithm 8.7.1).
4. If the reciprocal $\mathrm{F}_1$ differ and sons differ from daughters, the gene is X-linked (or Z-linked in birds): sons of a mutant mother are mutant (Algorithm 6.4.1).
5. If the sexes do not differ, ask whom the phenotype follows. The mother in every generation, with nuclear markers replaced by backcrossing: an **organelle** or endosymbiont (Algorithm 11.1.1). The genotype of the mother, so that $\mathrm{F}_2$ individuals are all of one type and the $\mathrm{F}_3$ broods segregate $3:1$: a **maternal effect** (Formula 11.6.1). The sex of the parent who transmitted the allele: **genomic imprinting** (Algorithm 18.2.1).
6. In every branch, look for the anomalies that signal a special mechanism: ratios with missing classes (lethality), skipped generations (incomplete **penetrance**), recessive phenotypes appearing in heterozygotes for a set of adjacent loci (**pseudodominance**, a deletion), half-sterile heterozygotes and markers on two chromosomes that behave as linked (a **reciprocal translocation**), and recombination that disappears in one region in heterozygotes only (an **inversion**).

For humans the crosses are replaced by a pedigree, and the steps become the elimination rules of Algorithm 7.2.1: male-to-male transmission excludes X linkage, affected children of unaffected parents indicate recessive inheritance, transmission only through mothers to all their children indicates mitochondrial inheritance, and remaining hypotheses are compared by their likelihoods (the LOD logic of 7.4.14).

![The decision procedure of Algorithm 26.2.1. From the data (top), the first question is whether reciprocal crosses give the same F1. If they do, the number of parts of the F2 ratio gives the number of genes (T = 4: one gene, with 3:1, 1:2:1 or a 2:1 lethal ratio; T = 16: two genes with 9:3:3:1 or a merged ratio), and a testcross of two loci decides between linkage (excess of parental classes; recombination frequency and map) and independent assortment (1:1:1:1, tested by χ²). If they do not, a difference between sons and daughters means X linkage with criss-cross inheritance; otherwise the phenotype follows the mother in every generation (organellar inheritance), the genotype of the mother (maternal effect, with 3:1 among F3 broods) or the sex of the transmitting parent (imprinting). Human pedigrees follow the same logic with Algorithm 7.2.1. The bottom row lists anomalies that point to a special mechanism in any branch: 2:1 and 6:3:2:1 ratios (lethal alleles), skipped generations (incomplete penetrance), pseudodominance (a deletion), semisterility and pseudolinkage (a translocation) and continuous variation (polygenes); chapter sections in parentheses](./plots/decision-tree.py)

**Example 26.2.1** A recessive mutant female is crossed with a wild-type male and the reciprocal cross is made. In the first cross all sons are mutant and all daughters **wild type**; in the reciprocal cross all progeny are wild type. The $\mathrm{F}_2$ of the first cross has half mutant sons and half mutant daughters. Step 1 sends us to step 4; the sexes differ in the way the X chromosome predicts (sons receive their only X from the mother), and the $\mathrm{F}_2$ ($X^mX^+ \times X^mY$) gives $\tfrac12$ mutant in each sex: X-linked recessive. Had the first cross given only mutant progeny of both sexes, and its $\mathrm{F}_2$ only mutants as well, step 5 would point to organellar inheritance; had the $\mathrm{F}_1$ of the first cross been mutant but the $\mathrm{F}_2$ all wild type, to a **maternal effect** (Figure in 7.4.11).

## 26.3. The Logic of Genetic Inference

### 26.3.1. From Phenotype to Function

The chapters can be read as the steps of one argument, which every forward genetic analysis repeats.

| Step | Question | Method | Chapter |
|---|---|---|---|
| 1. Isolation | Is the variant heritable? | **forward genetic screen**, selection; balancers keep it | [7.4.1](/7.4.1), [7.4.19](/7.4.19), [7.4.15](/7.4.15) |
| 2. Segregation analysis | How many genes, how dominant? | ratios, χ², penetrance | [7.4.2](/7.4.2), [7.4.3](/7.4.3) |
| 3. Complementation | Are two mutations in the same gene? | trans heterozygote; **cis–trans test** | [7.4.4](/7.4.4), [7.4.13](/7.4.13) |
| 4. Mapping | Where is the gene? | recombination, tetrads, deficiencies, LOD, mapping by sequencing | [7.4.8](/7.4.8)–[7.4.10](/7.4.10), [7.4.14](/7.4.14), [7.4.20](/7.4.20) |
| 5. Interaction | Which genes act together, in what order? | **epistasis analysis**, suppressors, **enhancers**, **synthetic lethality** | [7.4.4](/7.4.4), [7.4.20](/7.4.20) |
| 6. Cloning | Which DNA sequence is the gene? | **positional cloning**, **transposon tagging**, **transgene** rescue | [7.4.14](/7.4.14), [7.4.17](/7.4.17), [7.4.19](/7.4.19) |
| 7. Function | What does it do, where and when? | allelic series, mosaics and **cell autonomy**, temperature shifts, reporters | [7.4.12](/7.4.12), [7.4.9](/7.4.9), [7.4.20](/7.4.20) |

**Reverse genetics** runs the same chain from the other end: from a sequence (a conserved gene, a GWAS signal, a variant found in a patient) to a designed allele ([7.4.19](/7.4.19)) and its phenotype. The two directions meet at rescue, the experiment that proves that a particular sequence causes a particular phenotype (7.4.1). The same logic is applied in humans without crosses: association replaces segregation, linkage disequilibrium replaces recombination in controlled crosses (Formula 25.2.1), fine-mapping replaces the recombinants of a **near-isogenic line**, and **Mendelian randomization** uses Mendel's law itself as a randomized experiment (Definition 25.4.3).

Two principles of inference recur at every step. First, a genetic conclusion is a statement about necessity or sufficiency that is tested by a further cross: complementation, rescue, a double mutant, a reciprocal cross. Second, the strength of the conclusion is a likelihood: a LOD of 3 is a posterior of about $0.95$ only because the prior for linkage is about $0.05$ (Proposition 14.9.1), and a genome-wide threshold of $5\times10^{-8}$ reflects about a million independent tests (Formula 25.3.2).

### 26.3.2. Lineages of Method

Methods in genetics change faster than the logic they serve. The figure follows four lineages in which a later method inherits the reasoning of an earlier one.

![Four lineages of genetic method, with the chapter of the course in parentheses. Crosses and maps: Mendel's segregation and assortment (1865), Morgan's white-eyed fly and X linkage (1910), Sturtevant's first map (1913), Haldane's mapping function (1919), Creighton and McClintock's cytological proof of exchange (1931), Lindegren's ordered tetrads (1933), interrupted mating in bacteria (1956) and Benzer's fine structure of the rII gene (1959). Mutants and screens: Muller's induction of mutations by X-rays (1927), Beadle and Tatum (1941), the Luria–Delbrück fluctuation test (1943), Brenner's screen in *C. elegans* (1974), the saturation screens of Nüsslein-Volhard and Wieschaus (1980), knockout mice (1989), genome-wide CRISPR screens (2014) and saturation genome editing (2018). Human genetics and genomes: Garrod's alkaptonuria (1902), Morton's LOD score (1955), linkage maps of DNA markers (1980), linkage of Huntington disease to chromosome 4 (1983), cloning of the cystic fibrosis gene (1989), the draft human genome (2001), the first large GWAS (2007) and the telomere-to-telomere genome (2022). Populations and quantitative traits: Hardy–Weinberg (1908), Fisher's polygenic model and variance partition (1918), Wright's drift and inbreeding (1931), Kimura's fixation probability (1962), Falconer's liability model (1965), the neutral theory (1968), SNP heritability (2010) and biobank-scale polygenic scores (2018). Solid arrows join methods within a lineage, dashed arrows across lineages: Sturtevant's counting of recombinants becomes the LOD score; Mendel's ratios become Hardy–Weinberg proportions; one gene–one enzyme becomes the fine structure of the gene; SNP heritability and GWAS share the polygenic model. The axis is compressed threefold before 1940](./plots/method-lineages.py)

Three regularities stand out. The unit of analysis has shrunk from a chromosome arm to a **base pair** (Benzer's $0.02$ map units, saturation editing of every possible substitution), while the scale has grown from one family to millions of people and from one gene to every gene at once. Each new technology was absorbed into an existing logic rather than replacing it: DNA markers made Sturtevant's mapping possible in humans, sequencing made mutant mapping a frequency measurement (Formula 20.2.1), and CRISPR made the forward screen a pooled experiment whose statistics are those of Poisson sampling (Formula 19.5.2). And the questions that each lineage asks have moved from the presence of an effect (is there a gene, is it linked) to its size and its distribution (how much variance, how many loci, how predictive).

## 26.4. From Cell to Organism

Cell biology, genetics and developmental biology tell one story at three levels. Cell biology describes the machinery that copies and partitions chromosomes, packages and marks them, and divides and specializes cells; genetics follows the consequences of that machinery for transmission between generations and for variation among individuals; developmental biology uses the genetic tools to ask how one genome builds an organism. The table and the figure pair each piece of machinery with its genetic consequence and with what is built on it.

| Cell (7.3, 7.2) | Genetics (7.4) | Development (7.5), evolution (7.10) |
|---|---|---|
| **meiosis**: pairing, the **synaptonemal complex**, crossovers and chiasmata, **cohesin** and the spindle ([7.3.21](/7.3.21)) | segregation and assortment (Proposition 5.3.1); $r \le 1/2$ (Formula 8.3.1); **interference**; tetrads; **nondisjunction** and maternal age (Formula 16.2.1) | germ cells and **gametogenesis** (Definition 5.6.1); the meiotic origin of most aneuploid conceptions |
| chromosome structure, **karyotype**, **centromeres** ([7.3.17](/7.3.17), [7.2.2](/7.2.2)) | deletions, duplications, inversions, translocations ([7.4.15](/7.4.15)); **aneuploidy** and **polyploidy** ([7.4.16](/7.4.16)); **dosage balance** | dosage-sensitive development: the phenotypes of trisomies and of haploinsufficient regulators |
| **heterochromatin**, **X-chromosome inactivation**, **DNA methylation** ([7.3.17](/7.3.17), [7.2.15](/7.2.15)) | **dosage compensation** ([7.4.6](/7.4.6)); imprinting, position-effect variegation, epialleles ([7.4.18](/7.4.18)) | **cell memory**: Polycomb and trithorax keep *Hox* states; X inactivation chosen once per lineage |
| mitochondria and **plastids**, their genomes and partition ([7.3.12](/7.3.12)) | organellar inheritance, **heteroplasmy** drift, thresholds (Formula 11.4.1) | maternal contributions to the egg; **maternal-effect genes** set the axes (Definition 20.2.1) |
| the **cell cycle** and its checkpoints, **cancer** cells ([7.3.20](/7.3.20), [7.3.26](/7.3.26)) | the two-hit model (Formula 21.3.1), **loss of heterozygosity**, drivers and **mutational signatures** | the control of tissue growth; cancer as a failure of the constraints of development |
| signaling pathways ([7.3.18](/7.3.18), [7.3.19](/7.3.19)) | pathway order from **epistasis** (Algorithm 20.5.1); **modifier screens** in a **sensitized background** | induction, morphogen gradients and signaling centers |
| differentiation, **stem cells**, clonal dynamics ([7.3.24](/7.3.24)) | **mitotic recombination**, **twin spots** and **genetic mosaics** (Definition 9.5.2); **cell autonomy** (Definition 20.4.1); screens ([7.4.19](/7.4.19)) | the segmentation hierarchy (Definition 20.6.1), **homeotic genes** and colinearity; fate maps from clones |
| variation among individuals | populations, **quantitative traits**, GWAS ([7.4.22](/7.4.22)–[7.4.25](/7.4.25)) | adaptation, speciation and the coalescent ([7.10](/7.10)) |

![Cell biology, genetics and development as one system. Each row pairs a piece of cellular machinery (left, from 7.3 and 7.2) with the genetic phenomenon that it explains (middle, this course) and with the developmental or evolutionary question built on it (right): meiosis gives segregation, assortment, recombination and maps, and through errors maternal-age aneuploidy; chromosome structure gives rearrangements and changes of number, whose effects on development are dosage effects; chromatin and X inactivation give dosage compensation, imprinting and position effects, and in development the cell memory kept by Polycomb and trithorax; organelles give maternal and organellar inheritance, as maternal-effect genes give the axes of the embryo; the cell cycle and its checkpoints give the two-hit genetics of cancer; signaling pathways are ordered by epistasis analysis and pattern the embryo by induction; differentiation and clonal growth are studied with mosaics, twin spots and screens, which revealed the segmentation hierarchy and the Hox genes; and variation among individuals is the subject of population and quantitative genetics and leads to evolution (7.10). Filled arrows: mechanism; open arrows: tool or input](./plots/cell-genetics-development.py)

Two features of the table deserve comment. The bridge runs in both directions: genetics did not merely inherit its explanations from cell biology, but discovered many of the cell's components first as genes (the *cdc* genes of the cell cycle, the *sec* genes of secretion, the *ced* genes of **apoptosis**, all found by screens of the kind in [7.4.19](/7.4.19)), and the chromosome theory itself was proven by genetic exceptions (Bridges' **nondisjunction**, [7.4.6](/7.4.6)) before the cytology could show it. And the same genetic tools serve both neighbors: mosaics and cell-autonomy tests (7.4.9, 7.4.20) answer questions of cell biology inside a developing animal, and the screens that found the segmentation genes are the screens of this course, while their mechanisms are the subject of [7.5](/7.5).

## 26.5. Is Genetics Finished?

A common view of the subject, especially among students who meet it after **biochemistry**, molecular and cell biology, has three parts: that genetics needs only elementary mathematics, of the level of a middle-school course; that classical genetics is complete and no longer develops, the living parts having moved into molecular biology and evolutionary biology; and that its structure as a discipline will therefore not change, which makes it the easiest of the biological subjects to learn. Having worked through the course, we can examine each part against its contents. Each is partly right, and the parts that are right are worth stating precisely.

### 26.5.1. Is the Mathematics Elementary?

The rules of transmission are indeed elementary. Mendelian ratios, modified dihybrid ratios, X-linked crosses and the risk calculations of most pedigree problems use fractions, the product and sum rules and, at most, conditioning on an observation (Formulas 2.4.1, 4.2.1, Algorithm 7.3.1). The many-chapter structure rests on one number, the probability $1/2$ that a heterozygote transmits each allele (26.1.2). Compared with the hundreds of distinct molecular facts that biochemistry or cell biology asks one to learn, this economy is real, and it is what makes genetics problems feel like puzzles rather than recall.

The mathematics needed to infer the rules from data, and to follow them over many generations, is not elementary. The course used:

| Mathematics | Where it was needed |
|---|---|
| Poisson processes | **mapping functions** (Formula 8.5.1), tetrad frequencies (Formula 9.2.3), inversion products (Formula 15.4.1), assembly gaps (Formula 14.2.1), screens (Formula 19.5.1) |
| Likelihood, maximum likelihood, LOD | $r$ from an $\mathrm{F}_2$ (Formula 8.6.3), LOD scores with unknown phase (Formula 14.9.2), EM for ABO (Algorithm 22.2.2), interval mapping (Algorithm 25.1.1) |
| **Bayesian inference** | risk revision (Algorithm 7.4.1), the LOD 3 threshold (Proposition 14.9.1), fine-mapping (Formula 25.4.1) |
| Branching processes and heavy tails | the **Luria–Delbrück distribution** (Formula 12.4.1) |
| Nonlinear recursions and differential equations | selection, drive and endosymbiont spread (Theorem 23.3.1, Formulas 17.6.2, 11.6.2); **transposon** copy number (Formula 17.6.1) |
| Markov chains and diffusion | Wright–Fisher drift (Definition 23.5.1), the fixation probability (Theorem 23.6.1), epialleles (Formula 18.7.1) |
| Variance components, regression, mixed models | heritability (Theorem 24.3.1, Formulas 24.4.1, 24.4.2), stratification and **SNP heritability** (Definitions 25.3.3, 25.5.1) |
| Multiple testing and high-dimensional prediction | genome-wide significance (Formula 25.3.2), GWAS power (Formula 25.3.3), **polygenic scores** (Formula 25.6.1) |

![Four results of the course that need more than fractions, each computed from its own formula. A: a Poisson process of crossovers bends the additive relation r = d into the Haldane and Kosambi mapping functions (Formulas 8.5.1, 8.5.2), which saturate at r = 1/2. B: the Luria–Delbrück distribution (Formula 12.4.1): resistant mutants in 4000 simulated cultures grown from 10³ to 10⁹ cells with on average three mutations each, against the Poisson distribution with the same mean that induced mutation would give; random mutation during growth produces cultures with none (e⁻³ ≈ 5 %) and rare "jackpots" with hundreds of thousands, so that the variance exceeds the mean by four orders of magnitude. C: Kimura's fixation probability (Theorem 23.6.1) for a new mutation, relative to the neutral value 1/2N, against S = 4N_e s: for |S| below about 1 (shaded) selection is almost invisible to drift, and for large S the probability approaches 2s. D: the expected accuracy of a polygenic score (Formula 25.6.1) against GWAS sample size for three combinations of SNP heritability and number of effective segments; the score approaches its ceiling h² (dotted) only when N greatly exceeds M_e/h²](./plots/beyond-fractions.py)

The correct statement is therefore that the rules of transmission are simple and the inference of rules from data is not. This is not a peculiarity of genetics: the laws of mechanics can be stated in a line, while measuring a planet's orbit from noisy observations required Gauss to invent least squares. What gives genetics its reputation for simplicity is that its textbook problems mostly ask for predictions from known rules (from parents to offspring), whereas research mostly asks for the reverse (from offspring to rules), and the reverse problem is statistical.

### 26.5.2. Has Classical Genetics Stopped Developing?

Part of this claim is right. The Mendel–Morgan framework, completed by the chromosome theory, linkage maps and the synthesis with population genetics by the 1930s (26.3.2), has not been overturned, and no later discovery has required a new law of transmission. The apparent exceptions of the course were absorbed into it rather than replacing it: organellar and **maternal inheritance** (7.4.11) are Mendelian rules applied to other genomes or to the mother's genotype, **meiotic drive** (Definition 17.6.2) is a measurable change of the parameter $1/2$, imprinting (Definition 18.2.1) changes expression but not transmission (Proposition 18.2.1), and transgenerational effects must survive a counting argument before they count as inheritance (Formula 18.6.1). It is also true that much of current research on genes is carried out under the names of molecular biology, genomics and evolutionary biology.

The other part does not survive inspection, because the division between classical and molecular genetics has largely dissolved: the classical concepts are the working language of current research, applied at a scale that was unimaginable when they were introduced. Each item below is an active field in which the course's classical tools are the method.

- Association and fine-mapping at biobank scale. GWAS is linkage disequilibrium (Theorem 22.3.1) and a χ² test (Formula 25.3.1) applied to millions of people; resolving signals to causal variants (Formula 25.4.1) and to genes (the *FTO* locus acting through *IRX3* and *IRX5*, 7.4.25) is an unsolved problem for most loci.
- Polygenic prediction and its portability. The accuracy of polygenic scores (Formula 25.6.1) falls about twofold in East Asian and four- to fivefold in African-ancestry samples relative to European ones, because LD and allele frequencies differ; this is a problem of population genetics (7.4.22) and of equity, and it is being addressed by diverse biobanks.
- Rare variants and **missing heritability**. **Exome sequencing** of hundreds of thousands of people tests rare loss-of-function variants by **burden tests** (Definition 25.5.2) and estimates their contribution to heritability, which SNP heritability (Definition 25.5.1) leaves out.
- Somatic genetics. Every tissue is a mosaic of clones that carry their own mutations; **mutational signatures** (Definition 21.1.1) read the history of mutagenic processes in a tumor, and clonal expansions of mutant blood stem cells, detectable in about one in ten people over 70, raise the risk of **leukemia** and of cardiovascular disease. Mosaicism (7.4.9, 7.4.16) is no longer a curiosity but a property of every body.
- Genome-scale forward and reverse genetics. Pooled CRISPR screens test every gene in one experiment (Formula 19.5.2), and single-cell readouts of such screens (Perturb-seq) measure the **transcriptome** of each perturbed cell. Saturation **genome editing** classifies nearly every possible substitution in a gene such as *BRCA1* before it is ever seen in a patient (7.4.19, 7.4.21): an allelic series at base-pair resolution, the logic of Muller's classes (Definition 12.3.2) applied to thousands of alleles.
- Genetic interaction maps. In budding yeast about 23 million double mutants have been scored for growth (Costanzo and colleagues 2016), mapping close to a million negative and positive interactions; the measure is the multiplicative epistasis of Formula 4.3.1, and the map groups genes into pathways and complexes much as Algorithm 4.4.1 groups mutations into genes.
- Recombination and meiotic drive. The placement of crossovers by PRDM9 (7.4.8), its rapid evolution and its role in hybrid sterility, and the frequency of drivers in natural populations (7.4.17) are studied with the same tetrad and transmission-ratio arithmetic as in 7.4.9 and Formula 19.6.1.
- **Transgenerational epigenetic inheritance**. Whether acquired states are transmitted beyond the first unexposed generation in mammals is an open question whose answer depends on the experimental design defined by Formula 18.6.1; in plants and nematodes such inheritance is established (7.4.18).
- Engineered drive. Homing elements with CRISPR nucleases (Definition 17.6.3) spread by biased transmission and are being developed to suppress malaria mosquitoes; their dynamics, including the evolution of resistance alleles, are those of Formula 19.6.1.
- Genomes and history. Telomere-to-telomere assemblies and **pangenomes** (Definition 14.2.2) reveal the structural variation that a single reference hid; ancient DNA (7.4.14) and the genealogies of 7.4.23 reconstruct the movements and admixture of human populations.

None of these fields is "classical genetics" in the sense of crosses between pea plants, but each would be unintelligible without segregation, linkage, epistasis, allele frequencies and variance components. In this sense the classical theory has not stopped developing; it has become infrastructure.

### 26.5.3. Will the Framework Stay the Same?

The core is as stable as classical mechanics is in physics: the laws of transmission, the chromosome theory and the population-genetic recursions will be taught in the same form in fifty years. What changes is the set of questions the framework is asked to answer, and with it the shape of the discipline. Classical genetics asked whether a trait was genetic and where its gene was; its success was measured by a LOD score passing 3 or a complementation group being defined. Current genetics asks how large each effect is, how effects combine across thousands of loci and with the environment, and how well they predict the phenotype of an individual. The relevant results of the course are of that kind: heritability describes a population, not an individual (§24.8); most of the heritability of complex traits is spread over so many loci of small effect that a single-gene picture fails (7.4.25); a polygenic score explains a fraction of variance that depends on **sample size** and ancestry (Formula 25.6.1); and the gene, defined operationally by the **cis–trans test** (Definition 13.1.2), turns out at many GWAS loci to act through distant regulatory variants. The concepts that organize the field, the gene, the allele and the effect, have been sharpened and in places revised, even though the rules that connect them have not.

The balanced verdict is that the common view captures something real and misplaces its boundary. Transmission genetics is mathematically light and conceptually closed, and for a student it may well be the most economical of the biological subjects: a few principles explain a very large range of phenomena. But that economy belongs to the first half of the course. The genetics of populations, of quantitative traits, of somatic cells and of whole genomes is statistical, open and changing quickly, and it is where most of the discipline's current work lies.

## 26.6. Models and Diseases

### 26.6.1. An Index of the Quantitative Models

The models of the course that describe a process in time or space, as distinct from the counting formulas of 26.1, are collected below with their key prediction.

| Model | Equation | Parameters | Prediction | Chapter |
|---|---|---|---|---|
| Blending inheritance | $\sigma_t^2 = \sigma_0^2/2^t$ (Formula 2.1.1) | initial variance | variation vanishes; refuted by its persistence | [7.4.2](/7.4.2) |
| Flux through a pathway | $J = D/\sum 1/(k_iE_i)$ (Formula 3.2.1) | **enzyme** activities | **null alleles** are recessive | [7.4.3](/7.4.3) |
| Temperature-dependent sex | logistic in $T$ (Formula 6.1.2) | pivotal temperature, slope | sex ratio as a reaction norm | [7.4.6](/7.4.6) |
| Crossovers along a chromosome | Poisson; gamma renewal (Formulas 8.5.1, 8.5.2; 8.5.3) | map length, interference $\nu$ | $r \le 1/2$; coincidence below 1 | [7.4.8](/7.4.8) |
| **Conjugation** | transfer gradient $\mathrm{e}^{-\lambda x}$ (Formula 10.4.1) | breakage rate | map in minutes | [7.4.10](/7.4.10) |
| Heteroplasmy | binomial sampling (Formula 11.4.1) | bottleneck $N$ | variance rises to $h_0(1-h_0)$ | [7.4.11](/7.4.11) |
| *Wolbachia* spread | Eq. (11.2) | fecundity cost, CI strength | threshold $s_{\mathrm{f}}/s_{\mathrm{h}}$ | [7.4.11](/7.4.11) |
| Mutation during growth | Luria–Delbrück (Formula 12.4.1) | $m = \mu N_t$ | jackpots; $\mathbb{P}(0) = \mathrm{e}^{-m}$ | [7.4.12](/7.4.12) |
| Huntington onset | Formula 12.6.1 | CAG repeat length | onset falls exponentially with length | [7.4.12](/7.4.12) |
| Maternal age and **trisomy** 21 | Formula 16.2.1 | maternal age | risk from 1/1500 at 20 to 1/35 at 45 | [7.4.16](/7.4.16) |
| Transposon copy number | $\dot n = n(u - v - a - bn)$ (Formula 17.6.1) | **transposition**, excision, cost | equilibrium $n^*$ | [7.4.17](/7.4.17) |
| Meiotic drive | Formula 17.6.2, Eq. (19.4) | transmission ratio, **homozygote** fitness | polymorphism $p^* = 2k - 1$ | [7.4.17](/7.4.17), [7.4.19](/7.4.19) |
| Epiallele switching | Markov chain, Eq. (18.1) | switching rates $\alpha, \beta$ | equilibrium $\beta/(\alpha+\beta)$ | [7.4.18](/7.4.18) |
| Two-hit tumorigenesis | Eqs. (21.1), (21.2) | cells at risk, mutation rate | hereditary $\propto t$, sporadic $\propto t^2$ | [7.4.21](/7.4.21) |
| Multistage carcinogenesis | log–log incidence (21.1.2) | number of steps $k$ | slope $k - 1$ | [7.4.21](/7.4.21) |
| Selection, mutation, migration | Theorem 23.3.1, Formulas 23.1.1, 23.2.1 | $s$, $h$, $\mu$, $m$ | equilibria and their time scales | [7.4.23](/7.4.23) |
| Wright–Fisher drift | Definition 23.5.1, Theorem 23.5.1 | $N_e$ | **loss of heterozygosity** $1/2N_e$ per generation | [7.4.23](/7.4.23) |
| Drift with selection | Theorem 23.6.1 | $N_es$ | effective neutrality for $\lvert 4N_es\rvert \lesssim 1$ | [7.4.23](/7.4.23) |
| Response to selection | Theorem 24.5.1 | $h^2$, $S$ | $R = h^2S$ per generation | [7.4.24](/7.4.24) |
| Liability threshold | Formula 24.6.1 | prevalence, threshold | risk falls steeply with relatedness | [7.4.24](/7.4.24) |
| Polygenic prediction | Formula 25.6.1 | $h^2$, $M_e$, $N$ | accuracy saturates at $h^2$ | [7.4.25](/7.4.25) |

### 26.6.2. Diseases by Genetic Mechanism

| Mechanism | Examples (gene or region) | Genetic signature | Chapter |
|---|---|---|---|
| Autosomal recessive, loss of function | cystic fibrosis (*CFTR*), **phenylketonuria**, sickle-cell disease ($Hb\beta^S$), **alkaptonuria** | affected children of carrier parents, risk $1/4$; carriers $\approx 2\sqrt{Q}$; **consanguinity** raises risk $\approx 1 + F/q$ | [7.4.3](/7.4.3), [7.4.7](/7.4.7), [7.4.22](/7.4.22) |
| **Heterozygote advantage** | sickle-cell trait and malaria | stable $\hat q = s_1/(s_1+s_2) \approx 0.12$ | [7.4.23](/7.4.23) |
| Autosomal dominant, gain of function or dominant negative | achondroplasia (*FGFR3* G380R), Huntington disease (*HTT*), **collagen** and **p53** dominant negatives | every affected person has an affected parent or a new mutation; **paternal age effect** | [7.4.12](/7.4.12) |
| **Haploinsufficiency** and genomic disorders | Charcot–Marie–Tooth 1A and HNPP (17p12), Williams syndrome (7q11.23), 22q11.2 deletion | recurrent breakpoints from **non-allelic homologous recombination** | [7.4.3](/7.4.3), [7.4.15](/7.4.15) |
| X-linked recessive | Duchenne muscular dystrophy (*DMD*), hemophilia A (*F8*), red–green color vision defects (Xq28) | affected males, carrier mothers; one third new mutations for lethals; **manifesting heterozygotes** | [7.4.6](/7.4.6), [7.4.7](/7.4.7), [7.4.13](/7.4.13) |
| Repeat expansion | fragile X syndrome (*FMR1*, CGG), Huntington disease (CAG), myotonic dystrophy type 1 | **anticipation**; parent-of-origin bias of expansion; **premutation** | [7.4.12](/7.4.12) |
| Imprinting | Prader–Willi and **Angelman syndromes** (15q11–q13), Beckwith–Wiedemann and Silver–Russell syndromes (11p15) | deletion, **uniparental disomy**, imprinting defect; expression by parental origin | [7.4.18](/7.4.18) |
| Mitochondrial | LHON (homoplasmic), MERRF, MELAS, NARP and Leigh syndrome (heteroplasmic) | maternal transmission; **threshold effect**; recurrence by heteroplasmy distribution | [7.4.11](/7.4.11) |
| Chromosomal: number | Down syndrome (trisomy 21), Turner (45,X), Klinefelter (47,XXY) | maternal age; MI errors; tolerance of sex-chromosome aneuploidy by X inactivation | [7.4.16](/7.4.16), [7.4.6](/7.4.6) |
| Chromosomal: structure | translocation Down syndrome (**Robertsonian translocation**), hemophilia A inversions | familial recurrence about $10$–$15\,\%$ through a carrier mother | [7.4.15](/7.4.15) |
| Hereditary cancer | retinoblastoma (*RB1*), Li–Fraumeni (*TP53*), *BRCA1*/*BRCA2*, Lynch syndrome (mismatch-repair genes) | recessive in the cell, dominant in the family; **two-hit hypothesis**; **synthetic lethality** with PARP inhibitors | [7.4.21](/7.4.21) |
| Multifactorial threshold traits | pyloric stenosis, cleft lip, schizophrenia, **type 1 diabetes** | risk falls steeply with relatedness; sex difference in thresholds | [7.4.24](/7.4.24) |
| Polygenic common disease | coronary artery disease, breast cancer, height as a model trait | thousands of loci of small effect; polygenic scores for risk stratification | [7.4.25](/7.4.25) |

## Summary

- Toolbox (26.1): every calculation of the course in one table, from the product rule (Formula 2.4.1) to polygenic scores (Formula 25.6.1); four recurring ideas, independent transmission with probability $1/2$, Poisson zero terms, likelihood, and recursions over generations; combined problems join chapters (Examples 26.1.1, 26.1.2).
- Mode of inheritance (26.2): reciprocal crosses first, then the number of parts of the ratio, a testcross for linkage, and for differing reciprocal crosses the sex of the offspring, the mother, the mother's genotype or the parent of origin (Algorithm 26.2.1); pedigrees follow Algorithm 7.2.1.
- Inference (26.3): isolation, segregation, complementation, mapping, interaction, cloning and function; forward and reverse genetics meet at rescue; four lineages of method in which each new technology was absorbed into an existing logic, while the questions moved from the presence of effects to their size and distribution.
- Cell to organism (26.4): **meiosis** explains transmission and maps, chromosome structure explains rearrangements and aneuploidy, **chromatin** explains **dosage compensation** and imprinting, organelles explain maternal inheritance, the cell cycle explains the two hits of cancer, and mosaics, screens and **epistasis analysis** give development its tools.
- Is genetics finished? (26.5): the rules of transmission are elementary, their inference from data is statistical (Poisson processes, likelihood, diffusion, variance components, high-dimensional prediction); the Mendel–Morgan framework is stable and has absorbed every exception, but its concepts drive active fields from biobank GWAS and somatic mosaicism to saturation editing and genetic interaction maps; the framework stays, the questions shift from "whether and where" to "how much, how combined and how predictive".
- Models and diseases (26.6): an index of the dynamic and stochastic models and a table of diseases by mechanism, from recessive loss of function to polygenic common disease.

## Questions

1. Show that the $\mathrm{F}_2$ counts 182 : 61 : 77 fit a $9:3:4$ ratio, name the gene interaction, and give the expected testcross ratio.

   **Answer** Expected counts for $n = 320$ are $180, 60, 80$. $\chi^2 = 2^2/180 + 1^2/60 + 3^2/80 = 0.022 + 0.017 + 0.113 = 0.15$ with 2 df, $p = 0.93$ (Formula 2.5.1): an excellent fit. $9:3:4 = 9 : 3 : (3 + 1)$ merges $aaB\_$ and $aabb$, so $aa$ masks the second locus: **recessive epistasis** (Formula 4.2.1). A testcross $AaBb \times aabb$ gives $1\,AaBb : 1\,Aabb : 1\,aaBb : 1\,aabb$, i.e. $1:1:2$.

2. A testcross gives $r = 0.30$ between two loci. Convert it to map distance with the Haldane and the Kosambi functions and explain why the two differ.

   **Answer** Haldane: $d = -\tfrac12\ln(1 - 0.6) = 0.458\,\mathrm{M} = 45.8\,\mathrm{cM}$. Kosambi: $d = \tfrac14\ln(1.6/0.4) = \tfrac14\ln 4 = 0.347\,\mathrm{M} = 34.7\,\mathrm{cM}$ (Formulas 8.5.1, 8.5.2). Haldane assumes no interference, so more undetected **double crossovers** are added back; Kosambi assumes interference that suppresses nearby double crossovers, so less correction is needed. For short intervals both give $d \approx r$.

3. In 100 unordered yeast tetrads there are 70 PD, 2 NPD and 28 T. Are the loci linked? Estimate the recombination frequency and the map distance.

   **Answer** PD greatly exceeds NPD, so the loci are linked (unlinked loci give PD = NPD). $r = (\mathrm{NPD} + \tfrac12\mathrm{T})/n = (2 + 14)/100 = 0.16$ (Formula 9.2.1). Perkins: $d = 50(28 + 12)/100 = 20\,\mathrm{cM}$ (Formula 9.2.2), larger than $100r = 16$ because NPD reveal four-strand doubles; the Haldane conversion of $r = 0.16$ gives $19.3\,\mathrm{cM}$, close to Perkins.

4. A family has 10 informative meioses of known phase, one of them recombinant. Compute the LOD score at $\theta = 0.1$ and the number of such families needed for a LOD of 3.

   **Answer** $Z(0.1) = \log_{10}[0.1 \cdot 0.9^9 \cdot 2^{10}] = \log_{10}(39.7) = 1.60$ (Formula 14.9.1); this is also the maximum, at $\hat\theta = 1/10$. LOD scores of independent families add, so two such families give $3.20 \ge 3$. By Proposition 14.9.1, $Z = 3$ corresponds to a posterior probability of linkage of about $0.95$ because the prior is about $0.05$.

5. In Example 26.1.1, suppose the woman has three unaffected sons instead of two. What is her carrier probability, and the risk for a fourth son?

   **Answer** Prior $1/3$; joint for carrier $\tfrac13 \cdot \tfrac18 = \tfrac1{24}$, for noncarrier $\tfrac23 = \tfrac{16}{24}$; posterior $1/17 = 0.059$ (Algorithm 7.4.1). Risk for the next son $1/34 \approx 2.9\,\%$.

6. Cystic fibrosis affects about 1 in 2 500 births in a population in **Hardy–Weinberg equilibrium**. What is the risk that the healthy sibling of a patient has an affected child with an unrelated partner from the same population?

   **Answer** $q = \sqrt{1/2500} = 0.02$, carrier frequency $2pq = 0.0392$ (Formula 22.2.1). The healthy sibling is a carrier with probability $2/3$ (Proposition 7.3.1). Risk $= \tfrac23 \times 0.0392 \times \tfrac14 = 0.0065$, about $1/153$.

7. A recessive disease allele has frequency $q = 0.01$. How much more often is the child of first cousins affected than a child of unrelated parents?

   **Answer** $F = 1/16$ (Formula 7.5.1). $\mathbb{P}(aa) = q^2 + Fq(1 - q) = 0.0001 + 0.0625 \times 0.0099 = 0.00072$ (Formula 7.5.2), against $q^2 = 0.0001$: about $7.2$ times, close to the approximation $1 + F/q = 7.25$. The rarer the allele, the larger the ratio, which is why rare recessive diseases concentrate in consanguineous families.

8. In 50 parallel cultures each grown to $2\times10^8$ cells, 30 contain no resistant mutants. Estimate the mutation rate, and explain why the mean number of mutants per culture would be a poor estimator.

   **Answer** By the $p_0$ method, $\mathrm{e}^{-m} = 30/50$, so $m = -\ln 0.6 = 0.51$ mutations per culture and $\mu = m/N_t = 2.6\times10^{-9}$ per cell division (Formula 12.4.1, Algorithm 12.4.1). The mean is dominated by rare jackpots from early mutations, with variance far exceeding the mean (figure in 26.5.1, panel B), so it is unstable from sample to sample.

9. A new advantageous mutation with additive **selection coefficient** $s = 0.01$ arises in a population with $N = N_e = 10^4$. What is its probability of fixation, how does this compare with a neutral mutation, and roughly how many generations does selection need to take it from frequency $0.01$ to $0.99$?

   **Answer** With $p = 1/2N$, $u = (1 - \mathrm{e}^{-2s})/(1 - \mathrm{e}^{-400}) \approx 0.0198 \approx 2s$ (Theorem 23.6.1): about 400 times the neutral $1/2N = 5\times10^{-5}$, yet 98 % of such mutations are still lost by drift. Under genic selection $t \approx \tfrac1s\ln(p_tq_0/p_0q_t) = 100 \ln 9801 \approx 920$ generations (Formula 23.3.2).

10. A trait has $h^2 = 0.4$ and $\sigma_P = 5$. Breeders select the top 10 % as parents. Predict the response per generation.

    **Answer** For truncation at $p = 0.1$, $z = 1.28$ and $i = \varphi(z)/p = 1.755$ (Definition 24.5.2). $R = ih^2\sigma_P = 1.755 \times 0.4 \times 5 = 3.5$ units per generation (Formula 24.5.1, Theorem 24.5.1), which is $0.7$ phenotypic **standard deviations**.

11. A SNP with allele frequency $0.3$ changes a standardized trait by $0.05$ standard deviations per allele. How many individuals does a GWAS need for 80 % power at $p < 5\times10^{-8}$? With $N = 5\times10^5$, what accuracy could a polygenic score reach for a trait with $h^2 = 0.5$ and $M_e = 60\,000$?

    **Answer** Variance explained $2pq\beta^2 = 2(0.3)(0.7)(0.0025) = 0.00105$. Power 80 % at $5\times10^{-8}$ needs a noncentrality $\lambda \approx 39.6$, so $N = 39.6/0.00105 \approx 37\,700$ (Formula 25.3.3). Polygenic score: $R^2 = 0.5/(1 + 60\,000/250\,000) = 0.5/1.24 = 0.40$ (Formula 25.6.1), in a sample of the same ancestry; less in others.

12. Using Algorithm 26.2.1, distinguish organellar inheritance, a maternal effect and imprinting by crosses alone. Which generation is decisive for each?

    **Answer** Organellar: the phenotype follows the mother in every generation, including after repeated backcrossing of daughters to males of the other line, which replaces the nuclear genome (Algorithm 11.1.1); every generation is informative, and nuclear markers segregate normally while the trait does not. Maternal effect: offspring have the phenotype dictated by their mother's genotype, so the $\mathrm{F}_1$ of a $dd$ mother are all mutant whatever their own genotype, and the $\mathrm{F}_2$ (from $Dd$ mothers) are all wild type; the $\mathrm{F}_3$ is decisive, with broods uniform within each brood but segregating $3:1$ among the broods of different $\mathrm{F}_2$ mothers (Formula 11.6.1). Imprinting: the phenotype depends on which parent transmitted a nuclear allele, so it reverses when the allele passes through the other sex; the decisive test is a comparison of heterozygous offspring of carrier fathers and carrier mothers (Algorithm 18.2.1).

13. Choose two active research areas from 26.5.2 and identify, for each, the classical concept and the numbered result of the course on which it depends.

    **Answer** Example answers. (a) GWAS depends on linkage disequilibrium: a **tag SNP** is associated with a trait only because $D$ between it and the causal variant has not decayed, $D_t = (1 - r)^tD_0$ (Theorem 22.3.1), and its power is reduced by the factor $r^2$ (Formula 25.2.1). (b) Genetic interaction maps depend on epistasis in the quantitative sense: the deviation of a double-mutant fitness from the multiplicative expectation, $\varepsilon_{ab} = W_{ab} - W_aW_b$ (Formula 4.3.1), and on the logic of grouping by shared patterns, as complementation groups are defined in Algorithm 4.4.1. (c) Engineered gene drives depend on transmission ratio distortion (Formula 19.6.1) and homing (Definition 17.6.3).

14. (Open question) Is the statement "the rules of transmission are simple, their inference is statistical" also true of other fields you know? Give one example from genetics and one from another science.

    **Answer** Points to cover: in genetics, Mendel's rule is one sentence, but estimating a recombination frequency from an $\mathrm{F}_2$ with dominance requires solving a **likelihood equation** (Formula 8.6.3), and a LOD score requires a prior to interpret (Proposition 14.9.1). In other sciences: Newton's laws are simple, while orbit determination from observations required least squares; the law of radioactive decay is a single exponential, while dating a rock from isotope counts is a problem of statistical estimation. The general point is that forward problems (from rules to data) are often simpler than inverse problems (from data to rules), and research consists mostly of inverse problems.
