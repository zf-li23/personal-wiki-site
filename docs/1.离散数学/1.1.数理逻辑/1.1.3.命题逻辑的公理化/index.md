*一门形式科学最简洁的叙述方式可以是什么样的，《几何原本》可能给出了一个答案，在第一章给出了23个定义、5个公设和5个公理，其后的每一章都写满了命题，这些命题都可以从公理和之前的命题证明出来，这就是公理化演绎系统。逻辑学的公理系统要抛弃包括真值在内的一切不明确的定义，只规定符号串之间的推理关系。那么接下来让我们忘记一切等值公式和推理规则，进入一个只由罗素公理系统定义的宇宙。*

## 3.1. 公理系统的结构

一个公理系统应当包含以下要素：

1. **初始符号**：公理系统内允许出现的全体符号的集合
2. **形成规则**：公理系统内允许出现的合法符号序列的形成方法与规则
3. **公理**：精选的最基本的重言式，作为推演其它所有重言式的依据
4. **变形规则**：公理系统所规定的推理规则
5. **定理**：所有的重言式和对它们的证明

## 3.2. 罗素公理系统

*下面我们定义命题逻辑的公理系统，我们先规定一些命题是重言式，称为公理，再由一些规则不断地生产重言式，也就是定理。这种感觉就像：神说“过相异两点，能且只能作一直线……等等”是对的，等祂说了足够多的几句话之后，人就足以顿悟出来“三角形的内角和是180度”也是对的……*

### 初始符号

大写英文字母表示命题，联结词 $\{ \lnot, \lor \}$ ，圆括号 $()$ ，断言符 $\vdash$ 。

*断言符写在公式前，用于表示公式是重言式。 $\vdash A$ 就像是“神说/我说：‘$A$ ！’”*

### 形成规则

- 表示命题的大写英文字母是合式公式
- 若 $A,B$ 是合式公式，则 $A \lor B$ 是合式公式
- 若 $A$ 是合式公式，则 $\lnot A$ 是合式公式
- 只有有限次应用上述规则形成的符号串才是合式公式

### 定义

*不做这个定义也可以，其实我们选出来的两个联结词已经是完备集了（虽然之前证过，但这个公理系统已经从头开始了，所以我们理论上还不知道），但定义出来表示着还是方便些。*

- 定义1： $A \to B$ 定义为 $\lnot A \lor B$
- 定义2： $A \land B$ 定义为 $\lnot (\lnot A \lor \lnot B)$
- 定义3： $A \leftrightarrow B$ 定义为 $(A \to B) \land (B\to A)$

### 公理

- 公理1： $\vdash (P \lor P) \to P$ <p style="text-align: right;">重言律</p>
- 公理2： $\vdash P \to (P \lor Q)$ <p style="text-align: right;">$\lor$ 引入律</p>
- 公理3： $\vdash (P \lor Q) \to (Q \lor P)$ <p style="text-align: right;">析取交换律</p>
- 公理4： $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ <p style="text-align: right;">基本推理公式15</p>

*虽然这些公理的重言是我们定义出来的，但直观上我们也能理解他们是重言的。但问题是，重言的式子那么多，为什么就选了这4个作为公理？最重要的答案当然是数量少，但也不是最少的，毕竟还有只有三条公理的命题逻辑公理系统，所以可能也考虑到了推导另外的一些重要的重言式方便一些。*

### 变形规则

*都是我们的老熟人，之前在推理规则或以前都见过了。*

  - 代入规则：如果 $\vdash A$ ，那么 $\vdash A {\pi \over B}$
  - 置换规则：**定义**的左右两边可互相置换
  - 分离规则：如果 $\vdash A$ ， $\vdash A \to B$ ，那么 $\vdash B$ 

### 定理

定理的证明必须依据公理或已证明的定理，同时证明的过程（符号的变换过程）必须依据变形规则。*那么让我们开始写吧！*

