---
title: Canonical Correlation Analysis
description: Canonical correlation analysis of two sets of variables, the population canonical variates via the singular value decomposition, their interpretation through coefficients and correlations, invariance under standardization, sample canonical correlations with examples, the likelihood ratio test for the number of canonical pairs, and extensions.
---

Often two different kinds of variables are measured on the same units: exercise variables (climbing rate on a stair stepper, running speed, bench-press weight, push-ups per minute) and health variables (blood pressure, cholesterol, glucose level, body mass index); sales performance and aptitude test scores; image features and the words of their captions. *Canonical correlation analysis* (CCA), developed by H. Hotelling (1936), studies the association between two sets of variables through a few pairs of linear combinations, one from each set, chosen to be as highly correlated as possible. It identifies and quantifies the association between the sets, and it reduces the dimension of the cross-covariance matrix $\Sigma_{12}$, which has $pq$ entries, to $p$ canonical correlations. Like **principal component analysis** ([3.4.5](/3.4.5)), it proceeds by successive maximization under uncorrelatedness constraints, but it maximizes correlation between the sets instead of variance within one set, and its solution comes from the **singular value decomposition** of a standardized cross-covariance matrix ([2.1](/2.1)). Its special case with one variable in the first set is the multiple correlation of regression ([3.4.7](/3.4.7)); factor analysis ([3.4.8](/3.4.8)) has a probabilistic counterpart for two sets, mentioned in Section 9.5; and the likelihood ratio test of Section 9.4 relies on the **multivariate normal distribution** ([3.4.2](/3.4.2)). The method was the starting point of many modern techniques for multi-view data, such as cross-modal retrieval of images and texts and the linking of brain imaging data to behavioral measures.

## 9.1. The Problem

Let $\boldsymbol{X}^{(1)}=(X_1^{(1)},\dots,X_p^{(1)})^{\mathsf T}$ and $\boldsymbol{X}^{(2)}=(X_1^{(2)},\dots,X_q^{(2)})^{\mathsf T}$ be two random vectors, $p\le q$, with joint covariance matrix

$$
\Sigma=\operatorname{Cov}\begin{bmatrix}\boldsymbol{X}^{(1)}\\\boldsymbol{X}^{(2)}\end{bmatrix}=\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix},\qquad\Sigma_{11}\in\mathbb{R}^{p\times p},\quad\Sigma_{12}=\Sigma_{21}^{\mathsf T}\in\mathbb{R}^{p\times q},\quad\Sigma_{22}\in\mathbb{R}^{q\times q}.
$$
The association between the sets is contained in $\Sigma_{12}$, but its $pq$ entries are hard to digest. The aim is to find coefficient vectors $\boldsymbol{a}\in\mathbb{R}^p$ and $\boldsymbol{b}\in\mathbb{R}^q$ such that

$$
U=\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)}=a_1X_1^{(1)}+\cdots+a_pX_p^{(1)},\qquad V=\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)}=b_1X_1^{(2)}+\cdots+b_qX_q^{(2)}
$$
have the largest possible correlation, and then further pairs that capture the remaining association.

**Example 9.1.1 (Hotelling's Reading and Arithmetic Data)** Hotelling's original example relates $\boldsymbol{X}^{(1)}$ = (reading speed, reading power) to $\boldsymbol{X}^{(2)}$ = (arithmetic speed, arithmetic power), $p=q=2$, with

$$
\Sigma=\begin{bmatrix}100&60&30&7.2\\60&100&-6&8.4\\30&-6&144&57.6\\7.2&8.4&57.6&144\end{bmatrix},\qquad\rho=\begin{bmatrix}1&0.6&0.25&0.06\\0.6&1&-0.05&0.07\\0.25&-0.05&1&0.4\\0.06&0.07&0.4&1\end{bmatrix}.
$$
The four cross-correlations $0.25,0.06,-0.05,0.07$ are small and of mixed signs; which combinations of the reading scores are related to which combinations of the arithmetic scores?

## 9.2. Population Canonical Correlations

### 9.2.1. Definition

Since $\operatorname{Var}(U)=\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}$, $\operatorname{Var}(V)=\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}$ and $\operatorname{Cov}(U,V)=\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}$, the objective is

$$
\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\operatorname{Corr}(U,V)=\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}.
$$
Replacing $\boldsymbol{a}$ by $c\boldsymbol{a}$ with $c>0$ does not change the correlation, so we may normalize $\operatorname{Var}(U)=\operatorname{Var}(V)=1$.

**Definition 9.2.1 (Canonical Correlation)** The *first canonical variate pair* $(U_1,V_1)=(\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}_1^{\mathsf T}\boldsymbol{X}^{(2)})$ maximizes $\operatorname{Corr}(U,V)$ subject to $\operatorname{Var}(U)=\operatorname{Var}(V)=1$. For $k=2,\dots,p$, the *$k$-th canonical variate pair* $(U_k,V_k)=(\boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}_k^{\mathsf T}\boldsymbol{X}^{(2)})$ maximizes $\operatorname{Corr}(U,V)$ subject to

$$
\boldsymbol{a}_k^{\mathsf T}\Sigma_{11}\boldsymbol{a}_k=1,\quad\boldsymbol{b}_k^{\mathsf T}\Sigma_{22}\boldsymbol{b}_k=1,\quad\operatorname{Cov}(U_k,U_i)=\boldsymbol{a}_k^{\mathsf T}\Sigma_{11}\boldsymbol{a}_i=0,\quad\operatorname{Cov}(V_k,V_i)=\boldsymbol{b}_k^{\mathsf T}\Sigma_{22}\boldsymbol{b}_i=0\qquad(i<k).
$$
The variables $U_k$ and $V_k$ are the **canonical variates**, and $\rho_k^*=\operatorname{Corr}(U_k,V_k)$ is the $k$-th **canonical correlation**.

