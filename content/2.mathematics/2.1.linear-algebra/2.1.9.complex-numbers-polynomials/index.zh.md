---
title: 复数与多项式
---

矩阵能化简到什么程度，取决于它的特征多项式在所给数域上能分解到什么程度。例如 $\lambda^4+1$ 在 $\mathbb{Q}$ 上不可约，在 $\mathbb{R}$ 上分解为 $(\lambda^2+\sqrt2\lambda+1)(\lambda^2-\sqrt2\lambda+1)$，在 $\mathbb{C}$ 上分解为四个一次因式 $\prod_{k=0}^{3}(\lambda-\mathrm{e}^{\mathrm{i}(2k+1)\pi/4})$；相应地，以它为特征多项式的实矩阵在 $\mathbb{R}$ 上只能化成两个 $2\times2$ 块，在 $\mathbb{C}$ 上却能对角化。[第 8 章](/2.1.8) 的例 8.7.2 也说明了这一点。本章先系统地介绍复数——每个多项式都能完全分解的数域——以及复矩阵、复向量空间；再在一般数域 $\mathbb{F}$ 上研究一元多项式：带余除法、整除、最大公因式、不可约多项式与因式分解，最后讨论 $\mathbb{C}$、$\mathbb{R}$、$\mathbb{Q}$ 上的分解与根和系数的关系。

多项式理论将在 [第 10 章](/2.1.10) 中用于极小多项式和根子空间分解：把空间分解成线性变换的不变子空间的直和，靠的正是多项式的互素与 Bézout 等式；判断矩阵能否对角化，归结为检验极小多项式有没有重根，而这又只需用辗转相除法求一个最大公因式。[第 11 章](/2.1.11) 的矩阵函数用插值多项式计算。整章可以对照整数来读：$\mathbb{F}[x]$ 与 $\mathbb{Z}$ 一样有带余除法、最大公因数与唯一分解，它们都是离散数学中**多项式环**与**整环**（[1.3.3](/1.3.3)）的例子。多项式的计算还处处体现"标准化求解"：除法化为综合除法，最大公因式化为反复的带余除法，有理根化为有限次验证。

## 9.1. 复数

### 9.1.1. 复数的定义与运算

实矩阵 $A=\begin{bmatrix}a&-b\\b&a\end{bmatrix}$（$a,b\in\mathbb{R}$，$b\neq0$）的特征多项式 $(\lambda-a)^2+b^2$ 没有实根：在平面上 $A$ 是旋转与伸缩的复合，没有不变的方向。为了让它有特征值，需要引入满足 $\mathrm{i}^2=-1$ 的数 $\mathrm{i}$，这时特征值为 $a\pm b\mathrm{i}$。

**定义 9.1.1（复数）** 引入记号 $\mathrm{i}$，规定 $\mathrm{i}^2=-1$。形如 $z=a+b\mathrm{i}$（$a,b\in\mathbb{R}$）的数称为**复数**，$a=\operatorname{Re}z$ 与 $b=\operatorname{Im}z$ 分别称为 $z$ 的实部与虚部；全体复数记作 $\mathbb{C}=\{a+b\mathrm{i}\mid a,b\in\mathbb{R}\}$。

复数按多项式的规则运算，并把 $\mathrm{i}^2$ 换成 $-1$：

$$
(a_1+b_1\mathrm{i})\pm(a_2+b_2\mathrm{i})=(a_1\pm a_2)+(b_1\pm b_2)\mathrm{i},\qquad (a_1+b_1\mathrm{i})(a_2+b_2\mathrm{i})=(a_1a_2-b_1b_2)+(a_1b_2+a_2b_1)\mathrm{i}.
$$

**定义 9.1.2（共轭复数）** 复数 $z=a+b\mathrm{i}$ 的**共轭复数**是 $\bar z=a-b\mathrm{i}$。实数 $|z|=\sqrt{a^2+b^2}$ 称为 $z$ 的**模**。

共轭的基本性质：$\bar z=z$ 当且仅当 $z\in\mathbb{R}$；$\bar z=-z$ 当且仅当 $z$ 是零或纯虚数；$\overline{z_1\pm z_2}=\bar z_1\pm\bar z_2$，$\overline{z_1z_2}=\bar z_1\bar z_2$；$z\bar z=a^2+b^2=|z|^2$。由最后一式，$z\neq0$ 时 $\dfrac1z=\dfrac{\bar z}{|z|^2}$，$\dfrac{z_1}{z_2}=\dfrac{z_1\bar z_2}{|z_2|^2}$。所以 $\mathbb{C}$ 对四则运算封闭，是一个**数域**，而且是最大的数域。

### 9.1.2. 复数的几何表示与指数形式

复数 $z=a+b\mathrm{i}$ 有四种常用的写法：

1. 代数形式：$z=a+b\mathrm{i}$。
2. 几何形式：平面上的点 $(a,b)$，或从原点到 $(a,b)$ 的向量。复数的加法就是向量的加法，$\bar z$ 是关于实轴的反射，$|z|$ 是向量的长度。
3. 极形式：令 $r=|z|$，$\theta$ 为从正实轴到向量 $z$ 的转角，则 $\cos\theta=a/r$，$\sin\theta=b/r$，$z=r(\cos\theta+\mathrm{i}\sin\theta)$。
4. 指数形式：$z=r\mathrm{e}^{\mathrm{i}\theta}$（见下文的欧拉公式）。

**定义 9.1.3（复数的极形式）** 把非零复数写成 $z=r(\cos\theta+\mathrm{i}\sin\theta)$（$r=|z|>0$），称为 $z$ 的**极形式**（也称三角形式），$\theta$ 称为 $z$ 的**辐角**。辐角只确定到相差 $2\pi$ 的整数倍。

由三角函数的和角公式，

$$
r_1(\cos\theta_1+\mathrm{i}\sin\theta_1)\cdot r_2(\cos\theta_2+\mathrm{i}\sin\theta_2)=r_1r_2\big(\cos(\theta_1+\theta_2)+\mathrm{i}\sin(\theta_1+\theta_2)\big),
$$

即乘积的模是模的乘积，辐角是辐角的和：乘以 $z_2$ 就是把平面旋转 $\theta_2$、再伸缩 $r_2$ 倍。这与"指数相乘、指数相加"的规则相同，于是记

$$
\mathrm{e}^{\mathrm{i}\theta}=\cos\theta+\mathrm{i}\sin\theta,
$$

称为欧拉公式（Euler's Formula）。用幂级数可以把 $\mathrm{e}^z$ 定义到全体复数上，并证明这个等式（复变函数课程 2.3）；这里把它当作 $\mathrm{e}^{\mathrm{i}\theta}$ 的定义。由此 $\mathrm{e}^{\mathrm{i}\theta_1}\mathrm{e}^{\mathrm{i}\theta_2}=\mathrm{e}^{\mathrm{i}(\theta_1+\theta_2)}$，$(\mathrm{e}^{\mathrm{i}\theta})^n=\mathrm{e}^{\mathrm{i}n\theta}$（De Moivre 公式），$\mathrm{e}^{\mathrm{i}\theta}=\mathrm{e}^{\mathrm{i}(\theta+2k\pi)}$（$k\in\mathbb{Z}$），以及

$$
\mathrm{e}^{\mathrm{i}\pi}=-1,\qquad \mathrm{e}^{\mathrm{i}\pi/2}=\mathrm{i},\qquad \mathrm{e}^{2k\pi\mathrm{i}}=1\ (k\in\mathbb{Z}).
$$

**例 9.1.1** 求 $(1+\mathrm{i})^{10}$。$1+\mathrm{i}=\sqrt2\mathrm{e}^{\mathrm{i}\pi/4}$，所以 $(1+\mathrm{i})^{10}=2^5\mathrm{e}^{\mathrm{i}5\pi/2}=32\mathrm{i}$。用二项式展开需要计算 11 项，用指数形式只需算一次模的幂与一次辐角的倍数。又由 $(\cos\theta+\mathrm{i}\sin\theta)^2=\cos2\theta+\mathrm{i}\sin2\theta$，展开左边并比较实部与虚部，就得到倍角公式 $\cos2\theta=\cos^2\theta-\sin^2\theta$，$\sin2\theta=2\sin\theta\cos\theta$。

### 9.1.3. 复数的矩阵形式

**命题 9.1.1** 映射 $T\colon \mathbb{C}\to\mathbb{R}^{2\times2}$，$a+b\mathrm{i}\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ 是单射，并且保持加法与乘法：$T(z_1+z_2)=T(z_1)+T(z_2)$，$T(z_1z_2)=T(z_1)T(z_2)$。

**证明** 单射与保持加法显然。乘法：

$$
T(z_1)T(z_2)=\begin{bmatrix}a_1&-b_1\\b_1&a_1\end{bmatrix}\begin{bmatrix}a_2&-b_2\\b_2&a_2\end{bmatrix}=\begin{bmatrix}a_1a_2-b_1b_2&-(a_1b_2+a_2b_1)\\a_1b_2+a_2b_1&a_1a_2-b_1b_2\end{bmatrix}=T(z_1z_2).\ \square
$$

