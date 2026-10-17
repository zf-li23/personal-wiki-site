---
title: 多元正态分布
---

正态分布之所以重要，一是因为中心极限定理（[3.1.13](/3.1.13)），二是因为它在线性运算下封闭、计算简便。本章把它推广到随机向量。[3.1.6](/3.1.6) 已经用联合密度定义了二元正态分布；对一般的维数，更方便的定义是"独立标准正态随机变量的线性变换"，由此可以统一地推出联合密度、特征函数、边缘分布、线性变换、独立性判定与条件分布，证明的工具主要是特征函数（[3.1.11](/3.1.11)）与矩阵运算（[2.1](/2.1)）。多元正态分布的这些性质是统计推断中正态总体的抽样分布（[3.2.2](/3.2.2)）、线性回归与多元统计分析的基础。本章最后给出随机向量的大数定律与中心极限定理。

## 15.1. 随机向量的期望与协方差矩阵

本节与 [3.1.10](/3.1.10) 中的协方差矩阵一致，这里集中写出矩阵形式的运算规则。向量一律写成列向量。

设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 是随机向量。如果对每个 $i$，$\mu_i = \mathbb{E}X_i$ 存在，就称 $\boldsymbol{X}$ 的数学期望存在，并定义

$$
\boldsymbol{\mu} = \mathbb{E}\boldsymbol{X} = (\mathbb{E}X_1, \dots, \mathbb{E}X_n)^{\mathsf T} = (\mu_1, \dots, \mu_n)^{\mathsf T}.
$$
类似地，对元素为随机变量的矩阵 $Y = (X_{ij})_{m \times n}$，定义 $\mathbb{E}Y = (\mathbb{E}X_{ij})_{m \times n}$。

**性质 15.1.1** 设随机向量 $\boldsymbol{X}$、随机矩阵 $Y$ 的期望都存在，$\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T}$ 是常数向量，$A_{k \times m}$、$B_{n \times j}$ 是常数矩阵（维数使运算有意义），则

1. $\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\mathbb{E}\boldsymbol{X}$；
2. $(\mathbb{E}Y)^{\mathsf T} = \mathbb{E}(Y^{\mathsf T})$；
3. $\mathbb{E}(AY) = A\,\mathbb{E}Y$；
4. $\mathbb{E}(YB) = (\mathbb{E}Y)B$；
5. $\mathbb{E}(AYB) = A(\mathbb{E}Y)B$。

它们本质上都是期望的线性性质：例如 $AY$ 的 $(i, l)$ 元是 $\sum_s a_{is}X_{sl}$，其期望是 $\sum_s a_{is}\mathbb{E}X_{sl}$。

$\boldsymbol{X}$ 的协方差矩阵（定义 10.5.1）为

$$
\Sigma = \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}] = (\sigma_{ij})_{n \times n}, \quad \sigma_{ij} = \operatorname{Cov}(X_i, X_j).
$$
它是对称的非负定矩阵；$\det\Sigma = 0$（称 $\Sigma$ 退化）当且仅当存在不全为零的常数 $a_1, \dots, a_n$，使 $\sum_{i=1}^{n} a_i(X_i - \mathbb{E}X_i) = 0$ a.s.（定理 10.5.1）。证明的关键是 $\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} = \operatorname{Var}\left(\sum_i a_i(X_i - \mathbb{E}X_i)\right) \ge 0$。

**性质 15.1.2** 设 $\boldsymbol{X}$ 的协方差矩阵为 $\Sigma$，$A$ 是常数矩阵，$\boldsymbol{b}$ 是常数向量，则

$$
\mathbb{E}(\boldsymbol{b} + A\boldsymbol{X}) = \boldsymbol{b} + A\boldsymbol{\mu}, \qquad \operatorname{Cov}(\boldsymbol{b} + A\boldsymbol{X}) = A\Sigma A^{\mathsf T}.
$$

**证明** 由性质 15.1.1，$\operatorname{Cov}(\boldsymbol{b} + A\boldsymbol{X}) = \mathbb{E}[A(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}A^{\mathsf T}] = A\,\mathbb{E}[(\boldsymbol{X} - \boldsymbol{\mu})(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}]\,A^{\mathsf T} = A\Sigma A^{\mathsf T}$。 $\square$

特别地，$\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}$。

## 15.2. 多元正态分布的定义

**定义 15.2.1（多元正态分布）** 设 $\boldsymbol{\mu} = (\mu_1, \dots, \mu_n)^{\mathsf T}$ 是 $n$ 维常数列向量，$B$ 是 $n \times m$ 常数矩阵，$\varepsilon_1, \dots, \varepsilon_m$ 是相互独立且服从标准正态分布的随机变量，$\boldsymbol{\varepsilon} = (\varepsilon_1, \dots, \varepsilon_m)^{\mathsf T}$。如果

