---
title: 高阶线性微分方程与线性微分方程组
---

[上一章](/2.2.15)的一阶线性方程有两个特点：解集的结构是"一个特解加上齐次方程的通解"，齐次方程的解构成一个一维的线性空间。本章把这两点推广到 $n$ 阶线性方程与线性方程组：齐次方程的解集是 $n$ 维**线性空间**，求通解就是求它的一组**基**；判断 $n$ 个解是否构成基，要用 Wronski 行列式。这里线性代数（[2.1](/2.1)）的语言不是比喻，而是字面意义上的：求导是线性映射，线性微分方程就是线性映射的方程，叠加原理、解的结构、基与维数都是 [2.1.3](/2.1.3)、[2.1.8](/2.1.8) 中结论的具体实例。

变系数方程一般解不出来，本章只讨论已知部分解时的降阶与常数变易法。常系数方程则可以完全解出：把求导记为算子 $\mathrm{D}$，方程写成 $P(\mathrm{D})y=f$，求齐次方程的基归结为求多项式 $P$ 的根（特征方程），求非齐次方程的特解则有待定系数法与微分算子法。物理中的振动问题是常系数二阶方程最重要的应用。最后一节讨论一阶线性方程组 $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$，它与 $n$ 阶方程可以互化；常系数方程组的解由 $A$ 的**特征值**与**特征向量**给出，一般情形的 $\mathrm{e}^{tA}$ 与 Jordan 形见 [2.1.11](/2.1.11#sec-11.9)。更系统的理论见常微分方程（[2.4](/2.4)），平面方程组在生物建模中的应用见 [7.4.4](/7.4.4)。

## 16.1. 线性微分方程解的结构

### 16.1.1. $n$ 阶线性方程

$n$ 阶线性方程的一般形式是

$$
y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x),\tag{16.1}
$$
$f\equiv0$ 时

$$
y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=0\tag{16.2}
$$
称为式 (16.1) 对应的齐次方程。记 $L(y)=y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny$，则式 (16.1)、(16.2) 分别是 $L(y)=f$ 与 $L(y)=0$。

**定理 16.1.1** 设 $a_1(x),\dots,a_n(x),f(x)$ 在区间 $I$ 上连续，则对任意 $x_0\in I$ 和任意实数 $\eta_0,\eta_1,\dots,\eta_{n-1}$，式 (16.1) 满足 $y^{(k)}(x_0)=\eta_k$（$k=0,1,\dots,n-1$）的解在整个 $I$ 上存在且唯一。

这是一般存在唯一性定理（定理 15.1.1 的高维形式，[2.4](/2.4)）在线性情形的加强：线性方程的解不会在 $I$ 内"爆破"，所以存在区间是整个 $I$。以下总设系数在 $I$ 上连续。

**定理 16.1.2（叠加原理）** 

1. $L$ 是线性的：$L(c_1y_1+c_2y_2)=c_1L(y_1)+c_2L(y_2)$。特别地，齐次方程 (16.2) 的解的线性组合仍是它的解；
2. 若 $L(y_1)=f_1$，$L(y_2)=f_2$，则 $L(y_1+y_2)=f_1+f_2$；
3. 非齐次方程 (16.1) 的两个解之差是齐次方程 (16.2) 的解。因此，若 $y^*$ 是式 (16.1) 的一个解，则式 (16.1) 的每个解都可以写成 $y=y^*+Y$，其中 $Y$ 是式 (16.2) 的解。

**证明** 求导是线性运算，乘以函数 $a_k(x)$ 也是，所以 $L$ 线性；第 2、3 条由线性直接得到。 $\square$

用线性代数的话说：$L$ 是从 $C^n(I)$ 到 $C(I)$ 的线性映射，齐次方程的解集是它的核，非齐次方程的解集是核的一个陪集 $y^*+\ker L$。第 2 条的意义是可以把右端拆开，分别求特解再相加。

### 16.1.2. 函数组的线性相关性与 Wronski 行列式

**定义 16.1.1** 设函数 $\varphi_1,\dots,\varphi_m$ 在区间 $I$ 上有定义。若存在不全为零的常数 $c_1,\dots,c_m$，使 $c_1\varphi_1(x)+\cdots+c_m\varphi_m(x)=0$ 对所有 $x\in I$ 成立，则称它们在 $I$ 上**线性相关**，否则称为**线性无关**。

这就是 [2.1.3](/2.1.3) 中线性相关的定义，向量空间取函数空间。例如 $x^2+1$，$2x^2$，$1$ 线性相关（$2(x^2+1)-2x^2-2\cdot1=0$）；$\cos x,\sin x$ 在任何区间上线性无关。

**例 16.1.1** 若 $\lambda_1,\dots,\lambda_m$ 互不相等，则 $\mathrm{e}^{\lambda_1x},\dots,\mathrm{e}^{\lambda_mx}$ 在任何区间上线性无关。设 $\sum c_k\mathrm{e}^{\lambda_kx}=0$，求导 $0,1,\dots,m-1$ 次后令 $x=x_0$，得关于 $c_k\mathrm{e}^{\lambda_kx_0}$ 的齐次线性方程组，系数矩阵是 **Vandermonde 矩阵** $(\lambda_k^{j})$，其行列式 $\prod_{j<k}(\lambda_k-\lambda_j)\ne0$，所以 $c_k=0$。

这个例子的方法是一般的：一个线性关系对所有 $x$ 成立，求导后仍成立，于是得到一个数字线性方程组。

**定义 16.1.2** 设 $\varphi_1,\dots,\varphi_m$ 在 $I$ 上有 $m-1$ 阶导数，称

$$
W(x)=W[\varphi_1,\dots,\varphi_m](x)=\begin{vmatrix}\varphi_1(x)&\varphi_2(x)&\cdots&\varphi_m(x)\\ \varphi_1'(x)&\varphi_2'(x)&\cdots&\varphi_m'(x)\\ \vdots&\vdots&&\vdots\\ \varphi_1^{(m-1)}(x)&\varphi_2^{(m-1)}(x)&\cdots&\varphi_m^{(m-1)}(x)\end{vmatrix}
$$
为函数组 $\varphi_1,\dots,\varphi_m$ 的 **Wronski 行列式**。

它是 [2.1.11](/2.1.11) 中 **Wronski 矩阵**（取 $n=1$，即数值函数）的行列式，只是这里按列排列函数、按行排列导数。

**命题 16.1.1** 若 $\varphi_1,\dots,\varphi_m$ 在 $I$ 上线性相关，则 $W(x)\equiv0$。等价地，若存在 $x_0\in I$ 使 $W(x_0)\ne0$，则它们线性无关。

**证明** 设 $\sum c_k\varphi_k\equiv0$，$c_k$ 不全为零，求导得 $\sum c_k\varphi_k^{(i)}(x)=0$（$i=0,\dots,m-1$）。对每个 $x$，以 $W(x)$ 的矩阵为系数的齐次线性方程组有非零解 $(c_1,\dots,c_m)^{\mathsf T}$，所以 $W(x)=0$。 $\square$

逆命题不成立。$\varphi_1(x)=x^3$（$x\ge0$），$0$（$x<0$）；$\varphi_2(x)=0$（$x\ge0$），$x^3$（$x<0$）。两者都有连续导数，$W(x)=\varphi_1\varphi_2'-\varphi_1'\varphi_2\equiv0$（每点至少一个函数及其导数为零），但它们在 $\mathbb{R}$ 上线性无关：$c_1\varphi_1+c_2\varphi_2=0$ 在 $x=1$ 与 $x=-1$ 处分别给出 $c_1=0$、$c_2=0$。对齐次线性方程的解，逆命题却成立：

**定理 16.1.3** 设 $y_1,\dots,y_n$ 是齐次方程 (16.2) 在 $I$ 上的 $n$ 个解，则下列条件等价：

1. $y_1,\dots,y_n$ 在 $I$ 上线性相关；
2. $W(x)\equiv0$，$x\in I$；
3. 存在 $x_0\in I$ 使 $W(x_0)=0$。

因此 $n$ 个解的 Wronski 行列式要么恒为零，要么处处不为零。

**证明** 1 ⇒ 2 是命题 16.1.1，2 ⇒ 3 显然。3 ⇒ 1：$W(x_0)=0$，所以数字方程组 $\sum_kc_ky_k^{(i)}(x_0)=0$（$i=0,\dots,n-1$）有非零解 $(c_1,\dots,c_n)$。令 $y=\sum c_ky_k$，由叠加原理 $y$ 是式 (16.2) 的解，且 $y(x_0)=y'(x_0)=\cdots=y^{(n-1)}(x_0)=0$。$y\equiv0$ 也满足同样的初始条件，由定理 16.1.1 的唯一性，$\sum c_ky_k\equiv0$。 $\square$

两个解时可以算得更具体：$W=y_1y_2'-y_1'y_2$ 满足 $W'=y_1y_2''-y_1''y_2=-a_1(x)W$（代入方程 $y''=-a_1y'-a_2y$），所以

$$
W(x)=W(x_0)\,\mathrm{e}^{-\int_{x_0}^xa_1(t)\,\mathrm{d}t}.
$$
这称为 Liouville 公式（对 $n$ 阶方程同样成立），它直接说明了 $W$ 恒为零或处处非零。方程组的情形见定理 16.6.2。

### 16.1.3. 解空间与通解

**定理 16.1.4** 齐次方程 (16.2) 的全部解构成 $C^n(I)$ 的一个 $n$ 维线性子空间。

