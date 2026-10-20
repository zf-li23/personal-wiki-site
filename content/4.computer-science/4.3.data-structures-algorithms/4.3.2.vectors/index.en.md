---
title: Vectors
description: Abstract data types and data structures; the vector interface and a class-template implementation; capacity doubling and amortized analysis, incremental growth, shrinking and the load factor, how Python list and C++ vector grow; insertion, removal, search, deduplication and traversal of unsorted vectors; uniquification of sorted vectors, three versions of binary search, Fibonacci search and interpolation search; bubble sort and merge sort, stability and the lower bound for comparison sorting; bitmaps and sieves.
source_hash: 286ccda2b7ca
---

The array is the most basic way to organize data, but its length is fixed and its interface is crude. This chapter wraps the array into an abstract data type, the vector. The vector is the first complete data structure, and the stacks, heaps, hash tables and adjacency lists of graphs that follow are all built on it. The chapter has three threads. The first is the separation of interface from implementation (abstract data types). The second is dynamic space management and its analysis tool, amortized analysis. The third is the value of order: once a vector is sorted, search drops from linear to logarithmic time and deduplication from quadratic to linear time. [4.1.6](/4.1.6) covered how to use arrays and binary search, and [4.2.10](/4.2.10) covered how to use `std::vector`; this chapter shows how they are implemented and how their complexities are proved.

## 2.1. Abstract Data Types and Vectors

### 2.1.1. Interface and Implementation

**Definition 2.1.1 (Abstract Data Type)** A type consisting of a data model together with a set of operations defined on that model is called an **abstract data type** (ADT). It specifies only the semantics of the operations (their external logical behavior), not how the data is stored, and it does not consider the complexity of the operations. The complete set of storage schemes and algorithms that implements an abstract data type in some language is called a data structure for it; one abstract data type can have many implementations with different complexities.

An abstract data type defines the interface that divides the work between the implementer and the user of a data structure: the implementer is responsible for realizing each operation efficiently (building the refrigerator, building the car), and the user only follows the interface (using the refrigerator, driving the car). This is precisely **data abstraction** and **encapsulation** ([4.2.1](/4.2.1), [4.2.3](/4.2.3)): one interface needs to be implemented only once, algorithms and data structures can then be combined conveniently, and code becomes shorter, safer and more reusable. In C++ an abstract data type is expressed as a class **template**, and in Python as a class.

### 2.1.2. From Arrays to Vectors

In a C/C++ array `A[0, n)`, elements correspond one-to-one with indices, and every element can be accessed directly by its index: if each element occupies $s$ bytes, the address of `A[i]` is $A + i \cdot s$, and access takes only $O(1)$ time.

**Definition 2.1.2 (Vector)** A sequence formed by encapsulating a group of elements in linear order is called a **vector**: its $n$ elements correspond one-to-one with the integers in $[0, n)$, and exactly $r$ elements precede the element $V[r]$; $r$ is called its *rank*. Accessing an element directly through its rank is called *call-by-rank* access.

A vector is an abstraction and generalization of the array: the element type can be chosen flexibly (it may be another complex data structure), the length can change dynamically, and operations and management are more uniform and safer. The abstract data type of the vector provides the following interface.

| Operation | Function | Applies to |
|---|---|---|
| `size()` / `empty()` | Number of elements / whether empty | Vector |
| `V[r]` | Read or write the element of rank $r$ | Vector |
| `insert(r, e)` / `insert(e)` | Insert $e$ as the element of rank $r$ / as the last element | Vector |
| `remove(lo, hi)` / `remove(r)` | Delete the elements in $[\mathit{lo}, \mathit{hi})$ / the element of rank $r$ | Vector |
| `disordered()` / `sort()` | Count adjacent inverted pairs / sort | Vector |
| `find(e)` / `search(e)` | Look up $e$ | Vector / sorted vector |
| `dedup()` / `uniquify()` | Remove duplicate elements | Vector / sorted vector |
| `traverse(visit)` | Traverse, applying `visit` to every element | Vector |

These interface names follow Deng Junhui's textbook. They correspond to the C++ standard library as follows: `insert(e)` is `push_back`, `remove` is `erase`, `find` and `search` are `std::find` and `std::upper_bound`, and `uniquify` is `std::unique` plus `erase`.

## 2.2. Extendable Vectors

### 2.2.1. Dynamic Space Management

Internally, a vector stores its elements in a contiguous block of memory `elem`, and records the number of elements `size` and the block's capacity `capacity`. A fixed capacity (static space management) has clear drawbacks: the block may be too small to hold all the elements, causing overflow even though the system often still has plenty of space; or it may hold very few elements, wasting space. The ratio $\lambda = \mathit{size}/\mathit{capacity}$ is called the *load factor*; it measures space utilization. In general applications it is hard to estimate the required space accurately in advance.

The idea of dynamic space management is like a cicada molting: when the block is about to overflow, allocate a larger block, copy the elements over, and release the old block. The key question is how large the new capacity should be.

**Algorithm 2.2.1 (Capacity Doubling)** Before inserting an element, if the vector is full ($\mathit{size} = \mathit{capacity}$), allocate a block with twice the capacity, move the elements into it one by one, and release the old block.

Below is the core of the vector. The C++ version manages the block with `std::unique_ptr<T[]>` (**resource acquisition is initialization**, RAII, [4.2.4](/4.2.4)), so release is automatic and no **dangling pointer** can occur; ranks use the signed type `std::ptrdiff_t` so that $-1$ can indicate failure. Python has no fixed-length arrays, so `[None] * c` simulates a block of $c$ slots, read and written only by index, without calling the list's own `append` and `insert`.

```cpp tab
#include <algorithm>
#include <cstddef>
#include <format>
#include <iostream>
#include <memory>
#include <utility>

using Rank = std::ptrdiff_t;    // signed, so that lo - 1 can report a failure

template <typename T>
class Vector {
public:
    static constexpr Rank kMinCapacity = 4;

    explicit Vector(Rank c = kMinCapacity)
        : capacity_(std::max(c, kMinCapacity)), elem_(std::make_unique<T[]>(capacity_)) {}
    Vector(const T* a, Rank lo, Rank hi) { copy_from(a, lo, hi); }   // copy a[lo, hi)
    Vector(const Vector& v) { copy_from(v.elem_.get(), 0, v.size_); }
    Vector& operator=(const Vector& v) {
        if (this != &v) copy_from(v.elem_.get(), 0, v.size_);
        return *this;
    }

    Rank size() const { return size_; }
    Rank capacity() const { return capacity_; }
    bool empty() const { return size_ == 0; }
    T& operator[](Rank r) { return elem_[r]; }                 // 0 <= r < size()
    const T& operator[](Rank r) const { return elem_[r]; }

    Rank insert(Rank r, const T& e);                           // 0 <= r <= size()
    Rank insert(const T& e) { return insert(size_, e); }       // append
    Rank remove(Rank lo, Rank hi);                             // 0 <= lo <= hi <= size()
    T remove(Rank r);                                          // 0 <= r < size()

    Rank find(const T& e, Rank lo, Rank hi) const;             // Section 2.3
    Rank find(const T& e) const { return find(e, 0, size_); }
    Rank dedup();
    template <typename Visit> void traverse(Visit&& visit);
    Rank disordered() const;                                   // Section 2.4
    Rank uniquify();
    Rank search(const T& e, Rank lo, Rank hi) const;
    Rank search(const T& e) const { return search(e, 0, size_); }

private:
    Rank size_ = 0, capacity_ = 0;
    std::unique_ptr<T[]> elem_;

    void copy_from(const T* a, Rank lo, Rank hi);
    void reallocate(Rank c);
    void expand();
    void shrink();
};

template <typename T>
void Vector<T>::copy_from(const T* a, Rank lo, Rank hi) {
    capacity_ = std::max(kMinCapacity, 2 * (hi - lo));         // leave room to grow
    elem_ = std::make_unique<T[]>(capacity_);
    for (size_ = 0; lo < hi; ++size_, ++lo) elem_[size_] = a[lo];
}

template <typename T>
void Vector<T>::reallocate(Rank c) {                           // move into a block of size c
    auto old = std::move(elem_);
    elem_ = std::make_unique<T[]>(capacity_ = c);
    for (Rank i = 0; i < size_; ++i) elem_[i] = std::move(old[i]);
}                                                              // the old block is freed here

template <typename T>
void Vector<T>::expand() {                                     // before an insertion
    if (size_ == capacity_) reallocate(2 * capacity_);         // full: double the capacity
}

template <typename T>
void Vector<T>::shrink() {                                     // after a removal
    if (capacity_ > kMinCapacity && 4 * size_ < capacity_)     // load factor below 1/4:
        reallocate(capacity_ / 2);                             // halve the capacity
}

template <typename T>
Rank Vector<T>::insert(Rank r, const T& e) {
    expand();
    for (Rank i = size_; i > r; --i) elem_[i] = std::move(elem_[i - 1]);   // shift right
    elem_[r] = e;
    ++size_;
    return r;
}

template <typename T>
Rank Vector<T>::remove(Rank lo, Rank hi) {
    if (lo == hi) return 0;
    while (hi < size_) elem_[lo++] = std::move(elem_[hi++]);   // shift [hi, n) left
    size_ = lo;
    shrink();
    return hi - lo;                                            // number of removed elements
}

template <typename T>
T Vector<T>::remove(Rank r) {
    T e = std::move(elem_[r]);
    remove(r, r + 1);
    return e;
}

int main() {
    Vector<int> v;
    Rank last = v.capacity();
    auto report = [&] {                        // print the capacity whenever it changes
        if (v.capacity() != last)
            std::cout << std::format("size {:2}: capacity {} -> {}\n",
                                     v.size(), last, v.capacity());
        last = v.capacity();
    };
    for (int i = 0; i < 40; ++i) { v.insert(i); report(); }
    while (v.size() > 2) { v.remove(0); report(); }
}
```

