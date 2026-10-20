---
title: 动态规划
description: 从带备忘录的递归到自底向上的递推；最优子结构与重叠子问题；状态、状态转移方程与计算顺序；钢条切割、数字串中插入乘号、网格地图的最短路、矩阵连乘。
---

[4.1.10](/4.1.10) 中，Fibonacci 数列的递归程序因为反复求解同一个子问题而慢得无法使用，加上备忘录之后就变得飞快。本章把这个观察发展成一种系统的算法设计方法：动态规划。它适用于一类最优化问题：问题的最优解由子问题的最优解组合而成，而不同的决策序列会反复遇到相同的子问题。与 [4.1.11](/4.1.11) 的分治相比，动态规划的子问题是重叠的；与 [4.1.12](/4.1.12) 的回溯相比，动态规划不列出所有方案，只为每个子问题记住最优的一个。本章先用钢条切割问题完整地走一遍"递归—记忆化—递推"的过程，归纳出动态规划的要素，再用三个例子练习怎样定义状态和写出状态转移方程。动态规划的进一步内容（背包问题、最长公共子序列等）以及与图算法的联系见 [4.3.1](/4.3.1) 与 [4.3.11](/4.3.11)。

## 13.1. 从递归到动态规划：钢条切割

**例 13.1.1（钢条切割）** 一家公司把长钢条切割成短钢条出售，长度为 $i$ 的钢条售价为 $p_i$（见下表），切割本身不花钱。给定一根长度为 $n$ 的钢条，怎样切割才能使总收益 $r_n$ 最大？

| 长度 $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 价格 $p_i$ | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30 |

注意不切割也是一种方案：若 $p_n$ 足够大，最优方案可能就是整根出售。

### 13.1.1. 递归：第一刀切在哪里

长度为 $n$ 的钢条有 $n - 1$ 个可以下刀的位置，每个位置切或不切，共 $2^{n-1}$ 种方案，逐一枚举很快就不可行了。换一个角度：考虑最左边那一段的长度 $i$（$1 \leq i \leq n$；$i = n$ 表示不切）。这一段不再切割，收益为 $p_i$；右边剩下长度为 $n - i$ 的钢条，应当以最优的方式切割，收益为 $r_{n-i}$。枚举所有可能的 $i$、取最大值：

$$
r_0 = 0, \qquad r_n = \max_{1 \leq i \leq n} \bigl(p_i + r_{n-i}\bigr) \quad (n \geq 1).
$$

为什么右边剩下的部分要"以最优方式"切割？因为若右边的切法不是最优的，把它换成最优的切法，总收益只会更大。也就是说，原问题的最优解中包含着子问题的最优解。

直接写成递归程序是正确的，但调用次数为 $2^n$：计算 $r_n$ 要调用 $r_{n-1}, r_{n-2}, \dots, r_0$，而计算 $r_{n-1}$ 又要再调用 $r_{n-2}, \dots, r_0$，同一个子问题被求解了指数多次。$n = 30$ 时已有约 10 亿次调用。

### 13.1.2. 带备忘录的递归

子问题只有 $r_0, r_1, \dots, r_n$ 这 $n + 1$ 个，用一个数组记住每个子问题的结果，即记忆化，每个子问题就只算一次：

```cpp tab
#include <algorithm>
#include <iostream>
#include <vector>

const std::vector<int> price = {0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30};

int best_revenue(int n, std::vector<int>& memo) {
    if (n == 0) return 0;
    if (memo[n] >= 0) return memo[n];             // already solved
    int best = 0;
    for (int i = 1; i <= n; ++i)                  // length of the leftmost piece
        best = std::max(best, price[i] + best_revenue(n - i, memo));
    return memo[n] = best;
}

int main() {
    std::vector<int> memo(11, -1);
    std::cout << best_revenue(7, memo) << '\n';   // 18
}
```

```python tab
from functools import cache

PRICE = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

@cache
def best_revenue(n: int) -> int:
    if n == 0:
        return 0
    return max(PRICE[i] + best_revenue(n - i) for i in range(1, n + 1))

print(best_revenue(7))   # 18
```

现在每个 $r_k$ 只计算一次，计算它时要比较 $k$ 种情形，总的工作量约为 $1 + 2 + \cdots + n$，即与 $n^2$ 成正比。

### 13.1.3. 自底向上的递推

