---
title: 向量
description: 抽象数据类型与数据结构；向量的接口与模板类实现；容量倍增与分摊分析，递增策略、缩容与装填因子，Python list 与 std::vector 的扩容；无序向量的插入、删除、查找、去重与遍历；有序向量的唯一化，二分查找的三个版本、Fibonacci 查找与插值查找；起泡排序与归并排序，排序的稳定性与比较排序的下界；位图与筛法。
---

数组是最基本的数据组织方式，但它的长度固定、接口简陋。本章把数组包装成一个抽象数据类型：向量。向量是第一个完整的数据结构，后面的栈、堆、散列表、图的邻接表都建立在它之上。本章有三条线索：一是接口与实现的分离（抽象数据类型），二是动态空间管理及其分析工具分摊分析，三是有序性的价值：向量一旦有序，查找就能从线性降到对数，去重也能从平方降到线性。[4.1.6](/4.1.6) 讲过数组与二分查找的用法，[4.2.10](/4.2.10) 讲过 `std::vector` 的用法；本章讲它们怎样实现、复杂度怎样证明。

## 2.1. 抽象数据类型与向量

### 2.1.1. 接口与实现

**定义 2.1.1（抽象数据类型）** 由一个数据模型和定义在该模型上的一组操作组成的类型称为**抽象数据类型**（abstract data type，ADT）。它只规定操作的语义（外部的逻辑特性），不涉及数据的存储方式，也不考虑操作的复杂度。在某种语言中实现一个抽象数据类型的一整套存储方式与算法，称为它的一种数据结构；同一个抽象数据类型可以有多种实现，复杂度各不相同。

抽象数据类型在数据结构的实现者与使用者之间规定了分工的接口：实现者负责高效地兑现各个操作（造冰箱、造汽车），使用者只需按照接口使用（用冰箱、开汽车）。这正是**数据抽象**与**封装**（[4.2.1](/4.2.1)、[4.2.3](/4.2.3)）：同一套接口只需实现一次，各种算法与数据结构可以方便地组合，代码更短、更安全，复用程度更高。C++ 中用类**模板**表达抽象数据类型，Python 中用类表达。

### 2.1.2. 从数组到向量

C/C++ 的数组 `A[0, n)` 中，元素与编号一一对应，每个元素都可以由编号直接访问：若每个元素占 $s$ 个字节，则 `A[i]` 的地址为 $A + i \cdot s$，访问只需 $O(1)$ 时间。

**定义 2.1.2（向量）** 由一组元素按线性次序封装而成的序列称为**向量**（vector）：$n$ 个元素与 $[0, n)$ 中的整数一一对应，元素 $V[r]$ 前面恰有 $r$ 个元素，$r$ 称为它的秩（rank）。通过秩直接访问元素的方式称为循秩访问（call-by-rank）。

向量是数组的抽象与泛化：元素的类型可以灵活选取（可以是另一个复杂的数据结构），长度可以动态变化，操作和管理更统一、更安全。向量的抽象数据类型提供以下接口：

| 操作 | 功能 | 适用对象 |
|---|---|---|
| `size()` / `empty()` | 元素总数 / 是否为空 | 向量 |
| `V[r]` | 读写秩为 $r$ 的元素 | 向量 |
| `insert(r, e)` / `insert(e)` | 把 $e$ 作为秩为 $r$ 的元素 / 末元素插入 | 向量 |
| `remove(lo, hi)` / `remove(r)` | 删除区间 $[\mathit{lo}, \mathit{hi})$ 内的元素 / 秩为 $r$ 的元素 | 向量 |
| `disordered()` / `sort()` | 统计逆序的相邻元素对 / 排序 | 向量 |
| `find(e)` / `search(e)` | 查找 $e$ | 向量 / 有序向量 |
| `dedup()` / `uniquify()` | 剔除重复的元素 | 向量 / 有序向量 |
| `traverse(visit)` | 遍历，对每个元素执行 `visit` | 向量 |

这些接口沿用邓俊辉教材的命名，与 C++ 标准库的对应关系是：`insert(e)` 相当于 `push_back`，`remove` 相当于 `erase`，`find` 与 `search` 相当于 `std::find` 与 `std::upper_bound`，`uniquify` 相当于 `std::unique` 加 `erase`。

## 2.2. 可扩充向量

### 2.2.1. 动态空间管理

向量内部用一段地址连续的存储区 `elem` 存放元素，记录元素个数 `size` 与存储区的容量 `capacity`。若容量固定（静态空间管理），则有明显的不足：存储区可能不足以存放所有元素，造成上溢（overflow），尽管此时系统往往还有足够的空间；也可能其中的元素寥寥无几，造成浪费。$\lambda = \mathit{size}/\mathit{capacity}$ 称为装填因子（load factor），它衡量空间的利用率。一般的应用中很难预先准确地估计所需的空间。

动态空间管理的思路像蝉蜕壳：存储区即将上溢时，申请一块更大的存储区，把原有元素复制过去，再释放原来的存储区。关键的问题是新的容量取多大。

**算法 2.2.1（容量倍增）** 插入元素之前，若向量已满（$\mathit{size} = \mathit{capacity}$），则申请容量为原来 2 倍的存储区，把元素逐一移入，再释放原存储区。

