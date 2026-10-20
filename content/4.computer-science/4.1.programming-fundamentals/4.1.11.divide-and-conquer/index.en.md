---
title: Divide and Conquer
description: The three steps of divide and conquer and its recurrence; merge sort and the merging procedure; the idea of quicksort, several partitioning methods, and the choice of pivot; subsystem decomposition in the frog-crossing problem; the recursive solution and step count of the nine linked rings puzzle.
source_hash: c414ee0fc7bb
---

The **decrease and conquer** of the previous chapter leaves only one subproblem each time. The divide and conquer of this chapter goes a step further: it splits the problem into several mutually independent subproblems, solves each recursively, and then merges the solutions of the subproblems into a solution of the original problem. Divide and conquer is one of the most fruitful ideas in algorithm design; sorting, the fast Fourier transform, large-integer multiplication, the closest pair of points, and many other efficient algorithms are divide-and-conquer algorithms. This chapter takes the two most important sorting algorithms, merge sort and quicksort, as its main thread: they split the problem in half in different ways, one "easy to split, laborious to merge" and the other "laborious to split, easy to merge". We then use two puzzles (frog crossing and the nine linked rings) to practice finding decomposable structure in a seemingly complicated process. The complexity analysis of divide-and-conquer algorithms (the master theorem) and a systematic comparison of sorting algorithms are discussed in [4.3.1](/4.3.1), [4.3.2](/4.3.2), and [4.3.14](/4.3.14).

## 11.1. The Idea of Divide and Conquer

**Definition 11.1.1 (Divide and Conquer)** The strategy of decomposing a problem of size $n$ into several (usually two) smaller, mutually independent subproblems of the same kind as the original, solving these recursively, and merging their solutions into a solution of the original problem is called **divide and conquer**.

Every divide-and-conquer algorithm consists of three steps:

1. Divide: split the problem into several subproblems.
2. Conquer: solve the subproblems recursively, directly when they are small enough.
3. Combine: assemble the solutions of the subproblems into a solution of the original problem.

If a problem of size $n$ is split into $a$ subproblems of size $n/b$, and dividing and combining together take $f(n)$ work, then the total work satisfies the recurrence

$$
T(n) = a\,T(n/b) + f(n).
$$

In the merge sort below, $a = b = 2$ and $f(n)$ is proportional to $n$; solving gives $T(n)$ proportional to $n \log n$. The general solution of such recurrences (the master theorem) is in [4.3.1](/4.3.1).

Divide and conquer differs from decrease and conquer in the number of subproblems (one or several), and from the dynamic programming of [4.1.13](/4.1.13) in whether the subproblems overlap: divide and conquer requires the subproblems to be mutually independent; if the subproblems overlap heavily (such as the Fibonacci sequence in the previous chapter), direct divide and conquer repeats computation, and we should switch to **memoization** or dynamic programming.

## 11.2. Merge Sort

### 11.2.1. The Algorithm

**Algorithm 11.2.1 (Merge Sort)** To sort the array $A[\mathit{lo}..\mathit{hi})$:

1. If the interval has fewer than 2 elements, it is already sorted; return.
2. Take the midpoint $\mathit{mid} = \lfloor(\mathit{lo} + \mathit{hi})/2\rfloor$ and recursively sort $A[\mathit{lo}..\mathit{mid})$ and $A[\mathit{mid}..\mathit{hi})$ separately.
3. Merge the two sorted halves into one sorted segment.

Here we use the half-open interval $[\mathit{lo}, \mathit{hi})$ to denote a subarray: its length is exactly $\mathit{hi} - \mathit{lo}$, and the two halves $[\mathit{lo}, \mathit{mid})$ and $[\mathit{mid}, \mathit{hi})$ meet end to end with no $\pm 1$ corrections; this is also the convention of C++ iterators and Python slices.

Merging is the core of merge sort. The smallest element of two sorted sequences must be the first element of one of them, so we just compare the two "current first elements", move the smaller to the output, and repeat until one sequence is exhausted, then append the remainder of the other. Merging two sequences of total length $n$ takes at most $n - 1$ comparisons. Merging needs a temporary array; allocating it once before the recursion and sharing it among all levels of calls avoids repeatedly allocating and releasing memory in every call.

