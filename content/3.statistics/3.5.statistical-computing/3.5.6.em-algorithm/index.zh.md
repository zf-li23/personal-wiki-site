---
title: EM 算法
description: 隐变量与完全数据，E 步与 M 步，由 Jensen 不等式以及对数似然分解为证据下界与 Kullback–Leibler 散度得到的上升性质，例题（两枚硬币、身高、遗传连锁多项分布），广义 EM 与变分 EM，收敛速率与 Louis 加速，以及高斯混合与两成分混合模型的 EM。
source_hash: e5311e8151c2
---

观测数据常常是不完全的：有些值缺失，有些标签被隐藏，或者模型最自然的描述要借助我们从未观测到的量。这时观测数据的似然在对数内部含有求和或积分，没有闭式的极大值点；牛顿型方法（[3.5.5](/3.5.5)）需要这个别扭函数的导数，在高维时还可能不稳定。[3.4.11](/3.4.11) 中为高斯混合引入的 **EM 算法**把这类问题变成一列容易的问题：E 步在当前参数下用条件期望补全数据，M 步极大化补全后的对数似然。本章建立一般理论：为什么每次迭代都使似然增加（Jensen 不等式，或把对数似然分解为证据下界与一个 **Kullback–Leibler 散度**）；它收敛多快、怎样加速（Louis 方法，与观测信息和完全信息相联系）；以及两种推广，广义 EM 与变分 EM，它们通向近似贝叶斯推断（[3.7](/3.7)）。最后一部分把 EM 用于混合模型。始终要记住，EM 只是计算 [3.2.3](/3.2.3) 中 MLE 的一种方法。

## 6.1. EM 算法的基本原理

### 6.1.1. 隐变量

**例 6.1.1（一枚硬币）** 一枚硬币 $\mathbb{P}(H) = \theta$，$\mathbb{P}(T) = 1 - \theta$。为估计 $\theta$，抛 $n$ 次，得到 $h$ 次正面、$n - h$ 次反面。似然是二项的，$L(\theta) = \binom{n}{h}\theta^h(1 - \theta)^{n-h}$；求导并令其为零得极大似然估计 $\hat\theta = h/n$，即自然的估计。

**例 6.1.2（两枚硬币，完全数据）** 现在有两枚硬币 $A$ 与 $B$，目标是估计 $\theta_A$ 与 $\theta_B$。共做 5 次，每次选一枚硬币 $Z_i \in \{A, B\}$（$i = 1, \dots, 5$），抛 10 次：

| 轮次 $i$ | 硬币 $Z_i$ | 结果 |
|---|---|---|
| 1 | $B$ | 5 正，5 反 |
| 2 | $A$ | 9 正，1 反 |
| 3 | $A$ | 8 正，2 反 |
| 4 | $B$ | 4 正，6 反 |
| 5 | $A$ | 7 正，3 反 |

似然（略去二项系数）是五轮的乘积，

$$
L(\boldsymbol{\theta}) = \theta_B^5(1 - \theta_B)^5\cdot\theta_A^9(1 - \theta_A)\cdot\theta_A^8(1 - \theta_A)^2\cdot\theta_B^4(1 - \theta_B)^6\cdot\theta_A^7(1 - \theta_A)^3 = \theta_A^{24}(1 - \theta_A)^6\,\theta_B^9(1 - \theta_B)^{11},
$$
所以 MLE 是每枚硬币的正面比例，

$$
\hat\theta_A = \frac{\#\text{heads using }A}{\#\text{flips using }A} = \frac{24}{24 + 6} = 0.8, \qquad \hat\theta_B = \frac{\#\text{heads using }B}{\#\text{flips using }B} = \frac{9}{9 + 11} = 0.45.
$$

如果不知道每一轮用的是哪枚硬币呢？似然变成 $\theta_{Z_1}^5(1 - \theta_{Z_1})^5\,\theta_{Z_2}^9(1 - \theta_{Z_2})\cdots$，其中 $Z_i$ 未知，$\arg\max_{\boldsymbol{\theta}}L(\boldsymbol{\theta})$ 无法一步算出：这是一个缺失数据问题。数据完全时 MLE 就是频率；硬币标签缺失时，观测数据的似然含有未知的 $Z$，难以直接极大化。出路是把未知的 $Z$ 当作随机变量，用它的后验概率加权来补全数据。

**定义 6.1.1（隐变量与完全数据）** 在 EM 框架中，$X$ 是观测变量（样本的观测值），$Z$ 是**隐变量**（如观测所属的类别标签），它影响数据但没有被观测到。观测数据 $X$ 是**不完全数据**，$Y = (X, Z)$ 是**完全数据**。记待估参数为 $\theta$，观测数据的对数似然为 $\ell(\theta; x) = \log p(x \mid \theta)$，完全数据的对数似然为 $\ell_c(\theta; x, Z) = \log p(x, Z \mid \theta)$。

观测变量可以直接测量：一段语音录音的波形，今天是否下雨，烟雾报警器是否响了。隐变量（也称潜在因子）影响数据，却不容易测量：产生这段录音的音素，已知昨天下雨时今天下雨的概率，烟雾报警器是否失灵。完全数据 $Y = (X, Z)$ 是我们希望拥有的数据。

考虑反问题：给定 $(\theta_A, \theta_B) = (0.6, 0.5)$ 和相等的先验概率 $\mathbb{P}(Z_i = A) = \mathbb{P}(Z_i = B) = 1/2$，第一轮出现 5 正 5 反。由 **Bayes 公式**，所用硬币是 $A$ 的概率为

$$
\mathbb{P}(Z_1 = A \mid x_1) = \frac{\mathbb{P}(x_1 \mid Z_1 = A)\,\mathbb{P}(Z_1 = A)}{\mathbb{P}(x_1 \mid Z_1 = A)\,\mathbb{P}(Z_1 = A) + \mathbb{P}(x_1 \mid Z_1 = B)\,\mathbb{P}(Z_1 = B)} = \frac{0.6^5\times0.4^5}{0.6^5\times0.4^5 + 0.5^5\times0.5^5} \approx 0.45,
$$
是 $B$ 的概率为 $0.55$。EM 算法在隐藏标签的这种后验概率与参数估计之间交替迭代。

### 6.1.2. 算法

回忆**条件期望**。在回归中，$Y = f(X) + \varepsilon$、$\mathbb{E}\varepsilon = 0$ 给出 $\mathbb{E}(Y \mid X) = f(X)$。对分布为 $P_Z$ 的离散随机变量 $Z$，$\mathbb{E}[Z] = \sum_z z\mathbb{P}_Z(z)$，$\mathbb{E}[h(Z)] = \sum_z\mathbb{P}_Z(z)h(z)$；给定 $X = x$，$\mathbb{E}[h(Z) \mid x] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x)h(z)$。这里需要的是

$$
\mathbb{E}_{Z\mid x, \hat\theta^{(t)}}\bigl[\log \mathbb{P}(x, Z \mid \theta)\bigr] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x, \hat\theta^{(t)})\log \mathbb{P}(x, z \mid \theta):
$$
先由观测数据 $x$ 推断未观测的 $z$ 的概率 $\mathbb{P}_{Z\mid X}(z \mid x, \theta = \hat\theta^{(t)})$，再在这个分布下求完全数据对数似然的期望。

**定义 6.1.2（EM 算法）** 给出 $\theta$ 的初始估计 $\hat\theta^{(0)}$，重复直至收敛：

1. E 步：计算 **Q 函数**
   $$
   Q(\theta \mid \hat\theta^{(t)}) \triangleq \mathbb{E}_{Z\mid x, \hat\theta^{(t)}}\bigl[\log \mathbb{P}(x, Z \mid \theta)\bigr] = \sum_z\mathbb{P}_{Z\mid X}(z \mid x, \theta = \hat\theta^{(t)})\log \mathbb{P}(x, z \mid \theta),
   $$
   即在当前参数下隐变量的后验分布之下，完全数据对数似然的期望；
