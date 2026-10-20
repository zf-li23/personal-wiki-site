---
title: 数值线性代数
description: 线性方程组、最小二乘问题和特征值问题在计算机上的解法：带选主元的 LU 分解与 Cholesky 分解，投影算子，Gram–Schmidt、Householder 与 Givens 三种 QR 分解，奇异值分解及其应用，幂迭代法与 Schur 形，以及它们的运算量与稳定性。
source_hash: 259ebd0e2170
---

几乎所有统计计算最终都落到线性代数上：回归拟合要解一个**最小二乘**问题，Gauss 似然需要协方差矩阵的行列式和逆矩阵的二次型，主成分是特征向量，[3.5.5](/3.5.5) 的每一步牛顿迭代都要解一个线性方程组。这些问题的理论已在线性代数（[2.1](/2.1)）中建立：**LU 分解**见 [2.1.2](/2.1.2)，正交性与 **QR 分解**见 [2.1.4](/2.1.4)，特征值见 [2.1.6](/2.1.6)，**Cholesky 分解**与**奇异值分解**见 [2.1.7](/2.1.7)，Jordan 形与 Schur 形见 [2.1.10](/2.1.10) 和 [2.1.12](/2.1.12)。本章把同样的分解当作算法来看：怎样计算，要多少次浮点运算，舍入误差（[3.5.1](/3.5.1)）如何在其中传播。全章按三个基本问题分为三部分：线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$（Gauss 消元、选主元、Cholesky 分解），最小二乘问题 $A\boldsymbol{x}\approx\boldsymbol{b}$（投影算子、计算 QR 分解的三种方法、奇异值分解），特征值问题 $A\boldsymbol{x}=\lambda\boldsymbol{x}$（幂迭代法与揭示特征值的分解）。贯穿始终的原则是：没有最好的算法，只有最适合手头问题的算法——速度、稳定性和适用范围往往相互牵制。文中反复使用的 R 函数 `solve`、`chol`、`qr`、`svd`、`eigen` 调用的是 LINPACK 和 LAPACK 中实现下述算法的子程序。

## 3.1. 线性方程组

### 3.1.1. 矩阵乘法

设 $A\in\mathbb{C}^{m\times n}$ 的列为 $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$。矩阵乘向量是各列的线性组合：

$$
\boldsymbol{b}=A\boldsymbol{x}=\sum_{j=1}^n x_j\boldsymbol{a}_j .
$$
同样，$\boldsymbol{x}^{\mathsf T}A$ 是 $A$ 各行的线性组合。若 $B\in\mathbb{C}^{n\times p}$ 的行为 $\boldsymbol{b}_{(1)}^{\mathsf T},\dots,\boldsymbol{b}_{(n)}^{\mathsf T}$，则乘积是外积之和：

$$
AB=\begin{bmatrix}\boldsymbol{a}_1&\cdots&\boldsymbol{a}_n\end{bmatrix}\begin{bmatrix}\boldsymbol{b}_{(1)}^{\mathsf T}\\ \vdots\\ \boldsymbol{b}_{(n)}^{\mathsf T}\end{bmatrix}=\sum_{j=1}^n\boldsymbol{a}_j\boldsymbol{b}_{(j)}^{\mathsf T},
$$
其中每一项 $\boldsymbol{a}_j\boldsymbol{b}_{(j)}^{\mathsf T}$ 都是 $m\times p$ 的秩 1 矩阵。下文的向量化实现正是基于这一观点：用一次外积更新整个子矩阵。

若 $A$ 是可逆方阵，$\boldsymbol{x}=A^{-1}\boldsymbol{b}$ 是满足 $A\boldsymbol{x}=\boldsymbol{b}$ 的唯一向量，即 $\boldsymbol{b}$ 在 $A$ 的列构成的基下的展开系数。因此乘以 $A^{-1}$ 是一次基变换：它把 $\boldsymbol{b}$ 在标准基下的系数换成在基 $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$ 下的系数，乘以 $A$ 则换回来。

性质最好的基变换是**酉矩阵** $Q$，$Q^{\mathsf H}=Q^{-1}$（实情形为**正交矩阵**，$Q^{\mathsf T}=Q^{-1}$）。它的特征值的模都是 $1$，不同特征值的特征向量相互正交；乘以 $Q$ 或 $Q^{\mathsf H}$ 保持内积，因而保持长度和夹角：实情形下它是向量空间的刚性旋转（$\det Q=1$）或反射（$\det Q=-1$）。

**定理 3.1.1（酉不变性）** 对任意 $A\in\mathbb{C}^{m\times n}$ 和酉矩阵 $Q\in\mathbb{C}^{m\times m}$，

$$
\|QA\|_2=\|A\|_2\triangleq\sup_{\boldsymbol{x}\ne\boldsymbol{0}}\frac{\|A\boldsymbol{x}\|_2}{\|\boldsymbol{x}\|_2},\qquad \|QA\|_{\mathrm{F}}=\|A\|_{\mathrm{F}}\triangleq\Bigl(\sum_{i=1}^m\sum_{j=1}^n\lvert a_{ij}\rvert^2\Bigr)^{1/2}.
$$

**证明** 对每个 $\boldsymbol{x}$ 有 $\|QA\boldsymbol{x}\|_2=\|A\boldsymbol{x}\|_2$，得第一式。对第二式，$\|A\|_{\mathrm{F}}^2=\operatorname{tr}(A^{\mathsf H}A)=\sum_j\boldsymbol{a}_j^{\mathsf H}\boldsymbol{a}_j$，而 $(QA)^{\mathsf H}(QA)=A^{\mathsf H}A$。$\square$

正因为有这一不变性，由正交变换构成的算法（QR、SVD）不会放大舍入误差，而由一般三角变换构成的算法则可能放大。

### 3.1.2. 三角方程组

设 $A\in\mathbb{C}^{m\times m}$ 可逆，于是 $A\boldsymbol{x}=\boldsymbol{b}$ 有唯一解 $\boldsymbol{x}=A^{-1}\boldsymbol{b}$。显式求出 $A^{-1}$ 再相乘既浪费（工作量约为下述方法的三倍）又不够精确；Cramer 法则 $x_j=\det A_j/\det A$ 代价更高。关键的观察是：三角方程组很容易解。若 $L$ 是下三角矩阵，$L\boldsymbol{x}=\boldsymbol{b}$ 可用前代法（forward substitution）依次求出 $x_1,x_2,\dots$；若 $U$ 是上三角矩阵，$U\boldsymbol{x}=\boldsymbol{b}$ 可用回代法（back substitution）从 $x_m$ 向上求解：

$$
x_i=\frac1{l_{ii}}\Bigl(b_i-\sum_{j<i}l_{ij}x_j\Bigr),\qquad x_i=\frac1{u_{ii}}\Bigl(b_i-\sum_{j>i}u_{ij}x_j\Bigr).
$$

```r
for_sub <- function(L, b) {
  n <- length(b)
  x <- rep(0, n)
  x[1] <- b[1] / L[1, 1]
  for (i in 2:n) {
    tmp <- b[i]
    for (j in 1:(i - 1)) tmp <- tmp - L[i, j] * x[j]
    x[i] <- tmp / L[i, i]
  }
  return(x)
}

back_sub <- function(U, b) {
  n <- length(b)
  x <- rep(0, n)
  for (i in n:1) {
    tmp <- b[i]
    for (j in i:n) tmp <- tmp - U[i, j] * x[j]   # x[i] is still 0 here
    x[i] <- tmp / U[i, i]
  }
  return(x)
}
```

第 $k$ 行约需 $2k$ 次运算，故每解一个三角方程组需 $\sum_{k=1}^m2k\sim m^2$ 次浮点运算（基础 R 中有编译实现的 `forwardsolve` 和 `backsolve`）。对一般的 $A$，策略是把它分解为三角矩阵的乘积。

### 3.1.3. Gauss 消元法与 LU 分解

**定义 3.1.1（Gauss 消元法）** **Gauss 消元法**在左边施加简单的线性变换，把方阵方程组化为上三角方程组：第 $k$ 步对每个 $j>k$，从第 $j$ 行减去第 $k$ 行的 $l_{jk}=x_{jk}/x_{kk}$ 倍，其中 $x_{jk}$ 表示第 $k$ 步开始时矩阵的元素，$x_{kk}$ 称为**主元**。写成矩阵形式即 $L_{m-1}\cdots L_2L_1A=U$，其中

$$
L_k=I-\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T},\qquad \boldsymbol{\ell}_k=(0,\dots,0,l_{k+1,k},\dots,l_{mk})^{\mathsf T}.
$$
令 $L=L_1^{-1}L_2^{-1}\cdots L_{m-1}^{-1}$，就得到 **LU 分解** $A=LU$，$L$ 为单位下三角矩阵，$U$ 为上三角矩阵。

**例 3.1.1** 对

$$
A=\begin{bmatrix}2&1&1&0\\4&3&3&1\\8&7&9&5\\6&7&9&8\end{bmatrix},\qquad L_1A=\begin{bmatrix}1&&&\\-2&1&&\\-4&&1&\\-3&&&1\end{bmatrix}A=\begin{bmatrix}2&1&1&0\\&1&1&1\\&3&5&5\\&4&6&8\end{bmatrix},
$$
再用 $L_2=\begin{bmatrix}1&&&\\&1&&\\&-3&1&\\&-4&&1\end{bmatrix}$ 和 $L_3=\begin{bmatrix}1&&&\\&1&&\\&&1&\\&&-1&1\end{bmatrix}$ 完成消元：

$$
A=\begin{bmatrix}1&&&\\2&1&&\\4&3&1&\\3&4&1&1\end{bmatrix}\begin{bmatrix}2&1&1&0\\&1&1&1\\&&2&2\\&&&2\end{bmatrix}=LU .
$$

因子 $L$ 不需任何计算就能得到，这要归功于两个"好运气"。

**命题 3.1.1（两个好运气）** (a) $L_k^{-1}=I+\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T}$，只需把 $L_k$ 的次对角元变号。(b) $L=L_1^{-1}\cdots L_{m-1}^{-1}$ 是把各乘子 $l_{jk}$ 填到相应位置所得的单位下三角矩阵。

**证明** (a) $(I-\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T})(I+\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T})=I-\boldsymbol{\ell}_k(\boldsymbol{e}_k^{\mathsf T}\boldsymbol{\ell}_k)\boldsymbol{e}_k^{\mathsf T}=I$，因为 $\boldsymbol{\ell}_k$ 的第 $k$ 个分量为零。(b) 同理，$k<k'$ 时 $\boldsymbol{e}_k^{\mathsf T}\boldsymbol{\ell}_{k'}=0$，乘积中的交叉项全部消失，故 $L=I+\sum_k\boldsymbol{\ell}_k\boldsymbol{e}_k^{\mathsf T}$。$\square$

**算法 3.1.1（不选主元的 Gauss 消元法）** 令 $U=A$，$L=I$。对 $k=1,\dots,m-1$：对 $j=k+1,\dots,m$，令 $l_{jk}=u_{jk}/u_{kk}$，$u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$。写成向量化形式，第 $k$ 步先算出乘子列 $\boldsymbol{l}=u_{(k+1):m,k}/u_{kk}$，再用一次外积更新右下子矩阵：$u_{(k+1):m,k:m}\leftarrow u_{(k+1):m,k:m}-\boldsymbol{l}\,u_{k,k:m}$。

```r
# Input: a square matrix A whose leading principal minors are nonzero
# Output: unit lower triangular L and upper triangular U with A = LU
lu <- function(A) {
  m <- nrow(A)
  if (ncol(A) != m) stop("A must be square")
  L <- diag(m)
  U <- as.matrix(A)
  for (k in 1:(m - 1)) {
    multiplier <- U[(k + 1):m, k] / U[k, k]          # (m-k) x 1
    L[(k + 1):m, k] <- multiplier
    # outer product update: (m-k) x 1 times 1 x (m-k+1)
    U[(k + 1):m, k:m] <- U[(k + 1):m, k:m] - multiplier %*% U[k, k:m, drop = FALSE]
  }
  return(list(L = L, U = U))
}

A <- matrix(c(2, 1, 1, 0,
              4, 3, 3, 1,
              8, 7, 9, 5,
              6, 7, 9, 8), nrow = 4, byrow = TRUE)
out <- lu(A)
out$L %*% out$U    # equals A
```

一个算法在计算机上要运行多久？没有既简单又全面的回答；经典的度量是数浮点运算的次数。

**定义 3.1.2（浮点运算次数）** 一次 **flop**（浮点运算）是浮点数的一次加、减、乘、除或开方。计数时不区分实数与复数运算，也不考虑内存访问等其他性能因素；结果只报告首项，$f\sim g$ 表示维数趋于无穷时 $f/g\to1$。

算法 3.1.1 的主要工作量在更新 $u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$：对 $m-k+1$ 个元素各做一次乘法和一次减法。因此总量为

$$
\sum_{k=1}^{m-1}\sum_{j=k+1}^m2(m-k+1)=\sum_{k=1}^{m-1}2(m-k+1)(m-k)\sim\frac23m^3\ \text{flops}.
$$
得到 $A=LU$ 后，$A\boldsymbol{x}=\boldsymbol{b}$ 化为 $LU\boldsymbol{x}=\boldsymbol{b}$：先用前代法解 $L\boldsymbol{y}=\boldsymbol{b}$，再用回代法解 $U\boldsymbol{x}=\boldsymbol{y}$，合计 $\sim2m^2$ flops。总工作量由分解主导，为 $\sim\frac23m^3$ flops，而且同一分解可以用于多个右端项。

**注 3.1.1** 可逆矩阵 $A$ 有单位下三角 $L$ 的 LU 分解（且此时唯一），当且仅当它的 $1,\dots,m-1$ 阶**顺序主子式**都不为零（[2.1.2](/2.1.2)）；否则某个主元 $u_{kk}$ 会等于零。这正是选主元的动机。

### 3.1.4. 选主元

不选主元的 Gauss 消元法不仅对某些矩阵无法进行，而且是不稳定的。矩阵

$$
A=\begin{bmatrix}0&1\\1&1\end{bmatrix}
$$
满秩且良态（它的奇异值 `svd(A)$d` 为 $1.618$ 和 $0.618$），消元却在第一步就失败。稍加扰动便暴露出一般的问题：

$$
A=\begin{bmatrix}10^{-20}&1\\1&1\end{bmatrix}\ \Longrightarrow\ L=\begin{bmatrix}1&0\\10^{20}&1\end{bmatrix},\quad U=\begin{bmatrix}10^{-20}&1\\0&1-10^{20}\end{bmatrix}.
$$
在双精度下 $1-10^{20}$ 舍入为 $-10^{20}$（在 R 中 `1 - 10^20 == -10^20` 为 `TRUE`，而 `1 - 10^10 == -10^10` 为 `FALSE`），所以计算机存储的是

