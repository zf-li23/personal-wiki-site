---
title: "Introduction: Number Systems and Codes"
description: Analog and digital signals, the noise immunity of binary logic, and the abstraction levels of digital design; positional number systems and base conversion; BCD codes (8421, 5421, 2421, excess-3) and addition correction; construction, conversion and uses of Gray codes; ASCII; parity codes and code distance.
source_hash: b4ae61a35132
---

Digital logic studies how to carry out computation, control and storage with signals that take only two values and with switching networks built from transistors. It sits at the lowest level of computer hardware: [Computer Organization](/4.10) explains which components a processor is logically made of, while this course explains how those components (adders, decoders, registers, counters, state machines) are implemented with gates and flip-flops, and how they are described in a hardware description language and realized on an FPGA. The mathematical tool of the course is switching algebra, that is, the use of **Boolean algebra** from discrete mathematics in two-valued circuits (Chapter 2); the electrical behavior of gates is the subject of Chapter 3; Chapters 4 and 5 treat combinational and arithmetic circuits, Chapters 6–8 treat sequential circuits, and Chapter 9 treats programmable devices and hardware description languages.

This chapter prepares for the whole course. It first explains why digital systems use two-valued signals, and then collects the number systems and codes commonly used in digital circuits. The representation of numbers in computers (**fixed-point numbers**, **two's complement**, **floating-point numbers**) has already been covered in [Number Representation in Computers](/3.5.1), so here we cover only what digital design uses directly: base conversion, binary codes for decimal numbers, Gray codes and error-detecting codes.

## 1.1. Digital Systems

### 1.1.1. Analog and Digital Signals

Quantities in the physical world (temperature, sound pressure, light intensity) vary continuously in time and take continuous values. A circuit can represent them by proportional voltages, or it can first convert them into a finite number of discrete symbols and then process those.

**Definition 1.1.1 (Analog and Digital Signals)** A signal that varies continuously in both time and value is called an **analog signal**; a signal that is discrete in time (meaningful only at a sequence of instants) and takes only finitely many possible values is called a **digital signal**. A digital signal that takes only two values is called a binary signal, and its two values are written as logic $0$ and logic $1$. A circuit that processes analog signals is an analog circuit, and one that processes digital signals is a digital circuit.

![An analog signal, the sampled and quantized signal, and a noisy binary signal: for the binary signal we only need to decide which region the voltage falls in](./plots/analog-vs-digital.py)

In a circuit, logic $1$ and logic $0$ are not two exact voltages but two voltage ranges. Take $3.3\,\mathrm{V}$ LVCMOS levels as an example: an input voltage of at least $2.0\,\mathrm{V}$ is recognized as $1$, an input of at most $0.8\,\mathrm{V}$ is recognized as $0$, and the region between them is a forbidden zone in which the voltage must not stay for long. Representing $1$ by the high level is called positive logic, and representing $1$ by the low level is called negative logic; we use positive logic throughout. How a gate guarantees that its output falls in these two ranges is the topic of Chapter 3.

### 1.1.2. Why Binary Signals

Almost all the advantages of digital systems come from having to distinguish only two ranges:

- Noise immunity: as long as the noise superimposed on a signal does not push the voltage across the threshold, the receiver obtains exactly the right symbol, whereas every bit of noise on an analog signal becomes part of the signal.
- Regeneration: every gate pushes its output back to near the standard levels, so noise does not accumulate along a circuit. This is why a system made of hundreds of millions of gates in series and in parallel can still be reliable.
- Convenient storage, transmission and processing: binary symbols can be copied without distortion, check bits can be added to detect and correct errors ([§1.3.4](#sec-1.3.4)), and the same set of logic operations can carry out arbitrary computations.
- Simple implementation: a transistor operating in the two states on and off is a switch, and the two states of a switch correspond exactly to a binary signal.

The price is that several bits are needed to represent one quantity, and that quantization introduces error; but the precision can be increased without limit by adding bits. Real systems are mostly mixed: sensors and RF front ends are analog circuits, whose output is converted by an analog-to-digital converter (ADC), processed by digital circuits, and then output through a digital-to-analog converter (DAC). The digital computer is the most typical digital system.

Digital design is organized in abstraction levels, each of which cares only about the interface provided by the level below:

| Level | Basic elements | Concerns | In this course |
|---|---|---|---|
| Device | MOS transistors | On, off, current and capacitance | Chapter 3 |
| Gate | AND, OR, NOT, **NAND gate**, flip-flops | Logic function, delay, fan-out | Chapters 2–6 |
| Register-transfer level (RTL) | Adders, multiplexers, registers, state machines | How data is transferred and transformed between registers | Chapters 4–9 |
| System | Processors, memories, buses | Instruction set and performance | [Computer Organization](/4.10) |

Today almost all digital circuits are described at the register-transfer level in a hardware description language, and a synthesis tool then generates a gate-level netlist automatically; yet understanding the synthesis result, estimating the speed and area of a circuit, and tracking down timing problems still require knowledge at the gate and device levels, which is what this course provides.

## 1.2. Number Systems

### 1.2.1. Positional Number Systems

**Definition 1.2.1 (Positional Number System)** A positional number system with base $R$ (the base-$R$ system) uses $R$ digits $0, 1, \dots, R-1$ and carries when a position reaches $R$. The value of a base-$R$ number with $n$ integer digits and $m$ fractional digits

$$
N = (k_{n-1}k_{n-2}\cdots k_1k_0.k_{-1}\cdots k_{-m})_R
$$
is

$$
N = \sum_{i=-m}^{n-1} k_i R^i, \qquad 0 \le k_i \le R-1,
$$
where $R^i$ is called the **weight** of position $i$.

For example, $(143.75)_{10} = 1\times10^2 + 4\times10^1 + 3\times10^0 + 7\times10^{-1} + 5\times10^{-2}$, and $(101.11)_2 = 4 + 1 + 0.5 + 0.25 = (5.75)_{10}$.

The number systems commonly used in digital circuits:

| System | Base | Digits | Subscript notation | Notation in programs |
|---|---|---|---|---|
| Binary | 2 | 0, 1 | $(1011)_2$ | `0b1011` |
| Octal | 8 | 0–7 | $(13)_8$ | `0o13` (`013` in C) |
| Decimal | 10 | 0–9 | $(11)_{10}$ | `11` |
| Hexadecimal | 16 | 0–9, A–F | $(\mathrm{B})_{16}$ | `0xB`; `4'hB` in hardware description languages |

Binary is the native language of circuits: one binary digit is a **bit**. The bases of octal and hexadecimal are powers of $2$: one octal digit corresponds to exactly $3$ bits and one hexadecimal digit to exactly $4$ bits, so they are just compact ways of writing binary, and hexadecimal is the one mainly used today.

When stating storage capacity, two sets of prefixes must be distinguished. The SI prefixes k, M, G, T are $10^3, 10^6, 10^9, 10^{12}$, respectively; the binary prefixes Ki, Mi, Gi, Ti specified by IEC 80000-13 are $2^{10}, 2^{20}, 2^{30}, 2^{40}$, respectively. We have $1\,\mathrm{KiB} = 1024$ bytes, while $1\,\mathrm{kB} = 1000$ bytes; disk manufacturers label capacity with SI prefixes and operating systems often display it with binary prefixes, so the two differ by about $10\%$ at the TB scale.

### 1.2.2. Base Conversion

To convert from base $R$ to decimal, expand and sum the polynomial of Definition 1.2.1. For example, $(1101)_2 = 8 + 4 + 1 = (13)_{10}$.

To convert from decimal to base $R$, the integer part and the fractional part are converted separately.

- The integer part uses repeated division by $R$: divide repeatedly by $R$; the remainders are $k_0, k_1, \dots$ in turn, until the quotient is $0$. This works because $N = k_0 + R(k_1 + R(k_2 + \cdots))$, so each division strips off the lowest digit.
- The fractional part uses repeated multiplication by $R$: multiply repeatedly by $R$; the integer parts are $k_{-1}, k_{-2}, \dots$ in turn, until the fractional part is $0$ or the required precision is reached.

**Example 1.2.1** Convert $(75)_{10}$ to binary:

| Dividend | Quotient | Remainder |
|---|---|---|
| 75 | 37 | 1 ($k_0$) |
| 37 | 18 | 1 |
| 18 | 9 | 0 |
| 9 | 4 | 1 |
| 4 | 2 | 0 |
| 2 | 1 | 0 |
| 1 | 0 | 1 ($k_6$) |

Reading from the bottom up, $(75)_{10} = (1001011)_2$. For the fraction $(0.625)_{10}$: $0.625\times2 = 1.25$ gives $1$, $0.25\times2 = 0.5$ gives $0$, and $0.5\times 2 = 1.0$ gives $1$, so $(0.625)_{10} = (0.101)_2$. By contrast, $(0.1)_{10} = (0.0\overline{0011})_2$ is an infinite repeating fraction: a finite decimal fraction is a finite binary fraction only if its denominator (in lowest terms) has no prime factor other than $2$, and this is the source of rounding error in **floating-point numbers** (see [Number Representation in Computers](/3.5.1)).

To convert between binary and octal or hexadecimal, group the digits in sets of $3$ (octal) or $4$ (hexadecimal) outward from the radix point, to the left and to the right, padding with $0$ where necessary, and replace each group by one digit; the reverse conversion expands each digit into $3$ or $4$ bits.

**Example 1.2.2**
- $(1101101)_2 = (001\ 101\ 101)_2 = (155)_8$; $(1101101)_2 = (0110\ 1101)_2 = (6\mathrm{D})_{16}$.
- $(573)_8 = (101\ 111\ 011)_2$; $(5\mathrm{A}3\mathrm{F})_{16} = (0101\ 1010\ 0011\ 1111)_2$.

The process of repeated division by $R$ can be written directly as a program:

```python
def to_base(n: int, r: int) -> str:
    """Convert a non-negative integer to base r (2 <= r <= 16) by repeated division."""
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    out = []
    while n > 0:
        n, k = divmod(n, r)
        out.append(digits[k])
    return "".join(reversed(out))

print(to_base(75, 2), to_base(109, 8), to_base(109, 16))  # 1001011 155 6D
print(int("5A3F", 16), int("1001011", 2))                  # 23103 75
```

### 1.2.3. Signed Numbers

A group of bits in a circuit has no sign by itself; its user decides what it represents. Three encodings represent signed integers: **sign-magnitude representation** (the most significant bit is the sign and the remaining bits are the absolute value), ones' complement (the bits of a negative number are inverted) and **two's complement**. Modern processors use two's complement exclusively, because it lets addition and subtraction share one adder and gives $0$ a single representation. The range of $n$-bit two's complement is $-2^{n-1}$ to $2^{n-1}-1$, and the two's complement of $-x$ is obtained by inverting every bit of the two's complement of $x$ and adding $1$. The definition and properties of two's complement are in [Number Representation in Computers](/3.5.1); the circuit implementation of two's complement addition and subtraction and the detection of **overflow** are in [Arithmetic Circuits](/4.9.5).

## 1.3. Codes

Representing an object (a digit, a character, a state) by a group of bits is called coding. The same object can have several codes, and which one to choose depends on what the circuit has to do with it.

### 1.3.1. Binary Codes for Decimal Numbers

People are used to decimal, while circuits process binary. Displays, counting and financial computation need to preserve decimal digits one by one, and for this purpose four bits represent one decimal digit.

**Definition 1.3.1 (BCD Code)** A code that represents one decimal digit $0$–$9$ by a $4$-bit binary code is called a binary-coded decimal code, abbreviated **BCD**. If the four positions, from high to low, have fixed weights $w_3, w_2, w_1, w_0$, and the code $b_3b_2b_1b_0$ represents the digit $\sum_i w_ib_i$, the code is called a weighted code and is named after its weights (such as the 8421 code); otherwise it is called an unweighted code.

There are $16$ four-bit codes, of which only $10$ are used; the other $6$ are invalid codes. The four commonly used codes:

| Decimal | 8421 code | 5421 code | 2421 code | Excess-3 code |
|---|---|---|---|---|
| 0 | 0000 | 0000 | 0000 | 0011 |
| 1 | 0001 | 0001 | 0001 | 0100 |
| 2 | 0010 | 0010 | 0010 | 0101 |
| 3 | 0011 | 0011 | 0011 | 0110 |
| 4 | 0100 | 0100 | 0100 | 0111 |
| 5 | 0101 | 1000 | 1011 | 1000 |
| 6 | 0110 | 1001 | 1100 | 1001 |
| 7 | 0111 | 1010 | 1101 | 1010 |
| 8 | 1000 | 1011 | 1110 | 1011 |
| 9 | 1001 | 1100 | 1111 | 1100 |

- The 8421 code takes the first ten of the $4$-bit natural binary codes and is the most commonly used BCD code; "BCD code" usually means it. For example, $(93)_{10} = (1001\ 0011)_{\mathrm{8421BCD}}$. Note that a BCD code differs from a binary number: $(93)_{10} = (1011101)_2$.
- The 5421 and 2421 codes are also weighted codes. A digit may have two writings in the 2421 code ($5 = 1011 = 0101$); the choice in the table makes the codes of $k$ and $9-k$ bitwise complements of each other ($4 = 0100$, $5 = 1011$), so the $9$'s complement is obtained by inverting every bit. Such a code is called self-complementing. For example, the 5421 code of $(93)_{10}$ is $1100\ 0011$ and its 2421 code is $1111\ 0011$.
- The excess-3 code is the 8421 code plus $0011$; it is an unweighted code and is also self-complementing.

Addition in the 8421 code needs a correction. Adding two BCD digits as binary numbers gives a sum between $0$ and $19$. If the sum does not exceed $9$, the result is already a correct BCD code; if the sum exceeds $9$ (the four-bit result is an invalid code, or a carry is produced), add $6 = (0110)_2$ to skip the $6$ invalid codes and carry $1$ into the next higher digit.

**Example 1.3.1** $8 + 5$: $1000 + 0101 = 1101 > 9$; adding $0110$ gives $1\ 0011$, which is the BCD code of $13$. $9 + 9$: $1001 + 1001 = 1\ 0010$ has a carry, so add $0110$ to the low $4$ bits to get $1000$, and the result is $1\ 1000$, that is, $18$.

The corresponding rule for excess-3 addition is as follows: the sum of two excess-3 codes contains two "$+3$" offsets. If there is no carry, subtract $3$ from the result; if there is a carry, the carry has already absorbed $16 - 10 = 6$, that is, the two "$+3$" offsets, and $3$ must be added back to the low four bits. For example, $1 + 3$: $0100 + 0110 = 1010$ has no carry, and subtracting $0011$ gives $0111$ (that is, $4$); $5 + 6$: $1000 + 1001 = 1\ 0001$ has a carry, so adding $0011$ to the low four bits gives $0100$ (that is, $1$), and the carry $1$ written in excess-3 code is $0100$, so the result is $0100\ 0100$, that is, $11$.

Today BCD is used mainly where digits must be displayed one by one or decimal rounding must be exact: the registers of real-time clock chips, seven-segment displays, and financial computation (**IEEE 754**-2008 defines decimal floating-point formats, one encoding of which works digit by digit). Early processors had dedicated BCD adjustment instructions (such as `DAA` on x86), which were removed in the 64-bit mode of x86-64.

### 1.3.2. Gray Codes

When a counter goes from $0111$ to $1000$, all four bits flip at once. In a real circuit they cannot change at exactly the same instant, and a reader may see intermediate values such as $1111$ or $0000$ during the transition. If two adjacent codes differ in only one bit, then at any moment what is read can only be the value before or the value after the change.

**Definition 1.3.2 (Gray Code)** A sequence of $n$-bit codes in which any two adjacent codes differ in exactly one bit is called a **Gray code**; if the first and last codes also differ in exactly one bit, it is called a cyclic code.

The most commonly used one is the reflected Gray code (the standard Gray code), which can be constructed recursively: the $1$-bit reflected code is $0, 1$; write the sequence of the $(n-1)$-bit reflected code with $0$ prepended, and then write it again in reverse order with $1$ prepended, to obtain the $n$-bit reflected code. For example, the $2$-bit code is $00, 01, 11, 10$ and the $3$-bit code is $000, 001, 011, 010, 110, 111, 101, 100$.

**Theorem 1.3.1 (Conversion Between Reflected Gray Code and Binary)** Let $B = b_{n-1}\cdots b_1b_0$ be a natural binary number and $G = g_{n-1}\cdots g_1g_0$ the $B$-th reflected Gray code in the sequence. Then

$$
g_{n-1} = b_{n-1},\qquad g_i = b_{i+1} \oplus b_i\quad(0 \le i \le n-2),
$$
that is, $G = B \oplus (B \gg 1)$; conversely,

$$
b_i = g_{n-1} \oplus g_{n-2} \oplus \cdots \oplus g_i .
$$
The reflected Gray code is a cyclic code.

**Proof** We use induction on $n$. For $n = 1$, $G = B$. Assume the claim holds for $n-1$. In the first half, $b_{n-1} = 0$, and the code is $0$ followed by the $(n-1)$-bit reflected code corresponding to the low $n-1$ bits of $B$; in the formula $g_{n-1} = 0$ and $g_{n-2} = b_{n-2} \oplus 0$, consistent with the induction hypothesis. In the second half, $b_{n-1} = 1$, and the $B$-th code is $1$ followed by the $(2^n - 1 - B)$-th $(n-1)$-bit code (in reverse order); the low $n-1$ bits of $2^n - 1 - B$ are exactly the low $n-1$ bits of $B$ with every bit inverted, denoted $\bar b$. In its Gray code $\bar b_{n-2}, \bar b_{n-2}\oplus \bar b_{n-3}, \dots$, all bits except the highest coincide with those of the Gray code of $b$ (the two inversions cancel in the **exclusive or**), and the highest bit is $\bar b_{n-2} = b_{n-2} \oplus 1 = b_{n-1}\oplus b_{n-2}$, in agreement with the formula. The inverse transformation follows by recursion from the high bit downward using $b_{i+1} \oplus g_i = b_i$. Adjacency: within each half it holds by the induction hypothesis; at the junction of the two halves we have $0x$ and $1x$ ($x$ being the last of the $(n-1)$-bit codes), which differ only in the highest bit; the first and last codes are $0\,0\cdots0$ and $1\,0\cdots0$, which also differ in one bit only. $\square$

| Decimal | Binary | Gray code | Decimal | Binary | Gray code |
|---|---|---|---|---|---|
| 0 | 0000 | 0000 | 8 | 1000 | 1100 |
| 1 | 0001 | 0001 | 9 | 1001 | 1101 |
| 2 | 0010 | 0011 | 10 | 1010 | 1111 |
| 3 | 0011 | 0010 | 11 | 1011 | 1110 |
| 4 | 0100 | 0110 | 12 | 1100 | 1010 |
| 5 | 0101 | 0111 | 13 | 1101 | 1011 |
| 6 | 0110 | 0101 | 14 | 1110 | 1001 |
| 7 | 0111 | 0100 | 15 | 1111 | 1000 |

Converting binary to Gray code needs only one XOR gate per bit; converting Gray code to binary is a prefix of XORs, propagated stage by stage from the most significant bit. If the reflected code $0$–$9$ is used to encode decimal digits, $9 = 1101$ and $0 = 0000$ are not adjacent, so it is not a cyclic code; taking the segment $3$–$12$ ($0010, 0110, \dots, 1010$) to encode $0$–$9$, the first and last codes $0010$ and $1010$ differ in only one bit, which gives the excess-3 cyclic code.

![Three code tracks: in the natural binary code three tracks change at once at the boundary between 011 and 100, while in the reflected Gray code only one track changes at each boundary](./plots/gray-code-disk.py)

The main uses of Gray codes:

- Position encoders: the tracks of a rotary or linear encoder are laid out in Gray code, so even when the read head sits exactly on a boundary, the reading is off by only one position.
- Karnaugh maps: the rows and columns of a Karnaugh map are arranged in Gray code, so that geometrically adjacent cells correspond to **minterms** that differ in only one variable ([Logic Algebra and Minimization](/4.9.2)).
- Passing counter values across clock domains: the read and write pointers of an asynchronous FIFO are sent to the other clock domain in Gray code, so even if sampling occurs during a change, what is obtained is only the adjacent old or new value.
- State encoding: a state machine whose states change sequentially is encoded in Gray code, so that each transition flips only one flip-flop, which reduces power consumption and glitches ([Synchronous Sequential Circuits](/4.9.7)).

### 1.3.3. Character Codes

Text must also be encoded into bits. The most basic **character encoding** is ASCII (American Standard Code for Information Interchange), which represents $128$ characters by $7$-bit codes $b_6b_5\cdots b_0$, divided into regions by the high three bits:

| $b_6b_5b_4$ | Hexadecimal range | Content |
|---|---|---|
| 000, 001 | 00–1F | Control characters (line feed 0A, carriage return 0D, tab 09, etc.) |
| 010, 011 | 20–3F | Space, digits 0–9 (30–39), punctuation |
| 100, 101 | 40–5F | Uppercase letters A–Z (41–5A) and a few symbols |
| 110, 111 | 60–7F | Lowercase letters a–z (61–7A) and a few symbols; 7F is DEL |

This layout takes the convenience of circuit processing into account: the low $4$ bits of the digits `'0'`–`'9'` are exactly their 8421 codes, and uppercase and lowercase letters differ only in $b_5$ (a difference of `0x20`), so flipping one bit converts case. Text today generally uses Unicode, whose UTF-8 encoding is fully compatible with ASCII: characters with code values below $128$ still occupy one byte and are encoded as in ASCII.

### 1.3.4. Error-Detecting Codes

During storage and transmission, noise and radiation may flip individual bits. If redundant bits computed by a rule are appended to the data bits, the receiver can check whether the rule still holds and thus detect errors.

**Definition 1.3.3 (Parity Code)** Append one check bit $p$ to $n$ data bits $b_1, \dots, b_n$ so that the number of $1$s in the whole $(n+1)$-bit code is even (even parity) or odd (odd parity); the resulting code is called a **parity code**. For even parity,

$$
p = b_1 \oplus b_2 \oplus \cdots \oplus b_n ,
$$
and the receiver computes $S = b_1 \oplus \cdots \oplus b_n \oplus p$; $S = 1$ indicates an error. For odd parity the check bit is the opposite.

A parity code can detect only errors in an odd number of bits; it cannot detect an even number of simultaneous bit errors, nor tell which bit is wrong. What measures the error-detecting and error-correcting ability of a code is the code distance.

**Definition 1.3.4 (Code Distance)** The number of positions in which two codes of equal length differ is called their **Hamming distance**; the minimum Hamming distance over all pairs of valid codes of a code is called the code distance (minimum distance) of that code.

**Theorem 1.3.2** A code with code distance $d$ can detect any error of at most $d-1$ bits and can correct any error of at most $\lfloor (d-1)/2 \rfloor$ bits.

**Proof** When fewer than $d$ bits are in error, the received code cannot become another valid code, so the error is detected. If at most $t = \lfloor (d-1)/2\rfloor$ bits are in error, the received code is at distance at most $t$ from the original; by the triangle inequality, its distance from any other valid code is at least $d - t > t$, so choosing the nearest valid code recovers the original uniquely. $\square$

A binary code without checking has code distance $1$; a parity code has code distance $2$, which detects a one-bit error and cannot correct errors; Hamming codes use several check bits to raise the code distance to $3$, which corrects a one-bit error and is used for ECC memory, see [Data Representation and Error Correction](/4.10.4). Generating and checking a parity bit is an XOR tree, whose circuit is in [Combinational Logic Circuits](/4.9.4).

## Summary

| Topic | Key points |
|---|---|
| Digital signals | Two voltage ranges represent $0$ and $1$; noise immunity, regeneration, and distortion-free copying |
| Positional number systems | $N = \sum k_iR^i$; decimal to base $R$: divide the integer part by $R$ and take remainders, multiply the fractional part by $R$ and take integer parts; binary to octal or hexadecimal by grouping $3$ or $4$ bits |
| BCD codes | 8421, 5421 and 2421 (self-complementing) are weighted codes, and excess-3 is an unweighted self-complementing code; in 8421 addition, correct a sum above $9$ by adding $6$ |
| Gray codes | Adjacent codes differ in one bit; $G = B \oplus (B \gg 1)$, $b_i = g_{n-1}\oplus\cdots\oplus g_i$; used in encoders, Karnaugh maps and clock-domain crossing |
| ASCII | $7$ bits; the low $4$ bits of a digit are its 8421 code, and case differs in $b_5$ |
| Error-detecting codes | A parity code has code distance $2$ and detects errors in an odd number of bits; code distance $d$ detects $d-1$ and corrects $\lfloor(d-1)/2\rfloor$ bits |
