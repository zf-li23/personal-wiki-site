---
title: 集合
---

本章介绍集合论的基本语言：集合的表示、集合间的关系、集合的运算及其运算律、有限集合的基数，最后简要介绍 ZF 集合论公理系统。后续各章的关系、函数和基数都建立在这些概念之上：有序对与笛卡儿积给出关系的定义，有限集合的基数则在第 4 章推广到任意集合。

## 1.1. 集合的概念与表示方法

**集合**（set）是无法给出严格精确定义的最基本的数学概念，通常用如下方式描述：集合是一些确定的、可以区分的事物汇聚在一起组成的一个整体；组成一个集合的每个事物称为该集合的一个**元素**。Cantor 的原始叙述（旧译）是：

> 吾人直观或思维之对象，如为相异而确定之物，其总括之全体即谓之集合，其组成此集合之物谓之集合之元素。

一个集合的元素和该集合之间是隶属关系，即属于或不属于。若元素 $a$ 属于集合 $A$，记作 $a \in A$，否则记作 $a \notin A$。本课程采用的公理体系中，集合的元素都是集合；并且对任何集合 $A$ 都有 $A \notin A$（见定理 1.7.6）。

表示一个集合的方法有两种：**外延表示法**和**内涵表示法**。外延表示法又称列元素法，即列出集合的所有元素；内涵表示法又称谓词表示法，即用谓词概括集合中元素的性质。一般地，若 $P(x)$ 是一个谓词，则用 $\{x \mid P(x)\}$ 或 $\{x : P(x)\}$ 表示使 $P(x)$ 为真的所有 $x$ 组成的集合，即：$a$ 属于该集合当且仅当 $P(a)$ 为真。

## 1.2. 集合间的关系和特殊集合

**定义 1.2.1（集合的相等）** 两个集合 $A, B$ 相等，当且仅当它们具有相同的元素。若集合 $A$ 和 $B$ 相等，则记作 $A = B$；否则记作 $A \neq B$。该定义的符号化表示为

$$
\begin{aligned}
A = B &\Leftrightarrow (\forall x)(x \in A \leftrightarrow x \in B), \\
A \neq B &\Leftrightarrow (\exists x)\lnot(x \in A \leftrightarrow x \in B).
\end{aligned}
$$

**定义 1.2.2（子集）** 设 $A, B$ 为集合。若 $A$ 中的每个元素都是 $B$ 的元素，则称 $A$ 为 $B$ 的子集合，简称子集，这时也称 $B$ 包含 $A$，记作 $A \subseteq B$。该定义的符号化表示为

$$
A \subseteq B \Leftrightarrow (\forall x)(x \in A \rightarrow x \in B).
$$

**定理 1.2.1** 两个集合相等的充要条件是它们互为子集，即

$$
A = B \Leftrightarrow (A \subseteq B \land B \subseteq A).
$$

**定理 1.2.2** 对任意的集合 $A$、$B$ 和 $C$，包含关系具有下列性质：

1. $A \subseteq A$（自反性）；
2. $(A \subseteq B \land B \subseteq A) \Rightarrow A = B$（反对称性）；
3. $(A \subseteq B \land B \subseteq C) \Rightarrow A \subseteq C$（传递性）。

**定义 1.2.3（真子集）** 对任意两个集合 $A$ 和 $B$，若 $A \subseteq B$ 且 $A \neq B$，则称 $A$ 是 $B$ 的真子集，或称 $B$ 真包含 $A$，记作 $A \subset B$。该定义的符号化表示为

$$
A \subset B \Leftrightarrow (A \subseteq B \land A \neq B).
$$

**定义 1.2.4（不相交）** 若两个集合 $A$ 和 $B$ 没有公共元素，就称 $A$ 和 $B$ 是不相交的。该定义也可写成

$$
A \text{ 和 } B \text{ 不相交} \Leftrightarrow \lnot(\exists x)(x \in A \land x \in B).
$$

**定义 1.2.5（空集）** 不含任何元素的集合称为空集，记作 $\emptyset$。空集可符号化为

$$
\emptyset = \{x \mid x \neq x\}.
$$

