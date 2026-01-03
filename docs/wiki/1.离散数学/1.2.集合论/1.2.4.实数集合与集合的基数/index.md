## 12.1. 实数集合

**定义 12.1.1** 整数 对自然数集合 $N$，令
$$
Z_+ = N - \{0\}
$$

$$
Z_- = \{\langle 0,n\rangle | n \in Z_+\},
$$

$$
Z = Z_- \cup \{0\} \cup Z_+。
$$

则称 $Z_+$ 的元素为正整数，$Z_-$ 的元素为负整数，$Z$ 的元素为整数。

**定义 12.1.2** 一个整数的相反数分别是
$$
-n = \langle 0,n\rangle \text{当 } n \in Z_+,
$$

$$
-0 = 0,
$$

$$
-\langle 0,n\rangle = n \text{当 } n \in Z_+。
$$

**定义 12.1.3** 在集合 $Z$ 上定义小于等于关系 $\leq$ 为，对任意的 $x,y \in Z$，$x \leq y$ 当且仅当
$$
(x \in N \land y \in N \land x \leq y) \lor (x \in Z_- \land y \in N) \lor (x \in Z_- \land y \in Z_- \land -y \leq -x)。
$$
在集合 $Z$ 上定义小于关系 $<$ 为，对任意的 $x,y \in Z$，
$$
x < y \text{ 当且仅当 } (x \leq y) \land (x \neq y)。
$$

**定义 12.1.4** 等价关系 $\approx$ 对整数集合 $Z$，令
$$
Q_1 = Z \times (Z - \{0\}) = \{(a,b)| a \in Z \land b \in Z \land b \neq 0\},
$$
并称 $Q_1$ 是 $Z$ 上的因式的集合。对 $(a,b) \in Q_1$，可以用 $a/b$ 代替 $(a,b)$。在 $Q_1$ 上定义关系 $\approx$ 为，对任意的 $a/b \in Q_1$， $c/d \in Q_1$，
$$
a/b \approx c/d \text{ 当且仅当 } a \cdot d = b \cdot c。
$$
其中 $a \cdot b$ 是在 $Z$ 上定义的乘法，$=$ 是 $Z$ 上的相等关系。

**定理 12.1.1** 在 $Q_1$ 上的关系 $\approx$ 是等价关系。

**定义 12.1.5** 有理数集合 令 $Q = Q_1/\approx$，即 $Q$ 是集合 $Q_1$ 对等价关系 $\approx$ 的商集，则称 $Q$ 的元素为有理数，一般用 $a/b$ 表示 $Q$ 中的元素 $[a,b]_≈$。并习惯上取 $a, b$ 是互素的整数，且 $b > 0$。

**定义 12.1.6** 在 $Q$ 上定义小于等于关系 $\leq$ 为，对任意的 $a/b, c/d \in Q$，
$$
a/b \leq c/d \text{ 当且仅当 } a \cdot d \leq b \cdot c。
$$

**定义 12.1.7** 基本函数 如果 $f:N \rightarrow Q$ 满足条件：

(1) $(\exists x)(x \in Q \land (\forall n)(n \in N \rightarrow f(n) \leq x))$，

(2) $(\exists n)(n \in N \land (\forall m)(\forall i)((m \in N \land i \in N \land n \leq m \land n \leq i \land m \leq i) \rightarrow (f(m) \leq f(i))))$，

则称 $f$ 是一个基本函数，或有界非递减函数。当 $f$ 是一个基本函数时，则函数值
$$
f(0), f(1), f(2), \ldots, f(n), \ldots
$$
称为一个基本序列，它有时写为
$$
r_0, r_1, r_2, \cdots, r_n, \cdots。
$$
在以下定义与定理中，$B$ 表示所有基本函数的集合。$BF(f)$ 表示 $f$ 是一个基本函数。

**定理 12.1.2** 当 $f: N \to Q$ 取常数值时，$f$ 是基本函数。即对任意的 $r \in Q$，
$$
r, r, r, \cdots
$$
是一个基本序列。

**定理 12.1.3** 存在不是常值函数的基本函数。

