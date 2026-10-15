---
title: 行列式
---

行列式把一个方阵映成一个数。它有两种同样重要的解释：一是以矩阵各列为棱的平行体的有向体积，二是矩阵对应的线性变换把体积放大的倍数（变积系数）。本章不从"展开式"出发，而是像课件那样，先从有向面积抽象出三条公理（列多线性、列反对称、单位化），用公理推出行列式的全部性质与唯一性，再用展开式证明满足公理的函数确实存在。

由此得到的主要结论是：$\det A \ne 0$ 当且仅当 $A$ 可逆；$\det(AB) = \det A\det B$；行列式可以用 Gauss 消元在 $O(n^3)$ 次运算内算出。代数余子式给出逆矩阵公式与 Cramer 法则，它们在理论上很有用，但不适合数值计算。本章依赖第 2 章的**初等矩阵**、**可逆矩阵**与消元法，以及第 4 章的正交矩阵与 QR 分解；第 6 章用行列式定义特征多项式。完全展开式中的排列就是 1.3.2 中的**置换**。

## 5.1. 有向体积与行列式的定义

### 5.1.1. 有向面积

我们希望定义 $\mathbb{R}^n$ 中以 $n$ 个向量为棱的平行体的有向体积（带符号的体积）。先看平面：以 $\boldsymbol{a}_1 = \begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix}$，$\boldsymbol{a}_2 = \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}$ 为邻边的平行四边形的有向面积 $\delta(\boldsymbol{a}_1, \boldsymbol{a}_2)$ 应当满足：

- 双线性：$\delta(k\boldsymbol{a}_1 + k'\boldsymbol{a}_1', \boldsymbol{a}_2) = k\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) + k'\delta(\boldsymbol{a}_1', \boldsymbol{a}_2)$，对第二个变量同理（一条边伸长 $k$ 倍，面积变为 $k$ 倍；底边相加，面积相加）；
- 共线为零，等价地，反对称：$\delta(\boldsymbol{a}, \boldsymbol{a}) = 0$，等价于 $\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) = -\delta(\boldsymbol{a}_2, \boldsymbol{a}_1)$（交换两边改变定向）；
- 单位化：$\delta(\boldsymbol{e}_1, \boldsymbol{e}_2) = 1$（单位正方形的面积为 $1$）。

这三条性质唯一地确定了 $\delta$：

$$
\begin{aligned}
\delta(\boldsymbol{a}_1, \boldsymbol{a}_2) &= \delta(a_{11}\boldsymbol{e}_1 + a_{21}\boldsymbol{e}_2,\ a_{12}\boldsymbol{e}_1 + a_{22}\boldsymbol{e}_2) \\
&= a_{11}a_{12}\delta(\boldsymbol{e}_1, \boldsymbol{e}_1) + a_{11}a_{22}\delta(\boldsymbol{e}_1, \boldsymbol{e}_2) + a_{21}a_{12}\delta(\boldsymbol{e}_2, \boldsymbol{e}_1) + a_{21}a_{22}\delta(\boldsymbol{e}_2, \boldsymbol{e}_2) \\
&= a_{11}a_{22} - a_{12}a_{21}.
\end{aligned}
$$

### 5.1.2. 行列式的公理化定义

把 $n$ 个列向量的函数 $\delta(\boldsymbol{a}_1, \cdots, \boldsymbol{a}_n)$ 看作方阵 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ 的函数 $\delta(A)$，就得到：

**定义 5.1.1（行列式）** 定义在全体 $n$ 阶方阵上的函数 $\delta: \mathbb{R}^{n \times n} \to \mathbb{R}$ 若满足：

1. 列多线性：对每一列都是线性的，即对 $i = 1, \cdots, n$，
   $$
   \delta(\cdots, k\boldsymbol{a}_i + k'\boldsymbol{a}_i', \cdots) = k\delta(\cdots, \boldsymbol{a}_i, \cdots) + k'\delta(\cdots, \boldsymbol{a}_i', \cdots);
   $$
2. 列反对称：交换任意两列，函数值变号，即对 $i < j$，$\delta(\cdots, \boldsymbol{a}_i, \cdots, \boldsymbol{a}_j, \cdots) = -\delta(\cdots, \boldsymbol{a}_j, \cdots, \boldsymbol{a}_i, \cdots)$；
3. 单位化：$\delta(I_n) = 1$，

则称 $\delta$ 为 $n$ 阶行列式函数。行列式函数在方阵 $A$ 上的值称为 $A$ 的**行列式**，记作 $\det(A)$、$\det A$ 或 $|A|$。

后面将证明 $n$ 阶行列式函数存在且唯一（定理 5.3.1、定理 5.5.1），所以"$A$ 的行列式"是确定的。记号 $|A|$ 通常只在把 $A$ 写成 $n$ 行 $n$ 列数表（$n > 1$）时使用，注意与绝对值区分。

**例 5.1.1** 一阶行列式 $\det[a_{11}] = a_{11}$；二阶行列式就是有向面积：

$$
\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}.
$$

由列多线性，$\det(kA) = k^n\det A$，与体积的缩放规律一致。因此 $n > 1$ 时行列式不是线性函数：一般 $\det(A + B) \ne \det A + \det B$。

**性质 5.1.1（共线为零）** 设 $A$ 是 $n$ 阶方阵。

1. 若 $A$ 有两列相等，则 $\det A = 0$；
2. 若 $A$ 不满秩（即不可逆），则 $\det A = 0$；
3. 若 $A$ 有一列为零或一行为零，则 $\det A = 0$。

