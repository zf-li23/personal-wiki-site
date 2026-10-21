---
title: Arithmetic Circuits
description: Half adders and full adders; the ripple-carry adder and its delay; carry generate and propagate functions, the carry-lookahead adder, grouped and multilevel lookahead, and parallel-prefix adders; two's complement addition and subtraction, overflow and comparison; the structure of the arithmetic logic unit and the 74181 as a historical comparison; an introduction to multipliers.
source_hash: 53842239d988
---

Addition is the most basic operation in a computer: subtraction, comparison, address computation, multiplication and division are all built on adders. This chapter designs adders with the methods of [Combinational Logic Circuits](/4.9.4), starting from the one-bit half adder and full adder and proceeding to the multi-bit ripple-carry adder. The delay of ripple carry grows linearly with the number of bits, which leads to the central idea of the chapter: view the computation of the carries itself as a logic function that can be parallelized (carry lookahead and parallel prefix). We then use the adder to perform subtraction in **two's complement**, discuss the detection of **overflow** and comparison, and finally combine the various operations into the arithmetic logic unit (ALU). The representation of numbers in computers is in [Number Representation in Computers](/3.5.1); how the arithmetic unit of a processor uses the ALU described here is in the chapter on the arithmetic unit of [Computer Organization](/4.10).

In this chapter $A = A_{n-1}\cdots A_1A_0$ and $B$ are two $n$-bit binary numbers, subscript $0$ is the least significant bit, $C_i$ denotes the carry into bit $i$, $C_0$ is the carry input of the whole adder, and $C_n$ is its carry output.

## 5.1. Adders

### 5.1.1. Half Adders and Full Adders

**Definition 5.1.1 (Half Adder and Full Adder)** A circuit that adds two one-bit binary numbers $A$ and $B$, producing the sum bit $S$ and the carry $C$ to the higher bit without considering a carry from the lower bit, is called a **half adder**; a circuit that adds $A$, $B$ and the carry $C_{\mathrm{in}}$ from the lower bit, producing the sum bit $S$ and the carry output $C_{\mathrm{out}}$, is called a **full adder**.

Half adder: $S = A \oplus B$, $C = AB$. The **truth table** of the full adder:

| $A$ | $B$ | $C_{\mathrm{in}}$ | $C_{\mathrm{out}}$ | $S$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

