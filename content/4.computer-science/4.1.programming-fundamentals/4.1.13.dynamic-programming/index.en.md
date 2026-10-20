---
title: Dynamic Programming
description: From recursion with a memo to bottom-up iteration; optimal substructure and overlapping subproblems; states, state transition equations, and order of computation; rod cutting, inserting multiplication signs into a digit string, shortest paths on a grid map, and matrix chain multiplication.
source_hash: 18789edaab0f
---

In [4.1.10](/4.1.10), the recursive program for the Fibonacci sequence was too slow to use because it solved the same subproblem again and again, and became extremely fast once a memo was added. This chapter develops that observation into a systematic method of algorithm design: dynamic programming. It applies to a class of optimization problems in which the optimal solution of the problem is composed of optimal solutions of subproblems, and different sequences of decisions repeatedly encounter the same subproblems. Compared with the **divide and conquer** of [4.1.11](/4.1.11), the subproblems of dynamic programming overlap; compared with the **backtracking** of [4.1.12](/4.1.12), dynamic programming does not list all solutions and remembers only the best one for each subproblem. This chapter first uses the rod-cutting problem to walk through the whole process of "recursion, **memoization**, iteration" and distills the elements of dynamic programming, then uses three examples to practice defining states and writing state transition equations. Further topics of dynamic programming (the knapsack problem, longest common subsequence, and others) and its connection with graph algorithms are in [4.3.1](/4.3.1) and [4.3.11](/4.3.11).

## 13.1. From Recursion to Dynamic Programming: Rod Cutting

**Example 13.1.1 (Rod Cutting)** A company cuts long steel rods into short ones for sale; a rod of length $i$ sells for $p_i$ (see the table below), and cutting itself is free. Given a rod of length $n$, how should it be cut to maximize the total revenue $r_n$?

| Length $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Price $p_i$ | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 | 24 | 30 |

Note that not cutting is also a possible plan: if $p_n$ is large enough, the optimal plan may be to sell the whole rod.

### 13.1.1. Recursion: Where to Make the First Cut

A rod of length $n$ has $n - 1$ positions where a cut can be made, and each position is either cut or not, giving $2^{n-1}$ plans in all; enumerating them one by one quickly becomes infeasible. Look at it from another angle: consider the length $i$ of the leftmost piece ($1 \leq i \leq n$; $i = n$ means no cut). This piece is not cut further and yields $p_i$; the remaining rod of length $n - i$ on the right should be cut optimally, yielding $r_{n-i}$. Enumerating all possible $i$ and taking the maximum:

$$
r_0 = 0, \qquad r_n = \max_{1 \leq i \leq n} \bigl(p_i + r_{n-i}\bigr) \quad (n \geq 1).
$$

Why must the remaining part on the right be cut "optimally"? Because if the way of cutting it is not optimal, replacing it with the optimal way can only increase the total revenue. In other words, an optimal solution of the original problem contains optimal solutions of the subproblems.

Writing this directly as a recursive program is correct, but the number of calls is $2^n$: computing $r_n$ calls $r_{n-1}, r_{n-2}, \dots, r_0$, and computing $r_{n-1}$ in turn calls $r_{n-2}, \dots, r_0$ again, so the same subproblem is solved exponentially many times. For $n = 30$ there are already about a billion calls.

### 13.1.2. Recursion with a Memo

There are only $n + 1$ subproblems, $r_0, r_1, \dots, r_n$; recording the result of each in an array, that is, **memoization**, makes each subproblem computed only once:

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

Now each $r_k$ is computed only once, comparing $k$ cases each time, so the total work is about $1 + 2 + \cdots + n$, proportional to $n^2$.

### 13.1.3. Bottom-Up Iteration

Since $r_n$ depends only on smaller $r_k$, we can also avoid recursion: fill the table in the order $r_0, r_1, r_2, \dots$, so that when $r_k$ is computed, the needed $r_0, \dots, r_{k-1}$ are already in the table. While iterating, we record for each $r_k$ the length `first[k]` of the leftmost piece at which the maximum is attained, which lets us reconstruct the cutting plan: cut off `first[n]` first, then see how the remaining length `n - first[n]` should be cut, and so on.

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

The maximum revenue for a rod of length 7 is 18, for example by cutting into 1 + 6 (or 2 + 2 + 3). For lengths 1 to 10, the maximum revenues are 1, 5, 8, 10, 13, 17, 18, 22, 25, 30.

There is more than one way to divide into subproblems. We could also take "cut once somewhere into two pieces, each cut optimally" as the recurrence: $r_n = \max\bigl(p_n, \max_{1 \leq i < n} (r_i + r_{n-i})\bigr)$. It is equally correct, but each subproblem depends on more subproblems and symmetric cases are considered twice; the division that "decides only the leftmost piece" is more concise. Choosing how to describe the subproblems is the most important decision in designing a dynamic program.

