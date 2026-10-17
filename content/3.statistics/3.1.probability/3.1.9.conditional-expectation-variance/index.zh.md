---
title: 条件期望、条件方差
---

上一章用期望概括一个随机变量。如果已经获得了部分信息——例如知道某事件 $A$ 已经发生，或者测得了另一个随机变量 $Y$ 的值——就应当用条件分布代替无条件分布来计算平均值，这就是条件期望。例如已知一个人的足长，推测他的平均身高；已知某人能翻过一堵墙，推测他的平均身高。本章先回顾条件概率在事件与随机变量上的各种形式（乘法公式、全概率公式、贝叶斯公式），然后定义给定事件的条件期望 $\mathbb{E}(X \mid A)$ 与给定随机变量的条件期望 $\mathbb{E}(X \mid Y)$。后者本身是一个随机变量，它满足重期望公式 $\mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}X$，这一公式在有层次结构的模型中能大大简化计算；它还是在均方误差意义下用 $Y$ 预测 $X$ 的最佳预测。最后定义条件方差并证明全方差公式。本章用到 [3.1.6](/3.1.6) 的条件分布与 [3.1.8](/3.1.8) 的期望；条件期望的思想贯穿统计学，例如线性回归（[3.3](/3.3)）、Rao–Blackwell 定理（[3.2.3](/3.2.3)）与 EM 算法。

## 9.1. 条件概率回顾

条件概率已经以几种形式出现过：给定事件的条件概率 $\mathbb{P}(A \mid B)$（[3.1.2](/3.1.2)）、给定事件的随机变量的条件分布 $\mathbb{P}(X \in \cdot \mid A)$，以及给定随机变量的条件分布（[3.1.6](/3.1.6)）。设 $\mathbb{P}(A) > 0$，给定 $A$ 时 $X$ 的条件分布列为 $p_{X|A}(x) = \mathbb{P}(\{X = x\} \cap A)/\mathbb{P}(A)$；连续型时若存在 $f_{X|A} \ge 0$ 使 $\mathbb{P}(X \in B \mid A) = \int_B f_{X|A}(x)\,\mathrm{d}x$ 对一切 Borel 集 $B$ 成立，称 $f_{X|A}$ 为给定 $A$ 时 $X$ 的条件密度。特别地，$A = \{X \in C\}$ 时 $f_{X|A}(x) = f_X(x)\boldsymbol{1}_C(x)/\mathbb{P}(X \in C)$。

三条基本法则在各种形式下完全平行（设 $A_1, \dots, A_n$ 是 $\Omega$ 的一个分割，所涉及的条件概率有定义）：

| | 事件 | $X$ 给定事件 | $X$ 给定随机变量 $Y$ |
|---|---|---|---|
| 乘法公式 | $\mathbb{P}(A \cap B) = \mathbb{P}(B)\mathbb{P}(A \mid B)$ | $\mathbb{P}(\{X = x\} \cap A) = \mathbb{P}(A)p_{X\mid A}(x)$；$f_X(x)\boldsymbol{1}_C(x) = \mathbb{P}(X \in C)f_{X\mid\{X\in C\}}(x)$ | $p_{X,Y}(x, y) = p_Y(y)p_{X\mid Y}(x \mid y)$；$f(x, y) = f_Y(y)f_{X\mid Y}(x \mid y)$ |
| 全概率公式 | $\mathbb{P}(B) = \sum_i \mathbb{P}(A_i)\mathbb{P}(B \mid A_i)$ | $p_X(x) = \sum_i \mathbb{P}(A_i)p_{X\mid A_i}(x)$；$f_X(x) = \sum_i \mathbb{P}(A_i)f_{X\mid A_i}(x)$ | $p_X(x) = \sum_y p_Y(y)p_{X\mid Y}(x \mid y)$；$f_X(x) = \int f_Y(y)f_{X\mid Y}(x \mid y)\,\mathrm{d}y$ |
| 贝叶斯公式 | $\mathbb{P}(A_i \mid B) = \dfrac{\mathbb{P}(A_i)\mathbb{P}(B \mid A_i)}{\sum_j \mathbb{P}(A_j)\mathbb{P}(B \mid A_j)}$ | 类似 | 见下 |

给定随机变量的贝叶斯公式按 $X, Y$ 是离散型还是连续型分为四种情形，形式相同，只是分布列与密度互换：