$$
\tilde L=\begin{bmatrix}1&0\\10^{20}&1\end{bmatrix},\quad \tilde U=\begin{bmatrix}10^{-20}&1\\0&-10^{20}\end{bmatrix},\qquad \tilde L\tilde U=\begin{bmatrix}10^{-20}&1\\1&0\end{bmatrix}.
$$
两个因子各自只有极小的相对误差，乘积却完全丢掉了 $A$ 的 $(2,2)$ 元：微小的主元在 $L$ 和 $U$ 中产生了巨大的元素，而巨大元素的舍入误差与 $A$ 的元素同量级。这个算法不是后向稳定的。

**定义 3.1.3（列主元）** 在**列主元**（部分选主元）Gauss 消元法中，第 $k$ 步选第 $k$ 列对角线及以下模最大的元素 $\lvert u_{ik}\rvert=\max_{j\ge k}\lvert u_{jk}\rvert$ 作主元，消元前先交换第 $i$ 行与第 $k$ 行。只交换行；用置换矩阵 $P_k$ 表示即

$$
L_{m-1}P_{m-1}\cdots L_2P_2L_1P_1A=U .
$$
在**全主元**中，主元取整个右下子矩阵中模最大的元素，行和列都要置换：$L_{m-1}P_{m-1}\cdots L_1P_1AC_1\cdots C_{m-1}=U$，即 $PAC=LU$。

选列主元后所有乘子满足 $\lvert l_{jk}\rvert\le1$。置换可以移到右边，这是第三个好运气：

$$
L_{m-1}P_{m-1}\cdots L_2P_2L_1P_1=L'_{m-1}\cdots L'_2L'_1\,P_{m-1}\cdots P_2P_1,\qquad L'_k=P_{m-1}\cdots P_{k+1}L_kP_{k+1}^{-1}\cdots P_{m-1}^{-1}.
$$
例如 $L_3P_3L_2P_2L_1P_1=L'_3L'_2L'_1P_3P_2P_1$，其中 $L'_3=L_3$，$L'_2=P_3L_2P_3^{-1}$，$L'_1=P_3P_2L_1P_2^{-1}P_3^{-1}$。由于 $P_{k+1},\dots,P_{m-1}$ 只置换下标大于 $k$ 的行和列，每个 $L'_k$ 与 $L_k$ 结构相同，只是次对角元被重新排列。记 $L^{-1}=L'_{m-1}\cdots L'_1$，$P=P_{m-1}\cdots P_1$，便得到分解

$$
PA=LU .
$$

**算法 3.1.2（列主元 Gauss 消元法）** 令 $U=A$，$L=I$，$P=I$。对 $k=1,\dots,m-1$：选 $i\ge k$ 使 $\lvert u_{ik}\rvert$ 最大；若 $u_{ik}=0$ 则直接进入下一个 $k$；否则交换 $u_{k,k:m}\leftrightarrow u_{i,k:m}$、$l_{k,1:k-1}\leftrightarrow l_{i,1:k-1}$ 和 $p_{k,:}\leftrightarrow p_{i,:}$，然后对 $j=k+1,\dots,m$ 令 $l_{jk}=u_{jk}/u_{kk}$，$u_{j,k:m}=u_{j,k:m}-l_{jk}u_{k,k:m}$。

任何方阵，无论是否奇异，都有这样的分解。实际计算中 $P$ 并不作为矩阵存储：每步直接交换行，只记录置换。寻找主元需 $O(m^2)$ 次比较，与消元的 $\sim\frac23m^3$ flops 相比可以忽略。全主元需要 $O(m^3)$ 次比较，而对稳定性的改善很有限，所以很少使用。R 的 `solve(A, b)` 调用 LAPACK 子程序 `dgesv`，即列主元 Gauss 消元法；`Matrix::lu()` 返回各因子。

### 3.1.5. Cholesky 分解

**定理 3.1.2（Cholesky 分解）** 每个 Hermite **正定矩阵** $A$ 都有唯一的分解

$$
A=R^{\mathsf H}R,\qquad r_{jj}>0,
$$
其中 $R$ 为上三角矩阵。

统计中的数据通常是实数，"Hermite"便成为"对称"，$A=R^{\mathsf T}R$。回顾相关事实：**对称矩阵**的特征值为实数、特征向量相互正交；对称正定（SPD）矩阵还有正的特征值、正的对角元和消元中正的主元，对 $\boldsymbol{x}\ne\boldsymbol{0}$ 满足 $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}>0$，主子阵都正定，对任意列满秩的 $X$，$X^{\mathsf T}AX$ 仍是 SPD 矩阵，顺序主子式都为正（Sylvester 判据）。

Cholesky 分解是 Gauss 消元法的变体，它同时在矩阵的左右两边操作，从而保持并利用对称性。记

$$
A=\begin{bmatrix}a_{11}&\boldsymbol{w}^{\mathsf H}\\\boldsymbol{w}&K\end{bmatrix},\qquad \alpha=\sqrt{a_{11}} .
$$
在两边各做一步消元，得

$$
A=\begin{bmatrix}\alpha&0\\\boldsymbol{w}/\alpha&I\end{bmatrix}\begin{bmatrix}1&0\\0&K-\boldsymbol{w}\boldsymbol{w}^{\mathsf H}/a_{11}\end{bmatrix}\begin{bmatrix}\alpha&\boldsymbol{w}^{\mathsf H}/\alpha\\0&I\end{bmatrix}=R_1^{\mathsf H}A_1R_1 .
$$
子矩阵 $K-\boldsymbol{w}\boldsymbol{w}^{\mathsf H}/a_{11}$ 即 $a_{11}$ 的 **Schur 补**，它仍是正定的（它是 $A_1=R_1^{-\mathsf H}AR_1^{-1}$ 的主子阵），所以这一过程可以一直进行到右下角，最终得到 $A=R_1^{\mathsf H}R_2^{\mathsf H}\cdots R_m^{\mathsf H}\,R_m\cdots R_2R_1=R^{\mathsf H}R$。

**算法 3.1.3（Cholesky 分解）** 令 $R$ 为 $A$ 的上三角部分。对 $k=1,\dots,m$：对 $j=k+1,\dots,m$，令 $R_{j,j:m}=R_{j,j:m}-R_{k,j:m}\bar R_{kj}/R_{kk}$；然后令 $R_{k,k:m}=R_{k,k:m}/\sqrt{R_{kk}}$。

内层更新涉及 $m-j+1$ 个元素，每个两次运算，工作量为

$$
\sum_{k=1}^m\sum_{j=k+1}^m2(m-j+1)\sim2\sum_{k=1}^m\sum_{j=1}^{m-k}j\sim\sum_{k=1}^mk^2\sim\frac13m^3\ \text{flops},
$$
是 Gauss 消元法的一半。该算法总是稳定的：由于 $\|R\|_2=\|R^{\mathsf H}\|_2=\|A\|_2^{1/2}$，不会出现比 $A$ 的元素大得多的数；又因为正定矩阵的"分量"大多集中在对角线上，不需要选主元。对 SPD 矩阵 $A$，解 $A\boldsymbol{x}=\boldsymbol{b}$ 的标准方法是把它化为 $R^{\mathsf H}R\boldsymbol{x}=\boldsymbol{b}$，依次解 $R^{\mathsf H}\boldsymbol{y}=\boldsymbol{b}$ 和 $R\boldsymbol{x}=\boldsymbol{y}$；每个三角方程组只需 $\sim m^2$ flops，总量仍为 $\sim\frac13m^3$ flops，整个过程是后向稳定的。

**例 3.1.2（滑动平均过程的似然）** 设 $\varepsilon_t$（$t\in\mathbb{Z}$）独立同分布于 $\mathcal{N}(0,\delta)$（方差为 $\delta>0$ 的 Gauss 白噪声），$0<b<1$。过程 $X_t=\varepsilon_t+b\varepsilon_{t-1}$ 是一阶滑动平均过程 MA(1)。对 $\boldsymbol{X}=(X_1,\dots,X_n)^{\mathsf T}$，有 $\mathbb{E}\boldsymbol{X}=\boldsymbol{0}$ 和三对角协方差矩阵

$$
\Sigma=\operatorname{Cov}(\boldsymbol{X})=\delta\begin{bmatrix}1+b^2&b&&\\b&1+b^2&\ddots&\\&\ddots&\ddots&b\\&&b&1+b^2\end{bmatrix},
$$
故观测值 $\boldsymbol{X}=\boldsymbol{x}$ 的对数似然为

$$
\log L(b,\delta)=-\frac n2\log(2\pi)-\frac12\log\det\Sigma-\frac12\boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}.
$$
数值极大化时要在许多 $(b,\delta)$ 处计算它，既不应直接计算行列式，也不应直接求逆。利用 Cholesky 分解 $\Sigma=LL^{\mathsf T}$（$L=R^{\mathsf T}$ 为下三角矩阵），

$$
\det\Sigma=(\det L)^2=(l_{11}\cdots l_{nn})^2,\qquad \boldsymbol{x}^{\mathsf T}\Sigma^{-1}\boldsymbol{x}=(L^{-1}\boldsymbol{x})^{\mathsf T}(L^{-1}\boldsymbol{x})=\boldsymbol{y}^{\mathsf T}\boldsymbol{y},
$$
其中 $\boldsymbol{y}=L^{-1}\boldsymbol{x}$ 由前代法求得。

```r
ma1_loglik <- function(b, delta, x) {
  n <- length(x)
  Sigma <- diag(delta * (1 + b^2), n)
  Sigma[cbind(1:(n - 1), 2:n)] <- delta * b
  Sigma[cbind(2:n, 1:(n - 1))] <- delta * b
  R <- chol(Sigma)                          # Sigma = t(R) %*% R, R upper triangular
  y <- backsolve(R, x, transpose = TRUE)    # solves t(R) y = x
  -n / 2 * log(2 * pi) - sum(log(diag(R))) - sum(y^2) / 2
}
```

**例 3.1.3** $\rho$ 取何值时

$$
C=\begin{bmatrix}1&0.6&-0.3\\0.6&1&\rho\\-0.3&\rho&1\end{bmatrix}
$$
是相关矩阵？它必须是对称半正定矩阵。由 Sylvester 判据，一、二阶顺序主子式 $1$ 和 $1-0.36$ 为正，$\det C=-\rho^2-0.36\rho+0.55\ge0$ 给出 $-0.9432\le\rho\le0.5832$。另一种做法：Cholesky 分解的第一步留下 Schur 补

$$
\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}-\begin{bmatrix}0.6\\-0.3\end{bmatrix}\begin{bmatrix}0.6&-0.3\end{bmatrix}=\begin{bmatrix}0.64&\rho+0.18\\\rho+0.18&0.91\end{bmatrix},
$$
它半正定当且仅当 $0.5824-(\rho+0.18)^2\ge0$，即 $\lvert\rho+0.18\rvert\le0.7632$，得到同一区间。对半正定矩阵，R 提供选主元的版本 `chol(A, pivot = TRUE)`。

## 3.2. 最小二乘问题

### 3.2.1. 最小二乘问题

秩为 $r$ 的矩阵 $A\in\mathbb{R}^{m\times n}$ 把 $\mathbb{R}^n$ 映到 $\mathbb{R}^m$，它的四个基本子空间刻画了这个映射：$\mathbb{R}^n$ 中有维数为 $r$ 的行空间 $\mathcal{R}(A^{\mathsf T})$ 和维数为 $n-r$ 的零空间 $\mathcal{N}(A)$；$\mathbb{R}^m$ 中有维数为 $r$ 的**列空间** $\mathcal{R}(A)$ 和维数为 $m-r$ 的左零空间 $\mathcal{N}(A^{\mathsf T})$。每一对子空间互为正交补。每个 $\boldsymbol{x}=\boldsymbol{x}_r+\boldsymbol{x}_n$ 都分解为行空间部分与零空间部分，且 $A\boldsymbol{x}=A\boldsymbol{x}_r$；方程组 $A\boldsymbol{x}=\boldsymbol{b}$ 只有在 $\boldsymbol{b}\in\mathcal{R}(A)$ 时才有解。

方程个数多于未知数（$m>n$）的超定方程组通常无解。约 1800 年 Gauss 和 Legendre 提出的最小二乘思想是用

$$
\min_{\boldsymbol{x}}\|\boldsymbol{b}-A\boldsymbol{x}\|_2
$$
来"解"它。

**定理 3.2.1（最小二乘与正规方程）** 设 $A\in\mathbb{C}^{m\times n}$（$m\ge n$），$\boldsymbol{b}\in\mathbb{C}^m$。向量 $\boldsymbol{x}\in\mathbb{C}^n$ 使残差范数 $\|\boldsymbol{r}\|_2=\|\boldsymbol{b}-A\boldsymbol{x}\|_2$ 最小，当且仅当 $\boldsymbol{r}\perp\mathcal{R}(A)$，即 $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{0}$，或等价地

$$
A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b},
$$
又等价于 $P\boldsymbol{b}=A\boldsymbol{x}$，其中 $P\in\mathbb{C}^{m\times m}$ 是到 $\mathcal{R}(A)$ 上的正交投影算子。方程组 $A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b}$ 非奇异当且仅当 $A$ **满秩**，此时解唯一。

**证明** 若 $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{0}$，则对任意 $\boldsymbol{y}$，$\boldsymbol{b}-A\boldsymbol{y}=\boldsymbol{r}+A(\boldsymbol{x}-\boldsymbol{y})$ 的两项正交，于是 $\|\boldsymbol{b}-A\boldsymbol{y}\|_2^2=\|\boldsymbol{r}\|_2^2+\|A(\boldsymbol{x}-\boldsymbol{y})\|_2^2\ge\|\boldsymbol{r}\|_2^2$。反之，若 $A^{\mathsf H}\boldsymbol{r}=\boldsymbol{z}\ne\boldsymbol{0}$，取 $\boldsymbol{y}=\boldsymbol{x}+t\boldsymbol{z}$，$t>0$ 充分小，则 $\|\boldsymbol{b}-A\boldsymbol{y}\|_2^2=\|\boldsymbol{r}\|_2^2-2t\|\boldsymbol{z}\|_2^2+t^2\|A\boldsymbol{z}\|_2^2<\|\boldsymbol{r}\|_2^2$。最后，$A^{\mathsf H}A$ 非奇异当且仅当 $A\boldsymbol{z}=\boldsymbol{0}$ 只有零解。$\square$

几何上，$\boldsymbol{y}=A\boldsymbol{x}=P\boldsymbol{b}$ 是 $\mathcal{R}(A)$ 中离 $\boldsymbol{b}$ 最近的点。这就是 [3.3.7](/3.3.7) 中最小二乘回归的矩阵形式。为了理解 $P$，我们来研究投影算子。

