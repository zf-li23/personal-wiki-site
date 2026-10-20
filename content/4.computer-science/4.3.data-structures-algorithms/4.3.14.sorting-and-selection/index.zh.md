---
title: 排序与选取
description: 快速排序的轴点与四种划分（LUG、DUP、LGU、三路）；递归深度、随机化与期望比较次数的分析；内省排序；选取问题：多数元素、两个有序向量的中位数、基于堆的选取、快速选取与线性时间选取；希尔排序的增量序列与 Shell、PS、Pratt、Sedgewick 序列的复杂度。
---

排序是算法课程中被研究得最透彻的问题，前面几章已经陆续讲过起泡、选择、插入、归并、堆和锦标赛排序。本章先回到**快速排序**：它的基本思想与实现已在 [4.1.11](/4.1.11) 中讲过，这里关心的是划分的几种写法及其在相等元素面前的表现、递归深度与辅助空间，以及随机化之后的期望比较次数。随后讨论与排序密切相关的选取问题：不必全排序，怎样找出第 $k$ 小的元素、中位数或多数元素？快速排序的划分思想给出期望线性时间的快速选取，再加上"中位数的中位数"就得到最坏情况下也是线性时间的选取算法。最后讨论希尔排序，它的分析把排序的代价与逆序对、数论中的线性组合联系在一起，至今仍有未解决的问题。基于比较的排序的 $\Omega(n \log n)$ 下界见定理 2.5.3，散列与桶排序等不基于比较的方法见 [4.3.9](/4.3.9)。

## 14.1. 快速排序：轴点与划分

### 14.1.1. 轴点

**分治**的归并排序难在"合"，快速排序则难在"分"：把序列划分为前后两部分，使前缀中的元素都不大于后缀中的元素，两部分各自递归排序之后，原序列便自然有序。划分围绕一个特殊的元素进行。

**定义 14.1.1（轴点）** 若序列中某个元素不小于它左侧的所有元素、不大于它右侧的所有元素，则称它为该序列的**轴点**。

轴点必定已经就位：它在排序后的序列中所处的位置就是它现在的位置（反之不然）。进一步，一个序列有序，当且仅当其中所有元素都是轴点，所以快速排序就是把所有元素逐个转化为轴点的过程。坏消息是，一个序列中未必有轴点：例如有序序列循环移位一次后（`2 3 4 5 1`），没有任何元素在原位，因此也没有轴点。好消息是，只需不多的交换，就能让任一元素成为轴点。问题是怎样交换、代价多高。下面的四种划分方法都把一个随机选取的候选者（下称"轴点"）放到它的正确位置上，[4.1.11](/4.1.11) 中的"双向扫描"就是第一种。

### 14.1.2. LUG 版：勤于拓展、懒于交换

任取一个候选者（例如把随机选中的元素换到首位），把它暂存起来，首位就留下一个"空位"。序列分为三段：前缀 $L$ 中的元素都不大于轴点，后缀 $G$ 中的元素都不小于轴点，中间的 $U$ 尚未考查。交替地从右端向左拓展 $G$、从左端向右拓展 $L$：从右向左扫描时，不小于轴点的元素留在原地，遇到更小者就把它移到左端的空位，空位随之转到右端；从左向右扫描时同理。当两端相遇时 $U$ 为空，把轴点放进最后的空位，它就成了名副其实的轴点。

- 每个元素至多移动一次（候选者两次），累计 $O(n)$ 时间，只需 $O(1)$ 附加空间（就地）。
- 不稳定：两端的扫描方向相反，相等的元素可能前后颠倒。

### 14.1.3. 相等元素：DUP 版

LUG 版的扫描把与轴点相等的元素都留在原地。若序列中有大量与轴点相等的元素，它们全部停留在 $G$ 中（或 $L$ 中），划分点将接近端点，划分极度失衡：递归深度接近 $n$，运行时间接近 $\Theta(n^2)$。尴尬的是，当所有元素都相等时，序列其实已经有序，根本不需要排序。

只需把两个扫描循环的条件由"不小于（不大于）则继续"改为"大于（小于）才继续"：扫描遇到与轴点相等的元素就停下，把它移到另一端。这样，连续的相等元素会被交替地分到两侧，$\mathit{lo}$ 和 $\mathit{hi}$ 交替移动，划分点接近区间的中点。由"勤于拓展、懒于交换"转为"懒于拓展、勤于交换"，交换操作有所增加，也更不稳定，但对一般的输入复杂度并没有实质增加。注意扫描必须写成"先移动一步、再检查"（`do`–`while`）的形式，否则两端都停在相等元素上时会原地打转。

### 14.1.4. LGU 版：单向扫描

另一种思路是从左向右单向扫描，维护三段：$L = A(\mathit{lo}, \mathit{mi}]$ 中的元素小于轴点，$G = A(\mathit{mi}, k)$ 中的元素不小于轴点，$U = A[k, \mathit{hi})$ 尚未考查，轴点暂存于 $A[\mathit{lo}]$。考查 $A[k]$：若它不小于轴点，直接把 $G$ 向右拓展一位（$k$ 加 1）；否则把它与 $G$ 的首元素 $A[\mathit{mi}+1]$ 交换，相当于 $L$ 向右拓展一位、$G$ 整体"滚动"后移一位。扫描结束后交换 $A[\mathit{lo}]$ 与 $A[\mathit{mi}]$，轴点归位，得到 $A[\mathit{lo}, \mathit{mi}) < A[\mathit{mi}] \le A(\mathit{mi}, \mathit{hi})$。这种写法（N. Lomuto）最简洁，也最容易证明正确；它的缺点是交换次数较多，而且所有与轴点相等的元素都归入 $G$，与 LUG 版一样会在大量相等元素上退化。它的单向扫描方式也正好适用于下面的快速选取。

### 14.1.5. 三路划分

