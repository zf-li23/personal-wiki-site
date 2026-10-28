---
title: Gene Interaction and Epistasis
description: Two genes acting on one trait; new phenotypes; epistasis and its six classical F2 ratios with their pathway models and testcross ratios; suppressors, modifiers, redundancy and quantitative epistasis; genetic heterogeneity and the complementation test; deciding between one-gene and two-gene hypotheses by χ² tests and breeding tests; additive polygenes and the approach to continuous variation; dog coat color as a worked system; and a systematic algorithm for modified dihybrid and trihybrid ratios, including lethality.
---

Most traits are built by several **genes**. The pigment of a flower is made by a pathway of **enzymes**, a wing by a network of signaling **proteins** and **transcription** factors, and a **mutation** in any of the genes can change the **phenotype**. When two such genes segregate in one cross, the **law of independent assortment** still holds for the **genotypes**, which still come in the proportions $9\,A\_B\_ : 3\,A\_bb : 3\,aaB\_ : 1\,aabb$; but the phenotypes of the four classes need not be distinct, and the familiar 9:3:3:1 collapses into ratios such as 9:3:4, 9:7, 12:3:1, 13:3 or 15:1. The ratio is therefore a clue to how the two gene products work together, and reading it backwards, from the numbers to a pathway, is one of the oldest forms of genetic inference. It remains the logic of epistasis analysis in developmental genetics (7.4.20) and of the genome-wide genetic-interaction maps of systems biology ([7.9](/7.9)).

This chapter builds on the probability rules of 7.4.2 and the allelic interactions of 7.4.3. It also introduces the complementation test, which decides whether two **recessive** mutations with the same phenotype are in the same gene, and the additive model of many genes, which connects Mendelian genes with continuous variation (developed in 7.4.24). It ends with a systematic procedure for the "ratio puzzles" that are a staple of genetics problems.

## 4.1. Two Genes, One Trait

### 4.1.1. New Phenotypes from Gene Interaction

The simplest interaction leaves all four genotypic classes distinguishable but gives some of them **phenotypes** that neither parent had.

**Example 4.1.1 (Lentil seed coat)** **True-breeding** tan and gray lentils give a brown $\mathrm{F}_1$; the $\mathrm{F}_2$ has brown, tan, gray and green seeds in the ratio 9:3:3:1. The ratio shows two independently assorting **genes**, and the phenotypes suggest the model: $A$ is required for a tan pigment and $B$ for a gray pigment, made in independent pathways; $A\_B\_$ has both pigments and looks brown, $A\_bb$ tan, $aaB\_$ gray, and $aabb$ has neither, so the green of the chlorophyll beneath shows through. Brown and green are new phenotypes, produced by the combination of **alleles** at two **loci**.

**Example 4.1.2 (Comb shape in chickens)** Bateson and Punnett (1905) crossed rose-combed and pea-combed chickens. The $\mathrm{F}_1$ had a new walnut comb, and the $\mathrm{F}_2$ had walnut, rose, pea and single combs in 9:3:3:1: $R\_P\_$ walnut, $R\_pp$ rose, $rrP\_$ pea, $rrpp$ single. This was the first demonstration that two Mendelian genes can determine one trait. The *rose* allele is a large inversion that places the **transcription** factor gene *MNR2* under new regulatory control, and *pea* is a duplication in an **intron** of *SOX5* that causes its ectopic expression; walnut combs result when both are present.

## 4.2. Epistasis

### 4.2.1. Definitions

**Definition 4.2.1 (Epistasis)** **Epistasis** is an interaction between the **alleles** of different **genes** in which the **genotype** at one **locus** masks or modifies the phenotypic effect of the genotype at another locus. The gene whose alleles do the masking is epistatic to the other, which is hypostatic.

Epistasis is the inter-locus counterpart of **dominance**, which is an interaction between alleles of the same locus (7.4.3); the term is used in two senses that should be kept apart. In classical (Mendelian) genetics it means masking of one gene's **phenotype** by another's, which merges the four $\mathrm{F}_2$ classes. In quantitative and statistical genetics it means any departure of the joint effect of two loci from a specified (usually additive or multiplicative) model (4.3.3, 7.4.24).

**Definition 4.2.2 (Recessive and Dominant Epistasis)** In **recessive epistasis**, homozygosity for a **recessive** allele at one locus ($aa$) masks the phenotypic effects of the alleles at a second locus. In **dominant epistasis**, a dominant allele at one locus ($A\_$) masks the effects of the alleles at a second locus.

**Definition 4.2.3 (Complementary and Duplicate Gene Action)** Two genes show **complementary gene action** (reciprocal recessive epistasis, duplicate recessive epistasis) when a dominant allele at both loci is required for a phenotype ($A\_B\_$), and homozygosity for the recessive allele at either locus gives the alternative phenotype; the $\mathrm{F}_2$ ratio is 9:7. Two genes are **duplicate genes** (duplicate dominant epistasis, genetic redundancy) when a dominant allele at either locus is sufficient for a phenotype, which fails only in the double recessive $aabb$; the $\mathrm{F}_2$ ratio is 15:1.

### 4.2.2. The Six Classical Ratios and Their Pathways

**Formula 4.2.1 (Modified Dihybrid Ratios)** If two unlinked loci each have a completely dominant and a recessive allele, the $\mathrm{F}_2$ of $AaBb \times AaBb$ always contains the genotypic classes $9\,A\_B\_ : 3\,A\_bb : 3\,aaB\_ : 1\,aabb$, and the **testcross** $AaBb \times aabb$ the classes $1\,AaBb : 1\,Aabb : 1\,aaBb : 1\,aabb$. Each type of interaction assigns phenotypes to these classes; the phenotypic ratio is obtained by adding the classes with the same phenotype.

| Interaction | Phenotype classes ($A\_B\_$, $A\_bb$, $aaB\_$, $aabb$) | $\mathrm{F}_2$ ratio | Testcross ratio | Pathway model | Example |
|---|---|---|---|---|---|
| none (new phenotypes) | 1, 2, 3, 4 | 9:3:3:1 | 1:1:1:1 | two independent pathways | lentil seed coat, chicken comb |
| recessive epistasis ($aa$ epistatic to $B$, $b$) | 1, 2, 3, 3 | 9:3:4 | 1:1:2 | $A$ acts before $B$ in one pathway: $aa$ blocks the first step, and $B$ versus $b$ only matters after it | Labrador coat color, Bombay phenotype |
| complementary genes | 1, 2, 2, 2 | 9:7 | 1:3 | two steps in series, each needing a functional enzyme | sweet pea flower color, white clover cyanogenesis |
| dominant epistasis ($A$ epistatic to $B$, $b$) | 1, 1, 2, 3 | 12:3:1 | 2:1:1 | $A$ blocks or masks the pathway in which $B$ and $b$ act | summer squash fruit color |
| dominant suppression (dominant epistasis II) | 1, 1, 2, 1 | 13:3 | 3:1 | $A$ suppresses the phenotype that $B$ produces; color needs $aaB\_$ | white leghorn × white wyandotte chickens, silkworm cocoon color |
| duplicate genes (redundancy) | 1, 1, 1, 2 | 15:1 | 3:1 | either gene suffices: two parallel pathways or two copies of one function | shepherd's purse seed capsule, maize leaf development |
| duplicate genes with cumulative effect | 1, 2, 2, 3 | 9:6:1 | 1:2:1 | the products of the two genes add up | squash fruit shape |

