## 4.1. 基本概念

### 4.1.1. 行列式的定义与性质

行列式函数$\det: R^{n \times n} \to R$由三条性质唯一确定：
1. **列多线性**：对每一列是线性的
2. **列反对称**：交换两列变号，$\det(\cdots, \mathbf{a}_{i}, \cdots, \mathbf{a}_{j}, \cdots) = -\det(\cdots, \mathbf{a}_{j}, \cdots, \mathbf{a}_{i}, \cdots)$
3. **单位化**：$\det(I_{n}) = 1$

**基本性质**：
- $\det(A) \neq 0 \Leftrightarrow A$可逆
- $\det(AB) = \det(A)\det(B)$
- $\det(A^{T}) = \det(A)$
- $\det(kA) = k^{n}\det(A)$
- 有两列（行）相等或成比例时行列式为零

### 4.1.2. 行列式的计算

- 对角矩阵和三角矩阵的行列式等于对角元素之积
- 正交矩阵的行列式为 $\pm 1$
- $\det(X^{-1}) = 1/\det(X)$
- 通过初等变换化为三角形式计算

## 4.2. 行列式的展开式

### 4.2.1. 代数余子式与展开

元素$a_{ij}$的代数余子式 $C_{ij} = (-1)^{i+j}\det(A\binom{i}{j})$。

行列式可**按任意行或列展开**：
- 按第$j$列：$\det(A) = \sum_{i=1}^{n} a_{ij}C_{ij}$
- 按第$i$行：$\det(A) = \sum_{j=1}^{n} a_{ij}C_{ij}$

**代数余子式向量** $\mathbf{c}_{j} = [C_{1j}, C_{2j}, \dots, C_{nj}]^{T}$ 满足 ${\mathbf{a}_{j'}}^{T}\mathbf{c}_{j} = 0$（$j' \neq j$），即$\mathbf{c}_{j}$是以其余列为棱的底面的法向量，长度等于底面积。

### 4.2.2. 逆矩阵公式与克拉默法则

**逆矩阵公式**：$A^{-1} = \frac{1}{\det(A)}C^{T}$。

**克拉默法则**：若$\det(A) \neq 0$，则$A\mathbf{x} = \mathbf{b}$的唯一解为 $x_{j} = \frac{\det(B_{j})}{\det(A)}$，其中$B_{j}$是将$A$的第$j$列换为$\mathbf{b}$得到的矩阵。

**完全展开式**：$\det(A) = \sum_{\sigma} \text{sign}(\sigma) \prod_{i=1}^{n} a_{i\sigma_{i}}$，其中$\sigma$遍历所有排列。
