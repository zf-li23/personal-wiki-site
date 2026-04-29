## 4.1 基本概念 (Basic Concepts)

### 4.1.1 区间估计与置信区间 (Interval Estimation and Confidence Interval)
- **区间估计 (Interval Estimation)**：用样本构造的随机区间 $[\hat{g}_1(\mathbf{X}), \hat{g}_2(\mathbf{X})]$ 来估计参数 $g(\theta)$，并考察该区间包含真实参数的概率。
- **置信区间 (Confidence Interval, CI)**：对于给定的 $0 < \alpha < 1$，若统计量 $\hat{\theta}_1(\mathbf{X}), \hat{\theta}_2(\mathbf{X})$ 满足：
  $$
  P_\theta\left( \hat{\theta}_1(\mathbf{X}) \leq \theta \leq \hat{\theta}_2(\mathbf{X}) \right) \geq 1 - \alpha, \quad \forall \theta \in \Theta
  $$
  则称 $[\hat{\theta}_1(\mathbf{X}), \hat{\theta}_2(\mathbf{X})]$ 为 $\theta$ 的 **置信水平 (confidence level)** $1 - \alpha$ 的置信区间。
- **置信系数 (Confidence Coefficient)**：置信水平的下确界：
  $$
  \inf_{\theta \in \Theta} P_\theta\left( \hat{\theta}_1(\mathbf{X}) \leq \theta \leq \hat{\theta}_2(\mathbf{X}) \right)
  $$
- **精度 (Precision)**：常用置信区间的平均长度衡量：$E_\theta(\hat{\theta}_2 - \hat{\theta}_1)$。

### 4.1.2 置信限 (Confidence Limits)
- **上置信限 (Upper Confidence Limit)** $\hat{\theta}_U(\mathbf{X})$：满足 $P_\theta(\theta \leq \hat{\theta}_U) \geq 1 - \alpha$。
- **下置信限 (Lower Confidence Limit)** $\hat{\theta}_L(\mathbf{X})$：满足 $P_\theta(\hat{\theta}_L \leq \theta) \geq 1 - \alpha$。
- 若 $\hat{\theta}_L, \hat{\theta}_U$ 分别为置信水平 $1-\alpha_1$ 和 $1-\alpha_2$ 的置信限，则 $[\hat{\theta}_L, \hat{\theta}_U]$ 是置信水平 $1-(\alpha_1 + \alpha_2)$ 的置信区间。

### 4.1.3 置信区域 (Confidence Region)
- 对于多维参数 $\boldsymbol{\theta} = (\theta_1, \dots, \theta_k)$，定义随机区域 $S(\mathbf{X}) \subseteq \Theta$，若满足：
  $$
  P_\theta(\boldsymbol{\theta} \in S(\mathbf{X})) \geq 1 - \alpha, \quad \forall \boldsymbol{\theta} \in \Theta
  $$
  则 $S(\mathbf{X})$ 称为 $\boldsymbol{\theta}$ 的置信水平 $1 - \alpha$ 的置信区域。

### 4.1.4 可靠性与精度的权衡 (Trade-off between Reliability and Precision)
- **可靠性 (Reliability)**：置信水平 $1 - \alpha$。
- **精度 (Precision)**：置信区间的平均长度。
- 二者通常不能同时优化，需要在给定置信水平下寻求最短的置信区间（**Neyman 原则**）。

---

## 4.2 枢轴变量法 (Pivot Variable Method)

### 4.2.1 枢轴变量的定义与构造步骤
- **枢轴变量 (Pivot Variable)**：一个关于样本和参数的函数 $T(\mathbf{X}; \theta)$，满足：
  1. 表达式依赖于未知参数 $\theta$；
  2. 其分布完全已知，且与 $\theta$ 无关。
- **构造步骤**：
  1. 寻找包含 $\theta$ 和样本的统计量，其分布已知；
  2. 确定常数 $a < b$ 使得 $P_\theta(a \leq T \leq b) = 1 - \alpha$；
  3. 将不等式 $a \leq T \leq b$ 改写为 $\hat{\theta}_1(\mathbf{X}) \leq \theta \leq \hat{\theta}_2(\mathbf{X})$；
  4. 得到置信区间 $[\hat{\theta}_1, \hat{\theta}_2]$。

