---
title: Factor Analysis
description: The orthogonal factor model and its covariance structure, non-identifiability and scale invariance, estimation of loadings by the principal component and maximum likelihood methods with a test for the number of factors, varimax rotation, factor scores by weighted least squares and regression, and a strategy for applications.
---

*Factor analysis* explains the correlations among many observed variables by a few unobservable variables called factors. Its roots are in psychometrics: K. Pearson and C. Spearman asked whether the scores of children in different school subjects, which are all positively correlated, could be explained by a single "general intelligence". The model has two aims, reduction (describe a $p\times p$ covariance matrix by far fewer parameters) and interpretation (explain the covariances by latent factors with a meaning). Factor analysis is closely related to the **principal component analysis** of [3.4.5](/3.4.5), which supplies one of its estimation methods, but the two differ in an essential way: principal components are linear combinations of the observed variables, whereas in factor analysis the observed variables are modeled as linear combinations of the factors plus errors, and the model is identified only up to a rotation. The chapter introduces the orthogonal factor model (Section 8.1), estimates its parameters at the population level by the principal component and maximum likelihood methods (Section 8.2), rotates the solution to make it interpretable (Section 8.3), estimates the factors of each unit at the unit level (Section 8.4), and ends with a strategy for applications (Section 8.5). It uses the **spectral decomposition** of [2.1](/2.1), the **multivariate normal distribution** and its conditional distributions ([3.4.2](/3.4.2)), the likelihood ratio test ([3.2.5](/3.2.5)) and the least squares of [3.4.7](/3.4.7); canonical correlation analysis in [3.4.9](/3.4.9) is the analogous method for two sets of variables.

## 8.1. The Orthogonal Factor Model

### 8.1.1. Motivation

**Example 8.1.1 (Exam Scores)** Two high-school students have the same total score $511$ in six subjects, but student A scores $98,97,93$ in mathematics, physics and chemistry and $73,70,80$ in history, politics and literature, while student B scores $75,71,80$ and $95,94,96$. The correlation matrix of the six subjects over all students shows two blocks: the correlations among the three science subjects are $0.35$–$0.44$, those among the three humanities subjects $0.46$–$0.61$, and those across the blocks only $0.16$–$0.32$. This suggests two latent abilities, a "science factor" $F_1$ and a "humanities factor" $F_2$, so that, for instance,

$$
\begin{bmatrix}X_1\\X_2\end{bmatrix}-\begin{bmatrix}50\\60\end{bmatrix}=\begin{bmatrix}0.8&0.2\\0.1&0.9\end{bmatrix}\begin{bmatrix}F_1\\F_2\end{bmatrix}+\begin{bmatrix}\varepsilon_1\\\varepsilon_2\end{bmatrix}
$$
for the mathematics score $X_1$ and the literature score $X_2$, where $\varepsilon_1$ and $\varepsilon_2$ are the parts specific to mathematics and to literature. Students A and B are then described by their values of $(F_1,F_2)$ rather than by six scores.

**Example 8.1.2 (Spearman, 1904)** Spearman observed the correlation matrix of children's scores in $X_1$ = classics, $X_2$ = French and $X_3$ = English,

$$
R=\begin{bmatrix}1&0.83&0.78\\0.83&1&0.67\\0.78&0.67&1\end{bmatrix},
$$
and proposed the one-factor model $X_i=l_iF+\varepsilon_i$, $i=1,2,3$, with a single common factor $F$ behind all three scores. Questionnaires such as the Big Five personality tests are modern descendants of this idea.

### 8.1.2. The Model

**Definition 8.1.1 (Orthogonal Factor Model)** Let the observable random vector $\boldsymbol{X}$ with $p$ components have mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$. The **orthogonal factor model** with $m$ common factors assumes

$$
\underset{(p\times1)}{\boldsymbol{X}-\boldsymbol{\mu}}=\underset{(p\times m)}{L}\ \underset{(m\times1)}{\boldsymbol{F}}+\underset{(p\times1)}{\boldsymbol{\varepsilon}},\qquad\text{i.e.}\qquad X_i-\mu_i=l_{i1}F_1+l_{i2}F_2+\cdots+l_{im}F_m+\varepsilon_i,\quad i=1,\dots,p,
$$
where $\boldsymbol{F}$ and $\boldsymbol{\varepsilon}$ are unobservable random vectors satisfying

$$
\mathbb{E}(\boldsymbol{F})=\boldsymbol{0},\quad\operatorname{Cov}(\boldsymbol{F})=\mathbb{E}(\boldsymbol{F}\boldsymbol{F}^{\mathsf T})=I_m,\qquad\mathbb{E}(\boldsymbol{\varepsilon})=\boldsymbol{0},\quad\operatorname{Cov}(\boldsymbol{\varepsilon})=\Psi=\operatorname{diag}(\psi_1,\dots,\psi_p),\qquad\operatorname{Cov}(\boldsymbol{\varepsilon},\boldsymbol{F})=\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T})=O.
$$
The components of $\boldsymbol{F}$ are the **common factors**, the components of $\boldsymbol{\varepsilon}$ are the **specific factors**, $l_{ij}$ is the **factor loading** of the $i$-th variable on the $j$-th factor, and $L=(l_{ij})$ is the matrix of factor loadings.

"Orthogonal" refers to the uncorrelated factors. Each specific factor $\varepsilon_i$ affects only $X_i$, and the specific factors are uncorrelated with each other and with the common factors, so all correlation between the observed variables must pass through the common factors. The model is linear in the factors, and the unknown parameters are $\boldsymbol{\mu}$, $L$ and $\Psi$.

### 8.1.3. The Implied Covariance Structure

Since $(\boldsymbol{X}-\boldsymbol{\mu})(\boldsymbol{X}-\boldsymbol{\mu})^{\mathsf T}=(L\boldsymbol{F}+\boldsymbol{\varepsilon})(L\boldsymbol{F}+\boldsymbol{\varepsilon})^{\mathsf T}=L\boldsymbol{F}\boldsymbol{F}^{\mathsf T}L^{\mathsf T}+\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T}L^{\mathsf T}+L\boldsymbol{F}\boldsymbol{\varepsilon}^{\mathsf T}+\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T}$, taking expectations gives

$$
\Sigma=\operatorname{Cov}(\boldsymbol{X})=L\,\mathbb{E}(\boldsymbol{F}\boldsymbol{F}^{\mathsf T})L^{\mathsf T}+\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{F}^{\mathsf T})L^{\mathsf T}+L\,\mathbb{E}(\boldsymbol{F}\boldsymbol{\varepsilon}^{\mathsf T})+\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T})=LL^{\mathsf T}+\Psi,
$$
and similarly $\operatorname{Cov}(\boldsymbol{X},\boldsymbol{F})=\mathbb{E}(\boldsymbol{X}-\boldsymbol{\mu})\boldsymbol{F}^{\mathsf T}=\mathbb{E}(L\boldsymbol{F}+\boldsymbol{\varepsilon})\boldsymbol{F}^{\mathsf T}=L$. Componentwise, with $\boldsymbol{l}_i^{\mathsf T}$ the $i$-th row of $L$,

$$
\sigma_{ii}=\underbrace{l_{i1}^2+l_{i2}^2+\cdots+l_{im}^2}_{h_i^2}+\psi_i,\qquad\sigma_{ik}=\operatorname{Cov}(X_i,X_k)=\boldsymbol{l}_i^{\mathsf T}\boldsymbol{l}_k=l_{i1}l_{k1}+\cdots+l_{im}l_{km}\ (i\ne k),\qquad\operatorname{Cov}(X_i,F_j)=l_{ij}.
$$
The variance of $X_i$ thus splits into the *communality* $h_i^2=\sum_jl_{ij}^2$, the part explained by the common factors, and the *specific variance* $\psi_i$. The covariances are produced entirely by the loadings, and the loading $l_{ij}$ is the covariance of $X_i$ with $F_j$ (the correlation, if $X_i$ is standardized).

