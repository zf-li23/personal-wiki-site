---
title: 李代数
---

第 2 章的群大多是有限的，例如正三角形的 $6$ 个对称（例 2.4.1）。然而空间中的旋转、刚体运动这类对称是连续变化的：绕一根轴可以转任意角度，全体旋转构成一个"光滑"的无限群。直接研究这样的群很困难，挪威数学家 Sophus Lie 在 19 世纪 70 年代的想法是只看单位元附近的"无穷小变换"：它们构成一个向量空间，群的不可交换性在这个空间上留下一种双线性运算——**李括号**。这样得到的结构就是李代数，可以把它看作连续群的线性化；这样的连续群今称**李群**（Lie group）。

本章需要前面各章的以下内容：群、**子群**与**同态**（第 2 章），**域**与域上的**向量空间**（第 3 章，特别是定义 3.6.1），以及线性代数中的矩阵、迹和行列式（[线性代数](/2.1)）。第 4 章的格在这里不直接使用。与前面的结构相比，李代数的新特点是运算不满足**结合律**，雅可比恒等式代替了结合律的位置。本章先给出李代数的定义，再平行于群和环介绍子代数、理想、商代数与同态，然后列举基本例子并简介复单李代数的分类，最后用矩阵指数说明李群与李代数的联系。下一章的表示论将把群和李代数都"表示"为向量空间上的线性变换。

## 5.1. 李代数的定义

### 5.1.1. 向量空间

李代数首先是一个向量空间。本章所说的向量空间都是某个域 $F$（通常取 $\mathbb{R}$ 或 $\mathbb{C}$）上的向量空间，定义见定义 3.6.1：$(V, +)$ 是**交换群**，并有满足分配律、结合律的数乘。线性代数中的子空间、基、维数、线性映射和矩阵表示（[线性代数：线性空间与线性映射](/2.1.8)）在这里照常使用。