既然 $r_n$ 只依赖于更小的 $r_k$，也可以不用递归：按 $r_0, r_1, r_2, \dots$ 的顺序依次填表，算 $r_k$ 时所需的 $r_0, \dots, r_{k-1}$ 都已经在表中了。递推的同时记下每个 $r_k$ 取得最大值时最左段的长度 `first[k]`，就可以还原出切割方案：先切下 `first[n]`，再看剩下的长度 `n - first[n]` 应该怎样切，依此类推。

```cpp tab
#include <iostream>
#include <vector>

int main() {
    const std::vector<int> price = {0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    const int n = 7;
    std::vector<int> r(n + 1, 0), first(n + 1, 0);
    for (int k = 1; k <= n; ++k) {               // solve smaller problems first
        for (int i = 1; i <= k; ++i) {
            if (price[i] + r[k - i] > r[k]) {
                r[k] = price[i] + r[k - i];
                first[k] = i;                    // best length of the leftmost piece
            }
        }
    }
    std::cout << "revenue " << r[n] << ", pieces:";
    for (int k = n; k > 0; k -= first[k]) std::cout << ' ' << first[k];
    std::cout << '\n';                           // revenue 18, pieces: 1 6
}
```

```python tab
PRICE = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 7
r = [0] * (n + 1)
first = [0] * (n + 1)
for k in range(1, n + 1):                        # solve smaller problems first
    for i in range(1, k + 1):
        if PRICE[i] + r[k - i] > r[k]:
            r[k] = PRICE[i] + r[k - i]
            first[k] = i                         # best length of the leftmost piece

pieces = []
k = n
while k > 0:
    pieces.append(first[k])
    k -= first[k]
print("revenue", r[n], "pieces:", *pieces)       # revenue 18 pieces: 1 6
```

长度 7 的钢条最大收益为 18，例如切成 1 + 6（或 2 + 2 + 3）。长度为 1 到 10 时，最大收益依次为 1、5、8、10、13、17、18、22、25、30。

子问题的划分方式不止一种。也可以把"在某处切一刀分成两段，两段各自最优地切割"作为递推：$r_n = \max\bigl(p_n, \max_{1 \leq i < n} (r_i + r_{n-i})\bigr)$。它同样正确，但每个子问题依赖的子问题更多、对称的情形被重复考虑；"只决定最左一段"的划分更简洁。选择怎样描述子问题，是设计动态规划时最重要的决定。

## 13.2. 动态规划的要素

**定义 13.2.1（动态规划）** 把一个最优化问题分解为若干阶段的决策，利用原问题的最优解可由子问题的最优解构造出来这一性质，按一定顺序求解每个子问题并记录其最优值、避免重复求解的算法设计方法称为**动态规划**。描述一个子问题所需的参数称为**状态**，状态的最优值与更小的状态的最优值之间的关系式称为**状态转移方程**。一个问题适合用动态规划求解，通常要具备两个性质：

1. **最优子结构**：问题的最优解中包含的子问题的解，也是该子问题的最优解；
2. **重叠子问题**：在递归求解的过程中，相同的子问题会被反复遇到，不同子问题的总数却不多（通常是输入规模的多项式）。

"动态规划"这个名字是 Richard Bellman 在 1950 年代起的，"规划"（programming）指的是制定决策表，与写程序无关。设计一个动态规划算法可以按以下步骤进行：

1. 定义状态：用一句话说清楚 $f(\text{参数})$ 表示什么，例如"$r_k$ 是长度为 $k$ 的钢条的最大收益"；
2. 写出状态转移方程：考虑最后一步（或第一步）的所有选择，用更小的状态表示当前状态；
3. 确定边界：最小的状态的值；
4. 确定计算顺序：每个状态所依赖的状态要先算出来；
5. 如需要，记录每个状态的最优选择，以便还原出最优方案。

实现方式有两种：

| | 自顶向下（记忆化递归） | 自底向上（递推填表） |
|---|---|---|
| 写法 | 照状态转移方程写递归，加备忘录 | 按依赖关系安排循环顺序 |
| 优点 | 与问题描述直接对应；只计算真正用到的子问题 | 没有函数调用开销和递归深度限制；便于节省空间 |
| 缺点 | 递归开销；状态多时可能栈溢出 | 必须想清楚计算顺序；可能计算了用不到的子问题 |