```cpp tab
#include <iostream>
#include <vector>

// Sort a[lo, hi) using the buffer tmp (same size as a).
void merge_sort(std::vector<int>& a, std::vector<int>& tmp, int lo, int hi) {
    if (hi - lo < 2) return;                      // 0 or 1 element: sorted
    int mid = lo + (hi - lo) / 2;
    merge_sort(a, tmp, lo, mid);
    merge_sort(a, tmp, mid, hi);
    int i = lo, j = mid, k = lo;                  // merge a[lo, mid) and a[mid, hi)
    while (i < mid && j < hi)
        tmp[k++] = (a[j] < a[i]) ? a[j++] : a[i++];  // ties take the left: stable
    while (i < mid) tmp[k++] = a[i++];
    while (j < hi) tmp[k++] = a[j++];
    for (k = lo; k < hi; ++k) a[k] = tmp[k];
}

void merge_sort(std::vector<int>& a) {
    std::vector<int> tmp(a.size());               // allocated once
    merge_sort(a, tmp, 0, static_cast<int>(a.size()));
}

int main() {
    std::vector<int> a = {38, 27, 43, 3, 9, 82, 10};
    merge_sort(a);
    for (int x : a) std::cout << x << ' ';
    std::cout << '\n';
}
```

```python tab
def merge_sort(a: list[int]) -> list[int]:
    """Return a new sorted list (the input is not modified)."""
    if len(a) < 2:                                # 0 or 1 element: sorted
        return a[:]
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0                          # merge the two sorted halves
    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            out.append(right[j]); j += 1
        else:                                     # ties take the left: stable
            out.append(left[i]); i += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
```

The midpoint is written `lo + (hi - lo) / 2` rather than `(lo + hi) / 2` to avoid **integer overflow** when two large indices are added. The Python version obtains the two halves by slicing and returns a new list, which is closer to the mathematical description of the algorithm at the cost of copying data at every level; the C++ version sorts in place on the original array and uses only one shared buffer.

### 11.2.2. Properties

The recursion tree has about $\log_2 n$ levels, and the merges at each level together process $n$ elements, so the number of comparisons of merge sort is proportional to $n \log n$, independent of the initial order of the input, even in the worst case. It needs extra space of the same size as the input. Merge sort is stable: equal elements keep their original relative order after sorting (during merging, equal elements are taken from the left first). Stability is useful when sorting by several keys, for example sorting by name first and then stably by score, so that people with equal scores remain ordered by name.

Python's built-in `list.sort` and `sorted` are an improved merge sort (Timsort; since 3.11 it uses the merge policy of Powersort); it detects segments of the input that are already sorted, so it is especially fast on partially ordered data, and it is stable. C++'s `std::stable_sort` is also a stable merge-type sort.

## 11.3. Quicksort

### 11.3.1. The Idea

Merge sort mechanically cuts the array in two; there is no ordering relation between the two sorted halves, so merging takes effort. Quicksort does the opposite: it first spends effort arranging the array so that "everything on the left is no larger than some value and everything on the right is no smaller", so that once both sides are sorted the whole array is automatically sorted, with no merging needed.

**Algorithm 11.3.1 (Quicksort)** To sort the array $A[\mathit{lo}..\mathit{hi}]$:

1. If the interval has fewer than 2 elements, return.
2. Partition: choose an element as the *pivot* and rearrange the interval so that all elements to the left of the pivot are no larger than it and all elements to the right are no smaller; the pivot lands at its final position $p$.
3. Recursively sort $A[\mathit{lo}..p-1]$ and $A[p+1..\mathit{hi}]$ separately.

Correctness is easily explained by induction: after partitioning, the pivot is already at its final position, and after the left and right segments are sorted, the elements of the left segment are no larger than the pivot and those of the right segment no smaller, so the whole is sorted. The key and the difficulty of the algorithm lie in how to partition efficiently and in place.

### 11.3.2. Partitioning Methods

The most direct method uses extra space: scan once, put the elements smaller than, equal to, and greater than the pivot into three lists, and concatenate them. In Python this is almost the definition of the algorithm:

```python
def quick_sort(a: list[int]) -> list[int]:
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2]
    return (quick_sort([x for x in a if x < pivot])
            + [x for x in a if x == pivot]
            + quick_sort([x for x in a if x > pivot]))
```

It expresses the idea clearly but copies data at every level. A practical quicksort partitions in place, without an extra array. The common method is "two-way scanning": take the first element as the pivot and set it aside, leaving a "hole"; scan from right to left for an element smaller than the pivot and put it into the hole on the left, so that the hole moves to the right; then scan from left to right for an element larger than the pivot and put it into the hole on the right; the two directions alternate until the left and right pointers meet, and the pivot is put back at that position. Throughout the process, the elements to the left of the left pointer are no larger than the pivot, and those to the right of the right pointer are no smaller.

```cpp tab
#include <iostream>
#include <random>
#include <utility>
#include <vector>

std::mt19937 rng{2024};

// Partition a[lo..hi] around a random pivot; return the pivot's final index.
int partition(std::vector<int>& a, int lo, int hi) {
    std::uniform_int_distribution<int> pick(lo, hi);
    std::swap(a[lo], a[pick(rng)]);     // random pivot, moved to the front
    int pivot = a[lo];                  // a[lo] is now a "hole"
    while (lo < hi) {
        while (lo < hi && a[hi] >= pivot) --hi;
        a[lo] = a[hi];                  // a smaller element fills the left hole
        while (lo < hi && a[lo] <= pivot) ++lo;
        a[hi] = a[lo];                  // a larger element fills the right hole
    }
    a[lo] = pivot;                      // lo == hi: the pivot's final position
    return lo;
}

void quick_sort(std::vector<int>& a, int lo, int hi) {
    if (hi - lo < 1) return;            // fewer than 2 elements
    int p = partition(a, lo, hi);
    quick_sort(a, lo, p - 1);
    quick_sort(a, p + 1, hi);
}

int main() {
    std::vector<int> a = {6, 1, 2, 7, 9, 3, 4, 5, 10, 8};
    quick_sort(a, 0, static_cast<int>(a.size()) - 1);
    for (int x : a) std::cout << x << ' ';
    std::cout << '\n';
}
```

```python tab
import random

def partition(a: list[int], lo: int, hi: int) -> int:
    """Partition a[lo..hi] around a random pivot; return its final index."""
    k = random.randint(lo, hi)
    a[lo], a[k] = a[k], a[lo]           # random pivot, moved to the front
    pivot = a[lo]                       # a[lo] is now a "hole"
    while lo < hi:
        while lo < hi and a[hi] >= pivot:
            hi -= 1
        a[lo] = a[hi]                   # a smaller element fills the left hole
        while lo < hi and a[lo] <= pivot:
            lo += 1
        a[hi] = a[lo]                   # a larger element fills the right hole
    a[lo] = pivot                       # lo == hi: the pivot's final position
    return lo

def quick_sort(a: list[int], lo: int = 0, hi: int | None = None) -> None:
    if hi is None:
        hi = len(a) - 1
    if hi - lo < 1:                     # fewer than 2 elements
        return
    p = partition(a, lo, hi)
    quick_sort(a, lo, p - 1)
    quick_sort(a, p + 1, hi)

a = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
quick_sort(a)
print(a)
```

Another common formulation (Lomuto partitioning) uses a single left-to-right scanning pointer and maintains the invariant that "elements smaller than the pivot are all in front"; the code is shorter but makes more swaps. The method originally proposed by C. A. R. Hoare scans from both ends toward each other and swaps pairs of out-of-order elements. The details of the various partitioning methods, their comparison, and the handling of many repeated elements (three-way partitioning) are in [4.3.14](/4.3.14).

### 11.3.3. Choice of Pivot and Performance

The efficiency of quicksort depends on whether the partitions are balanced. If the pivot is always close to the median, the recursion tree has about $\log_2 n$ levels, the partitions at each level together scan $n$ elements, and the total work is proportional to $n \log n$; if the pivot is always the smallest or largest element, each step removes only one element, the work is proportional to $n^2$, and the recursion depth reaches $n$. When the first element is always taken as the pivot, an already sorted input is exactly the worst case, and sorted or nearly sorted data are common in practice.