### 3.2.2. 投影算子

从合适的方向把光照向一个子空间，向量 $\boldsymbol{v}$ 的影子就是它的投影 $P\boldsymbol{v}$；对影子再投影一次，不会有任何变化。

**定义 3.2.1（投影算子）** 满足 $P^2=P$（幂等）的方阵 $P$ 称为**投影算子**。矩阵 $I-P$ 称为 $P$ 的**互补投影**。若 $\mathcal{R}(P)$ 与 $\mathcal{N}(P)$ 正交，则称投影算子 $P$ 为**正交投影算子**，否则称为斜投影。

光线的方向是 $P\boldsymbol{v}-\boldsymbol{v}$，它属于 $\mathcal{N}(P)$，因为 $\mathbb{P}(P\boldsymbol{v}-\boldsymbol{v})=(P^2-P)\boldsymbol{v}=\boldsymbol{0}$。斜投影与正交投影的区别在于投影线是否与投影平面垂直。注意正交投影算子不是正交矩阵（除非 $P=I$）。

**命题 3.2.1** 设 $P\in\mathbb{C}^{m\times m}$ 为投影算子。

1. 它的特征值为 $0$ 和 $1$，且可对角化，因为 $P^2-P=\mathbb{P}(P-I)=O$ 而多项式 $z(z-1)$ 的根互不相同；因此 $\operatorname{tr}(P)=\operatorname{rank}(P)$。
2. 除 $P=I$ 外，$P$ 都是奇异的：若 $P^{-1}$ 存在，则 $P=P^{-1}P^2=I$。
3. $I-P$ 也是投影算子，$\mathcal{R}(I-P)=\mathcal{N}(P)$，$\mathcal{N}(I-P)=\mathcal{R}(P)$，且 $\mathcal{R}(P)\cap\mathcal{N}(P)=\{\boldsymbol{0}\}$。因此 $\mathbb{C}^m=\mathcal{R}(P)\oplus\mathcal{N}(P)$：$P$ 沿 $\mathcal{N}(P)$ 投影到 $\mathcal{R}(P)$ 上，每个 $\boldsymbol{v}$ 都唯一地分解为 $\boldsymbol{v}=P\boldsymbol{v}+(I-P)\boldsymbol{v}$。

**定理 3.2.2** 投影算子 $P$ 是正交投影算子当且仅当 $P=P^{\mathsf H}$。

**证明** 若 $P=P^{\mathsf H}$，则 $(P\boldsymbol{x})^{\mathsf H}(I-P)\boldsymbol{y}=\boldsymbol{x}^{\mathsf H}(P-P^2)\boldsymbol{y}=0$，所以 $\mathcal{R}(P)\perp\mathcal{R}(I-P)=\mathcal{N}(P)$。反之，若 $P$ 是正交投影算子，则对所有 $\boldsymbol{x},\boldsymbol{y}$，$\langle P\boldsymbol{x},\boldsymbol{y}-P\boldsymbol{y}\rangle=\langle\boldsymbol{x}-P\boldsymbol{x},P\boldsymbol{y}\rangle=0$；于是 $\langle P\boldsymbol{x},\boldsymbol{y}\rangle=\langle P\boldsymbol{x},P\boldsymbol{y}\rangle=\langle\boldsymbol{x},P\boldsymbol{y}\rangle=\langle P^{\mathsf H}\boldsymbol{x},\boldsymbol{y}\rangle$，即 $P=P^{\mathsf H}$。$\square$

所以正交投影算子就是 Hermite（实情形下为对称）的幂等矩阵。实对称矩阵有谱分解 $A=Q\Lambda Q^{\mathsf T}$（$Q$ 正交），而 $P$ 的特征值为 $0$ 和 $1$，故每个秩为 $n$ 的正交投影算子都形如

$$
P=\hat Q\hat Q^{\mathsf T}=\sum_{j=1}^n\boldsymbol{q}_j\boldsymbol{q}_j^{\mathsf T},
$$
其中 $\hat Q\in\mathbb{R}^{m\times n}$ 的列 $\boldsymbol{q}_1,\dots,\boldsymbol{q}_n$ 标准正交。特别地：

- 对单位向量 $\boldsymbol{q}$，秩 1 正交投影算子 $P_{\boldsymbol{q}}=\boldsymbol{q}\boldsymbol{q}^{\mathsf T}$ 分离出 $\boldsymbol{q}$ 方向的分量 $P\boldsymbol{v}=\boldsymbol{q}(\boldsymbol{q}^{\mathsf T}\boldsymbol{v})$，它的补 $P_{\perp\boldsymbol{q}}=I-\boldsymbol{q}\boldsymbol{q}^{\mathsf T}$（秩为 $m-1$）则消去这一分量；
- 对任意非零向量 $\boldsymbol{a}$，$P_{\boldsymbol{a}}=\dfrac{\boldsymbol{a}\boldsymbol{a}^{\mathsf T}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$，$P_{\perp\boldsymbol{a}}=I-\dfrac{\boldsymbol{a}\boldsymbol{a}^{\mathsf T}}{\boldsymbol{a}^{\mathsf T}\boldsymbol{a}}$。

对线性无关向量 $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$（即 $A=[\boldsymbol{a}_1|\cdots|\boldsymbol{a}_n]$ 的列）张成的子空间，设 $\boldsymbol{y}=A\boldsymbol{x}$ 是 $\boldsymbol{v}$ 在 $\mathcal{R}(A)$ 上的正交投影。则 $\boldsymbol{v}-\boldsymbol{y}\perp\mathcal{R}(A)$，即对每个 $j$ 有 $\boldsymbol{a}_j^{\mathsf T}(\boldsymbol{v}-A\boldsymbol{x})=0$，也即 $A^{\mathsf T}(\boldsymbol{v}-A\boldsymbol{x})=\boldsymbol{0}$。于是 $\boldsymbol{x}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{v}$，$P\boldsymbol{v}=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}\boldsymbol{v}$，

$$
P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T},
$$
$n=1$ 时它化为 $\boldsymbol{a}\boldsymbol{a}^{\mathsf T}/(\boldsymbol{a}^{\mathsf T}\boldsymbol{a})$。在线性回归 $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$ 中，它就是**帽子矩阵** $H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$（[3.3.7](/3.3.7)）。

### 3.2.3. QR 分解

许多应用关心 $A$ 的列依次张成的空间 $\langle\boldsymbol{a}_1\rangle\subseteq\langle\boldsymbol{a}_1,\boldsymbol{a}_2\rangle\subseteq\cdots$。QR 分解的想法是构造标准正交向量 $\boldsymbol{q}_1,\boldsymbol{q}_2,\dots$ 依次张成这些空间。

**定义 3.2.2（约化 QR 分解与完全 QR 分解）** 设 $A\in\mathbb{C}^{m\times n}$，$m\ge n$。**约化 QR 分解**是分解

$$
A=\hat Q\hat R,\qquad \begin{bmatrix}\boldsymbol{a}_1&\cdots&\boldsymbol{a}_n\end{bmatrix}=\begin{bmatrix}\boldsymbol{q}_1&\cdots&\boldsymbol{q}_n\end{bmatrix}\begin{bmatrix}r_{11}&r_{12}&\cdots&r_{1n}\\&r_{22}&\cdots&r_{2n}\\&&\ddots&\vdots\\&&&r_{nn}\end{bmatrix},
$$
其中 $\hat Q\in\mathbb{C}^{m\times n}$ 的列标准正交，$\hat R\in\mathbb{C}^{n\times n}$ 为上三角矩阵。**完全 QR 分解** $A=QR$ 给 $\hat Q$ 添上 $m-n$ 个标准正交列，使之成为酉矩阵 $Q\in\mathbb{C}^{m\times m}$，并给 $\hat R$ 添上 $m-n$ 行零，使 $R\in\mathbb{C}^{m\times n}$ 仍为上三角形。

若 $A$ 满秩 $n$，则 $r_{jj}\ne0$，且对每个 $j$ 有 $\langle\boldsymbol{a}_1,\dots,\boldsymbol{a}_j\rangle=\langle\boldsymbol{q}_1,\dots,\boldsymbol{q}_j\rangle$。逐列比较即得 **Gram–Schmidt 正交化**：

$$
\boldsymbol{q}_1=\frac{\boldsymbol{a}_1}{r_{11}},\quad \boldsymbol{q}_2=\frac{\boldsymbol{a}_2-r_{12}\boldsymbol{q}_1}{r_{22}},\quad\dots,\quad \boldsymbol{q}_n=\frac{\boldsymbol{a}_n-\sum_{i=1}^{n-1}r_{in}\boldsymbol{q}_i}{r_{nn}},
$$
其中 $r_{ij}=\boldsymbol{q}_i^{\mathsf H}\boldsymbol{a}_j$（$i<j$），$r_{jj}=\bigl\|\boldsymbol{a}_j-\sum_{i=1}^{j-1}r_{ij}\boldsymbol{q}_i\bigr\|_2$。完全 QR 分解中添加的列 $\boldsymbol{q}_{n+1},\dots,\boldsymbol{q}_m$ 构成 $\mathcal{N}(A^{\mathsf H})$（$\mathcal{R}(A)$ 的正交补）的一组标准正交基。

**定理 3.2.3（存在性与唯一性）** (a) 每个 $A\in\mathbb{C}^{m\times n}$（$m\ge n$）都有完全 QR 分解，因而也有约化 QR 分解。(b) 每个满秩的 $A\in\mathbb{C}^{m\times n}$（$m\ge n$）有唯一的满足 $r_{jj}>0$ 的约化 QR 分解 $A=\hat Q\hat R$。

存在性的证明由 Gram–Schmidt 算法本身给出（某个 $r_{jj}=0$ 时，任取一个与前面的 $\boldsymbol{q}_i$ 都正交的单位向量即可）。$m<n$ 时 QR 分解同样存在：$A=Q\begin{bmatrix}R_1&R_2\end{bmatrix}$，$R_1$ 是 $m\times m$ 上三角块，其后是列 $Q^{-1}\boldsymbol{a}_{m+1},Q^{-1}\boldsymbol{a}_{m+2},\dots$。

另一个简短的存在性证明利用 Cholesky 分解：若 $A$ 满秩且 $A^{\mathsf T}A=R^{\mathsf T}R$，则 $A=(AR^{-1})R$ 是约化 QR 分解，因为

$$
(AR^{-1})^{\mathsf T}(AR^{-1})=R^{-\mathsf T}A^{\mathsf T}AR^{-1}=R^{-\mathsf T}R^{\mathsf T}RR^{-1}=I .
$$
（另一个乘积 $(AR^{-1})(AR^{-1})^{\mathsf T}$ 是到 $\mathcal{R}(A)$ 上的投影算子，除非 $A$ 是方阵，否则不等于 $I$。）两种方法得到的三角因子只差各行的符号：

```r
A <- matrix(c(10, 1,  1,
               1, 20, 2,
               1, 2, 30), ncol = 3)
qr.R(qr(A))
chol(t(A) %*% A)
```

```text
> qr.R(qr(A))
         [,1]       [,2]      [,3]
[1,] -10.0995  -3.168472 -4.158620
[2,]   0.0000 -19.873620 -4.419101
[3,]   0.0000   0.000000 29.464851
> chol(t(A) %*% A)
        [,1]      [,2]      [,3]
[1,] 10.0995  3.168472  4.158620
[2,]  0.0000 19.873620  4.419101
[3,]  0.0000  0.000000 29.464851
```

用 QR 求解。 若 $A=QR$，则 $A\boldsymbol{x}=\boldsymbol{b}$ 化为 $QR\boldsymbol{x}=\boldsymbol{b}$，即 $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$。方法是：(1) 计算 QR 分解 $A=QR$；(2) 计算 $\boldsymbol{y}=Q^{\mathsf T}\boldsymbol{b}$；(3) 解三角方程组 $R\boldsymbol{x}=\boldsymbol{y}$。`lm` 正是这样做的：`lm` 拟合结果的分量 `effects` 就是向量 $Q^{\mathsf T}\boldsymbol{y}$，分量 `qr` 存放分解本身。

对 $m\ge n$ 且满秩的最小二乘问题 $\min_{\boldsymbol{x}}\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2$，把完全分解的 $Q$ 写成 $Q=\bigl[\tilde Q\ \big|\ \tilde Q_\perp\bigr]$，$\tilde Q\in\mathbb{R}^{m\times n}$，$\tilde Q_\perp\in\mathbb{R}^{m\times(m-n)}$，则 $Q^{\mathsf T}A=\begin{bmatrix}\hat R\\O\end{bmatrix}$。由酉不变性，

$$
\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2=\|Q^{\mathsf T}(A\boldsymbol{x}-\boldsymbol{b})\|_2^2=\left\|\begin{bmatrix}\hat R\boldsymbol{x}-\tilde Q^{\mathsf T}\boldsymbol{b}\\-\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\end{bmatrix}\right\|_2^2=\|\hat R\boldsymbol{x}-\tilde Q^{\mathsf T}\boldsymbol{b}\|_2^2+\|\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\|_2^2 .
$$
解 $\hat R\boldsymbol{x}=\tilde Q^{\mathsf T}\boldsymbol{b}$，即 $\boldsymbol{x}=\hat R^{-1}\tilde Q^{\mathsf T}\boldsymbol{b}$，就达到最小值，残差范数为 $\|\tilde Q_\perp^{\mathsf T}\boldsymbol{b}\|_2$。求解只需约化分解；完全分解多出的列只用于给出残差。

相对于正规方程的优势。 若用消元法解正规方程 $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$，矩阵是 $B=A^{\mathsf T}A$，$\kappa(B)=\kappa(A)^2$（2-范数下的**条件数**，见 [3.5.1](/3.5.1)）。用 QR 时解的是 $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$，由于 $\kappa(Q)=1$，有 $\kappa(R)=\kappa(QR)=\kappa(A)$。

**例 3.2.1** 对很小的 $\delta$，考虑

$$
A=\begin{bmatrix}1&1\\\delta&0\\0&\delta\end{bmatrix},\qquad B=A^{\mathsf T}A=\begin{bmatrix}1+\delta^2&1\\1&1+\delta^2\end{bmatrix}.
$$
$B$ 的特征值为 $2+\delta^2$ 和 $\delta^2$，故 $\kappa(B)=\frac{2+\delta^2}{\delta^2}\approx\frac2{\delta^2}$，而 $\kappa(R)=\kappa(A)=\sqrt{\frac{2+\delta^2}{\delta^2}}\approx\frac{\sqrt2}{\delta}$。当 $\delta=10^{-5}$ 时，$1+\delta^2$ 相对于 $\delta^2$ 已丢失一半有效数字，$\kappa(B)\approx2\times10^{10}$：

