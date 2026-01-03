## 7.1 贝叶斯与频率统计的基本对比 (Bayesian vs. Frequentist Statistics)

### 7.1.1 频率统计 (Frequentist Statistics)
- **核心假设**：
  - 参数 $\theta$ 是固定未知常数。
  - 概率定义为长期频率的极限。
  - 推断基于重复抽样思想。
- **推断方法**：
  - 点估计（如 MLE、矩估计）
  - 置信区间（频率解释）
  - 假设检验（基于 $p$ 值）
- **关键局限**：
  - 不直接给出“参数在区间内的概率”。
  - 依赖于未观测到的数据空间（如 $p$ 值计算）。

### 7.1.2 贝叶斯统计 (Bayesian Statistics)
- **核心假设**：
  - 参数 $\theta$ 是随机变量，具有概率分布。
  - 概率是主观信念的度量。
  - 推断基于先验信念与数据的结合。
- **推断框架**：
  - 先验分布 $\pi(\theta)$ 表达对 $\theta$ 的初始信念。
  - 后验分布 $\pi(\theta \mid x)$ 综合先验与数据。
  - 所有推断基于后验分布进行。

### 7.1.3 似然原理 (Likelihood Principle)
- **内容**：若两个实验产生的似然函数成比例，则它们应对 $\theta$ 提供相同的证据。
- **频率统计**：某些方法（如 $p$ 值）违反似然原理。
- **贝叶斯统计**：自动满足似然原理，因后验仅通过似然依赖于数据。

---

## 7.2 贝叶斯推断的基本原理 (Fundamentals of Bayesian Inference)

### 7.2.1 先验分布、似然与后验分布 (Prior, Likelihood and Posterior)

- **先验分布 (Prior Distribution)** $\pi(\theta)$：
  - 描述在见到数据前对 $\theta$ 的不确定性。
  - 可以是主观的（基于专家知识）或非信息的（如均匀先验）。
  
- **似然函数 (Likelihood Function)** $f(x \mid \theta)$：
  - 描述在给定 $\theta$ 下观测到数据 $x$ 的概率。
  
- **后验分布 (Posterior Distribution)** $\pi(\theta \mid x)$：
  - 结合先验与数据后的更新信念。
  - 由贝叶斯定理给出：

$$
\pi(\theta \mid x) = \frac{f(x \mid \theta) \pi(\theta)}{m(x)} \propto f(x \mid \theta) \pi(\theta)
$$

其中 $m(x) = \int f(x \mid \theta) \pi(\theta) d\theta$ 为**边际似然 (Marginal Likelihood)**，亦称证据（Evidence）。

### 7.2.2 共轭先验 (Conjugate Priors)

- **定义**：若先验分布与后验分布属于同一分布族，则称该先验为**共轭先验**。
- **优点**：
  - 后验有解析形式。
  - 计算简便，易于理解。
- **常见例子**：

| 总体分布                                       | 参数     | 共轭先验                      | 后验分布                                 |
| ---------------------------------------------- | -------- | ----------------------------- | ---------------------------------------- |
| $X \sim B(1, \theta)$                          | $\theta$ | $\text{Beta}(a,b)$            | $\text{Beta}(a+x, b+n-x)$                |
| $X \sim N(\theta, \sigma^2)$ ($\sigma^2$ 已知) | $\theta$ | $N(\mu_0, \tau_0^2)$          | $N(\mu_n, \tau_n^2)$                     |
| $X \sim \text{Poisson}(\theta)$                | $\theta$ | $\text{Gamma}(\alpha, \beta)$ | $\text{Gamma}(\alpha+\sum x_i, \beta+n)$ |

其中后验参数更新公式见具体推导。

### 7.2.3 先验的构造方法 (Constructing Priors)

#### 7.2.3.1 主观先验 (Subjective Priors)
- 基于历史数据、专家知识或理论模型。
- 可进行敏感性分析：更换不同先验，检查结论是否稳健。

