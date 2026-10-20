---
title: Markov 链 Monte Carlo
description: 蒙特卡洛积分（投点法与均值法）、重要性抽样及其方差、稀有事件与自归一化权重；Markov 链、平稳分布、细致平衡与基本极限定理；Metropolis–Hastings 算法、Gibbs 抽样与收敛诊断。
source_hash: bb824d9fd159
---

Markov 链 Monte Carlo（Markov chain Monte Carlo），简称 MCMC，用模拟来估计复杂模型中某个统计量的期望。相继的随机抽取构成一条 Markov 链，其平稳分布就是目标分布。它特别适用于计算复杂贝叶斯模型中的后验分布。在 Metropolis–Hastings 算法中，候选点从任意的提议分布中抽取，再按接受规则决定保留与否；Gibbs 抽样是它的特例，提议分布是向量中单个分量的条件分布。本章是课程的最后一章，把两条线索汇合在一起。第一部分接续 [3.1.12](/3.1.12) 的**蒙特卡洛方法**与 [3.5.8](/3.5.8) 的抽样方法：蒙特卡洛积分的两种方法与重要性抽样——它是拒绝抽样的镜像，在高维中以另一种方式失效。第二部分介绍 Markov 链、平稳分布与基本极限定理，并把两者结合成 MCMC。贝叶斯背景（**先验分布**、**后验分布**、**可信区间**）见 [3.2.7](/3.2.7)；贝叶斯统计（[3.7](/3.7)）通篇依赖这些抽样方法。

MCMC 用于高维空间中的积分与优化问题，涉及三类问题：积分、从概率分布中生成样本、优化。典型的例子有：

- 贝叶斯推断与学习：归一化 $p(x\mid y)=\dfrac{p(y\mid x)p(x)}{\int_{\mathcal{X}}p(y\mid t)p(t)\,\mathrm{d}t}$，边缘化 $p(x\mid y)=\int_{\mathcal{Z}}p(x,z\mid y)\,\mathrm{d}z$，以及期望 $\mathbb{E}_{X\mid Y}[f(X)]=\int_{\mathcal{X}}f(x)p(x\mid y)\,\mathrm{d}x$；
- 统计力学：状态为 $s$、Hamilton 量（能量）为 $H(s)$、Boltzmann 常数为 $k$、温度为 $T$ 的系统的配分函数 $Z=\sum_s\exp(-H(s)/(kT))$，对数量巨大的构型求和代价高得无法承受；
- 罚似然模型选择，以及核物理和计算机图形学中物理系统的模拟。

MCMC 不是一种具体的技术，而是一大类抽样算法，包括 Metropolis 算法、Gibbs 抽样、切片抽样等。

## 9.1. 蒙特卡洛积分

### 9.1.1. 用模拟作数值积分

考虑 $\int_0^\pi\sin x\,\mathrm{d}x=2$。Riemann 和、蒙特卡洛投点法与 R 的自适应求积分别给出：

```r
n <- 100; h <- pi/n
x <- seq(from = 0, to = pi, length = n)
rect <- sin(x) * h
sum(rect)                                  # 1.979834

# Monte Carlo method: the hit-or-miss method
n <- 1e+5
xran <- runif(n, min = 0, max = pi)
yran <- runif(n, min = 0, max = 1)
sum(yran <= sin(xran))/n * pi              # 1.997

integrate(sin, lower = 0, upper = pi)      # 2 with absolute error < 2.2e-14
```

尽管在计算机出现之前已有少数随机模拟的应用，它的广泛使用不得不等待计算机的发明。Stanislaw Ulam 于 1946 年玩单人纸牌时想到了这个方法；名称取自蒙特卡洛赌场，起初是个玩笑（当时多数地方禁止赌博），很快就成了随机过程模拟的技术术语。

### 9.1.2. 均值法

设 $X\sim p(x)$，$\mathbb{E}f=I(f)=\int_{\mathcal{X}}f(x)p(x)\,\mathrm{d}x$。由强**大数定律**，

$$
\hat I_n(f)=\frac1n\sum_{i=1}^nf(X_i)\xrightarrow{\text{a.s.}}I(f),\qquad n\to\infty.
$$
若 $f(X_i)$ 独立同分布且 $0<\operatorname{Var}(f(X))<\infty$，由**中心极限定理**，

$$
\frac{\hat I_n(f)-\mathbb{E}f}{\sqrt{\operatorname{Var}(f)/n}}\xrightarrow{d}\mathcal{N}(0,1).
$$
$\operatorname{Var}(f)$ 的无偏估计是 $s^2=\frac1{n-1}\sum_{i=1}^n\bigl(f(X_i)-\hat I_n(f)\bigr)^2$，所以 $\mathbb{E}f$ 的近似 $100(1-\alpha)\%$ 置信区间为 $\hat I_n(f)\pm z_{\alpha/2}s/\sqrt n$。误差的量级是 $n^{-1/2}$，与维数无关。

**例 9.1.1** 设 $X\sim\mathcal{N}(0,1)$，$a=\mathbb{P}(\sin(\pi X)>0.5)$。则 $a=\mathbb{E}\bigl[\boldsymbol{1}\{\sin(\pi X)>0.5\}\bigr]=\mathbb{E}f$，于是抽取 $X_i\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，构造 $\hat a=\frac1n\sum_{i=1}^n\boldsymbol{1}\{\sin(\pi X_i)>0.5\}$。各项独立同分布于 $\mathrm{Ber}(a)$，所以 $\hat a$ 满足方差为 $a(1-a)/n$ 的中心极限定理。

### 9.1.3. 投点法与均值法：方差比较

设对 $a\le x\le b$ 有 $0\le f(x)\le M$，要计算 $\theta=\int_a^bf(x)\,\mathrm{d}x$。

**定义 9.1.1（两种蒙特卡洛方法）** **投点法**在盒子 $[a,b]\times[0,M]$ 中均匀地投 $n$ 个点，记落在 $f$ 的图像下方的比例为 $\hat p$，估计为

$$
\hat\theta_H=M(b-a)\hat p.
$$
在**均值法**（朴素蒙特卡洛）中，把 $\theta$ 写成 $\theta=(b-a)\int_a^bf(x)\frac{1}{b-a}\,\mathrm{d}x=(b-a)\mathbb{E}[f(X)]$，$X\sim\mathrm{U}(a,b)$，并估计

$$
\hat\theta_M=(b-a)\hat I_n(f)=\frac{b-a}{n}\sum_{i=1}^nf(X_i),\qquad X_i\overset{\text{iid}}{\sim}\mathrm{U}(a,b).
$$

**定理 9.1.1** 在均匀点数 $n$ 相同时，$\operatorname{Var}(\hat\theta_M)\le\operatorname{Var}(\hat\theta_H)$。

**证明** $\hat p=\frac1n\sum_iY_i$，$Y_i\sim\mathrm{Ber}\bigl(\theta/(M(b-a))\bigr)$，所以

$$
\operatorname{Var}(\hat\theta_H)=\frac{\theta\bigl(M(b-a)-\theta\bigr)}{n},\qquad\operatorname{Var}(\hat\theta_M)=\frac{(b-a)^2}{n}\operatorname{Var}(f(X)).
$$
由于 $\mathbb{E}f=\theta/(b-a)$，