![The epistatic ratios as colored Punnett squares. Each panel is the F2 of AaBb × AaBb (gametes AB, Ab, aB, ab along both sides), with the 16 cells colored by phenotype under one kind of gene interaction; beneath each square is the pathway model that produces the coloring. Recessive epistasis 9:3:4: aa blocks the first step, so B and b are invisible. Complementary genes 9:7: both steps are needed. Dominant epistasis 12:3:1: A masks the pathway. Dominant suppression 13:3: A suppresses the color made by B. Duplicate genes 15:1: either gene suffices. Cumulative duplicate genes 9:6:1: the two products add](./plots/epistasis-squares.py)

**Example 4.2.1 (Recessive epistasis: Labrador retrievers)** Labrador retrievers are black, chocolate or yellow. Two genes are involved: *E*, which encodes the melanocortin-1 **receptor** (MC1R) of melanocytes, and *B*, which encodes tyrosinase-related **protein** 1 (TYRP1). With an active receptor ($E\_$), melanocytes make the dark pigment eumelanin, deposited densely in $B\_$ dogs (black) and less densely in $bb$ dogs (chocolate); without it ($ee$), they make only the yellow pigment pheomelanin, whatever the *B* genotype. A cross of two black $BbEe$ dogs gives 9 black ($B\_E\_$) : 3 chocolate ($bbE\_$) : 4 yellow ($B\_ee$ and $bbee$). The $ee$ genotype is epistatic to *B*. A yellow dog's *B* genotype is hidden, but it still shows in the nose and lips, which are black in $B\_ee$ and brown in $bbee$ dogs: whether a gene's effect is masked depends, again, on which phenotype is examined.

**Example 4.2.2 (The Bombay phenotype)** The H **antigen** made by the *FUT1* fucosyltransferase is the **substrate** on which the ABO **enzymes** build the A and B antigens (7.4.3). People **homozygous** for loss-of-function *FUT1* alleles ($hh$) make no H antigen and therefore no A or B antigen; they type as O whatever their ABO genotype. This recessive epistasis was discovered in Bombay (now Mumbai) in 1952. It explains a pedigree that seems to break Mendel's laws: two "type O" parents can have a type A or B child if one parent is $hh\,I^A\_$ or $hh\,I^B\_$. People with the Bombay phenotype have anti-H as well as anti-A and anti-B antibodies and can receive blood only from other Bombay donors.

**Example 4.2.3 (Complementary genes: sweet peas)** Bateson and Punnett crossed two **true-breeding** white-flowered lines of sweet pea (*Lathyrus odoratus*). The $\mathrm{F}_1$ was purple, and the $\mathrm{F}_2$ had 382 purple and 269 white plants, close to 9:7 (expected 366.2 : 284.8). The model: purple anthocyanin is made by two enzymatic steps in series, from a colorless precursor to a colorless intermediate (enzyme A) and from the intermediate to the pigment (enzyme B). A plant lacking either enzyme ($aa\,\_\_$ or $\_\_\,bb$) is white. The two white parents were $AAbb$ and $aaBB$; each supplies the step the other lacks, and the $\mathrm{F}_1$ is $AaBb$. This is the logic of the complementation test (4.4).

**Example 4.2.4 (Dominant epistasis: squash color)** In summer squash, the dominant allele $W$ of one gene prevents pigment deposition and gives white fruit; in $ww$ plants, a second gene gives yellow ($Y\_$) or green ($yy$) fruit. The $\mathrm{F}_2$ of $WwYy$ has 12 white ($W\_\,\_\_$) : 3 yellow ($wwY\_$) : 1 green ($wwyy$).

**Example 4.2.5 (Dominant suppression: chickens)** White leghorn chickens ($IICC$) carry a dominant inhibitor $I$ that prevents pigmentation; white wyandottes ($iicc$) lack the ability to make pigment ($cc$). Their $\mathrm{F}_1$ ($IiCc$) is white, and the $\mathrm{F}_2$ has 13 white : 3 colored, since only $iiC\_$ birds (3/16) are colored. The same 13:3 ratio appears for cocoon color in the silkworm *Bombyx mori*, where a dominant inhibitor $I$ prevents the yellow color produced by $Y$: the $\mathrm{F}_2$ of white $IIyy$ × yellow $iiYY$ has 13 white ($I\_\,\_\_$ and $iiyy$) : 3 yellow ($iiY\_$).

**Example 4.2.6 (Duplicate genes)** In shepherd's purse (*Capsella bursa-pastoris*), seed capsules are triangular if a plant carries a dominant allele of either of two genes and ovoid only in $aabb$: the $\mathrm{F}_2$ ratio is 15:1. The two genes arose by a duplication of the **genome** (the species is tetraploid), and each copy can do the job. In maize, plants that are $aabb$ for two genes that act in parallel to recruit cells into the leaf have thin, abnormal leaves, while one functional copy of either gene suffices.

**Example 4.2.7 (Cumulative duplicate genes)** Summer squash fruit can be disc-shaped, spherical or long. A cross of two true-breeding spherical lines ($AAbb \times aaBB$) gives disc-shaped $\mathrm{F}_1$ and an $\mathrm{F}_2$ of 9 disc ($A\_B\_$) : 6 spherical ($A\_bb$ and $aaB\_$) : 1 long ($aabb$): one active gene gives an intermediate shape and two give the full effect.

**Example 4.2.8 (Complementary genes resolved biochemically: cyanogenesis in white clover)** Many plants of white clover (*Trifolium repens*) release hydrogen cyanide when their leaves are crushed, a defense against herbivores. Two components are needed: cyanogenic glucosides (linamarin and lotaustralin), whose synthesis requires the dominant allele of *Ac*, and the hydrolyzing enzyme linamarase, encoded by the dominant allele of *Li*; the two are kept in different compartments of the cell and meet only when the tissue is damaged. The recessive alleles are deletions of the genes (*ac* lacks the **cytochrome P450** gene *CYP79D15*). Two acyanogenic plants, $Ac/Ac\,li/li$ and $ac/ac\,Li/Li$, give a cyanogenic $\mathrm{F}_1$ and an $\mathrm{F}_2$ of 9 cyanogenic : 7 acyanogenic. Corkill (1942) split the 7 by testing leaf extracts: adding linamarase releases cyanide from $Ac\_\,li/li$ extracts (3/16), adding glucoside releases it from $ac/ac\,Li\_$ extracts (3/16), and neither helps $ac/ac\,li/li$ (1/16). The biochemical tests restore the 9:3:3:1 hidden in 9:7, a direct demonstration that the merged classes of Formula 4.2.1 are distinct genotypes. Frequencies of the two alleles form latitudinal clines in Europe and North America, cyanogenic plants being commoner in warm climates, where herbivores are abundant, and rarer where frost damages leaves and releases cyanide in the plant's own tissue.

### 4.2.3. Why Ratios Reveal Pathways

The pathway models in the table follow from a few principles. If two genes act in sequence in one linear pathway and the phenotype requires the end product, loss of the earlier step makes the later step irrelevant (recessive epistasis, 9:3:4); if loss of either step gives the same phenotype, the two classes merge further (9:7). If the phenotype is produced by either of two parallel pathways, both must be lost (15:1). The order of action can be inferred from which gene is epistatic: in a pathway in which the mutant phenotypes differ (no pigment versus an intermediate color), the double mutant has the phenotype of the **mutation** in the earlier step of a biosynthetic pathway. For regulatory (switch) pathways, in which one gene controls another, the double mutant has the phenotype of the downstream gene, the basis of epistasis analysis in development (7.4.20).

