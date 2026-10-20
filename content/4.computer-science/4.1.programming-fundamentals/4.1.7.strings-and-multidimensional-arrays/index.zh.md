---
title: 字符串与多维数组
description: C 风格字符串与结束符、<cstring> 的函数与缓冲区溢出；std::string 与 Python 的 str；字符编码与 UTF-8；二维数组的行主序存储与矩阵乘法；冒泡排序；字符串排序、std::sort 与比较函数、严格弱序；Python 的 sorted 与 key 函数。
---

上一章的数组存放的是数。本章讨论数组的两种重要推广：元素是字符的数组即字符串，它是程序处理文本的基础；元素本身又是数组的数组即多维数组，它表示矩阵和表格。最后讨论另一项与数组密不可分的基本操作：排序。排好序的数据才能二分查找（[4.1.6](/4.1.6)），排序也是许多算法的第一步。本章的冒泡排序是最简单的排序算法，更快的归并排序与快速排序见 [4.1.11](/4.1.11)，排序算法的系统分析见 [4.3.2](/4.3.2) 与 [4.3.14](/4.3.14)；字符串的流、格式化与正则表达式见 [4.2.11](/4.2.11)，字符串匹配算法见 [4.3.13](/4.3.13)。

## 7.1. 字符串

**定义 7.1.1（字符串）** **字符串**（string）是由零个或多个字符组成的有限序列。字符的个数称为字符串的长度，长度为零的字符串称为空串。

### 7.1.1. C 风格字符串

C 语言没有字符串类型，用字符数组存放字符串，并在最后一个字符之后放一个编码为 $0$ 的空字符 `'\0'` 作为结束标志。C++ 中写在双引号里的字符串常量（如 `"china"`）就是这种形式，`<cstring>` 中的函数和 `std::cout` 都依靠结束符判断字符串在哪里结束。

```cpp
char a[6] = "china";                     // 5 characters + '\0': needs 6 elements
char b[] = "china";                      // size deduced: 6
char c[5] = {'c', 'h', 'i', 'n', 'a'};   // no room for '\0': not a C string
// char d[4] = "china";                  // compile error in C++: too long
std::cout << sizeof(b) << ' ' << std::strlen(b) << '\n';   // 6 5
```

`sizeof` 给出数组的字节数（含结束符），`std::strlen` 从首字符起数到 `'\0'` 为止（不含结束符），它要逐个扫描，耗时与长度成正比。像 `c` 这样没有结束符的字符数组，用 `std::cout << c` 输出时会一直输出到内存中恰好出现的某个 $0$ 为止，后面跟着乱码，这已经是越界访问。

`<cstring>` 提供的常用函数：

| 函数 | 作用 | 注意 |
|---|---|---|
| `strlen(s)` | 长度 | |
| `strcpy(dst, src)` | 把 `src` 复制到 `dst` | `dst` 必须足够大 |
| `strcat(dst, src)` | 把 `src` 接到 `dst` 末尾 | `dst` 必须能容纳两者之和 |
| `strcmp(s, t)` | 按字典序比较 | 返回负数、$0$、正数，分别表示 `s` 小于、等于、大于 `t` |

这些函数都不知道目标数组有多大。`char name[8]; std::strcpy(name, "Tsinghua University");` 会写到数组之外，这称为缓冲区溢出（buffer overflow），它不仅使程序出错，还是历史上最常见的安全漏洞之一：攻击者可以构造过长的输入，改写栈上的返回地址（[4.1.4](/4.1.4) 的调用栈）。在 C++ 中应当使用 `std::string`；只有与 C 语言的接口打交道时才需要 C 风格字符串，此时 `s.c_str()` 能从 `std::string` 得到它。

### 7.1.2. std::string

`std::string`（`<string>`）自己管理存储空间，长度可以随意增长，并且支持用运算符进行赋值、拼接和比较：

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

