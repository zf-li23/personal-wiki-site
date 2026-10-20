---
title: Ensemble Learning
description: Why ensembles work (diversity and the bias–variance trade-off); weak learners; the weighted majority algorithm and its mistake bound; stacking; bagging, random forests and out-of-bag error; boosting, AdaBoost and its training error bound; gradient boosting, XGBoost, LightGBM and CatBoost.
source_hash: efbad6e32b1f
---

"Three cobblers with their wits combined equal Zhuge Liang," says a Chinese proverb. Ensemble learning combines the predictions of several learners to obtain a prediction that is more accurate and more stable than any one of them. It is one of the most effective techniques of classical machine learning: random forests and gradient boosted trees are still the methods of first choice for tabular data and have long topped data science competitions. This chapter first explains why ensembles work and then introduces four ways of combining: the weighted majority algorithm, which takes weighted votes of different algorithms on the same data; stacking, which uses another learner to learn how to combine; bagging and random forests, which train the same algorithm on bootstrap samples; and boosting, AdaBoost and gradient boosting, which attend sequentially to the "hard" examples. The base learner is often the **decision tree** of [4.5.6](/4.5.6); bagging builds on the **bootstrap** ([3.5.7](/3.5.7)), and the mechanism by which ensembles reduce error can be understood through the **bias–variance trade-off**; statistical methods for evaluating the effect of an ensemble are in [4.6.7](/4.6.7).

## 6.1. Introduction to Ensemble Learning

### 6.1.1. The Basic Idea

**Definition 6.1.1 (Ensemble Learning)** **Ensemble learning** trains several learners $h_1, \dots, h_T$ (called base learners or individual learners); for a new instance $x$, each learner makes its own prediction, and a combination strategy then merges $h_1(x), \dots, h_T(x)$ into the final prediction $H(x)$.

Combining is not always beneficial. Suppose three classifiers $h_1, h_2, h_3$ predict three examples as follows (✓ for correct, ✗ for wrong) and are combined by majority vote:

| | (a) Positive effect | | | (b) No effect | | | (c) Negative effect | | |
|---|---|---|---|---|---|---|---|---|---|
| | Ex. 1 | Ex. 2 | Ex. 3 | Ex. 1 | Ex. 2 | Ex. 3 | Ex. 1 | Ex. 2 | Ex. 3 |
| $h_1$ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ |
| $h_2$ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| $h_3$ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| Ensemble | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |

In case (a) each classifier has accuracy $2/3$ and the ensemble has accuracy $1$; in (b) the three classifiers are identical, so the ensemble brings no new information; in (c) each classifier has accuracy only $1/3$ and the ensemble has accuracy $0$. Individual learners must therefore be "accurate and diverse": not too poor in performance, and different from one another.

**Proposition 6.1.1** Let $T$ (odd) binary classifiers each have error rate $\varepsilon < 1/2$ and make independent errors. Then the error rate of the majority vote is

$$
\mathbb{P}(H(x) \ne y) = \sum_{k > T/2} \binom{T}{k}\varepsilon^k(1 - \varepsilon)^{T - k} \le \exp\!\Big(-2T\big(\tfrac12 - \varepsilon\big)^2\Big),
$$
which tends to 0 exponentially as $T \to \infty$.

**Proof** The number $K$ of classifiers that err satisfies $K \sim \mathrm{Bin}(T, \varepsilon)$ (the **binomial distribution**), and the majority vote errs if and only if $K > T/2$; this gives the equality. The inequality is Hoeffding's inequality $\mathbb{P}(K/T - \varepsilon \ge s) \le \mathrm{e}^{-2Ts^2}$ with $s = 1/2 - \varepsilon$. $\square$

For example, for $\varepsilon = 0.3$ the majority vote of 11 independent classifiers has error rate about $0.078$, and that of 21 about $0.026$. In reality the learners are trained on the same data and their errors are highly correlated, so such an effect is not attained; the core of ensemble methods is to create diversity in various ways: different algorithms (weighted majority, stacking), different training examples (bagging), different features (random forests), and different example weights (boosting).

### 6.1.2. Why Ensembles Work

Dietterich (2000) explains the effect of ensembles from three viewpoints. Let $\mathcal{H}$ be the **hypothesis space** of the learning algorithm and $f$ the true target concept.

1. Statistical: when the training sample is small and $\mathcal{H}$ is large, there are many hypotheses equally accurate on the training set, and any one of them chosen at random may perform poorly on the test set; averaging them reduces the risk of a bad choice.
2. Computational: learning algorithms (the greedy construction of a **decision tree**, gradient descent for a neural network) can only find local optima, and exhaustive search for the global optimum in $\mathcal{H}$ is too expensive; combining several local optima obtained from different starting points often comes closer to $f$ than any one of them.
3. Representational: $\mathcal{H}$ may not contain $f$ at all, but weighted combinations of several hypotheses enlarge the class of representable functions; for example, a combination of axis-parallel decision stumps can approximate an oblique or curved decision boundary.

