## 1.1 总体与样本 (Population and Sample)

- **总体 (Population)**：所有研究对象的集合，通常用一个随机变量 $X$ 或其分布 $F$ 描述。
- **个体 (Individual)**：总体中的每一个元素。
- **样本 (Sample)**：从总体中抽取的一部分数据，记为 $X_1, X_2, \ldots, X_n$。
- **样本量 (Sample Size)**：$n$。
- **简单随机样本 (Simple Random Sample)**：若 $X_1, X_2, \ldots, X_n$ 是独立同分布的，即：
  $$
  X_1, X_2, \ldots, X_n \stackrel{\text{i.i.d.}}{\sim} F
  $$

## 1.2 样本空间 (Sample Space)

- **样本空间 $\mathcal{X}$**：所有可能样本值的集合。
- **观测值**：抽样后得到的实际数值 $x = (x_1, x_2, \ldots, x_n)$。

## 1.3 统计模型 (Statistical Model)

- **统计模型**：描述样本分布的数学模型，通常是一个分布族：
  $$
  \mathcal{F} = \{ f(x; \theta) : \theta \in \Theta \}
  $$
- **参数空间 (Parameter Space)**：$\Theta$，参数所有可能取值的集合。

## 1.4 统计量 (Statistic)

- **定义**：样本的函数 $T(X_1, X_2, \ldots, X_n)$，且不依赖于未知参数。
- **常用统计量**：
  - 样本均值 (Sample mean)：
    $$
    \bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
    $$
  - 样本方差 (Sample variance)：
    $$
    S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
    $$
  - 样本矩 (Sample moments)：
    $$
    a_{n,k} = \frac{1}{n} \sum_{i=1}^n X_i^k,\quad m_{n,k} = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^k
    $$
  - 样本协方差 (Sample covariance)：
    $$
    S_{XY} = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})(Y_i - \bar{Y})
    $$
  - 样本变异系数 (Sample coefficient of variation)：
    $$
    \hat{\nu} = \frac{S}{\bar{X}}
    $$
  - 样本偏度 (Sample skewness)：
    $$
    \hat{\beta}_1 = \frac{m_{n,3}}{m_{n,2}^{3/2}} = \sqrt{n} \frac{\sum_{i=1}^n (X_i - \bar{X})^3}{\left( \sum_{i=1}^n (X_i - \bar{X})^2 \right)^{3/2}}
    $$
    （对正态分布等于 0）
    其中 \( m_{n,k} \) 是样本 \( k \) 阶中心矩。
  - 样本峰度 (Sample kurtosis)：
    $$
    \hat{\beta}_2 = \frac{m_{n,4}}{m_{n,2}^2} - 3 = n \frac{\sum_{i=1}^n (X_i - \bar{X})^4}{\left( \sum_{i=1}^n (X_i - \bar{X})^2 \right)^2} - 3
    $$
    此处为**超额峰度**，正态分布的峰度定义为 3，减去 3 后正态分布对应 0。
    （对正态分布等于 0）
    其中 \( m_{n,k} \) 是样本 \( k \) 阶中心矩。

## 1.5 顺序统计量 (Order Statistics)

- **定义**：将样本按升序排列：$X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$
- **样本中位数**：
  $$
  m_{1/2} = 
  \begin{cases}
  X_{((n+1)/2)}, & n \text{ 为奇数} \\
  \frac{1}{2} \left[ X_{(n/2)} + X_{(n/2+1)} \right], & n \text{ 为偶数}
  \end{cases}
  $$
- **样本极差**：
  $$
  R = X_{(n)} - X_{(1)}
  $$

## 1.6 经验分布函数 (Empirical Distribution Function, E.D.F.)  

- **定义**：
  
  给定观测样本 \(X_1, X_2, \dots, X_n\)，经验分布函数 \(F_n(x)\) 定义为：
  $$
  F_n(x) = \frac{1}{n} \left[ \text{样本 } X_i \text{ 中小于等于 } x \text{ 的个数} \right] = \frac{1}{n} \sum_{i=1}^n I_{(-\infty, x]}(X_i)
  $$
  按顺序统计量 \(X_{(1)} \leq X_{(2)} \leq \dots \leq X_{(n)}\) 可表示为分段函数：
  $$
  F_n(x) =
  \begin{cases} 
  0, & x < X_{(1)}, \\ 
  \frac{k}{n}, & X_{(k)} \leq x < X_{(k+1)}, \quad k = 1, 2, \dots, n-1, \\ 
  1, & X_{(n)} \leq x.
  \end{cases}
  $$
  
- **性质**：
  - $nF_n(x) \sim B(n, F(x))$
  
  - 根据弱大数定律 (WLLN)，依概率收敛：$F_n(x) \xrightarrow{P} F(x)$
  
  - 根据强大数定律 (SLLN)，几乎处处收敛：$F_n(x) \xrightarrow{a.s.} F(x)$
  
  - 根据中心极限定理 (CLT)：
    $$
    \frac{\sqrt{n}(F_n(x) - F(x))}{\sqrt{F(x)(1 - F(x))}} \xrightarrow[n\to\infty]{d} N(0,1)
    $$
    
  - Glivenko–Cantelli 定理：
    $$
    \text{Let } D_n = \sup_{-\infty < x < \infty} |F_n(x) - F(x)| \\
    \text{then } P\left( \lim_{n \to \infty} D_n = 0 \right) = 1
    $$
    等价于：
    $$
    \sup_x |F_n(x) - F(x)| \xrightarrow{a.s.} 0
    $$

## 1.7 统计推断的类型 (Types of Statistical Inference)

- **参数推断 (Parametric Inference)**：已知分布形式，推断参数。
- **非参数推断 (Nonparametric Inference)**：不假设分布形式，推断分布特征。
- **点估计 (Point Estimation)**：用统计量估计参数。
- **区间估计 (Interval Estimation)**：构造参数的置信区间。
- **假设检验 (Hypothesis Testing)**：检验关于参数的假设。

---

## 小结 (Summary)

- **统计学基本概念**：
  - 总体、样本、样本空间是统计推断的基础。
  - 统计量是样本的函数，用于推断总体特征。
  - 经验分布函数是估计总体分布的非参数方法。
  - 统计推断分为参数与非参数、点估计与区间估计、假设检验等。
- **关键公式**：
  - 样本均值：$\bar{X} = \frac{1}{n} \sum X_i$
  - 样本方差：$S^2 = \frac{1}{n-1} \sum (X_i - \bar{X})^2$
  - 经验分布函数：$F_n(x) = \frac{1}{n} \sum I_{(-\infty, x]}(X_i)$
