---
title: 典型相关分析
description: 两组变量的典型相关分析：用奇异值分解求总体典型变量，通过系数与相关系数解释典型变量，对标准化的不变性，样本典型相关及例子，典型变量对个数的似然比检验，以及推广。
source_hash: e473cde8449a
---

常常在同一批个体上测量两类不同的变量：运动变量（在台阶机上的攀爬速度、跑一定距离的速度、卧推重量、每分钟俯卧撑个数）与健康变量（血压、胆固醇、血糖水平、体重指数）；销售业绩与能力测验成绩；图像特征与图像说明文字中的词语。典型相关分析（canonical correlation analysis），简称 CCA，由 H. Hotelling（1936）提出，它通过少数几对线性组合——每组变量各取一个，使其相关尽可能大——来研究两组变量之间的关联。它识别并量化两组变量之间的关联，并把含 $pq$ 个元素的交叉协方差矩阵 $\Sigma_{12}$ 约简为 $p$ 个典型相关系数。与**主成分分析**（[3.4.5](/3.4.5)）一样，它在不相关约束下逐次最大化，但最大化的是两组之间的相关而不是一组之内的方差，它的解来自一个标准化的交叉协方差矩阵的**奇异值分解**（[2.1](/2.1)）。第一组只有一个变量时，它就是回归中的复相关（[3.4.7](/3.4.7)）；因子分析（[3.4.8](/3.4.8)）对两组变量有一个概率版本，见 9.5 节；9.4 节的似然比检验依赖于**多元正态分布**（[3.4.2](/3.4.2)）。这一方法是许多现代多视图数据技术的出发点，例如图像与文本的跨模态检索，以及把脑成像数据与行为测量联系起来。

## 9.1. 问题

设 $\boldsymbol{X}^{(1)}=(X_1^{(1)},\dots,X_p^{(1)})^{\mathsf T}$ 与 $\boldsymbol{X}^{(2)}=(X_1^{(2)},\dots,X_q^{(2)})^{\mathsf T}$ 是两个随机向量，$p\le q$，联合协方差矩阵为

$$
\Sigma=\operatorname{Cov}\begin{bmatrix}\boldsymbol{X}^{(1)}\\\boldsymbol{X}^{(2)}\end{bmatrix}=\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix},\qquad\Sigma_{11}\in\mathbb{R}^{p\times p},\quad\Sigma_{12}=\Sigma_{21}^{\mathsf T}\in\mathbb{R}^{p\times q},\quad\Sigma_{22}\in\mathbb{R}^{q\times q}.
$$
两组之间的关联包含在 $\Sigma_{12}$ 中，但它的 $pq$ 个元素难以把握。目标是找系数向量 $\boldsymbol{a}\in\mathbb{R}^p$ 与 $\boldsymbol{b}\in\mathbb{R}^q$，使

$$
U=\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)}=a_1X_1^{(1)}+\cdots+a_pX_p^{(1)},\qquad V=\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)}=b_1X_1^{(2)}+\cdots+b_qX_q^{(2)}
$$
的相关尽可能大，再找刻画其余关联的后续各对。

**例 9.1.1（Hotelling 的阅读与算术数据）** Hotelling 最初的例子把 $\boldsymbol{X}^{(1)}$ =（阅读速度，阅读能力）与 $\boldsymbol{X}^{(2)}$ =（算术速度，算术能力）联系起来，$p=q=2$，

$$
\Sigma=\begin{bmatrix}100&60&30&7.2\\60&100&-6&8.4\\30&-6&144&57.6\\7.2&8.4&57.6&144\end{bmatrix},\qquad\rho=\begin{bmatrix}1&0.6&0.25&0.06\\0.6&1&-0.05&0.07\\0.25&-0.05&1&0.4\\0.06&0.07&0.4&1\end{bmatrix}.
$$
四个交叉相关 $0.25,0.06,-0.05,0.07$ 都很小且符号不一；阅读成绩的哪些组合与算术成绩的哪些组合相关？

## 9.2. 总体典型相关

### 9.2.1. 定义

由于 $\operatorname{Var}(U)=\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}$，$\operatorname{Var}(V)=\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}$，$\operatorname{Cov}(U,V)=\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}$，目标为

$$
\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\operatorname{Corr}(U,V)=\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}.
$$
把 $\boldsymbol{a}$ 换成 $c\boldsymbol{a}$（$c>0$）不改变相关系数，所以可以规定 $\operatorname{Var}(U)=\operatorname{Var}(V)=1$。

**定义 9.2.1（典型相关系数）** 第一对典型变量 $(U_1,V_1)=(\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}_1^{\mathsf T}\boldsymbol{X}^{(2)})$ 在 $\operatorname{Var}(U)=\operatorname{Var}(V)=1$ 的约束下使 $\operatorname{Corr}(U,V)$ 最大。对 $k=2,\dots,p$，第 $k$ 对典型变量 $(U_k,V_k)=(\boldsymbol{a}_k^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}_k^{\mathsf T}\boldsymbol{X}^{(2)})$ 在约束

$$
\boldsymbol{a}_k^{\mathsf T}\Sigma_{11}\boldsymbol{a}_k=1,\quad\boldsymbol{b}_k^{\mathsf T}\Sigma_{22}\boldsymbol{b}_k=1,\quad\operatorname{Cov}(U_k,U_i)=\boldsymbol{a}_k^{\mathsf T}\Sigma_{11}\boldsymbol{a}_i=0,\quad\operatorname{Cov}(V_k,V_i)=\boldsymbol{b}_k^{\mathsf T}\Sigma_{22}\boldsymbol{b}_i=0\qquad(i<k)
$$
下使 $\operatorname{Corr}(U,V)$ 最大。称 $U_k$ 与 $V_k$ 为**典型变量**，$\rho_k^*=\operatorname{Corr}(U_k,V_k)$ 为第 $k$ 个**典型相关系数**。

这一构造与 PCA 平行：找到最好的一对之后，再找与前面各对不相关的最好的一对。

