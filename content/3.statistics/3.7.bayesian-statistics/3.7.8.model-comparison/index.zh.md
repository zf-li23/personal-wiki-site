---
title: 模型比较
description: 预测精度（均方误差、对数预测密度、elpd、elppd 与样本内的 lppd），AIC 及其渐近推导，DIC、WAIC 与留一交叉验证作为样本外精度的偏差校正估计，八所学校的比较，BIC，以及贝叶斯因子：血友病例子、Jeffreys 证据尺度、Lindley 悖论、广义先验与 BIC 背后的 Laplace 近似。
source_hash: 17350c4fa15e
---

模型检验（[3.7.7](/3.7.7)）问的是某一个模型是否拟合数据，所用的差异量针对特定的失效方式。模型比较问的是若干模型中哪个更好，它还有另一个用途：把扩展后的模型与当前模型相比较，可以看出模型应该朝哪个方向改进。本章发展两类回答。第一类按模型对新数据的预测精度来评价模型（§8.1）。新数据通常得不到，所以只能用拟合模型的那批数据来估计精度，核心困难是校正模型在自己的训练数据上被评价时的乐观偏差。信息准则 AIC、DIC 与 WAIC 用有效参数个数校正样本内精度（§8.2–§8.4）；交叉验证则把一部分数据留出来（§8.5）。[3.7.6](/3.7.6) 的八所学校例子把它们全部比较了一遍（§8.6）。第二类是真正意义上的模型选择的贝叶斯回答：每个模型的后验概率，由 [3.2.7](/3.2.7) 的**贝叶斯因子**决定（§8.8），BIC 是它的大样本近似（§8.7）。两类回答追求的目标不同，一个是预测，一个是识别真实模型，二者可能不一致。

## 8.1. 预测精度的度量

预测精度是评价模型的一种方式。有时它本身就是目的，例如评价一个预报；更多时候它是比较模型的尺子。预测精度可以用很多方式度量：分类准确率、金钱成本、均方误差或对数似然。哪一种合适取决于预测的类型。

### 8.1.1. 点预测与概率预测

在点预测中，每个观测只报告一个值作为预测，自然的精度度量是预测值 $\mathbb{E}(y_i\mid\theta)$ 的均方误差

$$
\frac1n\sum_{i=1}^n\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2,\qquad\text{或加权形式}\qquad\frac1n\sum_{i=1}^n\frac{\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2}{\operatorname{Var}(y_i\mid\theta)}.
$$
它们易于解释，但对远离正态的模型不太合适，而且忽略了预测的不确定性。在概率预测中，报告的是完整的预测分布，应当把它当作分布来评价。

**定义 8.1.1（对数预测密度）** 参数为 $\theta$ 的模型下数据 $y$ 的**对数预测密度**是 $\log p(y\mid\theta)$，即在数据处取值的**似然函数**的对数。对密度为 $g$ 的预测分布，观测 $\tilde y$ 的对数预测密度是 $\log g(\tilde y)$，即该预测的对数得分。

本章其余部分使用对数预测密度，理由有二。

- 在方差恒定的正态模型中，$\log p(y\mid\theta)=-\frac n2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_i\big(y_i-\mathbb{E}(y_i\mid\theta)\big)^2$ 是均方误差的线性函数，两种度量一致。
- 若数据来自真实密度 $f$，则预测 $g$ 的期望对数预测密度为 $\mathbb{E}_f\log g(\tilde y)=\mathbb{E}_f\log f(\tilde y)-\operatorname{KL}(f\,\Vert\,g)$。第一项与模型无关，所以最大化期望对数预测密度等价于最小化真实分布到预测分布的 **Kullback–Leibler 散度**。

### 8.1.2. 样本外精度与样本内精度

对新观测 $\tilde y_i$ 的贝叶斯预测不是某个特定 $\theta$ 处的 $p(\tilde y_i\mid\theta)$，而是后验预测密度 $p_{\mathrm{post}}(\tilde y_i)=\int p(\tilde y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta$，其中 $p_{\mathrm{post}}(\theta)=p(\theta\mid y)$。其对数预测密度为

$$
\log p_{\mathrm{post}}(\tilde y_i)=\log\mathbb{E}_{\mathrm{post}}\big(p(\tilde y_i\mid\theta)\big)=\log\int p(\tilde y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta.
$$

**定义 8.1.2（期望对数逐点预测密度）** 设 $f$ 是产生数据的真实分布。对一个新数据点的期望对数预测密度，以及对含 $n$ 个点的新数据集的**期望对数逐点预测密度**分别为

$$
\mathrm{elpd}=\mathbb{E}_f\big(\log p_{\mathrm{post}}(\tilde y_i)\big)=\int\big(\log p_{\mathrm{post}}(\tilde y)\big)f(\tilde y)\,\mathrm{d}\tilde y,\qquad\mathrm{elppd}=\sum_{i=1}^n\mathbb{E}_f\big(\log p_{\mathrm{post}}(\tilde y_i)\big).
$$

elppd 度量样本外的预测精度，是模型比较的关键量：两个模型中 elppd 较大者平均而言对新数据预测得更好。由于 $f$ 未知，它无法计算。能够计算的是对手头数据的精度。

**定义 8.1.3（对数逐点预测密度）** 观测数据 $y=(y_1,\dots,y_n)$ 的**对数逐点预测密度**为

$$
\mathrm{lppd}=\log\prod_{i=1}^np_{\mathrm{post}}(y_i)=\sum_{i=1}^n\log\int p(y_i\mid\theta)\,p_{\mathrm{post}}(\theta)\,\mathrm{d}\theta.
$$
给定后验抽样 $\theta^1,\dots,\theta^S$，用 Monte Carlo 积分计算为

$$
\widehat{\mathrm{lppd}}=\sum_{i=1}^n\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^s)\Big).
$$

lppd 是样本内的预测精度，通常高估 elppd：同一批数据既用来拟合模型又用来评估模型，而且这种乐观偏差很可能随参数个数增加。由已有数据估计 elppd 有两种办法。

- 校正后的样本内精度：从 lppd（或从点估计处的对数预测密度）中减去偏差的校正量，其形式是一个有效参数个数（effective number of parameters），即模型能够拟合噪声的程度。AIC、DIC 与 WAIC 都属此类；它们很快，只需拟合一次。
- 交叉验证：用一部分数据拟合模型，在留出的部分上评估预测精度；这更接近定义，但计算代价可能很高。

出于历史原因，预测精度的度量称为信息准则，并按偏差统计量（deviance）$D(\theta)=-2\log p(y\mid\theta)$ 的尺度报告，即对数预测密度乘以 $-2$，因此越小越好。（在广义线性模型中，偏差习惯上相对于饱和模型度量，这只改变一个与 $\theta$ 无关的常数，不影响比较。）

## 8.2. Akaike 信息准则

最早的校正由 Akaike 在 1973–1974 年提出，估计的是**极大似然估计**量 $\hat\theta=\hat\theta(y)$ 处代入式预测 $p(\tilde y\mid\hat\theta)$ 的预测精度。对大的 $n$，后验集中在 $\hat\theta$ 附近（[3.7.5](/3.7.5)），elpd 近似为

$$
\mathrm{elpd}_{\hat\theta}=\mathbb{E}_f\log p\big(\tilde y_i\mid\hat\theta(y)\big),
$$
即新点 $\tilde y_i\sim f$ 在拟合模型下的期望对数密度。它不能直接计算，但对数据取期望后可以近似：$\hat\theta$ 渐近服从 $\mathcal{N}(\theta_0,V_0/n)$，且 $\tilde y_i$ 与 $\hat\theta$ 独立，所以 $\mathbb{E}_{\tilde y_i\times\hat\theta}\log p(\tilde y_i\mid\hat\theta)=\mathbb{E}_{\tilde y_i}\big[\mathbb{E}_{\hat\theta}\log p(\tilde y_i\mid\hat\theta)\big]$ 可以在 $\theta_0$ 附近展开。

