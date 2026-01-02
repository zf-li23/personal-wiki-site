*在真值表的基础上，理论上我们可以研究任何命题在任何赋值下的真值情况，但这只是一种非常粗暴的方式，我们需要一些工具让我们能够更加优雅地研究命题。这部分内容比较像逻辑游戏，不妨尝试着看懂并理解每个公式，锻炼一下自己的思维能力。上一篇中最重要的内容是定义了常用逻辑联结词，那么自然地，我们可以来讨论一下等号。*

## 2.1. 等值定理

对 $A(p_1, \cdots, p_n)$ 和 $B(p_1, \cdots, p_n)$ ，如果在任一解释 $p_1, \cdots, p_n$ 下， $A$ 和 $B$ 的真值都相同，则称 $A$ 和 $B$ 是**等值**的，记为 $A = B$ 或 $A \Leftrightarrow B$ 。*等值关系是一种等价关系，具有自反性、对称性、传递性。*

**等值定理**：设 $A$ 和 $B$ 为两个命题公式，则 $A = B$ 的充分必要条件是 $A \leftrightarrow B$ 是一个重言式。

一个经典的等值公式的例子是逆否命题：

原命题： $p \to q$

逆命题： $q \to p$

否命题： $\lnot p \to \lnot q$

逆否命题： $\lnot q \to \lnot p$

