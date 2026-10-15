---
title: 矩阵与线性方程组
---

线性代数研究高维变量之间的线性关系。一元微积分处理一维变量的非线性函数，线性代数则处理"自变量和因变量都是向量、但对应法则是线性的"函数 $\boldsymbol{y} = A\boldsymbol{x}$；多元微积分（[2.2](/2.2)）把两者结合起来，其核心手段正是局部线性化。本章从 $\mathbb{R}^m$ 中的向量与线性运算出发，引入线性映射及其表示矩阵；线性代数最基本的问题——线性方程组——就是给定像求原像。我们用初等变换把方程组化成阶梯形，得到求解的标准流程（Gauss 消元法与 Gauss–Jordan 消元法）和解的判定定理；最后由映射的加法、数乘与复合定义矩阵的线性运算、转置和乘法。

本章的线性映射是 [1.3.3](/1.3.3#sec-3.6.3) 中域上**向量空间**之间**线性映射**的特例，这里只在 $\mathbb{R}^n$ 上讨论，一般的线性空间留到[第 8 章](/2.1.8)。下一章用矩阵乘法刻画消元的每一步，讨论逆矩阵与 LU 分解；[第 3 章](/2.1.3)用子空间的语言彻底回答方程组解的结构。

## 1.1. 向量与线性运算

平面向量 $\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$ 可以相加、可以与实数相乘，并且任意平面向量都能写成 $\boldsymbol{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$、$\boldsymbol{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ 的组合 $x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2$。这些概念和运算可以原样推广到 $m$ 维。

**定义 1.1.1（$m$ 维向量）** 设 $a_1, a_2, \dots, a_m \in \mathbb{R}$，称 $m$ 元有序数组

$$
\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_m \end{bmatrix}
$$

为一个 $m$ 维（实）向量，$a_i$ 称为 $\boldsymbol{a}$ 的第 $i$ 个分量或坐标。全体 $m$ 维实向量的集合记为 $\mathbb{R}^m$。$\boldsymbol{a}$ 也称为列向量，$\boldsymbol{a}^{\mathsf T} = [a_1\ a_2\ \cdots\ a_m]$ 称为行向量，上标 $\mathsf T$ 表示转置。分量取复数时得到复向量，全体 $m$ 维复向量的集合记为 $\mathbb{C}^m$。

向量用粗体小写字母表示。两个向量相等是指它们的每个分量都相等。

**定义 1.1.2（向量的线性运算）** 在 $\mathbb{R}^m$ 中定义加法与数乘：

$$
\begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} + \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} := \begin{bmatrix} a_1 + b_1 \\ \vdots \\ a_m + b_m \end{bmatrix}, \qquad
k\begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} := \begin{bmatrix} ka_1 \\ \vdots \\ ka_m \end{bmatrix}, \quad k \in \mathbb{R}.
$$

二者统称为向量的线性运算。

$\mathbb{R}^m$ 在线性运算下封闭，连同这两种运算称为线性空间或**向量空间**；不同维数的向量（如 $\mathbb{R}^m$ 与 $\mathbb{R}^n$ 中的向量，$m \ne n$）不能相加。此外定义两个向量 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^m$ 的**内积**

$$
\boldsymbol{a} \cdot \boldsymbol{b} = a_1b_1 + a_2b_2 + \cdots + a_mb_m = \sum_{j=1}^m a_jb_j \in \mathbb{R},
$$

它与向量的长度、夹角、正交等几何性质有关，在[第 4 章](/2.1.4)讨论。

**性质 1.1.1（线性运算的运算法则）** 对任意 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c} \in \mathbb{R}^m$，$k, \ell \in \mathbb{R}$：

1. 加法结合律：$(\boldsymbol{a} + \boldsymbol{b}) + \boldsymbol{c} = \boldsymbol{a} + (\boldsymbol{b} + \boldsymbol{c})$；
2. 加法交换律：$\boldsymbol{a} + \boldsymbol{b} = \boldsymbol{b} + \boldsymbol{a}$；
3. 零向量：$\boldsymbol{0} = [0\ \cdots\ 0]^{\mathsf T}$ 满足 $\boldsymbol{a} + \boldsymbol{0} = \boldsymbol{a}$，且 $0\boldsymbol{a} = \boldsymbol{0}$；
4. 负向量：$-\boldsymbol{a} = [-a_1\ \cdots\ -a_m]^{\mathsf T}$ 满足 $\boldsymbol{a} + (-\boldsymbol{a}) = \boldsymbol{0}$，且 $(-1)\boldsymbol{a} = -\boldsymbol{a}$；
5. 单位数：$1\boldsymbol{a} = \boldsymbol{a}$；
6. 数乘结合律：$(k\ell)\boldsymbol{a} = k(\ell\boldsymbol{a})$；
7. 数乘对数的分配律：$(k + \ell)\boldsymbol{a} = k\boldsymbol{a} + \ell\boldsymbol{a}$；
8. 数乘对向量的分配律：$k(\boldsymbol{a} + \boldsymbol{b}) = k\boldsymbol{a} + k\boldsymbol{b}$。

由负向量可以定义减法 $\boldsymbol{a} - \boldsymbol{b} = \boldsymbol{a} + (-\boldsymbol{b})$。这八条法则保证了向量可以像数一样做形式运算，例如 $2(\boldsymbol{a} + 4\boldsymbol{b}) - \boldsymbol{a} + 3\boldsymbol{b} = \boldsymbol{a} + 11\boldsymbol{b}$；它们正是 [1.3.3](/1.3.3) 中向量空间公理（[定义 3.6.1](/1.3.3#def-3.6.1)）的具体形式。

**定义 1.1.3（线性组合与线性表示）** 给定 $\mathbb{R}^m$ 中的向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 和数 $k_1, \dots, k_n \in \mathbb{R}$，称向量 $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n$ 为这个向量组的一个**线性组合**。若 $\boldsymbol{b} \in \mathbb{R}^m$ 能写成 $\boldsymbol{b} = k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n$，则称 $\boldsymbol{b}$ 可以被向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性表示。向量组

$$
\boldsymbol{e}_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad \boldsymbol{e}_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \dots, \quad \boldsymbol{e}_m = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}
$$

称为 $\mathbb{R}^m$ 的标准坐标向量组，$\boldsymbol{e}_i$ 称为第 $i$ 个标准坐标向量。

任意 $\boldsymbol{x} \in \mathbb{R}^m$ 都可以被标准坐标向量组线性表示：$\boldsymbol{x} = x_1\boldsymbol{e}_1 + x_2\boldsymbol{e}_2 + \cdots + x_m\boldsymbol{e}_m$。注意粗体的 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 表示 $n$ 个向量，与一个向量的分量 $a_1, \dots, a_m$ 相区别。

## 1.2. 线性映射

先回顾**映射**（[1.2.3](/1.2.3) 中的函数）：设 $X, Y$ 是集合，若 $X$ 中每个元素 $x$ 都按某种法则 $f$ 对应 $Y$ 中唯一的元素 $f(x)$，则称 $f\colon X \to Y$ 是一个映射。$X$ 是 $f$ 的**定义域**，$Y$ 是 $f$ 的陪域；$y = f(x)$ 称为 $x$ 的像，$x$ 称为 $y$ 的原像；集合 $f(X) = \{f(x) \mid x \in X\} \subseteq Y$ 称为 $f$ 的像集或**值域**。两个映射 $f, g\colon X \to Y$ 相等当且仅当 $f(x) = g(x)$ 对所有 $x \in X$ 成立。$X$ 中每个元素的像唯一，但 $Y$ 中的元素不一定有原像，有原像时也可以不唯一。定义域与陪域相同的映射称为 $X$ 上的变换；**恒等映射** $\mathrm{id}_X$（课件称恒同变换）把每个 $x$ 映到自身。