Moreover, it is easy to find many "roughly correct" rules of thumb and hard to find a single highly accurate rule; an ensemble turns the former into the latter. From the viewpoint of the **bias–variance trade-off**, averaging mainly reduces variance:

**Proposition 6.1.2** Let $T$ predictions $Z_1, \dots, Z_T$ each have variance $\sigma^2$ and pairwise correlation $\rho$. Then

$$
\operatorname{Var}\Big(\frac1T\sum_{t=1}^T Z_t\Big) = \rho\sigma^2 + \frac{1 - \rho}{T}\sigma^2 .
$$

**Proof** We have $\operatorname{Var}\big(\sum_t Z_t\big) = \sum_t \operatorname{Var}(Z_t) + \sum_{s \ne t}\operatorname{Cov}(Z_s, Z_t) = T\sigma^2 + T(T-1)\rho\sigma^2$; dividing by $T^2$ gives the claim. $\square$

As $T$ grows the second term vanishes, and the variance has the lower bound $\rho\sigma^2$: to reduce the variance further, we must reduce the correlation among the individual learners. Averaging does not change the bias, so bagging and random forests suit learners with low bias and high variance (fully grown decision trees); boosting reduces the bias by correcting earlier mistakes sequentially and suits simple learners with high bias and low variance (decision stumps).

### 6.1.3. Weak Learners and Strong Learners

**Definition 6.1.2 (Weak Learner and Strong Learner)** For binary classification, a learning algorithm is called a **weak learner** if for every data distribution it outputs, with high probability, a hypothesis with error rate at most $1/2 - \gamma$ (for some fixed $\gamma > 0$), that is, only slightly better than random guessing; it is called a **strong learner** if for every $\varepsilon > 0$ it outputs, with high probability, a hypothesis with error rate at most $\varepsilon$.

Kearns and Valiant (1988) asked whether weak learnability is equivalent to strong learnability, that is, whether a weak learner can be "boosted" into a strong learner. Schapire (1990) answered in the affirmative by constructing the first polynomial-time boosting algorithm; Freund (1990) improved it; AdaBoost of Freund and Schapire (1995) does not need to know $\gamma$ in advance and has a large practical advantage, and later research developed the theory and the algorithms further.

### 6.1.4. Combination Strategies

| Strategy | Method | Applicable to |
|---|---|---|
| Simple averaging | $H(x) = \frac1T\sum_t h_t(x)$ | Regression, probability outputs |
| Weighted averaging | $H(x) = \sum_t w_t h_t(x)$, $w_t \ge 0$, $\sum_t w_t = 1$ | When the learners differ greatly in performance |
| Majority vote | The class with the most votes | Classification |
| Weighted vote | Count votes with weights $w_t$ | Classification |
| Soft voting | Average the class probabilities given by the learners and take the largest | Classifiers that output probabilities |
| Learned combination | Use another learner to learn how to combine | Stacking |

The methods in the following sections correspond to different sources of weights: the weighted majority algorithm adjusts the weights online, stacking learns the way of combining, bagging uses equal-weight votes, and boosting determines the weights from the error rate in each round.

## 6.2. The Weighted Majority Algorithm

The weighted majority algorithm (Littlestone and Warmuth, 1994) combines $n$ prediction algorithms from a pool $A = \{a_1, \dots, a_n\}$, which may be arbitrary learners or even fixed rules. The master algorithm maintains a weight $w_i$ for each $a_i$, votes according to the weights, and penalizes the algorithms that voted wrongly whenever it makes a mistake.

**Algorithm 6.2.1 (Weighted Majority Algorithm)** Let each $a_i$ output a value in $\{0, 1\}$ for input $x$, and let $\beta \in [0, 1)$ be the penalty factor.

1. Set $w_i \leftarrow 1$ for all $i$.
2. For each training example $\langle x, c(x)\rangle$:
   - compute $q_0 = \sum_{i : a_i(x) = 0} w_i$ and $q_1 = \sum_{i : a_i(x) = 1} w_i$; predict $c'(x) = 0$ if $q_0 > q_1$ and $c'(x) = 1$ otherwise (break ties arbitrarily when $q_0 = q_1$);
   - if $c'(x) \ne c(x)$, set $w_i \leftarrow \beta w_i$ for each algorithm with $a_i(x) \ne c(x)$.