1. $X, Y$ 都离散：$p_{X|Y}(x \mid y) = \dfrac{p_X(x)p_{Y|X}(y \mid x)}{p_Y(y)}$，$p_Y(y) = \sum_x p_X(x)p_{Y|X}(y \mid x)$。例：$X \in \{0, 1\}$ 表示飞机是否出现，$Y \in \{0, 1\}$ 表示雷达是否报警。
2. $X, Y$ 都连续：$f_{X|Y}(x \mid y) = \dfrac{f_X(x)f_{Y|X}(y \mid x)}{f_Y(y)}$，$f_Y(y) = \int f_X(x)f_{Y|X}(y \mid x)\,\mathrm{d}x$。例：$X$ 是连续的信号，$Y$ 是含有测量误差的观测，$f_{Y|X}$ 是噪声模型。
3. $X$ 离散、$Y$ 连续：$p_{X|Y}(x \mid y) = \dfrac{p_X(x)f_{Y|X}(y \mid x)}{f_Y(y)}$，$f_Y(y) = \sum_x p_X(x)f_{Y|X}(y \mid x)$。例：$X$ 表示是否患某种疾病，$Y$ 是血液中白细胞的浓度。
4. $X$ 连续、$Y$ 离散：$f_{X|Y}(x \mid y) = \dfrac{f_X(x)p_{Y|X}(y \mid x)}{p_Y(y)}$，$p_Y(y) = \int f_X(x)p_{Y|X}(y \mid x)\,\mathrm{d}x$。例：$X$ 是身高，$Y$ 是鞋码。

**例 9.1.1** 一台有缺陷的造币机造出的硬币正面朝上的概率是随机变量 $P$，密度为 $f_P(p) = p\mathrm{e}^p$（$0 \le p \le 1$）。取一枚这样造出的硬币反复独立地抛掷。求：(1) 一次抛掷得到正面的概率；(2) 已知第一次得到正面时 $P$ 的条件密度；(3) 已知第一次得到正面时第二次也得到正面的概率。

**解** 记 $A$、$B$ 分别为第一、二次得到正面。已知 $P = p$ 时各次抛掷独立，正面概率为 $p$。

(1) 由全概率公式（情形 4），$\mathbb{P}(A) = \int_0^1 p \cdot p\mathrm{e}^p\,\mathrm{d}p = \big[\mathrm{e}^p(p^2 - 2p + 2)\big]_0^1 = \mathrm{e} - 2 \approx 0.718$。

(2) 由贝叶斯公式，$f_{P|A}(p) = \dfrac{f_P(p)\mathbb{P}(A \mid P = p)}{\mathbb{P}(A)} = \dfrac{p^2\mathrm{e}^p}{\mathrm{e} - 2}$，$0 \le p \le 1$。

(3) 在条件概率 $\mathbb{P}(\cdot \mid A)$ 下再用全概率公式，$P$ 的分布换成 (2) 中的后验分布：

$$
\mathbb{P}(B \mid A) = \int_0^1 \mathbb{P}(B \mid P = p, A)f_{P|A}(p)\,\mathrm{d}p = \int_0^1 p\cdot\frac{p^2\mathrm{e}^p}{\mathrm{e} - 2}\,\mathrm{d}p = \frac{6 - 2\mathrm{e}}{\mathrm{e} - 2} \approx 0.784.
$$
它大于 $\mathbb{P}(B) = \mathrm{e} - 2$：两次抛掷在给定 $P$ 时独立，但无条件地不独立，第一次的正面提高了对 $P$ 的估计。

## 9.2. 给定事件的条件期望

### 9.2.1. 定义与计算

把期望定义中的分布换成给定 $A$ 的条件分布，就得到给定 $A$ 的条件期望，它是在概率 $\mathbb{P}_A(\cdot) = \mathbb{P}(\cdot \mid A)$ 下 $X$ 的期望。

**定义 9.2.1** 设 $\mathbb{P}(A) > 0$。离散型时，若 $\sum_i \lvert x_i \rvert\mathbb{P}(X = x_i \mid A) < \infty$，定义给定 $A$ 发生时 $X$ 的条件期望

$$
\mathbb{E}(X \mid A) = \sum_i x_i\,\mathbb{P}(X = x_i \mid A);
$$
连续型时，若 $\int \lvert x \rvert f_{X|A}(x)\,\mathrm{d}x < \infty$，定义 $\mathbb{E}(X \mid A) = \int_{-\infty}^{\infty} x f_{X|A}(x)\,\mathrm{d}x$。

**定理 9.2.1** 设 $\mathbb{P}(A) > 0$，$\mathbb{E}(X \mid A)$ 存在，则

$$
\mathbb{E}(X \mid A) = \frac{\mathbb{E}(X\boldsymbol{1}_A)}{\mathbb{P}(A)}.
$$

**证明** 先设 $X \ge 0$。$\mathbb{E}(X \mid A)$ 是在概率 $\mathbb{P}_A$ 下 $X$ 的期望，由定理 8.2.3，

$$
\mathbb{E}(X \mid A) = \int_0^{\infty}\mathbb{P}(X > x \mid A)\,\mathrm{d}x = \frac{1}{\mathbb{P}(A)}\int_0^{\infty}\mathbb{P}(\{X > x\} \cap A)\,\mathrm{d}x = \frac{1}{\mathbb{P}(A)}\int_0^{\infty}\mathbb{P}(X\boldsymbol{1}_A > x)\,\mathrm{d}x = \frac{\mathbb{E}(X\boldsymbol{1}_A)}{\mathbb{P}(A)},
$$
其中用到 $x \ge 0$ 时 $\{X > x\} \cap A = \{X\boldsymbol{1}_A > x\}$。一般情形把 $X$ 分解为正部与负部 $X = X^+ - X^-$，$X^+ = X\boldsymbol{1}\{X \ge 0\}$，$X^- = -X\boldsymbol{1}\{X < 0\}$，分别应用上式再相减。 $\square$