下面是向量的核心部分。C++ 版本用 `std::unique_ptr<T[]>` 管理存储区（**RAII**，[4.2.4](/4.2.4)），释放由它自动完成，不会出现**悬垂指针**；秩用有符号的 `std::ptrdiff_t`，以便用 $-1$ 表示失败。Python 没有定长数组，这里用 `[None] * c` 模拟一块有 $c$ 个槽位的存储区，只按下标读写，不调用列表自己的 `append` 与 `insert`。

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

程序依次插入 40 个元素，再逐个删除，输出容量的变化：插入第 5、9、17、33 个元素时，容量依次从 4 倍增到 8、16、32、64；删除到只剩 15、7、3 个元素时，容量依次减半（缩容见 2.2.3 节）。

插入 `insert(r, e)` 要把后缀 $[r, n)$ 自后向前依次后移一个单元，再放入新元素，时间为 $O(n - r)$；后移必须自后向前，否则会覆盖尚未移动的元素。区间删除 `remove(lo, hi)` 把后缀 $[\mathit{hi}, n)$ 整体前移 $\mathit{hi} - \mathit{lo}$ 个单元，时间为 $O(n - \mathit{hi})$，前移必须自前向后。单元素删除只是区间删除的特例 $[r, r+1)$。反过来，若用反复调用 `remove(r)` 来实现区间删除，每次都要移动整个后缀，总时间为 $O((\mathit{hi} - \mathit{lo})(n - \mathit{hi}))$，最坏可达 $O(n^2)$；所以区间删除是基本操作，单元素删除由它派生。

### 2.2.2. 分摊分析

单看一次插入，最坏情况下要复制全部 $n$ 个元素，需要 $O(n)$ 时间。但扩容很少发生：刚扩容之后，至少还要再插入 $n$ 个元素才会再次扩容。只看单次操作的最坏情况会严重高估总成本，需要另一种分析方法。

**定义 2.2.1（分摊分析）** 对数据结构连续实施足够多次的操作，把总成本分摊到每一次操作上：若对任意长度为 $m$ 的操作序列，总成本都不超过 $m \cdot f(n)$，则称每次操作的分摊成本为 $O(f(n))$。这种分析方法称为**分摊分析**（也称摊还分析），所得的复杂度称为分摊复杂度。

**定义 2.2.2（平均分析）** 根据各种输入或操作出现的概率分布，把对应的成本加权平均，这种分析方法称为**平均分析**，所得的复杂度称为平均复杂度（期望复杂度）。

两者的区别在于：平均分析把各次操作视为独立事件，需要对输入作概率假设，割裂了操作之间的相关性；分摊分析考察实际可能出现的操作序列的总体成本，不需要任何概率假设，所得的是对最坏情况的保证（只是保证的对象是整个序列，而不是单次操作）。分析数据结构时，分摊分析往往更忠实地刻画了真实的性能。分摊分析的三种标准方法（聚合、记账、势能）见 [4.3.4](/4.3.4)，这里先用最直接的聚合法：算出整个序列的总成本，再除以操作次数。

**定理 2.2.1** 从容量为 $c_0 \geq 1$ 的空向量开始连续插入 $n$ 个元素。若采用容量倍增策略，扩容所需的复制总时间为 $O(n)$，每次插入的分摊时间为 $O(1)$；若采用容量递增策略（每次扩容增加固定的 $I$ 个单元），复制总时间为 $\Theta(n^2/I)$，每次插入的分摊时间为 $\Theta(n/I)$。

**证明** 倍增：扩容发生在元素个数达到 $c_0, 2c_0, 4c_0, \dots$ 时，最后一次扩容时的元素个数小于 $n$。各次复制的元素个数构成几何级数，总和由末项主导：

$$
c_0 + 2c_0 + 4c_0 + \cdots + 2^k c_0 < 2 \cdot 2^k c_0 < 2n,
$$
加上 $n$ 次写入，总时间不超过 $3n$。递增：扩容发生在元素个数达到 $I, 2I, 3I, \dots$ 时，共约 $m = n/I$ 次，复制的元素个数构成算术级数：

$$
I + 2I + \cdots + (m-1)I = I \cdot \frac{m(m-1)}{2} = \Theta(n^2 / I). \qquad \square
$$

下图左边比较两种策略的总成本，右边是倍增策略下每次插入的实际成本：大部分插入只需 1 个单位，偶尔有一次代价很高，但累计的平均始终不超过 3。

![左：容量递增（每次 64）与倍增的总成本；右：倍增策略下每次插入的实际成本与平均成本](./plots/expansion-strategies.py)

更一般地，若扩容时容量乘以常数 $r > 1$，复制总量不超过 $n \cdot \frac{r}{r-1}$，分摊时间仍是 $O(1)$，代价是装填因子可能低至 $1/r$：

| 策略 | 累计扩容时间 | 分摊扩容时间 | 装填因子 |
|---|---|---|---|
| 递增 $I$ | $\Theta(n^2/I)$ | $\Theta(n/I)$ | $\approx 100\%$ |
| 倍增 | $\Theta(n)$ | $O(1)$ | $> 50\%$ |
| 乘以 $r > 1$ | $\Theta(n)$，常数约 $\frac{r}{r-1}$ | $O(1)$ | $> 1/r$ |