$$
\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon},
$$
且矩阵 $BB^{\mathsf T}$ 满秩，就称 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T}$ 服从 $n$ 维正态分布，或**多元正态分布**（multivariate normal distribution，MVN），记作 $\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, BB^{\mathsf T})$，维数明确时简记为 $\mathcal{N}(\boldsymbol{\mu}, BB^{\mathsf T})$。

$\boldsymbol{\varepsilon}$ 的各分量独立且方差为 $1$，$\mathbb{E}\boldsymbol{\varepsilon} = \boldsymbol{0}$，$\operatorname{Cov}(\boldsymbol{\varepsilon}) = \mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T}) = I_m$。由性质 15.1.2，

$$
\mathbb{E}\boldsymbol{X} = \boldsymbol{\mu} + B\,\mathbb{E}\boldsymbol{\varepsilon} = \boldsymbol{\mu}, \qquad \Sigma := \operatorname{Cov}(\boldsymbol{X}) = \mathbb{E}[(B\boldsymbol{\varepsilon})(B\boldsymbol{\varepsilon})^{\mathsf T}] = B\,\mathbb{E}(\boldsymbol{\varepsilon}\boldsymbol{\varepsilon}^{\mathsf T})\,B^{\mathsf T} = BI_mB^{\mathsf T} = BB^{\mathsf T}.
$$
所以记号 $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 中的两个参数正是期望向量与协方差矩阵。$BB^{\mathsf T}$ 满秩即 $\Sigma$ 正定，这要求 $m \ge n$。反之，对任意正定矩阵 $\Sigma$，取 $B = \Sigma^{1/2}$（或 Cholesky 分解中的下三角矩阵），$\boldsymbol{\mu} + B\boldsymbol{\varepsilon}$ 就服从 $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$，所以每个正定矩阵都是某个多元正态分布的协方差矩阵。

**例 15.2.1** 设 $\varepsilon_1, \varepsilon_2$ 独立同分布于 $\mathcal{N}(0, 1)$，

$$
\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix} + \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} \varepsilon_1 \\ \varepsilon_2 \end{pmatrix},
$$
则 $(X_1, X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}\right)$。由下面的定理 15.4.2，$X_1 = \mu_1 + \varepsilon_1 + \varepsilon_2$ 与 $X_2 = \mu_2 + \varepsilon_1 - \varepsilon_2$ 相互独立。

**定理 15.2.1（密度函数）** 当 $\Sigma$ 正定时，$\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$ 有联合密度函数

$$
f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^n\sqrt{\det\Sigma}}\exp\left[-\frac{1}{2}(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\right], \quad \boldsymbol{x} \in \mathbb{R}^n. \tag{15.1}
$$

**证明** 下面说明 $\boldsymbol{X}$ 的分布只依赖于 $\boldsymbol{\mu}$ 与 $\Sigma$（定理 15.2.2），所以可以取一个可逆方阵 $B$ 使 $\Sigma = BB^{\mathsf T}$，并设 $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$，$\boldsymbol{\varepsilon} \sim \mathcal{N}_n(\boldsymbol{0}, I_n)$。$\boldsymbol{\varepsilon}$ 的分量独立，密度为

$$
f_{\boldsymbol{\varepsilon}}(\boldsymbol{y}) = \prod_{i=1}^{n}\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-y_i^2/2} = \frac{1}{(\sqrt{2\pi})^n}\exp\left(-\frac{1}{2}\boldsymbol{y}^{\mathsf T}\boldsymbol{y}\right).
$$
映射 $\boldsymbol{y} = B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})$ 可逆，$\{\boldsymbol{X} = \boldsymbol{x}\} = \{\boldsymbol{\varepsilon} = B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\}$，Jacobi 行列式的绝对值为 $\lvert \det B^{-1} \rvert = 1/\sqrt{\det\Sigma}$（因为 $\det\Sigma = (\det B)^2$）。由随机向量函数的密度变换公式（[3.1.7](/3.1.7)），

$$
f(\boldsymbol{x}) = \frac{1}{(\sqrt{2\pi})^n}\exp\left\{-\frac{1}{2}[B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})]^{\mathsf T}[B^{-1}(\boldsymbol{x} - \boldsymbol{\mu})]\right\}\frac{1}{\sqrt{\det\Sigma}},
$$
而 $(B^{-1})^{\mathsf T}B^{-1} = (BB^{\mathsf T})^{-1} = \Sigma^{-1}$，即得式 (15.1)。 $\square$

