---
title: 实际溶液：活度与超额函数
---

[6.3.5](/6.3.5) 的两种理想溶液只是极限：理想液态混合物要求各组分分子几乎相同，理想稀溶液要求溶质无限稀。实际溶液在有限浓度下都偏离 Raoult 定律与 Henry 定律，偏离的方向与大小反映了分子间的相互作用。Lewis 的处理办法与对实际气体引入**逸度**（[6.3.4](/6.3.4)）完全平行：保留理想溶液化学势的形式，把浓度换成"有效浓度"——**活度**，偏离理想的程度集中在活度因子中。本章先描述偏差（6.1），再定义活度与活度因子并讨论标准态的选择（6.2），介绍活度的测定（6.3），然后用超额函数描述整个溶液的非理想性，并以单参数的正规溶液模型为例（6.4），最后讨论溶质在两个互不相溶的溶剂之间的分配与萃取（6.5）。活度是 [6.3.7](/6.3.7) 写出一般平衡常数的基础；电解质溶液的活度（平均活度、Debye–Hückel 理论）留到 [6.3.12](/6.3.12)，电动势法测活度见 [6.3.13](/6.3.13)。

## 6.1. 对 Raoult 定律的偏差

实际的液态混合物中，组分的蒸气分压大于 Raoult 定律的预言（$p_{\mathrm{B}} > p^*_{\mathrm{B}}x_{\mathrm{B}}$）称为正偏差，小于预言称为负偏差。二组分系统中两个组分通常偏向同一方向，总压曲线也随之向上或向下弯曲；偏差足够大时总压出现极大或极小，对应恒沸混合物（[6.3.9](/6.3.9)）。

偏差的分子原因是 A–B 之间的相互作用与 A–A、B–B 不同：

| 类型 | 分子原因 | 例子 | $\Delta_{\mathrm{mix}}H$ |
|---|---|---|---|
| 正偏差 | A–B 吸引弱于纯组分内部的吸引；混合破坏了某一组分的缔合（如醇的氢键） | 丙酮–二硫化碳、乙醇–水、乙醇–苯、苯–环己烷 | 常为正（吸热） |
| 负偏差 | A–B 吸引更强，或两者形成氢键、络合物 | 氯仿–丙酮（$\ce{C-H\cdots O=C}$ 氢键）、水–硝酸、水–HCl | 常为负（放热） |

无论偏差多大，在 $x_{\mathrm{A}} \to 1$ 的一端 A 总是服从 Raoult 定律、B 总是服从 Henry 定律；反之亦然。偏差的方向也决定了 Henry 常数与纯组分蒸气压的大小关系：理想时 $k_{x,\mathrm{B}} = p^*_{\mathrm{B}}$，正偏差时 $k_{x,\mathrm{B}} > p^*_{\mathrm{B}}$，负偏差时 $k_{x,\mathrm{B}} < p^*_{\mathrm{B}}$（见下图中的点线与虚线）。至今没有适用于一切非理想溶液的统一理论，热力学的任务是用少数几个可测的量（活度因子或超额函数）把偏离描述清楚，并保证它们相互一致。

![单参数 Margules 模型（6.4.3）给出的蒸气压，p*_A = 40 kPa，p*_B = 60 kPa：虚线为 Raoult 定律，点线为两端的 Henry 定律切线；左为正偏差（总压出现极大），右为负偏差](./plots/margules-deviations.py)

## 6.2. 活度与活度因子

### 6.2.1. 定义

理想液态混合物中 $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p) + RT\ln x_{\mathrm{B}}$，理想稀溶液中溶质 $\mu_{\mathrm{B}} = \mu^*_{x,\mathrm{B}}(T, p) + RT\ln x_{\mathrm{B}}$（[6.3.5](/6.3.5)）。对实际溶液，保留这一形式而修正浓度。

**定义 6.2.1（活度）** 选定组分 B 的参考态（与溶液同温同压，化学势为 $\mu^{\mathrm{ref}}_{\mathrm{B}}(T, p)$）后，把 B 在溶液中的化学势写成

$$
\mu_{\mathrm{B}}(\mathrm{sln}, T, p) = \mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) + RT\ln a_{\mathrm{B}},
$$
量纲一的量 $a_{\mathrm{B}}$ 称为 B 的活度；活度与相应浓度之比称为 B 的**活度因子**。参考态的选法有两类：

1. 按 Raoult 定律（用于溶剂，或混合物中地位相同的各组分）：参考态为同温同压下的纯液体 B，$\mu^{\mathrm{ref}}_{\mathrm{B}} = \mu^*_{\mathrm{B}}(\mathrm{l}, T, p)$，$a_{\mathrm{B}} = \gamma_{\mathrm{B}}x_{\mathrm{B}}$，且 $x_{\mathrm{B}} \to 1$ 时 $\gamma_{\mathrm{B}} \to 1$；
2. 按 Henry 定律（用于溶质）：参考态为 $x_{\mathrm{B}} = 1$、$b_{\mathrm{B}} = b^\circ$ 或 $c_{\mathrm{B}} = c^\circ$ 时仍服从 Henry 定律的假想态，$a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}x_{\mathrm{B}}$、$a_{b,\mathrm{B}} = \gamma_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ$、$a_{c,\mathrm{B}} = \gamma_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$，且 $x_{\mathrm{B}} \to 0$ 时三个活度因子都趋于 1。