**定义 12.1.8** 对基本函数的集合 $B$，定义 $B$ 上的关系 $\sim$ 为，对任意的 $f, g \in B$，$f \sim g$ 当且仅当
$$
(\forall \varepsilon)(\varepsilon \in Q \land \varepsilon > 0) \rightarrow (\exists n)(n \in N \land (\forall m)((m \in N \land n \leq m) \rightarrow |f(m)-g(m)| < \varepsilon))。
$$
直观上说，$f \sim g$ 等价于 $f$ 和 $g$ 的序列的极限相同。

**定理 12.1.4** $B$ 上的关系 $\sim$ 是等价关系。

**定理 12.1.5** 设 $f: N \to Q$ 和 $g: N \to Q$ 都是常值函数，且 $f \sim g$，则 $f = g$。

**定义 12.1.9** 实数集 令 $R = B / \sim$，即 $R$ 是集合 $B$ 对等价关系 $\sim$ 的商集，则称 $R$ 的元素为实数，称 $R$ 为实数集合。

**定义 12.1.10** 在 $B$ 上定义小于关系 $<_B$ 为，对任意的 $f, g \in B$，$f <_B g$ 当且仅当
$$
(\exists \varepsilon)(\varepsilon \in Q \land 0 < \varepsilon) \land (\exists n)(n \in N \land (\forall m)((m \in N \land n \leq m) \rightarrow g(m)-f(m) > \varepsilon)))。
$$

**定义 12.1.11** 在 $R$ 上定义小于等于关系 $\leq_R$ 和小于关系 $<_R$ 为，对任意的 $f, g \in B$，
$$
[f]_\sim \leq_R [g]_\sim \text{ 当且仅当 } f \leq_B g,
$$

$$
[f]_\sim <_R [g]_\sim \text{ 当且仅当 } f <_B g。
$$

## 12.2. 集合的等势

**定义 12.2.1** 集合的等势 对集合 $A$ 和 $B$，如果存在从 $A$ 到 $B$ 的双射函数，就称 $A$ 和 $B$ 等势，记作 $A \approx B$。如果不存在从 $A$ 到 $B$ 的双射函数，就称 $A$ 和 $B$ 不等势，记作 $\neg A \approx B$。

**定理 12.2.1** 对任意的集合 $A$，有
$$
P(A) \approx A_2。
$$

**定理 12.2.2** 对任意的集合 $ A, B $ 和 $C$，

(1) $A \approx A$，

(2) 若 $A \approx B$，则 $B \approx A$，

(3) 若 $A \approx B \land B \approx C$，则 $A \approx C$。

**定理 12.2.3** 康托尔定理

(1) $\neg N \approx R$，

(2) 对任意的集合 $A$，$\neg A \approx P(A)$。

## 12.3. 有限集合与无限集合

**定义 12.3.1** （有限集合与无限集合） 集合 $A$ 是有限集合，当且仅当存在 $n \in N$，使 $n \approx A$。集合 $A$ 是无限集合当且仅当 $A$ 不是有限集合，即不存在 $n \in N$ 使 $n \approx A$。

**定理 12.3.1** 不存在与自己的真子集等势的自然数。

**推论 12.3.1** 不存在与自己的真子集等势的有限集合。

**推论 12.3.2** 任何与自己的真子集等势的集合是无限集合。$N$ 和 $R$ 都是无限集合。

**推论 12.3.3** 任何有限集合只与唯一的自然数等势。

## 12.4. 集合的基数

**定义 12.4.1** 对任意的集合 $A$ 和 $B$，它们的基数分别用 $\text{card}(A)$ 和 $\text{card}(B)$ 表示，并且 $\text{card}(A) = \text{card}(B) \Leftrightarrow A \approx B$。（有时把 $\text{card}(A)$ 记作 $|A|$ 或 $\#(A)$。） 对有限集合 $A$ 和 $n \in N$，若 $A \approx n$，则
$$
\text{card}(A) = n。
$$

1. （自然数集合 $N$ 的基数） $N$ 的基数不是自然数，因为 $N$ 不与任何自然数等势。通常用康托尔的记法，把 $\text{card}(N)$ 记作 $\aleph_0$，读作“阿列夫零”。因此，
   $$
   \text{card}(Z) = \text{card}(Q) = \text{card}(N \times N) = \aleph_0。
   $$