"以空间换时间"在这里只付出了常数倍的代价：倍增策略浪费的空间不超过一半，却把扩容的成本从平方降到了线性。

### 2.2.3. 缩容

删除使装填因子下降。若规定装填因子低于某个阈值时把容量减半，阈值不能取 $1/2$：设容量为 $2c$、元素恰有 $c + 1$ 个，交替地删除与插入，每次删除都使装填因子降到 $1/2$ 以下而缩容到 $c$，每次插入又使向量满而扩容到 $2c$，每次操作都要复制约 $c$ 个元素。

上面的实现在装填因子低于 $1/4$ 时才把容量减半。每次重新分配之后，装填因子都约为 $1/2$：扩容后元素数约为新容量 $C$ 的一半；缩容前元素数不足旧容量的 $1/4$，即约为新容量 $C$ 的一半。从这个状态出发，下一次重新分配若是扩容，至少要再插入约 $C/2$ 个元素，复制约 $C$ 个；若是缩容，至少要再删除约 $C/4$ 个元素，复制不足 $C/4$ 个。无论哪种情况，复制的元素数都不超过这期间操作次数的常数倍（约 2 倍），所以插入与删除任意交替时，每次操作的分摊时间仍是 $O(1)$。

### 2.2.4. Python 的 list 与 C++ 的 vector

CPython 的 `list` 就是一个动态数组：对象内部是一个指向元素指针数组的指针，加上元素个数和已分配的容量。CPython 3.12 的扩容规则大致是：需要容纳 $m$ 个元素时，新容量取 $m + \lfloor m/8 \rfloor + 6$，再向下取整到 4 的倍数；元素个数降到容量的一半以下时缩容。因此 `append` 时容量依次为 $4, 8, 16, 24, 32, 40, 52, 64, 76, 92, \dots$，增长因子约为 $1.125$。按上一节的公式，复制总量约为 $9n$，分摊时间仍是 $O(1)$；由于数组中存放的只是 8 字节的指针，而且底层的 `realloc` 常常能就地扩展，实际代价很小。

| 操作 | 复杂度 |
|---|---|
| `a[i]`、`a[i] = x`、`len(a)` | $O(1)$ |
| `a.append(x)`、`a.pop()` | 分摊 $O(1)$ |
| `a.insert(i, x)`、`a.pop(i)`、`del a[i]` | $O(n - i)$ |
| `x in a`、`a.index(x)`、`a.count(x)` | $O(n)$ |
| `a[i:j]`（切片复制） | $O(j - i)$ |
| `a.sort()`、`sorted(a)` | $O(n \log n)$ |

所以在列表头部反复插入或删除（`insert(0, x)`、`pop(0)`）是 $O(n)$ 的，应改用 `collections.deque`（[4.3.4](/4.3.4)）。

C++ 的 `std::vector` 与本章的 `Vector` 结构相同（[4.2.10](/4.2.10)）：`size()` 达到 `capacity()` 时，libstdc++ 与 libc++ 把容量加倍，MSVC 乘以 1.5。增长因子取小于黄金比 $\phi \approx 1.618$ 的值有一个好处：此前释放的若干块旧存储区之和最终能大于新的请求，内存分配器有机会重用它们，而倍增时新块总比此前释放的所有块之和还大。`std::vector` 从不自动缩容；`reserve(n)` 预先分配容量，避免多次扩容；`shrink_to_fit()` 请求释放多余的容量（标准不保证照办）。

## 2.3. 无序向量

### 2.3.1. 查找

无序向量只支持判等，查找只能逐个比较。下面的 `find` 在区间 $[\mathit{lo}, \mathit{hi})$ 内自后向前查找，返回等于 $e$ 的元素中秩最大者；失败时返回 $\mathit{lo} - 1$，这是一个合法区间之外的、明确表示失败的值，调用者可以据此判断。这些成员函数与上一节的类定义放在一起使用。

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

最好情况下（末元素即为 $e$）只需 $O(1)$ 时间，最坏情况（查找失败或 $e$ 在首位）需要 $O(n)$ 时间，二者有实质的差别。这种复杂度依赖于输入的具体情况、而不仅是规模的算法，称为输入敏感（input-sensitive）的算法。

元素需要支持判等（`==`、`!=`）；后面的有序向量还需要比较（`<`）。若元素是"关键码—数值"对（词条），判等与比较只看关键码：被判为相等的词条未必相同。在 C++20 中可以为词条类定义 `operator==` 与 `operator<=>`（**三路比较运算符**），在 Python 中定义 `__eq__` 与 `__lt__`（**特殊方法**）。

### 2.3.2. 去重

`dedup()` 剔除无序向量中重复的元素，每组相等的元素只保留第一个。

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

正确性来自一个**循环不变式**：前缀 $[0, i)$ 中的元素互不相同。初始 $i = 1$ 时显然成立；每轮考察 $V[i]$，若它不在前缀中出现，则保留它、$i$ 加一，否则删除它，不变式都保持。每轮要么 $i$ 加一，要么规模减一，所以至多 $n$ 轮后终止。每轮中 `find` 与 `remove` 的时间之和为 $O(i) + O(n - i) = O(n)$，总时间为 $O(n^2)$。先排序再用下一节的 `uniquify()`，可以改进到 $O(n \log n)$；用散列表（[4.3.9](/4.3.9)）可以做到期望 $O(n)$。

