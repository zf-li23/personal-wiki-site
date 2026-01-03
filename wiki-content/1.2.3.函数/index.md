## 3.1. 函数和选择公理

**定义 3.1.1** **函数** 对集合 $A$ 到集合 $B$ 的关系 $f$，若满足下列条件：

(1) 对任意的 $x \in \text{dom}(f)$，存在唯一的 $y \in \text{ran}(f)$，使 $x f y$ 成立；

(2) $\text{dom}(f)=A$

则称 $f$ 为从 $A$ 到 $B$ 的函数，或称 $f$ 把 $A$ 映射到 $B$（有的 $B$ 称为全函数，映射，变换）。一个从 $A$ 到 $B$ 的函数 $f$，可以写成 $f:A \rightarrow B$。这时若 $x f y$，则可记作 $f:x \rightarrow y$ 或 $f(x)=y$。

函数的两个条件可以写成

(1) $( \forall x)( \forall y_1 )( \forall y_2 )( (x f y_1 \land x f y_2 ) \rightarrow y_1 = y_2 )$。

(2) $( \forall x)( x \in A \rightarrow (\exists y)( y \in B \land x f y))$。

**定义 3.1.2** **从 $A$ 到 $B$ 的所有函数的集合 $A_B$** 对集合 $A$ 和 $B$，从 $A$ 到 $B$ 的所有函数的集合记为 $A_B$（有的书记为 $B^A$），于是 $A_B = \{ f | f : A \rightarrow B \}$。
若 $A$ 和 $B$ 是有限集合，且 $|A|=m,|B|=n$，则 $|A_B|=n^m$。

**定义 3.1.3** **函数的象** 设 $f:A \rightarrow B, A_i \subseteq A$，定义 $A_i$ 在 $f$ 下的象 $f[A_i]$ 为
$$
f[A_i] = \{ y | (\exists x)( x \in A_i \land y = f(x)) \}
$$
把 $f[A]$ 称为函数的象。

设 $B_i \subseteq B$，定义 $B_i$ 在 $f$ 下的完全原象 $f^{-1}[B_i]$ 为
$$
f^{-1}[B_i] = \{ x | x \in A \land f(x) \in B_i \}
$$

**定义 3.1.4** **满射 单射 双射** 设 $f:A \rightarrow B$，

(1) 若 $\text{ran}(f)=B$，则称 $f$ 是满射的，或称 $f$ 是 $A$ 到 $B$ 上的；

(2) 若对任意的 $x_1,x_2 \in A, x_1 \neq x_2$，都有 $f(x_1) \neq f(x_2)$，则称 $f$ 是单射的，或内射的，或一对一的；

(3) 若 $f$ 是满射的又是单射的，则称 $f$ 是双射的，或一对一 $A$ 到 $B$ 上的。简称双射。

**定义 3.1.5** **常函数** 设 $f:A \rightarrow B$。如果存在一个 $y \in B$，使得对所有的 $x \in A$，有 $f(x)=y$，即 $f[A]=\{ y \}$，则称 $f:A \rightarrow B$ 为常函数。

**定义 3.1.6** **恒等函数** $A$ 上的恒等关系 $I_A: A \rightarrow A$ 称为恒等函数。于是，对任意的 $x \in A$，有 $I_A(x)=x$。

**定义 3.1.7** **单调函数** 对实数集 $R$，设 $f:R \rightarrow R$，如果 $(x \leq y) \rightarrow (f(x) \leq f(y))$，则称 $f$ 为单调递增的；如果 $(x \leq y) \rightarrow (f(x) \leq f(y))$，则称 $f$ 为严格单调递增的。类似可定义单调递减和严格单调递减的函数。

**定义 3.1.8** **$n$ 元运算** 对集合 $A, n \in N$，把函数 $f:A^n \rightarrow A$ 称为 $A$ 上的 $n$ 元运算。

**定义 3.1.9** **泛函** 设 $A,B,C$ 是集合 $B_C$ 为从 $B$ 到 $C$ 的所有函数的集合，则 $F:A \rightarrow B_C$ 称为一个泛函（有时将 $G:B_C \rightarrow A$ 称为一个泛函）。

