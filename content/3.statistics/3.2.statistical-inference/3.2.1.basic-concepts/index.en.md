---
title: Basic Concepts of Statistics
description: What statistics is and how it differs from probability; population, sample and simple random sample; statistical models, parameters and the types of statistical inference; statistics such as sample moments and order statistics; the empirical distribution function and the Glivenko–Cantelli theorem.
---

Probability theory ([3.1](/3.1)) starts from a completely specified model and computes the chances of events. Statistics runs the other way: it starts from observed data and asks what can be said about the model that produced them. This chapter fixes the vocabulary of that reversal. We first describe what statistics is and what kinds of questions statistical inference answers, then formalize the basic objects: the population and the sample, the simple random sample and its joint distribution, the statistical model as a family of distributions indexed by a parameter, and the statistic, a function of the sample that is computable from the data. The chapter closes with the most commonly used statistics (sample moments, order statistics) and with the empirical distribution function, whose uniform convergence to the true distribution function (the Glivenko–Cantelli theorem) explains why a large sample can reveal the whole population. The distributions of these statistics are studied in [3.2.2](/3.2.2); point estimation, interval estimation and hypothesis testing occupy the remaining chapters.

## 1.1. Statistics and Statistical Inference

### 1.1.1. Random Phenomena and Statistics

Some phenomena in nature are deterministic: a freely falling body covers the distance $s=gt^2/2$, and the area of a circle is $A=\pi r^2$. Others are random: two plots of wheat of the same area under the same conditions give different yields, a chemical process run at the same temperature, pressure and formula gives different outputs, and a marksman scores differently from shot to shot. Statistics is the science of random phenomena. It is the discipline concerned with the collection, organization, display, analysis, interpretation and presentation of data, and more broadly with drawing inferences from observed data and making decisions in the face of uncertainty.

| Stage | Main branches |
|---|---|
| Collecting data efficiently | survey sampling, design of experiments |
| Analyzing data | descriptive statistics and statistical graphics, statistical inference |
| Interpreting and presenting data | data visualization, reporting |

Collecting data efficiently is itself a statistical problem. A complete survey (a census) is often too expensive, so one takes a sampling survey: to study the incomes of 10000 farmers in a region where 70% live in rich plain areas and 30% in poor mountain areas, a sample of 100 farmers should respect these proportions rather than be drawn blindly. Similarly, if the yield of a chemical product depends on temperature, pressure and formula, each at four levels, a full comparison needs $4^3=64$ experiments; the design of experiments finds the best conditions with far fewer runs.

Using data efficiently means extracting the information in the data and drawing conclusions about the problem under study, which is statistical inference. To do so we build a statistical model for the data, propose inference methods, and compare the methods by some criterion. The choice of method depends on the problem.

**Example 1.1.1** A village of 10000 farmers is considered free of poverty if the average annual income exceeds 10000 yuan. A survey of 100 farmers finds 90 with an annual income of 5000 yuan and 10 with 100000 yuan. In units of 10000 yuan, the sample mean is

$$
\bar x=\frac{90\times0.5+10\times10}{100}=1.45,
$$
while the sample median, the average of the 50th and 51st ordered values, is $0.5$. The mean says the village is out of poverty; the median says the typical farmer is not. Which summary answers the question depends on what "free of poverty" is meant to capture.

### 1.1.2. Induction, and Probability versus Statistics

Deductive inference reasons from premises to a conclusion that is logically certain: one proves that the base angles of an isosceles triangle are equal. Statistical inference is inductive: it draws conclusions about a population from a sample of individuals, as when the link between smoking and disease is inferred from patients. One could also draw many isosceles triangles, measure their angles and conclude that the base angles are equal; such a conclusion may be wrong because the data are random. What statistics adds is that the uncertainty of an inductive conclusion can be quantified by probability. A **confidence interval** together with the probability that it covers the true parameter is the typical example.

The contrast between probability and statistics is clearest in a single experiment.

| | Probability | Statistics |
|---|---|---|
| 1 | We have a fair coin. | We have a coin. |
| 2 | Flip it ten times. | Flip it ten times. |
| 3 | What is $\mathbb{P}(\text{all ten are heads})$? | All ten are heads. Is the coin fair? |

