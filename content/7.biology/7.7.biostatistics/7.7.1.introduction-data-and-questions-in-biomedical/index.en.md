---
title: "Introduction: Data and Questions in Biomedical Research"
description: What biostatistics studies; populations and samples, parameters and statistics; levels of measurement; the unit × variable × time structure of data and cross-sectional, longitudinal and time-to-event data; study design and the hierarchy of evidence; the datasets and Python environment used throughout the course.
source_hash: 84d31e215abf
---

Does a new drug work? What causes cancer? How long will a patient live? Does smoking in childhood impair lung development? None of these questions can be answered by looking at a single patient: individuals differ greatly, and even repeated measurements on the same person do not agree. *Biostatistics* is the methodology for drawing reliable conclusions in the presence of such variation. This chapter first describes the role of statistics in biomedical research and its history, and then builds the basic vocabulary of the course: populations and samples, parameters and statistics, types of variables and levels of measurement. We then distinguish cross-sectional, longitudinal and time-to-event data along the three dimensions "unit × variable × time" and survey study design and the hierarchy of evidence; these two threads, the structure of the data and the design of the study, determine which methods the later chapters use. The chapter closes with the real datasets and analysis tools used throughout the course. Rigorous mathematical statements belong to the statistics courses ([3.1](/3.1) Probability Theory, [3.2](/3.2) Statistical Inference); here we concentrate on how methods are used, on their conditions and on the interpretation of results, and link back when a derivation is needed.

## 1.1. What Is Biostatistics

### 1.1.1. Statistics and Biostatistics

The word "statistics" has three meanings:

1. Numbers: facts that have been collected and organized, such as the number of births in a given year or the outpatient visits of a hospital.
2. Statistics in the technical sense: summary quantities computed from a sample, such as the mean and the standard deviation.
3. A discipline: a body of methods for collecting, displaying, analyzing and interpreting data and for making decisions based on them.

As a discipline, statistics divides into mathematical statistics and applied statistics. Mathematical statistics develops new methods of inference and studies their properties (for example the central limit theorem and the four distributions derived from the normal distribution, $z$, $t$, $\chi^2$ and $F$); applied statistics uses these methods in a particular field. Biostatistics is the branch of applied statistics that applies statistical methods to problems in medicine and biology. The two overlap: when standard methods do not apply (censored survival times, thousands of genes tested at once), biostatisticians have to develop new methods themselves, and survival analysis, meta-analysis and the false discovery rate all arose in this way. Related English names are medical statistics, health statistics and biometrics.

By task, statistical methods fall into two groups, descriptive and inferential. Descriptive statistics summarizes the data at hand with numbers and graphs ([7.7.2](/7.7.2)); **statistical inference** draws conclusions about a population from a limited sample and states the probability that the conclusion is wrong. Probability theory is the bridge between the two: it describes the laws of randomness itself, and so makes it possible to judge whether an observed difference exceeds what random fluctuation can explain. The basic idea of statistics can be put in one sentence: recognize randomness within regularity, look for regularity within randomness, and make decisions while controlling the probability of error.

### 1.1.2. The Flow of a Study

Statistics takes part in every step of a study, not only in "computing a p-value at the end".

| Step | Statistical questions | Chapters of this course |
|---|---|---|
| Posing the question | Can the question be answered with data? What is to be compared or estimated? | This chapter |
| Designing the study | Experiment or observation? How many individuals? How to randomize? | [7.7.5](/7.7.5), [7.7.13](/7.7.13), [7.7.18](/7.7.18) |
| Collecting and organizing data | Coding, entry, checking, missing values | Section 1.6 of this chapter |
| Describing the data | Distribution, central tendency, spread, outliers | [7.7.2](/7.7.2) |
| Inference | Estimation, confidence intervals, hypothesis tests, models | [7.7.5](/7.7.5)–[7.7.21](/7.7.21) |
| Decision and reporting | Is the conclusion reliable, can it be generalized, how large is the effect? | All chapters, [7.7.22](/7.7.22) |

**Example 1.1.1 (Automatic blood pressure machines)** In the 1970s, coin-operated automatic blood pressure machines appeared in banks and shopping centers in the United States. Polk et al. (1980) recruited about 100 users at each of four machines, and a trained observer and the machine each measured systolic blood pressure; the order of the two measurements was decided at random, so that an order effect ("nervous at the first measurement") would not be confounded with the difference between the methods. Each form was entered twice and the two entries were compared, and a program then checked that every value was in a plausible range (systolic pressure between 50 and 300 mmHg). Among the 98 users at site C, the machine reading was on average $\bar d = 14.0\,\mathrm{mmHg}$ higher than the manual reading, with a standard deviation of the differences of $s_d = 11.7\,\mathrm{mmHg}$. If the two methods did not differ in the population of users, how probable would it be to see such a large mean difference in a sample of 98? By the paired $t$-test of [7.7.7](/7.7.7),

