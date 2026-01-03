## 2.1 抽样分布 (Sampling Distribution)

### 2.1.1 基本概念
- **统计量**是样本的函数，因此是随机变量。
- **抽样分布**：统计量的概率分布。
- **精确抽样分布**：总体分布已知时统计量的分布，通常复杂难求。
- **极限分布**：当样本量 $n \to \infty$ 时统计量的极限分布，常用于大样本近似。

### 2.1.2 正态分布下的抽样分布

**定理1.** 设 $X_1, \ldots, X_n$ 独立，$X_k \sim N(a_k, \sigma_k^2)$，$c_1, \ldots, c_n$ 为常数，则
$$
T = \sum_{k=1}^n c_k X_k \sim N\left( \sum_{k=1}^n c_k a_k, \sum_{k=1}^n c_k^2 \sigma_k^2 \right) = N\left( a_k \sum_{k=1}^n c_k, \sigma_k^2 \sum_{k=1}^n c_k^2 \right) = N(\mu, \tau^2)
$$

**推论.** 若 $X_1, \ldots, X_n \stackrel{\text{i.i.d.}}{\sim} N(a, \sigma^2)$，则
$$
\bar{X} \sim N\left(a, \frac{\sigma^2}{n}\right)
$$

**定理 2. （正态向量的线性变换）**  
设 $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} N(a, \sigma^2)$，记 $\mathbf{X} = (X_1,\dots,X_n)^T$。  
设 $A = (a_{ij})$ 为 $n \times n$ 常数矩阵，$Y = A\mathbf{X}$，即  
\[
\begin{pmatrix} Y_1 \\ \vdots \\ Y_n \end{pmatrix} =
\begin{pmatrix}
a_{11} & \cdots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{n1} & \cdots & a_{nn}
\end{pmatrix}
\begin{pmatrix} X_1 \\ \vdots \\ X_n \end{pmatrix}.
\]

则：
1. **$Y$ 仍是正态随机向量**，且  
   \[
   E[Y_i] = a \sum_{k=1}^n a_{ik}, \quad 
   \mathrm{Var}(Y_i) = \sigma^2 \sum_{k=1}^n a_{ik}^2, \quad 
   \mathrm{Cov}(Y_i,Y_j) = \sigma^2 \sum_{k=1}^n a_{ik} a_{jk}.
   \]
2. **特别地**，若 $A$ 是 $n$ 阶正交矩阵（即 $AA^T = I$），则 $Y_1,\dots,Y_n$ **相互独立**，且  
   \[
   Y_i \sim N\!\left( a\sum_{k=1}^n a_{ik}, \ \sigma^2 \right).
   \]
3. 若进一步有 $a = 0$（即 $\mathbf{X} \sim N(0,\sigma^2 I)$），且 $A$ 为正交矩阵，则  
   \[
   Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} N(0,\sigma^2).
   \]

**定理3. (样本均值与样本方差)** 设 $$，则：

1. $\bar{X} \sim N(a, \sigma^2/n)$
2. $\dfrac{(n-1)S^2}{\sigma^2} \sim \chi_{n-1}^2$
3. $\bar{X}$ 与 $S^2$ 独立

### 2.1.3 三大抽样分布

#### 1. 卡方分布（$\chi^2$ Distribution）
**定义3.** 若 $X_1, \ldots, X_r \stackrel{\text{i.i.d.}}{\sim} N(0,1)$，则
$$
\xi = \sum_{i=1}^r X_i^2 \sim \chi_r^2
$$
**密度函数**：
$$
f(x) = \frac{1}{2^{r/2}\Gamma(r/2)} x^{(r/2)-1} e^{-x/2}, \quad x > 0
$$
**性质**：
- 特征函数：$\varphi(t) = (1 - 2it)^{-r/2}$
- $E(\xi) = r$, $\text{Var}(\xi) = 2r$
- 可加性：若 $\xi_i \sim \chi^2_{r_i}$ 独立，则 $\sum_{i=1}^k \xi_i \sim \chi^2_{r_1 + \cdots + r_k}$

