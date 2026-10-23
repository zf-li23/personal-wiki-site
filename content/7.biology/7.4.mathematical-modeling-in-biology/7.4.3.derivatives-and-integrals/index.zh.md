---
title: 导数与积分
---

**内容**：变化率（导数）与累积量（积分）的生物学对应（如生长速率、总生物量）；作为线性近似的导数。

在上一节中，我们利用Leslie矩阵研究了年龄结构化种群的离散时间动态。矩阵的主导特征值 $\lambda_1$ 给出了种群的长期增长率。若 $\lambda_1 > 1$，种群增长；若 $\lambda_1 < 1$，种群衰退。然而，这种线性模型假设增长率恒定，忽略了资源有限性导致的密度制约效应。本节将引入密度制约，并由此过渡到连续时间模型，介绍导数与积分的基本概念及其在种群增长中的应用。

## 3.1. 密度制约的种群增长：从离散到混沌

考虑一个简单的离散时间种群模型，其中种群数量 $n_t$ 随时间 $t$ 变化。假设增长率依赖于种群密度，即存在密度制约。最经典的模型是**逻辑斯谛映射**（Logistic map）：

$$
n_{t+1} = r n_t \left(1 - \frac{n_t}{K}\right)
$$

其中 $r$ 是内禀增长率，$K$ 是环境容纳量。为了简化，我们通常将种群数量标准化为 $x_t = n_t / K$，从而得到：

$$
x_{t+1} = r x_t (1 - x_t), \quad 0 \leq x_t \leq 1
$$

这个简单的二次映射能够产生极其丰富的动态行为，包括稳定平衡、周期振荡和混沌。

### 3.1.1. 导数的直观：变化率的线性近似

在离散系统中，我们通常关心 $x_{t+1}$ 相对于 $x_t$ 的变化。定义函数 $f(x) = r x (1 - x)$，则 $x_{t+1} = f(x_t)$。在平衡点 $\overline{x}$（即满足 $\overline{x} = f(\overline{x})$）附近，我们可以用导数来近似函数的行为。导数 $f'(\overline{x})$ 表示 $f$ 在 $\overline{x}$ 处的线性近似系数，即当 $x_t$ 偏离平衡点一个小量 $\delta$ 时，下一时刻的偏离约为 $f'(\overline{x}) \delta$。

平衡点的稳定性由导数 $f'(\overline{x})$ 的绝对值决定：

- 若 $|f'(\overline{x})| < 1$，平衡点稳定，小偏离会衰减；
- 若 $|f'(\overline{x})| > 1$，平衡点不稳定，小偏离会放大。

对于逻辑斯谛映射，平衡点有两个：$\overline{x}_0 = 0$ 和 $\overline{x}_1 = 1 - 1/r$（当 $r > 1$ 时）。计算导数 $f'(x) = r(1 - 2x)$，于是：

- 在 $\overline{x}_0 = 0$ 处，$f'(0) = r$，因此当 $0 < r < 1$ 时稳定，$r > 1$ 时不稳定。
- 在 $\overline{x}_1 = 1 - 1/r$ 处，$f'(\overline{x}_1) = 2 - r$，因此当 $1 < r < 3$ 时稳定（因为 $|2 - r| < 1$）。

当 $r$ 超过 3 时，平衡点 $\overline{x}_1$ 失稳，系统出现周期 2 振荡。随着 $r$ 进一步增大，周期倍增（倍周期分岔）发生，最终进入混沌状态。

### 3.1.2. 蛛网图（Cobweb plot）可视化

蛛网图是一种可视化离散映射迭代过程的工具。它通过绘制函数 $f(x) = rx(1-x)$ 和对角线 $f(x) = x$，并追踪迭代路径，帮助我们直观理解系统的动态。

![逻辑斯谛映射蛛网图：r = 0.75、1.5、2、2.5 时收敛到平衡点](./plots/logistic-cobweb-low-r.py)

可能需要稍加理解绘图逻辑：在每个迭代步骤，我们绘制从当前 $x_t$ 到下一个 $x_{t+1}$ ，即 $f(x_t)$ 的垂直线，再画水平线到 $f(x)=x$，从该点进行下一次迭代。这些线段构成了“蛛网”，显示了种群数量如何在每次迭代中沿着逻辑斯谛曲线移动。

通过改变 $r$ 的值，我们可以观察到：
- $r=0.75$（代表$0<r<1$）时，不存在平衡点，种群衰落
- $r=1.5$（代表$1<r<2$）时，在 $f(x)$ 的上升段有平衡点
- $r=2.0$ 时，在 $f(x)$ 的顶点有平衡点
- $r=2.5$（代表$2<r<3$）时，在 $f(x)$ 的下降段有平衡点振荡

![逻辑斯谛映射蛛网图：r = 3.2、3.5、3.662117、4 时的周期与混沌轨道](./plots/logistic-cobweb-high-r.py)

$r>3$ 时，为了使系统达到稳定震荡状态，我们忽略前1000次迭代，然后记录100次迭代的过程：
- $r=3.2$（代表$3<r<1+\sqrt{6}$）时，系统出现周期 2 振荡
- $r=3.5$（代表$r>1+\sqrt{6}$）时，系统出现周期 4 振荡，相比之前呈现周期倍增
- $r=3.662117$时，系统出现周期 8 振荡，此后振荡周期数改变越来越密集
- $r=4$时，系统混沌，无法找出振荡现象的发生

### 3.1.3. 分岔图与混沌

为了全面了解参数 $r$ 对系统行为的影响，我们可以绘制分岔图，即对于每个 $r$，将长期迭代后稳定的 $x_t$ 值绘制出来。以下代码生成逻辑斯谛映射的分岔图：

![逻辑斯谛映射的分岔图](./plots/logistic-bifurcation.py)

分岔图清晰地展示了从稳定平衡到倍周期分岔再到混沌的过程。在混沌区域（如 $r \approx 4$），系统对初始条件极其敏感，即著名的“蝴蝶效应”。这正是混沌系统的特征：确定性方程产生看似随机的输出，并且长期预测不可能。

