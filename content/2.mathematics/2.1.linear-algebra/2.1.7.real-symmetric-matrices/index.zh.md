---
title: 实对称矩阵
---

一般的方阵未必能对角化，即使能对角化，所用的特征向量也未必正交；而实对称矩阵两者兼得：它总能用一个**正交矩阵**对角化。本章从这一点出发，依次讨论实对称矩阵的谱分解、二次型与 Rayleigh 商、正定矩阵与合同关系，最后把"对称矩阵的正交对角化"推广到任意 $m\times n$ 矩阵，得到奇异值分解，并由此定义广义逆与谱范数。

本章用到 [第 4 章](/2.1.4) 的**内积**、**标准正交基**、**正交矩阵**与 **QR 分解**，[第 2 章](/2.1.2) 的 LDU 分解与 **Schur 补**，以及 [第 6 章](/2.1.6) 的**特征值**、**相似**与**特征值分解**。这里的结论是后续课程的基本工具：协方差矩阵是对称半正定矩阵（概率论 3.1），主成分分析就是协方差矩阵的谱分解（多元统计 3.4），最小二乘与广义逆是线性回归（3.3）的骨架，Cholesky 分解与 SVD 是统计计算（3.9）中的标准算法。复数域上的推广（正规矩阵、Hermite 矩阵、复 SVD）见 [第 12 章](/2.1.12) 与 [第 13 章](/2.1.13)。

## 7.1. 实对称矩阵的谱分解

**命题 7.1.1** 实对称矩阵的特征值都是实数。

**证明** 设 $n$ 阶实对称矩阵 $A$ 有特征值 $\lambda\in\mathbb{C}$ 和特征向量 $\boldsymbol{x}=[x_i]\in\mathbb{C}^n$，$A\boldsymbol{x}=\lambda\boldsymbol{x}$。两端取共轭转置，由 $\bar A=A$、$A^{\mathsf T}=A$ 得 $\boldsymbol{x}^{\mathsf H}A=\bar\lambda\,\boldsymbol{x}^{\mathsf H}$。于是

$$
\lambda\,\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\boldsymbol{x}^{\mathsf H}A\boldsymbol{x}=\bar\lambda\,\boldsymbol{x}^{\mathsf H}\boldsymbol{x},
$$

而 $\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\sum_{i=1}^n|x_i|^2>0$，故 $\lambda=\bar\lambda$。$\square$

由于 $\lambda$ 是实数，$\lambda I-A$ 是实矩阵，齐次方程组 $(\lambda I-A)\boldsymbol{x}=\boldsymbol{0}$ 有非零实解，所以实对称矩阵的特征向量都可以取为实向量。下文的特征向量均指实特征向量。

**命题 7.1.2** 实对称矩阵属于不同特征值的特征向量互相正交。

**证明** 设 $\lambda_1\neq\lambda_2$，$A\boldsymbol{x}_1=\lambda_1\boldsymbol{x}_1$，$A\boldsymbol{x}_2=\lambda_2\boldsymbol{x}_2$。对后一式取转置得 $\boldsymbol{x}_2^{\mathsf T}A=\lambda_2\boldsymbol{x}_2^{\mathsf T}$，于是 $\lambda_1\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1=\boldsymbol{x}_2^{\mathsf T}A\boldsymbol{x}_1=\lambda_2\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1$。由 $\lambda_1\neq\lambda_2$ 得 $\boldsymbol{x}_2^{\mathsf T}\boldsymbol{x}_1=0$。$\square$

**定理 7.1.1（实对称矩阵的谱分解）** 对 $n$ 阶实对称矩阵 $A$，存在 $n$ 阶正交矩阵 $Q$ 和实对角矩阵 $\Lambda$，使得 $A=Q\Lambda Q^{\mathsf T}$。

**证明** 对 $n$ 用数学归纳法。$n=1$ 时显然。设结论对 $n-1$ 阶实对称矩阵成立。任取 $A$ 的一个实特征对 $(\lambda_1,\boldsymbol{q}_1)$，$\|\boldsymbol{q}_1\|=1$，把 $\boldsymbol{q}_1$ 扩充成 $\mathbb{R}^n$ 的标准正交基 $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$，记 $Q_1=[\boldsymbol{q}_1\ Q_{12}]$。由 $A\boldsymbol{q}_1=\lambda_1\boldsymbol{q}_1$ 与 $Q_{12}^{\mathsf T}\boldsymbol{q}_1=\boldsymbol{0}$ 得

$$
Q_1^{\mathsf T}AQ_1=\begin{bmatrix}\boldsymbol{q}_1^{\mathsf T}A\boldsymbol{q}_1 & \boldsymbol{q}_1^{\mathsf T}AQ_{12}\\ Q_{12}^{\mathsf T}A\boldsymbol{q}_1 & Q_{12}^{\mathsf T}AQ_{12}\end{bmatrix}=\begin{bmatrix}\lambda_1 & \boldsymbol{0}^{\mathsf T}\\ \boldsymbol{0} & Q_{12}^{\mathsf T}AQ_{12}\end{bmatrix},
$$

右上块为零是因为 $\boldsymbol{q}_1^{\mathsf T}AQ_{12}=(Q_{12}^{\mathsf T}A\boldsymbol{q}_1)^{\mathsf T}$。$Q_{12}^{\mathsf T}AQ_{12}$ 是 $n-1$ 阶实对称矩阵，由归纳假设有 $Q_{12}^{\mathsf T}AQ_{12}=Q_2\Lambda_2Q_2^{\mathsf T}$。令

$$
Q=Q_1\begin{bmatrix}1&\\&Q_2\end{bmatrix},\qquad \Lambda=\begin{bmatrix}\lambda_1&\\&\Lambda_2\end{bmatrix},
$$

则 $Q$ 是正交矩阵（正交矩阵之积），$\Lambda$ 是实对角矩阵，且 $A=Q\Lambda Q^{\mathsf T}$。$\square$

分解 $A=Q\Lambda Q^{\mathsf T}$ 称为实对称矩阵 $A$ 的谱分解（Spectral Decomposition）。它是 [第 6 章](/2.1.6) **特征值分解** $A=X\Lambda X^{-1}$ 的特殊情形：$X$ 取成正交矩阵，$X^{-1}=X^{\mathsf T}$。有的教材对一般可对角化矩阵的 $X\Lambda X^{-1}$ 也称"谱分解"，本书只把这个名称用于正交（或酉）对角化。几点说明：

- 记 $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$，$\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，则
  $$
  A=Q\Lambda Q^{\mathsf T}=\lambda_1\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T}+\cdots+\lambda_n\boldsymbol{q}_n\boldsymbol{q}_n^{\mathsf T}.
  $$
  每个 $\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf T}$ 是向直线 $\operatorname{span}(\boldsymbol{q}_i)$ 的**正交投影矩阵**，所以 $A$ 作用于向量，就是先把向量沿 $n$ 个互相垂直的方向分解，再在各方向上分别伸缩 $\lambda_i$ 倍。
- 适当排列 $Q$ 的列，可以使 $\Lambda$ 的对角元是 $A$ 的特征值的任意排列。
- 实对称矩阵总可对角化，因此每个特征值的**几何重数**都等于**代数重数**。

**算法 7.1.1（实对称矩阵的谱分解）** 输入 $n$ 阶实对称矩阵 $A$：

1. 计算特征多项式 $p_A(\lambda)=\det(\lambda I-A)$ 的全部根，得到互不相同的特征值 $\mu_1,\dots,\mu_s$；
2. 对每个 $\mu_j$，求 $(\mu_jI-A)\boldsymbol{x}=\boldsymbol{0}$ 的解空间的一组基，再用 **Gram–Schmidt 正交化**把它化成标准正交基；
3. 把各特征子空间的标准正交基合在一起，按列排成 $Q$，相应的特征值排成 $\Lambda$。

由命题 7.1.2，不同特征子空间自动正交，所以第 2 步只需在每个特征子空间内部正交化。

**例 7.1.1** 求 $A=\begin{bmatrix}4&2&2\\2&4&2\\2&2&4\end{bmatrix}$ 的谱分解。$A=2I+2\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$，其中 $\boldsymbol{1}=[1\ 1\ 1]^{\mathsf T}$，所以特征值为 $8$（特征向量 $\boldsymbol{1}$）和二重的 $2$（特征子空间是 $x_1+x_2+x_3=0$）。在后者中取基 $[-1\ 1\ 0]^{\mathsf T},[-1\ 0\ 1]^{\mathsf T}$，正交化并单位化，得

$$
Q=\begin{bmatrix}\frac{1}{\sqrt3}&-\frac{1}{\sqrt2}&-\frac{1}{\sqrt6}\\ \frac{1}{\sqrt3}&\frac{1}{\sqrt2}&-\frac{1}{\sqrt6}\\ \frac{1}{\sqrt3}&0&\frac{2}{\sqrt6}\end{bmatrix},\qquad \Lambda=\operatorname{diag}(8,2,2),\qquad A=Q\Lambda Q^{\mathsf T}.
$$

