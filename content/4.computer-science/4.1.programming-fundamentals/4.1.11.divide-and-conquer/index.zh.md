---
title: 分治
description: 分治的三个步骤与递推式；归并排序与合并过程；快速排序的思路、几种划分方法与枢轴的选择；青蛙过河问题中的子系统分解；九连环的递归解法与步数。
---

上一章的减治每次只留下一个子问题。本章的分治更进一步：把问题分成几个互相独立的子问题，分别递归求解，再把子问题的解合并成原问题的解。分治是算法设计中最有成效的思想之一，排序、快速傅里叶变换、大整数乘法、最近点对等许多高效算法都是分治算法。本章以两种最重要的排序算法，归并排序与快速排序为主线：它们把问题分成两半的方式不同，一个"分得容易、合得费力"，一个"分得费力、合得容易"。随后用两道智力题（青蛙过河、九连环）练习怎样在一个看似复杂的过程里找出可以分解的结构。分治算法的复杂度分析（主定理）和排序算法的系统比较在 [4.3.1](/4.3.1)、[4.3.2](/4.3.2) 与 [4.3.14](/4.3.14) 中讨论。

## 11.1. 分治的思想

**定义 11.1.1（分治）** 把规模为 $n$ 的问题分解为若干个（通常是两个）规模较小、相互独立、与原问题同类的子问题，递归地求解这些子问题，再把它们的解合并为原问题的解，这种策略称为**分治**。

分治算法都由三步组成：

1. 分解（divide）：把问题分成若干子问题；
2. 解决（conquer）：递归地求解子问题，规模足够小时直接求解；
3. 合并（combine）：把子问题的解组合成原问题的解。

若把规模为 $n$ 的问题分成 $a$ 个规模为 $n/b$ 的子问题，分解与合并共需 $f(n)$ 的工作量，则总工作量满足递推式

$$
T(n) = a\,T(n/b) + f(n).
$$

下面的归并排序中 $a = b = 2$、$f(n)$ 与 $n$ 成正比，解出 $T(n)$ 与 $n \log n$ 成正比。这类递推式的一般解法（主定理）见 [4.3.1](/4.3.1)。

分治与减治的区别是子问题的个数（一个还是几个），与 [4.1.13](/4.1.13) 动态规划的区别是子问题是否重叠：分治要求子问题互相独立，若子问题大量重叠（如上一章的 Fibonacci 数列），直接分治会重复计算，应当改用记忆化或动态规划。

## 11.2. 归并排序

### 11.2.1. 算法

**算法 11.2.1（归并排序）** 对数组 $A[\mathit{lo}..\mathit{hi})$ 排序：

1. 若区间中元素少于 2 个，它已经有序，直接返回；
2. 取中点 $\mathit{mid} = \lfloor(\mathit{lo} + \mathit{hi})/2\rfloor$，递归地分别排序 $A[\mathit{lo}..\mathit{mid})$ 和 $A[\mathit{mid}..\mathit{hi})$；
3. 把两个有序的半段合并成一个有序段。

这里用左闭右开区间 $[\mathit{lo}, \mathit{hi})$ 表示子数组：它的长度就是 $\mathit{hi} - \mathit{lo}$，两半 $[\mathit{lo}, \mathit{mid})$ 与 $[\mathit{mid}, \mathit{hi})$ 首尾相接，不需要 $\pm 1$ 的修正，这也是 C++ 迭代器和 Python 切片的约定。

合并是归并排序的核心。两个有序序列的最小元素一定是其中之一的首元素，所以只要比较两个"当前首元素"，把较小者移到输出中，重复这一步，直到某个序列取完，再把另一个序列的剩余部分接上。合并两个总长为 $n$ 的序列只需不超过 $n - 1$ 次比较。合并需要一个临时数组；在递归之前一次性分配好、在各层调用之间共用，可以避免在每次调用中反复分配和释放内存。

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

中点写成 `lo + (hi - lo) / 2` 而不是 `(lo + hi) / 2`，是为了避免两个大下标相加时整数溢出。Python 版本用切片得到两半、返回新列表，写法更接近算法的数学描述，代价是每层都复制数据；C++ 版本在原数组上就地排序，只用一个共享的缓冲区。

### 11.2.2. 性质

递归树有约 $\log_2 n$ 层，每一层的合并操作合计处理 $n$ 个元素，所以归并排序的比较次数与 $n \log n$ 成正比，并且与输入的初始顺序无关，最坏情况也是如此。它需要与输入同样大小的额外空间。归并排序是稳定的：相等的元素在排序后保持原来的相对次序（合并时相等元素先取左边的）。稳定性在按多个关键字排序时很有用，例如先按姓名排序、再按成绩稳定排序，成绩相同的人仍按姓名排列。

