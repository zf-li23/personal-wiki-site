---
title: 内积与正交性
---

前三章只用到向量的线性运算：方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 有没有解、解集有多大，都由**秩**和四个基本子空间回答。但当 $\boldsymbol{b} \notin \mathcal{R}(A)$、方程组无解时，我们仍然希望找到"最接近"的 $\boldsymbol{x}$，这就需要度量长度与角度。本章在 $\mathbb{R}^n$ 上引入内积，由它定义长度、夹角与正交，再沿着一条"把问题化为正交的情形"的主线展开：标准正交基让坐标只需做内积；Gram–Schmidt 正交化把任意一组基化成标准正交基，写成矩阵形式就是 QR 分解；正交补与正交投影给出"最佳逼近"的几何刻画；最后用正规方程或 QR 分解求解最小二乘问题，并应用于数据拟合。

本章依赖第 2 章的 **LU 分解**和第 3 章的子空间、维数与秩；正交矩阵、QR 分解与正交投影是第 7 章实对称矩阵的谱分解与奇异值分解的基础。这里只讨论 $\mathbb{R}^n$ 上的标准内积，一般的内积空间、欧氏空间与酉空间见[第 12 章](/2.1.12)。最小二乘与正交投影矩阵也是统计学中线性回归的核心工具。

## 4.1. 内积、长度与夹角

**例 4.1.1（平面上的最佳逼近）** 考虑方程组 $\boldsymbol{a}x = \boldsymbol{b}$，其中 $\boldsymbol{a} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$，$\boldsymbol{b} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$，$x \in \mathbb{R}$。它显然无解。退而求其次，求 $\hat{x}$ 使 $\boldsymbol{b} - \hat{x}\boldsymbol{a}$ 的长度最小：

$$
\|\boldsymbol{b} - \hat{x}\boldsymbol{a}\| = \min_{x \in \mathbb{R}} \|\boldsymbol{b} - x\boldsymbol{a}\|, \qquad \|\boldsymbol{a}\| = \sqrt{a_1^2 + a_2^2} = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}.
$$

几何上，就是把 $\boldsymbol{b}$ 向直线 $\operatorname{span}(\boldsymbol{a}) = \{x\boldsymbol{a} \mid x \in \mathbb{R}\}$ 作垂线：做分解 $\boldsymbol{b} = \hat{x}\boldsymbol{a} + \boldsymbol{r}$，要求 $\boldsymbol{a}$ 与 $\boldsymbol{r}$ 垂直，即 $0 = \boldsymbol{a}^{\mathsf T}\boldsymbol{r} = \boldsymbol{a}^{\mathsf T}(\boldsymbol{b} - \hat{x}\boldsymbol{a})$，于是

$$
\hat{x} = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \frac{8}{5}, \qquad \boldsymbol{r} = \boldsymbol{b} - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a} = \frac{6}{5}\begin{bmatrix} -1 \\ 2 \end{bmatrix}, \qquad \|\boldsymbol{r}\| = \frac{6}{\sqrt{5}}.
$$

这个例子用到的"长度""垂直"都可以用 $\boldsymbol{a}^{\mathsf T}\boldsymbol{b}$ 表达，下面把它推广到 $\mathbb{R}^n$。

### 4.1.1. 内积与长度

**定义 4.1.1（内积）** 对 $\mathbb{R}^n$ 中的向量 $\boldsymbol{a} = [a_i]$，$\boldsymbol{b} = [b_i]$，定义二者的**内积**（也称标准内积、点积）为

$$
\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \sum_{i=1}^n a_i b_i \in \mathbb{R}.
$$

**性质 4.1.1** 内积满足：

1. 对称性：$\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \boldsymbol{b}^{\mathsf T}\boldsymbol{a}$；
2. 双线性：$\boldsymbol{a}^{\mathsf T}(k_1\boldsymbol{b}_1 + k_2\boldsymbol{b}_2) = k_1\boldsymbol{a}^{\mathsf T}\boldsymbol{b}_1 + k_2\boldsymbol{a}^{\mathsf T}\boldsymbol{b}_2$，$(k_1\boldsymbol{a}_1 + k_2\boldsymbol{a}_2)^{\mathsf T}\boldsymbol{b} = k_1\boldsymbol{a}_1^{\mathsf T}\boldsymbol{b} + k_2\boldsymbol{a}_2^{\mathsf T}\boldsymbol{b}$；
3. 正定性：$\boldsymbol{a}^{\mathsf T}\boldsymbol{a} \ge 0$，且 $\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 0$ 当且仅当 $\boldsymbol{a} = \boldsymbol{0}$。

这三条性质是后面一切结论的出发点；[第 12 章](/2.1.12)正是以它们为公理定义一般线性空间上的内积。

**定义 4.1.2（向量的长度）** 向量 $\boldsymbol{a} \in \mathbb{R}^n$ 的**长度**（Euclidean 范数）为

$$
\|\boldsymbol{a}\| = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}.
$$

长度为 $1$ 的向量称为单位向量；对非零向量 $\boldsymbol{a}$，$\boldsymbol{a}/\|\boldsymbol{a}\|$ 是单位向量，称为 $\boldsymbol{a}$ 的单位化；$\|\boldsymbol{a} - \boldsymbol{b}\|$ 称为 $\boldsymbol{a}$ 与 $\boldsymbol{b}$ 的距离。

**性质 4.1.2** 长度满足 $\|\boldsymbol{a}\| = 0 \iff \boldsymbol{a} = \boldsymbol{0}$，齐次性 $\|k\boldsymbol{a}\| = |k|\,\|\boldsymbol{a}\|$，以及极化恒等式

$$
\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \frac{1}{4}\left(\|\boldsymbol{a} + \boldsymbol{b}\|^2 - \|\boldsymbol{a} - \boldsymbol{b}\|^2\right).
$$

极化恒等式说明内积可以由长度完全确定，这将用于刻画正交矩阵（定理 4.3.2）。

### 4.1.2. Cauchy–Schwarz 不等式与夹角

**定理 4.1.1（Cauchy–Schwarz 不等式）** 对任意 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$，

$$
|\boldsymbol{a}^{\mathsf T}\boldsymbol{b}| \le \|\boldsymbol{a}\|\,\|\boldsymbol{b}\|,
$$

等号成立当且仅当 $\boldsymbol{a}, \boldsymbol{b}$ 共线。

**证明** $\boldsymbol{a} = \boldsymbol{0}$ 时显然。设 $\boldsymbol{a} \ne \boldsymbol{0}$，对任意 $x \in \mathbb{R}$，

$$
0 \le (\boldsymbol{b} - x\boldsymbol{a})^{\mathsf T}(\boldsymbol{b} - x\boldsymbol{a}) = (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})x^2 - 2(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})x + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} = (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})\left(x - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\right)^2 + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} - \frac{(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})^2}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}.
$$

取 $x = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$ 即得 $(\boldsymbol{a}^{\mathsf T}\boldsymbol{b})^2 \le (\boldsymbol{a}^{\mathsf T}\boldsymbol{a})(\boldsymbol{b}^{\mathsf T}\boldsymbol{b})$。等号成立当且仅当存在 $x$ 使 $\boldsymbol{b} - x\boldsymbol{a} = \boldsymbol{0}$，即 $\boldsymbol{a}, \boldsymbol{b}$ 共线。$\square$

**推论 4.1.1（三角不等式）** $\|\boldsymbol{a} + \boldsymbol{b}\| \le \|\boldsymbol{a}\| + \|\boldsymbol{b}\|$，即三角形两边之和不小于第三边。等号成立当且仅当 $\boldsymbol{a}, \boldsymbol{b}$ 中有零向量，或二者共线且同向。

**证明** $\|\boldsymbol{a} + \boldsymbol{b}\|^2 = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2 + 2\boldsymbol{a}^{\mathsf T}\boldsymbol{b} \le \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2 + 2\|\boldsymbol{a}\|\,\|\boldsymbol{b}\| = (\|\boldsymbol{a}\| + \|\boldsymbol{b}\|)^2$。等号要求 $\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \|\boldsymbol{a}\|\,\|\boldsymbol{b}\|$，由定理 4.1.1 即得等号条件。$\square$

由 Cauchy–Schwarz 不等式，对非零向量有 $|\boldsymbol{a}^{\mathsf T}\boldsymbol{b}|/(\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|) \le 1$，因此可以定义夹角。

**定义 4.1.3（夹角）** $\mathbb{R}^n$ 中两个非零向量 $\boldsymbol{a}, \boldsymbol{b}$ 的夹角定义为 $\arccos \dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\|\boldsymbol{a}\|\,\|\boldsymbol{b}\|} \in [0, \pi]$。

**定义 4.1.4（正交）** 对 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$，若 $\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = 0$，则称二者**正交**（垂直），记为 $\boldsymbol{a} \perp \boldsymbol{b}$。

零向量与任意向量都正交；非零向量 $\boldsymbol{a}, \boldsymbol{b}$ 正交当且仅当夹角为 $\pi/2$。

**定理 4.1.2（勾股定理）** 若 $\boldsymbol{a} \perp \boldsymbol{b}$，则 $\|\boldsymbol{a} \pm \boldsymbol{b}\|^2 = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2$。