$n = 2$、$\Sigma = \begin{pmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$ 时，式 (15.1) 正是 [3.1.6](/3.1.6) 中二元正态分布 $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ 的密度（定义 6.4.1）。密度的等高线 $(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) = c$ 是以 $\boldsymbol{\mu}$ 为中心的椭球，主轴方向是 $\Sigma$ 的特征向量，半轴长与特征值的平方根成正比。

![二元正态分布 N(0, 0, 1, 1, rho) 的密度等高线与条件期望直线 E(Y | X = x) = rho x（rho = -0.7, 0, 0.7）](./plots/bivariate-normal-contours.py)

**定理 15.2.2（特征函数）** $\boldsymbol{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \Sigma)$ 的特征函数为

$$
\varphi_{\boldsymbol{X}}(\boldsymbol{t}) = \mathbb{E}\exp(\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{X}) = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right], \quad \boldsymbol{t} \in \mathbb{R}^n.
$$

**证明** 先求 $\boldsymbol{\varepsilon}$ 的特征函数：由分量独立与例 11.3.6，对 $\boldsymbol{s} \in \mathbb{R}^m$，

$$
\varphi_{\boldsymbol{\varepsilon}}(\boldsymbol{s}) = \mathbb{E}\left[\prod_{j=1}^{m}\exp(\mathrm{i}s_j\varepsilon_j)\right] = \prod_{j=1}^{m}\mathbb{E}\exp(\mathrm{i}s_j\varepsilon_j) = \prod_{j=1}^{m}\exp\left(-\frac{s_j^2}{2}\right) = \exp\left(-\frac{\boldsymbol{s}^{\mathsf T}\boldsymbol{s}}{2}\right).
$$
于是

$$
\varphi_{\boldsymbol{X}}(\boldsymbol{t}) = \mathbb{E}\exp[\mathrm{i}(\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} + \boldsymbol{t}^{\mathsf T}B\boldsymbol{\varepsilon})] = \exp(\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu})\,\varphi_{\boldsymbol{\varepsilon}}(B^{\mathsf T}\boldsymbol{t}) = \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}BB^{\mathsf T}\boldsymbol{t}\right]. \quad \square
$$

由此可见，$\boldsymbol{X}$ 的期望与协方差矩阵唯一决定了 $\boldsymbol{X}$ 的特征函数，而随机向量的特征函数与分布函数相互唯一决定，所以多元正态分布由 $\boldsymbol{\mu}$ 和 $\Sigma$ 唯一决定，与表示 $\Sigma = BB^{\mathsf T}$ 中 $B$ 的选取无关。联合密度（定理 15.2.1）与特征函数（定理 15.2.2）都可以作为多元正态分布的等价定义。

## 15.3. 边缘分布与线性变换

**定理 15.3.1** 如果 $\boldsymbol{X}$ 服从多元正态分布，则 $\boldsymbol{X}$ 的任何一组分量 $(X_{j_1}, \dots, X_{j_k})^{\mathsf T}$ 也服从（多元）正态分布，期望与协方差矩阵分别是 $\boldsymbol{\mu}$、$\Sigma$ 中相应的分量与子矩阵。

**证明** 设 $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$，取出 $B$ 的第 $j_1, \dots, j_k$ 行组成 $B_1$，则 $(X_{j_1}, \dots, X_{j_k})^{\mathsf T} = (\mu_{j_1}, \dots, \mu_{j_k})^{\mathsf T} + B_1\boldsymbol{\varepsilon}$。$B_1B_1^{\mathsf T}$ 是正定矩阵 $BB^{\mathsf T}$ 的主子矩阵，仍然正定，由定义即得。 $\square$

例如在例 15.2.1 中，$X_1 = \mu_1 + \varepsilon_1 + \varepsilon_2 \sim \mathcal{N}(\mu_1, 2)$。

**定理 15.3.2** 如果 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，则对任意常数矩阵 $A$ 和常数向量 $\boldsymbol{b}$，只要 $\boldsymbol{b} + A\boldsymbol{X}$ 有意义且 $A\Sigma A^{\mathsf T}$ 满秩，就有

$$
\boldsymbol{Y} = \boldsymbol{b} + A\boldsymbol{X} \sim \mathcal{N}\left(\boldsymbol{b} + A\boldsymbol{\mu}, A\Sigma A^{\mathsf T}\right).
$$

