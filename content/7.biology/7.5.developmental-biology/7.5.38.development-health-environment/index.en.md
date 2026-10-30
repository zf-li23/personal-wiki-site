---
title: Development, Health and the Environment
description: What happens when development goes wrong and how the environment takes part in normal development. Pregnancy loss and birth defects; chance, with a binomial model of skewed X inactivation; pleiotropy and heterogeneity in syndromes; teratogens, critical periods and dose–response (four-parameter logistic, teratogenic index); thalidomide as a molecular glue that degrades SALL4; alcohol (with the Widmark formula) and retinoic acid (with a feedback model of the excess that becomes a deficiency); infections and other agents; endocrine disruptors and non-monotonic dose–response; the developmental origins of health and disease; cancer as a disease of development and differentiation therapy; plasticity, polyphenisms and their threshold models; developmental symbiosis.
---

The previous chapters described how an embryo builds itself when everything goes right. This chapter turns to two questions that are central to medicine and to ecology: how often and why development fails, and how much of normal development depends on information from outside the embryo. Most human conceptions do not survive, and about one newborn in thirty has a major malformation; the causes are mutations and chromosomal errors, chemicals and infections that interfere with developmental signals, and plain chance. Each cause can be read with the mechanisms of the earlier chapters: thalidomide destroys a transcription factor needed in the **limb field** ([7.5.31](/7.5.31)), alcohol and retinoic acid act on the **neural crest** ([7.5.20](/7.5.20)), estrogenic chemicals change the **Hox gene** code of the Müllerian duct ([7.5.26](/7.5.26)). The same pathways that build the embryo are reactivated in cancer, and tumours can sometimes be returned to normal behaviour by an embryonic environment. The second half of the chapter treats the environment not as a hazard but as a normal input: temperature, food, crowding, predators and symbiotic microbes direct development in many animals, often through hormones and thresholds that can be written as simple models. The genetics of these topics was treated in [7.4](/7.4) (aneuploidy in [7.4.16](/7.4.16), epigenetic inheritance in [7.4.18](/7.4.18), threshold traits in [7.4.24](/7.4.24)), the cell biology of cancer in [7.3.26](/7.3.26); how developmental mechanisms produce evolutionary change is the subject of the next chapter, [7.5.39](/7.5.39).

## 38.1. How Often Development Fails

