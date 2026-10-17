---
title: 统计学基础
description: 正态样本的抽样分布，χ²、t、F 分布，极限分布与 Slutsky 定理；指数族及其自然形式；充分统计量、极小充分统计量与完全统计量，因子分解定理与 Basu 定理。
source_hash: b641acd225aa
---

统计量是随机变量，而关于推断方法优劣的一切陈述（估计值多常接近真值、检验多常犯错）都是关于统计量分布的陈述。本章建立贯穿后续各章的三件工具。第一是抽样分布：对正态样本，样本均值与样本方差相互独立且分布可以写出，由此引出大多数置信区间与检验背后的 $\chi^2$、$t$、$F$ 分布；当精确分布难以求得时，代之以极限分布与 Slutsky 定理。第二是指数族，它包含正态、二项、Poisson、Gamma 等分布，后面各章的大多数最优性问题在指数族中都有简洁的解答。第三是充分性与完全性这一对概念：前者说明统计量何时不损失关于参数的信息，后者说明统计量何时丰富到足以唯一确定无偏估计；它们是 [3.2.3](/3.2.3) 中 UMVUE 理论和 [3.2.5](/3.2.5) 中最优检验的基础。本章使用 [3.2.1](/3.2.1) 的术语和概率论的极限定理（[3.1.12](/3.1.12)–[3.1.14](/3.1.14)）。

## 2.1. 抽样分布

### 2.1.1. 抽样分布与极限分布

样本是随机向量，统计量作为样本的函数，也是随机变量或随机向量。

**定义 2.1.1（抽样分布）** 统计量的分布称为它的**抽样分布**。

抽样分布用于研究统计量的性质和评价推断方法，求出抽样分布是数理统计的基本问题之一。抽样分布有两类。精确抽样分布是在总体分布形式已知时、样本量 $n$ 固定下统计量的分布；它往往复杂、难以求得，已知的结果大多针对正态总体。极限分布是 $n\to\infty$ 时抽样分布的极限；它较容易求得，形式往往简单，且只要 $n$ 足够大就能很好地近似精确分布。

设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$，它可以是物体重量、人的身高体重、股票收益率或取对数后的收入的模型。$a$ 与 $\sigma^2$ 的自然估计是 $\bar X$ 与 $S^2$。它们好不好，即 $\mathbb{E}[(\bar X-a)^2]$ 与 $\mathbb{E}[(S^2-\sigma^2)^2]$ 是多少？如何构造 $a$ 与 $\sigma^2$ 的置信区间？两个问题都需要 $\bar X$ 与 $S^2$ 的分布。

### 2.1.2. 正态变量的线性函数

**定理 2.1.1** 设 $X_1,\dots,X_n$ 相互独立，$X_k\sim\mathcal{N}(a_k,\sigma_k^2)$，$k=1,\dots,n$，$c_1,\dots,c_n$ 为常数，$T=\sum_{k=1}^nc_kX_k$，则 $T\sim\mathcal{N}(\mu,\tau^2)$，其中

$$
\mu=\sum_{k=1}^nc_ka_k,\qquad\tau^2=\sum_{k=1}^nc_k^2\sigma_k^2.
$$

**证明** 利用**特征函数**。由 $X_k\sim\mathcal{N}(a_k,\sigma_k^2)$，$\varphi_k(t)=\mathbb{E}[\mathrm{e}^{\mathrm{i}tX_k}]=\mathrm{e}^{\mathrm{i}a_kt-\frac12\sigma_k^2t^2}$。由独立性，

$$
\varphi_T(t)=\mathbb{E}\left[\prod_{k=1}^n\mathrm{e}^{\mathrm{i}tc_kX_k}\right]=\prod_{k=1}^n\varphi_k(c_kt)=\prod_{k=1}^n\mathrm{e}^{\mathrm{i}c_ka_kt-\frac12c_k^2\sigma_k^2t^2}=\exp\left\{\mathrm{i}t\sum_{k=1}^nc_ka_k-\frac12t^2\sum_{k=1}^nc_k^2\sigma_k^2\right\},
$$
这正是 $\mathcal{N}(\mu,\tau^2)$ 的特征函数，而特征函数唯一确定分布。$\square$

也就是说，独立正态随机变量的线性组合仍服从正态分布。其均值与方差由线性性即可算出，定理的实质在于分布仍是正态的。

**推论 2.1.1** 在定理 2.1.1 中，若 $a_1=\dots=a_n=a$，$\sigma_1^2=\dots=\sigma_n^2=\sigma^2$，则

$$
T\sim\mathcal{N}\left(a\sum_{k=1}^nc_k,\ \sigma^2\sum_{k=1}^nc_k^2\right).
$$

**推论 2.1.2** 若 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$，则 $\bar X\sim\mathcal{N}(a,\sigma^2/n)$。

**证明** 在推论 2.1.1 中取 $c_1=\dots=c_n=1/n$。$\square$

**定理 2.1.2（正态样本的线性变换）** 设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$，$\boldsymbol{X}=(X_1,\dots,X_n)^{\mathsf T}$，$A=(a_{ij})$ 为 $n\times n$ 常数矩阵，$\boldsymbol{Y}=(Y_1,\dots,Y_n)^{\mathsf T}=A\boldsymbol{X}$，即

$$
\begin{pmatrix}Y_1\\ \vdots\\ Y_n\end{pmatrix}=\begin{pmatrix}a_{11}&\cdots&a_{1n}\\ \vdots&&\vdots\\ a_{n1}&\cdots&a_{nn}\end{pmatrix}\begin{pmatrix}X_1\\ \vdots\\ X_n\end{pmatrix}.
$$

1. 每个 $Y_i$ 都服从正态分布，且

   $$
   \mathbb{E}[Y_i]=a\sum_{k=1}^na_{ik},\qquad\operatorname{Var}(Y_i)=\sigma^2\sum_{k=1}^na_{ik}^2,\qquad\operatorname{Cov}(Y_i,Y_j)=\sigma^2\sum_{k=1}^na_{ik}a_{jk}.
   $$
2. 若 $A$ 是正交矩阵，则 $Y_1,\dots,Y_n$ 相互独立，且 $Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$，其中 $\mu_i=a\sum_{k=1}^na_{ik}$。
3. 若进一步 $a=0$，则 $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2)$。

**证明** (1) 由 $Y_i=\sum_{k=1}^na_{ik}X_k$ 及推论 2.1.1，$Y_i\sim\mathcal{N}\big(a\sum_ka_{ik},\ \sigma^2\sum_ka_{ik}^2\big)$，且

$$
\operatorname{Cov}(Y_i,Y_j)=\mathbb{E}[(Y_i-\mathbb{E}Y_i)(Y_j-\mathbb{E}Y_j)]=\sum_{k=1}^n\sum_{l=1}^na_{ik}a_{jl}\,\mathbb{E}[(X_k-a)(X_l-a)]=\sum_{k=1}^n\sum_{l=1}^na_{ik}a_{jl}\delta_{kl}\sigma^2=\sigma^2\sum_{k=1}^na_{ik}a_{jk},
$$
其中 $k=l$ 时 $\delta_{kl}=1$，否则 $\delta_{kl}=0$。

(2) $\boldsymbol{Y}=A\boldsymbol{X}$ 是正态向量 $\boldsymbol{X}$ 的线性像，因此服从**多元正态分布**；对联合正态的变量，不相关等价于独立。若 $A$ 正交，则其各行是标准正交的：$\sum_ka_{ik}^2=1$，故 $\operatorname{Var}(Y_i)=\sigma^2$；$i\ne j$ 时 $\sum_ka_{ik}a_{jk}=0$，故 $\operatorname{Cov}(Y_i,Y_j)=0$。因此 $Y_1,\dots,Y_n$ 相互独立，$Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$。

(3) 若 $a=0$，则所有 $\mu_i=0$。$\square$

用矩阵语言：$\boldsymbol{X}\sim\mathcal{N}_n(a\boldsymbol{1},\sigma^2I_n)$，于是 $\boldsymbol{Y}=A\boldsymbol{X}\sim\mathcal{N}_n(aA\boldsymbol{1},\sigma^2AA^{\mathsf T})$，而正交矩阵满足 $AA^{\mathsf T}=I_n$。球对称的正态向量经旋转后仍是球对称的。

### 2.1.3. 正态样本的样本均值与样本方差

**定理 2.1.3** 设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$（$n\ge2$），$\bar X$ 与 $S^2$ 为样本均值与样本方差，则

1. $\bar X\sim\mathcal{N}(a,\sigma^2/n)$；
2. $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$；
3. $\bar X$ 与 $S^2$ 相互独立。

这里 $\chi^2_{n-1}$ 是自由度为 $n-1$ 的卡方分布，即 $n-1$ 个独立标准正态变量平方和的分布（见下面的定义 2.1.2）。

**证明** (1) 即推论 2.1.2。(2) 思路是通过适当的正交变换，把 $(n-1)S^2$ 写成 $n-1$ 个独立正态变量的平方和。设

$$
A=\begin{pmatrix}\frac1{\sqrt n}&\frac1{\sqrt n}&\cdots&\frac1{\sqrt n}\\ a_{21}&a_{22}&\cdots&a_{2n}\\ \vdots&\vdots&&\vdots\\ a_{n1}&a_{n2}&\cdots&a_{nn}\end{pmatrix}
$$
是第一行为 $(1/\sqrt n,\dots,1/\sqrt n)$ 的正交矩阵，其余各行可由 **Gram–Schmidt 正交化**得到。令 $\boldsymbol{Y}=A\boldsymbol{X}$，则 $Y_1=\frac1{\sqrt n}\sum_{i=1}^nX_i=\sqrt n\,\bar X$，且正交变换保持长度，$\sum_{i=1}^nY_i^2=\sum_{i=1}^nX_i^2$。所以