The probabilist computes, before the experiment and under an assumed model, that a fair coin gives ten heads with probability $(0.5)^{10}=1/1024\approx0.00098$; probability looks forward, much like mathematics. The statistician, after the experiment, concludes that the coin is not fair, because ten heads in a row would be very unlikely if it were; statistics looks backward, much like physics, inferring the model from what was observed.

### 1.1.3. A Brief History

Mathematical statistics took shape in the twentieth century. Its starting points are usually taken to be K. Pearson's 1900 paper introducing the $\chi^2$ criterion of fit and R. A. Fisher's 1922 paper "On the Mathematical Foundations of Theoretical Statistics". Up to the end of the Second World War the field was built by Fisher and K. Pearson (the British school), W. S. Gosset ("Student"), J. Neyman, E. S. Pearson (K. Pearson's son), A. Wald, P. L. Hsu and others; H. Cramér's *Mathematical Methods of Statistics* (1946) marks its maturity. After the war new branches appeared, such as statistical decision theory and Bayesian statistics, and the development of computers made methods such as Markov chain Monte Carlo possible.

In the last decades statistics has been transformed by new types of data (text, images, sound, video, networks), by enormous amounts of data, and by computations that were once unthinkable. The emphasis of the theory has accordingly shifted away from optimality results for small samples toward asymptotic methods with many observations and few assumptions (high-dimensional, nonparametric and semiparametric models), toward models for temporal, spatial and other complex data, and toward inference built on simulation, such as the bootstrap and Markov chain Monte Carlo.

### 1.1.4. Typical Problems of Statistical Inference

The following problems recur throughout the course.

- *Battery life.* Can a certain phone model play video for up to 15 hours? A census of all phones sold is too expensive and unnecessary for the precision required, so we test a sample, say of 100 phones. How should the video time be estimated (by the mean or the median)? How are the estimates evaluated and compared? How do we give an interval estimate? If the estimate is 15.1 hours, may we claim 15 hours? What if it is 14.8 or 10 hours? Statistical inference tells us how small the estimate must be to reject the claim, and how large the probability of a wrong conclusion is.
- *Acceptance sampling.* A store buys from a factory only if the long-run scrap rate $p$ is below $0.01$. In a sample of 100 products, 3 are scrap. Should the store buy?
- *Unemployment.* An agency samples $n=2000$ people from a city's labor force and finds 119 unemployed. Is the unemployment rate acceptable, for instance below $6.25\%$?
- *House prices.* The Ames housing data record 2930 residential sales in Ames, Iowa, from 2006 to 2010, with 82 variables (23 nominal, 23 ordinal, 14 discrete, 20 continuous and 2 identifiers). What drives the price of a house? How much does each additional square foot add? Does the siding material or the neighborhood matter? How well can the price be predicted?
- *Smoking and lung cancer.* Among 100 people classified as follows, is lung cancer associated with smoking?

| | Lung cancer | No lung cancer | Total |
|---|---|---|---|
| Smoking | 39 | 15 | 54 |
| Non-smoking | 21 | 25 | 46 |
| Total | 60 | 40 | 100 |

The course covers the basic concepts of statistical inference (this chapter and [3.2.2](/3.2.2)), point estimation ([3.2.3](/3.2.3)), confidence intervals and confidence regions ([3.2.4](/3.2.4)), parametric and nonparametric **hypothesis testing** ([3.2.5](/3.2.5), [3.2.6](/3.2.6)) and an introduction to Bayesian inference ([3.2.7](/3.2.7)).

## 1.2. Population and Sample

### 1.2.1. Population, Sample and Sample Space

**Definition 1.2.1 (Population)** The **population** is the collection of all objects under study; each member of it is an **individual**. A **sample** is a part of the population drawn for observation, and the number $n$ of individuals in it is the **sample size**.

**Example 1.2.1** Among 10000 products some are good and some are scrap, and we want the scrap rate. We select 100 products at random and test them. The population is the 10000 products, each product is an individual, the 100 tested products form the sample, and the sample size is 100. Let $X=1$ if a product is scrap and $X=0$ if it is good; then the statistical model is $X\sim\mathrm{Ber}(p)$, and if the population contains 100 scraps, $p=0.01$.

**Example 1.2.2** For the video time of a phone model, the population is all phones of that model sold, each phone is an individual, and a sample is, say, 100 phones selected from the population. Let $X$ be the video time of a phone; a statistical model is an assumption on the distribution of $X$, for instance $X\sim\mathcal{N}(a,\sigma^2)$.

What we care about in a population is not the individuals themselves but the distribution of the quantity measured on them. A population is therefore identified with a random variable $X$, or with its distribution function $F$ or density $f$, which is unknown or not fully specified. Sampling draws $n$ observations from it, and inference goes back from the sample to the population. When $X_1,\dots,X_n$ are drawn independently from the population $F$ (or $f$, or $X$), we write

$$
X_1,\dots,X_n\overset{\text{iid}}{\sim}F,
$$
where iid stands for independent and identically distributed.

A sample $\boldsymbol{X}=(X_1,\dots,X_n)$ has two faces. Before sampling, each $X_i$ is random (unknown) and has the same distribution as $X$: if the sampling were repeated, the values would change. After sampling, we have the observed values $\boldsymbol{x}=(x_1,\dots,x_n)$, which are known real numbers, for instance the simulated video times $14.5, 14.9, 13.1, 14.2, 13.1,\dots$. Capital letters denote the random sample, lower-case letters its observed value.

**Definition 1.2.2 (Sample Space)** The **sample space** $\mathcal{X}$ is the set of all values that a sample $\boldsymbol{X}=(X_1,\dots,X_n)$ can take.

In Example 1.2.1, $\mathcal{X}=\{(x_1,\dots,x_{100})\colon x_i=0\text{ or }1,\ i=1,\dots,100\}$; in Example 1.2.2, $\mathcal{X}=\{(x_1,\dots,x_{100})\colon x_i\in(0,\infty),\ i=1,\dots,100\}$. This is the sample space of the data, not the sample space $\Omega$ of an underlying random experiment in probability theory.

### 1.2.2. Simple Random Samples

Sampling is the method of taking a sample from the population. Its purpose is to infer unknown parameters of the population, such as the scrap rate, so the sample must carry useful information about the population. Simple random sampling has three features.

- *Representative*: every individual in the population has the same probability of being selected, so each sample point has the same distribution as the population.
- *Independent*: the value of each sample point is unaffected by the values of the others, so $X_1,\dots,X_n$ are independent random variables.
- *Implementation*: number the individuals and draw numbers by lot, from a random number table, or by computer simulation.

**Definition 1.2.3 (Simple Random Sample)** Let $F$ be a population and $X_1,\dots,X_n$ a sample of size $n$ from $F$. If $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$, then $X_1,\dots,X_n$ is called a **simple random sample** (or a **random sample** for short) from $F$.

The joint distribution of a random sample, the *sample distribution*, factors into the population distribution:

$$
F(x_1,\dots,x_n)=\prod_{i=1}^nF(x_i),\qquad f(x_1,\dots,x_n)=\prod_{i=1}^nf(x_i)
$$
(the second when a density exists). The sample may be multidimensional: if the population is a random vector $(X,Y)$, such as height and weight, and $(X_1,Y_1),\dots,(X_n,Y_n)$ is a random sample, then the joint distribution function and density are $\prod_{i=1}^nF(x_i,y_i)$ and $\prod_{i=1}^nf(x_i,y_i)$. From now on "sample" means a random sample unless stated otherwise.

**Example 1.2.3 (Sampling with Replacement)** Of $N$ products, $M$ are scrap; $N$ is known and $M$ is not. To estimate $M$, or the scrap rate $p=M/N$, we draw a sample of size $n$ with replacement. Let $X_i=1$ if the $i$-th draw is scrap and $X_i=0$ otherwise. Each product is drawn with probability $1/N$ at every draw, so $\mathbb{P}(X_i=1)=M/N$, $\mathbb{P}(X_i=0)=(N-M)/N$, and the draws are independent: $X_1,\dots,X_n$ is a simple random sample from $\mathrm{Ber}(M/N)$. For $x_i\in\{0,1\}$ with $\sum_{i=1}^nx_i=a$,

$$
\mathbb{P}(X_1=x_1,\dots,X_n=x_n)=\prod_{i=1}^n\mathbb{P}(X_i=x_i)=\left(\frac MN\right)^a\left(\frac{N-M}N\right)^{n-a},
$$
and the probability is $0$ for all other $(x_1,\dots,x_n)$.

**Example 1.2.4 (Sampling without Replacement)** In the setting of Example 1.2.3, draw without replacement. Write $A_i=\{X_i=x_i\}$; by the multiplication formula $\mathbb{P}(A_1\cdots A_n)=\mathbb{P}(A_1)\mathbb{P}(A_2\mid A_1)\cdots\mathbb{P}(A_n\mid A_1\cdots A_{n-1})$. For $n=3$ and $(x_1,x_2,x_3)=(1,0,1)$,

$$
\mathbb{P}(X_1=1,X_2=0,X_3=1)=\frac MN\cdot\frac{N-M}{N-1}\cdot\frac{M-1}{N-2}=\frac MN\cdot\frac{M-1}{N-1}\cdot\frac{N-M}{N-2}.
$$

The value depends only on how many 1's appear, not on where. In general, for $x_i\in\{0,1\}$ with $\sum_{i=1}^nx_i=a$,

$$
\mathbb{P}(X_1=x_1,\dots,X_n=x_n)=\frac MN\cdot\frac{M-1}{N-1}\cdots\frac{M-a+1}{N-a+1}\cdot\frac{N-M}{N-a}\cdots\frac{N-M-n+a+1}{N-n+1},
$$
and $0$ otherwise. By symmetry each $X_i$ still has the distribution $\mathrm{Ber}(M/N)$, but the $X_i$ are dependent, so this is not a simple random sample. When $n/N$ is small, each factor is close to $M/N$ or $(N-M)/N$ and the difference between sampling with and without replacement is negligible.

**Example 1.2.5** To determine the weight $a$ of an object we weigh it $n$ times on a balance, with results $X_1,\dots,X_n$. A joint distribution requires assumptions:

- the weighings are independent, so $X_1,\dots,X_n$ are independent;
- every weighing is done under the same conditions (the same balance, the same person, the same temperature and humidity), so the $X_i$ are identically distributed;
- the error is the sum of many small independent random effects, so by the **central limit theorem** it is approximately normally distributed;
- there is no systematic error, so $X_1\sim\mathcal{N}(a,\sigma^2)$.

Then the joint density is

$$
f(x_1,\dots,x_n)=(\sqrt{2\pi}\,\sigma)^{-n}\exp\left\{-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-a)^2\right\}.
$$