**定理 1.2.3** 空集是一切集合的子集，即对任意的集合 $A$，$\emptyset \subseteq A$。

**定义 1.2.6（全集）** 在给定的问题中，所考虑的所有事物组成的集合称为全集，记作 $E$。该定义亦可叙述为：在一个具体问题中，如果所涉及的集合都是某个集合的子集，则称这个集合为全集。全集的符号化表示为

$$
E = \{x \mid x = x\}.
$$

全集是相对的：不同的问题有不同的全集，即使同一个问题也可以取不同的全集。上式只是一种形式写法，由定理 1.7.5，不存在以一切集合为元素的集合，因此全集总是相对于具体问题取定的。

## 1.3. 集合的运算

**定义 1.3.1（集合的基本运算）** 对集合 $A$ 和 $B$，集合的基本运算包括并、交、差（相对补）、绝对补和对称差，分别定义如下：

1. 并集：$A \cup B = \{x \mid x \in A \lor x \in B\}$；
2. 交集：$A \cap B = \{x \mid x \in A \land x \in B\}$；
3. 差集：$A - B = \{x \mid x \in A \land x \notin B\}$，又称 $B$ 对 $A$ 的相对补集；
4. 余集：$-A = E - A = \{x \mid x \in E \land x \notin A\}$，其中 $E$ 为全集；$A$ 的余集又称 $A$ 的绝对补集，即 $A$ 对 $E$ 的相对补集；
5. 对称差：$A \oplus B = (A - B) \cup (B - A) = \{x \mid (x \in A \land x \notin B) \lor (x \notin A \land x \in B)\}$。

**定义 1.3.2（广义并和广义交）** 设 $A$ 为集合，$A$ 的所有元素的元素组成的集合称为 $A$ 的广义并，记作 $\bigcup A$；设 $A$ 为非空集合，$A$ 的所有元素的公共元素组成的集合称为 $A$ 的广义交，记作 $\bigcap A$。符号化表示为

$$
\begin{aligned}
\bigcup A &= \{x \mid (\exists z)(z \in A \land x \in z)\}, \\
\bigcap A &= \{x \mid (\forall z)(z \in A \rightarrow x \in z)\}.
\end{aligned}
$$

对空集也可以作广义并：$\bigcup \emptyset = \emptyset$。但 $\bigcap \emptyset$ 不是集合（按上式它将包含一切集合），没有意义。

**定义 1.3.3（幂集）** 设 $A$ 为集合，$A$ 的所有子集组成的集合称为 $A$ 的幂集，记作 $P(A)$。符号化表示为

$$
P(A) = \{x \mid x \subseteq A\}.
$$

对任意的集合 $A$，有 $\emptyset \subseteq A$ 和 $A \subseteq A$，因此 $\emptyset \in P(A)$，$A \in P(A)$。

由两个元素 $x$ 和 $y$（允许 $x = y$）按给定次序排列组成的二元组称为一个**有序对**（ordered pair）或序偶，记作 $\langle x, y \rangle$，其中 $x$ 是它的第一元素，$y$ 是它的第二元素。有序对具有以下性质：

1. 当 $x \neq y$ 时，$\langle x, y \rangle \neq \langle y, x \rangle$；
2. $\langle x, y \rangle = \langle u, v \rangle$ 的充要条件是 $x = u$ 且 $y = v$。

**定义 1.3.4（有序对）** 用集合的形式，有序对 $\langle x, y \rangle$ 定义为

$$
\langle x, y \rangle = \{\{x\}, \{x, y\}\}.
$$

**定义 1.3.5（$n$ 元组）** 若 $n \in \mathbb{N}$，$n > 1$，$x_1, x_2, \cdots, x_n$ 是 $n$ 个元素，则 $n$ 元组 $\langle x_1, x_2, \cdots, x_n \rangle$ 定义为：当 $n = 2$ 时，二元组是有序对 $\langle x_1, x_2 \rangle$；当 $n > 2$ 时，

$$
\langle x_1, x_2, \cdots, x_n \rangle = \langle \langle x_1, x_2, \cdots, x_{n-1} \rangle, x_n \rangle.
$$