$$
\operatorname{Var}(\hat\theta_M)\le\operatorname{Var}(\hat\theta_H)\iff\mathbb{E}[f^2]-(\mathbb{E}f)^2\le M\frac{\theta}{b-a}-\Bigl(\frac{\theta}{b-a}\Bigr)^2=M\,\mathbb{E}f-(\mathbb{E}f)^2\iff\mathbb{E}[f^2]\le M\,\mathbb{E}f,
$$
而 $0\le f\le M$ 蕴含 $f^2\le Mf$，所以成立。 $\square$

两种估计都由大数定律收敛，并可由中心极限定理构造置信区间；均值法的方差更小，是日常的首选。（投点法丢弃了信息：它只记录点是否在图像下方，而不记录下方多少。）

同样的估计也用于贝叶斯推断。对后验 $p(\theta\mid y)=L(\theta;y)p(\theta)/m(y)$，其中 $L(\theta;y)$ 是似然，$p(\theta)$ 是先验，$m(y)=\int L(\theta;y)p(\theta)\,\mathrm{d}\theta$，$f(\theta)$ 的后验均值

$$
\mu_f=\mathbb{E}(f(\theta)\mid y)=\int f(\theta)\frac{L(\theta;y)p(\theta)}{m(y)}\,\mathrm{d}\theta
$$
通常根本无法计算。若能抽样 $\theta^{(i)}\sim p(\cdot\mid y)$，$i=1,\dots,n$，则 $\hat\mu_f=\frac1n\sum_if(\theta^{(i)})=\bar f_n$，$\operatorname{Var}(\bar f_n)=\operatorname{Var}(f(\theta))/n$。我们关心不需要计算 $m(y)$ 的方法。

## 9.2. 重要性抽样

### 9.2.1. 重要性抽样估计

回顾拒绝抽样（[3.5.8](/3.5.8)）：为了在同一空间 $\Omega$ 上由 $Y\sim q$ 模拟 $X\sim p$，找 $c$ 使对一切 $x$ 有 $cq(x)\ge p(x)$，模拟 $y\sim q$ 与 $u\sim\mathrm{U}(0,1)$，若 $u<p(y)/(cq(y))$ 则接受 $y$。它有效是因为 $(y,ucq(y))$ 在 $cq$ 下方均匀分布，而被接受的点在 $p$ 下方均匀分布。重要性抽样讲的是一个略有不同的故事：它不产生 $p$ 的样本，而是直接用 $q$ 的样本估计 $p$ 下的期望。

**定义 9.2.1（重要性抽样）** 设 $\Omega$ 上 $X\sim p$，$\phi\colon\Omega\to\mathbb{R}$ 是给定函数，要求 $\theta=\mathbb{E}_p[\phi(X)]$，但只能抽样 $Y\sim q$，其中在 $\phi(x)p(x)\ne0$ 处 $q(x)>0$。由于

$$
\theta=\int\phi(x)p(x)\,\mathrm{d}x=\int\phi(x)\frac{p(x)}{q(x)}q(x)\,\mathrm{d}x=\mathbb{E}_q\bigl[\phi(Y)w(Y)\bigr],
$$
模拟 $Y_1,\dots,Y_n\overset{\text{iid}}{\sim}q$，并用**重要性权重** $w(Y_i)=p(Y_i)/q(Y_i)$ 构造加权平均

$$
\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^n\phi(Y_i)w(Y_i).
$$
这就是以 $q$ 为**提议分布**的**重要性抽样**（IS）。

取 $\phi\equiv1$，$\frac1n\sum_iw(Y_i)$ 是 $\mathbb{E}_p[1]=1$ 的 IS 估计；这是检查权重的有用办法。

**命题 9.2.1** 若 $\mathbb{E}_p[\phi(X)]$ 与 $\mathbb{E}_p[\phi^2(X)w(X)]$ 有限，则 $\hat\theta_n^{\mathrm{IS}}$ 无偏且相合。

**证明** 无偏性：

$$
\mathbb{E}_q\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^n\mathbb{E}_q\Bigl[\phi(Y_i)\frac{p(Y_i)}{q(Y_i)}\Bigr]=\frac1n\sum_{i=1}^n\int_\Omega\phi(y)\frac{p(y)}{q(y)}q(y)\,\mathrm{d}y=\frac1n\sum_{i=1}^n\mathbb{E}_p[\phi(X)]=\theta.
$$
相合性：由 **Markov 不等式**（对 $Z\ge0$ 有 $\mathbb{P}(Z\ge a)\le\mathbb{E}(Z)/a$），对任意 $\varepsilon>0$，

$$
\mathbb{P}\bigl(\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert\ge\varepsilon\bigr)=\mathbb{P}\bigl(\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert^2\ge\varepsilon^2\bigr)\le\frac{\mathbb{E}_q\lvert\hat\theta_n^{\mathrm{IS}}-\theta\rvert^2}{\varepsilon^2}=\frac{\operatorname{Var}_q\bigl(\phi(Y)w(Y)\bigr)}{n\varepsilon^2}\to0,
$$
因为 $\operatorname{Var}_q(\phi(Y)w(Y))\le\mathbb{E}_q[\phi^2w^2]=\mathbb{E}_p[\phi^2w]<\infty$。 $\square$

**例 9.2.1** 对 $a=1,2,3,\dots$ 与 $b>0$，可以用指数变量求和（变换法）模拟 $Y\sim\Gamma(a,b)$。设 $Y_i\overset{\text{iid}}{\sim}\Gamma(a,b)$，要对任意 $\alpha,\beta>0$ 求 $X\sim\Gamma(\alpha,\beta)$ 的 $\mathbb{E}_p[\phi(X)]$。$\Gamma(\alpha,\beta)$ 的密度为 $p(x;\alpha,\beta)=\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\beta x}$，所以

$$
w(y)=\frac{p(y)}{q(y)}=\frac{\Gamma(a)\beta^\alpha}{\Gamma(\alpha)b^a}y^{\alpha-a}\mathrm{e}^{-(\beta-b)y},\qquad\hat\theta_n^{\mathrm{IS}}=\frac{\Gamma(a)\beta^\alpha}{\Gamma(\alpha)b^a}\cdot\frac1n\sum_{i=1}^n\phi(Y_i)Y_i^{\alpha-a}\mathrm{e}^{-(\beta-b)Y_i}
$$
是 $\mathbb{E}_p[\phi(X)]$ 的无偏相合估计。同一批 $Y$ 可以"回收利用"，对许多 $\alpha$、$\beta$ 计算 $\mathbb{E}_{\alpha,\beta}[\phi(X)]$。

### 9.2.2. 重要性抽样估计的方差

**命题 9.2.2** 若 $\theta=\mathbb{E}_p[\phi(X)]$ 与 $\mathbb{E}_p[w(X)\phi^2(X)]$ 有限，则

$$
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)=\frac1n\Bigl(\mathbb{E}_p\bigl[w(X)\phi^2(X)\bigr]-\theta^2\Bigr).
$$

**证明**

$$
\begin{aligned}
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)&=\frac1n\operatorname{Var}_q\bigl(\phi(Y)w(Y)\bigr)=\frac1n\Bigl(\mathbb{E}_q\bigl[w^2(Y)\phi^2(Y)\bigr]-\bigl(\mathbb{E}_q[w(Y)\phi(Y)]\bigr)^2\Bigr)\\
&=\frac1n\Bigl(\int_\Omega\frac{p^2(y)}{q^2(y)}\phi^2(y)q(y)\,\mathrm{d}y-\theta^2\Bigr)=\frac1n\Bigl(\int_\Omega\frac{p(y)}{q(y)}\phi^2(y)p(y)\,\mathrm{d}y-\theta^2\Bigr)=\frac1n\Bigl(\mathbb{E}_p[w\phi^2]-\theta^2\Bigr). \qquad\square
\end{aligned}
$$