**Example 1.2.6** A random sample of $n$ people gives heights and weights $(X_1,Y_1),\dots,(X_n,Y_n)$, and we assume that height and weight jointly follow the bivariate normal distribution $\mathcal{N}(a,b;\sigma_1^2,\sigma_2^2,\rho)$. With $\theta=(a,b,\sigma_1^2,\sigma_2^2,\rho)$ the joint density is

$$
f(x_1,y_1,\dots,x_n,y_n;\theta)=\left(\frac1{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\right)^n\prod_{i=1}^n\exp\left\{-\frac1{2(1-\rho^2)}\left[\frac{(x_i-a)^2}{\sigma_1^2}-\frac{2\rho(x_i-a)(y_i-b)}{\sigma_1\sigma_2}+\frac{(y_i-b)^2}{\sigma_2^2}\right]\right\}.
$$

## 1.3. Statistical Models and Statistical Inference

### 1.3.1. Statistical Models and Parameters

**Definition 1.3.1 (Statistical Model)** The **statistical model** (probability model, mathematical model) of a practical problem is the sample distribution, that is, the joint distribution of the sample, specified up to the unknown quantities.

A model is named after its distribution: the normal model, the binomial model. It is determined by the sampling method together with assumptions on the population, as in Example 1.2.5. In G. Box's words, "all models are wrong, but some are useful". The same model serves many problems: the normal model of Example 1.2.5 can be used to estimate the weight of the object or the precision of the balance, by a point or by an interval.

Often we are interested not in the population itself but in a few numbers describing it, such as the mean income, or the mean and standard deviation of exam scores. Such quantities are called *population parameters* (or simply parameters) and are usually unknown: the scrap rate $p$, the mean $a$ and variance $\sigma^2$ of $\mathcal{N}(a,\sigma^2)$, the vector $\theta=(a,b,\sigma_1^2,\sigma_2^2,\rho)$ of a bivariate normal distribution. Parameters are customarily written with Greek letters such as $\mu,\sigma,\theta,\lambda$.

**Definition 1.3.2 (Parameter Space)** The **parameter space** $\Theta$ is the set of values the parameter can take. Each $\theta\in\Theta$ determines a distribution, and the set

$$
\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}
$$
is called the **distribution family** of the model.