The construction parallels PCA: after the best pair, look for the best pair uncorrelated with the previous ones.

### 9.2.2. Computing the Canonical Variates

**Theorem 9.2.1** Suppose $p\le q$ and the joint covariance matrix $\Sigma$ of $\boldsymbol{X}^{(1)}$ and $\boldsymbol{X}^{(2)}$ has full rank. Let $\rho_1^{*2}\ge\cdots\ge\rho_p^{*2}$ be the eigenvalues of

$$
\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}
$$
with orthonormal eigenvectors $\boldsymbol{e}_1,\dots,\boldsymbol{e}_p$. Then $\rho_1^{*2},\dots,\rho_p^{*2}$ are also the $p$ largest eigenvalues of $\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1/2}$, with orthonormal eigenvectors $\boldsymbol{f}_k=\frac{1}{\rho_k^*}\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1/2}\boldsymbol{e}_k$ (when $\rho_k^*>0$), and

$$
\max_{\boldsymbol{a},\boldsymbol{b}}\operatorname{Corr}(U,V)=\rho_1^*,
$$
attained by the first canonical variate pair $U_1=\boldsymbol{e}_1^{\mathsf T}\Sigma_{11}^{-1/2}\boldsymbol{X}^{(1)}$, $V_1=\boldsymbol{f}_1^{\mathsf T}\Sigma_{22}^{-1/2}\boldsymbol{X}^{(2)}$. The $k$-th pair $U_k=\boldsymbol{e}_k^{\mathsf T}\Sigma_{11}^{-1/2}\boldsymbol{X}^{(1)}$, $V_k=\boldsymbol{f}_k^{\mathsf T}\Sigma_{22}^{-1/2}\boldsymbol{X}^{(2)}$ maximizes the correlation $\operatorname{Corr}(U_k,V_k)=\rho_k^*$ among the linear combinations uncorrelated with the preceding $1,\dots,k-1$ canonical variates, $k=2,\dots,p$. Thus $\boldsymbol{a}_k=\Sigma_{11}^{-1/2}\boldsymbol{e}_k$ and $\boldsymbol{b}_k=\Sigma_{22}^{-1/2}\boldsymbol{f}_k$.

**Proof** Substitute $\tilde{\boldsymbol{a}}=\Sigma_{11}^{1/2}\boldsymbol{a}$ and $\tilde{\boldsymbol{b}}=\Sigma_{22}^{1/2}\boldsymbol{b}$; the normalization becomes $\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1$, and

$$
\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}=\max_{\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1}\tilde{\boldsymbol{a}}^{\mathsf T}\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}\tilde{\boldsymbol{b}}=\max_{\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1}\tilde{\boldsymbol{a}}^{\mathsf T}Y\tilde{\boldsymbol{b}},\qquad Y=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}.
$$
Let $Y=P_1\Lambda P_2^{\mathsf T}$ be a singular value decomposition, with $P_1$ ($p\times p$) and $P_2$ ($q\times q$) orthogonal and $\Lambda$ the $p\times q$ matrix with diagonal $\lambda_1\ge\cdots\ge\lambda_p\ge0$ and zeros elsewhere. Then $\boldsymbol{c}=P_1^{\mathsf T}\tilde{\boldsymbol{a}}$ and $\boldsymbol{d}=P_2^{\mathsf T}\tilde{\boldsymbol{b}}$ are again unit vectors, and by the **Cauchy–Schwarz inequality**

$$
\tilde{\boldsymbol{a}}^{\mathsf T}Y\tilde{\boldsymbol{b}}=\boldsymbol{c}^{\mathsf T}\Lambda\boldsymbol{d}=\sum_{i=1}^p\lambda_ic_id_i\le\sum_{i=1}^p\lambda_i\lvert c_i\rvert\lvert d_i\rvert\le\lambda_1\sum_{i=1}^p\lvert c_i\rvert\lvert d_i\rvert\le\lambda_1\|\boldsymbol{c}\|\|\boldsymbol{d}\|=\lambda_1,
$$
with equality for $\boldsymbol{c}$ and $\boldsymbol{d}$ the first standard basis vectors, i.e. $\tilde{\boldsymbol{a}}$ and $\tilde{\boldsymbol{b}}$ the first columns of $P_1$ and $P_2$, the first left and right **singular vectors** of $Y$. Since $YY^{\mathsf T}=P_1\Lambda\Lambda^{\mathsf T}P_1^{\mathsf T}=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}$ and $Y^{\mathsf T}Y=P_2\Lambda^{\mathsf T}\Lambda P_2^{\mathsf T}$, the left singular vectors are the $\boldsymbol{e}_k$, the right ones the $\boldsymbol{f}_k$, $\lambda_k^2=\rho_k^{*2}$, and $Y^{\mathsf T}\boldsymbol{e}_k=\lambda_k\boldsymbol{f}_k$ gives the formula for $\boldsymbol{f}_k$.

For the $k$-th pair, $\operatorname{Cov}(U,U_i)=\tilde{\boldsymbol{a}}^{\mathsf T}\boldsymbol{e}_i=c_i$ and $\operatorname{Cov}(V,V_i)=d_i$, so the constraints force $c_i=d_i=0$ for $i<k$, and the same chain of inequalities, now starting from $i=k$, gives the maximum $\lambda_k$, attained at $\tilde{\boldsymbol{a}}=\boldsymbol{e}_k$, $\tilde{\boldsymbol{b}}=\boldsymbol{f}_k$. $\square$

