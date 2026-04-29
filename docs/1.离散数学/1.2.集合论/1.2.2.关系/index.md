## 2.1. 二元关系

1.  **二元关系（有序对的集合）** 如果一个集合满足以下条件之一：
    （1）集合非空，且它的元素都是有序对（见1.3节中“1.有序对”）；
    （2）集合是空集。
    则称该集合为一个二元关系，记作 $R$。二元关系也简称关系。对于二元关系 $R$，如果 $\langle x，y \rangle \in R$，也可记作 $xRy$。

**定义2.1.1. A到B的二元关系** 设 $A，B$ 为集合，$A \times B$ 的任一子集所定义的二元关系称为 $A$ 到 $B$ 的二元关系。特别当 $A=B$ 时，$A \times A$ 的任一子集称为 $A$ 上的一个二元关系。

**定义2.1.2. n元关系（n元组的集合）** 若 $n \in N$ 且 $n>1$，$A_1，A_2，\dots，A_n$ 是 $n$ 个集合，则 $A_1 \times A_2 \times \dots \times A_n$ 的任一子集称为从 $A_1$ 到 $A_n$ 上的一个 $n$ 元关系。

2. **集合族上的包含关系与真包含关系** 设 $A$ 是集合族，$A$ 上的包含关系可定义为：
   $$
   R_{E} = \{ \langle x，y \rangle | x，y \in A \land x \subseteq y \}
   $$
   $A$ 上的真包含关系可定义为：
   $$
   R_{C} = \{ \langle x，y \rangle | x，y \in A \land x \subset y \}
   $$
   例如，对任意的集合 $A$，则 $A$ 的幂集 $P(A)$ 上的包含关系可定义为：
   $$
   R_{E} = \{ \langle x，y \rangle | x \in P(A) \land y \in P(A) \land x \subseteq y \}
   $$

**定义2.1.3. 三个特殊的关系——恒等关系、全域关系和空关系** 对任意的集合 $A$，

​    （1）$A$ 上的恒等关系 $I_A$ 定义为
$$
I_A = \{ \langle x，x \rangle | x \in A \}
$$
​    （2）$A$ 上的全域关系（全关系）$E_A$ 定义为
$$
E_A = \{ \langle x，y \rangle | x \in A \land y \in A \}
$$
​    （3）空集 $O$ 是 $A \times A$ 的子集，定义为 $A$ 上的空关系。

**定义2.1.4. 定义域和值域** 设 $R$ 是 $A$ 到 $B$ 的二元关系

​    （1）$R$ 中所有有序对的第1元素构成的集合称为 $R$ 的定义域，记作 $dom(R)$。形式化表示为 $dom(R) = \{x|(\exists y)(\langle x，y \rangle \in R)\}$

​    （2）$R$ 中所有有序对的第2元素构成的集合称为 $R$ 的值域，记作 $ran(R)$。形式化表示为 $ran(R) = \{y|(\exists x)(\langle x，y \rangle \in R)\}$

​    （3）$R$ 的定义域和值域的并集称为 $R$ 的域，记作 $fld(R)$。形式化表示为
$$
fld(R) = dom(R) \cup ran(R)
$$

## 2.2. 关系矩阵和关系图

**定义2.2.1. 关系矩阵** 设集合 $X=\{x_1，x_2，\dots，x_m\}$，$Y=\{y_1，y_2，\dots，y_n\}$，若 $R$ 是 $X$ 到 $Y$ 的一个关系。则 $R$ 的关系矩阵是 $m \times n$ 矩阵，矩阵元素是 $r_{ij}$。
$$
M(R) = (r_{ij})_{m \times n}
$$
其中
$$
r_{ij} =
\begin{cases}
1 & \text{当 } (x_i， y_j) \in R \\
0 & \text{当 } (x_i， y_j) \notin R
\end{cases}
\quad (1 \leq i \leq m， 1 \leq j \leq n)
$$
若 $R$ 是 $X$ 上的一个关系，则 $R$ 的关系矩阵是 $m \times m$ 方阵，定义与上述类似。