**定义 1.2.1（线性映射）** 若映射 $f\colon \mathbb{R}^n \to \mathbb{R}^m$ 满足叠加原理，则称 $f$ 是从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性映射；从 $\mathbb{R}^n$ 到自身的线性映射称为 $\mathbb{R}^n$ 上的**线性变换**。叠加原理是指以下两条性质：

1. 可加性：对任意 $\boldsymbol{x}, \boldsymbol{x}' \in \mathbb{R}^n$，$f(\boldsymbol{x} + \boldsymbol{x}') = f(\boldsymbol{x}) + f(\boldsymbol{x}')$；
2. 齐次性：对任意 $\boldsymbol{x} \in \mathbb{R}^n$，$k \in \mathbb{R}$，$f(k\boldsymbol{x}) = kf(\boldsymbol{x})$。

两条性质可以合写为 $f(k\boldsymbol{x} + \ell\boldsymbol{y}) = kf(\boldsymbol{x}) + \ell f(\boldsymbol{y})$。取 $k = 0$ 得 $f(\boldsymbol{0}_n) = \boldsymbol{0}_m$：线性映射把零向量映到零向量。恒等变换 $\mathrm{id}\colon \boldsymbol{x} \mapsto \boldsymbol{x}$ 是线性变换。

**例 1.2.1** 映射 $f\colon \mathbb{R} \to \mathbb{R}$ 中，$f(x) = 3x$ 与 $f(x) = 0$ 是线性映射；$f(x) = x + 1$、$f(x) = x^2$、$f(x) = |x|$、$f(x) = 1$ 都不是。由齐次性，$\mathbb{R} \to \mathbb{R}$ 的线性映射一定形如 $f(x) = f(1)\,x$，即正比例函数。

**例 1.2.2（平面上的变换）**

- 平移 $T_{\boldsymbol{a}}\colon \boldsymbol{x} \mapsto \boldsymbol{x} + \boldsymbol{a}$（$\boldsymbol{a} \ne \boldsymbol{0}$）不是线性变换，因为 $T_{\boldsymbol{a}}(\boldsymbol{0}) = \boldsymbol{a} \ne \boldsymbol{0}$。
- 绕原点逆时针旋转 $\theta$ 角的旋转变换 $R_\theta$ 是线性变换。它把 $\boldsymbol{e}_1, \boldsymbol{e}_2$ 分别转到 $[\cos\theta\ \sin\theta]^{\mathsf T}$、$[-\sin\theta\ \cos\theta]^{\mathsf T}$，由线性性

  $$
  R_\theta\left(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}\right) = x_1R_\theta(\boldsymbol{e}_1) + x_2R_\theta(\boldsymbol{e}_2) = x_1\begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix} + x_2\begin{bmatrix} -\sin\theta \\ \cos\theta \end{bmatrix}.
  $$

  所以只要知道标准坐标向量的像，旋转就完全确定。
- 关于过原点的直线 $\ell_\theta: x_2\cos\theta - x_1\sin\theta = 0$（与 $x_1$ 轴夹角为 $\theta$）的反射 $H_\theta$ 是线性变换；直线不过原点时，反射不是线性映射。

旋转的例子说明了一般规律。设 $f\colon \mathbb{R}^n \to \mathbb{R}^m$ 是线性映射，记 $\boldsymbol{a}_i = f(\boldsymbol{e}_i) \in \mathbb{R}^m$。对 $\boldsymbol{x} = x_1\boldsymbol{e}_1 + \cdots + x_n\boldsymbol{e}_n$，

$$
f(\boldsymbol{x}) = x_1f(\boldsymbol{e}_1) + \cdots + x_nf(\boldsymbol{e}_n) = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n,
$$

即 $f$ 由标准坐标向量组的像完全决定。

**定理 1.2.1（线性映射由标准坐标向量的像决定）** 任取 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n \in \mathbb{R}^m$，存在唯一的线性映射 $f\colon \mathbb{R}^n \to \mathbb{R}^m$，使得 $f(\boldsymbol{e}_i) = \boldsymbol{a}_i$（$i = 1, \dots, n$）。

**证明** 存在性：定义 $f(\boldsymbol{x}) = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n$。由向量运算法则，$f(k\boldsymbol{x} + \ell\boldsymbol{y}) = \sum_i (kx_i + \ell y_i)\boldsymbol{a}_i = kf(\boldsymbol{x}) + \ell f(\boldsymbol{y})$，故 $f$ 线性，且 $f(\boldsymbol{e}_i) = \boldsymbol{a}_i$。唯一性：若线性映射 $f, g$ 满足 $f(\boldsymbol{e}_i) = g(\boldsymbol{e}_i)$，则对任意 $\boldsymbol{x}$，$f(\boldsymbol{x}) = \sum_i x_if(\boldsymbol{e}_i) = \sum_i x_ig(\boldsymbol{e}_i) = g(\boldsymbol{x})$，所以 $f = g$。$\square$

## 1.3. 矩阵与矩阵–向量乘积

把 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 并排写成一个数表，就得到线性映射的完整"数值表示"。

**定义 1.3.1（矩阵）** 由 $mn$ 个实数 $a_{ij}$（$i = 1, \dots, m$；$j = 1, \dots, n$）排成的 $m$ 行 $n$ 列的矩形数表

$$
A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} = [a_{ij}]_{m \times n}
$$

称为 $m \times n$ **矩阵**，$a_{ij}$ 称为 $A$ 的 $(i, j)$ 元。$m = n$ 时称 $A$ 为 $n$ 阶方阵。两个矩阵相等是指它们的行数、列数相同且每个元素都相等。全体 $m \times n$ 实矩阵的集合记为 $\mathbb{R}^{m \times n}$。

矩阵用大写字母表示；双下标有歧义时用逗号隔开，如 $a_{i,j-1}$。$m$ 维列向量是 $m \times 1$ 矩阵，$n$ 维行向量是 $1 \times n$ 矩阵。矩阵既可以看作 $n$ 个列向量的横向排列，也可以看作 $m$ 个行向量的纵向排列：

$$
A = [\boldsymbol{a}_1\ \boldsymbol{a}_2\ \cdots\ \boldsymbol{a}_n] = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \vdots \\ \tilde{\boldsymbol{a}}_m^{\mathsf T} \end{bmatrix}, \qquad \boldsymbol{a}_j = \begin{bmatrix} a_{1j} \\ \vdots \\ a_{mj} \end{bmatrix} \in \mathbb{R}^m, \quad \tilde{\boldsymbol{a}}_i^{\mathsf T} = [a_{i1}\ \cdots\ a_{in}].
$$

**定义 1.3.2（表示矩阵）** 设 $f\colon \mathbb{R}^n \to \mathbb{R}^m$ 是线性映射，$\boldsymbol{a}_i = f(\boldsymbol{e}_i)$（$i = 1, \dots, n$），称 $m \times n$ 矩阵 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ 为 $f$ 在标准坐标向量下的**表示矩阵**。