### 9.2.2. 典型变量的求法

**定理 9.2.1** 设 $p\le q$，$\boldsymbol{X}^{(1)}$ 与 $\boldsymbol{X}^{(2)}$ 的联合协方差矩阵 $\Sigma$ 满秩。设 $\rho_1^{*2}\ge\cdots\ge\rho_p^{*2}$ 是

$$
\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}
$$
的特征值，$\boldsymbol{e}_1,\dots,\boldsymbol{e}_p$ 为相应的标准正交特征向量。则 $\rho_1^{*2},\dots,\rho_p^{*2}$ 也是 $\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1/2}$ 的前 $p$ 个最大特征值，相应的标准正交特征向量为 $\boldsymbol{f}_k=\frac{1}{\rho_k^*}\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1/2}\boldsymbol{e}_k$（当 $\rho_k^*>0$），并且

$$
\max_{\boldsymbol{a},\boldsymbol{b}}\operatorname{Corr}(U,V)=\rho_1^*,
$$
由第一对典型变量 $U_1=\boldsymbol{e}_1^{\mathsf T}\Sigma_{11}^{-1/2}\boldsymbol{X}^{(1)}$、$V_1=\boldsymbol{f}_1^{\mathsf T}\Sigma_{22}^{-1/2}\boldsymbol{X}^{(2)}$ 达到。第 $k$ 对 $U_k=\boldsymbol{e}_k^{\mathsf T}\Sigma_{11}^{-1/2}\boldsymbol{X}^{(1)}$、$V_k=\boldsymbol{f}_k^{\mathsf T}\Sigma_{22}^{-1/2}\boldsymbol{X}^{(2)}$ 在与前 $1,\dots,k-1$ 个典型变量不相关的线性组合中使相关系数最大，$\operatorname{Corr}(U_k,V_k)=\rho_k^*$，$k=2,\dots,p$。于是 $\boldsymbol{a}_k=\Sigma_{11}^{-1/2}\boldsymbol{e}_k$，$\boldsymbol{b}_k=\Sigma_{22}^{-1/2}\boldsymbol{f}_k$。

**证明** 令 $\tilde{\boldsymbol{a}}=\Sigma_{11}^{1/2}\boldsymbol{a}$，$\tilde{\boldsymbol{b}}=\Sigma_{22}^{1/2}\boldsymbol{b}$；规范化条件变为 $\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1$，且

$$
\max_{\boldsymbol{a},\boldsymbol{b}\ne\boldsymbol{0}}\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}=\max_{\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1}\tilde{\boldsymbol{a}}^{\mathsf T}\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}\tilde{\boldsymbol{b}}=\max_{\|\tilde{\boldsymbol{a}}\|=\|\tilde{\boldsymbol{b}}\|=1}\tilde{\boldsymbol{a}}^{\mathsf T}Y\tilde{\boldsymbol{b}},\qquad Y=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}.
$$
设 $Y=P_1\Lambda P_2^{\mathsf T}$ 是奇异值分解，$P_1$（$p\times p$）与 $P_2$（$q\times q$）正交，$\Lambda$ 是对角元为 $\lambda_1\ge\cdots\ge\lambda_p\ge0$、其余为零的 $p\times q$ 矩阵。则 $\boldsymbol{c}=P_1^{\mathsf T}\tilde{\boldsymbol{a}}$ 与 $\boldsymbol{d}=P_2^{\mathsf T}\tilde{\boldsymbol{b}}$ 仍是单位向量，由 **Cauchy–Schwarz 不等式**，

$$
\tilde{\boldsymbol{a}}^{\mathsf T}Y\tilde{\boldsymbol{b}}=\boldsymbol{c}^{\mathsf T}\Lambda\boldsymbol{d}=\sum_{i=1}^p\lambda_ic_id_i\le\sum_{i=1}^p\lambda_i\lvert c_i\rvert\lvert d_i\rvert\le\lambda_1\sum_{i=1}^p\lvert c_i\rvert\lvert d_i\rvert\le\lambda_1\|\boldsymbol{c}\|\|\boldsymbol{d}\|=\lambda_1,
$$
当 $\boldsymbol{c}$、$\boldsymbol{d}$ 为第一个标准基向量，即 $\tilde{\boldsymbol{a}}$、$\tilde{\boldsymbol{b}}$ 为 $P_1$、$P_2$ 的第一列——$Y$ 的第一对左、右**奇异向量**——时等号成立。由于 $YY^{\mathsf T}=P_1\Lambda\Lambda^{\mathsf T}P_1^{\mathsf T}=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\Sigma_{11}^{-1/2}$，$Y^{\mathsf T}Y=P_2\Lambda^{\mathsf T}\Lambda P_2^{\mathsf T}$，左奇异向量就是各 $\boldsymbol{e}_k$，右奇异向量就是各 $\boldsymbol{f}_k$，$\lambda_k^2=\rho_k^{*2}$，而 $Y^{\mathsf T}\boldsymbol{e}_k=\lambda_k\boldsymbol{f}_k$ 给出 $\boldsymbol{f}_k$ 的公式。

对第 $k$ 对，$\operatorname{Cov}(U,U_i)=\tilde{\boldsymbol{a}}^{\mathsf T}\boldsymbol{e}_i=c_i$，$\operatorname{Cov}(V,V_i)=d_i$，所以约束迫使 $i<k$ 时 $c_i=d_i=0$；同样的不等式链从 $i=k$ 开始，给出最大值 $\lambda_k$，在 $\tilde{\boldsymbol{a}}=\boldsymbol{e}_k$、$\tilde{\boldsymbol{b}}=\boldsymbol{f}_k$ 处达到。$\square$

