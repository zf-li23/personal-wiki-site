---
title: Extra Sums of Squares and General Linear Tests
description: Extra sums of squares and the three types of sums of squares, the general linear test for nested models and linear hypotheses, coefficients of partial determination and partial correlation with the Frisch–Waugh–Lovell theorem, the standardized regression model, and suppressor variables.
---

In a multiple regression the regression sum of squares measures what all the explanatory variables explain together. To judge a single variable or a group of variables we need the part of the variation that they explain *in addition to* the other variables. This chapter introduces these extra sums of squares and the three ways (Types I, II and III) in which software splits the regression sum of squares. The comparison of a full and a reduced model, met for simple regression in [3.3.4](/3.3.4) and used informally in [3.3.8](/3.3.8), then becomes the general linear test, which covers single coefficients, groups of coefficients and arbitrary linear hypotheses. Dividing an extra sum of squares by the variation still unexplained gives the coefficient of partial determination, whose square root is the partial correlation; the Frisch–Waugh–Lovell theorem shows that both come from a regression of residuals on residuals. The chapter ends with the standardized regression model, which makes coefficients comparable, and with suppressor variables, which explain why a variable can matter more in the presence of another one. Correlated explanatory variables, the cause of most of the phenomena seen here, are studied in [3.3.10](/3.3.10).

## 9.1. Extra Sums of Squares

### 9.1.1. Definition

When we add explanatory variables to a model we hope to explain more of the variability of the response and thereby reduce the error. An extra sum of squares quantifies this gain, either as the increase of the regression sum of squares $\mathrm{SSR}$ or, equivalently, as the reduction of the error sum of squares $\mathrm{SSE}$; the two agree because $\mathrm{SSR}+\mathrm{SSE}=\mathrm{SSTO}$ does not depend on the model. We write $\mathrm{SSR}(X_1,X_2)$ and $\mathrm{SSE}(X_1,X_2)$ for the sums of squares of the model containing $X_1$ and $X_2$ (and an intercept).

**Definition 9.1.1 (Extra Sum of Squares)** For two disjoint sets of explanatory variables $A$ and $B$, the **extra sum of squares** of $A$ given $B$ is

$$
\mathrm{SSR}(A\mid B)=\mathrm{SSR}(A,B)-\mathrm{SSR}(B)=\mathrm{SSE}(B)-\mathrm{SSE}(A,B),
$$
the additional variation explained by $A$ when it is added to a model that already contains $B$. Its degrees of freedom are the number of variables in $A$.

For instance, $\mathrm{SSR}(X_1,X_2,X_3)$ is the total variation explained by $X_1,X_2,X_3$; $\mathrm{SSR}(X_1\mid X_2)=\mathrm{SSE}(X_2)-\mathrm{SSE}(X_1,X_2)$ is the additional variation explained by $X_1$ when added to a model containing $X_2$; and

$$
\mathrm{SSR}(X_1,X_4\mid X_2,X_3)=\mathrm{SSR}(X_1,X_2,X_3,X_4)-\mathrm{SSR}(X_2,X_3)=\mathrm{SSE}(X_2,X_3)-\mathrm{SSE}(X_1,X_2,X_3,X_4)
$$
is the part of $\mathrm{SSE}(X_2,X_3)$ that is explained by $X_1$ and $X_4$ and was not explained by $X_2$ and $X_3$.

**Example 9.1.1 (Body Fat)** For $20$ healthy women, the body fat $Y$ (measured by the expensive gold standard of underwater weighing) is to be predicted from three cheap body measurements: triceps skinfold thickness $X_1$, thigh circumference $X_2$ and midarm circumference $X_3$. The total sum of squares is $\mathrm{SSTO}=495.39$, and

| model | $\mathrm{SSR}$ | $\mathrm{SSE}$ |
|---|---|---|
| $X_1$ | $352.27$ | $143.12$ |
| $X_2$ | $381.97$ | $113.42$ |
| $X_1,X_2$ | $385.44$ | $109.95$ |
| $X_1,X_2,X_3$ | $396.98$ | $98.41$ |

Hence $\mathrm{SSR}(X_2\mid X_1)=143.12-109.95=33.17$, whereas $\mathrm{SSR}(X_1\mid X_2)=113.42-109.95=3.47$, and $\mathrm{SSR}(X_3\mid X_1,X_2)=109.95-98.41=11.54$. Skinfold explains much on its own ($352.27$) but almost nothing once thigh is in the model ($3.47$): the two measurements carry nearly the same information.

![The total sum of squares 495.39 of the body fat data split in two orders: X1 first gives SSR(X1) = 352.27 and SSR(X2 | X1) = 33.17, X2 first gives SSR(X2) = 381.97 and SSR(X1 | X2) = 3.47; in both orders SSE(X1, X2) = 109.95](./plots/extra-ss-bars.py)

### 9.1.2. Three Types of Sums of Squares

The **analysis of variance** splits the total variation of the response into sources in order to judge the effect of each explanatory variable. For $Y\sim X_1+X_2+X_3+X_4$ we have $\mathrm{SSTO}=\mathrm{SSR}(X_1,\dots,X_4)+\mathrm{SSE}(X_1,\dots,X_4)$, but how should $\mathrm{SSR}(X_1,\dots,X_4)$ be attributed to the individual variables? There are three common answers.

**Definition 9.1.2 (Types of Sums of Squares)** In a model with terms $T_1,\dots,T_m$ (variables, or groups such as interactions),

