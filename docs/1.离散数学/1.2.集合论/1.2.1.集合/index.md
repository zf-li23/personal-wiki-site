## 1.1. 集合的概念与表示方法

1.  **集合的概念** 集合是无法给出严格精确定义的最基本的数学概念。以下是两则典型的叙述。
    集合是一些确定的、可以区分的事物汇聚在一起组成的一个整体。组成一个集合的每个事物称为该集合的一个元素。
    吾人直观或思维之对象，如为相异而确定之物，其总括之全体即谓称集合，其组成此集合之物谓称集合之元素。

2.  **集合的元素与集合之间的关系** 一个集合的元素和该集合之间是隶属关系，即属于或不属于。若元素a属于集合A，记作 $a \in A$，否则记作 $a \notin A$。
    本书采用的体系中规定，集合的元素都是集合。同时为保持体系上的严谨性，规定：对任何集合 $A$ 都有 $A \notin A$。

3.  **集合的表示法** 表示一个集合的方法有两种：外延表示法和内涵表示法。外延表示法又称之为列元素法，即列出集合的所有元素。内涵表示法又称为谓词表示法，即用谓词来概括集合中元素的性质。一般而言，如果 $P(x)$ 表示一个谓词，则可以用 $\{ x | P(x) \} $ 或 $\{ x : P(x) \} $ 表示一个集合。$\{ x | P(x) \} $ 是使 $P(x)$ 为其所有元素x组成的集合。即若 $P(a)$ 为真，则a属于该集合。

## 1.2. 集合间的关系和特殊集合

**定义1.2.1. 集合的相等** 两个集合 $ A, B $ 相等，当且仅当它们具有相同的元素。若集合A和B相等，则记作 $ A = B $; 否则记作 $A \neq B$。该定义的符号化表示为
$$
A = B \Leftrightarrow (\forall x) (x \in A \Rightarrow x \in B)
$$

$$
A \neq B \Leftrightarrow (\exists x) \neg (x \in A \Rightarrow x \in B)
$$

**定义1.2.2. 子集** 设 $ A, B $ 为集合；若 $A$ 中的每个元素都是B的元素，则称 $A$ 为 $B$ 的子集合。简称子集。这时称 $B$ 包含 $A$ ，记作 $A \subseteq B$。该定义的符号化表示为
$$
A \subseteq B \Leftrightarrow (\forall x) (x \in A \Rightarrow x \in B)
$$

**定理1.2.1.** 两个集合相等的充要条件是它们互为子集。符号化表示为
$$
A = B \Leftrightarrow (A \subseteq B \land B \subseteq A)
$$

**定理1.2.2.** 对任意的集合 $A$ ,  $B$ 和 $ C $ ，包含关系分别具有下列性质：
(1) $A \subseteq A$ （自反性）。
(2) $(A \subseteq B \land B \subseteq A) \Rightarrow A = B$ （反对称性）。
(3) $(A \subseteq B \land B \subseteq C) \Rightarrow A \subseteq C$ （传递性）。

**定义1.2.3. 真子集** 对任意两个集合 $A$ 和 $B$ ，若 $A \subseteq B$ 且 $A \neq B$，则称 $A$ 是 $B$ 的真子集，或称 $B$ 真包含 $A$ 。记作 $A \subset B$。该定义的符号化表示为
$$
A \subset B \Leftrightarrow (A \subseteq B \land A \neq B)
$$

**定义1.2.4. 不相交** 若两个集合 $A$ 和 $B$ 没有公共元素，就称 $A$ 和 $B$ 是不相交的。该定义也可写成
$$
A \text{和} B \text{不相交} \Leftrightarrow (\exists x)(x \in A \land x \in B)
$$

**定义1.2.5. 空集** 不含任何元素的集合称为空集，记作 $\emptyset$。空集可符号化为
$$
\emptyset = \{ x | x \neq x \}
$$

**定理1.2.3.** 空集是一切集合的子集。即，对任意的集合A，$\emptyset \subseteq A$。

**定义1.2.6. 全集** 在给定的问题中，所考虑的所有事物的集合称为全集，记作E。该定义亦可叙述为：在一个具体问题中，如果所涉及的集合都是某个集合的子集，则称这个集合为全集。全集定义的符号化表示为
$$
E = \{ x | x = x \}
$$
全集是有相对性的，不同的问题有不同的全集。即使同一个问题也可以取不同的全集。

