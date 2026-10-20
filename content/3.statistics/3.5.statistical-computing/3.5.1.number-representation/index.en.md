---
title: Computer Representation of Numbers
description: How computers store numbers (bits, bytes and words, fixed-point and IEEE 754 floating-point formats, normalized and subnormal numbers, machine epsilon), why floating-point arithmetic differs from real arithmetic (rounding errors, cancellation, absorption), and how the accuracy of a computed result depends on the stability of the algorithm and the conditioning of the problem.
---

Why does R say that $0.58-0.08$ is smaller than $0.5$? A computer has only finitely many bits, so it can represent only finitely many numbers, and almost every real number, and almost every result of an arithmetic operation, has to be rounded. This chapter explains what is stored and what is lost. It first fixes the vocabulary of digital data (bits, bytes, words), then describes the two models of numbers used by hardware: fixed-point numbers for integers and floating-point numbers, standardized by IEEE 754, for real numbers. The second half studies the consequences: the size of rounding errors, how they propagate through the four arithmetic operations, and the two questions that every numerical computation raises: is the algorithm stable, and is the problem well-conditioned? The tools introduced here (machine epsilon, backward stability, condition numbers) are used throughout the course: in the matrix computations of [3.5.3](/3.5.3), the iterative methods of [3.5.4](/3.5.4) and [3.5.5](/3.5.5), and the simulation methods of the later chapters. Matrix norms, singular values and the **condition number** of a matrix were introduced in linear algebra ([2.1.7](/2.1.7)); here they reappear as measures of sensitivity.

## 1.1. Statistical Computing and Digital Data

### 1.1.1. Statistical Computing

**Definition 1.1.1 (Statistical Computing)** **Statistical computing** (also called computational statistics) is the combination of statistical methods with computer-based calculation. It has two aspects: turning statistical methods into reliable and efficient algorithms and implementing them in programs, and developing new statistical methods that rely on the processing power of modern computers.

Examples of the first aspect are the numerical algorithms for **maximum likelihood estimation** ([3.5.4](/3.5.4)–[3.5.6](/3.5.6)); examples of the second are simulation methods for Bayesian models ([3.5.9](/3.5.9)) and **bootstrap** confidence intervals ([3.5.7](/3.5.7)).

Statistical applications store, manipulate and present data, and a statistician must be aware of what the machine does with numbers. The following are all real outcomes of computer arithmetic:

- the product of two positive integers can be negative;
- the input $1.41421356$ can come back as $1.41421354$ (when it is stored in single precision);
- $1+0.00000001=1$ (in single precision; in double precision the same happens to $1+10^{-16}$).

Knowing how computers store and manipulate numbers allows us to anticipate and correct such problems before a program produces meaningless results.

### 1.1.2. Bits, Bytes and Words

Computers are digital: data of every form (numbers, text, images) are represented by groups of the two states of an electronic switch, written $0$ and $1$.

**Definition 1.1.2 (Bit, Byte, Word)** A **bit** (binary digit) is a single binary digit, $0$ or $1$; it is the smallest unit of information. A **byte** is a sequence of $8$ bits, $00000000,00000001,\dots,11111111$, so it takes $2^8=256$ values. A **word** (storage unit) is the fixed-length sequence of $N$ bits that a processor handles as a unit, with $N=16$, $32$ or $64$ depending on the computer.

The byte is the smallest addressable unit of memory; the word is the largest chunk of bits that the processor can process at a time, which is why one speaks of 32-bit and 64-bit machines.

A byte is associated with a character according to a fixed coding rule, a *character encoding*. *ASCII* (American Standard Code for Information Interchange) encodes $128$ characters (English letters, digits, punctuation, control characters) in $7$ bits. *Unicode* is a universal character set that assigns a code point to every character of every writing system; it is stored with variable-length encodings: *UTF-8* (one to four bytes per character, compatible with ASCII, and by far the most widely used encoding on the web), *UTF-16* (used internally by Java and Windows), and the Chinese national standard *GB18030*, which also covers all of Unicode.

Memory capacity is counted in powers of $2$ (binary prefixes, IEC 80000-13):

| Unit | Bytes | Approximately |
|---|---|---|
| $1$ kibibyte (KiB) | $2^{10}=1024$ | $10^3$ |
| $1$ mebibyte (MiB) | $2^{20}=1\,048\,576$ | $10^6$ |
| $1$ gibibyte (GiB) | $2^{30}=1\,073\,741\,824$ | $10^9$ |
| $1$ tebibyte (TiB) | $2^{40}=1\,099\,511\,627\,776$ | $10^{12}$ |

The decimal prefixes kB, MB, GB, TB mean $10^3,10^6,10^9,10^{12}$ bytes, but operating systems often display binary units under the decimal names. A disk sold as $500$ GB holds $500\times10^9$ bytes, which is $500\times10^9/2^{30}\approx465.7$ GiB, displayed as "465 GB".

## 1.2. Fixed-Point and Floating-Point Numbers

### 1.2.1. Fixed-Point Numbers

Mathematics offers two models of numbers, the ring of **integers** and the field of real numbers, and computers simulate them with two models: fixed-point and floating-point numbers. For a digital representation two properties matter most: the *magnitude* (the largest and smallest numbers that can be represented) and the *precision* (the size of the gaps between representable numbers).

A *fixed-point number* represents a relatively small integer (or, more generally, a number with a fixed number of digits after the point) directly in binary. With $k$ bits in a storage unit and one bit kept for the sign ($0$ for $+$, $1$ for $-$), the remaining $k-1$ bits hold the binary digits of $|n|$:

| Sign $\pm$ | Binary number |
|---|---|
| $1$ bit | $k-1$ bits |

With $k=4$, the patterns $0000,0001,\dots,0111$ represent $0,1,\dots,7$; this *sign-magnitude* format represents the integers from $-(2^{k-1}-1)$ to $2^{k-1}-1$. Actual hardware stores signed integers in *two's complement*: the leading bit has weight $-2^{k-1}$ instead of a sign, the range becomes $-2^{k-1},\dots,2^{k-1}-1$, and addition needs no special treatment of signs. R's integers are 32-bit two's complement numbers, with the largest value `.Machine$integer.max` $=2^{31}-1=2147483647$.