所以 $T$ 是一个单的**环同态**，$\mathbb{C}$ 同构于 $2\times2$ 实矩阵环中的子域 $\left\{\begin{bmatrix}a&-b\\b&a\end{bmatrix}\right\}$（也见 [第 8 章](/2.1.8) 的例 8.4.1）。在这个对应下，$\mathrm{i}$ 对应旋转 $90^\circ$ 的矩阵 $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$，它的平方是 $-I$；$\bar z$ 对应**转置**；$|z|^2$ 对应**行列式**；极形式对应

$$
T(r\mathrm{e}^{\mathrm{i}\theta})=r\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix},
$$

即伸缩矩阵 $rI$ 与旋转矩阵之积，这正是复数乘法的几何意义。把 $z=r\mathrm{e}^{\mathrm{i}\theta}$ 推广到矩阵，就是 [第 13 章](/2.1.13) 的极分解 $A=R\mathrm{e}^{\mathrm{i}M}$（$R$ 半正定，$\mathrm{e}^{\mathrm{i}M}$ 是酉矩阵）；矩阵 $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ 则是 [第 12 章](/2.1.12) 中二阶实正规矩阵的典型。

### 9.1.4. 复数的幂与方根

对实数 $\alpha$ 和 $z=r\mathrm{e}^{\mathrm{i}\theta}\neq0$，由 $z=r\mathrm{e}^{\mathrm{i}(\theta+2k\pi)}$，定义

$$
z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}\alpha(\theta+2k\pi)},\qquad k\in\mathbb{Z}.
$$

它可能有多个值：

- $\alpha\in\mathbb{Z}$ 时，$\mathrm{e}^{2\mathrm{i}\alpha k\pi}=1$，$z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}\alpha\theta}$ 只有一个值；
- $\alpha=q/p$（$p>0$，$p,q$ 互素）时，$z^\alpha=r^\alpha \mathrm{e}^{\mathrm{i}(q\theta+2qk\pi)/p}$ 随 $k$ 以 $p$ 为周期变化，恰有 $p$ 个值（$k=0,1,\dots,p-1$）；
- $\alpha\notin\mathbb{Q}$ 时，不同的 $k$ 给出不同的值，$z^\alpha$ 有无穷多个值。例如 $\mathrm{i}=\mathrm{e}^{\mathrm{i}(\pi/2+2k\pi)}$，所以 $\mathrm{i}^\pi=\mathrm{e}^{\mathrm{i}(\pi^2/2+2k\pi^2)}$，$k\in\mathbb{Z}$。

多值函数的系统处理（分支、Riemann 面）属于复变函数课程。最重要的是 $1$ 的方根。

**定义 9.1.4（单位根）** 方程 $z^n=1$ 的 $n$ 个复根 $\omega_k=\mathrm{e}^{2k\pi\mathrm{i}/n}$（$k=0,1,\dots,n-1$）称为 $n$ 次**单位根**。

记 $\omega=\omega_1=\mathrm{e}^{2\pi\mathrm{i}/n}$，则 $\omega_k=\omega^k$，$n$ 次单位根是单位圆的内接正 $n$ 边形的顶点，且 $x^n-1=\prod_{k=0}^{n-1}(x-\omega^k)$。它们满足：

- $\bar\omega_k=\omega_{n-k}$（$\omega_k$ 的模为 $1$，故 $\bar\omega_k=\omega_k^{-1}$）；
- $n\ge2$ 时 $1+\omega+\omega^2+\cdots+\omega^{n-1}=0$：由 $\omega\neq1$，等比数列求和得 $\frac{1-\omega^n}{1-\omega}=0$；几何上，正多边形的顶点向量之和为零。

下图左边演示乘法的几何意义：乘以 $w=1.3\,\mathrm{e}^{\mathrm{i}\pi/6}$ 把整个平面绕原点旋转 $30^\circ$ 并放大 $1.3$ 倍，图形的形状不变；右边是 $8$ 次单位根，它们是正八边形的顶点，首尾相接地依次相加回到原点。

![左：把图形 S 依次乘以 w = 1.3 e^{iπ/6}，每次旋转 30° 并放大 1.3 倍；右：8 次单位根 ω^k 构成单位圆的内接正八边形，部分和 1 + ω + ⋯ + ω^k 构成的折线（缩小 0.35 倍显示）回到原点](./plots/complex-multiplication-roots-of-unity.py)

## 9.2. 复矩阵与复向量空间

复矩阵 $A=[a_{ij}]\in\mathbb{C}^{m\times n}$ 的共轭是 $\bar A=[\bar a_{ij}]$。把元素的实部、虚部分开，$A=U+\mathrm{i}V$（$U,V$ 是实矩阵），则 $\bar A=U-\mathrm{i}V$；$A$ 是实矩阵当且仅当 $\bar A=A$；由 $\overline{z_1z_2}=\bar z_1\bar z_2$ 得 $\overline{AB}=\bar A\bar B$。例如

$$
\begin{bmatrix}1-\mathrm{i}&2\mathrm{i}\\3+\mathrm{i}&4\end{bmatrix}=\begin{bmatrix}1&0\\3&4\end{bmatrix}+\mathrm{i}\begin{bmatrix}-1&2\\1&0\end{bmatrix}.
$$

**定义 9.2.1（共轭转置）** 复矩阵 $A$ 的**共轭转置**（又称 Hermite 共轭）是 $A^{\mathsf H}=\bar A^{\mathsf T}=\overline{A^{\mathsf T}}$。

共轭转置满足 $(A^{\mathsf H})^{\mathsf H}=A$，$(A+B)^{\mathsf H}=A^{\mathsf H}+B^{\mathsf H}$，$(kA)^{\mathsf H}=\bar kA^{\mathsf H}$，$(AB)^{\mathsf H}=B^{\mathsf H}A^{\mathsf H}$；实矩阵的共轭转置就是转置。它在复数域上扮演转置在实数域上的角色，关键在于对复向量 $\boldsymbol{x}=[x_i]\neq\boldsymbol{0}$，

$$
\boldsymbol{x}^{\mathsf H}\boldsymbol{x}=\sum_i\bar x_ix_i=\sum_i|x_i|^2>0,
$$

而 $\boldsymbol{x}^{\mathsf T}\boldsymbol{x}$ 可以为零（如 $\boldsymbol{x}=[1\ \mathrm{i}]^{\mathsf T}$）。所以 $\mathbb{C}^n$ 上的标准内积要取成 $\langle\boldsymbol{x},\boldsymbol{y}\rangle=\boldsymbol{y}^{\mathsf H}\boldsymbol{x}$，见 [第 12 章](/2.1.12)。[第 7 章](/2.1.7) 证明实对称矩阵的特征值是实数，用的正是这个不等式。

**定义 9.2.2（复向量空间）** 复数域 $\mathbb{C}$ 上的线性空间（[第 8 章](/2.1.8) 的定义 8.1.2 中取 $\mathbb{F}=\mathbb{C}$）称为**复向量空间**。

复向量空间也可以只允许实数作数乘，看作实线性空间，这时维数加倍：$\dim_{\mathbb{C}}\mathbb{C}=1$（基 $1$），$\dim_{\mathbb{R}}\mathbb{C}=2$（基 $1,\mathrm{i}$）；$\dim_{\mathbb{C}}\mathbb{C}^2=2$，而作为实空间 $\mathbb{C}^2$ 有基 $[1\ 0]^{\mathsf T},[0\ 1]^{\mathsf T},[\mathrm{i}\ 0]^{\mathsf T},[0\ \mathrm{i}]^{\mathsf T}$，$\dim_{\mathbb{R}}\mathbb{C}^2=4$。一般地 $\dim_{\mathbb{R}}V=2\dim_{\mathbb{C}}V$。

复向量空间上的线性变换与矩阵的关系同第 8 章：$T\colon \mathbb{C}^n\to\mathbb{C}^n$ 是线性变换当且仅当存在 $A\in\mathbb{C}^{n\times n}$ 使 $T(\boldsymbol{x})=A\boldsymbol{x}$；在基 $\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n$ 下，$T(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)A$，$A$ 的第 $k$ 列是 $T(\boldsymbol{\alpha}_k)$ 的坐标；换基 $(\boldsymbol{\beta}_1,\dots,\boldsymbol{\beta}_n)=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_n)P$ 后矩阵变为 $P^{-1}AP$（定理 8.7.3）。于是一个线性变换对应一个相似等价类 $\{P^{-1}AP\mid P\text{ 可逆}\}$，"判断两个矩阵是否相似"就是"能否为同一个线性变换找到相应的两组基"（定理 8.7.4）。