For $\beta = 0$, an algorithm that errs is eliminated outright, which is the Halving algorithm: if the pool contains an algorithm that never errs, each mistake of the master algorithm eliminates at least half of the weight, so it makes at most $\log_2 n$ mistakes. Another common version penalizes every erring $a_i$ whether or not the master algorithm errs; the mistake bound below holds for both versions. The algorithm extends easily to multiclass outputs (accumulate weights for each class).

**Theorem 6.2.1 (Mistake Bound of the Weighted Majority Algorithm)** Suppose the best algorithm in the pool makes $m$ mistakes on the sequence of examples. Then the number $M$ of mistakes of the weighted majority algorithm satisfies

$$
M \le \frac{\log_2 n + m\log_2(1/\beta)}{\log_2\big(2/(1 + \beta)\big)} .
$$

**Proof** Let $W = \sum_i w_i$ be the total weight, initially $W = n$. Each time the master algorithm errs, the algorithms that voted wrongly carry total weight at least $W/2$, and all of it is multiplied by $\beta$, so the new total weight is at most

$$
\frac W2 + \beta\cdot\frac W2 = \frac{1 + \beta}{2}\,W .
$$
When the master algorithm does not err, $W$ does not increase. Hence after $M$ mistakes, $W \le n\big(\frac{1+\beta}2\big)^M$. On the other hand, the best algorithm is penalized at most $m$ times, so its weight is at least $\beta^m$, and this does not exceed $W$:

$$
\beta^m \le n\Big(\frac{1 + \beta}{2}\Big)^M .
$$
Taking logarithms to base 2 and rearranging gives the claim. $\square$

For $\beta = 1/2$ we get $M \le 2.41\,(m + \log_2 n)$: the number of mistakes of the master algorithm is at most a constant multiple of that of the best algorithm plus a term logarithmic in the size of the pool. No probabilistic assumption on the sequence of examples is made here; the sequence may even be constructed by an adversary, which makes this a typical result of "competing with the best expert" in online learning. Its continuous version (Hedge, the multiplicative weights update) is widely used in online learning, game theory and optimization.

## 6.3. Stacking

The weighted majority algorithm combines the algorithms by a fixed rule; stacking (Wolpert, 1992) treats the combination itself as a learning problem.

**Algorithm 6.3.1 (Stacking)** Given data $\{(x_i, y_i)\}_{i=1}^n$, $K$ base learners $M_1, \dots, M_K$ (identical or different) and a second-level learner (the meta-learner).

1. Generate the predictions of the base learners for every example by $k$-fold **cross-validation**: for each fold, train $M_1, \dots, M_K$ on the other folds and predict the $x_i$ in this fold, obtaining $z_i = (\hat y_{i1}, \dots, \hat y_{iK})$;
2. Train the second-level learner on the new data $\{(z_i, y_i)\}$;
3. Retrain $M_1, \dots, M_K$ on all the data. At prediction time, first obtain $z = (\hat y_1, \dots, \hat y_K)$ from the base learners, and then take the output of the second-level learner as the final prediction.

In step 1 we must not generate $z_i$ from base learners trained on $x_i$ itself: the resulting predictions would be too optimistic, and the second-level learner would favor the most overfitted base learner. Using the out-of-fold predictions obtained by cross-validation avoids this overfitting. The second-level learner is usually a simple model such as **logistic regression** or linear regression with nonnegative weights (Breiman, 1996); using the class probabilities output by the base learners works better than using class labels. Stacking can combine any methods, and the more the base learners differ (for example, tree models, linear models and **k-nearest neighbors**), the greater the gain tends to be.

## 6.4. Bagging and Random Forests

### 6.4.1. Bootstrap Sampling

If we have only one learning algorithm, how do we obtain several different learners? Training on different data gives different models. The naive approach is to split the training set into disjoint subsets and train one model on each, but every subset is too small and the models perform poorly. Bagging (Bootstrap AGGregatING, Breiman, 1996) instead generates the training sets with the **bootstrap** (Efron, 1979): from a training set $D$ of $m$ examples, draw $m$ times uniformly at random with replacement to obtain a **bootstrap sample** $D_t$.

**Proposition 6.4.1** The probability that a given example does not appear in a bootstrap sample is $(1 - 1/m)^m \to \mathrm{e}^{-1} \approx 0.368$ as $m \to \infty$. Hence each bootstrap sample contains on average about $63.2\%$ of the distinct examples.

For $m = 100$ the probability is already $0.366$. Bootstrap samples differ considerably from one another yet have the same size as the original training set, so the learners trained on them are different from one another and each is not too poor.

### 6.4.2. Bagging

**Definition 6.4.1 (Bagging)** For $t = 1, \dots, T$, **bagging** draws a bootstrap sample $D_t$ from the training set $S$ and trains a learner $H_t$ on $D_t$; for classification it takes an equal-weight majority vote of $H_1(x), \dots, H_T(x)$, and for regression the average.

