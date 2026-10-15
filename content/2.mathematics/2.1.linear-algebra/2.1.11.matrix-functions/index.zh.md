---
title: 矩阵函数
---

本章回答两个问题。第一，复数有极形式 $z = re^{i\theta}$，矩阵能否也写成"伸缩乘以旋转"的形式 $A = Re^{iM}$？这需要先定义 $e^{iM}$，答案在 [第 13 章](/2.1.13)的极分解。第二，一元方程 $x'(t) = kx(t)$ 的解是 $x(t) = x(0)e^{kt}$；方程组 $X'(t) = AX(t)$ 的解能否写成 $X(t) = e^{At}X(0)$？两个问题都要求把复函数 $f: \mathbb{C} \to \mathbb{C}$ 推广为矩阵上的映射 $f: M_n(\mathbb{C}) \to M_n(\mathbb{C})$。

离散数学中已经用幂级数定义过**矩阵指数**并讨论了它与李群的关系（[1.3.5](/1.3.5)）。本章给出 $f(A)$ 的三种等价定义——Jordan 标准形上的谱定义、插值多项式、幂级数——以及相应的三种算法，并比较它们的代价。准备工作是把微积分（[2.2](/2.2)）中的极限、导数、级数搬到矩阵上；主要工具是[上一章](/2.1.10)的 Jordan 标准形与极小多项式，以及[第 9 章](/2.1.9)的 **Lagrange 插值多项式**。核心结论是：$f(A)$ 只依赖于 $f$ 及其导数在 $A$ 的特征值处的有限个值，因此计算 $f(A)$ 可以归结为解一个线性方程组。最后一节用矩阵指数求解线性常系数微分方程组，它是常微分方程（[2.4](/2.4)）的起点。

## 11.1. 函数矩阵

**定义 11.1.1** 以区间 $[a, b]$ 上的实函数 $a_{ij}(x)$ 为元素的矩阵 $A(x) = (a_{ij}(x))_{m \times n}$ 称为**函数矩阵**。

例如 $A(x) = \begin{pmatrix} \sin x & e^x & 1 \\ 3x^2 & 0 & x - 1 \end{pmatrix}$。数字矩阵是函数矩阵的特例。函数矩阵的加法、与函数 $k(x)$ 的数乘、乘法 $A(x)B(x) = \left(\sum_k a_{ik}(x)b_{kj}(x)\right)$ 和转置都与数字矩阵相同。

**定义 11.1.2** 设 $A(x)$ 是 $n$ 阶函数矩阵。若存在 $n$ 阶函数矩阵 $B(x)$，使对任意 $x \in [a, b]$ 都有 $A(x)B(x) = B(x)A(x) = I$，则称 $A(x)$ 在 $[a, b]$ 上可逆，记 $B(x) = A^{-1}(x)$。$A(x)$ 中不恒等于零的子式的最高阶数称为 $A(x)$ 的秩；$n$ 阶函数矩阵的秩为 $n$ 时称为满秩。

**定理 11.1.1** $n$ 阶函数矩阵 $A(x)$ 在 $[a, b]$ 上可逆 $\Leftrightarrow$ $\det A(x)$ 在 $[a, b]$ 上处处不为零。此时 $A^{-1}(x) = \dfrac{1}{\det A(x)}\operatorname{adj}A(x)$，$\operatorname{adj}A(x)$ 是**伴随矩阵**。

与数字矩阵不同，满秩不等于可逆：$A(x) = \begin{pmatrix} x & 0 \\ 0 & 1 \end{pmatrix}$ 在 $[-1, 1]$ 上 $\det A(x) = x$ 不恒为零，秩为 $2$；但 $\det A(0) = 0$，它在 $[-1, 1]$ 上不可逆。满秩只要求行列式不恒为零，可逆要求它处处不为零。

**定义 11.1.3** 若 $A(x)$ 的每个元素在 $x_0$ 处有极限（连续、可导），则称 $A(x)$ 在 $x_0$ 处有极限（连续、可导），并逐元素定义

$$
\lim_{x \to x_0} A(x) = \left(\lim_{x \to x_0} a_{ij}(x)\right), \qquad A'(x) = \frac{\mathrm{d}A}{\mathrm{d}x} = \left(a_{ij}'(x)\right), \qquad \int_a^b A(x)\,\mathrm{d}x = \left(\int_a^b a_{ij}(x)\,\mathrm{d}x\right).
$$

**性质 11.1.1** 设 $A(x)$、$B(x)$ 可导，大小使运算有意义。