**证明** 1. 交换这两列，矩阵不变，由列反对称性 $\det A = -\det A$。2. 若 $A$ 不满秩，其列向量组**线性相关**，有一列可以写成其他列的**线性组合** $\boldsymbol{a}_j = \sum_{i \ne j} k_i\boldsymbol{a}_i$。由列多线性，

$$
\det A = \sum_{i \ne j} k_i\,\delta(\boldsymbol{a}_1, \cdots, \boldsymbol{a}_{j-1}, \boldsymbol{a}_i, \boldsymbol{a}_{j+1}, \cdots, \boldsymbol{a}_n) = 0,
$$

因为每一项都有两列相等。3. 有一行或一列为零的矩阵不满秩，由 2 即得。$\square$

在列多线性的条件下，列反对称与"两列相等则为零"等价：前者推出后者见上；反之，若两列相等时总为零，则

$$
0 = \delta(\cdots, \boldsymbol{a}_i + \boldsymbol{a}_j, \cdots, \boldsymbol{a}_i + \boldsymbol{a}_j, \cdots) = \delta(\cdots, \boldsymbol{a}_i, \cdots, \boldsymbol{a}_j, \cdots) + \delta(\cdots, \boldsymbol{a}_j, \cdots, \boldsymbol{a}_i, \cdots).
$$

几何上，性质 5.1.1 的 2 是说：棱落在一个低维子空间里的平行体是"扁"的，体积为零。只有可逆矩阵的行列式才可能非零，下一节证明它确实非零。

## 5.2. 行列式的性质

### 5.2.1. 初等矩阵的行列式

记第 2 章的三类初等矩阵为：对换矩阵 $P_{ij}$（交换第 $i, j$ 列）；倍乘矩阵 $E_{ii;k}$（第 $i$ 列乘以 $k \ne 0$）；倍加矩阵 $E_{ji;k} = I_n + k\boldsymbol{e}_j\boldsymbol{e}_i^{\mathsf T}$（右乘时把第 $j$ 列的 $k$ 倍加到第 $i$ 列）。

**命题 5.2.1（初等矩阵的行列式）** $\det P_{ij} = -1$，$\det E_{ii;k} = k$，$\det E_{ji;k} = 1$。初等矩阵与其转置的行列式相同。

**证明** 三类初等矩阵都是对 $I_n$ 做一次初等列变换得到的。$P_{ij}$ 交换 $I_n$ 的两列，由列反对称性 $\det P_{ij} = -\det I_n = -1$；$E_{ii;k}$ 把第 $i$ 列乘以 $k$，由列多线性 $\det E_{ii;k} = k$；对 $E_{ji;k}$，

$$
\det E_{ji;k} = \delta(\cdots, \boldsymbol{e}_i + k\boldsymbol{e}_j, \cdots, \boldsymbol{e}_j, \cdots) = \delta(\cdots, \boldsymbol{e}_i, \cdots, \boldsymbol{e}_j, \cdots) + k\,\delta(\cdots, \boldsymbol{e}_j, \cdots, \boldsymbol{e}_j, \cdots) = 1.
$$

又 $P_{ij}^{\mathsf T} = P_{ij}$，$E_{ii;k}^{\mathsf T} = E_{ii;k}$，$E_{ji;k}^{\mathsf T} = E_{ij;k}$，故转置后行列式不变。$\square$

**命题 5.2.2（初等列变换下的行列式）** 同理可得：

1. 交换 $A$ 的第 $i, j$ 列：$\det(AP_{ij}) = -\det A = \det A\det P_{ij}$；
2. 把 $A$ 的第 $i$ 列乘以 $k \ne 0$：$\det(AE_{ii;k}) = k\det A = \det A\det E_{ii;k}$；
3. 把 $A$ 的第 $j$ 列的 $k$ 倍加到第 $i$ 列：$\det(AE_{ji;k}) = \det A = \det A\det E_{ji;k}$。

即对任意初等矩阵 $E$，$\det(AE) = \det A\det E$。

### 5.2.2. 行列式的运算规则

**定理 5.2.1** 设 $A, B$ 是 $n$ 阶方阵。

1. 若可逆矩阵 $A = E_1E_2\cdots E_m$，$E_i$ 是初等矩阵，则 $\det A = \det E_1\det E_2\cdots\det E_m$；
2. $\det A \ne 0$ 当且仅当 $A$ 可逆；
3. $\det(AB) = \det A\det B = \det(BA)$；
4. $\det A^{\mathsf T} = \det A$。

**证明** 1. 反复应用命题 5.2.2：$\det A = \det(E_1\cdots E_{m-1})\det E_m = \cdots = \det E_1\cdots\det E_m$。

2. 可逆矩阵是初等矩阵的乘积（第 2 章），由 1 和命题 5.2.1，其行列式是若干非零数之积，非零；不可逆矩阵的行列式为零（性质 5.1.1）。

3. 若 $B$ 可逆，$B = E_1\cdots E_m$，则 $\det(AB) = \det(AE_1\cdots E_m) = \det A\det E_1\cdots\det E_m = \det A\det B$。若 $B$ 不可逆，则 $AB$ 不可逆（$\operatorname{rank}(AB) \le \operatorname{rank}B < n$），两边都是 $0$。交换 $A, B$ 即得第二个等号。

4. 若 $A = E_1\cdots E_m$ 可逆，则 $A^{\mathsf T} = E_m^{\mathsf T}\cdots E_1^{\mathsf T}$，由命题 5.2.1 与 1，$\det A^{\mathsf T} = \det E_m\cdots\det E_1 = \det A$。若 $A$ 不可逆，则 $A^{\mathsf T}$ 也不可逆，两边都是 $0$。$\square$

