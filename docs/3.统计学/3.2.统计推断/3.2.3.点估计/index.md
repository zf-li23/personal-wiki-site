## 3.1 估计量的最优准则 (Optimal Criterion of Estimation)

### 3.1.1 无偏性 (Unbiasedness)
- 定义：若 $E_\theta[\hat{g}(X)] = g(\theta)$，则 $\hat{g}(X)$ 是 $g(\theta)$ 的无偏估计。
- 渐近无偏性：$\lim_{n \to \infty} E_\theta[\hat{g}_n(X)] = g(\theta)$。
- 样本均值 $\bar{X}$ 和样本方差 $S^2$ 分别是 $\mu$ 和 $\sigma^2$ 的无偏估计。

### 3.1.2 有效性 (Efficiency)
- 定义：若两个无偏估计 $\hat{g}_1$ 和 $\hat{g}_2$ 满足 $Var(\hat{g}_1) \leq Var(\hat{g}_2)$，且至少在某一点严格成立，则 $\hat{g}_1$ 更有效。
- 样本均值比单个观测更有效。

### 3.1.3 均方误差 (Mean Squared Error, MSE)
- 定义：$MSE(\hat{\theta}) = E_\theta(\hat{\theta} - \theta)^2$。
- 分解：$MSE = Var(\hat{\theta}) + [Bias(\hat{\theta})]^2$。
- 无偏估计的 MSE 等于方差。
- 偏差-方差权衡：有时允许轻微偏差以大幅降低方差。

### 3.1.4 相合性 (Consistency)
- 弱相合：$\hat{g}_n \xrightarrow{P} g(\theta)$。
- 强相合：$\hat{g}_n \xrightarrow{a.s.} g(\theta)$。
- $r$ 阶矩相合：$\lim_{n \to \infty} E|\hat{g}_n - g(\theta)|^r = 0$。
- 样本矩是强相合的。

### 3.1.5 渐近正态性 (Asymptotic Normality)
- 在一定正则条件下，估计量服从渐近正态分布。

---

## 3.2 矩估计法 (Method of Moments)

### 3.2.1 定义

设总体分布来自参数族 \(\mathcal{F} = \{f(x; \theta) : \theta \in \Theta\}\)，其中 \(\theta\) 可为向量。假设待估参数 \(g(\theta)\) 可以表示为若干个总体矩的函数：

$$
g(\theta) = G(\alpha_1, \dots, \alpha_k; \mu_2, \dots, \mu_s),
$$

其中：
- **总体原点矩**：\(\alpha_k = E_{\theta}(X^k)\)，
- **总体中心矩**：\(\mu_k = E_{\theta}[(X - \alpha_1)^k]\)。

设 \(\boldsymbol{X} = (X_1, \dots, X_n)\) 是来自该总体的简单随机样本，定义相应的**样本矩**：
- **样本原点矩**：\(a_{n,k} = \frac{1}{n} \sum_{i=1}^{n} X_i^k\),
- **样本中心矩**：\(m_{n,k} = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar{X})^k\)，其中 \(\bar{X} = a_{n,1}\)。

**定义 9 (矩估计).** 将总体矩 \(\alpha_k, \mu_k\) 替换为对应的样本矩 \(a_{n,k}, m_{n,k}\)，得到：
$$
\hat{g}(\boldsymbol{X}) = G(a_{n1}, \dots, a_{nk}; m_{n2}, \dots, m_{ns}),
$$
称 \(\hat{g}(\boldsymbol{X})\) 为 \(g(\theta)\) 的**矩估计**。

---

### 3.2.2 矩估计的性质

#### 1. 无偏性 (Unbiasedness)
- **样本原点矩**是总体原点矩的**无偏估计**：
  $$
  E[a_{n,k}] = \alpha_k.
  $$
- **样本中心矩**通常**不是无偏估计**：
  $$
  E[m_{n,k}] \neq \mu_k \quad (k \ge 2).
  $$
  例如，对于方差，有：
  $$
  E[m_{n,2}] = \frac{n-1}{n} \mu_2 \neq \mu_2.
  $$
  使用调整样本方差 \(S_n^2 = \frac{n}{n-1} m_{n,2}\) 可得到无偏估计。
- 一般地，矩估计 \(\hat{g}(\boldsymbol{X})\) 是**有偏**的，但常为**渐近无偏**。