2. （实数集合 $R$ 的基数） $R$ 的基数不是自然数，也不是 $\aleph_0$（因为 $\neg R \approx N$）。通常把 $\text{card}(R)$ 记作 $\aleph_1$，读作“阿列夫壹”。因此，
   $$
   \text{card}([0,1]) = \text{card}((0,1)) = \text{card}(\mathbb{R}_+) = \aleph_1。
   $$

## 12.5. 基数的算术运算

**定义 12.5.1** 对任意的基数 $k$ 和 $l$，

   （1）若存在集合 $K$ 和 $L$，$K \cap L = \emptyset$，$\text{card}(K) = k, \text{card}(L) = l$，则
$$
   k + l = \text{card}(K \cup L)。
$$
   （2）若存在集合 $K$ 和 $L$，$\text{card}(K) = k, \text{card}(L) = l$，则
$$
   k \cdot l = \text{card}(K \times L)。
$$
   （3）若存在集合 $K$ 和 $L$，$\text{card}(K) = k, \text{card}(L) = l$，则
$$
   k^l = \text{card}(L_K)，
$$
   其中 $L_K$ 是从 $L$ 到 $K$ 的函数的集合。

**定理 12.5.1** 对任意的基数 $k$、$l$ 和 $m$，

   （1）$k + l = l + k$， $k \cdot l = l \cdot k$，

   （2）$k + (l+m) = (k+l) + m$， $k \cdot (l \cdot m) = (k \cdot l) \cdot m$，

   （3）$k \cdot (l+m) = k \cdot l + k \cdot m$，

   （4）$k^{(l+m)} = k^l \cdot k^m$，

   （5）$(k \cdot l)^m = k^m \cdot l^m$，

   （6）$(k^l)^m = k^{(l \cdot m)}$。

## 12.6. 基数的比较

**定义 12.6.1** 对集合 $K$ 和 $L$，$\text{card}(K) = k, \text{card}(L) = l$，如果存在从 $K$ 到 $L$ 的单射函数，则称集合 $L$ 优于 $K$，记作 $K \preceq L$，且称基数 $k$ 不大于基数 $l$，记作 $k \leq l$。

**定义 12.6.2** 对基数 $k$ 和 $l$，如果 $k \leq l$ 且 $k \neq l$，则称 $k$ 小于 $l$，记作 $k < l$。

**定理 12.6.1** 对任意的基数 $k,l$ 和 $m$，

   （1）$k \leq k$，

   （2）若 $k \leq l$ 且 $l \leq m$，则 $k \leq m$，

   （3）若 $k \leq l$ 且 $l \leq k$ 则 $k = l$，

   （4）$k \leq l$ 或 $l \leq k$。

**定理 12.6.2** 对任意的基数 $k,l$ 和 $m$，如果 $k \leq l$，

   （1）$k + m \leq l + m$，

   （2）$k \cdot m \leq l \cdot m$，

   （3）$k^m \leq l^m$，

   （4）若 $k \neq 0$ 或 $m \neq 0$，则 $m^k \leq m^l$。

**定理 12.6.3** 对基数 $k$ 和 $l$，如果 $k \leq l$，$k \neq 0$，$l$ 是无限基数，则
$$
   k + l = k \cdot l = l = \max(k, l)。
$$

**定理 12.6.4**

   （1）对任意的无限集合 $K$，$N \preceq K$。

   （2）对任意的无限基数 $k$，$\aleph_0 \leq k$。

## 12.7. 可数集合与连续统假设

**定义 12.7.1** （可数集合） 对集合 $K$，如果 $\text{card}(K) \leq \aleph_0$，则称 $K$ 是可数集合。

**定理 12.7.1** （可数集的性质）

   （1）可数集的任何子集是可数集。

   （2）两个可数集的并集和笛卡儿积是可数集。

   （3）若 $K$ 是无限集合，则 $P(K)$ 是不可数的。

   （4）可数个可数集的并集是可数集（该结论可写为：若 $A$ 是可数集，$A$ 的元素都是可数集，则 $\cup A$ 是可数集）。

已知的基数按从小到大的次序排列就是
$$
0,1,\cdots,n,\cdots,\aleph_0,\aleph_1,2^{\aleph_0},\cdots。
$$

（连续统假设）“连续统假设”就是断言不存在基数 $k$，使
$$
\aleph_0 < k < 2^{\aleph_0}。
$$
这个假设至今未经过证明。有人已证明：根据现有的公理系统，既不能证明它是对的，也不能证明它是错的。
