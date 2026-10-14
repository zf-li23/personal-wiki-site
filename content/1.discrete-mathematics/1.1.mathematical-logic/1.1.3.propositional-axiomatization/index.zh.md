---
title: 命题逻辑的公理化
---

一门形式科学最简洁的叙述方式可以是什么样的？《几何原本》也许给出了一个答案：第一卷先给出 23 个定义、5 个公设和 5 个公理，其后每一卷都写满了命题，这些命题都可以从公理和之前的命题证明出来，这就是公理化演绎系统。逻辑学的公理系统要抛弃包括真值在内的一切不明确的概念，只规定符号串之间的推演关系。那么接下来，让我们忘记前两章的一切等值公式和推理规则，进入一个只由罗素公理系统定义的宇宙。最后再介绍另一种更适合计算机的系统：王浩算法。

## 3.1. 公理系统的结构

一个**公理系统**（axiomatic system）包含以下要素：

1. **初始符号**：系统内允许出现的全体符号的集合；
2. **形成规则**：由初始符号构成合法符号序列（公式）的规则；
3. **公理**：精选的最基本的重言式，作为推演其他所有重言式的依据；
4. **变形规则**：系统所规定的推理规则；
5. **定理**：由公理出发、按变形规则推出的公式，以及对它们的证明。

## 3.2. 罗素公理系统

下面定义命题逻辑的罗素公理系统：先规定一些公式是重言式，称为公理，再用一些规则不断地生成重言式，也就是定理。这种感觉就像：神说"过相异两点，能且只能作一直线……"是对的，等祂说了足够多的话之后，人就足以顿悟出"三角形的内角和是 180 度"也是对的。

### 3.2.1. 初始符号

- 命题变项：大写英文字母 $P, Q, R, \cdots$；
- 联结词：$\lnot, \lor$；
- 圆括号：$($、$)$；
- 断言符：$\vdash$。

断言符写在公式前，表示该公式是系统的定理（重言式）。$\vdash A$ 就像是"神说：'$A$！'"

### 3.2.2. 形成规则

1. 命题变项是合式公式；
2. 若 $A, B$ 是合式公式，则 $(A \lor B)$ 是合式公式；
3. 若 $A$ 是合式公式，则 $\lnot A$ 是合式公式；
4. 只有有限次应用上述规则形成的符号串才是合式公式。

### 3.2.3. 定义

系统只有 $\lnot$ 和 $\lor$ 两个联结词。其实它们已经构成完备集（定理 2.4.1；不过这个公理系统是从头开始的，所以理论上我们在系统内还不知道这一点），其他联结词可以作为缩写来定义，这样表示起来方便些：

**定义 3.2.1** $A \to B$ 定义为 $\lnot A \lor B$。

**定义 3.2.2** $A \land B$ 定义为 $\lnot (\lnot A \lor \lnot B)$。

**定义 3.2.3** $A \leftrightarrow B$ 定义为 $(A \to B) \land (B \to A)$。

### 3.2.4. 公理