$$
(n-1)S^2=\sum_{i=1}^n(X_i-\bar X)^2=\sum_{i=1}^nX_i^2-n\bar X^2=\sum_{i=1}^nY_i^2-Y_1^2=\sum_{i=2}^nY_i^2.
$$

由定理 2.1.2，$Y_1,\dots,Y_n$ 相互独立，$Y_i\sim\mathcal{N}(\mu_i,\sigma^2)$，而当 $i\ge2$ 时

$$
\mu_i=a\sum_{k=1}^na_{ik}=\sqrt n\,a\sum_{k=1}^n\frac1{\sqrt n}a_{ik}=0,
$$
因为 $A$ 的第 $i$ 行与第一行正交。于是 $Y_2/\sigma,\dots,Y_n/\sigma\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，$(n-1)S^2/\sigma^2=\sum_{i=2}^n(Y_i/\sigma)^2\sim\chi^2_{n-1}$。

(3) 在 (2) 的证明中，$S^2$ 是 $Y_2,\dots,Y_n$ 的函数，$\bar X$ 是 $Y_1$ 的函数，而 $Y_1,\dots,Y_n$ 相互独立。$\square$

定理 2.1.3 是 [3.2.4](/3.2.4) 与 [3.2.5](/3.2.5) 中正态总体均值、方差的置信区间与检验的基础。其中 (3) 的独立性刻画了正态分布：对其他任何总体，$\bar X$ 与 $S^2$ 都不独立。下面的模拟展示了所涉及的三个分布。

![从 N(1, 4) 中模拟 1000 个容量为 100 的样本，样本均值、样本方差与 t 统计量的直方图及理论密度](./plots/normal-sample-simulation.py)

右图表明 $\sqrt n(\bar X-a)/S$ 看起来服从标准正态分布。我们将看到两种解释：它的精确分布是 $t_{n-1}$（推论 2.1.4），$n$ 较大时接近 $\mathcal{N}(0,1)$；由 Slutsky 定理，它的极限分布是 $\mathcal{N}(0,1)$（例 2.1.2）。

### 2.1.4. 卡方分布、t 分布与 F 分布

**定义 2.1.2（卡方分布）** 设 $X_1,\dots,X_r\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，称

$$
\xi=\sum_{i=1}^rX_i^2
$$
的分布为**自由度**为 $r$ 的**卡方分布**，记作 $\xi\sim\chi^2_r$。其密度为

$$
f(x)=\frac1{\Gamma(r/2)\,2^{r/2}}x^{r/2-1}\mathrm{e}^{-x/2},\qquad x>0,
$$
$x\le0$ 时 $f(x)=0$。

这里 $\Gamma(\alpha)=\int_0^\infty y^{\alpha-1}\mathrm{e}^{-y}\,\mathrm{d}y$ 是 **Gamma 函数**。密度可以由 $X_1,\dots,X_r$ 的联合密度 $(2\pi)^{-r/2}\exp\{-\frac12\sum x_i^2\}$ 在球 $\{\sum x_i^2\le x\}$ 上用球坐标积分得到。等价地，在速率参数化下 $\chi^2_r=\Gamma(r/2,1/2)$：标准正态变量的平方服从 $\Gamma(1/2,1/2)$，而速率相同的独立 Gamma 变量之和的形状参数相加。密度的支撑为 $(0,\infty)$；$r=1,2$ 时单调下降，$r\ge3$ 时有唯一的峰，$r$ 越大越对称（由**中心极限定理**，它渐近正态）。卡方分布出现在正态样本的样本方差、似然比统计量和 Pearson $\chi^2$ 拟合优度检验中，用于方差的置信区间与检验。

**定义 2.1.3（上分位数）** 设随机变量 $\xi$ 服从连续分布，$0<\alpha<1$。满足 $\mathbb{P}(\xi>c)=\alpha$ 的数 $c$ 称为该分布的**上 $\alpha$ 分位数**。标准正态、$\chi^2_r$、$t_r$ 与 $F_{r_1,r_2}$ 分布的上 $\alpha$ 分位数分别记作 $z_\alpha$、$\chi^2_{r,\alpha}$、$t_{r,\alpha}$ 与 $F_{r_1,r_2,\alpha}$。

**命题 2.1.1** 设 $\xi\sim\chi^2_r$。

1. $\xi$ 的特征函数为 $\varphi(t)=(1-2\mathrm{i}t)^{-r/2}$。
2. $\mathbb{E}[\xi]=r$，$\operatorname{Var}(\xi)=2r$。
3. 若 $\xi_1\sim\chi^2_{r_1}$、$\xi_2\sim\chi^2_{r_2}$ 相互独立，则 $\xi_1+\xi_2\sim\chi^2_{r_1+r_2}$；一般地，若 $\xi_i\sim\chi^2_{r_i}$（$i=1,\dots,k$）相互独立，则 $\sum_{i=1}^k\xi_i\sim\chi^2_{r_1+\cdots+r_k}$。

**证明** 对 $X\sim\mathcal{N}(0,1)$，$\mathbb{E}[\mathrm{e}^{\mathrm{i}tX^2}]=\frac1{\sqrt{2\pi}}\int\mathrm{e}^{-(1-2\mathrm{i}t)x^2/2}\,\mathrm{d}x=(1-2\mathrm{i}t)^{-1/2}$，由独立性得 (1)。(2) $\mathbb{E}[X^2]=1$，$\operatorname{Var}(X^2)=\mathbb{E}[X^4]-1=3-1=2$，由独立性 $\mathbb{E}[\xi]=r$，$\operatorname{Var}(\xi)=2r$。(3) 由 (1)，和的特征函数为 $(1-2\mathrm{i}t)^{-(r_1+\cdots+r_k)/2}$；也可以直接看出，和是 $r_1+\dots+r_k$ 个独立标准正态变量的平方和。$\square$

**定义 2.1.4（t 分布）** 设 $X\sim\mathcal{N}(0,1)$ 与 $Y\sim\chi^2_r$ 相互独立，称

$$
T=\frac X{\sqrt{Y/r}}
$$
的分布为自由度为 $r$ 的 **$t$ 分布**（Student $t$ 分布），记作 $T\sim t_r$。其密度为

$$
f_T(t)=\frac{\Gamma\left(\frac{r+1}2\right)}{\Gamma\left(\frac r2\right)\sqrt{\pi r}}\left(1+\frac{t^2}r\right)^{-(r+1)/2},\qquad t\in\mathbb{R}.
$$

这一分布由 W. S. Gosset 发现，他于 1908 年以笔名 "Student" 发表，因此又称学生氏分布。密度关于 $0$ 对称，所以 $t_{r,1-\alpha}=-t_{r,\alpha}$；它的尾部比正态密度更厚。

**命题 2.1.2** 设 $T\sim t_r$。

1. $\mathbb{E}[T^k]$ 存在当且仅当 $k<r$，此时

   $$
   \mathbb{E}[T^k]=\begin{cases}r^{k/2}\dfrac{\Gamma\left(\frac{k+1}2\right)\Gamma\left(\frac{r-k}2\right)}{\Gamma\left(\frac r2\right)\Gamma\left(\frac12\right)}, & k\text{ 为偶数},\\[3mm] 0, & k\text{ 为奇数}.\end{cases}
   $$
   特别地，$r\ge2$ 时 $\mathbb{E}[T]=0$，$r\ge3$ 时 $\operatorname{Var}(T)=r/(r-2)$。
2. $r=1$ 时，$t_1$ 是标准 Cauchy 分布，密度为 $f_1(t)=\dfrac1{\pi(1+t^2)}$，$t\in\mathbb{R}$；它没有均值。
3. 当 $r\to\infty$ 时，$t_r$ 收敛于 $\mathcal{N}(0,1)$。

**证明** (1) $f_T$ 的尾部与 $|t|^{-(r+1)}$ 同阶，所以 $\int|t|^kf_T(t)\,\mathrm{d}t<\infty$ 当且仅当 $k<r$。对偶数 $k<r$，由独立性 $\mathbb{E}[T^k]=r^{k/2}\,\mathbb{E}[X^k]\,\mathbb{E}[Y^{-k/2}]$，其中 $\mathbb{E}[X^k]=2^{k/2}\Gamma(\frac{k+1}2)/\Gamma(\frac12)$，$\mathbb{E}[Y^{-k/2}]=2^{-k/2}\Gamma(\frac{r-k}2)/\Gamma(\frac r2)$，相乘即得公式；奇数阶矩由对称性为零。$k=2$ 时公式给出 $r\cdot\frac{\Gamma(3/2)\Gamma(r/2-1)}{\Gamma(r/2)\Gamma(1/2)}=\frac r{2(r/2-1)}=\frac r{r-2}$。(2) 代入 $r=1$、$\Gamma(1)=1$、$\Gamma(\frac12)=\sqrt\pi$。(3) 由**大数定律**，$Y/r$ 依概率收敛于 $1$，再由 Slutsky 定理（定理 2.1.4）得 $T\xrightarrow{d}\mathcal{N}(0,1)$；密度也逐点收敛，因为 $(1+t^2/r)^{-(r+1)/2}\to\mathrm{e}^{-t^2/2}$。$\square$

**定义 2.1.5（F 分布）** 设 $X\sim\chi^2_{r_1}$ 与 $Y\sim\chi^2_{r_2}$ 相互独立，称

$$
F=\frac{X/r_1}{Y/r_2}
$$
的分布为自由度为 $r_1$ 与 $r_2$ 的 **$F$ 分布**，记作 $F\sim F_{r_1,r_2}$。其密度为

$$
f_{r_1,r_2}(x)=\begin{cases}\dfrac{\Gamma\left(\frac{r_1+r_2}2\right)}{\Gamma\left(\frac{r_1}2\right)\Gamma\left(\frac{r_2}2\right)}\left(\dfrac{r_1}{r_2}\right)^{r_1/2}x^{r_1/2-1}\left(1+\dfrac{r_1}{r_2}x\right)^{-(r_1+r_2)/2}, & x>0,\\[3mm] 0, & x\le0.\end{cases}
$$

