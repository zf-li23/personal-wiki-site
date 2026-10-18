---
title: 额外平方和与一般线性检验
description: 额外平方和与三种类型的平方和，嵌套模型与线性假设的一般线性检验，偏决定系数、偏相关系数与 Frisch–Waugh–Lovell 定理，标准化回归模型，以及抑制变量。
source_hash: 319cc5f49b9b
---

在多元回归中，回归平方和度量全部解释变量合起来能解释多少。要评价单个变量或一组变量，我们需要的是它们在其他变量之外*额外*解释的那部分变异。本章引入这种额外平方和，以及软件拆分回归平方和的三种方式（第 I、II、III 类）。完全模型与简化模型的比较在 [3.3.4](/3.3.4) 中对简单回归出现过，在 [3.3.8](/3.3.8) 中被非正式地使用，这里成为一般线性检验，它涵盖单个系数、一组系数以及任意线性假设。额外平方和除以尚未解释的变异就得到偏决定系数，其平方根是偏相关系数；Frisch–Waugh–Lovell 定理表明二者都来自残差对残差的回归。本章最后讨论使系数可比的标准化回归模型，以及抑制变量——它解释了为什么一个变量在另一个变量存在时反而更重要。这里看到的大多数现象都源于解释变量之间的相关，这是 [3.3.10](/3.3.10) 的主题。

## 9.1. 额外平方和

### 9.1.1. 定义

向模型中加入解释变量时，我们希望多解释一些响应的变异，从而减少误差。额外平方和量化这种收益：它既可以看作回归平方和 $\mathrm{SSR}$ 的增加，也可以等价地看作误差平方和 $\mathrm{SSE}$ 的减少；二者相同，因为 $\mathrm{SSR}+\mathrm{SSE}=\mathrm{SSTO}$ 与模型无关。记 $\mathrm{SSR}(X_1,X_2)$ 和 $\mathrm{SSE}(X_1,X_2)$ 为含 $X_1$、$X_2$（以及截距）的模型的平方和。

**定义 9.1.1（额外平方和）** 对两个不相交的解释变量集合 $A$ 和 $B$，给定 $B$ 时 $A$ 的**额外平方和**为

$$
\mathrm{SSR}(A\mid B)=\mathrm{SSR}(A,B)-\mathrm{SSR}(B)=\mathrm{SSE}(B)-\mathrm{SSE}(A,B),
$$
即把 $A$ 加入已含 $B$ 的模型时额外解释的变异。它的自由度是 $A$ 中变量的个数。

例如，$\mathrm{SSR}(X_1,X_2,X_3)$ 是 $X_1,X_2,X_3$ 解释的全部变异；$\mathrm{SSR}(X_1\mid X_2)=\mathrm{SSE}(X_2)-\mathrm{SSE}(X_1,X_2)$ 是把 $X_1$ 加入含 $X_2$ 的模型时额外解释的变异；而

$$
\mathrm{SSR}(X_1,X_4\mid X_2,X_3)=\mathrm{SSR}(X_1,X_2,X_3,X_4)-\mathrm{SSR}(X_2,X_3)=\mathrm{SSE}(X_2,X_3)-\mathrm{SSE}(X_1,X_2,X_3,X_4)
$$
是 $\mathrm{SSE}(X_2,X_3)$ 中由 $X_1$ 与 $X_4$ 解释、而 $X_2$ 与 $X_3$ 未能解释的部分。

**例 9.1.1（体脂）** 对 $20$ 名健康女性，要用三项廉价的身体测量——三头肌皮褶厚度 $X_1$、大腿围 $X_2$ 和上臂中部围 $X_3$——来预测体脂 $Y$（由昂贵的金标准水下称重法测得）。总平方和 $\mathrm{SSTO}=495.39$，且

| 模型 | $\mathrm{SSR}$ | $\mathrm{SSE}$ |
|---|---|---|
| $X_1$ | $352.27$ | $143.12$ |
| $X_2$ | $381.97$ | $113.42$ |
| $X_1,X_2$ | $385.44$ | $109.95$ |
| $X_1,X_2,X_3$ | $396.98$ | $98.41$ |

于是 $\mathrm{SSR}(X_2\mid X_1)=143.12-109.95=33.17$，而 $\mathrm{SSR}(X_1\mid X_2)=113.42-109.95=3.47$，$\mathrm{SSR}(X_3\mid X_1,X_2)=109.95-98.41=11.54$。皮褶厚度单独能解释很多（$352.27$），一旦大腿围在模型中，它几乎不再解释什么（$3.47$）：两项测量携带的信息几乎相同。

![体脂数据的总平方和 495.39 按两种顺序拆分：X1 在先给出 SSR(X1) = 352.27 与 SSR(X2 | X1) = 33.17，X2 在先给出 SSR(X2) = 381.97 与 SSR(X1 | X2) = 3.47；两种顺序下 SSE(X1, X2) 都是 109.95](./plots/extra-ss-bars.py)

### 9.1.2. 三种类型的平方和

**方差分析**把响应的总变异拆分成若干来源，以便判断每个解释变量的作用。对 $Y\sim X_1+X_2+X_3+X_4$，有 $\mathrm{SSTO}=\mathrm{SSR}(X_1,\dots,X_4)+\mathrm{SSE}(X_1,\dots,X_4)$，但 $\mathrm{SSR}(X_1,\dots,X_4)$ 应该怎样分摊给各个变量？常见的答案有三种。

**定义 9.1.2（平方和的类型）** 在含项 $T_1,\dots,T_m$（变量，或交互作用等变量组）的模型中，

