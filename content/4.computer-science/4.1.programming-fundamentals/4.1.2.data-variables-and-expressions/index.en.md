---
title: Data, Variables and Expressions
description: Defining, initializing and assigning variables; ranges and memory representations of the basic data types; integer overflow and undefined behavior; floating-point error; operators, precedence and order of evaluation; implicit and explicit type conversion; input, output and formatting; dynamic typing, everything-is-an-object and unbounded integers in Python.
source_hash: f15d0e701d8e
---

Programs process data. This chapter discusses how data is named in a program (variables), how it is interpreted (data types), how it takes part in computation (expressions and operators), and how it enters and leaves a program (input and output). Many "mysterious" errors of beginners, such as `5/9` being $0$, the product of two positive numbers being negative, or `0.1 + 0.2 != 0.3`, all come from not realizing that numbers in a computer differ from numbers in mathematics: they have a fixed number of digits and a definite encoding. The encodings of integers and floating-point numbers are discussed in detail in [3.5.1](/3.5.1); this chapter only explains their consequences from the point of view of writing programs. The next chapter [4.1.3](/4.1.3) uses the expressions of this chapter to build branches and loops; the addresses of variables and pointers are left to [4.1.8](/4.1.8).

## 2.1. Variables

### 2.1.1. Defining and Assigning Variables

Consider an example: convert a Fahrenheit temperature to Celsius, $C = \frac{5}{9}(F - 32)$, with the Fahrenheit temperature entered by the user.

```cpp tab
#include <iostream>

int main() {
    double fahrenheit;                  // define a variable
    std::cout << "Fahrenheit: ";
    std::cin >> fahrenheit;             // read a value into it
    double celsius = 5.0 / 9 * (fahrenheit - 32);   // define and initialize
    std::cout << fahrenheit << " F = " << celsius << " C\n";
    return 0;
}
```

```python tab
fahrenheit = float(input("Fahrenheit: "))   # input() returns a string
celsius = 5 / 9 * (fahrenheit - 32)
print(f"{fahrenheit} F = {celsius} C")
```

With input `98.6`, both programs print a result close to `37`. A quantity in a program that can be stored and changed while the program runs is a variable.

**Definition 2.1.1 (Variable)** A **variable** is a named storage unit in a program. In C++, a variable has four attributes: its name, its type, the memory location it occupies, and the value currently stored; the type is fixed at definition and does not change afterwards.

In C++ a variable must be defined before it is used:

```cpp
double d;              // definition: type name, then variable name
int count = 0;         // definition with initialization
int n{10};             // brace initialization (C++11), rejects narrowing such as int n{3.7}
const double pi = 3.141592653589793;   // a named constant: cannot be assigned later
constexpr int days_per_week = 7;       // a compile-time constant
```

A variable name (identifier) consists of letters, digits and underscores, cannot start with a digit, is case sensitive, and cannot be a keyword such as `int`, `if` or `for`. Giving a constant name to a value that appears repeatedly (such as a precision or an array size) makes the code easier to read and ensures that a change is made in only one place.

The meaning of the assignment `x = e` is: compute the value of the expression $e$ on the right and use it to overwrite the old value of the variable `x`. The variables used on the right are only read; their values do not change. Hence `a = a + 1` is not an equation but "add $1$ to the value of `a` and store it back in `a`":

```cpp
int a = 0, b = 0, c = 0;
a = 7;        // a is 7 (the old 0 is overwritten)
b = a;        // b is 7, a is unchanged
c = a + b;    // c is 14
a = a + 1;    // a is 8
```

In C++, if a local variable is defined without initialization, its value is indeterminate and reading it is an error (a **compiler** usually warns about this with `-Wall`). Get into the habit of initializing at definition.

### 2.1.2. In Python: Names and Objects

Python has a different model of variables. In Python all data are objects, each with its own type and value; a variable is merely a name bound to an object, and the assignment `x = e` makes the name `x` refer to the object that is the result of the expression $e$. The name itself has no type:

```python
x = 42            # x refers to an int object
print(type(x))    # <class 'int'>
x = "forty-two"   # now x refers to a str object; this is allowed
print(type(x))    # <class 'str'>
```

The time at which types are checked is an important difference between the two languages. In a language with *static typing*, the type of every variable and expression is determined at compile time and type errors are reported at compile time; C++ is of this kind. In a language with *dynamic typing*, types belong to the values at run time rather than to the variables, and a type error is found only when the offending line executes; Python is of this kind. For example, adding a string and an integer, `std::string("1") + 2`, fails to compile in C++, whereas `"1" + 2` in Python raises a `TypeError` only at run time. Python allows type annotations such as `count: int = 0`; the **interpreter** does not check them, but tools such as mypy can use them for static checking ([4.2.9](/4.2.9), [4.4.1](/4.4.1)).

