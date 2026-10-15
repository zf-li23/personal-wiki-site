---
title: 线性空间与线性映射
---

前七章都在 $\mathbb{R}^n$ 中工作：向量是数组，线性映射就是矩阵。但"线性"的现象远不止于此：齐次线性微分方程的解可以相加、数乘；多项式、矩阵、函数都可以做线性组合；求导、转置、取迹、在若干点取值都满足叠加原理。本章把 $\mathbb{R}^n$ 的概念抽象为数域上的线性空间与线性映射，使前面的全部理论能够处理这些对象。

本章是全课程的转折点。§8.1–§8.3 把子空间、线性相关、基与维数搬到一般的线性空间上（推理与 [第 3 章](/2.1.3) 相同，只是不再依赖矩阵的具体形式），并新增子空间的交、和与直和。§8.4–§8.7 是本章的核心：取定基以后，抽象的向量变成坐标，线性映射变成矩阵，复合变成**矩阵乘法**，核与像变成**零空间**与**列空间**；换一组基，线性映射的矩阵做相抵变换，线性变换的矩阵做相似变换。于是前面关于矩阵的结论都成为线性映射本身的性质，而"化简矩阵"就成为"为线性映射选择一组好的基"。后面几章正是沿这条路走下去的：[第 10 章](/2.1.10) 为线性变换寻找使矩阵最简单的基（Jordan 标准形），[第 12 章](/2.1.12) 要求这组基是标准正交的，[第 13 章](/2.1.13) 研究双线性型在基变换下的合同。§8.8 介绍对偶空间，它解释了转置 $A^{\mathsf T}$ 的意义，也是第 13 章双线性型与张量的起点。本章的抽象定义与离散数学中域上的**向量空间**（[1.3.3](/1.3.3)）一致，只是这里的数取自数域。

记号约定：从本章起，一般数域记作 $\mathbb{F}$；抽象线性空间用斜体大写 $V, W$，其元素（包括零向量 $0$）用普通斜体 $v, w$，不加粗；只有 $\mathbb{F}^n$ 中的列向量用粗体，包括抽象向量在一组基下的坐标（如 $\hat{\boldsymbol{x}}\in\mathbb{F}^n$）。粗体与否本身提示对象是具体的数组还是抽象的向量。

## 8.1. 数域与线性空间

**定义 8.1.1（数域）** 设 $\mathbb{F}$ 是复数集 $\mathbb{C}$ 的子集，至少含有一个非零复数，且对复数的加、减、乘、除（除数非零）四则运算封闭，则称 $\mathbb{F}$ 是一个**数域**。

$\mathbb{F}$ 含非零数 $a$，所以含 $a-a=0$ 与 $a/a=1$，从而含全体有理数：任何数域都包含 $\mathbb{Q}$。常见的数域有有理数域 $\mathbb{Q}$、实数域 $\mathbb{R}$、复数域 $\mathbb{C}$；自然数集 $\mathbb{N}$、整数集 $\mathbb{Z}$ 不是数域（不对减法或除法封闭）。$\mathbb{Q}(\sqrt2)=\{a+b\sqrt2\mid a,b\in\mathbb{Q}\}$ 也是数域，更多例子见 [第 9 章](/2.1.9)。Gauss 消元只用到四则运算，所以数域 $\mathbb{F}$ 上的线性方程组若有解，则有 $\mathbb{F}$ 中的解；矩阵的秩、可逆性等也不因把 $\mathbb{F}$ 看作更大的数域而改变。

**定义 8.1.2（线性空间）** 给定非空集合 $V$ 和数域 $\mathbb{F}$。若 $V$ 上定义了加法（对任意 $a,b\in V$，有 $V$ 中唯一的元素 $a+b$ 与之对应）与数乘（对任意 $a\in V$，$k\in \mathbb{F}$，有 $V$ 中唯一的元素 $ka$ 与之对应），且对任意 $a,b,c\in V$，$k,\ell\in \mathbb{F}$ 满足以下八条运算法则，则称 $V$ 是 $\mathbb{F}$ 上的**线性空间**（或向量空间），其中的元素称为向量：

1. 加法结合律：$(a+b)+c=a+(b+c)$；
2. 加法交换律：$a+b=b+a$；
3. 零元：存在 $0\in V$，使对任意 $a$ 有 $a+0=a$，$0$ 称为零向量；
4. 负元：对任意 $a$，存在 $b\in V$ 使 $a+b=0$，$b$ 称为 $a$ 的负向量，记作 $-a$；
5. 单位数：$1a=a$；
6. 数乘结合律：$(k\ell)a=k(\ell a)$；
7. 数乘对数的分配律：$(k+\ell)a=ka+\ell a$；
8. 数乘对向量的分配律：$k(a+b)=ka+kb$。

用代数系统的语言说，前四条就是 $(V,+)$ 是交换群。减法定义为 $a-b=a+(-b)$。

**命题 8.1.1** 在线性空间中：

1. 零向量唯一；
2. 每个向量的负向量唯一；
3. 加法消去律：由 $a+b=a+c$ 可推出 $b=c$；
4. 移项：由 $a+b=c$ 可推出 $a=c-b$；
5. $0a=0$，$(-1)a=-a$，$k0=0$；
6. 约系数：由 $ka=b$，$k\neq0$ 可推出 $a=\frac1kb$。

**证明** 1：若 $0,\tilde{0}$ 都是零向量，则 $\tilde{0}=\tilde{0}+0=0$。2：若 $b,c$ 都是 $a$ 的负向量，则 $b=b+(a+c)=(b+a)+c=c$。3、4：两边加上 $-a$ 或 $-b$。5：$0a=(0+0)a=0a+0a$，由消去律得 $0a=0$；$(-1)a+a=0a=0$，故 $(-1)a=-a$；$k0+ka=k(0+a)=ka$，由消去律得 $k0=0$。6：$a=(\frac1kk)a=\frac1k(ka)=\frac1kb$。$\square$

常见的线性空间（加法与数乘都是通常的运算）：

| 空间 | 元素 | 说明 |
|---|---|---|
| $\mathbb{F}^m$ | $m$ 维有序数组 | 数组向量空间，运算同 $\mathbb{R}^m$ |
| $\mathbb{F}^{m\times n}$ | $m\times n$ 矩阵 | 矩阵空间 |
| 函数空间 | 定义域为 $D$ 的实值函数 | $(f+g)(x)=f(x)+g(x)$，$(kf)(x)=kf(x)$ |
| $C(D)$ | $D$ 上的连续函数 | 函数空间的子空间 |
| $C^\infty(D)$ | $D$ 上的无穷次可微函数（光滑函数） | $C(D)$ 的子空间 |
| $\mathbb{F}[x]$ | 系数在 $\mathbb{F}$ 中的多项式（含零多项式） | 多项式空间；作为环就是**多项式环** |
| $\mathbb{F}[x]_n$ | 次数小于 $n$ 的多项式（含零多项式） | $\mathbb{F}[x]$ 的子空间 |
| $\mathbb{C}$ | 复数 | 既是 $\mathbb{C}$ 上的、也是 $\mathbb{R}$ 上的线性空间 |
| $\mathbb{R}$ | 实数 | 既是 $\mathbb{R}$ 上的、也是 $\mathbb{Q}$ 上的线性空间 |
| $\operatorname{Hom}(U,V)$ | $U$ 到 $V$ 的线性映射 | 见 §8.4 |

后两行说明：同一个集合在不同数域上是不同的线性空间，维数也可能不同（§8.3）。

## 8.2. 子空间的交、和与直和

**定义 8.2.1（子空间）** 设 $V$ 是数域 $\mathbb{F}$ 上的线性空间，$M$ 是 $V$ 的非空子集。若 $M$ 关于 $V$ 的加法和数乘也构成线性空间，则称 $M$ 是 $V$ 的（线性）**子空间**。

**命题 8.2.1** 线性空间 $V$ 的非空子集 $M$ 是子空间，当且仅当 $M$ 对加法和数乘封闭。

**证明** 必要性显然。充分性：八条法则中除零元与负元外都对 $V$ 的元素成立，自然对 $M$ 成立；而任取 $a\in M$，有 $0=0a\in M$，$-a=(-1)a\in M$。$\square$

例如矩阵 $A\in \mathbb{F}^{m\times n}$ 的列空间 $\mathcal{R}(A)$ 是 $\mathbb{F}^m$ 的子空间，零空间 $\mathcal{N}(A)$ 是 $\mathbb{F}^n$ 的子空间；$n$ 阶上三角矩阵的全体、对称矩阵的全体都是 $\mathbb{F}^{n\times n}$ 的子空间；$\mathbb{F}[x]_n$ 是 $\mathbb{F}[x]$ 的子空间。

**定义 8.2.2（子空间的交与和）** 设 $M_1,M_2$ 是线性空间 $V$ 的两个子空间。集合 $M_1\cap M_2=\{x\mid x\in M_1,\ x\in M_2\}$ 称为 $M_1$ 与 $M_2$ 的交；集合 $M_1+M_2=\{m_1+m_2\mid m_1\in M_1,\ m_2\in M_2\}$ 称为 $M_1$ 与 $M_2$ 的和，即**子空间的和**。

由命题 8.2.1 容易验证 $M_1\cap M_2$ 与 $M_1+M_2$ 都是子空间，且 $M_1+M_2$ 是同时包含 $M_1,M_2$ 的最小子空间。并集 $M_1\cup M_2$ 一般不是子空间：$\mathbb{R}^2$ 中两条不同的过原点直线之并，对加法不封闭。用矩阵写，设 $A\in \mathbb{F}^{m\times n}$，$B\in \mathbb{F}^{m\times p}$，$C\in \mathbb{F}^{q\times n}$，则