$F$ 分布用于比较两个正态总体的方差、方差分析等问题。

**命题 2.1.3**

1. 若 $F\sim F_{r_1,r_2}$，则 $1/F\sim F_{r_2,r_1}$。
2. 若 $T\sim t_r$，则 $T^2\sim F_{1,r}$。
3. 若 $F\sim F_{r_1,r_2}$，$0<2k<r_2$，则

   $$
   \mathbb{E}[F^k]=\left(\frac{r_2}{r_1}\right)^k\frac{\Gamma\left(\frac{r_1}2+k\right)\Gamma\left(\frac{r_2}2-k\right)}{\Gamma\left(\frac{r_1}2\right)\Gamma\left(\frac{r_2}2\right)};
   $$
   特别地，

   $$
   \mathbb{E}[F]=\frac{r_2}{r_2-2}\quad(r_2\ge3),\qquad\operatorname{Var}(F)=\frac{2r_2^2(r_1+r_2-2)}{r_1(r_2-2)^2(r_2-4)}\quad(r_2\ge5).
   $$
4. $F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$。

**证明** (1) $1/F=\frac{Y/r_2}{X/r_1}$，只是 $X$ 与 $Y$ 的角色互换。(2) $T^2=\frac{X^2/1}{Y/r}$，其中 $X^2\sim\chi^2_1$ 与 $Y\sim\chi^2_r$ 独立。(3) 由独立性 $\mathbb{E}[F^k]=(r_2/r_1)^k\,\mathbb{E}[X^k]\,\mathbb{E}[Y^{-k}]$，而对 $\xi\sim\chi^2_r$ 与 $s>-r/2$，$\mathbb{E}[\xi^s]=2^s\Gamma(\frac r2+s)/\Gamma(\frac r2)$。(4) 由 (1)，$1-\alpha=\mathbb{P}(F>F_{r_1,r_2,1-\alpha})=\mathbb{P}(1/F<1/F_{r_1,r_2,1-\alpha})$，于是 $\mathbb{P}(1/F>1/F_{r_1,r_2,1-\alpha})=\alpha$，而 $1/F\sim F_{r_2,r_1}$。$\square$

性质 (4) 说明了为什么 $F$ 分布表只列出较小的 $\alpha$。

![卡方分布在 r = 1, 2, 4, 8 时的密度（阴影为 r = 4 时上 0.05 分位数右侧的面积），t 分布在 r = 1, 5, 10 时的密度与标准正态密度的比较，以及三组自由度下 F 分布的密度](./plots/sampling-distributions.py)

### 2.1.5. 几个有用的推论

下面的推论把定理 2.1.3 与上述定义结合起来，它们是 [3.2.4](/3.2.4) 与 [3.2.5](/3.2.5) 中正态理论区间估计与检验的枢轴量。

**推论 2.1.3** 若 $X_1,\dots,X_n$ 相互独立，$X_i\sim\mathcal{N}(a_i,\sigma_i^2)$，则

$$
\sum_{i=1}^n\left(\frac{X_i-a_i}{\sigma_i}\right)^2\sim\chi^2_n.
$$

**证明** 标准化变量 $(X_i-a_i)/\sigma_i$ 独立同分布于 $\mathcal{N}(0,1)$。$\square$

**推论 2.1.4** 若 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathcal{N}(a,\sigma^2)$，则

$$
T=\frac{\sqrt n(\bar X-a)}S\sim t_{n-1}.
$$

**证明** 写 $T=\dfrac{\sqrt n(\bar X-a)/\sigma}{\sqrt{[(n-1)S^2/\sigma^2]/(n-1)}}$。由定理 2.1.3，分子服从 $\mathcal{N}(0,1)$，方括号内的量服从 $\chi^2_{n-1}$，且二者独立。$\square$

**推论 2.1.5** 设 $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(a_1,\sigma^2)$，$Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(a_2,\sigma^2)$，且两样本相互独立，则

$$
T=\frac{(\bar X-\bar Y)-(a_1-a_2)}{S_w}\sqrt{\frac{mn}{m+n}}\sim t_{m+n-2},
$$
其中 $(m+n-2)S_w^2=(m-1)S_X^2+(n-1)S_Y^2$，$S_X^2=\frac1{m-1}\sum_{i=1}^m(X_i-\bar X)^2$，$S_Y^2=\frac1{n-1}\sum_{j=1}^n(Y_j-\bar Y)^2$。

**证明** 由定理 2.1.1，$\bar X-\bar Y\sim\mathcal{N}\big(a_1-a_2,\ \sigma^2(\frac1m+\frac1n)\big)$，所以 $U=\frac{(\bar X-\bar Y)-(a_1-a_2)}\sigma\sqrt{\frac{mn}{m+n}}\sim\mathcal{N}(0,1)$。由定理 2.1.3 与命题 2.1.1，$V=(m+n-2)S_w^2/\sigma^2=(m-1)S_X^2/\sigma^2+(n-1)S_Y^2/\sigma^2\sim\chi^2_{m+n-2}$，又因 $\bar X,S_X^2,\bar Y,S_Y^2$ 相互独立，$V$ 与 $U$ 独立。故 $T=U/\sqrt{V/(m+n-2)}\sim t_{m+n-2}$。$\square$

**推论 2.1.6** 设 $X_1,\dots,X_m\overset{\text{iid}}{\sim}\mathcal{N}(a_1,\sigma_1^2)$，$Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(a_2,\sigma_2^2)$，且两样本相互独立，则

$$
F=\frac{S_X^2}{S_Y^2}\cdot\frac{\sigma_2^2}{\sigma_1^2}\sim F_{m-1,n-1}.
$$

**证明** $F=\dfrac{[(m-1)S_X^2/\sigma_1^2]/(m-1)}{[(n-1)S_Y^2/\sigma_2^2]/(n-1)}$，是相互独立的 $\chi^2_{m-1}$ 与 $\chi^2_{n-1}$ 变量各除以自由度后的比。$\square$

**推论 2.1.7** 若 $X_1,\dots,X_n\overset{\text{iid}}{\sim}\mathrm{Exp}(\lambda)$，密度为 $f(x;\lambda)=\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$，则

$$
2\lambda n\bar X=2\lambda\sum_{i=1}^nX_i\sim\chi^2_{2n}.
$$

**证明** 先看 $2\lambda X_1$：对 $x>0$，$\mathbb{P}(2\lambda X_1>x)=\mathbb{P}(X_1>x/(2\lambda))=\mathrm{e}^{-x/2}$，所以 $2\lambda X_1$ 的密度为 $\frac12\mathrm{e}^{-x/2}$，正是 $\chi^2_2$ 的密度。各 $2\lambda X_i$ 是独立的 $\chi^2_2$ 变量，由命题 2.1.1，其和服从 $\chi^2_{2n}$。$\square$

### 2.1.6. 极限分布

**定义 2.1.6（极限分布）** 若当样本量 $n\to\infty$ 时统计量的分布收敛于某个给定的分布，则称该分布为统计量的**极限分布**（大样本分布）。

需要极限分布，是因为精确分布通常难以求得，即使求得也可能复杂到无法使用；极限分布提供了近似，也是比较推断方法的标准工具。统计量或推断方法在 $n\to\infty$ 时的性质称为大样本性质，研究它们的理论是大样本（渐近）理论；样本量固定时的性质称为小样本性质。

**例 2.1.1** 设 $X_1,\dots,X_n\overset{\text{iid}}{\sim}F$（不必是正态），均值为 $a_F$，方差 $\sigma_F^2\in(0,\infty)$，$\bar X_n$ 为样本均值。大样本性质：由强**大数定律**，$\mathbb{P}(\lim_{n\to\infty}\bar X_n=a_F)=1$；由**中心极限定理**，$\sqrt n(\bar X_n-a_F)/\sigma_F\xrightarrow{d}\mathcal{N}(0,1)$，因此 $n$ 较大时

$$
\mathbb{P}(|\bar X_n-a_F|>c)\approx2\left[1-\Phi\left(\frac{c\sqrt n}{\sigma_F}\right)\right],
$$
其中 $\Phi$ 是标准正态分布函数。小样本性质：对每个 $n$，$\mathbb{E}[\bar X_n]=a_F$。

求极限分布的主要工具是 Slutsky 定理，其证明见 [3.1.14](/3.1.14)。

**定理 2.1.4（Slutsky 定理）** 设 $X_n$、$Y_n$ 为随机变量序列，$X_n\xrightarrow{d}X$，$Y_n\xrightarrow{p}c$，$c$ 为常数，则

1. $X_n+Y_n\xrightarrow{d}X+c$；
2. $X_nY_n\xrightarrow{d}cX$；
3. 当 $c\ne0$ 时，$X_n/Y_n\xrightarrow{d}X/c$。

**例 2.1.2** 在例 2.1.1 中，由于 $S_n^2=\frac n{n-1}\left(\frac1n\sum X_i^2-\bar X_n^2\right)$，而两个平均值都由强大数定律收敛，故 $S_n^2\to\sigma_F^2$ 几乎处处成立；于是 $\sigma_F/S_n\xrightarrow{p}1$，由 Slutsky 定理

$$
\frac{\sqrt n(\bar X_n-a_F)}{S_n}=\frac{\sqrt n(\bar X_n-a_F)}{\sigma_F}\cdot\frac{\sigma_F}{S_n}\xrightarrow{d}\mathcal{N}(0,1)
$$
对任何方差有限且为正的总体成立。对正态总体，这个统计量的精确分布是 $t_{n-1}$（推论 2.1.4）；两者并不矛盾，因为 $t_{n-1}\to\mathcal{N}(0,1)$。