**例 7.1.2（正交投影矩阵的谱分解）** 正交投影矩阵 $P$ 满足 $P^2=P^{\mathsf T}=P$，是实对称矩阵。若 $P\boldsymbol{x}=\lambda\boldsymbol{x}$，由 $P\boldsymbol{x}=P^2\boldsymbol{x}$ 得 $\lambda\boldsymbol{x}=\lambda^2\boldsymbol{x}$，故 $\lambda\in\{0,1\}$。分别取 $\mathcal{R}(P)$ 与 $\mathcal{N}(P)$ 的标准正交基 $\boldsymbol{q}_1,\dots,\boldsymbol{q}_r$ 与 $\boldsymbol{q}_{r+1},\dots,\boldsymbol{q}_n$，它们分别是属于 $1$ 与 $0$ 的特征向量，合起来是 $\mathbb{R}^n$ 的标准正交基（$\mathcal{N}(P)=\mathcal{R}(P)^\perp$）。令 $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$，则

$$
P=Q\begin{bmatrix}I_r&\\&O\end{bmatrix}Q^{\mathsf T}=\boldsymbol{q}_1\boldsymbol{q}_1^{\mathsf T}+\cdots+\boldsymbol{q}_r\boldsymbol{q}_r^{\mathsf T}.
$$

谱分解 $A=Q\Lambda Q^{\mathsf T}$ 也可以写成 $Q^{\mathsf T}AQ=\Lambda$，这引出下面的等价关系。

**定义 7.1.1（正交相似）** 对实方阵 $A,B$，如果存在正交矩阵 $Q$ 使得 $Q^{\mathsf T}AQ=B$，则称 $A$ 与 $B$ **正交相似**。

**命题 7.1.3** 实方阵的正交相似关系是**等价关系**。

**证明** 自反性：$A=I^{\mathsf T}AI$。对称性：由 $Q^{\mathsf T}AQ=B$ 得 $Q BQ^{\mathsf T}=A$，而 $Q^{\mathsf T}$ 也是正交矩阵。传递性：由 $Q^{\mathsf T}AQ=B$、$R^{\mathsf T}BR=C$ 得 $(QR)^{\mathsf T}A(QR)=C$。$\square$

对应的等价变换 $A\mapsto Q^{\mathsf T}AQ$ 称为正交相似变换。正交相似是**相似**的特例（$Q^{\mathsf T}=Q^{-1}$），所以相似的不变量（秩、特征多项式、特征值及其代数重数与几何重数、行列式、迹）都是正交相似的不变量；此外它还保持对称性：$Q^{\mathsf T}AQ$ 对称（反对称）当且仅当 $A$ 对称（反对称）。定理 7.1.1 说明：实对称矩阵在正交相似下的标准形是实对角矩阵，即一个实方阵正交相似于对角矩阵当且仅当它是对称矩阵（必要性：$Q\Lambda Q^{\mathsf T}$ 显然对称）。正交相似并不只用于对称矩阵，非对称实矩阵的正交相似标准形（实 Schur 形）与复矩阵的酉相似见 [第 12 章](/2.1.12)。

## 7.2. 二次型与 Rayleigh 商

**定义 7.2.1（二次型）** 关于变量 $x_1,\dots,x_n$ 的实系数齐次二次函数

$$
f(x_1,\dots,x_n)=\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_ix_j
$$

称为一个**二次型**。记 $\boldsymbol{x}=[x_i]$，$A=[a_{ij}]_{n\times n}$，则 $f(\boldsymbol{x})=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$。

由 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})^{\mathsf T}=\boldsymbol{x}^{\mathsf T}A^{\mathsf T}\boldsymbol{x}$ 得

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{x}^{\mathsf T}\frac{A+A^{\mathsf T}}{2}\boldsymbol{x},
$$

即二次型只和 $A$ 的**对称矩阵**部分 $\frac12(A+A^{\mathsf T})$ 有关（任意方阵唯一地分解为对称部分与**反对称矩阵**部分之和）。因此以后总假定二次型的矩阵是实对称的，这时 $A$ 由二次型唯一确定：$a_{ii}$ 是 $x_i^2$ 的系数，$a_{ij}=a_{ji}$ 是 $x_ix_j$ 系数的一半。很多物理系统的能量是二次型，例如弹簧振子的能量

$$
\tfrac12kx^2+\tfrac12mv^2=\begin{bmatrix}x&v\end{bmatrix}\begin{bmatrix}\frac12k&\\&\frac12m\end{bmatrix}\begin{bmatrix}x\\v\end{bmatrix},
$$

所以 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ 也常称为能量函数。

**例 7.2.1（Hesse 矩阵）** 设 $f\colon \mathbb{R}^n\to\mathbb{R}$ 在 $\boldsymbol{x}_0$ 附近三阶连续可微，则由多元函数的**泰勒公式**，在 $\boldsymbol{x}_0$ 的半径为 $\rho$ 的小邻域内

$$
f(\boldsymbol{x})=f(\boldsymbol{x}_0)+\nabla f(\boldsymbol{x}_0)^{\mathsf T}(\boldsymbol{x}-\boldsymbol{x}_0)+\tfrac12(\boldsymbol{x}-\boldsymbol{x}_0)^{\mathsf T}H(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)+o(\rho^2),
$$

其中 $\nabla f(\boldsymbol{x}_0)=\Big[\frac{\partial f}{\partial x_i}(\boldsymbol{x}_0)\Big]_{n\times1}$ 称为梯度，$H(\boldsymbol{x}_0)=\Big[\frac{\partial^2 f}{\partial x_i\partial x_j}(\boldsymbol{x}_0)\Big]_{n\times n}$ 称为 $f$ 在 $\boldsymbol{x}_0$ 的 Hesse 矩阵（Hessian Matrix）。二阶偏导连续时混合偏导与次序无关，所以 Hesse 矩阵是实对称矩阵，Taylor 展开的二阶项是一个二次型。

用谱分解可以把二次型化成没有交叉项的形式。设 $A=Q\Lambda Q^{\mathsf T}$，作正交变量替换 $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$，则

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}\Lambda\boldsymbol{y}=\lambda_1y_1^2+\cdots+\lambda_ny_n^2.
$$

几何上，这是把坐标轴转到 $A$ 的 $n$ 个互相正交的特征向量方向（称为主轴）。例如 $5x_1^2+4x_1x_2+5x_2^2=1$ 的矩阵 $\begin{bmatrix}5&2\\2&5\end{bmatrix}$ 有特征值 $7,3$，特征向量 $\frac{1}{\sqrt2}[1\ 1]^{\mathsf T},\frac{1}{\sqrt2}[-1\ 1]^{\mathsf T}$，所以曲线是 $7y_1^2+3y_2^2=1$，即主轴沿 $45^\circ$ 方向、半轴长为 $1/\sqrt7$ 与 $1/\sqrt3$ 的椭圆。

只考虑 $\boldsymbol{x}$ 的方向对二次型的影响时，把二次型除以 $\|\boldsymbol{x}\|^2$：

**定义 7.2.2（Rayleigh 商）** 给定实方阵 $A$ 和非零向量 $\boldsymbol{x}\in\mathbb{R}^n$，实数 $\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$ 称为 $\boldsymbol{x}$ 关于 $A$ 的 **Rayleigh 商**。

若 $A=QBQ^{\mathsf T}$（$Q$ 正交），令 $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$，则 $\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\dfrac{\boldsymbol{y}^{\mathsf T}B\boldsymbol{y}}{\boldsymbol{y}^{\mathsf T}\boldsymbol{y}}$：正交相似把 Rayleigh 商变成另一个矩阵的 Rayleigh 商，只是自变量做了正交变换。取 $B=\Lambda$ 就得到下面的极值刻画。

**定理 7.2.1（特征值的极值刻画）** 设实对称矩阵 $A$ 的特征值为 $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$，相应的特征向量 $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$ 构成 $\mathbb{R}^n$ 的标准正交基，则

$$
\lambda_i=\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\min_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_i)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}.
$$

特别地，$\lambda_1=\max\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$，$\lambda_n=\min\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\dfrac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$。

条件 $\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)$ 等价于 $\boldsymbol{x}\perp\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_{i-1})$，即在与前 $i-1$ 个特征向量正交的方向中求最大值。

**证明** 令 $Q=[\boldsymbol{q}_1\ \cdots\ \boldsymbol{q}_n]$，$\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，则 $A=Q\Lambda Q^{\mathsf T}$。令 $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$，由 $Q^{\mathsf T}\boldsymbol{q}_j=\boldsymbol{e}_j$，$\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)$ 当且仅当 $\boldsymbol{y}\in\operatorname{span}(\boldsymbol{e}_i,\dots,\boldsymbol{e}_n)$，即 $y_1=\cdots=y_{i-1}=0$。于是

$$
\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_i,\dots,\boldsymbol{q}_n)}}\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\max_{\substack{\boldsymbol{y}\neq\boldsymbol{0}\\ y_1=\cdots=y_{i-1}=0}}\frac{\lambda_iy_i^2+\cdots+\lambda_ny_n^2}{y_i^2+\cdots+y_n^2}=\lambda_i,
$$