1. $(A + B)' = A' + B'$，$(A^{\mathsf T})' = (A')^{\mathsf T}$，$(\operatorname{tr}A)' = \operatorname{tr}A'$；
2. $(AB)' = A'B + AB'$，因子的顺序不能交换，所以 $(A^2)' = A'A + AA'$，一般不等于 $2AA'$；
3. 若 $A(x)$ 可逆，则 $(A^{-1})' = -A^{-1}A'A^{-1}$（对 $AA^{-1} = I$ 求导）；
4. 若 $x = u(t)$ 可导，则 $\dfrac{\mathrm{d}}{\mathrm{d}t}A(u(t)) = A'(u(t))\,u'(t)$。

## 11.2. 函数向量的线性相关性

**定义 11.2.1** 设 $\alpha_1(x), \dots, \alpha_m(x)$ 是 $[a, b]$ 上连续的 $n$ 维函数向量。若存在不全为零的实数 $k_1, \dots, k_m$，使 $k_1\alpha_1(x) + \cdots + k_m\alpha_m(x) = 0$ 对所有 $x \in [a, b]$ 成立，则称它们在 $[a, b]$ 上线性相关，否则称为线性无关。

系数必须是常数。按定义判断需要对无穷多个 $x$ 同时成立，下面两种方法把它化成一个数字矩阵的秩。

**定义 11.2.2** 称 $m$ 阶矩阵 $G = (g_{ij})$，$g_{ij} = \displaystyle\int_a^b \alpha_i^{\mathsf T}(x)\alpha_j(x)\,\mathrm{d}x$ 为 $\alpha_1(x), \dots, \alpha_m(x)$ 的 **Gram 矩阵**，$\det G$ 称为 Gram 行列式。

**定理 11.2.1** $[a, b]$ 上连续的函数向量 $\alpha_1(x), \dots, \alpha_m(x)$ 线性无关 $\Leftrightarrow$ 它们的 Gram 矩阵满秩。

**证明** 设 $\sum_j k_j\alpha_j(x) = 0$ (\*)。左乘 $\alpha_i^{\mathsf T}(x)$ 并积分，得 $\sum_j g_{ij}k_j = 0$，即 $Gk = 0$，$k = (k_1, \dots, k_m)^{\mathsf T}$。若 $G$ 满秩，则 $k = 0$，向量组线性无关。若 $G$ 不满秩，取 $Gk = 0$ 的非零解，令 $\alpha(x) = \sum_i k_i\alpha_i(x)$，则

$$
\int_a^b \alpha^{\mathsf T}(x)\alpha(x)\,\mathrm{d}x = k^{\mathsf T}Gk = 0.
$$

被积函数 $\|\alpha(x)\|^2$ 连续且非负，所以 $\alpha(x) \equiv 0$，(\*) 有非零解，向量组线性相关。 $\square$

$g_{ij}$ 是 $\alpha_i, \alpha_j$ 在积分内积下的内积，[下一章](/2.1.12)将看到 Gram 矩阵就是一般内积空间中一组向量的度量矩阵。若函数向量足够光滑，还可以用导数判别。

**定义 11.2.3** 设 $\alpha_1(x), \dots, \alpha_m(x)$ 在 $[a, b]$ 上有 $m - 1$ 阶导数，$A(x)$ 是以 $\alpha_i^{\mathsf T}(x)$ 为第 $i$ 行的 $m \times n$ 函数矩阵。称 $m \times mn$ 矩阵 $W(x) = \left(A(x), A'(x), \dots, A^{(m-1)}(x)\right)$ 为 $\alpha_1(x), \dots, \alpha_m(x)$ 的 **Wronski 矩阵**。

**定理 11.2.2** 若存在 $x_0 \in [a, b]$ 使数字矩阵 $W(x_0)$ 的秩为 $m$，则 $\alpha_1(x), \dots, \alpha_m(x)$ 在 $[a, b]$ 上线性无关。

**证明** 反证。若 $\sum_j k_j\alpha_j(x) = 0$ 有非零解 $k$，逐次求导得 $\sum_j k_j\alpha_j^{(l)}(x) = 0$（$l = 0, \dots, m - 1$），在 $x_0$ 处写成矩阵形式为 $W^{\mathsf T}(x_0)k = 0$，于是 $\operatorname{rank}(W(x_0)) < m$，矛盾。 $\square$

这个条件只是充分的。取 $n = 1$，$\alpha_1(x) = x^2$，$\alpha_2(x) = x|x|$，它们在 $[-1, 1]$ 上线性无关（在 $[0, 1]$ 上相等，在 $[-1, 0]$ 上相反），但 $W(x) = \begin{pmatrix} x^2 & 2x \\ x|x| & 2|x| \end{pmatrix}$ 的行列式 $2x^2|x| - 2x^2|x|$ 恒为零。

## 11.3. 矩阵序列与矩阵级数

**定义 11.3.1** 设 $A_k = (a_{ij}^{(k)}) \in M_n(\mathbb{C})$。若 $n^2$ 个数列 $\{a_{ij}^{(k)}\}$ 都收敛到 $a_{ij}$，则称矩阵序列 $\{A_k\}$ 收敛，$A = (a_{ij})$ 为它的极限，记作 $\lim_{k \to \infty}A_k = A$；否则称为发散。

**性质 11.3.1** 若 $A_k \to A$，$B_k \to B$，则

1. $aA_k + bB_k \to aA + bB$（$a, b \in \mathbb{C}$）；
2. $A_kB_k \to AB$；
3. $PA_kQ \to PAQ$（$P, Q$ 为固定矩阵）；
4. 若 $A$ 与所有 $A_k$ 可逆，则 $A_k^{-1} \to A^{-1}$（由伴随矩阵公式，逆矩阵的元素是元素的连续函数）。

矩阵幂 $A^k$ 的收敛性只取决于特征值。

**定义 11.3.2** $A \in M_n(\mathbb{C})$ 的**谱半径**是 $\rho(A) = \max\{|\lambda| : \lambda \text{ 是 } A \text{ 的特征值}\}$。

**定理 11.3.1** $\lim_{k \to \infty}A^k = O$ $\Leftrightarrow$ $\rho(A) < 1$。

**证明** 由 Jordan 标准形 $A = PJP^{-1}$，$A^k = PJ^kP^{-1}$，只需考虑一个 Jordan 块。$J_{\lambda,m} = \lambda I + N$，$N^m = O$，$\lambda I$ 与 $N$ 可交换，由二项式定理

$$
J_{\lambda,m}^k = \sum_{j=0}^{m-1} \binom{k}{j}\lambda^{k-j}N^j,
$$

它的元素是 $\binom{k}{j}\lambda^{k-j}$（$0 \le j \le m - 1$）。若 $|\lambda| < 1$，$k$ 的多项式乘以 $|\lambda|^k$ 趋于零；若 $|\lambda| \ge 1$，对角元 $\lambda^k$ 不趋于零。 $\square$

谱半径与范数的关系：对任一特征值 $\lambda$ 与单位特征向量 $x$，$|\lambda| = \|Ax\| \le \|A\|_2$，所以 $\rho(A)$ 不超过**谱范数**；可以证明 $\rho(A) = \lim_{k\to\infty}\|A^k\|_2^{1/k}$。$\rho(A)$ 决定 $A^k$ 最终的指数增长率，但前若干步的行为还取决于 $A$ 偏离"正规"的程度：下图中两个矩阵的谱半径都是 $0.9$，上三角那个的 $\|A^k\|_2$ 先增长到 $6$ 左右才开始衰减。这一现象与[下一章](/2.1.12)的正规矩阵有关。

![三个 2 阶矩阵的幂的谱范数随 k 的变化：谱半径决定极限行为，非正规矩阵有暂态增长](./plots/matrix-powers-spectral-radius.py)

**定义 11.3.3** 称 $A_1 + A_2 + \cdots$ 为**矩阵级数**，$S_k = A_1 + \cdots + A_k$ 为部分和。若 $\lim_{k \to \infty}S_k = S$，则称级数收敛，和为 $S = \sum_{k=1}^\infty A_k$；否则称为发散。若 $n^2$ 个数项级数 $\sum_k a_{ij}^{(k)}$ 都绝对收敛，则称矩阵级数绝对收敛。

显然，矩阵级数收敛当且仅当 $n^2$ 个数项级数都收敛，和的元素就是它们的和。

**定理 11.3.2** 设 $A \in M_n(\mathbb{C})$，则 $\sum_{k=0}^\infty A^k$ 收敛 $\Leftrightarrow$ $\rho(A) < 1$，此时 $\sum_{k=0}^\infty A^k = (I - A)^{-1}$。

**证明** 若级数收敛，一般项 $A^k \to O$，由定理 11.3.1 得 $\rho(A) < 1$。反之，若 $\rho(A) < 1$，则 $1$ 不是 $A$ 的特征值，$I - A$ 可逆。由 $(I - A)(I + A + \cdots + A^k) = I - A^{k+1} \to I$，得部分和趋于 $(I - A)^{-1}$。 $\square$

**定理 11.3.3** 记 $|A| = \max_{i,j}|a_{ij}|$。

1. $\sum_k A_k$ 绝对收敛 $\Leftrightarrow$ 数项级数 $\sum_k |A_k|$ 收敛；
2. 若 $\sum_k A_k$ 绝对收敛，$P, Q$ 是固定矩阵，则 $\sum_k PA_kQ$ 也绝对收敛，且 $\sum_k PA_kQ = P\left(\sum_k A_k\right)Q$；
3. （比较判别法）若 $B_k = (b_{ij}^{(k)})$ 的元素非负、$|a_{ij}^{(k)}| \le b_{ij}^{(k)}$，且 $\sum_k B_k$ 收敛，则 $\sum_k A_k$ 绝对收敛。

**证明** 1：$|a_{ij}^{(k)}| \le |A_k| \le \sum_{i,j}|a_{ij}^{(k)}|$，再用数项级数的比较判别法。2：$PA_kQ$ 的每个元素的模不超过 $n^2|P||A_k||Q|$。3：逐元素比较。 $\square$

## 11.4. 矩阵多项式

先看最简单的情形：$f(x) = a_kx^k + \cdots + a_1x + a_0$ 是多项式，$f(A) = a_kA^k + \cdots + a_1A + a_0I$。由[上一章](/2.1.10)的引理 10.5.1，$f(P^{-1}AP) = P^{-1}f(A)P$，而分块对角阵的多项式是各块的多项式。于是若 $P^{-1}AP = J = \operatorname{diag}(J_{\mu_1, m_{11}}, \dots)$ 是 Jordan 标准形，

$$
f(A) = Pf(J)P^{-1} = P\operatorname{diag}\left(f(J_{\mu_1, m_{11}}), \dots\right)P^{-1},
$$

问题化为计算一个 Jordan 块的多项式。

**定理 11.4.1** 设 $f$ 是多项式，$J_{\lambda,m}$ 是 $m$ 阶 Jordan 块，则

$$
f(J_{\lambda,m}) = \begin{pmatrix} f(\lambda) & f'(\lambda) & \frac{1}{2!}f''(\lambda) & \cdots & \frac{1}{(m-1)!}f^{(m-1)}(\lambda) \\ & f(\lambda) & f'(\lambda) & \ddots & \vdots \\ & & \ddots & \ddots & \frac{1}{2!}f''(\lambda) \\ & & & f(\lambda) & f'(\lambda) \\ & & & & f(\lambda) \end{pmatrix} = \sum_{j=0}^{m-1} \frac{f^{(j)}(\lambda)}{j!}N^j. \tag{11.1}
$$

**证明** 由**泰勒公式**，多项式 $f$ 在 $\lambda$ 处的展开 $f(x) = \sum_{j \ge 0} \frac{f^{(j)}(\lambda)}{j!}(x - \lambda)^j$ 是有限和，精确成立。代入 $x = J_{\lambda,m} = \lambda I + N$，$N = J_{0,m}$ 满足 $N^m = O$，而 $N^j$ 是第 $j$ 条上对角线为 $1$、其余为 $0$ 的矩阵。 $\square$

**例 11.4.1** $J_{2,3} = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$，$f(x) = x^3$。$f(2) = 8$，$f'(2) = 12$，$\frac{1}{2}f''(2) = 6$，故 $J_{2,3}^3 = \begin{pmatrix} 8 & 12 & 6 \\ 0 & 8 & 12 \\ 0 & 0 & 8 \end{pmatrix}$。

所以计算 $f(A)$ 只需要知道 $f$ 在每个特征值 $\mu_i$ 处直到 $m_i - 1$ 阶的导数值，$m_i$ 是关于 $\mu_i$ 的最大 Jordan 块的阶数，即 $\mu_i$ 在极小多项式中的重数。这个观察给出了一般函数的定义。

## 11.5. 矩阵函数的谱定义

**定义 11.5.1（矩阵的谱）** 设 $A \in M_n(\mathbb{C})$ 的极小多项式为 $m_A(\lambda) = (\lambda - \mu_1)^{m_1}\cdots(\lambda - \mu_s)^{m_s}$，$\mu_i$ 互不相同。称 $\sigma(A) = \{\mu_1, \dots, \mu_s\}$ 为 $A$ 的**谱**。设 $f$ 是复函数，若

$$
f(\mu_i), f'(\mu_i), \dots, f^{(m_i - 1)}(\mu_i), \qquad i = 1, \dots, s
$$

都有定义，则称 $f$ 在 $A$ 的谱上有定义，这 $m = \deg m_A$ 个数称为 $f$ 在 $A$ 的谱上的值。

**定义 11.5.2** 设 $f$ 在 $A$ 的谱上有定义，$P^{-1}AP = J$ 是 Jordan 标准形。对 Jordan 块按式 (11.1) 定义 $f(J_{\lambda,k})$，并称下面的 $f(A)$ 为**矩阵函数**：

$$
f(A) = Pf(J)P^{-1} = P\operatorname{diag}\left(f(J_{\mu_1, m_{11}}), \dots, f(J_{\mu_s, m_{st_s}})\right)P^{-1}.
$$

定理 11.6.1 将说明 $f(A)$ 与 Jordan 基 $P$ 的选取无关。多值函数（如 $\ln z$、$\sqrt{z}$）要在每个特征值附近取定一个分支，不同的分支给出不同的 $f(A)$。

**性质 11.5.1** 设 $f, g$ 在 $A$ 的谱上有定义，$\det(\lambda I - A) = \prod_i(\lambda - \mu_i)^{n_i}$。

1. $P^{-1}f(A)P = f(P^{-1}AP)$，且 $f(A)$ 与 $A$ 可交换；
2. $(f + g)(A) = f(A) + g(A)$，$(fg)(A) = f(A)g(A)$（对式 (11.1) 用 Leibniz 公式）；
3. $\det(\lambda I - f(A)) = \prod_i (\lambda - f(\mu_i))^{n_i}$，即 $f(A)$ 的特征值是 $f(\mu_i)$，重数不变（$f(J)$ 是上三角阵）；
4. $e^A$ 总是可逆的，$(e^A)^{-1} = e^{-A}$（由 2 与 $e^ze^{-z} = 1$；也可由 3 得 $\det e^A = \prod e^{n_i\mu_i} \ne 0$）；
5. 若 $A$ 可对角化，$P^{-1}AP = \operatorname{diag}(\mu_1I_{n_1}, \dots, \mu_sI_{n_s})$，则 $f(A) = P\operatorname{diag}(f(\mu_1)I_{n_1}, \dots, f(\mu_s)I_{n_s})P^{-1}$ 也可对角化。

**例 11.5.1** $J = J_{0,3}$，$f(z) = \sin z$。$m_J = \lambda^3$，$f(0) = 0$，$f'(0) = 1$，$f''(0) = 0$，故 $\sin J = J$。

**例 11.5.2** $A = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 2 & 0 & 1 & 0 \\ 0 & -2 & 0 & 0 \\ 4 & 0 & 2 & 0 \end{pmatrix}$，求 $e^A$。$\det(\lambda I_4 - A) = \lambda^4$，$\operatorname{rank}(A) = 2$，$\operatorname{rank}(A^2) = 1$，$A^3 = O$，故 $J = \operatorname{diag}(J_{0,3}, J_{0,1})$，$m_A = \lambda^3$。取 Jordan 基 $P = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ -2 & 0 & 1 & 0 \\ 0 & 2 & 0 & 1 \end{pmatrix}$（第 1、2、3 列是一条 Jordan 链，第 4 列是另一个特征向量）。由 $f(z) = e^z$，$f(0) = f'(0) = f''(0) = 1$，

$$
e^J = \operatorname{diag}\left(\begin{pmatrix} 1 & 1 & \frac12 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}, 1\right), \qquad e^A = Pe^JP^{-1} = \begin{pmatrix} 2 & 1 & \frac12 & 0 \\ 2 & 1 & 1 & 0 \\ -2 & -2 & 0 & 0 \\ 4 & 0 & 2 & 1 \end{pmatrix}.
$$

**例 11.5.3** 若 $A \ne O$，$A^2 = O$，则 $m_A = \lambda^2$，Jordan 块只有 $J_{0,2}$ 和 $J_{0,1}$。$e^{J_{0,2}} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = I + J_{0,2}$，$e^{J_{0,1}} = 1$，所以 $e^J = I + J$，$e^A = P(I + J)P^{-1} = I + A$。

## 11.6. 插值法

例 11.5.2 中 $A^3 = O$，直接看 $e^A = I + A + \frac{1}{2}A^2$ 似乎更快：右边恰好是 $f(z) = e^z$ 在 $0$ 处的二次 Taylor 多项式。一般地，$f(A)$ 总等于某个低次多项式在 $A$ 处的值。

**定理 11.6.1** 设 $m_A(\lambda) = \prod_{i=1}^s(\lambda - \mu_i)^{m_i}$，$m = \deg m_A$，$f$ 在 $A$ 的谱上有定义。则存在唯一的次数小于 $m$ 的多项式 $r(z)$，使

$$
r^{(j)}(\mu_i) = f^{(j)}(\mu_i), \qquad i = 1, \dots, s, \quad j = 0, 1, \dots, m_i - 1,
$$

并且 $f(A) = r(A)$。$r(z)$ 称为 $f$ 关于 $A$ 的谱的 Hermite 插值多项式（Hermite interpolation polynomial），课件称为 Hermite–Lagrange 插值多项式。

**证明** 次数小于 $m$ 的多项式构成 $m$ 维空间，映射 $r \mapsto \left(r^{(j)}(\mu_i)\right)_{i,j} \in \mathbb{C}^m$ 是线性的。它是单射：若所有这些值为零，则 $(z - \mu_i)^{m_i} \mid r$ 对每个 $i$ 成立，从而 $m_A \mid r$，而 $\deg r < m$，故 $r = 0$。维数相同，所以它也是满射，$r$ 存在且唯一。对 $A$ 的每个 Jordan 块 $J_{\mu_i, k}$（$k \le m_i$），式 (11.1) 只用到 $f^{(j)}(\mu_i)$，$j < k$，因此 $f(J_{\mu_i,k}) = r(J_{\mu_i,k})$，$f(A) = Pr(J)P^{-1} = r(A)$。右边与 $P$ 无关，所以定义 11.5.2 不依赖于 Jordan 基的选取。 $\square$

所有 $m_i = 1$（$A$ 可对角化）时，$r$ 就是过点 $(\mu_i, f(\mu_i))$ 的 Lagrange 插值多项式，于是

$$
f(A) = \sum_{i=1}^s f(\mu_i)\prod_{j \ne i}\frac{A - \mu_jI}{\mu_i - \mu_j}.
$$

定理 11.6.1 把求 $f(A)$ 化成了解一个 $m$ 阶线性方程组（带导数条件的 Vandermonde 方程组），不需要 Jordan 基。

**算法 11.6.1（待定系数法）** 输入 $A$ 与在 $A$ 的谱上有定义的 $f$。

1. 求 $A$ 的极小多项式 $m_A(\lambda) = \prod_{i=1}^s(\lambda - \mu_i)^{m_i}$，$m = \sum_i m_i$。不知道极小多项式时，可用特征多项式代替（它也是化零多项式，只是方程组更大）。
2. 设 $r(z) = a_0 + a_1z + \cdots + a_{m-1}z^{m-1}$。
3. 由 $r^{(j)}(\mu_i) = f^{(j)}(\mu_i)$ 列出 $m$ 个线性方程，解出 $a_0, \dots, a_{m-1}$。
4. $f(A) = r(A) = a_0I + a_1A + \cdots + a_{m-1}A^{m-1}$。

**例 11.6.1** $A = \begin{pmatrix} -4 & 2 & 10 \\ -4 & 3 & 7 \\ -3 & 1 & 7 \end{pmatrix}$，求 $\cos A$。$\det(\lambda I - A) = (\lambda - 2)^3$，$\operatorname{rank}(2I - A) = 2$，只有一个 Jordan 块，$m_A = (\lambda - 2)^3$。设 $r(z) = a_0 + a_1z + a_2z^2$，由 $r(2) = \cos 2$，$r'(2) = -\sin 2$，$r''(2) = -\cos 2$：

$$
\begin{cases} a_0 + 2a_1 + 4a_2 = \cos 2, \\ a_1 + 4a_2 = -\sin 2, \\ 2a_2 = -\cos 2, \end{cases} \qquad a_0 = 2\sin 2 - \cos 2, \quad a_1 = 2\cos 2 - \sin 2, \quad a_2 = -\tfrac12\cos 2.
$$

于是

$$
\cos A = a_0I + a_1A + a_2A^2 = \begin{pmatrix} 2\cos 2 + 6\sin 2 & -2\sin 2 & -2\cos 2 - 10\sin 2 \\ \frac12\cos 2 + 4\sin 2 & \cos 2 - \sin 2 & -\cos 2 - 7\sin 2 \\ \frac12\cos 2 + 3\sin 2 & -\sin 2 & -5\sin 2 \end{pmatrix}.
$$

**例 11.6.2** $A = \begin{pmatrix} 3 & -3 & 2 \\ -1 & 5 & -2 \\ -1 & 3 & 0 \end{pmatrix}$，求 $\ln A$、$\sin\frac{\pi}{4}A$ 与 $e^A$。$\det(\lambda I - A) = (\lambda - 2)^2(\lambda - 4)$，极小多项式是 $(\lambda - 2)^2(\lambda - 4)$ 或 $(\lambda - 2)(\lambda - 4)$；由 $\operatorname{rank}(A - 2I) = 1$，$\lambda = 2$ 有两个 Jordan 块，$m_A = (\lambda - 2)(\lambda - 4)$。设 $r(z) = a_0 + a_1z$。

- $\ln$：$a_0 + 2a_1 = \ln 2$，$a_0 + 4a_1 = 2\ln 2$，得 $a_0 = 0$，$a_1 = \frac12\ln 2$，$\ln A = \frac{\ln 2}{2}A$。
- $\sin\frac{\pi}{4}z$：$a_0 + 2a_1 = 1$，$a_0 + 4a_1 = 0$，得 $a_0 = 2$，$a_1 = -\frac12$，$\sin\frac{\pi}{4}A = 2I - \frac12A = \begin{pmatrix} \frac12 & \frac32 & -1 \\ \frac12 & -\frac12 & 1 \\ \frac12 & -\frac32 & 2 \end{pmatrix}$。
- $e^z$：$a_0 + 2a_1 = e^2$，$a_0 + 4a_1 = e^4$，$e^A = (2e^2 - e^4)I + \frac12(e^4 - e^2)A$。

下面的代码按算法 11.6.1 求解带导数条件的 Vandermonde 方程组，计算 $e^A$，并与 SciPy 的 `expm` 对比。

```python
import numpy as np
from math import factorial
from scipy.linalg import expm

def matrix_function(A, spectrum, derivs):
    """f(A) by Hermite interpolation on the spectrum.

    spectrum: list of (eigenvalue, multiplicity in the minimal polynomial)
    derivs:   derivs(mu, j) returns the j-th derivative of f at mu
    """
    m = sum(k for _, k in spectrum)              # degree of m_A
    V = np.zeros((m, m), dtype=complex)          # confluent Vandermonde matrix
    b = np.zeros(m, dtype=complex)
    row = 0
    for mu, k in spectrum:
        for j in range(k):                       # condition r^{(j)}(mu) = f^{(j)}(mu)
            for p in range(j, m):
                V[row, p] = factorial(p) / factorial(p - j) * mu ** (p - j)
            b[row] = derivs(mu, j)
            row += 1
    a = np.linalg.solve(V, b)                    # coefficients of r(z)
    R, P = np.zeros_like(A, dtype=complex), np.eye(len(A))
    for coef in a:                               # accumulate a_0 I + a_1 A + ...
        R += coef * P
        P = P @ A
    return R

A = np.array([[-4., 2, 10], [-4, 3, 7], [-3, 1, 7]])     # m_A = (z - 2)^3
E = matrix_function(A, [(2, 3)], lambda mu, j: np.exp(mu))
print(np.abs(E - expm(A)).max())                         # ~1e-13
B = np.array([[3., -3, 2], [-1, 5, -2], [-1, 3, 0]])     # m_B = (z - 2)(z - 4)
E = matrix_function(B, [(2, 1), (4, 1)], lambda mu, j: np.exp(mu))
print(np.abs(E - expm(B)).max())
```

插值法对小矩阵和精确计算很方便，但它需要准确的特征值和重数，而带导数条件的 Vandermonde 方程组在特征值相近时病态。数值软件中的 `expm` 采用"缩放与平方"配合有理逼近：先算 $e^{A/2^s}$（$\|A/2^s\|$ 很小，用 Padé 逼近），再平方 $s$ 次。

## 11.7. 幂级数定义

第三种定义直接把幂级数中的 $z$ 换成 $A$，它与 [1.3.5](/1.3.5) 中矩阵指数的定义一致。设 $S(z) = \sum_{p=0}^\infty a_pz^p$ 的收敛半径为 $R$：$|z| < R$ 时绝对收敛，$|z| > R$ 时发散；逐项求导后的级数有相同的收敛半径（[2.2.8](/2.2.8)）。常用的展开有

$$
e^z = \sum_{p=0}^\infty \frac{z^p}{p!}, \quad \sin z = \sum_{p=0}^\infty \frac{(-1)^pz^{2p+1}}{(2p+1)!}, \quad \cos z = \sum_{p=0}^\infty \frac{(-1)^pz^{2p}}{(2p)!} \quad (R = +\infty), \qquad \ln(1 + z) = \sum_{p=1}^\infty \frac{(-1)^{p-1}z^p}{p} \quad (R = 1).
$$

**定义 11.7.1** 对 $A \in M_n(\mathbb{C})$，令 $S(A) = \sum_{p=0}^\infty a_pA^p$；若部分和 $S_p(A) = a_0I + \cdots + a_pA^p$ 收敛，则称 $S(A)$ 收敛。

**定理 11.7.1** 设幂级数 $S(z)$ 的收敛半径为 $R$，在 $|z| < R$ 内的和函数为 $f(z)$。若 $A$ 的所有特征值满足 $|\mu_i| < R$（即 $\rho(A) < R$），则 $S(A)$ 绝对收敛，且 $S(A) = f(A)$，其中 $f(A)$ 按谱定义计算。若有某个 $|\mu_i| > R$，则 $S(A)$ 发散。

**证明** $S_p(A) = PS_p(J)P^{-1}$。由式 (11.1)，$S_p(J_{\lambda,k})$ 的元素是 $\frac{1}{j!}S_p^{(j)}(\lambda)$，即 $S$ 的 $j$ 阶导级数的部分和。$|\lambda| < R$ 时它们绝对收敛到 $\frac{1}{j!}f^{(j)}(\lambda)$，所以 $S_p(J) \to f(J)$；$|\lambda| > R$ 时对角元 $S_p(\lambda)$ 发散。 $\square$

课件此处的推论写成"若 $S(z)$ 的收敛半径为 $R$，则 $|\mu_i| < R$"，方向颠倒了；正确的是上面的定理：特征值都在收敛圆内时级数收敛。

由定理 11.7.1，$e^A$、$\sin A$、$\cos A$ 对一切 $A$ 收敛；$\rho(A) < 1$ 时 $\ln(I + A) = A - \frac12A^2 + \frac13A^3 - \cdots$，并且 $\sum_k A^k = (I - A)^{-1}$（定理 11.3.2）正是 $f(z) = \frac{1}{1 - z}$ 的情形。对满足特殊关系的矩阵，幂级数可以直接求和：

**例 11.7.1** 若 $A^2 = O$，则 $e^A = I + A$，$\sin A = A$，$\cos A = I$（与例 11.5.3 一致）。若 $A^2 = A$，则 $A^k = A$（$k \ge 1$），

$$
e^A = I + \left(1 + \frac{1}{2!} + \frac{1}{3!} + \cdots\right)A = I + (e - 1)A.
$$

## 11.8. 矩阵指数

**定义 11.8.1（矩阵指数）** 对 $A \in M_n(\mathbb{C})$ 与 $t \in \mathbb{R}$（或 $\mathbb{C}$），

$$
e^{At} = \sum_{k=0}^\infty \frac{t^k}{k!}A^k = I + tA + \frac{t^2}{2!}A^2 + \cdots.
$$

由定理 11.7.1，级数对一切 $A$、$t$ 绝对收敛，且等于 $f(z) = e^{tz}$ 在 $A$ 处的矩阵函数。

**定理 11.8.1** 设 $A, B \in M_n(\mathbb{C})$，$P$ 可逆。

1. 若 $AB = BA$，则 $e^{A+B} = e^Ae^B$；
2. $e^{P^{-1}AP} = P^{-1}e^AP$；
3. $\det e^A = e^{\operatorname{tr}A}$；
4. $\dfrac{\mathrm{d}}{\mathrm{d}t}e^{At} = Ae^{At} = e^{At}A$。

**证明** 1：$A, B$ 可交换时二项式定理成立，两个绝对收敛级数的 Cauchy 乘积按 $e^{x+y} = e^xe^y$ 的同样方式重排。2：性质 11.5.1。3：由性质 11.5.1 的第 3 条，$e^A$ 的特征值是 $e^{\lambda_1}, \dots, e^{\lambda_n}$（计重数），乘积为 $e^{\lambda_1 + \cdots + \lambda_n}$。4：幂级数逐项求导。 $\square$

可交换的条件不能去掉：$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$，$e^Ae^B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$，而 $A + B$ 的特征值为 $\pm 1$，$e^{A+B} = \begin{pmatrix} \cosh 1 & \sinh 1 \\ \sinh 1 & \cosh 1 \end{pmatrix}$。

计算 $e^{At}$ 时，由 $P^{-1}AP = J$ 得 $e^{At} = Pe^{Jt}P^{-1}$。对 Jordan 块，$J_{\lambda,m}t = \lambda tI + tN$ 的两项可交换，

$$
e^{J_{\lambda,m}t} = e^{\lambda t}e^{tN} = e^{\lambda t}\left(I + tN + \frac{t^2}{2!}N^2 + \cdots + \frac{t^{m-1}}{(m-1)!}N^{m-1}\right). \tag{11.2}
$$

这也是 $f(z) = e^{tz}$ 代入式 (11.1) 的结果（$f^{(j)}(\lambda) = t^je^{\lambda t}$）。注意 $tJ_{\lambda,m}$ 的上对角线是 $t$，它本身不是 Jordan 块，不能把它当作 Jordan 块再套用式 (11.1)。

**例 11.8.1** $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$，$m_A = \lambda^2 + 1$，谱为 $\{i, -i\}$。用插值法，设 $r(z) = a_0 + a_1z$，由 $a_0 + ia_1 = e^{it}$，$a_0 - ia_1 = e^{-it}$ 得 $a_0 = \cos t$，$a_1 = \sin t$，所以

$$
e^{At} = \cos t\,I + \sin t\,A = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}.
$$

