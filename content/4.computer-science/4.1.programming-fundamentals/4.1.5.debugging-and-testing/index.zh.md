---
title: 调试与测试
description: 程序错误的种类与编译器警告；重现、诊断、修复、反思的调试过程；输出调试；调试器的断点、条件断点、单步执行、观察变量与调用栈（GDB、VS Code、pdb）；AddressSanitizer 与 UBSan；测试用例、边界条件与差一错误、单元测试与对拍；防御性编程与断言。
---

写程序的时间，往往有一大半花在找错误上。调试（debugging）是找出并改正程序错误的过程，测试（testing）是通过运行程序来发现错误的过程：测试回答"有没有错"，调试回答"错在哪里"。本章介绍两者的方法和现行工具：先说明错误的种类和调试的一般过程，再介绍调试器、编译器警告和运行时检查工具，最后讨论怎样设计测试、怎样用断言让错误尽早暴露。本章的例子用到前四章的循环、函数和数组；数组越界、悬垂指针等内存错误的成因见 [4.1.8](/4.1.8)；测试在软件工程中的系统方法（测试框架、持续集成、覆盖率）见 [4.14](/4.14)；用 AI 工具辅助调试时，同样要靠本章的测试方法验证结果（[4.2.14](/4.2.14)）。

## 5.1. 错误的种类与调试过程

### 5.1.1. 让编译器帮忙

[4.1.1](/4.1.1) 把程序错误分为编译错误、运行时错误和逻辑错误。三者中，越早发现的越容易修正，所以第一条原则是：尽量让错误在编译时暴露。编译时始终打开警告：

```bash
g++ -std=c++20 -Wall -Wextra -g prog.cpp -o prog
```

警告不是可以忽略的提示，很多警告直接指向逻辑错误。例如：

```cpp
int sum = 0;
for (int i = 1; i <= 10; ++i);    // stray semicolon: the loop body is empty
    sum += i;                     // error: i is not declared here
if (sum = 0) { /* ... */ }        // assignment instead of comparison
```

GCC 对第二行报告"`'for' clause does not guard...` [-Wmisleading-indentation]"（若去掉第三行对 `i` 的引用，程序能编译，但循环什么也不做），对 `if (sum = 0)` 报告"suggest parentheses around assignment used as truth value [-Wparentheses]"。还可以加 `-Werror` 把警告当作错误，强迫自己处理每一条警告。

格式混乱也会掩盖错误。把 `return 0;` 误写在循环体里面、把输出"无解"的判断误写在循环内部，用自动格式化工具（clang-format）整理一下缩进，问题往往一目了然。读编译错误信息时从第一条读起，它给出了文件名、行号和原因；后面的错误常常是第一条引起的连锁反应。

### 5.1.2. 调试的一般过程

程序能运行但结果不对时，调试是一个实验科学的过程：