**证明** $\|\boldsymbol{a} \pm \boldsymbol{b}\|^2 = \boldsymbol{a}^{\mathsf T}\boldsymbol{a} + \boldsymbol{b}^{\mathsf T}\boldsymbol{b} \pm 2\boldsymbol{a}^{\mathsf T}\boldsymbol{b} = \|\boldsymbol{a}\|^2 + \|\boldsymbol{b}\|^2$。$\square$

## 4.2. 标准正交基与 Gram–Schmidt 正交化

### 4.2.1. 向直线的正交投影

设 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^n$，$\boldsymbol{a} \ne \boldsymbol{0}$。与例 4.1.1 相同，做分解 $\boldsymbol{b} = \hat{x}\boldsymbol{a} + \boldsymbol{r}$ 且 $\boldsymbol{a} \perp \boldsymbol{r}$，得到

$$
\hat{x} = \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}, \qquad \boldsymbol{r} = \boldsymbol{b} - \frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}.
$$

向量 $\dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}$ 称为 $\boldsymbol{b}$ 向直线 $\operatorname{span}(\boldsymbol{a})$ 的正交投影，$\boldsymbol{r}$ 与 $\boldsymbol{a}$ 正交。4.4 节会把它推广到任意子空间上的正交投影。

**命题 4.2.1** 设 $\boldsymbol{a} \ne \boldsymbol{0}$，则 $\left\|\boldsymbol{b} - \dfrac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}\boldsymbol{a}\right\| = \min\limits_{x \in \mathbb{R}} \|\boldsymbol{b} - x\boldsymbol{a}\|$。

**证明** 由定理 4.1.1 证明中的配方式，$\|\boldsymbol{b} - x\boldsymbol{a}\|^2$ 是 $x$ 的二次函数，在 $x = \boldsymbol{a}^{\mathsf T}\boldsymbol{b}/\boldsymbol{a}^{\mathsf T}\boldsymbol{a}$ 处取最小值。$\square$

### 4.2.2. 正交向量组与标准正交基

**定义 4.2.1（正交向量组）** 设 $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_r$ 是 $\mathbb{R}^n$ 中的向量组。若这些向量都非零且两两正交，则称之为**正交向量组**；若正交向量组中的向量都是单位向量，则称之为**正交单位向量组**。

**命题 4.2.2** 正交向量组**线性无关**。

**证明** 设 $k_1\boldsymbol{a}_1 + \cdots + k_r\boldsymbol{a}_r = \boldsymbol{0}$。两边与 $\boldsymbol{a}_i$ 做内积，由两两正交得 $k_i\|\boldsymbol{a}_i\|^2 = 0$；而 $\boldsymbol{a}_i \ne \boldsymbol{0}$，故 $k_i = 0$（$i = 1, \cdots, r$）。$\square$

**定义 4.2.2（标准正交基）** 设 $M$ 是 $\mathbb{R}^n$ 的子空间。若 $M$ 的一组基是正交向量组，则称之为 $M$ 的一组**正交基**；若是正交单位向量组，则称之为 $M$ 的一组**标准正交基**。

**标准基** $\boldsymbol{e}_1, \cdots, \boldsymbol{e}_n$ 是 $\mathbb{R}^n$ 的一组标准正交基。由命题 4.2.2，$r$ 维子空间 $M$ 中任意 $r$ 个向量构成的正交向量组都是 $M$ 的正交基。标准正交基的好处是坐标只需做内积：一般的基下求坐标要解一个线性方程组，而在正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_n$ 下，把 $\boldsymbol{a} = \sum_j x_j\boldsymbol{q}_j$ 两边与 $\boldsymbol{q}_i$ 做内积就得到 $x_i$：

$$
\boldsymbol{a} = \frac{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_1}\boldsymbol{q}_1 + \frac{\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_2}\boldsymbol{q}_2 + \cdots + \frac{\boldsymbol{q}_n^{\mathsf T}\boldsymbol{a}}{\boldsymbol{q}_n^{\mathsf T}\boldsymbol{q}_n}\boldsymbol{q}_n,
$$

即 $\boldsymbol{a}$ 等于它向各个 $\operatorname{span}(\boldsymbol{q}_i)$ 的正交投影之和；对标准正交基，系数就是 $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}$。

**定理 4.2.1（标准正交基的存在定理）** $\mathbb{R}^n$ 的任意非零子空间 $M$ 都存在一组正交基，从而存在一组标准正交基。

**证明** 对 $\dim M$ 用数学归纳法。$\dim M = 1$ 时任一非零向量构成正交基。设结论对 $r$ 维子空间成立，考虑 $r+1$ 维子空间 $M$，取 $M$ 的一组基 $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_{r+1}$。由归纳假设，$N = \operatorname{span}(\boldsymbol{a}_1, \cdots, \boldsymbol{a}_r)$ 有正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$，于是 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r, \boldsymbol{a}_{r+1}$ 也是 $M$ 的基。令 $\boldsymbol{q}_{r+1} = \boldsymbol{a}_{r+1} + k_1\boldsymbol{q}_1 + \cdots + k_r\boldsymbol{q}_r$，要求它与 $\boldsymbol{q}_i$ 正交，两边与 $\boldsymbol{q}_i$ 做内积得 $0 = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_{r+1} + k_i\|\boldsymbol{q}_i\|^2$，故

$$
\boldsymbol{q}_{r+1} = \boldsymbol{a}_{r+1} - \frac{\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_{r+1}}{\|\boldsymbol{q}_1\|^2}\boldsymbol{q}_1 - \cdots - \frac{\boldsymbol{q}_r^{\mathsf T}\boldsymbol{a}_{r+1}}{\|\boldsymbol{q}_r\|^2}\boldsymbol{q}_r.
$$

由于 $\boldsymbol{a}_{r+1} \notin N$，$\boldsymbol{q}_{r+1} \ne \boldsymbol{0}$，于是 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_{r+1}$ 是 $M$ 的正交基。把每个向量单位化即得标准正交基。$\square$

**定理 4.2.2（标准正交基的扩充定理）** 设 $M \subseteq N$ 是 $\mathbb{R}^n$ 的两个子空间，则 $M$ 的任意一组标准正交基都可以扩充为 $N$ 的一组标准正交基。

**证明** 设 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$ 是 $M$ 的标准正交基。由第 3 章的基扩充定理，可以把它扩充为 $N$ 的一组基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r, \boldsymbol{a}_{r+1}, \cdots, \boldsymbol{a}_s$。对后面的向量依次重复定理 4.2.1 证明中的构造（前 $r$ 个向量已经两两正交，不会改变），再单位化，即得 $N$ 的一组包含 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$ 的标准正交基。$\square$

### 4.2.3. Gram–Schmidt 正交化

定理 4.2.1 的证明本身就是一个算法：从任意一组基出发，逐个减去在已得正交向量方向上的投影。

**算法 4.2.1（Gram–Schmidt 正交化）** 输入 $r$ 维子空间 $M \subseteq \mathbb{R}^n$ 的一组基 $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_r$，输出 $M$ 的一组标准正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$。

1. 正交化：依次计算
   $$
   \begin{aligned}
   \tilde{\boldsymbol{q}}_1 &= \boldsymbol{a}_1, \\
   \tilde{\boldsymbol{q}}_2 &= \boldsymbol{a}_2 - \frac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_2}{\|\tilde{\boldsymbol{q}}_1\|^2}\tilde{\boldsymbol{q}}_1, \\
   &\ \ \vdots \\
   \tilde{\boldsymbol{q}}_r &= \boldsymbol{a}_r - \frac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_1\|^2}\tilde{\boldsymbol{q}}_1 - \frac{\tilde{\boldsymbol{q}}_2^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_2\|^2}\tilde{\boldsymbol{q}}_2 - \cdots - \frac{\tilde{\boldsymbol{q}}_{r-1}^{\mathsf T}\boldsymbol{a}_r}{\|\tilde{\boldsymbol{q}}_{r-1}\|^2}\tilde{\boldsymbol{q}}_{r-1};
   \end{aligned}
   $$
2. 单位化：$\boldsymbol{q}_i = \tilde{\boldsymbol{q}}_i / \|\tilde{\boldsymbol{q}}_i\|$（$i = 1, \cdots, r$）。

第 $i$ 步把 $\boldsymbol{a}_i$ 减去它在 $\tilde{\boldsymbol{q}}_1, \cdots, \tilde{\boldsymbol{q}}_{i-1}$ 方向上的正交投影，留下与它们都正交的部分 $\tilde{\boldsymbol{q}}_i$。每一步中三个向量组

$$
\{\tilde{\boldsymbol{q}}_1, \cdots, \tilde{\boldsymbol{q}}_{i-1}, \tilde{\boldsymbol{q}}_i\}, \qquad \{\tilde{\boldsymbol{q}}_1, \cdots, \tilde{\boldsymbol{q}}_{i-1}, \boldsymbol{a}_i\}, \qquad \{\boldsymbol{a}_1, \cdots, \boldsymbol{a}_{i-1}, \boldsymbol{a}_i\}
$$