对朴素估计 $\hat\theta_n^{\mathrm{MC}}=\frac1n\sum_i\phi(X_i)$，$X_i\sim p$，有 $\operatorname{Var}(\hat\theta_n^{\mathrm{MC}})=\frac1n\bigl(\mathbb{E}_p[\phi^2]-\theta^2\bigr)$，因此

$$
\operatorname{Var}_q\bigl(\hat\theta_n^{\mathrm{IS}}\bigr)=\operatorname{Var}\bigl(\hat\theta_n^{\mathrm{MC}}\bigr)-\frac1n\mathbb{E}_p\bigl[(1-w(X))\phi^2(X)\bigr].
$$
当在 $\phi^2p$ 大的地方有 $w<1$（即 $q>p$）时，IS 降低方差：好的提议把更多质量放在 $\lvert\phi\rvert p$ 大的地方。降低方差是重要性抽样的主要目的。

每次使用 IS 都应检查这个方差有限，最好还很小，即 $\mathbb{E}_p[w\phi^2]<\infty$。若 $\phi(X)$ 的均值与方差有限，则 $\mathbb{E}_p[\phi^2]<\infty$；若权重还有界，即对一切 $x\in\Omega$ 有 $w(x)\le M$，则

$$
\mathbb{E}_p[w\phi^2]\le M\,\mathbb{E}_p[\phi^2]<\infty.
$$
这与拒绝抽样的条件 $p(x)/q(x)\le M$ 相同，只是现在只需要 $M$ 存在，而不需要知道它的值。这个条件只是充分的：$w$ 可以无界，而 $\mathbb{E}_p[w\phi^2]$ 仍然有限。因此重要性抽样的适用范围比拒绝抽样更广，而且由于不浪费任何样本，统计上也更有效。根本的要求是 $q$ 的尾部不比 $p$ 的尾部更薄。

**例 9.2.2** 对 Gamma 的例子，$\mathbb{E}_p[w\phi^2]\propto\int_0^\infty p(x)x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}\phi^2(x)\,\mathrm{d}x$。若 $\alpha\ge a$ 且 $\beta>b$，因子 $x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}$ 有界，这足以保证方差有限。对 $\phi(x)=1$，

$$
p(x)x^{\alpha-a}\mathrm{e}^{-(\beta-b)x}\propto x^{2\alpha-a-1}\mathrm{e}^{-(2\beta-b)x},
$$
它在 $(0,\infty)$ 上可积当且仅当 $a<2\alpha$ 且 $b<2\beta$；这是充分必要条件。取 $a=b=2$、$\alpha=0.5$、$\beta=2.5$，使 $2\alpha<a$。监视权重 $w(y_i)$ 与逐步的估计 $\hat\theta_m^{\mathrm{IS}}$，$m=1,\dots,n$，可以看到估计量不时被巨大的权重击中，始终稳定不下来。

### 9.2.3. 稀有事件

设 $X\sim p$，要求 $\mathbb{P}(X>x_0)=\mathbb{E}_p[\boldsymbol{1}\{X>x_0\}]$，其中 $x_0$ 位于 $p$ 的上尾深处。朴素样本中可能根本没有 $X_i>x_0$，此时 $\hat\theta_n=\frac1n\sum_i\boldsymbol{1}\{X_i>x_0\}$ 恰好为零。IS 取一个把更多概率放在大值上的 $q$，再重新加权得到 $p$ 下的期望，可以大幅降低方差。估计稀有事件的概率是重要性抽样最重要的应用之一；例如在金融中，它给出损失超过 $99.9\%$ 分位数的概率。

**例 9.2.3** 设 $p(x)=\mathcal{N}(x;\mu,\sigma^2)$，$\theta=\mathbb{P}(X>x_0)$，$x_0\gg\mu+3\sigma$。自然的提议位于 $x_0$ 上方：$q(y)=\mathcal{N}(y;x_0,\sigma^2)$。权重为

$$
w(y)=\frac{\mathcal{N}(y;\mu,\sigma^2)}{\mathcal{N}(y;x_0,\sigma^2)}=\exp\Bigl(-\frac{(y-\mu)^2}{2\sigma^2}+\frac{(y-x_0)^2}{2\sigma^2}\Bigr),\qquad\hat\theta_n^{\mathrm{IS}}=\frac1n\sum_{i=1}^nw(Y_i)\boldsymbol{1}\{Y_i>x_0\}.
$$
对 $X\sim\mathcal{N}(0,1)$ 的 $\mathbb{P}(X>4)=3.17\times10^{-5}$，取 $q=\mathcal{N}(4,1)$，每个用 $n=1000$ 的 $100$ 个估计的标准差，比朴素蒙特卡洛的小约 $100$ 倍，而后者的估计大多恰好为 $0$。

![重要性抽样。左：目标 Gamma(0.5, 2.5) 下 E_p[1] = 1 的逐步估计；提议 Gamma(2, 2) 违反 a < 2 alpha，被巨大的权重击中，而 Gamma(0.5, 1) 收敛。右：X ~ N(0, 1) 时 P(X > 4) 的 100 个估计（n = 1000）：朴素蒙特卡洛多数返回 0，从 N(4, 1) 作重要性抽样则很准确。](./plots/importance-sampling.py)

在尾部 $p$ 极小；覆盖它的拒绝包络 $cq$ 几乎会拒绝所有提议，一亿次朴素抽取也可能一次都碰不到这个事件。重要性抽样有意选择尾部较厚或向尾部平移的提议，在稀有区域大量抽样，再用很小的权重把样本"拉回"现实。它几乎是计算稀有事件概率唯一的经典非 Markov 链方法。

### 9.2.4. 未归一化的密度

归一化常数难以计算，所以我们偏好不必计算 $p$ 本身就能模拟 $X\sim p$ 的算法。设 $p(x)=\tilde p(x)/Z_p$，$q(x)=\tilde q(x)/Z_q$，能计算 $\tilde p$ 与 $\tilde q$，但不能计算 $Z_p$、$Z_q$。拒绝抽样仍然有效：找 $M$ 使对一切 $x$ 有 $M\ge\tilde p(x)/\tilde q(x)$；模拟 $y\sim q$（在拒绝抽样或 MCMC 抽样器中只需要 $\tilde q$）与 $u\sim\mathrm{U}(0,1)$；若 $u<\tilde p(y)/(M\tilde q(y))$，返回 $X=y$，否则重复。

**例 9.2.4** 设 $p(x)\propto\sin^2x/x^2$，$-\infty<x<\infty$，$q(y)\propto(1+y^2)^{-1}$ 为 Cauchy 分布。则

$$
\frac{\tilde p(x)}{\tilde q(x)}=\frac{(1+x^2)\sin^2x}{x^2}=\frac{\sin^2x}{x^2}+\sin^2x\le2=:M.
$$
模拟 $y\sim t_1$ 与 $u\sim\mathrm{U}(0,1)$；若 $u<\dfrac{(1+y^2)\sin^2y}{2y^2}$，返回 $X=y$；否则重复。

对重要性抽样也有同样的问题，因为 $w=p/q$ 需要归一化的密度。令 $\tilde w=\tilde p/\tilde q$，则

$$
\mathbb{E}_q\Bigl[\frac1n\sum_{i=1}^n\frac{\tilde p(Y_i)}{\tilde q(Y_i)}\phi(Y_i)\Bigr]=\frac{Z_p}{Z_q}\mathbb{E}_p[\phi(X)],\qquad\mathbb{E}_q\Bigl[\frac1n\sum_{i=1}^n\frac{\tilde p(Y_i)}{\tilde q(Y_i)}\Bigr]=\frac{Z_p}{Z_q}.
$$