因为分子不超过 $\lambda_i(y_i^2+\cdots+y_n^2)$，且 $\boldsymbol{y}=\boldsymbol{e}_i$ 时取等号。对 $-A$ 应用这一结论：$-A$ 的特征值 $-\lambda_n\ge\cdots\ge-\lambda_1$ 对应特征向量 $\boldsymbol{q}_n,\dots,\boldsymbol{q}_1$，得 $-\lambda_i=\max\limits_{\boldsymbol{x}\in\operatorname{span}(\boldsymbol{q}_1,\dots,\boldsymbol{q}_i)}\frac{\boldsymbol{x}^{\mathsf T}(-A)\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$，即后一等式。$\square$

定理 7.2.1 把特征值问题变成了约束优化问题：$\lambda_1$ 是二次型在单位球面 $\|\boldsymbol{x}\|=1$ 上的最大值，最大值点是 $\boldsymbol{q}_1$。主成分分析正是这样求协方差矩阵方差最大的方向。更一般的 Courant–Fischer 极小极大原理不需要事先知道特征向量：$\lambda_i$ 是 Rayleigh 商在所有 $i$ 维子空间上的最小值的最大值。

以前面的 $5x_1^2+4x_1x_2+5x_2^2$ 为例：下图左边是它的等值线，都是以两个特征向量为主轴的椭圆；右边是 Rayleigh 商沿单位圆的取值，最大值 $7$ 在 $\boldsymbol{q}_1$ 方向（$45^\circ$）取到，最小值 $3$ 在与之正交的 $\boldsymbol{q}_2$ 方向（$135^\circ$）取到。

![左：二次型 5x_1^2+4x_1x_2+5x_2^2 的等值线是以特征向量为主轴的椭圆，箭头是曲线 x^T A x = 1 的两条半轴 q_i/√λ_i；右：Rayleigh 商在单位圆上的取值，最大值与最小值恰为特征值 7 与 3](./plots/principal-axes-rayleigh.py)

对非对称的实方阵 $A$，Rayleigh 商只依赖于 $A$ 的对称部分，所以它的极值是 $\frac12(A+A^{\mathsf T})$ 的最大、最小特征值，而不是 $A$ 的特征值。例如 $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ 的特征值都是 $0$，但 Rayleigh 商 $x_1x_2/(x_1^2+x_2^2)$ 取遍 $[-\frac12,\frac12]$。

## 7.3. 正定矩阵与合同

### 7.3.1. 二次型的分类

**定义 7.3.1（二次型的分类）** 给定 $n$ 阶实方阵 $A$，若对任意非零向量 $\boldsymbol{x}\in\mathbb{R}^n$ 都有

1. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$，则称 $A$ 为**正定矩阵**，也称二次型正定；
2. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\ge0$，则称 $A$ 为**半正定矩阵**，也称二次型半正定；
3. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}<0$，则称 $A$ **负定**；
4. $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\le0$，则称 $A$ **半负定**；
5. 若 $A$ 不满足以上任何一种条件，即存在 $\boldsymbol{x},\boldsymbol{y}$ 使 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0>\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$，则称 $A$ 为**不定矩阵**，也称二次型不定。

$A$（半）负定当且仅当 $-A$（半）正定，所以只需研究正定与半正定。按 §7.2 的约定，讨论正定性时总假定 $A$ 是实对称矩阵。

**命题 7.3.1** 设 $T$ 是 $n$ 阶可逆矩阵，则 $T^{\mathsf T}AT$ 的（半）正定、（半）负定、不定的性质都与 $A$ 相同。

**证明** 以正定为例。若 $A$ 正定，对 $\boldsymbol{x}\neq\boldsymbol{0}$ 有 $T\boldsymbol{x}\neq\boldsymbol{0}$，故 $\boldsymbol{x}^{\mathsf T}T^{\mathsf T}AT\boldsymbol{x}=(T\boldsymbol{x})^{\mathsf T}A(T\boldsymbol{x})>0$。反之，若 $T^{\mathsf T}AT$ 正定，对 $\boldsymbol{x}\neq\boldsymbol{0}$ 令 $\boldsymbol{y}=T^{-1}\boldsymbol{x}\neq\boldsymbol{0}$，则 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}T^{\mathsf T}AT\boldsymbol{y}>0$。$\square$

**例 7.3.1（Hesse 矩阵与极值）** 回到例 7.2.1。若 $\boldsymbol{x}_0$ 是驻点，即 $\nabla f(\boldsymbol{x}_0)=\boldsymbol{0}$，则 $f(\boldsymbol{x})-f(\boldsymbol{x}_0)=\frac12(\boldsymbol{x}-\boldsymbol{x}_0)^{\mathsf T}H(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)+o(\rho^2)$。因此：$H(\boldsymbol{x}_0)$ 正定时 $\boldsymbol{x}_0$ 是极小值点；负定时是极大值点；不定时不是极值点；半正定或半负定（且奇异）时需要更高阶的 Taylor 展开才能判断。

### 7.3.2. 正定矩阵

正定矩阵一定可逆（否则取 $\boldsymbol{x}\in\mathcal{N}(A)$ 非零，$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=0$）。实对角矩阵正定当且仅当对角元都是正数；特别地，单位矩阵正定，这就是**内积**的正定性 $\boldsymbol{x}^{\mathsf T}\boldsymbol{x}>0$。

**定义 7.3.2（顺序主子式）** 方阵 $A$ 的第 $i$ 个顺序主子阵 $A_i$（左上角 $i\times i$ 子矩阵）的行列式 $\det A_i$ 称为 $A$ 的第 $i$ 个**顺序主子式**。

**定理 7.3.1（正定矩阵的等价条件）** 对实对称矩阵 $A$，以下叙述等价：

1. $A$ 正定，即对任意非零向量 $\boldsymbol{x}$ 都有 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$；
2. $A$ 的特征值都是正数；
3. 存在可逆矩阵 $T$，使得 $A=T^{\mathsf T}T$；
4. $A$ 有 $LDL^{\mathsf T}$ 分解（$L$ 为单位下三角矩阵，$D$ 为对角矩阵），且 $D$ 的对角元都是正数；
5. $A$ 的顺序主子式都是正数；
6. $A$ 的顺序主子阵都正定。

**证明**（轮转证法）$1\Rightarrow2$：设 $(\lambda,\boldsymbol{x})$ 是特征对，则 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\lambda\boldsymbol{x}^{\mathsf T}\boldsymbol{x}>0$，故 $\lambda>0$。

$2\Rightarrow3$：由谱分解 $A=Q\Lambda Q^{\mathsf T}$，$\Lambda$ 的对角元为正，取对角矩阵 $\Lambda^{1/2}$ 使 $(\Lambda^{1/2})^2=\Lambda$，令 $T=\Lambda^{1/2}Q^{\mathsf T}$，则 $T$ 可逆且 $A=T^{\mathsf T}T$。

$3\Rightarrow4$：对 $T$ 做 **QR 分解** $T=QR$，$R$ 是对角元为正的上三角矩阵，则 $A=R^{\mathsf T}Q^{\mathsf T}QR=R^{\mathsf T}R$。把 $R^{\mathsf T}$ 写成 $L\tilde D$（$L$ 单位下三角，$\tilde D$ 为 $R$ 的对角部分，对角元为正），得 $A=L\tilde D^2L^{\mathsf T}$，取 $D=\tilde D^2$ 即可。

$4\Rightarrow5$：按第 $i$ 个顺序主子阵分块，

$$
\begin{bmatrix}A_i&A_{21}^{\mathsf T}\\A_{21}&A_{22}\end{bmatrix}=\begin{bmatrix}L_i&\\L_{21}&L_{22}\end{bmatrix}\begin{bmatrix}D_i&\\&D_{22}\end{bmatrix}\begin{bmatrix}L_i&\\L_{21}&L_{22}\end{bmatrix}^{\mathsf T},
$$

比较左上块得 $A_i=L_iD_iL_i^{\mathsf T}$，故 $\det A_i=\det D_i>0$。

$5\Rightarrow6$：对 $n$ 归纳。$n=1$ 显然。设结论对 $n-1$ 阶成立；$A$ 的顺序主子阵 $A_1,\dots,A_{n-1}$ 也是 $A_{n-1}$ 的顺序主子阵，由归纳假设它们都正定，只需再证 $A=A_n$ 正定。$A_{n-1}$ 可逆且 $A_{n-1}^{-1}$ 对称。写 $A=\begin{bmatrix}A_{n-1}&\boldsymbol{a}\\\boldsymbol{a}^{\mathsf T}&a_{nn}\end{bmatrix}$，作分块消元，

$$
A=\begin{bmatrix}I_{n-1}&\\\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}&1\end{bmatrix}\begin{bmatrix}A_{n-1}&\\&a_{nn}-\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{a}\end{bmatrix}\begin{bmatrix}I_{n-1}&A_{n-1}^{-1}\boldsymbol{a}\\&1\end{bmatrix}=TBT^{\mathsf T}.
$$

由命题 7.3.1，$A$ 正定当且仅当 $B$ 正定。$B$ 的右下角是 $A_{n-1}$ 的 **Schur 补**，取行列式得 $a_{nn}-\boldsymbol{a}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{a}=\det A/\det A_{n-1}>0$，而 $A_{n-1}$ 正定，所以分块对角矩阵 $B$ 正定。

$6\Rightarrow1$：$A=A_n$ 本身是顺序主子阵。$\square$

