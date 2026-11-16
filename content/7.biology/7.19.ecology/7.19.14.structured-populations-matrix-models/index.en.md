---
title: "Structured Populations: Matrix Models"
description: "Population projection matrices for age- and stage-structured populations: Leslie and Lefkovitch matrices, life cycle graphs, the Perron–Frobenius theorem with proof, stable stage distribution, reproductive value and the damping ratio; sensitivity and elasticity analysis with derivations; the killer whale, loggerhead turtle and royal catchfly; transient dynamics, the McKendrick–von Foerster equation and integral projection models."
---

Individuals of different ages, sizes or stages contribute differently to the growth of a population: a seed in the soil, a rosette and a flowering plant face different risks and produce different numbers of offspring. Counting only total numbers, as in the models of [7.19.10](/7.19.10)–[7.19.13](/7.19.13), throws this information away. Matrix population models keep it, and they are the main quantitative tool of conservation and pest management for organisms whose life cycle can be described by a few classes. This chapter builds the models from the simplest example, the Fibonacci rabbits, through the **Leslie matrix** of [7.10.15](/7.10.15) to general stage-classified matrices; proves the Perron–Frobenius theorem that governs their long-run behavior; derives the sensitivity and elasticity of the growth rate, which tell managers where in the life cycle to intervene; and applies these results to killer whales, loggerhead sea turtles and a prairie plant. The last section treats transient dynamics and the continuous-age (McKendrick–von Foerster) and continuous-size (integral projection) versions of the same idea. The linear algebra is that of [2.1.6](/2.1.6); the evolutionary interpretation of the same quantities (fitness, the force of selection) is in [7.10.15](/7.10.15), and stochastic versions of the models, used for viability analysis, are in [7.19.15](/7.19.15).

## 14.1. From Fibonacci to Age Structure

Fibonacci's rabbit problem (1202) is the earliest age-structured population model. Each pair of adult rabbits produces one pair of young each month; young pairs mature in one month; no rabbit dies. Let $A_t$ and $J_t$ be the numbers of adult and juvenile pairs in month $t$. Then $A_{t+1} = A_t + J_t$ and $J_{t+1} = A_t$, or in matrix form

$$
\boldsymbol{n}(t + 1) = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}\boldsymbol{n}(t), \qquad \boldsymbol{n}(t) = \begin{bmatrix} A_t \\ J_t \end{bmatrix}.
$$
The total $F_t = A_t + J_t$ satisfies $F_{t+1} = F_t + F_{t-1}$, the Fibonacci recursion. The characteristic equation of the matrix is $\lambda^2 - \lambda - 1 = 0$, with roots $\lambda_1 = (1 + \sqrt5)/2 \approx 1.618$ and $\lambda_2 = (1 - \sqrt5)/2 \approx -0.618$. Writing $\boldsymbol{n}(0)$ in the basis of **eigenvectors**, $\boldsymbol{n}(t) = c_1\lambda_1^t\boldsymbol{w}_1 + c_2\lambda_2^t\boldsymbol{w}_2$, and since $\lvert\lambda_2\rvert < \lambda_1$ the second term becomes negligible: the population grows geometrically at rate $\lambda_1$, the golden ratio, and the ratio of adults to juveniles approaches that of the eigenvector $\boldsymbol{w}_1 = (\lambda_1, 1)^{\mathsf T}$, again the golden ratio. The left eigenvector, $\boldsymbol{v}_1^{\mathsf T} = (\lambda_1, 1)$, says that an adult pair is worth $\lambda_1$ juvenile pairs for future growth, because it breeds a month earlier. Growth rate, stable structure and relative value of the classes: these three quantities, the dominant eigenvalue and the right and left eigenvectors, are what every matrix model delivers.

## 14.2. Projection Matrices

### 14.2.1. Age- and Stage-Classified Models