**命题 9.2.3（自归一化重要性抽样）** 比值

$$
\hat\theta_n^{\mathrm{IS}}=\frac{\frac1n\sum_{i=1}^n\tilde w(Y_i)\phi(Y_i)}{\frac1n\sum_{i=1}^n\tilde w(Y_i)}=\frac{\sum_{i=1}^n\tilde w(Y_i)\phi(Y_i)}{\sum_{i=1}^n\tilde w(Y_i)}
$$
是 $\mathbb{E}_p[\phi(X)]$ 的相合估计：由大数定律，分子收敛到 $\frac{Z_p}{Z_q}\mathbb{E}_p[\phi(X)]$，分母收敛到 $\frac{Z_p}{Z_q}$。

这个自归一化重要性抽样（self-normalized importance sampling）估计在有限 $n$ 时有偏但相合，它也满足中心极限定理，方差可用 **Delta 方法**估计。由于它从不需要 $Z_p$，它是贝叶斯计算中求后验期望的关键工具。

**例 9.2.5** 回到例 9.2.1，$Y_i\sim\Gamma(a,b)$，目标为 $\Gamma(\alpha,\beta)$。去掉常数，$\tilde w(y)=y^{\alpha-a}\mathrm{e}^{-(\beta-b)y}$，$\sum_i\tilde w(Y_i)\phi(Y_i)/\sum_i\tilde w(Y_i)$ 是 $\mathbb{E}_p[\phi(X)]$ 的相合估计。为估计 $p=\Gamma(2,4)$ 的 $\mathbb{E}_pX$（真值 $\alpha/\beta=0.5$），取 $a=b=1$，即 $Y\sim\mathrm{Exp}(1)$：

```r
phi <- function(x) {x}
theta.est <- function(n, alpha, beta) {
  # IS estimate of E_p(phi(X)), X ~ Gamma(alpha, beta)
  y <- rexp(n)
  w <- y^(alpha-1) * exp(-(beta-1)*y)
  theta.hat <- sum(phi(y)*w)/sum(w)
  return(theta.hat)
}
theta.est(1000, alpha = 2, beta = 4)   # [1] 0.5043166
```

### 9.2.5. 拒绝抽样与重要性抽样

两种方法面对同一个困难——无法直接从目标 $p$ 中抽样——走了相反的路线。

| 方面 | 拒绝抽样 | 重要性抽样 |
|---|---|---|
| 对样本的处理 | 硬性淘汰：不合适的提议被丢弃，浪费计算 | 保留每个样本，用权重软性调节 |
| 对提议的要求 | 从上方包络：处处 $cq(x)\ge p(x)$ | 从下方兜底：$q$ 的尾部不比 $p$ 的薄（$p/q$ 有界即可） |
| 关键 | $c$ 要小（接受率 $1/c$ 高） | $p/q$（在 $\phi^2p$ 下）的方差要小 |
| 输出 | 真正来自 $p$ 的独立同分布样本 | 加权样本；只能求期望 |
| 方差 | 由接受率控制，总是有限 | 权重爆炸时可能无穷 |
| 稀有事件 | 无能为力：几乎没有提议被接受 | 首选方法：把 $q$ 倾斜到事件上 |
| 高维 | $c$ 随 $d$ 指数增长（$c\propto\kappa^d$），接受率 $\to0$ | 权重退化：几乎全部权重集中在一个样本上 |

拒绝抽样并没有被重要性抽样淘汰，原因有二。它产生真正的、独立的 $p$ 的样本；只要任务不只是求期望，而是要画直方图、作密度估计，或作为另一个随机过程的输入，就需要这样的样本。并且它的方差有绝对的安全边界：不会因为单个极端权重而出现灾难性的不稳定。

在高维中两种方法都会失效，但方式不同。对拒绝抽样，即使 $q$ 与 $p$ 在每个坐标上都很相似，$d$ 个坐标乘积的全局上界 $c$ 也会指数增长，接受率 $1/c$ 趋于零。对重要性抽样，$p$ 与 $q$ 的重合区域变得极窄，权重是许多比值的乘积：$100\,000$ 个样本中，可能一个样本就占了 $99.99\%$ 的总权重。此时有效样本量（effective sample size）

$$
\mathrm{ESS}=\frac{\bigl(\sum_{i=1}^nw_i\bigr)^2}{\sum_{i=1}^nw_i^2}\in[1,n]
$$
萎缩到 $1$ 左右，估计的方差巨大，实际上近乎无穷。

总之：低维、需要纯净样本且能找到紧的上界 $c$ 时，用拒绝抽样；低到中等维数下求期望、积分、尾部行为与稀有事件时，用重要性抽样；高维（例如许多贝叶斯后验那样 $d>10$）时两者都失效，就要转向 MCMC。

## 9.3. Markov 链

### 9.3.1. 定义

Markov 链是一个随机地从一个状态转移到另一个状态的过程，每一步都是"无记忆"的：未来只依赖当前状态，而不依赖过去。模拟的本性使我们只考虑离散时间的过程。

**定义 9.3.1（Markov 链）** 取值于可数集 $S$（状态空间）的随机变量序列 $X_0,X_1,\dots$ 称为 **Markov 链**，如果它具有 **Markov 性**

$$
\mathbb{P}(X_{n+1}=x\mid X_0=x_0,X_1=x_1,\dots,X_n=x_n)=\mathbb{P}(X_{n+1}=x\mid X_n=x_n)
$$
对一切 $n$ 与一切状态成立。若 $\mathbb{P}(X_{t+1}=j\mid X_t=i)=p_{ij}$ 不依赖于 $t$，称它是时齐的；矩阵 $P=(p_{ij})\in\mathbb{R}^{\lvert S\rvert\times\lvert S\rvert}$ 称为**转移矩阵**，$p_{ij}\ge0$，行和 $\sum_jp_{ij}=1$。

因此 Markov 链需要三个要素：一列随机变量（链），状态空间（它们取的值），以及转移矩阵（转移的规则）。下面的链都是时齐的。

**例 9.3.1** 从 $\{1,2,3\}$ 中抽数，记 $X_t$ 为时刻 $t$ 看到的最后一个数。有放回地抽取时，$X_t$ 独立同分布，是（平凡的）Markov 链。无放回地抽取时，$X_t$ 不是 Markov 链：给定 $X_2$ 时 $X_3$ 的分布依赖于 $X_1$，因为已抽到的数不会再出现。

Markov 链本质上是图上的随机游走。在有向图 $G=(V,E)$ 中，每个顶点是一个状态，每条边标有从一个状态移到另一个状态的概率；对每个顶点 $x$，出边构成一个分布，$\sum_jp_{xj}=1$。从顶点 $x_0$ 出发，按这些概率随机选一条出边，移到 $x_1$，如此重复。例如在 $S=\{1,2,3\}$ 上，

$$
P=\begin{bmatrix}0.6&0.2&0.2\\0.3&0.4&0.3\\0&0.3&0.7\end{bmatrix}.
$$

**注 9.3.1** Markov 性是随机过程的性质（未来只通过现在依赖过去）；**指数分布**的无记忆性 $\mathbb{P}(X>s+t\mid X>s)=\mathbb{P}(X>t)$ 是单个随机变量的分布的性质。两者不要混淆。

### 9.3.2. 平稳分布