条件 2 与条件 5 是两种实用的判别法：前者要求特征值，后者只要算 $n$ 个行列式；而条件 4 说明，对称矩阵的 Gauss 消元若主元全为正，就同时证明了它正定，这是计算上最便宜的判别法。由定理 7.3.1 还可得到正定矩阵的几条性质：

- 若 $A$ 正定，则 $A^{-1}$ 正定（特征值是 $\lambda_i^{-1}>0$），$A^k$（$k\in\mathbb{N}$）正定；
- 若 $A,B$ 正定，$k>0$，则 $A+B$、$kA$ 正定（直接由定义）；
- 正定矩阵的对角元 $a_{ii}=\boldsymbol{e}_i^{\mathsf T}A\boldsymbol{e}_i>0$；
- 若 $C$ 是 $m\times n$ 列满秩矩阵，则 $C^{\mathsf T}C$ 正定（$\boldsymbol{x}^{\mathsf T}C^{\mathsf T}C\boldsymbol{x}=\|C\boldsymbol{x}\|^2>0$）。

### 7.3.3. Cholesky 分解

条件 4 中令 $\tilde L=LD^{1/2}$，就把 $A$ 写成一个下三角矩阵与其转置之积。

**定理 7.3.2（Cholesky 分解）** 实对称矩阵 $A$ 正定，当且仅当存在对角元都为正数的下三角矩阵 $L$，使得 $A=LL^{\mathsf T}$；这样的 $L$ 唯一。

**证明** 存在性：由定理 7.3.1 的条件 4，$A=L_0DL_0^{\mathsf T}$，令 $L=L_0D^{1/2}$ 即可。反之，若 $A=LL^{\mathsf T}$ 且 $L$ 可逆，则由条件 3 知 $A$ 正定。唯一性：若 $L_1L_1^{\mathsf T}=L_2L_2^{\mathsf T}$，则 $L_2^{-1}L_1=L_2^{\mathsf T}L_1^{-\mathsf T}$。左边是下三角矩阵，右边是上三角矩阵，所以两边都等于一个对角矩阵 $D$，且对角元为正；又 $D=L_2^{-1}L_1$ 与 $D^{-1}=(L_2^{\mathsf T}L_1^{-\mathsf T})^{-1}=L_1^{\mathsf T}L_2^{-\mathsf T}=D^{\mathsf T}=D$，故 $D^2=I$，$D=I$，$L_1=L_2$。$\square$

比较 $A=LL^{\mathsf T}$ 两边的 $(i,j)$ 元（$i\ge j$）得 $a_{ij}=\sum_{k=1}^{j}l_{ik}l_{jk}$，按列逐个解出 $L$ 的元素：

**算法 7.3.1（Cholesky 分解）** 输入 $n$ 阶实对称矩阵 $A$。对 $j=1,2,\dots,n$：

1. 计算 $d=a_{jj}-\sum_{k=1}^{j-1}l_{jk}^2$。若 $d\le0$，则 $A$ 不正定，停止；否则 $l_{jj}=\sqrt d$；
2. 对 $i=j+1,\dots,n$，计算 $l_{ij}=\Big(a_{ij}-\sum_{k=1}^{j-1}l_{ik}l_{jk}\Big)\Big/l_{jj}$。

算法只用到 $A$ 的下三角部分，运算量约 $\frac13n^3$ 次乘加，是 LU 分解（约 $\frac23n^3$）的一半，存储也只需一半；它不需要选主元，数值上是稳定的；而且算法能否进行到底本身就是正定性的判别。求解正定方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 时，先做 $A=LL^{\mathsf T}$，再依次用前代法解 $L\boldsymbol{y}=\boldsymbol{b}$、用**回代法**解 $L^{\mathsf T}\boldsymbol{x}=\boldsymbol{y}$。正规方程 $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$（$A$ 列满秩）、多元正态分布的抽样都以此为标准做法。

**例 7.3.2** 对 $A=\begin{bmatrix}4&2&2\\2&5&3\\2&3&6\end{bmatrix}$：$l_{11}=2$，$l_{21}=l_{31}=1$；$l_{22}=\sqrt{5-1}=2$，$l_{32}=(3-1)/2=1$；$l_{33}=\sqrt{6-1-1}=2$。所以 $A$ 正定，且

$$
A=\begin{bmatrix}2&&\\1&2&\\1&1&2\end{bmatrix}\begin{bmatrix}2&1&1\\&2&1\\&&2\end{bmatrix}.
$$

在复数域上，正定 Hermite 矩阵同样有唯一的分解 $A=R^{\mathsf H}R$，$R$ 为对角元是正实数的上三角矩阵，见 [第 13 章](/2.1.13)。

### 7.3.4. 半正定矩阵与不定矩阵

**命题 7.3.2（半正定矩阵的等价条件）** 对实对称矩阵 $A$，以下叙述等价：

1. $A$ 半正定；
2. $A$ 的特征值都是非负数；
3. 存在矩阵 $T$ 使得 $A=T^{\mathsf T}T$；
4. $A$ 有 $LDL^{\mathsf T}$ 分解，且 $D$ 的对角元都是非负数。

**证明** $1\Rightarrow2$、$2\Rightarrow3$ 与定理 7.3.1 相同（这时 $\Lambda^{1/2}$ 可以有零对角元）。$3\Rightarrow1$：$\boldsymbol{x}^{\mathsf T}T^{\mathsf T}T\boldsymbol{x}=\|T\boldsymbol{x}\|^2\ge0$。$4\Rightarrow1$：令 $\boldsymbol{y}=L^{\mathsf T}\boldsymbol{x}$，则 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}D\boldsymbol{y}\ge0$。$1\Rightarrow4$：对 $n$ 归纳，写 $A=\begin{bmatrix}a_{11}&\boldsymbol{a}^{\mathsf T}\\\boldsymbol{a}&A'\end{bmatrix}$。若 $a_{11}>0$，消去第一列，$A=\begin{bmatrix}1&\\\boldsymbol{a}/a_{11}&I\end{bmatrix}\begin{bmatrix}a_{11}&\\&A'-\boldsymbol{a}\boldsymbol{a}^{\mathsf T}/a_{11}\end{bmatrix}\begin{bmatrix}1&\\\boldsymbol{a}/a_{11}&I\end{bmatrix}^{\mathsf T}$，由命题 7.3.1 中间的矩阵半正定，对右下块用归纳假设。若 $a_{11}=0$，则 $\boldsymbol{a}=\boldsymbol{0}$：否则取 $\boldsymbol{x}=[t\ \ \boldsymbol{a}^{\mathsf T}]^{\mathsf T}$，$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=2t\|\boldsymbol{a}\|^2+\boldsymbol{a}^{\mathsf T}A'\boldsymbol{a}$ 在 $t\to-\infty$ 时为负；于是 $A=\operatorname{diag}(0,A')$，对 $A'$ 用归纳假设。$\square$

- 对实对称半正定矩阵 $A$，$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=0$ 当且仅当 $\boldsymbol{x}\in\mathcal{N}(A)$：由 $A=T^{\mathsf T}T$，$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\|T\boldsymbol{x}\|^2=0$ 推出 $T\boldsymbol{x}=\boldsymbol{0}$，从而 $A\boldsymbol{x}=\boldsymbol{0}$。
- 半正定矩阵的顺序主子式都非负，但反之不成立：$A=\begin{bmatrix}0&0\\0&-1\end{bmatrix}$ 的顺序主子式是 $0,0$，而 $\boldsymbol{e}_2^{\mathsf T}A\boldsymbol{e}_2=-1$。正确的判别法是：实对称矩阵半正定，当且仅当它的所有主子式（任选同样的若干行和列得到的子矩阵的行列式）都非负。
- 对任意实矩阵 $C$，$C^{\mathsf T}C$ 与 $CC^{\mathsf T}$ 都半正定（条件 3），§7.4 的奇异值分解由此出发。

**命题 7.3.3** 若 $n$ 阶实对称矩阵 $A$ 不定，即存在 $\boldsymbol{x},\boldsymbol{y}$ 使 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$，$\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}<0$，则存在非零向量 $\boldsymbol{z}$ 使 $\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=0$。

**证明** $\boldsymbol{x},\boldsymbol{y}$ 线性无关（否则二者的二次型同号），所以 $\boldsymbol{z}=\boldsymbol{x}+k\boldsymbol{y}\neq\boldsymbol{0}$。$\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}+2k\,\boldsymbol{x}^{\mathsf T}A\boldsymbol{y}+k^2\,\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$ 是 $k$ 的二次函数，首项系数为负、常数项为正，判别式 $4(\boldsymbol{x}^{\mathsf T}A\boldsymbol{y})^2-4(\boldsymbol{x}^{\mathsf T}A\boldsymbol{x})(\boldsymbol{y}^{\mathsf T}A\boldsymbol{y})>0$，有实根。$\square$

### 7.3.5. 合同与惯性定律

命题 7.3.1 中的变换 $A\mapsto T^{\mathsf T}AT$ 来自变量替换 $\boldsymbol{x}=T\boldsymbol{y}$：$\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=\boldsymbol{y}^{\mathsf T}(T^{\mathsf T}AT)\boldsymbol{y}$。这启发下面的定义。