**例 2.1.3** 设 $X_1,\dots,X_n$ 是取自 Bernoulli 总体 $\mathrm{Ber}(p)$（$0<p<1$）的样本，则 $\dfrac{\sqrt n(\bar X_n-p)}{\sqrt{\bar X_n(1-\bar X_n)}}$ 的极限分布为 $\mathcal{N}(0,1)$。

**证明** 记 $\hat p=\bar X_n$。由**中心极限定理**与弱大数定律，

$$
\frac{\sqrt n(\hat p-p)}{\sqrt{p(1-p)}}\xrightarrow{d}\mathcal{N}(0,1),\qquad\frac{p(1-p)}{\hat p(1-\hat p)}\xrightarrow{p}1
$$
（后者是因为 $\hat p\xrightarrow{p}p$，而 $x\mapsto p(1-p)/[x(1-x)]$ 在 $p$ 处连续）。由 Slutsky 定理，

$$
\frac{\sqrt n(\bar X_n-p)}{\sqrt{\bar X_n(1-\bar X_n)}}=\frac{\sqrt n(\hat p-p)}{\sqrt{p(1-p)}}\cdot\sqrt{\frac{p(1-p)}{\hat p(1-\hat p)}}\xrightarrow{d}\mathcal{N}(0,1).
$$

当 $\hat p\in\{0,1\}$ 时统计量没有定义，但这一事件的概率为 $p^n+(1-p)^n\to0$，不影响极限。$\square$

这个例子是 [3.2.4](/3.2.4) 中比例的大样本置信区间的基础。

## 2.2. 指数族

### 2.2.1. 分布族与似然函数

分布族 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$（[3.2.1](/3.2.1)）的参数可以是向量 $\theta=(\theta_1,\dots,\theta_k)$。记号 $f_\theta(x)$、$f(x\mid\theta)$ 与 $f(x;\theta)$ 通用；连续情形下 $f$ 是密度，离散情形下是概率质量函数。对观测值 $x$，把密度看作 $\theta$ 的函数，称为似然函数 $L(\theta;x)=f(x;\theta)$，称 $\ell(\theta;x)=\log L(\theta;x)$ 为对数似然函数；它们是 [3.2.3](/3.2.3) 的核心。

许多熟悉的分布族形式相似：

- 正态 $\mathcal{N}(\theta,1)$：$f(x;\theta)=\frac1{\sqrt{2\pi}}\mathrm{e}^{-(x-\theta)^2/2}$，$x\in\mathbb{R}$，$\theta\in\mathbb{R}$；
- Poisson：$f(x;\theta)=\frac{\theta^x}{x!}\mathrm{e}^{-\theta}$，$x=0,1,2,\dots$，$\theta>0$；
- 指数：$f(x;\theta)=\theta\mathrm{e}^{-\theta x}$，$x>0$，$\theta>0$；
- 正态 $\mathcal{N}(\mu,\sigma^2)$：$f(x;\theta)=\frac1{\sqrt{2\pi}\sigma}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}$，$x\in\mathbb{R}$，$\theta=(\mu,\sigma^2)\in\mathbb{R}\times(0,\infty)$。

在每一个中，参数与观测值只通过"$\theta$ 的函数乘以 $x$ 的函数"之和的指数相互作用。

### 2.2.2. 定义与例子

**定义 2.2.1（指数族）** 设 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 是参数空间为 $\Theta$ 的分布族。若密度具有形式

$$
f(x;\theta)=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)T_i(x)\right\}h(x),
$$
其中 $k$ 为正整数，$C(\theta)>0$ 与 $Q_1(\theta),\dots,Q_k(\theta)$ 只是 $\theta$ 的函数（与 $x$ 无关），$h(x)\ge0$ 与 $T_1(x),\dots,T_k(x)$ 只是 $x$ 的函数（与 $\theta$ 无关），则称 $\mathcal{F}$ 为**指数族**。

引入指数族的意义不在于公式形状相同，而在于它们共有的结构：统计理论的许多问题（充分性、完全性、最优估计与最优检验）对指数族有完整的解答。这一概念源于 E. J. G. Pitman、G. Darmois 与 B. O. Koopman（1935—1936），他们证明了：在支撑与参数无关的分布族中，本质上只有指数族对每个样本量都存在固定维数的充分统计量（Pitman–Koopman–Darmois 定理）。

**例 2.2.1** 设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是取自 $\mathcal{N}(\mu,\sigma^2)$ 的样本。记 $\theta=(\mu,\sigma^2)\in\Theta=\{(\mu,\sigma^2)\colon-\infty<\mu<\infty,\ \sigma^2>0\}$，联合密度为

$$
f(\boldsymbol{x};\theta)=(\sqrt{2\pi}\sigma)^{-n}\exp\left\{-\frac1{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2\right\}=(\sqrt{2\pi}\sigma)^{-n}\mathrm{e}^{-\frac{n\mu^2}{2\sigma^2}}\exp\left\{\frac\mu{\sigma^2}\sum_{i=1}^nx_i-\frac1{2\sigma^2}\sum_{i=1}^nx_i^2\right\},
$$
具有 $C(\theta)\exp\{Q_1(\theta)T_1(\boldsymbol{x})+Q_2(\theta)T_2(\boldsymbol{x})\}h(\boldsymbol{x})$ 的形式，其中

$$
C(\theta)=(\sqrt{2\pi}\sigma)^{-n}\mathrm{e}^{-n\mu^2/(2\sigma^2)},\quad Q_1(\theta)=\frac\mu{\sigma^2},\quad Q_2(\theta)=-\frac1{2\sigma^2},\quad T_1(\boldsymbol{x})=\sum_{i=1}^nx_i,\quad T_2(\boldsymbol{x})=\sum_{i=1}^nx_i^2,\quad h(\boldsymbol{x})=1.
$$

所以样本分布族是指数族。取 $n=1$，同样的计算表明 $\{\mathcal{N}(\mu,\sigma^2)\}$ 本身就是指数族；这一性质与样本量无关。一般地，取自指数族的样本的联合密度仍是指数族形式，其中 $T_i(\boldsymbol{x})=\sum_{j=1}^nT_i(x_j)$。

**例 2.2.2** 设 $\boldsymbol{X}$ 是取自 Gamma 分布 $\Gamma(\gamma,\lambda)$ 的样本，密度为 $\frac{\lambda^\gamma}{\Gamma(\gamma)}x^{\gamma-1}\mathrm{e}^{-\lambda x}\boldsymbol{1}_{(0,\infty)}(x)$，$\theta=(\gamma,\lambda)\in\Theta=\{(\gamma,\lambda)\colon\gamma>0,\ \lambda>0\}$。则

$$
f(\boldsymbol{x};\theta)=\prod_{i=1}^n\frac{\lambda^\gamma}{\Gamma(\gamma)}x_i^{\gamma-1}\mathrm{e}^{-\lambda x_i}\boldsymbol{1}_{(0,\infty)}(x_i)=\frac{\lambda^{n\gamma}}{(\Gamma(\gamma))^n}\exp\left\{-\lambda\sum_{i=1}^nx_i+(\gamma-1)\sum_{i=1}^n\log x_i\right\}\prod_{i=1}^n\boldsymbol{1}_{(0,\infty)}(x_i),
$$
是指数族，其中 $C(\theta)=\lambda^{n\gamma}/(\Gamma(\gamma))^n$，$Q_1(\theta)=-\lambda$，$Q_2(\theta)=\gamma-1$，$T_1(\boldsymbol{x})=\sum x_i$，$T_2(\boldsymbol{x})=\sum\log x_i$，$h(\boldsymbol{x})=\prod\boldsymbol{1}_{(0,\infty)}(x_i)$。

**例 2.2.3** 二项分布族 $\{\mathrm{Bin}(n,\theta)\colon0<\theta<1\}$ 是指数族。对 $X\sim\mathrm{Bin}(n,\theta)$，样本空间 $\mathcal{X}=\{0,1,\dots,n\}$，$\Theta=(0,1)$，

$$
f(x;\theta)=\binom nx\theta^x(1-\theta)^{n-x}=(1-\theta)^n\exp\left\{x\log\frac\theta{1-\theta}\right\}\binom nx,
$$
所以 $C(\theta)=(1-\theta)^n$，$Q_1(\theta)=\log\frac\theta{1-\theta}$，$T_1(x)=x$，$h(x)=\binom nx$。

**例 2.2.4** Poisson 分布族 $\{\mathrm{Poi}(\theta)\colon\theta>0\}$ 是指数族：对 $x\in\mathcal{X}=\{0,1,2,\dots\}$，

$$
f(x;\theta)=\frac{\mathrm{e}^{-\theta}\theta^x}{x!}=\mathrm{e}^{-\theta}\exp\{x\log\theta\}\frac1{x!},
$$
其中 $\Theta=(0,\infty)$，$C(\theta)=\mathrm{e}^{-\theta}$，$Q_1(\theta)=\log\theta$，$T_1(x)=x$，$h(x)=1/x!$。

指数族的支撑 $\{x\colon f(x;\theta)>0\}=\{x\colon h(x)>0\}$ 与 $\theta$ 无关：族中所有分布有相同的支撑。这给出了判断一个分布族不是指数族的快捷方法。

**例 2.2.5** (1) 均匀分布族 $\{\mathrm{U}(0,\theta)\colon\theta>0\}$，$f(x;\theta)=\frac1\theta\boldsymbol{1}_{[0,\theta]}(x)$，不是指数族，因为其支撑 $[0,\theta]$ 依赖于 $\theta$。

(2) Cauchy 位置分布族 $f(x;\theta)=\dfrac1{\pi[1+(x-\theta)^2]}$，$x\in\mathbb{R}$，$\theta\in\mathbb{R}$，支撑固定，但也不是指数族。若它是指数族，则对每个 $\theta$，$\log f(x;\theta)-\log f(x;0)=\log(1+x^2)-\log(1+(x-\theta)^2)$ 都应落在有限个函数 $1,T_1(x),\dots,T_k(x)$ 张成的空间中；但不同 $\theta$ 对应的函数 $\log(1+(x-\theta)^2)$ 张成的是无穷维空间。

### 2.2.3. 自然形式

记 $\varphi_i=Q_i(\theta)$，并把 $C(\theta)$ 表示为 $\varphi=(\varphi_1,\dots,\varphi_k)$ 的函数 $C^*(\varphi)$，形式会更简单；然后把 $\varphi_i$ 改记为 $\theta_i$。

**定义 2.2.2（自然形式）** 写成

$$
f(x;\theta)=C^*(\theta)\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)
$$
的指数族称为具有**自然形式**（标准形式），$\theta=(\theta_1,\dots,\theta_k)$ 称为**自然参数**。集合

