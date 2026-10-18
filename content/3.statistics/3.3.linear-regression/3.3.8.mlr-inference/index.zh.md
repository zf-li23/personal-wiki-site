---
title: 多元线性回归：实例与推断
description: 用学生数据完成一次完整的多元回归分析（探索、变换、候选模型、嵌套模型的 F 检验），然后给出正态线性模型的分布理论，并以矩阵形式写出系数的 t 检验与置信区间、平均响应的置信区间和预测区间。
source_hash: 45d4e7191248
---

建立简单线性回归模型有一套简短的流程：画图、拟合直线、检验斜率、检查残差。有多个解释变量时，每一步都变难了：候选模型很多，解释变量彼此相关，而且一个变量的系数、标准误和显著性都会随模型中的其他变量而变。本章先完整地分析一个真实数据集，展示这些困难以及通常的应对办法；然后给出正态线性模型的基本分布定理，并用它以矩阵形式重述 [3.3.3](/3.3.3) 与 [3.3.4](/3.3.4) 的推断：单个系数的检验与置信区间、平均响应的置信区间以及新观测的预测区间。矩阵记号和最小二乘估计来自 [3.3.7](/3.3.7)；这里非正式地用到的、以**一般线性检验**比较嵌套模型的方法在 [3.3.9](/3.3.9) 中系统展开，解释变量之间的相关性则是 [3.3.10](/3.3.10) 的主题。

## 8.1. 多元回归实例

### 8.1.1. 问题与数据

**例 8.1.1（计算机专业学生）** 某大学计算机专业的学生退学过多。能否找到在入学时就能获得的、预示学业成功的变量？对 $n=224$ 名学生记录了

| 变量 | 含义 | 取值 |
|---|---|---|
| gpa | 三个学期后的平均绩点（响应 $Y$） | $0.12$ 到 $4.00$ |
| hsm、hss、hse | 高中数学、科学、英语成绩 | 整数 $2$ 到 $10$ |
| satm、satv | SAT 数学与语文成绩 | 整数 $200$ 到 $800$ |
| sex | 性别（另有用途） | $1$、$2$ |

暂不考虑性别，于是有五个解释变量：三门高中成绩和两项 SAT 成绩。

### 8.1.2. 探索与变换

在拟合任何模型之前，先逐个考察变量（汇总统计量和直方图），再成对考察（相关系数和散点图矩阵，R 中的 `pairs()`）。这一阶段有两个问题：响应或解释变量是否需要变换，以及解释变量的分布格局对分析意味着什么。

高度偏斜的分布难以考察：偏斜方向上会出现看似离群的值，而相反方向上的异常值可能被掩盖。偏斜分布的均值不能很好地概括其中心，方差对离群值和偏斜也非常敏感。幂变换能使偏斜分布更对称：开方、取对数或取倒数减轻右偏，平方、立方或更高次幂减轻左偏。对数变换尤其常用，因为

$$
\log Y_1-\log Y_2=\log\Big(1+\frac{Y_1-Y_2}{Y_2}\Big)\approx\frac{Y_1-Y_2}{Y_2}
$$
把绝对变化变成相对变化；而且取正值的响应无法被误差正态的 $Y=X\boldsymbol{\beta}+\varepsilon$ 精确描述，它的对数却可以取任意实数。代价是解释。若 $\log Y=X\boldsymbol{\beta}+\varepsilon$，$X_k$ 的系数估计为 $b_k$，则在其他变量固定时 $X_k$ 每增加一个单位，拟合值 $\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{b}}$ 乘以 $\mathrm{e}^{b_k}$，即变化 $(\mathrm{e}^{b_k}-1)\times100\%$。注意 $\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{b}}$ 估计的是 $Y$ 的中位数而不是均值：误差正态时 $\mathbb{E}(Y)=\mathrm{e}^{\boldsymbol{x}^{\mathsf T}\boldsymbol{\beta}+\sigma^2/2}$。

变换之前要三思。变换可能毁掉解释（**Box–Cox 变换**选出的古怪指数是极端情形）；它改变原假设和误差分布；它不能保证正态性或方差齐性；逆变换回原尺度的置信区间可能有偏；变换后的尺度往往不能回答所关心的问题（医生要的是以 mg/dL 为单位的结果，而不是多少个标准差）。替代办法有广义线性模型、重抽样方法和非参数方法。