处理相等元素最彻底的办法是三路划分（three-way partitioning）：把序列分成小于、等于、大于轴点的三段。E. W. Dijkstra 以"荷兰国旗问题"的名义提出了一种单趟算法：维护 $A[\mathit{lo}, \mathit{lt})$ 小于轴点、$A[\mathit{lt}, i)$ 等于轴点、$A[\mathit{gt}, \mathit{hi})$ 大于轴点，$A[i, \mathit{gt})$ 尚未考查；考查 $A[i]$ 时，小于轴点则与 $A[\mathit{lt}]$ 交换、两个指针都前进，大于轴点则与 $A[\mathit{gt}-1]$ 交换、$\mathit{gt}$ 后退，等于则 $i$ 前进。划分之后中间一段已经全部就位，只需递归处理两端。所有元素都相等时，一趟划分就结束了；一般地，若输入中只有 $d$ 种不同的关键码，三路快速排序的期望时间为 $O(n \log d)$ 量级，在常数因子之内是最优的（Sedgewick 与 Bentley）。代价是每个元素可能要做两次比较；J. Bentley 与 M. D. McIlroy（1993）的写法把相等的元素先换到两端，划分结束后再换回中间，减少了这一开销。

下面的实现把四种划分写成返回"轴点所在区间"$[l, g)$ 的函数，供同一个快速排序框架调用：两路划分返回 $[\mathit{mi}, \mathit{mi}+1)$，三路划分返回等于轴点的那一段。排序时只对较短的一侧递归、对较长的一侧继续循环，原因见 14.2.1 节。

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

下图统计了输入只有 $d$ 种不同关键码时四种划分的比较次数。LUG 与 LGU 在相等元素很多时退化为平方时间（$d = 1$ 时比较次数是 $n \log_2 n$ 的约 50 倍）；DUP 在任何 $d$ 下都保持 $n \log n$ 量级；三路划分在 $d$ 较小时最快，关键码互不相同时则因每个元素两次比较而稍慢。

![四种划分在相等元素较多时的比较次数：LUG 与 LGU 在 d 很小时退化为平方时间，DUP 与三路划分保持 n log n 量级](./plots/duplicate-keys.py)

## 14.2. 快速排序：性能分析

### 14.2.1. 递归深度与辅助空间

快速排序的辅助空间就是递归的深度。最好情况下每次划分都均衡，深度为 $O(\log n)$；最坏情况下每次划分都偏向一侧，深度为 $\Theta(n)$，在规模很大时足以导致栈溢出。时间与空间的最坏情况可以分开处理：无论划分是否均衡，都可以把递归深度控制在 $O(\log n)$。

**定理 14.2.1** 若每次划分之后只对较短的一侧递归、对较长的一侧在本层继续迭代，则递归深度不超过 $\log_2 n$。

**证明** 每进入一层递归，处理的子区间的长度都不超过上一层区间长度的一半（较短的一侧不超过一半），而长度为 1 的区间不再递归，所以递归至多 $\log_2 n$ 层。$\square$

这一技巧等价于手工消除尾递归。也可以完全不用递归，而用一个显式的栈保存待排序的子区间：每次划分之后，较长的子区间先入栈、较短的后入栈，使较短的先被处理，栈的规模同样不超过 $O(\log n)$（可对 $n$ 归纳证明）。注意这只控制空间，不改变时间：最坏情况下仍有 $\Theta(n)$ 次失衡的划分，总时间 $\Theta(n^2)$。

### 14.2.2. 随机化与递归深度

最好情况下每次划分都接近平均，轴点总是接近中央，时间为 $O(n \log n)$，达到下界；最坏情况下每次划分都极不均衡（比如轴点总是最小或最大的元素），时间为 $\Theta(n^2)$，与起泡排序为伍。随机选取轴点、三者取中等策略只能降低最坏情况的概率，而不能杜绝它。既然如此，为何还称作"快速"排序？因为最坏情况的概率极低，而且不依赖于输入：对任何输入，只要随机数是真正随机的，算法都以压倒性的概率快速完成。

把轴点落在区间中间一半（秩在 $[n/4, 3n/4]$ 之间）称为"好轴点"，随机选取时概率约为 $1/2$。好轴点使两侧都不超过原长的 $3/4$。采用三者取中（随机取三个元素，以其中位数为轴点），好轴点的概率提高为

$$
1 - 2\left[\binom{3}{2}\left(\frac14\right)^2 \frac34 + \left(\frac14\right)^3\right] = 1 - \frac{20}{64} = \frac{11}{16} \approx 0.69.
$$

**定理 14.2.2** 随机选取轴点时，快速排序的递归深度以至少 $1 - n^{-2}$ 的概率不超过 $8 \log_{4/3} n = O(\log n)$。

**证明** 固定一个元素 $x$，考查包含 $x$ 的子区间所经历的划分序列。每遇到一个好轴点，包含 $x$ 的子区间长度至多变为原来的 $3/4$，所以这条路径上至多有 $k = \log_{4/3} n$ 个好轴点。在每一层，轴点是好轴点的条件概率约为 $1/2$，且各层的随机选择相互独立，所以路径长度超过 $L = 8k$ 意味着在 $L$ 次独立试验中成功不到 $k$ 次。由 Chernoff 界，记成功次数为 $X$，$\mathbb{E}[X] = L/2 = 4k$，

$$
\mathbb{P}(X < k) = \mathbb{P}\bigl(X < (1 - \tfrac34)\,\mathbb{E}[X]\bigr) \le \exp\!\left(-\frac{(3/4)^2 \cdot 4k}{2}\right) = \mathrm{e}^{-9k/8} = n^{-9/(8 \ln(4/3))} < n^{-3}.
$$

对全部 $n$ 个元素取并，递归深度超过 $L$ 的概率小于 $n \cdot n^{-3} = n^{-2}$。$\square$

