---
title: 李代数
---

李代数是带有一个满足特定恒等式的双线性运算（李括号）的向量空间。它源于挪威数学家 Sophus Lie 在 19 世纪 70 年代对**连续变换群**（今称李群）的研究：李群在单位元处的切空间自然地带有李代数结构，因此李代数可以看作李群的**线性化**。

李群描述整体的、光滑的连续对称；李代数描述这种对称在无穷小意义下的行为。两者通过**指数映射** $\exp: \mathfrak{g} \to G$ 联系起来（例如矩阵李群中 $\exp(X) = \sum_{k \ge 0} X^k / k!$），李群的许多问题因此可以化为李代数上的线性代数问题。

## 5.1. 李代数的定义

### 5.1.1. 向量空间

**定义 5.1.1** 设 $\mathbb{F}$ 是一个域（通常取 $\mathbb{R}$ 或 $\mathbb{C}$）。集合 $V$ 连同加法 $V \times V \to V$ 和数乘 $\mathbb{F} \times V \to V$ 称为 $\mathbb{F}$ 上的**向量空间**，如果 $(V, +)$ 是交换群，且对任意 $a, b \in \mathbb{F}$，$x, y \in V$ 有

$$
a(x + y) = ax + ay, \quad (a + b)x = ax + bx, \quad (ab)x = a(bx), \quad 1x = x.
$$

向量空间的元素可以是几何向量、矩阵、微分算子或函数等。

### 5.1.2. 李括号