**定义 7.3.3（合同）** 对方阵 $A,B$，若存在可逆矩阵 $X$ 使 $X^{\mathsf T}AX=B$，则称 $A$ 与 $B$ **合同**。

**命题 7.3.4** 方阵的合同关系是等价关系。

**证明** 自反性：$A=I^{\mathsf T}AI$。对称性：由 $X^{\mathsf T}AX=B$ 得 $(X^{-1})^{\mathsf T}BX^{-1}=A$。传递性：由 $X^{\mathsf T}AX=B$、$Y^{\mathsf T}BY=C$ 得 $(XY)^{\mathsf T}A(XY)=C$。$\square$

对应的等价变换 $A\mapsto X^{\mathsf T}AX$（$X$ 可逆）称为合同变换。它的不变量包括：秩、（半）正定、（半）负定和不定的性质（命题 7.3.1）、对称性。正交相似是一种特殊的合同（$X$ 正交时 $X^{\mathsf T}=X^{-1}$），但一般的合同不保持特征值，例如 $\operatorname{diag}(1,4)$ 与 $I_2$ 合同。由定理 7.3.1 的条件 3，实对称矩阵正定当且仅当它与单位矩阵合同。

**命题 7.3.5（合同标准形）** 对实对称矩阵 $A$，存在可逆矩阵 $X$ 使

$$
X^{\mathsf T}AX=J=\begin{bmatrix}I_p&&\\&-I_{r-p}&\\&&O\end{bmatrix},
$$

其中 $r=\operatorname{rank}(A)$，$0\le p\le r$。$J$ 称为 $A$ 的合同标准形。

**证明** 由谱分解，存在正交矩阵 $Q$ 使 $Q^{\mathsf T}AQ=\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，并把特征值排成 $\lambda_1,\dots,\lambda_p>0$，$\lambda_{p+1},\dots,\lambda_r<0$，$\lambda_{r+1}=\cdots=\lambda_n=0$。令 $Y=\operatorname{diag}\big(|\lambda_1|^{-1/2},\dots,|\lambda_r|^{-1/2},1,\dots,1\big)$，则 $Y^{\mathsf T}\Lambda Y=J$。取 $X=QY$ 即可。$\square$

**定理 7.3.3（Sylvester 惯性定律）** 实对称矩阵的合同标准形唯一，且其中正、负、零对角元的个数分别等于它的正、负、零特征值的个数（计重数）。

**证明** 由命题 7.3.5 的证明，只需证合同标准形唯一。设 $J_1=X^{\mathsf T}AX$，$J_2=Y^{\mathsf T}AY$ 是 $A$ 的两个合同标准形，正对角元个数分别为 $p,q$；二者的秩都是 $r$，只需证 $p=q$。分块 $X=[X_1\ X_2]$，$Y=[Y_1\ Y_2]$，$X_1$ 有 $p$ 列，$Y_1$ 有 $q$ 列，则 $X_1^{\mathsf T}AX_1=I_p$，$Y_2^{\mathsf T}AY_2=\operatorname{diag}(-I_{r-q},O)$。令 $M=\mathcal{R}(X_1)$，$N=\mathcal{R}(Y_2)$，则 $\dim M=p$，$\dim N=n-q$；对非零 $\boldsymbol{x}\in M$ 有 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$，对 $\boldsymbol{x}\in N$ 有 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\le0$，所以 $M\cap N=\{\boldsymbol{0}\}$。由 $\dim(M+N)=\dim M+\dim N\le n$ 得 $p\le q$。交换 $J_1,J_2$ 的地位得 $q\le p$。$\square$

**定义 7.3.4（惯性指数）** 实对称矩阵 $A$ 的合同标准形中正对角元 $1$ 的个数 $p$ 称为 $A$ 的**正惯性指数**，负对角元 $-1$ 的个数 $r-p$ 称为**负惯性指数**；三元组 $(p,\,r-p,\,n-r)$ 称为 $A$ 的**惯性指数**。

惯性指数是合同变换下的完全不变量：两个 $n$ 阶实对称矩阵合同，当且仅当它们的惯性指数相同（都与同一个 $J$ 合同）。因此 $n$ 阶实对称矩阵在合同下的等价类共有 $\sum_{r=0}^n(r+1)=\frac{(n+1)(n+2)}{2}$ 个。实对称矩阵正定当且仅当 $p=n$，半正定当且仅当 $p=r$。

**例 7.3.3（配平方）** 合同标准形给出二次型的"平方和"形式：若 $A=T^{\mathsf T}JT$，令 $\boldsymbol{y}=T\boldsymbol{x}$，则

$$
\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}=y_1^2+\cdots+y_p^2-y_{p+1}^2-\cdots-y_r^2,
$$

称为二次型的标准形。实际计算时不必求特征值，逐个变量配方即可（每配一次，剩余部分少一个变量）。例如

$$
x_1^2+x_1x_2+2x_3^2=\Big(x_1+\tfrac12x_2\Big)^2-\tfrac14x_2^2+2x_3^2,
$$

令 $y_1=x_1+\frac12x_2$，$y_2=\frac12x_2$，$y_3=\sqrt2\,x_3$，得 $y_1^2-y_2^2+y_3^2$，惯性指数为 $(2,1,0)$。配方所用的替换不唯一，所得系数也不唯一，但由惯性定律，正、负平方项的个数不变。若用正交替换（谱分解），平方项的系数就是特征值；一般的可逆替换只保证符号。

**例 7.3.4（二元二次函数的驻点）** 对 $f(\boldsymbol{x})=\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$，$A$ 为 2 阶实对称矩阵，$\boldsymbol{0}$ 是驻点，Hesse 矩阵为 $2A$。$A$ 的合同标准形共 6 种：$\operatorname{diag}(1,1)$（极小值，椭圆抛物面）、$\operatorname{diag}(-1,-1)$（极大值）、$\operatorname{diag}(1,-1)$（鞍点，双曲抛物面）、$\operatorname{diag}(1,0)$ 与 $\operatorname{diag}(-1,0)$（抛物柱面，驻点沿一条直线退化）、$\operatorname{diag}(0,0)$（常值函数）。前五种在新坐标 $\boldsymbol{y}$ 下的图像如下。

![五种非零合同标准形对应的二次曲面 z = y^T J y](./plots/quadratic-forms-2d.py)

## 7.4. 奇异值分解

$m\times n$ 矩阵没有特征值，但 $A^{\mathsf T}A$（$n$ 阶）与 $AA^{\mathsf T}$（$m$ 阶）都是对称半正定矩阵，可以做谱分解。由 $\mathcal{N}(A^{\mathsf T}A)=\mathcal{N}(A)$ 得 $\operatorname{rank}(A)=\operatorname{rank}(A^{\mathsf T}A)=\operatorname{rank}(AA^{\mathsf T})$，记为 $r$；于是二者的特征值都非负，且各有 $r$ 个正特征值（计重数）。

**命题 7.4.1** $A^{\mathsf T}A$ 与 $AA^{\mathsf T}$ 有相同的正特征值（计重数），且对应的特征向量可以相互导出。

**证明** 设 $A^{\mathsf T}A\boldsymbol{x}=\lambda\boldsymbol{x}$，$\lambda>0$，$\boldsymbol{x}\neq\boldsymbol{0}$。令 $\boldsymbol{y}=A\boldsymbol{x}$，则 $\boldsymbol{y}\neq\boldsymbol{0}$（否则 $\lambda\boldsymbol{x}=\boldsymbol{0}$），且 $AA^{\mathsf T}\boldsymbol{y}=A(\lambda\boldsymbol{x})=\lambda\boldsymbol{y}$。反过来由 $AA^{\mathsf T}\boldsymbol{y}=\lambda\boldsymbol{y}$ 令 $\boldsymbol{x}=A^{\mathsf T}\boldsymbol{y}$。映射 $\boldsymbol{x}\mapsto A\boldsymbol{x}$ 把 $A^{\mathsf T}A$ 属于 $\lambda$ 的**特征子空间**单射地映入 $AA^{\mathsf T}$ 属于 $\lambda$ 的特征子空间，反之亦然，所以两个特征子空间维数相同；对称矩阵的代数重数等于几何重数，故重数也相同。$\square$

把特征值、特征向量推广到长方矩阵：

**定义 7.4.1（奇异值）** 给定 $m\times n$ 实矩阵 $A$ 和数 $\sigma\ge0$，若存在非零向量 $\boldsymbol{x}\in\mathbb{R}^n$，$\boldsymbol{y}\in\mathbb{R}^m$ 使得 $A\boldsymbol{x}=\sigma\boldsymbol{y}$，$A^{\mathsf T}\boldsymbol{y}=\sigma\boldsymbol{x}$，则称 $\sigma$ 是 $A$ 的一个**奇异值**，$\boldsymbol{x}$ 与 $\boldsymbol{y}$ 分别是 $A$ 的属于 $\sigma$ 的**右奇异向量**与**左奇异向量**。

这时 $A^{\mathsf T}A\boldsymbol{x}=\sigma^2\boldsymbol{x}$，$AA^{\mathsf T}\boldsymbol{y}=\sigma^2\boldsymbol{y}$：右奇异向量是 $A^{\mathsf T}A$ 的特征向量，左奇异向量是 $AA^{\mathsf T}$ 的特征向量，奇异值是对应特征值的算术平方根。