动态规划与其他策略的关系可以这样理解：它是"不重复计算的递归枚举"。回溯法沿决策树逐个尝试所有方案；动态规划注意到许多不同的部分方案通向同一个子问题，而对后续决策来说，只需要知道这个子问题本身（当前状态），不需要知道是怎样到达它的。因此每个子问题只需求解一次、记住最优值。

## 13.3. 例：数字串中插入乘号

**例 13.3.1** 在一个长度为 $L$ 的数字串中插入 $K$ 个乘号，使得到的乘积最大。例如在 `3215125` 中插入 3 个乘号，最大乘积为 $321 \times 51 \times 2 \times 5 = 163\,710$。

先找子问题。插入 $K$ 个乘号是一个整体的方案，但可以把它看作逐个决定乘号的位置。考虑位置上的最后一个乘号：若它插在第 $i$ 个数字之后，则乘积等于"前 $i$ 个数字中插入 $K - 1$ 个乘号的乘积"乘以"后面那段数字组成的数"。后面那段数不受前面怎样插乘号的影响，所以前一部分应当取最大乘积：这就是最优子结构（这里所有因子都非负，"较大乘以非负数仍较大"成立）。

设 $D(i, j)$ 是第 $i + 1$ 到第 $j$ 个数字组成的整数，$f(j, k)$ 是在前 $j$ 个数字中插入 $k$ 个乘号所得的最大乘积，则

$$
f(j, 0) = D(0, j), \qquad f(j, k) = \max_{k \leq i < j} f(i, k - 1) \cdot D(i, j) \quad (k \geq 1),
$$

答案为 $f(L, K)$。$i \geq k$ 保证前 $i$ 个数字中放得下 $k - 1$ 个乘号（每段至少一个数字）。按 $k$ 从小到大计算即可。

```cpp tab
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    const std::string s = "3215125";
    const int L = static_cast<int>(s.size()), K = 3;
    auto D = [&](int i, int j) { return std::stoll(s.substr(i, j - i)); };  // digits i..j-1
    // f[k][j]: maximum product of the first j digits with k multiplication signs
    std::vector<std::vector<long long>> f(K + 1, std::vector<long long>(L + 1, -1));
    for (int j = 1; j <= L; ++j) f[0][j] = D(0, j);
    for (int k = 1; k <= K; ++k)
        for (int j = k + 1; j <= L; ++j)
            for (int i = k; i < j; ++i)              // the last sign goes after digit i
                f[k][j] = std::max(f[k][j], f[k - 1][i] * D(i, j));
    std::cout << f[K][L] << '\n';                     // 163710
}
```

```python tab
s, K = "3215125", 3
L = len(s)

def D(i: int, j: int) -> int:                        # digits i..j-1 as a number
    return int(s[i:j])

# f[k][j]: maximum product of the first j digits with k multiplication signs
f = [[-1] * (L + 1) for _ in range(K + 1)]
for j in range(1, L + 1):
    f[0][j] = D(0, j)
for k in range(1, K + 1):
    for j in range(k + 1, L + 1):
        f[k][j] = max(f[k - 1][i] * D(i, j) for i in range(k, j))  # last sign after digit i
print(f[K][L])                                       # 163710
```

状态有 $(K + 1)(L + 1)$ 个，每个状态比较不超过 $L$ 种情形。对比一下暴力枚举：在 $L - 1$ 个空位中选 $K$ 个放乘号，有 $\binom{L-1}{K}$ 种方案，$L = 40$、$K = 10$ 时超过 6 亿种；动态规划只需几千次运算。数字串很长时乘积会超出 `long long` 的范围，C++ 需要用高精度整数，Python 的整数则没有上限。

## 13.4. 例：网格地图的最短路

**例 13.4.1** 一张地图上的道路构成 $4 \times 4$ 个路口的网格，每段道路标有长度。从左下角的路口出发，只能向上或向右走，求到右上角路口的最短路程。

把路口记为 $(i, j)$（第 $i$ 行、第 $j$ 列，从左下角的 $(0, 0)$ 开始）。设 $h_{i,j}$ 是从 $(i, j)$ 向右到 $(i, j+1)$ 的道路长度，$v_{i,j}$ 是从 $(i, j)$ 向上到 $(i+1, j)$ 的道路长度，$d_{i,j}$ 是从起点到 $(i, j)$ 的最短路程。只能向上或向右走，所以到达 $(i, j)$ 的最后一步要么来自下方的 $(i-1, j)$，要么来自左方的 $(i, j-1)$：

