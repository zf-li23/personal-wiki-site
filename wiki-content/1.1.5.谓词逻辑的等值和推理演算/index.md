*本章中的许多内容应当由命题逻辑进行类推来学习，不难发现许多概念是移植过来的，也适合对命题逻辑进行复习。*

## 5.1. 等值式

### 5.1.1. 等值的定义

在谓词逻辑中，等值关系建立在普遍有效性的基础上。设 $A$、$B$ 是一阶谓词逻辑中的公式。若 $A \leftrightarrow B$ 是**普遍有效**的公式，则称 $A$ 与 $B$ **等值**，记作 $A = B$ 或 $A \Leftrightarrow B$。

### 5.1.2. 否定型等值式

否定型等值式描述了量词与否定词交换位置的规律，是谓词逻辑中最基本的等值变换之一。否定型等值式反映了量词与否定词之间的德摩根律关系。

$$
\begin{align*}
\neg (\forall x)P(x) &\Leftrightarrow (\exists x)\neg P(x) \\
\neg (\exists x)P(x) &\Leftrightarrow (\forall x)\neg P(x)
\end{align*}
$$

这两个公式互为对偶形式。其语义是直观的：“并非所有个体都满足P”等价于“存在某个个体不满足P”；“不存在满足P的个体”等价于“所有个体都不满足P”。

**证明**（以第一个等值式为例，在有限域 $\{a_1, a_2, ..., a_n\}$ 上）：
$$
\begin{align*}
\neg \forall x P(x) &\Leftrightarrow \neg (P(a_1) \land P(a_2) \land ... \land P(a_n)) \\
&\Leftrightarrow \neg P(a_1) \lor \neg P(a_2) \lor ... \lor \neg P(a_n) \\
&\Leftrightarrow \exists x \neg P(x)
\end{align*}
$$

> **例子**：“并非所有的动物都是猫”。
>
> * 设 $A(x)$：$x$ 是动物，$B(x)$：$x$ 是猫。
> * 原语句：$\neg (\forall x)(A(x) \rightarrow B(x))$
> * 利用否定型等值式转换：

$$
\begin{align*}
\neg (\forall x)(A(x) \rightarrow B(x)) &\Leftrightarrow (\exists x)\neg (A(x) \rightarrow B(x)) \\
&\Leftrightarrow (\exists x)\neg (\neg A(x) \lor B(x)) \\
&\Leftrightarrow (\exists x)(A(x) \land \neg B(x))
\end{align*}
$$

> 转换后的公式 $(\exists x)(A(x) \land \neg B(x))$ 意为“存在是动物但不是猫的个体”，与原句含义一致。

## 5.2. 量词分配等值式

量词分配等值式描述了量词对各类逻辑联结词的分配性质，是进行谓词公式变换和简化的关键工具。

### 5.2.1. 量词对析取词和合取词的分配律（与命题变元）

当量词作用域内的公式包含一个与个体变元无关的命题变元时，量词可以“提取”出来。
$$
\begin{align*}
(\forall x)(P(x) \lor q) &\Leftrightarrow (\forall x)P(x) \lor q \\
(\exists x)(P(x) \lor q) &\Leftrightarrow (\exists x)P(x) \lor q \\
(\forall x)(P(x) \land q) &\Leftrightarrow (\forall x)P(x) \land q \\
(\exists x)(P(x) \land q) &\Leftrightarrow (\exists x)P(x) \land q
\end{align*}
$$
其中 $q$ 是命题变项，与个体变元 $x$ 无关。

### 5.2.2. 量词对蕴含词的分配律

量词对蕴含词的分配较为特殊，需要注意前件和后件的位置。
$$
\begin{align*}
(\forall x)(P(x) \rightarrow q) &\Leftrightarrow (\exists x)P(x) \rightarrow q \\
(\exists x)(P(x) \rightarrow q) &\Leftrightarrow (\forall x)P(x) \rightarrow q \\
(\forall x)(p \rightarrow Q(x)) &\Leftrightarrow p \rightarrow (\forall x)Q(x) \\
(\exists x)(p \rightarrow Q(x)) &\Leftrightarrow p \rightarrow (\exists x)Q(x)
\end{align*}
$$
其中 $p, q$ 是命题变项，与个体变元 $x$ 无关。**规律**：当量词修饰整个蕴含式时，若量词在前件($P(x)$)，则分配后量词变号（全称变存在，存在变全称）；若量词在后件($Q(x)$)，则分配后量词不变。