**Example 8.1.3** The covariance matrix

$$
\Sigma=\begin{bmatrix}19&30&2&12\\30&57&5&23\\2&5&38&47\\12&23&47&68\end{bmatrix}=\begin{bmatrix}4&1\\7&2\\-1&6\\1&8\end{bmatrix}\begin{bmatrix}4&7&-1&1\\1&2&6&8\end{bmatrix}+\begin{bmatrix}2&0&0&0\\0&4&0&0\\0&0&1&0\\0&0&0&3\end{bmatrix}
$$
has the form $LL^{\mathsf T}+\Psi$ with $m=2$. For the first variable, $\sigma_{11}=19=h_1^2+\psi_1$ with communality $h_1^2=l_{11}^2+l_{12}^2=4^2+1^2=17$ and specific variance $\psi_1=2$.

There is a useful geometric picture. For centered random variables with finite variance, $\langle U,W\rangle=\mathbb{E}(UW)$ is an inner product, in which the length of $U$ is its standard deviation and the cosine of the angle between $U$ and $W$ is their correlation. In this space $F_1,\dots,F_m$ form an orthonormal system, and $X_i-\mu_i=\tilde X_i+\varepsilon_i$ with $\tilde X_i=l_{i1}F_1+\cdots+l_{im}F_m$ in the span of the factors and $\varepsilon_i$ orthogonal to it and to every other $\varepsilon_k$. The loadings $l_{ij}=\langle X_i,F_j\rangle$ are the coordinates of $\tilde X_i$ in the factor basis, $h_i^2=\|\tilde X_i\|^2$, and $\psi_i=\|\varepsilon_i\|^2$.

### 8.1.4. Reduction, Non-Identifiability and Scale Invariance

*Reduction.* A covariance matrix has $p(p+1)/2$ free parameters, while $LL^{\mathsf T}+\Psi$ has $pm+p$. For $p=12$ and $m=2$ this is $36$ instead of $78$. The model is useful only when $m$ is much smaller than $p$, and it has a real limitation: not every covariance matrix can be factored as $LL^{\mathsf T}+\Psi$ with $m\ll p$. Even when a factorization exists mathematically, it may be statistically meaningless. If $\sigma_{11}$ in Example 8.1.3 were $15$ instead of $19$ (still a valid covariance matrix), the same $L$ would force $\psi_1=15-17=-2<0$. For the correlation matrix

$$
R=\begin{bmatrix}1&0.9&0.7\\0.9&1&0.4\\0.7&0.4&1\end{bmatrix}
$$
and $m=1$, the equations $l_1l_2=0.9$, $l_1l_3=0.7$, $l_2l_3=0.4$ give $l_1^2=0.9\cdot0.7/0.4=1.575$, so $\operatorname{Corr}(X_1,F)=l_1=1.255>1$ and $\psi_1=1-1.575=-0.575<0$. A solution with a negative specific variance (or a zero one) is called a *Heywood case* (H. B. Heywood, 1931).

*Non-identifiability.* Let $T$ be any $m\times m$ **orthogonal matrix**. Then

$$
\boldsymbol{X}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}=LTT^{\mathsf T}\boldsymbol{F}+\boldsymbol{\varepsilon}=L^*\boldsymbol{F}^*+\boldsymbol{\varepsilon},\qquad L^*=LT,\quad\boldsymbol{F}^*=T^{\mathsf T}\boldsymbol{F},
$$
and $\boldsymbol{F}^*$ satisfies the model assumptions: $\mathbb{E}\boldsymbol{F}^*=\boldsymbol{0}$, $\operatorname{Cov}(\boldsymbol{F}^*)=T^{\mathsf T}T=I_m$, $\operatorname{Cov}(\boldsymbol{\varepsilon},\boldsymbol{F}^*)=O$. Moreover $L^*L^{*\mathsf T}=LL^{\mathsf T}$, so $\Sigma$ cannot distinguish $L$ from $LT$: the loadings are determined only up to an orthogonal transformation. This freedom, removing $m(m-1)/2$ parameters from the count above, is used in two ways: to rotate the factors so that they become interpretable (Section 8.3), and to impose a convenient constraint that makes maximum likelihood estimation well defined (Section 8.2.2).

*Scale invariance.* Let $C=\operatorname{diag}(c_1,\dots,c_p)$ with $c_i\ne0$ and $\boldsymbol{Y}=C\boldsymbol{X}$ (a change of units). Then

$$
\boldsymbol{Y}=C\boldsymbol{\mu}+CL\boldsymbol{F}+C\boldsymbol{\varepsilon}=\boldsymbol{\mu}_C+L_C\boldsymbol{F}+\boldsymbol{\varepsilon}_C,
$$
and $\operatorname{Cov}(\boldsymbol{\varepsilon}_C)=C\Psi C$ is still diagonal because $C$ is diagonal. Thus $\boldsymbol{Y}$ follows an $m$-factor model with the same factors: factor analysis is unaffected by rescaling of the variables. In particular, for the standardized variables $\boldsymbol{Z}=V^{-1/2}(\boldsymbol{X}-\boldsymbol{\mu})$ with $V=\operatorname{diag}(\sigma_{11},\dots,\sigma_{pp})$,

$$
\boldsymbol{Z}=L_z\boldsymbol{F}+\boldsymbol{\varepsilon}_z,\qquad L_z=V^{-1/2}L,\qquad\Psi_z=V^{-1/2}\Psi V^{-1/2},\qquad\rho=L_zL_z^{\mathsf T}+\Psi_z,
$$
where $\rho$ is the correlation matrix of $\boldsymbol{X}$. Principal components have no such invariance ([3.4.5](/3.4.5)).

### 8.1.5. Population Level and Unit Level

Suppose $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$ are $n$ independent observations from a $p$-dimensional population with unknown $\boldsymbol{\mu}$ and $\Sigma$, summarized by the **sample covariance matrix** $S$ or the **sample correlation matrix** $R$. Factor analysis has two goals at different levels.

- *Population level*: given $m$, find $\hat L$ and $\hat\Psi$ with $S\approx\hat L\hat L^{\mathsf T}+\hat\Psi$ (Section 8.2), and give the factors a meaning through the loadings, after a suitable rotation (Section 8.3). These parameters describe a regularity shared by all units.
- *Unit level*: given $\hat L$ and $\hat\Psi$, estimate the value of the factors for each unit, the factor scores (Section 8.4).

For example, if $n=100$ students are observed in $p=6$ subjects and $m=2$, the $6\times2$ matrix $L$ and the diagonal $6\times6$ matrix $\Psi$ say that a common "science factor" and a common "humanities factor" influence all the scores, with the same strengths (loadings) for every student; if the model is right, another sample of students should show the same pattern. Each student, however, has individual factor values, for instance $(0.3,1.5)$ for a student strong in humanities and $(1.2,0.4)$ for one strong in science.

## 8.2. Estimating the Loadings

### 8.2.1. The Principal Component Method

By the spectral decomposition, $\Sigma=\sum_{i=1}^p\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}$ with eigenvalues $\lambda_1\ge\cdots\ge\lambda_p\ge0$ and orthonormal eigenvectors $\boldsymbol{e}_i$, that is,