1. **序贯平方和**（第 I 类）按给定顺序逐项加入：$\mathrm{SSR}(T_1)$、$\mathrm{SSR}(T_2\mid T_1)$、$\mathrm{SSR}(T_3\mid T_1,T_2)$，依此类推；
2. 一项的第 II 类平方和是给定除包含它的项（如它的交互作用）之外所有其他项时的额外平方和；
3. 一项的第 III 类平方和是给定所有其他项时的额外平方和，即该项最后加入。

只有序贯平方和加起来等于回归平方和：

$$
\mathrm{SSR}(X_1,X_2,X_3,X_4)=\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2\mid X_1)+\mathrm{SSR}(X_3\mid X_1,X_2)+\mathrm{SSR}(X_4\mid X_1,X_2,X_3).
$$
这就是 R 的 `anova()` 输出的"扩展的"方差分析表：原来的一行回归被拆成 $p-1$ 行，每个变量一行，各有一个自由度，统计量为 $F^*=\mathrm{SSR}(X_k\mid X_1,\dots,X_{k-1})/\mathrm{MSE}\overset{H_0}{\sim}F_{1,n-p}$，其中 $\mathrm{MSE}$ 取自完全模型。顺序是重要的：先进入的变量会占去与后面变量共有的那部分变异。

对两个因子 $A$、$B$ 及其交互作用 $AB$，三种类型为

| 项 | 第 I 类 | 第 II 类 | 第 III 类 |
|---|---|---|---|
| $A$ | $\mathrm{SSR}(A)$ | $\mathrm{SSR}(A\mid B)$ | $\mathrm{SSR}(A\mid B,AB)$ |
| $B$ | $\mathrm{SSR}(B\mid A)$ | $\mathrm{SSR}(B\mid A)$ | $\mathrm{SSR}(B\mid A,AB)$ |
| $AB$ | $\mathrm{SSR}(AB\mid A,B)$ | $\mathrm{SSR}(AB\mid A,B)$ | $\mathrm{SSR}(AB\mid A,B)$ |

第 II 类在评价主效应时假定没有显著的交互作用。因此：

- 改变模型中变量的顺序会改变第 I 类平方和，但不改变第 II 类和第 III 类平方和；
- 在没有交互项的模型中，第 II 类与第 III 类相同，都是 $t$ 检验背后的"最后加入变量"平方和；
- 对正交的解释变量（以及方差分析中的平衡设计），三种类型完全相同；变量相关或数据不平衡时，它们可能相差很大。

在 R 中，`anova()` 给出第 I 类；程序包 car 的 `Anova()` 默认给出第 II 类，`type = "III"` 时给出第 III 类；SAS 与 SPSS 默认报告第 III 类。该用哪一种？当有实质性理由优先考虑某个变量时（例如在控制已知变量之后检验某个特定变量的作用，就让它最后进入），第 I 类是合适的。否则，预计没有交互作用时用第 II 类，有交互作用时用第 III 类。像第 III 类那样在有交互作用时检验主效应，违反了试验设计中的边际性原则（marginality principle）：一个主效应在与之交互的因子的各水平上取平均，很少有意义（[3.3.14](/3.3.14)）。第 III 类的结果还依赖于因子的编码方式。

## 9.2. 一般线性检验

### 9.2.1. 完全模型与简化模型

[3.3.4](/3.3.4) 的一般线性检验比较两个模型：包含全部变量（参数）的完全模型，以及对完全模型施加原假设所得的简化模型。两个模型是嵌套的：完全模型包含简化模型的全部解释变量。例如 $\{X_1,\dots,X_5\}$ 包含 $\{X_1,X_2,X_3\}$，后者又包含 $\{X_1,X_2\}$。检验考察两个模型 $\mathrm{SSE}$（等价地，$\mathrm{SSR}$）之差。

**定义 9.2.1（一般线性检验）** 设简化模型 $R$ 嵌套在完全模型 $F$ 中，误差平方和 $\mathrm{SSE}(R)\ge\mathrm{SSE}(F)$，误差自由度 $\mathrm{df}_E(R)>\mathrm{df}_E(F)$。$H_0$：简化模型成立，对 $H_1$：完全模型成立，其**一般线性检验**使用偏 $F$ 统计量

$$
F^*=\frac{\big(\mathrm{SSE}(R)-\mathrm{SSE}(F)\big)/\big(\mathrm{df}_E(R)-\mathrm{df}_E(F)\big)}{\mathrm{SSE}(F)/\mathrm{df}_E(F)},
$$
$F^*$ 大时拒绝 $H_0$。

**定理 9.2.1** 在正态的完全模型和 $H_0$ 下，$F^*\sim F_{\mathrm{df}_E(R)-\mathrm{df}_E(F),\ \mathrm{df}_E(F)}$。

**证明** 设 $H_R$、$H_F$ 为两个模型的帽子矩阵；由 $\mathcal{R}(X_R)\subseteq\mathcal{R}(X_F)$ 得 $H_FH_R=H_R$，所以 $H_F-H_R$ 对称幂等，秩为 $q=\mathrm{df}_E(R)-\mathrm{df}_E(F)$，且 $(I_n-H_F)(H_F-H_R)=O$。现在 $\mathrm{SSE}(R)-\mathrm{SSE}(F)=\boldsymbol{Y}^{\mathsf T}(H_F-H_R)\boldsymbol{Y}$，$\mathrm{SSE}(F)=\boldsymbol{Y}^{\mathsf T}(I_n-H_F)\boldsymbol{Y}$。在 $H_0$ 下 $\mathbb{E}(\boldsymbol{Y})\in\mathcal{R}(X_R)$ 被两个矩阵都化为零，故由 [3.3.8](/3.3.8) 的引理 8.2.1，两个二次型除以 $\sigma^2$ 后分别服从 $\chi^2_q$ 与 $\chi^2_{\mathrm{df}_E(F)}$；又因 $(H_F-H_R)\boldsymbol{Y}$ 与 $(I_n-H_F)\boldsymbol{Y}$ 联合正态且不相关，二者独立。$\square$

