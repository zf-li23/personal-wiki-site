---
title: Bayesian Learning
description: The Bayesian view in machine learning. Computing posterior probabilities of hypotheses with Bayes' theorem; MAP and ML hypotheses, regularization as a prior, maximum likelihood and least squares; the Bayes optimal classifier and the Gibbs algorithm; the naive Bayes classifier, Laplace smoothing and Dirichlet priors, three event models, log probabilities and practical points; spam filtering and word sense disambiguation.
source_hash: 0ecf4df49bf8
---

Bayesian learning treats learning as probabilistic inference: every hypothesis has a probability, and after the training data are observed, **Bayes' theorem** ([3.1.2](/3.1.2)) updates the prior probabilities into posterior probabilities, from which one chooses a hypothesis or makes predictions directly. This view is useful in two ways. In theory, it gives many learning algorithms a unified interpretation: least squares, regularization and ensembles can all be seen as approximations to some kind of Bayesian inference. In practice, it directly yields a family of simple, fast and effective algorithms, the most important of which is the naive Bayes classifier, still the standard baseline for text classification. This chapter emphasizes the latter: how to turn Bayesian principles into a usable classifier, and the numerical, smoothing and feature issues to watch for in use. Statistical concepts such as prior, posterior and conjugate prior were defined in [Bayesian Inference](/3.2.7) and are cited here only when needed; for a more systematic and theoretical treatment see [Bayesian Statistics](/3.7). The evaluation methods of the [previous chapter](/4.6.2) apply to the classifiers of this chapter, while the $k$-nearest neighbors method of the [next chapter](/4.6.4) takes an entirely different approach: it makes no assumption about the distribution of the data.

## 3.1. Bayes' Theorem and the Posterior of a Hypothesis

### 3.1.1. Inferring the Posterior from the Prior

Let $H$ be the hypothesis space and $D$ the training data. For every hypothesis $h \in H$,

$$
\mathbb{P}(h \mid D) = \frac{\mathbb{P}(D \mid h)\,\mathbb{P}(h)}{\mathbb{P}(D)},
$$
where the terms mean the following:

| Notation | Name | Meaning |
|---|---|---|
| $\mathbb{P}(h)$ | Prior probability | Belief in $h$ before observing the data, reflecting background knowledge |
| $\mathbb{P}(D \mid h)$ | Likelihood | Probability of observing $D$ if $h$ holds |
| $\mathbb{P}(h \mid D)$ | Posterior probability | Belief in $h$ after observing $D$ |
| $\mathbb{P}(D)$ | Evidence | Marginal probability of $D$, $\mathbb{P}(D) = \sum_{h \in H}\mathbb{P}(D \mid h)\,\mathbb{P}(h)$ |

These quantities are the **prior distribution**, **likelihood function** and **posterior distribution** of statistics ([3.2.7](/3.2.7)), with hypotheses in place of parameters. Here the hypotheses in $H$ are required to be mutually exclusive and jointly exhaustive, that is, $\sum_{h \in H}\mathbb{P}(h) = 1$. $\mathbb{P}(D)$ does not depend on $h$ and can be ignored when comparing different hypotheses. The likelihood is often a product of many small probabilities, and in practice one always works with the log-likelihood $\log \mathbb{P}(D \mid h)$.

**Example 3.1.1** The prevalence of a certain cancer in the population is $0.008$. A laboratory test gives a positive result for a patient with probability $0.98$ and a negative result for a non-patient with probability $0.97$. Someone tests positive; the probability that this person has cancer is

$$
\mathbb{P}(\text{cancer} \mid +) = \frac{0.98 \times 0.008}{0.98 \times 0.008 + 0.03 \times 0.992} = \frac{0.00784}{0.03760} \approx 0.21.
$$

The test is quite accurate, yet the probability of disease given a positive result is only about one fifth. The reason is the very small prior probability: non-patients outnumber patients by more than a hundred to one, and their $3\%$ false positives outnumber the true positives among patients. Ignoring the prior (the base rate) is the most common error in intuitive reasoning.

## 3.2. MAP and ML Hypotheses

### 3.2.1. Two Kinds of Hypotheses

Learning usually means finding the most probable hypothesis given the training data.

**Definition 3.2.1 (MAP and ML Hypotheses)** The hypothesis that maximizes the posterior probability,