**证明** 由叠加原理，解集是子空间。取 $x_0\in I$，设 $y_k$ 是满足初始条件 $(y_k(x_0),y_k'(x_0),\dots,y_k^{(n-1)}(x_0))=\boldsymbol{e}_k^{\mathsf T}$ 的解（$\boldsymbol{e}_k$ 是 $\mathbb{R}^n$ 的标准基，解的存在由定理 16.1.1 保证），则 $W(x_0)=\det I_n=1$，$y_1,\dots,y_n$ 线性无关。对任一解 $y$，记 $\eta_i=y^{(i)}(x_0)$，则 $\tilde y=\sum_{k=1}^n\eta_{k-1}y_k$ 是满足同样初始条件的解，由唯一性 $y=\tilde y$。所以 $y_1,\dots,y_n$ 是解空间的一组基。 $\square$

换一个角度：映射 $y\mapsto(y(x_0),\dots,y^{(n-1)}(x_0))^{\mathsf T}$ 是解空间到 $\mathbb{R}^n$ 的线性映射，存在性说明它是满射，唯一性说明它是单射，所以它是**同构**，解空间的**维数**为 $n$。

**定义 16.1.3** 齐次方程 (16.2) 的 $n$ 个线性无关的解称为它的一个**基本解组**。

**定理 16.1.5** 设 $y_1,\dots,y_n$ 是式 (16.2) 的基本解组，$y^*$ 是式 (16.1) 的一个特解，则式 (16.1) 的通解为

$$
y=y^*+C_1y_1+C_2y_2+\cdots+C_ny_n,
$$
并且它包含了式 (16.1) 的全部解。

这与一阶方程不同：线性方程的通解就是全部解（比较例 15.2.1）。于是求解线性方程分成两个任务：求齐次方程的 $n$ 个线性无关解，求非齐次方程的一个特解。

**例 16.1.2** 求解下列各题。（1）$y''+y=0$ 有解 $\cos x$、$\sin x$，$W=\begin{vmatrix}\cos x&\sin x\\-\sin x&\cos x\end{vmatrix}=1\ne0$，通解 $y=C_1\cos x+C_2\sin x$。

（2）$(x-1)y''-xy'+y=0$：系数之和为零，所以 $y=\mathrm{e}^x$ 是解（$y=y'=y''$）；$y=x$ 也是解（$y''=0$，$-x\cdot1+x=0$）。$W=\begin{vmatrix}x&\mathrm{e}^x\\1&\mathrm{e}^x\end{vmatrix}=(x-1)\mathrm{e}^x$ 在 $x>1$ 或 $x<1$ 上不为零，通解 $y=C_1x+C_2\mathrm{e}^x$。

## 16.2. 二阶变系数线性方程

本节考虑 $y''+a_1(x)y'+a_2(x)y=f(x)$。变系数方程没有通用的解法，但已知齐次方程的一个解时可以求出全部解，常数变易法是其中的关键。

### 16.2.1. 已知一个解时的降阶

设 $y_1$ 是齐次方程 $y''+a_1y'+a_2y=0$ 的一个非零解。令 $y_2=C(x)y_1$，代入齐次方程，含 $C$ 的项因 $y_1$ 是解而消去，得

$$
C''y_1+C'(2y_1'+a_1y_1)=0,
$$
这是 $C'$ 的一阶线性方程（变量分离）：$\dfrac{\mathrm{d}C'}{C'}=-\Big(\dfrac{2y_1'}{y_1}+a_1\Big)\mathrm{d}x$，取一个非零解

$$
C'(x)=\frac{1}{y_1^2}\mathrm{e}^{-\int a_1(x)\,\mathrm{d}x},\qquad y_2=y_1\int\frac{1}{y_1^2}\mathrm{e}^{-\int a_1(x)\,\mathrm{d}x}\,\mathrm{d}x.
$$
$C'\ne0$，$C$ 不是常数，所以 $y_2$ 与 $y_1$ 线性无关（也可由 $W[y_1,y_2]=y_1^2C'=\mathrm{e}^{-\int a_1\mathrm{d}x}\ne0$ 看出，与 Liouville 公式一致）。

**例 16.2.1** 已知 $(x-1)y''-xy'+y=0$ 的一个解 $y_1=x$，求另一个线性无关解。令 $y_2=C(x)x$，代入得 $x(x-1)C''+(2x-2-x^2)C'=0$，

$$
\frac{\mathrm{d}C'}{C'}=\frac{x^2-2x+2}{x(x-1)}\,\mathrm{d}x=\Big(1+\frac{1}{x-1}-\frac2x\Big)\mathrm{d}x,\qquad C'=\frac{x-1}{x^2}\mathrm{e}^x=\Big(\frac1x-\frac1{x^2}\Big)\mathrm{e}^x.
$$
所以 $C=\dfrac{\mathrm{e}^x}{x}$，$y_2=\mathrm{e}^x$，与例 16.1.2（2）一致。

**例 16.2.2** 解 $x^2y''-2y=0$。观察出一个解 $y_1=x^2$（$2x^2-2x^2=0$）。令 $y_2=C(x)x^2$，代入得 $x^4C''+4x^3C'=0$，$C'=\dfrac1{x^4}$，$C=-\dfrac1{3x^3}$，取 $y_2=\dfrac1x$（常数因子可以去掉）。通解 $y=C_1x^2+\dfrac{C_2}x$。

### 16.2.2. 常数变易法

设已知齐次方程的基本解组 $y_1,y_2$，求非齐次方程 $y''+a_1y'+a_2y=f$ 的一个特解。仿照一阶方程，把通解 $C_1y_1+C_2y_2$ 中的常数换成函数：$Y=C_1(x)y_1+C_2(x)y_2$。两个未知函数只需满足一个方程，可以再加一个条件；选择

$$
C_1'y_1+C_2'y_2=0,
$$
使 $Y'=C_1y_1'+C_2y_2'$ 中不出现 $C_i'$。再求一次导数代入方程，利用 $y_1,y_2$ 是齐次解，得 $C_1'y_1'+C_2'y_2'=f$。

**算法 16.2.1（二阶方程的常数变易法）** 设 $y_1,y_2$ 是 $y''+a_1y'+a_2y=0$ 的基本解组。

1. 解线性方程组
   $$
   \begin{cases}C_1'y_1+C_2'y_2=0,\\ C_1'y_1'+C_2'y_2'=f(x),\end{cases}
   $$
   其系数行列式是 $W=W[y_1,y_2]\ne0$，由 Cramer 法则 $C_1'=-\dfrac{y_2f}{W}$，$C_2'=\dfrac{y_1f}{W}$；
2. 积分得 $C_1,C_2$（各取一个原函数），特解为 $Y=C_1y_1+C_2y_2$；若积分时保留常数，得到的就是通解。