In Example 1.2.5, $\Theta=\{(a,\sigma)\colon a>0,\ \sigma>0\}$; in Example 1.2.6, $\Theta=\{(a,b,\sigma_1,\sigma_2,\rho)\colon a>0,\ b>0,\ \sigma_1>0,\ \sigma_2>0,\ |\rho|<1\}$. The smaller the family, the more accurate and reliable the inference: if the balance is known to have $\sigma=1$, the mean $a$ is easier and more accurately estimated than when $\sigma$ is unknown. The price is a greater risk that the model is wrong.

### 1.3.2. Types of Statistical Inference

**Definition 1.3.3 (Statistical Inference)** **Statistical inference** is inference about the population based on a sample: the information in the observed data is used to draw conclusions about the unknown distribution. In **parametric inference** the form of the distribution is known and only finitely many parameters are unknown, as when the data are assumed to come from $\mathcal{N}(\mu,\sigma^2)$ with unknown $\mu$ and $\sigma^2$. In **nonparametric inference** the form of the distribution is not specified, and the inference concerns functionals of the population distribution such as its mean, its variance or the distribution function itself.

The procedures of inference fall into two kinds.

- Estimation of population parameters. In point estimation a single statistic is used as the estimate of a parameter. In interval estimation the variability of the statistic over repeated sampling is quantified, and an interval such as a **confidence interval** is reported.
- **Hypothesis testing**: the sample is compared with a hypothesized value or property of the population parameter, and the hypothesis is accepted or rejected.