**命题 8.2.1** 设 $y_1,\dots,y_n\overset{\text{iid}}{\sim}f$，模型 $p(y\mid\theta)$，$\theta\in\mathbb{R}^k$ 是正则的且包含真实分布，$f=p(\cdot\mid\theta_0)$。则当 $n\to\infty$ 时，到一阶有

$$
\mathbb{E}\big[\log p(y\mid\hat\theta)\big]-n\,\mathbb{E}\big[\mathrm{elpd}_{\hat\theta}\big]\to k.
$$

**证明**（概要）设 $S(y,\theta)$ 为单个观测的**得分函数**，$H(y,\theta)$ 为其 Hessian，$J=J(\theta_0)=-\mathbb{E}_fH(y,\theta_0)$ 为单个观测的 **Fisher 信息量**，$c(\theta_0)=\int f(y)\log p(y\mid\theta_0)\,\mathrm{d}y$，$Z_n=\sqrt n(\hat\theta-\theta_0)$ 依分布收敛于 $\mathcal{N}(\boldsymbol{0},J^{-1})$。在 $\theta_0$ 附近展开，并利用 $\mathbb{E}_fS(\tilde y,\theta_0)=\boldsymbol{0}$，

$$
\mathrm{elpd}_{\hat\theta}\approx c(\theta_0)+(\hat\theta-\theta_0)^{\mathsf T}\mathbb{E}_fS(\tilde y,\theta_0)-\frac12(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)=c(\theta_0)-\frac1{2n}Z_n^{\mathsf T}JZ_n.
$$
对样本内的一项，似然方程 $\boldsymbol{0}=\sum_iS(y_i,\hat\theta)\approx\sum_iS(y_i,\theta_0)+\sum_iH(y_i,\theta_0)(\hat\theta-\theta_0)$ 给出 $\frac1n\sum_iS(y_i,\theta_0)\approx J(\hat\theta-\theta_0)$，又 $\frac1n\sum_iH(y_i,\theta_0)\approx-J$，所以

$$
\frac1n\log p(y\mid\hat\theta)\approx\frac1n\sum_{i=1}^n\log p(y_i\mid\theta_0)+(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)-\frac12(\hat\theta-\theta_0)^{\mathsf T}J(\hat\theta-\theta_0)=\frac1n\sum_{i=1}^n\log p(y_i\mid\theta_0)+\frac1{2n}Z_n^{\mathsf T}JZ_n.
$$
第一项的期望为 $c(\theta_0)$。两式相减，$\mathbb{E}[\log p(y\mid\hat\theta)]-n\,\mathbb{E}[\mathrm{elpd}_{\hat\theta}]\approx\mathbb{E}[Z_n^{\mathsf T}JZ_n]=\operatorname{tr}(JJ^{-1})=k$。$\square$

因此样本内对数似然平均乐观了 $k$，而 $\widehat{\mathrm{elpd}}_{\mathrm{AIC}}=\log p(y\mid\hat\theta)-k$ 是 $n\,\mathrm{elpd}_{\hat\theta}$ 的近似无偏估计。（若模型不包含 $f$，同样的论证给出校正量 $\operatorname{tr}(J^{-1}K)$，其中 $K=\operatorname{Var}_fS(y,\theta_0)$；当 $K=J$ 时化为 $k$。）在偏差的尺度上，这就是**赤池信息准则**，已在 [3.4.11](/3.4.11) 见过。

**定义 8.2.1（赤池信息准则）** 对有 $k$ 个参数、极大似然估计为 $\hat\theta_{\mathrm{MLE}}$ 的模型，

$$
\mathrm{AIC}=-2\log p(y\mid\hat\theta_{\mathrm{MLE}})+2k=-2\,\widehat{\mathrm{elpd}}_{\mathrm{AIC}}.
$$
值越小，估计的预测精度越高。

一条实用的经验规则是：两个模型的 AIC 相差小于 $2$，说明二者没有实质差别。这条规则有检验的解释。设模型 1（简单，$k_1$ 个参数）嵌套于模型 2（复杂，$k_2>k_1$）。则

$$
\mathrm{AIC}_1-\mathrm{AIC}_2>2\iff-2\log\frac{p(y\mid\hat\theta_1)}{p(y\mid\hat\theta_2)}>2+2(k_2-k_1),
$$
左边是**似然比**统计量，在简单模型成立时近似服从 $\chi^2_{k_2-k_1}$。当 $k_2-k_1=1$ 时，以超过 $2$ 的差距偏好复杂模型，相当于在 $\chi^2_1>4$ 时拒绝简单模型，即水平为 $0.046$ 的检验。

AIC 是频率学派的构造：它代入极大似然估计并数参数个数。对有效复杂度不等于参数个数的模型，例如层次模型（总体分布约束了各组的参数），它不适用，而且它忽略了先验。

## 8.3. 偏差信息准则

Spiegelhalter 等人（2002）的偏差信息准则是 AIC 的贝叶斯版本。它用后验均值代替极大似然估计，用基于数据的估计代替参数个数。记 $d(y,\theta,\tilde\theta)=-2\log p(y\mid\theta)+2\log p(y\mid\tilde\theta)$ 为 $\theta$ 处的偏差与估计 $\tilde\theta=\tilde\theta(y)$ 处的偏差之差。AIC 评价的是真值处的超出量 $d(y,\theta_0,\hat\theta_{\mathrm{MLE}})$，其期望约为 $k$。贝叶斯观点把 $\theta$ 当作随机的，对后验取平均，先验就在这里起作用：

$$
p_{\mathrm{DIC}}=\mathbb{E}_{\theta\mid y}\,d(y,\theta,\tilde\theta)=\mathbb{E}_{\theta\mid y}\big[-2\log p(y\mid\theta)\big]+2\log p(y\mid\tilde\theta).
$$

**定义 8.3.1（偏差信息准则）** 设 $\hat\theta_{\mathrm{Bayes}}=\mathbb{E}(\theta\mid y)$ 为后验均值。DIC 的**有效参数个数**为

$$
p_{\mathrm{DIC}}=2\Big(\log p(y\mid\hat\theta_{\mathrm{Bayes}})-\mathbb{E}_{\mathrm{post}}\big(\log p(y\mid\theta)\big)\Big),\qquad\text{计算为}\qquad2\Big(\log p(y\mid\hat\theta_{\mathrm{Bayes}})-\frac1S\sum_{s=1}^S\log p(y\mid\theta^s)\Big),
$$
即后验平均偏差减去后验均值处的偏差。记 $\widehat{\mathrm{elpd}}_{\mathrm{DIC}}=\log p(y\mid\hat\theta_{\mathrm{Bayes}})-p_{\mathrm{DIC}}$，**偏差信息准则**为

$$
\mathrm{DIC}=-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})+2p_{\mathrm{DIC}}=-2\,\widehat{\mathrm{elpd}}_{\mathrm{DIC}}.
$$

在平坦先验与近似正态的后验下，$p_{\mathrm{DIC}}\approx k$，DIC 化为 AIC。在信息先验或层次结构下，参数不能自由地拟合噪声，$p_{\mathrm{DIC}}$ 小于参数个数。

**例 8.3.1（层次模型的有效参数个数）** 考虑各组方差已知的层次正态模型，$\bar y_{\cdot i}\mid\theta_i\sim\mathcal{N}(\theta_i,\sigma_i^2)$，$\theta_i\sim\mathcal{N}(\mu,\tau^2)$，$i=1,\dots,J$，并令

