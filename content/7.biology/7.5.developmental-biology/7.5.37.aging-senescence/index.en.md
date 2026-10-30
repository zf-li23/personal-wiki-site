---
title: Aging and Senescence
description: "Aging as the last stage of development. Definitions, survival curves and the Gompertz–Makeham law; the evolutionary theories: the selection shadow, mutation accumulation, antagonistic pleiotropy and the disposable soma, with a model of optimal investment in maintenance; lifespan, maturity and body mass; the cellular and molecular hallmarks, from DNA damage, telomeres and epigenetic clocks to NAD⁺, senescent cells and stem-cell exhaustion; the conserved insulin/IGF and mTOR pathways and dietary restriction; progeroid syndromes; interventions; animals with negligible senescence; human life expectancy."
---

Development does not end with maturity: after reproduction begins, most animals change in a characteristic way until they die, and this last phase of the life cycle is aging. It differs from the earlier phases in one essential respect: it is not, as far as we know, a program selected for its own sake, but the consequence of selection weakening with age. This chapter first defines aging by its demographic signature, the exponential rise of mortality with age, then explains why evolution permits it, describes the cellular and molecular changes that accompany it and the conserved pathways that set its pace, and ends with premature aging syndromes, interventions, animals that hardly age, and the human lifespan. Two topics treated elsewhere are only linked here: **cellular senescence**, **telomeres** and the **senescence-associated secretory phenotype** in [7.3.25](/7.3.25#sec-25.7), and DNA repair in [7.2.8](/7.2.8). The statistical methods of survival analysis (life tables, the Kaplan–Meier estimator, proportional hazards) belong to [7.7](/7.7), and the evolution of life histories to [7.10](/7.10).

## 37.1. What Aging Is

### 37.1.1. Definitions

**Definition 37.1.1 (Aging)** **Aging** (senescence of the organizm) is the progressive, time-dependent decline of an organizm's physiological functions, its capacity for self-regulation, repair and adaptation to its environment, that lowers its probability of survival and its fertility with age (after Birren and Zarit 1985).

Aging is defined statistically, at the level of a population: its defining feature is a rising probability of death with age, observed in cohorts, and individuals differ in how fast they age, both genetically and through their environment. The characteristics of aging (in humans, gray hair, wrinkled skin, loss of muscle mass and bone, arthritic joints, declining vision, hearing and memory) affect all individuals of a species; the diseases of aging (**cancer**, cardiovascular disease, **type 2 diabetes**, neurodegeneration) affect many but not all. Two quantities must be distinguished: the maximum lifespan of a species, the longest reliably recorded life (122.45 years for humans, Jeanne Calment, 1875–1997), and the life expectancy of a population, the mean age at death of a cohort under given mortality conditions, which is a property of populations and their environment, not of the species.

Organs and cell types age at different rates. Cells have their own lifespans, from days (neutrophils, gut epithelium) through months (red blood cells, 120 days) to the life of the organizm (most **neurons**, oocytes, lens fiber cells, many cardiomyocytes); the long-lived cells cannot be replaced and must be maintained, the short-lived ones depend on **stem cells** ([7.5.36](/7.5.36)).

### 37.1.2. The Gompertz–Makeham Law

Benjamin Gompertz (1825) noticed that, in human life tables, the probability of dying in the next year increases roughly geometrically with age over the adult range. William Makeham (1860) added an age-independent term.

**Definition 37.1.2 (Gompertz–Makeham Law)** Let $T$ be the age at death, $S(x) = \mathbb{P}(T > x)$ its **survival function** and $\mu(x) = -S'(x)/S(x)$ its **hazard function** (the age-specific mortality rate). The **Gompertz–Makeham law** is

$$
\mu(x) = A + B\,\mathrm{e}^{\gamma x},
\tag{37.1}
$$
where $A \ge 0$ is the age-independent (background or extrinsic) mortality, $B > 0$ the initial level of age-dependent mortality and $\gamma > 0$ its rate of increase. The **mortality-rate doubling time** is $\ln 2/\gamma$. With $A = 0$ it is the Gompertz law.

**Formula 37.1.1 (Survival and Lifespan Under Gompertz–Makeham)** Integrating $-\ln S(x) = \int_0^x\mu$,

$$
S(x) = \exp\Big(-Ax - \frac B\gamma\bigl(\mathrm{e}^{\gamma x} - 1\bigr)\Big),
$$
and for $A = 0$ the median lifespan is $x_{1/2} = \frac1\gamma\ln\bigl(1 + \frac{\gamma\ln 2}{B}\bigr)$, and the density of ages at death $\mu(x)S(x)$ has its mode at $x^* = \frac1\gamma\ln\frac\gamma B$. Moreover, multiplying the Gompertz hazard by a constant $c$ is equivalent to shifting age: $cB\mathrm{e}^{\gamma x} = B\mathrm{e}^{\gamma(x - \Delta)}$ with $\Delta = \ln(1/c)/\gamma$.

**Proof** $\int_0^x(A + B\mathrm{e}^{\gamma s})\,\mathrm{d}s = Ax + \frac B\gamma(\mathrm{e}^{\gamma x} - 1)$. Setting $S = \frac12$ with $A = 0$ gives the median. The density $f = \mu S$ has $(\ln f)' = \gamma - B\mathrm{e}^{\gamma x}$, which vanishes at $x^*$. The last identity is immediate. $\square$

**Example 37.1.1** For a present-day population with $\gamma = 0.1\ \mathrm{yr^{-1}}$ and $B = 1.7 \times 10^{-5}\ \mathrm{yr^{-1}}$, the doubling time is 6.9 years, the modal age at death $10\ln(0.1/1.7\times10^{-5}) \approx 87$ years and the Gompertz median 83 years. An intervention that halves mortality at every adult age ($c = \frac12$) postpones the whole curve by $\ln 2/\gamma \approx 7$ years: in a Gompertz world, halving the risk of death buys one doubling time. Typical values of $\gamma$ correspond to doubling times of about 8 years in humans, 3–4 months in laboratory mice and about 10 days in *Drosophila*. Because mortality is exponential, a reduction of hazard by a constant factor, as achieved by most interventions in mice (37.6), gives a lifespan gain of a fixed number of doubling times, which is why the same intervention adds weeks to a mouse and might add years to a human.

![The Gompertz-Makeham law. A: hazard on a logarithmic scale. Points: a life table estimated from a simulated cohort of 100 000 people (A = 3e-4, B = 1.7e-5, gamma = 0.10 per year); the least-squares fit of log hazard at ages 30-95 recovers gamma and a mortality doubling time of 6.9 years. A 1900-like population has much higher background mortality A. Flat dotted lines: the age-independent hazards measured in laboratory Hydra (about 0.6 % per year) and naked mole-rats (about 1/10 000 per day). B: survival curves: lowering A makes the curve more rectangular; lowering gamma moves its fall to later ages (dots: median lifespan)](./plots/gompertz.py)

The law fits human adult mortality between about 30 and 90 years remarkably well; at very old ages the rise appears to slow, and whether mortality reaches a plateau above about 105 years is debated, because the data are few and age records often wrong. Across countries and centuries, the falls in mortality have come mostly through $A$ (infections, accidents, childbirth) and through the level $B$ at given ages, with $\gamma$ changing much less; the survival curve has become more rectangular, and the age of greatest mortality has moved later. Survival curves of laboratory *Drosophila* have the same shape on a time scale of weeks. Estimating hazards and survival from censored data is the subject of [7.7](/7.7).

## 37.2. Why Do We Age? Evolutionary Theories

Aging seems paradoxical: **natural selection** should favor organizms that maintain themselves indefinitely. The resolution (Medawar 1952; Williams 1957; Hamilton 1966) is that the strength of selection falls with age. Even a non-aging organizm dies eventually of extrinsic causes (predators, disease, accidents), so few individuals reach old ages, and they have already produced most of their offspring.

**Formula 37.2.1 (The Selection Shadow)** In a population with survival to age $x$ equal to $l(x)$ and fecundity $m(x)$, a mutation that changes the mortality at age $a$ by a small amount affects fitness in proportion to the reproduction still to come after age $a$,

$$
s(a) \propto \int_a^\infty l(x)m(x)\,\mathrm{e}^{-rx}\,\mathrm{d}x,
$$
with $r$ the growth rate of the population (Hamilton 1966). The force of selection is maximal and constant before the age of first reproduction and declines afterwards, reaching zero once reproduction has ended.

Three theories build on this.

**Definition 37.2.1 (Evolutionary Theories of Aging)** The **mutation accumulation** theory (Medawar) holds that deleterious mutations whose effects appear only late in life are hardly removed by selection and accumulate in the population. The **antagonistic pleiotropy** theory (Williams) holds that alleles with beneficial effects early in life and harmful effects late in life are favored, so that aging is a by-product of selection for early fitness. The **disposable soma theory** (Kirkwood 1977) holds that, because resources are limited, an organizm must divide them between reproduction and the maintenance and repair of its body; selection sets the investment in maintenance at a level that keeps the soma in good condition through the expected reproductive life but not beyond.

The disposable soma theory is a physiological form of antagonistic **pleiotropy**: genes that shift resources to reproduction raise early fitness at the price of later decline. It predicts that species exposed to higher extrinsic mortality evolve faster aging, and that maintenance mechanisms (DNA repair, antioxidant defences, protein quality control) are more effective in long-lived species. Both predictions are borne out by comparisons: opossums on a predator-free island age more slowly than mainland ones (Austad 1993), birds and bats, which escape predators by flying, live much longer than terrestrial mammals of the same size, and fibroblasts from long-lived mammals are more resistant to stress.

**Formula 37.2.2 (A Disposable-Soma Model)** An organizm maturing at age 1 allocates a fraction $u$ of its resources to maintenance and $1 - u$ to reproduction, with fecundity $b(1 - u)$. Maintenance slows intrinsic aging: $\mu(x) = A + B\,\mathrm{e}^{\gamma(u)x}$ with $\gamma(u) = \gamma_0\mathrm{e}^{-ku}$. In a stationary population, fitness is lifetime reproduction,

$$
R_0(u) = b(1 - u)\int_1^\infty S_u(x)\,\mathrm{d}x,
$$
and the optimal investment $u^*$ satisfies $\frac{\mathrm{d}}{\mathrm{d}u}\ln R_0 = 0$, that is, $\dfrac{1}{1 - u^*} = \dfrac{\partial}{\partial u}\ln\int_1^\infty S_u(x)\,\mathrm{d}x\Big|_{u^*}$: the marginal loss of fecundity equals the marginal gain in expected reproductive lifetime.

**Example 37.2.1** With $B = 0.01$, $\gamma_0 = 1.5$ and $k = 3$ (time in units of the age at maturity), the optimal investment is $u^* \approx 0.52$ for extrinsic mortality $A = 0.02$, $0.41$ for $A = 0.1$ and $0.15$ for $A = 0.5$; the median lifespan falls from about 10 to about 1 time unit. When the world is dangerous, extra years of maintenance are rarely used, and selection favors spending on reproduction now. Two qualifications apply: if extrinsic mortality falls equally at all ages, it does not change the optimum in all models (it does when it affects some ages more, or when maintenance also protects against extrinsic deaths), and the model has no explicit mechanism for "damage", only a parameterized rate of aging.

![A disposable-soma model (Formula 37.2.2). A: lifetime reproduction as a function of the fraction u of resources spent on maintenance, for three levels of extrinsic mortality A; dots mark the optimum, which shifts towards less maintenance as A increases. B: the optimal investment and the resulting median lifespan fall as extrinsic mortality rises: high-risk environments select for fast aging](./plots/disposable-soma.py)

Among mammals, lifespan increases with the age at first reproduction (the mouse breeds at about six weeks and lives at most four years; the elephant breeds at about 12 years and lives about 65) and with body mass, as an **allometry** ([7.5.34](/7.5.34)).

**Formula 37.2.3 (Lifespan Allometry)** Across non-flying mammals, maximum lifespan $L$ scales with adult body mass $M$ approximately as $L \approx a\,M^{b}$ with $b \approx 0.2$; a fit to the 18 species in the figure gives $L \approx 12\ \mathrm{yr} \times (M/\mathrm{kg})^{0.22}$.

Large animals are less exposed to predators and grow slowly, consistent with the evolutionary theory; the scatter around the line is as informative as the trend. Bats of a few grams live 30–40 years, eight to ten times longer than predicted; the naked mole-rat, a 35 g eusocial rodent living underground, lives more than 37 years; humans live about four times longer than a mammal of their size. All are protected from extrinsic mortality by flight, burrows or social and technical defences.

![Maximum recorded lifespan and adult body mass in 22 mammals (approximate values from the AnAge database). The dashed line is the fit for 18 non-flying, non-burrowing species (lifespan of about 12 years times M^0.22, M in kg). Bats, the naked mole-rat and humans (open circles) live far longer than their mass predicts](./plots/lifespan-allometry.py)

## 37.3. Cellular and Molecular Hallmarks

Many changes accompany aging, and the difficulty is to tell causes from consequences. López-Otín and colleagues (2013, updated 2023) list twelve "hallmarks" that appear with age, accelerate aging when aggravated experimentally and slow it when reduced. They are grouped as primary damage, the responses to it, and the integrative consequences.

| Hallmark | Evidence (mainly mice) | Notes |
|---|---|---|
| Genomic instability | DNA-repair defects cause progeroid syndromes (37.5); **somatic mutations** accumulate | rate per year inversely related to species lifespan |
| **Telomere** attrition | telomerase-deficient mice and patients age prematurely; **telomerase** gene therapy extends mouse lifespan | 7.3.25 |
| Epigenetic alterations | methylation clocks; loss of **heterochromatin**; partial **reprogramming** reverses marks | sirtuins, **chromatin** modifiers |
| Loss of **proteostasis** | aggregates in neurodegeneration; chaperones extend lifespan in worms and flies | |
| Disabled **macroautophagy** | **autophagy** required for lifespan extension by dietary restriction and reduced **mTORC1** | |
| Deregulated nutrient sensing | insulin/IGF-1, mTORC1, AMPK, sirtuins (37.4) | the most robust interventions act here |
| Mitochondrial dysfunction | mtDNA mutator mice (proofreading-deficient polymerase γ) age prematurely | ROS role revised |
| **Cellular senescence** | clearance of p16-positive cells extends lifespan and healthspan | 7.3.25 |
| Stem-cell exhaustion | fewer or less functional **stem cells** in blood, muscle, hair follicle, brain | clonal hematopoiesis |
| Altered intercellular communication | heterochronic parabiosis; circulating factors | |
| Chronic inflammation ("inflammaging") | rising IL-6 and other cytokines; SASP | |
| Dysbiosis | gut microbiota of young animals extends lifespan of short-lived killifish | |

### 37.3.1. DNA Damage and Somatic Mutation

Every cell suffers thousands of **DNA lesions** a day, from replication errors, spontaneous hydrolysis and oxidation, and environmental agents; most are repaired ([7.2.8](/7.2.8)), but some leave mutations and some leave cells arrested or dead. The capacity of fibroblasts to repair ultraviolet damage correlates with species lifespan (Hart and Setlow 1974), and several human progeroid syndromes are DNA-repair defects (37.5). **Somatic mutations** accumulate linearly with age: about 40 single-nucleotide substitutions per year in human intestinal stem cells (Blokzijl and colleagues 2016). Sequencing of intestinal crypts from 16 mammalian species, from mouse to human and tiger, found that the somatic **mutation rate** per year varies about 15-fold and is inversely proportional to lifespan, so that each species reaches a similar burden, about 3000 substitutions per crypt genome, at the end of its life (Cagan and colleagues 2022). This is evidence that **mutation rate** co-evolves with lifespan, though not that mutations alone cause aging: mice with elevated mutation rates do not always age faster.

### 37.3.2. Telomeres

Telomeres shorten at each division in cells that lack **telomerase**, and critically short telomeres trigger a DNA-damage response and **replicative senescence** ([7.3.25](/7.3.25#sec-25.7.2)). Mice and humans with telomerase deficiencies (dyskeratosis congenita, telomere syndromes) show premature failure of renewing tissues (bone marrow, skin, lung). In mice, expressing telomerase **reverse transcriptase** with an adeno-associated virus from one year of age increased median lifespan by 24%, and from two years by 13%, without raising **cancer** incidence (Bernardes de Jesus and colleagues 2012). Telomere length is only a weak predictor of an individual's lifespan, and laboratory mice have long telomeres and short lives, so telomere attrition is one factor among many; in humans, short telomere length in leukocytes is associated statistically with age-related disease, and very long telomeres with some cancers.

### 37.3.3. Epigenetic Drift and Clocks

**DNA methylation** changes with age at many CpG sites: some gain and some lose methylation in a reproducible way, while the overall pattern becomes noisier (epigenetic drift). The methylation of the **promoters** of the estrogen receptor genes, for example, rises steadily with age in the colon and the vascular wall and is higher still in atherosclerotic plaques (Issa and colleagues 1994; Post and colleagues 1999). Methylation is copied with an error rate per site and division of the order of a few percent, far higher than DNA replication, which allows epimutations to accumulate.

**Definition 37.3.1 (Epigenetic Clock)** An **epigenetic clock** is a regression model that predicts age from the **DNA methylation** levels of a set of CpG sites; the difference between predicted and chronological age ("age acceleration") is used as a measure of biological aging.

Horvath (2013) trained a clock on about 8000 samples of 51 tissues and cell types; 353 CpG sites, some gaining and some losing methylation with age, predicted chronological age with a median error of about 3.6 years across tissues, and cells from early embryos and **embryonic stem cells** had an epigenetic age near zero. Clocks trained on blood (Hannum and colleagues 2013), and second-generation clocks trained on mortality and physiological measures (PhenoAge, GrimAge) or on the pace of aging (DunedinPACE), predict morbidity and mortality beyond chronological age. Tumors often appear epigenetically older than the surrounding tissue. **Reprogramming** to iPS cells resets the clock to zero, and partial reprogramming reduces it (37.6). Whether the methylation changes cause aging or only record it is not known.

### 37.3.4. Mitochondria, Reactive Oxygen Species and NAD⁺

The free radical theory (Harman 1956) proposed that **reactive oxygen species** (ROS) produced by mitochondria damage macromolecules and cause aging; about 0.1–2% of the electrons in the **respiratory chain** leak to oxygen, depending on conditions. Overexpressing catalase or superoxide dismutase extended lifespan in some fly and worm studies, and mice expressing catalase targeted to mitochondria live longer. But many tests failed: mice heterozygous for the mitochondrial superoxide dismutase *Sod2*, with more oxidative damage, have normal lifespans; worms lacking superoxide dismutases can live longer; and antioxidant supplements have not extended lifespan in mammals or reduced mortality in human trials. ROS are also signals, and mild mitochondrial stress can extend lifespan by inducing protective responses (mitohormesis). Mitochondrial dysfunction itself is clearly harmful: mice with a proofreading-deficient **mitochondrial DNA** polymerase γ accumulate mtDNA mutations and age prematurely, with hair loss, kyphosis, anemia and a lifespan of about a year (Trifunovic and colleagues 2004), largely without increased ROS.

The coenzyme NAD⁺, required for redox metabolism and as a substrate of sirtuins and of the DNA-repair enzymes PARPs, declines with age in many tissues, partly because the NADase CD38 rises on inflammatory cells. Supplementing its precursors nicotinamide mononucleotide (NMN) or nicotinamide riboside improves several age-related functions in mice, and NAD⁺ depletion contributes to the phenotypes of the DNA-repair disorders xeroderma pigmentosum group A, Cockayne syndrome and ataxia telangiectasia, in which PARP activation consumes NAD⁺ (Fang and colleagues 2014, 2016). In humans the precursors raise blood NAD⁺, but trials so far show modest or no effects on physiological measures and none on aging; their benefits remain unproven.

### 37.3.5. Senescent Cells, Stem Cells and Circulating Factors

Senescent cells accumulate with age and secrete the SASP (inflammatory cytokines, proteases, **growth factors**), which damages tissue function and spreads senescence; clearing them genetically or with **senolytic** drugs delays age-related decline and extends median lifespan in mice ([7.3.25](/7.3.25#sec-25.7.7)). Stem cells decline in number or function: **hematopoietic stem cells** shift towards myeloid output and lose regenerative capacity, and expanded clones carrying mutations in genes such as *DNMT3A* and *TET2* (clonal hematopoiesis of indeterminate potential) are found in more than 10% of people over 70 and raise the risk of **leukemia** and cardiovascular disease; muscle **satellite cells** regenerate less, partly through loss of Notch signaling; the melanocyte stem cells of the hair follicle become stranded in a compartment where they no longer receive the Wnt signal to mature, and the hair grays (Sun and colleagues 2023).

Is the decline intrinsic to the stem cells or a property of their environment? Heterochronic parabiosis, the surgical joining of the circulations of an old and a young mouse, restored Notch activation and regeneration in old muscle **satellite cells** and the proliferation of old liver cells (Conboy and colleagues 2005), and young plasma improved neurogenesis and memory in old mice, whereas old plasma impaired them in young ones (Villeda and colleagues 2011, 2014). The systemic environment thus contributes. The report that the TGF-β family member GDF11 is the rejuvenating factor that declines in old blood (Loffredo and colleagues 2013) was contradicted by later work, which found that circulating GDF11 does not decline with age, that the assays had confounded it with the related myostatin (GDF8), and that GDF11 inhibits muscle regeneration (Egerman and colleagues 2015); its role remains unresolved. Diluting old blood with saline and albumin also rejuvenates several tissues (Mehdipour and colleagues 2020), which suggests that removing harmful factors from old blood matters at least as much as adding young ones.

## 37.4. Conserved Longevity Pathways

The first genes that extend lifespan were found in *C. elegans*. Under crowding or starvation, worm larvae enter the dauer state, an alternative third larval stage that does not feed and can survive months instead of the normal adult life of about three weeks without shortening the subsequent adult life; dauer entry is controlled by an insulin-like pathway. Mutations in *age-1* (Friedman and Johnson 1988), which encodes the catalytic subunit of phosphatidylinositol 3-kinase, and weak alleles of *daf-2* (Kenyon and colleagues 1993), which encodes the insulin/IGF-1 receptor homolog, double adult lifespan, and the extension requires the FOXO transcription factor DAF-16, which activates genes for stress resistance, antimicrobial defence, protein quality control and metabolism. Removing the germ-line precursors extends lifespan further, through a steroid signal; *daf-2* mutants without a germ line lived on average about 125 days (Arantes-Oliveira and colleagues 2003). In competition with wild-type worms on limited food, however, *daf-2* mutants are outcompeted within a few generations: a direct demonstration of the cost of longevity in reduced fitness.

The pathway is conserved. In *Drosophila*, females homozygous for mutations in *chico*, which encodes an **insulin receptor** substrate, live about 50% longer, and overexpressing dFOXO in the fat body extends lifespan. In mice, females heterozygous for the IGF-1 receptor (*Igf1r*$^{+/-}$) live about 30% longer (males about 16%, not significant) (Holzenberger and colleagues 2003); dwarf mice lacking growth hormone or its receptor (Ames and Snell dwarfs, *Ghr* knockouts) live 40–60% longer; and among dog breeds, small breeds with low IGF-1 live longer than large ones. In humans, variants of *FOXO3* are associated with longevity in several populations, and people with Laron syndrome (growth hormone receptor deficiency) are protected from cancer and diabetes, though not demonstrably longer-lived. In yeast, **deletion** of *SCH9*, the homolog of the S6 kinase downstream of TOR, triples chronological lifespan.

The second pathway is **mTORC1**, a kinase complex that integrates **growth factors**, amino acids and energy to drive translation and growth and to suppress **autophagy**. Reducing its activity extends lifespan in yeast, worms, flies and mice. Rapamycin, an mTORC1 inhibitor, fed to genetically heterogeneous mice from 600 days of age (equivalent to about 60 human years), increased the age at 90% mortality by 14% in females and 9% in males (Harrison and colleagues 2009), the first drug shown to extend lifespan in mammals by the rigorous standards of the multi-center Interventions Testing Program; later studies found larger effects with earlier or intermittent treatment. Rapamycin suppresses the immune response and impairs glucose tolerance, and its use for aging in humans is not established.

![Conserved pathways that set lifespan, in activity-flow notation. Insulin or IGF-1 acts through its receptor, PI3K and AKT; AKT inhibits the transcription factor FOXO, which promotes stress resistance and repair, and activates mTORC1, which with amino acids promotes translation and growth and inhibits autophagy. AMPK, rapamycin and dietary restriction inhibit mTORC1; dietary restriction also lowers insulin and IGF-1. Right: the names of the components in worms, flies and mammals, and lifespan extensions obtained by reducing their activity](./plots/longevity-pathways.py)

Dietary restriction (DR), a reduction of food intake by 20–40% without malnutrition, extends lifespan in yeast, worms, flies, rodents (McCay and colleagues 1935: about 40% in rats) and many other species, acting through these same pathways (lower insulin/IGF-1 and mTORC1, activation of AMPK and autophagy); in some organizms its effects depend on particular nutrients, such as protein or methionine, rather than on calories. In rhesus macaques two long studies disagreed. At the Wisconsin National Primate Research Center, a 30% restriction begun in adults reduced age-related deaths (50% of controls survived at the time of analysis against 80% of restricted animals) and delayed diabetes, cancer, cardiovascular disease and brain atrophy (Colman and colleagues 2009, 2014). At the National Institute on Aging, restriction begun in young or old monkeys did not increase survival, although it improved metabolic health (Mattison and colleagues 2012). The designs differed: the Wisconsin controls ate ad libitum a purified, high-sucrose diet, whereas the NIA controls were themselves fed fixed portions of a natural-ingredient diet and were lighter, so the NIA comparison was between two partially restricted groups; the diets also differed in protein and fat sources and in supplementation (both groups supplemented at NIA, only the restricted group at Wisconsin). A joint analysis (Mattison and colleagues 2017) concluded that restriction benefits health and survival in primates, depending on diet composition, age of onset and the reference diet. In humans, a 12% reduction in calories over two years (the CALERIE trial) improved cardiometabolic risk factors and modestly slowed a methylation measure of the pace of aging (Waziry and colleagues 2023); effects on lifespan cannot be measured directly.

## 37.5. Progeroid Syndromes

Progeroid syndromes are genetic disorders with some features of accelerated aging. They are "segmental": each affects some tissues and not others, and none reproduces aging as a whole, but they point to processes that matter.

**Definition 37.5.1 (Progeroid Syndrome)** A **progeroid syndrome** is a hereditary disorder in which several features of normal aging appear prematurely; examples are Werner syndrome, Hutchinson–Gilford progeria, Cockayne syndrome and ataxia telangiectasia.

- Werner syndrome (autosomal **recessive**; mutations in *WRN*, a RecQ helicase with exonuclease activity needed for replication, repair and telomere maintenance). Growth stops at puberty (no adolescent growth spurt); gray hair, cataracts, skin atrophy, **type 2 diabetes**, osteoporosis, atherosclerosis and cancers (often **sarcomas**) appear in the twenties and thirties; the median age at death is now about 54 years. Patients' fibroblasts undergo far fewer divisions in culture than normal ones.
- **Hutchinson–Gilford progeria syndrome** (HGPS; dominant, almost always de novo). Children appear normal at birth, then fail to grow, lose hair and subcutaneous fat, and develop stiff joints, thin skin and progressive atherosclerosis, dying of heart attack or stroke at a median age of about 14.5 years; cognition is unaffected, and there is no increase in cancer or neurodegeneration.
- Cockayne syndrome (*ERCC6* or *ERCC8*, transcription-coupled nucleotide excision repair) causes growth failure, neurodegeneration and photosensitivity; xeroderma pigmentosum (global nucleotide excision repair) causes a thousandfold increase in sunlight-induced skin cancer and, in some groups, neurodegeneration; ataxia telangiectasia (*ATM*, the kinase that signals DNA double-strand breaks) causes cerebellar degeneration, immunodeficiency and cancer.

**Example 37.5.1 (Progerin)** Lamin A, a component of the **nuclear lamina** beneath the **inner nuclear membrane**, is made as prelamin A, which ends in a CaaX motif (Cys–Ser–Ile–Met). The cysteine is farnesylated, the last three residues are removed and the cysteine methylated, and the protease ZMPSTE24 then cuts off the last 15 residues, including the farnesyl group. In HGPS, the mutation c.1824C>T in exon 11 of *LMNA* does not change the encoded amino acid (p.G608G) but activates a cryptic splice donor site, so that 150 nucleotides (50 amino acids) are deleted from the mRNA. The **deletion** removes the second ZMPSTE24 cleavage site; the protein, **progerin**, remains farnesylated and anchored to the membrane, accumulates, deforms the nucleus into lobes and blebs, and disturbs **heterochromatin**, DNA repair and mechanical resistance, especially in vascular smooth muscle cells, which are subjected to strain and are lost from the arteries. The mechanism suggested a drug: the farnesyltransferase inhibitor lonafarnib, approved in 2020, extends the mean survival of children with HGPS by about 2.5 years. In mouse models, correcting the mutation with an adenine **base editor** delivered by a virus restored normal splicing in many tissues and more than doubled lifespan (Koblan and colleagues 2021). Small amounts of **progerin** are also made by the normal cryptic splice site, and they increase with age in normal people.

![Lamin A processing and the origin of progerin. A: prelamin A ends in CSIM; it is farnesylated, trimmed and methylated, and ZMPSTE24 cleaves off the last 15 residues with the farnesyl group, giving mature lamin A. B: in Hutchinson-Gilford progeria the silent mutation c.1824C>T activates a cryptic splice site that removes 50 amino acids including the second ZMPSTE24 site; progerin stays farnesylated and anchored to the inner nuclear membrane, and nuclei become misshapen. Lonafarnib inhibits farnesylation](./plots/progerin.py)

## 37.6. Interventions

Several interventions extend lifespan or healthspan in mice; their translation to humans is the open question.

| Intervention | Effect in mice | Status in humans |
|---|---|---|
| Dietary restriction | lifespan up to 30–50% (strain-dependent) | metabolic benefits (CALERIE); lifespan unknown |
| Rapamycin and rapalogues | lifespan +9–26% even when started late | trials of immune and other endpoints |
| **Senolytics** | median lifespan about +25% (genetic clearance), healthspan in disease models | early trials |
| Telomerase gene therapy | median lifespan +13–24% | none |
| Partial reprogramming (OSKM) | progeroid mice: lifespan about +30%; old wild-type mice: improved tissues | none |
| Heterochronic plasma, blood dilution | rejuvenation of several tissues | trials of plasma exchange |
| NAD⁺ precursors | improved functions; lifespan effects small | modest effects |
| Metformin | inconsistent | observational associations; trial planned |

Partial reprogramming deserves comment, because it links aging to development. Expressing the four Yamanaka factors (Oct4, Sox2, Klf4, c-Myc; [7.3.24](/7.3.24#sec-24.7.2)) continuously in mice causes teratomas, since cells become pluripotent. Ocampo and colleagues (2016) expressed them cyclically, two days on and five days off, in mice carrying the *Lmna* G609G mutation that models HGPS: cells did not lose their identity, epigenetic marks of aging (H3K9me3, H4K20me3) were partly restored, and the mice lived about 30% longer. In normal old mice, long-term cyclic induction of the factors improved skin and kidney (Browder and colleagues 2022), and in the retina the factors without c-Myc restored the youthful methylation pattern and vision after nerve injury (Lu and colleagues 2020). These experiments suggest that part of aging is a loss of epigenetic information that can be reset without changing cell type; how much, and whether safely in humans, is unknown.

## 37.7. Exceptions: Negligible Senescence

In some animals mortality does not rise with age, and fertility does not fall.

- *Hydra*. Polyps maintained in the laboratory for more than four years showed no increase in mortality or decline in reproduction (Martínez 1998); a large study found an annual mortality of about 0.6%, constant with age (Schaible and colleagues 2015). The body is continuously renewed from its three stem-cell lineages ([7.5.35](/7.5.35)); the transcription factor FoxO maintains stem-cell **self-renewal**, and its knockdown reduces it (Boehm and colleagues 2012). The cold-induced sexual reproduction of *Hydra oligactis*, however, is followed by aging and death, with loss of interstitial **stem cells**, so negligible senescence is a property of asexual life in some lineages.
- The naked mole-rat (*Heterocephalus glaber*). In more than 3000 records, the hazard did not increase with age, staying about 1 in 10 000 per day, and breeding females remained fertile into their thirties (Ruby and colleagues 2018). The animals rarely get **cancer**, have efficient protein quality control and high-molecular-mass **hyaluronan** in their tissues.
- Turtles and tortoises. In many species kept in zoos, mortality rises very slowly or not at all with age (da Silva and colleagues; Reinke and colleagues 2022), and a 60-year-old box turtle laid as many eggs as younger ones.
- Long-lived vertebrates in the wild include the bowhead whale (more than 200 years, estimated from amino-acid racemization in the eye lens), the Greenland shark (about 390 ± 120 years, from radiocarbon dating of the eye lens nucleus) and rockfishes of more than 200 years.
- Salamanders. Axolotls and newts regenerate repeatedly into old age; their efficient clearance of senescent cells by macrophages may contribute (Yun and colleagues 2015; [7.5.35](/7.5.35)).
- Reverse development. The hydrozoans *Turritopsis dohrnii* and *Hydractinia carnea* can transform their medusae, after reproduction, back into a ball of cells that forms a polyp, restarting the life cycle; in principle the cycle can be repeated indefinitely, though individuals in nature die of other causes.
- Monarch butterflies (*Danaus plexippus*) of the migratory generation live about eight months instead of two, because **juvenile hormone** is not made and reproduction is suspended; giving them **juvenile hormone** restores fertility and shortens life.

The diversity of demographic patterns is wide: across 46 species, mortality curves range from steep rises (humans, many mammals) through flat lines (*Hydra*) to declines with age (some plants and the desert tortoise), so the Gompertz shape is common but not universal (Jones and colleagues 2014).

## 37.8. Human Lifespan

For most of history, life expectancy at birth was 25–40 years, held down by infant and child mortality and infections; in England in the 1780s it was about 35 years. Since about 1840, the record life expectancy, the highest national value in each year, has risen almost linearly by about three months per year (Oeppen and Vaupel 2002), first through falling child mortality and then, since the mid-twentieth century, through falling mortality at older ages. In China, life expectancy at birth was about 35 years around 1949, 68 years in 1981, 77.9 in 2021 and 79.0 in 2024. Whether there is a limit is debated: the maximum reported age at death has not increased since the 1990s, which some interpret as a limit near 115 years (Dong, Milholland and Vijg 2016) and others as statistical noise; gains in life expectancy in the longest-lived countries have slowed since 1990, and the survival needed for life expectancies above 100 years seems implausible without slowing aging itself (Olshansky and colleagues 2024).

What do the longest-lived people have in common? Centenarians are more often women; they tend to have long-lived relatives, and their offspring have lower rates of cardiovascular disease and diabetes; the *APOE* ε2 allele is enriched and ε4 depleted among them, and *FOXO3* variants are associated with longevity. Most of them delay or escape major disease until late, so their period of disability is compressed. But the heritability of lifespan in the general population is low, probably below 10% once **assortative mating** is accounted for (Ruby and colleagues 2018), and many claims about places with exceptional numbers of very old people rest on unreliable age records. Evidence on lifestyle (not smoking, physical activity, diet, social ties) is largely observational, though consistent. For a population, as for a mouse, the Gompertz arithmetic of Example 37.1.1 holds: halving mortality at all adult ages would add about one doubling time, eight years.

## Summary

| Topic | Key points |
|---|---|
| Definitions | aging (Definition 37.1.1); maximum lifespan versus life expectancy; Gompertz–Makeham hazard $A + B\mathrm{e}^{\gamma x}$ (Definition 37.1.2, Eq. (37.1)); survival, median and the age-shift rule (Formula 37.1.1); halving mortality buys $\ln2/\gamma$ (Example 37.1.1) |
| Evolution | selection shadow (Formula 37.2.1); mutation accumulation, antagonistic **pleiotropy**, disposable soma (Definition 37.2.1); optimal maintenance falls with extrinsic mortality (Formula 37.2.2, Example 37.2.1); lifespan $\propto M^{0.2}$ with bats, mole-rats and humans above the line (Formula 37.2.3) |
| Hallmarks | DNA damage and somatic mutation (rate inversely related to lifespan); **telomeres**; epigenetic clocks (Definition 37.3.1); mitochondria (ROS theory revised), NAD⁺; senescent cells, stem-cell exhaustion, parabiosis and the GDF11 controversy |
| Pathways | insulin/IGF-1–FOXO (*daf-2*, *age-1*, *daf-16*, *chico*, *Igf1r*); mTORC1 and rapamycin; dietary restriction and the reconciled monkey studies |
| Progeroid syndromes | Definition 37.5.1; Werner (*WRN*), HGPS and progerin (Example 37.5.1), Cockayne, XP, A-T |
| Interventions | dietary restriction, rapamycin, **senolytics**, telomerase, partial reprogramming |
| Exceptions | negligible senescence in *Hydra*, naked mole-rat, turtles; reverse development; diversity of mortality curves |
| Humans | life expectancy rising about 3 months per year in record countries; limits debated; low heritability of lifespan |

## Questions

1. From a life table, the mortality rate at ages 60 and 70 is 0.010 and 0.022 per year. Estimate $\gamma$, the mortality doubling time, and the mortality at 80 if the Gompertz law holds. How long would a drug that reduces mortality by 25% at all ages above 60 extend median survival from 60?

   **Answer** $\gamma = \ln(0.022/0.010)/10 = \ln 2.2/10 \approx 0.079\ \mathrm{yr^{-1}}$; doubling time $\ln2/0.079 \approx 8.8$ years; at 80, $0.022 \times 2.2 = 0.048$. A hazard multiplied by $c = 0.75$ shifts the curve by $\ln(1/0.75)/\gamma = 0.288/0.079 \approx 3.6$ years (Formula 37.1.1), so median survival is extended by about 3.6 years (slightly less if background mortality $A$ is not negligible).

2. Why does the force of selection decline with age even in a population without aging? Use Formula 37.2.1 for a population with constant mortality $A$ and constant fecundity from age $\alpha$.

   **Answer** With $l(x) = \mathrm{e}^{-Ax}$, $m(x) = m$ for $x \ge \alpha$ and $r = 0$ (stationary), $s(a) \propto \int_{\max(a,\alpha)}^\infty m\mathrm{e}^{-Ax}\,\mathrm{d}x = \frac mA\mathrm{e}^{-A\max(a,\alpha)}$. It is constant up to $\alpha$ and then falls exponentially: extrinsic death alone makes late effects matter less, because fewer individuals survive to experience them. Selection therefore cannot efficiently remove late-acting deleterious alleles (mutation accumulation) and favors alleles with early benefits and late costs (antagonistic **pleiotropy**).

3. Design an experiment with *Drosophila* to test the prediction that high extrinsic mortality selects for faster aging. What confounding effect must be controlled?

   **Answer** Maintain replicate populations under high versus low imposed adult mortality (random culling at a fixed rate each generation, independent of age and condition) for many generations, then measure the intrinsic mortality curves of their descendants under common benign conditions. The prediction is a steeper Gompertz slope (larger $\gamma$) and earlier reproduction in the high-mortality lines. Confounding: culling that depends on condition or density can select for robustness instead (Stearns and colleagues found faster aging under high random mortality); also control for density and larval environment and rear all lines in a common garden for two generations before measuring to remove parental effects.

4. A mouse dies at most at about 4 years and a little brown bat of 8 g at 34 years. Use Formula 37.2.3 to compute how much longer than expected each lives, and explain the difference in evolutionary terms.

   **Answer** Prediction $12.3 \times M^{0.22}$ with $M$ in kg: mouse ($0.025$ kg) $12.3 \times 0.025^{0.22} = 12.3 \times 0.44 \approx 5.4$ years (observed 4, a little below); bat ($0.008$ kg) $12.3 \times 0.008^{0.22} \approx 12.3 \times 0.345 \approx 4.2$ years (observed 34, about eight times more). Flight lowers extrinsic mortality from predators, so selection favors investment in maintenance and slow life histories (one pup a year, long reproductive life); hibernation and low body temperature during torpor may add to it.

5. Explain how the **silent mutation** of HGPS changes the protein, why the disease is dominant, and why a farnesyltransferase inhibitor can help.

   **Answer** c.1824C>T does not change glycine 608 but creates a better splice donor within exon 11, so splicing removes 150 nucleotides and the protein lacks 50 amino acids including the ZMPSTE24 site needed to remove the farnesylated C-terminus. Progerin remains farnesylated and membrane-bound and acts as a dominant toxic protein, disturbing the lamina even in the presence of normal lamin A from the other allele (a gain-of-function, dominant-negative effect). Blocking farnesylation keeps progerin from being anchored to the membrane, reducing its toxicity; the benefit is partial because other prenylation (geranylgeranylation) and the deleted region still alter the protein.

6. Rapamycin increased the age at 90% mortality by 9% in male and 14% in female mice when given from 600 days. Assuming a Gompertz mortality with a doubling time of 100 days, by what factor did rapamycin reduce the hazard?

   **Answer** For a lifespan of about 1100–1200 days at 90% mortality, a 9–14% increase is about 100–160 days, i.e. 1.0–1.6 doubling times. A shift of $\Delta$ corresponds to a hazard factor $c = \mathrm{e}^{-\gamma\Delta} = 2^{-\Delta/T_2}$: about $2^{-1} = 0.5$ for males and $2^{-1.6} \approx 0.33$ for females. The treatment roughly halved to thirded the hazard in old mice, a large effect, though the shift in a Gompertz curve need not be uniform when treatment starts late.

7. The two rhesus monkey studies of caloric restriction reached opposite conclusions. List the design differences and explain which comparison measures what.

   **Answer** Control diet: Wisconsin controls ate ad libitum (and became heavier); NIA controls were given fixed amounts and were themselves mildly restricted, so the NIA contrast was smaller. Diet composition: Wisconsin used a purified diet high in sucrose (about 28%), NIA a natural-ingredient diet with less sugar and with fish oil and plant phytochemicals. Supplementation: both groups at NIA, only the restricted group at Wisconsin. Age at onset: adults at Wisconsin; young and old cohorts at NIA. Wisconsin therefore measured restriction against an unhealthy, overfed diet, NIA restriction against a healthy, controlled diet; both found metabolic benefits, and the joint analysis supports a benefit that depends on the reference diet and on age at onset.

8. Is an epigenetic clock a measure of aging or of time? Describe how one would test whether the methylation changes it reads cause aging.

   **Answer** It is trained to predict chronological age, so it partly measures time; age acceleration (clock age minus actual age) predicts mortality and morbidity, so it captures some biological aging. Causality tests: change the methylation of clock sites (for example with dCas9 fused to DNMT3A or TET1) in cells or mice and measure function and lifespan; ask whether interventions that extend lifespan (dietary restriction, rapamycin, dwarf mutations) slow the clock in mice (they do); test whether resetting the clock by partial reprogramming restores function (in the retina it did, and blocking the demethylases TET1/TET2 prevented the benefit). Correlation alone, or reversal of the clock by an intervention, does not prove that the sites themselves matter.

9. Why is negligible senescence in *Hydra* compatible with the evolutionary theories of aging?

   **Answer** In an asexual polyp that reproduces by budding throughout life and continuously renews all its cells from stem cells, there is no distinct germ line and soma; the soma is itself the reproducing tissue, and its maintenance is selected as long as the animal keeps budding. Fecundity does not decline with age, so the force of selection (Formula 37.2.1) does not fall to zero. In *Hydra oligactis*, sexual reproduction is followed by aging, as expected when resources are diverted to gametes and reproduction is concentrated at one time.

10. (Open question) Partial **reprogramming** reverses some marks of aging. What are the risks and what would you require before testing it in humans?

    **Answer** Risks: loss of cell identity, **dedifferentiation** and teratoma formation (if cells reach **pluripotency**), cancer from c-Myc and Klf4, effects on non-dividing cells such as **neurons** that cannot be replaced, organ failure (liver and gut failure occurred in mice with strong induction), and difficulty in controlling dose and duration in each tissue. Requirements: tissue-restricted, inducible and reversible delivery (for example OSK without c-Myc in the eye), long-term safety and efficacy in several animal species including primates, clear functional endpoints (vision, kidney function) rather than clocks alone, monitoring for tumors, and first trials in a local, accessible organ with a serious unmet need.