$$
\Sigma=\begin{bmatrix}\sqrt{\lambda_1}\boldsymbol{e}_1&\sqrt{\lambda_2}\boldsymbol{e}_2&\cdots&\sqrt{\lambda_p}\boldsymbol{e}_p\end{bmatrix}\begin{bmatrix}\sqrt{\lambda_1}\boldsymbol{e}_1^{\mathsf T}\\\vdots\\\sqrt{\lambda_p}\boldsymbol{e}_p^{\mathsf T}\end{bmatrix}=L_0L_0^{\mathsf T}+O.
$$
This is an exact factorization, but a useless one: it has as many common factors as variables and no specific variance. When the last $p-m$ eigenvalues are small, we neglect their contribution, $\Sigma\approx\sum_{i=1}^m\lambda_i\boldsymbol{e}_i\boldsymbol{e}_i^{\mathsf T}=LL^{\mathsf T}$ with a $p\times m$ matrix $L$, and let the diagonal of the remainder be the specific variances.

**Definition 8.2.1 (Principal Component Method)** Let $(\hat\lambda_1,\hat{\boldsymbol{e}}_1),\dots,(\hat\lambda_p,\hat{\boldsymbol{e}}_p)$ be the eigenpairs of $S$ (or of $R$), $\hat\lambda_1\ge\cdots\ge\hat\lambda_p$. The **principal component method** estimates the loadings and specific variances by

$$
\tilde L=\begin{bmatrix}\sqrt{\hat\lambda_1}\,\hat{\boldsymbol{e}}_1&\sqrt{\hat\lambda_2}\,\hat{\boldsymbol{e}}_2&\cdots&\sqrt{\hat\lambda_m}\,\hat{\boldsymbol{e}}_m\end{bmatrix},\qquad\tilde\Psi=\operatorname{diag}\big(S-\tilde L\tilde L^{\mathsf T}\big),\quad\text{i.e.}\quad\tilde\psi_i=s_{ii}-\sum_{j=1}^m\tilde l_{ij}^2,
$$
and the communalities by $\tilde h_i^2=\tilde l_{i1}^2+\cdots+\tilde l_{im}^2$.

By construction the diagonal of $S$ is reproduced exactly, but the off-diagonal entries of the residual matrix $S-(\tilde L\tilde L^{\mathsf T}+\tilde\Psi)$ are in general not zero. The columns of $\tilde L$ do not depend on $m$: increasing the number of factors adds columns but leaves the existing ones unchanged.

**Example 8.2.1** Take the matrix of Example 8.1.3 as a sample covariance matrix $S$. Its eigenvalues are $116.27$, $61.42$, $2.52$, $1.80$, and (up to the signs of the columns, numbers rounded)

| $m$ | $\tilde L$ (rows = variables) | $\operatorname{diag}(\tilde\Psi)$ |
|---|---|---|
| $1$ | $(-2.5),(-4.8),(-5.1),(-7.8)$ | $12.6,\ 34.4,\ 12.2,\ 6.5$ |
| $2$ | $(-2.5,3.3),(-4.8,5.8),(-5.1,-3.3),(-7.8,-2.4)$ | $1.9,\ 0.6,\ 1.1,\ 0.7$ |
| $3$ | add the third column $(1.3,-0.8,-0.3,0.2)$ | $0.1,\ 0.0,\ 1.0,\ 0.6$ |

With $m=2$ the off-diagonal residuals are at most $1.05$ in absolute value, and $S\approx\tilde L\tilde L^{\mathsf T}+\tilde\Psi$ reproduces $S$ well; with $m=1$ the residuals are as large as $19$. Note that the estimated $\tilde L$ and $\tilde\Psi$ differ from the $L$ and $\Psi$ used to construct $S$ in Example 8.1.3, although both reproduce $S$ well: the loadings are not unique, and the principal component method tends to attribute too much variance to the common factors.

How many factors should be used? As in PCA, the residual matrix measures the quality of the approximation.

**Proposition 8.2.1** For the principal component solution,

$$
\sum_{i,k}\Big[S-\big(\tilde L\tilde L^{\mathsf T}+\tilde\Psi\big)\Big]_{ik}^2\le\hat\lambda_{m+1}^2+\cdots+\hat\lambda_p^2.
$$

**Proof** $S-\tilde L\tilde L^{\mathsf T}=\sum_{i>m}\hat\lambda_i\hat{\boldsymbol{e}}_i\hat{\boldsymbol{e}}_i^{\mathsf T}$ has squared **Frobenius norm** $\sum_{i>m}\hat\lambda_i^2$. Subtracting $\tilde\Psi$ sets its diagonal to zero and leaves the off-diagonal entries unchanged, which can only decrease the sum of squares. $\square$

So a small sum of squares of the neglected eigenvalues implies a small sum of squared approximation errors (in Example 8.2.1 with $m=2$: $3.9\le\hat\lambda_3^2+\hat\lambda_4^2=9.6$). Another view uses explained variance. The total sample variance is $\operatorname{tr}(S)=s_{11}+\cdots+s_{pp}$, and the contribution of the $j$-th common factor is $\tilde l_{1j}^2+\cdots+\tilde l_{pj}^2=\hat\lambda_j\|\hat{\boldsymbol{e}}_j\|^2=\hat\lambda_j$, so the proportion of the total variance explained by the $m$ common factors is

$$
\frac{\hat\lambda_1+\cdots+\hat\lambda_m}{\operatorname{tr}(S)}\qquad\Big(\text{or }\frac{\hat\lambda_1+\cdots+\hat\lambda_m}{p}\text{ for }R\Big).
$$
In Example 8.2.1 this is $(116.27+61.42)/182=0.976$ for $m=2$. The rules for choosing the number of principal components (cumulative proportion, scree plot, eigenvalues of $R$ larger than $1$) therefore carry over.

**Example 8.2.2 (Consumer Preference)** In a consumer-preference study, a sample of customers rated a new food product on five attributes. The sample correlation matrix is

$$
R=\begin{bmatrix}1&0.02&0.96&0.42&0.01\\0.02&1&0.13&0.71&0.85\\0.96&0.13&1&0.50&0.11\\0.42&0.71&0.50&1&0.79\\0.01&0.85&0.11&0.79&1\end{bmatrix}
$$
for (taste, good buy for money, flavor, suitable for snack, provides lots of energy). Only two eigenvalues of $R$, $2.85$ and $1.81$, exceed $1$, and together they account for $93.2\%$ of the total standardized variance, so we choose $m=2$. The principal component solution is

| variable | $\tilde l_{i1}$ | $\tilde l_{i2}$ | $\tilde h_i^2$ | $\tilde\psi_i$ |
|---|---|---|---|---|
| taste | $0.56$ | $0.82$ | $0.98$ | $0.02$ |
| good buy for money | $0.78$ | $-0.53$ | $0.88$ | $0.12$ |
| flavor | $0.65$ | $0.75$ | $0.98$ | $0.02$ |
| suitable for snack | $0.94$ | $-0.10$ | $0.89$ | $0.11$ |
| provides lots of energy | $0.80$ | $-0.54$ | $0.93$ | $0.07$ |
| eigenvalue | $2.85$ | $1.81$ | | |
| cumulative proportion | $0.571$ | $0.932$ | | |

The communalities are high, so the two factors explain the five ratings well; the meaning of the factors is not yet clear, and Section 8.3 returns to this example.

### 8.2.2. The Maximum Likelihood Method

The principal component method makes no distributional assumption. If the common and specific factors are jointly normal, the parameters can be estimated by maximum likelihood.

Assume $\boldsymbol{F}\sim\mathcal{N}_m(\boldsymbol{0},I_m)$ and $\boldsymbol{\varepsilon}\sim\mathcal{N}_p(\boldsymbol{0},\Psi)$, independent. Then $\boldsymbol{X}\sim\mathcal{N}_p(\boldsymbol{\mu},\Sigma)$ with $\Sigma=LL^{\mathsf T}+\Psi$, and the likelihood of the sample is