对理想气体与稀溶液，这一定义回到 [6.1.8](/6.1.8#def-8.3.1) 中活度的非正式说法；本章给出的是它的严格形式。蒸气可视为理想气体时，定义 6.2.1 等价于修正后的两条定律：

$$
p_{\mathrm{A}} = p^*_{\mathrm{A}}a_{\mathrm{A}} = \gamma_{\mathrm{A}}p^*_{\mathrm{A}}x_{\mathrm{A}}, \qquad p_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}k_{x,\mathrm{B}}x_{\mathrm{B}}. \tag{6.1}
$$
活度因子度量对理想行为的偏离：按 Raoult 定律，$\gamma_{\mathrm{B}} > 1$ 为正偏差，$\gamma_{\mathrm{B}} < 1$ 为负偏差，$\lvert\gamma_{\mathrm{B}} - 1\rvert$ 越大越不理想。一般地 $\gamma_{\mathrm{B}} = \gamma_{\mathrm{B}}(T, p, x_{\mathrm{B}}, x_{\mathrm{C}}, \dots)$，主要靠实验测定（6.3）或分子模型（6.4.3）给出，这是溶液热力学的中心任务之一。

活度的含义是"有效浓度"：它是使理想溶液的公式在实际溶液中继续成立所需要的浓度。活度因子与逸度因子 $\varphi_{\mathrm{B}}$ 相对应：逸度修正压力，活度修正浓度。

### 6.2.2. 四种标准态

规定压力为 $p^\circ$ 时，参考态就成为**标准态**，化学势只是温度的函数。四种习惯选法：

| 处理基础 | 标准态（$T$，$p^\circ$） | 活度 | 极限条件 | 压力项被积函数 | 真实性 |
|---|---|---|---|---|---|
| Raoult 定律 $p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}}$ | 纯液体 B | $a_{\mathrm{B}} = \gamma_{\mathrm{B}}x_{\mathrm{B}}$ | $x_{\mathrm{B}} \to 1$，$\gamma_{\mathrm{B}} \to 1$ | $V^*_{\mathrm{m,B}}$ | 真实 |
| Henry 定律（$x$） | $x_{\mathrm{B}} = 1$ 仍服从 Henry 定律 | $a_{x,\mathrm{B}} = \gamma_{x,\mathrm{B}}x_{\mathrm{B}}$ | $x_{\mathrm{B}} \to 0$，$\gamma_{x,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | 假想 |
| Henry 定律（$b$） | $b_{\mathrm{B}} = b^\circ$ 仍服从 Henry 定律 | $a_{b,\mathrm{B}} = \gamma_{b,\mathrm{B}}b_{\mathrm{B}}/b^\circ$ | $b_{\mathrm{B}} \to 0$，$\gamma_{b,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | 假想 |
| Henry 定律（$c$） | $c_{\mathrm{B}} = c^\circ$ 仍服从 Henry 定律 | $a_{c,\mathrm{B}} = \gamma_{c,\mathrm{B}}c_{\mathrm{B}}/c^\circ$ | $c_{\mathrm{B}} \to 0$，$\gamma_{c,\mathrm{B}} \to 1$ | $V^{\infty}_{\mathrm{B}}$ | 假想 |

处于标准态时活度与活度因子都等于 1。理想液态混合物中 $\gamma_{\mathrm{B}} = 1$、$a_{\mathrm{B}} = x_{\mathrm{B}}$；理想稀溶液中溶剂 $\gamma_{\mathrm{A}} = 1$，溶质三种活度因子都为 1，三种活度分别等于 $x_{\mathrm{B}}$、$b_{\mathrm{B}}/b^\circ$、$c_{\mathrm{B}}/c^\circ$。

注意两点。第一，$a = 1$ 不等于处于标准态：标准态还规定了压力 $p^\circ$ 与纯度（或无限稀的环境）；一个 $x_{\mathrm{A}} = 0.3$、$a_{\mathrm{A}} = 1$ 的溶液中，A 的化学势等于纯 A 的化学势，蒸气分压等于纯 A 的饱和蒸气压，但它既不处于标准态，溶液也不是理想的。第二，按 Raoult 定律处理的组分 B，$x_{\mathrm{B}} = 1$ 时就是纯 B；按 Henry 定律处理时，即使 $x_{\mathrm{B}} = 1$ 也不是假想的标准态，$\gamma_{x,\mathrm{B}}(x_{\mathrm{B}} = 1) = p^*_{\mathrm{B}}/k_{x,\mathrm{B}}$。

### 6.2.3. 标准态的改变

对给定状态的溶液，$\mu_{\mathrm{B}}$ 与 $p_{\mathrm{B}}$ 唯一确定；活度与活度因子却随标准态（参考态）而变。由式 (6.1)，同一个 $p_{\mathrm{B}}$ 可以写成

$$
p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = k_{b,\mathrm{B}}a_{b,\mathrm{B}} = k_{c,\mathrm{B}}a_{c,\mathrm{B}},
$$
不同标准态下的活度之比是常数，等于 $\exp[(\mu^{\mathrm{ref}}_1 - \mu^{\mathrm{ref}}_2)/RT]$。特别地，

$$
\frac{\gamma_{\mathrm{B}}}{\gamma_{x,\mathrm{B}}} = \frac{k_{x,\mathrm{B}}}{p^*_{\mathrm{B}}} = \gamma^{\infty}_{\mathrm{B}}, \qquad \gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}}. \tag{6.2}
$$
第一式中 $\gamma^{\infty}_{\mathrm{B}}$ 是按 Raoult 定律的活度因子在无限稀时的极限（令 $x_{\mathrm{B}} \to 0$，$\gamma_{x,\mathrm{B}} \to 1$ 即得）。第二式由 $k_{b,\mathrm{B}} = k_{x,\mathrm{B}}M_{\mathrm{A}}b^\circ$（式 (5.5)）与 $M_{\mathrm{A}}b_{\mathrm{B}} = n_{\mathrm{B}}/n_{\mathrm{A}} = x_{\mathrm{B}}/x_{\mathrm{A}}$ 得到：$\gamma_{b,\mathrm{B}} = \frac{a_{b,\mathrm{B}}}{b_{\mathrm{B}}/b^\circ} = \frac{a_{x,\mathrm{B}}}{M_{\mathrm{A}}b_{\mathrm{B}}} = \frac{\gamma_{x,\mathrm{B}}x_{\mathrm{B}}}{x_{\mathrm{B}}/x_{\mathrm{A}}}$。即使溶液是理想稀溶液（$\gamma_{x,\mathrm{B}} = 1$），$\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}$ 也略小于 1，这只反映 $b_{\mathrm{B}}$ 与 $x_{\mathrm{B}}$ 不成严格正比。