### 8.1.3. 解释变量

$X$ 的分布格局与 $Y$ 的分布同样重要。好的设计带来更高的功效，并保证整个分析的有效性；要问一问是否存在可能的混杂变量和极端个体。尤其要警惕隐蔽外推（hidden extrapolation）：解释变量相关时，一个点可以落在每个变量各自的取值范围之内，却远离数据共同覆盖的区域，于是拟合的模型被用在从未检验过的地方。对数据拟合得好并不等于对预测有用。

![隐蔽外推：数据在 (X1, X2) 平面上覆盖一个狭长的椭圆区域；标出的新点落在 X1 的范围内，也落在 X2 的范围内，却远在数据的联合区域之外](./plots/hidden-extrapolation.py)

学生数据的直方图没有明显问题，因此不做变换。样本**相关系数**为

| | gpa | hsm | hss | hse | satm | satv |
|---|---|---|---|---|---|---|
| gpa | $1$ | $0.437$ | $0.329$ | $0.289$ | $0.252$ | $0.114$ |
| hsm | | $1$ | $0.576$ | $0.447$ | $0.454$ | $0.221$ |
| hss | | | $1$ | $0.579$ | $0.240$ | $0.262$ |
| hse | | | | $1$ | $0.108$ | $0.244$ |
| satm | | | | | $1$ | $0.464$ |

在 $0.05$ 水平下（`cor.test()`），除 satv 外（$p=0.087$），各变量与 gpa 的相关都显著；解释变量之间只有 hse 与 satm 不显著相关（$p=0.106$）。高中成绩显然与 gpa 有关，但散点图中的趋势并不明显，而且解释变量彼此相关。能否直接去掉 satv？答案取决于模型中的其他变量，下一步就会看到。

### 8.1.4. 比较模型

用 `lm()` 拟合若干模型并加以比较。

```r
fit1 <- lm(gpa ~ hsm + hss + hse, data = csdata)
summary(fit1)   # coefficients, t-tests, R^2, overall F-test
anova(fit1)     # sequential sums of squares
plot(fit1)      # diagnostic plots
fit2 <- lm(gpa ~ hsm + hse, data = csdata)
fit3 <- lm(gpa ~ hsm, data = csdata)
fit4 <- lm(gpa ~ satm + satv, data = csdata)
fit5 <- lm(gpa ~ hsm + hss + hse + satm + satv, data = csdata)
```

| 模型 | 解释变量 | $R^2$ | $R_a^2$ | $s=\sqrt{\mathrm{MSE}}$ | 总体 $F$（自由度） | $p$ 值 |
|---|---|---|---|---|---|---|
| 1 | hsm、hss、hse | $0.2046$ | $0.1937$ | $0.6998$ | $18.86$ $(3,220)$ | $6.4\times10^{-11}$ |
| 2 | hsm、hse | $0.2016$ | $0.1943$ | $0.6996$ | $27.89$ $(2,221)$ | $1.6\times10^{-11}$ |
| 3 | hsm | $0.1905$ | $0.1869$ | $0.7028$ | $52.25$ $(1,222)$ | $7.8\times10^{-12}$ |
| 4 | satm、satv | $0.0634$ | $0.0549$ | $0.7577$ | $7.48$ $(2,221)$ | $7.2\times10^{-4}$ |
| 5 | 全部五个 | $0.2115$ | $0.1934$ | $0.7000$ | $11.69$ $(5,218)$ | $5.1\times10^{-10}$ |

其中 $R_a^2=1-\frac{n-1}{n-p}\cdot\frac{\mathrm{SSE}}{\mathrm{SSTO}}$ 是调整的 $R^2$，它对参数个数施加惩罚（[3.3.11](/3.3.11)）。各模型的结果很有启发性。

