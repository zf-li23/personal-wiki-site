---
title: Data Representation and Error Detection and Correction
description: "How data is encoded in machine words: characters (ASCII, Unicode, UTF-8), unsigned and signed integers (sign-magnitude, ones' complement, two's complement, biased representation), sign extension and endianness, IEEE 754 floating point and rounding modes, low-precision formats for AI (BF16, FP8, MXFP4); error-detecting and error-correcting codes: code distance, parity, Hamming codes and SECDED, cyclic redundancy checks (CRC), erasure codes."
source_hash: 43da00858d89
---

A processor understands only bits. Programs, integers, real numbers, characters, and logical values are all, in the end, strings of $0$s and $1$s in machine words; how a given string is interpreted is decided by the instruction that uses it: `add` treats two words as **two's complement** integers, `fadd.s` treats them as single-precision **floating-point numbers**, and a byte fetched by `lbu` may be an ASCII character. This chapter collects the encodings of the data types found in a computer and the hardware-related properties of each. The first half covers how data is represented (the general representation of numbers in a computer was treated in [Computer Representation of Numbers](/3.5.1) and [Data, Variables and Expressions](/4.1.2); here we concentrate on machine-level details and the new low-precision formats), and the second half covers how errors in stored or transmitted data are detected and corrected. The arithmetic unit of the next chapter implements arithmetic on these encodings.

## 4.1. Encoding Data

### 4.1.1. Principles of Encoding

An encoding is an agreement to represent an object by a group of bits. Since $n$ bits have only $2^n$ combinations, at most $2^n$ different objects can be distinguished: the $26$ English letters need $5$ bits, adding upper and lower case, digits, and punctuation needs $7$ bits, and all the world's scripts together need a code space of $21$ bits (Unicode). Several considerations enter the design of an encoding:

- a few simple basic symbols ($0$ and $1$) and definite rules should represent a large amount of complex information;
- the encoding should be convenient for hardware arithmetic (**two's complement** lets addition and subtraction share one adder) and for comparison and sorting (in ASCII the letters are in alphabetical order);
- range, precision, and storage space must be traded off against one another.

The simplest data are logical values: $1$ means true and $0$ means false, and the operations are bitwise AND, OR, NOT, and **exclusive or**, which the processor performs on an entire word with instructions such as `and`, `or`, and `xor` (NOT is `xori rd, rs, -1`). C has no separate logical bit; it uses the integer $0$ for false and any nonzero value for true.

### 4.1.2. Characters

Characters are the basis of the human–machine interface: keyboard input, screen output, and text files are all sequences of characters. A **character encoding** assigns a binary code to every character and is the basis for exchanging information between a host and its peripherals and between hosts.

- ASCII: $7$ bits, $128$ characters (control characters, digits, English letters, and punctuation), usually stored in one byte with the top bit $0$. Its layout is convenient for circuits; see [Introduction: Number Systems and Codes](/4.9.1).
- Unicode: every character of every script is assigned a unique number, called a code point and written U+XXXX, in the range U+0000 to U+10FFFF (about $1.11$ million code points). The early UCS-2 used a fixed $16$ bits per character, which can hold only $65536$ code points (the Basic Multilingual Plane), and was later replaced by the variable-length UTF-16.
- UTF-8: the most common storage encoding of Unicode, which uses $1$ to $4$ bytes per character depending on the size of the code point:

| Code point range | Payload bits | Byte 1 | Byte 2 | Byte 3 | Byte 4 |
|---|---|---|---|---|---|
| U+0000–U+007F | 7 | `0xxxxxxx` | | | |
| U+0080–U+07FF | 11 | `110xxxxx` | `10xxxxxx` | | |
| U+0800–U+FFFF | 16 | `1110xxxx` | `10xxxxxx` | `10xxxxxx` | |
| U+10000–U+10FFFF | 21 | `11110xxx` | `10xxxxxx` | `10xxxxxx` | `10xxxxxx` |

UTF-8 has several advantages: it is fully compatible with ASCII; the length of a character is determined by the prefix of its first byte; every byte other than the first begins with `10`, so reading can start from any position and still find the beginning of the next character (self-synchronization); and byte-wise comparison gives the same order as comparison by code point. It is by far the dominant encoding on the Internet today.

**Example 4.1.1** The Chinese character meaning "clear" has code point U+6E05 $= 0110\,1110\,0000\,0101_2$, which falls in the three-byte range. Filling the $16$ payload bits into the template in groups of $4 + 6 + 6$ gives $1110\,0110$, $10\,111000$, $10\,000101$, that is, the byte sequence `E6 B8 85`.

Displaying a character requires a glyph. Early bitmap fonts stored each character as a monochrome bitmap (for example a $16\times16$ grid in which $1$ means a dot), looked up in a font table by character code; enlarged, they show jagged edges. Today's standard is the vector font (TrueType, OpenType): a glyph is described by the control points of several curves, which are scaled proportionally, joined by smooth curves, and filled when displayed, so the glyph can be scaled arbitrarily.

## 4.2. Integers

Numeric data are divided into fixed-point and **floating-point numbers**: in a **fixed-point number** the position of the radix point is fixed, and an integer is a fixed-point number with the radix point at the far right; in a floating-point number the radix point floats with the exponent (§4.3). A numeric format has two measures: its range is the largest and smallest values it can represent, and its precision is the number of significant digits it can give. Both depend on how many bits are used and how they are encoded, but the two concepts are different: the range of a $32$-bit integer is much smaller than that of a single-precision float, yet it has more significant bits.

### 4.2.1. Unsigned Integers

The value of an $n$-bit unsigned integer $b_{n-1}\cdots b_1b_0$ is the sum of the weights of its bits:

$$
U = \sum_{i=0}^{n-1} b_i 2^i ,
$$
and its range is $0$ to $2^n - 1$. The sizes of C integer types on **RISC-V** are fixed by the **calling convention** (the psABI): RV32 uses ILP32 (`int`, `long`, and pointers are all $32$ bits), and RV64 uses LP64 (`long` and pointers are $64$ bits, `int` is still $32$ bits); `char` is $8$ bits and, on RISC-V, unsigned by default (unlike x86). The constants `UCHAR_MAX` $=255$, `USHRT_MAX` $=65535$, and `UINT_MAX` $=2^{32}-1$ in `<limits.h>` are the upper bounds of these types.

### 4.2.2. Sign-Magnitude, Ones' Complement, and Two's Complement

A signed integer needs a mechanism for representing negative numbers. The three classical encodings all use the top bit $b_{n-1}$ to distinguish the sign ($0$ for positive, $1$ for negative); the three encodings of a positive number coincide, and they differ in the negative numbers.

**Definition 4.2.1 (Sign-Magnitude and Ones' Complement)** Consider an $n$-bit code $b_{n-1}b_{n-2}\cdots b_0$. In **sign-magnitude representation**, $b_{n-1}$ is the sign and the remaining $n-1$ bits are the absolute value, so the value is $(-1)^{b_{n-1}}\sum_{i=0}^{n-2}b_i2^i$. In **ones' complement**, the code of a negative number $-x$ is the bitwise complement of the code of $x$, and the value is $-b_{n-1}(2^{n-1}-1)+\sum_{i=0}^{n-2}b_i2^i$.

**Definition 4.2.2 (Two's Complement)** The value of an $n$-bit **two's complement** code is

$$
X = -b_{n-1}2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i ,
$$
that is, the weight of the top bit is $-2^{n-1}$. Equivalently, the two's complement of an integer $x \in [-2^{n-1}, 2^{n-1}-1]$ is the $n$-bit binary representation of $x \bmod 2^n$, written $[x]_{\text{tc}}$.

| Code (4 bits) | Unsigned | Sign-magnitude | Ones' complement | Two's complement |
|---|---|---|---|---|
| `0000` | 0 | $+0$ | $+0$ | 0 |
| `0111` | 7 | 7 | 7 | 7 |
| `1000` | 8 | $-0$ | $-7$ | $-8$ |
| `1001` | 9 | $-1$ | $-6$ | $-7$ |
| `1110` | 14 | $-6$ | $-1$ | $-2$ |
| `1111` | 15 | $-7$ | $-0$ | $-1$ |
| Range | $[0, 15]$ | $[-7, 7]$ | $[-7, 7]$ | $[-8, 7]$ |

**Sign-magnitude** is intuitive, but addition and subtraction must first compare signs and absolute values; sign-magnitude and ones' complement both have two zeros ($+0$ and $-0$), so a zero test must compare two codes. Two's complement has a single zero, its range of positive and negative numbers differs by one (the extra number is $-2^{n-1}$), and addition need not distinguish the sign bit from the value bits, so modern processors use two's complement for all integers. Sign-magnitude is still used for the mantissa of floating-point numbers (§4.3).

**Theorem 4.2.1 (Properties of Two's Complement)** Let $x, y$ and the results of the operations all lie within the range of $n$-bit two's complement, and let $\sim$ denote bitwise complement.

1. $[x+y]_{\text{tc}} = ([x]_{\text{tc}} + [y]_{\text{tc}}) \bmod 2^n$; that is, add the two codes as unsigned numbers and discard the carry out of bit $n$;
2. $[-x]_{\text{tc}} = (\sim[x]_{\text{tc}} + 1) \bmod 2^n$ ($x \ne -2^{n-1}$);
3. $[x-y]_{\text{tc}} = ([x]_{\text{tc}} + \sim[y]_{\text{tc}} + 1) \bmod 2^n$.

**Proof** By definition, $[x]_{\text{tc}} \equiv x \pmod{2^n}$. (1) Both sides are congruent to $x+y$ modulo $2^n$ and both lie in $[0, 2^n)$, so they are equal. (2) Every $n$-bit code $a$ satisfies $a + {\sim}a = 2^n - 1$, so ${\sim}[x]_{\text{tc}} + 1 = 2^n - [x]_{\text{tc}} \equiv -x \pmod{2^n}$. (3) follows from (1) and (2). $\square$

Property (3) says that subtraction only requires complementing the subtrahend and setting the carry-in of the lowest bit of the adder to $1$; the arithmetic unit of the next chapter uses exactly this to perform addition and subtraction with one adder. When the result leaves the range of $n$-bit two's complement, **overflow** occurs; how to detect it is also given in the next chapter.

**Example 4.2.1** Exactly one negative number has the same sign-magnitude and two's complement codes. Let its absolute value be $m$; its sign-magnitude code is $2^{n-1} + m$ and its two's complement code is $2^n - m$; equating the two gives $m = 2^{n-2}$. For $n = 32$ this number is $-2^{30}$, with code `1100 0000 … 0000` (`0xC0000000`).

### 4.2.3. Sign Extension and Zero Extension

When a shorter integer is placed in a wider **register**, its value must be preserved.

**Definition 4.2.3 (Sign Extension and Zero Extension)** When an $n$-bit code is extended to $m > n$ bits, filling all of the upper $m-n$ bits with the original top bit $b_{n-1}$ is called **sign extension**; filling them all with $0$ is called **zero extension**.

**Theorem 4.2.2** Sign extension preserves the value of a two's complement number, and zero extension preserves the value of an unsigned number.

**Proof** The case of zero extension is obvious. For sign extension it suffices to check extension by one bit: if $b_{n-1} = 0$, the new top bit is $0$ and the value is unchanged; if $b_{n-1} = 1$, the old top bit contributed $-2^{n-1}$, and after extension the two top bits together contribute $-2^n + 2^{n-1} = -2^{n-1}$, so the value is unchanged. Induction on the number of bits finishes the proof. $\square$

For example, in C, `int y = -100; long x = (long) y;` on RV64 sign-extends the $32$-bit `0xFFFFFF9C` to `0xFFFFFFFFFFFFFF9C`, whose value is still $-100$. RISC-V uses both kinds of extension everywhere:

- memory access: `lb` and `lh` (and `lw` on RV64) sign-extend the loaded data to the whole register, while `lbu`, `lhu`, and `lwu` zero-extend;
- immediates: the $12$-bit immediate in an instruction is always sign-extended, so the immediate range of `addi` is $[-2048, 2047]$;
- on RV64, `addw`, `subw`, and other $32$-bit operations sign-extend the result to $64$ bits.

### 4.2.4. Biased Representation

**Definition 4.2.4 (Biased Representation)** Fix an offset $K$ and encode an integer $E$ as the binary representation of the unsigned number $E + K$. This is called **biased representation** (also called excess-$K$ code).

An $n$-bit biased code usually takes $K = 2^{n-1}$ or $2^{n-1}-1$. The advantage of a biased code is that the order of the codes as unsigned numbers agrees with the order of the true values, and the smallest number is encoded as all zeros. The exponent field of **IEEE 754** is a biased code with $K = 2^{k-1}-1$ ("bias $127$" in single precision), and this offset is the **exponent bias**; as a result, two floating-point numbers of the same sign can be compared directly as integers, and the encoding of the floating-point number $0$ is also exactly all zeros.

### 4.2.5. Endianness

Main memory is byte-addressed, and a $32$-bit word occupies $4$ consecutive addresses. If the least significant byte of the word is placed at the lowest address, the arrangement is **little-endian**; if it is placed at the highest address, it is **big-endian**. For example, `0x12345678` stored in the $4$ bytes starting at address `0x100` is laid out as follows:

| Address | `0x100` | `0x101` | `0x102` | `0x103` |
|---|---|---|---|---|
| **Little-endian** | `78` | `56` | `34` | `12` |
| **Big-endian** | `12` | `34` | `56` | `78` |

RISC-V, x86, and most ARM systems are little-endian; network protocols transmit fields in big-endian order ("network **byte order**"). RISC-V instructions are always stored little-endian; data accesses can be configured as big-endian in the privileged architecture, but common software environments all use little-endian. Endianness affects only the arrangement of multibyte data in memory, not the values in registers; conversion is needed only when binary data is exchanged between machines of different endianness.

## 4.3. Floating-Point Numbers

### 4.3.1. The IEEE 754 Formats

A **floating-point number** represents a real number in scientific notation, $x = (-1)^s \times M \times 2^{E}$, so only the sign $s$, the mantissa $M$, and the exponent $E$ need to be stored. The **IEEE 754 standard** (published in 1985, revised in 2008 and 2019) specifies the binary floating-point formats used by almost all computers today. Its design was discussed in detail in [Computer Representation of Numbers](/3.5.1), so here we summarize only the points that matter for hardware. A floating-point number consists of three fields:

| Format | Sign $s$ | Exponent field `exp` | Fraction field `frac` | Bias $K$ | Precision $p$ |
|---|---|---|---|---|---|
| **Single precision** (binary32, C `float`) | 1 | 8 | 23 | 127 | 24 |
| **Double precision** (binary64, C `double`) | 1 | 11 | 52 | 1023 | 53 |

The value of the exponent field divides the numbers into four classes ($k$ is the number of exponent bits and $K = 2^{k-1}-1$):

| `exp` | `frac` | Value | Class |
|---|---|---|---|
| $1$ to $2^k-2$ | any | $(-1)^s \times 1.\mathtt{frac} \times 2^{\mathtt{exp}-K}$ | normalized number |
| $0$ | $\ne 0$ | $(-1)^s \times 0.\mathtt{frac} \times 2^{1-K}$ | **subnormal number** |
| $0$ | $0$ | $\pm 0$ | zero |
| $2^k-1$ | $0$ | $\pm\infty$ | infinity |
| $2^k-1$ | $\ne 0$ | NaN | **NaN** |

Several points deserve attention:

- The mantissa uses **sign-magnitude representation**: the sign is a separate bit, and `frac` is the fractional part of the absolute value of the mantissa. The top bit of the mantissa of a normalized number is necessarily $1$ and need not be stored; this is the **hidden bit** technique, which lets a $23$-bit fraction field provide $24$ bits of precision. Before an operation, the hardware must first restore this bit.
- The exponent uses a biased code, so that the all-zero code represents $+0$, and so that the order of nonnegative floating-point numbers agrees with the order of their codes as unsigned integers.
- The exponent of a **subnormal number** is $1-K$ rather than $0-K$ and the hidden bit is $0$, which fills the gap between $0$ and the smallest normalized number $2^{1-K}$ uniformly (gradual **underflow**). In single precision the two smallest positive normalized numbers are $2^{-126}$ and $2^{-126}+2^{-149}$, and originally there was no representable number between $0$ and $2^{-126}$; with subnormal numbers the smallest positive number is $2^{-149}$, and the spacing is nowhere larger than $2^{-149}$.
- The range of single-precision normalized numbers is about $1.18\times10^{-38}$ to $3.40\times10^{38}$, and that of **double precision** is about $2.23\times10^{-308}$ to $1.80\times10^{308}$. An absolute value above the largest number is an overflow, and the result is $\pm\infty$; a nonzero result whose absolute value is below the smallest normalized number is an underflow.
- NaN represents a meaningless result ($0/0$, $\infty-\infty$, $\sqrt{-4}$) and propagates through later operations: any operation involving a NaN yields a NaN, which helps in debugging.

![All nonnegative finite values of an 8-bit toy format (1 sign bit, 3 exponent bits, 2 fraction bits, bias 3): each binary octave $[2^e, 2^{e+1})$ contains 4 equally spaced numbers, and the spacing grows with the octave; subnormal numbers fill the gap between 0 and the smallest normalized number with the same spacing](./plots/minifloat-values.py)

**Example 4.3.1** Represent $-0.75$ as a single-precision number. Since $-0.75 = -0.11_2 = -1.1_2 \times 2^{-1}$, we have $s = 1$, `exp` $= -1 + 127 = 126 = 0111\,1110_2$, and `frac` $= 100\cdots0$. The encoding is `1 01111110 10000000000000000000000` $=$ `0xBF400000`.

**Example 4.3.2** Decimal fractions usually cannot be represented exactly. We have $0.1 = 1.6 \times 2^{-4}$, and the binary expansion of $0.6$ is the repeating fraction $0.1001\,1001\,1001\cdots_2$. Then `exp` $= -4 + 127 = 123 = 0111\,1011_2$; `frac` takes the first $23$ bits of the repeating fraction, $10011001100110011001100$, and the following bits are $1100\cdots$, which exceed one half, so round-to-nearest rounds up by $1$ to give $10011001100110011001101$. The encoding is `0x3DCCCCCD`, whose value is $0.100000001490116\cdots$, slightly larger than $0.1$. In general, to convert a decimal number to a binary floating-point number, first compute enough significant bits, then round to the precision of the format, and finally fill in the sign, exponent, and fraction fields.

### 4.3.2. Rounding

The exact result of a **floating-point operation** generally cannot be represented in finitely many bits, and type conversions (double to single precision, floating point to integer) also lose bits, so rounding is needed. **IEEE 754** specifies five rounding modes; the F/D extensions of RISC-V select one in the `frm` field of the floating-point control and status register `fcsr`, and each floating-point instruction can also specify one statically:

| IEEE 754 name | RISC-V mnemonic | Meaning | $2.5$ | $-2.5$ | $2.001$ | $-1.999$ |
|---|---|---|---|---|---|---|
| roundTiesToEven (default) | RNE | to nearest, ties to the number with an even last digit | $2$ | $-2$ | $2$ | $-2$ |
| roundTiesToAway | RMM | to nearest, ties to the larger absolute value | $3$ | $-3$ | $2$ | $-2$ |
| roundTowardZero | RTZ | toward zero (truncation) | $2$ | $-2$ | $2$ | $-1$ |
| roundTowardPositive | RUP | toward $+\infty$ (up) | $3$ | $-2$ | $3$ | $-1$ |
| roundTowardNegative | RDN | toward $-\infty$ (down) | $2$ | $-3$ | $2$ | $-2$ |

The table uses rounding to an integer as an example. The default "round to nearest, ties to even" is statistically unbiased, so long accumulations are not systematically too large or too small. C always truncates (rounds toward zero) when converting a floating-point number to an integer, which is why RISC-V `fcvt.w.s` is often used with `rtz`. How rounding is implemented in hardware is described in [The Arithmetic Unit](/4.10.5). The errors introduced by rounding and their analysis are covered under **rounding error** and **machine epsilon** in [Computer Representation of Numbers](/3.5.1).

### 4.3.3. Low-Precision Formats

Deep learning requires an enormous amount of computation but is insensitive to the precision of individual values, which has driven a series of formats narrower than single precision. The area of a floating-point unit is dominated by the mantissa multiplier and grows roughly as the square of the mantissa width; halving the width lets the same chip area hold several times as many arithmetic units, and halves storage and bandwidth requirements.

| Format | Sign | Exponent | Mantissa | Largest finite value | Standard and use |
|---|---|---|---|---|---|
| FP64 | 1 | 11 | 52 | $1.8\times10^{308}$ | IEEE 754 binary64; scientific computing |
| FP32 | 1 | 8 | 23 | $3.4\times10^{38}$ | IEEE 754 binary32 |
| TF32 | 1 | 8 | 10 | $3.4\times10^{38}$ | Internal Tensor Core format since NVIDIA A100; $19$ bits stored in $32$ |
| FP16 | 1 | 5 | 10 | $65504$ | IEEE 754 binary16; small range, training needs loss scaling |
| **BF16** | 1 | 8 | 7 | $3.4\times10^{38}$ | Proposed by Google, not part of IEEE 754; same range as FP32 |
| FP8 E4M3 | 1 | 4 | 3 | $448$ | OCP FP8 specification; no infinity, only one NaN encoding is kept to extend the range |
| FP8 E5M2 | 1 | 5 | 2 | $57344$ | OCP FP8 specification; keeps infinity and NaN, a truncated FP16 |
| FP4 E2M1 | 1 | 2 | 1 | $6$ | Represents only $0, 0.5, 1, 1.5, 2, 3, 4, 6$ and their negatives |

**BF16** keeps the $8$-bit exponent of FP32 and is exactly the upper $16$ bits of FP32, so conversion only truncates (or rounds) the mantissa; it has become the mainstream format for training large models. The two FP8 variants show that range and precision cannot both be had: E5M2 has a larger range and E4M3 higher precision. A common practice is to use E4M3 in the forward pass (weights and activations) and E5M2 in the backward pass (gradients), while DeepSeek-V3 uses E4M3 for all tensors together with fine-grained scaling.

When the bit width is very small, a single format cannot cover the range of values in a tensor, and two kinds of approaches have appeared:

- Block scaling (microscaling): neighboring elements of a matrix usually have similar magnitudes, so a small block of elements can share one scale factor that rescales them into the range representable in the low-precision format. In the OCP MX specification, every $32$ elements share one $8$-bit scale factor that represents only powers of $2$: the actual value of MXFP4 is each FP4 element times the common scale factor, an average of $4.25$ bits per element. NVIDIA's NVFP4 instead shares one E4M3 scale factor among every $16$ elements.
- Tapered precision: the bit widths of the exponent and mantissa are allocated dynamically within one encoding, with a wide mantissa and high precision for absolute values near $1$, and a wide exponent and large range for very large or very small absolute values. The posit format and Huawei Ascend's HiFloat8 take this approach.

Hardware support has evolved accordingly: NVIDIA Tensor Cores supported only FP16 in 2016, added INT8 and INT4 in 2018, BF16 and TF32 in 2020, FP8 in 2022, and FP6, FP4, and microscaling formats in 2024; Huawei Ascend and Google TPU have followed similar paths. Training usually mixes several formats: **matrix multiplication** uses low precision to exploit compute throughput, while accumulation, master weights, and optimizer states use FP32 for numerical stability ([Infrastructure for Large Models](/4.7.8)).

## 4.4. Error Detection and Correction

Data can be corrupted in storage and transmission: cosmic rays and $\alpha$ particles can flip bits in memory cells (soft errors), channel noise can make the received bits differ from those sent, and whole blocks of data on a disk or in a network can even be lost. There are two ways to decide whether data is in error: compare it against all legal codes, or give the code a certain feature in advance and check whether the feature is present. Error-detecting and error-correcting codes take the latter approach: redundant check bits are appended to the data bits according to a rule, and the receiver checks whether the rule holds; if it can also say which bit is wrong, it can complement that bit to correct the error. Such a code thus involves three steps: encoding, checking, and correcting.

### 4.4.1. Code Distance

**Definition 4.4.1 (Hamming Distance and Code Distance)** The number of positions in which two codes of equal length differ is called their **Hamming distance**. The minimum Hamming distance between any two legal codes of an encoding is called the **code distance** (minimum distance) of the encoding.

If all $2^k$ combinations of $k$ bits are legal codes, the **minimum distance** is $1$: an error in any single bit turns one legal code into another, so it cannot be detected. If $4$ bits are used to represent only $8$ states, we can choose $8$ codes that differ pairwise in at least two bits as legal codes and let the other $8$ be illegal, so that an error in any single bit yields an illegal code and is detected. The code distance determines the capability of an encoding ([Theorem 1.3.2](/4.9.1#thm-1.3.2) of [Introduction: Number Systems and Codes](/4.9.1)): an encoding of code distance $d$ can detect errors of up to $d-1$ bits and correct errors of up to $\lfloor (d-1)/2 \rfloor$ bits; detecting $t_{\mathrm{d}}$ bits while correcting $t_{\mathrm{c}}$ bits ($t_{\mathrm{d}} \ge t_{\mathrm{c}}$) requires $d \ge t_{\mathrm{c}} + t_{\mathrm{d}} + 1$. The larger the code distance, the stronger the capability, but representing the same number of legal codes takes more bits, which increases circuit complexity and the amount of data stored and transmitted.

| Code | Code distance | Capability | Typical use |
|---|---|---|---|
| **Parity code** | 2 | detects 1-bit errors | parallel transmission, early memory, cache tags |
| Hamming code | 3 | corrects 1-bit errors | parallel transmission and storage |
| Extended Hamming code (SECDED) | 4 | corrects 1-bit errors and detects 2-bit errors | ECC memory, caches |
| Cyclic redundancy check | depends on the generator polynomial | detects multi-bit and burst errors | serial transmission, networks, storage |

### 4.4.2. Parity

**Definition 4.4.2 (Parity Code)** Add $1$ check bit $P$ to $k$ data bits $D_1, \dots, D_k$ so that the number of $1$s in the resulting $k+1$-bit code is always even (even parity) or odd (odd parity); the resulting code is called a **parity code**. For even parity,

$$
P = D_1 \oplus D_2 \oplus \cdots \oplus D_k ,
$$
and the receiver computes $S = D_1 \oplus \cdots \oplus D_k \oplus P$; $S = 1$ indicates an error.

For example, the even parity bit of the data `0001` is $1$ and its odd parity bit is $0$; the even parity bit of `0101` is $0$ and its odd parity bit is $1$. A parity code has code distance $2$; it detects only errors in an odd number of bits, cannot detect an even number of simultaneous errors, and cannot correct any error. The generating and checking circuits are both an **exclusive or** (XOR) tree: $k$ data bits pass through $\lceil \log_2 k \rceil$ levels of two-input XOR gates to produce $P$, with very small delay, which suits word-by-word use on parallel buses.

### 4.4.3. Hamming Codes

To correct an error, we must know which bit is wrong. The idea of R. Hamming (1950) is to provide several check bits, each checking a different subset of the data bits, so that an error in any one bit makes a distinct set of check bits fail; the failing combination of check bits then reveals the position of the error.

**Theorem 4.4.1** Suppose $r$ check bits are provided for $k$ data bits so that an error in any one of the $k+r$ bits can be located. Then

$$
2^r \ge k + r + 1 .
$$

**Proof** The receiver evaluates $r$ check relations and obtains an $r$-bit result, which distinguishes at most $2^r$ cases; the cases to be distinguished number $k+r+1$: no error, or an error in exactly one of the $k+r$ bits. $\square$

The smallest $r$ satisfying the inequality is $r = 3$ for $k = 4$, $r = 4$ for $k = 8$, and $r = 5, 6, 7$ for $k = 16, 32, 64$. The proportion of check bits falls as $k$ grows.

**Definition 4.4.3 (Hamming Code)** Let $n = k + r$, where $r$ is the smallest integer satisfying Theorem 4.4.1. Number the positions of an $n$-bit code $1, \dots, n$, place the check bits $P_1, P_2, P_4, \dots, P_{2^{r-1}}$ at the power-of-two positions $1, 2, 4, \dots, 2^{r-1}$, and place the data bits in the remaining positions in order. The check bit $P_{2^i}$ is the XOR of all data bits whose position numbers have a $1$ in binary digit $i$, so that the number of $1$s in this group of bits (including $P_{2^i}$ itself) is even. The resulting $(n, k)$ code is called a **Hamming code**.

Take $k = 4$ as an example. The arrangement and check relations of the $7$-bit code are as follows (`×` marks a bit that takes part in the check):

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Content | $P_1$ | $P_2$ | $D_1$ | $P_4$ | $D_2$ | $D_3$ | $D_4$ |
| Position in binary | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
| Group $P_1$ | × | | × | | × | | × |
| Group $P_2$ | | × | × | | | × | × |
| Group $P_4$ | | | | × | × | × | × |

That is, $P_1 = D_1 \oplus D_2 \oplus D_4$, $P_2 = D_1 \oplus D_3 \oplus D_4$, and $P_4 = D_2 \oplus D_3 \oplus D_4$. The position number of each data bit is exactly the sum of the numbers of the check bits of the groups it belongs to (for example $7 = 1+2+4$), the combinations of groups of different data bits are all distinct, and each check bit belongs to only one group.

**Theorem 4.4.2 (Decoding a Hamming Code)** Let the received code be $c_1c_2\cdots c_n$ and define the syndrome

$$
S = \bigoplus_{j\,:\,c_j = 1} j ,
$$
that is, the bitwise XOR in binary of the position numbers of all bits whose value is $1$; equivalently, bit $i$ of $S$ is the XOR of all bits of group $i$. If there is no error, $S = 0$; if exactly bit $j$ is in error, $S = j$.

**Proof** By the encoding rule, every group of a correct code contains an even number of $1$s, so every bit of $S$ is $0$. Flipping bit $j$ changes the parity of exactly those groups $i$ for which bit $i$ of $j$ is $1$, so those bits of $S$ become $1$ and the others remain $0$; that is, $S = j$. $\square$

The error-correcting hardware is therefore: recompute $S$ with an XOR tree, use a **decoder** to turn $S$ into $n$ select lines, and complement the selected bit; when $S = 0$, nothing is changed.

**Example 4.4.1** Let the data be $D_1D_2D_3D_4 = 1011$. Then $P_1 = 1 \oplus 0 \oplus 1 = 0$, $P_2 = 1 \oplus 1 \oplus 1 = 1$, and $P_4 = 0 \oplus 1 \oplus 1 = 0$, so the transmitted code (positions 1 to 7) is `0110011`. If bit 5 is in error, the received code is `0110111`; the positions with value $1$ are $2, 3, 5, 6, 7$, and $S = 010 \oplus 011 \oplus 101 \oplus 110 \oplus 111 = 101_2 = 5$; complementing bit 5 restores the original code.

A Hamming code has code distance $3$: if two bits are in error simultaneously, $S$ equals the XOR of the two position numbers, which is nonzero but points to a position that is not in error, and "correcting" it would introduce a further error. In practice one more overall check bit is added to distinguish one-bit from two-bit errors.

**Definition 4.4.4 (Extended Hamming Code)** Adding to a Hamming code one more overall check bit $P_0$, chosen so that the number of $1$s in all $n+1$ bits is even, gives an **extended Hamming code**. It can correct one-bit errors and detect two-bit errors, and is also called a **SECDED code** (single-error correction, double-error detection).

When decoding, we compute both $S$ and the overall parity $Q$ of all $n+1$ bits ($Q = 0$ if there is no error):

| $S$ | $Q$ | Conclusion | Action |
|---|---|---|---|
| $0$ | $0$ | no error | none |
| $\ne 0$ | $1$ | an odd number of errors, treated as a one-bit error: bit $S$ is wrong | complement bit $S$ |
| $0$ | $1$ | the overall check bit $P_0$ itself is wrong | the data is correct |
| $\ne 0$ | $0$ | two-bit error | report an uncorrectable error |

A SECDED code has code distance $4$. For $k$ data bits, $r+1$ check bits are needed in all, where $r$ satisfies $2^r \ge k + r + 1$; writing the total number of check bits as $r'$, the condition is $2^{r'-1} \ge k + r'$. $64$ data bits need $8$ check bits, which is why the data width of a server ECC memory module is $72$ bits. The example with $3$ data bits is the case $k = 3$, $r = 3$: the data $110$ is encoded as $P_1P_2D_1P_4D_2D_3 = 011110$, with overall check bit $P_0 = 0$.

The following Python program implements SECDED encoding and checking for any word width according to the definition, and can be used to verify the examples above:

```python
def hamming_encode(data):
    """SEC-DED Hamming code: data bits -> codeword list, index 0 is the overall parity bit."""
    k = len(data)
    r = 1
    while 2**r < k + r + 1:
        r += 1
    n = k + r
    code = [0] * (n + 1)                 # positions 1..n; code[0] = overall parity
    it = iter(data)
    for pos in range(1, n + 1):
        if pos & (pos - 1):              # not a power of two: data bit
            code[pos] = next(it)
    for i in range(r):
        p = 1 << i
        code[p] = sum(code[pos] for pos in range(1, n + 1) if pos & p) % 2
    code[0] = sum(code[1:]) % 2
    return code

def hamming_check(code):
    """Return (syndrome, overall parity): (0,0) ok, (s,1) single error at s, (s!=0,0) double error."""
    s = 0
    for pos in range(1, len(code)):
        if code[pos]:
            s ^= pos
    return s, sum(code) % 2

c = hamming_encode([1, 0, 1, 1])
print(c[1:], c[0])                       # [0, 1, 1, 0, 0, 1, 1] 0
c[5] ^= 1
print(hamming_check(c))                  # (5, 1): flip bit 5 to correct
c[5] ^= 1; c[2] ^= 1; c[6] ^= 1
print(hamming_check(c))                  # (4, 0): double error, uncorrectable
```

### 4.4.4. Cyclic Redundancy Checks

**Parity codes** and Hamming codes are computed in parallel on whole words and suit buses and memories; in serial transmission (networks, serial ports, disk sectors), data arrives one bit at a time and errors often occur in bursts. A cyclic redundancy check generates its check bits by **polynomial** division, and the hardware needs only a **shift register** and a few XOR gates to compute the check value as the data flows through bit by bit.

Regard a $k$-bit binary string $m_{k-1}\cdots m_1m_0$ as a polynomial $M(x) = \sum_i m_i x^i$ with coefficients in the binary **finite field** $\mathbb{F}_2$. In $\mathbb{F}_2$ both addition and subtraction are XOR, with no carries or borrows; this is called modulo-2 arithmetic.

**Definition 4.4.5 (Cyclic Redundancy Check)** Fix a polynomial $G(x)$ of degree $r$, called the **generator polynomial**. For $k$ data bits $M(x)$, let $R(x)$ be the remainder (of degree less than $r$) of dividing $x^r M(x)$ by $G(x)$, and transmit the $(k + r)$-bit code

$$
T(x) = x^r M(x) + R(x) ,
$$
that is, append the $r$-bit $R(x)$ to the data. This error-detecting code is called a **cyclic redundancy check** (CRC), and $R(x)$ is called the CRC check value. The receiver divides the received code by $G(x)$ and decides that an error occurred if the remainder is not $0$.

Since $R(x) = -R(x)$ in $\mathbb{F}_2$, we have $T(x) = x^rM(x) - R(x) = Q(x)G(x)$, so a correct code is always divisible by $G(x)$. The division here is **division with remainder** of polynomials over $\mathbb{F}_2$, carried out like ordinary long division except that every subtraction is replaced by XOR.

**Example 4.4.2** Let the data be $M = 1101011011$ ($k = 10$) and the generator polynomial $G(x) = x^4 + x + 1$, that is, `10011` ($r = 4$). Append $4$ zeros to the data, and step by step XOR `10011` into the current leading $1$:

```text
11010110110000
10011
01001110110000
 10011
00000010110000
      10011
00000000101000
        10011
00000000001110
```

The remainder is $R = 1110$, so we send `1101011011 1110`. The receiver divides `11010110111110` by `10011` and gets remainder `0000`. If some bits flip in transmission, let the error polynomial be $E(x)$; what is received is $T(x) + E(x)$, and the remainder is $E(x) \bmod G(x)$; an error goes undetected if and only if $G(x) \mid E(x)$.

**Theorem 4.4.3 (Error-Detecting Capability of CRC)** Let the generator polynomial $G(x)$ have degree $r \ge 1$ and constant term $1$.

1. All one-bit errors are detected;
2. if $(x+1) \mid G(x)$, all errors in an odd number of bits are detected;
3. all burst errors of length at most $r$ (in which the erroneous bits all fall within $r$ consecutive positions) are detected.

**Proof** (1) For a one-bit error, $E(x) = x^i$. The constant term of $G(x)$ is $1$, so $G(x)$ is coprime to $x$, and its degree is at least $1$, hence it does not divide $x^i$. (2) If $E(x)$ has an odd number of terms, then $E(1) = 1$; but if $G \mid E$, then $(x+1) \mid G$ gives $E(1) = 0$, a contradiction. (3) A burst error of length $b \le r$ can be written $E(x) = x^i B(x)$, where $B(x)$ has degree $b - 1 < r$ and constant term $1$. If $G \mid E$, then since $G$ is coprime to $x^i$ we get $G \mid B$; but $B \ne 0$ and its degree is less than that of $G$, a contradiction. $\square$

A carefully chosen generator polynomial can also detect all two-bit errors (as long as the code length does not exceed a certain bound) and the great majority of longer burst errors: the fraction of undetected burst errors of length $r+1$ is $2^{-(r-1)}$, and that of longer burst errors is $2^{-r}$. Commonly used generator polynomials include CRC-16-CCITT ($x^{16}+x^{12}+x^5+1$, used in HDLC and Bluetooth), CRC-32 (IEEE 802.3, used for the Ethernet frame check sequence, ZIP, and PNG), and CRC-32C (Castagnoli, used for iSCSI and for ext4 and Btrfs metadata).

CRC hardware is a linear feedback shift register: $r$ **flip-flops** are chained into a shift register, XOR gates are inserted at the positions where the coefficient of $G(x)$ is $1$, and the output of the top bit is fed back to these positions; each input bit and clock tick performs one step of the long division, and after all the data has been shifted in, the register holds the remainder. Software implementations usually use a byte-wise table lookup, or can use dedicated processor instructions: x86 SSE4.2 has a `crc32` instruction that computes CRC-32C, and the Zbc extension of RISC-V provides the carry-less multiplications `clmul`, `clmulh`, and `clmulr` for fast CRC computation and polynomial multiplication over $\mathbb{F}_2$.

The following program computes Example 4.4.2 by long division and implements the CRC-32 used by Ethernet bit by bit, comparing it with the result of the Python standard library. The real CRC-32 also specifies that the register starts as all $1$s, that the result is complemented, and that the low bit within each byte is transmitted first (hence the bit-reversed generator polynomial `0xEDB88320`):

```python
import zlib

def crc_remainder(data: str, gen: str) -> str:
    """Remainder of data(x) * x^r modulo gen(x) over GF(2); bit strings, MSB first."""
    r = len(gen) - 1
    bits = [int(b) for b in data] + [0] * r
    g = [int(b) for b in gen]
    for i in range(len(data)):
        if bits[i]:                      # leading term present: subtract (XOR) gen(x)
            for j, gj in enumerate(g):
                bits[i + j] ^= gj
    return "".join(map(str, bits[-r:]))

print(crc_remainder("1101011011", "10011"))   # 1110

def crc32(message: bytes) -> int:
    """Bitwise CRC-32 (IEEE 802.3), reflected form, as used by Ethernet, zip and PNG."""
    crc = 0xFFFFFFFF
    for byte in message:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ (0xEDB88320 if crc & 1 else 0)
    return crc ^ 0xFFFFFFFF

msg = b"123456789"
print(hex(crc32(msg)), hex(zlib.crc32(msg)))  # both 0xcbf43926
```

A CRC only detects errors and does not correct them: after an error is found, a higher-level protocol discards the frame and retransmits it.

### 4.4.5. Erasure Codes and Stronger Codes

What is common in storage systems is not isolated bit flips but the loss of whole blocks of data (a failed disk, a node going offline), where the positions of the lost blocks are known.

**Definition 4.4.6 (Erasure Code)** An encoding that turns $k$ data blocks into $n > k$ blocks, so that the original data can be recovered whenever at most $n - k$ blocks at known positions are lost, is called an **erasure code**.

The simplest erasure code is the XOR parity of RAID 5: the parity block is the bitwise XOR of the data blocks, and when any one block is lost, XOR-ing the remaining blocks recovers it. RAID 6 and distributed storage (such as erasure-coded storage in HDFS and Ceph) use Reed–Solomon codes based on finite-field arithmetic, which tolerate the simultaneous loss of several blocks at a storage overhead far lower than multiple replicas. At the bit level, modern devices also use codes stronger than Hamming codes: DDR5 memory chips integrate on-die ECC, server memory uses the Chipkill technique, which corrects errors at the granularity of a chip, and solid-state drives and 5G communication use BCH codes and LDPC codes.

## Summary

| Topic | Key points |
|---|---|
| Characters | ASCII 7 bits; Unicode code points U+0000–U+10FFFF; UTF-8 variable length 1–4 bytes, ASCII-compatible, self-synchronizing |
| Integers | unsigned $[0, 2^n-1]$; two's complement $[-2^{n-1}, 2^{n-1}-1]$, addition and subtraction unified as addition modulo $2^n$, $-x = {\sim}x + 1$; **sign-magnitude representation** and ones' complement have two zeros |
| Extension and **endianness** | sign extension for signed numbers, zero extension for unsigned numbers; RISC-V immediates are always sign-extended; RISC-V is **little-endian** |
| Floating point | **IEEE 754**: sign + biased exponent + sign-magnitude mantissa (**hidden bit**); **subnormal numbers**, $\pm\infty$, NaN; default round to nearest, ties to even |
| Low-precision formats | TF32, FP16, **BF16**, FP8 (E4M3, E5M2), FP4; block scaling (MX formats) and tapered precision |
| **Minimum distance** | detects $d-1$-bit errors, corrects $\lfloor (d-1)/2\rfloor$-bit errors |
| **Parity code** | code distance 2, detects odd-bit errors, implemented by an XOR tree |
| Hamming code | $2^r \ge k + r + 1$; check bits at power-of-two positions; the syndrome $S$ gives the error position directly; adding an overall check bit gives SECDED (code distance 4, $72$-bit ECC memory) |
| CRC | $T(x) = x^rM(x) + R(x)$ is divisible by $G(x)$; detects all one-bit errors and burst errors of length $\le r$; implemented by a linear feedback **shift register**, suited to serial transmission |
| Erasure codes | recover blocks lost at known positions; RAID 5 XOR parity, Reed–Solomon |