1. the **sequential sums of squares** (Type I) add the terms one at a time in the order specified: $\mathrm{SSR}(T_1)$, $\mathrm{SSR}(T_2\mid T_1)$, $\mathrm{SSR}(T_3\mid T_1,T_2)$, and so on;
2. the Type II sum of squares of a term is its extra sum of squares given all other terms except those that contain it (such as its interactions);
3. the Type III sum of squares of a term is its extra sum of squares given all other terms, that is, the term is added last.

Only the sequential sums of squares add up to the regression sum of squares:

$$
\mathrm{SSR}(X_1,X_2,X_3,X_4)=\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2\mid X_1)+\mathrm{SSR}(X_3\mid X_1,X_2)+\mathrm{SSR}(X_4\mid X_1,X_2,X_3).
$$
This is the "extended" ANOVA table printed by `anova()` in R: the single regression row is replaced by $p-1$ rows, one per variable, each with one degree of freedom and the statistic $F^*=\mathrm{SSR}(X_k\mid X_1,\dots,X_{k-1})/\mathrm{MSE}\overset{H_0}{\sim}F_{1,n-p}$, where $\mathrm{MSE}$ is that of the full model. The order matters: whoever enters first collects the variation shared with later variables.

For two factors $A$, $B$ and their interaction $AB$ the three types are

| term | Type I | Type II | Type III |
|---|---|---|---|
| $A$ | $\mathrm{SSR}(A)$ | $\mathrm{SSR}(A\mid B)$ | $\mathrm{SSR}(A\mid B,AB)$ |
| $B$ | $\mathrm{SSR}(B\mid A)$ | $\mathrm{SSR}(B\mid A)$ | $\mathrm{SSR}(B\mid A,AB)$ |
| $AB$ | $\mathrm{SSR}(AB\mid A,B)$ | $\mathrm{SSR}(AB\mid A,B)$ | $\mathrm{SSR}(AB\mid A,B)$ |

Type II assumes that there is no significant interaction when it assesses the main effects. Consequently:

- reordering the variables in the model changes the Type I sums of squares but not the Type II or Type III sums of squares;
- in a model without interaction terms, Types II and III coincide and are the variable-added-last sums of squares that underlie the $t$-tests;
- for orthogonal explanatory variables (and for balanced designs in the analysis of variance) all three types coincide; with correlated variables or unbalanced data they can differ greatly.

In R, `anova()` gives Type I, and `Anova()` of the package car gives Type II by default and Type III with `type = "III"`; SAS and SPSS report Type III by default. Which one to use? Type I is appropriate when there is a substantive reason to give one variable priority (for example, to show the effect of a specific variable after controlling for established ones, entering it last). Otherwise use Type II when no interaction is expected and Type III when there is one. Testing main effects in the presence of an interaction, as Type III does, violates the *marginality principle* of the design of experiments: a main effect averaged over the levels of a factor with which it interacts is rarely meaningful ([3.3.14](/3.3.14)). Type III results also depend on how the factors are coded.

## 9.2. The General Linear Test

### 9.2.1. Full and Reduced Models

The general linear test of [3.3.4](/3.3.4) compares two models: the full model containing all the variables (parameters), and the reduced model obtained by applying the null hypothesis to the full model. The models are *nested*: the full model contains all the explanatory variables of the reduced model. For instance, $\{X_1,\dots,X_5\}$ contains $\{X_1,X_2,X_3\}$, which contains $\{X_1,X_2\}$. The test looks at the difference in $\mathrm{SSE}$ (equivalently in $\mathrm{SSR}$) between the two models.

**Definition 9.2.1 (General Linear Test)** Let the reduced model $R$ be nested in the full model $F$, with error sums of squares $\mathrm{SSE}(R)\ge\mathrm{SSE}(F)$ and error degrees of freedom $\mathrm{df}_E(R)>\mathrm{df}_E(F)$. The **general linear test** of $H_0$: the reduced model holds, against $H_1$: the full model holds, uses the *partial $F$-statistic*

$$
F^*=\frac{\big(\mathrm{SSE}(R)-\mathrm{SSE}(F)\big)/\big(\mathrm{df}_E(R)-\mathrm{df}_E(F)\big)}{\mathrm{SSE}(F)/\mathrm{df}_E(F)}
$$
and rejects $H_0$ for large values of $F^*$.

**Theorem 9.2.1** Under the normal full model and $H_0$, $F^*\sim F_{\mathrm{df}_E(R)-\mathrm{df}_E(F),\ \mathrm{df}_E(F)}$.

**Proof** Let $H_R$ and $H_F$ be the hat matrices; $\mathcal{R}(X_R)\subseteq\mathcal{R}(X_F)$ gives $H_FH_R=H_R$, so $H_F-H_R$ is symmetric and idempotent of rank $q=\mathrm{df}_E(R)-\mathrm{df}_E(F)$, and $(I_n-H_F)(H_F-H_R)=O$. Now $\mathrm{SSE}(R)-\mathrm{SSE}(F)=\boldsymbol{Y}^{\mathsf T}(H_F-H_R)\boldsymbol{Y}$ and $\mathrm{SSE}(F)=\boldsymbol{Y}^{\mathsf T}(I_n-H_F)\boldsymbol{Y}$. Under $H_0$, $\mathbb{E}(\boldsymbol{Y})\in\mathcal{R}(X_R)$ is annihilated by both matrices, so by Lemma 8.2.1 of [3.3.8](/3.3.8) the two quadratic forms divided by $\sigma^2$ are $\chi^2_q$ and $\chi^2_{\mathrm{df}_E(F)}$; they are independent because $(H_F-H_R)\boldsymbol{Y}$ and $(I_n-H_F)\boldsymbol{Y}$ are jointly normal and uncorrelated. $\square$