类似地，$\sin$ 曲线的混沌行为也可以通过类似的分岔图来展示，其中 $r$ 对应于频率或周期。两张图的形状几乎一模一样：

![正弦映射的分岔图](./plots/sine-map-bifurcation.py)

这种倍周期现象是如何产生的呢？在一定程度上，我们可以用重整化群来解释：

### 3.1.4. 重整化群：从自相似到普适性

重整化群（Renormalization Group, RG）是一个强大的理论框架，帮助我们理解为什么逻辑斯蒂映射会表现出如此规则的分岔模式。让我们从数值实验开始，直观感受重整化群的核心思想。

通过数值实验，我们可以发现逻辑斯蒂映射中惊人的自相似性：

![逻辑斯谛映射分岔图及其局部放大的自相似结构](./plots/bifurcation-self-similarity.py)

**观察**：右侧的局部放大图看起来像是左侧整体图的缩小版，这就是**自相似性**——整体结构在局部重复出现。

这种自相似性在迭代函数中表现得更加明显。我们比较不同阶数的迭代函数（即 $f(x)$, $f(f(x))$, $f^{(4)}(x)$）：

![f(x)、f(f(x)) 与 f⁽⁴⁾(x) 迭代函数的比较](./plots/iterated-maps-comparison.py)

**关键观察**：
1. **r=3.2时**：$f(f(x))$在$x=0.5$附近区域（红色方框）看起来像是$f(x)$在$r=2$时的**倒置版本**。
2. **r=3.5时**：$f^{(4)}(x)$在$x=0.5$附近的小区域（红色方框）看起来又像是$f(f(x))$在某个参数下的缩小版。

这种自相似性正是重整化群的核心。让我们通过具体操作来理解：

![重整化操作演示与 Feigenbaum 常数的数值估计](./plots/renormalization-feigenbaum.py)

上述观察可以形式化为**重整化群方程**。当我们进行尺度变换时，函数的行为满足：

$$
\mathcal{R}[f](x) = \alpha f\left(f\left(\frac{x}{\alpha}\right)\right) \approx f(x)
$$

其中 $\mathcal{R}$ 是重整化群算子，$g$ 是映射函数，$\alpha$ 是缩放因子。该变换描述了在倍周期分岔序列中，映射函数在尺度变换下的自相似行为。**不动点方程** $\mathcal{R}[g^*] = g^*$ 的解 $g^*$ 称为**普适函数（universal function）**，它决定了倍周期分岔的临界行为。

费根鲍姆（Feigenbaum）通过数值计算发现，在倍周期分岔序列中，两个关键常数具有普适性：

1. **分岔参数间隔比 $\delta$**：
   $$
   \delta = \lim_{n\to\infty} \frac{r_n - r_{n-1}}{r_{n+1} - r_n} \approx 4.669
   $$
   其中 $r_n$ 是第 $n$ 次倍周期分岔发生时的参数值。

2. **轨道尺度缩放比 $\alpha$**：
   $$
   \alpha = \lim_{n\to\infty} \frac{d_n}{d_{n+1}} \approx -2.5029
   $$
   其中 $d_n$ 是第 $n$ 周期轨道在分岔点处的特征间距。

这些常数不仅适用于逻辑斯谛映射，也适用于一大类单峰映射（unimodal maps），体现了混沌现象的**普适性（universality）**。

让我们尝试数值寻找普适函数：

![重整化群迭代流向普适函数](./plots/renormalization-universal-function.py)

即使看不懂重整化群的这一部分，我们至少可以得到一个感想：即使是逻辑斯谛方程这样简单的形式，也能衍生出非常复杂的混沌现象，可以借此体会为什么说生命系统以不可求解的非线性动力学为主，所以即使是把时间尺度分得再小，这样的模拟方法在解决生物问题时都是有可能行不通的，这也是为什么我们需要不断地对方法进行整合。接下来的内容可以视为把上述刻画逻辑斯谛方程的过程整合为导数与积分。

### 3.1.5. 李雅普诺夫指数与混沌检测

对于非线性系统，长期行为可能极为复杂，包括混沌。**李雅普诺夫指数（Lyapunov Exponent）** 量化了相邻轨迹的发散速率，是检测混沌的重要指标。

对于一维离散映射 $x_{n+1} = f(x_n)$，考虑两个初始条件极其接近的轨道：$x_0$ 和 $x_0 + \delta_0$，其中 $\delta_0$ 极小。经过一次迭代后，它们的距离为：

$$
\delta_1 = |f(x_0 + \delta_0) - f(x_0)| \approx |f'(x_0)|\cdot|\delta_0|
$$

经过 $n$ 次迭代后：

$$
\delta_n \approx |f'(x_{n-1})f'(x_{n-2})\cdots f'(x_0)|\cdot|\delta_0|
$$

取对数并除以 $n$：

$$
\frac{1}{n} \ln\left|\frac{\delta_n}{\delta_0}\right| \approx \frac{1}{n} \sum_{i=0}^{n-1} \ln|f'(x_i)|
$$

当 $n \to \infty$ 时，得到**李雅普诺夫指数**：

$$
\lambda = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln|f'(x_i)|
$$

- $\lambda > 0$：相邻轨道指数发散，系统对初始条件极度敏感 → **混沌**
- $\lambda = 0$：相邻轨道保持恒定距离 → **周期边界**（如临界分岔点）
- $\lambda < 0$：相邻轨道指数收敛 → **稳定周期或平衡点**

对于 $d$ 维系统，有 $d$ 个李雅普诺夫指数，按大小排列 $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_d$。若 $\lambda_1 > 0$，系统呈现混沌行为。

对于逻辑斯蒂映射 $x_{n+1} = rx_n(1-x_n)$，导数为 $f'(x) = r(1-2x)$，因此：

$$
\lambda(r) = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln|r(1-2x_i)|
$$

将李雅普诺夫指数谱与分岔图结合，可以直观地看到混沌区域与周期区域：

![分岔图与李雅普诺夫指数谱叠加](./plots/lyapunov-bifurcation.py)

## 3.2. 连续的种群增长：导数与积分