The consequences of the separation of names and objects will show up in parameter passing ([4.1.4](/4.1.4)) and in lists ([4.1.6](/4.1.6)).

## 2.2. Basic Data Types

### 2.2.1. Types, Ranges and Sizes

**Definition 2.2.1 (Data Type)** A **data type** specifies the set of values of a class of data, the operations that can be performed on them, and how these values are represented in memory. The same string of bits, interpreted as an integer and as a floating-point number, gives entirely different values.

The basic types of C++ (typical for GCC on 64-bit Linux):

| Type | Bytes | Range or precision | Use |
|---|---|---|---|
| `bool` | 1 | `true`, `false` | Logical values |
| `char` | 1 | Usually $-128 \sim 127$ | Characters (stores a character code) |
| `short` | 2 | $-2^{15} \sim 2^{15}-1$ | |
| `int` | 4 | $-2^{31} \sim 2^{31}-1$, about $\pm 2.1 \times 10^9$ | The default integer type |
| `long` | 8 (4 on Windows) | Platform dependent | Avoid where possible |
| `long long` | 8 | $-2^{63} \sim 2^{63}-1$, about $\pm 9.2 \times 10^{18}$ | Large integers |
| `unsigned int` | 4 | $0 \sim 2^{32}-1$ | Nonnegative integers, bit operations |
| `float` | 4 | About 7 significant digits | Single-precision floating point |
| `double` | 8 | About 15 to 16 significant digits | The default floating-point type |
| `long double` | 16 (x86-64 GCC, actually 80-bit extended precision; 8 on MSVC) | Platform dependent | |

The C++ standard specifies only the minimum range and the ordering of sizes of the types (`sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`); the concrete sizes are determined by the platform. When a definite width is needed, use the fixed-width types `std::int32_t`, `std::int64_t`, `std::uint8_t` and so on from `<cstdint>`; use `std::size_t` for sizes and indices. The operator `sizeof` gives the number of bytes occupied by a type or variable, and `std::numeric_limits<T>` in `<limits>` gives the range of a type, for example `std::numeric_limits<int>::max()`.

Python has only a few basic types: `int` (integers of arbitrary size), `float` (an IEEE 754 double, equivalent to C++ `double`), `complex`, `bool` (`True` and `False`, a subclass of `int`) and `str` (strings; there is no separate character type).

### 2.2.2. Integer Representation and Overflow

Integers are stored in memory in binary. An intuitive example is the "number-guessing cards": write the numbers in $1 \sim 63$ whose $k$-th binary digit is $1$ on card number $k$ ($k = 0, 1, \dots, 5$); the other person only needs to say on which cards the number he has in mind appears, and adding up the $2^k$ of those cards gives the number. For example $37 = (100101)_2 = 2^5 + 2^2 + 2^0$ appears exactly on cards 0, 2 and 5. The program that generates the cards is in [4.1.3](/4.1.3).

