## 7.1 随机向量函数的分布

### 7.1.1 三大统计分布

#### 卡方分布（$\chi^2$分布）
- **定义**：$X \sim \chi_v^2$ 的密度函数为：
  $$
  f(x) = \frac{1}{2^{v/2}\Gamma(v/2)} x^{\frac{v}{2}-1} e^{-\frac{x}{2}}, \quad x \geq 0
  $$
- **性质**：
  - 若 $Z_1, ..., Z_n \overset{\text{i.i.d}}{\sim} N(0,1)$，则 $\sum_{i=1}^n Z_i^2 \sim \chi_n^2$
  - $\chi_n^2 = \Gamma\left(\frac{n}{2}, \frac{1}{2}\right)$

#### Student's t分布
- **定义**：$X \sim t_v$ 的密度函数为：
  $$
  f(x) = \frac{\Gamma\left(\frac{v+1}{2}\right)}{\sqrt{v\pi}\Gamma\left(\frac{v}{2}\right)} \left(1 + \frac{x^2}{v}\right)^{-\frac{v+1}{2}}, \quad x \in \mathbb{R}
  $$
- **性质**：
  - 若 $Z \sim N(0,1)$，$X \sim \chi_n^2$ 且独立，则 $T = \frac{Z}{\sqrt{X/n}} \sim t_n$
  - 对称分布，比正态分布重尾
  - $v=1$ 时为 Cauchy 分布

#### F分布
- **定义**：$X \sim F(m,n)$ 的密度函数为：
  $$
  f(x) = \frac{\Gamma\left(\frac{m+n}{2}\right) m^{m/2} n^{n/2} x^{\frac{m}{2}-1}}{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right) (mx+n)^{\frac{m+n}{2}}}, \quad x \geq 0
  $$
- **性质**：
  - 若 $X \sim \chi_m^2$，$Y \sim \chi_n^2$ 且独立，则 $F = \frac{X/m}{Y/n} \sim F(m,n)$

### 7.1.2 一般方法：直接求分布

**基本思路**：
1. 求 $Z = g(X,Y)$ 的 CDF：$F_Z(z) = \mathbb{P}(g(X,Y) \leq z)$
2. 对 CDF 求导得 PDF

### 7.1.3 特殊情形

#### 和的分布：$Z = X + Y$
- **离散型**：
  $$
  \mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x, Y = z - x)
  $$
  独立时：$\mathbb{P}(Z = z) = \sum_x \mathbb{P}(X = x)\mathbb{P}(Y = z - x)$
- **连续型**：
  $$
  f_Z(z) = \int_{-\infty}^{\infty} f(x, z - x) dx
  $$
  独立时：$f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z - x) dx$

#### 差的分布：$V = X - Y$
- **连续型**：
  $$
  f_V(v) = \int_{-\infty}^{\infty} f(x, x - v) dx
  $$

**例子**  
设 $X_1, X_2, \dots, X_n$ 独立同分布，且服从 $\mathcal{U}(-1, 1)$。则：

1. **$X_1 + X_2$ 的密度函数**为：  
$$
f_{X_1 + X_2}(x) = 
\begin{cases} 
\dfrac{2 - |x|}{4}, & |x| \leq 2, \\
0, & |x| > 2.
\end{cases}
$$

2. **$X_1 + X_2 + X_3$ 的密度函数**为：  
$$
f_{X_1 + X_2 + X_3}(x) =
\begin{cases} 
\dfrac{(3 - |x|)^2}{16}, & 1 \leq |x| \leq 3, \\
\dfrac{3 - x^2}{8}, & 0 \leq |x| \leq 1, \\
0, & |x| > 3.
\end{cases}
$$

3. **$S_n = X_1 + X_2 + \cdots + X_n$ 的密度函数**为：  
$$
f_{S_n}(x) =
\begin{cases} 
\dfrac{1}{2^n(n-1)!}
\sum_{k=0}^{\lfloor \frac{n+x}{2} \rfloor} (-1)^k \binom{n}{k} (n+x-2k)^{n-1}, & |x| \leq n, \\
0, & |x| > n.
\end{cases}
$$
此处 $\lfloor a \rfloor$ 表示 $a$ 的整数部分。

### 7.1.4 多个函数的联合密度

**定理**：设 $(X, Y)$ 有联合密度函数 $f(x, y)$，令  
$$
U = u(X, Y), \quad V = v(X, Y)
$$
为 $(X, Y)$ 的变换。设 $D \subset \mathbb{R}^2$ 满足 $\mathbb{P}\big( (U, V) \in D \big) = 1$。  

若存在 $D$ 上的函数组  
$$
x_i = x_i(u, v), \quad y_i = y_i(u, v), \quad i = 1, 2, \dots, n
$$
使得以下条件成立：  

1. 对任意 $(u, v) \in D$，事件  
   $$
   \{ U = u, \, V = v \} = \bigcup_{i=1}^n \{ X = x_i(u,v), \, Y = y_i(u,v) \}
   $$
   即 $(u, v)$ 由 $n$ 个不同的 $(x_i, y_i)$ 变换而来；  

2. 每个变换 $\Delta_i: (u, v) \mapsto (x_i, y_i)$ 是 $D \to D_i$ 的可逆映射，其中 $D_i$ 是 $\Delta_i(D)$，且 $x_i(u,v), y_i(u,v)$ 在 $D$ 上连续可微，并且雅可比行列式  
   $$
   J_i(u,v) = \frac{\partial(x_i, y_i)}{\partial(u, v)} \neq 0, \quad \forall (u,v) \in D;
   $$