**例 9.2.1** 判断 $A=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$ 与 $B=\begin{bmatrix}0&0&0\\1&0&0\\2&3&0\end{bmatrix}$ 是否相似。二者的特征多项式都是 $\lambda^3$，且都不可对角化，所以特征值不足以判断。令 $T(\boldsymbol{x})=A\boldsymbol{x}$，则 $T(\boldsymbol{e}_1)=\boldsymbol{0}$，$T(\boldsymbol{e}_2)=\boldsymbol{e}_1$，$T(\boldsymbol{e}_3)=\boldsymbol{e}_2$。$A$ 与 $B$ 相似，当且仅当存在基 $\boldsymbol{\beta}_1,\boldsymbol{\beta}_2,\boldsymbol{\beta}_3$ 使 $T$ 在其下的矩阵为 $B$，即

$$
T(\boldsymbol{\beta}_1)=\boldsymbol{\beta}_2+2\boldsymbol{\beta}_3,\qquad T(\boldsymbol{\beta}_2)=3\boldsymbol{\beta}_3,\qquad T(\boldsymbol{\beta}_3)=\boldsymbol{0}.
$$

从最后一式倒推：取 $\boldsymbol{\beta}_3=\boldsymbol{e}_1$；由 $T(\boldsymbol{\beta}_2)=3\boldsymbol{e}_1$ 取 $\boldsymbol{\beta}_2=3\boldsymbol{e}_2$；由 $T(\boldsymbol{\beta}_1)=3\boldsymbol{e}_2+2\boldsymbol{e}_1$ 取 $\boldsymbol{\beta}_1=2\boldsymbol{e}_2+3\boldsymbol{e}_3$。过渡矩阵

$$
P=[\boldsymbol{\beta}_1\ \boldsymbol{\beta}_2\ \boldsymbol{\beta}_3]=\begin{bmatrix}0&0&1\\2&3&0\\3&0&0\end{bmatrix}
$$

可逆（$\det P=-9$），所以 $B=P^{-1}AP$，$A$ 与 $B$ 相似。这种"沿 $T$ 的作用倒推出一串向量"的方法，在 [第 10 章](/2.1.10) 中发展为 Jordan 链；那里还会看到，相似与否只需比较 $\operatorname{rank}(A-\lambda I)^k$ 这一列数。

**例 9.2.2** 设 $A=\begin{bmatrix}a&-b\\b&a\end{bmatrix}$，$T(\boldsymbol{x})=A\boldsymbol{x}$。$\mathbb{C}^2$ 取标准内积，$\boldsymbol{e}_1,\boldsymbol{e}_2$ 是标准正交基。令 $\boldsymbol{v}_1=\frac1{\sqrt2}[1\ {-\mathrm{i}}]^{\mathsf T}$，$\boldsymbol{v}_2=\frac1{\sqrt2}[1\ \mathrm{i}]^{\mathsf T}$，则 $\boldsymbol{v}_1^{\mathsf H}\boldsymbol{v}_1=\boldsymbol{v}_2^{\mathsf H}\boldsymbol{v}_2=1$，$\boldsymbol{v}_2^{\mathsf H}\boldsymbol{v}_1=0$，也是一组标准正交基，且 $A\boldsymbol{v}_1=(a+b\mathrm{i})\boldsymbol{v}_1$，$A\boldsymbol{v}_2=(a-b\mathrm{i})\boldsymbol{v}_2$。所以 $T$ 在标准正交基 $\boldsymbol{v}_1,\boldsymbol{v}_2$ 下的矩阵是 $\operatorname{diag}(a+b\mathrm{i},a-b\mathrm{i})$：实矩阵 $A$ 不能在 $\mathbb{R}$ 上对角化，却能在 $\mathbb{C}$ 上用"复的正交矩阵"（酉矩阵）对角化。

这引出高等线性代数部分的几个目标，它们都是把复数的性质推广到矩阵：

| 复数 | 矩阵 | 章节 |
|---|---|---|
| $\mathbb{C}$ 上多项式完全分解 | 相似意义下的最简形：Jordan 标准形 | [第 10 章](/2.1.10) |
| $\mathrm{e}^z$ 等函数 | 矩阵函数 $\mathrm{e}^A$、线性微分方程组 | [第 11 章](/2.1.11) |
| $\mathbb{R}^n$ 的标准正交基、正交矩阵、正交相似、实对称矩阵 | $\mathbb{C}^n$ 的标准正交基、酉矩阵、酉相似、正规矩阵 | [第 12 章](/2.1.12) |
| 实数 $\bar z=z$，极形式 $z=r\mathrm{e}^{\mathrm{i}\theta}$ | Hermite 矩阵 $A^{\mathsf H}=A$，极分解 $A=R\mathrm{e}^{\mathrm{i}M}$ | [第 13 章](/2.1.13) |

## 9.3. 一元多项式与带余除法

### 9.3.1. 数域上的多项式

多项式的系数取自一个**数域** $\mathbb{F}$（[第 8 章](/2.1.8) 的定义 8.1.1）。除 $\mathbb{Q},\mathbb{R},\mathbb{C}$ 外，还有许多中间的数域。例如 $\mathbb{Q}(\sqrt2)=\{a+b\sqrt2\mid a,b\in\mathbb{Q}\}$ 是数域：它对加、减、乘显然封闭，而 $a+b\sqrt2\neq0$ 时 $\dfrac1{a+b\sqrt2}=\dfrac{a-b\sqrt2}{a^2-2b^2}\in\mathbb{Q}(\sqrt2)$（$\sqrt2$ 是无理数，故 $a^2-2b^2\neq0$）。但 $\{a+b\sqrt2+c\sqrt3\mid a,b,c\in\mathbb{Q}\}$ 不是数域，因为 $\sqrt2\cdot\sqrt3=\sqrt6$ 不在其中；把 $\sqrt6$ 补进去得到的 $\mathbb{Q}(\sqrt2,\sqrt3)=\{a+b\sqrt2+c\sqrt3+d\sqrt6\}$ 才是数域（乘法封闭可直接展开验证；求倒数时，先乘以把 $\sqrt3$ 变号的"共轭"化为 $\mathbb{Q}(\sqrt2)$ 中的数，再用上面的公式）。正实数集、整数集不是数域。

**定义 9.3.1（多项式）** 设 $\mathbb{F}$ 是数域，$x$ 是一个不定元，形如 $f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$（$a_i\in \mathbb{F}$）的表达式称为 $\mathbb{F}$ 上的（一元）**多项式**。$a_n\neq0$ 时，$a_nx^n$ 称为首项，$a_n$ 称为首项系数，$n$ 称为 $f$ 的次数，记作 $\deg f$；$a_0$ 称为常数项。首项系数为 $1$ 的多项式称为**首一多项式**。系数全为零的多项式称为零多项式，不定义它的次数。$\mathbb{F}$ 上多项式的全体记作 $\mathbb{F}[x]$。

两个多项式相等指它们的对应系数都相等。$x$ 可以用 $\mathbb{F}$ 中的数代入，也可以用 $\mathbb{F}$ 上的方阵代入：对 $f(x)=x^2+2x-3$ 和方阵 $A$，$f(A)=A^2+2A-3I$。后者是矩阵函数的起点（第 11 章）。

$\mathbb{F}[x]$ 中的加法与乘法按通常规则进行：若 $f=\sum_{i=0}^na_ix^i$，$g=\sum_{j=0}^mb_jx^j$，则 $fg=\sum_{l=0}^{n+m}\big(\sum_{i+j=l}a_ib_j\big)x^l$。对非零多项式（在有定义时）

$$
\deg(f+g)\le\max\{\deg f,\deg g\},\qquad \deg(fg)=\deg f+\deg g,
$$

后者是因为 $fg$ 的首项为 $a_nb_mx^{n+m}$，$a_nb_m\neq0$。所以 $\mathbb{F}[x]$ 没有零因子，是一个整环，而且只有非零常数可逆——与 $\mathbb{Z}$ 中只有 $\pm1$ 可逆相仿。$\mathbb{F}[x]$ 也是 $\mathbb{F}$ 上的无限维线性空间（第 8 章例 8.3.3）。

### 9.3.2. 带余除法与整除

多项式一般不能相除：$(x^2+1)\div(x+2)$ 不是多项式。仿照整数的 $9=4\times2+1$，有带余除法。

**定理 9.3.1（带余除法）** 设 $f,g\in \mathbb{F}[x]$，$g\neq0$，则存在唯一的 $q,r\in \mathbb{F}[x]$，使

$$
f=qg+r,\qquad r=0\ \text{或}\ \deg r<\deg g.
$$

$q,r$ 分别称为 $g$ 除 $f$ 的商与余式。

**证明** 存在性：若 $f=0$ 或 $\deg f<\deg g$，取 $q=0$，$r=f$。否则设 $f,g$ 的首项为 $a_nx^n$ 与 $b_mx^m$（$n\ge m$），则 $f_1=f-\frac{a_n}{b_m}x^{n-m}g$ 为零或次数小于 $n$，对 $\deg f$ 归纳即得。唯一性：若 $q_1g+r_1=q_2g+r_2$，则 $(q_1-q_2)g=r_2-r_1$；若 $q_1\neq q_2$，左边次数 $\ge\deg g$，右边为零或次数 $<\deg g$，矛盾。所以 $q_1=q_2$，$r_1=r_2$。$\square$

