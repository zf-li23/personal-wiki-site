---
title: "Prelude: Why Regression?"
description: Where the word "regression" comes from (Galton's quincunx, sweet peas and family heights, regression toward the mean and the bivariate normal distribution), and what to do before fitting a model, from formulating the problem and exploratory data analysis to the terminology and steps of a regression analysis.
---

Why is the most widely used tool of statistics called "regression"? The name records a discovery, not a method: in the 1870s and 1880s Francis Galton found that the offspring of unusually large or small parents are, on average, less extreme than their parents. He called this "regression toward mediocrity", and his attempt to explain it produced the regression line, the **correlation coefficient** and, eventually, multiple regression. The first half of this chapter retells that story, because the mathematics behind it (the **conditional expectation** of a **bivariate normal distribution**, [3.1.6](/3.1.6)) is exactly the starting point of the course. The second half collects what has to be done before any model is fitted: understanding the problem and the data, exploring the data, and fixing the vocabulary and the steps of a regression analysis. The **simple linear regression model** itself is set up in [3.3.2](/3.3.2).

## 1.1. The History of Regression

### 1.1.1. Least Squares Before Regression

Regression-type problems were first considered in the eighteenth century, to aid navigation by astronomy: several noisy observations had to be combined into estimates of a few unknown quantities. Legendre published the method of **least squares** in 1805; Gauss claimed to have used it a few years earlier, and in 1809 he showed that least squares is the optimal solution when the errors are normally distributed. Until late in the nineteenth century the method was used almost exclusively in the physical sciences, where the unknowns were constants of nature. Its move into biology and the social sciences, where the "unknown" is a relationship between variables, came through Galton's work on heredity.

### 1.1.2. Galton's Quincunx

Darwin's theory of natural selection left a lurking problem. Heritable variation is passed to the offspring, and the same parents produce offspring with different heritable traits, so the variability of a population should grow from one generation to the next. Yet the dispersion of a population is stable over the short term; indeed this stability is essential for the very definition of a species. How can both be true?

Galton studied the question with the *quincunx* (Galton board): shot falls from a funnel through rows of pegs, each peg deflecting it left or right, and piles up in compartments at the bottom in an approximately normal shape. A population whose trait is normally distributed is like the shot in the upper compartments; passing through the pegs (the random variation between parent and offspring) spreads every compartment into a small normal curve, so the offspring generation is more dispersed than the parents. In his 1877 version, Galton inserted *inclined chutes* between the upper compartments and the pegs: the chutes move the shot toward the center, and he called this movement *reversion*. The chutes compensate for the increase in dispersion caused by the pegs, so that the population dispersion stays constant; the board also shows how the offspring of one upper stature group are traced through the process to the bottom.

**Example 1.1.1 (The Mathematics of the Quincunx)** Measure positions from the center and let the parent generation be $F\sim\mathcal{N}(0,\sigma_1^2)$.

- The inclined chutes contract every position by a factor $c<1$: $Z=cF\sim\mathcal{N}(0,c^2\sigma_1^2)$.
- Row $i$ of pegs adds a change $X_i$. If the $X_i$ are iid with mean $0$, then by the **central limit theorem** $X=\sum_{i=1}^nX_i$ is approximately $\mathcal{N}(0,\sigma^2)$, and its **variance** $\operatorname{Var}(X)=\sum_{i=1}^n\operatorname{Var}(X_i)$ grows with the number of rows.
- If $X$ is independent of $F$, the offspring generation is $S=Z+X\sim\mathcal{N}(0,c^2\sigma_1^2+\sigma^2)$.

The population is stable, $S\overset{d}{=}F$, exactly when $c^2\sigma_1^2+\sigma^2=\sigma_1^2$, that is, $c=\sqrt{1-\sigma^2/\sigma_1^2}$: the contraction toward the center must be strong enough to absorb the spread added by the pegs. Each upper compartment $F=f$ produces a normal curve $\mathcal{N}(cf,\sigma^2)$ at the bottom, and these local normal curves add up to the overall normal curve of $S$ (a normal distribution whose mean is itself normally distributed is again normal).

![The quincunx as a model of heredity: the chutes contract the parent distribution N(0, 1) to N(0, 0.64), the pegs add independent N(0, 0.36) noise, and the offspring distribution is again N(0, 1); on the right, the offspring of five parent groups are normal curves centered closer to the mean, and their sum is the overall normal curve](./plots/quincunx-stability.py)

### 1.1.3. Sweet Peas, Family Heights and Regression Toward the Mean

In 1875 Galton distributed packets of sweet pea seeds of seven different weights to friends, had them grown, and compared the weights of the daughter seeds with those of the mother seeds. Taking for each mother weight the median weight of the daughters, the points lay roughly on a straight line. A slope of $0$ would have meant that the daughters' weights do not depend on the mothers' at all, contradicting the heritability of "characters"; a slope of $1$ would have meant that the population spreads out indefinitely. Galton's first documented study of this type suggested a slope of about $0.33$: positive, which affirmed heritability, but less than $1$. This is the prototype of *regression toward the mean*: an individual whose parent deviates from the mean by some amount deviates, on average, by a smaller amount in the same direction. Galton designated the slope by $r$, for regression.

Galton believed that he had estimated a single, universal heredity constant,

$$
y-\bar y=r(x-\bar x).
$$
Different sets of measurements, however, have different spreads, and he adjusted the observed slope by the ratio of the spreads,

$$
y-\bar y=r\,\frac{S_y}{S_x}(x-\bar x),
$$
using an estimated value of $r$; as the measure of spread he used the quantile deviation (the semi-interquartile range). In standard units the slope is $r$ itself, a dimensionless number.

In 1886 Galton published the heights of $928$ adult children of $205$ pairs of parents. He summarized each pair by the *mid-parent* height (the average of the father's height and $1.08$ times the mother's height, to put women's heights on the men's scale) and cross-tabulated the children's heights against the mid-parents' heights. Plotting the median height of the children against the mid-parent height gave a line of slope about $2/3$: "When mid-parents are taller than mediocrity, their children tend to be shorter than they; when mid-parents are shorter than mediocrity, their children tend to be taller than they." This is the regression effect.

Is the effect biological? Suppose the table is read the other way round, with the children's heights as the given variable and the mid-parents' median height as the response. The resulting line is again flatter than the diagonal: the parents of unusually tall children are, on average, less tall than their children. Regression toward the mean occurs in both directions, and Galton found the same for the heights of brothers. An effect that appears whichever variable is put first cannot be a law of inheritance; the explanation must be statistical, not biological.

### 1.1.4. Two Regression Lines and the Bivariate Normal Distribution

Galton smoothed the counts of his table to make the pattern stand out, and saw rough elliptical contours emerge around the densest portion. He found a theoretical representation for the table, the **bivariate normal distribution**, whose contours of equal density are ellipses, and two "regression lines": the expected height of the children as a function of the mid-parent height, and the expected height of the mid-parent as a function of the children's height. In modern language, each regression line is a *regression function*

$$
m(x)=\mathbb{E}(Y\mid X=x),
$$
the **conditional expectation** of the response given the value of the other variable. For $(X,Y)\sim\mathcal{N}(\mu_X,\mu_Y,\sigma_X^2,\sigma_Y^2,\rho)$ both regression functions are linear ([3.1.6](/3.1.6)):

$$
\mathbb{E}(Y\mid X=x)=\mu_Y+\rho\frac{\sigma_Y}{\sigma_X}(x-\mu_X),\qquad\mathbb{E}(X\mid Y=y)=\mu_X+\rho\frac{\sigma_X}{\sigma_Y}(y-\mu_Y).
$$
In standard units $u=(x-\mu_X)/\sigma_X$, $v=(y-\mu_Y)/\sigma_Y$ they read $v=\rho u$ and $u=\rho v$; since $\lvert\rho\rvert\le1$, the predicted value is never more extreme, in standard units, than the given value. This is regression toward the mean, now a theorem rather than an empirical rule, and Galton's slope $r$ is the **correlation coefficient**.

**Example 1.1.2** Let $(X,Y)$ have a standard bivariate normal distribution with $\rho=0.5$. The line $\mathbb{E}(Y\mid X=x)=0.5x$ has slope $0.5$; the line $\mathbb{E}(X\mid Y=y)=0.5y$, drawn in the same $(x,y)$-plane, is $y=2x$ and has slope $2$. Both pass through the center, and the major axis $y=x$ of the elliptical contours lies between them: neither regression line is the axis of the ellipse. If $\rho=0$, the two lines are the horizontal and the vertical axis (knowing one variable says nothing about the other); if $\rho=1$, the distribution is concentrated on the line $y=x$ and the two regression lines coincide with it.

![Left: a sample of 200 points from a standard bivariate normal distribution with rho = 0.5, with contours of the density, the major axis y = x, and the two regression lines E(Y | X = x) = 0.5 x and E(X | Y = y) = 0.5 y; right: simulated parent and child heights with the median child height in each parent group, which follows a line flatter than the diagonal](./plots/two-regression-lines.py)

### 1.1.5. Galton's Interpretation and Its Legacy

Galton explained the regression of brothers' heights with a simple variance-component model. Write the heights of two brothers as

$$
F=G+V_1,\qquad S=G+V_2,
$$
where $G$ is an unobserved persistent (genetic) component that blood relatives hold in common, with $\mathbb{E}(G)=p$ (the population mean), and $V_1,V_2$ are unobserved transitory random components with $\mathbb{E}(V_1)=\mathbb{E}(V_2)=0$, uncorrelated with $G$ and with each other. Then $\operatorname{Cov}(F,S)=\operatorname{Var}(G)$, and if all components are normal,

$$
\mathbb{E}(S\mid F=f)=p+\frac{\operatorname{Var}(G)}{\operatorname{Var}(G)+\operatorname{Var}(V_1)}(f-p).
$$
The coefficient lies strictly between $0$ and $1$. In Galton's words (*Natural Inheritance*, 1889), "the unknown brother has two different tendencies, the one to resemble the known man, and the other to resemble his race. The one tendency is to deviate from P as much as his brother, and the other tendency is not to deviate at all. The result is a compromise."

This also resolved Darwin's problem. Regression toward the mean is not a force pulling the population back; it is a simple consequence of the imperfect correlation between parents and offspring, and it is exactly what keeps the population dispersion in an approximate evolutionary equilibrium: the movement of individuals from the population center toward the extremes is balanced by the movement back.

Galton went one step further. He noticed that earlier generations (grandparents, great-grandparents) also influence an individual's characteristics, with diminishing effects. He had hit upon the kernel of multiple regression: a variable may be influenced by a multitude of causes of greater and lesser importance, and some of these causes may overlap with one another.

The impact was far-reaching.

- A measure of association, the **correlation coefficient**, was born.
- Francis Edgeworth, G. Udny Yule and Karl Pearson took the idea to higher dimensions: partial correlations, multidimensional least squares and principal components of variance (the forerunner of **principal component analysis**). Statistics had jumped off the two-dimensional page of tables of numbers and become a technology for problems of great complexity.
- Galton played no important role in the acceptance of Darwin's theory, but his methods became central to twentieth-century biology. His correlation and variance-component models found, by statistical means alone, some of the results that followed from the rediscovery of Mendel's work in 1900; in 1918 Ronald A. Fisher derived the correlations and partial correlations of relatives under Mendelian inheritance for all kinds of relationships, and much of modern quantitative genetics was born.
- The variance-component idea became key to quantitative and educational psychology, and Galton's separation of permanent and transitory effects is at the heart of Milton Friedman's permanent income hypothesis (*A Theory of the Consumption Function*, 1957), work recognized by his 1976 Nobel Prize.

## 1.2. Before the Analysis

### 1.2.1. From the Problem to the Data

A statistical study starts with a problem, proceeds with the collection of data, continues with the data analysis and finishes with conclusions. A common mistake is to plunge into a complex analysis without paying attention to what the objectives are, or even to whether the data are appropriate for the proposed analysis.

To formulate the problem correctly:

- understand the physical background;
- understand the objective, and make sure you know what the client wants;
- put the problem into statistical terms.

Then ask how the data were collected.

- Were they obtained by a designed sample survey or experiment, or are they observational? How the data were collected has a crucial impact on what conclusions can be drawn.
- Is there nonresponse? The data you do not see may be just as important as the data you do see.
- Are there missing values? This is a common problem that is troublesome and time-consuming to handle.
- How are the data coded? In particular, how are the qualitative variables represented?
- What are the units of measurement?
- Beware of data-entry errors and other corruption of the data, and perform sanity checks.

### 1.2.2. Exploratory Data Analysis

**Exploratory data analysis**, promoted by John Tukey, encourages statisticians to explore the data before modeling them, and possibly to formulate hypotheses that could lead to new data collection and experiments. It is an approach to analyzing data sets that summarizes their main characteristics, often with visual methods:

- numerical summaries: means, standard deviations, maxima and minima, correlations, and whatever else is appropriate to the data set;
- graphical summaries: for one variable, **boxplots**, histograms and density plots (**kernel density estimation**, [3.2.3](/3.2.3)); for two or more variables, scatterplots and scatterplot matrices; interactive and dynamic graphics;
- a search for outliers, data-entry errors, skewed or unusual distributions, and structure.

These steps are simple but vital.

**Example 1.2.1 (Pima Indians Diabetes Data)** The National Institute of Diabetes and Digestive and Kidney Diseases conducted a study of $768$ adult female Pima Indians living near Phoenix. The variables are the number of pregnancies, the plasma glucose concentration two hours after an oral glucose tolerance test, the diastolic blood pressure (mmHg), the triceps skin fold thickness (mm), the two-hour serum insulin ($\mu$U/ml), the body mass index (weight in kg divided by the square of the height in m), the diabetes pedigree function, the age (years), and a test result: whether the patient showed signs of diabetes. Before any analysis we should know the purpose of the study and how the data were collected, and then look at the data.

```r
library(faraway)
summary(pima)
sort(pima$diastolic)   # 35 zeros: a blood pressure of 0 is impossible
```

The summary shows a minimum of $0$ for glucose, diastolic blood pressure, triceps thickness, insulin and BMI. A blood pressure of $0$ is impossible, and sorting the values shows $35$ zeros followed by $24, 30, 30, 38,\dots$: the zeros are missing values coded as $0$. Treating them as numbers would distort every mean and every fit, so they are recoded as `NA`. The test result is a qualitative variable coded $0/1$ and should be declared a factor.

```r
pima$diastolic[pima$diastolic == 0] <- NA
pima$glucose[pima$glucose == 0] <- NA
pima$triceps[pima$triceps == 0] <- NA
pima$insulin[pima$insulin == 0] <- NA
pima$bmi[pima$bmi == 0] <- NA
pima$test <- factor(pima$test)
levels(pima$test) <- c("negative", "positive")
summary(pima)   # now reports NA counts: 5 (glucose), 35 (diastolic), 227 (triceps), 374 (insulin), 11 (bmi)
```

After recoding, the mean diastolic blood pressure rises from $69.1$ to $72.4$, and the test variable is summarized as $500$ negative and $268$ positive cases. The usual plots follow:

```r
hist(pima$diastolic)                          # histogram
plot(density(pima$diastolic, na.rm = TRUE))   # kernel density estimate
plot(diabetes ~ diastolic, pima)              # scatterplot of two quantitative variables
plot(diabetes ~ test, pima)                   # side-by-side boxplots for a factor
pairs(pima)                                   # scatterplot matrix
```

### 1.2.3. Terminology

A regression relates a *response variable* (response, output, dependent variable), written $Y$, to one or more *explanatory variables* (predictors, inputs, independent variables), written $X$ or $X_1,\dots,X_p$. In R the relationship is written as a formula `Y ~ X`.

| Formula | Name |
|---|---|
| $Y\sim X$ | simple regression |
| $Y\sim X_1+\cdots+X_p$ | multiple regression: more than one $X$ in one formula |
| $Y_1\sim X,\ \dots,\ Y_q\sim X$ | multivariate regression: more than one $Y$, in different formulae |
| $Y_k\sim X_1+\cdots+X_p$, $k=1,\dots,q$ | multivariate multiple regression: several $X$'s to predict several $Y$'s, each $Y$ in its own formula, usually based on the same data |

The form of the analysis depends on the types of the variables. In the Pima data:

| Formula | Response | Predictors | Analysis |
|---|---|---|---|
| `diabetes ~ diastolic + bmi` | continuous | quantitative | multiple regression ([3.3.7](/3.3.7)) |
| `bmi ~ diastolic + test` | continuous | quantitative and qualitative | analysis of covariance |
| `diastolic ~ test` | continuous | qualitative only | **analysis of variance** ([3.3.12](/3.3.12)) |
| `test ~ diastolic + bmi` | qualitative (binary) | quantitative | **logistic regression** |
| `pregnant ~ diastolic + bmi` | discrete (count) | quantitative | Poisson regression |

This course treats continuous responses; the last two rows belong to generalized linear models.

### 1.2.4. Objectives and Steps of a Regression Analysis

A regression analysis may aim at

- prediction of future observations;
- assessment of the effect of the explanatory variables on the response, or of the relationship between them;
- a general description of the structure of the data.

It usually proceeds in the following steps:

1. statement of the problem;
2. selection of potentially relevant variables;
3. data collection;
4. model specification;
5. choice of the fitting method;
6. model fitting;
7. model validation and criticism;
8. use of the chosen model(s) for the solution of the posed problem.

The steps are not a one-way street: validation (step 7) often sends us back to the specification (step 4), and the course follows the same loop, from fitting ([3.3.2](/3.3.2)) and inference ([3.3.3](/3.3.3), [3.3.4](/3.3.4)) to diagnostics and remedies ([3.3.5](/3.3.5), [3.3.6](/3.3.6)).

## Summary

- "Regression" is named after Galton's regression toward the mean: the offspring of extreme parents are, on average, less extreme. His quincunx shows that this contraction is exactly what keeps a population's dispersion stable from generation to generation.
- The effect is statistical: it appears in both directions and is a consequence of imperfect correlation. For a bivariate normal distribution the two regression functions $\mathbb{E}(Y\mid X=x)$ and $\mathbb{E}(X\mid Y=y)$ are different straight lines with standardized slope $\rho$, and neither is the major axis of the contour ellipses.
- Galton's work produced the correlation coefficient and the idea of multiple regression, and through Pearson, Yule and Fisher it shaped modern statistics and quantitative genetics.
- Before modeling: formulate the problem in statistical terms, find out how the data were collected, and explore the data with numerical and graphical summaries and sanity checks (zeros that are really missing values, wrongly coded factors).
- The type of the response and of the predictors determines the analysis: regression, analysis of covariance, analysis of variance, logistic or Poisson regression.