设 $\{X_t\}_{t=0}^\infty$ 是 $S$ 上的时齐 Markov 链，初始分布 $X_0\sim\pi_0$（行向量），转移概率为 $p_{ij}$。$n$ 步转移概率 $p_{ij}^{(n)}=\mathbb{P}(X_{t+n}=j\mid X_t=i)$ 是 $P^n$ 的元素。记 $\pi_t(j)=\mathbb{P}(X_t=j)$，由**全概率公式**，

$$
\pi_t(j)=\sum_{i\in S}\pi_{t-1}(i)p_{ij}=(\pi_{t-1}P)(j)=(\pi_0P^t)(j).
$$
原则上，关于 Markov 链概率行为的任何问题都可以用矩阵运算回答。

**定义 9.3.2（平稳分布）** $S$ 上的分布 $\pi$ 若满足 $\pi=\pi P$，即对一切 $j$ 有 $\pi(j)=\sum_i\pi(i)p_{ij}$，称为链的**平稳分布**。若分布 $\pi$ 对一切 $i,j$ 满足 $\lim_{n\to\infty}p_{ij}^{(n)}=\pi(j)$，称为链的极限分布。

条件 $\pi^{\mathsf T}=P^{\mathsf T}\pi^{\mathsf T}$ 说明 $\pi^{\mathsf T}$ 是 $P^{\mathsf T}$ 对应于特征值 $1$ 的特征向量。由于 $P\boldsymbol{1}=\boldsymbol{1}$，特征值 $1$ 总是存在；由于 $P^n$ 对一切 $n$ 仍是随机矩阵，没有模大于 $1$ 的特征值。

**定理 9.3.1（细致平衡）** 设 $S$ 是离散状态空间，$\pi$ 是 $S$ 上的分布。若对一切 $i,j\in S$

$$
\pi(i)p_{ij}=\pi(j)p_{ji},
$$
则 $\pi$ 是 $P$ 的平稳分布。

**证明** $(\pi P)(i)=\sum_j\pi(j)p_{ji}=\sum_j\pi(i)p_{ij}=\pi(i)\sum_jp_{ij}=\pi(i)$。 $\square$

这个等式称为细致平衡条件（detailed balance condition）；满足它的链称为可逆 Markov 链（reversible Markov chain），因为在平衡状态下每个转移 $i\to j$ 与反向转移 $j\to i$ 发生得一样频繁。细致平衡是平稳的充分而非必要条件，但比 $\pi=\pi P$ 容易验证得多；下面的每个 MCMC 算法都建立在它之上。

**推论 9.3.1** 若 $S$ 有限且 $P$ 对称，$P=P^{\mathsf T}$，则均匀分布 $\pi(i)=1/\lvert S\rvert$ 是平稳的；链是可逆的，因为任何转移在正向与反向发生的概率相同。更一般地，只要 $P$ 是双随机的，即列和也为 $1$，均匀分布就是平稳的，例如

$$
P=\begin{bmatrix}0.2&0.3&0.5\\0.4&0.3&0.3\\0.4&0.4&0.2\end{bmatrix},\qquad\pi=\bigl(\tfrac13,\tfrac13,\tfrac13\bigr).
$$

**例 9.3.2** 考虑 $S=\{0,1\}$ 上的两状态链

$$
P=\begin{bmatrix}1-a&a\\b&1-b\end{bmatrix},\qquad a,b\in[0,1],\ 0<a+b<2,
$$
以概率 $\alpha$ 从状态 $0$ 出发，$\pi_0=(\alpha,1-\alpha)$。$P$ 的特征值为 $1$ 与 $1-a-b$，且

$$
P^n=\frac{1}{a+b}\begin{bmatrix}b&a\\b&a\end{bmatrix}+\frac{(1-a-b)^n}{a+b}\begin{bmatrix}a&-a\\-b&b\end{bmatrix}
$$
（记 $E_1,E_2$ 为上面两个矩阵连同因子 $1/(a+b)$，则 $P=E_1+(1-a-b)E_2$，且 $E_1^2=E_1$，$E_2^2=E_2$，$E_1E_2=E_2E_1=O$，所以 $P^n=E_1+(1-a-b)^nE_2$）。由于 $\lvert1-a-b\rvert<1$，

$$
\lim_{n\to\infty}P^n=\frac{1}{a+b}\begin{bmatrix}b&a\\b&a\end{bmatrix},\qquad\pi=\lim_{n\to\infty}\pi_n=\Bigl(\frac{b}{a+b},\frac{a}{a+b}\Bigr)
$$
对每个 $\alpha$ 成立。由 $\pi=\pi P$ 也得到同一个 $\pi$：第一个坐标给出 $\pi(0)(1-a)+\pi(1)b=\pi(0)$，即 $a\pi(0)=b\pi(1)$，这也就是细致平衡条件。

平稳概率还有第二层含义。设 $R$ 是首次回到状态 $0$ 的时间，$r_0=\mathbb{E}(R\mid X_0=0)$ 是平均返回时间（mean return time）。对第一步取条件：若 $X_1=0$，则 $R=1$；若 $X_1=1$，则 $R=1+G$，其中 $G\sim\mathrm{Geo}(b)$ 是离开状态 $1$ 所需的时间，所以 $\mathbb{E}(R\mid X_1=1)=1+1/b$，且

$$
r_0=(1-a)\cdot1+a\Bigl(1+\frac1b\Bigr)=\frac{a+b}{b}=\frac1{\pi(0)}.
$$
同理 $r_1=(a+b)/a=1/\pi(1)$。一般地，对不可约正常返链（定义见下），$r_i=1/\pi(i)$：若 $\pi(i)=1/4$，链有四分之一的时间处于状态 $i$，平均需要四步才回到它。

平稳分布不一定是极限分布。取 $a=b=1$，$P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ 有平稳分布 $\pi=(\frac12,\frac12)$，因为 $\pi P=\pi$。但 $X_{n+2}=X_n$：链来回交替，$n$ 为偶数时 $X_n=X_0$，为奇数时 $X_n=X_1$，所以 $P^n$ 没有极限，$X_n$ 的分布不收敛，并且依赖于初始分布。有时极限分布根本不存在。

### 9.3.3. 基本极限定理

链的长期行为由三条性质控制：它应能在状态空间中自由移动，不应确定性地循环，而且应能回来。

**定义 9.3.3（不可约性）** 若对某个 $n\ge0$ 有 $p_{ij}^{(n)}>0$，称状态 $j$ 可由 $i$ 到达（$i\to j$）；若 $i\to j$ 且 $j\to i$，称 $i$ 与 $j$ 互通（$i\leftrightarrow j$）。若每一对状态都互通，即 $S$ 只构成一个互通类，称链或其转移矩阵 $P$ **不可约**；等价地，转移图是强连通的。

**定义 9.3.4（周期）** 状态 $i$ 的**周期**是 $d_i=\gcd\{n\ge1\colon p_{ii}^{(n)}>0\}$。若 $d_i=1$，称状态 $i$ **非周期**，此时回到 $i$ 可以发生在不规则的时刻；对 $d_i=1$ 的状态存在 $n'$，使对一切 $n\ge n'$ 有 $p_{ii}^{(n)}>0$。若所有状态都非周期，称链非周期。

例如 $S=\{0,1\}$、$P=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ 有 $d_0=d_1=2$。同样，在 $S=\{1,2,3,4\}$ 上取 $\pi_0=(1,0,0,0)$ 与