#### 2. $t$ 分布（Student’s t Distribution）
**定义4.** 若 $X \sim N(0,1)$, $Y \sim \chi_r^2$ 独立，则
$$
T = \frac{X}{\sqrt{Y/r}} \sim t_r
$$
**密度函数**：
$$
f_T(t) = \frac{\Gamma\left(\frac{r+1}{2}\right)}{\Gamma\left(\frac{r}{2}\right)\sqrt{\pi r}} \left(1 + \frac{t^2}{r}\right)^{-(r+1)/2}, \quad t \in \mathbb{R}
$$
**性质**：
- 矩存在性：$E(T^k)$ 存在当且仅当 $k < r$；$k$ 为奇数时 $E(T^k)=0$
- $r \ge 2$ 时 $E(T) = 0$，$r \ge 3$ 时 $\text{Var}(T) = r/(r-2)$
- 特例：$t_1$ 是 Cauchy 分布，密度为 $f_1(t) = \frac{1}{\pi(1+t^2)}$
- $r \to \infty$ 时 $t_r$ 收敛于 $N(0,1)$

#### 3. $F$ 分布（F Distribution）
**定义5.** 若 $X \sim \chi_{r_1}^2$, $Y \sim \chi_{r_2}^2$ 独立，则
$$
F = \frac{X/r_1}{Y/r_2} \sim F_{r_1, r_2}
$$
**性质**：
- 倒数性：若 $F \sim F_{r_1,r_2}$，则 $1/F \sim F_{r_2,r_1}$
- 与 $t$ 分布的关系：若 $T \sim t_r$，则 $T^2 \sim F_{1,r}$
- 矩公式：若 $2k < r_2$，
  \[
  E(F^k) = \left( \frac{r_2}{r_1} \right)^k \frac{\Gamma\left(\frac{r_1}{2}+k\right)\Gamma\left(\frac{r_2}{2}-k\right)}{\Gamma\left(\frac{r_1}{2}\right)\Gamma\left(\frac{r_2}{2}\right)}
  \]
  特别地：
  \[
  E(F) = \frac{r_2}{r_2 - 2}\ (r_2 \ge 3),\quad
  \text{Var}(F) = \frac{2r_2^2(r_1 + r_2 - 2)}{r_1(r_2-2)^2(r_2-4)}\ (r_2 \ge 5)
  \]
- 分位数关系：$F_{r_1,r_2}(1 - \alpha) = 1 / F_{r_2,r_1}(\alpha)$

#### 4. 推论（Useful Corollaries）
- **推论1**（标准化平方和）：若 $X_i \sim N(a_i,\sigma_i^2)$ 独立，则
  \[
  \sum_{i=1}^n \left( \frac{X_i-a_i}{\sigma_i} \right)^2 \sim \chi_n^2
  \]
- **推论2**（单样本 t 统计量）：若 $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} N(a,\sigma^2)$，则
  \[
  T = \frac{\sqrt{n}(\bar{X}-a)}{S} \sim t_{n-1}
  \]
- **推论3**（两独立样本 t 统计量，方差相等）：若
  \[
  X_1,\dots,X_m \stackrel{\text{i.i.d.}}{\sim} N(a_1,\sigma^2),\quad
  Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} N(a_2,\sigma^2)
  \]
  且两者独立，则
  \[
  T = \frac{(\bar{X}-\bar{Y})-(a_1-a_2)}{S_w} \sqrt{\frac{mn}{m+n}} \sim t_{m+n-2}
  \]
  其中 $S_w^2 = \frac{(m-1)S_X^2 + (n-1)S_Y^2}{m+n-2}$。
- **推论4**（方差比 F 统计量）：在上述两样本情形（独立，正态），若 $\sigma_1^2,\sigma_2^2$ 为真方差，则
  \[
  F = \frac{S_X^2}{S_Y^2} \cdot \frac{\sigma_2^2}{\sigma_1^2} \sim F_{m-1,n-1}
  \]
- **推论5**（指数分布与卡方分布）：若 $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\lambda)$，则
  \[
  2\lambda n\bar{X} = 2\lambda \sum_{i=1}^n X_i \sim \chi_{2n}^2
  \]