所以条件期望可以由无条件期望算出，不必先求条件分布。

**例 9.2.1** 设 $X \sim \mathrm{Exp}(\lambda)$，$a > 0$，则 $\mathbb{E}(X \mid X > a) = a + \frac{1}{\lambda}$。

**证明** 由定理 9.2.1 并分部积分，

$$
\mathbb{E}(X \mid X > a) = \frac{\mathbb{E}(X\boldsymbol{1}\{X > a\})}{\mathbb{P}(X > a)} = \mathrm{e}^{\lambda a}\int_a^{\infty} x\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \mathrm{e}^{\lambda a}\Big(a + \frac{1}{\lambda}\Big)\mathrm{e}^{-\lambda a} = a + \frac{1}{\lambda}.
$$
也可以由指数分布的无记忆性直接得到：在 $X > a$ 的条件下 $X - a$ 仍服从 $\mathrm{Exp}(\lambda)$，所以 $\mathbb{E}(X \mid X > a) = a + \mathbb{E}(X - a \mid X > a) = a + \frac{1}{\lambda}$。 $\square$

**例 9.2.2** 设 $X \sim \mathrm{Exp}(\lambda)$ 与 $Y \sim \mathrm{Exp}(\mu)$ 独立，计算 $\mathbb{E}(X \mid X < Y)$。

**解** 先对 $y$ 积分，$\mathbb{E}(X\boldsymbol{1}\{X < Y\}) = \int_0^{\infty} x\,\mathbb{P}(Y > x)\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \int_0^{\infty} x\lambda\mathrm{e}^{-(\lambda + \mu)x}\,\mathrm{d}x = \frac{\lambda}{(\lambda + \mu)^2}$，而 $\mathbb{P}(X < Y) = \int_0^{\infty}\mathrm{e}^{-\mu x}\lambda\mathrm{e}^{-\lambda x}\,\mathrm{d}x = \frac{\lambda}{\lambda + \mu}$。由定理 9.2.1，

$$
\mathbb{E}(X \mid X < Y) = \frac{\lambda/(\lambda + \mu)^2}{\lambda/(\lambda + \mu)} = \frac{1}{\lambda + \mu}.
$$
结果恰好是 $\min\{X, Y\} \sim \mathrm{Exp}(\lambda + \mu)$ 的期望：事实上在 $X < Y$ 时 $X = \min\{X, Y\}$，而 $\min\{X, Y\}$ 与事件 $\{X < Y\}$ 独立。

### 9.2.2. 全期望公式

由给定各种情形的条件期望可以"加权平均"出无条件期望，这是全概率公式在期望上的推广。

**定理 9.2.2（全期望公式）** 设 $A_1, \dots, A_n$ 是 $\Omega$ 的一个分割，$\mathbb{P}(A_i) > 0$，$\mathbb{E}\lvert X \rvert < \infty$，则

$$
\mathbb{E}X = \sum_{i=1}^n \mathbb{P}(A_i)\,\mathbb{E}(X \mid A_i).
$$

**证明** 由定理 9.2.1，右端等于 $\sum_i \mathbb{E}(X\boldsymbol{1}_{A_i}) = \mathbb{E}\big(X\sum_i\boldsymbol{1}_{A_i}\big) = \mathbb{E}X$。也可以由全概率公式 $p_X(x) = \sum_i \mathbb{P}(A_i)p_{X|A_i}(x)$ 两边乘 $x$ 后求和、交换求和次序得到。 $\square$

公式对可列分割同样成立。计算全班的平均分，可以先算各小组的平均分，再按各组人数比例加权平均，这就是全期望公式。

**例 9.2.3** 设 $X \sim \mathrm{Geo}(p)$，用全期望公式求 $\mathbb{E}X$。

**解** 取分割 $A_1 = \{X = 1\}$，$A_2 = \{X > 1\}$。由无记忆性，在 $X > 1$ 的条件下 $X - 1$ 仍服从 $\mathrm{Geo}(p)$，故 $\mathbb{E}(X \mid X > 1) = 1 + \mathbb{E}X$。于是

$$
\mathbb{E}X = 1\cdot p + (1 + \mathbb{E}X)(1 - p),
$$
解得 $\mathbb{E}X = 1/p$。这个方法（对第一步的结果取条件）称为首步分析，它常把期望的计算化为解方程。

**例 9.2.4（赌徒输光问题）** 甲有本金 $a$ 元，决心再赢 $b$ 元就停止赌博，输光也必须停止。设甲每局赢的概率为 $\frac{1}{2}$，各局相互独立，每局输赢都是 1 元。求甲停止时平均赌了多少局。