#### 7.2.3.2 非信息先验 (Non-informative Priors)
- 旨在让数据“自己说话”，最小化先验影响。
- **均匀先验 (Uniform Prior)**：
  - $\pi(\theta) \propto 1$，可能为**广义先验 (Improper Prior)**。
  - 需确保后验是正常（Proper）的。
- **Jeffreys 先验**：
  - $\pi(\theta) \propto \sqrt{I(\theta)}$，其中 $I(\theta)$ 为 Fisher 信息。
  - 具有**重参数化不变性**。
- **最大熵先验 (Maximum Entropy Prior)**：
  - 在给定约束（如矩条件）下，选择熵最大的分布。
  - 对正态约束给出正态先验。

#### 7.2.3.3 分层先验 (Hierarchical Priors)
- 先验参数本身也有分布，形成层次结构：
  $$
  \pi(\theta) = \int \pi(\theta \mid \psi) g(\psi) d\psi
  $$
- 适用于参数具有组结构的情形（如多组均值估计）。

---

## 7.3 贝叶斯点估计 (Bayesian Point Estimation)

### 7.3.1 常用估计量

- **后验众数估计 (Maximum A Posteriori, MAP)**：
  $$
  \hat{\theta}_{\text{MAP}} = \arg \max_{\theta} \pi(\theta \mid x)
  $$
  - 在均匀先验下，MAP 等于 MLE。
  
- **后验均值估计 (Posterior Mean)**：
  $$
  \hat{\theta}_{\text{mean}} = E[\theta \mid x] = \int \theta \, \pi(\theta \mid x) d\theta
  $$
  - 在平方损失下，是**最优估计**（最小化后验均方误差 PMSE）。

- **后验中位数估计 (Posterior Median)**：
  $$
  \hat{\theta}_{\text{median}} = \text{median of } \pi(\theta \mid x)
  $$
  - 在绝对损失下最优。

### 7.3.2 估计精度：后验均方误差 (Posterior Mean Squared Error, PMSE)

$$
\text{PMSE}(\hat{\theta}) = E[(\theta - \hat{\theta})^2 \mid x] = \text{Var}(\theta \mid x) + (\hat{\theta} - E[\theta \mid x])^2
$$

- 后验均值估计使 PMSE 最小。
- 后验方差 $\text{Var}(\theta \mid x)$ 是估计不确定性的度量。

### 7.3.3 例子

#### 例1：正态均值估计（方差已知）
- $X_i \stackrel{\text{i.i.d.}}{\sim} N(\theta, \sigma^2)$，$\sigma^2$ 已知。
- 先验：$\theta \sim N(\mu_0, \tau_0^2)$。
- 后验：$\theta \mid x \sim N(\mu_n, \tau_n^2)$，其中
  $$
  \mu_n = \frac{\sigma^2/n}{\sigma^2/n + \tau_0^2} \mu_0 + \frac{\tau_0^2}{\sigma^2/n + \tau_0^2} \bar{x}, \quad \tau_n^2 = \frac{\sigma^2 \tau_0^2}{n\tau_0^2 + \sigma^2}
  $$
- 后验均值 $\mu_n$ 是先验均值与样本均值的加权平均。

#### 例2：二项成功率估计
- $X \sim B(n, \theta)$。
- 先验：$\theta \sim \text{Beta}(a, b)$。
- 后验：$\theta \mid x \sim \text{Beta}(a+x, b+n-x)$。
- 后验均值：$\hat{\theta}_{\text{mean}} = \frac{a+x}{a+b+n}$。
- 特别当 $a=b=1$（均匀先验）时，$\hat{\theta}_{\text{mean}} = \frac{x+1}{n+2}$，避免极端估计（如 $x=0$ 时估计不为0）。

---

## 7.4 贝叶斯区间估计 (Bayesian Interval Estimation)

### 7.4.1 可信区间 (Credible Interval)

- **定义**：给定 $1-\alpha$，若区间 $[L(x), U(x)]$ 满足
  $$
  P(L(x) \le \theta \le U(x) \mid x) \ge 1-\alpha,
  $$
  则称 $[L, U]$ 为 $\theta$ 的 $1-\alpha$ **可信区间**。