分子自由度是*额外*变量的个数，分母自由度是较大模型的误差自由度。例如 $n=100$ 时比较 $X_1,\dots,X_5$ 与 $X_1,X_2,X_3$，即检验 $H_0\colon\beta_4=\beta_5=0$ 对 $H_1$：$\beta_4,\beta_5$ 至少有一个不为零，

$$
F^*=\frac{\mathrm{SSR}(X_4,X_5\mid X_1,X_2,X_3)/2}{\mathrm{SSE}(X_1,\dots,X_5)/(n-6)}\overset{H_0}{\sim}F_{2,94}.
$$
拒绝 $H_0$（比如 $p$ 值 $\le0.05$）意味着：在已含 $X_1,X_2,X_3$ 的线性模型中，$X_4$ 或 $X_5$ 或二者包含对预测 $Y$ 有用的额外信息。

由于两个模型的 $\mathrm{SSTO}$ 相同，这个统计量也可以用复决定系数写出：

$$
F^*=\frac{\big(R^2(F)-R^2(R)\big)/\big(\mathrm{df}_E(R)-\mathrm{df}_E(F)\big)}{\big(1-R^2(F)\big)/\mathrm{df}_E(F)}.
$$

### 9.2.2. 特殊情形

**命题 9.2.1** 设 $c_{kk}=[(X^{\mathsf T}X)^{-1}]_{kk}$ 是完全模型中 $\beta_k$ 对应的对角元。则

$$
\mathrm{SSR}(X_k\mid X_1,\dots,X_{k-1},X_{k+1},\dots,X_{p-1})=\frac{b_k^2}{c_{kk}},
$$
所以 $H_0\colon\beta_k=0$ 的一般线性检验的统计量为 $F^*=b_k^2/(c_{kk}\,\mathrm{MSE})=(t^*)^2$，即 [3.3.8](/3.3.8) 中 $t$ 统计量的平方，且 $F_{1,n-p}=t_{n-p}^2$：两个检验等价。

**证明** 把列排成 $X=(X_{-k},\boldsymbol{x}_k)$，设 $H_{-k}$ 为 $X_{-k}$ 的帽子矩阵，$\tilde{\boldsymbol{x}}=(I_n-H_{-k})\boldsymbol{x}_k$ 为 $\boldsymbol{x}_k$ 对其余各列回归的残差。$X$ 的列空间是 $\mathcal{R}(X_{-k})$ 与 $\tilde{\boldsymbol{x}}$ 张成的直线的正交和，因此 $H=H_{-k}+\tilde{\boldsymbol{x}}\tilde{\boldsymbol{x}}^{\mathsf T}/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$，且

$$
\mathrm{SSE}(X_{-k})-\mathrm{SSE}(X)=\boldsymbol{Y}^{\mathsf T}(H-H_{-k})\boldsymbol{Y}=\frac{(\tilde{\boldsymbol{x}}^{\mathsf T}\boldsymbol{Y})^2}{\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}}}.
$$
由下面的定理 9.3.1，$b_k=\tilde{\boldsymbol{x}}^{\mathsf T}\boldsymbol{Y}/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$；由分块求逆公式（$X^{\mathsf T}X$ 中 $X_{-k}^{\mathsf T}X_{-k}$ 的 **Schur 补**），$c_{kk}=\big(\boldsymbol{x}_k^{\mathsf T}\boldsymbol{x}_k-\boldsymbol{x}_k^{\mathsf T}H_{-k}\boldsymbol{x}_k\big)^{-1}=1/(\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}})$。因此额外平方和等于 $b_k^2\,\tilde{\boldsymbol{x}}^{\mathsf T}\tilde{\boldsymbol{x}}=b_k^2/c_{kk}$。$\square$

这个恒等式也补全了 [3.2.5](/3.2.5) 中"单个系数的似然比检验就是 $t$ 检验"的证明。另一极端，对 $H_0\colon\beta_1=\cdots=\beta_{p-1}=0$，简化模型只含截距，$\mathrm{SSE}(R)=\mathrm{SSTO}$，一般线性检验就是总体方差分析 $F$ 检验。

### 9.2.3. 实例：体脂

```r
reg1 <- lm(fat ~ skinfold + thigh + midarm, data = a1)
summary(reg1)
anova(reg1)                      # Type I (sequential) sums of squares
library(car)
Anova(reg1, type = "II")         # Type II
Anova(reg1, type = "III")        # Type III
drop1(reg1, test = "F")          # each variable deleted from the full model
```

**例 9.2.1（体脂，续）** 完全模型的拟合结果与各类平方和为

| | 估计 | 标准误 | $t$ | $p$ 值 | 第 I 类 SS | 第 II/III 类 SS |
|---|---|---|---|---|---|---|
| 截距 | $117.085$ | $99.782$ | $1.17$ | $0.258$ | | |
| 皮褶 $X_1$ | $4.334$ | $3.016$ | $1.44$ | $0.170$ | $352.27$ | $12.705$ |
| 大腿 $X_2$ | $-2.857$ | $2.582$ | $-1.11$ | $0.285$ | $33.17$ | $7.529$ |
| 上臂 $X_3$ | $-2.186$ | $1.595$ | $-1.37$ | $0.190$ | $11.55$ | $11.546$ |