### 2.1.4 极限分布与Slutsky定理
- **极限分布**：当 $n \to \infty$ 时统计量的极限分布。
- **Slutsky定理**：若 $X_n \xrightarrow{d} X$，$Y_n \xrightarrow{p} c$（常数），则：
  - $X_n + Y_n \xrightarrow{d} X + c$
  - $X_n Y_n \xrightarrow{d} cX$
  - $X_n / Y_n \xrightarrow{d} X/c$（若 $c \ne 0$）

**应用例子**：对于正态样本 $X_1,\dots,X_n \sim N(a,\sigma^2)$，有  
\[
\sqrt{n}(\overline{X}-a)/\sigma \xrightarrow{d} N(0,1)，\quad S^2 \xrightarrow{p} \sigma^2
\]
由Slutsky定理可得  
\[
\frac{\sqrt{n}(\overline{X} - a)}{S} \xrightarrow{d} N(0,1)
\]
实际上在有限样本下，它是自由度为 $n-1$ 的 $t$ 分布；当 $n \to \infty$ 时 $t_{n-1}$ 趋于标准正态分布。

---

## 2.2 指数族 (Exponential Family)

### 2.2.1 定义

**定义7.** 若分布族 $\mathcal{F} = \{f(x, \theta) : \theta \in \Theta\}$ 的密度函数可写为：
$$
f(x, \theta) = C(\theta) \exp\left\{ \sum_{i=1}^k Q_i(\theta) T_i(x) \right\} h(x)
$$
则称 $\mathcal{F}$ 为**指数族**。

**各符号含义**：
- $\theta$：参数（可为向量）
- $\Theta$：参数空间
- $k$：正整数，指数族维数
- $C(\theta) \ge 0$：仅依赖于参数的规范化函数
- $Q_i(\theta)$：仅依赖于参数的函数
- $T_i(x)$：仅依赖于样本 $x$ 的充分统计量函数
- $h(x) \ge 0$：仅依赖于样本的基准函数

---

### 2.2.2 示例

1. **正态分布** $N(\mu, \sigma^2)$ 的样本 $X_1,\dots,X_n$
   \[
   f(\boldsymbol{x};\mu,\sigma^2) = (\sqrt{2\pi}\sigma)^{-n} e^{-\frac{n\mu^2}{2\sigma^2}} \exp\left\{ \frac{\mu}{\sigma^2} \sum x_i - \frac{1}{2\sigma^2} \sum x_i^2 \right\}
   \]
   对应：
   \[
   C(\theta)=(\sqrt{2\pi}\sigma)^{-n}e^{-n\mu^2/(2\sigma^2)},\ 
   Q_1=\mu/\sigma^2,\ 
   Q_2=-1/(2\sigma^2),\ 
   T_1=\sum x_i,\ 
   T_2=\sum x_i^2,\ 
   h(\boldsymbol{x})=1.
   \]

2. **二项分布** $B(n, \theta)$
   \[
   f(x;\theta) = C_n^x \theta^x (1-\theta)^{n-x} = (1-\theta)^n \exp\left\{ x\log\frac{\theta}{1-\theta} \right\} C_n^x
   \]
   对应：
   \[
   C(\theta)=(1-\theta)^n,\ 
   Q_1=\log\frac{\theta}{1-\theta},\ 
   T_1=x,\ 
   h(x)=C_n^x.
   \]

3. **泊松分布** $P(\theta)$
   \[
   f(x;\theta) = \frac{e^{-\theta}\theta^x}{x!} = e^{-\theta} \exp\{ x\log\theta \} \frac{1}{x!}
   \]
   对应：
   \[
   C(\theta)=e^{-\theta},\ 
   Q_1=\log\theta,\ 
   T_1=x,\ 
   h(x)=1/x!.
   \]

4. **Gamma分布** $\Gamma(\gamma, \lambda)$ 的样本 $X_1,\dots,X_n$
   \[
   f(\boldsymbol{x};\gamma,\lambda) = \frac{\lambda^{n\gamma}}{(\Gamma(\gamma))^n} \exp\left\{ -\lambda\sum x_i + (\gamma-1)\sum\log x_i \right\} \prod I_{(0,\infty)}(x_i)
   \]
   对应：
   \[
   C(\theta)=\lambda^{n\gamma}/(\Gamma(\gamma))^n,\ 
   Q_1=-\lambda,\ 
   Q_2=\gamma-1,\ 
   T_1=\sum x_i,\ 
   T_2=\sum\log x_i,\ 
   h(\boldsymbol{x})=\prod I_{(0,\infty)}(x_i).
   \]