#### 2. 相合性 (Consistency)
- 由**强大数定律 (SLLN)**，样本矩是总体矩的**强相合估计**：
  $$
  a_{n,k} \xrightarrow{a.s.} \alpha_k, \quad m_{n,k} \xrightarrow{a.s.} \mu_k \quad (n \to \infty).
  $$
- 若 \(G\) 是连续函数，则由连续映射定理，矩估计也是**强相合**的：
  $$
  \hat{g}(\boldsymbol{X}) \xrightarrow{a.s.} g(\theta).
  $$

#### 3. 渐近正态性 (Asymptotic Normality)
- 在一定正则条件下（如总体矩存在且有限），矩估计是**相合渐近正态估计**。
- 具体地，对多元矩估计向量 \(\hat{\boldsymbol{g}}\)，当 \(n \to \infty\) 时：
  $$
  \sqrt{n}\big(\hat{\boldsymbol{g}} - \boldsymbol{g}(\theta)\big) \xrightarrow{d} N(\boldsymbol{0}, \boldsymbol{\Sigma}),
  $$
  其中 \(\boldsymbol{\Sigma}\) 为渐近协方差矩阵，可通过 Delta 方法或中心极限定理求得。
- **常见例子**：
  - 样本均值 \(\bar{X}\)：\(\sqrt{n}(\bar{X} - \mu) \xrightarrow{d} N(0, \sigma^2)\)。
  - 调整样本方差 \(S_n^2\)：\(\sqrt{n}(S_n^2 - \sigma^2) \xrightarrow{d} N(0, \mu_4 - \sigma^4)\)。

---

### 3.2.3 矩估计的优缺点
- **优点**：
  - 方法简单直观，计算方便。
  - 无需知道总体分布的具体形式，只需矩存在即可。
  - 具有良好的大样本性质（相合性、渐近正态性）。
- **缺点**：
  - 小样本时可能有偏。
  - 有时不唯一（如矩的选取方式不同）。
  - 可能效率不如其他估计方法（如极大似然估计）。

---

### 3.2.4 矩估计的一般步骤
1. 将待估参数 \(g(\theta)\) 表示为总体矩的函数。
2. 根据样本计算对应的样本矩。
3. 用样本矩替换总体矩，得到矩估计。
4. 根据需要进行大样本推断（如渐近方差估计、置信区间构造）。

---

## 3.3 极大似然估计 (Maximum Likelihood Estimation, MLE)

### 3.3.1 基本概念

设总体分布族为 \(\mathcal{F} = \{f(x; \theta) : \theta \in \Theta\}\)，其中 \(\Theta\) 为参数空间。设 \(\boldsymbol{X} = (X_1, \dots, X_n)\) 是从该分布抽取的简单随机样本，观测值为 \(\boldsymbol{x} = (x_1, \dots, x_n)\)。

**定义 5 (似然函数与对数似然函数).**
- **似然函数**定义为样本的联合密度（或概率）函数：
  $$
  L(\theta; \boldsymbol{x}) = \prod_{i=1}^{n} f(x_i; \theta), \quad \theta \in \Theta.
  $$
- **对数似然函数**为：
  $$
  l(\theta; \boldsymbol{x}) = \log L(\theta; \boldsymbol{x}) = \sum_{i=1}^{n} \log f(x_i; \theta).
  $$

**定义 5 (极大似然估计).**
如果估计量 \(\hat{\theta} = \hat{\theta}(\boldsymbol{X})\) 满足：
$$
L(\hat{\theta}(\boldsymbol{x}); \boldsymbol{x}) = \sup_{\theta \in \Theta} L(\theta; \boldsymbol{x}), \quad \forall \boldsymbol{x} \in \mathcal{X},
$$
或等价地，
$$
l(\hat{\theta}(\boldsymbol{x}); \boldsymbol{x}) = \sup_{\theta \in \Theta} l(\theta; \boldsymbol{x}), \quad \forall \boldsymbol{x} \in \mathcal{X},
$$
则称 \(\hat{\theta}(\boldsymbol{X})\) 为 \(\theta\) 的**极大似然估计量**，\(\hat{\theta}(\boldsymbol{x})\) 称为 \(\theta\) 的**极大似然估计值**。

---

### 3.3.2 求解方法

#### 1. 似然方程法
在参数空间内部，若似然函数对 \(\theta\) 可微，则极大似然估计通常满足**似然方程**（对数似然方程）：
$$
\frac{\partial l(\theta; \boldsymbol{x})}{\partial \theta_i} = 0, \quad i = 1, \dots, k \quad (\text{若 } \theta \text{ 为向量})。
$$