其中 $\mathrm{SSE}=98.40$（自由度 $16$，$\mathrm{MSE}=6.15$，$s=2.48$），$R^2=0.8014$，$R_a^2=0.7641$，$F^*=21.52$（自由度 $(3,16)$，$p=7.3\times10^{-6}$）。这组变量作为整体非常有用，却没有一个单独显著。皮褶和大腿先进入，第 I 类平方和很大；而二者的第 II 类与第 III 类平方和（这里没有交互作用，二者相等）都很小：其他变量在模型中时，每个变量都增加不了多少。

三个变量与体脂的边际相关系数分别为 $0.843$（皮褶）、$0.878$（大腿）和 $0.142$（上臂，$p=0.55$）。能否去掉相关最弱的上臂，并认为大腿最重要？仅凭这些证据不能：边际相关忽略了解释变量之间的关系。要评价上臂，应把完全模型与去掉它的模型相比较：

```r
reg3 <- lm(fat ~ skinfold + thigh, data = a1)
anova(reg3, reg1)    # general linear test of H0: beta_3 = 0
```

结果为 $\mathrm{SSR}(X_3\mid X_1,X_2)=109.951-98.405=11.546$（自由度 $1$），$F^*=11.546/6.150=1.877$，$p=0.190$，恰好就是完全模型中上臂的 $t$ 检验（$(-1.370)^2=1.877$）。皮褶和大腿在模型中时，上臂不是显著的预测变量。

解释时要小心。$t$ 检验评价的是在*已考虑* $X_1$ 和 $X_2$ 之后 $X_3$ 的显著性，它并不检验 $Y$ 与 $X_3$ 单独的关系。这正是**偏回归系数** $\beta_3$ 的含义：其他变量保持不变时，$X_3$ 每增加一个单位 $\mathbb{E}(Y)$ 的变化。对变量子集的偏 $F$ 检验与总体 $F$ 检验回答的是不同的问题。

皮褶单独是高度显著的线性预测变量：$\hat Y=-1.496+0.857X_1$，$t=6.66$，$R^2=0.711$，$\mathrm{SSE}=143.12$（自由度 $18$）。另外两个变量在皮褶之外还有贡献吗？$H_0\colon\beta_2=\beta_3=0$ 的一般线性检验给出 $\mathrm{SSR}(X_2,X_3\mid X_1)=143.120-98.405=44.715$（自由度 $2$），$F^*=(44.715/2)/6.150=3.635$，$p=0.0500$：它们确有帮助，处于边缘。也许最好的模型包含两个预测变量（[3.3.10](/3.3.10)）。

两点实践上的说明。通常备择假设只是原假设中那组变量至少有一个起作用；而且我们往往希望不拒绝，因为目标是剔除不必要的变量。这时功效和样本量至关重要：样本太小，可能错误地删去变量。在 [3.3.8](/3.3.8) 的例 8.1.1 中，$n=224$，向 hsm 和 hse 加入 hss、satm、satv 的 $p$ 值为 $0.436$，足以支持舍弃它们。

### 9.2.4. 线性假设

一般线性检验适用于关于系数线性组合的任何假设。在体脂模型中，$H_0\colon\beta_2=\beta_3$ 对应简化模型 $Y=\beta_0+\beta_1X_1+\beta_c(X_2+X_3)+\varepsilon$；$H_0\colon\beta_2=2$ 对应把已知项 $2X_2$ 移到左边（作为偏移量）的简化模型：

```r
glt1 <- lm(fat ~ skinfold + I(thigh + midarm), data = a1)
anova(glt1, reg1)                                    # H0: beta_2 = beta_3
glt2 <- lm(fat ~ skinfold + offset(2 * thigh) + midarm, data = a1)
anova(glt2, reg1)                                    # H0: beta_2 = 2
linearHypothesis(reg1, "thigh - 3*midarm = 12")      # package car
```

一般地，$q$ 个线性约束写成 $H_0\colon C\boldsymbol{\beta}=\boldsymbol{t}$，其中 $C$ 是秩为 $q$（线性无关约束的个数）的 $q\times p$ 矩阵，$\boldsymbol{t}\in\mathbb{R}^q$。

**定理 9.2.2** 在正态线性模型和 $H_0\colon C\boldsymbol{\beta}=\boldsymbol{t}$ 下，

$$
F^*=\frac{(C\boldsymbol{b}-\boldsymbol{t})^{\mathsf T}\big(C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)^{-1}(C\boldsymbol{b}-\boldsymbol{t})}{q\,s^2}\sim F_{q,n-p},
$$
且分子 $q\,s^2F^*$ 等于 $\mathrm{SSE}(R)-\mathrm{SSE}(F)$，其中 $R$ 是在约束下拟合的模型。