$A^2 = -I$，$A$ 在这里扮演虚数单位的角色，这个等式就是**欧拉公式** $e^{it} = \cos t + i\sin t$ 的矩阵版本；$\{e^{At}\}$ 是平面旋转构成的**单参数子群**。

**例 11.8.2** 若 $P^{-1}AP = J = \operatorname{diag}(J_{2,1}, J_{4,2})$，则由式 (11.2)，

$$
e^{At} = P\begin{pmatrix} e^{2t} & 0 & 0 \\ 0 & e^{4t} & te^{4t} \\ 0 & 0 & e^{4t} \end{pmatrix}P^{-1}.
$$

**定理 11.8.2** 设 $B \in M_n(\mathbb{C})$，则存在 $X$ 使 $e^X = B$ $\Leftrightarrow$ $B$ 可逆。

**证明** 必要性：$\det e^X = e^{\operatorname{tr}X} \ne 0$。充分性：由定理 11.8.1 的第 2 条，只需对 $B$ 的每个 Jordan 块 $J_{\lambda,k}$（$\lambda \ne 0$）找到 $X$。写 $J_{\lambda,k} = \lambda(I + M)$，$M = \lambda^{-1}N$ 幂零。取 $\lambda$ 的一个对数 $\ell$（$e^\ell = \lambda$），令