由 3，若 $A$ 可逆，则 $\det A\det A^{-1} = \det I_n = 1$，即 $\det A^{-1} = 1/\det A$。注意乘积公式虽然成立，加法却没有对应的公式。

**推论 5.2.1（行列式作为行向量组的函数）** 由 $\det A^{\mathsf T} = \det A$：

1. 行列式也是行多线性、行反对称的；初等行变换对行列式的影响与初等列变换相同；
2. 若函数 $\delta: \mathbb{R}^{n \times n} \to \mathbb{R}$ 满足行多线性、行反对称和单位化，则 $\delta$ 就是 $n$ 阶行列式函数（因为 $A \mapsto \delta(A^{\mathsf T})$ 满足定义 5.1.1）。

## 5.3. 几何意义与唯一性

### 5.3.1. 变积系数

从线性变换的角度看 $\det(AB) = \det A\det B$：设 $A$ 对应线性变换 $\boldsymbol{x} \mapsto A\boldsymbol{x}$，$B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$，则

$$
\det(AB) = \delta(A\boldsymbol{b}_1, \cdots, A\boldsymbol{b}_n) = \det A \cdot \delta(\boldsymbol{b}_1, \cdots, \boldsymbol{b}_n),
$$

即在 $A$ 的作用下，以 $\boldsymbol{b}_1, \cdots, \boldsymbol{b}_n$ 为棱的平行体的有向体积变为原来的 $\det A$ 倍。因此 $\det A$ 称为线性变换 $A$ 的变积系数；复合变换的变积系数是各自变积系数之积。$\det A$ 的符号表示变换是否保持定向，$|\det A|$ 表示体积放大的倍数。这一观点在多元积分的变量替换中会再次出现（Jacobi 行列式）。

平面上的三类初等变换正好对应三种基本的几何操作：

| 初等矩阵 | 例 | 几何意义 | 行列式 | 对应的消元操作 |
|---|---|---|---|---|
| 对换矩阵 $P_{12}$ | $(x_1, x_2) \mapsto (x_2, x_1)$ | 关于直线 $x_1 = x_2$ 的反射 | $-1$ | 交换两行：行列式变号 |
| 倍乘矩阵 $E_{11;k}$ | $(x_1, x_2) \mapsto (kx_1, x_2)$ | 沿 $x_1$ 方向伸缩 | $k$ | 一行乘以 $k$：行列式乘以 $k$ |
| 倍加矩阵 $E_{21;k}$ | $(x_1, x_2) \mapsto (x_1, kx_1 + x_2)$ | 错切（等底等高） | $1$ | 一行的倍数加到另一行：不变 |

一般地，$n$ 阶对换矩阵 $P_{ij} = I_n - (\boldsymbol{e}_i - \boldsymbol{e}_j)(\boldsymbol{e}_i - \boldsymbol{e}_j)^{\mathsf T} = I_n - 2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}$，$\boldsymbol{v} = (\boldsymbol{e}_i - \boldsymbol{e}_j)/\sqrt{2}$，是一个 **Householder 变换**。

### 5.3.2. 唯一性

**定理 5.3.1** $n$ 阶行列式函数如果存在，则唯一。

**证明** 设 $\delta_1, \delta_2$ 都是行列式函数。若 $A$ 不满秩，$\delta_1(A) = \delta_2(A) = 0$；若 $A$ 是初等矩阵，命题 5.2.1 只用到了公理，故 $\delta_1(A) = \delta_2(A)$；若 $A$ 可逆，$A = E_1\cdots E_m$，则 $\delta_1(A) = \delta_1(E_1)\cdots\delta_1(E_m) = \delta_2(E_1)\cdots\delta_2(E_m) = \delta_2(A)$。$\square$

证明过程说明行列式由它在初等矩阵上的值和乘积性质决定：

**命题 5.3.1** 定义在全体 $n$ 阶方阵上的函数 $\delta$ 若满足以下五条，则 $\delta$ 就是行列式函数：

1. $\delta(AB) = \delta(A)\delta(B)$；
2. 若 $A$ 不可逆，则 $\delta(A) = 0$；
3. 对换矩阵满足 $\delta(P_{ij}) = -1$；
4. 倍乘矩阵满足 $\delta(E_{ii;k}) = k$（$k \ne 0$）；
5. 倍加矩阵满足 $\delta(E_{ji;k}) = 1$。

这五条正是"$\mathbb{R}^n$ 上线性变换的变积系数"应当具有的性质。

## 5.4. 行列式的计算

### 5.4.1. 特殊矩阵的行列式

**例 5.4.1**

1. **对角矩阵**：由列多线性，行列式是对角元之积；几何上是各棱沿标准基方向的长方体的有向体积。
2. **三角矩阵**：行列式是对角元之积。若有对角元为零，则矩阵不满秩，行列式为零；否则可以用倍加变换消去非对角元而不改变行列式，几何上就是用一系列等底等高的错切把平行体化成等体积的长方体。
3. 正交矩阵 $Q$：由 $Q^{\mathsf T}Q = I_n$ 取行列式得 $(\det Q)^2 = 1$，$\det Q = \pm 1$。正交变换保距保角，不改变体积的大小。
4. 可逆矩阵 $X$：$\det X^{-1} = 1/\det X$，进一步 $\det(X^{-1}AX) = \det A$。
5. 分块对角与分块三角矩阵：设 $A, B$ 是方阵，则
   $$
   \det\begin{bmatrix} A & O \\ O & B \end{bmatrix} = \det\begin{bmatrix} A & C \\ O & B \end{bmatrix} = \det\begin{bmatrix} A & O \\ D & B \end{bmatrix} = \det A\det B.
   $$