```python tab
from collections.abc import Callable, Iterable, Iterator
from typing import Any


class Vector:
    """A dynamic array on a fixed-size block of slots; the block is only indexed."""
    MIN_CAPACITY = 4

    def __init__(self, items: Iterable[Any] = ()) -> None:
        self._size = 0
        self._capacity = self.MIN_CAPACITY
        self._elem: list[Any] = [None] * self._capacity
        for e in items:
            self.insert(self._size, e)

    def __len__(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def __getitem__(self, r: int) -> Any:          # 0 <= r < size
        if not 0 <= r < self._size:
            raise IndexError(r)
        return self._elem[r]

    def __setitem__(self, r: int, e: Any) -> None:
        if not 0 <= r < self._size:
            raise IndexError(r)
        self._elem[r] = e

    def __iter__(self) -> Iterator[Any]:
        for r in range(self._size):
            yield self._elem[r]

    def __repr__(self) -> str:
        return f"Vector([{', '.join(map(repr, self))}])"

    def _reallocate(self, c: int) -> None:         # move into a block of size c
        old, self._elem, self._capacity = self._elem, [None] * c, c
        for i in range(self._size):
            self._elem[i] = old[i]

    def _expand(self) -> None:                     # before an insertion
        if self._size == self._capacity:           # full: double the capacity
            self._reallocate(2 * self._capacity)

    def _shrink(self) -> None:                     # after a removal
        if self._capacity > self.MIN_CAPACITY and 4 * self._size < self._capacity:
            self._reallocate(self._capacity // 2)  # load factor below 1/4: halve

    def insert(self, r: int, e: Any) -> int:       # 0 <= r <= size
        self._expand()
        for i in range(self._size, r, -1):         # shift the suffix right
            self._elem[i] = self._elem[i - 1]
        self._elem[r] = e
        self._size += 1
        return r

    def append(self, e: Any) -> int:
        return self.insert(self._size, e)

    def remove_range(self, lo: int, hi: int) -> int:   # 0 <= lo <= hi <= size
        if lo == hi:
            return 0
        while hi < self._size:                     # shift the suffix [hi, n) left
            self._elem[lo] = self._elem[hi]
            lo, hi = lo + 1, hi + 1
        for i in range(lo, self._size):            # drop references to removed objects
            self._elem[i] = None
        self._size = lo
        self._shrink()
        return hi - lo                             # number of removed elements

    def remove(self, r: int) -> Any:               # 0 <= r < size
        e = self._elem[r]
        self.remove_range(r, r + 1)
        return e


v = Vector()
last = v.capacity()

def report() -> None:                          # print the capacity whenever it changes
    global last
    if v.capacity() != last:
        print(f"size {len(v):2}: capacity {last} -> {v.capacity()}")
    last = v.capacity()

for i in range(40):
    v.append(i)
    report()
while len(v) > 2:
    v.remove(0)
    report()
```

The program inserts 40 elements and then removes them one by one, printing how the capacity changes: when the 5th, 9th, 17th and 33rd elements are inserted, the capacity doubles from 4 to 8, 16, 32 and 64; when removal leaves 15, 7 and 3 elements, the capacity is halved in turn (shrinking is discussed in Section 2.2.3).

Insertion `insert(r, e)` shifts the suffix $[r, n)$ back by one cell, from the end toward the front, and then places the new element, taking $O(n - r)$ time; the shift must go from back to front, or elements not yet moved would be overwritten. Range removal `remove(lo, hi)` shifts the suffix $[\mathit{hi}, n)$ forward by $\mathit{hi} - \mathit{lo}$ cells, taking $O(n - \mathit{hi})$ time; the shift must go from front to back. Removing a single element is just the special case $[r, r+1)$. Conversely, implementing range removal by calling `remove(r)` repeatedly would move the entire suffix each time, for a total of $O((\mathit{hi} - \mathit{lo})(n - \mathit{hi}))$, up to $O(n^2)$ in the worst case; so range removal is the basic operation and single-element removal is derived from it.

### 2.2.2. Amortized Analysis

Looking at a single insertion, in the worst case all $n$ elements must be copied, which takes $O(n)$ time. But expansion happens rarely: right after an expansion, at least $n$ more elements must be inserted before the next one. Looking only at the worst case of a single operation badly overestimates the total cost, so another method of analysis is needed.

**Definition 2.2.1 (Amortized Analysis)** Apply enough consecutive operations to a data structure and spread the total cost over the individual operations: if for every operation sequence of length $m$ the total cost is at most $m \cdot f(n)$, the amortized cost of each operation is said to be $O(f(n))$. This method of analysis is called **amortized analysis**, and the resulting complexity is called amortized complexity.

**Definition 2.2.2 (Average-Case Analysis)** Given the probability distribution of the various inputs or operations, take the weighted average of the corresponding costs. This method of analysis is called **average-case analysis**, and the resulting complexity is called the average (expected) complexity.

The two differ as follows. Average-case analysis treats operations as independent events and needs probabilistic assumptions about the input, which severs the correlation between operations. Amortized analysis examines the total cost of the operation sequences that can actually occur, needs no probabilistic assumption, and gives a worst-case guarantee (except that the guarantee is for the whole sequence rather than for a single operation). When analyzing data structures, amortized analysis often describes real performance more faithfully. The three standard methods of amortized analysis (aggregate, accounting, potential) appear in [4.3.4](/4.3.4); here we use the most direct one, the aggregate method: compute the total cost of the whole sequence and divide by the number of operations.

**Theorem 2.2.1** Starting from an empty vector of capacity $c_0 \geq 1$, insert $n$ elements consecutively. With the capacity-doubling strategy, the total copying time for expansions is $O(n)$ and the amortized time per insertion is $O(1)$. With the incremental strategy (each expansion adds a fixed $I$ cells), the total copying time is $\Theta(n^2/I)$ and the amortized time per insertion is $\Theta(n/I)$.

**Proof** Doubling: expansions occur when the number of elements reaches $c_0, 2c_0, 4c_0, \dots$, and at the last expansion the number of elements is less than $n$. The numbers of elements copied form a geometric series whose sum is dominated by the last term:

$$
c_0 + 2c_0 + 4c_0 + \cdots + 2^k c_0 < 2 \cdot 2^k c_0 < 2n,
$$
and adding the $n$ writes, the total time is at most $3n$. Incremental: expansions occur when the number of elements reaches $I, 2I, 3I, \dots$, about $m = n/I$ times, and the numbers of elements copied form an arithmetic series:

$$
I + 2I + \cdots + (m-1)I = I \cdot \frac{m(m-1)}{2} = \Theta(n^2 / I). \qquad \square
$$

The left side of the figure below compares the total cost of the two strategies, and the right side shows the actual cost of each insertion under doubling: most insertions cost only 1 unit, an occasional one is very expensive, but the running average never exceeds 3.

![Left: total cost of incremental growth (64 each time) versus doubling; right: actual and average cost of each insertion under doubling](./plots/expansion-strategies.py)

More generally, if the capacity is multiplied by a constant $r > 1$ at each expansion, the total number of elements copied is at most $n \cdot \frac{r}{r-1}$ and the amortized time is still $O(1)$, at the price that the load factor may fall as low as $1/r$:

| Strategy | Cumulative expansion time | Amortized expansion time | Load factor |
|---|---|---|---|
| Incremental $I$ | $\Theta(n^2/I)$ | $\Theta(n/I)$ | $\approx 100\%$ |
| Doubling | $\Theta(n)$ | $O(1)$ | $> 50\%$ |
| Multiply by $r > 1$ | $\Theta(n)$, constant about $\frac{r}{r-1}$ | $O(1)$ | $> 1/r$ |

Trading space for time costs only a constant factor here: the doubling strategy wastes at most half of the space, yet lowers the cost of expansion from quadratic to linear.

### 2.2.3. Shrinking

Deletion lowers the load factor. If we halve the capacity when the load factor falls below some threshold, the threshold cannot be $1/2$. Suppose the capacity is $2c$ and there are exactly $c + 1$ elements, and we alternate deletions and insertions: each deletion drops the load factor below $1/2$ and shrinks the capacity to $c$, each insertion then fills the vector and expands the capacity back to $2c$, and every operation copies about $c$ elements.

The implementation above halves the capacity only when the load factor falls below $1/4$. After each reallocation, the load factor is about $1/2$: after an expansion the number of elements is about half the new capacity $C$; before a shrink the number of elements is below $1/4$ of the old capacity, which is about half the new capacity $C$. From this state, if the next reallocation is an expansion, at least about $C/2$ more elements must be inserted, and about $C$ elements are copied; if it is a shrink, at least about $C/4$ more elements must be deleted, and fewer than $C/4$ elements are copied. In either case the number of elements copied is at most a constant multiple (about 2) of the number of operations in the meantime, so with arbitrarily interleaved insertions and deletions the amortized time per operation is still $O(1)$.

### 2.2.4. Python's list and C++'s vector

CPython's `list` is a dynamic array: internally an object holds a pointer to an array of element pointers, together with the number of elements and the allocated capacity. The growth rule of CPython 3.12 is roughly this: to hold $m$ elements, the new capacity is $m + \lfloor m/8 \rfloor + 6$, rounded down to a multiple of 4; the list shrinks when the number of elements falls below half the capacity. Thus under `append` the capacities are $4, 8, 16, 24, 32, 40, 52, 64, 76, 92, \dots$, with a growth factor of about $1.125$. By the formula of the previous section the total copying is about $9n$ and the amortized time is still $O(1)$; since the array stores only 8-byte pointers, and the underlying `realloc` can often extend in place, the actual cost is small.

| Operation | Complexity |
|---|---|
| `a[i]`, `a[i] = x`, `len(a)` | $O(1)$ |
| `a.append(x)`, `a.pop()` | Amortized $O(1)$ |
| `a.insert(i, x)`, `a.pop(i)`, `del a[i]` | $O(n - i)$ |
| `x in a`, `a.index(x)`, `a.count(x)` | $O(n)$ |
| `a[i:j]` (slice copy) | $O(j - i)$ |
| `a.sort()`, `sorted(a)` | $O(n \log n)$ |

So repeatedly inserting or deleting at the head of a list (`insert(0, x)`, `pop(0)`) takes $O(n)$ each time, and `collections.deque` ([4.3.4](/4.3.4)) should be used instead.

C++'s `std::vector` has the same structure as this chapter's `Vector` ([4.2.10](/4.2.10)): when `size()` reaches `capacity()`, libstdc++ and libc++ double the capacity, while MSVC multiplies it by 1.5. Choosing a growth factor below the golden ratio $\phi \approx 1.618$ has an advantage: the sum of several previously released old blocks can eventually exceed the new request, so the memory allocator has a chance to reuse them, whereas with doubling the new block is always larger than the sum of all previously released blocks. `std::vector` never shrinks automatically; `reserve(n)` preallocates capacity to avoid repeated expansion; `shrink_to_fit()` requests release of excess capacity (the standard does not guarantee compliance).

## 2.3. Unsorted Vectors

### 2.3.1. Search

An unsorted vector supports only equality tests, so search can only compare elements one by one. The `find` below searches the interval $[\mathit{lo}, \mathit{hi})$ from back to front and returns the largest rank among elements equal to $e$; on failure it returns $\mathit{lo} - 1$, a value outside any valid interval that unambiguously signals failure, which the caller can test. These member functions are used together with the class definition of the previous section.

```cpp tab
template <typename T>
Rank Vector<T>::find(const T& e, Rank lo, Rank hi) const {     // 0 <= lo <= hi <= size()
    while (lo < hi && elem_[hi - 1] != e) --hi;                // scan from back to front
    return hi - 1;                                             // the last match, or lo - 1
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def find(self, e: Any, lo: int = 0, hi: int | None = None) -> int:
        """Rank of the last element == e in [lo, hi), or lo - 1."""
        if hi is None:
            hi = self._size
        while lo < hi and self._elem[hi - 1] != e:   # scan from back to front
            hi -= 1
        return hi - 1
```

In the best case (the last element is $e$) it takes only $O(1)$ time, and in the worst case (the search fails or $e$ is at the front) it takes $O(n)$ time; the two differ substantially. An algorithm whose complexity depends on the particular input, not only on its size, is called *input-sensitive*.

Elements must support equality tests (`==`, `!=`); the sorted vectors below also need comparison (`<`). If the elements are "key-value" pairs (entries), equality and comparison look only at the key: entries judged equal need not be identical. In C++20 one can define `operator==` and `operator<=>` (the **three-way comparison operator**) for the entry class, and in Python `__eq__` and `__lt__` (**special methods**).

### 2.3.2. Deduplication

`dedup()` removes duplicate elements from an unsorted vector, keeping only the first of each group of equal elements.

```cpp tab
template <typename T>
Rank Vector<T>::dedup() {                                      // keep the first copy of each value
    Rank old_size = size_;
    for (Rank i = 1; i < size_;)
        if (find(elem_[i], 0, i) < 0) ++i;                     // new value: keep it
        else remove(i);                                        // seen before: remove it
    return old_size - size_;
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def dedup(self) -> int:                        # keep the first copy of each value
        old_size, i = self._size, 1
        while i < self._size:
            if self.find(self._elem[i], 0, i) < 0:
                i += 1                             # new value: keep it
            else:
                self.remove(i)                     # seen before: remove it
        return old_size - self._size
```

Correctness comes from a **loop invariant**: the elements of the prefix $[0, i)$ are pairwise distinct. It holds trivially at the start, $i = 1$. In each round we examine $V[i]$: if it does not occur in the prefix, we keep it and increase $i$ by one; otherwise we delete it; the invariant is preserved either way. In each round either $i$ increases by one or the size decreases by one, so the loop terminates after at most $n$ rounds. In each round the times of `find` and `remove` add up to $O(i) + O(n - i) = O(n)$, so the total time is $O(n^2)$. Sorting first and then using `uniquify()` from the next section improves this to $O(n \log n)$; with a hash table ([4.3.9](/4.3.9)) expected $O(n)$ is achievable.

### 2.3.3. Traversal

Traversal applies some operation `visit` uniformly to every element of the vector. In C one passes a function pointer; more flexible is to pass a **function object** or a **lambda expression** ([4.2.12](/4.2.12)), which can carry state (such as an accumulator) and are also easy for the compiler to inline.

```cpp tab
template <typename T>
template <typename Visit>
void Vector<T>::traverse(Visit&& visit) {
    for (Rank i = 0; i < size_; ++i) visit(elem_[i]);
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def traverse(self, visit: Callable[[Any], Any]) -> None:
        for r in range(self._size):
            visit(self._elem[r])
```

For example, `v.traverse([](int& x) { x *= 10; })` multiplies every element by 10, and `v.traverse([&sum](int x) { sum += x; })` computes the sum. The C++ version declares `visit` as a forwarding reference `Visit&&`, so it accepts any callable object. In Python, `visit` receives a reference to the element, so immutable objects (such as integers) cannot be modified in place, only read.

## 2.4. Sorted Vectors

### 2.4.1. Order

**Definition 2.4.1 (Sorted Vector)** A vector whose elements are all in nondecreasing order, that is, $V[r-1] \leq V[r]$ for every $0 < r < n$, is called a **sorted vector**.

In a sorted vector every pair of adjacent elements is in order; conversely, the number of adjacent inverted pairs measures to some extent how disordered a vector is. `disordered()` counts this number, and returns 0 if and only if the vector is sorted.

```cpp tab
template <typename T>
Rank Vector<T>::disordered() const {                           // number of adjacent inversions
    Rank count = 0;
    for (Rank i = 1; i < size_; ++i)
        if (elem_[i] < elem_[i - 1]) ++count;
    return count;
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def disordered(self) -> int:                   # number of adjacent inversions
        return sum(self._elem[i] < self._elem[i - 1] for i in range(1, self._size))
```