**定义 3.1.10** **特征函数** 设 $E$ 是全集，对任意的 $A \subseteq E$，$A$ 的特征函数 $\chi_A$ 定义为：
$$
\chi_A: E \rightarrow \{0,1\}, \quad \chi_A(a) = 
\begin{cases} 
1 & a \in A, \\
0 & a \notin A.
\end{cases}
$$

**定义 3.1.3** **典型映射或自然映射** 设 $R$ 是 $A$ 上的等价关系，令 $g:A \rightarrow A/R$， $g(a) = [a]_R$，则称 $g$ 为从 $A$ 到商集 $A/R$ 的典型映射或自然映射。

**选择公理(形式1)** 对任意的关系 $R$，存在函数 $f$，使得
$$
f \subseteq R \text{且 } \text{dom}(f) = \text{dom}(R).
$$

## 3.2. 函数的合成与函数的逆

**定理 3.2.1** **函数的合成** 设 $g:A \rightarrow B$， $f:B \rightarrow C$，则

(1) $f \circ g$ 是函数 $f \circ g : A \rightarrow C$，

(2) 对任意的 $x \in A$，有 $(f \circ g)(x) = f(g(x))$。

**定理 3.2.2** **函数的合成的性质1** 设 $g:A \rightarrow B$， $f:B \rightarrow C$，

(1) 若 $f,g$ 是满射的，则 $f \circ g$ 是满射的，

(2) 若 $f,g$ 是单射的，则 $f \circ g$ 是单射的，

(3) 若 $f,g$ 是双射的，则 $f \circ g$ 是双射的。

**定理 3.2.3** **函数的合成的性质2** 设 $g:A \rightarrow B$， $f:B \rightarrow C$，

(1) 若 $f \circ g$ 是满射的，则 $f$ 是满射的，

(2) 若 $f \circ g$ 是单射的，则 $g$ 是单射的，

(3) 若 $f \circ g$ 是双射的，则 $f$ 是满射的，$g$ 是单射的。

**定理 3.2.4** 设 $f:A \rightarrow B$，则 $f = f \circ I_A = I_B \circ f$。

**定理 3.2.5** **函数的逆** 若 $f:A \rightarrow B$ 是双射的，则 $f^{-1}$ 是函数 $f^{-1}: B \rightarrow A$。

**定义 3.2.1** **反函数** 设 $f:A \rightarrow B$ 是双射的，则称 $f^{-1}: B \rightarrow A$ 为 $f$ 的反函数。

**定理 3.2.6** 若 $f:A \rightarrow B$ 是双射的，则 $f^{-1}: B \rightarrow A$ 是双射的。

**定理 3.2.7** 若 $f:A \rightarrow B$ 是双射的，则对任意的 $x \in A$，有 $f^{-1}(f(x)) = x$，对任意的 $y \in B$，有 $f(f^{-1}(y)) = y$。

**定义 3.2.2** **函数的左逆和右逆** 设 $f:A \rightarrow B$， $g:B \rightarrow A$，如果 $g \circ f = I_A$，则称 $g$ 为 $f$ 的左逆；如果 $f \circ g = I_B$，则称 $g$ 为 $f$ 的右逆。

**定理 3.2.8** 设 $f:A \rightarrow B$， $A \neq \emptyset$，则

(1) $f$ 存在左逆，当且仅当 $f$ 是单射；

(2) $f$ 存在右逆，当且仅当 $f$ 是满射的；

(3) $f$ 存在左逆又存在右逆，当且仅当 $f$ 是双射的；

(4) 若 $f$ 是双射的，则 $f$ 的左逆等于右逆。

## 3.3. 函数的性质

**定义 3.3.1** **函数的相容性** 设 $f:A \rightarrow B$， $g:C \rightarrow D$，如果对任意的 $x \in A \cap C$，都有 $f(x) = g(x)$，就说 $f$ 和 $g$ 是相容的。

**定义 3.3.2** **函数集的相容性** 设 $C$ 是由一些函数组成的集合，如果 $C$ 中任意两个函数 $f$ 和 $g$ 都是相容的，就说 $C$ 是相容的。

**定理 3.3.1** 设 $f: A \rightarrow B, g: C \rightarrow D$，则 $f$ 和 $g$ 是相容的当且仅当 $f \cup g$ 是函数。

**定理 3.3.2** 设 $f: A \rightarrow B, g: C \rightarrow D$，则 $f$ 与 $g$ 是相容的当且仅当
$$
f \uparrow (A \cap C) = g \uparrow (A \cap C)。
$$

