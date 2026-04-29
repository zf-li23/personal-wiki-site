## 6.1. 实对称矩阵的谱分解

### 6.1.1. 实对称矩阵的性质

实对称矩阵的特征值都是实数，特征向量可取为实向量，属于不同特征值的特征向量互相正交。

**谱分解**：存在正交矩阵$Q$和实对角矩阵$\Lambda$使：
$$A = Q\Lambda Q^{T} = \sum_{i=1}^{n} \lambda_{i}\mathbf{q}_{i}\mathbf{q}_{i}^{T}$$

其中$\mathbf{q}_{i}$是标准正交的特征向量组。

### 6.1.2. 二次型与Rayleigh商

**二次型**：$f(\mathbf{x}) = \mathbf{x}^{T}A\mathbf{x} = \mathbf{x}^{T}\frac{A+A^{T}}{2}\mathbf{x}$，二次型只与对称部分有关。

**Rayleigh商**：$\frac{\mathbf{x}^{T}A\mathbf{x}}{\mathbf{x}^{T}\mathbf{x}}$ 是二次型的归一化。特征值与Rayleigh商之间的极值关系：
$$\lambda_{1} = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\mathbf{x}^{T}A\mathbf{x}}{\mathbf{x}^{T}\mathbf{x}}, \quad \lambda_{n} = \min_{\mathbf{x} \neq \mathbf{0}} \frac{\mathbf{x}^{T}A\mathbf{x}}{\mathbf{x}^{T}\mathbf{x}}$$

## 6.2. 正定矩阵

### 6.2.1. 正定性与等价条件

对实对称矩阵$A$，若对任意非零$\mathbf{x} \in R^{n}$有 $\mathbf{x}^{T}A\mathbf{x} > 0$，则$A$**正定**。

**正定的等价条件**（可使用轮转证法）：
1. 特征值都是正数
2. 存在可逆矩阵$T$使 $A = TT^{T}$
3. 有$LDL^{T}$分解且$D$的对角元素都是正数
4. 顺序主子式都是正数
5. 顺序主子阵都正定
6. $A = LL^{T}$（乔列斯基分解）

**半正定**的条件相应放宽为“非负”，$\mathbf{x}^{T}A\mathbf{x} = 0$当且仅当$\mathbf{x} \in \mathcal{N}(A)$。

### 6.2.2. 合同关系与惯性定律

$A$与$B$**合同**当且仅当存在可逆矩阵$X$使 $B = X^{T}AX$。合同关系保持正定性、秩和对称性。正定矩阵与单位矩阵合同。

**合同标准形**：$X^{T}AX = \begin{bmatrix} I_{p} & & \\ & -I_{r-p} & \\ & & O \end{bmatrix}$。

**西尔维斯特惯性定律**指出正、负、零对角元的个数唯一确定，分别等于正、负、零特征值的个数。正惯性指数$p$确定正定性：$p = n$时正定。

## 6.3. 奇异值分解

### 6.3.1. 奇异值

对$m \times n$矩阵$A$，$A^{T}A$和$AA^{T}$是半正定矩阵，有相同的$r = \text{rank}(A)$个正特征值。$A$的**奇异值**$\sigma_{i} \geq 0$是这些特征值的算术平方根。

若非零向量满足 $A\mathbf{x} = \sigma\mathbf{y}$ 和 $A^{T}\mathbf{y} = \sigma\mathbf{x}$，则$\mathbf{x}$是右奇异向量，$\mathbf{y}$是左奇异向量。

### 6.3.2. 奇异值分解（SVD）

对任意$m \times n$矩阵$A$，存在正交矩阵$U$（$m$阶）和$V$（$n$阶）使得：
$$A = U\Sigma V^{T}, \quad \Sigma = \begin{bmatrix} \Sigma_{r} & \\ & O \end{bmatrix}$$

其中 $\Sigma_{r} = \text{diag}(\sigma_{1}, \sigma_{2}, \dots, \sigma_{r})$。

**简化SVD**：$A = U_{1}\Sigma_{r}V_{1}^{T} = \sum_{i=1}^{r} \sigma_{i}\mathbf{u}_{i}\mathbf{v}_{i}^{T}$。

SVD揭示了四个基本子空间的标准正交基：$\mathbf{u}_{1},\dots,\mathbf{u}_{r}$是$\mathcal{R}(A)$的基，$\mathbf{v}_{1},\dots,\mathbf{v}_{r}$是$\mathcal{R}(A^{T})$的基，$\mathbf{u}_{r+1},\dots,\mathbf{u}_{m}$是$\mathcal{N}(A^{T})$的基，$\mathbf{v}_{r+1},\dots,\mathbf{v}_{n}$是$\mathcal{N}(A)$的基。

### 6.3.3. 谱范数

矩阵的**谱范数** $\|A\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|}$ 等于$A$的最大奇异值。谱范数具有正定性、齐次性、三角不等式和次可乘性。