Once an unsorted vector has been preprocessed (sorted) into a sorted vector, many algorithms can be optimized.

### 2.4.2. Uniquification

Equal elements in a sorted vector are necessarily adjacent. One direct approach is to scan from front to back and delete the current element whenever it equals the previous one. Each deletion moves the suffix, so when many elements are equal the total time is $O(n^2)$: diligent but inefficient.

A better approach is not to delete, but to move the first element of each group of equal elements directly forward, and truncate the tail once at the end. Use two indices: $i$ points to the last element of the prefix of distinct elements already determined, and $j$ scans forward; when an element different from $V[i]$ is found, it is moved to $V[i + 1]$. This approach is called the *two-pointer technique*.

```cpp tab
template <typename T>
Rank Vector<T>::uniquify() {                                   // the vector must be sorted
    if (size_ < 2) return 0;
    Rank i = 0;                                                // elem_[0, i] are distinct
    for (Rank j = 1; j < size_; ++j)
        if (elem_[i] != elem_[j]) elem_[++i] = std::move(elem_[j]);   // next distinct value
    Rank removed = size_ - (i + 1);
    size_ = i + 1;
    shrink();
    return removed;
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def uniquify(self) -> int:                     # the vector must be sorted
        if self._size < 2:
            return 0
        i = 0                                      # elem[0..i] are distinct
        for j in range(1, self._size):
            if self._elem[i] != self._elem[j]:     # next distinct value
                i += 1
                self._elem[i] = self._elem[j]
        return self.remove_range(i + 1, self._size)
```

Invariant: $V[0..i]$ consists of the distinct elements of $V[0..j)$ in their original order, and $V[i]$ is the largest of them. $j$ increases by one each round and each element is moved at most once, so the total time is $O(n)$.

### 2.4.3. Binary Search (Version A)

In a sorted vector, any element $x = V[\mathit{mi}]$ divides the search interval $[\mathit{lo}, \mathit{hi})$ into three parts: the elements in $[\mathit{lo}, \mathit{mi})$ are all no greater than $x$, and those in $(\mathit{mi}, \mathit{hi})$ are all no less than $x$. So one comparison of the target $e$ with $x$ suffices to shrink the problem: go into the left side when $e < x$, into the right side when $x < e$, and we have a hit when $e = x$. This is the decrease-and-conquer idea of **binary search** ([4.1.6](/4.1.6)).

**Algorithm 2.4.1 (Binary Search, Version A)** Take $\mathit{mi}$ to be the midpoint of the interval and handle the three cases above, until a hit occurs or the interval is empty.

```cpp tab
#include <cstddef>
#include <format>
#include <iostream>
#include <span>

using Rank = std::ptrdiff_t;

// Version A: compare with the middle element, three-way branching.
template <typename T>
Rank bin_search_a(std::span<const T> s, const T& e) {
    Rank lo = 0, hi = std::ssize(s);
    while (lo < hi) {
        Rank mi = lo + (hi - lo) / 2;
        if (e < s[mi]) hi = mi;               // continue in [lo, mi)
        else if (s[mi] < e) lo = mi + 1;      // continue in (mi, hi)
        else return mi;                       // hit
    }
    return -1;                                // miss
}

// Fibonacci search: the pivot splits [lo, hi) at a Fibonacci number.
template <typename T>
Rank fib_search(std::span<const T> s, const T& e) {
    Rank lo = 0, hi = std::ssize(s);
    Rank f = 1, g = 0;                        // (f, g) = (F(k), F(k-1))
    while (f <= hi) { f += g; g = f - g; }    // step up until F(k) > n
    while (lo < hi) {
        while (hi - lo < f) { g = f - g; f -= g; }   // step down: largest F(k) <= hi - lo
        Rank mi = lo + f - 1;
        if (e < s[mi]) hi = mi;
        else if (s[mi] < e) lo = mi + 1;
        else return mi;
    }
    return -1;
}

int main() {
    const int a[] = {1, 3, 4, 6, 8, 9, 11, 14, 17, 20, 23, 25};
    std::span<const int> s = a;
    for (int e : {8, 1, 25, 10})
        std::cout << std::format("{:2}: A -> {:2}, Fibonacci -> {:2}\n",
                                 e, bin_search_a(s, e), fib_search(s, e));
}
```

```python tab
def bin_search_a(s: list, e) -> int:
    """Version A: compare with the middle element, three-way branching."""
    lo, hi = 0, len(s)
    while lo < hi:
        mi = (lo + hi) // 2
        if e < s[mi]:
            hi = mi                    # continue in [lo, mi)
        elif s[mi] < e:
            lo = mi + 1                # continue in (mi, hi)
        else:
            return mi                  # hit
    return -1                          # miss

def fib_search(s: list, e) -> int:
    """Fibonacci search: the pivot splits [lo, hi) at a Fibonacci number."""
    lo, hi = 0, len(s)
    f, g = 1, 0                        # (f, g) = (F(k), F(k-1))
    while f <= hi:                     # step up until F(k) > n
        f, g = f + g, f
    while lo < hi:
        while hi - lo < f:             # step down: largest F(k) <= hi - lo
            f, g = g, f - g
        mi = lo + f - 1
        if e < s[mi]:
            hi = mi
        elif s[mi] < e:
            lo = mi + 1
        else:
            return mi
    return -1

a = [1, 3, 4, 6, 8, 9, 11, 14, 17, 20, 23, 25]
for e in (8, 1, 25, 10):
    print(f"{e:2}: A -> {bin_search_a(a, e):2}, Fibonacci -> {fib_search(a, e):2}")
```

(The same program also contains the Fibonacci search of the next section.) After at most two comparisons, either there is a hit or the interval is halved, so $T(n) = T(n/2) + O(1) = O(\log n)$, far better than sequential search.

A finer measure is the number of key comparisons. Note that in version A the two branches have different costs: first compare `e < s[mi]`, and if it holds go left, costing 1 comparison; otherwise compare `s[mi] < e`, and going right or hitting both cost 2 comparisons. Under the assumption that all cases are equally likely, the average number of comparisons for a successful (unsuccessful) search is called the average successful (unsuccessful) search length. Take $n = 7$ as an example: the numbers of comparisons for the 7 successful cases are $4, 3, 5, 2, 5, 4, 6$, averaging $29/7 \approx 4.14$; the 8 unsuccessful cases average $36/8 = 4.5$. In general, the average search length of version A is about $1.5 \log_2 n$: each level descended costs 1.5 comparisons on average.

### 2.4.4. Fibonacci Search

In version A, going left (1 comparison) costs less than going right (2 comparisons), while the recursion depths on the two sides are the same. If we make the left side longer and the right side shorter, using the imbalance in recursion depth to compensate for the imbalance in the cost of turning, the average search length should shrink further.

**Algorithm 2.4.2 (Fibonacci Search)** Let the length of the search interval be $F_k - 1$ ($F_k$ a Fibonacci number) and take the pivot $\mathit{mi} = \mathit{lo} + F_{k-1} - 1$. Then the left and right subintervals have lengths $F_{k-1} - 1$ and $F_{k-2} - 1$, which again have the same form; comparisons are made as in version A. When the length is not of the form $F_k - 1$, at each step take the largest Fibonacci number $F$ not exceeding the interval length and set $\mathit{mi} = \mathit{lo} + F - 1$.

The `fib_search` above needs no precomputed table of Fibonacci numbers: the pair $(f, g) = (F_k, F_{k-1})$ can be advanced in place to $(F_{k+1}, F_k)$, or moved back in place to $(F_{k-1}, F_{k-2})$. The total number of moves back is $O(\log n)$, so the amortized cost of determining the pivot is $O(1)$. For $n = 7$, the average successful search length of Fibonacci search is $28/7 = 4$ and the unsuccessful one is $35/8 \approx 4.38$, both slightly better than version A.

Why Fibonacci numbers? Consider a general strategy: always take the pivot at fraction $\lambda$ of the interval length ($0 < \lambda < 1$; binary search has $\lambda = 1/2$). Let the average number of comparisons for success be $\alpha(\lambda) \log_2 n$. Writing the recurrence by going left (probability about $\lambda$, 1 comparison) or right (probability about $1 - \lambda$, 2 comparisons):

$$
\alpha \log_2 n = \lambda\bigl(1 + \alpha \log_2(\lambda n)\bigr) + (1 - \lambda)\bigl(2 + \alpha \log_2((1-\lambda) n)\bigr),
$$
which simplifies to