比较运算符按字典序（lexicographic order）比较两个字符串：从第一个字符起逐个比较字符的编码，第一个不同的字符决定大小；若一个串是另一个的前缀，较短的串较小。因此 `"Zoo" < "apple"`（大写字母的编码小于小写字母），`"10" < "9"`（比较的是字符 `'1'` 与 `'9'`）。按数值比较要先转换为数。

`std::cin >> s` 读入一个"单词"，遇到空白就停止；读入包含空格的一整行用 `std::getline(std::cin, s)`。在 `std::cin >> n` 之后紧接着调用 `getline`，会读到 `n` 后面剩下的那个换行符而得到空行，需要先用 `std::cin.ignore()` 跳过它，或统一用 `getline` 读入每一行再自己转换。只读的字符串参数用 `const std::string&` 传递；C++17 的 `std::string_view` 可以不复制地引用字符串的一部分。

Python 的字符串 `str` 是不可变的：`s[0] = "b"` 是错误，`s += …`、`s.upper()` 都产生新的字符串。在循环中反复用 `+=` 拼接字符串可能很慢（每次都可能复制），应把片段放进列表，最后用 `"".join(parts)` 一次连接。Python 没有字符类型，`s[0]` 是长度为 1 的字符串；`ord("A")` 给出编码 $65$，`chr(65)` 反过来给出 `"A"`。

### 7.1.3. 字符编码与 Unicode

一个 `char` 是一个字节，只能表示 $256$ 种值，足够容纳 ASCII，却容纳不了汉字。现代程序普遍使用 Unicode：它为世界上各种文字的每个字符分配一个编号，称为码位（code point），如"清"是 U+6E05；码位再按某种**字符编码**存为字节，最常用的是 UTF-8：ASCII 字符占 1 个字节（与 ASCII 兼容），常用汉字占 3 个字节，表情符号等占 4 个字节（[3.5.1](/3.5.1)）。

```cpp tab
#include <iostream>
#include <string>

int main() {
    std::string s = "清华 THU";               // the source file is saved as UTF-8
    std::cout << s.size() << '\n';            // 10: bytes, not characters
    return 0;
}
```

```python tab
s = "清华 THU"
print(len(s))                    # 6: code points
print(len(s.encode("utf-8")))    # 10: bytes in UTF-8
print(hex(ord("清")))            # 0x6e05
```

C++ 的 `std::string` 只是一串字节，`size()` 数的是字节，`s[0]` 是"清"的三个字节中的第一个；按字符处理中文文本需要专门的库。Python 3 的 `str` 是码位的序列，`len` 数的是码位，只有在读写文件或网络时才需要指定编码（`open(path, encoding="utf-8")`、`s.encode()`、`b.decode()`）。源文件、终端和数据文件统一使用 UTF-8，可以避免绝大多数"乱码"问题。

### 7.1.4. 例：统计字母频率

**例 7.1.1** 读入一段英文文本，统计 26 个字母（不分大小写）各出现多少次。

用一个长度为 26 的计数数组，下标 $0 \sim 25$ 对应 `'a'` $\sim$ `'z'`：字母 `ch` 对应的下标是 `ch - 'a'`。这是 [4.1.6](/4.1.6) 中"下标代表数据本身"的思想的又一次应用，与筛法相同。

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

Python 中更自然的写法是用标准库的 `collections.Counter`，它是一个"值到次数"的字典（[4.2.10](/4.2.10)）；词频统计等更大的文本处理任务见 [4.1.9](/4.1.9)。

## 7.2. 多维数组

### 7.2.1. 二维数组

元素类型为 `T`、$R$ 行 $C$ 列的二维数组定义为 `T a[R][C]`，第 $i$ 行第 $j$ 列的元素是 `a[i][j]`（$0 \le i < R$，$0 \le j < C$）。C++ 把它理解为"$R$ 个元素的数组，每个元素是 $C$ 个 `T` 组成的数组"。

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