定理中的常数是为了证明方便而取的，实际的期望递归深度约为 $4.31 \ln n \approx 2.99 \log_2 n$（Devroye，1986）。直观地说，除非轴点过于偏侧，每一次划分都会有效地缩短递归路径，好轴点在每一层都以常数概率出现，而只要出现 $O(\log n)$ 个，递归就必然终止。

### 14.2.3. 期望比较次数

设输入的 $n$ 个元素互不相同，轴点均匀随机地选取。记期望的比较次数为 $T(n)$。一次划分需要 $n - 1$ 次比较，轴点的秩等可能地为 $0, 1, \dots, n-1$，于是

$$
T(n) = (n - 1) + \frac{1}{n}\sum_{k=0}^{n-1}\bigl[T(k) + T(n - k - 1)\bigr] = (n - 1) + \frac{2}{n}\sum_{k=0}^{n-1} T(k).
$$

两边乘以 $n$，再与 $n - 1$ 时的同一等式相减，可以消去求和，解得下面的结论。这里给出另一种更有启发性的证明。

**定理 14.2.3** 随机轴点的快速排序对 $n$ 个互不相同的元素，期望比较次数为

$$
T(n) = 2(n + 1)H_n - 4n \approx 2n \ln n \approx 1.386\, n \log_2 n,
$$
其中 $H_n = 1 + \frac12 + \cdots + \frac1n$ 是调和数。

**证明**（后向分析）设排序后的输出序列为 $s_0 < s_1 < \cdots < s_{n-1}$。这一输出与具体使用何种算法无关，所以可以倒过来，从输出出发分析算法的过程。比较只发生在轴点与其他元素之间，任何一对元素至多比较一次（比较之后轴点就位，不再参与后续比较），所以期望的比较次数等于每一对 $(s_i, s_j)$ 在排序过程中被比较的概率之和。

快速排序的过程可以理解为把所有元素逐个转化为轴点。对 $i < j$，考查 $s_i, s_{i+1}, \dots, s_j$ 这 $j - i + 1$ 个元素：在它们之中的某个元素被选为轴点之前，它们始终位于同一个子区间中；其他元素早于或晚于它们被转化，都与 $s_i$、$s_j$ 是否比较无关。若其中第一个被选为轴点的是 $s_i$ 或 $s_j$，二者就会比较；若是介于二者之间的某个 $s_k$，二者就被分到两侧，再也不会比较。由于轴点是均匀随机选取的，这 $j - i + 1$ 个元素中的每一个率先被选中的概率相等，所以

$$
\mathbb{P}(s_i \text{ 与 } s_j \text{ 比较}) = \frac{2}{j - i + 1}.
$$

求和，令 $d = j - i$：

$$
T(n) = \sum_{d=1}^{n-1} (n - d)\,\frac{2}{d + 1} = \sum_{k=2}^{n} \frac{2(n + 1 - k)}{k} = 2(n + 1)(H_n - 1) - 2(n - 1) = 2(n+1)H_n - 4n. \qquad \square
$$

因为 $H_n = \ln n + O(1)$，期望的比较次数约为 $2 n \ln n \approx 1.386\, n \log_2 n$，比下界 $\log_2 n! \approx n \log_2 n - 1.44n$ 多出约 39%。采用三者取中后，期望的比较次数降为约 $\frac{12}{7} n \ln n \approx 1.188\, n \log_2 n$。下图比较了三种 $O(n \log n)$ 排序算法在随机排列上的实测比较次数：

![随机排列上的比较次数：归并排序最接近下界 log2 n!，快速排序约为 2 ln n，堆排序约为 2 log2 n](./plots/comparison-counts.py)

### 14.2.4. 实际中的快速排序

比较次数并不是全部。下表从几个角度比较向量上的各种排序算法：

| 算法 | 比较次数 | 元素移动 | 附加空间 | 稳定 | 访存局部性 |
|---|---|---|---|---|---|
| 插入排序 | $O(n)$ 至 $O(n^2)$ | $O(n)$ 至 $O(n^2)$ | $O(1)$ | 是 | 好 |
| 选择排序 | $\Theta(n^2)$ | $O(n)$ | $O(1)$ | 否 | 好 |
| 堆排序 | 约 $2n \log_2 n$ | 约 $n \log_2 n$ | $O(1)$ | 否 | 差：父子的秩相差一倍 |
| 归并排序 | 约 $n \log_2 n$ | 约 $n \log_2 n$ 至 $2n\log_2 n$ | $O(n)$ | 是 | 好：顺序访问 |
| 快速排序 | 期望约 $1.39\, n \log_2 n$ | 期望约 $0.69\, n \log_2 n$ | 期望 $O(\log n)$ | 否 | 很好：轴点常驻寄存器 |

快速排序的比较次数不是最少的，但它的内层循环极其简单，元素移动少，扫描是顺序的，对缓存非常友好，所以实际中通常最快。工业级的实现在此基础上做了几项改进：

- 内省排序（D. R. Musser，1997）：以快速排序为主，记录递归深度，超过 $2 \log_2 n$ 时改用堆排序（[4.3.12](/4.3.12)），从而保证最坏 $O(n \log n)$；区间很短（如十几个元素）时停止递归，最后用插入排序收尾。C++ 的 `std::sort` 在主流标准库中都采用这一框架，轴点取首、中、尾三者的中位数，大规模时取九者的中位数。
- 模式消除快速排序（pdqsort，O. Peters，2021）：在内省排序的基础上识别已经有序或逆序的输入、在划分明显失衡时打乱元素以破坏对手构造的输入，并用三路划分的思想处理大量相等元素。Go 从 1.19 起的 `sort` 包采用它；Rust 的不稳定排序最初采用它，1.81 起换成了在其基础上改进的 ipnsort。
- Python 不采用快速排序：`list.sort` 与 `sorted` 要求稳定，并且在实际数据中经常遇到部分有序的输入，所以使用自适应的归并排序 Timsort（T. Peters，2002），3.11 起其合并次序改用 Powersort 的策略（J. I. Munro 与 S. Wild，2018）。比较在 Python 中代价很高（每次都要调用对象的 `__lt__`），而 Timsort 在部分有序的输入上所需的比较次数远少于 $n \log_2 n$。