$$
X = \ell I + L, \qquad L = \ln(I + M) = M - \frac{M^2}{2} + \cdots + \frac{(-1)^kM^{k-1}}{k-1},
$$

级数因 $M^k = O$ 而有限。形式幂级数恒等式 $\exp(\ln(1 + z)) = 1 + z$ 对幂零矩阵代入后成立，所以 $e^L = I + M$；$\ell I$ 与 $L$ 可交换，$e^X = e^\ell e^L = \lambda(I + M) = J_{\lambda,k}$。 $\square$

对数不唯一：$e^{2\pi i I} = I = e^O$。实矩阵也未必有实对数，例如 $\operatorname{diag}(-1, 2)$ 没有实对数：对实矩阵 $X$，$e^X$ 关于负特征值的 Jordan 块总是成对出现（来自 $X$ 的一对共轭复特征值 $\ell, \bar\ell$）。

## 11.9. 线性常系数微分方程组

设 $X(t) = (x_1(t), \dots, x_n(t))^{\mathsf T}$，$A \in M_n(\mathbb{C})$ 是常数矩阵，求解 $X'(t) = AX(t)$。仿照一元方程：$e^{-At}$ 与 $A$ 可交换，由性质 11.1.1 与定理 11.8.1，

$$
\left(e^{-At}X(t)\right)' = -Ae^{-At}X(t) + e^{-At}X'(t) = e^{-At}\left(X'(t) - AX(t)\right).
$$

**定理 11.9.1** 方程组 $X'(t) = AX(t)$ 满足初值 $X(0) = x_0$ 的解存在且唯一，为 $X(t) = e^{At}x_0$。因此通解是 $X(t) = e^{At}c$，即 $e^{At}$ 各列的任意线性组合。

**证明** 由定理 11.8.1 的第 4 条，$e^{At}x_0$ 是解。反之若 $X(t)$ 是解，则上式右边为零，$e^{-At}X(t)$ 是常向量，等于 $X(0) = x_0$，于是 $X(t) = e^{At}x_0$。 $\square$

**推论 11.9.1** 设 $P^{-1}AP = J$。$X'(t) = AX(t)$ 的通解为 $X(t) = Pe^{Jt}c$（$c = P^{-1}x_0$ 为任意常向量）。具体地，若 $p_1, \dots, p_k$ 是关于特征值 $\lambda$ 的一条 Jordan 链（$p_1$ 是特征向量），则它给出 $k$ 个线性无关的解

$$
e^{\lambda t}p_1, \quad e^{\lambda t}(tp_1 + p_2), \quad e^{\lambda t}\left(\frac{t^2}{2!}p_1 + tp_2 + p_3\right), \quad \dots, \quad e^{\lambda t}\sum_{j=1}^{k}\frac{t^{k-j}}{(k-j)!}p_j.
$$

**证明** $Pe^{Jt}c = e^{At}Pc$ 是解，$Pc$ 取遍 $\mathbb{C}^n$。$Pe^{Jt}$ 的列由式 (11.2) 直接写出。 $\square$

可以验证，形如 $e^{\lambda t}\left(\frac{t^{k-1}}{(k-1)!}\alpha_1 + \cdots + t\alpha_{k-1} + \alpha_k\right)$（$\alpha_1 \ne 0$）的函数是解，当且仅当 $\alpha_1, \dots, \alpha_k$ 是关于 $\lambda$ 的 Jordan 链。所以解方程组就是求 Jordan 链。

**例 11.9.1** 求解

$$
\begin{cases} x_1' = 6x_1 + 2x_2 + 2x_3, \\ x_2' = -2x_1 + 2x_2, \\ x_3' = 2x_3, \end{cases} \qquad A = \begin{pmatrix} 6 & 2 & 2 \\ -2 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}.
$$

$\det(\lambda I - A) = (\lambda - 2)(\lambda - 4)^2$，$\operatorname{rank}(A - 4I) = 2$，关于 $4$ 只有一个块，$J = \operatorname{diag}(2, J_{4,2})$。$(A - 2I)x = 0$ 得 $p_1 = (0, -1, 1)^{\mathsf T}$；$(A - 4I)x = 0$ 得 $p_2 = (2, -2, 0)^{\mathsf T}$；$(A - 4I)x = p_2$ 得 $p_3 = (1, 0, 0)^{\mathsf T}$。通解为

$$
X(t) = c_1e^{2t}\begin{pmatrix} 0 \\ -1 \\ 1 \end{pmatrix} + c_2e^{4t}\begin{pmatrix} 2 \\ -2 \\ 0 \end{pmatrix} + c_3e^{4t}\left(t\begin{pmatrix} 2 \\ -2 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}\right).
$$

