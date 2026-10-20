---
title: Applications of Search Trees
description: Applications of search trees to geometric queries, namely stabbing queries with interval trees, elementary intervals and segment trees, one-dimensional and planar range queries and output sensitivity, multi-level search trees, range trees and fractional cascading, and the construction, querying and complexity of k-d trees.
source_hash: 19bdd8b10232
---

The binary search trees of the previous chapter answer the question "does a given key exist?". Many practical problems ask instead "which data fall within a given range?": which reservations cover three o'clock in the afternoon? Which employees are between 30 and 40 years old and earn between 20,000 and 30,000 a month? Which places lie in a rectangular window on a map? These are basic queries of computational geometry. The data set is relatively static while queries keep arriving (online queries), so it is worth the time to preprocess the data into a suitable structure that makes every query fast.

All the structures in this chapter are built on **balanced binary search trees** ([4.3.6](/4.3.6)), and the core idea is the same throughout: decompose the query range into $O(\log n)$ "canonical" subtrees of the tree, each of which is either entirely reported or entirely excluded, so that only the nodes near the boundary need to be checked one by one. Interval trees and segment trees handle stabbing queries on intervals; range trees and k-d trees handle orthogonal range queries on point sets. Output sensitivity recurs throughout the analysis: reporting $r$ results takes at least $\Omega(r)$ time, so the time of a good query algorithm should have the form $O(f(n) + r)$, where $f(n)$ is much smaller than $n$.

## 7.1. Interval Trees

### 7.1.1. Stabbing Queries

**Definition 7.1.1 (Stabbing Query)** Given a set $S$ of $n$ closed intervals on the $x$-axis, finding all intervals of $S$ that contain a query point $q_x$ is called a **stabbing query**.

The brute-force solution checks every interval, taking $O(n)$ time and making no use of the fact that the interval set is relatively static. If the interval set is preprocessed into an interval tree, each query takes only $O(\log n + r)$ time, where $r$ is the number of intervals reported.

### 7.1.2. Structure

The construction of an interval tree is by **divide and conquer**. Let $P$ be the set of all interval endpoints ($2n$ of them) and take its median $x_{\mathrm{mid}}$; all intervals fall into three classes according to their relation to $x_{\mathrm{mid}}$:

- $S_{\mathrm{left}}$: the intervals lying entirely to the left of $x_{\mathrm{mid}}$;
- $S_{\mathrm{mid}}$: the intervals containing $x_{\mathrm{mid}}$;
- $S_{\mathrm{right}}$: the intervals lying entirely to the right of $x_{\mathrm{mid}}$.

**Definition 7.1.2 (Interval Tree)** Take $x_{\mathrm{mid}}$ as the root and store $S_{\mathrm{mid}}$ at the root node; partition $S_{\mathrm{left}}$ and $S_{\mathrm{right}}$ recursively in the same way, building the left and right subtrees respectively, until no further partition is needed. The set $S_{\mathrm{mid}}$ at a node is stored as two associated lists: the L-list, sorted by left endpoint in increasing order, and the R-list, sorted by right endpoint in decreasing order (both "from the outside in"). The binary tree so obtained is called an **interval tree**.

The endpoints of $S_{\mathrm{left}}$ and of $S_{\mathrm{right}}$ each make up less than half of $P$, so the size of the subproblem at least halves with every level, and the height of the tree is $O(\log n)$. Each interval is stored in exactly one node (at the topmost $x_{\mathrm{mid}}$ it contains), in two copies, so the total space is $O(n)$. If all endpoints are sorted once beforehand, then each level needs only linear time to find the median and to distribute the intervals, and the total construction time is $O(n \log n)$.

### 7.1.3. Querying

**Algorithm 7.1.1 (Stabbing Query on an Interval Tree)** Starting at the root, at the current node $v$:

1. If $q_x < x_{\mathrm{mid}}(v)$: all intervals in $S_{\mathrm{mid}}(v)$ contain $x_{\mathrm{mid}}(v) > q_x$, so they contain $q_x$ if and only if their left endpoint is at most $q_x$. We scan the L-list from the front, report the intervals whose left endpoint is at most $q_x$, and stop at the first one whose left endpoint exceeds $q_x$; then we go into the left subtree.
2. If $q_x > x_{\mathrm{mid}}(v)$: symmetrically, we scan the R-list and then go into the right subtree.
3. If $q_x = x_{\mathrm{mid}}(v)$: we report all intervals in $S_{\mathrm{mid}}(v)$ directly and finish (no interval in either subtree contains $q_x$).