1. 重现：找到一个能稳定触发错误、而且尽量简单的输入。不能重现的错误几乎无法修正。
2. 诊断：根据现象提出假设（"可能是这一项算错了"），设计实验验证或否定它（输出这一项的值），逐步缩小错误所在的范围，直到找到原因。
3. 修复：改正错误，并用原来的输入确认错误消失，用其他输入确认没有引入新的错误。
4. 反思：这类错误为什么会发生，以后怎样避免；把这个输入加入测试（[5.4](#sec-5.4)）。

**例 5.1.1** 程序应当计算 $1 + \frac{1}{2 \cdot 2 + 1} = 1.2$，却输出了 `1`：

```cpp
double x = 1 + 1 / (2 * 2 + 1);
std::cout << x << '\n';            // prints 1
```

观察：输出恰好等于第一项，于是假设"第二项的值是 $0$"。实验：单独输出 `1 / (2 * 2 + 1)`，果然是 `0`；分母 `2 * 2 + 1` 是 `5` 没有错，再输出 `1 / 5`，仍是 `0`。结论：两个整数相除是整数除法（[4.1.2](/4.1.2)），把 `1` 改成 `1.0` 即可。反思：凡是含除法的表达式，都要想一想运算对象的类型。

诊断时最常用的二分思想：在程序中间检查一个中间结果，如果它已经错了，错误在前半段，否则在后半段，每次把可疑范围减半。

### 5.1.3. 输出调试

最简单的诊断工具是在程序中插入输出语句，打印变量的值或"执行到了这里"：

```cpp tab
#include <iostream>

int main() {
    int total = 0;
    for (int i = 1; i <= 5; ++i) {
        total += i * i;
        std::cerr << "[debug] line " << __LINE__ << ": i=" << i
                  << " total=" << total << '\n';   // goes to standard error
    }
    std::cout << total << '\n';
    return 0;
}
```

```python tab
total = 0
for i in range(1, 6):
    total += i * i
    print(f"[debug] {i=} {total=}")   # the = specifier prints the name and the value
print(total)
```

调试信息写到标准错误 `std::cerr`（Python 中可写 `print(..., file=sys.stderr)`），它与标准输出分开，不会混入程序的正式输出，在线评测也不会检查它。`__LINE__` 是当前行号（C++20 还有 `std::source_location`）。输出调试的缺点是要反复修改、重新编译程序，用完还要删掉；程序较复杂时，调试器更有效。正式的程序用日志（Python 标准库 `logging`）代替零散的输出语句，可以按级别打开或关闭。

## 5.2. 调试器

### 5.2.1. 断点、单步执行与观察

**定义 5.2.1（调试器）** **调试器**（debugger）是控制另一个程序的执行、使它在指定位置暂停，并在暂停时检查和修改其状态（变量的值、内存、调用栈）的程序。

调试器的基本操作：

- 断点（breakpoint）：程序执行到这一行之前暂停。条件断点只在指定条件成立时才暂停，如 `k >= 30`，适合循环执行很多次、只在某一次出错的情形。
- 单步执行：暂停后一次执行一行。"单步跳过"（step over）把当前行中的函数调用整个执行完；"单步进入"（step into）进入被调用的函数内部；"单步跳出"（step out）执行完当前函数，回到调用处。
- 继续：运行到下一个断点或程序结束。
- 观察：查看变量和表达式的当前值；监视点（watchpoint）在某个变量被修改时暂停，用来查"这个变量是被谁改掉的"。
- 调用栈：查看当前是怎样一层层调用到这里的（[4.1.4](/4.1.4)），并切换到某一层查看它的局部变量。

C++ 程序要用 `-g` 编译，可执行文件才含有源代码行号和变量名的信息；同时最好用 `-O0` 关闭优化，否则编译器重排或删除的代码会让单步执行显得跳来跳去。

| 操作 | GDB | VS Code | pdb |
|---|---|---|---|
| 启动 | `gdb ./prog`，`run` | F5 | `python -m pdb prog.py` |
| 设断点 | `break 9`、`break f` | 点击行号左侧，或 F9 | `b 9`、`b f`；代码中写 `breakpoint()` |
| 条件断点 | `break 9 if k >= 30` | 右击断点，编辑条件 | `b 9, k >= 30` |
| 单步跳过 / 进入 / 跳出 | `next` / `step` / `finish` | F10 / F11 / Shift+F11 | `n` / `s` / `r` |
| 继续 | `continue` | F5 | `c` |
| 查看值 | `print k` | 变量面板、悬停、监视面板 | `p k` |
| 调用栈 | `backtrace` | 调用堆栈面板 | `w` |

macOS 上的 Clang 工具链用 LLDB，命令与 GDB 类似（`b`、`r`、`n`、`s`、`bt`）。

### 5.2.2. 例：查找数组越界

**例 5.2.1** 下面的程序用筛法（[4.1.6](/4.1.6)）求 $30$ 以内的质数，运行时却可能输出不完整、陷入死循环或崩溃，表现随编译选项而变：

```cpp
#include <iostream>

int main() {
    const int N = 30;
    int composite[N] = {};              // composite[i] == 1 if i is composite
    for (int i = 2; i < N; ++i) {
        if (composite[i] == 0) {
            for (int k = 2 * i; k <= N; k += i)   // bug: k == N is out of bounds
                composite[k] = 1;
            std::cout << i << ' ';
        }
    }
    std::cout << '\n';
    return 0;
}
```

数组 `composite` 只有下标 $0 \sim 29$，而内层循环会写 `composite[30]`。越界写入是未定义行为：它可能改写了恰好位于数组之后的其他变量（比如 `i`），使程序的表现与源代码看起来毫不相关，这正是这类错误难查的原因。用 GDB 设置条件断点，在越界写入发生之前停下：

```text
$ g++ -std=c++20 -g -O0 sieve.cpp -o sieve
$ gdb ./sieve
(gdb) break 9 if k >= 30
Breakpoint 1 at ...: file sieve.cpp, line 9.
(gdb) run
Breakpoint 1, main () at sieve.cpp:9
9                       composite[k] = 1;
(gdb) print k
$1 = 30
(gdb) print i
$2 = 2
```

程序停在 `i = 2`、`k = 30` 处，正要写下标 $30$。原因是循环条件 `k <= N` 应为 `k < N`。在 VS Code 中做法相同：在第 9 行设断点并加上条件 `k >= 30`，按 F5 启动调试，停下后在变量面板中查看 `k` 和 `i`。调试器还能显示 `&composite[30]` 与 `&i` 等地址，验证越界写入改写了哪个变量（[4.1.8](/4.1.8)）。

### 5.2.3. 在 VS Code 中调试

VS Code 通过扩展支持调试：C++ 用 Microsoft 的 C/C++ 扩展（底层调用 GDB 或 LLDB）或 CodeLLDB 扩展，Python 用 Python 扩展（底层是 debugpy）。调试配置写在项目的 `.vscode/launch.json` 中，例如：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug C++",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/sieve",
      "args": ["30"],
      "cwd": "${workspaceFolder}",
      "MIMode": "gdb"
    },
    {
      "name": "Debug Python",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "args": ["30"],
      "console": "integratedTerminal"
    }
  ]
}
```

`args` 给出命令行参数（[5.5](#sec-5.5)），程序从标准输入读数据时，可以在终端中输入，或在 `args` 中用 `"<", "input.txt"` 重定向（视调试器而定）。C++ 程序需要先用 `-g` 编译好；也可以配置 `preLaunchTask`，在启动调试前自动编译。

### 5.2.4. Python 的 pdb

Python 标准库的调试器是 pdb。在代码中需要暂停的地方写一行 `breakpoint()`，运行到这里就进入 pdb 的交互界面；也可以用 `python -m pdb prog.py` 从头开始调试。程序因异常终止时，`python -m pdb -c continue prog.py` 会在出错处停下，让你查看当时的变量，这称为事后调试（post-mortem debugging）。pdb 中还可以直接输入任意 Python 表达式求值。Python 3.14 起还可以用 `python -m pdb -p <进程号>` 附加到一个正在运行的 Python 进程上。

Python 出错时打印的 traceback 本身就是重要的调试信息：它从外到内列出调用栈中的每一层（文件、行号、函数名），最后一行给出异常的类型和说明，如 `IndexError: list index out of range`。从最后一行读起，向上找到第一处属于自己代码的位置。

## 5.3. 运行时检查工具

C++ 的未定义行为（[4.1.2](/4.1.2)）不一定立即导致崩溃，错误可能在很久以后、很远的地方才表现出来。编译器提供的检查工具（sanitizer）在程序运行时检查这类错误，并在错误发生的那一刻报告：

- AddressSanitizer（`-fsanitize=address`）：检查数组越界、使用已释放的内存、内存泄漏等内存错误；
- UndefinedBehaviorSanitizer（`-fsanitize=undefined`）：检查有符号整数溢出、除以零、非法移位等。

用 `-fsanitize=address,undefined -g` 编译例 5.2.1 的程序并运行，程序在越界写入时立即停止，报告的开头是：

```text
==7870==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7c016d600098 ...
WRITE of size 4 at 0x7c016d600098 thread T0
    #0 ... in main sieve.cpp:9
  This frame has 1 object(s):
    [32, 152) 'composite' (line 5) <== Memory access at offset 152 overflows this variable