由定理 1.2.1，线性映射 $\mathbb{R}^n \to \mathbb{R}^m$ 与 $m \times n$ 矩阵一一对应：每个线性映射由它的表示矩阵完全决定，每个矩阵也唯一确定一个线性映射。矩阵 $A$ 对应的线性映射记作 $T_A\colon \mathbb{R}^n \to \mathbb{R}^m$，$T_A(\boldsymbol{x}) = A\boldsymbol{x}$（乘积 $A\boldsymbol{x}$ 的定义见下）。

**定义 1.3.3（矩阵与向量的乘积）** $m \times n$ 矩阵 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ 与 $n$ 维列向量 $\boldsymbol{x}$ 的乘积定义为

$$
A\boldsymbol{x} = x_1\boldsymbol{a}_1 + x_2\boldsymbol{a}_2 + \cdots + x_n\boldsymbol{a}_n = \begin{bmatrix} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \end{bmatrix} = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{x} \\ \vdots \\ \tilde{\boldsymbol{a}}_m^{\mathsf T}\boldsymbol{x} \end{bmatrix}.
$$

于是线性映射可以写成 $f(\boldsymbol{x}) = T_A(\boldsymbol{x}) = A\boldsymbol{x}$。乘积有两种看法：

- 列观点：$A\boldsymbol{x}$ 是 $A$ 的列向量的线性组合，系数是 $\boldsymbol{x}$ 的分量；要求 $A$ 的列数等于 $\boldsymbol{x}$ 的维数。
- 行观点：$A\boldsymbol{x}$ 的第 $i$ 个分量是第 $i$ 行与 $\boldsymbol{x}$ 的内积 $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x}$，只依赖于 $A$ 的第 $i$ 行。特别地，两个同维向量的内积就是行向量与列向量的乘积：$\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}$。

**命题 1.3.1（分配律）** 设 $A$ 是 $m \times n$ 矩阵，对任意 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$ 和 $k_1, k_2 \in \mathbb{R}$，有 $A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) = k_1(A\boldsymbol{x}_1) + k_2(A\boldsymbol{x}_2)$。

这只是"$T_A$ 是线性映射"的矩阵写法。

**例 1.3.1** $3 \times 2$ 矩阵 $\begin{bmatrix} 2 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$ 把 $\mathbb{R}^2$ 映到 $\mathbb{R}^3$ 中由两列张成的平面；$2 \times 3$ 矩阵 $\begin{bmatrix} 1 & 0 & 3 \\ 1 & 2 & 2 \end{bmatrix}$ 把 $\mathbb{R}^3$ 映到 $\mathbb{R}^2$；$1 \times 2$ 矩阵 $[1\ \ 1]$ 把 $\mathbb{R}^2$ 映到 $\mathbb{R}$，它就是与向量 $[1\ 1]^{\mathsf T}$ 作内积。一般地，每个 $\boldsymbol{a} \in \mathbb{R}^n$ 都对应一个线性映射 $\mathbb{R}^n \to \mathbb{R}$，$\boldsymbol{x} \mapsto \boldsymbol{a}^{\mathsf T}\boldsymbol{x}$。

## 1.4. 平面上的线性变换与几类特殊方阵

按定义 1.3.2，平面线性变换的表示矩阵就是把 $\boldsymbol{e}_1, \boldsymbol{e}_2$ 的像并排。常见的几种汇总如下（$k, \ell \in \mathbb{R}$）：

| 变换 | 作用 | 表示矩阵 |
|---|---|---|
| 旋转 $R_\theta$ | 绕原点逆时针转 $\theta$ | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ |
| 反射 $H_\theta$ | 关于直线 $\ell_\theta$ 反射 | $\begin{bmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{bmatrix}$ |
| 对换 | 交换两个分量（关于直线 $x_2 = x_1$ 反射） | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ |
| 伸缩 | $x_1$ 方向乘 $k$，$x_2$ 方向乘 $\ell$ | $\begin{bmatrix} k & 0 \\ 0 & \ell \end{bmatrix}$ |
| 投影 | 投影到 $x_1$ 轴（$\ell = 0$ 的伸缩） | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ |
| 错切 $S_k$ | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \mapsto \begin{bmatrix} x_1 + kx_2 \\ x_2 \end{bmatrix}$ | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ |

错切把 $\boldsymbol{e}_1, \boldsymbol{e}_2$ 围成的正方形变成面积相同的平行四边形。下图画出这些变换对网格和单位正方形的作用：

![平面上几种线性变换对网格（蓝）与单位正方形（橙）的作用，红色箭头是标准坐标向量的像](./plots/plane-transformations.py)

三维的例子：给定 $\boldsymbol{a} \in \mathbb{R}^3$，叉积 $\boldsymbol{b} \mapsto \boldsymbol{a} \times \boldsymbol{b} = [a_2b_3 - a_3b_2\ \ a_3b_1 - a_1b_3\ \ a_1b_2 - a_2b_1]^{\mathsf T}$ 是 $\mathbb{R}^3$ 上的线性变换，表示矩阵为

$$
\begin{bmatrix} 0 & -a_3 & a_2 \\ a_3 & 0 & -a_1 \\ -a_2 & a_1 & 0 \end{bmatrix}.
$$

方阵中行号与列号相同的元素称为对角元素。下面几类方阵结构简单，在求解方程组时起关键作用（矩阵中为零的元素常省略不写）。

**定义 1.4.1（几类特殊方阵）**

1. 对角元素都是 $1$、其余元素都是 $0$ 的 $n$ 阶方阵称为 $n$ 阶**单位矩阵**，记为 $I_n = [\boldsymbol{e}_1\ \cdots\ \boldsymbol{e}_n]$。
2. 非对角元素全为 $0$ 的方阵称为**对角矩阵**，记为 $D = \operatorname{diag}(d_1, \dots, d_n)$。
3. 对角线下方元素全为 $0$ 的方阵 $U = [u_{ij}]$ 称为上三角矩阵；对角线上方元素全为 $0$ 的方阵 $L = [\ell_{ij}]$ 称为下三角矩阵，二者统称**三角矩阵**。对角元素也都是 $0$ 的称为严格上（下）三角矩阵，对角元素都是 $1$ 的称为单位上（下）三角矩阵。

几何上，$I_n\boldsymbol{x} = \boldsymbol{x}$ 表示恒等变换；$D\boldsymbol{x} = [d_1x_1\ \cdots\ d_nx_n]^{\mathsf T}$ 表示沿坐标轴的伸缩；单位上三角矩阵表示 $\mathbb{R}^n$ 上的错切。三角矩阵与向量的乘积为

$$
U\boldsymbol{x} = \begin{bmatrix} u_{11}x_1 + u_{12}x_2 + \cdots + u_{1n}x_n \\ u_{22}x_2 + \cdots + u_{2n}x_n \\ \vdots \\ u_{nn}x_n \end{bmatrix}, \qquad
L\boldsymbol{x} = \begin{bmatrix} \ell_{11}x_1 \\ \ell_{21}x_1 + \ell_{22}x_2 \\ \vdots \\ \ell_{n1}x_1 + \ell_{n2}x_2 + \cdots + \ell_{nn}x_n \end{bmatrix}.
$$

## 1.5. 线性方程组

线性代数最基本、最常见的应用是求解线性方程组。

**定义 1.5.1（线性方程组）** 给定 $m \times n$ 矩阵 $A = [a_{ij}]$ 和 $\boldsymbol{b} \in \mathbb{R}^m$，关于未知量 $x_1, \dots, x_n$ 的方程组

$$
\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1, \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2, \\ \quad\vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m, \end{cases}
\qquad \text{即} \qquad A\boldsymbol{x} = \boldsymbol{b},
$$

称为**线性方程组**，$A$ 称为系数矩阵，$\boldsymbol{b}$ 称为右端项。方程数 $m$ 不一定等于未知量个数 $n$。

求解线性方程组有三种几何图像：

- 映射的观点：求给定向量 $\boldsymbol{b}$ 在线性映射 $T_A$ 下的原像 $\boldsymbol{x}$。
- 行的观点：第 $i$ 个方程 $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x} = b_i$ 是 $\mathbb{R}^n$ 中的一个 $n-1$ 维（仿射）超平面，求解就是求 $m$ 个超平面的交点。
- 列的观点：$A\boldsymbol{x} = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b}$，求解就是寻找列向量的一个线性组合使其等于 $\boldsymbol{b}$。