**定义 1.3.6（笛卡儿积）** 设 $A, B$ 为集合，以 $A$ 中元素为第一元素、$B$ 中元素为第二元素构成有序对，所有这样的有序对组成的集合称为 $A$ 和 $B$ 的笛卡儿积，记作 $A \times B$。符号化表示为

$$
A \times B = \{\langle x, y \rangle \mid x \in A \land y \in B\}.
$$

**定义 1.3.7（$n$ 阶笛卡儿积）** 若 $n \in \mathbb{N}$，$n > 1$，$A_1, A_2, \cdots, A_n$ 是 $n$ 个集合，它们的 $n$ 阶笛卡儿积记作 $A_1 \times A_2 \times \cdots \times A_n$，定义为

$$
A_1 \times A_2 \times \cdots \times A_n = \{\langle x_1, x_2, \cdots, x_n \rangle \mid x_1 \in A_1 \land x_2 \in A_2 \land \cdots \land x_n \in A_n\}.
$$

集合运算的优先顺序规定如下：

- 广义并、广义交、幂集、绝对补（$\bigcup A, \bigcap A, P(A), -A$）为一类运算；并、交、对称差、笛卡儿积、相对补（$\cup, \cap, \oplus, \times, -$）为二类运算。
- 一类运算优先于二类运算；二类运算优先于集合关系运算（$=, \subseteq, \subset, \in$）；上述集合运算都优先于逻辑运算（$\lnot, \land, \lor, \rightarrow, \leftrightarrow, \Rightarrow$）。
- 括号内优先于括号外；同一层括号内优先级相同时，一类运算之间按由右向左的顺序进行，其他按由左向右的顺序进行。

## 1.4. 集合的图形表示法

**文氏图**（Venn diagram）由英国逻辑学家 J. Venn（1834–1923）引入，他在 1881 年出版的《符号逻辑》中用相交区域的图解说明类与类之间的关系，后人便以他的名字命名这种用图形表示集合间关系和集合运算的方法。其画法是：用一个大矩形表示全集（有时为简单起见可省略），在矩形内画一些圆（或其他闭曲线），用圆内部的点表示相应集合的元素，不同的圆代表不同的集合，用阴影区域表示运算得到的新集合。文氏图形象直观、易于理解，但缺乏严格的理论基础，因此只能用于说明，不能用于证明。

## 1.5. 集合运算的性质和证明

**定理 1.5.1（集合恒等式）** 对任意的集合 $A$、$B$ 和 $C$，下列恒等式成立：

1. 交换律：$A \cup B = B \cup A$，$A \cap B = B \cap A$。
2. 结合律：$(A \cup B) \cup C = A \cup (B \cup C)$，$(A \cap B) \cap C = A \cap (B \cap C)$。
3. 分配律：$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$，$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$。
4. 幂等律：$A \cup A = A$，$A \cap A = A$。
5. 吸收律：$A \cup (A \cap B) = A$，$A \cap (A \cup B) = A$。
6. De Morgan 律：
   $$
   \begin{aligned}
   A - (B \cup C) &= (A - B) \cap (A - C), & A - (B \cap C) &= (A - B) \cup (A - C), \\
   -(B \cup C) &= -B \cap -C, & -(B \cap C) &= -B \cup -C.
   \end{aligned}
   $$
7. 同一律：$A \cup \emptyset = A$，$A \cap E = A$。
8. 零律：$A \cup E = E$，$A \cap \emptyset = \emptyset$。
9. 补余律：$A \cup -A = E$（排中律），$A \cap -A = \emptyset$（矛盾律）。
10. 补律：$-\emptyset = E$，$-E = \emptyset$。
11. 双补律：$-(-A) = A$。

**定理 1.5.2（差集的性质）** 对任意的集合 $A$、$B$ 和 $C$，

$$
\begin{aligned}
A - B &= A - (A \cap B), \\
A - B &= A \cap -B, \\
A \cup (B - A) &= A \cup B, \\
A \cap (B - C) &= (A \cap B) - C.
\end{aligned}
$$

**定理 1.5.3（对称差的性质）** 对任意的集合 $A$、$B$ 和 $C$，

