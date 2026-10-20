---
title: Sorting and Selection
description: The pivot and four partitioning schemes of quicksort (LUG, DUP, LGU, three-way); recursion depth, randomization and the analysis of the expected number of comparisons; introsort; the selection problem with majority elements, the median of two sorted vectors, heap-based selection, quickselect and linear-time selection; the gap sequences of Shellsort and the complexity of the Shell, PS, Pratt and Sedgewick sequences.
source_hash: c8814178dcc1
---

Sorting is the most thoroughly studied problem in algorithms courses, and the previous chapters have already covered bubble sort, selection sort, insertion sort, merge sort, heapsort and **tournament sort**. This chapter first returns to **quicksort**: its basic idea and implementation were presented in [4.1.11](/4.1.11), and here we are concerned with several ways of writing the partition and their behavior in the presence of equal elements, with the recursion depth and auxiliary space, and with the expected number of comparisons after randomization. We then discuss the selection problem, which is closely related to sorting: without sorting completely, how do we find the $k$-th smallest element, the median or the majority element? The partitioning idea of quicksort gives quickselect with expected linear time, and adding the "median of medians" gives a selection algorithm that runs in linear time even in the worst case. Finally we discuss Shellsort, whose analysis connects the cost of sorting with **inversions** and with linear combinations in number theory, and which still has unsolved problems. The $\Omega(n \log n)$ lower bound for comparison-based sorting is in Theorem 2.5.3, and non-comparison methods such as hashing and bucket sort are in [4.3.9](/4.3.9).

## 14.1. Quicksort: Pivots and Partitioning

### 14.1.1. Pivots

For merge sort, based on **divide and conquer**, the difficulty lies in "combining"; for quicksort it lies in "dividing": divide the sequence into a front part and a back part such that every element of the prefix is no greater than every element of the suffix; after the two parts are sorted recursively, the original sequence is automatically sorted. The partition is carried out around a special element.

**Definition 14.1.1 (Pivot)** An element of a sequence that is no smaller than all elements to its left and no greater than all elements to its right is called a **pivot** of the sequence.

A pivot is necessarily already in place: its position in the sorted sequence is its present position (but not conversely). Furthermore, a sequence is sorted if and only if all of its elements are pivots, so quicksort is the process of turning all elements into pivots one by one. The bad news is that a sequence need not have any pivot: for example, a sorted sequence rotated by one position (`2 3 4 5 1`) has no element in its place and hence no pivot. The good news is that only a few swaps are needed to make any given element a pivot. The question is how to swap and at what cost. The four partitioning methods below all put a randomly chosen candidate (called the pivot below) into its correct position; the "two-way scan" in [4.1.11](/4.1.11) is the first of them.

### 14.1.2. The LUG Version: Eager to Expand, Lazy to Swap

Take any candidate (for example, swap a randomly chosen element to the front), and store it aside, leaving a "hole" at the front. The sequence is divided into three segments: every element of the prefix $L$ is no greater than the pivot, every element of the suffix $G$ is no smaller than the pivot, and the middle segment $U$ has not yet been examined. We alternately expand $G$ leftward from the right end and $L$ rightward from the left end: when scanning from right to left, elements no smaller than the pivot stay in place, and upon meeting a smaller one we move it into the hole at the left end, whereupon the hole moves to the right end; scanning from left to right is symmetric. When the two ends meet, $U$ is empty, and putting the pivot into the last hole makes it a pivot in the true sense.

- Each element moves at most once (the candidate twice), $O(n)$ time in total, with only $O(1)$ additional space (in place).
- Not stable: the two ends are scanned in opposite directions, so equal elements may be reversed.

### 14.1.3. Equal Elements: The DUP Version

The scan of the LUG version leaves all elements equal to the pivot in place. If the sequence contains many elements equal to the pivot, they all stay in $G$ (or in $L$), the partition point is close to an endpoint, and the partition is extremely unbalanced: the recursion depth approaches $n$ and the running time approaches $\Theta(n^2)$. Awkwardly, when all elements are equal the sequence is in fact already sorted and need not be sorted at all.

It suffices to change the conditions of the two scanning loops from "continue if no smaller (no greater)" to "continue only if greater (smaller)": the scan stops at an element equal to the pivot and moves it to the other end. Then consecutive equal elements are distributed alternately to both sides, $\mathit{lo}$ and $\mathit{hi}$ move alternately, and the partition point is close to the midpoint of the interval. Switching from "eager to expand, lazy to swap" to "lazy to expand, eager to swap" increases the number of swaps and makes the sort less stable, but does not substantially increase the complexity on general inputs. Note that the scans must be written in the form "move one step first, then check" (`do`–`while`); otherwise the algorithm would spin in place when both ends stop at equal elements.

### 14.1.4. The LGU Version: One-Directional Scan

Another idea is a one-directional scan from left to right, maintaining three segments: the elements of $L = A(\mathit{lo}, \mathit{mi}]$ are smaller than the pivot, those of $G = A(\mathit{mi}, k)$ are no smaller than the pivot, $U = A[k, \mathit{hi})$ has not been examined, and the pivot is stored temporarily in $A[\mathit{lo}]$. To examine $A[k]$: if it is no smaller than the pivot, simply expand $G$ to the right by one position ($k$ increases by 1); otherwise swap it with the first element $A[\mathit{mi}+1]$ of $G$, which amounts to expanding $L$ to the right by one position and "rolling" $G$ back by one position as a whole. After the scan, swap $A[\mathit{lo}]$ with $A[\mathit{mi}]$ to put the pivot in place, giving $A[\mathit{lo}, \mathit{mi}) < A[\mathit{mi}] \le A(\mathit{mi}, \mathit{hi})$. This formulation (N. Lomuto) is the simplest and the easiest to prove correct; its drawbacks are that it makes more swaps and that all elements equal to the pivot go into $G$, so, like the LUG version, it degrades on many equal elements. Its one-directional scan is also exactly what quickselect below needs.

### 14.1.5. Three-Way Partitioning

The most thorough way to handle equal elements is *three-way partitioning*: divide the sequence into three segments of elements smaller than, equal to and greater than the pivot. E. W. Dijkstra proposed a single-pass algorithm under the name of the "Dutch national flag problem": maintain $A[\mathit{lo}, \mathit{lt})$ smaller than the pivot, $A[\mathit{lt}, i)$ equal to the pivot, $A[\mathit{gt}, \mathit{hi})$ greater than the pivot, with $A[i, \mathit{gt})$ not yet examined; to examine $A[i]$, if it is smaller than the pivot, swap it with $A[\mathit{lt}]$ and advance both pointers; if greater, swap it with $A[\mathit{gt}-1]$ and move $\mathit{gt}$ back; if equal, advance $i$. After partitioning, the middle segment is entirely in place, and only the two ends need to be processed recursively. When all elements are equal, a single partitioning pass finishes the job; in general, if the input has only $d$ distinct keys, the expected time of three-way quicksort is of order $O(n \log d)$, optimal up to a constant factor (Sedgewick and Bentley). The price is that each element may need two comparisons; the formulation of J. Bentley and M. D. McIlroy (1993) first swaps equal elements to the two ends and moves them back to the middle after partitioning, reducing this overhead.

The implementation below writes the four partitioning methods as functions returning the "interval of the pivot" $[l, g)$, to be called from the same quicksort framework: a two-way partition returns $[\mathit{mi}, \mathit{mi}+1)$, and a three-way partition returns the segment equal to the pivot. The sort recurses only on the shorter side and continues looping on the longer side, for reasons explained in §14.2.1.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

using Vec = std::vector<int>;
using Range = std::pair<std::size_t, std::size_t>;  // [first, last) of the pivot(s)
std::mt19937 rng(14);

int random_pivot(Vec& a, std::size_t lo, std::size_t hi) {  // moved to a[lo]
    std::swap(a[lo], a[lo + rng() % (hi - lo)]);
    return a[lo];
}

// LUG: L (keys <= pivot) grows from the left end, G (keys >= pivot) from the right,
// the unknown part U lies in between; a[lo] or a[hi] is always a "hole".
Range partition_lug(Vec& a, std::size_t lo, std::size_t hi) {
    int pivot = random_pivot(a, lo, hi);              // a[lo] is the first hole
    while (lo < hi) {
        do --hi; while (lo < hi && pivot <= a[hi]);   // grow G: equal keys stay right
        if (lo < hi) a[lo] = a[hi];                   // a smaller key moves to L
        do ++lo; while (lo < hi && a[lo] <= pivot);   // grow L: equal keys stay left
        if (lo < hi) a[hi] = a[lo];                   // a larger key moves to G
    }                                                 // now lo == hi or lo == hi + 1
    a[hi] = pivot;
    return {hi, hi + 1};
}

