## 3.1 事件的独立性

### 3.1.1 两个事件的独立性

**定义**：设 $(\Omega, \mathcal{F}, \mathbb{P})$ 是概率空间，$A, B \in \mathcal{F}$，如果
$$
\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B),
$$
则称 $A$ 与 $B$ 相互独立，简称独立。

**性质**：
- 若 $\mathbb{P}(B) > 0$，则独立性等价于 $\mathbb{P}(A|B) = \mathbb{P}(A)$
- 不可能事件、必然事件与任何事件独立
- 若 $A$ 与 $B$ 独立，则 $A$ 与 $B^c$、$A^c$ 与 $B$、$A^c$ 与 $B^c$ 均独立

**注意**：独立性与互不相容（不相交）是不同的概念

### 3.1.2 两个事件的条件独立性

**定义**：设 $(\Omega, \mathcal{F}, \mathbb{P})$ 是概率空间，$A, B, C \in \mathcal{F}$，且 $\mathbb{P}(C) > 0$，如果
$$
\mathbb{P}(A \cap B|C) = \mathbb{P}(A|C)\mathbb{P}(B|C),
$$
则称 $A$ 与 $B$ 在给定 $C$ 之下条件独立。

**注意**：独立性不蕴含条件独立性，反之亦然

### 3.1.3 一组事件的相互独立性

**定义**：设 $A_1, A_2, \ldots, A_n \in \mathcal{F}$，如果对任意非空子集 $S \subset \{1, 2, \ldots, n\}$，都有
$$
\mathbb{P}\left( \bigcap_{i \in S} A_i \right) = \prod_{i \in S} \mathbb{P}(A_i),
$$
则称 $A_1, A_2, \ldots, A_n$ 相互独立。

### 3.1.4 一组事件的两两独立性

**定义**：设 $A_1, A_2, \ldots, A_n \in \mathcal{F}$，如果对任意的 $i \neq j$，有
$$
\mathbb{P}(A_i \cap A_j) = \mathbb{P}(A_i)\mathbb{P}(A_j),
$$
则称 $A_1, A_2, \ldots, A_n$ 两两独立。

**注意**：两两独立不一定相互独立

### 3.1.5 事件独立性的应用

**例**：检测问题。设每人携带违禁品的概率为0.04%，连续检测20人，求至少一人携带的概率。
$$
\mathbb{P}\left( \bigcup_{i=1}^{20} A_i \right) = 1 - \mathbb{P}\left( \bigcap_{i=1}^{20} A_i^c \right) = 1 - (1 - 0.0004)^{20} \approx 0.008.
$$

## 3.2 随机变量

### 3.2.1 随机变量的引入

**动机**：
- 简化事件表示
- 数值化试验结果
- 通用性，多个场景可共用同一模型

**定义**（随机变量）：设 $(\Omega, \mathcal{F})$ 为可测空间，如果函数 $X: \Omega \to \mathbb{R}$ 满足对任意 $x \in \mathbb{R}$，有
$$
\{ \omega \in \Omega : X(\omega) \leq x \} \in \mathcal{F},
$$
则称 $X$ 为随机变量。

**注**：随机变量是样本空间到实数的可测函数

### 3.2.2 随机变量的例子

1. 抛掷两次硬币，$X$ 表示正面朝上的次数
2. 测量血压，$X$ 表示收缩压的测量值
3. 扑克牌中抽13张，$X$ 表示梅花的张数

### 3.2.3 随机变量的函数

**定理**：若 $X$ 是随机变量，$g$ 是可测函数，则 $Y = g(X)$ 也是随机变量

**推论**：随机变量的四则运算、极限、连续函数复合等仍为随机变量

## 3.3 随机变量的独立性

### 3.3.1 定义

**定义**：设 $X_1, X_2, \ldots, X_n$ 是随机变量，如果对任意实数 $x_1, x_2, \ldots, x_n$，有
$$
\mathbb{P}(X_1 \leq x_1, X_2 \leq x_2, \ldots, X_n \leq x_n) = \mathbb{P}(X_1 \leq x_1) \mathbb{P}(X_2 \leq x_2) \cdots \mathbb{P}(X_n \leq x_n),
$$
则称 $X_1, X_2, \ldots, X_n$ 相互独立。

### 3.3.2 性质

**定理**：若 $X_1, \ldots, X_n$ 相互独立，则对任意 Borel 集 $A_1, \ldots, A_n$，事件 $\{X_1 \in A_1\}, \ldots, \{X_n \in A_n\}$ 相互独立

**定理**：若 $X_1, \ldots, X_n$ 相互独立，$g_1, \ldots, g_n$ 是可测函数，则 $g_1(X_1), \ldots, g_n(X_n)$ 相互独立

### 3.3.3 独立序列与独立同分布

**定义**：如果对任意 $n$，$X_1, \ldots, X_n$ 相互独立，则称随机变量序列 $\{X_i\}$ 相互独立

**定义**：如果随机变量序列 $\{X_i\}$ 相互独立且具有相同的分布，则称为独立同分布序列（i.i.d.）

## 3.4 赌徒破产模型（补充）

**问题**：甲有本金 $a$ 元，决心赢到 $b$ 元停止。每局赢的概率 $p=1/2$，输赢1元，输光停止。求输光概率 $q(a)$

**解**：设 $q(k)$ 表示有本金 $k$ 元时输光的概率。边界条件 $q(0)=1$，$q(a+b)=0$。由全概率公式：
$$
q(k) = \frac{1}{2} q(k+1) + \frac{1}{2} q(k-1)
$$
解得：
$$
q(a) = \frac{b}{a+b}
$$

**结论**：本金有限时，贪心越大（$b$ 越大），输光概率越大。若一直赌下去（$b \to \infty$），必定输光

## 小结

### 核心知识点
- **事件的独立性**：两个事件、条件独立、相互独立与两两独立
- **随机变量**：定义、例子、随机变量的函数
- **随机变量的独立性**：定义、性质、独立序列与i.i.d.序列

### 重要技巧
- 反例法区分概念差异
- 类比法理解新概念
- 归纳法求解递归问题（如赌徒破产模型）

### 关键公式
- 独立性：$\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$
- 条件独立性：$\mathbb{P}(A \cap B|C) = \mathbb{P}(A|C)\mathbb{P}(B|C)$
- 相互独立：对任意子集 $S$，$\mathbb{P}\left( \bigcap_{i \in S} A_i \right) = \prod_{i \in S} \mathbb{P}(A_i)$
- 随机变量独立：$\mathbb{P}(X_1 \leq x_1, \ldots, X_n \leq x_n) = \prod_{i=1}^n \mathbb{P}(X_i \leq x_i)$