```

它指出了出错的行（第 9 行）、操作（写 4 字节）和被越界的变量（第 5 行定义的 `composite`，120 字节，即 30 个 `int`）。不加检查、用 `-O2` 编译时，同一个程序在这台机器上的表现则是 `*** stack smashing detected ***: terminated`，只知道栈被破坏了，不知道在哪里。

开发和测试时用 sanitizer 编译，发布时去掉（它会使程序变慢约 2 倍、占用更多内存）。在线评测中出现"运行时错误"或结果时对时错时，先在本地用 sanitizer 跑一遍测试数据。Linux 上的 Valgrind 也能检查内存错误，不需要重新编译，但慢得多。Python 中越界访问会抛出 `IndexError`、整数不会溢出，所以没有对应的问题，代价是每次访问都有检查开销。

## 5.4. 测试

### 5.4.1. 测试用例与边界条件

**定义 5.4.1（测试用例）** 一个**测试用例**（test case）由程序的一组输入和对应的预期输出组成。运行程序，比较实际输出与预期输出，不一致就说明程序有错误。

测试只能证明有错误，不能证明没有错误（Dijkstra）。可能的输入通常无穷多，测试用例要有代表性地选取：

- 等价类：把输入划分成若干类，同一类中的输入预期会被程序以相同的方式处理，每类选一个代表。例如判断闰年：不被 4 整除、被 4 整除但不被 100 整除、被 100 整除但不被 400 整除、被 400 整除，四类各选一个年份。
- 边界值：错误最常出现在边界上。取每类的边界和边界两侧的值：空输入、只有一个元素、最小值与最大值、恰好等于阈值、刚好溢出。
- 特殊情况：重复元素、负数与零、全部相同、已经有序或逆序。

最常见的边界错误是差一错误（off-by-one error）：循环多执行或少执行一次、下标多一或少一、`<` 与 `<=` 混淆。数组下标从 $0$ 到 $n-1$，长度为 $n$ 的区间 $[a, b)$ 包含 $b - a$ 个整数，$[a, b]$ 包含 $b - a + 1$ 个，这些都要在写循环时想清楚。

**例 5.4.1** 判断字符串是否为回文（正读反读都一样）。下面的实现有错误：

```cpp
bool is_palindrome(const std::string& s) {
    int n = s.size();
    for (int i = 0; i <= n / 2; ++i)
        if (s[i] != s[n - i]) return false;   // bug: should be s[n - 1 - i]
    return true;
}
```

用简单的例子手工检验："aba" 的长度 $n = 3$，$i = 0$ 时比较 `s[0]` 与 `s[3]`，而最后一个字符的下标是 $2$。正确的对称位置是 $n - 1 - i$。再看循环范围：要比较的是 $(0, n-1), (1, n-2), \dots$ 共 $\lfloor n/2 \rfloor$ 对，所以条件应为 `i < n / 2`；写成 `<=` 时，$n = 4$ 会多比较一次 `s[2]` 与 `s[1]`（结果虽然正确，却说明作者没有想清楚范围）。改正后的版本和它的测试见下一节。好的测试用例集应包括 `""`、`"a"`、`"ab"`、`"aa"`、`"aba"`、`"abba"`、`"abca"`：长度为 0、1、偶数、奇数，结果为真和为假的都有。

### 5.4.2. 单元测试与对拍

单元测试（unit testing）对程序中的每个函数单独测试。把测试写成代码，每次修改程序后重新运行全部测试，就能立即发现修改是否破坏了原有功能（回归）。最简单的写法是一个调用被测函数、用断言（[5.5](#sec-5.5)）检查结果的测试函数：

```cpp tab
#include <cassert>
#include <iostream>
#include <string>