Development fails often, and mostly early. When pregnancies are detected by daily hormone assays from the time of implantation, about a third of them are lost, two thirds of these before the woman knows that she is pregnant (Wilcox and colleagues 1988); in IVF, only about a third of transferred embryos implant. About 15 % of clinically recognized pregnancies end in miscarriage, more than 80 % of these before the twelfth week, and about half of first-trimester losses have a chromosomally abnormal embryo ([7.5.5](/7.5.5#sec-5.7.1), with the maternal-age effect in [7.4.16](/7.4.16#sec-16.2.2)). Of the babies born, about 3 % have a major structural birth defect, and more have functional deficits recognized later.

![Outcome of 100 human pregnancies detected from implantation by a daily urinary hCG assay: about 22 are lost before clinical recognition and about 9 as recognized miscarriages, leaving about 69 live births, of which about 3 % carry a major birth defect. Losses before implantation are not detectable by this method and are not included](./plots/pregnancy-outcomes.py)

There are three broad causes of abnormal development:

- genetic: mutations, **aneuploidy** and chromosomal rearrangements ([7.4.12](/7.4.12), [7.4.15](/7.4.15), [7.4.16](/7.4.16));
- environmental: drugs, chemicals, infections, radiation and maternal conditions such as diabetes that interfere with developmental signals;
- stochastic: chance events in development itself, which can produce a defect in a genetically normal embryo in a normal environment.

Most defects are multifactorial: a genotype raises the susceptibility, an exposure or a chance event pushes development across a threshold, the logic of the **liability** model of [7.4.24](/7.4.24#def-24.6.1).

## 38.2. The Role of Chance

Developmental outcomes are probabilistic. Gene expression is noisy ([7.2](/7.2)), cell fate decisions in small populations are random ([7.5.36](/7.5.36#sec-36.4)), and some decisions are made once in a few founder cells and then inherited. **X-chromosome inactivation** is the clearest example ([7.4.18](/7.4.18#sec-18.5)). In a woman heterozygous for an X-linked mutation, each cell of the early epiblast inactivates one X at random, and its descendants keep the choice. If by chance most precursor cells of a tissue inactivate the normal X, the woman expresses the disease. Identical twin sisters, both carriers of a hemophilia allele, have been described of whom one had severe hemophilia and the other was healthy.

**Formula 38.2.1 (Skewed X Inactivation in a Small Pool)** If a tissue descends from $N$ precursor cells at the time of X inactivation and each keeps the wild-type X active with probability $\frac12$, independently, the number $K$ of precursors with an active wild-type X is binomial, and the fraction of cells in the tissue that express the wild-type allele is

$$
f=\frac{K}{N},\qquad K\sim\mathrm{Bin}\!\left(N,\tfrac12\right),\qquad \mathbb{E}[f]=\tfrac12,\qquad \operatorname{Var}(f)=\frac{1}{4N}.
\tag{38.1}
$$
The probability of a skew below a level $c<\frac12$ is $\mathbb{P}(f\le c)=\sum_{k\le cN}\binom{N}{k}2^{-N}$, which falls roughly exponentially with $N$ (by the Chernoff bound, $\mathbb{P}(f\le c)\le \mathrm{e}^{-2N(1/2-c)^2}$).

**Example 38.2.1** Factor VIII, the clotting factor missing in hemophilia A, is produced by cells whose X choice was made in a small founder pool. With $N=8$, $\mathbb{P}(f\le 0.4)=\mathbb{P}(K\le 3)=\frac{1+8+28+56}{256}\approx 0.36$; with $N=16$, $\mathbb{P}(K\le 6)\approx 0.23$; with $N=64$ it is about $0.07$. A plasma level below 40 % of normal, the range of mild hemophilia, is in fact found in roughly a quarter of female carriers, consistent with an effective founder pool of the order of ten cells. A severe deficiency ($f\le0.1$) requires $K=0$ when $N=8$, probability $\frac{1}{256}$, which is why severely affected carriers are rare.

![Chance in development: random X inactivation. A: distribution of the fraction f of cells that keep the wild-type X active in a tissue founded by N = 8, 16 or 64 precursors (Formula 38.2.1); the shaded region f ≤ 0.4 corresponds to clotting-factor levels in the range of mild hemophilia. B: probability of f ≤ 0.4 and of f ≤ 0.1 against N on a logarithmic scale: skewed inactivation is common in small founder pools and vanishingly rare in large ones](./plots/xci-skew.py)

The same reasoning applies to any decision fixed early in a few cells: the left–right decision when cilia-driven flow is weak ([7.5.17](/7.5.17)), the incomplete penetrance of many developmental mutations (**penetrance**, [7.4.3](/7.4.3#sec-3.5.1)), and the different phenotypes of monozygotic twins.

## 38.3. Genetic Syndromes

Human birth defects often come as syndromes (Greek, "running together"), sets of anomalies that occur together. A syndrome arises either from a chromosomal change that alters the dose of many genes at once, as in trisomy 21, or from one gene with several effects, **pleiotropy** ([7.4.3](/7.4.3#sec-3.4.2)). Developmental biology distinguishes two kinds.

**Definition 38.3.1 (Mosaic and Relational Pleiotropy)** In **mosaic pleiotropy** a gene is needed independently in several tissues, and each tissue is abnormal because it lacks the gene's product. In **relational pleiotropy** a gene is needed in one tissue only, and other tissues are abnormal because they depend on signals or structures from the first.

The receptor tyrosine kinase KIT and its ligand stem cell factor (SCF) are needed for the proliferation and migration of melanoblasts from the neural crest, of hematopoietic stem cells and of **primordial germ cells**. Mice homozygous for severe *Kit* (*Dominant white spotting*) or *Kitl* (*Steel*) alleles are white, anemic and sterile, mosaic pleiotropy. Human piebaldism, caused by heterozygous *KIT* mutations, usually shows only the pigment defect (a white forelock and unpigmented skin), because one functional copy suffices for blood and germ cells ([7.5.1](/7.5.1#sec-1.9)). The transcription factor MITF is an example of relational pleiotropy: in *Mitf* mutant mice the retinal pigment epithelium fails to differentiate, the choroid fissure of the optic cup does not close properly, the vitreous fluid drains, and the whole eye remains small; the lens and cornea, which never express MITF, are small as a consequence (microphthalmia).

The converse also holds. **Genetic heterogeneity** ([7.4.4](/7.4.4)) is the production of the same phenotype by mutations in different genes, typically genes of one pathway: the white-spotting syndrome is produced by loss of KIT or of its ligand, and holoprosencephaly, the failure of the forebrain to divide, with cyclopia at its extreme, by mutations in *SHH*, in genes needed for its release or reception, or in the cholesterol synthesis gene *DHCR7* (Smith–Lemli–Opitz syndrome), because Hedgehog proteins carry a cholesterol adduct and Smoothened needs cholesterol to signal ([7.3.19](/7.3.19)).

**Definition 38.3.2 (Phenotypic Heterogeneity)** **Phenotypic heterogeneity** is the production of different phenotypes, or different severities of one phenotype, by the same mutation in different individuals, because of differences in genetic background, environment and chance.

The same *FGFR3* mutation produced phenotypes from mild to lethal in ten unrelated families, and a homozygous limb mutation in one family produced anything from severe phocomelia to a slightly abnormal thumb. Phenotypic heterogeneity is the clinical face of variable expressivity and modifier genes ([7.4.3](/7.4.3#sec-3.5.2)).

![Three relations between genes and syndromes. A: mosaic pleiotropy: KIT and its ligand are needed independently in melanoblasts, blood stem cells and germ cells, so severe loss of function causes white spotting, anemia and sterility. B: relational pleiotropy: MITF acts only in the retinal pigment epithelium, but the failure of this tissue prevents closure of the choroid fissure and retention of vitreous fluid, so the lens and cornea, which do not express MITF, remain small. C: genetic heterogeneity: loss of SHH, of DISP1 or GLI2, or of cholesterol synthesis (DHCR7) all reduce Hedgehog signaling in the prechordal midline and give the same phenotype, holoprosencephaly](./plots/pleiotropy.py)

Down syndrome, the commonest viable autosomal aneuploidy, illustrates the chromosomal route ([7.4.16](/7.4.16#sec-16.2.3)). An extra chromosome 21 raises the dose of about 230 protein-coding genes by half, and no single gene accounts for the syndrome: the dual-specificity kinase DYRK1A contributes to the neural and craniofacial features, the transcription factor and microRNA genes of the chromosome (including the microRNA *MIR155*) to the misregulation of many targets, and the extra copies of *APP* to the early Alzheimer disease of adults. Mouse models that carry only parts of the human chromosome are used to map which segments cause which features. The heart defects (atrioventricular septal defects in about 40 % of children) and the duodenal atresia are malformations of organogenesis ([7.5.28](/7.5.28), [7.5.30](/7.5.30)).

## 38.4. Teratogenesis

### 38.4.1. Teratogens and Critical Periods

In the summer of 1962 two events showed that embryos are vulnerable to the chemical environment. Rachel Carson's *Silent Spring* documented the damage done by the insecticide DDT to birds, and it became known that thalidomide, a sedative prescribed in early pregnancy, caused severe limb malformations. "It is all of a piece, thalidomide and pesticides," Carson wrote.

**Definition 38.4.1 (Teratogen)** A **teratogen** (Greek, "monster-maker") is an exogenous agent, chemical, physical or infectious, or a maternal metabolic condition, that causes structural or functional abnormalities in the embryo or fetus at exposures that do not necessarily harm the mother.

The general principles were summarized by James Wilson in 1959 and are still the framework of teratology:

1. Susceptibility depends on the genotype of the embryo and the mother and on their interaction with the agent.
2. Susceptibility depends on the developmental stage at exposure.
3. Teratogens act by specific mechanisms on specific developing cells and tissues.
4. The outcomes are death, malformation, growth retardation and functional deficit.
5. Access of the agent to the embryo depends on its nature (placental transfer, metabolism).
6. The frequency and severity of effects increase with dose, from no effect to lethality.

**Definition 38.4.2 (Critical Period)** The **critical period** of an organ for a teratogen is the period of development during which exposure can cause a malformation of that organ; it coincides with the period in which the organ's primordium is induced, patterned and grows.

Human development is divided into the embryonic period, to the end of the eighth week after fertilization, in which the organs form, and the fetal period of growth and maturation. Before the third week, exposure usually has an all-or-none effect: either many cells die and the embryo is lost, or few die and the regulative embryo replaces them ([7.5.1](/7.5.1)). The embryonic period is the time of greatest sensitivity to structural malformations, and each organ has its own window. The brain keeps developing and remains sensitive to functional damage through fetal life and childhood.

![Critical periods of human development. A: weeks after fertilization (logarithmic scale): dark bars, periods of highest sensitivity to major structural malformations; light bars, sensitivity to minor malformations and functional defects; before week 3, the all-or-none period. Windows are approximate. B: the stage-and-dose model of Formula 38.4.1 for three organs with Gaussian sensitivity windows (heart, arms, palate) at doses of 0.7, 1 and 2 times the half-effective dose: the timing of exposure decides which organ is affected, the dose how often; the grey curve is the probability that any of the three is malformed](./plots/critical-periods.py)

**Formula 38.4.1 (Stage Window and Dose)** A simple model combines the two dependences. Let $s_k(t)\in[0,1]$ be the sensitivity of organ $k$ to exposure on day $t$ and $H(D)=D^h/(D^h+D_{50}^h)$ a Hill function of dose ([7.1](/7.1)). If the organs are affected independently,

$$
\mathbb{P}_k(t,D)=s_k(t)\,H(D),\qquad \mathbb{P}(\text{any malformation})=1-\prod_k\bigl(1-s_k(t)\,H(D)\bigr).
\tag{38.2}
$$
The pattern of malformations identifies the time of exposure, the frequency reflects the dose.

The model explains why the defects caused by one agent depend on the time of exposure, as for thalidomide below, and why different agents taken at the same time produce similar spectra. In the laboratory, teratogenic potency is measured by exposing embryos at a defined stage to a dilution series, for example in the frog embryo teratogenesis assay (FETAX) with *Xenopus laevis* or in zebrafish, and scoring malformation and death.

**Formula 38.4.2 (Dose–Response and Teratogenic Index)** The fraction of embryos responding at dose $x$ is fitted with the four-parameter logistic function

$$
y(x)=y_{\min}+\frac{y_{\max}-y_{\min}}{1+(\mathrm{EC}_{50}/x)^{n}},
\tag{38.3}
$$
with $\mathrm{EC}_{50}$ the dose of half-maximal effect and $n$ the Hill slope ([7.7](/7.7) for the statistics of such fits). Fitting malformation gives the $\mathrm{EC}_{50}$, fitting death the $\mathrm{LC}_{50}$; the teratogenic index is

$$
\mathrm{TI}=\frac{\mathrm{LC}_{50}}{\mathrm{EC}_{50}}.
$$
A large index means that the agent malforms at doses that do not kill the embryo; in FETAX, $\mathrm{TI}>1.5$ is taken to indicate teratogenic hazard.

![Dose–response of a teratogen in a simulated embryo assay: 40 embryos at each of ten doses, scored for malformation (blue) and death (red); curves, least-squares four-parameter logistic fits (Formula 38.4.2) with 95 % confidence bands; dashed lines, the fitted EC50 and LC50 with their confidence intervals. The teratogenic index LC50/EC50 is about 8](./plots/dose-response.py)

**Example 38.4.1** In the simulated assay of the figure (true $\mathrm{EC}_{50}=8$, $\mathrm{LC}_{50}=60$), the fits give $\mathrm{EC}_{50}\approx7.7$ (95 % CI 6.1–9.6) and $\mathrm{LC}_{50}\approx60$ (52–70), $\mathrm{TI}\approx7.8$: at doses between about 15 and 30 most embryos survive but are malformed. An agent that kills and malforms at similar doses (TI near 1) is an embryotoxin rather than a specific teratogen.

Species differ: the thalidomide disaster was not prevented by tests in rats and mice, which are insensitive to it, and teratogenicity testing has since been required in a second, non-rodent species, usually the rabbit.

### 38.4.2. Thalidomide

Thalidomide was marketed from 1957, in West Germany as Contergan and then in some 40 countries, as a sedative that was also taken against nausea in early pregnancy. About 10,000 children were born with malformations, about 40 % of whom died in their first year, before Widukind Lenz and William McBride linked them to the drug in 1961; in the United States Frances Kelsey of the Food and Drug Administration had withheld approval. The characteristic defect is phocomelia ("seal limb"), absence of the proximal limb segments with relatively preserved hands or feet, or complete absence of limbs (amelia), often with ear, eye, heart, kidney and gut malformations. The critical period is about days 20–36 after fertilization (34–50 days after the last menstrual period), and within it the time of intake predicts the defect: ear anomalies with the earliest exposures, then arms, then legs, and triphalangeal thumbs with the latest. A single tablet in this window could suffice.

How thalidomide acts remained unknown for half a century, and several hypotheses were proposed: damage to limb nerves, inhibition of angiogenesis in the limb bud (a thalidomide analogue that blocks angiogenesis truncates chick limbs), and cell death in the progress zone ([7.5.31](/7.5.31#sec-31.5)). The answer came from the drug's molecular target.

1. Ito, Handa and colleagues (2010) isolated cereblon (CRBN) as the protein that binds thalidomide. CRBN is the substrate receptor of a cullin-RING ubiquitin ligase, CRL4^CRBN (with CUL4A, DDB1 and RBX1). Knocking down *crbn* in zebrafish and chick embryos produced fin and limb defects like those of thalidomide, and a CRBN mutant that cannot bind the drug made the embryos resistant. CRBN is therefore necessary for the teratogenic effect.
2. In 2014 the anticancer effect of thalidomide analogues (lenalidomide, pomalidomide) in multiple myeloma was explained: the drug binding to CRBN creates a new surface that recruits the transcription factors IKZF1 and IKZF3 to the ligase, which **ubiquitin**-tags them for degradation by the **proteasome**. Thalidomide is a "molecular glue" that gives the ligase new substrates (neosubstrates).
3. Donovan and colleagues and Matyskiela and colleagues (2018) found that thalidomide induces the degradation of the zinc-finger transcription factor SALL4 in human cells. Heterozygous loss-of-function mutations of *SALL4* cause Duane-radial ray (Okihiro) syndrome, whose radial ray and ear defects resemble thalidomide embryopathy so closely that some people diagnosed as thalidomide victims carry *SALL4* mutations instead. SALL4 is degraded in human, primate and rabbit cells but not in mouse and rat cells, because of amino-acid differences in the zinc finger that contacts CRBN: this explains the species difference that defeated the original tests.
4. Further neosubstrates contribute: the transcription factor p63, which is needed in the apical ectodermal ridge and in the ear (its thalidomide-induced degradation causes fin and ear defects in zebrafish), and PLZF, whose degradation causes limb defects in chick embryos.

![Thalidomide as a molecular glue. Thalidomide binds cereblon (CRBN), the substrate receptor of the CRL4 ubiquitin ligase, and creates a surface that recruits neosubstrates such as SALL4; these are polyubiquitinated (Ub) and degraded by the proteasome. Right: neosubstrates and the consequences of their degradation, and the species difference in SALL4 that makes primates and rabbits, but not mice and rats, sensitive](./plots/thalidomide.py)

Thalidomide is used again, under strict pregnancy-prevention programs, against multiple myeloma and erythema nodosum leprosum. Its mechanism has become the basis of a new class of drugs, targeted protein degraders (molecular glues and bifunctional degraders), whose teratogenic risk is assessed by testing for degradation of SALL4 and the other developmental neosubstrates.

### 38.4.3. Alcohol

In frequency and cost to society, the most important teratogen is ethanol.

**Definition 38.4.3 (Fetal Alcohol Spectrum Disorder)** **Fetal alcohol spectrum disorder** (FASD) is the range of physical, neurological and behavioural effects of prenatal alcohol exposure. Its most severe form, **fetal alcohol syndrome** (FAS), combines a characteristic face (short palpebral fissures, a smooth philtrum and a thin upper lip), growth deficiency and abnormal brain structure or function (small head size, intellectual disability, deficits in attention, memory and executive function).

The face of FAS was described by Lemoine (1968) and by Jones and Smith (1973) ([7.5.1](/7.5.1#sec-1.9)). Many affected children have no facial signs, only cognitive and behavioural deficits, and imaging of fibre tracts reveals abnormalities in children with normal head size and intelligence quotient. Estimates of prevalence have risen with active case-finding: a study of first-grade children in four communities of the United States found FASD in 1–5 % (May and colleagues 2018), FAS itself in a few per thousand; the older figure of about 1 in 650 for FAS underestimated the problem.

Mouse models reproduce the face of FAS when the mother receives alcohol around gastrulation (embryonic day 7, corresponding to the third week of human development), and later exposures cause other defects (Sulik 2005). Several mechanisms act together:

- cell death of the cranial **neural crest** and of the anterior neural plate: ethanol generates **reactive oxygen species**, and the death and the malformations are reduced by antioxidants such as superoxide dismutase;
- reduced Sonic hedgehog signaling from the prechordal mesoderm, which normally supports the survival of the neural crest and the splitting of the forebrain; implanting Shh-secreting cells prevents the death of crest cells in alcohol-exposed chick embryos, and the face of FAS overlaps the mild end of holoprosencephaly;
- premature differentiation of neural crest cells into cartilage instead of migration and proliferation;
- inhibition of the **cell adhesion molecule** L1, which mediates adhesion of neural cells and the guidance of axons: alcohol at $7\,\mathrm{mM}$ blocks L1-mediated adhesion in culture, and mutations in human *L1CAM* cause a syndrome resembling severe FAS;
- interference with retinoic acid synthesis, because alcohol and retinol are oxidized by overlapping alcohol and aldehyde dehydrogenases.

How much alcohol reaches the embryo can be estimated from the mother's blood concentration, since ethanol crosses the placenta freely.

**Formula 38.4.3 (Widmark's Formula)** After drinking $A$ grams of ethanol, the peak blood alcohol concentration of a person of body mass $W$ (kg) is approximately

$$
c_{\max}\approx\frac{A}{r\,W}\quad(\mathrm{g\,L^{-1}}),
\tag{38.4}
$$
where $r$ is the fraction of the body mass in which ethanol distributes (about $0.55$ in women, $0.68$ in men, essentially body water). Thereafter the concentration falls approximately linearly, at about $0.10$–$0.20\,\mathrm{g\,L^{-1}\,h^{-1}}$, because alcohol dehydrogenase is saturated (zero-order kinetics, [7.1](/7.1)).

**Example 38.4.2** Two standard drinks in the United States contain $2\times14=28\,\mathrm{g}$ of ethanol. For a woman of $60\,\mathrm{kg}$, $c_{\max}\approx 28/(0.55\times60)\approx0.85\,\mathrm{g\,L^{-1}}$; with the molar mass $46\,\mathrm{g\,mol^{-1}}$, this is about $18\,\mathrm{mM}$, more than twice the concentration that blocks L1 adhesion in culture and close to the $25\,\mathrm{mM}$ that kills migrating cranial neural crest in chick embryos. At $0.15\,\mathrm{g\,L^{-1}\,h^{-1}}$ it takes almost six hours to clear. The effect of a dose therefore depends on the peak more than on the weekly total: binge drinking at the time of gastrulation, often before a pregnancy is recognized, is the most dangerous pattern. No safe level of drinking in pregnancy has been established.

### 38.4.4. Retinoic Acid

Retinoic acid (RA) is a normal developmental signal: it patterns the hindbrain and the trunk, the limbs, the heart and the gut ([7.5.17](/7.5.17#sec-17.2.3), [7.5.31](/7.5.31)), and its own concentration is regulated by synthesis (RALDH2) and degradation by the cytochrome P450 enzymes of the CYP26 family. Its analogue 13-*cis*-retinoic acid (isotretinoin) has been used against severe acne since 1982, and women of reproductive age are among its main users. Lammer and colleagues (1985) followed women who had been exposed in early pregnancy: of 59 fetuses, 26 were normal, 12 were spontaneously aborted and 21 had a characteristic pattern of malformations: absent or small ears, a small jaw, cleft palate, defects of the aortic arch and outflow tract, thymic aplasia and malformations of the hindbrain. These are the derivatives of the cranial neural crest of the pharyngeal arches and of the hindbrain, whose identity is set by the RA-dependent **Hox gene** code ([7.5.20](/7.5.20#sec-20.7)); excess RA shifts the code anteriorly, so that anterior rhombomeres take on posterior identities and the crest that should populate the first arch is reduced. The sensitive period in humans is days 20–35 after fertilization.

A puzzling observation is that excess and deficiency of RA cause similar malformations. A feedback model shows how this can happen.

**Formula 38.4.4 (Overshoot of the Retinoic Acid Feedback)** Let $R$ be the RA concentration in a tissue and $C$ the level of the RA-inducible degrading enzyme CYP26:

$$
\begin{aligned}
\frac{\mathrm{d}R}{\mathrm{d}t}&=s+u(t)-(k_0+k\,C)\,R,\\
\frac{\mathrm{d}C}{\mathrm{d}t}&=c_0+a\,\frac{R^n}{K^n+R^n}-\delta\,C,
\end{aligned}
\tag{38.5}
$$
with endogenous synthesis $s$, an external dose $u(t)$, basal and CYP26-dependent degradation, and induction of CYP26 by RA. If CYP26 turns over slowly ($\delta$ small compared with the degradation rate $k_0+kC$ of RA), a pulse of RA raises $C$, and after the pulse $C$ remains high for a time of order $1/\delta$ while $R$ relaxes quickly to the lower quasi-steady state $s/(k_0+kC)$: the excess is followed by a deficit.

**Example 38.4.3** With $s=1$, $k_0=0.2$, $k=1$, $c_0=0.05$, $a=0.6$, $K=1.5$, $n=2$ and $\delta=0.05\,\mathrm{h^{-1}}$ (a CYP26 half-life of about $14\,\mathrm{h}$), a six-hour pulse that raises RA ninefold induces CYP26 about twofold; when the pulse ends, RA falls to about half of its steady-state level and remains more than 20 % below it for about 19 hours. Larger pulses deepen and lengthen the deficit, which saturates at about 55 % below steady state. In embryos, Lee and colleagues (2012) found that a teratogenic dose of RA indeed induces *Cyp26* and lowers RA signaling below normal for a prolonged period, and that the malformations resemble those of RA deficiency.

![Why an excess of retinoic acid can end as a deficiency (Formula 38.4.4, illustrative parameters). A: a 6-hour pulse of RA (shaded) raises RA about ninefold and induces the slowly degraded enzyme CYP26; after the pulse, RA falls to about half of its steady state and recovers only as CYP26 decays. B: the largest fall of RA below its steady state (solid) and the time spent more than 20 % below it (dashed) against the pulse amplitude](./plots/ra-feedback.py)

Isotretinoin is now prescribed only with pregnancy-prevention programs. Vitamin A itself is teratogenic in high doses (above about 10,000 IU per day as supplements), whereas vitamin A deficiency causes eye, heart and lung malformations: the developmental system needs RA within a window.

### 38.4.5. Infections and Other Agents

| Agent | Critical exposure | Main effects | Mechanism or note |
|---|---|---|---|
| Rubella virus | first 16 weeks (risk about 90 % before week 11) | cataract, deafness, heart defects (patent ductus arteriosus), microcephaly | infection of the embryo; Gregg (1941) recognized the first viral teratogen; prevented by vaccination |
| Cytomegalovirus | any trimester, worst early | hearing loss, microcephaly, cerebral calcifications | the commonest congenital infection, about 0.5 % of births in high-income countries |
| Zika virus | first and second trimester | microcephaly, eye and joint defects | infects and kills neural progenitor cells of the cortex (epidemic in Brazil 2015–2016) |
| *Toxoplasma gondii*, *Treponema pallidum* | any time | hydrocephalus, chorioretinitis; congenital syphilis | transplacental infection |
| Ionizing radiation | weeks 8–15 for the brain | microcephaly, intellectual disability | death of proliferating neural progenitors; observed after the atomic bombings |
| Maternal hyperthermia | first trimester | neural tube defects | fever above about 39 °C |
| Maternal diabetes | organogenesis | heart defects, caudal regression, neural tube defects | hyperglycemia, oxidative stress |
| Valproic acid | weeks 3–4 | **neural tube defects** (1–2 %), facial anomalies, autism risk | histone deacetylase inhibition, folate antagonism |
| Warfarin | weeks 6–9 | nasal hypoplasia, stippled epiphyses | inhibition of vitamin K-dependent bone proteins |
| ACE inhibitors | second and third trimesters | renal failure, oligohydramnios, skull hypoplasia | fetal renin–angiotensin system needed for kidney function |
| Methylmercury | throughout | cerebral palsy-like syndrome, intellectual disability | neurotoxicity; Minamata disease in Japan |
| Maternal phenylketonuria | throughout | microcephaly, heart defects | high phenylalanine crosses the placenta |

Teratogens also occur in nature. In the 1950s, ewes in Idaho grazing on corn lily (*Veratrum californicum*) on day 14 of pregnancy gave birth to cyclopic lambs. The responsible alkaloids, cyclopamine and jervine, were later found to block Smoothened, the transducer of the **Hedgehog signaling pathway** ([7.3.19](/7.3.19)), and so reproduce the holoprosencephaly of *SHH* mutations; the synthetic Smoothened inhibitor vismodegib, derived from this line of work, is used against basal cell carcinoma and is itself teratogenic. Nicotine impairs lung and brain development, and components of crude oil from the 2010 Deepwater Horizon spill caused craniofacial defects of neural crest origin in zebrafish.

## 38.5. Endocrine Disruptors

**Definition 38.5.1 (Endocrine Disruptor)** An **endocrine disruptor** is an exogenous chemical, or mixture of chemicals, that alters the function of the endocrine system and thereby causes adverse effects in an organism, its offspring or populations (World Health Organization definition, 2002).

Endocrine disruptors are a special case of teratogens. Their effects are usually not gross malformations but changes in the differentiation and physiology of hormone-dependent tissues (the reproductive tract, the mammary gland, the brain, fat), which may appear only in adult life. They act in several ways:

- as agonists of a **nuclear receptor**: diethylstilbestrol (DES) and bisphenol A (BPA) bind the estrogen receptors;
- as antagonists: DDE, a metabolite of the insecticide DDT, and the fungicide vinclozolin block the androgen receptor;
- by changing hormone synthesis, transport or elimination: the herbicide atrazine induces aromatase, which converts androgens into estrogens; polychlorinated biphenyls interfere with thyroid hormone transport;
- by altering the sensitivity of tissues to later hormone exposure.

The synthetic estrogen diethylstilbestrol (DES) was prescribed to several million pregnant women, more than a million in the United States between 1947 and 1971, in the mistaken belief that it prevented miscarriage (a controlled trial in 1953 had already shown that it did not). In 1971 Herbst and colleagues linked it to clear-cell adenocarcinoma of the vagina, a cancer otherwise almost unknown in young women, in the daughters of treated mothers. DES daughters also have structural changes of the reproductive tract (a T-shaped uterus, cervical anomalies, vaginal adenosis), infertility and ectopic pregnancy. Mouse experiments revealed the mechanism. The **Müllerian duct** is regionalized by nested expression of posterior *Hoxa* genes: *Hoxa9* in the oviduct, *Hoxa10* and *Hoxa11* in the uterus, *Hoxa13* in the cervix and upper vagina ([7.5.26](/7.5.26#sec-26.3.1)). DES given to pregnant mice repressed *Hoxa10* in the mesenchyme of the duct, and the *Hoxa10* knockout mouse shows a homeotic transformation of the upper uterus into oviduct. DES, acting through the estrogen receptor, also represses *Wnt7a* in the epithelium; WNT7A maintains *Hoxa10* and *Hoxa11* in the mesenchyme and induces *Wnt5a*, which drives mesenchymal proliferation; *Wnt7a* knockout mice have reproductive tracts resembling those of DES-exposed mice. The case shows a general principle: a hormone given at the wrong time rewrites a positional code.

Bisphenol A (BPA), synthesized in the 1930s as an estrogen, became a component of polycarbonate plastics and epoxy resins (can linings, bottles, receipt paper) and is detectable in the urine of most people. In mice, low doses during fetal life alter the development of the mammary gland, prostate and reproductive tract and increase meiotic errors in oocytes, an effect first noticed when damaged polycarbonate cages released BPA and the frequency of aneuploid eggs rose (Hunt and colleagues 2003). Whether human exposure levels are harmful is contested. A large guideline-compliant rat study coordinated by the US National Toxicology Program (CLARITY-BPA, 2018) found few effects at low doses, whereas academic studies within the same consortium reported changes in several organs; in 2023 the European Food Safety Authority lowered its tolerable daily intake by a factor of about 20,000, to $0.2\,\mathrm{ng}$ per kg of body weight per day, mainly because of effects on the immune system in animals. Many countries have banned BPA in baby bottles.

Two features complicate the assessment of endocrine disruptors. Exposures are to mixtures, and hormones act at very low concentrations through receptors, so that the response need not increase steadily with dose.

**Formula 38.5.1 (A Non-Monotonic Dose–Response)** If a chemical activates a receptor-mediated response, $E_1(x)=x/(x+\mathrm{EC}_{50})$, and at higher doses suppresses it (receptor down-regulation, negative feedback, cytotoxicity), $E_2(x)=1/(1+(x/\mathrm{IC}_{50})^m)$, the net response

$$
E(x)=\frac{x}{x+\mathrm{EC}_{50}}\cdot\frac{1}{1+(x/\mathrm{IC}_{50})^{m}}
\tag{38.6}
$$
is an inverted U when $\mathrm{EC}_{50}\ll\mathrm{IC}_{50}$, with its maximum at intermediate doses. Toxicological testing, which starts at high doses and determines a no-observed-effect level, then extrapolates to lower doses assuming monotonicity, can miss the peak.

![A non-monotonic dose–response (Formula 38.5.1; illustrative): grey, a monotonic Hill curve; orange, a receptor-mediated response multiplied by a high-dose loss of response (EC50 = 0.01, IC50 = 1), an inverted U. A design that tests only high doses (red points) and extrapolates downwards (dashed) predicts no effect at low doses, where the inverted U has its maximum](./plots/nonmonotonic.py)

Non-monotonic responses are well established for hormones themselves, for example for estradiol and the growth of the prostate in mice; whether they occur for a given chemical at environmental doses has to be shown case by case, and this is the core of the disagreement about BPA.

Among other suspected disruptors, the herbicide atrazine has been studied most. Hayes and colleagues (2002) reported that it, at concentrations from $0.1\,\mathrm{\mu g\,L^{-1}}$, caused hermaphroditic gonads and lowered testosterone in male frogs, through induction of aromatase; other laboratories obtained mixed results, and regulatory reviews in the United States did not confirm effects at environmental concentrations, while the European Union withdrew atrazine in 2004 because of groundwater contamination. A clear case of endocrine disruption in wildlife is tributyltin, the antifouling paint of ship hulls, which at nanogram-per-litre concentrations caused female dog whelks and other marine snails to grow a penis and vas deferens (imposex), through the retinoid X receptor, and led to the collapse of snail populations near harbours until its worldwide ban in 2008. Turtles with **temperature-dependent sex determination** ([7.5.26](/7.5.26#sec-26.6)) can be feminized at male-producing temperatures by estrogenic compounds such as some PCBs and BPA. Waters from hydraulic fracturing ("fracking") sites contain chemicals with estrogenic and anti-androgenic activity in reporter assays; whether they affect human development is not known.

## 38.6. Developmental Origins of Health and Disease

**Definition 38.6.1 (Developmental Origins of Health and Disease)** The **developmental origins of health and disease** (DOHaD) are the influences of the environment in prenatal and early postnatal life (nutrition, stress, toxicants, maternal disease) on the risk of chronic disease in adult life, through persistent changes in the structure, physiology and gene regulation of organs.

The concept grew from epidemiology. David Barker found in 1989 that men born in Hertfordshire with a low birth weight had a higher risk of death from ischaemic heart disease, and later studies linked low birth weight with hypertension, type 2 diabetes and the metabolic syndrome. Natural experiments separate the effect of timing: children conceived during the Dutch Hunger Winter of 1944–1945, when rations fell below $1000\,\mathrm{kcal}$ per day for about six months, had a normal birth weight if the famine struck early in pregnancy but as adults more obesity, coronary heart disease and schizophrenia; exposure late in pregnancy reduced birth weight and later glucose tolerance. Sixty years later, those exposed around conception had slightly lower methylation of the imprinted *IGF2* region, although whether such marks cause the disease is unknown ([7.4.18](/7.4.18#sec-18.6.5)). Mechanisms include a reduced number of nephrons (a small kidney raises blood pressure for life, [7.5.25](/7.5.25)) and of pancreatic beta cells, altered set points of the hypothalamic–pituitary–adrenal axis, and epigenetic changes in the liver; in rats, protein restriction during pregnancy changes the methylation and expression of metabolic genes in the offspring's liver. The best-understood epigenetic model is the *Agouti viable yellow* allele, whose methylation, and with it coat colour and obesity, can be shifted by the mother's diet ([7.4.18](/7.4.18#sec-18.6.2)).

Two interpretations are discussed. In the thrifty-phenotype hypothesis (Hales and Barker 1992), a poorly nourished fetus sacrifices the growth of some organs to protect the brain, and the damage persists. In the predictive-adaptive-response or mismatch hypothesis (Gluckman and Hanson), the fetus sets its metabolism for the environment it expects, and disease results when the adult environment differs from the prediction.

**Formula 38.6.1 (A Mismatch Model)** Let $s$ be a metabolic set point fixed in fetal life by the nutrition received and $e$ the nutritional level of adult life (both scaled to $[0,1]$). A risk function with a mismatch term and a general cost of rich diets,

$$
r(s,e)=r_0\,\mathrm{e}^{\alpha(e-s)^2}+\beta \mathrm{e}^2,
\tag{38.7}
$$
is lowest, for each $s$, near $e=s$. In a population that is uniformly affluent ($e$ near 1), risk decreases with $s$, so that small babies carry the highest risk, although the same individuals would have been best adapted to scarcity.

![The mismatch idea (Formula 38.6.1; illustrative parameters r0 = 0.05, α = 4, β = 0.04). A: disease risk against the adult nutritional environment for three fetal set points; each curve is lowest near its own set point (dots), and the individual that developed under fetal undernutrition (red) is at the highest risk in an affluent adult environment (shaded). B: in a uniformly affluent environment, risk falls with the set point, the epidemiological association of low birth weight with adult disease](./plots/dohad-mismatch.py)

The model is qualitative, and the two hypotheses are not exclusive. The rapid rise of type 2 diabetes in populations that moved within one or two generations from scarcity to abundance, as in China and India, fits the mismatch interpretation.

Effects across more than one generation must be judged by the counting of exposed generations in [7.4.18](/7.4.18#fml-18.6.1): after exposure of a pregnant female, the fetus and its germ cells are exposed too, and only effects in the third generation (F3) are **transgenerational epigenetic inheritance**. The best-known claim is that of Anway, Skinner and colleagues (2005): a single injection of the antiandrogenic fungicide vinclozolin into pregnant rats during gonadal sex determination caused reduced sperm production and testis degeneration in males for four generations, associated with changed **DNA methylation** of sperm. Other laboratories, using oral exposure or other strains, did not reproduce the transmission, and in mammals most methylation is erased twice in each generation ([7.4.18](/7.4.18#sec-18.6.5)). Transgenerational effects are well documented in nematodes (small RNAs) and plants, much less so in mammals.

## 38.7. Cancer as a Disease of Development

Cancer is usually described as a disease of mutated cells ([7.3.26](/7.3.26)), but it is also a disease of development, in two senses. First, the genes mutated in cancers are largely the developmental regulators of this course, reactivated or released from control in adult tissues. Second, whether a cell with oncogenic mutations forms a tumour depends on its tissue environment, as the behaviour of embryonic cells depends on their neighbours.

| Developmental pathway | Cancer | Developmental counterpart |
|---|---|---|
| Hedgehog (**Hedgehog signaling pathway**) | basal cell carcinoma, medulloblastoma: loss of *PTCH1* or activating *SMO* mutations (Gorlin syndrome) | **floor plate** and neural tube patterning, granule-cell proliferation in the cerebellum |
| Wnt (**Wnt signaling pathway**) | colorectal cancer: loss of *APC* or stabilizing mutations of β-catenin | renewal of the intestinal crypt |
| Notch (**Notch signaling pathway**) | T-cell acute lymphoblastic leukemia: activating *NOTCH1* mutations | T-cell specification in the thymus |
| Hippo (**Hippo pathway**) | YAP/TAZ activation in many solid tumours | organ size control ([7.5.34](/7.5.34#sec-34.4)) |
| *Hox* and *MEIS1* | acute myeloid leukemia with *MLL* rearrangements | hematopoietic progenitor programs |
| Nodal | melanoma (secreted Nodal) | embryonic patterning ([7.5.16](/7.5.16)) |

Several observations show that the environment can override a malignant genome:

- Teratocarcinoma cells injected into a mouse blastocyst contribute to normal tissues of a **chimera** (Mintz and Illmensee 1975; [7.5.34](/7.5.34#sec-34.7)).
- Aggressive human melanoma cells transplanted into the neural tube of a chick embryo migrate along the neural crest pathways and integrate as non-malignant cells into crest derivatives, downregulating their secretion of Nodal; an environment of embryonic stem cells, which secrete Nodal inhibitors, has a similar effect (Kulesa, Hendrix and colleagues).
- In tissue recombination experiments with rat mammary glands, epithelium and stroma were separated, treated separately with the carcinogen *N*-nitrosomethylurea or with vehicle, and recombined. Tumours arose when the stroma had been exposed, whether or not the epithelium had, and not when only the epithelium had (Maffini, Soto and Sonnenschein 2004). The design is that of the classical epithelium–mesenchyme recombinations of organogenesis ([7.5.22](/7.5.22), [7.5.25](/7.5.25)).
- Normal adult tissues carry many cells with driver mutations without forming tumours: in human eyelid skin and oesophagus, clones with *NOTCH1* or *TP53* mutations occupy a large fraction of the epithelium by middle age (Martincorena and colleagues 2015, 2018).

These results led to the view, put most strongly by Sonnenschein and Soto as the "tissue organization field theory", that carcinogenesis is a disruption of tissue architecture; most cancer biologists hold that mutations are necessary but that tissue context decides whether a mutant clone progresses. Tumours also contain hierarchies of cells resembling those of renewing tissues, with self-renewing cancer stem cells ([7.5.36](/7.5.36#sec-36.5)).

**Definition 38.7.1 (Differentiation Therapy)** **Differentiation therapy** is the treatment of a cancer by agents that induce the malignant cells to resume differentiation, and thereby to stop dividing, rather than by killing them.

The paradigm is acute promyelocytic leukemia (APL). A t(15;17) translocation fuses the *PML* gene to the gene of the retinoic acid receptor α; the PML–RARα fusion protein binds RA response elements and recruits corepressors more strongly than normal RARα, so that myeloid progenitors are arrested at the promyelocyte stage. Pharmacological doses of all-*trans* retinoic acid release the block, and the leukemic cells differentiate into neutrophils, as first shown clinically by Wang Zhenyi's group in Shanghai (1988); arsenic trioxide, introduced by Zhang Tingdong in Harbin, induces the degradation of the fusion protein. Combined, the two drugs cure more than 90 % of patients without conventional chemotherapy (Lo-Coco and colleagues 2013), and APL, once the most rapidly fatal leukemia, has become one of the most curable. Inhibitors of mutant isocitrate dehydrogenase, which release a differentiation block caused by an oncometabolite, act on the same principle in some acute myeloid leukemias. Restoring tissue-specific microRNAs, such as miR-206 in rhabdomyosarcoma cells, induces differentiation in experimental models. Conversely, drugs developed against developmental pathways (Smoothened inhibitors such as vismodegib, the thalidomide analogues) are teratogens: the same knowledge serves both fields.

## 38.8. The Environment as a Normal Developmental Signal

### 38.8.1. Plasticity and Polyphenism

The model organisms of developmental biology were chosen partly because their development is little affected by the environment, which gives the impression that everything needed to build an animal is in the egg. In many animals this is not so.

**Definition 38.8.1 (Developmental Plasticity)** **Developmental plasticity** is the ability of one genotype to produce different phenotypes in response to environmental conditions experienced during development. The relation between environment and phenotype for a genotype is its **norm of reaction** ([7.4.3](/7.4.3#sec-3.5.4)); the alternative phenotypes are called morphs.

**Definition 38.8.2 (Polyphenism)** A **polyphenism** is a form of developmental plasticity in which an environmental cue switches development between two or more discrete alternative phenotypes, with few intermediates.

Plasticity is often continuous: the muscles of an athlete, or the tail depth of wood frog tadpoles, which increases with the number of predators in the pond. Polyphenisms are discontinuous, and the switch is almost always endocrine: a sensory system detects the cue, and hormones such as **juvenile hormone**, **ecdysone**, thyroid hormone, corticotropin-releasing hormone or insulin-like peptides change gene expression in the target tissues during a sensitive period. **Temperature-dependent sex determination** is a polyphenism ([7.5.26](/7.5.26#sec-26.6)).

| Cue | Example | Morphs | Mechanism |
|---|---|---|---|
| Season (temperature, day length) | the butterfly *Bicyclus anynana* | wet-season form with large ventral eyespots that deflect attacks; dry-season form, brown and cryptic in leaf litter | higher pupal temperature raises the 20-hydroxyecdysone titre earlier; ecdysone receptor in the eyespot centres enlarges the eyespots (Monteiro and colleagues 2015) |
| Season | the map butterfly *Araschnia levana* | orange spring form, dark summer form (Linnaeus described them as two species) | day length of the larva sets the timing of ecdysone release in the pupa; injected ecdysone produces the summer form |
| Food | honeybee, *Apis mellifera* | queen (fertile, lives years) or worker (sterile, lives weeks) | larvae fed royal jelly throughout develop as queens; worker jelly contains less sugar and more plant compounds such as *p*-coumaric acid, which suppress ovary development; knockdown of the DNA methyltransferase *Dnmt3* in larvae produces queen-like adults |
| Food | dung beetles, *Onthophagus* | horned fighting males or hornless "sneaker" males | larval nutrition sets body size; above a threshold size, juvenile hormone and insulin signaling at the last larval molt allow horn imaginal discs to grow (below) |
| Crowding | desert locust, *Schistocerca gregaria* | solitary green form or gregarious, swarming, dark form with longer wings | touch of the hind legs by other locusts raises serotonin in the thoracic ganglia within hours (behavioural switch); colour and morphology change over generations through maternal effects |
| Predator chemicals | the water flea *Daphnia* | helmet and spine, or none | kairomones from fly larvae (*Chaoborus*) or fish act through juvenile hormone and insulin pathways; induced mothers produce induced offspring |
| Predators | tree frog tadpoles (*Hyla chrysoscelis*), the snail *Thais lamellosa* | deep red tail fin; thick shell with a "tooth" | induced morphs survive predators better but grow more slowly without them (a trade-off) |
| Vibration | red-eyed tree frog, *Agalychnis callidryas* | early hatching | embryos from day 5 hatch within seconds when an egg-eating snake attacks the clutch |
| Drying pond, diet | spadefoot toads (*Scaphiopus*, *Spea*) | omnivorous or carnivorous (cannibalistic) tadpoles with large jaw muscles | in *Scaphiopus* falling water levels raise corticotropin-releasing hormone and thyroid hormone, accelerating metamorphosis; in *Spea* eating shrimp induces the carnivore morph |

**Definition 38.8.3 (Kairomone)** A **kairomone** is a chemical released by one species that benefits a receiver of another species; in predator-induced polyphenism, the predator's chemicals that induce defences in its prey.

To establish a predator-induced polyphenism one shows that the change is induced by the predator, or by water in which it has lived, and that the induced morph has a higher fitness in the predator's presence; in the snail *Thais*, crabs did not attack thick-shelled snails until more than half of the typical snails had been eaten.

Larval settlement is another normal environmental input. Many marine larvae delay metamorphosis until they encounter a specific cue: biofilms of particular bacteria, the prey of the adult, or the substrate itself. Larvae of the tubeworm *Hydroides elegans* metamorphose when they contact arrays of phage-tail-like structures produced by the bacterium *Pseudoalteromonas luteoviolacea* (Shikuma and colleagues 2014), and coral larvae swim towards the sound of reefs. William Keith Brooks restored the oyster beds of Chesapeake Bay in the 1880s by having shells thrown back into the bay, because the larvae of *Crassostrea virginica* need a hard, biofilm-covered substrate to settle. Plasticity has a cost: environmental change can trap a species, as with sea turtles whose nesting beaches warm and produce almost only females ([7.5.26](/7.5.26#sec-26.6.1)), and predator cues can make pesticides many times more lethal to tadpoles.

### 38.8.2. A Threshold Model of Polyphenism

The horns of male dung beetles show how a discontinuous phenotype can arise from a continuous variable. Body size at metamorphosis depends on the amount and quality of dung the mother provided and is roughly normally distributed; horn length is a steep sigmoid function of body size (Emlen; Moczek and Nijhout).

**Formula 38.8.1 (Sigmoid Allometry and Bimodality)** Let body size $X\sim\mathcal{N}(\mu,\sigma^2)$ and horn length

$$
H=h_0+\frac{h_1-h_0}{1+\mathrm{e}^{-(X-x_0)/w}},
\tag{38.8}
$$
with a threshold size $x_0$ and a transition width $w\ll\sigma$. The density of $H$ is $f_H(h)=f_X(x(h))\,\lvert\mathrm{d}x/\mathrm{d}h\rvert$ with $x(h)=x_0+w\ln\frac{h-h_0}{h_1-h}$; since $\lvert\mathrm{d}x/\mathrm{d}h\rvert=\frac{w\,(h_1-h_0)}{(h-h_0)(h_1-h)}$ diverges at both plateaus, the distribution of horn length is bimodal although body size is unimodal. The fraction of horned males is $\mathbb{P}(X>x_0)=1-\Phi\bigl((x_0-\mu)/\sigma\bigr)$.

**Example 38.8.1** With $\mu=3.2\,\mathrm{mm}$, $\sigma=0.35\,\mathrm{mm}$ and $x_0=3.25\,\mathrm{mm}$, $1-\Phi(0.14)\approx0.44$ of males are horned. A population whose threshold is $0.3\,\mathrm{mm}$ higher has only $1-\Phi(1.0)\approx0.16$ horned males on the same food. Such differences evolved within decades between populations of *Onthophagus taurus* introduced into Australia and into the eastern United States (Moczek and Nijhout 2003): the threshold itself is heritable, a link between plasticity and evolution taken up in [7.5.39](/7.5.39).

![A threshold polyphenism in dung beetles (Formula 38.8.1). A: horn length against body size for 2000 simulated males (body size normally distributed, mean 3.2 mm, SD 0.35 mm; sigmoid with threshold 3.25 mm; small noise in horn growth). B: the resulting horn lengths are bimodal: hornless and fully horned males, few intermediates. C: shifting the threshold by 0.3 mm on the same distribution of body sizes lowers the fraction of horned males from 44 % to 16 %](./plots/horn-threshold.py)

The same structure, a continuous internal variable read through a threshold, underlies the queen–worker switch (nutrition and juvenile hormone), caste determination in ants, and the liability models of human malformations (38.1).

## 38.9. Developmental Symbiosis

Symbiosis, in its original sense, is any close and persistent association of organisms of different species, whether parasitic (one partner benefits at the other's expense), mutualistic (both benefit) or commensal (one benefits, the other is unaffected). In many animals the development of organs requires signals from symbiotic microbes.

**Definition 38.9.1 (Developmental Symbiosis)** In **developmental symbiosis** the normal development of an organism requires signals or products of symbionts of other species. The host together with its persistent symbionts is called a **holobiont**.

Symbionts are transmitted vertically, through the egg, or horizontally, acquired from the environment in each generation.

- Vertical transmission, *Wolbachia*. These intracellular bacteria infect a large fraction of insect species and are transmitted through the oocyte. In *Drosophila* they move from the nurse cells into the oocyte along microtubules with dynein, like *bicoid* mRNA ([7.5.14](/7.5.14)), and they protect flies against RNA viruses. In the pill bug *Armadillidium vulgare*, *Wolbachia* feminizes genetic males, which then transmit the bacteria; in the parasitoid wasp *Asobara tabida*, removing *Wolbachia* with antibiotics causes apoptosis of the ovaries and sterility, an obligate dependence; in the filarial nematode *Brugia malayi*, *Wolbachia* are needed for the anterior–posterior polarity of the first division. *Wolbachia* that block dengue virus replication are released in mosquitoes to control disease.
- Horizontal transmission, the bobtail squid. The Hawaiian bobtail squid *Euprymna scolopes* hatches without symbionts and without a mature light organ. Within hours, cilia and mucus on two ciliated appendages of the nascent organ capture *Vibrio fischeri* from seawater, selecting it among many bacterial species. The bacteria colonize crypts of the organ and induce, through two components of their cell envelope, peptidoglycan fragments (tracheal cytotoxin) and lipopolysaccharide, the apoptosis and regression of the ciliated appendages over about four days, the differentiation of the crypt epithelium and the expression of opsins and other visual proteins in the organ. Squid raised in sterile seawater keep the ciliated appendages; purified tracheal cytotoxin with lipopolysaccharide induces their regression without bacteria (Koropatnick and colleagues 2004). The bacteria glow only at high density (quorum sensing, [7.11](/7.11)), and the squid uses the light to cancel its shadow in moonlight; each dawn it expels about 90 % of the bacteria, and the rest regrow.
- Algae in salamander eggs. The green alga *Oophila amblystomatis* colonizes the eggs, and even the cells, of the spotted salamander *Ambystoma maculatum*; its photosynthesis supplies oxygen to embryos deep in the egg mass, and herbicides that kill the alga reduce hatching.
- The mammalian gut. Humans carry about as many bacterial cells as human cells (roughly $4\times10^{13}$ against $3\times10^{13}$, Sender, Fuchs and Milo 2016), most of them in the colon, acquired at and after birth from the mother's vagina, gut and skin and from milk, whose oligosaccharides are indigestible by the infant but feed bifidobacteria. Germ-free mice show what the microbiota does. The gut epithelium differentiates incompletely; genes such as those for colipase and angiogenin-4 are induced by bacteria such as *Bacteroides thetaiotaomicron* (Hooper and colleagues 2001), and the capillary network of the villi is incomplete until bacteria are introduced, acting through Paneth cells (Stappenbeck and colleagues 2002). In germ-free zebrafish fewer intestinal epithelial cells divide and some cell types are missing ([7.5.30](/7.5.30)). The gut-associated lymphoid tissue, the balance of T-cell subsets and oral tolerance depend on bacterial products: the capsular polysaccharide A of *Bacteroides fragilis* restores T-cell development in germ-free mice (Mazmanian and colleagues 2005), and short-chain fatty acids such as butyrate from clostridial species induce regulatory T cells ([7.15](/7.15)). Germ-free mice also differ in stress hormones and behaviour, and effects of the microbiota on brain development are under study; claims about human behaviour and disease are mostly correlational so far.

Developmental symbiosis is the rule rather than the exception: the development of most animals has evolved in the presence of microbes, and some processes have come to depend on them, just as embryonic tissues depend on inductive signals from their neighbours.

## Summary

- Failure is common (38.1): about a third of implanted pregnancies are lost, about half of early miscarriages are aneuploid, and about 3 % of newborns have a major malformation. Causes are genetic, environmental and stochastic, usually combined through a threshold.
- Chance (Formula 38.2.1): a decision made in $N$ founder cells, such as X inactivation, gives a binomial fraction with variance $1/(4N)$; skewed expression of an X-linked mutation is common for $N\approx10$.
- Syndromes (38.3): mosaic and relational pleiotropy (Definition 38.3.1), genetic heterogeneity (one pathway, many genes) and phenotypic heterogeneity (Definition 38.3.2).
- **Teratogens** (Definition 38.4.1) act on specific targets during critical periods (Definition 38.4.2, Wilson's principles); timing selects the organ and dose the frequency (Formula 38.4.1). Potency is measured with four-parameter logistic fits and the teratogenic index $\mathrm{LC}_{50}/\mathrm{EC}_{50}$ (Formula 38.4.2).

| Teratogen | Window (after fertilization) | Target and mechanism |
|---|---|---|
| Thalidomide | days 20–36 | binds CRBN; degradation of SALL4, p63, PLZF; limb, ear, heart defects; rodents resistant |
| Alcohol | gastrulation onwards | neural crest death (ROS, reduced Shh), L1 adhesion; FASD (Definition 38.4.3); about $18\,\mathrm{mM}$ after two drinks (Formula 38.4.3) |
| Retinoic acid | days 20–35 | Hox code of hindbrain and pharyngeal crest; CYP26 feedback turns excess into deficit (Formula 38.4.4) |
| Rubella, CMV, Zika | first trimester | eye, ear, heart; neural progenitors |
| Cyclopamine | gastrulation | Smoothened; holoprosencephaly |

- Endocrine disruptors (Definition 38.5.1): DES repressed *Hoxa10* and *Wnt7a* in the Müllerian duct; BPA and atrazine remain contested; tributyltin caused imposex; receptor-mediated effects may be non-monotonic (Formula 38.5.1).
- DOHaD (Definition 38.6.1): fetal conditions set adult risk (Barker, Dutch Hunger Winter); thrifty phenotype and mismatch (Formula 38.6.1); transgenerational claims require the F3 generation.
- **Cancer** (38.7) reuses developmental pathways and depends on tissue context; differentiation therapy (Definition 38.7.1) cures APL with retinoic acid and arsenic.
- The environment as a normal signal (38.8): plasticity and polyphenism (Definitions 38.8.1, 38.8.2), endocrine switches, kairomones (Definition 38.8.3); a sigmoid read-out of a normal variable gives bimodal morphs, and the threshold is heritable (Formula 38.8.1).
- Developmental symbiosis (Definition 38.9.1): *Wolbachia*, the squid light organ induced by *Vibrio fischeri*, the gut microbiota and the development of the intestine and the immune system.

## Questions

1. Why are the risks of malformation and of embryonic death distributed so differently over the first eight weeks of human development?

   **Answer** Before about day 15 the embryo consists of few, largely undetermined cells that regulate: a teratogen either kills enough cells to end the pregnancy or kills few, which are replaced, so the outcome is death or normal development (all or none). From the third week, organ primordia are induced and patterned in sequence, each during a limited window; damage in a window removes or misplaces cells that cannot be replaced by regulation, producing a specific malformation, while the embryo as a whole survives. After week 8 organs mainly grow, so structural malformations become rare, but the brain remains sensitive to functional damage.

2. A woman carrying an X-linked recessive mutation for a clotting factor has a factor level of 15 % of normal. Using Formula 38.2.1 with $N=8$ founder cells, how likely is a level of at most 1/8 of normal? What other explanations should be considered?

   **Answer** A level of at most $1/8$ needs $K\le1$: $\mathbb{P}=\frac{1+8}{256}\approx0.035$, so about 3.5 % of carriers. Other explanations: a second, independent mutation on the other X; a structural abnormality of the normal X that forces it to be inactivated (non-random inactivation selecting against it); Turner mosaicism (45,X cells); or secondary selection of cells in the tissue; and, for factor VIII, the influence of von Willebrand factor and blood group on the measured level.

3. Explain how mosaic pleiotropy and relational pleiotropy could be distinguished experimentally in the mouse.

   **Answer** Delete the gene in one tissue only with a tissue-specific Cre driver, or make chimeras of mutant and wild-type cells. Under mosaic pleiotropy each tissue lacking the gene is abnormal independently, and in chimeras only the mutant cells of each tissue are abnormal (a cell-autonomous defect). Under relational pleiotropy the deletion in the primary tissue (for MITF, the pigment epithelium) is enough to cause the defects of the secondary tissues, while deleting the gene in the secondary tissues has no effect; wild-type secondary tissue combined with mutant primary tissue is still abnormal.

4. Thalidomide was tested in rats and mice before it was marketed and caused no malformations. Explain the species difference at the molecular level and say how a drug company could now test a new CRBN-binding drug for this risk.

   **Answer** Thalidomide makes the CRBN ligase degrade SALL4 (and other neosubstrates) by creating an interface between CRBN and a zinc-finger degron of SALL4. The zinc finger of rodent SALL4 differs at amino acids that contact the drug–CRBN surface, so rodent SALL4 is not degraded and rodent embryos are resistant; human, primate and rabbit SALL4 are degraded. A new drug can be tested in human cells (for example human embryonic stem cells or iPS-derived limb-bud-like cells) for degradation of SALL4, p63, PLZF and other zinc-finger proteins by proteomics, and in a sensitive species such as the rabbit; mice with a humanized SALL4 zinc finger or humanized CRBN can be used as models.

5. Estimate the peak blood alcohol concentration in mM of a $55\,\mathrm{kg}$ woman who drinks four standard US drinks quickly, and the time until it falls below the concentration that inhibits L1 adhesion in culture.

   **Answer** $A=4\times14=56\,\mathrm{g}$; $c_{\max}\approx56/(0.55\times55)\approx1.85\,\mathrm{g\,L^{-1}}$, that is $1.85/46\times1000\approx40\,\mathrm{mM}$. The L1 threshold of $7\,\mathrm{mM}$ corresponds to $0.32\,\mathrm{g\,L^{-1}}$; at $0.15\,\mathrm{g\,L^{-1}\,h^{-1}}$ the fall from $1.85$ to $0.32\,\mathrm{g\,L^{-1}}$ takes about $(1.85-0.32)/0.15\approx10\,\mathrm{h}$. (Absorption is not instantaneous, so the true peak is somewhat lower and later; the estimate shows that a binge keeps the embryo above the threshold for most of a day.)

6. In the retinoic acid feedback model (Formula 38.4.4), what parameter mainly controls how long the RA deficit after a pulse lasts, and what would happen if CYP26 were degraded as fast as RA?

   **Answer** The deficit lasts about as long as CYP26 remains elevated, which is set by its turnover rate $\delta$: after the pulse, $C$ decays as $\mathrm{e}^{-\delta t}$ and $R$ follows the quasi-steady state $s/(k_0+kC)$, so the duration scales as $1/\delta$ (about a day for a half-life of 14 h). If CYP26 turned over as fast as RA, $C$ would track $R$ and fall back as soon as the pulse ended; $R$ would return to steady state with little or no undershoot, and an RA excess would not turn into a deficiency. The separation of time scales (slow enzyme, fast ligand) creates the overshoot.

7. Design a study to test whether a chemical has a non-monotonic dose–response for an effect on mammary gland development in mice, and say why the usual high-dose design is insufficient.

   **Answer** Expose pregnant mice (or newborn females) to vehicle and to at least five to seven doses spanning several orders of magnitude, including doses at and below human exposure, with a positive control (estradiol at a known effective dose) and a negative control; randomize, blind the analysis, use enough animals per group and litter as the unit; measure mammary branching and terminal end buds at a fixed age; fit monotonic and non-monotonic models (for example Formula 38.5.1) and compare them. Because the design of guideline studies tests few high doses and extrapolates down assuming monotonicity, a peak of effect at low doses, where the receptor is not yet down-regulated or toxicity has not set in, would be missed; low-dose groups and dense dose spacing are essential, as is control of background estrogens in feed and cages.

8. A study reports that great-granddaughters of rats exposed during pregnancy to a chemical have altered behaviour. List the controls you would ask for before accepting this as transgenerational epigenetic inheritance.

   **Answer** The F3 generation must be studied (exposure of the pregnant F0 also exposes F1 and its germ cells, [7.4.18](/7.4.18#fml-18.6.1)); transmission should be tested through both the male and the female line, with outcrosses to unexposed animals; maternal behaviour and the uterine environment must be controlled by cross-fostering or embryo transfer; genetic differences (including new mutations and mitochondrial DNA) and differences in the microbiome must be excluded; the result should be replicated in another laboratory with the same route and dose; and a carrier in the germ line (methylation, small RNAs in sperm) should be identified and shown to be sufficient, for example by transferring sperm RNA or by editing the mark.

9. Explain why retinoic acid is used to treat acute promyelocytic leukemia and why the same molecule is a teratogen.

   **Answer** In APL the PML–RARα fusion protein binds RA response elements and represses genes needed for granulocyte differentiation more strongly than normal RARα; pharmacological concentrations of all-*trans* RA bind the fusion protein, release the corepressors and allow differentiation into neutrophils, which stop dividing and die (differentiation therapy, Definition 38.7.1); arsenic trioxide additionally degrades the fusion protein. In the embryo, RA is a positional signal whose concentration is tightly regulated in space and time; excess RA changes the Hox code of the hindbrain and the cranial neural crest and induces feedback that later creates a deficiency, so the same receptor activation that is therapeutic in leukemic cells misinforms embryonic cells about their position.

10. In the dung beetle model (Formula 38.8.1), what happens to the distribution of horn length if the transition width $w$ becomes comparable with the standard deviation $\sigma$ of body size? Relate this to the difference between a reaction norm and a polyphenism.

    **Answer** When $w\ll\sigma$ almost all males lie on one of the two plateaus and the horn distribution is strongly bimodal: a polyphenism. As $w$ grows to the order of $\sigma$, more males fall on the sloping part of the sigmoid, the two modes merge and for large $w$ the horn distribution becomes unimodal, close to a linear transform of body size: a continuous reaction norm. The steepness of the developmental response (in beetles, the sensitivity of horn discs to juvenile hormone and insulin signaling at a critical size) therefore decides whether plasticity is continuous or discrete, and it can evolve.

11. Design an experiment to show that a structure of a host animal requires a bacterial symbiont for its development, and that a particular bacterial molecule is sufficient.

    **Answer** Raise hosts germ-free (sterile eggs or caesarean delivery and isolators), and compare them with conventional hosts and with germ-free hosts colonized by the single symbiont species (gnotobiotic): the structure should be abnormal in germ-free hosts and restored by the symbiont. Use symbiont mutants that cannot colonize or that lack candidate molecules, then apply the purified molecule to germ-free hosts at a defined developmental stage. In the bobtail squid, aposymbiotic hatchlings keep their ciliated appendages, colonization by *V. fischeri* induces their regression, and purified tracheal cytotoxin plus lipopolysaccharide induce regression without bacteria; for the mouse gut, *B. thetaiotaomicron* alone restores villus capillaries.
