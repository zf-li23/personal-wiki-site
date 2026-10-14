---
title: 表示论
---

**表示论**（representation theory）把前几章的群、李代数等抽象代数结构"表示"为具体向量空间上的线性变换（选定基后即为矩阵），从而把结构问题转化为**线性代数**问题。在量子力学中，粒子的状态由 Hilbert 空间中的向量描述，对称性由群在这个空间上的作用描述，表示论因此成为连接对称性与可观测量（算子的谱）的数学框架。

抽象地看，一个表示就是从一个代数结构到"向量空间 $V$ 上线性变换所成的同类结构"的同态：群表示是到可逆线性变换群 $\operatorname{GL}(V)$ 的群同态，李代数表示是到一般线性李代数 $\mathfrak{gl}(V)$ 的李代数同态。

## 6.1. 群表示

### 6.1.1. 群表示的定义

**定义 6.1.1** 设 $G$ 是一个群，$V$ 是域 $\mathbb{F}$ 上的向量空间，$\operatorname{GL}(V)$ 是 $V$ 上所有可逆线性变换关于合成构成的群（$V$ 的**一般线性群**）。群同态 $\rho: G \to \operatorname{GL}(V)$ 称为 $G$ 在 $V$ 上的一个（线性）**表示**，$V$ 称为**表示空间**，$V$ 的维数称为该表示的**维数**。

当 $V$ 是 $n$ 维空间时，取定一组基后，$\operatorname{GL}(V)$ 中的元素就是 $n$ 阶可逆矩阵，于是表示 $\rho$ 把 $G$ 的每个元素对应到一个可逆矩阵。同态条件 $\rho(gh) = \rho(g)\rho(h)$ 保证了群运算与矩阵乘法一致。

**定义 6.1.2** 设 $G$ 是群，$V$ 是域 $\mathbb{F}$ 上的向量空间。若给定映射 $G \times V \to V$，$(g, v) \mapsto g \cdot v$，使得对任意 $g, h \in G$，$v, w \in V$，$\lambda, \mu \in \mathbb{F}$ 满足：

1. **线性性**：$g \cdot (\lambda v + \mu w) = \lambda(g \cdot v) + \mu(g \cdot w)$（即每个 $g$ 给出 $V$ 上的一个线性变换）；
2. **相容性**：$g \cdot (h \cdot v) = (gh) \cdot v$；
3. **单位性**：$e \cdot v = v$，

则称 $G$ **线性作用**于 $V$。

线性作用与表示是同一件事的两种说法：令 $\rho(g)(v) = g \cdot v$，条件 2、3 保证 $\rho(g)$ 可逆（逆为 $\rho(g^{-1})$）且 $\rho$ 是群同态；反之，由表示 $\rho$ 令 $g \cdot v = \rho(g)(v)$ 就得到线性作用。

### 6.1.2. 等价表示、不变子空间与不可约表示

**定义 6.1.3** 设 $\rho_1: G \to \operatorname{GL}(V_1)$ 和 $\rho_2: G \to \operatorname{GL}(V_2)$ 是群 $G$ 的两个表示。若存在线性同构 $\varphi: V_1 \to V_2$，使得对任意 $g \in G$ 有 $\varphi \circ \rho_1(g) = \rho_2(g) \circ \varphi$，则称这两个表示是**等价**的。在有限维情形下取定基，这意味着存在同一个可逆矩阵 $P$，使得对所有 $g$ 都有 $\rho_2(g) = P\rho_1(g)P^{-1}$。

**定义 6.1.4（不可约表示）** 设 $\rho: G \to \operatorname{GL}(V)$ 是表示。若子空间 $W \subseteq V$ 满足对所有 $g \in G$ 有 $\rho(g)W \subseteq W$，则称 $W$ 是**不变子空间**。若 $V \neq \{0\}$ 且除 $\{0\}$ 和 $V$ 外没有其他不变子空间，则称该表示是不可约表示；否则（$V$ 有非平凡的不变子空间）称为**可约**的。

不可约表示是构造一般表示的基本单元。例如对有限群 $G$，若域 $\mathbb{F}$ 的特征不整除 $|G|$（如 $\mathbb{F} = \mathbb{C}$），则 Maschke 定理保证 $G$ 的任何有限维表示都是若干不可约表示的直和。

## 6.2. 李代数表示

把李代数的元素对应为向量空间上的线性变换，就得到李代数的表示。思想与群表示相同，只是同态条件换成保持李括号。

**定义 6.2.1** 设 $\mathfrak{g}$ 是域 $\mathbb{F}$ 上的李代数，$V$ 是 $\mathbb{F}$ 上的向量空间，$\mathfrak{gl}(V)$ 是 $V$ 上全体线性变换关于 $[X, Y] = XY - YX$ 构成的李代数。李代数同态 $\pi: \mathfrak{g} \to \mathfrak{gl}(V)$ 称为 $\mathfrak{g}$ 在 $V$ 上的一个**表示**，即 $\pi$ 是线性映射，且 $\pi([x, y]) = \pi(x)\pi(y) - \pi(y)\pi(x)$。

