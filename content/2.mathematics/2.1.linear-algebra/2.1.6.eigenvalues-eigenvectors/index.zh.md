---
title: 特征值与特征向量
---

前几章研究的是单个线性映射 $\boldsymbol{x} \mapsto A\boldsymbol{x}$：它的值域、零点（解集）与最优逼近。本章研究线性变换的迭代：$A^t\boldsymbol{x}$ 在 $t$ 很大时如何变化，是否存在不变的方向。关键是方程 $A\boldsymbol{x} = \lambda\boldsymbol{x}$：如果能找到 $n$ 个线性无关的向量，$A$ 在每个方向上都只是伸缩，那么在这组基下 $A$ 就是对角矩阵，$A^t$ 也就一目了然。

本章的路线是：由两个例子引出特征值问题，并因此进入复数域；用**行列式**定义特征多项式，求特征值与特征向量；讨论特征值的性质（圆盘定理、迹与行列式）；研究矩阵何时可对角化（代数重数与几何重数）；最后引入相似关系，证明任意方阵都相似于上三角矩阵，由此得到 Cayley–Hamilton 定理，并陈述 Jordan 标准形。本章依赖第 3 章的**秩**与**维数**、第 5 章的行列式；第 7 章把本章的结论用于实对称矩阵（谱分解与正交对角化），[第 10 章](/2.1.10)证明 Jordan 标准形，[第 11 章](/2.1.11)用它定义矩阵函数。特征值也是图的谱、Markov 链与种群模型的核心工具。

## 6.1. 问题的引入

**例 6.1.1（人口迁移）** 设 $\mathbb{R}^2$ 上的线性变换

$$
A\colon \boldsymbol{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \mapsto A\boldsymbol{x} = \begin{bmatrix} 0.6 & 0.1 \\ 0.4 & 0.9 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

描述甲、乙两地人口一年间的流动：甲地每年有 $40\%$ 的人迁往乙地，乙地有 $10\%$ 的人迁往甲地。长时间后人口分布如何？是否存在稳定的分布？两个问题可以表述为：

1. $A^t$（$t \in \mathbb{N}$）在 $t \to \infty$ 时的极限；
2. 是否存在 $\boldsymbol{x} \ne \boldsymbol{0}$ 使 $A\boldsymbol{x} = \boldsymbol{x}$。

先看第 2 个问题：$A\boldsymbol{x} = \boldsymbol{x}$ 即 $(I_2 - A)\boldsymbol{x} = \boldsymbol{0}$，而 $I_2 - A = \begin{bmatrix} 0.4 & -0.1 \\ -0.4 & 0.1 \end{bmatrix}$ 不满秩，$\mathcal{N}(I_2 - A) = \operatorname{span}(\boldsymbol{x}_1)$，$\boldsymbol{x}_1 = \begin{bmatrix} 0.2 \\ 0.8 \end{bmatrix}$，所以存在稳定分布。

再看第 1 个问题。若还能找到与 $\boldsymbol{x}_1$ 线性无关的 $\boldsymbol{x}_2$ 满足 $A\boldsymbol{x}_2 = k\boldsymbol{x}_2$，则任意 $\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + \ell_2\boldsymbol{x}_2$ 满足 $A^t\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + \ell_2k^t\boldsymbol{x}_2$。$(kI_2 - A)\boldsymbol{x}_2 = \boldsymbol{0}$ 有非零解当且仅当

$$
\det(kI_2 - A) = \begin{vmatrix} k - 0.6 & -0.1 \\ -0.4 & k - 0.9 \end{vmatrix} = k^2 - 1.5k + 0.5 = 0,
$$

它有两个根 $1$ 和 $0.5$。取 $k = 0.5$ 得 $\boldsymbol{x}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$。于是 $A^t\boldsymbol{x} = \ell_1\boldsymbol{x}_1 + 0.5^t\ell_2\boldsymbol{x}_2 \to \ell_1\boldsymbol{x}_1$。用矩阵表示：令 $X = [\boldsymbol{x}_1\ \boldsymbol{x}_2]$，$\Lambda = \operatorname{diag}(1, 0.5)$，则 $AX = X\Lambda$，$A = X\Lambda X^{-1}$，

$$
A^t = X\Lambda^tX^{-1} = \begin{bmatrix} 0.2 & 1 \\ 0.8 & -1 \end{bmatrix}\begin{bmatrix} 1 & \\ & 0.5^t \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 0.8 & -0.2 \end{bmatrix} = \begin{bmatrix} 0.2 + 0.8 \cdot 0.5^t & 0.2 - 0.2 \cdot 0.5^t \\ 0.8 - 0.8 \cdot 0.5^t & 0.8 + 0.2 \cdot 0.5^t \end{bmatrix} \to \begin{bmatrix} 0.2 & 0.2 \\ 0.8 & 0.8 \end{bmatrix}.
$$

对任意初始分布 $\boldsymbol{x}$，$A^t\boldsymbol{x} \to (x_1 + x_2)\boldsymbol{x}_1$：总人口不变，最终按 $1 : 4$ 分布在两地。

这里的关键是方程组 $A\boldsymbol{x} = \lambda\boldsymbol{x}$，其中 $\lambda$ 不是给定的参数，而是要由 $A$ 确定的、使方程组有非零解的数。它表示 $\boldsymbol{x}$ 在变换下的像 $A\boldsymbol{x}$ 与 $\boldsymbol{x}$ 共线。

**例 6.1.2（平面上的保距变换）** 由例 4.3.1，$\mathbb{R}^2$ 上的保距变换有反射与旋转两类：

$$
H_\theta = \begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}, \qquad R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix},
$$

$H_\theta$ 是关于与 $x_1$ 轴夹角为 $\theta$ 的直线的反射。对反射，$\det(\lambda I_2 - H_\theta) = \lambda^2 - 1$，$\lambda = \pm 1$，相应的解为 $\begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$（反射轴方向，不动）与 $\begin{bmatrix} -\sin\theta \\ \cos\theta \end{bmatrix}$（法方向，反向），与几何直观一致。对旋转，

$$
\det(\lambda I_2 - R_\theta) = \begin{vmatrix} \lambda - \cos\theta & \sin\theta \\ -\sin\theta & \lambda - \cos\theta \end{vmatrix} = \lambda^2 - 2\lambda\cos\theta + 1,
$$

$\lambda = \cos\theta \pm \mathrm{i}\sin\theta$。$\theta = k\pi$（$k \in \mathbb{Z}$）时得二重根 $\lambda = (-1)^k$，$\lambda I_2 - R_\theta = O$，每个向量都满足 $R_\theta\boldsymbol{x} = (-1)^k\boldsymbol{x}$；$\theta \ne k\pi$ 时两个根都不是实数，没有实向量满足 $R_\theta\boldsymbol{x} \parallel \boldsymbol{x}$——旋转确实没有不变的方向。要让方程总有解，必须把 $R_\theta$ 看作 $\mathbb{C}^2$ 上的线性变换。

### 6.1.1. 复矩阵与复向量

对 $n$ 阶方阵 $A$，$A\boldsymbol{x} = \lambda\boldsymbol{x}$ 有非零解当且仅当

$$
0 = \det(\lambda I_n - A) = \begin{vmatrix} \lambda - a_{11} & -a_{12} & \cdots & -a_{1n} \\ -a_{21} & \lambda - a_{22} & \cdots & -a_{2n} \\ \vdots & \vdots & & \vdots \\ -a_{n1} & -a_{n2} & \cdots & \lambda - a_{nn} \end{vmatrix}.
$$

由行列式的完全展开（定理 5.7.1），右端是关于 $\lambda$ 的首项系数为 $1$ 的 $n$ 次多项式。求多项式的根必然要用到复数，因此本章在复数集 $\mathbb{C}$ 上考虑向量和矩阵，除非特别说明。实矩阵的矩阵运算、线性方程组、子空间、基与维数、行列式等概念和结论都可以原样推广到复矩阵。内积与正交性是例外：复向量 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{C}^n$ 的内积要定义为 $\boldsymbol{a}^{\mathsf H}\boldsymbol{b} = \overline{\boldsymbol{a}}^{\mathsf T}\boldsymbol{b}$，见[第 12 章](/2.1.12)。

对 $a, b \in \mathbb{R}$，复数 $a + b\mathrm{i}$ 的共轭记为 $\overline{a + b\mathrm{i}} = a - b\mathrm{i}$。共轭保持加法和乘法：$\overline{z + w} = \bar{z} + \bar{w}$，$\overline{zw} = \bar{z}\,\bar{w}$。复矩阵的共轭 $\bar{A}$ 是逐元素取共轭，同样有 $\overline{AB} = \bar{A}\,\bar{B}$。复数与复向量空间的系统讨论见[第 9 章](/2.1.9)。

## 6.2. 多项式的根