$$
\mathcal{R}(A)+\mathcal{R}(B)=\mathcal{R}\big([A\ B]\big),\qquad \mathcal{N}(A)\cap\mathcal{N}(C)=\mathcal{N}\left(\begin{bmatrix}A\\C\end{bmatrix}\right).
$$

**定义 8.2.3（直和）** 设 $M_1,M_2$ 是线性空间 $V$ 的子空间，$M=M_1+M_2$。若 $M$ 中每个向量 $m$ 的分解式 $m=m_1+m_2$（$m_1\in M_1$，$m_2\in M_2$）都唯一，则称 $M$ 为 $M_1$ 与 $M_2$ 的**直和**，记作 $M=M_1\oplus M_2$。

**定理 8.2.1** 对线性空间 $V$ 的两个子空间 $M_1,M_2$，以下叙述等价：

1. $M_1+M_2$ 是直和；
2. 零向量的分解式唯一：由 $0=m_1+m_2$，$m_i\in M_i$，可推出 $m_1=m_2=0$；
3. $M_1\cap M_2=\{0\}$。

**证明**（轮转证法）$1\Rightarrow2$：显然。$2\Rightarrow3$：对 $m\in M_1\cap M_2$，$0=m+(-m)$，其中 $m\in M_1$，$-m\in M_2$，故 $m=0$。$3\Rightarrow1$：若 $m=m_1+m_2=m_1'+m_2'$，则 $m_1-m_1'=m_2'-m_2\in M_1\cap M_2=\{0\}$。$\square$

**例 8.2.1** 设 $\mathcal{U},\mathcal{L}$ 分别是 $n$ 阶上三角、下三角矩阵的全体，$\mathcal{S},\mathcal{K}$ 分别是 $n$ 阶**对称矩阵**、**反对称矩阵**的全体，它们都是 $\mathbb{F}^{n\times n}$ 的子空间。$\mathcal{U}\cap\mathcal{L}$ 是对角矩阵的全体，$\mathcal{U}+\mathcal{L}=\mathbb{F}^{n\times n}$，但这个和不是直和。任意方阵唯一地分解为 $A=\frac12(A+A^{\mathsf T})+\frac12(A-A^{\mathsf T})$，且 $\mathcal{S}\cap\mathcal{K}=\{O\}$，所以 $\mathbb{F}^{n\times n}=\mathcal{S}\oplus\mathcal{K}$。

[第 4 章](/2.1.4) 的 $\mathbb{R}^n=M\oplus M^\perp$ 是直和的另一个例子。多个子空间的直和与线性变换下的空间分解见 [第 10 章](/2.1.10)。

## 8.3. 线性相关性、基与维数

### 8.3.1. 线性组合与线性相关

**定义 8.3.1（线性表示）** 设 $V$ 是数域 $\mathbb{F}$ 上的线性空间，$a_1,\dots,a_n\in V$，$k_1,\dots,k_n\in \mathbb{F}$，称 $k_1a_1+\cdots+k_na_n$ 是 $a_1,\dots,a_n$ 的一个**线性组合**。若向量 $b$ 等于 $a_1,\dots,a_n$ 的某个线性组合，则称 $b$ 可以被 $a_1,\dots,a_n$ 线性表示；若向量组 $b_1,\dots,b_m$ 中每个向量都可以被 $a_1,\dots,a_n$ 线性表示，则称前者可以被后者线性表示；两个向量组可以互相线性表示时，称二者线性等价。

仿照矩阵与向量的乘法，引入形式记号

$$
k_1a_1+\cdots+k_na_n=(a_1,\dots,a_n)\begin{bmatrix}k_1\\\vdots\\k_n\end{bmatrix},\qquad (b_1,\dots,b_m)=(a_1,\dots,a_n)\begin{bmatrix}k_{11}&\cdots&k_{1m}\\\vdots&&\vdots\\k_{n1}&\cdots&k_{nm}\end{bmatrix}.
$$

这里 $(a_1,\dots,a_n)$ 不是真正的矩阵（$a_i$ 可以是多项式或函数），但它对矩阵的乘法满足分配律与结合律：$(a_1,\dots,a_n)(K\boldsymbol{x})=\big((a_1,\dots,a_n)K\big)\boldsymbol{x}$，$(a_1,\dots,a_n)(KL)=\big((a_1,\dots,a_n)K\big)L$，直接展开即可验证。本章的计算都借助这一记号。

**定义 8.3.2（线性生成与线性相关）** 向量组 $a_1,\dots,a_n$ 的线性组合的全体构成 $V$ 的子空间，称为由该向量组**线性生成**的子空间，记作 $\operatorname{span}(a_1,\dots,a_n)$。若存在不全为零的 $k_1,\dots,k_n\in \mathbb{F}$ 使 $k_1a_1+\cdots+k_na_n=0$，则称向量组**线性相关**；若由 $k_1a_1+\cdots+k_na_n=0$ 只能推出 $k_1=\cdots=k_n=0$，则称向量组**线性无关**。

用形式记号，线性无关就是：$(a_1,\dots,a_n)\boldsymbol{k}=0\Rightarrow\boldsymbol{k}=\boldsymbol{0}$。由此，若向量组线性无关，则用它线性表示一个向量的方式唯一。

**命题 8.3.1** 设 $a_1,\dots,a_s$ 线性无关，则对任意向量 $b$：$a_1,\dots,a_s,b$ 线性相关，当且仅当 $b$ 可以被 $a_1,\dots,a_s$ 线性表示。

**证明** 充分性显然。必要性：设 $k_1a_1+\cdots+k_sa_s+kb=0$，系数不全为零。若 $k=0$，则与 $a_i$ 线性无关矛盾；故 $k\neq0$，$b=-\frac1k(k_1a_1+\cdots+k_sa_s)$。$\square$

据此，从一个向量组的第一个非零向量开始，依次检查每个向量能否被已选出的向量线性表示，不能就选入，这样的筛选法得到一个线性无关、且能线性表示整个向量组的部分组。

**引理 8.3.1** 若向量组 $b_1,\dots,b_t$ 可以被 $a_1,\dots,a_s$ 线性表示，且 $t>s$，则 $b_1,\dots,b_t$ 线性相关。

**证明** 设 $(b_1,\dots,b_t)=(a_1,\dots,a_s)K$，$K$ 是 $s\times t$ 矩阵。齐次方程组 $K\boldsymbol{k}=\boldsymbol{0}$ 的方程个数少于未知数个数，有非零解 $\boldsymbol{k}$，于是 $(b_1,\dots,b_t)\boldsymbol{k}=(a_1,\dots,a_s)(K\boldsymbol{k})=0$。$\square$

引理 8.3.1 把一般线性空间的问题归结为数域上的齐次线性方程组，这是本章反复使用的手法。由它立即得到：两个线性等价且各自线性无关的向量组所含向量个数相同。

**定义 8.3.3（极大线性无关部分组与秩）** 向量组 $S:a_1,\dots,a_s$ 的部分组 $a_{i_1},\dots,a_{i_r}$ 若线性无关，且 $S$ 可以被它线性表示，则称它是 $S$ 的一个**极大线性无关部分组**。$S$ 的任意两个极大线性无关部分组线性等价，所以含有相同个数的向量，这个数称为向量组 $S$ 的**秩**，记作 $\operatorname{rank}(S)$；只含零向量的向量组的秩规定为零。

### 8.3.2. 基与维数

**定义 8.3.4（基与维数）** 设 $V$ 是数域 $\mathbb{F}$ 上的线性空间。若 $V$ 中有一个线性无关的向量组，使 $V$ 中任意向量都可以被它线性表示，则称该向量组为 $V$ 的一组**基**。若 $V$ 的一组基含 $n$ 个向量，则称 $V$ 是 $n$ 维线性空间，$V$ 的**维数**为 $n$，记作 $\dim V=n$。若 $V$ 中存在任意多个线性无关的向量，则称 $V$ 为无限维线性空间；否则称 $V$ 为**有限维线性空间**。零空间 $\{0\}$ 的维数规定为 $0$。

由引理 8.3.1，有限维空间的任意两组基所含向量个数相同，所以维数是良定义的；需要强调数域时写作 $\dim_{\mathbb{F}}V$。

**命题 8.3.2（基的判定）** 设 $\dim V=n$，$a_1,\dots,a_n\in V$。若 $a_1,\dots,a_n$ 线性无关，或 $V=\operatorname{span}(a_1,\dots,a_n)$，则它是 $V$ 的一组基。

**证明** 若线性无关，对任意 $b\in V$，$n+1$ 个向量 $a_1,\dots,a_n,b$ 可以被 $V$ 的基（$n$ 个向量）线性表示，由引理 8.3.1 线性相关，再由命题 8.3.1，$b$ 可以被 $a_i$ 线性表示。若线性生成 $V$，取它的极大线性无关部分组，这是 $V$ 的一组基，由维数唯一，它就是全部 $n$ 个向量。$\square$

**定理 8.3.1（基扩充定理）** 有限维线性空间 $V$ 中任意 $r$ 个线性无关的向量都可以扩充成 $V$ 的一组基。因此，有限维空间 $V$ 的子空间 $M$ 的任意一组基都可以扩充成 $V$ 的一组基，$\dim M\le\dim V$，且等号成立当且仅当 $M=V$。

**证明** 若 $a_1,\dots,a_r$ 不是基，则有 $b\in V$ 不能被它们线性表示，由命题 8.3.1，$a_1,\dots,a_r,b$ 线性无关。重复这一步，由于 $V$ 中线性无关组的向量个数不超过 $\dim V$，过程必在有限步后停止。$\square$

**定理 8.3.2（维数公式）** 设 $M_1,M_2$ 是有限维线性空间 $V$ 的两个子空间，则

$$
\dim(M_1+M_2)=\dim M_1+\dim M_2-\dim(M_1\cap M_2).
$$