The proof treats both vectors at once through the SVD. One can also proceed one vector at a time: for fixed $\tilde{\boldsymbol{a}}$, the Cauchy–Schwarz inequality gives the best $\tilde{\boldsymbol{b}}=Y^{\mathsf T}\tilde{\boldsymbol{a}}/\|Y^{\mathsf T}\tilde{\boldsymbol{a}}\|$ with value $\|Y^{\mathsf T}\tilde{\boldsymbol{a}}\|=\sqrt{\tilde{\boldsymbol{a}}^{\mathsf T}YY^{\mathsf T}\tilde{\boldsymbol{a}}}$, and maximizing this **Rayleigh quotient** over unit $\tilde{\boldsymbol{a}}$ gives the largest eigenvalue of $YY^{\mathsf T}$, attained at $\boldsymbol{e}_1$; then $\tilde{\boldsymbol{b}}=Y^{\mathsf T}\boldsymbol{e}_1/\rho_1^*=\boldsymbol{f}_1$. A third route, Lagrange multipliers, leads to the generalized eigenvalue problem $\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\boldsymbol{a}=\rho^2\Sigma_{11}\boldsymbol{a}$, i.e. $\lvert\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}-\rho^2\Sigma_{11}\rvert=0$; this form generalizes to kernel CCA.

**Example 9.2.1 (Hotelling's Data, Continued)** For the $\Sigma$ of Example 9.1.1, the eigenvalues are $\rho_1^{*2}\approx0.146$ and $\rho_2^{*2}\approx0.005$, so $\rho_1^*\approx0.38$ and $\rho_2^*\approx0.07$, and

$$
U_1=\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}^{(1)}=-0.12X_1^{(1)}+0.10X_2^{(1)},\qquad V_1=\boldsymbol{b}_1^{\mathsf T}\boldsymbol{X}^{(2)}=-0.09X_1^{(2)}+0.03X_2^{(2)}.
$$
The best linear combinations of the two sets have correlation $0.38$, larger than every individual cross-correlation (at most $0.25$); the second pair is practically uncorrelated. (The signs of $\boldsymbol{a}_k$ and $\boldsymbol{b}_k$ can be reversed together.) How should $U_1$ and $V_1$ be interpreted?

### 9.2.3. Interpreting the Canonical Variates

Two kinds of quantities describe a canonical variate.

- The *canonical coefficients* $a_{ik}$, the entries of $\boldsymbol{a}_i^{\mathsf T}=(a_{i1},\dots,a_{ip})$, measure the contribution of the $k$-th variable $X_k^{(1)}$ to $U_i$ given the other variables of the set (a multivariate measure, like a regression coefficient). They depend on the units of the variables, and with correlated variables their signs can be misleading.
- The correlations between the canonical variates and the original variables (a univariate measure, like a loading) show how strongly each variable is related to the variate on its own.

In matrix form, let $A=[\boldsymbol{a}_1,\dots,\boldsymbol{a}_p]^{\mathsf T}$ ($p\times p$) and $B=[\boldsymbol{b}_1,\dots,\boldsymbol{b}_p]^{\mathsf T}$ ($p\times q$), so that $\boldsymbol{U}=A\boldsymbol{X}^{(1)}$ and $\boldsymbol{V}=B\boldsymbol{X}^{(2)}$ collect all canonical variates, and let $D_{11}=\operatorname{diag}(\Sigma_{11})$ and $D_{22}=\operatorname{diag}(\Sigma_{22})$ be the diagonal matrices of variances. Since $\operatorname{Cov}(\boldsymbol{U},\boldsymbol{X}^{(1)})=\operatorname{Cov}(A\boldsymbol{X}^{(1)},\boldsymbol{X}^{(1)})=A\Sigma_{11}$ and the canonical variates have unit variance,

$$
\begin{aligned}
\operatorname{Corr}(\boldsymbol{U},\boldsymbol{X}^{(1)})&=\operatorname{Cov}(\boldsymbol{U},D_{11}^{-1/2}\boldsymbol{X}^{(1)})=A\Sigma_{11}D_{11}^{-1/2},&\operatorname{Corr}(\boldsymbol{U},\boldsymbol{X}^{(2)})&=A\Sigma_{12}D_{22}^{-1/2},\\
\operatorname{Corr}(\boldsymbol{V},\boldsymbol{X}^{(2)})&=B\Sigma_{22}D_{22}^{-1/2},&\operatorname{Corr}(\boldsymbol{V},\boldsymbol{X}^{(1)})&=B\Sigma_{21}D_{11}^{-1/2}.
\end{aligned}
$$