注意方程必须先化为 $y''$ 的系数为 1 的标准形式，$f$ 指标准形式的右端。这与 [2.1.11](/2.1.11#sec-11.9) 中方程组的**常数变易法**是同一个方法（见 16.6.3）。

**例 16.2.3** 解 $y''+y=\sec x$（$\lvert x\rvert<\frac\pi2$）。$y_1=\cos x$，$y_2=\sin x$，$W=1$。

$$
\begin{cases}C_1'\cos x+C_2'\sin x=0,\\ -C_1'\sin x+C_2'\cos x=\sec x,\end{cases}\qquad C_1'=-\tan x,\quad C_2'=1.
$$
所以 $C_1=\ln\cos x$，$C_2=x$，通解为

$$
y=C_1\cos x+C_2\sin x+\cos x\ln\cos x+x\sin x.
$$
同理，$y''+y=\tan x$ 的一个特解是 $-\cos x\ln(\sec x+\tan x)$。

也可以只用一个齐次解 $y_1=\cos x$：令 $y=C(x)\cos x$ 代入，得 $C''\cos x-2C'\sin x=\sec x$，即 $C'$ 的一阶线性方程 $(C')'-2\tan x\,C'=\sec^2x$，解出 $C'=\dfrac{x+C_1}{\cos^2x}$，再积分得同样的通解。这说明只知道一个齐次解时，16.2.1 的方法直接作用于非齐次方程也能求出通解。

**例 16.2.4** 已知 $(x-1)y''-xy'+y=0$ 的通解为 $C_1x+C_2\mathrm{e}^x$，求 $(x-1)y''-xy'+y=(x-1)^2$ 的通解。标准形式的右端为 $f=x-1$，$W=(x-1)\mathrm{e}^x$。

$$
\begin{cases}C_1'x+C_2'\mathrm{e}^x=0,\\ C_1'+C_2'\mathrm{e}^x=x-1,\end{cases}\qquad C_1'=-1,\quad C_2'=x\mathrm{e}^{-x}.
$$
$C_1=-x$，$C_2=-(x+1)\mathrm{e}^{-x}$，特解 $Y=-x^2-(x+1)=-(x^2+x+1)$，通解 $y=C_1x+C_2\mathrm{e}^x-(x^2+x+1)$。

## 16.3. 常系数齐次线性方程

### 16.3.1. 微分算子与特征方程

记 $\mathrm{D}=\dfrac{\mathrm{d}}{\mathrm{d}x}$，$\mathrm{D}^ky=y^{(k)}$。对多项式 $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$（$a_k$ 为常数），定义 $P(\mathrm{D})=\mathrm{D}^n+a_1\mathrm{D}^{n-1}+\cdots+a_n$，则常系数线性方程写成

$$
P(\mathrm{D})y=y^{(n)}+a_1y^{(n-1)}+\cdots+a_{n-1}y'+a_ny=f(x).\tag{16.3}
$$
常系数算子的运算与多项式的运算一致：$P(\mathrm{D})Q(\mathrm{D})=(PQ)(\mathrm{D})$，并且可交换。所以 $P$ 的因式分解对应算子的分解，例如 $\mathrm{D}^2-3\mathrm{D}+2=(\mathrm{D}-1)(\mathrm{D}-2)$。

指数函数是 $\mathrm{D}$ 的"特征向量"：$\mathrm{D}\mathrm{e}^{\lambda x}=\lambda\mathrm{e}^{\lambda x}$，所以 $P(\mathrm{D})\mathrm{e}^{\lambda x}=P(\lambda)\mathrm{e}^{\lambda x}$。于是 $\mathrm{e}^{\lambda x}$ 是齐次方程的解当且仅当 $P(\lambda)=0$。

**定义 16.3.1** 代数方程 $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$ 称为常系数齐次方程 $P(\mathrm{D})y=0$ 的**特征方程**，它的根称为方程的**特征根**。

特征方程就是 16.6.5 中把方程化为方程组后系数矩阵（一个**友矩阵**，[2.1.6](/2.1.6)）的**特征多项式**等于零，特征根就是这个矩阵的特征值。

$\lambda$ 是 $k$ 重根时，只得到一个解 $\mathrm{e}^{\lambda x}$，还缺 $k-1$ 个。下面的引理是处理重根与非齐次方程的基本工具。

**引理 16.3.1（位移公式）** 设 $u(x)$ 有 $n$ 阶导数，$\lambda$ 是复数，则

$$
P(\mathrm{D})\big(\mathrm{e}^{\lambda x}u\big)=\mathrm{e}^{\lambda x}P(\mathrm{D}+\lambda)u.
$$

**证明** $\mathrm{D}(\mathrm{e}^{\lambda x}u)=\mathrm{e}^{\lambda x}(u'+\lambda u)=\mathrm{e}^{\lambda x}(\mathrm{D}+\lambda)u$，反复使用得 $\mathrm{D}^m(\mathrm{e}^{\lambda x}u)=\mathrm{e}^{\lambda x}(\mathrm{D}+\lambda)^mu$（也可由 **Leibniz 公式**与二项式定理得到），再作线性组合。 $\square$

这里允许 $\lambda$ 为复数：对 $\lambda=\alpha+\mathrm{i}\beta$，由**欧拉公式**定义 $\mathrm{e}^{\lambda x}=\mathrm{e}^{\alpha x}(\cos\beta x+\mathrm{i}\sin\beta x)$（[2.2.9](/2.2.9) 中由幂级数得到），复值函数逐实部、虚部求导，直接验证 $(\mathrm{e}^{\lambda x})'=\lambda\mathrm{e}^{\lambda x}$ 仍成立。由于 $P(\mathrm{D})$ 的系数是实数，复值函数 $z=u+\mathrm{i}v$ 满足 $P(\mathrm{D})z=g+\mathrm{i}h$ 当且仅当 $P(\mathrm{D})u=g$ 且 $P(\mathrm{D})v=h$：取实部、虚部即得实方程的解。

### 16.3.2. 基本解组

**定理 16.3.1** 设特征方程 $P(\lambda)=0$ 的互不相同的实根为 $\lambda_1,\dots,\lambda_r$，重数为 $m_1,\dots,m_r$；互不相同的共轭复根对为 $\alpha_j\pm\mathrm{i}\beta_j$（$\beta_j>0$），重数为 $l_j$（$j=1,\dots,s$），$\sum m_i+2\sum l_j=n$。则下列 $n$ 个函数构成 $P(\mathrm{D})y=0$ 的基本解组：

1. 每个 $m$ 重实根 $\lambda$ 对应 $\mathrm{e}^{\lambda x},\ x\mathrm{e}^{\lambda x},\ \dots,\ x^{m-1}\mathrm{e}^{\lambda x}$；
2. 每对 $l$ 重共轭复根 $\alpha\pm\mathrm{i}\beta$ 对应
   $$
   \mathrm{e}^{\alpha x}\cos\beta x,\ x\mathrm{e}^{\alpha x}\cos\beta x,\ \dots,\ x^{l-1}\mathrm{e}^{\alpha x}\cos\beta x;\qquad\mathrm{e}^{\alpha x}\sin\beta x,\ \dots,\ x^{l-1}\mathrm{e}^{\alpha x}\sin\beta x.
   $$

**证明** 是解：设 $\lambda$（实或复）是 $m$ 重根，则 $P(\mu)=(\mu-\lambda)^mR(\mu)$，$P(\mathrm{D}+\lambda)=\mathrm{D}^mR(\mathrm{D}+\lambda)$。由引理 16.3.1，对 $k<m$，

$$
P(\mathrm{D})(x^k\mathrm{e}^{\lambda x})=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^mx^k=0.
$$
复根 $\alpha+\mathrm{i}\beta$ 时 $x^k\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ 是复值解，它的实部 $x^k\mathrm{e}^{\alpha x}\cos\beta x$ 与虚部 $x^k\mathrm{e}^{\alpha x}\sin\beta x$ 都是实解。

线性无关：只需证明对互不相同的复数 $\mu_1,\dots,\mu_q$ 与多项式 $p_1,\dots,p_q$，$\sum_{j}p_j(x)\mathrm{e}^{\mu_jx}\equiv0$ 蕴含所有 $p_j\equiv0$（实函数组可由 $\mathrm{e}^{\mu x}$、$\mathrm{e}^{\bar\mu x}$ 线性表示，且表示可逆，所以复的线性无关性蕴含实的）。对 $q$ 归纳。$q=1$ 时显然。设 $q\ge2$，两边乘以 $\mathrm{e}^{-\mu_qx}$：$\sum_{j<q}p_j\mathrm{e}^{(\mu_j-\mu_q)x}+p_q\equiv0$。用 $\mathrm{D}^{d+1}$（$d=\deg p_q$）作用，$p_q$ 消失；由引理 16.3.1，$\mathrm{D}^{d+1}(p_j\mathrm{e}^{\nu x})=\mathrm{e}^{\nu x}(\mathrm{D}+\nu)^{d+1}p_j$，当 $\nu=\mu_j-\mu_q\ne0$ 时 $(\mathrm{D}+\nu)^{d+1}p_j$ 与 $p_j$ 次数相同（最高次项乘以 $\nu^{d+1}$）。由归纳假设这些多项式都为零，所以 $p_j\equiv0$（$j<q$），从而 $p_q\equiv0$。 $\square$

**算法 16.3.1（常系数齐次线性方程）** 求解 $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$：

1. 写出特征方程 $\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$，求出全部特征根及重数；
2. 按定理 16.3.1 写出 $n$ 个线性无关解，通解是它们的任意线性组合。

二阶方程 $y''+py'+qy=0$ 的三种情形：

| 判别式 $p^2-4q$ | 特征根 | 通解 |
|---|---|---|
| $>0$ | 两个不等实根 $\lambda_1,\lambda_2$ | $C_1\mathrm{e}^{\lambda_1x}+C_2\mathrm{e}^{\lambda_2x}$ |
| $=0$ | 二重实根 $\lambda=-\frac p2$ | $(C_1+C_2x)\mathrm{e}^{\lambda x}$ |
| $<0$ | 共轭复根 $\alpha\pm\mathrm{i}\beta$ | $\mathrm{e}^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$ |

**例 16.3.1** 求解下列各题。（1）$y^{(4)}-y=0$：$\lambda^4-1=0$，根 $\pm1$、$\pm\mathrm{i}$，通解 $C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+C_3\cos x+C_4\sin x$。

（2）$y'''-3y''+3y'-y=0$：$(\lambda-1)^3=0$，三重根 $1$，通解 $(C_1+C_2x+C_3x^2)\mathrm{e}^x$。

（3）$y^{(4)}+y''+y=0$：$\lambda^4+\lambda^2+1=(\lambda^2+1)^2-\lambda^2=(\lambda^2+\lambda+1)(\lambda^2-\lambda+1)$，根 $\dfrac{-1\pm\sqrt3\,\mathrm{i}}{2}$、$\dfrac{1\pm\sqrt3\,\mathrm{i}}{2}$，通解

$$
y=\mathrm{e}^{-x/2}\Big(C_1\cos\frac{\sqrt3}2x+C_2\sin\frac{\sqrt3}2x\Big)+\mathrm{e}^{x/2}\Big(C_3\cos\frac{\sqrt3}2x+C_4\sin\frac{\sqrt3}2x\Big).
$$

（4）$y^{(4)}-2y'''+5y''=0$：$\lambda^2(\lambda^2-2\lambda+5)=0$，根 $0$（二重）、$1\pm2\mathrm{i}$，通解 $C_1+C_2x+\mathrm{e}^x(C_3\cos2x+C_4\sin2x)$。

**例 16.3.2** 求以 $\mathrm{e}^{-x}$、$2x\mathrm{e}^{-x}$、$3\mathrm{e}^x$ 为解的三阶常系数齐次方程。由定理 16.3.1，$-1$ 至少是二重根，$1$ 是根，三阶方程的特征方程只能是 $(\lambda+1)^2(\lambda-1)=\lambda^3+\lambda^2-\lambda-1=0$，所求方程为 $y'''+y''-y'-y=0$。

## 16.4. 常系数非齐次方程

### 16.4.1. 待定系数法

当右端 $f$ 是多项式、指数函数、正弦余弦函数及其乘积时，特解与 $f$ 有相同的形式，可以设出含待定系数的特解代入求解。下面 $Q_m(x)$ 表示 $m$ 次多项式。

**定理 16.4.1** 设 $\lambda$ 是 $P(\lambda)=0$ 的 $k$ 重根（$\lambda$ 不是根时 $k=0$），$Q_m$ 是 $m$ 次多项式，则 $P(\mathrm{D})y=Q_m(x)\mathrm{e}^{\lambda x}$ 有形如

$$
y^*=x^kS_m(x)\mathrm{e}^{\lambda x}
$$
的特解，其中 $S_m$ 是待定的 $m$ 次多项式。

**证明** 写 $P(\mu)=(\mu-\lambda)^kR(\mu)$，$R(\lambda)\ne0$。由引理 16.3.1，$P(\mathrm{D})(x^kS\mathrm{e}^{\lambda x})=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^k(x^kS)$。$\mathrm{D}^k$ 把 $m+k$ 次多项式 $x^kS$ 映为 $m$ 次多项式，且 $x^kS\mapsto\mathrm{D}^k(x^kS)$ 是 $m$ 次多项式空间上的双射（比较最高次项，逐次确定系数）；$R(\mathrm{D}+\lambda)$ 的常数项 $R(\lambda)\ne0$，在多项式上也是可逆的（比较系数可从最高次向下逐个解出）。所以方程 $R(\mathrm{D}+\lambda)\mathrm{D}^k(x^kS)=Q_m$ 有唯一的 $m$ 次多项式解 $S$。 $\square$

右端为 $Q_m(x)\mathrm{e}^{\alpha x}\cos\beta x$ 或 $Q_m(x)\mathrm{e}^{\alpha x}\sin\beta x$ 时，它们是 $Q_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ 的实部与虚部。按定理 16.4.1 求复方程的特解，再取实部或虚部即可；也可以直接设实形式的特解。

**算法 16.4.1（待定系数法）** 求 $P(\mathrm{D})y=f(x)$ 的特解。按下表设出特解，代入方程比较系数；$f$ 是几项之和时按叠加原理分别求解再相加。

| 右端 $f(x)$ | 特解形式 | $k$ 的取法 |
|---|---|---|
| $Q_m(x)$ | $x^kS_m(x)$ | $0$ 作为特征根的重数 |
| $Q_m(x)\mathrm{e}^{\lambda x}$ | $x^kS_m(x)\mathrm{e}^{\lambda x}$ | $\lambda$ 作为特征根的重数 |
| $\mathrm{e}^{\alpha x}\big(Q_m(x)\cos\beta x+\tilde Q_l(x)\sin\beta x\big)$ | $x^k\mathrm{e}^{\alpha x}\big(S_M(x)\cos\beta x+T_M(x)\sin\beta x\big)$，$M=\max\{m,l\}$ | $\alpha+\mathrm{i}\beta$ 作为特征根的重数 |
| 同上（复指数法） | 求 $P(\mathrm{D})z=Q_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$ 的特解 $x^kS_m(x)\mathrm{e}^{(\alpha+\mathrm{i}\beta)x}$，取实部（对 $\cos$）或虚部（对 $\sin$） | 同上 |

第三行中即使 $f$ 只含 $\cos\beta x$，特解也要同时设 $\cos\beta x$ 与 $\sin\beta x$ 两项。

**例 16.4.1** 解 $y''-y=2x\mathrm{e}^x$。特征根 $\pm1$，$1$ 是单根，设 $y^*=x(ax+b)\mathrm{e}^x$。由引理 16.3.1，

$$
(\mathrm{D}^2-1)\big((ax^2+bx)\mathrm{e}^x\big)=\mathrm{e}^x\big((\mathrm{D}+1)^2-1\big)(ax^2+bx)=\mathrm{e}^x(\mathrm{D}^2+2\mathrm{D})(ax^2+bx)=\mathrm{e}^x(4ax+2a+2b),
$$
比较系数 $4a=2$，$2a+2b=0$，得 $a=\frac12$，$b=-\frac12$。通解 $y=C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+\dfrac{x^2-x}2\mathrm{e}^x$。

（位移公式把"代入后求两次导数"变成了对多项式的运算，比直接代入简洁。）

**例 16.4.2** 解 $y''-2y'+y=4x\mathrm{e}^x$。$1$ 是二重特征根，设 $y^*=x^2(ax+b)\mathrm{e}^x$，则 $(\mathrm{D}-1)^2(x^2(ax+b)\mathrm{e}^x)=\mathrm{e}^x\mathrm{D}^2(ax^3+bx^2)=\mathrm{e}^x(6ax+2b)$，得 $a=\frac23$，$b=0$。通解 $y=(C_1+C_2x)\mathrm{e}^x+\dfrac23x^3\mathrm{e}^x$。

**例 16.4.3** 解 $y''-2y'+4y=\cos x+\mathrm{e}^x\sin x$。特征根 $1\pm\sqrt3\,\mathrm{i}$。

- 对 $\cos x$：$\mathrm{i}$ 不是特征根，求 $P(\mathrm{D})z=\mathrm{e}^{\mathrm{i}x}$ 的特解 $z=\dfrac{\mathrm{e}^{\mathrm{i}x}}{P(\mathrm{i})}=\dfrac{\mathrm{e}^{\mathrm{i}x}}{3-2\mathrm{i}}=\dfrac{(3+2\mathrm{i})(\cos x+\mathrm{i}\sin x)}{13}$，实部 $\dfrac{3\cos x-2\sin x}{13}$ 是 $P(\mathrm{D})y=\cos x$ 的特解；
- 对 $\mathrm{e}^x\sin x$：$1+\mathrm{i}$ 不是特征根，$P(1+\mathrm{i})=(1+\mathrm{i})^2-2(1+\mathrm{i})+4=2$，$z=\dfrac12\mathrm{e}^{(1+\mathrm{i})x}$，虚部 $\dfrac12\mathrm{e}^x\sin x$。

通解 $y=\mathrm{e}^x(C_1\cos\sqrt3x+C_2\sin\sqrt3x)+\dfrac{3\cos x-2\sin x}{13}+\dfrac12\mathrm{e}^x\sin x$。

**例 16.4.4** 解 $y''+9y=18\cos3x+30\sin3x$。$3\mathrm{i}$ 是单特征根，求 $(\mathrm{D}^2+9)z=\mathrm{e}^{3\mathrm{i}x}$ 的特解 $z=Ax\mathrm{e}^{3\mathrm{i}x}$。由引理 16.3.1，$(\mathrm{D}^2+9)(Ax\mathrm{e}^{3\mathrm{i}x})=\mathrm{e}^{3\mathrm{i}x}\big((\mathrm{D}+3\mathrm{i})^2+9\big)(Ax)=\mathrm{e}^{3\mathrm{i}x}(\mathrm{D}^2+6\mathrm{i}\mathrm{D})(Ax)=6\mathrm{i}A\mathrm{e}^{3\mathrm{i}x}$，所以 $A=\dfrac{1}{6\mathrm{i}}=-\dfrac{\mathrm{i}}{6}$，

$$
z=-\frac{\mathrm{i}}{6}x(\cos3x+\mathrm{i}\sin3x)=\frac x6(\sin3x-\mathrm{i}\cos3x).
$$
$\cos3x$ 对应实部 $\frac x6\sin3x$，$\sin3x$ 对应虚部 $-\frac x6\cos3x$。通解

$$
y=C_1\cos3x+C_2\sin3x+x(3\sin3x-5\cos3x).
$$

**例 16.4.5** 解 $y''+y=x\cos2x$。$2\mathrm{i}$ 不是特征根，设 $y^*=(a_1x+b_1)\cos2x+(a_2x+b_2)\sin2x$，代入得

$$
(-3a_1x-3b_1+4a_2)\cos2x+(-3a_2x-3b_2-4a_1)\sin2x=x\cos2x,
$$
比较系数 $a_1=-\frac13$，$a_2=0$，$b_1=0$，$b_2=\frac49$。通解 $y=C_1\cos x+C_2\sin x-\dfrac13x\cos2x+\dfrac49\sin2x$。

**例 16.4.6** 写出 $y''+2y'-3y=3\mathrm{e}^x+\sin2x+\mathrm{e}^x\cos2x$ 的特解形式。特征根 $1,-3$。三项分别对应 $\lambda=1$（单根，$k=1$）、$2\mathrm{i}$（$k=0$）、$1+2\mathrm{i}$（$k=0$），特解形式为

$$
y^*=Ax\mathrm{e}^x+(B\cos2x+C\sin2x)+\mathrm{e}^x(D\cos2x+E\sin2x).
$$

### 16.4.2. 微分算子法

把 $P(\mathrm{D})$ 当作多项式来分解和"求逆"，是求特解的另一套方法，称为**微分算子法**。

方法（1）：逐次降阶（"剥皮"）。实系数多项式 $P$ 可以分解为一次与二次实因式的乘积。若 $P(\mathrm{D})=(\mathrm{D}-\lambda_1)R(\mathrm{D})$，令 $z=R(\mathrm{D})y$，先解一阶线性方程 $z'-\lambda_1z=f$（公式 (15.3)），再解低一阶的方程 $R(\mathrm{D})y=z$；二次因式 $\mathrm{D}^2+s\mathrm{D}+t$ 同样处理，用二阶方程的常数变易法。每一步都只用到一阶、二阶方程的解法，所以理论上任何常系数非齐次方程都能解出。这一方法对右端没有限制。

**例 16.4.7** 求解下列各题。（1）$y''-y=2x\mathrm{e}^x$：$(\mathrm{D}-1)(\mathrm{D}+1)y=2x\mathrm{e}^x$。令 $z=(\mathrm{D}+1)y$，$z'-z=2x\mathrm{e}^x$，$z=\mathrm{e}^x\int2x\,\mathrm{d}x=x^2\mathrm{e}^x$（取一个特解）。再解 $y'+y=x^2\mathrm{e}^x$：$y=\mathrm{e}^{-x}\int x^2\mathrm{e}^{2x}\,\mathrm{d}x=\Big(\dfrac{x^2}2-\dfrac x2+\dfrac14\Big)\mathrm{e}^x$。其中 $\frac14\mathrm{e}^x$ 是齐次解，可以去掉，与例 16.4.1 一致。

（2）$y'''+y'=\sec x$：令 $z=y'$，$z''+z=\sec x$，由例 16.2.3，$z=\cos x\ln\cos x+x\sin x$。积分得特解

$$
y=\int(\cos x\ln\cos x+x\sin x)\,\mathrm{d}x=\sin x\ln\cos x-x\cos x+\ln(\sec x+\tan x),
$$
其中 $\int\cos x\ln\cos x\,\mathrm{d}x=\sin x\ln\cos x+\int\frac{\sin^2x}{\cos x}\,\mathrm{d}x=\sin x\ln\cos x-\sin x+\ln(\sec x+\tan x)$，$\int x\sin x\,\mathrm{d}x=-x\cos x+\sin x$。通解 $y=C_1+C_2\cos x+C_3\sin x+\sin x\ln\cos x-x\cos x+\ln(\sec x+\tan x)$。

方法（2）：右端为指数函数。由 $P(\mathrm{D})\mathrm{e}^{\lambda x}=P(\lambda)\mathrm{e}^{\lambda x}$ 与引理 16.3.1：

**命题 16.4.1** 若 $P(\lambda)\ne0$，则 $\dfrac{\mathrm{e}^{\lambda x}}{P(\lambda)}$ 是 $P(\mathrm{D})y=\mathrm{e}^{\lambda x}$ 的特解。若 $\lambda$ 是 $k$ 重根，$P(\mu)=(\mu-\lambda)^kR(\mu)$，则 $\dfrac{x^k\mathrm{e}^{\lambda x}}{k!\,R(\lambda)}$ 是特解。

**证明** 第一条直接验证。第二条：$P(\mathrm{D})\big(x^k\mathrm{e}^{\lambda x}\big)=\mathrm{e}^{\lambda x}R(\mathrm{D}+\lambda)\mathrm{D}^kx^k=k!\,R(\lambda)\mathrm{e}^{\lambda x}$，因为 $\mathrm{D}^kx^k=k!$ 是常数，$R(\mathrm{D}+\lambda)$ 作用于常数只剩常数项 $R(\lambda)$。 $\square$

**例 16.4.8** 求解下列各题。（1）$y'''-2y''-5y'+6y=\mathrm{e}^{4x}$：$P(\lambda)=(\lambda-1)(\lambda-3)(\lambda+2)$，$P(4)=18$，特解 $\dfrac{\mathrm{e}^{4x}}{18}$，通解 $C_1\mathrm{e}^x+C_2\mathrm{e}^{3x}+C_3\mathrm{e}^{-2x}+\dfrac{\mathrm{e}^{4x}}{18}$。

（2）同一个算子，$y'''-2y''-5y'+6y=(\mathrm{e}^{2x}+3)^2=\mathrm{e}^{4x}+6\mathrm{e}^{2x}+9$：$P(2)=-4$，$P(0)=6$，特解 $\dfrac{\mathrm{e}^{4x}}{18}-\dfrac32\mathrm{e}^{2x}+\dfrac32$。

（3）$y^{(4)}-y=\mathrm{e}^x$：$1$ 是单根，$P(\mu)=(\mu-1)(\mu+1)(\mu^2+1)$，$R(1)=4$，特解 $\dfrac{x\mathrm{e}^x}4$，通解 $C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}+C_3\cos x+C_4\sin x+\dfrac{x\mathrm{e}^x}{4}$。

（4）$y''+y'-2y=2\sin x$：$P(\mathrm{i})=-3+\mathrm{i}$，$\dfrac{2\mathrm{e}^{\mathrm{i}x}}{-3+\mathrm{i}}=-\dfrac{(3+\mathrm{i})(\cos x+\mathrm{i}\sin x)}{5}$，取虚部得特解 $-\dfrac{\cos x+3\sin x}5$。

方法（3）：右端为多项式。若 $f$ 是 $m$ 次多项式且 $P(0)\ne0$，把 $\dfrac1{P(\lambda)}$ 在 $\lambda=0$ 处展开为幂级数 $b_0+b_1\lambda+b_2\lambda^2+\cdots$（用长除法，按升幂排列），则

$$
y^*=\big(b_0+b_1\mathrm{D}+\cdots+b_m\mathrm{D}^m\big)f
$$
是 $P(\mathrm{D})y=f$ 的特解：因为 $P(\lambda)(b_0+\cdots+b_m\lambda^m)=1+O(\lambda^{m+1})$，而 $\mathrm{D}^{m+1}f=0$。若 $0$ 是 $k$ 重根，$P(\mathrm{D})=\mathrm{D}^kR(\mathrm{D})$，先对 $R$ 这样求出 $R(\mathrm{D})u=f$ 的多项式解 $u$，再积分 $k$ 次。

**例 16.4.9** 解 $2y''+2y'+3y=x^2+2x-1$。$\dfrac{1}{3+2\lambda+2\lambda^2}=\dfrac13-\dfrac29\lambda-\dfrac2{27}\lambda^2+\cdots$，所以

$$
y^*=\Big(\frac13-\frac29\mathrm{D}-\frac2{27}\mathrm{D}^2\Big)(x^2+2x-1)=\frac{x^2+2x-1}3-\frac29(2x+2)-\frac4{27}=\frac13x^2+\frac29x-\frac{25}{27}.
$$
特征根 $\dfrac{-1\pm\sqrt5\,\mathrm{i}}{2}$，通解 $y=\mathrm{e}^{-x/2}\Big(C_1\cos\dfrac{\sqrt5}2x+C_2\sin\dfrac{\sqrt5}2x\Big)+\dfrac13x^2+\dfrac29x-\dfrac{25}{27}$。

### 16.4.3. Euler 方程

**定义 16.4.1** 形如

$$
x^ny^{(n)}+a_1x^{n-1}y^{(n-1)}+\cdots+a_{n-1}xy'+a_ny=f(x)\qquad(a_k\text{ 为常数})
$$
的方程称为 **Euler 方程**。

它是变系数方程，但 $x^ky^{(k)}$ 在伸缩 $x\mapsto cx$ 下不变，换元 $x=\mathrm{e}^t$ 可以化为常系数方程。

**命题 16.4.2** 设 $x>0$，令 $x=\mathrm{e}^t$，记 $\mathrm{D}=\dfrac{\mathrm{d}}{\mathrm{d}t}$，则

$$
x^k\frac{\mathrm{d}^ky}{\mathrm{d}x^k}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y.
$$

**证明** $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}y}{\mathrm{d}t}\cdot\dfrac{\mathrm{d}t}{\mathrm{d}x}=\dfrac1x\mathrm{D}y$，即 $k=1$ 成立。设对 $k$ 成立，即 $x^ky^{(k)}=Q_k(\mathrm{D})y$，$Q_k(\mathrm{D})=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)$。两边对 $x$ 求导再乘以 $x$：左边为 $kx^ky^{(k)}+x^{k+1}y^{(k+1)}$，右边为 $x\cdot\dfrac1x\mathrm{D}Q_k(\mathrm{D})y$。所以 $x^{k+1}y^{(k+1)}=(\mathrm{D}-k)Q_k(\mathrm{D})y=Q_{k+1}(\mathrm{D})y$。 $\square$