1. $\vdash (Q \to R) \to ((P \lor Q) \to (P \lor R))$ <p style="text-align: right;">公理4</p>
2. $\vdash (Q \to R) \to ((\lnot P \lor Q) \to (\lnot P \lor R))$ <p style="text-align: right;">1代入 $P \over \lnot P$</p>
3. $\vdash (Q \to R) \to ((P \to Q) \to (P \to R))$ <p style="text-align: right;">2定义1</p>
4. $\vdash P \to P \lor Q$ <p style="text-align: right;">公理2</p>
5. $\vdash P \to P \lor P$ <p style="text-align: right;">4代入 $Q \over P$</p>
6. $\vdash P \lor P \to P$ <p style="text-align: right;">公理1</p>
7. $\vdash (P \lor P \to P) \to ((P \to P \lor P) \to (P \to P))$ <p style="text-align: right;">3代入 ${Q \over P \lor P},{R \over P}$</p>
8. $\vdash (P \to P \lor P) \to (P \to P)$ <p style="text-align: right;">6,7分离</p>
9. $\vdash P \to P$ <p style="text-align: right;">5,8分离</p>
10. $\vdash \lnot P \lor P$ <p style="text-align: right;">9定义1</p>
11. $\vdash (P \lor Q) \to (Q \lor P)$ <p style="text-align: right;">公理3</p>
12. $\vdash (\lnot P \lor P) \to (P \lor \lnot P)$ <p style="text-align: right;">11代入 ${P \over \lnot P},{Q \over P}$</p>
13. $\vdash P \lor \lnot P$ <p style="text-align: right;">10,12分离</p>
14. $\vdash \lnot P \lor \lnot \lnot P$ <p style="text-align: right;">13代入 $P \over \lnot P$</p>
15. $\vdash P \to \lnot \lnot P$ <p style="text-align: right;">14定义1</p>

*可见罗素公理系统证明步骤之繁琐，如果随便丢给你一个重言式要求你用罗素公理系统证明，大概真的很需要灵感和时间。如果考试要考的话，可能也会先给出一些已证明的定理供你使用。*

*那么写到这里我们大概会有些疑问：罗素公理系统能写出所有重言式吗？以及就这样无脑地写下去而不用真值表判断，有没有可能某一步突然就不是重言式了呢？幸运的是，罗素公理系统是一个具有完备性和可靠性的系统。*

## 3.3. 公理系统的完备性和演绎定理

这部分内容定义了公理系统的完备性、可靠性、语义完备性、语义无矛盾性、命题演算的有穷可判定性等等概念，给出了证明罗素公理系统具有这些性质的方法。

*但我对这里的证明实在不感兴趣，所以就不想详细介绍了。除了罗素公理系统以外，还有其他具有这些性质的公理系统。*

## 3.4. 王浩算法

简单来说，王浩算法也是一种命题逻辑公理系统，它实现了定理证明的自动化，更适合计算机实现。王浩算法只有1条公理，但直接引入了5个常用联结词，定义了相继式和前件规则与后件规则各5条，共10条变形规则。定理推演的过程将所要证明的定理写成相继式形式，然后反复使用变形规则，消去全部联结词以得到一个或多个无联结词的相继式若所有无联结词的相继式都是公理，则定理得证，否则定理不成立。

***因为我对王浩算法不是很有兴趣，它和逻辑学的主线偏离得也比较多，所以以下内容的总结借助了AI工具，请仔细甄别其中的内容。***

### 1. **王浩算法的基本概念**

王浩算法的核心是通过变形规则（推理规则）逐步消去公式中的逻辑联结词，最终将问题简化为公理的形式。如果所有简化后的公理都成立，则原命题成立；否则，命题不成立。

### 2. **符号定义**

王浩算法引入了以下符号和定义：

#### **相继式（Sequent）**

- **定义**：如果 $ \alpha $ 和 $ \beta $ 是公式串，则称 $ \alpha \Rightarrow \beta $ 是一个相继式。
- **前件**：$ \alpha $ 是前件，表示公式串的左边部分。
- **后件**：$ \beta $ 是后件，表示公式串的右边部分。
- **含义**：当 $ \alpha $ 中的所有公式均为真时，$ \beta $ 中至少有一个公式为真。

#### **公式串**

- 公式串 $ \alpha $ 和 $ \beta $ 是由命题公式组成的序列，例如 $ \alpha = A_1, A_2, \dots, A_m $ 和 $ \beta = B_1, B_2, \dots, B_n $。

- **前件的合取**：$ \alpha $ 表示为 $ \bigwedge_{i=1}^{m} A_i $。

- **后件的析取**：$ \beta $ 表示为 $ \bigvee_{j=1}^{n} B_j $。