| 公理 | 公式 | 名称 |
| :-: | :-- | :-- |
| 1 | $\vdash (P \lor P) \to P$ | 重言律 |
| 2 | $\vdash P \to (P \lor Q)$ | $\lor$ 引入律 |
| 3 | $\vdash (P \lor Q) \to (Q \lor P)$ | 析取交换律 |
| 4 | $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ | [基本推理公式](/1.1.2#sec-2.8)第 15 条 |

这些公式在系统中是规定为定理的，但直观上我们也能理解它们是重言式。问题是，重言式那么多，为什么偏偏选了这 4 个作为公理？最重要的原因当然是数量少；但这还不是最少的，毕竟还有只用三条公理的命题逻辑公理系统，所以选择时可能也考虑了推导其他一些重要的重言式是否方便。

### 3.2.5. 变形规则

这些规则都是老熟人，在 [1.1.2](/1.1.2#sec-2.9) 的推理规则中都见过：

- **代入规则**：如果 $\vdash A$，那么 $\vdash A\dfrac{\pi}{B}$，其中 $\pi$ 是 $A$ 中的命题变项，$B$ 是任一合式公式，并且要代换 $\pi$ 的所有出现；
- **置换规则**：定义 3.2.1–3.2.3 的左右两边可以互相置换；
- **分离规则**：如果 $\vdash A$ 且 $\vdash A \to B$，那么 $\vdash B$。

### 3.2.6. 定理

定理的证明必须依据公理或已证明的定理，证明的每一步（符号的变换）都必须依据变形规则。那么让我们开始写吧！

**定理 3.2.1** $\vdash (Q \to R) \to ((P \to Q) \to (P \to R))$。

**定理 3.2.2** $\vdash P \to P$。

**定理 3.2.3** $\vdash P \lor \lnot P$。

**定理 3.2.4** $\vdash P \to \lnot \lnot P$。

**证明** 下面的推演中，第 3 行是定理 3.2.1，第 9 行是定理 3.2.2，第 13 行是定理 3.2.3，第 15 行是定理 3.2.4。

| 步骤 | 公式 | 依据 |
| :-: | :-- | :-- |
| 1 | $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ | 公理 4 |
| 2 | $\vdash (Q \to R) \to ((\lnot P \lor Q) \to (\lnot P \lor R))$ | 1 代入 $\dfrac{P}{\lnot P}$ |
| 3 | $\vdash (Q \to R) \to ((P \to Q) \to (P \to R))$ | 2 用定义 3.2.1 置换 |
| 4 | $\vdash P \to (P \lor Q)$ | 公理 2 |
| 5 | $\vdash P \to (P \lor P)$ | 4 代入 $\dfrac{Q}{P}$ |
| 6 | $\vdash (P \lor P) \to P$ | 公理 1 |
| 7 | $\vdash ((P \lor P) \to P) \to ((P \to (P \lor P)) \to (P \to P))$ | 3 代入 $\dfrac{Q}{P \lor P}, \dfrac{R}{P}$ |
| 8 | $\vdash (P \to (P \lor P)) \to (P \to P)$ | 6、7 分离 |
| 9 | $\vdash P \to P$ | 5、8 分离 |
| 10 | $\vdash \lnot P \lor P$ | 9 用定义 3.2.1 置换 |
| 11 | $\vdash (P \lor Q) \to (Q \lor P)$ | 公理 3 |
| 12 | $\vdash (\lnot P \lor P) \to (P \lor \lnot P)$ | 11 代入 $\dfrac{P}{\lnot P}, \dfrac{Q}{P}$ |
| 13 | $\vdash P \lor \lnot P$ | 10、12 分离 |
| 14 | $\vdash \lnot P \lor \lnot \lnot P$ | 13 代入 $\dfrac{P}{\lnot P}$ |
| 15 | $\vdash P \to \lnot \lnot P$ | 14 用定义 3.2.1 置换 |

$\square$

可见罗素公理系统的证明步骤相当繁琐。如果随便给出一个重言式，要求用罗素公理系统证明，大概真的很需要灵感和时间；如果考试要考，可能也会先给出一些已证明的定理供使用。

写到这里，我们大概会有些疑问：罗素公理系统能推出所有重言式吗？这样不借助真值表地推下去，会不会某一步突然推出了不是重言式的公式？幸运的是，罗素公理系统既是可靠的，也是完备的。

## 3.3. 公理系统的完备性和演绎定理

本节只列出结论，不给出证明。

**定义 3.3.1（可靠性与完备性）** 若一个公理系统的每个定理都是重言式，则称它是**可靠的**；若每个重言式都是它的定理，则称它是（语义）**完备的**。

**定义 3.3.2（无矛盾性）** 若不存在公式 $A$ 使 $\vdash A$ 与 $\vdash \lnot A$ 同时成立，则称公理系统是**无矛盾的**（一致的）。

**定理 3.3.1** 罗素公理系统是可靠的、无矛盾的，并且是完备的：一个公式是它的定理，当且仅当这个公式是重言式。

由于任一公式是否为重言式都能用真值表在有限步内判定，命题演算是**可判定的**。

**定理 3.3.2（演绎定理）** 设 $\Gamma$ 是公式集。若以 $\Gamma$ 中的公式和 $A$ 为前提（对前提不使用代入规则）能推出 $B$，记为 $\Gamma, A \vdash B$，则 $\Gamma \vdash A \to B$。

演绎定理就是条件证明规则（[1.1.2](/1.1.2#sec-2.9)）在公理系统中的对应，用它可以大大简化公理系统中的证明。除了罗素公理系统以外，还有其他具有这些性质的公理系统。

## 3.4. 王浩算法

> 作者注：我对王浩算法兴趣不大，它和逻辑学的主线偏离得也比较多，所以本节内容的总结借助了 AI 工具，请仔细甄别。

**王浩算法**（Wang Hao's algorithm）也是一种命题逻辑的形式系统，它使定理证明可以自动化，更适合计算机实现。它只有 1 条公理，但直接使用 5 个常用联结词，定义了相继式，以及前件规则与后件规则各 5 条，共 10 条变形规则。

### 3.4.1. 基本思想

将要证明的定理写成相继式，然后反复使用变形规则，每次消去一个联结词，最终得到一个或多个不含联结词的相继式。若所有不含联结词的相继式都是公理，则定理得证；否则定理不成立。

### 3.4.2. 相继式

**定义 3.4.1（相继式）** 设 $\alpha = A_1, \cdots, A_m$ 与 $\beta = B_1, \cdots, B_n$ 是公式串（由公式组成的有限序列，可以为空），则称 $\alpha \Rightarrow \beta$ 为一个**相继式**（sequent），$\alpha$ 称为它的**前件**，$\beta$ 称为它的**后件**。

相继式 $\alpha \Rightarrow \beta$ 的含义是：当 $\alpha$ 中的公式全部为真时，$\beta$ 中至少有一个公式为真。也就是说，前件中的公式以合取相连，后件中的公式以析取相连：

$$
\bigwedge_{i=1}^{m} A_i \Rightarrow \bigvee_{j=1}^{n} B_j
$$

约定空的前件为真，空的后件为假。这里的 $\Rightarrow$ 与重言蕴含（定义 2.7.1）用同一个符号，含义也一致：相继式成立，当且仅当 $\bigwedge_i A_i \to \bigvee_j B_j$ 是重言式。

### 3.4.3. 公理

王浩算法只有一条公理：

- **公理**：若公式串 $\alpha$ 和 $\beta$ 都只由命题变项组成，则 $\alpha \Rightarrow \beta$ 是公理，当且仅当 $\alpha$ 和 $\beta$ 中至少含有一个相同的命题变项。

### 3.4.4. 变形规则

变形规则分为前件规则和后件规则，每条规则都消去一个联结词。下面 $\alpha, \beta, \gamma$ 是公式串，$X, Y$ 是公式；"如果……则……"表示由上方（一个或两个）相继式可以得到下方的相继式。

**前件规则**

| 规则 | 如果 | 则 |
| :-- | :-- | :-- |
| $\lnot \Rightarrow$ | $\alpha, \beta \Rightarrow X, \gamma$ | $\alpha, \lnot X, \beta \Rightarrow \gamma$ |
| $\land \Rightarrow$ | $X, Y, \alpha, \beta \Rightarrow \gamma$ | $\alpha, X \land Y, \beta \Rightarrow \gamma$ |
| $\lor \Rightarrow$ | $X, \alpha, \beta \Rightarrow \gamma$ 且 $Y, \alpha, \beta \Rightarrow \gamma$ | $\alpha, X \lor Y, \beta \Rightarrow \gamma$ |
| $\to \Rightarrow$ | $Y, \alpha, \beta \Rightarrow \gamma$ 且 $\alpha, \beta \Rightarrow X, \gamma$ | $\alpha, X \to Y, \beta \Rightarrow \gamma$ |
| $\leftrightarrow \Rightarrow$ | $X, Y, \alpha, \beta \Rightarrow \gamma$ 且 $\alpha, \beta \Rightarrow X, Y, \gamma$ | $\alpha, X \leftrightarrow Y, \beta \Rightarrow \gamma$ |

**后件规则**

| 规则 | 如果 | 则 |
| :-- | :-- | :-- |
| $\Rightarrow \lnot$ | $X, \alpha \Rightarrow \beta, \gamma$ | $\alpha \Rightarrow \beta, \lnot X, \gamma$ |
| $\Rightarrow \land$ | $\alpha \Rightarrow X, \beta, \gamma$ 且 $\alpha \Rightarrow Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \land Y, \gamma$ |
| $\Rightarrow \lor$ | $\alpha \Rightarrow X, Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \lor Y, \gamma$ |
| $\Rightarrow \to$ | $X, \alpha \Rightarrow Y, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \to Y, \gamma$ |
| $\Rightarrow \leftrightarrow$ | $X, \alpha \Rightarrow Y, \beta, \gamma$ 且 $Y, \alpha \Rightarrow X, \beta, \gamma$ | $\alpha \Rightarrow \beta, X \leftrightarrow Y, \gamma$ |

可以按相继式的含义理解这些规则。例如前件中的 $\lnot X$ 为真即 $X$ 为假，所以可以把 $X$ 移到后件；前件中的 $X \to Y$ 为真，即"$Y$ 为真"或"$X$ 为假"，于是分成两种情况。

### 3.4.5. 定理推演过程

**算法 3.4.1（王浩算法）**

1. **写成相继式**：把要证明的定理 $A_1 \land \cdots \land A_n \to B$ 写成相继式 $A_1, \cdots, A_n \Rightarrow B$（要证 $A$ 是定理时写成 $\Rightarrow A$）；
2. **反向使用变形规则**：从这个相继式出发，找出由哪些相继式可以得到它，逐步消去所有联结词，直到只剩不含联结词的相继式；
3. **验证公理**：如果所有不含联结词的相继式都是公理，则原定理得证；否则原公式不是定理。

**例 3.4.1** 用王浩算法证明 $(P \to Q) \to (\lnot Q \to \lnot P)$。

| 步骤 | 相继式 | 依据 |
| :-: | :-- | :-- |
| 1 | $\Rightarrow (P \to Q) \to (\lnot Q \to \lnot P)$ | 待证 |
| 2 | $P \to Q \Rightarrow \lnot Q \to \lnot P$ | 由 1，$\Rightarrow \to$ |
| 3 | $\lnot Q, P \to Q \Rightarrow \lnot P$ | 由 2，$\Rightarrow \to$ |
| 4 | $P, \lnot Q, P \to Q \Rightarrow$ | 由 3，$\Rightarrow \lnot$ |
| 5 | $P, P \to Q \Rightarrow Q$ | 由 4，$\lnot \Rightarrow$ |
| 6 | $Q, P \Rightarrow Q$ | 由 5，$\to \Rightarrow$（第一支），公理 |
| 7 | $P \Rightarrow P, Q$ | 由 5，$\to \Rightarrow$（第二支），公理 |

第 6、7 行都不含联结词且两边有相同的命题变项，都是公理，所以原公式得证。

### 3.4.6. 王浩算法的特点

- **可靠且完备**：王浩算法证明的都是重言式，并且能证明命题逻辑中的所有重言式；
- **机械化**：每用一次变形规则就消去一个联结词，推演必然在有限步内结束，并给出"是定理"或"不是定理"的结论，因此可以由计算机实现，使定理证明自动化；
- **方向明确**：从要证的结论出发反向使用变形规则，每一步只需看当前相继式中的联结词，不需要像罗素公理系统那样寻找合适的代入。

这么抽象的内容写一章就足够了，接下来我们还是讨论具体一些的语言——谓词逻辑。