**定义2.2.2. 关系图** 设集合 $X=\{x_1，x_2，\dots，x_m\}$，$Y=\{y_1，y_2，\dots，y_n\}$。
​    （1）若 $R$ 是 $X$ 到 $Y$ 的一个关系，则 $R$ 的关系图是一个有向图 $G(R)=(V，E)$。它的顶点集是 $V=X \cup Y$，边集是 $E$，从 $x_i$ 到 $y_j$ 的有向边 $e_{ij} \in E$，当且仅当 $\langle x_i，y_j \rangle \in R$。
​    （2）若 $R$ 是 $X$ 上的一个关系，则 $R$ 的关系图是上述情形的特例。

## 2.3. 关系的逆、合成、限制和象

**定义2.3.1. 关系的逆、合成、限制和象** 对 $X$ 到 $Y$ 的关系 $R$，$Y$ 到 $Z$ 的关系 $S$，定义

​    （1）$R$ 的逆 $R^{-1}$ 为 $Y$ 到 $X$ 的关系
$$
R^{-1} = \{\langle y，x \rangle | \langle x，y \rangle \in R\}
$$
​    （2）$R$ 与 $S$ 的合成 $S \cdot R$（有些书中称之为关系的左复合）为 $X$ 到 $Z$ 的关系
$$
S \cdot R = \{\langle x，z \rangle | (\exists y)(\langle x，y \rangle \in R \land \langle y，z \rangle \in S)\}
$$
​    （3）对任意的集合 $A$，定义 $R$ 在 $A$ 上的限制 $R \upharpoonright A$ 为 $A$ 到 $Y$ 的关系
$$
R \upharpoonright A = \{\langle x，y \rangle | \langle x，y \rangle \in R \land x \in A\}
$$
​    （4）$A$ 在 $R$ 下的象 $R[A]$ 为集合
$$
R[A] = \{y | (\exists x)(x \in A \land \langle x，y \rangle \in R)\}
$$

​    $S \cdot R$ 的关系矩阵 设 $A$ 是有限集合，$|A|=n$。关系 $R$ 和 $S$ 都是 $A$ 上的关系，$R$ 和 $S$ 的关系矩阵
$$
M(R) = [r_{ij}] \quad \text{和} \quad M(S) = [s_{ij}]
$$
​    都是 $n \times n$ 的方阵。于是 $R$ 与 $S$ 的合成 $S \cdot R$ 的关系矩阵
$$
M(S \cdot R) = (w_{ij})_{n \times n}
$$
​    可以用下述的矩阵逻辑乘计算（类似于矩阵乘法）。记作
$$
M(S \cdot R) = M(R) \cdot M(S)
$$
​    其中
$$
w_{ij} = \bigvee_{k=1}^{n} (r_{ik} \land s_{kj})
$$

**定理2.3.1. 关系$R$的逆关系的性质** 对 $X$ 到 $Y$ 的关系 $R$ 和 $Y$ 到 $Z$ 的关系 $S$，有
$$
dom(R^{-1}) = ran(R) \\
ran(R^{-1}) = dom(R) \\
(R^{-1})^{-1} = R \\
(S \cdot R)^{-1} = R^{-1} \cdot S^{-1}
$$

**定理2.3.2. 关系的合成的结合律** 对 $X$ 到 $Y$ 的关系 $Q$，$Y$ 到 $Z$ 的关系 $S$，$Z$ 到 $W$ 的关系 $R$，有
$$
(R \cdot S) \cdot Q = R \cdot (S \cdot Q)
$$

**定理2.3.3. 关系的合成的其他性质** 对 $X$ 到 $Y$ 的关系 $R_2$，$R_3$，$Y$ 到 $Z$ 的关系 $R_1$，有
$$
R_1 \cdot (R_2 \cup R_3) = R_1 \cdot R_2 \cup R_1 \cdot R_3 \\
R_1 \cdot (R_2 \cap R_3) \subseteq R_1 \cdot R_2 \cap R_1 \cdot R_3
$$
对 $X$ 到 $Y$ 的关系 $R_3$，$Y$ 到 $Z$ 的关系 $R_1$，$R_2$，有
$$
(R_1 \cup R_2) \cdot R_3 = R_1 \cdot R_3 \cup R_2 \cdot R_3 \\
(R_1 \cap R_2) \cdot R_3 \subseteq R_1 \cdot R_2 \cap R_1 \cdot R_3
$$
（注意，规定关系合成运算符优先于集合运算符）