$$
\begin{aligned}
L(\boldsymbol{\mu},\Sigma)&=(2\pi)^{-\frac{np}{2}}\lvert\Sigma\rvert^{-\frac n2}\exp\Big\{-\frac12\operatorname{tr}\Big[\Sigma^{-1}\Big(\sum_{j=1}^n(\boldsymbol{x}_j-\bar{\boldsymbol{x}})(\boldsymbol{x}_j-\bar{\boldsymbol{x}})^{\mathsf T}+n(\bar{\boldsymbol{x}}-\boldsymbol{\mu})(\bar{\boldsymbol{x}}-\boldsymbol{\mu})^{\mathsf T}\Big)\Big]\Big\}\\
&=(2\pi)^{-\frac{(n-1)p}{2}}\lvert\Sigma\rvert^{-\frac{n-1}{2}}\exp\Big\{-\frac12\operatorname{tr}\Big[\Sigma^{-1}\sum_{j=1}^n(\boldsymbol{x}_j-\bar{\boldsymbol{x}})(\boldsymbol{x}_j-\bar{\boldsymbol{x}})^{\mathsf T}\Big]\Big\}\times(2\pi)^{-\frac p2}\lvert\Sigma\rvert^{-\frac12}\exp\Big\{-\frac n2(\bar{\boldsymbol{x}}-\boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\bar{\boldsymbol{x}}-\boldsymbol{\mu})\Big\}.
\end{aligned}
$$
It depends on $L$ and $\Psi$ only through $\Sigma=LL^{\mathsf T}+\Psi$, so by non-identifiability the maximizer $L$ is not unique. One imposes the computationally convenient uniqueness condition

$$
L^{\mathsf T}\Psi^{-1}L=\Delta,\qquad\Delta\text{ a diagonal matrix}.
$$

The condition is always attainable and picks one representative of each class of equivalent loadings. Call $L_1$ and $L_2$ equivalent if $L_1=L_2P$ for an orthogonal $P$; equivalent loadings give the same $\Sigma$, and the likelihood cannot separate them. For any $L_1$, the symmetric matrix $B=L_1^{\mathsf T}\Psi^{-1}L_1$ has a spectral decomposition $B=P\Delta P^{\mathsf T}$, and $L_0=L_1P$ is equivalent to $L_1$ with $L_0^{\mathsf T}\Psi^{-1}L_0=P^{\mathsf T}BP=\Delta$ diagonal. When the diagonal entries of $\Delta$ are distinct, $L_0$ is unique up to the signs of its columns. The maximization is carried out numerically (by iterative algorithms or the EM algorithm of [3.5](/3.5)).

**Theorem 8.2.1** Let $\boldsymbol{X}_1,\dots,\boldsymbol{X}_n$ be a random sample from $\mathcal{N}_p(\boldsymbol{\mu},\Sigma)$, where $\Sigma=LL^{\mathsf T}+\Psi$ is the covariance matrix of the $m$-factor model, and let $\hat L$, $\hat\Psi$ and $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$ be the maximum likelihood estimators subject to $\hat L^{\mathsf T}\hat\Psi^{-1}\hat L$ being diagonal. Then the maximum likelihood estimators of the communalities are

$$
\hat h_i^2=\hat l_{i1}^2+\hat l_{i2}^2+\cdots+\hat l_{im}^2,\qquad i=1,\dots,p,
$$
and the proportion of the total sample variance due to the $j$-th factor is

$$
\frac{\hat l_{1j}^2+\hat l_{2j}^2+\cdots+\hat l_{pj}^2}{s_{11}+s_{22}+\cdots+s_{pp}}.
$$

The first statement follows from the invariance of maximum likelihood estimators ([3.2.3](/3.2.3)); the second is then a definition. By the same invariance and the scale invariance of the model, the estimates for the standardized variables are obtained directly from those for the original variables:

$$
\hat L_z=\hat V^{-1/2}\hat L,\qquad\hat\Psi_z=\hat V^{-1/2}\hat\Psi\hat V^{-1/2},\qquad\hat V=\operatorname{diag}(\hat\sigma_{11},\dots,\hat\sigma_{pp}),
$$
so maximum likelihood factor analysis of $S$ and of $R$ are equivalent. For $R$, the proportion due to factor $j$ is $(\hat l_{1j}^2+\cdots+\hat l_{pj}^2)/p$ with the standardized loadings.

**Example 8.2.3 (Stock Prices)** The weekly rates of return of five stocks (JPMorgan, Citibank, Wells Fargo, Royal Dutch Shell, ExxonMobil) were recorded for $n=103$ weeks. A two-factor model for the sample correlation matrix gives

| variable | ML $\hat l_{i1}$ | ML $\hat l_{i2}$ | ML $\hat\psi_i$ | PC $\tilde l_{i1}$ | PC $\tilde l_{i2}$ | PC $\tilde\psi_i$ |
|---|---|---|---|---|---|---|
| JPMorgan | $0.115$ | $0.755$ | $0.42$ | $0.732$ | $-0.437$ | $0.27$ |
| Citibank | $0.322$ | $0.788$ | $0.27$ | $0.831$ | $-0.280$ | $0.23$ |
| Wells Fargo | $0.182$ | $0.652$ | $0.54$ | $0.726$ | $-0.374$ | $0.33$ |
| Royal Dutch Shell | $1.000$ | $-0.000$ | $0.00$ | $0.605$ | $0.694$ | $0.15$ |
| ExxonMobil | $0.683$ | $-0.032$ | $0.53$ | $0.563$ | $0.719$ | $0.17$ |
| cumulative proportion | $0.323$ | $0.647$ | | $0.487$ | $0.769$ | |

