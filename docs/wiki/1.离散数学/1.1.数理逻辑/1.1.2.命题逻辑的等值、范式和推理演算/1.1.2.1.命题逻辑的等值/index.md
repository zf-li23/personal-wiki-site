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