$$
\Theta^*=\left\{(\theta_1,\dots,\theta_k)\colon\int_{\mathcal{X}}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x<\infty\right\}
$$
称为**自然参数空间**。

对离散分布，积分换成求和。$\Theta^*$ 是使上式定义一个概率分布的全部 $\theta$ 的集合，此时 $C^*(\theta)=\left(\int\mathrm{e}^{\sum\theta_iT_i}h\,\mathrm{d}x\right)^{-1}$；它包含原参数空间的像，也可能更大。

**例 2.2.6** 对正态样本（例 2.2.1），令

$$
\begin{cases}\varphi_1=\mu/\sigma^2,\\ \varphi_2=-1/(2\sigma^2),\end{cases}\qquad\text{于是}\qquad\begin{cases}\sigma^2=-1/(2\varphi_2),\\ \mu^2/\sigma^2=-\varphi_1^2/(2\varphi_2).\end{cases}
$$

则 $C(\theta)=C^*(\varphi)=(-\pi/\varphi_2)^{-n/2}\exp\{n\varphi_1^2/(4\varphi_2)\}$，且

$$
f(\boldsymbol{x};\varphi)=C^*(\varphi)\exp\{\varphi_1T_1(\boldsymbol{x})+\varphi_2T_2(\boldsymbol{x})\}h(\boldsymbol{x}),\qquad\Theta^*=\{(\varphi_1,\varphi_2)\colon-\infty<\varphi_1<\infty,\ -\infty<\varphi_2<0\}.
$$

**例 2.2.7** 对二项分布族（例 2.2.3），令 $\varphi=\log[\theta/(1-\theta)]$，则 $-\infty<\varphi<\infty$，$1-\theta=1/(1+\mathrm{e}^\varphi)$，于是

$$
f(x;\varphi)=(1+\mathrm{e}^\varphi)^{-n}\exp\{\varphi x\}\binom nx,\qquad\Theta^*=(-\infty,\infty).
$$

自然参数是对数优势比，也就是 logistic 回归中的参数。

### 2.2.4. 指数族的性质

**定理 2.2.1** 设 $\{f(x;\theta)\colon\theta\in\Theta^*\}$ 是自然形式的指数族。

1. 族中所有分布有相同的支撑 $\{x\colon h(x)>0\}$，它与 $\theta$ 无关。
2. 自然参数空间 $\Theta^*$ 是凸集。
3. 设 $\Theta^*$ 有内点，记 $\Theta_0$ 为其内点的集合。若实函数 $g(x)$ 使

   $$
   G(\theta)=\int_{\mathcal{X}}g(x)\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x
   $$
   在 $\Theta^*$ 上存在且有限，则 $G$ 在 $\Theta_0$ 上有任意阶偏导数，且可在积分号下求导：

   $$
   \frac{\partial^mG(\theta)}{\partial\theta_1^{m_1}\cdots\partial\theta_k^{m_k}}=\int_{\mathcal{X}}g(x)\prod_{i=1}^kT_i(x)^{m_i}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x,\qquad m=m_1+\cdots+m_k.
   $$
4. 指数族在光滑可逆变换下保持不变：若 $Y=Y(X)$ 是 $X$ 的光滑可逆变换，则 $Y$ 的分布仍构成指数族，且 $C$ 与 $Q_i$ 不变。

**证明** (1) 由 $C^*(\theta)>0$ 和指数函数取正值即得。(2) 设 $\theta^0,\theta^1\in\Theta^*$，$0<\alpha<1$，$\theta=\alpha\theta^0+(1-\alpha)\theta^1$。由 Hölder 不等式 $\|fg\|_1\le\|f\|_p\|g\|_q$（取 $p=1/\alpha$，$q=1/(1-\alpha)$），

$$
\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta_iT_i(x)}h(x)\,\mathrm{d}x=\int_{\mathcal{X}}\left[\mathrm{e}^{\sum_i\theta^0_iT_i(x)}h(x)\right]^\alpha\left[\mathrm{e}^{\sum_i\theta^1_iT_i(x)}h(x)\right]^{1-\alpha}\mathrm{d}x\le\left[\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta^0_iT_i}h\,\mathrm{d}x\right]^\alpha\left[\int_{\mathcal{X}}\mathrm{e}^{\sum_i\theta^1_iT_i}h\,\mathrm{d}x\right]^{1-\alpha}<\infty,
$$
所以 $\theta\in\Theta^*$。(3) 在内点附近，被积函数及其导数被形如 $|g|\,\mathrm{e}^{\sum(\theta_i\pm\delta)T_i}h$ 的可积函数控制，由控制收敛定理可在积分号下求导；细节从略。(4) 由变量替换公式，

$$
f_Y(y;\theta)=f_X(x(y);\theta)\left|\frac{\partial x}{\partial y}\right|=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)T_i(x(y))\right\}h(x(y))\left|\frac{\partial x}{\partial y}\right|.
$$

Jacobi 行列式只依赖于 $y$，所以 $C(\theta)$ 与 $Q_i(\theta)$ 不变，而 $T_i$ 变为 $T_i(x(y))$，$h$ 变为 $h(x(y))\,|\partial x/\partial y|$。$\square$

在性质 3 中取 $g=1$，就能只用归一化常数算出 $T_i(X)$ 的各阶矩。

**推论 2.2.1** 在自然形式下记 $D(\theta)=\log C^*(\theta)$。对 $\theta\in\Theta_0$，

$$
\mathbb{E}_\theta[T_i(X)]=-\frac{\partial D(\theta)}{\partial\theta_i},\qquad\operatorname{Cov}_\theta(T_i(X),T_j(X))=-\frac{\partial^2D(\theta)}{\partial\theta_i\partial\theta_j};
$$
特别地，$\operatorname{Var}_\theta(T_i(X))=-\partial^2D(\theta)/\partial\theta_i^2$。

**证明** 由 $\int f(x;\theta)\,\mathrm{d}x=1$，

$$
\int_{\mathcal{X}}\exp\left\{\sum_{i=1}^k\theta_iT_i(x)\right\}h(x)\,\mathrm{d}x=\frac1{C^*(\theta)}=\mathrm{e}^{-D(\theta)}.
$$

对 $\theta_i$ 在积分号下求导（定理 2.2.1(3)），

$$
\int_{\mathcal{X}}T_i(x)\exp\left\{\sum_{l=1}^k\theta_lT_l(x)\right\}h(x)\,\mathrm{d}x=-\frac{\partial D(\theta)}{\partial\theta_i}\mathrm{e}^{-D(\theta)},
$$
两边乘以 $\mathrm{e}^{D(\theta)}=C^*(\theta)$ 即得 $\mathbb{E}_\theta[T_i(X)]=-\partial D/\partial\theta_i$。把这个等式写成 $\int T_i\,f(x;\theta)\,\mathrm{d}x=-\partial_iD$，再对 $\theta_j$ 求导，得 $\int T_i(T_j+\partial_jD)f\,\mathrm{d}x=-\partial_i\partial_jD$，即 $\mathbb{E}[T_iT_j]-\mathbb{E}[T_i]\mathbb{E}[T_j]=-\partial_i\partial_jD$。$\square$

**例 2.2.8** 对自然形式（例 2.2.7）下的 $X\sim\mathrm{Bin}(n,\theta)$，$\theta=\mathrm{e}^\varphi/(1+\mathrm{e}^\varphi)$，$T_1(x)=x$，$D(\varphi)=\log C^*(\varphi)=-n\log(1+\mathrm{e}^\varphi)$。于是

$$
\mathbb{E}[X]=-\frac{\partial D}{\partial\varphi}=n\frac{\mathrm{e}^\varphi}{1+\mathrm{e}^\varphi}=n\theta,\qquad\operatorname{Var}(X)=-\frac{\partial^2D}{\partial\varphi^2}=n\frac{\mathrm{e}^\varphi}{(1+\mathrm{e}^\varphi)^2}=n\theta(1-\theta),
$$
无需任何求和就得到了二项分布的均值与方差。

## 2.3. 充分统计量与完全统计量

### 2.3.1. 充分统计量

设 $\boldsymbol{X}=(X_1,\dots,X_n)$ 是取自 $f(x;\theta)$ 的样本。统计量 $T(\boldsymbol{X})$ 是对样本中关于 $\theta$ 的信息的简化或概括。我们希望简化程度尽量高，而信息损失尽量少。直观上，

$$
\boldsymbol{X}\text{ 中关于 }\theta\text{ 的信息}=T(\boldsymbol{X})\text{ 中的信息}+\text{已知 }T(\boldsymbol{X})\text{ 后 }\boldsymbol{X}\text{ 中剩余的信息}.
$$

若最后一项为零，$T$ 就提取了全部信息，可以用 $T(\boldsymbol{X})$ 代替 $n$ 个观测值而不损失信息。当给定 $T$ 时样本的条件分布与 $\theta$ 无关，剩余信息就是零：此时详细的数据相当于一次不需要知道 $\theta$ 就能产生的额外随机抽取。这一概念由 R. A. Fisher 于 1922 年提出。