The principal component solution has a general "market factor" $F_1$, on which all stocks load about equally, and a contrast $F_2$ between the oil stocks and the banks (an "industry factor"). The maximum likelihood solution has an oil factor and a bank factor; its estimate $\hat\psi_4=0.00$ for Shell lies on the boundary, a Heywood case. The columns of $\tilde L$ are orthogonal (they are scaled eigenvectors), those of $\hat L$ need not be; the principal component method gives smaller specific variances and a larger proportion of explained variance, since it is designed to maximize the explained variance. (R's `factanal` reports slightly different maximum likelihood values, e.g. loadings $0.121$, $0.754$ for JPMorgan and specific variances $0.417,0.275,0.542,0.005,0.530$.)

### 8.2.3. A Large-Sample Test for the Number of Common Factors

Under normality, the adequacy of $m$ factors can be tested:

$$
H_0\colon\underset{(p\times p)}{\Sigma}=\underset{(p\times m)}{L}\ \underset{(m\times p)}{L^{\mathsf T}}+\underset{(p\times p)}{\Psi}\ \ \text{(with }L^{\mathsf T}\Psi^{-1}L=\Delta\text{ diagonal)}\qquad\text{vs.}\qquad H_1\colon\Sigma\text{ is any other positive definite matrix}.
$$
Under $H_1$ the maximum likelihood estimates are $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$ and $\hat\Sigma=S_n=\frac{n-1}{n}S$, with maximized likelihood proportional to $\lvert S_n\rvert^{-n/2}\mathrm{e}^{-np/2}$; under $H_0$ they are $\bar{\boldsymbol{x}}$ and $\hat\Sigma=\hat L\hat L^{\mathsf T}+\hat\Psi$, with maximized likelihood proportional to $\lvert\hat L\hat L^{\mathsf T}+\hat\Psi\rvert^{-n/2}\exp\big\{-\frac n2\operatorname{tr}\big[(\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}S_n\big]\big\}$. The **likelihood ratio test** statistic is

$$
-2\ln\Lambda=-2\ln\frac{\text{maximized likelihood under }H_0}{\text{maximized likelihood}}=n\ln\frac{\lvert\hat L\hat L^{\mathsf T}+\hat\Psi\rvert}{\lvert S_n\rvert}+n\Big[\operatorname{tr}\big((\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}S_n\big)-p\Big],
$$
and the trace term vanishes at the maximum likelihood estimates. By **Wilks' theorem** it is approximately $\chi^2_{\nu-\nu_0}$ for large $n$, where the degrees of freedom are the difference in the number of free parameters:

- under $H_1$: $\nu=p(p+1)/2$;
- under $H_0$: $p(m+1)$ parameters in $L$ and $\Psi$, minus $m(m-1)/2$ equations imposed by the constraint (each off-diagonal entry of the symmetric $m\times m$ matrix $L^{\mathsf T}\Psi^{-1}L$ must vanish), so $\nu_0=p(m+1)-m(m-1)/2$;

$$
\nu-\nu_0=\frac12p(p+1)-p(m+1)+\frac12m(m-1)=\frac12\big[(p-m)^2-p-m\big].
$$
The test requires $\nu-\nu_0>0$, which bounds the number of factors that can be tested. Bartlett's correction, which replaces $n$ by $n-1-(2p+4m+5)/6$, improves the chi-square approximation and is used by standard software.

**Example 8.2.4 (Stock Prices, Continued)** For $p=5$, the test of $m=2$ has $\frac12[(5-2)^2-7]=1$ degree of freedom; R's `factanal` reports $\chi^2=1.97$ and $p$-value $0.16$, so two factors are sufficient. For $m=1$ there are $\frac12[16-6]=5$ degrees of freedom and $\chi^2=62.22$ with $p$-value $4.2\times10^{-12}$: one factor is clearly not enough.

### 8.2.4. Comparing the Two Methods

| | principal component method | maximum likelihood method |
|---|---|---|
| assumptions | none beyond the model | joint normality of $\boldsymbol{F}$ and $\boldsymbol{\varepsilon}$ |
| uniqueness | columns of $\tilde L$ orthogonal (from the eigenvectors) | $L^{\mathsf T}\Psi^{-1}L$ diagonal |
| computation | explicit; solutions nested in $m$ | iterative optimization |
| covariance or correlation | different results for $S$ and $R$ | results for $S$ and $R$ convertible into each other |
| choice of $m$ | as in PCA (proportion, eigenvalues of $R$ above $1$) | likelihood ratio test |
| drawbacks | $\tilde\Psi$ obtained as a remainder; off-diagonal fit not optimized | relies on normality; Heywood cases possible |

In practice both are computed and compared (Section 8.5).

## 8.3. Factor Rotation

### 8.3.1. Why Rotate?

Any $\hat L^*=\hat LT$ with an orthogonal $T$ is an equally good estimate. Rotation is not possible in PCA, because there the components are defined by maximizing variances one after another, which fixes their directions; in factor analysis only the span of the factors is determined. What does rotation change?

- Unchanged: the estimated covariance matrix $\hat L^*\hat L^{*\mathsf T}+\hat\Psi=\hat L\hat L^{\mathsf T}+\hat\Psi$, the residual matrix, the specific variances $\hat\psi_i$, and the communalities $\hat h_i^2$ (the rows of $\hat L$ keep their lengths), hence also the total proportion of variance explained by the $m$ factors.
- Changed: the individual loadings, the proportion of variance attributed to each factor, and hence the interpretation of the factors.

The purpose of rotation is interpretation. Ideally each variable loads highly on a single factor and has small to moderate loadings on the others. In Example 8.2.2, the pattern

| | taste | good buy | flavor | snack | energy |
|---|---|---|---|---|---|
| $F_1^*$ | $1$ | $0$ | $1$ | $0$ | $0$ |
| $F_2^*$ | $0$ | $1$ | $0$ | $1$ | $1$ |

would give a clean "taste" factor and a clean "nutrition" factor, whereas the unrotated loadings mix them.

### 8.3.2. The Varimax Criterion

**Definition 8.3.1 (Varimax Rotation)** Let $\hat l_{ij}^*$ be the rotated loadings and $\tilde l_{ij}^*=\hat l_{ij}^*/\hat h_i$ the loadings scaled by the square roots of the communalities. The **varimax rotation** chooses, among all orthogonal matrices $T$, the one that maximizes

$$
V=\frac1p\sum_{j=1}^m\Big[\sum_{i=1}^p\big(\tilde l_{ij}^*\big)^4-\frac1p\Big(\sum_{i=1}^p\big(\tilde l_{ij}^*\big)^2\Big)^2\Big]
$$
and then multiplies the rotated scaled loadings back by $\hat h_i$.

Three ideas lie behind the criterion. The importance of a loading depends on its magnitude, not its sign, so the criterion works with squares $(\tilde l_{ij}^*)^2$. The scaling by $\hat h_i$ gives variables with small communalities the same weight as variables with large ones. Finally, $V$ is proportional to $\sum_{j=1}^m$ (variance of the squared scaled loadings in column $j$), so maximizing $V$ spreads out the squares of the loadings on each factor as much as possible, pushing them toward $0$ or $\pm1$. The maximization must be restricted to orthogonal $T$; over arbitrary matrices it would be meaningless. In two dimensions, $T$ is a rotation by an angle $\phi$ (possibly combined with a reflection), and $V(\phi)$ can be maximized directly.

**Example 8.3.1 (Consumer Preference, Continued)** The varimax rotation of the principal component loadings of Example 8.2.2 is a rotation of the factor axes by about $33^\circ$:

| variable | $\tilde l_{i1}^*$ | $\tilde l_{i2}^*$ | $\tilde h_i^2$ |
|---|---|---|---|
| taste | $0.02$ | $0.99$ | $0.98$ |
| good buy for money | $0.94$ | $-0.01$ | $0.88$ |
| flavor | $0.13$ | $0.98$ | $0.98$ |
| suitable for snack | $0.84$ | $0.43$ | $0.89$ |
| provides lots of energy | $0.97$ | $-0.02$ | $0.93$ |
| cumulative proportion | $0.507$ | $0.932$ | |

Now good buy, snack and energy load on $F_1^*$, a nutritional factor, and taste and flavor on $F_2^*$, a taste factor. The communalities and the cumulative proportion $0.932$ are unchanged; only its split between the two factors moves from $(0.571,0.361)$ to $(0.507,0.425)$.

![Varimax rotation for the consumer-preference data: the five variables plotted by their loadings on two factors, with the unrotated factor axes (left) and the varimax-rotated axes (right), which pass close to the two clusters of variables](./plots/varimax-rotation.py)

### 8.3.3. Other Rotations

*Orthogonal rotations* keep the factors uncorrelated (independent under normality). Varimax maximizes, for each factor, the variance of the squared loadings across variables, aiming at factors that are simple to interpret; quartimax maximizes, for each variable, the variance of its squared loadings across factors, aiming at variables that are simple to interpret, and tends to produce a general factor.

*Oblique rotations* allow correlated factors; intuitively, the angle between the factor axes need not be a right angle. Examples are oblimin, which minimizes the covariance of the squared loadings between factors; promax, which starts from an orthogonal (varimax) solution and drives small loadings even closer to zero; and target rotation, which approaches a "simple structure" chosen in advance. An oblique solution is reported by two matrices: the *pattern matrix* of the usual loadings, used to interpret the factors, and the *structure matrix* of correlations between the variables and the factors. For orthogonal factors the two coincide.

Which to use? The choice is generally not critical. Interpretation after an orthogonal (varimax) rotation is simple because the factors are uncorrelated and the loadings of standardized variables are correlations. An oblique (promax) configuration may look simpler, but the correlations between the factors can be difficult to reconcile with the interpretation.

## 8.4. Factor Scores

### 8.4.1. Purpose and Setting

Factor scores, the estimated values $\hat{\boldsymbol{f}}_j$ of the common factors for each unit $j$, are used for diagnostics (outliers, checking assumptions), as inputs to subsequent analyses (for example, regression on a few factors instead of many variables), and as indices in their own right (a measure of ability or of a personality trait).

Estimating them is not ordinary estimation: for each unit there are $m+p$ unobserved quantities $(\boldsymbol{f},\boldsymbol{\varepsilon})$ but only $p$ observations. The usual heuristic is to take $L$, $\Psi$ and $\boldsymbol{\mu}$ as known, replacing them by their estimates, and to estimate the factor vector of a single unit with observation $\boldsymbol{x}$. Two views of $\boldsymbol{F}$ lead to two methods.

- When the population parameters $L$, $\Psi$ were estimated, the regularity shared by many units was sought, and each unit's factors varied with the sampling, so $\boldsymbol{F}$ was random.
- For a fixed unit (a particular student), the factors (abilities) are fixed but unknown constants, to be estimated from that unit's observed $\boldsymbol{x}$, which is no longer random. This view leads to the weighted least squares method; keeping $\boldsymbol{F}$ random and predicting it from $\boldsymbol{X}$ leads to the regression method.

### 8.4.2. The Weighted Least Squares Method

For a fixed unit, the model $\boldsymbol{x}-\boldsymbol{\mu}=L\boldsymbol{f}+\boldsymbol{\varepsilon}$ is a linear regression with "design matrix" $L$, "coefficients" $\boldsymbol{f}$ and $p$ "observations". Ordinary least squares ([3.4.7](/3.4.7)) minimizes $\sum_{i=1}^p\varepsilon_i^2=(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})^{\mathsf T}(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})$ and gives $\hat{\boldsymbol{f}}=(L^{\mathsf T}L)^{-1}L^{\mathsf T}(\boldsymbol{x}-\boldsymbol{\mu})$. But the errors have unequal variances $\operatorname{Var}(\varepsilon_i)=\psi_i$, so the Gauss–Markov conditions fail. Rescaling by $\Psi^{-1/2}$,