2. M 步：$\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)})$。

典型的终止准则是 $\lVert\hat\theta^{(t+1)} - \hat\theta^{(t)}\rVert < \varepsilon$。$Z$ 连续时求和换成积分。实际中数据为 $x_1, \dots, x_n$，假定独立同分布，对各点求和得 $Q(\theta \mid \theta^{(t)}) = \sum_{i=1}^n\sum_z\mathbb{P}_{Z\mid X}(z \mid x_i, \theta^{(t)})\log \mathbb{P}(x_i, z \mid \theta)$。

**例 6.1.3（两枚硬币，标签隐藏）** 初始化 $\theta_A^{(0)} = 0.6$，$\theta_B^{(0)} = 0.5$，按上面的方法计算五轮的后验概率 $w_{iA} = \mathbb{P}(Z_i = A \mid x_i, \boldsymbol{\theta}^{(0)})$。在 E 步中，它们给出归于每枚硬币的正面、反面期望次数：

| 轮次 $i$ | 结果 | $w_{iA}$ | $w_{iB}$ | 硬币 $A$ 的期望次数 | 硬币 $B$ 的期望次数 |
|---|---|---|---|---|---|
| 1 | 5 正，5 反 | 0.45 | 0.55 | 2.2 正，2.2 反 | 2.8 正，2.8 反 |
| 2 | 9 正，1 反 | 0.80 | 0.20 | 7.2 正，0.8 反 | 1.8 正，0.2 反 |
| 3 | 8 正，2 反 | 0.73 | 0.27 | 5.9 正，1.5 反 | 2.1 正，0.5 反 |
| 4 | 4 正，6 反 | 0.35 | 0.65 | 1.4 正，2.1 反 | 2.6 正，3.9 反 |
| 5 | 7 正，3 反 | 0.65 | 0.35 | 4.5 正，1.9 反 | 2.5 正，1.1 反 |
| 合计 | | | | 21.3 正，8.6 反 | 11.7 正，8.4 反 |

形式上，记第 $i$ 轮 $n_i = 10$ 次中有 $x_i$ 次正面，完全数据的对数似然为（相差先验 $1/2$ 带来的常数）

$$
\log \mathbb{P}(x, Z \mid \boldsymbol{\theta}) = \sum_{i=1}^5\bigl[x_i\log\theta_{Z_i} + (n_i - x_i)\log(1 - \theta_{Z_i})\bigr],
$$
它的条件期望以 $w_{iA}$ 与 $w_{iB} = 1 - w_{iA}$ 为各轮加权：

$$
\begin{aligned}
Q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^{(0)}) &= 0.45\bigl[5\log\theta_A + 5\log(1 - \theta_A)\bigr] + 0.55\bigl[5\log\theta_B + 5\log(1 - \theta_B)\bigr] \\
&\quad + 0.80\bigl[9\log\theta_A + \log(1 - \theta_A)\bigr] + 0.20\bigl[9\log\theta_B + \log(1 - \theta_B)\bigr] + \cdots \\
&= 21.3\log\theta_A + 8.6\log(1 - \theta_A) + 11.7\log\theta_B + 8.4\log(1 - \theta_B),
\end{aligned}
$$
这是一个解耦的目标函数。M 步极大化它，就是以期望次数计算的完全数据 MLE：

$$
\theta_A^{(1)} = \frac{21.3}{21.3 + 8.6} = 0.71, \qquad \theta_B^{(1)} = \frac{11.7}{11.7 + 8.4} = 0.58.
$$
重复这两步，估计收敛到 $(\hat\theta_A, \hat\theta_B) \approx (0.797, 0.520)$，约十次迭代后精确到三位小数。

### 6.1.3. 收敛性

用 $p$ 表示密度，用积分代替求和。隐变量下极大似然的困难在于求和的对数 $\log p(x \mid \theta) = \log\sum_zp(x, z \mid \theta)$。对任意分布 $H(z)$（概率质量函数，$H(z) \ge 0$，$\sum_zH(z) = 1$，且在 $p(x, z \mid \theta) > 0$ 处为正），由凹函数对数的 **Jensen 不等式**，

$$
\log p(x \mid \theta) = \log\sum_zH(z)\frac{p(x, z \mid \theta)}{H(z)} = \log\mathbb{E}_{z\sim H}\left[\frac{p(x, z \mid \theta)}{H(z)}\right] \ge \mathbb{E}_{z\sim H}\left[\log\frac{p(x, z \mid \theta)}{H(z)}\right] = \sum_zH(z)\log\frac{p(x, z \mid \theta)}{H(z)}.
$$
Jensen 不等式取等号当且仅当随机变量为常数，即对所有 $z$ 有 $p(x, z \mid \theta)/H(z) = c$。于是 $\sum_zp(x, z \mid \theta) = c\sum_zH(z) = c$，所以

$$
H(z) = \frac{p(x, z \mid \theta)}{\sum_{z'}p(x, z' \mid \theta)} = p(z \mid x, \theta),
$$
即隐变量的后验分布（连续情形 $h(z) = f(x, z \mid \theta)/\int f(x, z \mid \theta)\,\mathrm{d}z = f_{Z\mid X}(z \mid x, \theta)$）。于是极大化 $\log p(x \mid \theta)$ 变成在当前参数的后验下极大化 $\mathbb{E}_{Z\mid x}\bigl[\log\frac{p(x, Z \mid \theta)}{p(Z \mid x, \theta)}\bigr]$。取 $H(z) = p(z \mid x, \hat\theta^{(t)})$ 定义代理函数

$$
g_t(\theta) = \sum_zp(z \mid x, \hat\theta^{(t)})\log\frac{p(x, z \mid \theta)}{p(z \mid x, \hat\theta^{(t)})} = Q(\theta \mid \hat\theta^{(t)}) - \sum_zp(z \mid x, \hat\theta^{(t)})\log p(z \mid x, \hat\theta^{(t)}),
$$
它对所有 $\theta$ 满足 $g_t(\theta) \le \log p(x \mid \theta)$，且 $g_t(\hat\theta^{(t)}) = \log p(x \mid \hat\theta^{(t)})$。第二项与 $\theta$ 无关，所以极大化 $g_t$ 就是 M 步。

**定理 6.1.1（EM 的上升性质）** 每次 EM 迭代都不会使观测数据的似然减小：$p(x \mid \hat\theta^{(t+1)}) \ge p(x \mid \hat\theta^{(t)})$。

**证明** 由于 $\hat\theta^{(t+1)} = \arg\max_\theta g_t(\theta)$，有 $g_t(\hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t)})$。因此

$$
\log p(x \mid \hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t+1)}) \ge g_t(\hat\theta^{(t)}) = \log p(x \mid \hat\theta^{(t)}). \qquad\square
$$

同一结果也可以围绕对数似然的一个分解来组织，它对任意分布 $q(z)$ 成立：

$$
\begin{aligned}
\ell(\theta) = \log p(x \mid \theta) &= \int q(z)\log p(x \mid \theta)\,\mathrm{d}z = \int q(z)\log\frac{p(x, z \mid \theta)}{p(z \mid x, \theta)}\,\mathrm{d}z = \int q(z)\log\frac{p(x, z \mid \theta)\,q(z)}{p(z \mid x, \theta)\,q(z)}\,\mathrm{d}z \\
&= \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z + \int q(z)\log\frac{q(z)}{p(z \mid x, \theta)}\,\mathrm{d}z \triangleq F(q, \theta) + \operatorname{KL}\bigl(q \,\Vert\, p(\cdot \mid x, \theta)\bigr).
\end{aligned}
$$

**定义 6.1.3（证据下界）** 对隐变量的分布 $q$，泛函

$$
F(q, \theta) = \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z = \mathbb{E}_q\bigl[\log p(x, Z \mid \theta)\bigr] - \mathbb{E}_q\bigl[\log q(Z)\bigr]
$$
称为**证据下界**（ELBO）。