The numerator degrees of freedom are the number of *extra* variables, and the denominator degrees of freedom are those of the larger model. For example, with $n=100$ and the comparison of $X_1,\dots,X_5$ with $X_1,X_2,X_3$, that is, $H_0\colon\beta_4=\beta_5=0$ against $H_1$: at least one of $\beta_4,\beta_5$ is nonzero,

$$
F^*=\frac{\mathrm{SSR}(X_4,X_5\mid X_1,X_2,X_3)/2}{\mathrm{SSE}(X_1,\dots,X_5)/(n-6)}\overset{H_0}{\sim}F_{2,94}.
$$
Rejecting $H_0$ (say, $p$-value $\le0.05$) means that $X_4$ or $X_5$ or both contain additional information useful for predicting $Y$ in a linear model that already includes $X_1,X_2,X_3$.

Since $\mathrm{SSTO}$ is the same for both models, the statistic can also be written with the coefficients of multiple determination,

$$
F^*=\frac{\big(R^2(F)-R^2(R)\big)/\big(\mathrm{df}_E(R)-\mathrm{df}_E(F)\big)}{\big(1-R^2(F)\big)/\mathrm{df}_E(F)}.
$$

### 9.2.2. Special Cases

**Proposition 9.2.1** Let $c_{kk}=[(X^{\mathsf T}X)^{-1}]_{kk}$ be the diagonal entry of the full model belonging to $\beta_k$. Then

$$
\mathrm{SSR}(X_k\mid X_1,\dots,X_{k-1},X_{k+1},\dots,X_{p-1})=\frac{b_k^2}{c_{kk}},
$$
so the general linear test of $H_0\colon\beta_k=0$ has $F^*=b_k^2/(c_{kk}\,\mathrm{MSE})=(t^*)^2$, the square of the $t$-statistic of [3.3.8](/3.3.8), and $F_{1,n-p}=t_{n-p}^2$: the two tests are equivalent.

**Proof** Order the columns as $X=(X_{-k},\boldsymbol{x}_k)$, let $H_{-k}$ be the hat matrix of $X_{-k}$ and $\tilde{\boldsymbol{x}}=(I_n-H_{-k})\boldsymbol{x}_k$ the residual of $\boldsymbol{x}_k$ regressed on the other columns. The column space of $X$ is the orthogonal sum of $\mathcal{R}(X_{-k})$ and the line spanned by $\tilde{\boldsymbol{x}}$, so $H=H_{-k}+\tilde{\boldsymbol{x}}\tilde{\boldsymbol{x}}^{\mathsf T}/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$ and

$$
\mathrm{SSE}(X_{-k})-\mathrm{SSE}(X)=\boldsymbol{Y}^{\mathsf T}(H-H_{-k})\boldsymbol{Y}=\frac{(\tilde{\boldsymbol{x}}^{\mathsf T}\boldsymbol{Y})^2}{\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}}}.
$$
By Theorem 9.3.1 below, $b_k=\tilde{\boldsymbol{x}}^{\mathsf T}\boldsymbol{Y}/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$, and by the block inversion formula (the **Schur complement** of $X_{-k}^{\mathsf T}X_{-k}$ in $X^{\mathsf T}X$), $c_{kk}=\big(\boldsymbol{x}_k^{\mathsf T}\boldsymbol{x}_k-\boldsymbol{x}_k^{\mathsf T}H_{-k}\boldsymbol{x}_k\big)^{-1}=1/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$. Hence the extra sum of squares equals $b_k^2\,\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}}=b_k^2/c_{kk}$. $\square$

This identity also completes the proof in [3.2.5](/3.2.5) that the likelihood ratio test of a single coefficient is the $t$-test. At the other extreme, for $H_0\colon\beta_1=\cdots=\beta_{p-1}=0$ the reduced model contains only the intercept, $\mathrm{SSE}(R)=\mathrm{SSTO}$, and the general linear test is the overall ANOVA $F$-test.

### 9.2.3. Example: Body Fat

```r
reg1 <- lm(fat ~ skinfold + thigh + midarm, data = a1)
summary(reg1)
anova(reg1)                      # Type I (sequential) sums of squares
library(car)
Anova(reg1, type = "II")         # Type II
Anova(reg1, type = "III")        # Type III
drop1(reg1, test = "F")          # each variable deleted from the full model
```

**Example 9.2.1 (Body Fat, Continued)** The fit of the full model and the sums of squares are

| | estimate | std. error | $t$ | $p$-value | Type I SS | Type II/III SS |
|---|---|---|---|---|---|---|
| intercept | $117.085$ | $99.782$ | $1.17$ | $0.258$ | | |
| skinfold $X_1$ | $4.334$ | $3.016$ | $1.44$ | $0.170$ | $352.27$ | $12.705$ |
| thigh $X_2$ | $-2.857$ | $2.582$ | $-1.11$ | $0.285$ | $33.17$ | $7.529$ |
| midarm $X_3$ | $-2.186$ | $1.595$ | $-1.37$ | $0.190$ | $11.55$ | $11.546$ |

with $\mathrm{SSE}=98.40$ on $16$ degrees of freedom ($\mathrm{MSE}=6.15$, $s=2.48$), $R^2=0.8014$, $R_a^2=0.7641$, and $F^*=21.52$ on $(3,16)$ degrees of freedom ($p=7.3\times10^{-6}$). The set of variables as a whole is very helpful, but no single variable is significant. The Type I sums of squares are large for skinfold and thigh, which enter first, while the Type II and III sums of squares (equal here, as there is no interaction) are small for both: each adds little once the others are present.