- 模型 1：总体 $F$ 检验高度显著，但只有 hsm 的 $t$ 检验显著（$b=0.169$，$t=4.75$）；hss 的 $t=0.91$（$p=0.36$），hse 的 $t=1.17$（$p=0.25$）。总体 $F$ 检验显著而单个 $t$ 检验不显著，是解释变量相关的典型症状。截距（$0.590$，$p=0.046$）在这里没有意义，因为没有学生的各科成绩全为 $0$。
- 模型 2（去掉 hss）：hsm 高度显著，hse 处于边缘（$t=1.75$，$p=0.082$）；$R_a^2$ 甚至略有上升。
- 模型 3（只用 hsm）：$b=0.208$，$t=7.23$；MSE 和 $R_a^2$ 比模型 2 略差。变量越少，拟合值的不同取值越少；只用 hsm（$2$ 到 $10$ 的整数）时至多有九个。
- 模型 4（只用 SAT 成绩）：satm 显著（$t=3.44$），satv 不显著（$t=-0.04$）；MSE 和 $R_a^2$ 差得多。
- 模型 5（全部五个）：只有 hsm 显著（$t=3.72$，$p=0.0003$），尽管除 satv 外每个变量单独使用时都显著。

两个比较嵌套模型的 $F$ 检验（`anova(reduced, full)`）厘清了两组变量的作用：

| 简化模型 | 完全模型 | 增加的自由度 | $F$ | $p$ 值 | 结论 |
|---|---|---|---|---|---|
| hsm、hss、hse | 全部五个 | $2$ | $0.950$ | $0.388$ | SAT 成绩没有增加信息 |
| satm、satv | 全部五个 | $3$ | $13.65$ | $3.4\times10^{-8}$ | 高中成绩不可缺少 |

第一个检验中两个模型的残差平方和分别为 $107.75$（自由度 $220$）和 $106.82$（自由度 $218$），故 $F=\big((107.75-106.82)/2\big)/(106.82/218)=0.950$。类似地，在已含 hsm 和 hse 的模型中，hss、satm、satv 三个变量作为一组也没有增加信息（$p=0.436$）；$n=224$ 时检验有足够的功效，这说明没有丢失重要信息。

哪个模型最好？hsm 显然重要。在只含 hsm 的模型和含 hsm 与 hse 的模型之间，前者解释了 gpa 变异的 $19\%$，后者 $20\%$，$R_a^2$ 略偏向两变量模型。选择取决于目的：若要解释系数，一变量模型避免了解释变量相关带来的含糊；若要预测 gpa，解释变量之间的一些相关无伤大雅，可以选两变量模型。系统的模型选择方法见 [3.3.11](/3.3.11)。

### 8.1.5. 从实例中得到的经验

1. 先逐个变量考察图形和数值汇总，再用散点图和相关系数理解变量两两之间的关系。
2. 一个变量单独使用时可以是显著的预测变量，而模型中有其他解释变量时却不显著。回归系数、它们的标准误和显著性检验的结果都取决于模型中还有哪些解释变量。
3. $\beta_k$ 的 $t$ 检验是"最后加入变量"（variable-added-last）检验：它问的是，在其他变量都已进入模型之后，$X_k$ 是否还有帮助。响应中待解释的变异总量为 $\mathrm{SSTO}$；相关的解释变量在各自能解释的那部分变异上相互重叠，因而彼此竞争，可能每一个看起来都不显著，合在一起却显著（[3.3.10](/3.3.10)）。
4. 显著性检验并不说明一切。实践中必须了解数据是如何收集的、变量的性质以及它们彼此的关系。

与此相关的是位置与变异的区别。回归系数和拟合值描述的是均值；$R^2$ 和预测区间描述的是变异。因此一个系数可以高度显著而 $R^2$ 很小：只用 satm 对 gpa 回归，$b=0.00227$，$p=0.00014$，但 $R^2=0.063$。二者的联系是

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}=\frac{R^2}{1-R^2}\cdot\frac{n-p}{p-1},
$$
所以 $n$ 很大时，即使 $R^2$ 很小，$F^*$ 也会很大。显著性说明平均响应随 $X$ 变化；$R^2$ 小说明单个响应围绕这个均值散布得很开。

![两个数据集有相同的回归直线，斜率都高度显著：左图中各点紧贴直线，R^2 大；右图中噪声大得多，R^2 小](./plots/significance-vs-r2.py)

**注 8.1.1** 若把数据集中的每个个体都复制一份，最小二乘估计不变，但残差平方和翻倍，而误差自由度从 $n-p$ 增加到 $2n-p$。于是估计的标准误缩小为原来的 $\sqrt{(n-p)/(2n-p)}\approx1/\sqrt{2}$，$t$ 统计量约增大为 $\sqrt{2}$ 倍，$p$ 值变小，尽管没有增加任何新信息。只有个体相互独立时，标准误才是有效的。