**证明** 取 $M_1\cap M_2$ 的一组基 $a_1,\dots,a_r$，分别扩充成 $M_1$ 的基 $a_1,\dots,a_r,b_1,\dots,b_s$ 与 $M_2$ 的基 $a_1,\dots,a_r,c_1,\dots,c_t$。只需证明这 $r+s+t$ 个向量是 $M_1+M_2$ 的一组基。它们显然线性生成 $M_1+M_2$。若 $\sum k_ia_i+\sum\ell_jb_j+\sum m_lc_l=0$，则 $v=-\sum m_lc_l=\sum k_ia_i+\sum\ell_jb_j\in M_1\cap M_2$，于是 $v$ 可以被 $a_1,\dots,a_r$ 线性表示；由 $a_i,c_l$ 线性无关得 $m_l=0$，$v=0$，再由 $a_i,b_j$ 线性无关得其余系数为零。$\square$

**推论 8.3.1** 设 $M_1,M_2$ 是有限维子空间，则 $M_1+M_2$ 是直和当且仅当 $\dim(M_1+M_2)=\dim M_1+\dim M_2$；这时 $M_1$ 与 $M_2$ 的基合起来是 $M_1\oplus M_2$ 的基。

维数公式与集合的容斥原理形式相同，但只对两个子空间成立：三个子空间的类似公式一般不对（$\mathbb{R}^2$ 中三条不同的直线）。

### 8.3.3. 例子

**例 8.3.1** 数域的选取影响维数：

- $\mathbb{R}$ 作为 $\mathbb{R}$ 上的线性空间，任一非零实数是一组基，维数为 $1$；作为 $\mathbb{Q}$ 上的线性空间，对任意 $n$，$1,\pi,\dots,\pi^n$ 线性无关（$\pi$ 是超越数，不是任何非零有理系数多项式的根），所以是无限维的。
- $\mathbb{C}$ 作为 $\mathbb{R}$ 上的线性空间，$1,\mathrm{i}$ 是一组基，$\dim_{\mathbb{R}}\mathbb{C}=2$；作为 $\mathbb{C}$ 上的线性空间，$\dim_{\mathbb{C}}\mathbb{C}=1$。

**例 8.3.2** 数组与矩阵空间：$\boldsymbol{e}_1,\dots,\boldsymbol{e}_m$ 是 $\mathbb{F}^m$ 的基，$\dim \mathbb{F}^m=m$。令 $E_{ij}$ 为 $(i,j)$ 元为 $1$、其余元素为 $0$ 的 $m\times n$ 矩阵，则 $\{E_{ij}\}$ 是 $\mathbb{F}^{m\times n}$ 的基，$\dim \mathbb{F}^{m\times n}=mn$。在例 8.2.1 中，$\dim\mathcal{U}=\dim\mathcal{L}=\dim\mathcal{S}=\frac{n(n+1)}2$，$\dim\mathcal{K}=\frac{n(n-1)}2$，$\dim(\mathcal{U}\cap\mathcal{L})=n$，与维数公式 $\dim(\mathcal{U}+\mathcal{L})=n(n+1)-n=n^2$、$\dim\mathcal{S}+\dim\mathcal{K}=n^2$ 一致。

**例 8.3.3** $\mathbb{F}[x]_n$ 中，$1,x,\dots,x^{n-1}$ 线性无关。设 $k_0+k_1x+\cdots+k_{n-1}x^{n-1}=0$（右端是零多项式，即函数值处处为零）。代入 $n$ 个两两不同的数 $\lambda_1,\dots,\lambda_n$，得齐次方程组

$$
\begin{bmatrix}1&\lambda_1&\cdots&\lambda_1^{n-1}\\\vdots&\vdots&&\vdots\\1&\lambda_n&\cdots&\lambda_n^{n-1}\end{bmatrix}\begin{bmatrix}k_0\\\vdots\\k_{n-1}\end{bmatrix}=\boldsymbol{0},
$$

系数矩阵是 **Vandermonde 矩阵**，可逆，所以 $k_i$ 全为零。因此 $1,x,\dots,x^{n-1}$ 是 $\mathbb{F}[x]_n$ 的基，$\dim \mathbb{F}[x]_n=n$；由 $n$ 的任意性，$\mathbb{F}[x]$、$C^\infty(D)$、$C(D)$ 与函数空间都是无限维的。

**例 8.3.4** $C^\infty(\mathbb{R})$ 中，对相异实数 $\lambda_1,\lambda_2$，$\mathrm{e}^{\lambda_1x},\mathrm{e}^{\lambda_2x}$ 线性无关。设 $k_1\mathrm{e}^{\lambda_1x}+k_2\mathrm{e}^{\lambda_2x}=0$（零函数），求导得 $k_1\lambda_1\mathrm{e}^{\lambda_1x}+k_2\lambda_2\mathrm{e}^{\lambda_2x}=0$，即

$$
\begin{bmatrix}\mathrm{e}^{\lambda_1x}&\mathrm{e}^{\lambda_2x}\\\lambda_1\mathrm{e}^{\lambda_1x}&\lambda_2\mathrm{e}^{\lambda_2x}\end{bmatrix}\begin{bmatrix}k_1\\k_2\end{bmatrix}=\boldsymbol{0},
$$

系数矩阵的**行列式** $\mathrm{e}^{(\lambda_1+\lambda_2)x}(\lambda_2-\lambda_1)\neq0$，故 $k_1=k_2=0$。对相异实数 $\lambda_1,\dots,\lambda_n$，求导 $n-1$ 次得到的系数行列式是 $\mathrm{e}^{(\lambda_1+\cdots+\lambda_n)x}$ 乘一个 Vandermonde 行列式，同理 $\mathrm{e}^{\lambda_1x},\dots,\mathrm{e}^{\lambda_nx}$ 线性无关。这一方法（Wronski 矩阵）在 [第 11 章](/2.1.11) 中用于判定函数向量的线性相关性。

## 8.4. 线性映射

**定义 8.4.1（线性映射）** 设 $U,V$ 是数域 $\mathbb{F}$ 上的线性空间。若映射 $f\colon U\to V$ 保持加法和数乘，即

1. 可加性：对任意 $a,b\in U$，$f(a+b)=f(a)+f(b)$；
2. 齐次性：对任意 $a\in U$，$k\in \mathbb{F}$，$f(ka)=kf(a)$，

则称 $f$ 为 $U$ 到 $V$ 的**线性映射**，也称为同态映射。$U$ 到 $V$ 的线性映射的全体记作 $\operatorname{Hom}(U,V)$。

线性映射就是线性空间这种代数系统之间的**同态**。$f\in\operatorname{Hom}(U,V)$ 满足 $f(0_U)=0_V$；**函数** $f\colon U\to V$ 是线性映射，当且仅当对任意 $a,b\in U$，$k,\ell\in \mathbb{F}$ 有 $f(ka+\ell b)=kf(a)+\ell f(b)$。

**定义 8.4.2（线性映射的运算）** 对 $f,g\in\operatorname{Hom}(U,V)$，$k\in \mathbb{F}$，定义 $f+g\colon x\mapsto f(x)+g(x)$，$kf\colon x\mapsto kf(x)$。对 $f\in\operatorname{Hom}(U,V)$，$g\in\operatorname{Hom}(V,W)$，定义 $f$ 与 $g$ 的复合 $g\circ f\colon U\to W$，$x\mapsto g(f(x))$，也称为 $g$ 与 $f$ 的乘积，记作 $gf$。

$f+g$、$kf$、$gf$ 仍是线性映射，$\operatorname{Hom}(U,V)$ 关于加法与数乘构成线性空间（零元是零映射）。复合满足结合律，对加法满足分配律，但一般不交换。

**定义 8.4.3（核与像集）** 对 $f\in\operatorname{Hom}(U,V)$，集合 $\mathcal{N}(f)=\{a\in U\mid f(a)=0\}$ 称为 $f$ 的**核**，集合 $\mathcal{R}(f)=\{f(a)\mid a\in U\}$ 称为 $f$ 的像集。

**命题 8.4.1** 设 $f\in\operatorname{Hom}(U,V)$，则 $\mathcal{N}(f)$ 是 $U$ 的子空间，$\mathcal{R}(f)$ 是 $V$ 的子空间；$f$ 是**单射**当且仅当 $\mathcal{N}(f)=\{0\}$；$f$ 是**满射**当且仅当 $\mathcal{R}(f)=V$。

**证明** 子空间由线性直接验证。若 $f$ 单射，则 $f(a)=0=f(0)$ 推出 $a=0$；反之若 $\mathcal{N}(f)=\{0\}$，由 $f(a)=f(b)$ 得 $f(a-b)=0$，$a=b$。满射的刻画是定义。$\square$

**定义 8.4.4（线性变换的特征值）** 线性空间 $U$ 到自身的线性映射称为 $U$ 上的**线性变换**。设 $f\in\operatorname{Hom}(U,U)$，若 $\lambda\in \mathbb{F}$ 与非零向量 $x\in U$ 满足 $f(x)=\lambda x$，则称 $\lambda$ 为 $f$ 的**特征值**，$x$ 为 $f$ 的属于 $\lambda$ 的**特征向量**，$(\lambda,x)$ 为 $f$ 的特征对；核 $\mathcal{N}(\lambda\,\mathrm{id}-f)$ 称为 $f$ 的属于 $\lambda$ 的**特征子空间**，其中 $\mathrm{id}$ 是**恒等映射**。

**命题 8.4.2** 线性变换属于不同特征值的特征向量线性无关。

**证明** 设 $x_1,\dots,x_k$ 分别属于互不相同的特征值 $\lambda_1,\dots,\lambda_k$，对 $k$ 归纳。设 $c_1x_1+\cdots+c_kx_k=0$，两边作用 $f$，再减去 $\lambda_k$ 倍的原式，得 $c_1(\lambda_1-\lambda_k)x_1+\cdots+c_{k-1}(\lambda_{k-1}-\lambda_k)x_{k-1}=0$。由归纳假设 $c_i(\lambda_i-\lambda_k)=0$，故 $c_1=\cdots=c_{k-1}=0$，再由 $x_k\neq 0$ 得 $c_k=0$。$\square$