**解** 记 $m_i$ 为甲有 $i$ 元时到停止为止还要赌的平均局数，$m_0 = m_{a+b} = 0$。对第一局的输赢应用全期望公式，$0 < i < a + b$ 时

$$
m_i = \frac{1}{2}(1 + m_{i-1}) + \frac{1}{2}(1 + m_{i+1}),
$$
即二阶差分 $(m_{i+1} - m_i) - (m_i - m_{i-1}) = -2$。所以 $m_i$ 是 $i$ 的二次函数，结合边界条件得 $m_i = i(a + b - i)$，所求平均局数为 $m_a = ab$。（这里默认 $m_i$ 有限，可以用更细致的论证说明这一点。）

## 9.3. 给定随机变量的条件期望

### 9.3.1. 定义

**定义 9.3.1** 离散型时，若 $\sum_i \lvert x_i \rvert\mathbb{P}(X = x_i \mid Y = y) < \infty$，定义给定 $Y = y$ 时 $X$ 的条件期望

$$
\mathbb{E}(X \mid Y = y) = \sum_i x_i\,\mathbb{P}(X = x_i \mid Y = y);
$$
连续型时，若 $\int \lvert x \rvert f_{X|Y}(x \mid y)\,\mathrm{d}x < \infty$，定义 $\mathbb{E}(X \mid Y = y) = \int_{-\infty}^{\infty} x f_{X|Y}(x \mid y)\,\mathrm{d}x$。

$\mathbb{E}(X \mid Y = y)$ 是 $y$ 的函数。把其中的 $y$ 换成随机变量 $Y$，就得到一个新的随机变量。

**定义 9.3.2（条件期望）** 设 $(X, Y)$ 是随机向量，$\mathbb{E}\lvert X \rvert < \infty$，令 $m(y) = \mathbb{E}(X \mid Y = y)$，称随机变量 $m(Y)$ 为给定 $Y$ 时 $X$ 的**条件期望**，记作 $\mathbb{E}(X \mid Y)$。

要计算 $\mathbb{E}(X \mid Y)$，只需把 $Y$ 当作定值 $y$ 计算 $m(y) = \mathbb{E}(X \mid Y = y)$，再把结果中的 $y$ 换成 $Y$。由于 $\mathbb{E}(\cdot \mid Y = y)$ 就是在条件分布下求期望，它具有期望的一切性质（线性性、单调性等）。只要相应的期望有合理的定义，$X, Y$ 不必同为离散型或连续型（参看 §9.1 中贝叶斯公式的四种情形）。$Y$ 也可以是随机向量。

**例 9.3.1** 设 $X, Y$ 独立同分布，都服从 $\mathrm{Poi}(\lambda)$，求 $\mathbb{E}(X + Y \mid X)$ 与 $\mathbb{E}(X \mid X + Y)$。

**解** 给定 $X = x$ 时，由独立性 $Y$ 的条件分布仍是 $\mathrm{Poi}(\lambda)$，所以 $\mathbb{E}(X + Y \mid X = x) = x + \lambda$，$\mathbb{E}(X + Y \mid X) = X + \lambda$。

给定 $X + Y = n$ 时，由 $X + Y \sim \mathrm{Poi}(2\lambda)$，对 $0 \le k \le n$，

$$
\mathbb{P}(X = k \mid X + Y = n) = \frac{\mathbb{P}(X = k)\mathbb{P}(Y = n - k)}{\mathbb{P}(X + Y = n)} = \frac{\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda}\frac{\lambda^{n-k}}{(n-k)!}\mathrm{e}^{-\lambda}}{\frac{(2\lambda)^n}{n!}\mathrm{e}^{-2\lambda}} = \binom{n}{k}\Big(\frac{1}{2}\Big)^n,
$$
即 $X \mid X + Y = n \sim \mathrm{Bin}(n, 1/2)$，$\mathbb{E}(X \mid X + Y = n) = n/2$，所以 $\mathbb{E}(X \mid X + Y) = \frac{X + Y}{2}$。后者也可以由对称性看出：$\mathbb{E}(X \mid X + Y) = \mathbb{E}(Y \mid X + Y)$，两者之和为 $\mathbb{E}(X + Y \mid X + Y) = X + Y$。

**例 9.3.2（身高与足长）** 用 $X, Y$ 分别表示成年人的身高与足长，通常可以设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$，求 $\mathbb{E}(X \mid Y)$。

**解** 由例 6.5.2，给定 $Y = y$ 时 $X \sim \mathcal{N}\big(\mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2), (1 - \rho^2)\sigma_1^2\big)$，于是

