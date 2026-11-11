---
title: Neural Decoding and Population Codes
description: "Decoding as inference from a noisy population response: signal detection theory, ROC curves and the comparison of neurometric and psychometric functions in MT (Britten et al.); maximum-likelihood, maximum a posteriori and population-vector decoders for Poisson populations; Fisher information, the Cramér–Rao bound and the optimal width of tuning curves in D dimensions; noise correlations, saturation of information with population size and information-limiting correlations; reconstruction of a stimulus from spike trains with optimal linear filters."
---

Chapter [7.16.16](/7.16.16) asked how a stimulus is encoded in spike trains. This chapter reverses the question: given the spikes that were observed, what can be said about the stimulus? Decoding matters for two reasons. It is the problem the brain itself must solve, since downstream circuits see only spikes and must decide what to do about the stimulus that caused them. And it is a tool: an ideal decoder tells how much information a population carries, whether a code is efficient, and which of its features (tuning width, noise correlations, population size) limit the precision of perception. We treat decoding as statistical inference, using the maximum-likelihood and Bayesian methods of [3.2](/3.2) and [3.7](/3.7), and ask three quantitative questions: how well can two stimuli be discriminated from one neuron, how well can a stimulus be estimated from a population, and how do the variability and correlations of the neurons limit the answer. The chapter is the basis of [7.16.27](/7.16.27), where priors enter the decoder, and of the population analyses of [7.16.28](/7.16.28) and [7.16.32](/7.16.32).

Throughout the chapter the stimulus is $s$ (a vector $\boldsymbol{s}$ if it has several components) and the response of a population of $N$ neurons is the vector $\boldsymbol{r} = (r_1, \dots, r_N)$ of spike counts in a window of length $T$. The tuning curve $f_i(s) = \mathbb{E}[r_i \mid s]$ is the mean count of neuron $i$ (Definition 16.3.1; counts and rates differ by the factor $T$, which we absorb into $f_i$, so that $T = 1\,\mathrm{s}$ makes the numbers equal to rates in $\mathrm{Hz}$). The conditional distribution $\mathbb{P}(\boldsymbol{r} \mid s)$ is the encoding model, and $p(s \mid \boldsymbol{r})$ the posterior of the decoder. The Fisher information is written $I_{\mathrm{F}}(s)$ to avoid confusion with current.

## 26.1. Encoding and Decoding