$$
\rho_i=\frac{\tau^2}{\tau^2+\sigma_i^2}
$$
为 $\bar y_{\cdot i}$ 的方差中由组均值的变异所占的比例（第 $i$ 组的组内相关）。

- 若 $\mu$ 与 $\tau^2$ 已知，则 $p_{\mathrm{DIC}}=\sum_i\rho_i$。
- 若 $\tau^2$ 已知而 $\mu$ 取均匀超先验，则 $p_{\mathrm{DIC}}=\sum_i\rho_i+\dfrac{\sum_i\rho_i(1-\rho_i)}{\sum_i\rho_i}$；若所有 $\sigma_i^2$ 相等，即 $\rho_i=\rho$，则 $p_{\mathrm{DIC}}=1+(J-1)\rho$。

*推导* 对这个正态似然，$-2\log p(y\mid\theta)=\sum_i(\bar y_{\cdot i}-\theta_i)^2/\sigma_i^2+\text{常数}$，对此二次型，后验平均偏差减去后验均值处的偏差为 $p_{\mathrm{DIC}}=\sum_i\operatorname{Var}(\theta_i\mid y)/\sigma_i^2$。当 $\mu,\tau$ 已知时，$\theta_i\mid y\sim\mathcal{N}\big(\rho_i\bar y_{\cdot i}+(1-\rho_i)\mu,\rho_i\sigma_i^2\big)$，得到 $\sum_i\rho_i$。当 $\mu$ 未知时，$\theta_i=\rho_i\bar y_{\cdot i}+(1-\rho_i)\mu+\text{噪声}$，其中 $\operatorname{Var}(\mu\mid y)=\big(\sum_j(\sigma_j^2+\tau^2)^{-1}\big)^{-1}$（[3.7.6](/3.7.6)），所以 $\operatorname{Var}(\theta_i\mid y)=\rho_i\sigma_i^2+(1-\rho_i)^2\operatorname{Var}(\mu\mid y)$。由于 $(1-\rho_i)^2/\sigma_i^2=\rho_i(1-\rho_i)/\tau^2$，$(\sigma_j^2+\tau^2)^{-1}=\rho_j/\tau^2$，额外的一项为 $\sum_i\rho_i(1-\rho_i)/\sum_j\rho_j$。对相等的 $\rho_i=\rho$，它等于 $1-\rho$，$p_{\mathrm{DIC}}=J\rho+1-\rho$。$\square$

两个极限很有启发。当 $\tau\to\infty$（$\rho\to1$，**无合并**）时 $p_{\mathrm{DIC}}\to J$，每组一个参数；当 $\tau\to0$（$\rho\to0$，**完全合并**）时 $p_{\mathrm{DIC}}\to1$，即共同的均值。**分层模型**介于两者之间，它的有效参数个数由数据通过 $\tau$ 决定。

:::

DIC 仍然使用点估计，所以依赖于参数化（$\hat\theta_{\mathrm{Bayes}}$ 不具有不变性），当后验均值不是好的概括时（例如双峰后验）表现可能很差。

## 8.4. Watanabe–Akaike 信息准则

Watanabe（2010）的 Watanabe–Akaike（或称广泛适用）信息准则是更彻底的贝叶斯方法。它从 lppd，即真实后验预测分布的样本内精度出发，而不是从代入式估计出发；它逐点估计有效参数个数；并且可以作为交叉验证的近似推导出来。

**定义 8.4.1（Watanabe–Akaike 信息准则）** 设 $\mathrm{lppd}$ 如定义 8.1.3。有效参数个数的两个估计为

$$
p_{\mathrm{WAIC}1}=2\sum_{i=1}^n\Big(\log\big(\mathbb{E}_{\mathrm{post}}p(y_i\mid\theta)\big)-\mathbb{E}_{\mathrm{post}}\big(\log p(y_i\mid\theta)\big)\Big),\qquad p_{\mathrm{WAIC}2}=\sum_{i=1}^n\operatorname{Var}_{\mathrm{post}}\big(\log p(y_i\mid\theta)\big),
$$
由后验抽样计算为

$$
\hat p_{\mathrm{WAIC}1}=2\sum_{i=1}^n\Big(\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^s)\Big)-\frac1S\sum_{s=1}^S\log p(y_i\mid\theta^s)\Big),\qquad\hat p_{\mathrm{WAIC}2}=\sum_{i=1}^nV_{s=1}^S\log p(y_i\mid\theta^s),
$$
其中 $V_{s=1}^S$ 表示对各次抽样的样本方差。记 $\widehat{\mathrm{elppd}}_{\mathrm{WAIC}}=\mathrm{lppd}-p_{\mathrm{WAIC}}$，**Watanabe–Akaike 信息准则**为 $\mathrm{WAIC}=-2\,\widehat{\mathrm{elppd}}_{\mathrm{WAIC}}$。

两种校正都是对数据点求和，每一项度量后验不确定性对该点拟合的影响有多大。由 Jensen 不等式，$p_{\mathrm{WAIC}1}\ge0$，且对正则模型二者渐近相等；一般推荐 $p_{\mathrm{WAIC}2}$，因为它的行为更接近留一交叉验证。与 DIC 不同，WAIC 对后验取平均而不是以点估计为条件，所以对重新参数化不变，并且适用于奇异模型（如混合模型），这时后验远非正态。由于它是逐点计算的，要求数据可以划分成条件独立的块 $y_i$，这对回归是自然的，对时间序列或空间数据则不然。

**注 8.4.1（理论背景）** Watanabe 的理论区分正则模型与奇异模型（真实分布处对数似然的 Hessian 是否正定），以及可实现与不可实现的模型（真实分布是否在模型之内）。若真实分布对模型是正则且可实现的，则 WAIC 与 AIC、DIC 渐近等价；否则它们不等价。即使真实分布对模型是奇异的或不可实现的，WAIC 作为随机变量也渐近等价于贝叶斯留一交叉验证。

## 8.5. 交叉验证

**交叉验证**通过留出数据来估计样本外精度。把数据划分为训练集 $y_{\mathrm{train}}$ 与验证集 $y_{\mathrm{validation}}$；模型在训练数据上拟合，得到后验 $p_{\mathrm{train}}(\theta)=p(\theta\mid y_{\mathrm{train}})$；用验证数据的对数预测密度 $\log p_{\mathrm{train}}(y_{\mathrm{validation}})=\log\int p(y_{\mathrm{validation}}\mid\theta)\,p_{\mathrm{train}}(\theta)\,\mathrm{d}\theta$ 评价拟合，通常由 $p_{\mathrm{train}}(\theta)$ 的模拟来估计。验证数据起新数据的作用，所以除了模型是用较少的数据拟合的以外，不需要再校正乐观偏差。

**定义 8.5.1（留一交叉验证）** 在**留一交叉验证**中，模型拟合 $n$ 次，每次留出一个点 $y_i$，其后验为 $p_{\mathrm{post}(-i)}(\theta)=p(\theta\mid y_{-i})$。估计的 lppd 为

$$
\mathrm{lppd}_{\mathrm{loo\text{-}cv}}=\sum_{i=1}^n\log p_{\mathrm{post}(-i)}(y_i),\qquad\text{计算为}\qquad\sum_{i=1}^n\log\Big(\frac1S\sum_{s=1}^{S}p(y_i\mid\theta^{is})\Big),
$$
其中 $\theta^{is}$，$s=1,\dots,S$，是来自 $p_{\mathrm{post}(-i)}$ 的抽样。由此隐含的有效参数个数为 $p_{\mathrm{loo\text{-}cv}}=\mathrm{lppd}-\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$。

