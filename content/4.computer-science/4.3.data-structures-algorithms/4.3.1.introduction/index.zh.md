---
title: 绪论
description: 算法的要素与有穷性（Hailstone 序列）；图灵机与 RAM 计算模型；最坏情况的时间复杂度与空间复杂度；大 O、Ω、Θ 记号与复杂度的层次；级数与迭代的分析、封底估算；递归跟踪、递推方程、主定理与 Akra–Bazzi 定理；最大子段和的四种算法；Fibonacci 数列与最长公共子序列中的动态规划。
---

[4.1 程序设计基础](/4.1)讲的是怎样想出解法：递归、分治、回溯、动态规划。这门课程要回答的是另外两个问题：解法是否正确，代价有多大；以及怎样组织数据，使常用的操作都足够快。前一个问题需要一套与机器无关的度量尺度和分析工具，后一个问题就是各种数据结构。本章先说明算法与计算模型，再建立渐近记号这把"尺子"，然后介绍分析迭代与递归的基本方法，包括分治递推式的主定理，最后用最大子段和、Fibonacci 数列和最长公共子序列三个例子演示同一问题的算法怎样从指数级、立方级逐步改进到线性。以后各章（向量、列表、栈与队列、树、图、散列……）的每一个结论，都用这里的方法来证明。

## 1.1. 算法

### 1.1.1. 计算与算法

计算是借助某种工具、遵照一定的规则、以明确而机械的形式进行的信息处理。工具可以是绳子、尺规，也可以是电子计算机；把工具抽象成数学对象，就得到计算模型。**算法**（[4.1.1](/4.1.1)）是在特定计算模型下、为解决特定问题而设计的指令序列，它应当满足：

| 要素 | 含义 |
|---|---|
| 输入与输出 | 输入是待处理的信息（问题的实例），输出是处理的结果（答案） |
| 正确性 | 对每个合法输入，输出都是问题所要求的答案 |
| 确定性 | 由明确的基本操作组成，没有"加盐少许""煮至半熟"之类的含糊步骤 |
| 可行性 | 每个基本操作都能实现，并且在常数时间内完成 |
| 有穷性 | 对任何输入，经有穷次基本操作后都能得到输出 |

其中最不起眼、却最难验证的是有穷性。

**例 1.1.1（Hailstone 序列）** 对正整数 $n$，若 $n$ 为偶数则变为 $n/2$，若为奇数则变为 $3n + 1$，重复这一过程直到 $n = 1$。所得序列称为 Hailstone 序列，例如 $7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1$，长度为 17。

```cpp tab
#include <format>
#include <iostream>

// Length of the hailstone (Collatz) sequence that starts at n.
int hailstone(unsigned long long n) {
    int length = 1;
    while (n > 1) {
        n = (n % 2 == 1) ? 3 * n + 1 : n / 2;
        ++length;
    }
    return length;
}

int main() {
    for (unsigned long long n : {7ULL, 27ULL, 97ULL})
        std::cout << std::format("|Hailstone({})| = {}\n", n, hailstone(n));
}
```

```python tab
def hailstone(n: int) -> int:
    """Length of the hailstone (Collatz) sequence that starts at n."""
    length = 1
    while n > 1:
        n = 3 * n + 1 if n % 2 == 1 else n // 2
        length += 1
    return length

for n in (7, 27, 97):
    print(f"|Hailstone({n})| = {hailstone(n)}")
```

序列的长度与 $n$ 的大小没有简单的关系：$|\mathrm{Hailstone}(27)| = 112$，而 $|\mathrm{Hailstone}(32)| = 6$。这段程序对每个 $n$ 都会终止吗？这就是 Collatz 猜想，至今未被证明（已经用计算机验证到 $2^{68}$ 左右），Erdős 评论说"数学还没有准备好解决这类问题"。因此，在猜想被证明之前，`hailstone()` 只能称为程序，不能称为算法：程序未必满足有穷性。

**例 1.1.2** 设 `rand()` 是理想的随机数发生器，循环 `while (rand() & 1);` 每轮以概率 $1/2$ 继续。它在理论上可能运行任意多轮，但轮数服从**几何分布**，**数学期望**只有 2 轮，运行无穷多轮的概率为 0。随机算法的有穷性要在概率意义下理解。

### 1.1.2. 好算法

正确只是最低要求。一个好的算法还应当健壮（能辨别不合法的输入并做适当处理，而不是非正常退出）、可读（结构化、准确命名、必要的注释），而最受关注的是效率：速度尽可能快，存储空间尽可能少。正确性本身也分层次：能处理简单的输入，能处理大规模的输入，能处理一般的输入，能处理退化的输入（空序列、全部相等的元素……），直至能处理任意合法的输入。

Wirth 说"算法 + 数据结构 = 程序"。数据结构（data structure）是数据元素的组织方式连同在其上实现的一组操作；同一组数据组织得不同，各种操作的代价也就不同。算法要在合适的数据结构上才能高效，而数据结构的价值也只能通过它所支持的算法来衡量。这门课程的主题，可以概括为"（算法 + 数据结构）× 效率 = 计算"。

## 1.2. 计算模型

### 1.2.1. 问题规模与最坏情况

要比较算法的优劣，先要能度量成本。记 $T_A(P)$ 为算法 $A$ 求解问题实例 $P$ 的成本。问题的实例太多，不可能逐一列出；经验表明，实例的规模往往是决定成本的最主要因素，规模相近的实例成本也相近。于是改用规模 $n$ 的函数来描述成本。但规模相同的实例成本仍可能相差悬殊：在平面上 $n$ 个点构成的 $\binom{n}{3}$ 个三角形中判断是否有面积不超过 5 的，运气好时第一个就是，运气差时要枚举全部。稳妥起见，只看最坏者。

**定义 1.2.1（时间复杂度）** 设 $T_A(P)$ 为算法 $A$ 求解实例 $P$ 所需执行的基本操作次数，称

$$
T_A(n) = \max\{\, T_A(P) : P \text{ 的规模为 } n \,\}
$$
为算法 $A$ 的（最坏情况）**时间复杂度**，讨论特定算法时简记为 $T(n)$。类似地可以定义最好情况与平均情况（对实例的某个概率分布取期望）的复杂度。

只用实验来比较算法是不够的：不同算法可能适应于不同规模、不同类型的输入；同一算法可能由不同的程序员、用不同的语言和编译器、在不同的体系结构和操作系统上实现。为了得到客观的结论，需要一个与这些因素都无关的理想平台，也就是计算模型。

### 1.2.2. 图灵机