Because the sample is random, no conclusion of statistical inference is correct with certainty, and a measure of how reliable it is must be part of the answer; in Example 1.2.5, for instance, $\mathbb{P}(|\bar X-a|>c)$ measures how far the average of the weighings may be from the true weight. Statistical inference therefore has three tasks: to propose methods, to compute their measure of reliability, and to find the best method under given assumptions and a given optimality criterion, or to prove that a given method is optimal.

## 1.4. Statistics

### 1.4.1. Definition

The information about population parameters in a random sample $\boldsymbol{X}=(X_1,\dots,X_n)$ is extracted by computing a function of the sample.

**Definition 1.4.1 (Statistic)** A function $T(X_1,\dots,X_n)$ of the sample that does not depend on any unknown quantity is called a **statistic**. A statistic may be vector-valued.

**Example 1.4.1** For a sample from a population with unknown mean $\mu$,

$$
\frac1{n-1}\sum_{i=1}^n(X_i-\mu)^2
$$
is not a statistic, because it cannot be computed from the data; it becomes a statistic when $\mu$ is known. Which statistic to use depends on the problem.

Like the sample, a statistic has two faces. Before sampling it is a random variable (or random vector) $T(\boldsymbol{X})$; after sampling it is the real number (or vector) $T(\boldsymbol{x})$ computed from the observed values, for instance the observed sample mean $\bar x=\frac1n\sum_{i=1}^nx_i$ and sample variance $s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2$.

### 1.4.2. Sample Mean, Sample Variance and Sample Moments