本节只陈述后面需要的多项式结论，多项式的系统理论见[第 9 章](/2.1.9)。

**定理 6.2.1** 复系数一元 $n$ 次多项式（$n \ge 1$）在 $\mathbb{C}$ 上至少有一个根。

这就是**代数基本定理**，其证明需要分析或拓扑的工具，这里不给出。

**推论 6.2.1** 复系数一元 $n$ 次多项式 $p(x)$ 在 $\mathbb{C}$ 上恰有 $n$ 个根（计重数）。设 $p(x)$ 的全部不同的根为 $x_1, \dots, x_s$，则

$$
p(x) = a_0(x - x_1)^{n_1}(x - x_2)^{n_2}\cdots(x - x_s)^{n_s}, \qquad n_1 + \cdots + n_s = n,
$$

$n_i$ 称为根 $x_i$ 的重数，$x_i$ 称为 $p(x)$ 的 $n_i$ 重根。

**证明** 设 $p(x) = a_0x^n + a_1x^{n-1} + \cdots + a_n$，由定理 6.2.1 存在根 $x_1$。由

$$
p(x) = p(x) - p(x_1) = a_0(x^n - x_1^n) + a_1(x^{n-1} - x_1^{n-1}) + \cdots + a_{n-1}(x - x_1)
$$

及 $x^k - x_1^k = (x - x_1)(x^{k-1} + x^{k-2}x_1 + \cdots + x_1^{k-1})$，得 $p(x) = (x - x_1)q(x)$，$q$ 是 $n-1$ 次多项式。对 $q$ 重复这一步即得结论。$\square$

**定理 6.2.2** 设复系数多项式 $p(x) = a_0x^n + a_1x^{n-1} + \cdots + a_n$（$a_0 \ne 0$）的 $n$ 个根（计重数）为 $x_1, \dots, x_n$，则对 $k = 1, \dots, n$，

$$
(-1)^k\frac{a_k}{a_0} = \sum_{1 \le i_1 < \cdots < i_k \le n} x_{i_1}x_{i_2}\cdots x_{i_k}.
$$

特别地，$-\dfrac{a_1}{a_0} = x_1 + \cdots + x_n$，$(-1)^n\dfrac{a_n}{a_0} = x_1x_2\cdots x_n$。

这组根与系数的关系称为 **Vieta 定理**。

**证明** 把 $p(x) = a_0(x - x_1)\cdots(x - x_n)$ 展开，$x^{n-k}$ 的系数为 $a_0(-1)^k\sum_{i_1 < \cdots < i_k}x_{i_1}\cdots x_{i_k}$，与 $a_k$ 比较即得。$\square$

**命题 6.2.1** 若 $a + b\mathrm{i}$ 是实系数多项式 $p(x)$ 的根，则 $\overline{a + b\mathrm{i}} = a - b\mathrm{i}$ 也是它的根，且二者重数相同。

**证明** 设 $p(x) = \sum_k a_kx^{n-k}$，$a_k \in \mathbb{R}$。共轭保持加法与乘法，故 $p(\bar{z}) = \sum_k a_k\bar{z}^{\,n-k} = \overline{\sum_k a_kz^{n-k}} = \overline{p(z)}$，$p(z) = 0$ 推出 $p(\bar{z}) = 0$。对因式分解 $p(x) = a_0\prod(x - x_i)^{n_i}$ 两边取共轭，由分解的唯一性知 $z$ 与 $\bar{z}$ 重数相同。$\square$

## 6.3. 特征值与特征向量

### 6.3.1. 定义

**定义 6.3.1（特征值与特征向量）** 设 $A$ 是 $n$ 阶方阵。若对复数 $\lambda \in \mathbb{C}$，存在非零向量 $\boldsymbol{x} \in \mathbb{C}^n$ 使 $A\boldsymbol{x} = \lambda\boldsymbol{x}$，则称 $\lambda$ 为 $A$（在 $\mathbb{C}$ 上）的一个**特征值**，$\boldsymbol{x}$ 为 $A$ 的属于特征值 $\lambda$ 的一个**特征向量**，二元组 $(\lambda, \boldsymbol{x})$ 称为 $A$ 的一个**特征对**。若 $\lambda \in \mathbb{R}$，$\boldsymbol{x} \in \mathbb{R}^n$，则称它们为 $A$ 在 $\mathbb{R}$ 上的特征值、特征向量与特征对。

只有方阵才有特征值和特征向量。零向量不是特征向量；若 $\boldsymbol{x}$ 是特征向量，则对任意 $k \ne 0$，$k\boldsymbol{x}$ 也是属于同一特征值的特征向量，所以我们关心的是线性无关的特征向量。$(\lambda_0, \boldsymbol{x}_0)$ 是特征对当且仅当 $\boldsymbol{x}_0$ 是 $\mathcal{N}(\lambda_0I_n - A)$ 中的非零向量。

**命题 6.3.1** 数 $\lambda_0$ 是 $A$ 的特征值当且仅当 $\det(\lambda_0I_n - A) = 0$。特别地，$0$ 是 $A$ 的特征值当且仅当 $A$ 不可逆；若 $\lambda_0$ 不是 $A$ 的特征值，则 $\lambda_0I_n - A$ 可逆。

**证明** $(\lambda_0I_n - A)\boldsymbol{x} = \boldsymbol{0}$ 有非零解，当且仅当 $\lambda_0I_n - A$ 不可逆，当且仅当其行列式为零（定理 5.2.1）。$\square$

**定义 6.3.2（特征多项式）** $n$ 阶方阵 $A$ 的**特征多项式**为 $p_A(\lambda) = \det(\lambda I_n - A)$，它是关于 $\lambda$ 的首项系数为 $1$ 的 $n$ 次多项式。

于是 $\lambda_0$ 是 $A$ 的特征值当且仅当它是 $p_A$ 的根。由推论 6.2.1，$n$ 阶方阵在 $\mathbb{C}$ 上恰有 $n$ 个特征值（计重数），在 $\mathbb{R}$ 上则可能一个也没有（例 6.1.2 中的旋转）。

**定义 6.3.3（特征子空间）** 设 $\lambda_0$ 是 $A$ 的特征值，零空间 $\mathcal{N}(\lambda_0I_n - A)$ 称为 $A$ 的属于 $\lambda_0$ 的**特征子空间**。

属于 $\lambda_0$ 的特征向量的全体就是 $\mathcal{N}(\lambda_0I_n - A) \setminus \{\boldsymbol{0}\}$，它非空；$\mathcal{N}(\lambda_0I_n - A)$ 的一组基就是属于 $\lambda_0$ 的一组极大的线性无关特征向量。

### 6.3.2. 计算

**算法 6.3.1（计算特征值与特征向量）** 输入 $n$ 阶方阵 $A$。

1. 计算特征多项式 $p_A(\lambda) = \det(\lambda I_n - A)$；
2. 求 $p_A(\lambda)$ 的全部根，即 $A$ 的全部特征值；
3. 对每个不同的特征值 $\lambda_i$，用 Gauss 消元求齐次线性方程组 $(\lambda_iI_n - A)\boldsymbol{x} = \boldsymbol{0}$ 的解空间 $\mathcal{N}(\lambda_iI_n - A)$ 的一组基 $\boldsymbol{x}_{i,1}, \dots, \boldsymbol{x}_{i,r_i}$，它们就是属于 $\lambda_i$ 的线性无关的特征向量。

这是手算的标准流程。数值计算中并不求特征多项式的根（根对系数的扰动非常敏感），而是用 QR 迭代等算法直接计算特征值，这属于数值线性代数的内容；反过来，求多项式的根可以化为求友矩阵的特征值（6.4.4 节）。

**例 6.3.1** 求 $A = \begin{bmatrix} 7 & -5 & 5 \\ -2 & 3 & -2 \\ -10 & 10 & -8 \end{bmatrix}$ 的特征值与特征向量。

特征多项式为

$$
p_A(\lambda) = \begin{vmatrix} \lambda - 7 & 5 & -5 \\ 2 & \lambda - 3 & 2 \\ 10 & -10 & \lambda + 8 \end{vmatrix} = (\lambda - 2)(\lambda^2 + 1),
$$

特征值为 $\lambda_1 = 2$，$\lambda_2 = \mathrm{i}$，$\lambda_3 = -\mathrm{i}$。解 $(\lambda_iI_3 - A)\boldsymbol{x} = \boldsymbol{0}$：