---

### 2.2.3 非指数族示例

1. **均匀分布** $U[0,\theta]$  
   \[
   f(x;\theta) = \frac{1}{\theta}I_{[0,\theta]}(x)
   \]
   支撑集 $[0,\theta]$ 依赖于 $\theta$。

2. **柯西分布**  
   \[
   f(x;\theta) = \frac{1}{\pi[1+(x-\theta)^2]}
   \]
   无法写成指数族形式。

**关键判别准则**：指数族的支撑集 $\{x: h(x) > 0\}$ 与参数 $\theta$ 无关。

---

### 2.2.4 自然形式 (Canonical Form)

**定义8.** 通过参数变换 $\varphi_i = Q_i(\theta)$，可将指数族化为**自然形式**：
$$
f(x, \varphi) = C^*(\varphi) \exp\left\{ \sum_{i=1}^k \varphi_i T_i(x) \right\} h(x),
$$
其中 $\varphi = (\varphi_1,\dots,\varphi_k)$ 称为**自然参数**，自然参数空间为：
$$
\Theta^* = \left\{ \varphi : \int \exp\left\{ \sum_{i=1}^k \varphi_i T_i(x) \right\} h(x) dx < \infty \right\}.
$$

**示例**：

1. 二项分布：令 $\varphi = \log\frac{\theta}{1-\theta}$，则
   \[
   f(x;\varphi) = (1+e^{\varphi})^{-n} \exp\{\varphi x\} C_n^x,
   \quad \Theta^* = (-\infty, \infty).
   \]

2. 正态分布：令 $\varphi_1 = \mu/\sigma^2,\ \varphi_2 = -1/(2\sigma^2)$，则
   \[
   f(\boldsymbol{x};\varphi) = (-\pi/\varphi_2)^{-n/2} \exp\{ n\varphi_1^2/(4\varphi_2) \} \exp\{\varphi_1\sum x_i + \varphi_2\sum x_i^2\},
   \]
   \[
   \Theta^* = \{(\varphi_1,\varphi_2): \varphi_1\in\mathbb{R},\ \varphi_2<0\}.
   \]

---

### 2.2.5 指数族的性质

1. **支撑集与参数无关**  
   所有分布的支撑集相同：$\{x: h(x)>0\}$，不依赖于 $\theta$。

2. **自然参数空间是凸集**  
   $\Theta^*$ 是 $\mathbb{R}^k$ 中的凸集。  
   **证明**：对任意 $\varphi^0,\varphi^1\in\Theta^*$ 和 $0<\alpha<1$，由 Hölder 不等式：
   \[
   \int \exp\left\{ \sum (\alpha\varphi_i^0 + (1-\alpha)\varphi_i^1)T_i(x) \right\} h(x) dx
   \le \left[ \int e^{\sum\varphi_i^0 T_i} h dx \right]^{\alpha}
       \left[ \int e^{\sum\varphi_i^1 T_i} h dx \right]^{1-\alpha} < \infty.
   \]

3. **矩母函数的可微性**  
   若 $\varphi$ 是内点，对任意使积分 $G(\varphi)=\int g(x) e^{\sum\varphi_i T_i(x)} h(x) dx$ 存在的 $g(x)$，$G(\varphi)$ 在 $\Theta^*$ 内部任意阶可导，且：
   \[
   \frac{\partial^m G(\varphi)}{\partial\varphi_1^{m_1}\cdots\partial\varphi_k^{m_k}}
   = \int g(x) \left( \prod T_i^{m_i}(x) \right) e^{\sum\varphi_i T_i(x)} h(x) dx.
   \]
   **应用**：矩的计算（令 $g(x)=1$ 得矩母函数）：
   \[
   E[T_i(X)] = -\frac{\partial}{\partial\varphi_i} D(\varphi),\quad
   \text{Cov}[T_i(X),T_j(X)] = -\frac{\partial^2}{\partial\varphi_i\partial\varphi_j} D(\varphi),
   \]
   其中 $D(\varphi) = \log C^*(\varphi)$。