**Example 9.2.2 (Hotelling's Data, Continued)** For $V_1=-0.09X_1^{(2)}+0.03X_2^{(2)}$, the correlations are $\operatorname{Corr}(V_1,X_1^{(2)})=-0.923$ and $\operatorname{Corr}(V_1,X_2^{(2)})=-0.017$. The positive coefficient of arithmetic power does not mean that $V_1$ is positively related to it: given arithmetic speed, power enters with a small positive weight, but on its own it is uncorrelated with $V_1$, which is essentially (minus) arithmetic speed. Similarly $\operatorname{Corr}(U_1,X_1^{(1)})=-0.65$ and $\operatorname{Corr}(U_1,X_2^{(1)})=0.22$. The first canonical pair thus mainly links reading speed with arithmetic speed.

![Hotelling's example: the four variables plotted by their correlations with the canonical variates U_1 and U_2 of the reading set; arithmetic speed is related to U_1, arithmetic power to neither](./plots/hotelling-correlation-plot.py)

### 9.2.4. Properties

The canonical variates satisfy, for $k,l=1,\dots,p$,

$$
\operatorname{Var}(U_k)=\operatorname{Var}(V_k)=1,\qquad\operatorname{Cov}(U_k,U_l)=\operatorname{Cov}(V_k,V_l)=\operatorname{Cov}(U_k,V_l)=0\quad(k\ne l),
$$
or in matrix form

$$
\operatorname{Cov}(\boldsymbol{U})=A\Sigma_{11}A^{\mathsf T}=I_p,\qquad\operatorname{Cov}(\boldsymbol{V})=B\Sigma_{22}B^{\mathsf T}=I_p,\qquad\operatorname{Cov}(\boldsymbol{U},\boldsymbol{V})=A\Sigma_{12}B^{\mathsf T}=\operatorname{diag}(\rho_1^*,\dots,\rho_p^*),
$$
so that $\operatorname{Cov}\begin{bmatrix}\boldsymbol{U}\\\boldsymbol{V}\end{bmatrix}=\begin{bmatrix}I_p&\Lambda_\rho\\\Lambda_\rho&I_p\end{bmatrix}$ with $\Lambda_\rho=\operatorname{diag}(\rho_1^*,\dots,\rho_p^*)$. The cross-covariance $\Sigma_{12}$ with $pq$ entries has been reduced to $p$ numbers. Unlike in PCA, the coefficient vectors $\boldsymbol{a}_i$ are not orthogonal to each other; they are orthogonal in the inner product defined by $\Sigma_{11}$.

The first canonical correlation generalizes the ordinary correlation:

- $p$ and $q$ variables: $\rho_1^*=\max_{\boldsymbol{a},\boldsymbol{b}}\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})$;
- $1$ and $1$ variable: $\lvert\operatorname{Corr}(X_i^{(1)},X_k^{(2)})\rvert$ is the correlation of two particular linear combinations, so it is at most $\rho_1^*$;
- $1$ and $q$ variables: the *multiple correlation coefficient* $\max_{\boldsymbol{b}}\operatorname{Corr}(X_1^{(1)},\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})$, the correlation between $X_1^{(1)}$ and its **best linear predictor** from $\boldsymbol{X}^{(2)}$, is at most $\rho_1^*$, and equals it when $p=1$.

An $R^2$-type interpretation follows from the same idea. For the $k$-th pair,

$$
\max_{\boldsymbol{b}}\operatorname{Corr}(U_k,\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})=\operatorname{Corr}(U_k,V_k)=\rho_k^*,\qquad\max_{\boldsymbol{a}}\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)},V_k)=\rho_k^*,
$$
(the first because $\max_{\boldsymbol{b}}$ equals $\sqrt{\boldsymbol{a}_k^{\mathsf T}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\boldsymbol{a}_k}=\sqrt{\boldsymbol{e}_k^{\mathsf T}YY^{\mathsf T}\boldsymbol{e}_k}=\rho_k^*$). Hence $\rho_k^{*2}$ is the proportion of the variance of $U_k$ explained by $\boldsymbol{X}^{(2)}$, and also the proportion of the variance of $V_k$ explained by $\boldsymbol{X}^{(1)}$: the variance shared by the two sets along the $k$-th pair.

Geometrically, in the space of centered random variables with inner product $\langle X,W\rangle=\mathbb{E}(XW)$ (length = standard deviation, cosine of the angle = correlation), the variables of each set span a subspace, of dimension $p$ and $q$. The first canonical pair is the pair of unit vectors, one in each subspace, with the smallest angle $\theta_1$, and $\rho_1^*=\cos\theta_1$; the further pairs give the further principal angles between the two subspaces. For $p=1$ and $q=2$, $V_1$ is the direction of the projection of $X^{(1)}$ onto the plane of $\boldsymbol{X}^{(2)}$, which is regression. For $p=q=2$, if the two planes intersect in a line, then $U_1=V_1$ lies on that line and $\rho_1^*=1$; if moreover the remaining directions are orthogonal, $\rho_2^*=0$.

### 9.2.5. Standardized Variables

What happens if one of the variables is measured on a dramatically different scale? The canonical correlations do not change, as we now show, although the coefficients do. The canonical variates can be computed for the standardized variables

$$
Z_k^{(j)}=\frac{X_k^{(j)}-\mu_k^{(j)}}{\sqrt{\sigma_{kk}^{(j)}}},\qquad\text{or}\qquad\boldsymbol{Z}^{(j)}=D_{jj}^{-1/2}(\boldsymbol{X}^{(j)}-\boldsymbol{\mu}^{(j)}),\quad j=1,2,
$$
whose covariance matrix is the correlation matrix

$$
\begin{bmatrix}\rho_{11}&\rho_{12}\\\rho_{21}&\rho_{22}\end{bmatrix}=\rho=D^{-1/2}\Sigma D^{-1/2}=\begin{bmatrix}D_{11}^{-1/2}&O\\O&D_{22}^{-1/2}\end{bmatrix}\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}\begin{bmatrix}D_{11}^{-1/2}&O\\O&D_{22}^{-1/2}\end{bmatrix}.
$$
Theorem 9.2.1 applied to $\rho$ gives the canonical variates $U_k=\boldsymbol{e}_k^{\mathsf T}\rho_{11}^{-1/2}\boldsymbol{Z}^{(1)}$, $V_k=\boldsymbol{f}_k^{\mathsf T}\rho_{22}^{-1/2}\boldsymbol{Z}^{(2)}$, where now $\rho_1^{*2}\ge\cdots\ge\rho_p^{*2}$ are the eigenvalues of $\rho_{11}^{-1/2}\rho_{12}\rho_{22}^{-1}\rho_{21}\rho_{11}^{-1/2}$ with eigenvectors $\boldsymbol{e}_k$, and $\boldsymbol{f}_k=\frac{1}{\rho_k^*}\rho_{22}^{-1/2}\rho_{21}\rho_{11}^{-1/2}\boldsymbol{e}_k$ (the $\boldsymbol{e}_k$, $\boldsymbol{f}_k$ differ from those for $\Sigma$).