## 14.3. 选取

### 14.3.1. 选取问题与中位数

**定义 14.3.1（选取问题）** 在任意一组可以比较大小的元素中，找出按非降次序排列后秩为 $k$（$0 \le k < n$）的元素，即非降序列 $s_0 \le s_1 \le \cdots \le s_{n-1}$ 中的 $s_k$，称为 $k$-选取问题，统称**选取问题**。

**中位数**是选取的一个特例：本章约定长度为 $n$ 的有序序列中秩为 $\lfloor n/2 \rfloor$ 的元素为中位数（$n$ 为偶数时取两个中间元素中较大的一个，与它相等者也都是中位数）。电子表格中的 `LARGE(range, k)` 与 `MEDIAN(range)` 就是这两个问题。稍后将看到，中位数也是选取问题中难度最大的情形。

蛮力的方法是先排序、再取出秩为 $k$ 者，需要 $O(n \log n)$ 时间。另一方面，任何选取算法都至少需要 $\Omega(n)$ 时间：第 $k$ 小是相对于序列整体而言的，在访问每个元素至少一次之前，绝无可能确定它（未访问的元素可能是任何值）。问题是能否在 $O(n)$ 时间内完成。

### 14.3.2. 多数元素

先看一个相关的问题。

**定义 14.3.2（多数元素）** 若无序向量中有一半以上的元素都等于 $m$，则称 $m$ 为它的**多数元素**（课件中称为众数，注意不要与统计中出现次数最多的"众数"混淆）。

例如 `5 3 9 3 1 3 3` 中多数元素为 3，而 `5 3 9 3 1 3` 中没有多数元素（3 恰占一半）。平凡的算法是排序后扫描，$O(n \log n)$ 时间。若要求只用 $O(n)$ 时间和 $O(1)$ 附加空间呢？一个必要条件是：多数元素若存在，则必是中位数（它占据了排序后一半以上的位置，必然覆盖中间的位置）。所以只要能在线性时间内找出中位数，再花 $O(n)$ 时间验证它出现的次数，就解决了这个问题。不过在高效的中位数算法出现之前，可以借助一个功能更弱、但计算成本更低的必要条件，选出唯一的候选者。

**定理 14.3.1** 若向量 $A$ 的某个偶数长度的前缀 $P$ 中，元素 $x$ 出现的次数恰好是 $\lvert P \rvert / 2$，则：$A$ 有多数元素，仅当后缀 $A \setminus P$ 有多数元素 $m$，且 $m$ 就是 $A$ 的多数元素。

**证明** 设 $A$ 有多数元素 $m$，记 $c(y)$ 为 $y$ 出现的次数，$m$ 在 $A$ 中出现 $c(m) > \lvert A \rvert / 2$ 次。若 $x = m$，去掉 $P$ 后 $m$ 与其他元素在数量上的差距保持不变（$P$ 中二者各占一半）；若 $x \ne m$，则 $m$ 在 $P$ 中至多出现 $\lvert P \rvert / 2$ 次，去掉 $P$ 后 $m$ 与其他元素的差距不会缩小。两种情况下 $m$ 在后缀中仍然超过半数。$\square$

于是可以减而治之：自左向右扫描，维护候选者 `cand` 与计数器 `count`；计数器为零时以当前元素为新的候选者，否则遇到候选者则计数加一、遇到其他元素则减一。计数器每次归零，都恰好切下一个满足定理条件的前缀。扫描结束时的候选者是唯一可能的多数元素，最后再扫描一遍验证。这就是 Boyer 与 Moore（1981）的多数投票算法（majority vote algorithm）：两趟扫描，$O(n)$ 时间，$O(1)$ 空间。

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

若把多数元素的标准从"一半以上"改为"至少一半"，这个算法就不再适用，例如 `1 2` 中两个元素都恰占一半。推广到找出所有出现超过 $n/k$ 次的元素，可以同时维护 $k - 1$ 个候选者（Misra 与 Gries，1982），它也是数据流算法中频繁项统计的基础。

### 14.3.3. 两个有序向量的中位数

给定两个有序向量 $S_1$、$S_2$，长度分别为 $n_1$、$n_2$，要找出它们合并之后的中位数。蛮力的方法是二路归并后取中间元素，需要 $O(n_1 + n_2)$ 时间，但毕竟未能充分利用两个向量各自的有序性。

先看 $n_1 = n_2 = n$ 的情形，仍采用减而治之。比较两者各自的中位数 $m_1 = S_1[\lfloor n/2 \rfloor]$ 与 $m_2 = S_2[\lfloor (n-1)/2 \rfloor]$：若 $m_1 = m_2$，则它们同为 $S_1$、$S_2$ 和 $S_1 \cup S_2$ 的中位数；若 $m_1 < m_2$，则 $S_1$ 中 $m_1$ 左侧的元素与 $S_2$ 中 $m_2$ 右侧的元素都不可能是合并后的中位数，而且两侧删去的元素一样多，于是删去这两部分（各约一半）之后，中位数不变；$m_1 > m_2$ 时同理。每一步规模减半，共需 $O(\log n)$ 时间。

一般的 $n_1 \ne n_2$ 可以类似地处理，但边界情况繁琐。更简洁的是直接求合并后秩为 $k$ 的元素：设合并后的前 $k + 1$ 个元素中有 $i$ 个来自 $S_1$、$j = k + 1 - i$ 个来自 $S_2$，正确的 $i$ 是满足 $S_1[i] \ge S_2[j - 1]$ 的最小者，而这个条件关于 $i$ 是单调的，可以二分查找。对较短的向量二分，时间为 $O(\log \min(n_1, n_2))$。可见，等长的情形实际上才是难度最大的。

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