线性方程组的解只有三种可能：无解、有唯一解、有无穷多组解（定理 1.7.2）。

系数矩阵是特殊方阵时，方程组容易求解：$I_n\boldsymbol{x} = \boldsymbol{b}$ 的解是 $\boldsymbol{x} = \boldsymbol{b}$；$D\boldsymbol{x} = \boldsymbol{b}$ 在对角元素都不为零时的解是 $x_i = b_i / d_i$；三角方程组则可以逐个求出未知量。

**算法 1.5.1（回代法）** 设 $U$ 是对角元素都不为零的 $n$ 阶上三角矩阵。求解 $U\boldsymbol{x} = \boldsymbol{b}$：先求 $x_n = b_n / u_{nn}$；再对 $i = n-1, \dots, 1$ 依次计算

$$
x_i = \frac{1}{u_{ii}}\left(b_i - \sum_{j=i+1}^n u_{ij}x_j\right).
$$

这种自下而上、从 $x_n$ 到 $x_1$ 求解的方法称为回代法。

**算法 1.5.2（前代法）** 设 $L$ 是对角元素都不为零的 $n$ 阶下三角矩阵。求解 $L\boldsymbol{x} = \boldsymbol{b}$：先求 $x_1 = b_1 / \ell_{11}$；再对 $i = 2, \dots, n$ 依次计算

$$
x_i = \frac{1}{\ell_{ii}}\left(b_i - \sum_{j=1}^{i-1} \ell_{ij}x_j\right).
$$

两种算法中，求第 $i$ 个未知量需要不超过 $n-1$ 次乘法和加减法、一次除法，总计约 $n^2$ 次浮点运算。对一般的系数矩阵，我们希望先把它化成三角形，这正是下面消元法要做的事。

## 1.6. 初等变换

**例 1.6.1** 求解 $\begin{cases} x_1 + x_2 = 8, \\ 2x_1 + 4x_2 = 22. \end{cases}$ 依次做三步变换：把第 1 个方程的 $-2$ 倍加到第 2 个方程上，得 $2x_2 = 6$；第 2 个方程乘 $\frac12$，得 $x_2 = 3$；把第 2 个方程的 $-1$ 倍加到第 1 个方程上，得 $x_1 = 5$。整个过程只有系数和右端项参与计算，把它们并排写成一个矩阵，过程可以简写为

$$
\begin{bmatrix} 1 & 1 & 8 \\ 2 & 4 & 22 \end{bmatrix} \to \begin{bmatrix} 1 & 1 & 8 \\ 0 & 2 & 6 \end{bmatrix} \to \begin{bmatrix} 1 & 1 & 8 \\ 0 & 1 & 3 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 3 \end{bmatrix},
$$

得唯一解 $x_1 = 5$，$x_2 = 3$。系数矩阵先变成上三角矩阵，再变成单位矩阵。

**例 1.6.2** 求解 $\begin{cases} 2x_2 - x_3 = 1, \\ x_1 - x_2 + x_3 = 0, \\ 2x_1 - 2x_2 + 3x_3 = 1. \end{cases}$ 第一个方程不含 $x_1$，先对换第 1、2 个方程，再消元：

$$
\begin{bmatrix} 0 & 2 & -1 & 1 \\ 1 & -1 & 1 & 0 \\ 2 & -2 & 3 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 1 & 0 \\ 0 & 2 & -1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 1 & 0 \\ 0 & 1 & -\frac12 & \frac12 \\ 0 & 0 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix},
$$

得唯一解 $\boldsymbol{x} = [0\ 1\ 1]^{\mathsf T}$。

**定义 1.6.1（初等变换）** 线性方程组的三类初等变换是：对换变换（互换两个方程的位置）、倍乘变换（把某个方程两边同乘一个非零常数 $k$）、倍加变换（把某个方程的 $k$ 倍加到另一个方程上）。相应地，矩阵的三类**初等行变换**（列变换）是：互换两行（列）；某一行（列）乘非零常数 $k$；把某一行（列）的 $k$ 倍加到另一行（列）上。把系数矩阵与右端项并排得到的 $m \times (n+1)$ 矩阵 $[A\ \boldsymbol{b}]$（也写作 $[A \mid \boldsymbol{b}]$）称为方程组的**增广矩阵**。

对线性方程组做初等变换，等价于对增广矩阵做初等行变换。

**命题 1.6.1** 初等变换都可逆，且逆变换也是同类的初等变换：对换变换的逆是它自身；参数为 $k$ 的倍乘变换的逆是参数为 $\frac1k$ 的倍乘变换；参数为 $k$ 的倍加变换的逆是参数为 $-k$ 的倍加变换。

**定理 1.6.1（同解变换）** 线性方程组经过一次初等变换得到的新方程组与原方程组同解。

**证明** 设 $A\boldsymbol{x} = \boldsymbol{b}$ 经过一次初等变换变成 $\tilde{A}\boldsymbol{x} = \tilde{\boldsymbol{b}}$。新方程组的每个方程都是原方程的组合，所以原方程组的解都满足新方程组。由命题 1.6.1，$\tilde{A}\boldsymbol{x} = \tilde{\boldsymbol{b}}$ 也可以经过一次初等变换变回 $A\boldsymbol{x} = \boldsymbol{b}$，同理新方程组的解也是原方程组的解。$\square$

## 1.7. 阶梯形与消元法

并非每个方阵都能化成单位矩阵，方程组也不一定是方的。先看两个例子，再给出一般的目标形状。

**例 1.7.1** 求解 $\begin{cases} 2x_3 + x_4 = 1, \\ x_1 - x_2 + 4x_3 = 0. \end{cases}$ 对增广矩阵做对换、倍乘、倍加：

$$
\begin{bmatrix} 0 & 0 & 2 & 1 & 1 \\ 1 & -1 & 4 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 4 & 0 & 0 \\ 0 & 0 & 2 & 1 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 4 & 0 & 0 \\ 0 & 0 & 1 & \frac12 & \frac12 \end{bmatrix} \to
\begin{bmatrix} 1 & -1 & 0 & -2 & -2 \\ 0 & 0 & 1 & \frac12 & \frac12 \end{bmatrix}.
$$

方程组化为 $x_1 - x_2 - 2x_4 = -2$，$x_3 + \frac12x_4 = \frac12$，即