这个证明借助 SVD 一并处理两个向量。也可以逐个击破：对固定的 $\tilde{\boldsymbol{a}}$，由 Cauchy–Schwarz 不等式，最好的 $\tilde{\boldsymbol{b}}=Y^{\mathsf T}\tilde{\boldsymbol{a}}/\|Y^{\mathsf T}\tilde{\boldsymbol{a}}\|$，取值 $\|Y^{\mathsf T}\tilde{\boldsymbol{a}}\|=\sqrt{\tilde{\boldsymbol{a}}^{\mathsf T}YY^{\mathsf T}\tilde{\boldsymbol{a}}}$；在单位向量 $\tilde{\boldsymbol{a}}$ 上最大化这个 **Rayleigh 商**，得到 $YY^{\mathsf T}$ 的最大特征值，在 $\boldsymbol{e}_1$ 处达到；于是 $\tilde{\boldsymbol{b}}=Y^{\mathsf T}\boldsymbol{e}_1/\rho_1^*=\boldsymbol{f}_1$。第三条途径是 Lagrange 乘子法，它导出广义特征值问题 $\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\boldsymbol{a}=\rho^2\Sigma_{11}\boldsymbol{a}$，即 $\lvert\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}-\rho^2\Sigma_{11}\rvert=0$；这种形式可以推广到核 CCA。

**例 9.2.1（Hotelling 数据，续）** 对例 9.1.1 的 $\Sigma$，特征值为 $\rho_1^{*2}\approx0.146$、$\rho_2^{*2}\approx0.005$，故 $\rho_1^*\approx0.38$，$\rho_2^*\approx0.07$，且

$$
U_1=\boldsymbol{a}_1^{\mathsf T}\boldsymbol{X}^{(1)}=-0.12X_1^{(1)}+0.10X_2^{(1)},\qquad V_1=\boldsymbol{b}_1^{\mathsf T}\boldsymbol{X}^{(2)}=-0.09X_1^{(2)}+0.03X_2^{(2)}.
$$
两组的最佳线性组合的相关系数为 $0.38$，大于每一个单独的交叉相关（至多 $0.25$）；第二对几乎不相关。（$\boldsymbol{a}_k$ 与 $\boldsymbol{b}_k$ 的符号可以同时反号。）$U_1$ 与 $V_1$ 应当如何解释？

### 9.2.3. 典型变量的解释

刻画一个典型变量有两类量。

- 典型系数，即 $\boldsymbol{a}_i^{\mathsf T}=(a_{i1},\dots,a_{ip})$ 的元素 $a_{ik}$，衡量在同组其他变量给定时第 $k$ 个变量 $X_k^{(1)}$ 对 $U_i$ 的贡献（一种多元的度量，类似回归系数）。它们依赖于变量的单位，变量相关时其符号可能产生误导。
- 典型变量与原始变量之间的相关系数（一种单变量的度量，类似载荷）显示每个变量单独与该典型变量的关系有多强。

写成矩阵形式，令 $A=[\boldsymbol{a}_1,\dots,\boldsymbol{a}_p]^{\mathsf T}$（$p\times p$），$B=[\boldsymbol{b}_1,\dots,\boldsymbol{b}_p]^{\mathsf T}$（$p\times q$），于是 $\boldsymbol{U}=A\boldsymbol{X}^{(1)}$、$\boldsymbol{V}=B\boldsymbol{X}^{(2)}$ 汇集了全部典型变量；令 $D_{11}=\operatorname{diag}(\Sigma_{11})$、$D_{22}=\operatorname{diag}(\Sigma_{22})$ 为方差构成的对角矩阵。由于 $\operatorname{Cov}(\boldsymbol{U},\boldsymbol{X}^{(1)})=\operatorname{Cov}(A\boldsymbol{X}^{(1)},\boldsymbol{X}^{(1)})=A\Sigma_{11}$，且典型变量方差为 1，

$$
\begin{aligned}
\operatorname{Corr}(\boldsymbol{U},\boldsymbol{X}^{(1)})&=\operatorname{Cov}(\boldsymbol{U},D_{11}^{-1/2}\boldsymbol{X}^{(1)})=A\Sigma_{11}D_{11}^{-1/2},&\operatorname{Corr}(\boldsymbol{U},\boldsymbol{X}^{(2)})&=A\Sigma_{12}D_{22}^{-1/2},\\
\operatorname{Corr}(\boldsymbol{V},\boldsymbol{X}^{(2)})&=B\Sigma_{22}D_{22}^{-1/2},&\operatorname{Corr}(\boldsymbol{V},\boldsymbol{X}^{(1)})&=B\Sigma_{21}D_{11}^{-1/2}.
\end{aligned}
$$

**例 9.2.2（Hotelling 数据，续）** 对 $V_1=-0.09X_1^{(2)}+0.03X_2^{(2)}$，相关系数为 $\operatorname{Corr}(V_1,X_1^{(2)})=-0.923$，$\operatorname{Corr}(V_1,X_2^{(2)})=-0.017$。算术能力的系数为正，并不意味着 $V_1$ 与它正相关：在给定算术速度时，算术能力以很小的正权重进入，但它单独与 $V_1$ 不相关，$V_1$ 本质上就是（负的）算术速度。类似地，$\operatorname{Corr}(U_1,X_1^{(1)})=-0.65$，$\operatorname{Corr}(U_1,X_2^{(1)})=0.22$。因此第一对典型变量主要把阅读速度与算术速度联系起来。

![Hotelling 的例子：四个变量按其与阅读组典型变量 U_1、U_2 的相关系数画出；算术速度与 U_1 相关，算术能力与两者都不相关](./plots/hotelling-correlation-plot.py)

### 9.2.4. 性质

对 $k,l=1,\dots,p$，典型变量满足

$$
\operatorname{Var}(U_k)=\operatorname{Var}(V_k)=1,\qquad\operatorname{Cov}(U_k,U_l)=\operatorname{Cov}(V_k,V_l)=\operatorname{Cov}(U_k,V_l)=0\quad(k\ne l),
$$
写成矩阵形式为