当种群数量很大且世代重叠时，离散时间模型可能不再适用，我们需要连续时间模型。连续模型用微分方程描述种群瞬时变化率。

### 3.2.1. 指数增长模型

设 $N(t)$ 表示时刻 $t$ 的种群数量。最简单的连续增长模型是指数增长：

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = r N
$$

其中 $r$ 是瞬时增长率。这个微分方程表示种群变化率与当前数量成正比。方程的积分式为：

$$
N(t) = N_0 \mathrm{e}^{rt}
$$

其中 $N_0 = N(0)$ 是初始数量。指数增长在资源无限时是合理的，但现实世界中资源有限，因此我们需要引入密度制约。

### 3.2.2. 逻辑斯谛增长模型

在连续时间中，密度制约表现为增长率随种群数量增加而下降。逻辑斯谛方程是：

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = r N \left(1 - \frac{N}{K}\right)
$$

其中 $K$ 是环境容纳量。当 $N$ 接近 $K$ 时，增长率趋近于零。这个方程可以解析求解（通过分离变量法），得到：

$$
N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) \mathrm{e}^{-rt}}
$$

逻辑斯谛增长曲线呈S形（Sigmoid），从初始指数增长逐渐减速，最终趋于 $K$。

求解步骤如下：

1. 分离变量，将方程改写为：
$$
\frac{\mathrm{d}N}{N \left(1 - \frac{N}{K}\right)} = r \, \mathrm{d}t
$$

2. 分解有理式，对左边分母进行部分分式分解：
$$
\frac{1}{N \left(1 - \frac{N}{K}\right)} = \frac{1}{N} + \frac{1}{K - N}
$$
代入得：
$$
\left( \frac{1}{N} + \frac{1}{K - N} \right) \mathrm{d}N = r \, \mathrm{d}t
$$

3. 两边积分：
$$
\int \left( \frac{1}{N} + \frac{1}{K - N} \right) \mathrm{d}N = \int r \, \mathrm{d}t
$$
计算积分：
$$
\ln |N| - \ln |K - N| = rt + C
$$
其中 $C$ 为积分常数。合并对数项：
$$
\ln \left| \frac{N}{K - N} \right| = rt + C
$$

4. 消去对数取指数：
$$
\left| \frac{N}{K - N} \right| = \mathrm{e}^{rt + C} = A \mathrm{e}^{rt}
$$
其中 $A = \mathrm{e}^C > 0$。当 $0 < N < K$ 时，可去掉绝对值：
$$
\frac{N}{K - N} = A \mathrm{e}^{rt}
$$

5. 整理方程，解出 $N(t)$：
：
$$
N = (K - N) A \mathrm{e}^{rt} = K A \mathrm{e}^{rt} - N A \mathrm{e}^{rt}
$$
$$
N (1 + A \mathrm{e}^{rt}) = K A \mathrm{e}^{rt}
$$
$$
N(t) = \frac{K A \mathrm{e}^{rt}}{1 + A \mathrm{e}^{rt}}
$$

6. 由初始条件确定常数 $A$：
代入 $t = 0$，$N(0) = N_0$：
$$
N_0 = \frac{K A}{1 + A}
$$
解得：
$$
A = \frac{N_0}{K - N_0}
$$

7. 代入得最终解：
将 $A$ 代入 $N(t)$：
$$
N(t) = \frac{K \cdot \frac{N_0}{K - N_0} \cdot \mathrm{e}^{rt}}{1 + \frac{N_0}{K - N_0} \cdot \mathrm{e}^{rt}}
$$
分子分母同乘以 $K - N_0$：
$$
N(t) = \frac{K N_0 \mathrm{e}^{rt}}{K - N_0 + N_0 \mathrm{e}^{rt}}
$$
或等价地，分子分母同除以 $N_0 \mathrm{e}^{rt}$：
$$
N(t) = \frac{K}{1 + \left( \frac{K - N_0}{N_0} \right) \mathrm{e}^{-rt}}
$$

### 3.2.3. 导数与积分的生物学意义

在连续模型中，导数 $\dfrac{\mathrm{d}N}{\mathrm{d}t}$ 表示种群数量在时刻 $t$ 的**瞬时变化率**。它告诉我们种群增长的速度。例如，在逻辑斯谛模型中，当 $N$ 很小时，$\dfrac{\mathrm{d}N}{\mathrm{d}t} \approx r N$，近似指数增长；当 $N$ 接近 $K$ 时，变化率趋近于零。

积分则是导数的逆运算。从变化率 $\mathrm{d}N/\mathrm{d}t$ 求种群数量 $N(t)$ 的过程就是积分。指数增长和逻辑斯谛增长模型的解析解就是通过积分得到的。在实际应用中，我们经常需要数值积分来求解无法解析求解的微分方程。

## 3.3. 增长曲线拟合

在实际研究中，我们经常需要根据实验数据估计模型参数。例如，给定一组时间序列的种群数量数据，我们希望拟合逻辑斯谛曲线，估计参数 $r$ 和 $K$。

### 3.3.1. 直接使用非线性最小二乘法

我们可以使用 `scipy.optimize.curve_fit` 函数直接拟合逻辑斯谛函数。假设我们有一组数据 $(t_i, N_i)$，定义逻辑斯谛函数：

![逻辑斯谛增长曲线的非线性最小二乘拟合](./plots/logistic-curve-fit.py)

### 3.3.2. 线性化后拟合

对于逻辑斯谛方程，我们可以通过变换将其线性化，然后使用线性回归。我们通常没有瞬时变化率 $r$ 的数据，而逻辑斯谛方程可以改写为：

$$
\ln\left(\dfrac{K - N}{N}\right) = \ln\left(\dfrac{K - N_0}{N_0}\right) - r t
$$

如果我们已知 $K$，则可以对 $\ln((K-N)/N)$ 关于 $t$ 进行线性回归得到 $r$。但 $K$ 通常是未知的，虽然可以目测，但如果种群尚未增长到环境容纳量附近，一种常用的方法是**三点法**，即有三个时间间隔相等的种群数量的数据点时，可以用如下公式计算得到 $K$：