4. **光滑可逆变换下的封闭性**  
   若 $Y = Y(X)$ 是光滑可逆变换，则 $Y$ 的分布仍为指数族。  
   **原因**：Jacobi 项 $|\partial X/\partial Y|$ 仅依赖于 $y$，不影响 $C(\theta), Q_i(\theta)$ 的形式。

---

## 2.3 充分统计量与完全统计量 (Sufficient and Complete Statistics)

### 2.3.1 充分统计量 (Sufficient Statistic)

设 \(\boldsymbol{X} = (X_1, \dots, X_n)\) 是来自分布族 \(\{f(x; \theta): \theta \in \Theta\}\) 的随机样本，\(T = T(\boldsymbol{X})\) 是一个统计量。

**定义 8 (充分统计量).** 如果在给定 \(T=t\) 的条件下，样本 \(\boldsymbol{X}\) 的条件分布与参数 \(\theta\) 无关，即：
\[
f_{\boldsymbol{X} \mid T}(\boldsymbol{x} \mid t; \theta) = f_{\boldsymbol{X} \mid T}(\boldsymbol{x} \mid t), \quad \forall \theta \in \Theta,
\]
则称 \(T(\boldsymbol{X})\) 是 \(\theta\) 的**充分统计量**。

---

### 2.3.2 因子分解定理 (Factorization Theorem)

**定理 6 (因子分解定理).** \(T(\boldsymbol{X})\) 是充分统计量当且仅当存在非负函数 \(g\) 和 \(h\)，使得样本的联合密度（或概率）函数可分解为：
\[
f(\boldsymbol{x}; \theta) = g(T(\boldsymbol{x}); \theta) \cdot h(\boldsymbol{x}), \quad \forall \boldsymbol{x} \in \mathcal{X}, \ \theta \in \Theta,
\]
其中 \(h(\boldsymbol{x})\) 与 \(\theta\) 无关，\(g\) 只通过 \(T(\boldsymbol{x})\) 依赖于 \(\boldsymbol{x}\)。

#### 例子
1. **伯努利分布**  
   设 \(\boldsymbol{X} \stackrel{\text{i.i.d.}}{\sim} B(1, \theta)\)，则联合概率为：
   \[
   f(\boldsymbol{x}; \theta) = \theta^{\sum x_i} (1-\theta)^{n-\sum x_i} = g(t(\boldsymbol{x}); \theta) \cdot 1,
   \]
   其中 \(t(\boldsymbol{x}) = \sum_{i=1}^n x_i\) 是充分统计量 \(T(\boldsymbol{X})\) 的观测值。

2. **正态分布 (方差已知)**  
   设 \(\boldsymbol{X} \stackrel{\text{i.i.d.}}{\sim} N(\theta, 1)\)，则：
   \[
   f(\boldsymbol{x}; \theta) = (2\pi)^{-\frac{n}{2}} e^{-\frac{1}{2} \sum (x_i - \theta)^2} = (2\pi)^{-\frac{n}{2}} e^{-\frac{n\theta^2}{2} + n\theta\bar{x}} \cdot e^{-\frac{1}{2} \sum x_i^2}.
   \]
   这里 \(t(\boldsymbol{x}) = \bar{x}\)，\(g(t; \theta) = e^{-\frac{n\theta^2}{2} + n\theta\bar{x}}\)，\(h(\boldsymbol{x}) = (2\pi)^{-\frac{n}{2}} e^{-\frac{1}{2} \sum x_i^2}\)。

3. **均匀分布**  
   设 \(\boldsymbol{X} \stackrel{\text{i.i.d.}}{\sim} U(0, \theta)\)，则：
   \[
   f(\boldsymbol{x}; \theta) = \frac{1}{\theta^n} I(0 < x_i < \theta, \ \forall i) = \frac{1}{\theta^n} I(x_{(n)} < \theta) \cdot I(x_{(1)} > 0).
   \]
   其中 \(t(\boldsymbol{x}) = x_{(n)} = \max\{x_1,\dots,x_n\}\) 是充分统计量 \(T(\boldsymbol{X})\) 的观测值。

---

### 2.3.3 极小充分统计量 (Minimal Sufficient Statistic)