$$
\alpha(\lambda) = \frac{\lambda - 2}{\lambda \log_2 \lambda + (1 - \lambda) \log_2(1 - \lambda)}.
$$
We have $\alpha(1/2) = 1.5$, and $\alpha(\lambda)$ attains its minimum of about $1.44$ at $\lambda = \phi - 1 = \frac{\sqrt5 - 1}{2} \approx 0.618$: this is exactly the split ratio of Fibonacci search.

### 2.4.5. Binary Search (Versions B and C)

The imbalance in the cost of turning can also be removed directly: do only one comparison per iteration, with only two branches.

**Algorithm 2.4.3 (Binary Search, Version B)** Take the midpoint $\mathit{mi}$; if $e < V[\mathit{mi}]$, go into $[\mathit{lo}, \mathit{mi})$, otherwise into $[\mathit{mi}, \mathit{hi})$; only when the interval length is 1 do we test for a hit.

Compared with version A, version B does not return early even if it meets $e$ along the way, so the best case gets worse and the worst case gets better, and overall performance is more balanced: every search takes exactly about $\log_2 n$ comparisons.

Version B has another drawback: on failure it only returns $-1$, and when several elements match it cannot guarantee which one is returned. To maintain a sorted vector, however, `search` needs to supply more information. For example, when inserting a new element $e$ we would like to write `V.insert(V.search(e) + 1, e)`: even if the search fails, it must give a position where the new element can be placed (sortedness); if equal elements already exist, the new element should go after them (stability, see Section 2.5.1). Therefore we adopt the convention that `search(e)` always returns the rank $m$ of the last element not greater than $e$ (or $\mathit{lo} - 1$ if there is none).

**Algorithm 2.4.4 (Binary Search, Version C)** Take the midpoint $\mathit{mi}$; if $e < V[\mathit{mi}]$, set $\mathit{hi} \gets \mathit{mi}$, otherwise set $\mathit{lo} \gets \mathit{mi} + 1$; continue until the interval is empty, then return $\mathit{lo} - 1$.

```cpp tab
#include <cstddef>
#include <format>
#include <iostream>
#include <span>

using Rank = std::ptrdiff_t;

// Version B: one comparison per step, two-way branching; check for a hit at the end.
template <typename T>
Rank bin_search_b(std::span<const T> s, const T& e) {
    Rank lo = 0, hi = std::ssize(s);
    if (hi == 0) return -1;
    while (hi - lo > 1) {                     // stop when one candidate is left
        Rank mi = lo + (hi - lo) / 2;
        if (e < s[mi]) hi = mi; else lo = mi; // [lo, mi) or [mi, hi)
    }
    return (s[lo] == e) ? lo : -1;
}

// Version C: return the rank of the last element <= e (-1 if there is none).
template <typename T>
Rank bin_search_c(std::span<const T> s, const T& e) {
    Rank lo = 0, hi = std::ssize(s);          // invariant: s[0, lo) <= e < s[hi, n)
    while (lo < hi) {
        Rank mi = lo + (hi - lo) / 2;
        if (e < s[mi]) hi = mi; else lo = mi + 1;
    }
    return lo - 1;                            // now lo == hi
}

int main() {
    const int a[] = {1, 3, 3, 3, 6, 8, 8, 11};
    std::span<const int> s = a;
    for (int e : {3, 8, 0, 5, 20})
        std::cout << std::format("{:2}: B -> {:2}, C -> {:2}\n",
                                 e, bin_search_b(s, e), bin_search_c(s, e));
}
```

```python tab
def bin_search_b(s: list, e) -> int:
    """Version B: one comparison per step, two-way branching; check for a hit at the end."""
    lo, hi = 0, len(s)
    if hi == 0:
        return -1
    while hi - lo > 1:                 # stop when one candidate is left
        mi = (lo + hi) // 2
        if e < s[mi]:
            hi = mi                    # [lo, mi)
        else:
            lo = mi                    # [mi, hi)
    return lo if s[lo] == e else -1

def bin_search_c(s: list, e) -> int:
    """Version C: return the rank of the last element <= e (-1 if there is none)."""
    lo, hi = 0, len(s)                 # invariant: s[:lo] <= e < s[hi:]
    while lo < hi:
        mi = (lo + hi) // 2
        if e < s[mi]:
            hi = mi
        else:
            lo = mi + 1
    return lo - 1                      # now lo == hi

a = [1, 3, 3, 3, 6, 8, 8, 11]
for e in (3, 8, 0, 5, 20):
    print(f"{e:2}: B -> {bin_search_b(a, e):2}, C -> {bin_search_c(a, e):2}")
```

Version C differs from version B in only two places: when $e \geq V[\mathit{mi}]$ it goes into $(\mathit{mi}, \mathit{hi})$ rather than $[\mathit{mi}, \mathit{hi})$, so the interval length can shrink to 0; and the return value. Since $V[\mathit{mi}]$ is excluded from the interval, might it be missed? The following theorem shows it is not.

**Theorem 2.4.1** The value $m$ returned by version C satisfies $V[0, m] \leq e < V[m+1, n)$; that is, $m$ is the rank of the last element not greater than $e$.

**Proof** We prove the loop invariant $V[0, \mathit{lo}) \leq e < V[\mathit{hi}, n)$ (every element of the two ranges is $\leq e$ and $> e$ respectively). Initially $\mathit{lo} = 0$ and $\mathit{hi} = n$, both ranges are empty, and the invariant holds trivially. Suppose the invariant holds before some iteration. If $e < V[\mathit{mi}]$, by sortedness every element of $V[\mathit{mi}, n)$ is $\geq V[\mathit{mi}] > e$, and after setting $\mathit{hi} = \mathit{mi}$ the invariant holds. Otherwise $V[\mathit{mi}] \leq e$, every element of $V[0, \mathit{mi}]$ is $\leq V[\mathit{mi}] \leq e$, and after setting $\mathit{lo} = \mathit{mi} + 1$ the invariant also holds. In each iteration the interval length $\mathit{hi} - \mathit{lo}$ strictly decreases, so the loop must terminate, at which point $\mathit{lo} = \mathit{hi}$ and the invariant reads $V[0, \mathit{lo}) \leq e < V[\mathit{lo}, n)$; returning $m = \mathit{lo} - 1$ is exactly what is required. $\square$

Version C uses one comparison per step, about $\lceil \log_2(n+1) \rceil$ in all; to decide whether there is a hit, the caller makes one more comparison $V[m] = e$. The figure below compares the average number of comparisons of the three algorithms for successful search: they grow linearly in $\log_2 n$, with slopes of about $1.5$, $1.44$ and $1$ respectively.

![Average number of comparisons for successful search by binary search versions A and C and Fibonacci search (n is a Fibonacci number minus one)](./plots/search-lengths.py)

The return value of version C corresponds to `std::upper_bound(first, last, e) - 1` in the standard library and `bisect.bisect_right(a, e) - 1` in Python ([4.1.6](/4.1.6)). The `search` member of the `Vector` class in Section 2.2 is exactly version C:

```cpp tab
template <typename T>
Rank Vector<T>::search(const T& e, Rank lo, Rank hi) const {   // version C, Section 2.4.5
    while (lo < hi) {
        Rank mi = lo + (hi - lo) / 2;
        if (e < elem_[mi]) hi = mi; else lo = mi + 1;
    }
    return lo - 1;                                             // the last element <= e
}
```

```python tab
class Vector:  # continued: more methods of the class in Section 2.2
    def search(self, e: Any, lo: int = 0, hi: int | None = None) -> int:
        """Version C (Section 2.4.5): rank of the last element <= e in [lo, hi)."""
        if hi is None:
            hi = self._size
        while lo < hi:
            mi = (lo + hi) // 2
            if e < self._elem[mi]:
                hi = mi
            else:
                lo = mi + 1
        return lo - 1
```

### 2.4.6. Interpolation Search

Binary search uses only the order relations among elements, not their numerical values. When looking up a word in an English dictionary, nobody starts from the middle: "binary" is at about $2/26$ of the way, and "search" at about $19/26$. If the elements follow roughly a uniform distribution, the elements in the interval $[\mathit{lo}, \mathit{hi}]$ should grow roughly linearly, and the pivot position can be guessed from the values.

**Algorithm 2.4.5 (Interpolation Search)** In the closed interval $[\mathit{lo}, \mathit{hi}]$, take the pivot