存在性的证明就是长除法：每一步用首项消去当前被除式的首项。整个过程只用到 $\mathbb{F}$ 中的四则运算，所以商与余式仍在 $\mathbb{F}[x]$ 中，而且不因把 $\mathbb{F}$ 换成更大的数域而改变；乘法次数约为 $(\deg f-\deg g+1)(\deg g+1)$。

**例 9.3.1** $6x^4-9x^2+18=(6x^2+9)(x^2-3)+45$；$x^5-x^3+3x^2-1=(x^2+2)(x^3-3x+2)+(x^2+6x-5)$。

**定义 9.3.2（整除）** 设 $f,g\in \mathbb{F}[x]$。若存在 $h\in \mathbb{F}[x]$ 使 $f=gh$，则称 $g$ **整除** $f$，记作 $g\mid f$，称 $g$ 是 $f$ 的因式。$g\neq0$ 时，$g\mid f$ 当且仅当 $g$ 除 $f$ 的余式为零。

整除的基本性质：

- 若 $f\mid g$ 且 $g\mid f$（$f,g\neq0$），则 $f=cg$，$c$ 为非零常数（此时称 $f,g$ 相伴）：由 $f=gh$，$g=fk$ 得 $f=fkh$，$\deg(kh)=0$；
- 若 $f\mid g_1$，$f\mid g_2$，则对任意 $h_1,h_2\in \mathbb{F}[x]$，$f\mid g_1h_1+g_2h_2$；
- 整除关系不随数域扩大而改变：若 $f,g\in \mathbb{F}[x]$，$\mathbb{F}\subseteq \mathbb{K}$，则在 $\mathbb{K}[x]$ 中 $g\mid f$ 当且仅当在 $\mathbb{F}[x]$ 中 $g\mid f$（带余除法的结果与数域无关）。

## 9.4. 余数定理、综合除法与插值

### 9.4.1. 余数定理与综合除法

用一次多项式 $x-a$ 作除式时，余式是常数。在 $f(x)=q(x)(x-a)+r$ 中代入 $x=a$ 得 $r=f(a)$。

**定理 9.4.1（余数定理）** 设 $f\in \mathbb{F}[x]$，$a\in \mathbb{F}$，则 $x-a$ 除 $f$ 的余式是 $f(a)$。特别地，$(x-a)\mid f$ 当且仅当 $f(a)=0$。

设 $f=a_nx^n+\cdots+a_1x+a_0$，$q=b_{n-1}x^{n-1}+\cdots+b_0$，比较 $f=q(x-a)+r$ 两边的系数，得到商与余式的递推公式：

**算法 9.4.1（综合除法）** 输入 $f=a_nx^n+\cdots+a_0$ 与 $a\in \mathbb{F}$：

1. $b_{n-1}=a_n$；
2. 对 $k=n-1,n-2,\dots,1$，计算 $b_{k-1}=a_k+ab_k$；
3. $r=a_0+ab_0$。

输出商 $q=b_{n-1}x^{n-1}+\cdots+b_0$ 与余式 $r=f(a)$。手算时排成三行：第一行是 $f$ 的系数，第三行从左到右逐个得出 $b_k$，每个 $b_k$ 乘以 $a$ 写在第二行下一列，再与第一行相加。

作为求值算法，综合除法就是 Horner 算法：

$$
f(a)=\big(\cdots\big((a_na+a_{n-1})a+a_{n-2}\big)a+\cdots+a_1\big)a+a_0,
$$

只需 $n$ 次乘法与 $n$ 次加法。逐项计算 $a_ka^k$ 需要约 $\frac{n(n+1)}2$ 次乘法；即使逐次累乘幂 $a^k=a\cdot a^{k-1}$，也需要 $2n-1$ 次乘法。可以证明，对一般的多项式，$n$ 次乘法已是最少（Ostrowski、Pan）。

**例 9.4.1** 用 $x+\frac12=x-(-\frac12)$ 除 $f=4x^4-6x^3+x+\frac12$：

| | $4$ | $-6$ | $0$ | $1$ | $\frac12$ |
|---|---|---|---|---|---|
| $\times(-\frac12)$ | | $-2$ | $4$ | $-2$ | $\frac12$ |
| | $4$ | $-8$ | $4$ | $-1$ | $1$ |

所以 $q=4x^3-8x^2+4x-1$，$r=f(-\frac12)=1$。

**例 9.4.2（按 $x-a$ 的方幂展开）** 把 $f=x^4-2x^3+3$ 写成 $\sum_kb_k(x-2)^k$。由 $f=(x-2)q_1+b_0$，$q_1=(x-2)q_2+b_1$，……，反复用 $x-2$ 做综合除法，依次得到余数 $b_0=3$，$b_1=8$，$b_2=12$，$b_3=6$，$b_4=1$，即

$$
x^4-2x^3+3=(x-2)^4+6(x-2)^3+12(x-2)^2+8(x-2)+3.
$$

由 Taylor 公式，$b_k=f^{(k)}(2)/k!$；这就是 [第 8 章](/2.1.8) 例 8.5.2 中 $f$ 在基 $1,x-2,\dots,(x-2)^{n-1}$ 下的坐标，但这里不必求导，也不必求过渡矩阵的逆，只用 $\frac{n(n+1)}2$ 次乘法。

```python
from fractions import Fraction

def synthetic_division(coeffs, a):
    """Divide f by (x - a); coeffs = [a_n, ..., a_1, a_0].
    Returns (quotient coefficients, remainder f(a)). Uses n multiplications."""
    b = [coeffs[0]]
    for c in coeffs[1:]:
        b.append(c + a * b[-1])
    return b[:-1], b[-1]

def taylor_shift(coeffs, a):
    """Coefficients of f in powers of (x - a), lowest degree first,
    by repeated synthetic division (n(n+1)/2 multiplications)."""
    out = []
    while coeffs:
        coeffs, rem = synthetic_division(coeffs, a)
        out.append(rem)
    return out

f = [4, -6, 0, 1, Fraction(1, 2)]          # 4x^4 - 6x^3 + x + 1/2
print(synthetic_division(f, Fraction(-1, 2)))   # quotient [4, -8, 4, -1], remainder 1
print(taylor_shift([1, -2, 0, 0, 3], 2))   # [3, 8, 12, 6, 1]
```

### 9.4.2. 根与重根

若 $a\in \mathbb{F}$ 使 $f(a)=0$，则称 $a$ 是 $f$ 在 $\mathbb{F}$ 中的根（零点）。根与数域有关：$x^2+1\in\mathbb{Q}[x]$ 在 $\mathbb{Q}$ 中没有根。由余数定理，$a$ 是根当且仅当 $(x-a)\mid f$。

**定义 9.4.1（重根）** 设 $f\neq0$，$a\in \mathbb{F}$，$k\ge1$。若 $(x-a)^k\mid f$ 而 $(x-a)^{k+1}\nmid f$，则称 $a$ 是 $f$ 的 $k$ 重根；$k=1$ 时称为单根，$k\ge2$ 时称为**重根**。

**命题 9.4.1**

1. 次数为 $n$ 的多项式在 $\mathbb{F}$ 中至多有 $n$ 个根（按重数计）。
2. 若 $\deg f\le n$，$\deg g\le n$，且在 $n+1$ 个不同的数处 $f(x_i)=g(x_i)$，则 $f=g$。
3. $a$ 是 $f$ 的重根，当且仅当 $f(a)=f'(a)=0$。这里 $f'$ 是形式导数：$(\sum a_kx^k)'=\sum ka_kx^{k-1}$。

**证明** 1：对 $n$ 归纳。若 $a$ 是根，$f=(x-a)f_1$，$\deg f_1=n-1$，而 $f$ 的其他根都是 $f_1$ 的根（$b\neq a$ 时 $(b-a)f_1(b)=0$ 推出 $f_1(b)=0$）。2：$h=f-g$ 若非零，次数 $\le n$，却有 $n+1$ 个根，与 1 矛盾。3：写 $f=(x-a)^kg$，$g(a)\neq0$，$k\ge1$，则 $f'=(x-a)^{k-1}\big(kg+(x-a)g'\big)$，而 $kg(a)+0\neq0$，所以 $f'(a)=0$ 当且仅当 $k\ge2$。$\square$

### 9.4.3. 插值

给定 $\mathbb{F}$ 中 $n+1$ 个点 $(a_0,b_0),\dots,(a_n,b_n)$，$a_i$ 两两不同，求次数不超过 $n$ 的多项式 $L$ 使 $L(a_i)=b_i$。由命题 9.4.1 的第 2 条，这样的 $L$ 至多一个。存在性有两种求法：

1. 解线性方程组：把 $L=c_0+c_1x+\cdots+c_nx^n$ 代入，得到系数矩阵为 **Vandermonde 矩阵**的方程组，它可逆（[第 5 章](/2.1.5)），这就是**多项式插值**的存在唯一性。但用 Gauss 消元求解需要 $O(n^3)$ 次运算，且 Vandermonde 矩阵通常非常病态。
2. 直接构造，即下面的 Lagrange 公式，只需 $O(n^2)$ 次运算。