**定理 7.4.1（奇异值分解）** 设 $A$ 是 $m\times n$ 实矩阵，$\operatorname{rank}(A)=r$，则存在 $m$ 阶正交矩阵 $U$ 和 $n$ 阶正交矩阵 $V$，使得 $A=U\Sigma V^{\mathsf T}$，其中

$$
\Sigma=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}_{m\times n},\qquad \Sigma_r=\operatorname{diag}(\sigma_1,\dots,\sigma_r),\qquad \sigma_1\ge\sigma_2\ge\cdots\ge\sigma_r>0.
$$

分解 $A=U\Sigma V^{\mathsf T}$ 称为 $A$ 的奇异值分解，简称 SVD。

**证明** $A^{\mathsf T}A$ 对称半正定，有谱分解 $A^{\mathsf T}A=V\Lambda V^{\mathsf T}$，特征值由大到小排列，记 $\Lambda=\operatorname{diag}(\Sigma_r^2,O)$，其中 $\Sigma_r$ 的对角元为正。分块 $V=[V_1\ V_2]$，$V_1$ 为 $n\times r$，则

$$
V_1^{\mathsf T}A^{\mathsf T}AV_1=\Sigma_r^2,\qquad V_2^{\mathsf T}A^{\mathsf T}AV_2=O,
$$

后者即 $\|AV_2\boldsymbol{z}\|^2=0$ 对一切 $\boldsymbol{z}$ 成立，故 $AV_2=O$。令 $U_1=AV_1\Sigma_r^{-1}$（$m\times r$），则 $U_1^{\mathsf T}U_1=\Sigma_r^{-1}V_1^{\mathsf T}A^{\mathsf T}AV_1\Sigma_r^{-1}=I_r$，即 $U_1$ 的列是标准正交的。把它扩充成正交矩阵 $U=[U_1\ U_2]$，则

$$
U^{\mathsf T}AV=\begin{bmatrix}U_1^{\mathsf T}AV_1&U_1^{\mathsf T}AV_2\\U_2^{\mathsf T}AV_1&U_2^{\mathsf T}AV_2\end{bmatrix}=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}=\Sigma,
$$

其中 $U_1^{\mathsf T}AV_1=\Sigma_r^{-1}V_1^{\mathsf T}A^{\mathsf T}AV_1=\Sigma_r$，$U_2^{\mathsf T}AV_1=U_2^{\mathsf T}U_1\Sigma_r=O$。故 $A=U\Sigma V^{\mathsf T}$。$\square$

记 $U=[\boldsymbol{u}_1\ \cdots\ \boldsymbol{u}_m]=[U_1\ U_2]$，$V=[\boldsymbol{v}_1\ \cdots\ \boldsymbol{v}_n]=[V_1\ V_2]$。由 SVD 可以读出：

- 由 $AV=U\Sigma$、$A^{\mathsf T}U=V\Sigma^{\mathsf T}$ 得 $A\boldsymbol{v}_i=\sigma_i\boldsymbol{u}_i$，$A^{\mathsf T}\boldsymbol{u}_i=\sigma_i\boldsymbol{v}_i$：$\sigma_i$ 是奇异值，$\boldsymbol{u}_i,\boldsymbol{v}_i$ 是相应的左、右奇异向量。
- 简化奇异值分解与秩一展开：
  $$
  A=U_1\Sigma_rV_1^{\mathsf T}=\sigma_1\boldsymbol{u}_1\boldsymbol{v}_1^{\mathsf T}+\cdots+\sigma_r\boldsymbol{u}_r\boldsymbol{v}_r^{\mathsf T},
  $$
  左、右奇异向量相互导出：$U_1=AV_1\Sigma_r^{-1}$，$V_1=A^{\mathsf T}U_1\Sigma_r^{-1}$。
- 四个基本子空间：$\boldsymbol{u}_1,\dots,\boldsymbol{u}_r$ 是**列空间** $\mathcal{R}(A)$ 的标准正交基，$\boldsymbol{v}_1,\dots,\boldsymbol{v}_r$ 是**行空间** $\mathcal{R}(A^{\mathsf T})$ 的标准正交基，$\boldsymbol{u}_{r+1},\dots,\boldsymbol{u}_m$ 是**左零空间** $\mathcal{N}(A^{\mathsf T})$ 的标准正交基，$\boldsymbol{v}_{r+1},\dots,\boldsymbol{v}_n$ 是**零空间** $\mathcal{N}(A)$ 的标准正交基。SVD 同时给出了四个子空间最好的基，并且 $A$ 把行空间的基 $\boldsymbol{v}_i$ 一一映成列空间的基的倍数 $\sigma_i\boldsymbol{u}_i$。
- $A^{\mathsf T}A=V\Sigma^{\mathsf T}\Sigma V^{\mathsf T}$，$AA^{\mathsf T}=U\Sigma\Sigma^{\mathsf T}U^{\mathsf T}$ 分别是二者的谱分解；$A$ 的非零奇异值是 $A^{\mathsf T}A$（或 $AA^{\mathsf T}$）的非零特征值的算术平方根。
- 实对称矩阵的奇异值是特征值的绝对值（由 $A=Q\Lambda Q^{\mathsf T}$，把负特征值的符号移到 $U$ 的列上），对称半正定矩阵的奇异值就是特征值；正交相似的矩阵有相同的特征值与奇异值。若 $A$ 可逆，则 $A^{-1}=V\Sigma^{-1}U^{\mathsf T}$，$A^{-1}$ 的奇异值是 $A$ 的奇异值的倒数。

几何上，$A=U\Sigma V^{\mathsf T}$ 说明任何线性映射都是"旋转（或反射）、沿坐标轴伸缩、再旋转"的复合：$A$ 把单位球面映成以 $\sigma_i\boldsymbol{u}_i$ 为半轴的（退化的）椭球面。下图以例 7.4.1 中的 $2\times2$ 矩阵 $\begin{bmatrix}3&0\\4&5\end{bmatrix}$ 为例，把 $V^{\mathsf T}$、$\Sigma$、$U$ 依次作用于单位圆：$V^{\mathsf T}$ 把右奇异向量 $\boldsymbol{v}_1,\boldsymbol{v}_2$ 转到坐标轴上，$\Sigma$ 沿坐标轴分别伸缩 $\sigma_1,\sigma_2$ 倍，$U$ 再把坐标轴转到 $\boldsymbol{u}_1,\boldsymbol{u}_2$ 方向。

![SVD 的几何意义：单位圆依次经过旋转 V^T、沿坐标轴伸缩 Σ、旋转 U，得到它在 A 下的像；红、绿箭头跟踪 v_1、v_2，最终成为椭圆的半轴 σ_1 u_1、σ_2 u_2（前两幅放大显示）](./plots/svd-rotate-stretch-rotate.py)

**算法 7.4.1（计算奇异值分解）** 输入 $m\times n$ 实矩阵 $A$：

1. 计算 $A^{\mathsf T}A$ 的谱分解 $A^{\mathsf T}A=V\Lambda V^{\mathsf T}$，特征值由大到小排列，$\Lambda=\operatorname{diag}(\Sigma_r^2,O)$；
2. 取 $\Sigma_r$ 为正特征值的算术平方根，$\Sigma=\begin{bmatrix}\Sigma_r&O\\O&O\end{bmatrix}_{m\times n}$；
3. 分块 $V=[V_1\ V_2]$，$V_1$ 为 $n\times r$；
4. 令 $U_1=AV_1\Sigma_r^{-1}$；
5. 把 $U_1$ 扩充成正交矩阵 $U=[U_1\ U_2]$（$U_2$ 的列是 $\mathcal{N}(A^{\mathsf T})$ 的标准正交基）。

若 $m<n$，可以对 $AA^{\mathsf T}$ 做同样的计算以减小规模。这一算法适合手算；数值计算中不应显式形成 $A^{\mathsf T}A$，因为这会把条件数平方、丢失小奇异值的精度，实用的算法（Golub–Kahan 双对角化）直接对 $A$ 做正交变换，运算量为 $O(mn^2)$（$m\ge n$）。

**例 7.4.1** 求 $A=\begin{bmatrix}3&0\\4&5\\0&0\end{bmatrix}$ 的奇异值分解。$A^{\mathsf T}A=\begin{bmatrix}25&20\\20&25\end{bmatrix}$，特征值为 $45,5$，特征向量 $\boldsymbol{v}_1=\frac1{\sqrt2}[1\ 1]^{\mathsf T}$，$\boldsymbol{v}_2=\frac1{\sqrt2}[-1\ 1]^{\mathsf T}$。所以 $\sigma_1=3\sqrt5$，$\sigma_2=\sqrt5$，

$$
U_1=AV\Sigma_r^{-1}=\begin{bmatrix}3&0\\4&5\\0&0\end{bmatrix}\begin{bmatrix}\frac1{\sqrt2}&-\frac1{\sqrt2}\\\frac1{\sqrt2}&\frac1{\sqrt2}\end{bmatrix}\begin{bmatrix}\frac{1}{3\sqrt5}&\\&\frac1{\sqrt5}\end{bmatrix}=\begin{bmatrix}\frac1{\sqrt{10}}&-\frac3{\sqrt{10}}\\\frac3{\sqrt{10}}&\frac1{\sqrt{10}}\\0&0\end{bmatrix}.
$$