$$
P=\begin{bmatrix}0&1/2&0&1/2\\1/2&0&1/2&0\\0&1/2&0&1/2\\1/2&0&1/2&0\end{bmatrix},
$$
对一切奇数 $n$ 有 $p_{11}^{(n)}=0$，每个状态的周期都是 $2$。

**定理 9.3.2** 若状态 $i,j\in S$ 互通，则 $d_i=d_j$。特别地，不可约链的所有状态有相同的周期。

**证明** 由于 $j$ 可由 $i$ 到达，存在 $n_1$ 使 $p_{ij}^{(n_1)}>0$；由于 $i$ 可由 $j$ 到达，存在 $n_2$ 使 $p_{ji}^{(n_2)}>0$。于是 $p_{ii}^{(n_1+n_2)}\ge p_{ij}^{(n_1)}p_{ji}^{(n_2)}>0$，所以 $d_i\mid(n_1+n_2)$。设 $n$ 是任意满足 $p_{jj}^{(n)}>0$ 的整数，则 $p_{ii}^{(n_1+n+n_2)}>0$，所以 $d_i\mid(n_1+n+n_2)$，从而 $d_i\mid n$。因此 $d_i$ 整除 $\{n\colon p_{jj}^{(n)}>0\}$ 的每个元素，$d_j\ge d_i$。交换 $i$ 与 $j$ 的角色得 $d_i\ge d_j$。 $\square$

使不可约链变为非周期的一个简单技巧是加一个自环：对某个状态 $i$ 令 $p_{ii}>0$。

**定义 9.3.5（常返性）** 若离开某状态后有正的概率永不返回，称该状态为**暂态**；若链以概率 $1$ 返回它，称它为**常返**的。平均返回时间有限的常返状态称为**正常返**的，无穷的称为**零常返**的（以概率 $1$ 返回并不意味着期望返回时间有限）。

在有限状态空间上，不可约链的每个状态都是正常返的。

**定理 9.3.3（基本极限定理）** 设 Markov 链 $X_0,X_1,\dots$ 不可约、非周期且正常返（对有限状态空间：不可约且非周期）。则存在唯一的平稳分布 $\pi$，且对任意初始分布 $\pi_0$，

$$
\lim_{n\to\infty}\pi_n(i)=\pi(i)\quad\text{for all states } i;
$$
等价地，$\lim_{n\to\infty}P^n$ 是各行都等于 $\pi$ 的矩阵。

我们说这条链"瞄准"了 $\pi$：无论从哪里出发，一段时间后它处于状态 $i$ 的概率都约为 $\pi(i)$。具有这三条性质的链称为遍历（ergodic）的：遍历 = 不可约 + 非周期 + 正常返。对模拟而言最重要的推论是遍历定理：对平稳分布为 $\pi$ 的不可约正常返链以及任何满足 $\mathbb{E}_\pi\lvert\phi\rvert<\infty$ 的 $\phi$，从任意初始状态出发都有

$$
\frac1n\sum_{t=0}^{n-1}\phi(X_t)\xrightarrow{\text{a.s.}}\mathbb{E}_\pi[\phi(X)].
$$
这是 Markov 链的大数定律；沿一条路径的平均代替了独立样本的平均。

把两部分合在一起就得到 MCMC。我们要求 $S$ 上的概率质量函数或密度 $p$ 下的 $\mathbb{E}_p[\phi(X)]$。按蒙特卡洛方法，问题归结为生成分布为 $p$ 的 $S$ 中的随机元素；MCMC 的做法是构造一条平稳分布 $\pi=p$ 的 Markov 链。模拟一个相关的序列 $X_0,X_1,X_2,\dots$，使 $X_t\sim\pi$（或至少 $X_t\xrightarrow{d}\pi$），再用通常的估计

$$
\hat\phi_n=\frac1n\sum_{t=0}^{n-1}\phi(X_t).
$$
例如 $\{0,1\}^m$ 上的随机游走：从 $\{1,\dots,m\}$ 中均匀随机地取 $j$，翻转 $X_{t-1}=(z_1,\dots,z_m)$ 的第 $j$ 个坐标，$X_t=(z_1,\dots,1-z_j,\dots,z_m)$；转移矩阵对称，所以这条链瞄准均匀分布。MCMC 方法也适用于可数无穷与连续的状态空间，是我们所拥有的最灵活的蒙特卡洛算法之一。

## 9.4. Metropolis–Hastings 算法

### 9.4.1. 算法

设需要来自 $S=\{1,\dots,m\}$ 上的概率质量函数 $\pi(x)=\tilde\pi(x)/Z_\pi$ 的样本，只知道它相差常数 $Z_\pi$ 的形式。只需给出由 $X_t$ 模拟 $X_{t+1}$ 的规则。在所有 Metropolis–Hastings（MH）算法中，候选点 $Y$ 由提议分布 $q(\cdot\mid X_t)$ 生成，$Y\sim q(\cdot\mid x)$ 表示 $\mathbb{P}(Y=y\mid X=x)=q(y\mid x)$。若候选点被接受，链移到 $X_{t+1}=Y$；否则留在原处，$X_{t+1}=X_t$。提议可以依赖当前状态；它的选取非常灵活，但得到的链必须收敛到目标 $\pi$。

**算法 9.4.1（Metropolis–Hastings 算法）**

1. 选择提议分布 $q(\cdot\mid X_t)$，满足正则条件（链必须不可约且非周期）。
2. 生成 $X_0$，例如从 $q$ 中生成。
3. 重复，直到按某个准则判断链已收敛到平稳分布：
   1. 从 $q(\cdot\mid X_t)$ 生成 $Y$，从 $\mathrm{U}(0,1)$ 生成 $U$；
   2. 若
      $$
      U\le\alpha(Y\mid X_t)=\min\Bigl\{1,\frac{\tilde\pi(Y)\,q(X_t\mid Y)}{\tilde\pi(X_t)\,q(Y\mid X_t)}\Bigr\},
      $$
      接受 $Y$，令 $X_{t+1}=Y$；否则令 $X_{t+1}=X_t$；
   3. $t$ 增加 $1$。

候选点以概率 $\alpha(Y\mid X_t)$ 被接受，这就是接受概率；由于只出现比值 $\tilde\pi(Y)/\tilde\pi(X_t)$，只需知道目标的一个常数倍。

**定理 9.4.1** Metropolis–Hastings 算法生成的 Markov 链关于 $\pi$ 满足细致平衡；因此 $\pi$ 是平稳分布，若链不可约且非周期，$\pi$ 就是它的极限分布。

**证明** 由基本极限定理，只需证明 $\pi$ 是平稳的；由定理 9.3.1，只需证明 $\pi(x)p_{xy}=\pi(y)p_{yx}$。$x=y$ 时显然。对 $y\ne x$，链从 $X_t=x$ 移到 $X_{t+1}=y$ 当且仅当 $y$ 被提出且被接受，所以 $p_{xy}=q(y\mid x)\alpha(y\mid x)$，且

$$
\begin{aligned}
\pi(x)p_{xy}&=\pi(x)q(y\mid x)\min\Bigl\{1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\Bigr\}=\min\bigl\{\pi(x)q(y\mid x),\ \pi(y)q(x\mid y)\bigr\}\\
&=\pi(y)q(x\mid y)\min\Bigl\{1,\frac{\pi(x)q(y\mid x)}{\pi(y)q(x\mid y)}\Bigr\}=\pi(y)q(x\mid y)\alpha(x\mid y)=\pi(y)p_{yx}. \qquad\square
\end{aligned}
$$

### 9.4.2. 例子