The $H_t$ can be trained in parallel. Breiman held out $10\%$ of the training set as a test set on several data sets and compared the test error of a single decision tree with that of the majority vote of 50 bootstrap decision trees, averaged over 100 repetitions; bagging reduced the error substantially, while the same experiment with a k-nearest neighbor classifier gave almost no improvement. The reason is the stability of the learner: "if perturbing the learning set can cause significant changes in the predictor constructed, then bagging can improve accuracy" (Breiman, 1996). Decision trees, neural networks and subset selection in regression are unstable, since small differences in the training set produce very different hypotheses; k-nearest neighbors and linear regression are stable, the models on the bootstrap samples are almost identical, and averaging has no effect. This is consistent with Proposition 6.1.2: bagging reduces variance and helps little for a learner whose variance is already small.

In general, a larger $T$ is better but with diminishing returns: in Breiman's classification experiments the improvement is small beyond 25 bootstrap samples, and further increases mainly add computation; unlike boosting, increasing $T$ does not cause bagging to overfit.

### 6.4.3. Out-of-Bag Error

Each example is absent from about $36.8\%$ of the bootstrap samples, and the "out-of-bag" learners trained on those samples have not seen it, so they can be used to evaluate it without bias.

**Definition 6.4.2 (Out-of-Bag Error)** For each training example $x_i$, let only the learners $\{H_t : x_i \notin D_t\}$ whose training sets do not contain $x_i$ vote, which gives the out-of-bag prediction $H^{\mathrm{oob}}(x_i)$. The **out-of-bag error** is the error rate of the out-of-bag predictions over all training examples,

$$
\mathrm{err}_{\mathrm{oob}} = \frac1m\sum_{i=1}^m \boldsymbol{1}\{H^{\mathrm{oob}}(x_i) \ne y_i\} .
$$

The out-of-bag error is an estimate of the generalization error obtained for free during bagging; it plays a role similar to cross-validation and needs no separate validation set. For sufficiently large $T$ it is quite close to the estimate from the holdout method or cross-validation, with differences within the sampling error of the estimate itself ([4.6.7](/4.6.7)). It is also often used to select **hyperparameters**, such as the number of features a random forest considers at each split.

### 6.4.4. Random Forests

A random forest (Breiman, 2001) is bagging with **decision trees** as base learners, plus randomness in the features, which further reduces the correlation $\rho$ between trees.

**Algorithm 6.4.1 (Random Forest)** Let the training set have $n$ examples and $p$ features, and let the parameters be the number of trees $T$ and the number of features $k$ considered at each split.

1. For $t = 1, \dots, T$: draw a bootstrap sample of $n$ examples from the training set; grow a decision tree on it in which, at every node, $k$ features are first chosen at random from the $p$ features and the best split is sought only among these $k$ features; grow the tree fully, without pruning.
2. For classification, take a majority vote of the $T$ trees (for regression, the average).

The formulation in the lecture slides, "for each tree choose $k$ of the $p$ features at random to build the tree," describes the random subspace method (Ho, 1998); in Breiman's random forest the features are chosen anew at every node, which makes the trees differ more. The usual defaults are $k = \lfloor\sqrt p\rfloor$ for classification and $k = \lfloor p/3\rfloor$ for regression; for $k = p$ the method reduces to ordinary bagging. The smaller $k$ is, the weaker each tree but the less correlated the trees.

The advantages of random forests:

- they can learn interactions among features, and the randomness in the features alleviates overfitting;
- each split considers only some of the features, which makes high-dimensional data easy to handle;
- training can be parallelized, and the method is insensitive to **hyperparameters** and needs almost no tuning;
- through the way bootstrap samples are drawn (for example, oversampling the minority class) the errors on imbalanced data sets can be balanced to some extent;
- they give feature importances: first, the total impurity decrease contributed by each feature over all splits (MDI, which favors features with many values), and second, permutation importance, the increase in out-of-bag error after the values of a feature in the out-of-bag examples are randomly shuffled.

The drawbacks are that they still overfit when the noise is very large, and that a model of several hundred trees loses the interpretability of a single decision tree. Extremely randomized trees (Extra-Trees, Geurts et al., 2006) additionally choose the split threshold at random on the randomly selected features, which increases diversity further and speeds up training.

## 6.5. Boosting and AdaBoost

### 6.5.1. The Basic Idea

The learners of bagging are trained independently and know nothing of one another. Boosting lets learners "learn from failure" sequentially:

**Definition 6.5.1 (Boosting)** **Boosting** assigns a weight to each training example and iterates for $T$ rounds: in each round a weak learner $C_t$ is trained on the weighted examples, and then the weights of the examples misclassified by $C_t$ are increased and those of the correctly classified examples are decreased, so that the next round attends more to the "hard" examples; finally $C_1, \dots, C_T$ are combined with weights.