Many digital signal processors, to lower the cost of the implementation, perform arithmetic only on integers. Fractions can still be handled by rounding, or by an *implied binary point*: a fixed number of the bits is interpreted as the fractional part, so that in an $8$-bit field with $4$ fractional bits the bits have weights $-2^3$ (sign bit, two's complement), $2^2,2^1,2^0$ and $2^{-1},2^{-2},2^{-3},2^{-4}$. Every bit spent on the fraction is lost to the integer part.

**Definition 1.2.1 (Overflow)** An operation is said to **overflow** if its exact result needs more bits than the storage unit has, so that, if additional higher-order bits were available, they would be nonzero, or the sign bit would be interpreted as a regular numeric bit.

In a fixed-point format the addition of two large positive integers can therefore produce a negative integer, because the carry overflows into the sign bit: $(+)\times(+)=(-)$ and $(+)+(+)=(-)$ are possible. R does not wrap around; it returns `NA` with a warning:

```r
.Machine$integer.max + 1L
```

```text
[1] NA
Warning message:
In .Machine$integer.max + 1L : NAs produced by integer overflow
```

The fundamental limitation of fixed-point numbers is that their gaps are fixed: with a fixed position of the point, the same system cannot represent both a very small number such as $0.0000000000009$ and a very large one such as $9000000000000$. Neither large nor small numbers are available at the same time.

### 1.2.2. Floating-Point Numbers

The solution is the scientific notation: $-0.9876\times10^{-3}$ consists of the sign of the mantissa, the mantissa $0.9876$ (whose length fixes the number of significant digits), the base $10$ and the signed exponent $-3$, which "floats" the point to the right position. Floating-point arithmetic is the hardware analogue of this notation.

**Definition 1.2.2 (Floating-Point Number)** Let $b\ge2$ be an integer (the *radix*) and $p\ge1$ (the *precision*). A **floating-point number** is a number of the form

$$
\pm0.d_1d_2\dots d_p\times b^{e},
$$
where the digits $d_i$ are integers with $0\le d_i<b$, the significand has at most $p$ digits, and the integer exponent $e$ lies in a range $[e_{\min},e_{\max}]$. The number is **normalized** if its leading digit is nonzero, $d_1\ne0$.

For $b=2$ the leading digit of a normalized number is necessarily $1$, so it does not need to be stored; this saved bit is called the *hidden bit*. Moving the point one place, a normalized binary floating-point number is written

$$
\pm1.d_1d_2\dots d_{p-1}\times2^{e}=\pm\bigl(1+d_12^{-1}+\cdots+d_{p-1}2^{-(p-1)}\bigr)\times2^{e},\qquad d_i\in\{0,1\},
$$
with $p-1$ stored fraction bits and precision $p$.

### 1.2.3. The IEEE 754 Standard and Single Precision

The *IEEE 754* standard (ANSI/IEEE Std 754, established in 1985 by the Institute of Electrical and Electronics Engineers, revised in 2008 and 2019) is implemented by essentially all hardware floating-point units; the first integrated circuit to implement a draft of it was the Intel 8087 coprocessor (1980). It defines arithmetic formats, interchange formats, rounding rules, operations and exception handling. The two basic formats are *single precision* (32 bits) and *double precision* (64 bits).

A single-precision word is divided into $1$ sign bit $S$, $8$ exponent bits $E$ and $23$ fraction bits $M$ (the mantissa without the hidden bit), with $b=2$ and $p=24$. The stored exponent $E\in[0,2^8-1]=[0,255]$ is a nonnegative integer; to represent negative exponents it is shifted by a fixed *exponent bias* (offset), $127$ in single precision. A normalized number has the value

$$
v=(-1)^S\times m\times2^{e}=(-1)^S\times1.M\times2^{E-127},\qquad m=1.d_1d_2\dots d_{23}=1+d_12^{-1}+d_22^{-2}+\cdots+d_{23}2^{-23},
$$
so the significand satisfies $m\in[1,2-2^{-23}]$.

The two extreme values of $E$ are reserved for special meanings, which reduces the exponent range of normalized numbers slightly to $e=E-127\in[-126,127]$:

| | $E=0$ | $0<E<255$ | $E=255$ |
|---|---|---|---|
| $M=0$ | $\pm0$ | powers of $2$ | $\pm\infty$ |
| $M\ne0$ | subnormal numbers, $\pm0.M\times2^{-126}$ | ordinary normalized numbers | NaN |

Hence the largest normalized single-precision number is $(2-2^{-23})\times2^{127}\approx3.4\times10^{38}$ and the smallest positive one is $2^{-126}\approx1.18\times10^{-38}$. An operation whose result exceeds the largest number in magnitude overflows and returns $\pm\infty$. Operations with infinity are defined as limits, for instance $4-\infty=\lim_{x\to\infty}(4-x)=-\infty$; $x/\pm\infty=0$ for every finite $x$ and $x/0=\pm\infty$ for every nonzero $x$. *NaN* (not a number) is returned when an operation has no well-defined finite or infinite result, such as $\infty-\infty$, $\infty/\infty$, $0/0$ or $\sqrt{-1}$, and every operation involving a NaN returns NaN.

**Example 1.2.1** Two single-precision bit patterns, with $S$, $E$, $M$ separated by spaces:

- `0 00000111 11000000000000000000000`: $E=2^0+2^1+2^2=7$ and $M=2^{-1}+2^{-2}=0.75$, so the value is $+1.75\times2^{7-127}\approx1.316554\times10^{-36}$;
- `1 10000001 01100000000000000000000`: $E=2^0+2^7=129$ and $M=2^{-2}+2^{-3}=0.375$, so the value is $-1.375\times2^{129-127}=-5.5$.

Normalized numbers leave a gap between $0$ and $2^{e_{\min}}$, while just above $2^{e_{\min}}$ they are spaced $2^{e_{\min}-23}$ apart. IEEE 754 fills this gap by allowing a significand without the hidden bit when the exponent field is $E=0$: the leading $1$ becomes $0$, $1.M\times2^{e_{\min}}\Rightarrow0.M\times2^{e_{\min}}$.

**Definition 1.2.3 (Subnormal Number)** A floating-point number with exponent field $E=0$ and fraction $M\ne0$ is called a **subnormal number** (or denormalized number); its value is $\pm0.M\times2^{e_{\min}}$, with $e_{\min}=-126$ in single precision. When a subnormal number is the result of an arithmetic operation, one speaks of *gradual underflow* (graceful underflow); an **underflow** in general is a nonzero result smaller in magnitude than the smallest normalized number.

Subnormal numbers are equally spaced in $[0,2^{e_{\min}}]$, with the same gap $2^{e_{\min}-23}$ as the normalized numbers in $[2^{e_{\min}},2^{e_{\min}+1})$, so the number line has no hole at $0$. They have fewer significant bits than normalized numbers, so their relative precision deteriorates as they approach $0$.

| $S$ | $E$ | $M$ | Value |
|---|---|---|---|
| 0 | 0000 0000 | 000…000 | $0$ |
| 1 | 0000 0000 | 000…000 | $-0$ |
| 0 | 1111 1111 | 000…000 | $\infty$ |
| 1 | 1111 1111 | 000…000 | $-\infty$ |
| 0 or 1 | 1111 1111 | nonzero | NaN |
| 0 | 0000 0000 | 000…001 | $2^{-126}\times2^{-23}=2^{-149}\approx1.4\times10^{-45}$ |
| 0 | 0000 0000 | 100…000 | $2^{-126}\times2^{-1}=2^{-127}\approx5.9\times10^{-39}$ |
| 0 | 0000 0001 | 000…000 | $2^{1-127}\times1=2^{-126}\approx1.2\times10^{-38}$ |
| 0 | 1000 0000 | 000…000 | $2^{128-127}\times1=2$ |
| 0 | 1000 0001 | 101…000 | $2^{129-127}\times(1+0.5+0.125)=6.5$ |
| 1 | 1000 0001 | 101…000 | $-2^{129-127}\times(1+0.5+0.125)=-6.5$ |

**Example 1.2.2 (Largest Subnormal Number)** Suppose an IEEE-style format has $k$ exponent bits and $n$ fraction bits. Then the bias is $2^{k-1}-1$ and $e_{\min}=1-(2^{k-1}-1)=2-2^{k-1}$. The largest subnormal number has all fraction bits equal to $1$:

$$
0.\underbrace{11\dots1}_{n}\times2^{e_{\min}}=(1-2^{-n})\times2^{2-2^{k-1}},
$$
and the smallest positive subnormal number is $2^{-n}\times2^{2-2^{k-1}}$. For single precision ($k=8$, $n=23$) these are $(1-2^{-23})\times2^{-126}\approx1.18\times10^{-38}$, just below the smallest normalized number $2^{-126}$, and $2^{-149}$.

![Top: all nonnegative numbers of a toy binary system with precision p = 3 and exponents -1 to 2; the normalized numbers are equally spaced between consecutive powers of 2 and the gap doubles at each power, while the subnormal numbers fill the interval between 0 and 2^-1 with the smallest gap. Bottom: in IEEE double precision the gap to the next number, divided by x, oscillates between 2^-53 and 2^-52](./plots/float-number-line.py)

The figure shows the key feature of floating-point numbers: the absolute gaps scale with the size of the numbers, while the relative gaps stay within a factor of $2$. If $x=1.M\times2^{e}$ is a normalized single-precision number, the next number is $x+2^{e-23}$, and the ratio of the gap to $x$ is $2^{-23}/1.M\in(2^{-24},2^{-23}]$. In particular, every integer $n$ with $|n|\le2^{24}=16\,777\,216$ is exactly representable in single precision, so such integers are added, subtracted and multiplied without rounding error as long as the results stay in this range; above about $\pm16.8$ million the gaps exceed $1$ and some integers are missed.

### 1.2.4. Conversion Between Decimal and Binary

To convert a binary number $d_k\dots d_2d_1.f_1f_2\dots f_m$ to decimal, treat the integral and fractional parts separately:

$$
D_1=\sum_{i=1}^{k}d_i\times2^{i-1},\qquad D_2=\sum_{i=1}^{m}f_i\times2^{-i}.
$$
To convert a decimal number to binary, again separate the two parts:

- for the integral part, divide by the target radix $2$ repeatedly and collect the remainders in reverse order;
- for the fractional part, multiply by $2$ repeatedly and collect the integral parts in order.

**Example 1.2.3** Convert $18.6875$ to binary. Integral part: $18/2=9$ remainder $0$; $9/2=4$ remainder $1$; $4/2=2$ remainder $0$; $2/2=1$ remainder $0$; $1/2=0$ remainder $1$ (stop when the quotient is $0$). Reading the remainders upward gives $18=10010_2$. Fractional part: $0.6875\times2=1.375$ (digit $1$), $0.375\times2=0.75$ (digit $0$), $0.75\times2=1.5$ (digit $1$), $0.5\times2=1.0$ (digit $1$, stop). Hence $0.6875=0.1011_2$ and

$$
18.6875=10010.1011_2=1.00101011_2\times2^{4}.
$$
In single precision this is stored as `0 10000011 00101011000000000000000` ($E=4+127=131$).

Two further cases. A negative number differs only in the sign bit: $-5=-101_2=-1.01_2\times2^2$ is stored as `1 10000001 01000000000000000000000`. A fraction such as $1/5=0.2$ never terminates: $0.2\times2=0.4$ (digit $0$), $0.4\times2=0.8$ ($0$), $0.8\times2=1.6$ ($1$), $0.6\times2=1.2$ ($1$), $0.2\times2=0.4$, and the pattern repeats, so $0.2=0.\overline{0011}_2$. A decimal fraction is a finite binary fraction only if its denominator in lowest terms is a power of $2$; numbers like $0.1$, $0.2$ and $0.58$ cannot be stored exactly and must be rounded.

### 1.2.5. Double Precision and Numbers in R

Double precision simply adds more bits to both the exponent and the fraction: $1$ sign bit, $11$ exponent bits (bias $1023$) and $52$ fraction bits.

| | Single precision | Double precision |
|---|---|---|
| Significand size $p$ | $24$ bits | $53$ bits |
| Exponent size | $8$ bits | $11$ bits |
| Total size | $32$ bits | $64$ bits |
| Exponent bias | $127$ | $1023$ |
| $e_{\max}$ | $+127$ | $+1023$ |
| $e_{\min}$ | $-126$ | $-1022$ |
| Smallest normalized number | $2^{-126}\approx1.2\times10^{-38}$ | $2^{-1022}\approx2.2\times10^{-308}$ |
| Largest normalized number | $(2-2^{-23})\,2^{127}\approx3.4\times10^{38}$ | $(2-2^{-52})\,2^{1023}\approx1.8\times10^{308}$ |
| Machine epsilon $\varepsilon_{\mathrm{mach}}$ | $2^{-23}\approx1.2\times10^{-7}$ | $2^{-52}\approx2.2\times10^{-16}$ |

**Definition 1.2.4 (Machine Epsilon)** The **machine epsilon** $\varepsilon_{\mathrm{mach}}$ of a floating-point format is the distance from $1$ to the next larger floating-point number: $\varepsilon_{\mathrm{mach}}=2^{1-p}$, that is, $2^{-23}$ in single and $2^{-52}$ in double precision. Half of it, $u=\varepsilon_{\mathrm{mach}}/2=2^{-p}$, is called the **unit roundoff**.

Machine epsilon is often described as the smallest number $\varepsilon$ with $1+\varepsilon>1$ in floating-point arithmetic. Under rounding to nearest this is only approximately true: $1+2^{-53}$ lies exactly halfway between $1$ and $1+2^{-52}$ and is rounded to $1$ (ties go to the number with an even last bit), while any number slightly larger than $2^{-53}$ added to $1$ gives $1+2^{-52}$. R stores $\varepsilon_{\mathrm{mach}}$ in `.Machine$double.eps`:

```r
2^1024                       # overflow
log(2^1023, base = 10)
1 + 2^(-53) > 1
1 + 2^(-52) > 1
log(.Machine$double.eps, base = 2)
```

```text
[1] Inf
[1] 307.9537
[1] FALSE
[1] TRUE
[1] -52
```

**Remark 1.2.1** The literature uses two conventions for the symbol $\varepsilon_{\mathrm{machine}}$: the gap $2^{1-p}$ (as in R and MATLAB) and the bound $2^{-p}$ on the relative rounding error (as in Trefethen and Bau). This page writes $\varepsilon_{\mathrm{mach}}=2^{-52}$ for the gap and $u=2^{-53}$ for the bound of Theorem 1.3.1; since they differ by a factor of $2$, statements of the form $O(\varepsilon_{\mathrm{mach}})$ do not depend on the convention.

R has no single-precision data type: all real numbers are stored in double precision. The functions `as.single` and `single` are identical to `as.double` and `double` except that they set the attribute `Csingle`, which is used only in the `.C` and `.Fortran` interfaces to compiled code. It is a historical anomaly that R has two names for its floating-point vectors, *double* and *numeric* (and formerly had *real*): `mode()` reports the broad classes logical, numeric, complex and character, while `typeof()` distinguishes the storage types integer and double. Integers are written with the suffix `L`.

```r
x <- 1.2
mode(x); typeof(x)
x <- 1L
mode(x); typeof(x)
```

```text
[1] "numeric"
[1] "double"
[1] "numeric"
[1] "integer"
```

**Example 1.2.4 (Why $0.58-0.08<0.5$)** A problem from a previous exam: explain the following output.

```r
a <- 0.58; b <- 0.08
(a - b) >= 0.5
a - b <= 0.5
tol <- 1e-5
(a - b) >= (0.5 - tol)
```

```text
[1] FALSE
[1] TRUE
[1] TRUE
```

Neither $0.58$ nor $0.08$ has a finite binary expansion, so both are rounded when they are stored. In double precision the $52$ fraction bits kept are

$$
\begin{aligned}
\operatorname{fl}(0.58)&=2^{-1}\times1.0010100011110101110000101000111101011100001010001111_2\quad\text{(rounded down)},\\
\operatorname{fl}(0.08)&=2^{-4}\times1.0100011110101110000101000111101011100001010001111011_2\quad\text{(rounded up)},
\end{aligned}
$$
(in single precision they would be `0 01111110 00101000111101011100001` and `0 01111011 01000111101011100001010`). The values actually stored are

$$
\operatorname{fl}(0.58)=0.57999999999999996003\ldots,\qquad\operatorname{fl}(0.08)=0.08000000000000000166\ldots,
$$
and the computed difference is the double $0.49999999999999994449\ldots$, one gap below $0.5$. R prints numbers with $7$ significant digits by default, which hides the error; more digits reveal it:

```r
print(0.58, digits = 17)
print(0.58 - 0.08, digits = 17)
sprintf("%.20f", 0.08)
```

```text
[1] 0.57999999999999996
[1] 0.49999999999999994
[1] "0.08000000000000000167"
```

The lesson is never to test floating-point numbers for exact equality with `==`. Compare them with a tolerance instead, either explicitly, as `abs(x - y) < tol`, or with `all.equal`, which tests "near equality" with a default relative tolerance of $1.5\times10^{-8}$ and returns `TRUE` or a description of the difference (wrap it in `isTRUE()` inside `if` conditions):

```r
(a - b) == 0.5
all.equal(a - b, 0.5)
isTRUE(all.equal(a - b, 0.5))
```

```text
[1] FALSE
[1] TRUE
[1] TRUE
```

## 1.3. Rounding Errors and Floating-Point Arithmetic

### 1.3.1. Rounding Errors

A finite number of bits can represent only a finite subset of the real numbers. This causes two difficulties: the magnitude of the representable numbers is bounded (they cannot be arbitrarily large or small), and their precision is limited (there must be gaps between them). From now on we consider numbers in the normalized range, where the gaps scale with the size of the numbers.

**Definition 1.3.1 (Rounding Error)** Let $r$ be a real number and $v$ its floating-point representation, called the *computer number* of $r$. The **rounding error** (round-off error) of $r$ is $\varepsilon=|r-v|$, and its *relative rounding error* is $|r-v|/|r|$.

Every real number $r\ne0$ has a binary expansion $r=\pm\sum_{k=-\infty}^{N_r}\alpha_k2^k$ with $\alpha_k\in\{0,1\}$ and $\alpha_{N_r}=1$, where the integer $N_r$ depends on $r$; it is unique if expansions ending in infinitely many $1$s are excluded. If $2^{-1022}\le|r|<2^{1024}$ (approximately $2.2\times10^{-308}\le|r|<1.8\times10^{308}$), this can be written as

$$
r=(-1)^S\times1.M^*\times2^{E-1023},\qquad M^*=\alpha_{-1}2^{-1}+\alpha_{-2}2^{-2}+\cdots,
$$
with an infinite-precision mantissa $M^*$ (the digits renumbered after the leading one). The nearest double to the left, $v_-=(-1)^S\times1.M\times2^{E-1023}$, keeps the first $52$ bits, $M=\alpha_{-1}2^{-1}+\cdots+\alpha_{-52}2^{-52}$; the nearest double to the right has $\tilde M=M+2^{-52}$. Rounding to the nearest of the two gives

$$
\varepsilon=|r-v|=2^{E-1023}\min\bigl(|M^*-M|,\,|M^*-\tilde M|\bigr)\le2^{E-1023}\cdot\frac{2^{-52}}{2}=2^{E-1023}\cdot2^{-53}.
$$
Dividing by $|r|=2^{E-1023}\cdot1.M^*\ge2^{E-1023}$ bounds the relative error.

**Theorem 1.3.1 (Relative Rounding Error)** Let $\operatorname{fl}\colon\mathbb{R}\to F$ map a real number to the nearest element of the set $F$ of double-precision numbers. If $r$ lies in the normalized range, then

$$
\frac{|r-\operatorname{fl}(r)|}{|r|}\le2^{-53}=u.
$$
Equivalently, there is a number $\mu$ with $|\mu|\le u$ such that $\operatorname{fl}(r)=r(1+\mu)$.

The bound $u$ does not depend on $r$ and is a characteristic of the machine; this is why it is used as the unit of accuracy in error analysis (Remark 1.2.1). In words: *the relative error of storing a number is at most half a unit in the last place*, about $16$ significant decimal digits in double precision and $7$ in single precision.

### 1.3.2. Accuracy and Stability

We can regard a computation as a function. Let $X$ and $Y$ be normed vector spaces. A mathematical *problem* is a map $f\colon X\to Y$ from data to solutions, and an algorithm for it is another map $\tilde f\colon X\to Y$, namely what the computer actually computes, rounding errors included. The rounding function $\operatorname{fl}$ itself is the simplest example: $f$ is the identity and $\tilde f=\operatorname{fl}$.

**Definition 1.3.2 (Forward and Backward Error)** Let $y=f(x)$ be the exact solution and $\tilde y=\tilde f(x)$ the computed one. The **forward error** of $\tilde f$ at $x$ is the difference $\Delta y=\tilde y-y=\tilde f(x)-f(x)$. The **backward error** is the smallest perturbation $\Delta x=|\tilde x-x|$ of the data for which the computed result is the exact solution, $f(\tilde x)=\tilde f(x)$.

The forward error asks "how far is the answer from the truth?"; the backward error asks "for what data have we actually solved our problem?"

**Example 1.3.1 (Computing $\sqrt2$)** Let $f(x)=\sqrt x$, and suppose some algorithm gives $\tilde f(2)=1.41$. The forward error is $\Delta y=1.41-\sqrt2\approx-0.004213562$. Since $1.41=\sqrt{1.9881}$, the computed value is the exact square root of $\tilde x=1.41^2$, and the backward error is $\min\{|\tilde x-x|:f(\tilde x)=\tilde f(x)\}=2-1.41^2=0.0119$.

We would be happy if $\Delta y$ were always tiny, but this cannot always be achieved; small backward errors are often the best one can hope for. The following definitions measure errors relative to the size of the data and solutions and compare them with the unit roundoff; $h(t)=O(g(t))$ means that there is a constant $C>0$ with $\|h(t)\|\le Cg(t)$ for all $t$ sufficiently close to the limit under consideration (here $u\to0$, thinking of a sequence of ever more precise machines).

**Definition 1.3.3 (Accuracy, Stability, Backward Stability)** An algorithm $\tilde f$ for a problem $f$ is

1. **accurate** if for each $x\in X$
   $$
   \frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}=O(u);
   $$
