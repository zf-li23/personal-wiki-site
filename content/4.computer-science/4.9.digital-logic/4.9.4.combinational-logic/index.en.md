---
title: Combinational Logic Circuits
description: Analysis and design of combinational circuits; decoders (enable inputs, expansion, address decoding, display decoding), multiplexers and implementing arbitrary functions with them, encoders and priority encoders, magnitude comparators, parity checkers; ROM and PLA as arrays implementing combinational functions; the causes, detection and elimination of races and hazards.
source_hash: db4a443d245f
---

A circuit whose output depends only on the present inputs is called a combinational circuit. This chapter first gives the general method of analyzing and designing combinational circuits, which combines the tools of [Logic Algebra and Minimization](/4.9.2) with the implementation constraints of [Logic Gates](/4.9.3); it then discusses, one by one, the medium-scale combinational building blocks that recur in digital systems: decoders, multiplexers, encoders, comparators and **parity check** circuits. These blocks are both stand-alone chips of the 74 series and basic components inside processors; for example, the read ports of a register file are multiplexers, the opcode of an instruction goes through a decoder, and an interrupt controller uses a priority encoder. Next, read-only memories and programmable logic arrays are viewed as regular arrays that implement arbitrary combinational functions; finally we discuss the races and hazards caused by gate delays. Adders and the arithmetic logic unit are the subject of the [next chapter](/4.9.5).

Each block is accompanied by a short SystemVerilog description. Today digital design writes such blocks in a hardware description language at the register-transfer level, and a synthesis tool generates the gates; the language itself is covered in [Programmable Logic and HDL](/4.9.9), and here it suffices to understand that `assign` describes a combinational function and that the statements in an `always_comb` block describe the behavior of combinational logic.

## 4.1. Analysis and Design of Combinational Circuits

### 4.1.1. Combinational Circuits

**Definition 4.1.1 (Combinational Logic Circuit)** A digital circuit whose output at any instant depends only on the inputs at that instant, and not on earlier inputs, is called a **combinational logic circuit** (combinational circuit for short).