Kullback–Leibler 散度 $\operatorname{KL}(q \Vert p) = \int q(z)\log\frac{q(z)}{p(z)}\,\mathrm{d}z$，又称相对熵，度量一个分布与参照分布的差别。它非负，所以 $F(q, \theta) \le \log p(x \mid \theta)$，即证据：用前面的记号，$F(q, \theta) = \mathbb{E}_q\bigl[\log\frac{p(x, Z \mid \theta)}{q(Z)}\bigr] \le \log\mathbb{E}_q\bigl[\frac{p(x, Z \mid \theta)}{q(Z)}\bigr] = \log p(x \mid \theta)$。

**引理 6.1.1** 对密度 $p$ 与 $q$，$\operatorname{KL}(q \Vert p) \ge 0$，等号当且仅当 $q = p$ 几乎处处成立。

**证明** 利用对所有 $x > 0$ 有 $\ln x \le x - 1$，等号只在 $x = 1$ 时成立：

$$
-\operatorname{KL}(q \Vert p) = \int q(z)\log\frac{p(z)}{q(z)}\,\mathrm{d}z \le \int q(z)\left(\frac{p(z)}{q(z)} - 1\right)\mathrm{d}z = \int p(z)\,\mathrm{d}z - \int q(z)\,\mathrm{d}z \le 0,
$$
其中积分在 $q > 0$ 的集合上进行。$\square$

用这种语言，E 步把 $q$ 设为后验，使 KL 项为零，M 步在 $\theta$ 上极大化 $F$：

$$
\ell(\hat\theta^{(t)}) \overset{\text{E-step}}{=} F(\hat q^{(t+1)}, \hat\theta^{(t)}) \overset{\text{M-step}}{\le} F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \overset{\text{KL} \ge 0}{\le} \ell(\hat\theta^{(t+1)}), \qquad \hat q^{(t+1)} = p(\cdot \mid x, \hat\theta^{(t)}).
$$
上升性质表明，只要能改进完全数据对数似然的期望，EM 就改进了我们对观测变量 $x$ 的模型。EM 迭代地极大化一个在当前值处与对数似然相切的代理函数，即 ELBO，这是极小化–极大化（minorization–maximization）原理的一个实例。

![两成分正态混合（100 个模拟点）中混合比例 alpha 的 EM。实线是观测对数似然；每条虚线是在当前值（圆点）由 E 步得到的下界，它在该处与对数似然相切；M 步跳到下界的极大值点（三角形），新值处的对数似然位于下界之上（箭头）。](./plots/em-lower-bound.py)

因此观测似然单调增加；若 $\ell(\theta)$ 有上界，序列 $\ell(\hat\theta^{(t)})$ 收敛，在温和的正则条件下 $\hat\theta^{(t)}$ 收敛到驻点，可能只是局部极大值点（或鞍点）。与牛顿法相比，EM 更稳定，对初值更宽容：它从不需要 $\ell$ 的 Hesse 矩阵，所以不会因不连续或奇异矩阵而崩溃。

### 6.1.4. 例子

**例 6.1.4（身高分布）** 设男性与女性的身高服从正态分布，$x_m \sim \mathcal{N}(\mu_m, \sigma_m^2)$，$x_f \sim \mathcal{N}(\mu_f, \sigma_f^2)$，$\mu_m, \mu_f$ 未知，$\sigma$ 已知。若随机选 $n_m$ 名男性和 $n_f$ 名女性，记录他们的身高 $\{x_{m,i}\}_{i=1}^{n_m}$ 与 $\{x_{f,i}\}_{i=1}^{n_f}$，似然

$$
L(\mu_m, \mu_f) = (2\pi\sigma_m^2)^{-n_m/2}(2\pi\sigma_f^2)^{-n_f/2}\exp\left\{-\frac{\sum_i(x_{m,i} - \mu_m)^2}{2\sigma_m^2} - \frac{\sum_i(x_{f,i} - \mu_f)^2}{2\sigma_f^2}\right\}
$$
通过解 $\nabla\ell(\mu_m, \mu_f) = \boldsymbol{0}$ 极大化：$\hat\mu_m = \bar x_m$，$\hat\mu_f = \bar x_f$。现在设有 100 条身高记录（50 男 50 女），但没有性别：身高 $X$ 可观测，性别 $Z$ 隐藏，先验 $\mathbb{P}(Z = \mathrm{m}) = 0.5$。初始化 $\mu_m^{(0)}, \mu_f^{(0)}$，记 $\hat\theta^{(t)} = (\hat\mu_m^{(t)}, \hat\mu_f^{(t)})$。E 步计算后验概率

$$
w_i^{(t)} = \mathbb{P}(Z_i = \mathrm{m} \mid x_i; \hat\theta^{(t)}) = \frac{\varphi_m(x_i)}{\varphi_m(x_i) + \varphi_f(x_i)}, \qquad \mathbb{P}(Z_i = \mathrm{f} \mid x_i; \hat\theta^{(t)}) = 1 - w_i^{(t)},
$$
其中 $\varphi_m, \varphi_f$ 是当前均值下的两个正态密度（相等的先验约去），进而得到 $Q(\theta \mid \hat\theta^{(t)})$；M 步极大化 $Q$，得到加权均值，

$$
\hat\mu_m^{(t+1)} = \frac{\sum_iw_i^{(t)}x_i}{\sum_iw_i^{(t)}}, \qquad \hat\mu_f^{(t+1)} = \frac{\sum_i(1 - w_i^{(t)})x_i}{\sum_i(1 - w_i^{(t)})}.
$$
这是隐含成分指示 $Z_i = \boldsymbol{1}_{\{X_i \sim \mathcal{N}_k\}}$ 的正态混合；完整的讨论见 6.3 节。

**例 6.1.5（多项分布）** 197 只动物按多项分布落入四类，各类概率为 $\bigl(\frac12 + \frac\theta4, \frac{1 - \theta}{4}, \frac{1 - \theta}{4}, \frac\theta4\bigr)$，$\theta \in [0, 1]$ 未知；观测计数为 $\boldsymbol{x} = (x_1, x_2, x_3, x_4) = (125, 18, 20, 34)$。估计 $\theta$。观测数据的密度是**多项分布**的密度，

$$
P_X(\boldsymbol{x} \mid \theta) = \frac{n!}{x_1!\,x_2!\,x_3!\,x_4!}\left(\frac12 + \frac\theta4\right)^{x_1}\left(\frac14 - \frac\theta4\right)^{x_2}\left(\frac14 - \frac\theta4\right)^{x_3}\left(\frac\theta4\right)^{x_4},
$$
对数似然为 $\ell(\theta; \boldsymbol{x}) = c + x_1\log(2 + \theta) + (x_2 + x_3)\log(1 - \theta) + x_4\log\theta$。把第一类拆成概率为 $\frac12$ 与 $\frac\theta4$ 的两个格子，我们只观测到它们的和 $x_1 = x_{11} + x_{12}$。完全数据的密度为

$$
P_Y\bigl((x_{11}, x_{12}, x_2, x_3, x_4) \mid \theta\bigr) = \frac{n!}{x_{11}!\,x_{12}!\,x_2!\,x_3!\,x_4!}\left(\frac12\right)^{x_{11}}\left(\frac\theta4\right)^{x_{12}}\left(\frac{1 - \theta}{4}\right)^{x_2}\left(\frac{1 - \theta}{4}\right)^{x_3}\left(\frac\theta4\right)^{x_4},
$$
对数似然 $\ell_c(\theta) \propto (x_{12} + x_4)\log\theta + (x_2 + x_3)\log(1 - \theta)$，是一个二项试验的对数似然。隐变量是 $Z = X_{12}$。给定观测数据，它服从二项分布，