**证明** 由定义，存在 $n \times m$ 常数矩阵 $B$ 与独立标准正态的 $\varepsilon_1, \dots, \varepsilon_m$ 使 $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$。于是 $\boldsymbol{Y} = (\boldsymbol{b} + A\boldsymbol{\mu}) + (AB)\boldsymbol{\varepsilon}$，且 $(AB)(AB)^{\mathsf T} = A\Sigma A^{\mathsf T}$ 满秩，再次由定义，$\boldsymbol{Y}$ 服从多元正态分布，期望与协方差矩阵由性质 15.1.2 给出。 $\square$

**例 15.3.1** 设

$$
\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 1 \\ -5 \end{pmatrix}, \begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\right), \qquad \begin{pmatrix} Y_1 \\ Y_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} X_1 \\ X_2 \end{pmatrix},
$$
则 $\boldsymbol{b} + A\boldsymbol{\mu} = (2, -4)^{\mathsf T}$，

$$
A\Sigma A^{\mathsf T} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix},
$$
所以 $(Y_1, Y_2)^{\mathsf T} = (1 + X_1, X_1 + X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 2 \\ -4 \end{pmatrix}, \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix}\right)$。

取 $A$ 为行向量 $\boldsymbol{a}^{\mathsf T}$，就得到一维的情形；它的逆命题也成立，这是判断多元正态分布最实用的工具。

**定理 15.3.3（判定法则）** $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 的充要条件是：对任何 $\boldsymbol{a} = (a_1, \dots, a_n)^{\mathsf T} \in \mathbb{R}^n$，

$$
Y := \boldsymbol{a}^{\mathsf T}\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}).
$$
（$\boldsymbol{a} = \boldsymbol{0}$ 时理解为退化于常数的"正态分布" $\mathcal{N}(0, 0)$。）

**证明** 必要性：$Y$ 的特征函数为

$$
\varphi_Y(t) = \mathbb{E}\exp(\mathrm{i}tY) = \mathbb{E}\exp[\mathrm{i}(t\boldsymbol{a})^{\mathsf T}\boldsymbol{X}] = \exp\left[\mathrm{i}t(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}) - \frac{1}{2}t^2\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}\right], \tag{15.2}
$$
所以 $Y \sim \mathcal{N}(\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$。充分性：在式 (15.2) 中取 $t = 1$，

$$
\mathbb{E}\exp(\mathrm{i}\boldsymbol{a}^{\mathsf T}\boldsymbol{X}) = \varphi_Y(1) = \exp\left[\mathrm{i}\boldsymbol{a}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}\right]
$$
对一切 $\boldsymbol{a}$ 成立，这正是 $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$ 的特征函数，由唯一性，$\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$。 $\square$

例如 $(X_1, X_2)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 1 \\ -5 \end{pmatrix}, \begin{pmatrix} 4 & -2 \\ -2 & 9 \end{pmatrix}\right)$ 当且仅当对一切 $a_1, a_2$，$a_1X_1 + a_2X_2 \sim \mathcal{N}(a_1 - 5a_2, 4a_1^2 - 4a_1a_2 + 9a_2^2)$。

**注 15.3.1** 定理 15.3.3 要求的是一切线性组合都是正态的，只有每个分量正态是不够的。设 $X \sim \mathcal{N}(0, 1)$，$S$ 与 $X$ 独立，$\mathbb{P}(S = 1) = \mathbb{P}(S = -1) = \frac{1}{2}$，令 $Y = SX$。由对称性 $Y \sim \mathcal{N}(0, 1)$，但 $\mathbb{P}(X + Y = 0) = \mathbb{P}(S = -1) = \frac{1}{2}$，$X + Y$ 不是正态的，所以 $(X, Y)$ 不服从二元正态分布。此外 $\operatorname{Cov}(X, Y) = \mathbb{E}(SX^2) = \mathbb{E}S \cdot \mathbb{E}X^2 = 0$，但 $\lvert Y \rvert = \lvert X \rvert$，$X$ 与 $Y$ 不独立。

![注 15.3.1 的反例：X, Y 都是标准正态且不相关，但 (X, Y) 的样本集中在两条对角线上，不是二元正态](./plots/normal-marginals-not-joint.py)

## 15.4. 独立性判定

对多元正态分布，独立性可以直接从协方差矩阵读出。

**定理 15.4.1** 设 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，按分块写作

$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \qquad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \qquad \Sigma = \begin{pmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} \end{pmatrix},
$$
其中 $\boldsymbol{X}_1$、$\boldsymbol{\mu}_1$ 与方阵 $\Sigma_{11}$ 的行数相同，则 $\boldsymbol{X}_1$ 与 $\boldsymbol{X}_2$ 独立，而且 $\boldsymbol{X}_1 \sim \mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11})$，$\boldsymbol{X}_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$。

