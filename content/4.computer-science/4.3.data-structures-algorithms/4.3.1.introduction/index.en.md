---
title: Introduction
description: Elements of an algorithm and finiteness (the hailstone sequence); the Turing machine and RAM models of computation; worst-case time and space complexity; big O, Omega and Theta notation and the hierarchy of complexities; analysis of series and iteration, back-of-the-envelope estimates; recursion traces, recurrence relations, the master theorem and the Akra–Bazzi theorem; four algorithms for the maximum subarray problem; dynamic programming for Fibonacci numbers and longest common subsequences.
source_hash: e599fed58bb0
---

[4.1 Programming Fundamentals](/4.1) is about how to come up with a solution: recursion, divide and conquer, backtracking, dynamic programming. This course answers two other questions: whether a solution is correct and what it costs, and how to organize data so that the common operations are all fast enough. The first question needs a machine-independent yardstick and a set of analysis tools; the second is the subject of data structures. This chapter first explains algorithms and models of computation, then builds the yardstick of asymptotic notation, then introduces the basic methods for analyzing iteration and recursion, including the master theorem for divide-and-conquer recurrences. Finally, three examples (the maximum subarray problem, Fibonacci numbers and longest common subsequences) show how algorithms for one problem improve step by step from exponential or cubic time to linear time. Every result in the later chapters (vectors, lists, stacks and queues, trees, graphs, hashing, and so on) is proved with the methods introduced here.

## 1.1. Algorithms

### 1.1.1. Computation and Algorithms

Computation is information processing carried out with some tool, according to definite rules, in an explicit and mechanical form. The tool may be a rope, a straightedge and compass, or an electronic computer; abstracting the tool into a mathematical object gives a model of computation. An **algorithm** ([4.1.1](/4.1.1)) is a sequence of instructions designed to solve a specific problem in a specific model of computation. It should satisfy the following requirements.

| Requirement | Meaning |
|---|---|
| Input and output | The input is the information to be processed (an instance of the problem); the output is the result (the answer) |
| Correctness | For every valid input, the output is the answer the problem asks for |
| Definiteness | It consists of well-defined basic operations, with no vague steps such as "add a pinch of salt" or "cook until half done" |
| Feasibility | Every basic operation can be carried out, and in constant time |
| Finiteness | For every input, an output is obtained after finitely many basic operations |

The least conspicuous of these, finiteness, is also the hardest to verify.

**Example 1.1.1 (Hailstone Sequence)** For a positive integer $n$, replace $n$ by $n/2$ if $n$ is even and by $3n + 1$ if $n$ is odd, and repeat until $n = 1$. The resulting sequence is the hailstone sequence. For example, $7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1$ has length 17.

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

The length of the sequence has no simple relation to the size of $n$: $|\mathrm{Hailstone}(27)| = 112$, whereas $|\mathrm{Hailstone}(32)| = 6$. Does this program terminate for every $n$? This is the Collatz conjecture, which remains unproved (it has been verified by computer up to about $2^{68}$); Erdős remarked that "mathematics may not be ready for such problems." Until the conjecture is proved, `hailstone()` can only be called a program, not an algorithm: a program need not be finite.

**Example 1.1.2** Let `rand()` be an ideal random number generator. The loop `while (rand() & 1);` continues each round with probability $1/2$. In principle it may run arbitrarily many rounds, but the number of rounds follows a **geometric distribution** with an **expectation** of only 2, and the probability of running forever is 0. The finiteness of a randomized algorithm must be understood in the probabilistic sense.

### 1.1.2. Good Algorithms

Correctness is only the minimum requirement. A good algorithm should also be robust (it recognizes invalid input and handles it properly instead of terminating abnormally) and readable (structured, accurately named, commented where needed), but the property that receives the most attention is efficiency: as fast as possible and using as little storage as possible. Correctness itself comes in levels: handling simple inputs, large inputs, general inputs, degenerate inputs (the empty sequence, all elements equal, and so on), and finally arbitrary valid inputs.

Wirth wrote, "Algorithms + Data Structures = Programs." A *data structure* is a way of organizing data elements together with a set of operations implemented on them; the same data organized differently makes the operations cost differently. An algorithm is efficient only on a suitable data structure, and the value of a data structure can be measured only by the algorithms it supports. The theme of this course can be summarized as "(algorithms + data structures) × efficiency = computation."

## 1.2. Models of Computation

### 1.2.1. Problem Size and the Worst Case

To compare algorithms we must first be able to measure cost. Let $T_A(P)$ be the cost of algorithm $A$ on problem instance $P$. There are too many instances to list one by one; experience shows that the size of an instance is usually the dominant factor in the cost, and instances of similar size cost about the same. So we describe the cost as a function of the size $n$. Instances of the same size can still differ greatly in cost, however. Suppose we want to decide whether any of the $\binom{n}{3}$ triangles formed by $n$ points in the plane has area at most 5: with luck the first one qualifies, and with bad luck we must enumerate them all. To be safe, we look only at the worst case.

**Definition 1.2.1 (Time Complexity)** Let $T_A(P)$ be the number of basic operations algorithm $A$ executes on instance $P$. Then