```r
d <- 1e-2
A <- matrix(c(1, d, 0, 1, 0, d), ncol = 2)
kappa(A, exact = TRUE)               # 141.4249
kappa(t(A) %*% A, exact = TRUE)      # 20001
kappa(A, exact = TRUE)^2             # 20001
d <- 1e-5
A <- matrix(c(1, d, 0, 1, 0, d), ncol = 2)
kappa(A)                             # 141422.4 (an estimate)
kappa(t(A) %*% A)                    # 19999989553
```

计算 QR 分解主要有三种方法：Gram–Schmidt 正交化、Householder 三角化和 Givens 旋转。

### 3.2.4. Gram–Schmidt 正交化

**算法 3.2.1（经典 Gram–Schmidt 正交化）** 对 $j=1,\dots,n$：令 $\boldsymbol{v}_j=\boldsymbol{a}_j$；对 $i=1,\dots,j-1$，令 $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$，$\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$；然后令 $r_{jj}=\|\boldsymbol{v}_j\|_2$，$\boldsymbol{q}_j=\boldsymbol{v}_j/r_{jj}$。

在精确算术下它给出 $\hat Q$ 和 $\hat R$；在浮点算术下，得到的向量可能远非正交。

**例 3.2.2** 对

$$
\boldsymbol{a}_1=(1,\varepsilon,0,0)^{\mathsf T},\quad \boldsymbol{a}_2=(1,0,\varepsilon,0)^{\mathsf T},\quad \boldsymbol{a}_3=(1,0,0,\varepsilon)^{\mathsf T}
$$
作正交化，其中 $\varepsilon$ 小到 $1+\varepsilon^2$ 舍入为 $1$（例如双精度下 $\varepsilon=10^{-10}$）。经典 Gram–Schmidt 给出：$r_{11}=\sqrt{1+\varepsilon^2}\approx1$，$\boldsymbol{q}_1=(1,\varepsilon,0,0)^{\mathsf T}$；$r_{12}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_2=1$，$\boldsymbol{v}_2=\boldsymbol{a}_2-\boldsymbol{q}_1=(0,-\varepsilon,\varepsilon,0)^{\mathsf T}$，$r_{22}=\sqrt2\varepsilon$，$\boldsymbol{q}_2=(0,-1,1,0)^{\mathsf T}/\sqrt2$；$r_{13}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3=1$，$r_{23}=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}_3=0$，$\boldsymbol{v}_3=(0,-\varepsilon,0,\varepsilon)^{\mathsf T}$，$r_{33}=\sqrt2\varepsilon$，以及

$$
\boldsymbol{q}_3=(0,-1,0,1)^{\mathsf T}/\sqrt2 .
$$
这里 $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_2=-\varepsilon/\sqrt2\approx0$，但 $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_3=1/2$：正交性完全丧失。

补救办法来自正交投影算子的观点。Gram–Schmidt 计算 $\boldsymbol{q}_j=P_j\boldsymbol{a}_j/\|P_j\boldsymbol{a}_j\|$，其中 $P_1=I$，$j\ge2$ 时

$$
P_j\boldsymbol{v}=\boldsymbol{v}-(\boldsymbol{q}_1^{\mathsf H}\boldsymbol{v})\boldsymbol{q}_1-\cdots-(\boldsymbol{q}_{j-1}^{\mathsf H}\boldsymbol{v})\boldsymbol{q}_{j-1}=\Bigl(I-\sum_{i=1}^{j-1}\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H}\Bigr)\boldsymbol{v}.
$$
由于各 $\boldsymbol{q}_i$ 标准正交，$P_j=I-\sum_{i<j}\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H}=\prod_{i<j}(I-\boldsymbol{q}_i\boldsymbol{q}_i^{\mathsf H})=P_{\perp\boldsymbol{q}_{j-1}}\cdots P_{\perp\boldsymbol{q}_2}P_{\perp\boldsymbol{q}_1}$：一次秩为 $m-j+1$ 的投影等于 $j-1$ 次秩为 $m-1$ 的投影的复合。经典 Gram–Schmidt 采用左边的形式，所有系数都从原始列 $\boldsymbol{a}_j$ 算出；修正版本采用右边的形式，每次只沿一个方向投影当前已部分正交化的向量。

**算法 3.2.2（修正 Gram–Schmidt 正交化）** 对 $i=1,\dots,n$，令 $\boldsymbol{v}_i=\boldsymbol{a}_i$。对 $i=1,\dots,n$：令 $r_{ii}=\|\boldsymbol{v}_i\|_2$，$\boldsymbol{q}_i=\boldsymbol{v}_i/r_{ii}$；对 $j=i+1,\dots,n$，令 $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$，$\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$。

与算法 3.2.1 唯一的区别是用 $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$（MGS）代替 $r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{a}_j$（CGS）；两者在精确算术下等价，但修正 Gram–Schmidt 对舍入误差的敏感程度低得多。在例 3.2.2 中它算得 $r_{13}=\boldsymbol{q}_1^{\mathsf T}\boldsymbol{v}_3=1$，$\boldsymbol{v}_3=(0,-\varepsilon,0,\varepsilon)^{\mathsf T}$，然后 $r_{23}=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=\varepsilon/\sqrt2$，$\boldsymbol{v}_3\leftarrow(0,-\varepsilon/2,-\varepsilon/2,\varepsilon)^{\mathsf T}$，$r_{33}=\sqrt6\varepsilon/2$，以及

$$
\boldsymbol{q}_3=(0,-1,-1,2)^{\mathsf T}/\sqrt6,\qquad \boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_3=0 .
$$

原因何在？在 MGS 中，$\boldsymbol{v}_3^{(1)}=\boldsymbol{a}_3-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_1$，$\boldsymbol{v}_3=\boldsymbol{v}_3^{(1)}-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)})\boldsymbol{q}_2$，所以无论 $\boldsymbol{v}_3^{(1)}$ 含有什么误差，都有 $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)}-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3^{(1)})\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_2=0$。在 CGS 中，$\boldsymbol{v}_3=\boldsymbol{a}_3-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_1-(\boldsymbol{q}_2^{\mathsf T}\boldsymbol{a}_3)\boldsymbol{q}_2$ 给出 $\boldsymbol{q}_2^{\mathsf T}\boldsymbol{v}_3=-(\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3)\,\boldsymbol{q}_2^{\mathsf T}\boldsymbol{q}_1$：若计算 $\boldsymbol{q}_2$ 时出现误差，使 $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{q}_2=\delta$ 很小但不为零，这一误差在之后的计算中都得不到纠正，还会被可能很大的系数 $\boldsymbol{q}_1^{\mathsf T}\boldsymbol{a}_3$ 放大。

```r
CGS <- function(A) {
  m <- nrow(A); n <- ncol(A)
  Q <- matrix(0, m, n); R <- matrix(0, n, n)
  for (j in 1:n) {
    v <- A[, j]
    if (j > 1) for (i in 1:(j - 1)) {
      R[i, j] <- sum(Q[, i] * A[, j])      # coefficient from the original column
      v <- v - R[i, j] * Q[, i]
    }
    R[j, j] <- sqrt(sum(v^2))
    Q[, j] <- v / R[j, j]
  }
  list(Q, R)
}

MGS <- function(A) {
  m <- nrow(A); n <- ncol(A)
  V <- A; Q <- matrix(0, m, n); R <- matrix(0, n, n)
  for (i in 1:n) {
    R[i, i] <- sqrt(sum(V[, i]^2))
    Q[, i] <- V[, i] / R[i, i]
    if (i < n) for (j in (i + 1):n) {
      R[i, j] <- sum(Q[, i] * V[, j])      # coefficient from the updated column
      V[, j] <- V[, j] - R[i, j] * Q[, i]
    }
  }
  list(Q, R)
}
```

**例 3.2.3** 以 $(1,2,3)^{\mathsf T},(4,5,6)^{\mathsf T},(7,8,9)^{\mathsf T}$ 为列的奇异矩阵秩为 $2$。用 `MGS` 计算时，第三列 $\boldsymbol{v}_3$ 恰好变为 $\boldsymbol{0}$，于是 $r_{33}=0$，$\boldsymbol{q}_3$ 为 `NaN`：方法暴露出了秩亏损。`CGS` 则返回 $r_{33}=5.6\times10^{-15}$，第三列与 $\boldsymbol{q}_2$ 约有 $15$ 位相同，$\tilde Q^{\mathsf T}\tilde Q$ 的非对角元为 $1$，问题未被察觉。

运算量。 算法 3.2.2 的主要工作在内层循环：$r_{ij}=\boldsymbol{q}_i^{\mathsf T}\boldsymbol{v}_j$（$m$ 次乘法、$m-1$ 次加法）和 $\boldsymbol{v}_j=\boldsymbol{v}_j-r_{ij}\boldsymbol{q}_i$（$m$ 次乘法、$m$ 次减法），每次迭代约 $4m$ flops：

$$
\sum_{i=1}^n\sum_{j=i+1}^n4m=4m\sum_{i=1}^n(n-i)\sim2mn^2\ \text{flops}.
$$
精确计数时，算上 $m$ 次除法和每个范数的 $2m-1$ 次运算，加法共 $\frac12n(n+1)(m-1)$ 次，减法 $\frac12mn(n-1)$ 次，乘法 $mn^2$ 次，除法 $mn$ 次，总计 $2mn^2+mn-\frac12n^2-\frac12n\sim2mn^2$ flops（开方另有 $n$ 次）。经典 Gram–Schmidt 的运算量相同。

### 3.2.5. Householder 三角化

Gram–Schmidt 是在 $A$ 的右边乘三角矩阵，使其列标准正交。第 1 步为

$$
\begin{bmatrix}\boldsymbol{a}_1&\boldsymbol{a}_2&\cdots&\boldsymbol{a}_n\end{bmatrix}\begin{bmatrix}\frac1{r_{11}}&\frac{-r_{12}}{r_{11}}&\cdots&\frac{-r_{1n}}{r_{11}}\\&1&&\\&&\ddots&\\&&&1\end{bmatrix}=\begin{bmatrix}\boldsymbol{q}_1&\boldsymbol{a}_2^{(2)}&\cdots&\boldsymbol{a}_n^{(2)}\end{bmatrix},
$$
全部完成后 $AR_1R_2\cdots R_n=\hat Q$，$R_1R_2\cdots R_n=\hat R^{-1}$：Gram–Schmidt 是三角正交化。Householder 方法则是正交三角化：在 $A$ 的左边乘酉矩阵 $Q_k$，使之成为三角形，

$$
Q_n\cdots Q_2Q_1A=R,\qquad Q_n\cdots Q_2Q_1=Q^{-1}.
$$
（用这套说法，Gauss 消元 $L_{m-1}\cdots L_1A=U$ 是三角三角化。）第 $k$ 步在第 $k$ 列对角线以下引入零，并保持之前引入的零：

$$
\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\end{bmatrix}\xrightarrow{Q_1}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{Q_2}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&0&\times\\0&0&\times\\0&0&\times\end{bmatrix}\xrightarrow{Q_3}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&0&\times\\0&0&0\\0&0&0\end{bmatrix}.
$$
为了不动前 $k-1$ 行和前 $k-1$ 列，$Q_k$ 必须形如

$$
Q_k=\begin{bmatrix}I_{k-1}&O\\O&F\end{bmatrix},
$$
其中 $F$ 把第 $k$ 列第 $k,\dots,m$ 个元素组成的向量 $\boldsymbol{x}\in\mathbb{R}^{m-k+1}$ 映为 $\boldsymbol{e}_1$ 的倍数。由于 $Q_kQ_k^{\mathsf T}=\begin{bmatrix}I&O\\O&FF^{\mathsf T}\end{bmatrix}=I$，$F$ 必须正交，故 $\|F\boldsymbol{x}\|=\|\boldsymbol{x}\|$，目标是 $F\boldsymbol{x}=\pm\|\boldsymbol{x}\|\boldsymbol{e}_1$。

**定义 3.2.3（Householder 反射）** 对非零 $\boldsymbol{v}\in\mathbb{R}^p$，矩阵

$$
F=I-2\frac{\boldsymbol{v}\boldsymbol{v}^{\mathsf T}}{\boldsymbol{v}^{\mathsf T}\boldsymbol{v}}
$$
是关于超平面 $\operatorname{span}(\boldsymbol{v})^\perp$ 的 **Householder 变换**（Householder 反射）。取 $\boldsymbol{v}=\|\boldsymbol{x}\|\boldsymbol{e}_1-\boldsymbol{x}$，它把 $\boldsymbol{x}$ 映为 $\|\boldsymbol{x}\|\boldsymbol{e}_1$。

与秩为 $p-1$ 的投影算子 $P_{\perp\boldsymbol{v}}=I-\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$ 比较：投影走到超平面为止，反射则走两倍远，到达镜像。$F$ 对称且正交，$F=F^{\mathsf T}=F^{-1}$，满秩，$Q_k$ 也是如此。（既对称又正交的矩阵并不限于元素为 $0,\pm1$ 的矩阵：$\boldsymbol{v}=(1,2)^{\mathsf T}$ 给出 $F=\frac15\begin{bmatrix}3&-4\\-4&-3\end{bmatrix}$。）

反射并不唯一：$\boldsymbol{x}$ 可以反射到 $+\|\boldsymbol{x}\|\boldsymbol{e}_1$，也可以反射到 $-\|\boldsymbol{x}\|\boldsymbol{e}_1$，从计算的角度看，选择很重要。若 $\boldsymbol{x}$ 接近 $+\|\boldsymbol{x}\|\boldsymbol{e}_1$，计算 $\boldsymbol{v}=\|\boldsymbol{x}\|\boldsymbol{e}_1-\boldsymbol{x}$ 会发生灾难性抵消，$\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$ 也就不准确。稳定的选择是把 $\boldsymbol{x}$ 反射到较远的点 $-\operatorname{sgn}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1$，即 $\boldsymbol{v}=\operatorname{sgn}(x_1)\|\boldsymbol{x}\|\boldsymbol{e}_1+\boldsymbol{x}$，使第一个分量是两个同号数之和（约定 $\operatorname{sgn}(0)=1$）。

**算法 3.2.3（Householder QR 分解）** 对 $k=1,\dots,n$：令 $\boldsymbol{x}=A_{k:m,k}$，$\boldsymbol{v}_k=\operatorname{sgn}(x_1)\|\boldsymbol{x}\|_2\boldsymbol{e}_1+\boldsymbol{x}$，$\boldsymbol{v}_k=\boldsymbol{v}_k/\|\boldsymbol{v}_k\|_2$，$A_{k:m,k:n}=A_{k:m,k:n}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}A_{k:m,k:n})$。