**例 8.4.1（线性映射的例子）**

- 设 $A\in \mathbb{F}^{m\times n}$，左乘 $L_A\colon \mathbb{F}^{n\times p}\to \mathbb{F}^{m\times p}$，$X\mapsto AX$ 与右乘 $R_A\colon \mathbb{F}^{\ell\times m}\to \mathbb{F}^{\ell\times n}$，$X\mapsto XA$ 都是线性映射。
- **转置** $\mathbb{F}^{m\times n}\to \mathbb{F}^{n\times m}$，$A\mapsto A^{\mathsf T}$ 与取**迹** $\mathbb{F}^{n\times n}\to \mathbb{F}$，$A\mapsto\operatorname{tr}(A)$ 都是线性映射。
- 在 $n$ 个两两不同的点取值：$C(\mathbb{R})\to\mathbb{R}^n$，$f\mapsto[f(x_i)]$ 是线性映射；插值问题就是问它限制在 $\mathbb{R}[x]_n$ 上是否为双射（例 8.3.3 说明是）。
- 对称化 $S\colon \mathbb{F}^{n\times n}\to \mathbb{F}^{n\times n}$，$A\mapsto\frac12(A+A^{\mathsf T})$ 是线性变换，$\mathcal{N}(S)$ 与 $\mathcal{R}(S)$ 分别是反对称、对称矩阵构成的子空间。由 $S^2=S$，特征值满足 $\lambda^2=\lambda$，所以只能是 $1,0$，相应的特征子空间为 $\mathcal{N}(\mathrm{id}-S)=\mathcal{R}(S)$ 与 $\mathcal{N}(S)$。
- 在 $C^\infty(\mathbb{R})$ 上，求导算子 $D=\frac{\mathrm{d}}{\mathrm{d}x}$ 是线性变换，$\mathcal{N}(D)$ 是常值函数构成的子空间。由 $(\lambda\,\mathrm{id}-D)f=0$，即 $f'=\lambda f$，解得 $f=k\mathrm{e}^{\lambda x}$，所以每个实数 $\lambda$ 都是 $D$ 的特征值，$\mathrm{e}^{\lambda x}$ 是相应的特征向量。结合命题 8.4.2，这再次证明了例 8.3.4。
- $V=\left\{\begin{bmatrix}a&-b\\b&a\end{bmatrix}\,\middle|\,a,b\in\mathbb{R}\right\}$ 是 $\mathbb{R}^{2\times2}$ 的子空间，$\mathbb{C}\to V$，$a+b\mathrm{i}\mapsto\begin{bmatrix}a&-b\\b&a\end{bmatrix}$ 是 $\mathbb{R}$ 上线性空间之间的双射线性映射，并且保持乘法（[第 9 章](/2.1.9)）。
- 给定可逆矩阵 $T\in \mathbb{F}^{n\times n}$，$\boldsymbol{x}\mapsto T\boldsymbol{x}$ 是 $\mathbb{F}^n$ 到自身的可逆线性变换。

## 8.5. 同构与坐标

**定义 8.5.1（同构映射）** 设 $U,V$ 是数域 $\mathbb{F}$ 上的线性空间。若存在双射 $f\in\operatorname{Hom}(U,V)$，则称 $U$ 与 $V$（线性）同构，$f$ 称为 $U$ 到 $V$ 的**同构**映射。$U$ 到自身的同构映射称为 $U$ 上的**自同构**。

**命题 8.5.1** 设 $f\colon U\to V$，$g\colon V\to W$ 是同构映射，则 $gf\colon U\to W$ 与 $f^{-1}\colon V\to U$ 都是同构映射。因此线性空间的同构关系是**等价关系**。

**证明** $gf$ 是线性的双射。$f^{-1}$ 是双射，只需验证它是线性的：对 $x_1,x_2\in V$，记 $a_i=f^{-1}(x_i)$，由 $f(k_1a_1+k_2a_2)=k_1x_1+k_2x_2$ 得 $f^{-1}(k_1x_1+k_2x_2)=k_1f^{-1}(x_1)+k_2f^{-1}(x_2)$。同构关系的自反性来自恒等映射，对称性与传递性来自上面两条。$\square$

$n$ 阶可逆矩阵对应的 $\mathbb{F}^n$ 上的自同构在复合下构成**一般线性群**。同构关系既然是等价关系，就要问它的不变量与标准形是什么。答案由坐标给出。

**定义 8.5.2（坐标）** 设 $e_1,\dots,e_n$ 是 $n$ 维线性空间 $V$ 的一组基。任意 $x\in V$ 可以唯一地写成 $x=x_1e_1+\cdots+x_ne_n=(e_1,\dots,e_n)\hat{\boldsymbol{x}}$，有序数组 $\hat{\boldsymbol{x}}=[x_1\ \cdots\ x_n]^{\mathsf T}\in \mathbb{F}^n$ 称为 $x$ 在这组基下的**坐标**。

坐标依赖于基向量的顺序：交换两个基向量，坐标的相应分量也交换。由此得到坐标映射

$$
\sigma_{e_1,\dots,e_n}\colon V\to \mathbb{F}^n,\quad x\mapsto\hat{\boldsymbol{x}},\qquad \sigma^{-1}_{e_1,\dots,e_n}\colon \mathbb{F}^n\to V,\quad\hat{\boldsymbol{x}}\mapsto(e_1,\dots,e_n)\hat{\boldsymbol{x}}.
$$

**定理 8.5.1** 坐标映射 $\sigma_{e_1,\dots,e_n}\colon V\to \mathbb{F}^n$ 是同构映射。因此数域 $\mathbb{F}$ 上两个有限维线性空间同构，当且仅当它们的维数相等：维数是同构关系的完全不变量，$\mathbb{F}^n$ 是 $n$ 维空间的标准形。

**证明** $\sigma$ 是双射，且由 $kx+\ell y=(e_1,\dots,e_n)(k\hat{\boldsymbol{x}}+\ell\hat{\boldsymbol{y}})$ 得 $\sigma(kx+\ell y)=k\sigma(x)+\ell\sigma(y)$。所以 $n$ 维空间都与 $\mathbb{F}^n$ 同构，从而互相同构。反之，若 $f\colon U\to V$ 是同构映射，$e_1,\dots,e_n$ 是 $U$ 的基，则 $f(e_1),\dots,f(e_n)$ 线性无关（$f$ 单射）且线性生成 $V$（$f$ 满射），是 $V$ 的基，故 $\dim V=n$。$\square$

同构映射保持线性运算，从而保持一切只用线性运算表述的性质。特别地：

**推论 8.5.1** 在 $n$ 维线性空间 $V$ 中取定一组基，设 $a_1,\dots,a_m$ 的坐标为 $\hat{\boldsymbol{a}}_1,\dots,\hat{\boldsymbol{a}}_m$，则 $a_1,\dots,a_m$ 在 $V$ 中线性无关，当且仅当 $\hat{\boldsymbol{a}}_1,\dots,\hat{\boldsymbol{a}}_m$ 在 $\mathbb{F}^n$ 中线性无关；一般地，向量组的**秩**等于坐标矩阵 $[\hat{\boldsymbol{a}}_1\ \cdots\ \hat{\boldsymbol{a}}_m]$ 的秩。

这就是"标准化求解"在抽象空间中的体现：判断多项式、矩阵或函数的线性相关性、求极大线性无关部分组，都化为对坐标矩阵做 Gauss 消元。例如 $1+x,\ x+x^2,\ 1-x^2$ 在基 $1,x,x^2$ 下的坐标矩阵 $\begin{bmatrix}1&0&1\\1&1&0\\0&1&-1\end{bmatrix}$ 的秩为 $2$（第三列等于第一列减第二列），所以它们线性相关，且 $1-x^2=(1+x)-(x+x^2)$。

### 8.5.1. 基变换与坐标变换

坐标依赖于基的选取。设 $e_1,\dots,e_n$ 与 $t_1,\dots,t_n$ 是 $V$ 的两组基，每个 $t_j$ 都能被 $e_1,\dots,e_n$ 线性表示：

$$
(t_1,\dots,t_n)=(e_1,\dots,e_n)T,\qquad T=\begin{bmatrix}t_{11}&\cdots&t_{1n}\\\vdots&&\vdots\\t_{n1}&\cdots&t_{nn}\end{bmatrix}.
$$

这称为基变换公式，$T$ 称为从基 $e_1,\dots,e_n$ 到基 $t_1,\dots,t_n$ 的过渡矩阵（change-of-basis matrix）；它的第 $j$ 列是 $t_j$ 在旧基下的坐标。设 $a\in V$ 在两组基下的坐标分别为 $\boldsymbol{x}$ 与 $\boldsymbol{y}$，则

$$
a=(e_1,\dots,e_n)\boldsymbol{x}=(t_1,\dots,t_n)\boldsymbol{y}=(e_1,\dots,e_n)(T\boldsymbol{y}),
$$

由坐标的唯一性得坐标变换公式 $\boldsymbol{x}=T\boldsymbol{y}$，$\boldsymbol{y}=T^{-1}\boldsymbol{x}$。注意方向：基按 $T$ 变化，坐标按 $T^{-1}$ 变化。例如在 $\mathbb{R}^2$ 中取 $\boldsymbol{t}_1=2\boldsymbol{e}_1+\boldsymbol{e}_2$，$\boldsymbol{t}_2=\boldsymbol{e}_1+2\boldsymbol{e}_2$，即 $T=\begin{bmatrix}2&1\\1&2\end{bmatrix}$；向量 $\boldsymbol{a}=[4\ 5]^{\mathsf T}$ 在新基下的坐标是 $\boldsymbol{y}=T^{-1}\boldsymbol{a}=[1\ 2]^{\mathsf T}$，即 $\boldsymbol{a}=\boldsymbol{t}_1+2\boldsymbol{t}_2$。