**定理 3.3.3** 对函数的集合 $C$，若 $C$ 是相容的，且 $F = \bigcup C$，则 $F$ 是函数 $F: \text{dom}(F) \rightarrow \text{ran}(F)$，
$$
\text{dom}(F) = \bigcup \{\text{dom}(f) | f \in C\}。
$$

**定义 3.3.3** **关系与函数的相容性** 设 $R$ 是 $A$ 上的等价关系，且 $f: A \rightarrow A$，如果对任意的 $x,y \in A$，有 $\langle x,y \rangle \in R \Rightarrow \langle f(x),f(y) \rangle \in R$，则称关系 $R$ 与函数 $f$ 是相容的。

**定理 3.3.4** 设 $R$ 是 $A$ 上的等价关系，且 $f: A \rightarrow A$，如果 $R$ 与 $f$ 是相容的，则存在唯一的函数 $F: A/R \rightarrow A/R$，使 $F([x]_R) = [f(x)]_R$；如果 $R$ 与 $f$ 不相容，则不存在这样的函数 $F$。

## 3.4. 开集与闭集

**定义 3.4.1** **距离** 对实数集 $R$，若 $\rho: R \times R \rightarrow R$ 定义为 $\rho(\langle x,y \rangle) = |x-y|$，其中 $|x-y|$ 是 $x-y$ 的绝对值，则称 $\rho$ 为 $R$ 上的距离函数，对任意 $\langle x,y \rangle \in R \times R$，把 $\rho(\langle x,y \rangle)$ 称为 $x$ 和 $y$ 的距离，并可写为 $\rho(x,y) = |x-y|$。

**定义 3.4.2** **邻域** 对实数集 $R$，$<$ 是 $R$ 上的小于关系，$\rho$ 是 $R$ 上的距离函数，若 $x_0 \in R, \varepsilon \in R$ 且 $\varepsilon > 0$，则集合
$$
\{ x | x \in R \land \rho(x_0,x) < \varepsilon \}
$$
称为 $x_0$ 的邻域。

**定义 3.4.3** **极限点** 对实数集 $R, A \subseteq R, x_0 \in R$，如果在 $x_0$ 的任一个 $\varepsilon$ 邻域中，都存在不等于 $x_0$ 的元素 $x$，且 $x \in A$，则称 $x_0$ 是 $A$ 的一个极限点（或凝聚点）。

定义的条件可以写成
$$
(\forall \varepsilon)(\varepsilon \in R \land \varepsilon > 0) \rightarrow (\exists x)(x \in A \land x \neq x_0 \land \rho(x,x_0) < \varepsilon)。
$$

**定理 3.4.1** 对实数集 $R, A \subseteq R, x_0 \in R, x_0$ 是 $A$ 的极限点当且仅当在 $A$ 中存在点列
$$
\{ x_n | x_n \in A \land x_n \neq x_0 \land (m \neq n \rightarrow x_m \neq x_n) \}
$$
使得 $\lim_{n \to \infty} x_n = x_0$。

**定理 3.4.2** 若 $A \subseteq R$ 是有界无限集，则 $A$ 具有极限点。

**定义 3.4.4** **孤立点** 对实数集 $R, A \subseteq R, x_0 \in A$，若 $x_0$ 不是 $A$ 的极限点，则称 $x_0$ 为 $A$ 的孤立点。

**定义 3.4.5** **导集与闭集** 对实数集 $R, A \subseteq R, A$ 的所有极限点的集合称为 $A$ 的导集，记作 $A'$。如果 $A' \subseteq A$，则称 $A$ 为闭集。

**定理 3.4.3** 对实数集 $R, A \subseteq R$，则 $A'$ 是闭集，即 $(A')' \subseteq A'$。

**定理 3.4.4** 任意个闭集的交集是闭集。有限个闭集的并集是闭集。

**定义 3.4.6** **内点** 对实数集 $R, A \subseteq R, x_0 \in R$，如果存在 $x_0$ 的 $\varepsilon$ 邻域，其中全是 $A$ 的元素，则称 $x_0$ 为 $A$ 的一个内点。

定义的条件可以写成
$$
(\exists \varepsilon)(\varepsilon \in R \land \varepsilon > 0 \land (\forall x)((x \in R \land \rho(x,x_0) < \varepsilon) \rightarrow x \in A))。
$$