$$
X_{12} \mid \boldsymbol{x} \sim \mathrm{Bin}\left(x_1, \frac{\theta/4}{1/2 + \theta/4}\right) = \mathrm{Bin}\left(x_1, \frac{\theta}{2 + \theta}\right).
$$
在 E 步中，由 $\boldsymbol{x}$ 推断未观测的 $x_{12}$ 的分布并求期望；由于 $\ell_c$ 关于 $x_{12}$ 是线性的，这就是用条件均值代替 $x_{12}$：

$$
Q(\theta \mid \hat\theta^{(t)}) = \bigl(x_{12}^{(t)} + x_4\bigr)\log\theta + (x_2 + x_3)\log(1 - \theta), \qquad x_{12}^{(t)} = \frac{\hat\theta^{(t)}}{2 + \hat\theta^{(t)}}x_1.
$$
M 步关于 $\theta$ 极大化它：

$$
\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)}) = \frac{x_{12}^{(t)} + x_4}{x_{12}^{(t)} + x_2 + x_3 + x_4}.
$$

```r
emfun <- function(th0, maxit = 1000, releps = 1e-09) {
  i <- 0; th1 <- th0; th0 <- th1 + 1
  while ((i != maxit) & (abs(th1 - th0) > releps * abs(th0))) {
    i <- i + 1; th0 <- th1
    x12 <- (125 * th1) / (2 + th1)                  # E-step
    th1 <- (x12 + 34) / (x12 + 34 + 18 + 20)        # M-step
    print(c(tht = th0, thtplus = th1, iter = i))
  }
  return(list(nit = i, theta_hat = th1))
}
emfun(0.5)
```

```text
$nit
[1] 11

$theta_hat
[1] 0.6268215
```

（每次迭代打印的轨迹从略。）三个例子的模式相同：E 步用后验权重或条件期望补全缺失数据，M 步计算完全数据的 MLE。

![遗传连锁多项分布。左：观测对数似然，以及从 theta_0 = 0.05 出发的 EM 迭代，它们单调地爬升到 MLE 0.6268215。右：误差（对数坐标）按几何级数下降，比值为 0.1328，即 MLE 处缺失信息的比例（6.2.3 节）。](./plots/multinomial-em-convergence.py)

关于这一方法的几个问答：

- EM 能保证收敛到全局极大值吗？不能，它可能停在局部极大值点；实践中从多个初值运行。
- EM 什么时候最有用？当缺失数据可以定义为隐变量，且完全数据的 MLE 容易求得时。引入隐变量或者是为了简化似然函数（更常见的情形，如例 6.1.5），或者是为了处理真实的缺失数据。
- EM 什么时候不太有用？当 E 步很慢时，例如数据维数很高或缺失数据比例很大；缺失信息的比例大也会使 EM 收敛很慢。

## 6.2. EM 算法的扩展

### 6.2.1. 广义 EM

由分解 $\log p(x \mid \theta) = F(q, \theta) + \operatorname{KL}\bigl(q \Vert p(\cdot \mid x, \theta)\bigr)$，当 $q(z) = p(z \mid x, \hat\theta^{(t)})$ 容易得到时，EM 计算并极大化 $F(q, \theta)$。EM 其实是 $F$ 上的坐标上升：交替地在 $q$ 和 $\theta$ 上极大化。

**定义 6.2.1（广义 EM）** **广义 EM 算法**（GEM）交替进行

1. E 步：$\hat q^{(t+1)} = \arg\min_q\operatorname{KL}\bigl(q \Vert p(\cdot \mid x, \hat\theta^{(t)})\bigr) = \arg\max_qF(q, \hat\theta^{(t)})$；
2. M 步：选 $\hat\theta^{(t+1)}$ 使 $F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t)})$，例如 $\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t+1)}, \theta) = \arg\max_\theta\int\hat q^{(t+1)}(z)\log p(x, z \mid \theta)\,\mathrm{d}z$。

于是 M 步不必极大化 $Q$，只需使它增加，$Q(\hat\theta^{(t+1)} \mid \hat\theta^{(t)}) \ge Q(\hat\theta^{(t)} \mid \hat\theta^{(t)})$；当 $Q$ 没有闭式极大值点、M 步本身需要数值优化（比如一步牛顿法）时，这很有用。定理 6.1.1 的证明照样成立：$\ell(\hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t+1)}) \ge F(\hat q^{(t+1)}, \hat\theta^{(t)}) = \ell(\hat\theta^{(t)})$。

**注 6.2.1** 设极大值点唯一。两步的顺序能否交换，即先 $\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t)}, \theta)$，再 $\hat q^{(t+1)} = \arg\max_qF(q, \hat\theta^{(t+1)})$？可以：交替极大化产生同样的点对序列，交换顺序只是让交替从初始的 $q$ 而不是初始的 $\theta$ 开始。

若 $q$ 难以得到，或 $F(q, \theta)$ 难以计算，就转向变分 EM（见下文）或 Monte Carlo EM，后者用 $Z$ 的模拟值的平均来近似 E 步中的期望。

### 6.2.2. 变分推断

当后验 $p(z \mid x, \theta)$ 难以处理时，我们无法使 KL 项为零，但仍可在一个受限的、可处理的分布族上极大化 ELBO；这时间隙 $\operatorname{KL}(q \Vert p)$ 度量近似的质量。

**定义 6.2.2（平均场近似）** **平均场近似**假设在给定 $x$ 时所有隐变量相互独立，用因子分解的分布近似后验：

$$
q(z) = \prod_iq_i(z_i).
$$

这一假设使我们能单独计算每个隐变量的更新，它在许多问题中都很成功。固定 $j$，把 $F$ 看作 $q_j$ 的函数。在 $q$ 因子分解时，

$$
F(q, \theta) = \int\prod_iq_i(z_i)\log p(x, z \mid \theta)\,\mathrm{d}z - \sum_i\int q_i(z_i)\log q_i(z_i)\,\mathrm{d}z_i.
$$
第一项为 $\int q_j(z_j)\,\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\mathrm{d}z_j$，其中 $\mathbb{E}_{-j}$ 表示在 $\prod_{i\ne j}q_i$ 下对 $z_{-j} = (z_i)_{i\ne j}$ 求期望。记

$$
q_j^*(z_j) = \frac1C\exp\Bigl\{\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\Bigr\}, \qquad C = \int\exp\Bigl\{\mathbb{E}_{-j}\bigl[\log p(x, z_{-j}, z_j \mid \theta)\bigr]\Bigr\}\mathrm{d}z_j.
$$
则

$$
F(q, \theta) = -\operatorname{KL}(q_j \Vert q_j^*) + \sum_{i\ne j}H(q_i) + \log C,
$$
其中 $H(q_i) = -\int q_i\log q_i$ 是熵，$C$ 与 $q_j$ 无关。由于 KL 散度非负，ELBO 关于 $q_j$ 在 $\operatorname{KL}(q_j \Vert q_j^*) = 0$ 时取极大，即 $q_j = q_j^*$。

**定义 6.2.3（变分 EM）** **变分 EM 算法**（VBEM，变分贝叶斯 EM）用 ELBO 的平均场极大化代替精确的 E 步：

1. E 步：对所有 $j$ 计算 $q_j^*(z_j) = \frac1C\exp\bigl\{\mathbb{E}_{-j}[\log p(x, z_{-j}, z_j \mid \theta)]\bigr\}$，令 $\hat q^{(t+1)}(z) = \prod_jq_j^*(z_j)$；
2. M 步：$\hat\theta^{(t+1)} = \arg\max_\theta F(\hat q^{(t+1)}, \theta)$。

在完全贝叶斯的版本中，$\theta$ 本身也被当作带**先验分布**的隐变量，在 $q$ 中有自己的因子。由于每个 $q_j^*$ 依赖于其他因子，E 步用坐标上升计算：

**算法 6.2.1（坐标上升变分推断）** 输入：模型 $p(x, z)$ 与数据集 $x$。输出：平均场变分密度 $q(z) = \prod_{j=1}^mq_j(z_j)$ 与 ELBO $F(q, \theta)$。