2. **stable** if for each $x\in X$
   $$
   \frac{\|\tilde f(x)-f(\tilde x)\|}{\|f(\tilde x)\|}=O(u)\quad\text{for some }\tilde x\text{ with }\frac{\|\tilde x-x\|}{\|x\|}=O(u);
   $$
3. **backward stable** if for each $x\in X$
   $$
   \tilde f(x)=f(\tilde x)\quad\text{for some }\tilde x\text{ with }\frac{\|\tilde x-x\|}{\|x\|}=O(u).
   $$

Accuracy concerns the forward error. A stable algorithm gives nearly the right answer to nearly the right question; a backward stable algorithm, a tightening of stability, gives exactly the right answer to nearly the right question. The relations between the three notions follow directly from the definitions:

- backward stability implies stability (take the same $\tilde x$; the left side of 2 is then $0$);
- accuracy implies stability (take $\tilde x=x$);
- neither stability nor backward stability implies accuracy: whether a backward stable algorithm is accurate depends on the problem, through its condition number (Theorem 1.4.1 and Example 1.4.1).

### 1.3.3. Floating-Point Arithmetic

Every operation of a computer is followed by a rounding. IEEE 754 requires that the four basic operations, and the square root, be *correctly rounded*: the computed result is the exact result rounded to the nearest floating-point number. Write $\oplus,\ominus,\otimes,\oslash$ for the floating-point versions of $+,-,\times,\div$, and $\circledast$ for any of them. Theorem 1.3.1 then gives:

**Theorem 1.3.2 (Fundamental Axiom of Floating-Point Arithmetic)** For all $x,y\in F$ (as long as the exact result $x*y$ lies in the normalized range), there is a $\mu$ with $|\mu|\le u$ such that

$$
x\circledast y=\operatorname{fl}(x*y)=(x*y)(1+\mu).
$$

Each single operation is thus accurate. The danger lies in chains of operations, whose inputs already carry errors.

**Example 1.3.2 (Multiplication Is Accurate and Backward Stable)** Let $x,y\in\mathbb{R}$. Storing and multiplying them gives

$$
\operatorname{fl}(x)=x(1+s)\triangleq X,\qquad\operatorname{fl}(y)=y(1+t)\triangleq Y,\qquad X\otimes Y=XY(1+\mu),
$$
with $\max\{|s|,|t|,|\mu|\}\le u$. The forward error is $XY(1+\mu)-xy=xy(s+t+st)+xy(1+s)(1+t)\mu$, so the relative error

$$
\Bigl|\frac{XY(1+\mu)-xy}{xy}\Bigr|=|s+t+st+(1+s)(1+t)\mu|\le|s|+|t|+|st|+(1+|s|)(1+|t|)|\mu|=O(u):
$$
multiplication is accurate. It is also backward stable: write $1+\mu=(1+\mu_1)(1+\mu_2)$ with $|\mu_1|,|\mu_2|\le u$ (for instance $\mu_1=\mu_2=\sqrt{1+\mu}-1$), and set $\tilde x=x(1+s)(1+\mu_1)$, $\tilde y=y(1+t)(1+\mu_2)$. Then $X\otimes Y=\tilde x\tilde y$ exactly, and the backward error satisfies $\|(x,y)-(\tilde x,\tilde y)\|=O(u)\|(x,y)\|$. The same argument applies to division.

**Example 1.3.3 (Addition)** $\operatorname{fl}(x)\oplus\operatorname{fl}(y)=\bigl(x(1+s)+y(1+t)\bigr)(1+\mu)=x(1+s)(1+\mu)+y(1+t)(1+\mu)$ is the exact sum of $\tilde x=x(1+s)(1+\mu)$ and $\tilde y=y(1+t)(1+\mu)$, both relative perturbations of size $O(u)$: computing $f(x,y)=x+y$ this way is backward stable. Now consider $f(x)=x+1$ computed as $\operatorname{fl}(x)\oplus1=\bigl(x(1+s)+1\bigr)(1+\mu)$. The only $\tilde x$ with $\tilde x+1$ equal to the result is $\tilde x=x(1+s)(1+\mu)+\mu$, and for $x\approx0$ the relative perturbation $|\tilde x-x|/|x|\approx|\mu|/|x|$ is not $O(u)$. The algorithm is not backward stable (it is still stable, since the result is accurate): the constant $1$ is treated as exact data, so the error cannot be thrown back onto it.

Subtraction can lose all accuracy. Let the significand have $m+1$ bits, and take

$$
x=1\cdot2^{q},\qquad y=(1+2^{-1}+\cdots+2^{-m})\cdot2^{q-1},\qquad x-y=2^{q-m-1}.
$$
If the subtraction is performed with only the $m+1$ digits of the format, $y$ must first be shifted to the exponent of $x$, $y=(2^{-1}+\cdots+2^{-m}+2^{-m-1})\cdot2^{q}$, which needs $m+1$ fraction digits; the last one is lost. Chopping gives $y\approx(2^{-1}+\cdots+2^{-m})\cdot2^q$ and the computed difference $2^{q-m}$; rounding gives $y\approx1\cdot2^q$ and the difference $0$. The relative errors are