## 1.3. 集合的运算

**定义1.3.1. 集合的基本运算** 对集合 $A$ 和 $B$ ，集合的基本运算包括并，交，差(相对补)和对称差，分别定义如下。

(1) 并集 $ A \cup B $ 定义为 $ A \cup B = \{ x | x \in A \lor x \in B \} $。

(2) 交集 $A \cap B$ 定义为 $ A \cap B = \{ x | x \in A \land x \in B \} $。

(3) 差集 $A - B$ 定义为 $ A - B = \{ x | x \in A \land x \notin B \} $ (又称 $B$ 对 $A$ 的相对补集)。

(4) 余集 $- A$ 定义为 $ A - E = A - \{ x | x \notin A \} $ (其中 $E$ 为全集。 $A$ 的余集又称 $A$ 的绝对补集，也是 $A$ 对 $E$ 的相对补集)。

(5) 对称差 $ A \oplus B $ 定义为 $ A \oplus B = (A - B) \cup (B - A) = \{ x | x \in A \lor x \in B \} $。

**定义1.3.2. 广义并和广义交** 设 $A$ 为集合，A 的所有元素的元素组成的集合称为 $A$ 的广义并，记作 $\bigcup A$；设 $A$ 为非空集合，把 $A$ 的所有元素的公共元素组成的集合称为 $A$ 的广义交，记作 $\bigcap A$。分别用符号化表示为
$$
\bigcup A = \{ x | (\exists z)(z \in A \land x \in z) \},
$$

$$
\bigcap A = \{ x | (\forall z)(z \in A \rightarrow x \in z) \}.
$$

此外，对空集 $\emptyset$ 可以进行广义并， $\bigcup \emptyset = \emptyset$。但 $\bigcap \emptyset$ 不是集合，没有意义。

**定义1.3.3. 幂集** 设 $A$ 为集合，把 $A$ 的所有子集组成的集合称为 $A$ 的幂集，记作 $P(A)$ 。符号化表示为
$$
P(A) = \{ x | x \subseteq A \}.
$$
对任意的集合 $A$ ，有 $\emptyset \subseteq A$ 和 $A \subseteq A$，因此有 $\emptyset \in P(A)$ 和 $ A \in P(A)$。

1. **有序对** 由两个元素 $x$ 和 $y$  (允许 $x=y$ )按给定次序排列组成的二元组称为一个有序对或序偶，记作$ (x,y) $，其中x是它的第一元素，y是它的第二元素。
   有序对$ (x,y) $ 具有以下性质：
   (1) 当 $x \neq y$ 时，$ (x,y) \neq (y,x) $。
   (2) $ (x,y) = (u,v) $ 的充要条件是 $ x=u $ 且 $ y=v $。

   **定义1.3.4.** 用集合的形式，有序对$ (x,y) $定义为
   $$
   (x,y) = \{ \{ x \}, \{ x,y \} \}
   $$

   **定义1.3.5. n元组** 若 $n \in N$且 $n > 1, x_1, x_2, \cdots, x_n$是n个元素，则 $n$ 元组$ (x_1, x_2, \cdots, x_n) $定义为
       当$n=2$时，二元组是有序对$(x_1, x_2)$；
       当$n \neq 2$时，$ (x_1, x_2, \cdots, x_n) = \{ (x_1, x_2, \cdots, x_{n-1}), x_n \} $。

   **定义1.3.6. 集合A和B的笛卡儿积** 设 $ A, B $ 为集合，用 $A$ 中元素为第一元素， $B$ 中元素为第二元素构成有序对。所有这样的有序对组成的集合称为 $A$ 和 $B$ 的笛卡儿积，记作$A \times B$。$A$ 和 $B$ 的笛卡儿积的符号化表示为：
   $$
   A \times B = \{ (x,y) | x \in A \land y \in B \}
   $$

   **定义1.3.7. n阶笛卡儿积** 若$n \in N$，且$n > 1, A_1, A_2, \cdots, A_n$是n个集合，它们的n阶笛卡儿积记作$A_1 \times A_2 \times \cdots \times A_n$，并定义为：
   $$
   A_1 \times A_2 \times \cdots \times A_n = \{ (x_1, x_2, \cdots, x_n) | x_1 \in A_1 \land x_2 \in A_2 \land \cdots \land x_n \in A_n \}
   $$