**Proposition 9.2.1** Let $\boldsymbol{Z}^{(i)}=C_i\boldsymbol{X}^{(i)}+\boldsymbol{c}_i$ with invertible $C_1\in\mathbb{R}^{p\times p}$, $C_2\in\mathbb{R}^{q\times q}$. Then $\boldsymbol{Z}^{(1)},\boldsymbol{Z}^{(2)}$ have the same canonical correlations as $\boldsymbol{X}^{(1)},\boldsymbol{X}^{(2)}$, and the same canonical variates up to additive constants; the canonical coefficients transform as $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$, $\boldsymbol{b}=C_2^{\mathsf T}\boldsymbol{b}_z$. In particular, for standardization, $\boldsymbol{a}_z=D_{11}^{1/2}\boldsymbol{a}$ and $\boldsymbol{b}_z=D_{22}^{1/2}\boldsymbol{b}$: the standardized coefficients are the raw coefficients times the standard deviations.

**Proof** The covariance blocks of $\boldsymbol{Z}$ are $\tilde\Sigma_{ij}=C_i\Sigma_{ij}C_j^{\mathsf T}$, so for $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$, $\boldsymbol{b}=C_2^{\mathsf T}\boldsymbol{b}_z$,

$$
\frac{\boldsymbol{a}_z^{\mathsf T}\tilde\Sigma_{12}\boldsymbol{b}_z}{\sqrt{\boldsymbol{a}_z^{\mathsf T}\tilde\Sigma_{11}\boldsymbol{a}_z}\sqrt{\boldsymbol{b}_z^{\mathsf T}\tilde\Sigma_{22}\boldsymbol{b}_z}}=\frac{(C_1^{\mathsf T}\boldsymbol{a}_z)^{\mathsf T}\Sigma_{12}(C_2^{\mathsf T}\boldsymbol{b}_z)}{\sqrt{(C_1^{\mathsf T}\boldsymbol{a}_z)^{\mathsf T}\Sigma_{11}(C_1^{\mathsf T}\boldsymbol{a}_z)}\sqrt{(C_2^{\mathsf T}\boldsymbol{b}_z)^{\mathsf T}\Sigma_{22}(C_2^{\mathsf T}\boldsymbol{b}_z)}}=\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}.
$$
Since $\boldsymbol{a}_z\mapsto C_1^{\mathsf T}\boldsymbol{a}_z$ is a bijection, the two problems, including the uncorrelatedness constraints, have the same optimal values, and the optimal variates $\boldsymbol{a}_z^{\mathsf T}\boldsymbol{Z}^{(1)}=\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)}+\boldsymbol{a}_z^{\mathsf T}\boldsymbol{c}_1$ coincide up to a constant. $\square$