$$
h_{\mathrm{MAP}} = \arg\max_{h \in H}\ \mathbb{P}(h \mid D) = \arg\max_{h \in H}\ \mathbb{P}(D \mid h)\,\mathbb{P}(h),
$$
is called the **maximum a posteriori hypothesis** (MAP hypothesis). The hypothesis that maximizes the likelihood,

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \mathbb{P}(D \mid h),
$$
is called the **maximum likelihood hypothesis** (ML hypothesis).

When the hypotheses are described by continuous parameters, these are the **maximum a posteriori estimate** and **maximum likelihood estimation** of statistics ([3.2.7](/3.2.7), [3.2.3](/3.2.3)). If nothing is known about the hypotheses, or if all hypotheses are believed to have the same prior probability, then $\mathbb{P}(h)$ is constant and $h_{\mathrm{MAP}} = h_{\mathrm{ML}}$.

**Example 3.2.1** In Example 3.1.1 there are two hypotheses, cancer and $\lnot$cancer. We have $\mathbb{P}(+ \mid \text{cancer})\,\mathbb{P}(\text{cancer}) = 0.0078$ and $\mathbb{P}(+ \mid \lnot\text{cancer})\,\mathbb{P}(\lnot\text{cancer}) = 0.0298$, so $h_{\mathrm{MAP}} = \lnot\text{cancer}$. On the other hand, $\mathbb{P}(+ \mid \text{cancer}) = 0.98 > \mathbb{P}(+ \mid \lnot\text{cancer}) = 0.03$, so $h_{\mathrm{ML}} = \text{cancer}$. The two differ, and the difference comes entirely from the prior.

**Example 3.2.2** There are two coins whose probabilities of heads are $p$ and $q$. Each time, coin 1 is chosen with probability $a$ and coin 2 with probability $1-a$, and the chosen coin is tossed several times. The parameters $a, p, q$ are all unknown. Four records are observed (the digit is the chosen coin): 2HHHT, 1HTHT, 2HHHT, 2HTTH. Find the ML estimates of $a, p, q$.

Consider first a single coin: $m$ tosses give $k$ heads, and the log-likelihood is $\ell(p) = k\log p + (m-k)\log(1-p)$. Setting $\ell'(p) = \frac{k}{p} - \frac{m-k}{1-p} = 0$ gives $\hat p = k/m$. The likelihood of the three parameters can be maximized separately, each in this form: coin 1 was chosen once among 4 records, so $\hat a = 1/4$; coin 1 was tossed 4 times with 2 heads, so $\hat p = 2/4$; coin 2 was tossed 12 times with 8 heads, so $\hat q = 8/12$.

If the records did not contain the coin labels, the likelihood would involve a latent variable and could no longer be maximized separately; this is exactly the problem handled by the **EM algorithm**, and [3.5.6](/3.5.6) uses precisely the two-coin example.

### 3.2.2. The Prior as Regularization

After taking logarithms, the MAP hypothesis is

$$
h_{\mathrm{MAP}} = \arg\max_{h \in H}\ \bigl[\log \mathbb{P}(D \mid h) + \log \mathbb{P}(h)\bigr] = \arg\min_{h \in H}\ \bigl[-\log \mathbb{P}(D \mid h) - \log \mathbb{P}(h)\bigr].
$$
The first term is the loss for fitting the data and the second is a penalty on the hypothesis. Most of the familiar "loss plus regularizer" objective functions in machine learning can be interpreted in this way:

| Prior $\mathbb{P}(\boldsymbol{w})$ | $-\log \mathbb{P}(\boldsymbol{w})$ (up to a constant) | Corresponding method |
|---|---|---|
| Uniform (noninformative) | Constant | Maximum likelihood, no regularization |
| $\boldsymbol{w} \sim \mathcal{N}(\boldsymbol{0}, \tau^2 I)$ | $\frac{1}{2\tau^2}\|\boldsymbol{w}\|_2^2$ | $L_2$ regularization (**ridge regression**, weight decay) |
| Components independent and Laplace distributed with scale $b$ | $\frac{1}{b}\|\boldsymbol{w}\|_1$ | $L_1$ regularization (**Lasso**) |