### 4.2.2 单正态总体均值的置信区间
- **方差已知**：$\sigma^2$ 已知，$\mu$ 未知。
  枢轴变量：
  $$
  Z = \frac{\sqrt{n}(\bar{X} - \mu)}{\sigma} \sim N(0,1)
  $$
  置信区间：
  $$
  \left[ \bar{X} - \frac{\sigma}{\sqrt{n}} z_{\alpha/2},\; \bar{X} + \frac{\sigma}{\sqrt{n}} z_{\alpha/2} \right]
  $$

- **方差未知**：$\sigma^2$ 未知，$\mu$ 未知。
  枢轴变量：
  $$
  T = \frac{\sqrt{n}(\bar{X} - \mu)}{S} \sim t_{n-1}
  $$
  置信区间：
  $$
  \left[ \bar{X} - \frac{S}{\sqrt{n}} t_{n-1,\alpha/2},\; \bar{X} + \frac{S}{\sqrt{n}} t_{n-1,\alpha/2} \right]
  $$

### 4.2.3 单正态总体方差的置信区间
- **均值已知**：$\mu$ 已知，$\sigma^2$ 未知。
  令 $S_\mu^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \mu)^2$，
  枢轴变量：
  $$
  \frac{n S_\mu^2}{\sigma^2} \sim \chi_n^2
  $$
  置信区间：
  $$
  \left[ \frac{n S_\mu^2}{\chi_{n;\alpha/2}^2},\; \frac{n S_\mu^2}{\chi_{n;1-\alpha/2}^2} \right]
  $$

- **均值未知**：$\mu$ 未知，$\sigma^2$ 未知。
  枢轴变量：
  $$
  \frac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2
  $$
  置信区间：
  $$
  \left[ \frac{(n-1)S^2}{\chi_{n-1;\alpha/2}^2},\; \frac{(n-1)S^2}{\chi_{n-1;1-\alpha/2}^2} \right]
  $$

### 4.2.4 两正态总体均值差的置信区间（方差相等）
- 假设 $X_1,\dots,X_m \stackrel{\text{i.i.d.}}{\sim} N(\mu_1,\sigma^2)$，$Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} N(\mu_2,\sigma^2)$，且相互独立。
- 定义合并样本方差：
  $$
  S_w^2 = \frac{(m-1)S_X^2 + (n-1)S_Y^2}{m+n-2}
  $$
- 枢轴变量：
  $$
  T = \frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{S_w \sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t_{m+n-2}
  $$
- 置信区间：
  $$
  (\bar{X} - \bar{Y}) \pm t_{m+n-2,\alpha/2} \cdot S_w \sqrt{\frac{1}{m} + \frac{1}{n}}
  $$

### 4.2.5 两正态总体方差比的置信区间
- 假设 $X_1,\dots,X_m \stackrel{\text{i.i.d.}}{\sim} N(\mu_1,\sigma_1^2)$，$Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} N(\mu_2,\sigma_2^2)$，且相互独立。
- 枢轴变量：
  $$
  F = \frac{S_X^2 / \sigma_1^2}{S_Y^2 / \sigma_2^2} \sim F_{m-1,n-1}
  $$
- 置信区间：
  $$
  \left[ \frac{S_X^2}{S_Y^2} F_{n-1,m-1;1-\alpha/2},\; \frac{S_X^2}{S_Y^2} F_{n-1,m-1;\alpha/2} \right]
  $$

### 4.2.6 均匀分布参数的置信区间
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} U(0,\theta)$。
- 充分统计量：$X_{(n)} = \max\{X_1,\dots,X_n\}$。
- 令 $Y = X_{(n)} / \theta$，其密度为 $f_Y(y) = n y^{n-1},\; 0 \leq y \leq 1$。
- 选择 $a,b$ 使得 $b^n - a^n = 1 - \alpha$，则置信区间为：
  $$
  \left[ \frac{X_{(n)}}{b},\; \frac{X_{(n)}}{a} \right]
  $$