**Example 9.2.3 (Hotelling's Data, Continued)** The correlation matrix $\rho$ gives the same $\rho_1^{*2}=0.146$ and $\rho_2^{*2}=0.005$ as $\Sigma$. The standardized coefficients are $U_1=-1.22Z_1^{(1)}+0.95Z_2^{(1)}$ and $V_1=-1.09Z_1^{(2)}+0.42Z_2^{(2)}$, the raw coefficients multiplied by the standard deviations $10,10$ and $12,12$.

## 9.3. Sample Canonical Correlations

### 9.3.1. Sample Canonical Variates

Let $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$ be $n$ independent observations from a $(p+q)$-dimensional population with mean $\boldsymbol{\mu}$ and covariance matrix $\Sigma$. Each observation is split as $\boldsymbol{x}_j=(\boldsymbol{x}_j^{(1)},\boldsymbol{x}_j^{(2)})$, so the $n\times(p+q)$ data matrix consists of an $n\times p$ block of first-set variables and an $n\times q$ block of second-set variables, with **sample covariance matrix** and **sample correlation matrix**

$$
S=\begin{bmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{bmatrix},\qquad R=\begin{bmatrix}R_{11}&R_{12}\\R_{21}&R_{22}\end{bmatrix}.
$$
The sample version replaces the population distribution by the empirical distribution, $\Sigma$ by $S$ and $\rho$ by $R$, and follows the same procedure.

**Theorem 9.3.1** Let $\hat\rho_1^{*2}\ge\cdots\ge\hat\rho_p^{*2}$ be the eigenvalues of $S_{11}^{-1/2}S_{12}S_{22}^{-1}S_{21}S_{11}^{-1/2}$ with orthonormal eigenvectors $\hat{\boldsymbol{e}}_1,\dots,\hat{\boldsymbol{e}}_p$; they are also the $p$ largest eigenvalues of $S_{22}^{-1/2}S_{21}S_{11}^{-1}S_{12}S_{22}^{-1/2}$, with eigenvectors $\hat{\boldsymbol{f}}_k=\frac{1}{\hat\rho_k^*}S_{22}^{-1/2}S_{21}S_{11}^{-1/2}\hat{\boldsymbol{e}}_k$. The $k$-th pair of sample canonical variates

$$
\hat U_k=\hat{\boldsymbol{e}}_k^{\mathsf T}S_{11}^{-1/2}\boldsymbol{x}^{(1)},\qquad\hat V_k=\hat{\boldsymbol{f}}_k^{\mathsf T}S_{22}^{-1/2}\boldsymbol{x}^{(2)}
$$
attains the $k$-th sample canonical correlation $\widehat{\operatorname{Corr}}(\hat U_k,\hat V_k)=\hat\rho_k^*$, $k=1,\dots,p$, and the sample canonical variates satisfy

$$
\widehat{\operatorname{Var}}(\hat U_k)=\widehat{\operatorname{Var}}(\hat V_k)=1,\qquad\widehat{\operatorname{Cov}}(\hat U_k,\hat U_l)=\widehat{\operatorname{Cov}}(\hat V_k,\hat V_l)=\widehat{\operatorname{Cov}}(\hat U_k,\hat V_l)=0\quad(k\ne l).
$$

Here $\widehat{\operatorname{Var}}$ and $\widehat{\operatorname{Cov}}$ are sample variances and covariances over the $n$ units, not population moments. In matrix form, with $\hat A$ and $\hat B$ built from $\hat{\boldsymbol{a}}_k=S_{11}^{-1/2}\hat{\boldsymbol{e}}_k$ and $\hat{\boldsymbol{b}}_k=S_{22}^{-1/2}\hat{\boldsymbol{f}}_k$, $\hat{\boldsymbol{U}}=\hat A\boldsymbol{x}^{(1)}$, $\hat{\boldsymbol{V}}=\hat B\boldsymbol{x}^{(2)}$, and $\hat AS_{11}\hat A^{\mathsf T}=I_p$, $\hat BS_{22}\hat B^{\mathsf T}=I_p$, $\hat AS_{12}\hat B^{\mathsf T}=\operatorname{diag}(\hat\rho_1^*,\dots,\hat\rho_p^*)$; the results are most easily obtained in this matrix form.

The values $\hat U_k(\boldsymbol{x}_j)$ and $\hat V_k(\boldsymbol{x}_j)$ for the units are the *canonical variate scores*. As with factor analysis ([3.4.8](/3.4.8)), two kinds of plots are useful: at the population level, the variables are plotted by their correlations with two canonical variates; at the unit level, the units are plotted by their scores.

![Two sets of simulated variables (p = 2, q = 3): scatter plots of the sample canonical variate scores (U_1, V_1) and (U_2, V_2), with sample canonical correlations of about 0.83 and 0.31](./plots/canonical-variates-scatter.py)

### 9.3.2. Examples

**Example 9.3.1 (Salespeople Data)** For $n=50$ salespeople, three measures of sales performance, $\boldsymbol{x}^{(1)}$ = (sales growth, sales profitability, new-account sales), and four test scores, $\boldsymbol{x}^{(2)}$ = (creativity, mechanical reasoning, abstract reasoning, mathematics), were recorded. The heat map of the correlation matrix shows strong positive correlations within the performance block and between performance and the mathematics test. The sample canonical correlations are

$$
\hat\rho_1^*=0.994,\qquad\hat\rho_2^*=0.878,\qquad\hat\rho_3^*=0.384.
$$
The coefficients of $\hat U_1$ (as computed by the R function `cc`) are $-0.458$, $-0.212$, $-0.369$ for growth, profitability and new-account sales, and the correlations of $\hat U_1$ with these variables are $-0.980$, $-0.946$, $-0.952$: $\hat U_1$ is (minus) an overall sales performance index. (The function `cancor` gives coefficients that differ by the factor $-1/\sqrt{n-1}$, because it normalizes the variates to unit sum of squares instead of unit sample variance and chooses the opposite signs; the canonical correlations are the same.) The scores of the first salesperson are $(\hat U_1,\hat U_2,\hat U_3)=(0.978,-0.363,0.819)$.

To visualize the association, both sets of variables can be projected onto the plane of two canonical variates of the first set. The coordinates of a variable are its correlations with the two variates: in the geometry of Section 9.2.4, the projection of $X_i$ onto the direction $U_1$ has length $\sqrt{\operatorname{Var}(X_i)}\cos\theta=\sqrt{\operatorname{Var}(X_i)}\operatorname{Corr}(X_i,U_1)$, which for a standardized variable is the correlation itself. Since this is a projection, some information is lost; variables close to the unit circle are well represented. Plotting the plane of $(\hat U_1,\hat U_3)$, all seven variables lie on the negative side of the $\hat U_1$ axis, the performance variables close to $-1$, and the third canonical variate separates sales growth and abstract reasoning (positive) from new-account sales and creativity (negative). The unit-level plot of the scores $(\hat U_1,\hat U_3)$ shows individual salespeople, for instance one with an unusually large $\hat U_3$. The two plots are not related point by point: the first shows relations between variables, the second shows characteristics of units. The choice of $(\hat U_1,\hat U_3)$ here is only for illustration; usually one uses $(\hat U_1,\hat U_2)$, or $(\hat V_1,\hat V_2)$, the coordinates in which the association between the two sets is strongest.

**Example 9.3.2 (Images and Texts)** From the COCO image data set, $100$ images with captions were sampled at random. Each image was transformed into $21$ visual features $\boldsymbol{x}^{(1)}$ and each caption into $20$ text features $\boldsymbol{x}^{(2)}$, the TF–IDF weights (term frequency times $\log(N/n_t)$, where $n_t$ of the $N$ documents contain the term) of the $20$ most frequent words. A large $\hat U_1$ corresponds to images with rich horizontal edges and strong brightness contrast, common in indoor scenes; a large $\hat V_1$ to captions describing indoor, close-up, focused scenes, and a small $\hat V_1$ to outdoor, wide scenes. The scatter plot of $(\hat U_1,\hat V_1)$ separates indoor from outdoor images: CCA has found a common "indoor versus outdoor" dimension in the two modalities. Such shared representations are the basis of cross-modal retrieval (finding images for a text query and vice versa).

### 9.3.3. Matrices of Approximation Errors

How much of the sample covariance structure do the first $r$ canonical pairs reproduce? Extend $\hat B$ to an invertible $q\times q$ matrix by $q-p$ further rows that are $S_{22}$-orthonormal to the first $p$, so that $\hat{\boldsymbol{U}}=\hat A\boldsymbol{x}^{(1)}$ and $\hat{\boldsymbol{V}}=\hat B\boldsymbol{x}^{(2)}$ can be inverted: $\boldsymbol{x}^{(1)}=\hat A^{-1}\hat{\boldsymbol{U}}$ and $\boldsymbol{x}^{(2)}=\hat B^{-1}\hat{\boldsymbol{V}}$ (after centering). Write the columns as $\hat A^{-1}=[\hat{\boldsymbol{a}}^{(1)},\dots,\hat{\boldsymbol{a}}^{(p)}]$ and $\hat B^{-1}=[\hat{\boldsymbol{b}}^{(1)},\dots,\hat{\boldsymbol{b}}^{(q)}]$. Since the sample canonical variates are uncorrelated with unit variances and $\widehat{\operatorname{Cov}}(\hat U_k,\hat V_k)=\hat\rho_k^*$,

$$
S_{11}=\sum_{k=1}^p\hat{\boldsymbol{a}}^{(k)}\hat{\boldsymbol{a}}^{(k)\mathsf T},\qquad S_{22}=\sum_{k=1}^q\hat{\boldsymbol{b}}^{(k)}\hat{\boldsymbol{b}}^{(k)\mathsf T},\qquad S_{12}=\sum_{k=1}^p\hat\rho_k^*\,\hat{\boldsymbol{a}}^{(k)}\hat{\boldsymbol{b}}^{(k)\mathsf T}.
$$
If only the first $r$ pairs are used, $\tilde{\boldsymbol{x}}^{(1)}=[\hat{\boldsymbol{a}}^{(1)},\dots,\hat{\boldsymbol{a}}^{(r)},\boldsymbol{0},\dots,\boldsymbol{0}]\hat{\boldsymbol{U}}$ and $\tilde{\boldsymbol{x}}^{(2)}=[\hat{\boldsymbol{b}}^{(1)},\dots,\hat{\boldsymbol{b}}^{(r)},\boldsymbol{0},\dots,\boldsymbol{0}]\hat{\boldsymbol{V}}$, and the matrices of errors of approximation are

$$
\begin{aligned}
S_{11}-\big(\hat{\boldsymbol{a}}^{(1)}\hat{\boldsymbol{a}}^{(1)\mathsf T}+\cdots+\hat{\boldsymbol{a}}^{(r)}\hat{\boldsymbol{a}}^{(r)\mathsf T}\big)&=\hat{\boldsymbol{a}}^{(r+1)}\hat{\boldsymbol{a}}^{(r+1)\mathsf T}+\cdots+\hat{\boldsymbol{a}}^{(p)}\hat{\boldsymbol{a}}^{(p)\mathsf T},\\
S_{22}-\big(\hat{\boldsymbol{b}}^{(1)}\hat{\boldsymbol{b}}^{(1)\mathsf T}+\cdots+\hat{\boldsymbol{b}}^{(r)}\hat{\boldsymbol{b}}^{(r)\mathsf T}\big)&=\hat{\boldsymbol{b}}^{(r+1)}\hat{\boldsymbol{b}}^{(r+1)\mathsf T}+\cdots+\hat{\boldsymbol{b}}^{(q)}\hat{\boldsymbol{b}}^{(q)\mathsf T},\\
S_{12}-\big(\hat\rho_1^*\hat{\boldsymbol{a}}^{(1)}\hat{\boldsymbol{b}}^{(1)\mathsf T}+\cdots+\hat\rho_r^*\hat{\boldsymbol{a}}^{(r)}\hat{\boldsymbol{b}}^{(r)\mathsf T}\big)&=\hat\rho_{r+1}^*\hat{\boldsymbol{a}}^{(r+1)}\hat{\boldsymbol{b}}^{(r+1)\mathsf T}+\cdots+\hat\rho_p^*\hat{\boldsymbol{a}}^{(p)}\hat{\boldsymbol{b}}^{(p)\mathsf T}.
\end{aligned}
$$
These are descriptive summaries of how well the first $r$ canonical variates reproduce the sample covariance matrices. Usually $S_{12}$ is reproduced best, because its error terms are weighted by the small remaining canonical correlations; $S_{11}$ and $S_{22}$ may be reproduced poorly, since the canonical coefficient vectors are chosen to maximize correlations, not to account for the variation within each set.

A single-number summary is the proportion of the total sample variance of the first set explained by the first $r$ canonical variates,

$$
\frac{\sum_{k=1}^r\hat{\boldsymbol{a}}^{(k)\mathsf T}\hat{\boldsymbol{a}}^{(k)}}{\operatorname{tr}(S_{11})},
$$
and similarly for the second set. For standardized variables, $\hat{\boldsymbol{a}}^{(k)}$ is the vector of correlations between $\hat U_k$ and the variables of the first set, and the denominator is $p$. The proportion indicates how well the canonical variates represent their own set.

## 9.4. Large-Sample Inference

If $\Sigma_{12}=O$, all canonical correlations are zero and CCA is meaningless, so this hypothesis should be tested first. Suppose

$$
\begin{bmatrix}\boldsymbol{X}^{(1)}\\\boldsymbol{X}^{(2)}\end{bmatrix}\sim\mathcal{N}_{p+q}\left(\begin{bmatrix}\boldsymbol{\mu}^{(1)}\\\boldsymbol{\mu}^{(2)}\end{bmatrix},\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}\right),\qquad\rho_1^*\ge\rho_2^*\ge\cdots\ge\rho_p^*.
$$

**Theorem 9.4.1** For testing $H_0\colon\rho_1^*=\cdots=\rho_p^*=0$ (equivalently $\Sigma_{12}=O$) against $H_1$: some $\rho_i^*\ne0$, the **likelihood ratio test** statistic is

$$
-2\log\Lambda=n\log\frac{\lvert S_{11}\rvert\lvert S_{22}\rvert}{\lvert S\rvert}=-n\log\prod_{i=1}^p\big(1-\hat\rho_i^{*2}\big),
$$
which for large $n$ is approximately $\chi^2_{pq}$ under $H_0$; the degrees of freedom $pq$ equal the number of entries of $\Sigma_{12}$.

The key step is a determinant identity, stated with population notation (the sample version is identical). By the **Schur complement** formula,

$$
\lvert\Sigma\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}\rvert\,\lvert I_q-\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1/2}\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}\rvert\,\lvert I_q-Y^{\mathsf T}Y\rvert.
$$
With $Y=P_1\Lambda P_2^{\mathsf T}$, $\lvert I_q-Y^{\mathsf T}Y\rvert=\lvert P_2(I_q-\Lambda^{\mathsf T}\Lambda)P_2^{\mathsf T}\rvert=\lvert I_q-\Lambda^{\mathsf T}\Lambda\rvert=\prod_{i=1}^p(1-\rho_i^{*2})$. Under $H_0$ the maximum likelihood estimate of $\Sigma$ is block diagonal, which gives the ratio of determinants.