每次拟合用 $n-1$ 而不是 $n$ 个数据点，所以 $\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ 略微低估了用全部数据拟合的模型的精度。偏差校正后的版本为

$$
\mathrm{lppd}_{\mathrm{cloo\text{-}cv}}=\mathrm{lppd}_{\mathrm{loo\text{-}cv}}+b,\qquad b=\mathrm{lppd}-\overline{\mathrm{lppd}}_{-i},\qquad\overline{\mathrm{lppd}}_{-i}=\frac1n\sum_{i=1}^n\sum_{j=1}^n\log p_{\mathrm{post}(-i)}(y_j),
$$
其中 $\overline{\mathrm{lppd}}_{-i}$ 计算为 $\frac1n\sum_i\sum_j\log\big(\frac1S\sum_sp(y_j\mid\theta^{is})\big)$；对大的 $n$，校正量 $b$ 通常忽略不计。精确的留一交叉验证需要 $n$ 次后验模拟。实际中常由一次拟合出发，用权重为 $1/p(y_i\mid\theta^s)$ 的重要性抽样近似，并用 Pareto 平滑使之稳定（PSIS-LOO）。交叉验证与 WAIC 一样，要求数据可以划分为可交换或条件独立的块，而块的选取（单个观测还是层次模型的整个组）决定了“新数据”的含义。

## 8.6. 例：八所学校

**例 8.6.1** 回顾 [3.7.6](/3.7.6) 的八所学校：在八个随机化实验中，特殊辅导对 SAT 语文成绩的效应估计 $y_j$ 及其标准误 $\sigma_j$ 为

| 学校 | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| $y_j$ | $28$ | $8$ | $-3$ | $7$ | $-1$ | $1$ | $18$ | $12$ |
| $\sigma_j$ | $15$ | $10$ | $16$ | $11$ | $9$ | $11$ | $10$ | $18$ |

把数据当作八个方差已知的正态观测 $y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$，比较三个先验均为无信息的模型：

1. **无合并**（分别估计，$\tau=\infty$）：$\theta_1,\dots,\theta_8$ 取 $p(\theta_1,\dots,\theta_8)\propto1$，于是 $\theta_j\mid y\sim\mathcal{N}(y_j,\sigma_j^2)$；
2. **完全合并**（$\tau=0$）：$\theta_1=\cdots=\theta_8=\theta$，$p(\theta)\propto1$，得到合并后验 $\theta\mid y\sim\mathcal{N}(7.7,4.1^2)$；
3. **分层模型**（估计 $\tau$）：$\theta_j\mid\mu,\tau\sim\mathcal{N}(\mu,\tau^2)$，$p(\mu,\tau)\propto1$。

各准则按偏差的尺度，由下图的脚本根据后验模拟计算（末位数字随 Monte Carlo 误差变化），结果为：

| | | 无合并 | 完全合并 | 层次模型 |
|---|---|---|---|---|
| AIC | $-2\log p(y\mid\hat\theta_{\mathrm{MLE}})$ | $54.6$ | $59.4$ | |
| | $k$ | $8$ | $1$ | |
| | $\mathrm{AIC}$ | $70.6$ | $61.4$ | |
| DIC | $-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})$ | $54.6$ | $59.4$ | $57.4$ |
| | $p_{\mathrm{DIC}}$ | $8.0$ | $1.0$ | $2.8$ |
| | $\mathrm{DIC}$ | $70.6$ | $61.4$ | $63.1$ |
| WAIC | $-2\,\mathrm{lppd}$ | $60.2$ | $59.8$ | $59.2$ |
| | $p_{\mathrm{WAIC}1}$ | $2.5$ | $0.6$ | $1.0$ |
| | $p_{\mathrm{WAIC}2}$ | $4.0$ | $0.7$ | $1.3$ |
| | $\mathrm{WAIC}$（用 $p_{\mathrm{WAIC}1}$） | $65.1$ | $60.9$ | $61.3$ |
| | $\mathrm{WAIC}$（用 $p_{\mathrm{WAIC}2}$） | $68.2$ | $61.1$ | $61.9$ |
| LOO-CV | $p_{\mathrm{loo\text{-}cv}}$ | | $0.7$ | $1.7$ |
| | $-2\,\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | | $61.1$ | $62.7$ |

![八所学校。左：三个模型由 AIC、DIC、WAIC（用 p_WAIC2）与精确留一交叉验证得到的 −2 elppd 估计；AIC 对层次模型没有定义，LOO-CV 对无合并没有定义。右：当两个模型都取正常先验 N(0, A²) 时，完全合并相对于各自独立效应的贝叶斯因子；它随 A 增大而无界增长（§8.8.5）。](./plots/eight_schools_ic.py)

有几点值得说明。

- 无合并在极大似然估计处完美拟合数据（$\hat\theta_j=y_j$），所以它的样本内偏差最低，但 $8$ 个参数的惩罚使它在每个准则下都是最差的模型。它的校正量可以精确计算（思考题 4）：$p_{\mathrm{DIC}}=8$，$p_{\mathrm{WAIC}1}=8(1-\log2)=2.45$，$p_{\mathrm{WAIC}2}=4$。这里 $p_{\mathrm{WAIC}}$ 远小于参数个数，WAIC 低估了每个数据点都用自己的参数去拟合的模型的乐观偏差；WAIC 的逐点校正依赖于数据量相对于参数个数充足，而每个参数只有一个观测时这一条件不成立。
- 完全合并只有一个参数，所有准则一致，$p\approx1$ 或更小。
- 层次模型有 $8$ 个组参数外加 $\mu$ 与 $\tau$，但它的有效参数个数在 $1.0$ 到 $2.8$ 之间，因为 $\tau$ 的后验集中在较小的值附近，各 $\theta_j$ 被强烈合并（例 8.3.1）。AIC 对它完全无能为力。
- LOO-CV 对无合并不可用：在每个 $\theta_j$ 上取平坦先验时，给定其余七所学校后的后验对被留出的学校没有任何信息，其预测分布是不正常的。

完全合并与层次模型的差别在偏差尺度上小于 $2$：只有八个数据点时，数据无法从预测精度上区分它们，这与 $\tau$ 的后验有相当一部分质量靠近 $0$ 是一致的。层次模型仍是自然的选择，因为它包含两个极端，并让数据决定合并的程度；各准则也确认，这额外的灵活性几乎不花代价。

## 8.7. 贝叶斯信息准则

**贝叶斯信息准则**（[3.4.11](/3.4.11)），又因 Gideon Schwarz（1978）而称 Schwarz 准则，常与 AIC 一起被提到，但来源不同。

**定义 8.7.1（贝叶斯信息准则）** 对拟合 $n$ 个观测、有 $k$ 个参数的模型，

$$
\mathrm{BIC}=-2\log p(y\mid\hat\theta)+k\log n.
$$

BIC 是作为模型下数据的边际密度 $p(y)$ 的近似导出的，而不是预测精度的近似（§8.8.6）。因此它与贝叶斯因子而不是 elppd 相关。它看起来像是惩罚更重的 AIC，以 $k\log n$ 代替 $2k$（$n\ge8$ 起就更重），并倾向于选择更简单的模型。两个准则回答的是不同的问题。

- BIC 假设候选模型之一为真，试图找出在贝叶斯意义下最可能为真的模型。当真实模型在候选之中时，随着 $n\to\infty$，它以趋于 $1$ 的概率选中真实模型。
- AIC 与交叉验证试图找出预测最好的模型，不论候选中是否有真实模型；多一个冗余参数的模型可能预测得几乎一样好，AIC 对它的惩罚不足以把它排除。