1. 初始化 $q_j(z_j)$（$j = 1, \dots, m$），例如取相应的边缘分布。
2. 当 ELBO 尚未收敛，即 $\lvert F(q^{(k+1)}, \theta) - F(q^{(k)}, \theta)\rvert \ge \varepsilon$ 时：对 $j = 1, \dots, m$ 令 $q_j(z_j) = q_j^*(z_j) = \frac1C\exp\bigl\{\mathbb{E}_{-j}[\log p(x, z_{-j}, z_j \mid \theta)]\bigr\}$；然后计算 $q(z) = \prod_jq_j(z_j)$ 与
   $$
   F(q, \theta) = \int q(z)\log\frac{p(x, z \mid \theta)}{q(z)}\,\mathrm{d}z = \mathbb{E}_q\bigl[\log p(x, z)\bigr] - \mathbb{E}_q\bigl[\log q(z)\bigr].
   $$
3. 返回 $q(z)$ 与 $F(q, \theta)$。

由于每次更新只沿一个坐标（一个因子 $q_j$）移动，ELBO 在函数空间中一步一步地爬升。

**例 6.2.1（两个来源）** 一维观测 $x$（比如事件发生的位置）来自中心已知为 $\mu_1$ 与 $\mu_2$ 的两个来源。对某个具体观测 $x$，它是哪个来源产生的？隐变量 $z = (z_1, z_2)$ 是独热编码：第一个来源为 $z = (1, 0)$，第二个为 $(0, 1)$，我们要求近似后验 $q(z_1, z_2)$。在真实后验中，$z_1$ 与 $z_2$ 互斥且高度相关（$z_1 + z_2 = 1$），但平均场近似假设 $q(z_1, z_2) = q_1(z_1)q_2(z_2)$，$z_1, z_2 \in \{0, 1\}$。设化简后联合对数概率具有指数族中常见的交叉项结构，

$$
\log p(x, z_1, z_2 \mid \theta) = 2.2z_1 + 2.2z_2 - 4.5z_1z_2 + \text{const}.
$$
初始化 $q_2 = \mathrm{Ber}(0.5)$，即 $\mathbb{E}_2[z_2] = 0.5$。

- 更新 $q_1$：把 $z_2$ 换成它的当前期望，$\mathbb{E}_{-1}[\log p] = 2.2z_1 + 2.2(0.5) - 4.5z_1(0.5) + \text{const} = -0.05z_1 + \text{const}$，所以 $q_1^*(z_1) \propto \exp\{-0.05z_1\}$：$q_1^*(0) \propto 1$，$q_1^*(1) \propto \mathrm{e}^{-0.05} \approx 0.9512$，$C = 1.9512$，$q_1(1) = 0.9512/1.9512 \approx 0.4875$，$\mathbb{E}_1[z_1] \approx 0.4875$。
- 更新 $q_2$：$\mathbb{E}_{-2}[\log p] = (2.2 - 4.5\times0.4875)z_2 + \text{const} \approx 0.00625z_2 + \text{const}$，所以 $q_2^*(1) \propto \mathrm{e}^{0.00625} \approx 1.0063$，$C = 2.0063$，$q_2(1) \approx 0.5016$。

第一轮之后 $q_1(1) = 0.4875$，$q_2(1) = 0.5016$，四个联合状态的概率为 $q(0, 0) \approx 0.2554$，$q(1, 0) \approx 0.2430$，$q(0, 1) \approx 0.2571$，$q(1, 1) \approx 0.2445$：从均衡值 $0.5$ 出发，四个状态仍几乎同样可能，不过排斥项 $-4.5z_1z_2$ 已开始把 $q(1, 1)$ 压到 $1/4$ 以下。ELBO 是能量项的期望加上熵：

$$
\mathbb{E}_q[\log p] = 2.2q_1(1) + 2.2q_2(1) - 4.5q_1(1)q_2(1) = 1.0725 + 1.1035 - 1.1004 = 1.0756,
$$
$$
H(q_1) = -\bigl(0.4875\log0.4875 + 0.5125\log0.5125\bigr) \approx 0.6929, \qquad H(q_2) \approx 0.6931,
$$
所以 $F^{(1)} = 1.0756 + 1.3860 = 2.4616$（相差一个常数）。算法随后带着更新后的 $q_1, q_2$ 回到 while 循环的开头，计算 $F^{(2)}$，只要 $F^{(k+1)} - F^{(k)} \ge \varepsilon$ 就继续。继续迭代，各因子离开对称的起点，收敛到 $q_1(1) \approx 0.220$，$q_2(1) \approx 0.770$，$F \approx 2.482$。不可能状态的概率降到 $q(1, 1) \approx 0.169$，但仍远高于它的精确后验值 $0.045$（由四个未归一化权重 $\mathrm{e}^0, \mathrm{e}^{2.2}, \mathrm{e}^{2.2}, \mathrm{e}^{-0.1}$ 算出），$F$ 也一直低于 $\log p(x) = \log(1 + 2\mathrm{e}^{2.2} + \mathrm{e}^{-0.1}) \approx 2.993$：因子分解的 $q$ 无法表达"$z_1, z_2$ 恰有一个为 1"，KL 间隙度量了这一损失。

总结起来：当后验 $p$ 无法精确计算时，我们寻找最接近的近似分布 $q$（广义 EM）；优化是在函数 $q$ 上进行的，空间太大，于是引入各因子独立的平均场假设（VBEM）；坐标上升轮流更新各因子直至收敛。

**例 6.2.2（不含数据的玩具例子）** 用 $q(z) = q_1(z_1)q_2(z_2)$ 近似二元正态 $p(z) = \mathcal{N}(z \mid \boldsymbol{\mu}, \Lambda^{-1})$，均值 $\boldsymbol{\mu} = (\mu_1, \mu_2)^{\mathsf T}$，精度矩阵 $\Lambda = \begin{bmatrix}\Lambda_{11} & \Lambda_{12} \\ \Lambda_{21} & \Lambda_{22}\end{bmatrix}$。则

$$
\begin{aligned}
\log q_1^*(z_1) &= \mathbb{E}_{q_2(z_2)}\bigl[\log p(z)\bigr] + \text{const} = \mathbb{E}_{q_2(z_2)}\left[-\frac12(z_1 - \mu_1)^2\Lambda_{11} - (z_1 - \mu_1)\Lambda_{12}(z_2 - \mu_2)\right] + \text{const} \\
&= -\frac12z_1^2\Lambda_{11} + z_1\mu_1\Lambda_{11} - z_1\Lambda_{12}\bigl(\mathbb{E}[z_2] - \mu_2\bigr) + \text{const}.
\end{aligned}
$$
配方得 $q_1^*(z_1) = \mathcal{N}(z_1 \mid m_1, \Lambda_{11}^{-1})$，其中 $\mathbb{E}[z_1] \triangleq m_1 = \mu_1 - \Lambda_{11}^{-1}\Lambda_{12}(\mathbb{E}[z_2] - \mu_2)$；由对称性 $q_2^*(z_2) = \mathcal{N}(z_2 \mid m_2, \Lambda_{22}^{-1})$，$m_2 = \mu_2 - \Lambda_{22}^{-1}\Lambda_{21}(\mathbb{E}[z_1] - \mu_1)$。这两个方程的解是 $\mathbb{E}[z_1] = \mu_1$，$\mathbb{E}[z_2] = \mu_2$，于是得到闭式

$$
q^*(z) = q_1^*(z_1)q_2^*(z_2) = \mathcal{N}(z_1 \mid \mu_1, \Lambda_{11}^{-1})\,\mathcal{N}(z_2 \mid \mu_2, \Lambda_{22}^{-1}).
$$
均值是精确的，但只要 $z_1$ 与 $z_2$ 相关，方差 $\Lambda_{11}^{-1} \le (\Lambda^{-1})_{11}$ 就偏小：平均场近似倾向于低估后验的不确定性。

### 6.2.3. Louis 加速