**定理 9.4.2（Lagrange 插值多项式）** 令

$$
L_i(x)=\prod_{j\neq i}\frac{x-a_j}{a_i-a_j}=\frac{(x-a_0)\cdots(x-a_{i-1})(x-a_{i+1})\cdots(x-a_n)}{(a_i-a_0)\cdots(a_i-a_{i-1})(a_i-a_{i+1})\cdots(a_i-a_n)},
$$

则 $L_i(a_j)=\delta_{ij}$，且 $L(x)=b_0L_0(x)+b_1L_1(x)+\cdots+b_nL_n(x)$ 是唯一的次数不超过 $n$、满足 $L(a_i)=b_i$ 的多项式，称为 Lagrange 插值多项式。

**证明** $L_i$ 的分子在 $a_j$（$j\neq i$）处为零，在 $a_i$ 处等于分母，所以 $L_i(a_j)=\delta_{ij}$，$L(a_j)=\sum_ib_i\delta_{ij}=b_j$；$\deg L\le n$。唯一性见上。$\square$

$L_0,\dots,L_n$ 是 $\mathbb{F}[x]_{n+1}$ 的一组基，$L$ 在这组基下的坐标就是 $(b_0,\dots,b_n)$；而且 $L_0,\dots,L_n$ 恰是第 8 章取值映射 $p\mapsto(p(a_0),\dots,p(a_n))$ 下标准基 $\boldsymbol{e}_i$ 的原像。用余数的语言，插值问题是求次数 $\le n$ 的 $L$，使 $L$ 除以 $x-a_i$ 的余式为 $b_i$（$i=0,\dots,n$），这是多项式的中国剩余定理的特例。[第 11 章](/2.1.11) 还要求导数值也吻合，得到 Hermite 插值，用于计算矩阵函数。

插值多项式虽然唯一，但用它近似函数的效果取决于节点的选取。对 $f(x)=\frac1{1+25x^2}$ 在 $[-1,1]$ 上用等距节点插值，次数越高，区间两端的振荡反而越剧烈，插值多项式不收敛于 $f$，这称为 Runge 现象（Runge Phenomenon）；改用 Chebyshev 节点 $\cos\frac{(2k+1)\pi}{2n+2}$（$k=0,\dots,n$），节点向两端加密，插值多项式就一致收敛于 $f$。

![Runge 函数 1/(1+25x^2) 的 Lagrange 插值：左边用等距节点，次数升高时端点附近的振荡越来越大；右边用 Chebyshev 节点，插值多项式随次数升高收敛于原函数](./plots/lagrange-runge.py)

**例 9.4.3** 求首一二次多项式 $f$，使 $f$ 除以 $x-1$ 余 $1$，除以 $x-2$ 余 $2$。由余数定理 $f(1)=1$，$f(2)=2$，所以 $f(x)-x$ 是以 $1,2$ 为根的首一二次多项式：$f=x+(x-1)(x-2)=x^2-2x+2$。

## 9.5. 最大公因式与辗转相除法

**定义 9.5.1（最大公因式）** 设 $f,g\in \mathbb{F}[x]$。若 $d\in \mathbb{F}[x]$ 满足 $d\mid f$，$d\mid g$，且 $f,g$ 的任一公因式都整除 $d$，则称 $d$ 是 $f$ 与 $g$ 的一个**最大公因式**。

若 $d,d'$ 都是最大公因式，则 $d\mid d'$，$d'\mid d$，二者只差一个非零常数因子。$f,g$ 不全为零时，记 $(f,g)$ 为首项系数为 $1$ 的那个最大公因式；$(f,0)$ 是 $f$ 除以其首项系数，$(0,0)=0$。存在性由辗转相除法给出，它依据下面的引理。

**引理 9.5.1** 若 $f=qg+r$，则 $f,g$ 的公因式与 $g,r$ 的公因式相同，从而 $(f,g)=(g,r)$。

**证明** 由 $r=f-qg$ 与 $f=qg+r$ 及整除的组合性质。$\square$

**算法 9.5.1（辗转相除法）** 输入 $f,g\in \mathbb{F}[x]$，$g\neq0$。令 $r_{-1}=f$，$r_0=g$；对 $k=0,1,2,\dots$，只要 $r_k\neq0$，就用带余除法 $r_{k-1}=q_{k+1}r_k+r_{k+1}$。由于 $\deg r_0>\deg r_1>\deg r_2>\cdots$，过程在有限步后得到 $r_{s+1}=0$。由引理 9.5.1，

$$
(f,g)=(g,r_1)=(r_1,r_2)=\cdots=(r_{s-1},r_s)=(r_s,0),
$$

所以最后一个非零余式 $r_s$ 除以它的首项系数就是 $(f,g)$。

**例 9.5.1** 求 $f=x^4+x^3-x^2-2x+1$ 与 $g=x^3+2x^2-3$ 的最大公因式：

$$
\begin{aligned}
f&=(x-1)g+(x^2+x-2),\\
g&=(x+1)(x^2+x-2)+(x-1),\\
x^2+x-2&=(x+2)(x-1),
\end{aligned}
$$

所以 $(f,g)=x-1$。

辗转相除法只用 $\mathbb{F}$ 中的四则运算，所以最大公因式与数域的选取无关：$f,g\in\mathbb{Q}[x]$ 在 $\mathbb{Q}[x]$ 中与在 $\mathbb{C}[x]$ 中的最大公因式相同。这一点很重要：不知道多项式的根，也能判断两个多项式有没有公共根。

**定理 9.5.1（Bézout 等式）** 设 $f,g\in \mathbb{F}[x]$，则存在 $u,v\in \mathbb{F}[x]$ 使

$$
(f,g)=uf+vg.
$$

**证明** 在算法 9.5.1 中，$r_s=r_{s-2}-q_sr_{s-1}$，而 $r_{s-1}=r_{s-3}-q_{s-1}r_{s-2}$，……，自下而上逐次代入，就把 $r_s$ 写成 $f$ 与 $g$ 的组合，再除以 $r_s$ 的首项系数。$f=g=0$ 时显然。$\square$

**算法 9.5.2（扩展辗转相除法）** 在算法 9.5.1 中同时维护 $u_k,v_k$，使 $r_k=u_kf+v_kg$：$u_{-1}=1$，$v_{-1}=0$，$u_0=0$，$v_0=1$，每一步 $u_{k+1}=u_{k-1}-q_{k+1}u_k$，$v_{k+1}=v_{k-1}-q_{k+1}v_k$。最后 $r_s=u_sf+v_sg$。这与回代的结果相同，但不必保存全部商。

**例 9.5.2** 对例 9.5.1，由第二式与第一式，

$$
x-1=g-(x+1)(x^2+x-2)=g-(x+1)\big(f-(x-1)g\big)=-(x+1)f+x^2g.
$$

**例 9.5.3** 设 $f=x^4+2x^3-x^2-4x-2$，$g=x^4+x^3-x^2-2x-2$。$f=g+(x^3-2x)$，$g=(x+1)(x^3-2x)+(x^2-2)$，$x^3-2x=x(x^2-2)$，所以 $(f,g)=x^2-2$，且

$$
x^2-2=g-(x+1)(f-g)=-(x+1)f+(x+2)g.
$$

$u,v$ 不唯一：$u'=u+\frac gd$，$v'=v-\frac fd$（$d=(f,g)\neq0$）也满足 $u'f+v'g=d$。另外，$uf+vg=h$ 一般不能推出 $h$ 是最大公因式（例如 $1\cdot x+(-1)\cdot x=0$），但 $h=1$ 时可以，这就是下一节的互素判别法。用 1.3.3 的语言说，$\{uf+vg\mid u,v\in \mathbb{F}[x]\}$ 是 $\mathbb{F}[x]$ 的一个**理想**，Bézout 等式说它由 $(f,g)$ 生成：$\mathbb{F}[x]$ 的每个理想都由一个多项式生成。

## 9.6. 互素

**定义 9.6.1（互素）** 若 $(f,g)=1$，则称 $f$ 与 $g$ **互素**。

例如 $c_1\neq c_2$ 时 $x-c_1$ 与 $x-c_2$ 互素：$\frac{1}{c_2-c_1}\big((x-c_1)-(x-c_2)\big)=1$。

**定理 9.6.1** $f,g$ 互素，当且仅当存在 $u,v\in \mathbb{F}[x]$ 使 $uf+vg=1$。

**证明** 必要性即 Bézout 等式。充分性：若 $c\mid f$，$c\mid g$，则 $c\mid uf+vg=1$，$c$ 是非零常数，所以 $(f,g)=1$。$\square$

**命题 9.6.1** 设 $f,g,h,f_1,f_2\in \mathbb{F}[x]$。

1. 若 $f_1\mid g$，$f_2\mid g$，且 $(f_1,f_2)=1$，则 $f_1f_2\mid g$；
2. 若 $(f,g)=1$，$f\mid gh$，则 $f\mid h$；
3. 若 $d=(f,g)\neq0$，则 $\big(\frac fd,\frac gd\big)=1$；
4. 若 $t$ 是首一多项式，则 $(tf,tg)=t\,(f,g)$；
5. 若 $(f_1,g)=(f_2,g)=1$，则 $(f_1f_2,g)=1$。

