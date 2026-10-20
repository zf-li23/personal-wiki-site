---
title: Strings and Multidimensional Arrays
description: C-style strings and the terminator, functions of <cstring> and buffer overflow; std::string and Python's str; character encodings and UTF-8; row-major storage of two-dimensional arrays and matrix multiplication; bubble sort; sorting strings, std::sort and comparison functions, strict weak ordering; Python's sorted and key functions.
source_hash: b34c856555c0
---

The **arrays** of the previous chapter held numbers. This chapter discusses two important generalizations of arrays: the array whose elements are characters, the string, which is the basis of text processing in programs; and the array whose elements are themselves arrays, the multidimensional array, which represents matrices and tables. Finally we discuss another basic operation inseparable from arrays: sorting. Only sorted data can be searched with **binary search** ([4.1.6](/4.1.6)), and sorting is also the first step of many algorithms. The bubble sort of this chapter is the simplest sorting algorithm; the faster merge sort and quicksort are in [4.1.11](/4.1.11), and the systematic analysis of sorting algorithms is in [4.3.2](/4.3.2) and [4.3.14](/4.3.14); string streams, formatting and regular expressions are in [4.2.11](/4.2.11), and string-matching algorithms are in [4.3.13](/4.3.13).

## 7.1. Strings

**Definition 7.1.1 (String)** A **string** is a finite sequence of zero or more characters. The number of characters is called the length of the string, and a string of length zero is called the empty string.

### 7.1.1. C-Style Strings

The C language has no string type; it stores a string in a character array and places after the last character a null character `'\0'` with code $0$ as the terminator. String constants written in double quotes in C++ (such as `"china"`) are of this form, and both the functions in `<cstring>` and `std::cout` rely on the terminator to know where a string ends.

```cpp
char a[6] = "china";                     // 5 characters + '\0': needs 6 elements
char b[] = "china";                      // size deduced: 6
char c[5] = {'c', 'h', 'i', 'n', 'a'};   // no room for '\0': not a C string
// char d[4] = "china";                  // compile error in C++: too long
std::cout << sizeof(b) << ' ' << std::strlen(b) << '\n';   // 6 5
```

`sizeof` gives the number of bytes of the array (including the terminator), and `std::strlen` counts from the first character up to `'\0'` (not including the terminator); it must scan one by one, taking time proportional to the length. For a character array without a terminator such as `c`, `std::cout << c` keeps printing until it happens to meet a $0$ somewhere in memory, followed by garbage, which is already an out-of-bounds access.

Common functions provided by `<cstring>`:

| Function | Effect | Note |
|---|---|---|
| `strlen(s)` | Length | |
| `strcpy(dst, src)` | Copy `src` to `dst` | `dst` must be large enough |
| `strcat(dst, src)` | Append `src` to the end of `dst` | `dst` must hold the sum of both |
| `strcmp(s, t)` | Compare in lexicographic order | Returns a negative number, $0$ or a positive number, meaning `s` is less than, equal to or greater than `t` |

None of these functions knows how large the destination array is. `char name[8]; std::strcpy(name, "Tsinghua University");` writes beyond the array, which is called a *buffer overflow*; it not only makes the program fail but is also one of the most common security vulnerabilities in history: an attacker can construct overlong input to overwrite the return address on the stack (the **call stack** of [4.1.4](/4.1.4)). In C++ one should use `std::string`; C-style strings are needed only when dealing with interfaces to the C language, and then `s.c_str()` gets one from a `std::string`.

### 7.1.2. std::string

`std::string` (in `<string>`) manages its own storage, can grow to any length, and supports assignment, concatenation and comparison with operators:

```cpp tab
#include <iostream>
#include <string>

int main() {
    std::string s = "Beijing";
    s += ", Tsinghua";                        // concatenation
    std::cout << s << " (" << s.size() << ")\n";            // Beijing, Tsinghua (17)
    std::cout << s.substr(9, 8) << '\n';                    // Tsinghua: 8 chars from index 9
    std::cout << s.find("jing") << '\n';                    // 3: index of the first match
    if (s.find("Peking") == std::string::npos) std::cout << "not found\n";
    std::cout << (std::string("Peking") < "Tsinghua") << '\n';   // 1: lexicographic order
    for (char& ch : s)                         // modify characters in place
        if ('a' <= ch && ch <= 'z') ch = ch - 'a' + 'A';
    std::cout << s << '\n';                    // BEIJING, TSINGHUA
    int n = std::stoi("2026") + 1;             // string -> int
    std::cout << std::to_string(n) + "!" << '\n';   // int -> string: 2027!
    return 0;
}
```