The Leslie matrix (Leslie 1945; [Definition 15.1.5](/7.10.15#def-15.1.5) of 7.10.15) classifies individuals by age: in one time step every survivor moves to the next age class, so the only non-zero entries are fecundities in the first row and survival probabilities on the subdiagonal. For many organisms age is a poor predictor of fate. Trees of the same age differ enormously in size; a turtle's chance of surviving depends on whether it is a hatchling, a juvenile or an adult; a perennial plant can remain a rosette for several years. Lefkovitch (1965) generalized the Leslie matrix to classes defined by stage or size, in which individuals can remain in a class, advance, skip classes or even regress.

**Definition 14.2.1 (Population Projection Matrix)** A **population projection matrix** for a population divided into $s$ classes is a nonnegative $s \times s$ matrix $A = (a_{ij})$ such that the vector $\boldsymbol{n}(t)$ of numbers in each class at successive censuses obeys

$$
\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t), \qquad \text{so} \qquad \boldsymbol{n}(t) = A^t\boldsymbol{n}(0).
\tag{14.1}
$$
The entry $a_{ij}$ is the expected number of class-$i$ individuals at time $t + 1$ per class-$j$ individual at time $t$: a survival or transition probability (at most 1), a fecundity, or a sum of both. A matrix classified by age is a Leslie matrix; one classified by stage or size is a *Lefkovitch matrix*. The **life cycle graph** of $A$ is the directed graph with a vertex for each class and an arc $j \to i$ labeled $a_{ij}$ for each $a_{ij} > 0$.

Typical entries of a stage-classified matrix are $P_i$ (survive and remain in class $i$, on the diagonal), $G_i$ (survive and grow to class $i + 1$, on the subdiagonal) and $F_i$ (fecundity, in the first row). If $\sigma_i$ is the annual survival of class $i$ and $\gamma_i$ the probability that a survivor moves on, then $P_i = \sigma_i(1 - \gamma_i)$ and $G_i = \sigma_i\gamma_i$; for a stage of fixed duration $T_i$ years in a stationary population, $\gamma_i = 1/T_i$ is a common approximation. Fecundities depend on the timing of the census: in a census just after breeding (as in [7.10.15](/7.10.15)) $F_i$ is the survival of a class-$i$ parent to the next breeding season times its number of offspring; in a census just before breeding, it is the number of offspring times their survival to the next census. These conventions do not change $\lambda$ but do change the eigenvectors, and confusing them is the most common error in building matrix models.

Matrix models make the same assumptions as the exponential model of [7.19.10](/7.19.10): vital rates are constant (no **density dependence**, no environmental variation), individuals in a class are identical, and only females (or a fixed sex ratio) are modeled. They are projections of what would happen if present conditions persisted, not forecasts (Caswell compares $\lambda$ to the reading of a speedometer). Their power lies in comparing conditions, populations and management options.

**Example 14.2.1 (Resident Killer Whales)** The resident killer whales (*Orcinus orca*) of the coastal waters of British Columbia and Washington live in stable matrilineal pods and can be identified individually from photographs, so that their demography has been followed since 1973. Brault and Caswell (1993) classified females into yearlings, juveniles (past their first year but not yet mature), reproductive adults and post-reproductive adults, and estimated from the 1973–1987 censuses the matrix

$$
A = \begin{bmatrix}
0 & 0.0043 & 0.1132 & 0 \\
0.9775 & 0.9111 & 0 & 0 \\
0 & 0.0736 & 0.9534 & 0 \\
0 & 0 & 0.0452 & 0.9804
\end{bmatrix}.
$$
Juveniles remain juveniles with probability $0.9111$ and mature with probability $0.0736$ per year (a mean juvenile period of about 13 years), reproductive females produce $0.1132$ female yearlings a year (one calf every four to five years, half of them female) and stop reproducing with probability $0.0452$ a year; post-reproductive females survive with probability $0.9804$. The small fecundity of juveniles represents females that mature and breed within the year.

:::

![Life cycle graph of the killer whale model of Brault and Caswell (1993). Each arrow j → i is a non-zero matrix entry a_ij: loops are probabilities of surviving and staying in a stage, forward arrows probabilities of surviving and maturing, and the arrows back to stage 1 (red) are fecundities. No arrow leads from stage 4 back into the other stages, so stage 4 does not contribute to growth](./plots/killer-whale-life-cycle.py)

### 14.2.2. Irreducibility and Primitivity

Two properties of the life cycle graph control the long-run behavior. The matrix $A$ is *irreducible* if its life cycle graph is strongly connected, that is, every class can contribute descendants to every other class; this is the case for most life cycles without post-reproductive classes. An irreducible matrix is *primitive* if, in addition, the greatest common divisor of the lengths of the cycles of its graph is 1. A self-loop has length 1, so any irreducible matrix with a positive diagonal entry is primitive. For a Leslie matrix (no self-loops) each fecundity $F_x > 0$ closes a cycle $0 \to 1 \to \cdots \to x \to 0$ of length $x + 1$, and the matrix is primitive when the ages at which reproduction occurs have greatest common divisor 1, for example when there are two successive breeding ages ([Theorem 15.1.1](/7.10.15#thm-15.1.1) of 7.10.15). Equivalently, a nonnegative matrix is primitive if and only if some power $A^k$ is strictly positive, and then $A^k > 0$ already for $k = s^2 - 2s + 2$ (Wielandt).

The killer whale matrix is reducible, because stage 4 cannot reach the others. Its dynamics are those of the block of stages 1–3, which is irreducible and, having loops, primitive; stage 4 merely accumulates survivors of stage 3.

## 14.3. Long-Run Behavior

### 14.3.1. The Perron–Frobenius Theorem

The general solution of Eq. (14.1) for a diagonalizable $A$ is $\boldsymbol{n}(t) = \sum_k c_k\lambda_k^t\boldsymbol{w}_k$, and the term with the largest $\lvert\lambda_k\rvert$ eventually dominates ([2.1.6](/2.1.6)). For a general matrix the dominant eigenvalue could be complex or negative, or several eigenvalues could share the largest modulus, and the dominant eigenvector could have negative entries, which would make no sense for a population. The Perron–Frobenius theorem rules these out for nonnegative matrices. It was stated for irreducible matrices in [1.4.7](/1.4.7#thm-7.6.1); here we need the stronger form for primitive matrices and give a proof.

**Theorem 14.3.1 (Perron–Frobenius for Primitive Matrices)** Let $A \ge 0$ be a primitive $s \times s$ matrix. Then:

1. $A$ has a real eigenvalue $\lambda_1 > 0$ equal to its **spectral radius**, with a right eigenvector $\boldsymbol{w} > 0$ and a left eigenvector $\boldsymbol{v} > 0$ (all components strictly positive);
2. $\lambda_1$ is algebraically simple, and $\lambda_1 > \lvert\lambda\rvert$ for every other eigenvalue $\lambda$;
3. no other eigenvalue has a nonnegative eigenvector.

If $A$ is irreducible but not primitive, 1 and 3 still hold and $\lambda_1$ is simple, but there are $h > 1$ eigenvalues of modulus $\lambda_1$, namely $\lambda_1\mathrm{e}^{2\pi\mathrm{i}k/h}$, $k = 0, \dots, h - 1$, where $h$ is the greatest common divisor of the cycle lengths.

**Proof** We first prove 1–3 for a strictly positive matrix $A > 0$ and then reduce the primitive case to it.

*Existence.* Let $S = \{\boldsymbol{x} \ge 0 : \sum_ix_i = 1\}$. The map $f(\boldsymbol{x}) = A\boldsymbol{x}/\sum_i(A\boldsymbol{x})_i$ is continuous from $S$ to $S$ (the denominator is positive because $A > 0$), so by Brouwer's fixed-point theorem it has a fixed point $\boldsymbol{w}$: $A\boldsymbol{w} = \lambda_1\boldsymbol{w}$ with $\lambda_1 = \sum_i(A\boldsymbol{w})_i > 0$, and $\boldsymbol{w} = A\boldsymbol{w}/\lambda_1 > 0$. Applying the same argument to $A^{\mathsf T}$ gives $\boldsymbol{v} > 0$ and $\mu > 0$ with $\boldsymbol{v}^{\mathsf T}A = \mu\boldsymbol{v}^{\mathsf T}$; then $\mu\boldsymbol{v}^{\mathsf T}\boldsymbol{w} = \boldsymbol{v}^{\mathsf T}A\boldsymbol{w} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$, and $\boldsymbol{v}^{\mathsf T}\boldsymbol{w} > 0$, so $\mu = \lambda_1$.

*Dominance.* Let $A\boldsymbol{y} = \lambda\boldsymbol{y}$ with $\boldsymbol{y} \ne \boldsymbol{0}$, and write $\lvert\boldsymbol{y}\rvert$ for the vector of moduli. By the triangle inequality $\lvert\lambda\rvert\,\lvert\boldsymbol{y}\rvert = \lvert A\boldsymbol{y}\rvert \le A\lvert\boldsymbol{y}\rvert$ componentwise. Multiplying by $\boldsymbol{v}^{\mathsf T} > 0$ gives $\lvert\lambda\rvert\,\boldsymbol{v}^{\mathsf T}\lvert\boldsymbol{y}\rvert \le \lambda_1\boldsymbol{v}^{\mathsf T}\lvert\boldsymbol{y}\rvert$, so $\lvert\lambda\rvert \le \lambda_1$ and $\lambda_1$ is the spectral radius. If $\lvert\lambda\rvert = \lambda_1$, the nonnegative vector $A\lvert\boldsymbol{y}\rvert - \lambda_1\lvert\boldsymbol{y}\rvert$ has $\boldsymbol{v}^{\mathsf T}(A\lvert\boldsymbol{y}\rvert - \lambda_1\lvert\boldsymbol{y}\rvert) = 0$, hence is zero; then $\lvert\sum_ja_{ij}y_j\rvert = \sum_ja_{ij}\lvert y_j\rvert$ for every $i$, and since all $a_{ij} > 0$ this equality in the triangle inequality forces all $y_j$ to have the same argument: $\boldsymbol{y} = \mathrm{e}^{\mathrm{i}\phi}\lvert\boldsymbol{y}\rvert$. Then $\lambda\lvert\boldsymbol{y}\rvert = A\lvert\boldsymbol{y}\rvert = \lambda_1\lvert\boldsymbol{y}\rvert$, so $\lambda = \lambda_1$.

*Simplicity.* If $A\boldsymbol{y} = \lambda_1\boldsymbol{y}$ with $\boldsymbol{y}$ real and not a multiple of $\boldsymbol{w}$, choose $\varepsilon$ so that $\boldsymbol{z} = \boldsymbol{w} - \varepsilon\boldsymbol{y} \ge 0$ has a zero component but $\boldsymbol{z} \ne \boldsymbol{0}$. Then $\boldsymbol{z} = A\boldsymbol{z}/\lambda_1 > 0$ because $A > 0$, a contradiction; so the eigenspace is one-dimensional. A Jordan block would require $\boldsymbol{u}$ with $(A - \lambda_1I)\boldsymbol{u} = \boldsymbol{w}$; multiplying by $\boldsymbol{v}^{\mathsf T}$ gives $0 = \boldsymbol{v}^{\mathsf T}\boldsymbol{w} > 0$, impossible. Hence $\lambda_1$ is algebraically simple.

*No other nonnegative eigenvector.* If $A\boldsymbol{y} = \lambda\boldsymbol{y}$ with $\boldsymbol{y} \ge 0$, $\boldsymbol{y} \ne \boldsymbol{0}$, then $\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{y} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{y}$ with $\boldsymbol{v}^{\mathsf T}\boldsymbol{y} > 0$, so $\lambda = \lambda_1$.

*Primitive matrices.* If $A$ is primitive, $B = A^k > 0$ for some $k$. The eigenvalues of $B$ are the $k$-th powers of those of $A$, with the same eigenvectors. Let $\boldsymbol{w} > 0$ be the Perron vector of $B$, with eigenvalue $\rho(B)$. Since $A$ commutes with $B$, $A\boldsymbol{w}$ is also an eigenvector of $B$ for $\rho(B)$ (or zero), so by simplicity $A\boldsymbol{w} = \lambda_1\boldsymbol{w}$ for some $\lambda_1$; as $A \ge 0$, $\boldsymbol{w} > 0$ and $A$ has no zero column (it is irreducible), $\lambda_1 > 0$, and $\lambda_1^k = \rho(B)$. Every other eigenvalue $\lambda$ of $A$ has $\lvert\lambda\rvert^k = \lvert\lambda^k\rvert < \rho(B)$ unless $\lambda^k = \rho(B)$ with an eigenvector that is then a multiple of $\boldsymbol{w}$, which forces $\lambda = \lambda_1$. Algebraic simplicity transfers in the same way, since a Jordan block of $A$ for $\lambda_1$ would give one of $B$ for $\rho(B)$. The left eigenvector is obtained from $A^{\mathsf T}$, and 3 follows as before. The statement for imprimitive matrices is proved in texts on nonnegative matrices (Seneta 2006) and is not used below. $\square$

**Theorem 14.3.2 (Strong Ergodic Theorem)** Let $A$ be primitive with dominant eigenvalue $\lambda_1$ and positive eigenvectors $\boldsymbol{w}$, $\boldsymbol{v}$. Then for every initial vector $\boldsymbol{n}(0) \ge 0$,

$$
\lim_{t\to\infty}\frac{\boldsymbol{n}(t)}{\lambda_1^t} = \frac{\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)}{\boldsymbol{v}^{\mathsf T}\boldsymbol{w}}\,\boldsymbol{w}.
\tag{14.2}
$$
In particular the proportions $\boldsymbol{n}(t)/\sum_in_i(t)$ converge to $\boldsymbol{w}/\sum_iw_i$ whatever the initial structure (provided $\boldsymbol{n}(0) \ne \boldsymbol{0}$), and the error decays like $(\lvert\lambda_2\rvert/\lambda_1)^t$, where $\lambda_2$ is an eigenvalue of second-largest modulus.

**Proof** The space $\mathbb{R}^s$ is the direct sum of the line spanned by $\boldsymbol{w}$ and the subspace $U = \{\boldsymbol{x} : \boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0\}$, and both are invariant under $A$ (if $\boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0$ then $\boldsymbol{v}^{\mathsf T}A\boldsymbol{x} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0$). Write $\boldsymbol{n}(0) = c\boldsymbol{w} + \boldsymbol{u}$ with $c = \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$ and $\boldsymbol{u} \in U$. The eigenvalues of $A$ restricted to $U$ are the eigenvalues other than $\lambda_1$ (because $\lambda_1$ is simple), all of modulus at most $\lvert\lambda_2\rvert < \lambda_1$. Hence $\lVert A^t\boldsymbol{u}\rVert \le C_\varepsilon(\lvert\lambda_2\rvert + \varepsilon)^t$ for any $\varepsilon > 0$ (Gelfand's formula), and $A^t\boldsymbol{n}(0)/\lambda_1^t = c\boldsymbol{w} + A^t\boldsymbol{u}/\lambda_1^t \to c\boldsymbol{w}$. The constant $c$ is positive when $\boldsymbol{n}(0) \ge 0$ is non-zero, because $\boldsymbol{v} > 0$. $\square$

Equation (14.2) is the basis for the biological interpretation of the eigen-quantities.

**Definition 14.3.1 (Stable Age Distribution)** The **stable age distribution** (for stage-classified models, the stable stage distribution) of a population with primitive projection matrix $A$ is the right eigenvector $\boldsymbol{w}$ of the dominant eigenvalue, normalized so that $\sum_iw_i = 1$: the proportions in each class that any population approaches when its vital rates remain constant. The dominant eigenvalue $\lambda_1$ is the asymptotic **finite rate of increase** of the population, $r = \ln\lambda_1$ its asymptotic rate of increase, and the population grows, is stationary or declines according as $\lambda_1 > 1$, $= 1$ or $< 1$.

The left eigenvector $\boldsymbol{v}$ gives the **reproductive value** of each class (Fisher 1930; [Definition 15.1.6](/7.10.15#def-15.1.6) of 7.10.15). Equation (14.2) shows what this means: the asymptotic size of a population is proportional to $\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0) = \sum_iv_in_i(0)$, the total reproductive value of its initial members. An individual in class $i$ is "worth" $v_i/v_1$ newborns for the future of the population. For the killer whale (Figure 4B), with $v$ scaled to 1 for yearlings, a juvenile is worth $1.05$ and a reproductive female $1.57$ yearlings, and a post-reproductive female nothing.

### 14.3.2. The Rate of Convergence

**Definition 14.3.2 (Damping Ratio)** The *damping ratio* of a primitive projection matrix is $\rho = \lambda_1/\lvert\lambda_2\rvert > 1$, the ratio of the dominant eigenvalue to the largest modulus of the others.

By Theorem 14.3.2 the deviation from the stable distribution shrinks roughly like $\rho^{-t}$, so the time needed to reduce it by a factor $10$ is about $\ln 10/\ln\rho$. If $\lambda_2$ is complex, the approach is oscillatory with period $2\pi/\arg\lambda_2$: an age structure perturbed by a baby boom echoes for several generations. Long-lived species with slow maturation typically have damping ratios close to 1 and converge slowly, which is why transient dynamics matter for them (Section 14.6.1).

For the killer whale, $\lambda_1 = 1.0254$ (an increase of 2.5 % a year) and the stable stage distribution is $\boldsymbol{w} = (0.037, 0.316, 0.323, 0.324)$. The second eigenvalue is $0.9804$, the survival of post-reproductive females, so $\rho = 1.046$ and a deviation shrinks tenfold only in about 51 years (Figure 3C). The annual growth rate settles within a few decades, but the proportion of post-reproductive females takes a century to stabilize.

![Projection of the killer whale population of Brault and Caswell (1993) from 10 yearlings, 60 juveniles, 110 reproductive and 70 post-reproductive females. A: numbers in each stage and in total over 50 years (log scale). B: the annual growth rate N(t+1)/N(t) converges to λ1 = 1.0254. C: stage proportions converge to the stable stage distribution w (dashed lines), slowly because the second eigenvalue, 0.9804, is close to λ1](./plots/killer-whale-projection.py)

### 14.3.3. When Convergence Fails

If the matrix is irreducible but imprimitive, the population never settles to a stable structure. A semelparous insect that breeds only at age 3, with $A = \begin{bmatrix} 0 & 0 & 8 \\ 0.5 & 0 & 0 \\ 0 & 0.5 & 0 \end{bmatrix}$, has $A^3 = 2I$: all three eigenvalues have modulus $2^{1/3}$, and a population that starts as a single cohort moves through the age classes as a block, the proportions cycling with period 3 forever. Such "population waves" are seen in periodical cicadas and in some salmon runs dominated by one year class. Any slight variation in age at reproduction (a positive entry elsewhere) makes the matrix primitive, and the oscillation then decays slowly.

If the matrix is reducible, as for the killer whale, Theorem 14.3.2 applies to the irreducible block that contains the dominant eigenvalue, provided the classes outside it (here post-reproductive females) have smaller "own" growth rates; their reproductive value is zero.

## 14.4. Sensitivity and Elasticity

### 14.4.1. Sensitivity of the Growth Rate

Managers want to know which vital rates matter most: should one protect nests, juveniles or adults? Such questions are answered by perturbation analysis of $\lambda_1$ (Caswell 1978, 2001), which also gives the strength of selection on each vital rate ([7.10.15](/7.10.15#thm-15.1.2)).

**Definition 14.4.1 (Demographic Sensitivity and Elasticity)** For a primitive projection matrix $A$ with dominant eigenvalue $\lambda_1 = \lambda$, the **demographic sensitivity** of $\lambda$ to the entry $a_{ij}$ is $s_{ij} = \partial\lambda/\partial a_{ij}$, the change in the growth rate per unit absolute change of $a_{ij}$ with the other entries fixed. The **demographic elasticity** is the proportional sensitivity

$$
e_{ij} = \frac{a_{ij}}{\lambda}\frac{\partial\lambda}{\partial a_{ij}} = \frac{\partial\ln\lambda}{\partial\ln a_{ij}} .
$$

**Theorem 14.4.1 (Sensitivity Formula)** With $\boldsymbol{w}$ and $\boldsymbol{v}$ the right and left eigenvectors of $\lambda$,

$$
s_{ij} = \frac{v_iw_j}{\boldsymbol{v}^{\mathsf T}\boldsymbol{w}}, \qquad e_{ij} = \frac{a_{ij}v_iw_j}{\lambda\,\boldsymbol{v}^{\mathsf T}\boldsymbol{w}} .
\tag{14.3}
$$

**Proof** Because $\lambda$ is a simple eigenvalue, $\lambda$ and (suitably normalized) $\boldsymbol{w}$ are differentiable functions of the entries of $A$ (implicit function theorem applied to $\det(A - \lambda I) = 0$). Differentiate $A\boldsymbol{w} = \lambda\boldsymbol{w}$:

$$
(\mathrm{d}A)\boldsymbol{w} + A\,\mathrm{d}\boldsymbol{w} = (\mathrm{d}\lambda)\boldsymbol{w} + \lambda\,\mathrm{d}\boldsymbol{w}.
$$
Multiply on the left by $\boldsymbol{v}^{\mathsf T}$ and use $\boldsymbol{v}^{\mathsf T}A = \lambda\boldsymbol{v}^{\mathsf T}$: the terms in $\mathrm{d}\boldsymbol{w}$ cancel, leaving $\boldsymbol{v}^{\mathsf T}(\mathrm{d}A)\boldsymbol{w} = \mathrm{d}\lambda\,\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$. For a change of the single entry $a_{ij}$, $\boldsymbol{v}^{\mathsf T}(\mathrm{d}A)\boldsymbol{w} = v_iw_j\,\mathrm{d}a_{ij}$. $\square$

The formula has a clear meaning: changing the flow from class $j$ to class $i$ matters in proportion to how common class $j$ is in the stable population ($w_j$) and how valuable the destination class $i$ is ($v_i$). Sensitivities are defined even for entries that are zero (they tell what would happen if a new transition became possible), and they are not comparable between survival probabilities, bounded by 1, and fecundities, which may be large. Elasticities solve both problems.

**Theorem 14.4.2 (Properties of Elasticities)** The elasticities of a primitive projection matrix are nonnegative, vanish for zero entries, and satisfy

$$
\sum_{i,j}e_{ij} = 1, \qquad \sum_ie_{ij} = \sum_ie_{ji} \quad \text{for every class } j .
$$

**Proof** By Eq. (14.3), $\sum_{i,j}e_{ij} = \boldsymbol{v}^{\mathsf T}A\boldsymbol{w}/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = \lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = 1$. (Equivalently, $\lambda$ is a homogeneous function of degree 1 of the entries, and Euler's theorem on homogeneous functions gives $\sum a_{ij}\partial\lambda/\partial a_{ij} = \lambda$.) For the second identity, $\sum_ie_{ij} = w_j(\boldsymbol{v}^{\mathsf T}A)_j/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = v_jw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$ and $\sum_ie_{ji} = v_j(A\boldsymbol{w})_j/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = v_jw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$. $\square$

The first identity lets elasticities be read as the proportional contributions of the transitions to $\lambda$; the second says that elasticity is conserved at every vertex of the life cycle graph, like a flow: the total elasticity of arcs entering a class equals that of arcs leaving it. Consequently all transitions along a cycle of the graph that belongs to no other cycle have the same elasticity. In the killer whale (Figure 4C) the transition from yearling to juvenile (elasticity $0.042$) is the only arc leaving the yearling class and equals the sum of the two fecundities entering it ($0.0015 + 0.0407$).

Vital rates often enter several matrix entries at once. If the entries depend on lower-level parameters $\theta$ (survival $\sigma_i$, growth $\gamma_i$, clutch size), the chain rule gives $\partial\lambda/\partial\theta = \sum_{i,j}s_{ij}\,\partial a_{ij}/\partial\theta$. For example, with $P_i = \sigma_i(1 - \gamma_i)$ and $G_i = \sigma_i\gamma_i$, the elasticity of $\lambda$ to stage survival $\sigma_i$ is $e_{P_i} + e_{G_i}$.

Two cautions apply. Sensitivities and elasticities are local: they predict the effect of small changes, and large changes (eliminating a mortality source) must be evaluated by recomputing $\lambda$. And a vital rate with high elasticity may matter little in practice if it varies little or cannot be changed, which is why retrospective methods (life table response experiments, λ-contribution analysis; Caswell 1989, Sibly and Smith 1998) decompose observed differences in $\lambda$ between years, sites or treatments into contributions of each vital rate, weighting the differences by their sensitivities.

**Example 14.4.1 (Loggerhead Sea Turtles)** Loggerhead turtles (*Caretta caretta*) nesting in the southeastern United States declined in the late twentieth century, and conservation had concentrated on protecting nests and hatchlings on beaches. Crouse, Crowder and Caswell (1987) built a seven-stage matrix (eggs and hatchlings, small juveniles, large juveniles, subadults, novice breeders, first-year remigrants, mature breeders) from data on Little Cumberland Island, Georgia:

$$
A = \begin{bmatrix}
0 & 0 & 0 & 0 & 127 & 4 & 80 \\
0.6747 & 0.7370 & 0 & 0 & 0 & 0 & 0 \\
0 & 0.0486 & 0.6610 & 0 & 0 & 0 & 0 \\
0 & 0 & 0.0147 & 0.6907 & 0 & 0 & 0 \\
0 & 0 & 0 & 0.0518 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0.8091 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0.8091 & 0.8089
\end{bmatrix}.
$$
Here $\lambda = 0.945$: the population was declining by about 5 % a year. The elasticities (Figure 5A) are largest for the survival of small juveniles ($0.23$ in total), mature breeders ($0.23$), subadults ($0.19$) and large juveniles ($0.17$), and small for fecundity ($0.05$) and for the survival of eggs and hatchlings ($0.05$). Recomputing $\lambda$ for large changes confirms the conclusion: halving the mortality of eggs and hatchlings raises $\lambda$ only to $0.956$, a 50 % increase in fecundity to $0.966$, whereas halving the mortality of large juveniles gives $0.992$ (Figure 5B). Even perfect nest protection could not stop the decline. The analysis shifted conservation toward reducing the mortality of large juveniles and subadults in shrimp trawls; turtle excluder devices, which let turtles escape from nets, were made mandatory in US shrimp fisheries, and later models (Crowder et al. 1994) projected that they could reverse the decline.

:::

![Elasticity analysis of loggerhead sea turtles (matrix of Crouse et al. 1987, λ1 = 0.945). A: elasticities of λ1 summed by stage and by type of transition: fecundity, staying in a stage and growing to the next; they sum to 1. B: λ1 recomputed after halving the annual mortality of a single stage, or after a 50 % increase in fecundity (solid line: original λ1; dashed line: λ = 1). Improving juvenile and subadult survival has the largest effect; protecting eggs and hatchlings has little](./plots/loggerhead-elasticity.py)

## 14.5. Further Case Studies

### 14.5.1. Killer Whales Revisited

The killer whale model illustrates all the quantities of this chapter (Figure 4). A population of 250 females that starts entirely as reproductive adults ends up, relative to growth at the rate $\lambda_1$, $1.79$ times as large as its initial size; one that starts as yearlings only $1.14$ times, after an initial dip while the yearlings mature; one made of post-reproductive females dies out. These constants are $v_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$ (with $\sum_iw_i = 1$), by Eq. (14.2). The elasticities show that $\lambda$ depends overwhelmingly on the survival of reproductive females in their stage ($e = 0.54$) and of juveniles ($e = 0.34$); fecundity accounts for only 4 %. This is the typical pattern of long-lived, slowly reproducing animals, and it explains their vulnerability to any additional adult mortality: by Eq. (14.3), $\partial\lambda/\partial a_{33} = 0.58$, so an extra annual mortality of 4.4 % of reproductive females would by itself bring $\lambda$ from $1.025$ to about 1. The southern resident population of the same region, which feeds mainly on declining stocks of Chinook salmon, has in fact declined since the 1990s; its demography is now analyzed with stochastic versions of such models ([7.19.15](/7.19.15)).

![The role of the initial stage and the eigenvectors in the killer whale model. A: total size, relative to growth at the asymptotic rate, of four populations of 250 females that start entirely in one stage; each converges to the reproductive value of the starting stage divided by v·w (dashed lines), and a population of post-reproductive females dies out. B: stable stage distribution w (proportions) and reproductive values v (yearling = 1). C: elasticities of λ1 to the six non-zero entries; they sum to 1, and adult and juvenile survival dominate](./plots/killer-whale-initial-conditions.py)

### 14.5.2. A Prairie Plant and Two Pests

The royal catchfly *Silene regia*, a long-lived perennial of North American prairies, has high adult survival, slow growth, frequent flowering and very episodic recruitment: in most populations and years no seedlings establish. Menges and Dolan (1998) built a six-stage matrix (seedling, vegetative, small, medium and large flowering plants, and "alive but undefined", plants without size data after mowing or herbivory) for 16 populations and several years. For a population managed by prescribed burning, in a year with recruitment, the matrix (columns: stage at $t$; rows: stage at $t + 1$) was

$$
A = \begin{bmatrix}
0 & 0 & 5.32 & 12.74 & 30.88 & 0 \\
0.308 & 0.111 & 0 & 0 & 0 & 0 \\
0 & 0.566 & 0.506 & 0.137 & 0.167 & 0.367 \\
0 & 0.111 & 0.210 & 0.608 & 0.167 & 0.300 \\
0 & 0 & 0.012 & 0.039 & 0.667 & 0.167 \\
0 & 0.222 & 0.198 & 0.196 & 0 & 0.133
\end{bmatrix},
$$
whose dominant eigenvalue (computed from these rounded entries) is $1.70$; the published value is $1.67$. All populations with $\lambda > 1.35$ in years with recruitment had been burned, and none of them was projected to go extinct, whereas unburned populations had lower $\lambda$ and, in stochastic simulations, extinction probabilities of 10–100 % over 1000 years. Fire opens gaps in the vegetation in which seedlings can establish, and the management recommendation followed directly.

Matrix models serve pest management in the same way. For nine-banded armadillos (*Dasypus novemcinctus*), a reservoir of leprosy in the southern United States, the elasticity of $\lambda$ to adult survival approaches 0.5, so control, if needed, should target adults (Oli et al. 2017). For the nodding thistle *Carduus nutans*, an invasive weed, the elasticities differ between Australia (dominated by survival and growth of small plants) and New Zealand (dominated by seed production and germination); a root-crown weevil that reduces growth and survival worked in Australia, whereas in New Zealand an agent reducing seed set would be needed (Shea et al. 2005). The same species can have different vulnerabilities in different places.

## 14.6. Transients and Continuous Structure

### 14.6.1. Transient Dynamics

Asymptotic analysis describes where a population goes; managers often care about the next 10 or 20 years, during which the structure may be far from $\boldsymbol{w}$. Transient behavior is governed by the subdominant eigenvalues and by the initial structure. Two measures are common. The *amplification* (or attenuation) relative to asymptotic growth, $\lim_t N(t)/(\lambda_1^tN(0)) = \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/(\boldsymbol{v}^{\mathsf T}\boldsymbol{w}\,\sum_in_i(0))$ with $\sum_iw_i = 1$, tells whether a population with a given structure will end up larger or smaller than one with the stable structure; for introductions and reintroductions it shows that releasing reproductive adults rather than juveniles gives a larger population for the same number of animals (Figure 4A). *Population momentum* is the special case of a population whose vital rates suddenly change to replacement level ($\lambda_1 = 1$): it keeps growing (or declining) for a time because of its age structure, and its final size is $\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$, computed with the eigenvectors of the new matrix. Human populations with a young age structure continue to grow for decades after fertility falls to replacement. A matrix may also be *reactive*: even if $\lambda_1 < 1$, some initial structures grow in the short term (a pulse of juveniles that are about to mature), which can mislead short monitoring programs.

### 14.6.2. Continuous Age: the McKendrick–von Foerster Equation

If age $a$ and time $t$ are continuous, let $n(t, a)$ be the density of individuals of age $a$ at time $t$, $\mu(a)$ the age-specific mortality rate and $m(a)$ the birth rate (female births per female per unit time).

**Definition 14.6.1 (McKendrick–von Foerster Equation)** The *McKendrick–von Foerster equation* is the first-order partial differential equation

$$
\frac{\partial n}{\partial t} + \frac{\partial n}{\partial a} = -\mu(a)\,n, \qquad n(t, 0) = \int_0^\infty m(a)\,n(t, a)\,\mathrm{d}a, \qquad n(0, a) = n_0(a),
\tag{14.4}
$$
in which individuals age at unit speed and die at rate $\mu(a)$, and the boundary condition at age 0 collects the births.

It is solved by the **method of characteristics** ([2.5.2](/2.5.2)). Along the lines $a - t = \text{const}$ (a cohort ageing as time passes), $\mathrm{d}n/\mathrm{d}t = -\mu(a)n$, so with survivorship $\ell(a) = \exp\bigl(-\int_0^a\mu(s)\,\mathrm{d}s\bigr)$,

$$
n(t, a) = \begin{cases} B(t - a)\,\ell(a), & a < t, \\ n_0(a - t)\,\ell(a)/\ell(a - t), & a \ge t, \end{cases}
$$
where $B(t) = n(t, 0)$ is the birth rate. Substituting into the boundary condition gives the renewal equation of Lotka (1922):

$$
B(t) = \int_0^tm(a)\ell(a)B(t - a)\,\mathrm{d}a + G(t),
\tag{14.5}
$$
where $G(t) = \int_t^\infty m(a)n_0(a - t)\ell(a)/\ell(a - t)\,\mathrm{d}a$ is the contribution of individuals alive at time 0, which vanishes once they are past reproduction. Trying $B(t) = B_0\mathrm{e}^{rt}$ in the homogeneous equation gives the continuous **Euler–Lotka equation**

$$
\int_0^\infty\mathrm{e}^{-ra}\ell(a)m(a)\,\mathrm{d}a = 1,
\tag{14.6}
$$
whose left side decreases strictly in $r$ from $+\infty$ to 0 (when $\ell m$ is not identically zero), so it has exactly one real root $r$; all complex roots have smaller real part, and $B(t) \sim B_0\mathrm{e}^{rt}$ (Feller 1941). The stable age distribution is $c(a) \propto \mathrm{e}^{-ra}\ell(a)$: the density at age $a$ is reduced by survival and by the fact that older individuals were born when the population was smaller (Figure 6). This is the continuous counterpart of Theorem 14.3.2, and the discrete Euler–Lotka equation of [7.10.15](/7.10.15) is its version for a **life table** with annual age classes. The equation (14.4) is the starting point for physiologically structured models, in which size or another physiological variable replaces age and grows at a rate that may depend on food.

![The McKendrick–von Foerster equation with constant mortality μ = 0.3 per year and fecundity 1.2 per year between ages 2 and 6, starting from a pulse of individuals aged 0–1 year. A: the age distribution n(t, a)/N(t) over 40 years: cohorts travel along the characteristics a - t = const (white lines), and the echoes of the initial pulse fade. B: age distributions at four times and the stable age distribution c(a) ∝ exp(-ra) l(a) with r = 0.121 per year from the Euler–Lotka equation (dashed)](./plots/mckendrick-characteristics.py)

### 14.6.3. Integral Projection Models

When demography depends on a continuous trait such as body mass or plant size, arbitrary class boundaries lose information. An *integral projection model* (Easterling, Ellner and Dixon 2000) replaces the matrix by a kernel:

$$
n(z', t + 1) = \int_L^U K(z', z)\,n(z, t)\,\mathrm{d}z, \qquad K(z', z) = s(z)\,g(z' \mid z) + f(z)\,c(z'),
$$
where $s(z)$ is the survival of an individual of size $z$, $g(z' \mid z)$ the probability density of its size $z'$ next year, $f(z)$ its fecundity and $c(z')$ the size distribution of offspring. Each function is estimated by a regression on individual data (survival by logistic regression on size, growth by linear regression, and so on), which uses the data efficiently. Numerically the integral is evaluated with the midpoint rule on a fine grid, which turns $K$ into a large matrix, and all the results of this chapter (dominant eigenvalue, eigenvectors, sensitivities, now functions of size) carry over. Integral projection models can include density dependence and environmental covariates in the vital-rate functions; in Soay sheep on St Kilda they link body mass, population density and the population growth rate (Coulson 2012).

## Summary

- A projection matrix $A$ (Definition 14.2.1) projects class numbers by $\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t)$; Leslie matrices classify by age, Lefkovitch matrices by stage or size, with entries $P_i = \sigma_i(1 - \gamma_i)$, $G_i = \sigma_i\gamma_i$ and fecundities $F_i$ whose definition depends on the timing of the census. The life cycle graph shows the structure; irreducibility (strong connectivity) and primitivity (cycle lengths with greatest common divisor 1) control the long-run behavior.
- Perron–Frobenius (Theorem 14.3.1) and the strong ergodic theorem (Theorem 14.3.2):

  | Quantity | Definition | Meaning |
  |---|---|---|
  | $\lambda_1$ | dominant eigenvalue, positive and simple | asymptotic finite rate of increase; $r = \ln\lambda_1$ |
  | $\boldsymbol{w}$ | $A\boldsymbol{w} = \lambda_1\boldsymbol{w}$, $\boldsymbol{w} > 0$ | stable age (stage) distribution (Definition 14.3.1) |
  | $\boldsymbol{v}$ | $\boldsymbol{v}^{\mathsf T}A = \lambda_1\boldsymbol{v}^{\mathsf T}$, $\boldsymbol{v} > 0$ | reproductive value; asymptotic size $\propto \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)$, Eq. (14.2) |
  | $\rho = \lambda_1/\lvert\lambda_2\rvert$ | damping ratio (Definition 14.3.2) | rate of convergence; slow for long-lived species |

  Imprimitive matrices give persistent waves; reducible ones decompose into blocks.
- Sensitivity $s_{ij} = v_iw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$ and elasticity $e_{ij} = a_{ij}s_{ij}/\lambda$ (Definition 14.4.1, Theorem 14.4.1); elasticities sum to 1 and are conserved at each class (Theorem 14.4.2). Lower-level parameters follow by the chain rule; large changes must be recomputed; retrospective analyses (LTRE, λ-contribution) decompose observed variation.
- Applications: killer whales ($\lambda = 1.025$, adult survival dominates, slow convergence), loggerhead turtles ($\lambda = 0.945$; juvenile and subadult survival, not nest protection, controls the trend: turtle excluder devices), royal catchfly (burning allows recruitment), armadillos and thistles (management targets differ by species and place).
- Transients: amplification, momentum and reactivity depend on the initial structure through $\boldsymbol{v}$. Continuous age gives the McKendrick–von Foerster equation (Definition 14.6.1), solved along characteristics, leading to Lotka's renewal equation (14.5), the Euler–Lotka equation (14.6) and the stable age distribution $c(a) \propto \mathrm{e}^{-ra}\ell(a)$. Integral projection models replace classes by a continuous trait.

## Questions

1. For the Fibonacci matrix $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$, compute the sensitivities and elasticities of $\lambda_1$ and check Theorem 14.4.2.

   **Answer** With $\varphi = \lambda_1 = (1 + \sqrt5)/2$, $\boldsymbol{w} = (\varphi, 1)^{\mathsf T}$ and $\boldsymbol{v} = (\varphi, 1)^{\mathsf T}$ (the matrix is symmetric), $\boldsymbol{v}^{\mathsf T}\boldsymbol{w} = \varphi^2 + 1$. The sensitivities are $s_{11} = \varphi^2/(\varphi^2 + 1) = 0.724$, $s_{12} = s_{21} = \varphi/(\varphi^2 + 1) = 0.447$, $s_{22} = 1/(\varphi^2 + 1) = 0.276$. The elasticities of the three non-zero entries are $e_{11} = s_{11}/\varphi = 0.447$, $e_{12} = e_{21} = s_{12}/\varphi = 0.276$, and $e_{22} = 0$. They sum to $0.447 + 0.276 + 0.276 = 1$, and at the juvenile class the incoming elasticity $e_{21} = 0.276$ equals the outgoing $e_{12} = 0.276$, as the conservation law requires: the two arcs form a cycle of length 2 that belongs to no other cycle.

2. In the killer whale model, suppose $h$ reproductive females are removed every year (for example by bycatch or by captures for aquaria), and the population is at its stable structure with 250 females. Estimate the largest sustainable $h$ from the sensitivity, and explain why the estimate is only approximate.

   **Answer** Removing a constant fraction $q$ of reproductive females reduces $a_{33}$ and $a_{43}$ (and the fecundity $a_{13}$, which assumes survival) by the factor $1 - q$. Using only $a_{33}$, $\Delta\lambda \approx -s_{33}a_{33}q = -0.579 \times 0.953\,q$, and $\lambda$ stays at least 1 if $q \le 0.0254/0.552 \approx 0.046$; including the other two entries, the total elasticity of the three entries in column 3 is $0.54 + 0.04 + 0.0 = 0.58$, giving $\Delta\ln\lambda \approx -0.58q$ and $q \le 0.025/0.58 \approx 0.043$ (recomputing $\lambda$ exactly gives $0.047$). With $250 \times 0.323 \approx 81$ reproductive females, this is about $3.5$ females a year, and a simulation of $\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t) - \boldsymbol{h}$ from the stable structure also gives about $3.5$. The estimate is approximate because the sensitivity is a linear approximation, because constant-number removal differs from constant-proportion removal (it becomes a larger fraction as the population shrinks), and because the model ignores stochasticity and density dependence; in reality no harvest of such a small, slowly reproducing population would be advisable.

3. Show that the Leslie matrix with fecundities only at ages 2 and 4 (and positive survival up to age 4) is irreducible but not primitive. What does this imply for the age structure of a population that starts with newborns only?

   **Answer** The graph has the path through the age classes and arcs back to the first class from the two breeding ages, which close cycles of lengths 2 and 4. All classes are mutually reachable, so the matrix is irreducible, but every cycle has even length, so $h = \gcd(2, 4) = 2$: there is an eigenvalue $-\lambda_1$ of the same modulus as $\lambda_1$. A population of newborns has offspring only in even years and only in even age classes, so the population alternates between two different structures (odd and even classes populated) and never converges to $\boldsymbol{w}$; any breeding at an odd age makes the matrix primitive and the oscillation decays.

4. Derive the stable age distribution of the McKendrick–von Foerster equation directly, by substituting $n(t, a) = \mathrm{e}^{rt}c(a)$ into Eq. (14.4).

   **Answer** Substitution gives $rc(a) + c'(a) = -\mu(a)c(a)$, so $c(a) = c(0)\exp\bigl(-ra - \int_0^a\mu\bigr) = c(0)\mathrm{e}^{-ra}\ell(a)$. The boundary condition becomes $c(0) = \int m(a)c(0)\mathrm{e}^{-ra}\ell(a)\,\mathrm{d}a$, which for $c(0) \ne 0$ is the Euler–Lotka equation (14.6). So separable solutions exist only for the roots of Eq. (14.6), and the one with real $r$ has a positive age distribution.

5. A conservation agency can either protect beaches (halving the mortality of eggs and hatchlings) or require turtle excluder devices (halving the mortality of large juveniles and subadults) for loggerheads. Using the elasticities of Example 14.4.1, explain which option the matrix model favors and what additional information a manager would need before deciding.

   **Answer** The elasticity of $\lambda$ to the survival of eggs and hatchlings is about $0.05$, whereas the combined elasticity to the survival of large juveniles and subadults is about $0.36$. Halving mortality changes stage survival by different proportional amounts in different stages (hatchling survival $0.67 \to 0.84$, a 24 % increase; large juvenile survival $0.68 \to 0.84$), so the comparison should be made by recomputing $\lambda$: beach protection gives $\lambda \approx 0.956$, excluder devices applied to both stages give about $1.025$, enough to reverse the decline. The manager also needs the costs and feasibility of each action, the uncertainty of the vital rates (the sensitivity of the conclusion to estimation error), possible density dependence at high abundance, and whether the matrix (from one beach in the 1980s) represents the current population; elasticities show where effort could help, not whether a given program is feasible.

6. (Open question) The reproductive value of a post-reproductive killer whale female is zero in the matrix model. Discuss whether this means that such females are unimportant for the population.

   **Answer** Key points: the matrix model counts only direct contributions to future births, so by construction post-reproductive females have zero reproductive value and their survival has zero sensitivity. In resident killer whales, however, post-reproductive mothers lead their pods to salmon in years of food shortage, and the death of a post-reproductive mother greatly increases the mortality of her adult offspring, especially sons, in the following years (Foster et al. 2012; Brent et al. 2015). These effects act through the survival of other classes, which the model treats as constants; a model in which juvenile or adult survival depends on the presence of a grandmother would give post-reproductive females indirect reproductive value. The example shows that the matrix model is only as good as its assumption of independent individuals, and connects to the evolution of menopause through kin selection ([7.10.16](/7.10.16)).