$$
\operatorname{Cov}(\boldsymbol{U})=A\Sigma_{11}A^{\mathsf T}=I_p,\qquad\operatorname{Cov}(\boldsymbol{V})=B\Sigma_{22}B^{\mathsf T}=I_p,\qquad\operatorname{Cov}(\boldsymbol{U},\boldsymbol{V})=A\Sigma_{12}B^{\mathsf T}=\operatorname{diag}(\rho_1^*,\dots,\rho_p^*),
$$
即 $\operatorname{Cov}\begin{bmatrix}\boldsymbol{U}\\\boldsymbol{V}\end{bmatrix}=\begin{bmatrix}I_p&\Lambda_\rho\\\Lambda_\rho&I_p\end{bmatrix}$，$\Lambda_\rho=\operatorname{diag}(\rho_1^*,\dots,\rho_p^*)$。含 $pq$ 个元素的交叉协方差 $\Sigma_{12}$ 被约简为 $p$ 个数。与 PCA 不同，系数向量 $\boldsymbol{a}_i$ 彼此并不正交；它们在 $\Sigma_{11}$ 所定义的内积下正交。

第一个典型相关系数推广了通常的相关系数：

- $p$ 个与 $q$ 个变量：$\rho_1^*=\max_{\boldsymbol{a},\boldsymbol{b}}\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)},\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})$；
- $1$ 个与 $1$ 个变量：$\lvert\operatorname{Corr}(X_i^{(1)},X_k^{(2)})\rvert$ 是两个特定线性组合的相关系数，所以至多为 $\rho_1^*$；
- $1$ 个与 $q$ 个变量：复相关系数（multiple correlation coefficient）$\max_{\boldsymbol{b}}\operatorname{Corr}(X_1^{(1)},\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})$，即 $X_1^{(1)}$ 与它由 $\boldsymbol{X}^{(2)}$ 得到的**最佳线性预测**之间的相关系数，至多为 $\rho_1^*$，当 $p=1$ 时两者相等。

由同样的想法可以得到一种 $R^2$ 型的解释。对第 $k$ 对，

$$
\max_{\boldsymbol{b}}\operatorname{Corr}(U_k,\boldsymbol{b}^{\mathsf T}\boldsymbol{X}^{(2)})=\operatorname{Corr}(U_k,V_k)=\rho_k^*,\qquad\max_{\boldsymbol{a}}\operatorname{Corr}(\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)},V_k)=\rho_k^*,
$$
（第一式是因为 $\max_{\boldsymbol{b}}$ 等于 $\sqrt{\boldsymbol{a}_k^{\mathsf T}\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\boldsymbol{a}_k}=\sqrt{\boldsymbol{e}_k^{\mathsf T}YY^{\mathsf T}\boldsymbol{e}_k}=\rho_k^*$）。因此 $\rho_k^{*2}$ 是 $U_k$ 的方差中由 $\boldsymbol{X}^{(2)}$ 解释的比例，也是 $V_k$ 的方差中由 $\boldsymbol{X}^{(1)}$ 解释的比例：两组变量沿第 $k$ 对共享的方差。

从几何上看，在内积为 $\langle X,W\rangle=\mathbb{E}(XW)$（长度为标准差，夹角余弦为相关系数）的中心化随机变量空间中，每组变量张成一个子空间，维数分别为 $p$ 与 $q$。第一对典型变量是分别位于两个子空间中、夹角 $\theta_1$ 最小的一对单位向量，$\rho_1^*=\cos\theta_1$；后续各对给出两个子空间之间其余的主角。$p=1$、$q=2$ 时，$V_1$ 是 $X^{(1)}$ 在 $\boldsymbol{X}^{(2)}$ 所张平面上投影的方向，这就是回归。$p=q=2$ 时，若两个平面交于一条直线，则 $U_1=V_1$ 位于这条直线上，$\rho_1^*=1$；若其余方向又相互正交，则 $\rho_2^*=0$。

### 9.2.5. 标准化变量

如果某个变量的测量尺度与其他变量相差悬殊，会怎样？下面将证明典型相关系数不变，系数则会改变。可以对标准化变量

$$
Z_k^{(j)}=\frac{X_k^{(j)}-\mu_k^{(j)}}{\sqrt{\sigma_{kk}^{(j)}}},\qquad\text{即}\qquad\boldsymbol{Z}^{(j)}=D_{jj}^{-1/2}(\boldsymbol{X}^{(j)}-\boldsymbol{\mu}^{(j)}),\quad j=1,2
$$
求典型变量，其协方差矩阵就是相关矩阵

$$
\begin{bmatrix}\rho_{11}&\rho_{12}\\\rho_{21}&\rho_{22}\end{bmatrix}=\rho=D^{-1/2}\Sigma D^{-1/2}=\begin{bmatrix}D_{11}^{-1/2}&O\\O&D_{22}^{-1/2}\end{bmatrix}\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}\begin{bmatrix}D_{11}^{-1/2}&O\\O&D_{22}^{-1/2}\end{bmatrix}.
$$
对 $\rho$ 应用定理 9.2.1，得到典型变量 $U_k=\boldsymbol{e}_k^{\mathsf T}\rho_{11}^{-1/2}\boldsymbol{Z}^{(1)}$、$V_k=\boldsymbol{f}_k^{\mathsf T}\rho_{22}^{-1/2}\boldsymbol{Z}^{(2)}$，其中 $\rho_1^{*2}\ge\cdots\ge\rho_p^{*2}$ 现在是 $\rho_{11}^{-1/2}\rho_{12}\rho_{22}^{-1}\rho_{21}\rho_{11}^{-1/2}$ 的特征值，$\boldsymbol{e}_k$ 为特征向量，$\boldsymbol{f}_k=\frac{1}{\rho_k^*}\rho_{22}^{-1/2}\rho_{21}\rho_{11}^{-1/2}\boldsymbol{e}_k$（这里的 $\boldsymbol{e}_k$、$\boldsymbol{f}_k$ 与对 $\Sigma$ 求得的不同）。