EM 可以看作不动点迭代。设 $M(\theta)$ 是一次 E 步与 M 步合起来的映射，于是 $\theta_{n+1} = M(\theta_n)$。在标准的正则条件下，MLE $\theta^*$ 是这个映射的不动点，$\theta^* = M(\theta^*)$。在最优点附近作一阶 Taylor 展开，

$$
M(\theta_n) \approx M(\theta^*) + \nabla M(\theta^*)(\theta_n - \theta^*) \quad\Longrightarrow\quad \theta_{n+1} - \theta^* \approx J(\theta^*)(\theta_n - \theta^*),
$$
其中 $J(\theta) = \nabla M(\theta)$ 是 EM 映射的 Jacobi 矩阵。它可以用三个信息矩阵表示。

**定义 6.2.4（完全信息、观测信息与缺失信息）** 对模型 $p(x, z \mid \theta)$ 与观测数据 $x$，定义观测信息 $I_X(\theta) = -\nabla^2\log p(x \mid \theta)$，完全信息 $I_{Z,X}(\theta) = \mathbb{E}_{Z\mid x, \theta}\bigl[-\nabla^2\log p(x, Z \mid \theta)\bigr]$，缺失信息 $I_{Z\mid X}(\theta) = \mathbb{E}_{Z\mid x, \theta}\bigl[-\nabla^2\log p(Z \mid x, \theta)\bigr]$。**缺失信息原理**（Orchard 与 Woodbury，1972；Louis，1982）指出

$$
I_X(\theta) = I_{Z,X}(\theta) - I_{Z\mid X}(\theta):
$$
观测信息等于完全信息减去缺失信息。

把 $\log p(x \mid \theta) = \log p(x, z \mid \theta) - \log p(z \mid x, \theta)$ 对 $\theta$ 求两次导数，再对 $Z \sim p(\cdot \mid x, \theta)$ 取平均即得；左边与 $z$ 无关。

**定理 6.2.1（EM 的收敛速率）** 设 $\theta^*$ 是 $\ell$ 的局部极大值点，$I_X(\theta^*) \succ 0$，M 步的极大值点在内部，$Q$ 二阶可微。则

$$
J(\theta^*) = I_{Z,X}(\theta^*)^{-1}I_{Z\mid X}(\theta^*).
$$
它的特征值位于 $[0, 1)$，所以 EM 在 $\theta^*$ 附近线性收敛，谱半径 $\rho\bigl(J(\theta^*)\bigr) = \max\lvert\lambda_{J(\theta^*)}\rvert$，即缺失信息的最大比例，就是控制误差缩小快慢的速率。

**证明**（概要）M 步意味着对所有 $\theta'$ 有 $\nabla_\theta Q\bigl(M(\theta') \mid \theta'\bigr) = \boldsymbol{0}$。在 $\theta' = \theta^* = M(\theta^*)$ 处对 $\theta'$ 求导，

$$
\nabla^{2}_{\theta\theta}Q(\theta^* \mid \theta^*)\,\nabla M(\theta^*) + \nabla^{2}_{\theta\theta'}Q(\theta^* \mid \theta^*) = O.
$$
按定义 $\nabla^2_{\theta\theta}Q(\theta^* \mid \theta^*) = -I_{Z,X}(\theta^*)$。把 $\log p(x, Z \mid \theta)$ 写成 $\log p(x \mid \theta) + \log p(Z \mid x, \theta)$，混合导数就是 $\theta = \theta' = \theta^*$ 处的 $\nabla_{\theta'}\mathbb{E}_{Z\mid x, \theta'}\bigl[\nabla_\theta\log p(Z \mid x, \theta)\bigr]$，由条件密度的信息恒等式它等于 $\mathbb{E}\bigl[\nabla\log p(Z \mid x, \theta^*)\,\nabla\log p(Z \mid x, \theta^*)^{\mathsf T}\bigr] = I_{Z\mid X}(\theta^*)$。因此 $\nabla M(\theta^*) = I_{Z,X}^{-1}I_{Z\mid X}$。这个矩阵相似于 $I_{Z,X}^{-1/2}I_{Z\mid X}I_{Z,X}^{-1/2}$，后者的特征值位于 $[0, 1)$，因为 $O \preceq I_{Z\mid X}$ 且 $I_{Z,X} - I_{Z\mid X} = I_X \succ 0$。$\square$

这里 $\theta$ 是列向量。若像 Dempster、Laird 与 Rubin（1977）那样用行向量，Jacobi 矩阵以转置形式 $I_{Z\mid X}I_{Z,X}^{-1}$ 出现，特征值相同。在例 6.1.5 中，$I_{Z,X}(\hat\theta) = 435.32$，$I_X(\hat\theta) = 377.52$，$I_{Z\mid X}(\hat\theta) = 57.80$，所以速率为 $57.80/435.32 = 0.1328$，恰是那里图中看到的斜率；$\hat\theta$ 的标准误为 $I_X(\hat\theta)^{-1/2} = 0.0515$。

几何式的衰减启发我们外推。把误差递推式级联 $n$ 次，得 $\theta_{n+j} - \theta^* \approx J^n(\theta^*)(\theta_j - \theta^*)$，所以对足够大的基准迭代 $j$，步长也按几何级数衰减，$\theta_{n+j+1} - \theta_{n+j} \approx J^n(\theta^*)(\theta_{j+1} - \theta_j)$。把 $\theta^*$ 写成伸缩和，就能不经无穷次迭代而外推出最终的最优点：

$$
\theta^* = \theta_j + \sum_{k=1}^\infty(\theta_{k+j} - \theta_{k+j-1}) \approx \theta_j + \sum_{k=0}^\infty J^k(\theta^*)(\theta_{j+1} - \theta_j) = \theta_j + \bigl[I - J(\theta^*)\bigr]^{-1}(\theta_{j+1} - \theta_j).
$$
几何级数收敛，因为 $J$ 的特征值的绝对值都小于 1。由缺失信息原理，$I - J(\theta) = I_{Z,X}(\theta)^{-1}\bigl(I_{Z,X}(\theta) - I_{Z\mid X}(\theta)\bigr) = I_{Z,X}(\theta)^{-1}I_X(\theta)$。

**算法 6.2.2（Louis 加速）** 给定当前估计 $\theta_n$：

1. 用标准 EM 算法的一步计算 $M(\theta_n)$；
2. 计算 $\bigl[I - J(\theta_n)\bigr]^{-1} = I_X(\theta_n)^{-1}I_{Z,X}(\theta_n)$；
3. 令 $\theta_{n+1} = \theta_n + \bigl[I - J(\theta_n)\bigr]^{-1}\bigl(M(\theta_n) - \theta_n\bigr)$。

相对于一次 EM 迭代，额外的代价在于计算并求逆 $I_X(\theta_n)$。收敛只在最优点 $\theta^*$ 的某个邻域内有保证，而这个邻域的大小和形状在应用中通常未知。缺失比例低时，$[I - J(\theta_n)]^{-1} \approx I$，序列与通常的 EM 序列相似；缺失比例高时，$[I - J(\theta_n)]^{-1}$ 很大，通常的 EM 步被大幅修正。

**注 6.2.2** 在 $\theta^*$ 附近，EM 步近似是一个缩放的梯度步：由于 $\nabla_\theta Q(\theta \mid \theta_n)$ 在 $\theta = \theta_n$ 处等于观测得分 $\nabla\ell(\theta_n)$，对 $Q$ 作一步牛顿法得 $M(\theta_n) - \theta_n \approx I_{Z,X}(\theta_n)^{-1}\nabla\ell(\theta_n)$。因此加速步近似为 $\theta_n + I_X(\theta_n)^{-1}\nabla\ell(\theta_n)$，即对 $\ell$ 的牛顿法（[3.5.5](/3.5.5)）。Louis 加速用 EM 的稳定性换取牛顿法的速度，这既解释了它快速的局部收敛，也解释了为什么要在最优点附近启动它。

## 6.3. 应用：混合模型中的参数估计

### 6.3.1. 混合模型

混合模型应用广泛：机器学习、计算机视觉、自然语言处理、数量遗传学中的混合模型、心理测量学中的项目反应理论、医学图像重建和结构工程。它们用于数据聚类，用于分解叠加的信号（**高斯混合模型**、隐 Markov 模型），用于估计复合 Dirichlet 分布等复合分布的参数，以及寻找若干固定模型的最佳组合。分类从带标签的数据中学习规则，而聚类在没有标签时寻找分组（[3.4.11](/3.4.11)）；高斯混合的 EM 是 **k 均值聚类**的软版本。

均值 $\mu$、方差 $\sigma^2$ 的正态密度为 $\varphi_{\mu,\sigma}(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\bigl\{-\frac{(x - \mu)^2}{2\sigma^2}\bigr\}$，$d$ 维时为 $\varphi_{\boldsymbol{\mu},\Sigma}(\boldsymbol{x}) = (2\pi)^{-d/2}\lvert\Sigma\rvert^{-1/2}\exp\bigl\{-\frac12(\boldsymbol{x} - \boldsymbol{\mu})^{\mathsf T}\Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu})\bigr\}$。组合 $m$ 个基本密度可以刻画复杂的数据分布。