That is, $A + B + C_{\mathrm{in}} = 2C_{\mathrm{out}} + S$. $S$ is $1$ when the number of $1$s among the three inputs is odd, so it is the parity function of three variables; $C_{\mathrm{out}}$ is $1$ when at least two inputs are $1$, so it is the majority function of three variables ([Example 4.1.2](/4.9.4#ex-4.1.2)):

$$
S = A \oplus B \oplus C_{\mathrm{in}},\qquad C_{\mathrm{out}} = AB + AC_{\mathrm{in}} + BC_{\mathrm{in}} = AB + (A \oplus B)\,C_{\mathrm{in}} .
$$
The **Karnaugh map** of $S$ is a checkerboard, with no two adjacent $1$s, so it cannot be minimized; written as a sum of products it needs four three-variable product terms.

![Left: a full adder made of two half adders and an OR gate; right: four full adders connected in series to form a 4-bit ripple-carry adder](./plots/full-adder.py)

The last equation gives the commonly used structure: the first half adder computes $A \oplus B$ and $AB$, the second half adder adds $A \oplus B$ and $C_{\mathrm{in}}$, and the two carries are ORed to give $C_{\mathrm{out}}$ (the carries of the two half adders are never $1$ at the same time, so OR replaces addition).

The full adder has a useful symmetry: if all three inputs are complemented, both outputs are complemented too ($\overline{S}$ and $\overline{C_{\mathrm{out}}}$ are the sum and carry of $\overline{A}, \overline{B}, \overline{C_{\mathrm{in}}}$). Because a single-stage CMOS gate naturally produces an inverted signal ([Logic Gates and Their Electrical Characteristics](/4.9.3)), a multi-bit adder is often built from two mutually inverting kinds of full adders connected alternately for odd and even bits, which saves the inverters on the carry chain; the "two kinds of one-bit adders connected alternately" in Chinese textbooks is exactly this trick, which the mirror adder in CMOS also exploits.

### 5.1.2. Ripple-Carry Adders

**Definition 5.1.2 (Ripple-Carry Adder)** Connecting $n$ full adders in series, with the carry output of bit $i$ connected to the carry input of bit $i+1$, gives an $n$-bit **ripple-carry adder**.

It has a simple structure and a small area ($n$ full adders), but it is slow: the carry of bit $i$ can be determined only after the carry of bit $i-1$ has been computed, and in the worst case (such as $0111\cdots1 + 0000\cdots1$) the carry must propagate from the lowest bit all the way to the highest. If the carry output takes a delay of $t_c$ and the sum bit takes $t_s$, then

$$
t_{\text{ripple}} \approx (n-1)\,t_c + \max(t_c, t_s) = O(n).
$$
For example, if the carry takes $2$ gate levels and the sum takes $3$, then for a $4$-bit adder $C_4$ needs $8$ levels and $S_3$ needs $9$; for $32$ bits and $64$ bits, over sixty and over one hundred levels are needed, respectively, far from meeting the requirement that a processor complete an addition within one clock cycle.

## 5.2. Carry-Lookahead Adders

### 5.2.1. Carry Generate and Carry Propagate Functions

Consider when bit $i$ produces a carry to the higher bit: when $A_i = B_i = 1$, it carries regardless of whether there is a carry from the lower bit; when exactly one of $A_i$ and $B_i$ is $1$, a carry from the lower bit is "propagated" through; when $A_i = B_i = 0$, there is no carry. Define

$$
G_i = A_iB_i,\qquad P_i = A_i \oplus B_i ,
$$
called the carry generate function and the carry propagate function of bit $i$, respectively. They depend only on the inputs of this bit and can be computed for all bits simultaneously. Then

$$
C_{i+1} = G_i + P_iC_i,\qquad S_i = P_i \oplus C_i .
$$
(In the carry formula $P_i$ can also be taken as $A_i + B_i$, because the case $A_i = B_i = 1$ is already covered by $G_i$; but the sum bit needs the **exclusive or** form.)

**Theorem 5.2.1 (Carry Lookahead)** Expanding the recurrence, the carry of every bit can be expressed directly by $G$, $P$ and $C_0$:

$$
\begin{aligned}
C_1 &= G_0 + P_0C_0,\\
C_2 &= G_1 + P_1G_0 + P_1P_0C_0,\\
C_3 &= G_2 + P_2G_1 + P_2P_1G_0 + P_2P_1P_0C_0,\\
C_4 &= G_3 + P_3G_2 + P_3P_2G_1 + P_3P_2P_1G_0 + P_3P_2P_1P_0C_0 .
\end{aligned}
$$
In general $C_{i+1} = \sum_{j=-1}^{i} \bigl(\prod_{k=j+1}^{i} P_k\bigr) G_j$, with the convention $G_{-1} = C_0$.

**Proof** Use induction on $i$: substitute the expansion of $C_i$ into $C_{i+1} = G_i + P_iC_i$ and multiply $P_i$ in. Intuitively, $C_{i+1} = 1$ if and only if some bit $j \le i$ generates a carry and all the bits above $j$ up to $i$ propagate it. $\square$

**Definition 5.2.1 (Carry-Lookahead Adder)** An adder in which dedicated carry logic computes the carries of all bits simultaneously according to Theorem 5.2.1, instead of propagating the carry bit by bit, is called a **carry-lookahead adder** (CLA), also called a parallel-carry adder.

According to these formulas, each carry is a two-level sum of products, and the carries of all bits are obtained at the same time: $G$ and $P$ take $1$ level, the carries $2$ levels, and the XOR for the sum bit another $1$ level, so a $4$-bit addition takes $4$ levels, independent of the number of bits. The cost is the fan-in and number of gates: $C_{i+1}$ has $i+2$ product terms, the longest of which has $i+2$ inputs, and $P_i$ must drive more and more gates. A gate with too large a fan-in is slow and large ([§3.3.1](/4.9.3#sec-3.3.1)), so one level of lookahead goes only up to about $4$ bits.

### 5.2.2. Grouping and Multilevel Lookahead

Take $4$ bits as a group and define generate and propagate functions for the group as well:

$$
G^{*} = G_3 + P_3G_2 + P_3P_2G_1 + P_3P_2P_1G_0,\qquad P^{*} = P_3P_2P_1P_0,
$$
so that the carry output of this group is $C_4 = G^{*} + P^{*}C_0$, of exactly the same form as for one bit. There are then two ways to organize a $16$-bit adder:

- Parallel within groups, serial between groups: four $4$-bit carry-lookahead adders are connected in series, with the carry propagating group by group. The delay grows linearly with the number of groups, but is about $4$ times faster than bit-by-bit ripple.
- Two-level lookahead: each group outputs $G^{*}_m$ and $P^{*}_m$ ($m = 0, 1, 2, 3$), and a lookahead unit computes $C_4, C_8, C_{12}$ (and $C_{16}$) simultaneously by the same set of formulas as Theorem 5.2.1, and feeds them back to the groups as their internal carry inputs. The integrated chip 74182 is such a lookahead unit, and together with the 4-bit ALU 74181 it forms a $16$-bit fast arithmetic unit.

In the simple model of $1$ level per gate, the critical path of the two-level lookahead $16$-bit adder is: $G$, $P$ ($1$ level) → group $G^{*}$, $P^{*}$ ($2$ levels) → inter-group carries ($2$ levels) → intra-group carries ($2$ levels) → sum bit ($1$ level), $8$ levels in all. This structure can be continued recursively: each additional layer multiplies the number of bits handled by $4$ and adds only a constant number of levels to the delay, so the total delay for $n$ bits is $O(\log n)$.

### 5.2.3. Parallel-Prefix Adders

Multilevel lookahead can be described uniformly in a more general framework. View a contiguous segment of bits $[i, j]$ as a whole, and denote its generate and propagate functions by $(G_{i:j}, P_{i:j})$: the segment either generates a carry by itself or passes on the carry that enters it. When two adjacent segments $[k+1, i]$ (high) and $[j, k]$ (low) are merged,

$$
(G_{i:j},\ P_{i:j}) = (G_{i:k+1},\ P_{i:k+1}) \circ (G_{k:j},\ P_{k:j}),\qquad (g, p) \circ (g', p') = (g + pg',\ pp') .
$$

**Theorem 5.2.2** The operation $\circ$ satisfies the **associative law**. Hence $C_{i+1} = G_{i:0}$ (with $C_0$ absorbed into $G_0$ of bit $0$) is the prefix "product" of the sequence $(G_i, P_i), \dots, (G_0, P_0)$ and can be computed in any order of parenthesization.

**Proof** Direct computation:

$$
\bigl((g_1,p_1)\circ(g_2,p_2)\bigr)\circ(g_3,p_3) = (g_1 + p_1g_2 + p_1p_2g_3,\ p_1p_2p_3) = (g_1,p_1)\circ\bigl((g_2,p_2)\circ(g_3,p_3)\bigr). \qquad\square
$$

Finding all the carries is thus a parallel prefix (scan) problem, and the data structures and the prefix-sum techniques of parallel algorithms can all be used: merging serially from the low bit one at a time gives the ripple-carry adder, and merging with a balanced tree gives the $O(\log n)$-level *parallel-prefix adder*. Two common structures are:

| Structure | Levels | Merge cells | Features |
|---|---|---|---|
| Kogge–Stone | $\log_2 n$ | About $n\log_2 n$ | Fastest, with a **fan-out** of $2$ for each cell, but many wires and a large area |
| Brent–Kung | $2\log_2 n - 1$ | About $2n$ | Small area and regular wiring, with about twice as many levels |

Other compromise structures (Sklansky, Han–Carlson, and so on) lie between the two. There are also the carry-select adder (the high half is computed twice, once assuming a carry of $0$ and once of $1$, and a **multiplexer** selects one when the carry from the low half arrives) and the carry-skip adder, which trade area for speed. Modern synthesis tools choose automatically among these structures according to the timing constraints: a ripple-carry structure when timing is relaxed, and a parallel-prefix structure when timing is tight.

The program below simulates the ripple-carry and Kogge–Stone adders at the bit level, verifies all inputs exhaustively for $8$ bits, and counts the number of levels at which the carry output arrives under the model of $2$ levels per AND-OR cell and $1$ level for $G$/$P$:

```python
def bits(x, n):
    return [(x >> i) & 1 for i in range(n)]


def ripple_add(a, b, n, c0=0):
    """Ripple-carry adder; returns (sum, carry out, depth of the carry out)."""
    A, B = bits(a, n), bits(b, n)
    c, dc, s = c0, 0, 0
    for i in range(n):
        g, p = A[i] & B[i], A[i] ^ B[i]     # level 1
        s |= (p ^ c) << i
        c = g | (p & c)                     # AND-OR: two more levels
        dc = max(dc, 1) + 2
    return s, c, dc


def prefix_add(a, b, n, c0=0):
    """Kogge-Stone parallel-prefix adder with the (g, p) operator."""
    A, B = bits(a, n), bits(b, n)
    g = [A[i] & B[i] for i in range(n)]
    p = [A[i] ^ B[i] for i in range(n)]
    g[0] |= p[0] & c0                   # fold the carry-in into bit 0
    G, P, d, depth = g[:], p[:], 1, 1
    while d < n:                        # log2(n) stages
        G = [G[i] | (P[i] & G[i - d]) if i >= d else G[i] for i in range(n)]
        P = [P[i] & P[i - d] if i >= d else P[i] for i in range(n)]
        d, depth = 2 * d, depth + 2
    carries = [c0] + G[:-1]             # carry into bit i is G[i-1]
    s = sum((p[i] ^ carries[i]) << i for i in range(n))
    return s, G[n - 1], depth


n = 8
for a in range(2 ** n):
    for b in range(2 ** n):
        for c0 in (0, 1):
            t = a + b + c0
            assert ripple_add(a, b, n, c0)[:2] == (t % 2 ** n, t >> n)
            assert prefix_add(a, b, n, c0)[:2] == (t % 2 ** n, t >> n)
print("all", 2 * 4 ** n, "cases correct")
for n in (4, 8, 16, 32, 64):
    print(n, ripple_add(0, 0, n)[2], prefix_add(0, 0, n)[2])
```

```text
all 131072 cases correct
4 9 5
8 17 7
16 33 9
32 65 11
64 129 13
```

![Number of gate levels on the critical path of an n-bit adder under the simple model: ripple carry grows linearly, grouped lookahead grows piecewise, and parallel prefix grows logarithmically](./plots/adder-delay.py)

## 5.3. Subtraction and Two's Complement Arithmetic

### 5.3.1. Two's Complement Addition and Subtraction

An $n$-bit **two's complement** number represents the integers from $-2^{n-1}$ to $2^{n-1}-1$, and the two's complement of $-B$ is $B$ with every bit inverted plus $1$ ([Number Representation in Computers](/3.5.1)). Therefore

$$
A - B = A + \overline{B} + 1 ,
$$
and subtraction needs only a row of XOR gates in front of the $B$ input of the adder together with use of the carry input: with a control signal $\mathit{sub}$, the second operand of the adder is $B_i \oplus \mathit{sub}$ and the carry input is $C_0 = \mathit{sub}$. When $\mathit{sub} = 0$ the adder computes $A + B$, and when $\mathit{sub} = 1$ it computes $A + \overline{B} + 1 = A - B$. The same adder and the same bits can be interpreted either as unsigned numbers or as two's complement numbers, which is the advantage of two's complement; the difference lies only in how **overflow** is detected and magnitudes are compared.

### 5.3.2. Detecting Overflow

**Theorem 5.3.1 (Overflow in Two's Complement Addition)** Let $n$-bit two's complement numbers $A$ and $B$ be added by an adder (possibly with a carry input), let $C_{n-1}$ and $C_n$ be the carries into and out of the most significant bit, and let $S$ be the result interpreted as a two's complement number. Then the exact sum is $A + B + C_0 = S + (C_{n-1} - C_n)\,2^n$, so the result **overflows** if and only if

$$
V = C_n \oplus C_{n-1} = 1 ,
$$
or equivalently, if and only if the two addends have the same sign and the sign of the result differs from theirs: $V = A_{n-1}B_{n-1}\overline{S_{n-1}} + \overline{A_{n-1}}\,\overline{B_{n-1}}S_{n-1}$.

**Proof** Write $A = -A_{n-1}2^{n-1} + A'$ and $B = -B_{n-1}2^{n-1} + B'$, where $A'$ and $B'$ are the unsigned values of the low $n-1$ bits. Adding the low $n-1$ bits gives $A' + B' + C_0 = C_{n-1}2^{n-1} + S'$, and the full adder of the most significant bit gives $A_{n-1} + B_{n-1} + C_{n-1} = 2C_n + S_{n-1}$. Then

$$
A + B + C_0 = -(2C_n + S_{n-1} - C_{n-1})\,2^{n-1} + C_{n-1}2^{n-1} + S' = \bigl(-S_{n-1}2^{n-1} + S'\bigr) + (C_{n-1} - C_n)\,2^n ,
$$
where the expression in parentheses is exactly the two's complement value of $S$. The exact sum can be represented in $n$ bits if and only if it equals $S$, that is, $C_{n-1} = C_n$. If the two addends have different signs, the exact sum is necessarily in range and there is no overflow; if the signs are the same and the sign of the result differs, the result is clearly wrong. Checking the eight input combinations of the most significant bit one by one shows that the two criteria are equivalent. $\square$

**Example 5.3.1** In $4$-bit two's complement, $0111 + 0001 = 1000$, that is, $7 + 1$ gives $-8$. The carry into the most significant bit is $C_3 = 1$ and the carry out is $C_4 = 0$, so $V = 1$ and the sum overflows. For $1111 + 1111 = 1\,1110$, that is, $(-1) + (-1) = -2$, we have $C_3 = C_4 = 1$ and $V = 0$, and the result is correct after discarding $C_4$.

For unsigned numbers, overflow is determined by the carry output: in addition, $C_n = 1$ means that the result exceeds $2^n - 1$; in subtraction, $A - B = A + (2^n - 1 - B) + 1 = (A - B) + 2^n$, so $C_n = 1$ if and only if $A \ge B$, and $C_n = 0$ means that there is not enough to subtract (a borrow).

### 5.3.3. Comparison

Comparing two numbers is usually implemented by subtraction: compute $A - B$ and set flag bits according to the result:

| Flag | Meaning | How to obtain |
|---|---|---|
| $Z$ (zero) | The result is $0$ | **NOR** of the bits of the result |
| $N$ (negative) | The most significant bit of the result | $S_{n-1}$ |
| $C$ (carry) | The carry out of the most significant bit | $C_n$ |
| $V$ (overflow) | Two's complement overflow | $C_n \oplus C_{n-1}$ |

**Theorem 5.3.2 (Comparison by Subtraction)** Suppose $A - B$ is computed as $A + \overline{B} + 1$. For unsigned numbers, $A < B$ if and only if $C = 0$; for two's complement numbers, $A < B$ if and only if $N \oplus V = 1$; under both interpretations, $A = B$ if and only if $Z = 1$.

**Proof** The unsigned case is shown in the previous subsection. For the two's complement case, by Theorem 5.3.1 the exact difference is $A - B = S + (C_{n-1} - C_n)2^n$. Without overflow $A - B = S$, and its sign is $N$. With overflow, $\lvert A - B\rvert \le 2^n - 1$ while $S \in [-2^{n-1}, 2^{n-1} - 1]$, and the two differ by $\pm 2^n$, so $A - B$ and $S$ have opposite signs and $A - B \ne 0$. Together, $A - B < 0$ if and only if $N \oplus V = 1$. $\square$

x86 and ARM processors keep these four flags in a flag register for use by subsequent conditional jumps; RISC-V has no flag register, but uses the `slt` and `sltu` instructions to write the comparison result (that is, $N \oplus V$ or $\overline{C}$) directly into a general-purpose register, and conditional branch instructions perform the comparison themselves ([Computer Organization](/4.10)).

## 5.4. The Arithmetic Logic Unit

### 5.4.1. Structure

**Definition 5.4.1 (Arithmetic Logic Unit)** A combinational circuit that, under the selection of control signals, can perform various arithmetic operations (addition, subtraction, etc.) and logic operations (AND, OR, XOR, etc.) on two operands is called an **arithmetic logic unit** (ALU).

The typical structure of an ALU in a modern processor is "compute in parallel, select at the end": functional units such as the adder-subtractor, AND, OR, XOR, shifter and comparison operate on $A$ and $B$ simultaneously, and a multiplexer driven by the ALU control code selects the desired result; status outputs such as whether the result is zero are produced as well.

![The structure of a simple 32-bit ALU: the functional units compute in parallel, and a multiplexer driven by the ALU control code selects the result; subtraction reuses the adder by inverting B and setting the carry input to 1, and the signed less-than comparison takes the XOR of N and V](./plots/alu-structure.py)

A shifter is also a combinational circuit: a *barrel shifter* uses one level of 2-to-1 multiplexers for each bit of the shift amount (shifting by $1, 2, 4, 8, 16$ bits or not at all), so $32$-bit data can be shifted by any amount through $5$ levels of multiplexers. Below is an ALU implementing the RV32I integer operations:

```systemverilog
typedef enum logic [3:0] {
    OP_ADD, OP_SUB, OP_AND, OP_OR, OP_XOR,
    OP_SLT, OP_SLTU, OP_SLL, OP_SRL, OP_SRA
} alu_op_t;

module alu (
    input  alu_op_t     op,
    input  logic [31:0] a, b,
    output logic [31:0] y,
    output logic        zero
);
    logic        sub, cout, n, v;
    logic [31:0] bb, sum;

    assign sub = (op == OP_SUB) || (op == OP_SLT) || (op == OP_SLTU);
    assign bb  = sub ? ~b : b;                       // A - B = A + ~B + 1
    assign {cout, sum} = {1'b0, a} + {1'b0, bb} + 33'(sub);
    assign n = sum[31];
    assign v = (a[31] == bb[31]) && (sum[31] != a[31]);   // signed overflow

    always_comb
        case (op)
            OP_ADD, OP_SUB: y = sum;
            OP_AND:  y = a & b;
            OP_OR:   y = a | b;
            OP_XOR:  y = a ^ b;
            OP_SLT:  y = {31'b0, n ^ v};             // signed a < b
            OP_SLTU: y = {31'b0, ~cout};             // unsigned a < b: borrow
            OP_SLL:  y = a << b[4:0];
            OP_SRL:  y = a >> b[4:0];
            OP_SRA:  y = $signed(a) >>> b[4:0];
            default: y = '0;
        endcase

    assign zero = (y == '0);
endmodule
```

The `+` in the code does not specify the structure of the adder: the synthesis tool chooses a ripple-carry or parallel-prefix structure according to the timing requirements ([§5.2.3](#sec-5.2.3)).

### 5.4.2. The 74181: A 4-Bit ALU of Historical Interest

Before single-chip processors appeared, the arithmetic units of minicomputers were assembled from medium-scale chips, the most famous of which was the 4-bit ALU 74181 introduced in 1970. Its design idea differs from the "compute in parallel, select at the end" above: it has no separate logic-operation units but uses four function-select inputs $S_3S_2S_1S_0$ to control the $G_i$ and $P_i$ generated at each bit (each a function of $A_i$ and $B_i$), which then pass through the internal lookahead logic; when the mode input $M = 1$ the carries between bits are blocked and each bit independently outputs a logic function, and when $M = 0$ the carries between bits take effect and arithmetic operations are performed. One chip thus provides $16$ logic operations and $16$ arithmetic operations, for example (positive-logic data):

| $S_3S_2S_1S_0$ | $M = 1$ (logic) | $M = 0$ (arithmetic) |
|---|---|---|
| 0000 | $\overline{A}$ | $A$ (plus carry input) |
| 0110 | $A \oplus B$ | $A$ minus $B$ minus $1$ (gives $A - B$ when the carry input is $1$) |
| 1001 | $\overline{A \oplus B}$ | $A$ plus $B$ |
| 1011 | $AB$ | |
| 1110 | $A + B$ | |
| 1111 | $A$ | $A$ minus $1$ |

The 74181 also outputs group generate and group propagate signals, and together with the lookahead unit 74182 it forms $16$-bit and $32$-bit fast arithmetic units. Today it has only historical significance: the ALU is now a part of the processor, written in a hardware description language and implemented by a synthesis tool. But the idea of "changing $G_i$ and $P_i$ by control signals so as to reuse one set of carry logic", and the hierarchy of group generate and propagate signals, remain good examples for understanding fast adders.

## 5.5. A Brief Look at Multipliers

Binary multiplication is the same as decimal long multiplication: each bit $B_j$ of $B$ is ANDed with $A$ to give the partial product $A \cdot B_j$, which is shifted left by $j$ bits and then added. An $n \times n$-bit array multiplier uses $n^2$ AND gates to produce all the partial products and then about $n^2$ full adders arranged in an array to add them, with delay $O(n)$; using carry-save adders to compress the partial products layer by layer in a tree (a Wallace tree or a Dadda tree) and finally adding with a fast adder reduces the delay to $O(\log n)$. Two's complement multiplication usually uses Booth encoding to reduce the number of partial products. The organization of multipliers and dividers in processors is covered in [Computer Organization](/4.10).

The area of a multiplier is roughly proportional to the square of the number of bits, which has direct practical significance: deep learning inference makes heavy use of $8$-bit and $4$-bit integers or low-precision **floating-point numbers** (such as FP8), and the area and energy of a $4 \times 4$-bit multiplier are only about $1/64$ of those of a $32 \times 32$-bit multiplier, so many more multiplier units fit into the same chip area.

## Summary

| Topic | Key points |
|---|---|
| Full adder | $S = A \oplus B \oplus C_{\mathrm{in}}$ (parity), $C_{\mathrm{out}} = AB + (A\oplus B)C_{\mathrm{in}}$ (majority); two half adders plus an OR gate |
| Ripple carry | $n$ full adders in series; delay $O(n)$ |
| Carry lookahead | $G_i = A_iB_i$, $P_i = A_i \oplus B_i$; $C_{i+1} = G_i + P_iC_i$ expands to a two-level sum of products; group $G^*$, $P^*$ and recursive levels give $O(\log n)$ |
| Parallel prefix | $(g,p)\circ(g',p') = (g + pg', pp')$ is associative; Kogge–Stone is fastest, Brent–Kung is most economical |
| Subtraction | $A - B = A + \overline{B} + 1$: XOR gates plus the carry input |
| Overflow | Two's complement $V = C_n \oplus C_{n-1}$; for unsigned addition look at $C_n$, and for subtraction $C_n = 0$ means a borrow |
| Comparison | Unsigned $A < B \iff C = 0$; two's complement $A < B \iff N \oplus V$ |
| ALU | Compute in parallel, select with a multiplexer; the 74181 controls $G$ and $P$ with $S$, and $M$ selects logic or arithmetic |