$$
\Psi^{-1/2}(\boldsymbol{x}-\boldsymbol{\mu})=\Psi^{-1/2}L\boldsymbol{f}+\Psi^{-1/2}\boldsymbol{\varepsilon},\qquad\operatorname{Cov}(\Psi^{-1/2}\boldsymbol{\varepsilon})=\Psi^{-1/2}\Psi\Psi^{-1/2}=I_p,
$$
restores them, and OLS for the rescaled model minimizes $\sum_{i=1}^p\varepsilon_i^2/\psi_i=(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu}-L\boldsymbol{f})$.

**Definition 8.4.1 (Bartlett Factor Score)** The **weighted least squares factor score** (**Bartlett factor score**, M. S. Bartlett, 1937) of a unit with observation $\boldsymbol{x}_j$ is

$$
\hat{\boldsymbol{f}}_j=(\hat L^{\mathsf T}\hat\Psi^{-1}\hat L)^{-1}\hat L^{\mathsf T}\hat\Psi^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}}),
$$
obtained from $\boldsymbol{f}=(L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ by taking $\hat L$, $\hat\Psi$ and $\hat{\boldsymbol{\mu}}=\bar{\boldsymbol{x}}$ as the true values.

With maximum likelihood estimates, $\hat L^{\mathsf T}\hat\Psi^{-1}\hat L=\hat\Delta$ is diagonal and the inverse is trivial. If $L$ and $\Psi$ are those of the standardized variables, $L_z=V^{-1/2}L$ and $\Psi_z=V^{-1/2}\Psi V^{-1/2}$, then $L_z^{\mathsf T}\Psi_z^{-1}L_z=L^{\mathsf T}\Psi^{-1}L$ and $L_z^{\mathsf T}\Psi_z^{-1}\boldsymbol{z}=L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$, so

$$
\hat{\boldsymbol{f}}_z=(L_z^{\mathsf T}\Psi_z^{-1}L_z)^{-1}L_z^{\mathsf T}\Psi_z^{-1}\boldsymbol{z}=\hat{\boldsymbol{f}}:
$$
the Bartlett scores do not depend on whether the analysis uses $S$ or $R$, in accordance with the scale invariance of the model, provided the estimates of $L$ and $\Psi$ transform accordingly (as maximum likelihood estimates do).

If $L$ and $\Psi$ are estimated by the principal component method, one usually uses OLS, because the specific variances are not modeled. With $\tilde L=[\sqrt{\hat\lambda_1}\hat{\boldsymbol{e}}_1,\dots,\sqrt{\hat\lambda_m}\hat{\boldsymbol{e}}_m]$, the matrix $\tilde L^{\mathsf T}\tilde L=\operatorname{diag}(\hat\lambda_1,\dots,\hat\lambda_m)$ is diagonal and $\tilde L^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})$ has entries $\sqrt{\hat\lambda_j}\,\hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})$, so

$$
\hat f_j=\frac{1}{\sqrt{\hat\lambda_j}}\,\hat{\boldsymbol{e}}_j^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\frac{\hat y_j}{\sqrt{\hat\lambda_j}},\qquad j=1,\dots,m,
$$
where $\hat y_j$ is the $j$-th principal component score of [3.4.5](/3.4.5): the factor scores are the standardized principal component scores. Geometrically, when the principal component method is used, the space spanned by the common factors is exactly the subspace onto which PCA reduces the data (for $m=2$, the same plane). The factors are unit-variance coordinates in that subspace, $F_j=Y_j/\sqrt{\lambda_j}$ with $Y_j=\boldsymbol{e}_j^{\mathsf T}(\boldsymbol{X}-\boldsymbol{\mu})$, so that $L\boldsymbol{F}=\sum_{j\le m}\boldsymbol{e}_jY_j$, while the specific factors $\boldsymbol{\varepsilon}=\sum_{j>m}\boldsymbol{e}_jY_j$ are made of the remaining components.

### 8.4.3. The Regression Method

Now treat $\boldsymbol{F}$ as random. Under the normal factor model,

$$
\begin{bmatrix}\boldsymbol{X}-\boldsymbol{\mu}\\\boldsymbol{F}\end{bmatrix}=\begin{bmatrix}L\\I_m\end{bmatrix}\boldsymbol{F}+\begin{bmatrix}\boldsymbol{\varepsilon}\\\boldsymbol{0}\end{bmatrix}\sim\mathcal{N}_{p+m}\left(\boldsymbol{0},\begin{bmatrix}LL^{\mathsf T}+\Psi&L\\L^{\mathsf T}&I_m\end{bmatrix}\right).
$$
By the formula for the **conditional distribution** of a multivariate normal vector ([3.4.2](/3.4.2)), $\boldsymbol{F}\mid\boldsymbol{X}=\boldsymbol{x}$ is normal with

$$
\mathbb{E}(\boldsymbol{F}\mid\boldsymbol{x})=L^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})=L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}(\boldsymbol{x}-\boldsymbol{\mu}),\qquad\operatorname{Cov}(\boldsymbol{F}\mid\boldsymbol{x})=I_m-L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}L.
$$

**Definition 8.4.2 (Regression Factor Score)** The **regression factor score** (**Thomson factor score**, G. H. Thomson, 1951) of a unit with observation $\boldsymbol{x}_j$ is

$$
\hat{\boldsymbol{f}}_j=\hat L^{\mathsf T}\hat\Sigma^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}})=\hat L^{\mathsf T}(\hat L\hat L^{\mathsf T}+\hat\Psi)^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}}).
$$