If $H_0$ is rejected, one asks how many canonical correlations are nonzero. For $H_0^{(k)}\colon\rho_1^*\ne0,\dots,\rho_k^*\ne0,\ \rho_{k+1}^*=\cdots=\rho_p^*=0$ against $H_1^{(k)}$: $\rho_i^*\ne0$ for some $i\ge k+1$, the likelihood ratio statistic is

$$
-2\log\Lambda=-n\log\prod_{i=k+1}^p\big(1-\hat\rho_i^{*2}\big)\ \overset{\cdot}{\sim}\ \chi^2_{(p-k)(q-k)}.
$$
The tests are applied sequentially for $k=0,1,2,\dots$ until $H_0^{(k)}$ is not rejected. Bartlett's correction replaces $n$ by $n-1-\frac12(p+q+1)$ and improves the approximation; software often reports Wilks' statistic $\prod_{i>k}(1-\hat\rho_i^{*2})$ with an $F$ approximation (Rao's $F$) instead.

**Example 9.4.1 (Salespeople Data, Continued)** With $n=50$, $p=3$ and $q=4$, the products $\prod_{i>k}(1-\hat\rho_i^{*2})$ are $0.0021$, $0.195$ and $0.853$ for $k=0,1,2$. With Bartlett's correction the statistics are $276.4$ ($12$ degrees of freedom), $73.5$ ($6$) and $7.16$ ($2$), with $p$-values $<10^{-15}$, $8\times10^{-14}$ and $0.028$; Rao's $F$ approximation gives the same conclusions. At level $0.05$, even the third canonical correlation $0.384$ is significant.

## 9.5. Extensions

- *Probabilistic CCA* (F. Bach and M. Jordan, 2005) is a latent variable model in the spirit of factor analysis: $\boldsymbol{X}=W_1\boldsymbol{Z}+\boldsymbol{\mu}_1+\boldsymbol{\varepsilon}_1$, $\boldsymbol{Y}=W_2\boldsymbol{Z}+\boldsymbol{\mu}_2+\boldsymbol{\varepsilon}_2$ with a shared $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},I_k)$ and $\boldsymbol{\varepsilon}_i\sim\mathcal{N}(\boldsymbol{0},\Psi_i)$; its maximum likelihood estimates recover the canonical directions, and it extends to conditional generative models.
- *Kernel CCA* (S. Akaho, 2006) maps both sets into reproducing kernel Hilbert spaces, as kernel PCA does in [3.4.6](/3.4.6), to capture nonlinear associations.
- *Sparse CCA* (D. Witten, R. Tibshirani and T. Hastie, 2009) adds $\ell_1$ penalties to the coefficient vectors through a penalized matrix decomposition, so that each canonical variate involves only a few variables, which is essential when $p$ and $q$ exceed $n$.
- *Deep CCA* (G. Andrew, R. Arora, J. Bilmes and K. Livescu, 2013) maximizes $\operatorname{Corr}\big(f(\boldsymbol{X};\theta_f),g(\boldsymbol{Y};\theta_g)\big)$ over two neural networks $f$ and $g$.