3. 值域区域 $D_1, D_2, \dots, D_n$ 互不相交。  

则 $(U, V)$ 的联合密度函数为  
$$
g(u, v) =
\begin{cases}
\displaystyle
\sum_{i=1}^n f\big( x_i(u,v), \, y_i(u,v) \big) \, \left| J_i(u,v) \right|, & (u, v) \in D, \\
0, & (u, v) \notin D.
\end{cases}
$$

**雅可比行列式**：
$$
\left| \frac{\partial(x,y)}{\partial(u,v)} \right| = \left| \begin{matrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{matrix} \right|
$$

**重要应用**：
- 极坐标变换：$X = R\cos\Theta$, $Y = R\sin\Theta$
- Box-Muller 方法生成正态随机变量

## 7.2 次序统计量

### 7.2.1 定义
设 $X_1, ..., X_n$ 为随机变量，将其观测值从小到大排列：
$$
X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}
$$
称 $X_{(1)}, ..., X_{(n)}$ 为次序统计量。

### 7.2.2 分布性质

#### 联合密度
若 $X_1, ..., X_n \overset{\text{i.i.d}}{\sim} f(x)$，则：
$$
g(x_1, ..., x_n) = 
\begin{cases}
n! \prod_{i=1}^n f(x_i), & x_1 < \cdots < x_n \\
0, & \text{其他}
\end{cases}
$$

#### 第k个次序统计量的密度
$$
g_k(x) = n \binom{n-1}{k-1} [F(x)]^{k-1} [1-F(x)]^{n-k} f(x)
$$

#### 第k₁和k₂个次序统计量的联合密度（$k_1 < k_2$）
$$
g(x_{k_1}, x_{k_2}) = \frac{n!}{(k_1-1)!(k_2-k_1-1)!(n-k_2)!} \times [F(x_{k_1})]^{k_1-1} [F(x_{k_2})-F(x_{k_1})]^{k_2-k_1-1} [1-F(x_{k_2})]^{n-k_2} f(x_{k_1}) f(x_{k_2})
$$

### 7.2.3 应用实例
- **最小值分布**：$X_{(1)} = \min\{X_1, ..., X_n\}$
- **最大值分布**：$X_{(n)} = \max\{X_1, ..., X_n\}$
- **灯泡寿命问题**：灯泡数量增加会缩短首次故障时间

### 7.2.4 Beta分布
- **定义**：$X \sim Beta(\alpha, \beta)$ 的密度为：
  $$
  f(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1}, \quad 0 < x < 1
  $$
  其中 $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$
- **特例**：
  - $\alpha = \beta = 1$：均匀分布
  - 与次序统计量的关系：均匀分布的次序统计量服从 Beta 分布

## 7.3 随机变量的p分位数

### 7.3.1 定义
设 $X$ 的分布函数为 $F(x)$，对 $p \in (0,1)$，p分位数定义为：
$$
\xi_p = F^{-1}(p) = \inf\{x | F(x) \geq p\}
$$
特别地，$\xi_{0.5}$ 称为中位数。

### 7.3.2 性质
1. **单调性**：$F^{-1}(p)$ 关于 $p$ 单调非降
2. **不等式**：$F^{-1}(F(x)) \leq x$
3. **下界**：$F(F^{-1}(p)) \geq p$
4. **等价条件**：$F^{-1}(p) \leq t \Leftrightarrow p \leq F(t)$
5. **左连续性**：$F^{-1}(p)$ 左连续
6. **连续性情形**：若 $F$ 连续，则 $F(F^{-1}(p)) = p$

### 7.3.3 随机变量生成
**定理**：若 $U \sim U(0,1)$，$F$ 为连续分布函数，则：
$$
Y = F^{-1}(U) \sim F
$$

**应用**：
- 指数分布：$X = -\lambda^{-1} \ln(1-U)$
- 正态分布：Box-Muller 方法
- 经验分布：从观测值中等概率抽样

## 小结

### 核心知识点
- **三大统计分布**：$\chi^2$、t、F分布的定义、性质及与正态分布的关系
- **随机向量函数的分布**：
  - 一般方法：通过CDF求分布
  - 特殊情形：和、差分布的卷积公式
  - 多函数变换：雅可比行列式方法
- **次序统计量**：
  - 定义和排序概念
  - 单个和多个次序统计量的分布密度
  - 与Beta分布的关系
- **p分位数**：
  - 正式定义和性质
  - 在统计推断和随机数生成中的应用

### 关键公式
- 和的分布：$f_Z(z) = \int_{-\infty}^{\infty} f(x, z-x) dx$
- 次序统计量密度：$g_k(x) = n \binom{n-1}{k-1} [F(x)]^{k-1} [1-F(x)]^{n-k} f(x)$
- p分位数：$\xi_p = F^{-1}(p) = \inf\{x | F(x) \geq p\}$
- 随机变量生成：$Y = F^{-1}(U)$，其中 $U \sim U(0,1)$

### 应用技巧
- **分布推导**：根据问题特点选择CDF法或直接变换法
- **雅可比变换**：用于坐标变换和多函数联合密度推导
- **次序统计量**：理解极端值分布和系统可靠性分析
- **分位数应用**：统计检验中的临界值确定和随机数生成