**命题 9.2.1** 设 $\boldsymbol{Z}^{(i)}=C_i\boldsymbol{X}^{(i)}+\boldsymbol{c}_i$，$C_1\in\mathbb{R}^{p\times p}$、$C_2\in\mathbb{R}^{q\times q}$ 可逆。则 $\boldsymbol{Z}^{(1)},\boldsymbol{Z}^{(2)}$ 与 $\boldsymbol{X}^{(1)},\boldsymbol{X}^{(2)}$ 有相同的典型相关系数，典型变量也在相差常数的意义下相同；典型系数按 $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$、$\boldsymbol{b}=C_2^{\mathsf T}\boldsymbol{b}_z$ 变换。特别地，对标准化，$\boldsymbol{a}_z=D_{11}^{1/2}\boldsymbol{a}$，$\boldsymbol{b}_z=D_{22}^{1/2}\boldsymbol{b}$：标准化系数等于原始系数乘以标准差。

**证明** $\boldsymbol{Z}$ 的协方差块为 $\tilde\Sigma_{ij}=C_i\Sigma_{ij}C_j^{\mathsf T}$，所以对 $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$、$\boldsymbol{b}=C_2^{\mathsf T}\boldsymbol{b}_z$，

$$
\frac{\boldsymbol{a}_z^{\mathsf T}\tilde\Sigma_{12}\boldsymbol{b}_z}{\sqrt{\boldsymbol{a}_z^{\mathsf T}\tilde\Sigma_{11}\boldsymbol{a}_z}\sqrt{\boldsymbol{b}_z^{\mathsf T}\tilde\Sigma_{22}\boldsymbol{b}_z}}=\frac{(C_1^{\mathsf T}\boldsymbol{a}_z)^{\mathsf T}\Sigma_{12}(C_2^{\mathsf T}\boldsymbol{b}_z)}{\sqrt{(C_1^{\mathsf T}\boldsymbol{a}_z)^{\mathsf T}\Sigma_{11}(C_1^{\mathsf T}\boldsymbol{a}_z)}\sqrt{(C_2^{\mathsf T}\boldsymbol{b}_z)^{\mathsf T}\Sigma_{22}(C_2^{\mathsf T}\boldsymbol{b}_z)}}=\frac{\boldsymbol{a}^{\mathsf T}\Sigma_{12}\boldsymbol{b}}{\sqrt{\boldsymbol{a}^{\mathsf T}\Sigma_{11}\boldsymbol{a}}\sqrt{\boldsymbol{b}^{\mathsf T}\Sigma_{22}\boldsymbol{b}}}.
$$
由于 $\boldsymbol{a}_z\mapsto C_1^{\mathsf T}\boldsymbol{a}_z$ 是双射，两个问题（包括不相关约束）的最优值相同，最优典型变量 $\boldsymbol{a}_z^{\mathsf T}\boldsymbol{Z}^{(1)}=\boldsymbol{a}^{\mathsf T}\boldsymbol{X}^{(1)}+\boldsymbol{a}_z^{\mathsf T}\boldsymbol{c}_1$ 在相差常数的意义下一致。$\square$

**例 9.2.3（Hotelling 数据，续）** 相关矩阵 $\rho$ 给出与 $\Sigma$ 相同的 $\rho_1^{*2}=0.146$、$\rho_2^{*2}=0.005$。标准化系数为 $U_1=-1.22Z_1^{(1)}+0.95Z_2^{(1)}$，$V_1=-1.09Z_1^{(2)}+0.42Z_2^{(2)}$，即原始系数乘以标准差 $10,10$ 与 $12,12$。

## 9.3. 样本典型相关

### 9.3.1. 样本典型变量

设 $\boldsymbol{x}_1,\dots,\boldsymbol{x}_n$ 是来自均值为 $\boldsymbol{\mu}$、协方差矩阵为 $\Sigma$ 的 $(p+q)$ 维总体的 $n$ 个独立观测。每个观测分为 $\boldsymbol{x}_j=(\boldsymbol{x}_j^{(1)},\boldsymbol{x}_j^{(2)})$，于是 $n\times(p+q)$ 数据矩阵由第一组变量的 $n\times p$ 块与第二组变量的 $n\times q$ 块组成，**样本协方差矩阵**与**样本相关矩阵**为

$$
S=\begin{bmatrix}S_{11}&S_{12}\\S_{21}&S_{22}\end{bmatrix},\qquad R=\begin{bmatrix}R_{11}&R_{12}\\R_{21}&R_{22}\end{bmatrix}.
$$
样本版本用经验分布代替总体分布，用 $S$ 代替 $\Sigma$、$R$ 代替 $\rho$，按同样的步骤进行。

**定理 9.3.1** 设 $\hat\rho_1^{*2}\ge\cdots\ge\hat\rho_p^{*2}$ 是 $S_{11}^{-1/2}S_{12}S_{22}^{-1}S_{21}S_{11}^{-1/2}$ 的特征值，$\hat{\boldsymbol{e}}_1,\dots,\hat{\boldsymbol{e}}_p$ 为标准正交特征向量；它们也是 $S_{22}^{-1/2}S_{21}S_{11}^{-1}S_{12}S_{22}^{-1/2}$ 的前 $p$ 个最大特征值，特征向量为 $\hat{\boldsymbol{f}}_k=\frac{1}{\hat\rho_k^*}S_{22}^{-1/2}S_{21}S_{11}^{-1/2}\hat{\boldsymbol{e}}_k$。第 $k$ 对样本典型变量

$$
\hat U_k=\hat{\boldsymbol{e}}_k^{\mathsf T}S_{11}^{-1/2}\boldsymbol{x}^{(1)},\qquad\hat V_k=\hat{\boldsymbol{f}}_k^{\mathsf T}S_{22}^{-1/2}\boldsymbol{x}^{(2)}
$$
达到第 $k$ 个样本典型相关系数 $\widehat{\operatorname{Corr}}(\hat U_k,\hat V_k)=\hat\rho_k^*$，$k=1,\dots,p$，并且样本典型变量满足

$$
\widehat{\operatorname{Var}}(\hat U_k)=\widehat{\operatorname{Var}}(\hat V_k)=1,\qquad\widehat{\operatorname{Cov}}(\hat U_k,\hat U_l)=\widehat{\operatorname{Cov}}(\hat V_k,\hat V_l)=\widehat{\operatorname{Cov}}(\hat U_k,\hat V_l)=0\quad(k\ne l).
$$