$$
T_A(n) = \max\{\, T_A(P) : P \text{ has size } n \,\}
$$
is called the (worst-case) **time complexity** of $A$, written $T(n)$ when a particular algorithm is under discussion. The best-case and average-case complexities (the expectation over some probability distribution on instances) are defined similarly.

Experiments alone are not enough to compare algorithms: different algorithms may suit different sizes and types of input, and the same algorithm may be implemented by different programmers, in different languages, with different compilers, on different architectures and operating systems. To reach objective conclusions we need an idealized platform independent of all these factors, that is, a model of computation.

### 1.2.2. The Turing Machine

A *Turing machine* has four parts: a tape that is infinite in both directions and divided evenly into cells, each holding one symbol from a finite alphabet (initially `#`); a read/write head that is always aligned with one cell, can read or overwrite its symbol, and moves to the left or right neighboring cell at each step; a controller that is always in one of finitely many states, with `h` by convention the halting state; and a transition table. Each entry of the transition function is written $(q, c;\ d, \mathrm{L}/\mathrm{R}, p)$: if the current state is $q$ and the current symbol is $c$, overwrite the symbol with $d$, move one cell left or right, and enter state $p$. The number of steps from start to halt is the cost of the computation.

**Example 1.2.1 (Binary Increment)** The head is at the lowest bit of a binary number, in state `<`. To add one, flip all the trailing 1s to 0, and flip the 0 (or blank `#`) immediately before them to 1.