```python tab
s = "Beijing"
s += ", Tsinghua"                     # creates a new string
print(s, f"({len(s)})")               # Beijing, Tsinghua (17)
print(s[9:17])                        # Tsinghua: slice from index 9 to 16
print(s.find("jing"))                 # 3: index of the first match
if "Peking" not in s:
    print("not found")
print("Peking" < "Tsinghua")          # True: lexicographic order
print(s.upper())                      # BEIJING, TSINGHUA
n = int("2026") + 1                   # str -> int
print(str(n) + "!")                   # int -> str: 2027!
```

The comparison operators compare two strings in *lexicographic order*: compare the codes of characters one by one from the first character, and the first differing character decides; if one string is a prefix of the other, the shorter string is smaller. Hence `"Zoo" < "apple"` (the codes of uppercase letters are smaller than those of lowercase letters) and `"10" < "9"` (the characters `'1'` and `'9'` are compared). To compare by numerical value, convert to numbers first.

`std::cin >> s` reads one "word" and stops at whitespace; to read a whole line containing spaces use `std::getline(std::cin, s)`. Calling `getline` right after `std::cin >> n` reads the newline character left over after `n` and so gets an empty line; one must first skip it with `std::cin.ignore()`, or read every line uniformly with `getline` and convert oneself. Read-only string parameters are passed as `const std::string&`; the `std::string_view` of C++17 can refer to part of a string without copying.

The Python string `str` is immutable: `s[0] = "b"` is an error, and `s += …` and `s.upper()` both produce new strings. Concatenating strings repeatedly with `+=` in a loop can be slow (each time may copy); put the pieces in a list and join them at the end with `"".join(parts)`. Python has no character type: `s[0]` is a string of length 1; `ord("A")` gives the code $65$ and `chr(65)` gives `"A"` conversely.

### 7.1.3. Character Encodings and Unicode

A `char` is one byte and can represent only $256$ values, enough for ASCII but not for Chinese characters. Modern programs generally use Unicode: it assigns a number to every character of the world's scripts, called its *code point*, for example U+6E05 for the first character of "Tsinghua" in Chinese; code points are then stored as bytes according to some **character encoding**, the most common being UTF-8: ASCII characters take 1 byte (compatible with ASCII), common Chinese characters take 3 bytes, and emoji and the like take 4 bytes ([3.5.1](/3.5.1)).

```cpp tab
#include <iostream>
#include <string>

int main() {
    std::string s = "\u6e05\u534e THU";      // two Chinese characters (Tsinghua) + " THU"
    std::cout << s.size() << '\n';            // 10: bytes, not characters
    return 0;
}
```

```python tab
s = "\u6e05\u534e THU"         # two Chinese characters (Tsinghua) + " THU"
print(len(s))                    # 6: code points
print(len(s.encode("utf-8")))    # 10: bytes in UTF-8
print(hex(ord("\u6e05")))      # 0x6e05
```

The C++ `std::string` is only a string of bytes, `size()` counts bytes, and `s[0]` is the first of the three bytes of the first character; handling Chinese text character by character requires a dedicated library. The Python 3 `str` is a sequence of code points, `len` counts code points, and an encoding needs to be specified only when reading or writing files or the network (`open(path, encoding="utf-8")`, `s.encode()`, `b.decode()`). Using UTF-8 uniformly for source files, terminals and data files avoids the vast majority of "garbled text" problems.

### 7.1.4. Example: Counting Letter Frequencies

**Example 7.1.1** Read a piece of English text and count how many times each of the 26 letters (case insensitive) occurs.

Use a counting array of length 26, with indices $0 \sim 25$ corresponding to `'a'` $\sim$ `'z'`: the index of a letter `ch` is `ch - 'a'`. This is another application of the idea from [4.1.6](/4.1.6) that "the index stands for the data itself", the same as in the **sieve of Eratosthenes**.

```cpp tab
#include <array>
#include <iostream>
#include <string>

int main() {
    std::array<int, 26> count{};                 // all zero
    std::string line;
    while (std::getline(std::cin, line))         // read until the end of input
        for (char ch : line) {
            if ('A' <= ch && ch <= 'Z') ch = ch - 'A' + 'a';   // to lower case
            if ('a' <= ch && ch <= 'z') ++count[ch - 'a'];      // letter -> index
        }
    for (int i = 0; i < 26; ++i)
        if (count[i] > 0)
            std::cout << static_cast<char>('a' + i) << ": " << count[i] << '\n';
    return 0;
}
```