$$
\Bigl|\frac{2^{q-m}-2^{q-m-1}}{2^{q-m-1}}\Bigr|=1\qquad\text{or}\qquad\Bigl|\frac{0-2^{q-m-1}}{2^{q-m-1}}\Bigr|=1.
$$
The absolute error is as large as the target quantity: no digit of the output is correct. In decimal, with $7$ significant digits, $1.234571\times10^5-1.234567\times10^5=0.000004\times10^5$, which is renormalized to $4.000000\times10^{-1}$: of the seven digits shown, only the first carries information. Such *cancellation* occurs when nearly equal numbers are subtracted, and it is the most common source of loss of significance.

**Definition 1.3.4 (Benign and Catastrophic Cancellation)** Cancellation is **benign cancellation** when the subtracted quantities are known exactly (for example, they are floating-point numbers that are data of the problem), and **catastrophic cancellation** when the operands themselves involve rounding errors from earlier operations.

**Theorem 1.3.3 (Guard Digit)** If the subtraction of two floating-point numbers is carried out with one extra digit, a *guard digit*, before the final rounding, then the relative error of the result is less than $2u$.

IEEE 754 arithmetic, being correctly rounded, behaves even better (relative error at most $u$), so the subtraction of two stored numbers is always accurate. Catastrophic cancellation does not introduce a new error; it exposes the errors already present in the operands.

**Example 1.3.4** Let $b=3.34$, $a=1.22$, $c=2.28$, so that $b^2-4ac=11.1556-11.1264=0.0292$. In decimal arithmetic with three significant digits, $b^2=11.1556\approx11.2$ and $4ac=11.1264\approx11.1$, so the computed discriminant is $0.1$, more than three times too large. The subtraction itself was exact; it only revealed the errors made in the two multiplications. Rounding the products to four digits instead, $11.16-11.13=0.03$, is already close.

To avoid catastrophic cancellation, rewrite formulas so that nearly equal *computed* quantities are not subtracted:

- for $x\approx y$, compute $x^2-y^2$ as $(x+y)(x-y)$: $x-y$ is a benign cancellation of exact data, and the product is accurate, whereas $x^2$ and $y^2$ are rounded before they cancel;
- for the roots of $ax^2+bx+c=0$ with $b>0$ and $b^2\gg4|ac|$, the formula $r_1=(-b+\sqrt{b^2-4ac})/(2a)$ subtracts two nearly equal numbers. Compute instead

$$
r_2=\frac{-b-\sqrt{b^2-4ac}}{2a},\qquad r_1=\frac{c}{ar_2}=\frac{-2c}{b+\sqrt{b^2-4ac}},
$$
which involve only additions of numbers of the same sign (for $b<0$ exchange the roles of the signs); the second formula follows from $r_1r_2=c/a$.

When numbers of very different magnitudes are added or subtracted, the smaller one can be lost, an effect called *absorption*: if $|y|$ is less than half the gap between $x$ and its neighbors, then $x\oplus y=x$. This holds whenever $|y|<\tfrac12u|x|$, and next to $x=1$, whose upper neighbor is $1+2^{-52}$, for every $0<y<u$. In single precision $1+0.00000001=1$; in double precision $10^{-11}$ is still visible next to $1$,

```r
options(digits = 16)
1 + 0.00000000001
1 - 0.00000000001
1 + 1e-16 == 1
```

```text
[1] 1.00000000001
[1] 0.99999999999
[1] TRUE
```

but $10^{-16}<u\approx1.1\times10^{-16}$ is absorbed by $1$. Absorption and cancellation affect addition and subtraction only; multiplication and division have neither problem (Example 1.3.2).

A consequence is that floating-point addition is not associative: in double precision, `(0.1 + 0.2) + 0.3` gives $0.6000000000000001$ while `0.1 + (0.2 + 0.3)` gives $0.6$. The order of summation matters.

**Example 1.3.5 (Order of Summation)** Compare

$$
\mathrm{sum}_{\mathrm{o}}=1+\frac{1}{2^2}+\cdots+\frac{1}{n^2},\qquad\mathrm{sum}_{\mathrm{r}}=\frac{1}{n^2}+\cdots+\frac{1}{2^2}+1.
$$
For $n=10^5$ the exact value is $1.644924066898\ldots$ (close to $\pi^2/6\approx1.644934$, the limit as $n\to\infty$). In single precision the forward sum gives $1.6447253$, with an error of $2.0\times10^{-4}$, while the reversed sum gives $1.6449240$, with an error of $2.2\times10^{-8}$. Adding in increasing order is better: in the forward sum, once the running sum exceeds $1$, every term below half the gap, $2^{-24}\approx6\times10^{-8}$, is absorbed completely (this happens for all $k>4096$), and the rounding error of each addition is proportional to the current partial sum, which stays small for as long as possible when the small terms come first. The same principle helps whenever a quantity is accumulated from one large and many small contributions, as in the numerical integration of trajectories.

## 1.4. Conditioning

### 1.4.1. Well-Conditioned and Ill-Conditioned Problems

Why does backward stability not imply accuracy?

**Example 1.4.1** Consider finding the roots of $x^2-2x+c=0$ as a function of the coefficient $c$,

$$
r(c)=\frac{-b\pm\sqrt{b^2-4ac}}{2a}=1\pm\sqrt{1-c},
$$
and suppose that the algorithm $\tilde r(c)=r\bigl(c(1-\varepsilon)\bigr)$ makes a relative error $\varepsilon=0.0001$ in the coefficient. For $c=1$, $r(1)=1$ (a double root), but $\tilde r(1)=r(0.9999)=1\pm\sqrt{0.0001}=1\pm0.01$. The forward error $0.01$ is a hundred times the relative perturbation $\varepsilon$, so the algorithm is not accurate. Yet for every $c$, $\tilde r=1\pm\sqrt{1-c(1-\varepsilon)}$ is the exact root for the coefficient $\tilde c=-(\tilde r^2-2\tilde r)=c(1-\varepsilon)$, a backward error of $|c-\tilde c|=c\varepsilon$: the algorithm is backward stable. A small perturbation of the coefficients causes a large change of the roots, and this is a property of the problem, not of the algorithm.

Consider a problem as a function $f\colon X\to Y$ from a normed vector space $X$ of data to a normed vector space $Y$ of solutions.

**Definition 1.4.1 (Well- and Ill-Conditioned Problems)** A problem $f$ is **well-conditioned** at $x$ if all small perturbations of $x$ lead to only small changes in $f(x)$, and **ill-conditioned** if some small perturbation of $x$ leads to a large change in $f(x)$.

Conditioning is intrinsic to the problem; stability is a property of an algorithm. No algorithm can repair an ill-conditioned problem, but a bad algorithm can spoil a well-conditioned one. Two classical examples of numerical analysis:

- **Runge phenomenon** ([2.1.9](/2.1.9)): interpolating $1/(1+25x^2)$ on $[-1,1]$ by polynomials at equally spaced nodes, the interpolants of degrees $5$ and $9$ oscillate more and more near the endpoints; interpolation at equally spaced nodes of high degree is ill-conditioned;
- *Wilkinson's polynomial* $p(x)=\prod_{i=1}^{20}(x-i)=\sum_{i=0}^{20}c_ix^i$: perturbing each coefficient $c_i$ by a random relative amount of at most $10^{-10}$ moves several of the roots $10,\dots,20$ far off the real axis, by distances of order $1$; finding the roots of a polynomial from its coefficients is ill-conditioned.

### 1.4.2. Condition Numbers

Let $\delta x$ be a small perturbation of $x$ and $\delta f=f(x+\delta x)-f(x)$.

**Definition 1.4.2 (Condition Numbers)** The **absolute condition number** of the problem $f$ at $x$ is

$$
\hat\kappa=\hat\kappa(x)=\lim_{\varepsilon\to0}\sup_{\|\delta x\|\le\varepsilon}\frac{\|\delta f\|}{\|\delta x\|},
$$
and the **relative condition number** is

$$
\kappa=\kappa(x)=\lim_{\varepsilon\to0}\sup_{\|\delta x\|\le\varepsilon}\frac{\|\delta f\|/\|f(x)\|}{\|\delta x\|/\|x\|}.
$$

With the understanding that $\delta x$ is infinitesimal, one writes simply $\hat\kappa=\sup_{\delta x}\|\delta f\|/\|\delta x\|$ and $\kappa=\sup_{\delta x}\dfrac{\|\delta f\|/\|f(x)\|}{\|\delta x\|/\|x\|}$. If $f$ is differentiable with **Jacobian matrix** $J(x)$, $J_{ij}=\partial f_i/\partial x_j$, then $\delta f\approx J(x)\,\delta x$, and