### 2.3.3. 遍历

遍历对向量中的每个元素统一执行某个操作 `visit`。C 的写法是传入函数指针；更灵活的是传入**函数对象**或 **lambda 表达式**（[4.2.12](/4.2.12)），它们可以携带状态（如累加器），也便于编译器内联。

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

例如 `v.traverse([](int& x) { x *= 10; })` 把每个元素乘以 10，`v.traverse([&sum](int x) { sum += x; })` 求和。C++ 版本把 `visit` 声明为转发引用 `Visit&&`，可以接受任何可调用对象。Python 的 `visit` 拿到的是元素的引用，对不可变对象（如整数）无法就地修改，只能读取。

## 2.4. 有序向量

### 2.4.1. 有序性

**定义 2.4.1（有序向量）** 若向量中所有元素都按非降次序排列，即对任意 $0 < r < n$ 都有 $V[r-1] \leq V[r]$，则称之为**有序向量**。

有序向量中任何一对相邻元素都是顺序的；反过来，逆序的相邻元素对的数目，可以在一定程度上度量向量的紊乱程度。`disordered()` 统计这一数目，返回 0 当且仅当向量有序。

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

无序向量经过预处理（排序）转换为有序向量之后，许多算法都可以优化。

### 2.4.2. 唯一化

有序向量中相等的元素必然紧邻。一种直接的做法是：从前向后扫描，若当前元素与前一个相等，就删除它。这种做法每次删除都要移动后缀，当大量元素相等时总时间为 $O(n^2)$：勤奋而低效。

更好的做法是不删除，而是把每组相等元素中的第一个直接移到前面去，最后一次性截去尾部。用两个下标：$i$ 指向已确定的不重复前缀的末元素，$j$ 向后扫描；遇到与 $V[i]$ 不同的元素就把它移到 $V[i + 1]$。这种做法称为双指针法（two-pointer technique）。

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

不变式：$V[0..i]$ 由 $V[0..j)$ 中的不同元素按原次序组成，且 $V[i]$ 是其中最大者。$j$ 每轮加一，每个元素至多移动一次，总时间为 $O(n)$。

### 2.4.3. 二分查找（版本 A）

有序向量中，任一元素 $x = V[\mathit{mi}]$ 都把查找区间 $[\mathit{lo}, \mathit{hi})$ 分为三部分：$[\mathit{lo}, \mathit{mi})$ 中的元素都不大于 $x$，$(\mathit{mi}, \mathit{hi})$ 中的都不小于 $x$。所以只需把目标 $e$ 与 $x$ 比较一次，就能把问题缩小：$e < x$ 时深入左侧，$x < e$ 时深入右侧，$e = x$ 时命中。这就是**二分查找**（[4.1.6](/4.1.6)）的减治思想。

**算法 2.4.1（二分查找，版本 A）** 取 $\mathit{mi}$ 为区间的中点，按上述三种情况分别处理，直到命中或区间为空。

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

（同一程序中还有下一节的 Fibonacci 查找。）每经过至多两次比较，要么命中，要么区间缩短一半，故 $T(n) = T(n/2) + O(1) = O(\log n)$，远远优于顺序查找。

更精细的度量是关键码的比较次数。注意版本 A 中转向左、右两个分支的代价不同：先比较 `e < s[mi]`，成立则转向左侧，只需 1 次比较；否则再比较 `s[mi] < e`，转向右侧或命中都需 2 次。在等概率的假设下，查找成功（失败）时比较次数的平均值称为成功（失败）的平均查找长度。以 $n = 7$ 为例，7 种成功情况的比较次数依次为 $4, 3, 5, 2, 5, 4, 6$，平均 $29/7 \approx 4.14$；8 种失败情况平均 $36/8 = 4.5$。一般地，版本 A 的平均查找长度约为 $1.5 \log_2 n$：每深入一层，平均需要 $1.5$ 次比较。

### 2.4.4. Fibonacci 查找

版本 A 中，转向左侧的代价（1 次比较）低于转向右侧（2 次），而两侧的递归深度相同。若让左侧更长、右侧更短，用递归深度的不均衡来补偿转向成本的不均衡，平均查找长度应能进一步缩短。

**算法 2.4.2（Fibonacci 查找）** 设查找区间的长度为 $F_k - 1$（$F_k$ 为 Fibonacci 数），取轴点 $\mathit{mi} = \mathit{lo} + F_{k-1} - 1$，则左、右两个子区间的长度分别为 $F_{k-1} - 1$ 与 $F_{k-2} - 1$，仍然具有同样的形式；比较的方式与版本 A 相同。长度不是 $F_k - 1$ 的形式时，每步取不超过区间长度的最大 Fibonacci 数 $F$，令 $\mathit{mi} = \mathit{lo} + F - 1$。

上面的 `fib_search` 不需要预先制作 Fibonacci 数表：$(f, g) = (F_k, F_{k-1})$ 可以就地前进为 $(F_{k+1}, F_k)$，也可以就地后退为 $(F_{k-1}, F_{k-2})$。后退的总次数不超过 $O(\log n)$，所以确定轴点的分摊代价是 $O(1)$。$n = 7$ 时，Fibonacci 查找成功的平均查找长度为 $28/7 = 4$，失败的为 $35/8 \approx 4.38$，都略优于版本 A。