**证明** 由 [3.3.8](/3.3.8) 的定理 8.2.1，在 $H_0$ 下 $C\boldsymbol{b}-\boldsymbol{t}\sim\mathcal{N}_q\big(\boldsymbol{0},\sigma^2C(X^{\mathsf T}X)^{-1}C^{\mathsf T}\big)$，所以分子中的二次型除以 $\sigma^2$ 服从 $\chi^2_q$；它是 $\boldsymbol{b}$ 的函数，因而与 $(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$ 独立。分子等于 $\mathrm{SSE}$ 的增量，可以用 Lagrange 乘子在约束 $C\boldsymbol{\beta}=\boldsymbol{t}$ 下极小化 $\|\boldsymbol{Y}-X\boldsymbol{\beta}\|^2$ 得到。$\square$

**例 9.2.2** 对体脂模型，$\boldsymbol{\beta}=(\beta_0,\beta_1,\beta_2,\beta_3)^{\mathsf T}$，假设 $H_0\colon\beta_2-3\beta_3=12$ 给出 $\mathrm{SSE}(R)=182.953$（自由度 $17$），故 $F^*=(182.953-98.405)/6.150=13.75$（自由度 $(1,16)$），$p=0.0019$。两个约束 $\beta_2=\beta_3$ 与 $\beta_2-3\beta_3=12$ 合起来对应

$$
C=\begin{bmatrix}0&0&1&-1\\0&0&1&-3\end{bmatrix},\qquad\boldsymbol{t}=\begin{bmatrix}0\\12\end{bmatrix},\qquad q=2,
$$
给出 $\mathrm{SSE}(R)=816.2$（自由度 $18$），$F^*=58.35$（自由度 $(2,16)$），$p=4.5\times10^{-8}$：

```r
C <- matrix(c(0, 0, 1, -1,
              0, 0, 1, -3), byrow = TRUE, nrow = 2)
linearHypothesis(reg1, hypothesis.matrix = C, rhs = c(0, 12))
```

定理 9.2.2 的统计量与 [3.4.7](/3.4.7) 中 $F$ 检验的二次型相同，结构上与 Hotelling $T^2$ 一致：它是 $C\boldsymbol{b}$ 与 $\boldsymbol{t}$ 在其估计协方差矩阵度量下距离的平方。

## 9.3. 偏决定系数与偏相关系数

### 9.3.1. 偏决定系数

复决定系数 $R^2=\mathrm{SSR}(X_1,\dots,X_{p-1})/\mathrm{SSTO}$ 是模型解释的变异占总变异的比例，即引入整组解释变量后 $Y$ 的变异减少的比例。偏决定系数则度量在其他变量都已进入模型时，一个变量的边际贡献：它解释的变异占*剩余*变异的比例。

**定义 9.3.1（偏决定系数）** 给定其他变量 $X_{-k}=\{X_j\colon j\ne k\}$ 时，$Y$ 与 $X_k$ 的**偏决定系数**为

$$
R^2_{Yk\mid-k}=\frac{\mathrm{SSR}(X_k\mid X_{-k})}{\mathrm{SSE}(X_{-k})}=\frac{\mathrm{SSE}(X_{-k})-\mathrm{SSE}(X_1,\dots,X_{p-1})}{\mathrm{SSE}(X_{-k})}\in[0,1].
$$
竖线后面是被控制的变量，例如 $R^2_{Y1\mid23}=\mathrm{SSR}(X_1\mid X_2,X_3)/\mathrm{SSE}(X_2,X_3)$。同样的定义适用于一组变量；在方差分析中这个量称为偏 $\eta^2$。

在以 $Y$、$X_1$、$X_2$ 为圆的 Venn 图中，设 $A$ 是 $Y$ 只与 $X_1$ 共有的部分，$B$ 是只与 $X_2$ 共有的部分，$C$ 是与二者都共有的部分，$D$ 是与二者都不共有的部分。则 $R^2=(A+B+C)/(A+B+C+D)$，$R^2_{Y1\mid2}=A/(A+D)$，$R^2_{Y2\mid1}=B/(B+D)$：重叠部分 $C$ 计入模型，却不计入任何一个偏决定系数。（这幅图只是启发性的；存在抑制变量时（9.4.3 节），重叠部分将不得不为负。）

**例 9.3.1** 在 [3.3.8](/3.3.8) 的例 8.1.1 中，模型 gpa $\sim$ hsm + hss + hse 的序贯平方和为 $25.810$、$1.237$、$0.665$，$\mathrm{SSE}=107.750$。于是

$$
R^2_{\text{gpa, hse}\mid\text{hsm, hss}}=\frac{0.665}{0.665+107.750}=0.0061:
$$
hse 解释了 hsm 和 hss 之后剩余变异的 $0.6\%$。又如，若 $\mathrm{SSTO}=100$，$X_1$ 解释了 $60$，$X_2$ 解释了剩下的 $40$ 中的 $20$，$X_3$ 解释了剩下的 $20$ 中的 $5$，则 $R^2_{Y2\mid1}=20/40=0.5$，$R^2_{Y3\mid12}=5/20=0.25$。

由定义 9.2.1，对 $H_0\colon\beta_k=0$，偏 $F$ 统计量是偏决定系数的单调函数：$F^*=\dfrac{R^2_{Yk\mid-k}}{1-R^2_{Yk\mid-k}}\cdot(n-p)$。

偏决定系数可以直接解释为一个普通的 $R^2$。记 $Y\mid X_{-k}$ 为 $Y$ 对 $X_{-k}$ 回归的残差，$X_k\mid X_{-k}$ 为 $X_k$ 对 $X_{-k}$ 回归的残差：它们是 $Y$ 和 $X_k$ 中其他变量不能解释的部分。

**定理 9.3.1（Frisch–Waugh–Lovell 定理）** 把 $X=(X_1,X_2)$ 按列分块，其中 $X_1$ 含截距，令 $M_1=I_n-X_1(X_1^{\mathsf T}X_1)^{-1}X_1^{\mathsf T}$。则在 $\boldsymbol{Y}$ 对 $X$ 的回归中，$X_2$ 的最小二乘系数 $\boldsymbol{b}_2$ 等于残差 $M_1\boldsymbol{Y}$ 对残差 $M_1X_2$ 回归的系数：

$$
\boldsymbol{b}_2=(X_2^{\mathsf T}M_1X_2)^{-1}X_2^{\mathsf T}M_1\boldsymbol{Y},
$$
而且两个回归的残差相同。

**证明** $M_1X_2$ 的各列与 $\mathcal{R}(X_1)$ 正交，且 $\mathcal{R}(X)=\mathcal{R}(X_1)\oplus\mathcal{R}(M_1X_2)$ 是正交和。因此到 $\mathcal{R}(X)$ 上的投影为 $H=H_1+P$，其中 $H_1=I_n-M_1$，$P$ 是到 $\mathcal{R}(M_1X_2)$ 上的投影。令 $\boldsymbol{c}=(X_2^{\mathsf T}M_1X_2)^{-1}X_2^{\mathsf T}M_1\boldsymbol{Y}$，则 $P\boldsymbol{Y}=M_1X_2\boldsymbol{c}=X_2\boldsymbol{c}-H_1X_2\boldsymbol{c}$，所以对某个 $\boldsymbol{a}$ 有 $H\boldsymbol{Y}=X_1\boldsymbol{a}+X_2\boldsymbol{c}$。由于 $X$ 列满秩，$H\boldsymbol{Y}=X\boldsymbol{b}$ 的系数唯一，故 $\boldsymbol{b}_2=\boldsymbol{c}$。最后 $\boldsymbol{Y}-H\boldsymbol{Y}=M_1\boldsymbol{Y}-P\boldsymbol{Y}=M_1\boldsymbol{Y}-M_1X_2\boldsymbol{c}$，正是 $M_1\boldsymbol{Y}$ 对 $M_1X_2$ 回归的残差向量。$\square$

**推论 9.3.1** 偏决定系数 $R^2_{Yk\mid-k}$ 是 $Y\mid X_{-k}$ 对 $X_k\mid X_{-k}$ 的简单回归的 $R^2$，该回归的斜率为 $b_k$。

**证明** 在定理 9.3.1 中取 $X_2=\boldsymbol{x}_k$。残差 $M_1\boldsymbol{Y}$ 的均值为零（截距在 $X_1$ 中），所以这个简单回归的总平方和为 $\|M_1\boldsymbol{Y}\|^2=\mathrm{SSE}(X_{-k})$，误差平方和为完全模型的 $\mathrm{SSE}$。因此它的 $R^2$ 为 $1-\mathrm{SSE}(X_1,\dots,X_{p-1})/\mathrm{SSE}(X_{-k})=R^2_{Yk\mid-k}$。$\square$

**例 9.3.2** 对体脂数据，完全模型中皮褶的系数为 $b_1=4.334$。把体脂对大腿和上臂回归的残差，再对皮褶对大腿和上臂回归的残差做回归，得到斜率 $4.334$ 和 $R^2=0.1143$，这就是 $R^2_{Y1\mid23}=12.705/111.11$：

```r
fity <- lm(fat ~ thigh + midarm, data = a1)        # Y | X_{-1}
fitx <- lm(skinfold ~ thigh + midarm, data = a1)   # X_1 | X_{-1}
summary(lm(fity$res ~ fitx$res))                   # slope 4.334, R^2 0.1143
cor(fitx$res, fity$res)^2                          # 0.1143
```

这个简单回归给出的标准误（$2.843$）与完全模型的（$3.016$）略有不同，因为简单回归按 $18$ 而不是 $16$ 个误差自由度计算。三个变量的偏决定系数（程序包 heplots 的 `etasq()`）分别为 $0.114$、$0.071$、$0.105$：最后加入时，皮褶和上臂解释的剩余变异最多。

### 9.3.2. 偏相关系数

**定义 9.3.2（偏相关系数）** 给定 $X_{-k}$ 时 $Y$ 与 $X_k$ 的**偏相关系数** $r_{Yk\mid-k}$ 是残差 $Y\mid X_{-k}$ 与 $X_k\mid X_{-k}$ 的相关系数。等价地，$\lvert r_{Yk\mid-k}\rvert=\sqrt{R^2_{Yk\mid-k}}$，$r_{Yk\mid-k}$ 的符号与 $b_k$ 相同。

等价性就是推论 9.3.1：在简单回归中，$R^2$ 是相关系数的平方，斜率与相关系数同号。偏相关系数度量考虑了其他变量之后两个变量之间线性关系的强度。计算时，用其他 $X$ 预测 $Y$，用其他 $X$ 预测 $X_k$，再求两组残差的相关系数。

对三个变量，若 $0<r_{12\mid3}<r_{12}$，则变量 $3$ 部分地解释了变量 $1$ 与 $2$ 之间的相关。相反的情形 $0<r_{12}<r_{12\mid3}$ 也会出现：控制变量 $3$ 之后关联反而更强，这就是 9.4.3 节的抑制效应。

## 9.4. 标准化回归

### 9.4.1. 相关变换

在 [3.3.8](/3.3.8) 的 Dwaine 影楼模型 $Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\varepsilon_i$ 中，$\beta_1$（每千名年轻人对应的销售额）与 $\beta_2$（每千元收入对应的销售额）的单位不同，大小取决于 $X_1$、$X_2$ 的单位，不能直接比较。此外，当解释变量的数量级相差悬殊时，计算 $(X^{\mathsf T}X)^{-1}$ 可能在数值上不准确。这两个问题都可以用**标准化**解决：中心化（减去均值）加尺度化（除以标准差）。当大多数测量的尺度都是任意的时候，通常更愿意这样做。

**定义 9.4.1（标准化回归模型）** 设 $\bar Y$、$\bar X_k$ 为样本均值，$s_Y=\sqrt{\sum_i(Y_i-\bar Y)^2/(n-1)}$、$s_k=\sqrt{\sum_i(X_{ik}-\bar X_k)^2/(n-1)}$ 为样本标准差。**相关变换**为

$$
Y_i^*=\frac{1}{\sqrt{n-1}}\cdot\frac{Y_i-\bar Y}{s_Y},\qquad X_{ik}^*=\frac{1}{\sqrt{n-1}}\cdot\frac{X_{ik}-\bar X_k}{s_k},\qquad k=1,\dots,p-1,
$$
称不含截距的模型 $Y_i^*=\beta_1^*X_{i1}^*+\cdots+\beta_{p-1}^*X_{i,p-1}^*+\varepsilon_i^*$ 为**标准化回归模型**，其系数 $\beta_k^*$ 称为**标准化回归系数**。

从原模型中减去平均后的模型 $\bar Y=\beta_0+\sum_k\beta_k\bar X_k+\bar\varepsilon$，再除以 $\sqrt{n-1}\,s_Y$，得到

$$
Y_i^*=\sum_{k=1}^{p-1}\frac{s_k}{s_Y}\beta_k\,X_{ik}^*+\frac{\varepsilon_i-\bar\varepsilon}{\sqrt{n-1}\,s_Y},\qquad\text{故}\qquad\beta_k^*=\frac{s_k}{s_Y}\beta_k,\quad\beta_0=\bar Y-\sum_{k=1}^{p-1}\beta_k\bar X_k.
$$
标准化系数没有单位，含义相同——其他变量固定时 $X_k$ 每增加一个标准差，$Y$ 变化多少个标准差——因此可以在直观意义上相互比较（变量相关时要注意 [3.3.10](/3.3.10) 中的问题）。

这个名称来自叉积矩阵。由于 $\sum_iX_{ik}^*X_{il}^*=r_{kl}$ 是 $X_k$ 与 $X_l$ 的样本相关系数，$n\times(p-1)$ 的设计矩阵 $X^*=(X_{ik}^*)$ 满足

$$
X^{*\mathsf T}X^*=r_{XX}=\begin{bmatrix}1&r_{12}&\cdots&r_{1,p-1}\\r_{21}&1&\cdots&r_{2,p-1}\\\vdots&\vdots&\ddots&\vdots\\r_{p-1,1}&r_{p-1,2}&\cdots&1\end{bmatrix},\qquad X^{*\mathsf T}\boldsymbol{Y}^*=\boldsymbol{r}_{YX}=\begin{bmatrix}r_{Y1}\\r_{Y2}\\\vdots\\r_{Y,p-1}\end{bmatrix},
$$
即解释变量的**样本相关矩阵**以及它们与 $Y$ 的相关系数构成的向量，故 $\boldsymbol{b}^*=r_{XX}^{-1}\boldsymbol{r}_{YX}$。所有元素都在 $-1$ 与 $1$ 之间，这避免或减轻了求 $X^{\mathsf T}X$ 逆矩阵时的数值问题。

**命题 9.4.1** 对所有变量做标准化，不改变 $R^2$、$R_a^2$、总体 $F$ 统计量、各斜率的 $t$ 统计量和偏决定系数；各平方和除以 $(n-1)s_Y^2$。只对解释变量做标准化，会改变系数（$b_k$ 变为 $s_kb_k$，相差因子 $\sqrt{n-1}$），但不改变方差分析表和偏决定系数。

**证明** 对解释变量做中心化和尺度变换，不改变含截距的设计矩阵的列空间，因而不改变拟合值和任何平方和；把 $Y$ 乘以常数，所有平方和都乘以该常数的平方，在每个比值中相互抵消。$\square$

这里假定标准化模型带截距拟合，就像对标准化数据使用 `lm()` 那样（此时截距的估计为 $0$）。若不带截距拟合，误差自由度会多算一个，$\mathrm{MSE}$ 和各检验会有极小的变化。

对体脂数据，程序包 QuantPsyc 的 `lm.beta()`，或对 `scale(a1)` 使用 `lm()`，给出标准化系数 $4.264$、$-2.929$、$-1.561$；用 `scale()`（它不含因子 $1/\sqrt{n-1}$）时，平方和 $352.27$、$33.17$、$11.55$、$98.40$ 变为 $13.51$、$1.27$、$0.44$、$3.77$，加起来等于 $n-1=19$，而 $R^2=0.8014$ 和 $F^*=21.52$ 不变。

### 9.4.2. 相关系数与偏相关系数

有两个解释变量时，$r_{XX}^{-1}=\frac{1}{1-r_{12}^2}\begin{bmatrix}1&-r_{12}\\-r_{12}&1\end{bmatrix}$，所以

$$
b_1^*=\frac{r_{Y1}-r_{12}r_{Y2}}{1-r_{12}^2},\qquad b_2^*=\frac{r_{Y2}-r_{12}r_{Y1}}{1-r_{12}^2},\qquad b_k=\frac{s_Y}{s_k}b_k^*.
$$
变换回原尺度，$b_1=\Big(\dfrac{\sum_i(X_{i1}-\bar X_1)(Y_i-\bar Y)}{\sum_i(X_{i1}-\bar X_1)^2}-\dfrac{s_Y}{s_1}r_{12}r_{Y2}\Big)\Big/(1-r_{12}^2)$：它是按 $X_1$ 与 $X_2$ 的相关修正过的简单回归斜率。若 $r_{12}=0$，多元回归系数与简单回归系数相同。

**命题 9.4.2** 有两个解释变量时，

$$
R^2_{Y2\mid1}=r_{Y2\mid1}^2=\frac{(r_{Y2}-r_{Y1}r_{12})^2}{(1-r_{Y1}^2)(1-r_{12}^2)}.
$$

**证明** 在相关变换后的变量中，$Y^*$ 和 $X_2^*$ 对 $X_1^*$ 回归的残差分别为 $\boldsymbol{Y}^*-r_{Y1}\boldsymbol{X}_1^*$ 和 $\boldsymbol{X}_2^*-r_{12}\boldsymbol{X}_1^*$（所有向量长度为 $1$、均值为 $0$）。二者内积为 $r_{Y2}-r_{Y1}r_{12}$，长度的平方为 $1-r_{Y1}^2$ 与 $1-r_{12}^2$；偏相关系数是它们夹角的余弦（定义 9.3.2）。$\square$

把所有下标都再以其他变量为条件，同一公式依然成立，例如 $r_{Y2\mid13}^2=(r_{Y2\mid3}-r_{Y1\mid3}r_{12\mid3})^2/\big((1-r_{Y1\mid3}^2)(1-r_{12\mid3}^2)\big)$。在两个解释变量互不相关、又都与 $Y$ 相关的理想情形下，$b_2$ 在 $Y\sim X_2$ 与 $Y\sim X_1+X_2$ 中相同，但 $R^2_{Y2\mid1}=r_{Y2}^2/(1-r_{Y1}^2)$ 比 $R^2_{Y2}=r_{Y2}^2$ 大：去掉 $X_1$ 解释的变异之后，$X_2$ 的贡献在剩余部分中所占的比例更大。

### 9.4.3. 抑制变量

**定义 9.4.2（抑制变量）** 若 $\mathrm{SSR}(X_2\mid X_1)>\mathrm{SSR}(X_2)$，则称 $X_1$ 为**抑制变量**：有 $X_1$ 在时，$X_2$ 解释的 $Y$ 的变异比它单独时更多。

其想法是：抑制变量压制了另一个解释变量中与 $Y$ 无关的那部分变异。这个条件是对称的：由于 $\mathrm{SSR}(X_2\mid X_1)=\mathrm{SSR}(X_1,X_2)-\mathrm{SSR}(X_1)$，

$$
\mathrm{SSR}(X_2\mid X_1)>\mathrm{SSR}(X_2)\iff\mathrm{SSR}(X_1,X_2)>\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2)\iff\mathrm{SSR}(X_1\mid X_2)>\mathrm{SSR}(X_1),
$$
所以两个变量合起来解释的比各自单独解释的总和还多，每个都是另一个的抑制变量。在 9.3.1 节的 Venn 图中，重叠部分 $C$ 将为负。这个条件蕴含 $R^2_{Y2\mid1}>R^2_{Y2}$，因为 $R^2_{Y2\mid1}=\mathrm{SSR}(X_2\mid X_1)/\mathrm{SSE}(X_1)$ 而 $\mathrm{SSE}(X_1)\le\mathrm{SSTO}$；反之不成立，9.4.2 节末尾的不相关情形就是反例。用相关系数表示，条件为 $R^2>r_{Y1}^2+r_{Y2}^2$；经典的例子是 $r_{Y1}\approx0$ 而 $r_{12}\ne0$，此时 $R^2_{Y2\mid1}\approx r_{Y2}^2/(1-r_{12}^2)>r_{Y2}^2$。