1. 交换律：$A \oplus B = B \oplus A$；
2. 结合律：$(A \oplus B) \oplus C = A \oplus (B \oplus C)$；
3. 分配律：$A \cap (B \oplus C) = (A \cap B) \oplus (A \cap C)$；
4. 同一律：$A \oplus \emptyset = A$；
5. 零律：$A \oplus A = \emptyset$；
6. 吸收律：$A \oplus (A \oplus B) = B$。

**定理 1.5.4（包含关系的性质）** 对任意的集合 $A$、$B$、$C$ 和 $D$，

$$
\begin{aligned}
A \subseteq B &\Rightarrow A \cup C \subseteq B \cup C, \\
A \subseteq B &\Rightarrow A \cap C \subseteq B \cap C, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A \cup C \subseteq B \cup D, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A \cap C \subseteq B \cap D, \\
(A \subseteq B) \land (C \subseteq D) &\Rightarrow A - D \subseteq B - C, \\
C \subseteq D &\Rightarrow A - D \subseteq A - C.
\end{aligned}
$$

**定理 1.5.5（幂集的性质 1）** 对任意的集合 $A$ 和 $B$，

$$
\begin{aligned}
A \subseteq B &\Leftrightarrow P(A) \subseteq P(B), \\
A = B &\Leftrightarrow P(A) = P(B).
\end{aligned}
$$

**定理 1.5.6（幂集的性质 2）** 对任意的集合 $A$ 和 $B$，

$$
P(A) \in P(B) \Rightarrow A \in B.
$$

**定理 1.5.7（幂集的性质 3）** 对任意的集合 $A$ 和 $B$，

$$
\begin{aligned}
P(A) \cap P(B) &= P(A \cap B), \\
P(A) \cup P(B) &\subseteq P(A \cup B).
\end{aligned}
$$

**定理 1.5.8（幂集的性质 4）** 对任意的集合 $A$ 和 $B$，

$$
P(A - B) \subseteq (P(A) - P(B)) \cup \{\emptyset\}.
$$

**定义 1.5.1（传递集合）** 如果集合 $A$ 的任一元素的元素都是 $A$ 的元素，就称 $A$ 为传递集合。该定义也可写成

$$
A \text{ 是传递集合} \Leftrightarrow (\forall x)(\forall y)((x \in y \land y \in A) \rightarrow x \in A).
$$

**定理 1.5.9（传递集合的性质 1）** 对任意的集合 $A$，$A$ 是传递集合 $\Leftrightarrow A \subseteq P(A)$。

**定理 1.5.10（传递集合的性质 2）** 对任意的集合 $A$，$A$ 是传递集合 $\Leftrightarrow P(A)$ 是传递集合。

**定理 1.5.11（广义并和广义交的性质 1）** 对集合族 $A$ 和 $B$，

$$
\begin{aligned}
A \subseteq B &\Rightarrow \textstyle\bigcup A \subseteq \bigcup B, \\
A \subseteq B &\Rightarrow \textstyle\bigcap B \subseteq \bigcap A \quad (A \neq \emptyset).
\end{aligned}
$$

**定理 1.5.12（广义并和广义交的性质 2）** 对集合族 $A$ 和 $B$，

$$
\begin{aligned}
\textstyle\bigcup (A \cup B) &= \left(\textstyle\bigcup A\right) \cup \left(\textstyle\bigcup B\right), \\
\textstyle\bigcap (A \cup B) &= \left(\textstyle\bigcap A\right) \cap \left(\textstyle\bigcap B\right) \quad (A \neq \emptyset,\ B \neq \emptyset).
\end{aligned}
$$

**定理 1.5.13（广义并与幂集的关系）** 对任意的集合 $A$，

$$
\textstyle\bigcup P(A) = A.
$$

**定理 1.5.14（传递集合的性质 3）** 若集合 $A$ 是传递集合，则 $\bigcup A$ 是传递集合。

**定理 1.5.15（传递集合的性质 4）** 若集合 $A$ 的元素都是传递集合，则 $\bigcup A$ 是传递集合。