The query descends along a single path from the root and visits $O(\log n)$ nodes. At each node, the successful steps of scanning the associated list are charged to the output and there is at most one failure, so the total time is $O(\log n + r)$.

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

## 7.2. Segment Trees

### 7.2.1. Elementary Intervals and Discretization

Another idea is to discretize the $x$-axis. We sort the endpoints of the $n$ intervals as $p_1 < p_2 < \dots < p_m$ ($m \le 2n$); they divide the $x$-axis into segments: the open intervals $(-\infty, p_1)$, $(p_1, p_2)$, $\dots$, $(p_m, +\infty)$ and (since the intervals are closed) the single points $[p_i, p_i]$, in total $2m + 1$ segments, called *elementary intervals*.

At any position within the same elementary interval, the result of a stabbing query is exactly the same. We can therefore store all elementary intervals in order in a **sorted vector** and let each elementary interval record its query result in advance. A query determines the elementary interval containing $q_x$ by binary search and then outputs the recorded result, taking only $O(\log n + r)$ time. The problem is space: in the worst case, every input interval spans $\Theta(n)$ elementary intervals (for example, $n$ nested intervals), and $\Theta(n^2)$ space is needed in total.

### 7.2.2. Structure

We upgrade the sorted vector to a **balanced binary search tree** whose leaves are the elementary intervals. The scope $R(v)$ of a node $v$ is defined as follows: the scope of a leaf is its elementary interval, and the scope of an internal node is the union of the scopes of its two children, that is, the union of the elementary intervals of all its descendant leaves, a contiguous interval.

If input intervals are recorded only at the leaves they span, the space is still $\Theta(n^2)$. The remedy is to merge greedily: if an interval covers the entire scope of some node, it is recorded only at that node and no longer at its descendants.

**Definition 7.2.1 (Segment Tree)** In the above balanced binary search tree whose leaves are the elementary intervals, each node $v$ records a set $\mathrm{Int}(v)$: an input interval $s$ belongs to $\mathrm{Int}(v)$ if and only if $R(v) \subseteq s$ and $R(\operatorname{parent}(v)) \not\subseteq s$. Such a structure is called a **segment tree**.

**Proposition 7.2.1** Each input interval is recorded in at most $2$ nodes on each level, so the total space of a segment tree is $O(n \log n)$.

**Proof** Suppose an interval $s$ is recorded at three nodes $v_1$, $v_2$, $v_3$ of the same level, from left to right. Since $s$ is a contiguous interval, it covers the entire range from $R(v_1)$ to $R(v_3)$. The sibling of $v_2$ lies on the same level right next to $v_2$, between $v_1$ and $v_3$ (inclusive), so its scope is also covered by $s$; hence $R(\operatorname{parent}(v_2)) \subseteq s$, contradicting $s \in \mathrm{Int}(v_2)$. The height of the tree is $O(\log n)$, so each interval is recorded in at most $O(\log n)$ nodes. $\square$

**Algorithm 7.2.1 (Inserting an Interval)** Starting at the root, run `InsertSeg(v, s)` for the interval $s$: if $R(v) \subseteq s$, record $s$ in $\mathrm{Int}(v)$ and return; otherwise, if $R(\operatorname{lc}(v))$ intersects $s$, recurse on the left child; if $R(\operatorname{rc}(v))$ intersects $s$, recurse on the right child.

On each level, this procedure visits at most $4$ nodes ($2$ that record $s$ and $2$ that continue the recursion), so inserting one interval takes only $O(\log n)$ time. To build a segment tree, we first sort all endpoints ($O(n \log n)$), organize the elementary intervals into a balanced binary tree and compute the scopes of the nodes bottom-up ($O(n)$), and then insert the intervals one by one ($O(n \log n)$).

### 7.2.3. Querying

