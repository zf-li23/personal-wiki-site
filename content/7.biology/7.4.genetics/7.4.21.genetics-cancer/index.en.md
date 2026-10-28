---
title: The Genetics of Cancer
description: "Cancer from the point of view of genetic analysis. Clonal origin shown by X-inactivation mosaics and shared breakpoints; the multistage model and the Armitage–Doll power law; driver and passenger mutations, mutational signatures and tumor mutational burden; how oncogenes were found by transformation assays and how they are activated; tumor suppressor genes, the quantitative form of Knudson's two-hit model for hereditary and sporadic retinoblastoma, and the five mechanisms of loss of heterozygosity; hereditary cancer syndromes, penetrance and Bayesian risk in pedigrees, variants of uncertain significance; the genetic logic of targeted therapy and synthetic lethality."
---

**Cancer** is a genetic disease of somatic cells: it arises from **mutations** in a cell lineage, and the clone that descends from the first altered cell accumulates further mutations and is selected for growth. The **cell biology** of the disease (its hallmarks, the pathways involved, the microenvironment and the main treatments) is the subject of [7.3.26](/7.3.26), where the **two-hit hypothesis**, the Armitage–Doll multistage model, **clonal evolution**, **driver mutation**s and **synthetic lethality** are defined. This chapter takes the complementary view: what the genetic methods of the preceding chapters say about **tumors** and about the families in which cancer runs. The evidence for clonal origin comes from X-inactivation mosaics ([7.4.6](/7.4.6#sec-6.5.1)); the number of rate-limiting steps is read off an incidence curve; **oncogene**s were found by a transformation assay that is a **transformation** experiment in the genetic sense; **tumor suppressor gene**s were found in **pedigrees** and mapped by **loss of heterozygosity**, whose mechanisms are those of [7.4.9](/7.4.9) and [7.4.15](/7.4.15); and the risks quoted to families are the conditional probabilities of [7.4.7](/7.4.7). The **cell cycle** and checkpoint machinery that the mutated **genes** control is treated in [7.3.20](/7.3.20) and [7.3.22](/7.3.22).

## 21.1. Cancer Is Clonal and Multistep

### 21.1.1. The Evidence for a Clonal Origin

If a tumor grows from one transformed cell, all its cells share that cell's **genotype** and any epigenetic mark it carried; if instead many cells responded together to a stimulus, the tumor would be a mixture. The decisive argument came from a genetic mosaic. In a woman heterozygous for two electrophoretically distinguishable **alleles** of the **X-linked** gene for glucose-6-phosphate dehydrogenase, **X-chromosome inactivation** makes each somatic cell express one allele or the other, and normal tissue is a patchwork of both. Linder and Gartler (1965) found that uterine leiomyomas express only one of the two forms, and each tumor of the same woman may express a different one: every tumor descends from a single cell. Three later lines of evidence agree: all cells of a chronic myeloid **leukemia** share one breakpoint of the *BCR*–*ABL1* fusion, to the **base pair**; all cells of a B-cell **lymphoma** share one rearrangement of the immunoglobulin genes made by **V(D)J recombination** ([7.2.9](/7.2.9#sec-9.7)); and sequencing shows that the mutations of a tumor form a single phylogeny with a common trunk.

Clonality does not mean homogeneity. By the time a tumor is detected it contains about $10^9$ cells and many subclones ([7.3.26](/7.3.26#sec-26.2.3)); the trunk of its phylogeny is what all cells share, and the branches are what distinguishes the subclones.

### 21.1.2. Reading the Number of Steps off an Incidence Curve

That cancer needs several mutations in one lineage is an inference from the shape of its age-specific incidence, which is the quantitative core of the multistage model. The multistage model of [7.3.26](/7.3.26#fml-26.2.1) gives the hazard for $k$ rate-limiting steps as $h(t) \propto t^{k-1}$, so that a log–log plot of incidence against age has slope $k - 1$. Epidemiological data give slopes of about 4–6 for the common **carcinomas**, which suggests five to seven steps; the same analysis gives slope 1 for the hereditary and 2 for the sporadic form of retinoblastoma (21.3.2), the cleanest case because the tumor arises from a small, short-lived population of cells.

**Example 21.1.1** The incidence of colorectal cancer rises about 1000-fold between ages 30 and 80. (a) On a log–log plot, $\log(1000)/\log(80/30) = 3/0.426 = 7.0$, so the slope is about 7 and $k \approx 8$. (b) If one step is made ten times faster (by a mutator **phenotype** or a **carcinogen**), the incidence at any age is multiplied by 10, since $h$ is proportional to the product of the rates. (c) If instead an inherited mutation removes one step, the incidence becomes proportional to $t^{k-2}$: at age 40 the ratio of hereditary to sporadic incidence is roughly $k/(\mu t)$, a large number, which is why hereditary cancers appear decades earlier.

Two warnings belong with the inference. Clonal expansion between mutational steps mimics extra steps ([7.3.26](/7.3.26#sec-26.2.2)), so $k$ estimated from the slope is an upper bound on the number of mutations; and exposures that change with the calendar year (tobacco in the twentieth century) distort age curves measured across birth cohorts.

### 21.1.3. Drivers, Passengers and Signatures

A tumor **genome** typically carries thousands of **somatic mutations**, of which only a few are **driver mutation**s; the rest are passengers, acquired in the lineage without contributing to its growth.

**Definition 21.1.1 (Passenger Mutation and Mutational Signature)** A **passenger mutation** is a somatic mutation present in a tumor that does not contribute to its growth, having been acquired in a cell lineage whose expansion was driven by other mutations. A **mutational signature** is a characteristic distribution of mutation types (for example base substitutions classified by the base changed and its two neighbours) produced by a particular mutagenic process, which can be recognized in the spectrum of mutations of a tumor.

Drivers are distinguished from passengers statistically, not individually: a gene is a candidate driver if it is mutated in more tumors than the local background **mutation rate** predicts, if its mutations cluster at particular **residues** (gain of function) or are spread as nonsense and **frameshift mutations** throughout (loss of function), and if the pattern is reproduced in independent cohorts. Across cancers, several hundred genes are recurrently mutated drivers, and a typical tumor carries a few of them ([7.3.26](/7.3.26#sec-26.4.2)).

Signatures identify causes. Tobacco smoke leaves C→A **transversions**, ultraviolet light C→T **transition**s at adjacent pyrimidines, defective **mismatch repair** an excess of small insertions and deletions at **microsatellite**s, defective **homologous recombination** a characteristic pattern of deletions with microhomology, and ageing a slow accumulation of C→T at CpG dinucleotides from the **deamination** of 5-methylcytosine ([7.4.12](/7.4.12#sec-12.6.1)). The spectra are decomposed into a set of reference signatures by a factorization of the mutation-type-by-tumor matrix, a problem of statistics ([3.5](/3.5)); the biology behind each of them is the chemistry of mutation of [7.2.8](/7.2.8).

The tumor mutational burden varies by three orders of magnitude between cancer types, from a few mutations per megabase in pediatric leukemias to hundreds in melanoma and in tumors with defective **mismatch repair** or polymerase **proofreading**. It matters clinically because tumors with many mutations present more neoantigens and respond better to **immune checkpoint blockade** ([7.3.26](/7.3.26#sec-26.6.4)).

![Mutational processes read from the spectrum of somatic mutations (illustrative values). A: proportions of the six classes of base substitution for four mutational processes — ageing (C>T at CpG from deamination of 5-methylcytosine), tobacco smoke (C>A), ultraviolet light (C>T at dipyrimidines) and defective mismatch repair (C>T and T>C, with an excess of small insertions and deletions that the panel does not show). B: tumor mutational burden, in substitutions per megabase, for several cancer types on a logarithmic scale, spanning three orders of magnitude; tumors above a few tens of mutations per megabase present enough neoantigens to respond to checkpoint blockade more often](./plots/mutational-signatures.py)

## 21.2. Oncogenes

**Definition 21.2.1 (Genetic Behavior of an Oncogene)** An **oncogene** is a **mutant** allele that promotes cancer in a dominant fashion at the level of the cell: one altered copy suffices, because the mutation confers a new or constitutive activity on the gene product. Its normal counterpart is a **proto-oncogene**.

The dominance is what made **oncogenes** findable by a gain-of-function assay. DNA extracted from a human tumor was broken into fragments and introduced into mouse NIH 3T3 fibroblasts; cells that took up a fragment carrying a complete oncogene became transformed, growing as foci above the monolayer, and the human DNA in those foci was recovered by its repetitive sequences. In 1982 the groups of Robert Weinberg, Michael Wigler and Mariano Barbacid identified in this way the first human oncogene, an allele of *HRAS* differing from the normal gene by a single base, which replaces glycine at position 12 and locks the **protein** in its GTP-bound, active state ([7.1.15](/7.1.15)). The experiment is a transformation in the genetic sense, with the transformed phenotype as the selectable marker, and its logic is that of [7.4.10](/7.4.10).

**Proto-oncogenes** are activated in four ways, each with a genetic signature:

| Mechanism | Example | What is seen genetically |
|---|---|---|
| **point mutation** | *KRAS* G12, *BRAF* V600E, *EGFR* in lung cancer | **missense mutations** clustered at one or two **codons** |
| amplification | *MYCN* in neuroblastoma, *ERBB2* (HER2) in breast cancer | increased copy number, visible as double minutes or homogeneously staining regions ([7.4.15](/7.4.15)) |
| chromosomal translocation creating a fusion protein | *BCR*–*ABL1* on the Philadelphia **chromosome** in chronic myeloid leukemia | a **reciprocal translocation** with breakpoints inside two genes |
| chromosomal translocation placing a gene under a new regulatory region | *MYC* to the immunoglobulin heavy-chain **locus** in Burkitt lymphoma | a translocation that leaves the coding sequence intact but changes its expression |

The two kinds of translocation illustrate the difference between a structural and a regulatory change, and both are rearrangements of the sort analyzed in [7.4.15](/7.4.15): the breakpoints are reproducible within a tumor type, which is why they serve as diagnostic markers and as measures of residual disease after treatment.

Activated oncogenes behave as dominant alleles in cells but are almost never inherited: a constitutively active growth signal in the germ line is usually lethal or strongly deleterious in development. The exceptions are informative, such as the *RET* mutations of multiple **endocrine** neoplasia type 2, which are inherited as dominant traits and cause specific endocrine tumors, and activating mutations of *HRAS* and its relatives, which when present in the germ line cause developmental syndromes rather than cancer.

## 21.3. Tumor Suppressor Genes and the Two-Hit Model

### 21.3.1. Recessive in the Cell, Dominant in the Family

**Definition 21.3.1 (Genetic Behavior of a Tumor Suppressor Gene)** A **tumor suppressor gene** is a gene whose loss of function promotes cancer. Its mutant alleles are recessive at the level of the cell, since one functional copy suffices, but a **germline mutation** is transmitted as a dominant predisposition in a family, because the second copy is lost somatically in some of the many cells at risk.

This apparent contradiction, dominant in the pedigree and recessive in the cell, is the central genetic fact about inherited cancer, and it was resolved by Knudson's analysis of retinoblastoma. Children with the hereditary form have an affected parent in about half the families, develop several tumors, usually in both eyes, and do so in the first years of life; children with the sporadic form have one tumor in one eye, later, and no family history. Some patients carry a visible deletion of chromosome 13q14, which located the gene, and the tumors of heterozygous **carriers** lose the remaining normal allele.

Tumor suppressors fall into two functional classes. Gatekeepers (*RB1*, *APC*, *TP53*) restrain proliferation or trigger death directly, and their loss expands the population at risk; caretakers (*BRCA1*, *BRCA2*, the mismatch-repair genes, the *XP* genes) maintain the genome, and their loss raises the mutation rate of every gene ([7.3.26](/7.3.26#sec-26.3.1)). The distinction matters for the arithmetic of the next section: losing a caretaker adds no step to the pathway but multiplies the rates of all the other steps.

### 21.3.2. The Quantitative Form of Knudson's Model

**Formula 21.3.1 (Tumor Counts Under the Two-Hit Model)** Let $N$ be the number of cells at risk (retinoblasts), let each allele of the tumor suppressor be inactivated at rate $\mu$ per cell per year, and let one cell with both alleles inactivated give one tumor. In a carrier of a germline mutation each cell needs one hit, so the number of tumors by age $t$ is Poisson distributed with mean

$$
m_1(t) = N \mu t,
\tag{21.1}
$$

while in a non-carrier two hits are needed in the same cell and

$$
m_2(t) \approx N (\mu t)^2 .
\tag{21.2}
$$

In either case the probability of developing at least one tumor, the **penetrance** at age $t$, is $1 - \mathrm{e}^{-m(t)}$, the probability of bilateral disease (with the cells divided equally between the two eyes) is $(1 - \mathrm{e}^{-m/2})^2$, and the distribution of the number of tumors is $\mathrm{Poi}(m)$.

**Proof** Each cell is an independent trial with a small probability of becoming a tumor: $\mu t$ for the carrier (one hit needed) and approximately $(\mu t)^2$ for the non-carrier (two independent hits during the same period). The number of successes among $N$ cells is binomial with small $p$, hence Poisson with mean $Np$ ([3.1.4](/3.1.4)). The eyes contain $N/2$ cells each and are independent, so each eye is affected with probability $1 - \mathrm{e}^{-m/2}$, and both with the square of that. $\square$

With $N \approx 1.5 \times 10^5$ retinoblasts at risk and $\mu \approx 4 \times 10^{-6}$ per allele per year ([7.3.26](/7.3.26#sec-26.2.2)), a carrier has $m_1 \approx 3$ tumors by age five, so the **penetrance** is $1 - \mathrm{e}^{-3} = 0.95$ and about 64 % of affected carriers have bilateral disease, while a non-carrier has $m_2 \approx 6 \times 10^{-5}$, about one case in 17 000 children, unilateral in nearly every case. These numbers reproduce the clinical picture, and they explain the 90 % penetrance quoted for hereditary retinoblastoma without any special assumption: the missing 10 % are carriers in whom no second hit happened to occur before the retinoblasts stopped dividing.

**Example 21.3.1** (a) The expected number of tumors in a carrier by age 5 is $m_1 = 1.5 \times 10^5 \times 4 \times 10^{-6} \times 5 = 3.0$. (b) The probability of no tumor is $\mathrm{e}^{-3} = 0.050$, so the penetrance is 95 %. (c) Each eye contains $N/2$ cells and is affected with probability $1 - \mathrm{e}^{-1.5} = 0.777$, so both eyes are affected in $0.777^2 = 0.60$ of all carriers, that is $0.60/0.95 = 0.64$ of those who develop any tumor. (d) A sporadic case, needing two hits, has $m_2 = 1.5 \times 10^5 \times (4 \times 10^{-6} \times 5)^2 = 6 \times 10^{-5}$: about one child in 17 000, and the probability of a second, independent tumor in such a child is again $6 \times 10^{-5}$, which is why sporadic cases are unilateral.

A further prediction distinguishes the two forms without any molecular test. The fraction of carriers still free of disease at age $t$ is $\mathrm{e}^{-N\mu t}$, which is a straight line on a semi-logarithmic plot against age, whereas for non-carriers it is $\mathrm{e}^{-N\mu^2t^2}$, a straight line against $t^2$. Knudson's 1971 analysis of 48 cases showed exactly this, and it was the first quantitative argument for the number of events in a human cancer.

![Knudson's two-hit model in quantitative form, Eqs. (21.1) and (21.2), with $N = 1.5 \times 10^5$ retinoblasts and $\mu = 4 \times 10^{-6}$ per allele per year. A: the fraction of children still free of tumors against age, on a logarithmic scale, for a process needing one hit and a process needing two, scaled to the same cumulative risk at age six so that only their shapes are compared: one hit gives a straight line in age, two hits a line that is straight against the square of age, which is the diagnostic Knudson applied to his patients. B: the distribution of the number of tumors in a carrier by age five, Poisson with mean 3, from which the penetrance and the proportion with bilateral disease follow. C: penetrance against age for carriers (left axis) and non-carriers (right axis, a hundred-thousand times smaller), with the 90 % penetrance observed in hereditary retinoblastoma marked](./plots/knudson-model.py)

### 21.3.3. Loss of Heterozygosity

The second hit is usually not a second point mutation: it is the loss of the chromosome region carrying the normal allele, which also removes the **heterozygosity** of any marker in that region.

**Definition 21.3.2 (Loss of Heterozygosity in Tumors)** **Loss of heterozygosity** is the conversion of a heterozygous locus to hemizygosity or homozygosity in a somatic cell, so that one parental allele and the markers linked to it are no longer present; in a tumor from a carrier of a germline mutation in a **tumor suppressor gene**, the allele lost is almost always the normal one.

Five mechanisms produce it, and they are distinguished by what happens to the copy number and to the flanking markers:

| Mechanism | Copy number of the region | Markers lost | Earlier chapter |
|---|---|---|---|
| loss of the whole chromosome by **nondisjunction** | one copy | all markers of the chromosome | [7.4.16](/7.4.16) |
| loss of the chromosome followed by duplication of the remaining one | two copies, both from one parent | all markers of the chromosome | [7.4.16](/7.4.16) |
| **mitotic recombination** between the **centromere** and the gene | two copies | markers from the crossover point to the **telomere** | [7.4.9](/7.4.9#sec-9.5) |
| interstitial deletion | one copy | markers near the gene only | [7.4.15](/7.4.15) |
| **gene conversion**, point mutation or epigenetic silencing of the remaining allele | two copies | none (the allele is present but inactive) | [7.4.9](/7.4.9#sec-9.4.3), [7.4.18](/7.4.18) |

The pattern of markers that lose heterozygosity in a panel of tumors locates the gene: the region common to every tumor's loss contains it. This was how *RB1*, *APC*, *TP53*, *NF1* and many other suppressors were mapped before sequencing, and the same logic now operates on genome-wide arrays and sequence data, where copy-neutral **loss of heterozygosity** (the third and fifth mechanisms) is recognized from the allele ratios of heterozygous markers without any change of copy number. Epigenetic silencing by hypermethylation of a **promoter** **CpG island** counts as a hit under the model but leaves the sequence intact, which is why methylation is tested when no second mutation is found; *MLH1* in sporadic colorectal cancer with **microsatellite** instability is the standard example.

![Five routes to loss of heterozygosity at a tumor suppressor locus in a cell heterozygous for a germline mutation. The chromosome carrying the mutant allele (red, m) and its homolog with the normal allele (blue, +) are drawn with three linked markers. Chromosome loss leaves one copy; loss followed by duplication leaves two identical copies; mitotic recombination between the centromere and the locus makes the region distal to the crossover homozygous while the copy number stays at two; an interstitial deletion removes the normal allele and the markers immediately around it; and a point mutation or promoter methylation inactivates the normal allele without changing any marker. The copy number and the markers that remain heterozygous distinguish the mechanisms in a tumor sample](./plots/loh-mechanisms.py)

## 21.4. Hereditary Cancer in Families

### 21.4.1. Risks and Their Calculation

About 5–10 % of cancers arise in carriers of a germline mutation in a cancer-predisposition gene ([7.3.26](/7.3.26#sec-26.3.1)). The pedigree features that suggest such a family are early age at onset, several affected relatives on one side, multiple primary tumors in one person, bilateral disease in a paired organ, a characteristic combination of cancers, and a tumor rare for the age or sex (male breast cancer). The genes behave as dominant traits with incomplete, age-dependent penetrance, so every risk in the family is a conditional probability of the kind computed in [7.4.7](/7.4.7).

| Syndrome | Gene(s) | Main risks |
|---|---|---|
| hereditary retinoblastoma | *RB1* | retinoblastoma about 90 %, later osteosarcoma |
| hereditary breast and ovarian cancer | *BRCA1*, *BRCA2* | breast about 60–70 % by age 80 for both genes; ovary about 40–45 % (*BRCA1*) and 15–20 % (*BRCA2*) |
| Lynch syndrome | *MLH1*, *MSH2*, *MSH6*, *PMS2* | colorectal 10–50 % and endometrial 10–40 % by age 70, depending strongly on the gene |
| familial adenomatous polyposis | *APC* | hundreds of polyps; colorectal cancer near 100 % without surgery |
| Li–Fraumeni syndrome | *TP53* | about 50 % of carriers develop a cancer by age 40, over 80 % by age 70; **sarcoma**, breast, brain, adrenal |

The ranges are wide because penetrance is estimated from different kinds of family and depends on the gene, the position of the mutation and the rest of the genome; estimates from families ascertained through several affected members are biased upward, and population-based estimates are lower. Modifier loci, measured as a **polygenic score** ([7.4.25](/7.4.25)), shift the risk of a *BRCA1* carrier by tens of percentage points, which is why counseling uses models that combine the mutation, the family history and common variants.

**Algorithm 21.4.1 (Risk for a Relative in a Cancer Family)**

1. Establish the mode of inheritance and the gene, if possible by testing an affected relative first: a negative test in an unaffected person is informative only if the family's mutation is known.
2. Compute the prior probability that the consultand carries the mutation from the transmission chain ($1/2$ per generation from a known carrier).
3. Condition on the evidence: their current age and cancer-free status, using the age-specific penetrance $f(a)$, and any test result with its detection rate (**Bayes' theorem**, [7.4.7](/7.4.7#sec-7.4)).
4. Convert the posterior carrier probability into a risk of disease: multiply by the remaining lifetime penetrance, $\left(f(80) - f(a)\right)/\left(1 - f(a)\right)$ for a carrier now aged $a$ and unaffected.
5. For the children of the consultand, multiply the posterior carrier probability by $1/2$ and then by the penetrance.

**Example 21.4.1** A woman of 45 has a mother with *BRCA1*-associated breast cancer at 42; she is unaffected and has not been tested. Take the penetrance of breast cancer in carriers as 0.25 by age 45 and 0.65 by age 80. (a) Her prior carrier probability is $1/2$. (b) Conditioning on being unaffected at 45: the posterior is
$$
\frac{0.5 \times (1 - 0.25)}{0.5 \times (1 - 0.25) + 0.5 \times (1 - 0.05)} = \frac{0.375}{0.375 + 0.475} = 0.44,
$$
taking the population risk of breast cancer by 45 as 0.05 for a non-carrier. (c) Her risk of breast cancer between 45 and 80 is $0.44 \times (0.65 - 0.25)/(1 - 0.25) = 0.44 \times 0.533 = 0.235$, compared with about 0.10 for a woman of the general population, which is the number that matters for her decision about surveillance or risk-reducing surgery. (d) If she tests negative for her mother's mutation, her posterior carrier probability falls essentially to zero (the test detects the known familial variant with near certainty) and her risk returns to the population level.

![Bayesian risk in a hereditary cancer family (illustrative penetrance curves, of the shape and magnitude reported for *BRCA1* carriers and for the general population, so the numbers differ slightly from those of Example 21.4.1). A: the pedigree, with ages at diagnosis and current ages written under the symbols; the consultand (arrow) is untested. B: the probability that she carries the familial variant, as a function of her current age while she remains unaffected: the prior $1/2$ falls as she passes the ages of highest risk without disease. C: her risk of breast cancer between 45 and 80 years if she remains untested, if she tests negative for the familial variant, and for a woman of the general population](./plots/hereditary-risk.py)

### 21.4.2. Variants of Uncertain Significance

Sequencing a cancer-predisposition gene often returns a missense change that has not been seen before. Such a variant of uncertain significance cannot be used for clinical decisions, and the fraction of tests that return one is higher in populations that are under-represented in the reference databases, which makes the problem one of equity as well as of biology. Four kinds of evidence resolve them, and they are the classical genetic ones: segregation with disease in families (a **likelihood ratio** computed as in **linkage** analysis, [7.4.14](/7.4.14)), absence from large population databases, the behavior of the variant in a functional assay, and the frequency of the same variant in independent patient series. Saturation **genome editing** ([7.4.19](/7.4.19#sec-19.4.3)) supplies functional data for all possible variants of a gene in advance of their appearance in patients, and for *BRCA1* it has reclassified most previously uncertain variants.

## 21.5. The Genetic Logic of Treatment

Two of the treatment strategies of [7.3.26](/7.3.26#sec-26.6) are genetic arguments.

The first is to target the product of a **driver mutation**: a tumor that depends on a constitutively active kinase can be treated with an inhibitor of that kinase, as chronic myeloid leukemia is treated with imatinib against the BCR–ABL1 fusion protein and HER2-amplified breast cancer with an **antibody** against the **receptor**. The genotype of the tumor, not its tissue of origin, selects the treatment, and resistance arises by further mutation of the same gene, which is itself a selection experiment: mutations in the drug-binding site of *ABL1* are recovered from relapsing patients in the same way as resistance mutations are recovered from bacterial cultures ([7.4.10](/7.4.10)).

The second is **synthetic lethality** ([7.3.26](/7.3.26#def-26.6.2)), which exploits a **loss-of-function mutation** rather than a gain. Two genes are synthetically lethal when a cell survives the loss of either but not of both; if a tumor has already lost one of them, a drug that inhibits the other kills the tumor cells and spares the normal cells of the patient, which retain one functional copy. Inhibitors of the **enzyme** poly(ADP-ribose) polymerase are lethal in cells that lack **homologous recombination**, so they are used against tumors with *BRCA1* or *BRCA2* mutations, in which the normal allele has been lost somatically. The genetics of the approach is that of a synthetic lethal screen in yeast, carried out between an inherited mutation and a drug, and its limits are also genetic: resistance arises by secondary mutations that restore the **reading frame** of *BRCA1* or *BRCA2*, a reversion in the classical sense ([7.4.12](/7.4.12#sec-12.1)).

## Summary

| Topic | Key points |
|---|---|
| Clonality (21.1.1) | X-inactivation mosaics (G6PD leiomyomas), identical breakpoints and immunoglobulin rearrangements, one phylogeny per tumor; clonal, not homogeneous |
| Multistage (21.1.2) | log–log slope $k-1$ of the incidence curve; 4–6 for carcinomas; clonal expansion inflates $k$; hereditary forms lose one step |
| Drivers and signatures (Definition 21.1.1) | drivers identified statistically by excess and clustering; signatures of tobacco, ultraviolet light, **mismatch repair**, homologous-recombination defects and ageing; mutational burden spans three orders of magnitude and predicts response to checkpoint blockade |
| Oncogenes (Definition 21.2.1) | dominant in the cell; found by the NIH 3T3 transformation assay (*HRAS* G12, 1982); activated by point mutation, amplification, fusion or regulatory translocation; rarely inherited |
| Suppressors (Definition 21.3.1) | recessive in the cell, dominant in the family; gatekeepers vs caretakers |
| Two-hit model (Formula 21.3.1, Eqs. (21.1), (21.2)) | $m_1 = N\mu t$, $m_2 \approx N(\mu t)^2$; penetrance $1 - \mathrm{e}^{-m}$; $N = 1.5\times10^5$, $\mu = 4\times10^{-6}$ give $m_1 \approx 3$, penetrance 95 %, mostly bilateral, against one sporadic case in about 17 000; semi-logarithmic straight line in $t$ vs $t^2$ |
| LOH (Definition 21.3.2) | chromosome loss, loss with duplication, **mitotic recombination**, deletion, point mutation or methylation; copy number and marker pattern distinguish them; overlapping losses map the gene |
| Families (Algorithm 21.4.1, Example 21.4.1) | pedigree features; penetrance estimates and their ascertainment bias; posterior carrier probability from age and test results; modifiers as polygenic scores |
| Uncertain variants (21.4.2) | segregation, population frequency, functional assay, recurrence; saturation editing supplies the functional map in advance |
| Treatment (21.5) | target the driver product (imatinib, anti-HER2), resistance by mutation of the same gene; **synthetic lethality** with PARP inhibitors in *BRCA*-mutant tumors, resistance by reversion |

## Questions

1. Why does the finding that a leiomyoma from a woman heterozygous for two G6PD alleles expresses only one of them argue for a clonal origin, and why would the same result in a tumor from a man prove nothing?

   **Answer** Normal tissue of a heterozygous woman is a mosaic of cells expressing either allele, because X inactivation is random and clonally inherited; a tumor expressing only one allele must therefore descend from a single cell (or from a group of cells within one patch, which other evidence excludes). A man is **hemizygous** and expresses one allele in all cells anyway, so the observation carries no information.

2. The incidence of a carcinoma rises 300-fold between ages 35 and 75. (a) Estimate the number of rate-limiting steps. (b) A population in which one step occurs 5 times faster has what incidence relative to the first, at any age? (c) Why is the estimate from (a) an upper bound on the number of driver mutations?

   **Answer** (a) Slope $= \log 300/\log(75/35) = 2.477/0.330 = 7.5$, so $k - 1 \approx 7.5$ and $k \approx 8.5$, say 8 or 9 steps. (b) Five times higher: the hazard is proportional to the product of the step rates (the multistage model of [7.3.26](/7.3.26#fml-26.2.1)). (c) Clonal expansion of intermediate cells between steps steepens the age curve, so part of the apparent power comes from growth rather than from extra mutations.

3. A tumor has 4 000 somatic mutations, of which 5 are judged drivers. (a) What distinguishes drivers statistically? (b) Why can a gene with many mutations across a cohort nevertheless be a passenger? (c) What does a high burden imply for treatment?

   **Answer** (a) Drivers are mutated more often than the local background rate predicts and show a characteristic pattern: recurrent missense changes at a few residues for gain of function, dispersed truncating mutations for loss of function, reproduced in independent cohorts. (b) Long genes, late-replicating regions and regions with **mutational hotspots** accumulate many passengers; the comparison must be with the local background rate, not with the genome average. (c) Many mutations mean many potential neoantigens, so **immune checkpoint blockade** is more likely to work.

4. Using Eqs. (21.1) and (21.2) with $N = 1.5 \times 10^5$ and $\mu = 4 \times 10^{-6}$ per year: (a) the expected number of tumors in a carrier by age 3; (b) the penetrance at that age; (c) the proportion of carriers with bilateral disease by age 3.

   **Answer** (a) $m_1 = 1.5 \times 10^5 \times 4 \times 10^{-6} \times 3 = 1.8$. (b) $1 - \mathrm{e}^{-1.8} = 0.835$. (c) Each eye has $m/2 = 0.9$: affected with probability $1 - \mathrm{e}^{-0.9} = 0.593$, both eyes with probability $0.593^2 = 0.352$, that is 35 % of all carriers and $0.352/0.835 = 42\,\%$ of those affected by that age.

5. Show that in the two-hit model the fraction of carriers still free of disease is a straight line against age on semi-logarithmic axes, while for non-carriers it is a straight line against the square of age, and explain how Knudson used this.

   **Answer** For carriers $\mathbb{P}(\text{no tumor}) = \mathrm{e}^{-N\mu t}$, so $\ln \mathbb{P} = -N\mu t$ is linear in $t$; for non-carriers $\mathbb{P} = \mathrm{e}^{-N\mu^2 t^2}$, so $\ln \mathbb{P} = -N\mu^2 t^2$ is linear in $t^2$. Knudson plotted the fraction of patients not yet diagnosed against age for bilateral (hereditary) and unilateral (mostly sporadic) cases and found the two shapes, which told him that one form needs one event and the other two.

6. In a retinoblastoma from a patient with a germline *RB1* mutation, markers along chromosome 13 show: heterozygosity retained at loci near the centromere, lost from a point in 13q14 to the telomere, with two copies of the chromosome throughout. (a) Which mechanism produced the loss? (b) Which allele was lost? (c) What result would a whole-chromosome **nondisjunction** have given?

   **Answer** (a) Mitotic recombination between the centromere and the crossover point, which makes everything distal homozygous while the copy number stays at two. (b) The normal allele, together with the markers linked to it on that chromosome arm. (c) One copy of the whole chromosome, with loss of heterozygosity for every marker on it, including those near the centromere.

7. A sporadic unilateral retinoblastoma is found to carry two mutant *RB1* alleles in tumor tissue, with normal *RB1* in blood. (a) Explain in terms of the model. (b) What is the recurrence risk for the patient's siblings and children? (c) What if the same tumor had a mutation also present in blood at low level?

   **Answer** (a) Both hits were somatic in one retinoblast, which is the sporadic case of Eq. (21.2). (b) Low, essentially the population risk, apart from the small possibility of parental germline mosaicism; the patient's children are at population risk. (c) Low-level presence in blood indicates somatic mosaicism for the first hit, arising early in development: the risk to the patient's children is then intermediate, up to $1/2$ if germ cells carry it, and testing of gametes or offspring is required.

8. A woman of 35 whose mother carries a *BRCA2* mutation is untested and unaffected. Using a penetrance of breast cancer in carriers of 0.10 by age 35 and 0.60 by 80, and a population risk of 0.02 by 35: (a) her posterior carrier probability; (b) her risk of breast cancer between 35 and 80; (c) the risk for each of her children of carrying the mutation.

   **Answer** (a) $\dfrac{0.5 \times 0.90}{0.5 \times 0.90 + 0.5 \times 0.98} = \dfrac{0.45}{0.94} = 0.479$. (b) $0.479 \times (0.60 - 0.10)/(1 - 0.10) = 0.479 \times 0.556 = 0.266$. (c) $0.479 \times 1/2 = 0.24$.

9. Why does a negative gene test in an unaffected relative mean little unless the family's mutation is known, and what is the first test to order in a cancer family?

   **Answer** A negative result may mean that the person did not inherit the family's mutation, or that the family's predisposition is caused by a mutation the test cannot detect (in another gene, or of a kind the assay misses). Only when a specific mutation has been identified in an affected relative does a negative result exclude it (a "true negative"). The first test is therefore of an affected family member, preferably the youngest or most severely affected.

10. Two genes are synthetically lethal. (a) State the genetic condition precisely. (b) Why does a PARP inhibitor spare the normal cells of a *BRCA1* mutation carrier? (c) By what genetic change do tumors become resistant, and what does that predict about the sequence of the resistant allele?

    **Answer** (a) Cells lacking either gene alone are viable; cells lacking both die. (b) The patient's normal cells are heterozygous and retain one functional *BRCA1* allele, so **homologous recombination** still works; the tumor cells have lost the second allele and depend on the pathway that the drug blocks. (c) By restoring homologous recombination, most often through a second mutation that restores the reading frame of the original frameshift allele (an intragenic reversion or compensatory **indel**), so the resistant allele encodes a nearly full-length, partly functional protein.

11. A colorectal tumor shows instability at **microsatellite** markers and no mutation in the mismatch-repair genes. (a) What is the likely second hit? (b) How would you demonstrate it? (c) Does this tumor count as having two hits under the model?

    **Answer** (a) Epigenetic silencing of *MLH1* by hypermethylation of its promoter **CpG island**, the usual cause in sporadic cases. (b) By a methylation assay of the promoter together with loss of the MLH1 protein in immunostaining, and absence of the mutation in germline DNA (which also distinguishes it from Lynch syndrome). (c) Yes: both copies are inactive, one usually by methylation of both alleles or by methylation plus loss of the region; the model counts functional inactivation, whatever its molecular form.

12. (Synthesis) Explain why an inherited mutation in a caretaker gene and an inherited mutation in a gatekeeper gene both produce dominant predisposition in pedigrees, yet affect the age-incidence curve differently.

    **Answer** Both are recessive in the cell and are inherited as single mutant alleles that are completed somatically, so both give dominant transmission with incomplete penetrance. A gatekeeper mutation removes one of the rate-limiting steps, so the incidence curve keeps its shape but shifts to earlier ages and its log–log slope falls by one. A caretaker mutation adds no step; by raising the mutation rate it multiplies the rates of all the remaining steps, so the incidence is multiplied by a large factor at every age while the slope stays the same. Distinguishing the two in data requires fitting the whole curve, not only the childhood risk.