**例 6.2.1** 某溶质 B 的水溶液，B 的蒸气压–组成曲线在 $x_{\mathrm{B}} \to 0$ 处的切线外推到 $x_{\mathrm{B}} = 1$ 得 $k_{x,\mathrm{B}} = 150\,\mathrm{kPa}$，纯 B 的饱和蒸气压 $p^*_{\mathrm{B}} = 50\,\mathrm{kPa}$。(1) 求三种活度 $a_{\mathrm{B}}$（Raoult）、$a_{x,\mathrm{B}}$、$a_{b,\mathrm{B}}$ 之间的关系；(2) 求 $x_{\mathrm{B}} \to 0$ 与 (3) $x_{\mathrm{B}} \to 1$ 时三种活度与活度因子。

**解** (1) 由 $p_{\mathrm{B}} = p^*_{\mathrm{B}}a_{\mathrm{B}} = k_{x,\mathrm{B}}a_{x,\mathrm{B}} = k_{b,\mathrm{B}}a_{b,\mathrm{B}}$，

$$
\frac{a_{\mathrm{B}}}{a_{x,\mathrm{B}}} = \frac{k_{x,\mathrm{B}}}{p^*_{\mathrm{B}}} = 3, \qquad \frac{a_{x,\mathrm{B}}}{a_{b,\mathrm{B}}} = \frac{k_{b,\mathrm{B}}}{k_{x,\mathrm{B}}} = M_{\mathrm{A}}b^\circ = 0.018015.
$$

(2) $x_{\mathrm{B}} \to 0$ 时 B 服从 Henry 定律：$\gamma_{x,\mathrm{B}} = \gamma_{b,\mathrm{B}} = 1$，$a_{x,\mathrm{B}} = x_{\mathrm{B}}$，$a_{b,\mathrm{B}} = b_{\mathrm{B}}/b^\circ$；而 $a_{\mathrm{B}} = 3x_{\mathrm{B}}$，$\gamma_{\mathrm{B}} = 3$（正偏差）。

(3) $x_{\mathrm{B}} \to 1$ 时 B 服从 Raoult 定律：$\gamma_{\mathrm{B}} = 1$，$a_{\mathrm{B}} = x_{\mathrm{B}}$；$a_{x,\mathrm{B}} = p^*_{\mathrm{B}}x_{\mathrm{B}}/k_{x,\mathrm{B}} = x_{\mathrm{B}}/3$，$\gamma_{x,\mathrm{B}} = 1/3$；$a_{b,\mathrm{B}} = a_{x,\mathrm{B}}/0.018015 = 18.5x_{\mathrm{B}}$，而 $b_{\mathrm{B}} \to \infty$，所以 $\gamma_{b,\mathrm{B}} \to 0$（与式 (6.2) 中 $\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}} \to 0$ 一致）。质量摩尔浓度标度只适合稀溶液，在浓溶液中活度因子失去"偏离程度"的直观意义。

### 6.2.4. 化学势的通式

把参考态的化学势用标准态表示，$\mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) = \mu^\circ_{\mathrm{B}}(T) + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$，得到任意物质化学势的通式：

$$
\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}} + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p. \tag{6.3}
$$

| 物质 | 标准态 | $a_{\mathrm{B}}$ | 压力项 |
|---|---|---|---|
| 气体 | $p^\circ$ 下的纯理想气体 | $f_{\mathrm{B}}/p^\circ = \varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ$ | 无（已含在逸度中） |
| 纯液体、纯固体 | $p^\circ$ 下的纯物质 | 1 | $\int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p$ |
| 液态混合物的组分、溶剂 | $p^\circ$ 下的纯液体 | $\gamma_{\mathrm{B}}x_{\mathrm{B}}$ | $\int_{p^\circ}^{p}V^*_{\mathrm{m,B}}\,\mathrm{d}p$ |
| 溶质 | 假想态（$x$、$b$ 或 $c$） | $\gamma_{x,\mathrm{B}}x_{\mathrm{B}}$ 等 | $\int_{p^\circ}^{p}V^{\infty}_{\mathrm{B}}\,\mathrm{d}p$ |

对凝聚相，压力项在压力不大时通常可以忽略，于是 $\mu_{\mathrm{B}} \approx \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}}$，这就是 [6.3.7](/6.3.7) 推导平衡常数时所用的形式。

另一种常见约定（IUPAC 的相对活度）把压力项并入活度：$a_{\mathrm{B}} = \exp[(\mu_{\mathrm{B}} - \mu^\circ_{\mathrm{B}})/RT]$，此时 $p \ne p^\circ$ 下的纯液体 $a \ne 1$。两者相差因子 $\exp(\int V\,\mathrm{d}p/RT)$，对水在 $1\,\mathrm{MPa}$ 下只有 $1.007$。本课程沿用把参考态取在实际压力下的约定，纯凝聚相的活度恒为 1。

## 6.3. 活度的测定

### 6.3.1. 蒸气压法

测出溶液上方的平衡分压，由式 (6.1)，

$$
a_{\mathrm{A}} = \frac{p_{\mathrm{A}}}{p^*_{\mathrm{A}}}, \qquad a_{x,\mathrm{B}} = \frac{p_{\mathrm{B}}}{k_{x,\mathrm{B}}},
$$
$k_{x,\mathrm{B}}$ 由 $p_{\mathrm{B}}/x_{\mathrm{B}}$ 外推到 $x_{\mathrm{B}} \to 0$ 求得。蒸气不理想时把分压换成逸度。此法只适用于溶剂与挥发性溶质。

