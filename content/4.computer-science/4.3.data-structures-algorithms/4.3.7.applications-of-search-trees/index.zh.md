---
title: 搜索树的应用
description: 搜索树在几何查询中的应用：穿刺查询与区间树、基本区间与线段树；一维与平面的范围查询、输出敏感性；多层搜索树、范围树与分散层叠；kd 树的构造、查询与复杂度。
---

上一章的二叉搜索树回答的是"某个关键码是否存在"。许多实际问题问的却是"哪些数据落在某个范围内"：哪些预约时段覆盖了下午三点？哪些员工的年龄在 30 到 40 岁之间、月薪在两万到三万之间？地图上某个矩形窗口里有哪些地点？这些是计算几何中的基本查询，数据集相对固定，查询却源源不断（在线查询），所以值得花时间把数据预处理成合适的结构，使每次查询都很快。

本章的各种结构都建立在平衡二叉搜索树（[4.3.6](/4.3.6)）之上，核心思想是同一个：把查询范围分解为树中 $O(\log n)$ 个"规范"的子树，每棵子树要么整体命中，要么整体排除，只有边界附近的节点需要逐个检查。区间树与线段树处理区间的穿刺查询；范围树与 kd 树处理点集的正交范围查询。分析中会反复出现输出敏感性：报告 $r$ 个结果至少需要 $\Omega(r)$ 时间，所以好的查询算法的时间应形如 $O(f(n) + r)$，其中 $f(n)$ 远小于 $n$。

## 7.1. 区间树

### 7.1.1. 穿刺查询

**定义 7.1.1（穿刺查询）** 给定 $x$ 轴上 $n$ 个闭区间组成的集合 $S$，对任一查询点 $q_x$，找出 $S$ 中包含 $q_x$ 的所有区间，称为**穿刺查询**。

蛮力解法逐个检查每个区间，需要 $O(n)$ 时间，没有利用"区间集相对固定"的条件。把区间集预处理成一棵区间树，每次查询只需 $O(\log n + r)$ 时间，$r$ 是命中的区间数。

### 7.1.2. 结构

区间树的构造是**分治**的。设 $P$ 是所有区间端点组成的集合（$2n$ 个），取其中位数 $x_{\mathrm{mid}}$，所有区间按与 $x_{\mathrm{mid}}$ 的关系分为三类：

- $S_{\mathrm{left}}$：整个位于 $x_{\mathrm{mid}}$ 左侧的区间；
- $S_{\mathrm{mid}}$：包含 $x_{\mathrm{mid}}$ 的区间；
- $S_{\mathrm{right}}$：整个位于 $x_{\mathrm{mid}}$ 右侧的区间。

**定义 7.1.2（区间树）** 以 $x_{\mathrm{mid}}$ 为根，$S_{\mathrm{mid}}$ 存放在根节点，对 $S_{\mathrm{left}}$、$S_{\mathrm{right}}$ 递归地同样划分，分别构造左右子树，直至无需划分。根节点中的 $S_{\mathrm{mid}}$ 存成两个关联列表：按左端点从小到大排列的 L-list，以及按右端点从大到小排列的 R-list（都是"由外向内"）。这样得到的二叉树称为**区间树**。

$S_{\mathrm{left}}$ 与 $S_{\mathrm{right}}$ 的端点都只占 $P$ 的一半以下，所以每深入一层，子问题的规模至少减半，树高为 $O(\log n)$。每个区间恰好存放在一个节点中（它所包含的、深度最小的那个 $x_{\mathrm{mid}}$ 处），存放两份，所以总空间为 $O(n)$。构造时若先对全部端点排序一次，此后各层只需线性时间就能取中位数并分拣区间，总构造时间为 $O(n \log n)$。

### 7.1.3. 查询

**算法 7.1.1（区间树的穿刺查询）** 从根出发，在当前节点 $v$ 处：

1. 若 $q_x < x_{\mathrm{mid}}(v)$：$S_{\mathrm{mid}}(v)$ 中的区间都包含 $x_{\mathrm{mid}}(v) > q_x$，所以它们包含 $q_x$ 当且仅当左端点不大于 $q_x$。从头扫描 L-list，报告左端点不大于 $q_x$ 的区间，遇到第一个左端点大于 $q_x$ 的就停止；然后转入左子树。
2. 若 $q_x > x_{\mathrm{mid}}(v)$：对称地扫描 R-list，然后转入右子树。
3. 若 $q_x = x_{\mathrm{mid}}(v)$：直接报告 $S_{\mathrm{mid}}(v)$ 中的全部区间，结束（此时两棵子树中的区间都不包含 $q_x$）。

查询只沿一条从根出发的路径下行，访问 $O(\log n)$ 个节点。在每个节点处，扫描关联列表时成功的次数计入输出，失败的至多一次，所以总时间为 $O(\log n + r)$。

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <memory>
#include <random>
#include <vector>

template <typename T>
class IntervalTree {                                // closed intervals [lo, hi]
public:
    struct Interval { T lo, hi; int id; };

private:
    struct Node {
        T xmid;
        std::vector<Interval> by_lo, by_hi;         // S_mid sorted by lo ascending / hi descending
        std::unique_ptr<Node> lc, rc;
    };
    std::unique_ptr<Node> root;

    static std::unique_ptr<Node> build(std::vector<Interval> s) {
        if (s.empty()) return nullptr;
        std::vector<T> ends;                        // median of all endpoints
        for (auto& i : s) { ends.push_back(i.lo); ends.push_back(i.hi); }
        auto mid = ends.begin() + ends.size() / 2;
        std::ranges::nth_element(ends, mid);        // O(|s|)
        auto v = std::make_unique<Node>();
        v->xmid = *mid;
        std::vector<Interval> left, right;
        for (auto& i : s) {
            if (i.hi < v->xmid) left.push_back(i);
            else if (v->xmid < i.lo) right.push_back(i);
            else v->by_lo.push_back(i);              // contains xmid
        }
        v->by_hi = v->by_lo;
        std::ranges::sort(v->by_lo, {}, &Interval::lo);
        std::ranges::sort(v->by_hi, std::greater{}, &Interval::hi);
        v->lc = build(std::move(left));
        v->rc = build(std::move(right));
        return v;
    }

public:
    explicit IntervalTree(std::vector<Interval> s) : root(build(std::move(s))) {}