**Definition 1.4.2 (Sample Mean and Sample Variance)** The **sample mean** and the **sample variance** are

$$
\bar X=\frac1n\sum_{i=1}^nX_i,\qquad S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2,
$$
and $S=\sqrt{S^2}$ is the **sample standard deviation**.

The sample mean carries information about the population mean and the sample variance about the population variance. The divisor $n-1$ makes $S^2$ unbiased for the variance, as shown in [3.2.3](/3.2.3).

**Proposition 1.4.1** Let $X_1,\dots,X_n$ be a sample.

1. $\sum_{i=1}^n(X_i-\bar X)=0$.
2. If $Y_i=aX_i+b$ ($i=1,\dots,n$) for constants $a,b$, then $\bar Y=a\bar X+b$ and $S_Y^2=a^2S_X^2$.
3. For every constant $c$,

   $$
   \sum_{i=1}^n(X_i-c)^2\ge\sum_{i=1}^n(X_i-\bar X)^2,
   $$
   with equality if and only if $c=\bar X$.

**Proof** Item 1 is $\sum X_i-n\bar X=0$. For item 2, $\bar Y=\frac1n\sum(aX_i+b)=a\bar X+b$ and $Y_i-\bar Y=a(X_i-\bar X)$. For item 3, expand using item 1:

$$
\sum_{i=1}^n(X_i-c)^2=\sum_{i=1}^n(X_i-\bar X)^2+2(\bar X-c)\sum_{i=1}^n(X_i-\bar X)+n(\bar X-c)^2=\sum_{i=1}^n(X_i-\bar X)^2+n(\bar X-c)^2. \quad\square
$$

Item 3 says that $\bar X$ is the least-squares center of the data. Item 1 explains the divisor $n-1$: the $n$ deviations $X_i-\bar X$ satisfy one linear constraint, so only $n-1$ of them are free.

**Definition 1.4.3 (Sample Moments)** The $k$-th **sample origin moment** and the $k$-th **sample central moment** are

$$
a_{n,k}=\frac1n\sum_{i=1}^nX_i^k\quad(k=1,2,\dots),\qquad m_{n,k}=\frac1n\sum_{i=1}^n(X_i-\bar X)^k\quad(k=2,3,\dots).
$$

Thus $a_{n,1}=\bar X$ and $m_{n,2}=\frac{n-1}nS^2$. For a two-dimensional sample $(X_1,Y_1),\dots,(X_n,Y_n)$ we use the marginal quantities $\bar X$, $S_X^2$, $\bar Y$, $S_Y^2$ together with the *sample covariance*

$$
S_{XY}=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)(Y_i-\bar Y),
$$
and the sample correlation coefficient $r=S_{XY}/(S_XS_Y)$.

### 1.4.3. Order Statistics

Some problems call for statistics other than moments. The flight time of a certain route from Beijing to Shanghai is at least 80 minutes; suppose it is uniformly distributed between 80 and an unknown $\theta$, so that $X\sim\mathrm{U}(80,\theta)$. Given the times $X_1,\dots,X_n$ of $n$ days, how should $\theta$ be estimated? Since $\mathbb{E}[X]=(80+\theta)/2$, one candidate is $2\bar X-80$; another is the largest observation $X_{(n)}=\max(X_1,\dots,X_n)$. Which is better is a question for [3.2.3](/3.2.3). Similarly, estimating the longest waiting time at a bank leads naturally to $X_{(n)}$.

**Definition 1.4.4 (Order Statistic)** Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$. Arranging them in ascending order, $X_{(1)}\le X_{(2)}\le\cdots\le X_{(n)}$, we call $(X_{(1)},X_{(2)},\dots,X_{(n)})$, and any part of it such as $X_{(i)}$ or $(X_{(i)},X_{(j)})$, the **order statistics** of the sample; $X_{(j)}$ is the $j$-th order statistic.

For example, the observations $(x_1,\dots,x_6)=(4,6,0,3,7,2)$ give $x_{(1)}=0$, $x_{(2)}=2,\dots,x_{(6)}=7$. Important order statistics are the extremes $X_{(1)}$ and $X_{(n)}$, the *sample median*