The regularization coefficient thus expresses the strength of the prior: the smaller $\tau$ is, the more concentrated the prior is around $\boldsymbol{0}$ and the heavier the penalty. In practice the regularization coefficient is chosen by cross-validation ([4.6.2](/4.6.2#sec-2.2.2)), not determined by actual prior beliefs.

### 3.2.3. Maximum Likelihood and Least Squares

Let the training data be $\langle x_i, d_i\rangle$, $i = 1, \dots, m$, where $d_i = f(x_i) + e_i$, $f$ is the noise-free target function, and the noise terms $e_i$ are independent and identically distributed as $\mathcal{N}(0, \sigma^2)$.

**Theorem 3.2.1 (Maximum Likelihood and Least Squares)** Under the above assumptions,

$$
h_{\mathrm{ML}} = \arg\min_{h \in H}\ \sum_{i=1}^m \bigl(d_i - h(x_i)\bigr)^2,
$$
that is, the maximum likelihood hypothesis is the hypothesis that minimizes the sum of squared errors.

**Proof** Given $h$, the $d_i \sim \mathcal{N}(h(x_i), \sigma^2)$ are mutually independent, so

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \prod_{i=1}^m \frac{1}{\sqrt{2\pi}\,\sigma}\exp\Bigl(-\frac{(d_i - h(x_i))^2}{2\sigma^2}\Bigr).
$$
Since $\ln$ is increasing, taking logarithms does not change the maximizer:

$$
h_{\mathrm{ML}} = \arg\max_{h \in H}\ \sum_{i=1}^m \Bigl[-\ln(\sqrt{2\pi}\,\sigma) - \frac{(d_i - h(x_i))^2}{2\sigma^2}\Bigr].
$$
The first term does not depend on $h$; after dropping the constant factor $\frac{1}{2\sigma^2}$, maximizing the negative sum of squared errors is minimizing the sum of squared errors. $\square$

This gives the LMS rule of [4.6.1](/4.6.1) and the method of **least squares** a probabilistic interpretation: under normal noise they yield the ML hypothesis. A different noise model gives a different loss: Laplace noise corresponds to **least absolute deviations**; in binary classification, if $h(x)$ is interpreted as the probability of the positive class and the labels follow a Bernoulli distribution, the negative log-likelihood is the cross-entropy loss, which leads to **logistic regression** ([3.4.12](/3.4.12)).

## 3.3. The Bayes Optimal Classifier and the Gibbs Algorithm

### 3.3.1. The Bayes Optimal Classifier

The question so far was "what is the most probable hypothesis given the data?". In classification the real question is "what is the most probable class of a new example $x$ given the data?". The answers to the two questions can differ.

**Example 3.3.1** Suppose the hypothesis space contains only three hypotheses, with posterior probabilities $\mathbb{P}(h_1 \mid D) = 0.4$ and $\mathbb{P}(h_2 \mid D) = \mathbb{P}(h_3 \mid D) = 0.3$. The hypothesis $h_1$ classifies $x$ as positive, and $h_2, h_3$ classify it as negative. The MAP hypothesis is $h_1$, which says that $x$ is positive; but the posterior probability that $x$ is positive is only $0.4$, and that it is negative is $0.6$.

**Definition 3.3.1 (Bayes Optimal Classifier)** For a set of classes $\mathcal{V}$ and a new example $x$, the rule that classifies by

$$
v^* = \arg\max_{v \in \mathcal{V}}\ \sum_{h \in H}\mathbb{P}(v \mid x, h)\,\mathbb{P}(h \mid D)
$$
is called the **Bayes optimal classifier**.

It does not select one hypothesis but lets all hypotheses vote, weighted by their posterior probabilities. The sum is the **posterior predictive distribution** of the class of $x$ given $D$ ([3.2.7](/3.2.7)), so the Bayes optimal classifier takes the mode of the posterior predictive distribution; it is the **Bayes classifier** ([3.4.10](/3.4.10)) that uses the posterior predictive distribution as the class probabilities. With the same hypothesis space and prior, no other classification method has a better average performance (the average being over the prior and the data). The combined result may even not belong to any single hypothesis in $H$.

The price is computation: one must sum or integrate over the entire hypothesis space. Except in a few cases such as conjugate priors, this is infeasible.

### 3.3.2. The Gibbs Algorithm

**Definition 3.3.2 (Gibbs Algorithm)** Draw a hypothesis $h$ at random from the posterior distribution $\mathbb{P}(h \mid D)$ and use $h$ to classify the new example. This method is called the **Gibbs algorithm**.

The Gibbs algorithm needs only one draw, so its computation is much smaller than that of the Bayes optimal classifier, and the price is limited: if the target concept is indeed drawn at random from the prior distribution, the expected error rate of the Gibbs algorithm is at most twice that of the Bayes optimal classifier (Haussler, Kearns and Schapire, 1994).

Approximations to the Bayes optimal classifier are everywhere in modern machine learning: drawing several hypotheses from the posterior with Markov chain Monte Carlo methods and averaging them (**Gibbs sampling** is one of these, [3.5.9](/3.5.9)); training several neural networks with different random initializations and averaging their predictions (deep ensembles); and ensemble learning more generally ([4.6.6](/4.6.6)) can also be understood from this angle.

## 3.4. The Naive Bayes Classifier

### 3.4.1. The Conditional Independence Assumption

Let each example be described by $n$ attributes, $x = (a_1, \dots, a_n)$, with class $v \in \mathcal{V}$. The most probable class is

$$
v_{\mathrm{MAP}} = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(v \mid a_1, \dots, a_n) = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(a_1, \dots, a_n \mid v)\,\mathbb{P}(v).
$$
$\mathbb{P}(v)$ is easy to estimate from the training data: just count how many examples each class has. $\mathbb{P}(a_1, \dots, a_n \mid v)$ is not: the joint distribution of $n$ binary attributes has $2^n - 1$ parameters in each class, and even for $n = 30$ one would need on the order of a billion examples to see each combination of values a few times.

**Definition 3.4.1 (Naive Bayes Classifier)** Assume that the attributes are conditionally independent given the class,

$$
\mathbb{P}(a_1, \dots, a_n \mid v) = \prod_{i=1}^n \mathbb{P}(a_i \mid v).
$$
The resulting classification rule

$$
v_{\mathrm{NB}} = \arg\max_{v \in \mathcal{V}}\ \mathbb{P}(v)\prod_{i=1}^n \mathbb{P}(a_i \mid v)
$$
is called the **naive Bayes classifier**.

The conditional independence assumption reduces the number of parameters from exponential to the order of $n \lvert\mathcal{V}\rvert$, and each $\mathbb{P}(a_i \mid v)$ requires only a one-dimensional count. If the conditional independence assumption holds, then $v_{\mathrm{NB}} = v_{\mathrm{MAP}}$.

This assumption almost never holds in practice (in text, "machine" and "learning" are obviously not independent), yet naive Bayes often classifies well. The reason is that classification requires only that the correct class receive the highest score, not that the probabilities be accurate: correlations among attributes make the estimated posterior probabilities too extreme (usually too close to $0$ or $1$), but do not necessarily change the class at which the maximum is attained (Domingos and Pazzani, 1997). The class decisions of naive Bayes are therefore usable, but the probabilities it outputs should not be taken directly as trustworthy probabilities; if needed, they should be calibrated first.

Naive Bayes is a generative classifier: it models $\mathbb{P}(x \mid v)$ and $\mathbb{P}(v)$ and then obtains $\mathbb{P}(v \mid x)$ by Bayes' theorem. Logistic regression, which models $\mathbb{P}(v \mid x)$ directly, is discriminative. The two form a generative–discriminative pair: for binary attributes the decision function of naive Bayes is also a linear function of the attributes. Ng and Jordan (2002) found that naive Bayes needs far fewer samples to reach its asymptotic error rate (of the order of the logarithm of the number of attributes), whereas the asymptotic error rate of logistic regression is lower; so naive Bayes is often better when training data are scarce, and logistic regression overtakes it when data are plentiful.

### 3.4.2. Parameter Estimation and Laplace Smoothing

The ML estimates of the parameters are relative frequencies. Take text classification as an example: let the vocabulary have $K$ words, let $n_{v,j}$ be the total number of occurrences of the $j$-th word in all training documents of class $v$, and let $n_v = \sum_j n_{v,j}$; then $\hat{\mathbb{P}}(w_j \mid v) = n_{v,j}/n_v$. The problem is that as soon as a word never occurs in the training documents of some class, its estimated probability is $0$, and a single $0$ in the product makes the posterior probability of the whole class $0$, however strong the other evidence is. The less training data and the larger the vocabulary, the more common this becomes.

**Definition 3.4.2 (Laplace Smoothing)** For $\alpha > 0$, replacing the relative frequency by

$$
\hat{\mathbb{P}}(w_j \mid v) = \frac{n_{v,j} + \alpha}{n_v + \alpha K}
$$
is called additive smoothing; for $\alpha = 1$ it is called **Laplace smoothing** (add-one smoothing).

Laplace smoothing amounts to having every word "seen" once beforehand in every class. For $0 < \alpha < 1$ it is called Lidstone smoothing, which smooths less and is often better; $\alpha$ is a **hyperparameter**, selected with a validation set or cross-validation. The $m$-estimate $\frac{n_{v,j} + m p}{n_v + m}$ in Mitchell's textbook expresses the same idea: $p$ is a prior estimate (for example the uniform $1/K$) and $m$ is the "equivalent sample size"; taking $p = 1/K$ and $m = \alpha K$ gives the formula above.

Smoothing has a clear Bayesian interpretation. Let $\boldsymbol{\theta}_v = (\theta_{v,1}, \dots, \theta_{v,K})$ be the word distribution of class $v$; the word counts follow a **multinomial distribution**, whose **conjugate prior** ([3.2.7](/3.2.7)) is the Dirichlet distribution.

**Definition 3.4.3 (Dirichlet Distribution)** Let $\alpha_1, \dots, \alpha_K > 0$. The distribution on the probability simplex $\{\boldsymbol{\theta}\colon \theta_j \ge 0,\ \sum_j \theta_j = 1\}$ with density

$$
f(\boldsymbol{\theta}) = \frac{\Gamma(\alpha_1 + \cdots + \alpha_K)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{j=1}^K \theta_j^{\alpha_j - 1}
$$
is called the **Dirichlet distribution** $\mathrm{Dir}(\alpha_1, \dots, \alpha_K)$. For $K = 2$ it is the **beta distribution**.

Take the symmetric prior $\mathrm{Dir}(\alpha, \dots, \alpha)$. After observing the counts $n_{v,1}, \dots, n_{v,K}$, the posterior is $\mathrm{Dir}(n_{v,1} + \alpha, \dots, n_{v,K} + \alpha)$, and its **posterior mean** is exactly the estimate in Definition 3.4.2. Laplace smoothing is therefore the posterior mean estimate under the uniform prior ($\alpha = 1$); it is also the maximum a posteriori estimate under the prior $\mathrm{Dir}(2, \dots, 2)$. The larger $\alpha$ is, the stronger the prior and the more the estimate is pulled toward the uniform distribution.

### 3.4.3. Three Event Models

There are different choices for "what the attribute $a_i$ is and which distribution $\mathbb{P}(a_i \mid v)$ takes", corresponding to several commonly used variants of naive Bayes:

| Variant | Attribute | $\mathbb{P}(a_i \mid v)$ | Parameter estimate | Use |
|---|---|---|---|---|
| Multinomial naive Bayes | Number of occurrences of a word in the document | Probability of word $w_i$ in a multinomial distribution | Definition 3.4.2 | Text classification (usually best with long documents and large vocabularies) |
| Bernoulli naive Bayes | Whether each word occurs ($0/1$) | $\theta_{v,i}^{a_i}(1-\theta_{v,i})^{1-a_i}$ | $\hat\theta_{v,i} = \frac{\text{number of class-}v\text{ documents containing } w_i + \alpha}{\text{number of class-}v\text{ documents} + 2\alpha}$ | Short texts, binary features |
| Gaussian naive Bayes | Continuous attribute | Density of $\mathcal{N}(\mu_{v,i}, \sigma_{v,i}^2)$ | Sample mean and variance of each attribute in each class | General classification with continuous features |

The Bernoulli model differs from the multinomial model in that the former also treats "the word does not occur" as evidence (multiplying by $1 - \theta_{v,i}$), whereas the latter looks only at the words that occur and counts how many times they occur. The comparison by McCallum and Nigam (1998) shows that the multinomial model is usually better when the vocabulary is large. In the Gaussian model, if all classes share the same variances, the decision boundary is linear, which agrees with linear discriminant analysis with a diagonal covariance matrix in [3.4.10](/3.4.10); to avoid variance estimates of $0$, implementations usually add a small constant to every variance. Attributes of mixed types can each use a suitable distribution, with the log probabilities added.

### 3.4.4. Practical Points

**Example 3.4.1** We train a multinomial naive Bayes classifier (with Laplace smoothing) on six short emails and then predict the probability that each of three new emails is spam. We first implement it from scratch with NumPy, with all computation done in log space.

```python
import numpy as np

docs = ["win cash now", "cheap pills win", "win a free prize now",
        "meeting at noon", "project meeting notes", "lunch at noon"]
labels = np.array([1, 1, 1, 0, 0, 0])                 # 1 = spam, 0 = ham

vocab = sorted({w for d in docs for w in d.split()})
index = {w: j for j, w in enumerate(vocab)}

def counts(doc):
    x = np.zeros(len(vocab))
    for w in doc.split():
        if w in index:                                # unseen words are ignored
            x[index[w]] += 1
    return x

X = np.array([counts(d) for d in docs])

def fit(X, y, alpha=1.0):
    classes = np.unique(y)
    log_prior = np.log(np.array([np.mean(y == c) for c in classes]))
    n_cw = np.array([X[y == c].sum(axis=0) for c in classes])          # word counts per class
    log_lik = np.log((n_cw + alpha) / (n_cw.sum(axis=1, keepdims=True) + alpha * X.shape[1]))
    return classes, log_prior, log_lik

def predict_log_proba(model, X):
    classes, log_prior, log_lik = model
    joint = X @ log_lik.T + log_prior                 # log P(c) + sum_j x_j log P(w_j | c)
    joint -= joint.max(axis=1, keepdims=True)         # log-sum-exp trick for normalization
    return joint - np.log(np.exp(joint).sum(axis=1, keepdims=True))

model = fit(X, labels)
for doc in ["win a prize", "notes for the meeting", "free lunch"]:
    p_spam = np.exp(predict_log_proba(model, counts(doc)[None, :]))[0, 1]
    print(f"{doc!r:26} P(spam | doc) = {p_spam:.3f}")
```

```text
'win a prize'              P(spam | doc) = 0.926
'notes for the meeting'    P(spam | doc) = 0.124
'free lunch'               P(spam | doc) = 0.458
```

The same model in scikit-learn takes only a few lines and gives the same result:

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

docs = ["win cash now", "cheap pills win", "win a free prize now",
        "meeting at noon", "project meeting notes", "lunch at noon"]
labels = [1, 1, 1, 0, 0, 0]
clf = make_pipeline(CountVectorizer(token_pattern=r"\b\w+\b"), MultinomialNB(alpha=1.0))
clf.fit(docs, labels)
print(clf.predict_proba(["win a prize", "notes for the meeting", "free lunch"])[:, 1].round(3))
```

```text
[0.926 0.124 0.458]
```

(Python 3.12, NumPy 2.5, scikit-learn 1.9.) Several points about using naive Bayes can be drawn from this example.

1. Use log probabilities. For an email of a thousand words, with a conditional probability of about $10^{-4}$ per word, the product is about $10^{-4000}$, far smaller than the smallest positive number a double-precision floating-point number can represent (about $10^{-308}$), so multiplying directly underflows to $0$. After taking logarithms the product becomes a sum: $\log \mathbb{P}(v) + \sum_j x_j \log \mathbb{P}(w_j \mid v)$. For classification it suffices to compare this sum; when normalized posterior probabilities are needed, use the log-sum-exp trick $\log\sum_k \mathrm{e}^{s_k} = m + \log\sum_k \mathrm{e}^{s_k - m}$ ($m = \max_k s_k$) to avoid overflow, which is the step of subtracting the maximum in the program above.
2. Smoothing is necessary. Without smoothing, the word "free" in "free lunch" has never occurred in legitimate emails, which would make the probability of the legitimate class $0$.
3. A word not seen in training is not in the vocabulary, and the simplest treatment is to ignore it ("for" and "the" in the program above).
4. Feature engineering matters more than the model (see Sec. 3.5.1): how to split words, whether to distinguish case, whether to add bigrams, and whether to treat the email header separately often matter more than switching to another model. Replacing raw counts by TF-IDF weighted term frequencies is also often effective in the multinomial model.
5. Class priors and thresholds. $\mathbb{P}(v)$ is estimated from the class proportions in the training set; if the class proportions at deployment differ, or the costs of the two kinds of error differ, the prior or the decision threshold should be adjusted, rather than simply taking the class with the largest posterior.
6. Training is a single pass of counting and can be updated incrementally: when a new email arrives one only updates the counts, with no retraining, which suits online settings.

Naive Bayes suits the following situations: many attributes and few samples (high-dimensional sparse text); very fast training and prediction needed; a simple and reliable baseline needed; data arriving as a stream. When attributes are strongly correlated (for example, one feature repeated many times has its evidence counted repeatedly), when accurate probabilities are needed, or when data are plentiful, logistic regression, gradient boosted trees or neural networks are usually better.

## 3.5. Applications

### 3.5.1. Spam Filtering

Spam filtering is one of the most successful applications of naive Bayes. Two early papers were published at the same academic conference in 1998, by Pantel and Lin and by Sahami et al. of Microsoft Research. In articles of 2002–2003, Paul Graham reported that the Bayesian filter he implemented himself caught $99.5\%$ of spam with a false positive rate below $0.03\%$, while the method of Pantel and Lin caught only $92\%$ with a false positive rate of $1.16\%$. The differences he identified have almost all to do with data and features rather than with the model:

- Too little training data: only 160 spam emails and 466 legitimate emails.
- The email header was ignored. The sender address, routing information and subject line in the header may be the most important evidence, and the same word in the subject (`Subject*FREE`) and in the body has a different meaning and should be a different feature.
- Words were stemmed, discarding useful distinctions (the spam probabilities of `free` and `free!!` differ greatly).
- All words were used, whereas Graham used only the 15 most significant words (those whose probabilities deviate most from $0.5$).
- No bias toward reducing false positives. Deleting a legitimate email costs far more than letting a spam email through; Graham counted the word frequencies in legitimate emails twice, making the filter more reluctant to classify an email as spam.

These lessons correspond one by one to the design issues in [4.6.1](/4.6.1#sec-1.3.1): do not discard any information arbitrarily; the two kinds of error have different costs, so evaluation must look at false positives and false negatives separately ([4.6.2](/4.6.2#sec-2.3.2)).

### 3.5.2. Word Sense Disambiguation

Many words have several senses: bank can mean a financial institution or a river bank; of the two occurrences of fly in "A fly flies into the kitchen", one is the noun for the insect and the other is the verb "to fly". Deciding from the context which sense a word takes in a sentence is called word sense disambiguation.

**Definition 3.5.1 (Word Sense Disambiguation)** Let a word $w$ have senses $s_1, \dots, s_K$, and let its context $c$ in one occurrence be the set of words $w_1, \dots, w_m$ around it. The task of deciding, from $c$, which sense $w$ takes in this occurrence is called **word sense disambiguation**.

To use naive Bayes for word sense disambiguation, take the senses as classes and the words in the context as attributes, and assume that they are conditionally independent given the sense:

$$
s^* = \arg\max_{s_k}\ \Bigl[\log \mathbb{P}(s_k) + \sum_{w_j \in c}\log \mathbb{P}(w_j \mid s_k)\Bigr],
$$
where $\mathbb{P}(s_k)$ and $\mathbb{P}(w_j \mid s_k)$ are estimated (with smoothing) from counts in a corpus annotated with senses: $\mathbb{P}(s_k) = C(s_k)/C(w)$ and $\mathbb{P}(w_j \mid s_k) = C(w_j, s_k)/C(s_k)$, where $C$ denotes a count. When money, loan and account occur in the context of bank, the sense "financial institution" is favored, and when river, water and fishing occur, "river bank" is favored. Gale, Church and Yarowsky (1992) obtained very good results for the time with this method. Today's approach uses context-dependent word representations from pre-trained language models ([4.7](/4.7)); the representation of the same word is itself different in different contexts, and the disambiguation accuracy is far higher than that of naive Bayes, but the latter is still the best starting point for understanding the problem.

## Summary

| Concept | Formula | Key point |
|---|---|---|
| Posterior | $\mathbb{P}(h \mid D) \propto \mathbb{P}(D \mid h)\,\mathbb{P}(h)$ | When the prior is very small, the posterior can be small even under strong evidence |
| MAP hypothesis | $\arg\max_h \mathbb{P}(D \mid h)\,\mathbb{P}(h)$ | $-\log$ prior is the regularizer |
| ML hypothesis | $\arg\max_h \mathbb{P}(D \mid h)$ | Equivalent to least squares under normal noise |
| Bayes optimal classifier | $\arg\max_v \sum_h \mathbb{P}(v \mid x, h)\,\mathbb{P}(h \mid D)$ | Optimal on average, hard to compute |
| Gibbs algorithm | Draw one $h$ from the posterior to classify | Expected error at most twice as large |
| Naive Bayes | $\arg\max_v \mathbb{P}(v)\prod_i \mathbb{P}(a_i \mid v)$ | Conditional independence; log probabilities; Laplace smoothing = posterior mean under a Dirichlet prior |