对第 5 条中的分块上三角矩阵，证明如下（其余类似）。若 $A$ 不可逆，则前几列线性相关，两边都为零。若 $A$ 可逆，

$$
\begin{bmatrix} A & C \\ O & B \end{bmatrix} = \begin{bmatrix} A & O \\ O & I \end{bmatrix}\begin{bmatrix} I & A^{-1}C \\ O & B \end{bmatrix}.
$$

函数 $X \mapsto \det\begin{bmatrix} X & O \\ O & I \end{bmatrix}$ 满足定义 5.1.1 的三条公理，故等于 $\det X$；在第二个因子中，用前面的列做倍加列变换可消去 $A^{-1}C$ 而不改变行列式，再用同样的论证得 $\det\begin{bmatrix} I & O \\ O & B \end{bmatrix} = \det B$。

由第 3 条与 QR 分解可以得到行列式的一个直观解释：设 $A = QR$（第 4 章），则 $\det A = \det Q\det R$，其中 $\det Q = \pm 1$ 表示有向体积的符号，$\det R = \prod_i r_{ii} = \prod_i \|\tilde{\boldsymbol{q}}_i\| \ge 0$ 是体积的大小。$\|\tilde{\boldsymbol{q}}_i\|$ 是 $\boldsymbol{a}_i$ 到前 $i-1$ 个棱张成的子空间的距离，即平行体逐层的"高"，所以 $|\det A|$ 就是"底面积乘高"的 $n$ 维推广。

### 5.4.2. 用消元计算行列式

对一般的矩阵，计算行列式的基本方法是用初等变换把它化简，并记录每一步对行列式的影响：

- 倍加行（列）变换：行列式不变；
- 对换行（列）变换：行列式变号；
- 参数为 $k$ 的倍乘行（列）变换：行列式变为 $k$ 倍。

**算法 5.4.1（用 Gauss 消元计算行列式）** 输入 $n$ 阶方阵 $A$。

1. 对 $A$ 做 Gauss 消元（必要时交换行选主元），只用倍加变换与对换变换化为上三角矩阵 $U$，记录对换的次数 $s$；若某一步找不到非零主元，则 $\det A = 0$；
2. $\det A = (-1)^s u_{11}u_{22}\cdots u_{nn}$。

用矩阵语言，就是求出 **PLU 分解** $PA = LU$，于是 $\det A = \det P^{-1}\det L\det U = \pm\prod_i u_{ii}$。运算量约为 $\frac{2}{3}n^3$ 次浮点运算，与解一个线性方程组相当。

**例 5.4.2** 计算 $\det A = \begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 3 & 7 & 10 \end{vmatrix}$。

用倍加变换消去第一列，再交换后两行：

$$
\begin{vmatrix} 1 & 2 & 3 \\ 2 & 4 & 7 \\ 3 & 7 & 10 \end{vmatrix} = \begin{vmatrix} 1 & 2 & 3 \\ 0 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = -\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} = -1.
$$

也可以在第二步把它看作分块上三角矩阵：$\begin{vmatrix} 1 & 2 & 3 \\ 0 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = 1 \cdot \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} = -1$。

### 5.4.3. Vandermonde 行列式与多项式插值

**例 5.4.3** 设二次多项式 $p(x) = k_2x^2 + k_1x + k_0$ 经过三个横坐标两两不同的点 $(\lambda_i, \mu_i)$（$i = 1, 2, 3$）。这样的多项式是否存在？是否唯一？

条件 $p(\lambda_i) = \mu_i$ 是关于系数的线性方程组

$$
\begin{bmatrix} 1 & \lambda_1 & \lambda_1^2 \\ 1 & \lambda_2 & \lambda_2^2 \\ 1 & \lambda_3 & \lambda_3^2 \end{bmatrix}\begin{bmatrix} k_0 \\ k_1 \\ k_2 \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \mu_2 \\ \mu_3 \end{bmatrix}.
$$

多项式存在且唯一，当且仅当系数矩阵可逆，即行列式非零。从右向左，把每一列的 $-\lambda_1$ 倍加到右边相邻的列：

$$
\begin{vmatrix} 1 & \lambda_1 & \lambda_1^2 \\ 1 & \lambda_2 & \lambda_2^2 \\ 1 & \lambda_3 & \lambda_3^2 \end{vmatrix}
= \begin{vmatrix} 1 & 0 & 0 \\ 1 & \lambda_2 - \lambda_1 & \lambda_2^2 - \lambda_2\lambda_1 \\ 1 & \lambda_3 - \lambda_1 & \lambda_3^2 - \lambda_3\lambda_1 \end{vmatrix}
= (\lambda_2 - \lambda_1)(\lambda_3 - \lambda_1)\begin{vmatrix} 1 & \lambda_2 \\ 1 & \lambda_3 \end{vmatrix}
= \prod_{1 \le j < i \le 3}(\lambda_i - \lambda_j).
$$

$\lambda_i$ 两两不同时它非零，所以三点唯一确定一个次数不超过 $2$ 的多项式。

**定义 5.4.1（Vandermonde 矩阵）** 形如