补上 $\boldsymbol{u}_3=\boldsymbol{e}_3$，得 $U=[U_1\ \boldsymbol{e}_3]$，$\Sigma=\begin{bmatrix}3\sqrt5&0\\0&\sqrt5\\0&0\end{bmatrix}$，$A=U\Sigma V^{\mathsf T}$。下图左边是 $A$ 的前两行构成的 $2\times2$ 矩阵（奇异值与奇异向量相同）把单位圆映成椭圆的情形。

![左：A 把单位圆映成以 σ_i u_i 为半轴的椭圆；右：一个 80×60 矩阵的截断 SVD 的相对误差随秩 k 的变化](./plots/svd-geometry-low-rank.py)

SVD 是数据分析中最常用的矩阵分解。秩一展开中各项按 $\sigma_i$ 由大到小排列，截取前 $k$ 项就得到 $A$ 的最佳秩 $k$ 近似（定理 7.6.2），这是图像压缩、去噪和推荐系统中"低秩模型"的基础；对中心化的数据矩阵做 SVD，右奇异向量就是主成分方向；奇异值中远小于其余者的个数刻画了数值意义下的秩；下一节的广义逆则统一处理了各种线性方程组与最小二乘问题。

## 7.5. Moore–Penrose 广义逆

**定义 7.5.1（Moore–Penrose 广义逆）** 设 $A\in\mathbb{R}^{m\times n}$，$\operatorname{rank}(A)=r$，有简化奇异值分解 $A=U_r\Sigma_rV_r^{\mathsf T}$。矩阵

$$
A^+=V_r\Sigma_r^{-1}U_r^{\mathsf T}\in\mathbb{R}^{n\times m}
$$

称为 $A$ 的 **Moore–Penrose 广义逆**，简称广义逆或伪逆。（$A=O$ 时规定 $A^+=O$。）

由 $U_r^{\mathsf T}U_r=V_r^{\mathsf T}V_r=I_r$ 立得：

- $AA^+=U_rU_r^{\mathsf T}$ 是向 $\mathcal{R}(A)$ 的**正交投影**的矩阵，$I-AA^+$ 是向 $\mathcal{N}(A^{\mathsf T})$ 的正交投影的矩阵；
- $A^+A=V_rV_r^{\mathsf T}$ 是向 $\mathcal{R}(A^{\mathsf T})$ 的正交投影的矩阵，$I-A^+A$ 是向 $\mathcal{N}(A)$ 的正交投影的矩阵；
- $A$ 可逆时 $A^+=A^{-1}$；$A$ 列满秩时 $A^+=(A^{\mathsf T}A)^{-1}A^{\mathsf T}$；$A$ 行满秩时 $A^+=A^{\mathsf T}(AA^{\mathsf T})^{-1}$。

$A^+$ 不依赖于 SVD 的选取：它是满足 Penrose 条件

$$
AXA=A,\qquad XAX=X,\qquad (AX)^{\mathsf T}=AX,\qquad (XA)^{\mathsf T}=XA
$$

的唯一矩阵 $X$（满足性由上面的投影性质直接验证；若 $X_1,X_2$ 都满足，则 $AX_1=AX_2$ 都是向 $\mathcal{R}(A)$ 的正交投影，$X_1A=X_2A$ 都是向 $\mathcal{R}(A^{\mathsf T})$ 的正交投影，于是 $X_1=X_1AX_1=X_2AX_1=X_2AX_2=X_2$）。

**定理 7.5.1** 对线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$，$\boldsymbol{x}^+=A^+\boldsymbol{b}$ 是长度最小的**最小二乘法**解：最小二乘解的全体为 $\{A^+\boldsymbol{b}+\boldsymbol{x}_0\mid\boldsymbol{x}_0\in\mathcal{N}(A)\}$，且 $\|A^+\boldsymbol{b}+\boldsymbol{x}_0\|^2=\|A^+\boldsymbol{b}\|^2+\|\boldsymbol{x}_0\|^2$。特别地，方程组有解时，$A^+\boldsymbol{b}$ 是长度最小的解；$A$ 可逆时它是唯一解。

**证明** $AA^+\boldsymbol{b}$ 是 $\boldsymbol{b}$ 在 $\mathcal{R}(A)$ 上的正交投影，所以 $A^+\boldsymbol{b}$ 是最小二乘解；等价地，$(I-AA^+)\boldsymbol{b}\in\mathcal{N}(A^{\mathsf T})$ 给出 $A^{\mathsf T}A(A^+\boldsymbol{b})=A^{\mathsf T}\boldsymbol{b}$，即 $A^+\boldsymbol{b}$ 满足**正规方程**（有的教材称解正规方程的方法为"正则化方法"，与统计中的正则化 regularization 不是一回事）。正规方程的解集是一个特解加 $\mathcal{N}(A^{\mathsf T}A)=\mathcal{N}(A)$。最后 $A^+\boldsymbol{b}=V_r(\cdots)\in\mathcal{R}(A^{\mathsf T})\perp\mathcal{N}(A)$，由勾股定理得长度公式。方程组有解时最小二乘解就是解。$\square$

## 7.6. 谱范数与奇异值的稳定性

$A^{\mathsf T}A$ 的 Rayleigh 商是 $\dfrac{\boldsymbol{x}^{\mathsf T}A^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}=\dfrac{\|A\boldsymbol{x}\|^2}{\|\boldsymbol{x}\|^2}$，它度量 $A$ 把向量拉长的倍数。由定理 7.2.1，它的极值是奇异值的平方。

**定义 7.6.1（谱范数）** 对 $m\times n$ 实矩阵 $A$，非负数

$$
\|A\|=\max_{\boldsymbol{x}\neq\boldsymbol{0}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\max_{\|\boldsymbol{x}\|=1}\|A\boldsymbol{x}\|
$$

称为 $A$ 的**谱范数**。

由定义，对任意 $\boldsymbol{x}$ 有 $\|A\boldsymbol{x}\|\le\|A\|\|\boldsymbol{x}\|$（相容性），且存在单位向量 $\boldsymbol{x}_0$ 使 $\|A\|=\|A\boldsymbol{x}_0\|$（单位球面是有界闭集）；正交矩阵 $Q$ 满足 $\|Q\|=1$。

**命题 7.6.1** 设 $A$ 的奇异值（补上零，共 $n$ 个）为 $\sigma_1\ge\cdots\ge\sigma_n\ge0$，相应的右奇异向量 $\boldsymbol{v}_1,\dots,\boldsymbol{v}_n$ 构成 $\mathbb{R}^n$ 的标准正交基，则

$$
\sigma_i=\max_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{v}_i,\dots,\boldsymbol{v}_n)}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}=\min_{\substack{\boldsymbol{x}\neq\boldsymbol{0}\\ \boldsymbol{x}\in\operatorname{span}(\boldsymbol{v}_1,\dots,\boldsymbol{v}_i)}}\frac{\|A\boldsymbol{x}\|}{\|\boldsymbol{x}\|}.
$$

特别地，谱范数等于最大奇异值：$\|A\|=\sigma_1$，即 $A^{\mathsf T}A$ 最大特征值的算术平方根；$\sigma_n=\min\limits_{\boldsymbol{x}\neq\boldsymbol{0}}\|A\boldsymbol{x}\|/\|\boldsymbol{x}\|$。

**证明** 对 $A^{\mathsf T}A$（特征值 $\sigma_1^2\ge\cdots\ge\sigma_n^2$，特征向量 $\boldsymbol{v}_i$）应用定理 7.2.1，再开平方。$\square$

对 $n$ 阶可逆矩阵 $A$，$A^{-1}$ 的最大奇异值是 $1/\sigma_n$，所以 $\|A^{-1}\|=1/\sigma_n$。数 $\kappa(A)=\|A\|\|A^{-1}\|=\sigma_1/\sigma_n\ge1$ 称为 $A$ 的条件数（Condition Number）。它度量解线性方程组的误差放大：若 $A\boldsymbol{x}=\boldsymbol{b}$，$A(\boldsymbol{x}+\delta\boldsymbol{x})=\boldsymbol{b}+\delta\boldsymbol{b}$，则由 $\|\boldsymbol{b}\|\le\|A\|\|\boldsymbol{x}\|$ 与 $\|\delta\boldsymbol{x}\|\le\|A^{-1}\|\|\delta\boldsymbol{b}\|$ 得

$$
\frac{\|\delta\boldsymbol{x}\|}{\|\boldsymbol{x}\|}\le\kappa(A)\frac{\|\delta\boldsymbol{b}\|}{\|\boldsymbol{b}\|}.
$$

正交矩阵的条件数为 $1$，这是 [第 4 章](/2.1.4) 中正交变换数值稳定的原因；而 $\kappa(A^{\mathsf T}A)=\kappa(A)^2$，所以直接解正规方程比用 QR 分解更容易损失精度。

**命题 7.6.2** 谱范数满足：