$$
\mathbb{E}(X \mid Y = y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2), \qquad \mathbb{E}(X \mid Y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(Y - \mu_2).
$$
测得现场留下的足迹长度 $y$，就可以用 $\mathbb{E}(X \mid Y = y)$ 推算嫌疑人的身高。统计学中的线性回归模型正是基于这种条件期望的思想（[3.3](/3.3)）。

**例 9.3.3** 设 $X, Y$ 独立，都服从 $\mathrm{Exp}(\lambda)$，$Z = X + Y$。求条件密度 $f_{X|Z}(x \mid z)$ 与 $\mathbb{E}(X^2 \mid Z)$。

**解** 对变换 $(x, z) = (x, x + y)$ 应用定理 7.1.4（Jacobi 行列式为 1），$(X, Z)$ 的联合密度为 $f(x, z) = \lambda\mathrm{e}^{-\lambda x}\cdot\lambda\mathrm{e}^{-\lambda(z - x)} = \lambda^2\mathrm{e}^{-\lambda z}$，$0 < x < z$。注意取值范围：联合密度在 $0 < x < z$ 内与 $x$ 无关。$Z \sim \Gamma(2, \lambda)$，$f_Z(z) = \lambda^2 z\mathrm{e}^{-\lambda z}$，所以

$$
f_{X|Z}(x \mid z) = \frac{\lambda^2\mathrm{e}^{-\lambda z}}{\lambda^2 z\mathrm{e}^{-\lambda z}} = \frac{1}{z}, \quad 0 < x < z,
$$
即 $X \mid Z = z \sim \mathrm{U}(0, z)$。于是 $\mathbb{E}(X^2 \mid Z = z) = z^2/3$，$\mathbb{E}(X^2 \mid Z) = Z^2/3$。

### 9.3.2. 重期望公式

条件期望 $\mathbb{E}(X \mid Y)$ 是"按 $Y$ 分组后各组的平均"。例如某人群中足长为 24、25、26 cm 的人分别占 0.1、0.6、0.3，各组的平均身高分别为 165、175、180 cm，则 $\mathbb{E}(X \mid Y)$ 以概率 0.1、0.6、0.3 取值 165、175、180，而全体的平均身高是这些组平均的加权平均 $165 \times 0.1 + 175 \times 0.6 + 180 \times 0.3 = 175.5$ cm。这就是下面的定理。

**定理 9.3.1（重期望公式）** 设 $X, Y$ 是随机变量，$\mathbb{E}\lvert X \rvert < \infty$，则

$$
\mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}X.
$$

**证明** 离散情形：记 $m(y) = \mathbb{E}(X \mid Y = y)$，交换求和次序（绝对收敛保证可交换），

$$
\mathbb{E}[\mathbb{E}(X \mid Y)] = \sum_y m(y)p_Y(y) = \sum_y\Big(\sum_x x\,p_{X|Y}(x \mid y)\Big)p_Y(y) = \sum_x x\sum_y p_{X,Y}(x, y) = \sum_x x\,p_X(x) = \mathbb{E}X.
$$
连续情形把求和换成积分，用 $f_{X|Y}(x \mid y)f_Y(y) = f(x, y)$ 与 Fubini 定理。 $\square$

定理 9.2.2 是 $Y$ 取 $n$ 个值（$Y = i$ 当且仅当 $A_i$ 发生）时的特例，两者统称全期望公式，也称塔性质。它在有层次结构的模型（如贝叶斯网络）中常有简化作用：先在给定上层变量的条件下计算，再对上层变量求平均。

**例 9.3.4（密室逃脱）** 一位玩家在有三个门的密室中迷了路。第一个门通向一条走 3 小时可到达出口的密道；第二个门通向走 5 小时后又回到原地的密道；第三个门通向走 7 小时后又回到原地的密道。他每次都等可能地选择其中一个门（不记得以前走过哪个），求他到达出口平均要花多少时间。

**解** 设 $X$ 为到达出口所需的时间，$Y$ 为他最初选择的门的编号，$\mathbb{P}(Y = i) = \frac{1}{3}$。回到原地后情形与开始时完全相同，所以

$$
\mathbb{E}(X \mid Y = 1) = 3, \quad \mathbb{E}(X \mid Y = 2) = 5 + \mathbb{E}X, \quad \mathbb{E}(X \mid Y = 3) = 7 + \mathbb{E}X.
$$
由全期望公式，$\mathbb{E}X = \frac{1}{3}[3 + (5 + \mathbb{E}X) + (7 + \mathbb{E}X)]$，解得 $\mathbb{E}X = 15$ 小时。

**例 9.3.5** 续例 6.5.3：$Y \sim \Gamma(\alpha, \lambda)$，已知 $Y = y$ 时 $X \sim \mathrm{Exp}(y)$。求 $\mathbb{E}(X \mid Y)$、$\mathbb{E}(Y \mid X)$ 与 $\mathbb{E}X$。

**解** 给定 $Y = y$ 时 $\mathbb{E}(X \mid Y = y) = \int_0^{\infty} x\cdot y\mathrm{e}^{-xy}\,\mathrm{d}x = \frac{1}{y}$，故 $\mathbb{E}(X \mid Y) = \frac{1}{Y}$。

由例 6.5.3，$f_X(x) = \frac{\alpha\lambda^\alpha}{(x + \lambda)^{\alpha+1}}$，于是给定 $X = x$ 时