**例 2.3.1** 设 $X_1,\dots,X_n$ 是取自 $\mathrm{Ber}(\theta)$（$0<\theta<1$）的样本，$T(\boldsymbol{X})=\sum_{i=1}^nX_i\sim\mathrm{Bin}(n,\theta)$。直观上，成功次数包含了关于 $\theta$ 的全部信息，而成功出现的顺序不包含任何信息。事实上，记 $t=\sum x_i$，则 $f_{\boldsymbol{X}}(\boldsymbol{x};\theta)=\theta^t(1-\theta)^{n-t}$，$f_T(t;\theta)=\binom nt\theta^t(1-\theta)^{n-t}$，因此对满足 $\sum x_i=t$ 的 $\boldsymbol{x}$，

$$
f(\boldsymbol{x}\mid t)=\frac{\mathbb{P}(X_1=x_1,\dots,X_n=x_n,T=t)}{f_T(t)}=\frac{\mathbb{P}(X_1=x_1,\dots,X_{n-1}=x_{n-1},X_n=t-x_1-\dots-x_{n-1})}{f_T(t)}=\frac{\theta^t(1-\theta)^{n-t}}{\binom nt\theta^t(1-\theta)^{n-t}}=\frac1{\binom nt},
$$
而 $\sum x_i\ne t$ 时 $f(\boldsymbol{x}\mid t)=0$。给定成功次数，无论 $\theta$ 是多少，每种排列都等可能。

**定义 2.3.1（充分统计量）** 若给定 $T=t$ 时 $\boldsymbol{X}=(X_1,\dots,X_n)$ 的条件分布与 $\theta$ 无关，即

$$
g(\boldsymbol{x}\mid t,\theta)=g(\boldsymbol{x}\mid t),
$$
则称统计量 $T(\boldsymbol{X})$ 对 $\theta$ 是充分的，或称 $T(\boldsymbol{X})$ 是 $\theta$ 的**充分统计量**。

**注 2.3.1**

- 充分统计量包含了样本中关于 $\theta$ 的全部信息。
- 若 $T$ 是 $\theta$ 的充分统计量，$g$ 是一一的可测函数，则 $T^*=g(T)$ 也是充分统计量，因为以 $T$ 为条件与以 $T^*$ 为条件是一回事。
- 若 $T$ 是充分统计量，$T_1$ 是任一统计量，则 $(T,T_1)$ 是充分统计量。
- 若 $\theta$ 是 $k$ 维的，通常需要多维的充分统计量，其维数一般为 $k$。

**例 2.3.2** 设 $X_1,\dots,X_n$ 是取自 $\mathcal{N}(\theta,1)$ 的样本，则 $T(\boldsymbol{X})=\bar X$ 是 $\theta$ 的充分统计量。直接求给定 $\bar X$ 时 $\boldsymbol{X}$ 的条件分布较为麻烦；改用定理 2.1.3 证明中的正交矩阵 $A$，令 $\boldsymbol{Y}=A\boldsymbol{X}$，则

$$
Y_1=\frac1{\sqrt n}\sum_{i=1}^nX_i=\sqrt n\,\bar X,\qquad Y_j=\sum_{k=1}^na_{jk}X_k,\quad j=2,\dots,n.
$$

这一变换是一一的，Jacobi 行列式的绝对值为 $1$，所以 $\bar X$ 对 $\boldsymbol{X}$ 的充分性等价于 $Y_1$ 对 $\boldsymbol{Y}$ 的充分性。由定理 2.1.3 的证明，$Y_1,\dots,Y_n$ 相互独立，$Y_1\sim\mathcal{N}(\sqrt n\theta,1)$，$i\ge2$ 时 $Y_i\sim\mathcal{N}(0,1)$。于是 $\boldsymbol{Y}$ 的联合密度与 $Y_1$ 的边缘密度为

$$
f(y_1,\dots,y_n)=(2\pi)^{-n/2}\exp\left\{-\frac12(y_1-\sqrt n\theta)^2-\frac12\sum_{i=2}^ny_i^2\right\},\qquad f_{Y_1}(y_1)=(2\pi)^{-1/2}\exp\left\{-\frac12(y_1-\sqrt n\theta)^2\right\},
$$
给定 $Y_1=y_1$ 时 $\boldsymbol{Y}$ 的条件密度为

$$
f(y_1,\dots,y_n\mid y_1)=\frac{f(y_1,\dots,y_n)}{f_{Y_1}(y_1)}=(2\pi)^{-(n-1)/2}\exp\left\{-\frac12\sum_{i=2}^ny_i^2\right\},
$$
它与 $\theta$ 无关。

**例 2.3.3** 在例 2.3.2 中，$T(\boldsymbol{X})=X_1$ 不是充分统计量：它只用了一个观测值，不含 $X_2,\dots,X_n$ 中的信息。事实上

$$
f(x_1,\dots,x_n\mid x_1)=\frac{f(x_1,\dots,x_n)}{f_{X_1}(x_1)}=f(x_2,\dots,x_n)=(2\pi)^{-(n-1)/2}\exp\left\{-\frac12\sum_{i=2}^n(x_i-\theta)^2\right\}
$$
依赖于 $\theta$。

### 2.3.2. 因子分解定理

用条件分布验证充分性很繁琐。因子分解定理由 Fisher 在 1920 年代提出，最一般的形式及严格证明由 P. R. Halmos 与 L. J. Savage（1949）借助 Radon–Nikodym 定理给出；它把问题归结为考察联合密度。

**定理 2.3.1（因子分解定理）** 设 $f(\boldsymbol{x};\theta)$ 为样本 $\boldsymbol{X}=(X_1,\dots,X_n)$ 的联合密度，$T(\boldsymbol{X})$ 为统计量。则 $T(\boldsymbol{X})$ 是 $\theta$ 的充分统计量，当且仅当存在非负函数 $g$ 与 $h$ 使得

$$
f(\boldsymbol{x};\theta)=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x})\qquad\text{对一切 }\boldsymbol{x}\text{ 与 }\theta\text{ 成立},
$$
其中 $t(\boldsymbol{x})$ 是 $T(\boldsymbol{X})$ 的观测值；即 $g$ 只通过 $T$ 依赖于样本，$h$ 与 $\theta$ 无关。

**证明** 离散情形。若 $f=g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$，则对满足 $t(\boldsymbol{x})=t$ 的 $\boldsymbol{x}$，

$$
\mathbb{P}_\theta(\boldsymbol{X}=\boldsymbol{x}\mid T=t)=\frac{g(t;\theta)h(\boldsymbol{x})}{\sum_{\boldsymbol{y}\colon t(\boldsymbol{y})=t}g(t;\theta)h(\boldsymbol{y})}=\frac{h(\boldsymbol{x})}{\sum_{\boldsymbol{y}\colon t(\boldsymbol{y})=t}h(\boldsymbol{y})},
$$
与 $\theta$ 无关。反之，若 $T$ 充分，则 $f(\boldsymbol{x};\theta)=\mathbb{P}_\theta(T=t(\boldsymbol{x}))\,\mathbb{P}(\boldsymbol{X}=\boldsymbol{x}\mid T=t(\boldsymbol{x}))$ 就是所要求形式的分解。

连续情形。设 $\boldsymbol{T}=(T_1,\dots,T_k)$，$k\le n$，取 $n-k$ 维统计量 $\boldsymbol{Y}=(Y_1,\dots,Y_{n-k})$，使 $\boldsymbol{X}\mapsto(\boldsymbol{T},\boldsymbol{Y})$ 是一一的且有连续的一阶偏导数，于是 $X_i=X_i(\boldsymbol{T},\boldsymbol{Y})$。记 Jacobi 行列式的绝对值为 $w(\boldsymbol{t},\boldsymbol{y})=\left|\frac{\partial(x_1,\dots,x_n)}{\partial(\boldsymbol{t},\boldsymbol{y})}\right|$。

充分性："若"。$(\boldsymbol{T},\boldsymbol{Y})$ 的联合密度为