$$
V = \begin{bmatrix} 1 & \lambda_1 & \lambda_1^2 & \cdots & \lambda_1^{n-1} \\ 1 & \lambda_2 & \lambda_2^2 & \cdots & \lambda_2^{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & \lambda_n & \lambda_n^2 & \cdots & \lambda_n^{n-1} \end{bmatrix}
$$

的矩阵称为 **Vandermonde 矩阵**。

**定理 5.4.1** $\det V = \displaystyle\prod_{1 \le j < i \le n}(\lambda_i - \lambda_j)$。特别地，$\lambda_1, \cdots, \lambda_n$ 两两不同时 $V$ 可逆。

**证明** 对 $n$ 用数学归纳法，$n = 2$ 时 $\det V = \lambda_2 - \lambda_1$。与例 5.4.3 相同，从最后一列开始，依次把第 $k$ 列的 $-\lambda_1$ 倍加到第 $k+1$ 列（$k = n-1, \cdots, 1$），第 $i$ 行变为 $[1,\ \lambda_i - \lambda_1,\ \lambda_i(\lambda_i - \lambda_1),\ \cdots,\ \lambda_i^{n-2}(\lambda_i - \lambda_1)]$，第一行变为 $[1, 0, \cdots, 0]$。按分块下三角矩阵计算，再从第 $i$ 行（$i \ge 2$）提出公因子 $\lambda_i - \lambda_1$，得

$$
\det V = \prod_{i=2}^n(\lambda_i - \lambda_1) \cdot \det V(\lambda_2, \cdots, \lambda_n),
$$

其中 $V(\lambda_2, \cdots, \lambda_n)$ 是 $n-1$ 阶 Vandermonde 矩阵。由归纳假设即得结论。$\square$

**定义 5.4.2（多项式插值）** 给定平面上若干点，求一条经过这些点的曲线，称为插值；插值函数是多项式时称为**多项式插值**。

由定理 5.4.1，给定 $n$ 个横坐标两两不同的点，存在唯一的次数不超过 $n-1$ 的插值多项式。直接解 Vandermonde 方程组并不是求插值多项式的好方法（$V$ 往往非常病态）；Lagrange 插值公式见[第 9 章](/2.1.9)。

## 5.5. 行列式的展开

### 5.5.1. 余子式与代数余子式

**例 5.5.1** 用列多线性把第一列拆开，再用行反对称性把非零元换到第一行，可以用二阶行列式表示三阶行列式：

$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}
= a_{11}\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}
- a_{21}\begin{vmatrix} a_{12} & a_{13} \\ a_{32} & a_{33} \end{vmatrix}
+ a_{31}\begin{vmatrix} a_{12} & a_{13} \\ a_{22} & a_{23} \end{vmatrix}.
$$

完全展开即得

$$
\det A = a_{11}a_{22}a_{33} - a_{11}a_{32}a_{23} + a_{21}a_{32}a_{13} - a_{21}a_{12}a_{33} + a_{31}a_{12}a_{23} - a_{31}a_{22}a_{13}.
$$

下面把这一做法推广到 $n$ 阶：用 $n-1$ 阶行列式递归地表示 $n$ 阶行列式，这同时证明了行列式函数的存在性。

**定义 5.5.1（余子式与代数余子式）** 设 $A$ 是 $n$ 阶方阵，$n \ge 2$。记 $A\binom{i}{j}$ 为从 $A$ 中划去第 $i$ 行和第 $j$ 列得到的 $n-1$ 阶方阵，则 $M_{ij} = \det A\binom{i}{j}$ 称为元素 $a_{ij}$ 的**余子式**，$C_{ij} = (-1)^{i+j}M_{ij}$ 称为 $a_{ij}$ 的**代数余子式**。

符号 $(-1)^{i+j}$ 来自行列式的反对称性：把第 $i$ 行、第 $j$ 列移到左上角需要 $(i-1) + (j-1)$ 次相邻对换。例如二阶时 $\det A = a_{11}C_{11} + a_{21}C_{21}$，三阶时例 5.5.1 就是 $\det A = a_{11}C_{11} + a_{21}C_{21} + a_{31}C_{31}$。

**定理 5.5.1（按第一列展开）** 设 $A = [a_{ij}]$ 是 $n$ 阶方阵，$n \ge 2$，则

$$
\delta(A) = a_{11}C_{11} + a_{21}C_{21} + \cdots + a_{n1}C_{n1} = \sum_{i=1}^n a_{i1}C_{i1}
$$

是 $n$ 阶行列式函数。从而行列式函数存在，且 $\det A = \sum_i a_{i1}C_{i1}$，称为行列式按第一列的展开式。

**证明** 对 $n$ 用数学归纳法，$n = 2$ 时已验证。设 $n-1$ 阶行列式函数存在（即代数余子式有意义且具有行列式的全部性质）。由推论 5.2.1，只需验证 $\delta$ 满足行多线性、行反对称和单位化。

