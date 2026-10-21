---
title: 索引
description: 数据库系统的索引结构：搜索码、聚集索引与辅助索引、稠密索引与稀疏索引、多级索引；B+ 树索引的高度界、查找、带分裂的插入（可运行的实现）、删除，及其在 PostgreSQL、InnoDB 和 SQLite 中的工程实现；静态散列与可扩展散列；LSM 树、压实与 Bloom 过滤器；位图索引、GIN、GiST 与 BRIN 索引；CREATE INDEX 与物理设计，附 SQLite 中实测的执行计划。
source_hash: dfae1165eb24
---

文件组织（[4.13.7](/4.13.7)）至多只能很好地支持一种访问路径：**堆文件**适合扫描，按 `sample_id` 排序的文件适合关于样本的查询。查询还有许多其他查找行的方式：某个基因的全部测量、17 号染色体上两个位置之间的基因、三月份采集的样本。索引是一种辅助结构，它把某些**属性**的值映射到匹配记录的位置，使这样的查询只读几个**页**而不是整张表。本章先固定索引的术语，再研究 B+ 树（几乎每个关系系统默认使用的索引结构），接着是散列、写密集型系统的日志结构合并树、位图索引和 PostgreSQL 的专用索引类型。最后讨论实际问题，即创建哪些索引，这是数据库物理设计的核心。数据结构本身已在 [4.3](/4.3) 中介绍：B 树及 B+ 树变体见 [4.3.8](/4.3.8#sec-8.2)，散列表见 [4.3.9](/4.3.9)。这里把它们看作驻留在磁盘上、以页为单位的结构，并讨论使它们在 DBMS 中可用的工程实现。优化器如何在索引与扫描之间选择是 [4.13.9](/4.13.9) 的主题；并发事务下如何保持索引一致，在 [4.13.11](/4.13.11) 中略有涉及。

## 8.1. 基本概念

### 8.1.1. 搜索码与索引类型

**定义 8.1.1（索引）** 设 $r$ 是关系，$K$ 是 $r$ 的一个属性列表，即**搜索码**（不一定是 $r$ 的码）。$r$ 上以 $K$ 为搜索码的**索引**是一种数据结构，它与 $r$ 分开存放，或作为 $r$ 的文件组织，对给定的 $K$ 值或值的范围，返回 $r$ 中具有这些值的记录的位置（记录标识符或主码值）。索引中存放的（搜索码值，位置）对称为它的**索引项**。

“码”这个词有多重含义：**搜索码**是查询用来查找的任意属性列表，而 [4.13.2](/4.13.2) 意义下的**关系**的码则是数据的性质。`measurement(gene_id)` 上的索引的搜索码不是码：每个值对每个样本出现一次。

**定义 8.1.2（聚集索引与辅助索引）** 若文件的记录按某个索引的搜索码顺序存储，则该索引是**聚集索引**（也称*主索引*）；否则它是**辅助索引**（也称*非聚集索引*）。一个文件至多有一个聚集索引，可以有任意多个辅助索引。

这一区别决定范围查询的代价。通过**聚集索引**，码在某个范围内的记录占据连续的**页**，取 $m$ 条匹配记录约需 $m / f$ 次页读，其中 $f$ 是每页的记录数。通过**辅助索引**，相邻的索引项指向散布在文件各处的记录，取 $m$ 条记录可能多达 $m$ 次页读，每条记录一次。对大的 $m$，这比扫描文件糟糕得多（§8.6.2）。

**定义 8.1.3（稠密索引与稀疏索引）** 若索引对文件中出现的每个搜索码值（对辅助索引：每条记录）都有一个索引项，则称它是**稠密**的；若只对部分值有索引项，通常是文件每个页的第一个码，则称它是**稀疏**的。

稀疏**索引**只可能是聚集索引：要找码 $k$，先找 $\le k$ 的最大**索引项**，再从它指向的页起向前扫描文件。稀疏索引很小，每页一项而不是每条记录一项，这对树的上层很重要。辅助索引必须是稠密的，因为文件的顺序对码在哪里毫无提示。若辅助索引的搜索码不唯一，则它的索引项要么每条记录重复一次码，要么把码存一次并附上**记录标识符**的列表（*倒排列表*，posting list）；PostgreSQL 在 13 版引入的 B 树*去重*（deduplication）自动做后者。

评价索引看它支持的访问类型（等值查找、范围查找、有序输出、前缀查找）、查找的代价、插入和删除的代价，以及所需的空间。

### 8.1.2. 多级索引

大文件上的索引本身也很大。对 500,000 条记录、每项 20 字节的稠密索引，要占约 2,500 个 4 KiB 的页；对它做**二分查找**需要 $\lceil \log_2 2500 \rceil = 12$ 次页读。补救办法是把索引看作排序文件，在它上面再建稀疏索引，如此继续，直到最顶层能放进一个页。每个索引页有 $f$ 项时，每一层把页数缩小到 $1/f$，所以 $N$ 个索引项的层数是 $\lceil \log_f N \rceil$，而不是页数的 $\log_2$。对 $f = 200$ 和 $N = 500{,}000$，层数为 3，最上面的一两层总在**缓冲池**中。静态多级索引在插入下难以维护；**B+ 树**是这一思想的动态版本。

## 8.2. B+ 树索引

### 8.2.1. 结构

**B+ 树**在 [4.3.8](/4.3.8#sec-8.2.7) 中作为**B 树**的一种变体引入，其中所有的码都存放在叶子中，叶子相互链接。作为**数据库**的**索引**，每个结点是一个页，重要的参数是扇出，即内部结点的孩子数，数量级在几百。

**定义 8.2.1（B+ 树）** $n$ 阶 B+ 树（$n \ge 3$）是一棵有根树，所有叶子在同一深度，并且：

1. 每个内部结点含 $k - 1$ 个搜索码值 $K_1 < K_2 < \dots < K_{k-1}$ 和 $k$ 个孩子指针 $P_1, \dots, P_k$，其中 $\lceil n/2 \rceil \le k \le n$，只有根例外，根满足 $2 \le k \le n$。$P_1$ 的**子树**中所有码 $< K_1$，$P_i$（$1 < i < k$）的子树中所有码 $\ge K_{i-1}$ 且 $< K_i$，$P_k$ 的子树中所有码 $\ge K_{k-1}$。
2. 每个叶子含 $\lceil (n-1)/2 \rceil$ 到 $n - 1$ 个按码排序的索引项（搜索码值和记录位置），只有叶子是根时例外，此时可含 0 到 $n - 1$ 个。
3. 每个叶子有一个指向按码顺序的下一个叶子的指针。

内部结点构成叶子之上的稀疏多级索引，叶子构成文件上的稠密索引（对**索引组织表**，叶子就包含记录本身，[4.13.7](/4.13.7#sec-7.4.3)）。占用条件，即每个非根结点至少半满，使树保持较矮。

**定理 8.2.1（B+ 树的高度）** 设 $n \ge 3$ 阶 B+ 树含 $N \ge 1$ 个索引项，$h$ 为层数（从根到叶子的路径上的结点数）。则

$$
\left\lceil \frac{n}{2} \right\rceil^{h-1} \le N, \qquad\text{即}\qquad h \le 1 + \log_{\lceil n/2 \rceil} N.
$$

**证明** 记 $d = \lceil n/2 \rceil$，$l = \lceil (n-1)/2 \rceil$。$h = 1$ 时断言即 $1 \le N$。$h \ge 2$ 时，根至少有 2 个孩子，其他每个内部结点至少有 $d$ 个孩子，所以第 $j$ 层（$1 \le j \le h$，根为第 1 层）当 $j \ge 2$ 时至少有 $2 d^{j-2}$ 个结点；特别地，至少有 $2 d^{h-2}$ 个叶子。每个叶子都不是根，至少含 $l$ 个项，所以 $N \ge 2 l\, d^{h-2}$。最后，对 $n \ge 3$ 有 $2l \ge n - 1 \ge \frac{n+1}{2} \ge d$，故 $N \ge d^{h-1}$。$\square$

**例 8.2.1** 在 PostgreSQL 中，`bigint` 码的一个**索引项**约占 20 字节（8 字节的索引**元组**头、8 字节的码和 4 字节的行指针），所以一个 8 KiB 的**页**约容纳 400 项；建索引时叶子填到 90%（默认的 `fillfactor`），随机插入后平均约 70% 满，所以取有效扇出 300。于是三层索引 $300^3 = 2.7 \times 10^7$ 行，四层索引 $8.1 \times 10^9$ 行。根和第二层共 1 + 300 个页几乎总是在缓存中，所以在数十亿行的表中做一次点查找，在索引中只需一两次页读，再加记录的一次。

### 8.2.2. 查找

要找码为 $v$ 的项，从根开始；在码为 $K_1, \dots, K_{k-1}$ 的内部结点中，沿指针 $P_i$ 前进，其中 $i$ 是 $\le v$ 的码的个数加一；到了叶子，在其中查找 $v$。对范围 $[a, b]$，先查找 $a$，再沿叶子链前进，直到某个码超过 $b$。一次查找的代价是下降过程的 $h$ 次页读，加上范围内每 $f$ 个后续项一个叶子，再加上读记录的次数。

### 8.2.3. 插入

插入先找到该码所属的叶子，并按序插入该项。若叶子溢出（会含 $n$ 项），就对它做*分裂*：前 $\lceil n/2 \rceil$ 项留下，其余移到新的右兄弟，新叶子的最小码连同指向新叶子的指针被*复制*到父结点中。若父结点溢出（有 $n + 1$ 个孩子），也要分裂，但中间的码是*上移*而不是复制，因为内部的码只用来引导查找。根的分裂创建有两个孩子的新根；这是树增高的唯一方式，所以所有叶子保持在同一深度。这些分裂就是 B 树的分裂（[4.3.8](/4.3.8#sec-8.2.4)），唯一的差别是复制与上移的区别。

下面是 $n = 4$（每个叶子至多 3 项、每个内部结点至多 4 个孩子）的实现，它在某些插入之后逐层打印整棵树。

```python
from bisect import bisect_left, bisect_right

N = 4  # maximum number of children of a node; a leaf holds at most N - 1 keys


class Node:
    def __init__(self, leaf):
        self.leaf = leaf
        self.keys = []
        self.children = []   # child nodes (internal) or record ids (leaf)
        self.next = None     # right sibling (leaves only)


class BPlusTree:
    def __init__(self):
        self.root = Node(leaf=True)

    def _find_leaf(self, key):
        node, path = self.root, []
        while not node.leaf:
            path.append(node)
            node = node.children[bisect_right(node.keys, key)]
        return node, path

    def search(self, key):
        leaf, _ = self._find_leaf(key)
        i = bisect_left(leaf.keys, key)
        return leaf.children[i] if i < len(leaf.keys) and leaf.keys[i] == key else None

    def range(self, lo, hi):
        """Yield (key, rid) for lo <= key <= hi by walking the leaf chain."""
        leaf, _ = self._find_leaf(lo)
        while leaf is not None:
            for k, rid in zip(leaf.keys, leaf.children):
                if k > hi:
                    return
                if k >= lo:
                    yield k, rid
            leaf = leaf.next

    def insert(self, key, rid):
        leaf, path = self._find_leaf(key)
        i = bisect_left(leaf.keys, key)
        leaf.keys.insert(i, key)
        leaf.children.insert(i, rid)
        if len(leaf.keys) < N:
            return
        # split the leaf; the first key of the new right leaf is COPIED up
        right = Node(leaf=True)
        mid = (len(leaf.keys) + 1) // 2
        right.keys, leaf.keys = leaf.keys[mid:], leaf.keys[:mid]
        right.children, leaf.children = leaf.children[mid:], leaf.children[:mid]
        right.next, leaf.next = leaf.next, right
        self._insert_in_parent(path, leaf, right.keys[0], right)

    def _insert_in_parent(self, path, left, key, right):
        if not path:                      # the root was split: grow a level
            self.root = Node(leaf=False)
            self.root.keys, self.root.children = [key], [left, right]
            return
        parent = path.pop()
        i = parent.children.index(left)
        parent.keys.insert(i, key)
        parent.children.insert(i + 1, right)
        if len(parent.children) <= N:
            return
        # split the internal node; the middle key is PUSHED up (not kept)
        mid = len(parent.keys) // 2
        up = parent.keys[mid]
        sibling = Node(leaf=False)
        sibling.keys, parent.keys = parent.keys[mid + 1:], parent.keys[:mid]
        sibling.children, parent.children = parent.children[mid + 1:], parent.children[:mid + 1]
        self._insert_in_parent(path, parent, up, sibling)

    def show(self):
        level = [self.root]
        while level:
            print("   ".join("[" + " ".join(map(str, n.keys)) + "]" for n in level))
            level = [] if level[0].leaf else [c for n in level for c in n.children]


t = BPlusTree()
for k in [10, 20, 5, 6, 12, 30, 7, 17, 3, 25, 8, 9]:
    t.insert(k, f"rid{k}")
    if k in (6, 30, 25, 9):
        print(f"after inserting {k}:")
        t.show()
print("search(12) ->", t.search(12), "  search(13) ->", t.search(13))
print("range(6, 20) ->", [k for k, _ in t.range(6, 20)])
```

```text
after inserting 6:
[10]
[5 6]   [10 20]
after inserting 30:
[10 20]
[5 6]   [10 12]   [20 30]
after inserting 25:
[6 10 20]
[3 5]   [6 7]   [10 12 17]   [20 25 30]
after inserting 9:
[10]
[6 8]   [20]
[3 5]   [6 7]   [8 9]   [10 12 17]   [20 25 30]
search(12) -> rid12   search(13) -> None
range(6, 20) -> [6, 7, 8, 9, 10, 12, 17, 20]
```

第四个码 6 使唯一的叶子 `[5 6 10 20]` 溢出，它分裂为 `[5 6]` 和 `[10 20]`；码 10 被复制到新的根中。插入 9 使叶子 `[6 7 8]` 溢出；码 8 被复制到根 `[6 10 20]` 中，于是它有五个孩子并分裂：`[6 8]` 和 `[20]` 成为内部结点，中间的码 10 移入新的根，树因此增长到三层。码 10 现在出现在根和一个叶子中，但不在其他任何内部结点中。

### 8.2.4. 删除

删除从叶子中去掉该项。若叶子低于最小占用，它要么从兄弟那里*借*项（重新分配，这会改变父结点中的分隔码），要么与兄弟*合并*（这会从父结点中去掉一个码和指针，可能使父结点转而下溢）。若根只剩一个孩子，这个孩子成为新的根，高度减一。

实际系统会放宽这些规则。结点一低于半满就合并，当插入和删除在边界附近交替出现时会引起反复的分裂与合并，也会使并发复杂化。PostgreSQL 从不合并部分满的 B 树页；它只在页完全变空时才删除它，失效的项由 `VACUUM` 清理，或在页本来要分裂时顺带清理。空间因此是随时间回收的，而不是立即回收，遭受大量删除的索引可以用 `REINDEX` 重建。

### 8.2.5. 实际系统中的 B+ 树

教科书的结构在许多方面得到了改进：

- *重复值。* 不唯一的**搜索码**通过在码后附加**记录标识符**而变得唯一，使每一项有明确的位置；PostgreSQL 还把相等码的一串项连同倒排列表只存一次（去重）。
- *复合码。* $(A, B)$ 上的索引按字典序排序：先按 $A$，$A$ 相等时再按 $B$。它支持关于 $A$、关于 $A$ 和 $B$ 的条件，以及 $A = a$ 加上 $B$ 的范围的条件，并按 $(A, B)$ 的顺序返回行。仅关于 $B$ 的条件不决定一个连续的范围；*跳跃扫描*（skip scan）把它看作对 $A$ 的每个不同值各做一次范围查找，当 $A$ 的不同值很少时是划算的。SQLite 早就这样做（见 §8.6.2），PostgreSQL 18 增加了 B 树跳跃扫描。
- *覆盖索引与仅索引扫描。* 若查询需要的每一列都在索引中，就根本不必读记录。PostgreSQL 的 `CREATE INDEX ... INCLUDE (...)`（自 11 版起）为此把额外的非码列存放在叶子中；仅索引扫描仍要查询可见性映射（[4.13.7](/4.13.7#sec-7.4.1)），以知道**堆**页上的行版本是否对每个事务都可见。
- *压缩。* 内部结点的码只需区分它们的子树，所以可以截断（*后缀截断*）；叶子的码共享前缀（*前缀压缩*）。两者都能提高扇出。
- *批量加载。* 逐项插入来建索引会引起随机 I/O 和半满的页。`CREATE INDEX` 改为对项排序（用 [4.13.9](/4.13.9#sec-9.4) 的外部排序）并自底向上建树，把叶子顺序填到填充因子，再由下一层的第一个码创建每个内部层。
- *并发。* 对 B+ 树的操作在页上持有短期的闩锁（不是事务锁，见 [4.13.11](/4.13.11)），并使用*闩锁耦合*（latch coupling）：先闩住孩子，再释放它的父结点。PostgreSQL 实现了 Lehman–Yao 的 *B-link 树*，其中每个结点还存放一个右链接和一个高码，使读者到达一个刚被另一进程分裂的结点时，可以沿右链接恢复。
- *索引组织表上的辅助索引。* 在 InnoDB 中，辅助索引项存放主码，而不是页地址；查找先下降辅助索引，再下降聚集索引。于是记录在分裂时可以在页之间移动而不必更新辅助索引，代价是每次查找多一次下降。

## 8.3. 散列索引

### 8.3.1. 静态散列

散列**索引**把它的项存放在*桶*中，每个桶是一个**页**（满时带一串溢出页），**散列函数** $h$ 把搜索码值映射到桶号。等值查找读一个桶及其溢出链；插入和删除同样只触及一个桶。这就是磁盘上的**链地址法**（[4.3.9](/4.3.9#sec-9.3)），页相当于链表结点。

散列索引不支持范围查询或有序输出，因为 $h$ 破坏了码的顺序。桶数 $B$ 固定（*静态散列*）时，文件增大则溢出链变长，文件缩小则空间浪费；像内存**散列表**那样把一切重新散列到更大的表中，意味着一次性重写整个索引。动态散列方案则逐步增长表。

### 8.3.2. 可扩展散列

**定义 8.3.1（可扩展散列）** 在**可扩展散列**中，索引由含 $2^g$ 个指向桶的指针的目录和桶本身组成，其中 $g$ 是**全局深度**。码 $k$ 属于目录项号 $h(k) \bmod 2^g$ 所指向的桶，即由 $h(k)$ 的低 $g$ 位决定。每个桶有**局部深度** $l \le g$：桶中所有码的散列值在低 $l$ 位上一致，并且有 $2^{g-l}$ 个目录项指向该桶。

当局部深度为 $l$ 的桶溢出时：

1. 若 $l < g$，把桶分裂为两个局部深度为 $l + 1$ 的桶，按散列值的第 $l + 1$ 位分配它的码，并把 $2^{g-l}$ 个目录项中的一半重定向到新桶。其他桶都不动。
2. 若 $l = g$，先把目录加倍（项 $i + 2^g$ 成为项 $i$ 的副本，$g$ 加一），再如情形 1 那样分裂。

目录加倍只复制指针，而且目录足够小，可以留在内存中。等值查找的代价是一次目录访问和一次桶读。

**例 8.3.1** 设桶容量为 2，并且为了便于阅读取 $h(k) = k$。向全局深度为 1 的索引依次插入 4、6、9、13 和 2 之后，低位为 0 的桶溢出过一次，目录加倍了：

```python
CAPACITY = 2  # records per bucket


class Bucket:
    def __init__(self, depth):
        self.depth = depth       # local depth
        self.keys = []


class ExtendibleHash:
    """Directory indexed by the low-order global_depth bits of h(key) = key."""

    def __init__(self):
        self.global_depth = 1
        self.directory = [Bucket(1), Bucket(1)]

    def _bucket(self, key):
        return self.directory[key & ((1 << self.global_depth) - 1)]

    def insert(self, key):
        b = self._bucket(key)
        if len(b.keys) < CAPACITY:
            b.keys.append(key)
            return
        if b.depth == self.global_depth:          # directory doubling
            self.directory = self.directory + self.directory
            self.global_depth += 1
        # split b on bit number b.depth
        b.depth += 1
        new = Bucket(b.depth)
        bit = 1 << (b.depth - 1)
        old_keys, b.keys = b.keys, []
        for i, entry in enumerate(self.directory):
            if entry is b and i & bit:
                self.directory[i] = new
        for k in old_keys:
            self._bucket(k).keys.append(k)
        self.insert(key)                          # may split again

    def show(self):
        print(f"global depth {self.global_depth}")
        seen = {}
        for i, b in enumerate(self.directory):
            label = seen.setdefault(id(b), chr(ord("A") + len(seen)))
            bits = format(i, f"0{self.global_depth}b")
            print(f"  {bits} -> bucket {label} (local depth {b.depth}): {b.keys}")


h = ExtendibleHash()
for k in [4, 6, 9, 13, 2]:
    h.insert(k)
h.show()
for k in [11, 10]:
    h.insert(k)
    print(f"after inserting {k} (binary {k:b}):")
    h.show()
```

```text
global depth 2
  00 -> bucket A (local depth 2): [4]
  01 -> bucket B (local depth 1): [9, 13]
  10 -> bucket C (local depth 2): [6, 2]
  11 -> bucket B (local depth 1): [9, 13]
after inserting 11 (binary 1011):
global depth 2
  00 -> bucket A (local depth 2): [4]
  01 -> bucket B (local depth 2): [9, 13]
  10 -> bucket C (local depth 2): [6, 2]
  11 -> bucket D (local depth 2): [11]
after inserting 10 (binary 1010):
global depth 3
  000 -> bucket A (local depth 2): [4]
  001 -> bucket B (local depth 2): [9, 13]
  010 -> bucket C (local depth 3): [2, 10]
  011 -> bucket D (local depth 2): [11]
  100 -> bucket A (local depth 2): [4]
  101 -> bucket B (local depth 2): [9, 13]
  110 -> bucket E (local depth 3): [6]
  111 -> bucket D (local depth 2): [11]
```

插入 11 使桶 B 溢出，其局部深度 1 小于全局深度 2：B 按第二位分裂，目录大小不变。插入 10 使桶 C 溢出，其局部深度等于全局深度：目录加倍为 8 项，C 按第三位分裂为 `[2, 10]`（低位 010）和 `[6]`（低位 110）。桶 A、B 和 D 不受影响，现在各被两个目录项引用。

如果许多码具有相同的散列值，再多的分裂也无法把它们分开，仍然需要溢出页。

### 8.3.3. 实践中的散列索引

线性散列（linear hashing）由 Litwin 于 1980 年提出，它避免了目录：每当**装填因子**超过阈值时，就按固定的轮转顺序一次分裂一个桶，而不管是哪个桶溢出；溢出的桶使用溢出页，直到轮到它们。PostgreSQL 的 `hash` 索引类型使用带桶分裂与溢出页的变体；它自 10 版起才是抗崩溃的（有 WAL 日志），只支持 `=` 运算符，并且在同一个码上很少比 **B 树**快。实践中，散列更多地用在查询处理内部，如散列**连接**和散列聚集（[4.13.9](/4.13.9)），以及 DBMS 的内存结构，如缓冲表和锁表，而不是持久的索引。MySQL 的 InnoDB 不提供持久的散列索引，而是在内存中对频繁访问的 B 树页建立*自适应散列索引*。

## 8.4. 日志结构合并树

### 8.4.1. 结构

**B+ 树**就地更新**页**：每插入一个随机码都要读一个叶子并最终把整个页写回，对一个小的项而言是很大的**写放大**。以写为主的工作负载（事件日志、时间序列、指标、消息传递）更喜欢把随机写变成顺序写的结构。

**定义 8.4.1（日志结构合并树）** **日志结构合并树**（LSM 树）把键–值项存储在若干组件中。写操作进入内存中的有序结构，即**内存表**（通常是**跳表**），同时也追加到预写日志以保证持久性。内存表满时，它被作为不可变的有序文件，即**有序字符串表**（SSTable），写到持久存储中，并开始一个新的内存表。称为**压实**的后台进程把 SSTable 合并成更大的有序文件，并丢弃被覆盖和被删除的项。删除被写成一个特殊的项，即**墓碑标记**，它隐藏该码的较旧的值，直到压实把两者一并清除。

点查找先查**内存表**，再从新到旧查 **SSTable**，并返回找到的第一项。范围扫描合并所有组件的有序流。**LSM 树**由 O'Neil 等人在 1996 年描述，并因 Google 的 Bigtable（2006）而流行。如今它是 LevelDB、RocksDB（用于 MySQL 的 MyRocks、TiKV、CockroachDB 的早期版本和许多其他系统）、Apache Cassandra、HBase 和 ScyllaDB 的存储引擎；CockroachDB 现在使用 Pebble，这是它自己的 LSM 引擎。

### 8.4.2. 压实策略

**压实**决定三种代价之间的权衡：**写放大**（一项被重写的频率）、*读放大*（一次查找必须检查的组件数）和*空间放大*（保留了多少过时数据）。

| 策略 | 组织 | 写 | 读与空间 |
|---|---|---|---|
| 分层（Leveled；LevelDB、RocksDB 默认） | 第 $L_i$ 层含互不重叠的 SSTable，总大小约为 $L_{i-1}$ 的 $T$ 倍（通常 $T = 10$）；一个文件被合并进下一层与它重叠的文件中 | 高：每项在每一层被重写约 $T$ 次 | 低：每层只需检查一个文件，过时数据少 |
| 分级或按大小分级（Tiered、size-tiered；Cassandra 默认、RocksDB “universal”） | 每层收集至多 $T$ 个大小相近、相互重叠的有序段；满时合并成下一层的一个段 | 低：每层重写一次 | 较高：每层至多 $T$ 个段，过时数据较多 |

与 B+ 树相比，LSM 树有更高的写吞吐量和更好的压缩（文件不可变且顺序写出），但读更慢、更难预测，并且**压实**与前台工作负载争用 I/O。

### 8.4.3. Bloom 过滤器

为了避免读取不可能含有某个码的 SSTable，每个 SSTable 带有一个关于其码的 Bloom 过滤器，保存在内存中。

**定义 8.4.2（Bloom 过滤器）** 含 $n$ 个码的集合 $S$ 的 **Bloom 过滤器**是一个 $m$ 位的位数组（初始全为零），连同 $k$ 个取值在 $\{0, \dots, m-1\}$ 中的散列函数 $h_1, \dots, h_k$。插入码 $x$ 就把位 $h_1(x), \dots, h_k(x)$ 置位。对 $y$ 的查询，若位 $h_1(y), \dots, h_k(y)$ 全被置位则回答“可能在 $S$ 中”，否则回答“不在 $S$ 中”。

**Bloom 过滤器**没有假阴性：$S$ 的每个码都置位了自己的位。它可能有假阳性。

**命题 8.4.1** 若**散列函数**的行为像独立、均匀分布的随机函数，则对 $y \notin S$ 的查询回答“可能在 $S$ 中”的概率约为

$$
p \approx \left(1 - \mathrm{e}^{-kn/m}\right)^k,
$$

对固定的每个码的位数 $c = m/n$，它在 $k = c \ln 2$ 时最小，此时 $p \approx 2^{-k} \approx 0.6185^{c}$。

**证明** 经过 $n$ 次插入，已有 $kn$ 个位置被均匀随机地选中，所以固定的一位仍为零的概率是 $(1 - 1/m)^{kn} \approx \mathrm{e}^{-kn/m}$。假阳性要求 $y$ 的 $k$ 个位置全被置位；把这 $k$ 个事件看作独立的（对大的 $m$ 是很好的近似），得 $p \approx (1 - \mathrm{e}^{-kn/m})^k$。记 $q = \mathrm{e}^{-k/c}$，它随 $k$ 增大从 1 减小到 0，于是 $k = -c \ln q$，$\ln p = k \ln(1 - q)$。求导，

$$
\frac{\mathrm{d} \ln p}{\mathrm{d} k} = \ln(1-q) + k \cdot \frac{q}{c\,(1-q)} = \frac{(1-q)\ln(1-q) - q \ln q}{1-q} = -\frac{\psi(q)}{1-q},
\qquad \psi(q) = q \ln q - (1-q)\ln(1-q).
$$

函数 $\psi$ 满足 $\psi(1-q) = -\psi(q)$，在 $(0,1)$ 的两端趋于 $0$，并且 $\psi'(q) = \ln\bigl(q(1-q)\bigr) + 2$ 在两端附近为负，在含 $\tfrac12$ 的中间区间上为正；因此 $\psi < 0$ 于 $(0, \tfrac12)$，$\psi(\tfrac12) = 0$，$\psi > 0$ 于 $(\tfrac12, 1)$。所以当 $q > \tfrac12$ 时 $\ln p$ 随 $k$ 减小，当 $q < \tfrac12$ 后增大：最小值在 $q = \tfrac12$，即 $k = c \ln 2$，此时 $p = (1/2)^k = 2^{-c \ln 2} = (2^{-\ln 2})^c \approx 0.6185^c$。$\square$

每个码 10 位、$k = 7$ 时，假阳性率约为 0.8%；每个码每增加 4.8 位，假阳性率就除以 10。下图把公式与模拟作了比较。

![Bloom 过滤器的假阳性率随每个码的位数的变化，分别对固定的散列函数个数和最优的整数个数；圆点是对 2,000 个码和 200,000 个不在集合中的探测码的模拟结果。](./plots/bloom-filter-fpr.py)

Bloom 过滤器的用途远不止 LSM 树：在分布式**连接**中避免传送不会匹配的行，在 PostgreSQL 的 `bloom` 扩展中作为一种**索引**类型，以及在生物信息学中用于序列组装器和读段分类器中的 $k$-mer 成员判定。

## 8.5. 位图索引与其他索引类型

### 8.5.1. 位图索引

**定义 8.5.1（位图索引）** 对关系 $r$ 的属性 $A$（$r$ 的记录编号为 $0, 1, \dots, n_r - 1$），**位图索引**对 $A$ 的每个值 $v$ 存储一个长为 $n_r$ 的位向量，其第 $i$ 位为 1 当且仅当记录 $i$ 满足 $A = v$。

**位图索引**适合只有少数不同值的**属性**，如运行示例中的 `tissue` 或 `treatment`。条件的合取与析取变成对整个机器字的按位运算：满足 `tissue = 'lung' AND treatment = 'treated'` 的样本就是 $B_{\text{lung}} \land B_{\text{treated}}$ 中的 1 位，对它们计数是一次位计数（population count）。有五种组织和 $n_r$ 行时，**索引**在压缩前需要 $5 n_r$ 位，远少于每行一项的 B+ 树。稀疏的位向量用游程方案（BBC、WAH）压缩，或者在多数当前系统中用 Roaring 位图：它把向量分成 $2^{16}$ 位的块，每块存储为有序数组、位图或游程，取其中最小的。

**位图**索引的更新代价高（新增一行会改变其值的向量中的一位，压缩后的向量必须部分重写），主要用于**数据仓库**；Oracle 把它们作为持久的索引类型提供。PostgreSQL 没有持久的位图索引，但它的*位图索引扫描*（bitmap index scan）由一个或多个普通索引即时构造匹配的**堆**页的位图，用 AND 和 OR 组合它们，然后按物理顺序读匹配的堆页，这把辅助索引的随机 I/O 变成近乎顺序的 I/O。

### 8.5.2. 其他索引类型

PostgreSQL 的索引访问方法说明了 **B+ 树**和散列之外索引结构的范围：

| 类型 | 结构 | 典型用途 |
|---|---|---|
| `btree` | B+ 树（B-link 树） | 默认；等值、范围、排序、`LIKE 'abc%'`（配合合适的排序规则或运算符类） |
| `hash` | 线性散列的变体 | 仅等值 |
| `gist` | 广义搜索树：由谓词（如 R 树中的包围盒）组成的平衡树 | 几何（PostGIS）、区间、最近邻搜索、排除约束 |
| `spgist` | 空间划分树（四叉树、k-d 树、基数树） | 点、IP 地址、文本前缀 |
| `gin` | 广义倒排索引：元素的 B 树，附带行的倒排列表 | 全文搜索、`jsonb`、数组 |
| `brin` | 块范围索引：每 128 页一个范围的最小值和最大值（或其他摘要） | 物理顺序与某列相关的超大表，如追加行的时间戳 |

倒排索引（inverted index）是 GIN 和搜索引擎背后的结构，它把每个元素（单词、数组元素、JSON 键）映射到含有它的行的列表。对有十亿条追加测量的表，采集日期上的 BRIN 索引只占几百千字节，使范围查询可以跳过所有摘要不含该范围的**页**范围，且几乎不需要维护代价；若该列与物理顺序不相关，它就没有用。向量和近似最近邻搜索的索引（HNSW、IVF）可通过 `pgvector` 扩展在 PostgreSQL 中使用，在 [4.13.12](/4.13.12) 中讨论。

## 8.6. SQL 中的索引与物理设计

### 8.6.1. 创建索引

**SQL** 标准没有定义**索引**（它们是物理层面的事），但每个系统支持的语句基本相同。在 PostgreSQL 中：

```sql
-- a secondary B-tree index on one column
CREATE INDEX measurement_gene_idx ON measurement (gene_id);

-- a composite index; serves conditions on chrom, or on chrom and start_pos
CREATE INDEX gene_location_idx ON gene (chrom, start_pos);

-- a unique index enforces uniqueness (as UNIQUE and PRIMARY KEY constraints do)
CREATE UNIQUE INDEX gene_symbol_idx ON gene (symbol);

-- a covering index: tpm is stored in the leaves but is not part of the key
CREATE INDEX measurement_gene_cover_idx ON measurement (gene_id) INCLUDE (tpm);

-- an expression index, used by WHERE lower(symbol) = ...
CREATE INDEX gene_symbol_lower_idx ON gene (lower(symbol));

-- a partial index: only rows that satisfy the predicate are indexed
CREATE INDEX measurement_high_idx ON measurement (gene_id) WHERE tpm > 100;

-- other access methods
CREATE INDEX sample_date_brin ON sample USING brin (collected_on);

-- build without blocking writes to the table (slower, cannot run in a transaction)
CREATE INDEX CONCURRENTLY measurement_tpm_idx ON measurement (tpm);

DROP INDEX measurement_tpm_idx;
```

主码和唯一约束会自动创建它们的索引；**外码**则不会，尽管引用列上的索引通常是必需的，这样删除被引用的行时才不必扫描引用表。MySQL 和 SQLite 支持相同的核心语法（复合索引、唯一索引、表达式索引，SQLite 中还有部分索引）；MySQL 的 InnoDB 把每张表聚簇于它的**主码**，所以那里的“辅助索引”总是引用主码。

### 8.6.2. 索引的实际效果

[4.13.7](/4.13.7) 的合成**数据库**在 `measurement` 上有主码 `(sample_id, gene_id)`，含 100 个样本和 5,000 个基因。下面的脚本在 SQLite 3.45 上运行，对查询计时（9 次运行的中位数，数据在**操作系统**的**页缓存**中），并打印 SQLite 选择的计划。

```python
import sqlite3, time

con = sqlite3.connect("idx.db")


def timed(sql, args=()):
    """Median of 9 runs, in milliseconds, and the plan of the statement."""
    plan = " | ".join(r[3] for r in con.execute("EXPLAIN QUERY PLAN " + sql, args))
    runs = []
    for _ in range(9):
        start = time.perf_counter()
        con.execute(sql, args).fetchall()
        runs.append((time.perf_counter() - start) * 1000)
    return sorted(runs)[4], plan


q = "SELECT avg(tpm) FROM measurement WHERE gene_id = ?"
g = ("ENSG00000000042",)
print("%8.3f ms  %s" % timed(q, g))
con.execute("CREATE INDEX measurement_gene ON measurement (gene_id)")
print("%8.3f ms  %s" % timed(q, g))
con.execute("CREATE INDEX measurement_gene_tpm ON measurement (gene_id, tpm)")
print("%8.3f ms  %s" % timed(q, g))

# Secondary index on tpm versus a full scan, for predicates of growing selectivity.
con.execute("CREATE INDEX measurement_tpm ON measurement (tpm)")
n = con.execute("SELECT count(*) FROM measurement").fetchone()[0]
print("threshold  fraction  full scan  via index")
for t in [1000, 100, 30, 10, 1]:
    frac = con.execute("SELECT count(*) FROM measurement WHERE tpm > ?", (t,)).fetchone()[0] / n
    scan, _ = timed("SELECT max(sample_id) FROM measurement NOT INDEXED WHERE tpm > ?", (t,))
    idx, _ = timed("SELECT max(sample_id) FROM measurement INDEXED BY measurement_tpm WHERE tpm > ?", (t,))
    print(f"{t:9d}  {frac:8.4f}  {scan:6.1f} ms  {idx:6.1f} ms")
```

```text
   0.153 ms  SEARCH measurement USING INDEX sqlite_autoindex_measurement_1 (ANY(sample_id) AND gene_id=?)
   0.022 ms  SEARCH measurement USING INDEX measurement_gene (gene_id=?)
   0.007 ms  SEARCH measurement USING COVERING INDEX measurement_gene_tpm (gene_id=?)
threshold  fraction  full scan  via index
     1000    0.0006    21.3 ms     0.1 ms
      100    0.0409    18.3 ms    22.5 ms
       30    0.1748    21.7 ms   101.2 ms
       10    0.4192    31.3 ms   299.9 ms
        1    0.9085    35.5 ms   561.0 ms
```

这些结果把关于索引的主要事实集中展示出来。

- 在 `gene_id` 上没有索引时，SQLite 仍然避免了全表扫描：`ANALYZE` 收集的统计信息告诉它 `sample_id` 只有 100 个不同值，所以它对主码索引做跳跃扫描，每个样本一次下降（`ANY(sample_id)`）。
- `gene_id` 上的**辅助索引**使查找快约七倍：一次下降找到 100 个项，随后按 rowid 取 100 条记录。
- `(gene_id, tpm)` 上的覆盖索引只靠索引就能回答查询，所以更快。
- 辅助索引只对选择性高的谓词有帮助。这里的盈亏平衡点略低于行数的 4%；对匹配 91% 行的 `tpm > 1`，索引计划比扫描慢 16 倍，因为它按索引顺序逐条取记录，而不是顺序地读表。当数据在磁盘上而不是在**页**缓存中时，随机取记录更贵，盈亏平衡的比例更低，通常是百分之几或更少。根据统计信息决定采用哪个计划是优化器的任务（[4.13.9](/4.13.9)）。

### 8.6.3. 物理设计

物理数据库设计针对给定的**模式**和工作负载，选择文件组织、索引、**分区**，以及在分析型系统中的排序顺序和**物化视图**。索引不是免费的：每个索引占用空间（上面的覆盖索引几乎与表一样大），并且必须随被索引列的每次插入、删除和更新而更新，一次本来只触及一个页的写入，每多一个索引就多触及一个页。常见的准则：

1. 从工作负载出发：频繁的和昂贵的查询，以及更新的速率。没有查询使用的索引纯属代价；PostgreSQL 的 `pg_stat_user_indexes` 统计每个索引被扫描的次数。
2. 为选择性高的 `WHERE` 条件和**连接**条件的**属性**建索引，包括外码。
3. 复合索引的列按查询使用它们的方式排序：先是等值列，再是范围或排序列。$(A, B)$ 上的一个索引可以服务关于 $A$ 和关于 $(A, B)$ 的查询，但一般不能服务关于 $B$ 的查询。
4. 对读取少数几列的频繁查询使用覆盖索引，当查询集中于一小部分行时使用部分索引。
5. 为最重要的范围查询选择聚簇（在 InnoDB 和 SQLite 的 `WITHOUT ROWID` 中就是主码），并优先选择随时间递增的码，如**标识列**或按时间排序的 UUID（UUID 版本 7，PostgreSQL 18 用 `uuidv7()` 生成），使插入落到最右的叶子，而不是在树的各处分裂页。
6. 批量加载时，先删除辅助索引，加载后再重建：用排序建索引比逐行维护它便宜得多。
7. 测量：比较前后的计划和耗时（§8.6.2），并用 `ANALYZE` 保持统计信息最新。

根据记录的工作负载建议索引的自动工具（*索引顾问*，如 SQL Server 的 Database Engine Tuning Advisor 以及 PostgreSQL 扩展 HypoPG 和 `pg_qualstats`）用优化器的代价模型评估假设的索引，而无需真正建立它们。

## 小结

- **索引**把搜索码值映射到记录位置。**聚集索引**遵循文件顺序，可以是稀疏的；**辅助索引**是稠密的，通过它们取许多记录，每条记录要付出一次随机读。
- B+ 树是各结点至少半满的平衡多级索引；其高度至多为 $1 + \log_{\lceil n/2 \rceil} N$，扇出在几百时就是三四层。叶子分裂把码复制上去，内部分裂把码上移；实际系统在重复值、压缩、批量加载、并发（B-link 树）和惰性删除上有所改进。
- 散列索引只支持等值；可扩展散列通过目录加倍并一次分裂一个桶来增长，线性散列通过按轮转顺序分裂桶来增长。
- LSM 树把写变成对有序段的顺序追加，再由压实合并，用读放大和空间放大换取较低的写放大；每个码约 10 位的 Bloom 过滤器可筛掉 99% 不必要的段查找。
- 位图索引适合分析型工作负载中基数低的属性；倒排索引（GIN）、广义搜索树（GiST）和块范围索引（BRIN）覆盖文本、几何和只追加的超大表。
- 物理设计在查询速度与更新代价之间权衡；索引有助于选择性高的谓词、连接、排序和覆盖，并且必须对照实测的计划加以检验。