**例 6.2.1（伴随表示）** 对任意李代数 $\mathfrak{g}$，定义映射 $\operatorname{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ 为

$$
\operatorname{ad}(x)(y) = [x, y], \quad \forall x, y \in \mathfrak{g}.
$$

则 $\operatorname{ad}$ 是李代数同态，称为 $\mathfrak{g}$ 的**伴随表示**。事实上，对任意 $z \in \mathfrak{g}$，

$$
\operatorname{ad}([x, y])(z) = [[x, y], z], \qquad [\operatorname{ad}(x), \operatorname{ad}(y)](z) = [x, [y, z]] - [y, [x, z]],
$$

两者相等恰好就是雅可比恒等式。也就是说，雅可比恒等式等价于 $\operatorname{ad}$ 保持李括号。

## 6.3. 李群表示与李代数表示的关系

李群 $G$ 的表示经过微分得到其李代数 $\mathfrak{g}$ 的表示；反过来，李代数的表示通过指数映射可以（至少局部地）提升为李群的表示，当 $G$ 单连通时可以提升为整个 $G$ 的表示。

**定理 6.3.1** 设 $G$ 是李群，$\rho: G \to \operatorname{GL}(V)$ 是 $G$ 在有限维空间 $V$ 上的（光滑）表示，则

$$
\mathrm{d}\rho(X) = \left.\frac{\mathrm{d}}{\mathrm{d}t}\right|_{t=0} \rho(\exp(tX)), \quad X \in \mathfrak{g}
$$

定义了李代数的表示 $\mathrm{d}\rho: \mathfrak{g} \to \mathfrak{gl}(V)$，并且 $\rho(\exp(X)) = \exp(\mathrm{d}\rho(X))$，即群表示与指数映射交换。

这体现了李代数作为"线性近似"的价值：它把李群上的非线性问题化为李代数上的线性代数问题，是数学物理中最常用的技巧之一。例如物理学中通过旋转群 $SO(3)$ 的李代数 $\mathfrak{so}(3)$ 的表示来分类角动量（半整数自旋对应于 $SO(3)$ 的二重覆盖 $SU(2)$ 的表示）。

## 6.4. 特征标与正交关系

特征标是群表示最重要的不变量，它由表示矩阵的迹给出。

**定义 6.4.1** 设 $\rho: G \to \operatorname{GL}(V)$ 是有限群 $G$ 在有限维向量空间 $V$ 上的表示。函数 $\chi_\rho: G \to \mathbb{F}$，

$$
\chi_\rho(g) = \operatorname{tr}(\rho(g)), \quad \forall g \in G,
$$

称为表示 $\rho$ 的**特征标**。

由迹的性质，$\chi_\rho(e) = \dim V$，$\chi_\rho(hgh^{-1}) = \chi_\rho(g)$（特征标在共轭类上取常值），等价的表示有相同的特征标。

**定理 6.4.1（Schur 引理）** 设 $(\rho_1, V_1)$ 和 $(\rho_2, V_2)$ 是群 $G$ 的两个不可约表示，$\varphi: V_1 \to V_2$ 是 $G$-等变线性映射，即对任意 $g \in G$ 有 $\varphi \circ \rho_1(g) = \rho_2(g) \circ \varphi$，则：

1. $\varphi = 0$ 或 $\varphi$ 是线性同构；特别地，当两个表示不等价时，$\varphi = 0$；
2. 若 $V_1 = V_2 = V$ 是有限维空间，$\rho_1 = \rho_2$，且域 $\mathbb{F}$ 代数闭（如 $\mathbb{C}$），则 $\varphi = \lambda \cdot \mathrm{id}_V$（$\lambda \in \mathbb{F}$）是数乘变换。

**证明**：$\ker \varphi$ 是 $V_1$ 的不变子空间，$\varphi(V_1)$ 是 $V_2$ 的不变子空间。由不可约性，$\ker \varphi = V_1$（即 $\varphi = 0$）或 $\ker \varphi = \{0\}$；在后一情形 $\varphi(V_1) \neq \{0\}$，故 $\varphi(V_1) = V_2$，$\varphi$ 是同构，得 1。对 2，取 $\varphi$ 的一个特征值 $\lambda$（代数闭域上存在），则 $\varphi - \lambda \cdot \mathrm{id}_V$ 也是等变映射且不是同构，由 1 得 $\varphi = \lambda \cdot \mathrm{id}_V$。 $\square$

Schur 引理揭示了不可约表示之间的"刚性"，是推导正交关系和分类不可约表示的基础。由它可以得到下面的正交关系。

**定理 6.4.2（特征标的正交关系）** 设 $G$ 是有限群，$\chi_i$、$\chi_j$ 是 $G$ 在 $\mathbb{C}$ 上两个不可约表示的特征标，则

$$
\frac{1}{|G|} \sum_{g \in G} \chi_i(g)\,\overline{\chi_j(g)} =
\begin{cases} 1, & \text{两个表示等价}, \\ 0, & \text{两个表示不等价}. \end{cases}
$$

因此复表示由其特征标唯一确定（在等价意义下）。

## 6.5. 表示论的意义

表示论把抽象的群、李代数和环的元素具体化为线性变换，从而揭示这些结构的内部性质。在数学上，有限单群、李群与代数群的研究都高度依赖表示论。在物理学上，基本粒子的分类与原子光谱的分析都由群与李代数的表示描述：量子力学的角动量理论就是 $SO(3)$（及 $SU(2)$）的表示论，粒子物理的标准模型则依赖规范群 $SU(3) \times SU(2) \times U(1)$ 的表示。因此表示论是连接抽象代数与物理应用的最直接的桥梁之一。