这里 $\widehat{\operatorname{Var}}$ 与 $\widehat{\operatorname{Cov}}$ 是在 $n$ 个个体上计算的样本方差与样本协方差，而不是总体矩。写成矩阵形式，由 $\hat{\boldsymbol{a}}_k=S_{11}^{-1/2}\hat{\boldsymbol{e}}_k$、$\hat{\boldsymbol{b}}_k=S_{22}^{-1/2}\hat{\boldsymbol{f}}_k$ 构成 $\hat A$ 与 $\hat B$，则 $\hat{\boldsymbol{U}}=\hat A\boldsymbol{x}^{(1)}$，$\hat{\boldsymbol{V}}=\hat B\boldsymbol{x}^{(2)}$，且 $\hat AS_{11}\hat A^{\mathsf T}=I_p$，$\hat BS_{22}\hat B^{\mathsf T}=I_p$，$\hat AS_{12}\hat B^{\mathsf T}=\operatorname{diag}(\hat\rho_1^*,\dots,\hat\rho_p^*)$；用矩阵形式推导这些结果最为简便。

各个体的取值 $\hat U_k(\boldsymbol{x}_j)$、$\hat V_k(\boldsymbol{x}_j)$ 称为典型变量得分。与因子分析（[3.4.8](/3.4.8)）一样，有两类有用的图：在总体水平，按变量与两个典型变量的相关系数画出各变量；在个体水平，按得分画出各个体。

![两组模拟变量（p = 2，q = 3）：样本典型变量得分 (U_1, V_1) 与 (U_2, V_2) 的散点图，样本典型相关系数约为 0.83 与 0.31](./plots/canonical-variates-scatter.py)

### 9.3.2. 例子

**例 9.3.1（销售人员数据）** 对 $n=50$ 名销售人员记录了三项销售业绩指标 $\boldsymbol{x}^{(1)}$ =（销售增长、销售利润率、新客户销售额）与四项测验成绩 $\boldsymbol{x}^{(2)}$ =（创造力、机械推理、抽象推理、数学）。相关矩阵的热图显示，业绩块内部以及业绩与数学测验之间都有很强的正相关。样本典型相关系数为

$$
\hat\rho_1^*=0.994,\qquad\hat\rho_2^*=0.878,\qquad\hat\rho_3^*=0.384.
$$
$\hat U_1$ 的系数（由 R 函数 `cc` 计算）对增长、利润率与新客户销售额分别为 $-0.458$、$-0.212$、$-0.369$，$\hat U_1$ 与这些变量的相关系数为 $-0.980$、$-0.946$、$-0.952$：$\hat U_1$ 是（负的）综合销售业绩指数。（函数 `cancor` 给出的系数相差因子 $-1/\sqrt{n-1}$，因为它把典型变量规范化为平方和为 1 而不是样本方差为 1，并取相反的符号；典型相关系数相同。）第一名销售人员的得分为 $(\hat U_1,\hat U_2,\hat U_3)=(0.978,-0.363,0.819)$。

为了把关联可视化，可以把两组变量都投影到第一组两个典型变量所在的平面上。变量的坐标是它与这两个典型变量的相关系数：按 9.2.4 节的几何，$X_i$ 在 $U_1$ 方向上投影的长度为 $\sqrt{\operatorname{Var}(X_i)}\cos\theta=\sqrt{\operatorname{Var}(X_i)}\operatorname{Corr}(X_i,U_1)$，对标准化变量就是相关系数本身。既然是投影，就会损失一些信息；靠近单位圆的变量表示得较好。在 $(\hat U_1,\hat U_3)$ 平面上，七个变量都位于 $\hat U_1$ 轴的负侧，业绩变量接近 $-1$；第三个典型变量把销售增长与抽象推理（正）同新客户销售额与创造力（负）区分开来。得分 $(\hat U_1,\hat U_3)$ 的个体水平图显示了各个销售人员，例如有一人的 $\hat U_3$ 异常大。两幅图之间没有逐点的对应关系：前者展示变量之间的关系，后者展示个体的特点。这里选择 $(\hat U_1,\hat U_3)$ 只是为了示例；通常使用 $(\hat U_1,\hat U_2)$ 或 $(\hat V_1,\hat V_2)$，即两组之间关联最强的坐标系。

**例 9.3.2（图像与文本）** 从 COCO 图像数据集中随机抽取 $100$ 张带说明文字的图像。每张图像转换为 $21$ 个视觉特征 $\boldsymbol{x}^{(1)}$，每段说明转换为 $20$ 个文本特征 $\boldsymbol{x}^{(2)}$，即 $20$ 个最高频词的 TF–IDF 权重（词频乘以 $\log(N/n_t)$，$N$ 篇文档中有 $n_t$ 篇含该词）。$\hat U_1$ 大对应于水平边缘丰富、明暗对比强的图像，常见于室内场景；$\hat V_1$ 大对应于描述室内、近景、聚焦场景的说明，$\hat V_1$ 小则对应于室外、开阔场景。$(\hat U_1,\hat V_1)$ 的散点图把室内图像与室外图像分开：CCA 在两种模态中找到了一个共同的"室内对室外"维度。这样的共享表示是跨模态检索（为文本查询寻找图像，或反之）的基础。

### 9.3.3. 近似误差矩阵