2. **集合运算的优先顺序** 对集合运算的优先顺序做如下规定：
   称广义并，广义交，幂集，绝对补运算($\bigcup A, \bigcap A, P(A), -A$)为一类运算；
   并，交，对称差，笛卡儿积，相对补运算($\cup, \cap, \oplus, \times, -$)为二类运算。
   一类运算优先于二类运算；
   二类运算优先于集合关系运算($=, \subseteq, \subset, \in$)。
   同时，上述集合运算优先于逻辑运算($\neg, \land, \lor, \rightarrow, \leftrightarrow, \Rightarrow$)。
   括号内优先于括号外的；同一层括号内，相同优先级的，一类运算之间按由右向左顺序进行；其他按从左到右的顺序进行。

## 1.4. 集合的图形表示法

**文氏图(Venn Diagram)** 英国逻辑学家J.Venn(1834-1923)于1881年在《符号逻辑》一书中，首先使用相交区域的图解来说明类与类之间的关系。后来人们以他的名字来命名这种用图形来表示集合间的关系和集合的基本运算的方法。其构造如下：用一个大的矩形表示全集的所有元素(有时为简单起见，可将全集省略)。在矩形内画一些圆(或其他任何形状的闭曲线)，用圆的内部的点表示相应集合的元素。不同的圆代表不同的集合。用阴影或斜线的区域表示新组成的集合。文氏图的优点是形象直观，易于理解。缺点是理论基础不够严谨。因此只能用于说明，不能用于证明。

## 1.5. 集合运算的性质和证明

**定理1.5.1. 集合恒等式** 对任意的集合 $A$ ,  $B$ 和 $ C $ ，下列恒等式成立：

(1) **交换律** 
$$
A \cup B = B \cup A \\
A \cap B = B \cap A
$$

(2) **结合律**
$$
(A \cup B) \cup C = A \cup (B \cup C) \\
(A \cap B) \cap C = A \cap (B \cap C)
$$

(3) **分配律**
$$
A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \\
A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
$$

(4) **幂等律**
$$
A \cup A = A \\
A \cap A = A
$$

(5) **吸收律**
$$
A \cup (A \cap B) = A \\
A \cap (A \cup B) = A
$$

(6) **摩根律**
$$
A - (B \cup C) = (A - B) \cap (A - C) \\
A - (B \cap C) = (A - B) \cup (A - C) \\
- (B \cup C) = -B \cap -C \\
- (B \cap C) = -B \cup -C
$$

(7) **同一律**
$$
A \cup \emptyset = A \\
A \cap E = A
$$

(8) **零律**
$$
A \cup E = E \\
A \cap \emptyset = \emptyset
$$

(9) **补余律**
$$
A \cup -A = E \text{(排中律)} \\
A \cap -A = \emptyset \text{(矛盾律)}
$$
(10) **补律**
$$
-\emptyset = E \\
-E = \emptyset
$$

(11) **双补律**
$$
-(-A) = A
$$

**定理1.5.2. 差集的性质** 对任意的集合 $ A, B $ 和 $ C $，
$$
A - B = A - (A \cap B) \\
A - B = A \cap -B \\
A \cup (B - A) = A \cup B \\
A \cap (B - C) = (A \cap B) - C
$$

**定理1.5.3. 对称差的性质** 对任意的集合 $ A, B $ 和 $ C $，

(1) 交换律
$$
A \oplus B = B \oplus A
$$
(2) 结合律
$$
(A \oplus B) \oplus C = A \oplus (B \oplus C)
$$
(3) 分配律
$$
A \cap (B \oplus C) = (A \cap B) \oplus (A \cap C)
$$
(4) 同一律
$$
A \oplus \emptyset = A
$$
(5) 零律
$$
A \oplus A = \emptyset
$$
(6) 吸收律
$$
A \oplus (A \oplus B) = B
$$