**定义 3.4.7** **开集** 对实数集 $R, A \subseteq R$，若 $A$ 的元素都是 $A$ 的内点，则称 $A$ 为开集。

**定理 3.4.5** 任意个开集的并集是开集，有限个开集的交集是开集。

**定理 3.4.6** 对实数集 $R, A \subseteq R$，

(1) 若 $A$ 是开集，则 $R - A$ 是闭集。

(2) 若 $A$ 是闭集，则 $R - A$ 是开集。

## 3.5. 模糊子集

**定理 3.5.1** **特征函数的性质** 设 $E$ 是论域，$A \subseteq E, B \subseteq E$，$+, -, *$ 是算术加、减、乘法，

(1) $(\forall x)(\chi_A(x)=0) \Leftrightarrow A = \emptyset$，

(2) $(\forall x)(\chi_A(x)=1) \Leftrightarrow A = E$，

(3) $(\forall x)(\chi_A(x) \leq \chi_B(x)) \Leftrightarrow A \subseteq B$，

(4) $(\forall x)(\chi_A(x)=\chi_B(x)) \Leftrightarrow A = B$，

(5) $\chi_{A \cap B}(x) = \chi_A(x) * \chi_B(x)$，

(6) $\chi_{A \cup B}(x) = \chi_A(x) + \chi_B(x) - \chi_{A \cap B}(x)$，

(7) $\chi_{A-B}(x) = \chi_A(x) - \chi_{A \cap B}(x)$，

(8) $\chi_{\bar A}(x) = 1 - \chi_A(x)$。

**定义 3.5.1** **模糊子集与隶属函数** 设 $E$ 是论域，$E$ 上的一个模糊子集 $A$ 是指：存在一个函数 $\mu_A: E \rightarrow [0,1]$，并称 $\mu_A$ 为 $A$ 的隶属函数。

**定义 3.5.2** 设 $E$ 是全集，$A, B \in F(E)$，则 $A \cup B, A \cap B, \bar A$ 具有下列隶属函数
$$
\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x)),
$$

$$
\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x)),
$$

$$
\mu_{\bar A}(x) = 1 - \mu_A(x).
$$

$A \cup B, A \cap B, \bar A$ 分别称为并集、交集、绝对补集。

**定义 3.5.3** **截集** 设 $E$ 是全集，$A \in F(E)$，对 $\lambda \in [0,1]$，集合
$$
(A)_{\lambda} = \{x | \mu_A(x) \geq \lambda\}
$$
称为 $A$ 的 $\lambda$ 截集，$(A)_{\lambda}$ 可以写作 $A_{\lambda}$。

**定理 3.5.2** 设 $E$ 是全集，$A, B \in F(E), \lambda \in [0,1]$ 则

(1) $(A \cup B)_{\lambda} = (A)_{\lambda} \cup (B)_{\lambda}$，

(2) $(A \cap B)_{\lambda} = (A)_{\lambda} \cap (B)_{\lambda}$。

**定理 3.5.3** 设 $E$ 是全集，$A \in F(E), \lambda, \sigma \in [0,1]$ 则

(1) $\lambda \leq \sigma \Rightarrow A_{\sigma} \subseteq A_{\lambda}$，

(2) $A_0 = E$。

**定理 3.5.4** **分解定理** 设 $E$ 是全集，$A \in F(E), \lambda \in [0,1]$，$\chi_{A_{\lambda}}(u)$ 是 $A_{\lambda}$ 的特征函数，则
$$
\mu_A(u) = \sup_{\lambda \in [0,1]} (\inf(\lambda, \chi_{A_{\lambda}}(u)))。
$$
（其中 $\sup$ 表示集合的上确界，$\inf$ 表示集合的下确界）

**定义 3.5.4** **支集 核 边界 正规模糊集** 设 $E$ 是全集，$A \in F(E)$，则
$$
\text{supp} A = \{ u | \mu_A(u) > 0 \}
$$
称为 $A$ 的支集，截集 $A_1$ 称为 $A$ 的核，$(\text{supp} A) - A_1$ 称为 $A$ 的边界。

核 $A_1$ 的元素完全隶属于 $A$。若 $A_1 \neq \emptyset$，就称 $A$ 为正规模糊集；若 $A_1 = \emptyset$，就称 $A$ 为非正规模糊集。