- 最短区间取 $b=1,\; a=\alpha^{1/n}$，即 $[X_{(n)},\; X_{(n)}/\alpha^{1/n}]$。

### 4.2.7 指数分布参数的置信区间
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\lambda)$。
- 枢轴变量：
  $$
  2\lambda n\bar{X} = 2\lambda \sum_{i=1}^n X_i \sim \chi_{2n}^2
  $$
- 置信区间：
  $$
  \left[ \frac{\chi_{2n;1-\alpha/2}^2}{2n\bar{X}},\; \frac{\chi_{2n;\alpha/2}^2}{2n\bar{X}} \right]
  $$

---

## 4.3 近似置信区间 (Approximate Confidence Intervals)

### 4.3.1 适用场景与基本思想
- **适用场景**：精确分布复杂或未知，但样本量 $n$ 较大。
- **基本思想**：利用中心极限定理 (CLT) 和 Slutsky 定理，构造渐近分布不依赖于参数的统计量，从而得到近似置信区间。
- **渐近有效置信区间 (Asymptotically Valid CI)**：满足
  $$
  \lim_{n\to\infty} P_\theta\left( \hat{\theta}_1(\mathbf{X}_n) \leq \theta \leq \hat{\theta}_2(\mathbf{X}_n) \right) \geq 1 - \alpha
  $$

### 4.3.2 伯努利分布参数的近似置信区间
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} B(1,\theta)$。
- 由 CLT：
  $$
  \frac{\sqrt{n}(\bar{X}_n - \theta)}{\sqrt{\theta(1-\theta)}} \stackrel{d}{\to} N(0,1)
  $$
- 用 $\bar{X}_n(1-\bar{X}_n)$ 代替 $\theta(1-\theta)$（由 WLLN），得近似枢轴变量：
  $$
  \frac{\sqrt{n}(\bar{X}_n - \theta)}{\sqrt{\bar{X}_n(1-\bar{X}_n)}} \stackrel{d}{\to} N(0,1)
  $$
- 近似置信区间：
  $$
  \bar{X}_n \pm z_{\alpha/2} \sqrt{\frac{\bar{X}_n(1-\bar{X}_n)}{n}}
  $$

### 4.3.3 泊松分布参数的近似置信区间
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} P(\theta)$。
- 近似枢轴变量：
  $$
  \frac{\sqrt{n}(\bar{X}_n - \theta)}{\sqrt{\bar{X}_n}} \stackrel{d}{\to} N(0,1)
  $$
- 近似置信区间：
  $$
  \bar{X}_n \pm z_{\alpha/2} \sqrt{\frac{\bar{X}_n}{n}}
  $$

### 4.3.4 指数分布参数的近似置信区间
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\theta)$，其中 $E X_1 = \theta$。
- 近似枢轴变量：
  $$
  \frac{\sqrt{n}(\bar{X}_n - \theta)}{\bar{X}_n} \stackrel{d}{\to} N(0,1)
  $$
- 近似置信区间：
  $$
  \bar{X}_n \pm z_{\alpha/2} \frac{\bar{X}_n}{\sqrt{n}}
  $$

### 4.3.5 两总体均值差的近似置信区间（方差不等）
- **Behrens-Fisher 问题**：$\sigma_1^2 \neq \sigma_2^2$ 且未知，$m,n$ 不一定大。
- 当 $m,n$ 较大时，由 CLT：
  $$
  \frac{(\bar{X} - \bar{Y}) - (\mu_1 - \mu_2)}{\sqrt{S_X^2/m + S_Y^2/n}} \stackrel{d}{\to} N(0,1)
  $$
- 近似置信区间：
  $$
  (\bar{X} - \bar{Y}) \pm z_{\alpha/2} \sqrt{\frac{S_X^2}{m} + \frac{S_Y^2}{n}}
  $$