The name comes from a second derivation that needs no normality. Regress the factors on the observations, $\boldsymbol{F}=B(\boldsymbol{X}-\boldsymbol{\mu})+\boldsymbol{\eta}$ with $\mathbb{E}\boldsymbol{\eta}=\boldsymbol{0}$ and $\operatorname{Cov}(\boldsymbol{X}-\boldsymbol{\mu},\boldsymbol{\eta})=O$, i.e. take the **best linear predictor** of $\boldsymbol{F}$ from $\boldsymbol{X}$. Since $\boldsymbol{F}$ is not observed, $B$ cannot be fitted directly, but the loadings are known covariances:

$$
l_{ij}=\operatorname{Cov}(X_i-\mu_i,F_j)=b_{j1}\sigma_{i1}+\cdots+b_{jp}\sigma_{ip},\qquad\text{i.e.}\qquad L=\Sigma B^{\mathsf T},
$$
so $B^{\mathsf T}=\Sigma^{-1}L$ and $\hat{\boldsymbol{F}}=L^{\mathsf T}\Sigma^{-1}(\boldsymbol{X}-\boldsymbol{\mu})$.

In practice $S$ is often used instead of $\hat L\hat L^{\mathsf T}+\hat\Psi$, which makes the scores more stable if the number of factors is chosen incorrectly: $\hat{\boldsymbol{f}}_j=\hat L^{\mathsf T}S^{-1}(\boldsymbol{x}_j-\bar{\boldsymbol{x}})$, or $\hat{\boldsymbol{f}}_j=\hat L_z^{\mathsf T}R^{-1}\boldsymbol{z}_j$ for standardized data. With principal component loadings this approximation again gives the standardized principal component scores: writing $S=P\Lambda P^{\mathsf T}$ and $\tilde L=P_m\Lambda_m^{1/2}$ (the first $m$ columns of $P$, the first $m$ eigenvalues),

$$
\hat{\boldsymbol{f}}=\tilde L^{\mathsf T}S^{-1}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\Lambda_m^{1/2}P_m^{\mathsf T}P\Lambda^{-1}P^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}})=\Lambda_m^{-1/2}P_m^{\mathsf T}(\boldsymbol{x}-\bar{\boldsymbol{x}}).
$$

### 8.4.4. Comparing the Methods

Write $\Delta=L^{\mathsf T}\Psi^{-1}L$, $\hat{\boldsymbol{f}}_{\mathrm{WLS}}=\Delta^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ and $\hat{\boldsymbol{f}}_{\mathrm{R}}=L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$. The key algebraic tool is

$$
L^{\mathsf T}(LL^{\mathsf T}+\Psi)^{-1}=(I_m+L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1},
$$
which follows from the **Woodbury matrix identity**, or directly from $(I_m+L^{\mathsf T}\Psi^{-1}L)L^{\mathsf T}=L^{\mathsf T}\Psi^{-1}(LL^{\mathsf T}+\Psi)$.

**Proposition 8.4.1** The two scores are related by

$$
\hat{\boldsymbol{f}}_{\mathrm{R}}=(I_m+\Delta)^{-1}\Delta\,\hat{\boldsymbol{f}}_{\mathrm{WLS}},\qquad\hat{\boldsymbol{f}}_{\mathrm{WLS}}=(I_m+\Delta^{-1})\,\hat{\boldsymbol{f}}_{\mathrm{R}}.
$$
Moreover:

1. (Unbiasedness) $\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{WLS}}\mid\boldsymbol{F})=\boldsymbol{F}$, whereas $\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{R}}\mid\boldsymbol{F})=(I_m+\Delta^{-1})^{-1}\boldsymbol{F}$, so the regression scores are biased toward $\boldsymbol{0}$.
2. (Mean squared error) $\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{WLS}}-\boldsymbol{F})(\hat{\boldsymbol{f}}_{\mathrm{WLS}}-\boldsymbol{F})^{\mathsf T}=\Delta^{-1}$ and $\mathbb{E}(\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F})(\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F})^{\mathsf T}=(I_m+\Delta)^{-1}$, which is smaller.
3. (Rotation) If $L^*=LT$ with $T$ orthogonal, both scores transform as the factors do: $\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$.

**Proof** The relation follows from the identity, since $L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})=\Delta\hat{\boldsymbol{f}}_{\mathrm{WLS}}$. Substituting $\boldsymbol{x}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}$,

$$
\hat{\boldsymbol{f}}_{\mathrm{WLS}}=\boldsymbol{F}+\Delta^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon},\qquad\hat{\boldsymbol{f}}_{\mathrm{R}}=(I_m+\Delta)^{-1}\Delta\boldsymbol{F}+(I_m+\Delta)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}.
$$
Taking conditional expectations gives 1, since $(I_m+\Delta)^{-1}\Delta=(I_m+\Delta^{-1})^{-1}$. For 2, $\operatorname{Cov}(L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon})=L^{\mathsf T}\Psi^{-1}\Psi\Psi^{-1}L=\Delta$, so the WLS error has covariance $\Delta^{-1}\Delta\Delta^{-1}=\Delta^{-1}$. The regression error is $\hat{\boldsymbol{f}}_{\mathrm{R}}-\boldsymbol{F}=-(I_m+\Delta)^{-1}\boldsymbol{F}+(I_m+\Delta)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}$, with $\boldsymbol{F}$ and $\boldsymbol{\varepsilon}$ uncorrelated and $\operatorname{Cov}(\boldsymbol{F})=I_m$, so its second moment is $(I_m+\Delta)^{-1}(I_m+\Delta)(I_m+\Delta)^{-1}=(I_m+\Delta)^{-1}$; and $\Delta^{-1}\succeq(I_m+\Delta)^{-1}$ because the eigenvalues satisfy $1/\delta\ge1/(1+\delta)$. For 3, $(T^{\mathsf T}\Delta T)^{-1}T^{\mathsf T}L^{\mathsf T}\Psi^{-1}=T^{\mathsf T}\Delta^{-1}L^{\mathsf T}\Psi^{-1}$ and $T^{\mathsf T}L^{\mathsf T}(LTT^{\mathsf T}L^{\mathsf T}+\Psi)^{-1}=T^{\mathsf T}L^{\mathsf T}\Sigma^{-1}$. $\square$

When $\Delta$ is diagonal (the maximum likelihood constraint), the relation is componentwise, $\hat f_{\mathrm{R},j}=\frac{\delta_j}{1+\delta_j}\hat f_{\mathrm{WLS},j}$: the regression scores are the Bartlett scores shrunk toward $0$, most strongly for factors with small $\delta_j$, i.e. factors that are poorly determined by the data. This is a **bias–variance trade-off**: the Bartlett score is unbiased with larger mean squared error, the regression score biased with smaller mean squared error.

![Simulated two-factor model: Bartlett (weighted least squares) scores scatter around the 45-degree line, regression scores are shrunk toward zero but have smaller mean squared error](./plots/factor-score-shrinkage.py)

The comparison has a natural interpretation as ridge regression ([3.4.7](/3.4.7)) of the rescaled model $\Psi^{-1/2}(\boldsymbol{x}-\boldsymbol{\mu})=\Psi^{-1/2}L\boldsymbol{f}+\Psi^{-1/2}\boldsymbol{\varepsilon}$.

**Proposition 8.4.2** Let $\hat{\boldsymbol{f}}(\lambda)=(\Delta+\lambda I_m)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ for $\lambda\ge0$, the ridge estimator of $\boldsymbol{f}$ in the rescaled model, so that $\hat{\boldsymbol{f}}(0)=\hat{\boldsymbol{f}}_{\mathrm{WLS}}$ and $\hat{\boldsymbol{f}}(1)=\hat{\boldsymbol{f}}_{\mathrm{R}}$. Then

