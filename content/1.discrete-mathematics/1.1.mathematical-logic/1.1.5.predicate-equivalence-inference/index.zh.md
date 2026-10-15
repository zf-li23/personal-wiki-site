---
title: 谓词逻辑的等值和推理演算
---

本章的许多内容可以由命题逻辑类推来学习：等值、范式、推理规则和归结法的概念都是从 [1.1.2](/1.1.2) 移植过来的，新的部分在于如何处理量词。因此本章也适合用来复习命题逻辑。

## 5.1. 等值式

### 5.1.1. 等值的定义

谓词逻辑中的等值建立在普遍有效性（定义 4.6.1）的基础上。

**定义 5.1.1（等值）** 设 $A$、$B$ 是一阶谓词逻辑中的公式。若 $A \leftrightarrow B$ 是**普遍有效公式**，则称 $A$ 与 $B$ **等值**，记为 $A = B$ 或 $A \Leftrightarrow B$。

### 5.1.2. 否定型等值式

否定型等值式描述量词与否定词交换位置的规律，是谓词逻辑中最基本的等值变换之一，反映了量词与否定词之间的**德摩根律**。

**公式 5.1.1（否定型等值式）**

$$
\begin{aligned}
\lnot (\forall x)P(x) & = (\exists x)\lnot P(x) \\
\lnot (\exists x)P(x) & = (\forall x)\lnot P(x)
\end{aligned}
$$

这两个公式互为对偶。它们的语义是直观的："并非所有个体都满足 $P$"等价于"存在某个个体不满足 $P$"；"不存在满足 $P$ 的个体"等价于"所有个体都不满足 $P$"。