Signed integers are represented in **two's complement**; the range of an $N$-bit signed integer is $-2^{N-1} \sim 2^{N-1}-1$, while for an unsigned integer all $N$ bits are value bits and the range is $0 \sim 2^N - 1$. Bits, bytes and word length, and the encodings of sign-magnitude and two's complement, are treated in Sections 1.1.2 and 1.2.1 of [Computer Representation of Numbers](/3.5.1#sec-1.1.2); here we discuss only the consequences one must know when programming. The range is finite and the result of an operation may exceed it, which is called **overflow** in general in [3.5.1](/3.5.1#sec-1.2.1); for integer operations the consequence depends on the type.

**Definition 2.2.2 (Integer Overflow)** When the mathematical result of an integer operation exceeds the range representable by the result type, we speak of **integer overflow**. In C++, operations on unsigned integers are performed modulo $2^N$ and "wrap around" on overflow, with a well-defined result; signed integer overflow is undefined behavior.

**Definition 2.2.3 (Undefined Behavior)** A program behavior whose result the C++ standard does not specify at all is called **undefined behavior** (UB). Once a program exhibits undefined behavior, the standard no longer gives any guarantee about the execution of the whole program: it may print a plausible value, crash, or behave entirely differently when optimization is turned on. Common undefined behaviors are signed integer overflow, array out-of-bounds access, reading an uninitialized variable and division by zero.

```cpp
#include <climits>
#include <iostream>

int main() {
    int a = 50000;
    int square = a * a;                       // overflow: undefined behavior
    long long wide = 1LL * a * a;             // compute in a 64-bit type
    unsigned int u = 0;
    u = u - 1;                                // well defined: wraps to 2^32 - 1
    std::cout << square << '\n' << wide << '\n' << u << '\n';
    std::cout << INT_MAX << ' ' << INT_MIN << '\n';
    return 0;
}
```

On x86-64, `square` usually prints `-1794967296` (that is, $2.5 \times 10^9 - 2^{32}$), but this is not a result one can rely on. Compiled with `-fsanitize=undefined`, the program reports `signed integer overflow: 50000 * 50000 cannot be represented in type 'int'` when it reaches the overflow. Note the form `1LL * a * a`: one operand is first turned into `long long`, so that the multiplication takes place in 64 bits; written as `long long wide = a * a;`, the multiplication is still carried out in `int` first and has already overflowed.

Estimating orders of magnitude is a basic skill for avoiding overflow: $12! \approx 4.8 \times 10^8$ is still within the range of `int`, while $13! \approx 6.2 \times 10^9$ exceeds it; the sum of $10^5$ numbers each at most $10^5$ can reach $10^{10}$ and requires `long long`.

In Python: the `int` of Python has no fixed number of bits and allocates memory as needed, so integer arithmetic never overflows: `2**100` gives exactly `1267650600228229401496703205376`. The price is speed: every integer is an object, and the time for operations on big integers grows with the number of digits. The `float` of Python is still a 64-bit floating-point number; when the result of an operation such as multiplication is too large the result is `inf` (functions such as `math.exp` raise `OverflowError` instead); the integer arrays of the third-party library NumPy are also fixed-width and do wrap around ([4.4.2](/4.4.2)).

### 2.2.3. Floating-Point Numbers and Rounding Error

`float` and `double` are the single- and double-precision **floating-point numbers** of the IEEE 754 standard. Their format (sign, exponent, significand), normalized and subnormal numbers, and the conversion between decimal and binary are discussed in detail in [Section 1.2 of Computer Representation of Numbers](/3.5.1#sec-1.2); what we must remember when programming is that a floating-point number can represent exactly only finitely many numbers of the form $\pm m \times 2^e$, and every other real number must be rounded. The binary representation of $0.1$ is an infinite repeating fraction, so:

```cpp tab
#include <iostream>

int main() {
    std::cout << (0.1 + 0.2 == 0.3) << '\n';   // prints 0 (false)
    float f1 = 34.6f, f2 = 34.0f;
    std::cout << f1 - f2 << '\n';              // prints 0.599998
    return 0;
}
```

```python tab
print(0.1 + 0.2 == 0.3)   # False
print(0.1 + 0.2)          # 0.30000000000000004
```

The relative spacing of adjacent floating-point numbers is determined by the **machine epsilon** ([Section 1.2.5 of 3.5.1](/3.5.1#sec-1.2.5)): about $2.2 \times 10^{-16}$ for `double` (`std::numeric_limits<double>::epsilon()`, or `sys.float_info.epsilon` in Python) and about $1.2 \times 10^{-7}$ for `float`. This gives two programming rules:

- Use `double` by default, and use `float` only when memory or speed really requires it;
- Do not compare two computed floating-point numbers with `==`; instead test whether their difference is small enough, for example `std::abs(x - y) <= 1e-9 * std::max(std::abs(x), std::abs(y))`; in Python use `math.isclose(x, y)`.

Quantities that must be exact decimals, such as money, should not use floating-point numbers; store them as integers in units of cents (Python also has the standard library `decimal`). How rounding errors propagate through a computation, why floating-point arithmetic is not associative, and what makes an algorithm stable are covered in [Section 1.3 of Computer Representation of Numbers](/3.5.1#sec-1.3).

### 2.2.4. Characters and Boolean Values

A `char` stores the code of a character, that is, a small integer; the rule that matches characters with codes is the **character encoding**. English letters, digits and common symbols use the ASCII encoding; for example `'A'` is $65$, `'a'` is $97$, `'0'` is $48$, and uppercase and lowercase letters differ by $32$. Characters can therefore take part in arithmetic and comparisons: the value of `'A' + 2` is the integer $67$, `char('A' + 2)` is the character `'C'`; `'0' <= c && c <= '9'` tests whether `c` is a digit character, and `c - '0'` gives the numeric value it represents. Non-ASCII characters such as Chinese characters cannot fit into a single `char`; strings and Unicode are discussed in [4.1.7](/4.1.7).

Character constants use single quotes (`'A'`) and string constants use double quotes (`"A"`); their types differ. Special characters are written as *escape sequences*: `'\n'` newline, `'\t'` tab, `'\\'` backslash, `'\''` and `'\"'` quotes, and `'\0'` the null character with code $0$.

`bool` has only the two values `true` and `false`. It can be converted to and from integers: `true` becomes $1$ and `false` becomes $0$; when an integer is converted to `bool`, $0$ gives `false` and any nonzero value gives `true`. `std::cout` prints a boolean as `1` or `0` by default, and as `true` or `false` after `std::boolalpha` has been output.

## 2.3. Expressions and Operators

An *expression* consists of operands (variables, constants, function calls) and operators, and yields a value when evaluated.

### 2.3.1. Arithmetic Operations

| Operator | Meaning | Note |
|---|---|---|
| `+ - *` | Addition, subtraction, multiplication | Integers may overflow |
| `/` | Division | Dividing two integers gives an integer; the fractional part is discarded |
| `%` | Remainder | Integers only |

In C++, integer division truncates toward zero, and the remainder has the same sign as the dividend, so that `(a / b) * b + a % b == a`; in Python, `/` always gives a floating-point number, integer division is written `//` and rounds down (floor), and the result of `%` has the same sign as the divisor. The two differ on negative numbers:

| Expression | C++ | Python |
|---|---|---|
| `7 / 2` | `3` | `3.5` |
| `7 // 2` | — | `3` |
| `-7 / 2` (C++), `-7 // 2` (Python) | `-3` | `-4` |
| `-7 % 2` | `-1` | `1` |

Integer division and remainder are the basic tools for handling digits: for a three-digit number `n`, the units digit is `n % 10`, the tens digit is `n / 10 % 10` and the hundreds digit is `n / 100`. To test parity, write `n % 2 == 0` (for negative numbers, `n % 2 == 1` cannot be used in C++ to test for an odd number because `-3 % 2` is `-1`; write `n % 2 != 0`).

### 2.3.2. Assignment and Increment

Compound assignment is a common shorthand: `x += 2` means `x = x + 2`, and similarly for `-=`, `*=`, `/=`, `%=`. C++ also has the increment and decrement operators:

| Form | Effect | Value of the expression |
|---|---|---|
| `++i` | `i` increases by 1 | The value after increasing |
| `i++` | `i` increases by 1 | The value before increasing |
| `--i`, `i--` | `i` decreases by 1 | Same as above |

As a statement on its own, `++i;` and `i++;` have the same effect, and the usual habit is to write `++i`. Do not modify the same variable more than once in one expression, and do not read a variable while modifying it: `i = i++ + ++i` is undefined behavior; the result of `std::cout << i << i++ << ++i` was unspecified before C++17, while from C++17 on the operands of `<<` are evaluated from left to right, printing `23 23 25` (with `i` initially 23), but compilers may still warn, and such code is hard to read. Python has no `++`; write `i += 1`.

### 2.3.3. Relational Operations

The relational operators `>`, `<`, `>=`, `<=`, `==` (equal) and `!=` (not equal) compare two values, and the result is a `bool`. The most common error is writing `=` for `==`: `if (x = 0)` assigns $0$ to `x`, and the condition is always false; `-Wall` warns about this. In Python, writing an assignment inside a condition is a syntax error, and chained comparisons such as `0 <= x < 10` are supported; in C++, `0 <= x < 10` compiles, but it first evaluates `0 <= x` to get $0$ or $1$ and then compares that with $10$, so the result is always true; write `0 <= x && x < 10`. The logical operators `&&`, `||` and `!` are in [4.1.3](/4.1.3).

### 2.3.4. Precedence, Associativity and Order of Evaluation

When an expression contains several operators, precedence and associativity determine how the operands are grouped. The precedence of the common operators, from high to low, is roughly:

1. Postfix `x++`, function call `f(x)`, subscript `a[i]`;
2. Prefix `++x`, `!`, unary `-`, type casts;
3. `* / %`;
4. `+ -`;
5. `<< >>` (shifts, also used for input and output);
6. `< <= > >=`;
7. `== !=`;
8. `&`, `^`, `|` (bitwise operations, in decreasing order);
9. `&&`, then `||`;
10. `?:` and assignment `= += …` (right associative).

Binary arithmetic operators are left associative: `a - b - c` means `(a - b) - c`; assignment is right associative: `a = b = 0` means `a = (b = 0)`. Precedence determines only the grouping, not the order of evaluation: in `f() + g()`, which function is called first is unspecified. When in doubt about precedence, add parentheses, for example `(x & 1) == 0` (without parentheses it would be parsed as `x & (1 == 0)`).

### 2.3.5. Type Conversion

When data of different types are combined in an operation, an *implicit conversion* takes place:

- In arithmetic operations, the "narrower" type is converted to the "wider" type before computing: in an operation between `int` and `double`, the `int` is first converted to `double`; `char`, `bool` and `short` are first promoted to `int`.
- In assignment and initialization, the value on the right is converted to the type of the variable on the left. When a `double` is converted to `int`, the fractional part is cut off (rounding toward zero); such a conversion, which may lose information, is called a *narrowing conversion*.
- When signed and unsigned integers are mixed in an operation, the signed number is converted to unsigned, and the result of `-1 < 1u` is `false`. The compiler option `-Wsign-compare` (included in `-Wall`) warns about this.

If the temperature conversion at the beginning of the chapter were written as `5 / 9 * (fahrenheit - 32)`, then `5 / 9` is integer division with result $0$, and the program prints $0$ whatever the input; after writing `5.0 / 9`, the $9$ is converted to `double` and we get $0.555\ldots$.

When a conversion is needed, it should be written explicitly. The recommended C++ form is `static_cast<target type>(expression)`:

```cpp
double length = 3.7;
int n = static_cast<int>(length);       // 3: truncates toward zero
double ratio = static_cast<double>(n) / 2;   // 1.5 instead of 1
char next = static_cast<char>('A' + 1);      // 'B'
```

The C-style `(int)length` and the function-style `int(length)` also work, but they do not distinguish the kind of conversion and are hard to search for in code. Use `std::round` (in `<cmath>`) to round to the nearest integer and `std::floor` to round down.

In Python: Python never implicitly converts a string to a number: `"3" + 4` raises a `TypeError`, and the conversion must be written explicitly as `int("3")`, `float("2.5")` or `str(4)`. `int(-3.7)` truncates toward zero and gives `-3`, while `math.floor` rounds down; the built-in `round` uses "round half to even", so `round(2.5)` is `2` and `round(3.5)` is `4`, which reduces cumulative statistical bias.

## 2.4. Input and Output

C++ uses streams for input and output: `std::cin >> x` reads a value from standard input into `x`, skipping spaces and newlines when reading, so several data items may be written on one line or on several lines; `std::cout << e` outputs the value of an expression, and `<<` can be chained.

```cpp tab
#include <format>     // std::format (C++20)
#include <iomanip>    // std::setprecision, std::fixed
#include <iostream>

int main() {
    int n;
    double x;
    std::cin >> n >> x;                                   // e.g. "3 2.5"
    std::cout << std::fixed << std::setprecision(2) << n * x << '\n';   // 7.50
    std::cout << std::format("{} * {:.3f} = {:8.2f}\n", n, x, n * x); // aligned output
    return 0;
}
```

```python tab
n, x = input().split()          # e.g. "3 2.5"
n, x = int(n), float(x)
print(f"{n * x:.2f}")           # 7.50
print(f"{n} * {x:.3f} = {n * x:8.2f}")
```

The format specifications mean the same in both languages: `.2f` means fixed-point format with 2 decimal places, and `8.2f` additionally requires a total width of 8 characters (right aligned). The `std::format` of C++20 and the `std::print` of C++23 (`std::print("{}\n", x)`, which needs a recent compiler such as GCC 14) use Python's format syntax, which is clearer than manipulators such as `std::setprecision` or C's `printf`, and also safer (when the format string of `printf` does not match the argument types, the behavior is undefined). String formatting and file streams are in [4.2.11](/4.2.11).

The `input()` of Python reads a whole line and returns a string, which must be split and converted by hand; reading several integers from one line is often written `a, b = map(int, input().split())`.

## Summary

- A variable is a named storage unit; the type of a C++ variable is fixed at definition (static typing), while a Python name is only a label on an object and the type belongs to the object (dynamic typing).
- The data type determines the range of values and the memory representation. Integers have a fixed number of bits: signed integer overflow is undefined behavior, so estimate orders of magnitude and use `long long` when necessary; the Python `int` does not overflow.
- Floating-point numbers have rounding error; use `double` by default and do not compare floating-point numbers with `==`.
- Watch out for truncation in integer division, the different conventions of C++ and Python for division and remainder of negative numbers, `=` versus `==`, and operator precedence; do not modify the same variable several times in one expression.
- Mixed-type operations convert implicitly; when a conversion is needed, write it explicitly with `static_cast`. For formatting output prefer `std::format` (C++) and f-strings (Python).
