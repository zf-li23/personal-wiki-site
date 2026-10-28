---
title: "Mapping Complex Traits: QTL, GWAS and Polygenic Prediction"
description: "Finding the genes behind quantitative variation. QTL mapping in experimental crosses: single-marker tests, interval mapping with LOD scores and permutation thresholds, fine mapping with near-isogenic lines (fw2.2); association mapping, haplotype blocks and tag SNPs; genome-wide association studies: the allelic test and odds ratio, genome-wide significance, Manhattan and QQ plots, genomic inflation and population stratification, power and the winner's curse; from signal to gene: credible sets, eQTLs and the FTO–IRX3 story; Mendelian randomization; SNP heritability, missing heritability, the omnigenic model and rare-variant burden tests; polygenic scores, their accuracy, portability and uses."
---

Quantitative genetics ([7.4.24](/7.4.24)) describes complex traits by **variance** components without naming a single **gene**. Mapping asks the complementary question: where in the **genome** are the loci that contribute to the variation, how large are their effects, and which genes and variants are responsible? Two strategies exist. In experimental organisms we can make crosses between lines that differ in the trait and follow the co-segregation of the trait with markers in the progeny: QTL mapping, the quantitative extension of the **linkage** mapping of [7.4.8](/7.4.8) and [7.4.14](/7.4.14). In humans, and whenever crosses are impossible or too coarse, we use the recombination that has accumulated over thousands of generations of history: association mapping in populations, which relies on **linkage disequilibrium** ([7.4.22](/7.4.22), §22.3) between markers and causal variants and which, applied to the whole genome, is the genome-wide association study (GWAS).

Since 2005 GWAS have found tens of thousands of associations for hundreds of traits and diseases, and changed the picture of complex traits: most are influenced by thousands of variants of tiny effect, most of them noncoding, spread over the genome. This chapter covers the design, calculation and interpretation of these studies, from the single-marker test in a backcross to polygenic scores. The statistics are those of **hypothesis testing** and multiple comparisons ([3.2.4](/3.2.4), [3.2.6](/3.2.6)), regression and **analysis of variance** ([3.3](/3.3)) and **principal components** ([3.4.5](/3.4.5)); the processing of sequencing and **genotyping** data and imputation are treated in bioinformatics (7.8).

## 25.1. QTL Mapping in Experimental Crosses

**Definition 25.1.1 (Quantitative Trait Locus)** A **quantitative trait locus** (QTL) is a chromosomal region containing one or more genes whose allelic variation contributes to the variation of a **quantitative trait**; QTL mapping is the localization of such regions by the statistical association between the trait and **genotypes** at genetic markers in a segregating population.

### 25.1.1. Crosses and Single-Marker Tests

The classical design starts from two inbred lines that differ in the trait and are homozygous at essentially every **locus** ([7.4.22](/7.4.22), §22.4.3). Their F₁ is heterozygous everywhere; in a backcross F₁ × parent or an F₂, every locus segregates, and recombination in the F₁ makes the **chromosomes** of the progeny mosaics of the two parental genomes. If a marker is linked to a QTL, the progeny classes of the marker differ in mean **phenotype**.