$$
\hat\kappa(x)=\|J(x)\|,\qquad\kappa(x)=\frac{\|J(x)\|\,\|x\|}{\|f(x)\|},
$$
where $\|J(x)\|$ is the norm of $J(x)$ induced by the norms on $X$ and $Y$ (Definition 1.4.3). A problem with $\kappa$ of moderate size ($1$, $10$, $10^2$) is well-conditioned; with $\kappa=10^6$ or more it is ill-conditioned. Relative condition numbers are the natural ones in floating-point arithmetic, whose errors are relative.

**Example 1.4.2** For the roots of Example 1.4.1, $r(c)=1\pm\sqrt{1-c}$ gives $\hat\kappa(c)=|r'(c)|=\dfrac{1}{2\sqrt{1-c}}$, so $\hat\kappa(1)=\infty$: near a double root the problem is ill-conditioned. Other examples:

- $f(x)=x/2$: $\kappa=\dfrac{|f'(x)|\,|x|}{|f(x)|}=\dfrac{(1/2)|x|}{|x|/2}=1$;
- $f(x)=\sqrt x$ ($x>0$): $\kappa=\dfrac{1}{2\sqrt x}\cdot\dfrac{x}{\sqrt x}=\dfrac12$;
- $f(\boldsymbol{x})=x_1-x_2$ for $\boldsymbol{x}=(x_1,x_2)^{\mathsf T}\in\mathbb{R}^2$ with the $\infty$-norm on the data: $J=(1,-1)$ has induced norm $\|J\|_\infty=2$ (Example 1.4.3), so
  $$
  \kappa=\frac{2\max\{|x_1|,|x_2|\}}{|x_1-x_2|},
  $$
  which is arbitrarily large when $x_1\approx x_2$. This is cancellation seen from the side of the problem: subtracting nearly equal numbers is ill-conditioned, so errors already present in the operands are amplified.

**Theorem 1.4.1 (Backward Stability and Accuracy)** If a backward stable algorithm is used to solve a problem $f$ with condition number $\kappa$, the relative errors satisfy

$$
\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}=O\bigl(\kappa(x)\,u\bigr).
$$

**Proof** By backward stability, $\tilde f(x)=f(\tilde x)$ for some $\tilde x$ with $\|\tilde x-x\|/\|x\|=O(u)$. By the definition of $\kappa(x)$, applied to the perturbation $\delta x=\tilde x-x\to0$,

$$
\frac{\|\tilde f(x)-f(x)\|}{\|f(x)\|}=\frac{\|f(\tilde x)-f(x)\|}{\|f(x)\|}\le\bigl(\kappa(x)+o(1)\bigr)\frac{\|\tilde x-x\|}{\|x\|}=O\bigl(\kappa(x)\,u\bigr).\qquad\square
$$

If the problem is well-conditioned, $\kappa=O(1)$, a backward stable algorithm is therefore accurate. Otherwise the solution may be inaccurate, but it is still the exact solution of a nearby problem, and since the data themselves are usually known only approximately, backward stability is often as good as one can possibly hope for.

### 1.4.3. Norms

A norm measures the size of a vector, a matrix or a tensor. A norm on a vector space $V$ is a function $\|\cdot\|\colon V\to\mathbb{R}$ with

1. nonnegativity: $\|\boldsymbol{x}\|\ge0$;
2. definiteness: $\|\boldsymbol{x}\|=0$ only if $\boldsymbol{x}=\boldsymbol{0}$;
3. the **triangle inequality**: $\|\boldsymbol{x}+\boldsymbol{y}\|\le\|\boldsymbol{x}\|+\|\boldsymbol{y}\|$;
4. homogeneity: $\|\lambda\boldsymbol{x}\|=|\lambda|\,\|\boldsymbol{x}\|$ for $\lambda\in\mathbb{R}$.

The standard norms of a vector $\boldsymbol{x}\in\mathbb{R}^n$ are

| Norm | Definition |
|---|---|
| $\ell^1$ norm (Manhattan norm) | $\Vert\boldsymbol{x}\Vert_1=\sum_{i=1}^n\lvert x_i\rvert$ |
| $\ell^2$ norm (Euclidean norm) | $\Vert\boldsymbol{x}\Vert_2=\bigl(\sum_{i=1}^n\lvert x_i\rvert^2\bigr)^{1/2}$ |
| $\ell^p$ norm, $p\ge1$ | $\Vert\boldsymbol{x}\Vert_p=\bigl(\sum_{i=1}^n\lvert x_i\rvert^p\bigr)^{1/p}$ |
| $\ell^\infty$ norm (maximum norm) | $\Vert\boldsymbol{x}\Vert_\infty=\max_{1\le i\le n}\lvert x_i\rvert$ |

For $0<p<1$ the formula still makes sense, but the triangle inequality fails (the unit ball is not convex), so it is not a norm. The "$\ell^0$ norm" $\|\boldsymbol{x}\|_0=\#\{i:x_i\ne0\}$, the number of nonzero entries, which appears in sparse regression, is not a norm either: it is not homogeneous.

Norms provide vector spaces and their linear operators with measures of size, length and distance. A linear operator is measured by how much it can stretch a vector.

**Definition 1.4.3 (Induced Norm)** Let $X,Y$ be normed spaces and $A\colon X\to Y$ a linear operator. The **induced norm** (operator norm) of $A$ is

$$
\|A\|=\sup_{\boldsymbol{x}\ne\boldsymbol{0}}\frac{\|A\boldsymbol{x}\|_Y}{\|\boldsymbol{x}\|_X}=\sup_{\|\boldsymbol{x}\|_X=1}\|A\boldsymbol{x}\|_Y.
$$

It is the "blow-up factor" of $A$; the identity has $\|I\|=1$; and for finite-dimensional spaces the supremum is attained, so it is a maximum. The induced norm is submultiplicative, since $\|AB\boldsymbol{x}\|\le\|A\|\,\|B\boldsymbol{x}\|\le\|A\|\,\|B\|\,\|\boldsymbol{x}\|$, so it is a **matrix norm**. For an $m\times n$ matrix the norms induced by $\ell^1$, $\ell^\infty$ and $\ell^2$ are the maximum absolute column sum, the maximum absolute row sum and the largest singular value, the **spectral norm** ([2.1.7](/2.1.7)):

$$
\|A\|_1=\max_{1\le j\le n}\sum_{i=1}^m|a_{ij}|,\qquad\|A\|_\infty=\max_{1\le i\le m}\sum_{j=1}^n|a_{ij}|,\qquad\|A\|_2=\sigma_1.
$$

A special case is a linear functional $f\colon\mathbb{R}^n\to\mathbb{R}$. By the **Riesz representation theorem** ([2.1.12](/2.1.12)), every linear functional on $\mathbb{R}^n$ has the form $f(\boldsymbol{x})=\boldsymbol{z}^{\mathsf T}\boldsymbol{x}\triangleq f_{\boldsymbol{z}}(\boldsymbol{x})$ for some $\boldsymbol{z}\in\mathbb{R}^n$. Every normed space has a dual space of linear functionals, each with a size given by the *dual norm*

$$
\|f\|'=\sup_{\boldsymbol{x}\ne\boldsymbol{0}}\frac{|f(\boldsymbol{x})|}{\|\boldsymbol{x}\|},\qquad\text{in coordinates}\qquad\|\boldsymbol{z}\|'=\sup_{\boldsymbol{x}\ne\boldsymbol{0}}\frac{|\boldsymbol{z}^{\mathsf T}\boldsymbol{x}|}{\|\boldsymbol{x}\|},
$$
which is the induced norm of the $1\times n$ matrix $\boldsymbol{z}^{\mathsf T}$. The dual of the $\ell^\infty$ norm is the $\ell^1$ norm, the dual of $\ell^1$ is $\ell^\infty$, and $\ell^2$ is its own dual (by the Cauchy–Schwarz inequality).

**Example 1.4.3** A student asked: for $A=(1,-1)$ and $f(\boldsymbol{x})=A\boldsymbol{x}=x_1-x_2$, regarded as a vector $\|A\|_\infty=\max\{|1|,|-1|\}=1$, but regarded as a matrix

$$
\|A\|_\infty=\sup_{x_1,x_2}\frac{|x_1-x_2|}{\max\{|x_1|,|x_2|\}}=2.
$$
Is this a contradiction? No: the two numbers are norms of different objects in different spaces. As an element of $\mathbb{R}^2$, $A$ has the vector $\ell^\infty$ norm $1$. As a linear operator from $(\mathbb{R}^2,\|\cdot\|_\infty)$ to $\mathbb{R}$, it has the induced norm, which is the maximum absolute row sum $|1|+|-1|=2$, that is, the dual norm $\|(1,-1)\|_1=2$ (attained at $\boldsymbol{x}=(1,-1)^{\mathsf T}$). Whenever a condition number is computed, one has to be clear about which space the object lives in; for the subtraction problem of Example 1.4.2 the relevant number is the operator norm $2$.