**定理1.5.4. 集合间的包含关系的性质** 对任意的集合 $A, B, C$ 和 $ D $，
$$
A \subseteq B \Rightarrow (A \cup C) \subseteq (B \cup C) \\
A \subseteq B \Rightarrow (A \cap C) \subseteq (B \cap C) \\
(A \subseteq B) \land (C \subseteq D) \Rightarrow (A \cup C) \subseteq (B \cup D) \\
(A \subseteq B) \land (C \subseteq D) \Rightarrow (A \cap C) \subseteq (A \subseteq B) \land (C \subseteq D) \Rightarrow (A - D) \subseteq (B - C \subseteq D \Rightarrow (A - D) \subseteq (A - C)
$$

**定理1.5.5. 幂集合的性质1** 对任意的集合 $A$ 和 $B$ ，
$$
A \subseteq B \iff P(A) \subseteq P(B) \\
A = B \iff P(A) = P(B)
$$

**定理1.5.6. 幂集合的性质2** 对任意的集合 $A$ 和 $B$ ，
$$
P(A) \in P(B) \Rightarrow A \in B
$$

**定理1.5.7. 幂集合的性质3** 对任意的集合 $A$ 和 $B$ ，
$$
P(A) \cap P(B) = P(A \cap B) \\
P(A) \cup P(B) \subseteq P(A \cup B)
$$

**定理1.5.8. 幂集合的性质4** 对任意的集合 $A$ 和 $B$ ，
$$
P(A - B) \subseteq (P(A) - P(B)) \cup \{ \emptyset \}
$$

**定义1.5.1. 传递集合** 如果集合 $A$ 的任一元素的元素都是 $A$ 的元素，就称 $A$ 为传递集合。该定义也可写成
$$
A \text{是传递集合} \iff (\forall x)(\forall y)((x \in y \land y \in A) \rightarrow x \in A)
$$

**定理1.5.9. 传递集合的性质1** 对任意的集合 $A$ ,  $A$ 是传递集合 $\iff A \subseteq P(A)$。

**定理1.5.10. 传递集合的性质2** 对任意的集合 $A$ ,  $A$ 是传递集合 $\iff P(A)$ 是传递集合。

**定理1.5.11. 广义并和广义交的性质1** 对集合的集合 $A$ 和 $B$ ，
$$
A \subseteq B \Rightarrow \cup A \subseteq \cup B \\
A \subseteq B \Rightarrow \cap B \subseteq \cap A
$$

**定理1.5.12. 广义并和广义交的性质2** 对集合的集合 $A$ 和 $B$ ，
$$
\begin{align}
\cup (A \cup B) &= (\cup A) \cup (\cup B) \\
\cap (A \cup B) &= (\cap A) \cap (\cap B) \text{（其中A和B非空）}
\end{align}
$$

**定理1.5.13. 广义并和幂集运算的关系性质** 对任意的集合 $A$ ，
$$
\cup (P(A)) = A
$$

**定理1.5.14. 传递集合的性质3** 若集合 $A$ 是传递集合，则$\cup A$是传递集合。

**定理1.5.15. 传递集合的性质4** 若集合 $A$ 的元素都是传递集合，则$\cup A$是传递集合。

**定理1.5.16. 传递集合的性质5** 若非空集合 $A$ 是传递集合，则$\cap A$是传递集合，且$\cap A \subseteq \emptyset$。

**定理1.5.17. 传递集合的性质6** 若非空集合 $A$ 的元素都是传递集合，则$\cap A$是传递集合。

**定理1.5.18. 幂集的性质** 若A是集合，$x \in A, y \in A$，则 $(x,y) \in PP(A)$。($PP(A)$表示$P(P(A))$)。

**定理1.5.19. 笛卡儿积与$\cup$, $\cap$运算的性质** 对任意的集合 $ A, B $ 和 $ C $，
$$
A \times (B \cup C) = (A \times B) \cup (A \times C) \\
A \times (B \cap C) = (A \times B) \cap (A \times C) \\
(B \cup C) \times A = (B \times A) \cup (C \times A) \\
(B \cap C) \times A = (B \times A) \cap (C \times A)
$$

**定理1.5.20. 笛卡儿积与包含运算的性质1** 对任意的集合 $ A, B $ 和 $ C $，若$C \neq \emptyset$，则
$$
(A \subseteq B) \Leftrightarrow (A \times C \subseteq B \times C) \Leftrightarrow (C \times A \subseteq C \times B)
$$

**定理1.5.21. 笛卡儿积与包含运算的性质2** 对任意的集合 $A, B, C$ 和 $ D $，
$$
(A \times B \subseteq C \times D) \Leftrightarrow (A \subseteq C \land B \subseteq D)
$$

## 1.6. 有限集合的基数

**定义1.6.1. 有限集合的基数** 如果存在 $n \in N$，使集合 A 与集合 $\{x | x \in N \land x < n\} = \{0,1,2,\cdots,n-1\}$ 的元素个数相同，就说集合 A 的基数是 n，记作 $\|A\| = n$ 或 $\operatorname{card}(A) = n$。空集 $\emptyset$ 的基数是 0。

**定义1.6.2. 有限集合** 如果存在 $n \in N$，使 n 是集合 $A$ 的基数，就说 $A$ 是有限集合。如果不存在这样的 $n$ ，就说 $A$ 是无限集合。

**定理1.6.1. 幂集的基数** 对有限集合 $A$ ，
$$
\|P(A)\| = 2^{|A|}
$$

**定理1.6.2. 笛卡儿积的基数** 对有限集合 $A$ 和 $B$ ，
$$
\|A \times B\| = \|A\| \cdot \|B\|
$$

**定理1.6.3. 基本运算的基数** 对有限集合 $A$ 和 $B$ ，
$$
\|A\| \leq \|A\| + \|B\| \\
\|A \cap B\| \leq \min(\|A\|, \|B\|) \\
\|A-B\| \geq \|A\| - \|B\| \\
\|A \oplus B\| = \|A\| + \|B\| - 2 \|A \cap B\|
$$

**定理1.6.4. 包含排除原理** 对有限集合 $A$ 和 $B$ ，
$$
\|A \cup B\| = \|A\| + \|B\| - \|A \cap B\|
$$
该定理可推广到 n 个集合的情形。若 $n \in N$ 且 $n > 1, A_1, A_2, \cdots, A_n$ 是有限集合，则
$$
\|A_1 \cup A_2 \cup \cdots \cup A_n\| = \sum_{1 \leq i \leq n} \|A_i\| - \sum_{1 \leq i < j \leq n} \|A_i \cap A_j\| + \sum_{1 \leq i < j < k \leq n} \|A_i \cap A_j \cap A_k\| + \cdots + (-1)^{n-1} \|A_1 \cap A_2 \cap \cdots \cap A_n\|
$$

## 1.7. 集合论公理系统

1. **集合论公理系统** 集合论公理系统是一阶谓词公理系统的扩展，它包括一阶谓词公理系统和几个集合论公理。集合论公理系统可以推出一阶谓词的所有定理，也可以推出集合论的概念和定理。它从理论上防止了集合论中悖论的出现。
   集合论公理系统的一个基本思想是“任一集合的所有元素都是集合”。集合论研究的对象只是集合。除集合外的其他对象(如有序对，数字，字母)都要用集合定义。

2. **ZF (Zermelo-Fraenkel) 集合论公理系统** ZF 集合论公理系统由德国数学家 E. Zermelo 和 A. Fraenkel 提出，是一个非常著名的集合论公理系统。它包括 10 条集合论公理，但并非彼此独立。其中的无序对集合存在公理和子集公理模式可由其他公理推出。

   (1) **外延公理** 两集合相等的充要条件是它们恰好具有同样的元素。
   $$
   (\forall x)(\forall y)(x = y \Rightarrow (\forall z)(z \in x \Rightarrow z \in y))
   $$
   (2) **空集合存在公理** 存在不含任何元素的集合(空集$\emptyset$)。
   $$
   (\exists x)(\forall y)(y \notin x)
   $$
   (3) **无序对集合存在公理** 对任意的集合 $x$ 和 $y$，存在一个集合 $z$，它的元素恰好为 $x$ 和 $y$。
   $$
   (\forall x)(\forall y)(\exists z)(\forall u)(u \in z \leftrightarrow ((u = x) \lor (u = y)))
   $$
   (4) **并集合公理** 对任意的集合 $x$，存在一个集合 $y$，它的元素恰好为 $x$ 的元素的元素。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\exists u)(z \in u \land u \in x))
   $$
   (5) **子集公理模式(分离公理模式)** 对任意的谓词公式 $P(z)$，对任意的集合 $x$，存在一个集合 $y$，它的元素恰好既是 $x$ 的元素又使 $P(z)$ 为真。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (z \in x \land P(z)))
   $$
   (6) **幂集合公理(集合的幂集是集合)** 对任意的集合 $x$，存在一个集合 $y$，它的元素恰好是 $x$ 的子集。
   $$
   (\forall x)(\exists y)(\forall z)(z \in y \leftrightarrow (\forall u)(u \in z \leftrightarrow u \in x))
   $$
   (7) **正则公理** 对任意的非空集合 $x$，存在 $x$ 的一个元素，它和 $x$ 不相交。
   $$
   (\forall x)(x \neq \emptyset \rightarrow (\exists y)(y \in x \land (x \cap y = \emptyset)))
   $$
   (8) **无穷公理** 存在一个由所有自然数组成的集合。
   $$
   (\exists x)(\emptyset \in x \land (\forall y)(y \in x \rightarrow (y \cup \{y\}) \in x))
   $$
   (9) **替换公理模式** 对于任意的谓词公式 $P(x,y)$，如果对任意的 $x$ 存在唯一的 $y$ 使得 $P(x,y)$ 为真，那么对所有的集合 $t$ 就存在一个集合 $s$，使 $s$ 中的元素恰好是 $t$ 中元素 $x$ 所对应的那些 $y$。
   $$
   (\forall x)(\exists ! y)P(x,y) \rightarrow (\forall t)(\exists s)(\forall u)(u \in s \leftrightarrow (\exists z)(z \in t \land P(z,u)))
   $$
   其中 $(\exists ! y)$ 表示存在唯一的一个 $y$。
   (10) **选择公理** 对任意的关系 $R$，存在一个函数 $F$，$F$ 是 $R$ 的子集，而且 $F$ 和 $R$ 的定义域相等。
   $$
   (\forall \text{关系} R)(\exists \text{函数} F)(F \subseteq R \land dom(R) = dom(F))
   $$