**例 6.3.1** $30\,^\circ\mathrm{C}$ 时 $p^*_{\mathrm{A}} = 40\,\mathrm{kPa}$，$p^*_{\mathrm{B}} = 120\,\mathrm{kPa}$。$x_{\mathrm{A}} = 0.5$ 的实际液态混合物与蒸气平衡，总压 $100\,\mathrm{kPa}$，已知 $\gamma_{\mathrm{A}} = 1.1$，求 $\gamma_{\mathrm{B}}$ 与气相组成 $y_{\mathrm{A}}$。

**解** $p_{\mathrm{A}} = \gamma_{\mathrm{A}}p^*_{\mathrm{A}}x_{\mathrm{A}} = 1.1 \times 40 \times 0.5 = 22\,\mathrm{kPa}$，$p_{\mathrm{B}} = 100 - 22 = 78\,\mathrm{kPa}$，$\gamma_{\mathrm{B}} = 78/(120 \times 0.5) = 1.3$；$y_{\mathrm{A}} = 22/100 = 0.22$。两个活度因子都大于 1，是正偏差系统。

### 6.3.2. 依数性法

[6.3.5](/6.3.5) 的凝固点降低与渗透压公式只用到溶剂的化学势；对实际溶液，把其中的 $x_{\mathrm{A}}$ 换成 $a_{\mathrm{A}}$，推导不变：

$$
\ln a_{\mathrm{A}} = -\frac{\Delta_{\mathrm{fus}}H_{\mathrm{m,A}}}{R}\left(\frac{1}{T_{\mathrm{f}}} - \frac{1}{T^*_{\mathrm{f}}}\right), \qquad \ln a_{\mathrm{A}} = -\frac{\varPi V^*_{\mathrm{m,A}}}{RT}. \tag{6.4}
$$
测出凝固点或渗透压即得溶剂的活度。前者给出的是凝固点下的活度，要换算到其他温度需用 $H^{\mathrm{E}}$（6.4）。此法只能直接测溶剂的活度；溶质（尤其是不挥发的溶质）的活度由下面的 Gibbs–Duhem 方程求得。

### 6.3.3. Gibbs–Duhem 方程法

等温等压下，二组分溶液的 **Gibbs–Duhem 方程** $x_{\mathrm{A}}\,\mathrm{d}\mu_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\mu_{\mathrm{B}} = 0$ 中代入 $\mathrm{d}\mu_{\mathrm{B}} = RT\,\mathrm{d}\ln a_{\mathrm{B}}$（参考态的化学势在等温等压下是常数，与标准态的选择无关）：

$$
x_{\mathrm{A}}\,\mathrm{d}\ln a_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln a_{\mathrm{B}} = 0.
$$
再代入 $a = \gamma x$，由 $x_{\mathrm{A}}\,\mathrm{d}\ln x_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln x_{\mathrm{B}} = \mathrm{d}x_{\mathrm{A}} + \mathrm{d}x_{\mathrm{B}} = 0$，

$$
x_{\mathrm{A}}\,\mathrm{d}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln\gamma_{\mathrm{B}} = 0. \tag{6.5}
$$
它对 B 用 Raoult 定律或 Henry 定律处理都成立（两者的 $\ln\gamma$ 只差一个常数，式 (6.2)）。由此，已知一个组分的活度因子随组成的变化，就能积分求出另一个：

