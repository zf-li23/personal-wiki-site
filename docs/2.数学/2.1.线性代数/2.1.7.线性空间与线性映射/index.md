### 7.1. 线性空间

#### 7.1.1. 数域与线性空间的定义

**数域**$F$是对加减乘除四则运算封闭的复数子集，常见的有$Q$（有理数域）、$R$（实数域）、$C$（复数域）。

**线性空间**$\mathcal{V}$是定义了满足八条运算法则的加法和数乘运算的非空集合。零向量唯一，负向量唯一，并满足加法消去律等性质。

**子空间**是对加法和数乘封闭的非空子集。子空间的交与和仍是子空间，但并通常不是。

**直和** $\mathcal{M} = \mathcal{M}_{1} \oplus \mathcal{M}_{2}$ 要求分解唯一，等价于 $\mathcal{M}_{1} \cap \mathcal{M}_{2} = \{\mathbf{0}\}$。

### 7.2. 基和维数

#### 7.2.1. 线性组合的表示

在选定基$\mathbf{e}_{1}, \dots, \mathbf{e}_{n}$下，向量与矩阵乘法形式统一：
$$\mathbf{b} = (\mathbf{e}_{1}, \dots, \mathbf{e}_{n})\begin{bmatrix} k_{1} \\ k_{2} \\ \vdots \\ k_{n} \end{bmatrix}$$

其中$[k_{1}, k_{2}, \dots, k_{n}]^{T}$是$\mathbf{b}$在该基下的坐标。

#### 7.2.2. 维数与维数公式

线性空间的维数$\dim\mathcal{V}$是其基所含向量的个数。$F$上任意$n$维线性空间都与$F^{n}$同构，维数是线性空间同构关系的唯一不变量。

**维数公式**：$\dim(\mathcal{M}_{1} + \mathcal{M}_{2}) = \dim\mathcal{M}_{1} + \dim\mathcal{M}_{2} - \dim(\mathcal{M}_{1} \cap \mathcal{M}_{2})$。直和的充要条件为维数相加。

### 7.3. 线性映射

#### 7.3.1. 核与像集

对于线性映射 $f \in \text{Hom}(\mathcal{U}, \mathcal{V})$：
- **核** $\mathcal{N}(f) = \{\mathbf{a} \in \mathcal{U} \mid f(\mathbf{a}) = \mathbf{0}\}$，是$\mathcal{U}$的子空间
- **像集** $\mathcal{R}(f) = \{f(\mathbf{a}) \mid \mathbf{a} \in \mathcal{U}\}$，是$\mathcal{V}$的子空间

$f$是单射当且仅当 $\mathcal{N}(f) = \{\mathbf{0}\}$，是满射当且仅当 $\mathcal{R}(f) = \mathcal{V}$。维数关系：$\dim\mathcal{N}(f) + \dim\mathcal{R}(f) = \dim\mathcal{U}$。

**同构映射**是双射的线性映射，线性空间的同构关系是等价关系。

### 7.4. 向量的坐标表示

#### 7.4.1. 坐标与基变换

在基$\mathbf{e}_{1}, \dots, \mathbf{e}_{n}$下，向量$\mathbf{x}$的坐标$\widehat{\mathbf{x}}$由 $\mathbf{x} = (\mathbf{e}_{1}, \dots, \mathbf{e}_{n})\widehat{\mathbf{x}}$ 唯一确定。

**基变换**：若新基$(\mathbf{t}_{1}, \dots, \mathbf{t}_{n}) = (\mathbf{e}_{1}, \dots, \mathbf{e}_{n})T$，则坐标变换为 $\widehat{\mathbf{x}}_{\text{旧}} = T\widehat{\mathbf{x}}_{\text{新}}$。过渡矩阵$T$总是可逆的。

### 7.5. 线性映射的矩阵表示

#### 7.5.1. 表示矩阵

取定$\mathcal{U}$的基$\mathbf{e}_{1}, \dots, \mathbf{e}_{n}$和$\mathcal{V}$的基$\mathbf{i}_{1}, \dots, \mathbf{i}_{m}$，线性映射$f$由矩阵$F$完全表示，满足 $f(\mathbf{e}_{1}, \dots, \mathbf{e}_{n}) = (\mathbf{i}_{1}, \dots, \mathbf{i}_{m})F$。

$\text{Hom}(\mathcal{U}, \mathcal{V})$与$F^{m \times n}$同构，维数为$mn$。映射的复合对应于矩阵乘法。

**基变换下表示矩阵的变化**：若$\mathcal{U}$和$\mathcal{V}$分别作基变换（过渡矩阵$T$和$S$），则新表示矩阵 $\widetilde{F} = S^{-1}FT$，即原矩阵与新矩阵相抵。

#### 7.5.2. 线性变换的表示矩阵

对于$\mathcal{V}$上的线性变换$f$，选定一组基后得到表示矩阵$F$。基变换下表示矩阵的变化为**相似变换**：$\widetilde{F} = T^{-1}FT$。两个矩阵相似当且仅当是同一线性变换在不同基下的表示矩阵。

特征值和特征向量的概念可推广到抽象线性空间：$(\lambda, \mathbf{x})$是$f$的特征对当且仅当$(\lambda, \widehat{\mathbf{x}})$是$F$的特征对。$f$可对角化当且仅当$F$可对角化。