**证明** 把 $\boldsymbol{t}$ 相应地分块为 $(\boldsymbol{t}_1^{\mathsf T}, \boldsymbol{t}_2^{\mathsf T})^{\mathsf T}$。由定理 15.2.2，

$$
\begin{aligned}
\varphi(\boldsymbol{t}) = \varphi(\boldsymbol{t}_1, \boldsymbol{t}_2) &= \exp\left[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}\right] = \exp\left[\mathrm{i}\boldsymbol{t}_1^{\mathsf T}\boldsymbol{\mu}_1 - \frac{1}{2}\boldsymbol{t}_1^{\mathsf T}\Sigma_{11}\boldsymbol{t}_1 + \mathrm{i}\boldsymbol{t}_2^{\mathsf T}\boldsymbol{\mu}_2 - \frac{1}{2}\boldsymbol{t}_2^{\mathsf T}\Sigma_{22}\boldsymbol{t}_2\right] \\
&= \exp\left[\mathrm{i}\boldsymbol{t}_1^{\mathsf T}\boldsymbol{\mu}_1 - \frac{1}{2}\boldsymbol{t}_1^{\mathsf T}\Sigma_{11}\boldsymbol{t}_1\right] \times \exp\left[\mathrm{i}\boldsymbol{t}_2^{\mathsf T}\boldsymbol{\mu}_2 - \frac{1}{2}\boldsymbol{t}_2^{\mathsf T}\Sigma_{22}\boldsymbol{t}_2\right] = \varphi_1(\boldsymbol{t}_1)\varphi_2(\boldsymbol{t}_2),
\end{aligned}
$$
其中 $\varphi_1$、$\varphi_2$ 分别是 $\mathcal{N}(\boldsymbol{\mu}_1, \Sigma_{11})$、$\mathcal{N}(\boldsymbol{\mu}_2, \Sigma_{22})$ 的特征函数（由定理 15.3.1，也就是 $\boldsymbol{X}_1$、$\boldsymbol{X}_2$ 的特征函数）。由特征函数的独立性判别法（推论 11.3.2）即得。 $\square$

**例 15.4.1**

$$
\begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 2 \\ 7 \\ 3 \end{pmatrix}, \begin{pmatrix} 4 & 0 & 0 \\ 0 & 9 & -3 \\ 0 & -3 & 8 \end{pmatrix}\right) \iff \begin{cases} X_1 \sim \mathcal{N}(2, 4), \\ (X_2, X_3)^{\mathsf T} \sim \mathcal{N}\left(\begin{pmatrix} 7 \\ 3 \end{pmatrix}, \begin{pmatrix} 9 & -3 \\ -3 & 8 \end{pmatrix}\right), \\ X_1 \text{ 与 } (X_2, X_3) \text{ 独立}. \end{cases}
$$
（"$\Leftarrow$"：独立的正态向量拼起来，联合特征函数是乘积，正是左边的特征函数。）

**定理 15.4.2** 如果 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，则 $X_1, X_2, \dots, X_n$ 相互独立的充要条件是

$$
\Sigma = \operatorname{diag}(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2).
$$

充分性是定理 15.4.1 的反复应用（或直接把特征函数分解成 $n$ 个因子的乘积）；必要性是因为独立蕴含不相关。例如 $\Sigma = \operatorname{diag}(4, 9, 8)$ 时 $X_1, X_2, X_3$ 相互独立。

所以对服从多元正态分布的随机向量，各分量"不相关"与"独立"等价。注意前提是联合正态：注 15.3.1 中的 $X, Y$ 各自正态、不相关，却不独立。

## 15.5. 条件分布

**定理 15.5.1（条件分布）** 设 $\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，$\det\Sigma > 0$，分块

$$
\boldsymbol{X} = \begin{pmatrix} \boldsymbol{X}_1 \\ \boldsymbol{X}_2 \end{pmatrix}, \qquad \boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \qquad \Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix},
$$
其中 $\boldsymbol{X}_1$、$\boldsymbol{\mu}_1$ 与方阵 $\Sigma_{11}$ 的行数相同。则在条件 $\boldsymbol{X}_1 = \boldsymbol{x}_1$ 下，$\boldsymbol{X}_2$ 服从多元正态分布

$$
\mathcal{N}\left(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1),\ \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\right).
$$

**证明** 令