## 13.2. Elements of Dynamic Programming

**Definition 13.2.1 (Dynamic Programming)** The algorithm design method that decomposes an optimization problem into decisions at several stages and, using the property that an optimal solution of the original problem can be constructed from optimal solutions of subproblems, solves each subproblem in a suitable order, recording its optimal value so as to avoid repeated solving, is called **dynamic programming**. The parameters needed to describe a subproblem are called the **state**, and the relation between the optimal value of a state and the optimal values of smaller states is called the **state transition equation**. A problem is suited to dynamic programming usually if it has two properties:

1. **Optimal substructure**: the solutions of subproblems contained in an optimal solution of the problem are themselves optimal for those subproblems.
2. **Overlapping subproblems**: in the course of recursive solving, the same subproblems are encountered repeatedly, while the total number of distinct subproblems is small (usually a polynomial in the input size).

The name "dynamic programming" was coined by Richard Bellman in the 1950s; "programming" here refers to drawing up a table of decisions and has nothing to do with writing programs. A dynamic programming algorithm can be designed in the following steps:

1. Define the state: say in one sentence what $f(\text{parameters})$ means, for example "$r_k$ is the maximum revenue of a rod of length $k$".
2. Write the state transition equation: consider all choices for the last step (or the first step) and express the current state through smaller states.
3. Determine the boundary: the values of the smallest states.
4. Determine the order of computation: the states on which each state depends must be computed first.
5. If needed, record the optimal choice for each state so that the optimal plan can be reconstructed.

There are two ways to implement it:

| | Top-down (memoized recursion) | Bottom-up (iterative table filling) |
|---|---|---|
| Style | write the recursion directly from the state transition equation and add a memo | arrange the order of loops according to the dependencies |
| Advantages | corresponds directly to the problem description; computes only the subproblems actually used | no function call overhead or recursion depth limit; easy to save space |
| Disadvantages | recursion overhead; may overflow the stack when there are many states | the order of computation must be worked out; may compute subproblems that are never used |

The relation of dynamic programming to other strategies can be understood as follows: it is "recursive enumeration without repeated computation". **Backtracking** tries all plans one by one along the decision tree; dynamic programming notices that many different partial plans lead to the same subproblem, and for later decisions only the subproblem itself (the current state) needs to be known, not how it was reached. Hence each subproblem need be solved only once and its optimal value remembered.

## 13.3. Example: Inserting Multiplication Signs into a Digit String

**Example 13.3.1** Insert $K$ multiplication signs into a digit string of length $L$ so that the resulting product is maximal. For example, inserting 3 multiplication signs into `3215125`, the maximum product is $321 \times 51 \times 2 \times 5 = 163\,710$.

First find the subproblems. Inserting $K$ multiplication signs is one overall plan, but it can be seen as deciding the positions of the signs one at a time. Consider the last sign: if it is inserted after the $i$-th digit, then the product equals "the product obtained by inserting $K - 1$ signs into the first $i$ digits" times "the number formed by the digits after it". The number after it is not affected by how signs were inserted earlier, so the earlier part should take the maximum product: this is optimal substructure (here all factors are nonnegative, so "larger times a nonnegative number is still larger" holds).

Let $D(i, j)$ be the integer formed by digits $i + 1$ through $j$, and $f(j, k)$ the maximum product obtained by inserting $k$ multiplication signs into the first $j$ digits. Then

$$
f(j, 0) = D(0, j), \qquad f(j, k) = \max_{k \leq i < j} f(i, k - 1) \cdot D(i, j) \quad (k \geq 1),
$$

and the answer is $f(L, K)$. The condition $i \geq k$ guarantees that the first $i$ digits have room for $k - 1$ signs (each segment has at least one digit). Computing in increasing order of $k$ suffices.

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

There are $(K + 1)(L + 1)$ states, and each compares at most $L$ cases. Compare brute-force enumeration: choosing $K$ of the $L - 1$ gaps for multiplication signs gives $\binom{L-1}{K}$ plans, over 600 million for $L = 40$ and $K = 10$; dynamic programming needs only a few thousand operations. When the digit string is very long, the product exceeds the range of `long long`; C++ then needs arbitrary-precision integers, whereas Python integers have no upper limit.

## 13.4. Example: Shortest Path on a Grid Map

**Example 13.4.1** The roads on a map form a grid of $4 \times 4$ intersections, with the length marked on each road segment. Starting from the lower-left intersection and moving only up or to the right, find the shortest distance to the upper-right intersection.

Denote an intersection by $(i, j)$ (row $i$, column $j$, starting from $(0, 0)$ at the lower left). Let $h_{i,j}$ be the length of the road from $(i, j)$ rightward to $(i, j+1)$, $v_{i,j}$ the length of the road from $(i, j)$ upward to $(i+1, j)$, and $d_{i,j}$ the shortest distance from the start to $(i, j)$. Since we move only up or right, the last step into $(i, j)$ comes either from below, $(i-1, j)$, or from the left, $(i, j-1)$:

$$
d_{i,j} = \min\bigl(d_{i-1,j} + v_{i-1,j},\ d_{i,j-1} + h_{i,j-1}\bigr),
$$

with boundary $d_{0,0} = 0$, and the first row and first column can be reached from only one direction. We compute in increasing order of rows and columns, or in stages by the value of $i + j$: the intersections of stage $s$ depend only on stage $s - 1$. The figure below marks the road lengths, the shortest distance to each intersection, and a shortest route (6 stages in all); the answer is 10.

![Shortest distance from the start to each intersection; orange marks one shortest route](./plots/grid-shortest-path.py)

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

"Only up or right" guarantees that the dependencies among intersections contain no cycles: every step increases $i + j$ by 1, so the states naturally fall into successive stages. If movement in all four directions were allowed, the last step into an intersection might come from an intersection not yet computed, and the table could not be filled in order so simply; shortest paths in general graphs need methods such as Dijkstra's algorithm ([4.3.11](/4.3.11)), which are likewise built on the optimal substructure that "part of a shortest path is itself a shortest path".

## 13.5. Example: Matrix Chain Multiplication

**Example 13.5.1 (Matrix Chain Multiplication)** Given $n$ matrices $A_1, A_2, \dots, A_n$, where $A_i$ has size $p_{i-1} \times p_i$. Matrix multiplication is associative, so any parenthesization gives the same result, but the number of scalar multiplications required differs. Find a parenthesization that minimizes the number of scalar multiplications needed to compute the product $A_1 A_2 \cdots A_n$.

Multiplying a $p \times q$ matrix by a $q \times r$ matrix gives a result with $pr$ entries, each needing $q$ multiplications, $pqr$ in all. Let $A$, $B$, $C$ have sizes $10 \times 100$, $100 \times 5$, and $5 \times 50$; then $(AB)C$ needs $10 \cdot 100 \cdot 5 + 10 \cdot 5 \cdot 50 = 7500$ multiplications, whereas $A(BC)$ needs $100 \cdot 5 \cdot 50 + 10 \cdot 100 \cdot 50 = 75\,000$, a tenfold difference. The number of parenthesizations is a Catalan number, which grows exponentially in $n$, so they cannot be enumerated one by one.

Consider the last multiplication: it splits $A_i \cdots A_j$ into the two parts $A_i \cdots A_k$ and $A_{k+1} \cdots A_j$ ($i \leq k < j$), whose results are matrices of sizes $p_{i-1} \times p_k$ and $p_k \times p_j$; multiplying them at the end needs $p_{i-1} p_k p_j$ multiplications, and each part should itself be computed optimally. Let $m_{i,j}$ be the minimum number of scalar multiplications needed to compute $A_i \cdots A_j$; then

$$
m_{i,i} = 0, \qquad m_{i,j} = \min_{i \leq k < j} \bigl(m_{i,k} + m_{k+1,j} + p_{i-1} p_k p_j\bigr) \quad (i < j).
$$

Computing $m_{i,j}$ needs the results of all shorter subchains, so we compute in increasing order of chain length $\ell = j - i + 1$ from 2 to $n$. At the same time we record the split point $s_{i,j} = k$ attaining the minimum, and finally output the parentheses recursively starting from $s_{1,n}$.

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

For the 6 matrices of sizes $30 \times 35$, $35 \times 15$, $15 \times 5$, $5 \times 10$, $10 \times 20$, and $20 \times 25$, at least 15125 scalar multiplications are needed, and the optimal plan is $((A_1(A_2A_3))((A_4A_5)A_6))$. There are about $n^2/2$ states $(i, j)$, each trying at most $n$ split points, so the total work is proportional to $n^3$. This state design of "choosing a split point within an interval" is called interval dynamic programming; it applies equally to optimal binary search trees, polygon triangulation, and similar problems.

## Summary

| Example | State | State transition | Order of computation |
|---|---|---|---|
| Rod cutting | $r_k$: maximum revenue of length $k$ | enumerate the length of the leftmost piece | $k$ increasing |
| Inserting multiplication signs | $f(j, k)$: $k$ signs in the first $j$ digits | enumerate the position of the last sign | $k$ increasing |
| Grid shortest path | $d_{i,j}$: shortest distance to intersection $(i, j)$ | from below or from the left | by stage $i + j$ |
| Matrix chain | $m_{i,j}$: minimum multiplications for $A_i \cdots A_j$ | enumerate the split point of the last multiplication | chain length increasing |

- Dynamic programming applies to optimization problems with optimal substructure and overlapping subproblems.
- The key is defining the state: the state must suffice to describe the subproblem, and later decisions depend only on the state itself, not on the process by which it was reached.
- There are two ways to implement it, memoized recursion and iterative table filling; recording the optimal choice of each state allows the optimal plan to be reconstructed.