## 4.3. Suppressors, Modifiers and Redundancy

### 4.3.1. Suppressor Mutations

**Definition 4.3.1 (Suppressor Mutation)** A **suppressor mutation** is a **mutation** that reverses, partly or completely, the phenotypic effect of another mutation, restoring a **wild-type** or near-wild-type **phenotype**. An intragenic suppressor lies in the same **gene** as the first mutation (a second-site change that compensates for it); an intergenic suppressor lies in a different gene.

In *Drosophila* the **recessive** **allele** $pd$ makes purple eyes. A recessive allele $su$ of an unlinked gene has no phenotype of its own but suppresses $pd$: $pd/pd;\, su/su$ flies have wild-type red eyes. In the $\mathrm{F}_2$ of $pd/+;\, su/+$ flies, purple appears only in $pd/pd;\, su^+/\_$ (3/16), and the ratio is 13 red : 3 purple, the dominant-suppression ratio of Example 4.2.5 with the roles of **dominant** and recessive exchanged.

Suppressors find interacting **proteins**. If the first mutation changes a **residue** at a binding surface so that the protein can no longer bind its partner, a compensating change in the partner's binding surface can restore binding; such allele-specific suppression is strong evidence that the two proteins contact each other. Suppressor screens in yeast and bacteria identified many interacting proteins, components of the same complex and steps of the same pathway. Nonsense mutations can be suppressed by mutant **tRNAs** that read the **stop codon** ([7.2.19](/7.2.19)), and some suppressors work by increasing the amount of a partly functional protein. The opposite of a suppressor is an **enhancer**, a mutation that makes the phenotype of another more severe; enhancer and suppressor screens in a sensitized background are standard in developmental genetics (7.4.20).

### 4.3.2. Modifiers and Incomplete Dominance in Dihybrid Crosses

**Modifier genes** (**modifier gene**, 7.4.3) change the degree of a phenotype without masking it, and the line between modification and epistasis is a matter of degree. When one or both genes show **incomplete dominance**, more of the nine **genotypes** become distinguishable. If $A$ is incompletely dominant and $B$ completely dominant, the $\mathrm{F}_2$ phenotypes are $(1:2:1) \times (3:1) = 3:6:3:1:2:1$ (six classes); if both are incompletely dominant, all nine genotypes are distinguishable and the ratio is $(1:2:1)^2 = 1:2:1:2:4:2:1:2:1$.

### 4.3.3. Redundancy and Quantitative Epistasis

**Definition 4.3.2 (Genetic Redundancy)** Two genes are **genetically redundant** for a phenotype when the loss of either alone has little or no effect and the loss of both gives a strong phenotype.

Redundancy is common because **genomes** contain duplicated genes (**paralogs**, [7.1.4](/7.1.4)) and alternative pathways. It is one reason why many single knockouts show no visible phenotype (7.4.1). In yeast, about 80 % of the roughly 6 000 genes can be deleted individually without killing the cell, but when nearly all pairs were tested (about 23 million double mutants; Costanzo et al. 2016), about 550 000 showed negative and 350 000 positive interactions, and some thousands of pairs are lethal together. Such a pair shows **synthetic lethality**, a relation now used in **cancer** therapy ([7.3.26](/7.3.26)).

For a measurable phenotype such as growth rate, epistasis can be quantified.

**Formula 4.3.1 (Multiplicative Epistasis)** Let $W_{ab}$, $W_a$, $W_b$ be the fitness (growth rate relative to the wild type, $W_{\text{wt}} = 1$) of a double mutant and of the two single mutants. If the mutations act independently, their effects multiply, and the epistasis score is

$$
\varepsilon_{ab} = W_{ab} - W_a W_b .
$$

$\varepsilon < 0$ (negative or aggravating epistasis) means the double mutant is sicker than expected, synthetic lethality being the extreme ($W_{ab} = 0$ with $W_a, W_b$ near 1); $\varepsilon > 0$ (positive or alleviating epistasis) means it is healthier than expected, as when the two genes act in the same pathway or complex, so that losing the second gene after the first costs nothing more.

**Example 4.3.1** Two yeast deletions grow at $W_a = 0.9$ and $W_b = 0.8$. The multiplicative expectation for the double mutant is $0.72$. If the double mutant grows at $0.30$, $\varepsilon = -0.42$: a strong negative interaction, suggesting the genes act in parallel pathways that buffer each other. If it grows at $0.80$, the same as the sicker single mutant, $\varepsilon = +0.08$, the pattern expected if both genes are needed for the same process: once $b$ is lost, losing $a$ does not matter. Genome-wide maps of $\varepsilon$ group genes into pathways and complexes ([7.9](/7.9)).

## 4.4. Genetic Heterogeneity and the Complementation Test

### 4.4.1. Many Genes, One Phenotype

**Definition 4.4.1 (Genetic Heterogeneity)** A **phenotype** shows **genetic heterogeneity** (**locus** heterogeneity) when **mutations** in any one of several different **genes** can produce it.

Heterogeneity is the rule for phenotypes that depend on a long pathway or a complex structure. Mutations in more than 100 human genes can cause hereditary hearing loss, mostly **recessive**; in dozens can cause retinitis pigmentosa; and an albino mouse may be mutant in any of several genes of melanin synthesis or melanocyte development. Two individuals with the same recessive phenotype may therefore carry mutations in the same gene or in different genes, and a test is needed to tell which.

### 4.4.2. The Complementation Test

**Definition 4.4.2 (Complementation Test)** The **complementation test** asks whether two recessive mutations that produce the same phenotype are in the same gene. Individuals **homozygous** for each mutation are crossed (or, in microorganisms, the two mutant **genomes** are brought together in one cell), and the phenotype of the progeny, which carry one copy of each mutation, is examined:

- if the progeny are **wild type**, the mutations complement each other: each mutant genome supplies the gene function that the other lacks, so the mutations are in different genes;
- if the progeny are mutant, the mutations fail to complement and are in the same gene (they are **alleles**).

The test works because the progeny are trans-heterozygotes. If $m_1$ and $m_2$ are in different genes, the progeny are $m_1/+;\, m_2/+$, **heterozygous** for a recessive mutation at each of two loci, and wild type. If they are in the same gene, the progeny are $m_1/m_2$: both copies of that gene are mutant, and no functional product is made.

![The complementation test. Left: two recessive mutations (red marks) in different genes, a and b, brought together in a trans-heterozygote; each homologue carries a wild-type copy of the gene mutated on the other homologue, so both gene products are made and the phenotype is wild type (complementation). Right: two recessive mutations in the same gene; neither homologue has a functional copy, no product is made and the phenotype is mutant (no complementation)](./plots/complementation-test.py)

**Example 4.4.1 (Hearing loss)** Two people with recessive congenital deafness have children together. If all the children hear normally, the parents are most likely homozygous for mutations in different genes ($aaBB \times AAbb$, children $AaBb$): complementation. If all the children are deaf, both parents are probably homozygous for mutations in the same gene ($aa \times aa$). Pedigrees of both kinds are known; the first kind was how heterogeneity of deafness was recognized before the genes were cloned.