1. $\lambda_1 = 2$：$2I_3 - A = \begin{bmatrix} -5 & 5 & -5 \\ 2 & -1 & 2 \\ 10 & -10 & 10 \end{bmatrix}$，特征向量 $\boldsymbol{x}_1 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$，$(2, \boldsymbol{x}_1)$ 是 $A$ 在 $\mathbb{R}$ 上的特征对；
2. $\lambda_2 = \mathrm{i}$：$\mathrm{i}I_3 - A = \begin{bmatrix} -7 + \mathrm{i} & 5 & -5 \\ 2 & -3 + \mathrm{i} & 2 \\ 10 & -10 & 8 + \mathrm{i} \end{bmatrix}$，特征向量 $\boldsymbol{x}_2 = \begin{bmatrix} -\frac{1}{2} \\ \frac{3 + \mathrm{i}}{10} \\ 1 \end{bmatrix}$；
3. $\lambda_3 = -\mathrm{i}$：特征向量 $\boldsymbol{x}_3 = \overline{\boldsymbol{x}_2} = \begin{bmatrix} -\frac{1}{2} \\ \frac{3 - \mathrm{i}}{10} \\ 1 \end{bmatrix}$（见命题 6.4.1）。

**例 6.3.2**

1. **对角矩阵** $D = \operatorname{diag}(d_1, \dots, d_n)$ 的特征值就是对角元 $d_1, \dots, d_n$，标准基 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_n$ 是 $n$ 个线性无关的特征向量。$I_n$ 只有特征值 $1$，任意非零向量都是特征向量。
2. **三角矩阵**的特征值就是对角元（$\lambda I_n - T$ 仍是三角矩阵）。但特征向量的个数可以不同：$\begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix}$ 有特征值 $1, 2$，特征向量 $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$、$\begin{bmatrix} 1 \\ 1 \end{bmatrix}$，两个一维特征子空间；$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 只有特征值 $1$，只有一个线性无关的特征向量 $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$。
3. 旋转 $R_\theta$：$\theta = k\pi$ 时特征值为 $(-1)^k$，特征子空间是整个 $\mathbb{C}^2$；$\theta \ne k\pi$ 时有两个复特征值 $\cos\theta \pm \mathrm{i}\sin\theta$，对应的特征向量为 $\begin{bmatrix} 1 \\ \mp\mathrm{i} \end{bmatrix}$。

下图左边的实矩阵有特征值 $2.5$ 和 $1$：单位圆变成椭圆，一般的向量 $\boldsymbol{x}$ 被变换后方向改变，只有两条特征方向上的向量只被伸缩。右边的 $0.9R_{\pi/6}$ 有一对共轭复特征值 $0.9\,\mathrm{e}^{\pm\mathrm{i}\pi/6}$，每个向量都被转过 $\pi/6$ 并缩短为 $0.9$ 倍，没有实的不变方向，迭代 $B^t\boldsymbol{x}_0$ 沿螺线收缩到原点：复特征值的辐角是转角，模是伸缩倍数。

![左：A = [2 1; 0.5 1.5] 把单位圆变成椭圆，灰色箭头从 x 指向 Ax，只有两条特征方向上的向量保持方向；右：B = 0.9 R_{π/6} 把每个向量旋转并缩短，没有实特征向量，轨道 B^t x_0 是收缩的螺线](./plots/eigen-directions.py)

## 6.4. 特征值的性质

### 6.4.1. 圆盘定理

特征值的大致位置可以直接由矩阵元素估计。

**定理 6.4.1（Gershgorin 圆盘定理）** 对 $n$ 阶方阵 $A = [a_{ij}]$，在复平面上定义 $n$ 个圆盘

$$
G_i(A) = \Big\{z \in \mathbb{C} \;\Big|\; |z - a_{ii}| \le \sum_{j \ne i}|a_{ij}|\Big\}, \qquad i = 1, \dots, n,
$$

则 $A$ 的每个特征值都落在某个圆盘中，即全部特征值都在 $G_1(A) \cup \cdots \cup G_n(A)$ 中。

**证明** 设 $\lambda_0$ 是特征值，则 $\lambda_0I_n - A$ 不可逆。若 $\lambda_0$ 不在任何一个圆盘中，则对每个 $i$ 有 $|\lambda_0 - a_{ii}| > \sum_{j \ne i}|a_{ij}|$，即 $\lambda_0I_n - A$ 是（严格）**对角占优矩阵**，从而可逆（第 2 章），矛盾。$\square$

**注 6.4.1** 更精细的结论（证明用到特征值对矩阵元素的连续依赖）：若其中 $k$ 个圆盘的并与其余 $n - k$ 个圆盘不相交，则这个并中恰有 $k$ 个特征值（计重数）。对 $A^{\mathsf T}$ 应用定理 6.4.1，还可以用列和代替行和。下图中四个圆盘两两不交，每个圆盘里恰有一个特征值；矩阵为

$$
A = \begin{bmatrix} 6 & 1 & 0.5 & 0 \\ 0.5 & 2 & 0 & 0.5 \\ 1 & 1 & -3 & 1 \\ 0 & 0.5 & 0.5 & 3 + 2.5\mathrm{i} \end{bmatrix}.
$$

![一个 4 阶复矩阵的 Gershgorin 圆盘与特征值：四个圆盘两两不交，每个圆盘中恰有一个特征值](./plots/gershgorin-discs.py)

### 6.4.2. 代数重数与共轭特征值

**定义 6.4.1（代数重数）** 设 $\lambda_0$ 是 $n$ 阶方阵 $A$ 的特征值。若 $\lambda_0$ 是特征多项式 $p_A(\lambda)$ 的 $n_0$ 重根，则称 $n_0$ 为 $\lambda_0$ 的**代数重数**（简称重数），称 $\lambda_0$ 是 $A$ 的 $n_0$ 重特征值。$1$ 重特征值称为**单特征值**。

**命题 6.4.1** 若 $n$ 阶实方阵 $A$ 有非实数的特征值 $\lambda_0$，则 $\overline{\lambda_0}$ 也是 $A$ 的特征值，且二者代数重数相等。进一步，若 $\boldsymbol{x}_0$ 是属于 $\lambda_0$ 的特征向量，则 $\overline{\boldsymbol{x}_0}$ 是属于 $\overline{\lambda_0}$ 的特征向量。

**证明** $p_A$ 是实系数多项式，由命题 6.2.1 即得关于特征值的结论。对 $A\boldsymbol{x}_0 = \lambda_0\boldsymbol{x}_0$ 取共轭，由 $\bar{A} = A$ 得 $A\overline{\boldsymbol{x}_0} = \overline{\lambda_0}\,\overline{\boldsymbol{x}_0}$。$\square$

例 6.3.1 中的 $\pm\mathrm{i}$ 与例 6.3.2 中旋转的 $\cos\theta \pm \mathrm{i}\sin\theta$ 都是这样的共轭对，对应的特征向量也互为共轭。

### 6.4.3. 迹与行列式

**定理 6.4.2** 设 $A = [a_{ij}]$ 是 $n$ 阶方阵，则其特征多项式具有形式

$$
p_A(\lambda) = \lambda^n - \operatorname{tr}(A)\lambda^{n-1} + \cdots + (-1)^n\det A,
$$

其中 $\operatorname{tr}(A) = a_{11} + \cdots + a_{nn}$ 是 $A$ 的**迹**。

**证明** 在 $\det(\lambda I_n - A)$ 的完全展开式中，每一项是来自不同行、不同列的 $n$ 个元素之积，只有对角元含 $\lambda$。要得到 $\lambda^{n-1}$，至少要取 $n-1$ 个对角元，而剩下的一个元素与它们不同行不同列，只能也是对角元。所以 $\lambda^{n-1}$ 项只来自 $(\lambda - a_{11})\cdots(\lambda - a_{nn})$，系数为 $-(a_{11} + \cdots + a_{nn})$。常数项为 $p_A(0) = \det(-A) = (-1)^n\det A$。$\square$

**推论 6.4.1** 设 $A$ 的 $n$ 个特征值（计重数）为 $\lambda_1, \dots, \lambda_n$，则

$$
\lambda_1 + \lambda_2 + \cdots + \lambda_n = \operatorname{tr}(A), \qquad \lambda_1\lambda_2\cdots\lambda_n = \det A.
$$

**证明** 由定理 6.4.2 与 Vieta 定理（定理 6.2.2）。$\square$

这两个等式在习题中常用来确定未知参数或检验计算结果。例如例 6.3.1 中 $2 + \mathrm{i} - \mathrm{i} = 2 = 7 + 3 - 8$，$2 \cdot \mathrm{i} \cdot (-\mathrm{i}) = 2 = \det A$。

**性质 6.4.1** 设 $(\lambda_0, \boldsymbol{x})$ 是 $A$ 的特征对。

1. 对正整数 $k$，$(\lambda_0^k, \boldsymbol{x})$ 是 $A^k$ 的特征对；更一般地，对任意多项式 $f$，$(f(\lambda_0), \boldsymbol{x})$ 是 $f(A)$ 的特征对，例如 $(1 + \lambda_0, \boldsymbol{x})$ 是 $I_n + A$ 的特征对；
2. 若 $A$ 可逆，则 $\lambda_0 \ne 0$，且 $(\lambda_0^{-1}, \boldsymbol{x})$ 是 $A^{-1}$ 的特征对；
3. 若多项式 $f$ 满足 $f(A) = O$，则 $A$ 的每个特征值都是 $f$ 的根（这样的 $f$ 称为 $A$ 的化零多项式，见[第 10 章](/2.1.10)）。

