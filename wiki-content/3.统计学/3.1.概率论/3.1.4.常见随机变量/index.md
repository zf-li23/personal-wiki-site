## 4.1 离散型随机变量

### 4.1.1 基本概念

**定义**：如果随机变量$X$只取有限个值$x_1, \ldots, x_m$或者可列个值$x_1, x_2, \ldots$，则称$X$是**离散型随机变量**。

**概率分布列（PMF）**：
$$
\mathbb{P}(X = x_k) = p_k, \quad k \geq 1
$$
满足：
1. $p_k \geq 0$
2. $\sum_{k=1}^{\infty} p_k = 1$

### 4.1.2 两点分布（Bernoulli分布）

**定义**：如果$X$只取值0或1，且
$$
\mathbb{P}(X = 1) = p = 1 - \mathbb{P}(X = 0)
$$
则称$X$服从**两点分布**，记作$X \sim B(1,p)$或$X \sim B(p)$。

**分布列**：
$$
\begin{array}{c|cc}
X & 0 & 1 \\
\hline
\mathbb{P} & 1-p & p \\
\end{array}
$$

### 4.1.3 二项分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n
$$
则称$X$服从**二项分布**，记作$X \sim B(n,p)$。

**性质**：
- 如果$X_1, \ldots, X_n$相互独立且都服从$B(1,p)$，则$S = X_1 + \cdots + X_n \sim B(n,p)$
- 如果$X \sim B(n,p)$，$Y \sim B(m,p)$且相互独立，则$X + Y \sim B(m+n,p)$

**最大可能值**：
- 当$(n+1)p$为整数时，$b((n+1)p,n,p)$与$b((n+1)p-1,n,p)$均为最大项
- 当$(n+1)p$不为整数时，$b([(n+1)p],n,p)$为唯一最大项

### 4.1.4 几何分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = (1-p)^{k-1}p, \quad k = 1, 2, \ldots
$$
则称$X$服从**几何分布**，记作$X \sim G(p)$。

**无记忆性**：取正整数值的随机变量$X \sim G(p)$的充要条件是对每个$k \geq 1$，
$$
\mathbb{P}(X = k + 1 | X > k) = \mathbb{P}(X = 1)
$$

### 4.1.5 帕斯卡分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = \binom{k-1}{r-1} (1-p)^{k-r} p^r, \quad k = r, r+1, \ldots
$$
则称$X$服从**帕斯卡分布**。

**注**：当$r = 1$时，帕斯卡分布就是几何分布。

### 4.1.6 负二项分布

**定义**：令$Y = X - r$，则$Y$的概率分布为
$$
\mathbb{P}(Y = k) = \binom{k+r-1}{r-1} (1-p)^k p^r, \quad k = 0, 1, \ldots
$$
称$Y$服从**负二项分布**，记作$Y \sim NB(r,p)$。

### 4.1.7 超几何分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = \frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}}, \quad k = 0, 1, \ldots, \min\{n, M\}
$$
则称$X$服从**超几何分布**，记作$X \sim H(n, M, N)$。

**近似性质**：当$N$很大时，超几何分布可用二项分布近似：
$$
\frac{\binom{M}{k}\binom{N-M}{n-k}}{\binom{N}{n}} \approx \binom{n}{k} p_N^k (1-p_N)^{n-k}, \quad \text{其中 } p_N = \frac{M}{N}
$$

### 4.1.8 负超几何分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = \frac{\binom{k+r-1}{k}\binom{N-k-r}{M-r}}{\binom{N}{M}}, \quad k = 0, 1, \ldots, N-M
$$
则称$X$服从**负超几何分布**，记作$X \sim NH(r, M, N)$。

### 4.1.9 泊松分布

**定义**：如果随机变量$X$的概率分布为
$$
\mathbb{P}(X = k) = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k = 0, 1, 2, \ldots
$$
则称$X$服从**泊松分布**，记作$X \sim \mathcal{P}(\lambda)$。