- 与频率置信区间不同，这里的概率是**给定数据**下参数落在区间内的概率。

### 7.4.2 最高后验密度区间 (Highest Posterior Density Interval, HPD)

- **定义**：是所有 $1-\alpha$ 可信区间中长度最短的区间。
- 特点：区间内任一点的后验密度不低于区间外任一点。
- 对于单峰对称后验，HPD 区间即为等尾区间。

### 7.4.3 例子：正态均值的可信区间

- 沿用 7.3.3 例1 设置，后验 $\theta \mid x \sim N(\mu_n, \tau_n^2)$。
- $1-\alpha$ 等尾可信区间为：
  $$
  [\mu_n - z_{\alpha/2} \tau_n,\; \mu_n + z_{\alpha/2} \tau_n]
  $$

---

## 7.5 贝叶斯假设检验 (Bayesian Hypothesis Testing)

### 7.5.1 基本方法

- **假设**：$H_0: \theta \in \Theta_0$ vs $H_1: \theta \in \Theta_1$。
- 计算后验概率：
  $$
  \alpha_0 = P(\theta \in \Theta_0 \mid x), \quad \alpha_1 = P(\theta \in \Theta_1 \mid x)
  $$
- **决策**：若 $\alpha_1 > \alpha_0$，则倾向于拒绝 $H_0$。
- 可计算**后验优势比 (Posterior Odds)**：
  $$
  \frac{\alpha_1}{\alpha_0} = \frac{P(\theta \in \Theta_1 \mid x)}{P(\theta \in \Theta_0 \mid x)}
  $$

### 7.5.2 贝叶斯因子 (Bayes Factor)

- 比较两个模型 $M_0$ 与 $M_1$ 的相对支持程度：
  $$
  BF_{10} = \frac{m_1(x)}{m_0(x)} = \frac{\int f(x \mid \theta, M_1) \pi_1(\theta) d\theta}{\int f(x \mid \theta, M_0) \pi_0(\theta) d\theta}
  $$
- $BF_{10} > 1$ 表示数据更支持 $M_1$。

### 7.5.3 例子：二项分布的成功率检验

- $X \sim B(n, \theta)$，检验 $H_0: \theta \le 0.5$ vs $H_1: \theta > 0.5$。
- 取均匀先验 $\theta \sim U(0,1)$。
- 后验：$\theta \mid x \sim \text{Beta}(x+1, n-x+1)$。
- 计算 $\alpha_0 = P(\theta \le 0.5 \mid x)$，$\alpha_1 = 1 - \alpha_0$。

---

## 7.6 贝叶斯预测 (Bayesian Prediction)

### 7.6.1 后验预测分布 (Posterior Predictive Distribution)

- **问题**：已有数据 $x$，预测新观测 $\tilde{x}$。
- 后验预测密度：
  $$
  p(\tilde{x} \mid x) = \int f(\tilde{x} \mid \theta) \pi(\theta \mid x) d\theta
  $$
- 意义：综合了参数不确定性（通过后验）与抽样变异性。

### 7.6.2 例子：二项分布的预测

- $X \sim B(n, \theta)$，先验 $\theta \sim \text{Beta}(a,b)$。
- 后验：$\theta \mid x \sim \text{Beta}(a+x, b+n-x)$。
- 预测新 $m$ 次试验中成功次数 $Y$：
  $$
  P(Y=y \mid x) = \int_0^1 \binom{m}{y} \theta^y (1-\theta)^{m-y} \pi(\theta \mid x) d\theta
  $$
  该分布为 **Beta-Binomial 分布**。

---

## 7.7 贝叶斯计算技术 (Computational Techniques for Bayesian Inference)

### 7.7.1 解析方法

- 适用于共轭先验或简单模型。
- 可直接计算后验、后验矩、可信区间等。

### 7.7.2 数值方法