$$
x_1 = -2 + x_2 + 2x_4, \qquad x_3 = \tfrac12 - \tfrac12x_4, \qquad x_2, x_4 \in \mathbb{R}.
$$

$x_2, x_4$ 可以任意取值，$x_1, x_3$ 由它们和右端项决定；变换后 $x_1, x_3$ 所在的列构成单位矩阵。写成向量形式，解集为

$$
\left\{ \begin{bmatrix} -2 \\ 0 \\ \frac12 \\ 0 \end{bmatrix} + a\begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \end{bmatrix} + b\begin{bmatrix} 2 \\ 0 \\ -\frac12 \\ 1 \end{bmatrix} \;\middle|\; a, b \in \mathbb{R} \right\}.
$$

**例 1.7.2** 求解 $\begin{cases} x_1 + x_2 - 3x_3 = -1, \\ 2x_1 + x_2 - 2x_3 = 1, \\ x_1 + x_2 + x_3 = 3, \\ x_1 + 2x_2 - 3x_3 = 0. \end{cases}$ 从下标最小的变量开始，对增广矩阵向下消元：

$$
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 2 & 1 & -2 & 1 \\ 1 & 1 & 1 & 3 \\ 1 & 2 & -3 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & -1 & 4 & 3 \\ 0 & 0 & 4 & 4 \\ 0 & 1 & 0 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & -1 & 4 & 3 \\ 0 & 0 & 4 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}.
$$

回代得 $x_3 = 1$，$x_2 = 1$，$x_1 = 1$。也可以继续把主元化成 $1$，并从最后一个主元开始向上消元：

$$
\begin{bmatrix} 1 & 1 & -3 & -1 \\ 0 & 1 & -4 & -3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix},
$$

直接读出解 $x_1 = x_2 = x_3 = 1$。若把第 4 个方程的右端改成 $3$，同样的消元得到最后一行 $[0\ 0\ 0\ 3]$，即矛盾方程 $0 = 3$，方程组无解。

**定义 1.7.1（阶梯形矩阵）** 元素全为零的行称为零行，否则称为非零行；非零行左起第一个非零元素称为该行的**主元**。若矩阵满足：零行都在所有非零行的下方，且主元的列指标随行指标的增加而严格增加，则称它为**阶梯形矩阵**。非零行的行数称为阶梯数；主元所在的列称为主列，其他列称为自由列。

**定义 1.7.2（行简化阶梯形）** 若阶梯形矩阵的主元都是 $1$，且主列中除主元外的元素都是 $0$，则称它为**行简化阶梯形**矩阵。矩阵 $A$ 化成的行简化阶梯形记为 $\operatorname{rref}(A)$。

用 $\bullet$ 表示主元、$\star$ 表示可能不为零的数，两种形状例如

$$
\begin{bmatrix} \bullet & \star & \star & \star & \star & \star \\ 0 & 0 & \bullet & \star & \star & \star \\ 0 & 0 & 0 & \bullet & \star & \star \\ 0 & 0 & 0 & 0 & 0 & \bullet \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix},
\qquad
\begin{bmatrix} 1 & \star & 0 & 0 & \star & 0 \\ 0 & 0 & 1 & 0 & \star & 0 \\ 0 & 0 & 0 & 1 & \star & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

阶梯形中主元所在行与主列交叉处的元素组成对角元素非零的上三角矩阵；行简化阶梯形中它们组成单位矩阵。

**定义 1.7.3（主变量与自由变量）** 把方程组的增广矩阵化成阶梯形后，主列对应的未知量称为主变量，自由列对应的未知量称为**自由变量**。用自由变量和右端项表示主变量的表达式称为方程组的通解（一般解）。

自由变量可以任意取值；主变量的选取一般不唯一，通常从下标最小的变量开始选。

**定理 1.7.1** 任意矩阵都可以只用对换行变换和倍加行变换化为阶梯形；任意矩阵都可以用初等行变换化为行简化阶梯形。

**证明** 对行数 $m$ 用数学归纳法证明第一条。$m = 1$ 时，$1 \times n$ 矩阵自然是阶梯形。假设 $(m-1) \times n$ 矩阵都可以化成阶梯形，考察 $m \times n$ 矩阵 $A$：

1. 若 $a_{11} \ne 0$，把第 1 行的 $-a_{i1}/a_{11}$ 倍加到第 $i$ 行（$2 \le i \le m$），第一列除 $a_{11}$ 外全化为零。第 $2$ 到 $m$ 行、第 $2$ 到 $n$ 列交叉处构成 $(m-1) \times (n-1)$ 矩阵，由归纳假设可化为阶梯形（这些行变换不影响已化为零的第一列），于是 $A$ 化成了阶梯形。
2. 若 $a_{11} = 0$ 但第一列有非零元素 $a_{i1}$，对换第 $1, i$ 行，归于情形 1。
3. 若第一列全为零，取左起第一个非零列（第 $j$ 列），对第 $j$ 到 $n$ 列构成的矩阵做同样的讨论；若矩阵全为零，它已是阶梯形。

第二条：先化成阶梯形，用倍乘变换把每个主元化成 $1$，再从最后一个主元开始，依次用倍加变换把每个主元上方的元素化为零。向上消元时，主元所在行左侧都是零，不会破坏已经得到的零。$\square$

**定理 1.7.2（判定定理）** 把增广矩阵 $[A\ \boldsymbol{b}]$ 化成阶梯形（$A$ 同时化成阶梯形），设 $A$ 化成的阶梯形的阶梯数为 $r$，$n$ 为未知量个数，则

1. 若 $[A\ \boldsymbol{b}]$ 对应的阶梯数大于 $r$（此时恰为 $r+1$），方程组无解；
2. 若 $[A\ \boldsymbol{b}]$ 对应的阶梯数等于 $r$，方程组有解，其中：
   - $r = n$ 时有唯一解；
   - $r < n$ 时有无穷多组解。

**证明** 由定理 1.6.1，阶梯形对应的方程组与原方程组同解。若增广矩阵的阶梯数为 $r+1$，第 $r+1$ 行是 $[0\ \cdots\ 0\ c]$（$c \ne 0$），对应矛盾方程 $0 = c$。否则零行对应恒等式 $0 = 0$，可以去掉；剩下 $r$ 个方程，每个主变量的系数（主元）非零。$r = n$ 时没有自由变量，系数矩阵是对角元素非零的上三角矩阵，回代法给出唯一解；$r < n$ 时自由变量可任意取值，每组取值通过回代唯一确定主变量，所以有无穷多组解。$\square$

由定理 1.7.1 和定理 1.7.2，求解线性方程组可以完全按标准流程进行：

**算法 1.7.1（Gauss 消元法）** 输入线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$。

1. 写出增广矩阵 $[A\ \boldsymbol{b}]$。
2. 从左到右逐列处理：在当前列中选一个非零元素作主元，必要时对换行，把它移到当前行；用倍加行变换把主元下方的元素全部化为零；转到下一行、下一列。得到阶梯形。
3. 按判定定理判断有无解。
4. 有解时，把自由变量作为参数，用回代法求出主变量。

**算法 1.7.2（Gauss–Jordan 消元法）** 把增广矩阵用初等行变换化成行简化阶梯形（先按算法 1.7.1 向下消元，再把主元化成 $1$ 并向上消元），把自由变量移到方程右端，即得方程组的通解。