| Transition | Effect |
|---|---|
| $(\texttt{<}, 1;\ 0, \mathrm{L}, \texttt{<})$ | Carry: 1 becomes 0, keep moving left |
| $(\texttt{<}, 0;\ 1, \mathrm{R}, \texttt{>})$ | Carry absorbed: 0 becomes 1, turn around |
| $(\texttt{<}, \#;\ 1, \mathrm{R}, \texttt{>})$ | The number was all 1s: write a 1 before the most significant bit |
| $(\texttt{>}, 0;\ 0, \mathrm{R}, \texttt{>})$ | Move right back to the lowest bit |
| $(\texttt{>}, \#;\ \#, \mathrm{L}, \texttt{h})$ | Step back one cell past the lowest bit and halt |

The third entry cannot be omitted; otherwise an input such as $111$ could not be handled.

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

The transition table is the "program" of this machine, and its convention with the input tape (where the head starts and where it stops) is its interface. The significance of the Turing machine is theoretical: computability (which problems can be solved by an algorithm) and the complexity classes are all defined relative to it.

### 1.2.3. The RAM Model

A Turing machine can only move one cell at a time, so reaching distant data costs time proportional to the distance, which is far from a real computer. Algorithm analysis more commonly uses the *random-access machine*:

- It has infinitely many sequentially numbered registers $R[0], R[1], \dots$, any of which can be accessed directly by its number (call-by-rank access);
- an instruction register IR indicates which instruction is executed;
- the basic operations are only a few kinds, such as assignment, arithmetic, comparison, and conditional and unconditional jumps, each taking constant time.

**Example 1.2.2 (Ceiling Division)** To compute $\lceil c/d \rceil$ ($c \geq 0$, $d > 0$), repeatedly subtract $R[1] = d$ from $R[0] = c$ and count the subtractions performed before the value becomes nonpositive.

```text
[0] R[3] <- 1              // constant 1
[1] GOTO 4                 // in case R[0] = c == 0
[2] R[2] <- R[2] + R[3]    // x++
[3] R[0] <- R[0] - R[1]    // c -= d
[4] IF R[0] > 0 GOTO 2     // if c > 0 goto 2
[5] R[0] <- R[2]           // else copy x to R[0]
[6] STOP                   // return R[0] = x = ceil(c / d)
```

For $c = 12$ and $d = 5$, 14 instructions are executed and the result is 3. In general, the time cost is the sum of the execution counts of the instructions, here $3\lceil c/d \rceil + 5$.

In the RAM model, the running time of an algorithm is the number of basic operations it executes. Each statement of a high-level language (arithmetic, comparison, assignment, array indexing, function call and return) is equivalent to a constant number of RAM instructions, and branches, loops and recursive calls are all jumps in essence. Hence, asymptotically, we may count high-level statements directly, without translating into RAM instructions.

Strictly speaking, "each register holds an arbitrarily large integer and operations take constant time" makes the model too powerful (the whole input can be encoded in one integer). Modern textbooks use the word RAM: each word has $w \geq \log_2 n$ bits, and operations on words are constant time. This course assumes this model by default: arithmetic on indices, pointers and ordinary integers takes $O(1)$.

## 1.3. Asymptotic Complexity

### 1.3.1. Big O Notation

The exact $T(n)$ is hard to find and not very important: what really matters is how the cost grows with the size once the size is large enough. This is asymptotic analysis. *Asymptotic notation* ignores constant factors and lower-order terms and keeps only the order of growth.

**Definition 1.3.1 (Big O Notation)** Let $f, g$ be functions defined on the positive integers that are eventually positive. If there exist constants $c > 0$ and $n_0$ such that $f(n) \leq c \cdot g(n)$ for all $n \geq n_0$, we write $f(n) = O(g(n))$. This notation is called **big O notation**; it gives an asymptotic upper bound on the growth rate of $f$.

**Definition 1.3.2 (Big Omega and Big Theta Notation)** If there exist $c > 0$ and $n_0$ such that $f(n) \geq c \cdot g(n)$ for all $n \geq n_0$, we write $f(n) = \Omega(g(n))$ (**big Omega notation**, an asymptotic lower bound). If $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$, we write $f(n) = \Theta(g(n))$ (**big Theta notation**, an asymptotically tight bound).

For example, for $T(n) = 3n^2 + 10n + 7$, taking $c = 4$ and $n_0 = 11$ gives $T(n) = O(n^2)$; also $T(n) \geq 3n^2$, so $T(n) = \Theta(n^2)$. The "$=$" here is a conventional abuse of notation; what it really means is that $f$ belongs to the set $O(g) = \{f : \exists c, n_0,\ \forall n \geq n_0,\ f(n) \leq c\,g(n)\}$. Hence $O(n) = O(n^2)$ is true, while the reverse is wrong. There are also strict versions: $f = o(g)$ means $f(n)/g(n) \to 0$, and $f = \omega(g)$ means $f(n)/g(n) \to \infty$.

The following rules follow directly from the definitions and are used repeatedly in analysis:

- Constant factors can be ignored: $O(c \cdot f) = O(f)$;
- addition keeps the larger term: $O(f) + O(g) = O(\max(f, g))$, so for a polynomial only the highest-degree term matters;
- multiplication multiplies: $O(f) \cdot O(g) = O(f \cdot g)$, used for nested loops;
- transitivity: $f = O(g)$ and $g = O(h)$ imply $f = O(h)$.

An "$O(n^2)$ algorithm" usually means one whose worst-case time complexity is $O(n^2)$; when this bound is tight, that is, the worst case really requires $\Theta(n^2)$, the more accurate statement is $\Theta(n^2)$. The symbol $\Omega$ is mainly used to state lower bounds on a problem: how much time every algorithm needs in the worst case ([4.3.2](/4.3.2) shows that comparison-based sorting needs $\Omega(n \log n)$ comparisons).

**Definition 1.3.3 (Space Complexity)** The amount of storage an algorithm needs during execution, beyond the space occupied by the input itself, is called its **space complexity**, written $S(n)$; as with time, we take the worst case and describe it with asymptotic notation. Space that can be reused is counted only once.

In the RAM model, every memory cell used requires at least one write, so apart from space that is allocated once and never accessed, $S(n) = O(T(n))$ always holds. This is why usually only time complexity is discussed. For recursive algorithms (the recursion depth determines the stack space, [4.3.4](/4.3.4)) and algorithms that need auxiliary arrays (such as **merge sort**), however, space complexity matters just as much.

### 1.3.2. Hierarchy of Complexities

An $O(1)$ algorithm is the most efficient, and a constant-time code segment need not be free of loops, branches or calls:

```cpp
for (i = 0; i < n; i += n / 2024 + 1);     // about 2024 iterations: O(1)
for (i = 1; i < n; i = 1 << i);            // log* n iterations: almost O(1)
if ((n + m) * (n + m) < 4 * n * m) goto UNREACHABLE;   // never taken (ignoring overflow)
```

The step size of the first loop grows with $n$, so it iterates at most 2025 times; the third condition never holds because $(n+m)^2 \geq 4nm$. What matters is the number of executions, not the shape of the code.

Next, logarithmic time $O(\log n)$. The base of the logarithm does not matter: $\log_a n = \log_b n / \log_b a$ differs only by a constant factor, so we write $O(\log n)$ without a base (in this course $\log$ without a base means base 2). A constant power does not matter either: $\log n^c = c \log n = O(\log n)$. A polynomial in the logarithm, $\log^c n$, still grows more slowly than any positive power: for any $c > 0$ and $\varepsilon > 0$, $\log^c n = o(n^\varepsilon)$. Such algorithms are extremely efficient, for example **binary search** in a sorted vector.

Among the polynomials $O(n^c)$, $O(n)$ is called linear and is the ideal goal for many problems (just reading the input takes linear time); the range from $O(n)$ to $O(n^2)$ is the main territory of the programming exercises in this course. The class of problems that have polynomial-time algorithms is denoted $\mathrm{P}$; in the view of Cobham and Edmonds, polynomial time is the standard for "efficiently computable."

Exponential time $O(2^n)$ is different: for any $c > 0$ and $a > 1$, $n^c = o(a^n)$, so exponential cost grows extremely fast and is usually considered intolerable. The step from polynomial to exponential is the watershed between efficient and inefficient algorithms. For many problems an exponential algorithm is obvious, while designing a polynomial one is extremely hard.

**Example 1.3.1 (Subset Sum Problem)** Given a set of positive integers $S = \{a_1, \dots, a_n\}$ and a target $t$, decide whether some subset sums to exactly $t$. For example, can two candidates competing for the 538 electoral votes each get exactly 269? Classifying by whether the last element is taken or not gives a direct recursion:

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

In the worst case it examines all $2^n$ subsets. The subset sum problem is NP-complete: if it had a polynomial-time algorithm, then every NP problem (a problem whose solutions can be verified in polynomial time) would too, that is, $\mathrm{P} = \mathrm{NP}$. This conjecture remains open; it is widely believed that $\mathrm{P} \neq \mathrm{NP}$, but nobody can currently prove that no polynomial algorithm exists for subset sum. Note also that **dynamic programming** solves it in $O(nt)$ time, but this is not polynomial time: in the input, $t$ occupies only $\log t$ bits, so $O(nt)$ is exponential in the input length (this is called pseudo-polynomial time).

The figure below shows the growth curves of common functions. For very small sizes, a lower-order function is not necessarily smaller ($2^n \leq n^2$ when $n \leq 4$); once the size is somewhat larger, the order of growth decides: a fast start does not win the long race.

![Growth of common complexity functions: very small sizes on the left, somewhat larger sizes on the right](./plots/growth-rates.py)

| Complexity | Name | Typical examples |
|---|---|---|
| $O(1)$ | Constant | Basic operations of data structures (call-by-rank access in a vector, push and pop of a stack) |
| $O(\log^* n)$ | Iterated logarithm | Nearly constant; the complexity of union-find is expressed with the even more slowly growing inverse Ackermann function ([4.3.11](/4.3.11)) |
| $O(\log n)$ | Logarithmic | Binary search in a sorted vector; search, insertion and deletion in balanced search trees and heaps |
| $O(n)$ | Linear | Sequential search; traversal of trees and graphs |
| $O(n \log n)$ | Linearithmic | Sorting; Huffman coding |
| $O(n^2)$ | Quadratic | Pairwise combinations of input objects; the naive Dijkstra algorithm |
| $O(n^3)$ | Cubic | Naive matrix multiplication |
| $O(n^c)$ | Polynomial | Problems in P |
| $O(2^n)$ | Exponential | Trivial algorithms for many problems (enumerating all subsets) |

Here $\log^* n$ is the number of times $\log_2$ must be applied to $n$ before the result is at most 1: $\log^* 2^{65536} = 5$, and $2^{65536}$ far exceeds the number of atoms in the universe.

## 1.4. Analysis of Iteration

### 1.4.1. Series

The complexity of an iterative algorithm usually reduces to summing a series. The following types are the most common.

| Series | Result | Remark |
|---|---|---|
| Arithmetic series $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ | $\Theta(n^2)$ | Same order as the square of the last term |
| Power series $\sum_{k=1}^{n} k^d$ | $\Theta(n^{d+1})$ | One order higher than the exponent |
| Geometric series $\sum_{k=0}^{n} a^k = \frac{a^{n+1} - 1}{a - 1}$ ($a > 1$) | $\Theta(a^n)$ | Same order as the last term |
| Convergent series, such as $\sum_{k=1}^{n} \frac{1}{k^2} < \frac{\pi^2}{6}$ | $O(1)$ | |
| **Harmonic series** $H_n = \sum_{k=1}^{n} \frac{1}{k}$ | $\ln n + \gamma + o(1) = \Theta(\log n)$ | $\gamma \approx 0.5772$ |
| Logarithmic series $\sum_{k=1}^{n} \log k = \log n!$ | $\Theta(n \log n)$ | By Stirling's formula |
| $\sum_{k=1}^{n} k \cdot 2^k = (n-1)2^{n+1} + 2$ | $\Theta(n \, 2^n)$ | |

The order of a power series can be found by squeezing with integrals: $\int_0^n x^d \,\mathrm{d}x \leq \sum_{k=1}^n k^d \leq \int_1^{n+1} x^d\,\mathrm{d}x$, and both ends are $\Theta(n^{d+1})$. The upper bound $\log n! \leq n \log n$ for the logarithmic series is obvious; for the lower bound, keep the last half of the terms: $\log n! \geq \sum_{k > n/2} \log k \geq \frac{n}{2}\log\frac{n}{2} = \Omega(n \log n)$.

Convergent series matter too: the number of basic operations is an integer, but its expected or amortized value can be a fraction. The loop in Example 1.1.2 executes $\sum_{k \geq 1} k \cdot 2^{-k} = 2$ rounds in expectation, which is a convergent series.

### 1.4.2. Loops

The number of iterations of a loop often corresponds directly to a series. Let `O1op` denote a constant-time operation.

| Loop | Executions | Complexity |
|---|---|---|
| `for (i = 0; i < n; i++)` `for (j = 0; j < n; j++) O1op;` | $n^2$ | $\Theta(n^2)$ |
| `for (i = 0; i < n; i++)` `for (j = 0; j < i; j++) O1op;` | $\sum_{i} i = \frac{n(n-1)}{2}$ | $\Theta(n^2)$ |
| `for (i = 0; i < n; i++)` `for (j = 0; j < i; j += 2024) O1op;` | $\sum_i \lceil i/2024 \rceil$ | $\Theta(n^2)$ |
| `for (i = 1; i < n; i <<= 1)` `for (j = 0; j < i; j++) O1op;` | $1 + 2 + 4 + \cdots < 2n$ | $\Theta(n)$ |
| `for (i = 0; i <= n; i++)` `for (j = 1; j < i; j += j) O1op;` | $\sum_{i} \lceil \log_2 i \rceil$ | $\Theta(n \log n)$ |

In the second row, the inner iteration counts form an arithmetic series, geometrically half of a square, still $\Theta(n^2)$. In the third row, the large step of the inner loop only changes the constant factor. In the fourth row, the outer loop runs only $\log n$ rounds, but the inner iteration counts form a geometric series, so the total is dominated by the last term. In the fifth row, $j$ doubles in the inner loop, giving $\Theta(\log i)$ iterations per round, so the total is a logarithmic series.

### 1.4.3. Back-of-the-Envelope Estimates

With asymptotic complexity we can roughly estimate the running time before implementing anything, which is a *back-of-the-envelope calculation*. Some useful orders of magnitude: a day is about $10^5$ seconds (86400), a year about $3 \times 10^7$ seconds, a century about $3 \times 10^9$ seconds, and the time since the Big Bang about $4 \times 10^{17}$ seconds. An ordinary computer executes about $10^9$ simple instructions per second, and an exascale supercomputer of the 2020s performs about $10^{18}$ floating-point operations per second.

**Example 1.4.1** Sort national census data ($n \approx 10^9$). A $\Theta(n^2)$ **bubble sort** needs about $10^{18}$ operations, which takes an ordinary computer $10^9$ seconds, more than 30 years; a $\Theta(n \log n)$ merge sort needs about $10^9 \times 30 = 3 \times 10^{10}$ operations, which an ordinary computer finishes in half a minute. Improving the algorithm beats improving the hardware: running bubble sort on an exascale supercomputer that is $10^9$ times faster (and assuming it parallelizes perfectly) still takes about 1 second; the $10^9$-fold hardware advantage barely cancels the gap between $n^2$ and $n \log n$.

## 1.5. Analysis of Recursion

### 1.5.1. Decrease and Conquer: Recursion Traces and Recurrence Relations

**Decrease and conquer** ([4.1.10](/4.1.10)) splits a problem into two subproblems, one of which is trivial while the other has a reduced size. Take array summation as an example: the sum of $n$ numbers equals the sum of the first $n - 1$ numbers plus the last one.

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

There are two ways to analyze a recursive algorithm.

1. *Recursion trace*: draw all the recursion instances that occur during the computation together with their call relations; the sum of the time each takes (not counting the recursive calls themselves) is the total running time. The summation example has $n + 1$ recursion instances, each taking $O(1)$ time, so the total time is $O(n)$.
2. *Recurrence relation*: when the size is larger and the structure more complex, the recursion trace is no longer intuitive, and we describe the cost with a recurrence. To solve a problem of size $n$, `sum` must first solve the problem of size $n - 1$ and then perform one addition:

$$
T(n) = T(n - 1) + O(1), \qquad T(0) = O(1),
$$
and unrolling gives $T(n) = O(n)$.

Both summation and reversal are linear recursion: each recursion instance calls itself at most once. Their space complexity is also $O(n)$, because the recursion depth is $n$ and $n$ stack frames coexist on the **call stack**. The recursive call in the reversal is the last step of the function (tail recursion), which can be mechanically rewritten as a loop, reducing the space to $O(1)$ ([4.3.4](/4.3.4)).

### 1.5.2. Divide and Conquer

**Divide and conquer** ([4.1.11](/4.1.11)) splits a problem into several (usually two, of roughly equal size) subproblems, solves each, and merges the results. Array summation can also be done by divide and conquer: cut the interval $[\mathit{lo}, \mathit{hi})$ at the midpoint $\mathit{mi}$, sum each half, and add the two sums.

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

Recursion trace: let $n = 2^m$. Level $k$ of the recursion tree has $2^k$ instances, each $O(1)$, so the total time is the geometric series $1 + 2 + \cdots + 2^m = 2n - 1 = O(n)$. The recurrence is

$$
T(n) = 2T(n/2) + O(1), \qquad T(1) = O(1),
$$
and setting $S(n) = T(n) + c$ turns it into $S(n) = 2S(n/2)$, which again gives $T(n) = O(n)$. Divide and conquer is no faster than decrease and conquer here (there are always $n - 1$ additions), but the recursion depth drops from $n$ to $\log n$.

### 1.5.3. The Master Theorem

The recurrence of a divide-and-conquer algorithm generally has the form $T(n) = a\,T(n/b) + f(n)$: the original problem is split into $a$ subproblems of size $n/b$, and splitting and merging take $f(n)$ time in total. Comparing $f(n)$ with $n^{\log_b a}$ gives the answer directly.

**Theorem 1.5.1 (Master Theorem)** Let the constants satisfy $a \geq 1$ and $b > 1$, let $f(n)$ be eventually positive, and let $T(n) = a\,T(n/b) + f(n)$ (where $n/b$ may be $\lfloor n/b \rfloor$ or $\lceil n/b \rceil$). Write $p = \log_b a$.

1. If $f(n) = O(n^{p - \varepsilon})$ for some $\varepsilon > 0$, then $T(n) = \Theta(n^p)$;
2. if $f(n) = \Theta(n^p \log^k n)$ for some $k \geq 0$, then $T(n) = \Theta(n^p \log^{k+1} n)$;
3. if $f(n) = \Omega(n^{p + \varepsilon})$ for some $\varepsilon > 0$, and there is $c < 1$ such that $a f(n/b) \leq c f(n)$ for all sufficiently large $n$, then $T(n) = \Theta(f(n))$.

**Proof** We prove only the case where $n$ is a power of $b$ and $k = 0$ (for the general case see Chapter 4 of CLRS). Level $j$ of the recursion tree ($0 \leq j < \log_b n$) has $a^j$ instances of size $n/b^j$, and there are $a^{\log_b n} = n^{\log_b a} = n^p$ leaves, so

$$
T(n) = \Theta(n^p) + \sum_{j=0}^{\log_b n - 1} a^j f(n/b^j).
$$
Case 1: $a^j f(n/b^j) \leq C a^j (n/b^j)^{p - \varepsilon} = C n^{p-\varepsilon} (b^{\varepsilon})^j$ (using $a = b^p$). The sum over $j$ is a geometric series with ratio $b^\varepsilon > 1$, dominated by its last term, giving $O(n^{p-\varepsilon} \cdot n^{\varepsilon}) = O(n^p)$, the same order as the leaves. Case 2: each level contributes $a^j \cdot \Theta\bigl((n/b^j)^p\bigr) = \Theta(n^p)$, and there are $\log_b n$ levels, so the total is $\Theta(n^p \log n)$. Case 3: by the regularity condition, $a^j f(n/b^j) \leq c^j f(n)$, and the sum is a geometric series with ratio $c < 1$, dominated by its first term, giving $O(f(n))$. Since also $T(n) \geq f(n)$, we get $T(n) = \Theta(f(n))$; here $f(n) = \Omega(n^{p+\varepsilon})$ also dominates the $\Theta(n^p)$ contributed by the leaves. $\square$

The three cases correspond to the cost of the recursion tree being concentrated at the leaves, spread evenly over the levels, and concentrated at the root, respectively.

| Algorithm | Recurrence | $p = \log_b a$ | Case | Result |
|---|---|---|---|---|
| Divide-and-conquer summation | $2T(n/2) + O(1)$ | 1 | 1 | $\Theta(n)$ |
| Range query in a kd-tree ([4.3.7](/4.3.7)) | $2T(n/4) + O(1)$ | $1/2$ | 1 | $\Theta(\sqrt{n})$ |
| Big-integer multiplication, naive divide and conquer | $4T(n/2) + O(n)$ | 2 | 1 | $\Theta(n^2)$ |
| Big-integer multiplication, Karatsuba | $3T(n/2) + O(n)$ | $\log_2 3$ | 1 | $\Theta(n^{1.585})$ |
| Binary search | $T(n/2) + O(1)$ | 0 | 2, $k = 0$ | $\Theta(\log n)$ |
| Merge sort | $2T(n/2) + O(n)$ | 1 | 2, $k = 0$ | $\Theta(n \log n)$ |
| In-place merge sort without a buffer | $2T(n/2) + O(n \log n)$ | 1 | 2, $k = 1$ | $\Theta(n \log^2 n)$ |
| Quickselect (average case, [4.3.14](/4.3.14)) | $T(n/2) + O(n)$ | 0 | 3 | $\Theta(n)$ |

Big-integer multiplication deserves a few more words. Split two $n$-digit numbers into high and low halves, $x = x_1 B + x_0$ and $y = y_1 B + y_0$ ($B$ the base corresponding to $n/2$ digits). Then $xy = x_1 y_1 B^2 + (x_1 y_0 + x_0 y_1) B + x_0 y_0$, which naively needs 4 multiplications of half length. Karatsuba (1960) observed that

$$
x_1 y_0 + x_0 y_1 = (x_1 + x_0)(y_1 + y_0) - x_1 y_1 - x_0 y_0,
$$
so only 3 multiplications are needed, plus a few linear-time additions and subtractions, and the complexity drops from $\Theta(n^2)$ to $\Theta(n^{\log_2 3})$. This was the first multiplication algorithm to break quadratic complexity; the best known in theory is the $O(n \log n)$ algorithm of Harvey and van der Hoeven (2019). CPython's integer multiplication uses the Karatsuba algorithm for numbers with many digits.

The in-place merge sort without a buffer in the table corresponds to the fallback of C++ `std::stable_sort` when no extra memory can be allocated ([4.2.10](/4.2.10)).

### 1.5.4. The Akra–Bazzi Theorem

There are gaps between the three cases of the master theorem. For example, in $T(n) = 2T(n/2) + n / \log n$, $f(n)$ is smaller than $n^1$ but not smaller by a polynomial factor, so none of the three cases applies. Moreover, the subproblems may have unequal sizes. A more general tool is the theorem of Akra and Bazzi (1998).

**Theorem 1.5.2 (Akra–Bazzi Theorem)** Suppose that for sufficiently large $x$,

$$
T(x) = g(x) + \sum_{i=1}^{k} a_i\, T\bigl(b_i x + h_i(x)\bigr),
$$
where the constants satisfy $a_i > 0$ and $0 < b_i < 1$, $g(x)$ is nonnegative and polynomially bounded (there is $c$ with $g(x) = O(x^c)$, and the values of $g$ on $[b_i x, x]$ differ from each other by at most a constant factor), and the perturbation terms satisfy $|h_i(x)| = O(x / \log^2 x)$ (which allows rounding). Let $p$ be the unique real number with $\sum_{i=1}^{k} a_i b_i^p = 1$. Then

$$
T(x) = \Theta\Bigl(x^p \Bigl(1 + \int_1^x \frac{g(u)}{u^{p+1}}\,\mathrm{d}u\Bigr)\Bigr).
$$

Note that the conclusion does not depend on $h_i$: rounding does not affect the asymptotic result. A few examples:

- $T(n) = 2T(n/2) + n/\log n$: $p = 1$ and $\int_2^x \frac{\mathrm{d}u}{u \ln u} = \Theta(\log\log x)$, so $T(n) = \Theta(n \log\log n)$.
- Linear-time selection ([4.3.14](/4.3.14)) with elements split into groups of 5 gives $T(n) = T(n/5) + T(7n/10) + \Theta(n)$. Since $\frac15 + \frac{7}{10} < 1$, the solution has $p < 1$ and the integral $\int_1^x u^{-p}\,\mathrm{d}u = \Theta(x^{1-p})$, so $T(n) = \Theta(n)$.
- With groups of 3 instead, $T(n) = T(n/3) + T(2n/3) + \Theta(n)$, so $p = 1$ and the integral is $\Theta(\log x)$, giving $T(n) = \Theta(n \log n)$: the group size decides whether the algorithm is linear.

### 1.5.5. Example: Maximum Subarray

The *maximum subarray problem*: given an integer sequence $A[0, n)$, find the sum of the nonempty segment $A[\mathit{lo}, \mathit{hi})$ with the largest total. It is a classic example of one problem having several algorithms of different complexities.

1. Brute force: enumerate all $\Theta(n^2)$ segments and sum each in $O(n)$ time, for $\Theta(n^3)$ in total.
2. Incremental: the sums of segments with the same start are related, $\operatorname{sum}[\mathit{lo}, \mathit{hi}+1) = \operatorname{sum}[\mathit{lo}, \mathit{hi}) + A[\mathit{hi}]$. Fixing the start and advancing the end, each segment needs only $O(1)$ time, so $\Theta(n^2)$ in total.
3. Divide and conquer: cut at the midpoint $\mathit{mi}$. The best segment lies entirely in the left half, entirely in the right half (both solved recursively), or crosses the cut. A segment crossing the cut is necessarily a nonempty suffix of the left half joined with a nonempty prefix of the right half, and the two can be maximized independently: scan left from $\mathit{mi}$ for the maximum suffix sum and right for the maximum prefix sum, $O(n)$ in total. Hence $T(n) = 2T(n/2) + O(n) = O(n \log n)$.
4. Linear scan: let $s_k$ be the maximum sum of a segment ending at $A[k]$. A segment ending at $A[k]$ either contains only $A[k]$ or extends one cell further some segment ending at $A[k-1]$, so

$$
s_k = \max(s_{k-1}, 0) + A[k], \qquad \text{answer} = \max_{0 \leq k < n} s_k.
$$
The meaning is that a prefix with nonpositive sum does not help what follows and can simply be cut off. One scan takes $O(n)$ time and $O(1)$ space (this algorithm is often called Kadane's algorithm).

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

The main program uses the brute-force algorithm as the standard and checks the other three algorithms on 1000 sets of random data (**differential testing**, [4.1.5](/4.1.5)), then prints the four results for one example (all 17, corresponding to the segment $7, 2, 6, -9, 5, 6$). The linear scan is already optimal: any algorithm must read the whole input, since an unread element could be a huge positive number.

## 1.6. Introduction to Dynamic Programming

### 1.6.1. Fibonacci Numbers: Why Recursion Is Slow

The basic idea of **dynamic programming** ([4.1.13](/4.1.13)) can be seen clearly through the Fibonacci numbers. Recursing directly from the definition, `fib(n)` calls `fib(n-1)` and `fib(n-2)`, and the cost satisfies

$$
T(n) = T(n-1) + T(n-2) + 1, \qquad T(0) = T(1) = 1.
$$
Let $S(n) = \frac{T(n) + 1}{2}$. Then $S(n) = S(n-1) + S(n-2)$ with $S(0) = S(1) = 1$, that is, $S(n) = F_{n+1}$, so $T(n) = 2F_{n+1} - 1 = \Theta(\phi^n)$, where $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$. A back-of-the-envelope estimate: $\phi^{43} \approx 10^9$, $\phi^{67} \approx 10^{14}$, $\phi^{92} \approx 10^{19}$; on a computer performing $10^9$ operations per second, `fib(43)` takes about 1 second, `fib(67)` about a day, and `fib(92)` nearly eight hundred years.

The root of the inefficiency is the large number of repeated recursion instances: there are $\Theta(\phi^n)$ instances in total, but only $n + 1$ distinct ones. There are two ways to eliminate the repetition.

1. **Memoization** ([4.1.10](/4.1.10)): keep the top-down recursion, but record computed results in a table and look them up when encountered again. Both time and space are $O(n)$.
2. Dynamic programming: reverse the direction of computation, replacing top-down recursion by bottom-up iteration, computing in the order $F_0, F_1, F_2, \dots$, where each term depends only on the previous two.

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

The C++ version completes $(f, g) \gets (g, f + g)$ in the two steps $g \gets g + f$ and $f \gets g - f$, with no third variable; the convention $F_{-1} = 1$ makes the recurrence valid from $k = 0$. Time is $O(n)$ and space is $O(1)$.

### 1.6.2. Longest Common Subsequence

**Definition 1.6.1 (Longest Common Subsequence)** A sequence formed by some elements of a sequence, in their original relative order, is called a **subsequence** of it (the elements need not be adjacent). The longest among the common subsequences of two sequences is called their **longest common subsequence** (LCS).

For example, one longest common subsequence of `EDUCATIONAL` and `ADVANTAGE` is `DATA`, of length 4. The longest common subsequence may not be unique; tools such as `diff` that compare files, and DNA sequence alignment, are based on it.

For $A[0, n)$ and $B[0, m)$, let $\operatorname{LCS}(n, m)$ be the length of their longest common subsequence. Comparing the last elements gives only three cases:

1. If $n = 0$ or $m = 0$, then $\operatorname{LCS}(n, m) = 0$ (the base case, always reachable);
2. if $A[n-1] = B[m-1]$, then $\operatorname{LCS}(n, m) = \operatorname{LCS}(n-1, m-1) + 1$ (decrease and conquer);
3. if $A[n-1] \neq B[m-1]$, then $\operatorname{LCS}(n, m) = \max\bigl(\operatorname{LCS}(n, m-1), \operatorname{LCS}(n-1, m)\bigr)$ (divide and conquer).

Correctness of case 2: let $C$ be a longest common subsequence and $x = A[n-1] = B[m-1]$. If the last element of $C$ is not $x$, then $C$ uses neither $A[n-1]$ nor $B[m-1]$, and appending $x$ gives a longer common subsequence, a contradiction. So $C$ ends with $x$, and this $x$ can be matched exactly to $A[n-1]$ and $B[m-1]$; removing it leaves a common subsequence of $A[0, n-1)$ and $B[0, m-1)$. Case 3: the last element of $C$ cannot correspond to both $A[n-1]$ and $B[m-1]$ (they differ), so $C$ is a common subsequence of $A[0, n-1)$ and $B$, or of $A$ and $B[0, m-1)$.

With direct recursion, each comparison shortens at least one sequence by one element, so the best case (for example, two identical sequences) takes only $O(n + m)$ time. In the worst case (for example, two sequences with no common element), however, the subproblems are not only numerous but heavily repeated: the subproblem $\operatorname{LCS}(a, b)$ may be computed as many as $\binom{(n-a) + (m-b)}{n-a}$ times, and when $n = m$, $\operatorname{LCS}(1, 1)$ is computed $\binom{2n-2}{n-1} = \Theta(4^n / \sqrt{n})$ times. Yet there are only $(n+1)(m+1)$ distinct subproblems, each corresponding to a pair of prefixes of $A$ and $B$. Arranging them in a table and computing row by row from $\operatorname{LCS}(0, \cdot)$ and $\operatorname{LCS}(\cdot, 0)$ up to $\operatorname{LCS}(n, m)$ gives a dynamic programming algorithm with $O(nm)$ time. Once the table is filled, tracing back from $(n, m)$ along the source of each value recovers a longest common subsequence: each solution corresponds to a monotone path in the table from $(0, 0)$ to $(n, m)$.

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

If only the length is needed, row $i$ depends only on row $i - 1$, so keeping two rows suffices and the space drops to $O(\min(n, m))$. If we need both the solution and the savings in space, Hirschberg's divide-and-conquer algorithm does it in $O(nm)$ time and $O(n + m)$ space.

## Summary

| Topic | Key points |
|---|---|
| Algorithm | Input, output, correctness, definiteness, feasibility, finiteness; finiteness is not always easy to decide (hailstone) |
| Models of computation | The Turing machine serves computability theory; in the (word) RAM model, running time = number of basic operations |
| Complexity | Worst-case $T(n)$ and $S(n)$; $O$ upper bound, $\Omega$ lower bound, $\Theta$ tight bound |
| Hierarchy | $1 \prec \log^* n \prec \log n \prec \sqrt n \prec n \prec n\log n \prec n^2 \prec n^3 \prec 2^n$; polynomial vs. exponential is the watershed between efficient and inefficient |
| Iteration | Reduces to series: arithmetic $\Theta(n^2)$, geometric dominated by the last term, harmonic $\Theta(\log n)$, logarithmic $\Theta(n \log n)$ |
| Recursion | Recursion trace or recurrence relation; $T(n) = aT(n/b) + f(n)$ by the master theorem, unequal splits by the Akra–Bazzi theorem |
| Improving algorithms | Maximum subarray: $n^3 \to n^2 \to n \log n \to n$; Fibonacci and LCS: remove repeated subproblems, exponential $\to$ polynomial |