**Algorithm 7.2.2 (Stabbing Query on a Segment Tree)** Starting at the root, descend to the leaf containing $q_x$, reporting along the way all intervals in $\mathrm{Int}(v)$ of each node $v$.

When $q_x$ lies in $R(v)$, every interval in $\mathrm{Int}(v)$ covers $R(v)$ and hence certainly contains $q_x$; conversely, an interval that contains $q_x$ is necessarily recorded at some node on the path (exactly one of its canonical nodes has a scope containing $q_x$), and only once. One node is visited per level, taking time $O(1 + r_v)$ at node $v$, so the total time is $O(\log n + r)$.

**Theorem 7.2.2** Given $n$ intervals on the $x$-axis, a segment tree occupying $O(n \log n)$ space can be built in $O(n \log n)$ time, and with it each stabbing query can be answered in $O(\log n + r)$ time.

The implementation below stores this completely balanced tree in a heap-style array (the children of node $v$ are $2v$ and $2v + 1$), and numbers the leaves in order: leaf $2i$ is the open interval to the left of $p_i$, and leaf $2i + 1$ is the single point $p_i$.

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

Compared with interval trees, segment trees use an extra factor of $\log n$ in space, but they are more general: the $\mathrm{Int}(v)$ of each node can be replaced by another structure, which supports counting queries and weighted queries, or a search tree on the second dimension can be nested inside to handle line segments in the plane (window queries).

The "segment tree" often mentioned in programming contests is another use of the same skeleton: the leaves are the indices of an array, and each node stores an aggregate (sum, minimum, and so on) over its index range; any index interval can be decomposed into the scopes of $O(\log n)$ nodes, so range sums and range updates (with lazy tags) take only $O(\log n)$ time.

## 7.3. Range Queries

### 7.3.1. One-Dimensional Range Queries

**Definition 7.3.1 (Range Query)** Given a point set $P$ and a query range $R$ (an interval $[x_1, x_2]$ in one dimension, and in $d$ dimensions a product of intervals, one per dimension, called an orthogonal range), counting how many points of $P$ fall in $R$ (a counting query) or listing these points (a reporting query) is called a **range query**.

Usually $P$ is relatively static while $R$ keeps changing. The brute-force algorithm checks every point and takes $O(n)$ time. In the worst case $\Theta(n)$ points are hit, and even just listing them takes $\Theta(n)$ time, so judged by the worst case alone, brute force cannot be improved. But if we separate searching from reporting, we can do better.

We preprocess all points into a **sorted vector** (with a **sentinel node** $p_0$ of value $-\infty$ placed at the front). To answer the query $[x_1, x_2]$, we determine $t = \max\{i : p_i \le x_2\}$ by binary search and then traverse backward from $p_t$ until some $p_s$ falls outside the query interval; the points in $(s, t]$ are exactly the output. The query time is $O(\log n + r)$; an algorithm whose running time depends on the size of the output in this way is called *output-sensitive*. If only the count is needed, $s$ can also be found by binary search, taking only $O(\log n)$ time, independent of $r$.

### 7.3.2. Planar Range Queries and Inclusion–Exclusion

The method of the sorted vector does not generalize directly to the plane: there is no linear order on the points of the plane suitable for both the $x$ and $y$ directions. If we consider only counting queries, we can use the inclusion–exclusion principle. For a point $(x, y)$ in the plane, let $n(x, y)$ be the number of input points with $p_x \le x$ and $p_y \le y$ (the number of points dominated by $(x, y)$). For the rectangle $[x_1, x_2] \times [y_1, y_2]$ we have

$$
\text{count} = n(x_2, y_2) - n(x_1^-, y_2) - n(x_2, y_1^-) + n(x_1^-, y_1^-),
$$

where $x_1^-$ denotes a position slightly smaller than $x_1$. The function $n(x, y)$ takes different values only at the $(n+1) \times (n+1)$ grid points formed by the coordinates of the input points, so it can be precomputed and stored; at query time, the four corners of the rectangle are snapped to grid points by binary search, taking only $O(\log n)$ time. The price is $\Theta(n^2)$ preprocessing time and space, which grows to $\Theta(n^d)$ in $d$ dimensions. To find a feasible method, we must revisit the one-dimensional case.

### 7.3.3. A Tree View of One-Dimensional Range Queries