结果 $R$ 留在 $A$ 的位置上，反射向量 $\boldsymbol{v}_k$ 保存起来以备后用；$Q$ 从不显式形成。要解 $A\boldsymbol{x}=\boldsymbol{b}$（或最小二乘问题），隐式地计算 $Q^{-1}\boldsymbol{b}=Q^{\mathsf T}\boldsymbol{b}=Q_n\cdots Q_1\boldsymbol{b}$：对 $k=1,\dots,n$，令 $\boldsymbol{b}_{k:m}=\boldsymbol{b}_{k:m}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}\boldsymbol{b}_{k:m})$，再用回代法解上三角方程组 $R\boldsymbol{x}=Q^{\mathsf T}\boldsymbol{b}$。由于每个 $Q_k$ 对称，$Q=Q_1^{\mathsf T}\cdots Q_n^{\mathsf T}=Q_1Q_2\cdots Q_n$，所以 $Q\boldsymbol{x}$ 可以对 $k=n$ 到 $1$ 依次令 $\boldsymbol{x}_{k:m}=\boldsymbol{x}_{k:m}-2\boldsymbol{v}_k(\boldsymbol{v}_k^{\mathsf T}\boldsymbol{x}_{k:m})$ 求得。若需要显式的 $Q$，把这一过程作用于 $\boldsymbol{x}=\boldsymbol{e}_1,\dots,\boldsymbol{e}_m$ 即可（求 $\hat Q$ 只需 $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$）。

运算量。 第 $k$ 次迭代中，内积 $\boldsymbol{v}_k^{\mathsf T}A_{k:m,k:n}$ 约需 $2(m-k)(n-k)$ flops，外积 $2\boldsymbol{v}_k(\cdots)$ 约需 $(m-k)(n-k)$，减法再需 $(m-k)(n-k)$。连同外层循环，总量为

$$
\sum_{k=1}^n4(m-k)(n-k)=4\sum_{k=1}^n\bigl(mn-k(m+n)+k^2\bigr)\sim4mn^2-4(m+n)\frac{n^2}2+\frac43n^3=2mn^2-\frac23n^3\ \text{flops},
$$
略少于 Gram–Schmidt 的 $2mn^2$。对可逆方阵（$m=n$），它是 $\frac43m^3$，为 Gauss 消元 $\frac23m^3$ 的两倍：若以最少运算量为目标，方阵方程组应当用 Gauss 消元法求解。

稳定性。 由于舍入误差，计算所得的因子满足 $A=\tilde Q\tilde R+E$。残差 $E$ 通常不是问题：对 Householder 和 Gram–Schmidt 都有 $\|E\|\le c\,\varepsilon_{\mathrm{mach}}\|A\|$，$c$ 只依赖于维数，两者算出的 $\tilde R$ 在逐列的意义下都是准确的。主要差别在于正交因子的正交性：

$$
\text{Householder：}\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}},\qquad \text{MGS：}\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}}\kappa(A),\qquad \text{CGS：}\|I-\tilde Q^{\mathsf T}\tilde Q\|\le c\,\varepsilon_{\mathrm{mach}}\kappa(A)^2,
$$
最后一个界在 $\varepsilon_{\mathrm{mach}}\kappa(A)^2$ 远小于 $1$ 时成立。Householder 把 $\tilde Q$ 算成精确反射（在舍入意义下正交）的乘积，而 Gram–Schmidt 中没有任何机制能在舍入误差面前迫使 $\tilde Q$ 保持标准正交。因此 Householder 三角化是计算 QR 分解的主要方法。

![对条件数给定的 50 x 12 测试矩阵，所得 Q 的正交性损失。Householder QR 始终保持在机器精度的量级；修正 Gram–Schmidt 的正交性损失与 kappa(A) 成正比，经典 Gram–Schmidt 则与 kappa(A)^2 成正比，直到各列完全失去线性无关性。](./plots/qr-orthogonality-loss.py)

**注 3.2.1（用 MGS 解最小二乘）** MGS 的弱点在于 $\tilde Q$，而不在于最小二乘解，只要用法正确。解 $\min\|A\boldsymbol{x}-\boldsymbol{b}\|_2$ 时，不能用算出的 $Q$ 计算 $\boldsymbol{x}=R^{-1}(Q^{\mathsf T}\boldsymbol{b})$，而应对增广矩阵作 MGS：

$$
\begin{bmatrix}A&\boldsymbol{b}\end{bmatrix}=\begin{bmatrix}Q&\boldsymbol{q}_{n+1}\end{bmatrix}\begin{bmatrix}R&\boldsymbol{z}\\\boldsymbol{0}^{\mathsf T}&\rho\end{bmatrix}.
$$
于是 $A\boldsymbol{x}-\boldsymbol{b}=\begin{bmatrix}A&\boldsymbol{b}\end{bmatrix}\begin{bmatrix}\boldsymbol{x}\\-1\end{bmatrix}=Q(R\boldsymbol{x}-\boldsymbol{z})-\rho\boldsymbol{q}_{n+1}$，又因 $\boldsymbol{q}_{n+1}$ 与 $Q$ 的各列正交，$\|A\boldsymbol{x}-\boldsymbol{b}\|_2^2=\|R\boldsymbol{x}-\boldsymbol{z}\|_2^2+\rho^2$。解为 $\boldsymbol{x}=R^{-1}\boldsymbol{z}$，其中 $\boldsymbol{z}$ 作为 MGS 过程的一部分算出，而不是作为乘积 $Q^{\mathsf T}\boldsymbol{b}$ 算出。这样使用时 MGS 解最小二乘问题是稳定的，尽管用它计算标准正交基可能结果很差：算法的稳定性取决于所解的问题。

**例 3.2.4** 对例 3.2.3 的奇异矩阵，Householder 实现给出的 $\tilde Q$ 满足 $\|\tilde Q^{\mathsf T}\tilde Q-I\|$ 为 $10^{-16}$ 量级，$\tilde R$ 最后一个对角元为 $-4.4\times10^{-16}$，清楚地显示出秩亏损；CGS 因子的 $\tilde Q^{\mathsf T}\tilde Q$ 则有等于 $1$ 的非对角元。

R 中的 QR。 函数 `qr` 计算 Householder QR 分解（由 LINPACK 子程序 `dqrdc2` 完成，`LAPACK = TRUE` 时改用 LAPACK），并以紧凑形式返回：

```r
A <- rbind(c(2, -2, 18), c(2, 1, 0), c(1, 2, 0))
A.qr <- qr(A)
A.qr.out <- list(Q = qr.Q(A.qr), R = qr.R(A.qr))
A.qr
```

```text
$qr
          [,1] [,2] [,3]
[1,] -3.0000000  0.0  -12
[2,]  0.6666667 -3.0   12
[3,]  0.3333333  0.8    6

$rank
[1] 3

$qraux
[1] 1.666667 1.600000 6.000000

$pivot
[1] 1 2 3
```

`$qr` 的上三角部分就是 $R$。Householder 向量存放在对角线以下和 `$qraux` 中：反射为 $H_i=I-\boldsymbol{v}_i\boldsymbol{v}_i^{\mathsf T}/p_i$，其中 $p_i$ 是 `$qraux` 的第 $i$ 个元素，$\boldsymbol{v}_i$ 的分量为 $\boldsymbol{v}_i[1{:}(i-1)]=0$，$\boldsymbol{v}_i[i]=p_i$（$=\boldsymbol{v}_i^{\mathsf T}\boldsymbol{v}_i/2$），$\boldsymbol{v}_i[(i+1){:}m]=$ `A.qr$qr[(i+1):m, i]`。这就是反射 $F=I-2\boldsymbol{v}\boldsymbol{v}^{\mathsf T}/(\boldsymbol{v}^{\mathsf T}\boldsymbol{v})$，只是 $\boldsymbol{v}$ 的标度不同。可以直接验证：

```r
p <- A.qr$qraux
v1 <- matrix(c(p[1], A.qr$qr[2:3, 1]))
p[1] == t(v1) %*% v1 / 2
v2 <- matrix(c(0, p[2], A.qr$qr[3, 2]))
I <- diag(3)
H1 <- I - v1 %*% t(v1) / p[1]
H2 <- I - v2 %*% t(v2) / p[2]
Q <- H1 %*% H2    # equals qr.Q(A.qr)

B <- cbind(c(2, -2, 18), c(2, -2, 18), c(2, 1, 0))
qr(B)$pivot       # 1 3 2: A P = Q R
```

默认的 `qr` 采用一种有限的列选主元：（在数值意义下）是前面各列线性组合的列被移到最后，于是分解为 $AP=QR$，`$rank` 报告数值秩。`B` 的第二列重复第一列，置换向量为 $(1,3,2)$。

### 3.2.6. Givens 旋转

**Givens 变换**

$$
G=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}
$$
把 $\boldsymbol{x}\in\mathbb{R}^2$ 逆时针旋转 $\theta$（它的两列是 $\boldsymbol{e}_1$ 和 $\boldsymbol{e}_2$ 的像）。把它作用于矩阵的第 $i,j$ 两行（其余部分为单位阵），可以把一个元素置零：取

$$
\cos\theta=\frac{x_i}{\sqrt{x_i^2+x_j^2}},\qquad \sin\theta=\frac{-x_j}{\sqrt{x_i^2+x_j^2}},
$$
得 $G\begin{bmatrix}x_i\\x_j\end{bmatrix}=\begin{bmatrix}\sqrt{x_i^2+x_j^2}\\0\end{bmatrix}$（符号取反时为 $-\sqrt{x_i^2+x_j^2}$）。Givens QR 自下而上地在每一列引入零，每个零用一次旋转：

$$
\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\\times&\times&\times\end{bmatrix}\xrightarrow{(3,4)}\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\\times&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{(2,3)}\begin{bmatrix}\times&\times&\times\\\times&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\xrightarrow{(1,2)}\begin{bmatrix}\times&\times&\times\\0&\times&\times\\0&\times&\times\\0&\times&\times\end{bmatrix}\to\cdots\to R .
$$
运算量为 $3mn^2-n^3$，比 Householder QR 多 50%。因此 Givens 旋转主要用于结构化矩阵，那里只需把少数元素置零（三对角或上 Hessenberg 矩阵每列只需一次旋转），以及在增删一行后更新或"降级"分解时所需的精细置零。

QR 分解是解线性方程组、最小二乘问题和特征值问题（3.3 节）的多用途计算工具。三种方法中：Gram–Schmidt 依次正交化 $A$ 的各列，是最古老的方法，也是大多数线性代数教材所讲的方法；它的优点是可以中途停止，得到前若干列的约化 QR。Householder 变换是计算 QR 分解最通用的方法。当 $A$ 有特殊的稀疏结构（如带状或 Hessenberg 结构）时，首选 Givens 变换。Gram–Schmidt 显式地给出 $Q$，而 Householder 和 Givens 以因子乘积的形式保存 $Q$。

### 3.2.7. 奇异值分解

我们希望在 $\mathbb{C}^n$ 的标准正交基 $\{\boldsymbol{v}_i\}$ 与 $\mathbb{C}^m$ 的标准正交基 $\{\boldsymbol{u}_i\}$ 之间变换，使 $A\boldsymbol{v}_i=\sigma_i\boldsymbol{u}_i$：

$$
AV=A\begin{bmatrix}\boldsymbol{v}_1&\cdots&\boldsymbol{v}_n\end{bmatrix}=\begin{bmatrix}\boldsymbol{u}_1&\cdots&\boldsymbol{u}_m\end{bmatrix}\begin{bmatrix}\sigma_1&&\\&\ddots&\\&&\sigma_r\\&&&\end{bmatrix}=U\Sigma\ \Longrightarrow\ A=U\Sigma V^{\mathsf H}.
$$

**定义 3.2.4** $A\in\mathbb{C}^{m\times n}$ 的奇异值分解（SVD）是分解 $A=U\Sigma V^{\mathsf H}$，其中 $U\in\mathbb{C}^{m\times m}$、$V\in\mathbb{C}^{n\times n}$ 为酉矩阵，$\Sigma\in\mathbb{R}^{m\times n}$ 为对角矩阵，对角元 $\sigma_1\ge\sigma_2\ge\cdots\ge\sigma_{\min(m,n)}\ge0$。$\sigma_j$ 称为 $A$ 的**奇异值**，$U$ 的列 $\boldsymbol{u}_j$ 称为 $A$ 的**左奇异向量**，$V$ 的列 $\boldsymbol{v}_j$ 称为**右奇异向量**，编号使 $A\boldsymbol{v}_j=\sigma_j\boldsymbol{u}_j$。当 $m\ge n$ 时，**约化 SVD** $A=\hat U\hat\Sigma V^{\mathsf H}$ 只保留 $U$ 的前 $n$ 列（$\hat U\in\mathbb{C}^{m\times n}$ 列标准正交，$\hat\Sigma\in\mathbb{R}^{n\times n}$）；完全 SVD 用 $m-n$ 个"沉默"列把 $\hat U$ 扩充为酉矩阵 $U$，并给 $\Sigma$ 添上零行。

$\boldsymbol{v}_i$ 是 $A^{\mathsf H}A$ 的特征向量，$\boldsymbol{u}_i$ 是 $AA^{\mathsf H}$ 的特征向量，非零奇异值是它们非零特征值的平方根。几何上，$A$ 把 $\mathbb{R}^n$ 的单位球映为 $\mathbb{R}^m$ 中的超椭球：沿正交方向 $\boldsymbol{u}_1,\dots,\boldsymbol{u}_m$ 分别伸缩 $\sigma_1,\dots,\sigma_m$ 倍（可能为零）；向量 $\sigma_j\boldsymbol{u}_j$ 是超椭球的主半轴，长度为 $\sigma_j$。分解 $A=U\Sigma V^{\mathsf H}$ 把这一变换拆成一次旋转（或反射）$V^{\mathsf H}$、一次沿坐标轴的伸缩 $\Sigma$ 和又一次旋转 $U$。若 $\operatorname{rank}(A)=r<n$，约化 SVD 还可以进一步缩为 $A=\hat U_{m\times r}\hat\Sigma_{r\times r}\hat V_{n\times r}^{\mathsf H}$，完全 SVD 则把 $U$ 和 $V$ 都扩充为酉矩阵；$i>r$ 时沉默列满足 $\boldsymbol{v}_i\in\mathcal{N}(A)=\mathcal{N}(A^{\mathsf H}A)$，$\boldsymbol{u}_i\in\mathcal{N}(A^{\mathsf H})=\mathcal{N}(AA^{\mathsf H})$。

**定理 3.2.4（SVD 的存在性与唯一性）** 每个矩阵 $A\in\mathbb{C}^{m\times n}$ 都有奇异值分解。奇异值是唯一确定的；若 $A$ 是方阵且各 $\sigma_j$ 互不相同，则左、右奇异向量在相差一个复符号（模为 1 的因子）的意义下唯一确定。奇异值都是实数；若 $A$ 是实矩阵，$U$ 和 $V$ 可取为实矩阵。