- 充分统计量**不唯一**。例如，在正态样本 \(N(\theta, 1)\) 中，\(T_1(\boldsymbol{X}) = \bar{X}\) 和 \(T_2(\boldsymbol{X}) = (\sum_{i=1}^{m} X_i, \sum_{i=m+1}^n X_i)\) (\(1 < m < n\)) 都是充分统计量，但前者更简单。

**定义 9 (极小充分统计量).** 如果一个充分统计量 \(T(\boldsymbol{X})\) 可以表示为任何其他充分统计量的函数，则称 \(T(\boldsymbol{X})\) 为**极小充分统计量**。

---

### 2.3.4 完全统计量 (Complete Statistic)

**定义 10 (完全统计量).** 设 \(T = T(\boldsymbol{X})\) 是一个统计量。如果对于任意可测函数 \(\varphi\)，满足：
\[
E_\theta[\varphi(T)] = 0, \quad \forall \theta \in \Theta
\]
都有：
\[
P_\theta(\varphi(T) = 0) = 1, \quad \forall \theta \in \Theta,
\]
则称 \(T(\boldsymbol{X})\) 是 \(\theta\) 的**完全统计量**。

**注记**：若 \(T\) 的密度为 \(g(t; \theta)\)，则完全性等价于：从 \(\int \varphi(t) g(t; \theta) dt = 0 \ (\forall \theta)\) 可推出 \(\varphi(t) = 0\) 几乎处处成立。这意味着密度函数族 \(\{g(t; \theta): \theta \in \Theta\}\) 在 \(L^1\) 意义下是完备的。

#### 例子
1. **伯努利分布**：\(T = \sum X_i \sim B(n, \theta)\) 是完全统计量。
2. **正态分布 \(N(\theta, 1)\)**：\(T = \bar{X}\) 是完全统计量。
3. **均匀分布 \(U(0, \theta)\)**：\(T = X_{(n)}\) 是完全统计量。

---

### 2.3.5 有界完全统计量 (Bounded Complete Statistic)

**定义 11 (有界完全统计量).** 若定义 10 中的 \(\varphi\) 仅限定为**有界函数**时结论成立，则称 \(T(\boldsymbol{X})\) 是**有界完全统计量**。

完全性蕴含了有界完全性，反之不一定成立。

---

### 2.3.6 指数族中的完全性定理

**定理 7 (指数族的完全性).** 设 \(\boldsymbol{X}\) 来自指数族，其联合密度为：
\[
f(\boldsymbol{x}; \boldsymbol{\theta}) = C(\boldsymbol{\theta}) \exp\left\{ \sum_{i=1}^k \theta_i T_i(\boldsymbol{x}) \right\} h(\boldsymbol{x}), \quad \boldsymbol{\theta} = (\theta_1, \dots, \theta_k) \in \Theta^*,
\]
并令 \(T(\boldsymbol{X}) = (T_1(\boldsymbol{X}), \dots, T_k(\boldsymbol{X}))\)。如果自然参数空间 \(\Theta^* \subset \mathbb{R}^k\) 含有内点，则 \(T(\boldsymbol{X})\) 是完全统计量。

---

### 2.3.7 Basu 定理 (Basu's Theorem)

**定理 8 (Basu).** 若 \(T(\boldsymbol{X})\) 是有界完全的充分统计量，而另一个统计量 \(V(\boldsymbol{X})\) 的分布与 \(\theta\) 无关，则 \(T(\boldsymbol{X})\) 和 \(V(\boldsymbol{X})\) 相互独立。

#### 例子：正态分布中的独立性
设 \(\boldsymbol{X} \stackrel{\text{i.i.d.}}{\sim} N(\theta, 1)\)，则：
- \(T(\boldsymbol{X}) = \bar{X}\) 是有界完全的充分统计量。
- \(V(\boldsymbol{X}) = X_{(n)} - X_{(1)}\)（样本极差）的分布与 \(\theta\) 无关（因为 \(Y_i = X_i - \theta \sim N(0,1)\)，其极差不依赖于 \(\theta\)）。

由 Basu 定理，\(\bar{X}\) 与样本极差 \(V(\boldsymbol{X})\) 独立。