**定理1.7.1. 交集存在定理** 对任意的集合 $A$ 和 $B$，交集 $A \cap B$ 是集合。

**定理1.7.2. 差集存在定理** 对任意的集合 $A$ 和 $B$，差集 $A - B$ 是集合。

**定理1.7.3. 广义交存在定理** 对任意的非空集合 $A$，广义交 $\bigcap A$ 是集合。

**定理1.7.4. 笛卡儿积存在定理** 对任意的集合 $A$ 和 $B$，笛卡儿积 $A \times B$ 是集合。

**定理1.7.5. 万有集不存在定理** 不存在集合 $A$，使任一集合都是 $A$ 的元素。

**定义1.7.1. 极小元** 对任意的集合 $A$ 和 $B$，当满足 $A \in B$ 且 $A \cap B = \emptyset$，就称 $A$ 为 $B$ 的一个极小元。

**定理1.7.6. 集合的重要性质 1** 对任意的集合 $A, A \notin A$。

**定理1.7.7. 集合的重要性质 2** 对任意的集合 $A$ 和 $B$，有 $ \neg (A \in B \land B \in A) $。

**定理1.7.8. 传递集合的性质 7** 对任意非空的传递集合 $A$，有 $\emptyset \in A$。

**定义1.7.2. 奇异集合** 如果集合 $A$ 中有集合的序列 $A_0 \in A, A_1 \in A, \cdots, A_n \in A, \cdots$，使得满足 $\cdots \in A_{n+1} \in A_n \in A_{n-1} \in \cdots \in A_2 \in A_1 \in A_0$，就称 $A$ 为奇异集合。