$$
\begin{pmatrix} \boldsymbol{Y}_1 \\ \boldsymbol{Y}_2 \end{pmatrix} = \begin{pmatrix} I & O \\ -\Sigma_{21}\Sigma_{11}^{-1} & I \end{pmatrix}\begin{pmatrix} \boldsymbol{X}_1 - \boldsymbol{\mu}_1 \\ \boldsymbol{X}_2 - \boldsymbol{\mu}_2 \end{pmatrix}.
$$
由定理 15.3.2 并直接计算 $A\Sigma A^{\mathsf T}$（利用 $\Sigma_{12} = \Sigma_{21}^{\mathsf T}$），

$$
\begin{pmatrix} \boldsymbol{Y}_1 \\ \boldsymbol{Y}_2 \end{pmatrix} \sim \mathcal{N}\left(\boldsymbol{0}, \begin{pmatrix} \Sigma_{11} & O \\ O & \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12} \end{pmatrix}\right),
$$
（变换矩阵可逆，协方差矩阵仍正定）。由定理 15.4.1，$\boldsymbol{Y}_1 = \boldsymbol{X}_1 - \boldsymbol{\mu}_1$ 与 $\boldsymbol{Y}_2 = \boldsymbol{X}_2 - \boldsymbol{\mu}_2 - \Sigma_{21}\Sigma_{11}^{-1}\boldsymbol{Y}_1$ 独立，且 $\boldsymbol{Y}_2 \sim \mathcal{N}(\boldsymbol{0}, \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$。于是

$$
\boldsymbol{X}_2 = \boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{X}_1 - \boldsymbol{\mu}_1),
$$
从而

$$
\begin{aligned}
\mathbb{P}(\boldsymbol{X}_2 \le \boldsymbol{x}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1) &= \mathbb{P}(\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1) \le \boldsymbol{x}_2 \mid \boldsymbol{Y}_1 = \boldsymbol{x}_1 - \boldsymbol{\mu}_1) \\
&= \mathbb{P}(\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1) \le \boldsymbol{x}_2),
\end{aligned}
$$
最后一步用到 $\boldsymbol{Y}_2$ 与 $\boldsymbol{Y}_1$ 独立（不等号按分量理解）。即在 $\boldsymbol{X}_1 = \boldsymbol{x}_1$ 的条件下，$\boldsymbol{X}_2$ 与 $\boldsymbol{Y}_2 + \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1)$ 同分布，结论成立。 $\square$

条件期望 $\mathbb{E}(\boldsymbol{X}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1) = \boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1)$ 是 $\boldsymbol{x}_1$ 的线性函数，条件协方差矩阵 $\Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$（$\Sigma_{11}$ 的 Schur 补）与 $\boldsymbol{x}_1$ 无关。所以对多元正态分布，最佳预测（**条件期望**，[3.1.9](/3.1.9)）就是最佳线性预测（[3.1.10](/3.1.10)）。二元正态 $\mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$ 的情形：

$$
X_2 \mid X_1 = x_1 \sim \mathcal{N}\left(\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x_1 - \mu_1),\ \sigma_2^2(1 - \rho^2)\right).
$$

## 15.6. 常用应用

**例 15.6.1** 设 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$，$\Sigma$ 正定，则 $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_n$。

**证明** 由谱分解，$\Sigma^{-1} = P\Lambda P^{\mathsf T}$，$P$ 正交，$\Lambda$ 是正的对角矩阵，令 $\Sigma^{-1/2} = P\Lambda^{1/2}P^{\mathsf T}$（对称，且 $\Sigma^{-1/2}\Sigma\Sigma^{-1/2} = I_n$）。由定理 15.3.2，

$$
\boldsymbol{Y} = \Sigma^{-1/2}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \mathcal{N}(\boldsymbol{0}, I_n),
$$
由定理 15.4.2，$Y_1, \dots, Y_n$ 独立同分布于 $\mathcal{N}(0, 1)$，所以 $(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} = Y_1^2 + \cdots + Y_n^2 \sim \chi^2_n$（**卡方分布**，定义 7.1.1）。 $\square$

**例 15.6.2** 设 $\begin{pmatrix} X \\ Y \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \Sigma\right)$，$\Sigma = \begin{pmatrix} \sigma_{11} & \sigma_{12} \\ \sigma_{21} & \sigma_{22} \end{pmatrix}$ 正定。求 $X + Y$ 与 $X - Y$ 独立的充分必要条件。

**解** 令 $\begin{pmatrix} Z_1 \\ Z_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} X \\ Y \end{pmatrix}$，变换矩阵可逆，由定理 15.3.2，$(Z_1, Z_2)^{\mathsf T}$ 服从二元正态分布，协方差矩阵为