$$
t = \frac{\bar d}{s_d/\sqrt{n}} = \frac{14.0}{11.7/\sqrt{98}} = 11.8,
$$
which lies far beyond the range of random fluctuation (the probability is far below one in a thousand), so we conclude that this machine has a systematic bias. Site D ($n = 62$, $\bar d = 6.9$, $s_d = 13.6$) gives $t = 4.0$, which is also significant; at sites A and B the mean difference was only $0.5\,\mathrm{mmHg}$. This small study contains all the components of a research project: sample size calculation, randomization, data checking, description and inference. It also shows how common missing data are: only 62–98 users per site yielded valid readings, which should have been anticipated when the sample size was calculated.

### 1.1.3. A Brief History

Statistics began as the "science of the state": the English word statistics shares its origin with state, and the Statistik taught by the German scholar Hermann Conring around 1660 was a systematic description of a country's population, land and wealth; the Domesday Book of 1086 was already a national census. In 1662 John Graunt analyzed the London bills of mortality and found that slightly more boys than girls were born and that mortality was higher in the city than in the countryside, the beginning of the numerical study of the health of populations.

The second source is probability theory. Pascal and Fermat (17th century) introduced mathematical expectation starting from problems of gambling, Jacob Bernoulli proved the law of large numbers, and de Moivre obtained the normal approximation to the binomial distribution. Laplace and Gauss (1777–1855) established the normal distribution and the method of least squares in the study of errors in astronomical observations.

In the 19th century statistical methods entered medicine and public health. During the 1854 cholera epidemic in London, John Snow marked the address of every death and found that the cases clustered around the pump in Broad Street (figure below); he concluded that cholera was transmitted by contaminated water, thirty years before the pathogen was discovered. Florence Nightingale used polar area diagrams ("rose diagrams") to show that far more soldiers in the Crimean War died of preventable disease than in battle, which drove reform of army hygiene.