$$
k(\boldsymbol{t},\boldsymbol{y};\theta)=f(\boldsymbol{x};\theta)\,w(\boldsymbol{t},\boldsymbol{y})=g(\boldsymbol{t};\theta)\,h\big(x_1(\boldsymbol{t},\boldsymbol{y}),\dots,x_n(\boldsymbol{t},\boldsymbol{y})\big)\,w(\boldsymbol{t},\boldsymbol{y})=g(\boldsymbol{t};\theta)\,\mu(\boldsymbol{t},\boldsymbol{y}),
$$
其中 $\mu$ 与 $\theta$ 无关。$\boldsymbol{T}$ 的边缘密度为 $V(\boldsymbol{t};\theta)=g(\boldsymbol{t};\theta)\int\mu(\boldsymbol{t},\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$，所以给定 $\boldsymbol{T}=\boldsymbol{t}$ 时 $\boldsymbol{Y}$ 的条件密度

$$
q(\boldsymbol{y}\mid\boldsymbol{t})=\frac{k(\boldsymbol{t},\boldsymbol{y};\theta)}{V(\boldsymbol{t};\theta)}=\frac{\mu(\boldsymbol{t},\boldsymbol{y})}{\int_{\mathbb{R}^{n-k}}\mu(\boldsymbol{t},\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}}
$$
与 $\theta$ 无关。由于 $\boldsymbol{X}$ 是 $(\boldsymbol{T},\boldsymbol{Y})$ 的函数，给定 $\boldsymbol{T}$ 时 $\boldsymbol{X}$ 的条件分布也与 $\theta$ 无关。

必要性："仅若"。若 $\boldsymbol{T}$ 充分，则 $q(\boldsymbol{y}\mid\boldsymbol{t})$ 与 $\theta$ 无关，且 $k(\boldsymbol{t},\boldsymbol{y};\theta)=q(\boldsymbol{y}\mid\boldsymbol{t})V(\boldsymbol{t};\theta)$。变换回去，

$$
f(\boldsymbol{x};\theta)=k(\boldsymbol{t},\boldsymbol{y};\theta)\left|\frac{\partial(\boldsymbol{t},\boldsymbol{y})}{\partial(x_1,\dots,x_n)}\right|=V(\boldsymbol{t}(\boldsymbol{x});\theta)\cdot q(\boldsymbol{y}(\boldsymbol{x})\mid\boldsymbol{t}(\boldsymbol{x}))\left|\frac{\partial(\boldsymbol{t},\boldsymbol{y})}{\partial(x_1,\dots,x_n)}\right|,
$$
即 $g=V$ 时的 $g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$。$\square$

**例 2.3.4** 因子分解定理立即给出例 2.3.1 与例 2.3.2 的结论。对 $\mathrm{Ber}(\theta)$，记 $t=\sum x_i$，$f(\boldsymbol{x};\theta)=\theta^t(1-\theta)^{n-t}=g(t(\boldsymbol{x});\theta)\cdot1$。对 $\mathcal{N}(\theta,1)$，记 $t=\bar x$，

$$
f(\boldsymbol{x};\theta)=(2\pi)^{-n/2}\exp\left\{-\frac12\sum_{i=1}^n(x_i-\theta)^2\right\}=\underbrace{(2\pi)^{-n/2}\mathrm{e}^{-\frac{n\theta^2}2+n\theta t}}_{g(t;\theta)}\cdot\underbrace{\mathrm{e}^{-\frac12\sum_{i=1}^nx_i^2}}_{h(\boldsymbol{x})}.
$$

**例 2.3.5** 设 $X_1,\dots,X_n$ 是取自 $\mathrm{U}(0,\theta)$ 的样本，则 $T(\boldsymbol{X})=X_{(n)}$ 是 $\theta$ 的充分统计量，因为

$$
f(\boldsymbol{x};\theta)=\frac1{\theta^n}\boldsymbol{1}_{\{0<x_i<\theta,\ i=1,\dots,n\}}=\frac1{\theta^n}\boldsymbol{1}_{\{x_{(n)}<\theta\}}\cdot\boldsymbol{1}_{\{x_{(1)}>0\}}=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x}).
$$

**例 2.3.6（指数族中的充分性）** 设 $\boldsymbol{X}$ 是取自指数族的样本，则 $T(\boldsymbol{X})=(T_1(\boldsymbol{X}),\dots,T_k(\boldsymbol{X}))$ 是 $\theta$ 的充分统计量，因为

$$
f(\boldsymbol{x};\theta)=C(\theta)\exp\left\{\sum_{i=1}^kQ_i(\theta)t_i(\boldsymbol{x})\right\}h(\boldsymbol{x})=g(t(\boldsymbol{x});\theta)\,h(\boldsymbol{x}).
$$

对正态样本，$(\sum X_i,\sum X_i^2)$，或等价地 $(\bar X,S^2)$，是 $(\mu,\sigma^2)$ 的充分统计量；对 Gamma 样本，$(\sum X_i,\sum\log X_i)$ 是 $(\gamma,\lambda)$ 的充分统计量。

### 2.3.3. 极小充分统计量

充分统计量不唯一。在例 2.3.2 中，$T(\boldsymbol{X})=\bar X$ 是充分统计量，对任意 $1\le m<n$，$T_1(\boldsymbol{X})=\left(\sum_{i=1}^mX_i,\ \sum_{i=m+1}^nX_i\right)$ 也是；$T$ 是 $T_1$ 的函数，而且更简单。整个样本总是充分的。我们要寻求最大限度的简化。

**定义 2.3.2（极小充分统计量）** 若一个充分统计量能表示为其他任一充分统计量的函数，则称它为**极小充分统计量**。

极小充分统计量在不损失信息的前提下实现了最大限度的数据压缩。对自然参数空间有内点的自然形式指数族，$(T_1,\dots,T_k)$ 是极小充分统计量。

### 2.3.4. 完全统计量

完全性仿照正交函数系的完全性：函数系 $M$ 称为完全的，是指与 $M$ 中每个函数都正交的函数只有 $0$。对统计量而言，完全性是无偏估计唯一性的关键（[3.2.3](/3.2.3) 中的 UMVUE 理论）。

**定义 2.3.3（完全统计量）** 设 $\mathcal{F}=\{f(x;\theta)\colon\theta\in\Theta\}$ 是参数空间为 $\Theta$ 的分布族，$T=T(\boldsymbol{X})$ 为统计量。若对任何满足

$$
\mathbb{E}_\theta[\varphi(T(\boldsymbol{X}))]=0\qquad\text{对一切 }\theta\in\Theta
$$
的函数 $\varphi$，都有

$$
\mathbb{P}_\theta(\varphi(T(\boldsymbol{X}))=0)=1\qquad\text{对一切 }\theta\in\Theta,
$$
则称 $T(\boldsymbol{X})$ 是 $\theta$ 的**完全统计量**。

若 $T$ 有密度 $g(t;\theta)$，条件即：由 $\int\varphi(t)g(t;\theta)\,\mathrm{d}t=0$ 对一切 $\theta$ 成立，可推出 $\varphi$ 在支撑上几乎处处为 $0$。也就是说，与整个函数族 $\{g(t;\theta)\colon\theta\in\Theta\}$ 都"正交"的函数只有 $0$，$T$ 的完全性就是这个函数族的完全性。由定义立即可得两点：若 $T$ 完全，则对任何可测函数 $\delta$，$\delta(T)$ 也完全（对 $\varphi\circ\delta$ 应用定义）；若 $T$ 完全，两个对每个 $\theta$ 期望都相同的函数 $\varphi_1(T)$、$\varphi_2(T)$ 以概率 1 相等。

**例 2.3.7** 设 $X_1,\dots,X_n$ 是取自 $\mathrm{Ber}(\theta)$ 的样本，则 $T(\boldsymbol{X})=\sum X_i$ 对 $\theta\in(0,1)$ 是完全的。事实上 $T\sim\mathrm{Bin}(n,\theta)$，$\mathbb{E}_\theta\varphi(T)=0$（$0<\theta<1$）意味着

$$
\sum_{k=0}^n\varphi(k)\binom nk\theta^k(1-\theta)^{n-k}=0\quad\Longleftrightarrow\quad\sum_{k=0}^n\varphi(k)\binom nk\delta^k=0,\qquad\delta=\frac\theta{1-\theta}\in(0,\infty).
$$

次数不超过 $n$ 的 $\delta$ 的多项式在 $(0,\infty)$ 上恒为零，则其系数全为零，所以 $\varphi(k)\binom nk=0$，即 $\varphi(k)=0$，$k=0,1,\dots,n$。而 $\{0,1,\dots,n\}$ 是 $T$ 的支撑，故 $\mathbb{P}_\theta(\varphi(T)=0)=1$。

**例 2.3.8** 设 $X_1,\dots,X_n$ 是取自 $\mathcal{N}(\theta,1)$（$\theta\in\mathbb{R}$）的样本，则 $T(\boldsymbol{X})=\bar X$ 是完全的。由推论 2.1.2，$\bar X\sim\mathcal{N}(\theta,1/n)$，所以 $\mathbb{E}_\theta\varphi(T)=0$ 对一切 $\theta$ 成立意味着

$$
\sqrt{\frac n{2\pi}}\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-n(t-\theta)^2/2}\,\mathrm{d}t=\sqrt{\frac n{2\pi}}\,\mathrm{e}^{-n\theta^2/2}\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{nt\theta}\,\mathrm{d}t=0,
$$
从而，令 $z=n\theta$，

$$
G(z)=\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{tz}\,\mathrm{d}t=0,\qquad-\infty<z<\infty.
$$

由于积分对每个实数 $z$ 绝对收敛，$G$ 可延拓为复变量 $z$ 的**整函数**，且在实轴上为零；由解析函数的唯一性定理，$G(z)=0$ 对一切 $z\in\mathbb{C}$ 成立。取 $z=-\mathrm{i}u$ 得

$$
\int_{-\infty}^\infty\varphi(t)\mathrm{e}^{-nt^2/2}\mathrm{e}^{-\mathrm{i}ut}\,\mathrm{d}t=0,\qquad u\in\mathbb{R},
$$
即 $\varphi(t)\mathrm{e}^{-nt^2/2}$ 的 **Fourier 变换**恒为零，所以 $\varphi(t)\mathrm{e}^{-nt^2/2}=0$ 对几乎所有 $t$ 成立，即 $\varphi$ 几乎处处为 $0$。因此 $T$ 是完全的。

**例 2.3.9** 设 $X_1,\dots,X_n$ 是取自 $\mathrm{U}(0,\theta)$（$\theta>0$）的样本，则 $T(\boldsymbol{X})=X_{(n)}$ 是完全的。$X_{(n)}$ 的密度为 $g(t;\theta)=nt^{n-1}\theta^{-n}\boldsymbol{1}_{(0,\theta)}(t)$，所以 $\mathbb{E}_\theta\varphi(T)=0$ 对一切 $\theta>0$ 成立意味着

$$
\frac n{\theta^n}\int_0^\theta\varphi(t)t^{n-1}\,\mathrm{d}t=0,\quad\text{即}\quad\int_0^\theta\varphi(t)t^{n-1}\,\mathrm{d}t=0\qquad\text{对一切 }\theta>0.
$$

对 $\theta$ 求导得 $\theta^{n-1}\varphi(\theta)=0$，所以 $\varphi(\theta)=0$ 对几乎所有 $\theta>0$ 成立（在每个连续点处成立），从而 $\mathbb{P}_\theta(\varphi(T)=0)=1$。