行多线性：以第一行为例（其他行同理）。设第一行 $a_{1j} = ka_{1j}' + \ell a_{1j}''$（$j = 1, \cdots, n$），$A', A''$ 分别是把第一行换成 $[a_{1j}']$、$[a_{1j}'']$ 的矩阵。$i \ne 1$ 时，$C_{i1}$ 所对应的子矩阵含有第一行（去掉第一个元素），由归纳假设 $C_{i1} = kC_{i1}' + \ell C_{i1}''$；而 $C_{11} = C_{11}' = C_{11}''$。于是

$$
\delta(A) = (ka_{11}' + \ell a_{11}'')C_{11} + \sum_{i=2}^n a_{i1}(kC_{i1}' + \ell C_{i1}'') = k\delta(A') + \ell\delta(A'').
$$

行反对称：在行多线性下等价于"两行相等则为零"。设 $A$ 的第 $p, q$ 行相等（$p < q$）。$i \ne p, q$ 时，$A\binom{i}{1}$ 有两行相等，$C_{i1} = 0$。而 $a_{p1} = a_{q1}$，且 $A\binom{p}{1}$ 与 $A\binom{q}{1}$ 只差一次把某一行移过 $q - p - 1$ 行的操作，故 $M_{p1} = (-1)^{q-p-1}M_{q1}$，于是

$$
a_{p1}C_{p1} + a_{q1}C_{q1} = a_{p1}\left((-1)^{p+1}(-1)^{q-p-1} + (-1)^{q+1}\right)M_{q1} = a_{p1}\left((-1)^{q} + (-1)^{q+1}\right)M_{q1} = 0.
$$

单位化：$\delta(I_n) = 1 \cdot C_{11} = \det I_{n-1} = 1$。$\square$

### 5.5.2. 按任意行或列展开

**定理 5.5.2** 行列式可以按任意一列或任意一行展开：

1. 按第 $j$ 列展开：$\det A = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj} = \sum_{i=1}^n a_{ij}C_{ij}$；
2. 按第 $i$ 行展开：$\det A = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in} = \sum_{j=1}^n a_{ij}C_{ij}$。

**证明** 1. 通过 $j-1$ 次相邻列对换把第 $j$ 列移到最左边，得 $A' = [\boldsymbol{a}_j\ \boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_{j-1}\ \boldsymbol{a}_{j+1}\ \cdots\ \boldsymbol{a}_n]$，$\det A = (-1)^{j-1}\det A'$。$A'$ 与 $A$ 满足 $a_{i1}' = a_{ij}$，$M_{i1}' = M_{ij}$，$C_{i1}' = (-1)^{1-j}C_{ij}$，对 $A'$ 按第一列展开即得。2. 对 $A^{\mathsf T}$ 按第 $i$ 列展开，并利用 $\det A^{\mathsf T} = \det A$。$\square$

展开式把一个 $n$ 阶行列式化为 $n$ 个 $n-1$ 阶行列式；当某一行或列有许多零时，按它展开能显著简化计算。

**例 5.5.2** 计算例 4.3.2 中正交矩阵 $Q = \begin{bmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} & 0 \end{bmatrix}$ 的行列式。

第三列有一个零元，按第三列展开：

$$
\det Q = \frac{1}{\sqrt{2}}\begin{vmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} \end{vmatrix} + \frac{1}{\sqrt{2}}\begin{vmatrix} \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & -\frac{2}{\sqrt{6}} \end{vmatrix} = \sqrt{2}\cdot\left(-\frac{3}{\sqrt{18}}\right) = -1.
$$

（第一项的符号为 $(-1)^{1+3} = 1$，第二项为 $(-1)^{2+3}\cdot\left(-\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}$。）$\det Q = -1$ 说明这个正交变换改变定向，与 $\det Q = \pm 1$ 一致。

## 5.6. 代数余子式的应用

### 5.6.1. 代数余子式向量

**命题 5.6.1** 设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，令第 $j$ 列元素的代数余子式组成向量 $\boldsymbol{c}_j = [C_{1j}\ C_{2j}\ \cdots\ C_{nj}]^{\mathsf T}$，则

$$
\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j = \begin{cases} \det A, & j' = j, \\ 0, & j' \ne j. \end{cases}
$$

对某一行元素的代数余子式组成的向量有类似结论。

**证明** $j' = j$ 时，$\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j$ 就是 $\det A$ 按第 $j$ 列的展开。$j' \ne j$ 时，把 $A$ 的第 $j$ 列换成 $\boldsymbol{a}_{j'}$，新矩阵的第 $j$ 列代数余子式仍是 $\boldsymbol{c}_j$，按第 $j$ 列展开得到 $\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j$；而新矩阵有两列相等，行列式为零。$\square$

几何意义：对 $j' \ne j$ 有 $\boldsymbol{a}_{j'} \perp \boldsymbol{c}_j$，所以 $\boldsymbol{c}_j$ 是以其余 $n-1$ 个列向量为棱的"底面"的法向量。$\boldsymbol{a}_j$ 向 $\boldsymbol{c}_j$ 方向的投影的有向长度 $\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j/\|\boldsymbol{c}_j\|$ 是平行体的高，而

$$
\det A = \boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j = \frac{\boldsymbol{a}_j^{\mathsf T}\boldsymbol{c}_j}{\|\boldsymbol{c}_j\|} \cdot \|\boldsymbol{c}_j\|,
$$

即"体积 = 高 × 底面积"，所以 $\|\boldsymbol{c}_j\|$ 是底面的面积。$n = 3$ 时，$\boldsymbol{c}_3$ 正是 $\boldsymbol{a}_1, \boldsymbol{a}_2$ 的叉积。

### 5.6.2. 伴随矩阵与逆矩阵公式

**定义 5.6.1（伴随矩阵）** 对 $n$ 阶方阵 $A = [a_{ij}]$，以 $a_{ij}$ 的代数余子式 $C_{ij}$ 为 $(i, j)$ 元的矩阵 $C = [C_{ij}]$ 称为 $A$ 的代数余子式矩阵，其转置 $C^{\mathsf T}$ 称为 $A$ 的**伴随矩阵**，记作 $\operatorname{adj}A$。

课件把 $C^{\mathsf T}$ 称为补矩阵。注意它与[第 12 章](/2.1.12)中线性变换的伴随（共轭转置）是不同的概念。

**定理 5.6.1（逆矩阵公式）** 对任意 $n$ 阶方阵 $A$，$C^{\mathsf T}A = AC^{\mathsf T} = \det(A)I_n$。特别地，若 $A$ 可逆，则