$$
\ln\gamma_{\mathrm{B}}(x_{\mathrm{B}}) = -\int_{1}^{x_{\mathrm{B}}}\frac{x_{\mathrm{A}}}{x_{\mathrm{B}}}\frac{\mathrm{d}\ln\gamma_{\mathrm{A}}}{\mathrm{d}x_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} \quad (\text{按 Raoult 定律}), \qquad \ln\gamma_{x,\mathrm{B}}(x_{\mathrm{B}}) = -\int_{0}^{x_{\mathrm{B}}}\frac{x_{\mathrm{A}}}{x_{\mathrm{B}}}\frac{\mathrm{d}\ln\gamma_{\mathrm{A}}}{\mathrm{d}x_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} \quad (\text{按 Henry 定律}).
$$
后一个积分在 $x_{\mathrm{B}} \to 0$ 处收敛，因为 $\ln\gamma_{\mathrm{A}}$ 在那里像 $x_{\mathrm{B}}^2$ 一样趋于零（溶剂服从 Raoult 定律的程度比溶质服从 Henry 定律高一阶）。过去用图解积分，现在用数值积分：把测得的 $\ln\gamma_{\mathrm{A}}$ 先用多项式拟合平滑，再求导、积分（`numpy.polyfit` 或 `scipy.integrate.cumulative_trapezoid`，[4.4.4](/4.4.4#sec-4.3.1)）。

![由 γ_A 的"测量值"（双参数 Margules 模型加 1% 噪声）经平滑后按 Gibbs–Duhem 方程数值积分得到的 ln γ_B，与模型的真值几乎重合](./plots/gibbs-duhem-integration.py)

若两个组分的活度因子都由实验测得，它们必须满足式 (6.5)，称为热力学一致性。式 (6.5) 还说明：等温等压下组成改变时，若 $\mu_{\mathrm{A}}$（或 $a_{\mathrm{A}}$）增大，$\mu_{\mathrm{B}}$（或 $a_{\mathrm{B}}$）必然减小。一个整体性的检验见 6.4.1。

电解质溶液中，正负离子不能单独存在，活度以平均活度表示，主要由电动势法测定（[6.3.13](/6.3.13)）。

## 6.4. 超额函数

### 6.4.1. 定义与性质

活度因子描述单个组分的非理想性；整个溶液的非理想性用超额函数描述。

**定义 6.4.1（超额函数）** 给定温度、压力与组成下，实际溶液的混合函数减去同组成的理想液态混合物的混合函数，称为超额函数：

$$
V^{\mathrm{E}} = \Delta_{\mathrm{mix}}V - \Delta_{\mathrm{mix}}V^{\mathrm{id}}, \quad H^{\mathrm{E}} = \Delta_{\mathrm{mix}}H - \Delta_{\mathrm{mix}}H^{\mathrm{id}}, \quad S^{\mathrm{E}} = \Delta_{\mathrm{mix}}S - \Delta_{\mathrm{mix}}S^{\mathrm{id}}, \quad G^{\mathrm{E}} = \Delta_{\mathrm{mix}}G - \Delta_{\mathrm{mix}}G^{\mathrm{id}}.
$$
其中 $G^{\mathrm{E}}$ 称为**超额 Gibbs 自由能**。

由于 $\Delta_{\mathrm{mix}}V^{\mathrm{id}} = \Delta_{\mathrm{mix}}H^{\mathrm{id}} = 0$（定理 5.1.1），$V^{\mathrm{E}}$ 与 $H^{\mathrm{E}}$ 就是实际的混合体积与混合焓，可以用膨胀计与量热计直接测量。超额函数之间满足与普通热力学函数相同的关系（$G^{\mathrm{E}} = H^{\mathrm{E}} - TS^{\mathrm{E}}$ 等），因为理想部分已经分别满足这些关系。

**定理 6.4.1** 各组分都按 Raoult 定律选取参考态时，

$$
G^{\mathrm{E}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}, \qquad RT\ln\gamma_{\mathrm{B}} = \left(\frac{\partial G^{\mathrm{E}}}{\partial n_{\mathrm{B}}}\right)_{T,p,n_{\mathrm{C}}}, \tag{6.6}
$$
并且

$$
V^{\mathrm{E}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial p}\right)_{T,x}, \qquad H^{\mathrm{E}} = -RT^2\sum_{\mathrm{B}}n_{\mathrm{B}}\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial T}\right)_{p,x}, \qquad S^{\mathrm{E}} = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\left[\ln\gamma_{\mathrm{B}} + T\left(\frac{\partial\ln\gamma_{\mathrm{B}}}{\partial T}\right)_{p,x}\right].
$$

**证明** $\Delta_{\mathrm{mix}}G = \sum_{\mathrm{B}}n_{\mathrm{B}}(\mu_{\mathrm{B}} - \mu^*_{\mathrm{B}}) = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln a_{\mathrm{B}} = RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}} + RT\sum_{\mathrm{B}}n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$，第一项是 $\Delta_{\mathrm{mix}}G^{\mathrm{id}}$，得第一式。$G^{\mathrm{E}}$ 是偏摩尔量 $RT\ln\gamma_{\mathrm{B}} = \mu_{\mathrm{B}} - \mu^{\mathrm{id}}_{\mathrm{B}}$ 的加和，由偏摩尔量的定义得第二式。其余三式分别由 $V^{\mathrm{E}} = (\partial G^{\mathrm{E}}/\partial p)_{T,n}$、$H^{\mathrm{E}} = -T^2[\partial(G^{\mathrm{E}}/T)/\partial T]_{p,n}$（Gibbs–Helmholtz 方程）、$S^{\mathrm{E}} = -(\partial G^{\mathrm{E}}/\partial T)_{p,n}$ 得到。$\square$

式 (6.6) 说明 $G^{\mathrm{E}}(T, p, n_{\mathrm{A}}, n_{\mathrm{B}}, \dots)$ 是所有活度因子的"生成函数"：给出一个 $G^{\mathrm{E}}$ 的模型，求偏导就得到每个组分的活度因子，而且它们自动满足 Gibbs–Duhem 方程。这是建立溶液模型的标准做法。由式 (6.6) 还得到一个整体的一致性检验：二组分系统中 $G^{\mathrm{E}}_{\mathrm{m}}/RT = x_{\mathrm{A}}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$ 在 $x_{\mathrm{B}} = 0$ 与 $1$ 处都为零，由式 (6.5) 它对 $x_{\mathrm{B}}$ 的导数为 $\ln(\gamma_{\mathrm{B}}/\gamma_{\mathrm{A}})$，于是恒温数据必须满足

$$
\int_0^1\ln\frac{\gamma_{\mathrm{A}}}{\gamma_{\mathrm{B}}}\,\mathrm{d}x_{\mathrm{B}} = 0
$$
（面积检验）。$\ln(\gamma_{\mathrm{A}}/\gamma_{\mathrm{B}})$ 对 $x_{\mathrm{B}}$ 的曲线在横轴上下所围的面积应当相等。

超额函数常用来提取分子间相互作用的信息。氯仿–丙酮系统 $H^{\mathrm{E}} < 0$（形成氢键放热），$S^{\mathrm{E}}$ 也为负（氢键使分子排列更有序），$\lvert H^{\mathrm{E}}\rvert$ 大于 $\lvert G^{\mathrm{E}}\rvert$，焓与熵的效应部分抵消。把同样的思想用于光谱，实际混合物的光谱减去按组成加权的纯组分光谱，得到"超额光谱"，可以分辨混合后新出现或消失的相互作用。

### 6.4.2. 正规溶液与无热溶液

由 $G^{\mathrm{E}} = H^{\mathrm{E}} - TS^{\mathrm{E}}$，非理想性可以来自焓，也可以来自熵。两种极端情形：

