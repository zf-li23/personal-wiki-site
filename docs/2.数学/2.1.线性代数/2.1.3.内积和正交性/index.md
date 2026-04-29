## 3.1. 基本概念

### 3.1.1. 内积与长度

向量内积 $\mathbf{a}^{T}\mathbf{b} = \sum_{i=1}^{n} a_{i}b_{i}$ 具有对称性、双线性和正定性。

向量长度 $\|\mathbf{a}\| = \sqrt{\mathbf{a}^{T}\mathbf{a}}$，单位向量长度为$1$。柯西-施瓦茨不等式：$|\mathbf{a}^{T}\mathbf{b}| \leq \|\mathbf{a}\|\|\mathbf{b}\|$。

### 3.1.2. 正交与正交投影

向量正交：$\mathbf{a}^{T}\mathbf{b} = 0$。正交向量组线性无关。

$\mathbf{b}$在直线$\text{span}(\mathbf{a})$上的正交投影为 $\frac{\mathbf{a}^{T}\mathbf{b}}{\mathbf{a}^{T}\mathbf{a}}\mathbf{a}$，残量$\mathbf{r} = \mathbf{b} - \frac{\mathbf{a}^{T}\mathbf{b}}{\mathbf{a}^{T}\mathbf{a}}\mathbf{a}$与$\mathbf{a}$正交。

### 3.1.3. 标准正交基与正交化

**标准正交基**是两两正交的单位向量组成的基。标准基是特殊的标准正交基，可扩充为更大的标准正交基。

**格拉姆-施密特正交化**从任意基出发构造正交基，递归地在第$r$步减去前$r-1$个正交向量方向上的投影：
$$\widetilde{\mathbf{q}}_{r} = \mathbf{a}_{r} - \sum_{i=1}^{r-1} \frac{\widetilde{\mathbf{q}}_{i}^{T}\mathbf{a}_{r}}{\|\widetilde{\mathbf{q}}_{i}\|^{2}} \widetilde{\mathbf{q}}_{i}$$

正交基单位化即得标准正交基。

## 3.2. 正交矩阵和QR分解

### 3.2.1. 正交矩阵

$n$阶方阵$Q$是正交矩阵当且仅当 $Q^{T}Q = I_{n}$，等价于$Q$可逆且 $Q^{-1} = Q^{T}$，也等价于$Q$的列向量组构成$R^{n}$的标准正交基。正交矩阵保距（$\|Q\mathbf{x}\| = \|\mathbf{x}\|$）且保内积。

**特殊正交矩阵**包括吉文斯旋转变换$G_{\theta;i,j}$和豪斯霍尔德反射变换 $H_{\mathbf{v}} = I_{n} - 2\mathbf{v}\mathbf{v}^{T}$。

### 3.2.2. QR分解

对$n$阶可逆矩阵$A$，存在唯一的分解 $A = QR$，其中$Q$是正交矩阵，$R$是对角元均为正数的上三角矩阵。可通过Gram-Schmidt正交化过程得到：将$A$的列向量正交化得$\widetilde{Q}$，再单位化得$Q$。

对$m \times n$矩阵（$m \geq n$），有简化QR分解 $A = Q_{1}R_{1}$。

## 3.3. 子空间和投影

### 3.3.1. 正交补

子空间$\mathcal{M}$的正交补 $\mathcal{M}^{\perp} = \{\mathbf{a} \in R^{n} \mid \mathbf{a} \perp \mathcal{M}\}$。基本性质：
- $\mathcal{M} \cap \mathcal{M}^{\perp} = \{\mathbf{0}\}$
- $\dim\mathcal{M}^{\perp} = n - \dim\mathcal{M}$
- $(\mathcal{M}^{\perp})^{\perp} = \mathcal{M}$
- $\mathcal{R}(A^{T})^{\perp} = \mathcal{N}(A)$，$\mathcal{R}(A)^{\perp} = \mathcal{N}(A^{T})$

任意向量$\mathbf{a} \in R^{n}$可唯一分解为 $\mathbf{a} = \mathbf{a}_{1} + \mathbf{a}_{2}$，其中 $\mathbf{a}_{1} \in \mathcal{M}$，$\mathbf{a}_{2} \in \mathcal{M}^{\perp}$。

### 3.3.2. 正交投影与最小二乘

**正交投影矩阵**将向量投影到列空间$\mathcal{R}(A)$上：$P_{A} = Q_{1}Q_{1}^{T}$。$P$是正交投影矩阵 $\Leftrightarrow$ $P^{2} = P^{T} = P$。

**最小二乘问题**求 $\min_{\mathbf{x}} \|\mathbf{b} - A\mathbf{x}\|$ 的解。正规方程为 $A^{T}A\mathbf{x} = A^{T}\mathbf{b}$。当$A$列满秩时，最小二乘解唯一：$\mathbf{x}_{0} = (A^{T}A)^{-1}A^{T}\mathbf{b}$。

通过QR分解也可求解：$R_{1}\mathbf{x} = Q_{1}^{T}\mathbf{b}$。