$$
K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}
$$

推导如下：设三个等距时间点 $t_0, t_1 = t_0 + \Delta t, t_2 = t_0 + 2\Delta t$ 对应的种群数量为 $N_0, N_1, N_2$。由解的形式可得：
$$
\begin{aligned}
\frac{K - N_0}{N_0} &= c, \\
\frac{K - N_1}{N_1} &= c \mathrm{e}^{-r\Delta t}, \\
\frac{K - N_2}{N_2} &= c \mathrm{e}^{-2r\Delta t}.
\end{aligned}
$$
消去 $c$ 和 $r$ 得：
$$
\left(\frac{K - N_1}{N_1}\right)^2 = \frac{K - N_0}{N_0} \cdot \frac{K - N_2}{N_2}.
$$
整理后解出 $K$：
$$
K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}.
$$
求得 $K$ 后，代入下式计算 $r$：
$$
r = -\frac{1}{\Delta t} \ln\left( \frac{(K - N_1) N_0}{(K - N_0) N_1} \right).
$$

实际上，直接非线性拟合更为方便可靠，线性化方法可能会引入偏差（因为变换会改变误差结构）。但在某些情况下，线性化可以提供快速的参数估计。

## 小结

- 离散的逻辑斯谛映射 $x_{t+1} = f(x_t) = rx_t(1-x_t)$ 虽然简单，却随 $r$ 依次出现稳定平衡、倍周期分岔与混沌（3.1）。平衡点 $\bar x$ 的稳定性由导数决定：$\lvert f'(\bar x)\rvert < 1$ 稳定，$> 1$ 不稳定。

  | $r$ 的范围 | 长期行为 |
  |---|---|
  | $0 < r < 1$ | 收敛到 $\bar x_0 = 0$，种群衰落 |
  | $1 < r < 3$ | 收敛到 $\bar x_1 = 1 - 1/r$（$f'(\bar x_1) = 2 - r$） |
  | $3 < r < 1 + \sqrt6$ | 稳定的周期 2 振荡 |
  | 更大的 $r$ | 周期 4、8、…… 的倍周期级联，直至混沌（如 $r = 4$） |

- 蛛网图与分岔图是观察一维映射的两种工具（3.1.2、3.1.3）。分岔图具有自相似性，可用重整化群 $\mathcal{R}[f](x) = \alpha f(f(x/\alpha))$ 解释；Feigenbaum 常数 $\delta \approx 4.669$、$\alpha \approx -2.503$ 对一大类单峰映射普适，正弦映射的分岔图因此与逻辑斯谛映射几乎相同（3.1.4）。
- 李雅普诺夫指数 $\lambda = \lim_{n\to\infty}\frac1n\sum_{i=0}^{n-1}\ln\lvert f'(x_i)\rvert$ 度量相邻轨道的分离速率：$\lambda > 0$ 为混沌，$\lambda < 0$ 为稳定周期或平衡点，$\lambda = 0$ 出现在分岔点（3.1.5）。
- 连续时间模型中，导数是瞬时变化率，积分由变化率还原数量（3.2）：指数增长 $\frac{\mathrm{d}N}{\mathrm{d}t} = rN$ 的解为 $N_0\mathrm{e}^{rt}$；逻辑斯谛增长 $\frac{\mathrm{d}N}{\mathrm{d}t} = rN(1 - N/K)$ 经分离变量与部分分式积分得 S 形曲线 $N(t) = K/\bigl(1 + \frac{K-N_0}{N_0}\mathrm{e}^{-rt}\bigr)$。
- 拟合增长曲线有两种做法（3.3）：直接用非线性最小二乘（`scipy.optimize.curve_fit`）；或用等间隔三点估计 $K$，再对 $\ln\frac{K-N}{N}$ 关于 $t$ 作线性回归。线性化改变了误差结构，通常不如直接非线性拟合可靠。

## 思考题

1. （选做）取我们在文档中写下的重整化群变换。你会如何编写程序来数值计算普适函数？

   **答** 可以参考正文中的作图代码。

