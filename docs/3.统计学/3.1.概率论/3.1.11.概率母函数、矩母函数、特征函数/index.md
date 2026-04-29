## 11.1 概率母函数

### 11.1.1 定义

设 $X$ 是取非负整值的随机变量，称
$$
g(s) = E(s^X) = \sum_{j=0}^{\infty} s^j P(X = j), \quad s \in [-1,1]
$$
为 $X$ 的概率母函数，约定 $0^0 = 1$。

### 11.1.2 性质

设 $g(s)$ 是 $X$ 的概率母函数，$g^{(k)}(s)$ 是 $g(s)$ 的 $k$-阶导数，则：

1. 
$$
g(s) = E(s^X) = \sum_{j=0}^{\infty} s^j \mathbb{P}(X = j), \quad s \in [-1,1]
$$

$$
\mathbb{P}(X = k) = \frac{g^{(k)}(0)}{k!}, \quad k = 0, 1, \ldots
$$

2. 
$$
E(X) = g^{(1)}(1)
$$

3. 如果 $E(X) < \infty$，则
$$
var(X) = g^{(2)}(1) + g^{(1)}(1) - [g^{(1)}(1)]^2
$$

4. 如果 $X_1, \ldots, X_n$ 相互独立，则 $Y = X_1 + \cdots + X_n$ 的概率母函数为
$$
g_Y(s) = g_1(s)g_2(s)\cdots g_n(s), \quad s \in [-1,1]
$$

### 11.1.3 常见分布的概率母函数

- 二项分布 $B(n, p)$：
$$
g(s) = (q + sp)^n, \quad q = 1-p
$$

- Poisson分布 $P(\lambda)$：
$$
g(s) = e^{\lambda(s-1)}
$$

- 几何分布 $G(p)$：
$$
g(s) = \frac{sp}{1-sq}, \quad q = 1-p
$$

### 11.1.4 随机个随机变量之和

设 $\{X_j\}$ 是独立同分布的非负整值随机变量，$N$ 为取正整值的随机变量，且与 $\{X_j\}$ 独立，则
$$
W = X_1 + X_2 + \cdots + X_N
$$
的概率母函数为
$$
g_W(s) = g_N[g_X(s)]
$$

## 11.2 矩母函数

### 11.2.1 定义

设 $X$ 是随机变量，称
$$
M_X(s) = E(e^{sX})
$$
为 $X$ 的矩母函数。

- 离散型：
$$
M_X(s) = \sum_j e^{sx_j} \mathbb{P}(X = x_j)
$$

- 连续型：
$$
M_X(s) = \int_{-\infty}^{\infty} e^{sx} f_X(x) dx
$$

### 11.2.2 性质

设 $M(s)$ 是 $X$ 的矩母函数，则：

1. $Y = aX + b$ 的矩母函数为
$$
M_Y(s) = e^{sb} M(sa)
$$

2. 
$$
EX^k = M^{(k)}(0), \quad k = 1, 2, \ldots, n
$$
3. 可逆性：如果存在正数 $a$，使得对任意 $s \in [-a, a]$ 有 $M(s) < \infty$，则 $M(s)$ 唯一决定 $X$ 的分布

4. 如果 $X_1, \ldots, X_n$ 相互独立，则 $Y = X_1 + \cdots + X_n$ 的矩母函数为
$$
M_Y(s) = M_{X_1}(s) \cdots M_{X_n}(s)
$$
### 11.2.3 常见分布的矩母函数

- 指数分布 $\mathcal{E}(\lambda)$：
$$
M(s) = \frac{\lambda}{\lambda - s}, \quad s < \lambda
$$
- 正态分布 $N(\mu, \sigma^2)$：
$$
M(s) = e^{\mu s + \frac{\sigma^2 s^2}{2}}
$$
### 11.2.4 随机个随机变量之和

设 $\{X_j\}$ 独立同分布，$N$ 为取正整值的随机变量且与 $\{X_j\}$ 独立，则
$$
W = X_1 + \cdots + X_N
$$
的矩母函数为
$$
M_W(s) = E[(M_X(s))^N]
$$
## 11.3 特征函数

### 11.3.1 定义

对随机变量 $X$，称
$$
\phi(t) = E(e^{itX}) = E \cos(tX) + iE \sin(tX), \quad t \in \mathbb{R}
$$
为 $X$ 的特征函数，其中 $i = \sqrt{-1}$。