$x<0$ 时令 $x=-\mathrm{e}^t$，结果相同，所以最后答案中的 $\ln x$ 可写成 $\ln\lvert x\rvert$。

**算法 16.4.2（Euler 方程）** 令 $x=\mathrm{e}^t$，把 $x^ky^{(k)}$ 换成 $\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y$，得到常系数方程 $P(\mathrm{D})y=f(\mathrm{e}^t)$；用 16.3、16.4 的方法求解后以 $t=\ln x$ 代回。齐次方程的解 $t^j\mathrm{e}^{\lambda t}$ 代回为 $x^\lambda\ln^jx$，所以也可以直接设 $y=x^\lambda$ 代入齐次方程求 $\lambda$。

**例 16.4.10** 求解下列各题。（1）解 $x^3y'''+3x^2y''-2xy'+2y=0$。$[\mathrm{D}(\mathrm{D}-1)(\mathrm{D}-2)+3\mathrm{D}(\mathrm{D}-1)-2\mathrm{D}+2]y=(\mathrm{D}^3-3\mathrm{D}+2)y=(\mathrm{D}-1)^2(\mathrm{D}+2)y=0$，所以 $y=C_1\mathrm{e}^t+C_2t\mathrm{e}^t+C_3\mathrm{e}^{-2t}=C_1x+C_2x\ln x+\dfrac{C_3}{x^2}$。

（2）解 $x^2y''-xy'+4y=\cos\ln x+x\sin\ln x$。化为 $(\mathrm{D}^2-2\mathrm{D}+4)y=\cos t+\mathrm{e}^t\sin t$，与例 16.4.3 的方程相同（自变量换成 $t$），所以

$$
y=x\big(C_1\cos(\sqrt3\ln x)+C_2\sin(\sqrt3\ln x)\big)+\frac{3\cos\ln x-2\sin\ln x}{13}+\frac x2\sin\ln x.
$$

（3）解 $x^2y''+3xy'-8y=25x\ln x$。化为 $(\mathrm{D}^2+2\mathrm{D}-8)y=25t\mathrm{e}^t$，特征根 $2,-4$。$1$ 不是根，设 $y^*=(at+b)\mathrm{e}^t$，由引理 16.3.1，$(\mathrm{D}^2+2\mathrm{D}-8)\big((at+b)\mathrm{e}^t\big)=\mathrm{e}^t(\mathrm{D}^2+4\mathrm{D}-5)(at+b)=\mathrm{e}^t(-5at+4a-5b)$，得 $a=-5$，$b=-4$。所以

$$
y=C_1x^2+\frac{C_2}{x^4}-x(5\ln x+4).
$$

## 16.5. 振动问题

质量为 $m$ 的物体系在弹簧上，在有阻力的介质中沿直线运动。设 $x(t)$ 为偏离平衡位置的位移，弹性恢复力 $-hx$（Hooke 定律），阻力 $-cx'$ 与速度成正比，外力 $F(t)$。由 Newton 第二定律 $mx''=-hx-cx'+F(t)$，记 $\omega^2=h/m$，$2k=c/m$，$f=F/m$：

$$
x''+2kx'+\omega^2x=f(t),\qquad\omega>0,\ k\ge0.\tag{16.4}
$$
电路中 RLC 串联回路的电荷满足同样的方程。

### 16.5.1. 自由振动

$f=0$ 的情形。特征方程 $\lambda^2+2k\lambda+\omega^2=0$，$\lambda=-k\pm\sqrt{k^2-\omega^2}$。

- 无阻尼（$k=0$）：$x=C_1\cos\omega t+C_2\sin\omega t=A\sin(\omega t+\theta)$，其中振幅 $A=\sqrt{C_1^2+C_2^2}$，初相 $\theta$ 满足 $\sin\theta=C_1/A$，$\cos\theta=C_2/A$。这是周期为 $2\pi/\omega$ 的简谐振动，$\omega$ 称为固有频率。
- 欠阻尼（$0<k<\omega$，弱阻尼）：$x=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)$，振动的振幅按指数衰减，频率变为 $\sqrt{\omega^2-k^2}<\omega$。
- 临界阻尼（$k=\omega$）：$x=(C_1+C_2t)\mathrm{e}^{-\omega t}$，不再振动，回到平衡位置最快。
- 过阻尼（$k>\omega$，强阻尼）：$x=C_1\mathrm{e}^{(-k+\sqrt{k^2-\omega^2})t}+C_2\mathrm{e}^{(-k-\sqrt{k^2-\omega^2})t}$，两个指数都为负，单调地（至多越过平衡位置一次）缓慢回到平衡位置。

![x'' + 2k x' + x = 0 在初值 x(0) = 1, x'(0) = 0 下的三种阻尼情形：欠阻尼 k = 0.15 时振幅按 e^{-kt}（虚线包络）衰减；临界阻尼 k = 1 时最快回到平衡位置；过阻尼 k = 2.5 时缓慢回到平衡位置](./plots/damped-oscillation.py)

### 16.5.2. 强迫振动与共振

设外力是周期力 $f(t)=H\sin pt$。

无阻尼（$k=0$）的情形。方程 $x''+\omega^2x=H\sin pt$。

- $p\ne\omega$：$\mathrm{i}p$ 不是特征根，由命题 16.4.1，$\dfrac{\mathrm{e}^{\mathrm{i}pt}}{\omega^2-p^2}$ 的虚部给出特解，通解
  $$
  x=A\sin(\omega t+\theta)+\frac{H}{\omega^2-p^2}\sin pt,
  $$
  是固有振动与强迫振动的叠加。$p$ 越接近 $\omega$，强迫振动的振幅越大。
- $p=\omega$：$\mathrm{i}\omega$ 是单根，由命题 16.4.1，$\dfrac{t\mathrm{e}^{\mathrm{i}\omega t}}{2\mathrm{i}\omega}$ 的虚部 $-\dfrac{t\cos\omega t}{2\omega}$ 给出特解，通解
  $$
  x=A\sin(\omega t+\theta)-\frac{H}{2\omega}t\cos\omega t.
  $$
  振幅随时间线性增长，没有上界。外力频率等于固有频率时振幅无限增大的现象称为共振（resonance）。

有阻尼（$0<k<\omega$）的情形。$\mathrm{i}p$ 不是特征根，$P(\mathrm{i}p)=\omega^2-p^2+2kp\,\mathrm{i}$，

$$
\frac{\mathrm{e}^{\mathrm{i}pt}}{\omega^2-p^2+2kp\,\mathrm{i}}=\frac{\big((\omega^2-p^2)-2kp\,\mathrm{i}\big)(\cos pt+\mathrm{i}\sin pt)}{(\omega^2-p^2)^2+4k^2p^2},
$$
取虚部，通解为

$$
x=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)+H\frac{(\omega^2-p^2)\sin pt-2kp\cos pt}{(\omega^2-p^2)^2+4k^2p^2}
=A\mathrm{e}^{-kt}\sin\big(\sqrt{\omega^2-k^2}\,t+\theta\big)+\frac{H}{\sqrt{(\omega^2-p^2)^2+4k^2p^2}}\sin(pt-\varphi),
$$
其中 $\tan\varphi=\dfrac{2kp}{\omega^2-p^2}$。第一项随时间衰减（暂态），第二项是与外力同频率、振幅有界的稳态振动：有阻尼时不会出现振幅无限增大。稳态振幅

$$
A(p)=\frac{H}{\sqrt{(\omega^2-p^2)^2+4k^2p^2}}
$$
作为 $p$ 的函数，当 $k<\omega/\sqrt2$ 时在 $p=\sqrt{\omega^2-2k^2}$ 处取最大值 $\dfrac{H}{2k\sqrt{\omega^2-k^2}}$（对 $(\omega^2-p^2)^2+4k^2p^2$ 关于 $p^2$ 求最小值即得）。阻尼越小，峰越高越尖，峰值位置越接近 $\omega$；$k\to0$ 时回到无阻尼的共振。

![左：稳态振幅 A(p) 与驱动频率 p 的关系（H = 1, ω = 1），阻尼越小共振峰越高、越接近 p = ω；右：无阻尼共振 x'' + x = sin t 的特解 -(t cos t)/2，振幅线性增长](./plots/resonance.py)

## 16.6. 线性微分方程组

### 16.6.1. 一般概念

设 $A(t)=(a_{ij}(t))$ 是 $n\times n$ 函数矩阵，$\boldsymbol{f}(t)=(f_1(t),\dots,f_n(t))^{\mathsf T}$，$\boldsymbol{x}(t)=(x_1(t),\dots,x_n(t))^{\mathsf T}$ 是未知函数向量。函数矩阵的连续、导数、积分都逐个元素定义（[2.1.11](/2.1.11#sec-11.1)）。

**定义 16.6.1** 方程组

$$
\begin{cases}x_1'=a_{11}(t)x_1+\cdots+a_{1n}(t)x_n+f_1(t),\\ \quad\vdots\\ x_n'=a_{n1}(t)x_1+\cdots+a_{nn}(t)x_n+f_n(t)\end{cases}
\qquad\text{即}\qquad\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)\tag{16.5}
$$
称为（一阶）**线性微分方程组**；$\boldsymbol{f}\equiv\boldsymbol{0}$ 时

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}\tag{16.6}
$$
称为齐次方程组。$A$ 是常数矩阵时称为常系数线性方程组。

**定理 16.6.1** 若 $A(t)$、$\boldsymbol{f}(t)$ 在区间 $I$ 上连续，则对任意 $t_0\in I$、$\boldsymbol{\eta}\in\mathbb{R}^n$，初值问题 $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$，$\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ 在整个 $I$ 上存在唯一解。

函数矩阵的求导满足乘积法则 $(AB)'=A'B+AB'$，但行列式的导数不是导数的行列式：$\dfrac{\mathrm{d}}{\mathrm{d}t}\det A(t)$ 等于把 $\det A(t)$ 的第 $i$ 行换成该行的导数所得的 $n$ 个行列式之和（$i=1,\dots,n$），这由行列式对每一行的线性与乘积法则得到。下面计算 Wronski 行列式的导数时要用到它。

### 16.6.2. 解的结构

与 16.1 节完全平行。函数向量组 $\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t)$ 的线性相关与无关按 [2.1.11 的定义 11.2.1](/2.1.11#def-11.2.1)（系数为常数）；称

$$
W(t)=\det\big(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t)\big)
$$
为它们的 **Wronski 行列式**。若它们线性相关，则 $W\equiv0$。

**定理 16.6.2** 设 $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ 是齐次方程组 (16.6) 在 $I$ 上的解。

1. 若存在 $t_0\in I$ 使 $W(t_0)=0$，则 $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ 线性相关，从而 $W\equiv0$；因此 $W$ 恒为零或处处不为零；
2. （Liouville 公式）$W(t)=W(t_0)\,\mathrm{e}^{\int_{t_0}^t\operatorname{tr}(A(s))\,\mathrm{d}s}$。

**证明** （1）$W(t_0)=0$，存在不全为零的 $c_1,\dots,c_n$ 使 $\sum c_k\boldsymbol{\varphi}_k(t_0)=\boldsymbol{0}$。$\sum c_k\boldsymbol{\varphi}_k(t)$ 与 $\boldsymbol{0}$ 都是 (16.6) 满足 $\boldsymbol{x}(t_0)=\boldsymbol{0}$ 的解，由唯一性 $\sum c_k\boldsymbol{\varphi}_k\equiv\boldsymbol{0}$。（2）记 $\Phi=(\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n)$，按上面的行列式求导法则，第 $i$ 行的导数是 $\sum_ja_{ij}(\text{第 }j\text{ 行})$，换进去后减去 $j\ne i$ 的倍数行，只剩 $a_{ii}\det\Phi$。所以 $W'=\operatorname{tr}(A)W$，解这个一阶线性方程即得。 $\square$

**定理 16.6.3** 齐次方程组 (16.6) 的解集是 $n$ 维线性空间。

**证明** 取 $\boldsymbol{\varphi}_k$ 为满足 $\boldsymbol{\varphi}_k(t_0)=\boldsymbol{e}_k$ 的解，则 $W(t_0)=1$，它们线性无关；任一解 $\boldsymbol{\varphi}$ 与 $\sum_k\eta_k\boldsymbol{\varphi}_k$（$\boldsymbol{\eta}=\boldsymbol{\varphi}(t_0)$）满足同样的初始条件，由唯一性两者相等。 $\square$

**定义 16.6.2** 方程组 (16.6) 的 $n$ 个线性无关解称为它的一个**基本解组**；以基本解组为列的矩阵 $\Phi(t)=(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t))$ 称为**基解矩阵**。

$\Phi$ 是基解矩阵当且仅当 $\Phi'=A\Phi$ 且 $\det\Phi(t)\ne0$。齐次方程组的通解是 $\boldsymbol{x}=\Phi(t)\boldsymbol{c}$，$\boldsymbol{c}$ 为任意常向量；满足 $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$ 的解为

$$
\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}_0,
$$
因为 $\boldsymbol{c}$ 由 $\Phi(t_0)\boldsymbol{c}=\boldsymbol{x}_0$ 唯一确定。常系数时 $\mathrm{e}^{tA}$ 就是满足 $\Phi(0)=I$ 的基解矩阵（[2.1.11 的定理 11.9.1](/2.1.11#thm-11.9.1)），任何基解矩阵都满足 $\Phi(t)\Phi^{-1}(0)=\mathrm{e}^{tA}$，Liouville 公式成为 $\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$。

**例 16.6.1** 求解下列各题。（1）解 $\boldsymbol{x}'=\begin{bmatrix}1&1\\0&1\end{bmatrix}\boldsymbol{x}$。第二个方程 $x_2'=x_2$ 得 $x_2=C_2\mathrm{e}^t$；代入第一个方程 $x_1'-x_1=C_2\mathrm{e}^t$，由公式 (15.3) 得 $x_1=\mathrm{e}^t(C_2t+C_1)$。所以

$$
\boldsymbol{x}=C_1\begin{bmatrix}\mathrm{e}^t\\0\end{bmatrix}+C_2\begin{bmatrix}t\mathrm{e}^t\\ \mathrm{e}^t\end{bmatrix},\qquad\Phi(t)=\begin{bmatrix}\mathrm{e}^t&t\mathrm{e}^t\\0&\mathrm{e}^t\end{bmatrix},\quad\det\Phi=\mathrm{e}^{2t}=\mathrm{e}^{t\operatorname{tr}(A)}.
$$

（2）求满足 $\boldsymbol{x}(0)=(3,2)^{\mathsf T}$ 的解。$\Phi(0)=I$，所以 $\boldsymbol{x}=\Phi(t)\boldsymbol{x}(0)=\big((3+2t)\mathrm{e}^t,\ 2\mathrm{e}^t\big)^{\mathsf T}$。这里 $\Phi(t)=\mathrm{e}^{tA}$，$A$ 是一个 Jordan 块，$t\mathrm{e}^t$ 一项来自 Jordan 链（[2.1.11 的推论 11.9.1](/2.1.11#cor-11.9.1)）。

### 16.6.3. 非齐次方程组与常数变易法

由叠加原理，非齐次方程组 (16.5) 的通解等于它的一个特解加上齐次方程组的通解。特解仍用常数变易法求：

**定理 16.6.4** 设 $\Phi(t)$ 是 (16.6) 的基解矩阵，则 (16.5) 的通解为

$$
\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s.\tag{16.7}
$$

**证明** 令 $\boldsymbol{x}=\Phi(t)\boldsymbol{c}(t)$，则 $\boldsymbol{x}'=\Phi'\boldsymbol{c}+\Phi\boldsymbol{c}'=A\Phi\boldsymbol{c}+\Phi\boldsymbol{c}'$。代入 (16.5) 得 $\Phi\boldsymbol{c}'=\boldsymbol{f}$，$\boldsymbol{c}'=\Phi^{-1}\boldsymbol{f}$，积分即得。 $\square$

$\Phi=\mathrm{e}^{tA}$ 时 $\Phi(t)\Phi^{-1}(s)=\mathrm{e}^{(t-s)A}$，式 (16.7) 就是 [2.1.11](/2.1.11#sec-11.9) 的**常数变易公式**。对二阶方程 $y''+a_1y'+a_2y=f$，取 $\boldsymbol{x}=(y,y')^{\mathsf T}$，式 (16.7) 中的 $\Phi^{-1}\boldsymbol{f}$ 恰好就是算法 16.2.1 中由 Cramer 法则解出的 $(C_1',C_2')^{\mathsf T}$。

**例 16.6.2** 解 $\boldsymbol{x}'=\begin{bmatrix}1&1\\0&1\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}\mathrm{e}^{-t}\\0\end{bmatrix}$，$\boldsymbol{x}(0)=\begin{bmatrix}-1\\1\end{bmatrix}$。由例 16.6.1，$\Phi(t)=\begin{bmatrix}\mathrm{e}^t&t\mathrm{e}^t\\0&\mathrm{e}^t\end{bmatrix}$，$\Phi^{-1}(s)=\begin{bmatrix}\mathrm{e}^{-s}&-s\mathrm{e}^{-s}\\0&\mathrm{e}^{-s}\end{bmatrix}$，

$$
\int_0^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s=\int_0^t\begin{bmatrix}\mathrm{e}^{-2s}\\0\end{bmatrix}\mathrm{d}s=\begin{bmatrix}\frac{1-\mathrm{e}^{-2t}}{2}\\0\end{bmatrix}.
$$
由 $\boldsymbol{x}(0)=\Phi(0)\boldsymbol{c}=\boldsymbol{c}$ 得 $\boldsymbol{c}=(-1,1)^{\mathsf T}$，所以

$$
\boldsymbol{x}(t)=\Phi(t)\begin{bmatrix}-\frac12-\frac12\mathrm{e}^{-2t}\\1\end{bmatrix}=\begin{bmatrix}t\mathrm{e}^t-\frac{\mathrm{e}^t+\mathrm{e}^{-t}}{2}\\ \mathrm{e}^t\end{bmatrix}.
$$

### 16.6.4. 常系数齐次方程组

对常系数方程组 $\boldsymbol{x}'=A\boldsymbol{x}$，仿照 $n$ 阶方程试探 $\boldsymbol{x}=\mathrm{e}^{\lambda t}\boldsymbol{r}$（$\boldsymbol{r}\ne\boldsymbol{0}$ 为常向量），代入得 $\lambda\mathrm{e}^{\lambda t}\boldsymbol{r}=\mathrm{e}^{\lambda t}A\boldsymbol{r}$，即 $A\boldsymbol{r}=\lambda\boldsymbol{r}$：$\mathrm{e}^{\lambda t}\boldsymbol{r}$ 是解当且仅当 $(\lambda,\boldsymbol{r})$ 是 $A$ 的特征值与特征向量。$\lambda$ 是**特征多项式** $\det(\lambda I-A)$ 的根。

**定理 16.6.5** 若 $A$ 有 $n$ 个线性无关的特征向量 $\boldsymbol{r}_1,\dots,\boldsymbol{r}_n$（即 $A$ **可对角化**），对应的特征值为 $\lambda_1,\dots,\lambda_n$，则 $\mathrm{e}^{\lambda_1t}\boldsymbol{r}_1,\dots,\mathrm{e}^{\lambda_nt}\boldsymbol{r}_n$ 是 $\boldsymbol{x}'=A\boldsymbol{x}$ 的基本解组。

**证明** 每个都是解（见上）；$t=0$ 处的 Wronski 行列式 $\det(\boldsymbol{r}_1,\dots,\boldsymbol{r}_n)\ne0$，由定理 16.6.2 线性无关。 $\square$

$A$ 是实矩阵、$\lambda=\alpha+\mathrm{i}\beta$（$\beta\ne0$）是复特征值、$\boldsymbol{r}=\boldsymbol{a}+\mathrm{i}\boldsymbol{b}$ 是对应的特征向量时，$\mathrm{e}^{\lambda t}\boldsymbol{r}$ 是复值解，它的实部与虚部

$$
\mathrm{e}^{\alpha t}\big(\boldsymbol{a}\cos\beta t-\boldsymbol{b}\sin\beta t\big),\qquad\mathrm{e}^{\alpha t}\big(\boldsymbol{a}\sin\beta t+\boldsymbol{b}\cos\beta t\big)
$$
是两个线性无关的实解，它们代替共轭特征值 $\alpha\pm\mathrm{i}\beta$ 对应的两个复解。

**算法 16.6.1（常系数齐次方程组，$A$ 可对角化）**

1. 求特征多项式 $\det(\lambda I-A)$ 的根 $\lambda_1,\dots,\lambda_n$；
2. 对每个特征值求特征向量（重特征值求出其特征子空间的一组基）；共轭复特征值只需对其中一个求特征向量，再取 $\mathrm{e}^{\lambda t}\boldsymbol{r}$ 的实部与虚部；
3. 通解 $\boldsymbol{x}=\sum C_k\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$。

若 $A$ 不可对角化（有**亏损特征值**），特征向量不够 $n$ 个，还需要形如 $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$ 的解，其中 $\boldsymbol{p}_1,\boldsymbol{p}_2,\dots$ 是 **Jordan 链**；一般地基解矩阵是 $\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$，见 [2.1.11 的推论 11.9.1](/2.1.11#cor-11.9.1) 与[例 11.9.1](/2.1.11#ex-11.9.1)。例 16.6.1 就是最简单的这种情形。

**例 16.6.3** 解 $\begin{cases}x_1'=x_2-x_3,\\x_2'=x_3,\\x_3'=x_2.\end{cases}$ $\det(\lambda I-A)=\begin{vmatrix}\lambda&-1&1\\0&\lambda&-1\\0&-1&\lambda\end{vmatrix}=\lambda(\lambda-1)(\lambda+1)$，特征值 $0,1,-1$，特征向量 $\boldsymbol{r}_1=(1,0,0)^{\mathsf T}$，$\boldsymbol{r}_2=(0,1,1)^{\mathsf T}$，$\boldsymbol{r}_3=(2,-1,1)^{\mathsf T}$。通解

$$
\boldsymbol{x}=\begin{bmatrix}1&0&2\mathrm{e}^{-t}\\0&\mathrm{e}^t&-\mathrm{e}^{-t}\\0&\mathrm{e}^t&\mathrm{e}^{-t}\end{bmatrix}\begin{bmatrix}C_1\\C_2\\C_3\end{bmatrix}.
$$

**例 16.6.4** 解 $\begin{cases}x_1'=3x_1+5x_2,\\x_2'=-5x_1+3x_2.\end{cases}$ $\det(\lambda I-A)=(\lambda-3)^2+25$，特征值 $3\pm5\mathrm{i}$。对 $\lambda=3+5\mathrm{i}$，$(A-\lambda I)\boldsymbol{r}=\boldsymbol{0}$ 即 $-5\mathrm{i}r_1+5r_2=0$，取 $\boldsymbol{r}=(1,\mathrm{i})^{\mathsf T}=\boldsymbol{a}+\mathrm{i}\boldsymbol{b}$，$\boldsymbol{a}=(1,0)^{\mathsf T}$，$\boldsymbol{b}=(0,1)^{\mathsf T}$。实部、虚部给出

$$
\boldsymbol{x}=\mathrm{e}^{3t}\begin{bmatrix}\cos5t&\sin5t\\-\sin5t&\cos5t\end{bmatrix}\begin{bmatrix}C_1\\C_2\end{bmatrix}.
$$
轨线是以 $5$ 为角速度顺时针旋转、同时按 $\mathrm{e}^{3t}$ 远离原点的螺线（不稳定焦点）。二维常系数方程组的各种相图见 [2.1.11](/2.1.11#sec-11.9)。

### 16.6.5. 方程组与高阶方程的互化

$n$ 阶方程可以化为一阶方程组：对 $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=f$，令 $x_1=y$，$x_2=y'$，…，$x_n=y^{(n-1)}$，得

$$
\boldsymbol{x}'=\begin{bmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-a_n&-a_{n-1}&\cdots&-a_1\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}0\\ \vdots\\0\\f\end{bmatrix}.
$$
系数矩阵是**友矩阵**，它的特征多项式恰好是 $\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$（[2.1.6](/2.1.6)），即 16.3 节的特征方程；方程的 $n$ 个解 $y_1,\dots,y_n$ 对应方程组的解 $(y_k,y_k',\dots,y_k^{(n-1)})^{\mathsf T}$，两种 Wronski 行列式相同。所以 16.1 节的结论都是本节的特例。反过来，方程组也可以用消元法化为一个高阶方程。

**例 16.6.5** 解 $\begin{cases}x_1'=3x_1-x_2,\\x_2'=x_1+x_2.\end{cases}$ 由第一式 $x_2=3x_1-x_1'$，代入第二式 $3x_1'-x_1''=x_1+3x_1-x_1'$，即 $x_1''-4x_1'+4x_1=0$，$x_1=\mathrm{e}^{2t}(C_1+C_2t)$。于是 $x_2=3x_1-x_1'=\mathrm{e}^{2t}(C_1-C_2+C_2t)$。这里 $A=\begin{bmatrix}3&-1\\1&1\end{bmatrix}$ 有二重特征值 $2$ 而只有一个特征向量方向，不可对角化，解中出现 $t\mathrm{e}^{2t}$。

**例 16.6.6** 解 $x'''-3x''+2x'=0$。令 $y=x'$，$z=x''$，得方程组 $x'=y$，$y'=z$，$z'=-2y+3z$。特征多项式 $\lambda(\lambda^2-3\lambda+2)$，特征值 $0,1,2$，特征向量 $(1,0,0)^{\mathsf T}$，$(1,1,1)^{\mathsf T}$，$(1,2,4)^{\mathsf T}$（友矩阵关于 $\lambda$ 的特征向量总是 $(1,\lambda,\lambda^2)^{\mathsf T}$）。取第一个分量：$x=C_1+C_2\mathrm{e}^t+C_3\mathrm{e}^{2t}$，与直接用特征方程 $\lambda^3-3\lambda^2+2\lambda=0$ 的结果一致。