**Example 25.1.1 (Fruit Weight in Tomato)** A large-fruited cultivar (Beefmaster, B; fruits about $230\,\mathrm{g}$) was crossed with a small-fruited one (Sungold, S; $10\,\mathrm{g}$), and the F₁ backcrossed to B, so that every backcross plant is B/B or B/S at each marker. In a sample of backcross plants (overall mean fruit weight $175.7\,\mathrm{g}$), the B/B and B/S classes had means $176.3$ and $175.3\,\mathrm{g}$ at marker M1, but $180.7$ and $169.6\,\mathrm{g}$ at marker M3. The near-equality at M1 is what is expected if no QTL lies near M1; the difference of $11\,\mathrm{g}$ at M3 suggests a QTL linked to M3, at which a B **allele** increases fruit weight. Each comparison is a two-sample $t$ test, or equivalently a one-way **analysis of variance** with the marker genotype as factor ([3.3.12](/3.3.12#sec-12.2)).

**Formula 25.1.1 (Marker-Class Difference in a Backcross)** Let a QTL with genotypic values $\mu_{QQ}$ and $\mu_{Qq}$ (difference $\delta = \mu_{QQ} - \mu_{Qq}$) lie at **recombination frequency** $r$ from a marker. In a backcross, the difference between the marker classes is

$$
\bar Z_{MM} - \bar Z_{Mm} = (1 - 2r)\,\delta, \tag{25.1}
$$

and the proportion of the phenotypic variance explained by the marker is $(1 - 2r)^2$ times that explained by the QTL.

**Proof** Among backcross progeny of class $MM$, the QTL genotype is $QQ$ with probability $1 - r$ (no recombination) and $Qq$ with probability $r$, so the class mean is $(1 - r)\mu_{QQ} + r\mu_{Qq}$; for class $Mm$ it is $r\mu_{QQ} + (1 - r)\mu_{Qq}$. The difference is $(1 - 2r)(\mu_{QQ} - \mu_{Qq})$. $\square$

A single marker therefore confounds effect and position: a small difference may come from a large QTL far away or a small one nearby. In Example 25.1.1, if the QTL were $10\,\mathrm{cM}$ from M3 ($r = 0.091$ by the Haldane function, [7.4.8](/7.4.8)), the true effect would be $11.1/(1 - 0.18) = 13.6\,\mathrm{g}$.

### 25.1.2. Interval Mapping

Lander and Botstein (1989) resolved the confounding by scanning positions between markers.

**Algorithm 25.1.1 (Interval Mapping with Permutation Threshold)**

1. Genotype $n$ progeny at markers spaced along each chromosome and measure the trait $y_i$.
2. At each test position $x$ (for example every $1\,\mathrm{cM}$), compute for each individual the conditional probability $\pi_i(x)$ of the QTL genotype given its flanking marker genotypes and the map distances (no **interference**, [7.4.8](/7.4.8)).
3. Fit the model with a QTL at $x$ and compare it with the model without: by maximum likelihood with the mixture of QTL genotypes (Lander–Botstein), or approximately by regressing $y_i$ on $\pi_i(x)$ (Haley–Knott regression). The evidence for a QTL at $x$ is the **LOD score**
   $$
   \mathrm{LOD}(x) = \log_{10}\frac{L(\text{QTL at } x)}{L(\text{no QTL})} = \frac n2\log_{10}\frac{\mathrm{RSS}_0}{\mathrm{RSS}_1(x)}
   $$
   (the second form for regression with normal errors; $\mathrm{RSS}$ are residual sums of squares). This is the decimal logarithm of a **likelihood ratio**, as in human linkage analysis ([7.4.14](/7.4.14)).
4. Determine the genome-wide significance threshold by permutation (Churchill and Doerge 1994): shuffle the phenotypes among individuals many times (which destroys any genotype–phenotype association but keeps the marker data and trait distribution), repeat the scan, and record the maximum LOD of each permutation; the $95\,\%$ **quantile** of these maxima is the $5\,\%$ genome-wide threshold.
5. Report the peak position as the QTL estimate, its effect from the fitted model, and a support interval (the region within $1.5$ LOD units of the peak, roughly a $95\,\%$ **confidence interval**).

Genome-wide thresholds in a mouse- or plant-sized genome are typically LOD $3$–$4$, higher than the pointwise threshold because hundreds of correlated tests are performed. With a few hundred progeny the support interval is usually $10$–$30\,\mathrm{cM}$, which may contain hundreds of genes: QTL mapping in a cross localizes, it does not identify. Resolution is limited by the number of recombination events in the population. Larger crosses, recombinant inbred lines (many generations of selfing or sib mating after the cross), advanced intercross lines and multiparent populations (MAGIC lines in *Arabidopsis*, rice and wheat; the mouse Collaborative Cross) accumulate more recombination and give finer maps.

![QTL mapping in a simulated backcross of 200 individuals with markers every 10 cM and one QTL at 47 cM, whose heterozygote raises the trait by 0.6 phenotypic standard deviations (Algorithm 25.1.1). A: LOD profile of Haley–Knott interval mapping (line) and single-marker LOD scores at the markers (dots); the peak lies near the true QTL (triangle); shaded: the 1.5-LOD support interval; dashed: the 5 % genome-wide threshold from 200 permutations. B: the distribution of the maximum LOD over the chromosome when the phenotypes are permuted, with the threshold (dashed) and the observed maximum (solid)](./plots/interval-mapping.py)

### 25.1.3. Fine Mapping and Gene Identification

**Definition 25.1.2 (Near-Isogenic Line)** A **near-isogenic line** (NIL, or congenic line) is a line that is genetically identical to a recurrent parental line except for a short introgressed chromosomal segment from a donor line, produced by repeated backcrossing to the recurrent parent with selection for markers flanking the segment. After $t$ backcross generations the expected donor fraction outside the selected region is $(1/2)^{t+1}$.

A panel of NILs whose donor segments end at different points within a QTL interval allows the QTL to be localized by comparing their phenotypes: the QTL lies in the region shared by all lines with the donor phenotype and absent from all others. Each recombinant within the interval is informative, and the expected number among $n$ meioses for an interval of $d$ morgans is $nd$; for a $2\,\mathrm{cM}$ interval, 500 meioses give about 10 recombinants.

**Example 25.1.2 (fw2.2)** The tomato QTL *fw2.2* accounts for up to $30\,\%$ of the difference in fruit weight between wild tomatoes, whose fruits weigh a few grams, and domesticated ones. Fine mapping with NILs narrowed it to a small region, and Frary and colleagues (2000) showed by transformation that the gene (*CNR*/*ORFX*, a member of a family of cell-number regulators) acts as a negative regulator of cell division in the developing fruit; the large-fruit allele differs from the wild allele not in the **protein** but in the timing and level of expression. This pattern, a regulatory variant of moderate effect in a conserved gene, is typical of the QTL cloned in crops and of the domestication genes such as *tb1* in maize.

## 25.2. Association Mapping

**Definition 25.2.1 (Association Mapping)** **Association mapping** (linkage disequilibrium mapping) locates genetic variants that influence a trait by testing, in samples of individuals from a population (not from a designed cross), for statistical association between marker genotypes and phenotype. It relies on linkage disequilibrium between markers and causal variants, created by the history of the population and eroded by the recombination of many past generations.

Because the relevant recombination events are those of all generations since a causal variant arose, LD extends over short distances (in humans typically $10$–$100\,\mathrm{kb}$, [7.4.22](/7.4.22), Theorem 22.3.1), and association mapping localizes much more finely than a cross. The price is that the markers must be dense and the samples large, and that the population must be homogeneous or its structure modeled (§25.3.3).

Human **haplotypes** have a block structure: stretches of tens of kilobases with high LD and few common haplotypes, separated by **recombination hotspots**, which in humans are mostly specified by **binding sites** of the PRDM9 protein ([7.4.8](/7.4.8)). The International HapMap Project (2005) and the 1000 Genomes Project (2015) catalogued common variants and their LD in several populations.

**Definition 25.2.2 (Tag SNP)** A **tag SNP** is a SNP chosen to represent a group of SNPs in strong linkage disequilibrium with it (commonly $r^2 \geq 0.8$), so that genotyping the tag captures most of the information about the untyped variants. A set of tag SNPs, together with imputation of untyped variants from a reference panel of haplotypes, lets genotyping arrays of $10^5$–$10^6$ SNPs survey most common variation of a genome of $10^7$ common variants.

**Formula 25.2.1 (Indirect Association)** If a tested marker has linkage disequilibrium $r^2$ with an untyped causal variant, the noncentrality of the marker's 1-df test is $r^2$ times that of the causal variant: a study of $N$ individuals has at the marker the power of a study of $r^2N$ individuals at the causal variant. The effect estimated at the marker is attenuated accordingly (by the factor $r\,\sigma_{\mathrm{causal}}/\sigma_{\mathrm{marker}}$ for allele-count regression).

This follows because the marker's genotype is a noisy proxy of the causal genotype with squared correlation $r^2$ ([7.4.22](/7.4.22), Definition 22.3.2), and the noncentrality of the regression test is proportional to the squared correlation between predictor and trait.

![Haplotype blocks in simulated haplotypes (400 chromosomes, 40 SNPs, recombination hotspots at 0.30 and 0.68 of the region; copying model with founder haplotypes). Each diamond is a pair of SNPs, shaded by r² (A) or |D′| (B); the top track maps the evenly spaced SNPs of the triangle to their physical positions. Within blocks |D′| is close to 1 for most pairs, while r² is high only for SNPs that mark the same haplotypes; both drop at the hotspots. A few tag SNPs per block capture most of the variation](./plots/ld-blocks.py)

## 25.3. Genome-Wide Association Studies

### 25.3.1. Design and the Single-SNP Test

**Definition 25.3.1 (Genome-Wide Association Study)** A **genome-wide association study** (GWAS) tests genetic variants across the whole genome, typically $10^6$–$10^7$ SNPs genotyped on arrays and imputed, or obtained by sequencing, for association with a trait in a sample of individuals: for a disease, by comparing allele frequencies between cases and controls; for a quantitative trait, by regressing the trait on allele counts.

The first GWAS (age-related macular degeneration, 2005; the Wellcome Trust Case Control Consortium, 2007) used a few thousand individuals; today's biobanks and consortia analyze millions.

**Formula 25.3.1 (Allelic Test for Case–Control Data)** For a SNP with alleles G and C, arrange the allele counts in a $2 \times 2$ **contingency table** (rows: alleles; columns: cases and controls; each person contributes two alleles). Under the **null hypothesis** of equal allele frequencies, $E = (\text{row total})(\text{column total})/(\text{grand total})$ for each cell and

$$
X^2 = \sum_{\text{cells}} \frac{(O - E)^2}{E} \;\overset{H_0}{\approx}\; \chi^2_1. \tag{25.2}
$$

This is the χ² **test of independence** ([3.2.6](/3.2.6#sec-6.4)). It assumes Hardy–Weinberg proportions (so that the two alleles of a person are independent); the Cochran–Armitage trend test on genotype counts, or **logistic regression** of disease status on allele count with covariates, avoids that assumption and is used in practice.

**Definition 25.3.2 (Odds Ratio)** The **odds ratio** of an allele is the ratio of the odds of carrying it in cases to the odds in controls,

$$
\mathrm{OR} = \frac{a/b}{c/d} = \frac{ad}{bc}, \qquad \operatorname{SE}(\ln\widehat{\mathrm{OR}}) = \sqrt{\frac1a + \frac1b + \frac1c + \frac1d}, \tag{25.3}
$$

with $a, b$ the counts of the risk and other allele in cases and $c, d$ in controls. For a rare disease it approximates the relative risk per copy of the allele; $\mathrm{OR} = 1$ means no association.

**Example 25.3.1** In a study of coronary heart disease with 3848 case and 5872 control chromosomes at one SNP, cases carry 2132 C and 1716 G alleles ($55.4\,\%$ C) and controls 2783 C and 3089 G ($47.4\,\%$ C). The expected counts under independence are, for G, $4805 \cdot 3848/9720 = 1902$ in cases and $2903$ in controls, and for C, $1946$ and $2969$. Then

$$
X^2 = \frac{(1716 - 1902)^2}{1902} + \frac{(3089 - 2903)^2}{2903} + \frac{(2132 - 1946)^2}{1946} + \frac{(2783 - 2969)^2}{2969} = 18.2 + 11.9 + 17.8 + 11.7 = 59.7,
$$

with $p = 1.1 \times 10^{-14}$. The odds ratio of C is $(2132 \cdot 3089)/(1716 \cdot 2783) = 1.38$, with $95\,\%$ confidence interval $\exp(\ln 1.38 \pm 1.96 \cdot 0.042) = (1.27, 1.50)$. An odds ratio of $1.2$–$1.4$ per allele is typical of the strongest common-variant associations of common diseases.

### 25.3.2. Multiple Testing and Genome-Wide Significance

A GWAS performs about a million tests, so a nominal level of $0.05$ would give some 50 000 false positives.

**Formula 25.3.2 (Genome-Wide Significance)** The conventional genome-wide significance threshold is

$$
p < 5 \times 10^{-8} \approx \frac{0.05}{10^6}, \tag{25.4}
$$

a **Bonferroni correction** ([3.2.4](/3.2.4#sec-4.4.2)) for about one million independent common-variant tests in the genome of a population of European ancestry (correlated SNPs in LD count as fewer independent tests). It corresponds to $X^2 > 29.7$ ($|z| > 5.45$). Suggestive associations ($p < 10^{-5}$) are carried forward to replication.

The threshold controls the **family-wise error rate** and is conservative; the **false discovery rate** is used for follow-up and for omics data. In addition, every association must be replicated in an independent sample, because the effect estimate of a SNP selected for passing a stringent threshold is biased upward (the winner's curse): among many SNPs with similar true effects, those that pass the threshold are the ones whose estimates happened to be high. Replication samples should therefore be larger than a naive calculation based on the discovery estimate suggests.

### 25.3.3. Manhattan and QQ Plots, Inflation and Stratification

GWAS results are displayed in a Manhattan plot, $-\log_{10} p$ for each SNP against its genome position, with chromosomes in alternating colors: associations appear as towers of SNPs in LD with a causal variant, rising above the significance line. The QQ plot compares the ordered observed $-\log_{10} p$ with their **expectation** under the null ($-\log_{10}$ of the uniform **order statistics** $(i - 0.5)/n$): a null scan follows the diagonal, true associations depart from it only in the extreme tail, and a systematic departure over the whole range signals inflation.

**Definition 25.3.3 (Population Stratification and Genomic Inflation Factor)** **Population stratification** is the presence in a study sample of subpopulations that differ both in allele frequencies and in the frequency of the trait (or its mean); it creates associations at every SNP whose frequency differs between the subpopulations, whether or not it influences the trait. The **genomic inflation factor** is

$$
\lambda_{\mathrm{GC}} = \frac{\operatorname{median}(X^2_j)}{0.455}, \tag{25.5}
$$

the **median** of the observed 1-df **test statistics** divided by the median of $\chi^2_1$; $\lambda_{\mathrm{GC}} \approx 1$ indicates no systematic inflation.

The classic illustration is a fictional "gene for chopstick use" found in a sample of San Francisco residents: any allele more common in people of East Asian ancestry would be associated with the trait. Stratification is controlled by design (matched cases and controls, family-based tests such as the transmission disequilibrium test, which compares transmitted with untransmitted parental alleles) and by analysis: the top principal components of the genotype matrix capture ancestry (**principal component analysis**, [3.4.5](/3.4.5)) and are included as covariates (Price and colleagues 2006); linear mixed models include a random effect whose **covariance** is the genomic relatedness matrix, which also accounts for cryptic relatedness. Genomic control divides all test statistics by $\lambda_{\mathrm{GC}}$.

For highly polygenic traits in very large samples, $\lambda_{\mathrm{GC}}$ exceeds 1 even without stratification, because thousands of SNPs carry small true effects. LD score regression (Bulik-Sullivan and colleagues 2015) separates the two: under polygenicity, a SNP's expected statistic increases with its LD score $\ell_j = \sum_k r^2_{jk}$ (the amount of genome it tags),

$$
\mathbb{E}[X^2_j] = 1 + \frac{N h^2_{\mathrm{SNP}}}{M}\,\ell_j + Na, \tag{25.6}
$$

whereas stratification adds a constant $Na$ (the intercept) unrelated to LD. The slope estimates the SNP heritability (§25.5).

![A simulated GWAS (4000 cases and 4000 controls, about 5900 SNPs on 12 chromosomes; four causal variants with odds ratios 1.2–1.35, each tagged by neighboring SNPs in LD). A: Manhattan plot; solid line: genome-wide significance 5 × 10⁻⁸; dotted: suggestive 10⁻⁵; red: the causal SNPs. Three loci reach significance; the weakest (chromosome 2) does not, an example of limited power. B: QQ plot with the 95 % band of the null: the p-values follow the diagonal except for the tail of true associations (λ_GC ≈ 1). C: the same design with 60 % of the cases but only 40 % of the controls drawn from one of two subpopulations that differ slightly in allele frequency (F_ST = 0.0005): the whole distribution is inflated (λ_GC ≈ 1.28), the signature of stratification](./plots/gwas-scan.py)

### 25.3.4. Power

**Formula 25.3.3 (Power of a Quantitative-Trait GWAS)** For a SNP with **allele frequency** $p$ and **additive effect** $\beta$ per allele on a trait with variance $\sigma^2$, the fraction of variance it explains is $q^2 = 2pq\beta^2/\sigma^2$, and in $N$ unrelated individuals the 1-df test statistic is approximately noncentral $\chi^2_1$ with **noncentrality parameter**

$$
\lambda = N q^2 = \frac{N\cdot 2pq\beta^2}{\sigma^2}. \tag{25.7}
$$

Power at threshold $\alpha$ is $\mathbb{P}(\chi^2_1(\lambda) > \chi^2_{1,\alpha})$; for $80\,\%$ power at $5 \times 10^{-8}$, $\lambda \approx (5.45 + 0.84)^2 = 39.6$.

**Example 25.3.2** A variant explaining $0.1\,\%$ of the variance of a trait ($q^2 = 0.001$) requires $N \approx 39.6/0.001 \approx 40\,000$ individuals for $80\,\%$ power; one explaining $0.02\,\%$ requires about $200\,000$. This is why the yield of GWAS grew with **sample size** almost without limit: for height, $\approx 180$ significant loci in $180\,000$ people (2010), $\approx 700$ in $700\,000$ (2018) and more than 12 000 independent signals in 5.4 million (2022). For case–control studies the noncentrality also depends on prevalence and case fraction; balanced designs maximize power for a given total.

![Power of a genome-wide association test (1 df, p < 5 × 10⁻⁸) against sample size, for variants explaining fractions q² = 0.5 %, 0.1 %, 0.02 % and 0.01 % of trait variance (Formula 25.3.3). Dashed: the same variants detected through a tag SNP with r² = 0.5, which halves the effective sample size (Formula 25.2.1); dotted: 80 % power](./plots/gwas-power.py)

## 25.4. From Signal to Gene

### 25.4.1. Statistical Fine-Mapping

A significant locus usually contains dozens of SNPs in LD with each other, any of which might be causal, and often several independent signals. Statistical fine-mapping assigns each SNP a probability of being causal.

**Definition 25.4.1 (Fine-Mapping and Credible Set)** **Fine-mapping** is the identification of the causal variant(s) underlying an association signal among the variants in LD with the lead SNP. A $95\,\%$ **credible set** is a smallest set of variants whose posterior probabilities of being causal sum to at least $0.95$; the posterior inclusion probability (PIP) of a variant is its posterior probability of being causal.

**Formula 25.4.1 (Single-Causal-Variant Fine-Mapping)** Assume one causal variant in the region, equal prior probabilities, and approximately normal effect estimates $\hat\beta_j$ with variance $V_j$ and a normal prior $\mathcal{N}(0, W)$ for a causal effect. Then the posterior probability that variant $j$ is causal is proportional to its approximate **Bayes factor** (Wakefield 2009),

$$
\mathrm{PIP}_j = \frac{\mathrm{ABF}_j}{\sum_k \mathrm{ABF}_k}, \qquad \mathrm{ABF}_j = \sqrt{1 - \rho_j}\,\exp\!\left(\frac{\rho_jz_j^2}{2}\right), \quad \rho_j = \frac{W}{V_j + W}, \tag{25.8}
$$

where $z_j = \hat\beta_j/\sqrt{V_j}$. With equal **standard errors**, the PIPs depend only on the $z$ scores.

**Example 25.4.1** Four SNPs in a locus have $z = 6.0$, $5.9$, $5.5$ and $3.0$ (standard error $0.02$, prior SD $0.2$, so $\rho = 0.990$). The **Bayes factors** are proportional to $\exp(0.495z^2)$, and the PIPs are $0.62$, $0.34$, $0.036$ and $10^{-6}$. The $95\,\%$ credible set contains the first two SNPs (cumulative $0.96$): the data cannot distinguish two SNPs in strong LD, however large the sample. Methods with multiple causal variants (such as SuSiE), functional annotations as priors, and populations with different LD (trans-ancestry fine-mapping) shrink credible sets further.

### 25.4.2. Functional Follow-Up: eQTLs and the *FTO* Locus

About $90\,\%$ of GWAS signals lie outside protein-coding sequences, mostly in **enhancers** active in trait-relevant cell types ([7.2.15](/7.2.15)); they act by changing gene regulation.

**Definition 25.4.2 (Expression Quantitative Trait Locus)** An **expression quantitative trait locus** (eQTL) is a genetic variant associated with the expression level of a gene, measured by RNA abundance in a tissue; it is cis-acting when near the gene (typically within $1\,\mathrm{Mb}$) and trans-acting when elsewhere. Colocalization analysis tests whether a GWAS signal and an eQTL share the same causal variant, which links a noncoding association to a target gene.

**Example 25.4.2 (*FTO*, *IRX3* and *IRX5*)** The strongest common-variant association with obesity lies in the first **intron** of *FTO*: each risk allele adds about $0.4\,\mathrm{kg/m^2}$ to body mass index, and **homozygotes** weigh about $3\,\mathrm{kg}$ more than non-carriers. For years the obvious hypothesis was that *FTO*, an RNA demethylase, was the gene. **Chromatin** conformation and eQTL studies showed instead that the intronic region is an enhancer that contacts, over hundreds of kilobases, the **promoters** of *IRX3* and *IRX5*. Claussnitzer and colleagues (2015) identified the causal variant rs1421085: its risk allele T→C disrupts a binding site of the **repressor** ARID5B, so that the enhancer becomes more active in adipocyte precursors, *IRX3* and *IRX5* are expressed more, and developing fat cells shift from energy-dissipating beige ("browning") to energy-storing white function. Editing the single nucleotide in human cells reversed the effect. The lesson is general: the nearest gene is not necessarily the target, and the path from association to mechanism requires regulatory genomics and experiment.

### 25.4.3. Mendelian Randomization

Associations between a modifiable exposure (LDL **cholesterol**, alcohol, body mass index) and a disease in observational data may be confounded or reflect reverse causation. Because alleles are assigned at random at **meiosis**, independently of most environmental factors ([7.4.2](/7.4.2)), genetic variants that influence the exposure can serve as natural experiments.

**Definition 25.4.3 (Mendelian Randomization)** **Mendelian randomization** (MR) is the use of genetic variants as instrumental variables to estimate the causal effect of an exposure $X$ on an outcome $Y$ from observational data. A variant $G$ is a valid instrument if (1) it is associated with $X$ (relevance); (2) it is independent of the confounders of the $X$–$Y$ relation (independence); (3) it affects $Y$ only through $X$ (exclusion restriction, no horizontal **pleiotropy**).

**Formula 25.4.2 (Wald Ratio)** If $\hat\beta_{GX}$ is the effect of the variant on the exposure and $\hat\beta_{GY}$ its effect on the outcome, the causal effect of $X$ on $Y$ is estimated by

$$
\hat\beta_{XY} = \frac{\hat\beta_{GY}}{\hat\beta_{GX}}, \qquad \operatorname{SE}(\hat\beta_{XY}) \approx \frac{\operatorname{SE}(\hat\beta_{GY})}{|\hat\beta_{GX}|}. \tag{25.9}
$$

With many independent variants, the ratio estimates are combined by inverse-variance weighting; methods robust to some invalid instruments (MR-Egger, weighted median) test for pleiotropy.

**Example 25.4.3** A variant raises LDL cholesterol by $0.1\,\mathrm{SD}$ per allele and increases the log odds of coronary heart disease by $0.02$ per allele (standard error $0.004$). The Wald ratio is $0.02/0.1 = 0.2$ log odds (odds ratio $1.22$) per SD of LDL, with standard error $0.04$. MR studies of this kind, together with trials, established LDL as causal, and showed that HDL cholesterol, though inversely correlated with heart disease, is probably not causal; drugs that raised HDL failed in trials. Variants in the genes encoding drug targets (*HMGCR* for **statins**, *PCSK9*) mimic lifelong inhibition of the protein, and genetic support for a target roughly doubles the probability that a drug succeeds in clinical development, the reason why GWAS and MR are now part of drug discovery.

## 25.5. SNP Heritability, Missing Heritability and Rare Variants

**Definition 25.5.1 (SNP Heritability and Missing Heritability)** The **SNP heritability** $h^2_{\mathrm{SNP}}$ is the proportion of phenotypic variance explained jointly by all genotyped (or imputed) SNPs, in an additive model in which every SNP has an effect. **Missing heritability** is the difference between the heritability estimated from family or twin studies ([7.4.24](/7.4.24)) and the variance explained by associated variants, originally by the genome-wide significant ones only.

When the first GWAS of height found loci explaining a few percent of the variance of a trait with $h^2 \approx 0.8$, the gap seemed paradoxical. Yang and colleagues (2010) estimated $h^2_{\mathrm{SNP}}$ without identifying the loci, by relating the phenotypic similarity of pairs of unrelated people to their genomic similarity (genome-based restricted maximum likelihood, GREML): the genomic relationship matrix $A_{ik} = \frac1M\sum_j (x_{ij} - 2p_j)(x_{kj} - 2p_j)/(2p_jq_j)$ replaces the **pedigree** relationship in the covariance $\operatorname{Cov}(y_i, y_k) = A_{ik}h^2_{\mathrm{SNP}}\sigma^2$ ([7.4.24](/7.4.24), Formula 24.4.1). For height, common SNPs explained about $45\,\%$ of the variance, most of the missing heritability: it was hidden in thousands of variants each too small to reach significance. LD score regression, Eq. (25.6), gives similar estimates from summary statistics. The remaining gap is explained by rare variants poorly tagged by arrays (whole-genome sequencing recovers most of it for height) and partly by overestimation in twin studies (nonadditive effects, shared environment).

The resulting picture is that complex traits are extremely polygenic: for height, the $12\,000$ independent genome-wide significant signals cluster in about $20\,\%$ of the genome and explain $40$–$50\,\%$ of the variance in people of European ancestry. The omnigenic model (Boyle, Li and Pritchard 2017) proposes an explanation: because regulatory networks are highly interconnected, essentially every gene expressed in the relevant cells affects the "core genes" of the trait indirectly through trans effects, so that most heritability comes from many peripheral genes rather than from the core pathway.

**Definition 25.5.2 (Burden Test)** A **burden test** tests the combined effect of rare variants (typically minor allele frequency below $1\,\%$, often only predicted loss-of-function or damaging missense variants) in a gene by collapsing them into one score per individual, $B_i = \sum_{j \in \text{gene}} w_jx_{ij}$, and testing the association of $B_i$ with the trait.

Rare variants are individually too infrequent for single-variant tests, and collapsing them by gene recovers power when most of them act in the same direction. **Exome sequencing** of hundreds of thousands of biobank participants (UK Biobank) has found genes in which rare loss-of-function variants have large effects (for example *PCSK9* and LDL, *GPR75* and obesity, which protects **carriers**), bridging the gap between Mendelian and complex genetics. Variance-component tests (SKAT) allow effects in both directions.

## 25.6. Polygenic Scores

**Definition 25.6.1 (Polygenic Score)** A **polygenic score** (PGS, polygenic risk score for diseases) is a weighted sum of an individual's allele counts at many variants,

$$
\mathrm{PGS}_i = \sum_{j=1}^M \hat\beta_jx_{ij}, \tag{25.10}
$$

where $x_{ij} \in \{0, 1, 2\}$ and the weights $\hat\beta_j$ are effect estimates from a GWAS in an independent sample, either for genome-wide significant SNPs only or, better, for all SNPs with shrinkage that accounts for LD (clumping and thresholding, LDpred, PRS-CS). It estimates the individual's **breeding value** for the trait (Definition 24.3.2, [7.4.24](/7.4.24)).

**Formula 25.6.1 (Expected Accuracy of a Polygenic Score)** If a trait has SNP heritability $h^2$ spread over $M_e$ independent effective chromosome segments, and the weights come from a GWAS of $N$ individuals, the expected squared correlation between score and phenotype in a new sample of the same ancestry is approximately (Daetwyler and colleagues 2008)

$$
R^2 \approx \frac{h^2}{1 + M_e/(Nh^2)}. \tag{25.11}
$$

$R^2$ approaches $h^2$ only when $N \gg M_e/h^2$; for humans $M_e$ is about $5 \times 10^4$–$10^5$.

**Example 25.6.1** For $h^2 = 0.5$ and $M_e = 60\,000$, a GWAS of $N = 10^5$ gives $R^2 = 0.5/(1 + 60\,000/50\,000) = 0.23$, and $N = 10^6$ gives $0.5/1.12 = 0.45$. For height the best current scores reach $R^2 \approx 0.4$ in people of European ancestry; for most diseases the variance explained on the liability scale is $5$–$15\,\%$.

![Expected accuracy of a polygenic score against GWAS sample size (Formula 25.6.1), for SNP heritability 0.5 and 0.2 with M_e = 60 000 effective independent segments, and for h² = 0.5 with M_e = 20 000; dotted: the ceiling h². Dots: simulations with M_e independent standardized SNPs whose estimated effects are the true effects plus sampling noise of variance 1/N; the score's R² in a new sample, (β̂·β)²/|β̂|², follows the formula](./plots/pgs-accuracy.py)

Three limitations shape the use of polygenic scores.

- Portability. Accuracy falls in populations whose ancestry differs from the GWAS sample, because LD between tag SNPs and causal variants differs, allele frequencies differ, and effects may interact with environment: scores derived from European-ancestry GWAS are about 2 times less accurate in East Asian and 4–5 times less accurate in African-ancestry samples (Martin and colleagues 2019). About $80$–$90\,\%$ of GWAS participants have been of European ancestry, so the inequity is a direct consequence of study design; diverse biobanks are correcting it.
- Within-family effects. Population GWAS estimates include indirect genetic effects (parents' genotypes acting on the child through the environment, "genetic nurture"), **assortative mating** and residual stratification. Within-family (sibling) GWAS remove them; for height the estimates change little, but for educational attainment and cognitive traits the within-family effects are about half of the population estimates.
- Individual prediction. A score shifts risk, it does not determine outcome. For coronary artery disease, the $8\,\%$ of people with the highest scores have about a threefold risk, comparable to a monogenic **familial hypercholesterolemia** **mutation**, which has motivated its use in risk stratification together with conventional risk factors; for breast **cancer**, scores modify the risk of carriers of *BRCA* mutations ([7.4.21](/7.4.21)).

**Example 25.6.2 (Embryo Selection)** Selecting among embryos by a polygenic score is constrained by the within-family variance: siblings share their parents, so the score varies among embryos of one couple with only half of its population variance. If a score explains $R^2 = 0.25$ of height (SD $7\,\mathrm{cm}$), the score among embryos has SD $7\sqrt{0.25/2} = 2.5\,\mathrm{cm}$, and choosing the highest of 10 embryos gains on average $1.54 \cdot 2.5 = 3.8\,\mathrm{cm}$ (the expected maximum of 10 standard normals is $1.54$); for $R^2 = 0.1$ the gain is $2.4\,\mathrm{cm}$, before accounting for the attenuation in other ancestries, the small number of viable embryos and pleiotropic effects on other traits. For diseases the absolute risk reductions are small. Professional societies have judged embryo selection on polygenic scores to be unproven, and it raises ethical questions about eugenics and inequality that the genetics alone cannot answer.

## Summary

| Method | Population | Key quantities | Resolution |
|---|---|---|---|
| single-marker test (cross) | backcross, F₂ | class difference $(1 - 2r)\delta$ (Formula 25.1.1) | confounds effect and position |
| interval mapping | backcross, F₂, RILs | LOD$(x) = \tfrac n2\log_{10}(\mathrm{RSS}_0/\mathrm{RSS}_1)$, permutation threshold, 1.5-LOD interval (Algorithm 25.1.1) | $10$–$30\,\mathrm{cM}$ |
| NIL fine mapping | congenic lines | recombinants in the interval, $nd$ | gene level (*fw2.2*) |
| association mapping / GWAS | unrelated individuals | allelic χ² (Formula 25.3.1), OR $= ad/bc$ (Definition 25.3.2), $p < 5 \times 10^{-8}$ (Formula 25.3.2) | LD block, $10$–$100\,\mathrm{kb}$ |

- Indirect association: power at a tag with LD $r^2$ equals power at the causal variant with $r^2N$ (Formula 25.2.1); tag SNPs and imputation exploit haplotype blocks.
- Quality and confounding: Manhattan and QQ plots; $\lambda_{\mathrm{GC}} = \operatorname{median}X^2/0.455$; stratification controlled by principal components and mixed models (Definition 25.3.3); LD score regression separates polygenicity (slope) from confounding (intercept), Eq. (25.6).
- Power: $\lambda = N\cdot 2pq\beta^2/\sigma^2$, $\lambda \approx 39.6$ for $80\,\%$ power at $5 \times 10^{-8}$ (Formula 25.3.3); winner's curse requires replication.
- From signal to gene: credible sets from approximate Bayes factors (Formula 25.4.1); eQTL colocalization; *FTO* acts through *IRX3*/*IRX5*; Mendelian randomization with the Wald ratio $\beta_{GY}/\beta_{GX}$ under three instrument assumptions (Definition 25.4.3, Formula 25.4.2).
- Heritability: $h^2_{\mathrm{SNP}}$ by GREML or LD score regression recovers most missing heritability; complex traits are extremely polygenic (omnigenic model); rare variants by burden tests (Definition 25.5.2).
- Polygenic scores: $\mathrm{PGS} = \sum\hat\beta_jx_j$; $R^2 \approx h^2/(1 + M_e/Nh^2)$ (Formula 25.6.1); limited portability across ancestries, inflated by indirect effects, informative for risk stratification but weak for individual prediction and embryo selection.

## Questions

1. In a backcross, the two classes of a marker have mean trait values $52.0$ and $48.4$, and the marker is estimated to be $15\,\mathrm{cM}$ from the QTL. (a) Estimate the QTL effect, using the Haldane **mapping function**. (b) Why is interval mapping preferable to this calculation?

   **Answer** (a) $r = \tfrac12(1 - \mathrm{e}^{-0.3}) = 0.130$; $\delta = 3.6/(1 - 0.259) = 4.86$. (b) The distance is unknown in practice; with one marker the effect and distance cannot be separated, whereas interval mapping uses both flanking markers to estimate position and effect jointly and provides a likelihood-based support interval.

2. Explain why the genome-wide LOD threshold obtained by permutation is higher than the threshold for a single test at a pre-specified position. What would happen to the threshold if the marker density were doubled?

   **Answer** The genome-wide threshold controls the probability that the maximum over all positions exceeds it under the null; scanning many correlated positions makes a high maximum more likely by chance, so the quantile of the maximum is above the single-test quantile. Doubling marker density adds positions that are highly correlated with existing ones (neighboring positions share most recombination information), so the threshold rises only slightly, approaching a limit set by the genome length and the number of meioses.

3. A QTL has been placed in a $2\,\mathrm{cM}$ interval. How many backcross plants must be screened to expect 10 recombinants within the interval, and with what probability does a sample of 200 contain at least one?

   **Answer** Expected recombinants $= nd$ with $d = 0.02$: $n = 500$. With $n = 200$, the number is approximately Poisson with mean 4: $\mathbb{P}(\geq 1) = 1 - \mathrm{e}^{-4} = 0.98$.

4. In a case–control study of 2000 cases and 2000 controls, the risk allele has 1400 copies among the case chromosomes and 1200 among the controls. Compute the allelic χ², the **p-value** and the odds ratio. Is the result genome-wide significant?

   **Answer** Table: cases 1400 / 2600, controls 1200 / 2800 (of 4000 chromosomes each). Row totals 2600 and 5400, grand total 8000; expected risk-allele counts 1300 and 1300, others 2700 and 2700. $X^2 = 100^2/1300 \cdot 2 + 100^2/2700 \cdot 2 = 15.38 + 7.41 = 22.8$, $p = 1.8 \times 10^{-6}$. OR $= (1400 \cdot 2800)/(2600 \cdot 1200) = 1.26$. Not genome-wide significant ($p > 5 \times 10^{-8}$), but suggestive; it should be tested in a replication sample.

5. Why is the genome-wide threshold $5 \times 10^{-8}$ and not $0.05$ divided by the number of SNPs on the array? Would the threshold be different for a study in an African population?

   **Answer** Many SNPs on an array (or after imputation, many millions) are in strong LD and their tests are not independent; the effective number of independent common-variant tests in European-ancestry genomes was estimated at about one million, giving $0.05/10^6$. African populations have shorter LD (older, larger populations) and therefore more independent tests; a stricter threshold (about $10^{-8}$ or lower) has been proposed for them and for whole-genome sequencing studies that include rare variants.

6. A GWAS reports a median 1-df statistic of $0.52$. (a) Compute $\lambda_{\mathrm{GC}}$. (b) Give two explanations and say how LD score regression would distinguish them.

   **Answer** (a) $\lambda_{\mathrm{GC}} = 0.52/0.455 = 1.14$. (b) Population stratification or cryptic relatedness (confounding), or true polygenic signal in a large sample. LD score regression regresses the statistics on LD scores: polygenicity produces a slope (SNPs that tag more of the genome carry more signal), confounding an intercept above 1; an intercept near 1 with a positive slope indicates polygenicity.

7. A SNP with allele frequency $0.4$ has an additive effect of $0.02$ **standard deviations** per allele. (a) What fraction of the trait variance does it explain? (b) What sample size gives $80\,\%$ power at $5 \times 10^{-8}$? (c) How does the answer change if only a tag SNP with $r^2 = 0.6$ is typed?

   **Answer** (a) $q^2 = 2 \cdot 0.4 \cdot 0.6 \cdot 0.02^2 = 1.92 \times 10^{-4}$. (b) $N = 39.6/1.92 \times 10^{-4} = 206\,000$. (c) The **effective sample size** is $0.6N$, so $N = 206\,000/0.6 = 344\,000$.

8. Explain the winner's curse. Why does a replication study designed with the effect size estimated in the discovery GWAS tend to be underpowered?

   **Answer** Among many variants with small true effects, those that cross a stringent significance threshold in the discovery sample are disproportionately those whose sampling errors happened to be positive; their estimated effects are biased upward, more so when power is low. A replication sample sized for the inflated effect is too small for the true effect; replication should use conservative effect estimates (bias-corrected, or the **lower confidence limit**) or much larger samples.

9. Four SNPs in an associated region have $z$ scores $7.0$, $6.8$, $4.0$, $1.0$, with equal standard errors and $\rho = 0.99$ in Eq. (25.8). Compute the PIPs and the $95\,\%$ credible set.

   **Answer** $\mathrm{ABF} \propto \exp(0.495z^2)$: exponents $24.26$, $22.89$, $7.92$, $0.50$. Relative to the first: $1$, $\mathrm{e}^{-1.37} = 0.254$, $\mathrm{e}^{-16.3} \approx 8 \times 10^{-8}$, negligible. PIPs: $0.797$, $0.203$, $\approx 10^{-7}$, $\approx 0$. The $95\,\%$ credible set is the first two SNPs (cumulative $1.00$; the first alone gives $0.80 < 0.95$).

10. A variant increases body mass index by $0.08\,\mathrm{SD}$ per allele and the log odds of **type 2 diabetes** by $0.04$ per allele (SE $0.006$). (a) Estimate the causal effect of BMI on diabetes by the Wald ratio, with its standard error. (b) Which assumption would be violated if the variant also acted directly on **insulin** secretion in pancreatic cells?

    **Answer** (a) $\hat\beta = 0.04/0.08 = 0.5$ log odds per SD of BMI (odds ratio $1.65$), SE $\approx 0.006/0.08 = 0.075$. (b) The exclusion restriction (no horizontal pleiotropy): the variant would affect the outcome through a path other than the exposure, biasing the estimate; methods using many instruments (MR-Egger, weighted median) can detect and partly correct this.

11. A trait has SNP heritability $0.5$ and $M_e = 60\,000$. (a) What GWAS sample size gives a polygenic score with $R^2 = 0.25$? (b) What is the ceiling of $R^2$, and why might the observed $R^2$ in another ancestry be much lower?

    **Answer** (a) $0.25 = 0.5/(1 + 60\,000/0.5N)$ gives $1 + 120\,000/N = 2$, $N = 120\,000$. (b) The ceiling is $h^2_{\mathrm{SNP}} = 0.5$. In another ancestry, LD between tag SNPs and causal variants differs, allele frequencies differ (some variants are rare or absent), and effects may differ through interactions with environment and genetic background, so the score captures less of the genetic variance.

12. For embryo selection on a polygenic score with $R^2 = 0.1$ for a trait with SD $\sigma$, compute the expected gain from choosing the best of 5 embryos (expected maximum of 5 standard normals: $1.16$). Why is the within-family variance used?

    **Answer** Among siblings the score has variance $\tfrac12R^2\sigma^2$ (half of the population variance of breeding values is within families, the Mendelian sampling variance), SD $\sigma\sqrt{0.05} = 0.224\sigma$. Gain $= 1.16 \cdot 0.224\sigma = 0.26\sigma$ (about $1.8\,\mathrm{cm}$ for height). Only the within-family variation can be selected among embryos of one couple; the parents' contribution is fixed.

13. Why did most GWAS signals turn out to be noncoding, and what evidence links a noncoding signal to a gene? Illustrate with *FTO*.

    **Answer** Coding variants with large effects on common traits are kept rare by purifying selection ([7.4.23](/7.4.23)); regulatory variants have smaller, often cell-type-specific effects and can be common. Evidence: overlap of the credible set with enhancers in relevant cells, colocalization with eQTLs, chromatin contacts with promoters, and experimental editing. At *FTO* the intronic risk region contacts *IRX3*/*IRX5*; the risk allele of rs1421085 disrupts an ARID5B repressor site, raises *IRX3*/*IRX5* expression in adipocyte precursors and shifts them from beige to white fat; editing the base reverses the phenotype.

14. (Open question.) Compare QTL mapping in a cross with GWAS in a natural population in terms of power to detect a locus, resolution, the range of alleles studied and confounding.

    **Answer** A cross has high power per individual for loci where the two parents differ (allele frequencies $1/2$, no LD decay to weaken signals, effects often large), little confounding (randomization by Mendelian segregation within the cross) but poor resolution ($10$–$30\,\mathrm{cM}$, few meioses) and only the alleles of the two parents. GWAS samples many alleles and their natural frequencies, and has fine resolution because of historical recombination, but needs dense markers and very large samples (small effects, LD dilution, rare alleles), and is vulnerable to population stratification and indirect effects. Multiparent crosses and wild-population GWAS in **model organisms** combine features of both.