内存是一维的。C++ 按行存放二维数组：先存第 $0$ 行的全部元素，再存第 $1$ 行，依此类推，这称为行主序（row-major order）。因此 `a[i][j]` 的地址是 $p + (iC + j) \cdot \mathrm{sizeof}(T)$，其中 $p$ 是首地址。Fortran、MATLAB 和 R 则按列存放（列主序，column-major order）。存放顺序影响速度：按存放顺序访问（C++ 中让内层循环遍历列下标 $j$）时，相邻的访问落在相邻的内存中，能充分利用 CPU 的高速缓存（[4.10](/4.10)）。

内置二维数组的行数和列数都必须是编译时常量，作为函数参数时列数必须写明（`void f(int a[][4], int rows)`）。运行时才确定大小的矩阵，常用 `std::vector<std::vector<double>> a(rows, std::vector<double>(cols))`，它的每一行是一个独立的 `vector`；对性能要求高时，用一个长度为 $R \cdot C$ 的 `std::vector<double>`，自己按 `a[i * C + j]` 计算下标，所有元素连续存放。更高维的数组以此类推。

### 7.2.2. 矩阵乘法

$m \times n$ 矩阵 $A$ 与 $n \times p$ 矩阵 $B$ 的**矩阵乘法**给出 $m \times p$ 矩阵 $C$，$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$（[2.1](/2.1)）。直接写出每个 $c_{ij}$ 的表达式会得到大量相似的代码；观察到其中变化的只有 $i$、$j$、$k$ 三个下标，就得到三重循环：

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

结果矩阵的每个元素需要 $n$ 次乘法，总共 $mnp$ 次；两个 $n$ 阶方阵相乘需要 $n^3$ 次。三重循环的三种顺序在数学上等价，这里把 $k$ 放在中间、$j$ 放在最内层，使 `b[k][j]` 和 `c[i][j]` 都按行连续访问；在大矩阵上，这比按定义的 $i$-$j$-$k$ 顺序快数倍。实际计算中应使用高度优化的线性代数库（BLAS），Python 中即 NumPy 的 `a @ b`，它比上面的纯 Python 循环快几个数量级（[4.4.3](/4.4.3)）。

Python 用嵌套列表表示矩阵时有一个陷阱：`[[0.0] * p] * m` 不是 $m$ 个独立的行，而是同一个行列表的 $m$ 个引用（[4.1.6](/4.1.6)），修改 `c[0][0]` 会使每一行的第一个元素都改变。上面的代码用列表推导式为每一行创建新列表，避免了这个问题。

## 7.3. 排序

排序（sorting）是把一组元素按某种顺序（如从小到大）重新排列。

### 7.3.1. 冒泡排序

**算法 7.3.1（冒泡排序）** 冒泡排序（bubble sort，也称起泡排序）把长度为 $n$ 的数组 $a$ 按升序排列：从头到尾依次比较相邻的两个元素 $a[j]$ 与 $a[j+1]$，若 $a[j] > a[j+1]$ 就交换它们，这称为一趟。一趟之后，最大的元素被换到了末尾，如同气泡上浮；对前 $n - 1$ 个元素重复这一过程，依此类推，至多 $n - 1$ 趟后全部有序。若某一趟没有发生任何交换，数组已经有序，可以提前结束。

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

内层循环的范围由"第 `pass` 趟开始时，末尾已有 `pass - 1` 个元素就位"这一不变式决定：第一趟（`pass = 1`）比较 $j = 0, \dots, n-2$，共 $n - 1$ 次，以后每趟少一次。交换两个变量需要一个临时变量（`t = x; x = y; y = t;`），`std::swap` 替我们做了这件事。

最坏情况（逆序）下，比较次数为 $(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}$，与 $n^2$ 成正比；已经有序时只需一趟、$n - 1$ 次比较。冒泡排序只交换相邻的、顺序相反的元素，相等的元素不会交换，所以它是稳定的：相等元素排序后保持原来的相对次序。$n^2$ 的增长在 $n = 10^5$ 时已经是 $5 \times 10^9$ 次比较，实际中应使用 $n \log n$ 的排序算法（[4.1.11](/4.1.11)）。

### 7.3.2. 字符串排序

**例 7.3.1** 把若干选手的姓名（拼音，不含空格）按字典序排序。