**定理2.3.4. 集合在关系下的象的性质** 对 $X$ 到 $Y$ 的关系 $R$ 和集合 $A$，$B$，有
$$
R[A \cup B] = R[A] \cup R[B] \\
R[\cup A] = \cup \{ R[B] | B \in A \} \\
R[A \cap B] \subseteq R[A] \cap R[B] \\
R[\cap A] \subseteq \cap \{ R[B] | B \in A \} \quad A \neq \emptyset \\
R[A] - R[B] \subseteq R[A - B]
$$

## 2.4. 关系的性质

**定义2.4.1. 自反性与非自反性** 设 $R$ 为集合 $A$ 上的关系，则

​    $R$ 在 $A$ 上是自反的 $\Leftrightarrow (\forall x)(x \in A \Rightarrow \langle x， x \rangle \in R)$

​    $R$ 在 $A$ 上是非自反的 $\Leftrightarrow (\forall x)(x \in A \Rightarrow \langle x， x \rangle \notin R)$

**定义2.4.2. 对称性与反对称性** 设 $R$ 为集合 $A$ 上的关系，则

​    $R$ 在 $A$ 上是对称的 $\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x， y \rangle \in R) \Rightarrow \langle y， x \rangle \in R)$

​    $R$ 在 $A$ 上是反对称的 $\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x， y \rangle \in R \land \langle y， x \rangle \in R) \Rightarrow x = y)$

​    反对称性的另一种等价的定义为

​    $R$ 在 $A$ 上是反对称的 $\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x， y \rangle \in R \land x \neq y) \Rightarrow \langle y， x \rangle \notin R)$

**定义2.4.3. 传递性** 设 $R$ 为集合 $A$ 上的关系，则

​    $R$ 在 $A$ 上是传递的 $\Leftrightarrow (\forall x)(\forall y)(\forall z)((x \in A \land y \in A \land z \in A \land \langle x， y \rangle \in R \land \langle y， z \rangle \in R) \Rightarrow \langle x， z \rangle \in R)$

**定理2.4.1. 几个特殊关系的自反性** 设 $R_1$，$R_2$ 是 $A$ 上的自反关系，则 $R^{-1}$，$R_1 \cap R_2$，$R_1 \cup R_2$ 也是 $A$ 上的自反关系。

**定理2.4.2. 几个特殊关系的对称性** 设 $R_1$，$R_2$ 是 $A$ 上的对称关系，则 $R^{-1}$，$R_1 \cap R_2$，$R_1 \cup R_2$ 也是 $A$ 上的对称关系。

**定理2.4.3. 几个特殊关系的传递性** 设 $R_1$，$R_2$ 是 $A$ 上的传递关系，则 $R^{-1}$，$R_1 \cap R_2$ 是 $A$ 上的传递关系。但 $R_1 \cup R_2$ 不一定是传递的。

**定理2.4.4. 几个特殊关系的反对称性** 设 $R_1$，$R_2$ 是 $A$ 上的传递关系，则 $R^{-1}$，$R_1 \cap R_2$ 是 $A$ 上的反对称关系。但 $R_1 \cup R_2$ 不一定是反对称的。

**定理2.4.5. 对称性与反对称性的两个性质** 设 $R$ 是 $A$ 上的关系，则

​    （1）$R$ 是对称的 $\Leftrightarrow R = R^{-1}$，

​    （2）$R$ 是反对称的 $\Leftrightarrow R \cap R^{-1} \subseteq I_A$。

## 2.5. 关系的闭包

**定义2.5.1. 多个关系的合成** 设 $R$ 为 $A$ 上的关系，$n \in N$，关系 $R$ 的 $n$ 次幂定义为：
$$
R^0 = \{\langle x， x \rangle| x \in A\} = I_A \\
R^{n+1} = R^n \cdot R \quad (n \geq 0)
$$