为什么是 Fibonacci 数？考虑一般的策略：总是在区间长度的 $\lambda$ 处取轴点（$0 < \lambda < 1$；二分查找 $\lambda = 1/2$）。设成功的平均比较次数为 $\alpha(\lambda) \log_2 n$，按转向左（概率约 $\lambda$，1 次比较）、转向右（概率约 $1 - \lambda$，2 次比较）列出递推：

$$
\alpha \log_2 n = \lambda\bigl(1 + \alpha \log_2(\lambda n)\bigr) + (1 - \lambda)\bigl(2 + \alpha \log_2((1-\lambda) n)\bigr),
$$
整理得

$$
\alpha(\lambda) = \frac{\lambda - 2}{\lambda \log_2 \lambda + (1 - \lambda) \log_2(1 - \lambda)}.
$$
$\alpha(1/2) = 1.5$，而 $\alpha(\lambda)$ 在 $\lambda = \phi - 1 = \frac{\sqrt5 - 1}{2} \approx 0.618$ 处取最小值约 $1.44$：这正是 Fibonacci 查找的分割比例。

### 2.4.5. 二分查找（版本 B 与版本 C）

转向成本的不平衡也可以直接消除：每次迭代只做一次比较，只有两个分支。

**算法 2.4.3（二分查找，版本 B）** 取中点 $\mathit{mi}$，若 $e < V[\mathit{mi}]$ 则深入 $[\mathit{lo}, \mathit{mi})$，否则深入 $[\mathit{mi}, \mathit{hi})$；直到区间长度为 1，才判断是否命中。

与版本 A 相比，版本 B 即使在中途遇到 $e$ 也不会提前返回，所以最好情况变差、最坏情况变好，整体性能更加均衡：任何查找都恰好需要约 $\log_2 n$ 次比较。

版本 B 还有一个缺点：失败时只返回 $-1$，有多个命中元素时不能保证返回哪一个。而为了维护有序向量，`search` 需要更多的信息。例如插入新元素 $e$ 时，希望写成 `V.insert(V.search(e) + 1, e)`：即使查找失败，也要给出新元素可以安置的位置（有序性）；若已有相等的元素，新元素应排在它们之后（稳定性，见 2.5.1 节）。为此约定：`search(e)` 总是返回不大于 $e$ 的最后一个元素的秩 $m$（不存在时为 $\mathit{lo} - 1$）。

**算法 2.4.4（二分查找，版本 C）** 取中点 $\mathit{mi}$，若 $e < V[\mathit{mi}]$ 则 $\mathit{hi} \gets \mathit{mi}$，否则 $\mathit{lo} \gets \mathit{mi} + 1$；直到区间为空，返回 $\mathit{lo} - 1$。

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

版本 C 与版本 B 只有两处不同：$e \geq V[\mathit{mi}]$ 时深入 $(\mathit{mi}, \mathit{hi})$ 而不是 $[\mathit{mi}, \mathit{hi})$，因而区间长度可以缩短到 0；以及返回值。$V[\mathit{mi}]$ 被排除出区间，会不会被遗漏？下面的定理说明不会。

**定理 2.4.1** 版本 C 返回的 $m$ 满足 $V[0, m] \leq e < V[m+1, n)$，即 $m$ 是不大于 $e$ 的最后一个元素的秩。

**证明** 证明循环不变式 $V[0, \mathit{lo}) \leq e < V[\mathit{hi}, n)$（区间中的每个元素分别 $\leq e$ 和 $> e$）。初始 $\mathit{lo} = 0$、$\mathit{hi} = n$，两个区间都为空，自然成立。设某次迭代前不变式成立。若 $e < V[\mathit{mi}]$，由有序性 $V[\mathit{mi}, n)$ 中的元素都 $\geq V[\mathit{mi}] > e$，令 $\mathit{hi} = \mathit{mi}$ 后不变式成立；否则 $V[\mathit{mi}] \leq e$，$V[0, \mathit{mi}]$ 中的元素都 $\leq V[\mathit{mi}] \leq e$，令 $\mathit{lo} = \mathit{mi} + 1$ 后不变式也成立。每次迭代区间长度 $\mathit{hi} - \mathit{lo}$ 严格减小，循环必然终止，此时 $\mathit{lo} = \mathit{hi}$，不变式即为 $V[0, \mathit{lo}) \leq e < V[\mathit{lo}, n)$，返回 $m = \mathit{lo} - 1$ 正合所求。$\square$

版本 C 每步一次比较，共 $\lceil \log_2(n+1) \rceil$ 次左右；要判断是否命中，调用者再比较一次 $V[m] = e$。下图比较三种算法成功查找的平均比较次数：随 $\log_2 n$ 线性增长，斜率分别约为 $1.5$、$1.44$ 和 $1$。

![二分查找的版本 A、C 与 Fibonacci 查找成功时的平均比较次数（n 取 Fibonacci 数减一）](./plots/search-lengths.py)

版本 C 的返回值在标准库中对应 `std::upper_bound(first, last, e) - 1` 与 Python 的 `bisect.bisect_right(a, e) - 1`（[4.1.6](/4.1.6)）。2.2 节的 `Vector` 类中的 `search` 成员就是版本 C：

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