    template <typename F> void stab(T q, F&& report) const {  // O(log n + r)
        for (Node* v = root.get(); v; ) {
            if (q < v->xmid) {                      // only the lo side can exclude q
                for (auto& i : v->by_lo) { if (q < i.lo) break; report(i); }
                v = v->lc.get();
            } else if (v->xmid < q) {               // only the hi side can exclude q
                for (auto& i : v->by_hi) { if (i.hi < q) break; report(i); }
                v = v->rc.get();
            } else {                                // q == xmid: all of S_mid, and stop
                for (auto& i : v->by_lo) report(i);
                return;
            }
        }
    }
};

int main() {
    std::mt19937 rng(3);
    using IT = IntervalTree<int>;
    std::vector<IT::Interval> s;
    for (int k = 0; k < 2000; ++k) {
        int a = static_cast<int>(rng() % 10000), b = static_cast<int>(rng() % 10000);
        s.push_back({std::min(a, b), std::max(a, b), k});
    }
    IT t(s);
    std::size_t total = 0;
    for (int q = -5; q <= 10005; ++q) {             // compare with brute force
        std::vector<int> got, want;
        t.stab(q, [&](const IT::Interval& i) { got.push_back(i.id); });
        for (auto& i : s) if (i.lo <= q && q <= i.hi) want.push_back(i.id);
        std::ranges::sort(got);
        if (got != want) return 1;
        total += got.size();
    }
    std::cout << std::format("ok: {} reported intervals\n", total);
}
```

```python tab
from __future__ import annotations

import random
from collections.abc import Iterator
from typing import NamedTuple


class Interval(NamedTuple):                        # closed interval [lo, hi]
    lo: float
    hi: float
    id: int


class Node:
    def __init__(self, xmid: float, mid: list[Interval]) -> None:
        self.xmid = xmid
        self.by_lo = sorted(mid, key=lambda i: i.lo)              # ascending lo
        self.by_hi = sorted(mid, key=lambda i: i.hi, reverse=True)  # descending hi
        self.lc: Node | None = None
        self.rc: Node | None = None