**定理2.5.1. 有限集合上只有有限个不同的二元关系** 设 $A$ 是有限集合，$|A| = n$，$R$ 是 $A$ 上的关系，则存在自然数 $s$ 和 $t$，$s \neq t$ 使得 $R^s = R^t$。

**定理2.5.2. 有限集合上关系的合成** 设 $A$ 是有限集合，$R$ 是 $A$ 上的关系，$m$ 和 $n$ 是非零自然数，则
$$
R^m \cdot R^n = R^{m+n} \\
(R^m)^n = R^{mn}
$$

**定理2.5.3. 有限集合上关系的幂序列具有周期性** 设 $A$ 是有限集合，$R$ 是 $A$ 上的关系，若存在自然数 $s$ 和 $t$，$s < t$，使得 $R^s = R^t$，则

​    （1）$R^{s+k} = R^{t+k}$，其中 $k \in N$；

​    （2）$R^{s+lp+i} = R^{s+i}$，其中 $l， i \in N， p = t - s$；

​    （3）令 $B = \{R^0， R^1， \dots， R^{t-1}\}$，则 $R$ 的各次幂均为 $B$ 的元素，即对任意的 $q \in N$，有 $R^q \in B$。

**定义2.5.2. 闭包的定义** 设 $R$ 是非空集合 $A$ 上的关系，如果 $A$ 上有另一个关系 $R'$ 满足：

​    （1）$R'$ 是自反的（对称的，传递的）；

​    （2）$R \subseteq R'$；

​    （3）对 $A$ 上任何自反的（对称的，传递的）关系 $R''$，$R' \subseteq R''$。

​    则称关系 $R'$ 为 $R$ 的自反（对称，传递）闭包。一般将 $R$ 的自反闭包记作 $r(R)$，对称闭包记作 $s(R)$，传递闭包记作 $t(R)$。它们分别是具有自反性（对称性，传递性）的 $R$ 的“最小”超集合。

**定理2.5.4. 闭包的性质 1** 对非空集合 $A$ 上的关系 $R$，有

​    （1）$R$ 是自反的 $\Leftrightarrow r(R) = R$，

​    （2）$R$ 是对称的 $\Leftrightarrow s(R) = R$，

​    （3）$R$ 是传递的 $\Leftrightarrow t(R) = R$。

**定理2.5.5. 闭包的性质 2** 对非空集合 $A$ 上的关系 $R_1$，$R_2$，若 $R_1 \subseteq R_2$，则
$$
r(R_1) \subseteq r(R_2) \\
s(R_1) \subseteq s(R_2) \\
t(R_1) \subseteq t(R_2)
$$

**定理2.5.6. 闭包的性质 3** 对非空集合 $A$ 上的关系 $R_1$，$R_2$，
$$
r(R_1) \cup r(R_2) = r(R_1 \cup R_2) \\
s(R_1) \cup s(R_2) = s(R_1 \cup R_2) \\
t(R_1) \cup t(R_2) \subseteq t(R_1 \cup R_2)
$$

**定理2.5.7. 自反闭包的构造方法** 对非空集合 $A$ 上的关系 $R$，有
$$
r(R) = R \cup I_A
$$

**定理2.5.8. 对称闭包的构造方法** 对非空集合 $A$ 上的关系 $R$，有
$$
s(R) = R \cup R^{-1}
$$

**定理2.5.9. 传递闭包的构造方法** 对非空集合 $A$ 上的关系 $R$，有
$$
t(R) = R \cup R^2 \cup R^3 \cup \dots
$$

**定理2.5.10. 传递闭包的有限构造方法** $A$ 为非空有限集合，$|A|=n$，$R$ 是 $A$ 上的关系，则存在正整数 $k \leq n$，使得
$$
t(R) = R \cup R^2 \cup \dots \cup R^k
$$

**定理2.5.11. 闭包同时具有的多种性质 1** 对非空集合 $A$ 上的关系 $R$，有

​    （1）若 $R$ 是自反的，则 $s(R)$ 和 $t(R)$ 是自反的，

​    （2）若 $R$ 是对称的，则 $r(R)$ 和 $t(R)$ 是对称的，

​    （3）若 $R$ 是传递的，则 $r(R)$ 是传递的。