由于 $A^{\mathsf H}A=V\Sigma^{\mathsf H}U^{\mathsf H}U\Sigma V^{\mathsf H}=V\Sigma^{\mathsf H}\Sigma V^{\mathsf H}$，$AA^{\mathsf H}=U\Sigma\Sigma^{\mathsf H}U^{\mathsf H}$，原则上可以分两步得到 SVD：(1) 由 $A^{\mathsf H}A$ 的特征分解得到 $\{\boldsymbol{v}_j,\sigma_j\}$；(2) 对 $j\le r$ 令 $\boldsymbol{u}_j=A\boldsymbol{v}_j/\sigma_j$，再用 $\mathcal{N}(A^{\mathsf H})$ 的标准正交基补全。由此可见 $\kappa(A^{\mathsf T}A)=\sigma_1^2/\sigma_n^2=\kappa(A)^2$。数值计算中并不走这条路，正是因为形成 $A^{\mathsf H}A$ 会使条件数平方并毁掉小奇异值；库程序（`svd` 调用的 LAPACK）先用 Householder 反射把 $A$ 化为双对角形，再对双对角矩阵迭代。

**命题 3.2.2（由 SVD 得到的矩阵性质）** 设 $A=U\Sigma V^{\mathsf H}$ 有 $r$ 个非零奇异值。

1. $\operatorname{rank}(A)=r$。
2. $\mathcal{R}(A)=\langle\boldsymbol{u}_1,\dots,\boldsymbol{u}_r\rangle$，$\mathcal{N}(A)=\langle\boldsymbol{v}_{r+1},\dots,\boldsymbol{v}_n\rangle$。
3. $\|A\|_2=\sigma_1$，$\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{\mathsf H}A)}=\sqrt{\sigma_1^2+\cdots+\sigma_r^2}$（两种范数都是酉不变的，所以等于 $\Sigma$ 的范数）。
4. 非零奇异值 $\sigma_j=\sqrt{\lambda_j(A^{\mathsf H}A)}=\sqrt{\lambda_j(AA^{\mathsf H})}$。
5. 若 $A=A^{\mathsf H}$，则 $\sigma_j=\lvert\lambda_j(A)\rvert$。
6. 对方阵 $A$，$\lvert\det A\rvert=\prod_j\sigma_j$（而 $\det A=\prod_j\lambda_j$，$\operatorname{tr}(A)=\sum_j\lambda_j$）。

和式 $\|A\|_*=\sum_i\sigma_i$ 是核范数。这些性质也是最好的计算工具：确定矩阵的秩最好的方法是数出大于某个审慎选取的容差的奇异值个数（性质 1）；求值域或零空间的标准正交基最精确的方法是性质 2（QR 分解提供更快但不总是同样精确的替代方案）；性质 3 是计算 $\|A\|_2$ 的标准方法。此外，SVD 还是最小二乘拟合、子空间求交、正则化等众多问题的稳健算法的组成部分。

解 $A\boldsymbol{x}=\boldsymbol{b}$：一次基变换。 记 $\tilde{\boldsymbol{b}}=U^{\mathsf H}\boldsymbol{b}$，$\tilde{\boldsymbol{x}}=V^{\mathsf H}\boldsymbol{x}$，则

$$
\boldsymbol{b}=A\boldsymbol{x}\iff U^{\mathsf H}\boldsymbol{b}=\Sigma V^{\mathsf H}\boldsymbol{x}\iff\tilde{\boldsymbol{b}}=\Sigma\tilde{\boldsymbol{x}} .
$$
当值域用 $U$ 的列作基、定义域用 $V$ 的列作基表示时，$A$ 就化为对角矩阵 $\Sigma$：只要为定义域和值域选择合适的基，每个矩阵都是对角的。特别地，对可逆的 $A$，$A^{-1}=V\Sigma^{-1}U^{\mathsf H}$。

再看条件数。 对奇异值为 $\sigma_1\ge\cdots\ge\sigma_m>0$ 的可逆矩阵 $A\in\mathbb{R}^{m\times m}$，映射 $\boldsymbol{x}\mapsto A\boldsymbol{x}$ 和 $\boldsymbol{b}\mapsto A^{-1}\boldsymbol{b}$ 的条件数（[3.5.1](/3.5.1)）满足

$$
\kappa(\boldsymbol{x})=\|A\|\frac{\|\boldsymbol{x}\|}{\|A\boldsymbol{x}\|}\le\|A\|\,\|A^{-1}\|,\qquad \kappa(\boldsymbol{b})=\|A^{-1}\|\frac{\|\boldsymbol{b}\|}{\|\boldsymbol{x}\|}\le\|A^{-1}\|\,\|A\|,
$$
且 $\kappa(A)=\|A\|_2\|A^{-1}\|_2=\sigma_1/\sigma_m$。把 $A$ 写成 $m$ 个秩 1 矩阵之和 $A=\sum_{i=1}^m\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}$：若 $\boldsymbol{x}=k\boldsymbol{v}_m$ 是对应 $\sigma_m$ 的右奇异向量的倍数，第一个界取等号，因为此时 $\|\boldsymbol{x}\|/\|A\boldsymbol{x}\|=\|k\boldsymbol{v}_m\|/\|k\sigma_m\boldsymbol{u}_m\|=1/\sigma_m=\|A^{-1}\|$；若 $\boldsymbol{b}=k\boldsymbol{u}_1$，第二个界取等号，因为由 $A^{-1}=\sum_i\boldsymbol{v}_i\boldsymbol{u}_i^{\mathsf T}/\sigma_i$ 得 $\|\boldsymbol{b}\|/\|\boldsymbol{x}\|=\|k\boldsymbol{u}_1\|/\|k\boldsymbol{v}_1/\sigma_1\|=\sigma_1=\|A\|$。奇异值本身是完全良态的：若 $\tilde\sigma_i$ 是 $A+E$ 的奇异值，则对每个 $i$ 有 $\lvert\tilde\sigma_i-\sigma_i\rvert\le\|E\|_2$（Weyl），且 $\sqrt{\sum_i(\tilde\sigma_i-\sigma_i)^2}\le\|E\|_{\mathrm{F}}$（Mirsky）。

**定理 3.2.5（低秩近似）** 设 $A=U\Sigma V^{\mathsf T}\in\mathbb{R}^{m\times n}$，$r=\operatorname{rank}(A)$，对 $k<r$ 令

$$
A_k=\sum_{i=1}^k\sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}.
$$
则

$$
\min_{\operatorname{rank}(B)\le k}\|A-B\|_2=\|A-A_k\|_2=\sigma_{k+1},\qquad \min_{\operatorname{rank}(B)\le k}\|A-B\|_{\mathrm{F}}=\|A-A_k\|_{\mathrm{F}}=\sqrt{\sigma_{k+1}^2+\cdots+\sigma_r^2}.
$$

这就是 **Eckart–Young 定理**（同时涉及 2-范数和 Frobenius 范数时也称 Eckart–Young–Mirsky 定理，证明见 [2.1.7](/2.1.7)）。误差的值来自 $U^{\mathsf T}A_kV=\operatorname{diag}(\sigma_1,\dots,\sigma_k,0,\dots,0)$，从而 $U^{\mathsf T}(A-A_k)V=\operatorname{diag}(0,\dots,0,\sigma_{k+1},\dots,\sigma_r)$。例如，离 $\operatorname{diag}(4,2,1,3)$ 最近的秩 2 矩阵是 $\operatorname{diag}(4,0,0,3)$：保留的是两个最大的奇异值，不论它们在对角线上的位置。

**例 3.2.5（图像压缩）** 数字图像是像素矩阵；彩色图像是三个这样的矩阵，即红、绿、蓝三色的强度（取值 $0$ 到 $255$，在 R 中被缩放到 $[0,1]$）。图像压缩只保留每个矩阵的低秩近似，它保留了图像的主要信息。对一张 $400\times286$ 的照片（满秩 $286$），每个通道的秩 $20$ 近似已经清晰可辨，每个通道只需 $20(400+286+1)$ 个数，而不是 $400\times286$ 个；保留的奇异值越多，近似越精确。

```r
library(jpeg)
x <- readJPEG("photo.jpg")      # convert the image into an array
dim(x)                          # 400 286 3
# each matrix holds one color channel of the RGB scale
r <- x[, , 1]; r.svd <- svd(r)
g <- x[, , 2]; g.svd <- svd(g)
b <- x[, , 3]; b.svd <- svd(b)
# collect the results into a list used to reconstruct the image
rgb.svds <- list(r.svd, g.svd, b.svd)

for (j in c(3, 5, 10, 20, 30)) {
  a <- sapply(rgb.svds, function(i) {
    i$u[, 1:j] %*% diag(i$d[1:j]) %*% t(i$v[, 1:j])
  }, simplify = "array")
  writeJPEG(pmin(pmax(a, 0), 1), paste0("compressed_svd_rank_", j, ".jpg"))
}
```

主成分分析。 高维数据矩阵难以使用。样本量 $n$ 固定而变量数 $p$ 增大时，良好预测所需的样本数呈指数增长，算法容易过拟合，其表现随 $p$ 先升后降（Hughes 现象）。这是维数灾难的一部分：空间的体积增长得如此之快，以致现有数据变得稀疏，大部分数据集中在一层薄"壳"中，所有点彼此几乎等距，基于距离的方法表现很差，数据也无法再可视化。降低数据矩阵 $X_{n\times p}$ 的维数，是指在尽可能保留方差的前提下减少变量数 $p$。**主成分分析**（[3.4.5](/3.4.5)）借助 SVD 做到这一点。

把 $X$ 的行 $\boldsymbol{X}_{(i)}^{\mathsf T}$ 看作数据点，并设 $X$ 的各列已中心化（如有需要也已标准化）。数据点在单位向量 $\boldsymbol{v}_1$ 上的投影为 $\boldsymbol{v}_1\boldsymbol{v}_1^{\mathsf T}\boldsymbol{X}_{(i)}$，系数为 $\boldsymbol{v}_1^{\mathsf T}\boldsymbol{X}_{(i)}=\boldsymbol{X}_{(i)}^{\mathsf T}\boldsymbol{v}_1$；对所有点合写为 $\boldsymbol{Y}_1=X\boldsymbol{v}_1\in\mathbb{R}^n$。利用样本协方差矩阵 $\frac1{n-1}X^{\mathsf T}X$，

$$
\operatorname{Var}(\boldsymbol{Y}_1)=\frac1{n-1}\boldsymbol{Y}_1^{\mathsf T}\boldsymbol{Y}_1=\frac1{n-1}\boldsymbol{v}_1^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_1,\qquad \max_{\|\boldsymbol{v}_1\|_2=1}\boldsymbol{v}_1^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_1=\max_{\|\boldsymbol{v}_1\|_2=1}\|X\boldsymbol{v}_1\|_2^2=\|X\|_2^2 .
$$
因此，对 SVD $X=U\Sigma V^{\mathsf T}$，$\sigma_1\ge\cdots\ge\sigma_p$，方差最大的方向即第一主方向，就是第一右奇异向量 $\boldsymbol{v}_1$，等价地是 $X^{\mathsf T}X$ 最大特征值 $\lambda_1=\sigma_1^2$ 的特征向量；$\boldsymbol{Y}_1=X\boldsymbol{v}_1=\sigma_1\boldsymbol{u}_1$ 是第一主成分得分向量，方差为 $\sigma_1^2/(n-1)$。保留前 $k<p$ 个主成分，相当于用 $k$ 维椭球拟合数据，或把数据投影到 $k$ 维平面上，解释的方差比例为

$$
\frac{\sum_{i=1}^k\boldsymbol{v}_i^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_i}{\sum_{i=1}^p\boldsymbol{v}_i^{\mathsf T}X^{\mathsf T}X\boldsymbol{v}_i}=\frac{\sum_{i=1}^k\sigma_i^2}{\sum_{i=1}^p\sigma_i^2}=\frac{\sum_{i=1}^k\lambda_i}{\sum_{i=1}^p\lambda_i}.
$$
用这些比例画出的碎石图帮助选择 $k$，方法是寻找"拐点"。是否标准化会给出不同的结果：方差最大的变量主导第一主成分，所以当变量的单位不同或不可比时，通常先标准化；这等于赋予所有变量同等的重要性，而且对离群值敏感（可改用中位数和四分位距作稳健缩放）。但当所有变量以同一单位测量同一种量时，不应标准化：若同时记录许多神经元，它们活动水平的差异本身很重要，用一个几乎沉默的神经元的微小标准差去除它的活动，会把多半只是噪声的东西大大放大。

### 3.2.8. 最小二乘的三种算法

设 $A\in\mathbb{C}^{m\times n}$（$m\ge n$）满秩。有三种算法求解 $\min_{\boldsymbol{x}}\|A\boldsymbol{x}-\boldsymbol{b}\|_2$。

**算法 3.2.4（用正规方程解最小二乘）** (1) 形成矩阵 $A^{\mathsf H}A$ 和向量 $A^{\mathsf H}\boldsymbol{b}$。(2) 计算 Cholesky 分解 $A^{\mathsf H}A=R^{\mathsf H}R$。(3) 解下三角方程组 $R^{\mathsf H}\boldsymbol{w}=A^{\mathsf H}\boldsymbol{b}$ 得 $\boldsymbol{w}$。(4) 解上三角方程组 $R\boldsymbol{x}=\boldsymbol{w}$ 得 $\boldsymbol{x}$。

这是经典的做法：$A$ 满秩时，正规方程是 $n$ 维的 Hermite 正定方程组，解这类方程组的标准方法就是 Cholesky 分解。形成 $A^{\mathsf H}A$ 需 $\sim\sum_{i=1}^n\sum_{j=1}^i2m\sim mn^2$ flops（由对称性只需算一半），Cholesky 分解需 $\sim n^3/3$；总量为 $\sim mn^2+n^3/3$ flops。

**算法 3.2.5（用 QR 解最小二乘）** (1) 计算约化 QR 分解 $A=\hat Q\hat R$。(2) 计算向量 $\hat Q^{\mathsf H}\boldsymbol{b}$。(3) 解上三角方程组 $\hat R\boldsymbol{x}=\hat Q^{\mathsf H}\boldsymbol{b}$ 得 $\boldsymbol{x}$。

这一 1960 年代以来流行的"现代经典"方法使用 Gram–Schmidt 或（更常见的）Householder 三角化。其依据是：$P=\hat Q\hat Q^{\mathsf H}$ 是到 $\mathcal{R}(A)$ 上的正交投影算子，所以 $A\boldsymbol{x}=P\boldsymbol{b}$ 化为 $\hat Q\hat R\boldsymbol{x}=\hat Q\hat Q^{\mathsf H}\boldsymbol{b}$，即 $\hat R\boldsymbol{x}=\hat Q^{\mathsf H}\boldsymbol{b}$；等价地，正规方程 $\hat R^{\mathsf H}\hat Q^{\mathsf H}\hat Q\hat R\boldsymbol{x}=\hat R^{\mathsf H}\hat Q^{\mathsf H}\boldsymbol{b}$ 也化为它。工作量由 QR 分解主导，用 Householder 反射时为 $\sim2mn^2-\frac23n^3$ flops。