## 8.2. 多元回归中的推断

### 8.2.1. 模型与最小二乘

数据由 $n$ 个个体上观测到的响应 $Y$ 和 $p-1$ 个解释变量 $X_1,\dots,X_{p-1}$ 组成，个体 $i$ 的取值为 $(Y_i,X_{i1},\dots,X_{i,p-1})$。模型为

$$
Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i,\qquad\varepsilon_i\overset{\text{iid}}{\sim}\mathcal{N}(0,\sigma^2),\quad i=1,\dots,n,
$$
即 $\boldsymbol{Y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$，$\boldsymbol{\varepsilon}\sim\mathcal{N}_n(\boldsymbol{0},\sigma^2I_n)$，其中 $n\times p$ 的**设计矩阵** $X$ 的各行为 $\boldsymbol{x}_i^{\mathsf T}=(1,X_{i1},\dots,X_{i,p-1})$，$p$ 是包括截距在内的参数个数。

回归函数 $\mathbb{E}(Y)=\beta_0+\beta_1X_1+\cdots+\beta_{p-1}X_{p-1}$ 称为回归曲面（regression surface）或响应曲面（response surface）；有两个解释变量时它是一个平面，例如 $\mathbb{E}(Y)=10+2X_1+5X_2$，每个 $Y_i$ 以其误差 $\varepsilon_i$ 偏离这个平面。这种一阶模型（first-order model）适用于各解释变量对平均响应的作用可加、即没有交互作用的情形（[3.3.10](/3.3.10)）。

**定义 8.2.1（偏回归系数）** 在一阶模型中，称 $\beta_1,\dots,\beta_{p-1}$ 为**偏回归系数**：$\beta_k$ 是其他解释变量都保持不变时，$X_k$ 每增加一个单位平均响应 $\mathbb{E}(Y)$ 的变化量。

"偏"字至关重要：$\beta_k$ 描述的是给定其他变量时 $X_k$ 的作用，因此其他变量的集合改变时它的估计也随之改变（例 8.1.1）。

[3.3.7](/3.3.7) 的最小二乘结果是（$H=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}$ 为**帽子矩阵**）

$$
\boldsymbol{b}=\hat{\boldsymbol{\beta}}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y},\qquad\hat{\boldsymbol{Y}}=X\boldsymbol{b}=H\boldsymbol{Y},\qquad\boldsymbol{e}=\boldsymbol{Y}-\hat{\boldsymbol{Y}}=(I_n-H)\boldsymbol{Y},
$$

$$
s^2=\mathrm{MSE}=\frac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{n-p}=\frac{\boldsymbol{Y}^{\mathsf T}(I_n-H)\boldsymbol{Y}}{n-p}.
$$
几何上，$\hat{\boldsymbol{Y}}$ 是 $\boldsymbol{Y}$ 在列空间 $\mathcal{R}(X)$ 上的**正交投影**，$\boldsymbol{e}$ 位于其正交补 $\mathcal{N}(X^{\mathsf T})$ 中；系数向量 $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ 通过 $X^{\mathsf T}$ 线性地依赖于 $\boldsymbol{Y}$。误差正态时 $\boldsymbol{b}$ 与 $\boldsymbol{e}$（从而与 $s^2$）独立，这是下面定理的一部分。

### 8.2.2. 基本定理

需要关于正态向量**二次型**的两个事实。以 $\chi^2_r(\delta)$ 记自由度为 $r$、非中心参数为 $\delta$ 的非中心卡方分布，即 $\boldsymbol{Z}\sim\mathcal{N}_r(\boldsymbol{\mu},I_r)$、$\|\boldsymbol{\mu}\|^2=\delta$ 时 $\|\boldsymbol{Z}\|^2$ 的分布；$\delta=0$ 时就是通常的**卡方分布** $\chi^2_r$。

**引理 8.2.1** 设 $\boldsymbol{Z}\sim\mathcal{N}_n(\boldsymbol{\mu},I_n)$，$A$ 是 $n\times n$ 对称矩阵。则 $\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}\sim\chi^2_r(\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu})$ 当且仅当 $A$ 幂等且 $\operatorname{rank}(A)=r$。