The marginal correlations with fat are $0.843$ (skinfold), $0.878$ (thigh) and $0.142$ (midarm, $p=0.55$). Should we drop midarm, the least correlated variable, and regard thigh as the most important one? Not on this evidence: the marginal correlations ignore the relations among the explanatory variables. To assess midarm we compare the full model with the model without it:

```r
reg3 <- lm(fat ~ skinfold + thigh, data = a1)
anova(reg3, reg1)    # general linear test of H0: beta_3 = 0
```

This gives $\mathrm{SSR}(X_3\mid X_1,X_2)=109.951-98.405=11.546$ on $1$ degree of freedom, $F^*=11.546/6.150=1.877$ and $p=0.190$, exactly the $t$-test of midarm in the full model ($(-1.370)^2=1.877$). With skinfold and thigh in the model, midarm is not a significant predictor.

The interpretation needs care. The $t$-test assesses the significance of $X_3$ *after* $X_1$ and $X_2$ have been taken into account; it does not test the relationship between $Y$ and $X_3$ alone. This is the meaning of the **partial regression coefficient** $\beta_3$: the change in $\mathbb{E}(Y)$ per unit increase of $X_3$ when the other variables are held constant. The partial $F$-test of a subset and the overall $F$-test answer different questions.

Skinfold alone is a highly significant linear predictor: $\hat Y=-1.496+0.857X_1$ with $t=6.66$, $R^2=0.711$ and $\mathrm{SSE}=143.12$ on $18$ degrees of freedom. Do the other two variables contribute beyond skinfold? The general linear test of $H_0\colon\beta_2=\beta_3=0$ gives $\mathrm{SSR}(X_2,X_3\mid X_1)=143.120-98.405=44.715$ on $2$ degrees of freedom, $F^*=(44.715/2)/6.150=3.635$ and $p=0.0500$: they do help, borderline. Perhaps the best model contains two predictors ([3.3.10](/3.3.10)).

Two practical notes. Usually the alternative hypothesis is just that at least one variable of the null group matters, and often we hope to fail to reject, because the goal is to eliminate unnecessary variables. Then power and sample size are essential: with a small sample we may wrongly remove variables. In Example 8.1.1 of [3.3.8](/3.3.8), with $n=224$, the $p$-value $0.436$ for adding hss, satm and satv to hsm and hse justifies discarding them.

### 9.2.4. Linear Hypotheses

The general linear test applies to any hypothesis about linear combinations of the coefficients. In the body fat model, $H_0\colon\beta_2=\beta_3$ leads to the reduced model $Y=\beta_0+\beta_1X_1+\beta_c(X_2+X_3)+\varepsilon$, and $H_0\colon\beta_2=2$ to the reduced model with the known term $2X_2$ moved to the left side (an offset):

```r
glt1 <- lm(fat ~ skinfold + I(thigh + midarm), data = a1)
anova(glt1, reg1)                                    # H0: beta_2 = beta_3
glt2 <- lm(fat ~ skinfold + offset(2 * thigh) + midarm, data = a1)
anova(glt2, reg1)                                    # H0: beta_2 = 2
linearHypothesis(reg1, "thigh - 3*midarm = 12")      # package car
```

In general, a set of $q$ linear restrictions is written as $H_0\colon C\boldsymbol{\beta}=\boldsymbol{t}$, where $C$ is a $q\times p$ matrix of rank $q$ (the number of linearly independent restrictions) and $\boldsymbol{t}\in\mathbb{R}^q$.

**Theorem 9.2.2** Under the normal linear model and $H_0\colon C\boldsymbol{\beta}=\boldsymbol{t}$,

$$
F^*=\frac{(C\boldsymbol{b}-\boldsymbol{t})^{\mathsf T}\big(C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)^{-1}(C\boldsymbol{b}-\boldsymbol{t})}{q\,s^2}\sim F_{q,n-p},
$$
and the numerator $q\,s^2F^*$ equals $\mathrm{SSE}(R)-\mathrm{SSE}(F)$, where $R$ is the model fitted under the restriction.