$$
\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\Sigma\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^{\mathsf T} = \begin{pmatrix} \sigma_{11} + 2\sigma_{12} + \sigma_{22} & \sigma_{11} - \sigma_{22} \\ \sigma_{11} - \sigma_{22} & \sigma_{11} - 2\sigma_{12} + \sigma_{22} \end{pmatrix}.
$$
由定理 15.4.2，$Z_1$ 与 $Z_2$ 独立当且仅当非对角元为 $0$，即 $\sigma_{11} = \sigma_{22}$（$X$ 与 $Y$ 的方差相等），与 $\sigma_{12}$ 无关。

**例 15.6.3（正态样本均值与样本方差）** 设 $X_1, \dots, X_n$ 相互独立，同服从 $\mathcal{N}(\mu, \sigma^2)$，$\bar X = \frac{1}{n}\sum_{i=1}^{n} X_i$ 为**样本均值**，$S_n^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2$ 为**样本方差**，则

1. $\bar X$ 与 $S_n^2$ 独立；
2. $\bar X \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$；
3. $\frac{(n-1)S_n^2}{\sigma^2} \sim \chi^2_{n-1}$。

**证明** 不妨设 $\mu = 0$，$\sigma = 1$（否则考虑 $(X_i - \mu)/\sigma$），则 $\boldsymbol{X} = (X_1, \dots, X_n)^{\mathsf T} \sim \mathcal{N}(\boldsymbol{0}, I_n)$。取一个正交矩阵 $Q$，其第一行为 $\left(\frac{1}{\sqrt{n}}, \dots, \frac{1}{\sqrt{n}}\right)$（把这个单位向量扩充为 $\mathbb{R}^n$ 的标准正交基），令 $\boldsymbol{Y} = Q\boldsymbol{X}$。由定理 15.3.2，$\boldsymbol{Y} \sim \mathcal{N}(\boldsymbol{0}, QQ^{\mathsf T}) = \mathcal{N}(\boldsymbol{0}, I_n)$，由定理 15.4.2，$Y_1, \dots, Y_n$ 独立同分布于 $\mathcal{N}(0, 1)$。而 $Y_1 = \sqrt{n}\,\bar X$，且由正交变换保持长度，

$$
(n-1)S_n^2 = \sum_{i=1}^{n} X_i^2 - n\bar X^2 = \boldsymbol{Y}^{\mathsf T}\boldsymbol{Y} - Y_1^2 = Y_2^2 + \cdots + Y_n^2.
$$
所以 $\bar X = Y_1/\sqrt{n} \sim \mathcal{N}(0, 1/n)$；$(n-1)S_n^2 \sim \chi^2_{n-1}$；前者只依赖 $Y_1$，后者只依赖 $Y_2, \dots, Y_n$，两者独立。 $\square$

这个定理是正态总体统计推断的基石（$t$ 检验、$\chi^2$ 检验、$F$ 检验，见 [3.2](/3.2)）；高维情形有类似的结论（Wishart 分布）。

## 15.7. 随机向量的极限定理

把随机向量的问题化为一维（Cramér–Wold 方法，定理 14.4.5），一维的大数定律与中心极限定理就推广到随机向量。

**定理 15.7.1** 设 $\boldsymbol{X}_1, \boldsymbol{X}_2, \dots$ 是独立同分布的 $k$ 维随机向量，$\mathbb{E}\boldsymbol{X}_1$ 存在，则

$$
\frac{\boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n}{n} \xrightarrow{\text{a.s.}} \mathbb{E}\boldsymbol{X}_1 \quad (\text{从而也依概率收敛}).
$$

**证明** 对每个分量 $j$，$X_{1j}, X_{2j}, \dots$ 独立同分布且期望存在，由强大数定律（定理 12.3.4），$\frac{1}{n}\sum_{i=1}^{n} X_{ij} \xrightarrow{\text{a.s.}} \mathbb{E}X_{1j}$。$k$ 个概率为 $1$ 的事件之交的概率仍为 $1$，即得向量的几乎处处收敛。 $\square$

例如 $\frac{1}{n}\sum_{i=1}^{n}(a\boldsymbol{X}_i + \boldsymbol{b}) \xrightarrow{\text{a.s.}} a\,\mathbb{E}\boldsymbol{X}_1 + \boldsymbol{b}$。

**定理 15.7.2（多元中心极限定理）** 设 $\boldsymbol{X}_1, \boldsymbol{X}_2, \dots$ 是独立同分布的 $k$ 维随机向量，$\mathbb{E}\boldsymbol{X}_1 = \boldsymbol{\mu}$，协方差矩阵 $\operatorname{Cov}(\boldsymbol{X}_1) = \Sigma$ 正定，$\boldsymbol{S}_n = \boldsymbol{X}_1 + \cdots + \boldsymbol{X}_n$，则