$$
f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{(x + \lambda)^{\alpha+1}}{\Gamma(\alpha + 1)}y^{\alpha}\mathrm{e}^{-(x + \lambda)y}, \quad y > 0,
$$
这是 $\Gamma(\alpha + 1, x + \lambda)$ 的密度，所以 $\mathbb{E}(Y \mid X = x) = \frac{\alpha + 1}{x + \lambda}$，$\mathbb{E}(Y \mid X) = \frac{\alpha + 1}{X + \lambda}$。这正是贝叶斯推断中的共轭更新：观测到寿命 $x$ 后，环境指标的分布由 $\Gamma(\alpha, \lambda)$ 更新为 $\Gamma(\alpha + 1, \lambda + x)$。

最后，由重期望公式，

$$
\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)] = \mathbb{E}Y^{-1} = \int_0^{\infty}\frac{1}{y}\cdot\frac{\lambda^\alpha}{\Gamma(\alpha)}y^{\alpha-1}\mathrm{e}^{-\lambda y}\,\mathrm{d}y = \begin{cases} \dfrac{\lambda\Gamma(\alpha - 1)}{\Gamma(\alpha)} = \dfrac{\lambda}{\alpha - 1}, & \alpha > 1, \\ \infty, & 0 < \alpha \le 1. \end{cases}
$$
$\alpha \le 1$ 时积分在 $y = 0$ 附近发散。用重期望公式计算比直接对 $f_X$ 积分简便。

### 9.3.3. 条件期望的性质

**定理 9.3.2** 设 $X, Y$ 是随机变量，$g(x)$、$h(y)$ 是实函数，$\mathbb{E}\lvert X \rvert < \infty$，$\mathbb{E}\lvert g(X) \rvert < \infty$，$X_1, \dots, X_n$ 的期望有限，则

1. $\lvert\mathbb{E}(X \mid Y)\rvert \le \mathbb{E}(\lvert X \rvert \mid Y)$；
2. $[\mathbb{E}(X \mid Y)]^2 \le \mathbb{E}(X^2 \mid Y)$；
3. $\mathbb{E}[h(Y)g(X) \mid Y] = h(Y)\,\mathbb{E}[g(X) \mid Y]$（设左端有定义）；
4. $\mathbb{E}[\mathbb{E}(g(X) \mid Y)] = \mathbb{E}g(X)$；
5. 当 $X, Y$ 独立时，$\mathbb{E}[g(X) \mid Y] = \mathbb{E}g(X)$；
6. $\mathbb{E}\big(c + \sum_{i=1}^n c_iX_i \mid Y\big) = c + \sum_{i=1}^n c_i\mathbb{E}(X_i \mid Y)$；
7. 如果 $X_1 \le X_2$，则 $\mathbb{E}(X_1 \mid Y) \le \mathbb{E}(X_2 \mid Y)$。

**证明** 这些等式与不等式都对每个 $y$ 在条件分布下验证。1、2、6、7 是期望的性质 $\lvert\mathbb{E}X\rvert \le \mathbb{E}\lvert X \rvert$、$(\mathbb{E}X)^2 \le \mathbb{E}X^2$（Jensen 不等式）、线性性、单调性在条件分布下的形式。3：给定 $Y = y$ 时 $h(Y) = h(y)$ 是常数，可以提到期望之外。4 是重期望公式应用于 $g(X)$。5：独立时 $X$ 的条件分布等于其无条件分布（定理 6.5.1、6.5.2）。 $\square$

性质 3 说的是：在给定 $Y$ 的条件下，$Y$ 的函数可以当作常数。它与重期望公式结合，常用来计算乘积的期望：$\mathbb{E}[h(Y)X] = \mathbb{E}[h(Y)\mathbb{E}(X \mid Y)]$。

**例 9.3.6** 设 $\mathbb{E}X^2 < \infty$，$\mathbb{E}h^2(Y) < \infty$，则

$$
\mathbb{E}\big[(X - \mathbb{E}(X \mid Y))h(Y)\big] = 0.
$$

**证明** 由 Cauchy–Schwarz 不等式，$\mathbb{E}\lvert Xh(Y) \rvert \le \sqrt{\mathbb{E}X^2\,\mathbb{E}h^2(Y)} < \infty$。由性质 3 与重期望公式，

$$
\mathbb{E}[\mathbb{E}(X \mid Y)h(Y)] = \mathbb{E}[\mathbb{E}(Xh(Y) \mid Y)] = \mathbb{E}[Xh(Y)],
$$
两者相减即得。 $\square$

几何上，把方差有限的随机变量看作向量、$\mathbb{E}(UV)$ 看作内积，所有形如 $h(Y)$ 的随机变量构成一个子空间，例 9.3.6 说明 $X - \mathbb{E}(X \mid Y)$ 与这个子空间正交：$\mathbb{E}(X \mid Y)$ 是 $X$ 在 $Y$ 的函数空间上的**正交投影**。由此得到条件期望最重要的意义。

**定理 9.3.3（最佳预测）** 设 $\mathbb{E}X^2 < \infty$，$m(Y) = \mathbb{E}(X \mid Y)$，则对任何实函数 $g(y)$，