**Proof** By Theorem 8.2.1 of [3.3.8](/3.3.8), $C\boldsymbol{b}-\boldsymbol{t}\sim\mathcal{N}_q\big(\boldsymbol{0},\sigma^2C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)$ under $H_0$, so the quadratic form in the numerator divided by $\sigma^2$ is $\chi^2_q$; it is a function of $\boldsymbol{b}$ and hence independent of $(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$. That the numerator is the increase of $\mathrm{SSE}$ follows by minimizing $\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2$ subject to $C\boldsymbol{\beta}=\boldsymbol{t}$ with a Lagrange multiplier. $\square$

**Example 9.2.2** For the body fat model with $\boldsymbol{\beta}=(\beta_0,\beta_1,\beta_2,\beta_3)^{\mathsf T}$, the hypothesis $H_0\colon\beta_2-3\beta_3=12$ has $\mathrm{SSE}(R)=182.953$ on $17$ degrees of freedom, so $F^*=(182.953-98.405)/6.150=13.75$ on $(1,16)$ degrees of freedom and $p=0.0019$. The two restrictions $\beta_2=\beta_3$ and $\beta_2-3\beta_3=12$ together correspond to

$$
C=\begin{bmatrix}0&0&1&-1\\0&0&1&-3\end{bmatrix},\qquad\boldsymbol{t}=\begin{bmatrix}0\\12\end{bmatrix},\qquad q=2,
$$
and give $\mathrm{SSE}(R)=816.2$ on $18$ degrees of freedom, $F^*=58.35$ on $(2,16)$ degrees of freedom, $p=4.5\times10^{-8}$:

```r
C <- matrix(c(0, 0, 1, -1,
              0, 0, 1, -3), byrow = TRUE, nrow = 2)
linearHypothesis(reg1, hypothesis.matrix = C, rhs = c(0, 12))
```

The statistic of Theorem 9.2.2 is the same quadratic form as in the $F$-test of [3.4.7](/3.4.7) and has the structure of Hotelling's $T^2$: a squared distance of $C\boldsymbol{b}$ from $\boldsymbol{t}$ in the metric of its estimated covariance matrix.

## 9.3. Partial Determination and Partial Correlation

### 9.3.1. Coefficients of Partial Determination

The coefficient of multiple determination $R^2=\mathrm{SSR}(X_1,\dots,X_{p-1})/\mathrm{SSTO}$ is the proportion of the total variation explained by the model, the proportionate reduction of the variation of $Y$ achieved by the entire set of explanatory variables. A coefficient of partial determination measures instead the marginal contribution of one variable when all others are already in the model: the proportion of the *remaining* variation that it explains.

**Definition 9.3.1 (Coefficient of Partial Determination)** The **coefficient of partial determination** of $Y$ and $X_k$ given the other variables $X_{-k}=\{X_j\colon j\ne k\}$ is

$$
R^2_{Yk\mid-k}=\frac{\mathrm{SSR}(X_k\mid X_{-k})}{\mathrm{SSE}(X_{-k})}=\frac{\mathrm{SSE}(X_{-k})-\mathrm{SSE}(X_1,\dots,X_{p-1})}{\mathrm{SSE}(X_{-k})}\in[0,1].
$$
The variables after the bar are those controlled for; for instance $R^2_{Y1\mid23}=\mathrm{SSR}(X_1\mid X_2,X_3)/\mathrm{SSE}(X_2,X_3)$. The same definition applies to a group of variables, and in the analysis of variance the quantity is called the partial $\eta^2$.

In a Venn diagram with circles for $Y$, $X_1$ and $X_2$, let $A$ be the part of $Y$ shared only with $X_1$, $B$ the part shared only with $X_2$, $C$ the part shared with both and $D$ the part shared with neither. Then $R^2=(A+B+C)/(A+B+C+D)$, $R^2_{Y1\mid2}=A/(A+D)$ and $R^2_{Y2\mid1}=B/(B+D)$: the overlap $C$ counts for the model but for neither partial coefficient. (The picture is only a heuristic; with suppressor variables, Section 9.4.3, the overlap would have to be negative.)

**Example 9.3.1** In Example 8.1.1 of [3.3.8](/3.3.8), the sequential sums of squares of the model gpa $\sim$ hsm + hss + hse are $25.810$, $1.237$, $0.665$, with $\mathrm{SSE}=107.750$. Hence

$$
R^2_{\text{gpa, hse}\mid\text{hsm, hss}}=\frac{0.665}{0.665+107.750}=0.0061:
$$
hse explains $0.6\%$ of the variation left after hsm and hss. Similarly, if $\mathrm{SSTO}=100$, $X_1$ explains $60$, $X_2$ explains $20$ of the remaining $40$ and $X_3$ explains $5$ of the remaining $20$, then $R^2_{Y2\mid1}=20/40=0.5$ and $R^2_{Y3\mid12}=5/20=0.25$.

By Definition 9.2.1, for $H_0\colon\beta_k=0$ the partial $F$-statistic is a monotone function of the partial coefficient: $F^*=\dfrac{R^2_{Yk\mid-k}}{1-R^2_{Yk\mid-k}}\cdot(n-p)$.

The coefficient of partial determination has a direct interpretation as an ordinary $R^2$. Write $Y\mid X_{-k}$ for the residuals of the regression of $Y$ on $X_{-k}$ and $X_k\mid X_{-k}$ for the residuals of the regression of $X_k$ on $X_{-k}$: the parts of $Y$ and of $X_k$ that the other variables cannot explain.

**Theorem 9.3.1 (Frisch–Waugh–Lovell Theorem)** Partition $X=(X_1,X_2)$ by columns, where $X_1$ contains the intercept, and let $M_1=I_n-X_1(X_1^{\mathsf T}X_1)^{-1}X_1^{\mathsf T}$. The least squares coefficients $\boldsymbol{b}_2$ of $X_2$ in the regression of $\boldsymbol{Y}$ on $X$ equal the coefficients of the regression of the residuals $M_1\boldsymbol{Y}$ on the residuals $M_1X_2$,

$$
\boldsymbol{b}_2=(X_2^{\mathsf T}M_1X_2)^{-1}X_2^{\mathsf T}M_1\boldsymbol{Y},
$$
and the residuals of the two regressions coincide.

**Proof** The columns of $M_1X_2$ are orthogonal to $\mathcal{R}(X_1)$, and $\mathcal{R}(X)=\mathcal{R}(X_1)\oplus\mathcal{R}(M_1X_2)$ is an orthogonal sum. Hence the projection onto $\mathcal{R}(X)$ is $H=H_1+P$, where $H_1=I_n-M_1$ and $P$ projects onto $\mathcal{R}(M_1X_2)$. With $\boldsymbol{c}=(X_2^{\mathsf T}M_1X_2)^{-1}X_2^{\mathsf T}M_1\boldsymbol{Y}$ we get $P\boldsymbol{Y}=M_1X_2\boldsymbol{c}=X_2\boldsymbol{c}-H_1X_2\boldsymbol{c}$, so $H\boldsymbol{Y}=X_1\boldsymbol{a}+X_2\boldsymbol{c}$ for some $\boldsymbol{a}$. Since $X$ has full column rank, the coefficients of $H\boldsymbol{Y}=X\boldsymbol{b}$ are unique, so $\boldsymbol{b}_2=\boldsymbol{c}$. Finally $\boldsymbol{Y}-H\boldsymbol{Y}=M_1\boldsymbol{Y}-P\boldsymbol{Y}=M_1\boldsymbol{Y}-M_1X_2\boldsymbol{c}$, which is the residual vector of the regression of $M_1\boldsymbol{Y}$ on $M_1X_2$. $\square$

**Corollary 9.3.1** The coefficient of partial determination $R^2_{Yk\mid-k}$ is the $R^2$ of the simple regression of $Y\mid X_{-k}$ on $X_k\mid X_{-k}$, and the slope of that regression is $b_k$.

**Proof** Apply Theorem 9.3.1 with $X_2=\boldsymbol{x}_k$. The residuals $M_1\boldsymbol{Y}$ have mean zero (the intercept is in $X_1$), so the total sum of squares of the simple regression is $\|M_1\boldsymbol{Y}\|^2=\mathrm{SSE}(X_{-k})$, and its error sum of squares is the $\mathrm{SSE}$ of the full model. Its $R^2$ is therefore $1-\mathrm{SSE}(X_1,\dots,X_{p-1})/\mathrm{SSE}(X_{-k})=R^2_{Yk\mid-k}$. $\square$

**Example 9.3.2** For the body fat data, the full model gives $b_1=4.334$ for skinfold. Regressing the residuals of fat on thigh and midarm on the residuals of skinfold on thigh and midarm gives the slope $4.334$ and $R^2=0.1143$, which is $R^2_{Y1\mid23}=12.705/111.11$:

```r
fity <- lm(fat ~ thigh + midarm, data = a1)        # Y | X_{-1}
fitx <- lm(skinfold ~ thigh + midarm, data = a1)   # X_1 | X_{-1}
summary(lm(fity$res ~ fitx$res))                   # slope 4.334, R^2 0.1143
cor(fitx$res, fity$res)^2                          # 0.1143
```

The standard error printed by this simple regression ($2.843$) differs slightly from that of the full model ($3.016$), because the simple regression counts $18$ instead of $16$ error degrees of freedom. The partial coefficients of all three variables (`etasq()` in the package heplots) are $0.114$, $0.071$ and $0.105$: skinfold and midarm explain the most remaining variation when added last.

### 9.3.2. Partial Correlation

**Definition 9.3.2 (Partial Correlation Coefficient)** The **partial correlation coefficient** $r_{Yk\mid-k}$ of $Y$ and $X_k$ given $X_{-k}$ is the correlation between the residuals $Y\mid X_{-k}$ and $X_k\mid X_{-k}$. Equivalently, $\lvert r_{Yk\mid-k}\rvert=\sqrt{R^2_{Yk\mid-k}}$ and the sign of $r_{Yk\mid-k}$ is that of $b_k$.

The equivalence is Corollary 9.3.1: in a simple regression, $R^2$ is the squared correlation and the slope has the sign of the correlation. The partial correlation measures the strength of the linear relation between two variables after taking the other variables into account. To compute it, predict $Y$ from the other $X$'s, predict $X_k$ from the other $X$'s, and correlate the two sets of residuals.

For three variables, if $0<r_{12\mid3}<r_{12}$, then variable $3$ partly explains the correlation between variables $1$ and $2$. The opposite case $0<r_{12}<r_{12\mid3}$ also occurs: controlling for variable $3$ strengthens the association, which is the suppression effect of Section 9.4.3.

## 9.4. Standardized Regression

### 9.4.1. The Correlation Transformation

In the Dwaine Studios model $Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\varepsilon_i$ of [3.3.8](/3.3.8), the units of $\beta_1$ (sales per thousand young people) and $\beta_2$ (sales per thousand of income) differ, and their magnitudes depend on the units of $X_1$ and $X_2$; they cannot be compared directly. Moreover, when the explanatory variables differ in magnitude by several orders, computing $(X^{\mathsf T}X)^{-1}$ can be numerically inaccurate. Both problems are solved by **standardization**: centering (subtracting the mean) and scaling (dividing by the standard deviation). This is typically preferred when most of the measures are on arbitrary scales.

**Definition 9.4.1 (Standardized Regression Model)** Let $\bar Y$, $\bar X_k$ be the sample means and $s_Y=\sqrt{\sum_i(Y_i-\bar Y)^2/(n-1)}$, $s_k=\sqrt{\sum_i(X_{ik}-\bar X_k)^2/(n-1)}$ the sample standard deviations. The **correlation transformation** is

$$
Y_i^*=\frac{1}{\sqrt{n-1}}\cdot\frac{Y_i-\bar Y}{s_Y},\qquad X_{ik}^*=\frac{1}{\sqrt{n-1}}\cdot\frac{X_{ik}-\bar X_k}{s_k},\qquad k=1,\dots,p-1,
$$
and the **standardized regression model** is $Y_i^*=\beta_1^*X_{i1}^*+\cdots+\beta_{p-1}^*X_{i,p-1}^*+\varepsilon_i^*$, without intercept. Its coefficients $\beta_k^*$ are the **standardized regression coefficients**.

Subtracting the averaged model $\bar Y=\beta_0+\sum_k\beta_k\bar X_k+\bar\varepsilon$ from the original model and dividing by $\sqrt{n-1}\,s_Y$ gives

$$
Y_i^*=\sum_{k=1}^{p-1}\frac{s_k}{s_Y}\beta_k\,X_{ik}^*+\frac{\varepsilon_i-\bar\varepsilon}{\sqrt{n-1}\,s_Y},\qquad\text{so}\qquad\beta_k^*=\frac{s_k}{s_Y}\beta_k,\quad\beta_0=\bar Y-\sum_{k=1}^{p-1}\beta_k\bar X_k.
$$
The standardized coefficients are unit-free and have the same interpretation, the change in $Y$, in standard deviations, per standard deviation of $X_k$ with the other variables fixed, so they can be compared with each other in an intuitive sense (with the caveats of [3.3.10](/3.3.10) when the variables are correlated).

The name comes from the cross-product matrices. Since $\sum_iX_{ik}^*X_{il}^*=r_{kl}$, the sample correlation of $X_k$ and $X_l$, the design matrix $X^*=(X_{ik}^*)$ of size $n\times(p-1)$ satisfies

$$
X^{*\mathsf T}X^*=r_{XX}=\begin{bmatrix}1&r_{12}&\cdots&r_{1,p-1}\\r_{21}&1&\cdots&r_{2,p-1}\\\vdots&\vdots&\ddots&\vdots\\r_{p-1,1}&r_{p-1,2}&\cdots&1\end{bmatrix},\qquad X^{*\mathsf T}\boldsymbol{Y}^*=\boldsymbol{r}_{YX}=\begin{bmatrix}r_{Y1}\\r_{Y2}\\\vdots\\r_{Y,p-1}\end{bmatrix},
$$
the **sample correlation matrix** of the explanatory variables and the vector of their correlations with $Y$, so $\boldsymbol{b}^*=r_{XX}^{-1}\boldsymbol{r}_{YX}$. All entries lie between $-1$ and $1$, which avoids or mitigates the numerical problems of inverting $X^{\mathsf T}X$.

**Proposition 9.4.1** Standardizing all variables leaves $R^2$, $R_a^2$, the overall $F$-statistic, the $t$-statistics of the slopes and the coefficients of partial determination unchanged; the sums of squares are divided by $(n-1)s_Y^2$. Standardizing only the explanatory variables changes the coefficients ($b_k$ becomes $s_kb_k$, up to the factor $\sqrt{n-1}$) but leaves the ANOVA table and the partial coefficients unchanged.

**Proof** Centering and rescaling the explanatory variables does not change the column space of the design matrix with intercept, hence neither the fitted values nor any sum of squares; rescaling $Y$ by a constant multiplies all sums of squares by its square, which cancels in every ratio. $\square$

This assumes that the standardized model is fitted with an intercept, as `lm()` on standardized data does (the estimated intercept is then $0$). Fitted without intercept, it is credited with one more error degree of freedom, which changes $\mathrm{MSE}$ and the tests very slightly.

For the body fat data, `lm.beta()` of the package QuantPsyc, or `lm()` on `scale(a1)`, gives the standardized coefficients $4.264$, $-2.929$ and $-1.561$; with `scale()` (which omits the factor $1/\sqrt{n-1}$) the sums of squares $352.27$, $33.17$, $11.55$, $98.40$ become $13.51$, $1.27$, $0.44$, $3.77$, which add up to $n-1=19$, while $R^2=0.8014$ and $F^*=21.52$ do not change.

### 9.4.2. Correlation and Partial Correlation

With two explanatory variables, $r_{XX}^{-1}=\frac{1}{1-r_{12}^2}\begin{bmatrix}1&-r_{12}\\-r_{12}&1\end{bmatrix}$, so

$$
b_1^*=\frac{r_{Y1}-r_{12}r_{Y2}}{1-r_{12}^2},\qquad b_2^*=\frac{r_{Y2}-r_{12}r_{Y1}}{1-r_{12}^2},\qquad b_k=\frac{s_Y}{s_k}b_k^*.
$$
Transformed back, $b_1=\Big(\dfrac{\sum_i(X_{i1}-\bar X_1)(Y_i-\bar Y)}{\sum_i(X_{i1}-\bar X_1)^2}-\dfrac{s_Y}{s_1}r_{12}r_{Y2}\Big)\Big/(1-r_{12}^2)$: the simple-regression slope corrected for the correlation of $X_1$ with $X_2$. If $r_{12}=0$, the multiple and simple regression coefficients coincide.

**Proposition 9.4.2** With two explanatory variables,

$$
R^2_{Y2\mid1}=r_{Y2\mid1}^2=\frac{(r_{Y2}-r_{Y1}r_{12})^2}{(1-r_{Y1}^2)(1-r_{12}^2)}.
$$

**Proof** In the correlation-transformed variables the residuals of $Y^*$ and of $X_2^*$ regressed on $X_1^*$ are $\boldsymbol{Y}^*-r_{Y1}\boldsymbol{X}_1^*$ and $\boldsymbol{X}_2^*-r_{12}\boldsymbol{X}_1^*$ (all vectors have length $1$ and mean $0$). Their inner product is $r_{Y2}-r_{Y1}r_{12}$ and their squared lengths are $1-r_{Y1}^2$ and $1-r_{12}^2$; the partial correlation is the cosine of the angle between them (Definition 9.3.2). $\square$

The same formula holds with all subscripts conditioned on further variables, for instance $r_{Y2\mid13}^2=(r_{Y2\mid3}-r_{Y1\mid3}r_{12\mid3})^2/\big((1-r_{Y1\mid3}^2)(1-r_{12\mid3}^2)\big)$. In the ideal case of two uncorrelated explanatory variables both correlated with $Y$, the coefficient $b_2$ is the same in $Y\sim X_2$ and $Y\sim X_1+X_2$, but $R^2_{Y2\mid1}=r_{Y2}^2/(1-r_{Y1}^2)$ is larger than $R^2_{Y2}=r_{Y2}^2$: removing the variation explained by $X_1$ makes the contribution of $X_2$ a larger fraction of what is left.

### 9.4.3. Suppressor Variables

**Definition 9.4.2 (Suppressor Variable)** If $\mathrm{SSR}(X_2\mid X_1)>\mathrm{SSR}(X_2)$, then $X_1$ is called a **suppressor variable**: $X_2$ explains more of the variation of $Y$ in the presence of $X_1$ than alone.

The idea is that a suppressor variable suppresses variance of the other explanatory variable that is irrelevant for $Y$. The condition is symmetric: since $\mathrm{SSR}(X_2\mid X_1)=\mathrm{SSR}(X_1,X_2)-\mathrm{SSR}(X_1)$,

$$
\mathrm{SSR}(X_2\mid X_1)>\mathrm{SSR}(X_2)\iff\mathrm{SSR}(X_1,X_2)>\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2)\iff\mathrm{SSR}(X_1\mid X_2)>\mathrm{SSR}(X_1),
$$
so the two variables together explain more than the sum of what they explain separately, and each acts as a suppressor for the other. In the Venn diagram of Section 9.3.1 the overlap $C$ would be negative. The condition implies $R^2_{Y2\mid1}>R^2_{Y2}$, because $R^2_{Y2\mid1}=\mathrm{SSR}(X_2\mid X_1)/\mathrm{SSE}(X_1)$ and $\mathrm{SSE}(X_1)\le\mathrm{SSTO}$; the converse fails, as the uncorrelated case at the end of Section 9.4.2 shows. In terms of correlations, the condition reads $R^2>r_{Y1}^2+r_{Y2}^2$; the classical example is $r_{Y1}\approx0$ and $r_{12}\ne0$, where $R^2_{Y2\mid1}\approx r_{Y2}^2/(1-r_{12}^2)>r_{Y2}^2$.