**Definition 4.4.3 (Complementation Group)** A **complementation group** is a set of mutations that fail to complement one another (and complement every mutation outside the set). Each complementation group normally corresponds to one gene.

**Algorithm 4.4.1 (Grouping Mutations by Complementation)**

1. Collect recessive mutations with the same phenotype, each in a homozygous (or **haploid**) strain.
2. Cross every pair and score the progeny: + (wild type: complementation) or − (mutant: no complementation). The diagonal (a mutation with itself) is −.
3. Put two mutations in the same group if their progeny are mutant. Because "fails to complement" is (normally) an equivalence relation, the groups are its equivalence classes; check that the table is consistent (if $m_1$ and $m_2$ fail to complement, and $m_2$ and $m_3$ fail, then $m_1$ and $m_3$ must fail).
4. The number of groups is the minimum number of genes in which mutations produce the phenotype.

**Example 4.4.2** Six recessive white-eyed *Drosophila* mutations are crossed in all pairs (− = mutant progeny):

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | − | + | − | + | + | − |
| 2 | | − | + | − | + | + |
| 3 | | | − | + | + | − |
| 4 | | | | − | + | + |
| 5 | | | | | − | + |
| 6 | | | | | | − |

Mutations 1, 3 and 6 fail to complement each other, as do 2 and 4; 5 complements all others. There are three complementation groups, $\{1, 3, 6\}$, $\{2, 4\}$ and $\{5\}$, and so at least three genes.

The test has limits. It requires recessive mutations: a **dominant** mutation gives a mutant phenotype in the progeny whatever the other mutation is. Rarely, two mutations in the same gene complement (intragenic complementation, when the **protein** is a **multimer** and the two mutant **subunits** compensate for each other; 7.4.13), and two mutations in different genes can fail to complement when their products form a dosage-sensitive complex (non-allelic non-complementation). The cis–trans form of the test and its use to define the cistron are the subject of 7.4.13.

## 4.5. One Gene or Two?

A ratio alone may not decide how many **genes** are involved, because different hypotheses can predict similar numbers. The decision then needs a statistical comparison and, if that is not conclusive, a further cross that the hypotheses predict differently.

**Example 4.5.1** **True-breeding** albino mice crossed with true-breeding brown mice give an all-black $\mathrm{F}_1$, and the $\mathrm{F}_2$ has 90 black, 30 brown and 40 albino mice ($n = 160$).

*Two-gene hypothesis (recessive epistasis).* A gene *C* is needed for any pigment ($cc$ albino), and a gene *B* determines black ($B\_$) or brown ($bb$). The parents are $ccBB$ (albino) and $CCbb$ (brown), the $\mathrm{F}_1$ $CcBb$ (black), and the $\mathrm{F}_2$ 9 black : 3 brown : 4 albino. Expected numbers $90 : 30 : 40$, $\chi^2 = 0$.

*One-gene hypothesis.* One gene with **alleles** $c^{1}$ (albino parent) and $c^{2}$ (brown parent), whose **heterozygote** is black (a new **phenotype**). The $\mathrm{F}_2$ is 1 albino : 2 black : 1 brown, so 2:1:1 in the order black : brown : albino, expected $80 : 40 : 40$, and

$$
\chi^2 = \frac{10^2}{80} + \frac{10^2}{40} + 0 = 1.25 + 2.5 = 3.75,
$$

with two degrees of freedom ($p = 0.15$).

The data fit 9:3:4 perfectly but do not reject 2:1:1 at the 5 % level. A breeding test separates them. Cross each $\mathrm{F}_2$ albino with the true-breeding brown strain. Under the one-gene model every albino is $c^1c^1$ and every cross gives only black ($c^1c^2$) progeny. Under the two-gene model the albinos are $ccBB$, $ccBb$ or $ccbb$ (1:2:1), and crossed with $CCbb$ they give all black, half black and half brown, or all brown progeny, respectively. Finding brown progeny in some crosses refutes the one-gene model; in the actual experiment this is what was seen.

![One gene or two? A: the F2 of albino × brown mice (90 black, 30 brown, 40 albino) beside the counts expected under the two-gene hypothesis of recessive epistasis (9:3:4) and the one-gene hypothesis with a black heterozygote (2:1:1); neither hypothesis is rejected by the χ² test. B: the breeding test. Each F2 albino is crossed with true-breeding brown mice; the two-gene model predicts that a quarter of the crosses give only black progeny, half give black and brown, and a quarter give only brown, whereas the one-gene model predicts only black progeny from every cross](./plots/one-or-two-genes.py)

**Algorithm 4.5.1 (Deciding Between Genetic Hypotheses)**

1. List the hypotheses (number of genes, **dominance**, epistasis) consistent with the $\mathrm{F}_1$ phenotype.
2. For each, compute the expected $\mathrm{F}_2$ (and **testcross**) counts and the χ² statistic; reject those with small **p-values**.
3. If several survive, find a cross for which they predict qualitatively different outcomes (progeny tests of individual $\mathrm{F}_2$ classes, testcrosses, crosses with tester strains).
4. Prefer the hypothesis that predicts the outcome of the new cross, and test it again with fresh data.

## 4.6. Many Genes with Additive Effects

Mendel's question "can the laws explain continuous traits?" was answered by the Swedish plant breeder Herman Nilsson-Ehle (1909). Crossing wheat with red and white kernels he obtained $\mathrm{F}_2$ in which red was not a single class but graded in intensity, and in some crosses the white class was $1/16$, in others $1/64$.

**Definition 4.6.1 (Additive Polygenic Inheritance)** In **polygenic inheritance** with additive effects, a trait is influenced by several **genes**, and each "contributing" **allele** at any of the **loci** adds the same amount to the **phenotype**, independently of the other alleles.

**Formula 4.6.1 (Distribution of Contributing Alleles)** Let $n$ unlinked loci each have a contributing allele ($R$) and a non-contributing allele ($r$), and self-fertilize the $n$-fold **heterozygote**. Each of the $2n$ alleles of a progeny is $R$ with probability $1/2$, independently, so the number $K$ of contributing alleles has the **binomial distribution** $\mathrm{Bin}(2n, 1/2)$:

$$
\mathbb{P}(K = k) = \binom{2n}{k}\frac{1}{4^n}, \qquad k = 0, 1, \dots, 2n,
$$

with mean $n$ and variance $n/2$. The phenotypic ratio is the row $2n$ of Pascal's triangle: $1:2:1$ for $n = 1$, $1:4:6:4:1$ for $n = 2$, $1:6:15:20:15:6:1$ for $n = 3$. Each extreme class has frequency $1/4^n$, which gives an estimate of the number of genes:

$$
n \approx \frac{\ln(1/f)}{\ln 4},
$$

where $f$ is the fraction of $\mathrm{F}_2$ progeny as extreme as one parent.

**Example 4.6.1** Nilsson-Ehle's crosses that gave $1/64$ white kernels involved $n = \ln 64/\ln 4 = 3$ segregating genes; the $\mathrm{F}_2$ had seven intensity classes, 1:6:15:20:15:6:1, and 63 colored : 1 white. If one of 1 000 $\mathrm{F}_2$ plants is as extreme as a parent, $n \approx \ln 1000/\ln 4 = 5.0$.