// DUP: the same, except that the scans stop at keys equal to the pivot,
// so equal keys are moved alternately to L and G.
Range partition_dup(Vec& a, std::size_t lo, std::size_t hi) {
    int pivot = random_pivot(a, lo, hi);
    while (lo < hi) {
        do --hi; while (lo < hi && pivot < a[hi]);
        if (lo < hi) a[lo] = a[hi];
        do ++lo; while (lo < hi && a[lo] < pivot);
        if (lo < hi) a[hi] = a[lo];
    }
    a[hi] = pivot;
    return {hi, hi + 1};
}

// LGU: a[lo] = pivot, L = a(lo, mi] < pivot, G = a(mi, k) >= pivot, U = a[k, hi).
Range partition_lgu(Vec& a, std::size_t lo, std::size_t hi) {
    int pivot = random_pivot(a, lo, hi);
    std::size_t mi = lo;
    for (std::size_t k = lo + 1; k < hi; ++k)
        if (a[k] < pivot) std::swap(a[++mi], a[k]);  // L grows, G rolls to the right
    std::swap(a[lo], a[mi]);
    return {mi, mi + 1};
}

// Three-way (Dijkstra): a[lo, lt) < pivot, a[lt, i) == pivot, a[gt, hi) > pivot.
Range partition_3way(Vec& a, std::size_t lo, std::size_t hi) {
    int pivot = random_pivot(a, lo, hi);
    std::size_t lt = lo, i = lo, gt = hi;
    while (i < gt) {
        if (a[i] < pivot) std::swap(a[lt++], a[i++]);
        else if (pivot < a[i]) std::swap(a[i], a[--gt]);
        else ++i;
    }
    return {lt, gt};
}

// Recurse on the smaller side, loop on the larger: the stack depth is O(log n).
template <typename Partition>
void quick_sort(Vec& a, std::size_t lo, std::size_t hi, Partition part) {
    while (hi - lo > 1) {
        auto [l, g] = part(a, lo, hi);
        if (l - lo < hi - g) { quick_sort(a, lo, l, part); lo = g; }
        else                 { quick_sort(a, g, hi, part); hi = l; }
    }
}