#### 2. 验证极值条件
- 对于单参数情形，需检查二阶导数 \(l''(\theta; \boldsymbol{x}) < 0\)。
- 对于多参数情形，需验证 Hessian 矩阵 \(\boldsymbol{H} = \left[ \frac{\partial^2 l}{\partial \theta_i \partial \theta_j} \right]\) 在 \(\hat{\theta}\) 处负定。

#### 3. 数值方法
当似然方程无解析解时，可使用迭代数值方法（如 Newton-Raphson、EM 算法等）求解。

---

### 3.3.3 重要性质

#### 1. 不变性原理 (Invariance Principle)
若 \(\hat{\theta}\) 是 \(\theta\) 的 MLE，则对任意函数 \(g(\theta)\)（不必为一一映射），\(g(\hat{\theta})\) 是 \(g(\theta)\) 的 MLE。

#### 2. 与充分统计量的关系
**定理 4.** 设 \(T = T(\boldsymbol{X})\) 是 \(\theta\) 的充分统计量。若 MLE 存在，则它一定是 \(T\) 的函数。

*证明.* 由因子分解定理：
$$
L(\theta; \boldsymbol{x}) = g(T(\boldsymbol{x}), \theta) \cdot h(\boldsymbol{x}).
$$
最大化 \(L(\theta; \boldsymbol{x})\) 等价于最大化 \(g(T(\boldsymbol{x}), \theta)\)，因此 MLE 只通过 \(T(\boldsymbol{x})\) 依赖于样本。

#### 3. 大样本性质

**相合性 (Consistency)**  
**定理 5.** 在一定正则条件下，MLE 序列 \(\hat{\theta}_n\) 是**相合估计**：
$$
\hat{\theta}_n \xrightarrow{P_\theta} \theta, \quad n \to \infty.
$$

**渐近正态性 (Asymptotic Normality)**  
**定理 6.** 在正则条件下，MLE 是**渐近正态**的：
$$
\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, \sigma_\theta^2), \quad \text{其中 } \sigma_\theta^2 = \frac{1}{I(\theta)}.
$$
这里 \(I(\theta)\) 是 **Fisher 信息量**（每个观测）：
$$
I(\theta) = E_\theta\left[ \left( \frac{\partial}{\partial \theta} \log f(X; \theta) \right)^2 \right].
$$

**渐近有效性 (Asymptotic Efficiency)**  
在上述正则条件下，MLE 是**渐近有效**的，即达到 Cramér-Rao 下界。

---

### 3.3.4 指数族中的 MLE

对于指数族分布，其密度为：
$$
f(x; \boldsymbol{\theta}) = C(\boldsymbol{\theta}) \exp\left\{ \sum_{i=1}^{k} \theta_i T_i(x) \right\} h(x), \quad \boldsymbol{\theta} \in \Theta^*,
$$
其中 \(\Theta^*\) 是自然参数空间。样本的对数似然函数为：
$$
l(\boldsymbol{\theta}; \boldsymbol{x}) = n \log C(\boldsymbol{\theta}) + \sum_{i=1}^{k} \theta_i \sum_{j=1}^{n} T_i(x_j) + \log h(\boldsymbol{x}).
$$
似然方程为：
$$
\frac{n}{C(\boldsymbol{\theta})} \frac{\partial C(\boldsymbol{\theta})}{\partial \theta_i} = - \sum_{j=1}^{n} T_i(x_j), \quad i = 1, \dots, k.
$$

**定理 2.** 如果对任意样本，上述似然方程在自然参数空间的内点集 \(\Theta_0\) 中有解，则该解**唯一**，并且就是 MLE。

---

### 3.3.5 矩估计与 MLE 的比较

| 性质         | 矩估计 (MME)                     | 极大似然估计 (MLE)               |
|--------------|----------------------------------|----------------------------------|
| 无偏性       | 样本原点矩无偏，中心矩有偏       | 通常有偏，但渐近无偏             |
| 相合性       | 强相合（若矩存在）               | 强相合（在一定条件下）           |
| 渐近正态性   | 是，但效率可能较低               | 是，且渐近有效                   |
| 计算复杂度   | 较简单                           | 可能较复杂，需求解方程           |
| 适用条件     | 只需矩存在                       | 需知道分布形式，且似然函数良好   |
| 不变性       | 一般不具有函数不变性             | 具有不变性原理                   |