Python 内置的 `list.sort` 与 `sorted` 是一种归并排序的改进（Timsort，3.11 起改用 Powersort 的合并策略），它会识别输入中已经有序的段，因此对部分有序的数据特别快，并且是稳定的。C++ 的 `std::stable_sort` 也是稳定的归并类排序。

## 11.3. 快速排序

### 11.3.1. 思路

归并排序把数组机械地切成两半，排好序的两半之间没有大小关系，所以要费力合并。快速排序反过来：先花力气把数组整理成"左边都不大于某个值、右边都不小于它"，这样两边各自排好序之后，整个数组自然有序，不需要合并。

**算法 11.3.1（快速排序）** 对数组 $A[\mathit{lo}..\mathit{hi}]$ 排序：

1. 若区间中元素少于 2 个，直接返回；
2. 划分：选一个元素作为枢轴（pivot），重排区间，使枢轴左边的元素都不大于它、右边的都不小于它，枢轴落在它的最终位置 $p$；
3. 递归地分别排序 $A[\mathit{lo}..p-1]$ 与 $A[p+1..\mathit{hi}]$。

正确性很容易用归纳法说明：划分之后枢轴已在最终位置，左右两段各自排好序后，左段的元素都不大于枢轴、右段的都不小于枢轴，整体有序。算法的关键和难点在于怎样高效地、就地完成划分。

### 11.3.2. 划分方法

最直接的方法是借助额外空间：扫描一遍，把小于枢轴的、等于枢轴的、大于枢轴的元素分别放进三个列表，再拼起来。这在 Python 中几乎就是算法的定义：

```python
def quick_sort(a: list[int]) -> list[int]:
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2]
    return (quick_sort([x for x in a if x < pivot])
            + [x for x in a if x == pivot]
            + quick_sort([x for x in a if x > pivot]))
```

它清楚地表达了思想，但每层都要复制数据。实用的快速排序就地划分，不使用额外数组。常用的是"双向扫描"：以首元素为枢轴并把它暂存起来，留下一个"空位"；从右向左找一个小于枢轴的元素填入左边的空位，空位随之转到右边；再从左向右找一个大于枢轴的元素填入右边的空位；两个方向轮流进行，直到左右两个指针相遇，把枢轴放回这个位置。整个过程中，左指针左边的元素都不大于枢轴，右指针右边的元素都不小于枢轴。

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

另一种常见写法（Lomuto 划分）只用一个从左到右的扫描指针，维护"小于枢轴的元素都在前面"，代码更短但交换次数更多；C. A. R. Hoare 最初提出的方法则从两端相向扫描、成对交换逆序的元素。各种划分方法的细节、比较以及对大量重复元素的处理（三路划分）见 [4.3.14](/4.3.14)。

### 11.3.3. 枢轴的选择与性能

快速排序的效率取决于划分是否均衡。若每次枢轴都接近中位数，递归树有约 $\log_2 n$ 层，每层的划分合计扫描 $n$ 个元素，总工作量与 $n \log n$ 成正比；若每次枢轴都是最小或最大元素，每次只能去掉一个元素，工作量与 $n^2$ 成正比，递归深度也达到 $n$。固定取首元素作枢轴时，已经有序的输入恰好是最坏情况，而有序或接近有序的数据在实际中很常见。

解决办法是随机选取枢轴（上面的代码就是这样做的），或者取首、中、尾三个元素的中位数。随机选取枢轴时，对任何输入，期望的比较次数都约为 $1.39\, n \log_2 n$，最坏情况出现的概率极小。快速排序在实际中通常比归并排序快：它就地进行、访问内存的模式对缓存友好，内层循环极简单。它的缺点是不稳定，最坏情况较差。C++ 的 `std::sort` 在主流实现中采用内省排序（introsort）：以快速排序为主，递归过深时改用堆排序，保证最坏情况下也是 $n \log n$ 量级，小区间改用插入排序。

| | 归并排序 | 快速排序 |
|---|---|---|
| 分解 | 从中间切开，不费力 | 划分，费力 |
| 合并 | 合并两个有序段，费力 | 不需要 |
| 比较次数 | 总是 $n \log n$ 量级 | 平均 $n \log n$，最坏 $n^2$ |
| 额外空间 | 与 $n$ 成正比 | 递归栈，平均 $\log n$ 层 |
| 稳定 | 是 | 否 |

## 11.4. 例：青蛙过河

**例 11.4.1（青蛙过河，NOI 2000）** 一条小溪的左岸有石柱 L，右岸有石柱 R，溪中有 $s$ 根石柱和 $y$ 片荷叶。$n$ 只大小各不相同的青蛙按编号 $1, \dots, n$（1 最小）叠在 L 上，大的在下、小的在上。规则如下：

- 每次只能跳一只青蛙，且只能跳最上面的那只；
- 石柱（L、R 和溪中的石柱）上可以叠多只青蛙，但必须大的在下、小的在上；荷叶上只能有一只青蛙；
- 青蛙离开 L 后不能再跳回 L，跳上 R 后不能再离开。