**定义 6.3.1（有限混合模型）** 有 $m$ 个成分的**有限混合模型**的密度为

$$
p_\Theta(x) = \sum_{i=1}^m\alpha_i\varphi_{\theta_i}(x), \qquad \alpha_i \ge 0, \quad \sum_{i=1}^m\alpha_i = 1,
$$
参数为 $\Theta = (\alpha_1, \dots, \alpha_m, \theta_1, \dots, \theta_m)$，其中 $\alpha_i$ 是混合比例，$\varphi_{\theta_i}$ 是成分密度。若每个成分都是正态的，$\theta_k = (\mu_k, \sigma_k)$（或 $(\boldsymbol{\mu}_k, \Sigma_k)$），它就是高斯混合模型。

从混合分布抽样时，先以 $\mathbb{P}(z = k) = \alpha_k$ 抽成分标签 $z$，再从 $\varphi_{\theta_z}$ 抽 $x$。

### 6.3.2. 高斯混合的极大似然

$n$ 个观测点 $x_1, \dots, x_n$ 的对数似然为

$$
\ell(\Theta; \boldsymbol{x}) = \sum_{j=1}^n\log\sum_{i=1}^m\alpha_i\varphi_{\theta_i}(x_j),
$$
是求和的对数，难以解析地优化。改为引入 $n$ 个隐藏标签 $z_1, \dots, z_n$：$z_i = k$ 表示 $x_i$ 由第 $k$ 个高斯分布产生，$k \in \{1, \dots, m\}$，于是

$$
p_\Theta(x_i \mid z_i = k) = \varphi_{\theta_k}(x_i), \qquad p_\Theta(x_i, z_i = k) = \alpha_k\varphi_{\theta_k}(x_i).
$$

**算法 6.3.1（高斯混合的 EM）** 取参数的初始猜测 $\hat\Theta$，迭代直至收敛：

1. E 步：计算给定观测时 $z_i$ 的后验分布，
   $$
   \Lambda_{i,k} = p_{\hat\Theta}(z_i = k \mid x_i) = \frac{\hat\alpha_k\varphi_{\hat\theta_k}(x_i)}{p_{\hat\Theta}(x_i)} = \frac{\hat\alpha_k\varphi_{\hat\theta_k}(x_i)}{\sum_{j=1}^m\hat\alpha_j\varphi_{\hat\theta_j}(x_i)},
   $$
   从而 $Q(\Theta \mid \hat\Theta) = \sum_{i=1}^n\sum_{k=1}^m\Lambda_{i,k}\log\bigl(\alpha_k\varphi_{\theta_k}(x_i)\bigr)$；
2. M 步：对每个高斯成分 $k = 1, \dots, m$ 更新 $\alpha_k, \mu_k, \sigma_k$：
   $$
   \hat\alpha_k = \frac1n\sum_{i=1}^n\Lambda_{i,k}, \qquad \hat\mu_k = \frac{\sum_{i=1}^n\Lambda_{i,k}x_i}{\sum_{i=1}^n\Lambda_{i,k}}, \qquad \hat\sigma_k^2 = \frac{\sum_{i=1}^n\Lambda_{i,k}(x_i - \hat\mu_k)^2}{\sum_{i=1}^n\Lambda_{i,k}};
   $$
   对一般协方差的 $d$ 维数据，$\hat\Sigma_k = \frac{\sum_i\Lambda_{i,k}(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_k)(\boldsymbol{x}_i - \hat{\boldsymbol{\mu}}_k)^{\mathsf T}}{\sum_i\Lambda_{i,k}}$。

后验概率 $\Lambda_{i,k}$ 常称为成分 $k$ 对观测 $i$ 的责任度（Responsibility）。M 步公式是完全数据 MLE 的加权版本。对比例，在 $\sum_k\alpha_k = 1$ 下极大化 $\sum_k\bigl(\sum_i\Lambda_{i,k}\bigr)\log\alpha_k$：用 Lagrange 乘子，对所有 $k$ 有 $\sum_i\Lambda_{i,k}/\alpha_k = \lambda$，对 $k$ 求和得 $\lambda = n$。对 $\mu_k$ 与 $\sigma_k^2$，$Q$ 中涉及成分 $k$ 的项是权重为 $\Lambda_{i,k}$ 的正态对数似然，由加权均值和加权方差极大化。EM 是软聚类（$x_i$ 以概率 $\Lambda_{i,k}$ 属于每个成分），k 均值是硬聚类；成分为公共方差 $\sigma^2 \to 0$ 的球形分布时，EM 退化为 k 均值。

若高斯成分数 $m$ 未知，怎样估计它？选使 $\ell(\Theta \mid x)$ 尽可能大的 $m$ 是行不通的：$m = n$ 时每个数据点有自己的来源，完美拟合数据，但对新数据点可能效果很差。（事实上，方差自由时似然在 $m \ge 2$ 时就已无界：一个以某个观测为中心、$\sigma_k \to 0$ 的成分使 $\ell \to \infty$。因此高斯混合的 MLE 被理解为参数空间内部一个表现良好的局部极大值点。）可以把数据分为训练集 $T$ 和验证集 $V$，对每个 $m$ 在 $T$ 上拟合参数，在 $V$ 上计算似然，不过这样仍可能偏向大的 $m$。也可以用**贝叶斯信息准则**或**赤池信息准则**（[3.4.11](/3.4.11)），它们在拟合良好的模型中选最简单的：记自由参数个数为 $p$，极大化 $\ln L - \frac p2\ln n$（即极小化 $\mathrm{BIC} = -2\ln L + p\ln n$），或极小化 $\mathrm{AIC} = 2p - 2\ln L$。

### 6.3.3. 两成分正态混合

以概率 $\alpha = 0.4$ 取 $\mathcal{N}(1, 2^2)$、以概率 $0.6$ 取 $\mathcal{N}(4, 1)$ 生成混合数据：

```r
mu1 <- 1
s1 <- 2
mu2 <- 4
s2 <- 1
a0 <- 0.4
n <- 100
set.seed(5288)
z <- rbinom(n, 1, a0)
x <- rnorm(n, mu1 * z + mu2 * (1 - z),
           s1 * z + (1 - z) * s2)
hist(x)
rug(x)
```

若 $\mu_1, \sigma_1, \mu_2$ 与 $\sigma_2$ 已知，唯一的参数是 $\alpha$，可以把观测数据的对数似然画成 $\alpha$ 的函数并直接极大化；这个"神谕"估计是比较的金标准：

```r
f <- function(x, a) {
  a * dnorm(x, mu1, s1) + (1 - a) * dnorm(x, mu2, s2)
}
loglike <- Vectorize(
  function(a) {
    sum(log(f(x, a)))
  }
)
curve(loglike, 0.01, 0.95, n = 200, xlab = expression(alpha))
op <- optimize(loglike, c(0.01, 0.95), maximum = TRUE, tol = 1e-8)
op$maximum
```