### 14.3.4. 基于堆的选取

优先级队列（[4.3.12](/4.3.12)）给出了几种不同的思路：

| 方法 | 做法 | 时间 |
|---|---|---|
| 小顶堆 | 把所有元素建成小顶堆（$O(n)$），连续执行 $k + 1$ 次 `delMin` | $O(n + k \log n)$ |
| 大小为 $k + 1$ 的大顶堆 | 任取 $k + 1$ 个元素建成大顶堆；对其余每个元素，插入后再删除堆顶；最后的堆顶即为所求 | $O(k + (n - k)\log k)$ |
| 两个堆 | 把输入任意划分为大小为 $k$ 与 $n - k$ 的两部分，分别建成大顶堆 $L$ 与小顶堆 $G$；只要 $L$ 的堆顶大于 $G$ 的堆顶，就交换二者并各自下滤；最后 $G$ 的堆顶即为所求 | $O(n + \min(k, n - k)\log n)$ |

当 $k$ 很小或很接近 $n$ 时，这些方法都接近线性；但对中位数（$k \approx n/2$），它们都需要 $\Theta(n \log n)$ 时间。C++ 的 `std::partial_sort` 和 Python 的 `heapq.nsmallest` 就是第二种方法，适合"前 $k$ 名"这类 $k \ll n$ 的需求。

### 14.3.5. 快速选取

快速排序的划分给出了另一种思路：对整个向量做一次划分，轴点就位于秩 $\mathit{mi}$。若 $\mathit{mi} = k$，轴点就是所求；若 $\mathit{mi} < k$，所求的元素必在轴点右侧，剪除前缀；若 $\mathit{mi} > k$，剪除后缀。只需在一侧继续，直到猜中为止（C. A. R. Hoare，1961）。

**算法 14.3.1（快速选取）** 令 $[\mathit{lo}, \mathit{hi}) = [0, n)$。反复执行：在 $[\mathit{lo}, \mathit{hi})$ 中随机选取轴点做 LGU 划分，得到轴点的秩 $\mathit{mi}$；若 $\mathit{mi} < k$ 则令 $\mathit{lo} \gets \mathit{mi} + 1$，若 $\mathit{mi} > k$ 则令 $\mathit{hi} \gets \mathit{mi}$，否则返回 $A[\mathit{mi}]$。

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

与快速排序一样，大量相等的元素会使 LGU 划分退化，此时应改用三路划分：当 $k$ 落在等于轴点的一段中时立即返回。

**定理 14.3.2** 随机轴点的快速选取，对任何 $k$，期望比较次数不超过 $4n$。

**证明** 记 $T(n)$ 为规模为 $n$ 时对最坏的 $k$ 的期望比较次数。一次划分需要 $n - 1$ 次比较，轴点的秩等可能地为 $0, \dots, n-1$，剩下的一侧至多为 $\max(i, n - 1 - i)$，所以

$$
T(n) \le (n - 1) + \frac{1}{n} \sum_{i=0}^{n-1} T\bigl(\max(i, n - 1 - i)\bigr).
$$
对 $n$ 归纳，设 $T(m) \le 4m$ 对 $m < n$ 成立。由于 $\sum_{i=0}^{n-1} \max(i, n-1-i) \le \frac{3}{4}n^2$，

$$
T(n) \le (n - 1) + \frac{4}{n}\cdot\frac{3n^2}{4} < n + 3n = 4n. \qquad \square
$$

更精确的分析表明，对中位数期望约需 $2(1 + \ln 2)n \approx 3.39n$ 次比较，$k$ 越接近两端越少。但快速选取的最坏情况仍是 $\Theta(n^2)$：轴点每次都选到一侧的极端。

### 14.3.6. 线性时间选取

能否在最坏情况下也做到线性时间？关键是保证每次划分都能剪除一定比例的元素，即找到一个"足够好"的轴点。M. Blum、R. W. Floyd、V. Pratt、R. L. Rivest 与 R. E. Tarjan（1973）的办法是：用递归求出的"中位数的中位数"作为轴点。

**算法 14.3.2（线性时间选取）** 设 $Q$ 为一个小常数（如 $Q = 5$）。对 $A$ 和秩 $k$：

0. 若 $n = \lvert A \rvert$ 不超过某个常数，直接排序后返回秩为 $k$ 者；
1. 否则把 $A$ 均匀地划分为 $\lceil n/Q \rceil$ 组，每组 $Q$ 个元素（最后一组可能较少）；
2. 对每组排序（如插入排序），求出各组的中位数；
3. 递归调用本算法，求出这 $\lceil n/Q \rceil$ 个中位数的中位数 $M$；
4. 把 $A$ 划分为 $L = \{x < M\}$、$E = \{x = M\}$、$G = \{x > M\}$，并计数；
5. 若 $k < \lvert L \rvert$，在 $L$ 中递归地选取秩为 $k$ 者；若 $k < \lvert L \rvert + \lvert E \rvert$，返回 $M$；否则在 $G$ 中递归地选取秩为 $k - \lvert L \rvert - \lvert E \rvert$ 者。

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

**定理 14.3.3** 取 $Q = 5$ 时，线性时间选取在最坏情况下只需 $O(n)$ 时间。

**证明** 先估计第 5 步的规模。$\lceil n/5 \rceil$ 个组中位数里，至少一半不大于 $M$；除去 $M$ 所在的组和最后一个可能不满的组，这些组中各有至少 3 个元素（中位数及比它小的两个）不大于 $M$。所以不大于 $M$ 的元素至少有