一般而言，AIC 适合挑选用于预测的模型，BIC 适合挑选用于解释的模型。尽管名为“贝叶斯”，BIC 并不是完全贝叶斯的量：与 AIC 一样，它使用点估计与参数个数，除先验的数量级外忽略了先验。

## 8.8. 贝叶斯因子

### 8.8.1. 定义

预测准则对模型排序；严格意义下的贝叶斯模型选择则给模型赋予概率。设两个模型（假设）$H_1$ 与 $H_2$ 的先验概率为 $p(H_1)$、$p(H_2)$，每个都定义了数据的完整概率模型，于是数据在各模型下有**边际似然** $p(y\mid H)=\int p(y\mid\theta,H)\,p(\theta\mid H)\,\mathrm{d}\theta$。

**定义 8.8.1（贝叶斯因子）** $H_2$ 相对于 $H_1$ 的**贝叶斯因子**是边际似然之比，

$$
\mathrm{BF}(H_2;H_1)=\frac{p(y\mid H_2)}{p(y\mid H_1)}=\frac{\int p(y\mid\theta_2,H_2)\,p(\theta_2\mid H_2)\,\mathrm{d}\theta_2}{\int p(y\mid\theta_1,H_1)\,p(\theta_1\mid H_1)\,\mathrm{d}\theta_1},
$$
于是由 Bayes 公式，

$$
\underbrace{\frac{p(H_2\mid y)}{p(H_1\mid y)}}_{\text{后验优势比}}=\underbrace{\frac{p(H_2)}{p(H_1)}}_{\text{先验优势比}}\times\mathrm{BF}(H_2;H_1).
$$

贝叶斯因子度量数据把一个模型相对于另一个模型的优势比改变了多少：它是**后验优势比**与**先验优势比**之比。反过来，给定先验概率后，贝叶斯因子决定后验概率。

**命题 8.8.1** 若 $H_1$ 与 $H_2$ 是仅有的两个可能的模型，$B(y)=\mathrm{BF}(H_1;H_2)$，则

$$
p(H_1\mid y)=\frac{1}{1+\dfrac{1}{B(y)}\dfrac{p(H_2)}{p(H_1)}}.
$$

**证明** $p(H_1\mid y)+p(H_2\mid y)=1$，且 $p(H_2\mid y)/p(H_1\mid y)=\frac{p(H_2)}{p(H_1)}\cdot\frac1{B(y)}$；解出 $p(H_1\mid y)$ 即可。$\square$

下面三点划定了贝叶斯因子的适用范围。

- 只有当数据在每个模型下的边际密度都是正常的，贝叶斯因子才有定义，这要求先验是正常的（§8.8.5）。
- 当底层的模型空间确实是离散的，即每个备择都有科学意义而且没有明显处于二者之间的模型时，贝叶斯因子效果很好。
- 对本质上连续的模型，嵌套模型之间的离散选择是人为的，贝叶斯因子的效果较差；这时把模型嵌入一个更大的连续模型（如层次模型）通常提供更多信息。

### 8.8.2. 离散的例子：血友病

**例 8.8.1** 血友病是 X 连锁隐性遗传病：单条 X 染色体上带有该基因的男性发病，带有一个拷贝的女性是不发病的携带者。考虑一位女性，她的兄弟患病，这说明她的母亲是携带者；她的父亲未患病。因此她本人携带该基因的概率为 $\frac12$。令 $\theta=1$ 表示她是携带者，$\theta=0$ 表示不是，先验为 $\mathbb{P}(\theta=1)=\mathbb{P}(\theta=0)=\frac12$。数据是她两个儿子（不是同卵双胞胎）的状况，患病记 $y_i=1$，未患病记 $y_i=0$，两人均未患病。若她是携带者，每个儿子独立地以概率 $\frac12$ 患病；若不是，则两人都不可能患病：

$$
p(y_1=0,y_2=0\mid\theta=1)=\tfrac12\cdot\tfrac12=0.25,\qquad p(y_1=0,y_2=0\mid\theta=0)=1.
$$
她是携带者的后验概率为 $\mathbb{P}(\theta=1\mid y)=\frac{0.25\cdot0.5}{0.25\cdot0.5+1\cdot0.5}=0.2$。用模型比较的语言，取 $H_1\colon\theta=1$，$H_2\colon\theta=0$：

| 先验优势比 | 贝叶斯因子 | 后验优势比 |
|---|---|---|
| $\dfrac{p(H_2)}{p(H_1)}=1$ | $\dfrac{p(y\mid H_2)}{p(y\mid H_1)}=\dfrac{1.0}{0.25}=4$ | $\dfrac{p(H_2\mid y)}{p(H_1\mid y)}=4$ |

这个例子具备使贝叶斯因子有用的两个特征：每个离散的备择都有科学意义，且没有处于二者之间的科学模型；数据在每个模型下的边际分布 $p(y\mid H_i)$ 是正常的。

### 8.8.3. Jeffreys 证据尺度

远大于 $1$ 的贝叶斯因子支持分子上的模型。Jeffreys 给证据提出了语言标签，针对 $B(y)=p(y\mid H_2)/p(y\mid H_1)$ 给出，其中 $H_2$ 是零模型。

**定义 8.8.2（Jeffreys 证据尺度）** **Jeffreys 证据尺度**把零模型 $H_2$ 相对于备择 $H_1$ 的贝叶斯因子 $B(y)$ 分级如下：

| $B(y)$ | 证据 |
|---|---|
| $B(y)\ge1$ | 支持 $H_2$ |
| $10^{-1/2}\approx0.316\le B(y)<1$ | 不利于 $H_2$，但几乎不值一提 |
| $10^{-1}\le B(y)<10^{-1/2}$ | 对 $H_2$ 相当不利 |
| $10^{-3/2}\approx0.0316\le B(y)<10^{-1}$ | 对 $H_2$ 强烈不利 |
| $10^{-2}\le B(y)<10^{-3/2}$ | 对 $H_2$ 极强烈不利 |
| $B(y)<10^{-2}$ | 对 $H_2$ 决定性不利 |

各级按 $\log_{10}B$ 每半个单位一级，标签显然有些随意；这个尺度是交流用的约定，而不是决策规则。有些表述把强烈与极强烈两级合并为 $0.01\le B(y)<0.1$ 的一级。

### 8.8.4. 连续模型与 Lindley 悖论

**例 8.8.2** 设 $y_1,\dots,y_n\overset{\text{iid}}{\sim}\mathcal{N}(\mu,1)$，检验 $H_0\colon\mu=0$ 对 $H_1\colon\mu\ne0$，其中在 $H_1$ 下先验为 $\mu\sim\mathcal{N}(0,1)$。样本均值 $\bar y$ 是充分的。在 $H_0$ 下无需积分，$p(\bar y\mid H_0)=\mathcal{N}(\bar y\mid0,1/n)$；在 $H_1$ 下，

$$
p(\bar y\mid H_1)=\int p(\bar y\mid\mu,H_1)\,p(\mu\mid H_1)\,\mathrm{d}\mu=\mathcal{N}\big(\bar y\mid0,1+\tfrac1n\big).
$$
因此