- **Welch 近似**：当 $m,n$ 不太大时，可用 $t$ 分布近似，自由度 $r$ 为：
  $$
  r = \frac{\left( \frac{S_X^2}{m} + \frac{S_Y^2}{n} \right)^2}{\frac{S_X^4}{m^2(m-1)} + \frac{S_Y^4}{n^2(n-1)}}
  $$
  取最接近的整数。置信区间为：
  $$
  (\bar{X} - \bar{Y}) \pm t_{r,\alpha/2} \sqrt{\frac{S_X^2}{m} + \frac{S_Y^2}{n}}
  $$

---

## 4.4 置信区域 (Confidence Regions)

### 4.4.1 正态分布均值和方差的联合置信区域
- $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} N(\mu,\sigma^2)$。
- 选取 $c$ 使得 $P(-c \leq Z \leq c) = \sqrt{1-\alpha},\; Z \sim N(0,1)$。
- 选取 $a,b$ 使得 $P(a \leq X \leq b) = \sqrt{1-\alpha},\; X \sim \chi_{n-1}^2$。
- 联合置信区域由以下不等式定义：
  $$
  (\mu - \bar{X})^2 \leq \frac{c^2}{n} \sigma^2, \quad \frac{(n-1)S^2}{b} \leq \sigma^2 \leq \frac{(n-1)S^2}{a}
  $$
  在 $(\mu,\sigma^2)$ 平面上为一抛物线围成的区域。

### 4.4.2 多个均值参数的联合置信区域
- **问题**：构造 $k$ 个均值参数 $\mu_1,\dots,\mu_k$ 的联合置信区域。
- **Bonferroni 校正法**：对每个 $\mu_i$ 分别构造置信水平 $1 - \alpha/k$ 的置信区间，这些区间的笛卡尔积构成联合置信区域。
  - 对于正态样本，$\mu_i$ 的置信区间为：
    $$
    \bar{X}_i \pm t_{n_i-1,\alpha/(2k)} \frac{S_i}{\sqrt{n_i}}
    $$
- **Šidák 校正法**：若各样本独立，可构造置信水平 $\sqrt[k]{1-\alpha}$ 的边际置信区间，再取笛卡尔积。
  - 对于正态独立样本，$\mu_i$ 的置信区间为：
    $$
    \bar{X}_i \pm t_{n_i-1,\gamma} \frac{S_i}{\sqrt{n_i}}, \quad \gamma = \frac{1 - \sqrt[k]{1-\alpha}}{2}
    $$
- **适用性**：Bonferroni 法更保守，适用于独立或相关的情形；Šidák 法要求独立性。

---

## 小结 (Summary)

- **置信区间** 是区间估计的核心概念，提供了参数估计的不确定性度量。
- **枢轴变量法** 是构造精确置信区间的主要方法，关键在于找到分布已知且与参数无关的统计量。
- **常用精确置信区间**：
  - 单正态总体均值（方差已知/未知）、方差（均值已知/未知）。
  - 两正态总体均值差（方差相等）、方差比。
  - 均匀分布、指数分布参数的置信区间。
- **近似置信区间** 依赖于大样本理论（CLT），适用于精确分布复杂或未知的情形，如伯努利、泊松、指数分布以及 Behrens-Fisher 问题。
- **置信区域** 用于多维参数的联合推断，常用 Bonferroni 或 Šidák 校正法构造矩形区域。
- **核心权衡**：在给定置信水平下，寻求最短的置信区间（或最小区域），平衡可靠性与精度。

### 关键公式
- 单正态均值（方差未知）：
  $$
  \bar{X} \pm t_{n-1,\alpha/2} \frac{S}{\sqrt{n}}
  $$
- 单正态方差（均值未知）：
  $$
  \left[ \frac{(n-1)S^2}{\chi_{n-1;\alpha/2}^2},\; \frac{(n-1)S^2}{\chi_{n-1;1-\alpha/2}^2} \right]
  $$
- 两正态均值差（方差相等）：
  $$
  (\bar{X} - \bar{Y}) \pm t_{m+n-2,\alpha/2} \cdot S_w \sqrt{\frac{1}{m} + \frac{1}{n}}
  $$
- 伯努利参数近似区间：
  $$
  \hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
  $$