### 5.2.3. 全称量词对 $\land$，存在量词对 $\lor$ 的分配律

这是量词对相同量词修饰的谓词公式的分配。
$$
\begin{align*}
(\forall x)(P(x) \land Q(x)) &\Leftrightarrow (\forall x)P(x) \land (\forall x)Q(x) \\
(\exists x)(P(x) \lor Q(x)) &\Leftrightarrow (\exists x)P(x) \lor (\exists x)Q(x)
\end{align*}
$$

### 5.2.4. 重要的不等价与蕴含关系

并非所有的分配都成立等值关系，以下仅为蕴含关系：
$$
\begin{align*}
(\forall x)P(x) \lor (\forall x)Q(x) &\Rightarrow (\forall x)(P(x) \lor Q(x)) \\
(\exists x)(P(x) \land Q(x)) &\Rightarrow (\exists x)P(x) \land (\exists x)Q(x)
\end{align*}
$$

> 例如，设论域为所有人，$P(x)$: $x$ 是高才生，$Q(x)$: $x$ 是运动员。
>
> * $(\forall x)(P(x) \lor Q(x))$ 意为“每个人或者是高才生，或者是运动员”。
> * $(\forall x)P(x) \lor (\forall x)Q(x)$ 意为“要么所有人都是高才生，要么所有人都是运动员”。
>   显然，前者为真不能推出后者为真（可能一部分人是高才生，另一部分是运动员）。

### 5.2.5. 变元易名与多重量词分配

通过变元易名规则，可以将涉及不同个体变元的量词进行合并或重组。
$$
\begin{align*}
(\forall x)(\forall y)(P(x) \lor Q(y)) &\Leftrightarrow (\forall x)P(x) \lor (\forall x)Q(x) \\
(\exists x)(\exists y)(P(x) \land Q(y)) &\Leftrightarrow (\exists x)P(x) \land (\exists x)Q(x)
\end{align*}
$$

## 5.3. 范式

范式是谓词公式的一种标准形式，对于判定问题、定理证明（特别是归结法）具有重要意义。

### 5.3.1. 前束范式

**定义**：设 $A$ 为一个一阶谓词逻辑公式，如果 $A$ 中所有量词都位于该公式的最左边（且这些量词前都不含否定词），且这些量词的辖域都延伸到整个公式的末端，则称 $A$ 为**前束范式**。
前束范式的一般形式为：
$$
(Q_1 x_1)(Q_2 x_2) \cdots (Q_n x_n) M(x_1, x_2, \cdots, x_n)
$$
其中 $Q_i(1 \leq i \leq n)$ 为 $\forall$ 或 $\exists$，$M$ 为不含量词的公式，称为公式的**基式**或**母式**。

**前束范式存在定理**：一阶谓词逻辑的任一公式都存在与之等值的前束范式，但其前束范式并不唯一（量词顺序、母式等价变换均可导致不同形式）。

### 5.3.2. 化前束范式的基本步骤

将一个任意公式转化为前束范式，可遵循以下机械化步骤：

1.  **消去联结词**：利用等值式 $A \rightarrow B \Leftrightarrow \neg A \lor B$ 和 $A \leftrightarrow B \Leftrightarrow (A \rightarrow B) \land (B \rightarrow A)$，消去公式中的蕴含词($\rightarrow$)和双蕴含词($\leftrightarrow$)。
2.  **否定词内移**：利用**否定型等值式**和德摩根律，将否定词($\neg$)深入，直至直接作用于原子谓词公式。
3.  **量词左移**：利用**量词分配等值式**，将量词逐个向左（公式前端）移动。
4.  **变元易名**：利用**变元易名规则**，确保不同量词约束的变元使用不同的名称，避免混淆。约束变元的换名不改变公式含义。