消元法是计算机求解线性方程组（数值线性代数）的基本方法。对 $n$ 阶方阵，向下消元约需 $\frac23n^3$ 次浮点运算，回代只需约 $n^2$ 次；Gauss–Jordan 消元把上方元素也消去，约需 $n^3$ 次。所以数值计算中通常用 Gauss 消元加回代，下一章把这一过程整理成 LU 分解。下面是 Gauss–Jordan 消元的一个精确算术实现：

```python
from fractions import Fraction

def rref(rows):
    """Gauss-Jordan elimination with exact arithmetic; returns (R, pivot_columns)."""
    R = [[Fraction(x) for x in row] for row in rows]
    m, n = len(R), len(R[0])
    pivots, r = [], 0                      # r = index of the next pivot row
    for j in range(n):
        p = next((i for i in range(r, m) if R[i][j] != 0), None)
        if p is None:                      # no pivot in column j: a free column
            continue
        R[r], R[p] = R[p], R[r]            # swap rows
        R[r] = [x / R[r][j] for x in R[r]] # scale the pivot to 1
        for i in range(m):                 # eliminate above and below the pivot
            if i != r and R[i][j] != 0:
                R[i] = [a - R[i][j] * b for a, b in zip(R[i], R[r])]
        pivots.append(j)
        r += 1
        if r == m:
            break
    return R, pivots

# Example 1.7.2: rows of R are [1,0,0,1], [0,1,0,1], [0,0,1,1], [0,0,0,0]
R, pivots = rref([[1, 1, -3, -1], [2, 1, -2, 1], [1, 1, 1, 3], [1, 2, -3, 0]])
print(pivots)  # [0, 1, 2]
```

## 1.8. 齐次线性方程组

**定义 1.8.1（齐次线性方程组）** 线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 当 $\boldsymbol{b} = \boldsymbol{0}$ 时称为**齐次线性方程组**，当 $\boldsymbol{b} \ne \boldsymbol{0}$ 时称为非齐次的。$\boldsymbol{x} = \boldsymbol{0}$ 总是齐次方程组的解，称为零解或平凡解；其他的解（如果存在）称为非零解或非平凡解。

若 $\boldsymbol{x}$ 是 $A\boldsymbol{x} = \boldsymbol{0}$ 的非零解，则 $k\boldsymbol{x}$（$k \in \mathbb{R}$）也都是解，所以有非零解时就有无穷多组解。增广矩阵 $[A\ \boldsymbol{0}]$ 的阶梯数总等于 $A$ 的阶梯数，消元时只需对系数矩阵计算。把判定定理用于齐次方程组，得到：

**推论 1.8.1** 设 $A$ 化成的阶梯形的阶梯数为 $r$，$n$ 为未知量个数。齐次线性方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 只有零解当且仅当 $r = n$；有非零解当且仅当 $r < n$。

**推论 1.8.2** 若齐次线性方程组的方程个数小于未知量个数，则它一定有非零解。

**证明** 阶梯数不超过方程个数 $m$，而 $m < n$，故 $r \le m < n$，由推论 1.8.1 即得。$\square$

**例 1.8.1** 求解齐次线性方程组

$$
\begin{cases} x_1 + x_2 - 3x_4 - x_5 = 0, \\ x_1 - x_2 + 2x_3 - x_4 = 0, \\ 4x_1 - 2x_2 + 6x_3 + 3x_4 - 4x_5 = 0, \\ 2x_1 + 4x_2 - 2x_3 + 4x_4 - 7x_5 = 0. \end{cases}
$$

对系数矩阵消元：

$$
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 1 & -1 & 2 & -1 & 0 \\ 4 & -2 & 6 & 3 & -4 \\ 2 & 4 & -2 & 4 & -7 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & -6 & 6 & 15 & 0 \\ 0 & 2 & -2 & 10 & -5 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 12 & -4 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

阶梯数 $3 < 5$，有无穷多组解；主变量为 $x_1, x_2, x_4$，自由变量为 $x_3, x_5$。继续化为行简化阶梯形

$$
\begin{bmatrix} 1 & 0 & 1 & 0 & -\frac76 \\ 0 & 1 & -1 & 0 & -\frac56 \\ 0 & 0 & 0 & 1 & -\frac13 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix},
$$

移项得通解 $x_1 = -x_3 + \frac76x_5$，$x_2 = x_3 + \frac56x_5$，$x_4 = \frac13x_5$，其中 $x_3, x_5 \in \mathbb{R}$。

## 1.9. 矩阵的线性运算与转置

线性映射可以相加、数乘、复合；矩阵的运算就按"表示矩阵跟随映射"的原则来定义。

**定义 1.9.1（映射的线性运算）** 设 $T_A, T_B\colon \mathbb{R}^n \to \mathbb{R}^m$ 是线性映射，$k \in \mathbb{R}$，定义映射

$$
T_A + T_B\colon \boldsymbol{x} \mapsto T_A(\boldsymbol{x}) + T_B(\boldsymbol{x}), \qquad kT_A\colon \boldsymbol{x} \mapsto kT_A(\boldsymbol{x}),
$$

分别称为 $T_A$ 与 $T_B$ 的和、数 $k$ 与 $T_A$ 的数乘。

容易验证 $T_A + T_B$ 与 $kT_A$ 仍是线性映射，且对任意 $k, \ell$ 有 $(kT_A + \ell T_B)(\boldsymbol{x}) = kT_A(\boldsymbol{x}) + \ell T_B(\boldsymbol{x})$。全体 $\mathbb{R}^n \to \mathbb{R}^m$ 的线性映射在这两种运算下封闭，并满足与性质 1.1.1 相同的八条法则（零元素是零映射）；它本身构成一个线性空间（[第 8 章](/2.1.8)）。

**定义 1.9.2（矩阵的线性运算）** 设 $A = [a_{ij}]_{m \times n}$，$B = [b_{ij}]_{m \times n}$，$k \in \mathbb{R}$，定义

$$
A + B = [a_{ij} + b_{ij}]_{m \times n}, \qquad kA = [ka_{ij}]_{m \times n}.
$$

所有元素全为 $0$ 的矩阵称为零矩阵，记为 $O_{m \times n}$ 或 $O$；$-A = (-1)A$ 称为 $A$ 的负矩阵，$A - B = A + (-B)$。

$T_A + T_B$、$kT_A$ 的表示矩阵分别是 $A + B$、$kA$（逐列比较 $\boldsymbol{e}_j$ 的像即得），即 $T_A + T_B = T_{A+B}$，$kT_A = T_{kA}$。矩阵的加法与数乘同样满足八条运算法则，$\mathbb{R}^{m \times n}$ 也是一个线性空间。由映射的等式 $(kT_A + \ell T_B)(\boldsymbol{x}) = kT_A(\boldsymbol{x}) + \ell T_B(\boldsymbol{x})$ 立得：

**命题 1.9.1** 矩阵与向量的乘积对矩阵的线性运算满足分配律：$(kA + \ell B)\boldsymbol{x} = k(A\boldsymbol{x}) + \ell(B\boldsymbol{x})$。

**定义 1.9.3（矩阵的转置）** 对调 $m \times n$ 矩阵 $A$ 的行与列得到的 $n \times m$ 矩阵称为 $A$ 的**转置**，记为 $A^{\mathsf T}$，即 $A^{\mathsf T}$ 的 $(j, i)$ 元是 $a_{ij}$：