### 2.4.6. 插值查找

二分查找只利用了元素之间的大小关系，没有利用元素的数值。查英文词典时，没有人从中间翻起：binary 大约在 $2/26$ 处，search 大约在 $19/26$ 处。若元素大致服从均匀分布，区间 $[\mathit{lo}, \mathit{hi}]$ 内的元素应大致呈线性增长，就可以按数值猜测轴点的位置。

**算法 2.4.5（插值查找）** 在闭区间 $[\mathit{lo}, \mathit{hi}]$ 内，取轴点

$$
\mathit{mi} = \mathit{lo} + \left\lfloor \frac{e - V[\mathit{lo}]}{V[\mathit{hi}] - V[\mathit{lo}]} \,(\mathit{hi} - \mathit{lo}) \right\rfloor,
$$
其余与版本 A 相同；$e$ 落在 $[V[\mathit{lo}], V[\mathit{hi}]]$ 之外时直接判定失败。

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

在 $10^6$ 个均匀分布的随机整数中做 1000 次成功查找，插值查找平均只需 4 次多探测，二分查找约需 19 次。可以证明（Yao 与 Yao，1976；Perl、Itai 与 Avni，1978），对独立均匀分布的数据，插值查找的平均探测次数为 $O(\log\log n)$：每探测一次，待查找区间的长度大致从 $n$ 缩小到 $\sqrt n$。换一个角度看：区间长度的二进制位数（有效字长）$\log n$ 每次减半，所以插值查找是"在字长意义上的二分查找"，而二分查找是"在字长意义上的顺序查找"（每次只减少一位）。

插值查找的缺点也很明显。最坏情况是 $O(n)$：例如数据按指数增长时，每次猜测都偏向一端，区间每次只缩短一个元素。它需要做乘法和除法，比较之外的开销较大；从 $O(\log n)$ 到 $O(\log\log n)$ 的优势在实际规模下并不显著（$n = 2^{32}$ 时 $\log_2 n = 32$，$\log_2 \log_2 n = 5$），除非查找表极长或访问一次元素的代价极高（例如在磁盘上）。实用的办法是接力：先用插值查找迅速缩小范围，再改用二分查找，最后在一两百个元素的范围内改用顺序查找。

## 2.5. 排序

### 2.5.1. 起泡排序

排序是把无序向量转化为有序向量的过程。先回顾最简单的**起泡排序**（[4.1.7](/4.1.7)）：在有序序列中任何一对相邻元素都是顺序的，在无序序列中总有一对相邻元素是逆序的。于是反复扫描：依次比较每一对相邻元素，若逆序则交换，直到某趟扫描后确认相邻元素均已顺序。

**定理 2.5.1** 经过 $k$ 趟扫描交换后，最大的 $k$ 个元素必然就位，位于向量的末尾 $k$ 个位置并且有序。因此至多 $n - 1$ 趟后起泡排序必然终止，并给出正确的结果。

**证明** 对 $k$ 归纳。第 $k$ 趟扫描只涉及前 $n - k + 1$ 个元素；扫描中较大的元素一路被交换到后面，扫描到达末尾时，其中的最大者（即全体中第 $k$ 大的元素）必定被带到位置 $n - k$。$\square$

定理说明每趟扫描后问题规模缩减一，但往往不必做满 $n - 1$ 趟：若某趟扫描没有发生交换，向量已经有序，可以提前终止。进一步，若某趟扫描中最后一次交换发生在位置 $\mathit{last}$（交换了 $V[\mathit{last} - 1]$ 与 $V[\mathit{last}]$），则后缀 $V[\mathit{last}, \mathit{hi})$ 中没有逆序对，并且其中的元素都不小于前面的元素，已经就位，下一趟只需扫描到 $\mathit{last}$。

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

最好情况（输入已经有序）只需一趟扫描，$O(n)$；最坏情况（完全逆序）需要 $n - 1$ 趟，$\Theta(n^2)$。

**定义 2.5.1（稳定排序）** 若排序算法总能保持相等元素在输入序列中的相对次序，则称之为**稳定排序**。例如输入 $6, 7_a, 3, 2, 7_b, 1, 5, 8, 7_c, 4$，稳定排序的输出必为 $1, 2, 3, 4, 5, 6, 7_a, 7_b, 7_c, 8$，而不稳定的排序可能输出 $\dots, 7_a, 7_c, 7_b, \dots$。

稳定性在按多个关键码排序时很重要：先按次要关键码排序，再按主要关键码稳定排序，主要关键码相同的元素仍按次要关键码排列。起泡排序是稳定的：只有相邻的逆序元素才会交换，相等的元素从不交换。若把比较条件 `a[i] < a[i-1]` 改为 `a[i] <= a[i-1]`，相等的相邻元素也会交换，算法仍然正确，但不再稳定（而且可能做无用功）。

### 2.5.2. 归并排序

**归并排序**（[4.1.11](/4.1.11)）由 von Neumann 于 1945 年首次编程实现，它是第一个在最坏情况下达到 $O(n \log n)$ 的排序算法：把序列一分为二（$O(1)$），两个子序列递归排序（$2T(n/2)$），再把有序子序列合并（$O(n)$）。