![X1 与 Y 不相关（r_Y1 = 0）、r_Y2 = 0.2、0.3、0.5 时，给定 X1 下 Y 与 X2 的偏决定系数：R^2_{Y2|1} = r_Y2^2 / (1 - r_12^2) 从 r_Y2^2（虚线）出发，随两个解释变量的相关系数 r_12 趋向其最大可取值而增长到接近 1](./plots/suppressor-effect.py)

**例 9.4.1** 在体脂数据中，上臂的 $r_{Y3}=0.14$，而 $r_{13}=0.46$。两种顺序下的序贯平方和为

| 顺序 | 第一个变量 | 第二个变量 | $\mathrm{SSE}$ |
|---|---|---|---|
| 皮褶、上臂 | $\mathrm{SSR}(X_1)=352.27$ | $\mathrm{SSR}(X_3\mid X_1)=37.19$ | $105.93$ |
| 上臂、皮褶 | $\mathrm{SSR}(X_3)=10.05$ | $\mathrm{SSR}(X_1\mid X_3)=379.40$ | $105.93$ |

由于 $\mathrm{SSR}(X_1\mid X_3)=379.40>\mathrm{SSR}(X_1)=352.27$，上臂是皮褶的抑制变量；相应地 $\mathrm{SSR}(X_3\mid X_1)=37.19>\mathrm{SSR}(X_3)=10.05$：在这个两变量模型的序贯方差分析表中（$\mathrm{MSE}=6.23$，自由度 $17$），上臂先进入时不显著（$F=1.61$，$p=0.22$），在皮褶之后进入则显著（$F=5.97$，$p=0.026$）。