![Partial coefficient of determination of Y and X2 given X1 when X1 is uncorrelated with Y (r_Y1 = 0), for r_Y2 = 0.2, 0.3, 0.5: R^2_{Y2|1} = r_Y2^2 / (1 - r_12^2) starts at r_Y2^2 (dotted lines) and grows towards 1 as the correlation r_12 between the two explanatory variables approaches its largest admissible value](./plots/suppressor-effect.py)

**Example 9.4.1** In the body fat data, $r_{Y3}=0.14$ for midarm while $r_{13}=0.46$. The sequential sums of squares in the two orders are

| order | first variable | second variable | $\mathrm{SSE}$ |
|---|---|---|---|
| skinfold, midarm | $\mathrm{SSR}(X_1)=352.27$ | $\mathrm{SSR}(X_3\mid X_1)=37.19$ | $105.93$ |
| midarm, skinfold | $\mathrm{SSR}(X_3)=10.05$ | $\mathrm{SSR}(X_1\mid X_3)=379.40$ | $105.93$ |

Since $\mathrm{SSR}(X_1\mid X_3)=379.40>\mathrm{SSR}(X_1)=352.27$, midarm is a suppressor variable for skinfold, and correspondingly $\mathrm{SSR}(X_3\mid X_1)=37.19>\mathrm{SSR}(X_3)=10.05$: in the sequential ANOVA table of the two-variable model (with $\mathrm{MSE}=6.23$ on $17$ degrees of freedom), midarm entered first is not significant ($F=1.61$, $p=0.22$), but entered after skinfold it is ($F=5.97$, $p=0.026$).