$$
3\left(\left\lceil \frac12 \left\lceil \frac{n}{5} \right\rceil \right\rceil - 2\right) \ge \frac{3n}{10} - 6
$$
个，因而 $\lvert G \rvert \le \frac{7n}{10} + 6$；同理 $\lvert L \rvert \le \frac{7n}{10} + 6$。各步的时间是：第 1、2、4 步 $O(n)$（每组排序只需常数时间），第 3 步 $T(\lceil n/5 \rceil)$，第 5 步至多 $T(7n/10 + 6)$。于是存在常数 $a$，使

$$
T(n) \le T\!\left(\left\lceil \frac{n}{5} \right\rceil\right) + T\!\left(\frac{7n}{10} + 6\right) + a n.
$$
设 $T(m) \le cm$ 对 $m < n$ 成立，代入得 $T(n) \le c(n/5 + 1) + c(7n/10 + 6) + an = cn - (cn/10 - 7c - an)$。当 $n \ge 140$ 且 $c \ge 20a$ 时，$cn/10 - 7c \ge cn/20 \ge an$，故 $T(n) \le cn$；$n < 140$ 的情形取 $c$ 足够大即可。$\square$

证明的关键在于两个子问题的规模之和 $\frac{n}{5} + \frac{7n}{10} = \frac{9n}{10}$ 小于 $n$，于是递归树每深入一层，总工作量就按几何级数递减。组的大小 $Q$ 取 3 时这一和为 $\frac13 + \frac23 = 1$，不能保证线性；取 7 或更大也可以，但每组排序的代价更高。

线性时间选取的常数因子很大，实际中很少直接使用，它的意义在于证明了选取问题可以在线性时间内解决，并为快速选取提供了"保底"。更实用的方法有：内省选取（introselect，Musser），以快速选取为主，递归过深时改用中位数的中位数，C++ 的 `std::nth_element` 采用这类方法，标准只要求平均线性时间；Floyd 与 Rivest（1975）的抽样算法先从一个小样本中选出两个夹住目标的元素，期望只需 $n + \min(k, n - k) + o(n)$ 次比较。对于中位数，已知的最好算法需要约 $2.95n$ 次比较（Dor 与 Zwick），而任何算法都至少需要 $(2 + \varepsilon)n$ 次，精确的常数至今未知。

## 14.4. 希尔排序

### 14.4.1. 框架

插入排序对接近有序的输入很快，但每次只能把元素移动一个位置，对远离正确位置的元素效率很低。D. L. Shell（1959）的想法是：先让元素以大的步长跳跃，粗略地就位，再逐步缩小步长。

**定义 14.4.1（希尔排序）** 取一个递减至 1 的步长序列 $h_t > h_{t-1} > \cdots > h_1 = 1$。依次对每个步长 $h$，把序列 $S[0, n)$ 看作一个 $h$ 列的矩阵（$S[i]$ 位于第 $i \bmod h$ 列），对每一列分别做插入排序。这一排序方法称为**希尔排序**，各步长由小到大排成的序列 $\mathcal{H} = \{h_1 = 1, h_2, \dots\}$ 称为它的**增量序列**（步长序列）。

对一个步长 $h$ 的处理称为 $h$-排序，其结果是 $h$-有序的序列：对所有 $0 \le i < n - h$，$S[i] \le S[i + h]$。由粗到细、逐步求精：先重排成很宽的矩阵并逐列排序，再重排成更窄的矩阵、再次逐列排序，直到矩阵变成一列。最后的 1-排序就是一次完整的插入排序，所以希尔排序一定正确：1-有序就是有序。

矩阵只是一种看法，不需要真的使用二维向量。在每一步中，若当前矩阵宽度为 $h$，则第 $j$ 列由秩为 $j, j + h, j + 2h, \dots$ 的元素组成，直接在一维向量上按步长 $h$ 访问即可。实现时也不必逐列处理：按秩从小到大扫描每个元素，把它插入到所在列的前缀中，效果相同。

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

希尔排序的效率完全取决于增量序列。最后的插入排序代价为 $O(n + I)$，其中 $I$ 为逆序对的总数（定理 3.8.1）：前面的各步就是为了以较低的代价大幅减少逆序对。

### 14.4.2. Shell 序列

Shell 最初建议的增量序列是 $n/2, n/4, \dots, 2, 1$，即 $\mathcal{H}_{\mathrm{shell}} = \{1, 2, 4, 8, \dots, 2^k, \dots\}$（$n$ 为 2 的幂时）。它在最坏情况下需要 $\Theta(n^2)$ 时间。

**例 14.4.1** 设 $n = 2^N$，把最小的 $n/2$ 个元素按升序放在奇数位置、最大的 $n/2$ 个元素按升序放在偶数位置。除最后的 1 之外，所有步长都是偶数，$h$-排序从不比较奇偶位置不同的元素，所以在最后一步之前序列丝毫未变：偶数位置都是大元素，奇数位置都是小元素。第 $i$ 小的元素位于秩 $2i - 1$，需要向前移动约 $i$ 个位置，最后的 1-排序共需 $\sum_{i} \Theta(i) = \Theta(n^2)$ 时间。

问题的根源在于 Shell 序列中各项并不互素，甚至相邻项也不互素：步长为偶数的各步之间没有"交流"。好的增量序列应让相邻的步长**互素**。

### 14.4.3. 保序性与线性组合

为了分析一般的增量序列，需要两个事实。第一个事实是，后面的步骤不会破坏前面步骤的成果。

**引理 14.4.1** 设 $x_1, \dots, x_{m+r}$ 与 $y_1, \dots, y_{n+r}$ 是两个序列，满足 $y_{n+j} \ge x_j$（$1 \le j \le r$）。把两个序列分别排序后，仍有 $y_{n+j} \ge x_j$（$1 \le j \le r$）。