A combinational circuit has no storage element and no feedback loop from output to input, so it can be described completely by a set of logic functions $Y_j = F_j(X_1, \dots, X_n)$. In contrast, a circuit whose output also depends on past inputs is a sequential circuit, which contains latches or flip-flops that store state ([Latches and Flip-Flops](/4.9.6)). Because gates have delay, after an input change the output of a combinational circuit takes some time to settle at the function value, and during this time brief erroneous outputs may occur ([§4.8](#sec-4.8)).

### 4.1.2. Analysis

Analysis finds the function from the circuit:

1. Write the output expression of each gate stage by stage from the inputs to the outputs, obtaining the logic expressions of the outputs;
2. Simplify the expressions and list the **truth table**;
3. Summarize the function of the circuit from the truth table.

![A worked analysis example: a circuit of four NAND gates; writing out the output of each gate stage by stage shows that Y is the exclusive or of A and B](./plots/nand-xor.py)

**Example 4.1.1** Analyze the circuit in the figure. Writing stage by stage:

$$
N_1 = \overline{AB},\qquad N_2 = \overline{A N_1},\qquad N_3 = \overline{B N_1},\qquad Y = \overline{N_2 N_3} = A N_1 + B N_1 .
$$
Substituting $N_1$: $Y = (A + B)\,\overline{AB} = (A + B)(\overline{A} + \overline{B}) = A\overline{B} + \overline{A}B = A \oplus B$. The circuit is an **exclusive or** gate built only from **NAND gates**, using $4$ gates and $3$ levels of delay.

### 4.1.3. Design

Design finds the circuit from the function:

1. Analyze the requirements and determine the input and output variables and their coding (what each variable being $1$ means);
2. List the truth table and mark the **don't-care terms**;
3. Minimize: for a two-level implementation, use a **Karnaugh map** or a minimization tool to find the **minimal sum of products** (or product of sums);
4. Transform the expression according to the available devices: with NAND gates only, complementing the minimal sum of products twice gives the **NAND**–NAND form, $AB + CD = \overline{\overline{AB}\cdot\overline{CD}}$; with **NOR gates** only, the **NOR**–NOR form is obtained from the minimal product of sums;
5. Draw the circuit and check whether the fan-in and **fan-out** exceed the capability of the devices (if they do, add buffers or use multiple levels);
6. Verify by simulation or by the truth table.

**Example 4.1.2 (Three-Person Voting Circuit)** Three judges $A, B, C$ vote, and the motion passes ($Y = 1$) when a majority approves (at least two are $1$). The rows of the truth table with $Y = 1$ are $011, 101, 110, 111$, that is, $Y = \sum m(3, 5, 6, 7)$. Karnaugh-map minimization gives

$$
Y = AB + BC + AC = \overline{\overline{AB}\cdot\overline{BC}\cdot\overline{AC}},
$$
implemented with three 2-input NAND gates and one 3-input NAND gate. This function is called the majority function, and it is also the carry output of a full adder ([Arithmetic Circuits](/4.9.5)).

```systemverilog
module majority3 (
    input  logic a, b, c,
    output logic y
);
    assign y = (a & b) | (b & c) | (a & c);
endmodule
```

In today's design flow, steps 3 and 4 are done by the synthesis tool: the designer writes a truth table or an expression, and the tool chooses the implementation according to the cell library of the target technology (or the lookup tables of an FPGA). The manual methods of analysis and design remain the basis for understanding synthesis results and for estimating circuit size and delay.

## 4.2. Decoders

### 4.2.1. Variable Decoders

**Definition 4.2.1 (Decoder)** A combinational circuit with $n$ inputs and $2^n$ outputs that makes exactly one corresponding output active for each combination of inputs is called an $n$-to-$2^n$ line **decoder**. The $i$-th output is the minterm $m_i$ of the input variables. More broadly, a circuit that converts one code into another is also called a decoder (code converter, display decoder, [§4.2.3](#sec-4.2.3)).

Take the 2-to-4 decoder as an example, with inputs $A_1A_0$ ($A_1$ the high bit) and an enable input $\mathit{EN}$:

| $\mathit{EN}$ | $A_1$ | $A_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
|---|---|---|---|---|---|---|
| 0 | × | × | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 1 |

$$
Y_0 = \mathit{EN}\,\overline{A_1}\,\overline{A_0},\quad Y_1 = \mathit{EN}\,\overline{A_1}A_0,\quad Y_2 = \mathit{EN}\,A_1\overline{A_0},\quad Y_3 = \mathit{EN}\,A_1A_0 .
$$

The outputs of actual chips are mostly active low and are implemented with NAND gates: $\overline{Y_i} = \overline{\mathit{EN}\cdot m_i}$. The load must also be considered in design: each input variable directly drives $2^{n-1}$ gates and one inverter, so integrated decoders add a buffer stage at the inputs (one buffer each for the true and complemented variable), so that each input presents only one load to the outside.

The enable input has two uses:

- Expansion: using the high-order address bits to control the enable inputs of the individual chips, several small decoders form a large one. For example, two 3-to-8 decoders form a 4-to-16 decoder: the most significant bit $A_3$ is connected to the active-low enable input of the first chip and to the active-high enable input of the second, so that when $A_3 = 0$ the first chip decodes $0$–$7$, and when $A_3 = 1$ the second chip decodes $8$–$15$.
- Strobing: setting $\mathit{EN} = 0$ while the inputs are changing masks the glitches on the decoder outputs ([§4.8.3](#sec-4.8.3)).

Commonly used integrated decoders are the dual 2-to-4 decoder 74HC139, the 3-to-8 decoder 74HC138 (one active-high and two active-low enable inputs $G_1, \overline{G_{2A}}, \overline{G_{2B}}$, with active-low outputs) and the 4-to-16 decoder 74HC154.

```systemverilog
module decoder3to8 (
    input  logic       en,
    input  logic [2:0] a,
    output logic [7:0] y
);
    always_comb begin
        y = 8'b0;
        if (en) y[a] = 1'b1;    // one-hot output
    end
endmodule
```

### 4.2.2. Address Decoding

The most important use of decoders in computers is address decoding: the processor presents an address, and the decoder selects the memory chip or peripheral that holds that address.

**Example 4.2.1** A processor has an $8$-bit address $A_7\cdots A_0$ ($256$ addresses) and is to be connected to $8$ ROM chips of $32$ bytes each. Inside each chip the low $5$ bits $A_4\cdots A_0$ select the byte; the high $3$ bits $A_7A_6A_5$ are connected to the inputs of a 74HC138, whose eight outputs are connected to the active-low chip-select inputs $\overline{\mathit{CS}}$ of the ROM chips. Chip $k$ then occupies the addresses $32k$ to $32k + 31$:

| $A_7A_6A_5$ | Selected | Address range |
|---|---|---|
| 000 | Chip 0 | `0x00`–`0x1F` |
| 001 | Chip 1 | `0x20`–`0x3F` |
| … | … | … |
| 111 | Chip 7 | `0xE0`–`0xFF` |

Peripheral registers can be assigned addresses in the same way, which is called memory-mapped I/O; modern processors such as RISC-V access peripherals this way ([Computer Organization](/4.10)).

As the number $n$ of decoder inputs grows, in single-stage decoding each AND gate needs $n$ inputs and each input variable must drive $2^{n-1}$ gates, which soon becomes infeasible. Large memories use multi-stage decoding internally: the address is first split into two parts, each decoded by a small decoder (for example, $8$ bits split into two $4$-bit parts giving $16$ outputs each), and then $16 \times 16$ 2-input AND gates combine them pairwise to give $256$ outputs; in the memory array these two parts become the row address and the column address.

### 4.2.3. Display Decoders

A seven-segment display forms digits from seven light-emitting segments a–g. The segments of a common-cathode display light up when the input is high, while those of a common-anode display light up when the input is low. A BCD-to-seven-segment display decoder converts one digit of 8421 **BCD** code $ABCD$ ($A$ the high bit) into the control signals of the seven segments. For a common-cathode display (lit when high):

| Digit | $ABCD$ | a | b | c | d | e | f | g |
|---|---|---|---|---|---|---|---|---|
| 0 | 0000 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0001 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 0010 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3 | 0011 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 4 | 0100 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 5 | 0101 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| 6 | 0110 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 7 | 0111 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 8 | 1000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | 1001 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |

$1010$–$1111$ are not BCD codes and are treated as don't-care terms. Minimizing each segment with a Karnaugh map (the results were verified with the [Q-M program](/4.9.2#sec-2.6.3)) gives, for example,

$$
a = A + C + BD + \overline{B}\,\overline{D},\qquad b = \overline{B} + \overline{C}\,\overline{D} + CD,\qquad c = B + \overline{C} + D,\qquad e = \overline{B}\,\overline{D} + C\overline{D} .
$$
Integrated display decoders (such as the 74HC4511) also provide lamp test, blanking and latching. A circuit minimized using don't-care terms displays a meaningless pattern when given an invalid code; if all segments are required to be off for invalid inputs, the outputs for these inputs must be specified as $0$, which is called full decoding, and the circuit becomes more complex.

### 4.2.4. Implementing Logic Functions with Decoders

The outputs of a decoder are all the **minterms**, so adding an OR gate implements any **canonical sum of products**. With an active-low decoder, use a NAND gate: $F = \sum m_i = \overline{\prod \overline{m_i}}$; it suffices to connect the $\overline{Y_i}$ contained in $F$ to a NAND gate. For example, the voting circuit of Example 4.1.2 can be implemented with a 74HC138 as $Y = \overline{\overline{Y_3}\,\overline{Y_5}\,\overline{Y_6}\,\overline{Y_7}}$. One decoder can supply minterms for several functions at once, which suits multiple-output functions.

Taking the enable input of a decoder as a data input $D$ and the select inputs as the address, $D$ appears only at the selected output while the other outputs remain inactive: this is a demultiplexer, which distributes one line of data to several outputs according to the address, the inverse of a multiplexer.

## 4.3. Multiplexers

### 4.3.1. Multiplexers

**Definition 4.3.1 (Multiplexer)** A combinational circuit with $2^n$ data inputs, $n$ select inputs and one output, whose output equals the data input designated by the binary value of the select inputs, is called a $2^n$-to-$1$ **multiplexer** (MUX).

The output of a 4-to-1 multiplexer is

$$
Y = \overline{S_1}\,\overline{S_0}\,D_0 + \overline{S_1}S_0D_1 + S_1\overline{S_0}\,D_2 + S_1S_0D_3 = \sum_{i=0}^{3} m_i D_i ,
$$
where $m_i$ are the minterms of the select inputs. Its structure is a 2-to-4 decoder followed by AND-OR gates: the decoder selects one line, the AND gate lets this line pass, and the OR gate collects the results. Data of width $k$ (such as a $32$-bit register) uses $k$ identical multiplexers in parallel sharing the select signals.

```systemverilog
module mux4 #(parameter int W = 32) (
    input  logic [1:0]   s,
    input  logic [W-1:0] d0, d1, d2, d3,
    output logic [W-1:0] y
);
    always_comb
        case (s)
            2'd0: y = d0;
            2'd1: y = d1;
            2'd2: y = d2;
            default: y = d3;
        endcase
endmodule
```

There are two ways of expansion: tree expansion, for example five 4-to-1 multiplexers forming a 16-to-1 multiplexer, with the four multiplexers of the first level controlled by $S_1S_0$ and the one of the second level controlled by $S_3S_2$; or multiplexers with enable inputs (and **tri-state gate** outputs), where the high-order select signals are decoded to control the enables of the chips and the outputs are connected in parallel. Multiplexers are everywhere in processors: the read ports of the register file, the selection of ALU inputs, the selection of write-back data and the selection of the next instruction address are all multiplexers ([Computer Organization](/4.10)).

### 4.3.2. Implementing Logic Functions with Multiplexers

By definition, the output $\sum m_iD_i$ of a $2^n$-to-$1$ multiplexer is exactly the general form of the **canonical sum of products** of an $n$-variable function: connecting the $n$ variables to the select inputs and the $i$-th data input to the constant $F(i)$ implements an arbitrary $n$-variable function $F$. A more economical approach uses [Shannon expansion](/4.9.2#thm-2.2.4): an $n$-variable function is implemented with a $2^{n-1}$-to-$1$ multiplexer, the first $n-1$ variables are connected to the select inputs, and the remaining variable appears at the data inputs, where each data input is a function of this one variable and can only be $0$, $1$, the variable itself, or its complement.

**Example 4.3.1** Implement $F(A, B, C, D) = \sum m(3, 4, 5, 7, 9, 13, 14, 15)$ with an 8-to-1 multiplexer. Let $S_2S_1S_0 = ABC$ and, for each $ABC$, look at the values of $F$ when $D = 0$ and when $D = 1$ (that is, the minterms $m_{2i}$ and $m_{2i+1}$):

| $ABC$ | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| Minterms | $m_0, m_1$ | $m_2, m_3$ | $m_4, m_5$ | $m_6, m_7$ | $m_8, m_9$ | $m_{10}, m_{11}$ | $m_{12}, m_{13}$ | $m_{14}, m_{15}$ |
| $D_i$ | $0$ | $D$ | $1$ | $D$ | $D$ | $0$ | $D$ | $1$ |

This method needs no minimization, and when the function changes only the connections of the data inputs need to change. This is exactly the idea behind the lookup table (LUT), the basic logic element of an FPGA: a $k$-input lookup table is a $2^k$-to-$1$ multiplexer whose data inputs are connected to $2^k$ programmable memory bits, and storing the truth table implements an arbitrary $k$-variable function ([Programmable Logic and HDL](/4.9.9)).

## 4.4. Encoders

### 4.4.1. Encoders

**Definition 4.4.1 (Encoder)** A combinational circuit with $2^n$ inputs and $n$ outputs that outputs the binary code of the index of the input when exactly one input is active is called a $2^n$-to-$n$ line **encoder**. It is the inverse of a decoder.

The outputs of a 4-to-2 encoder (inputs $I_0$–$I_3$ active high) are $Y_1 = I_2 + I_3$ and $Y_0 = I_1 + I_3$. Such an encoder requires one-hot inputs: only one input is active at any time. If $I_1$ and $I_2$ are active simultaneously, the output $11$ would be mistaken for $I_3$; if no input is active, the output $00$ cannot be distinguished from $I_0$. In practice several inputs are often active at the same time (several keys pressed together, several devices requesting an interrupt), hence the need for a priority encoder.

### 4.4.2. Priority Encoders

**Definition 4.4.2 (Priority Encoder)** An encoder for which the priorities of the inputs are fixed in advance, which encodes only the input of highest priority when several inputs are active at the same time, and which has an extra output $V$ indicating whether any input is active, is called a **priority encoder**.

The function table of an 8-to-3 priority encoder (inputs active high, larger index has priority):

| $I_7$ | $I_6$ | $I_5$ | $I_4$ | $I_3$ | $I_2$ | $I_1$ | $I_0$ | $Y_2Y_1Y_0$ | $V$ |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 000 | 0 |
| 1 | × | × | × | × | × | × | × | 111 | 1 |
| 0 | 1 | × | × | × | × | × | × | 110 | 1 |
| 0 | 0 | 1 | × | × | × | × | × | 101 | 1 |
| 0 | 0 | 0 | 1 | × | × | × | × | 100 | 1 |
| 0 | 0 | 0 | 0 | 1 | × | × | × | 011 | 1 |
| 0 | 0 | 0 | 0 | 0 | 1 | × | × | 010 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | × | 001 | 1 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 000 | 1 |

Minimizing from the function table (the "×" entries are exactly the role of don't-care terms) gives

$$
\begin{aligned}
Y_2 &= I_7 + I_6 + I_5 + I_4,\\
Y_1 &= I_7 + I_6 + \overline{I_5}\,\overline{I_4}\,I_3 + \overline{I_5}\,\overline{I_4}\,I_2,\\
Y_0 &= I_7 + \overline{I_6}I_5 + \overline{I_6}\,\overline{I_4}\,I_3 + \overline{I_6}\,\overline{I_4}\,\overline{I_2}\,I_1,\\
V &= I_7 + I_6 + \cdots + I_0 .
\end{aligned}
$$

The inputs and outputs of the integrated priority encoder 74HC148 are all active low; in addition it has an enable input $\overline{\mathit{EI}}$, an enable output $\overline{\mathit{EO}}$ (which is $0$ when this chip is enabled and no input is active, and is used to enable the next chip of lower priority) and an output-valid flag $\overline{\mathit{GS}}$. Two chips cascade into a 16-to-4 priority encoder: the $\overline{\mathit{EO}}$ of the high-order chip is connected to the $\overline{\mathit{EI}}$ of the low-order chip, so that the low-order chip is disabled whenever the high-order chip has an active input; the $\overline{\mathit{GS}}$ of the high-order chip serves directly as the most significant output bit (also active low), and the low three output bits of the two chips are ANDed correspondingly (which for active-low signals amounts to an OR) to give the low three bits.

Priority encoders are used in interrupt controllers (selecting the highest-priority device when several request at once), in bus arbitration, and in finding the position of the highest $1$ of a binary number (leading-zero count), which is needed both in the normalization of **floating-point numbers** and in integer division. In a hardware description language, the priority relation is expressed naturally by a loop that scans from low to high:

```systemverilog
module prio_enc8 (
    input  logic [7:0] i,
    output logic [2:0] y,
    output logic       v
);
    always_comb begin
        y = 3'd0;
        for (int k = 0; k < 8; k++)
            if (i[k]) y = 3'(k);      // a later (higher) k overrides
        v = |i;
    end
endmodule
```

## 4.5. Magnitude Comparators

**Definition 4.5.1 (Magnitude Comparator)** A combinational circuit that compares the magnitudes of two binary numbers $A$ and $B$ and produces the three results $A > B$, $A = B$ and $A < B$ is called a **magnitude comparator**.

One-bit comparison: $G_i = A_i\overline{B_i}$ ($A_i > B_i$), $L_i = \overline{A_i}B_i$ ($A_i < B_i$), $E_i = \overline{A_i \oplus B_i}$ (equal). Multi-bit numbers are compared starting from the most significant bit, and a lower bit matters only when the higher bits are equal. For the $4$-bit numbers $A_3A_2A_1A_0$ and $B_3B_2B_1B_0$:

$$
\begin{aligned}
(A = B) &= E_3E_2E_1E_0,\\
(A > B) &= G_3 + E_3G_2 + E_3E_2G_1 + E_3E_2E_1G_0,\\
(A < B) &= \overline{(A > B) + (A = B)} .
\end{aligned}
$$

The integrated comparator 74HC85 also has three cascade inputs $(A > B)_{\mathrm{in}}$, $(A = B)_{\mathrm{in}}$, $(A < B)_{\mathrm{in}}$, which represent the comparison result of the lower bits and take effect only when all $4$ bits of this chip are equal. To compare $8$-bit numbers, the three outputs of the low $4$-bit chip are connected to the cascade inputs of the high $4$-bit chip, and the cascade inputs of the low chip are fixed to "equal". The delay of this serial cascade grows linearly with the number of bits; for many bits, the segments can be compared in parallel first and then merged in a way similar to carry lookahead.

Comparison can also be done by subtraction: compute $A - B$ and examine the sign and whether the result is zero; for signed numbers **overflow** must also be considered ([Arithmetic Circuits](/4.9.5)). This is how comparison instructions and conditional branches in processors are implemented. To test only for equality, it suffices to XOR bit by bit and then NOR the results, which is the simplest and most common form of a comparator (such as address matching and cache tag comparison).

## 4.6. Parity Checkers

The check bit $P = d_0 \oplus d_1 \oplus \cdots \oplus d_{n-1}$ of a [parity code](/4.9.1#def-1.3.3) is produced by XOR gates. The XOR of $n$ inputs can be arranged as a chain ($n - 1$ levels) or as a balanced tree, which needs only $\lceil \log_2 n \rceil$ levels.

![An 8-bit even-parity generator: seven XOR gates form a balanced tree of three levels; P = 1 when the number of 1s in the data is odd, so that the number of 1s in the 9-bit code is always even](./plots/parity-tree.py)

The same circuit is both a generator and a checker: the transmitter uses it to compute $P$ and sends it along with the data; the receiver feeds the received $8$ data bits and $P$, $9$ bits in all, to a $9$-input XOR tree, where a result of $0$ means that no error is detected and $1$ means that an error in an odd number of bits has occurred. The integrated chip 74HC280 is a 9-bit parity generator/checker that provides both odd and even outputs. In SystemVerilog, the reduction operator `^d` is the XOR of all the bits.

## 4.7. Programmable Logic Arrays

### 4.7.1. ROM as a Combinational Circuit

Any combinational function can be written as a sum of products, so it can be implemented by a regular structure: an AND array produces the product terms and an OR array adds the product terms together. A read-only memory (ROM) is exactly such a structure: the $n$-bit address passes through a complete $n$-to-$2^n$ decoder (a fixed AND array that produces all $2^n$ minterms, the word lines), and each output bit is the OR of some word lines (the OR array, determined by the stored contents). Writing the truth table of a function into a ROM makes it a combinational circuit implementing that function, "computing by storing".

**Example 4.7.1** Compute the square of a $3$-bit binary number $X$ with a ROM. $X^2 \le 49$ requires $6$ output bits, but bit $0$ of $X^2$ equals bit $0$ of $X$ and bit $1$ is always $0$ (a square modulo $4$ can only be $0$ or $1$), so an $8$-word $\times$ $4$-bit ROM suffices to store the remaining $4$ bits.

The drawback of a ROM is that its size grows exponentially with the number of input bits: however many product terms the function needs, the AND array produces all $2^n$ minterms.

### 4.7.2. PLA

**Definition 4.7.1 (Programmable Logic Array)** An array structure in which both the AND array and the OR array are programmable is called a **programmable logic array** (PLA): the AND array produces only the product terms that the function actually needs, and the OR array combines them into the outputs.

To implement functions with a PLA, first find the minimal sum of products of each output, trying to make several outputs share product terms (multiple-output minimization); the total number of product terms determines the size of the AND array.

![Implementing the conversion from 4-bit binary code to Gray code with a PLA: a dot in the AND array denotes a literal contained in a product term, and a dot in the OR array denotes a product term contained in an output](./plots/pla-gray.py)

**Example 4.7.2** Conversion of the 4-bit binary code $B_3B_2B_1B_0$ to **Gray code** ([Theorem 1.3.1](/4.9.1#thm-1.3.1)): $G_3 = B_3$, $G_i = B_{i+1} \oplus B_i$. Written as sums of products, $7$ distinct product terms are needed in all:

$$
\begin{aligned}
&P_1 = B_3,\quad P_2 = B_3\overline{B_2},\quad P_3 = \overline{B_3}B_2,\quad P_4 = B_2\overline{B_1},\quad P_5 = \overline{B_2}B_1,\quad P_6 = B_1\overline{B_0},\quad P_7 = \overline{B_1}B_0,\\
&G_3 = P_1,\quad G_2 = P_2 + P_3,\quad G_1 = P_4 + P_5,\quad G_0 = P_6 + P_7 .
\end{aligned}
$$
The AND array has $8$ columns ($4$ variables and their complements) and $7$ rows, $56$ programmable points in all; the OR array has $4 \times 7 = 28$ points, a total of $84$. Implementing the same function with a $16 \times 4$ ROM takes $8 \times 16 = 128$ points in the AND array and $4 \times 16 = 64$ points in the OR array, a total of $192$.

| Structure | AND array | OR array | Features |
|---|---|---|---|
| ROM | Fixed (full decoding) | Programmable | Stores the truth table directly; size $2^n$ |
| PLA | Programmable | Programmable | Produces only the needed product terms; most flexible |
| PAL | Programmable | Fixed | A fixed number of product terms per output; fast and easy to manufacture |

The regular structure of a PLA was also used for control logic inside processors (instruction decoding). The architectures of programmable devices such as PAL, GAL, CPLD and FPGA are covered in [Programmable Logic and HDL](/4.9.9).

## 4.8. Races and Hazards

### 4.8.1. Causes

So far we have treated combinational circuits as ideal functions. In fact every gate has delay ([Logic Gates and Their Electrical Characteristics](/4.9.3)), and an input change that reaches the same gate along different paths arrives at different times.

**Definition 4.8.1 (Races and Hazards)** The phenomenon of one input change reaching a gate along paths of different delays is called a **race**; the phenomenon in which, because of a race, the output of a combinational circuit shows a brief erroneous value (a glitch) before settling at the correct value is called a **hazard**. If the output should stay unchanged before and after the change (both $1$ or both $0$) but shows a brief opposite value, it is called a static hazard (static-1 hazard, static-0 hazard); if the output should change once but actually changes several times back and forth, it is called a dynamic hazard.

![A static-1 hazard: for F = AB + A'C with B = C = 1, after A falls, AB becomes 0 first and A'C becomes 1 one gate delay later, so the output shows a brief 0; after adding the consensus term BC, the glitch disappears](./plots/static-hazard.py)

**Example 4.8.1** Take $F = AB + \overline{A}C$ with $B = C = 1$, so that $F = A + \overline{A} = 1$ regardless of $A$. But $\overline{A}$ is produced by an inverter and lags $A$ by one gate delay. When $A$ goes from $1$ to $0$, the AND gate $AB$ first outputs $0$, while the AND gate $\overline{A}C$ outputs $1$ only one more gate delay later; during this interval both AND gates output $0$, and $F$ shows a negative pulse about one gate delay wide. Dually, $F = (A + B)(\overline{A} + C)$ with $B = C = 0$ gives $F = A\overline{A} = 0$ and may show a positive pulse, a static-0 hazard.

The above are hazards caused by the change of a single input, called logic hazards; they depend on the specific structure of the circuit and can be eliminated by modifying the circuit. When several inputs change at the same time, even if every gate is ideal, the inputs arrive in different orders and the circuit briefly "passes through" intermediate input combinations; if the outputs for the intermediate combinations differ, a glitch results. This is called a function hazard, which is a property of the function itself and cannot be eliminated by adding redundant terms.

### 4.8.2. Detection

- Algebraic method: in a sum of products, if a variable $X$ appears in both uncomplemented and complemented form, and for some assignment of the other variables the expression becomes $X + \overline{X}$, then there is a static-1 hazard when $X$ changes; in a product of sums, if it becomes $X\overline{X}$, there is a static-0 hazard.
- Karnaugh-map method: on the Karnaugh map of the minimal sum of products, if two circles are adjacent (there are two adjacent $1$s belonging to the two circles respectively) and no other circle covers both of these $1$s, there is a static-1 hazard when the input changes between these two minterms. In Example 4.8.1, the two circles $AB$ and $\overline{A}C$ are adjacent between $ABC = 111$ and $011$.

### 4.8.3. Elimination

1. Add a redundant term: add the **consensus** term between adjacent circles so that the adjacent $1$s are covered by the same circle. In Example 4.8.1, adding $BC$ gives $F = AB + \overline{A}C + BC$; by the [consensus theorem](/4.9.2#thm-2.2.1) the function is unchanged, while with $B = C = 1$ the term $BC$ stays $1$ throughout, so $F$ stays $1$ when $A$ changes. Here the minimal form has been deliberately given up.
2. Strobing: while the inputs are changing and the circuit has not yet settled, block the output with a strobe (enable) signal, and open it again once the circuit is stable. The enable input of a decoder is often used this way: for example, when the inputs of a 2-to-4 decoder change from $11$ to $00$, if the two inputs do not change exactly simultaneously, the decoder briefly passes through $01$ or $10$, glitches appear on $Y_1$ or $Y_2$, and $Y_3$ and $Y_0$ may even be active at the same time; removing the enable before the change and applying it again after all inputs are stable and at least one gate delay has elapsed eliminates these glitches. The strobe pulse should cover the whole process of the input change, but should not be too wide, or the speed is reduced.
3. Filtering: connect a small capacitor in parallel at the output to absorb narrow pulses. It also slows down the edges of the normal signal, and is used only where the speed is very low.
4. Synchronous design: the standard practice in modern digital systems is to let the outputs of combinational circuits be sampled by flip-flops only at clock edges, with a clock period longer than the longest delay of the combinational circuit ([Synchronous Sequential Circuits](/4.9.7)). The glitches have subsided before sampling and cause no error, so in general combinational logic does not need hazard elimination.

Synchronous design also marks where hazards are really dangerous: signals that are sensitive to every transition, namely clocks, asynchronous resets and presets, latch enables, and signals sent to other chips or other clock domains, must not be driven directly by combinational logic that may produce glitches, but should come from the outputs of flip-flops. Glitches also consume extra power (each flip charges and discharges a capacitance), and are to be minimized in low-power design.

## Summary

| Block | Function | Key points |
|---|---|---|
| Analysis and design | Circuit ↔ truth table | Write expressions stage by stage; truth table → minimization → NAND–NAND → check fan-in and fan-out |
| Decoder | $n$-bit code → $2^n$ one-hot outputs | Outputs are minterms; enable inputs for expansion and strobing; address decoding, display decoding |
| Multiplexer | Select $1$ of $2^n$ lines | $Y = \sum m_iD_i$; a $2^{n-1}$-to-$1$ multiplexer implements an $n$-variable function; the principle of the LUT |
| Encoder | One-hot input → index | A plain encoder requires mutually exclusive inputs; a priority encoder encodes only the highest priority and adds a valid flag |
| Comparator | Compare $A$ and $B$ | Compare bit by bit from the high end; cascade inputs; can also use subtraction |
| Parity checker | Produce and check the parity bit | XOR tree, $\lceil\log_2 n\rceil$ levels |
| ROM, PLA | Arrays implementing sums of products | ROM has a fixed fully decoded AND array; both arrays of a PLA are programmable, sharing product terms |
| Races and hazards | Delay causes glitches | Static hazards are eliminated by adding consensus terms; in synchronous design only clocks and asynchronous signals need protection |