int main() {
    std::vector<std::pair<const char*, Range (*)(Vec&, std::size_t, std::size_t)>> methods = {
        {"LUG", partition_lug}, {"DUP", partition_dup},
        {"LGU", partition_lgu}, {"3-way", partition_3way}};
    for (auto [name, part] : methods) {
        Vec a = {6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2};
        quick_sort(a, 0, a.size(), part);
        std::cout << std::format("{:>5}:", name);
        for (int x : a) std::cout << std::format(" {}", x);
        std::cout << '\n';
        for (int trial = 0; trial < 2000; ++trial) {  // differential test against std::sort
            Vec v(rng() % 100);
            int range = 1 + static_cast<int>(rng() % 20);  // many equal keys
            for (int& x : v) x = static_cast<int>(rng() % range);
            Vec ref = v;
            std::sort(ref.begin(), ref.end());
            quick_sort(v, 0, v.size(), part);
            if (v != ref) { std::cout << "mismatch\n"; return 1; }
        }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random

rng = random.Random(14)


def random_pivot(a: list, lo: int, hi: int):
    """Move a random element of a[lo:hi] to a[lo] and return it."""
    k = rng.randrange(lo, hi)
    a[lo], a[k] = a[k], a[lo]
    return a[lo]


def partition_lug(a: list, lo: int, hi: int) -> tuple[int, int]:
    """L (<= pivot) grows from the left, G (>= pivot) from the right."""
    pivot = random_pivot(a, lo, hi)               # a[lo] is the first hole
    while lo < hi:
        hi -= 1
        while lo < hi and pivot <= a[hi]:         # grow G: equal keys stay right
            hi -= 1
        if lo < hi:
            a[lo] = a[hi]                         # a smaller key moves to L
        lo += 1
        while lo < hi and a[lo] <= pivot:         # grow L: equal keys stay left
            lo += 1
        if lo < hi:
            a[hi] = a[lo]                         # a larger key moves to G
    a[hi] = pivot                                 # now lo == hi or lo == hi + 1
    return hi, hi + 1


def partition_dup(a: list, lo: int, hi: int) -> tuple[int, int]:
    """As LUG, but the scans stop at keys equal to the pivot."""
    pivot = random_pivot(a, lo, hi)
    while lo < hi:
        hi -= 1
        while lo < hi and pivot < a[hi]:
            hi -= 1
        if lo < hi:
            a[lo] = a[hi]
        lo += 1
        while lo < hi and a[lo] < pivot:
            lo += 1
        if lo < hi:
            a[hi] = a[lo]
    a[hi] = pivot
    return hi, hi + 1


def partition_lgu(a: list, lo: int, hi: int) -> tuple[int, int]:
    """a[lo] = pivot, L = a[lo+1:mi+1] < pivot, G = a[mi+1:k] >= pivot."""
    pivot = random_pivot(a, lo, hi)
    mi = lo
    for k in range(lo + 1, hi):
        if a[k] < pivot:                          # L grows, G rolls to the right
            mi += 1
            a[mi], a[k] = a[k], a[mi]
    a[lo], a[mi] = a[mi], a[lo]
    return mi, mi + 1


def partition_3way(a: list, lo: int, hi: int) -> tuple[int, int]:
    """Dijkstra: a[lo:lt] < pivot, a[lt:i] == pivot, a[gt:hi] > pivot."""
    pivot = random_pivot(a, lo, hi)
    lt, i, gt = lo, lo, hi
    while i < gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt, i = lt + 1, i + 1
        elif pivot < a[i]:
            gt -= 1
            a[i], a[gt] = a[gt], a[i]
        else:
            i += 1
    return lt, gt


def quick_sort(a: list, lo: int, hi: int, part) -> None:
    """Recurse on the smaller side, loop on the larger: depth O(log n)."""
    while hi - lo > 1:
        l, g = part(a, lo, hi)
        if l - lo < hi - g:
            quick_sort(a, lo, l, part)
            lo = g
        else:
            quick_sort(a, g, hi, part)
            hi = l


for name, part in [("LUG", partition_lug), ("DUP", partition_dup),
                   ("LGU", partition_lgu), ("3-way", partition_3way)]:
    a = [6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2]
    quick_sort(a, 0, len(a), part)
    print(f"{name:>5}:", *a)
    for trial in range(2000):                     # differential test against sorted()
        keys = rng.randint(1, 20)                 # many equal keys
        v = [rng.randrange(keys) for _ in range(rng.randrange(100))]
        ref = sorted(v)
        quick_sort(v, 0, len(v), part)
        assert v == ref
print("random tests passed")
```

The figure below shows the number of comparisons of the four partitioning methods when the input has only $d$ distinct keys. LUG and LGU degrade to quadratic time when there are many equal elements (for $d = 1$ the number of comparisons is about 50 times $n \log_2 n$); DUP stays at the order of $n \log n$ for every $d$; three-way partitioning is the fastest for small $d$, and slightly slower when all keys are distinct because of the two comparisons per element.

![Comparisons of the four partitioning schemes with many equal elements: LUG and LGU degrade to quadratic time for very small d, while DUP and three-way partitioning stay at the order of n log n](./plots/duplicate-keys.py)

## 14.2. Quicksort: Performance Analysis

### 14.2.1. Recursion Depth and Auxiliary Space

The auxiliary space of quicksort is the depth of the recursion. In the best case every partition is balanced and the depth is $O(\log n)$; in the worst case every partition leans to one side and the depth is $\Theta(n)$, enough to cause a stack overflow at large sizes. The worst cases for time and for space can be handled separately: whether or not the partitions are balanced, the recursion depth can be kept at $O(\log n)$.

**Theorem 14.2.1** If after each partition we recurse only on the shorter side and continue iterating at the current level on the longer side, then the recursion depth does not exceed $\log_2 n$.

**Proof** Each time we enter a level of recursion, the length of the subinterval being processed is at most half the length of the interval at the previous level (the shorter side is at most half), and an interval of length 1 is not recursed on, so the recursion has at most $\log_2 n$ levels. $\square$

This technique is equivalent to eliminating tail recursion by hand. One can also avoid recursion altogether and keep the subintervals to be sorted in an explicit **stack**: after each partition, push the longer subinterval first and the shorter one afterwards, so that the shorter one is processed first, and the size of the stack is again $O(\log n)$ (provable by induction on $n$). Note that this controls only space and does not change time: in the worst case there are still $\Theta(n)$ unbalanced partitions, for a total time of $\Theta(n^2)$.

### 14.2.2. Randomization and Recursion Depth

In the best case every partition is close to the average, the pivot is always near the center, and the time is $O(n \log n)$, meeting the lower bound; in the worst case every partition is extremely unbalanced (for example the pivot is always the smallest or largest element), the time is $\Theta(n^2)$, and quicksort keeps company with bubble sort. Strategies such as choosing the pivot at random or the median of three can only lower the probability of the worst case, not rule it out. If so, why is it still called "quick" sort? Because the probability of the worst case is extremely low and does not depend on the input: for any input, as long as the random numbers are truly random, the algorithm finishes quickly with overwhelming probability.

A pivot that falls in the middle half of the interval (with rank between $n/4$ and $3n/4$) is called a "good pivot", which has probability about $1/2$ under random selection. A good pivot makes both sides at most $3/4$ of the original length. With median-of-three (choose three elements at random and take their median as the pivot), the probability of a good pivot rises to

$$
1 - 2\left[\binom{3}{2}\left(\frac14\right)^2 \frac34 + \left(\frac14\right)^3\right] = 1 - \frac{20}{64} = \frac{11}{16} \approx 0.69.
$$

**Theorem 14.2.2** With randomly chosen pivots, the recursion depth of quicksort is at most $8 \log_{4/3} n = O(\log n)$ with probability at least $1 - n^{-2}$.

**Proof** Fix an element $x$ and consider the sequence of partitions undergone by the subinterval containing $x$. Each time a good pivot is met, the length of the subinterval containing $x$ becomes at most $3/4$ of the original, so there are at most $k = \log_{4/3} n$ good pivots on this path. At each level, the conditional probability that the pivot is good is about $1/2$, and the random choices at different levels are independent, so a path of length exceeding $L = 8k$ means fewer than $k$ successes in $L$ independent trials. Let $X$ be the number of successes, so $\mathbb{E}[X] = L/2 = 4k$; by the Chernoff bound,

$$
\mathbb{P}(X < k) = \mathbb{P}\bigl(X < (1 - \tfrac34)\,\mathbb{E}[X]\bigr) \le \exp\!\left(-\frac{(3/4)^2 \cdot 4k}{2}\right) = \mathrm{e}^{-9k/8} = n^{-9/(8 \ln(4/3))} < n^{-3}.
$$

Taking a union over all $n$ elements, the probability that the recursion depth exceeds $L$ is less than $n \cdot n^{-3} = n^{-2}$. $\square$

The constants in the theorem were chosen for convenience of proof; the actual expected recursion depth is about $4.31 \ln n \approx 2.99 \log_2 n$ (Devroye, 1986). Intuitively, unless the pivot leans too far to one side, each partition effectively shortens the recursion path; a good pivot appears at each level with constant probability, and as soon as $O(\log n)$ of them appear, the recursion necessarily terminates.

### 14.2.3. The Expected Number of Comparisons

Suppose the $n$ input elements are distinct and the pivot is chosen uniformly at random. Let $T(n)$ be the expected number of comparisons. One partition needs $n - 1$ comparisons, and the rank of the pivot is equally likely to be $0, 1, \dots, n-1$, so

$$
T(n) = (n - 1) + \frac{1}{n}\sum_{k=0}^{n-1}\bigl[T(k) + T(n - k - 1)\bigr] = (n - 1) + \frac{2}{n}\sum_{k=0}^{n-1} T(k).
$$

Multiplying both sides by $n$ and subtracting the same equation for $n - 1$ eliminates the sum and yields the result below. Here we give another, more illuminating proof.

**Theorem 14.2.3** For $n$ distinct elements, quicksort with random pivots makes an expected number of comparisons

$$
T(n) = 2(n + 1)H_n - 4n \approx 2n \ln n \approx 1.386\, n \log_2 n,
$$
where $H_n = 1 + \frac12 + \cdots + \frac1n$ is the harmonic number.

**Proof** (backward analysis) Let the sorted output sequence be $s_0 < s_1 < \cdots < s_{n-1}$. This output is independent of which algorithm is used, so we can turn things around and analyze the course of the algorithm starting from the output. Comparisons happen only between a pivot and other elements, and any pair of elements is compared at most once (after the comparison the pivot is in place and takes no part in later comparisons), so the expected number of comparisons equals the sum over all pairs $(s_i, s_j)$ of the probability that the pair is compared during sorting.

The course of quicksort can be understood as turning all elements into pivots one by one. For $i < j$, consider the $j - i + 1$ elements $s_i, s_{i+1}, \dots, s_j$: until one of them is chosen as a pivot, they always lie in the same subinterval; whether other elements are converted earlier or later than these is irrelevant to whether $s_i$ and $s_j$ are compared. If the first of them chosen as pivot is $s_i$ or $s_j$, the two are compared; if it is some $s_k$ strictly between them, the two are separated to different sides and will never be compared. Since pivots are chosen uniformly at random, each of these $j - i + 1$ elements is equally likely to be chosen first, so

$$
\mathbb{P}(s_i \text{ is compared with } s_j) = \frac{2}{j - i + 1}.
$$

Summing, with $d = j - i$:

$$
T(n) = \sum_{d=1}^{n-1} (n - d)\,\frac{2}{d + 1} = \sum_{k=2}^{n} \frac{2(n + 1 - k)}{k} = 2(n + 1)(H_n - 1) - 2(n - 1) = 2(n+1)H_n - 4n. \qquad \square
$$

Since $H_n = \ln n + O(1)$, the expected number of comparisons is about $2 n \ln n \approx 1.386\, n \log_2 n$, about 39% more than the lower bound $\log_2 n! \approx n \log_2 n - 1.44n$. With median-of-three, the expected number of comparisons drops to about $\frac{12}{7} n \ln n \approx 1.188\, n \log_2 n$. The figure below compares the measured numbers of comparisons of three $O(n \log n)$ sorting algorithms on random permutations:

![Comparisons on random permutations: merge sort is closest to the lower bound log2 n!, quicksort uses about 2 ln n, and heapsort about 2 log2 n](./plots/comparison-counts.py)

### 14.2.4. Quicksort in Practice

The number of comparisons is not everything. The table below compares various sorting algorithms on vectors from several viewpoints:

| Algorithm | Comparisons | Element moves | Additional space | Stable | Locality of reference |
|---|---|---|---|---|---|
| Insertion sort | $O(n)$ to $O(n^2)$ | $O(n)$ to $O(n^2)$ | $O(1)$ | Yes | Good |
| Selection sort | $\Theta(n^2)$ | $O(n)$ | $O(1)$ | No | Good |
| Heapsort | about $2n \log_2 n$ | about $n \log_2 n$ | $O(1)$ | No | Poor: ranks of parent and child differ by a factor of two |
| Merge sort | about $n \log_2 n$ | about $n \log_2 n$ to $2n\log_2 n$ | $O(n)$ | Yes | Good: sequential access |
| Quicksort | expected about $1.39\, n \log_2 n$ | expected about $0.69\, n \log_2 n$ | expected $O(\log n)$ | No | Very good: the pivot stays in a register |

Quicksort does not make the fewest comparisons, but its inner loop is extremely simple, it moves few elements, and its scans are sequential and very cache friendly, so it is usually the fastest in practice. Industrial-strength implementations make several improvements on this basis:

- **Introsort** (D. R. Musser, 1997): quicksort is the main algorithm, the recursion depth is recorded, and when it exceeds $2 \log_2 n$ the algorithm switches to **heapsort** ([4.3.12](/4.3.12)), guaranteeing $O(n \log n)$ in the worst case; recursion stops when the interval is short (a dozen or so elements), and insertion sort finishes the job at the end. C++'s `std::sort` uses this framework in all mainstream standard libraries, taking the median of the first, middle and last elements as pivot, and the median of nine for large sizes.
- Pattern-defeating quicksort (pdqsort, O. Peters, 2021): on top of introsort, it recognizes inputs that are already sorted or reversed, shuffles elements when a partition is clearly unbalanced to defeat adversarially constructed inputs, and handles many equal elements with the idea of three-way partitioning. Go's `sort` package has used it since 1.19; Rust's unstable sort first used it and since 1.81 uses ipnsort, an improvement on it.
- Python does not use quicksort: `list.sort` and `sorted` are required to be stable and often meet partially sorted input in practice, so they use Timsort (T. Peters, 2002), an adaptive merge sort, whose merge order has used the strategy of Powersort (J. I. Munro and S. Wild, 2018) since 3.11. Comparisons are very expensive in Python (each one calls the object's `__lt__`), and on partially sorted input Timsort needs far fewer than $n \log_2 n$ comparisons.

## 14.3. Selection

### 14.3.1. The Selection Problem and the Median

**Definition 14.3.1 (Selection Problem)** Given any set of comparable elements, find the element of rank $k$ ($0 \le k < n$) in nondecreasing order, that is, $s_k$ in the nondecreasing sequence $s_0 \le s_1 \le \cdots \le s_{n-1}$; this is called the $k$-selection problem, collectively the **selection problem**.

The **median** is a special case of selection: in this chapter, the median of a sorted sequence of length $n$ is the element of rank $\lfloor n/2 \rfloor$ (when $n$ is even, the larger of the two middle elements, and any element equal to it is also a median). The functions `LARGE(range, k)` and `MEDIAN(range)` of spreadsheets are these two problems. We shall see later that the median is also the hardest case of selection.

The brute-force method sorts first and then takes the element of rank $k$, which needs $O(n \log n)$ time. On the other hand, any selection algorithm needs at least $\Omega(n)$ time: being the $k$-th smallest is a property relative to the sequence as a whole, and it can by no means be determined before every element has been accessed at least once (an unaccessed element could have any value). The question is whether it can be done in $O(n)$ time.

### 14.3.2. Majority Elements

First consider a related problem.

**Definition 14.3.2 (Majority Element)** If more than half of the elements of an unsorted vector are equal to $m$, then $m$ is called its **majority element** (note that this is different from the "mode" in statistics, the value that occurs most often).

For example, in `5 3 9 3 1 3 3` the majority element is 3, while `5 3 9 3 1 3` has no majority element (3 makes up exactly half). The trivial algorithm sorts and then scans, in $O(n \log n)$ time. What if we require only $O(n)$ time and $O(1)$ additional space? A necessary condition is that a majority element, if it exists, must be the median (it occupies more than half of the positions after sorting, and so necessarily covers the middle position). So as soon as we can find the median in linear time, spending another $O(n)$ time to verify the number of its occurrences solves the problem. But before efficient median algorithms appeared, one could use a weaker but computationally cheaper necessary condition to select a unique candidate.

**Theorem 14.3.1** Suppose that in some prefix $P$ of even length of a **vector** $A$, an element $x$ occurs exactly $\lvert P \rvert / 2$ times. Then $A$ has a majority element only if the suffix $A \setminus P$ has a majority element $m$, and this $m$ is then the majority element of $A$.

**Proof** Suppose $A$ has a majority element $m$, let $c(y)$ be the number of occurrences of $y$, so $m$ occurs $c(m) > \lvert A \rvert / 2$ times in $A$. If $x = m$, then after removing $P$ the numerical gap between $m$ and the other elements is unchanged ($m$ and the other elements each make up half of $P$); if $x \ne m$, then $m$ occurs at most $\lvert P \rvert / 2$ times in $P$, and after removing $P$ the gap between $m$ and the other elements does not shrink. In both cases $m$ still exceeds half of the suffix. $\square$

We can therefore decrease and conquer: scan from left to right, maintaining a candidate `cand` and a counter `count`; when the counter is zero, take the current element as the new candidate; otherwise increment the counter on meeting the candidate and decrement it on meeting another element. Each time the counter returns to zero, a prefix satisfying the condition of the theorem has been cut off. The candidate at the end of the scan is the only possible majority element, and one more scan verifies it. This is the *majority vote algorithm* of Boyer and Moore (1981): two scans, $O(n)$ time and $O(1)$ space.

```cpp tab
#include <format>
#include <iostream>
#include <optional>
#include <random>
#include <vector>

// Boyer-Moore majority vote: the only possible majority, in one pass and O(1) space.
template <typename T>
T majority_candidate(const std::vector<T>& a) {
    T cand{};
    std::size_t count = 0;
    for (const T& x : a) {
        if (count == 0) { cand = x; count = 1; }   // a new prefix P starts here
        else if (x == cand) ++count;
        else --count;                              // x and one copy of cand cancel out
    }
    return cand;
}

template <typename T>
std::optional<T> majority(const std::vector<T>& a) {
    T cand = majority_candidate(a);
    std::size_t occ = 0;
    for (const T& x : a) occ += (x == cand);       // verify: O(n)
    if (2 * occ > a.size()) return cand;
    return std::nullopt;
}

int main() {
    for (const auto& a : {std::vector<int>{5, 3, 9, 3, 1, 3, 3}, std::vector<int>{5, 3, 9, 3, 1, 3}}) {
        auto m = majority(a);
        std::cout << (m ? std::format("majority {}\n", *m) : std::string("no majority\n"));
    }
    std::mt19937 rng(15);                          // differential test against counting
    for (int trial = 0; trial < 20000; ++trial) {
        std::vector<int> a(rng() % 12);
        for (int& x : a) x = static_cast<int>(rng() % 3);
        std::optional<int> ref;
        for (int v = 0; v < 3; ++v) {
            std::size_t c = 0;
            for (int x : a) c += (x == v);
            if (2 * c > a.size()) ref = v;
        }
        if (majority(a) != ref) { std::cout << "mismatch\n"; return 1; }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random


def majority_candidate(a: list):
    """Boyer-Moore majority vote: the only possible majority, O(1) space."""
    cand, count = None, 0
    for x in a:
        if count == 0:                             # a new prefix P starts here
            cand, count = x, 1
        elif x == cand:
            count += 1
        else:                                      # x and one copy of cand cancel out
            count -= 1
    return cand


def majority(a: list):
    """Return the element occurring more than len(a)/2 times, or None."""
    cand = majority_candidate(a)
    occ = sum(1 for x in a if x == cand)           # verify: O(n)
    return cand if 2 * occ > len(a) else None


print(majority([5, 3, 9, 3, 1, 3, 3]), majority([5, 3, 9, 3, 1, 3]))

rng = random.Random(15)                            # differential test against counting
for trial in range(20000):
    a = [rng.randrange(3) for _ in range(rng.randrange(12))]
    ref = next((v for v in range(3) if 2 * a.count(v) > len(a)), None)
    assert majority(a) == ref
print("random tests passed")
```

If the criterion for a majority element is changed from "more than half" to "at least half", this algorithm no longer applies; for example in `1 2` both elements make up exactly half. The generalization to finding all elements occurring more than $n/k$ times can maintain $k - 1$ candidates simultaneously (Misra and Gries, 1982), and is also the basis of frequent-item counting in data-stream algorithms.

### 14.3.3. The Median of Two Sorted Vectors

Given two **sorted vectors** $S_1$ and $S_2$ of lengths $n_1$ and $n_2$, we want to find the median of their union. The brute-force method merges the two and takes the middle element, in $O(n_1 + n_2)$ time, but this does not make full use of the sortedness of each vector.

First consider the case $n_1 = n_2 = n$, again by decrease and conquer. Compare the medians $m_1 = S_1[\lfloor n/2 \rfloor]$ and $m_2 = S_2[\lfloor (n-1)/2 \rfloor]$ of the two: if $m_1 = m_2$, then it is the median of $S_1$, of $S_2$ and of $S_1 \cup S_2$; if $m_1 < m_2$, then neither the elements of $S_1$ to the left of $m_1$ nor the elements of $S_2$ to the right of $m_2$ can be the median of the union, and the two sides deleted contain equally many elements, so after deleting these two parts (about half of each) the median is unchanged; the case $m_1 > m_2$ is symmetric. Each step halves the size, for a total of $O(\log n)$ time.

The general case $n_1 \ne n_2$ can be treated similarly, but the boundary cases are tedious. More concise is to compute directly the element of rank $k$ in the union: suppose among the first $k + 1$ elements of the union, $i$ come from $S_1$ and $j = k + 1 - i$ from $S_2$; the correct $i$ is the smallest one satisfying $S_1[i] \ge S_2[j - 1]$, and this condition is monotone in $i$, so binary search applies. Binary searching on the shorter vector takes $O(\log \min(n_1, n_2))$ time. We see that the equal-length case is in fact the hardest.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <vector>

// The k-th smallest (k = 0, 1, ...) element of the union of two sorted vectors,
// in O(log min(|a|, |b|)) time. Requires k < |a| + |b|.
int kth_of_two(const std::vector<int>& a, const std::vector<int>& b, std::size_t k) {
    if (a.size() > b.size()) return kth_of_two(b, a, k);  // binary search on the shorter one
    // Take i elements from a and j = k + 1 - i from b; find the smallest i with a[i] >= b[j-1].
    std::size_t lo = k + 1 > b.size() ? k + 1 - b.size() : 0, hi = std::min(k + 1, a.size());
    while (lo < hi) {
        std::size_t i = lo + (hi - lo) / 2, j = k + 1 - i;
        if (a[i] < b[j - 1]) lo = i + 1;          // too few from a
        else hi = i;
    }
    std::size_t i = lo, j = k + 1 - lo;           // a[0, i) and b[0, j) are the k+1 smallest
    if (i == 0) return b[j - 1];
    if (j == 0) return a[i - 1];
    return std::max(a[i - 1], b[j - 1]);
}

int median_of_two(const std::vector<int>& a, const std::vector<int>& b) {
    return kth_of_two(a, b, (a.size() + b.size()) / 2);   // the element of rank floor(n/2)
}

int main() {
    std::cout << median_of_two({1, 4, 7, 10}, {2, 3, 8, 9, 11}) << '\n';

    std::mt19937 rng(16);                         // differential test against merging
    for (int trial = 0; trial < 20000; ++trial) {
        std::vector<int> a(rng() % 10), b(rng() % 10);
        for (int& x : a) x = static_cast<int>(rng() % 20);
        for (int& x : b) x = static_cast<int>(rng() % 20);
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        std::vector<int> all(a);
        all.insert(all.end(), b.begin(), b.end());
        std::sort(all.begin(), all.end());
        for (std::size_t k = 0; k < all.size(); ++k)
            if (kth_of_two(a, b, k) != all[k]) { std::cout << "mismatch\n"; return 1; }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random


def kth_of_two(a: list, b: list, k: int):
    """The k-th smallest (k = 0, 1, ...) of the union of two sorted lists;
    O(log min(len(a), len(b))). Requires k < len(a) + len(b)."""
    if len(a) > len(b):                           # binary search on the shorter one
        a, b = b, a
    # Take i elements from a and k + 1 - i from b; find the smallest i with a[i] >= b[k-i].
    lo, hi = max(0, k + 1 - len(b)), min(k + 1, len(a))
    while lo < hi:
        i = (lo + hi) // 2
        if a[i] < b[k - i]:                       # too few from a
            lo = i + 1
        else:
            hi = i
    i, j = lo, k + 1 - lo                         # a[:i] and b[:j] are the k+1 smallest
    if i == 0:
        return b[j - 1]
    if j == 0:
        return a[i - 1]
    return max(a[i - 1], b[j - 1])


def median_of_two(a: list, b: list):
    return kth_of_two(a, b, (len(a) + len(b)) // 2)   # the element of rank n // 2


print(median_of_two([1, 4, 7, 10], [2, 3, 8, 9, 11]))

rng = random.Random(16)                           # differential test against merging
for trial in range(20000):
    a = sorted(rng.randrange(20) for _ in range(rng.randrange(10)))
    b = sorted(rng.randrange(20) for _ in range(rng.randrange(10)))
    merged = sorted(a + b)
    assert all(kth_of_two(a, b, k) == merged[k] for k in range(len(merged)))
print("random tests passed")
```

### 14.3.4. Heap-Based Selection

The **priority queue** ([4.3.12](/4.3.12)) suggests several different ideas:

| Method | Procedure | Time |
|---|---|---|
| Min-heap | Build all elements into a min-heap ($O(n)$) and perform `delMin` $k + 1$ times in a row | $O(n + k \log n)$ |
| Max-heap of size $k + 1$ | Build any $k + 1$ elements into a max-heap; for each remaining element, insert it and then delete the top; the final top is the answer | $O(k + (n - k)\log k)$ |
| Two heaps | Partition the input arbitrarily into parts of sizes $k$ and $n - k$, and build them into a max-heap $L$ and a min-heap $G$ respectively; as long as the top of $L$ is greater than the top of $G$, swap the two and percolate each down; finally the top of $G$ is the answer | $O(n + \min(k, n - k)\log n)$ |

When $k$ is very small or very close to $n$, these methods are all nearly linear; but for the median ($k \approx n/2$) they all need $\Theta(n \log n)$ time. C++'s `std::partial_sort` and Python's `heapq.nsmallest` are the second method, suited to needs such as "the top $k$" with $k \ll n$.

### 14.3.5. Quickselect

The partition of quicksort gives another idea: partition the whole vector once, and the pivot lands at rank $\mathit{mi}$. If $\mathit{mi} = k$, the pivot is the answer; if $\mathit{mi} < k$, the sought element must lie to the right of the pivot, and the prefix is pruned; if $\mathit{mi} > k$, the suffix is pruned. It suffices to continue on one side until we hit the answer (C. A. R. Hoare, 1961).

**Algorithm 14.3.1 (Quickselect)** Let $[\mathit{lo}, \mathit{hi}) = [0, n)$. Repeat: choose a random pivot in $[\mathit{lo}, \mathit{hi})$ and perform an LGU partition to obtain the rank $\mathit{mi}$ of the pivot; if $\mathit{mi} < k$ set $\mathit{lo} \gets \mathit{mi} + 1$, if $\mathit{mi} > k$ set $\mathit{hi} \gets \mathit{mi}$, otherwise return $A[\mathit{mi}]$.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

// Quickselect: the k-th smallest (k = 0, 1, ...) element; expected O(n) time.
// The vector is taken by value and rearranged.
int quick_select(std::vector<int> a, std::size_t k, std::mt19937& rng) {
    std::size_t lo = 0, hi = a.size();            // the answer stays in a[lo, hi)
    for (;;) {
        std::swap(a[lo], a[lo + rng() % (hi - lo)]);
        int pivot = a[lo];
        std::size_t mi = lo;                      // LGU partition
        for (std::size_t i = lo + 1; i < hi; ++i)
            if (a[i] < pivot) std::swap(a[++mi], a[i]);
        std::swap(a[lo], a[mi]);                  // a[lo, mi) < a[mi] <= a(mi, hi)
        if (mi < k) lo = mi + 1;                  // guessed too small: drop the prefix
        else if (k < mi) hi = mi;                 // guessed too large: drop the suffix
        else return a[mi];
    }
}

int main() {
    std::mt19937 rng(17);
    std::vector<int> a = {6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2};
    std::cout << std::format("median = {}\n", quick_select(a, a.size() / 2, rng));

    for (int trial = 0; trial < 3000; ++trial) {  // differential test against std::sort
        std::vector<int> v(1 + rng() % 60);
        for (int& x : v) x = static_cast<int>(rng() % 15);
        std::vector<int> ref = v;
        std::sort(ref.begin(), ref.end());
        std::size_t k = rng() % v.size();
        if (quick_select(v, k, rng) != ref[k]) { std::cout << "mismatch\n"; return 1; }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random


def quick_select(a: list, k: int, rng: random.Random):
    """The k-th smallest (k = 0, 1, ...) element; expected O(n). a is copied."""
    a = list(a)
    lo, hi = 0, len(a)                            # the answer stays in a[lo:hi]
    while True:
        r = rng.randrange(lo, hi)
        a[lo], a[r] = a[r], a[lo]
        pivot, mi = a[lo], lo                     # LGU partition
        for i in range(lo + 1, hi):
            if a[i] < pivot:
                mi += 1
                a[mi], a[i] = a[i], a[mi]
        a[lo], a[mi] = a[mi], a[lo]               # a[lo:mi] < a[mi] <= a[mi+1:hi]
        if mi < k:                                # guessed too small: drop the prefix
            lo = mi + 1
        elif k < mi:                              # guessed too large: drop the suffix
            hi = mi
        else:
            return a[mi]


rng = random.Random(17)
a = [6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2]
print("median =", quick_select(a, len(a) // 2, rng))

for trial in range(3000):                         # differential test against sorted()
    v = [rng.randrange(15) for _ in range(rng.randint(1, 60))]
    k = rng.randrange(len(v))
    assert quick_select(v, k, rng) == sorted(v)[k]
print("random tests passed")
```

As in quicksort, many equal elements make the LGU partition degenerate, and in that case one should switch to three-way partitioning: return immediately when $k$ falls in the segment equal to the pivot.

**Theorem 14.3.2** For quickselect with random pivots, the expected number of comparisons is at most $4n$ for every $k$.

**Proof** Let $T(n)$ be the expected number of comparisons for size $n$ and the worst $k$. One partition needs $n - 1$ comparisons, the rank of the pivot is equally likely to be $0, \dots, n-1$, and the remaining side has size at most $\max(i, n - 1 - i)$, so

$$
T(n) \le (n - 1) + \frac{1}{n} \sum_{i=0}^{n-1} T\bigl(\max(i, n - 1 - i)\bigr).
$$
We use induction on $n$, assuming $T(m) \le 4m$ for $m < n$. Since $\sum_{i=0}^{n-1} \max(i, n-1-i) \le \frac{3}{4}n^2$,

$$
T(n) \le (n - 1) + \frac{4}{n}\cdot\frac{3n^2}{4} < n + 3n = 4n. \qquad \square
$$

A more precise analysis shows that the median needs about $2(1 + \ln 2)n \approx 3.39n$ comparisons in expectation, and fewer the closer $k$ is to either end. But the worst case of quickselect is still $\Theta(n^2)$: the pivot is extreme on one side every time.

### 14.3.6. Linear-Time Selection

Can linear time be achieved even in the worst case? The key is to guarantee that each partition prunes a fixed fraction of the elements, that is, to find a "good enough" pivot. The approach of M. Blum, R. W. Floyd, V. Pratt, R. L. Rivest and R. E. Tarjan (1973) is to use the "median of medians" computed recursively as the pivot.

**Algorithm 14.3.2 (Linear-Time Selection)** Let $Q$ be a small constant (such as $Q = 5$). For $A$ and a rank $k$:

0. If $n = \lvert A \rvert$ does not exceed some constant, sort directly and return the element of rank $k$;
1. Otherwise divide $A$ evenly into $\lceil n/Q \rceil$ groups of $Q$ elements each (the last group may be smaller);
2. Sort each group (for example by insertion sort) and find the median of each group;
3. Call this algorithm recursively to find the median $M$ of these $\lceil n/Q \rceil$ medians;
4. Partition $A$ into $L = \{x < M\}$, $E = \{x = M\}$ and $G = \{x > M\}$, and count them;
5. If $k < \lvert L \rvert$, select recursively in $L$ the element of rank $k$; if $k < \lvert L \rvert + \lvert E \rvert$, return $M$; otherwise select recursively in $G$ the element of rank $k - \lvert L \rvert - \lvert E \rvert$.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

void insertion_sort(std::vector<int>& a, std::size_t lo, std::size_t hi) {
    for (std::size_t i = lo + 1; i < hi; ++i)
        for (std::size_t j = i; j > lo && a[j] < a[j - 1]; --j) std::swap(a[j], a[j - 1]);
}

// Linear-time selection (median of medians, groups of 5): the k-th smallest, k = 0, 1, ...
int linear_select(std::vector<int> a, std::size_t k) {
    constexpr std::size_t Q = 5;
    for (;;) {
        if (a.size() <= 2 * Q) {                  // base case: sort a few elements
            insertion_sort(a, 0, a.size());
            return a[k];
        }
        std::vector<int> medians;                 // 1-2. the median of each group of Q
        for (std::size_t g = 0; g < a.size(); g += Q) {
            std::size_t end = std::min(g + Q, a.size());
            insertion_sort(a, g, end);
            medians.push_back(a[g + (end - g) / 2]);
        }
        int m = linear_select(medians, medians.size() / 2);  // 3. median of the medians
        std::vector<int> less, greater;           // 4. split around m
        std::size_t equal = 0;
        for (int x : a) {
            if (x < m) less.push_back(x);
            else if (m < x) greater.push_back(x);
            else ++equal;
        }
        if (k < less.size()) a = std::move(less); // 5. continue on one side only
        else if (k < less.size() + equal) return m;
        else { k -= less.size() + equal; a = std::move(greater); }
    }
}

int main() {
    std::vector<int> a = {6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2};
    std::cout << std::format("median = {}\n", linear_select(a, a.size() / 2));

    std::mt19937 rng(18);                         // differential test against std::sort
    for (int trial = 0; trial < 3000; ++trial) {
        std::vector<int> v(1 + rng() % 300);
        int range = 1 + static_cast<int>(rng() % 100);
        for (int& x : v) x = static_cast<int>(rng() % range);
        std::vector<int> ref = v;
        std::sort(ref.begin(), ref.end());
        std::size_t k = rng() % v.size();
        if (linear_select(v, k) != ref[k]) { std::cout << "mismatch\n"; return 1; }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random


def insertion_sort(a: list, lo: int, hi: int) -> None:
    for i in range(lo + 1, hi):
        x, j = a[i], i
        while j > lo and x < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
        a[j] = x


def linear_select(a: list, k: int):
    """Median of medians with groups of 5: the k-th smallest in O(n) worst case."""
    Q = 5
    a = list(a)
    while True:
        if len(a) <= 2 * Q:                       # base case: sort a few elements
            insertion_sort(a, 0, len(a))
            return a[k]
        medians = []                              # 1-2. the median of each group of Q
        for g in range(0, len(a), Q):
            end = min(g + Q, len(a))
            insertion_sort(a, g, end)
            medians.append(a[g + (end - g) // 2])
        m = linear_select(medians, len(medians) // 2)   # 3. median of the medians
        less = [x for x in a if x < m]            # 4. split around m
        greater = [x for x in a if m < x]
        equal = len(a) - len(less) - len(greater)
        if k < len(less):                         # 5. continue on one side only
            a = less
        elif k < len(less) + equal:
            return m
        else:
            k -= len(less) + equal
            a = greater


a = [6, 3, 8, 1, 5, 9, 8, 4, 5, 7, 2]
print("median =", linear_select(a, len(a) // 2))

rng = random.Random(18)                           # differential test against sorted()
for trial in range(3000):
    keys = rng.randint(1, 100)
    v = [rng.randrange(keys) for _ in range(rng.randint(1, 300))]
    k = rng.randrange(len(v))
    assert linear_select(v, k) == sorted(v)[k]
print("random tests passed")
```

**Theorem 14.3.3** With $Q = 5$, linear-time selection takes only $O(n)$ time in the worst case.

**Proof** First estimate the size in step 5. Among the $\lceil n/5 \rceil$ group medians, at least half are no greater than $M$; excluding the group containing $M$ and the last group, which may be incomplete, each of these groups has at least 3 elements (the median and the two smaller ones) no greater than $M$. So there are at least

$$
3\left(\left\lceil \frac12 \left\lceil \frac{n}{5} \right\rceil \right\rceil - 2\right) \ge \frac{3n}{10} - 6
$$
elements no greater than $M$, and hence $\lvert G \rvert \le \frac{7n}{10} + 6$; likewise $\lvert L \rvert \le \frac{7n}{10} + 6$. The time of the steps is as follows: steps 1, 2 and 4 take $O(n)$ (sorting each group takes constant time), step 3 takes $T(\lceil n/5 \rceil)$, and step 5 at most $T(7n/10 + 6)$. So there is a constant $a$ with

$$
T(n) \le T\!\left(\left\lceil \frac{n}{5} \right\rceil\right) + T\!\left(\frac{7n}{10} + 6\right) + a n.
$$
Assume $T(m) \le cm$ for $m < n$; substituting gives $T(n) \le c(n/5 + 1) + c(7n/10 + 6) + an = cn - (cn/10 - 7c - an)$. When $n \ge 140$ and $c \ge 20a$, we have $cn/10 - 7c \ge cn/20 \ge an$, so $T(n) \le cn$; for $n < 140$ it suffices to take $c$ large enough. $\square$

The key of the proof is that the sum of the sizes of the two subproblems, $\frac{n}{5} + \frac{7n}{10} = \frac{9n}{10}$, is less than $n$, so with each level deeper in the recursion tree the total work decreases geometrically. With group size $Q = 3$ this sum is $\frac13 + \frac23 = 1$, which cannot guarantee linearity; $7$ or larger also works, but sorting each group costs more.

The constant factor of linear-time selection is large, and it is rarely used directly in practice; its significance is in proving that selection can be solved in linear time, and in providing a "safety net" for quickselect. More practical methods include introselect (Musser), which uses quickselect as the main algorithm and switches to the median of medians when the recursion gets too deep, and which C++'s `std::nth_element` uses in this kind of implementation, the standard requiring only linear time on average; and the sampling algorithm of Floyd and Rivest (1975), which first selects from a small sample two elements bracketing the target and needs only $n + \min(k, n - k) + o(n)$ comparisons in expectation. For the median, the best known algorithm needs about $2.95n$ comparisons (Dor and Zwick), while any algorithm needs at least $(2 + \varepsilon)n$; the exact constant is still unknown.

## 14.4. Shellsort

### 14.4.1. The Framework

**Insertion sort** is fast on nearly sorted input, but it moves an element only one position at a time, which is very inefficient for elements far from their correct positions. The idea of D. L. Shell (1959) is to let elements jump with a large step first, putting them roughly in place, and then gradually reduce the step.

**Definition 14.4.1 (Shellsort)** Take a gap sequence decreasing to 1, $h_t > h_{t-1} > \cdots > h_1 = 1$. For each gap $h$ in turn, regard the sequence $S[0, n)$ as a matrix with $h$ columns ($S[i]$ lies in column $i \bmod h$), and perform insertion sort on each column separately. This sorting method is called **Shellsort**, and the sequence $\mathcal{H} = \{h_1 = 1, h_2, \dots\}$ of gaps arranged from small to large is called its **gap sequence** (increment sequence).

The processing of one gap $h$ is called $h$-sorting, and its result is an $h$-ordered sequence: $S[i] \le S[i + h]$ for all $0 \le i < n - h$. Refining step by step from coarse to fine: first rearrange into a very wide matrix and sort column by column, then rearrange into a narrower matrix and again sort column by column, until the matrix becomes a single column. The final 1-sort is a complete insertion sort, so Shellsort is certainly correct: 1-ordered means sorted.

The matrix is only a way of looking at things, and no two-dimensional vector need actually be used. In each step, if the current matrix has width $h$, then column $j$ consists of the elements of ranks $j, j + h, j + 2h, \dots$, which can be accessed directly on the one-dimensional vector with stride $h$. An implementation also need not process column by column: scan the elements in increasing order of rank and insert each into the prefix of its column, with the same effect.

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <vector>

// Gap sequences, in increasing order, with all gaps < n.
std::vector<std::size_t> gaps_shell(std::size_t n) {          // ..., n/4, n/2
    std::vector<std::size_t> g;
    for (std::size_t h = n / 2; h > 0; h /= 2) g.insert(g.begin(), h);
    return g;
}
std::vector<std::size_t> gaps_ps(std::size_t n) {             // 2^k - 1: 1, 3, 7, 15, ...
    std::vector<std::size_t> g;
    for (std::size_t h = 1; h < n; h = 2 * h + 1) g.push_back(h);
    return g;
}
std::vector<std::size_t> gaps_pratt(std::size_t n) {          // 2^p 3^q: 1, 2, 3, 4, 6, 8, 9, ...
    std::vector<std::size_t> g = {1};                          // generated in increasing order
    for (std::size_t i2 = 0, i3 = 0;;) {
        std::size_t h = std::min(2 * g[i2], 3 * g[i3]);
        if (h >= n) break;
        g.push_back(h);
        if (h == 2 * g[i2]) ++i2;
        if (h == 3 * g[i3]) ++i3;
    }
    return g;
}
std::vector<std::size_t> gaps_sedgewick(std::size_t n) {      // 1, 5, 19, 41, 109, 209, ...
    std::vector<std::size_t> g;
    for (std::size_t i = 0;; ++i) {
        std::size_t p = std::size_t{1} << i;                    // 2^i
        std::size_t a = 9 * p * p - 9 * p + 1;                  // 9*4^i - 9*2^i + 1
        std::size_t b = p * p * 4 * 4 - 3 * p * 4 + 1;          // 4^(i+2) - 3*2^(i+2) + 1
        if (a >= n) break;
        g.push_back(a);
        if (b < n) g.push_back(b);
    }
    return g;
}

// Shellsort: h-sort for each gap h from the largest to 1 (insertion sort on each column).
void shell_sort(std::vector<int>& a, const std::vector<std::size_t>& gaps) {
    for (auto it = gaps.rbegin(); it != gaps.rend(); ++it) {
        const std::size_t h = *it;
        for (std::size_t j = h; j < a.size(); ++j) {           // insert a[j] into its column
            int x = a[j];
            std::size_t i = j;
            for (; i >= h && x < a[i - h]; i -= h) a[i] = a[i - h];
            a[i] = x;
        }
    }
}

int main() {
    for (std::size_t h : gaps_sedgewick(1000)) std::cout << std::format("{} ", h);
    std::cout << '\n';
    std::mt19937 rng(19);                                       // differential test against std::sort
    for (auto gaps : {gaps_shell, gaps_ps, gaps_pratt, gaps_sedgewick}) {
        for (int trial = 0; trial < 1000; ++trial) {
            std::vector<int> v(rng() % 300);
            for (int& x : v) x = static_cast<int>(rng() % 100);
            std::vector<int> ref = v;
            std::sort(ref.begin(), ref.end());
            shell_sort(v, gaps(v.size()));
            if (v != ref) { std::cout << "mismatch\n"; return 1; }
        }
    }
    std::cout << "random tests passed\n";
}
```

```python tab
import random


def gaps_shell(n: int) -> list[int]:              # ..., n//4, n//2
    g, h = [], n // 2
    while h > 0:
        g.insert(0, h)
        h //= 2
    return g


def gaps_ps(n: int) -> list[int]:                 # 2^k - 1: 1, 3, 7, 15, ...
    g, h = [], 1
    while h < n:
        g.append(h)
        h = 2 * h + 1
    return g


def gaps_pratt(n: int) -> list[int]:              # 2^p 3^q: 1, 2, 3, 4, 6, 8, 9, ...
    g, i2, i3 = [1], 0, 0                         # generated in increasing order
    while (h := min(2 * g[i2], 3 * g[i3])) < n:
        g.append(h)
        i2 += h == 2 * g[i2]
        i3 += h == 3 * g[i3]
    return g


def gaps_sedgewick(n: int) -> list[int]:          # 1, 5, 19, 41, 109, 209, ...
    g, i = [], 0
    while (a := 9 * 4**i - 9 * 2**i + 1) < n:
        g.append(a)
        if (b := 4 ** (i + 2) - 3 * 2 ** (i + 2) + 1) < n:
            g.append(b)
        i += 1
    return g


def shell_sort(a: list, gaps: list[int]) -> None:
    """h-sort for each gap h from the largest to 1 (insertion sort on each column)."""
    for h in reversed(gaps):
        for j in range(h, len(a)):                # insert a[j] into its column
            x, i = a[j], j
            while i >= h and x < a[i - h]:
                a[i] = a[i - h]
                i -= h
            a[i] = x


print(*gaps_sedgewick(1000))
rng = random.Random(19)                           # differential test against sorted()
for gaps in (gaps_shell, gaps_ps, gaps_pratt, gaps_sedgewick):
    for trial in range(1000):
        v = [rng.randrange(100) for _ in range(rng.randrange(300))]
        ref = sorted(v)
        shell_sort(v, gaps(len(v)))
        assert v == ref
print("random tests passed")
```

The efficiency of Shellsort depends entirely on the gap sequence. The cost of the final insertion sort is $O(n + I)$, where $I$ is the total number of **inversions** (Theorem 3.8.1): the earlier steps exist to reduce the inversions substantially at a low cost.

### 14.4.2. The Shell Sequence

The gap sequence originally suggested by Shell is $n/2, n/4, \dots, 2, 1$, that is, $\mathcal{H}_{\mathrm{shell}} = \{1, 2, 4, 8, \dots, 2^k, \dots\}$ (when $n$ is a power of 2). In the worst case it needs $\Theta(n^2)$ time.

**Example 14.4.1** Let $n = 2^N$, place the smallest $n/2$ elements in ascending order at the odd positions and the largest $n/2$ elements in ascending order at the even positions. Except for the final 1, all gaps are even, and $h$-sorting never compares elements at positions of different parity, so the sequence is completely unchanged before the last step: the even positions all hold large elements and the odd positions all hold small elements. The $i$-th smallest element is at rank $2i - 1$ and has to move forward about $i$ positions, and the final 1-sort takes $\sum_{i} \Theta(i) = \Theta(n^2)$ time in total.

The root of the problem is that the terms of the Shell sequence are not relatively prime, not even adjacent ones: there is no "communication" among the steps with even gaps. A good gap sequence should make adjacent gaps **coprime**.

### 14.4.3. Order Preservation and Linear Combinations

To analyze general gap sequences, two facts are needed. The first is that later steps do not destroy the results of earlier steps.

**Lemma 14.4.1** Let $x_1, \dots, x_{m+r}$ and $y_1, \dots, y_{n+r}$ be two sequences satisfying $y_{n+j} \ge x_j$ ($1 \le j \le r$). After the two sequences are each sorted, we still have $y_{n+j} \ge x_j$ ($1 \le j \le r$).

**Proof** After sorting, $y_{n+j}$ is the $(n + j)$-th smallest element of $y$; it is no smaller than at least $n + j$ elements of $y$, of which at least $j$ lie among $y_{n+1}, \dots, y_{n+r}$ of the original sequence (the other positions number only $n$). Each of these $j$ elements is no smaller than a distinct $x$, so after sorting $y_{n+j}$ is no smaller than at least $j$ of the $x$, and hence no smaller than the sorted $x_j$. $\square$

**Theorem 14.4.1** A $g$-ordered sequence remains $g$-ordered after $h$-sorting (Knuth, TAOCP Vol. 3).

**Proof** $h$-sorting sorts each column separately. Consider column $c$ and column $c'$ with $c' \equiv c + g \pmod h$. The element of rank $p$ in column $c$ corresponds one to one to the element of rank $p + g$ in column $c'$, and the position of the latter in column $c'$ is shifted back relative to the position of the former in column $c$ by a fixed amount $\lfloor (c + g)/h \rfloor$. $g$-orderedness says exactly that every such pair satisfies $S[p] \le S[p+g]$, which is exactly the condition of Lemma 14.4.1. So after the two columns are sorted separately these inequalities still hold, and the sequence is still $g$-ordered. $\square$

A sequence that is both $g$-ordered and $h$-ordered is called $(g, h)$-ordered. By transitivity it is $(ag + bh)$-ordered for all $a, b \in \mathbb{N}$: starting from $S[i]$, take $a$ steps of $g$ and then $b$ steps of $h$, and every step along the way is nondecreasing. The second fact comes from number theory: if $g, h$ are coprime, then the numbers of the form $ag + bh$ ($a, b \in \mathbb{N}$) include all integers not less than $(g-1)(h-1)$, and the largest integer that cannot be represented is $gh - g - h$ (Sylvester, 1884). For example, with stamps of only 4 cents and 13 cents, every postage of at least 36 cents can be made up, while 35 cents cannot.

**Theorem 14.4.2** Let $g, h$ be coprime and let $S[0, n)$ be $(g, h)$-ordered. Then $S[i] \le S[j]$ whenever $j - i \ge (g-1)(h-1)$; hence each element has at most $(g-1)(h-1)$ larger elements to its left, and the total number of inversions is at most $n(g-1)(h-1)$.

**Proof** $j - i \ge (g-1)(h-1)$ can be written as $ag + bh$, and $(g, h)$-orderedness implies $(ag + bh)$-orderedness. $\square$

From this we can estimate the cost of $d$-sorting: if $g, h$ are coprime and both $O(d)$, then in $d$-sorting a $(g, h)$-ordered sequence, each element in each column has at most $(g-1)(h-1)/d = O(d)$ larger elements to its left, and insertion moves it at most that many times, so $d$-sorting takes only $O(nd)$ time.

### 14.4.4. The PS Sequence

**Example 14.4.2** The sequence of Papernov and Stasevich (1965) is $\mathcal{H}_{\mathrm{ps}} = \{2^k - 1\} = \{1, 3, 7, 15, 31, \dots\}$ (also called the Hibbard sequence). Non-adjacent terms are not necessarily coprime (such as 3 and 15), but adjacent terms necessarily are: $\gcd(2^{k+1} - 1, 2^k - 1) = \gcd(2(2^k - 1) + 1, 2^k - 1) = 1$.

**Theorem 14.4.3** Shellsort with the PS sequence takes $O(n^{3/2})$ time in the worst case.

**Proof** Let $h_t$ be the gap closest to $\sqrt{n}$, so $h_t = \Theta(\sqrt{n})$. We estimate in two parts.

1. The steps with gap $h_k \ge h_t$: each column has at most $\lceil n/h_k \rceil$ elements, and insertion sorting the $h_k$ columns separately takes $O(h_k \cdot (n/h_k)^2) = O(n^2/h_k)$ time. The gaps grow by a factor of 2, so these terms form a geometric series whose sum is determined by the smallest term: $O(n^2/h_t) = O(n^{3/2})$.
2. The steps with gap $h_k < h_t$: $h_{k+1}$-sorting and $h_{k+2}$-sorting have been done before, so by Theorem 14.4.1 the sequence is $(h_{k+1}, h_{k+2})$-ordered. The two are coprime and both $O(h_k)$, so $h_k$-sorting takes only $O(n h_k)$ time. These terms also form a geometric series whose sum is determined by the largest term: $O(n h_t) = O(n^{3/2})$.

The total is $O(n^{3/2})$. $\square$

This upper bound is tight: there are inputs for which the PS sequence needs $\Theta(n^{3/2})$ time. Simulations of the average case suggest about $O(n^{5/4})$, which has not been proved to this day.

### 14.4.5. The Pratt Sequence

**Example 14.4.3** The sequence of V. Pratt (1971) consists of all numbers of the form $2^p 3^q$: $\mathcal{H}_{\mathrm{pratt}} = \{1, 2, 3, 4, 6, 8, 9, 12, 16, 18, \dots\}$. Its adjacent terms are not necessarily coprime, and there are $\Theta(\log^2 n)$ terms not exceeding $n$ ($p$ and $q$ each take $O(\log n)$ values).

**Theorem 14.4.4** Shellsort with the Pratt sequence takes $O(n \log^2 n)$ time.

**Proof** First consider a $(2, 3)$-ordered sequence: $(2-1)(3-1) = 2$, and by Theorem 14.4.2, $S[i] \le S[j]$ when $j - i \ge 2$, so for each element at most the one immediately to its left can be larger, and insertion sort takes only $O(n)$ time. Now consider any gap $h$: $2h$ and $3h$ (if not exceeding $n$) are both in the sequence and have been processed before, so by Theorem 14.4.1 the sequence is $(2h, 3h)$-ordered at this point. Divide it into $h$ columns; each column is $(2, 3)$-ordered, so $h$-sorting takes $O(n)$ in total. There are $\Theta(\log^2 n)$ steps, for a total of $O(n \log^2 n)$. $\square$

The Pratt sequence gives the best known worst-case upper bound for Shellsort, but it has too many steps: even for already sorted input it makes $\Theta(\log^2 n)$ scans, and in practice it is slower.

### 14.4.6. The Sedgewick Sequence and Practice

R. Sedgewick (1986) combined the ideas of the PS sequence and the Pratt sequence and proposed

$$
\mathcal{H}_{\mathrm{sedgewick}} = \{9 \cdot 4^k - 9 \cdot 2^k + 1\} \cup \{4^{k+2} - 3 \cdot 2^{k+2} + 1\} = \{1, 5, 19, 41, 109, 209, 505, 929, \dots\},
$$
whose worst case is $O(n^{4/3})$ and whose average case is conjectured to be $O(n^{7/6})$, and which is among the best in practice. The sequence $1, 4, 10, 23, 57, 132, 301, 701$ obtained experimentally by M. Ciura (2001) (extended beyond that by a factor of about 2.25) makes fewer comparisons in experiments, but has no theoretical analysis.

| Gap sequence | Example | Worst case | Remarks |
|---|---|---|---|
| Shell (1959) | $1, 2, 4, 8, \dots$ | $\Theta(n^2)$ | Adjacent terms not coprime |
| Papernov–Stasevich (1965) | $1, 3, 7, 15, \dots$ | $\Theta(n^{3/2})$ | Adjacent terms coprime |
| Pratt (1971) | $1, 2, 3, 4, 6, 8, 9, \dots$ | $\Theta(n \log^2 n)$ | $\Theta(\log^2 n)$ steps |
| Sedgewick (1986) | $1, 5, 19, 41, 109, \dots$ | $O(n^{4/3})$ | Good in practice |
| Ciura (2001) | $1, 4, 10, 23, 57, \dots$ | Unknown | Found experimentally |

![Comparisons per element of four gap sequences on random permutations](./plots/shellsort-gaps.py)

Is there a gap sequence with worst case $O(n \log n)$? The answer is no: Plaxton, Poonen and Suel (1992) proved that Shellsort with any gap sequence needs at least $\Omega\bigl(n (\log n / \log\log n)^2\bigr)$ time in the worst case. Whether there is a gap sequence with average case $O(n \log n)$ is still unsolved. Shellsort has short code, is in place and needs no recursion, and is still used in settings such as embedded systems; for example, embedded C libraries such as uClibc have used it to implement `qsort`.

## 14.5. Sorting and Selection in Standard Libraries

The sorting and selection algorithms of the C++ standard library ([4.2.10](/4.2.10)) all operate on ranges of random-access iterators and accept a comparator:

| Function | Purpose | Common implementation | Complexity |
|---|---|---|---|
| `std::sort` | sorting, not stable | introsort | $O(n \log n)$ |
| `std::stable_sort` | stable sorting | merge sort | $O(n \log n)$; $O(n \log^2 n)$ if no buffer can be allocated |
| `std::partial_sort` | sort only the smallest $k$ | heap of size $k$ | $O(n \log k)$ |
| `std::nth_element` | put the element of rank $k$ at position $k$, with elements no greater on its left and no smaller on its right | introselect | average $O(n)$ |
| `std::make_heap` etc. | heap operations | binary heap | see [4.3.12](/4.3.12) |

Since C++20 they all have `std::ranges` versions (such as `std::ranges::sort(v)`), which can operate directly on a whole container and accept projections (sorting by a member only).

Python provides only sorting: `list.sort()` sorts in place and `sorted()` returns a new list, both stable Timsort (using the merge strategy of Powersort since 3.11), with the sort criterion specified through the `key` parameter. Python has no built-in linear-time selection: `statistics.median` sorts first and then takes the middle element, in $O(n \log n)$; to take the $k$ smallest, use `heapq.nsmallest`, in $O(n \log k)$. For selection on large numerical data, NumPy's `partition` can be used ([4.4](/4.4)).

## Summary

- Quicksort = turning elements into pivots one by one. LUG is eager to expand and degrades on equal elements; DUP distributes equal elements alternately to both sides; LGU scans in one direction and is the simplest; three-way partitioning puts equal elements in place in one pass.
- Recursing only on the shorter side gives $O(\log n)$ space; a random pivot makes the recursion depth $O(\log n)$ with very high probability, and the expected number of comparisons is $2(n+1)H_n - 4n \approx 1.386\, n \log_2 n$ (backward analysis: the probability that $s_i$ and $s_j$ are compared is $2/(j - i + 1)$).
- Industrial-strength sorting: C++'s **introsort** (quicksort + **heapsort** + **insertion sort**) and pdqsort, Python's Timsort / Powersort.
- Selection: lower bound $\Omega(n)$; the majority vote algorithm takes $O(n)$ time and $O(1)$ space; the $k$-th smallest of two **sorted vectors** takes $O(\log \min(n_1, n_2))$; quickselect takes expected $O(n)$; the median of medians guarantees $O(n)$ in the worst case, the key being $\frac15 + \frac{7}{10} < 1$.
- The efficiency of Shellsort depends on the gap sequence: $h$-sorting preserves $g$-orderedness; a $(g, h)$-ordered sequence with $g, h$ coprime has only $O(n gh)$ **inversions**. The Shell sequence gives $\Theta(n^2)$, the PS sequence $\Theta(n^{3/2})$, the Pratt sequence $\Theta(n \log^2 n)$, the Sedgewick sequence $O(n^{4/3})$; no gap sequence has worst case $O(n \log n)$.