本章常用的记号：$M_n(F)$ 表示 $F$ 上全体 $n$ 阶矩阵；$\operatorname{End}(V)$ 表示 $V$ 上的全体线性变换，取定基后它就是 $M_n(F)$（$n = \dim V$）；$\operatorname{tr}$ 表示矩阵的迹，满足 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$（[矩阵的迹](/2.1.1#def-1.10.3)）。

在矩阵上，最自然的"度量不可交换程度"的运算是**换位子**（commutator）$[A, B] = AB - BA$：$[A, B] = 0$ 当且仅当 $A$ 与 $B$ 可交换。换位子关于 $A$、$B$ 都是线性的，满足 $[A, A] = 0$，但不满足结合律（例如取 $A = B$ 时 $[[A, B], C] = 0$，而 $[A, [B, C]]$ 一般不为零）。李代数的公理正是从换位子的这些性质中抽象出来的。

### 5.1.2. 李括号

**定义 5.1.2（李代数）** 设 $\mathfrak{g}$ 是域 $F$ 上的向量空间。若在 $\mathfrak{g}$ 上定义了运算 $[\cdot\,, \cdot]\colon \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$（称为**李括号**），满足以下三条公理，则称 $\mathfrak{g}$ 是一个李代数：

1. **双线性**：对任意 $x, y, z \in \mathfrak{g}$ 和 $a, b \in F$，
   $$
   [ax + by, z] = a[x, z] + b[y, z], \quad [x, ay + bz] = a[x, y] + b[x, z];
   $$
2. **交错性**：对任意 $x \in \mathfrak{g}$，
   $$
   [x, x] = 0;
   $$
3. **雅可比恒等式**：对任意 $x, y, z \in \mathfrak{g}$，
   $$
   [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
   $$

$\mathfrak{g}$ 作为向量空间的维数称为李代数的维数。用第 1 章的语言说，李代数是一个代数系统：加法、数乘之外再加一个二元运算 $[\cdot\,, \cdot]$，而分配律被双线性所包含。

由交错性和双线性可推出反对称性 $[x, y] = -[y, x]$：展开 $0 = [x + y, x + y] = [x, y] + [y, x]$ 即得，这对任何特征的域都成立。反过来，若**域的特征**（定义 3.5.4）不为 $2$，则由反对称性得 $[x, x] = -[x, x]$，从而 $[x, x] = 0$，两条公理等价。

李括号一般不满足结合律，雅可比恒等式起着替代结合律的作用。记 $\operatorname{ad} x\colon y \mapsto [x, y]$，利用反对称性，雅可比恒等式可以改写为

$$
\operatorname{ad} x\,([y, z]) = [\operatorname{ad} x\,(y), z] + [y, \operatorname{ad} x\,(z)],
$$

即 $\operatorname{ad} x$ 对李括号满足 Leibniz 法则（$\operatorname{ad} x$ 是一个导子）。

### 5.1.3. 交换李代数

**定义 5.1.3（交换李代数）** 若对任意 $x, y \in \mathfrak{g}$ 都有 $[x, y] = 0$，则称 $\mathfrak{g}$ 为交换李代数。

任何向量空间配上零括号都是交换李代数，一维李代数必定是交换的。交换李代数是最简单的李代数；一般李代数中 $[x, y]$ 度量了 $x$ 与 $y$ "不可交换"的程度。

## 5.2. 子代数、理想与同态

本节与群论的 2.2、2.6、2.7 节以及环论的 3.2、3.3 节完全平行：子结构、可以作商的子结构、同态与同态基本定理。

### 5.2.1. 子代数

**定义 5.2.1** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{h} \subseteq \mathfrak{g}$ 是线性子空间。若 $\mathfrak{h}$ 在李括号下封闭（即对所有 $x, y \in \mathfrak{h}$，$[x, y] \in \mathfrak{h}$），则称 $\mathfrak{h}$ 是 $\mathfrak{g}$ 的**李子代数**。

### 5.2.2. 理想

**定义 5.2.2** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{i} \subseteq \mathfrak{g}$ 是线性子空间。若对所有 $x \in \mathfrak{g}$ 和 $y \in \mathfrak{i}$ 都有 $[x, y] \in \mathfrak{i}$，则称 $\mathfrak{i}$ 是 $\mathfrak{g}$ 的**理想**，记作 $\mathfrak{i} \triangleleft \mathfrak{g}$。

由反对称性，$[y, x] = -[x, y]$ 也在 $\mathfrak{i}$ 中，因此李代数不必区分左理想和右理想。与群论中的**正规子群**、环论中的理想一样，李代数的理想是构造商结构的基础。两个重要的理想是：

- **中心**（center）$Z(\mathfrak{g}) = \{x \in \mathfrak{g} \mid [x, y] = 0 \text{ 对所有 } y \in \mathfrak{g}\}$；$\mathfrak{g}$ 交换当且仅当 $Z(\mathfrak{g}) = \mathfrak{g}$；
- **导出代数**（derived algebra）$[\mathfrak{g}, \mathfrak{g}]$，即全体 $[x, y]$ 张成的子空间；$\mathfrak{g}$ 交换当且仅当 $[\mathfrak{g}, \mathfrak{g}] = \{0\}$。

**定理 5.2.1** 若 $\mathfrak{i}$ 是李代数 $\mathfrak{g}$ 的理想，则商空间 $\mathfrak{g}/\mathfrak{i}$ 关于运算

$$
[x + \mathfrak{i}, y + \mathfrak{i}] = [x, y] + \mathfrak{i}
$$

构成一个李代数，称为**商李代数**（quotient Lie algebra）。

这里的商空间 $\mathfrak{g}/\mathfrak{i}$ 是加法群 $(\mathfrak{g}, +)$ 关于子群 $\mathfrak{i}$ 的**商群**（定理 2.6.3），数乘规定为 $a(x + \mathfrak{i}) = ax + \mathfrak{i}$，它是一个向量空间，维数为 $\dim \mathfrak{g} - \dim \mathfrak{i}$。括号运算与代表元的选取无关：若 $x' = x + u$，$y' = y + v$（$u, v \in \mathfrak{i}$），则 $[x', y'] - [x, y] = [x, v] + [u, y] + [u, v] \in \mathfrak{i}$。用第 1 章的话说，"$x \sim y \iff x - y \in \mathfrak{i}$"对加法、数乘和李括号都是**同余关系**；双线性、交错性和雅可比恒等式都由 $\mathfrak{g}$ 继承。

### 5.2.3. 李代数同态

**定义 5.2.3** 设 $\mathfrak{g}_1$ 和 $\mathfrak{g}_2$ 是同一域上的李代数，$\varphi\colon \mathfrak{g}_1 \to \mathfrak{g}_2$ 是一个**线性映射**。若对所有 $x, y \in \mathfrak{g}_1$ 有 $\varphi([x, y]_{\mathfrak{g}_1}) = [\varphi(x), \varphi(y)]_{\mathfrak{g}_2}$，则称 $\varphi$ 是**李代数同态**；若 $\varphi$ 还是双射，则称 $\varphi$ 为**李代数同构**。

**定理 5.2.2** 设 $\varphi\colon \mathfrak{g}_1 \to \mathfrak{g}_2$ 是李代数同态，则 $\ker \varphi = \{x \in \mathfrak{g}_1 \mid \varphi(x) = 0\}$ 是 $\mathfrak{g}_1$ 的理想，象 $\varphi(\mathfrak{g}_1)$ 是 $\mathfrak{g}_2$ 的子代数。

**证明**：$\ker \varphi$ 是线性映射的核，因而是子空间。对 $x \in \mathfrak{g}_1$，$y \in \ker \varphi$，有 $\varphi([x, y]) = [\varphi(x), 0] = 0$，故 $[x, y] \in \ker \varphi$。象是子空间，且 $[\varphi(x), \varphi(y)] = \varphi([x, y])$ 仍在象中。 $\square$

**定理 5.2.3（李代数的同态基本定理）** 设 $\varphi\colon \mathfrak{g}_1 \to \mathfrak{g}_2$ 是李代数满同态，则

$$
\mathfrak{g}_1 / \ker \varphi \cong \mathfrak{g}_2,
$$

同构由 $x + \ker \varphi \mapsto \varphi(x)$ 给出。

**证明**：与定理 2.7.7 相同：该映射与代表元无关且是线性双射（这是线性代数中关于商空间的结论，也是加法群的同态基本定理），又 $[x + \ker \varphi, y + \ker \varphi] = [x, y] + \ker \varphi \mapsto \varphi([x, y]) = [\varphi(x), \varphi(y)]$，所以它保持括号。 $\square$

至此，群、环、李代数的"同态—核—商—同态基本定理"这条线索完全一致，它们都是定理 1.4.4 的特例。

## 5.3. 复单李代数的分类（简介）

单群是只有平凡正规子群 $\{e\}$ 与 $G$ 的群，例如素数阶循环群 $\mathbb{Z}_p$ 和**交错群** $A_5$；由同态基本定理，单群没有非平凡的同态象，它们是构造一般群的"原子"。李代数中有完全类似的概念。

**定义 5.3.1（单李代数）** 若李代数 $\mathfrak{g}$ 不是交换的，并且除 $\{0\}$ 和 $\mathfrak{g}$ 外没有其他理想，则称 $\mathfrak{g}$ 是单李代数。

**定义 5.3.2（半单李代数）** 若有限维李代数 $\mathfrak{g}$ 没有非零的交换理想，则称 $\mathfrak{g}$ 是半单李代数。

在特征为 $0$ 的域上，有限维半单李代数恰好是若干个单李代数的直和。单李代数在李代数理论中的地位类似于单群在群论中的地位。

利用根空间分解，有限维复单李代数可以完全分类：每一个都同构于四个无穷系列的**典型李代数**（classical Lie algebra）之一，或五个**例外李代数**（exceptional Lie algebra）$G_2, F_4, E_6, E_7, E_8$（维数分别为 $14, 52, 78, 133, 248$）之一。典型李代数如下表（其中的矩阵李代数见 5.4 节，$\mathfrak{so}(m, \mathbb{C})$ 是 $m$ 阶复反对称矩阵构成的李代数，$\mathfrak{sp}(2l, \mathbb{C})$ 是满足 $X^{\mathsf{T}} J + J X = 0$ 的矩阵构成的李代数，其中 $J = \begin{pmatrix} 0 & I_l \\ -I_l & 0 \end{pmatrix}$）：

| 类型 | 名称 | 矩阵实现 | 维数 |
| :--- | :--- | :--- | :--- |
| $A_l \ (l \ge 1)$ | 特殊线性李代数 | $\mathfrak{sl}(l+1, \mathbb{C})$ | $l(l+2)$ |
| $B_l \ (l \ge 2)$ | 奇数维正交李代数 | $\mathfrak{so}(2l+1, \mathbb{C})$ | $l(2l+1)$ |
| $C_l \ (l \ge 3)$ | 辛李代数 | $\mathfrak{sp}(2l, \mathbb{C})$ | $l(2l+1)$ |
| $D_l \ (l \ge 4)$ | 偶数维正交李代数 | $\mathfrak{so}(2l, \mathbb{C})$ | $l(2l-1)$ |

对 $l$ 的限制是为了避免重复：小秩时有同构 $B_1 \cong C_1 \cong A_1$、$C_2 \cong B_2$、$D_3 \cong A_3$，而 $D_2 = \mathfrak{so}(4, \mathbb{C})$ 不是单李代数（它同构于 $\mathfrak{sl}(2, \mathbb{C}) \oplus \mathfrak{sl}(2, \mathbb{C})$）。

## 5.4. 李代数的例子

### 5.4.1. 三维空间中的叉积

**例 5.4.1** 设 $\mathfrak{g} = \mathbb{R}^3$，定义李括号为向量的叉积：

$$
[\boldsymbol{u}, \boldsymbol{v}] = \boldsymbol{u} \times \boldsymbol{v}.
$$

叉积是双线性的，$\boldsymbol{u} \times \boldsymbol{u} = \boldsymbol{0}$，并满足雅可比恒等式，因此 $(\mathbb{R}^3, \times)$ 构成一个李代数。在标准基下，$[\boldsymbol{e}_1, \boldsymbol{e}_2] = \boldsymbol{e}_3$，$[\boldsymbol{e}_2, \boldsymbol{e}_3] = \boldsymbol{e}_1$，$[\boldsymbol{e}_3, \boldsymbol{e}_1] = \boldsymbol{e}_2$。它就是三维旋转群 $\operatorname{SO}(3)$ 的李代数 $\mathfrak{so}(3)$ 的向量形式（见例 5.4.4 与 5.5 节）：$\boldsymbol{u}$ 表示绕轴 $\boldsymbol{u}$ 的无穷小旋转，叉积刻画了两个无穷小旋转的不可交换性。

### 5.4.2. 矩阵李代数

**例 5.4.2** 设 $\mathfrak{gl}(n, F)$ 为域 $F$ 上所有 $n \times n$ 矩阵的集合，定义李括号为矩阵的**换位子**

$$
[A, B] = AB - BA,
$$

则 $(\mathfrak{gl}(n, F), [\cdot\,, \cdot])$ 是一个李代数，称为**一般线性李代数**（general linear Lie algebra），是矩阵李代数的典型例子。雅可比恒等式可以直接展开验证：$[A, [B, C]] + [B, [C, A]] + [C, [A, B]]$ 展开后的十二项两两抵消。一般地，任何结合代数（如环 $\operatorname{End}(V)$）配上换位子都成为李代数；$\operatorname{End}(V)$ 配上换位子记作 $\mathfrak{gl}(V)$。

**例 5.4.3** 迹为零的矩阵的集合

$$
\mathfrak{sl}(n, F) = \{A \in \mathfrak{gl}(n, F) \mid \operatorname{tr}(A) = 0\}
$$

是 $\mathfrak{gl}(n, F)$ 的子代数，称为**特殊线性李代数**（special linear Lie algebra）。事实上，由 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ 知任意换位子的迹都为零，所以 $\mathfrak{sl}(n, F)$ 甚至是 $\mathfrak{gl}(n, F)$ 的理想。它是迹映射 $\operatorname{tr}\colon \mathfrak{gl}(n, F) \to F$ 的核（把 $F$ 看作一维交换李代数，$\operatorname{tr}$ 是李代数同态），由定理 5.2.3，$\mathfrak{gl}(n, F)/\mathfrak{sl}(n, F) \cong F$。

**例 5.4.4** 三维旋转群 $\operatorname{SO}(3)$ 对应的李代数 $\mathfrak{so}(3)$ 由所有 $3 \times 3$ 实反对称矩阵构成，李括号为矩阵换位子。映射

$$
\boldsymbol{u} = (u_1, u_2, u_3) \mapsto \hat{u} = \begin{pmatrix} 0 & -u_3 & u_2 \\ u_3 & 0 & -u_1 \\ -u_2 & u_1 & 0 \end{pmatrix}
$$

满足 $\hat{u}\boldsymbol{v} = \boldsymbol{u} \times \boldsymbol{v}$ 和 $[\hat{u}, \hat{v}] = \widehat{\boldsymbol{u} \times \boldsymbol{v}}$，因此是 $(\mathbb{R}^3, \times)$ 到 $\mathfrak{so}(3)$ 的李代数同构：矩阵形式和叉积形式可以相互转换。

**例 5.4.5** $\mathfrak{sl}(2, F)$ 是三维的，取基

$$
e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

直接计算得

$$
[h, e] = 2e, \qquad [h, f] = -2f, \qquad [e, f] = h.
$$

即 $e$、$f$ 都是 $\operatorname{ad} h$ 的特征向量（特征值 $2$ 与 $-2$）。当 $F = \mathbb{C}$ 时，$\mathfrak{sl}(2, \mathbb{C})$ 是最小的单李代数（表中的 $A_1$），它的表示论（例 6.2.2）是整个理论的原型。

## 5.5. 李群与李代数

本节说明李代数是怎样从连续群中产生的。为避免微分几何，只讨论由矩阵构成的群。

### 5.5.1. 矩阵指数

对 $X \in M_n(\mathbb{C})$，定义**矩阵指数**（matrix exponential）

$$
\mathrm{e}^X = \exp(X) = \sum_{k=0}^{\infty} \frac{X^k}{k!} = I + X + \frac{X^2}{2!} + \cdots,
$$

该级数对任意 $X$ 都收敛。它有以下性质（与实数的指数函数对照，区别在于需要可交换的条件）：

**定理 5.5.1** 对任意 $X, Y \in M_n(\mathbb{C})$ 和可逆矩阵 $P$：

1. 若 $XY = YX$，则 $\mathrm{e}^{X+Y} = \mathrm{e}^X \mathrm{e}^Y$；特别地 $\mathrm{e}^X$ 可逆，$(\mathrm{e}^X)^{-1} = \mathrm{e}^{-X}$；
2. $\mathrm{e}^{PXP^{-1}} = P \mathrm{e}^X P^{-1}$；
3. $\det(\mathrm{e}^X) = \mathrm{e}^{\operatorname{tr} X}$；
4. $t \mapsto \mathrm{e}^{tX}$ 是 $(\mathbb{R}, +)$ 到 $\operatorname{GL}(n, \mathbb{C})$ 的群同态，并且 $\dfrac{\mathrm{d}}{\mathrm{d}t} \mathrm{e}^{tX} = X \mathrm{e}^{tX}$。

性质 4 说明 $\{e^{tX} \mid t \in \mathbb{R}\}$ 是一个子群，称为由 $X$ 生成的**单参数子群**（one-parameter subgroup），$X$ 是它在 $t = 0$ 处的"速度"。性质 3 可以借助 Jordan 标准形（[线性代数](/2.1.10#thm-10.9.2)）和性质 2 证明：上三角矩阵的指数仍是上三角的，对角元为 $\mathrm{e}^{\lambda_i}$。

### 5.5.2. 矩阵李群

**定义 5.5.1（矩阵李群）** 设 $G$ 是**一般线性群** $\operatorname{GL}(n, \mathbb{C})$ 的子群。若 $G$ 中的任意矩阵序列只要收敛到一个可逆矩阵 $A$，就有 $A \in G$，则称 $G$ 是一个矩阵李群。

常见的矩阵李群有：

- $\operatorname{GL}(n, \mathbb{R})$；$\operatorname{SL}(n, \mathbb{R}) = \{A \mid \det A = 1\}$（它是 $\det$ 的核，见 2.7.5 节）；
- 正交群 $\operatorname{O}(n) = \{R \in M_n(\mathbb{R}) \mid R^{\mathsf{T}} R = I\}$ 与特殊正交群 $\operatorname{SO}(n) = \{R \in \operatorname{O}(n) \mid \det R = 1\}$（正交矩阵见[线性代数](/2.1.4#def-4.3.1)）；$\operatorname{SO}(3)$ 就是三维空间中全体绕原点的旋转；
- 酉群 $\operatorname{U}(n) = \{U \in M_n(\mathbb{C}) \mid U^{\mathsf H} U = I\}$ 与 $\operatorname{SU}(n) = \{U \in \operatorname{U}(n) \mid \det U = 1\}$。

这些群都是无限群，但只依赖有限个连续参数，例如 $\operatorname{SO}(3)$ 中的旋转由转轴方向（$2$ 个参数）和转角（$1$ 个参数）决定。

**定义 5.5.2** 矩阵李群 $G$ 的李代数是

$$
\mathfrak{g} = \{X \in M_n(\mathbb{C}) \mid \mathrm{e}^{tX} \in G \text{ 对所有 } t \in \mathbb{R} \text{ 成立}\},
$$

即 $G$ 中全体单参数子群的"速度"。

**定理 5.5.2** 矩阵李群 $G$ 的李代数 $\mathfrak{g}$ 是实向量空间，并且对换位子封闭，因而是 $\mathfrak{gl}(n, \mathbb{C})$（看作实李代数）的李子代数。

**证明**（要点）：数乘封闭是显然的。加法封闭由 Lie 乘积公式 $\mathrm{e}^{X+Y} = \lim_{m \to \infty} (\mathrm{e}^{X/m} \mathrm{e}^{Y/m})^m$ 和定义 5.5.1 中的闭性得到。对括号，设 $X, Y \in \mathfrak{g}$，由定理 5.5.1 的性质 2，$\mathrm{e}^{s \cdot \mathrm{e}^{tX} Y \mathrm{e}^{-tX}} = \mathrm{e}^{tX} \mathrm{e}^{sY} \mathrm{e}^{-tX} \in G$，所以 $\mathrm{e}^{tX} Y \mathrm{e}^{-tX} \in \mathfrak{g}$ 对所有 $t$ 成立；它对 $t$ 的导数在 $t = 0$ 处为 $XY - YX$，而子空间中曲线的导数仍在该子空间中，故 $[X, Y] \in \mathfrak{g}$。 $\square$

李括号与群的不可交换性的关系可以从下面的展开式看出：对很小的 $t$，

$$
\mathrm{e}^{tX} \mathrm{e}^{tY} \mathrm{e}^{-tX} \mathrm{e}^{-tY} = I + t^2 [X, Y] + O(t^3).
$$

左边是群中的"换位子" $aba^{-1}b^{-1}$，它等于 $I$ 当且仅当 $a$ 与 $b$ 可交换；右边的二阶项正是李括号。

利用定理 5.5.1 可以算出前面例子的来源：

- $\operatorname{GL}(n, \mathbb{R})$ 的李代数是 $\mathfrak{gl}(n, \mathbb{R})$；
- 由 $\det(\mathrm{e}^{tX}) = \mathrm{e}^{t \operatorname{tr} X}$，$\operatorname{SL}(n, \mathbb{R})$ 的李代数是 $\mathfrak{sl}(n, \mathbb{R})$；
- 由 $(\mathrm{e}^{tX})^{\mathsf{T}} \mathrm{e}^{tX} = I$ 对所有 $t$ 成立当且仅当 $X^{\mathsf{T}} = -X$（在 $t = 0$ 处求导得必要性，充分性由 $(\mathrm{e}^{tX})^{\mathsf{T}} = \mathrm{e}^{tX^{\mathsf{T}}} = \mathrm{e}^{-tX}$ 得到），$\operatorname{O}(n)$ 与 $\operatorname{SO}(n)$ 的李代数都是反对称矩阵构成的 $\mathfrak{so}(n)$。

$\dim \mathfrak{so}(3) = 3$，这与 $\operatorname{SO}(3)$ 有 $3$ 个连续参数相吻合：李代数的维数就是李群的参数个数。

**例 5.5.1** 设 $\boldsymbol{u}$ 是单位向量，$\hat{u}$ 如例 5.4.4，则 $\hat{u}^3 = -\hat{u}$，由级数直接求和得 **Rodrigues 公式**（Rodrigues' rotation formula）

$$
\mathrm{e}^{\theta \hat{u}} = I + \sin\theta\, \hat{u} + (1 - \cos\theta)\, \hat{u}^2,
$$

它正是绕轴 $\boldsymbol{u}$ 转角 $\theta$ 的旋转矩阵。因此 $\mathfrak{so}(3)$ 中的一个向量 $\theta\boldsymbol{u}$（"旋转向量"）通过指数映射给出一个旋转，而且每个旋转都可以这样得到。分子模拟和结构生物学中常用旋转向量或单位四元数（与 $\operatorname{SU}(2)$ 对应）来参数化分子的取向，正是基于这一事实。

**例 5.5.2** 三维空间的刚体运动 $\boldsymbol{x} \mapsto R\boldsymbol{x} + \boldsymbol{t}$（$R \in \operatorname{SO}(3)$，$\boldsymbol{t} \in \mathbb{R}^3$）构成群 $\operatorname{SE}(3)$。用齐次坐标 $(\boldsymbol{x}, 1)$ 可以把它写成 $4$ 阶矩阵

$$
\begin{pmatrix} R & \boldsymbol{t} \\ \boldsymbol{0}^{\mathsf{T}} & 1 \end{pmatrix},
$$

于是 $\operatorname{SE}(3)$ 是 $\operatorname{GL}(4, \mathbb{R})$ 的矩阵李群，其李代数由 $\begin{pmatrix} \hat{\omega} & \boldsymbol{v} \\ \boldsymbol{0}^{\mathsf{T}} & 0 \end{pmatrix}$（$\boldsymbol{\omega}, \boldsymbol{v} \in \mathbb{R}^3$）构成，维数为 $6$，对应刚体的 $3$ 个转动自由度和 $3$ 个平动自由度。分子对接要在 $\operatorname{SE}(3)$ 中搜索配体相对受体的位姿；AlphaFold2 等蛋白质结构模型把每个残基的主链表示为一个局部坐标系，也就是 $\operatorname{SE}(3)$ 的一个元素。

## 本章小结

| 主题 | 核心概念 |
|------|----------|
| 定义 | 域上的向量空间，李括号的双线性、交错性、雅可比恒等式，反对称性，$\operatorname{ad} x$ 是导子 |
| 子结构与同态 | 李子代数、理想（中心、导出代数）、商李代数、李代数同态、核是理想、同态基本定理 |
| 分类 | 单李代数、半单李代数，复单李代数的典型系列 $A_l, B_l, C_l, D_l$ 与例外李代数 |
| 例子 | 叉积 $(\mathbb{R}^3, \times) \cong \mathfrak{so}(3)$，$\mathfrak{gl}(n, F)$，$\mathfrak{sl}(n, F)$，$\mathfrak{sl}(2, F)$ 的基 $e, f, h$ |
| 李群 | 矩阵指数，单参数子群，矩阵李群（$\operatorname{GL}$、$\operatorname{SL}$、$\operatorname{O}(n)$、$\operatorname{SO}(n)$、$\operatorname{SE}(3)$），李群的李代数，群换位子与李括号 |

本章看到，旋转群 $\operatorname{SO}(3)$ 本来就是由矩阵构成的，群运算就是矩阵乘法；$\mathfrak{so}(3)$ 也是矩阵，括号就是换位子。下一章把这种"用矩阵实现"的做法推广到任意群和李代数：一个表示就是到 $\operatorname{GL}(V)$ 或 $\mathfrak{gl}(V)$ 的同态。