![同一个向量 a 在两组基下的坐标：左边标准基下为 (4, 5)，右边基 t_1, t_2 下为 (1, 2)；网格线是各自坐标系的坐标线，虚线是 a 沿基向量的分解](./plots/change-of-basis-coordinates.py)

**命题 8.5.2** 设 $e_1,\dots,e_n$ 是 $V$ 的基，$T\in \mathbb{F}^{n\times n}$，$(t_1,\dots,t_n)=(e_1,\dots,e_n)T$，则 $t_1,\dots,t_n$ 是 $V$ 的基，当且仅当 $T$ 可逆。

**证明** 由推论 8.5.1，$t_j$ 线性无关当且仅当它们的坐标，即 $T$ 的列，线性无关，即 $T$ 可逆。$\square$

**算法 8.5.1（$\mathbb{F}^n$ 中的过渡矩阵）** 设 $\mathbb{F}^n$ 的两组基分别排成可逆矩阵 $A$ 与 $B$，则过渡矩阵 $T$ 满足 $B=AT$，即 $T=A^{-1}B$。对 $[A\ B]$ 做 **Gauss–Jordan 消元法**：

$$
[A\ \ B]\ \longrightarrow\ [I\ \ A^{-1}B]=[I\ \ T].
$$

若两组基张成 $\mathbb{F}^n$ 的同一个 $m$ 维子空间，$A,B$ 是 $n\times m$ 列满秩矩阵，则消元得 $[A\ B]\to\begin{bmatrix}I_m&T\\O&O\end{bmatrix}$；用 **Moore–Penrose 广义逆**写，$T=A^+B=(A^{\mathsf T}A)^{-1}A^{\mathsf T}B$（实数域上）。

**例 8.5.1** $\mathbb{F}^{2\times2}$ 有基 $E_{11},E_{12},E_{21},E_{22}$，$A=\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}$ 的坐标是 $\boldsymbol{a}=[a_{11}\ a_{12}\ a_{21}\ a_{22}]^{\mathsf T}$。另一组基 $E_{11},E_{22},E_{12}+E_{21},E_{12}-E_{21}$ 由对称矩阵与反对称矩阵组成（例 8.2.1 的直和分解），过渡矩阵与新坐标为

$$
T=\begin{bmatrix}1&0&0&0\\0&0&1&1\\0&0&1&-1\\0&1&0&0\end{bmatrix},\qquad \tilde{\boldsymbol{a}}=\Big[a_{11}\ \ a_{22}\ \ \tfrac{a_{12}+a_{21}}2\ \ \tfrac{a_{12}-a_{21}}2\Big]^{\mathsf T},
$$

可以验证 $\boldsymbol{a}=T\tilde{\boldsymbol{a}}$。

**例 8.5.2** $\mathbb{R}[x]_n$ 有基 $1,x,\dots,x^{n-1}$ 与 $1,x-x_0,\dots,(x-x_0)^{n-1}$。对 $f=a_0+a_1x+\cdots+a_{n-1}x^{n-1}$，由 Taylor 展开，$f$ 在后一组基下的坐标是 $\tilde{\boldsymbol{f}}=\Big[f(x_0)\ \ f'(x_0)\ \ \cdots\ \ \frac{f^{(n-1)}(x_0)}{(n-1)!}\Big]^{\mathsf T}$。由二项式展开 $(x-x_0)^k=\sum_{i=0}^k\binom ki(-x_0)^{k-i}x^i$，过渡矩阵是上三角矩阵

$$
T=\begin{bmatrix}1&-x_0&x_0^2&\cdots&(-x_0)^{n-1}\\&1&-2x_0&\cdots&(n-1)(-x_0)^{n-2}\\&&\ddots&\ddots&\vdots\\&&&1&-(n-1)x_0\\&&&&1\end{bmatrix},
$$

其 $(i,k)$ 元（从 $0$ 编号）为 $\binom ki(-x_0)^{k-i}$，且 $[a_0\ \cdots\ a_{n-1}]^{\mathsf T}=T\tilde{\boldsymbol{f}}$。

同一个空间的不同的基各有所长。下图画出 $\mathbb{R}[x]_4$ 的三组基：单项式基最便于运算，但在 $[0,1]$ 上 $x^2$ 与 $x^3$ 的图像相差不大，用它表示函数时系数对误差很敏感（相应的 Vandermonde 矩阵病态）；平移后的基 $(x-x_0)^k$ 下的坐标是 $f$ 在 $x_0$ 处的 Taylor 系数（例 8.5.2）；以 $0,\frac13,\frac23,1$ 为节点的 Lagrange 基 $L_0,\dots,L_3$ 满足 $L_i(a_j)=\delta_{ij}$，多项式在这组基下的坐标就是它在四个节点处的值（定理 9.4.2）。

![R[x]_4 的三组基在 [0, 1] 上的图像：单项式基 1, x, x^2, x^3；平移基 (x − 1/2)^k；以 0, 1/3, 2/3, 1 为节点的 Lagrange 基，L_i 在第 i 个节点取 1（空心点）、在其余节点取 0（实心点）](./plots/polynomial-bases.py)

## 8.6. 线性映射的矩阵表示

**命题 8.6.1** 设 $U,V$ 是有限维线性空间，$e_1,\dots,e_n$ 是 $U$ 的基，则：

1. 任意 $f\in\operatorname{Hom}(U,V)$ 由基的像 $f(e_1),\dots,f(e_n)$ 唯一确定；
2. 对 $V$ 中任意 $n$ 个向量 $a_1,\dots,a_n$，存在唯一的 $f\in\operatorname{Hom}(U,V)$ 使 $f(e_i)=a_i$。

**证明** 1：若 $f(e_i)=g(e_i)$，则对 $a=\sum a_ie_i$ 有 $f(a)=\sum a_if(e_i)=\sum a_ig(e_i)=g(a)$。2：唯一性由 1 得到。存在性：定义 $f(x_1e_1+\cdots+x_ne_n)=x_1a_1+\cdots+x_na_n$，坐标唯一保证 $f$ 是映射，坐标的线性保证 $f$ 是线性映射。$\square$

记 $f(e_1,\dots,e_n)=(f(e_1),\dots,f(e_n))$，则 $\operatorname{Hom}(U,V)$ 与 $V$ 中有序的 $n$ 元向量组一一对应。再取 $V$ 的基，把这些像写成坐标，就得到矩阵。

**定义 8.6.1（线性映射的矩阵）** 设 $e_1,\dots,e_n$ 与 $\eta_1,\dots,\eta_m$ 分别是 $U$ 与 $V$ 的基，$f\in\operatorname{Hom}(U,V)$，$f(e_j)=f_{1j}\eta_1+\cdots+f_{mj}\eta_m$，即

$$
f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F,\qquad F=[f_{ij}]_{m\times n},
$$

则 $m\times n$ 矩阵 $F$ 称为 $f$ 在基 $e_1,\dots,e_n;\eta_1,\dots,\eta_m$ 下的**表示矩阵**。$F$ 的第 $j$ 列是 $f(e_j)$ 的坐标。

对 $a=(e_1,\dots,e_n)\hat{\boldsymbol{a}}$，由线性，$f(a)=(f(e_1),\dots,f(e_n))\hat{\boldsymbol{a}}=(\eta_1,\dots,\eta_m)(F\hat{\boldsymbol{a}})$，即

$$
\widehat{f(a)}=F\hat{\boldsymbol{a}}:
$$

在坐标下，线性映射就是左乘它的矩阵。形式上 $f((e_1,\dots,e_n)K)=\big(f(e_1,\dots,e_n)\big)K$ 对任意 $n\times p$ 矩阵 $K$ 成立。对 $\mathbb{F}^n\to \mathbb{F}^m$ 的线性映射取标准基，表示矩阵就是 $[f(\boldsymbol{e}_1)\ \cdots\ f(\boldsymbol{e}_n)]$，这正是 [第 1 章](/2.1.1) 的定义。

**定理 8.6.1** 映射 $\sigma=\sigma_{e_1,\dots,e_n;\eta_1,\dots,\eta_m}\colon \operatorname{Hom}(U,V)\to \mathbb{F}^{m\times n}$，$f\mapsto F$ 是同构映射。特别地 $\dim\operatorname{Hom}(U,V)=mn$。

**证明** $f$ 与向量组 $(f(e_1),\dots,f(e_n))$ 一一对应，每个 $f(e_j)$ 又与它的坐标一一对应，所以 $\sigma$ 是双射。对 $\sigma(f)=F$，$\sigma(g)=G$，

$$
(kf+\ell g)(e_1,\dots,e_n)=k(\eta_1,\dots,\eta_m)F+\ell(\eta_1,\dots,\eta_m)G=(\eta_1,\dots,\eta_m)(kF+\ell G),
$$

故 $\sigma(kf+\ell g)=k\sigma(f)+\ell\sigma(g)$。$\square$

**命题 8.6.2** 设 $U,V,W$ 分别有基 $e_1,\dots,e_n$；$\eta_1,\dots,\eta_m$；$\zeta_1,\dots,\zeta_\ell$，$f\in\operatorname{Hom}(U,V)$，$g\in\operatorname{Hom}(V,W)$，则 $\sigma(gf)=\sigma(g)\sigma(f)$：复合映射的矩阵是矩阵的乘积。

**证明** 设 $f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F$，$g(\eta_1,\dots,\eta_m)=(\zeta_1,\dots,\zeta_\ell)G$，则

$$
(gf)(e_1,\dots,e_n)=g\big((\eta_1,\dots,\eta_m)F\big)=\big(g(\eta_1,\dots,\eta_m)\big)F=(\zeta_1,\dots,\zeta_\ell)(GF).\ \square
$$

所以同构 $\sigma$ 不仅保持线性运算，也保持乘法：线性映射的代数与矩阵的代数完全相同。这解释了矩阵乘法为什么要那样定义，也说明 $f$ 可逆当且仅当它的矩阵可逆（$\dim U=\dim V$ 时），且 $\sigma(f^{-1})=\sigma(f)^{-1}$。

**命题 8.6.3** 设 $F$ 是 $f\in\operatorname{Hom}(U,V)$ 在基 $e_1,\dots,e_n;\eta_1,\dots,\eta_m$ 下的矩阵，则坐标映射限制为同构 $\mathcal{N}(f)\to\mathcal{N}(F)$ 与 $\mathcal{R}(f)\to\mathcal{R}(F)$。于是 $\dim\mathcal{N}(f)=\dim\mathcal{N}(F)$，$\dim\mathcal{R}(f)=\operatorname{rank}(F)$，并且

$$
\dim\mathcal{N}(f)+\dim\mathcal{R}(f)=\dim U.
$$

**证明** 由 $\widehat{f(a)}=F\hat{\boldsymbol{a}}$，$a\in\mathcal{N}(f)$ 当且仅当 $\hat{\boldsymbol{a}}\in\mathcal{N}(F)$；$b\in\mathcal{R}(f)$ 当且仅当存在 $\hat{\boldsymbol{a}}$ 使 $\hat{\boldsymbol{b}}=F\hat{\boldsymbol{a}}$，即 $\hat{\boldsymbol{b}}\in\mathcal{R}(F)$。最后一式是矩阵的**秩–零化度定理** $\dim\mathcal{N}(F)+\operatorname{rank}(F)=n$。$\square$

$\dim\mathcal{R}(f)$ 称为 $f$ 的秩，它不依赖于基的选取。由此，当 $\dim U=\dim V<\infty$ 时，$f\in\operatorname{Hom}(U,V)$ 是单射 ⇔ 满射 ⇔ 双射；无限维时这不成立，例如 $\mathbb{R}[x]$ 上的求导是满射但不是单射。

**例 8.6.1** 设 $A=[\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]\in \mathbb{F}^{m\times n}$，$L_A\colon \mathbb{F}^{n\times2}\to \mathbb{F}^{m\times2}$，$X\mapsto AX$。取基 $E_{j1}=[\boldsymbol{e}_j\ \boldsymbol{0}]$，$E_{j2}=[\boldsymbol{0}\ \boldsymbol{e}_j]$（$j=1,\dots,n$）与 $F_{i1}=[\boldsymbol{e}_i\ \boldsymbol{0}]$，$F_{i2}=[\boldsymbol{0}\ \boldsymbol{e}_i]$（$i=1,\dots,m$），都按先第一列后第二列的顺序排列。由 $AE_{j1}=[\boldsymbol{a}_j\ \boldsymbol{0}]$，$AE_{j2}=[\boldsymbol{0}\ \boldsymbol{a}_j]$，$L_A$ 的矩阵是分块对角矩阵 $\begin{bmatrix}A&\\&A\end{bmatrix}$。

**例 8.6.2** 在 $V=\operatorname{span}(1,\sin x,\cos x)\subseteq C^\infty(\mathbb{R})$ 上，求导 $D$ 是线性变换：

$$
D(1,\sin x,\cos x)=(0,\cos x,-\sin x)=(1,\sin x,\cos x)\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix}.
$$