在有限个体域 $\{a_1, a_2, \cdots, a_n\}$ 上展开（[4.5 节](/1.1.4#sec-4.5)），可以看出第一个等值式就是命题逻辑的德摩根律：

$$
\begin{aligned}
\lnot (\forall x)P(x) & = \lnot (P(a_1) \land P(a_2) \land \cdots \land P(a_n)) \\
& = \lnot P(a_1) \lor \lnot P(a_2) \lor \cdots \lor \lnot P(a_n) \\
& = (\exists x)\lnot P(x)
\end{aligned}
$$

**例 5.1.1** "并非所有的动物都是猫"。设 $A(x)$：$x$ 是动物，$B(x)$：$x$ 是猫，原语句为 $\lnot (\forall x)(A(x) \to B(x))$。利用否定型等值式：

$$
\begin{aligned}
\lnot (\forall x)(A(x) \to B(x)) & = (\exists x)\lnot (A(x) \to B(x)) \\
& = (\exists x)\lnot (\lnot A(x) \lor B(x)) \\
& = (\exists x)(A(x) \land \lnot B(x))
\end{aligned}
$$

转换后的公式意为"存在是动物但不是猫的个体"，与原句含义一致。

## 5.2. 量词分配等值式

量词分配等值式描述量词对各联结词的分配性质，是谓词公式变换和化简的关键工具。

### 5.2.1. 量词对析取和合取的分配律

当量词辖域内的公式包含一个与个体变元无关的命题变项时，量词可以"提取"出来。

**公式 5.2.1** 设 $q$ 是命题变项，与个体变元 $x$ 无关，则

$$
\begin{aligned}
(\forall x)(P(x) \lor q) & = (\forall x)P(x) \lor q \\
(\exists x)(P(x) \lor q) & = (\exists x)P(x) \lor q \\
(\forall x)(P(x) \land q) & = (\forall x)P(x) \land q \\
(\exists x)(P(x) \land q) & = (\exists x)P(x) \land q
\end{aligned}
$$

更一般地，$q$ 可以换成任何不含 $x$ 的自由出现的公式。本节其余公式中的 $p, q$ 同样如此。

### 5.2.2. 量词对蕴含的分配律

量词对蕴含的分配比较特殊，需要注意变元出现在前件还是后件。

**公式 5.2.2** 设 $p, q$ 是命题变项，与个体变元 $x$ 无关，则

$$
\begin{aligned}
(\forall x)(P(x) \to q) & = (\exists x)P(x) \to q \\
(\exists x)(P(x) \to q) & = (\forall x)P(x) \to q \\
(\forall x)(p \to Q(x)) & = p \to (\forall x)Q(x) \\
(\exists x)(p \to Q(x)) & = p \to (\exists x)Q(x)
\end{aligned}
$$

其中的规律是：量词作用于整个蕴含式时，若 $x$ 只出现在前件，则分配后量词变号（全称变存在，存在变全称）；若 $x$ 只出现在后件，则分配后量词不变。这是因为 $P(x) \to q = \lnot P(x) \lor q$，前件带着一个否定。

### 5.2.3. 全称量词对合取、存在量词对析取的分配律

当两个谓词都含有被量化的变元时，全称量词可以对合取分配，存在量词可以对析取分配。

**公式 5.2.3**

$$
\begin{aligned}
(\forall x)(P(x) \land Q(x)) & = (\forall x)P(x) \land (\forall x)Q(x) \\
(\exists x)(P(x) \lor Q(x)) & = (\exists x)P(x) \lor (\exists x)Q(x)
\end{aligned}
$$

### 5.2.4. 只有蕴含关系的情形

反过来，全称量词对析取、存在量词对合取的分配不成立等值关系，只有蕴含关系：

**公式 5.2.4**

$$
\begin{aligned}
(\forall x)P(x) \lor (\forall x)Q(x) & \Rightarrow (\forall x)(P(x) \lor Q(x)) \\
(\exists x)(P(x) \land Q(x)) & \Rightarrow (\exists x)P(x) \land (\exists x)Q(x)
\end{aligned}
$$

**例 5.2.1** 设论域为所有人，$P(x)$：$x$ 是高才生，$Q(x)$：$x$ 是运动员。$(\forall x)(P(x) \lor Q(x))$ 意为"每个人或者是高才生，或者是运动员"；$(\forall x)P(x) \lor (\forall x)Q(x)$ 意为"要么所有人都是高才生，要么所有人都是运动员"。前者为真推不出后者为真：可能一部分人是高才生，另一部分人是运动员。

### 5.2.5. 变元易名与多重量词分配

通过变元易名，可以把涉及不同个体变元的量词合并或重组。

**公式 5.2.5**

$$
\begin{aligned}
(\forall x)(\forall y)(P(x) \lor Q(y)) & = (\forall x)P(x) \lor (\forall x)Q(x) \\
(\exists x)(\exists y)(P(x) \land Q(y)) & = (\exists x)P(x) \land (\exists x)Q(x)
\end{aligned}
$$

## 5.3. 范式

范式是谓词公式的标准形式，对**判定问题**和定理证明（特别是归结法）有重要意义。

### 5.3.1. 前束范式

**定义 5.3.1（前束范式）** 设 $A$ 是一阶谓词逻辑公式。如果 $A$ 中所有量词都位于公式的最左边，这些量词前都不含否定词，并且它们的**辖域**都延伸到公式的末端，则称 $A$ 为**前束范式**（prenex normal form）。前束范式的一般形式为

$$
(Q_1 x_1)(Q_2 x_2) \cdots (Q_n x_n) M(x_1, x_2, \cdots, x_n)
$$

其中每个 $Q_i$（$1 \leq i \leq n$）为 $\forall$ 或 $\exists$，$M$ 是不含量词的公式，称为公式的**母式**（matrix），也称基式。

**定理 5.3.1（前束范式存在定理）** 一阶谓词逻辑的任一公式都存在与之等值的前束范式。

前束范式并不唯一：量词的顺序、母式的等值变换都可能导致不同的形式。

### 5.3.2. 化前束范式的基本步骤

把一个公式化为前束范式，可以按以下机械的步骤进行：

1. 消去联结词：利用 $A \to B = \lnot A \lor B$ 和 $A \leftrightarrow B = (A \to B) \land (B \to A)$，消去公式中的 $\to$ 和 $\leftrightarrow$；
2. 否定词内移：利用否定型等值式（公式 5.1.1）和**德摩根律**，把否定词移到原子谓词公式之前；
3. 变元易名：利用**变元易名规则**，使不同量词约束的变元名称不同，且与自由变元不同名，避免混淆；约束变元换名不改变公式含义；
4. 量词左移：利用量词分配等值式（[5.2 节](#sec-5.2)），把量词逐个移到公式的最左边。

**例 5.3.1** 求 $\lnot \big((\forall x)(\exists y)P(a, x, y) \to (\exists x)(\lnot (\forall y)Q(y, b) \to R(x))\big)$ 的前束范式。

$$
\begin{aligned}
& \lnot \big((\forall x)(\exists y)P(a, x, y) \to (\exists x)(\lnot (\forall y)Q(y, b) \to R(x))\big) \\
={} & (\forall x)(\exists y)P(a, x, y) \land \lnot (\exists x)(\lnot (\forall y)Q(y, b) \to R(x)) \\
={} & (\forall x)(\exists y)P(a, x, y) \land (\forall x)\big(\lnot (\forall y)Q(y, b) \land \lnot R(x)\big) \\
={} & (\forall x)(\exists y)P(a, x, y) \land (\forall x)\big((\exists y)\lnot Q(y, b) \land \lnot R(x)\big) \\
={} & (\forall x)\big((\exists y)P(a, x, y) \land (\exists z)\lnot Q(z, b) \land \lnot R(x)\big) \\
={} & (\forall x)(\exists y)(\exists z)\big(P(a, x, y) \land \lnot Q(z, b) \land \lnot R(x)\big)
\end{aligned}
$$

依次用到：$\lnot (A \to B) = A \land \lnot B$；否定型等值式与 $\lnot (A \to B) = A \land \lnot B$；否定型等值式；全称量词对合取的分配（公式 5.2.3）并将第二个 $y$ 易名为 $z$；量词左移（公式 5.2.1）。

### 5.3.3. Skolem 标准型

前束范式为进一步的标准化提供了基础，其中最重要的两种是仅含全称量词的前束范式和存在量词全在全称量词左边的前束范式，它们分别对判定公式的不可满足性和普遍有效性有特殊作用。

**定义 5.3.2（Skolem 标准型）** 对一阶谓词逻辑公式 $A$ 的前束范式，使所有存在量词都在全称量词的左边，或者只保留全称量词而消去存在量词，得到的公式称为 $A$ 的 **Skolem 标准型**（Skolem normal form）。

公式 $A$ 与它的 Skolem 标准型一般并不等值，只在某种意义下保持一致（见下面的 [5.3.4](#sec-5.3.4)、[5.3.5](#sec-5.3.5) 节）。

消去存在量词的关键是：

- **Skolem 常数**（Skolem constant）：若存在量词前没有全称量词，则用一个新常数替换它约束的变元。例如 $(\exists y)P(y)$ 化为 $P(c)$；
- **Skolem 函数**（Skolem function）：若存在量词前有全称量词，则用一个依赖于这些全称变元的新函数 $f(x_1, \cdots, x_n)$ 替换它约束的变元。例如 $(\forall x)(\exists y)P(x, y)$ 化为 $(\forall x)P(x, f(x))$。

**例 5.3.2** 求 $(\exists x)(\forall y)(\forall z)(\exists u)(\forall v)(\exists w)P(x, y, z, u, v, w)$ 的仅含全称量词的 Skolem 标准型。

1. 消去 $(\exists x)$：它前面没有全称量词，用常数 $a$ 替换 $x$；
2. 消去 $(\exists u)$：它前面有 $(\forall y)(\forall z)$，用函数 $f(y, z)$ 替换 $u$；
3. 消去 $(\exists w)$：它前面有 $(\forall y)(\forall z)(\forall v)$，用函数 $g(y, z, v)$ 替换 $w$。

最终得到 $(\forall y)(\forall z)(\forall v)P(a, y, z, f(y, z), v, g(y, z, v))$。

### 5.3.4. $\exists$ 前束范式

**定义 5.3.3（$\exists$ 前束范式）** 形如 $(\exists x_1)\cdots(\exists x_i)(\forall x_{i+1})\cdots(\forall x_n)M$ 的前束范式，即所有存在量词都在全称量词左边、且至少有一个存在量词的前束范式，称为 **$\exists$ 前束范式**。

**定理 5.3.2** 一阶谓词逻辑的任一公式 $A$ 都可以化成相应的 $\exists$ 前束范式，并且 $A$ 是普遍有效的，当且仅当它的 $\exists$ 前束范式是普遍有效的。

### 5.3.5. $\forall$ 前束范式

**定义 5.3.4（$\forall$ 前束范式）** 仅含全称量词的前束范式称为 **$\forall$ 前束范式**。它可以通过引入 Skolem 常数和 Skolem 函数消去存在量词得到。

**定理 5.3.3** 一阶谓词逻辑的任一公式 $A$ 都可以化成相应的 $\forall$ 前束范式，并且 $A$ 是不可满足的，当且仅当它的 $\forall$ 前束范式是不可满足的。

一般公式与它的 $\forall$ 前束范式并不等值，但两者在不可满足的意义下一致，这正是归结法（[5.6 节](#sec-5.6)）所需要的。

## 5.4. 基本推理公式

在一阶谓词逻辑中，从前提 $A_1, A_2, \cdots, A_n$ 推出结论 $B$ 的推理形式为 $A_1 \land A_2 \land \cdots \land A_n \to B$。若它是普遍有效的，则称推理正确，记为 $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$。基本推理公式就是一些普遍有效的蕴含式，是谓词逻辑推理演算的基础。

除了命题逻辑的推理公式（[1.1.2](/1.1.2#sec-2.8)）以外，谓词逻辑中还有以下基本推理公式：

| 编号 | 推理公式 | 说明 |
| :-: | :-- | :-- |
| 1 | $(\forall x)P(x) \lor (\forall x)Q(x) \Rightarrow (\forall x)(P(x) \lor Q(x))$ | 公式 5.2.4 |
| 2 | $(\exists x)(P(x) \land Q(x)) \Rightarrow (\exists x)P(x) \land (\exists x)Q(x)$ | 公式 5.2.4 |
| 3 | $(\forall x)(P(x) \to Q(x)) \Rightarrow (\forall x)P(x) \to (\forall x)Q(x)$ | |
| 4 | $(\forall x)(P(x) \to Q(x)) \Rightarrow (\exists x)P(x) \to (\exists x)Q(x)$ | |
| 5 | $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\forall x)P(x) \leftrightarrow (\forall x)Q(x)$ | |
| 6 | $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\exists x)P(x) \leftrightarrow (\exists x)Q(x)$ | |
| 7 | $(\forall x)(P(x) \to Q(x)) \land (\forall x)(Q(x) \to R(x)) \Rightarrow (\forall x)(P(x) \to R(x))$ | 谓词逻辑的三段论 |
| 8 | $(\forall x)(P(x) \to Q(x)) \land P(a) \Rightarrow Q(a)$ | 全称实例化推理 |
| 9 | $(\forall x)(\forall y)P(x, y) \Rightarrow (\exists x)(\forall y)P(x, y)$ | |
| 10 | $(\exists x)(\forall y)P(x, y) \Rightarrow (\forall y)(\exists x)P(x, y)$ | 逆不成立 |

**注 5.4.1** 第 10 条的逆不成立。$(\forall y)(\exists x)P(x, y)$ 意为"对每个 $y$，都存在一个 $x$ 使 $P(x, y)$ 成立"，这个 $x$ 可以依赖于 $y$（对不同的 $y$ 可以是不同的 $x$）；$(\exists x)(\forall y)P(x, y)$ 意为"存在一个 $x$，对所有 $y$ 都有 $P(x, y)$ 成立"，这个 $x$ 是统一的、不依赖于 $y$ 的。显然后者强于前者。

## 5.5. 推理演算

谓词逻辑的推理演算在命题逻辑的**推理规则**（[1.1.2](/1.1.2#sec-2.9)）的基础上，增加了处理量词的规则，形成可操作的形式推演系统。

### 5.5.1. 量词推理规则

量词推理规则是谓词逻辑推理演算的核心，共四条：

| 规则 | 形式 | 条件 |
| :-- | :-- | :-- |
| 全称量词消去（UI） | $\dfrac{(\forall x)P(x)}{P(y)}$ 或 $\dfrac{(\forall x)P(x)}{P(c)}$ | $y$ 是任意不在 $P(x)$ 中约束出现的个体变项，$c$ 是任意个体常项；必须替换 $x$ 的所有自由出现 |
| 全称量词引入（UG） | $\dfrac{P(y)}{(\forall x)P(x)}$ | $P(y)$ 对论域中任意个体 $y$ 都为真；$x$ 不在 $P(y)$ 中约束出现 |
| 存在量词消去（EI） | $\dfrac{(\exists x)P(x)}{P(c)}$ | $c$ 是使 $P$ 为真的特定个体常项，且是新的（此前未在证明中出现，也不在 $P(x)$ 中出现）；$P(x)$ 中没有其他自由出现的个体变项 |
| 存在量词引入（EG） | $\dfrac{P(c)}{(\exists x)P(x)}$ | $c$ 是特定的个体常项；$x$ 不在 $P(c)$ 中出现 |

UI 是 universal instantiation，UG 是 universal generalization，EI 是 existential instantiation，EG 是 existential generalization。

**注 5.5.1** UI 中替换 $x$ 的 $y$ 不能是 $P(x)$ 中已被约束的变元，否则会出错。例如在实数域上 $(\forall x)(\exists y)(x < y)$ 为真，若用 $y$ 替换 $x$，会错误地得到 $(\exists y)(y < y)$，它在实数域上为假。原因就是用来替换 $x$ 的 $y$ 已在 $P(x) = (\exists y)(x < y)$ 中受 $\exists y$ 约束。

**注 5.5.2** EI 要求 $c$ 是新的常项，并且 $P(x)$ 中没有其他自由变元，否则 $c$ 可能依赖于这些变元，或与已有的个体混为一谈。

### 5.5.2. 推理演算的一般过程

1. 形式化：用谓词公式符号化自然语言的前提和结论；
2. 去量词：用 UI 和 EI 消去前提中的量词，得到命题或只含自由变元的公式；
3. 命题推理：在无量词的情况下，运用命题逻辑的推理规则和推理公式进行推导；
4. 引入量词：用 UG 和 EG 给推出的中间结论或最终结论加上所需的量词。

**例 5.5.1** 证明三段论："所有的人都是要死的；苏格拉底是人；所以苏格拉底是要死的。"

设 $P(x)$：$x$ 是人，$Q(x)$：$x$ 是要死的，$s$：苏格拉底。要证 $(\forall x)(P(x) \to Q(x)) \land P(s) \Rightarrow Q(s)$。

**证明**

| 步骤 | 公式 | 依据 |
| :-: | :-- | :-- |
| 1 | $(\forall x)(P(x) \to Q(x))$ | 前提引入 |
| 2 | $P(s) \to Q(s)$ | 1，UI（用 $s$ 替换 $x$） |
| 3 | $P(s)$ | 前提引入 |
| 4 | $Q(s)$ | 2、3 分离 |

$\square$

## 5.6. 谓词逻辑的归结推理法

归结推理法是一种适用于机器自动定理证明的方法，它把命题逻辑的**归结法**（[1.1.2](/1.1.2#sec-2.10)）推广到谓词逻辑。

### 5.6.1. 基本思想

要证明 $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$，等价于证明 $G = A_1 \land A_2 \land \cdots \land A_n \land \lnot B$ 是**不可满足公式**。归结法通过推导出空子句 $\square$ 来证明 $G$ 的不可满足性。

### 5.6.2. 归结推理法步骤

**算法 5.6.1（谓词逻辑的归结法）**

1. 构造公式：$G = A_1 \land A_2 \land \cdots \land A_n \land \lnot B$；
2. 化为 Skolem 标准型：先将 $G$ 化成前束范式，再消去所有存在量词，得到 $\forall$ 前束范式 $G^*$，并把它的母式化为**合取范式**。由定理 5.3.3，$G$ 与 $G^*$ 在不可满足的意义下一致；
3. 生成子句集：略去 $G^*$ 中的所有全称量词（此时公式中的变元都被默认为全称量化），把母式的各合取项（**子句**，即简单析取式）组成子句集 $S$；
4. 归结演绎：对 $S$ 中的子句做归结，把**归结式**加入 $S$，重复这一过程，直到产生空子句 $\square$。空子句代表矛盾，证明结束。

谓词逻辑的归结需要**合一**（unification）：寻找一个替换（如 $\{x / a\}$），使两个子句中的某对文字成为互补对，然后消去这对文字，把剩余部分析取起来，得到归结式。

**例 5.6.1** 设 $C_1 = P(x) \lor Q(x)$，$C_2 = \lnot P(a) \lor R(y)$。对 $C_1$ 做替换 $\{x / a\}$ 后，$P(a)$ 与 $\lnot P(a)$ 构成互补对，归结得到 $Q(a) \lor R(y)$。

谓词逻辑归结的核心是处理含变元的原子公式：通过合一找到使原子公式互补的替换，再应用归结规则。这使归结法能够处理涉及量词的推理，为自动定理证明奠定了基础。谓词逻辑的归结法是完备的：若 $G$ 不可满足，则一定能在有限步内归结出空子句；但若 $G$ 可满足，归结过程可能永不终止。这与一阶谓词逻辑的不可判定性（定理 4.6.1）是一致的。