```python tab
import sys

count = [0] * 26
for line in sys.stdin:                         # read until the end of input
    for ch in line.lower():
        if "a" <= ch <= "z":
            count[ord(ch) - ord("a")] += 1     # letter -> index
for i, c in enumerate(count):
    if c > 0:
        print(f"{chr(ord('a') + i)}: {c}")
```

The more natural way in Python is to use the standard library's `collections.Counter`, a dictionary from values to counts ([4.2.10](/4.2.10)); larger text-processing tasks such as word-frequency counting are in [4.1.9](/4.1.9).

## 7.2. Multidimensional Arrays

### 7.2.1. Two-Dimensional Arrays

A two-dimensional array with element type `T`, $R$ rows and $C$ columns is defined as `T a[R][C]`, and the element in row $i$ and column $j$ is `a[i][j]` ($0 \le i < R$, $0 \le j < C$). C++ understands it as "an array of $R$ elements, each of which is an array of $C$ `T`s".

```cpp
int m[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12},
};
for (int i = 0; i < 3; ++i) {          // row
    for (int j = 0; j < 4; ++j)        // column
        std::cout << m[i][j] << ' ';
    std::cout << '\n';
}
```

Memory is one-dimensional. C++ stores a two-dimensional array row by row: first all elements of row $0$, then row $1$, and so on, which is called *row-major order*. Hence the address of `a[i][j]` is $p + (iC + j) \cdot \mathrm{sizeof}(T)$, where $p$ is the starting address. Fortran, MATLAB and R, on the other hand, store column by column (column-major order). The storage order affects speed: when elements are accessed in storage order (in C++, let the inner loop run over the column index $j$), adjacent accesses fall on adjacent memory, making full use of the CPU cache ([4.10](/4.10)).

For a built-in two-dimensional array, both the number of rows and of columns must be compile-time constants, and as a function parameter the number of columns must be given (`void f(int a[][4], int rows)`). For a matrix whose size is determined at run time, one commonly uses `std::vector<std::vector<double>> a(rows, std::vector<double>(cols))`, each row of which is an independent `vector`; when performance matters, use a single `std::vector<double>` of length $R \cdot C$ and compute the index yourself as `a[i * C + j]`, so that all elements are stored contiguously. Higher-dimensional arrays follow by analogy.

### 7.2.2. Matrix Multiplication

The **matrix multiplication** of an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$ gives an $m \times p$ matrix $C$ with $c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$ ([2.1](/2.1)). Writing out the expression for each $c_{ij}$ directly gives a lot of similar code; noticing that only the three indices $i$, $j$, $k$ vary, we get a triple loop:

```cpp tab
#include <iostream>
#include <vector>

using Matrix = std::vector<std::vector<double>>;   // a type alias

Matrix multiply(const Matrix& a, const Matrix& b) {
    std::size_t m = a.size(), n = b.size(), p = b[0].size();   // a is m x n, b is n x p
    Matrix c(m, std::vector<double>(p, 0.0));
    for (std::size_t i = 0; i < m; ++i)
        for (std::size_t k = 0; k < n; ++k)        // i-k-j order: row-wise access to b and c
            for (std::size_t j = 0; j < p; ++j)
                c[i][j] += a[i][k] * b[k][j];
    return c;
}

int main() {
    Matrix a = {{1, 2, 3}, {4, 5, 6}};             // 2 x 3
    Matrix b = {{7, 8}, {9, 10}, {11, 12}};        // 3 x 2
    for (const auto& row : multiply(a, b)) {
        for (double x : row) std::cout << x << ' ';
        std::cout << '\n';                         // 58 64 / 139 154
    }
    return 0;
}
```

```python tab
def multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, n, p = len(a), len(b), len(b[0])            # a is m x n, b is n x p
    c = [[0.0] * p for _ in range(m)]              # a new list for each row
    for i in range(m):
        for k in range(n):
            for j in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c


a = [[1, 2, 3], [4, 5, 6]]                         # 2 x 3
b = [[7, 8], [9, 10], [11, 12]]                    # 3 x 2
for row in multiply(a, b):
    print(*row)                                    # 58.0 64.0 / 139.0 154.0
```