### 6.5.2. AdaBoost

AdaBoost (Adaptive Boosting, Freund and Schapire, 1995) is the best-known boosting algorithm. Below we use $y \in \{-1, +1\}$ for the labels of binary classification.

**Algorithm 6.5.1 (AdaBoost)** The input is a training set $\{(x_i, y_i)\}_{i=1}^N$, a weak learning algorithm and the number of rounds $T$.

1. Initialize the example weights $D_1(i) = 1/N$.
2. For $t = 1, \dots, T$:
   - train a weak learner under the weights $D_t$ to obtain $h_t\colon \mathcal{X} \to \{-1, +1\}$;
   - compute the weighted error rate $\varepsilon_t = \sum_{i : h_t(x_i) \ne y_i} D_t(i)$, the sum of the weights of all misclassified examples;
   - set $\alpha_t = \frac12\ln\frac{1 - \varepsilon_t}{\varepsilon_t}$;
   - update the weights: multiply correctly classified examples by $\mathrm{e}^{-\alpha_t}$ and misclassified ones by $\mathrm{e}^{\alpha_t}$, that is, $D_{t+1}(i) = D_t(i)\exp(-\alpha_t y_i h_t(x_i))/Z_t$, where $Z_t$ is the normalization factor making $\sum_i D_{t+1}(i) = 1$.
3. Output $H(x) = \operatorname{sgn}\big(F(x)\big)$ with $F(x) = \sum_{t=1}^T \alpha_t h_t(x)$.

For $\varepsilon_t < 1/2$ we have $\alpha_t > 0$, and the smaller the error rate, the larger the voting weight of $h_t$. After the weight update, the weighted error rate of $h_t$ under the new weights is exactly $1/2$ (the total weight of the misclassified examples changes from $\varepsilon_t$ to $\varepsilon_t \mathrm{e}^{\alpha_t}/Z_t = 1/2$), so the weak learner of the next round must learn something that $h_t$ has not learned.

The lecture slides also give the formulation of AdaBoost.M1: stop if $\varepsilon_t > 0.5$; let $\beta_t = \varepsilon_t/(1 - \varepsilon_t)$, multiply the weights of the correctly classified examples by $\beta_t$ and leave the misclassified ones unchanged, then normalize; the final voting weight is $\log(1/\beta_t)$. Since $\beta_t = \mathrm{e}^{-2\alpha_t}$, the normalized weights are exactly the same as in Algorithm 6.5.1, and the voting weight $\log(1/\beta_t) = 2\alpha_t$ differs only by a constant factor, so the two are the same algorithm. AdaBoost.M1 applies directly to multiclass problems but requires the error rate of every weak learner to be below $1/2$, a very strong requirement for multiclass problems; SAMME (Zhu et al., 2009) changes the weight to $\alpha_t = \ln\frac{1 - \varepsilon_t}{\varepsilon_t} + \ln(K - 1)$, which requires only that the weak learner be better than random guessing among $K$ classes, $1 - 1/K$, and is the algorithm of `AdaBoostClassifier` in scikit-learn.

**Example 6.5.1** The tutorial of Freund and Schapire has an example of 10 points in the plane in which the weak learners are horizontal or vertical lines (decision stumps). The weighted error rates and voting weights of the three rounds are about $\varepsilon_1 = 0.30$, $\alpha_1 = 0.42$; $\varepsilon_2 = 0.21$, $\alpha_2 = 0.65$; $\varepsilon_3 = 0.14$, $\alpha_3 = 0.92$. The final classifier $H = \operatorname{sgn}(0.42h_1 + 0.65h_2 + 0.92h_3)$ classifies all 10 points correctly, which no single line can do.

### 6.5.3. The Training Error Bound

**Theorem 6.5.1 (Training Error Bound of AdaBoost)** Let $\gamma_t = 1/2 - \varepsilon_t$. The training error rate of the output $H$ of AdaBoost satisfies

$$
\frac1N\sum_{i=1}^N \boldsymbol{1}\{H(x_i) \ne y_i\} \le \prod_{t=1}^T Z_t = \prod_{t=1}^T 2\sqrt{\varepsilon_t(1 - \varepsilon_t)} = \prod_{t=1}^T\sqrt{1 - 4\gamma_t^2} \le \exp\Big(-2\sum_{t=1}^T\gamma_t^2\Big).
$$
In particular, if $\gamma_t \ge \gamma > 0$ in every round, the training error rate is at most $\mathrm{e}^{-2T\gamma^2}$ and decreases exponentially in $T$.

**Proof** Unrolling the weight update $T$ times,