合并（二路归并）反复比较两个有序序列的首元素，把小者移入输出。在向量中实现时，只需把左半段 $B = V[\mathit{lo}, \mathit{mi})$ 复制到缓冲区，右半段 $C = V[\mathit{mi}, \mathit{hi})$ 可以就地读取：写入位置 $i = j + k$（$j$、$k$ 分别是 $B$、$C$ 中已取出的元素个数），而 $C$ 中下一个待读元素的位置是 $\mathit{mi} + k = \mathit{lb} + k$（相对于 $\mathit{lo}$，$\mathit{lb}$ 是 $B$ 的长度）。只要 $B$ 尚未取完（$j < \mathit{lb}$），就有 $i < \mathit{lb} + k$，写入永远不会覆盖 $C$ 中尚未读取的元素；而 $B$ 取完时，$C$ 的剩余部分已经在正确的位置上，无需移动。于是缓冲区只需 $n/2$ 个单元，并且可以在各次递归调用之间共用，只分配一次。

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

合并时，只有 $C$ 的首元素严格小于 $B$ 的首元素才取 $C$，相等时取左边的 $B$，所以归并排序是稳定的；示例中的三个 7 保持了 $a, b, c$ 的次序。

**定理 2.5.2** 二路归并的时间为 $O(\mathit{lb} + \mathit{lc})$；归并排序的时间为 $O(n \log n)$，空间为 $O(n)$。

**证明** 合并的两个循环每迭代一步，$i$ 都递增一，$j$ 或 $k$ 之一也随之递增一。因 $0 \leq j \leq \mathit{lb}$、$0 \leq k \leq \mathit{lc}$，累计迭代步数不超过 $\mathit{lb} + \mathit{lc}$。即使两个子序列的长度相差悬殊，这一结论依然成立。于是 $T(n) = 2T(n/2) + O(n)$，由**主定理**（[4.3.1](/4.3.1)）得 $T(n) = O(n \log n)$。缓冲区 $n/2$，递归深度 $O(\log n)$，总空间 $O(n)$。$\square$

归并排序的优点是：最坏情况下也是 $O(n \log n)$；只顺序访问数据，不需要随机读写，因此特别适用于列表（[4.3.3](/4.3.3)）、磁带一类的设备，以及数据量超过内存的外部排序（海量数据的归并）；可以保证稳定；易于并行化。缺点是需要与输入规模相当的辅助空间，不是就地算法（in-place algorithm）：就地算法只使用 $O(1)$ 或 $O(\log n)$ 的辅助空间；而且即使输入已经有序，仍需 $\Theta(n \log n)$ 时间。改进的方向之一是识别输入中已经有序的段，这正是 Python 的 `list.sort`（Timsort，3.11 起采用 Powersort 的合并策略）的做法，它对部分有序的数据接近线性时间。

### 2.5.3. 比较排序的下界

归并排序是否已经最优？在只能通过比较两个元素来获取信息的模型下，答案是肯定的。

任何基于比较的排序算法都可以用一棵比较树（comparison tree）描述：每个内部节点是一次比较 "$a_i < a_j$?"，按结果走向左或右子树；每个叶节点对应一种输出（输入的一个排列）。算法对某个输入执行的比较次数，就是从根到相应叶节点的路径长度。

**定理 2.5.3（基于比较的排序的下界）** 任何基于比较的排序算法，在最坏情况下至少需要 $\lceil \log_2 n! \rceil = \Omega(n \log n)$ 次比较。

**证明** $n$ 个互不相同的元素有 $n!$ 种排列，算法必须把它们区分开：两个不同的排列若到达同一个叶节点，算法对二者执行完全相同的数据移动，不可能把两者都排好。所以比较树至少有 $n!$ 个叶节点。高度为 $h$ 的二叉树至多有 $2^h$ 个叶节点，故 $2^h \geq n!$，$h \geq \log_2 n!$。由 [4.3.1](/4.3.1) 的对数级数，$\log_2 n! = \Theta(n \log n)$。$\square$

同样的论证也给出平均情况的下界：$n!$ 个叶节点的二叉树，叶节点的平均深度至少为 $\log_2 n!$。所以归并排序在比较次数的意义上是渐近最优的，堆排序（[4.3.12](/4.3.12)）也是。要突破这一下界，必须利用比较之外的信息，例如关键码的数值本身（桶排序与基数排序，[4.3.9](/4.3.9)），正如插值查找利用数值突破了二分查找的 $\log_2 n$。

## 2.6. 位图

### 2.6.1. 结构与实现

很多问题需要维护一个有限整数集合 $S \subseteq [0, U)$，支持判断 $k \in S$、加入 $k$、删除 $k$。若 $U$ 不太大，可以用每个整数一个二进制位来表示。

**定义 2.6.1（位图）** 用长度为 $U$ 的二进制位序列表示集合 $S \subseteq [0, U)$、第 $k$ 位为 1 当且仅当 $k \in S$ 的数据结构称为**位图**（bitmap，也称位向量）。

位图存放在 $\lceil U/8 \rceil$ 个字节中：第 $k$ 位位于第 $\lfloor k/8 \rfloor$ 个字节（`k >> 3`）的第 $k \bmod 8$ 位（`k & 7`）。用**掩码** `0x80 >> (k & 7)` 选出这一位，`test`、`set`、`clear` 各只需一次位运算（[4.1.3](/4.1.3)），都是 $O(1)$。

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