线性等价，因此对每个 $i$ 都有 $\operatorname{span}(\boldsymbol{q}_1, \cdots, \boldsymbol{q}_i) = \operatorname{span}(\boldsymbol{a}_1, \cdots, \boldsymbol{a}_i)$。这一"前 $i$ 个向量张成同一子空间"的性质，正是下一节 $R$ 为上三角矩阵的原因。

**例 4.2.1** 用 Gram–Schmidt 正交化把 $\mathbb{R}^3$ 的基 $\boldsymbol{a}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$，$\boldsymbol{a}_2 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$，$\boldsymbol{a}_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ 化为标准正交基。

$$
\tilde{\boldsymbol{q}}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad
\tilde{\boldsymbol{q}}_2 = \boldsymbol{a}_2 - \frac{2}{3}\tilde{\boldsymbol{q}}_1 = \frac{1}{3}\begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}, \quad
\tilde{\boldsymbol{q}}_3 = \boldsymbol{a}_3 - \frac{1}{3}\tilde{\boldsymbol{q}}_1 - \frac{1/3}{2/3}\tilde{\boldsymbol{q}}_2 = \frac{1}{2}\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}.
$$

单位化得 $\boldsymbol{q}_1 = \dfrac{1}{\sqrt{3}}\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$，$\boldsymbol{q}_2 = \dfrac{1}{\sqrt{6}}\begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}$，$\boldsymbol{q}_3 = \dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$。结果依赖于向量的顺序：按 $\boldsymbol{a}_3, \boldsymbol{a}_2, \boldsymbol{a}_1$ 的顺序做正交化，得到的是标准基 $\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3$。

## 4.3. 正交矩阵与 QR 分解

### 4.3.1. 正交矩阵

设 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_n$ 是 $\mathbb{R}^n$ 的标准正交基，$Q = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$，则 $Q^{\mathsf T}Q$ 的 $(i, j)$ 元是 $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{q}_j$，即 $Q^{\mathsf T}Q = I_n$。

**定义 4.3.1（正交矩阵）** 满足 $Q^{\mathsf T}Q = I_n$ 的 $n$ 阶方阵 $Q$ 称为 $n$ 阶**正交矩阵**。

**定理 4.3.1** 对 $n$ 阶方阵 $Q$，以下叙述等价：

1. $Q$ 是正交矩阵，即 $Q^{\mathsf T}Q = I_n$；
2. $Q$ 可逆，且 $Q^{-1} = Q^{\mathsf T}$；
3. $QQ^{\mathsf T} = I_n$；
4. $Q^{\mathsf T}$ 是正交矩阵；
5. $Q$ 可逆，且 $Q^{-1}$ 是正交矩阵；
6. $Q$ 的列向量组构成 $\mathbb{R}^n$ 的一组标准正交基；
7. $Q$ 的行向量组（转置后）构成 $\mathbb{R}^n$ 的一组标准正交基。

**证明** 方阵满足 $BA = I_n$ 即可推出 $A$ 是**可逆矩阵**且 $A^{-1} = B$（第 2 章），故 1 ⇔ 2 ⇔ 3；3 就是 4 的定义，2 与 4 合起来即 5；1 ⇔ 6 见定义前的计算，3 ⇔ 7 同理。$\square$

由定理 4.3.1，求正交矩阵的逆只需转置，这是正交矩阵在计算上最重要的优点。两个 $n$ 阶正交矩阵的乘积仍是正交矩阵：$(Q_1Q_2)^{\mathsf T}(Q_1Q_2) = Q_2^{\mathsf T}Q_1^{\mathsf T}Q_1Q_2 = I_n$。

**定理 4.3.2** 对 $n$ 阶方阵 $Q$，以下叙述等价：

1. $Q$ 是正交矩阵；
2. $Q$ 保距：对任意 $\boldsymbol{x} \in \mathbb{R}^n$，$\|Q\boldsymbol{x}\| = \|\boldsymbol{x}\|$；
3. $Q$ 保内积：对任意 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$，$(Q\boldsymbol{x})^{\mathsf T}(Q\boldsymbol{y}) = \boldsymbol{x}^{\mathsf T}\boldsymbol{y}$。

**证明** 用轮转证法。1 ⇒ 2：$\|Q\boldsymbol{x}\|^2 = \boldsymbol{x}^{\mathsf T}Q^{\mathsf T}Q\boldsymbol{x} = \|\boldsymbol{x}\|^2$。2 ⇒ 3：由极化恒等式（性质 4.1.2），

$$
\boldsymbol{x}^{\mathsf T}\boldsymbol{y} = \frac{1}{4}\left(\|\boldsymbol{x} + \boldsymbol{y}\|^2 - \|\boldsymbol{x} - \boldsymbol{y}\|^2\right) = \frac{1}{4}\left(\|Q\boldsymbol{x} + Q\boldsymbol{y}\|^2 - \|Q\boldsymbol{x} - Q\boldsymbol{y}\|^2\right) = (Q\boldsymbol{x})^{\mathsf T}(Q\boldsymbol{y}).
$$

3 ⇒ 1：$Q^{\mathsf T}Q$ 的 $(i, j)$ 元为 $\boldsymbol{e}_i^{\mathsf T}Q^{\mathsf T}Q\boldsymbol{e}_j = (Q\boldsymbol{e}_i)^{\mathsf T}(Q\boldsymbol{e}_j) = \boldsymbol{e}_i^{\mathsf T}\boldsymbol{e}_j$，故 $Q^{\mathsf T}Q = I_n$。$\square$

保距与保内积说明正交矩阵也保持夹角，几何上它对应的**线性变换**是"刚体运动"（旋转与反射的复合）。反过来，保角的变换不一定是正交矩阵，例如 $2Q$ 保角但不保距。

**例 4.3.1（二阶正交矩阵）** 设 $Q = [\boldsymbol{q}_1\ \boldsymbol{q}_2]$ 是二阶正交矩阵，则 $\boldsymbol{q}_1, \boldsymbol{q}_2$ 是 $\mathbb{R}^2$ 的标准正交基。设 $\boldsymbol{q}_1 = \begin{bmatrix} \cos\theta \\ \sin\theta \end{bmatrix}$，$\boldsymbol{q}_2 = \begin{bmatrix} \cos\varphi \\ \sin\varphi \end{bmatrix}$，由 $\boldsymbol{q}_1 \perp \boldsymbol{q}_2$ 得 $\cos(\theta - \varphi) = 0$，即 $\theta - \varphi = (k + \frac{1}{2})\pi$，$k \in \mathbb{Z}$。按 $k$ 的奇偶，二阶正交矩阵只有两种形式：

$$
R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \qquad
H_{\theta/2} = \begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}.
$$

$R_\theta$ 是转角为 $\theta$ 的旋转，$H_{\theta/2}$ 是关于过原点、与 $x_1$ 轴夹角为 $\theta/2$ 的直线 $\ell_{\theta/2}$ 的反射。二者满足

$$
R_{\theta - \varphi} = H_{\theta/2}H_{\varphi/2}, \qquad H_{(\theta + \varphi)/2} = R_\theta H_{\varphi/2} = H_{\varphi/2}R_{-\theta},
$$

因此任意二阶正交矩阵都能写成至多两个反射的乘积。设 $\boldsymbol{v} = \begin{bmatrix} -\sin(\theta/2) \\ \cos(\theta/2) \end{bmatrix}$ 是 $\ell_{\theta/2}$ 的单位法向量，$\boldsymbol{w}$ 向 $\operatorname{span}(\boldsymbol{v})$ 的投影为 $(\boldsymbol{v}^{\mathsf T}\boldsymbol{w})\boldsymbol{v}$，把它减去两次就得到反射像：$H_{\theta/2}\boldsymbol{w} = \boldsymbol{w} - 2(\boldsymbol{v}^{\mathsf T}\boldsymbol{w})\boldsymbol{v} = (I_2 - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T})\boldsymbol{w}$，即 $H_{\theta/2} = I_2 - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$。

### 4.3.2. Givens 变换与 Householder 变换

平面上的旋转与反射都可以推广到 $\mathbb{R}^n$。

**定义 4.3.2（Givens 变换）** 在 $\boldsymbol{e}_i$–$\boldsymbol{e}_j$ 平面上转角为 $\theta$、其余坐标不变的旋转称为 **Givens 变换**，其表示矩阵 $G_{\theta;i,j}$ 与 $I_n$ 只在第 $i, j$ 行与第 $i, j$ 列的交叉处不同：

$$
(G_{\theta;i,j})_{ii} = (G_{\theta;i,j})_{jj} = \cos\theta, \qquad (G_{\theta;i,j})_{ij} = -\sin\theta, \qquad (G_{\theta;i,j})_{ji} = \sin\theta.
$$

即 $\boldsymbol{x} = G_{\theta;i,j}\boldsymbol{w}$ 满足 $\begin{bmatrix} x_i \\ x_j \end{bmatrix} = R_\theta\begin{bmatrix} w_i \\ w_j \end{bmatrix}$，且 $x_k = w_k$（$k \ne i, j$）。$G_{\theta;i,j}$ 保距，是正交矩阵。适当选取 $\theta$ 可以把 $\boldsymbol{w}$ 的第 $j$ 个分量变为零，因此一系列 Givens 变换可以逐个消去矩阵的下三角元素。