给定初值 $X(0) = x_0$ 时，$c = P^{-1}x_0$，$P = (p_1, p_2, p_3)$。例如 $x_0 = (1, 0, 0)^{\mathsf T} = p_3$ 时 $c = (0, 0, 1)^{\mathsf T}$，$X(t) = e^{4t}(1 + 2t, -2t, 0)^{\mathsf T}$。

非齐次方程组的解由齐次解加上输入的"累积响应"组成。

**定理 11.9.2** 设 $B \in \mathbb{C}^{n \times m}$，$u(t)$ 是连续的 $m$ 维函数向量。方程组 $X'(t) = AX(t) + Bu(t)$ 满足 $X(0) = x_0$ 的解存在且唯一，为

$$
X(t) = e^{At}x_0 + \int_0^t e^{A(t-\tau)}Bu(\tau)\,\mathrm{d}\tau. \tag{11.3}
$$

**证明** 设 $X(t)$ 是解，则 $\left(e^{-At}X(t)\right)' = e^{-At}\left(X' - AX\right) = e^{-At}Bu(t)$。从 $0$ 到 $t$ 积分：$e^{-At}X(t) - x_0 = \int_0^t e^{-A\tau}Bu(\tau)\,\mathrm{d}\tau$，两边左乘 $e^{At}$ 即得式 (11.3)，这同时证明了唯一性；直接求导可验证式 (11.3) 确实是解。 $\square$