**定理2.5.12. 闭包同时具有的多种性质 2** 对非空集合 $A$ 上的关系 $R$，有

​    （1）$rs(R)=sr(R)$，

​    （2）$rt(R)=tr(R)$，

​    （3）$st(R)\subseteq ts(R)$。

​    其中 $rs(R)=r(s(R))$，其他类似。

## 2.6. 等价关系和划分

**定义2.6.1. 等价关系** 设 $R$ 为非空集合 $A$ 上的关系，如果 $R$ 是自反的、对称的和传递的，则称 $R$ 为 $A$ 上的等价关系。

**定义2.6.2. 等价类** 设 $R$ 为非空集合 $A$ 上的等价关系，对任意的 $x \in A$，令
$$
[x]_R = \{y | y \in A \land xRy\}
$$
​    称集合 $[x]_R$ 为关于 $R$ 的等价类，简称 $x$ 的等价类，也可简记作 $[x]_R$ 或 $\overline{x}$。

**定理2.6.1. 等价类的性质** $R$ 是非空集合 $A$ 上的等价关系，对任意的 $x，y \in A$，有

​    （1）$[x]_R \neq \emptyset$ 且 $[x]_R \subseteq A$，即 $[x]_R$ 是 $A$ 的非空子集，

​    （2）若 $xRy$，则 $[x]_R = [y]_R$，

​    （3）若 $(x，y) \notin R$，则 $[x]_R \cap [y]_R = \emptyset$，

​    （4）$\cup \{[x]_R | x \in A\} = A$。

**定义2.6.3. 商集** 设 $R$ 为非空集合 $A$ 上的关系，以 $R$ 的不相交的等价类为元素的集合称为 $A$ 的商集，记作 $A/R$。即
$$
A/R = \{[x]_R | x \in A\}
$$

**定义2.6.4. 划分** 设 $A$ 为非空集合，若存在 $A$ 的非空子集构成的集合 $\pi$ 满足下列条件：

​    （1）$(\forall x)(x \in \pi \rightarrow x \subseteq A)$，

​    （2）$\emptyset \notin \pi$，

​    （3）$\cup \pi = A$，

​    （4）$(\forall x)(\forall y)((x \in \pi \land y \in \pi \land x \neq y) \rightarrow x \cap y = \emptyset)$

​    则称 $\pi$ 为 $A$ 的一个划分，称 $\pi$ 中的元素为 $A$ 的划分块。

**定理2.6.2. 等价关系$R$诱导出的$A$的划分** 对非空集合 $A$ 上的等价关系 $R$，$A$ 的商集 $A/R$ 就是 $A$ 的划分，称为由等价关系 $R$ 诱导出的 $A$ 的划分，记作 $\pi_R$。

**定理2.6.3. 划分$\pi$诱导出的$A$上的等价关系** 对非空集合 $A$ 上的一个划分 $\pi$，令 $A$ 上的关系 $R_\pi$ 为
$$
R_\pi = \{ \langle x，y \rangle | (\exists z)(z \in \pi \land x \in z \land y \in z) \}
$$
​    则 $R_\pi$ 为 $A$ 上的等价关系，它称为划分 $\pi$ 诱导出的 $A$ 上的等价关系。

**定理2.6.4. 划分$\pi$和$A$上的等价关系$R$** 对非空集合 $A$ 上的一个划分 $\pi$ 和 $A$ 上的等价关系 $R$，$\pi$ 诱导 $R$ 当且仅当 $R$ 诱导 $\pi$。

## 2.7. 相容关系和覆盖

**定义2.7.1. 相容关系** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是自反的、对称的，则称 $R$ 为 $A$ 上的相容关系。

**定义2.7.2. 相容类** 对非空集合 $A$ 上的相容关系 $R$，若 $C \subseteq A$，且 $ C $ 中任意两个元素 $x$ 和 $y$ 有 $xRy$，则称 $ C $ 是由相容关系 $R$ 产生的相容类，简称相容类。这个定义也可以写成
$$
C = \{ x | x \in A \land (\forall y)(y \in C \rightarrow xRy) \}
$$