bool is_palindrome(const std::string& s) {
    int n = static_cast<int>(s.size());
    for (int i = 0; i < n / 2; ++i)
        if (s[i] != s[n - 1 - i]) return false;
    return true;
}

void test_is_palindrome() {
    assert(is_palindrome(""));          // empty string
    assert(is_palindrome("a"));         // one character
    assert(!is_palindrome("ab"));       // even length, false
    assert(is_palindrome("aa"));        // even length, true
    assert(is_palindrome("aba"));       // odd length, true
    assert(is_palindrome("abba"));
    assert(!is_palindrome("abca"));
}

int main() {
    test_is_palindrome();
    std::cout << "all tests passed\n";
    return 0;
}
```

```python tab
import unittest


def is_palindrome(s: str) -> bool:
    n = len(s)
    return all(s[i] == s[n - 1 - i] for i in range(n // 2))


class TestIsPalindrome(unittest.TestCase):
    def test_short(self):
        self.assertTrue(is_palindrome(""))       # empty string
        self.assertTrue(is_palindrome("a"))      # one character
        self.assertFalse(is_palindrome("ab"))    # even length, false

    def test_longer(self):
        for s in ["aa", "aba", "abba"]:
            self.assertTrue(is_palindrome(s), s)
        self.assertFalse(is_palindrome("abca"))


if __name__ == "__main__":
    unittest.main()
```

实际项目中使用测试框架，它负责发现和运行所有测试、报告哪些失败：C++ 常用 GoogleTest、Catch2，Python 标准库有 `unittest`，社区中最常用的是第三方的 pytest（直接用 `assert` 写测试函数）。测试框架、覆盖率和持续集成见 [4.14](/4.14)。

另一种有效的方法是对拍（differential testing）：写一个简单、明显正确但可能很慢的参考实现，用大量随机生成的输入同时运行两个实现，比较结果是否一致。判断回文的参考实现就是"把字符串反转后与原串比较"：

```python
import random

for _ in range(10_000):
    s = "".join(random.choices("ab", k=random.randint(0, 8)))   # random short strings
    assert is_palindrome(s) == (s == s[::-1]), s                # compare with the reference
```

只用两个字母、长度很短的随机串，能高效地碰到各种边界情况。随机测试一旦发现不一致，它打印出的那个输入就是重现错误的最小例子。在线评测的训练中，对拍是查找"为什么只得部分分"最常用的手段：用枚举写参考解，再与优化后的解对比。

## 5.5. 防御性编程与断言

程序的输入不总是符合预期：用户可能输入字母而不是数字，可能少给一个命令行参数，文件可能不存在。防御性编程（defensive programming）的原则是对可能发生的意外情况预先作出处理：检查输入是否合法，出错时给出清楚的提示，而不是崩溃或输出错误的结果。

**例 5.5.1** 程序从命令行读入两个整数，输出它们的和（`./add 3 4` 输出 `7`）。`main` 的两个参数给出命令行参数：`argc` 是参数个数（包括程序名本身），`argv[i]` 是第 $i$ 个参数的字符串。不检查 `argc` 就访问 `argv[1]`，用户少给参数时程序就会崩溃。

```cpp tab
#include <exception>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc != 3) {                                   // check the number of arguments
        std::cerr << "usage: " << argv[0] << " a b\n";
        return 1;                                      // nonzero exit status: failure
    }
    try {
        int a = std::stoi(argv[1]), b = std::stoi(argv[2]);
        std::cout << a + b << '\n';
    } catch (const std::exception& e) {                // not an integer, or out of range
        std::cerr << "invalid integer: " << e.what() << '\n';
        return 1;
    }
    return 0;
}
```

```python tab
import sys