**算法 3.2.6（用 SVD 解最小二乘）** (1) 计算约化 SVD $A=\hat U\hat\Sigma V^{\mathsf H}$。(2) 计算向量 $\hat U^{\mathsf H}\boldsymbol{b}$。(3) 解对角方程组 $\hat\Sigma\boldsymbol{w}=\hat U^{\mathsf H}\boldsymbol{b}$ 得 $\boldsymbol{w}$。(4) 令 $\boldsymbol{x}=V\boldsymbol{w}$。

此时 $P=\hat U\hat U^{\mathsf H}$，$A^{\mathsf H}A\boldsymbol{x}=A^{\mathsf H}\boldsymbol{b}$ 化为 $V\hat\Sigma\hat U^{\mathsf H}\hat U\hat\Sigma V^{\mathsf H}\boldsymbol{x}=V\hat\Sigma\hat U^{\mathsf H}\boldsymbol{b}$，即 $\hat\Sigma V^{\mathsf H}\boldsymbol{x}=\hat U^{\mathsf H}\boldsymbol{b}$。工作量由 SVD 主导，为 $\sim2mn^2+11n^3$ flops。对秩亏损的 $A$，同样的步骤只用非零（或不可忽略的）奇异值，得到最小范数解 $\boldsymbol{x}=A^+\boldsymbol{b}$，其中 $A^+=V\Sigma^+U^{\mathsf H}$ 是 **Moore–Penrose 广义逆**；满秩时 $A^+=(A^{\mathsf H}A)^{-1}A^{\mathsf H}$。

| 算法 | 运算量 | 稳定性 | 适用场合 |
|---|---|---|---|
| 正规方程 + Cholesky | $\sim mn^2+n^3/3$ | 误差按 $\kappa(A)^2$ 增长 | 只考虑速度、$A$ 良态 |
| Householder QR | $\sim2mn^2-\frac23n^3$ | 后向稳定 | 标准选择（`lm`、`qr.solve`） |
| SVD | $\sim2mn^2+11n^3$ | 最稳健 | $A$ 接近秩亏损 |

每种方法都在某些情形下占优。只考虑速度时，算法 3.2.4 可能最好，$m\gg n$ 时它的代价约为其他两种的一半。但由于 $\kappa(A^{\mathsf T}A)=\kappa(A)^2$，在存在舍入误差时解正规方程并不总是稳定的，所以数值分析学家推荐改用算法 3.2.5。若 $A$ 接近秩亏损，算法 3.2.5 本身的稳定性也不够理想，这时首选算法 3.2.6。下图在条件数给定的相容方程组（$\boldsymbol{b}=A\boldsymbol{x}$）上比较三者。

![条件数给定的 100 x 10 矩阵、b = A x 时最小二乘解的相对误差。Householder QR 和 SVD 的精度损失与 kappa(A) 成正比；正规方程的精度损失与 kappa(A)^2 成正比，且 kappa(A) 超过约 10^8 后完全失效（A^T A 的 Cholesky 分解失败）。](./plots/least-squares-accuracy.py)

## 3.3. 特征值问题

### 3.3.1. 基本定义

**定义 3.3.1（特征值与特征向量）** 设 $A\in\mathbb{C}^{m\times m}$ 为方阵。若非零向量 $\boldsymbol{x}\in\mathbb{C}^m$ 与 $\lambda\in\mathbb{C}$ 满足 $A\boldsymbol{x}=\lambda\boldsymbol{x}$，则称 $\boldsymbol{x}$ 为 $A$ 的**特征向量**，$\lambda$ 为对应的**特征值**。$A$ 的全体特征值构成的集合称为 $A$ 的**谱**，它是 $\mathbb{C}$ 的子集，记作 $\Lambda(A)$。

想法是：矩阵在 $\mathbb{C}^m$ 的某个子空间 $S$ 上的作用有时就像数乘。子空间 $E_\lambda=\mathcal{N}(A-\lambda I)$ 是 $\lambda$ 的特征子空间，其中任何非零 $\boldsymbol{x}$ 都是特征向量；由于 $AE_\lambda\subseteq E_\lambda$，特征子空间是 $A$ 的不变子空间。特征值问题只在映射的值域与定义域是同一空间时才有意义，且

$$
\det A=\prod_{j=1}^m\lambda_j,\qquad \operatorname{tr}(A)=\sum_{j=1}^m\lambda_j .
$$
属于不同特征值的特征向量的线性组合不是特征向量。在 $\mathbb{C}$ 上，由代数基本定理，每个方阵至少有一个特征值和特征向量。

$\lambda$ 的**几何重数**是 $\dim E_\lambda=\dim\mathcal{N}(A-\lambda I)$。**特征多项式** $p_A(z)=\det(zI-A)=(z-\lambda_1)(z-\lambda_2)\cdots(z-\lambda_m)$ 是 $m$ 次多项式；合并相同的根得 $p_A(z)=(z-\lambda_1)^{k_1}\cdots(z-\lambda_r)^{k_r}$，$r\le m$，$\lambda_j$ 的**代数重数**是它作为 $p_A$ 的根的重数 $k_j$。几何重数永远不超过代数重数。对

$$
A=\begin{bmatrix}1&2\\0&1\end{bmatrix},\qquad \det(A-\lambda I)=(1-\lambda)^2,\qquad A-I=\begin{bmatrix}0&2\\0&0\end{bmatrix},
$$
特征值 $1$ 的代数重数为 $2$，几何重数却为 $1$。

$A$ 的**极小多项式** $\mu_A$ 是使 $\mathbb{P}(A)=O$ 的次数最低的首一多项式 $P$；任何满足 $Q(A)=O$ 的多项式 $Q$ 都是 $\mu_A$ 的倍式。由 **Cayley–Hamilton 定理**，矩阵满足它自己的特征方程 $p_A(A)=O$，所以 $\mu_A\mid p_A$：若 $p_A(z)=\prod_j(z-\lambda_j)^{k_j}$，则 $\mu_A(z)=\prod_j(z-\lambda_j)^{s_j}$，$1\le s_j\le k_j$。在 $A$ 的 **Jordan 标准形**（[2.1.10](/2.1.10)）中，$\lambda$ 的几何重数是属于 $\lambda$ 的 Jordan 块的个数，代数重数是这些块的阶数之和，它在 $\mu_A$ 中的重数 $s_j$ 是其中最大块的阶数；$A$ 可对角化当且仅当每个 Jordan 块都是 1 阶的，即当且仅当 $\mu_A$ 只有单根。

矩阵的秩是非零奇异值的个数，却不是非零特征值的个数：$A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ 的秩为 $1$，$\sigma_1=1$，$\sigma_2=0$，但 $\lambda_1=\lambda_2=0$。对可对角化矩阵两者一致，这时 $\mathcal{N}(A)=E_0(A)$，$\mathcal{R}(A)$ 是 $\lambda\ne0$ 的各特征子空间之和。

**例 3.3.1** 求实矩阵 $A$ 使 $A^7=A^4$ 而 $A^2\ne A$。极小多项式必须满足 $\mu_A(x)\mid x^7-x^4=x^4(x-1)(x^2+x+1)$ 且 $\mu_A(x)\nmid x^2-x=x(x-1)$。所以可以直接取 $\mu_A(x)=x^2$、$x^3$ 或 $x^4$，使 $A$ 幂零，例如

$$
A=\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad A=\begin{bmatrix}0&1&\\&0&1\\&&0\end{bmatrix}\quad\text{或}\quad A=\begin{bmatrix}0&1&&\\&0&1&\\&&0&1\\&&&0\end{bmatrix}.
$$
也可以令 $\mu_A(x)=x^2+x+1$，其根为 $\lambda=\frac{-1\pm\sqrt3\,\mathrm{i}}2$。由于 $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ 的特征值为 $a\pm b\mathrm{i}$，可以取旋转 $120°$ 的矩阵

$$
A=\begin{bmatrix}-1/2&-\sqrt3/2\\\sqrt3/2&-1/2\end{bmatrix},
$$
它满足 $A^3=I$，从而 $A^7=A=A^4$，而 $A^2\ne A$。

**例 3.3.2** 证明对 $A=\begin{bmatrix}4&-2\\5&-3\end{bmatrix}$ 有 $A^4=5A+6I$。特征多项式为 $p_A(\lambda)=(4-\lambda)(-3-\lambda)+10=\lambda^2-\lambda-2$，根为 $\lambda_1=-1$，$\lambda_2=2$。由 Cayley–Hamilton 定理 $A^2-A-2I=O$，故 $A^2=A+2I$，$A^3=A^2+2A=3A+2I$，$A^4=3A^2+2A=3(A+2I)+2A=5A+6I$。另一种做法：$f(x)=x^4-5x-6$ 满足 $f(\lambda_1)=f(\lambda_2)=0$，所以 $p_A\mid f$，由 $p_A(A)=O$ 得 $f(A)=O$。

实矩阵的特征值或为实数，或成共轭复数对出现；实对称矩阵的特征值为实数，特征向量相互正交。判断矩阵是否正定有一个借助对角占优的快捷方法。

**定义 3.3.2（严格对角占优）** 若对所有 $i$ 有 $\lvert a_{ii}\rvert>\sum_{j\ne i}\lvert a_{ij}\rvert$，称 $A$ 严格（行）对角占优；若对所有 $i$ 有 $\lvert a_{ii}\rvert>\sum_{j\ne i}\lvert a_{ji}\rvert$，称 $A$ 严格列对角占优。

**定理 3.3.1（Gershgorin 圆盘定理）** $A$ 的每个特征值都至少落在一个 Gershgorin 圆盘 $D\bigl(a_{ii},\sum_{j\ne i}\lvert a_{ij}\rvert\bigr)$（$i=1,\dots,m$）中。

**证明** 对特征值 $\lambda$，把特征向量 $\boldsymbol{x}$ 缩放到最大分量为 $x_i=1$，其余 $j\ne i$ 满足 $\lvert x_j\rvert\le1$。$A\boldsymbol{x}=\lambda\boldsymbol{x}$ 的第 $i$ 行为 $\sum_{j\ne i}a_{ij}x_j+a_{ii}=\lambda$，于是 $\lvert\lambda-a_{ii}\rvert=\bigl\lvert\sum_{j\ne i}a_{ij}x_j\bigr\rvert\le\sum_{j\ne i}\lvert a_{ij}\rvert$。$\square$

**推论 3.3.1** 对所有 $i$ 满足 $a_{ii}>\sum_{j\ne i}\lvert a_{ij}\rvert$ 的对称矩阵是正定的。

事实上，它的特征值都是实数，又落在位于右半平面的圆盘中。逆命题不成立；正定矩阵只满足 $\lvert a_{ij}\rvert<\sqrt{a_{ii}a_{jj}}\le(a_{ii}+a_{jj})/2$。

特征值特别适合分析由线性方程支配的系统随时间演化的行为，即 $t\to\infty$ 时 $A^t$ 或 $\mathrm{e}^{tA}=\sum_{n=0}^\infty\frac{(tA)^n}{n!}$ 的行为：例如共振（乐器或桥梁的振动）和稳定性（受小扰动的流体流动）的研究。若 $A$ 有 $m$ 个线性无关的特征向量，$A\boldsymbol{x}_j=\lambda_j\boldsymbol{x}_j$ 等价于 $AX=X\Lambda$，其中 $X=[\boldsymbol{x}_1|\cdots|\boldsymbol{x}_m]$，$\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_m)$，即 $A=X\Lambda X^{-1}$。于是 $X^{-1}A=\Lambda X^{-1}$ 是换到"特征向量坐标"的基变换，且 $A^n=X\Lambda^nX^{-1}$。

### 3.3.2. 幂迭代法

为求 $A$ 的主特征值（模最大者，$\lvert\lambda_1\rvert>\lvert\lambda_i\rvert$，$i\ne1$）及其特征向量，我们反复用 $A$ 乘一个向量。

**算法 3.3.1（幂迭代法）** 随机选取 $\boldsymbol{q}_0\in\mathbb{R}^n$，$\|\boldsymbol{q}_0\|=1$。对 $k=1,2,\dots$，当 $\|\boldsymbol{q}_{k-1}-\boldsymbol{q}_{k-2}\|>\varepsilon$ 时：令 $\boldsymbol{z}_k=A\boldsymbol{q}_{k-1}$，$\boldsymbol{q}_k=\boldsymbol{z}_k/\|\boldsymbol{z}_k\|$，$\lambda^{(k)}=\boldsymbol{q}_k^{\mathsf T}A\boldsymbol{q}_k$。

**定理 3.3.2** 设 $A\in\mathbb{R}^{n\times n}$ 可对角化，特征值满足 $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert\ge\cdots\ge\lvert\lambda_n\rvert$，单位特征向量为 $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$，并设 $\boldsymbol{q}_0=\sum_ic_i\boldsymbol{x}_i$，$c_1\ne0$。则 $\boldsymbol{q}_k$ 在相差符号的意义下收敛到 $\boldsymbol{x}_1$，误差为 $O(\lvert\lambda_2/\lambda_1\rvert^k)$，且 $\lambda^{(k)}\to\lambda_1$。

**证明** $n$ 个线性无关的特征向量构成 $\mathbb{R}^n$ 的基，$c_1\ne0$ 表示 $\boldsymbol{q}_0$ 在 $\boldsymbol{x}_1$ 方向有分量。于是

$$
A^k\boldsymbol{q}_0=\sum_{i=1}^nc_iA^k\boldsymbol{x}_i=\sum_{i=1}^nc_i\lambda_i^k\boldsymbol{x}_i=c_1\lambda_1^k\Bigl(\boldsymbol{x}_1+\sum_{i=2}^n\frac{c_i}{c_1}\Bigl(\frac{\lambda_i}{\lambda_1}\Bigr)^k\boldsymbol{x}_i\Bigr).
$$
由于 $\lambda_1$ 占优，$(\lambda_i/\lambda_1)^k\to0$，$A^k\boldsymbol{q}_0$ 趋于方向 $c_1\lambda_1^k\boldsymbol{x}_1$。幂迭代法只是对乘积 $A\boldsymbol{q}_{k-1}$ 作归一化以避免上溢或下溢，$\boldsymbol{q}_k=A^k\boldsymbol{q}_0/\|A^k\boldsymbol{q}_0\|$，所以它收敛到 $\pm\boldsymbol{x}_1$，特征值估计满足 $\boldsymbol{q}_k^{\mathsf T}A\boldsymbol{q}_k\approx\boldsymbol{q}_k^{\mathsf T}\lambda_1\boldsymbol{q}_k=\lambda_1$。$\square$