前 $r$ 对典型变量能再现多少样本协方差结构？用与前 $p$ 行 $S_{22}$-标准正交的另外 $q-p$ 行把 $\hat B$ 扩充为可逆的 $q\times q$ 矩阵，使 $\hat{\boldsymbol{U}}=\hat A\boldsymbol{x}^{(1)}$ 与 $\hat{\boldsymbol{V}}=\hat B\boldsymbol{x}^{(2)}$ 可以反解：$\boldsymbol{x}^{(1)}=\hat A^{-1}\hat{\boldsymbol{U}}$，$\boldsymbol{x}^{(2)}=\hat B^{-1}\hat{\boldsymbol{V}}$（中心化之后）。按列记 $\hat A^{-1}=[\hat{\boldsymbol{a}}^{(1)},\dots,\hat{\boldsymbol{a}}^{(p)}]$，$\hat B^{-1}=[\hat{\boldsymbol{b}}^{(1)},\dots,\hat{\boldsymbol{b}}^{(q)}]$。由于样本典型变量互不相关、方差为 1，且 $\widehat{\operatorname{Cov}}(\hat U_k,\hat V_k)=\hat\rho_k^*$，

$$
S_{11}=\sum_{k=1}^p\hat{\boldsymbol{a}}^{(k)}\hat{\boldsymbol{a}}^{(k)\mathsf T},\qquad S_{22}=\sum_{k=1}^q\hat{\boldsymbol{b}}^{(k)}\hat{\boldsymbol{b}}^{(k)\mathsf T},\qquad S_{12}=\sum_{k=1}^p\hat\rho_k^*\,\hat{\boldsymbol{a}}^{(k)}\hat{\boldsymbol{b}}^{(k)\mathsf T}.
$$
若只用前 $r$ 对，$\tilde{\boldsymbol{x}}^{(1)}=[\hat{\boldsymbol{a}}^{(1)},\dots,\hat{\boldsymbol{a}}^{(r)},\boldsymbol{0},\dots,\boldsymbol{0}]\hat{\boldsymbol{U}}$，$\tilde{\boldsymbol{x}}^{(2)}=[\hat{\boldsymbol{b}}^{(1)},\dots,\hat{\boldsymbol{b}}^{(r)},\boldsymbol{0},\dots,\boldsymbol{0}]\hat{\boldsymbol{V}}$，近似误差矩阵为

$$
\begin{aligned}
S_{11}-\big(\hat{\boldsymbol{a}}^{(1)}\hat{\boldsymbol{a}}^{(1)\mathsf T}+\cdots+\hat{\boldsymbol{a}}^{(r)}\hat{\boldsymbol{a}}^{(r)\mathsf T}\big)&=\hat{\boldsymbol{a}}^{(r+1)}\hat{\boldsymbol{a}}^{(r+1)\mathsf T}+\cdots+\hat{\boldsymbol{a}}^{(p)}\hat{\boldsymbol{a}}^{(p)\mathsf T},\\
S_{22}-\big(\hat{\boldsymbol{b}}^{(1)}\hat{\boldsymbol{b}}^{(1)\mathsf T}+\cdots+\hat{\boldsymbol{b}}^{(r)}\hat{\boldsymbol{b}}^{(r)\mathsf T}\big)&=\hat{\boldsymbol{b}}^{(r+1)}\hat{\boldsymbol{b}}^{(r+1)\mathsf T}+\cdots+\hat{\boldsymbol{b}}^{(q)}\hat{\boldsymbol{b}}^{(q)\mathsf T},\\
S_{12}-\big(\hat\rho_1^*\hat{\boldsymbol{a}}^{(1)}\hat{\boldsymbol{b}}^{(1)\mathsf T}+\cdots+\hat\rho_r^*\hat{\boldsymbol{a}}^{(r)}\hat{\boldsymbol{b}}^{(r)\mathsf T}\big)&=\hat\rho_{r+1}^*\hat{\boldsymbol{a}}^{(r+1)}\hat{\boldsymbol{b}}^{(r+1)\mathsf T}+\cdots+\hat\rho_p^*\hat{\boldsymbol{a}}^{(p)}\hat{\boldsymbol{b}}^{(p)\mathsf T}.
\end{aligned}
$$
它们是前 $r$ 个典型变量再现样本协方差矩阵好坏的描述性概括。通常 $S_{12}$ 再现得最好，因为其误差项以较小的剩余典型相关系数为权重；$S_{11}$ 与 $S_{22}$ 可能再现得很差，因为典型系数向量是为最大化相关而选的，并不是为了解释各组内部的变异。

一个单一数值的概括是前 $r$ 个典型变量所解释的第一组样本总方差的比例

$$
\frac{\sum_{k=1}^r\hat{\boldsymbol{a}}^{(k)\mathsf T}\hat{\boldsymbol{a}}^{(k)}}{\operatorname{tr}(S_{11})},
$$
第二组类似。对标准化变量，$\hat{\boldsymbol{a}}^{(k)}$ 是 $\hat U_k$ 与第一组各变量的相关系数构成的向量，分母为 $p$。这个比例表明典型变量对其所在组的代表程度。

## 9.4. 大样本推断

若 $\Sigma_{12}=O$，所有典型相关系数都为零，CCA 就没有意义，所以应当先检验这一假设。设

$$
\begin{bmatrix}\boldsymbol{X}^{(1)}\\\boldsymbol{X}^{(2)}\end{bmatrix}\sim\mathcal{N}_{p+q}\left(\begin{bmatrix}\boldsymbol{\mu}^{(1)}\\\boldsymbol{\mu}^{(2)}\end{bmatrix},\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}\right),\qquad\rho_1^*\ge\rho_2^*\ge\cdots\ge\rho_p^*.
$$

**定理 9.4.1** 对检验 $H_0\colon\rho_1^*=\cdots=\rho_p^*=0$（等价于 $\Sigma_{12}=O$）对 $H_1$：某个 $\rho_i^*\ne0$，**似然比检验**的统计量为

$$
-2\log\Lambda=n\log\frac{\lvert S_{11}\rvert\lvert S_{22}\rvert}{\lvert S\rvert}=-n\log\prod_{i=1}^p\big(1-\hat\rho_i^{*2}\big),
$$
$n$ 很大时它在 $H_0$ 下近似服从 $\chi^2_{pq}$；自由度 $pq$ 等于 $\Sigma_{12}$ 的元素个数。

关键的一步是一个行列式恒等式，这里用总体记号叙述（样本版本完全相同）。由 **Schur 补**公式，