def main() -> int:
    if len(sys.argv) != 3:                             # check the number of arguments
        print(f"usage: {sys.argv[0]} a b", file=sys.stderr)
        return 1                                       # nonzero exit status: failure
    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
    except ValueError as e:                            # not an integer
        print(f"invalid integer: {e}", file=sys.stderr)
        return 1
    print(a + b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`std::stoi` 和 Python 的 `int` 在字符串不是合法整数时抛出异常，`try … catch`（Python 为 `try … except`）捕获异常并处理；异常机制在 [4.2](/4.2) 的有关章节中详细讨论。

对外部输入要检查并报告错误；对程序内部"按道理一定成立"的条件，则用断言。

**定义 5.5.1（断言）** **断言**（assertion）是程序员在程序某处写下的、认为在此处必然成立的条件。程序运行到断言时检查该条件：若成立则继续执行；若不成立，说明程序本身有错误，立即终止并报告断言所在的文件、行号和条件。

```cpp
#include <cassert>

int days_in_month(int y, int m) {
    assert(1 <= m && m <= 12);           // precondition: the caller must pass a valid month
    /* ... */
    return 31;
}

static_assert(sizeof(int) == 4, "this program assumes a 32-bit int");   // checked at compile time
```

断言常用于检查函数的前置条件（调用者应保证的条件）、后置条件（函数应保证的结果）和循环不变式（[4.1.3](/4.1.3)）。它把"错误的状态"变成"立即的、有位置信息的失败"，错误就在离原因最近的地方暴露出来，而不是在很远的地方以奇怪的结果出现。`assert` 只在调试时起作用：C++ 定义了宏 `NDEBUG` 时（发布版本的编译选项常含 `-DNDEBUG`），Python 用 `python -O` 运行时，断言被全部删去。因此：

- 断言用来发现程序员的错误，不能用来检查用户输入或文件内容，这些要用 `if` 判断并报告错误；
- 断言中的表达式不能有副作用，如 `assert(++count < 10)`，否则去掉断言后程序的行为就变了。

`static_assert` 在编译时检查只依赖常量的条件，不满足时编译失败，没有运行时的开销。

## 小结

- 打开编译器警告（`-Wall -Wextra`）并认真处理；用格式化工具整理缩进，让结构错误显形。
- 调试是重现、诊断、修复、反思的实验过程，用二分缩小可疑范围；输出调试写到标准错误。
- 调试器用断点（含条件断点）暂停程序，单步执行并观察变量和调用栈；C++ 用 `-g -O0` 编译，Python 用 `breakpoint()` 或 pdb。
- AddressSanitizer 与 UBSan 在越界、溢出等未定义行为发生的那一刻报告错误，开发时应当打开。
- 测试只能证明有错误：按等价类和边界值设计测试用例，警惕差一错误；把测试写成代码反复运行，用随机输入与参考实现对拍。
- 对外部输入做防御性检查，对内部必然成立的条件用断言；断言不能有副作用，也不能代替输入检查。