**定义 6.4.2** $S^{\mathrm{E}} = 0$（混合熵与理想溶液相同）而 $H^{\mathrm{E}} \ne 0$ 的溶液称为**正规溶液**，此时 $G^{\mathrm{E}} = H^{\mathrm{E}}$，非理想性完全来自混合热效应；$H^{\mathrm{E}} = 0$ 而 $S^{\mathrm{E}} \ne 0$ 的溶液称为**无热溶液**，此时 $G^{\mathrm{E}} = -TS^{\mathrm{E}}$，非理想性完全来自熵。

由定理 6.4.1，正规溶液中 $S^{\mathrm{E}} = 0$ 意味着 $RT\ln\gamma_{\mathrm{B}}$ 不随温度变化（组成一定时），所以 $\ln\gamma_{\mathrm{B}} \propto 1/T$；无热溶液中 $H^{\mathrm{E}} = 0$ 意味着 $\ln\gamma_{\mathrm{B}}$ 与温度无关。分子大小相近、只有色散力作用的非极性液体混合物接近正规溶液（Hildebrand 的正规溶液理论）；分子大小悬殊而相互作用相近的系统（如高分子在其单体或类似小分子中的溶液）接近无热溶液，非理想性来自大分子与小分子排列方式数目的差别（Flory–Huggins 理论，[6.3.21](/6.3.21)）。

### 6.4.3. 单参数 Margules 模型

最简单的正规溶液模型取

$$
G^{\mathrm{E}} = W\frac{n_{\mathrm{A}}n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}}, \qquad G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}},
$$
$W$ 为与组成无关的参数。

**定理 6.4.2（Margules 方程）** 在上述模型中

$$
\ln\gamma_{\mathrm{A}} = \frac{W}{RT}x_{\mathrm{B}}^2, \qquad \ln\gamma_{\mathrm{B}} = \frac{W}{RT}x_{\mathrm{A}}^2. \tag{6.7}
$$
式 (6.7) 是单参数的 Margules 方程。

**证明** 由式 (6.6)，$RT\ln\gamma_{\mathrm{A}} = \frac{\partial}{\partial n_{\mathrm{A}}}\frac{Wn_{\mathrm{A}}n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}} = \frac{Wn_{\mathrm{B}}(n_{\mathrm{A}} + n_{\mathrm{B}}) - Wn_{\mathrm{A}}n_{\mathrm{B}}}{(n_{\mathrm{A}} + n_{\mathrm{B}})^2} = Wx_{\mathrm{B}}^2$，同理得 $\ln\gamma_{\mathrm{B}}$。$\square$

可以直接验证式 (6.7) 满足 Gibbs–Duhem 方程：$x_{\mathrm{A}}\,\mathrm{d}(x_{\mathrm{B}}^2) + x_{\mathrm{B}}\,\mathrm{d}(x_{\mathrm{A}}^2) = 2x_{\mathrm{A}}x_{\mathrm{B}}(\mathrm{d}x_{\mathrm{B}} + \mathrm{d}x_{\mathrm{A}}) = 0$。模型的性质：

- $W > 0$ 为正偏差，$W < 0$ 为负偏差；两个组分的 $\ln\gamma$ 曲线互为镜像，无限稀时 $\gamma^{\infty} = \mathrm{e}^{W/RT}$，Henry 常数 $k_{x,\mathrm{B}} = p^*_{\mathrm{B}}\mathrm{e}^{W/RT}$（式 (6.2)）。
- 若 $W$ 与温度无关，$H^{\mathrm{E}} = G^{\mathrm{E}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$，$S^{\mathrm{E}} = 0$，是正规溶液。
- 格子模型给出 $W$ 的分子意义：每个分子有 $z$ 个最近邻，A–A、B–B、A–B 对的相互作用能为 $\varepsilon_{\mathrm{AA}}$、$\varepsilon_{\mathrm{BB}}$、$\varepsilon_{\mathrm{AB}}$（吸引为负），随机混合时 $W = zN_{\mathrm{A}}\left[\varepsilon_{\mathrm{AB}} - \frac{1}{2}(\varepsilon_{\mathrm{AA}} + \varepsilon_{\mathrm{BB}})\right]$。异种分子之间的吸引弱于同种分子的平均时 $W > 0$。
- $W > 2RT$ 时 $\Delta_{\mathrm{mix}}G_{\mathrm{m}} = RT(x_{\mathrm{A}}\ln x_{\mathrm{A}} + x_{\mathrm{B}}\ln x_{\mathrm{B}}) + Wx_{\mathrm{A}}x_{\mathrm{B}}$ 在 $x = 1/2$ 附近向上凸，溶液分成两个液相；临界温度 $T_{\mathrm{c}} = W/(2R)$ 就是**会溶温度**（[6.3.9](/6.3.9)）。

![单参数 Margules 模型的活度因子（按 Raoult 定律）：正偏差时 ln γ > 0，负偏差时 ln γ < 0，两组分的曲线互为镜像](./plots/margules-activity-coefficients.py)

实际系统常需要两个参数：$\ln\gamma_{\mathrm{A}} = x_{\mathrm{B}}^2[A_{\mathrm{AB}} + 2(A_{\mathrm{BA}} - A_{\mathrm{AB}})x_{\mathrm{A}}]$，$\ln\gamma_{\mathrm{B}} = x_{\mathrm{A}}^2[A_{\mathrm{BA}} + 2(A_{\mathrm{AB}} - A_{\mathrm{BA}})x_{\mathrm{B}}]$（双参数 Margules 方程，$A_{\mathrm{AB}} = \ln\gamma^{\infty}_{\mathrm{A}}$，$A_{\mathrm{BA}} = \ln\gamma^{\infty}_{\mathrm{B}}$）；工程上更常用 Wilson、NRTL、UNIQUAC 等局部组成模型，它们都由一个 $G^{\mathrm{E}}$ 的表达式出发，按式 (6.6) 求出活度因子。

## 6.5. 分配定律与萃取

### 6.5.1. Nernst 分配定律

实验发现：一定温度和压力下，一种物质溶解在两种同时存在、互不相溶的液体中，达到平衡后，在低浓度范围内它在两相中的浓度之比为常数。热力学给出这一规律的证明与适用条件。

**定理 6.5.1（Nernst 分配定律）** 一定温度和压力下，溶质 B 在互不相溶的两液相 $\alpha$、$\beta$ 之间达到平衡时，

$$
\frac{a_{\mathrm{B}}(\alpha)}{a_{\mathrm{B}}(\beta)} = \exp\frac{\mu^{\mathrm{ref}}_{\mathrm{B}}(\beta) - \mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha)}{RT} = K(T, p);
$$
两相都是理想稀溶液时，