![四种命题间的逆否关系](https://files.mdnice.com/user/86063/d505d8ec-4830-4ec2-8fb5-9f04bf2b011c.png)

一个命题与它的逆否命题等值： $p \to q = \lnot q \to \lnot p$

一个命题的逆命题与否命题等值： $q \to p = \lnot p \to \lnot q$

**置换规则**：设 $A$ 是 $\Phi(A)$ 的子公式，若有公式 $B$ 满足 $A = B$ ，则有 $\Phi(A) = \Phi(B)$ 。

_置换规则和代入规则的不同点在于，公式不一定需要是重言式，且可以进行公式的置换，而不是仅限于命题变项。_

## 2.2. 等值公式

为了更加灵活地使用置换规则，我们可以先推导出一些常用的**等值公式**：

*这些推导都可以用真值表证明，这种情况下讨论它们细致的证明意义不大，如果你能用接近自然语言的逻辑推理自圆其说地证明出它们，我认为意义会更大。*

1. **双重否定律**

$$
\lnot \lnot p = p
$$

2. **结合律**

$$
\begin{split}
(p \lor q) \lor r & = p \lor (q \lor r) \\
(p \land q) \land r & = p \land (q \land r) \\
(p \leftrightarrow q) \leftrightarrow r & = p \leftrightarrow (q \leftrightarrow r) \\
(p \to q) \to r & \neq p \to (q \to r) \\
\end{split}
$$

3. **交换律**

$$
\begin{split}
p \lor q & = q \lor p \\
p \land q & = q \land p \\
p \leftrightarrow q & = q \leftrightarrow p \\
p \to q & \neq q \to p \\
\end{split}
$$

4. **分配律**

$$
\begin{split}
p \lor (q \land r) & = (p \lor q) \land (p \lor r) \\
p \land (q \lor r) & = (p \land q) \lor (p \land r) \\
p \to (q \to r) & = (p \to q) \to (p \to r) \\
p \leftrightarrow (q \leftrightarrow r) & \neq (p \leftrightarrow q) \leftrightarrow (p \leftrightarrow r) \\
\end{split}
$$

5. **等幂律**/**恒等律**

$$
\begin{split}
p \lor p & = p \\
p \land p & = p \\
p \to p & = 1 \\
p \leftrightarrow p & = 1 \\
\end{split}
$$

6. **吸收律**

$$
\begin{split}
p \lor (p \land q) & = p \\
p \land (p \lor q) & = p \\
\end{split}
$$

7. **摩根律**

$$
\begin{split}
\lnot (p \lor q) & = \lnot p \land \lnot q \\
\lnot (p \land q) & = \lnot p \lor \lnot q \\
\lnot (p \to q) & = p \land \lnot q \\
\lnot (p \leftrightarrow q) & = \lnot p \leftrightarrow q = p \leftrightarrow \lnot q \\
& = (\lnot p \land q) \lor (p \land \lnot q)
\end{split}
$$

*摩根律有非常频繁地应用，应用熟练以后不止局限于这几个公式，可以推广到 **2.5. 对偶式** 中的一个结论，即：**多个命题的析（合）取取反，等于每个命题的否定之后的合（析）取。**其实我们早就接触过另一种形式的摩根律，就是小学学拆减法后面的括号时，括号里面的加减号要变号、*

8. **同一律**

$$
\begin{split}
p \lor 0 & = p \\
p \land 1 & = p \\
1 \to p & = p \\
1 \leftrightarrow p & = p \\
p \to 0 & = \lnot p \\
p \leftrightarrow 0 & = \lnot p \\
\end{split}
$$

9. **零律**

$$
\begin{split}
p \lor 1 & = 1 \\
p \land 0 & = 0 \\
p \to 1 & = 1 \\
0 \to p & = 1 \\
\end{split}
$$

10. **补余律**

$$
\begin{split}
p \lor \lnot p & = 1 \\
p \land \lnot p & = 0 \\
p \to \lnot p & = \lnot p \\
\lnot p \to p & = p \\
p \leftrightarrow \lnot p & = 0 \\
\end{split}
$$

11. 其他常用的等值公式

**蕴含等值式**：

$$
p \to q = \lnot p \lor q
$$

**假言易位**：

$$
p \to q = \lnot q \to \lnot p
$$

**前提交换**：

$$
p \to (q \to r) = q \to (p \to r)
$$

**前提合取合并**：

$$
p \to (q \to r) = (p \land q) \to r
$$

**前提析取合并**：

$$
(p \to r) \land (q \to r) = (p \lor q) \to r
$$

**等价等值式**：

$$
p \leftrightarrow q = (p \to q) \land (q \to p)
$$

**等价否定等值式**：
$$
p \leftrightarrow q = \lnot p \leftrightarrow \lnot q
$$

**从取真来描述双条件**：

$$
p \leftrightarrow q = (p \land q) \lor (\lnot p \land \lnot q)
$$

**从取假来描述双条件**：
$$
p \leftrightarrow q = (p \lor \lnot q) \land (\lnot p \lor q)
$$

**归谬论**：
$$
(p \to q) \land (p \to \lnot q) = \lnot p
$$

_介绍了命题逻辑的等值之后，我们就知道有许多形式不同的公式表达了实际上完全相同的含义，他们有完全相同的真值表，那么有没有可能形成某种规范，从中选取一个确定的式子来代表它们呢？_

## 2.3. 命题公式与真值表的关系

*从命题公式建立真值表的方法是自然的，我们已经介绍过。反之，若给定了 $p_1, \cdots, p_n$ 到 $A$ 的真值表，也可以写出 $A(p_1, \cdots, p_n)$ 的逻辑表达式：*

考查有 $n$ 个命题变项 $p_i$ 的命题公式 $A$ ，若其真值表中有 $m$ 行取 $1$，有 $k$ 行取 $0$ ，我们先不考虑真值表的严格列写顺序，（与书中稍有区别地，）让 $p_{ij}$ 代表第 $i$ 行中第 $j$ 项的真值，则真值表可以写成：

|  $p_1$   | $\cdots$ |  $p_n$   |   $A$    |
| :------: | :------: | :------: | :------: |
| $p_{11}$ | $\cdots$ | $p_{1n}$ |   $1$    |
| $\vdots$ | $\ddots$ | $\ldots$ | $\ldots$ |
| $p_{m1}$ | $\cdots$ | $p_{mn}$ |   $1$    |
| $p_{11}$ | $\cdots$ | $p_{1n}$ |   $0$    |
| $\vdots$ | $\ddots$ | $\ldots$ | $\ldots$ |
| $p_{k1}$ | $\cdots$ | $p_{kn}$ |   $0$    |

那么命题公式 $A$ 可以表示成：

- **从取 1 的行来列写**：

$$
\begin{split}
A & = q_1 \lor \cdots \lor q_m \\
q_i & = r_{i1} \land \cdots \land r_{in} \\
r_{ij} & =
\begin{cases}
p_{ij} & p_{ij} = 1 \\
\lnot p_{ij} & p_{ij} = 0
\end{cases}
\end{split}
$$

- **从取 0 的行来列写**：考查有 $n$ 个命题变项 $p_i$ 的命题公式 $A$ ，若其真值表中则命题公式 $A$ 可以表示成：

$$
\begin{split}
A & = q_1 \land \cdots \land q_k \\
q_i & = r_{i1} \lor \cdots \lor r_{in} \\
r_{ij} & =
\begin{cases}
\lnot p_{ij} & p_{ij} = 1 \\
p_{ij} & p_{ij} = 0
\end{cases}
\end{split}
$$

*从取 1 的行来列写是一个容易可以用自然语言理解的过程，也就是枚举了所有取真的情况，将从取 0 的行来列写看成是它的反面，也就是排除掉所有取假的情况，就也可以自然理解。*

## 2.4. 联结词的完备集

讨论二元运算符，对于以 $p,q$ 为命题变项的所有公式，将等值的公式视为同一类，则每个公式可以定义一个联结词与之对应，这样能够定义 16 个联结词。如果有 $n$ 个命题变项，就能定义 $2^{2^n}$ 个联结词。

除了常用联结词以外，还定义了 3 个二元联结词：

- **异或**/**不可兼或** $\overline{\lor}$ ：

$$
p \overline{\lor} q = (\lnot p \land q) \lor (p \land \lnot q)
$$

- **与非** $\uparrow$ ：

$$
p \uparrow q = \lnot (p \land q)
$$

- **或非** $\downarrow$ ：

$$
p \downarrow q = \lnot (p \lor q)
$$

| $p$  | $q$  | $p \overline{\lor} q$ | $p \uparrow q$ | $p \downarrow q$ |
| :--: | :--: | :-------------------: | :------------: | :--------------: |
|  0   |  0   |           0           |       1        |        1         |
|  0   |  1   |           1           |       1        |        0         |
|  1   |  0   |           1           |       1        |        0         |
|  1   |  1   |           0           |       0        |        0         |

明显地，表示真值表的所有逻辑并不需要这么多联结词，5个常用联结词是一定足够的。定义**联结词的完备集**，用 $C$ 表示，所有包含 $n$ 个命题变项的公式都可以由仅含在 $C$ 中的联结词表示。对于二元运算， $\{ \lnot, \land \}$、$\{ \lnot, \lor \}$、$\{ \lnot, \to \}$、$\{ \uparrow \}$、$\{ \downarrow \}$ 都是联结词的完备集。作为完备集， $\{ \lnot, \land, \lor \}$ 构成了布尔代数系统， $\{ \lnot, \to \}$ 可以用于研究逻辑系统的演绎推理， $\{ \uparrow \}$、$\{ \downarrow \}$ 在大规模集成电路中有广泛应用。

*如果感兴趣的话，可以自己试试证明以上联结词的完备集成立。可以从5个常用联结词入手，自上而下地看看哪些联结词是可省的：双蕴含是蕴含的合取，蕴含可以用蕴含等值式省去，所以 $\{ \lnot, \land, \lor \}$ 是完备集。 $p \lor q = \lor (\lnot p \land \lnot q)$ ， $p \land = \lor (\lnot p \lor \lnot q)$ ，所以 **与、或** 之一也是可省的。 $p \lor q = \lnot p \to q$ ，所以 $\{ \lnot, \to \}$ 也是完备集。在此基础上，要证明与非和或非是完备集的关键在于自下而上地表示出 $\lnot$ 和 $\land$ 或 $\lor$ ，不难发现 $\lnot p = p \uparrow p = p \downarrow p$ ，有了非之后， $p \land q = \lnot (p \uparrow q)$ 和 $p \lor q = \lnot (p \downarrow q)$ 就容易得到。*

## 2.5. 对偶式

对于仅包含 $\{ \lnot, \land, \lor \}$ 中的联结词的 $A = A(p_1, \cdots, p_n)$ ，定义 $A^- = A(\lnot p_1, \cdots, \lnot p_n)$ ，定义对偶式 $A^*$ 为将 $A$ 中所有的 $\land, \lor, 0, 1$ 分别以 $\lor, \land, 1, 0$ 替换。对偶式有许多有趣的性质，这里只进行列举，不进行证明：

- $\lnot (A^*) = (\lnot A)^*$ ， $\lnot (A^-) = (\lnot A)^-$ 
- $(A^*)^*  = A$ ， $(A^-)^-  = A$ 
- $\lnot A = (A^*)^-$ ，即一般化的摩根律
- 若 $A = B$ ，则 $A^* = B^*$ 
- 若 $A \to B$ 永真，则 $B^* \to A^*$ 永真
- $A$ 与 $A^-$ 同永真，同可满足； $\lnot A$ 与 $A^*$ 同永真，同可满足
- 若 $A$ 为重言式，则 $A^*$ 为矛盾式

## 2.6. 范式与主范式

定义命题变项 $p$ 及其否定式 $\lnot p$ 统称**文字**， $p$ 与 $\lnot p$ 称为**互补对**。

由文字的析取所组成的公式称为**析取式**，由有限个文字构成的析取式叫做**简单析取式**。一个简单析取式是重言式当且仅当它同时含有某个命题变项及它的否定式，即一个互补对。

由文字的合取所组成的公式称为**合取式**，由有限个文字构成的合取式称为**简单合取式**。一个简单合取式是矛盾式当且仅当它同时含有某个命题变项及它的否定式，即一个互补对。

**析取范式**是形如 $A_i \lor \cdots \lor A_n$ 的公式，其中 $A_i$ 是合取式。

**合取范式**是形如 $A_i \land \cdots \land A_n$ 的公式，其中 $A_i$ 是析取式。

**范式存在定理**：任一命题公式都存在与之等值的合取范式和析取范式。

*但命题公式的合取范式和析取范式并不唯一，所以有必要进一步定义主范式。*

设**极小项** $m_i = q_{i1} \land \cdots \land q_{in}$ ，其中 $q_{ij} = p_{ij}$ 或 $\lnot p_{ij}$ ， $i$ 为命题变项的取值由二进制转换为十进制*，代表真值表上取1的行*。

设**极大项** $M_i = q_{i1} \lor \cdots \lor q_{in}$ ，其中 $q_{ij} = p_{ij}$ 或 $\lnot p_{ij}$ ， $i$ 为命题变项的取值由二进制转换为十进制*，代表真值表上取0的行*。

极小项与极大项的性质：

- 对含有 $n$ 个命题变项的公式，所有可能的极小项和极大项的个数都和该公式的解释个数 $2^n$ 相同
- 每个极小项只在一个解释下为真，每个极大项只在一个解释下为假
- 极小项和极大项两两不等值， $m_i \land m_j = 0$ ， $M_i \lor M_j = 1$
- 任一含有 $n$ 个命题变项的公式 $A$ 都可以用 $k$ 个极小项的析取或 $k$ 个极大项的合取表示， $\lnot A$ 则是剩下 $2^n - k$ 个极小项的析取或极大项的合取
- 由 $2^n$ 个极小项的析取构成的公式必为重言式，由 $2^n$ 个极大项的合取构成的公式必为矛盾式

$$
\begin{split}
\bigvee_{i = 0}^{2^n - 1} m_i & = 1 \\
\bigwedge_{i = 0}^{2^n - 1} M_i & = 0 \\
\end{split}
$$

**主析取范式**：仅由极小项构成的析取范式

**主析取范式定理**：任一含有 $n$ 个命题变项的公式，都存在唯一的与之等值的且恰仅含这 $n$ 个命题变项的主析取范式

**主析取范式的符号化**：$\lor_{\cdots, i, j, \cdots} = \cdots \lor m_i \lor m_j \lor \cdots$ ，其中 $\cdots, i, j, \cdots$ 代表 $\text{真值表中取1的行号}$ 。

**主合取范式**：仅由极大项构成的合取范式

**主合取范式定理**：任一含有 $n$ 个命题变项的公式，都存在唯一的与之等值的且恰仅含这 $n$ 个命题变项的主合取范式

**主合取范式的符号化**：$\land_{\cdots, i, j, \cdots} = \cdots \land m_i \lor m_j \land \cdots$ ，其中 $\cdots, i, j, \cdots$ 代表 $2^n - \text{真值表中取0的行号}$ 。

永真式的主合取范式为空公式，矛盾式的主析取范式为空公式。

*现在我们知道，主范式利用了布尔代数联结词**与或非**的完备性，**主析取范式**和**主合取范式**其实就分别对应了前文所讲的**从取1的行列写**和**从取0的行列写**，并且在这种符号化表示下，主析取范式和主合取范式之间能非常方便地转化。*

*我们已经讨论了命题逻辑的等值和范式，但无论怎么变换，我们得到的新的命题的真值和变换前是完全一致的。但为了进行推理演算，我们需要从已有的命题经变换接近想要证明的命题，这中间不一定每一步都需要是等值的，而是也可以包括一些从强的条件推出弱的条件的步骤，这就是蕴含联结词的作用。在前面的讨论中我们总是希望去掉蕴含，但在推理中我们很希望出现蕴含这种简洁的表达形式。*

## 2.7. 推理形式

**推理形式**由**前提**和**结论**部分组成，**前提真，结论必真**的推理形式为正确的推理形式。

对 $A(p_1, \cdots, p_n)$ 和 $B(p_1, \cdots, p_n)$ ，如果当 $A$ 取值为真时， $B$ 就必取值为真，则称 $A$ **重言蕴含** $B$ ，或称 $B$ 是 $A$ 的**逻辑推论**，记为 $A \Rightarrow B$ 。重言蕴含可以带来一些自然的结论：

- 若 $A \Rightarrow B$ 成立，且 $A$ 为重言式，则 $B$ 也为重言式
- 若 $A \Rightarrow B$ 和 $B \Rightarrow A$ 同时成立，则有 $A = B$ 
- 若 $A \Rightarrow B$ 和 $B \Rightarrow C$ 同时成立，则有 $A \Rightarrow C$ 
- 若 $A \Rightarrow B$ 和 $A \Rightarrow C$ 同时成立，则有 $A \Rightarrow B \land C$ ，自然也有 $A \Rightarrow B \lor C$ 
- 若 $A \Rightarrow C$ 和 $B \Rightarrow C$ 同时成立，则有 $A \lor B \Rightarrow C$ ，自然也有 $A \land B \Rightarrow C$ 
- $A \Rightarrow B$ 的充要条件是 $A \to B$ 是重言式
- $A \Rightarrow B$ 的充要条件是 $A \land \lnot B$ 是矛盾式

## 2.8. 基本推理公式

*以下规则许多能够用自然语言理解，另一些是已有规则的推论。可以用和等值公式同样的自然语言思路看一看以下公式：*

1. $p \land q \Rightarrow p$ <p style="text-align: right;">自然的结论</p>
2. $\lnot (p \to q) \Rightarrow p$ <p style="text-align: right;">1式的推论</p>
3. $\lnot (p \to q) \Rightarrow \lnot q$ <p style="text-align: right;">1式的推论</p>
4. $p \Rightarrow p \lor q$ <p style="text-align: right;">自然的结论</p>
5. $\lnot p \Rightarrow p \to q$ <p style="text-align: right;">4式的推论，2式的逆否</p>
6. $q \Rightarrow p \to q$ <p style="text-align: right;">4式的推论，3式的逆否</p>
7. $\lnot p \land (p \lor q) \Rightarrow q$ <p style="text-align: right;">自然的结论</p>
8. $p \land (p \to q) \Rightarrow q$ <p style="text-align: right;">假言推理，分离规则</p>
9. $\lnot q \land (p \to q) \Rightarrow \lnot p$ <p style="text-align: right;">假言推理的反面</p>
10. $(p \to q) \land (q \to r) \Rightarrow p \to r$ <p style="text-align: right;">三段论</p>
11. $(p \leftrightarrow q) \land (q \leftrightarrow r) \Rightarrow p \leftrightarrow r$ <p style="text-align: right;">双向的三段论</p>
12. $(p \to r) \land (q \to r) \land (p \lor q) \Rightarrow r$ <p style="text-align: right;">三段论的推论</p>
13. $(p \to q) \land (r \to s) \land (p \lor q) \Rightarrow r \lor s$ <p style="text-align: right;">三段论的推论</p>
14. $(p \to q) \land (r \to s) \land (\lnot q \lor \lnot s) \Rightarrow \lnot p \lor \lnot r$ <p style="text-align: right;">三段论的推论</p>
15. $q \to r \Rightarrow (p \lor q) \to (p \lor r)$ <p style="text-align: right;">对 $p$ 分类讨论</p>
16. $q \to r \Rightarrow (p \to q) \to (p \to r)$ <p style="text-align: right;">对 $p$ 分类讨论</p>

## 2.9. 推理演算

推理的基本过程是从前提出发，运用基本推理公式和推理规则，逐步推演出结论。**推理规则**包括：

- 前提引入规则：推理过程中可随时引入已知前提
- 结论引入规则：中间结论可作为后续推理的前提
- 代入规则（如前所述，对重言式中的命题变项使用）
- 置换规则（如前所述，对子公式使用等值公式置换）
- 分离规则（如前所述，通过假言推理分离部分结论）
- 条件证明规则/附加前提引入：如果结论是蕴含式，可以将结论中的蕴含前件当做前提使用，结论变为蕴含后件，原因是 $p \Rightarrow q \to r$ 与 $p \land q \Rightarrow r$ 等价

*例：证明 $p \to q,q \to r$ 重言蕴含 $p \to r$*

*证明：*

*1. $p \to q$ <p style="text-align: right;">前提引入</p>*
*2. $p$ <p style="text-align: right;">附加前提引入</p>*
*3. $q$ <p style="text-align: right;">1、2分离</p>*
*4. $q \to r$ <p style="text-align: right;">前提引入</p>*
*5. $r$ <p style="text-align: right;">3、4分离</p>*

## 2.10. 归结推理法

*如前所述的推理过程多少还是需要一些灵光一现，因为规则和公式太多，需要的技巧比较高。能不能只建立一条推理规则，让计算机可以暴力地实现？那么上一篇讲的范式就派上用场了，我们又要尽可能把蕴含转化成布尔代数。*

**归结法**的证明步骤：

1. 将结论的否定 $\lnot B$ 与所有前提 $A$ 进行合取，得到一个希望被证明为矛盾式的公式 $A \land \lnot B$ 。即要证 $A \Rightarrow B$ ，等价于证 $A \land \lnot B$ 是矛盾式。
2. 将 $A \land \lnot B$ 化为合取范式 $C_1 \land \cdots \land C_n$ ，建立子句集 $S = \{ C_1, \cdots, C_n \}$ ，其中 $C_i$ 为析取式。
3. 对子句集 $S$ 中的子句做**归结**，归结的结果仍放入 $S$ 中，重复此过程。
4. 直至归结出空子句，即矛盾式。如果归结不出空子句，直至没有新子句，则 $A \land \lnot B$ 为可满足式，无法证明公式。

**归结**的推理规则：

对子句 $C_i, C_j$ 做归结，就是消去二者的互补对，需要其中有互补对。

$$
\begin{split}
C_i & = p \lor C_i' \\
C_j & = \lnot p \lor C_j' \\
\end{split}
$$

则 $C_i, C_j$ 的归结式 $R(C_i, C_j) = C_i' \lor C_j'$ ，依据是可证明 $C_i \land C_j \Rightarrow C_i' \lor C_j'$ 

*归结法是半完备的，虽然可能产生无穷演算，但可以通过去重避免，但是归结法不能证明公式不是定理。*

*前两章的内容对命题逻辑从语义出发进行了不严谨的初步的形式化，许多结论仍然可以从自然逻辑产生，比如对真值何时为真何时为假的朴素的定义。这只是逻辑学的起点，如果要继续探讨，我们可能需要再抛开真假这种具象的事情（虽然似乎已经很抽象了）。*