**证明** 排序后的 $y_{n+j}$ 是 $y$ 中第 $n + j$ 小的元素，它不小于 $y$ 中至少 $n + j$ 个元素，其中至少 $j$ 个位于原序列的 $y_{n+1}, \dots, y_{n+r}$ 之中（其余位置只有 $n$ 个）。这 $j$ 个元素各不小于一个不同的 $x$，所以排序后的 $y_{n+j}$ 不小于至少 $j$ 个 $x$，从而不小于排序后的 $x_j$。$\square$

**定理 14.4.1** 一个 $g$-有序的序列，经过 $h$-排序之后，仍然是 $g$-有序的（Knuth，TAOCP 第 3 卷）。

**证明** $h$-排序分别对各列排序。考查第 $c$ 列与第 $c'$ 列，其中 $c' \equiv c + g \pmod h$。第 $c$ 列中秩为 $p$ 的元素与第 $c'$ 列中秩为 $p + g$ 的元素一一对应，后者在第 $c'$ 列中的位置比前者在第 $c$ 列中的位置后移一个固定的量 $\lfloor (c + g)/h \rfloor$。$g$-有序性正是说每一对这样的元素都满足 $S[p] \le S[p+g]$，这恰好是引理 14.4.1 的条件。所以两列各自排序之后，这些不等式仍然成立，序列仍是 $g$-有序的。$\square$

同时是 $g$-有序和 $h$-有序的序列称为 $(g, h)$-有序的。由传递性，它对任何 $a, b \in \mathbb{N}$ 都是 $(ag + bh)$-有序的：从 $S[i]$ 出发，先走 $a$ 步 $g$、再走 $b$ 步 $h$，沿途每一步都不减。第二个事实来自数论：设 $g, h$ 互素，则形如 $ag + bh$（$a, b \in \mathbb{N}$）的数包含所有不小于 $(g-1)(h-1)$ 的整数，不能表示的最大整数是 $gh - g - h$（Sylvester，1884）。例如邮资只有 4 分和 13 分两种邮票时，所有不少于 36 分的邮资都能凑出，35 分则不能。

**定理 14.4.2** 设 $g, h$ 互素，$S[0, n)$ 是 $(g, h)$-有序的。则当 $j - i \ge (g-1)(h-1)$ 时 $S[i] \le S[j]$；因此每个元素的左侧至多有 $(g-1)(h-1)$ 个比它大的元素，逆序对总数不超过 $n(g-1)(h-1)$。

**证明** $j - i \ge (g-1)(h-1)$ 可以写成 $ag + bh$，$(g, h)$-有序蕴含 $(ag + bh)$-有序。$\square$

由此可以估计 $d$-排序的代价：若 $g, h$ 互素且都是 $O(d)$，对一个 $(g, h)$-有序的序列做 $d$-排序，每一列中每个元素左侧比它大的元素至多 $(g-1)(h-1)/d = O(d)$ 个，插入时至多移动这么多次，所以 $d$-排序只需 $O(nd)$ 时间。

### 14.4.4. PS 序列

**例 14.4.2** Papernov 与 Stasevich（1965）的序列 $\mathcal{H}_{\mathrm{ps}} = \{2^k - 1\} = \{1, 3, 7, 15, 31, \dots\}$（也称 Hibbard 序列）。其中不相邻的项未必互素（如 3 与 15），但相邻的项必然互素：$\gcd(2^{k+1} - 1, 2^k - 1) = \gcd(2(2^k - 1) + 1, 2^k - 1) = 1$。

**定理 14.4.3** 采用 PS 序列的希尔排序在最坏情况下需要 $O(n^{3/2})$ 时间。

**证明** 设 $h_t$ 是最接近 $\sqrt{n}$ 的步长，$h_t = \Theta(\sqrt{n})$。分两部分估计。

1. 步长 $h_k \ge h_t$ 的各步：每一列至多 $\lceil n/h_k \rceil$ 个元素，对 $h_k$ 列分别做插入排序共需 $O(h_k \cdot (n/h_k)^2) = O(n^2/h_k)$ 时间。步长按 2 的倍数增长，这些项构成几何级数，总和由最小的一项决定：$O(n^2/h_t) = O(n^{3/2})$。
2. 步长 $h_k < h_t$ 的各步：此前已经做过 $h_{k+1}$-排序和 $h_{k+2}$-排序，由定理 14.4.1，序列是 $(h_{k+1}, h_{k+2})$-有序的。二者互素且都是 $O(h_k)$，所以 $h_k$-排序只需 $O(n h_k)$ 时间。这些项也构成几何级数，总和由最大的一项决定：$O(n h_t) = O(n^{3/2})$。

合计 $O(n^{3/2})$。$\square$

这个上界是紧的：存在使 PS 序列需要 $\Theta(n^{3/2})$ 时间的输入。平均情况的模拟结果约为 $O(n^{5/4})$，但至今未能证明。

### 14.4.5. Pratt 序列

**例 14.4.3** V. Pratt（1971）的序列由所有形如 $2^p 3^q$ 的数组成：$\mathcal{H}_{\mathrm{pratt}} = \{1, 2, 3, 4, 6, 8, 9, 12, 16, 18, \dots\}$。它的相邻项未必互素，而且不超过 $n$ 的项有 $\Theta(\log^2 n)$ 个（$p$ 与 $q$ 各有 $O(\log n)$ 种取值）。

**定理 14.4.4** 采用 Pratt 序列的希尔排序需要 $O(n \log^2 n)$ 时间。

**证明** 先看 $(2, 3)$-有序的序列：$(2-1)(3-1) = 2$，由定理 14.4.2，$j - i \ge 2$ 时 $S[i] \le S[j]$，所以每个元素的左侧至多紧邻的一个元素可能比它大，插入排序只需 $O(n)$ 时间。再看任一步长 $h$：$2h$ 与 $3h$（若不超过 $n$）都在序列中、并且已在之前处理过，由定理 14.4.1，此时序列是 $(2h, 3h)$-有序的。把它分成 $h$ 列，每一列都是 $(2, 3)$-有序的，所以 $h$-排序共需 $O(n)$ 时间。共 $\Theta(\log^2 n)$ 步，合计 $O(n \log^2 n)$。$\square$