$$
\frac{c_{\mathrm{B}}(\alpha)}{c_{\mathrm{B}}(\beta)} = K \quad\text{或}\quad \frac{b_{\mathrm{B}}(\alpha)}{b_{\mathrm{B}}(\beta)} = K'. \tag{6.8}
$$

**证明** 平衡时 B 在两相中的化学势相等：$\mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha) + RT\ln a_{\mathrm{B}}(\alpha) = \mu^{\mathrm{ref}}_{\mathrm{B}}(\beta) + RT\ln a_{\mathrm{B}}(\beta)$。两相中 B 都按 Henry 定律选取参考态，参考态的化学势只与 $T$、$p$ 及溶剂有关，故活度之比是常数。理想稀溶液中活度等于相对浓度。$\square$

比值 $K$ 称为分配系数（partition coefficient）。几点说明：

1. 两相中 B 的参考态不同（溶剂不同，假想态不同），$\mu^{\mathrm{ref}}_{\mathrm{B}}(\alpha) \ne \mu^{\mathrm{ref}}_{\mathrm{B}}(\beta)$。所以平衡时 B 在两相中的化学势相等，浓度（以至活度）却不相等。若两相共用一个蒸气相，由 $p_{\mathrm{B}} = k_{\mathrm{B},\alpha}a_{\mathrm{B}}(\alpha) = k_{\mathrm{B},\beta}a_{\mathrm{B}}(\beta)$ 得 $K = k_{\mathrm{B},\beta}/k_{\mathrm{B},\alpha}$：B 在 Henry 常数较小（溶剂对它吸引较强）的一相中浓度较高。
2. 分配定律只对两相中分子形态相同的部分成立。苯甲酸在水中主要以单体存在，在苯中大部分缔合成二聚体：对单体 $c_{\mathrm{B}}(\text{水})/c_{\mathrm{B}}(\text{苯，单体}) = K$，二聚平衡 $c_{\ce{B2}}/c_{\mathrm{B}}^2 = K_{\mathrm{d}}$；若苯中几乎全是二聚体，总浓度 $c(\text{苯}) \approx c_{\ce{B2}}$，于是 $c(\text{水})/\sqrt{c(\text{苯})}$ 为常数。解离同理。
3. 分配系数在药物化学中极为重要：药物在正辛醇与水之间的分配系数 $P$ 的对数 $\lg P$ 是其亲脂性的标准量度，决定它能否穿过细胞膜的脂双层；口服药物一般要求 $\lg P$ 不超过约 5（Lipinski 规则之一）。反相色谱的保留、污染物在生物体内的富集也由分配系数决定。

### 6.5.2. 萃取

用与原溶剂不相溶的另一种溶剂把溶质从溶液中提取出来，称为萃取（extraction）。分配定律给出萃取的效率。

设 $V$ 体积的水溶液中含溶质 $m_0$，每次用 $V_{\mathrm{e}}$ 体积的有机溶剂萃取，分配系数 $K = c(\text{有机相})/c(\text{水相})$。第一次萃取后水相中剩余 $m_1$：

$$
\frac{(m_0 - m_1)/V_{\mathrm{e}}}{m_1/V} = K \quad\Longrightarrow\quad m_1 = m_0\frac{V}{V + KV_{\mathrm{e}}}.
$$
重复 $n$ 次，$m_n = m_0\left(\frac{V}{V + KV_{\mathrm{e}}}\right)^n$。

**命题 6.5.1** 萃取剂总体积 $V_{\mathrm{e}}$ 一定时，分 $n$ 次萃取（每次 $V_{\mathrm{e}}/n$）后的剩余量

$$
m_n = m_0\left(1 + \frac{KV_{\mathrm{e}}}{nV}\right)^{-n}
$$
随 $n$ 单调减小，$n \to \infty$ 时趋于 $m_0\exp(-KV_{\mathrm{e}}/V)$。

**证明** 记 $u = KV_{\mathrm{e}}/V > 0$。$(1 + u/n)^n$ 随 $n$ 单调增大并趋于 $\mathrm{e}^u$（对 $f(t) = t\ln(1 + u/t)$ 求导，$f'(t) = \ln(1 + s) - \frac{s}{1 + s} > 0$，其中 $s = u/t$），故 $m_n$ 单调减小并趋于 $m_0\mathrm{e}^{-u}$。$\square$

例如 $K = 4$、$V = 100\,\mathrm{mL}$、$V_{\mathrm{e}} = 30\,\mathrm{mL}$：一次萃取剩余 $1/(1 + 1.2) = 45.5\%$；分三次各 $10\,\mathrm{mL}$ 剩余 $(1/1.4)^3 = 36.4\%$；无限多次的极限为 $\mathrm{e}^{-1.2} = 30.1\%$。"少量多次"优于"一次全量"，但次数增加的收益递减。

![萃取剂总量一定（K = 4，V = 100 mL，V_e = 30 mL）时水相中剩余溶质随萃取次数的变化，虚线为 n → ∞ 的极限 e^{−KV_e/V}](./plots/extraction.py)

## 6.6. 综合例题