**定义 4.3.3（Householder 变换）** 设 $\boldsymbol{v} \in \mathbb{R}^n$ 是单位向量，$\mathcal{N}(\boldsymbol{v}^{\mathsf T})$ 是以 $\boldsymbol{v}$ 为法向量的超平面。关于这个超平面的反射

$$
H_{\boldsymbol{v}} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}
$$

称为 **Householder 变换**（镜面反射）。

把 $\boldsymbol{w}$ 正交分解为 $\boldsymbol{w} = (I_n - \boldsymbol{v}\boldsymbol{v}^{\mathsf T})\boldsymbol{w} + \boldsymbol{v}\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$，前者在超平面 $\mathcal{N}(\boldsymbol{v}^{\mathsf T})$ 内，后者是 $\boldsymbol{w}$ 向 $\operatorname{span}(\boldsymbol{v})$ 的投影；反射保留前者、反转后者，即得 $H_{\boldsymbol{v}}\boldsymbol{w}$。$H_{\boldsymbol{v}}$ 是**对称矩阵**，且 $H_{\boldsymbol{v}}^{\mathsf T}H_{\boldsymbol{v}} = H_{\boldsymbol{v}}^2 = I_n - 4\boldsymbol{v}\boldsymbol{v}^{\mathsf T} + 4\boldsymbol{v}(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})\boldsymbol{v}^{\mathsf T} = I_n$，所以是正交矩阵。

**命题 4.3.1** 设 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ 等长且 $\boldsymbol{x} \ne \boldsymbol{y}$，令 $\boldsymbol{v} = \dfrac{\boldsymbol{y} - \boldsymbol{x}}{\|\boldsymbol{y} - \boldsymbol{x}\|}$，则 $H_{\boldsymbol{v}}\boldsymbol{x} = \boldsymbol{y}$。

**证明** 记 $\boldsymbol{w} = \boldsymbol{y} - \boldsymbol{x}$。由 $\|\boldsymbol{x}\| = \|\boldsymbol{y}\|$，$\|\boldsymbol{w}\|^2 = 2\|\boldsymbol{x}\|^2 - 2\boldsymbol{y}^{\mathsf T}\boldsymbol{x} = -2\boldsymbol{w}^{\mathsf T}\boldsymbol{x}$。于是

$$
H_{\boldsymbol{v}}\boldsymbol{x} = \boldsymbol{x} - \frac{2(\boldsymbol{w}^{\mathsf T}\boldsymbol{x})}{\|\boldsymbol{w}\|^2}\boldsymbol{w} = \boldsymbol{x} + \boldsymbol{w} = \boldsymbol{y}. \qquad \square
$$

特别地，取 $\boldsymbol{y} = \mp\|\boldsymbol{x}\|\boldsymbol{e}_1$，一次 Householder 变换就能把 $\boldsymbol{x}$ 除第一个分量以外的分量全部消为零。这与 Gauss 消元用倍加变换消元的思路相同，只是所用的变换换成了正交矩阵。

### 4.3.3. QR 分解

用矩阵乘法描述 Gauss 消元得到 **LU 分解**；类似地，用矩阵乘法描述 Gram–Schmidt 正交化，得到另一种矩阵分解。设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ 可逆，对它的列向量组做算法 4.2.1，得到正交基 $\tilde{\boldsymbol{q}}_1, \cdots, \tilde{\boldsymbol{q}}_n$ 与标准正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_n$。由于 $\boldsymbol{a}_i$ 可以由 $\tilde{\boldsymbol{q}}_1, \cdots, \tilde{\boldsymbol{q}}_i$ 线性表示，令 $\tilde{Q} = [\tilde{\boldsymbol{q}}_1\ \cdots\ \tilde{\boldsymbol{q}}_n]$，$Q = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$，有

$$
A = \tilde{Q}\tilde{R}, \qquad
\tilde{R} = \begin{bmatrix}
1 & \dfrac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_2}{\|\tilde{\boldsymbol{q}}_1\|^2} & \cdots & \dfrac{\tilde{\boldsymbol{q}}_1^{\mathsf T}\boldsymbol{a}_n}{\|\tilde{\boldsymbol{q}}_1\|^2} \\
 & 1 & \cdots & \dfrac{\tilde{\boldsymbol{q}}_2^{\mathsf T}\boldsymbol{a}_n}{\|\tilde{\boldsymbol{q}}_2\|^2} \\
 & & \ddots & \vdots \\
 & & & 1
\end{bmatrix}.
$$

单位化写成 $\tilde{Q} = Q\operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)$，于是 $A = Q\operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)\tilde{R} = QR$，其中 $Q$ 是正交矩阵，$R = \operatorname{diag}(\|\tilde{\boldsymbol{q}}_i\|)\tilde{R}$ 是对角元都为正数的上三角矩阵，$R$ 的 $(i, j)$ 元（$i < j$）为 $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$，对角元为 $\|\tilde{\boldsymbol{q}}_i\|$。

**定理 4.3.3（可逆矩阵的 QR 分解）** 设 $A$ 是 $n$ 阶可逆矩阵，则存在唯一的分解 $A = QR$，其中 $Q$ 是正交矩阵，$R$ 是对角元都为正数的上三角矩阵。

**证明** 存在性已由上面的构造给出。唯一性：设 $A = Q_1R_1 = Q_2R_2$，则 $U = Q_2^{-1}Q_1 = R_2R_1^{-1}$ 既是正交矩阵，又是对角元为正数的上三角矩阵。$U^{\mathsf T} = U^{-1}$ 一个是下三角矩阵、一个是上三角矩阵，故 $U$ 是对角矩阵；由 $U^{\mathsf T}U = I_n$ 与对角元为正得 $U = I_n$，即 $Q_1 = Q_2$，$R_1 = R_2$。$\square$

为把 QR 分解推广到 $m \times n$ 矩阵，引入：

**定义 4.3.4（列正交矩阵）** 满足 $Q^{\mathsf T}Q = I_n$ 的 $m \times n$ 矩阵 $Q$ 称为**列正交矩阵**。

$Q$ 是列正交矩阵等价于其列向量组是 $\mathbb{R}^m$ 中的正交单位向量组。列正交矩阵**列满秩**，因此 $m \ge n$。

**定理 4.3.4（QR 分解）** 设 $A$ 是 $m \times n$ 矩阵，$m \ge n$，则：

1. 存在 $m \times n$ 列正交矩阵 $Q_1$ 和对角元非负的 $n$ 阶上三角矩阵 $R_1$，使 $A = Q_1R_1$；
2. 进一步，存在 $m$ 阶正交矩阵 $Q = [Q_1\ Q_2]$（其列向量组由 $Q_1$ 的列向量组扩充而成）和 $m \times n$ 矩阵 $R = \begin{bmatrix} R_1 \\ O \end{bmatrix}$，使 $A = QR$。

$A = QR$ 称为 $A$ 的 **QR 分解**，$A = Q_1R_1$ 称为 $A$ 的简化 QR 分解。

**证明** 对 $n$ 用数学归纳法。$n = 1$ 时，若 $\boldsymbol{a}_1 \ne \boldsymbol{0}$，取 $Q_1 = \boldsymbol{a}_1/\|\boldsymbol{a}_1\|$，$R_1 = \|\boldsymbol{a}_1\|$；若 $\boldsymbol{a}_1 = \boldsymbol{0}$，任取单位向量作 $Q_1$，$R_1 = 0$。设结论对 $m \times (n-1)$ 矩阵成立，记 $A = [A_0\ \boldsymbol{a}_n]$，$A_0 = Q_0R_0$。

- 若 $\boldsymbol{a}_n \notin \mathcal{R}(Q_0)$，由 Gram–Schmidt 正交化，存在 $\boldsymbol{r}_n$ 使 $\tilde{\boldsymbol{q}}_n = \boldsymbol{a}_n - Q_0\boldsymbol{r}_n \ne \boldsymbol{0}$ 与 $Q_0$ 的各列正交，令 $\boldsymbol{q}_n = \tilde{\boldsymbol{q}}_n/\|\tilde{\boldsymbol{q}}_n\|$；
- 若 $\boldsymbol{a}_n \in \mathcal{R}(Q_0)$，则 $\boldsymbol{a}_n = Q_0\boldsymbol{r}_n$，任取与 $Q_0$ 各列正交的单位向量 $\boldsymbol{q}_n$，并记 $\|\tilde{\boldsymbol{q}}_n\| = 0$。

两种情形都有

$$
A = [Q_0R_0\ \ Q_0\boldsymbol{r}_n + \|\tilde{\boldsymbol{q}}_n\|\boldsymbol{q}_n] = [Q_0\ \boldsymbol{q}_n]\begin{bmatrix} R_0 & \boldsymbol{r}_n \\ \boldsymbol{0}^{\mathsf T} & \|\tilde{\boldsymbol{q}}_n\| \end{bmatrix} = Q_1R_1.
$$

再由定理 4.2.2 把 $Q_1$ 的列扩充为 $\mathbb{R}^m$ 的标准正交基，得 $Q = [Q_1\ Q_2]$，且 $A = Q_1R_1 = [Q_1\ Q_2]\begin{bmatrix} R_1 \\ O \end{bmatrix}$。$\square$