**应用**：
- 某段高速公路一年内交通事故数
- 某市场一天中到达的顾客次数
- 某办公室一天中收到的电话数

**与二项分布的关系**：如果$n$很大，$p$很小，且$np \approx \lambda$，则可用$\mathcal{P}(\lambda)$近似$B(n,p)$

## 4.2 连续型随机变量

### 4.2.1 基本概念

**定义**：设随机变量$X$，如果存在非负函数$f(x)$使得对任意$a < b$，
$$
\mathbb{P}(a < X \leq b) = \int_a^b f(x) dx
$$
则称$X$是**连续型随机变量**，称$f(x)$是$X$的**概率密度函数（PDF）**。

**性质**：
1. $\int_{-\infty}^{\infty} f(x) dx = 1$
2. 对任意Borel集$A$，有$\mathbb{P}(X \in A) = \int_A f(x) dx$
3. $\mathbb{P}(X = a) = 0$

### 4.2.2 均匀分布

**定义**：对$a < b$，如果$X$的概率密度为
$$
f(x) = 
\begin{cases} 
\frac{1}{b - a}, & x \in (a, b) \\
0, & x \notin (a, b)
\end{cases}
$$
称$X$服从**均匀分布**，记作$X \sim U(a,b)$。

**推广**：对Borel集$A$，如果$X$的密度为
$$
f(x) = 
\begin{cases} 
\frac{1}{m(A)}, & x \in A \\
0, & x \notin A
\end{cases}
$$
称$X$服从$A$上的均匀分布，记作$X \sim U(A)$。

### 4.2.3 指数分布

**定义**：对正常数$\lambda$，如果$X$的概率密度为
$$
f(x) = 
\begin{cases} 
\lambda e^{-\lambda x}, & x \geq 0 \\
0, & x < 0
\end{cases}
$$
称$X$服从**指数分布**，记作$X \sim \mathcal{E}(\lambda)$。

**无记忆性**：连续型非负随机变量$X$服从指数分布的充要条件是对任意的$s, t \geq 0$，
$$
\mathbb{P}(X > s + t | X > s) = \mathbb{P}(X > t)
$$

**应用**：
- 到发生某个事件为止所用的时间
- 仪器的使用寿命

### 4.2.4 正态分布

**定义**：如果$X$的密度为
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}
$$
称$X$服从**正态分布**，记作$X \sim N(\mu, \sigma^2)$。

**标准正态分布**：当$X \sim N(0,1)$时，密度函数为
$$
\varphi(x) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{x^2}{2}\right), \quad x \in \mathbb{R}
$$

**性质**：
- $f(x)$关于$x = \mu$对称
- $f(\mu) = (\sigma\sqrt{2\pi})^{-1}$是最大值
- $f(x)$在$x = \mu \pm \sigma$处有拐点

**背景与应用**：
- De Moive-Laplace中心极限定理
- 天文学中的测量误差
- Brown运动研究
- 产品质量指标、生理指标等

### 4.2.5 其他连续型分布（拓展）

#### Beta分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1}(1-x)^{\beta-1}, \quad 0 < x < 1
$$
其中$B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$，称$X$服从**Beta分布**，记作$X \sim Beta(\alpha, \beta)$。
$$
\Gamma (x) = \int_0^{+\infty} e^{-t} t^{x-1} dt \quad (x > 0)
$$
**特例**：当$\alpha = \beta = 1$时，为均匀分布$U(0,1)$

#### Gamma分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}, \quad x \geq 0
$$
称$X$服从**Gamma分布**，记作$X \sim \Gamma(\alpha, \lambda)$。

**特例**：
- 当$\alpha = 1$时，为指数分布
- 当$\alpha$为正整数时，称为Erlang分布