A tuning curve alone does not decode, for two reasons. First, the same count can arise from different stimuli: a neuron with a bell-shaped tuning curve responds equally to stimuli on the two flanks of its peak, so one neuron cannot say which side the stimulus is on. Second, the count is a random variable. Repeated presentations of the same stimulus yield different counts, with variance close to the mean ([7.16.16](/7.16.16#sec-16.4.3)), so the count of one trial is compatible with a range of stimuli.

Both problems are solved by inference over the population. The encoding model $\mathbb{P}(\boldsymbol{r} \mid s)$ gives the **likelihood function** of the stimulus $s$ for the observed response $\boldsymbol{r}$, and together with a **prior distribution** $p(s)$ it gives the **posterior distribution** by **Bayes' theorem**,

$$
p(s \mid \boldsymbol{r}) = \frac{\mathbb{P}(\boldsymbol{r} \mid s)\,p(s)}{\mathbb{P}(\boldsymbol{r})}. \tag{26.1}
$$
Every decoder is a rule that maps $\boldsymbol{r}$ to an estimate $\hat s$ or to a posterior. Which estimate is best depends on the cost of an error: the posterior mean minimizes the expected squared error, the posterior median the expected absolute error, and the mode of the posterior, the **maximum a posteriori estimate**, minimizes the probability of an error when $s$ takes discrete values ([3.2.7](/3.2.7)). With a flat prior the mode is the estimate of **maximum likelihood estimation**. Whatever the choice, the posterior contains more than an estimate: its width says how reliable the estimate is, which is the quantity that Bayesian perception and cue combination use in [7.16.27](/7.16.27).

The prior can matter as much as the data. A diagnostic test with sensitivity $0.7$ and specificity $0.99$ is applied to a person from a population in which the prevalence of the disease is $0.1\,\%$.

**Example 26.1.1** Let $D$ denote the disease and $+$ a positive test. Then $\mathbb{P}(+ \mid D) = 0.7$, $\mathbb{P}(+ \mid \overline{D}) = 0.01$ and $\mathbb{P}(D) = 0.001$, and by Eq. (26.1)

$$
\mathbb{P}(D \mid +) = \frac{0.7\times0.001}{0.7\times0.001 + 0.01\times0.999} \approx 0.065.
$$
Although the test is highly specific, only $6.5\,\%$ of the positive results are true: the low prior outweighs a likelihood ratio of $70$. A decoder that ignored the prior, as a maximum-likelihood decoder does, would call every positive person ill.

:::

## 26.2. Discrimination and Signal Detection Theory

The simplest decoding problem is a choice between two stimuli, for example two directions of motion, $s_+$ and $s_-$, from the count $r$ of one neuron. Because both counts are random, the neuron makes errors, and the question is how often.

**Definition 26.2.1 (Signal Detection Theory)** **Signal detection theory** analyzes the discrimination of two alternatives from noisy observations. An observer reports "$+$" when the response $r$ exceeds a criterion $z$. The *hit rate* $\beta(z) = \mathbb{P}(r \ge z \mid +)$ (the power of the test) and the *false alarm rate* $\alpha(z) = \mathbb{P}(r \ge z \mid -)$ (its size) change with $z$; the curve of $\beta$ against $\alpha$ traced out as $z$ varies is the **ROC curve** (receiver operating characteristic curve).

By the **Neyman–Pearson lemma** ([3.2.5](/3.2.5#thm-5.4.1)), for a given false alarm rate the likelihood-ratio test has the highest hit rate; when the likelihood ratio increases with $r$, as for a neuron whose rate rises with the stimulus value, thresholding the count is that test. For a neuron an ROC curve is a complete description of how well its responses separate the two stimuli, independent of any criterion.

**Theorem 26.2.1 (Area under the ROC Curve)** The area under the ROC curve equals the probability that a random response to the preferred stimulus exceeds a random response to the other stimulus (ties counted one half): $\mathrm{AUC} = \mathbb{P}(r_+ > r_-) + \tfrac12\mathbb{P}(r_+ = r_-)$, with $r_+ \sim \mathbb{P}(\cdot \mid +)$ and $r_- \sim \mathbb{P}(\cdot \mid -)$ independent. It is therefore the proportion correct of a two-alternative forced-choice observer who is shown both stimuli and picks the one that evoked the larger response.

**Proof** For continuous $r$ with densities $p_+, p_-$ the area is $\int \beta\,\mathrm{d}\alpha = \int \mathbb{P}(r_+ \ge z)\,p_-(z)\,\mathrm{d}z = \mathbb{P}(r_+ \ge r_-)$, because $\alpha'(z) = -p_-(z)$. For discrete counts the ROC curve is the polygon connecting the points and the trapezoids give the tie term. $\square$

For Gaussian responses with equal variances $\sigma^2$ and means $\mu_\pm$, define the sensitivity $d' = (\mu_+ - \mu_-)/\sigma$. The difference $r_+ - r_-$ is normal with mean $\sigma d'$ and variance $2\sigma^2$, so

$$
\mathrm{AUC} = \Phi\!\Bigl(\frac{d'}{\sqrt2}\Bigr), \tag{26.2}
$$
where $\Phi$ is the standard normal distribution function: $d' = 1$ gives $0.76$ and $d' = 2$ gives $0.92$.

### 26.2.1. Neurometric and Psychometric Functions

Signal detection theory lets neural and behavioral performance be compared on the same scale. In the experiments of Newsome and colleagues described in [7.16.18](/7.16.18#sec-18.8), a monkey reports the direction of a field of random dots in which a fraction $c$ of the dots, the motion coherence, move coherently. The probability of a correct report as a function of $c$ is the *psychometric function*, well described by a Weibull curve,

$$
p(c) = 1 - \tfrac12\exp\!\bigl[-(c/\alpha)^\beta\bigr], \tag{26.3}
$$
which rises from $1/2$ (chance) at $c = 0$ to $1$; the threshold $\alpha$ is the coherence at which $p = 1 - \mathrm{e}^{-1}/2 \approx 0.82$.

**Definition 26.2.2 (Neurometric Function)** The **neurometric function** of a neuron is the proportion correct of an ideal observer who discriminates the two directions from the neuron's responses alone, as a function of the stimulus strength $c$: the area under the ROC curve of the response distributions to the preferred and null directions at coherence $c$ (Theorem 26.2.1), usually fitted with Eq. (26.3).

Britten et al. (1992) recorded single neurons in area MT while the monkey performed the task, with the dots moving in the neuron's preferred or null direction. For each coherence they computed the ROC area, obtained a neurometric function for each of 216 neurons and compared its threshold with the animal's. The surprising result was that the two were nearly the same on average: the typical single neuron was about as sensitive as the monkey, and the most sensitive neurons were more sensitive. The figure reproduces the analysis with a model neuron whose mean count in a $2\,\mathrm{s}$ trial is $40 + 0.5c$ for the preferred and $40 - 0.25c$ for the null direction (with Fano factor $1.5$): at $12.8\,\%$ coherence the count distributions overlap substantially and the ROC area is about $0.81$, a neurometric threshold of $13\,\%$ close to the psychometric threshold of $10\,\%$.

![Neurometric versus psychometric function in a model MT neuron (Weibull psychometric function with α = 10 % and β = 1.3; the neuron has a mean count in 2 s of 40 + 0.5c for the preferred and 40 − 0.25c for the null direction, Fano factor 1.5, c = coherence in percent). A: distributions of the count at 12.8 % coherence over 5000 trials each, and a criterion z: counts above z are called "preferred". B: ROC curves for coherences of 3.2, 6.4, 12.8 and 25.6 %; the areas are given in the legend and grow with coherence. C: area under the ROC curve from 300 simulated trials per direction (points) with its Weibull fit (dashed, threshold 13 %) and the psychometric function (solid)](./plots/neurometric.py)

The result sets a puzzle. The monkey has thousands of MT neurons with similar tuning, and if their noise were independent, combining $N$ of them would improve $d'$ by a factor $\sqrt N$, giving a behavioral threshold far below that of a single neuron. The animal's actual threshold is that of one neuron. Either the information is lost downstream, or the noise of nearby neurons is correlated so that averaging does not help. We return to this in Section 26.5. A related measure is the *choice probability*: the AUC between the responses of a neuron to repetitions of the *same* stimulus sorted by the animal's choice. Values slightly above $0.5$ (about $0.55$ in MT) show that trial-to-trial fluctuations of a neuron are weakly but significantly related to the decision, which would be expected from correlated noise shared with the decision circuit ([7.16.47](/7.16.47)).

## 26.3. Decoding a Population

### 26.3.1. Bayesian Decoding of a Poisson Population

Suppose the neurons respond independently given the stimulus, with Poisson counts of mean $f_i(s)$ ([7.16.16](/7.16.16#sec-16.4.1)). The likelihood is a product,

$$
\mathbb{P}(\boldsymbol{r} \mid s) = \prod_{i=1}^N \frac{f_i(s)^{r_i}\mathrm{e}^{-f_i(s)}}{r_i!}.
$$

**Theorem 26.3.1 (Posterior of a Poisson Population)** For independent Poisson neurons, the log posterior is

$$
\ln p(s \mid \boldsymbol{r}) = \ln p(s) + \sum_{i=1}^N r_i\ln f_i(s) - \sum_{i=1}^N f_i(s) + \mathrm{const}, \tag{26.4}
$$
where the constant does not depend on $s$. If the tuning curves tile the stimulus space so that $\sum_i f_i(s)$ is independent of $s$ and the prior is flat, the maximum of the posterior is at the maximum of $\sum_i r_i\ln f_i(s)$.

**Proof** Take the logarithm of Eq. (26.1) with the product above. The factors $1/r_i!$ and $\mathbb{P}(\boldsymbol{r})$ do not depend on $s$. $\square$

Equation (26.4) is the basis of maximum a posteriori (MAP) decoding: the stimulus estimate is the **maximum a posteriori estimate** $\hat s_{\mathrm{MAP}} = \arg\max_s \ln p(s \mid \boldsymbol{r})$. Its structure is simple: each neuron votes for the stimuli where its tuning curve is high, weighted by how many spikes it fired. The estimate is a *template match* of the observed spike counts with the logarithms of the tuning curves, and a neuron that fired no spikes still contributes through the term $-f_i(s)$, which penalizes stimuli at which it should have fired. The prior shifts the estimate towards likely stimuli, and the weight of the prior relative to the likelihood falls as spikes accumulate.

For Gaussian tuning curves of common width $\sigma_f$ and amplitude $A$, $f_i(s) = A\exp[-(s - s_i)^2/2\sigma_f^2]$ with preferred values $s_i$ that are dense and evenly spaced, $\sum_i f_i(s)$ is constant and $\ln f_i(s) = \ln A - (s - s_i)^2/2\sigma_f^2$. Maximizing $-\sum_i r_i(s - s_i)^2$ gives, by setting the derivative to zero,

$$
\hat s_{\mathrm{ML}} = \frac{\sum_i r_i s_i}{\sum_i r_i}. \tag{26.5}
$$
The maximum-likelihood estimate is the center of mass of the population response: each neuron votes with its preferred stimulus, weighted by its count. Moreover, the posterior itself is Gaussian in $s$: Eq. (26.4) is a quadratic function of $s$ with curvature $\sum_i r_i/\sigma_f^2$, so the posterior standard deviation is $\sigma_f/\sqrt{\sum_i r_i}$. The width of the posterior therefore *shrinks with the total number of spikes*, a property that makes population activity a natural code for uncertainty (Section 27.5 of [7.16.27](/7.16.27#sec-27.5)).

### 26.3.2. The Population Vector

For a circular variable such as the direction of an arm movement, Georgopoulos and colleagues (1982, 1986) found that cells of motor cortex have broad, approximately cosine tuning, $f_i(\theta) = r_0 + A\cos(\theta - \theta_i)$, so that a single neuron says little about the direction. They showed that the direction of the movement is predicted by the **population vector**, the sum of the preferred-direction vectors $\boldsymbol{c}_i = (\cos\theta_i, \sin\theta_i)$ of the neurons weighted by their activity,

$$
\hat{\boldsymbol{v}} = \sum_{i=1}^N r_i\,\boldsymbol{c}_i, \qquad \hat\theta_{\mathrm{pv}} = \arg\hat{\boldsymbol{v}}. \tag{26.6}
$$
(The vector with $r_i$ replaced by the rate minus the baseline $r_0$ is used when the baseline is large.) The population vector is the circular version of Eq. (26.5), and the connection is exact for a von Mises tuning curve without baseline, $f_i(\theta) = A\exp\{\kappa[\cos(\theta - \theta_i) - 1]\}$: then $\ln f_i = \mathrm{const} + \kappa\cos(\theta - \theta_i)$ and

$$
\sum_i r_i\ln f_i(\theta) = \mathrm{const} + \kappa\,\operatorname{Re}\Bigl[\mathrm{e}^{-\mathrm{i}\theta}\sum_i r_i\mathrm{e}^{\mathrm{i}\theta_i}\Bigr],
$$
which is maximal at $\theta = \arg\sum_i r_i\mathrm{e}^{\mathrm{i}\theta_i}$, the population vector. For tuning curves with a baseline, or for non-uniform coverage and unequal tuning widths, the population vector is not optimal but remains a good, simple, linear readout that a downstream neuron could implement by weighting its inputs ([7.14.45](/7.14.45)).

A decoder that picks the stimulus of the most active neuron (winner-take-all) is the other simple alternative; it discards the information carried by the rest of the population, and for broad tuning curves is much worse. In area MT, Nichols and Newsome (2002) used microstimulation to ask which readout the brain performs: stimulating a cluster of neurons while the stimulus had a different direction shifted the monkey's choices as a vector average of the two directions at small separations, but selected one of the two (winner-take-all) at large separations.

The figure compares the decoders on a ring of $N$ Poisson neurons. The error of both decreases as $1/\sqrt N$; the maximum-likelihood decoder lies on the lower bound derived in the next section, and the population vector is slightly worse because the tuning curves here have a baseline.

![Decoding the direction of a stimulus on the circle from independent Poisson neurons with von Mises tuning (baseline 2, amplitude 20, κ = 2, preferred directions evenly spaced). A: tuning curves of 12 of the neurons (mean counts). B: root-mean-square error of the maximum-likelihood decoder (circles), the population vector (squares) and the Cramér–Rao bound (dashed, Eq. (26.8)), as a function of the number of neurons N, from 2000 random stimuli for each N. All decrease as 1/√N, and the maximum-likelihood decoder attains the bound](./plots/ml-vs-population-vector.py)

## 26.4. Fisher Information and the Optimal Tuning Curve

How precisely *can* a stimulus be estimated, whatever the decoder? The answer is the **Cramér–Rao lower bound** ([3.2.3](/3.2.3#thm-3.4.4)): any unbiased estimator $\hat s$ of $s$ has variance at least $1/I_{\mathrm{F}}(s)$, where

$$
I_{\mathrm{F}}(s) = \mathbb{E}\Bigl[\Bigl(\frac{\partial\ln\mathbb{P}(\boldsymbol{r} \mid s)}{\partial s}\Bigr)^2\,\Big|\,s\Bigr] \tag{26.7}
$$
is the **Fisher information**. The maximum-likelihood estimator attains the bound asymptotically for many neurons or long counting windows. For independent Poisson neurons the score is $\sum_i (r_i/f_i - 1)f_i'$, and its variance, using $\operatorname{Var}(r_i) = f_i$, is

$$
I_{\mathrm{F}}(s) = \sum_{i=1}^N\frac{f_i'(s)^2}{f_i(s)}, \qquad \operatorname{Var}(\hat s) \ge \frac{1}{I_{\mathrm{F}}(s)}. \tag{26.8}
$$
For Gaussian noise with a fixed covariance matrix $\Sigma$ the corresponding expression is $I_{\mathrm{F}} = \boldsymbol{f}'^{\mathsf T}\Sigma^{-1}\boldsymbol{f}'$ with $\boldsymbol{f}' = (f_1', \dots, f_N')^{\mathsf T}$. Information adds across independent neurons, and each contributes where its tuning curve is steepest relative to its noise; at the peak of its tuning curve it contributes nothing, because $f_i' = 0$. For discrimination, $I_{\mathrm{F}}$ has an operational meaning: two stimuli separated by a small $\Delta s$ are discriminated with sensitivity $d' \approx \Delta s\sqrt{I_{\mathrm{F}}}$, so that the discrimination threshold for $d' = 1$ is $I_{\mathrm{F}}^{-1/2}$.

### 26.4.1. Dense Gaussian Tuning

Take Gaussian tuning curves of width $\sigma$ and amplitude $A$, whose preferred values are uniformly distributed with density $\eta$ per unit stimulus. Replacing the sum in Eq. (26.8) by an integral over preferred values $c$, with $u = s - c$,

$$
I_{\mathrm{F}} = \eta\int A\frac{u^2}{\sigma^4}\mathrm{e}^{-u^2/2\sigma^2}\,\mathrm{d}u = \sqrt{2\pi}\,\frac{\eta A}{\sigma}.
$$
Narrower tuning curves carry more information in one dimension, because each active neuron is steeper, and the number of neurons that respond (those within about $\sigma$ of the stimulus) falls only in proportion to $\sigma$. The result changes qualitatively when the stimulus has $D$ dimensions, the tuning curves being Gaussian in all of them (Zhang and Sejnowski, 1999). The number of active neurons then scales as $\sigma^D$, since the neurons within a distance about $\sigma$ in $D$ dimensions fill a volume proportional to $\sigma^D$, while each contributes about $A/\sigma^2$, so that

$$
I_{\mathrm{F}} = (2\pi)^{D/2}\,\eta A\,\sigma^{D-2}. \tag{26.9}
$$
The information decreases with the width for $D = 1$, does not depend on it for $D = 2$, and *increases* with it for $D \ge 3$ (figure). Narrow tuning is optimal only for one-dimensional stimuli; neurons that encode many features at once, as most cortical neurons do ([7.16.16](/7.16.16#sec-16.3)), are better broadly tuned, at least as far as the stimulus precision is concerned. The result holds for a fixed density $\eta$ of neurons per unit stimulus volume and for Poisson noise; with a fixed total number of neurons and finite stimulus ranges, other constraints (coverage, the time to read out the code, the cost of spikes) enter ([7.16.20](/7.16.20)).

![Fisher information of a population of independent Poisson neurons with Gaussian tuning (amplitude 10) whose preferred values lie on a cubic lattice of spacing 0.25 in D dimensions. A: tuning curves of width σ = 0.5 and 1.5. B: Fisher information about one stimulus coordinate against the width σ for D = 1, 2 and 3: dots from the lattice sum, lines the continuum result of Eq. (26.9). The information decreases with width in one dimension, is independent of width in two and increases in three](./plots/fisher-vs-width.py)

## 26.5. Noise Correlations

The noise of cortical neurons is not independent: the trial-to-trial fluctuations of the counts of nearby neurons are positively correlated.

**Definition 26.5.1 (Noise Correlation)** The **noise correlation** of two neurons is the correlation coefficient $\rho_{ij} = \operatorname{Corr}(r_i, r_j \mid s)$ of their spike counts across repeated presentations of the same stimulus. The *signal correlation* is the correlation of their tuning curves across stimuli.

Measured noise correlations in sensory cortex are small, with coefficients between $0.05$ and $0.2$ for counts in windows of $100\,\mathrm{ms}$ to $1\,\mathrm{s}$, larger for neurons with similar tuning and for nearby ones, and they depend on arousal, attention and the state of the cortex ([7.16.18](/7.16.18#sec-18.7)). They arise from shared input and from slow common fluctuations of excitability and are not removed by averaging over the population. Their effect on information depends on how they are oriented relative to the signal.

### 26.5.1. Two Neurons

Consider two neurons with Gaussian noise of equal variance $\sigma^2$, correlation $\rho$, and tuning-curve slopes $\boldsymbol{f}' = (f_1', f_2')^{\mathsf T}$. The covariance matrix is $\Sigma = \sigma^2\begin{pmatrix}1 & \rho\\ \rho & 1\end{pmatrix}$ with $\Sigma^{-1} = \dfrac{1}{\sigma^2(1 - \rho^2)}\begin{pmatrix}1 & -\rho\\ -\rho & 1\end{pmatrix}$. If the slopes are equal, $\boldsymbol{f}' = a(1, 1)^{\mathsf T}$, and if they are opposite, $\boldsymbol{f}' = a(1, -1)^{\mathsf T}$, then

$$
I_{\mathrm{F}} = \frac{2a^2}{\sigma^2(1 + \rho)} \quad\text{(equal slopes)},\qquad I_{\mathrm{F}} = \frac{2a^2}{\sigma^2(1 - \rho)} \quad\text{(opposite slopes)}. \tag{26.10}
$$
Positive noise correlation therefore *reduces* the information in a pair of neurons that respond to the stimulus in the same way, and *increases* it in a pair with opposite slopes: when both neurons rise together with the noise, the signal cannot be told from the noise, whereas when one rises and the other falls with the stimulus, the common fluctuation cancels in their difference (panels A and B of the figure). Because neurons with similar tuning are the ones with larger noise correlation, the net effect in a real population is usually a reduction.

### 26.5.2. Large Populations

The reduction is not harmless in a large population. Let $N$ neurons have the same slope $a$, variance $\sigma^2$ and a uniform correlation $\rho$ between all pairs. The covariance matrix $\sigma^2[(1 - \rho)I + \rho\boldsymbol{1}\boldsymbol{1}^{\mathsf T}]$ has the eigenvalue $\sigma^2[1 + (N - 1)\rho]$ along the direction $\boldsymbol{1}$, and $\boldsymbol{f}' = a\boldsymbol{1}$ lies along it, so that

$$
I_{\mathrm{F}} = \frac{Na^2}{\sigma^2[1 + (N - 1)\rho]} \;\longrightarrow\; \frac{a^2}{\sigma^2\rho} \quad (N \to \infty).
$$
The information *saturates*: beyond $N \approx 1/\rho$, adding neurons gives nothing, because the fluctuation shared by all of them is indistinguishable from a change of the stimulus (Zohary, Shadlen and Newsome, 1994). This resolves much of the puzzle of Section 26.2: MT neurons with a correlation of about $0.1$ saturate at the information of roughly ten independent neurons, so a pool of a hundred or a thousand neurons improves the threshold of a single neuron by only a factor of about $\sqrt{10} \approx 3$.

Not all correlations limit information. A general criterion follows from the structure of Eq. (26.8). Information can grow without bound with $N$ only if the noise has no component along the signal direction $\boldsymbol{f}'$ that grows with $N$; noise that is parallel to $\boldsymbol{f}'$ is, by definition, indistinguishable from a signal.

**Definition 26.5.2 (Information-Limiting Correlations)** Noise whose covariance has a component proportional to $\boldsymbol{f}'\boldsymbol{f}'^{\mathsf T}$, that is, $\Sigma = \Sigma_0 + \varepsilon\,\boldsymbol{f}'\boldsymbol{f}'^{\mathsf T}$ with $\varepsilon > 0$, is called **information-limiting correlations** (or differential correlations; Moreno-Bote et al., 2014).

**Theorem 26.5.1 (Saturation of Information)** For $\Sigma = \Sigma_0 + \varepsilon\boldsymbol{f}'\boldsymbol{f}'^{\mathsf T}$, the Fisher information is

$$
I_{\mathrm{F}} = \frac{I_0}{1 + \varepsilon I_0}, \qquad I_0 = \boldsymbol{f}'^{\mathsf T}\Sigma_0^{-1}\boldsymbol{f}', \tag{26.11}
$$
so that $I_{\mathrm{F}} < 1/\varepsilon$ however large the population, and $I_{\mathrm{F}} \to 1/\varepsilon$ as $I_0 \to \infty$.

**Proof** By the **Sherman–Morrison formula** ([2.1.2](/2.1.2#thm-2.7.2)), $\Sigma^{-1} = \Sigma_0^{-1} - \dfrac{\varepsilon\,\Sigma_0^{-1}\boldsymbol{f}'\boldsymbol{f}'^{\mathsf T}\Sigma_0^{-1}}{1 + \varepsilon I_0}$. Hence $\boldsymbol{f}'^{\mathsf T}\Sigma^{-1}\boldsymbol{f}' = I_0 - \dfrac{\varepsilon I_0^2}{1 + \varepsilon I_0} = \dfrac{I_0}{1 + \varepsilon I_0}$. $\square$

Such correlations arise naturally when the noise is itself a fluctuation of the stimulus estimate that is shared by the whole population: a noisy input, imprecision of the sensory front end or an error in the early processing, all of which are passed on as a change of the apparent stimulus. They are the only correlations that cap the information at a finite value in an arbitrarily large population. Correlations that depend on tuning similarity (limited-range correlations, such as $\rho_{ij} \propto \mathrm{e}^{-\lvert\theta_i - \theta_j\rvert/w}$) also reduce the information, as the figure shows. In a perfectly homogeneous population they can even make it saturate (Sompolinsky et al., 2001), but by Theorem 26.5.1 only because, in the limit of large $N$, they contain a differential component; in heterogeneous populations, like real ones, they lower the slope of the growth without imposing a ceiling (Ecker et al., 2011). The experimental consequence is a test: record the information that a decoder extracts from growing subpopulations; information that increases linearly and then bends to a plateau as $N$ grows, in the manner of Eq. (26.11), is a signature of information-limiting correlations.

![Noise correlations and information. A: spike counts of two neurons with the same tuning slope for two nearby stimuli (blue and orange; ellipses are 1 s.d. contours; dashed: independent noise, solid: noise correlation 0.7). With a positive correlation the elongated noise distributions overlap more: information is reduced (Eq. (26.10)). B: the same for two neurons with opposite slopes: the distributions are more separated and the information is greater. C: Fisher information of a ring of von Mises neurons against the number of neurons N (baseline 2, amplitude 20, κ = 2, Fano factor 1) for independent noise (grows in proportion to N), for limited-range correlations (coefficient 0.2 exp(−Δθ/15°), Δθ the difference of preferred directions), and for information-limiting correlations with ε = 1/400 (Eq. (26.11); the dotted line is the ceiling 1/ε = 400). Both kinds of correlation reduce the growth; the information-limiting ones bound it at 1/ε, and in this perfectly homogeneous population the limited-range ones also make it level off](./plots/noise-correlations.py)

## 26.6. Decoding Spike Trains

So far the response was a count in a window. A stimulus that varies in time, such as the velocity of an object or the amplitude of a sound, is encoded in the times of the spikes, and the decoder estimates the stimulus at each time $t$ from the spike train $\rho(t) = \sum_k\delta(t - t_k)$ ([7.16.16](/7.16.16#sec-16.2)). The simplest decoder is linear: it filters the spike train with a kernel $K$,

$$
\hat s(t) = \bar s + \int K(\tau)\bigl[\rho(t - \tau) - \bar r\bigr]\,\mathrm{d}\tau, \tag{26.12}
$$
where $\bar r$ is the mean rate; each spike is replaced by a copy of $K$ placed at the time of the spike. For a population, each neuron has its own kernel and the contributions are summed. The kernel is chosen to minimize the mean squared error $\langle(\hat s - s)^2\rangle$, as in the linear regression of [3.3](/3.3) (it is the **Wiener filter** of [7.6.14](/7.6.14)); for a stationary stimulus and a stationary response the solution is found in the frequency domain, where convolution becomes multiplication ([2.5](/2.5)):

$$
\tilde K(\omega) = \frac{P_{s\rho}(\omega)}{P_{\rho\rho}(\omega)}, \tag{26.13}
$$
the cross-spectrum of stimulus and spike train divided by the power spectrum of the spike train. The mean squared error at frequency $\omega$ is then $P_{ss}(\omega)[1 - C(\omega)]$, where $C(\omega) = \lvert P_{s\rho}\rvert^2/(P_{ss}P_{\rho\rho})$ is the coherence between stimulus and spikes, so the coherence tells which frequency components of the stimulus can be recovered; a function of it is also a lower bound on the information rate ([7.16.20](/7.16.20)). The kernel is not causal: because a neuron responds to the stimulus with a delay, the spikes that tell the value of $s$ at $t$ occur *after* $t$, and the decoder must look at the spike train from $t$ to some tens of milliseconds later. It reflects the same filtering as the spike-triggered average of [7.16.16](/7.16.16#sec-16.5), reversed in time, and its width is set by the correlation time of the stimulus and the spike rate.

Applied to an ON–OFF population of Poisson neurons (figure), the linear decoder recovers the fast fluctuations of a stimulus with a correlation time of $30\,\mathrm{ms}$ only when the neurons are many: one neuron gives a smoothed, partial image (correlation $0.5$), twenty give $0.88$. The ON and OFF neurons have filters of opposite sign, positive for the neuron that fires more when the stimulus rises and negative for the other, and both peak at the response delay. In the fly, Bialek, Rieke and colleagues (1991) reconstructed the angular velocity of a moving pattern from the spikes of the motion-sensitive neuron H1 in this way and measured the reconstruction error; in the electric fish, the amplitude modulation of the electric field is recovered from afferent spikes similarly. Beyond the linear decoder, the full Bayesian decoder of Section 26.3 can be applied in time, as in the decoding of position from hippocampal place cells ([7.16.42](/7.16.42)), where the stimulus is a trajectory with a prior given by the dynamics of movement.

![Linear reconstruction of a time-varying stimulus from spikes (low-pass filtered Gaussian noise with time constant 30 ms; ON and OFF Poisson neurons with a response delay of 20 ms; ridge regression for the filters, fitted on 80 s and tested on 40 s). A: stimulus (black) and its reconstruction from one neuron (orange) and from 20 neurons (blue) in a segment of the test data. B: the decoding filters of one ON and one OFF neuron of the 20-neuron decoder, against the time of the spike relative to the reconstructed time t: spikes about 20 ms after t carry the most information. C: correlation between stimulus and reconstruction in the test data against the number of neurons](./plots/spike-reconstruction.py)

## Summary

- Decoding is inference: the encoding model $\mathbb{P}(\boldsymbol{r} \mid s)$ and a prior give the posterior of Eq. (26.1); the posterior width measures reliability. Priors matter (Example 26.1.1).
- Signal detection theory compares two stimuli; the ROC area equals the proportion correct of a forced-choice observer (Theorem 26.2.1, Eq. (26.2)). The neurometric function of single MT neurons is close to the monkey's psychometric function (Definition 26.2.2).
- For independent Poisson neurons the log posterior is Eq. (26.4); for dense Gaussian tuning the ML estimate is the center of mass (Eq. (26.5)), and for von Mises tuning without baseline it is exactly the population vector (Eq. (26.6)).
- The Fisher information $I_{\mathrm{F}} = \sum_i f_i'^2/f_i$ (Eq. (26.8)) bounds the precision of any decoder, and ML attains the bound. For Gaussian tuning in $D$ dimensions $I_{\mathrm{F}} \propto \sigma^{D-2}$ (Eq. (26.9)): narrow tuning is optimal only in one dimension.
- Noise correlations reduce information when they are aligned with the signal (Eq. (26.10)); uniform correlations make information saturate at $a^2/(\sigma^2\rho)$, and information-limiting correlations $\varepsilon\boldsymbol{f}'\boldsymbol{f}'^{\mathsf T}$ cap it at $1/\varepsilon$ (Theorem 26.5.1).
- Time-varying stimuli are reconstructed from spike trains by an optimal linear filter (Eqs. (26.12)–(26.13)), whose error spectrum is set by the coherence.

## Questions

1. Show that for Gaussian responses with equal variances the area under the ROC curve is $\Phi(d'/\sqrt2)$, and compute the proportion correct for a neuron whose mean counts to the two stimuli are $40$ and $50$ with variance $30$ in both cases.

   **Answer** By Theorem 26.2.1 the area is $\mathbb{P}(r_+ > r_-)$; $r_+ - r_-$ is normal with mean $\mu_+ - \mu_- = \sigma d'$ and variance $2\sigma^2$, so the probability is $\Phi(\sigma d'/(\sqrt2\sigma)) = \Phi(d'/\sqrt2)$. Here $d' = 10/\sqrt{30} = 1.83$, $d'/\sqrt2 = 1.29$ and $\Phi(1.29) \approx 0.90$: the neuron discriminates correctly in $90\,\%$ of two-alternative trials.
2. A neuron has a Gaussian tuning curve with peak $A = 20$ and width $\sigma = 15^\circ$ and Poisson variability. At which stimulus offset from the peak is its Fisher information largest, and what is its value there?

   **Answer** $f' = -f\,u/\sigma^2$ with $u = s - s_{\mathrm{pref}}$, so $f'^2/f = f u^2/\sigma^4 = A u^2\mathrm{e}^{-u^2/2\sigma^2}/\sigma^4$. Setting the derivative to zero gives $u^2 = 2\sigma^2$, i.e. $u = \sqrt2\,\sigma = 21^\circ$, on the flank, not at the peak. The value is $A\cdot2\sigma^2\mathrm{e}^{-1}/\sigma^4 = 2A/(\mathrm{e}\sigma^2) = 2\times20/(2.718\times225) \approx 0.065\,\mathrm{deg^{-2}}$ per counting window; one neuron alone gives a threshold of $I_{\mathrm{F}}^{-1/2} \approx 3.9^\circ$ there.
3. For two neurons with equal slopes and noise correlation $\rho = 0.5$, by what factor does the correlation change the Fisher information compared with independent noise? What if the slopes are opposite?

   **Answer** From Eq. (26.10), independent noise gives $I_{\mathrm{F}} = 2a^2/\sigma^2$. With equal slopes the correlation multiplies it by $1/(1 + \rho) = 2/3$; with opposite slopes by $1/(1 - \rho) = 2$. So the same correlation costs a third of the information in one case and doubles it in the other, which is why the structure of the correlations relative to the tuning, not their size alone, matters.
4. Each neuron of a population contributes $5\,\mathrm{rad^{-2}}$ to the independent-noise information, and there are information-limiting correlations with $\varepsilon = 1/400\,\mathrm{rad^2}$. How many neurons are needed to reach $90\,\%$ of the saturation value, and what is the corresponding threshold?

   **Answer** The ceiling is $1/\varepsilon = 400\,\mathrm{rad^{-2}}$. By Eq. (26.11), $I_{\mathrm{F}}/(1/\varepsilon) = \varepsilon I_0/(1 + \varepsilon I_0) = 0.9$ requires $\varepsilon I_0 = 9$, i.e. $I_0 = 3600$, so $N = 3600/5 = 720$ neurons. Then $I_{\mathrm{F}} = 360$ and the threshold is $I_{\mathrm{F}}^{-1/2} = 0.053\,\mathrm{rad} = 3.0^\circ$, only slightly above the limit of $2.9^\circ$ set by the correlations. Further neurons are almost useless.
5. (Open question) Design an analysis of simultaneous recordings from a few hundred neurons that tests whether the information in the population is limited by differential correlations.

   **Answer** Fit a decoder to subsets of $n$ neurons for several values of $n$ (random subsets, many repetitions, cross-validated) and compute the information, for example from the sensitivity of a linear discriminant for two nearby stimuli, $d'^2 \approx \Delta s^2 I_{\mathrm{F}}$. Plot $I_{\mathrm{F}}$ against $n$: independent or generic correlations give a curve that continues to rise (linearly for independent noise), while differential correlations give saturation, $I_{\mathrm{F}}(n) \approx I_0(n)/(1 + \varepsilon I_0(n))$. Because the plateau can be mimicked by overfitting or by insufficient trials, shuffled trials (which destroy correlations) and the fitted noise covariance should be used to compute $I_0$ from the same data; the estimated $\varepsilon$ must be significantly different from zero when the decoder's bias is controlled. Moreno-Bote et al. (2014) proposed to estimate $\varepsilon$ from the difference between the information of the data and that with the component of the noise along $\boldsymbol{f}'$ removed.