$$
d_{i,j} = \min\bigl(d_{i-1,j} + v_{i-1,j},\ d_{i,j-1} + h_{i,j-1}\bigr),
$$

边界为 $d_{0,0} = 0$，第一行与第一列只有一个方向可来。按行、列从小到大的顺序计算，或者按 $i + j$ 的值分阶段计算：第 $s$ 阶段的路口只依赖第 $s - 1$ 阶段。下图标出了道路长度、每个路口的最短路程和最短路线（共 6 个阶段），答案为 10。

![每个路口到起点的最短路程，橙色为一条最短路线](./plots/grid-shortest-path.py)

```cpp tab
#include <algorithm>
#include <iostream>

int main() {
    constexpr int n = 4;
    const int h[n][n - 1] = {{3, 2, 3}, {2, 1, 4}, {3, 4, 5}, {3, 1, 2}};      // rightward roads
    const int v[n - 1][n] = {{2, 2, 3, 4}, {4, 1, 2, 4}, {1, 2, 2, 3}};       // upward roads
    int d[n][n] = {};
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) continue;
            if (i == 0) d[i][j] = d[i][j - 1] + h[i][j - 1];
            else if (j == 0) d[i][j] = d[i - 1][j] + v[i - 1][j];
            else d[i][j] = std::min(d[i - 1][j] + v[i - 1][j], d[i][j - 1] + h[i][j - 1]);
        }
    }
    std::cout << d[n - 1][n - 1] << '\n';   // 10
}
```

```python tab
H = [[3, 2, 3], [2, 1, 4], [3, 4, 5], [3, 1, 2]]      # rightward roads
V = [[2, 2, 3, 4], [4, 1, 2, 4], [1, 2, 2, 3]]       # upward roads
n = 4
INF = float("inf")
d = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        from_below = d[i - 1][j] + V[i - 1][j] if i > 0 else INF
        from_left = d[i][j - 1] + H[i][j - 1] if j > 0 else INF
        d[i][j] = min(from_below, from_left)
print(d[n - 1][n - 1])   # 10
```

"只能向上或向右"保证了路口之间的依赖没有环：每一步都让 $i + j$ 增加 1，状态天然地分成先后的阶段。若允许向四个方向走，到达一个路口的最后一步可能来自尚未算出的路口，就不能这样简单地按顺序填表了；一般图上的最短路需要 Dijkstra 算法等方法（[4.3.11](/4.3.11)），它们同样建立在"最短路的一部分也是最短路"这一最优子结构之上。

## 13.5. 例：矩阵连乘

**例 13.5.1（矩阵连乘）** 给定 $n$ 个矩阵 $A_1, A_2, \dots, A_n$，其中 $A_i$ 的大小为 $p_{i-1} \times p_i$。矩阵乘法满足结合律，任何加括号的方式结果都相同，但所需的标量乘法次数不同。求一种加括号的方式，使计算乘积 $A_1 A_2 \cdots A_n$ 所需的标量乘法次数最少。

一个 $p \times q$ 矩阵与一个 $q \times r$ 矩阵相乘，结果有 $pr$ 个元素，每个元素需要 $q$ 次乘法，共 $pqr$ 次。设 $A$、$B$、$C$ 的大小分别为 $10 \times 100$、$100 \times 5$、$5 \times 50$，则 $(AB)C$ 需要 $10 \cdot 100 \cdot 5 + 10 \cdot 5 \cdot 50 = 7500$ 次，而 $A(BC)$ 需要 $100 \cdot 5 \cdot 50 + 10 \cdot 100 \cdot 50 = 75\,000$ 次，相差十倍。加括号的方式数是 Catalan 数，随 $n$ 指数增长，不能逐一枚举。

考虑最后一次乘法：它把 $A_i \cdots A_j$ 分成 $A_i \cdots A_k$ 与 $A_{k+1} \cdots A_j$ 两部分（$i \leq k < j$），两部分各自的结果是 $p_{i-1} \times p_k$ 与 $p_k \times p_j$ 的矩阵，最后相乘需要 $p_{i-1} p_k p_j$ 次乘法，两部分各自应当以最优的方式计算。设 $m_{i,j}$ 为计算 $A_i \cdots A_j$ 所需的最少标量乘法次数，则