实际中幂迭代法是否好用取决于比值 $\lvert\lambda_2\rvert/\lvert\lambda_1\rvert$，它决定了收敛速度。$\boldsymbol{q}_0$ 缺少 $\boldsymbol{x}_1$ 分量（$c_1=0$）的危险不必太担心：若 $\boldsymbol{q}_0$ 随机选取，$c_1=0$ 的概率为 $0$，而且舍入误差通常会使某些 $\boldsymbol{q}_k$ 获得 $\boldsymbol{x}_1$ 方向的分量。每次迭代只算一次矩阵乘向量，$O(n^2)$ flops，若 $A$ 稀疏则远少于此：即使 $n$ 非常大，方法也很高效，Google 的 PageRank 算法就是一例。当主特征值的模不唯一时方法失效，例如旋转矩阵的特征值 $\mathrm{e}^{\pm\mathrm{i}\theta}$ 模相同，$\boldsymbol{q}_k$ 只会不停地旋转。

对 Hermite 矩阵 $A$ 和非零向量 $\boldsymbol{q}$，**Rayleigh 商** $R(A,\boldsymbol{q})=\boldsymbol{q}^{\mathsf H}A\boldsymbol{q}/(\boldsymbol{q}^{\mathsf H}\boldsymbol{q})$ 满足 $\lambda_n\le R(A,\boldsymbol{q})\le\lambda_1$（特征值按递减排列）；$\lambda^{(k)}$ 就是 $\boldsymbol{q}_k$ 的 Rayleigh 商。对对称矩阵，Rayleigh 商在特征向量处取驻值，所以特征值误差是特征向量误差的平方量级，为 $O(\lvert\lambda_2/\lambda_1\rvert^{2k})$。

![对 lambda_1 = 1、|lambda_2/lambda_1| = 0.5、0.8、0.95 的 50 x 50 对称矩阵作幂迭代。特征向量误差按 ratio^k 下降（虚线），Rayleigh 商的特征值误差按 ratio^(2k) 下降，直到两者都降到舍入误差的水平。](./plots/power-method-convergence.py)

**例 3.3.3（PageRank）** 搜索引擎必须做三件事：抓取网络、找到所有公开可访问的网页；为数据建立索引，以便高效地按关键词检索；评定每个网页的重要性，使用户检索时在含有所需信息的网页中先呈现更重要的网页。PageRank 给每个网页一个数值权重，衡量它在超链接文档集中的相对重要性。对一个由四个网页组成的网络，若网页 $j$ 把自己的重要性平均分给它链接到的网页，链接矩阵为

$$
A=\begin{bmatrix}0&0&1&\frac12\\\frac13&0&0&0\\\frac13&\frac12&0&\frac12\\\frac13&\frac12&0&0\end{bmatrix},
$$
重要性得分满足 $A\boldsymbol{x}=\boldsymbol{x}$：$\boldsymbol{x}$ 是这个列随机矩阵的主特征值 $1$ 的特征向量，这里 $\boldsymbol{x}\propto(12,4,9,6)^{\mathsf T}$。对拥有数十亿网页的真实网络，它由幂迭代法计算。

### 3.3.3. 揭示特征值的分解

**定义 3.3.3（特征值分解）** 方阵 $A$ 的**特征值分解**（谱分解）是分解

$$
A=X\Lambda X^{-1},
$$
其中 $X$ 可逆，$\Lambda$ 为对角矩阵。代数重数大于几何重数的特征值称为**亏损特征值**，有一个或多个亏损特征值的矩阵称为**亏损矩阵**。

**定理 3.3.3** 方阵 $A$ 有特征值分解 $A=X\Lambda X^{-1}$，当且仅当它非亏损，即可对角化。

这种分解并不总是存在，而 R 并不会对此发出警告：

```r
A <- matrix(c(1, 0, 2, 1), 2)    # rows (1, 2) and (0, 1)
eigen(A)
```

```text
eigen() decomposition
$values
[1] 1 1

$vectors
     [,1]          [,2]
[1,]    1 -1.000000e+00
[2,]    0  1.110223e-16
```

算出的两个特征向量在舍入误差范围内平行，矩阵 $X$ 在数值上是奇异的。分解存在时也不唯一（特征向量可以缩放和重排，多维特征子空间中任何一组基都可以）。即使分解存在，若 $X$ 高度病态，从 $A$ 到 $\Lambda$ 的过程中也可能丢失大量信息。

酉对角化。 若存在酉矩阵 $Q$ 使 $A=Q\Lambda Q^{\mathsf H}$，则称 $A$ 可酉对角化：$m$ 个线性无关的特征向量可以取为标准正交的。

**定理 3.3.4** 矩阵可酉对角化当且仅当它是正规的，即 $A^{\mathsf H}A=AA^{\mathsf H}$。

**正规矩阵**的例子有 Hermite 矩阵（$A=A^{\mathsf H}$）、斜 Hermite 矩阵（$A=-A^{\mathsf H}$）、酉矩阵（$A^{-1}=A^{\mathsf H}$）和循环矩阵，以及它们加上 $kI$。对称性解释了 $\|A\|_2=\sigma_1$ 和 $\|A^{-1}\|_2=1/\sigma_m$：由于 $B=A^{\mathsf H}A$ 是 Hermite 矩阵，$\mathbb{C}^n$ 有一组由 $B$ 的特征向量构成的标准正交基 $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$，特征值为 $\lambda_1,\dots,\lambda_n\ge0$。对 $\boldsymbol{x}=a_1\boldsymbol{e}_1+\cdots+a_n\boldsymbol{e}_n$，

$$
\|A\boldsymbol{x}\|_2^2=\boldsymbol{x}^{\mathsf H}A^{\mathsf H}A\boldsymbol{x}=\langle\boldsymbol{x},B\boldsymbol{x}\rangle=\langle\boldsymbol{x},a_1\lambda_1\boldsymbol{e}_1+\cdots+a_n\lambda_n\boldsymbol{e}_n\rangle=\sum_j\lambda_j\lvert a_j\rvert^2\le\max_j\lambda_j\,\|\boldsymbol{x}\|_2^2,
$$
所以 $\|A\|_2\le\sqrt{\max_j\lambda_j}=\sigma_1$，取 $\boldsymbol{x}=\boldsymbol{e}_{j_0}$（最大特征值的特征向量）时等号成立；对 $A^{-1}$ 应用同样的论证得 $\|A^{-1}\|_2=1/\sigma_m$。

正规矩阵也正是特征值完全良态的矩阵。对一般的可对角化矩阵，敏感程度取决于特征向量矩阵。

**定理 3.3.5（Bauer–Fike 定理）** 设 $A\in\mathbb{C}^{n\times n}$ 可对角化，$A=X\Lambda X^{-1}$，$\mu$ 是 $A+\delta A$ 的特征值。则对任何 $p$-范数

$$
\min_{\lambda\in\Lambda(A)}\lvert\lambda-\mu\rvert\le\kappa_p(X)\,\|\delta A\|_p .
$$

对正规矩阵，$X$ 可取为酉矩阵，$\kappa_2(X)=1$：若 $\lambda$ 与 $\lambda+\delta\lambda$ 是 $A$ 与 $A+\delta A$ 的对应特征值，则 $\lvert\delta\lambda\rvert\le\|\delta A\|_2$。因此对称（乃至正规）特征值问题的绝对条件数为 $\hat\kappa=1$。

**定义 3.3.4（Schur 分解）** 方阵 $A$ 的 **Schur 分解**（酉三角化）是分解 $A=QTQ^{\mathsf H}$，其中 $Q$ 为酉矩阵，$T$ 为上三角矩阵。实矩阵 $A$ 的实 Schur 分解是 $A=QTQ^{\mathsf T}$，其中 $Q$ 正交，$T$ 为拟上三角矩阵（对角线上为 $1\times1$ 和 $2\times2$ 块的块上三角矩阵，$2\times2$ 块承载共轭复特征值对）。

由于 $A$ 与 $T$ 相似，$A$ 的特征值出现在 $T$ 的对角线上。由 **Schur 定理**（[2.1.12](/2.1.12)），每个方阵都有 Schur 分解。

**例 3.3.4** 矩阵

$$
A=\begin{bmatrix}-2&4&0&-1\\8&-1&0&4\\-2&1&1&9\\7&7&-1&-1\end{bmatrix}
$$
的特征值为 $\lambda_1=6.1429$，$\lambda_{2,3}=-0.6175\pm1.7365\mathrm{i}$，$\lambda_4=-7.9078$。它的实 Schur 分解 $A=QTQ^{\mathsf T}$ 中

$$
T=Q^{\mathsf T}AQ=\begin{bmatrix}6.1429&7.1693&-2.3027&-2.8451\\0&-0.6175&-11.0418&0.4232\\0&0.2731&-0.6175&-0.9995\\0&0&0&-7.9078\end{bmatrix},
$$
其中 $2\times2$ 对角块的特征值为 $-0.6175\pm\mathrm{i}\sqrt{11.0418\times0.2731}=-0.6175\pm1.7365\mathrm{i}$。

**算法 3.3.2（QR 算法）** 设 $A$ 是要求特征值的实矩阵。令 $A_0=A$。对 $k=0,1,2,\dots$：计算 QR 分解 $A_k=Q_kR_k$，令 $A_{k+1}=R_kQ_k$。

由于 $A_{k+1}=R_kQ_k=Q_k^{-1}Q_kR_kQ_k=Q_k^{-1}A_kQ_k$，所有 $A_k$ 都相似，有相同的特征值。若 $\lvert\lambda_1\rvert>\lvert\lambda_2\rvert>\cdots>\lvert\lambda_n\rvert$，$A_k$ 收敛到上三角矩阵 $T$，即 $A$ 的一个 Schur 形，其对角线列出各特征值。实用的版本先用 Householder 反射把 $A$ 化为上 Hessenberg 形，再用位移加速收敛；`eigen` 调用的就是这类 LAPACK 子程序（对称矩阵另有专用程序）。

三种揭示特征值的分解把矩阵化为显式呈现特征值的形式，它们是嵌套的：

- 对角化 $A=X\Lambda X^{-1}$ 存在，当且仅当 $A$ 非亏损；
- 酉对角化 $A=Q\Lambda Q^{\mathsf H}$ 存在，当且仅当 $A$ 正规；
- 酉三角化（Schur 分解）$A=QTQ^{\mathsf H}$ 总是存在。

就适用的矩阵而言，Schur 分解（所有方阵）$\supset$ 特征值分解（可对角化矩阵）$\supset$ 酉对角化（正规矩阵）；Schur 形是数值特征值计算的通用基础。

### 3.3.4. SVD 与特征值分解的比较

对可酉对角化的 $A=Q\Lambda Q^{\mathsf H}$，这本身是特征值分解，而 $A=Q\lvert\Lambda\rvert\bigl(\operatorname{sgn}(\Lambda)Q^{\mathsf H}\bigr)=U\Sigma V^{\mathsf H}$，其中 $U=Q$，$\Sigma=\lvert\Lambda\rvert$，$V=Q\,\overline{\operatorname{sgn}(\Lambda)}$，$\operatorname{sgn}(\Lambda)=\operatorname{diag}(\lambda_j/\lvert\lambda_j\rvert)$（$\lambda_j=0$ 时取 $1$），给出一个 SVD（再按 $\lvert\lambda_j\rvert$ 递减重排）。因此当 $A$ 是对称半正定矩阵（更一般地，Hermite 半正定矩阵）时，奇异值也是特征值，这时 SVD 与特征值分解一致。一般地，对每个特征对都有 $\sigma_1=\|A\|_2\ge\|A\boldsymbol{x}\|/\|\boldsymbol{x}\|=\lvert\lambda\rvert$，所以 $\sigma_1\ge\lvert\lambda_1\rvert$。

两种分解都以对角化矩阵为主题，但：

| | 特征值分解 $A=X\Lambda X^{-1}$ | SVD $A=U\Sigma V^{\mathsf H}$ |
|---|---|---|
| 适用对象 | 非亏损的方阵 | 所有矩阵，包括长方阵 |
| 基 | 一组基（特征向量），一般不正交 | 两组标准正交基（左、右奇异向量） |
| 对角元 | 一般为复数 | 实数、非负 |
| 相关的问题 | $A^k$ 或 $\mathrm{e}^{tA}$ 的行为 | $A$ 本身或 $A^{-1}$ 的行为 |

## 小结

没有最好的算法，只有最适合问题的算法。

| 问题 | 工具 | 稳定性与代价 |
|---|---|---|
| 线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$ | 列主元 LU，$PA=LU$；SPD 矩阵用 Cholesky，$A=R^{\mathsf T}R$ | LU 需要选主元；Cholesky 不选主元也稳定，代价减半 |
| 最小二乘 $A\boldsymbol{x}\approx\boldsymbol{b}$ | Householder QR 为标准；奇异或近奇异的 $A$ 用 SVD | 正规方程把误差放大 $\kappa(A)^2$ 倍；QR 稳定；SVD 最稳健、最昂贵 |
| 矩阵结构（秩、压缩、PCA） | SVD，适用于任意矩阵 | 奇异值按重要性给方向排序；最优低秩近似 |
| 特征值、矩阵幂、长期行为 | 特征值分解用于 $A^k$；Schur 形适用于任意方阵；幂迭代法求大型稀疏矩阵的主特征值 | 正规矩阵的特征值完全良态 |

| 运算 | 运算量（首项） |
|---|---|
| 解三角方程组 | $m^2$ |
| LU 分解（Gauss 消元） | $\frac23m^3$ |
| Cholesky 分解 | $\frac13m^3$ |
| Gram–Schmidt QR（经典或修正） | $2mn^2$ |
| Householder QR | $2mn^2-\frac23n^3$ |
| Givens QR | $3mn^2-n^3$ |
| 最小二乘：正规方程 / QR / SVD | $mn^2+\frac13n^3$ / $2mn^2-\frac23n^3$ / $2mn^2+11n^3$ |

关键事实：正交变换不放大误差（$\|QA\|_2=\|A\|_2$），这是 QR 和 SVD 数值稳定的基础；直接解正规方程 $A^{\mathsf T}A\boldsymbol{x}=A^{\mathsf T}\boldsymbol{b}$ 会使条件数平方；修正与经典 Gram–Schmidt 在精确算术下等价，在浮点算术下却不同；矩阵可对角化当且仅当几何重数与代数重数相等，可酉对角化当且仅当它正规，而总可以通过酉相似化为三角形；SVD 对每个矩阵都存在，且 $\sigma_i=\sqrt{\lambda_i(A^{\mathsf H}A)}$；幂迭代法以速率 $\lvert\lambda_2/\lambda_1\rvert$ 收敛到模最大特征值的特征向量。