**证明** 1. $A^k\boldsymbol{x} = A^{k-1}(\lambda_0\boldsymbol{x}) = \cdots = \lambda_0^k\boldsymbol{x}$，再由线性组合得 $f(A)\boldsymbol{x} = f(\lambda_0)\boldsymbol{x}$。2. 对 $A\boldsymbol{x} = \lambda_0\boldsymbol{x}$ 两边左乘 $\lambda_0^{-1}A^{-1}$。3. 由 1，$\boldsymbol{0} = f(A)\boldsymbol{x} = f(\lambda_0)\boldsymbol{x}$，而 $\boldsymbol{x} \ne \boldsymbol{0}$，故 $f(\lambda_0) = 0$。$\square$

例如幂零矩阵（nilpotent matrix），即存在正整数 $k$ 使 $A^k = O$ 的方阵，它的特征值全为 $0$；幂等矩阵（$A^2 = A$）的特征值只能是 $0$ 或 $1$。

**例 6.4.1（秩一矩阵的特征值）** 设 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$ 非零，$n \ge 2$，求 $A = \boldsymbol{a}\boldsymbol{b}^{\mathsf T}$ 的特征值。

$A\boldsymbol{x} = (\boldsymbol{b}^{\mathsf T}\boldsymbol{x})\boldsymbol{a}$。于是 $\mathcal{N}(A) = \operatorname{span}(\boldsymbol{b})^\perp$ 是 $n-1$ 维的，$0$ 是特征值，特征子空间为 $\operatorname{span}(\boldsymbol{b})^\perp$；又 $A\boldsymbol{a} = (\boldsymbol{b}^{\mathsf T}\boldsymbol{a})\boldsymbol{a}$。由推论 6.4.1，特征值之和为 $\operatorname{tr}(\boldsymbol{a}\boldsymbol{b}^{\mathsf T}) = \boldsymbol{b}^{\mathsf T}\boldsymbol{a}$，而 $0$ 至少占了 $n-1$ 个（几何重数不超过代数重数，见 6.6 节的定理 6.6.1），所以 $p_A(\lambda) = \lambda^{n-1}(\lambda - \boldsymbol{b}^{\mathsf T}\boldsymbol{a})$。分两种情形：

- $\boldsymbol{b}^{\mathsf T}\boldsymbol{a} \ne 0$：特征值为 $\boldsymbol{b}^{\mathsf T}\boldsymbol{a}$（特征子空间 $\operatorname{span}(\boldsymbol{a})$）与 $n-1$ 重的 $0$（特征子空间 $\operatorname{span}(\boldsymbol{b})^\perp$）；
- $\boldsymbol{b}^{\mathsf T}\boldsymbol{a} = 0$：只有特征值 $0$，代数重数为 $n$，而特征子空间 $\operatorname{span}(\boldsymbol{b})^\perp$ 只有 $n-1$ 维（此时 $\boldsymbol{a}$ 也在其中，$A^2 = O$）。

### 6.4.4. 友矩阵