$$
m_{i,i} = 0, \qquad m_{i,j} = \min_{i \leq k < j} \bigl(m_{i,k} + m_{k+1,j} + p_{i-1} p_k p_j\bigr) \quad (i < j).
$$

计算 $m_{i,j}$ 需要所有更短的子链的结果，所以按链长 $\ell = j - i + 1$ 从 2 到 $n$ 的顺序计算。同时记录取得最小值的分割点 $s_{i,j} = k$，最后从 $s_{1,n}$ 出发递归地输出括号。

```cpp tab
#include <iostream>
#include <limits>
#include <string>
#include <vector>

std::vector<std::vector<int>> split;

std::string parenthesize(int i, int j) {
    if (i == j) return "A" + std::to_string(i);
    int k = split[i][j];
    return "(" + parenthesize(i, k) + parenthesize(k + 1, j) + ")";
}

int main() {
    const std::vector<long long> p = {30, 35, 15, 5, 10, 20, 25};  // A_i is p[i-1] x p[i]
    const int n = static_cast<int>(p.size()) - 1;
    std::vector<std::vector<long long>> m(n + 1, std::vector<long long>(n + 1, 0));
    split.assign(n + 1, std::vector<int>(n + 1, 0));
    for (int len = 2; len <= n; ++len) {             // shorter chains first
        for (int i = 1; i + len - 1 <= n; ++i) {
            int j = i + len - 1;
            m[i][j] = std::numeric_limits<long long>::max();
            for (int k = i; k < j; ++k) {            // the last multiplication splits after A_k
                long long cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (cost < m[i][j]) { m[i][j] = cost; split[i][j] = k; }
            }
        }
    }
    std::cout << m[1][n] << ' ' << parenthesize(1, n) << '\n';
    // 15125 ((A1(A2A3))((A4A5)A6))
}
```

```python tab
p = [30, 35, 15, 5, 10, 20, 25]                      # A_i is p[i-1] x p[i]
n = len(p) - 1
m = [[0] * (n + 1) for _ in range(n + 1)]
split = [[0] * (n + 1) for _ in range(n + 1)]
for length in range(2, n + 1):                       # shorter chains first
    for i in range(1, n - length + 2):
        j = i + length - 1
        m[i][j], split[i][j] = min(
            (m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j], k)  # split after A_k
            for k in range(i, j)
        )

def parenthesize(i: int, j: int) -> str:
    if i == j:
        return f"A{i}"
    k = split[i][j]
    return f"({parenthesize(i, k)}{parenthesize(k + 1, j)})"

print(m[1][n], parenthesize(1, n))                   # 15125 ((A1(A2A3))((A4A5)A6))
```

对于大小依次为 $30 \times 35$、$35 \times 15$、$15 \times 5$、$5 \times 10$、$10 \times 20$、$20 \times 25$ 的 6 个矩阵，最少需要 15125 次标量乘法，最优方案为 $((A_1(A_2A_3))((A_4A_5)A_6))$。状态 $(i, j)$ 约有 $n^2/2$ 个，每个状态尝试不超过 $n$ 个分割点，总工作量与 $n^3$ 成正比。这种"在区间内选一个分割点"的状态设计称为区间动态规划，它同样适用于最优二叉搜索树、多边形三角剖分等问题。

## 小结

| 例子 | 状态 | 状态转移 | 计算顺序 |
|---|---|---|---|
| 钢条切割 | $r_k$：长度 $k$ 的最大收益 | 枚举最左段长度 | $k$ 从小到大 |
| 插入乘号 | $f(j, k)$：前 $j$ 个数字插 $k$ 个乘号 | 枚举最后一个乘号的位置 | $k$ 从小到大 |
| 网格最短路 | $d_{i,j}$：到路口 $(i, j)$ 的最短路程 | 来自下方或左方 | 按阶段 $i + j$ |
| 矩阵连乘 | $m_{i,j}$：计算 $A_i \cdots A_j$ 的最少乘法 | 枚举最后一次乘法的分割点 | 链长从小到大 |

- 动态规划适用于具有最优子结构和重叠子问题的最优化问题。
- 关键是定义状态：状态要足以描述子问题，并且后续决策只依赖于状态本身，与到达它的过程无关。
- 实现方式有记忆化递归与递推填表两种；记录每个状态的最优选择可以还原最优方案。