- 因此，相继式 $ \alpha \Rightarrow \beta $ 可以表示为：

  $$
  \bigwedge_{i=1}^{m} A_i \Rightarrow \bigvee_{j=1}^{n} B_j
  $$

### 3. **公理**

王浩算法的公理非常简单，只有一条：

- **公理**：如果公式串 $ \alpha $ 和 $ \beta $ 中的公式仅包含命题变项 $ A, B, \dots $，则 $ \alpha \Rightarrow \beta $ 是公理的充分必要条件是 $ \alpha $ 和 $ \beta $ 中至少有一个相同的命题变项。

### 4. **变形规则（推理规则）**

变形规则分为前件规则和后件规则，用于逐步消去联结词。以下是主要的变形规则：

#### **前件规则**

1. **否定规则（$ \neg \Rightarrow $）**：

   如果 $ \alpha, \beta \Rightarrow X, \gamma $，则 $ \alpha, \neg X, \beta \Rightarrow \gamma $

2. **合取规则（$ \land \Rightarrow $）**：

   如果 $ X, Y, \alpha, \beta \Rightarrow \gamma $，则 $ \alpha, X \land Y, \beta \Rightarrow \gamma $

3. **析取规则（$ \vee \Rightarrow $）**：

   如果 $ X, \alpha, \beta \Rightarrow \gamma $ 且 $ Y, \alpha, \beta \Rightarrow \gamma $，则 $ \alpha, X \vee Y, \beta \Rightarrow \gamma $

4. **蕴含规则（$ \rightarrow \Rightarrow $）**：

   如果 $ Y, \alpha, \beta \Rightarrow \gamma $ 且 $ \alpha, \beta \Rightarrow X, \gamma $，则 $ \alpha, X \rightarrow Y, \beta \Rightarrow \gamma $

5. **等价规则（$ \leftrightarrow \Rightarrow $）**：

   如果 $ X, Y, \alpha, \beta \Rightarrow \gamma $ 且 $ \alpha, \beta \Rightarrow X, Y, \gamma $，则 $ \alpha, X \leftrightarrow Y, \beta \Rightarrow \gamma $

#### **后件规则**

1. **否定规则（$ \Rightarrow \neg $）**：

   如果 $ X, \alpha \Rightarrow \beta, \gamma $，则 $ \alpha \Rightarrow \beta, \neg X, \gamma $

2. **合取规则（$ \Rightarrow \land $）**：

   如果 $ \alpha \Rightarrow X, \beta, \gamma $ 且 $ \alpha \Rightarrow Y, \beta, \gamma $，则 $ \alpha \Rightarrow \beta, X \land Y, \gamma $

3. **析取规则（$ \Rightarrow \vee $）**：

   如果 $ \alpha \Rightarrow X, Y, \beta, \gamma $，则 $ \alpha \Rightarrow \beta, X \vee Y, \gamma $

4. **蕴含规则（$ \Rightarrow \rightarrow $）**：

   如果 $ X, \alpha \Rightarrow Y, \beta, \gamma $，则 $ \alpha \Rightarrow \beta, X \rightarrow Y, \gamma $

5. **等价规则（$ \Rightarrow \leftrightarrow $）**：

   如果 $ X, \alpha \Rightarrow Y, \beta, \gamma $ 且 $ Y, \alpha \Rightarrow X, \beta, \gamma $，则 $ \alpha \Rightarrow \beta, X \leftrightarrow Y, \gamma $

### 5. **定理推演过程**

王浩算法的定理推演过程如下：

1. **写成相继式**：将要证明的定理 $ A_1 \land A_2 \land \dots \land A_n \rightarrow B $ 写成相继式形式：

   $$
   A_1, A_2, \dots, A_n \Rightarrow B
   $$

2. **反复使用变形规则**：反复使用变形规则，逐步消去所有逻辑联结词，直到得到无联结词的相继式。

3. **验证公理**：如果所有无联结词的相继式都是公理，则原命题成立；否则，命题不成立。

### 6. **王浩算法的特点**

- **完备性**：王浩算法可以证明命题逻辑中的所有定理，因此是完备的。
- **机械化**：该算法可以通过计算机实现，使得定理证明过程自动化。
- **效率**：通过反向使用变形规则，逐步简化问题，提高了证明的效率。

*这么抽象的内容写一篇就足够了，属实超出我的思维能力范围，接下来我们还是讨论具象一些的语言吧。*