## Summary

- Motivation: describe the association $\Sigma_{12}$ between two sets of variables by a few pairs of linear combinations, reducing $pq$ cross-covariances to $p$ canonical correlations ($p\le q$).
- Solution: the key matrix is $Y=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}$, the key tool its singular value decomposition (or the maximization of a Rayleigh quotient), the key idea successive maximization: $\rho_k^*$ is the $k$-th singular value of $Y$, $\boldsymbol{a}_k=\Sigma_{11}^{-1/2}\boldsymbol{e}_k$, $\boldsymbol{b}_k=\Sigma_{22}^{-1/2}\boldsymbol{f}_k$, and $\operatorname{Cov}(\boldsymbol{U},\boldsymbol{V})=\operatorname{diag}(\rho_k^*)$ with $\operatorname{Cov}(\boldsymbol{U})=\operatorname{Cov}(\boldsymbol{V})=I_p$.
- Interpretation: canonical coefficients (multivariate, given the other variables) versus correlations between variates and variables (univariate); $\rho_k^{*2}$ is the shared variance; geometrically, the $\rho_k^*$ are cosines of the principal angles between the two spans; $\rho_1^*$ generalizes the simple and the multiple correlation.
- Invariance: the canonical correlations and variates are unchanged by invertible linear transformations of each set (in particular by standardization); the coefficients transform as $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$.
- Application: sample CCA replaces $\Sigma$ by $S$ (or $\rho$ by $R$); plots of variables by their correlations with the variates (population level) and of units by their scores (unit level); the likelihood ratio test $-n\log\prod_{i>k}(1-\hat\rho_i^{*2})\overset{\cdot}{\sim}\chi^2_{(p-k)(q-k)}$ decides whether CCA is needed and how many pairs to keep.