**定义 6.4.2（友矩阵）** 对首一多项式 $p(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \cdots + c_1\lambda + c_0$，矩阵

$$
C_p = \begin{bmatrix} 0 & 1 & & & \\ & 0 & 1 & & \\ & & \ddots & \ddots & \\ & & & 0 & 1 \\ -c_0 & -c_1 & \cdots & -c_{n-2} & -c_{n-1} \end{bmatrix}
$$

称为 $p$ 的**友矩阵**。

**命题 6.4.2** $C_p$ 的特征多项式就是 $p(\lambda)$；若 $\lambda_0$ 是 $C_p$ 的特征值，则 $\boldsymbol{y} = [1\ \lambda_0\ \lambda_0^2\ \cdots\ \lambda_0^{n-1}]^{\mathsf T}$ 是属于 $\lambda_0$ 的特征向量。

**证明** 对 $\det(\lambda I_n - C_p)$ 按第 $n$ 行展开，第 $n$ 行为 $[c_0\ \cdots\ c_{n-2}\ \ \lambda + c_{n-1}]$，各代数余子式对应的子矩阵都是三角矩阵，计算可得 $p(\lambda)$。对 $\boldsymbol{y}$，$C_p\boldsymbol{y}$ 的前 $n-1$ 个分量为 $\lambda_0, \dots, \lambda_0^{n-1}$，即 $\lambda_0 y_1, \dots, \lambda_0 y_{n-1}$；最后一个分量为 $-\sum_{k=0}^{n-1}c_k\lambda_0^k = \lambda_0^n = \lambda_0y_n$（因为 $p(\lambda_0) = 0$）。$\square$

由 Abel–Ruffini 定理，五次及以上的多项式没有一般的求根公式，即不能用有限次加、减、乘、除、开方表示根。因此特征值一般只能数值计算；反过来，任意多项式的根都可以通过计算其友矩阵的特征值得到，`numpy.roots` 正是这样做的。

## 6.5. 对角化

### 6.5.1. 可对角化与特征值分解

**定义 6.5.1（可对角化）** 对 $n$ 阶方阵 $A$，若存在可逆矩阵 $X$ 使 $X^{-1}AX = \Lambda$ 是对角矩阵，则称 $A$（在 $\mathbb{C}$ 上）**可对角化**，称 $X$ 把 $A$ 对角化。若 $A, X, \Lambda$ 都是实矩阵，则称 $A$ 在 $\mathbb{R}$ 上可对角化。$A$ 可对角化时，分解 $A = X\Lambda X^{-1}$ 称为 $A$ 的**特征值分解**。

有的教材把一般可对角化矩阵的 $A = X\Lambda X^{-1}$ 也称为谱分解（特征值的全体也称为谱）。本站的**谱分解**专指实对称矩阵（或正规矩阵）的正交（酉）对角化 $A = Q\Lambda Q^{\mathsf T}$，见[第 7 章](/2.1.7)；一般情形称特征值分解，以示区别。

特征值分解把矩阵的幂化为对角矩阵的幂：若 $A = X\Lambda X^{-1}$，则 $A^t = X\Lambda^tX^{-1}$；$A$ 可逆时 $A^{-1} = X\Lambda^{-1}X^{-1}$。对任意 $\boldsymbol{x} \in \mathbb{C}^n$，写 $\boldsymbol{x} = X\boldsymbol{k}$（即 $\boldsymbol{x}$ 在 $X$ 的列向量这组基下的坐标为 $\boldsymbol{k}$），则 $A^t\boldsymbol{x} = X\Lambda^t\boldsymbol{k}$：在特征向量组成的基下，$A$ 的作用就是各坐标分别乘以对应的特征值。

**定理 6.5.1** $n$ 阶方阵 $A$ 可对角化，当且仅当 $A$ 有 $n$ 个线性无关的特征向量。此时 $\Lambda$ 的对角元就是 $A$ 的特征值，$X$ 的列就是对应的 $n$ 个线性无关的特征向量。

**证明** 充分性：若 $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$（$i = 1, \dots, n$），$\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ 线性无关，令 $X = [\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_n]$，$\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$，则 $X$ 可逆，$AX = X\Lambda$。必要性：若 $X^{-1}AX = \Lambda$，则 $A[\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_n] = [\lambda_1\boldsymbol{x}_1\ \cdots\ \lambda_n\boldsymbol{x}_n]$，即 $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$，而 $X$ 可逆说明 $\boldsymbol{x}_i$ 线性无关且非零。$\square$

### 6.5.2. 属于不同特征值的特征向量

**定理 6.5.2** 方阵的属于不同特征值的特征向量线性无关。

**证明** 设 $A\boldsymbol{x}_i = \lambda_i\boldsymbol{x}_i$，$\boldsymbol{x}_i \ne \boldsymbol{0}$（$i = 1, \dots, r$），$\lambda_1, \dots, \lambda_r$ 两两不同，且 $k_1\boldsymbol{x}_1 + \cdots + k_r\boldsymbol{x}_r = \boldsymbol{0}$。两边左乘 $A^i$（$i = 1, \dots, r-1$）得 $k_1\lambda_1^i\boldsymbol{x}_1 + \cdots + k_r\lambda_r^i\boldsymbol{x}_r = \boldsymbol{0}$。把这 $r$ 个等式写成矩阵形式：

$$
[k_1\boldsymbol{x}_1\ k_2\boldsymbol{x}_2\ \cdots\ k_r\boldsymbol{x}_r]\begin{bmatrix} 1 & \lambda_1 & \cdots & \lambda_1^{r-1} \\ 1 & \lambda_2 & \cdots & \lambda_2^{r-1} \\ \vdots & \vdots & & \vdots \\ 1 & \lambda_r & \cdots & \lambda_r^{r-1} \end{bmatrix} = O.
$$

右边的因子是 **Vandermonde 矩阵**，由定理 5.4.1 可逆，故 $k_i\boldsymbol{x}_i = \boldsymbol{0}$，从而 $k_i = 0$。$\square$

**推论 6.5.1** 有 $n$ 个不同特征值的 $n$ 阶方阵可对角化。

这不是必要条件：$I_n$ 只有一个 $n$ 重特征值 $1$，但它本身就是对角矩阵。

## 6.6. 几何重数与可对角化的条件

### 6.6.1. 几何重数

**定义 6.6.1（几何重数）** 设 $\lambda_0$ 是 $n$ 阶方阵 $A$ 的特征值，特征子空间 $\mathcal{N}(\lambda_0I_n - A)$ 的维数 $n - \operatorname{rank}(\lambda_0I_n - A)$ 称为 $\lambda_0$ 的**几何重数**。

几何重数就是属于 $\lambda_0$ 的线性无关特征向量的最大个数，至少为 $1$。

**定理 6.6.1** 方阵的特征值的几何重数不大于其代数重数。

**证明** 设 $\lambda_0$ 的几何重数为 $r$，$\boldsymbol{x}_1, \dots, \boldsymbol{x}_r$ 是 $\mathcal{N}(\lambda_0I_n - A)$ 的一组基。把它扩充为 $\mathbb{C}^n$ 的基 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_r, \boldsymbol{y}_{r+1}, \dots, \boldsymbol{y}_n$，记 $X_0 = [\boldsymbol{x}_1\ \cdots\ \boldsymbol{x}_r]$，$Y = [\boldsymbol{y}_{r+1}\ \cdots\ \boldsymbol{y}_n]$，$X = [X_0\ Y]$ 可逆。由 $AX_0 = \lambda_0X_0$，

$$
AX = [X_0\ Y]\begin{bmatrix} \lambda_0I_r & M_{12} \\ O & M_{22} \end{bmatrix} = XM.
$$

$A$ 与 $M = X^{-1}AX$ 的特征多项式相同：$\det(\lambda I_n - M) = \det(X^{-1}(\lambda I_n - A)X) = \det(\lambda I_n - A)$。而 $M$ 是分块上三角矩阵，$\det(\lambda I_n - M) = (\lambda - \lambda_0)^r\det(\lambda I_{n-r} - M_{22})$，所以 $\lambda_0$ 的代数重数至少是 $r$。$\square$

**定义 6.6.2（半单特征值与亏损特征值）** 几何重数等于代数重数的特征值称为**半单特征值**；几何重数小于代数重数的特征值称为**亏损特征值**。

单特征值的两种重数都是 $1$，所以一定半单。

### 6.6.2. 可对角化的等价条件

**定理 6.6.2**

1. $n$ 阶方阵 $A$ 可对角化，当且仅当它的特征值都半单；
2. $n$ 阶实方阵 $A$ 在 $\mathbb{R}$ 上可对角化，当且仅当它的特征值都是实数并且都半单。

**证明** 1. 设 $A$ 的全部不同特征值为 $\lambda_1, \dots, \lambda_s$，几何重数为 $m_1, \dots, m_s$，代数重数为 $n_1, \dots, n_s$，$\sum_i n_i = n$。

必要性：若 $A$ 可对角化，它有 $n$ 个线性无关的特征向量，其中属于 $\lambda_i$ 的有 $k_i$ 个，都在 $\mathcal{N}(\lambda_iI_n - A)$ 中，故 $k_i \le m_i \le n_i$；又 $\sum k_i = n = \sum n_i$，所以 $k_i = m_i = n_i$。

充分性：若 $m_i = n_i$，在每个特征子空间中取一组基，共 $\sum m_i = n$ 个特征向量。它们线性无关：若某个线性组合为零，把属于同一特征值的项合并成 $\boldsymbol{u}_i \in \mathcal{N}(\lambda_iI_n - A)$，则 $\sum\boldsymbol{u}_i = \boldsymbol{0}$；由定理 6.5.2，非零的 $\boldsymbol{u}_i$ 不能线性相关，故每个 $\boldsymbol{u}_i = \boldsymbol{0}$，再由每组基线性无关知系数全为零。由定理 6.5.1，$A$ 可对角化。

2. 若 $A = X\Lambda X^{-1}$ 且 $X, \Lambda$ 是实矩阵，则特征值（$\Lambda$ 的对角元）都是实数，并由 1 都半单。反之，若特征值都是实数，$\lambda_iI_n - A$ 是实矩阵，它在 $\mathbb{R}$ 上与在 $\mathbb{C}$ 上的秩相同（消元过程只用到实数运算），所以可以在每个特征子空间中取实向量组成的基，按 1 的充分性得到实的 $X$。$\square$

**命题 6.6.1（分块对角矩阵的对角化）** **分块对角矩阵** $A = \operatorname{diag}(A_1, \dots, A_r)$（对角块 $A_i$ 都是方阵）可对角化，当且仅当每个 $A_i$ 都可对角化。

**证明** 只需证 $r = 2$。充分性：若 $X_i^{-1}A_iX_i = D_i$ 是对角矩阵，令 $X = \operatorname{diag}(X_1, X_2)$，则 $X^{-1}AX = \operatorname{diag}(D_1, D_2)$。必要性：$p_A(\lambda) = p_{A_1}(\lambda)p_{A_2}(\lambda)$。对 $A$ 的任意特征值 $\lambda_0$，设它作为 $A_1, A_2$ 的特征值的代数重数为 $n_{01}, n_{02}$（不是特征值时记为 $0$），几何重数为 $m_{01}, m_{02}$，则 $\lambda_0$ 作为 $A$ 的特征值的代数重数为 $n_{01} + n_{02}$；由 $\operatorname{rank}(\lambda_0I - A) = \operatorname{rank}(\lambda_0I - A_1) + \operatorname{rank}(\lambda_0I - A_2)$，其几何重数为 $m_{01} + m_{02}$。$A$ 可对角化，故 $m_{01} + m_{02} = n_{01} + n_{02}$；又 $m_{01} \le n_{01}$，$m_{02} \le n_{02}$，所以 $m_{01} = n_{01}$，$m_{02} = n_{02}$，$A_1, A_2$ 的特征值都半单。$\square$

**例 6.6.1**

1. $I_n$ 只有特征值 $1$，代数重数与几何重数都是 $n$，$1$ 是半单特征值。
2. 倍加矩阵 $E_{21;k} = \begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$（$k \ne 0$）只有特征值 $1$，代数重数为 $2$，几何重数为 $1$，$1$ 是亏损特征值，$E_{21;k}$ 不可对角化。几何上，错切只有一个不变方向。

**定义 6.6.3（Jordan 块）** $n$ 阶方阵

$$
J_n(\lambda) = \begin{bmatrix} \lambda & 1 & & \\ & \lambda & \ddots & \\ & & \ddots & 1 \\ & & & \lambda \end{bmatrix}
$$

称为关于 $\lambda$ 的 $n$ 阶 **Jordan 块**。

$J_n(\lambda)$ 只有特征值 $\lambda$，代数重数为 $n$；$\lambda I_n - J_n(\lambda)$ 的秩为 $n-1$，几何重数为 $1$。$n > 1$ 时 $\lambda$ 是亏损特征值，$J_n(\lambda)$ 不可对角化。6.10 节将说明，Jordan 块是不可对角化矩阵的"基本零件"。

**性质 6.6.1**

1. 幂等矩阵（$A^2 = A$）可对角化，且相似于 $\operatorname{diag}(I_r, O)$，$r = \operatorname{rank}(A)$；
2. 设 $\boldsymbol{v}$ 是单位向量，则存在正交矩阵 $Q$ 使 $Q^{-1}H_{\boldsymbol{v}}Q = \operatorname{diag}(-1, 1, \dots, 1)$，其中 $H_{\boldsymbol{v}} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$ 是 **Householder 变换**。

**证明** 1. 对任意 $\boldsymbol{x}$，$\boldsymbol{x} = A\boldsymbol{x} + (\boldsymbol{x} - A\boldsymbol{x})$，其中 $A(A\boldsymbol{x}) = A\boldsymbol{x}$，$A(\boldsymbol{x} - A\boldsymbol{x}) = \boldsymbol{0}$。所以 $\mathcal{R}(A)$ 中的非零向量都是属于 $1$ 的特征向量，$\mathcal{N}(A)$ 是属于 $0$ 的特征子空间，二者维数之和为 $\operatorname{rank}(A) + (n - \operatorname{rank}(A)) = n$。取 $\mathcal{R}(A)$ 与 $\mathcal{N}(A)$ 的基合起来，由定理 6.5.2 的论证它们线性无关，就是 $n$ 个线性无关的特征向量。2. $H_{\boldsymbol{v}}\boldsymbol{v} = -\boldsymbol{v}$，而对 $\boldsymbol{w} \perp \boldsymbol{v}$ 有 $H_{\boldsymbol{v}}\boldsymbol{w} = \boldsymbol{w}$。取 $Q$ 的第一列为 $\boldsymbol{v}$，其余列为 $\operatorname{span}(\boldsymbol{v})^\perp$ 的标准正交基即可。$\square$

### 6.6.3. 对角化的计算

**算法 6.6.1（对角化）** 输入 $n$ 阶方阵 $A$。

1. 用算法 6.3.1 求出全部不同的特征值 $\lambda_1, \dots, \lambda_s$ 及其代数重数 $n_1, \dots, n_s$；
2. 对每个 $\lambda_i$ 求 $\mathcal{N}(\lambda_iI_n - A)$ 的一组基，其个数就是几何重数 $m_i$；
3. 若有某个 $m_i < n_i$，则 $A$ 不可对角化，停止；
4. 否则把所有基向量排成 $X$，相应的特征值（各重复 $m_i$ 次）排成 $\Lambda$，得 $A = X\Lambda X^{-1}$。

## 6.7. 应用：矩阵的幂与线性递推

**例 6.7.1** 求 $A = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 2 & 0 \\ -1 & -1 & 3 \end{bmatrix}$ 的特征值分解与 $A^n$。

$A$ 是下三角矩阵，特征值为 $1, 2, 3$，互不相同，所以可对角化。对应的特征向量为 $\boldsymbol{x}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$，$\boldsymbol{x}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$，$\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$。令

$$
X = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}, \quad \Lambda = \begin{bmatrix} 1 & & \\ & 2 & \\ & & 3 \end{bmatrix}, \quad X^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix},
$$