图灵机（Turing machine）由四部分组成：一条两端无限、均匀划分为单元格的纸带，每格存有有限字母表中的一个字符（初始为 `#`）；一个读写头，总是对准某一格，可以读取或改写其中的字符，每个节拍可以移到左侧或右侧的邻格；一个控制器，总处于有限种状态之一，约定 `h` 为停机状态；以及一张转移函数表。转移函数的每一条写作 $(q, c;\ d, \mathrm{L}/\mathrm{R}, p)$：若当前状态为 $q$、当前字符为 $c$，则把字符改写为 $d$，左移或右移一格，转入状态 $p$。从启动到停机经历的节拍数，就是计算的成本。

**例 1.2.1（二进制加一）** 读写头位于二进制数的最低位，状态为 `<`。加一的原理是：末尾连续的 1 全部翻转为 0，紧邻它们的那个 0（或空白 `#`）翻转为 1。

| 转移 | 作用 |
|---|---|
| $(\texttt{<}, 1;\ 0, \mathrm{L}, \texttt{<})$ | 进位：1 变 0，继续左行 |
| $(\texttt{<}, 0;\ 1, \mathrm{R}, \texttt{>})$ | 进位被吸收：0 变 1，掉头 |
| $(\texttt{<}, \#;\ 1, \mathrm{R}, \texttt{>})$ | 原数全为 1：在最高位之前写一个 1 |
| $(\texttt{>}, 0;\ 0, \mathrm{R}, \texttt{>})$ | 右行回到最低位 |
| $(\texttt{>}, \#;\ \#, \mathrm{L}, \texttt{h})$ | 越过最低位后退回一格，停机 |

第三条不能省略，否则 $111$ 这样的输入无法处理。

```cpp tab
#include <format>
#include <iostream>
#include <map>
#include <string>
#include <utility>

// One rule (q, c; d, L/R, p): in state q reading c, write d, move, enter p.
struct Rule { char write; int move; char next; };

int main() {
    const std::map<std::pair<char, char>, Rule> delta{
        {{'<', '1'}, {'0', -1, '<'}},   // carry: 1 -> 0, keep moving left
        {{'<', '0'}, {'1', +1, '>'}},   // absorb the carry: 0 -> 1, turn back
        {{'<', '#'}, {'1', +1, '>'}},   // all ones so far: write a new leading 1
        {{'>', '0'}, {'0', +1, '>'}},   // walk back to the right end
        {{'>', '#'}, {'#', -1, 'h'}},   // stop on the lowest bit
    };
    std::string tape = "##10111##";
    int head = 6;                      // on the lowest bit
    char state = '<';
    int steps = 0;
    while (state != 'h') {
        const Rule& r = delta.at({state, tape[head]});
        tape[head] = r.write;
        head += r.move;
        state = r.next;
        ++steps;
    }
    std::cout << std::format("tape = {}, steps = {}\n", tape, steps);  // ##11000## 8
}
```

```python tab
# delta[(q, c)] = (d, move, p): in state q reading c, write d, move, enter p.
delta = {
    ("<", "1"): ("0", -1, "<"),   # carry: 1 -> 0, keep moving left
    ("<", "0"): ("1", +1, ">"),   # absorb the carry: 0 -> 1, turn back
    ("<", "#"): ("1", +1, ">"),   # all ones so far: write a new leading 1
    (">", "0"): ("0", +1, ">"),   # walk back to the right end
    (">", "#"): ("#", -1, "h"),   # stop on the lowest bit
}
tape = list("##10111##")
head, state, steps = 6, "<", 0     # the head starts on the lowest bit
while state != "h":
    tape[head], move, state = delta[(state, tape[head])]
    head += move
    steps += 1
print(f"tape = {''.join(tape)}, steps = {steps}")   # ##11000## 8
```

转移函数表就是这台机器的"程序"，它与输入纸带之间的约定（读写头从哪里开始、停在哪里）就是接口。图灵机的意义在于理论：可计算性（什么问题能用算法解决）和复杂度类都以它为基准定义。

### 1.2.3. RAM 模型

图灵机只能逐格移动，访问远处的数据要付出与距离成正比的代价，这与真实计算机相去甚远。分析算法更常用随机存取机（random-access machine）：

- 有无限多个顺序编号的寄存器 $R[0], R[1], \dots$，可以通过编号直接访问任意一个（"循秩访问"）；
- 指令寄存器 IR 指示当前执行哪条指令；
- 基本操作只有赋值、加减乘除、比较、条件与无条件跳转等少数几种，每种都只需常数时间。

**例 1.2.2（向上取整的除法）** 求 $\lceil c/d \rceil$（$c \geq 0$，$d > 0$）：反复从 $R[0] = c$ 中减去 $R[1] = d$，统计减到不大于 0 之前所做的减法次数。

```text
[0] R[3] <- 1              // constant 1
[1] GOTO 4                 // in case R[0] = c == 0
[2] R[2] <- R[2] + R[3]    // x++
[3] R[0] <- R[0] - R[1]    // c -= d
[4] IF R[0] > 0 GOTO 2     // if c > 0 goto 2
[5] R[0] <- R[2]           // else copy x to R[0]
[6] STOP                   // return R[0] = x = ceil(c / d)
```

$c = 12$、$d = 5$ 时共执行 14 条指令，结果为 3。一般地，时间成本是各条指令执行次数的总和，这里为 $3\lceil c/d \rceil + 5$。

在 RAM 模型中，算法的运行时间就是它执行的基本操作次数。高级语言中的一条语句（算术运算、比较、赋值、下标访问、函数调用与返回）都等效于常数条 RAM 指令；分支、循环和递归调用本质上都是跳转。因此在渐近的意义下，可以直接按高级语言的语句计数，不必真的翻译成 RAM 指令。

严格地说，"每个寄存器存放任意大的整数、运算只需常数时间"会让模型过于强大（可以把整个输入编码进一个整数）。现代教材采用字 RAM（word RAM）：每个字有 $w \geq \log_2 n$ 位，字长内的运算是常数时间。本课程默认这一模型：下标、指针、普通整数的运算都是 $O(1)$。

## 1.3. 渐近复杂度

### 1.3.1. 大 O 记号

精确的 $T(n)$ 既难求，也不重要：真正关心的是规模足够大以后，成本随规模增长的趋势。这就是渐近分析。渐近记号（asymptotic notation）忽略常数因子和低阶项，只保留增长的阶。

**定义 1.3.1（大 O 记号）** 设 $f, g$ 是定义在正整数上、最终取正值的函数。若存在常数 $c > 0$ 和 $n_0$，使得对所有 $n \geq n_0$ 都有 $f(n) \leq c \cdot g(n)$，则记 $f(n) = O(g(n))$。这种记号称为**大 O 记号**，它给出 $f$ 增长速度的渐近上界。

**定义 1.3.2（大 Ω 记号与大 Θ 记号）** 若存在 $c > 0$ 和 $n_0$，使得对所有 $n \geq n_0$ 都有 $f(n) \geq c \cdot g(n)$，则记 $f(n) = \Omega(g(n))$（**大 Ω 记号**，渐近下界）；若 $f(n) = O(g(n))$ 且 $f(n) = \Omega(g(n))$，则记 $f(n) = \Theta(g(n))$（**大 Θ 记号**，渐近确界）。

例如 $T(n) = 3n^2 + 10n + 7$：取 $c = 4$、$n_0 = 11$ 得 $T(n) = O(n^2)$；又 $T(n) \geq 3n^2$，故 $T(n) = \Theta(n^2)$。这里的"$=$"是约定俗成的写法，确切的含义是 $f$ 属于集合 $O(g) = \{f : \exists c, n_0,\ \forall n \geq n_0,\ f(n) \leq c\,g(n)\}$，所以 $O(n) = O(n^2)$ 成立，而反过来写就是错的。另有严格的版本：$f = o(g)$ 表示 $f(n)/g(n) \to 0$，$f = \omega(g)$ 表示 $f(n)/g(n) \to \infty$。

由定义可以直接得到以下运算规则，分析时反复使用：

- 常数因子可以忽略：$O(c \cdot f) = O(f)$；
- 加法取较大者：$O(f) + O(g) = O(\max(f, g))$，因此多项式只看最高次项；
- 乘法相乘：$O(f) \cdot O(g) = O(f \cdot g)$，用于嵌套的循环；
- 传递性：$f = O(g)$、$g = O(h)$ 推出 $f = O(h)$。

一个"$O(n^2)$ 的算法"通常指其最坏情况时间复杂度为 $O(n^2)$；当这个上界是紧的、即最坏情况确实需要 $\Theta(n^2)$ 时，更准确的说法是 $\Theta(n^2)$。$\Omega$ 主要用于叙述问题的下界：无论采用什么算法，最坏情况都至少需要多少时间（[4.3.2](/4.3.2) 将证明基于比较的排序需要 $\Omega(n \log n)$ 次比较）。

**定义 1.3.3（空间复杂度）** 算法在执行过程中，除输入数据本身所占的空间之外所需的存储空间量，称为算法的**空间复杂度**，记为 $S(n)$，同样取最坏情况并用渐近记号描述。可以重复使用的空间只计一次。

在 RAM 模型中，每使用一个存储单元至少要执行一次写入，所以除去一次性申请而从未访问的空间，总有 $S(n) = O(T(n))$。这也是通常只讨论时间复杂度的原因；但对递归算法（递归深度决定栈空间，[4.3.4](/4.3.4)）和需要辅助数组的算法（如**归并排序**），空间复杂度同样重要。

### 1.3.2. 复杂度的层次

常数 $O(1)$ 的算法效率最高，而常数时间的代码段不一定不含循环、分支或调用：

```cpp
for (i = 0; i < n; i += n / 2024 + 1);     // about 2024 iterations: O(1)
for (i = 1; i < n; i = 1 << i);            // log* n iterations: almost O(1)
if ((n + m) * (n + m) < 4 * n * m) goto UNREACHABLE;   // never taken (ignoring overflow)
```

第一个循环的步长随 $n$ 增长，迭代次数不超过 2025；第三个条件永不成立，因为 $(n+m)^2 \geq 4nm$。要看的是执行次数，而不是代码的形状。

再看对数 $O(\log n)$。对数的底数无所谓：$\log_a n = \log_b n / \log_b a$，相差的只是常数因子，所以写 $O(\log n)$ 时不注明底数（本课程中 $\log$ 不注明底数时默认为 2）；常数次幂也无所谓：$\log n^c = c \log n = O(\log n)$。对数的多项式 $\log^c n$ 仍然比任何正幂次增长得慢：对任意 $c > 0$ 和 $\varepsilon > 0$，$\log^c n = o(n^\varepsilon)$。这类算法极其高效，例如有序向量的**二分查找**。

多项式 $O(n^c)$ 之中，$O(n)$ 称为线性，是许多问题的理想目标（读入输入就需要线性时间）；从 $O(n)$ 到 $O(n^2)$ 是本课程编程习题主要覆盖的范围。存在多项式时间算法的问题类记为 $\mathrm{P}$，按 Cobham 与 Edmonds 的观点，多项式时间是"可以有效计算"的标准。

指数 $O(2^n)$ 则不同：对任意 $c > 0$ 与 $a > 1$，$n^c = o(a^n)$，指数级的成本增长极快，通常被认为不可忍受。从多项式到指数，是从有效算法到无效算法的分水岭。许多问题的指数算法显而易见，设计多项式算法却极其困难。

**例 1.3.1（子集和问题）** 给定正整数集合 $S = \{a_1, \dots, a_n\}$ 与目标 $t$，问是否存在和恰为 $t$ 的子集。例如两位候选人竞争选举人团的 538 票，会不会恰好各得 269 票。按最后一个元素取或不取分类，直接递归：

```cpp tab
#include <format>
#include <iostream>
#include <span>

// Is there a subset of the positive integers s whose sum is exactly t?
bool subset_sum(std::span<const int> s, long long t) {
    if (t == 0) return true;               // the empty subset
    if (s.empty() || t < 0) return false;
    auto rest = s.first(s.size() - 1);     // classify by the last element:
    return subset_sum(rest, t) || subset_sum(rest, t - s.back());   // skip it or take it
}

int main() {
    int s[] = {3, 34, 4, 12, 5, 2};
    std::cout << std::format("{} {}\n", subset_sum(s, 9), subset_sum(s, 30));   // true false
}
```

```python tab
def subset_sum(s: list[int], t: int, n: int | None = None) -> bool:
    """Is there a subset of the positive integers s[:n] whose sum is exactly t?"""
    if n is None:
        n = len(s)
    if t == 0:
        return True                        # the empty subset
    if n == 0 or t < 0:
        return False
    # classify by the last element: skip it or take it
    return subset_sum(s, t, n - 1) or subset_sum(s, t - s[n - 1], n - 1)

s = [3, 34, 4, 12, 5, 2]
print(subset_sum(s, 9), subset_sum(s, 30))   # True False
```

最坏情况下它要检视全部 $2^n$ 个子集。子集和问题是 NP 完全的：若它有多项式时间算法，则所有 NP 问题（解可以在多项式时间内验证的问题）都有，即 $\mathrm{P} = \mathrm{NP}$。这一猜想至今悬而未决，人们普遍相信 $\mathrm{P} \neq \mathrm{NP}$，但目前没有人能证明子集和问题不存在多项式算法。另外要注意，用**动态规划**可以在 $O(nt)$ 时间内求解，但这不是多项式时间：输入中 $t$ 只占 $\log t$ 位，$O(nt)$ 关于输入长度是指数的（称为伪多项式时间）。

下图是常见函数的增长曲线。规模很小时，低阶的函数未必更小（$n \leq 4$ 时 $2^n \leq n^2$）；规模稍大，增长的阶就起决定作用，即"先胖不算胖，路遥知马力"。

![常见复杂度函数的增长：左图规模很小，右图规模稍大](./plots/growth-rates.py)

| 复杂度 | 名称 | 典型的例子 |
|---|---|---|
| $O(1)$ | 常数 | 数据结构的基本操作（向量的循秩访问、栈的压入与弹出） |
| $O(\log^* n)$ | 迭代对数 | 近乎常数；并查集的复杂度用增长更慢的反 Ackermann 函数表达（[4.3.11](/4.3.11)） |
| $O(\log n)$ | 对数 | 有序向量的二分查找，平衡搜索树、堆的查找、插入与删除 |
| $O(n)$ | 线性 | 顺序查找，树与图的遍历 |
| $O(n \log n)$ | 线性对数 | 排序，Huffman 编码 |
| $O(n^2)$ | 平方 | 输入对象两两组合，朴素的 Dijkstra 算法 |
| $O(n^3)$ | 立方 | 朴素的矩阵乘法 |
| $O(n^c)$ | 多项式 | P 类问题 |
| $O(2^n)$ | 指数 | 许多问题的平凡算法（枚举全部子集） |

其中 $\log^* n$ 是对 $n$ 反复取 $\log_2$、直到结果不超过 1 所需的次数：$\log^* 2^{65536} = 5$，而 $2^{65536}$ 远远超过宇宙中原子的总数。

## 1.4. 迭代的分析

### 1.4.1. 级数

迭代算法的复杂度通常归结为级数求和。以下几类最常用：

| 级数 | 结论 | 说明 |
|---|---|---|
| 算术级数 $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ | $\Theta(n^2)$ | 与末项的平方同阶 |
| 幂方级数 $\sum_{k=1}^{n} k^d$ | $\Theta(n^{d+1})$ | 比幂次高出一阶 |
| 几何级数 $\sum_{k=0}^{n} a^k = \frac{a^{n+1} - 1}{a - 1}$（$a > 1$） | $\Theta(a^n)$ | 与末项同阶 |
| 收敛级数，如 $\sum_{k=1}^{n} \frac{1}{k^2} < \frac{\pi^2}{6}$ | $O(1)$ | |
| **调和级数** $H_n = \sum_{k=1}^{n} \frac{1}{k}$ | $\ln n + \gamma + o(1) = \Theta(\log n)$ | $\gamma \approx 0.5772$ |
| 对数级数 $\sum_{k=1}^{n} \log k = \log n!$ | $\Theta(n \log n)$ | 由 Stirling 公式 |
| $\sum_{k=1}^{n} k \cdot 2^k = (n-1)2^{n+1} + 2$ | $\Theta(n \, 2^n)$ | |

幂方级数的阶可以用积分夹逼：$\int_0^n x^d \,\mathrm{d}x \leq \sum_{k=1}^n k^d \leq \int_1^{n+1} x^d\,\mathrm{d}x$，两端都是 $\Theta(n^{d+1})$。对数级数的上界 $\log n! \leq n \log n$ 显然；下界取后一半的项：$\log n! \geq \sum_{k > n/2} \log k \geq \frac{n}{2}\log\frac{n}{2} = \Omega(n \log n)$。

收敛级数也有意义：基本操作的次数是整数，但它们的期望或分摊值可以是分数。例 1.1.2 的循环期望执行 $\sum_{k \geq 1} k \cdot 2^{-k} = 2$ 轮，就是一个收敛级数。

### 1.4.2. 循环

循环的次数往往直接对应一个级数。设 `O1op` 表示一个常数时间的操作：

| 循环 | 执行次数 | 复杂度 |
|---|---|---|
| `for (i = 0; i < n; i++)` `for (j = 0; j < n; j++) O1op;` | $n^2$ | $\Theta(n^2)$ |
| `for (i = 0; i < n; i++)` `for (j = 0; j < i; j++) O1op;` | $\sum_{i} i = \frac{n(n-1)}{2}$ | $\Theta(n^2)$ |
| `for (i = 0; i < n; i++)` `for (j = 0; j < i; j += 2024) O1op;` | $\sum_i \lceil i/2024 \rceil$ | $\Theta(n^2)$ |
| `for (i = 1; i < n; i <<= 1)` `for (j = 0; j < i; j++) O1op;` | $1 + 2 + 4 + \cdots < 2n$ | $\Theta(n)$ |
| `for (i = 0; i <= n; i++)` `for (j = 1; j < i; j += j) O1op;` | $\sum_{i} \lceil \log_2 i \rceil$ | $\Theta(n \log n)$ |

第二行的内循环次数构成算术级数，几何上是正方形的一半，仍是 $\Theta(n^2)$；第三行内循环的步长虽大，只改变常数因子；第四行外循环只有 $\log n$ 轮，但内循环次数构成几何级数，总数由最后一项主导；第五行内循环的 $j$ 倍增，每轮 $\Theta(\log i)$ 次，总数是对数级数。

### 1.4.3. 封底估算

有了渐近复杂度，就可以在动手实现之前粗略估计运行时间，即封底估算（back-of-the-envelope calculation）。几个常用的量级：一天约 $10^5$ 秒（86400），一年约 $3 \times 10^7$ 秒，一个世纪约 $3 \times 10^9$ 秒，宇宙大爆炸至今约 $4 \times 10^{17}$ 秒；一台普通计算机每秒约执行 $10^9$ 条简单指令，2020 年代的 E 级超级计算机每秒约执行 $10^{18}$ 次浮点运算。

**例 1.4.1** 对全国人口普查数据（$n \approx 10^9$）排序。用 $\Theta(n^2)$ 的**冒泡排序**约需 $10^{18}$ 次操作，普通计算机要算 $10^9$ 秒，即 30 余年；用 $\Theta(n \log n)$ 的归并排序约需 $10^9 \times 30 = 3 \times 10^{10}$ 次操作，普通计算机半分钟即可完成。算法的改进胜过硬件的提升：把冒泡排序搬到快 $10^9$ 倍的 E 级超级计算机上（并假设它能完美地并行），也要约 1 秒，硬件上 $10^9$ 倍的差距才勉强抵消了 $n^2$ 与 $n \log n$ 之间的差距。

## 1.5. 递归的分析

### 1.5.1. 减而治之：递归跟踪与递推方程

**减治**（[4.1.10](/4.1.10)）把问题划分为两个子问题，其一平凡，另一个规模缩减。以数组求和为例：$n$ 个数的和等于前 $n - 1$ 个数的和加上最后一个数。

```cpp tab
#include <format>
#include <iostream>
#include <span>
#include <utility>

// Linear recursion: sum(a) = sum(a without its last element) + last element.
long long sum(std::span<const int> a) {
    return a.empty() ? 0 : sum(a.first(a.size() - 1)) + a.back();
}

// Decrease and conquer again: swap the two ends, then reverse the middle.
void reverse(std::span<int> a) {
    if (a.size() < 2) return;
    std::swap(a.front(), a.back());
    reverse(a.subspan(1, a.size() - 2));
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    reverse(a);
    std::cout << std::format("sum = {}, a =", sum(a));
    for (int x : a) std::cout << std::format(" {}", x);
    std::cout << '\n';
}
```

```python tab
def total(a: list[int], n: int) -> int:
    """Linear recursion: the sum of a[:n] is the sum of a[:n-1] plus a[n-1]."""
    return 0 if n == 0 else total(a, n - 1) + a[n - 1]

def reverse(a: list[int], lo: int, hi: int) -> None:
    """Reverse a[lo:hi]: swap the two ends, then reverse the middle."""
    if hi - lo < 2:
        return
    a[lo], a[hi - 1] = a[hi - 1], a[lo]
    reverse(a, lo + 1, hi - 1)

a = [1, 2, 3, 4, 5, 6, 7]
reverse(a, 0, len(a))
print(f"sum = {total(a, len(a))}, a = {a}")
```

分析递归算法有两种方法。

1. 递归跟踪（recursion trace）：画出计算过程中出现过的所有递归实例及其调用关系，它们各自所需时间（不计递归调用本身）的总和就是总的运行时间。求和的例子共有 $n + 1$ 个递归实例，每个只需 $O(1)$ 时间，总时间为 $O(n)$。
2. 递推方程（recurrence relation）：规模较大、结构较复杂时，递归跟踪不再直观，改用递推式描述成本。为求 `sum` 的规模为 $n$ 的问题，要先解规模为 $n - 1$ 的问题，再做一次加法：

$$
T(n) = T(n - 1) + O(1), \qquad T(0) = O(1),
$$
展开即得 $T(n) = O(n)$。

求和与倒置都是线性递归：每个递归实例至多调用自身一次。它们的空间复杂度也是 $O(n)$，因为递归深度为 $n$，**调用栈**上同时存在 $n$ 个栈帧。倒置的递归调用是函数的最后一步（尾递归），可以机械地改写为循环，空间降为 $O(1)$（[4.3.4](/4.3.4)）。

### 1.5.2. 分而治之

**分治**（[4.1.11](/4.1.11)）把问题划分为若干个（通常两个、规模大体相当的）子问题，分别求解后合并。数组求和也可以分治：把区间 $[\mathit{lo}, \mathit{hi})$ 从中点 $\mathit{mi}$ 切开，两半分别求和再相加。

```cpp tab
#include <format>
#include <iostream>
#include <span>

// Binary recursion on a nonempty span: split at the middle, add the two sums.
long long sum(std::span<const int> a) {
    if (a.size() == 1) return a[0];
    std::size_t mi = a.size() / 2;
    return sum(a.first(mi)) + sum(a.subspan(mi));
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8};
    std::cout << std::format("{}\n", sum(a));   // 36
}
```

```python tab
def total(a: list[int], lo: int, hi: int) -> int:
    """Binary recursion on a nonempty a[lo:hi]: split at the middle, add the two sums."""
    if hi - lo == 1:
        return a[lo]
    mi = (lo + hi) // 2
    return total(a, lo, mi) + total(a, mi, hi)

print(total([1, 2, 3, 4, 5, 6, 7, 8], 0, 8))   # 36
```

递归跟踪：设 $n = 2^m$，递归树的第 $k$ 层有 $2^k$ 个实例，每个 $O(1)$，总时间为几何级数 $1 + 2 + \cdots + 2^m = 2n - 1 = O(n)$。递推方程为

$$
T(n) = 2T(n/2) + O(1), \qquad T(1) = O(1),
$$
令 $S(n) = T(n) + c$ 可化为 $S(n) = 2S(n/2)$，同样得到 $T(n) = O(n)$。分治在这里并没有比减治快（加法总要做 $n - 1$ 次），但递归深度从 $n$ 降到了 $\log n$。

### 1.5.3. 主定理

分治算法的递推式一般形如 $T(n) = a\,T(n/b) + f(n)$：原问题被分为 $a$ 个规模为 $n/b$ 的子问题，划分与合并共需 $f(n)$ 时间。比较 $f(n)$ 与 $n^{\log_b a}$ 的大小，就能直接写出答案。

**定理 1.5.1（主定理）** 设常数 $a \geq 1$、$b > 1$，$f(n)$ 最终取正值，$T(n) = a\,T(n/b) + f(n)$（$n/b$ 可以是 $\lfloor n/b \rfloor$ 或 $\lceil n/b \rceil$）。记 $p = \log_b a$。

1. 若存在 $\varepsilon > 0$ 使 $f(n) = O(n^{p - \varepsilon})$，则 $T(n) = \Theta(n^p)$；
2. 若存在 $k \geq 0$ 使 $f(n) = \Theta(n^p \log^k n)$，则 $T(n) = \Theta(n^p \log^{k+1} n)$；
3. 若存在 $\varepsilon > 0$ 使 $f(n) = \Omega(n^{p + \varepsilon})$，并且存在 $c < 1$ 使 $a f(n/b) \leq c f(n)$ 对充分大的 $n$ 成立，则 $T(n) = \Theta(f(n))$。

**证明** 只对 $n$ 是 $b$ 的幂、$k = 0$ 的情形证明（一般情形的处理见 CLRS 第 4 章）。递归树的第 $j$ 层（$0 \leq j < \log_b n$）有 $a^j$ 个规模为 $n/b^j$ 的实例，叶子共有 $a^{\log_b n} = n^{\log_b a} = n^p$ 个，于是

$$
T(n) = \Theta(n^p) + \sum_{j=0}^{\log_b n - 1} a^j f(n/b^j).
$$
情形 1：$a^j f(n/b^j) \leq C a^j (n/b^j)^{p - \varepsilon} = C n^{p-\varepsilon} (b^{\varepsilon})^j$（用到 $a = b^p$），对 $j$ 求和是公比 $b^\varepsilon > 1$ 的几何级数，由末项主导，为 $O(n^{p-\varepsilon} \cdot n^{\varepsilon}) = O(n^p)$，与叶子同阶。情形 2：每一层都是 $a^j \cdot \Theta\bigl((n/b^j)^p\bigr) = \Theta(n^p)$，共 $\log_b n$ 层，总和为 $\Theta(n^p \log n)$。情形 3：由正则条件，$a^j f(n/b^j) \leq c^j f(n)$，求和是公比 $c < 1$ 的几何级数，由首项主导，为 $O(f(n))$；又 $T(n) \geq f(n)$，故 $T(n) = \Theta(f(n))$；此时 $f(n) = \Omega(n^{p+\varepsilon})$ 也压过了叶子的 $\Theta(n^p)$。$\square$

三种情形分别对应递归树的成本集中在叶子、均匀分布在各层、集中在根。

| 算法 | 递推式 | $p = \log_b a$ | 情形 | 结论 |
|---|---|---|---|---|
| 分治求和 | $2T(n/2) + O(1)$ | 1 | 1 | $\Theta(n)$ |
| kd 树的范围查询（[4.3.7](/4.3.7)） | $2T(n/4) + O(1)$ | $1/2$ | 1 | $\Theta(\sqrt{n})$ |
| 大整数乘法，朴素分治 | $4T(n/2) + O(n)$ | 2 | 1 | $\Theta(n^2)$ |
| 大整数乘法，Karatsuba | $3T(n/2) + O(n)$ | $\log_2 3$ | 1 | $\Theta(n^{1.585})$ |
| 二分查找 | $T(n/2) + O(1)$ | 0 | 2，$k = 0$ | $\Theta(\log n)$ |
| 归并排序 | $2T(n/2) + O(n)$ | 1 | 2，$k = 0$ | $\Theta(n \log n)$ |
| 无缓冲区的就地归并排序 | $2T(n/2) + O(n \log n)$ | 1 | 2，$k = 1$ | $\Theta(n \log^2 n)$ |
| 快速选取（平均情况，[4.3.14](/4.3.14)） | $T(n/2) + O(n)$ | 0 | 3 | $\Theta(n)$ |

大整数乘法值得多说一句。把两个 $n$ 位数各自分成高低两半，$x = x_1 B + x_0$，$y = y_1 B + y_0$（$B$ 为 $n/2$ 位对应的基数），则 $xy = x_1 y_1 B^2 + (x_1 y_0 + x_0 y_1) B + x_0 y_0$，朴素地需要 4 次半长的乘法。Karatsuba（1960）注意到

$$
x_1 y_0 + x_0 y_1 = (x_1 + x_0)(y_1 + y_0) - x_1 y_1 - x_0 y_0,
$$
只需 3 次乘法，再加若干次线性时间的加减，复杂度从 $\Theta(n^2)$ 降到 $\Theta(n^{\log_2 3})$。这是第一个打破平方复杂度的乘法算法；目前理论上最好的是 Harvey 与 van der Hoeven（2019）的 $O(n \log n)$ 算法。CPython 的整数乘法在位数较多时就采用 Karatsuba 算法。

表中无缓冲区的就地归并排序对应 C++ 的 `std::stable_sort` 在申请不到额外内存时的退化方案（[4.2.10](/4.2.10)）。

### 1.5.4. Akra–Bazzi 定理

主定理的三种情形之间有缝隙：例如 $T(n) = 2T(n/2) + n / \log n$，$f(n)$ 比 $n^1$ 小，但不是小一个多项式因子，三种情形都不适用。另外，子问题的规模也可能不均等。更一般的工具是 Akra 与 Bazzi（1998）的定理。

**定理 1.5.2（Akra–Bazzi 定理）** 设对充分大的 $x$，

$$
T(x) = g(x) + \sum_{i=1}^{k} a_i\, T\bigl(b_i x + h_i(x)\bigr),
$$
其中常数 $a_i > 0$、$0 < b_i < 1$，$g(x)$ 非负且多项式增长（存在 $c$ 使 $g(x) = O(x^c)$，并且 $g$ 在 $[b_i x, x]$ 上的取值彼此相差不超过常数倍），扰动项 $|h_i(x)| = O(x / \log^2 x)$（这容许取整）。取 $p$ 为满足 $\sum_{i=1}^{k} a_i b_i^p = 1$ 的唯一实数，则

$$
T(x) = \Theta\Bigl(x^p \Bigl(1 + \int_1^x \frac{g(u)}{u^{p+1}}\,\mathrm{d}u\Bigr)\Bigr).
$$

注意结论与 $h_i$ 无关：取整不影响渐近结果。几个例子：

- $T(n) = 2T(n/2) + n/\log n$：$p = 1$，$\int_2^x \frac{\mathrm{d}u}{u \ln u} = \Theta(\log\log x)$，故 $T(n) = \Theta(n \log\log n)$。
- 线性时间选取（[4.3.14](/4.3.14)）把元素按 5 个一组划分时，$T(n) = T(n/5) + T(7n/10) + \Theta(n)$。由于 $\frac15 + \frac{7}{10} < 1$，解出的 $p < 1$，积分 $\int_1^x u^{-p}\,\mathrm{d}u = \Theta(x^{1-p})$，故 $T(n) = \Theta(n)$。
- 若改为 3 个一组，$T(n) = T(n/3) + T(2n/3) + \Theta(n)$，此时 $p = 1$，积分为 $\Theta(\log x)$，$T(n) = \Theta(n \log n)$：分组的大小决定了算法是否线性。

### 1.5.5. 例：最大子段和

最大子段和问题（maximum subarray problem）：给定整数序列 $A[0, n)$，求总和最大的非空区段 $A[\mathit{lo}, \mathit{hi})$ 的总和。它是同一问题有多种复杂度不同的算法的典型例子。

1. 蛮力：枚举全部 $\Theta(n^2)$ 个区段，每个用 $O(n)$ 时间求和，共 $\Theta(n^3)$。
2. 递增：起点相同的区段，总和之间有关联：$\operatorname{sum}[\mathit{lo}, \mathit{hi}+1) = \operatorname{sum}[\mathit{lo}, \mathit{hi}) + A[\mathit{hi}]$，固定起点、递增终点，每个区段只需 $O(1)$ 时间，共 $\Theta(n^2)$。
3. 分治：从中点 $\mathit{mi}$ 切开，最大区段要么完全在左半、要么完全在右半（递归求解），要么跨越切分线。跨越切分线的区段必然由左半的一个非空后缀与右半的一个非空前缀拼成，并且二者可以独立地取最大：从 $\mathit{mi}$ 向左扫描求最大后缀和，向右扫描求最大前缀和，合计 $O(n)$。于是 $T(n) = 2T(n/2) + O(n) = O(n \log n)$。
4. 线性扫描：设 $s_k$ 为以 $A[k]$ 结尾的区段的最大和。以 $A[k]$ 结尾的区段要么只含 $A[k]$，要么是以 $A[k-1]$ 结尾的某个区段再延长一格，所以

$$
s_k = \max(s_{k-1}, 0) + A[k], \qquad \text{答案} = \max_{0 \leq k < n} s_k.
$$
它的含义是：总和非正的前缀对后面毫无帮助，可以直接剪除。一趟扫描，$O(n)$ 时间、$O(1)$ 空间（这一算法常以 Kadane 命名）。

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <span>
#include <vector>

using Sum = long long;

// O(n^3): try every interval [lo, hi) and sum it from scratch.
Sum gs_bf(std::span<const int> a) {
    Sum best = a[0];
    for (std::size_t lo = 0; lo < a.size(); ++lo)
        for (std::size_t hi = lo + 1; hi <= a.size(); ++hi) {
            Sum s = 0;
            for (std::size_t k = lo; k < hi; ++k) s += a[k];
            best = std::max(best, s);
        }
    return best;
}

// O(n^2): intervals with the same lo share their prefix sums.
Sum gs_ic(std::span<const int> a) {
    Sum best = a[0];
    for (std::size_t lo = 0; lo < a.size(); ++lo) {
        Sum s = 0;
        for (std::size_t hi = lo; hi < a.size(); ++hi)
            best = std::max(best, s += a[hi]);
    }
    return best;
}

// O(n log n): best of the left half, the right half, and the crossing intervals.
Sum gs_dc(std::span<const int> a) {
    if (a.size() == 1) return a[0];
    std::size_t mi = a.size() / 2;
    Sum best_left = a[mi - 1], s = 0;            // best suffix of a[0, mi)
    for (std::size_t i = mi; i-- > 0;) best_left = std::max(best_left, s += a[i]);
    Sum best_right = a[mi]; s = 0;               // best prefix of a[mi, n)
    for (std::size_t j = mi; j < a.size(); ++j) best_right = std::max(best_right, s += a[j]);
    return std::max({best_left + best_right, gs_dc(a.first(mi)), gs_dc(a.subspan(mi))});
}

// O(n): s is the best sum of an interval ending at the current element.
Sum gs_ls(std::span<const int> a) {
    Sum best = a[0], s = 0;
    for (int x : a) {
        s = std::max<Sum>(s, 0) + x;     // drop a prefix whose sum is not positive
        best = std::max(best, s);
    }
    return best;
}

int main() {
    std::mt19937 rng(2024);
    std::uniform_int_distribution<int> value(-50, 50);
    for (int trial = 0; trial < 1000; ++trial) {
        std::vector<int> a(1 + trial % 60);
        for (int& x : a) x = value(rng);
        Sum r = gs_bf(a);
        if (gs_ic(a) != r || gs_dc(a) != r || gs_ls(a) != r) {
            std::cout << "mismatch\n";
            return 1;
        }
    }
    int a[] = {1, -2, 7, 2, 6, -9, 5, 6, -12, -8, 13, 0, -3, 1, -2, 4, -1};
    std::cout << std::format("{} {} {} {}\n", gs_bf(a), gs_ic(a), gs_dc(a), gs_ls(a));
}
```

```python tab
import random

def gs_bf(a: list[int]) -> int:
    """O(n^3): try every interval [lo, hi) and sum it from scratch."""
    n = len(a)
    return max(sum(a[k] for k in range(lo, hi))
               for lo in range(n) for hi in range(lo + 1, n + 1))

def gs_ic(a: list[int]) -> int:
    """O(n^2): intervals with the same lo share their prefix sums."""
    best = a[0]
    for lo in range(len(a)):
        s = 0
        for hi in range(lo, len(a)):
            s += a[hi]
            best = max(best, s)
    return best

def gs_dc(a: list[int], lo: int = 0, hi: int | None = None) -> int:
    """O(n log n): best of the two halves and of the crossing intervals."""
    if hi is None:
        hi = len(a)
    if hi - lo == 1:
        return a[lo]
    mi = (lo + hi) // 2
    best_left, s = a[mi - 1], 0          # best suffix of a[lo, mi)
    for i in range(mi - 1, lo - 1, -1):
        s += a[i]
        best_left = max(best_left, s)
    best_right, s = a[mi], 0             # best prefix of a[mi, hi)
    for j in range(mi, hi):
        s += a[j]
        best_right = max(best_right, s)
    return max(best_left + best_right, gs_dc(a, lo, mi), gs_dc(a, mi, hi))

def gs_ls(a: list[int]) -> int:
    """O(n): s is the best sum of an interval ending at the current element."""
    best, s = a[0], 0
    for x in a:
        s = max(s, 0) + x                # drop a prefix whose sum is not positive
        best = max(best, s)
    return best

rng = random.Random(2024)
for trial in range(1000):
    a = [rng.randint(-50, 50) for _ in range(1 + trial % 60)]
    r = gs_bf(a)
    assert gs_ic(a) == r == gs_dc(a) == gs_ls(a)
a = [1, -2, 7, 2, 6, -9, 5, 6, -12, -8, 13, 0, -3, 1, -2, 4, -1]
print(gs_bf(a), gs_ic(a), gs_dc(a), gs_ls(a))
```

主程序用蛮力算法作为标准，在 1000 组随机数据上核对其余三种算法（**对拍**，[4.1.5](/4.1.5)），再对一个例子输出四个结果（都是 17，对应区段 $7, 2, 6, -9, 5, 6$）。线性扫描已是最优：任何算法都必须读完全部输入，否则未读的元素可能是一个巨大的正数。

## 1.6. 动态规划初步

### 1.6.1. Fibonacci 数列：递归为什么慢

**动态规划**的基本思想（[4.1.13](/4.1.13)）可以从 Fibonacci 数列看清。按定义递归，`fib(n)` 调用 `fib(n-1)` 与 `fib(n-2)`，成本满足

$$
T(n) = T(n-1) + T(n-2) + 1, \qquad T(0) = T(1) = 1.
$$
令 $S(n) = \frac{T(n) + 1}{2}$，则 $S(n) = S(n-1) + S(n-2)$、$S(0) = S(1) = 1$，即 $S(n) = F_{n+1}$，于是 $T(n) = 2F_{n+1} - 1 = \Theta(\phi^n)$，其中 $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$。封底估算：$\phi^{43} \approx 10^9$，$\phi^{67} \approx 10^{14}$，$\phi^{92} \approx 10^{19}$；在每秒 $10^9$ 次的计算机上，`fib(43)` 约需 1 秒，`fib(67)` 约需一天，`fib(92)` 要近八百年。

低效的根源在于大量重复的递归实例：先后出现的递归实例共 $\Theta(\phi^n)$ 个，去除重复之后只有 $n + 1$ 种。有两种消除重复的办法。

1. **记忆化**（[4.1.10](/4.1.10)）：保持自顶向下的递归，但把算过的结果记入表中，再次遇到时直接查表。时间与空间都是 $O(n)$。
2. 动态规划：颠倒计算方向，由自顶向下的递归改为自底向上的迭代，按 $F_0, F_1, F_2, \dots$ 的次序依次计算，每一项只依赖前两项。

```cpp tab
#include <format>
#include <iostream>

// Bottom-up: keep only the last two terms; O(n) time and O(1) space.
unsigned long long fib(int n) {
    unsigned long long f = 1, g = 0;     // f = F(-1), g = F(0)
    while (n-- > 0) {
        g = g + f;                       // g = F(k + 1)
        f = g - f;                       // f = F(k)
    }
    return g;
}

int main() { std::cout << std::format("{} {}\n", fib(12), fib(90)); }
```

```python tab
def fib(n: int) -> int:
    """Bottom-up: keep only the last two terms; O(n) time and O(1) space."""
    f, g = 1, 0                          # f = F(-1), g = F(0)
    for _ in range(n):
        f, g = g, f + g
    return g

print(fib(12), fib(90))
```

C++ 版本用 $g \gets g + f$、$f \gets g - f$ 两步就完成了 $(f, g) \gets (g, f + g)$，不需要第三个变量；约定 $F_{-1} = 1$，使递推从 $k = 0$ 开始就成立。时间 $O(n)$，空间 $O(1)$。

### 1.6.2. 最长公共子序列

**定义 1.6.1（最长公共子序列）** 由序列中若干个元素按原来的相对次序构成的序列称为该序列的**子序列**（元素不必相邻）。两个序列的公共子序列中最长者称为它们的**最长公共子序列**（longest common subsequence，LCS）。

例如 `EDUCATIONAL` 与 `ADVANTAGE` 的一个最长公共子序列是 `DATA`，长度为 4。最长公共子序列可能不唯一；`diff` 等比较文件差异的工具、DNA 序列比对都以它为基础。

对 $A[0, n)$ 与 $B[0, m)$，记 $\operatorname{LCS}(n, m)$ 为它们的最长公共子序列的长度。比较末元素，只有三种情况：

1. 若 $n = 0$ 或 $m = 0$，则 $\operatorname{LCS}(n, m) = 0$（递归基，必能抵达）；
2. 若 $A[n-1] = B[m-1]$，则 $\operatorname{LCS}(n, m) = \operatorname{LCS}(n-1, m-1) + 1$（减而治之）；
3. 若 $A[n-1] \neq B[m-1]$，则 $\operatorname{LCS}(n, m) = \max\bigl(\operatorname{LCS}(n, m-1), \operatorname{LCS}(n-1, m)\bigr)$（分而治之）。

情况 2 的正确性：设 $C$ 是一个最长公共子序列，$x = A[n-1] = B[m-1]$。若 $C$ 的末元素不是 $x$，则 $C$ 没有用到 $A[n-1]$ 和 $B[m-1]$，在它末尾补上 $x$ 得到更长的公共子序列，矛盾；所以 $C$ 以 $x$ 结尾，并且可以让这个 $x$ 恰好对应 $A[n-1]$ 与 $B[m-1]$，去掉它就是 $A[0, n-1)$ 与 $B[0, m-1)$ 的公共子序列。情况 3：$C$ 的末元素不可能同时对应 $A[n-1]$ 与 $B[m-1]$（二者不等），所以 $C$ 是 $A[0, n-1)$ 与 $B$ 的、或 $A$ 与 $B[0, m-1)$ 的公共子序列。

直接递归时，每次比较至少使一个序列缩短一个元素，最好情况（如两序列相同）只需 $O(n + m)$ 时间；但在最坏情况下（如两个序列没有相同的元素），子问题不仅数量巨大，而且大量重复：子问题 $\operatorname{LCS}(a, b)$ 被重复计算的次数可多达 $\binom{(n-a) + (m-b)}{n-a}$ 次，当 $n = m$ 时，$\operatorname{LCS}(1, 1)$ 被计算 $\binom{2n-2}{n-1} = \Theta(4^n / \sqrt{n})$ 次。而不同的子问题只有 $(n+1)(m+1)$ 种，各对应 $A$ 与 $B$ 的一对前缀。把它们列成一张表，从 $\operatorname{LCS}(0, \cdot)$、$\operatorname{LCS}(\cdot, 0)$ 出发，逐行计算到 $\operatorname{LCS}(n, m)$，即得 $O(nm)$ 时间的动态规划算法。表填好后，从 $(n, m)$ 沿着取值的来源倒推，还能还原出一个最长公共子序列：每个解对应表中从 $(0, 0)$ 到 $(n, m)$ 的一条单调通路。

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

// L[i][j] = length of an LCS of the prefixes a[0, i) and b[0, j).
std::string lcs(std::string_view a, std::string_view b) {
    const std::size_t n = a.size(), m = b.size();
    std::vector<std::vector<int>> L(n + 1, std::vector<int>(m + 1, 0));
    for (std::size_t i = 1; i <= n; ++i)
        for (std::size_t j = 1; j <= m; ++j)
            L[i][j] = (a[i - 1] == b[j - 1]) ? L[i - 1][j - 1] + 1
                                             : std::max(L[i - 1][j], L[i][j - 1]);
    std::string s;                    // walk back from (n, m) to recover one LCS
    for (std::size_t i = n, j = m; i > 0 && j > 0;) {
        if (a[i - 1] == b[j - 1]) { s += a[i - 1]; --i; --j; }
        else if (L[i - 1][j] >= L[i][j - 1]) --i;
        else --j;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    std::string s = lcs("EDUCATIONAL", "ADVANTAGE");
    std::cout << std::format("{} (length {})\n", s, s.size());
}
```

```python tab
def lcs(a: str, b: str) -> str:
    """L[i][j] = length of an LCS of the prefixes a[:i] and b[:j]."""
    n, m = len(a), len(b)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            L[i][j] = (L[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1]
                       else max(L[i - 1][j], L[i][j - 1]))
    s, i, j = [], n, m                # walk back from (n, m) to recover one LCS
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            s.append(a[i - 1])
            i, j = i - 1, j - 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(s))

s = lcs("EDUCATIONAL", "ADVANTAGE")
print(f"{s} (length {len(s)})")
```

若只需要长度，第 $i$ 行只依赖第 $i - 1$ 行，保留两行即可，空间降为 $O(\min(n, m))$。若既要还原解又要节省空间，可以用 Hirschberg 的分治算法，在 $O(nm)$ 时间、$O(n + m)$ 空间内完成。

## 小结

| 主题 | 要点 |
|---|---|
| 算法 | 输入、输出、正确性、确定性、可行性、有穷性；有穷性未必容易判定（Hailstone） |
| 计算模型 | 图灵机用于可计算性理论；（字）RAM 模型下，运行时间 = 基本操作次数 |
| 复杂度 | 最坏情况的 $T(n)$ 与 $S(n)$；$O$ 上界、$\Omega$ 下界、$\Theta$ 确界 |
| 层次 | $1 \prec \log^* n \prec \log n \prec \sqrt n \prec n \prec n\log n \prec n^2 \prec n^3 \prec 2^n$；多项式与指数是有效与无效的分水岭 |
| 迭代 | 归结为级数：算术 $\Theta(n^2)$、几何由末项主导、调和 $\Theta(\log n)$、对数 $\Theta(n \log n)$ |
| 递归 | 递归跟踪或递推方程；$T(n) = aT(n/b) + f(n)$ 用主定理，不均等的划分用 Akra–Bazzi 定理 |
| 改进算法 | 最大子段和：$n^3 \to n^2 \to n \log n \to n$；Fibonacci、LCS：去除重复子问题，指数 $\to$ 多项式 |