$$
\mathbb{E}[X - m(Y)]^2 \le \mathbb{E}[X - g(Y)]^2,
$$
其中等号成立当且仅当 $g(Y) = m(Y)$ a.s.

**证明** 若 $\mathbb{E}g^2(Y) = \infty$，由不等式 $b^2 \le 2(a - b)^2 + 2a^2$ 得 $\infty = \mathbb{E}g^2(Y) \le 2\mathbb{E}[X - g(Y)]^2 + 2\mathbb{E}X^2$，从而右端为 $\infty$，不等式成立。下设 $\mathbb{E}g^2(Y) < \infty$。由性质 2 与重期望公式，$\mathbb{E}m^2(Y) \le \mathbb{E}X^2 < \infty$，令 $h(Y) = m(Y) - g(Y)$，则 $\mathbb{E}h^2(Y) < \infty$。由例 9.3.6，交叉项为零：

$$
\mathbb{E}[X - g(Y)]^2 = \mathbb{E}[X - m(Y)]^2 + \mathbb{E}[m(Y) - g(Y)]^2 + 2\mathbb{E}\big[(X - m(Y))h(Y)\big] = \mathbb{E}[X - m(Y)]^2 + \mathbb{E}[m(Y) - g(Y)]^2 \ge \mathbb{E}[X - m(Y)]^2.
$$
等号成立当且仅当 $\mathbb{E}[m(Y) - g(Y)]^2 = 0$，即 $g(Y) = m(Y)$ a.s. $\square$

称 $\mathbb{E}(X \mid Y)$ 为用 $Y$ 预测 $X$ 的最佳预测。这是定理 8.2.4（期望是最佳常数预测）的推广：信息 $Y$ 越多，可选的预测函数越多，均方误差越小。证明中"加一项、减一项"凑出零均值的交叉项，是处理二次型期望的常用技巧。

**例 9.3.7** 设 $(X, Y) \sim \mathcal{N}(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$。由例 9.3.2，最佳预测 $\mathbb{E}(X \mid Y) = \mu_1 + \rho\frac{\sigma_1}{\sigma_2}(Y - \mu_2)$ 是 $Y$ 的线性函数，所以对正态分布而言，最佳预测就是最佳线性预测（[3.1.10](/3.1.10)）。一般分布下 $\mathbb{E}(X \mid Y)$ 可以是非线性的，最佳线性预测只是它的一个近似。

![非线性情形：散点为 (Y, X) 的模拟样本，实线为条件期望 E(X | Y = y)，虚线为最佳线性预测](./plots/conditional-mean.py)

**例 9.3.8** 设随机变量 $X, Y$ 的二阶矩有限，且 $\mathbb{E}(X \mid Y) = Y$，$\mathbb{E}(Y \mid X) = X$，则 $X = Y$ a.s.

**证明** 由性质 3 与重期望公式，$\mathbb{E}(XY) = \mathbb{E}[Y\mathbb{E}(X \mid Y)] = \mathbb{E}Y^2$，同理 $\mathbb{E}(XY) = \mathbb{E}X^2$。于是

$$
\mathbb{E}(X - Y)^2 = \mathbb{E}X^2 - 2\mathbb{E}(XY) + \mathbb{E}Y^2 = 0,
$$
由例 8.2.8 得 $X = Y$ a.s. $\square$

## 9.4. 条件方差

### 9.4.1. 定义与全方差公式

**定义 9.4.1（条件方差）** 如果 $\mathbb{E}\big[(X - \mathbb{E}(X \mid Y))^2 \mid Y\big]$ 存在，称它为给定 $Y$ 时 $X$ 的**条件方差**，记作

$$
\operatorname{Var}(X \mid Y) := \mathbb{E}\big[(X - \mathbb{E}(X \mid Y))^2 \mid Y\big].
$$
相应地 $\operatorname{Var}(X \mid Y = y) = \mathbb{E}\big[(X - \mathbb{E}(X \mid Y = y))^2 \mid Y = y\big]$ 是条件分布的方差。

与方差的计算公式一样，$\operatorname{Var}(X \mid Y) = \mathbb{E}(X^2 \mid Y) - [\mathbb{E}(X \mid Y)]^2$。对它和 $\mathbb{E}(X \mid Y)$ 分别取期望与方差：

$$
\mathbb{E}[\operatorname{Var}(X \mid Y)] = \mathbb{E}X^2 - \mathbb{E}[\mathbb{E}(X \mid Y)]^2, \qquad \operatorname{Var}[\mathbb{E}(X \mid Y)] = \mathbb{E}[\mathbb{E}(X \mid Y)]^2 - (\mathbb{E}X)^2,
$$
两式相加，中间项抵消，得到 $\operatorname{Var}(X)$。

**定理 9.4.1（全方差公式）** 设 $\mathbb{E}X^2 < \infty$，则

$$
\operatorname{Var}(X) = \mathbb{E}[\operatorname{Var}(X \mid Y)] + \operatorname{Var}[\mathbb{E}(X \mid Y)].
$$

**证明** 另一种证明：插入 $\mathbb{E}(X \mid Y)$，并注意 $\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)]$，