$$
\mathit{mi} = \mathit{lo} + \left\lfloor \frac{e - V[\mathit{lo}]}{V[\mathit{hi}] - V[\mathit{lo}]} \,(\mathit{hi} - \mathit{lo}) \right\rfloor,
$$
and proceed as in version A; when $e$ lies outside $[V[\mathit{lo}], V[\mathit{hi}]]$, declare failure immediately.

```cpp tab
#include <algorithm>
#include <cstddef>
#include <format>
#include <iostream>
#include <memory>
#include <random>
#include <span>

using Rank = std::ptrdiff_t;

// Interpolation search on sorted numbers; counts the probes it makes.
Rank interpolation_search(std::span<const long long> s, long long e, int& probes) {
    Rank lo = 0, hi = std::ssize(s) - 1;      // closed interval [lo, hi]
    while (lo <= hi && s[lo] <= e && e <= s[hi]) {
        ++probes;
        if (s[lo] == s[hi]) return lo;        // all equal (and equal to e)
        double fraction = double(e - s[lo]) / double(s[hi] - s[lo]);
        Rank mi = lo + Rank(fraction * double(hi - lo));   // guess the position
        if (e < s[mi]) hi = mi - 1;
        else if (s[mi] < e) lo = mi + 1;
        else return mi;
    }
    return -1;
}

// Binary search (version A) with a probe counter, for comparison.
Rank binary_search(std::span<const long long> s, long long e, int& probes) {
    Rank lo = 0, hi = std::ssize(s);
    while (lo < hi) {
        ++probes;
        Rank mi = lo + (hi - lo) / 2;
        if (e < s[mi]) hi = mi;
        else if (s[mi] < e) lo = mi + 1;
        else return mi;
    }
    return -1;
}

int main() {
    const std::size_t n = 1'000'000, queries = 1000;
    auto a = std::make_unique<long long[]>(n);
    std::mt19937_64 rng(1);
    std::uniform_int_distribution<long long> value(0, 1'000'000'000'000LL);
    for (std::size_t i = 0; i < n; ++i) a[i] = value(rng);
    std::sort(a.get(), a.get() + n);
    std::span<const long long> s(a.get(), n);
    int p_interp = 0, p_binary = 0;
    for (std::size_t q = 0; q < queries; ++q) {
        long long e = s[rng() % n];           // a successful search
        if (s[interpolation_search(s, e, p_interp)] != e ||
            s[binary_search(s, e, p_binary)] != e) return 1;
    }
    std::cout << std::format("average probes: interpolation {:.2f}, binary {:.2f}\n",
                             double(p_interp) / queries, double(p_binary) / queries);
}
```

```python tab
import random

def interpolation_search(s: list[int], e: int, probes: list[int]) -> int:
    """Interpolation search on sorted numbers; probes[0] counts the probes."""
    lo, hi = 0, len(s) - 1             # closed interval [lo, hi]
    while lo <= hi and s[lo] <= e <= s[hi]:
        probes[0] += 1
        if s[lo] == s[hi]:             # all equal (and equal to e)
            return lo
        mi = lo + (e - s[lo]) * (hi - lo) // (s[hi] - s[lo])   # guess the position
        if e < s[mi]:
            hi = mi - 1
        elif s[mi] < e:
            lo = mi + 1
        else:
            return mi
    return -1

def binary_search(s: list[int], e: int, probes: list[int]) -> int:
    """Binary search (version A) with a probe counter, for comparison."""
    lo, hi = 0, len(s)
    while lo < hi:
        probes[0] += 1
        mi = (lo + hi) // 2
        if e < s[mi]:
            hi = mi
        elif s[mi] < e:
            lo = mi + 1
        else:
            return mi
    return -1

rng = random.Random(1)
n, queries = 1_000_000, 1000
s = sorted(rng.randint(0, 10**12) for _ in range(n))
p_interp, p_binary = [0], [0]
for _ in range(queries):
    e = s[rng.randrange(n)]            # a successful search
    assert s[interpolation_search(s, e, p_interp)] == e
    assert s[binary_search(s, e, p_binary)] == e
print(f"average probes: interpolation {p_interp[0] / queries:.2f}, "
      f"binary {p_binary[0] / queries:.2f}")
```

For 1000 successful searches among $10^6$ uniformly distributed random integers, interpolation search needs on average only a little over 4 probes, while binary search needs about 19. It can be shown (Yao and Yao, 1976; Perl, Itai and Avni, 1978) that for independent uniformly distributed data the average number of probes of interpolation search is $O(\log\log n)$: each probe shrinks the interval to be searched roughly from $n$ to $\sqrt n$. From another angle, the number of binary digits of the interval length (its effective word length), $\log n$, is halved each time, so interpolation search is "binary search on the word length", while binary search is "sequential search on the word length" (each step removes only one bit).

The drawbacks of interpolation search are also obvious. The worst case is $O(n)$: for example, when the data grow exponentially, every guess is biased toward one end and the interval shrinks by only one element each time. It needs multiplication and division, so its overhead beyond comparisons is larger; and the advantage of $O(\log\log n)$ over $O(\log n)$ is not significant at practical sizes ($\log_2 n = 32$ and $\log_2 \log_2 n = 5$ when $n = 2^{32}$), unless the table is extremely long or accessing one element is extremely expensive (for example on disk). A practical approach is a relay: first use interpolation search to narrow the range quickly, then switch to binary search, and finally switch to sequential search within a range of a hundred or two hundred elements.

## 2.5. Sorting

### 2.5.1. Bubble Sort

Sorting is the process of turning an unsorted vector into a sorted one. We first recall the simplest method, **bubble sort** ([4.1.7](/4.1.7)): in a sorted sequence every pair of adjacent elements is in order, while in an unsorted sequence there is always a pair of adjacent elements that is inverted. So we scan repeatedly: compare each pair of adjacent elements in turn and swap them if inverted, until after some scan we confirm that all adjacent elements are in order.

**Theorem 2.5.1** After $k$ scanning passes with swaps, the $k$ largest elements are necessarily in place, occupying the last $k$ positions of the vector in sorted order. Hence bubble sort necessarily terminates after at most $n - 1$ passes and gives the correct result.

**Proof** By induction on $k$. Pass $k$ involves only the first $n - k + 1$ elements; during the scan larger elements are swapped toward the back, and when the scan reaches the end, the largest among them (that is, the $k$-th largest overall) has necessarily been carried to position $n - k$. $\square$

The theorem says each pass reduces the problem size by one, but often not all $n - 1$ passes are needed: if a pass makes no swap, the vector is already sorted and we can stop early. Going further, if the last swap in a pass occurs at position $\mathit{last}$ (swapping $V[\mathit{last} - 1]$ and $V[\mathit{last}]$), then the suffix $V[\mathit{last}, \mathit{hi})$ has no inversions and its elements are all no smaller than those before it, so they are already in place, and the next pass needs to scan only up to $\mathit{last}$.

```cpp tab
#include <cstddef>
#include <format>
#include <iostream>
#include <span>
#include <utility>

// After each pass, a[last, hi) holds the largest elements in their final places.
template <typename T>
void bubble_sort(std::span<T> a) {
    for (std::size_t hi = a.size(), last; hi > 1; hi = last) {
        last = 0;                              // position of the last swap in this pass
        for (std::size_t i = 1; i < hi; ++i)
            if (a[i] < a[i - 1]) {             // an adjacent inversion
                std::swap(a[i - 1], a[i]);
                last = i;
            }
    }
}

int main() {
    int a[] = {5, 2, 7, 4, 6, 3, 1, 8, 9, 10};
    bubble_sort(std::span<int>(a));
    for (int x : a) std::cout << std::format("{} ", x);
    std::cout << '\n';
}
```

```python tab
def bubble_sort(a: list) -> None:
    """After each pass, a[last:hi] holds the largest elements in their final places."""
    hi = len(a)
    while hi > 1:
        last = 0                       # position of the last swap in this pass
        for i in range(1, hi):
            if a[i] < a[i - 1]:        # an adjacent inversion
                a[i - 1], a[i] = a[i], a[i - 1]
                last = i
        hi = last

a = [5, 2, 7, 4, 6, 3, 1, 8, 9, 10]
bubble_sort(a)
print(*a)
```

In the best case (the input is already sorted) one pass suffices, $O(n)$; in the worst case (completely reversed) $n - 1$ passes are needed, $\Theta(n^2)$.

**Definition 2.5.1 (Stable Sorting)** A sorting algorithm that always preserves the relative order of equal elements in the input sequence is called a **stable sorting** algorithm. For example, for the input $6, 7_a, 3, 2, 7_b, 1, 5, 8, 7_c, 4$, the output of a stable sort must be $1, 2, 3, 4, 5, 6, 7_a, 7_b, 7_c, 8$, whereas an unstable sort may output $\dots, 7_a, 7_c, 7_b, \dots$.