$$
D_{T+1}(i) = D_1(i)\prod_{t=1}^T\frac{\exp(-\alpha_t y_i h_t(x_i))}{Z_t} = \frac{\exp(-y_i F(x_i))}{N\prod_t Z_t} .
$$
If $H(x_i) \ne y_i$, then $y_i F(x_i) \le 0$ and $\exp(-y_i F(x_i)) \ge 1$; otherwise $\exp(-y_iF(x_i)) > 0$. Therefore $\boldsymbol{1}\{H(x_i) \ne y_i\} \le \exp(-y_i F(x_i))$; averaging over $i$ and using the identity above,

$$
\frac1N\sum_i\boldsymbol{1}\{H(x_i) \ne y_i\} \le \frac1N\sum_i\exp(-y_iF(x_i)) = \sum_i D_{T+1}(i)\prod_t Z_t = \prod_t Z_t .
$$
Next we compute $Z_t$: correctly classified examples contribute $\mathrm{e}^{-\alpha_t}$ times their weight and misclassified ones $\mathrm{e}^{\alpha_t}$ times,

$$
Z_t = (1 - \varepsilon_t)\mathrm{e}^{-\alpha_t} + \varepsilon_t\mathrm{e}^{\alpha_t} .
$$
Substituting $\mathrm{e}^{\alpha_t} = \sqrt{(1 - \varepsilon_t)/\varepsilon_t}$ gives $Z_t = 2\sqrt{\varepsilon_t(1 - \varepsilon_t)} = \sqrt{(1 - 2\gamma_t)(1 + 2\gamma_t)} = \sqrt{1 - 4\gamma_t^2}$. Finally, $1 + x \le \mathrm{e}^x$ gives $\sqrt{1 - 4\gamma_t^2} \le \sqrt{\mathrm{e}^{-4\gamma_t^2}} = \mathrm{e}^{-2\gamma_t^2}$. $\square$

The proof also shows where $\alpha_t$ comes from: $Z_t$ is a convex function of $\alpha_t$, and setting its derivative $-(1 - \varepsilon_t)\mathrm{e}^{-\alpha_t} + \varepsilon_t\mathrm{e}^{\alpha_t} = 0$ gives exactly $\alpha_t = \frac12\ln\frac{1 - \varepsilon_t}{\varepsilon_t}$. So in each round AdaBoost greedily minimizes the upper bound $\prod_t Z_t$ on the training error. By Theorem 6.5.1, when $T > \ln N/(2\gamma^2)$ the training error rate is below $1/N$, hence zero: as long as the weak learner of every round is slightly better than random guessing, AdaBoost classifies the training set perfectly. This answers affirmatively the question whether a weak learner can be boosted into a strong learner.

![AdaBoost with decision stumps learning a circular concept. Left: the decision regions after 200 rounds (the dashed line is the true boundary), assembled from axis-parallel segments. Right: the upper bound on the training error, the training error and the test error as functions of the number of rounds (log scale on the horizontal axis); after the training error reaches 0 the test error stays low](./plots/adaboost-error.py)

### 6.5.4. Exponential Loss and Margins

Friedman, Hastie and Tibshirani (2000) pointed out that AdaBoost fits the additive model $F(x) = \sum_t\alpha_t h_t(x)$ in a forward stagewise manner, minimizing the exponential loss

$$
L(y, F(x)) = \exp(-yF(x)) .
$$
At step $t$, with $F_{t-1}$ fixed, we minimize $\sum_i\exp\big(-y_i(F_{t-1}(x_i) + \alpha h(x_i))\big) = \sum_i w_i\exp(-\alpha y_i h(x_i))$, where $w_i = \exp(-y_iF_{t-1}(x_i)) \propto D_t(i)$: minimizing over $h$ means minimizing the weighted error rate under the weights $D_t$, and minimizing over $\alpha$ gives the $\alpha_t$ above. The population minimizer of the exponential loss is $F^*(x) = \frac12\ln\frac{\mathbb{P}(y = 1 \mid x)}{\mathbb{P}(y = -1 \mid x)}$, so $F$ can also be converted into class probabilities. This viewpoint connects boosting with additive models and **loss functions** in statistics and leads to the gradient boosting of the next section.

In experiments one often sees the test error continue to decrease after the training error has reached 0. Schapire et al. (1998) explain this by margins: the margin $y_iF(x_i)/\sum_t\alpha_t \in [-1, 1]$ of an example measures the confidence of the classification, further iterations increase the margins of the training examples, and the upper bound on the generalization error decreases as the margins increase.