**证明** 只证下面要用的方向。若 $A$ 对称幂等且秩为 $r$，则其特征值为 $0$ 和 $1$，故 $A=QQ^{\mathsf T}$，$Q\in\mathbb{R}^{n\times r}$ 的列标准正交。于是 $\boldsymbol{Z}^{\mathsf T}A\boldsymbol{Z}=\|Q^{\mathsf T}\boldsymbol{Z}\|^2$，其中 $Q^{\mathsf T}\boldsymbol{Z}\sim\mathcal{N}_r(Q^{\mathsf T}\boldsymbol{\mu},I_r)$，$\|Q^{\mathsf T}\boldsymbol{\mu}\|^2=\boldsymbol{\mu}^{\mathsf T}A\boldsymbol{\mu}$。（反过来，比较矩母函数可知 $A$ 的非零特征值必须都等于 $1$。）$\square$

**引理 8.2.2** 设 $\boldsymbol{y}\sim\mathcal{N}_n(\boldsymbol{\mu},\Sigma)$，$B$ 是 $k\times n$ 常数矩阵，$A$ 是 $n\times n$ 对称幂等常数矩阵。若 $B\Sigma A=O$，则 $B\boldsymbol{y}$ 与 $\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}$ 独立。

**证明** 由于 $A$ 对称幂等，$\boldsymbol{y}^{\mathsf T}A\boldsymbol{y}=\boldsymbol{y}^{\mathsf T}A^{\mathsf T}A\boldsymbol{y}=(A\boldsymbol{y})^{\mathsf T}(A\boldsymbol{y})$ 是 $A\boldsymbol{y}$ 的函数。$(B\boldsymbol{y},A\boldsymbol{y})$ 联合正态，且 $\operatorname{Cov}(B\boldsymbol{y},A\boldsymbol{y})=B\Sigma A^{\mathsf T}=B\Sigma A=O$，所以 $B\boldsymbol{y}$ 与 $A\boldsymbol{y}$ 独立（[3.1.15](/3.1.15)），从而与 $A\boldsymbol{y}$ 的任何函数独立。$\square$

**定理 8.2.1（正态线性模型的基本定理）** 设 $\boldsymbol{Y}\sim\mathcal{N}_n(X\boldsymbol{\beta},\sigma^2I_n)$，其中 $X$ 为 $n\times p$ 矩阵，秩为 $p<n$。则

1. $\boldsymbol{b}\sim\mathcal{N}_p\big(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1}\big)$；
2. $\dfrac{\boldsymbol{e}^{\mathsf T}\boldsymbol{e}}{\sigma^2}=\dfrac{(n-p)s^2}{\sigma^2}\sim\chi^2_{n-p}$；
3. $\boldsymbol{b}$ 与 $s^2$ 独立。

**证明** (1) $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}$ 是正态向量的线性变换，均值为 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}X\boldsymbol{\beta}=\boldsymbol{\beta}$，协方差矩阵为 $(X^{\mathsf T}X)^{-1}X^{\mathsf T}(\sigma^2I_n)X(X^{\mathsf T}X)^{-1}=\sigma^2(X^{\mathsf T}X)^{-1}$。

(2) $\boldsymbol{Y}/\sigma\sim\mathcal{N}_n(X\boldsymbol{\beta}/\sigma,I_n)$，且 $\boldsymbol{e}^{\mathsf T}\boldsymbol{e}/\sigma^2=(\boldsymbol{Y}/\sigma)^{\mathsf T}(I_n-H)(\boldsymbol{Y}/\sigma)$。矩阵 $I_n-H$ 对称幂等，$\operatorname{rank}(I_n-H)=\operatorname{tr}(I_n-H)=n-p$；由于 $(I_n-H)X=O$，非中心参数 $\boldsymbol{\beta}^{\mathsf T}X^{\mathsf T}(I_n-H)X\boldsymbol{\beta}/\sigma^2=0$。由引理 8.2.1 得 $\chi^2_{n-p}$。