$$
A^{\mathsf T} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]^{\mathsf T} = \begin{bmatrix} \boldsymbol{a}_1^{\mathsf T} \\ \vdots \\ \boldsymbol{a}_n^{\mathsf T} \end{bmatrix}.
$$

转置是向量转置的推广，满足 $(A^{\mathsf T})^{\mathsf T} = A$，$(A + B)^{\mathsf T} = A^{\mathsf T} + B^{\mathsf T}$，$(kA)^{\mathsf T} = kA^{\mathsf T}$。

**定义 1.9.4（对称矩阵与反对称矩阵）** 满足 $A = A^{\mathsf T}$ 的矩阵称为**对称矩阵**；满足 $A = -A^{\mathsf T}$ 的矩阵称为**反对称矩阵**（斜对称矩阵）。

对称矩阵与反对称矩阵一定是方阵；反对称矩阵的对角元素满足 $a_{ii} = -a_{ii}$，所以都是 $0$。

**命题 1.9.2** 任意方阵 $A$ 都可以唯一地表示为一个对称矩阵 $B$ 与一个反对称矩阵 $C$ 之和：

$$
A = B + C, \qquad B = \tfrac12(A + A^{\mathsf T}), \quad C = \tfrac12(A - A^{\mathsf T}).
$$

**证明** 直接验证 $B^{\mathsf T} = B$，$C^{\mathsf T} = -C$，$B + C = A$。唯一性：若 $A = B + C$，$B$ 对称、$C$ 反对称，则 $A^{\mathsf T} = B - C$，两式相加、相减即得 $B, C$ 的表达式。$\square$

## 1.10. 矩阵乘法

**定义 1.10.1（映射的复合）** 设 $f\colon X \to Y$，$g\colon Y \to Z$ 是映射，映射 $h\colon X \to Z$，$x \mapsto g(f(x))$ 称为 $g$ 与 $f$ 的复合，记为 $h = g \circ f$。

要定义 $g \circ f$，$g$ 的定义域必须是 $f$ 的陪域。复合满足结合律：对 $f\colon X \to Y$，$g\colon Y \to Z$，$h\colon Z \to W$，有 $h \circ (g \circ f) = (h \circ g) \circ f$，因为两边都把 $x$ 映到 $h(g(f(x)))$。

**命题 1.10.1** 设 $T_B\colon \mathbb{R}^n \to \mathbb{R}^m$，$T_A\colon \mathbb{R}^m \to \mathbb{R}^\ell$ 是线性映射，则 $T_A \circ T_B\colon \mathbb{R}^n \to \mathbb{R}^\ell$ 也是线性映射。并且对线性映射 $T_B, T_{B'}\colon \mathbb{R}^n \to \mathbb{R}^m$，$T_A, T_{A'}\colon \mathbb{R}^m \to \mathbb{R}^\ell$ 和 $k \in \mathbb{R}$，有

$$
(T_A + T_{A'}) \circ T_B = T_A \circ T_B + T_{A'} \circ T_B, \quad T_A \circ (T_B + T_{B'}) = T_A \circ T_B + T_A \circ T_{B'}, \quad k(T_A \circ T_B) = (kT_A) \circ T_B = T_A \circ (kT_B).
$$

**证明** 线性：$(T_A \circ T_B)(k\boldsymbol{x} + \ell\boldsymbol{x}') = T_A(kT_B(\boldsymbol{x}) + \ell T_B(\boldsymbol{x}')) = k(T_A \circ T_B)(\boldsymbol{x}) + \ell(T_A \circ T_B)(\boldsymbol{x}')$。第一个分配律：$((T_A + T_{A'}) \circ T_B)(\boldsymbol{x}) = T_A(T_B(\boldsymbol{x})) + T_{A'}(T_B(\boldsymbol{x}))$；第二个分配律要用到 $T_A$ 的可加性；数乘一式要用到 $T_A$ 的齐次性。$\square$

复合映射 $T_A \circ T_B$ 的表示矩阵是什么？设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ 是 $\ell \times m$ 矩阵，$B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ 是 $m \times n$ 矩阵，则第 $j$ 列是 $T_A(T_B(\boldsymbol{e}_j)) = A\boldsymbol{b}_j$。

**定义 1.10.2（矩阵乘法）** $\ell \times m$ 矩阵 $A$ 与 $m \times n$ 矩阵 $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ 的乘积是 $\ell \times n$ 矩阵

$$
AB = A[\boldsymbol{b}_1\ \boldsymbol{b}_2\ \cdots\ \boldsymbol{b}_n] = [A\boldsymbol{b}_1\ A\boldsymbol{b}_2\ \cdots\ A\boldsymbol{b}_n].
$$

于是 $AB$ 是 $T_A \circ T_B$ 的表示矩阵，即 $T_A \circ T_B = T_{AB}$，满足

$$
(AB)\boldsymbol{x} = A(B\boldsymbol{x}).
$$

计算 $AB$ 要求 $A$ 的列数等于 $B$ 的行数（对应于 $T_A$ 的定义域是 $T_B$ 的陪域）；$AB$ 的行数等于 $A$ 的行数，列数等于 $B$ 的列数。设 $A$ 的行向量为 $\tilde{\boldsymbol{a}}_1^{\mathsf T}, \dots, \tilde{\boldsymbol{a}}_\ell^{\mathsf T}$，则

$$
AB = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_n \\ \vdots & & \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_n \end{bmatrix} = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}B \\ \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}B \end{bmatrix}, \qquad c_{ik} = \tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{b}_k = \sum_{j=1}^m a_{ij}b_{jk}.
$$

$AB$ 的第 $k$ 列 $A\boldsymbol{b}_k$ 只由 $A$ 和 $B$ 的第 $k$ 列决定；第 $i$ 行 $\tilde{\boldsymbol{a}}_i^{\mathsf T}B$ 只由 $A$ 的第 $i$ 行和 $B$ 决定。按元素公式，计算 $AB$ 需要 $\ell mn$ 次乘法，两个 $n$ 阶方阵相乘约需 $2n^3$ 次浮点运算。

**例 1.10.1** 对 $\boldsymbol{x} \in \mathbb{R}^2$ 先做逆时针旋转 $90^\circ$，$B = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$；再对换两个分量，$A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$。复合映射的表示矩阵为

$$
AB = [A\boldsymbol{b}_1\ A\boldsymbol{b}_2] = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix},
$$

即关于 $x_1$ 轴的反射。

**命题 1.10.2（矩阵乘法的运算法则）** 在乘积有意义时：

1. 结合律：$A(BC) = (AB)C$，因此可以不加括号地写 $ABC$；
2. 分配律：$(A + B)C = AC + BC$，$A(B + C) = AB + AC$；
3. 与数乘交换：$k(AB) = (kA)B = A(kB)$；
4. 转置：$\boldsymbol{a}^{\mathsf T}\boldsymbol{x} = \boldsymbol{x}^{\mathsf T}\boldsymbol{a}$，$(A\boldsymbol{x})^{\mathsf T} = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}$，$(AB)^{\mathsf T} = B^{\mathsf T}A^{\mathsf T}$。

**证明** 结合律有三种证法。其一，$(AB)C$ 与 $A(BC)$ 分别是 $(T_A \circ T_B) \circ T_C$ 与 $T_A \circ (T_B \circ T_C)$ 的表示矩阵，而映射的复合满足结合律。其二，设 $C = [\boldsymbol{c}_1\ \cdots\ \boldsymbol{c}_p]$，由 $(AB)\boldsymbol{x} = A(B\boldsymbol{x})$，