---

## 3.4 一致最小方差无偏估计 (Uniformly Minimum Variance Unbiased Estimate, UMVUE)

### 3.4.1 UMVUE 的定义与存在性

- **定义**：若 $U = U(X_1, \cdots, X_n)$ 是 $g(\theta)$ 的无偏估计，且对任意其他无偏估计 $V$，都有
  $$
  \text{Var}_\theta(U) \leq \text{Var}_\theta(V), \quad \forall \theta \in \Theta
  $$
  则称 $U$ 为 $g(\theta)$ 的 UMVUE。

- **存在性**：无偏估计不一定存在。例如，对于 $X \sim B(n, p)$，$g(p) = 1/p$ 不存在无偏估计。

### 3.4.2 构造 UMVUE 的方法

#### 3.4.2.1 零无偏估计法 (Zero Unbiased Estimate Method)

- **定理**：若 $\hat{g}(X)$ 是 $g(\theta)$ 的无偏估计，且对任意满足 $E_\theta l(X) = 0$ 的统计量 $l(X)$，都有
  $$
  \text{Cov}_\theta(\hat{g}(X), l(X)) = 0, \quad \forall \theta \in \Theta
  $$
  则 $\hat{g}(X)$ 是 UMVUE。

- **推论**：若 $T$ 是充分统计量，$h(T)$ 是 $g(\theta)$ 的无偏估计，且对任意零无偏估计 $\delta(T)$，有 $\text{Cov}_\theta(h(T), \delta(T)) = 0$，则 $h(T)$ 是 UMVUE。

#### 3.4.2.2 充分完全统计量法 (Lehmann-Scheffé Theorem)

- **定理**：设 $T(X)$ 是充分且完全的统计量，若 $\hat{g}(T(X))$ 是 $g(\theta)$ 的无偏估计，则 $\hat{g}(T(X))$ 是唯一的 UMVUE。

- **构造方法**：若 $T$ 充分完全，则对任意无偏估计 $U$，令 $\hat{g}(T) = E_\theta(U \mid T)$，则 $\hat{g}(T)$ 是 UMVUE。

### 3.4.3 例子

#### 3.4.3.1 伯努利分布 $B(1, \theta)$

- $T = \sum X_i$ 充分完全。
- $\bar{X}$ 是 $\theta$ 的 UMVUE。
- $g(\theta) = \theta(1-\theta)$ 的 UMVUE 为 $\frac{T(n-T)}{n(n-1)}$。

#### 3.4.3.2 均匀分布 $U(0, \theta)$

- $T = X_{(n)}$ 充分完全。
- $\hat{\theta} = \frac{n+1}{n}X_{(n)}$ 是 $\theta$ 的 UMVUE。

#### 3.4.3.3 正态分布 $N(\mu, \sigma^2)$

- $T = (\bar{X}, S^2)$ 充分完全。
- $\bar{X}$ 是 $\mu$ 的 UMVUE。
- $S^2$ 是 $\sigma^2$ 的 UMVUE。
- $\sigma^r$ 的 UMVUE 为 $K_{n-1,r} \cdot T_2^{r/2}$，其中 $T_2 = \sum (X_i - \bar{X})^2$。
- $\mu/\sigma^2$ 的 UMVUE 为 $(n-3)\bar{X}/T_2$。

#### 3.4.3.4 泊松分布 $P(\theta)$

- $T = \sum X_i$ 充分完全。
- $\bar{X}$ 是 $\theta$ 的 UMVUE。
- $\theta^r$ 的 UMVUE 为 $\frac{T(T-1)\cdots(T-r+1)}{n^r}$。
- $P_\theta(X_1 = x)$ 的 UMVUE 为 $C_T^x \frac{(n-1)^{T-x}}{n^T}$。

### 3.4.4 C-R正则分布族

- **定义**：分布族 $\mathcal{F} = \{ f(x; \theta), \theta \in \Theta \}$ 称为C-R正则分布族，若满足：
  1. 参数空间 $\Theta$ 是 $\mathbb{R}$ 中的开区间
  2. 分布族有共同支撑集
  3. 对任意 $x \in \mathcal{X}$ 和 $\theta \in \Theta$，$\frac{\partial f(x;\theta)}{\partial \theta}$ 存在
  4. 积分与求导可交换：$\frac{\partial}{\partial \theta} \int f(x; \theta) dx = \int \frac{\partial}{\partial \theta} f(x; \theta) dx$
  5. Fisher信息 $I(\theta) = E_\theta \left[ \frac{\partial \log f(X; \theta)}{\partial \theta} \right]^2$ 满足 $0 < I(\theta) < \infty$