**例子**：求 $\neg ((\forall x)(\exists y)P(a, x, y) \rightarrow (\exists x)(\neg (\forall y)Q(y, b) \rightarrow R(x)))$ 的前束范式。
经过上述步骤，可得到其一个前束范式为：$(\forall x)(\exists y)(\exists z)(P(a, x, y) \land \neg Q(z, b) \land \neg R(x))$。

### 5.3.3. Skolem 标准型

一阶谓词逻辑的任一公式 $A$，若其前束范式中所有的存在量词都在全称量词的左边，或是仅保留全称量词而消去存在量词，便得到公式 $A$ 的Skolem标准型。公式 $A$ 与其Skolem标准型只能保持某种意义下的等值关系。

前束范式为进一步的标准化处理提供了基础，其中最重要的两种是**仅含全称量词的前束范式**和**仅含存在量词的前束范式**。它们对于判定公式的普遍有效性和不可满足性有特殊作用。

**构造 Skolem 标准型的关键**：

*   **Skolem常数**：若存在量词是最外层且其前无全称量词，则用一个新常数替换。
    *   例如，$\exists yP(y)$ 化为 $P(c)$。
*   **Skolem函数** $f(x_1, ..., x_n)$ ：若存在量词前有全称量词，则用一个依赖于这些全称变元的新函数替换。
    *   例如，$\forall x \exists y P(x, y)$ 化为 $\forall x P(x, f(x))$。

> *   **例子**：将 $(\exists x)(\forall y)(\forall z)(\exists u)(\forall v)(\exists w)P(x, y, z, u, v, w)$ 化为 Skolem 标准型。
>     1.  消去 $(\exists x)$：用常数 $a$ 替换 $x$。
>     2.  消去 $(\exists u)$：$u$ 前有 $(\forall y)(\forall z)$，用函数 $f(y, z)$ 替换 $u$。
>     3.  消去 $(\exists w)$：$w$ 前有 $(\forall y)(\forall z)(\forall v)$，用函数 $g(y, z, v)$ 替换 $w$。
>         最终得到：$(\forall y)(\forall z)(\forall v)P(a, y, z, f(y, z), v, g(y, z, v))$。

### 5.3.4. $\exists$ 前束范式

形式为 $(\exists x_1)(\exists x_2)\cdots(\exists x_i)(\forall x_{i+1})\cdots(\forall x_n)M$，即所有存在量词都在全称量词左边，且至少有一个存在量词。
**存在定理**：一阶谓词逻辑的任一公式 $A$ 都存在与之等值的 $\exists$ 前束范式，并且 **$A$ 是普遍有效的当且仅当其 $\exists$ 前束范式是普遍有效的**。

### 5.3.5. $\forall$ 前束范式

形式为仅保留全称量词的前束范式。通过引入 Skolem 函数或 Skolem 常数消去存在量词得到。
**存在定理**：一阶谓词逻辑的任一公式 $A$ 都可化成相应的 $\forall$ 前束范式，并且 **$A$ 是不可满足的当且仅当其 $\forall$ 前束范式是不可满足的**。注意，一般公式与其 Skolem 标准型并不等值，但**在不可满足的意义下一致**。

## 5.4. 基本推理公式

基本推理公式是普遍有效的蕴涵式，是进行谓词逻辑推理演算的基础。

在一阶谓词逻辑中，从前提 $A_1, A_2, \cdots, A_n$ 出发推出结论 $B$ 的推理形式结构为 $A_1 \land A_2 \land \cdots \land A_n \rightarrow B$。若此式为永真式（普遍有效），则称推理正确，记作 $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$。

以下是除命题逻辑推理公式外，谓词逻辑中特有的一些基本推理公式：