$$
\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, \Sigma), \qquad \Sigma^{-1/2} \cdot \frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, I_k).
$$

**证明** 任取常数向量 $\boldsymbol{a} \ne \boldsymbol{0}$。$\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n = \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1 + \cdots + \boldsymbol{a}^{\mathsf T}\boldsymbol{X}_n$ 是独立同分布随机变量之和，$\mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1) = \boldsymbol{a}^{\mathsf T}\boldsymbol{\mu}$，$\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}_1) = \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a} > 0$。由一维的中心极限定理（定理 13.1.1），

$$
\frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n - \mathbb{E}(\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n)}{\sqrt{\operatorname{Var}(\boldsymbol{a}^{\mathsf T}\boldsymbol{S}_n)}} = \frac{\boldsymbol{a}^{\mathsf T}(\boldsymbol{S}_n - n\boldsymbol{\mu})/\sqrt{n}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a}}} \xrightarrow{d} \mathcal{N}(0, 1),
$$
即 $\boldsymbol{a}^{\mathsf T}\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, \boldsymbol{a}^{\mathsf T}\Sigma\boldsymbol{a})$，而这正是 $\boldsymbol{a}^{\mathsf T}\boldsymbol{Z}$（$\boldsymbol{Z} \sim \mathcal{N}_k(\boldsymbol{0}, \Sigma)$）的分布（定理 15.3.3）。$\boldsymbol{a} = \boldsymbol{0}$ 时结论平凡。由定理 14.4.5 得第一个结论；第二个结论由连续映射定理（定理 14.4.1，线性映射 $\boldsymbol{x} \mapsto \Sigma^{-1/2}\boldsymbol{x}$）与定理 15.3.2 得到。 $\square$

**例 15.7.1（卡方检验的理论基础）** 结合例 15.6.1 与定理 15.7.2：记 $\boldsymbol{M}_n = \boldsymbol{S}_n/n$，由连续映射定理（$g(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}$），

$$
\left(\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}}\right)^{\mathsf T}\Sigma^{-1}\left(\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}}\right) = n(\boldsymbol{M}_n - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{M}_n - \boldsymbol{\mu}) \xrightarrow{d} \chi^2_k.
$$
这是 Pearson $\chi^2$ 拟合优度检验等大样本检验的理论基础（[3.2.6](/3.2.6)）。

## 小结

- 多元正态分布的三种等价定义：线性变换 $\boldsymbol{X} = \boldsymbol{\mu} + B\boldsymbol{\varepsilon}$（$BB^{\mathsf T}$ 满秩）；联合密度式 (15.1)；特征函数 $\exp[\mathrm{i}\boldsymbol{t}^{\mathsf T}\boldsymbol{\mu} - \frac{1}{2}\boldsymbol{t}^{\mathsf T}\Sigma\boldsymbol{t}]$。分布由期望向量 $\boldsymbol{\mu}$ 与协方差矩阵 $\Sigma$ 唯一决定。
- 线性变换封闭：$\boldsymbol{b} + A\boldsymbol{X} \sim \mathcal{N}(\boldsymbol{b} + A\boldsymbol{\mu}, A\Sigma A^{\mathsf T})$；边缘分布仍是正态。判定法则：$\boldsymbol{X}$ 多元正态当且仅当一切线性组合 $\boldsymbol{a}^{\mathsf T}\boldsymbol{X}$ 都是一元正态（仅分量正态不够）。
- 独立性：分块协方差为零（$\Sigma_{12} = O$）$\Leftrightarrow$ 两块独立；对联合正态的分量，不相关与独立等价。
- 条件分布：$\boldsymbol{X}_2 \mid \boldsymbol{X}_1 = \boldsymbol{x}_1 \sim \mathcal{N}(\boldsymbol{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\boldsymbol{x}_1 - \boldsymbol{\mu}_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$，条件期望线性、条件方差不依赖于 $\boldsymbol{x}_1$。
- 应用：$(\boldsymbol{X} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{X} - \boldsymbol{\mu}) \sim \chi^2_n$；正态样本的 $\bar X$ 与 $S_n^2$ 独立，$(n-1)S_n^2/\sigma^2 \sim \chi^2_{n-1}$。
- 随机向量的大数定律与中心极限定理：逐分量或经 Cramér–Wold 方法化为一维，$\frac{\boldsymbol{S}_n - n\boldsymbol{\mu}}{\sqrt{n}} \xrightarrow{d} \mathcal{N}_k(\boldsymbol{0}, \Sigma)$。