式 (11.3) 称为常数变易公式（variation of constants formula）：把齐次解 $e^{At}c$ 中的常向量 $c$ 换成函数 $c(t)$ 代入方程，就得到 $c'(t) = e^{-At}Bu(t)$。它是控制理论中线性系统响应的基本公式。

系数随时间变化的方程组 $X'(t) = A(t)X(t)$ 一般不能写成矩阵指数：只有当 $A(t)$ 与 $\int_0^tA(s)\,\mathrm{d}s$ 可交换时，$e^{\int_0^tA(s)\mathrm{d}s}$ 才是解。一般情形用基本解矩阵 $\Phi(t)$（$\Phi' = A\Phi$，$\Phi(0) = I$）代替 $e^{At}$，它满足 $\det\Phi(t) = e^{\int_0^t\operatorname{tr}A(s)\,\mathrm{d}s}$，非齐次方程的解为 $X(t) = \Phi(t)x_0 + \Phi(t)\int_0^t\Phi^{-1}(\tau)B(\tau)u(\tau)\,\mathrm{d}\tau$。这些内容留给常微分方程课程。

## 小结

| 主题 | 结论 |
|---|---|
| 函数矩阵 | 逐元素定义运算与微积分；可逆 $\Leftrightarrow$ 行列式处处非零；$(AB)' = A'B + AB'$，$(A^{-1})' = -A^{-1}A'A^{-1}$ |
| 函数向量的相关性 | Gram 矩阵满秩 $\Leftrightarrow$ 无关（定理 11.2.1）；Wronski 矩阵在一点满秩 $\Rightarrow$ 无关（定理 11.2.2） |
| 矩阵序列与级数 | $A^k \to O \Leftrightarrow \rho(A) < 1$；$\sum A^k = (I - A)^{-1} \Leftrightarrow \rho(A) < 1$；绝对收敛看 $\sum \lvert A_k\rvert$ |
| 矩阵函数 | 只依赖于 $f^{(j)}(\mu_i)$，$j < m_i$；三种定义一致（定理 11.6.1、11.7.1） |
| 矩阵指数 | 可交换时 $e^{A+B} = e^Ae^B$；$\det e^A = e^{\operatorname{tr}A}$；$e^X = B$ 可解 $\Leftrightarrow$ $B$ 可逆 |
| 微分方程组 | $X' = AX$：$X = e^{At}x_0$，基本解由 Jordan 链给出；非齐次：常数变易公式 (11.3) |

计算 $f(A)$ 的三种方法比较如下。

| 方法 | 需要什么 | 主要计算 | 适用场合 |
|---|---|---|---|
| Jordan 表示 $f(A) = Pf(J)P^{-1}$ | Jordan 形与 Jordan 基 $P$ | 逐链解方程组、求 $P^{-1}$ | 理论推导；同时需要 $f(A)$ 的结构（如解微分方程组的基本解） |
| 插值法（算法 11.6.1） | 极小多项式（或特征多项式）与 $f$ 在谱上的值 | 解 $m$ 阶线性方程组、算 $A^{m-1}$ 以内的幂 | 小矩阵、精确计算；不需要 $P$ |
| 幂级数 | $\rho(A)$ 小于收敛半径 | 级数截断 | $A$ 满足 $A^k = O$、$A^2 = A$ 等关系时可直接求和；数值上与缩放、有理逼近配合使用 |

三种方法把"矩阵上的函数"分别化成了三个标准问题：化 Jordan 形，解一个线性方程组，求数项级数的和。插值法最能体现本课程的思路——一个看似需要无穷多信息的问题，被拆解成了有限个数值和一个线性方程组。