(3) $\boldsymbol{b}=B\boldsymbol{Y}$，$B=(X^{\mathsf T}X)^{-1}X^{\mathsf T}$；$(n-p)s^2=\boldsymbol{Y}^{\mathsf T}A\boldsymbol{Y}$，$A=I_n-H$；由于 $X^{\mathsf T}H=X^{\mathsf T}$，$B(\sigma^2I_n)A=\sigma^2(X^{\mathsf T}X)^{-1}X^{\mathsf T}(I_n-H)=O$。由引理 8.2.2 得独立性。$\square$

[3.2.5](/3.2.5) 中未加证明地使用了这个定理（那里的[定理 5.6.1](/3.2.5#thm-5.6.1)），本课程中所有精确的 $t$ 与 $F$ 方法都源于它。

### 8.2.3. 回归系数的推断

[3.3.4](/3.3.4) 的总体 $F$ 检验可以照搬：检验 $H_0\colon\beta_1=\cdots=\beta_{p-1}=0$ 对 $H_1$：至少有一个 $k$ 使 $\beta_k\ne0$，用

$$
F^*=\frac{\mathrm{MSR}}{\mathrm{MSE}}=\frac{\mathrm{SSR}/(p-1)}{\mathrm{SSE}/(n-p)}\overset{H_0}{\sim}F_{p-1,n-p},
$$
在水平 $\alpha$ 下，当 $F^*>F_{p-1,n-p,\alpha}$，即 $p$ 值 $\mathbb{P}(F_{p-1,n-p}>F^*)$ 小于 $\alpha$ 时拒绝 $H_0$。

对单个系数，定理 8.2.1 给出 $b_k\sim\mathcal{N}\big(\beta_k,\sigma^2[(X^{\mathsf T}X)^{-1}]_{kk}\big)$，其中 $[(X^{\mathsf T}X)^{-1}]_{kk}$ 是 $\beta_k$ 对应的对角元（$k=0,1,\dots,p-1$）。$\boldsymbol{b}$ 的估计协方差矩阵和 $b_k$ 的估计方差为

$$
s^2(\boldsymbol{b})=\mathrm{MSE}\,(X^{\mathsf T}X)^{-1},\qquad s^2(b_k)=\mathrm{MSE}\,[(X^{\mathsf T}X)^{-1}]_{kk}.
$$

**定理 8.2.2** 在正态线性模型下，$(b_k-\beta_k)/s(b_k)\sim t_{n-p}$。因此：

1. $H_0\colon\beta_k=0$ 对 $H_1\colon\beta_k\ne0$ 的水平 $\alpha$ 检验在 $\lvert t^*\rvert>t_{n-p,\alpha/2}$ 时拒绝，其中 $t^*=b_k/s(b_k)$；
2. $\beta_k$ 的 $100(1-\alpha)\%$ 置信区间为 $b_k\pm t_{n-p,\alpha/2}\,s(b_k)$。

**证明** 由定理 8.2.1，$(b_k-\beta_k)/\big(\sigma\sqrt{[(X^{\mathsf T}X)^{-1}]_{kk}}\big)\sim\mathcal{N}(0,1)$ 与 $(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$ 独立；前者除以后者除以 $n-p$ 后的平方根，正是 $(b_k-\beta_k)/s(b_k)$。$\square$

这个 $t$ 检验评价的是给定模型中其他变量时的 $X_k$，同样是"最后加入变量"检验。作为一般线性检验，它把完全模型与只删去 $X_k$ 所得的简化模型

$$
Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_{k-1}X_{i,k-1}+\beta_{k+1}X_{i,k+1}+\cdots+\beta_{p-1}X_{i,p-1}+\varepsilon_i
$$
相比较，两种检验等价（[3.3.9](/3.3.9)）。

**例 8.2.1（Dwaine 影楼）** 一家公司在 $21$ 个中等城市经营人像影楼。在每个城市观测销售额 $Y$、$16$ 岁及以下人口 $X_1$（千人）和人均可支配收入 $X_2$（千元），拟合 $Y_i=\beta_0+\beta_1X_{i1}+\beta_2X_{i2}+\varepsilon_i$。

```r
reg1 <- lm(Sales ~ Targtpop + Dispoinc, data = a1)
summary(reg1)
confint(reg1, level = 0.95)   # t-intervals for each coefficient
```

| | 估计 | 标准误 | $t$ | $p$ 值 | $95\%$ 置信区间 |
|---|---|---|---|---|---|
| 截距 | $-68.857$ | $60.017$ | $-1.15$ | $0.266$ | $[-194.95,\ 57.23]$ |
| $X_1$（Targtpop） | $1.4546$ | $0.2118$ | $6.87$ | $2\times10^{-6}$ | $[1.010,\ 1.899]$ |
| $X_2$（Dispoinc） | $9.3655$ | $4.0640$ | $2.30$ | $0.033$ | $[0.827,\ 17.904]$ |

这里 $s=11.01$（自由度 $18$），$R^2=0.9167$，$R_a^2=0.9075$，$F^*=99.1$（自由度 $(2,18)$，$p=1.9\times10^{-10}$）。另一个变量已在模型中时，两个变量都有助于解释销售额。若只用 $X_1$，拟合为 $\hat Y=68.05+1.836X_1$，截距和斜率的置信区间为 $[48.24,87.85]$ 与 $[1.529,2.142]$：二者都变化很大，因为系数取决于模型中的其他变量。

### 8.2.4. 平均响应的估计

在解释变量的一组取值 $\boldsymbol{x}_h=(1,X_{h1},\dots,X_{h,p-1})^{\mathsf T}$ 处，平均响应 $\mathbb{E}(Y_h)=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}$ 的估计为

$$
\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}=\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{Y}\sim\mathcal{N}\big(\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta},\ \sigma^2\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big),
$$
估计方差为 $s^2(\hat Y_h)=\mathrm{MSE}\,\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h=\boldsymbol{x}_h^{\mathsf T}s^2(\boldsymbol{b})\boldsymbol{x}_h$。与定理 8.2.2 一样，$\mathbb{E}(Y_h)$ 的 $100(1-\alpha)\%$ **置信区间**为