Pratt 序列给出了希尔排序已知最好的最坏情况上界，但它的步数太多，即使对已经有序的输入也要做 $\Theta(\log^2 n)$ 趟扫描，实际中反而较慢。

### 14.4.6. Sedgewick 序列与实践

R. Sedgewick（1986）把 PS 序列与 Pratt 序列的思想结合起来，提出了

$$
\mathcal{H}_{\mathrm{sedgewick}} = \{9 \cdot 4^k - 9 \cdot 2^k + 1\} \cup \{4^{k+2} - 3 \cdot 2^{k+2} + 1\} = \{1, 5, 19, 41, 109, 209, 505, 929, \dots\},
$$
它的最坏情况为 $O(n^{4/3})$，平均情况据推测为 $O(n^{7/6})$，在实际中表现最好之一。M. Ciura（2001）通过实验得到的 $1, 4, 10, 23, 57, 132, 301, 701$（再往后按约 2.25 倍延伸）在实验中比较次数更少，但没有理论分析。

| 增量序列 | 例 | 最坏情况 | 说明 |
|---|---|---|---|
| Shell（1959） | $1, 2, 4, 8, \dots$ | $\Theta(n^2)$ | 相邻项不互素 |
| Papernov–Stasevich（1965） | $1, 3, 7, 15, \dots$ | $\Theta(n^{3/2})$ | 相邻项互素 |
| Pratt（1971） | $1, 2, 3, 4, 6, 8, 9, \dots$ | $\Theta(n \log^2 n)$ | 步数为 $\Theta(\log^2 n)$ |
| Sedgewick（1986） | $1, 5, 19, 41, 109, \dots$ | $O(n^{4/3})$ | 实际表现好 |
| Ciura（2001） | $1, 4, 10, 23, 57, \dots$ | 未知 | 实验得到 |

![四种增量序列在随机排列上每个元素的比较次数](./plots/shellsort-gaps.py)

是否存在最坏情况为 $O(n \log n)$ 的增量序列？答案是否定的：Plaxton、Poonen 与 Suel（1992）证明，任何增量序列的希尔排序在最坏情况下都至少需要 $\Omega\bigl(n (\log n / \log\log n)^2\bigr)$ 时间。是否存在平均情况为 $O(n \log n)$ 的增量序列，至今仍未解决。希尔排序代码短、就地、不需要递归，在嵌入式系统等场合仍有应用，例如 uClibc 等嵌入式 C 库曾用它实现 `qsort`。

## 14.5. 标准库中的排序与选取

C++ 标准库的排序与选取算法（[4.2.10](/4.2.10)）都作用于随机访问迭代器区间，可以传入比较器：

| 函数 | 作用 | 常见实现 | 复杂度 |
|---|---|---|---|
| `std::sort` | 排序，不稳定 | 内省排序 | $O(n \log n)$ |
| `std::stable_sort` | 稳定排序 | 归并排序 | $O(n \log n)$；无法分配缓冲区时 $O(n \log^2 n)$ |
| `std::partial_sort` | 只排出最小的 $k$ 个 | 大小为 $k$ 的堆 | $O(n \log k)$ |
| `std::nth_element` | 把秩为 $k$ 的元素放到位置 $k$，左侧不大于它、右侧不小于它 | 内省选取 | 平均 $O(n)$ |
| `std::make_heap` 等 | 堆操作 | 完全二叉堆 | 见 [4.3.12](/4.3.12) |

C++20 起它们都有 `std::ranges` 版本（如 `std::ranges::sort(v)`），可以直接作用于整个容器，并接受投影（只按某个成员排序）。

Python 只提供排序：`list.sort()` 就地排序，`sorted()` 返回新列表，二者都是稳定的 Timsort（3.11 起使用 Powersort 的合并策略），通过 `key` 参数指定排序依据。Python 没有内置的线性时间选取：`statistics.median` 先排序再取中间元素，$O(n \log n)$；取前 $k$ 小用 `heapq.nsmallest`，$O(n \log k)$。需要大规模数值数据的选取时，可以用 NumPy 的 `partition`（[4.4](/4.4)）。

## 小结

- 快速排序 = 把元素逐个转化为轴点。LUG 勤于拓展，在相等元素上退化；DUP 让相等元素交替地分到两侧；LGU 单向扫描、最简洁；三路划分把相等元素一次就位。
- 只对较短的一侧递归，空间 $O(\log n)$；随机轴点使递归深度以极高的概率为 $O(\log n)$，期望比较次数为 $2(n+1)H_n - 4n \approx 1.386\, n \log_2 n$（后向分析：$s_i$ 与 $s_j$ 比较的概率为 $2/(j - i + 1)$）。
- 工业级排序：C++ 的内省排序（快速排序 + 堆排序 + 插入排序）、pdqsort，Python 的 Timsort / Powersort。
- 选取：下界 $\Omega(n)$；多数投票算法 $O(n)$ 时间、$O(1)$ 空间；两个有序向量的第 $k$ 小 $O(\log \min(n_1, n_2))$；快速选取期望 $O(n)$；中位数的中位数保证最坏 $O(n)$，关键是 $\frac15 + \frac{7}{10} < 1$。
- 希尔排序的效率取决于增量序列：$h$-排序保持 $g$-有序性；$(g, h)$-有序且 $g, h$ 互素时只剩 $O(n gh)$ 个逆序对。Shell 序列 $\Theta(n^2)$，PS 序列 $\Theta(n^{3/2})$，Pratt 序列 $\Theta(n \log^2 n)$，Sedgewick 序列 $O(n^{4/3})$；不存在最坏 $O(n \log n)$ 的增量序列。