$$
A(BC) = [A(B\boldsymbol{c}_1)\ \cdots\ A(B\boldsymbol{c}_p)] = [(AB)\boldsymbol{c}_1\ \cdots\ (AB)\boldsymbol{c}_p] = (AB)C.
$$

其三，比较 $(i, s)$ 元：两边都等于 $\sum_{j=1}^m\sum_{k=1}^n a_{ij}b_{jk}c_{ks}$。第 2、3 条由命题 1.10.1 对应到表示矩阵即得。第 4 条：$\boldsymbol{a}^{\mathsf T}\boldsymbol{x} = \sum_j a_jx_j = \boldsymbol{x}^{\mathsf T}\boldsymbol{a}$；$(A\boldsymbol{x})^{\mathsf T}$ 的第 $i$ 个分量是 $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x} = \boldsymbol{x}^{\mathsf T}\tilde{\boldsymbol{a}}_i$，而 $A^{\mathsf T} = [\tilde{\boldsymbol{a}}_1\ \cdots\ \tilde{\boldsymbol{a}}_\ell]$，故 $(A\boldsymbol{x})^{\mathsf T} = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}$；最后，$(AB)^{\mathsf T}$ 的第 $k$ 行是 $(A\boldsymbol{b}_k)^{\mathsf T} = \boldsymbol{b}_k^{\mathsf T}A^{\mathsf T}$，正是 $B^{\mathsf T}A^{\mathsf T}$ 的第 $k$ 行。$\square$

对正整数 $k$，方阵 $A$ 的 $k$ 次幂定义为 $A^k = \underbrace{AA\cdots A}_{k\ \text{个}}$，并约定 $A^0 = I$。对多项式 $f(x) = a_0 + a_1x + \cdots + a_px^p$，定义矩阵多项式 $f(A) = a_0I + a_1A + \cdots + a_pA^p$。

**例 1.10.2** 对 $\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^n$，$A = \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ 是 $n$ 阶方阵。由结合律，$\boldsymbol{v}^{\mathsf T}\boldsymbol{u}$ 是一个数，可以提出来：

$$
A^k = \boldsymbol{u}(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})\cdots(\boldsymbol{v}^{\mathsf T}\boldsymbol{u})\boldsymbol{v}^{\mathsf T} = (\boldsymbol{v}^{\mathsf T}\boldsymbol{u})^{k-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}.
$$

矩阵乘法与数的乘法有三点主要区别：

- 一般不满足交换律。$AB$ 与 $BA$ 不一定同时有意义；都有意义时，只有 $A, B$ 是同阶方阵才同阶；即使同阶也可能不相等：

  $$
  \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \qquad \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}.
  $$

  $AB$ 读作"$A$ 左乘 $B$"或"$B$ 右乘 $A$"；若 $AB = BA$，称 $A, B$ 可交换。
- 一般不满足消去律：由 $AB = AC$ 和 $A \ne O$ 不能推出 $B = C$。例如 $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$，$B = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$，$C = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ 时 $AB = AC = O$。消去律成立需要 $A$ 可逆（下一章）。
- 有零因子：两个非零矩阵的乘积可以是零矩阵，所以 $AB = O$ 推不出 $A = O$ 或 $B = O$。

**例 1.10.3** $I_mA = A = AI_n$；$kI_n$ 称为数量矩阵，$(kI_n)A = kA$。平面上两个旋转的复合仍是旋转，$R_{\theta_1}R_{\theta_2} = R_{\theta_1 + \theta_2} = R_{\theta_2}R_{\theta_1}$，比较两边的元素就得到三角函数的和角公式。反射与自身的复合是恒等变换：$H_\theta^2 = I_2$，可以直接用 $\cos^2 2\theta + \sin^2 2\theta = 1$ 验证。

最后定义一个常用的数值特征。

**定义 1.10.3（迹）** 方阵 $A = [a_{ij}]_{n \times n}$ 的对角元素之和称为 $A$ 的**迹**，记为 $\operatorname{tr}(A) = a_{11} + a_{22} + \cdots + a_{nn}$。

**性质 1.10.1** 迹是线性的：$\operatorname{tr}(kA + \ell B) = k\operatorname{tr}(A) + \ell\operatorname{tr}(B)$；$\operatorname{tr}(A^{\mathsf T}) = \operatorname{tr}(A)$。设 $A, B$ 分别是 $m \times n$、$n \times m$ 矩阵，则 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$。

**证明** 前两条由定义直接得到。$AB$ 是 $m$ 阶方阵，$BA$ 是 $n$ 阶方阵，

$$
\operatorname{tr}(AB) = \sum_{i=1}^m\sum_{j=1}^n a_{ij}b_{ji} = \sum_{j=1}^n\sum_{i=1}^m b_{ji}a_{ij} = \operatorname{tr}(BA). \qquad \square
$$

## 小结

本章建立了"线性映射 $\leftrightarrow$ 矩阵"的对应，并把线性方程组的求解化为标准流程。

| 类别 | 内容 |
|---|---|
| 定义 | $m$ 维向量与线性运算（定义 1.1.1、1.1.2）；线性组合、标准坐标向量组（定义 1.1.3）；线性映射与线性变换（定义 1.2.1）；矩阵、表示矩阵、矩阵与向量的乘积（定义 1.3.1–1.3.3）；单位矩阵、对角矩阵、三角矩阵（定义 1.4.1）；线性方程组（定义 1.5.1）；初等变换与增广矩阵（定义 1.6.1）；阶梯形、行简化阶梯形、主变量与自由变量（定义 1.7.1–1.7.3）；齐次线性方程组（定义 1.8.1）；矩阵的线性运算、转置、对称与反对称矩阵（定义 1.9.2–1.9.4）；矩阵乘法（定义 1.10.2）；迹（定义 1.10.3） |
| 定理 | 线性映射由标准坐标向量的像唯一决定（定理 1.2.1）；初等变换同解（定理 1.6.1）；任意矩阵可化为（行简化）阶梯形（定理 1.7.1）；判定定理（定理 1.7.2）；方程数少于未知量数的齐次方程组有非零解（推论 1.8.2）；对称–反对称分解（命题 1.9.2）；矩阵乘法的运算法则（命题 1.10.2）；$\operatorname{tr}(AB) = \operatorname{tr}(BA)$（性质 1.10.1） |
| 算法 | 回代法与前代法（算法 1.5.1、1.5.2，约 $n^2$ 次运算）；Gauss 消元法（算法 1.7.1，约 $\frac23n^3$ 次）；Gauss–Jordan 消元法（算法 1.7.2，约 $n^3$ 次） |

| 观点 | $A\boldsymbol{x}$ | $AB$ |
|---|---|---|
| 列 | 列向量的线性组合 $\sum_j x_j\boldsymbol{a}_j$ | $[A\boldsymbol{b}_1\ \cdots\ A\boldsymbol{b}_n]$ |
| 行 | 第 $i$ 个分量 $\tilde{\boldsymbol{a}}_i^{\mathsf T}\boldsymbol{x}$ | 第 $i$ 行 $\tilde{\boldsymbol{a}}_i^{\mathsf T}B$ |
| 元素 | $\sum_j a_{ij}x_j$ | $c_{ik} = \sum_j a_{ij}b_{jk}$ |
| 映射 | $T_A(\boldsymbol{x})$ | $T_A \circ T_B = T_{AB}$ |