### 1.4.4. Conditioning of Linear Systems

Fix a nonsingular $A\in\mathbb{R}^{m\times m}$ and use the same norm on all vectors and the induced norm on matrices.

**Proposition 1.4.1** The problem of computing $A\boldsymbol{x}$ from the input $\boldsymbol{x}$ has relative condition number

$$
\kappa(\boldsymbol{x})=\|A\|\frac{\|\boldsymbol{x}\|}{\|A\boldsymbol{x}\|}\le\|A\|\,\|A^{-1}\|,
$$
and the problem of solving $A\boldsymbol{x}=\boldsymbol{b}$ for $\boldsymbol{x}$ given $\boldsymbol{b}$ has relative condition number

$$
\kappa(\boldsymbol{b})=\|A^{-1}\|\frac{\|\boldsymbol{b}\|}{\|\boldsymbol{x}\|}\le\|A^{-1}\|\,\|A\|.
$$

**Proof** For $f(\boldsymbol{x})=A\boldsymbol{x}$, $\delta f=A\,\delta\boldsymbol{x}$, so

$$
\kappa(\boldsymbol{x})=\sup_{\delta\boldsymbol{x}}\frac{\|A\,\delta\boldsymbol{x}\|/\|A\boldsymbol{x}\|}{\|\delta\boldsymbol{x}\|/\|\boldsymbol{x}\|}=\frac{\|\boldsymbol{x}\|}{\|A\boldsymbol{x}\|}\sup_{\delta\boldsymbol{x}}\frac{\|A\,\delta\boldsymbol{x}\|}{\|\delta\boldsymbol{x}\|}=\frac{\|\boldsymbol{x}\|}{\|A\boldsymbol{x}\|}\|A\|,
$$
and $\|\boldsymbol{x}\|=\|A^{-1}A\boldsymbol{x}\|\le\|A^{-1}\|\,\|A\boldsymbol{x}\|$ gives the bound. The second problem is the first one with $A^{-1}$ in place of $A$ and $\boldsymbol{b}$ in place of $\boldsymbol{x}$. $\square$

Now let $\boldsymbol{b}$ be fixed and perturb the matrix by an infinitesimal $\delta A$. Then $(A+\delta A)(\boldsymbol{x}+\delta\boldsymbol{x})=\boldsymbol{b}$; dropping the doubly infinitesimal term $(\delta A)(\delta\boldsymbol{x})$ gives $(\delta A)\boldsymbol{x}+A(\delta\boldsymbol{x})\approx\boldsymbol{0}$, that is, $\delta\boldsymbol{x}\approx-A^{-1}(\delta A)\boldsymbol{x}$, so $\|\delta\boldsymbol{x}\|\le\|A^{-1}\|\,\|\delta A\|\,\|\boldsymbol{x}\|$ and