2. 逻辑斯蒂映射的倍周期分岔与混沌

   注：本题中已出现在文档中的部分将不再重新给出回答。

   混沌通常与某种非线性动力学相关。我们在文档中已经看到，简单的逻辑斯蒂映射如何导致复杂的动力学行为。动力系统的研究通常关注长期行为（特别是稳态和其他"吸引子"）。我们可以通过改变系统参数 $r$ 来研究逻辑斯蒂映射中混沌的发生。

   当处于某些参数范围时，逻辑斯蒂映射为我们提供了一个动力学"不可预测"的例子。在本练习中，我们将通过观察逻辑斯蒂映射在长时间下沿吸引子运动的行为来研究其动力学特性。

   - **a)** 固定点与周期 8 吸引子

     对于 $r = 0.75$，使用几个初始条件 $x_0$ 迭代映射。最终，所有解都应趋于零（固定点）。在同一图上绘制 $f(x) = rx(1-x)$ 与 $x$ 以及对角线 $y = x$。然后编写一个简短的程序来绘制"蛛网图"，正如我在黑板上的演示。通过多次迭代逻辑斯蒂映射，我们可以找到吸引子上的点。找到一个 $r$ 值，使得吸引子具有周期 8。提交图形（并标出 $r$ 的值）。

   - **b)** 稳态解的稳定性与周期 2 解

     正如我们在文档中看到的，对于 $r > 3$，稳态解 $x^* = 1 - \frac{1}{r}$ 不再稳定。这可以通过证明导数 $\left|f^{\prime}\left(x^{*}\right)\right| > 1$ 来证明。可选练习：通过观察映射的第二次迭代并检查 $x = f(f(x))$ 的不动点。证明周期 2 解在 $3 < r < 1 + \sqrt{6}$ 时是稳定的。

   - **c)** 分岔图与自相似性
     - 让我们尝试构建逻辑斯蒂映射的分岔图。这里，分岔图是吸引子作为 $r$ 的函数的图，其中 $0 < r < 4$。一种方法是选取均匀间隔的 $\delta r$，运行 $n_{\mathrm{transient}}$ 步，记录 $n_{\mathrm{period}}$ 步，然后绘制记录的点。开始时使用较小的 $n_{\mathrm{transient}}$ 和 $n_{\mathrm{period}}$。确保你的 MATLAB 程序正常工作后，可以尝试 $\delta r < 0.01$ 且 $n_{\mathrm{transient}}$ 和 $n_{\mathrm{period}} > 100$。制作一个图形并提交。
     - 对于 $r = 3.2$，在同一图上绘制 $f(f(x))$ 和对角线 $y = x$。你能看出 $f(x)$ 的周期 2 解变成了 $f(f(x))$ 的一对稳定不动点吗？
     - 将此图与 $r = 2$ 时的 $f(x)$ 进行比较。注意，对于 $f(f(x))$，$x = \frac{1}{2}$ 附近的区域看起来像是 $r = 2$ 时映射的倒置版本。对于 $r = 3.5$，绘制 $f^{(4)}(x)$。注意在 $x = \frac{1}{2}$ 附近的相似映射。事实上，在我们改变 $r$ 以获得倍周期分岔后，单峰映射以缩放形式重新出现，这是每个后续倍周期分岔相互跟随的基本原因。普适性来自于这样一个事实：经过几次倍周期分岔后，这些单峰映射的形状变得与原始映射无关。
   - **d)** 正弦映射的分岔图

     绘制正弦映射的分岔图：
     $$
     x_{n + 1} = \mu \sin (\pi x_n)
     $$
     其中 $0 < \mu < 1$。它看起来与逻辑斯蒂映射的分岔图相似吗？

   **答** a) 可以先尝试采用数值模拟的方式，得到的结果可能对模拟的初值有一定的敏感性：

   ![搜索得到的周期 8 吸引子蛛网图](./plots/period-8-search-cobweb.py)

   对于逻辑斯蒂映射 $x_{n+1} = f(x_n) = r x_n (1 - x_n)$，周期8吸引子对应参数 $r$ 使得系统存在稳定的周期8轨道。寻找周期8吸引子可以通过最小化李雅普诺夫指数来实现，因为在周期窗口内，李雅普诺夫指数为负，且在窗口中心达到最小值（最负）。

   李雅普诺夫指数定义为：
   $$
   \lambda(r) = \lim_{n\to\infty} \frac{1}{n} \sum_{i=0}^{n-1} \ln |f'(x_i)|
   $$
   其中 $f'(x) = r(1 - 2x)$。数值计算时，取充分大的 $n$，并舍弃瞬态过程。

   在周期8窗口内，$\lambda(r)$ 为负值，且关于窗口中心对称，在中心处达到最小。因此，在给定区间 $[r_{\min}, r_{\max}]$ 上通过优化算法寻找 $\lambda(r)$ 的最小值点，即可找到周期8窗口中最稳定的参数。查找的区间来源于此前模拟出的经验值，此外再尝试在 $3.6<r<3.65$ 中进行查找，验证此方法的适用性。

   ```python
   import numpy as np
   from scipy.optimize import minimize_scalar

   def logistic_map(r, x):
       return r * x * (1 - x)

   def lyapunov_exponent(r, x0=0.5, n_transient=10000, n_iter=50000):
       """计算逻辑斯蒂映射的李雅普诺夫指数"""
       # 舍弃瞬态
       x = x0
       for _ in range(n_transient):
           x = logistic_map(r, x)

       # 计算李雅普诺夫指数
       lyap_sum = 0.0
       for _ in range(n_iter):
           x = logistic_map(r, x)
           df = abs(r * (1 - 2 * x))
           if df > 1e-12:  # 避免log(0)
               lyap_sum += np.log(df)
       return lyap_sum / n_iter

   # 在区间 [3.6, 3.65] 内最小化李雅普诺夫指数
   res = minimize_scalar(lyapunov_exponent, bounds=(3.6, 3.65), method='bounded')
   r_opt = res.x
   lyap_opt = res.fun

   print(f"最小李雅普诺夫指数对应的 r = {r_opt:.6f}")
   print(f"对应的李雅普诺夫指数 λ = {lyap_opt:.6f}")

   # 验证周期8：检查最后若干次迭代是否呈现周期8
   def check_period(r, x0=0.5, n_transient=10000, n_check=200, tol=1e-8):
       x = x0
       for _ in range(n_transient):
           x = logistic_map(r, x)

       # 记录轨迹
       trajectory = []
       for _ in range(n_check):
           x = logistic_map(r, x)
           trajectory.append(x)

       # 检查周期，从1到20
       for period in range(1, 21):
           if period < n_check:
               # 检查最后period个点是否与前面period个点一致
               diff = np.array(trajectory[-period:]) - np.array(trajectory[-2*period:-period])
               if np.max(np.abs(diff)) < tol:
                   return period
       return None

   period = check_period(r_opt)
   print(f"在 r = {r_opt:.6f} 处检测到的周期为 {period}")

   # 在区间 [3.66, 3.67] 内最小化李雅普诺夫指数
   res = minimize_scalar(lyapunov_exponent, bounds=(3.66, 3.67), method='bounded')
   r_opt = res.x
   lyap_opt = res.fun

   print(f"最小李雅普诺夫指数对应的 r = {r_opt:.6f}")
   print(f"对应的李雅普诺夫指数 λ = {lyap_opt:.6f}")

   period = check_period(r_opt)
   print(f"在 r = {r_opt:.6f} 处检测到的周期为 {period}")
   ```

   运行结果：

   ```
   最小李雅普诺夫指数对应的 r = 3.627558
   对应的李雅普诺夫指数 λ = -1.765538
   在 r = 3.627558 处检测到的周期为 6
   最小李雅普诺夫指数对应的 r = 3.662190
   对应的李雅普诺夫指数 λ = -0.513869
   在 r = 3.662190 处检测到的周期为 8
   ```

   作图进行验证：

   ![r = 3.627558 与 r = 3.662190 时的蛛网图对比](./plots/period-8-cobweb-comparison.py)

   b) 对于逻辑斯蒂映射 $x_{n+1} = f(x) = r x (1 - x)$，稳态解满足 $x = f(x)$，解得 $x_0^* = 0$ 和 $x_1^* = 1 - 1/r$（当 $r > 1$ 时）。

   稳态解的线性稳定性由导数 $f'(x^*) = r(1 - 2x^*)$ 的绝对值决定：
   - 对于 $x_0^* = 0$，$f'(0) = r$，故当 $0 < r < 1$ 时稳定，$r > 1$ 时不稳定。
   - 对于 $x_1^* = 1 - 1/r$，$f'(x_1^*) = r(1 - 2(1 - 1/r)) = 2 - r$。稳定性条件为 $|2 - r| < 1$，即 $1 < r < 3$。因此当 $r > 3$ 时，稳态解 $x_1^*$ 失稳。

   当 $r > 3$ 时，系统出现周期2解，满足 $x = f^{(2)}(x) = f(f(x))$ 且 $x \neq f(x)$。周期2解对应方程 $f^{(2)}(x) - x = 0$ 的两个根（除去 $x_0^*$ 和 $x_1^*$）。记周期2解为 $p$ 和 $q$，满足 $q = f(p)$，$p = f(q)$。

   周期2解的稳定性由复合函数 $f^{(2)}$ 在 $p$ 和 $q$ 处的导数乘积决定：
   $$
   \frac{\mathrm{d}}{\mathrm{d}x} f^{(2)}(x)\bigg|_{x=p} = f'(f(p)) f'(p) = f'(q) f'(p)
   $$
   同理在 $q$ 处相同。由于 $f'(x) = r(1 - 2x)$，故稳定性条件为 $|f'(p) f'(q)| < 1$。

   通过求解 $f^{(2)}(x) - x = 0$，可得 $p$ 和 $q$ 满足二次方程：
   $$
   r^2 x^2 - r(r+1) x + (r+1) = 0
   $$
   利用韦达定理：$p + q = \frac{r+1}{r}$，$pq = \frac{r+1}{r^2}$。计算：
   $$
   f'(p) f'(q) = r^2 (1 - 2p)(1 - 2q) = r^2 \left[1 - 2(p+q) + 4pq\right] = -r^2 + 2r + 4
   $$
   稳定性条件 $| -r^2 + 2r + 4 | < 1$ 等价于：
   1. $-r^2 + 2r + 4 < 1$ 即 $r^2 - 2r - 3 > 0$，解得 $r > 3$ 或 $r < -1$，结合 $r>0$ 得 $r>3$。
   2. $-r^2 + 2r + 4 > -1$ 即 $r^2 - 2r - 5 < 0$，解得 $1 - \sqrt{6} < r < 1 + \sqrt{6}$。

   综合得 $3 < r < 1 + \sqrt{6}$。证毕。

   选取几个值进行模拟：

   ![f(f(x)) 的不动点及周期 2 解的稳定性分析](./plots/period-2-stability.py)

   c) 分岔图的作图代码与结果见正文 3.1.3 的图（逻辑斯谛映射的分岔图）。关键是对所有 $r$ 同时迭代（向量化），舍弃瞬态后记录吸引子上的点：

   ```python
   import numpy as np
   import matplotlib.pyplot as plt

   def bifurcation(f, params, n_transient=1000, n_record=200, x0=0.3):
       """Iterate the map for all parameter values at once; return the attractor points."""
       x = np.full_like(params, x0)
       for _ in range(n_transient):
           x = f(params, x)
       P, X = [], []
       for _ in range(n_record):
           x = f(params, x)
           P.append(params)
           X.append(x)
       return np.concatenate(P), np.concatenate(X)

   logistic = lambda r, x: r * x * (1 - x)
   sine = lambda mu, x: mu * np.sin(np.pi * x)

   fig, axes = plt.subplots(1, 2, figsize=(10, 4))
   for ax, f, grid, label in [(axes[0], logistic, np.linspace(2.5, 4.0, 3000), 'r'),
                              (axes[1], sine, np.linspace(0.6, 1.0, 3000), 'mu')]:
       p, x = bifurcation(f, grid)
       ax.plot(p, x, ',', alpha=0.3)
       ax.set_xlabel(label)
       ax.set_ylabel('x')
   ```

   这里 $\delta r = 5\times10^{-4}$，$n_{\mathrm{transient}} = 1000$，$n_{\mathrm{period}} = 200$。图中依次可见 $r_1 = 3$、$r_2 = 1 + \sqrt6 \approx 3.4495$、$r_3 \approx 3.5441$、$r_4 \approx 3.5644$ 处的倍周期分岔，它们在 $r_\infty \approx 3.5699$ 处累积，之后是混沌带与其中的周期窗口（最宽的是从 $r = 1 + 2\sqrt2 \approx 3.8284$ 开始的周期 3 窗口）。

   $r = 3.2$ 时，$f(f(x)) = x$ 有四个解：$0$ 与 $1 - 1/r = 0.6875$ 是 $f$ 的不动点，在那里 $f(f(x))$ 的斜率分别为 $r^2 = 10.24$ 与 $(2 - r)^2 = 1.44$，都不稳定；另外两个解由 b) 中的二次方程给出，$p = 0.5130$、$q = 0.7995$，那里的斜率 $-r^2 + 2r + 4 = 0.16$，绝对值小于 1，所以 $f$ 的周期 2 解正是 $f(f(x))$ 的一对稳定不动点。

   $f(f(x))$ 在 $x = \frac12$ 附近有一个极小值（$f$ 把 $\frac12$ 映到极大值点 $r/4$，再由 $f$ 的下降段映回较小的值），这一段像倒过来的单峰映射；把它在包含 $p$ 的小方框内放大并翻转，就得到与 $r = 2$ 时的 $f$ 相似的图形（$r = 2$ 时不动点恰为 $x = \frac12$，是超稳定的）。$r = 3.5$ 时 $f^{(4)}$ 在 $x = \frac12$ 附近又出现一个更小、方向又翻转一次的单峰。这就是 3.1.4 中重整化变换 $\mathcal{R}[f](x) = \alpha f(f(x/\alpha))$ 的几何含义（见正文中 $f$、$f(f(x))$ 与 $f^{(4)}$ 的比较图），每翻转一次放大 $\lvert\alpha\rvert \approx 2.5$ 倍。

   d) 用上面的 `bifurcation(sine, …)` 即可，结果见正文 3.1.3 的正弦映射分岔图。$0 < \mu < 1$ 时 $x \mapsto \mu\sin(\pi x)$ 把 $[0, 1]$ 映入自身，在 $x = \frac12$ 处有唯一的二次极大值，与逻辑斯谛映射同属一类单峰映射，所以分岔图的形状几乎相同，只是参数轴的刻度不同。数值计算（周期 $2^k$ 轨道的乘子 $\prod f'(x_i)$ 等于 $-1$ 处）给出正弦映射的倍周期分岔点：

   | $k$ | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | $\mu_k$ | 0.7200 | 0.8333 | 0.8587 | 0.8641 | 0.8653 |

   第一个分岔点也可以直接求：不动点 $x^* = \mu\sin(\pi x^*)$ 处 $\mu\pi\cos(\pi x^*) = -1$，解得 $\mu_1 = 0.71996$。相邻间隔之比 $(\mu_k - \mu_{k-1})/(\mu_{k+1} - \mu_k)$ 依次为 $4.45$、$4.76$、$4.55$，在数值误差内趋于 Feigenbaum 常数 $\delta \approx 4.669$，累积点约为 $\mu_\infty \approx 0.8655$。两个映射的分岔点位置不同，但收敛的比值相同，周期窗口出现的先后次序也相同：这正是 3.1.4 所说的普适性。