**定理1.7.9. 奇异集合的性质1** 奇异集合不满足正则公理。

**定理1.7.10. 奇异集合的性质2** 若非空集合 $A$ 不是奇异集合，则A满足正则公理。

**定义1.7.3. 前驱与后继** 对任意的集合 $A$ ，定义集合 $A^+ = A \cup \{A\}$，把 $A^+$ 称为 $A$ 的后继，A称为 $A^+$ 的前驱。

**定义1.7.4. 用后继定义自然数** 集合 $0=\emptyset$ 是一个自然数。若集合 $n$ 是一个自然数，则集合 $ n+1=n^+ $ 也是一个自然数。

**定义1.7.5. 自然数的性质1** 对任意的自然数 $m$ 和 $n$，
$$
m < n \Leftrightarrow m \subseteq n \Leftrightarrow n > m,
$$

$$
m \leq n \Leftrightarrow m \subseteq n \Leftrightarrow n \geq m.
$$

**定义1.7.6. 集合的三歧性** 对集合 $A$ ，如果对任意的集合 $ A_1 \in A $ 和 $ A_2 \in A $，使
$$
A_1 \in A_2, A_1 = A_2, A_2 \in A_1
$$
三式中恰好有一个成立，就称集合 $A$ 有三歧性。

**定理1.7.11. 自然数的三歧性** 集合 $N$ 有三歧性。每个自然数都有三歧性。即
$$
(\forall m)(\forall n) (m \in N \land n \in N \Rightarrow m < n \lor m = n \lor m > n)
$$