$$
\frac{\|\delta\boldsymbol{x}\|/\|\boldsymbol{x}\|}{\|\delta A\|/\|A\|}\le\frac{\|A\|}{\|\boldsymbol{x}\|}\cdot\frac{\|A^{-1}\|\,\|\delta A\|\,\|\boldsymbol{x}\|}{\|\delta A\|}=\|A\|\,\|A^{-1}\|.
$$
For any $A$, $\boldsymbol{b}$ and norm there is a perturbation $\delta A$ for which $\|A^{-1}(\delta A)\boldsymbol{x}\|=\|A^{-1}\|\,\|\delta A\|\,\|\boldsymbol{x}\|$ (choose $\delta A=\eta\,\boldsymbol{w}\boldsymbol{z}^{\mathsf T}$, where $\boldsymbol{w}$ is a unit vector with $\|A^{-1}\boldsymbol{w}\|=\|A^{-1}\|$ and $\boldsymbol{z}$ satisfies $\boldsymbol{z}^{\mathsf T}\boldsymbol{x}=\|\boldsymbol{x}\|$ and $\|\boldsymbol{z}\|'=1$ in the dual norm), so the bound is attained:

$$
\kappa(A)\triangleq\sup_{\delta A}\frac{\|\delta\boldsymbol{x}\|/\|\boldsymbol{x}\|}{\|\delta A\|/\|A\|}=\|A\|\,\|A^{-1}\|.
\tag{1.1}
$$

The number $\kappa(A)=\|A\|\,\|A^{-1}\|$ is the **condition number** of the matrix $A$ ([2.1.7](/2.1.7)). It bounds how inaccurate the computed solution $\boldsymbol{x}$ of a linear system will be after approximation: by Theorem 1.4.1, a backward stable solver gives a relative error $O(\kappa(A)\,u)$. If the problem contains an ill-conditioned matrix $A$, we usually expect to "lose $\log_{10}\kappa(A)$ digits" in computing the solution.

For the $\ell^2$ norm, $\|A\|_2=\sigma_1$ and $\|A^{-1}\|_2=1/\sigma_m$, where $\sigma_1$ and $\sigma_m$ are the largest and smallest **singular values** in the **singular value decomposition** $A=U\Sigma V^{\mathsf T}$, so

$$
\kappa_2(A)=\frac{\sigma_1}{\sigma_m}.
$$
In Proposition 1.4.1 the bound $\kappa(\boldsymbol{x})\le\kappa(A)$ holds with equality if $\boldsymbol{x}$ is a multiple of the right **singular vector** $\boldsymbol{v}_m$ of $A$ corresponding to $\sigma_m$ (then $\|A\boldsymbol{x}\|_2=\sigma_m\|\boldsymbol{x}\|_2$), and $\kappa(\boldsymbol{b})\le\kappa(A)$ holds with equality if $\boldsymbol{b}$ is a multiple of the left singular vector $\boldsymbol{u}_1$ corresponding to $\sigma_1$ (then $\boldsymbol{x}=A^{-1}\boldsymbol{b}=\boldsymbol{v}_1\|\boldsymbol{b}\|_2/\sigma_1$).

**Remark 1.4.1** Two properties of $\kappa(A)$:

- $\kappa(A)\ge1$ for every induced norm, since by submultiplicativity $\kappa(A)=\|A^{-1}\|\,\|A\|\ge\|A^{-1}A\|=\|I\|=1$; for the $\ell^2$ norm this is $\sigma_1/\sigma_m\ge1$, with equality exactly for multiples of orthogonal matrices.
- If $A\in\mathbb{R}^{m\times n}$ is rectangular with full rank $n\le m$, the condition number is defined with the **Moore–Penrose pseudoinverse** $A^+=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\in\mathbb{R}^{n\times m}$ as $\kappa(A)\triangleq\|A^+\|\,\|A\|$. Since $A^+$ is motivated by least squares problems, this definition is most useful in the $\ell^2$ norm, where $\kappa(A)=\sigma_1/\sigma_n$. It reappears in the least squares algorithms of [3.5.3](/3.5.3).

**Example 1.4.4 (Eigenvalues of Nonsymmetric Matrices)** Computing eigenvalues is a nonlinear problem, but conditioning applies all the same. The matrices

$$
\begin{bmatrix}1&1000\\0&1\end{bmatrix}\qquad\text{and}\qquad\begin{bmatrix}1&1000\\0.001&1\end{bmatrix}
$$
differ by $0.001$ in one entry. The first has the double eigenvalue $1$; the second has characteristic polynomial $(\lambda-1)^2-1$ and eigenvalues $0$ and $2$. A perturbation of size $10^{-3}$ moves the eigenvalues by $1$: the eigenvalue problem of a nonsymmetric matrix is often ill-conditioned. For symmetric matrices it is well-conditioned: the eigenvalues move by at most $\|\delta A\|_2$, so $\hat\kappa=1$ (Weyl's inequality, or the Bauer–Fike theorem for normal matrices; compare [2.1.7](/2.1.7)). Intuitively, the eigenvectors of a symmetric matrix are orthogonal, and the orthogonal similarity that diagonalizes it has condition number $1$, so nothing is amplified.

## 1.5. Comparing Algorithms

### 1.5.1. The Cost of an Algorithm

Algorithms for the same problem are compared by

- the number of floating-point operations they perform: a *flop* is one floating-point addition, subtraction, multiplication or division, and the count is given as a function of the size of the problem (its order) together with the leading constant, such as $\tfrac23n^3$ flops for the LU decomposition of an $n\times n$ matrix. Flop counts underestimate the execution time, which also depends on memory traffic, but the time is frequently proportional to the count;
- the memory requirement;
- the accuracy, that is, the stability of the algorithm with respect to floating-point arithmetic.

The next two examples show that algorithms with the same mathematical result and similar costs can differ greatly in accuracy.

### 1.5.2. Numerical Differentiation

To approximate the **derivative** of a function $f$ at a point $x_0$, recall **Taylor's formula**

$$
f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(\xi)}{2}(x-x_0)^2,
$$
which gives

$$
\frac{f(x_0+h)-f(x_0)}{h}=f'(x_0)+\frac{f''(\xi)}{2}h=f'(x_0)+O(h).
$$
The left side, the *forward difference* approximation, approximates $f'(x_0)$ with an error proportional to the offset $h$, which diminishes as $h$ gets small. The *backward difference* $\bigl(f(x_0)-f(x_0-h)\bigr)/h=f'(x_0)+O(h)$ behaves in the same way. Expanding to third order,

$$
\begin{aligned}
f(x_0+h)&=f(x_0)+f'(x_0)h+\frac{f''(x_0)}{2}h^2+\frac{f^{(3)}(\xi_1)}{3!}h^3,\\
f(x_0-h)&=f(x_0)-f'(x_0)h+\frac{f''(x_0)}{2}h^2-\frac{f^{(3)}(\xi_2)}{3!}h^3,
\end{aligned}
$$
and subtracting, the $h^2$ terms cancel:

$$
\frac{f(x_0+h)-f(x_0-h)}{2h}=f'(x_0)+\frac{f^{(3)}(\xi_1)+f^{(3)}(\xi_2)}{12}h^2=f'(x_0)+O(h^2).
$$
This *central difference* (symmetric difference quotient) approximation is widely used in practice. For $f(x)=\mathrm{e}^x$ at $x_0=0$ with $h=1$, the forward, central and backward differences give $1.7183$, $1.1752$ and $0.6321$, with errors $0.7183$, $0.1752$ and $0.3679$ against the exact value $1$.

The formulas suggest that smaller $h$ always gives more accurate results. On a computer this is false: the numerator is a difference of two nearly equal computed values, a catastrophic cancellation. Each of $f(x_0\pm h)$ carries a rounding error of about $u|f(x_0)|$, so the computed forward difference has total error approximately

$$
\frac{|f''(x_0)|}{2}h+\frac{2u|f(x_0)|}{h},
$$
a truncation error that decreases with $h$ plus a rounding error that increases as $h\to0$. The sum is minimized near $h^*=2\sqrt{u|f(x_0)|/|f''(x_0)|}$, of order $\sqrt u\approx10^{-8}$, where the error is also about $10^{-8}$: only half of the digits are correct. For the central difference the error is about $\frac{|f^{(3)}(x_0)|}{6}h^2+\frac{u|f(x_0)|}{h}$, minimized near $h^*=\bigl(3u|f(x_0)|/|f^{(3)}(x_0)|\bigr)^{1/3}$, of order $u^{1/3}\approx10^{-5}$, with an error of about $10^{-10}$.

![Absolute error of the forward and central difference approximations to the derivative of exp at 1 as functions of h on log-log axes: both errors first decrease like h and h^2 (dashed truncation lines), reach their minima near h = 1e-8 and h = 1e-5 (vertical lines), and then increase like 2u f / h (dotted line) as rounding errors take over](./plots/numerical-differentiation-error.py)

### 1.5.3. Computing the Sample Variance

Which algorithm should be used to compute the **sample variance** $S^2$ of data $X_1,\dots,X_n$? Four candidates, all mathematically equivalent:

| Algorithm | Formulas |
|---|---|
| Two-pass algorithm | $\bar X=\dfrac1n\sum_{i=1}^nX_i$, then $S^2=\dfrac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2$ |
| West's algorithm | $M_1=X_1$, $T_1=0$; for $k=2,\dots,n$: $M_k=M_{k-1}+\dfrac{X_k-M_{k-1}}{k}$, $T_k=T_{k-1}+(k-1)(X_k-M_{k-1})\dfrac{X_k-M_{k-1}}{k}$; then $\bar X=M_n$, $S^2=\dfrac{T_n}{n-1}$ |
| Textbook algorithm | $\bar X=\dfrac1n\sum_{i=1}^nX_i$, $S^2=\dfrac{1}{n-1}\Bigl(\sum_{i=1}^nX_i^2-\dfrac1n\bigl(\sum_{i=1}^nX_i\bigr)^2\Bigr)$ |
| Cotton's algorithm | $M_1=X_1$, $T_1=0$; for $k=2,\dots,n$: $M_k=M_{k-1}+\dfrac{X_k-M_{k-1}}{k}$, $T_k=T_{k-1}+X_k^2+(k-1)M_{k-1}^2-kM_k^2$; then $S^2=\dfrac{T_n}{n-1}$ |

In all of them $T_k=\sum_{i=1}^k(X_i-M_k)^2$, the sum of squared deviations of the first $k$ observations. The textbook algorithm and Cotton's algorithm compute it as a difference of two large sums, $\sum X_i^2$ and $n\bar X^2$ (Cotton's algorithm does so incrementally, $T_k=\sum_{i\le k}X_i^2-kM_k^2$). If the mean is large compared with the standard deviation, both sums are about $n\bar X^2$, each carries a rounding error of order $u\,n\bar X^2$, and their difference, about $(n-1)S^2$, suffers catastrophic cancellation: the relative error is of order $u\bar X^2/S^2$, and all digits are lost once $\bar X^2/S^2\approx1/u\approx10^{16}$. The result can even be negative. The two-pass algorithm subtracts the mean first, a benign operation on the data, and then sums nonnegative squares; it is the most accurate, at the price of reading the data twice. West's algorithm (a form of Welford's updating algorithm) also works with deviations $X_k-M_{k-1}$ and adds only nonnegative terms; it needs only one pass, which matters for streaming data, and is almost as accurate. The two-pass algorithm or West's algorithm is the one to recommend; R's `var()` also centers the data before squaring.

![Relative error of the sample variance of 1000 standard normal values shifted by c, for c from 1 to 1e9, on log-log axes: the two-pass algorithm stays at the level of 1e-16 to 1e-15, West's one-pass algorithm loses a few more digits (about 1e-9 at c = 1e9), while the textbook algorithm and Cotton's algorithm lose two digits per factor of 10 in c and have relative errors of order 1 or larger from c = 1e8 on](./plots/sample-variance-algorithms.py)

A simple remedy for one-pass formulas is to shift the data by any value close to the mean (for example $X_1$) before using them, since the variance is invariant under shifts.

## Summary

| Topic | Key facts |
|---|---|
| Units | bit $\in\{0,1\}$; byte $=8$ bits; word $=16/32/64$ bits; $1$ KiB $=2^{10}$ bytes; UTF-8 encodes Unicode compatibly with ASCII |
| Fixed point | models the integers; point fixed; small range, fixed gaps; overflow |
| Floating point | models the reals; $\pm1.M\times2^{E-\text{bias}}$; huge range; gaps proportional to size |
| IEEE single / double | $1+8+23$ / $1+11+52$ bits; bias $127$ / $1023$; $E=0$: zero and subnormals; $E$ maximal: $\pm\infty$ and NaN |
| Machine epsilon | $\varepsilon_{\mathrm{mach}}=2^{1-p}$ ($2^{-52}$ in R); unit roundoff $u=2^{-p}$; $\operatorname{fl}(r)=r(1+\mu)$, $\lvert\mu\rvert\le u$ |
| Errors | forward error $\tilde f(x)-f(x)$; backward error: the smallest data perturbation explaining $\tilde f(x)$ |
| Algorithms | backward stable $\Rightarrow$ stable; accurate $\Rightarrow$ stable; accuracy also needs good conditioning |
| Arithmetic | $\otimes,\oslash$ backward stable; $\ominus$ of computed quantities: catastrophic cancellation; $\oplus$: absorption; not associative; never test with `==` |
| Conditioning | $\kappa(x)=\Vert J(x)\Vert\,\Vert x\Vert/\Vert f(x)\Vert$; backward stable algorithm: relative error $O(\kappa u)$ |
| Linear systems | $\kappa(A)=\Vert A\Vert\,\Vert A^{-1}\Vert\ge1$, $\kappa_2(A)=\sigma_1/\sigma_m$; lose about $\log_{10}\kappa(A)$ digits |
| Practice | central differences with $h\approx u^{1/3}$; two-pass or West's algorithm for variances; sum small terms first |