$$
\hat Y_h\pm t_{n-p,\alpha/2}\,s(\hat Y_h).
$$
它的宽度随 $\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$ 增大，即在 $X^{\mathsf T}X$ 给出的度量下 $\boldsymbol{x}_h$ 离数据中心越远，区间越宽；它也随 $\mathrm{MSE}$ 和置信水平增大，随 $n$ 增大而缩小。大样本时，即使误差不正态，这个区间也近似有效。

### 8.2.5. 新观测的预测

在 $\boldsymbol{x}_h$ 处的新观测 $Y_{h(\mathrm{new})}=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}+\varepsilon_h$（$\varepsilon_h\sim\mathcal{N}(0,\sigma^2)$ 与数据独立）用同一个 $\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}$ 来预测。这时不确定性有两个来源：$\boldsymbol{b}$ 的抽样波动和新的误差项。

**定理 8.2.3** 在正态线性模型下，

$$
Y_{h(\mathrm{new})}-\hat Y_h\sim\mathcal{N}\Big(0,\ \sigma^2\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)\Big),
$$
$Y_{h(\mathrm{new})}$ 的 $100(1-\alpha)\%$ **预测区间**为 $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\mathrm{pred})$，其中 $s^2(\mathrm{pred})=\mathrm{MSE}\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)$。

**证明** 代入 $\boldsymbol{b}=(X^{\mathsf T}X)^{-1}X^{\mathsf T}(X\boldsymbol{\beta}+\boldsymbol{\varepsilon})=\boldsymbol{\beta}+(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}$，

$$
Y_{h(\mathrm{new})}-\hat Y_h=\big(\boldsymbol{x}_h^{\mathsf T}\boldsymbol{\beta}+\varepsilon_h\big)-\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}=\varepsilon_h-\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}.
$$
两项是均值为 $0$ 的独立正态变量，所以差是正态的，方差为 $\operatorname{Var}(\varepsilon_h)+\operatorname{Var}\big(\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}X^{\mathsf T}\boldsymbol{\varepsilon}\big)=\sigma^2+\sigma^2\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$。由于 $\hat Y_h$ 只通过 $\boldsymbol{b}$ 依赖于数据，这个差与 $s^2$ 独立，区间的推导同定理 8.2.2。$\square$

与平均响应的置信区间不同，预测区间强烈依赖于误差的正态性：新误差的方差项 $\sigma^2$ 不随 $n$ 缩小，所以即使在大样本中，这个区间也依赖于误差分布的形状。