def build(s: list[Interval]) -> Node | None:
    if not s:
        return None
    ends = sorted(e for i in s for e in (i.lo, i.hi))  # (a linear-time selection would do)
    xmid = ends[len(ends) // 2]                    # median endpoint
    v = Node(xmid, [i for i in s if i.lo <= xmid <= i.hi])
    v.lc = build([i for i in s if i.hi < xmid])
    v.rc = build([i for i in s if xmid < i.lo])
    return v


def stab(v: Node | None, q: float) -> Iterator[Interval]:   # O(log n + r)
    while v:
        if q < v.xmid:                             # only the lo side can exclude q
            for i in v.by_lo:
                if q < i.lo:
                    break
                yield i
            v = v.lc
        elif v.xmid < q:                           # only the hi side can exclude q
            for i in v.by_hi:
                if i.hi < q:
                    break
                yield i
            v = v.rc
        else:                                      # q == xmid
            yield from v.by_lo
            return


rng = random.Random(3)
s = [Interval(*sorted((rng.randrange(10000), rng.randrange(10000))), k) for k in range(500)]
t = build(s)
for q in range(-5, 10006, 7):
    assert sorted(i.id for i in stab(t, q)) == [i.id for i in s if i.lo <= q <= i.hi]
print("ok")
```

## 7.2. 线段树

### 7.2.1. 基本区间与离散化

另一种思路是把 $x$ 轴离散化。把 $n$ 个区间的端点排序为 $p_1 < p_2 < \dots < p_m$（$m \le 2n$），它们把 $x$ 轴分成若干段：开区间 $(-\infty, p_1)$、$(p_1, p_2)$、……、$(p_m, +\infty)$，以及（处理闭区间时）单点 $[p_i, p_i]$，总共 $2m + 1$ 段，称为基本区间（elementary interval）。

同一段基本区间内的任何位置，穿刺查询的结果都完全一样。所以可以把所有基本区间按次序存入一个有序向量，并让每段基本区间预先记录它的查询结果。查询时二分查找确定 $q_x$ 所在的基本区间，再输出记录的结果，只需 $O(\log n + r)$ 时间。问题在于空间：最坏情况下，每个输入区间都横跨 $\Theta(n)$ 段基本区间（例如 $n$ 个互相嵌套的区间），总共需要 $\Theta(n^2)$ 的空间。

### 7.2.2. 结构

把有序向量升级为一棵以基本区间为叶节点的平衡二叉搜索树。节点 $v$ 的作用域 $R(v)$ 定义为：叶节点的作用域就是它对应的基本区间，内部节点的作用域是其两个孩子作用域的并，也就是它所有后代叶节点的基本区间之并，一段连续的区间。

若只在叶节点处记录横跨它的输入区间，空间仍是 $\Theta(n^2)$。改进的办法是贪心地合并：一个区间若覆盖了某节点的整个作用域，就只记在这个节点上，不再记在它的后代中。

**定义 7.2.1（线段树）** 在上述以基本区间为叶节点的平衡二叉搜索树中，每个节点 $v$ 记录一个集合 $\mathrm{Int}(v)$：输入区间 $s$ 属于 $\mathrm{Int}(v)$，当且仅当 $R(v) \subseteq s$ 而 $R(\operatorname{parent}(v)) \not\subseteq s$。这样的结构称为**线段树**（segment tree）。

**命题 7.2.1** 每个输入区间至多记录在每一层的 $2$ 个节点中，因此线段树的总空间为 $O(n \log n)$。

**证明** 设区间 $s$ 记录在同一层自左向右的三个节点 $v_1$、$v_2$、$v_3$ 中。$s$ 是一段连续的区间，所以它覆盖了从 $R(v_1)$ 到 $R(v_3)$ 之间的全部范围。$v_2$ 的兄弟在同一层上紧挨着 $v_2$，位于 $v_1$ 与 $v_3$ 之间（含两端），其作用域也被 $s$ 覆盖，于是 $R(\operatorname{parent}(v_2)) \subseteq s$，与 $s \in \mathrm{Int}(v_2)$ 矛盾。树高为 $O(\log n)$，所以每个区间至多记录在 $O(\log n)$ 个节点中。$\square$

**算法 7.2.1（插入区间）** 从根出发，对区间 $s$ 执行 `InsertSeg(v, s)`：若 $R(v) \subseteq s$，则把 $s$ 记入 $\mathrm{Int}(v)$ 并返回；否则，若 $R(\operatorname{lc}(v))$ 与 $s$ 相交，递归处理左孩子；若 $R(\operatorname{rc}(v))$ 与 $s$ 相交，递归处理右孩子。

在每一层上，这个过程至多访问 $4$ 个节点（$2$ 个记录 $s$，另外 $2$ 个继续递归），所以插入一个区间只需 $O(\log n)$ 时间。构造线段树时，先排序全部端点（$O(n \log n)$），把基本区间组织为平衡二叉树并自底而上算出各节点的作用域（$O(n)$），再逐个插入区间（$O(n \log n)$）。

### 7.2.3. 查询

**算法 7.2.2（线段树的穿刺查询）** 从根出发下行到包含 $q_x$ 的叶节点，沿途报告每个节点 $v$ 的 $\mathrm{Int}(v)$ 中的全部区间。

$q_x$ 落在 $R(v)$ 内时，$\mathrm{Int}(v)$ 中的区间都覆盖 $R(v)$，当然包含 $q_x$；反之，包含 $q_x$ 的区间必定记录在路径上的某个节点中（它的规范节点中恰有一个的作用域包含 $q_x$），而且只记录一次。每层只访问一个节点，在节点 $v$ 处用时 $O(1 + r_v)$，总时间为 $O(\log n + r)$。

**定理 7.2.2** 任给 $x$ 轴上的 $n$ 个区间，可以在 $O(n \log n)$ 时间内构造一棵占用 $O(n \log n)$ 空间的线段树，借助它，每次穿刺查询都能在 $O(\log n + r)$ 时间内完成。

下面的实现用堆式的数组存放这棵完全平衡的树（节点 $v$ 的孩子为 $2v$ 和 $2v + 1$），叶节点按次序编号：第 $2i$ 号叶节点是 $p_i$ 左侧的开区间，第 $2i + 1$ 号是单点 $p_i$。

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <vector>

// Segment tree for stabbing queries on closed intervals [lo, hi].
// The m distinct endpoints p_0 < ... < p_{m-1} cut the line into 2m + 1 elementary intervals:
// leaf 2i is the open gap left of p_i, leaf 2i + 1 is the point p_i, leaf 2m is (p_{m-1}, +inf).
template <typename T>
class SegmentTree {
public:
    struct Interval { T lo, hi; int id; };

private:
    std::vector<T> p;                               // sorted distinct endpoints
    std::vector<std::vector<int>> store;            // Int(v): ids stored at node v (heap layout)
    int leaves = 0;

    int leaf_of(T x) const {                        // elementary interval containing x, O(log m)
        int i = static_cast<int>(std::ranges::lower_bound(p, x) - p.begin());
        return (i < static_cast<int>(p.size()) && p[i] == x) ? 2 * i + 1 : 2 * i;
    }
    // Store id at the canonical nodes covering leaves [a, b]; node v spans leaves [l, r]
    void insert(int v, int l, int r, int a, int b, int id) {
        if (a <= l && r <= b) { store[v].push_back(id); return; }  // R(v) inside s: stop here
        int mid = (l + r) / 2;
        if (a <= mid) insert(2 * v, l, mid, a, b, id);
        if (mid < b) insert(2 * v + 1, mid + 1, r, a, b, id);
    }

public:
    explicit SegmentTree(const std::vector<Interval>& s) {
        for (auto& i : s) { p.push_back(i.lo); p.push_back(i.hi); }
        std::ranges::sort(p);
        p.erase(std::unique(p.begin(), p.end()), p.end());
        leaves = 2 * static_cast<int>(p.size()) + 1;
        store.resize(4 * leaves);
        for (auto& i : s) insert(1, 0, leaves - 1, leaf_of(i.lo), leaf_of(i.hi), i.id);
    }
    template <typename F> void stab(T q, F&& report) const {  // O(log n + r)
        int target = leaf_of(q), v = 1, l = 0, r = leaves - 1;
        while (true) {                              // one node per level, root to leaf
            for (int id : store[v]) report(id);
            if (l == r) return;
            int mid = (l + r) / 2;
            if (target <= mid) { v = 2 * v; r = mid; } else { v = 2 * v + 1; l = mid + 1; }
        }
    }
    std::size_t stored() const {                    // total number of stored copies
        std::size_t c = 0;
        for (auto& ids : store) c += ids.size();
        return c;
    }
};

int main() {
    std::mt19937 rng(5);
    using ST = SegmentTree<int>;
    std::vector<ST::Interval> s;
    for (int k = 0; k < 2000; ++k) {
        int a = static_cast<int>(rng() % 10000), b = static_cast<int>(rng() % 10000);
        s.push_back({std::min(a, b), std::max(a, b), k});
    }
    ST t(s);
    for (int q = -5; q <= 10005; ++q) {
        std::vector<int> got, want;
        t.stab(q, [&](int id) { got.push_back(id); });
        for (auto& i : s) if (i.lo <= q && q <= i.hi) want.push_back(i.id);
        std::ranges::sort(got);
        if (got != want) return 1;
    }
    std::cout << std::format("ok: {} intervals stored as {} copies\n", s.size(), t.stored());
}
```

```python tab
import random
from bisect import bisect_left
from collections.abc import Iterator


class SegmentTree:
    """Stabbing queries on closed intervals (lo, hi, id).

    The m distinct endpoints p_0 < ... < p_{m-1} give 2m + 1 elementary intervals:
    leaf 2i is the gap left of p_i, leaf 2i + 1 is the point p_i, leaf 2m is (p_{m-1}, +inf).
    """

    def __init__(self, s: list[tuple[float, float, int]]) -> None:
        self.p = sorted({e for lo, hi, _ in s for e in (lo, hi)})
        self.leaves = 2 * len(self.p) + 1
        self.store: list[list[int]] = [[] for _ in range(4 * self.leaves)]  # Int(v)
        for lo, hi, ident in s:
            self._insert(1, 0, self.leaves - 1, self._leaf(lo), self._leaf(hi), ident)

    def _leaf(self, x: float) -> int:              # elementary interval containing x
        i = bisect_left(self.p, x)
        return 2 * i + 1 if i < len(self.p) and self.p[i] == x else 2 * i

    def _insert(self, v: int, l: int, r: int, a: int, b: int, ident: int) -> None:
        if a <= l and r <= b:                      # R(v) inside the interval: store and stop
            self.store[v].append(ident)
            return
        mid = (l + r) // 2
        if a <= mid:
            self._insert(2 * v, l, mid, a, b, ident)
        if mid < b:
            self._insert(2 * v + 1, mid + 1, r, a, b, ident)

    def stab(self, q: float) -> Iterator[int]:     # O(log n + r)
        target, v, l, r = self._leaf(q), 1, 0, self.leaves - 1
        while True:                                # one node per level, root to leaf
            yield from self.store[v]
            if l == r:
                return
            mid = (l + r) // 2
            if target <= mid:
                v, r = 2 * v, mid
            else:
                v, l = 2 * v + 1, mid + 1


rng = random.Random(5)
s = [(*sorted((rng.randrange(10000), rng.randrange(10000))), k) for k in range(500)]
t = SegmentTree(s)
for q in range(-5, 10006, 7):
    assert sorted(t.stab(q)) == [k for lo, hi, k in s if lo <= q <= hi]
print("ok:", sum(map(len, t.store)), "stored copies")
```

与区间树相比，线段树多用了一个 $\log n$ 因子的空间，但它更通用：每个节点的 $\mathrm{Int}(v)$ 可以换成别的结构，从而支持计数查询、带权查询，或在第二维上再套一层搜索树来处理平面上的线段（窗口查询）。

程序设计竞赛中常说的"线段树"是同一骨架的另一种用法：叶节点是数组的各个下标，每个节点保存其下标范围上的聚合值（和、最小值等），任一下标区间都能分解为 $O(\log n)$ 个节点的作用域，因此区间求和、区间修改（配合懒惰标记）都只需 $O(\log n)$ 时间。

## 7.3. 范围查询

### 7.3.1. 一维范围查询

**定义 7.3.1（范围查询）** 给定点集 $P$，对任一查询范围 $R$（一维时是区间 $[x_1, x_2]$，$d$ 维时是各维区间的乘积，称为正交范围），统计 $P$ 中有多少点落在 $R$ 内（计数查询），或列出这些点（报告查询），称为**范围查询**。

通常 $P$ 相对固定，而 $R$ 不断变化。蛮力算法逐个检查每个点，需要 $O(n)$ 时间。在最坏情况下会有 $\Theta(n)$ 个点命中，即使只是列出它们也需要 $\Theta(n)$ 时间，所以单看最坏情况，蛮力已经无法改进。但若把查找与报告分开，就能做得更好。

把所有点预处理为一个有序向量（并在最前面放一个值为 $-\infty$ 的哨兵 $p_0$）。查询 $[x_1, x_2]$ 时，用二分查找确定 $t = \max\{i : p_i \le x_2\}$，再从 $p_t$ 开始向前遍历，直到在某个 $p_s$ 处越出查询区间，$(s, t]$ 中的点恰好是全部输出。查询时间为 $O(\log n + r)$，这样运行时间依赖于输出规模的算法称为输出敏感（output-sensitive）的。若只需计数，$s$ 也可以二分查找求得，只需 $O(\log n)$ 时间，与 $r$ 无关。

### 7.3.2. 平面范围查询与容斥

有序向量的方法无法直接推广到平面：平面上的点没有一个同时适合 $x$ 与 $y$ 两个方向的线性次序。若只考虑计数查询，可以借助容斥原理。对平面上任一点 $(x, y)$，令 $n(x, y)$ 为满足 $p_x \le x$ 且 $p_y \le y$ 的输入点数（被 $(x, y)$ 支配的点数）。对矩形 $[x_1, x_2] \times [y_1, y_2]$ 有

$$
\text{count} = n(x_2, y_2) - n(x_1^-, y_2) - n(x_2, y_1^-) + n(x_1^-, y_1^-),
$$

其中 $x_1^-$ 表示略小于 $x_1$ 的位置。$n(x, y)$ 只在输入点坐标构成的 $(n+1) \times (n+1)$ 个格点处取不同的值，可以预先计算并记录；查询时用二分查找把矩形的四个角吸附到格点上，只需 $O(\log n)$ 时间。代价是 $\Theta(n^2)$ 的预处理时间与空间，而且在 $d$ 维中增长为 $\Theta(n^d)$。要找到可行的方法，还需要重新审视一维的情况。

### 7.3.3. 一维范围查询的树形视角

把 $n$ 个点组织为一棵平衡二叉搜索树，点都存放在叶节点中，每个内部节点保存其左子树中的最大值，作为向左还是向右的分界。`search(x)` 返回不超过 $x$ 的最大者。

查询 $[x_1, x_2]$ 时，分别查找 $x_1$ 与 $x_2$，得到两条从根出发的路径。设两者的最低公共祖先为 $u$（分裂节点）。从 $u$ 出发：

- 沿通往 $x_1$ 的路径下行，每当路径向左转，该节点的右子树整个落在查询范围内，直接报告；向右转则忽略左子树；
- 沿通往 $x_2$ 的路径下行，对称地，每当路径向右转，就报告左子树。

最后检查两条路径末端的叶节点本身。这样，查询结果被表示为 $O(\log n)$ 棵彼此无交的子树之并。树中的每个节点对应 $x$ 轴上的一个区域（其子树中点的范围）：后代的区域包含于祖先的区域，没有祖先-后代关系的两个节点区域无交。查询就是把节点分为三类：整体接受（报告整棵子树）、整体拒绝、需要递归，而需要递归的只有两条路径上的 $O(\log n)$ 个节点，就像"用热刀切 $O(\log n)$ 层的巧克力蛋糕"。

于是一维范围查询需要 $O(n \log n)$ 的预处理时间、$O(n)$ 的空间，查询时间为 $O(\log n + r)$（计数只需 $O(\log n)$，若每个节点记录子树规模）。这种"规范子树分解"正是推广到高维的关键。

## 7.4. 多层搜索树与范围树

### 7.4.1. 多层搜索树

一次二维范围查询可以看作两次一维查询：先找出 $x$ 坐标落在 $[x_1, x_2]$ 内的点，再从中筛选出 $y$ 坐标落在 $[y_1, y_2]$ 内的点。但这样做在最坏情况下很不划算：$x$ 查询可能命中几乎所有的点，$y$ 查询却又排除了几乎所有的点，花费 $\Theta(n)$ 时间却几乎一无所获，不是输出敏感的。

**定义 7.4.1（多层搜索树）** 先按 $x$ 坐标构造一棵一维平衡二叉搜索树（$x$ 树）；然后对 $x$ 树中的每个节点 $v$，把 $v$ 的子树中的点按 $y$ 坐标另外构造一棵平衡二叉搜索树（$y$ 树），并让 $v$ 指向它。$v$ 与它的 $y$ 树对应输入点集的同一子集，只是按不同的方向排序。更高的维度可以照此逐层推广。这样的结构称为**多层搜索树**。

**算法 7.4.1（二维范围查询）** 先在 $x$ 树中做一维查询，找出 $O(\log n)$ 棵规范子树；再在它们各自的 $y$ 树中做一维查询 $[y_1, y_2]$，报告命中的点。

这些 $y$ 查询的输出互不相交，其并恰好就是所需的输出。

**定理 7.4.1** 对平面上任意 $n$ 个点，二层多层搜索树可以在 $O(n \log n)$ 时间内建立，占用 $O(n \log n)$ 空间，每次二维范围查询只需 $O(\log^2 n + r)$ 时间。

**证明** 查询：$x$ 查询用 $O(\log n)$ 时间找出 $O(\log n)$ 棵规范子树，每次 $y$ 查询用 $O(\log n + r_v)$ 时间，合计 $O(\log^2 n + r)$。空间：每个点恰好出现在它的每个祖先的 $y$ 树中，即 $O(\log n)$ 棵 $y$ 树中，总空间 $O(n \log n)$；也可以按深度统计，同一深度的各 $y$ 树合起来恰好包含全部 $n$ 个点。预处理：自底而上逐层构造，每个节点的 $y$ 序列由两个孩子的 $y$ 序列归并得到，不必重新排序，每层合计 $O(n)$ 时间。$\square$

推广到 $d$ 维欧氏空间（$d \ge 2$），$d$ 层的多层搜索树需要 $O(n \log^{d-1} n)$ 的构造时间与空间，每次查询需要 $O(\log^d n + r)$ 时间。

### 7.4.2. 范围树与分散层叠

二维查询中虽然要做 $O(\log n)$ 次 $y$ 查询，它们针对的 $y$ 树各不相同，查询的范围 $[y_1, y_2]$ 却完全相同。让它们各自独立地完成二分查找，浪费了这种相关性。

首先，最后一维的 $y$ 查询不需要再递归，所以 $y$ 树不必是一棵平衡二叉搜索树，一个按 $y$ 坐标排好序的向量即已足够：整个结构是一棵 $x$ 树，每个节点关联一个有序序列。进一步，节点 $v$ 的关联序列恰好是两个孩子的关联序列之并，可以在 $v$ 的序列与两个孩子的序列之间建立快捷引用：$v$ 的序列中每个元素同时记录它在左孩子、右孩子序列中的对应位置（第一个不小于它的元素）。这样，对同一个 $y$ 值，由 $v$ 中的查找结果可以在 $O(1)$ 时间内得到两个孩子中的查找结果。这一技巧称为分散层叠（fractional cascading）。

一次查询只需在分裂节点的序列中二分查找一次（$O(\log n)$），此后沿两条路径下行时，所有后代的 $y$ 查询都只需 $O(1)$ 时间加上输出时间。快捷引用可以在自底而上二路归并的过程中顺便建立，不增加预处理的复杂度。

**定义 7.4.2（范围树）** 引入了分散层叠技术的多层搜索树称为**范围树**（range tree）。也有文献把不带分散层叠的二层结构直接称为范围树。

**定理 7.4.2** 对平面上任意 $n$ 个点，二维范围树可以在 $O(n \log n)$ 时间内建立，占用 $O(n \log n)$ 空间，每次二维范围查询只需 $O(\log n + r)$ 时间。在 $d$ 维空间中（$d \ge 2$），构造时间与空间为 $O(n \log^{d-1} n)$，查询时间为 $O(\log^{d-1} n + r)$。

遗憾的是，分散层叠只能用于最后一个维度，所以高维时只节省了一个 $\log n$ 因子。下面的实现是不带分散层叠的二层结构，$x$ 树用堆式数组存放在按 $x$ 排好序的点上，每个节点的关联序列由归并得到，查询时间为 $O(\log^2 n + r)$。

```cpp tab
#include <algorithm>
#include <format>
#include <iostream>
#include <random>
#include <vector>

// Two-level range tree: a balanced x-tree whose every node keeps its points sorted by y.
// Query [x1, x2] x [y1, y2] in O(log^2 n + r) time; O(n log n) space.
template <typename T>
class RangeTree {
public:
    struct Point { T x, y; int id; };

private:
    std::vector<Point> pts;                         // sorted by x; node v spans pts[lo, hi)
    std::vector<std::vector<Point>> ylist;          // heap layout: node v's points sorted by y

    void build(int v, int lo, int hi) {
        if (hi - lo == 1) { ylist[v] = {pts[lo]}; return; }
        int mid = (lo + hi) / 2;
        build(2 * v, lo, mid);
        build(2 * v + 1, mid, hi);
        auto& a = ylist[2 * v];
        auto& b = ylist[2 * v + 1];
        ylist[v].resize(a.size() + b.size());       // merge the children: no re-sorting
        std::ranges::merge(a, b, ylist[v].begin(), {}, &Point::y, &Point::y);
    }
    template <typename F>
    void query(int v, int lo, int hi, T x1, T x2, T y1, T y2, F& report) const {
        if (pts[hi - 1].x < x1 || x2 < pts[lo].x) return;      // disjoint in x
        if (x1 <= pts[lo].x && pts[hi - 1].x <= x2) {          // canonical subtree: y-query
            auto& ys = ylist[v];
            auto it = std::ranges::lower_bound(ys, y1, {}, &Point::y);
            for (; it != ys.end() && it->y <= y2; ++it) report(*it);
            return;
        }
        int mid = (lo + hi) / 2;                    // partial overlap: recurse
        query(2 * v, lo, mid, x1, x2, y1, y2, report);
        query(2 * v + 1, mid, hi, x1, x2, y1, y2, report);
    }

public:
    explicit RangeTree(std::vector<Point> p) : pts(std::move(p)) {
        std::ranges::sort(pts, {}, &Point::x);
        ylist.resize(4 * pts.size());
        if (!pts.empty()) build(1, 0, static_cast<int>(pts.size()));
    }
    template <typename F> void query(T x1, T x2, T y1, T y2, F&& report) const {
        if (!pts.empty()) query(1, 0, static_cast<int>(pts.size()), x1, x2, y1, y2, report);
    }
};

int main() {
    std::mt19937 rng(11);
    using RT = RangeTree<int>;
    std::vector<RT::Point> p;
    for (int k = 0; k < 3000; ++k)
        p.push_back({static_cast<int>(rng() % 1000), static_cast<int>(rng() % 1000), k});
    RT t(p);
    for (int round = 0; round < 2000; ++round) {
        int x1 = rng() % 1000, x2 = rng() % 1000, y1 = rng() % 1000, y2 = rng() % 1000;
        if (x1 > x2) std::swap(x1, x2);
        if (y1 > y2) std::swap(y1, y2);
        std::vector<int> got, want;
        t.query(x1, x2, y1, y2, [&](const RT::Point& q) { got.push_back(q.id); });
        for (auto& q : p) if (x1 <= q.x && q.x <= x2 && y1 <= q.y && q.y <= y2) want.push_back(q.id);
        std::ranges::sort(got);
        if (got != want) return 1;
    }
    std::cout << "ok\n";
}
```

```python tab
import random
from bisect import bisect_left
from collections.abc import Iterator
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float
    id: int


def merge_by_y(a: list[Point], b: list[Point]) -> list[Point]:
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if b[j].y < a[i].y:
            out.append(b[j]); j += 1
        else:
            out.append(a[i]); i += 1
    return out + a[i:] + b[j:]


class RangeTree:
    """Two-level range tree: x-tree nodes keep their points sorted by y."""

    def __init__(self, points: list[Point]) -> None:
        self.pts = sorted(points, key=lambda p: p.x)   # node v spans pts[lo:hi]
        self.ylist: list[list[Point]] = [[] for _ in range(4 * len(self.pts))]
        self.ykeys: list[list[float]] = [[] for _ in range(4 * len(self.pts))]
        if self.pts:
            self._build(1, 0, len(self.pts))

    def _build(self, v: int, lo: int, hi: int) -> None:
        if hi - lo == 1:
            self.ylist[v] = [self.pts[lo]]
        else:
            mid = (lo + hi) // 2
            self._build(2 * v, lo, mid)
            self._build(2 * v + 1, mid, hi)
            self.ylist[v] = merge_by_y(self.ylist[2 * v], self.ylist[2 * v + 1])
        self.ykeys[v] = [p.y for p in self.ylist[v]]

    def query(self, x1: float, x2: float, y1: float, y2: float) -> Iterator[Point]:
        def rec(v: int, lo: int, hi: int) -> Iterator[Point]:
            if self.pts[hi - 1].x < x1 or x2 < self.pts[lo].x:     # disjoint in x
                return
            if x1 <= self.pts[lo].x and self.pts[hi - 1].x <= x2:  # canonical subtree
                ys = self.ylist[v]
                i = bisect_left(self.ykeys[v], y1)
                while i < len(ys) and ys[i].y <= y2:
                    yield ys[i]
                    i += 1
                return
            mid = (lo + hi) // 2                   # partial overlap: recurse
            yield from rec(2 * v, lo, mid)
            yield from rec(2 * v + 1, mid, hi)

        if self.pts:
            yield from rec(1, 0, len(self.pts))


rng = random.Random(11)
pts = [Point(rng.randrange(1000), rng.randrange(1000), k) for k in range(2000)]
t = RangeTree(pts)
for _ in range(300):
    x1, x2 = sorted((rng.randrange(1000), rng.randrange(1000)))
    y1, y2 = sorted((rng.randrange(1000), rng.randrange(1000)))
    got = sorted(p.id for p in t.query(x1, x2, y1, y2))
    assert got == [p.id for p in pts if x1 <= p.x <= x2 and y1 <= p.y <= y2]
print("ok")
```

## 7.5. kd 树

### 7.5.1. 构造

范围树的查询很快，但 $O(n \log n)$ 的空间（高维时 $O(n \log^{d-1} n)$）在数据量大时是负担。kd 树只用 $O(n)$ 的空间，代价是较慢的查询。它的思路是递归地划分平面，并把划分出来的矩形区域组织为一棵二叉树：根节点对应整个平面，然后交替地按 $x$、$y$ 坐标把区域一分为二，直至每个区域只含一个点。为避免歧义，可约定每个矩形区域都是左闭右开、下闭上开的。

**定义 7.5.1（kd 树）** 对点集 $P$ 与深度 $d$，`buildKdTree(P, d)` 递归地构造二叉树：若 $P$ 只含一个点，返回一个叶节点；否则，$d$ 为偶数时用竖直线、为奇数时用水平线把 $P$ 按相应坐标的中位数分为大致相等的两半 $P_1$、$P_2$，以这条分割线为根，对 $P_1$、$P_2$ 分别以深度 $d + 1$ 递归构造左右子树。这样得到的树称为二维的 **kd 树**（2d-tree）。在 $k$ 维空间中依次沿第 $1, 2, \dots, k$ 维循环切分，就是 $k$ 维的 kd 树。

kd 树有以下性质：

- 每个节点 $v$ 对应平面上的一个矩形区域 $\operatorname{region}(v)$ 及其中的点集；兄弟节点的区域无交，其并是父亲的区域；同一深度的所有节点的区域无缝地覆盖了整个平面。
- 每次划分都使点数减半，树高为 $O(\log n)$；共 $n$ 个叶节点、$n - 1$ 个内部节点，空间为 $O(n)$。
- 用线性时间的选取算法（[4.3.14](/4.3.14)）求中位数，构造时间满足 $T(n) = 2T(n/2) + O(n)$，即 $O(n \log n)$；也可以预先按两个坐标各排序一次，再在递归中线性地分拣。

任何一次矩形查询的解，都可以表示为若干个节点所对应点集的并。

若每次同时按 $x$ 与 $y$ 切分，每个节点就有四个孩子，这就是四叉树（quadtree）。四叉树通常按区域的几何中点而非点的中位数切分，实现直观，在图像处理和网格生成中应用广泛，但它不保证平衡：点分布不均匀时，树可能很深。

### 7.5.2. 查询

**算法 7.5.1（kd 树的范围查询）** `kdSearch(v, R)` 的前提是 $\operatorname{region}(v)$ 与查询矩形 $R$ 的边界相交：

1. 若 $v$ 是叶节点，检查它的点是否在 $R$ 内，是则报告；
2. 对 $v$ 的每个孩子 $c$：若 $\operatorname{region}(c) \subseteq R$，报告 $c$ 的整棵子树；否则若 $\operatorname{region}(c)$ 与 $R$ 相交，递归调用 `kdSearch(c, R)`；否则（无交）剪枝。

实现时不必存储每个节点的区域，只需在递归时由父亲的区域和分割线算出孩子的区域。用点集的包围盒代替区域，往往能更早地判定包含或无交，减少递归次数。

![一棵 64 个点的 2d-tree 与一次矩形查询（虚线）。绿色的区域整体落在查询范围内，其子树被批量报告；只有与查询边界相交的区域才需要递归](./plots/kd-tree-query.py)

```cpp tab
#include <algorithm>
#include <array>
#include <format>
#include <iostream>
#include <random>
#include <vector>

// 2d-tree: split alternately by x and y at the median; leaves hold single points.
template <typename T>
class KdTree {
public:
    struct Point { std::array<T, 2> c; int id; };
    struct Box { std::array<T, 2> lo, hi; };        // closed axis-parallel rectangle

private:
    struct Node { int dim = -1; T split{}; int lc = -1, rc = -1, lo = 0, hi = 0; };
    std::vector<Point> pts;                         // node v owns pts[lo, hi)
    std::vector<Node> nodes;

    int build(int lo, int hi, int depth) {
        int v = static_cast<int>(nodes.size());
        nodes.push_back({-1, T{}, -1, -1, lo, hi});
        if (hi - lo == 1) return v;                 // leaf
        int d = depth % 2, mid = (lo + hi) / 2;
        std::nth_element(pts.begin() + lo, pts.begin() + mid, pts.begin() + hi,
                         [d](const Point& a, const Point& b) { return a.c[d] < b.c[d]; });
        T split = pts[mid].c[d];                    // left coords <= split <= right coords
        int l = build(lo, mid, depth + 1);          // (recursion reorders pts, so save split first)
        int r = build(mid, hi, depth + 1);
        nodes[v] = {d, split, l, r, lo, hi};
        return v;
    }
    static bool inside(const Box& a, const Box& r) {    // a is contained in r
        return r.lo[0] <= a.lo[0] && a.hi[0] <= r.hi[0] && r.lo[1] <= a.lo[1] && a.hi[1] <= r.hi[1];
    }
    static bool meets(const Box& a, const Box& r) {     // a intersects r
        return a.lo[0] <= r.hi[0] && r.lo[0] <= a.hi[0] && a.lo[1] <= r.hi[1] && r.lo[1] <= a.hi[1];
    }
    template <typename F> void search(int v, const Box& region, const Box& r, F& report, int& visits) const {
        ++visits;
        const Node& x = nodes[v];
        if (x.dim < 0) {                            // leaf: check the point itself
            const Point& p = pts[x.lo];
            if (inside(Box{p.c, p.c}, r)) report(p);
            return;
        }
        Box left = region, right = region;          // regions of the two children
        left.hi[x.dim] = x.split;
        right.lo[x.dim] = x.split;
        for (auto [child, box] : {std::pair{x.lc, left}, std::pair{x.rc, right}}) {
            if (inside(box, r))                     // whole subtree inside: report in bulk
                for (int i = nodes[child].lo; i < nodes[child].hi; ++i) report(pts[i]);
            else if (meets(box, r))                 // boundary of r crosses it: recurse
                search(child, box, r, report, visits);
        }
    }

public:
    explicit KdTree(std::vector<Point> p) : pts(std::move(p)) {
        if (!pts.empty()) build(0, static_cast<int>(pts.size()), 0);
    }
    template <typename F> int query(const Box& r, F&& report) const {  // returns #nodes visited
        int visits = 0;
        if (pts.empty()) return 0;
        Box all{{pts[0].c}, {pts[0].c}};            // bounding box of all points
        for (auto& q : pts)
            for (int d = 0; d < 2; ++d) {
                all.lo[d] = std::min(all.lo[d], q.c[d]);
                all.hi[d] = std::max(all.hi[d], q.c[d]);
            }
        if (inside(all, r)) { for (auto& q : pts) report(q); return 1; }
        if (meets(all, r)) search(0, all, r, report, visits);
        return visits;
    }
};

int main() {
    std::mt19937 rng(13);
    using KD = KdTree<int>;
    std::vector<KD::Point> p;
    for (int k = 0; k < 4096; ++k)
        p.push_back({{static_cast<int>(rng() % 1000), static_cast<int>(rng() % 1000)}, k});
    KD t(p);
    long long visits = 0;
    for (int round = 0; round < 2000; ++round) {
        int x1 = rng() % 1000, x2 = rng() % 1000, y1 = rng() % 1000, y2 = rng() % 1000;
        if (x1 > x2) std::swap(x1, x2);
        if (y1 > y2) std::swap(y1, y2);
        std::vector<int> got, want;
        visits += t.query({{x1, y1}, {x2, y2}}, [&](const KD::Point& q) { got.push_back(q.id); });
        for (auto& q : p)
            if (x1 <= q.c[0] && q.c[0] <= x2 && y1 <= q.c[1] && q.c[1] <= y2) want.push_back(q.id);
        std::ranges::sort(got);
        if (got != want) return 1;
    }
    std::cout << std::format("ok: {:.0f} nodes visited per query on average (n = {})\n",
                             visits / 2000.0, p.size());
}
```

```python tab
from __future__ import annotations

import random
from collections.abc import Iterator

type Point = tuple[float, float, int]                # (x, y, id)
type Box = tuple[float, float, float, float]         # closed rectangle (x1, x2, y1, y2)


class KdNode:
    def __init__(self, pts: list[Point], depth: int) -> None:
        self.pts = pts      # points of this subtree, for bulk reports (index ranges would save space)
        self.lc = self.rc = None
        if len(pts) > 1:
            self.dim = depth % 2
            pts = sorted(pts, key=lambda p: p[self.dim])   # (linear-time selection would do)
            mid = len(pts) // 2
            self.split = pts[mid][self.dim]          # left coords <= split <= right coords
            self.lc = KdNode(pts[:mid], depth + 1)
            self.rc = KdNode(pts[mid:], depth + 1)


def inside(a: Box, r: Box) -> bool:
    return r[0] <= a[0] and a[1] <= r[1] and r[2] <= a[2] and a[3] <= r[3]


def meets(a: Box, r: Box) -> bool:
    return a[0] <= r[1] and r[0] <= a[1] and a[2] <= r[3] and r[2] <= a[3]


def search(v: KdNode, region: Box, r: Box) -> Iterator[Point]:
    if v.lc is None:                                # leaf: check the point itself
        x, y, _ = v.pts[0]
        if inside((x, x, y, y), r):
            yield v.pts[0]
        return
    x1, x2, y1, y2 = region
    if v.dim == 0:
        left, right = (x1, v.split, y1, y2), (v.split, x2, y1, y2)
    else:
        left, right = (x1, x2, y1, v.split), (x1, x2, v.split, y2)
    for child, box in ((v.lc, left), (v.rc, right)):
        if inside(box, r):                          # whole subtree inside: report in bulk
            yield from child.pts
        elif meets(box, r):                         # boundary of r crosses it: recurse
            yield from search(child, box, r)


def query(root: KdNode, r: Box) -> Iterator[Point]:
    xs = [p[0] for p in root.pts]
    ys = [p[1] for p in root.pts]
    whole = (min(xs), max(xs), min(ys), max(ys))     # bounding box of all points
    if inside(whole, r):
        yield from root.pts
    elif meets(whole, r):
        yield from search(root, whole, r)


rng = random.Random(13)
pts = [(rng.randrange(1000), rng.randrange(1000), k) for k in range(2000)]
root = KdNode(pts, 0)
for _ in range(300):
    x1, x2 = sorted((rng.randrange(1000), rng.randrange(1000)))
    y1, y2 = sorted((rng.randrange(1000), rng.randrange(1000)))
    got = sorted(p[2] for p in query(root, (x1, x2, y1, y2)))
    assert got == [k for x, y, k in pts if x1 <= x <= x2 and y1 <= y <= y2]
print("ok")
```

### 7.5.3. 复杂度

**定理 7.5.1** 在 $n$ 个点的二维 kd 树上，每次矩形范围查询的时间为 $O(\sqrt{n} + r)$。

**证明** 批量报告整棵子树的时间与其规模成正比，计入 $O(r)$。其余时间正比于递归调用的次数，也就是与 $R$ 的边界相交的区域的个数。$R$ 的边界由四条线段组成，只需估计与其中一条（不妨设为上边界 $N$）相交的区域数，再把 $N$ 放大为一整条水平直线 $\ell$。

记 $Q(n)$ 为 $n$ 个点的 kd 树中与一条水平直线相交的区域数。由父亲推到孩子的思路在这里行不通，要由祖父推到孙子：一个节点按 $x$ 切分时，两个孩子的区域都可能与 $\ell$ 相交；但孩子再按 $y$ 切分，每个孩子的两个孩子中至多一个与水平直线 $\ell$ 相交。所以任一与 $\ell$ 相交的区域，其四个孙子中至多两个也与 $\ell$ 相交，而每个孙子的子树只有约 $n/4$ 个点：

$$
Q(n) = 2 + 2\,Q(n/4) = O(\sqrt{n}).
$$

四条边各贡献 $O(\sqrt{n})$，总计 $O(\sqrt{n} + r)$。$\square$

这个界在最坏情况下是紧的，例如一个很窄的长条形查询区域可能与 $\Theta(\sqrt{n})$ 个区域相交而不含任何点。推广到 $d$ 维，$d$ 维 kd 树可以在 $O(n \log n)$ 时间内构造，占用 $O(n)$ 空间，每次正交范围查询需要 $O(n^{1-1/d} + r)$ 时间：维度越高，相对蛮力的优势越小。kd 树更常见的用途是最近邻查询，例如 SciPy 的 `scipy.spatial.KDTree`（[4.4](/4.4)）；数据库与地理信息系统中处理空间数据则多用面向外存的 R 树。

## 小结

| 问题 | 结构 | 预处理时间 | 空间 | 查询时间 |
|---|---|---|---|---|
| 区间的穿刺查询 | 区间树 | $O(n \log n)$ | $O(n)$ | $O(\log n + r)$ |
| 区间的穿刺查询 | 线段树 | $O(n \log n)$ | $O(n \log n)$ | $O(\log n + r)$ |
| 一维范围查询 | 有序向量或平衡二叉搜索树 | $O(n \log n)$ | $O(n)$ | $O(\log n + r)$ |
| 二维范围计数 | 支配点数表 + 容斥 | $O(n^2)$ | $O(n^2)$ | $O(\log n)$ |
| 二维范围查询 | 多层搜索树 | $O(n \log n)$ | $O(n \log n)$ | $O(\log^2 n + r)$ |
| 二维范围查询 | 范围树（分散层叠） | $O(n \log n)$ | $O(n \log n)$ | $O(\log n + r)$ |
| 二维范围查询 | kd 树 | $O(n \log n)$ | $O(n)$ | $O(\sqrt{n} + r)$ |