若 $A$ 列满秩，直接对 $A$ 的列向量组做 Gram–Schmidt 正交化即得 $Q_1, R_1$，且 $R_1$ 的对角元都是正数（可逆），此时简化 QR 分解唯一（证明同定理 4.3.3）。

**例 4.3.2** 求 $A = [\boldsymbol{a}_1\ \boldsymbol{a}_2\ \boldsymbol{a}_3] = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ 的 QR 分解。

由例 4.2.1，$A = \tilde{Q}\tilde{R}$，其中

$$
\tilde{Q} = \begin{bmatrix} 1 & \frac{1}{3} & \frac{1}{2} \\ 1 & \frac{1}{3} & -\frac{1}{2} \\ 1 & -\frac{2}{3} & 0 \end{bmatrix}, \quad
\tilde{R} = \begin{bmatrix} 1 & \frac{2}{3} & \frac{1}{3} \\ 0 & 1 & \frac{1}{2} \\ 0 & 0 & 1 \end{bmatrix}, \quad
\|\tilde{\boldsymbol{q}}_1\| = \sqrt{3},\ \|\tilde{\boldsymbol{q}}_2\| = \frac{\sqrt{6}}{3},\ \|\tilde{\boldsymbol{q}}_3\| = \frac{\sqrt{2}}{2}.
$$

于是 $A = QR$，

$$
Q = \begin{bmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} & 0 \end{bmatrix}, \qquad
R = \begin{bmatrix} \sqrt{3} & \frac{2}{\sqrt{3}} & \frac{1}{\sqrt{3}} \\ 0 & \frac{\sqrt{6}}{3} & \frac{1}{\sqrt{6}} \\ 0 & 0 & \frac{1}{\sqrt{2}} \end{bmatrix}.
$$

### 4.3.4. QR 分解的计算

**算法 4.3.1（Gram–Schmidt QR）** 输入列满秩的 $m \times n$ 矩阵 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，输出简化 QR 分解 $A = Q_1R_1$。对 $j = 1, \cdots, n$：

1. 计算 $r_{ij} = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$（$i = 1, \cdots, j-1$）；
2. 计算 $\tilde{\boldsymbol{q}}_j = \boldsymbol{a}_j - \sum_{i<j} r_{ij}\boldsymbol{q}_i$，$r_{jj} = \|\tilde{\boldsymbol{q}}_j\|$，$\boldsymbol{q}_j = \tilde{\boldsymbol{q}}_j / r_{jj}$。

改进的（modified）Gram–Schmidt 算法在数学上与之等价，只是把第 1 步中的 $\boldsymbol{a}_j$ 换成"已经减去前面投影的当前向量"：每得到一个 $\boldsymbol{q}_i$，就立即从所有后续向量中减去它的分量。总运算量约为 $2mn^2$ 次浮点运算。

**算法 4.3.2（Householder QR）** 输入 $m \times n$ 矩阵 $A$（$m \ge n$）。对 $j = 1, \cdots, n$：取当前矩阵第 $j$ 列中第 $j$ 到第 $m$ 个分量组成的向量 $\boldsymbol{x}$，按命题 4.3.1 构造 Householder 变换把 $\boldsymbol{x}$ 变成 $-\operatorname{sign}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1$（选这个符号是为了避免 $\boldsymbol{y} - \boldsymbol{x}$ 相减时的抵消），作用在当前矩阵的第 $j$ 到第 $m$ 行上。$n$ 步之后得到上三角的 $R$，而 $H_n\cdots H_1A = R$，即 $A = QR$，$Q = H_1H_2\cdots H_n$。

三种算法在精确算术下给出同一个分解，但在浮点运算中差别很大。下图对条件数 $\kappa(A)$（最大与最小奇异值之比，见[第 7 章](/2.1.7)）不同的 $60 \times 30$ 矩阵计算 $\|I - Q^{\mathsf T}Q\|_2$，即计算出的 $Q$ 偏离列正交的程度：经典 Gram–Schmidt 的误差约按 $\varepsilon\kappa(A)^2$ 增长（$\varepsilon \approx 10^{-16}$ 是双精度的机器精度），$\kappa(A) \approx 10^8$ 时已完全失去正交性；改进的 Gram–Schmidt 约按 $\varepsilon\kappa(A)$ 增长；Householder 方法始终保持在机器精度。这正是数值软件（如 LAPACK、`numpy.linalg.qr`）采用 Householder 变换的原因。

![三种 QR 算法的正交性损失随条件数的变化：经典 Gram–Schmidt 最差，改进的 Gram–Schmidt 居中，Householder 始终在机器精度](./plots/qr-orthogonality-loss.py)

## 4.4. 正交补与正交投影

4.2 节把向量投影到一条直线上；现在把它推广到任意子空间，从而回答本章开头的问题：$\boldsymbol{b} \notin \mathcal{R}(A)$ 时，$\mathcal{R}(A)$ 中离 $\boldsymbol{b}$ 最近的向量是什么。

### 4.4.1. 子空间的正交与正交补

若 $\boldsymbol{r}$ 与 $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_s$ 都正交，则由双线性，$\boldsymbol{r}$ 与 $\operatorname{span}(\boldsymbol{a}_1, \cdots, \boldsymbol{a}_s)$ 中任意向量都正交。例如齐次线性方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 的每个解都与 $A$ 的每个行向量正交，因此**零空间** $\mathcal{N}(A)$ 中的向量与**行空间** $\mathcal{R}(A^{\mathsf T})$ 中的向量都正交。

**定义 4.4.1（子空间正交）** 设 $M, N$ 是 $\mathbb{R}^n$ 的子空间。若 $M$ 中任意向量与 $N$ 中任意向量都正交，则称 $M$ 与 $N$ 正交，记为 $M \perp N$。若 $\operatorname{span}(\boldsymbol{a}) \perp M$，则称向量 $\boldsymbol{a}$ 与 $M$ 正交，记为 $\boldsymbol{a} \perp M$。

**定义 4.4.2（正交补）** 对 $\mathbb{R}^n$ 的子空间 $M$，集合 $M^\perp = \{\boldsymbol{a} \in \mathbb{R}^n \mid \boldsymbol{a} \perp M\}$ 称为 $M$ 的**正交补**。

由定义，若 $M \perp N$，则 $M \subseteq N^\perp$，$N \subseteq M^\perp$；若 $M \subseteq N$，则 $N^\perp \subseteq M^\perp$。$M^\perp$ 是子空间：$\boldsymbol{0} \in M^\perp$；若 $\boldsymbol{a}_1, \boldsymbol{a}_2 \in M^\perp$，则对任意 $\boldsymbol{b} \in M$ 有 $(k_1\boldsymbol{a}_1 + k_2\boldsymbol{a}_2)^{\mathsf T}\boldsymbol{b} = k_1\boldsymbol{a}_1^{\mathsf T}\boldsymbol{b} + k_2\boldsymbol{a}_2^{\mathsf T}\boldsymbol{b} = 0$。

**定理 4.4.1** 对 $\mathbb{R}^n$ 的子空间 $M$，有：

1. $M \cap M^\perp = \{\boldsymbol{0}\}$；
2. $\dim M^\perp = n - \dim M$；
3. $(M^\perp)^\perp = M$；
4. 对任意 $\boldsymbol{a} \in \mathbb{R}^n$，存在唯一的分解 $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2$，使 $\boldsymbol{a}_1 \in M$，$\boldsymbol{a}_2 \in M^\perp$。

**证明** 1. 若 $\boldsymbol{a} \in M \cap M^\perp$，则 $\boldsymbol{a} \perp \boldsymbol{a}$，$\boldsymbol{a}^{\mathsf T}\boldsymbol{a} = 0$，故 $\boldsymbol{a} = \boldsymbol{0}$。