$$
\mathbb{E}\big(\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}\big)\big(\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}\big)^{\mathsf T}=(\lambda I_m+\Delta)^{-1}+(\lambda^2-\lambda)(\lambda I_m+\Delta)^{-2},
$$
and its trace is minimized at $\lambda=1$: the regression score is the ridge estimator with the optimal tuning parameter.

**Proof** As above, $\hat{\boldsymbol{f}}(\lambda)-\boldsymbol{F}=-\lambda(\Delta+\lambda I_m)^{-1}\boldsymbol{F}+(\Delta+\lambda I_m)^{-1}L^{\mathsf T}\Psi^{-1}\boldsymbol{\varepsilon}$, whose second moment is $(\Delta+\lambda I_m)^{-1}(\lambda^2I_m+\Delta)(\Delta+\lambda I_m)^{-1}$; writing $\lambda^2I_m+\Delta=(\Delta+\lambda I_m)+(\lambda^2-\lambda)I_m$ gives the formula. In the eigenbasis of $\Delta$ the trace is $\sum_j(\delta_j+\lambda^2)/(\delta_j+\lambda)^2$, and $\frac{\mathrm{d}}{\mathrm{d}\lambda}\frac{\delta+\lambda^2}{(\delta+\lambda)^2}=\frac{2\delta(\lambda-1)}{(\delta+\lambda)^3}$ is negative for $\lambda<1$ and positive for $\lambda>1$. $\square$

Rotation and factor scores are two separate steps: rotation acts on $L$ at the population level, and factor scores are computed for each unit given whichever $L$ (rotated or not) has been chosen; by Proposition 8.4.1, rotating first and scoring afterwards gives the rotated scores. Which estimates of $L$ and $\Psi$ to use is a separate choice with its own merits:

- With principal component estimates, OLS and the (approximate) regression method give the same result, the standardized principal component scores, which are easy to compute; but they change when the data are standardized.
- With maximum likelihood estimates, the WLS and regression scores differ from each other, but both are unaffected by standardization, in accordance with the theoretical scale invariance of the model; they are harder to compute.

To plot factor scores, first estimate the population-level $L$ and $\Psi$, then compute the $m$-dimensional score of every unit; for $n=100$ students and $m=2$ this gives a $100\times2$ matrix of scores, and the scatter plot of its two columns is the plot of the first against the second factor.

**Example 8.4.1 (Stock Prices, Continued)** With the varimax-rotated maximum likelihood loadings (JPMorgan $0.763$ with a second loading below $0.1$; Citibank $0.819$, $0.232$; Wells Fargo $0.668$, $0.108$; Shell $0.113$, $0.991$; ExxonMobil $0.108$, $0.677$, so that $F_1^*$ is a bank factor and $F_2^*$ an oil factor), the Bartlett score of the first week is $(0.251,-1.854)$, while OLS would give $(0.176,-1.305)$: under maximum likelihood, OLS and WLS can differ a lot. With varimax-rotated principal component loadings, OLS (equal to the approximate regression score) gives $(0.065,-1.016)$ and WLS $(0.056,-1.045)$: under the principal component method the difference is small.

## 8.5. Factor Analysis in Practice

### 8.5.1. A Strategy

Two principles guide an application: interpretation ("if, while scrutinizing the factor analysis, the investigator can shout 'Wow, I understand these factors,' the application is deemed successful", in the words of R. Johnson and D. Wichern) and consistency of the results across methods and subsamples. The major steps are:

1. data collection and preparation;
2. choice of the number of factors;
3. extraction of the initial factors;
4. rotation to a final solution;
5. model diagnosis and refinement;
6. derivation of factor scores for further analysis.

In more detail: for large data sets, split them in half and perform the analysis on each part; for the given data and a fixed $m$, (1) perform a principal component factor analysis, (2) perform a maximum likelihood factor analysis, and (3) compare the two solutions, checking the factors and looking for outliers in factor score plots; repeat for other values of $m$; finally check consistency and interpretation.

**Example 8.5.1 (Chicken-Bone Data)** For $n=276$ chickens, six bone dimensions were measured: skull length and breadth (head), femur and tibia length (leg), humerus and ulna length (wing). With $m=3$ and varimax rotation, both methods find a dominant factor loading on the four leg and wing bones ($0.89$–$0.92$ for the principal component method, $0.83$–$0.94$ for maximum likelihood). The remaining factors differ: the principal component method gives one factor for skull breadth and one for skull length, with specific variances near zero for these two variables, while maximum likelihood gives a head factor and a weak wing factor; the cumulative proportions are $0.950$ and $0.823$. The plot of the first two factor scores reveals a few outlying chickens, and the plot of the scores from the two methods against each other shows that the first factors agree closely while the third factors do not; the third factor is therefore not a stable feature of the data.

### 8.5.2. Extensions

*Categorical variables.* Factor analysis hinges on the correlation matrix: as long as an interpretable correlation matrix is available, the analysis can be carried out. For binary or ordinal items, Pearson correlations tend to underestimate the associations; tetrachoric (binary) or polychoric (ordinal) correlations, which assume an underlying normal variable, are used instead.

*Exploratory and confirmatory analysis.* The analysis of this chapter is *exploratory factor analysis*: it summarizes the data, describes their correlation structure and generates hypotheses. *Confirmatory factor analysis* instead tests a highly constrained structure specified a priori: the number of factors is fixed by the analyst, it is specified which factors influence which observed variables (other loadings are set to zero), and one may test correlated measurement errors or a one-factor model against a multi-factor model. It is a special case of structural equation modeling.

## Summary

- Model: $\boldsymbol{X}-\boldsymbol{\mu}=L\boldsymbol{F}+\boldsymbol{\varepsilon}$ with uncorrelated unit-variance factors and diagonal $\Psi$; hence $\Sigma=LL^{\mathsf T}+\Psi$, $\sigma_{ii}=h_i^2+\psi_i$, $\operatorname{Cov}(\boldsymbol{X},\boldsymbol{F})=L$. The model reduces $p(p+1)/2$ parameters to $pm+p-m(m-1)/2$, is identified only up to rotations $L\mapsto LT$, and is invariant under rescaling of the variables; it can fail (Heywood cases).
- Population level: the principal component method ($\tilde L$ from the eigenpairs of $S$ or $R$; explicit, nested in $m$, residuals bounded by the neglected squared eigenvalues) and the maximum likelihood method (normality, constraint $L^{\mathsf T}\Psi^{-1}L$ diagonal, equivalent for $S$ and $R$, likelihood ratio test with $\frac12[(p-m)^2-p-m]$ degrees of freedom for the number of factors).
- Rotation: for interpretation only; communalities, specific variances and the fit are unchanged; varimax maximizes the spread of the squared scaled loadings in each column.
- Unit level: factor scores are computed for each unit given $\hat L$ and $\hat\Psi$ (see the table below); with principal component loadings, both OLS and the approximate regression method give the standardized principal component scores $\hat y_j/\sqrt{\hat\lambda_j}$.
- Factor analysis versus PCA: PCA expresses the components through the observed variables and is unique (up to signs); factor analysis expresses the observed variables through the factors and is unique only up to rotation; with the principal component method, both span the same subspace.

| | weighted least squares (Bartlett) | regression (Thomson) |
|---|---|---|
| formula | $(L^{\mathsf T}\Psi^{-1}L)^{-1}L^{\mathsf T}\Psi^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ | $L^{\mathsf T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ |
| view of $\boldsymbol{F}$ | fixed parameter | random vector |
| unbiased | yes | no (shrunk toward $\boldsymbol{0}$) |
| mean squared error | $\Delta^{-1}$ (larger) | $(I_m+\Delta)^{-1}$ (smaller) |
| under rotation $L^*=LT$ | $\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$ | $\hat{\boldsymbol{f}}^*=T^{\mathsf T}\hat{\boldsymbol{f}}$ |