**例 9.4.1** 设 $\pi(x)=x/Z_\pi$，$Z_\pi=\sum_{x=1}^mx$，$x=1,\dots,m$。取提议 $Y\sim\mathrm{U}\{1,\dots,m\}$，$q(y\mid x)=1/m$，它是不可约的（一步就能到达任何状态）。若 $X_t=x$：模拟 $y\sim\mathrm{U}\{1,\dots,m\}$ 与 $u\sim\mathrm{U}(0,1)$；若

$$
u\le\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\min\Bigl\{1,\frac yx\Bigr\},
$$
令 $X_{t+1}=y$，否则 $X_{t+1}=x$。链的轨迹（状态 $X_t$ 对 $t$）在 $\{1,\dots,30\}$ 中跳动，$X_t$ 的直方图随 $x$ 线性增长：

```r
m <- 30
n <- 10000; X <- rep(NA, n)
X[1] <- 1
for (t in 1:(n-1)) {
  x <- X[t]
  y <- ceiling(m*runif(1))     # uniform proposal on 1, ..., m
  a <- min(1, y/x)             # acceptance probability
  U <- runif(1)
  if (U <= a) {
    X[t+1] <- y
  } else {
    X[t+1] <- x
  }
}
plot(X[1:200], type = "l"); hist(X)
```

**例 9.4.2** 为模拟 **Poisson 分布** $\pi(x)=\mathrm{e}^{-\lambda}\lambda^x/x!\propto\lambda^x/x!$，用简单的提议 $q(y\mid x)=1/2$，$y=x\pm1$：掷一枚硬币，对 $x$ 加 $1$ 或减 $1$。若 $X_t=x$，模拟 $y\sim\mathrm{U}\{x-1,x+1\}$ 与 $u\sim\mathrm{U}(0,1)$。若 $y=-1$，则 $\alpha=0$；否则

$$
\alpha(y\mid x)=\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\begin{cases}\min\Bigl\{1,\dfrac{\lambda}{x+1}\Bigr\},&y=x+1,\\[2ex]\min\Bigl\{1,\dfrac{x}{\lambda}\Bigr\},&y=x-1.\end{cases}
$$
若 $u\le\alpha(y\mid x)$，令 $X_{t+1}=y$；否则 $X_{t+1}=x$。

对连续随机变量，同样的算法可以用密度来运行：计算机用很细的有限网格表示实数，一个网格单元的目标概率与提议概率近似等于密度乘以单元长度，而单元长度在 Hastings 比 $\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}$ 中相互抵消。所以有限空间上链的理论可以搬过来；严格的处理要用一般状态空间上的转移核。

**例 9.4.3** 为模拟 $X\sim\mathcal{N}(0,1)$，目标 $\tilde\pi(x)\propto\exp(-x^2/2)$，需要一个简单的不可约提议。固定 $a>0$，在以 $x$ 为中心、长 $2a$ 的窗口中均匀地选新点，$q(y\mid x)=\frac{1}{2a}\boldsymbol{1}\{x-a<y<x+a\}$。则 $q(y\mid x)=q(x\mid y)$，算法为：若 $X_t=x$，模拟 $y\sim\mathrm{U}(x-a,x+a)$ 与 $u\sim\mathrm{U}(0,1)$；若 $u\le\alpha(y\mid x)$，令 $X_{t+1}=y$，否则 $X_{t+1}=x$，其中

$$
\alpha(y\mid x)=\min\Bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\Bigr\}=\min\Bigl\{1,\exp\Bigl(-\frac{y^2}2+\frac{x^2}2\Bigr)\Bigr\}.
$$

```r
a <- 3; n <- 2000
X <- numeric(n); X[1] <- 0
for (t in 1:(n-1)) {
  x <- X[t]
  y <- x + (2*runif(1) - 1)*a          # uniform proposal on (x - a, x + a)
  if (runif(1) < exp((x^2 - y^2)/2)) {
    X[t+1] <- y
  } else {
    X[t+1] <- x
  }
}
```

### 9.4.3. 特殊情形

- Metropolis 算法（Metropolis algorithm）：提议对称，$q(x\mid y)=q(y\mid x)$，接受概率化为 $\min\{1,\tilde\pi(Y)/\tilde\pi(X_t)\}$；向"上坡"的移动总被接受，向"下坡"的移动有时被接受。例 9.4.1–9.4.3 都属于这一类。
- 随机游走 Metropolis 算法（random walk Metropolis）：$q(y\mid x)=g(y-x)$，$g$ 是对称密度。每次迭代生成增量 $Z\sim g$，令 $Y=X_t+Z$。
- 独立抽样器（independence sampler）：提议不依赖当前状态，$q(y\mid x)=q(y)$。接受概率为 $\min\{1,w(Y)/w(X_t)\}$，其中 $w=\tilde\pi/q$ 是重要性权重，这把 MH 与重要性抽样联系起来；当 $q$ 接近 $\pi$ 且尾部更厚时，这个抽样器效果好。
- Gibbs 抽样，见下一节。

## 9.5. Gibbs 抽样

当目标是多元分布 $\pi(\boldsymbol{x})$，$\boldsymbol{x}=(x_1,\dots,x_d)$ 时，常用 Gibbs 抽样。记 $\boldsymbol{x}_{(-j)}=(x_1,\dots,x_{j-1},x_{j+1},\dots,x_d)$；给定 $\boldsymbol{X}_{(-j)}=\boldsymbol{x}_{(-j)}$ 时 $X_j$ 的分布是完全条件分布（full conditional distribution）$\pi(x_j\mid\boldsymbol{x}_{(-j)})$。把 $X_t$ 记为 $\boldsymbol{X}(t)$。

**算法 9.5.1（Gibbs 抽样）**

1. 在时刻 $t=0$ 初始化 $\boldsymbol{X}(0)$。
2. 对每次迭代 $t=1,2,\dots$：
   1. 令 $\boldsymbol{x}=\boldsymbol{X}(t-1)$；
   2. 对每个坐标 $j=1,\dots,d$，从 $\pi(x_j\mid\boldsymbol{x}_{(-j)})$ 生成 $X_j^*(t)$，并更新 $x_j=X_j^*(t)$；
   3. 令 $\boldsymbol{X}(t)=(X_1^*(t),\dots,X_d^*(t))$；每个候选点都被接受。

Gibbs 抽样特别自然，只要条件分布容易抽样，它就效果很好。考虑二元密度 $\pi(\theta_1,\theta_2)$，设 $(\theta_1,\theta_2)\sim\pi$。先模拟 $\theta_1'\sim\pi(\theta_1'\mid\theta_2)$，再用新的 $\theta_1'$ 模拟 $\theta_2'\sim\pi(\theta_2'\mid\theta_1')$。$(\theta_1',\theta_2')$ 的分布为