$$
m_{1/2}=\begin{cases}X_{((n+1)/2)}, & n\text{ odd},\\[1mm] \dfrac12\left[X_{(n/2)}+X_{(n/2+1)}\right], & n\text{ even},\end{cases}
$$
and the *sample range* $R=X_{(n)}-X_{(1)}$. Order statistics are not independent even though the $X_i$ are; their joint and marginal distributions are derived in [3.1.7](/3.1.7).

### 1.4.4. Statistics Describing Shape

**Definition 1.4.5 (Coefficient of Variation, Skewness and Kurtosis)** The **sample coefficient of variation**, the **sample skewness** and the **sample kurtosis** are

$$
\hat\nu=\frac S{\bar X},\qquad\hat\beta_1=\frac{m_{n,3}}{m_{n,2}^{3/2}}=\frac{\sqrt n\sum_{i=1}^n(X_i-\bar X)^3}{\left(\sum_{i=1}^n(X_i-\bar X)^2\right)^{3/2}},\qquad\hat\beta_2=\frac{m_{n,4}}{m_{n,2}^2}-3=\frac{n\sum_{i=1}^n(X_i-\bar X)^4}{\left(\sum_{i=1}^n(X_i-\bar X)^2\right)^2}-3.
$$

The coefficient of variation measures dispersion relative to the level and does not depend on the unit of measurement. Skewness measures asymmetry and kurtosis measures the weight of the tails. The population counterparts $\mathbb{E}[(X-\mu)^3]/\sigma^3$ and $\mathbb{E}[(X-\mu)^4]/\sigma^4-3$ are both $0$ for a normal population (the normal kurtosis is $3$, and $\hat\beta_2$ is the excess kurtosis), so values of $\hat\beta_1$ and $\hat\beta_2$ far from $0$ indicate departure from normality.

## 1.5. The Empirical Distribution Function

### 1.5.1. Definition

The statistics so far summarize the sample by a few numbers. The empirical distribution function keeps all the information in the sample except the order of the observations, and estimates the whole population distribution.

**Definition 1.5.1 (Empirical Distribution Function)** Let $X_1,\dots,X_n$ be a sample from a population with distribution function $F$. For each $x\in\mathbb{R}$,

$$
F_n(x)=\frac1n\#\{i\colon X_i\le x\}=\frac1n\sum_{i=1}^n\boldsymbol{1}_{(-\infty,x]}(X_i)
$$
is called the **empirical distribution function** of the sample. In terms of the order statistics,

$$
F_n(x)=\begin{cases}0, & x<X_{(1)},\\[1mm] \dfrac kn, & X_{(k)}\le x<X_{(k+1)},\quad k=1,2,\dots,n-1,\\[1mm] 1, & X_{(n)}\le x.\end{cases}
$$

Here $\boldsymbol{1}_A(x)$ is $1$ for $x\in A$ and $0$ otherwise. Every realization of $F_n$ is a step function with a jump of $1/n$ at each observation (a jump of $k/n$ at a value observed $k$ times), that is, the distribution function of the discrete distribution putting mass $1/n$ on each data point.

![Empirical distribution functions of standard normal samples of size 10 and 100 against the true distribution function](./plots/empirical-distribution.py)

### 1.5.2. Properties

For fixed $x$, $F_n(x)$ is a discrete random variable, an estimator of $F(x)$. Let $Y_i=\boldsymbol{1}_{(-\infty,x]}(X_i)$; then $\mathbb{P}(Y_i=1)=\mathbb{P}(X_i\le x)=F(x)$ and $\mathbb{P}(Y_i=0)=1-F(x)$, so $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathrm{Ber}(F(x))$ and $nF_n(x)=\sum_{i=1}^nY_i$.

**Theorem 1.5.1** Let $F_n$ be the empirical distribution function of a sample of size $n$ from $F$, and fix $x\in\mathbb{R}$.