We organize the $n$ points into a balanced binary search tree with all points stored in the leaves; each internal node stores the maximum of its left subtree, which serves as the boundary between going left and going right. `search(x)` returns the largest element not exceeding $x$.

To answer the query $[x_1, x_2]$, we search for $x_1$ and $x_2$ separately, obtaining two paths from the root. Let $u$ be their lowest common ancestor (the split node). Starting from $u$:

- we descend along the path toward $x_1$; whenever the path turns left, the right subtree of that node lies entirely within the query range and is reported directly; when it turns right, the left subtree is ignored;
- we descend along the path toward $x_2$; symmetrically, whenever the path turns right, the left subtree is reported.

Finally we check the leaves at the ends of the two paths themselves. The query result is thus expressed as the union of $O(\log n)$ pairwise disjoint subtrees. Each node of the tree corresponds to a region of the $x$-axis (the range of the points in its subtree): the region of a descendant is contained in that of its ancestor, and the regions of two nodes without an ancestor-descendant relation are disjoint. A query classifies nodes into three kinds: fully accepted (the whole subtree is reported), fully rejected, and requiring recursion; only $O(\log n)$ nodes on the two paths require recursion, as if "cutting through the $O(\log n)$ layers of a chocolate cake with a hot knife".

One-dimensional range queries thus need $O(n \log n)$ preprocessing time and $O(n)$ space, and the query time is $O(\log n + r)$ (counting needs only $O(\log n)$ if each node records the size of its subtree). This "canonical subtree decomposition" is exactly the key to generalizing to higher dimensions.

## 7.4. Multi-Level Search Trees and Range Trees

### 7.4.1. Multi-Level Search Trees

A two-dimensional range query can be viewed as two one-dimensional queries: first find the points whose $x$-coordinates lie in $[x_1, x_2]$, then filter out of them those whose $y$-coordinates lie in $[y_1, y_2]$. But in the worst case this is wasteful: the $x$-query may hit almost all points while the $y$-query then excludes almost all of them, spending $\Theta(n)$ time and gaining almost nothing, which is not output-sensitive.

**Definition 7.4.1 (Multi-Level Search Tree)** First build a one-dimensional balanced binary search tree on the $x$-coordinates (the $x$-tree); then, for each node $v$ of the $x$-tree, build another balanced binary search tree on the $y$-coordinates of the points in the subtree of $v$ (the $y$-tree) and let $v$ point to it. The node $v$ and its $y$-tree correspond to the same subset of the input points, only sorted in different directions. Higher dimensions generalize level by level in the same way. Such a structure is called a **multi-level search tree**.

**Algorithm 7.4.1 (Two-Dimensional Range Query)** First perform a one-dimensional query in the $x$-tree to find $O(\log n)$ canonical subtrees; then perform the one-dimensional query $[y_1, y_2]$ in each of their $y$-trees and report the points hit.

The outputs of these $y$-queries are pairwise disjoint, and their union is exactly the required output.

**Theorem 7.4.1** For any $n$ points in the plane, a two-level multi-level search tree can be built in $O(n \log n)$ time and occupies $O(n \log n)$ space, and each two-dimensional range query takes only $O(\log^2 n + r)$ time.

**Proof** Query: the $x$-query finds $O(\log n)$ canonical subtrees in $O(\log n)$ time, and each $y$-query takes $O(\log n + r_v)$ time, in total $O(\log^2 n + r)$. Space: each point appears in the $y$-tree of each of its ancestors, that is, in $O(\log n)$ $y$-trees, for a total space of $O(n \log n)$; alternatively, counting by depth, the $y$-trees at the same depth together contain exactly all $n$ points. Preprocessing: we build level by level from the bottom up, and the $y$-sequence of each node is obtained by merging the $y$-sequences of its two children without resorting, taking $O(n)$ time per level in total. $\square$

Generalizing to $d$-dimensional Euclidean space ($d \ge 2$), a $d$-level multi-level search tree needs $O(n \log^{d-1} n)$ construction time and space, and each query needs $O(\log^d n + r)$ time.

### 7.4.2. Range Trees and Fractional Cascading