$$
\mathrm{BF}(H_0;H_1)=\frac{p(\bar y\mid H_0)}{p(\bar y\mid H_1)}=\sqrt{\frac{1+1/n}{1/n}}\;\frac{\mathrm{e}^{-n\bar y^2/2}}{\mathrm{e}^{-\frac{n}{n+1}\bar y^2/2}}=\sqrt{n+1}\,\exp\Big(-\frac{n^2\bar y^2}{2(n+1)}\Big)\approx\sqrt n\,\mathrm{e}^{-n\bar y^2/2}.
$$
以经典统计量 $z=\sqrt n\,\bar y$ 表示，$\mathrm{BF}(H_0;H_1)\approx\sqrt n\,\mathrm{e}^{-z^2/2}$，当 $n\bar y^2=\log n$，即 $\lvert z\rvert=\sqrt{\log n}$ 时等于 $1$。

作为对照，经典的双侧检验在水平 $0.05$ 下，当 $\lvert z\rvert>1.96$ 时拒绝 $H_0$，与 $n$ 无关。贝叶斯的阈值 $\sqrt{\log n}$ 随 $n$ 增大：固定 $z$ 时，支持 $H_0$ 的贝叶斯因子按 $\sqrt n$ 增长。恰好在 $5\%$ 水平显著的数据（$z=1.96$）给出的 $\mathrm{BF}(H_0;H_1)$ 在 $n=10$ 时为 $0.58$，$n=100$ 时为 $1.5$，$n=10000$ 时为 $14.7$，所以在先验概率为 $\frac12$ 时，$H_0$ 的后验概率由 $0.37$ 升到 $0.60$ 与 $0.94$。显著的 p 值与大样本下对零假设的强烈贝叶斯支持之间的这种冲突，就是 Lindley 悖论（Lindley's paradox）（Lindley 1957；也称 Jeffreys–Lindley 悖论）。

![y_i ~ N(μ, 1)、H0: μ = 0 对 H1: μ ~ N(0, 1) 时的 Lindley 悖论。左：数据固定在 z = 1.96、2.58 与 3.29（双侧 p = 0.05、0.01、0.001）时，支持 H0 的贝叶斯因子随样本量的变化。右：先验概率为 1/2 时 H0 的后验概率。](./plots/lindley_paradox.py)

两个回答对各自的问题都是正确的。p 值固定了证据的阈值，而 $\bar y$ 的精度不断提高，所以越来越小的偏离 $0$ 的量也变得显著。贝叶斯因子比较的是 $\mu=0$ 与一个具体的备择，后者把先验分布在量级为 $1$ 的取值上：对大的 $n$，$z=1.96$ 意味着 $\bar y\approx1.96/\sqrt n$，这个值比备择认为合理的大多数取值都更接近 $0$，所以数据偏向点零假设。答案依赖于 $H_1$ 下的先验方差，而在连续问题中这很难论证；这正是贝叶斯因子对本质上连续的模型效果不太好的含义。

:::

*历史* 贝叶斯因子由 Harold Jeffreys（1935）引入，并在他的 *Theory of Probability*（1939）中发展。Jeffreys 确信归纳是逻辑的扩展形式；这种“部分信念的逻辑”必须把信念程度当作概率；简单的定律或假设应当被视为具有非零先验概率的独立模型；一个有用且逻辑自洽的假设检验方法必须是比较性的，并且基于手头的数据，而不是基于从未观测到的数据。贝叶斯因子就是他对一种自洽的模型选择与假设检验方法的尝试，用来弥补 p 值检验的缺陷。

### 8.8.5. 广义先验：再看八所学校

**例 8.8.3** 在八所学校的例子中，用贝叶斯因子比较 §8.6 的两个极端模型：

$$
H_1\colon p(y\mid\theta_1,\dots,\theta_J)=\prod_{j=1}^J\mathcal{N}(y_j\mid\theta_j,\sigma_j^2),\quad p(\theta_1,\dots,\theta_J)\propto1;\qquad H_2\colon p(y\mid\theta)=\prod_{j=1}^J\mathcal{N}(y_j\mid\theta,\sigma_j^2),\quad p(\theta)\propto1.
$$
贝叶斯因子 $p(y\mid H_2)/p(y\mid H_1)$ 没有定义，因为两个先验都是广义的，从而两个边际密度也都是广义的：对每个 $c>0$，广义先验 $c\cdot p(\theta)$ 与 $p(\theta)$ 一样有效，而它把 $p(y\mid H)$ 乘以 $c$。因此比值是任意的。贝叶斯因子不能用于带无信息先验密度的原始模型。

把平坦先验换成正常先验，$H_1$ 下 $\theta_j\overset{\text{iid}}{\sim}\mathcal{N}(0,A^2)$，$H_2$ 下 $\theta\sim\mathcal{N}(0,A^2)$。这时贝叶斯因子有定义，但它对 $A$ 高度敏感。对大的 $A$，$p(y\mid H_1)\approx\prod_j(2\pi A^2)^{-1/2}\int\mathcal{N}(y_j\mid\theta_j,\sigma_j^2)\,\mathrm{d}\theta_j\propto A^{-J}$，而 $p(y\mid H_2)\propto A^{-1}$，所以 $p(y\mid H_2)/p(y\mid H_1)$ 按 $A^{J-1}=A^7$ 增长（思考题 5）：随着 $A$ 增大，不论数据如何，后验越来越集中于完全合并。在 §8.6 的图中，贝叶斯因子在 $A=10$ 时为 $3$，在 $A=50$ 时约为 $10^3$，在 $A=1000$ 时约为 $10^{12}$。本意为含糊的先验在贝叶斯因子中并非无害：它把参数更多的模型的先验质量分散到不合理的取值上，从而惩罚该模型。

每个模型内部的后验推断在 $A$ 增大时几乎不变，贝叶斯因子却会变。与其在两个极端模型之间选择，不如选用层次模型：它把两者作为极限情形（$\tau=\infty$ 与 $\tau=0$）包含在内，并由数据估计合并的程度。

### 8.8.6. Laplace 近似与 BIC

对大的 $n$，边际似然 $p(y\mid M)=\int p(y\mid\theta,M)\,p(\theta\mid M)\,\mathrm{d}\theta$ 可以通过让积分变得像正态积分来近似。写 $p(y\mid M)=\int\mathrm{e}^{g(\theta)}\,\mathrm{d}\theta$，其中

$$
g(\theta)=\log\big(p(y\mid\theta,M)\,p(\theta\mid M)\big),
$$
即未归一化后验的对数，并在后验众数 $\tilde\theta$（梯度为零处）附近展开到二阶：

$$
g(\theta)\approx g(\tilde\theta)+\frac12(\theta-\tilde\theta)^{\mathsf T}H(\tilde\theta)(\theta-\tilde\theta)=g(\tilde\theta)-\frac12(\theta-\tilde\theta)^{\mathsf T}I_{\tilde\theta}(\theta-\tilde\theta),
$$
其中 $H=\big(\partial^2g/\partial\theta_i\partial\theta_j\big)$ 为 **Hesse 矩阵**，$I_{\tilde\theta}=-H(\tilde\theta)$ 为**观测信息**（包含先验的微小贡献）。对 $\theta\in\mathbb{R}^k$，该积分的 Laplace 近似（Laplace approximation）为

$$
p(y\mid M)\approx\mathrm{e}^{g(\tilde\theta)}\int\exp\Big(-\frac12(\theta-\tilde\theta)^{\mathsf T}I_{\tilde\theta}(\theta-\tilde\theta)\Big)\,\mathrm{d}\theta=\mathrm{e}^{g(\tilde\theta)}\,(2\pi)^{k/2}\lvert I_{\tilde\theta}\rvert^{-1/2},
$$
这就是 [3.7.5](/3.7.5) 的正态近似用于归一化常数。取对数，