1.  $(\forall x)P(x) \lor (\forall x)Q(x) \Rightarrow (\forall x)(P(x) \lor Q(x))$
2.  $(\exists x)(P(x) \land Q(x)) \Rightarrow (\exists x)P(x) \land (\exists x)Q(x)$
3.  $(\forall x)(P(x) \rightarrow Q(x)) \Rightarrow (\forall x)P(x) \rightarrow (\forall x)Q(x)$
4.  $(\forall x)(P(x) \rightarrow Q(x)) \Rightarrow (\exists x)P(x) \rightarrow (\exists x)Q(x)$
5.  $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\forall x)P(x) \leftrightarrow (\forall x)Q(x)$
6.  $(\forall x)(P(x) \leftrightarrow Q(x)) \Rightarrow (\exists x)P(x) \leftrightarrow (\exists x)Q(x)$
7.  $(\forall x)(P(x) \rightarrow Q(x)) \land (\forall x)(Q(x) \rightarrow R(x)) \Rightarrow (\forall x)(P(x) \rightarrow R(x))$ （谓词逻辑三段论）
8.  $(\forall x)(P(x) \rightarrow Q(x)) \land P(a) \Rightarrow Q(a)$ （全称实例化推理）
9.  $(\forall x)(\forall y)P(x,y) \Rightarrow (\exists x)(\forall y)P(x,y)$
10.  $(\exists x)(\forall y)P(x,y) \Rightarrow (\forall y)(\exists x)P(x,y)$
     *   注意其逆不成立。$(\forall y)(\exists x)P(x,y)$ 意为“对每个y，都存在一个x使得P(x,y)成立”，这个x可以依赖于y（即对不同y可以是不同的x）。
     *   $(\exists x)(\forall y)P(x,y)$ 意为“存在一个x，对所有y都有P(x,y)成立”，这个x是统一的、不依赖于y的。显然后者强于前者。

## 5.5. 推理演算

谓词逻辑的推理演算是在命题逻辑推理规则基础上，增加了处理量词的规则，从而形成的可操作的形式推演系统。

### 5.5.1. 量词推理规则

这是谓词逻辑推理演算的核心新增规则，共四条。

1. **全称量词消去规则（UI - Universal Instantiation）**
   $$
   \frac{(\forall x)P(x)}{P(y)} \quad \text{或} \quad \frac{(\forall x)P(x)}{P(c)}
   $$
   **条件**：

   *   $y$ 是任意不在 $P(x)$ 中约束出现的个体变项（代表任意个体）。
   *   $c$ 是任意个体常项。
   *   替换必须在 $x$ 自由出现的所有地方进行。
   *   **关键限制**：替换 $x$ 的 $y$ 不能是 $P(x)$ 中已被约束的变元，否则可能导致错误。例如，从 $(\forall x)(\exists y)(x<y)$ (实数域上成立) 错误地 UI 为 $(\exists y)(y<y)$ (矛盾式)，原因就是将 $x$ 替换成了已在 $P(x)$ 中受 $\exists y$ 约束的 $y$。

2. **全称量词引入规则（UG - Universal Generalization）**
   $$
   \frac{P(y)}{(\forall x)P(x)}
   $$
   **条件**：

   *   $P(y)$ 必须对论域中任意个体 $y$ 都为真。
   *   取代 $y$ 的 $x$ 不能在 $P(y)$ 中约束出现。

3. **存在量词消去规则（EI - Existential Instantiation）**
   $$
   \frac{(\exists x)P(x)}{P(c)}
   $$
   **条件**：

   *   $c$ 是使 $P$ 为真的**特定的、新的**个体常项（此前未在证明中出现）。
   *   $P(x)$ 中不能有其他自由出现的个体变项（否则 $c$ 可能依赖于这些变元）。

4. **存在量词引入规则（EG - Existential Generalization）**
   $$
   \frac{P(c)}{(\exists x)P(x)}
   $$
   **条件**：

   *   $c$ 是特定的个体常项。
   *   取代 $c$ 的 $x$ 不能在 $P(c)$ 中出现过。