**定义2.7.3. 最大相容类** 对非空集合 $A$ 上的相容关系 $R$，一个相容类若不是任何相容类的真子集，就称为最大相容类，记作 $C_R$。
    最大相容类 $C_R$ 有下列性质：
$$
(\forall x)(\forall y)((x \in C_R \land y \in C_R) \rightarrow xRy) 
$$
​    和
$$
(\forall x)(x \in A - C_R \rightarrow (\exists y)(y \in C_R \land xRy))
$$

**定理2.7.1. 最大相容类的存在性** 对非空有限集合 $A$ 上的相容关系 $R$，若 $ C $ 是一个相容类，则存在一个最大相容类 $C_R$，使 $C \subseteq C_R$。

**定义2.7.4. 覆盖** 对非空集合 $A$，若存在集合 $\Omega$ 满足下列条件：

​    （1）$(\forall x)(x \in \Omega \rightarrow x \subseteq A)$，

​    （2）$\emptyset \notin \Omega$，

​    （3）$\cup \Omega = A$，

​    则称 $\Omega$ 为 $A$ 的一个覆盖，称 $\Omega$ 中的元素为 $\Omega$ 的覆盖块。

**定理2.7.2. 完全覆盖** 对非空集合 $A$ 上的相容关系 $R$，最大相容类的集合是 $A$ 的一个覆盖，称为 $A$ 的完全覆盖，记作 $C_R(A)$，而且 $C_R(A)$ 是唯一的。

**定理2.7.3. 覆盖与相容关系** 对非空集合 $A$ 的一个覆盖 $\Omega = \{ A_1， A_2， \cdots， A_n \}$，由 $\Omega$ 确定的关系
$$
R = A_1 \times A_1 \cup A_2 \times A_2 \cup \cdots \cup A_n \times A_n
$$
​    是 $A$ 上的相容关系。

## 2.8. 偏序关系

**定义2.8.1. 偏序关系** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是自反的、反对称的和传递的，则称 $R$ 为 $A$ 上的偏序关系。
    在不会产生误解时，偏序关系 $R$ 通常记作 $\leq$。当 $xRy$ 时，可记作 $x \leq y$，读作“$x$ 小于等于 $y$”。偏序关系又称弱偏序关系，或半序关系。

**定义2.8.2. 拟序关系（强偏序关系）** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是非自反的和传递的，则称 $R$ 为 $A$ 上的拟序关系。
    在不会产生误解时，拟序关系 $R$ 通常记作 $<$。当 $xRy$ 时，可记作 $x < y$，读作“$x$ 小于 $y$”。拟序关系又称强偏序关系。

**定理2.8.1.** $R$ 为 $A$ 上的拟序关系，则 $R$ 是反对称的。

**定理2.8.2.** 对 $A$ 上的拟序关系 $R$，$R \cup I_A$ 是 $A$ 上的偏序关系。

**定理2.8.3.** 对 $A$ 上的偏序关系 $R$，$R - I_A$ 是 $A$ 上的拟序关系。

**定义2.8.3. 偏序集** 集合 $A$ 与 $A$ 上的关系 $R$ 一起称为一个结构。集合 $A$ 与 $A$ 上的偏序关系 $R$ 一起称为一个偏序结构，或称偏序集，并记作 $(A，R)$。

**定义2.8.4. 盖住关系** 对偏序集 $(A，\leq)$，如果 $x，y \in A$，$x \leq y$，$x \neq y$，且不存在元素 $z \in A$ 使得 $x \leq z$ 且 $z \leq y$，则称 $y$ 盖住 $x$。$A$ 上的盖住关系 $cov A$ 定义为
$$
cov A = \{\langle x，y \rangle | x \in A \land y \in A \land y \text{ 盖住 } x\}
$$
**定义2.8.5. 最小元、最大元、极小元、极大元** 对偏序集 $(A，\leq)$，且 $B \subseteq A$，

​    （1）若 $y \in B \land (\forall x)(x \in B \rightarrow y \leq x)$，则称 $y$ 为 $B$ 的最小元；

​    （2）若 $y \in B \land (\forall x)(x \in B \rightarrow x \leq y)$，则称 $y$ 为 $B$ 的最大元；