$$
\log p(y\mid M)=\log p(y\mid\tilde\theta,M)+\log p(\tilde\theta\mid M)+\frac k2\log(2\pi)-\frac12\log\lvert I_{\tilde\theta}\rvert+o(1),
$$
这是一个近似的带惩罚的对数似然。对 $n$ 个独立观测，信息随 $n$ 线性增长，$I_{\tilde\theta}\approx nI_1$，$I_1$ 为单个观测的信息，所以 $\log\lvert I_{\tilde\theta}\rvert=k\log n+\log\lvert I_1\rvert$。除对数似然与 $-\frac k2\log n$ 之外，所有项在 $n\to\infty$ 时都保持有界：

$$
\log p(y\mid M)=\log p(y\mid\tilde\theta,M)-\frac k2\log n+O(1).
$$
对两个分别有 $k_1$ 与 $k_2$ 个参数、后验众数为 $\hat\theta_1$、$\hat\theta_2$（渐近等于极大似然估计）的模型 $H_1$ 与 $H_2$，由此得到，对大的 $n$，

$$
\log\mathrm{BF}(H_2;H_1)\approx\log p(y\mid\hat\theta_2,H_2)-\log p(y\mid\hat\theta_1,H_1)-\frac12(k_2-k_1)\log n=-\frac12\big(\mathrm{BIC}_2-\mathrm{BIC}_1\big).
$$
所以按贝叶斯因子给模型排序与按 BIC 排序是渐近等价的。近似的误差为 $O(1)$ 且依赖于先验，因此 $\mathrm{e}^{-\Delta\mathrm{BIC}/2}$ 只在相差一个有界因子的意义下近似贝叶斯因子；BIC 抓住了主导的 $\log n$ 行为，这足以做相合的模型选择，但不足以得到贝叶斯因子的准确值。

## 小结

| 度量 | 估计的对象 | 拟合项 | 惩罚（有效参数个数） | 备注 |
|---|---|---|---|---|
| AIC（定义 8.2.1） | 代入极大似然估计的 elpd | $-2\log p(y\mid\hat\theta_{\mathrm{MLE}})$ | $2k$ | 渐近的、频率学派的；无先验，不适用于层次模型 |
| DIC（定义 8.3.1） | 代入后验均值的 elpd | $-2\log p(y\mid\hat\theta_{\mathrm{Bayes}})$ | $2p_{\mathrm{DIC}}$，后验平均偏差减去均值处的偏差 | 依赖于参数化 |
| WAIC（定义 8.4.1） | 后验预测分布的 elppd | $-2\,\mathrm{lppd}$ | $2p_{\mathrm{WAIC}}$，$\log p(y_i\mid\theta)$ 的逐点后验方差 | 完全贝叶斯；渐近等于 LOO-CV |
| LOO-CV（定义 8.5.1） | elppd | $-2\,\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | 隐含的，$p_{\mathrm{loo\text{-}cv}}=\mathrm{lppd}-\mathrm{lppd}_{\mathrm{loo\text{-}cv}}$ | 拟合 $n$ 次，或用重要性抽样 |
| BIC（定义 8.7.1） | $-2\log p(y)$，边际似然 | $-2\log p(y\mid\hat\theta)$ | $k\log n$ | 选出真实模型；$\log\mathrm{BF}\approx-\frac12\Delta\mathrm{BIC}$ |
| 贝叶斯因子（定义 8.8.1） | 边际似然之比 | | 通过先验自动惩罚 | 需要正常先验；对先验敏感 |

- 预测精度是针对新数据定义的（elpd、elppd，定义 8.1.2），却要在没有新数据的情况下估计：或由样本内的 lppd（定义 8.1.3）经乐观偏差校正（命题 8.2.1）得到，或由交叉验证得到。所有这些都在偏差的尺度上比较，越低越好，相差不到约 $2$ 就不算实质差别。
- 信息准则服务于预测；贝叶斯因子与 BIC 服务于真实模型的选择。对真正离散的备择且先验正常时，贝叶斯因子是合理的（例 8.8.1，定义 8.8.2 的 Jeffreys 尺度），但对连续的模型族，它们强烈依赖于含糊的先验（Lindley 悖论，例 8.8.2；八所学校，例 8.8.3），包含各备择的层次模型通常更可取。
- 在八所学校的例子中，无合并显然最差，完全合并与层次模型在预测精度上无法区分；层次模型的有效参数个数为 $1$–$3$，远低于它的十个参数。

## 思考题

1. 一个模型拟合两个观测，保留三个后验抽样。似然值 $p(y_i\mid\theta^s)$ 为

   | $s$ | $p(y_1\mid\theta^s)$ | $p(y_2\mid\theta^s)$ |
   |---|---|---|
   | 1 | $0.20$ | $0.10$ |
   | 2 | $0.30$ | $0.05$ |
   | 3 | $0.10$ | $0.15$ |

   且在后验均值处 $p(y_1\mid\hat\theta_{\mathrm{Bayes}})=0.22$，$p(y_2\mid\hat\theta_{\mathrm{Bayes}})=0.11$。计算 lppd、$p_{\mathrm{WAIC}1}$、$p_{\mathrm{WAIC}2}$（样本方差，除数为 $S-1$）、WAIC、$p_{\mathrm{DIC}}$ 与 DIC。

   **答** 似然的后验均值为 $0.2$ 与 $0.1$，所以 $\mathrm{lppd}=\log0.2+\log0.1=\log0.02=-3.912$。对数似然在各次抽样上的均值为 $\frac13(\log0.2+\log0.3+\log0.1)=-1.705$ 与 $\frac13(\log0.1+\log0.05+\log0.15)=-2.399$，所以 $p_{\mathrm{WAIC}1}=2\big[(-1.609+1.705)+(-2.303+2.399)\big]=0.384$。$\log p(y_1\mid\theta^s)$ 与 $\log p(y_2\mid\theta^s)$ 的样本方差都是 $0.309$，所以 $p_{\mathrm{WAIC}2}=0.617$。于是用 $p_{\mathrm{WAIC}1}$ 时 $\mathrm{WAIC}=-2(-3.912-0.384)=8.59$，用 $p_{\mathrm{WAIC}2}$ 时为 $-2(-3.912-0.617)=9.06$。对 DIC，$\log p(y\mid\hat\theta_{\mathrm{Bayes}})=\log(0.22\cdot0.11)=-3.722$，而 $\log p(y\mid\theta^s)=\log p(y_1\mid\theta^s)+\log p(y_2\mid\theta^s)$ 的后验均值为 $-1.705-2.399=-4.104$，所以 $p_{\mathrm{DIC}}=2(-3.722+4.104)=0.765$，$\mathrm{DIC}=-2(-3.722)+2(0.765)=8.97$。
2. 在例 8.8.1 中，设这位女性有三个儿子且都未患病。求 $H_2$（不是携带者）相对于 $H_1$（是携带者）的贝叶斯因子、她是携带者的后验概率，以及以 $H_2$ 为零模型时在 Jeffreys 尺度上的等级。若有一个儿子患病，结果如何？

   **答** $p(y\mid H_1)=(\frac12)^3=0.125$，$p(y\mid H_2)=1$，所以 $\mathrm{BF}(H_2;H_1)=8$；先验优势比为 $1$ 时，$\mathbb{P}(\theta=1\mid y)=1/(1+8)=0.111$。由于 $B(y)=8\ge1$，数据支持零模型 $H_2$。若有一个儿子患病，则 $p(y\mid H_2)=0$（非携带者不可能有患病的儿子，不考虑新发突变），贝叶斯因子为 $0$，她是携带者的后验概率为 $1$：对 $H_2$ 是决定性的不利证据。