The remedy is to choose the pivot at random (as the code above does), or to take the median of the first, middle, and last elements. With a random pivot, for any input the expected number of comparisons is about $1.39\, n \log_2 n$, and the worst case occurs with very small probability. In practice quicksort is usually faster than merge sort: it works in place, its memory access pattern is cache-friendly, and its inner loop is extremely simple. Its drawbacks are that it is unstable and its worst case is poor. In mainstream implementations, C++'s `std::sort` uses *introsort*: quicksort as the main algorithm, switching to heapsort when the recursion becomes too deep so that even the worst case is of order $n \log n$, and to insertion sort for small intervals.

| | Merge sort | Quicksort |
|---|---|---|
| Divide | cut in the middle, effortless | partition, laborious |
| Combine | merge two sorted segments, laborious | not needed |
| Comparisons | always of order $n \log n$ | $n \log n$ on average, $n^2$ in the worst case |
| Extra space | proportional to $n$ | recursion stack, $\log n$ levels on average |
| Stable | yes | no |

## 11.4. Example: Frog Crossing

**Example 11.4.1 (Frog Crossing, NOI 2000)** On the left bank of a stream is a pillar L, and on the right bank a pillar R; in the stream there are $s$ pillars and $y$ lily pads. $n$ frogs of distinct sizes, numbered $1, \dots, n$ (1 the smallest), are stacked on L, the larger below and the smaller above. The rules are:

- only one frog may jump at a time, and only the topmost one;
- a pillar (L, R, or a pillar in the stream) may hold several stacked frogs, but the larger must be below and the smaller above; a lily pad can hold only one frog;
- a frog that has left L may not jump back to L, and a frog that has jumped onto R may not leave it.

Given $s$ and $y$, what is the largest number of frogs that can all be moved to R? Denote the answer by $\mathrm{Jump}(s, y)$.

Consider simple cases first. With no pillars in the stream, each lily pad can hold only one frog: first the top $y$ frogs jump in turn onto the $y$ lily pads, frog $y + 1$ jumps directly to R, and then the frogs on the lily pads jump to R in reverse order (largest first). So $\mathrm{Jump}(0, y) = y + 1$.

Now take $s = 1$, $y = 1$. We can first transfer the top two frogs on L to the pillar S in the stream using the lily pad (a small problem of the kind $\mathrm{Jump}(0, 1)$, only with the destination changed to S), then move the remaining two frogs on L to R using the lily pad (another $\mathrm{Jump}(0, 1)$), and finally move the two frogs on S to R using the lily pad (again $\mathrm{Jump}(0, 1)$; they are smaller than the frogs on R and can be stacked on them). That is 4 frogs and 9 steps.

This is the divide-and-conquer viewpoint: a pillar in the stream plays the same role as the two banks, being able to hold several stacked frogs. Divide the whole process into three stages, "L–lily pads–S", "L–lily pads–R", and "S–lily pads–R", each of which is the same problem with one pillar fewer. First use $s - 1$ pillars and all the lily pads to transfer the upper half of the frogs onto one pillar; then use the remaining $s - 1$ pillars and the lily pads to transfer the lower half to R; finally transfer the half on that pillar to R. Hence

$$
\mathrm{Jump}(s, y) = 2\,\mathrm{Jump}(s - 1, y), \qquad \mathrm{Jump}(0, y) = y + 1,
$$

which gives $\mathrm{Jump}(s, y) = 2^s (y + 1)$. For example, for $s = 3$ and $y = 4$ at most 40 frogs can cross.

```cpp tab
#include <iostream>

long long jump(int s, int y) {
    if (s == 0) return y + 1;
    return 2 * jump(s - 1, y);
}

int main() { std::cout << jump(3, 4) << '\n'; }  // 40
```

```python tab
def jump(s: int, y: int) -> int:
    return y + 1 if s == 0 else 2 * jump(s - 1, y)

print(jump(3, 4))  # 40
```

The program itself is only a few lines; the difficulty lies in modeling: first derive a conclusion from the simple case $s = 0$, then find the observation that "a pillar is equivalent to a bank that can temporarily hold frogs", and the problem decomposes. The argument above shows that $2^s(y + 1)$ frogs can cross; it is also the maximum, which needs an argument in the other direction (considering the positions of the other frogs before the largest frog jumps to R) that we omit here.