![A map of the 1854 cholera deaths in Soho, London (digitized coordinates from Snow's original map, HistData package). A: each dot is one death and the triangles are water pumps; orange dots are closest to the Broad Street pump. B: classification of the 578 deaths by nearest pump (straight-line distance); 359 (62%) were closest to the Broad Street pump](./plots/snow-cholera.py)

Modern statistics grew up together with genetics. Francis Galton introduced "regression" while studying the relation between the heights of parents and their children (**regression to the mean** in [3.3](/3.3)); his student Karl Pearson introduced the correlation coefficient and the $\chi^2$ test and founded *Biometrika*; R. A. Fisher laid the foundations of analysis of variance, maximum likelihood and experimental design while studying the relation between Mendelian inheritance and continuous traits. W. S. Gosset (pen name Student) derived the $t$ distribution for small-sample experiments at a brewery (1908).

In the middle of the 20th century statistics shaped the evidence standards of modern medicine. The 1948 Medical Research Council trial of streptomycin for pulmonary tuberculosis was the first clinical trial in which treatment was assigned with random numbers; the 1950 case-control study of Doll and Hill and the British doctors' cohort that began in 1951 established the relation between smoking and lung cancer; the Framingham Heart Study, begun in the same period, defined the concept of a "risk factor". Today a large cohort such as the UK Biobank provides genomes, images and electronic health records for about 500,000 people, and a **genome-wide association study** ([7.4.25](/7.4.25)) tests millions of variants at once; the scale and structure of data are changing statistics itself (Section 1.4).

## 1.2. Populations and Samples

**Definition 1.2.1 (Population and Sample)** The entire collection of individuals (or of their observed values) of interest in a study forms the **population**; the part of the population that is actually observed forms the **sample**. A population may be finite (all students of a school) or infinite or hypothetical (all patients who might take a drug in the future).

We are always interested in the population: whether a drug works for all patients of the same kind, not just for the 200 in the trial. The sample must be representative of the population. The most reliable way is random sampling, in which every individual has the same chance of being selected (a **simple random sample**, [7.7.5](/7.7.5)); individuals found for convenience (outpatients willing to participate, mice that happen to be in the laboratory) may differ systematically from the population in some respects. One must also distinguish the study population (the group that can be sampled, for example patients of a few hospitals) from the target population (the group to which the conclusions are meant to apply, for example patients nationwide): the step from the former to the latter requires subject-matter judgment, which statistics cannot guarantee.

Numbers describing a population (the population mean $\mu$, the population standard deviation $\sigma$, the prevalence $\pi$) are called parameters; they are fixed but unknown constants and are usually denoted by Greek letters. The corresponding numbers computed from a sample ($\bar x$, $s$, $\hat p$) are called **statistics** ([3.2.1](/3.2.1)) and are denoted by Latin letters. A statistic varies from sample to sample: with a different sample $\bar x$ would be different, and this difference caused by sampling is called sampling error. The central question of statistical inference is how far a statistic can be from the parameter ([7.7.4](/7.7.4), [7.7.5](/7.7.5)).

**Example 1.2.1** Around 1980 a study in East Boston measured the forced expiratory volume in one second (FEV, in L) of 654 children aged 3–19. The population is the children of that age range in the area, and the sample is these 654 children; "the mean FEV of the children in the area" is the parameter, and the sample mean $\bar x = 2.637\,\mathrm{L}$ is the statistic.

The reason statistics exists is variation. The individuals in a population must share common properties (homogeneity) for them to form a population that can be studied: averaging the lung function of children and adults together is meaningless. At the same time individuals differ (variation); if everyone had the same FEV, measuring one person would suffice. The task of statistics is to describe what members of the same population have in common despite variation, and to reveal differences between populations.

## 1.3. Variables and Levels of Measurement

### 1.3.1. Variables and Data

A variable is a characteristic of an individual, such as sex, height, serum cholesterol concentration or smoking status; data are the observed values of variables. By convention a capital letter $X$ denotes a variable (as a random variable) and a lowercase letter $x$ a specific value. In a study the role of each variable should be stated: the variable to be explained or predicted is the **response variable** (dependent variable, outcome), and the variables used to explain it are **explanatory variables** (independent variables, exposures, treatments, covariates).

### 1.3.2. Levels of Measurement

The operations that can be performed on a variable depend on its level of measurement.

**Definition 1.3.1 (Level of Measurement)** According to the relations among its values that can be compared, a variable has one of four **levels of measurement**:

| Level | Relation between values | Examples | Usual summaries |
|---|---|---|---|
| **Nominal scale** | Categories only, no order | Sex, blood group, smoking status | Counts, proportions, mode |
| **Ordinal scale** | Categories are ordered, but the gaps between adjacent grades have no definite size | Cancer stage I–IV, response (cured, improved, no effect, died), urine glucose +/++/+++ | Median, quantiles |
| **Interval scale** | Differences are meaningful, but the zero point is arbitrary | Celsius temperature, calendar year | Mean, standard deviation |
| **Ratio scale** | There is an absolute zero, and ratios are meaningful | Height, weight, concentration, survival time, cell count | Mean, standard deviation, geometric mean, coefficient of variation |

Variables on nominal and ordinal scales are together called categorical (qualitative) variables, and those on interval and ratio scales numerical (quantitative) variables.

The difference between the interval and the ratio scale lies in ratios: 40 °C is not "twice as hot" as 20 °C, but 40 kg is twice as heavy as 20 kg; the thermodynamic temperature $T/\mathrm{K}$ is on a ratio scale. In practice this difference rarely affects the choice of method, but the coefficient of variation and the geometric mean make sense only on a ratio scale ([7.7.2](/7.7.2)). Ordinal variables are often coded 1, 2, 3; these numbers indicate only order, and averaging them requires caution: the improvement from "no effect" to "improved" is not necessarily the same size as that from "improved" to "cured".

**Definition 1.3.2 (Discrete and Continuous Variables)** Among numerical variables, those whose values can be listed one by one (usually the result of counting) are **discrete variables**, such as the number of affected children in a family or the number of colonies on a culture dish; those that can take any real value in an interval (usually the result of measurement) are **continuous variables**, such as blood pressure, weight and FEV.

Information can be converted from a higher level to a lower one but not the other way round: continuous → discrete → ordinal → nominal. Age can be recorded in years or grouped as "child, young adult, middle-aged, elderly"; but data that record only the age group cannot be turned back into years. Downgrading loses information and statistical power, so the original measured values should be recorded when data are collected, and grouping should be left to the analysis, with the cut points fixed in advance (choosing cut points after looking at the data artificially creates significance). There are exceptions in the other direction as well: cell counts and read counts are discrete, but when the values are large they are often analyzed as continuous variables ([7.7.20](/7.7.20) discusses when this is not permissible).

### 1.3.3. Proportions, Rates and Ratios

Three relative numbers are easily confused:

- A proportion is the fraction of the whole made up by a part, $a/(a+b)$, between 0 and 1 and dimensionless. Example: 59 of 189 newborns had low birth weight, a proportion of $59/189 = 0.312$. Prevalence ([7.7.3](/7.7.3)) is a proportion.
- A rate is the frequency of events per unit time (or per unit person-time) and has the dimension of time. Example: 247 lung cancer deaths per 100,000 person-years. The incidence rate ([7.7.3](/7.7.3), [7.7.16](/7.7.16)) is a rate.
- A ratio is the quotient of two quantities, where the numerator need not be contained in the denominator. Examples: the sex ratio at birth (number of boys/number of girls, about 1.05), the odds $p/(1-p)$, and the ratio of the risks in two groups.

Chinese usage calls many proportions "rates" (prevalence rate, case fatality rate, response rate); when reading the literature, check the denominator and whether the quantity carries a time unit.

## 1.4. The Structure of Data: Unit × Variable × Time

### 1.4.1. Three Dimensions

A set of statistical data has three basic dimensions:

- Unit: the object observed, a patient, an animal, a cell, a protein, a brain region, the wearer of a device;
- Variable: the characteristic measured on each unit, a physiological index, a genotype, an environmental exposure;
- Time: whether each unit is measured once, measured repeatedly, or the interest lies in when some event occurs.

The standard situation of classical statistics is "$n$ mutually independent units, each measured once", that is, a sample of **independent and identically distributed** observations, arranged as a "unit × variable" matrix (panel A of the figure below) with one unit per row and one variable per column. Biomedical data often depart from this structure: the same unit is measured repeatedly, units enter the study at different times, and units are not independent (members of the same family, cells from the same culture). Different research questions give different data structures, and different data structures require different statistical methods.

**Definition 1.4.1 (Three Types of Data)** Data in which each unit is observed once, at a single time point, are **cross-sectional data**; data in which the same unit is measured repeatedly at several time points are **longitudinal data**; data in which the outcome variable is the time until some event (death, relapse, infection) occurs are **time-to-event data** (survival data).

![Real examples of the three data structures. A: cross-sectional data, the first 8 rows of the FEV data, one row per child, measured once (Tager et al. 1979). B: longitudinal data, the reaction time of 6 subjects measured once a day over 10 days of sleep restriction (sleepstudy, Belenky et al. 2003). C: time-to-event data, the follow-up of 16 patients in the Veterans Administration lung cancer trial; a filled dot at the end of a segment marks death and an open circle marks censoring; blue is standard chemotherapy and orange is experimental chemotherapy](./plots/data-types.py)

| | Cross-sectional data | Longitudinal data | Time-to-event data |
|---|---|---|---|
| Basic structure | Each unit observed once | Each unit measured several times | One event time per unit (possibly censored) |
| Role of time | None | Enters the model as a covariate | Time itself is the outcome variable |
| Core questions | Distributions, differences between groups, associations among variables | Trajectories over time, heterogeneity between individuals | The distribution of event times and the factors that influence it |
| Main difficulty | Confounding ([7.7.13](/7.7.13)) | Observations on the same unit are correlated | Censoring |
| Number of observations | Number of units | Number of units × number of measurements (not the number of independent units) | Number of units |
| Examples | One health examination, FEV, birth weight | Follow-up blood pressure, children's growth curves, sleepstudy | Survival time, time to relapse, veteran |
| In this course | [7.7.6](/7.7.6)–[7.7.14](/7.7.14) | [7.7.17](/7.7.17) | [7.7.16](/7.7.16) |

In longitudinal data one must distinguish two kinds of "measured three times": three consecutive blood pressure readings taken at the same time are technical replicates, essentially three readings of one data point, and are usually averaged; one measurement at each of three different times gives three data points that carry information about change over time, but the three values of the same person are correlated and are not equivalent to three independent individuals. Treating them as independent observations underestimates standard errors and exaggerates significance (pseudoreplication in [7.7.12](/7.7.12), and [7.7.17](/7.7.17)).

### 1.4.2. Censoring

**Definition 1.4.2 (Censoring)** In time-to-event data, if the event of a unit does not occur during the observation period (the unit is still alive when the study ends, is lost to follow-up, or withdraws for another reason), we know only that its **survival time** exceeds the time of the last observation; this is called **censoring** (more precisely, right censoring).

![Right censoring (schematic; the times are invented). A: 8 patients enter the study one after another between months 0 and 24 and are followed until death (filled dot), loss to follow-up (open circle before the end of the study) or the end of the study at month 36 (open circle on the dashed line, administrative censoring). B: the same follow-up on the study time scale, where every patient starts at 0; the analysis is carried out on this scale, and a censored patient tells us only that the survival time exceeds the observed time](./plots/censoring.py)

Censored data are incomplete information, not no information. Analyzing only the units in which the event has occurred (discarding the censored ones) systematically underestimates survival time, because people who live longer are more likely to be still alive at the end of the study and therefore censored; treating the censoring time as the time of death is biased as well. The correct approach is to build the censoring mechanism into the model (the Kaplan–Meier estimator and the Cox model, [7.7.16](/7.7.16)). These methods rely on a key assumption, that censoring is unrelated to prognosis (noninformative censoring). The assumption fails if patients whose condition worsens are more likely to drop out of the study.

### 1.4.3. Modern Biological Data

High-throughput technologies produce data of a new shape. Their common feature is that the number of variables $p$ is much larger than the number of units $n$, with structured correlation among observations:

| Data | Unit × variable | Features and challenges | Where in this wiki |
|---|---|---|---|
| Bulk transcriptome (RNA-seq) | Sample × read counts of about 60,000 genes | $p \gg n$; overdispersion of counts; thousands of simultaneous tests | [7.7.20](/7.7.20), [7.9](/7.9) |
| Single-cell transcriptome | Cell × gene | Extremely sparse: most genes are truly not expressed in a single cell, and technical effects add further "measured zeros" | [7.9](/7.9) |
| Protein structure (PDB) | Atom × three-dimensional coordinates | Hierarchical structure (atom → residue → chain); translation and rotation do not change the biological meaning | [7.8](/7.8) |
| Magnetic resonance imaging | Voxel × signal intensity | Millions of voxels, strongly correlated neighbors, registration needed across individuals | [7.6.13](/7.6.13) |
| Electroencephalography | Channel × time | Low signal-to-noise ratio, temporally correlated and nonstationary, few subjects | [7.16](/7.16) |
| Wearable devices | Individual × high-frequency time series | Continuous, irregular, many missing values | — |
| Biobanks and GWAS | Hundreds of thousands of people × millions of variants × thousands of phenotypes | Multiple testing, population stratification, genetic relatedness | [7.4.25](/7.4.25) |

Chapters 19–21 of this course treat the statistical problems common to such data: exploration and dimension reduction, large-scale inference, and prediction models; the workflows of specific omics are in bioinformatics ([7.8](/7.8)) and systems biology ([7.9](/7.9)).

## 1.5. Overview of Study Design

### 1.5.1. Experiment and Observation

**Definition 1.5.1 (Experimental and Observational Studies)** A study in which the investigator actively applies an intervention (treatment) and decides which individuals receive it is an **experimental study**; a study in which the investigator merely records the exposures and outcomes that individuals have naturally, without intervening, is an **observational study**.

The randomized controlled trial is the standard form of experimental study: the treatment is assigned at random, so that the treatment group and the control group are on average comparable in all factors, known and unknown ([7.7.5](/7.7.5), [7.7.18](/7.7.18)). Many questions cannot be studied by experiment: children cannot be randomly assigned to smoke. Observational studies therefore form the bulk of epidemiology: a cohort study follows exposed and unexposed people and compares the occurrence of outcomes; a case-control study starts from people who have and have not developed the disease and looks back at their past exposures; a cross-sectional study measures exposure and outcome at the same moment ([7.7.13](/7.7.13)).

![The usual hierarchy of evidence for questions about the effect of an exposure or treatment (schematic). Designs higher up control bias better: randomization removes confounding, and systematic reviews and meta-analyses pool several trials. This is a rule of thumb, not a law: a large, well-conducted cohort study may be more convincing than a small, biased trial](./plots/evidence-hierarchy.py)

### 1.5.2. Correlation Is Not Causation

An association found in an observational study may have another explanation. Chocolate consumption per capita and the number of Nobel laureates per 10 million inhabitants are highly correlated across 23 countries (Messerli 2012, $r = 0.79$), yet nobody believes that eating chocolate helps a country win Nobel prizes: national wealth affects both. Such a third variable is called a confounder; carrying an association at the country level over to individuals also commits the "ecological fallacy" ([7.7.15](/7.7.15)).

Causal inference is concerned with "what would happen if I did this". For this we distinguish two kinds of variables: treatment variables can be manipulated from outside (whether to take a drug, whether to quit smoking), whereas covariates exist naturally (age, sex). "What if a person's sex were changed" is not a well-defined causal question, whereas "what if everything else on a résumé stayed the same and only the sex field were changed" is: a good causal question corresponds to a definite intervention that can be applied locally without disrupting the other mechanisms of the system. [7.7.15](/7.7.15) discusses these questions systematically.

### 1.5.3. The Opening Question of the Course

**Example 1.5.1 (Do Smoking Children Have Better Lung Function?)** Of the 654 children in Example 1.2.1, 65 reported that they were smoking at the time. The mean FEV of the two groups is

| | Number | Mean FEV / L | Mean age / years | Mean height / in |
|---|---|---|---|---|
| Nonsmokers | 589 | 2.566 | 9.5 | 60.6 |
| Smokers | 65 | 3.277 | 13.5 | 66.0 |

The FEV of the smoking children is in fact higher by 0.71 L. Does this mean that smoking is good for lung function? The last two columns of the table already give a clue: the smokers are on average 4 years older and 5 inches taller, and the older and taller a child, the larger the lung capacity. The comparison of smoking with FEV is "confounded" by age. The later chapters answer the question step by step: [7.7.2](/7.7.2) plots the data, [7.7.7](/7.7.7) makes a two-sample comparison, [7.7.10](/7.7.10) adjusts for age and height by multiple regression (the coefficient of smoking becomes negative), and [7.7.15](/7.7.15) uses causal diagrams to explain what should and should not be adjusted for.

## 1.6. Data and Tools of This Course

### 1.6.1. Examples Used Throughout the Course

The course uses only a few research settings, so that they recur over many chapters, each time posing a new question on top of the previous one.

| Thread | Data | Content | Main chapters |
|---|---|---|---|
| Smoking and health | FEV | Age, FEV, height, sex and smoking status of 654 children (cross-sectional) | 1, 2, 5, 7, 8, 10, 15 |
| | birthwt | Birth weight of 189 newborns and the mother's smoking, age, weight, race and history | 2, 4–7, 9, 14, 15 |
| | Doll–Hill and British doctors | The 1950 case-control study; mortality of British doctors by amount smoked (published summary tables) | 3, 9, 13 |
| | veteran | Survival times (with censoring) of 137 patients with advanced lung cancer randomized to standard or experimental chemotherapy | 1, 16, 18 |
| Randomized trials and evidence synthesis | Physicians' Health Study (PHS) and aspirin trials | 22,071 male physicians randomized to aspirin or placebo; a meta-analysis of primary prevention trials | 3, 5, 9, 13, 18 |
| Diagnosis and screening | Low-dose CT lung cancer screening (NLST); COVID-19 antigen tests | Sensitivity, specificity, predictive values; ROC | 3, 5, 9, 14, 18, 21 |
| Laboratory assays | DNase, Puromycin, ToothGrowth | ELISA standard curve, enzyme kinetics, factorial experiment | 2, 7, 8, 10–12, 17 |
| Omics | airway | RNA-seq counts of airway smooth muscle cells before and after dexamethasone treatment | 19–21 |

Smoking and health is the backbone of the course: from description (is FEV higher in smoking children?) to comparison (are newborns of smoking mothers lighter?), from confounding and adjustment to causation, and then to prognosis (survival of lung cancer patients). This is also the history of biostatistics itself: the study of Doll and Hill, Fisher's doubts about the causal conclusion and Cornfield's rebuttal established the way of reasoning in observational studies.

The variables of the FEV and birthwt data are as follows (the other datasets are introduced in the chapters where they are used).

| FEV variable | Meaning | Type and unit |
|---|---|---|
| `id` | Child identifier | Nominal |
| `age` | Age | Discrete, years (3–19) |
| `fev` | Forced expiratory volume in one second | Continuous, L |
| `height` | Height | Continuous, inches (1 in = 2.54 cm) |
| `sex` | Sex | Nominal, 0 = female, 1 = male |
| `smoke` | Currently smoking | Nominal, 0 = no, 1 = yes |

| birthwt variable | Meaning | Type and unit |
|---|---|---|
| `bwt` | Birth weight | Continuous, g |
| `low` | Low birth weight (`bwt` < 2500 g) | Nominal, 0/1 |
| `age` | Mother's age | Discrete, years |
| `lwt` | Mother's weight at last menstrual period | Continuous, lb (1 lb = 0.4536 kg) |
| `race` | Mother's race | Nominal, 1 = white, 2 = black, 3 = other |
| `smoke` | Smoking during pregnancy | Nominal, 0/1 |
| `ptl` | Number of previous premature labors | Discrete |
| `ht` | History of hypertension | Nominal, 0/1 |
| `ui` | Uterine irritability | Nominal, 0/1 |
| `ftv` | Number of physician visits in the first trimester | Discrete |

### 1.6.2. Analysis Tools and Reproducible Analysis

Statistical analysis requires software. The code in this course is in Python: `pandas` reads and organizes data, `scipy.stats` provides the usual distribution computations and tests, `statsmodels` fits regression and generalized linear models, `lifelines` performs survival analysis, and `scikit-learn` builds prediction models; R is the other major language of the statistics community, and its use is described in [3.5.2](/3.5.2). The two languages give the same results, and the choice depends on collaborators and the conventions of the field; commercial packages such as SAS and SPSS are still common in drug regulation and the social sciences.

```python
import pandas as pd

fev = pd.read_csv("fev.csv")
print(fev.shape)          # (654, 6): 654 children, 6 variables
print(fev.dtypes)         # every column is read as a number

# declare the nominal variables, so that nobody averages them by mistake
fev["sex"] = fev["sex"].map({0: "female", 1: "male"}).astype("category")
fev["smoke"] = fev["smoke"].map({0: "no", 1: "yes"}).astype("category")

print(fev.describe())                                  # numeric variables
print(fev["smoke"].value_counts())                     # no 589, yes 65
print(fev.groupby("smoke", observed=True)[["fev", "age", "height"]].mean().round(3))
```

The last line gives the table of Example 1.5.1. A few habits that make an analysis reproducible:

- **Tidy data**: one variable per column, one observation per row, one table per type of observational unit; longitudinal data use the "long format" (one row per measurement, with the individual identifier and the time).
- Raw data are read-only: all cleaning and transformation is written in scripts that run from the raw file all the way to the results; numbers are never edited by hand in a spreadsheet.
- Check the data: examine the range of every variable, the coding of categories and the missing values (such as the range check in Example 1.1.1), and enter data twice or compare with the original records.
- Record the randomness: set random seeds for simulations and randomization so that results can be reproduced.
- Keep code, text and results together: produce reports with Jupyter notebooks or Quarto documents, and record the history of changes with Git.

"Torture the data long enough and it will confess to anything": writing the analysis plan in advance and distinguishing confirmatory from exploratory analysis is the other half of reproducibility ([7.7.18](/7.7.18), [7.7.21](/7.7.21)).

## Summary

- Biostatistics is applied statistics for medicine and biology and takes part in every step of research from design to reporting (Example 1.1.1). Descriptive statistics summarizes the data at hand; statistical inference draws conclusions about the population from a sample and states the probability of error.
- Population and sample (Definition 1.2.1): a parameter is a fixed unknown constant of the population, and a **statistic** is an estimate that varies from sample to sample; representativeness comes from random sampling.
- The level of measurement (Definition 1.3.1) determines which operations are allowed:

  | Level | Nominal | Ordinal | Interval | Ratio |
  |---|---|---|---|---|
  | Order | No | Yes | Yes | Yes |
  | Differences meaningful | No | No | Yes | Yes |
  | Ratios meaningful | No | No | No | Yes |
  | Central tendency | Mode | Median | Mean | Mean, geometric mean |

  Information can only be converted from higher to lower levels (Definition 1.3.2); proportions, rates and ratios differ in denominator and dimension.
- Data structure = unit × variable × time (Definition 1.4.1): cross-sectional, longitudinal and time-to-event data correspond to distributions and associations, trajectories of change, and event times, respectively; time-to-event data are characterized by censoring (Definition 1.4.2), and discarding the censored units causes bias. Modern omics and imaging data have $p \gg n$.
- Experimental and observational studies (Definition 1.5.1); the hierarchy of evidence has randomized controlled trials and meta-analyses at the top; correlation is not causation. That smoking children have higher FEV (Example 1.5.1) is the opening question of the course, and the answer is confounding.

## Questions

1. A study recruits 300 patients with type 2 diabetes from three hospitals in a city and measures their HbA1c (glycated hemoglobin), obtaining a mean of 7.8%. Identify the population, sample, parameter, statistic, variable and data in this study. Can the conclusion be generalized to diabetic patients nationwide?

   **Answer** The study population is the patients with type 2 diabetes of these three hospitals (or of the city); the sample is these 300 patients; the parameter is the mean HbA1c of the study population (unknown); the statistic is the sample mean 7.8%; the variable is "the HbA1c of a patient"; the data are the specific values of the individual patients (such as 6.9%, 8.4%). Generalizing to the whole country (the target population) requires an argument that the patients of these three hospitals represent patients nationwide: patients of large hospitals may have more severe disease and may come more often from cities, and statistics itself cannot guarantee this.

2. Determine the level of measurement of the following variables: (a) ABO blood group; (b) TNM stage of a tumor; (c) body temperature (°C); (d) serum creatinine concentration; (e) pain score (0–10); (f) the number of epileptic seizures in one week.

   **Answer** (a) Nominal; (b) ordinal; (c) interval (the zero point is arbitrary; on the thermodynamic scale in K it would be a ratio scale); (d) ratio (continuous); (e) ordinal; strictly the gaps between adjacent scores need not be equal, but with 11 grades it is often approximated as a numerical variable; (f) a discrete variable on a ratio scale (a count, with an absolute zero).

3. A study records systolic blood pressure in three groups, "< 120, 120–139, ≥ 140 mmHg", and later wants to compute the mean systolic pressure. Can this be done? What does it suggest for data collection?

   **Answer** No. After grouping we know only which interval each person falls into; the original values are lost, and can only be approximated by class midpoints (the group ≥ 140 does not even have an upper bound), so the loss of information is irreversible. The lesson is to record the original measured values (continuous variables) when collecting data, to do any grouping at the analysis stage with cut points specified in advance, and to remember that a variable can be converted only from a higher level to a lower one.

4. Classify each of the following relative numbers as a proportion, a rate or a ratio: (a) 6 of 40 patients in a ward develop a hospital-acquired infection; (b) a cohort has 3.2 myocardial infarctions per 1000 person-years; (c) the ratio of the lung cancer mortality of smokers to that of nonsmokers is 10; (d) the ratio of the numbers of boys to girls among newborns is 1.06.

   **Answer** (a) A proportion ($6/40 = 0.15$; the infected are included in the denominator); strictly it is the cumulative incidence proportion over a period of time. (b) A rate, with the dimension of time (person-years). (c) A ratio (the quotient of two rates, i.e., a rate ratio). (d) A ratio (the boys are not part of the number of girls).

5. In a trial of an antihypertensive drug, each patient has blood pressure measured once at baseline, week 4, week 8 and week 12, each time as the mean of three consecutive readings. What is this data structure? How many "independent" observations do 100 patients provide?

   **Answer** Longitudinal data. The three consecutive readings are technical replicates and are averaged, so each patient has one value at each time, $100 \times 4 = 400$ values in all; but the 4 values of the same patient are correlated, and the independent units remain the 100 patients. Treating the 400 values as independent observations underestimates the standard error; treating the 1200 readings as independent would be even more wrong.

6. In a follow-up study after lung cancer surgery, the investigators analyze only the patients who died during follow-up and obtain a median survival time of 14 months. What is wrong with this result?

   **Answer** Using only the uncensored (dead) patients underestimates survival time: patients who survive longer are more likely to be still alive at the end of the study and to be censored, so the excluded ones are exactly those with a good prognosis, and 14 months is too low. One should use the Kaplan–Meier method, which exploits the information that censored patients survived "at least this long" ([7.7.16](/7.7.16)).

7. In the cholera map of Section 1.1.3, 359 deaths were closest to the Broad Street pump. Does this alone prove that cholera is transmitted by water? What other evidence did Snow need?

   **Answer** It does not prove it by itself. The cases may cluster around the pump because the population there is densest and poorest, or because the "miasma" is strongest at that spot. Snow's strong evidence came from comparisons: a nearby brewery and a workhouse had their own water supply, and few of their workers and inmates fell ill; some people who lived far away but made a special trip to fetch water in Broad Street fell ill; later he compared households supplied by two water companies and living mixed in the same neighborhoods, and the death rate from cholera among customers of the company that drew water from the contaminated stretch of the Thames was several times higher, a "natural experiment" in which the two groups were similar in other respects and differed mainly in their water source. The epidemic was already declining when the pump handle was removed, so this cannot serve as evidence on its own.

8. (Open question) Someone finds that elderly people who take vitamin D supplements every day have fewer fractures and argues that all elderly people should take vitamin D. What type of study is this? What is the best design for answering whether vitamin D supplementation reduces fractures?

   **Answer** This is an observational study (possibly cross-sectional or cohort). Elderly people who take supplements voluntarily tend to be healthier, to pay more attention to diet and exercise and to have higher socioeconomic status, and these factors themselves lower the risk of fracture, so they are confounders; reverse causation is also possible (people with existing disease do not take, or stop taking, supplements). The best design is a randomized controlled trial: random assignment to vitamin D or placebo, double-blind, with fracture as the primary endpoint and the sample size calculated from the expected fracture rate. In fact, several large randomized trials (such as the VITAL trial) found that vitamin D supplementation does not reduce fractures in the general elderly population, contrary to the impression from observational studies; this is the point of the hierarchy of evidence.

9. In Example 1.5.1, why can we not conclude that "smoking is beneficial" from the higher FEV of the smoking group? Propose an analysis that does not need a complex model to test your explanation.

   **Answer** The smoking children are on average 4 years older and 5 inches taller, and age and height themselves determine the size of the lungs; the difference between the groups mainly reflects age, and the comparison of smoking with FEV is confounded by age. A simple test is stratification: compare the FEV of smokers and nonsmokers only among children of the same age (such as 13 or 15 years), or compare within each age and then combine. In the actual data, in each age group from 12 to 16 the mean FEV of smokers is lower than that of nonsmokers (for example at age 13: 3.38 vs 3.53 L, with 13 and 30 children; at age 15: 3.09 vs 3.92 L, with 10 and 9 children), which supports the explanation; the groups are small, and a rigorous adjustment is the regression of [7.7.10](/7.7.10).