**证明** 1：$g=f_1q_1=f_2q_2$，由 $uf_1+vf_2=1$，$g=ugf_1+vgf_2=uf_2q_2f_1+vf_1q_1f_2$，被 $f_1f_2$ 整除。2：由 $uf+vg=1$，$h=ufh+vgh$，两项都被 $f$ 整除。3：由 $d=uf+vg$ 两边除以 $d$ 得 $u\frac fd+v\frac gd=1$。4：由 $d=uf+vg$ 得 $td=u(tf)+v(tg)$，而 $td$ 是 $tf,tg$ 的首一公因式，被任一公因式整除，所以是最大公因式。5：把 $u_1f_1+v_1g=1$ 与 $u_2f_2+v_2g=1$ 相乘，得 $(u_1u_2)f_1f_2+(u_1f_1v_2+v_1u_2f_2+v_1v_2g)g=1$。$\square$

**例 9.6.1** 证明 $x^3-1\mid x^{3k}-1$。$x^3-1=(x-1)(x-\omega)(x-\omega^2)$，$\omega=\mathrm{e}^{2\pi\mathrm{i}/3}$，三个因式两两互素。$f=x^{3k}-1$ 满足 $f(1)=0$，$f(\omega)=\omega^{3k}-1=0$，$f(\omega^2)=0$，由余数定理每个因式都整除 $f$，由命题 9.6.1 的第 1 条，乘积整除 $f$。由整除与数域无关，这在 $\mathbb{Q}[x]$ 中也成立。

**例 9.6.2** 若 $(f,g)=1$，则对任意 $h$ 有 $(fh,g)=(h,g)$。记 $d=(fh,g)$，$d_1=(h,g)$。$d_1\mid h$，$d_1\mid g$，故 $d_1\mid fh$，$d_1\mid d$。反之 $(d,f)$ 整除 $f$ 与 $g$（因为 $d\mid g$），所以 $(d,f)=1$；由 $d\mid fh$ 与命题 9.6.1 的第 2 条，$d\mid h$，于是 $d\mid d_1$。二者都是首一的，故 $d=d_1$。

## 9.7. 不可约多项式与因式分解

**定义 9.7.1（不可约多项式）** 设 $f\in \mathbb{F}[x]$，$\deg f\ge1$。若不存在 $f_1,f_2\in \mathbb{F}[x]$，$\deg f_1\ge1$，$\deg f_2\ge1$，使 $f=f_1f_2$，则称 $f$ 是 $\mathbb{F}$ 上的**不可约多项式**；否则称 $f$ 在 $\mathbb{F}$ 上可约。

不可约多项式是多项式中的"素数"：它的因式只有非零常数 $c$ 和 $cf$。一次多项式总是不可约的。不可约性与数域有关：$x^2-2$ 在 $\mathbb{Q}$ 上不可约，在 $\mathbb{R}$ 上 $x^2-2=(x-\sqrt2)(x+\sqrt2)$。

**命题 9.7.1** 设 $p\in \mathbb{F}[x]$ 在 $\mathbb{F}$ 上不可约。

1. 对非零常数 $c$，$cp$ 也不可约；
2. 若 $\mathbb{F}\subseteq \mathbb{K}$ 都是数域，$p\in \mathbb{F}[x]$ 在 $\mathbb{K}$ 上不可约，则它在 $\mathbb{F}$ 上不可约；
3. 对任意 $g\in \mathbb{F}[x]$，或者 $(p,g)=1$，或者 $p\mid g$；
4. 若 $p\mid gh$，则 $p\mid g$ 或 $p\mid h$。

**证明** 1、2 由定义。3：$(p,g)$ 是 $p$ 的首一因式，只能是 $1$ 或 $p$ 除以其首项系数。4：若 $p\nmid g$，由 3 得 $(p,g)=1$，再由命题 9.6.1 的第 2 条得 $p\mid h$。$\square$

**定理 9.7.1（因式分解唯一性定理）** 设 $f\in \mathbb{F}[x]$，$\deg f\ge1$，则

1. $f$ 可以分解为 $\mathbb{F}$ 上有限个不可约多项式的乘积；
2. 若 $f=p_1p_2\cdots p_s=q_1q_2\cdots q_t$ 是两个这样的分解，则 $s=t$，且适当调整顺序后 $p_i=c_iq_i$，$c_i$ 为非零常数。

**证明** 存在性：对 $\deg f$ 归纳。$f$ 不可约则已完成；否则 $f=f_1f_2$，$1\le\deg f_i<\deg f$，对 $f_1,f_2$ 用归纳假设。唯一性：对 $s$ 归纳。$p_1\mid q_1\cdots q_t$，由命题 9.7.1 的第 4 条（推广到多个因式），$p_1$ 整除某个 $q_j$，不妨设 $j=1$；$q_1$ 不可约，所以 $q_1=c_1'p_1$。约去 $p_1$ 得 $p_2\cdots p_s=c_1'q_2\cdots q_t$，用归纳假设。$\square$

把每个不可约因式的首项系数提出来、相同的因式合并，得到 $f$ 的标准分解式

$$
f=c\,p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s},
$$

其中 $c$ 是 $f$ 的首项系数，$p_i$ 是互不相同的首一不可约多项式，$e_i\ge1$ 称为 $p_i$ 的重数。若 $f=c\prod p_i^{e_i}$，$g=c'\prod p_i^{f_i}$（$e_i,f_i\ge0$），则 $(f,g)=\prod p_i^{\min\{e_i,f_i\}}$。不过用标准分解式求最大公因式要先分解，而分解本身很难；辗转相除法则不需要分解。

定理 9.7.1 说明 $\mathbb{F}[x]$ 与 $\mathbb{Z}$ 一样是唯一分解的。用环论的语言（[1.3.3](/1.3.3)）：$p$ 不可约当且仅当它生成的理想 $(p)$ 是极大理想，当且仅当商环 $\mathbb{F}[x]/(p)$ 是域；例如 $\mathbb{R}[x]/(x^2+1)\cong\mathbb{C}$。剩下的问题是：给定 $f$，怎样判断它在 $\mathbb{F}$ 上是否不可约？答案强烈依赖于 $\mathbb{F}$。

## 9.8. 复数域、实数域与有理数域上的因式分解

### 9.8.1. 复系数多项式

**定理 9.8.1（代数基本定理）** 每个次数不小于 $1$ 的复系数多项式在 $\mathbb{C}$ 中至少有一个根。

这个定理已在 [第 6 章](/2.1.6) 中用来保证复矩阵有特征值。它的证明需要分析的工具（最简洁的证明用复变函数的 Liouville 定理），这里不给出。由余数定理和归纳法立即得到：

**推论 9.8.1** $\mathbb{C}[x]$ 中的不可约多项式恰为一次多项式。每个 $n$ 次复系数多项式可以分解为

$$
f=c(x-\lambda_1)^{n_1}(x-\lambda_2)^{n_2}\cdots(x-\lambda_s)^{n_s},\qquad n_1+\cdots+n_s=n,
$$

$\lambda_i$ 互不相同，所以 $f$ 在 $\mathbb{C}$ 中恰有 $n$ 个根（按重数计）。