Although a two-dimensional query performs $O(\log n)$ $y$-queries, they are directed at different $y$-trees while the query range $[y_1, y_2]$ is exactly the same. Letting each of them carry out its own binary search independently wastes this correlation.

First, the $y$-query in the last dimension needs no further recursion, so the $y$-tree need not be a balanced binary search tree; a **vector** sorted by $y$-coordinate suffices. The whole structure is then an $x$-tree with a sorted sequence attached to each node. Furthermore, the sequence attached to a node $v$ is exactly the union of the sequences of its two children, so shortcut references can be set up between the sequence of $v$ and the sequences of its two children: each element in the sequence of $v$ records also its corresponding positions in the sequences of the left and right children (the first element not smaller than it). Thus, for the same $y$ value, the search result in $v$ yields the search results in both children in $O(1)$ time. This technique is called *fractional cascading*.

A query needs only one binary search in the sequence of the split node ($O(\log n)$); afterward, when descending along the two paths, the $y$-query at every descendant takes only $O(1)$ time plus output time. The shortcut references can be built on the fly during the bottom-up two-way merging without increasing the complexity of preprocessing.

**Definition 7.4.2 (Range Tree)** A multi-level search tree that incorporates fractional cascading is called a **range tree**. Some of the literature also calls the two-level structure without fractional cascading a range tree.

**Theorem 7.4.2** For any $n$ points in the plane, a two-dimensional range tree can be built in $O(n \log n)$ time and occupies $O(n \log n)$ space, and each two-dimensional range query takes only $O(\log n + r)$ time. In $d$-dimensional space ($d \ge 2$), the construction time and space are $O(n \log^{d-1} n)$ and the query time is $O(\log^{d-1} n + r)$.

Unfortunately, fractional cascading applies only to the last dimension, so in high dimensions it saves only one factor of $\log n$. The implementation below is the two-level structure without fractional cascading: the $x$-tree is stored as a heap-style array over the points sorted by $x$, the associated sequence of each node is obtained by merging, and the query time is $O(\log^2 n + r)$.

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

## 7.5. k-d Trees

### 7.5.1. Construction

Range trees answer queries quickly, but the $O(n \log n)$ space (and $O(n \log^{d-1} n)$ in high dimensions) is a burden for large data sets. A k-d tree uses only $O(n)$ space, at the price of slower queries. Its idea is to partition the plane recursively and organize the resulting rectangular regions into a binary tree: the root corresponds to the whole plane, and the regions are then split in two alternately by the $x$ and $y$ coordinates until each region contains a single point. To avoid ambiguity, we may stipulate that every rectangular region is closed on the left and open on the right, closed at the bottom and open at the top.

**Definition 7.5.1 (k-d Tree)** For a point set $P$ and a depth $d$, `buildKdTree(P, d)` constructs a binary tree recursively: if $P$ contains only one point, it returns a leaf node; otherwise, when $d$ is even it splits $P$ by a vertical line, and when $d$ is odd by a horizontal line, at the median of the corresponding coordinate, into two roughly equal halves $P_1$, $P_2$; this splitting line becomes the root, and the left and right subtrees are built recursively from $P_1$ and $P_2$ with depth $d + 1$. The tree so obtained is called a two-dimensional **k-d tree** (2d-tree). In $k$-dimensional space, cycling through dimensions $1, 2, \dots, k$ for the splits gives a $k$-dimensional k-d tree.

A k-d tree has the following properties:

- Each node $v$ corresponds to a rectangular region $\operatorname{region}(v)$ of the plane and the point set in it; the regions of siblings are disjoint, and their union is the region of the parent; the regions of all nodes at the same depth cover the whole plane without gaps.
- Every split halves the number of points, so the height of the tree is $O(\log n)$; there are $n$ leaves and $n - 1$ internal nodes, and the space is $O(n)$.
- If the median is found by a linear-time selection algorithm ([4.3.14](/4.3.14)), the construction time satisfies $T(n) = 2T(n/2) + O(n)$, that is, $O(n \log n)$; alternatively, the points can be sorted once by each coordinate beforehand and then distributed linearly during the recursion.

The answer to any rectangular query can be expressed as the union of the point sets of several nodes.