主程序用位图实现 **Eratosthenes 筛法**（[4.1.6](/4.1.6)）：把每个质数 $i$ 的倍数标记为合数，外循环只需进行到 $i^2 < n$，内循环从 $i^2$ 开始（更小的倍数已被更小的质因数标记过）。时间为 $O(n \log\log n)$：内循环对质数 $p$ 执行约 $n/p$ 次，而 $\sum_{p \leq n} 1/p = \ln\ln n + O(1)$（Mertens 定理）。

C++ 标准库的 `std::bitset<N>`（长度在编译期确定）与 `std::vector<bool>`（按位压缩存储的特化）都是位图；Python 没有内置的位图，可以用 `bytearray`（如上）或把一个任意长的 `int` 当作位串使用。

### 2.6.2. 应用：小集合与大数据

**例 2.6.1** 有 $n = 10^{10}$ 个 24 位无符号整数，剔除其中重复的元素。若仿照 `uniquify()` 先排序再扫描，仅存放数据就需要至少 $4n = 40\,\mathrm{GB}$ 内存，频繁的外存读写也会导致效率低下。注意到取值范围 $U = 2^{24}$ 远小于 $n$，元素必有大量重复：用一个 $2^{24}$ 位、即 $2\,\mathrm{MB}$ 的位图，扫描一遍数据，对每个元素 `set`，再扫描一遍位图输出所有为 1 的位，总时间 $O(n + U)$，空间只需 $O(U)$。即使 $U = 2^{32}$，位图也只有 $512\,\mathrm{MB}$。这类方法的关键在于把问题中的对象（查询词、IP 地址……）映射为某个范围不大的整数集合。

### 2.6.3. 快速初始化

构造位图时要把全部 $\lceil U/8 \rceil$ 个字节清零，这需要 $\Theta(U)$ 时间。在上面的例子中这不影响渐近复杂度，但并非总是如此：若数据规模 $n$ 远小于 $U$，或者同一个位图要反复清空、每次只用到少数几位，$\Theta(U)$ 的初始化就会成为瓶颈。

Aho、Hopcroft 与 Ullman（1974）给出了一个巧妙的办法，可以省去初始化：用两个长度为 $U$ 的整数数组 $F$、$T$ 和一个计数器 $\mathit{top}$ 代替位图，其中 $T[0, \mathit{top})$ 依次记录已加入集合的元素，$F[k]$ 记录元素 $k$ 在 $T$ 中的位置。两个数组都不初始化，里面可能是任意的旧值。判断 $k \in S$ 的条件是两者构成一个"校验环"：

$$
0 \leq F[k] < \mathit{top} \quad \text{且} \quad T[F[k]] = k.
$$
若 $k$ 从未加入，$F[k]$ 是垃圾值；但只要它指向 $T$ 的有效部分，$T$ 中那个位置记录的就是另一个元素，不会等于 $k$，所以垃圾值不会造成误判。加入 $k$：$T[\mathit{top}] = k$，$F[k] = \mathit{top}$，$\mathit{top}$ 加一。删除 $k$：把 $T$ 的末元素 $T[\mathit{top} - 1]$ 移到 $k$ 的位置 $F[k]$ 上，并更新它的 $F$ 值，再令 $\mathit{top}$ 减一。清空整个集合只需令 $\mathit{top} = 0$。所有操作都是 $O(1)$，代价是空间增加到 $2U$ 个整数。

这一结构今天常称为稀疏集合（sparse set），由 Briggs 与 Torczon（1993）推广，用于编译器的寄存器分配等场合。要注意，在 C++ 中读取未初始化的整数是**未定义行为**，严格合规的实现需要由操作系统按需提供清零的内存（如大块的 `calloc`），这实际上把初始化的代价转嫁给了虚拟内存系统；在 Python 中创建列表本身就需要初始化，这一技巧没有意义。

## 小结

| 主题 | 要点 |
|---|---|
| 抽象数据类型 | 数据模型 + 操作；与实现（数据结构）分离 |
| 向量 | 循秩访问 $O(1)$；`insert(r)` 为 $O(n - r)$，`remove(lo, hi)` 为 $O(n - \mathit{hi})$ |
| 扩容 | 容量倍增：分摊 $O(1)$，装填因子 $> 1/2$；递增：分摊 $\Theta(n)$；缩容阈值取 $1/4$ |
| 分摊与平均 | 分摊：整个操作序列的总成本，不需要概率假设；平均：对输入分布取期望 |
| 无序向量 | 查找 $O(n)$、去重 $O(n^2)$ |
| 有序向量 | 唯一化 $O(n)$（双指针）；二分查找 $O(\log n)$，平均比较次数：版本 A 约 $1.5\log_2 n$，Fibonacci 约 $1.44\log_2 n$，版本 B/C 约 $\log_2 n$；插值查找平均 $O(\log\log n)$ |
| 排序 | 起泡 $O(n)$ 至 $O(n^2)$，稳定；归并 $\Theta(n \log n)$，稳定，需 $O(n)$ 辅助空间；比较排序的下界 $\Omega(n \log n)$ |
| 位图 | 小范围整数集合，各操作 $O(1)$；校验环可省去初始化 |