这些例子都是下面一般定理的特例。

**定理 2.3.2（指数族中的完全性）** 设 $\boldsymbol{X}$ 是取自自然形式指数族的样本，联合密度为

$$
f(\boldsymbol{x};\theta)=C(\theta)\exp\left\{\sum_{i=1}^k\theta_iT_i(\boldsymbol{x})\right\}h(\boldsymbol{x}),\qquad\theta=(\theta_1,\dots,\theta_k)\in\Theta^*.
$$

若自然参数空间 $\Theta^*$ 作为 $\mathbb{R}^k$ 的子集有内点，则 $T(\boldsymbol{X})=(T_1(\boldsymbol{X}),\dots,T_k(\boldsymbol{X}))$ 是 $\theta$ 的完全统计量。

证明推广了例 2.3.8 的论证：$\mathbb{E}_\theta\varphi(T)$ 在 $\theta$ 的一个开集上为零，使一个多元 **Laplace 变换**在开集上为零，由解析性它处处为零，再由其唯一性得 $\varphi=0$；细节从略。

**例 2.3.10** 设 $X_1,\dots,X_n$ 是取自 $\mathcal{N}(\mu,\sigma^2)$ 的样本，$\Theta=\{(\mu,\sigma^2)\colon-\infty<\mu<\infty,\ \sigma^2>0\}$，则 $(\bar X,S^2)$ 是 $\theta=(\mu,\sigma^2)$ 的完全统计量。由例 2.2.6，自然参数空间 $\Theta^*=\{(\varphi_1,\varphi_2)\colon\varphi_1\in\mathbb{R},\ \varphi_2<0\}$ 是开半平面，由定理 2.3.2，$(\sum X_i,\sum X_i^2)$ 是完全的，而 $(\bar X,S^2)$ 是它的函数，也是完全的。若 $\sigma^2$ 已知，则分布族是单参数指数族，自然参数 $\mu/\sigma^2$ 取遍 $\mathbb{R}$，$T=\sum X_i$，所以 $\bar X$ 完全；若 $\mu$ 已知，则自然参数为 $-1/(2\sigma^2)\in(-\infty,0)$，$\sum(X_i-\mu)^2$ 完全。

**例 2.3.11（充分但不完全的统计量）** 设 $X_1,\dots,X_n$（$n\ge2$）是取自 $\mathrm{U}(\theta-\frac12,\theta+\frac12)$（$\theta\in\mathbb{R}$）的样本。由于

$$
f(\boldsymbol{x};\theta)=\boldsymbol{1}_{\{\theta-1/2<x_{(1)}\}}\boldsymbol{1}_{\{x_{(n)}<\theta+1/2\}},
$$
由因子分解定理，$T(\boldsymbol{X})=(X_{(1)},X_{(n)})$ 是充分统计量。它不是完全的：要找 $\varphi$ 使 $\mathbb{E}_\theta\varphi(T)=0$ 但 $\mathbb{P}_\theta(\varphi(T)=0)\ne1$。令 $Y_i=X_i-(\theta-\frac12)$，则 $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathrm{U}(0,1)$，分布与 $\theta$ 无关，所以极差 $Z=X_{(n)}-X_{(1)}=Y_{(n)}-Y_{(1)}$ 的分布与 $\theta$ 无关，且 $\mathbb{E}[Z]=\frac{n-1}{n+1}$。因此 $\varphi(T)=X_{(n)}-X_{(1)}-\frac{n-1}{n+1}$ 对每个 $\theta$ 期望都为 $0$，但它是连续型随机变量，并不以概率 1 为零。（也可以取常数 $a<b$ 使 $\mathbb{P}(Z<a)=\mathbb{P}(Z>b)>0$，令 $\varphi$ 在 $\{Z<a\}$ 上为 $1$、在 $\{Z>b\}$ 上为 $-1$、其余为 $0$；这个 $\varphi$ 是有界的。）

这个例子显示了典型的障碍：若充分统计量的某个非常数函数的分布与 $\theta$ 无关，它就不是完全的。

### 2.3.5. 有界完全性与 Basu 定理

**定义 2.3.4（有界完全统计量）** 若定义 2.3.3 中的推断对每个有界函数 $\varphi$ 成立，则称 $T(\boldsymbol{X})$ 是 $\theta$ 的**有界完全统计量**。

完全统计量一定是有界完全的，因为条件只对更少的函数提出要求；反之一般不成立。例 2.3.11 末尾构造的有界 $\varphi$ 表明 $(X_{(1)},X_{(n)})$ 甚至不是有界完全的。

**定义 2.3.5（辅助统计量）** 分布与 $\theta$ 无关的统计量 $V(\boldsymbol{X})$ 称为**辅助统计量**。

辅助统计量本身不提供关于 $\theta$ 的任何信息。例 2.3.11 中的极差就是辅助统计量。Basu 定理说明：辅助统计量与任何有界完全的充分统计量独立。

**定理 2.3.3（Basu 定理）** 设 $T(\boldsymbol{X})$ 是 $\theta$ 的有界完全的充分统计量。若 $V(\boldsymbol{X})$ 的分布与 $\theta$ 无关，则对每个 $\theta\in\Theta$，$V(\boldsymbol{X})$ 与 $T(\boldsymbol{X})$ 相互独立。

**证明** 固定集合 $B$，记 $p_B=\mathbb{P}_\theta(V\in B)$，由于 $V$ 是辅助统计量，它与 $\theta$ 无关。令 $\eta(T)=\mathbb{P}(V\in B\mid T)$；由于 $T$ 充分，给定 $T$ 时样本的条件分布与 $\theta$ 无关，从而 $\eta$ 也与 $\theta$ 无关，$\eta(T)$ 是统计量。它是有界的，且对每个 $\theta$，$\mathbb{E}_\theta[\eta(T)-p_B]=\mathbb{P}_\theta(V\in B)-p_B=0$。由有界完全性，$\eta(T)=p_B$ 以概率 1 成立，即 $\mathbb{P}(V\in B\mid T)=\mathbb{P}(V\in B)$，所以 $V$ 与 $T$ 独立。$\square$

这一定理由 D. Basu（1955）给出，它提供了一种不必计算联合分布就能证明独立性的便捷方法。

**例 2.3.12** 设 $X_1,\dots,X_n$ 是取自 $\mathcal{N}(\theta,1)$ 的样本，$R(\boldsymbol{X})=X_{(n)}-X_{(1)}$ 为样本极差，$T(\boldsymbol{X})=\bar X$，则 $R$ 与 $T$ 相互独立。由例 2.3.2 与例 2.3.8，$T$ 是充分且完全的。令 $Y_i=X_i-\theta$，则 $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，分布与 $\theta$ 无关，所以 $R(\boldsymbol{X})=Y_{(n)}-Y_{(1)}$ 的分布与 $\theta$ 无关。由 Basu 定理，$T$ 与 $R$ 相互独立。

同样的论证给出定理 2.1.3(3) 的另一个证明。固定 $\sigma^2$，以 $\{\mathcal{N}(\mu,\sigma^2)\colon\mu\in\mathbb{R}\}$ 为模型；$\bar X$ 是 $\mu$ 的完全充分统计量（例 2.3.10），而 $S^2$ 是离差 $X_i-\mu$ 的函数，其分布与 $\mu$ 无关，所以 $S^2$ 是辅助统计量。因此对每个 $\mu$，$\bar X$ 与 $S^2$ 独立，而 $\sigma^2$ 是任意的。没有正态性，结论就不成立，下面对样本均值与极差的模拟说明了这一点。

![3000 个容量为 10 的样本的样本均值与样本极差散点图：正态样本不相关，指数样本明显相关](./plots/basu-independence.py)

## 小结

| 主题 | 主要结论 |
|---|---|
| 正态样本 | $\bar X\sim\mathcal{N}(a,\sigma^2/n)$，$(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$，$\bar X$ 与 $S^2$ 独立 |
| $\chi^2_r$ | $r$ 个独立 $\mathcal{N}(0,1)$ 的平方和；均值 $r$，方差 $2r$；可加 |
| $t_r$ | $X/\sqrt{Y/r}$；对称，厚尾；$t_1$ 为 Cauchy 分布；$t_r\to\mathcal{N}(0,1)$ |
| $F_{r_1,r_2}$ | $(X/r_1)/(Y/r_2)$；$1/F\sim F_{r_2,r_1}$；$t_r^2\sim F_{1,r}$；$F_{r_1,r_2,1-\alpha}=1/F_{r_2,r_1,\alpha}$ |
| 枢轴量 | $\sqrt n(\bar X-a)/S\sim t_{n-1}$；合并方差 $S_w$ 的两样本 $t$；方差比 $F_{m-1,n-1}$；$2\lambda\sum X_i\sim\chi^2_{2n}$ |
| 极限分布 | 中心极限定理加 Slutsky 定理：对任何方差有限的总体 $\sqrt n(\bar X-a)/S\xrightarrow{d}\mathcal{N}(0,1)$ |
| 指数族 | $C(\theta)\exp\{\sum Q_i(\theta)T_i(x)\}h(x)$；支撑固定；$\Theta^*$ 凸；$\mathbb{E}T_i=-\partial_iD$，$\operatorname{Cov}(T_i,T_j)=-\partial_i\partial_jD$ |
| 充分性 | 给定 $T$ 时样本的条件分布与 $\theta$ 无关；因子分解 $f=g(t(\boldsymbol{x});\theta)h(\boldsymbol{x})$ |
| 完全性 | $\mathbb{E}_\theta\varphi(T)=0$ 对一切 $\theta$ 成立蕴含 $\varphi(T)=0$ a.s.；有内点的指数族中 $(T_1,\dots,T_k)$ 完全 |
| Basu 定理 | 有界完全的充分统计量与辅助统计量独立 |