1. 正定性：$\|A\|\ge0$，且 $\|A\|=0$ 当且仅当 $A=O$；
2. 齐次性：$\|kA\|=|k|\|A\|$；
3. 三角不等式：$\|A+B\|\le\|A\|+\|B\|$；
4. 次乘性：$\|AB\|\le\|A\|\|B\|$；
5. 正交不变性：若 $U,V$ 是正交矩阵，则 $\|UAV^{\mathsf T}\|=\|A\|$。

**证明** 1、2 由定义直接得到。3：取单位向量 $\boldsymbol{x}_0$ 使 $\|A+B\|=\|(A+B)\boldsymbol{x}_0\|$，则 $\|A+B\|\le\|A\boldsymbol{x}_0\|+\|B\boldsymbol{x}_0\|\le\|A\|+\|B\|$。4：取单位向量 $\boldsymbol{x}_0$ 使 $\|AB\|=\|AB\boldsymbol{x}_0\|$，则 $\|AB\|\le\|A\|\|B\boldsymbol{x}_0\|\le\|A\|\|B\|$。5：由 4，$\|UAV^{\mathsf T}\|\le\|U\|\|A\|\|V^{\mathsf T}\|=\|A\|$；又 $A=U^{\mathsf T}(UAV^{\mathsf T})V$，同理 $\|A\|\le\|UAV^{\mathsf T}\|$。$\square$

**定义 7.6.2（矩阵范数）** 满足命题 7.6.2 中条件 1–4 的函数 $\|\cdot\|\colon \mathbb{R}^{m\times n}\to\mathbb{R}$（条件 4 对一切可乘的矩阵对成立）称为**矩阵范数**。

另一个常用的矩阵范数是 Frobenius 范数（Frobenius Norm）$\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{\mathsf T}A)}=\sqrt{\sum_{i,j}a_{ij}^2}$。由**迹**的正交不变性，$\|A\|_{\mathrm{F}}^2=\operatorname{tr}(\Sigma^{\mathsf T}\Sigma)=\sigma_1^2+\cdots+\sigma_r^2$，所以 $\|A\|\le\|A\|_{\mathrm{F}}\le\sqrt r\,\|A\|$。

**定理 7.6.1（奇异值的稳定性）** 设 $A,\tilde A$ 是同型实矩阵，奇异值分别为 $\sigma_1\ge\sigma_2\ge\cdots$ 与 $\tilde\sigma_1\ge\tilde\sigma_2\ge\cdots$，则 $|\tilde\sigma_i-\sigma_i|\le\|\tilde A-A\|$。

这个不等式（Weyl 不等式）的证明需要 Courant–Fischer 极小极大原理，这里从略。它说明奇异值是良态的：矩阵改变多少，奇异值至多改变多少。特征值则不然。

**例 7.6.1（奇异值与特征值的对比）** 设 $J_n(0)$ 是 $n$ 阶 Jordan 块（对角元为 $0$，上次对角线为 $1$），$J_n(0)^{\mathsf T}J_n(0)=\operatorname{diag}(0,1,\dots,1)$，所以 $J_n(0)$ 有 $n$ 重特征值 $0$，奇异值为 $n-1$ 重的 $1$ 和 $1$ 重的 $0$。把 $J_n(0)$ 的 $(n,1)$ 元改为 $10^{-n}$ 得 $\tilde J$，$\|\tilde J-J_n(0)\|=10^{-n}$。这时 $\tilde J^{\mathsf T}\tilde J=\operatorname{diag}(10^{-2n},1,\dots,1)$，奇异值为 $n-1$ 重的 $1$ 和 $10^{-n}$，变化恰为 $10^{-n}$；而特征多项式为 $\lambda^n-10^{-n}$，特征值为 $10^{-1}\mathrm{e}^{2\pi\mathrm{i}j/n}$（$j=1,\dots,n$），变化是 $10^{-1}$，比扰动大 $10^{n-1}$ 倍。一般地，特征值的变化只能估计为 $|\tilde\lambda_i-\lambda_i|\le C_A\|\tilde A-A\|^{1/n}$，其中 $C_A$ 是与 $A,\tilde A$ 有关的常数；所以称特征值不是良态的（病态的）。对称矩阵是例外：若 $A,\tilde A$ 都是实对称矩阵，特征值按大小排列，则同样有 $|\tilde\lambda_i-\lambda_i|\le\|\tilde A-A\|$（也由极小极大原理得到），所以实对称矩阵的特征值问题是良态的。

奇异值的极值刻画还回答了"用低秩矩阵逼近 $A$ 最好能做到多好"。

**定理 7.6.2（Eckart–Young 定理）** 设 $A$ 有 SVD $A=\sum_{i=1}^r\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$，$0\le k<r$，令 $A_k=\sum_{i=1}^k\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$，则

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|=\|A-A_k\|=\sigma_{k+1}.
$$

**证明** $A-A_k=\sum_{i=k+1}^r\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$ 的最大奇异值是 $\sigma_{k+1}$。另一方面，设 $\operatorname{rank}(B)\le k$，则 $\dim\mathcal{N}(B)\ge n-k$，它与 $(k+1)$ 维子空间 $\operatorname{span}(\boldsymbol{v}_1,\dots,\boldsymbol{v}_{k+1})$ 的维数之和大于 $n$，所以有公共的单位向量 $\boldsymbol{x}$。由命题 7.6.1，$\|A-B\|\ge\|(A-B)\boldsymbol{x}\|=\|A\boldsymbol{x}\|\ge\sigma_{k+1}$。$\square$

对 Frobenius 范数也有同样的结论，误差为 $\sqrt{\sigma_{k+1}^2+\cdots+\sigma_r^2}$。上图右边画出了一个奇异值按几何级数衰减的 $80\times60$ 矩阵的截断误差：存储 $A_k$ 只需 $k(m+n+1)$ 个数，而误差随 $k$ 迅速下降，这就是低秩压缩的原理。

## 小结

本章的主线是"用正交矩阵化简"：实对称矩阵在正交相似下化成对角矩阵，二次型在合同下化成平方和，任意矩阵在左右两个正交变换下化成对角矩阵。

| 主题 | 核心结论 | 计算方法 |
|---|---|---|
| 谱分解 | 实对称 $A=Q\Lambda Q^{\mathsf T}=\sum\lambda_i\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf T}$；实方阵正交相似于对角矩阵 ⇔ 对称 | 算法 7.1.1：特征值 + 每个特征子空间内 Gram–Schmidt |
| Rayleigh 商 | $\lambda_1=\max\frac{\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}}{\boldsymbol{x}^{\mathsf T}\boldsymbol{x}}$，$\lambda_n=\min$；$\lambda_i$ 是正交补上的极值 | 正交替换 $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{x}$ |
| 正定矩阵 | 六个等价条件：定义、特征值、$T^{\mathsf T}T$、$LDL^{\mathsf T}$、顺序主子式、顺序主子阵 | Cholesky（算法 7.3.1），$\frac13n^3$，兼作判别 |
| 半正定、不定 | 特征值非负 ⇔ $T^{\mathsf T}T$ ⇔ $D\ge0$；顺序主子式非负不够；不定 ⇒ 有非零 $\boldsymbol{z}$ 使 $\boldsymbol{z}^{\mathsf T}A\boldsymbol{z}=0$ | — |
| 合同 | $X^{\mathsf T}AX$；标准形 $\operatorname{diag}(I_p,-I_{r-p},O)$；惯性定律：$(p,r-p,n-r)$ 是完全不变量 | 配平方或谱分解 |
| 奇异值分解 | $A=U\Sigma V^{\mathsf T}=\sum\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$；奇异向量是四个基本子空间的标准正交基 | 算法 7.4.1：$A^{\mathsf T}A$ 的谱分解 + $U_1=AV_1\Sigma_r^{-1}$ |
| 广义逆 | $A^+=V_r\Sigma_r^{-1}U_r^{\mathsf T}$；$AA^+$、$A^+A$ 是正交投影；$A^+\boldsymbol{b}$ 是最小长度最小二乘解 | 由 SVD |
| 谱范数 | $\Vert A\Vert=\sigma_1$；正交不变；奇异值良态（$\vert\tilde\sigma_i-\sigma_i\vert\le\Vert\tilde A-A\Vert$），特征值一般病态 | — |
| 低秩近似 | $\min_{\operatorname{rank}(B)\le k}\Vert A-B\Vert=\sigma_{k+1}$，由截断 SVD 达到 | 截断 SVD |

三种等价关系的对比：

| 关系 | 定义 | 标准形 | 完全不变量 |
|---|---|---|---|
| 相抵 | $PAQ=B$，$P,Q$ 可逆 | $\operatorname{diag}(I_r,O)$ | 秩 |
| 相似 | $P^{-1}AP=B$，$P$ 可逆 | Jordan 标准形（[第 10 章](/2.1.10)） | 特征值与 Jordan 块结构 |
| 正交相似（实对称） | $Q^{\mathsf T}AQ=B$，$Q$ 正交 | $\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ | 特征值 |
| 合同（实对称） | $X^{\mathsf T}AX=B$，$X$ 可逆 | $\operatorname{diag}(I_p,-I_{r-p},O)$ | 惯性指数 |