​    （3）若 $y \in B \land (\forall x)(x \in B \land x \leq y \rightarrow x=y)$，则称 $y$ 为 $B$ 的极小元；

​    （4）若 $y \in B \land (\forall x)(x \in B \land y \leq x \rightarrow x=y)$，则称 $y$ 为 $B$ 的极大元。

**定义2.8.6. 上界、下界、上确界、下确界** 对偏序集 $(A，\leq)$，且 $B \subseteq A$，

​    （1）若 $y \in A \land (\forall x)(x \in B \rightarrow x \leq y)$，则称 $y$ 为 $B$ 的上界；

​    （2）若 $y \in A \land (\forall x)(x \in B \rightarrow y \leq x)$，则称 $y$ 为 $B$ 的下界；

​    （3）若集合 $C=\{y|y \text{ 是 B 的上界}\}$，则 $ C $ 的最小元称为 $B$ 的上确界或最小上界；

​    （4）若集合 $C=\{y|y \text{ 是 B 的下界}\}$，则 $ C $ 的最大元称为 $B$ 的下确界或最大下界。

**定义2.8.7. 可比** 对偏序集 $(A，\leq)$，对任意的 $x，y \in A$，若 $x \leq y$ 或 $y \leq x$，则称 $x$ 和 $y$ 是可比的。

**定义2.8.8. 全序关系与全序集** 对偏序集 $(A，\leq)$，如果对任意的 $x，y \in A$， $x$ 和 $y$ 都可比，则称 $\leq$ 为 $A$ 上的全序关系，或称线序关系。并称 $(A，\leq)$ 为全序集。

**定义2.8.9. 链、反链** 对偏序集 $(A，\leq)$，且 $B \subseteq A$，

​    （1）如果对任意的 $x，y \in B$， $x$ 和 $y$ 都是可比的，则称 $B$ 为 $A$ 上的链，$B$ 中元素个数称为链的长度。

​    （2）如果对任意的 $x，y \in B$， $x$ 和 $y$ 都不是可比的，则称 $B$ 为 $A$ 上的反链，$B$ 中元素个数称为反链的长度。

**定理2.8.4. 偏序集的分解定理** 对偏序集 $(A，\leq)$，设 $A$ 中最长链的长度是 $n$，则将 $A$ 中元素分成不相交的反链，反链个数至少是 $n$。

**定理2.8.5.** 对偏序集 $(A，\leq)$，若 $A$ 中元素为 $mn+1$ 个，则 $A$ 中或者存在一条长度为 $m+1$ 的反链，或者存在一条长度为 $n+1$ 的链。

**定义2.8.10. 良序关系与良序集** 对偏序集 $(A，\leq)$，如果 $A$ 的任何非空子集都有最小元，则称 $\leq$ 为良序关系，称 $(A， \leq)$ 为良序集。

**定理2.8.6.** 一个良序集一定是全序集。

**定理2.8.7.** 一个有限的全序集一定是良序集。

**定理2.8.8.（良序定理）** 任意的集合都是可以良序化的。

**定义2.8.11.（闭区间，开区间）** 在全序集 $(R， \leq)$ 上，对于 $a， b \in R， a \neq b， a \leq b$，

​    （1）$[a， b] = \{ x | x \in R \land a \leq x \leq b \}$，称为从 $a$ 到 $b$ 的闭区间；

​    （2）$(a， b) = \{ x | x \in R \land a \leq x \leq b \land x \neq a \land x \neq b \}$，称为从 $a$ 到 $b$ 的开区间；

​    （3）$[a， b) = \{ x | x \in R \land a \leq x \leq b \land x \neq b \}$，$(a， b] = \{ x | x \in R \land a \leq x \leq b \land x \neq a \}$ 都称为从 $a$ 到 $b$ 的半开区间；

​    （4）还可以定义下列区间

​         $(-\infty， a] = \{ x | x \in R \land x \leq a \}$，

​         $(-\infty， a) = \{ x | x \in R \land x \leq a \land x \neq a \}$，

​         $[a， \infty) = \{ x | x \in R \land a \leq x \}$，

​         $(a， \infty) = \{ x | x \in R \land a \leq x \land x \neq a \}$，

​         $(-\infty， \infty) = R$。