$$
A^{-1} = \frac{1}{\det A}C^{\mathsf T} = \frac{1}{\det A}\operatorname{adj}A.
$$

**证明** $C^{\mathsf T}A$ 的 $(i, j)$ 元为 $\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_j$，由命题 5.6.1，$i = j$ 时为 $\det A$，$i \ne j$ 时为 $0$。对行做同样的论证得 $AC^{\mathsf T} = \det(A)I_n$。$\square$

例如二阶时 $\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \dfrac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$。逆矩阵公式说明 $A^{-1}$ 的每个元素都是 $A$ 的元素的有理函数，因而连续依赖于 $A$；但它需要计算 $n^2$ 个 $n-1$ 阶行列式，实际求逆应当用第 2 章的 Gauss–Jordan 消元。

### 5.6.3. Cramer 法则

**定理 5.6.2（Cramer 法则）** 设 $A$ 是 $n$ 阶方阵，线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 有唯一解当且仅当 $\det A \ne 0$，此时唯一解为

$$
x_1 = \frac{\det B_1}{\det A}, \quad x_2 = \frac{\det B_2}{\det A}, \quad \cdots, \quad x_n = \frac{\det B_n}{\det A},
$$

其中 $B_j$ 是把 $A$ 的第 $j$ 列换成 $\boldsymbol{b}$ 得到的矩阵。

**证明** $A\boldsymbol{x} = \boldsymbol{b}$ 有唯一解当且仅当 $A$ 可逆，即 $\det A \ne 0$。把方程组写成 $x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b}$，两边与 $\boldsymbol{c}_i$ 做内积，由命题 5.6.1 得 $x_i\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_i = \boldsymbol{c}_i^{\mathsf T}\boldsymbol{b}$。$\boldsymbol{c}_i^{\mathsf T}\boldsymbol{a}_i$ 与 $\boldsymbol{c}_i^{\mathsf T}\boldsymbol{b}$ 分别是 $\det A$ 与 $\det B_i$ 按第 $i$ 列的展开，故 $x_i = \det B_i/\det A$。$\square$

几何意义：$x_i$ 是以 $\boldsymbol{b}$ 与 $\boldsymbol{a}_j$（$j \ne i$）为棱的平行体与以 $\boldsymbol{a}_1, \cdots, \boldsymbol{a}_n$ 为棱的平行体的有向体积之比。两个平行体有相同的底面（以 $\boldsymbol{a}_j$，$j \ne i$ 为棱）；由于 $\boldsymbol{b} - x_i\boldsymbol{a}_i = \sum_{j \ne i}x_j\boldsymbol{a}_j$ 在底面内，$\boldsymbol{b}$ 与 $x_i\boldsymbol{a}_i$ 在底面法向量 $\boldsymbol{c}_i$ 上的投影相等，所以 $x_i$ 就是两个平行体的高之比。

与逆矩阵公式一样，Cramer 法则是理论工具（例如说明解连续依赖于数据，或在二、三阶时手算），而不应用来数值求解方程组。

## 5.7. 排列与完全展开

### 5.7.1. 完全展开式

**例 5.7.1** 对三阶行列式的每一列都用多线性展开：

$$
\det A = \delta\left(\sum_{i} a_{i1}\boldsymbol{e}_i,\ \sum_{i} a_{i2}\boldsymbol{e}_i,\ \sum_{i} a_{i3}\boldsymbol{e}_i\right) = \sum_{\sigma_1, \sigma_2, \sigma_3} a_{\sigma_11}a_{\sigma_22}a_{\sigma_33}\,\delta(\boldsymbol{e}_{\sigma_1}, \boldsymbol{e}_{\sigma_2}, \boldsymbol{e}_{\sigma_3}).
$$

这是 $3^3 = 27$ 项之和，但只有 $\sigma_1, \sigma_2, \sigma_3$ 互不相同的 $3! = 6$ 项非零，它们对应的 $[\boldsymbol{e}_{\sigma_1}\ \boldsymbol{e}_{\sigma_2}\ \boldsymbol{e}_{\sigma_3}]$ 都是**置换矩阵**，行列式为 $\pm 1$，结果与例 5.5.1 一致。

### 5.7.2. 排列及其符号

**定义 5.7.1（排列）** 把 $1, 2, \cdots, n$ 按一定顺序排成 $\sigma_1, \sigma_2, \cdots, \sigma_n$，称为一个 $n$ 元排列，记作 $\sigma$。交换排列中两个数的位置，称为对该排列做一次对换。若排列 $\sigma$ 可以经过奇数次对换变为 $1, 2, \cdots, n$，则称为奇排列，定义其符号 $\operatorname{sign}(\sigma) = -1$；若可以经过偶数次对换变为 $1, 2, \cdots, n$，则称为偶排列，$\operatorname{sign}(\sigma) = 1$。

排列 $\sigma$ 就是映射 $i \mapsto \sigma_i$，即 1.3.2 中的**置换**；奇排列、偶排列分别对应**奇置换**、**偶置换**。排列与置换矩阵一一对应：$\sigma \mapsto P_\sigma = [\boldsymbol{e}_{\sigma_1}\ \cdots\ \boldsymbol{e}_{\sigma_n}]$，一次对换对应交换两列，于是 $\det P_\sigma = \operatorname{sign}(\sigma)$。