## 小结

- 额外平方和 $\mathrm{SSR}(A\mid B)=\mathrm{SSE}(B)-\mathrm{SSE}(A,B)$ 是 $A$ 在 $B$ 之外解释的变异。第 I 类（序贯）平方和加起来等于 $\mathrm{SSR}$，但依赖于顺序；第 II 类与第 III 类对每一项按其他项做调整，与顺序无关；变量正交时三者相同。
- 一般线性检验用 $F^*=\dfrac{(\mathrm{SSE}(R)-\mathrm{SSE}(F))/(\mathrm{df}_E(R)-\mathrm{df}_E(F))}{\mathrm{SSE}(F)/\mathrm{df}_E(F)}$ 比较嵌套模型；特殊情形有 $t$ 检验（$F=t^2$，因为 $\mathrm{SSR}(X_k\mid X_{-k})=b_k^2/c_{kk}$）、总体 $F$ 检验，以及任意线性假设 $C\boldsymbol{\beta}=\boldsymbol{t}$。
- 偏 $R^2$ 和偏相关系数度量一个变量对其他变量剩下的变异的贡献；由 Frisch–Waugh–Lovell 定理，它们来自残差对残差的回归，其斜率就是多元回归系数。
- 标准化系数 $\beta_k^*=(s_k/s_Y)\beta_k$ 没有单位，且 $X^{*\mathsf T}X^*=r_{XX}$；$R^2$ 和各检验不变。
- 抑制变量使另一个变量更有用：$\mathrm{SSR}(X_1,X_2)>\mathrm{SSR}(X_1)+\mathrm{SSR}(X_2)$。