Stability matters when sorting by several keys: sort by the secondary key first, then stably sort by the primary key, and elements with equal primary keys remain ordered by the secondary key. Bubble sort is stable: only adjacent inverted elements are swapped, and equal elements are never swapped. If the comparison `a[i] < a[i-1]` is changed to `a[i] <= a[i-1]`, equal adjacent elements are swapped as well; the algorithm is still correct but no longer stable (and may do useless work).

### 2.5.2. Merge Sort

**Merge sort** ([4.1.11](/4.1.11)) was first programmed by von Neumann in 1945, and was the first sorting algorithm to achieve $O(n \log n)$ in the worst case: split the sequence into two halves ($O(1)$), sort the two subsequences recursively ($2T(n/2)$), and merge the sorted subsequences ($O(n)$).

Merging (two-way merge) repeatedly compares the first elements of two sorted sequences and moves the smaller one to the output. When implemented in a vector, one only needs to copy the left half $B = V[\mathit{lo}, \mathit{mi})$ into a buffer, while the right half $C = V[\mathit{mi}, \mathit{hi})$ can be read in place. The write position is $i = j + k$ ($j$ and $k$ are the numbers of elements already taken from $B$ and $C$), and the position of the next element to read in $C$ is $\mathit{mi} + k = \mathit{lb} + k$ (relative to $\mathit{lo}$, where $\mathit{lb}$ is the length of $B$). As long as $B$ is not exhausted ($j < \mathit{lb}$), we have $i < \mathit{lb} + k$, so a write never overwrites an unread element of $C$; and when $B$ is exhausted, the rest of $C$ is already in its correct place and need not be moved. So the buffer needs only $n/2$ cells, and can be shared among the recursive calls and allocated just once.

```cpp tab
#include <cstddef>
#include <format>
#include <functional>
#include <iostream>
#include <memory>
#include <span>
#include <string>
#include <utility>

// Merge the sorted runs a[0, mi) and a[mi, n). Only the left run is copied out:
// the right run is read in place, since the write position never overtakes it.
template <typename T, typename Less>
void merge(std::span<T> a, std::size_t mi, T* buf, Less less) {
    const std::size_t lb = mi, lc = a.size() - mi;
    for (std::size_t j = 0; j < lb; ++j) buf[j] = std::move(a[j]);   // B = a[0, mi)
    T* c = a.data() + mi;                                           // C = a[mi, n)
    std::size_t i = 0, j = 0, k = 0;
    while (j < lb && k < lc)                   // take from C only if strictly smaller:
        a[i++] = less(c[k], buf[j]) ? std::move(c[k++]) : std::move(buf[j++]);   // stable
    while (j < lb) a[i++] = std::move(buf[j++]);   // what is left of C is already in place
}

template <typename T, typename Less>
void merge_sort(std::span<T> a, T* buf, Less less) {
    if (a.size() < 2) return;
    std::size_t mi = a.size() / 2;
    merge_sort(a.first(mi), buf, less);
    merge_sort(a.subspan(mi), buf, less);
    merge(a, mi, buf, less);
}

template <typename T, typename Less = std::less<>>
void merge_sort(std::span<T> a, Less less = {}) {
    auto buf = std::make_unique<T[]>(a.size() / 2);   // one buffer of n/2 for all calls
    merge_sort(a, buf.get(), less);
}

int main() {
    // Sort by the number only; equal numbers keep their input order (stability).
    using Item = std::pair<int, std::string>;
    Item a[] = {{6, "a"}, {7, "a"}, {3, "a"}, {2, "a"}, {7, "b"},
                {1, "a"}, {5, "a"}, {8, "a"}, {7, "c"}, {4, "a"}};
    merge_sort(std::span<Item>(a), [](const auto& x, const auto& y) { return x.first < y.first; });
    for (const auto& [key, tag] : a) std::cout << std::format("{}{} ", key, tag);
    std::cout << '\n';                         // 1a 2a 3a 4a 5a 6a 7a 7b 7c 8a
}
```

```python tab
from collections.abc import Callable
from typing import Any

def merge(a: list, lo: int, mi: int, hi: int, key: Callable[[Any], Any]) -> None:
    """Merge the sorted runs a[lo:mi] and a[mi:hi]; only the left run is copied out."""
    b = a[lo:mi]                       # B = copy of the left run
    i, j, k = lo, 0, mi                # write position, read positions in B and in C
    while j < len(b) and k < hi:       # take from C only if strictly smaller: stable
        if key(a[k]) < key(b[j]):
            a[i] = a[k]
            k += 1
        else:
            a[i] = b[j]
            j += 1
        i += 1
    while j < len(b):                  # what is left of C is already in place
        a[i] = b[j]
        i, j = i + 1, j + 1

def merge_sort(a: list, lo: int = 0, hi: int | None = None,
               key: Callable[[Any], Any] = lambda x: x) -> None:
    if hi is None:
        hi = len(a)
    if hi - lo < 2:
        return
    mi = (lo + hi) // 2
    merge_sort(a, lo, mi, key)
    merge_sort(a, mi, hi, key)
    merge(a, lo, mi, hi, key)

# Sort by the number only; equal numbers keep their input order (stability).
a = [(6, "a"), (7, "a"), (3, "a"), (2, "a"), (7, "b"),
     (1, "a"), (5, "a"), (8, "a"), (7, "c"), (4, "a")]
merge_sort(a, key=lambda p: p[0])
print(" ".join(f"{k}{t}" for k, t in a))   # 1a 2a 3a 4a 5a 6a 7a 7b 7c 8a
```

When merging, $C$'s first element is taken only if it is strictly smaller than $B$'s first element, and when they are equal the left one from $B$ is taken, so merge sort is stable; the three 7s in the example keep the order $a, b, c$.

**Theorem 2.5.2** The time of a two-way merge is $O(\mathit{lb} + \mathit{lc})$; merge sort takes $O(n \log n)$ time and $O(n)$ space.

**Proof** In each iteration of the two merging loops, $i$ increases by one and one of $j$ and $k$ also increases by one. Since $0 \leq j \leq \mathit{lb}$ and $0 \leq k \leq \mathit{lc}$, the cumulative number of iterations is at most $\mathit{lb} + \mathit{lc}$. This holds even if the two subsequences differ greatly in length. Hence $T(n) = 2T(n/2) + O(n)$, and by the **master theorem** ([4.3.1](/4.3.1)) $T(n) = O(n \log n)$. The buffer is $n/2$ and the recursion depth is $O(\log n)$, so the total space is $O(n)$. $\square$

The advantages of merge sort are as follows: it is $O(n \log n)$ even in the worst case; it accesses data only sequentially and needs no random reads and writes, so it is especially suitable for lists ([4.3.3](/4.3.3)), tape-like devices, and external sorting of data exceeding memory (merging massive data); stability is guaranteed; and it parallelizes easily. Its drawbacks are that it needs auxiliary space comparable to the input size and is not an *in-place algorithm* (an in-place algorithm uses only $O(1)$ or $O(\log n)$ auxiliary space), and that even if the input is already sorted it still takes $\Theta(n \log n)$ time. One direction of improvement is to recognize runs already sorted in the input, which is just what Python's `list.sort` does (Timsort, using the merge policy of Powersort since 3.11); on partially sorted data it approaches linear time.

### 2.5.3. Lower Bound for Comparison Sorting

Is merge sort already optimal? In the model where information can be obtained only by comparing two elements, the answer is yes.

Any comparison-based sorting algorithm can be described by a *comparison tree*: each internal node is a comparison "$a_i < a_j$?", whose result sends us to the left or right subtree; each leaf corresponds to an output (a permutation of the input). The number of comparisons the algorithm performs on an input is the length of the path from the root to the corresponding leaf.

**Theorem 2.5.3 (Lower Bound for Comparison-Based Sorting)** Any comparison-based sorting algorithm needs at least $\lceil \log_2 n! \rceil = \Omega(n \log n)$ comparisons in the worst case.

**Proof** $n$ distinct elements have $n!$ permutations, and the algorithm must distinguish them: if two different permutations reached the same leaf, the algorithm would perform exactly the same data movement on both, and could not sort both. So the comparison tree has at least $n!$ leaves. A binary tree of height $h$ has at most $2^h$ leaves, so $2^h \geq n!$ and $h \geq \log_2 n!$. By the logarithmic series in [4.3.1](/4.3.1), $\log_2 n! = \Theta(n \log n)$. $\square$

