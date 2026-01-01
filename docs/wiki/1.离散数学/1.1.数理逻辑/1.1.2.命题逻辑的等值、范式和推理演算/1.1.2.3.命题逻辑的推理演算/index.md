*在前两篇中，我们讨论了命题逻辑的等值和范式，但无论怎么变换，我们得到的新的命题的真值和变换前是完全一致的。但为了进行推理演算，我们需要从已有的命题经变换接近想要证明的命题，这中间不一定每一步都需要是等值的，而是也可以包括一些从强的条件推出弱的条件的步骤，这就是蕴含联结词的作用。在前面的讨论中我们总是希望去掉蕴含，但在推理中我们很希望出现蕴含这种简洁的表达形式。*

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