**例 6.6.1** $298\,\mathrm{K}$ 时某 NaCl 水溶液的渗透压为 $2p^\circ$。求下列过程的 $\Delta G$：

$$
1\,\mathrm{mol}\ \ce{H2O}(\text{溶液}, 298\,\mathrm{K}, p^\circ) \longrightarrow 1\,\mathrm{mol}\ \ce{H2O}(\mathrm{l}, 298\,\mathrm{K}, p^\circ).
$$
溶液的量很大，取出 $1\,\mathrm{mol}$ 水不改变其组成。

**解** 方法一：取 $298\,\mathrm{K}$、$p^\circ$ 下的纯水为参考态，$\Delta G = \mu^*_{\mathrm{A}} - \mu_{\mathrm{A}} = -RT\ln a_{\mathrm{A}}$。由式 (6.4)，$-RT\ln a_{\mathrm{A}} = \varPi V^*_{\mathrm{m,A}} = 2 \times 10^5\,\mathrm{Pa} \times 18.07 \times 10^{-6}\,\mathrm{m^3\,mol^{-1}} = 3.6\,\mathrm{J\,mol^{-1}}$。

方法二：设计途径：先把溶液从 $p^\circ$ 加压到 $3p^\circ$，$\Delta\mu_{\mathrm{I}} = \int_{p^\circ}^{3p^\circ}V_{\mathrm{A}}\,\mathrm{d}p \approx V^*_{\mathrm{m,A}} \cdot 2p^\circ = 3.6\,\mathrm{J\,mol^{-1}}$（稀溶液中 $V_{\mathrm{A}} \approx V^*_{\mathrm{m,A}}$）；此时溶液与 $p^\circ$ 下的纯水正好达到渗透平衡，水透过半透膜进入纯水一侧，$\Delta\mu_{\mathrm{II}} = 0$。两步相加，$\Delta G = 3.6\,\mathrm{J}$。

$\Delta G > 0$：从溶液中取出纯水不能自发进行。在等温等压下，它至少需要 $3.6\,\mathrm{J}$ 的非体积功，这就是反渗透的最小功（[6.3.5](/6.3.5)）。

**例 6.6.2** 某物质在互不相溶的液体 $\alpha$ 与 $\beta$ 之间达到分配平衡，它在 $\alpha$ 相中以 B 的形式存在，在 $\beta$ 相中以 $\ce{B2}$ 的形式存在。下列关系哪些成立：(a) $\mu_\alpha(\mathrm{B}) = \mu_\beta(\ce{B2})$；(b) $2\mu_\alpha(\mathrm{B}) = \mu_\beta(\ce{B2})$；(c) $a_\alpha^2(\mathrm{B})/a_\beta(\ce{B2}) = K$；(d) 等温等压下 $\mathrm{d}\ln a_\alpha^2(\mathrm{B}) = \mathrm{d}\ln a_\beta(\ce{B2})$？

**解** 这实际上是一个跨相的化学平衡 $2\mathrm{B}(\alpha) \ce{<=>} \ce{B2}(\beta)$，平衡条件是 $\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$（[6.3.7](/6.3.7)），即 (b)；代入化学势的表达式得 (c)；对 (b) 求微分得 (d)。(a) 不成立。分配定律式 (6.8) 只是这一平衡在两相分子形态相同时的特例。

## 小结

| 内容 | 要点 |
|---|---|
| 偏差 | 正偏差：A–B 吸引较弱或破坏缔合，$\gamma > 1$，$k_{x} > p^*$；负偏差相反 |
| 活度 | $\mu_{\mathrm{B}} = \mu^{\mathrm{ref}}_{\mathrm{B}}(T, p) + RT\ln a_{\mathrm{B}}$；Raoult 参考态（纯液体）与 Henry 参考态（$x$、$b$、$c$ 三种假想态）；活度随参考态而变，化学势不变 |
| 换算 | $\gamma_{\mathrm{B}}/\gamma_{x,\mathrm{B}} = k_{x,\mathrm{B}}/p^*_{\mathrm{B}} = \gamma^{\infty}_{\mathrm{B}}$；$\gamma_{b,\mathrm{B}} = x_{\mathrm{A}}\gamma_{x,\mathrm{B}}$ |
| 通式 | $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}} + \int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$；纯凝聚相 $a = 1$，气体 $a = f/p^\circ$ |
| 测定 | 蒸气压法；依数性法（溶剂）；Gibbs–Duhem 积分 $x_{\mathrm{A}}\,\mathrm{d}\ln\gamma_{\mathrm{A}} + x_{\mathrm{B}}\,\mathrm{d}\ln\gamma_{\mathrm{B}} = 0$（溶质，热力学一致性）；电动势法（电解质） |
| 超额函数 | $G^{\mathrm{E}} = RT\sum n_{\mathrm{B}}\ln\gamma_{\mathrm{B}}$，$RT\ln\gamma_{\mathrm{B}} = \partial G^{\mathrm{E}}/\partial n_{\mathrm{B}}$；$V^{\mathrm{E}} = \Delta_{\mathrm{mix}}V$，$H^{\mathrm{E}} = \Delta_{\mathrm{mix}}H$ |
| 模型 | 正规溶液 $S^{\mathrm{E}} = 0$，无热溶液 $H^{\mathrm{E}} = 0$；Margules：$G^{\mathrm{E}}_{\mathrm{m}} = Wx_{\mathrm{A}}x_{\mathrm{B}}$，$\ln\gamma_{\mathrm{A}} = Wx_{\mathrm{B}}^2/RT$；$W > 2RT$ 时分相 |
| 分配与萃取 | $a(\alpha)/a(\beta) = K$，稀溶液中浓度比为常数，只对相同分子形态成立；少量多次萃取更有效，剩余量 $\to m_0\mathrm{e}^{-KV_{\mathrm{e}}/V}$ |