**命题 9.8.1** 设 $f\in \mathbb{F}[x]$，$\deg f\ge1$。$f$ 在 $\mathbb{C}$ 中没有重根，当且仅当 $(f,f')=1$。

**证明** 若 $a\in\mathbb{C}$ 是重根，由命题 9.4.1 的第 3 条，$x-a$ 是 $f$ 与 $f'$ 的公因式，$(f,f')\neq1$。反之若 $d=(f,f')$ 次数 $\ge1$，由代数基本定理 $d$ 有复根 $a$，则 $f(a)=f'(a)=0$，$a$ 是重根。$\square$

由于最大公因式与数域无关，判断有无重根只需在 $\mathbb{F}[x]$ 中对 $f$ 与 $f'$ 做辗转相除，不必求根。[第 10 章](/2.1.10) 用这一点判断矩阵能否对角化：矩阵可对角化当且仅当它的极小多项式没有重根。

### 9.8.2. 实系数多项式

**引理 9.8.1** 设 $f\in\mathbb{R}[x]$，$z\in\mathbb{C}$。若 $f(z)=0$，则 $f(\bar z)=0$，且 $z$ 与 $\bar z$ 的重数相同。

**证明** $f$ 的系数是实数，对 $f(z)=\sum a_kz^k=0$ 取共轭得 $f(\bar z)=\sum a_k\bar z^k=0$。重数：对 $\deg f$ 归纳。设 $z\notin\mathbb{R}$ 是根，$g=(x-z)(x-\bar z)$ 是实系数多项式，两个一次因式互素且都整除 $f$，所以 $g\mid f$；带余除法在 $\mathbb{R}[x]$ 中进行，商 $h=f/g$ 仍是实系数的。$z$ 与 $\bar z$ 在 $f$ 中的重数都比在 $h$ 中的重数多 $1$，对 $h$ 用归纳假设即可。$\square$

若 $z=a+b\mathrm{i}$，$b\neq0$，则

$$
(x-z)(x-\bar z)=x^2-(z+\bar z)x+z\bar z=x^2-2ax+(a^2+b^2)
$$

是实系数二次多项式，判别式 $-4b^2<0$，在 $\mathbb{R}$ 上不可约。于是由推论 9.8.1：

**定理 9.8.2** $\mathbb{R}[x]$ 中的不可约多项式恰为一次多项式，以及判别式小于零的二次多项式 $ax^2+bx+c$（$b^2-4ac<0$）。每个实系数多项式可以分解为

$$
f=c\prod_{i=1}^s(x-a_i)^{n_i}\prod_{j=1}^t(x^2+p_jx+q_j)^{m_j},\qquad p_j^2-4q_j<0.
$$

**证明** 对 $\deg f$ 归纳。$f$ 若有实根 $a$，则分出 $x-a$；否则取一个复根 $z\notin\mathbb{R}$，由引理 9.8.1，$\bar z$ 也是根，$(x-z)(x-\bar z)$ 整除 $f$（在 $\mathbb{C}[x]$ 中，二者互素），而它是实多项式，由整除与数域无关，在 $\mathbb{R}[x]$ 中也整除 $f$。$\square$

特别地，奇数次实系数多项式必有实根，所以奇数阶实矩阵必有实特征值。

**例 9.8.1** $x^4+2$ 在 $\mathbb{R}$ 上可约吗？它的复根是 $\sqrt[4]2\,\mathrm{e}^{\mathrm{i}(2k+1)\pi/4}$（$k=0,1,2,3$），两两共轭。把共轭的一对合并：$\mathrm{e}^{\mathrm{i}\pi/4}$ 与 $\mathrm{e}^{-\mathrm{i}\pi/4}$ 给出 $x^2-2\sqrt[4]2\cos\frac\pi4\,x+\sqrt2=x^2-2^{3/4}x+\sqrt2$，另一对给出 $x^2+2^{3/4}x+\sqrt2$，所以

$$
x^4+2=\big(x^2-2^{3/4}x+\sqrt2\big)\big(x^2+2^{3/4}x+\sqrt2\big).
$$

引言中 $\lambda^4+1$ 的实分解也是这样得到的。可见次数 $\ge3$ 的实多项式总是可约的。

### 9.8.3. 有理系数多项式

$\mathbb{Q}[x]$ 中的情况完全不同：下面将看到，每个次数都有不可约多项式。$f\in\mathbb{Q}[x]$ 乘以系数分母的公倍数后成为整系数多项式，不改变它的根和可约性，所以只需讨论整系数多项式。

**定理 9.8.3（有理根定理）** 设 $f=a_nx^n+\cdots+a_1x+a_0\in\mathbb{Z}[x]$，$a_n\neq0$。若既约分数 $\frac rs$（$r,s\in\mathbb{Z}$ 互素）是 $f$ 的根，则 $r\mid a_0$，$s\mid a_n$。

**证明** 由 $f(\frac rs)=0$，两边乘以 $s^n$ 得 $a_nr^n+a_{n-1}r^{n-1}s+\cdots+a_1rs^{n-1}+a_0s^n=0$。除第一项外各项都被 $s$ 整除，所以 $s\mid a_nr^n$；$s$ 与 $r$ 互素，故 $s\mid a_n$。同理 $r\mid a_0s^n$，$r\mid a_0$。$\square$

于是求有理根只需有限次验证。例如 $2x^3-3x^2-3x+2$ 的有理根只可能是 $\pm1,\pm2,\pm\frac12$，逐个代入（用综合除法）得到根 $-1,\frac12,2$，所以 $2x^3-3x^2-3x+2=(x+1)(2x-1)(x-2)$。又如 $x^5-12x^3+36x+12$ 的有理根只可能是 $\pm1,\pm2,\pm3,\pm4,\pm6,\pm12$，验证可知都不是根，所以它没有有理根。

二次或三次多项式若可约，必有一次因式，从而有根；所以它在 $\mathbb{F}$ 上不可约当且仅当在 $\mathbb{F}$ 中没有根。例如 $x^3-3x-1$ 的有理根只可能是 $\pm1$，而 $f(1)=-3$，$f(-1)=1$，所以它在 $\mathbb{Q}$ 上不可约。但对四次及以上的多项式，没有有理根推不出不可约：$(x^2-2)^2\in\mathbb{Q}[x]$ 没有有理根，却显然可约。为此需要下面的工具。

**定义 9.8.1（本原多项式）** 若整系数多项式 $g$ 的各项系数的最大公因数为 $\pm1$，则称 $g$ 是**本原多项式**。

每个非零有理系数多项式都可以写成 $f=rg$，$r\in\mathbb{Q}$，$g$ 是本原多项式：先乘以分母的公倍数化为整系数多项式，再提出系数的最大公因数。这种写法在相差符号的意义下唯一（若 $r_1g_1=r_2g_2$，则 $r_1=\pm r_2$，$g_1=\pm g_2$）。例如 $4x^3+3x+2$ 是本原多项式，$8x^3+6x+4=2(4x^3+3x+2)$ 不是。

**定理 9.8.4（Gauss 引理）** 两个本原多项式的乘积仍是本原多项式。

**证明** 设 $f=\sum a_ix^i$，$g=\sum b_jx^j$ 本原，若 $h=fg$ 不是本原的，则有素数 $p$ 整除 $h$ 的所有系数。$f$ 本原，$p$ 不整除 $f$ 的全部系数，设 $a_i$ 是第一个不被 $p$ 整除的系数（$p\mid a_0,\dots,a_{i-1}$）；同样设 $b_j$ 是 $g$ 的第一个不被 $p$ 整除的系数。$h$ 的 $x^{i+j}$ 项系数为

$$
c_{i+j}=a_ib_j+(a_{i-1}b_{j+1}+a_{i-2}b_{j+2}+\cdots)+(a_{i+1}b_{j-1}+a_{i+2}b_{j-2}+\cdots),
$$

括号中的每一项都含有 $a_0,\dots,a_{i-1}$ 或 $b_0,\dots,b_{j-1}$ 之一，被 $p$ 整除；又 $p\mid c_{i+j}$，所以 $p\mid a_ib_j$，从而 $p\mid a_i$ 或 $p\mid b_j$，矛盾。$\square$

**推论 9.8.2** 非零整系数多项式 $f$ 能在 $\mathbb{Q}[x]$ 中分解为两个次数较低的多项式之积，当且仅当它能在 $\mathbb{Z}[x]$ 中分解为两个次数较低的整系数多项式之积。

**证明** 充分性显然。必要性：设 $f=gh$，$g,h\in\mathbb{Q}[x]$，$\deg g,\deg h<\deg f$。写 $f=r_ff_1$，$g=r_gg_1$，$h=r_hh_1$，$f_1,g_1,h_1$ 本原，$r_f\in\mathbb{Z}$（$f$ 是整系数的）。则 $r_ff_1=r_gr_h\,g_1h_1$，由 Gauss 引理 $g_1h_1$ 本原，由写法的唯一性 $r_gr_h=\pm r_f\in\mathbb{Z}$，于是 $f=(\pm r_fg_1)h_1$ 是整系数分解。$\square$

**定理 9.8.5（Eisenstein 判别法）** 设 $f=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0\in\mathbb{Z}[x]$。若存在素数 $p$ 使

1. $p\nmid a_n$；
2. $p\mid a_{n-1},\dots,a_1,a_0$；
3. $p^2\nmid a_0$，

则 $f$ 在 $\mathbb{Q}$ 上不可约。

**证明** 反设 $f$ 在 $\mathbb{Q}$ 上可约，由推论 9.8.2，$f=(b_lx^l+\cdots+b_0)(c_mx^m+\cdots+c_0)$，$b_i,c_j\in\mathbb{Z}$，$l,m\ge1$，$l+m=n$。$a_0=b_0c_0$，由 $p\mid a_0$，$p^2\nmid a_0$，$p$ 恰整除 $b_0,c_0$ 中的一个，不妨设 $p\mid b_0$，$p\nmid c_0$。由 $a_n=b_lc_m$ 与 $p\nmid a_n$ 得 $p\nmid b_l$。设 $b_k$ 是第一个不被 $p$ 整除的 $b$（$0<k\le l<n$），则 $a_k=b_kc_0+b_{k-1}c_1+\cdots+b_0c_k$，右边除 $b_kc_0$ 外都被 $p$ 整除，而 $p\nmid b_kc_0$，所以 $p\nmid a_k$，与条件 2 矛盾。$\square$

**例 9.8.2**

- 对任意 $n\ge1$，$x^n+2$ 在 $\mathbb{Q}$ 上不可约（取 $p=2$）。所以 $\mathbb{Q}[x]$ 中有任意次数的不可约多项式，与 $\mathbb{C}[x]$、$\mathbb{R}[x]$ 截然不同。
- 前面的 $x^5-12x^3+36x+12$ 取 $p=3$：$3\nmid1$，$3$ 整除 $-12,36,12$，$9\nmid12$，所以它在 $\mathbb{Q}$ 上不可约。没有有理根只说明它没有一次因式，Eisenstein 判别法进一步排除了二次因式。
- 有时需要先换元。设 $p$ 是素数，$\Phi_p(x)=x^{p-1}+x^{p-2}+\cdots+x+1=\frac{x^p-1}{x-1}$（它的根是 $p$ 次单位根中除 $1$ 外的 $p-1$ 个）。令 $x=y+1$，
  $$
  \Phi_p(y+1)=\frac{(y+1)^p-1}{y}=y^{p-1}+\binom p1y^{p-2}+\cdots+\binom p{p-2}y+\binom p{p-1},
  $$
  $p$ 整除 $\binom pi$（$1\le i\le p-1$），$p^2\nmid\binom p{p-1}=p$，所以 $\Phi_p(y+1)$ 不可约，从而 $\Phi_p(x)$ 在 $\mathbb{Q}$ 上不可约（$f(x)\mapsto f(y+1)$ 保持乘法与次数）。

三个数域上的不可约多项式对比如下：

| 数域 | 不可约多项式 | 判别方法 |
|---|---|---|
| $\mathbb{C}$ | 恰为一次多项式 | 代数基本定理 |
| $\mathbb{R}$ | 一次多项式；判别式为负的二次多项式 | 复根共轭成对 |
| $\mathbb{Q}$ | 任意次数都有 | 有理根定理（只排除一次因式）、Gauss 引理、Eisenstein 判别法 |

## 9.9. 根与系数的关系

**定理 9.9.1（Vieta 定理）** 设 $f=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0\in \mathbb{F}[x]$，$a_n\neq0$，在 $\mathbb{C}$ 中的 $n$ 个根（按重数计）为 $x_1,\dots,x_n$，则

$$
\begin{aligned}
x_1+x_2+\cdots+x_n&=-\frac{a_{n-1}}{a_n},\\
\sum_{1\le i<j\le n}x_ix_j&=\frac{a_{n-2}}{a_n},\\
&\ \ \vdots\\
\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}x_{i_2}\cdots x_{i_k}&=(-1)^k\frac{a_{n-k}}{a_n},\\
&\ \ \vdots\\
x_1x_2\cdots x_n&=(-1)^n\frac{a_0}{a_n}.
\end{aligned}
$$