问：已知 $s$ 和 $y$，最多能有多少只青蛙全部跳到 R 上？记答案为 $\mathrm{Jump}(s, y)$。

先看简单情形。溪中没有石柱时，荷叶只能各放一只青蛙：先把上面 $y$ 只青蛙依次跳到 $y$ 片荷叶上，第 $y + 1$ 只直接跳到 R，然后荷叶上的青蛙从小号到大号的逆序（即先大后小）依次跳到 R 上。所以 $\mathrm{Jump}(0, y) = y + 1$。

再看 $s = 1$、$y = 1$。可以先把 L 上面的两只青蛙借助荷叶转移到溪中石柱 S 上（相当于一个 $\mathrm{Jump}(0, 1)$ 的小问题，只是目的地换成了 S），再把 L 上剩下的两只借助荷叶跳到 R（又一个 $\mathrm{Jump}(0, 1)$），最后把 S 上的两只借助荷叶跳到 R（还是 $\mathrm{Jump}(0, 1)$；它们比 R 上的青蛙小，可以叠上去）。共 4 只、9 步。

这就是分治的视角：溪中的一根石柱与两岸的作用相同，可以叠放多只青蛙。把整个过程分为"L–荷叶–S""L–荷叶–R""S–荷叶–R"三个阶段，每个阶段都是少了一根石柱的同一问题。先用 $s - 1$ 根石柱和全部荷叶把上面一半青蛙转移到某根石柱上；再用剩下的 $s - 1$ 根石柱和荷叶把下面一半转移到 R；最后把那根石柱上的一半转移到 R。于是

$$
\mathrm{Jump}(s, y) = 2\,\mathrm{Jump}(s - 1, y), \qquad \mathrm{Jump}(0, y) = y + 1,
$$

解得 $\mathrm{Jump}(s, y) = 2^s (y + 1)$。例如 $s = 3$、$y = 4$ 时最多 40 只。

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

程序本身只有几行，难点在于建模：先从 $s = 0$ 的简单情形归纳出结论，再找到"一根石柱相当于一个可以暂存青蛙的岸"这个观察，问题就分解开了。上面的论证说明 $2^s(y + 1)$ 只青蛙可以过河；它也是最大值，这需要另一个方向的论证（考虑最大的青蛙跳到 R 之前其余青蛙的位置），这里从略。

## 11.5. 例：九连环

**例 11.5.1（九连环）** 九连环由 9 个环套在一根横杆（"剑"）上组成，环从外向内编号为 $1, \dots, 9$。规则是：第 1 号环可以随时上下；第 $k$ 号环（$k \geq 2$）能够上下，当且仅当第 $k-1$ 号环在杆上，并且第 $1, \dots, k-2$ 号环都不在杆上。开始时 9 个环都在杆上，求把它们全部取下的步骤。

要取下第 $n$ 号环，必须先使第 $n-1$ 号环在杆上、第 $1, \dots, n-2$ 号环都不在杆上。于是"取下前 $n$ 个环"可以分解为：

1. 取下前 $n - 2$ 个环；
2. 取下第 $n$ 号环（此时第 $n - 1$ 号在杆上、更小的都已取下，合法）；
3. 装上前 $n - 2$ 个环（为取下第 $n - 1$ 号环恢复条件）；
4. 取下前 $n - 1$ 个环。

第 3 步"装上前 $n - 2$ 个环"是与之对称的子问题，同样可以分解：先装上前 $n - 1$ 个环，再取下前 $n - 2$ 个环，装上第 $n$ 号环，最后装上前 $n - 2$ 个环。两个互相调用的递归函数就描述了全部步骤：

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

设取下（或装上，二者对称）$n$ 个环需要 $a_n$ 步，由分解得 $a_n = a_{n-1} + 2a_{n-2} + 1$，$a_1 = 1$，$a_2 = 2$，于是 $a_n$ 依次为 $1, 2, 5, 10, 21, 42, 85, 170, 341$：$n$ 为奇数时 $a_n = (2^{n+1} - 1)/3$，为偶数时 $a_n = (2^{n+1} - 2)/3$。九连环需要 341 步。与汉诺塔一样，步数随环数指数增长；不同的是这里的子问题有两种（取下与装上），它们互相递归。

## 小结

- 分治 = 分解 + 递归求解 + 合并，要求子问题相互独立；工作量满足 $T(n) = aT(n/b) + f(n)$。
- 归并排序：分得容易、合得费力；总是 $n \log n$ 量级，稳定，需要额外空间。
- 快速排序：分得费力、合得容易；平均 $n \log n$，就地进行，随机枢轴避免最坏情况，不稳定。
- 分析一个过程时，先算简单情形，再找出"去掉一个部件后仍是同一问题"的结构（青蛙过河的石柱、九连环的前 $n - 2$ 个环）。