$$
\begin{aligned}
p(\theta_1',\theta_2')&=\int\!\!\int\pi(\theta_1,\theta_2)\,\pi(\theta_1'\mid\theta_2)\,\pi(\theta_2'\mid\theta_1')\,\mathrm{d}\theta_1\,\mathrm{d}\theta_2
=\int\!\!\int\pi(\theta_1,\theta_2)\frac{\pi(\theta_1',\theta_2)}{\pi(\theta_2)}\cdot\frac{\pi(\theta_1',\theta_2')}{\pi(\theta_1')}\,\mathrm{d}\theta_1\,\mathrm{d}\theta_2\\
&=\pi(\theta_1',\theta_2')\int\pi(\theta_1\mid\theta_2)\,\mathrm{d}\theta_1\int\pi(\theta_2\mid\theta_1')\,\mathrm{d}\theta_2=\pi(\theta_1',\theta_2'),
\end{aligned}
$$
因为每个积分都等于 $1$（第二步中 $\pi(\theta_1,\theta_2)/\pi(\theta_2)=\pi(\theta_1\mid\theta_2)$，$\pi(\theta_1',\theta_2)/\pi(\theta_1')=\pi(\theta_2\mid\theta_1')$）。所以若 $\theta^{(0)}=(\theta_1,\theta_2)\sim\pi$，经过这两步后 $\theta^{(1)}=(\theta_1',\theta_2')\sim\pi$ 是一个新的、相关的样本，迭代下去得到 $\theta^{(2)},\theta^{(3)},\dots$：$\pi$ 是平稳的。Gibbs 抽样有几种变体。在多元情形 $\theta=(\theta_1,\dots,\theta_K)$，可以对 $i=1,\dots,K$ 依次抽样 $\pi(\theta_i\mid\theta_{(-i)})$（系统扫描），也可以在每一步选 $i\sim\mathrm{U}\{1,\dots,K\}$（随机扫描）。每构造一个新的抽样器，都必须检查遍历性条件。

**命题 9.5.1** 考虑目标为 $\pi(\theta_1,\theta_2)$、提议为 $q(\theta_1'\mid\theta)=\pi(\theta_1'\mid\theta_2)$、只更新 $\theta_1$ 的 MH 算法。它的接受概率等于 $1$；因此 Gibbs 抽样是一种 Metropolis–Hastings 抽样。

**证明** 记 $X_t=(\theta_1,\theta_2)$，$Y=(\theta_1',\theta_2)$，$\tilde\pi=\pi$，$q(Y\mid X_t)=\pi(\theta_1'\mid\theta_2)$，$q(X_t\mid Y)=\pi(\theta_1\mid\theta_2)$，则

$$
\alpha(Y\mid X_t)=\min\Bigl\{1,\frac{\pi(\theta_1',\theta_2)\,\pi(\theta_1\mid\theta_2)}{\pi(\theta_1,\theta_2)\,\pi(\theta_1'\mid\theta_2)}\Bigr\}=\min\Bigl\{1,\frac{\pi(\theta_2)}{\pi(\theta_2)}\Bigr\}=1,
$$
因为 $\pi(\theta_1',\theta_2)/\pi(\theta_1'\mid\theta_2)=\pi(\theta_2)=\pi(\theta_1,\theta_2)/\pi(\theta_1\mid\theta_2)$。 $\square$

**例 9.5.1** 对相关系数为 $\rho$ 的标准**二元正态分布**，完全条件分布为 $X\mid Y=y\sim\mathcal{N}(\rho y,1-\rho^2)$ 与 $Y\mid X=x\sim\mathcal{N}(\rho x,1-\rho^2)$（[3.1.15](/3.1.15)）。Gibbs 抽样交替进行这两次抽取。每一步都平行于一条坐标轴；当 $\lvert\rho\rvert$ 接近 $1$ 时，密度是沿对角线的窄脊，步子很短，链对分布的探索很慢。事实上序列 $X_t$ 是系数为 $\rho^2$ 的 AR(1) 过程，其滞后 $k$ 的自相关为 $\rho^{2k}$。

![标准二元正态的 Gibbs 抽样。左：rho = 0.9 时从 (-3, 3) 出发的前 15 轮扫描，沿密度的脊平行于坐标轴移动。右：第一个坐标的轨迹，rho = 0.5 时混合很快，rho = 0.99 时缓慢游荡。](./plots/gibbs-bivariate-normal.py)

## 9.6. 收敛诊断

基本极限定理只保证 $n\to\infty$ 时收敛；实践中必须决定链运行多久、用其中的多少。标准做法有：

- 预烧期（burn-in）：丢弃链的初始段，其间链从初始点移到 $\pi$ 的质量所在的区域；只对其余的状态取平均。
- 轨迹图，即 $X_t$ 对 $t$ 的图：混合良好的链看起来像平稳噪声，没有趋势或长段的平台。从分散的初始点出发的几条链应当相互重叠。
- 自相关：相继的状态是相关的，这会增大 $\hat\phi_n$ 的方差。记 $\phi(X_t)$ 的滞后 $k$ 自相关为 $\rho_k$，则 $\operatorname{Var}(\hat\phi_n)\approx\frac{\operatorname{Var}_\pi(\phi)}{n}\bigl(1+2\sum_{k\ge1}\rho_k\bigr)$，所以这条链相当于 $n/(1+2\sum_k\rho_k)$ 个独立抽样（它的有效样本量）。
- Gelman–Rubin 统计量 $\hat R$ 比较几条平行链之间的方差与链内的方差；接近 $1$ 的值（例如小于 $1.01$–$1.1$）表明已经收敛。

提议的尺度决定随机游走 Metropolis 的混合。步子小，几乎总被接受，但移动很慢；步子大，很少被接受，链停滞不动。两者都导致高自相关。一个理论上的指导（Roberts、Gelman 与 Gilks，1997）是：一维时接受率约 $0.44$，高维时约 $0.234$。

![N(0, 1) 的随机游走 Metropolis，提议在 (x - a, x + a) 上均匀，从 10 出发。a = 0.1 时几乎每一步都被接受，但链缓慢地漂向目标；a = 30 时几乎所有提议都被拒绝，轨迹长时间平直；a = 2.5 混合良好，在 200 次迭代的预烧期之后自相关衰减最快。](./plots/rw-metropolis-mixing.py)

## 小结

- 经典蒙特卡洛：投点法与均值法都基于大数定律；均值法的方差更小。
- 无法直接从 $p$ 中抽样时的两条镜像路线。拒绝抽样（硬淘汰）用 $cq$ 从上方控制 $p$；它给出真正的独立同分布样本，方差安全，但 $c$ 在高维中爆炸。重要性抽样（软加权）不需要 $c$、不浪费样本，权重 $w=p/q$；它是稀有事件的工具，自归一化后可用于未归一化的后验，但其权重在高维中退化。
- Markov 链：Markov 性与转移矩阵；平稳分布满足 $\pi=\pi P$，细致平衡 $\pi_ip_{ij}=\pi_jp_{ji}$ 充分但不必要；周期链可以有平稳分布而没有极限分布。基本极限定理：不可约 + 非周期 + 正常返（遍历）$\Rightarrow$ 平稳分布唯一，且从任意起点出发都以它为极限。
- MCMC 把两种蒙特卡洛思想结合起来：构造一条平稳分布为目标的链，让它收敛，再用沿相关链的平均代替独立样本的平均。Metropolis–Hastings 以概率 $\min\bigl\{1,\frac{\tilde\pi(y)q(x\mid y)}{\tilde\pi(x)q(y\mid x)}\bigr\}$ 接受 $Y\sim q(\cdot\mid x)$；Gibbs 抽样从完全条件分布中逐个抽取坐标，并总是接受。实践中要丢弃预烧期，检查轨迹图与自相关，并调整提议。

| 方法 | 样本的独立性 | 目标 | 用途 | 高维 |
|---|---|---|---|---|
| 朴素蒙特卡洛 | 独立 | 易于抽样 | 期望、积分 | 可以，只要能抽样 |
| 重要性抽样 | 加权、独立 | 任意，需提议 | 期望、积分 | 权重退化 |
| 拒绝抽样 | 独立 | 任意，需包络 | 样本 | 接受率指数衰减 |
| MCMC | 相关 | 任意，可未归一化 | 期望、样本 | 标准工具 |