The practical advantages of AdaBoost are that it is fast, simple and easy to implement; apart from the number of rounds $T$ it has almost no parameters to tune; it needs no prior knowledge about the weak learner and can be combined with any learner (neural networks, C4.5 decision trees, and so on); and it requires only that the weak learner be somewhat better than random guessing, which changed the way learning algorithms are designed. Its performance depends on the data and on the weak learner: a weak learner that is too complex overfits, whereas one that is too weak makes $\alpha_t$ tend quickly to 0, causing underfitting, or makes the margins so small that overfitting results. The exponential loss penalizes misclassified examples very heavily, and with much label noise the weights of the noisy examples grow larger and larger, so AdaBoost is sensitive to noise.

### 6.5.5. Reweighting and Resampling

Some learning methods cannot use example weights, and many common toolkits do not support weighted training sets. In that case we can resample instead of reweighting: draw from the training set with replacement according to the probabilities given by $D_t$ and train $h_t$ on the drawn sample. In general reweighting works better and resampling is easier to implement.

## 6.6. Gradient Boosting

### 6.6.1. Gradient Descent in Function Space

AdaBoost is a forward stagewise fit of the exponential loss. Friedman (2001) generalized the idea to an arbitrary differentiable loss $L(y, F)$: regard the values $(F(x_1), \dots, F(x_N))$ of $F$ on the training examples as variables and improve them step by step along the negative gradient of the loss, fitting the negative gradient with a regression tree at each step; this is **gradient descent** in function space.

**Algorithm 6.6.1 (Gradient Boosting)** The input is a training set, a differentiable loss $L$, the number of rounds $M$ and a learning rate $\nu \in (0, 1]$.

1. Initialize with the optimal constant $F_0(x) = \arg\min_c\sum_i L(y_i, c)$.
2. For $m = 1, \dots, M$:
   - compute the pseudo-residuals $r_{im} = -\left.\dfrac{\partial L(y_i, F)}{\partial F}\right|_{F = F_{m-1}(x_i)}$;
   - fit a regression tree to $\{(x_i, r_{im})\}$, obtaining the leaf regions $R_{1m}, \dots, R_{Jm}$;
   - for each leaf find the optimal value $c_{jm} = \arg\min_c\sum_{x_i \in R_{jm}} L(y_i, F_{m-1}(x_i) + c)$;
   - update $F_m(x) = F_{m-1}(x) + \nu\sum_{j=1}^J c_{jm}\boldsymbol{1}\{x \in R_{jm}\}$.
3. Output $F_M$.

For the squared loss $L = \frac12(y - F)^2$ the pseudo-residual is the ordinary residual $y_i - F_{m-1}(x_i)$, and each tree fits the part left unexplained by the previous trees. For binary classification with the log loss (logistic loss) the pseudo-residual is $y_i - p_i$, where $p_i$ is the probability of the positive class given by the current model. The smaller the learning rate $\nu$ (shrinkage, often $0.01$ to $0.1$), the more trees are needed and the better the generalization usually is; fitting each round on a random subset of the examples (stochastic gradient boosting, Friedman, 2002) both speeds up training and acts as regularization. Unlike bagging, gradient boosting overfits if the number of rounds is too large, and $M$ is usually determined by early stopping on a validation set.

### 6.6.2. XGBoost, LightGBM and CatBoost

The three mainstream implementations of gradient boosted decision trees (GBDT) each improve on the algorithm in different ways, all support parallel and GPU training, and are currently the most widely used models for tabular data.

- XGBoost (Chen and Guestrin, 2016) expands the loss to second order in a Taylor series and adds a regularization term for the complexity of the tree to the objective, $\Omega(f) = \gamma J + \frac12\lambda\sum_{j=1}^J w_j^2$ ($J$ is the number of leaves and $w_j$ the value of leaf $j$). Let $G_j$ and $H_j$ be the sums of the first and second derivatives over the examples in leaf $j$; then the optimal value is $w_j^* = -G_j/(H_j + \lambda)$, and the gain from splitting a node into a left and a right part is

  $$
  \frac12\left[\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}\right] - \gamma ,
  $$
  and a node is not split if the gain is negative. It can also learn automatically which branch missing values should follow.
- LightGBM (Ke et al., 2017) bins feature values into histograms to find split points, grows the tree leaf-wise (splitting the leaf with the largest gain) rather than level-wise, and reduces computation with gradient-based one-side sampling (GOSS, which keeps the examples with large gradients and samples those with small gradients) and exclusive feature bundling (EFB), which makes it fast on big data. The `HistGradientBoostingClassifier` of scikit-learn adopts a similar histogram algorithm.
- CatBoost (Prokhorenkova et al., 2018) uses ordered boosting to avoid the prediction shift caused by computing the gradient and fitting on the same example, and supports categorical features natively (ordered target statistics encoding); it gives very good results with default parameters.

On small and medium-sized tabular data, tuned gradient boosted trees usually still outperform deep neural networks (Grinsztajn et al., 2022); in recent years pretrained tabular foundation models (such as TabPFN, Hollmann et al., 2025) have become competitive with them on small data sets.