- **马尔可夫链蒙特卡洛 (Markov Chain Monte Carlo, MCMC)**：
  - 通过构建马尔可夫链，使其平稳分布为目标后验分布。
  - **Gibbs 抽样**：轮流从各参数的条件后验中抽样。
  - **Metropolis-Hastings 算法**：更一般的接受-拒绝抽样框架。
- **变分近似 (Variational Approximation)**：
  - 用简单分布族逼近后验，转化为优化问题。
- **拉普拉斯近似 (Laplace Approximation)**：
  - 在后验众数处进行二阶泰勒展开，近似为正态分布。

### 7.7.3 边际似然的计算

- 用于模型比较（如贝叶斯因子）。
- 方法：
  - **调和平均估计**
  - **桥抽样 (Bridge Sampling)**
  - **嵌套抽样 (Nested Sampling)**

---

## 7.8 贝叶斯决策理论 (Bayesian Decision Theory)

### 7.8.1 基本框架

- **行动空间** $\mathcal{A}$：所有可能决策的集合。
- **损失函数** $L(a, \theta)$：采取行动 $a$ 而真实参数为 $\theta$ 时的损失。
- **贝叶斯风险**：后验期望损失
  $$
  R(a \mid x) = E[L(a, \theta) \mid x]
  $$
- **贝叶斯决策**：选择使后验期望损失最小的行动
  $$
  a^* = \arg \min_{a \in \mathcal{A}} R(a \mid x)
  $$

### 7.8.2 常见损失函数下的贝叶斯估计

- **平方损失** $L(\hat{\theta}, \theta) = (\hat{\theta} - \theta)^2$ → 后验均值。
- **绝对损失** $L(\hat{\theta}, \theta) = |\hat{\theta} - \theta|$ → 后验中位数。
- **0-1损失**（假设检验）→ 选择后验概率最大的假设。

### 7.8.3 例子：疫苗接种决策

- 暴露于病毒后，感染概率 $\theta \sim \text{Beta}(1,2)$（先验）。
- 疫苗费用 £500，死亡损失极高（设为 ∞）。
- 计算接种与不接种的后验期望损失，选择损失较小的行动。

---

## 小结

- **贝叶斯推断** 将参数视为随机变量，通过先验分布表达初始信念，再利用贝叶斯定理将先验与数据结合得到后验分布，并基于后验进行所有推断。
- **与频率统计对比**：
  - 贝叶斯方法提供参数的概率陈述（如可信区间）。
  - 满足似然原理，且推断自然包含先验信息。
- **核心组成**：
  - **先验选择**：主观先验、非信息先验（均匀、Jeffreys、最大熵）、分层先验。
  - **后验计算**：共轭先验（解析解）、MCMC 等数值方法。
  - **点估计**：后验众数（MAP）、后验均值、后验中位数，其中后验均值在平方损失下最优。
  - **区间估计**：可信区间（直接概率解释），HPD 区间最短。
  - **假设检验**：基于后验概率或贝叶斯因子进行比较。
  - **预测**：通过后验预测分布综合参数与抽样不确定性。
- **决策理论**：为贝叶斯推断提供损失最小化的决策框架。
- **计算**：现代贝叶斯分析常依赖 MCMC 等数值方法处理复杂后验。

**关键公式**：

- 贝叶斯定理：
  $$
  \pi(\theta \mid x) \propto f(x \mid \theta) \pi(\theta)
  $$
- 后验均值（平方损失最优）：
  $$
  \hat{\theta}_{\text{mean}} = E[\theta \mid x]
  $$
- $1-\alpha$ 可信区间：
  $$
  P(L(x) \le \theta \le U(x) \mid x) \ge 1-\alpha
  $$
- 贝叶斯决策：
  $$
  a^* = \arg\min_a E[L(a, \theta) \mid x]
  $$

**应用提示**：
- 先验选择应反映可用信息，并进行敏感性分析。
- 对于非共轭模型，需熟练掌握 MCMC 等计算方法。
- 贝叶斯方法特别适合顺序更新、预测问题和决策分析。
