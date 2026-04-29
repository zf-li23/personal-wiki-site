李代数是一个同时具备向量空间结构和满足特定恒等式的双线性映射的代数结构。它由挪威数学家索菲斯·李在19世纪后期研究**连续变换群**（即李群）时提出，本质上是李群在单位元处的**线性化逼近**。

李代数与**李群**的关系是核心桥梁：李群描述整体的、光滑的、连续的对称变换；李代数则描述该对称性在无穷小意义下的局部的“切空间”行为。两者通过**指数映射**连接，类似于李群论中指明的对应关系。

## 5.1. 李代数的定义

### 5.1.1. 向量空间

**定义 5.1.1** 设 $\mathbb{F}$ 是一个域（通常取 $\mathbb{F} = \mathbb{R}$ 或 $\mathbb{C}$），$(V, +, \cdot)$ 是一个 $\mathbb{F}$-向量空间，定义了向量加法与标量乘法。其元素 $x, y, z, \dots$ 可以是几何向量、矩阵、微分算子或函数空间中的抽象元素。

### 5.1.2. 李括号

**定义 5.1.2** 在域 $\mathbb{F}$ 上的向量空间 $\mathfrak{g}$ 中，若定义了运算 $[\,\cdot\, , \cdot\,] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$（称为**李括号**），满足以下三个公理，则称 $\mathfrak{g}$ 是一个**李代数**：

1. **双线性**：对任意 $x, y, z \in \mathfrak{g}$ 和 $a, b \in \mathbb{F}$，
   $$
   [ax + by, z] = a[x, z] + b[y, z], \quad [x, ay + bz] = a[x, y] + b[x, z].
   $$
2. **反交换性**：对任意 $x \in \mathfrak{g}$，
   $$
   [x, x] = 0.
   $$
   由此可推出反对称性 $[x, y] = -[y, x]$（当域特征不为 $2$ 时）。
3. **雅可比恒等式**：对任意 $x, y, z \in \mathfrak{g}$，
   $$
   [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
   $$
   雅可比恒等式可以理解为将李括号视为一种“导子”时的结合律替代品——它本质上是要求 ad 算子满足莱布尼兹法则。

### 5.1.3. 交换李代数

- 若对任意 $x, y \in \mathfrak{g}$ 都有 $[x, y] = 0$，则 $\mathfrak{g}$ 称为**交换李代数**。交换意味着所有的生成元彼此间没有“非对易性”的相互作用，是最简单的李代数。

## 5.2. 子代数、理想与同态

### 5.2.1. 子代数

**定义 5.2.1** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{h} \subseteq \mathfrak{g}$ 是线性子空间。若 $\mathfrak{h}$ 在李括号下封闭（即对所有 $x, y \in \mathfrak{h}$，$[x, y] \in \mathfrak{h}$），则称 $\mathfrak{h}$ 是 $\mathfrak{g}$ 的**李子代数**。

### 5.2.2. 理想

**定义 5.2.2** 设 $\mathfrak{g}$ 是李代数，$\mathfrak{i} \subseteq \mathfrak{g}$ 是线性子空间。若对所有 $x \in \mathfrak{g}$ 和 $y \in \mathfrak{i}$ 都有 $[x, y] \in \mathfrak{i}$，则称 $\mathfrak{i}$ 是 $\mathfrak{g}$ 的**理想**。与群论中正规子群和环论中理想的定义类似，李代数理想也是构建商结构的基础。

**定理 5.2.1** 若 $\mathfrak{i}$ 是李代数 $\mathfrak{g}$ 的理想，则商空间 $\mathfrak{g}/\mathfrak{i}$ 关于如下运算构成一个李代数：
$$
[x + \mathfrak{i}, y + \mathfrak{i}] = [x, y] + \mathfrak{i},
$$
称为**商李代数**。

### 5.2.3. 李代数同态

**定义 5.2.3** 设 $\mathfrak{g}_1$ 和 $\mathfrak{g}_2$ 是李代数，$\varphi: \mathfrak{g}_1 \to \mathfrak{g}_2$ 是一个线性映射。若对所有 $x, y \in \mathfrak{g}_1$ 有：
$$
\varphi([x, y]_{\mathfrak{g}_1}) = [\varphi(x), \varphi(y)]_{\mathfrak{g}_2},
$$
则称 $\varphi$ 是**李代数同态**。若 $\varphi$ 是双射，则称 $\varphi$ 为**李代数同构**。

## 5.3. 典型复半单李代数的分类

如果李代数没有非平凡的可交换理想，则称为半单李代数。这一概念类似群论中的单群和环论中的本原环，是对“不可分解的结构”的形式化抽象。所有**有限维复半单李代数**可以通过根空间分解为四类**典型李代数**和五个**例外李代数**。下表给出典型李代数的分类：

| 类型 | 符号 | 简图 | 常用表示 / 例子 |
| :--- | :--- | :--- | :--- |
| 特殊线性代数 | $A_l \ (l \ge 1)$ | $A_l$ 型 Dynkin 图 | $\mathfrak{sl}(l+1, \mathbb{C})$ |
| 特殊正交代数 | $B_l \ (l \ge 2)$ | $B_l$ 型 Dynkin 图 | $\mathfrak{so}(2l+1, \mathbb{C})$ |
| 辛代数 | $C_l \ (l \ge 3)$ | $C_l$ 型 Dynkin 图 | $\mathfrak{sp}(2l, \mathbb{C})$ |
| 偶数维正交代数 | $D_l \ (l \ge 4)$ | $D_l$ 型 Dynkin 图 | $\mathfrak{so}(2l, \mathbb{C})$ |

## 5.4. 李代数的例子

### 5.4.1. 三维空间中的叉积

**例 5.4.1** 设 $\mathfrak{g} = \mathbb{R}^3$，定义李括号为向量**叉积**运算：
$$
[\boldsymbol{u}, \boldsymbol{v}] = \boldsymbol{u} \times \boldsymbol{v}.
$$
可以验证叉积满足双线性、$[\boldsymbol{u}, \boldsymbol{u}] = \boldsymbol{0}$ 和雅可比恒等式，因此 $(\mathbb{R}^3, \times)$ 构成一个李代数。叉积与三维旋转群 $SO(3)$ 有密切联系，恰好是三维旋转的李代数 $\mathfrak{so}(3)$ 在向量意义下的直观几何原型，描述无穷小旋转的可交换程度。

### 5.4.2. 矩阵李代数

**例 5.4.2** 设 $\mathfrak{gl}(n, \mathbb{F})$ 为域 $\mathbb{F}$ 上所有 $n \times n$ 矩阵的集合，定义李括号为矩阵的**换位子**：
$$
[A, B] = AB - BA.
$$
则 $(\mathfrak{gl}(n, \mathbb{F}), [\cdot, \cdot])$ 是一个李代数，称为**一般线性李代数**，是矩阵李代数的典型例子。

**例 5.4.3** 设 $\mathfrak{sl}(n, \mathbb{F}) = \{A \in \mathfrak{gl}(n, \mathbb{F}) \mid \operatorname{tr}(A) = 0\}$（迹为零的矩阵）构成 $\mathfrak{gl}(n, \mathbb{F})$ 的子代数，称为**特殊线性李代数**。

**例 5.4.4** 三维旋转群 $SO(3)$ 对应的李代数 $\mathfrak{so}(3)$ 由所有 $3 \times 3$ 反对称实矩阵构成，其李括号为矩阵换位子。$\mathfrak{so}(3)$ 与 $(\mathbb{R}^3, \times)$ 同构，证明了矩阵形式和叉积形式可以相互转换。