## 6.7. Comparing Bagging and Boosting

| | Bagging | Boosting |
|---|---|---|
| Training sets | Random sampling with replacement; the training sets of different rounds are independent | Depend on the result of the previous round; the rounds are not independent |
| Combination | Equal-weight vote or average | Weighted by error rate, with exponentially varying weights |
| Computation | Can be parallelized | Must proceed sequentially |
| Mainly reduces | Variance | Bias (and also variance) |
| Suitable base learners | Unstable, low bias (deep decision trees) | Weak, high bias (decision stumps, shallow trees) |
| Too many rounds | Does not overfit | May overfit; early stopping needed |
| Noisy data | Less affected | Performance may degrade markedly |

In practice bagging almost always helps; on average boosting does somewhat better than bagging but also more often hurts performance. For stable models bagging has little effect, whereas boosting may still be effective.

## 6.8. Practice

Below we use scikit-learn to compare a single **decision tree** with several ensemble methods (accuracy under 5-fold cross-validation), and to compare the out-of-bag estimate of a random forest with its accuracy on a held-out test set:

```python
from sklearn.datasets import make_classification
from sklearn.ensemble import (AdaBoostClassifier, BaggingClassifier, HistGradientBoostingClassifier,
                              RandomForestClassifier, StackingClassifier)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=2000, n_features=20, n_informative=8,
                           n_redundant=4, flip_y=0.05, random_state=0)
models = {
    "decision tree": DecisionTreeClassifier(random_state=0),
    "bagging (trees)": BaggingClassifier(DecisionTreeClassifier(), n_estimators=200, random_state=0),
    "random forest": RandomForestClassifier(n_estimators=200, random_state=0),
    "AdaBoost (stumps)": AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                                            n_estimators=200, random_state=0),
    "gradient boosting": HistGradientBoostingClassifier(random_state=0),
    "stacking": StackingClassifier(
        estimators=[("rf", RandomForestClassifier(n_estimators=200, random_state=0)),
                    ("knn", KNeighborsClassifier(n_neighbors=15))],
        final_estimator=LogisticRegression(), cv=5),
}
for name, model in models.items():
    acc = cross_val_score(model, X, y, cv=5)
    print(f"{name:18s} accuracy = {acc.mean():.3f} +- {acc.std():.3f}")

# out-of-bag estimate versus a held-out test set
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
rf = RandomForestClassifier(n_estimators=300, oob_score=True, random_state=0).fit(Xtr, ytr)
print(f"random forest: OOB accuracy {rf.oob_score_:.3f}, test accuracy {rf.score(Xte, yte):.3f}")
```

```text
decision tree      accuracy = 0.815 +- 0.011
bagging (trees)    accuracy = 0.895 +- 0.011
random forest      accuracy = 0.900 +- 0.014
AdaBoost (stumps)  accuracy = 0.882 +- 0.008
gradient boosting  accuracy = 0.907 +- 0.013
stacking           accuracy = 0.900 +- 0.012
random forest: OOB accuracy 0.892, test accuracy 0.917
```

The accuracy of a single decision tree is about $0.82$, and every ensemble method raises it to between $0.88$ and $0.91$, with gradient boosting the highest. The out-of-bag accuracy of the random forest differs from its accuracy on the 600 test examples by $0.025$, about twice the sampling error of the test accuracy (standard deviation about $\sqrt{0.9 \times 0.1/600} \approx 0.012$). Whether such differences suffice to show that one method is better than another must be judged with the tests of [4.6.7](/4.6.7).

## Summary

| Method | Source of diversity | Way of combining | Key points |
|---|---|---|---|
| Weighted majority | Different algorithms | Weighted vote; multiply by $\beta$ on mistakes | Mistakes $\le 2.41(m + \log_2 n)$ ($\beta = 1/2$) |
| Stacking | Different algorithms | Second-level learner | Train the second-level learner on out-of-fold predictions |
| Bagging | Bootstrap samples | Equal-weight vote or average | Reduces variance; out-of-bag error |
| Random forest | Bootstrap samples + random features at each node | Equal-weight vote or average | Reduces correlation among trees; feature importance |
| AdaBoost | Example weights | Weighted by $\alpha_t = \frac12\ln\frac{1-\varepsilon_t}{\varepsilon_t}$ | Training error $\le \exp(-2\sum_t\gamma_t^2)$; exponential loss |
| Gradient boosting | Fitting the negative gradient | Additive model, learning rate $\nu$ | Any differentiable loss; XGBoost, LightGBM, CatBoost |

The effect of an ensemble comes from individual learners that are accurate and diverse: bagging-type methods average out variance in parallel, and boosting-type methods correct bias sequentially.