As $n$ increases, the binomial distribution approaches a **normal distribution** (the **central limit theorem**, [3.1.13](/3.1.13)), the classes become too many and too close to distinguish, and small environmental effects blur the steps into a continuous curve. A handful of Mendelian genes is therefore enough to produce continuous variation; the full quantitative theory, with unequal effects, **dominance** and environmental variance, is the subject of 7.4.24.

![From Mendelian classes to continuous variation. Bars: the distribution of the number of contributing alleles in the F2 of an n-fold heterozygote for n = 1, 2, 3 and 6 additive genes, Bin(2n, 1/2). Curves: the same distributions blurred by environmental variation (a normal deviation with standard deviation 0.5 allele-equivalents added to each phenotype). With one or two genes the classes are distinct; with six genes and a modest environmental effect the distribution is indistinguishable from a continuous normal curve](./plots/polygenic-distribution.py)

## 4.7. A Worked System: Coat Color in Dogs

Dog coat color combines nearly every kind of interaction in this chapter. At least a dozen **genes** are involved; seven are well understood.

| Gene | Product | Alleles (dominance) | Effect |
|---|---|---|---|
| *E* (extension) | MC1R, the melanocortin-1 receptor of melanocytes | $E^m > E > e$ | $E$: the receptor can switch melanocytes to eumelanin; $e$: inactive receptor, only pheomelanin (yellow, red); $E^m$: dark facial mask |
| *K* (dominant black) | β-defensin 103, which binds MC1R | $K^B > k^{br} > k^y$ | $K^B$: solid eumelanin wherever $E$ is present, masking *A*; $k^{br}$: brindle; $k^yk^y$: *A* patterns are expressed |
| *A* (agouti) | agouti signaling protein, which antagonizes MC1R | $a^y > a^w > a^t > a$ | fawn or sable, wild-type agouti banding, tan points, recessive black |
| *B* (brown) | TYRP1 | $B > b$ | $bb$: brown (liver, chocolate) eumelanin |
| *D* (dilute) | melanophilin (MLPH), pigment granule transport | $D > d$ | $dd$: all pigments diluted (blue, isabella) |
| *S* (spotting) | MITF, transcription factor for melanocyte development | $S > s^p$ | $s^ps^p$: white with colored patches (piebald) |
| *M* (merle) | PMEL, a melanosome protein | $M$ incompletely dominant over $m$ | $Mm$: patches of diluted eumelanin; $MM$: mostly white, often deaf and with eye defects |

The interactions follow the biology of the melanocyte. MC1R is a switch: when it is active (bound by its **agonist**, and not blocked by agouti **protein**), melanocytes make eumelanin; when it is inactive, they make pheomelanin. Agouti protein and β-defensin 103 compete for the **receptor**: $K^B$ keeps it active everywhere, so $K^B$ is epistatic to all *A* **alleles**; $ee$ dogs have no functional receptor, so $ee$ is epistatic to both *K* and *A* (and to *B*, since TYRP1 acts on eumelanin). *D* acts on the transport of any pigment, and *S* and *M* on the survival and pigment-forming capacity of melanocytes in parts of the coat, so they act independently of the switch. *M* is **pleiotropic**: the same defect of melanocytes in the inner ear and the eye causes the deafness and eye defects of $MM$ dogs, which is why breeders avoid crossing two merles.

![The pigment switch in dog melanocytes as an activity-flow diagram. MC1R (gene E) activated by α-MSH drives eumelanin synthesis; agouti signaling protein (gene A) inhibits MC1R and allows pheomelanin; β-defensin 103 (gene K, allele K^B) binds MC1R, blocks the inhibition by agouti and keeps the receptor on. TYRP1 (gene B) is needed for black rather than brown eumelanin, and melanophilin (gene D) for full pigment deposition. The epistatic relations follow from the positions in the diagram: ee removes the receptor and masks K, A and B; K^B masks A](./plots/dog-coat-switch.py)

**Example 4.7.1** (a) Two black Labradors ($K^BK^B\,aa$ like all Labradors) of **genotype** $BbEe$ have puppies: $\mathbb{P}(\text{black}) = \tfrac34 \cdot \tfrac34 = \tfrac9{16}$, $\mathbb{P}(\text{chocolate}) = \tfrac14 \cdot \tfrac34 = \tfrac3{16}$, $\mathbb{P}(\text{yellow}) = \tfrac14$. (b) A black $BbEe$ Labrador and a chocolate $bbEe$ Labrador: black $\tfrac12 \cdot \tfrac34 = \tfrac38$, chocolate $\tfrac12 \cdot \tfrac34 = \tfrac38$, yellow $\tfrac14$. (c) For a dog of genotype $EE\, k^yk^y\, a^ta^t\, Bb\, Dd$ crossed with an identical dog, the proportion of puppies showing black-and-tan points (eumelanin black, not diluted) is $\mathbb{P}(B\_) \cdot \mathbb{P}(D\_) = \tfrac34 \cdot \tfrac34 = \tfrac9{16}$; the *E*, *K* and *A* **loci** are **homozygous** and contribute factors of 1.

## 4.8. A Systematic Method for Modified Ratios

### 4.8.1. The Algorithm

Problems in genetics often give a set of progeny counts and ask for the genetic explanation. The following procedure solves most of them.

**Algorithm 4.8.1 (Interpreting a Modified Ratio)**