## Summary

- The extra sum of squares $\mathrm{SSR}(A\mid B)=\mathrm{SSE}(B)-\mathrm{SSE}(A,B)$ is what $A$ explains beyond $B$. Type I (sequential) sums of squares add up to $\mathrm{SSR}$ but depend on the order; Type II and III adjust each term for the others and do not depend on the order; they all coincide for orthogonal variables.
- The general linear test compares nested models by $F^*=\dfrac{(\mathrm{SSE}(R)-\mathrm{SSE}(F))/(\mathrm{df}_E(R)-\mathrm{df}_E(F))}{\mathrm{SSE}(F)/\mathrm{df}_E(F)}$; special cases are the $t$-test ($F=t^2$, since $\mathrm{SSR}(X_k\mid X_{-k})=b_k^2/c_{kk}$), the overall $F$-test, and any linear hypothesis $C\boldsymbol{\beta}=\boldsymbol{t}$.
- Partial $R^2$ and partial correlation measure the contribution of a variable to the variation left by the others; by the Frisch–Waugh–Lovell theorem they come from regressing residuals on residuals, whose slope is the multiple regression coefficient.
- Standardized coefficients $\beta_k^*=(s_k/s_Y)\beta_k$ are unit-free, with $X^{*\mathsf T}X^*=r_{XX}$; $R^2$ and the tests are unchanged.
- A suppressor variable makes another variable more useful: $\mathrm{SSR}(X_1,X_2)>\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2)$.