**定义 5.1.2（李代数）** 设 $\mathfrak{g}$ 是域 $\mathbb{F}$ 上的向量空间。若在 $\mathfrak{g}$ 上定义了运算 $[\cdot\,, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$（称为**李括号**），满足以下三条公理，则称 $\mathfrak{g}$ 是一个李代数：

1. **双线性**：对任意 $x, y, z \in \mathfrak{g}$ 和 $a, b \in \mathbb{F}$，
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

由交错性和双线性可推出**反对称性** $[x, y] = -[y, x]$：展开 $0 = [x + y, x + y] = [x, y] + [y, x]$ 即得，这对任何特征的域都成立。反过来，若域的特征不为 $2$，则由反对称性得 $[x, x] = -[x, x]$，从而 $[x, x] = 0$，两条公理等价。

李括号一般不满足结合律，雅可比恒等式起着替代结合律的作用。记 $\operatorname{ad} x: y \mapsto [x, y]$，利用反对称性，雅可比恒等式可以改写为

$$
\operatorname{ad} x\,([y, z]) = [\operatorname{ad} x\,(y), z] + [y, \operatorname{ad} x\,(z)],
$$

即 $\operatorname{ad} x$ 对李括号满足 Leibniz 法则（$\operatorname{ad} x$ 是一个导子）。

### 5.1.3. 交换李代数

**定义 5.1.3（交换李代数）** 若对任意 $x, y \in \mathfrak{g}$ 都有 $[x, y] = 0$，则称 $\mathfrak{g}$ 为交换李代数。

任何向量空间配上零括号都是交换李代数，一维李代数必定是交换的。交换李代数是最简单的李代数；一般李代数中 $[x, y]$ 度量了 $x$ 与 $y$ "不可交换"的程度。

## 5.2. 子代数、理想与同态

### 5.2.1. 子代数

**定义 5.2.1** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{h} \subseteq \mathfrak{g}$ 是线性子空间。若 $\mathfrak{h}$ 在李括号下封闭（即对所有 $x, y \in \mathfrak{h}$，$[x, y] \in \mathfrak{h}$），则称 $\mathfrak{h}$ 是 $\mathfrak{g}$ 的**李子代数**。

### 5.2.2. 理想

**定义 5.2.2** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{i} \subseteq \mathfrak{g}$ 是线性子空间。若对所有 $x \in \mathfrak{g}$ 和 $y \in \mathfrak{i}$ 都有 $[x, y] \in \mathfrak{i}$，则称 $\mathfrak{i}$ 是 $\mathfrak{g}$ 的**理想**。

由反对称性，$[y, x] = -[x, y]$ 也在 $\mathfrak{i}$ 中，因此李代数不必区分左理想和右理想。与群论中的正规子群、环论中的理想一样，李代数的理想是构造商结构的基础。

**定理 5.2.1** 若 $\mathfrak{i}$ 是李代数 $\mathfrak{g}$ 的理想，则商空间 $\mathfrak{g}/\mathfrak{i}$ 关于运算

$$
[x + \mathfrak{i}, y + \mathfrak{i}] = [x, y] + \mathfrak{i}
$$

构成一个李代数，称为**商李代数**。

该运算与代表元的选取无关：若 $x' = x + u$，$y' = y + v$（$u, v \in \mathfrak{i}$），则 $[x', y'] - [x, y] = [x, v] + [u, y] + [u, v] \in \mathfrak{i}$。

### 5.2.3. 李代数同态

**定义 5.2.3** 设 $\mathfrak{g}_1$ 和 $\mathfrak{g}_2$ 是同一域上的李代数，$\varphi: \mathfrak{g}_1 \to \mathfrak{g}_2$ 是一个线性映射。若对所有 $x, y \in \mathfrak{g}_1$ 有

$$
\varphi([x, y]_{\mathfrak{g}_1}) = [\varphi(x), \varphi(y)]_{\mathfrak{g}_2},
$$

则称 $\varphi$ 是**李代数同态**。若 $\varphi$ 还是双射，则称 $\varphi$ 为**李代数同构**。

## 5.3. 复单李代数的分类

不是交换李代数、并且除 $\{0\}$ 和自身外没有其他理想的李代数称为**单李代数**；没有非零交换理想的有限维李代数称为**半单李代数**。在特征为 $0$ 的域上，有限维半单李代数恰好是若干个单李代数的直和。单李代数在李代数理论中的地位类似于单群在群论中的地位。

利用根空间分解，有限维复单李代数可以完全分类：每一个都同构于四个无穷系列的**典型李代数**之一，或五个**例外李代数** $G_2, F_4, E_6, E_7, E_8$（维数分别为 $14, 52, 78, 133, 248$）之一。典型李代数如下表（其中的矩阵李代数见 5.4 节）：

| 类型 | 名称 | 矩阵实现 | 维数 |
| :--- | :--- | :--- | :--- |
| $A_l \ (l \ge 1)$ | 特殊线性李代数 | $\mathfrak{sl}(l+1, \mathbb{C})$ | $l(l+2)$ |
| $B_l \ (l \ge 2)$ | 奇数维正交李代数 | $\mathfrak{so}(2l+1, \mathbb{C})$ | $l(2l+1)$ |
| $C_l \ (l \ge 3)$ | 辛李代数 | $\mathfrak{sp}(2l, \mathbb{C})$ | $l(2l+1)$ |
| $D_l \ (l \ge 4)$ | 偶数维正交李代数 | $\mathfrak{so}(2l, \mathbb{C})$ | $l(2l-1)$ |

对 $l$ 的限制是为了避免重复：小秩时有同构 $B_1 \cong C_1 \cong A_1$、$C_2 \cong B_2$、$D_3 \cong A_3$，而 $D_2 = \mathfrak{so}(4, \mathbb{C})$ 不是单李代数。

## 5.4. 李代数的例子

### 5.4.1. 三维空间中的叉积

**例 5.4.1** 设 $\mathfrak{g} = \mathbb{R}^3$，定义李括号为向量的**叉积**：

$$
[\boldsymbol{u}, \boldsymbol{v}] = \boldsymbol{u} \times \boldsymbol{v}.
$$

叉积是双线性的，$\boldsymbol{u} \times \boldsymbol{u} = \boldsymbol{0}$，并满足雅可比恒等式，因此 $(\mathbb{R}^3, \times)$ 构成一个李代数。它就是三维旋转群 $SO(3)$ 的李代数 $\mathfrak{so}(3)$ 的向量形式（见例 5.4.4）：$\boldsymbol{u}$ 表示绕轴 $\boldsymbol{u}$ 的无穷小旋转，叉积刻画了两个无穷小旋转的不可交换性。

### 5.4.2. 矩阵李代数

**例 5.4.2** 设 $\mathfrak{gl}(n, \mathbb{F})$ 为域 $\mathbb{F}$ 上所有 $n \times n$ 矩阵的集合，定义李括号为矩阵的**换位子**

$$
[A, B] = AB - BA,
$$

则 $(\mathfrak{gl}(n, \mathbb{F}), [\cdot\,, \cdot])$ 是一个李代数，称为**一般线性李代数**，是矩阵李代数的典型例子。一般地，任何结合代数配上换位子都成为李代数。

**例 5.4.3** 迹为零的矩阵的集合

$$
\mathfrak{sl}(n, \mathbb{F}) = \{A \in \mathfrak{gl}(n, \mathbb{F}) \mid \operatorname{tr}(A) = 0\}
$$

是 $\mathfrak{gl}(n, \mathbb{F})$ 的子代数，称为**特殊线性李代数**。事实上，由 $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ 知任意换位子的迹都为零，所以 $\mathfrak{sl}(n, \mathbb{F})$ 甚至是 $\mathfrak{gl}(n, \mathbb{F})$ 的理想。

**例 5.4.4** 三维旋转群 $SO(3)$ 对应的李代数 $\mathfrak{so}(3)$ 由所有 $3 \times 3$ 实反对称矩阵构成，李括号为矩阵换位子。映射

$$
\boldsymbol{u} = (u_1, u_2, u_3) \mapsto \hat{u} = \begin{pmatrix} 0 & -u_3 & u_2 \\ u_3 & 0 & -u_1 \\ -u_2 & u_1 & 0 \end{pmatrix}
$$

满足 $\hat{u}\boldsymbol{v} = \boldsymbol{u} \times \boldsymbol{v}$ 和 $[\hat{u}, \hat{v}] = \widehat{\boldsymbol{u} \times \boldsymbol{v}}$，因此是 $(\mathbb{R}^3, \times)$ 到 $\mathfrak{so}(3)$ 的李代数同构：矩阵形式和叉积形式可以相互转换。