1. Simplify the counts to a ratio. Divide by the smallest class (or fit small integers) and find the total number of parts $T$.
2. Count the **genes** from $T$. For an $\mathrm{F}_2$ (or self-fertilization): $T = 4$ suggests one gene, $16$ two genes, $64$ three genes ($T = 4^n$). For a **testcross**: $T = 2^n$. A total that is not a power of 4 (or 2) suggests lethality (12 = 16 − 4, 15 = 16 − 1, 9 = 16 − 7) or more than two **alleles**; a total of 3 in a **monohybrid cross** (2:1) suggests a **recessive** lethal.
3. Merge the genotypic classes. Write the standard classes ($9\,A\_B\_ : 3\,A\_bb : 3\,aaB\_ : 1\,aabb$, or the 27:9:9:9:3:3:3:1 classes for three genes, or the 1:2:1 classes when **dominance** is incomplete) and find which combination gives the observed ratio (9:3:4 = 9 : 3 : (3 + 1); 12:3:1 = (9 + 3) : 3 : 1; 9:7 = 9 : (3 + 3 + 1)). Identify each **phenotype** with its genotypic classes.
4. Propose a pathway or mechanism consistent with the merging (Table in 4.2.2) and check it against the parental and $\mathrm{F}_1$ phenotypes.
5. Predict a second cross: the testcross ratio (Formula 4.8.1), the progeny of individual $\mathrm{F}_2$ classes.
6. Test the hypothesis with χ², using the merged classes and $k - 1$ degrees of freedom (Algorithm 2.5.1 of [7.4.2](/7.4.2#sec-2.5)).

### 4.8.2. Ratios with Lethality

**Formula 4.8.1 (Lethality in Dihybrid Crosses)** For $AaBb \times AaBb$ with **complete dominance** at both **loci** and the stated **genotypes** lethal, the surviving phenotypic classes ($A\_B\_ : A\_bb : aaB\_ : aabb$, with the dominant classes reduced to their surviving genotypes) are:

| Lethal genotypes | Surviving ratio | Total |
|---|---|---|
| $AA$ (dominant allele $A$ with a recessive lethal effect, $A\_$ visible) | $6 : 3 : 2 : 1$ | 12 |
| $AA$ and $BB$ | $4 : 2 : 2 : 1$ | 9 |
| $aabb$ | $9 : 3 : 3$ | 15 |
| $aa$ (recessive lethal) | $9 : 3$ (only $A\_$ classes) | 12 |

Each row follows from the per-locus survivors: for $AA$ lethal, the $A$ locus gives $\tfrac23\,Aa : \tfrac13\,aa$ instead of $\tfrac34 : \tfrac14$, and $(2:1)(3:1) = 6:3:2:1$; for both, $(2:1)(2:1) = 4:2:2:1$. Lethality that removes a combination of genotypes at two loci (as $aabb$) cannot be factored and is computed from the 16 cells.

Lethality can also act on gametes rather than zygotes. A pollen-lethal or partly pollen-lethal allele changes the gametic proportions of one sex, and the zygotes are then formed from unequal gametes.

**Formula 4.8.2 (Gametic Selection)** Let a fraction $s$ of the $a$-bearing gametes of one sex (say the pollen) be nonfunctional, the other sex producing $A$ and $a$ in equal numbers. In $Aa \times Aa$ the functional pollen is $A : a = 1 : (1 - s)$, and the progeny are

$$
\mathbb{P}(AA) = \frac{1}{2(2 - s)}, \qquad \mathbb{P}(Aa) = \frac12, \qquad \mathbb{P}(aa) = \frac{1 - s}{2(2 - s)} .
$$

For $s = 1/2$ the genotypes are $2 : 3 : 1$ and the phenotypes $5 : 1$; for $s = 1$ (no $a$ pollen functions) they are $1 : 1 : 0$, and no recessive appears, although $a$ is still transmitted through the eggs. The reciprocal testcrosses distinguish gametic selection from zygotic lethality: with the $Aa$ plant as the seed parent the testcross gives 1:1; with it as the pollen parent, $1 : (1 - s)$. Combined with a second, normally segregating locus, the ratios multiply as before: $(5:1)(3:1) = 15 : 5 : 3 : 1$.

### 4.8.3. Testcross Ratios and Three Genes

The testcross of a dihybrid, $AaBb \times aabb$, gives the four classes in equal numbers, and the same merging rules apply: 9:3:4 → 1:1:2, 9:7 → 1:3, 12:3:1 → 2:1:1, 13:3 → 3:1, 15:1 → 3:1, 9:6:1 → 1:2:1. Two interactions with the same testcross ratio (13:3 and 15:1) are separated by the $\mathrm{F}_2$.

With three genes the $\mathrm{F}_2$ has $27\,A\_B\_C\_$ and the other classes of $(3 + 1)^3$. Complementary action of three genes (all three steps of a pathway needed) gives $27 : 37$; a three-step pathway with recessive epistasis in which loss of the last step gives a second color gives $27\,A\_B\_C\_ : 9\,A\_B\_cc : 28$ (colorless: $aa$ or $bb$); a trait requiring a dominant allele at any of three redundant genes gives $63 : 1$.

**Example 4.8.1** An $\mathrm{F}_2$ of 500 plants has 382 white and 118 colored plants. Two hypotheses are suggested: one gene with colored recessive (3:1), or dominant suppression (13:3). For 3:1 the expected numbers are $375 : 125$ and $\chi^2 = 0.13 + 0.39 = 0.52$ ($p = 0.47$). For 13:3 they are $406.25 : 93.75$ and $\chi^2 = 1.45 + 6.27 = 7.72$ ($p = 0.005$). The data reject 13:3 and fit 3:1.

**Example 4.8.2** Two **true-breeding** white-flowered lines are crossed; the $\mathrm{F}_1$ is purple and the $\mathrm{F}_2$ has 245 purple and 155 white. (1) $245 : 155 \approx 1.58 : 1$; in sixteenths, $9.8 : 6.2$, close to 9:7, $T = 16$: two genes. (2) 9:7 means purple requires $A\_B\_$: complementary genes. (3) The white parents were $AAbb$ and $aaBB$. (4) Prediction: the testcross of the $\mathrm{F}_1$ to a double recessive gives 1 purple : 3 white. (5) Test: expected $225 : 175$; $\chi^2 = 400/225 + 400/175 = 1.78 + 2.29 = 4.06$ with one degree of freedom, $p = 0.044$, a marginal rejection at the 5 % level. Before abandoning the model, one checks alternatives (3:1 is far worse: $\chi^2 = 40.3$) and classification errors; a testcross would settle it.

**Example 4.8.3** In mice, a cross of two yellow, black-eyed mice gives yellow black-eyed, yellow pink-eyed, agouti black-eyed and agouti pink-eyed progeny in the ratio $6:3:2:1$ (Example 3.4.1 of [7.4.3](/7.4.3#sec-3.4)). $T = 12$: two genes, with a lethal class removing 4 of 16. The ratio factors as $(2:1)(3:1)$: one locus segregates 2 yellow : 1 agouti (yellow lethal when **homozygous**), the other 3 black-eyed : 1 pink-eyed.

## Summary

| Topic | Key results |
|---|---|
| New phenotypes (4.1) | two genes in independent pathways: 9:3:3:1 with new classes (lentils, combs) |
| **Epistasis** (Definition 4.2.1) | one locus masks another; Mendelian vs statistical sense |
| Ratios (Formula 4.2.1, table in 4.2.2) | merged $9:3:3:1$ classes: **recessive epistasis** 9:3:4 (1:1:2), **complementary gene action** 9:7 (1:3), **dominant epistasis** 12:3:1 (2:1:1), dominant suppression 13:3 (3:1), **duplicate genes** 15:1 (3:1), cumulative 9:6:1 (1:2:1) |
| Biochemical resolution (Example 4.2.8) | clover extracts plus enzyme or substrate split 9:7 into 9:3:3:1 |
| Pathways (4.2.3) | genes in series: the earlier step is epistatic (biosynthesis); parallel genes: 15:1 |
| **Suppressor mutation** (Definition 4.3.1) | restores wild type; allele-specific suppression reveals contacts |
| Redundancy (Definition 4.3.2) | synthetic lethality; $\varepsilon_{ab} = W_{ab} - W_aW_b$ (Formula 4.3.1) |
| **Genetic heterogeneity** (Definition 4.4.1) | many genes, one phenotype |
| **Complementation test** (Definition 4.4.2) | trans-heterozygote wild type: different genes; mutant: same gene; **complementation groups** (Definition 4.4.3, Algorithm 4.4.1) |
| One or two genes (4.5) | χ² comparison and a discriminating breeding test (Example 4.5.1, Algorithm 4.5.1) |
| Polygenes (Definition 4.6.1, Formula 4.6.1) | $\mathrm{Bin}(2n, 1/2)$: $1:4:6:4:1$; extreme class $4^{-n}$, $n \approx \ln(1/f)/\ln 4$; normal limit |
| Dog coat (4.7) | MC1R switch: $ee$ epistatic to *K*, *A*, *B*; $K^B$ epistatic to *A*; *M* pleiotropic |
| Ratio puzzles (Algorithm 4.8.1) | $T = 4^n$; merge classes; lethality: $6:3:2:1$, $4:2:2:1$, $9:3:3$ (Formula 4.8.1); gametic selection $5:1$ for half the $a$ pollen nonfunctional (Formula 4.8.2); three genes: $27:37$, $27:9:28$, $63:1$ |

## Questions

1. For each $\mathrm{F}_2$ ratio, state the type of **gene** interaction and the **testcross** ratio: (a) 9:3:4; (b) 15:1; (c) 12:3:1; (d) 9:7; (e) 13:3; (f) 9:6:1.

   **Answer** (a) **Recessive** epistasis, 1:1:2. (b) Duplicate genes (redundancy), 3:1. (c) **Dominant** epistasis, 2:1:1. (d) Complementary genes, 1:3. (e) Dominant suppression (dominant epistasis II), 3:1. (f) Cumulative duplicate genes, 1:2:1.
2. In Labradors, what are the expected proportions of black, chocolate and yellow puppies from (a) $BbEe \times bbee$, (b) $BBEe \times bbEe$, (c) $Bbee \times bbEE$?

   **Answer** (a) $B$: $\tfrac12 B\_$, $\tfrac12 bb$; $E$: $\tfrac12 E\_$, $\tfrac12 ee$. Black $\tfrac14$, chocolate $\tfrac14$, yellow $\tfrac12$. (b) All $Bb$; $E$: $\tfrac34 E\_$. Black $\tfrac34$, yellow $\tfrac14$, no chocolate. (c) All $Ee$, so no yellow; black $\tfrac12$, chocolate $\tfrac12$.
3. Two "type O" parents have a type A child. Explain, giving possible **genotypes** at the *ABO* and *FUT1* **loci** of the parents and the child.

   **Answer** One parent must have the Bombay **phenotype**: for example the mother $hh\,I^Ai$ (types as O because she makes no H **antigen**) and the father $Hh\,ii$ (true type O). The child $Hh\,I^Ai$ receives $I^A$ from the mother and $H$ from the father and makes the A antigen. The probability of such a child from these parents is $\tfrac12 (H \text{ from father}) \times \tfrac12 (I^A \text{ from mother}) = \tfrac14$.
4. Two white-flowered sweet pea lines give a purple $\mathrm{F}_1$. (a) What $\mathrm{F}_2$ ratio is expected? (b) What fraction of the white $\mathrm{F}_2$ plants are **true-breeding**? (c) If two white $\mathrm{F}_2$ plants are crossed at random, what is the probability that they produce purple progeny at all?

   **Answer** (a) 9:7. (b) White classes: $A\_bb$ (3), $aaB\_$ (3), $aabb$ (1). All white plants are true-breeding white when selfed, since selfing a white plant cannot generate $A\_B\_$ ($A\_bb$ selfed gives only $\_\_bb$; $aaB\_$ gives only $aa\_\_$): 7/7 = 1. (c) Purple progeny need one parent to contribute $A$ and one to contribute $B$, which requires one parent from $A\_bb$ and the other from $aaB\_$. $\mathbb{P} = 2 \times \tfrac37 \times \tfrac37 = \tfrac{18}{49} \approx 0.37$ (any such pair produces some purple progeny).
5. An $\mathrm{F}_2$ of 480 plants has 271 disc, 181 spherical and 28 long fruits. (a) Test 9:6:1. (b) How could you distinguish the genotypes of the spherical plants?

   **Answer** (a) Expected 270, 180, 30. $\chi^2 = 1/270 + 1/180 + 4/30 = 0.004 + 0.006 + 0.133 = 0.14$, 2 df, $p = 0.93$: consistent. (b) Testcross each spherical plant with a long ($aabb$) plant: $AAbb$ and $aaBB$ give all spherical; $Aabb$ and $aaBb$ give 1 spherical : 1 long. Crossing two spherical plants that give disc progeny shows that one is $A\_bb$ and the other $aaB\_$.
6. Seven recessive **mutations** causing arginine requirement in yeast are tested for complementation in **diploids**. Pairs that fail to complement: 1–4, 1–6, 4–6, 2–7, 3–5. All other pairs complement. How many genes are identified, and which mutations are in each?

   **Answer** Groups: $\{1, 4, 6\}$, $\{2, 7\}$, $\{3, 5\}$: three genes. The table is consistent (within each group all pairs fail; between groups all complement).
7. Two deaf parents, each from a family with recessive deafness, have four children who all hear normally. (a) What is the most likely explanation? (b) If both parents are **homozygous** for mutations in different genes, what is the probability that a grandchild from two of these children (siblings, for the sake of the calculation) is deaf?

   **Answer** (a) Complementation: the parents are homozygous for mutations in two different genes ($aaBB \times AAbb$), and all children are $AaBb$. (b) $AaBb \times AaBb$: deaf if $aa$ or $bb$, $\mathbb{P} = 1 - \tfrac34 \cdot \tfrac34 = \tfrac7{16}$.
8. In Example 4.5.1, suppose each $\mathrm{F}_2$ albino mouse is crossed with the brown strain. Under the two-gene model, what fraction of the crosses will produce some brown progeny? What fraction of all progeny from all such crosses (equal family sizes) will be brown?

   **Answer** Albinos are $\tfrac14 ccBB$, $\tfrac12 ccBb$, $\tfrac14 ccbb$. Crossed with $CCbb$: $ccBB$ gives all black, $ccBb$ half brown, $ccbb$ all brown. Crosses with some brown: $\tfrac12 + \tfrac14 = \tfrac34$. Brown fraction of all progeny: $\tfrac12 \cdot \tfrac12 + \tfrac14 \cdot 1 = \tfrac12$.
9. Wheat kernel color is controlled by additive genes. A cross between dark red and white lines gives an intermediate $\mathrm{F}_1$; among 1 280 $\mathrm{F}_2$ kernels, 20 are as white as the white parent. (a) How many genes segregate? (b) What fraction of the $\mathrm{F}_2$ is expected to be exactly intermediate (like the $\mathrm{F}_1$)? (c) What are the mean and variance of the number of contributing **alleles**?

   **Answer** (a) $f = 20/1280 = 1/64$, $n = \ln 64/\ln 4 = 3$. (b) $\binom63/64 = 20/64 = 0.3125$. (c) $K \sim \mathrm{Bin}(6, 1/2)$: mean 3, variance $6 \times \tfrac14 = 1.5$.
10. In a **dihybrid cross** $AaBb \times AaBb$, $A$ (dominant, curly wings) is lethal when homozygous, and $B\_$ (red eyes) is completely dominant over $bb$ (brown eyes). What phenotypic ratio is expected among survivors? What fraction of the survivors are true-breeding for both traits?

    **Answer** $(2:1)(3:1) = 6$ curly red : 3 curly brown : 2 straight red : 1 straight brown. True-breeding individuals must be homozygous at both loci; $AA$ is dead and $Aa$ is not true-breeding, so only $aaBB$ and $aabb$: $\tfrac13 \cdot \tfrac14 + \tfrac13 \cdot \tfrac14 = \tfrac16$ of survivors.
11. Two yeast mutants grow at 70 % and 60 % of the **wild-type** rate, and the double mutant at 20 %. (a) Compute the multiplicative epistasis score. (b) If the double mutant grew at 60 %, what would that suggest?

    **Answer** (a) Expected $0.7 \times 0.6 = 0.42$; $\varepsilon = 0.20 - 0.42 = -0.22$, negative (aggravating) epistasis: the genes probably act in parallel, compensating pathways. (b) $\varepsilon = 0.60 - 0.42 = +0.18$, positive (alleviating), with the double mutant equal to the more severe single mutant: the genes probably act in the same pathway or complex, so that losing one inactivates the function and losing the other adds nothing.
12. (Competition style.) A trihybrid $AaBbCc$ is self-fertilized. Purple pigment requires dominant alleles at all three loci, which encode three **enzymes** of one pathway. (a) What fraction of the progeny is purple? (b) Among the white progeny, what fraction is homozygous recessive at exactly one locus and dominant at the other two? (c) If, instead, $cc$ plants with $A\_B\_$ accumulate a red intermediate, what is the full phenotypic ratio?

    **Answer** (a) $(3/4)^3 = 27/64$. (b) White plants: $37/64$. Exactly one recessive locus: $3 \times (1/4)(3/4)^2 = 27/64$; fraction among white: $27/37 \approx 0.73$. (c) Purple $A\_B\_C\_$: $27/64$; red $A\_B\_cc$: $\tfrac34 \cdot \tfrac34 \cdot \tfrac14 = 9/64$; white (any $aa$ or $bb$): $1 - 9/16 = 28/64$. The ratio is $27 : 9 : 28$.
13. (Competition style.) In a plant, flower color is controlled by two unlinked genes. A purple-flowered plant crossed with a white plant gives 3 purple : 5 white. What are the genotypes of the parents if the $\mathrm{F}_2$ of two true-breeding white lines shows 9 purple : 7 white?

    **Answer** The 9:7 ratio shows complementary genes: purple is $A\_B\_$. A total of 8 parts in a single cross means one parent makes four kinds of gametes and the other two: $AaBb \times Aabb$ (or $aaBb$). Check: $AaBb \times Aabb$ gives purple $\mathbb{P}(A\_)\mathbb{P}(B\_) = \tfrac34 \cdot \tfrac12 = \tfrac38$, white $\tfrac58$. So the purple parent is $AaBb$ and the white parent $Aabb$ or $aaBb$.
14. (Competition style.) In chickens, $I$ (dominant inhibitor) suppresses color and $cc$ is white. $IiCc \times iiCc$ is made. (a) Give the ratio of white to colored. (b) Among colored progeny, what fraction is $CC$?

    **Answer** (a) Colored requires $ii$ and $C\_$: $\tfrac12 \cdot \tfrac34 = \tfrac38$. White : colored = 5 : 3. (b) Among colored ($iiC\_$), $\mathbb{P}(CC \mid C\_) = 1/3$.
15. In shepherd's purse the $\mathrm{F}_2$ of a triangular × ovoid cross is 15 triangular : 1 ovoid (duplicate genes). If each triangular $\mathrm{F}_2$ plant is self-fertilized, what fractions of them give (a) only triangular progeny, (b) 3 triangular : 1 ovoid, (c) 15 : 1?

    **Answer** Triangular plants are the 15 of 16 classes other than $aabb$. (a) True-breeding requires $AA$ or $BB$: $AABB$, $AABb$, $AAbb$, $AaBB$, $aaBB$, which are $1 + 2 + 1 + 2 + 1 = 7$ sixteenths: $\tfrac7{15}$. (b) **Heterozygous** at one locus and recessive at the other ($Aabb$, $aaBb$): $\tfrac4{15}$. (c) $AaBb$: $\tfrac4{15}$. Check: $7 + 4 + 4 = 15$.
16. A plant heterozygous $Aa$ is self-fertilized and gives 410 dominant and 90 recessive progeny. (a) Test 3:1. (b) Test the hypothesis that half of the $a$ pollen is nonfunctional. (c) What reciprocal testcrosses would confirm it?

    **Answer** (a) Expected $375 : 125$; $\chi^2 = 3.27 + 9.80 = 13.1$ (1 df, $p = 3 \times 10^{-4}$): rejected. (b) Formula 4.8.2 with $s = 1/2$ predicts $5:1$, expected $416.7 : 83.3$; $\chi^2 = 0.11 + 0.53 = 0.64$ ($p = 0.42$): consistent. (c) $Aa$ (seed parent) × $aa$ should give 1:1; $aa$ (seed parent) × $Aa$ (pollen) should give $A : a = 1 : \tfrac12 = 2 : 1$.
17. Two yellow short-tailed mice are crossed repeatedly, and the progeny are yellow short : yellow long : gray short : gray long $= 6 : 3 : 2 : 1$. (a) Which genotype is lethal? (b) Give the genotypes of the yellow long-tailed and of the gray short-tailed progeny. (c) What fraction of the surviving progeny is homozygous at both loci? (d) What would a ratio of $4:2:2:1$ mean?

    **Answer** (a) Yellow : gray $= 9 : 3 = 3 : 1$, short : long $= 8 : 4 = 2 : 1$: the tail locus is the one with a lethal homozygote, $DD$ (short $D$ dominant for tail length, recessive lethal). (b) Yellow long: $YYdd$ or $Yydd$ ($1 : 2$); gray short: $yyDd$. (c) Of 12 surviving parts, $YYdd$ and $yydd$ are 1 each: $\tfrac2{12} = \tfrac16$. (d) $(2:1)(2:1)$: both $YY$ and $DD$ are lethal, and every yellow short survivor is $YyDd$.
18. A black dog crossed with a white dog gives all black puppies; intercrossing the $\mathrm{F}_1$ gives 25 black, 10 brown and 13 white puppies. Propose a model and test it.

    **Answer** Three classes with the white class about a quarter suggest recessive epistasis, 9 black ($A\_B\_$) : 3 brown ($aaB\_$) : 4 white ($\_\_bb$), with $bb$ epistatic. Expected for $n = 48$: $27 : 9 : 12$, all at least 5; $\chi^2 = 4/27 + 1/9 + 1/12 = 0.34$ with two degrees of freedom ($p = 0.84$). The parents were $AABB$ (black) and $\_\_bb$ white; since the $\mathrm{F}_1$ must be $AaBb$, the white parent was $aabb$. A testcross of the $\mathrm{F}_1$ to $aabb$ should give $1 : 1 : 2$.
19. An $\mathrm{F}_2$ of 160 plants from the cross $Ac/Ac\,li/li \times ac/ac\,Li/Li$ in white clover is tested by Corkill's method. How many plants are expected (a) to release cyanide on crushing, (b) to release it only when linamarase is added, (c) only when glucoside is added, (d) in neither case?

    **Answer** (a) $\tfrac9{16} \times 160 = 90$. (b) $Ac\_\,li/li$: $\tfrac3{16} \times 160 = 30$. (c) $ac/ac\,Li\_$: $30$. (d) $ac/ac\,li/li$: $10$.
20. (Competition style.) In a mammal, $bb$ is epistatic to black and brown ($A\_$ black, $aa$ brown in $B\_$ animals; $bb$ white, recessive epistasis), and a dominant allele $C$ at a third, unlinked locus prevents all pigmentation. The trihybrid $AaBbCc$ is intercrossed. Give the phenotypic ratio. What fraction of the white progeny is $CC$, and so certain to give only white offspring whatever its partner?

    **Answer** Pigment requires $cc$ ($\tfrac14$), within which the ratio is $9 : 3 : 4$. Out of 64: black $9$, brown $3$, white $4 + 48 = 52$: ratio $9 : 3 : 52$. All $CC$ animals ($\tfrac{16}{64}$) are white and transmit $C$ to every offspring: $\tfrac{16}{52} = \tfrac4{13}$ of the white progeny. The other white animals ($Cc$, or $cc$ with $bb$) can have colored offspring with a suitable partner (for example $Cc\,BB \times cc\,bb$).