则 $A = X\Lambda X^{-1}$，

$$
A^n = X\Lambda^nX^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 1 - 2^n & 2^n & 0 \\ 1 - 2^n & 2^n - 3^n & 3^n \end{bmatrix}.
$$

**例 6.7.2（Fibonacci 数列）** 设 $F_0 = 0$，$F_1 = 1$，$F_{n+1} = F_n + F_{n-1}$（$n \ge 1$），求 $F_n$ 的通项公式。

令 $\boldsymbol{u}_n = \begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix}$，递推关系写成

$$
\boldsymbol{u}_{n+1} = \begin{bmatrix} F_{n+1} \\ F_n \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} F_n \\ F_{n-1} \end{bmatrix} = A\boldsymbol{u}_n,
$$

于是 $\boldsymbol{u}_n = A^{n-1}\boldsymbol{u}_1$，$\boldsymbol{u}_1 = \boldsymbol{e}_1$。$p_A(\lambda) = \lambda^2 - \lambda - 1$，特征值 $\lambda_1 = \frac{1 + \sqrt{5}}{2}$，$\lambda_2 = \frac{1 - \sqrt{5}}{2}$，特征向量 $\boldsymbol{x}_i = \begin{bmatrix} \lambda_i \\ 1 \end{bmatrix}$（因为 $\lambda_i^2 = \lambda_i + 1$）。$X = [\boldsymbol{x}_1\ \boldsymbol{x}_2]$，$X^{-1} = \dfrac{1}{\lambda_1 - \lambda_2}\begin{bmatrix} 1 & -\lambda_2 \\ -1 & \lambda_1 \end{bmatrix}$，

$$
F_n = \boldsymbol{e}_1^{\mathsf T}\boldsymbol{u}_n = \boldsymbol{e}_1^{\mathsf T}X\Lambda^{n-1}X^{-1}\boldsymbol{e}_1 = \frac{1}{\lambda_1 - \lambda_2}[\lambda_1\ \ \lambda_2]\begin{bmatrix} \lambda_1^{n-1} & \\ & \lambda_2^{n-1} \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \frac{\lambda_1^n - \lambda_2^n}{\lambda_1 - \lambda_2} = \frac{1}{\sqrt{5}}\left[\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n\right].
$$

由于 $|\lambda_2| < 1$，$F_n$ 就是 $\lambda_1^n/\sqrt{5}$ 四舍五入后的整数，$F_{n+1}/F_n \to \lambda_1$（黄金比）。

一般地，若 $A$ 可对角化，$A^t\boldsymbol{x} = \sum_i k_i\lambda_i^t\boldsymbol{x}_i$，$t$ 很大时由绝对值最大的特征值主导：若所有特征值的绝对值都小于 $1$，则 $A^t\boldsymbol{x} \to \boldsymbol{0}$；若最大者大于 $1$，则一般 $\|A^t\boldsymbol{x}\| \to \infty$。例 6.1.1 中特征值 $1$ 决定了极限分布，$0.5$ 决定了收敛的速度。下面的代码验证这两个例子：