3. 在实验室中，研究人员对草履虫（*Paramecium caudatum*）种群的增长进行了监测。每隔24小时测量一次种群密度，得到以下数据：

   | 时间 t (h)             | 0   | 1    | 2    | 3    | 4    | 5     | 6     | 7     | 8     |
   | ---------------------- | --- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- |
   | 种群密度 N (个体数/mL) | 9.6 | 18.3 | 29.0 | 47.2 | 71.1 | 119.1 | 174.6 | 257.3 | 350.7 |

   | 9     | 10    | 11    | 12    | 13    | 14    | 15    | 16    | 17    | 18    |
   | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
   | 441.0 | 513.3 | 559.7 | 594.8 | 629.4 | 640.9 | 651.1 | 655.9 | 659.6 | 661.8 |

   **一、问题描述**

   使用以下两种方法拟合逻辑斯谛增长模型，并估计参数 $K$（环境容纳量）、$r$（内禀增长率）和 $N_0$（初始种群密度）：
   1. **非线性最小二乘拟合**：直接最小化原始数据的残差平方和。
   2. **线性化拟合（三点法）**：使用等间隔三点的数据计算 $K$，然后线性回归得到其他参数。

   **答**

   **二、模型与方法**

   **1. 逻辑斯谛增长模型**

   逻辑斯谛微分方程及其解析解为：
   $$
   \frac{\mathrm{d}N}{\mathrm{d}t} = r N \left(1 - \frac{N}{K}\right), \quad
   N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) \mathrm{e}^{-rt}}.
   $$

   **2. 拟合方法**

   **(1) 非线性最小二乘拟合**
   直接使用 `scipy.optimize.curve_fit` 函数拟合 $N(t)$，最小化残差平方和：
   $$
   \min_{K, r, N_0} \sum_{i=1}^{n} \left[N_i - N(t_i; K, r, N_0)\right]^2.
   $$

   **(2) 线性化拟合（三点法）**
   - **三点法计算 $K$**：选取等间隔的三个时间点 $t_0, t_1 = t_0 + \Delta t, t_2 = t_0 + 2\Delta t$，对应的种群数量为 $N_0, N_1, N_2$。由解析解的性质可得：
   $$
   K = \frac{N_1^2 (N_0 + N_2) - 2 N_0 N_1 N_2}{N_1^2 - N_0 N_2}.
   $$
   这里我们选择 $t_0 = 0$（$N_0 = 9.6$），$t_1 = 9$（$N_1 = 441.0$），$t_2 = 18$（$N_2 = 661.8$），$\Delta t = 9$ 小时。

   - **线性回归求 $r$ 和 $N_0$**：对变换后的方程进行线性回归：
   $$
   \ln\left(\frac{K - N}{N}\right) = \ln\left(\frac{K - N_0}{N_0}\right) - r t.
   $$
   令 $y = \ln\left(\dfrac{K - N}{N}\right)$，则 $y = a - r t$，其中 $a = \ln\left(\dfrac{K - N_0}{N_0}\right)$。通过线性回归得到 $a$ 和 $r$，然后：
   $$
   N_0 = \frac{K}{1 + \mathrm{e}^{a}}.
   $$

   **三、代码实现与结果**

   ![草履虫种群增长的逻辑斯谛拟合：拟合曲线、残差与拟合优度](./plots/paramecium-logistic-fit.py)

   ```python
   import numpy as np
   import matplotlib.pyplot as plt
   from scipy.optimize import curve_fit
   from scipy.stats import linregress
   from sklearn.metrics import r2_score

   # 实验数据
   t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
   N = np.array([9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 
                 441.0, 513.3, 559.7, 594.8, 629.4, 640.9, 651.1, 655.9, 659.6, 661.8])

   # ====================== 方法1：非线性最小二乘拟合 ======================
   def logistic_model(t, K, r, N0):
       """逻辑斯谛增长模型"""
       return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

   # 初始参数猜测（K ≈ 660, r ≈ 0.5, N0 ≈ 10）
   initial_guess = [660, 0.5, 10]
   params_nonlin, cov_nonlin = curve_fit(logistic_model, t, N, p0=initial_guess, maxfev=5000)
   K_nonlin, r_nonlin, N0_nonlin = params_nonlin
   # 计算参数的标准误差
   params_err_nonlin = np.sqrt(np.diag(cov_nonlin))

   # 计算预测值和拟合优度
   N_pred_nonlin = logistic_model(t, K_nonlin, r_nonlin, N0_nonlin)
   SSE_nonlin = np.sum((N - N_pred_nonlin)**2)
   R2_nonlin = r2_score(N, N_pred_nonlin)
   RMSE_nonlin = np.sqrt(SSE_nonlin / len(N))

   # ====================== 方法2：线性化拟合（三点法） ======================
   # 选择三个等间隔的点：t=0, t=9, t=18
   idx0, idx1, idx2 = 0, 9, 18
   N0_data, N1_data, N2_data = N[idx0], N[idx1], N[idx2]
   Δt = t[idx1] - t[idx0]

   # 三点法计算K
   K_linear = (N1_data**2 * (N0_data + N2_data) - 2 * N0_data * N1_data * N2_data) / (N1_data**2 - N0_data * N2_data)
   print(f"三点法计算的 K = {K_linear:.2f}")

   # 线性回归求 r 和 N0
   # 注意：当 N 接近 K 时，(K-N)/N 可能为负或零，这里仅使用 N < K 的数据点进行回归
   valid_mask = N < K_linear * 0.999  # 避免对数中出现非正数
   t_valid = t[valid_mask]
   N_valid = N[valid_mask]

   # 计算 y = ln((K-N)/N)
   y = np.log((K_linear - N_valid) / N_valid)

   # 线性回归：y = a - r*t
   slope, intercept, r_value, p_value, std_err = linregress(t_valid, y)
   r_linear = -slope
   a = intercept
   # 计算 N0
   N0_linear = K_linear / (1 + np.exp(a))

   # 计算预测值和拟合优度
   N_pred_linear = logistic_model(t, K_linear, r_linear, N0_linear)
   SSE_linear = np.sum((N - N_pred_linear)**2)
   R2_linear = r2_score(N, N_pred_linear)
   RMSE_linear = np.sqrt(SSE_linear / len(N))

   # ====================== 结果输出 ======================
   print("=" * 60)
   print("非线性最小二乘拟合结果：")
   print(f"  K = {K_nonlin:.2f} ± {params_err_nonlin[0]:.2f}")
   print(f"  r = {r_nonlin:.4f} ± {params_err_nonlin[1]:.4f}")
   print(f"  N0 = {N0_nonlin:.2f} ± {params_err_nonlin[2]:.2f}")
   print(f"  SSE = {SSE_nonlin:.2f}, R² = {R2_nonlin:.6f}, RMSE = {RMSE_nonlin:.2f}")

   print("\n" + "=" * 60)
   print("线性化拟合（三点法）结果：")
   print(f"  K = {K_linear:.2f} (由三点法直接计算)")
   print(f"  r = {r_linear:.4f}")
   print(f"  N0 = {N0_linear:.2f}")
   print(f"  SSE = {SSE_linear:.2f}, R² = {R2_linear:.6f}, RMSE = {RMSE_linear:.2f}")

   print("\n" + "=" * 60)
   print("拟合效果比较：")
   print(f"  非线性拟合SSE减少：{((SSE_linear - SSE_nonlin) / SSE_linear * 100):.2f}%")
   print(f"  非线性拟合R²提高：{((R2_nonlin - R2_linear) * 100):.4f}%")
   ```

   运行结果：

   ```
   三点法计算的 K = 664.29
   ============================================================
   非线性最小二乘拟合结果：
     K = 663.04 ± 1.70
     r = 0.5470 ± 0.0056
     N0 = 9.14 ± 0.38
     SSE = 194.23, R² = 0.999846, RMSE = 3.20

   ============================================================
   线性化拟合结果：
     K = 664.29 (由三点法直接计算)
     r = 0.5386
     N0 = 9.79
     SSE = 231.70, R² = 0.999816, RMSE = 3.49

   ============================================================
   拟合效果比较：
     非线性拟合SSE减少：16.18%
     非线性拟合R²提高：0.0030%
   ```

   我们得到以下拟合结果：

   **1. 非线性最小二乘拟合**
   - $K = 663.04 \pm 1.70$（个体/mL）
   - $r = 0.5470 \pm 0.0056$（/小时）
   - $N_0 = 9.14 \pm 0.38$（个体/mL）
   - $\mathrm{SSE} = 194.23$，$R^2 = 0.999846$，$\mathrm{RMSE} = 3.20$

   **2. 线性化拟合**
   - $K = 664.29$（个体/mL）（由三点法直接计算）
   - $r = 0.5386$（/小时）
   - $N_0 = 9.79$（个体/mL）
   - $\mathrm{SSE} = 231.70$，$R^2 = 0.999816$，$\mathrm{RMSE} = 3.49$

   **3. 拟合效果比较**
   - 非线性拟合的 $\mathrm{SSE}$ 比线性化拟合低 **16.18%**，$R^2$ 提高 **0.003%**。
   - 从残差图可以看出，非线性拟合的残差略小，分布较随机，而线性化拟合在中段存在一定系统偏差。

   **五、讨论与总结**

   1. **参数估计的准确性**：
      - 非线性最小二乘拟合直接最小化原始数据的残差，通常更准确可靠，特别是当数据存在测量误差时。
      - 三点法对所选数据点较为敏感，如果选取的点受噪声影响较大，$K$ 的估计会产生较大偏差。本例中三点法得到的 $K$ 与非线性拟合相近，但 $r$ 和 $N_0$ 略有差异。

   2. **方法适用性**：
      - **非线性拟合**：适用于具有完整增长曲线的数据，能够充分利用所有数据点信息，但需要较好的初始猜测。
      - **线性化拟合（+三点法）**：计算简单，适用于快速估算，但精度较低，且要求数据点等间隔、噪声小。

   3. **生物学意义**：
      - 两种方法得到的 $K$ 均约为 660 个体/mL，表明培养环境的最大容纳量约为 660 个体/mL。
      - 内禀增长率 $r$ 约为 0.54/小时，意味着在无密度制约下，种群每小时增加约 54%。
      - 初始密度 $N_0$ 约为 9 个体/mL，与实验起始值一致。

   **结论**：对于草履虫种群增长数据，非线性最小二乘拟合在统计指标上略优于线性化拟合，但线性拟合具有其便利性，可作为快速估算的辅助手段。