二阶方程 (16.4) 化为方程组 $x'=v$，$v'=-\omega^2x-2kv$ 后，可以在 $(x,v)$ 相平面上观察三种阻尼的区别：欠阻尼的轨线是绕原点的螺线，临界阻尼与过阻尼的轨线不绕原点、直接进入原点。

![阻尼振子 x'' + 2k x' + x = 0 化为方程组 x' = v, v' = -x - 2k v 后的相平面轨线（初值 x = 1, v = 0 等）：欠阻尼 k = 0.15 为螺线；临界阻尼 k = 1 与过阻尼 k = 2.5 的轨线沿特征向量方向（虚线）进入原点](./plots/oscillator-phase-plane.py)

## 小结

| 方程 | 结构或方法 | 要点 |
|---|---|---|
| $n$ 阶线性方程 $L(y)=f$ | 通解 = 特解 + 基本解组的线性组合 | 解空间 $n$ 维（定理 16.1.4）；$n$ 个解无关 $\Leftrightarrow$ $W$ 在一点非零（定理 16.1.3） |
| 二阶变系数，已知 $y_1$ | 令 $y=C(x)y_1$ 降阶 | $y_2=y_1\int y_1^{-2}\mathrm{e}^{-\int a_1\mathrm{d}x}\,\mathrm{d}x$ |
| 二阶变系数，已知 $y_1,y_2$ | 常数变易法（算法 16.2.1） | $C_1'y_1+C_2'y_2=0$，$C_1'y_1'+C_2'y_2'=f$ |
| 常系数齐次 $P(\mathrm{D})y=0$ | 特征方程（算法 16.3.1） | $k$ 重根 $\lambda$：$x^j\mathrm{e}^{\lambda x}$；复根取实部、虚部 |
| 常系数非齐次 $P(\mathrm{D})y=f$ | 待定系数法（算法 16.4.1） | 特解 $x^kS_m\mathrm{e}^{\lambda x}$，$k$ 为 $\lambda$ 的重数；三角函数用复指数 |
| 同上 | 微分算子法 | 因式分解逐次降阶；$\frac{\mathrm{e}^{\lambda x}}{P(\lambda)}$；多项式右端展开 $\frac1{P(\mathrm{D})}$ |
| Euler 方程 | $x=\mathrm{e}^t$（算法 16.4.2） | $x^ky^{(k)}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y$ |
| 振动 $x''+2kx'+\omega^2x=H\sin pt$ | 特征根 $-k\pm\sqrt{k^2-\omega^2}$ | 欠阻尼、临界阻尼、过阻尼；$k=0$、$p=\omega$ 时共振 |
| 方程组 $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}$ | 基解矩阵 $\Phi$；常数变易法 (16.7) | $\boldsymbol{x}=\Phi\Phi^{-1}(t_0)\boldsymbol{x}_0$；$\det\Phi$ 满足 Liouville 公式 |
| 常系数齐次组 $\boldsymbol{x}'=A\boldsymbol{x}$ | 特征值与特征向量（算法 16.6.1） | 可对角化：$\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$；否则用 Jordan 链与 $\mathrm{e}^{tA}$（[2.1.11](/2.1.11)） |

线性方程的理论与线性代数一一对应：

| 线性代数 | 线性微分方程 |
|---|---|
| 线性映射 $A$，方程 $A\boldsymbol{x}=\boldsymbol{b}$ | 微分算子 $L$，方程 $L(y)=f$ |
| 解集 = 特解 + $\mathcal{N}(A)$ | 通解 = 特解 + $\ker L$ |
| $\dim\mathcal{N}(A)=n-\operatorname{rank}(A)$ | $\dim\ker L=n$（阶数） |
| 向量组线性无关 $\Leftrightarrow$ 行列式非零 | $n$ 个解线性无关 $\Leftrightarrow$ Wronski 行列式非零 |
| 特征值、特征向量 $A\boldsymbol{r}=\lambda\boldsymbol{r}$ | 指数解 $\mathrm{D}\mathrm{e}^{\lambda x}=\lambda\mathrm{e}^{\lambda x}$，$\boldsymbol{x}=\mathrm{e}^{\lambda t}\boldsymbol{r}$ |
| Jordan 链 | 重根对应的 $x^j\mathrm{e}^{\lambda x}$ 与 $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$ |