#### Weibull分布
**定义**：如果$X$的密度为
$$
f(x) = \lambda a x^{\alpha-1} \exp(-\lambda x^\alpha), \quad x \geq 0
$$
称$X$服从**Weibull分布**。

**特例**：
- 当$\alpha = 1$时，为指数分布
- 当$\alpha = 2$时，为Rayleigh分布

#### Rayleigh分布
**定义**：如果$X$的密度为
$$
f(x) = x e^{-\frac{x^2}{2}}, \quad x \geq 0
$$
称$X$服从**Rayleigh分布**。

**性质**：设$X,Y$独立且都服从$N(0,1)$，则$(X,Y)$服从二元正态分布，$R=\sqrt{X^2+Y^2}$服从Rayleigh分布。

#### 卡方分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{1}{2^{v/2} \Gamma(v/2)} x^{\frac{v}{2}-1} e^{-\frac{x}{2}}, \quad x \geq 0
$$
称$X$服从**卡方分布**，记作$X \sim \chi_v^2$。

**性质**：如果$Z_1, \ldots, Z_n$ i.i.d. $\sim N(0,1)$，则$X = Z_1^2 + \cdots + Z_n^2 \sim \chi_n^2$

#### t分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{\Gamma\left(\frac{v+1}{2}\right)}{\sqrt{v\pi} \Gamma\left(\frac{v}{2}\right)} \left(1 + \frac{x^2}{v}\right)^{-\frac{v+1}{2}}, \quad x \in \mathbb{R}
$$
称$X$服从**t分布**，记作$X \sim t_v$。

**性质**：若$Z \sim N(0,1)$，$X \sim \chi_n^2$且独立，则$T = \frac{Z}{\sqrt{X/n}} \sim t_n$

**特例**：若$v = 1$，则$X \sim t_1$为Cauchy分布

#### Cauchy分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{1}{\pi(1 + x^2)}, \quad x \in \mathbb{R}
$$
称$X$服从**Cauchy分布**，可记作$X \sim t_1$。

**性质**：按照期望的严格数学定义，Cauchy分布没有期望和方差。

#### F分布
**定义**：如果$X$的密度为
$$
f(x) = \frac{\Gamma\left(\frac{m+n}{2}\right) m^{m/2} n^{n/2} x^{\frac{m}{2}-1}}{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right) (mx+n)^{\frac{(m+n)}{2}}}, \quad x \geq 0
$$
称$X$服从**F分布**，记作$X \sim F(m,n)$。

**性质**：设有独立同分布 (i.i.d) 的变量$X_i \sim N(0,1), \quad i=1,\dots,m$和独立同分布的变量$Y_j \sim N(0,1), \quad j=1,\dots,n$，令$F=\frac{\frac{\sum_i{X_i^2}}{m}}{\frac{\sum_j{Y_j^2}}{n}}$，则$F \sim F(m,n)$

## 小结

### 核心知识点
- **离散型随机变量**：两点分布、二项分布、几何分布、泊松分布等
- **连续型随机变量**：均匀分布、指数分布、正态分布等
- **分布间的关系**：二项分布与泊松分布的近似、超几何分布与二项分布的近似等

### 重要性质
- 几何分布和指数分布的无记忆性
- 二项分布的最大可能值
- 正态分布的对称性和钟形特征
- 各种分布之间的近似关系

### 应用技巧
- 利用实际问题背景选择合适的分布
- 掌握分布间的关系以便进行近似计算
- 理解各种分布的特性和适用场景

### 关键公式总结
- 二项分布：$\mathbb{P}(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- 几何分布：$\mathbb{P}(X = k) = (1-p)^{k-1}p$
- 泊松分布：$\mathbb{P}(X = k) = \frac{\lambda^k}{k!} e^{-\lambda}$
- 均匀分布：$f(x) = \frac{1}{b-a}I_{(a,b)}(x)$
- 指数分布：$f(x) = \lambda e^{-\lambda x}I_{[0,\infty)}(x)$
- 正态分布：$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$