| 规则名称              | 规则形式                                                     | 条件与说明                                                   |
| :-------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **全称量词消去 (UI)** | $\dfrac{(\forall x)P(x)}{P(y)}$ 或 $\dfrac{(\forall x)P(x)}{P(c)}$ | $y$ 为任意不在 $P(x)$ 中约束出现的个体变项；$c$ 为任意个体常项。必须替换 $x$ 的所有自由出现。 |
| **全称量词引入 (UG)** | $\dfrac{P(y)}{(\forall x)P(x)}$                              | 对任意 $y$，$P(y)$ 均为真；$x$ 不能在 $P(y)$ 中约束出现。    |
| **存在量词消去 (EI)** | $\dfrac{(\exists x)P(x)}{P(c)}$                              | $c$ 是使 $P$ 为真的**特定**个体常项；$c$ 不在 $P(x)$ 中出现；$P(x)$ 中无其他自由个体变项。 |
| **存在量词引入 (EG)** | $\dfrac{P(c)}{(\exists x)P(x)}$                              | $c$ 是特定的个体常项；$x$ 不在 $P(c)$ 中出现过。             |

### 5.5.2. 推理演算的一般过程

1.  **形式化**：用谓词公式符号化自然语言前提和结论。
2.  **去量词**：使用 UI 和 EI 规则，消去前提中的量词，得到命题或只含自由变元的公式。
3.  **命题推理**：在无量词环境下，运用命题逻辑的推理规则和公式进行推导。
4.  **引入量词**：使用 UG 和 EG 规则，给推导出的中间结论或最终结论加上所需的量词。

> **例子**：证明三段论“所有的人都是要死的；苏格拉底是人；所以苏格拉底是要死的。”
>
> *   形式化：$(\forall x)(P(x) \rightarrow Q(x)) \land P(s) \Rightarrow Q(s)$，其中 $P(x):x$是人，$Q(x):x$是要死的，$s$：苏格拉底。
> *   证明过程：
>     1.  $(\forall x)(P(x) \rightarrow Q(x))$ （前提引入）
>     2.  $P(s) \rightarrow Q(s)$ （UI，对1中 $x$ 用 $s$ 实例化）
>     3.  $P(s)$ （前提引入）
>     4.  $Q(s)$ （分离规则，由2和3）
>         结论得证。

## 5.6. 谓词逻辑的归结推理法

归结推理法是一种适用于机器自动定理证明的方法，它将命题逻辑的归结法推广到谓词逻辑。

### 5.6.1. 基本思想

欲证明 $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$，等价于证明 $G = A_1 \land A_2 \land \cdots \land A_n \land \neg B$ 是**不可满足的**（矛盾式）。归结法通过不断推导出空子句($\square$)来证明 $G$ 的不可满足性。

### 5.6.2. 归结推理法步骤

1. **构造矛盾式**：$G = A_1 \land A_2 \land \cdots \land A_n \land \neg B$。

2. **化为 Skolem 标准型**：

   *   将 $G$ 化成前束范式。
   *   再进行 Skolem 化，消去所有存在量词，得到仅含全称量词的 $\forall$ 前束范式 $G^*$。$G$ 与 $G^*$ 在不可满足的意义上一致。

3. **生成子句集**：

   *   略去 $G^*$ 中的所有全称量词（此时公式中的自由变元均被隐含地全称量化）。
   *   将 $G^*$ 的母式（已是合取范式）中的各合取项（子句）用逗号分隔，构成子句集 $S$。每个子句是一个析取式。

4. **归结演绎**：

   * 对子句集中的子句进行归结。**谓词逻辑的归结**需要**合一**操作：寻找一个替换（如 $\{x/a\}$），使两个子句中的某对文字（如 $P(x)$ 和 $\neg P(a)$）互补，然后消去这对文字，将剩余部分析取，得到归结式。例如：
     $$
     C_1 = P(x) \lor Q(x)
     $$

     $$
     C_2 = \neg P(a) \lor R(y)
     $$

     对 $C_1$ 应用置换 $\{x/a\}$ 后，$P(a)$ 与 $\neg P(a)$ 构成互补对，可进行归结，得到归结式 $Q(a) \lor R(y)$。

   * 将归结式加入子句集 $S$。

   * 重复归结过程，直至产生**空子句 $\square$**。空子句代表矛盾，证明结束。

**关键点**：谓词逻辑归结的核心在于处理含有变元的原子公式。通过合一找到使原子公式互补的替换，从而应用归结规则。这使得归结法能够处理涉及量词的复杂逻辑推理问题，并为自动定理证明奠定了坚实基础。