**定理 1.5.16（传递集合的性质 5）** 若非空集合 $A$ 是传递集合，则 $\bigcap A = \emptyset$，从而 $\bigcap A$ 是传递集合。

后一结论用到了正则公理：由定理 1.7.8，非空传递集合 $A$ 含有 $\emptyset$，故 $\bigcap A \subseteq \emptyset$。

**定理 1.5.17（传递集合的性质 6）** 若非空集合 $A$ 的元素都是传递集合，则 $\bigcap A$ 是传递集合。

**定理 1.5.18（有序对与幂集）** 若 $A$ 是集合，$x \in A$，$y \in A$，则 $\langle x, y \rangle \in P(P(A))$。

**定理 1.5.19（笛卡儿积对并、交的分配律）** 对任意的集合 $A$、$B$ 和 $C$，

$$
\begin{aligned}
A \times (B \cup C) &= (A \times B) \cup (A \times C), \\
A \times (B \cap C) &= (A \times B) \cap (A \times C), \\
(B \cup C) \times A &= (B \times A) \cup (C \times A), \\
(B \cap C) \times A &= (B \times A) \cap (C \times A).
\end{aligned}
$$

**定理 1.5.20（笛卡儿积与包含关系的性质 1）** 对任意的集合 $A$、$B$ 和 $C$，若 $C \neq \emptyset$，则

$$
A \subseteq B \Leftrightarrow A \times C \subseteq B \times C \Leftrightarrow C \times A \subseteq C \times B.
$$

**定理 1.5.21（笛卡儿积与包含关系的性质 2）** 对任意的非空集合 $A$、$B$ 和任意的集合 $C$、$D$，

$$
A \times B \subseteq C \times D \Leftrightarrow (A \subseteq C \land B \subseteq D).
$$

非空条件不能去掉：若 $A = \emptyset$，则 $A \times B = \emptyset \subseteq C \times D$ 总成立，而 $B \subseteq D$ 未必成立。

## 1.6. 有限集合的基数

**定义 1.6.1（有限集合的基数）** 如果存在 $n \in \mathbb{N}$，使集合 $A$ 与集合 $\{x \mid x \in \mathbb{N} \land x < n\} = \{0, 1, \cdots, n - 1\}$ 之间存在双射（即二者等势，见定义 4.2.1），就说集合 $A$ 的基数是 $n$，记作 $|A| = n$ 或 $\operatorname{card}(A) = n$。空集 $\emptyset$ 的基数是 $0$。

**定义 1.6.2（有限集合）** 如果存在 $n \in \mathbb{N}$，使 $n$ 是集合 $A$ 的基数，就说 $A$ 是有限集合；如果不存在这样的 $n$，就说 $A$ 是无限集合。

**定理 1.6.1（幂集的基数）** 对有限集合 $A$，

$$
|P(A)| = 2^{|A|}.
$$

**定理 1.6.2（笛卡儿积的基数）** 对有限集合 $A$ 和 $B$，

$$
|A \times B| = |A| \cdot |B|.
$$

**定理 1.6.3（基本运算的基数）** 对有限集合 $A$ 和 $B$，

$$
\begin{aligned}
|A \cup B| &\leq |A| + |B|, \\
|A \cap B| &\leq \min(|A|, |B|), \\
|A - B| &\geq |A| - |B|, \\
|A \oplus B| &= |A| + |B| - 2|A \cap B|.
\end{aligned}
$$

**定理 1.6.4（包含排除原理）** 对有限集合 $A$ 和 $B$，

$$
|A \cup B| = |A| + |B| - |A \cap B|.
$$

该定理可推广到 $n$ 个集合的情形：若 $n \in \mathbb{N}$，$n > 1$，$A_1, A_2, \cdots, A_n$ 是有限集合，则