Each element of the result matrix needs $n$ multiplications, $mnp$ in total; multiplying two square matrices of order $n$ needs $n^3$. The three orders of the triple loop are mathematically equivalent; here $k$ is placed in the middle and $j$ innermost, so that both `b[k][j]` and `c[i][j]` are accessed contiguously along rows; for large matrices this is several times faster than the $i$-$j$-$k$ order of the definition. In real computation one should use a highly optimized linear algebra library (BLAS), which in Python means NumPy's `a @ b`, several orders of magnitude faster than the pure Python loops above ([4.4.3](/4.4.3)).

There is a pitfall when Python represents matrices as nested lists: `[[0.0] * p] * m` is not $m$ independent rows but $m$ references to the same row list ([4.1.6](/4.1.6)), and modifying `c[0][0]` changes the first element of every row. The code above uses a list comprehension to create a new list for each row, which avoids this problem.

## 7.3. Sorting

Sorting rearranges a group of elements in some order (such as from small to large).

### 7.3.1. Bubble Sort

**Algorithm 7.3.1 (Bubble Sort)** Bubble sort arranges an array $a$ of length $n$ in ascending order: compare adjacent elements $a[j]$ and $a[j+1]$ in turn from beginning to end, and swap them if $a[j] > a[j+1]$; this is called one pass. After one pass the largest element has been moved to the end, like a bubble rising; repeat the process on the first $n - 1$ elements, and so on, and after at most $n - 1$ passes everything is in order. If no swap occurs in some pass, the array is already sorted and the algorithm can stop early.

```cpp tab
#include <iostream>
#include <utility>   // std::swap
#include <vector>

void bubble_sort(std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    for (int pass = 1; pass < n; ++pass) {        // at most n - 1 passes
        bool swapped = false;
        for (int j = 0; j < n - pass; ++j)        // a[n-pass+1..n-1] are already in place
            if (a[j] > a[j + 1]) {
                std::swap(a[j], a[j + 1]);
                swapped = true;
            }
        if (!swapped) break;                      // no swap: already sorted
    }
}

int main() {
    std::vector<int> a = {8, 4, 7, 9, 3, 5, 1};
    bubble_sort(a);
    for (int x : a) std::cout << x << ' ';        // 1 3 4 5 7 8 9
    std::cout << '\n';
    return 0;
}
```

```python tab
def bubble_sort(a: list[int]) -> None:
    n = len(a)
    for p in range(1, n):                     # at most n - 1 passes
        swapped = False
        for j in range(n - p):                # a[n-p+1:] are already in place
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]   # swap by tuple assignment
                swapped = True
        if not swapped:                       # no swap: already sorted
            break


a = [8, 4, 7, 9, 3, 5, 1]
bubble_sort(a)
print(*a)                                     # 1 3 4 5 7 8 9
```

The range of the inner loop is determined by the invariant "when pass `pass` begins, `pass - 1` elements at the end are already in place": the first pass (`pass = 1`) compares $j = 0, \dots, n-2$, $n - 1$ comparisons, and each later pass has one fewer. Swapping two variables needs a temporary variable (`t = x; x = y; y = t;`), and `std::swap` does this for us.

In the worst case (reverse order) the number of comparisons is $(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}$, proportional to $n^2$; for an already sorted array a single pass with $n - 1$ comparisons suffices. Bubble sort swaps only adjacent elements that are out of order, and equal elements are never swapped, so it is stable: equal elements keep their original relative order after sorting. The growth of $n^2$ is already $5 \times 10^9$ comparisons at $n = 10^5$, so in practice one should use an $n \log n$ sorting algorithm ([4.1.11](/4.1.11)).

### 7.3.2. Sorting Strings

**Example 7.3.1** Sort the names of several contestants (in pinyin, without spaces) in lexicographic order.

With C-style strings, the list of names is a two-dimensional character array `char names[10][21]` (each name at most 20 characters, plus a terminator), comparison needs `strcmp`, and swapping two strings needs three `strcpy`s:

```cpp
if (std::strcmp(names[j], names[j + 1]) > 0) {   // names[j] comes later in the dictionary
    char t[21];
    std::strcpy(t, names[j]);
    std::strcpy(names[j], names[j + 1]);
    std::strcpy(names[j + 1], t);
}
```

With `std::vector<std::string>`, comparison and swapping are written just as for integers; going one step further, we can call the sorting function of the standard library directly:

```cpp tab
#include <algorithm>   // std::sort
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> names = {"zhangsan", "lisi", "wangwu", "zhaoliu", "qianjiu"};
    std::sort(names.begin(), names.end());   // ascending, lexicographic
    for (const auto& s : names) std::cout << s << ' ';
    std::cout << '\n';   // lisi qianjiu wangwu zhangsan zhaoliu
    return 0;
}
```