2. 取 $M$ 的标准正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$，扩充为 $\mathbb{R}^n$ 的标准正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_n$（定理 4.2.2），则 $\operatorname{span}(\boldsymbol{q}_{r+1}, \cdots, \boldsymbol{q}_n) \subseteq M^\perp$。反之，对 $\boldsymbol{a} \in M^\perp$，$\boldsymbol{a} = \sum_{i=1}^n (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i = \sum_{i=r+1}^n (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i$。故 $M^\perp = \operatorname{span}(\boldsymbol{q}_{r+1}, \cdots, \boldsymbol{q}_n)$，$\dim M^\perp = n - r$。

3. $M \subseteq (M^\perp)^\perp$，且由 2，$\dim (M^\perp)^\perp = n - \dim M^\perp = \dim M$，故二者相等。

4. 存在性：取 $\boldsymbol{a}_1 = \sum_{i=1}^r (\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_i \in M$，$\boldsymbol{a}_2 = \boldsymbol{a} - \boldsymbol{a}_1$，则 $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_2 = 0$（$i \le r$），即 $\boldsymbol{a}_2 \in M^\perp$。唯一性：若 $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2 = \boldsymbol{a}_1' + \boldsymbol{a}_2'$，则 $\boldsymbol{a}_1 - \boldsymbol{a}_1' = \boldsymbol{a}_2' - \boldsymbol{a}_2 \in M \cap M^\perp = \{\boldsymbol{0}\}$。$\square$

### 4.4.2. 四个基本子空间的正交关系

**定理 4.4.2** 设 $A$ 是 $m \times n$ 矩阵，则：

1. $\mathcal{R}(A^{\mathsf T})^\perp = \mathcal{N}(A)$，$\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$；
2. $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$，$\mathcal{R}(A^{\mathsf T}A) = \mathcal{R}(A^{\mathsf T})$；$\mathcal{N}(AA^{\mathsf T}) = \mathcal{N}(A^{\mathsf T})$，$\mathcal{R}(AA^{\mathsf T}) = \mathcal{R}(A)$。

**证明** 1. $\boldsymbol{x} \in \mathcal{N}(A)$ 当且仅当 $\boldsymbol{x}$ 与 $A$ 的每一行正交，当且仅当 $\boldsymbol{x} \perp \mathcal{R}(A^{\mathsf T})$。对 $A^{\mathsf T}$ 应用同一结论得第二式。

2. 显然 $\mathcal{N}(A) \subseteq \mathcal{N}(A^{\mathsf T}A)$。反之，若 $A^{\mathsf T}A\boldsymbol{x} = \boldsymbol{0}$，则 $\|A\boldsymbol{x}\|^2 = \boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{x} = 0$，故 $A\boldsymbol{x} = \boldsymbol{0}$。于是 $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$。又 $\mathcal{R}(A^{\mathsf T}A) \subseteq \mathcal{R}(A^{\mathsf T})$，而由**秩–零化度定理**，$\operatorname{rank}(A^{\mathsf T}A) = n - \dim\mathcal{N}(A^{\mathsf T}A) = n - \dim\mathcal{N}(A) = \operatorname{rank}A = \operatorname{rank}A^{\mathsf T}$，故 $\mathcal{R}(A^{\mathsf T}A) = \mathcal{R}(A^{\mathsf T})$。把 $A$ 换成 $A^{\mathsf T}$ 得其余两式。$\square$

结合第 3 章的维数公式，四个基本子空间两两配成正交补（设 $\operatorname{rank}A = r$）：

| 子空间 | 所在空间 | 维数 | 正交补 |
|---|---|---|---|
| **列空间** $\mathcal{R}(A)$ | $\mathbb{R}^m$ | $r$ | $\mathcal{N}(A^{\mathsf T})$ |
| **左零空间** $\mathcal{N}(A^{\mathsf T})$ | $\mathbb{R}^m$ | $m - r$ | $\mathcal{R}(A)$ |
| 行空间 $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^n$ | $r$ | $\mathcal{N}(A)$ |
| 零空间 $\mathcal{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | $\mathcal{R}(A^{\mathsf T})$ |

由此，$A\boldsymbol{x} = \boldsymbol{b}$ 有解当且仅当 $\boldsymbol{b} \in \mathcal{R}(A) = \mathcal{N}(A^{\mathsf T})^\perp$，即 $\boldsymbol{b}$ 与 $A^{\mathsf T}\boldsymbol{y} = \boldsymbol{0}$ 的每个解都正交。

### 4.4.3. 子空间上的正交投影

设 $M$ 是 $\mathbb{R}^n$ 的子空间。由定理 4.4.1，每个 $\boldsymbol{a} \in \mathbb{R}^n$ 唯一地分解为 $\boldsymbol{a} = \boldsymbol{a}_1 + \boldsymbol{a}_2$，$\boldsymbol{a}_1 \in M$，$\boldsymbol{a}_2 \in M^\perp$。由分解的唯一性，$\boldsymbol{a} + \boldsymbol{b}$ 的分解就是两个分解之和，$k\boldsymbol{a}$ 的分解就是 $\boldsymbol{a}$ 的分解乘以 $k$，因此 $\boldsymbol{a} \mapsto \boldsymbol{a}_1$ 是一个线性变换。取 $M$ 的标准正交基 $\boldsymbol{q}_1, \cdots, \boldsymbol{q}_r$，令 $Q_r = [\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_r]$，则

$$
\boldsymbol{a}_1 = (\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_1 + \cdots + (\boldsymbol{q}_r^{\mathsf T}\boldsymbol{a})\boldsymbol{q}_r = (\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T} + \cdots + \boldsymbol{q}_r\boldsymbol{q}_r^{\mathsf T})\boldsymbol{a} = Q_rQ_r^{\mathsf T}\boldsymbol{a}.
$$

**定义 4.4.3（正交投影）** 线性变换 $P_M: \boldsymbol{a} \mapsto \boldsymbol{a}_1$ 称为子空间 $M$ 上的**正交投影**（变换），$\boldsymbol{a}_1 = P_M(\boldsymbol{a})$ 称为向量 $\boldsymbol{a}$ 在 $M$ 上的正交投影。它的表示矩阵是 $P_M = Q_rQ_r^{\mathsf T}$，其中 $Q_r$ 的列向量组是 $M$ 的任意一组标准正交基。

$P_M$ 由 $M$ 唯一确定，与标准正交基的选取无关（因为分解是唯一的）。由定义：

- $I_n = P_M + P_{M^\perp}$，即 $\boldsymbol{a} = P_M(\boldsymbol{a}) + P_{M^\perp}(\boldsymbol{a})$；
- $\boldsymbol{a} \in M$ 当且仅当 $P_M(\boldsymbol{a}) = \boldsymbol{a}$；$\boldsymbol{a} \in M^\perp$ 当且仅当 $P_M(\boldsymbol{a}) = \boldsymbol{0}$。

**定理 4.4.3（最佳逼近）** 设 $\boldsymbol{a}_1 = P_M(\boldsymbol{a})$，则 $\|\boldsymbol{a} - \boldsymbol{a}_1\| = \min\limits_{\boldsymbol{x} \in M} \|\boldsymbol{a} - \boldsymbol{x}\|$，且最小值只在 $\boldsymbol{x} = \boldsymbol{a}_1$ 处取到。

**证明** 对任意 $\boldsymbol{x} \in M$，$\boldsymbol{a} - \boldsymbol{x} = (\boldsymbol{a} - \boldsymbol{a}_1) + (\boldsymbol{a}_1 - \boldsymbol{x})$，其中 $\boldsymbol{a} - \boldsymbol{a}_1 \in M^\perp$，$\boldsymbol{a}_1 - \boldsymbol{x} \in M$。由勾股定理，$\|\boldsymbol{a} - \boldsymbol{x}\|^2 = \|\boldsymbol{a} - \boldsymbol{a}_1\|^2 + \|\boldsymbol{a}_1 - \boldsymbol{x}\|^2 \ge \|\boldsymbol{a} - \boldsymbol{a}_1\|^2$，等号当且仅当 $\boldsymbol{x} = \boldsymbol{a}_1$。$\square$

### 4.4.4. 正交投影矩阵

最常见的情形是投影到矩阵的列空间上：$M = \mathcal{R}(A)$，$M^\perp = \mathcal{N}(A^{\mathsf T})$。

**定义 4.4.4（正交投影矩阵）** 列空间 $\mathcal{R}(A)$ 上的正交投影的表示矩阵 $P_{\mathcal{R}(A)}$ 称为关于 $A$ 的**正交投影矩阵**，简记为 $P_A$。

于是 $I - P_A = P_{\mathcal{N}(A^{\mathsf T})}$；$A$ 可逆时 $\mathcal{R}(A) = \mathbb{R}^n$，$P_A = I_n$。若 $Q_r$ 的列是 $\mathcal{R}(A)$ 的标准正交基，则 $P_A = Q_rQ_r^{\mathsf T}$，且 $\mathcal{R}(P_A) = \mathcal{R}(Q_r) = \mathcal{R}(A)$，所以 $P_A$ 也是关于它自身的正交投影矩阵。

**定理 4.4.4** $n$ 阶方阵 $P$ 是正交投影矩阵，当且仅当 $P^2 = P^{\mathsf T} = P$。

**证明** 必要性：$P = Q_rQ_r^{\mathsf T}$，$Q_r$ 列正交，则 $P^{\mathsf T} = P$，$P^2 = Q_r(Q_r^{\mathsf T}Q_r)Q_r^{\mathsf T} = P$。

充分性：设 $P^2 = P^{\mathsf T} = P$，证明 $P$ 是关于自身的正交投影矩阵。对任意 $\boldsymbol{x}$，$\boldsymbol{x} = P\boldsymbol{x} + (I_n - P)\boldsymbol{x}$，其中 $P\boldsymbol{x} \in \mathcal{R}(P)$，而 $P^{\mathsf T}(I_n - P)\boldsymbol{x} = (P - P^2)\boldsymbol{x} = \boldsymbol{0}$，即 $(I_n - P)\boldsymbol{x} \in \mathcal{N}(P^{\mathsf T}) = \mathcal{R}(P)^\perp$。由分解的唯一性，这就是 $\mathcal{R}(P)$ 上正交投影对应的分解，故 $P = P_{\mathcal{R}(P)}$。$\square$

条件 $P^2 = P$ 表示"投影两次等于投影一次"，$P^{\mathsf T} = P$ 表示"沿垂直方向投影"；只满足前者的矩阵是斜投影。

## 4.5. 最小二乘问题

### 4.5.1. 最小二乘解与正规方程

**定义 4.5.1（最小二乘问题）** 设 $A$ 是 $m \times n$ 矩阵，$\boldsymbol{b} \in \mathbb{R}^m$。称 $\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x}$ 为残量。求 $\boldsymbol{x}$ 使残量的长度最小，

$$
\min_{\boldsymbol{x} \in \mathbb{R}^n} \|\boldsymbol{r}\| = \min_{\boldsymbol{x} \in \mathbb{R}^n} \|\boldsymbol{b} - A\boldsymbol{x}\|,
$$

称为**最小二乘问题**，其解称为线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 的最小二乘解。

"二乘"指平方：$\|\boldsymbol{b} - A\boldsymbol{x}\|^2$ 是各方程误差的平方和。$A\boldsymbol{x}$ 取遍 $\mathcal{R}(A)$，由定理 4.4.3，$\boldsymbol{x}_0$ 是最小二乘解当且仅当 $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$；而 $P_A\boldsymbol{b} \in \mathcal{R}(A)$，所以最小二乘解总是存在。

**定理 4.5.1** $\boldsymbol{x}$ 是 $A\boldsymbol{x} = \boldsymbol{b}$ 的最小二乘解，当且仅当

$$
A^{\mathsf T}A\boldsymbol{x} = A^{\mathsf T}\boldsymbol{b}. \tag{4.1}
$$

**证明** 必要性：$\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x} = \boldsymbol{b} - P_A\boldsymbol{b} \in \mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$，即 $A^{\mathsf T}(\boldsymbol{b} - A\boldsymbol{x}) = \boldsymbol{0}$。充分性：若 $A^{\mathsf T}A\boldsymbol{x} = A^{\mathsf T}\boldsymbol{b}$，则 $\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{N}(A^{\mathsf T}) = \mathcal{R}(A)^\perp$，又 $\boldsymbol{b} - P_A\boldsymbol{b} \in \mathcal{R}(A)^\perp$，相减得 $P_A\boldsymbol{b} - A\boldsymbol{x} \in \mathcal{R}(A) \cap \mathcal{R}(A)^\perp = \{\boldsymbol{0}\}$，即 $A\boldsymbol{x} = P_A\boldsymbol{b}$。$\square$

**定义 4.5.2（正规方程）** 方程组 (4.1) 称为 $A\boldsymbol{x} = \boldsymbol{b}$ 的**正规方程**（也称法方程）。

课件把"通过求解正规方程求最小二乘解"的方法称为"正则化方法"；为避免与统计和机器学习中的正则化（regularization，如岭回归）混淆，本站称之为正规方程法。正规方程有明确的几何意义：残量 $\boldsymbol{b} - A\boldsymbol{x}$ 与 $A$ 的每一列都正交。

**性质 4.5.1** 最小二乘解的结构：

1. 若 $A$ 列满秩，则 $A^{\mathsf T}A$ 可逆（$\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A) = \{\boldsymbol{0}\}$），最小二乘解唯一：$\boldsymbol{x}_0 = (A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{b}$。此时 $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ 对一切 $\boldsymbol{b}$ 成立，故
   $$
   P_A = A(A^{\mathsf T}A)^{-1}A^{\mathsf T};
   $$
2. 若 $A$ 不列满秩，设 $\boldsymbol{x}_0$ 是一个最小二乘解，则最小二乘解的全体为 $\{\boldsymbol{x}_0 + \boldsymbol{x}_1 \mid \boldsymbol{x}_1 \in \mathcal{N}(A)\}$（正规方程的解集，由 $\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$ 得出）。其中长度最小的那一个由 Moore–Penrose 广义逆给出，见[第 7 章](/2.1.7)。

### 4.5.2. 正规方程法与正交化方法

$A$ 列满秩时 $A^{\mathsf T}A$ 是对称正定矩阵（[第 7 章](/2.1.7)），存在对角元为正的 $LDL^{\mathsf T}$ 分解（第 2 章 LDU 分解的对称情形），于是正规方程化为三个三角或对角方程组。

**算法 4.5.1（正规方程法）** 设 $A$ 列满秩。

1. 计算 $C = A^{\mathsf T}A$，$\boldsymbol{d} = A^{\mathsf T}\boldsymbol{b}$；
2. 计算 $C$ 的分解 $C = LDL^{\mathsf T}$（$L$ 单位下三角，$D$ 对角）；
3. 前代法求解下三角方程组 $L\boldsymbol{z} = \boldsymbol{d}$；
4. 求解对角方程组 $D\boldsymbol{y} = \boldsymbol{z}$；
5. **回代法**求解上三角方程组 $L^{\mathsf T}\boldsymbol{x} = \boldsymbol{y}$。

另一种方法利用 QR 分解。设 $A$ 列满秩，$A = QR = [Q_1\ Q_2]\begin{bmatrix} R_1 \\ O \end{bmatrix} = Q_1R_1$。由于正交矩阵保距，

$$
\|\boldsymbol{b} - A\boldsymbol{x}\|^2 = \|Q^{\mathsf T}(\boldsymbol{b} - QR\boldsymbol{x})\|^2 = \left\|\begin{bmatrix} Q_1^{\mathsf T}\boldsymbol{b} \\ Q_2^{\mathsf T}\boldsymbol{b} \end{bmatrix} - \begin{bmatrix} R_1 \\ O \end{bmatrix}\boldsymbol{x}\right\|^2 = \|Q_1^{\mathsf T}\boldsymbol{b} - R_1\boldsymbol{x}\|^2 + \|Q_2^{\mathsf T}\boldsymbol{b}\|^2.
$$

第二项与 $\boldsymbol{x}$ 无关，第一项在 $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$ 时为零，所以最小二乘解满足上三角方程组 $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$，最小残量为 $\|Q_2^{\mathsf T}\boldsymbol{b}\|$。从投影的角度看，$P_A = Q_1Q_1^{\mathsf T}$，由 $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ 即 $Q_1R_1\boldsymbol{x}_0 = Q_1Q_1^{\mathsf T}\boldsymbol{b}$，两边左乘 $Q_1^{\mathsf T}$ 也得到同一方程。

**算法 4.5.2（正交化方法）** 设 $A$ 列满秩。

1. 计算简化 QR 分解 $A = Q_1R_1$；
2. 计算 $\boldsymbol{c} = Q_1^{\mathsf T}\boldsymbol{b}$；
3. 回代求解上三角方程组 $R_1\boldsymbol{x} = \boldsymbol{c}$。

实际计算中应解方程组 $R_1\boldsymbol{x} = \boldsymbol{c}$，而不是先求 $R_1^{-1}$。$A$ 不列满秩时，可以通过适当的列对换（列主元 QR 分解）使 $Q_1$ 的前 $r$ 列构成 $\mathcal{R}(A)$ 的标准正交基。

两种方法的比较：正规方程法的运算量较小（主要是计算 $A^{\mathsf T}A$，约 $mn^2$ 次浮点运算），但 $\kappa(A^{\mathsf T}A) = \kappa(A)^2$，舍入误差会被放大；正交化方法（用 Householder QR，约 $2mn^2 - \frac{2}{3}n^3$ 次浮点运算）直接作用于 $A$，数值上更稳定，是数值软件的标准做法。

**例 4.5.1** 求 $A\boldsymbol{x} = \boldsymbol{b}$ 的最小二乘解，其中 $A = [\boldsymbol{a}_1\ \boldsymbol{a}_2] = \begin{bmatrix} 1 & 1 \\ 2 & 1 \\ 1 & 3 \end{bmatrix}$，$\boldsymbol{b} = \begin{bmatrix} 0 \\ 3 \\ 5 \end{bmatrix}$。

正规方程法：$A^{\mathsf T}A = \begin{bmatrix} 6 & 6 \\ 6 & 11 \end{bmatrix}$，$A^{\mathsf T}\boldsymbol{b} = \begin{bmatrix} 11 \\ 18 \end{bmatrix}$，解得 $\boldsymbol{x} = \begin{bmatrix} 13/30 \\ 7/5 \end{bmatrix}$。

正交化方法：对 $\boldsymbol{a}_1, \boldsymbol{a}_2$ 做 Gram–Schmidt 正交化，$\tilde{\boldsymbol{q}}_1 = \boldsymbol{a}_1$，$\tilde{\boldsymbol{q}}_2 = \boldsymbol{a}_2 - \frac{6}{6}\tilde{\boldsymbol{q}}_1 = \begin{bmatrix} 0 \\ -1 \\ 2 \end{bmatrix}$，得

$$
Q_1 = \begin{bmatrix} \frac{1}{\sqrt{6}} & 0 \\ \frac{2}{\sqrt{6}} & -\frac{1}{\sqrt{5}} \\ \frac{1}{\sqrt{6}} & \frac{2}{\sqrt{5}} \end{bmatrix}, \quad
R_1 = \begin{bmatrix} \sqrt{6} & \sqrt{6} \\ 0 & \sqrt{5} \end{bmatrix}, \quad
Q_1^{\mathsf T}\boldsymbol{b} = \begin{bmatrix} 11/\sqrt{6} \\ 7/\sqrt{5} \end{bmatrix}.
$$

回代得 $x_2 = 7/5$，$x_1 = 11/6 - 7/5 = 13/30$，与正规方程法一致。最小残量为 $\boldsymbol{r} = \boldsymbol{b} - A\boldsymbol{x} = \frac{11}{30}\begin{bmatrix} -5 \\ 2 \\ 1 \end{bmatrix}$，它与 $\boldsymbol{a}_1, \boldsymbol{a}_2$ 都正交。

### 4.5.3. 数据拟合

最小二乘法的一个重要应用是数据拟合。设变量 $y$ 与 $t$ 之间存在某种规律 $y = f(t)$，但函数形式未知；通过测量得到数据点 $(t_1, y_1), \cdots, (t_m, y_m)$。假定 $f$ 是已知的简单函数 $f_1, \cdots, f_n$ 的线性组合：

$$
f(t) = x_1f_1(t) + x_2f_2(t) + \cdots + x_nf_n(t),
$$

确定 $f$ 就是求系数 $x_1, \cdots, x_n$。令

$$
\boldsymbol{f}_j = \begin{bmatrix} f_j(t_1) \\ \vdots \\ f_j(t_m) \end{bmatrix}, \quad
A = [\boldsymbol{f}_1\ \cdots\ \boldsymbol{f}_n] = \begin{bmatrix} f_1(t_1) & \cdots & f_n(t_1) \\ \vdots & & \vdots \\ f_1(t_m) & \cdots & f_n(t_m) \end{bmatrix}, \quad
\boldsymbol{b} = \begin{bmatrix} y_1 \\ \vdots \\ y_m \end{bmatrix},
$$

条件 $f(t_i) = y_i$（$i = 1, \cdots, m$）就是 $A\boldsymbol{x} = \boldsymbol{b}$。数据点通常多于参数（$m > n$），且测量有误差、选定的函数形式也只是近似，这个方程组一般无解，于是转而求最小二乘解。注意 $f$ 关于 $t$ 可以是非线性的，只要它关于未知系数 $\boldsymbol{x}$ 是线性的，就是线性最小二乘问题。常见的选择：

| 拟合 | 函数形式 | 基函数 $f_j$ |
|---|---|---|
| 线性拟合 | $f(t) = kt + a$ | $t,\ 1$ |
| 二次拟合 | $f(t) = at^2 + bt + c$ | $t^2,\ t,\ 1$ |
| 多项式拟合 | $f(t) = a_nt^n + \cdots + a_1t + a_0$ | $t^n, \cdots, t, 1$ |

对多项式拟合，$A$ 就是第 5 章的 **Vandermonde 矩阵**（取前 $n+1$ 列）。

**例 4.5.2（一元线性拟合）** 给定数据 $(t_1, y_1), \cdots, (t_m, y_m)$，用 $y = kt + a$ 拟合。记 $\boldsymbol{t} = [t_i]$，$\boldsymbol{1} = [1\ \cdots\ 1]^{\mathsf T}$，$\boldsymbol{b} = [y_i]$，则 $A = [\boldsymbol{t}\ \boldsymbol{1}]$，$\boldsymbol{x} = \begin{bmatrix} k \\ a \end{bmatrix}$。只要 $t_i$ 不全相同，$A$ 就列满秩，最小二乘解唯一。正规方程为

$$
\begin{bmatrix} \boldsymbol{t}^{\mathsf T}\boldsymbol{t} & \boldsymbol{1}^{\mathsf T}\boldsymbol{t} \\ \boldsymbol{1}^{\mathsf T}\boldsymbol{t} & m \end{bmatrix}\begin{bmatrix} k \\ a \end{bmatrix} = \begin{bmatrix} \boldsymbol{t}^{\mathsf T}\boldsymbol{b} \\ \boldsymbol{1}^{\mathsf T}\boldsymbol{b} \end{bmatrix},
$$

解得

$$
k = \frac{1}{c}\left(\boldsymbol{t}^{\mathsf T}\boldsymbol{b} - \frac{1}{m}(\boldsymbol{1}^{\mathsf T}\boldsymbol{t})(\boldsymbol{1}^{\mathsf T}\boldsymbol{b})\right), \qquad
a = \frac{1}{cm}\left((\boldsymbol{t}^{\mathsf T}\boldsymbol{t})(\boldsymbol{1}^{\mathsf T}\boldsymbol{b}) - (\boldsymbol{1}^{\mathsf T}\boldsymbol{t})(\boldsymbol{t}^{\mathsf T}\boldsymbol{b})\right), \qquad
c = \boldsymbol{t}^{\mathsf T}\boldsymbol{t} - \frac{1}{m}(\boldsymbol{1}^{\mathsf T}\boldsymbol{t})^2.
$$

用均值 $\bar{t} = \frac{1}{m}\sum t_i$、$\bar{y} = \frac{1}{m}\sum y_i$ 表示，即 $k = \dfrac{\sum (t_i - \bar{t})(y_i - \bar{y})}{\sum (t_i - \bar{t})^2}$，$a = \bar{y} - k\bar{t}$，这就是统计学中一元线性回归的系数公式；拟合直线总经过点 $(\bar{t}, \bar{y})$。

**注 4.5.1** 拟合函数关于参数非线性时，有时可以先做变换化为线性问题。例如 $y = a\mathrm{e}^{bt}$ 取对数得 $\ln y = \ln a + bt$，对数据 $(t_i, \ln y_i)$ 做线性拟合；$y = a/(t + b)$ 可写成 $1/y = t/a + b/a$。但变换后最小化的是变换后的误差平方和，与原问题的最小二乘解一般不同；需要原问题的最优解时，要用非线性最小二乘的迭代方法。

下图用 QR 分解（算法 4.5.2）对同一组数据分别做线性拟合与二次拟合，竖线是残量的各个分量；二次拟合的残量平方和明显更小。

![对同一组数据做线性拟合与二次拟合，红色竖线表示残量](./plots/least-squares-fit.py)

## 小结 {#summary}

本章的核心是"正交化"：有了标准正交基，坐标、投影和最小二乘都只需做内积。

| 概念或结论 | 内容 | 位置 |
|---|---|---|
| 内积、长度、夹角 | $\boldsymbol{a}^{\mathsf T}\boldsymbol{b}$；$\Vert \boldsymbol{a}\Vert = \sqrt{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$；$\arccos\frac{\boldsymbol{a}^{\mathsf T}\boldsymbol{b}}{\Vert \boldsymbol{a}\Vert \Vert \boldsymbol{b}\Vert }$ | 4.1 节 |
| Cauchy–Schwarz、三角不等式、勾股定理 | $\vert \boldsymbol{a}^{\mathsf T}\boldsymbol{b}\vert \le \Vert \boldsymbol{a}\Vert \Vert \boldsymbol{b}\Vert$ | 定理 4.1.1、推论 4.1.1、定理 4.1.2 |
| 标准正交基 | 存在、可扩充；坐标为 $\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}$ | 定理 4.2.1、定理 4.2.2 |
| 正交矩阵 | $Q^{\mathsf T}Q = I$；$Q^{-1} = Q^{\mathsf T}$；保距、保内积 | 定理 4.3.1、定理 4.3.2 |
| Givens / Householder 变换 | 平面旋转 $G_{\theta;i,j}$；反射 $H_{\boldsymbol{v}} = I - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$ | 定义 4.3.2、定义 4.3.3 |
| QR 分解 | $A = QR = Q_1R_1$；可逆时唯一 | 定理 4.3.3、定理 4.3.4 |
| 正交补 | $\dim M^\perp = n - \dim M$；$\mathcal{R}(A)^\perp = \mathcal{N}(A^{\mathsf T})$；$\mathcal{N}(A^{\mathsf T}A) = \mathcal{N}(A)$ | 定理 4.4.1、定理 4.4.2 |
| 正交投影 | $P_M = Q_rQ_r^{\mathsf T}$；最佳逼近；$P^2 = P^{\mathsf T} = P$ | 定理 4.4.3、定理 4.4.4 |
| 最小二乘 | $A\boldsymbol{x}_0 = P_A\boldsymbol{b}$ ⇔ $A^{\mathsf T}A\boldsymbol{x}_0 = A^{\mathsf T}\boldsymbol{b}$；列满秩时 $P_A = A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$ | 定理 4.5.1、性质 4.5.1 |

| 算法 | 输入 → 输出 | 要点 |
|---|---|---|
| Gram–Schmidt 正交化（算法 4.2.1） | 一组基 → 标准正交基 | 逐个减去已得方向上的投影，再单位化 |
| Gram–Schmidt QR（算法 4.3.1） | 列满秩 $A$ → $Q_1R_1$ | $r_{ij} = \boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$；改进版数值上更好 |
| Householder QR（算法 4.3.2） | $A$ → $QR$ | 逐列用反射消元；数值稳定，软件标准做法 |
| 正规方程法（算法 4.5.1） | $A, \boldsymbol{b}$ → 最小二乘解 | $A^{\mathsf T}A = LDL^{\mathsf T}$，解三个三角/对角方程组 |
| 正交化方法（算法 4.5.2） | $A, \boldsymbol{b}$ → 最小二乘解 | $R_1\boldsymbol{x} = Q_1^{\mathsf T}\boldsymbol{b}$；比正规方程法稳定 |
