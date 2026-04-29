## 5.1 基本概念 (General Concepts)

### 5.1.1 假设检验的动机与问题引入

参数假设检验是统计推断的两大主要任务之一，其核心是在总体分布形式已知（如属于分布族 $\{f(x; \theta): \theta \in \Theta\}$ ）的前提下，基于随机样本判断总体参数 $\theta$ 是否属于参数空间 $\Theta$ 的某个特定子集 $\Theta_0$。

#### 1. 基本思想
- **原假设 (Null Hypothesis)**：记为 $H_0: \theta \in \Theta_0$，表示待检验的、通常代表现状或保守观点的假设。
- **备择假设 (Alternative Hypothesis)**：记为 $H_1: \theta \in \Theta_1$，其中 $\Theta_1 = \Theta - \Theta_0$，代表与原假设对立的观点。
- 检验的目标：基于样本数据，决定是“拒绝”还是“接受” $H_0$。

#### 2. 假设的类型
- **简单假设 (Simple Hypothesis)**：如果 $\Theta_0$（或 $\Theta_1$）仅包含一个参数点。
- **复合假设 (Composite Hypothesis)**：如果 $\Theta_0$（或 $\Theta_1$）包含多个参数点。

#### 3. 常见的假设形式（当 $\theta \in \mathbb{R}$ 时）
  1. $H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta = \theta_1$
  2. $H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta > \theta_0$
  3. $H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta < \theta_0$
  4. $H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0$
  5. $H_0: \theta \leq \theta_0 \quad \text{vs} \quad H_1: \theta > \theta_0$
  6. $H_0: \theta \geq \theta_0 \quad \text{vs} \quad H_1: \theta < \theta_0$
  7. $H_0: \theta \leq \theta_1 \text{ 或 } \theta \geq \theta_2 \quad \text{vs} \quad H_1: \theta_1 < \theta < \theta_2$

### 5.1.2 检验的构成：拒绝域与检验函数

基于样本 $\mathbf{X} = (X_1, \cdots, X_n)$ 做出决策，需要构造一个规则。

#### 1. 拒绝域与接受域
- **拒绝域 (Rejection / Critical Region)**：样本空间 $\mathcal{X}$ 的一个子集 $D$，当样本观测值 $\mathbf{x} \in D$ 时，我们拒绝 $H_0$。
- **接受域 (Acceptance Region)**：拒绝域的补集 $D^c = \mathcal{X} - D$，当 $\mathbf{x} \in D^c$ 时，我们接受 $H_0$。

#### 2. 检验函数
- **非随机化检验 (Nonrandomized Test)**：检验函数 $\varphi(\mathbf{x})$ 只取 0 或 1。
  $$
  \varphi(\mathbf{x}) = 
  \begin{cases}
  1, & \text{拒绝 } H_0 \quad (\mathbf{x} \in D) \\
  0, & \text{接受 } H_0 \quad (\mathbf{x} \in D^c)
  \end{cases}
  $$
- **随机化检验 (Randomized Test)**：检验函数 $\varphi(\mathbf{x})$ 可以取 $[0, 1]$ 之间的值，表示拒绝 $H_0$ 的概率。
  $$
  \varphi(\mathbf{x}) =
  \begin{cases}
  1, & T(\mathbf{x}) > c \\
  r, & T(\mathbf{x}) = c \quad (0 < r < 1) \\
  0, & T(\mathbf{x}) < c
  \end{cases}
  $$
  常用于离散分布，以精确控制犯第一类错误的概率。

### 5.1.3 错误类型与检验的功效

#### 1. 两类错误 (Type I and Type II Errors)
- **第一类错误 (弃真)**：$H_0$ 为真时，拒绝了 $H_0$。其概率记为 $\alpha(\theta)$。
  $$
  \alpha(\theta) = P_\theta(\text{拒绝 } H_0) = E_\theta[\varphi(\mathbf{X})], \quad \theta \in \Theta_0
  $$
- **第二类错误 (取伪)**：$H_0$ 为假时，接受了 $H_0$。其概率记为 $\beta(\theta)$。
  $$
  \beta(\theta) = P_\theta(\text{接受 } H_0) = 1 - E_\theta[\varphi(\mathbf{X})], \quad \theta \in \Theta_1
  $$

#### 2. 显著性水平与功效函数
- **显著性水平 (Level of Significance)**：犯第一类错误的最大概率，记为 $\alpha$。
  $$
  \alpha = \max_{\theta \in \Theta_0} \alpha(\theta)
  $$
  通常预先设定为一个小值（如 0.05, 0.01）。
- **功效函数 (Power Function)**：检验函数 $\varphi$ 拒绝 $H_0$ 的概率，是参数 $\theta$ 的函数。
  $$
  \pi_\varphi(\theta) = P_\theta(\text{拒绝 } H_0) = E_\theta[\varphi(\mathbf{X})]
  $$
  当 $\theta \in \Theta_1$ 时，$\pi_\varphi(\theta)$ 越大越好；当 $\theta \in \Theta_0$ 时，希望 $\pi_\varphi(\theta) \leq \alpha$。