用 C 风格字符串时，姓名表是一个二维字符数组 `char names[10][21]`（每个姓名至多 20 个字符，加一个结束符），比较要用 `strcmp`，交换两个字符串要用三次 `strcpy`：

```cpp
if (std::strcmp(names[j], names[j + 1]) > 0) {   // names[j] comes later in the dictionary
    char t[21];
    std::strcpy(t, names[j]);
    std::strcpy(names[j], names[j + 1]);
    std::strcpy(names[j + 1], t);
}
```

改用 `std::vector<std::string>`，比较和交换都与整数一样写；再进一步，直接调用标准库的排序函数：

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

`std::sort(first, last)` 对迭代器区间 $[first, last)$ 中的元素按 `<` 升序排序，`names.begin()`、`names.end()` 表示整个容器；对内置数组 `int a[n]` 写 `std::sort(a, a + n)`。C++20 还可以写 `std::ranges::sort(names)`。`std::sort` 在最坏情况下也只需 $O(n \log n)$ 次比较（通常用 introsort 实现：以快速排序为主，递归过深时改用堆排序，小区间用插入排序），但它不是稳定的；需要稳定时用 `std::stable_sort`。

### 7.3.3. 比较函数

排序的顺序不一定是 `<`。给 `std::sort` 传入第三个参数，即一个比较函数 `comp(x, y)`，它在 $x$ 应当排在 $y$ 之前时返回 `true`，排序就按它定义的顺序进行。

**例 7.3.2** 按总分从高到低排列学生；总分相同的，按姓名的字典序排列。

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

这里用 `std::pair` 把姓名和分数放在一起；用结构体表示一条记录是更一般的做法（[4.1.9](/4.1.9)）。比较函数也常写成 lambda 表达式，直接写在调用处（[4.2.12](/4.2.12)）。

比较函数必须定义一个严格弱序（strict weak ordering）：对任何 $x$，`comp(x, x)` 为假（非自反）；`comp(x, y)` 与 `comp(y, x)` 不能同时为真；它具有传递性，"不可比较"（两者都为假）也具有传递性。直观地说，它要像 `<` 而不能像 `<=`：两个元素"相等"时必须返回 `false`。若比较函数在相等时返回 `true`，`std::sort` 的行为是未定义的，实际中可能越界访问而崩溃。多关键字比较时逐个关键字比较，前一个关键字相等才比较下一个，最后全部相等时返回 `false`，如上面的 `comes_before`。

Python 的 `sort` 和 `sorted` 不接受比较函数，而是接受一个 key 函数：为每个元素计算一个键，再按键的自然顺序排序。上例的键是元组 `(-分数, 姓名)`，元组按字典序比较，正好先按分数降序、再按姓名升序。`reverse=True` 给出降序。Python 的排序（Timsort 及其改进）是稳定的，所以多关键字排序也可以分几次进行：先按次要关键字排序，再按主要关键字排序。

## 小结

- C 风格字符串是以 `'\0'` 结尾的字符数组，`<cstring>` 的函数不检查目标空间，容易造成缓冲区溢出；C++ 中使用 `std::string`，Python 的 `str` 是不可变的码位序列。
- 字符串按字典序比较。Unicode 给每个字符一个码位，UTF-8 把码位编码为 1～4 个字节；C++ 的 `size()` 数字节，Python 的 `len` 数码位。
- C++ 的二维数组按行主序存放，`a[i][j]` 位于第 $iC + j$ 个位置；按存放顺序访问更快。动态大小的矩阵用 `vector<vector<T>>` 或一维 `vector` 加下标计算；Python 的嵌套列表要为每行分别创建。
- 矩阵乘法是三重循环，$n$ 阶方阵需要 $n^3$ 次乘法；实际计算用优化的库。
- 冒泡排序比较交换相邻元素，最坏 $\frac{n(n-1)}{2}$ 次比较，稳定；实际中用 `std::sort`（$O(n \log n)$，不稳定）或 `std::stable_sort`，自定义顺序时比较函数必须是严格弱序；Python 用 `sorted` 与 key 函数，排序是稳定的。