**例 8.2.2（Dwaine 影楼，续）** `predict(reg1, se.fit = TRUE, interval = "confidence")` 与 `interval = "prediction"` 在已观测的城市处给出

| 城市 | $X_1$ | $X_2$ | $Y$ | $\hat Y_h$ | $s(\hat Y_h)$ | $\mathbb{E}(Y_h)$ 的 $95\%$ 置信区间 | $95\%$ 预测区间 |
|---|---|---|---|---|---|---|---|
| 1 | $68.5$ | $16.7$ | $174.4$ | $187.18$ | $3.84$ | $[179.11,\ 195.25]$ | $[162.69,\ 211.68]$ |
| 2 | $45.2$ | $16.8$ | $164.4$ | $154.23$ | $3.56$ | $[146.76,\ 161.70]$ | $[129.93,\ 178.53]$ |
| 3 | $91.3$ | $18.2$ | $244.2$ | $234.40$ | $4.59$ | $[224.76,\ 244.04]$ | $[209.34,\ 259.45]$ |
| 21 | $52.3$ | $16.0$ | $166.5$ | $157.06$ | $4.08$ | $[148.49,\ 165.63]$ | $[132.40,\ 181.73]$ |

对城市 1，$s^2(\mathrm{pred})=s^2+s^2(\hat Y_h)=11.01^2+3.84^2$，故 $s(\mathrm{pred})=11.66$，预测区间 $187.18\pm2.101\times11.66$ 的宽度约为置信区间的三倍：单个城市的不确定性主要来自新的误差项，而不是 $\boldsymbol{\beta}$ 的估计。

### 8.2.6. 诊断与补救

[3.3.5](/3.3.5) 的诊断方法可以推广到多元回归：

- 考察每个变量的分布以及变量两两之间的关系；
- 画残差对拟合值、对每个解释变量、对时间或观测顺序（如有）的图；
- 用残差的直方图和**正态 QQ 图**检查正态性；
- 画残差对任何可能与方差有关的量（如拟合值或各个 $X_k$）的图，检查方差齐性。

补救措施也类似：Box–Cox 等变换（[3.3.6](/3.3.6)），以及分别包含和去掉可能的离群值进行分析。多元回归特有的诊断（附加变量图、杠杆值、影响度量与多重共线性度量）见 [3.3.11](/3.3.11)，更多的补救措施见 [3.3.12](/3.3.12)。

## 小结

- 多元回归分析从逐个变量和两两变量的探索开始；变换使偏斜变量更对称，但牺牲可解释性；相关的解释变量可能造成隐蔽外推。
- 系数、标准误和 $t$ 检验都取决于模型中的其他变量。每个 $t$ 检验都是"最后加入变量"检验；总体 $F$ 检验显著而 $t$ 检验不显著，提示解释变量相关；嵌套模型用残差平方和之差的 $F$ 检验来比较。
- 显著性关乎均值，$R^2$ 与预测区间关乎变异：$F^*=\frac{R^2}{1-R^2}\cdot\frac{n-p}{p-1}$。
- 基本定理：$\boldsymbol{b}\sim\mathcal{N}_p(\boldsymbol{\beta},\sigma^2(X^{\mathsf T}X)^{-1})$，$(n-p)s^2/\sigma^2\sim\chi^2_{n-p}$，且二者独立。

| 目标 | 估计 | 估计方差 | $100(1-\alpha)\%$ 区间 |
|---|---|---|---|
| $\beta_k$ | $b_k$ | $\mathrm{MSE}\,[(X^{\mathsf T}X)^{-1}]_{kk}$ | $b_k\pm t_{n-p,\alpha/2}\,s(b_k)$ |
| $\mathbb{E}(Y_h)$ | $\hat Y_h=\boldsymbol{x}_h^{\mathsf T}\boldsymbol{b}$ | $\mathrm{MSE}\,\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h$ | $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\hat Y_h)$ |
| $Y_{h(\mathrm{new})}$ | $\hat Y_h$ | $\mathrm{MSE}\,\big(1+\boldsymbol{x}_h^{\mathsf T}(X^{\mathsf T}X)^{-1}\boldsymbol{x}_h\big)$ | $\hat Y_h\pm t_{n-p,\alpha/2}\,s(\mathrm{pred})$ |