在 $\mathbb{R}[x]_n$ 的基 $1,x,\dots,x^{n-1}$ 下，$D$ 的矩阵是上次对角线为 $1,2,\dots,n-1$、其余为零的 $n$ 阶矩阵。

## 8.7. 基变换下的矩阵：相抵与相似

### 8.7.1. 线性映射：相抵

**定理 8.7.1** 设 $U$ 有两组基 $e_1,\dots,e_n$ 与 $t_1,\dots,t_n$，过渡矩阵为 $T$；$V$ 有两组基 $\eta_1,\dots,\eta_m$ 与 $s_1,\dots,s_m$，过渡矩阵为 $S$。若 $f\in\operatorname{Hom}(U,V)$ 在前两组基下的矩阵为 $F$，则 $f$ 在后两组基下的矩阵为 $\tilde F=S^{-1}FT$。

**证明** 由定义 $f(t_1,\dots,t_n)=(s_1,\dots,s_m)\tilde F=(\eta_1,\dots,\eta_m)(S\tilde F)$；另一方面

$$
f(t_1,\dots,t_n)=f\big((e_1,\dots,e_n)T\big)=\big((\eta_1,\dots,\eta_m)F\big)T=(\eta_1,\dots,\eta_m)(FT).
$$

由坐标唯一得 $S\tilde F=FT$，而 $S$ 可逆，故 $\tilde F=S^{-1}FT$。$\square$

所以同一个线性映射在不同基下的矩阵**相抵**。反之也成立：

**定理 8.7.2** 设 $f\in\operatorname{Hom}(U,V)$ 在某两组基下的矩阵是 $F$，则对任意与 $F$ 相抵的矩阵 $\tilde F$，存在 $U,V$ 的基使 $f$ 在其下的矩阵是 $\tilde F$。特别地，存在 $U,V$ 的基使 $f$ 的矩阵是**相抵标准形** $\begin{bmatrix}I_r&O\\O&O\end{bmatrix}$，$r=\operatorname{rank}(F)=\dim\mathcal{R}(f)$。

**证明** 若 $\tilde F=PFQ$，$P,Q$ 可逆，取 $T=Q$，$S=P^{-1}$，由命题 8.5.2 它们确定新的基，由定理 8.7.1 新矩阵为 $S^{-1}FT=\tilde F$。$\square$

相抵标准形对应的基也可以直接构造：取 $\mathcal{N}(f)$ 的基 $t_{r+1},\dots,t_n$，扩充成 $U$ 的基 $t_1,\dots,t_n$；则 $s_i=f(t_i)$（$i\le r$）是 $\mathcal{R}(f)$ 的基，再扩充成 $V$ 的基。在这两组基下 $f(t_i)=s_i$（$i\le r$），$f(t_i)=0$（$i>r$）。可见对两个空间之间的线性映射，唯一的不变量是秩：只要两边的基可以独立地选取，线性映射就没有更多的结构。

### 8.7.2. 线性变换：相似

线性变换 $f\in\operatorname{Hom}(V,V)$ 的定义域与陪域相同，表示矩阵时两边取同一组基：$f(e_1,\dots,e_n)=(e_1,\dots,e_n)F$，$n$ 阶方阵 $F$ 称为 $f$ 在这组基下的矩阵。

**命题 8.7.1** 设 $f\in\operatorname{Hom}(V,V)$ 在基 $e_1,\dots,e_n$ 下的矩阵为 $F$，$x$ 的坐标为 $\hat{\boldsymbol{x}}$，则 $(\lambda,x)$ 是 $f$ 的特征对，当且仅当 $(\lambda,\hat{\boldsymbol{x}})$ 是 $F$ 的特征对。因此 $F$ 可对角化当且仅当 $f$ 有 $n$ 个线性无关的特征向量。

**证明** $f(x)=(e_1,\dots,e_n)(F\hat{\boldsymbol{x}})$，由坐标唯一，$f(x)=\lambda x$ 当且仅当 $F\hat{\boldsymbol{x}}=\lambda\hat{\boldsymbol{x}}$。后一句由推论 8.5.1 与 [第 6 章](/2.1.6) 的对角化判据得到。$\square$

通过矩阵表示，抽象空间中线性变换的特征值问题化为矩阵的特征值问题，再化为求**特征多项式**的根与解齐次线性方程组。

**定理 8.7.3** 设 $V$ 的两组基之间的过渡矩阵为 $T$，即 $(t_1,\dots,t_n)=(e_1,\dots,e_n)T$。若 $f\in\operatorname{Hom}(V,V)$ 在基 $e_1,\dots,e_n$ 下的矩阵为 $F$，则 $f$ 在基 $t_1,\dots,t_n$ 下的矩阵为 $T^{-1}FT$。

**证明** 在定理 8.7.1 中取 $S=T$。$\square$

**定理 8.7.4** 数域 $\mathbb{F}$ 上的两个 $n$ 阶方阵 $A,B$ **相似**，当且仅当它们是某个 $n$ 维线性空间 $V$ 上同一个线性变换在两组基下的矩阵。

**证明** 充分性即定理 8.7.3。必要性：设 $B=T^{-1}AT$。任取 $V$ 的基 $e_1,\dots,e_n$，由命题 8.6.1 存在线性变换 $f$ 使 $f(e_1,\dots,e_n)=(e_1,\dots,e_n)A$。令 $(t_1,\dots,t_n)=(e_1,\dots,e_n)T$，它是一组基，$f$ 在其下的矩阵为 $T^{-1}AT=B$。$\square$

这一定理是后面几章的出发点：

- 把 $A$ 对角化，就是为 $\mathbb{F}^n$ 找一组基 $(\boldsymbol{t}_1,\dots,\boldsymbol{t}_n)=(\boldsymbol{e}_1,\dots,\boldsymbol{e}_n)T$，使 $\boldsymbol{x}\mapsto A\boldsymbol{x}$ 在这组基下的矩阵 $T^{-1}AT$ 是对角矩阵；这组基就是 $A$ 的 $n$ 个线性无关的特征向量。
- 相似不变量（特征多项式、特征值及其重数、**迹**、**行列式**、秩）都是线性变换本身的不变量，于是可以定义线性变换的特征多项式、迹与行列式，而不必指明基。
- 不能对角化时，自然的问题是：怎样选基能使矩阵"最简单"？[第 10 章](/2.1.10) 用不变子空间与根子空间的直和分解回答，结论是 **Jordan 标准形**。