```text
[1] 0.481365
```

设 $z_i \sim \mathrm{Ber}(\alpha)$：$z_i = 1$ 时 $x_i$ 来自总体 1，$z_i = 0$ 时来自总体 2。观测数据与缺失数据的联合密度，即完全数据密度，为

$$
p_\Theta(x_i, z_i) = \bigl[\alpha\varphi_{\theta_1}(x_i)\bigr]^{z_i}\bigl[(1 - \alpha)\varphi_{\theta_2}(x_i)\bigr]^{1 - z_i},
$$
对缺失数据求和，$\sum_{z_i=0}^1p_\Theta(x_i, z_i) = \alpha\varphi_{\theta_1}(x_i) + (1 - \alpha)\varphi_{\theta_2}(x_i) = p_\Theta(x_i)$，得到观测数据密度。通常的 EM 步为 $\hat\alpha = \frac1n\sum_i\Lambda_{i,1}$。加速版本需要 $I_X$，即观测对数似然 $\sum_i\log p_\Theta(x_i)$ 的二阶导数的相反数，以及 $I_{Z,X}$，即完全数据对数似然的期望 $\sum_i\bigl[\Lambda_{i,1}\log\alpha + (1 - \Lambda_{i,1})\log(1 - \alpha)\bigr]$ 的二阶导数的相反数；代码用 `deriv3` 做符号求导计算这两者，加速更新为 $\theta^* = \theta_n + I_{Z,X}(\theta_n)I_X(\theta_n)^{-1}(\theta_{n+1} - \theta_n)$（一维时因子的顺序无关紧要）。

```r
# usual EM
Lambda <- function(a, x, mu1, mu2, s1, s2) {
  a * dnorm(x, mu1, s1) / (a * dnorm(x, mu1, s1) +
                             (1 - a) * (dnorm(x, mu2, s2)))
}
M <- function(a0) {
  th.est <- Lambda(a0, x, mu1, mu2, s1, s2)
  mean(th.est)
}
# accelerated version
Mstar <- function(a0) {
  a1 <- M(a0)
  thhat <- Lambda(a0, x, mu1, mu2, s1, s2)
  a0 + (Ixz(a0) / Ix(a0)) * (a1 - a0)
}
Ix <- local({
  d <- deriv3(~ log(a * dnorm(x, mu1, s1) + (1 - a) * dnorm(x, mu2, s2)),
              "a", function.arg = TRUE)
  function(a) {
    H <- attr(d(a), "hessian")
    sum(H)   # sum over all data points
  }
})
Ixz <- local({
  d <- deriv3(~ thhat * log(a) + (1 - thhat) * log(1 - a),
              "a", function.arg = TRUE)
  function(a) {
    H <- attr(d(a), "hessian")
    sum(H)
  }
})
a0 <- 0.1
a0star <- 0.1
iter <- 6
EM <- numeric(iter)
Accel <- numeric(iter)
for (i in 1:iter) {
  thhat <- Lambda(a0, x, mu1, mu2, s1, s2)
  a1 <- M(a0)
  a1star <- Mstar(a0star)
  EM[i] <- a1
  Accel[i] <- a1star
  a0 <- a1
  a0star <- a1star
}
results <- data.frame(EM = EM, Accel = Accel,
                      errorEM = abs(EM - op$maximum),
                      errorAccel = abs(Accel - op$maximum))
format(results, scientific = FALSE)
```

```text
         EM     Accel     errorEM         errorAccel
1 0.3248608 0.3767740 0.156504282 0.1045910550708599
2 0.4204913 0.4733833 0.060873761 0.0079816884231566
3 0.4569536 0.4812987 0.024411415 0.0000662878894976
4 0.4714032 0.4813649 0.009961842 0.0000001006214514
5 0.4772680 0.4813650 0.004097023 0.0000000000426954
6 0.4796745 0.4813650 0.001690562 0.0000000001042916
```

加速方法的误差比标准方法下降得快得多：到第四次迭代它已接近 MLE $0.481365$，而标准 EM 六次迭代后还没有到达；后者的误差每步大约按 $0.41$ 的固定因子缩小。（`errorAccel` 的最后几位反映了参照值 `op$maximum` 的容差 `1e-8`。）

**注 6.3.1** 这段代码中函数 `Ixz` 从全局环境读取变量 `thhat`，而循环在那里存放的是标准 EM 迭代值 `a0` 处的责任度，不是 `a0star` 处的：R 在函数定义所在的环境中查找自由变量，所以 `Mstar` 内部对 `thhat` 的局部赋值从未被看到。因此加速序列使用的完全信息是在错误的点上计算的；它仍然收敛，因为两个序列趋于同一个 MLE。正确的做法是在加速迭代值处计算责任度，例如把它作为参数传入，或使用闭式 $I_X(\alpha) = \sum_i\frac{(\varphi_1(x_i) - \varphi_2(x_i))^2}{p_\Theta(x_i)^2}$ 与 $I_{Z,X}(\alpha) = \sum_i\bigl[\frac{\Lambda_{i,1}}{\alpha^2} + \frac{1 - \Lambda_{i,1}}{(1 - \alpha)^2}\bigr]$，如下图下方的 R 代码所示。

![两成分混合，数据按同样的设计由另一个随机数发生器模拟（因此估计值与上面的 R 输出不同）。左：100 个点的直方图、拟合的混合密度及其两个加权成分。右：从 alpha_0 = 0.1 出发的标准 EM 与 Louis 加速的误差（对数坐标）；EM 线性收敛，加速迭代四步内达到约 1e-10 的精度。](./plots/mixture-em-louis.py)

## 小结

- 当观测似然难以优化、但引入隐变量 $Z$ 后变得简单时，EM 计算 MLE；观测数据 $X$，隐变量 $Z$，完全数据 $Y = (X, Z)$。
- E 步：由 $\hat\theta^{(t)}$ 计算后验 $p(Z \mid X, \hat\theta^{(t)})$ 与 $Q(\theta \mid \hat\theta^{(t)}) = \mathbb{E}_{Z\mid X, \hat\theta^{(t)}}\log p(X, Z \mid \theta)$。M 步：$\hat\theta^{(t+1)} = \arg\max_\theta Q(\theta \mid \hat\theta^{(t)})$。在例题中，步骤是：写出完全数据的似然，确定隐变量，计算它的后验，构造 $Q$，推导更新公式（并能从给定的初值手工迭代）。
- 收敛性：由 Jensen 不等式，或由 $\log p(x \mid \theta) = F(q, \theta) + \operatorname{KL}(q \Vert p) \ge F(q, \theta)$，似然单调增加；EM 收敛到驻点，可能是局部极大值点，通常比牛顿法稳定。
- 速率：EM 是不动点迭代，线性收敛，速率等于缺失信息的最大比例，$J = I_{Z,X}^{-1}I_{Z\mid X}$，来自缺失信息原理 $I_X = I_{Z,X} - I_{Z\mid X}$。
- 扩展：GEM 只要求 M 步使 $Q$ 增加（ELBO 上的坐标上升）；E 步难以处理时，VBEM 用平均场因子分解；Louis 加速用 $(I - J)^{-1} = I_X^{-1}I_{Z,X}$ 外推，本质上是一步牛顿法。
- 高斯混合：E 步计算责任度 $\Lambda_{ik}$，M 步计算加权的比例、均值与方差；EM 是软聚类，k 均值是硬聚类；成分数由验证集或 BIC/AIC 选取。
- 优点：易于实现，存储小，每次迭代代价低，似然有界时单调收敛。缺点：线性（可能很慢）收敛，只能到局部最优，E 步的后验或 M 步的精确极大值点可能难以求得。这一方法由 Dempster、Laird 与 Rubin（1977）的经典论文命名并阐明。