### 3.4.5 Cramer-Rao不等式

- **单参数情形**：对于C-R正则分布族，若 $\hat{g}(\mathbf{X})$ 是 $g(\theta)$ 的无偏估计，则
  $$
  \text{Var}_{\theta} (\hat{g}(\mathbf{X})) \geq \frac{[g'(\theta)]^2}{nI(\theta)}, \quad \theta \in \Theta
  $$
  特别地，当 $g(\theta) = \theta$ 时，
  $$
  \text{Var}_{\theta} (\hat{g}(\mathbf{X})) \geq \frac{1}{nI(\theta)}
  $$

- **多参数情形**：设 $\theta = (\theta_1, \cdots, \theta_k)$，则
  $$
  \text{Cov}_{\theta}(\hat{\theta}) \geq (nI(\theta))^{-1}
  $$
  其中 $I(\theta) = (I_{ij}(\theta))$ 是Fisher信息矩阵，
  $$
  I_{ij}(\theta) = E_{\theta} \left[ \frac{\partial \log f(X; \theta)}{\partial \theta_i} \frac{\partial \log f(X; \theta)}{\partial \theta_j} \right]
  $$

### 3.4.6 Fisher信息

- **定义**：$I(\theta) = E_\theta \left[ \frac{\partial \log f(X; \theta)}{\partial \theta} \right]^2$
- **性质**：
  - 反映总体提供的信息量
  - 随机样本 $(X_1, \cdots, X_n)$ 的总信息量为 $nI(\theta)$
  - 在MLE的渐近正态性中起关键作用

### 3.4.7 有效估计

- **效率**：无偏估计 $\hat{g}(\mathbf{X})$ 的效率定义为
  $$
  e_{\hat{g}}(\theta) = \frac{[g'(\theta)]^2/(nI(\theta))}{\text{Var}_{\theta}(\hat{g}(\mathbf{X}))}
  $$
- **有效估计**：若 $e_{\hat{g}}(\theta) = 1$，则称 $\hat{g}(\mathbf{X})$ 为有效估计
- **渐近有效估计**：若 $\lim_{n \to \infty} e_{\hat{g}}(\theta) = 1$

### 3.4.8 例子

- **伯努利分布** $B(1, \theta)$：$\bar{X}$ 是 $\theta$ 的有效估计
- **泊松分布** $P(\theta)$：$\bar{X}$ 是 $\theta$ 的有效估计  
- **指数分布** $\text{Exp}(\theta)$：$\bar{X}$ 是 $1/\theta$ 的有效估计
- **正态分布** $N(\mu, \sigma^2)$：
  - $\bar{X}$ 是 $\mu$ 的有效估计
  - $S^2$ 不是 $\sigma^2$ 的有效估计，但是渐近有效

---

## 3.5 线性回归中的矩估计与 MLE

### 3.5.1 线性回归模型

- **简单线性回归**：
  $$
  y_i = \beta_0 + \beta_1 x_i + \epsilon_i, \quad i=1,\cdots,n
  $$
- **多元线性回归**：
  $$
  y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_p x_{ip} + \epsilon_i
  $$
- **矩阵形式**：
  $$
  Y = X\beta + \epsilon
  $$
  其中 $Y = (y_1, \cdots, y_n)'$，$X$ 为设计矩阵，$\beta = (\beta_0, \beta_1, \cdots, \beta_p)'$

### 3.5.2 基本假设

- **Gauss-Markov假设**：
  - $E(\epsilon_i) = 0$
  - $\text{Var}(\epsilon_i) = \sigma^2$（同方差）
  - $\epsilon_i$ 相互独立
  - $E(\epsilon_i | x_i) = 0$

- **正态假设**（用于MLE）：
  $$
  \epsilon_i \sim N(0, \sigma^2)
  $$

### 3.5.3 估计方法

#### 3.5.3.1 普通最小二乘法 (OLS)

- **目标**：最小化残差平方和
  $$
  \hat{\beta} = \arg\min_{\beta} \sum_{i=1}^n (y_i - x_i^T \beta)^2
  $$
- **解**：
  $$
  \hat{\beta} = (X^T X)^{-1} X^T Y
  $$
- **方差估计**：
  - 有偏估计：$\hat{\sigma}_n^2 = \frac{1}{n} \sum_{i=1}^n (y_i - x_i^T \hat{\beta})^2$
  - 无偏估计：$\hat{\sigma}^2 = \frac{1}{n-p-1} \sum_{i=1}^n (y_i - x_i^T \hat{\beta})^2$

#### 3.5.3.2 矩估计法

- **基于条件**：$E(\epsilon_i) = 0$，$E(x_i\epsilon_i) = 0$
- **估计方程**：
  $$
  \begin{cases}
  \frac{1}{n}\sum_{i=1}^n(y_i - \beta_0 - \beta_1 x_i) = 0 \\
  \frac{1}{n}\sum_{i=1}^n x_i(y_i - \beta_0 - \beta_1 x_i) = 0
  \end{cases}
  $$
- **结果**：与OLS估计相同

#### 3.5.3.3 极大似然估计 (MLE)

- **似然函数**（在正态假设下）：
  $$
  L(\beta, \sigma^2) = (2\pi\sigma^2)^{-n/2} \exp\left\{-\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - x_i^T \beta)^2\right\}
  $$
- **MLE**：
  $$
  \hat{\beta}_{\text{MLE}} = (X^T X)^{-1} X^T Y, \quad \hat{\sigma}^2_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^n (y_i - x_i^T \hat{\beta})^2
  $$

### 3.5.4 估计量的性质

- **无偏性**：在Gauss-Markov假设下，$\hat{\beta}$ 是 $\beta$ 的无偏估计
- **有效性**：$\hat{\beta}$ 是最佳线性无偏估计(BLUE)
- **正态性**：在正态假设下，
  $$
  \hat{\beta} \sim N(\beta, \sigma^2(X^T X)^{-1})
  $$
- **独立性**：$\hat{\beta}$ 与 $\hat{\sigma}^2$ 相互独立

---

## 3.6 核密度估计 (Kernel Density Estimation)

### 3.6.1 基本概念与动机

- **目标**：基于样本数据估计未知的概率密度函数
- **直方图的局限性**：
  - 依赖于分组数选择，可能过拟合或欠拟合
  - 不连续，不适合连续随机变量
  - 整体误差可能较大
- **核心思想**：用核函数对每个数据点赋予权重，叠加得到平滑的密度估计

### 3.6.2 从自然密度估计到核密度估计

- **理论基础**：对于连续随机变量，密度函数是分布函数的导数
  $$
  f(x) = F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x-h)}{2h}
  $$

- **自然密度估计**：用经验分布函数 $F_n(x)$ 代替 $F(x)$
  $$
  f_n(x) = \frac{F_n(x+h_n) - F_n(x-h_n)}{2h_n}
  $$

- **核密度估计公式**：
  $$
  \hat{f}_n(x) = \frac{1}{nh_n} \sum_{i=1}^n K\left(\frac{x - X_i}{h_n}\right)
  $$
  其中：

  - $K(\cdot)$ 是核函数（非负、对称、积分为1）
  - $h_n > 0$ 是带宽参数，$h_n \to 0$ 当 $n \to \infty$

### 3.6.3 核函数选择

- **常用核函数**：
  - 均匀核：$K(x) = \frac{1}{2}I_{[-1,1]}(x)$
  - 三角核
  - Epanechnikov核：在均方误差意义下最优
  - 四次核
  - 三权重核
  - 高斯核：数学性质方便，常用
- **核函数性质要求**：
  1. $K(x) \geq 0$, $\sup_{x \in R} K(x) \leq M < \infty$, $\lim_{|x| \to \infty} |x|K(x) = 0$
  2. $K(x) = K(-x)$, $\int_{-\infty}^{\infty} K(x)dx = 1$, $\int_{-\infty}^{\infty} x^2K(x)dx < \infty$

### 3.6.4 带宽选择

- **带宽的影响**：

  - $h$ 太小：估计过拟合，噪声多，方差大
  - $h$ 太大：估计过平滑，偏差大，细节丢失

- **偏差-方差权衡**：MSE = Bias² + Variance

- **最优带宽选择准则**：

  - **MISE**（均方积分误差）：
    $$
    MISE(h) = E\left[\int (\hat{f}_n(x) - f(x))^2 dx\right]
    $$

  - **AMISE**（渐近MISE）：
    $$
    AMISE(h) = \frac{R(K)}{nh} + \frac{1}{4}m_2(K)^2h^4R(f'')
    $$
    其中 $R(g) = \int g(x)^2dx$, $m_2(K) = \int x^2K(x)dx$

  - **最优带宽**：
    $$
    h_{AMISE} = \frac{R(K)^{1/5}}{m_2(K)^{2/5}R(f'')^{1/5}n^{1/5}}
    $$

- **实际选择方法**：

  - 插件法
  - 交叉验证法
  - 自适应带宽估计

### 3.6.5 R语言实现

- **函数**：`density(x, bw, kernel, ...)`
- **参数**：
  - `bw`：带宽，可用规则如 "nrd0", "sj" 等
  - `kernel`：核函数，包括 "gaussian", "epanechnikov", "rectangular" 等
  - `adjust`：调整系数，实际带宽为 `adjust * bw`

### 3.6.6 渐近性质

- **渐近无偏**：$\lim_{n \to \infty} E[f_n(x)] = f(x)$
- **均方相合**：$\lim_{n \to \infty} E[f_n(x) - f(x)]^2 = 0$
- **弱相合**：$f_n(x) \xrightarrow{P} f(x)$
- **强相合**：$f_n(x) \xrightarrow{a.s.} f(x)$
- **渐近正态**：$\frac{f_n(x) - E[f_n(x)]}{\sqrt{Var(f_n(x))}} \xrightarrow{d} N(0,1)$

---

## 小结

- **点估计** 是用样本构造的统计量来估计未知参数。
- **评价标准** 包括无偏性、有效性、MSE、相合性、渐近正态性。
- **矩估计法** 简单直观，适用于无模型设定或模型复杂的情况。
- **MLE** 具有优良的大样本性质，是常用的估计方法。
- **UMVUE** 是在所有无偏估计中方差最小的估计量，是最优无偏估计。
  - **构造方法**：
    - **零无偏估计法**：通过验证与所有零无偏估计的协方差为零来判断。
    - **Lehmann-Scheffé 定理**：利用充分完全统计量构造 UMVUE，这是最常用的方法。
  - **关键工具**：
    - **充分统计量**：包含所有样本信息。
    - **完全统计量**：确保无偏估计的唯一性。
      263
  - **应用**：在伯努利、均匀、正态、泊松等常见分布中，可以显式地给出 UMVUE。
  - **注意事项**：UMVUE 的存在性和形式依赖于统计模型和参数函数。

- **指数族** 中的估计量具有良好的数学性质，便于理论分析。

- **Cramer-Rao不等式** 给出了无偏估计的方差下界，是衡量估计量有效性的重要工具
- **Fisher信息** 反映了总体参数的信息量，信息量越大，估计精度越高
- **有效估计** 是达到C-R下界的无偏估计，具有最小方差
- **线性回归** 提供了连接解释变量和响应变量的统计框架
- **估计方法**：
  - **OLS**：最小化残差平方和，具有优良的有限样本性质
  - **矩估计**：基于矩条件，与OLS在经典假设下等价
  - **MLE**：在正态假设下与OLS相同，具有良好大样本性质
- **估计量性质**：
  - 无偏性、有效性(BLUE)、正态分布（在正态误差下）
  - 方差估计需要偏差校正以获得无偏性

## 总结对比

| 估计方法       | 优点                       | 缺点                       | 适用场景                   |
| -------------- | -------------------------- | -------------------------- | -------------------------- |
| **矩估计**     | 简单直观，无需分布假设     | 估计量可能不唯一，效率不高 | 初步估计，复杂模型         |
| **MLE**        | 优良的大样本性质，渐近有效 | 需要分布假设，可能无解析解 | 参数模型，大样本           |
| **UMVUE**      | 最优无偏性，理论完备       | 构造复杂，存在性不保证     | 精确推断，小样本           |
| **核密度估计** | 无需分布假设，灵活性强     | 收敛速度慢，带宽选择敏感   | 非参数密度估计，探索性分析 |

**核心关系**：

- 在正态假设下，线性回归的 OLS、矩估计和 MLE 等价
- MLE 在大样本下具有最优性质
- UMVUE 在有限样本下提供最优无偏估计
- 不同方法各有适用场景，应根据具体问题选择