这也回答了"一个排列能否既是奇排列又是偶排列"：不能。若 $\sigma$ 经过 $s$ 次对换变为恒等排列，则 $P_\sigma$ 经过 $s$ 次列对换变为 $I_n$，$\det P_\sigma = (-1)^s$，而 $\det P_\sigma$ 是唯一确定的（定理 5.3.1），故 $s$ 的奇偶性由 $\sigma$ 唯一确定。$n \ge 2$ 时，固定一个对换 $\tau$，$\sigma \mapsto \tau\sigma$ 是奇排列与偶排列之间的一一对应，所以二者各有 $n!/2$ 个。

### 5.7.3. 完全展开定理

**定理 5.7.1（行列式的完全展开）** 对 $n$ 阶方阵 $A = [a_{ij}]$，

$$
\det A = \sum_{\sigma} \operatorname{sign}(\sigma)\,a_{\sigma_11}a_{\sigma_22}\cdots a_{\sigma_nn} = \sum_{\sigma} \operatorname{sign}(\sigma)\,a_{1\sigma_1}a_{2\sigma_2}\cdots a_{n\sigma_n},
$$

其中求和取遍全部 $n!$ 个 $n$ 元排列。

**证明** 与例 5.7.1 相同，对每一列用多线性展开：

$$
\det A = \sum_{\sigma_1, \cdots, \sigma_n = 1}^n a_{\sigma_11}\cdots a_{\sigma_nn}\,\delta(\boldsymbol{e}_{\sigma_1}, \cdots, \boldsymbol{e}_{\sigma_n}).
$$

若 $\sigma_1, \cdots, \sigma_n$ 中有两个相同，则 $\delta(\boldsymbol{e}_{\sigma_1}, \cdots, \boldsymbol{e}_{\sigma_n})$ 有两列相等，为零；否则 $\sigma$ 是排列，$\delta(\boldsymbol{e}_{\sigma_1}, \cdots, \boldsymbol{e}_{\sigma_n}) = \det P_\sigma = \operatorname{sign}(\sigma)$。这就得到第一个等式。对 $\det A^{\mathsf T} = \det A$ 应用第一个等式得第二个。$\square$

这个证明只用到了公理，所以它也独立地给出了唯一性；反过来，直接验证右端满足三条公理，也可以证明存在性。

完全展开式有 $n!$ 项，每项 $n-1$ 次乘法，运算量为 $(n-1)\cdot n!$；按行列展开的递归算法也需要约 $(e-1)\cdot n!$ 次乘法。它们都随 $n$ 超指数增长，而 Gauss 消元（算法 5.4.1）只需约 $n^3/3$ 次乘法。$n = 20$ 时，完全展开需要约 $5 \times 10^{19}$ 次乘法，消元只需约 $3000$ 次。因此行列式一般不应通过完全展开或按行列展开来计算；完全展开式的价值在于理论，例如说明 $\det A$ 是矩阵元素的多项式（从而是连续函数），以及第 6 章特征多项式次数与系数的推导。

![计算 n 阶行列式所需乘法次数的比较（对数纵轴）：完全展开与按行列展开随 n! 增长，Gauss 消元只按 n³ 增长](./plots/determinant-cost.py)

## 小结 {#summary}

行列式的理论可以概括为："三条公理 → 性质与唯一性 → 展开式给出存在性 → 消元给出计算"。

| 概念或结论 | 内容 | 位置 |
|---|---|---|
| 行列式 | 列多线性、列反对称、单位化的函数；存在且唯一 | 定义 5.1.1、定理 5.3.1、定理 5.5.1 |
| 共线为零 | 两列相等、不满秩、有零行或零列 ⇒ $\det A = 0$ | 性质 5.1.1 |
| 初等矩阵 | $\det P_{ij} = -1$，$\det E_{ii;k} = k$，$\det E_{ji;k} = 1$ | 命题 5.2.1 |
| 运算规则 | $\det A \ne 0 \iff A$ 可逆；$\det(AB) = \det A\det B$；$\det A^{\mathsf T} = \det A$；$\det A^{-1} = 1/\det A$ | 定理 5.2.1 |
| 几何意义 | 有向体积；线性变换的变积系数 | 5.3 节 |
| 特殊矩阵 | 对角、三角：对角元之积；正交：$\pm 1$；分块三角：$\det A\det B$ | 例 5.4.1 |
| Vandermonde 行列式 | $\prod_{j<i}(\lambda_i - \lambda_j)$；插值多项式存在唯一 | 定理 5.4.1 |
| 按行或列展开 | $\det A = \sum_i a_{ij}C_{ij} = \sum_j a_{ij}C_{ij}$ | 定理 5.5.2 |
| 代数余子式向量 | $\boldsymbol{a}_{j'}^{\mathsf T}\boldsymbol{c}_j = \delta_{jj'}\det A$；底面的法向量，长度为底面积 | 命题 5.6.1 |
| 逆矩阵公式与 Cramer 法则 | $A^{-1} = C^{\mathsf T}/\det A$；$x_j = \det B_j/\det A$ | 定理 5.6.1、定理 5.6.2 |
| 完全展开 | $\det A = \sum_\sigma \operatorname{sign}(\sigma)\prod_i a_{\sigma_ii}$ | 定理 5.7.1 |

| 计算方法 | 运算量 | 适用场合 |
|---|---|---|
| Gauss 消元（算法 5.4.1） | 约 $\frac{2}{3}n^3$ 次浮点运算 | 一般矩阵的标准方法 |
| 按某行或某列展开 | 约 $(e-1)\cdot n!$ 次乘法 | 某行或某列有许多零元时手算 |
| 完全展开 | $(n-1)\cdot n!$ 次乘法 | 理论推导，二、三阶手算 |