下面的计算演示了"换基化简"：$\mathbb{R}[x]_4$ 上求导的矩阵在基 $1,x,x^2,x^3$ 下的上次对角线是 $1,2,3$；换成基 $1,x,\frac{x^2}{2!},\frac{x^3}{3!}$ 后，矩阵变成上次对角线全为 $1$ 的 Jordan 块。

```python
import sympy as sp

x = sp.symbols("x")
n = 4

def coords(p):
    """Coordinates of p in the monomial basis 1, x, ..., x^(n-1)."""
    c = sp.Poly(p, x).all_coeffs()[::-1]
    return sp.Matrix(c + [0] * (n - len(c)))

D = lambda p: sp.diff(p, x)
mono = [x**k for k in range(n)]
F = sp.Matrix.hstack(*[coords(D(b)) for b in mono])   # matrix of D in 1, x, x^2, x^3
new = [x**k / sp.factorial(k) for k in range(n)]       # basis 1, x, x^2/2, x^3/6
T = sp.Matrix.hstack(*[coords(b) for b in new])        # transition matrix
print(F)
print(T.inv() * F * T)                                 # matrix of D in the new basis
```

**例 8.7.1** 对称化变换 $S\colon \mathbb{F}^{2\times2}\to \mathbb{F}^{2\times2}$，$A\mapsto\frac12(A+A^{\mathsf T})$，取基 $E_{11},E_{21},E_{12},E_{22}$。由 $S(E_{11})=E_{11}$，$S(E_{21})=S(E_{12})=\frac12(E_{21}+E_{12})$，$S(E_{22})=E_{22}$，

$$
S(E_{11},E_{21},E_{12},E_{22})=(E_{11},E_{21},E_{12},E_{22})\begin{bmatrix}1&0&0&0\\0&\frac12&\frac12&0\\0&\frac12&\frac12&0\\0&0&0&1\end{bmatrix}.
$$

这个矩阵对称，可对角化，特征值为 $0$（一重）与 $1$（三重），特征向量分别是 $[0\ 1\ {-1}\ 0]^{\mathsf T}$ 与 $[1\ 0\ 0\ 0]^{\mathsf T},[0\ 0\ 0\ 1]^{\mathsf T},[0\ 1\ 1\ 0]^{\mathsf T}$。换回矩阵，

$$
\mathcal{N}(S)=\operatorname{span}\left(\begin{bmatrix}0&-1\\1&0\end{bmatrix}\right),\qquad \mathcal{N}(\mathrm{id}-S)=\mathcal{R}(S)=\operatorname{span}\left(\begin{bmatrix}1&0\\0&0\end{bmatrix},\begin{bmatrix}0&0\\0&1\end{bmatrix},\begin{bmatrix}0&1\\1&0\end{bmatrix}\right),
$$

在基 $\begin{bmatrix}1&0\\0&0\end{bmatrix},\begin{bmatrix}0&0\\0&1\end{bmatrix},\begin{bmatrix}0&1\\1&0\end{bmatrix},\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ 下，$S$ 的矩阵是 $\operatorname{diag}(1,1,1,0)$。

**例 8.7.2** 例 8.6.2 中 $D$ 在 $\operatorname{span}(1,\sin x,\cos x)$ 上的矩阵的特征多项式是 $\lambda(\lambda^2+1)$，在 $\mathbb{R}$ 上只有特征值 $0$，所以 $D$ 在实数域上不能对角化。若允许复系数，$\mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x$ 与 $\mathrm{e}^{-\mathrm{i}x}$ 是属于 $\pm\mathrm{i}$ 的特征向量，$D$ 在基 $1,\mathrm{e}^{\mathrm{i}x},\mathrm{e}^{-\mathrm{i}x}$ 下的矩阵是 $\operatorname{diag}(0,\mathrm{i},-\mathrm{i})$。能否对角化取决于数域，这是 [第 9 章](/2.1.9) 讨论复数与多项式分解的原因。

本课程中矩阵的几种等价关系，都可以理解为同一个对象在不同基下的表示：

| 关系 | 矩阵形式 | 表示的对象 | 基的选取 | 标准形 |
|---|---|---|---|---|
| 相抵 | $S^{-1}FT$ | 线性映射 $U\to V$ | $U,V$ 的基独立选取 | $\operatorname{diag}(I_r,O)$ |
| 相似 | $T^{-1}FT$ | 线性变换 $V\to V$ | 同一组基 | Jordan 标准形（[第 10 章](/2.1.10)） |
| 正交（酉）相似 | $Q^{\mathsf T}FQ$ | 内积空间上的线性变换 | 标准正交基 | 正规矩阵为对角形（[第 12 章](/2.1.12)） |
| 合同 | $T^{\mathsf T}GT$ | 双线性型 $V\times V\to \mathbb{F}$ | 同一组基 | 实对称时 $\operatorname{diag}(I_p,-I_q,O)$（[第 7 章](/2.1.7)、[第 13 章](/2.1.13)） |

## 8.8. 对偶空间

内积 $\langle\boldsymbol{x},\boldsymbol{u}\rangle$ 固定 $\boldsymbol{u}$ 时是 $\boldsymbol{x}$ 的线性函数，迹是矩阵的线性函数，定积分是连续函数的线性函数。这类"向量 ↦ 数"的线性映射本身构成线性空间，它与原空间对偶，转置运算正是在这里得到解释。

**定义 8.8.1（线性函数）** 设 $V$ 是数域 $\mathbb{F}$ 上的线性空间，线性映射 $f\colon V\to \mathbb{F}$（$\mathbb{F}$ 看作一维线性空间）称为 $V$ 上的**线性函数**。

由命题 8.6.1，线性函数由它在一组基上的值决定。例如 $f\colon \mathbb{R}^2\to\mathbb{R}$，$f(\boldsymbol{e}_1)=10$，$f(\boldsymbol{e}_2)=1$，则 $f\big([a\ b]^{\mathsf T}\big)=af(\boldsymbol{e}_1)+bf(\boldsymbol{e}_2)=10a+b$。其他例子：$\mathbb{F}^{n\times n}\to \mathbb{F}$ 的迹；$C[a,b]\to\mathbb{R}$，$g\mapsto\int_a^bg(x)\,\mathrm{d}x$；$\mathbb{F}[x]\to \mathbb{F}$，$p\mapsto p(c)$；取坐标的第 $i$ 个分量 $\boldsymbol{x}\mapsto x_i$。

**定义 8.8.2（对偶空间）** $V$ 上线性函数的全体 $V^*=\operatorname{Hom}(V,\mathbb{F})$，关于加法 $(f+g)(v)=f(v)+g(v)$ 与数乘 $(cf)(v)=cf(v)$ 构成 $\mathbb{F}$ 上的线性空间，称为 $V$ 的**对偶空间**。

**例 8.8.1** $(\mathbb{R}^3)^*$ 中的元素都形如 $f(\boldsymbol{x})=ax_1+bx_2+cx_3$，其中 $a=f(\boldsymbol{e}_1)$，$b=f(\boldsymbol{e}_2)$，$c=f(\boldsymbol{e}_3)$；所以 $(\mathbb{R}^3)^*$ 可以等同于行向量 $[a\ b\ c]$ 的全体，$f(\boldsymbol{x})$ 就是行向量乘列向量。一般地，$\mathbb{F}^n$ 上的线性函数就是 $1\times n$ 矩阵（定理 8.6.1）。

**命题 8.8.1（$\mathbb{R}^n$ 上线性函数的表示）** 设 $f$ 是 $\mathbb{R}^n$ 上的线性函数，则存在唯一的 $\boldsymbol{u}\in\mathbb{R}^n$ 使 $f(\boldsymbol{x})=\langle\boldsymbol{x},\boldsymbol{u}\rangle=\boldsymbol{u}^{\mathsf T}\boldsymbol{x}$ 对一切 $\boldsymbol{x}$ 成立，即 $\boldsymbol{u}=[f(\boldsymbol{e}_1)\ \cdots\ f(\boldsymbol{e}_n)]^{\mathsf T}$。

**证明** $f(\boldsymbol{x})=\sum x_if(\boldsymbol{e}_i)=\boldsymbol{u}^{\mathsf T}\boldsymbol{x}$；若 $\boldsymbol{u}_1,\boldsymbol{u}_2$ 都满足，则 $\langle\boldsymbol{x},\boldsymbol{u}_1-\boldsymbol{u}_2\rangle=0$ 对一切 $\boldsymbol{x}$ 成立，取 $\boldsymbol{x}=\boldsymbol{u}_1-\boldsymbol{u}_2$ 得 $\boldsymbol{u}_1=\boldsymbol{u}_2$。$\square$

也就是说，借助**内积**，映射 $\boldsymbol{u}\mapsto\langle\cdot,\boldsymbol{u}\rangle$ 是 $\mathbb{R}^n$ 到 $(\mathbb{R}^n)^*$ 的同构。证明只用到标准正交基 $\boldsymbol{e}_i$，所以对任意有限维内积空间同样成立，这就是 Riesz 表示定理（一般的内积空间见 [第 12 章](/2.1.12)）。对没有内积的一般线性空间，下面用对偶基建立 $V$ 与 $V^*$ 的联系。

**定义 8.8.3（对偶基）** 设 $e_1,\dots,e_n$ 是 $V$ 的基。由命题 8.6.1，存在唯一的 $f_i\in V^*$ 使 $f_i(e_j)=\delta_{ij}$（$i,j=1,\dots,n$），称 $f_1,\dots,f_n$ 为 $e_1,\dots,e_n$ 的**对偶基**，常记作 $e_1^*,\dots,e_n^*$。

$f_i$ 就是"取第 $i$ 个坐标"的函数：$f_i(x_1e_1+\cdots+x_ne_n)=x_i$。所以 $x=\sum_if_i(x)e_i$。