```python
import numpy as np

# Example 6.1.1: A^t tends to the rank-one matrix [x1 x1] with x1 = (0.2, 0.8)
A = np.array([[0.6, 0.1], [0.4, 0.9]])
print(np.linalg.eigvals(A))              # eigenvalues 0.5 and 1
print(np.linalg.matrix_power(A, 50))     # close to [[0.2, 0.2], [0.8, 0.8]]

# Example 6.7.2: Binet's formula from the eigendecomposition of [[1, 1], [1, 0]]
phi, psi = (1 + 5**0.5) / 2, (1 - 5**0.5) / 2
print([round((phi**n - psi**n) / 5**0.5) for n in range(1, 11)])
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

下图画出例 6.1.1 中不同初始分布的迭代 $A^t\boldsymbol{x}$。每一步属于特征值 $0.5$ 的分量减半，所以迭代点沿 $\boldsymbol{x}_2 = (1, -1)$ 方向（总人口不变）移向特征直线 $\operatorname{span}(\boldsymbol{x}_1)$；与极限的距离按 $0.5^t$ 衰减。

![例 6.1.1 的人口迁移：左图中各初始分布的迭代点沿 x2 方向收敛到特征直线 span(x1)；右图中与极限的距离按第二个特征值的幂 0.5^t 衰减](./plots/migration-iteration.py)

## 6.8. 相似

### 6.8.1. 相似关系

**定义 6.8.1（相似）** 对 $n$ 阶方阵 $A, B$，若存在可逆矩阵 $X$ 使 $X^{-1}AX = B$，则称 $A$ 与 $B$ **相似**，或 $A$ 相似于 $B$。

**例 6.8.1**

1. 数量矩阵 $kI_n$ 只与自己相似：$X^{-1}(kI_n)X = kI_n$。
2. $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ 与 $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ 相似：$\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}^{-1}\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$。
3. 对角元只差一个排列的两个对角矩阵相似：$\Lambda_1 = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$，$\Lambda_2 = \operatorname{diag}(\lambda_{\sigma_1}, \dots, \lambda_{\sigma_n})$，取**置换矩阵** $P = [\boldsymbol{e}_{\sigma_1}\ \cdots\ \boldsymbol{e}_{\sigma_n}]$，则 $P^{-1}\Lambda_1P = \Lambda_2$。

**命题 6.8.1** 方阵的相似关系是**等价关系**。

**证明** 自反性：$A = I_n^{-1}AI_n$。对称性：由 $X^{-1}AX = B$ 得 $(X^{-1})^{-1}BX^{-1} = A$。传递性：由 $X^{-1}AX = B$，$Y^{-1}BY = C$ 得 $(XY)^{-1}A(XY) = C$。$\square$

对应的变换 $A \mapsto X^{-1}AX$ 称为相似变换。$A$ 可对角化等价于 $A$ 与对角矩阵相似；若 $A, B$ 相似，则 $A$ 可对角化当且仅当 $B$ 可对角化。若 $X^{-1}AX = B$，则 $A\boldsymbol{x} = \boldsymbol{b}$ 等价于 $B(X^{-1}\boldsymbol{x}) = X^{-1}\boldsymbol{b}$：相似的矩阵是同一个线性变换在两组不同基下的表示矩阵，$X$ 的列就是新基（详见[第 8 章](/2.1.8)）。

### 6.8.2. 相似不变量

**定理 6.8.1** 相似的方阵具有相同的：

1. 秩；
2. 特征多项式，从而特征值、特征值的代数重数、迹与行列式；
3. 特征值的几何重数。

并且若 $(\lambda, \boldsymbol{u})$ 是 $A$ 的特征对，则 $(\lambda, X^{-1}\boldsymbol{u})$ 是 $X^{-1}AX$ 的特征对。

**证明** 1. 左乘、右乘可逆矩阵不改变秩。2. $\det(\lambda I_n - X^{-1}AX) = \det(X^{-1}(\lambda I_n - A)X) = \det(\lambda I_n - A)$；迹与行列式由特征值确定（推论 6.4.1）。3. $\operatorname{rank}(\lambda I_n - X^{-1}AX) = \operatorname{rank}(X^{-1}(\lambda I_n - A)X) = \operatorname{rank}(\lambda I_n - A)$，故特征子空间维数相同。最后，$X^{-1}AX(X^{-1}\boldsymbol{u}) = X^{-1}A\boldsymbol{u} = \lambda X^{-1}\boldsymbol{u}$。$\square$

这些不变量不足以判定相似：$I_2$ 与 $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 的秩、特征多项式、迹、行列式都相同，但 $I_2$ 只与自己相似。加上每个特征值的几何重数仍然不够（阶数不小于 $4$ 时），完全的不变量是 6.10 节的 Jordan 标准形。

**推论 6.8.1** 两个对角矩阵相似，当且仅当它们的对角元除排列次序外相同。

**证明** 充分性见例 6.8.1 的 3。必要性：相似矩阵的特征值（计重数）相同，而对角矩阵的特征值就是对角元。$\square$

$A$ 可对角化时，与它相似的对角矩阵称为 $A$ 的相似标准形，它在不计对角元次序的意义下唯一。

## 6.9. 上三角化与 Cayley–Hamilton 定理

并非所有方阵都能对角化，但所有方阵都能通过相似变换化为上三角矩阵。

**定理 6.9.1** 对 $n$ 阶方阵 $A$，存在可逆矩阵 $X$ 使 $X^{-1}AX = T$ 是上三角矩阵，且 $T$ 的对角元是 $A$ 的 $n$ 个特征值（计重数）。进一步，适当选取 $X$ 可以使 $T$ 的对角元按任意指定的次序排列。

**证明** 对 $n$ 用数学归纳法，$n = 1$ 时显然。设结论对 $n-1$ 阶方阵成立。任取 $A$ 的一个特征对 $(\lambda_1, \boldsymbol{x}_1)$，把 $\boldsymbol{x}_1$ 扩充为 $\mathbb{C}^n$ 的基 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$，令 $X_1 = [\boldsymbol{x}_1\ X_{12}]$，则

$$
AX_1 = [\lambda_1\boldsymbol{x}_1\ \ AX_{12}] = [\boldsymbol{x}_1\ X_{12}]\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & A_1 \end{bmatrix},
$$

$A_1$ 是 $n-1$ 阶方阵。由归纳假设，存在可逆矩阵 $X_2$ 使 $X_2^{-1}A_1X_2 = T_2$ 是上三角矩阵，于是

$$
A = X_1\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & X_2T_2X_2^{-1} \end{bmatrix}X_1^{-1} = X_1\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & X_2 \end{bmatrix}\begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & T_2 \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & X_2 \end{bmatrix}^{-1}X_1^{-1}.
$$

记 $X = X_1\operatorname{diag}(1, X_2)$，$T = \begin{bmatrix} \lambda_1 & * \\ \boldsymbol{0} & T_2 \end{bmatrix}$，则 $X$ 可逆，$T$ 是上三角矩阵，$A = XTX^{-1}$。$T$ 与 $A$ 相似，特征值相同，而三角矩阵的特征值就是对角元。由于每一步可以任选一个特征值，对角元的次序可以任意指定。$\square$

这个证明本身就是一个逐步降维的算法：取一个特征向量，扩充成基，对右下角的 $n-1$ 阶块重复。[第 10 章](/2.1.10)以 **Schur 定理**的名义把它写成构造性算法，[第 12 章](/2.1.12)把 $X$ 加强为酉矩阵。

**定理 6.9.2（Cayley–Hamilton 定理）** 设方阵 $A$ 的特征多项式为 $p_A(\lambda)$，则 $p_A(A) = O$。

按另一种习惯也称之为 Hamilton–Cayley 定理。

**证明** 由定理 6.9.1，$A = XTX^{-1}$，$T$ 是上三角矩阵，于是 $p_A(A) = Xp_A(T)X^{-1}$，只需证 $p_A(T) = O$。设 $T$ 的对角元依次为 $\lambda_1, \dots, \lambda_n$，则 $p_A(\lambda) = (\lambda - \lambda_1)\cdots(\lambda - \lambda_n)$，

$$
p_A(T) = (T - \lambda_1I_n)(T - \lambda_2I_n)\cdots(T - \lambda_nI_n),
$$

其中 $T - \lambda_iI_n$ 是上三角矩阵，第 $i$ 个对角元为零。令 $T_i = (T - \lambda_1I_n)\cdots(T - \lambda_iI_n)$，用归纳法证明 $T_i$ 的前 $i$ 列为零。$T_1 = T - \lambda_1I_n$ 的第一列为零。设 $T_i$ 的前 $i$ 列为零，写 $T_i = [O_{n \times i}\ P]$，把 $T - \lambda_{i+1}I_n$ 按行分块为 $\begin{bmatrix} * \\ Q \end{bmatrix}$，$Q$ 是后 $n - i$ 行；由于 $T - \lambda_{i+1}I_n$ 上三角且第 $i+1$ 个对角元为零，$Q$ 的前 $i + 1$ 列为零。于是 $T_{i+1} = [O\ P]\begin{bmatrix} * \\ Q \end{bmatrix} = PQ$ 的前 $i+1$ 列为零。所以 $p_A(T) = T_n = O$。$\square$

**例 6.9.1** 设 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$，$p_A(\lambda) = \lambda^2 - 5\lambda - 2$，于是 $A^2 - 5A - 2I_2 = O$，即 $A^2 = 5A + 2I_2$，

$$
A^3 = 5A^2 + 2A = 27A + 10I_2.
$$

$\det A = -2 \ne 0$，$A$ 可逆。由 $A(A - 5I_2) = 2I_2$ 得

$$
A^{-1} = \frac{1}{2}(A - 5I_2), \qquad A^{-2} = \frac{1}{4}(A - 5I_2)^2 = \frac{1}{4}(-5A + 27I_2).
$$

类似地，$A$ 的任意次幂（包括负整数次幂）都可以写成 $A$ 与 $I_2$ 的线性组合。一般地，对 $n$ 阶方阵与多项式 $f$，用 $p_A$ 对 $f$ 做带余除法 $f = qp_A + r$（$\deg r < n$），则 $f(A) = r(A)$：任意多项式在 $A$ 上的值都可以化为次数小于 $n$ 的多项式，这是[第 11 章](/2.1.11)计算矩阵函数的出发点。

## 6.10. Jordan 标准形

**定理 6.10.1（Jordan 分解）** 对 $n$ 阶方阵 $A$，存在可逆矩阵 $X$ 使

$$
X^{-1}AX = J = \begin{bmatrix} J_{n_1}(\lambda_1) & & & \\ & J_{n_2}(\lambda_2) & & \\ & & \ddots & \\ & & & J_{n_r}(\lambda_r) \end{bmatrix},
$$

其中 $J_{n_i}(\lambda_i)$ 是 $n_i$ 阶 Jordan 块，$n_1 + \cdots + n_r = n$，$\lambda_1, \dots, \lambda_r$ 中可以有相同的数。除 Jordan 块的排列次序外，$J$ 由 $A$ 唯一确定。当 $A$ 是实方阵且特征值全为实数时，$X$ 可以取为实方阵。分解 $A = XJX^{-1}$ 称为 $A$ 的 Jordan 分解，$J$ 称为 $A$ 的 **Jordan 标准形**。

本章只陈述这一定理，证明与计算见[第 10 章](/2.1.10)。几点说明：

- 每个 Jordan 块恰好贡献一个线性无关的特征向量，所以 $A$ 有 $r$ 个线性无关的特征向量；属于 $\lambda$ 的 Jordan 块个数等于 $\lambda$ 的几何重数，这些块的阶数之和等于代数重数。
- $A$ 可对角化当且仅当所有 $n_i = 1$，此时 $J = \Lambda$，$r = n$。
- 两个方阵相似当且仅当它们有相同的 Jordan 标准形（不计块的次序）。
- Jordan 标准形对矩阵元素的微小扰动极不稳定（例如 $J_n(0)$ 的任意小扰动都可能变成可对角化矩阵），所以它是理论工具，数值计算中通常用正交（酉）相似的上三角化（[第 12 章](/2.1.12)）或奇异值分解（[第 7 章](/2.1.7)）代替。

**例 6.10.1** 设 $A = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 1 & 1 \\ -1 & 0 & 2 \end{bmatrix}$。$p_A(\lambda) = (\lambda - 1)^3$，$A$ 只有特征值 $\lambda = 1$，代数重数为 $3$。

$$
\lambda I_3 - A = \begin{bmatrix} 1 & -1 & 0 \\ 1 & 0 & -1 \\ 1 & 0 & -1 \end{bmatrix}
$$

的秩为 $2$，几何重数为 $1$，$\lambda$ 是亏损特征值，$A$ 不可对角化，其 Jordan 标准形只能由一个 $3$ 阶 Jordan 块组成。为求 $X$，取非零向量 $\boldsymbol{x}_3$ 使 $(A - \lambda I_3)^2\boldsymbol{x}_3 \ne \boldsymbol{0}$，再令 $\boldsymbol{x}_2 = (A - \lambda I_3)\boldsymbol{x}_3$，$\boldsymbol{x}_1 = (A - \lambda I_3)\boldsymbol{x}_2$。这样的 $\boldsymbol{x}_3$ 一定存在：由 Cayley–Hamilton 定理 $(A - \lambda I_3)^3 = O$，而 $\dim\mathcal{N}((A - \lambda I_3)^2) \le 2\dim\mathcal{N}(A - \lambda I_3) = 2 < 3$（一般地 $\dim\mathcal{N}(BC) \le \dim\mathcal{N}(B) + \dim\mathcal{N}(C)$）。取

$$
\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, \quad \boldsymbol{x}_2 = (A - \lambda I_3)\boldsymbol{x}_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}, \quad \boldsymbol{x}_1 = (A - \lambda I_3)\boldsymbol{x}_2 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad (A - \lambda I_3)\boldsymbol{x}_1 = \boldsymbol{0},
$$

即 $A\boldsymbol{x}_1 = \lambda\boldsymbol{x}_1$，$A\boldsymbol{x}_2 = \boldsymbol{x}_1 + \lambda\boldsymbol{x}_2$，$A\boldsymbol{x}_3 = \boldsymbol{x}_2 + \lambda\boldsymbol{x}_3$；$\boldsymbol{x}_1$ 就是特征向量。$\boldsymbol{x}_1, \boldsymbol{x}_2, \boldsymbol{x}_3$ 线性无关（若 $k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2 + k_3\boldsymbol{x}_3 = \boldsymbol{0}$，依次左乘 $(A - \lambda I_3)^2$、$A - \lambda I_3$ 得 $k_3 = 0$、$k_2 = 0$，进而 $k_1 = 0$）。令 $X = [\boldsymbol{x}_1\ \boldsymbol{x}_2\ \boldsymbol{x}_3]$，则

$$
AX = X\begin{bmatrix} \lambda & 1 & \\ & \lambda & 1 \\ & & \lambda \end{bmatrix} = XJ_3(\lambda), \qquad X^{-1}AX = J_3(1).
$$

## 6.11. 同时对角化

**定义 6.11.1（同时对角化）** 设 $A, B$ 是 $n$ 阶方阵。若存在可逆矩阵 $X$ 使 $X^{-1}AX = \Lambda_1$ 与 $X^{-1}BX = \Lambda_2$ 都是对角矩阵，则称 $A, B$ 可以**同时对角化**。

$A, B$ 可以同时对角化，等价于存在 $n$ 个线性无关的向量同时是 $A$ 与 $B$ 的特征向量（对应的特征值可以不同）。

**定理 6.11.1** 设 $n$ 阶方阵 $A, B$ 都可对角化，则 $A, B$ 可以同时对角化，当且仅当 $AB = BA$。

**证明** 必要性：若 $X^{-1}AX = \Lambda_1$，$X^{-1}BX = \Lambda_2$，对角矩阵可交换，故

$$
AB = X\Lambda_1X^{-1}X\Lambda_2X^{-1} = X\Lambda_1\Lambda_2X^{-1} = X\Lambda_2\Lambda_1X^{-1} = BA.
$$

充分性：$A$ 可对角化，把相同的特征值排在一起，存在可逆矩阵 $X_1$ 使 $X_1^{-1}AX_1 = \Lambda_1 = \operatorname{diag}(\lambda_1I_{n_1}, \dots, \lambda_rI_{n_r})$，$\lambda_1, \dots, \lambda_r$ 两两不同。令 $\tilde{B} = X_1^{-1}BX_1$，由 $AB = BA$ 得 $\Lambda_1\tilde{B} = \tilde{B}\Lambda_1$。把 $\tilde{B}$ 按同样方式分块为 $[\tilde{B}_{ij}]$，比较两边的 $(i, j)$ 块得 $\lambda_i\tilde{B}_{ij} = \lambda_j\tilde{B}_{ij}$，$i \ne j$ 时 $\tilde{B}_{ij} = O$，即 $\tilde{B} = \operatorname{diag}(\tilde{B}_{11}, \dots, \tilde{B}_{rr})$。$B$ 可对角化，故与之相似的 $\tilde{B}$ 可对角化，由命题 6.6.1 每个 $\tilde{B}_{ii}$ 都可对角化：$X_{ii}^{-1}\tilde{B}_{ii}X_{ii} = \Lambda_{ii}$。令 $X_2 = \operatorname{diag}(X_{11}, \dots, X_{rr})$，则

$$
(X_1X_2)^{-1}B(X_1X_2) = X_2^{-1}\tilde{B}X_2 = \operatorname{diag}(\Lambda_{11}, \dots, \Lambda_{rr}), \qquad (X_1X_2)^{-1}A(X_1X_2) = X_2^{-1}\Lambda_1X_2 = \Lambda_1,
$$

后者是因为 $\Lambda_1$ 的每个对角块都是数量矩阵。所以 $X_1X_2$ 把 $A, B$ 同时对角化。$\square$

证明的思路是：$B$ 与 $A$ 可交换，所以 $B$ 把 $A$ 的每个特征子空间映到自身，于是可以在每个特征子空间内部再把 $B$ 对角化。

## 小结 {#summary}

本章的主线是"把方阵在相似意义下化简"：能对角化时化为对角矩阵（特征值分解），一般情形化为上三角矩阵，最简形式是 Jordan 标准形。

| 概念或结论 | 内容 | 位置 |
|---|---|---|
| 特征值、特征向量 | $A\boldsymbol{x} = \lambda\boldsymbol{x}$，$\boldsymbol{x} \ne \boldsymbol{0}$；$\lambda$ 是 $p_A(\lambda) = \det(\lambda I - A)$ 的根 | 定义 6.3.1、命题 6.3.1 |
| 特征子空间 | $\mathcal{N}(\lambda_0I - A)$ | 定义 6.3.3 |
| 圆盘定理 | 特征值落在 $\bigcup_i\{z : \vert z - a_{ii}\vert \le \sum_{j \ne i}\vert a_{ij}\vert\}$ 中 | 定理 6.4.1 |
| 迹与行列式 | $\sum\lambda_i = \operatorname{tr}(A)$，$\prod\lambda_i = \det A$ | 推论 6.4.1 |
| 特征值的运算 | $f(A)$ 的特征值为 $f(\lambda)$；$A^{-1}$ 的为 $\lambda^{-1}$；$f(A) = O$ ⇒ $f(\lambda) = 0$ | 性质 6.4.1 |
| 友矩阵 | 特征多项式为给定的首一多项式 | 命题 6.4.2 |
| 可对角化 | ⇔ 有 $n$ 个线性无关的特征向量 ⇔ 特征值都半单 | 定理 6.5.1、定理 6.6.2 |
| 不同特征值 | 特征向量线性无关；$n$ 个不同特征值 ⇒ 可对角化 | 定理 6.5.2、推论 6.5.1 |
| 两种重数 | $1 \le$ 几何重数 $\le$ 代数重数 | 定理 6.6.1 |
| 相似不变量 | 秩、特征多项式、特征值与两种重数、迹、行列式 | 定理 6.8.1 |
| 上三角化 | 任意方阵相似于上三角矩阵，对角元为特征值 | 定理 6.9.1 |
| Cayley–Hamilton 定理 | $p_A(A) = O$ | 定理 6.9.2 |
| Jordan 标准形 | $X^{-1}AX = \operatorname{diag}(J_{n_1}(\lambda_1), \dots, J_{n_r}(\lambda_r))$，不计次序唯一 | 定理 6.10.1 |
| 同时对角化 | 两个可对角化矩阵可同时对角化 ⇔ 可交换 | 定理 6.11.1 |

| 算法 | 步骤 | 说明 |
|---|---|---|
| 计算特征值与特征向量（算法 6.3.1） | 求 $p_A$ 的根；对每个 $\lambda_i$ 解 $(\lambda_iI - A)\boldsymbol{x} = \boldsymbol{0}$ | 手算流程；数值计算用 QR 迭代 |
| 对角化（算法 6.6.1） | 比较每个特征值的几何重数与代数重数；拼出 $X$ 与 $\Lambda$ | 得到 $A = X\Lambda X^{-1}$，$A^t = X\Lambda^tX^{-1}$ |
| 用 Cayley–Hamilton 定理化简（例 6.9.1） | $f = qp_A + r$ ⇒ $f(A) = r(A)$ | 计算高次幂与逆矩阵 |