The same argument also gives a lower bound for the average case: in a binary tree with $n!$ leaves, the average depth of a leaf is at least $\log_2 n!$. So merge sort is asymptotically optimal in the number of comparisons, and so is heapsort ([4.3.12](/4.3.12)). To break through this lower bound one must use information beyond comparisons, such as the numerical values of the keys themselves (bucket sort and radix sort, [4.3.9](/4.3.9)), just as interpolation search uses values to break through the $\log_2 n$ of binary search.

## 2.6. Bitmaps

### 2.6.1. Structure and Implementation

Many problems require maintaining a finite set of integers $S \subseteq [0, U)$, supporting testing $k \in S$, adding $k$ and deleting $k$. If $U$ is not too large, one can represent it with one binary bit per integer.

**Definition 2.6.1 (Bitmap)** The data structure that represents a set $S \subseteq [0, U)$ by a sequence of $U$ binary bits, where bit $k$ is 1 if and only if $k \in S$, is called a **bitmap** (also called a bit vector).

A bitmap is stored in $\lceil U/8 \rceil$ bytes: bit $k$ is bit $k \bmod 8$ (`k & 7`) of byte $\lfloor k/8 \rfloor$ (`k >> 3`). The **mask** `0x80 >> (k & 7)` selects that bit, and `test`, `set` and `clear` each need only one bit operation ([4.1.3](/4.1.3)), all $O(1)$.

```cpp tab
#include <cstddef>
#include <format>
#include <iostream>
#include <memory>

// A set of integers in [0, n), one bit per integer.
class Bitmap {
public:
    explicit Bitmap(std::size_t n)
        : bytes_((n + 7) / 8), m_(std::make_unique<unsigned char[]>(bytes_)) {}
    bool test(std::size_t k) const { return m_[k >> 3] & mask(k); }
    void set(std::size_t k) { m_[k >> 3] |= mask(k); }
    void clear(std::size_t k) { m_[k >> 3] &= static_cast<unsigned char>(~mask(k)); }

private:
    std::size_t bytes_;
    std::unique_ptr<unsigned char[]> m_;          // zero-initialized
    // Bit k lives in byte k / 8, at offset k % 8 counted from the high end.
    static unsigned char mask(std::size_t k) {
        return static_cast<unsigned char>(0x80 >> (k & 7));
    }
};

// Sieve of Eratosthenes on a bitmap: set bit k when k is known to be composite.
int main() {
    const std::size_t n = 100;
    Bitmap composite(n);
    for (std::size_t i = 2; i * i < n; ++i)
        if (!composite.test(i))
            for (std::size_t j = i * i; j < n; j += i) composite.set(j);
    for (std::size_t k = 2; k < n; ++k)
        if (!composite.test(k)) std::cout << std::format("{} ", k);
    std::cout << '\n';
}
```

```python tab
class Bitmap:
    """A set of integers in [0, n), one bit per integer."""

    def __init__(self, n: int) -> None:
        self._m = bytearray((n + 7) // 8)          # zero-initialized bytes

    @staticmethod
    def _mask(k: int) -> int:                      # offset k % 8 from the high end
        return 0x80 >> (k & 7)

    def test(self, k: int) -> bool:
        return bool(self._m[k >> 3] & self._mask(k))

    def set(self, k: int) -> None:
        self._m[k >> 3] |= self._mask(k)

    def clear(self, k: int) -> None:
        self._m[k >> 3] &= ~self._mask(k) & 0xFF

# Sieve of Eratosthenes on a bitmap: set bit k when k is known to be composite.
n = 100
composite = Bitmap(n)
i = 2
while i * i < n:
    if not composite.test(i):
        for j in range(i * i, n, i):
            composite.set(j)
    i += 1
print(*(k for k in range(2, n) if not composite.test(k)))
```

The main program implements the **sieve of Eratosthenes** ([4.1.6](/4.1.6)) with a bitmap: mark the multiples of each prime $i$ as composite; the outer loop needs to run only while $i^2 < n$, and the inner loop starts from $i^2$ (smaller multiples were already marked by smaller prime factors). The time is $O(n \log\log n)$: the inner loop executes about $n/p$ times for a prime $p$, and $\sum_{p \leq n} 1/p = \ln\ln n + O(1)$ (Mertens' theorem).

The C++ standard library's `std::bitset<N>` (length fixed at compile time) and `std::vector<bool>` (a specialization with bit-packed storage) are both bitmaps; Python has no built-in bitmap, but one can use a `bytearray` (as above) or treat an arbitrarily long `int` as a bit string.

### 2.6.2. Applications: Small Sets and Big Data

**Example 2.6.1** There are $n = 10^{10}$ 24-bit unsigned integers, from which we must remove the duplicates. If we imitate `uniquify()` by sorting first and then scanning, just storing the data requires at least $4n = 40\,\mathrm{GB}$ of memory, and frequent external-memory reads and writes also make it inefficient. Observe that the range of values $U = 2^{24}$ is far smaller than $n$, so there must be many duplicates: use a bitmap of $2^{24}$ bits, that is, $2\,\mathrm{MB}$, scan the data once and `set` each element, then scan the bitmap once and output all the bits equal to 1; the total time is $O(n + U)$ and the space is only $O(U)$. Even if $U = 2^{32}$, the bitmap is only $512\,\mathrm{MB}$. The key to such methods is to map the objects in the problem (query words, IP addresses, ...) to an integer set of modest range.

### 2.6.3. Fast Initialization

Constructing a bitmap requires clearing all $\lceil U/8 \rceil$ bytes, which takes $\Theta(U)$ time. In the example above this does not affect the asymptotic complexity, but that is not always so: if the data size $n$ is far smaller than $U$, or the same bitmap must be cleared repeatedly and only a few bits are used each time, the $\Theta(U)$ initialization becomes a bottleneck.

Aho, Hopcroft and Ullman (1974) gave a clever way to avoid initialization: use two integer arrays $F$, $T$ of length $U$ and a counter $\mathit{top}$ in place of the bitmap, where $T[0, \mathit{top})$ records in order the elements added to the set, and $F[k]$ records the position of element $k$ in $T$. Neither array is initialized; they may contain arbitrary old values. The test for $k \in S$ is that the two form a "validation cycle":

$$
0 \leq F[k] < \mathit{top} \quad \text{and} \quad T[F[k]] = k.
$$
If $k$ was never added, $F[k]$ is a garbage value; but even if it points into the valid part of $T$, the entry of $T$ at that position records another element, which cannot equal $k$, so garbage values cause no false positives. To add $k$: set $T[\mathit{top}] = k$ and $F[k] = \mathit{top}$, and increase $\mathit{top}$ by one. To delete $k$: move the last element $T[\mathit{top} - 1]$ of $T$ into the position $F[k]$ of $k$, update its $F$ value, and decrease $\mathit{top}$ by one. Clearing the whole set only requires setting $\mathit{top} = 0$. All operations are $O(1)$, at the cost of increasing the space to $2U$ integers.

This structure is nowadays often called a *sparse set*, generalized by Briggs and Torczon (1993) and used in places such as register allocation in compilers. Note that in C++ reading an uninitialized integer is **undefined behavior**, so a strictly conforming implementation needs the operating system to supply zeroed memory on demand (such as large `calloc` blocks), which in effect shifts the cost of initialization to the virtual memory system; in Python, creating a list itself requires initialization, so the trick is pointless.

## Summary

| Topic | Key points |
|---|---|
| Abstract data type | Data model + operations; separated from the implementation (the data structure) |
| Vector | Call-by-rank access $O(1)$; `insert(r)` is $O(n - r)$, `remove(lo, hi)` is $O(n - \mathit{hi})$ |
| Expansion | Capacity doubling: amortized $O(1)$, load factor $> 1/2$; incremental: amortized $\Theta(n)$; shrink threshold $1/4$ |
| Amortized vs. average | Amortized: total cost of a whole operation sequence, no probabilistic assumption; average: expectation over an input distribution |
| Unsorted vector | Search $O(n)$, deduplication $O(n^2)$ |
| Sorted vector | Uniquification $O(n)$ (two pointers); binary search $O(\log n)$, average comparisons: version A about $1.5\log_2 n$, Fibonacci about $1.44\log_2 n$, versions B/C about $\log_2 n$; interpolation search average $O(\log\log n)$ |
| Sorting | Bubble sort $O(n)$ to $O(n^2)$, stable; merge sort $\Theta(n \log n)$, stable, $O(n)$ auxiliary space; lower bound $\Omega(n \log n)$ for comparison sorting |
| Bitmap | Small-range integer sets, all operations $O(1)$; validation cycle avoids initialization |