$$
\lvert\Sigma\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}\rvert\,\lvert I_q-\Sigma_{22}^{-1/2}\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\Sigma_{22}^{-1/2}\rvert=\lvert\Sigma_{11}\rvert\,\lvert\Sigma_{22}\rvert\,\lvert I_q-Y^{\mathsf T}Y\rvert.
$$
由 $Y=P_1\Lambda P_2^{\mathsf T}$，$\lvert I_q-Y^{\mathsf T}Y\rvert=\lvert P_2(I_q-\Lambda^{\mathsf T}\Lambda)P_2^{\mathsf T}\rvert=\lvert I_q-\Lambda^{\mathsf T}\Lambda\rvert=\prod_{i=1}^p(1-\rho_i^{*2})$。在 $H_0$ 下 $\Sigma$ 的极大似然估计是分块对角的，由此得到行列式之比。

若拒绝 $H_0$，接着要问有几个典型相关系数非零。对 $H_0^{(k)}\colon\rho_1^*\ne0,\dots,\rho_k^*\ne0,\ \rho_{k+1}^*=\cdots=\rho_p^*=0$ 对 $H_1^{(k)}$：某个 $i\ge k+1$ 使 $\rho_i^*\ne0$，似然比统计量为

$$
-2\log\Lambda=-n\log\prod_{i=k+1}^p\big(1-\hat\rho_i^{*2}\big)\ \overset{\cdot}{\sim}\ \chi^2_{(p-k)(q-k)}.
$$
对 $k=0,1,2,\dots$ 依次检验，直到 $H_0^{(k)}$ 不被拒绝为止。Bartlett 修正把 $n$ 换成 $n-1-\frac12(p+q+1)$，改善近似；软件常常转而报告 Wilks 统计量 $\prod_{i>k}(1-\hat\rho_i^{*2})$ 及其 $F$ 近似（Rao 的 $F$）。

**例 9.4.1（销售人员数据，续）** $n=50$，$p=3$，$q=4$，对 $k=0,1,2$，乘积 $\prod_{i>k}(1-\hat\rho_i^{*2})$ 分别为 $0.0021$、$0.195$ 与 $0.853$。经 Bartlett 修正，统计量为 $276.4$（自由度 $12$）、$73.5$（$6$）与 $7.16$（$2$），$p$ 值分别为 $<10^{-15}$、$8\times10^{-14}$ 与 $0.028$；Rao 的 $F$ 近似给出相同的结论。在 $0.05$ 水平下，连第三个典型相关系数 $0.384$ 也是显著的。

## 9.5. 推广

- 概率 CCA（F. Bach 与 M. Jordan，2005）是一个因子分析风格的潜变量模型：$\boldsymbol{X}=W_1\boldsymbol{Z}+\boldsymbol{\mu}_1+\boldsymbol{\varepsilon}_1$，$\boldsymbol{Y}=W_2\boldsymbol{Z}+\boldsymbol{\mu}_2+\boldsymbol{\varepsilon}_2$，共享的 $\boldsymbol{Z}\sim\mathcal{N}(\boldsymbol{0},I_k)$，$\boldsymbol{\varepsilon}_i\sim\mathcal{N}(\boldsymbol{0},\Psi_i)$；其极大似然估计恢复出典型方向，并可推广为条件生成模型。
- 核 CCA（S. Akaho，2006）像 [3.4.6](/3.4.6) 中的核 PCA 那样，把两组变量映射到再生核 Hilbert 空间，以刻画非线性关联。
- 稀疏 CCA（D. Witten、R. Tibshirani 与 T. Hastie，2009）通过惩罚矩阵分解对系数向量加 $\ell_1$ 惩罚，使每个典型变量只涉及少数变量；当 $p$、$q$ 超过 $n$ 时这是必不可少的。
- 深度 CCA（G. Andrew、R. Arora、J. Bilmes 与 K. Livescu，2013）在两个神经网络 $f$ 与 $g$ 上最大化 $\operatorname{Corr}\big(f(\boldsymbol{X};\theta_f),g(\boldsymbol{Y};\theta_g)\big)$。

## 小结

- 动机：用少数几对线性组合描述两组变量之间的关联 $\Sigma_{12}$，把 $pq$ 个交叉协方差约简为 $p$ 个典型相关系数（$p\le q$）。
- 求解：关键矩阵是 $Y=\Sigma_{11}^{-1/2}\Sigma_{12}\Sigma_{22}^{-1/2}$，关键工具是它的奇异值分解（或 Rayleigh 商的最大化），关键思想是逐次最大化：$\rho_k^*$ 是 $Y$ 的第 $k$ 个奇异值，$\boldsymbol{a}_k=\Sigma_{11}^{-1/2}\boldsymbol{e}_k$，$\boldsymbol{b}_k=\Sigma_{22}^{-1/2}\boldsymbol{f}_k$，且 $\operatorname{Cov}(\boldsymbol{U},\boldsymbol{V})=\operatorname{diag}(\rho_k^*)$，$\operatorname{Cov}(\boldsymbol{U})=\operatorname{Cov}(\boldsymbol{V})=I_p$。
- 解释：典型系数（多元的，给定同组其他变量）与典型变量和变量之间的相关系数（单变量的）；$\rho_k^{*2}$ 是共享方差；从几何上看，各 $\rho_k^*$ 是两个张成空间之间主角的余弦；$\rho_1^*$ 推广了简单相关与复相关。
- 不变性：典型相关系数与典型变量在对各组做可逆线性变换（特别是标准化）时不变；系数按 $\boldsymbol{a}=C_1^{\mathsf T}\boldsymbol{a}_z$ 变换。
- 应用：样本 CCA 用 $S$ 代替 $\Sigma$（或用 $R$ 代替 $\rho$）；按变量与典型变量的相关系数作变量图（总体水平），按得分作个体图（个体水平）；似然比检验 $-n\log\prod_{i>k}(1-\hat\rho_i^{*2})\overset{\cdot}{\sim}\chi^2_{(p-k)(q-k)}$ 决定是否需要 CCA 以及保留几对。