### 11.3.2 性质

设 $\phi(t) = E(e^{itX})$，则：

1. 
$$
|\phi(t)| \leq \phi(0) = 1, \quad \phi(-t) = \overline{\phi(t)}
$$
2. $\phi(t)$ 在 $(-\infty, \infty)$ 上一致连续

3. 如果 $E(|X|^k) < \infty$，则
$$
\phi^{(k)}(t) = i^k E(X^k e^{itX}), \quad \phi^{(k)}(0) = i^k E(X^k)
$$
4. 对任意常数 $a, b$，有
$$
\phi_{aX+b}(t) = e^{itb} \phi_X(at)
$$
5. 如果 $X_1, \ldots, X_n$ 相互独立，则 $Y = X_1 + \cdots + X_n$ 的特征函数为
$$
\phi_Y(t) = \prod_{k=1}^n \phi_k(t)
$$
### 11.3.3 常见分布的特征函数

- 二项分布 $B(n, p)$：
$$
\phi(t) = (q + pe^{it})^n
$$
- Poisson分布 $\mathcal{P}(\lambda)$：
$$
\phi(t) = e^{\lambda(e^{it}-1)}
$$
- 几何分布 $G(p)$：
$$
\phi(t) = \frac{pe^{it}}{1 - qe^{it}}
$$
- 均匀分布 $U(a, b)$：
$$
\phi(t) = \frac{e^{itb} - e^{ita}}{it(b-a)}
$$
- 指数分布 $\mathcal{E}(\lambda)$：
$$
\phi(t) = \left(1 - \frac{it}{\lambda}\right)^{-1}
$$
- 正态分布 $N(\mu, \sigma^2)$：
$$
\phi(t) = \exp\left(i\mu t - \frac{1}{2} \sigma^2 t^2\right)
$$
- Cauchy分布：
$$
\phi(t) = e^{-|t|}
$$
### 11.3.4 特征函数与分布函数

- 随机变量的特征函数和分布函数相互唯一决定
- 逆转公式：如果 $F(x)$ 在 $a, b$ 连续，则
$$
\frac{1}{2\pi} \lim_{T \to \infty} \int_{-T}^{T} \frac{e^{-ita} - e^{-itb}}{it} \phi(t) dt = F(b) - F(a)
$$
### 11.3.5 特征函数与独立性

设 $X = (X_1, \ldots, X_n)$ 是随机向量，则 $X_1, \ldots, X_n$ 相互独立的充要条件是
$$
\phi(t) = \phi_1(t_1) \phi_2(t_2) \cdots \phi_n(t_n)
$$
### 11.3.6 特征函数与收敛性

- 连续性定理：$X_n$ 依分布收敛到 $X$ 的充分必要条件是
$$
\lim_{n \to \infty} \phi_n(t) = \phi(t), \quad \forall t \in \mathbb{R}
$$

## 小结

### 核心知识点

- 概率母函数、矩母函数、特征函数的定义与性质
- 三种母函数在计算概率、矩、确定分布等方面的应用
- 随机个随机变量之和的分布求解
- 特征函数在独立性判定和收敛性分析中的应用

### 关键公式对比

| 分布                   | 概率母函数         | 矩母函数                             | 特征函数                                |
| ---------------------- | ------------------ | ------------------------------------ | --------------------------------------- |
| $B(n, p)$              | $(q + ps)^n$       | $(q + pe^s)^n$                       | $(q + pe^{it})^n$                       |
| $\mathcal{P}(\lambda)$ | $e^{\lambda(s-1)}$ | $e^{\lambda(e^s-1)}$                 | $e^{\lambda(e^{it}-1)}$                 |
| $G(p)$                 | $\frac{sp}{1-sq}$  | -                                    | $\frac{pe^{it}}{1 - qe^{it}}$           |
| $\mathcal{E}(\lambda)$ | -                  | $\frac{\lambda}{\lambda-s}$          | $(1 - \frac{it}{\lambda})^{-1}$         |
| $N(\mu, \sigma^2)$     | -                  | $e^{\mu s + \frac{\sigma^2 s^2}{2}}$ | $e^{i\mu t - \frac{1}{2} \sigma^2 t^2}$ |

### 应用技巧

- 根据随机变量类型选择最合适的母函数工具
- 利用Taylor展开/级数展开计算矩
- 利用可逆性由母函数确定分布
- 利用乘积性质处理独立随机变量之和