3. 两个嵌套的回归模型拟合 $n=50$ 个观测：模型 1 有 $k_1=2$ 个参数，最大化对数似然为 $-120.3$；模型 2 有 $k_2=4$ 个参数，为 $-117.9$。用 AIC 与 BIC 比较它们，并近似模型 2 相对于模型 1 的贝叶斯因子。解释两个准则为何不一致。

   **答** $\mathrm{AIC}_1=240.6+4=244.6$，$\mathrm{AIC}_2=235.8+8=243.8$：AIC 略微偏好模型 2，但差 $0.8<2$，不算实质差别。取 $\log50=3.912$，$\mathrm{BIC}_1=240.6+2(3.912)=248.4$，$\mathrm{BIC}_2=235.8+4(3.912)=251.4$：BIC 以 $3.0$ 的差距偏好模型 1。由 §8.8.6，$\mathrm{BF}(2;1)\approx\mathrm{e}^{-3.02/2}=0.22$：数据以约 $4.5$ 倍的优势偏向更简单的模型 1。每个参数的惩罚在 AIC 下是 $2$，在 BIC 下是 $\log n=3.9$：对数似然提高 $2.4$，按 AIC 的预测准则足以买下两个额外参数，按 BIC 识别真实模型的准则则不够。
4. 对八所学校的无合并模型，$y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma_j^2)$，$p(\theta)\propto1$，$J=8$，精确计算 $p_{\mathrm{DIC}}$、$p_{\mathrm{WAIC}1}$ 与 $p_{\mathrm{WAIC}2}$。

   **答** 后验为 $\theta_j\mid y\sim\mathcal{N}(y_j,\sigma_j^2)$，所以 $Z_j=(y_j-\theta_j)/\sigma_j\sim\mathcal{N}(0,1)$ 且相互独立，$\log p(y_j\mid\theta_j)=-\frac12\log(2\pi\sigma_j^2)-\frac12Z_j^2$。*DIC*：$\hat\theta_{\mathrm{Bayes}}=y$，所以 $p_{\mathrm{DIC}}=2\sum_j\mathbb{E}(\frac12Z_j^2)=J=8$。*WAIC1*：$\mathbb{E}_{\mathrm{post}}p(y_j\mid\theta_j)=\mathcal{N}(y_j\mid y_j,2\sigma_j^2)=(4\pi\sigma_j^2)^{-1/2}$，所以每一项为 $2\big[-\frac12\log(4\pi\sigma_j^2)+\frac12\log(2\pi\sigma_j^2)+\frac12\big]=1-\log2$，$p_{\mathrm{WAIC}1}=8(1-\log2)=2.45$。*WAIC2*：$\operatorname{Var}(\frac12Z_j^2)=\frac14\cdot2=\frac12$，所以 $p_{\mathrm{WAIC}2}=4$。只有 DIC 数到了全部八个参数；当每个观测都有自己的参数时，WAIC 的逐点校正低估了乐观偏差。
5. 证明在例 8.8.3 中，取先验 $\mathcal{N}(0,A^2)$ 时，贝叶斯因子 $p(y\mid H_2)/p(y\mid H_1)$ 当 $A\to\infty$ 时按 $A^{J-1}$ 增长。为什么取平坦先验时贝叶斯因子没有定义？

   **答** 在 $H_1$ 下，$y_j\sim\mathcal{N}(0,\sigma_j^2+A^2)$ 相互独立，所以 $p(y\mid H_1)=\prod_j\big(2\pi(\sigma_j^2+A^2)\big)^{-1/2}\exp\big(-\frac{y_j^2}{2(\sigma_j^2+A^2)}\big)\sim(2\pi A^2)^{-J/2}$。在 $H_2$ 下，$p(y\mid H_2)=\int\prod_j\mathcal{N}(y_j\mid\theta,\sigma_j^2)\,\mathcal{N}(\theta\mid0,A^2)\,\mathrm{d}\theta$；对大的 $A$，在似然不可忽略的区域上先验密度近似为常数 $(2\pi A^2)^{-1/2}$，所以 $p(y\mid H_2)\sim(2\pi A^2)^{-1/2}\int\prod_j\mathcal{N}(y_j\mid\theta,\sigma_j^2)\,\mathrm{d}\theta$，即一个常数乘以 $A^{-1}$。比值按 $(2\pi A^2)^{(J-1)/2}\propto A^{J-1}$ 增长。取平坦先验时，$p(\theta)\propto1$ 意味着 $p(\theta)=c$，$c>0$ 任意，它把 $p(y\mid H)$ 乘以 $c$（对 $J$ 个参数则乘以 $c^J$）；两个边际密度带有互不相关的任意因子，所以它们的比值可以取任何值。上面的计算把这一点具体化了：让正常先验趋于平坦，比值以由维数之差决定的速率趋于无穷。
6. 在例 8.8.2 中，按近似式 $\mathrm{BF}\approx\sqrt n\,\mathrm{e}^{-z^2/2}$ 与精确公式，$n$ 要多大才能使 $z=1.96$ 的数据偏向 $H_0$？

   **答** 近似式给出，当 $\log n>z^2=3.84$，即 $n>\mathrm{e}^{3.84}\approx47$ 时，$\mathrm{BF}(H_0;H_1)>1$。精确的贝叶斯因子 $\sqrt{n+1}\exp\big(-\frac{z^2n}{2(n+1)}\big)$ 在 $n\approx42$ 时等于 $1$。超过约 $40$ 个观测后，恰好在 $5\%$ 水平显著的结果在这个先验下是支持零假设的证据。
7. 对二项观测 $n$ 次中 $y$ 次，取 $\theta$ 的均匀先验，精确的边际似然为 $p(y)=1/(n+1)$（[3.7.1](/3.7.1)）。推导 $p(y)$ 的 Laplace 近似，并对 $n=20$，$y=7$ 计算二者。

   **答** 取 $g(\theta)=\log\binom ny+y\log\theta+(n-y)\log(1-\theta)$，众数为 $\tilde\theta=y/n$，$-g''(\tilde\theta)=\frac{y}{\tilde\theta^2}+\frac{n-y}{(1-\tilde\theta)^2}=\frac{n}{\tilde\theta(1-\tilde\theta)}$。因此

   $$
   p(y)\approx\binom ny\tilde\theta^y(1-\tilde\theta)^{n-y}\sqrt{\frac{2\pi\tilde\theta(1-\tilde\theta)}{n}}.
   $$
   当 $n=20$，$y=7$，$\tilde\theta=0.35$ 时，它为 $0.0493$，精确值为 $1/21=0.0476$：相对误差为 $3.5\%$，并随 $n$ 增大而减小（这就是 Beta 函数中 Stirling 公式的误差）。
8. 解释为什么 AIC 对八所学校的层次模型没有定义，而 DIC 与 WAIC 有。你会报告所算出的哪些准则，为什么？

   **答** AIC 需要极大似然估计与参数个数 $k$。在层次模型中，$\theta_j$ 受其总体分布的约束，所以参数个数既不是 $10$（$\theta_1,\dots,\theta_8,\mu,\tau$），也不是 $2$，并且把 $\theta_j$ 积分掉之后对 $(\mu,\tau)$ 的似然最大值没有计入 $\tau$ 的后验不确定性。DIC 与 WAIC 由后验模拟估计有效参数个数（$p_{\mathrm{DIC}}=2.8$，$p_{\mathrm{WAIC}2}=1.3$），所以能适应合并的程度。我会报告用 $p_{\mathrm{WAIC}2}$ 的 WAIC，同时报告精确的或重要性抽样的 LOO-CV：它们是完全贝叶斯的，对参数化不变，并且估计的是实际使用的后验预测分布的预测精度；对这个小数据集，完全合并与层次模型之间小于 $2$ 的差别应当报告为没有真正的差别。