If each split cuts along both $x$ and $y$ at once, every node has four children, and this is the *quadtree*. A quadtree usually splits at the geometric midpoint of a region rather than at the median of the points; it is intuitive to implement and widely used in image processing and mesh generation, but it does not guarantee balance: when the points are unevenly distributed, the tree can be very deep.

### 7.5.2. Querying

**Algorithm 7.5.1 (Range Query on a k-d Tree)** `kdSearch(v, R)` assumes that $\operatorname{region}(v)$ intersects the boundary of the query rectangle $R$:

1. If $v$ is a leaf, check whether its point lies in $R$ and report it if so;
2. For each child $c$ of $v$: if $\operatorname{region}(c) \subseteq R$, report the entire subtree of $c$; otherwise, if $\operatorname{region}(c)$ intersects $R$, call `kdSearch(c, R)` recursively; otherwise (no intersection), prune.

In the implementation, there is no need to store the region of each node; the region of a child can be computed during the recursion from the region of the parent and the splitting line. Replacing regions by the bounding boxes of the point sets often decides containment or disjointness earlier and reduces the number of recursive calls.

![A 2d-tree on 64 points and a rectangle query (dashed). Green regions lie entirely inside the query range, and their subtrees are reported in bulk; only the regions that intersect the query boundary need recursion](./plots/kd-tree-query.py)

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

### 7.5.3. Complexity

**Theorem 7.5.1** On a two-dimensional k-d tree with $n$ points, each rectangular range query takes $O(\sqrt{n} + r)$ time.

**Proof** The time for reporting an entire subtree in bulk is proportional to its size and is charged to $O(r)$. The remaining time is proportional to the number of recursive calls, that is, to the number of regions that intersect the boundary of $R$. The boundary of $R$ consists of four line segments, so it suffices to estimate the number of regions that intersect one of them (say the upper boundary $N$) and then extend $N$ to a whole horizontal line $\ell$.

Let $Q(n)$ be the number of regions of a k-d tree with $n$ points that intersect a horizontal line. Passing from parent to child does not work here; we must pass from grandparent to grandchild: when a node splits by $x$, the regions of both children may intersect $\ell$; but when each child then splits by $y$, at most one of its two children intersects the horizontal line $\ell$. So of the four grandchildren of any region that intersects $\ell$, at most two also intersect $\ell$, and the subtree of each grandchild has only about $n/4$ points:

$$
Q(n) = 2 + 2\,Q(n/4) = O(\sqrt{n}).
$$

Each of the four sides contributes $O(\sqrt{n})$, for a total of $O(\sqrt{n} + r)$. $\square$

This bound is tight in the worst case; for example, a very narrow, long query region may intersect $\Theta(\sqrt{n})$ regions without containing any point. Generalizing to $d$ dimensions, a $d$-dimensional k-d tree can be built in $O(n \log n)$ time and occupies $O(n)$ space, and each orthogonal range query needs $O(n^{1-1/d} + r)$ time: the higher the dimension, the smaller the advantage over brute force. The more common use of k-d trees is nearest-neighbor search, for example SciPy's `scipy.spatial.KDTree` ([4.4](/4.4)); for spatial data, databases and geographic information systems mostly use the external-memory R-tree.

## Summary

| Problem | Structure | Preprocessing time | Space | Query time |
|---|---|---|---|---|
| Stabbing query on intervals | Interval tree | $O(n \log n)$ | $O(n)$ | $O(\log n + r)$ |
| Stabbing query on intervals | Segment tree | $O(n \log n)$ | $O(n \log n)$ | $O(\log n + r)$ |
| One-dimensional range query | Sorted vector or balanced binary search tree | $O(n \log n)$ | $O(n)$ | $O(\log n + r)$ |
| Two-dimensional range counting | Table of dominated-point counts + inclusion–exclusion | $O(n^2)$ | $O(n^2)$ | $O(\log n)$ |
| Two-dimensional range query | Multi-level search tree | $O(n \log n)$ | $O(n \log n)$ | $O(\log^2 n + r)$ |
| Two-dimensional range query | Range tree (fractional cascading) | $O(n \log n)$ | $O(n \log n)$ | $O(\log n + r)$ |
| Two-dimensional range query | k-d tree | $O(n \log n)$ | $O(n)$ | $O(\sqrt{n} + r)$ |