$$
\begin{aligned}
|A_1 \cup A_2 \cup \cdots \cup A_n| ={} & \sum_{1 \leq i \leq n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i \cap A_j| + \sum_{1 \leq i < j < k \leq n} |A_i \cap A_j \cap A_k| \\
& - \cdots + (-1)^{n-1} |A_1 \cap A_2 \cap \cdots \cap A_n|.
\end{aligned}
$$

**例 1.6.1** 在 $1$ 到 $100$ 的整数中，能被 $2$、$3$ 或 $5$ 整除的数有多少个？记 $A_d$ 为其中能被 $d$ 整除的数的集合，则

$$
\begin{aligned}
|A_2 \cup A_3 \cup A_5| &= (50 + 33 + 20) - (16 + 10 + 6) + 3 \\
&= 103 - 32 + 3 = 74.
\end{aligned}
$$

## 1.7. 集合论公理系统

集合论公理系统是[一阶谓词逻辑](/1.1.4)公理系统的扩展，它包括一阶谓词公理系统和若干集合论公理。由它既可以推出一阶谓词逻辑的所有定理，也可以推出集合论的概念和定理，并从理论上防止了集合论悖论的出现。集合论公理系统的一个基本思想是"任一集合的所有元素都是集合"：集合论研究的对象只是集合，其他对象（如有序对、数字、字母）都要用集合来定义。

ZF（Zermelo–Fraenkel）集合论公理系统由德国数学家 E. Zermelo 和 A. Fraenkel 提出，是最著名的集合论公理系统。下面列出 10 条公理（前 9 条构成 ZF，加上选择公理即 ZFC），它们并非彼此独立，例如无序对集合存在公理和子集公理模式可由其他公理推出。

1. **外延公理** 两个集合相等的充要条件是它们恰好具有同样的元素。
   $$
   (\forall x)(\forall y)((\forall z)(z \in x \leftrightarrow z \in y) \rightarrow x = y)
   $$
2. **空集合存在公理** 存在不含任何元素的集合（空集 $\emptyset$）。
   $$
   (\exists x)(\forall y)(y \notin x)
   $$
3. **无序对集合存在公理** 对任意的集合 $x$ 和 $y$，存在一个集合 $z$，它的元素恰好为 $x$ 和 $y$。
   $$
   (\forall x)(\forall y)(\exists z)(\forall u)(u \in z \leftrightarrow (u = x \lor u = y))
   $$
4. **并集合公理** 对任意的集合 $x$，存在一个集合 $y$，它的元素恰好为 $x$ 的元素的元素。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\exists u)(z \in u \land u \in x))
   $$
5. **子集公理模式**（分离公理模式） 对任意的谓词公式 $P(z)$ 和任意的集合 $x$，存在一个集合 $y$，它的元素恰好是 $x$ 中使 $P(z)$ 为真的元素。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (z \in x \land P(z)))
   $$
6. **幂集合公理** 对任意的集合 $x$，存在一个集合 $y$，它的元素恰好是 $x$ 的子集。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\forall u)(u \in z \rightarrow u \in x))
   $$
7. **正则公理** 对任意的非空集合 $x$，存在 $x$ 的一个元素，它和 $x$ 不相交。
   $$
   (\forall x)(x \neq \emptyset \rightarrow (\exists y)(y \in x \land x \cap y = \emptyset))
   $$
8. **无穷公理** 存在一个集合，它含有 $\emptyset$，并且对它的任一元素 $y$ 也含有 $y \cup \{y\}$；因此它含有全部自然数（见定义 1.7.4）。
   $$
   (\exists x)(\emptyset \in x \land (\forall y)(y \in x \rightarrow y \cup \{y\} \in x))
   $$
9. **替换公理模式** 对任意的谓词公式 $P(x, y)$，如果对任意的 $x$ 存在唯一的 $y$ 使 $P(x, y)$ 为真，那么对任意的集合 $t$ 存在一个集合 $s$，$s$ 的元素恰好是 $t$ 中元素 $x$ 所对应的那些 $y$。
   $$
   (\forall x)(\exists ! y)P(x, y) \rightarrow (\forall t)(\exists s)(\forall u)(u \in s \leftrightarrow (\exists z)(z \in t \land P(z, u)))
   $$
   其中 $(\exists ! y)$ 表示存在唯一的 $y$。
10. **选择公理**（axiom of choice） 对任意的关系 $R$，存在一个函数 $F$，$F$ 是 $R$ 的子集，而且 $F$ 和 $R$ 的定义域相等。
    $$
    (\forall \text{关系 } R)(\exists \text{函数 } F)(F \subseteq R \land \operatorname{dom}(F) = \operatorname{dom}(R))
    $$