### 5.1.4 Neyman-Pearson 原则与 p 值

#### 1. Neyman-Pearson 原则
  1. 首先控制第一类错误的概率不超过预先设定的显著性水平 $\alpha$。
  2. 在此约束下，尽可能使第二类错误的概率最小（即功效最大）。

#### 2. p 值 (p-value)
- **定义**：在原假设 $H_0$ 成立下，获得与当前样本同样极端或更极端结果的概率。
- **作用**：衡量反对 $H_0$ 的证据强度。p 值越小，证据越强。
- **决策规则**：若 p 值 $\leq \alpha$，则拒绝 $H_0$。
- **常见形式的 p 值**：
  - 双侧检验 $H_0: \theta = \theta_0$ vs $H_1: \theta \neq \theta_0$：
    $$
    p = P_{\theta_0}(|T(\mathbf{X})| \geq |t(\mathbf{x})|)
    $$
  - 右侧检验 $H_0: \theta \leq \theta_0$ vs $H_1: \theta > \theta_0$：
    $$
    p = P_{\theta_0}(T(\mathbf{X}) \geq t(\mathbf{x}))
    $$
  - 左侧检验 $H_0: \theta \geq \theta_0$ vs $H_1: \theta < \theta_0$：
    $$
    p = P_{\theta_0}(T(\mathbf{X}) \leq t(\mathbf{x}))
    $$

### 5.1.5 假设检验的一般步骤
1. **提出假设**：根据实际问题确定原假设 $H_0$ 和备择假设 $H_1$。
2. **选择检验统计量**：选取一个能较好区分 $H_0$ 和 $H_1$ 的样本函数 $T(\mathbf{X})$，并确定其抽样分布。
3. **确定拒绝域形式**：根据 $H_1$ 的方向（单侧或双侧）确定拒绝域 $D$ 的形式（如 $T > c$, $T < c$, $|T| > c$）。
4. **确定临界值**：根据显著性水平 $\alpha$ 和 $T(\mathbf{X})$ 在 $H_0$ 下的分布，确定临界值 $c$。
5. **计算并决策**：根据样本观测值计算检验统计量的值 $t(\mathbf{x})$，若 $t(\mathbf{x}) \in D$ 则拒绝 $H_0$，否则接受 $H_0$。通常也计算 p 值以提供更多信息。

## 5.2 各种总体下的参数假设检验 (Testing Hypotheses for Parameters in Various Populations)

### 5.2.1 单正态总体下的参数检验 (Testing Parameters in a Single Normal Population)