1. $nF_n(x)\sim\mathrm{Bin}(n,F(x))$, that is,

   $$
   \mathbb{P}\left(F_n(x)=\frac kn\right)=\binom nk[F(x)]^k[1-F(x)]^{n-k},\qquad k=0,1,\dots,n;
   $$
   in particular $\mathbb{E}[F_n(x)]=F(x)$ and $\operatorname{Var}(F_n(x))=F(x)[1-F(x)]/n$.
2. $F_n(x)\xrightarrow{p}F(x)$ and $F_n(x)\xrightarrow{\text{a.s.}}F(x)$ as $n\to\infty$.
3. If $0<F(x)<1$, then as $n\to\infty$

   $$
   \frac{\sqrt n\,(F_n(x)-F(x))}{\sqrt{F(x)(1-F(x))}}\xrightarrow{d}\mathcal{N}(0,1).
   $$

**Proof** Item 1 holds because $nF_n(x)$ is a sum of $n$ independent $\mathrm{Ber}(F(x))$ variables. Items 2 and 3 are the **law of large numbers** (in its weak and strong forms) and the **central limit theorem** applied to the iid variables $Y_i$, which have mean $F(x)$ and variance $F(x)(1-F(x))$. $\square$

Theorem 1.5.1 concerns one point $x$ at a time. The following theorem gives **almost sure convergence** uniformly in $x$.

**Theorem 1.5.2 (Glivenko–Cantelli Theorem)** Let $D_n=\sup_{-\infty<x<\infty}|F_n(x)-F(x)|$. Then

$$
\mathbb{P}\left(\lim_{n\to\infty}D_n=0\right)=1.
$$

**Proof** We sketch the argument for continuous $F$. Given $k\in\mathbb{N}_+$, choose points $-\infty=x_0<x_1<\dots<x_k=\infty$ with $F(x_j)=j/k$. For $x\in[x_{j-1},x_j]$, monotonicity of $F_n$ and $F$ gives

$$
F_n(x)-F(x)\le F_n(x_j)-F(x_{j-1})=F_n(x_j)-F(x_j)+\frac1k,\qquad F_n(x)-F(x)\ge F_n(x_{j-1})-F(x_{j-1})-\frac1k,
$$
so $D_n\le\max_{0\le j\le k}|F_n(x_j)-F(x_j)|+1/k$. By Theorem 1.5.1 the maximum over finitely many points tends to $0$ almost surely, so $\limsup_nD_n\le1/k$ almost surely for every $k$, hence $D_n\to0$ almost surely. For general $F$ the same argument works with the left limits $F(x_j-)$ and $F_n(x_j-)$ added at the jump points. $\square$

The Glivenko–Cantelli theorem is sometimes called the fundamental theorem of statistics: with probability one, the empirical distribution of a large enough sample is uniformly close to the population distribution, so the sample eventually determines the population. This justifies using sample quantities as estimates of population quantities. The rate is $1/\sqrt n$: $\sqrt nD_n$ has a nondegenerate limiting distribution (Kolmogorov's theorem), which is the basis of the Kolmogorov–Smirnov test in [3.2.6](/3.2.6).

![Kolmogorov distance between the empirical and the true distribution function for twenty growing normal samples; the distance decreases like the reference line 1 over root n](./plots/glivenko-cantelli.py)

## Summary

| Concept | Meaning |
|---|---|
| Population, sample | the distribution $F$ under study; observations $X_1,\dots,X_n$ drawn from it |
| Simple random sample | $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$, joint distribution $\prod F(x_i)$ |
| Statistical model | the sample distribution; a family $\{f(x;\theta)\colon\theta\in\Theta\}$ |
| Statistical inference | parametric or nonparametric; estimation (point, interval) and testing |
| Statistic | a function of the sample free of unknown quantities; random before sampling, a number after |
| Common statistics | $\bar X$, $S^2$, sample moments $a_{n,k}$, $m_{n,k}$, order statistics, median, range, skewness, kurtosis |
| Empirical distribution function | $F_n(x)=\frac1n\sum\boldsymbol{1}_{(-\infty,x]}(X_i)$; $nF_n(x)\sim\mathrm{Bin}(n,F(x))$; $\sup_x\lvert F_n-F\rvert\to0$ a.s. |