## 11.5. Example: The Nine Linked Rings

**Example 11.5.1 (Nine Linked Rings)** The nine linked rings puzzle consists of 9 rings threaded on a horizontal bar (the "sword"), numbered $1, \dots, 9$ from the outside inward. The rule is: ring 1 can be moved on or off the bar at any time; ring $k$ ($k \geq 2$) can be moved on or off if and only if ring $k-1$ is on the bar and rings $1, \dots, k-2$ are all off the bar. At the start all 9 rings are on the bar; find the steps that take them all off.

To take off ring $n$, ring $n-1$ must first be on the bar and rings $1, \dots, n-2$ all off. So "taking off the first $n$ rings" decomposes into:

1. take off the first $n - 2$ rings;
2. take off ring $n$ (now ring $n - 1$ is on the bar and all smaller ones are off, so this is legal);
3. put on the first $n - 2$ rings (restoring the condition for taking off ring $n - 1$);
4. take off the first $n - 1$ rings.

Step 3, "put on the first $n - 2$ rings", is a symmetric subproblem and decomposes in the same way: first put on the first $n - 1$ rings, then take off the first $n - 2$ rings, put on ring $n$, and finally put on the first $n - 2$ rings. Two mutually calling recursive functions describe all the steps:

```cpp tab
#include <iostream>

int steps = 0;
void put_on(int n);

void take_off(int n) {                 // rings 1..n are on; take all of them off
    if (n == 0) return;
    if (n == 1) { std::cout << "off 1\n"; ++steps; return; }
    take_off(n - 2);
    std::cout << "off " << n << '\n'; ++steps;
    put_on(n - 2);
    take_off(n - 1);
}

void put_on(int n) {                   // rings 1..n are off; put all of them on
    if (n == 0) return;
    if (n == 1) { std::cout << "on 1\n"; ++steps; return; }
    put_on(n - 1);
    take_off(n - 2);
    std::cout << "on " << n << '\n'; ++steps;
    put_on(n - 2);
}

int main() {
    take_off(9);
    std::cout << steps << " steps\n";  // 341
}
```

```python tab
def take_off(n: int, moves: list[str]) -> None:
    """Rings 1..n are on; take all of them off."""
    if n == 0:
        return
    if n == 1:
        moves.append("off 1")
        return
    take_off(n - 2, moves)
    moves.append(f"off {n}")
    put_on(n - 2, moves)
    take_off(n - 1, moves)

def put_on(n: int, moves: list[str]) -> None:
    """Rings 1..n are off; put all of them on."""
    if n == 0:
        return
    if n == 1:
        moves.append("on 1")
        return
    put_on(n - 1, moves)
    take_off(n - 2, moves)
    moves.append(f"on {n}")
    put_on(n - 2, moves)

moves: list[str] = []
take_off(9, moves)
print(len(moves), "steps")  # 341
```

Let $a_n$ be the number of steps to take off (or put on, which is symmetric) $n$ rings. The decomposition gives $a_n = a_{n-1} + 2a_{n-2} + 1$ with $a_1 = 1$ and $a_2 = 2$, so $a_n$ takes the values $1, 2, 5, 10, 21, 42, 85, 170, 341$: for odd $n$, $a_n = (2^{n+1} - 1)/3$, and for even $n$, $a_n = (2^{n+1} - 2)/3$. The nine linked rings take 341 steps. As with the Tower of Hanoi, the number of steps grows exponentially with the number of rings; the difference is that here there are two kinds of subproblems (taking off and putting on), which recurse into each other.

## Summary

- Divide and conquer = divide + solve recursively + combine; it requires the subproblems to be mutually independent; the work satisfies $T(n) = aT(n/b) + f(n)$.
- Merge sort: easy to split, laborious to merge; always of order $n \log n$, stable, needs extra space.
- Quicksort: laborious to split, easy to merge; $n \log n$ on average, in place, a random pivot avoids the worst case, unstable.
- When analyzing a process, first compute the simple cases, then look for the structure in which "after removing one component the problem is still the same" (the pillars in frog crossing, the first $n - 2$ rings in the nine linked rings).