```python tab
names = ["zhangsan", "lisi", "wangwu", "zhaoliu", "qianjiu"]
names.sort()                 # in place; sorted(names) returns a new list
print(*names)                # lisi qianjiu wangwu zhangsan zhaoliu
```

`std::sort(first, last)` sorts the elements in the iterator range $[first, last)$ in ascending order by `<`, and `names.begin()`, `names.end()` denote the whole container; for a built-in array `int a[n]` write `std::sort(a, a + n)`. C++20 also allows `std::ranges::sort(names)`. `std::sort` needs only $O(n \log n)$ comparisons even in the worst case (usually implemented as introsort: quicksort as the main method, switching to heapsort when the recursion gets too deep and to insertion sort for small ranges), but it is not stable; use `std::stable_sort` when stability is needed.

### 7.3.3. Comparison Functions

The order of sorting need not be `<`. Pass `std::sort` a third argument, a comparison function `comp(x, y)`, which returns `true` when $x$ should come before $y$, and the sort proceeds in the order it defines.

**Example 7.3.2** Arrange students by total score from high to low; those with the same total score are arranged in lexicographic order of name.

```cpp tab
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using Student = std::pair<std::string, int>;     // (name, score)

// True if x should come before y: higher score first, then smaller name.
bool comes_before(const Student& x, const Student& y) {
    if (x.second != y.second) return x.second > y.second;
    return x.first < y.first;
}

int main() {
    std::vector<Student> s = {{"wang", 85}, {"li", 92}, {"zhao", 85}, {"chen", 92}};
    std::sort(s.begin(), s.end(), comes_before);
    for (const auto& [name, score] : s)          // structured binding (C++17)
        std::cout << name << ' ' << score << '\n';   // chen 92, li 92, wang 85, zhao 85
    return 0;
}
```

```python tab
s = [("wang", 85), ("li", 92), ("zhao", 85), ("chen", 92)]
s.sort(key=lambda t: (-t[1], t[0]))    # higher score first, then smaller name
for name, score in s:
    print(name, score)                 # chen 92, li 92, wang 85, zhao 85
```

Here `std::pair` puts the name and the score together; representing a record by a structure is the more general approach ([4.1.9](/4.1.9)). Comparison functions are also often written as lambda expressions, directly at the call site ([4.2.12](/4.2.12)).

A comparison function must define a *strict weak ordering*: for every $x$, `comp(x, x)` is false (irreflexive); `comp(x, y)` and `comp(y, x)` cannot both be true; it is transitive, and "incomparability" (both false) is also transitive. Intuitively, it must behave like `<` and not like `<=`: when two elements are "equal" it must return `false`. If a comparison function returns `true` on equal elements, the behavior of `std::sort` is undefined, and in practice it may access out of bounds and crash. When comparing several keys, compare key by key, comparing the next key only if the previous one is equal, and return `false` when all are equal, as in `comes_before` above.

The `sort` and `sorted` of Python do not accept a comparison function but a key function: compute a key for each element and then sort by the natural order of the keys. The key in the example above is the tuple `(-score, name)`; tuples are compared lexicographically, which gives exactly descending score first and then ascending name. `reverse=True` gives descending order. Python's sort (Timsort and its refinements) is stable, so multi-key sorting can also be done in several steps: first sort by the secondary key, then by the primary key.

## Summary

- A C-style string is a character array ending with `'\0'`; the functions of `<cstring>` do not check the destination space and easily cause buffer overflow; in C++ use `std::string`, and the Python `str` is an immutable sequence of code points.
- Strings are compared in lexicographic order. Unicode gives each character a code point, and UTF-8 encodes code points as 1 to 4 bytes; `size()` in C++ counts bytes, `len` in Python counts code points.
- C++ two-dimensional arrays are stored in row-major order, with `a[i][j]` at position $iC + j$; access in storage order is faster. Matrices of dynamic size use `vector<vector<T>>` or a one-dimensional `vector` with index computation; Python nested lists must create each row separately.
- Matrix multiplication is a triple loop, needing $n^3$ multiplications for square matrices of order $n$; real computation uses optimized libraries.
- Bubble sort compares and swaps adjacent elements, with $\frac{n(n-1)}{2}$ comparisons in the worst case, and is stable; in practice use `std::sort` ($O(n \log n)$, not stable) or `std::stable_sort`, and a comparison function for a custom order must be a strict weak ordering; Python uses `sorted` and key functions, and its sort is stable.