**定理 1.7.1（交集存在定理）** 对任意的集合 $A$ 和 $B$，交集 $A \cap B$ 是集合。

**定理 1.7.2（差集存在定理）** 对任意的集合 $A$ 和 $B$，差集 $A - B$ 是集合。

**定理 1.7.3（广义交存在定理）** 对任意的非空集合 $A$，广义交 $\bigcap A$ 是集合。

**定理 1.7.4（笛卡儿积存在定理）** 对任意的集合 $A$ 和 $B$，笛卡儿积 $A \times B$ 是集合。

**定理 1.7.5（万有集不存在定理）** 不存在集合 $A$，使任一集合都是 $A$ 的元素。

**定义 1.7.1（$\in$-极小元）** 对任意的集合 $A$ 和 $B$，若 $A \in B$ 且 $A \cap B = \emptyset$，就称 $A$ 为 $B$ 的一个 $\in$-极小元。正则公理即断言：每个非空集合都有 $\in$-极小元。

**定理 1.7.6（集合的重要性质 1）** 对任意的集合 $A$，$A \notin A$。

**定理 1.7.7（集合的重要性质 2）** 对任意的集合 $A$ 和 $B$，$\lnot(A \in B \land B \in A)$。

**定理 1.7.8（传递集合的性质 7）** 对任意非空的传递集合 $A$，有 $\emptyset \in A$。

**定义 1.7.2（奇异集合）** 如果集合 $A$ 中有集合的序列 $A_0, A_1, \cdots, A_n, \cdots$（每个 $A_n \in A$），使得

$$
\cdots \in A_{n+1} \in A_n \in A_{n-1} \in \cdots \in A_2 \in A_1 \in A_0,
$$

就称 $A$ 为奇异集合。

**定理 1.7.9（奇异集合的性质 1）** 奇异集合的存在与正则公理矛盾：若 $A$ 是奇异集合，则非空集合 $\{A_0, A_1, \cdots\}$ 没有 $\in$-极小元。因此在 ZF 中不存在奇异集合。

**定理 1.7.10（奇异集合的性质 2）** 若非空集合 $A$ 不是奇异集合，则 $A$ 满足正则公理的结论，即 $A$ 有 $\in$-极小元。

**定义 1.7.3（前驱与后继）** 对任意的集合 $A$，定义集合 $A^+ = A \cup \{A\}$，称 $A^+$ 为 $A$ 的后继，称 $A$ 为 $A^+$ 的前驱。

**定义 1.7.4（用后继定义自然数）** 集合 $0 = \emptyset$ 是一个自然数；若集合 $n$ 是一个自然数，则集合 $n + 1 = n^+$ 也是一个自然数；自然数只有这样得到的集合。于是 $1 = \{0\}$，$2 = \{0, 1\}$，一般地 $n = \{0, 1, \cdots, n - 1\}$。

**定义 1.7.5（自然数的大小）** 对任意的自然数 $m$ 和 $n$，

$$
\begin{aligned}
m < n &\Leftrightarrow m \in n \Leftrightarrow n > m, \\
m \leq n &\Leftrightarrow m \subseteq n \Leftrightarrow n \geq m.
\end{aligned}
$$

由于 $n = \{0, 1, \cdots, n - 1\}$，对自然数有 $m \subseteq n \Leftrightarrow (m \in n \lor m = n)$，两式相容。

**定义 1.7.6（集合的三歧性）** 对集合 $A$，如果对任意的 $A_1 \in A$ 和 $A_2 \in A$，

$$
A_1 \in A_2, \quad A_1 = A_2, \quad A_2 \in A_1
$$

三式中恰好有一个成立，就称集合 $A$ 有三歧性。

**定理 1.7.11（自然数的三歧性）** 集合 $\mathbb{N}$ 有三歧性，每个自然数也都有三歧性，即

$$
(\forall m)(\forall n)(m \in \mathbb{N} \land n \in \mathbb{N} \rightarrow m < n \lor m = n \lor m > n).
$$