**证明** 由推论 9.8.1，$f=a_n(x-x_1)\cdots(x-x_n)$，展开右边并比较 $x^{n-k}$ 的系数。$\square$

左边是根的初等对称多项式。对特征多项式 $\det(\lambda I-A)$ 应用 Vieta 定理，就得到 [第 6 章](/2.1.6) 中特征值之和等于迹、之积等于行列式。根的任何对称多项式都能写成初等对称多项式的多项式（对称多项式基本定理），因而能用系数直接表示，不必求根。最重要的例子是判别式。

**定义 9.9.1（判别式）** 设 $f$ 是首一多项式，在 $\mathbb{C}$ 中的根为 $x_1,\dots,x_n$，称

$$
D(f)=\prod_{1\le i<j\le n}(x_i-x_j)^2
$$

为 $f$ 的**判别式**。

$D(f)$ 是根的对称多项式，所以是系数的多项式；$D(f)=0$ 当且仅当 $f$ 有重根（与命题 9.8.1 一致）。$D(f)$ 是 Vandermonde 行列式的平方：令 $V=[x_j^{i-1}]_{n\times n}$，则 $D(f)=(\det V)^2=\det(VV^{\mathsf T})$，而 $VV^{\mathsf T}$ 的 $(i,j)$ 元是幂和 $s_{i+j-2}=\sum_kx_k^{i+j-2}$，幂和可以用 Vieta 定理递推。

**例 9.9.1** 对二次多项式 $x^2+bx+c$，$x_1+x_2=-b$，$x_1x_2=c$，$D=(x_1-x_2)^2=(x_1+x_2)^2-4x_1x_2=b^2-4c$。对一般的 $ax^2+bx+c$，$(x_1-x_2)^2=\frac{b^2-4ac}{a^2}$。实系数时：$D>0$ 有两个不同的实根，$D=0$ 有二重实根，$D<0$ 有一对共轭复根。

**例 9.9.2（三次多项式的判别式）** 设 $f=x^3+qx+r\in\mathbb{R}[x]$（一般的三次多项式经平移 $x\mapsto x-\frac{a_2}3$ 都可化为这种形式），根为 $x_1,x_2,x_3$。由 Vieta 定理，$x_1+x_2+x_3=0$，$\sum x_ix_j=q$，$x_1x_2x_3=-r$。幂和为 $s_0=3$，$s_1=0$，$s_2=s_1^2-2q=-2q$；由 $x_k^3=-qx_k-r$ 得 $s_3=-qs_1-3r=-3r$，$s_4=-qs_2-rs_1=2q^2$。所以

$$
D=\det\begin{bmatrix}3&0&-2q\\0&-2q&-3r\\-2q&-3r&2q^2\end{bmatrix}=-4q^3-27r^2.
$$

实根个数由 $D$ 的符号决定：

- 若 $f$ 有一个实根 $c$ 和一对共轭复根 $z,\bar z$（$z=a+b\mathrm{i}$，$b\neq0$），则 $(c-z)(c-\bar z)=|c-z|^2$，$z-\bar z=2b\mathrm{i}$，所以 $D=|c-z|^4(2b\mathrm{i})^2=-4b^2|c-z|^4<0$；
- 若三个根都是实数，则 $D\ge0$，且 $D=0$ 当且仅当有重根。

由于实三次多项式的复根成对出现，只有这两种情形，所以：$D>0$ 时有三个不同的实根，$D=0$ 时有重根（都是实根），$D<0$ 时有一个实根和一对共轭复根。例如 $x^3+9x+r$ 的判别式 $-4\cdot9^3-27r^2<0$ 对任意实数 $r$ 成立，所以它总是恰有一个实根（这也可以由 $f'=3x^2+9>0$，$f$ 严格递增看出）；$x^3-3x-1$ 的判别式 $108-27=81>0$，有三个不同的实根（而由 §9.8.3，它们都是无理数）。

二次、三次、四次方程都有求根公式，但 Abel 与 Galois 证明了五次及以上的一般方程没有根式解。因此矩阵的特征值不是先求特征多项式再套公式算出的，而是用迭代算法（如 QR 算法）直接计算；反过来，数值软件求多项式的根时，正是计算它的**友矩阵**的特征值（例如 `numpy.roots`）。

## 小结

本章的两条主线：复数是使每个多项式完全分解的数域，复数的运算可以用 $2\times2$ 实矩阵实现；$\mathbb{F}[x]$ 与整数一样有带余除法、最大公因式与唯一分解，而且所有基本运算都有标准化的算法。

| 主题 | 核心结论 | 算法与代价 |
|---|---|---|
| 复数 | $z=a+b\mathrm{i}=r\mathrm{e}^{\mathrm{i}\theta}$；乘法 = 旋转与伸缩；$z\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ 是单的环同态 | 用指数形式计算 $z^n$ |
| 幂与方根 | $z^{q/p}$ 有 $p$ 个值；$n$ 次单位根 $\mathrm{e}^{2k\pi\mathrm{i}/n}$，和为零 | — |
| 复矩阵 | $A^{\mathsf H}=\bar A^{\mathsf T}$，$\boldsymbol{x}^{\mathsf H}\boldsymbol{x}>0$；复向量空间 $\dim_{\mathbb{R}}V=2\dim_{\mathbb{C}}V$ | — |
| 带余除法 | $f=qg+r$ 唯一；整除、最大公因式与数域无关 | 长除法 |
| 余数定理 | $x-a$ 除 $f$ 余 $f(a)$；$a$ 为重根 ⇔ $f(a)=f'(a)=0$ | 综合除法（Horner）：$n$ 次乘法；按 $x-a$ 展开：$\frac{n(n+1)}2$ 次 |
| 插值 | 次数 $\le n$、过 $n+1$ 点的多项式唯一 | Lagrange 公式 $O(n^2)$；Vandermonde 方程组 $O(n^3)$ |
| 最大公因式 | $(f,g)=uf+vg$（Bézout）；互素 ⇔ $uf+vg=1$ | 辗转相除法、扩展辗转相除法 |
| 因式分解 | 不可约多项式是"素数"；分解存在且唯一；无重根 ⇔ $(f,f')=1$ | 不需要求根即可判断重根 |
| $\mathbb{C},\mathbb{R},\mathbb{Q}$ | 代数基本定理；实系数复根共轭成对；有理根定理、Gauss 引理、Eisenstein 判别法 | 有理根：有限次验证 |
| 根与系数 | Vieta 定理；判别式 $\prod_{i<j}(x_i-x_j)^2$；$x^3+qx+r$：$D=-4q^3-27r^2$ | 幂和递推 + Vandermonde |