**定理 8.8.1** 对偶基 $f_1,\dots,f_n$ 是 $V^*$ 的基，且任意 $f\in V^*$ 有 $f=\sum_{i=1}^nf(e_i)f_i$。特别地，$\dim V^*=\dim V$。

**证明** 线性无关：若 $c_1f_1+\cdots+c_nf_n=0$（零函数），两边作用于 $e_j$ 得 $c_j=0$。线性生成：令 $g=\sum_if(e_i)f_i$，则 $g(e_j)=f(e_j)$ 对一切 $j$ 成立，由命题 8.6.1，$g=f$。$\square$

**定理 8.8.2（对偶基的基变换）** 设 $e_1,\dots,e_n$ 与 $t_1,\dots,t_n$ 是 $V$ 的两组基，$(t_1,\dots,t_n)=(e_1,\dots,e_n)P$，二者的对偶基满足 $(t_1^*,\dots,t_n^*)=(e_1^*,\dots,e_n^*)Q$，则 $Q=(P^{\mathsf T})^{-1}$。

**证明** 设 $P=[p_{ij}]$，$Q=[q_{ij}]$，则 $t_k=\sum_ip_{ik}e_i$，$t_l^*=\sum_jq_{jl}e_j^*$，于是

$$
\delta_{lk}=t_l^*(t_k)=\sum_j\sum_iq_{jl}p_{ik}\,e_j^*(e_i)=\sum_iq_{il}p_{ik}=(Q^{\mathsf T}P)_{lk},
$$

即 $Q^{\mathsf T}P=I$，$Q=(P^{-1})^{\mathsf T}=(P^{\mathsf T})^{-1}$。$\square$

基按 $P$ 变化，坐标按 $P^{-1}$ 变化，而对偶基按 $(P^{\mathsf T})^{-1}$ 变化；线性函数的"坐标"（它在基上的值组成的行向量 $[f(e_1)\ \cdots\ f(e_n)]$）则按 $P$ 右乘变化，与基同步。物理中称前者为逆变、后者为协变。

**例 8.8.2** 设 $v_1,v_2,v_3$ 是 $V$ 的基，求 $\alpha=v_1$，$\beta=v_1+v_2$，$\gamma=v_1+v_2+v_3$ 的对偶基。过渡矩阵与所需的矩阵为

$$
P=\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix},\qquad (P^{\mathsf T})^{-1}=\begin{bmatrix}1&0&0\\-1&1&0\\0&-1&1\end{bmatrix},
$$

所以 $\alpha^*=v_1^*-v_2^*$，$\beta^*=v_2^*-v_3^*$，$\gamma^*=v_3^*$。验证：$\alpha^*(\beta)=1-1=0$，$\beta^*(\beta)=1$，$\beta^*(\gamma)=1-1=0$。

### 8.8.1. 二次对偶

记 $\langle f,v\rangle=f(v)$（$f\in V^*$，$v\in V$）。这个配对对两个变量都是线性的，并且是非退化的：

- 若 $\langle f,v\rangle=0$ 对一切 $v\in V$ 成立，则 $f=0$（定义）；
- 若 $\langle f,v\rangle=0$ 对一切 $f\in V^*$ 成立，则 $v=0$（否则把 $v$ 扩充成基，取对偶基中对应 $v$ 的元素 $f$，有 $f(v)=1$）。

**定理 8.8.3** 设 $V$ 是有限维线性空间，则 $\Phi\colon V\to V^{**}$，$v\mapsto\Phi_{v}$，$\Phi_{v}(f)=f(v)$ 是同构映射。

**证明** $\Phi_{v}$ 是 $V^*$ 上的线性函数，$\Phi$ 是线性映射。由配对的非退化性，$\Phi_{v}=0$ 推出 $v=0$，$\Phi$ 是单射；又 $\dim V^{**}=\dim V^*=\dim V$，由命题 8.6.3，$\Phi$ 是双射。$\square$

$V$ 与 $V^*$ 维数相同，因而同构，但同构映射依赖于基的选取（例如 $e_i\mapsto e_i^*$，换一组基就不同）；而 $\Phi\colon V\to V^{**}$ 的定义不涉及任何基，称为典范同构。因此可以把 $V$ 看作 $V^*$ 的对偶空间，$V$ 与 $V^*$ 互为对偶。对无限维空间，$\Phi$ 仍是单射，但一般不是满射。

### 8.8.2. 对偶映射

**定义 8.8.4（对偶映射）** 设 $f\in\operatorname{Hom}(U,V)$。映射 $f^{\mathsf t}\colon V^*\to U^*$，$\varphi\mapsto\varphi\circ f$ 称为 $f$ 的**对偶映射**。

$f^{\mathsf t}$ 是线性映射，并满足 $\langle f^{\mathsf t}\varphi,u\rangle=\langle\varphi,f(u)\rangle$。注意方向反转：$f$ 从 $U$ 到 $V$，$f^{\mathsf t}$ 从 $V^*$ 到 $U^*$。（对偶映射也常记作 $f^*$；本书把 $f^*$ 留给 [第 12 章](/2.1.12) 内积空间上的伴随变换。）

**定理 8.8.4** 设 $f\in\operatorname{Hom}(U,V)$ 在基 $e_1,\dots,e_n;\eta_1,\dots,\eta_m$ 下的矩阵为 $F$，则 $f^{\mathsf t}$ 在对偶基 $\eta_1^*,\dots,\eta_m^*;e_1^*,\dots,e_n^*$ 下的矩阵为 $F^{\mathsf T}$。

**证明** 由定理 8.8.1，$f^{\mathsf t}(\eta_k^*)=\sum_j\big(f^{\mathsf t}\eta_k^*\big)(e_j)\,e_j^*=\sum_j\eta_k^*\big(f(e_j)\big)e_j^*$。而 $f(e_j)=\sum_lf_{lj}\eta_l$，所以 $\eta_k^*(f(e_j))=f_{kj}$，即 $f^{\mathsf t}(\eta_k^*)$ 的坐标是 $F$ 的第 $k$ 行，$f^{\mathsf t}$ 的矩阵的第 $k$ 列是 $F$ 的第 $k$ 行。$\square$

所以矩阵的**转置**就是对偶映射的矩阵。矩阵转置的性质由此都有了不依赖坐标的解释：$(gf)^{\mathsf t}=f^{\mathsf t}g^{\mathsf t}$ 对应 $(GF)^{\mathsf T}=F^{\mathsf T}G^{\mathsf T}$；$\operatorname{rank}(f^{\mathsf t})=\operatorname{rank}(f)$ 对应行秩等于列秩；$f^{\mathsf t}$ 的核是在 $\mathcal{R}(f)$ 上取零的线性函数的全体，对应 $\mathcal{N}(A^{\mathsf T})$ 与 $\mathcal{R}(A)$ 的正交关系。在 $\mathbb{R}^n$ 中用命题 8.8.1 把线性函数等同于向量，对偶映射就是**伴随变换**在标准正交基下的特例。对偶空间与 $V^*\times V\to \mathbb{F}$ 的配对是 [第 13 章](/2.1.13) 双线性型与张量的出发点。

## 小结

本章把 $\mathbb{R}^n$ 的理论推广到数域上的线性空间，并用"取基"把抽象问题翻译回矩阵问题。

| 主题 | 定义与结论 | 化为矩阵问题的方式 |
|---|---|---|
| 数域与线性空间 | 对四则运算封闭的 $\mathbb{C}$ 的子集；八条运算法则；$\mathbb{F}^m$、$\mathbb{F}^{m\times n}$、函数空间、$\mathbb{F}[x]_n$ | — |
| 子空间的和与直和 | $M_1+M_2$；直和 ⇔ 零向量分解唯一 ⇔ $M_1\cap M_2=\{0\}$ | $\mathcal{R}(A)+\mathcal{R}(B)=\mathcal{R}([A\ B])$ |
| 基与维数 | 引理 8.3.1（多的组被少的组表示则相关）；基扩充；维数公式 $\dim(M_1+M_2)=\dim M_1+\dim M_2-\dim(M_1\cap M_2)$ | 齐次方程组 $K\boldsymbol{k}=\boldsymbol{0}$ |
| 线性映射 | $\operatorname{Hom}(U,V)$；核 $\mathcal{N}(f)$、像集 $\mathcal{R}(f)$；单射 ⇔ $\mathcal{N}(f)=\{0\}$ | — |
| 同构与坐标 | 坐标映射 $V\to \mathbb{F}^n$ 是同构；维数是同构的完全不变量 | 线性相关性、秩 ⇔ 坐标矩阵的秩 |
| 基变换 | $(t_i)=(e_i)T$，坐标 $\boldsymbol{x}=T\boldsymbol{y}$ | 算法 8.5.1：$[A\ B]\to[I\ T]$ |
| 矩阵表示 | $f(e_1,\dots,e_n)=(\eta_1,\dots,\eta_m)F$；$\operatorname{Hom}(U,V)\cong \mathbb{F}^{m\times n}$；$\sigma(gf)=\sigma(g)\sigma(f)$；$\dim\mathcal{N}(f)+\dim\mathcal{R}(f)=\dim U$ | $\widehat{f(a)}=F\hat{\boldsymbol{a}}$ |
| 换基 | 线性映射：$S^{-1}FT$（相抵，标准形 $\operatorname{diag}(I_r,O)$）；线性变换：$T^{-1}FT$（相似） | 相似 ⇔ 同一线性变换在两组基下的矩阵 |
| 对偶空间 | $V^*=\operatorname{Hom}(V,\mathbb{F})$；对偶基 $f_i(e_j)=\delta_{ij}$，换基按 $(P^{\mathsf T})^{-1}$；$V\cong V^{**}$ 典范同构 | 对偶映射的矩阵是 $F^{\mathsf T}$ |