设 $X_1, \cdots, X_n \stackrel{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$。

#### 5.2.1.1 方差已知时均值的检验 (Test for Normal Mean μ when σ² is known)

检验问题：
1. $H_0: \mu = \mu_0 \quad \text{vs.} \quad H_1: \mu \neq \mu_0$ （双侧）
2. $H_0: \mu \leq \mu_0 \quad \text{vs.} \quad H_1: \mu > \mu_0$ （右侧单侧）
3. $H_0: \mu \geq \mu_0 \quad \text{vs.} \quad H_1: \mu < \mu_0$ （左侧单侧）

**检验统计量**：
$$
Z = \frac{\sqrt{n}(\bar{X} - \mu_0)}{\sigma} \stackrel{H_0}{\sim} N(0,1).
$$

**拒绝域**：
- 双侧：$D = \{ |Z| > z_{\alpha/2} \}$
- 右侧单侧：$D = \{ Z > z_\alpha \}$
- 左侧单侧：$D = \{ Z < -z_\alpha \}$

**功效函数**（以双侧检验为例）：
$$
\pi_1(\mu) = 1 - \Phi\left( z_{\alpha/2} + \frac{\sqrt{n}(\mu_0 - \mu)}{\sigma} \right) + \Phi\left( -z_{\alpha/2} + \frac{\sqrt{n}(\mu_0 - \mu)}{\sigma} \right).
$$

#### 5.2.1.2 方差未知时均值的检验 (Test for Normal Mean μ when σ² is unknown)

**检验统计量**：
$$
T = \frac{\sqrt{n}(\bar{X} - \mu_0)}{S} \stackrel{H_0}{\sim} t_{n-1}, \quad \text{其中 } S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2.
$$

**拒绝域**：
- 双侧：$D = \{ |T| > t_{n-1,\alpha/2} \}$
- 右侧单侧：$D = \{ T > t_{n-1,\alpha} \}$
- 左侧单侧：$D = \{ T < -t_{n-1,\alpha} \}$

#### 5.2.1.3 均值已知时方差的检验 (Test for Normal Variance σ² when μ is known)

检验问题：
1. $H_0: \sigma^2 = \sigma_0^2 \quad \text{vs.} \quad H_1: \sigma^2 \neq \sigma_0^2$
2. $H_0: \sigma^2 \leq \sigma_0^2 \quad \text{vs.} \quad H_1: \sigma^2 > \sigma_0^2$
3. $H_0: \sigma^2 \geq \sigma_0^2 \quad \text{vs.} \quad H_1: \sigma^2 < \sigma_0^2$

**检验统计量**：
$$
\chi^2 = \sum_{i=1}^n \left( \frac{X_i - \mu}{\sigma_0} \right)^2 \stackrel{H_0}{\sim} \chi_n^2.
$$

**拒绝域**（以双侧为例）：
$$
D = \left\{ \chi^2 < \chi_{n,1-\alpha/2}^2 \ \text{或} \ \chi^2 > \chi_{n,\alpha/2}^2 \right\}.
$$

#### 5.2.1.4 均值未知时方差的检验 (Test for Normal Variance σ² when μ is unknown)

**检验统计量**：
$$
\chi^2 = \frac{(n-1)S^2}{\sigma_0^2} \stackrel{H_0}{\sim} \chi_{n-1}^2.
$$

**拒绝域**（以双侧为例）：
$$
D = \left\{ \chi^2 < \chi_{n-1,1-\alpha/2}^2 \ \text{或} \ \chi^2 > \chi_{n-1,\alpha/2}^2 \right\}.
$$

### 5.2.2 非正态总体下的参数检验 (Testing Parameters in Non-normal Distribution)

#### 5.2.2.1 二项分布参数θ的检验 (Test for $B(1, \theta)$)

设 $X_1, \cdots, X_n \stackrel{\text{i.i.d.}}{\sim} B(1, \theta)$，记 $T(X) = \sum_{i=1}^n X_i \sim B(n, \theta)$。

对于检验问题 $H_0: \theta \leq \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$，常用随机化检验：
$$
\varphi(X) = \begin{cases}
1, & T(X) > c, \\
r, & T(X) = c, \\
0, & T(X) < c,
\end{cases}
$$
其中 $c$ 和 $r$ 由 $E_{\theta_0}[\varphi(X)] = \alpha$ 确定。

**大样本近似**：当 $n$ 较大时，由中心极限定理，
$$
U = \frac{\sqrt{n}(\bar{X} - \theta_0)}{\sqrt{\theta_0(1-\theta_0)}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} N(0,1),
$$
拒绝域为 $U > z_\alpha$（右侧单侧）。

#### 5.2.2.2 泊松分布参数θ的检验 (Test for $P(\theta)$)

设 $X_1, \cdots, X_n \stackrel{\text{i.i.d.}}{\sim} P(\theta)$。

**大样本近似**：当 $n$ 较大时，
$$
U_0 = \frac{\sqrt{n}(\bar{X} - \theta_0)}{\sqrt{\theta_0}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} N(0,1),
$$
拒绝域为 $|U_0| > z_{\alpha/2}$（双侧）等。

### 5.2.3 两个正态总体下的参数检验 (Testing Parameters in Two Normal Populations)

设 $X_1, \cdots, X_m \stackrel{\text{i.i.d.}}{\sim} N(\mu_1, \sigma_1^2)$，$Y_1, \cdots, Y_n \stackrel{\text{i.i.d.}}{\sim} N(\mu_2, \sigma_2^2)$，且两组样本独立。

#### 5.2.3.1 两总体均值差的检验 (Test for $\mu_1 - \mu_2$)

**（1）方差 $\sigma_1^2, \sigma_2^2$ 已知**

检验统计量：
$$
U = \frac{(\bar{X} - \bar{Y}) - \mu_0}{\sqrt{\sigma_1^2/m + \sigma_2^2/n}} \stackrel{H_0}{\sim} N(0,1),
$$
其中 $\mu_0$ 为假设的差值。拒绝域形式同单总体 $U$ 检验。

**（2）方差未知但相等（$\sigma_1^2 = \sigma_2^2 = \sigma^2$）**

检验统计量：
$$
T = \frac{(\bar{X} - \bar{Y}) - \mu_0}{\sqrt{S_p^2 \left( \frac{1}{m} + \frac{1}{n} \right)}} \stackrel{H_0}{\sim} t_{m+n-2},
$$
其中 $S_p^2 = \frac{(m-1)S_X^2 + (n-1)S_Y^2}{m+n-2}$ 为合并样本方差。拒绝域形式同单总体 $t$ 检验。

**（3）方差未知且不等（Behrens-Fisher 问题）**

当 $m, n$ 不大时，可采用 Welch 近似：
$$
T_* = \frac{(\bar{X} - \bar{Y}) - \mu_0}{\sqrt{S_X^2/m + S_Y^2/n}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} t_r,
$$
其中自由度 $r$ 由下式近似（取最接近的整数）：
$$
r = \frac{\left( \frac{S_X^2}{m} + \frac{S_Y^2}{n} \right)^2}{\frac{S_X^4}{m^2(m-1)} + \frac{S_Y^4}{n^2(n-1)}}.
$$

#### 5.2.3.2 两总体方差比的检验 (Test for $\sigma_1^2 / \sigma_2^2$)

**（1）均值 $\mu_1, \mu_2$ 未知**

检验统计量：
$$
F = \frac{S_Y^2}{S_X^2} \stackrel{H_0}{\sim} F_{n-1, m-1}, \quad \text{当 } \sigma_1^2 = \sigma_2^2 \text{ 时}.
$$
对于 $H_0: \sigma_2^2 / \sigma_1^2 = 1 \ \text{vs.} \ H_1: \sigma_2^2 / \sigma_1^2 \neq 1$，拒绝域为：
$$
D = \left\{ F < F_{n-1, m-1, 1-\alpha/2} \ \text{或} \ F > F_{n-1, m-1, \alpha/2} \right\}.
$$

**（2）均值 $\mu_1, \mu_2$ 已知**

检验统计量：
$$
F_k = \frac{S_{Y*}^2}{S_{X*}^2} = \frac{\frac{1}{n}\sum_{i=1}^n (Y_i - \mu_2)^2}{\frac{1}{m}\sum_{i=1}^m (X_i - \mu_1)^2} \stackrel{H_0}{\sim} F_{n, m}.
$$
拒绝域形式类似，但自由度不同。

### 5.2.4 成对比较 (Paired Comparison)

当成对数据 $(X_i, Y_i)$ 存在相依性时（如治疗前后比较），可考虑差值 $Z_i = Y_i - X_i$。若 $Z_i \stackrel{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$，则检验 $H_0: \mu = 0$ 可化为单样本 $t$ 检验：
$$
T = \frac{\sqrt{n}\bar{Z}}{S_Z} \stackrel{H_0}{\sim} t_{n-1}.
$$

### 5.2.5 大样本理论下的假设检验 (Hypothesis Testing Based on Large Sample Theory)

#### 5.2.5.1 中心极限定理的应用 (Application of CLT)

设 $X_1, \cdots, X_n \stackrel{\text{i.i.d.}}{\sim} F$，$E[X_i] = \mu$，$\operatorname{Var}(X_i) = \sigma^2 < \infty$。由中心极限定理及 Slutsky 定理，当 $n$ 较大时，
$$
\frac{\sqrt{n}(\bar{X} - \mu)}{S} \overset{d}{\to} N(0,1).
$$
因此，对于均值的检验，即使总体分布非正态，也可使用基于正态近似的 $U$ 检验。

#### 5.2.5.2 两总体均值差的大样本检验 (Large Sample Test for $\mu_1 - \mu_2$ when $\sigma_1^2, \sigma_2^2$ unknown)

当 $m, n$ 都较大时，
$$
U^* = \frac{(\bar{X} - \bar{Y}) - \mu_0}{\sqrt{S_X^2/m + S_Y^2/n}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} N(0,1).
$$
拒绝域同基于正态的检验。

#### 5.2.5.3 二项分布参数的大样本检验 (Large Sample Test for the Mean $\theta$ of $B(1, \theta)$)

当 $n$ 较大时，
$$
U = \frac{\sqrt{n}(\bar{X} - \theta_0)}{\sqrt{\theta_0(1-\theta_0)}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} N(0,1).
$$

#### 5.2.5.4 泊松分布参数的大样本检验 (Large Sample Test for the Mean $\theta$ of $P(\theta)$)

当 $n$ 较大时，
$$
U_0 = \frac{\sqrt{n}(\bar{X} - \theta_0)}{\sqrt{\theta_0}} \stackrel{H_0}{\overset{\text{approx}}{\sim}} N(0,1).
$$

## 5.3 似然比检验 (Likelihood Ratio Test)

### 5.3.1 动机与原理 (Motivation and Rationale)

似然比检验由 J. Neyman 和 E.S. Pearson 于 1928 年提出，其思想是比较原假设参数空间 $\Theta_0$ 和全参数空间 $\Theta$ 下的最大似然值。若原假设为真，则两个最大似然值应接近；若为假，则差距较大。

### 5.3.2 似然比检验的定义 (Definition of Likelihood Ratio Test)

设样本 $X$ 的似然函数为 $L(\theta) = f(X; \theta)$，$\hat{\theta}_{\text{MLE},0}$ 为 $\Theta_0$ 上的极大似然估计，$\hat{\theta}_{\text{MLE}}$ 为 $\Theta$ 上的极大似然估计。则似然比统计量为：
$$
\lambda(X) = \frac{L(\hat{\theta}_{\text{MLE},0})}{L(\hat{\theta}_{\text{MLE}})} = \frac{\sup_{\theta \in \Theta_0} L(\theta)}{\sup_{\theta \in \Theta} L(\theta)}.
$$
由于 $\lambda(X) \in [0,1]$，当 $\lambda(X)$ 过小时拒绝 $H_0$。拒绝域通常取 $\{ \lambda(X) < \lambda_0 \}$ 或等价地 $\{ -2\log \lambda(X) > C \}$。

### 5.3.3 例子与应用 (Examples and Applications)

#### 5.3.3.1 柯西分布的例子 (Example with Cauchy Distribution)

设 $X \sim \text{Cauchy}(\theta)$，p.d.f. 为 $f(x;\theta) = \frac{1}{\pi} \cdot \frac{1}{1+(x-\theta)^2}$。检验 $H_0: \theta = 0 \ \text{vs.} \ H_1: \theta \neq 0$。
易得 $\hat{\theta}_{\text{MLE}} = X$，故
$$
\lambda = \frac{f(X;0)}{f(X;X)} = \frac{1/(1+X^2)}{1} = \frac{1}{1+X^2}.
$$
拒绝域为 $\lambda < \lambda_0$，即 $|X| > C$，其中 $C = \tan\left( \frac{(1-\alpha)\pi}{2} \right)$。

#### 5.3.3.2 负指数分布的例子 (Example with Negative Exponential Distribution)

设 $X_1, \cdots, X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\theta)$，p.d.f. 为 $f(x;\theta) = \theta e^{-\theta x}, x>0$。检验 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \neq \theta_0$。
似然函数 $L(\theta) = \theta^n e^{-\theta T}$，其中 $T = \sum_{i=1}^n X_i$。MLE 为 $\hat{\theta} = n/T$。
似然比：
$$
\lambda = \frac{\theta_0^n e^{-\theta_0 T}}{(n/T)^n e^{-n}} = \left( \frac{e\theta_0}{n} \right)^n T^n e^{-\theta_0 T}.
$$
拒绝域 $\lambda < \lambda_0$ 等价于 $T e^{-(\theta_0/n)T} < C_0$，进一步可化为 $T < C_1$ 或 $T > C_2$，其中 $C_1, C_2$ 由 $P_{\theta_0}(T < C_1) = P_{\theta_0}(T > C_2) = \alpha/2$ 确定。

### 5.3.4 线性回归中的似然比检验 (Likelihood Ratio Test in Linear Regression)
在线性回归模型 $Y = X\beta + \epsilon$ 中，假设随机误差 $\epsilon_i \stackrel{\text{i.i.d.}}{\sim} N(0, \sigma^2)$。检验单个回归系数 $\beta_j$ 的显著性，即 $H_{0j}: \beta_j = 0$。

**参数空间与似然函数**：
- 全参数空间 $\Theta = \{(\beta, \sigma^2)\} \in \mathbb{R}^{p+2}$，维度 $k = p+2$。
- 零假设参数空间 $\Theta_0 = \{(\beta, \sigma^2): \beta_j=0\} \in \mathbb{R}^{p+1}$，维度 $s = p+1$。
- 似然函数：$L(\beta, \sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left\{ -\frac{||Y - X\beta||_2^2}{2\sigma^2} \right\}$。

**最大似然估计**：
- $\Theta$ 上的 MLE：$\hat{\beta}_{\text{MLE}} = (X^TX)^{-1}X^TY$，$\hat{\sigma}^2_{\text{MLE}} = \frac{1}{n} ||Y - X\hat{\beta}_{\text{MLE}}||_2^2$。
- $\Theta_0$ 上的 MLE：记 $\beta_{-j}$ 为去掉 $\beta_j$ 的向量，$X_{-j}$ 为去掉第 $j$ 列的设计矩阵。$\hat{\beta}_{\text{MLE},0} = (X_{-j}^T X_{-j})^{-1}X_{-j}^TY$，$\hat{\sigma}^2_{\text{MLE},0} = \frac{1}{n} ||Y - X_{-j}\hat{\beta}_{\text{MLE},0}||_2^2$。

**似然比统计量**：
$$
\lambda = \left( \frac{\hat{\sigma}^2_{\text{MLE}}}{\hat{\sigma}^2_{\text{MLE},0}} \right)^{n/2} = \left( \frac{||Y - X\hat{\beta}_{\text{MLE}}||_2^2}{||Y - X_{-j}\hat{\beta}_{\text{MLE},0}||_2^2} \right)^{n/2}
$$

**大样本性质**：由定理1，当 $n \to \infty$ 时，在原假设 $H_{0j}$ 下，
$$
-2\log\lambda \overset{d}{\to} \chi_1^2.
$$
近似水平为 $\alpha$ 的拒绝域为：$-2\log\lambda > \chi^2_{1,\alpha}$。

### 5.3.5 检验回归模型的整体显著性 (Testing Overall Significance of the Linear Model)
检验所有斜率系数是否均为零：$H_0: \beta_1 = \beta_2 = \cdots = \beta_p = 0$。

**参数空间**：
- 全参数空间 $\Theta$ 维度 $k = p+2$。
- 零假设参数空间 $\Theta_0 = \{(\beta_0, \sigma^2)\}$ 维度 $s = 2$。

**最大似然估计**：
- $\Theta_0$ 上的 MLE：$\hat{\beta}_0 = \bar{y}$，$\hat{\sigma}^2_0 = \frac{1}{n} ||Y - \bar{y}||_2^2$。

**似然比统计量**：
$$
\lambda = \left( \frac{\hat{\sigma}^2_{\text{MLE}}}{\hat{\sigma}^2_0} \right)^{n/2} = \left( \frac{||Y - X\hat{\beta}_{\text{MLE}}||_2^2}{||Y - \bar{y}||_2^2} \right)^{n/2}
$$

**精确检验（F检验）**：
利用平方和分解 $||Y - \bar{y}||_2^2 = ||Y - X\hat{\beta}_{\text{MLE}}||_2^2 + ||X\hat{\beta}_{\text{MLE}} - \bar{y}||_2^2$。
可以证明，在原假设 $H_0$ 下：
$$
F = \frac{||X\hat{\beta}_{\text{MLE}} - \bar{y}||_2^2 / p}{||Y - X\hat{\beta}_{\text{MLE}}||_2^2 / (n-p-1)} \sim F_{p, n-p-1}.
$$
水平为 $\alpha$ 的拒绝域为：$F > F_{p, n-p-1, \alpha}$。

### 5.3.6 双因素方差分析中的似然比检验 (Likelihood Ratio Test in Two-Way ANOVA)
考虑模型：$Y_{ij} = \mu + \alpha_i + \beta_j + e_{ij}$，其中 $i=1,\ldots,I$, $j=1,\ldots,J$，$e_{ij} \stackrel{\text{i.i.d.}}{\sim} N(0, \sigma^2)$，且满足 $\sum_i \alpha_i = 0$，$\sum_j \beta_j = 0$。

**检验行效应**：$H_{0,A}: \alpha_1 = \cdots = \alpha_I = 0$。
- 全模型参数空间维度：$I + J$（考虑约束条件后）。
- 零假设（无行效应）模型参数空间维度：$J + 1$。
- 可以构造基于平方和 $SS_A$（行间平方和）和 $SS_e$（误差平方和）的似然比检验。
- 在原假设 $H_{0,A}$ 下，可以证明：
  $$
  F_A = \frac{SS_A / (I-1)}{SS_e / [(I-1)(J-1)]} \sim F_{I-1, (I-1)(J-1)}.
  $$
  拒绝域为 $F_A > F_{I-1, (I-1)(J-1), \alpha}$。

**检验列效应**：$H_{0,B}: \beta_1 = \cdots = \beta_J = 0$，方法类似，检验统计量为 $F_B$，服从 $F_{J-1, (I-1)(J-1)}$ 分布。

## 5.4 一致最大功效检验 (Uniformly Most Powerful Test, UMP Test)

### 5.4.1 定义与动机 (Definition and Motivation)
对于一个固定的检验水平 $\alpha$，可能存在多个不同的检验。UMP检验的目标是在所有水平不超过 $\alpha$ 的检验中，找到一个对于 **所有** $\theta \in \Theta_1$ 都具有最大功效（即犯第二类错误概率最小）的检验。

**定义 (UMP Test)**：考虑检验问题 $H_0: \theta \in \Theta_0 \ \text{vs.} \ H_1: \theta \in \Theta_1$。设 $\varphi$ 是一个水平为 $\alpha$ 的检验。如果对于任何其他水平不超过 $\alpha$ 的检验 $\varphi^*$，都有 $\pi_\varphi(\theta) \geq \pi_{\varphi^*}(\theta)$ 对所有 $\theta \in \Theta_1$ 成立，则称 $\varphi$ 为 **一致最大功效 (UMP) 检验**。

- **局限性**：UMP检验通常只存在于参数为一维，且原假设和备择假设形式简单（如单边检验）的情形下。
- **简单假设**：当 $H_0$ 和 $H_1$ 都是简单假设（即 $\Theta_0$ 和 $\Theta_1$ 都只包含一个点）时，UMP检验的存在性由 **Neyman-Pearson基本引理** 保证。

### 5.4.2 Neyman-Pearson基本引理 (Neyman-Pearson Fundamental Lemma)
**定理 1 (N-P Lemma)**：设样本 $\mathbf{X}$ 的联合 p.d.f. (或 p.m.f.) 为 $f(\boldsymbol{x}; \theta)$。考虑简单对简单的检验问题：$H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta = \theta_1$，显著性水平为 $\alpha \in (0, 1)$。定义检验函数：
$$
\varphi(\boldsymbol{x}) = 
\begin{cases}
1, & f(\boldsymbol{x}; \theta_1) > C f(\boldsymbol{x}; \theta_0), \\
r, & f(\boldsymbol{x}; \theta_1) = C f(\boldsymbol{x}; \theta_0), \\
0, & f(\boldsymbol{x}; \theta_1) < C f(\boldsymbol{x}; \theta_0).
\end{cases}
$$
其中常数 $C \geq 0$ 和 $r \in [0, 1]$ 由条件 $E_{\theta_0}[\varphi(\mathbf{X})] = \alpha$ 确定。则：
1. 这样的 $C$ 和 $r$ 存在。
2. 检验 $\varphi$ 是此检验问题的 **最有效（MP）检验**，即在所有水平不超过 $\alpha$ 的检验中，其功效 $E_{\theta_1}[\varphi(\mathbf{X})]$ 最大。
- 若总体分布连续，通常可取 $r=0$。
- N-P引理是构造UMP检验的基石。

### 5.4.3 由N-P引理构造UMP检验 (Constructing UMP Test via N-P Lemma)
对于复合假设的 **单边检验** 问题，有时可以通过以下步骤构造UMP检验：
1. 在 $\Theta_0$ 中选一个“边界点” $\theta_0$，在 $\Theta_1$ 中任选一点 $\theta_1$。
2. 利用N-P引理构造 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta = \theta_1$ 的MP检验 $\varphi_{\theta_1}$。
3. 如果 $\varphi_{\theta_1}$ 的形式 **不依赖于** 所选取的 $\theta_1$（例如，拒绝域只依赖于样本和 $\theta_0$，而与 $\theta_1$ 的具体值无关），则此检验 $\varphi$ 就是原复合假设 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \in \Theta_1$ 的UMP检验。
4. 进一步，如果还能证明该检验 $\varphi$ 对于所有 $\theta \in \Theta_0$（不仅是 $\theta_0$）都有 $E_\theta[\varphi(\mathbf{X})] \leq \alpha$，那么它也是原复合假设 $H_0: \theta \in \Theta_0 \ \text{vs.} \ H_1: \theta \in \Theta_1$ 的UMP检验。

**例子**：设 $X \sim f(x;\theta) = \theta x^{\theta-1}, 0<x<1, \theta>1$。对于 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$，利用N-P引理得到的MP检验拒绝域为 $x > (1-\alpha)^{1/\theta_0}$，该形式不依赖于 $\theta_1$，因此它是 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$ 的UMP检验。

### 5.4.4 指数族分布中的UMP检验 (UMP Test in Exponential Family)
对于具有单调似然比的一维参数指数族，存在标准的UMP检验形式。

**定理 2**：设 $X_1, \cdots, X_n$ 来自一维参数指数族：$f(x,\theta) = C(\theta)e^{Q(\theta)T(x)}h(x)$，其中 $Q(\theta)$ 是 $\theta$ 的严格单调函数。令 $V = \sum_{i=1}^n T(X_i)$。
1. 对于检验问题 $H_0: \theta \leq \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$，UMP水平 $\alpha$ 检验为：
   $$
   \varphi(\boldsymbol{x}) = 
   \begin{cases}
   1, & V(\boldsymbol{x}) > C, \\
   r, & V(\boldsymbol{x}) = C, \\
   0, & V(\boldsymbol{x}) < C.
   \end{cases}
   $$
   其中 $C$ 和 $r$ 由 $E_{\theta_0}[\varphi(\mathbf{X})] = \alpha$ 决定。
2. 对于检验问题 $H_0: \theta \geq \theta_0 \ \text{vs.} \ H_1: \theta < \theta_0$，UMP检验拒绝域形式为 $V(\boldsymbol{x}) < C$。

**应用实例**：
- **二项分布** $B(1, \theta)$：$T(x)=x$，$V=\sum X_i \sim B(n, \theta)$。检验 $H_0: \theta \leq \theta_0$ 的UMP检验基于 $V$，拒绝域为 $V > C$（或带随机化）。
- **正态分布（方差已知）** $N(\theta, \sigma^2)$：$T(x)=x$，$V=\sum X_i$，$Q(\theta)=\theta/\sigma^2$ 单调增。检验 $H_0: \theta \leq \theta_0$ 的UMP检验等价于我们熟知的 $Z$ 检验，拒绝域为 $\sqrt{n}(\bar{X}-\theta_0)/\sigma > z_\alpha$。

**双边检验与无偏检验 (Two-Sided Test and Unbiased Test)**：
对于双边检验问题 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \neq \theta_0$，通常不存在UMP检验。此时，可以寻找 **一致最大功效无偏 (UMPU) 检验**。无偏检验要求其功效函数在备择假设上处处不低于水平 $\alpha$，即 $\pi(\theta) \geq \alpha, \forall \theta \in \Theta_1$。对于指数族，存在构造UMPU检验的方法。

## 5.5 假设检验与置信区间 (Hypothesis Testing and Confidence Interval)

### 5.5.1 对偶关系 (Duality)
假设检验与置信区间（或置信域）之间存在紧密的对偶关系，二者可以相互构造。

### 5.5.2 由假设检验构造置信区间 (Constructing Confidence Interval from Hypothesis Test)
**基本思想**：对于一个未知参数 $\theta$，其 $1-\alpha$ 置信区间由所有那些在水平 $\alpha$ 下不会被样本数据拒绝的假设值 $\theta_0$ 构成。

**定理**：设 $X$ 是来自总体 $\{f(x; \theta), \theta \in \Theta\}$ 的样本。对于每个可能的 $\theta \in \Theta$，考虑检验问题 $H_{0,\theta}: \theta^* = \theta \ \text{vs.} \ H_{1,\theta}: \theta^* \neq \theta$，并设 $A(\theta)$ 为该检验在水平 $\alpha$ 下的 **接受域**。定义样本观测值 $x$ 对应的集合：
$$
T(x) = \{\theta \in \Theta: x \in A(\theta)\}.
$$
则 $T(X)$ 是 $\theta$ 的一个置信水平为 $1-\alpha$ 的 **置信域**。
**证明**：$P_\theta(\theta \in T(X)) = P_\theta(X \in A(\theta)) = 1-\alpha$。

**操作方法（以构造双侧置信区间为例）**：
1. 写出检验 $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \neq \theta_0$ 的接受域 $D^c(\theta_0)$。
2. 接受域通常可表示为关于样本统计量和 $\theta_0$ 的不等式，例如 $a(X) \leq \theta_0 \leq b(X)$。
3. 将此不等式中的 $\theta_0$ 替换为 $\theta$，即得到 $\theta$ 的置信区间 $[a(X), b(X)]$。

**单侧置信限**：
- 检验 $H_0: \theta \geq \theta_0 \ \text{vs.} \ H_1: \theta < \theta_0$ 的接受域可导出 $\theta$ 的 **下置信限** $\hat{\theta}_L(X)$，满足 $P(\theta \geq \hat{\theta}_L(X)) = 1-\alpha$。
- 检验 $H_0: \theta \leq \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$ 的接受域可导出 $\theta$ 的 **上置信限** $\hat{\theta}_U(X)$，满足 $P(\theta \leq \hat{\theta}_U(X)) = 1-\alpha$。

### 5.5.3 由置信区间进行假设检验 (Hypothesis Testing Based on Confidence Interval)
反之，给定一个置信水平为 $1-\alpha$ 的置信区间（或置信限），可以立即对参数进行相应的假设检验。

**操作方法**：
1. **双侧检验** $H_0: \theta = \theta_0 \ \text{vs.} \ H_1: \theta \neq \theta_0$：
   - 若 $\theta_0$ 落在 $1-\alpha$ 置信区间之外，则在水平 $\alpha$ 下拒绝 $H_0$。
   - 因为 $P_{\theta_0}(\text{reject } H_0) = P_{\theta_0}(\theta_0 \notin CI) = \alpha$。
2. **左侧单边检验** $H_0: \theta \geq \theta_0 \ \text{vs.} \ H_1: \theta < \theta_0$：
   - 若 $\theta_0$ 大于 $1-\alpha$ **上置信限** $\hat{\theta}_U$，则拒绝 $H_0$。
3. **右侧单边检验** $H_0: \theta \leq \theta_0 \ \text{vs.} \ H_1: \theta > \theta_0$：
   - 若 $\theta_0$ 小于 $1-\alpha$ **下置信限** $\hat{\theta}_L$，则拒绝 $H_0$。

### 课程小结 (Course Summary)

**核心知识点**：
1. **参数假设检验框架**：明确了原假设 $H_0$ 与备择假设 $H_1$、检验统计量、拒绝域、显著性水平 $\alpha$、两类错误、功效函数等基本概念。
2. **经典正态总体检验**：系统掌握了单正态和两正态总体下，关于均值、方差（已知/未知）的各种 $Z$ 检验、$t$ 检验、$\chi^2$ 检验和 $F$ 检验，包括其适用条件、统计量形式和拒绝域。
3. **似然比检验 (LRT)**：理解了基于似然比原理构造检验的通用方法。LRT通过比较参数空间在 $H_0$ 约束下和全空间下的最大似然值来判断。在大样本下，$-2\log\lambda$ 服从卡方分布，适用于复杂假设。在线性回归和方差分析中，LRT导出了精确的 $t$ 检验和 $F$ 检验。
4. **一致最大功效检验 (UMP)**：掌握了在固定水平 $\alpha$ 下寻找“最优”检验的最优性准则。Neyman-Pearson基本引理是构造MP/UMP检验的理论基础。对于单边检验和具有单调似然比的指数族分布，可以构造出UMP检验。认识到UMP检验的局限性，特别是在双边检验中通常不存在。
5. **假设检验与置信区间的对偶性**：深刻理解并会应用二者之间的等价关系。可以从假设检验的接受域导出置信区间，也可以利用置信区间直接进行假设检验。这一关系统一了区间估计和假设检验两大推断形式。

**应用技巧**：
- 面对实际问题，首先根据研究目的正确设立原假设和备择假设（特别是单边与双边的选择）。
- 根据总体分布、样本量、待检参数等信息，选择合适的检验统计量和方法（如精确分布、大样本近似、参数/非参数方法）。
- 善用 $p$ 值进行决策和解释，理解其“拒绝原假设的最小显著性水平”的含义。
- 理解统计显著性与实际显著性的区别。
- 在回归分析中，熟练运用 $t$ 检验判断单个变量的显著性，运用 $F$ 检验判断模型整体或子集的显著性。

**关键公式总结**：
- 单样本 $t$ 检验：$T = \frac{\sqrt{n}(\bar{X}-\mu_0)}{S} \sim t_{n-1}$
- 两独立样本（方差齐）$t$ 检验：$T = \frac{(\bar{X}-\bar{Y})-\delta_0}{S_p\sqrt{1/m+1/n}} \sim t_{m+n-2}$
- 方差比检验：$F = S_X^2/S_Y^2 \sim F_{m-1,n-1}$ （在 $H_0: \sigma_1^2=\sigma_2^2$ 下）
- 似然比统计量：$\lambda = \frac{\sup_{\theta \in \Theta_0} L(\theta)}{\sup_{\theta \in \Theta} L(\theta)}$
- N-P引理检验形式：拒绝当 $f(x;\theta_1) > C f(x;\theta_0)$
- 置信区间与检验的关系：$1-\alpha$ 置信区间包含所有在水平 $\alpha$ 下不被拒绝的 $\theta_0$ 值。