$$
\operatorname{Var}(X) = \mathbb{E}\big[(X - \mathbb{E}(X \mid Y)) + (\mathbb{E}(X \mid Y) - \mathbb{E}X)\big]^2 = \mathbb{E}[X - \mathbb{E}(X \mid Y)]^2 + \operatorname{Var}[\mathbb{E}(X \mid Y)],
$$
交叉项由例 9.3.6（取 $h(Y) = \mathbb{E}(X \mid Y) - \mathbb{E}X$）为零。最后由重期望公式，$\mathbb{E}[X - \mathbb{E}(X \mid Y)]^2 = \mathbb{E}\big[\mathbb{E}[(X - \mathbb{E}(X \mid Y))^2 \mid Y]\big] = \mathbb{E}[\operatorname{Var}(X \mid Y)]$。 $\square$

总的波动分解为"组内波动的平均"与"组平均之间的波动"两部分。这正是方差分析、线性回归中平方和分解的原型；它也说明 $\operatorname{Var}[\mathbb{E}(X \mid Y)] \le \operatorname{Var}(X)$：用条件期望代替原随机变量，期望不变而方差不增，这是 Rao–Blackwell 定理（[3.2.3](/3.2.3)）的核心。

![全方差公式：三组数据的组内方差的平均加上组均值的方差等于总方差](./plots/total-variance.py)

**例 9.4.1（随机个数随机变量之和）** 设 $Y$ 是某校明年选修概率论课程的学生人数，$X_i$ 是第 $i$ 位同学在此后 5 年内写的论文篇数，$X = X_1 + \cdots + X_Y$ 是这些同学写的论文总数。设 $X_1, X_2, \dots$ 独立同分布，且与 $Y$ 独立，已知 $\mathbb{E}X_1$、$\mathbb{E}Y$、$\operatorname{Var}(X_1)$、$\operatorname{Var}(Y)$，求 $X$ 的期望与方差。

**解** 给定 $Y = n$ 时，由独立性 $X$ 与 $X_1 + \cdots + X_n$ 同分布，

$$
\mathbb{E}(X \mid Y = n) = n\mathbb{E}X_1, \qquad \operatorname{Var}(X \mid Y = n) = n\operatorname{Var}(X_1),
$$
所以 $\mathbb{E}(X \mid Y) = Y\mathbb{E}X_1$，$\operatorname{Var}(X \mid Y) = Y\operatorname{Var}(X_1)$。由重期望公式与全方差公式，

$$
\mathbb{E}X = \mathbb{E}Y\cdot\mathbb{E}X_1, \qquad \operatorname{Var}(X) = \mathbb{E}[Y\operatorname{Var}(X_1)] + \operatorname{Var}(Y\mathbb{E}X_1) = \mathbb{E}Y\cdot\operatorname{Var}(X_1) + (\mathbb{E}X_1)^2\operatorname{Var}(Y).
$$
方差的两项分别来自每个人论文数的随机性和选课人数的随机性。

## 小结

| | 给定事件 $A$ | 给定随机变量 $Y$ |
|---|---|---|
| 定义 | $\mathbb{E}(X \mid A) = \sum x_i\mathbb{P}(X = x_i \mid A)$ 或 $\int x f_{X\mid A}(x)\,\mathrm{d}x$ | $\mathbb{E}(X \mid Y) = m(Y)$，$m(y) = \mathbb{E}(X \mid Y = y)$ |
| 计算 | $\mathbb{E}(X \mid A) = \mathbb{E}(X\boldsymbol{1}_A)/\mathbb{P}(A)$ | 先固定 $Y = y$ 计算，再把 $y$ 换成 $Y$ |
| 由条件到无条件 | $\mathbb{E}X = \sum_i\mathbb{P}(A_i)\mathbb{E}(X \mid A_i)$ | $\mathbb{E}X = \mathbb{E}[\mathbb{E}(X \mid Y)]$ |
| 意义 | 已知 $A$ 发生时的平均 | 用 $Y$ 预测 $X$ 的最佳预测（正交投影） |

- 条件方差 $\operatorname{Var}(X \mid Y) = \mathbb{E}(X^2 \mid Y) - [\mathbb{E}(X \mid Y)]^2$；全方差公式 $\operatorname{Var}(X) = \mathbb{E}[\operatorname{Var}(X \mid Y)] + \operatorname{Var}[\mathbb{E}(X \mid Y)]$。
- 给定 $Y$ 时 $Y$ 的函数可以当作常数：$\mathbb{E}[h(Y)X \mid Y] = h(Y)\mathbb{E}(X \mid Y)$。
- 技巧：首步分析（对第一步取条件、解方程）；利用对称性（如 $\mathbb{E}(X \mid X + Y) = \frac{X + Y}{2}$）；求和或积分换序；在二次型的期望中加一项减一项，凑出零均值的交叉项。
