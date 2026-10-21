---
title: Indexing
description: "Index structures of database systems: search keys, clustering and secondary indexes, dense and sparse indexes, multilevel indexes; B+-tree indexes with height bound, search, insertion with splits (a runnable implementation), deletion and their engineering in PostgreSQL, InnoDB and SQLite; static and extendible hashing; LSM trees, compaction and Bloom filters; bitmap, GIN, GiST and BRIN indexes; CREATE INDEX and physical design with measured plans in SQLite."
---

A file organization ([4.13.7](/4.13.7)) supports at most one access path well: a heap file is good for scans, a file sorted on `sample_id` for queries on samples. Queries look up rows in many other ways: all measurements of a gene, the genes on chromosome 17 between two positions, the samples collected in March. An index is an auxiliary structure that maps values of some attributes to the locations of the matching records, so that such a query reads a few pages instead of the whole table. This chapter first fixes the vocabulary of indexing, then studies the B+ tree, the index structure that almost every relational system uses by default, followed by hashing, the log-structured merge tree of write-intensive systems, bitmap indexes and the specialized index types of PostgreSQL. It ends with the practical question of which indexes to create, the core of physical database design. The data structures themselves were introduced in [4.3](/4.3): B-trees and the B+-tree variant in [4.3.8](/4.3.8#sec-8.2), hash tables in [4.3.9](/4.3.9). Here we look at them as disk-resident structures, in units of pages, together with the engineering that makes them work in a DBMS. How the optimizer chooses between an index and a scan is the topic of [4.13.9](/4.13.9); how indexes are kept consistent under concurrent transactions is touched on in [4.13.11](/4.13.11).

## 8.1. Basic Concepts

### 8.1.1. Search Keys and Index Types

**Definition 8.1.1 (Index)** Let $r$ be a relation and $K$ a list of attributes of $r$, the **search key** (not necessarily a key of $r$). An **index** on $r$ with search key $K$ is a data structure, stored separately from $r$ or as its file organization, that returns for a given value or range of values of $K$ the locations (record identifiers or primary-key values) of the records of $r$ with those values. The pairs (search-key value, location) stored in an index are its **index entries**.

The term "key" is overloaded: a search key is any list of attributes that queries use for lookups, while a key of a relation in the sense of [4.13.2](/4.13.2) is a property of the data. An index on `measurement(gene_id)` has a search key that is not a key: each value occurs once per sample.

**Definition 8.1.2 (Clustering Index and Secondary Index)** An index is a **clustering index** (also *primary index*) if the records of the file are stored in the order of its search key; otherwise it is a **secondary index** (also *non-clustering index*). A file can have at most one clustering index and any number of secondary indexes.

The distinction decides the cost of a range query. Through a clustering index, the records with keys in a range occupy consecutive pages, and fetching $m$ matching records costs about $m / f$ page reads, where $f$ is the number of records per page. Through a secondary index, consecutive index entries point to records scattered over the file, and fetching $m$ records may cost up to $m$ page reads, one for each record. For large $m$ this is far worse than scanning the file (§8.6.2).

**Definition 8.1.3 (Dense and Sparse Index)** An index is **dense** if it contains an index entry for every search-key value that occurs in the file (for a secondary index: for every record), and **sparse** if it contains entries for only some of the values, typically the first key of each page of the file.

A sparse index is possible only for a clustering index: to find key $k$, find the largest index entry $\le k$ and scan the file forward from the page it points to. Sparse indexes are small, one entry per page instead of per record, which matters for the upper levels of a tree. A secondary index must be dense, since the order of the file tells nothing about where a key is. If the search key of a secondary index is not unique, its entries either repeat the key once per record or store a key once with a list of record identifiers (the *posting list*); PostgreSQL's B-tree *deduplication*, introduced in version 13, does the latter automatically.

Indexes are evaluated by the access types they support (equality search, range search, ordered output, prefix search), the cost of a lookup, the cost of insertion and deletion, and the space they need.

### 8.1.2. Multilevel Indexes

An index on a large file is itself large. A dense index on 500,000 records with 20-byte entries fills about 2,500 pages of 4 KiB; binary search over it costs $\lceil \log_2 2500 \rceil = 12$ page reads. The remedy is to treat the index as a sorted file and build a sparse index on it, and so on, until the top level fits in one page. With $f$ entries per index page, each level reduces the number of pages by a factor of $f$, so the number of levels for $N$ index entries is $\lceil \log_f N \rceil$ instead of $\log_2$ of the number of pages. For $f = 200$ and $N = 500{,}000$ it is 3, and the top one or two levels are always in the buffer pool. A static multilevel index is hard to maintain under insertions; the B+ tree is the dynamic version of this idea.

## 8.2. B+-Tree Indexes

### 8.2.1. Structure

The **B+ tree** was introduced in [4.3.8](/4.3.8#sec-8.2.7) as the variant of the B-tree in which all keys are stored in the leaves and the leaves are linked. As a database index, each node is one page, and the parameter that matters is the fan-out: the number of children of an internal node, which is in the hundreds.

**Definition 8.2.1 (B+ Tree)** A B+ tree of order $n$ ($n \ge 3$) is a rooted tree in which all leaves are at the same depth and:

1. Each internal node holds $k - 1$ search-key values $K_1 < K_2 < \dots < K_{k-1}$ and $k$ child pointers $P_1, \dots, P_k$, where $\lceil n/2 \rceil \le k \le n$, except that the root has $2 \le k \le n$. All keys in the subtree of $P_1$ are $< K_1$, all keys in the subtree of $P_i$ ($1 < i < k$) are $\ge K_{i-1}$ and $< K_i$, and all keys in the subtree of $P_k$ are $\ge K_{k-1}$.
2. Each leaf holds between $\lceil (n-1)/2 \rceil$ and $n - 1$ index entries (search-key value and record location), sorted by key, except when the leaf is the root, which may hold any number from 0 to $n - 1$.
3. Each leaf has a pointer to the next leaf in key order.

The internal nodes form a sparse multilevel index over the leaves, and the leaves form a dense index over the file (or contain the records themselves, for an index-organized table, [4.13.7](/4.13.7#sec-7.4.3)). The occupancy condition, every non-root node at least half full, is what keeps the tree shallow.

**Theorem 8.2.1 (Height of a B+ Tree)** Let a B+ tree of order $n \ge 3$ contain $N \ge 1$ index entries, and let $h$ be the number of levels (the number of nodes on a path from the root to a leaf). Then

$$
\left\lceil \frac{n}{2} \right\rceil^{h-1} \le N, \qquad\text{that is,}\qquad h \le 1 + \log_{\lceil n/2 \rceil} N.
$$

**Proof** Write $d = \lceil n/2 \rceil$ and $l = \lceil (n-1)/2 \rceil$. For $h = 1$ the claim is $1 \le N$. For $h \ge 2$, the root has at least 2 children and every other internal node has at least $d$ children, so level $j$ ($1 \le j \le h$, the root being level 1) has at least $2 d^{j-2}$ nodes for $j \ge 2$; in particular there are at least $2 d^{h-2}$ leaves. Each leaf is not the root and holds at least $l$ entries, so $N \ge 2 l\, d^{h-2}$. Finally $2l \ge n - 1 \ge \frac{n+1}{2} \ge d$ for $n \ge 3$, hence $N \ge d^{h-1}$. $\square$

**Example 8.2.1** In PostgreSQL an index entry for a `bigint` key takes about 20 bytes (an 8-byte index tuple header, the 8-byte key and a 4-byte line pointer), so an 8 KiB page holds about 400 entries; leaves are filled to 90% when built (the default `fillfactor`) and are on average about 70% full after random insertions, so take an effective fan-out of 300. Three levels then index $300^3 = 2.7 \times 10^7$ rows and four levels $8.1 \times 10^9$. The root and the second level, 1 + 300 pages, are practically always cached, so a point lookup in a table of billions of rows costs one or two page reads in the index plus one for the record.

### 8.2.2. Search

To find the entries with key $v$, start at the root; in an internal node with keys $K_1, \dots, K_{k-1}$, follow the pointer $P_i$ with $i$ the number of keys $\le v$ plus one; at the leaf, look for $v$. For a range $[a, b]$, search for $a$ and then follow the leaf chain until a key exceeds $b$. A lookup costs $h$ page reads for the descent, plus one leaf per $f$ further entries for a range, plus the reads of the records.

### 8.2.3. Insertion

Insertion finds the leaf where the key belongs and inserts the entry in order. If the leaf overflows (it would hold $n$ entries), it is *split*: the first $\lceil n/2 \rceil$ entries stay, the rest move to a new right sibling, and the smallest key of the new leaf is *copied* into the parent together with a pointer to the new leaf. If the parent overflows ($n + 1$ children), it is split as well, but the middle key is *moved* up rather than copied, because internal keys only guide the search. A split of the root creates a new root with two children; this is the only way the tree grows in height, so all leaves stay at the same depth. The splits are those of the B-tree ([4.3.8](/4.3.8#sec-8.2.4)), with the copy-versus-move distinction as the only difference.

The following implementation of order $n = 4$ (at most 3 entries per leaf and 4 children per internal node) prints the tree level by level after some of the insertions.

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

The fourth key, 6, overflows the single leaf `[5 6 10 20]`, which splits into `[5 6]` and `[10 20]`; the key 10 is copied into a new root. The insertion of 9 overflows the leaf `[6 7 8]`; key 8 is copied up into the root `[6 10 20]`, which then has five children and splits: `[6 8]` and `[20]` become internal nodes and the middle key 10 moves into a new root, so the tree grows to three levels. Key 10 now appears in the root and in a leaf, but in no other internal node.

### 8.2.4. Deletion

Deletion removes the entry from its leaf. If the leaf falls below the minimum occupancy, it either *borrows* entries from a sibling (redistribution, which changes the separating key in the parent) or is *merged* with a sibling (which removes one key and pointer from the parent, possibly causing the parent to underflow in turn). If the root is left with a single child, that child becomes the new root and the height decreases.

Real systems relax these rules. Merging nodes as soon as they fall below half full can cause repeated splits and merges when insertions and deletions alternate near the boundary, and it complicates concurrency. PostgreSQL never merges partially full B-tree pages; it removes a page only when it becomes completely empty, and dead entries are cleaned up by `VACUUM` or opportunistically when a page would otherwise split. Space is thus recovered over time rather than immediately, and an index that has suffered massive deletions can be rebuilt with `REINDEX`.

### 8.2.5. B+ Trees in Real Systems

The textbook structure is refined in many ways:

- *Duplicates.* Non-unique search keys are made unique by appending the record identifier to the key, so that every entry has a well-defined position; PostgreSQL additionally stores runs of equal keys once with a posting list (deduplication).
- *Composite keys.* An index on $(A, B)$ is ordered lexicographically: by $A$, and by $B$ among equal values of $A$. It supports conditions on $A$, on $A$ and $B$, and on $A = a$ with a range of $B$, and returns rows in $(A, B)$ order. A condition on $B$ alone does not determine a contiguous range; a *skip scan* treats it as one range search per distinct value of $A$, which pays off when $A$ has few distinct values. SQLite has done this for a long time (it appears in §8.6.2), and PostgreSQL 18 added B-tree skip scans.
- *Covering indexes and index-only scans.* If every column a query needs is in the index, the records need not be read at all. PostgreSQL's `CREATE INDEX ... INCLUDE (...)` (since version 11) stores extra non-key columns in the leaves for this purpose; an index-only scan still consults the visibility map ([4.13.7](/4.13.7#sec-7.4.1)) to know whether the row versions on a heap page are visible to every transaction.
- *Compression.* Keys of internal nodes need only distinguish their subtrees, so they can be truncated (*suffix truncation*); keys of a leaf share prefixes (*prefix compression*). Both raise the fan-out.
- *Bulk loading.* Building an index by inserting entries one by one causes random I/O and half-full pages. `CREATE INDEX` instead sorts the entries (with the external sort of [4.13.9](/4.13.9#sec-9.4)) and builds the tree bottom-up, filling the leaves sequentially to the fill factor and creating each internal level from the first keys of the level below.
- *Concurrency.* Operations on a B+ tree hold short-term latches on pages (not transaction locks; see [4.13.11](/4.13.11)) and use *latch coupling*: latch a child before releasing its parent. PostgreSQL implements the Lehman–Yao *B-link tree*, in which each node also stores a right-link and a high key, so that a reader that arrives at a node just split by another process can recover by following the right-link.
- *Secondary indexes on index-organized tables.* In InnoDB a secondary index entry stores the primary key, not a page address; a lookup descends the secondary index and then the clustered index. Records can thus move between pages during splits without updating secondary indexes, at the cost of a second descent per lookup.

## 8.3. Hash Indexes

### 8.3.1. Static Hashing

A hash index stores its entries in *buckets*, each bucket being a page (with a chain of overflow pages if it is full), and a **hash function** $h$ maps a search-key value to a bucket number. An equality lookup reads one bucket and its overflow chain; insertion and deletion likewise touch one bucket. This is **separate chaining** on disk ([4.3.9](/4.3.9#sec-9.3)), with pages as list nodes.

A hash index does not support range queries or ordered output, because $h$ destroys the order of the keys. With a fixed number $B$ of buckets (*static hashing*), the overflow chains grow as the file grows, and when the file shrinks the space is wasted; rehashing everything into a larger table, as an in-memory **hash table** would do, means rewriting the whole index at once. Dynamic hashing schemes grow the table gradually.

### 8.3.2. Extendible Hashing

**Definition 8.3.1 (Extendible Hashing)** In **extendible hashing**, the index consists of a directory of $2^g$ pointers to buckets, where $g$ is the **global depth**, and the buckets themselves. A key $k$ belongs to the bucket pointed to by directory entry number $h(k) \bmod 2^g$, that is, by the $g$ low-order bits of $h(k)$. Each bucket has a **local depth** $l \le g$: all keys in the bucket agree in the $l$ low-order bits of their hash values, and $2^{g-l}$ directory entries point to the bucket.

When a bucket with local depth $l$ overflows:

1. If $l < g$, split the bucket into two buckets of local depth $l + 1$, distribute its keys according to bit $l + 1$ of their hash values, and redirect half of the $2^{g-l}$ directory entries to the new bucket. No other bucket is touched.
2. If $l = g$, first double the directory (entry $i + 2^g$ becomes a copy of entry $i$, and $g$ increases by one), then split as in case 1.

Doubling the directory copies pointers only, and the directory is small enough to stay in memory. An equality lookup costs one directory access and one bucket read.

**Example 8.3.1** Take bucket capacity 2 and, for readability, $h(k) = k$. After inserting 4, 6, 9, 13 and 2 into an index that started with global depth 1, the bucket for low bit 0 has overflowed once, and the directory was doubled:

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

Inserting 11 overflows bucket B, whose local depth 1 is below the global depth 2: B splits on the second bit and the directory keeps its size. Inserting 10 overflows bucket C, whose local depth equals the global depth: the directory doubles to 8 entries and C splits on the third bit into `[2, 10]` (low bits 010) and `[6]` (low bits 110). Buckets A, B and D are untouched and are now each referenced by two directory entries.

If many keys share the same hash value, no number of splits separates them, and overflow pages are still needed.

### 8.3.3. Hash Indexes in Practice

*Linear hashing* (Litwin, 1980) avoids a directory: buckets are split one at a time in a fixed round-robin order, whenever the load factor exceeds a threshold, regardless of which bucket overflowed; overflowing buckets use overflow pages until their turn comes. PostgreSQL's `hash` index type uses a variant with bucket splitting and overflow pages; it has been crash-safe (WAL-logged) only since version 10, supports only the `=` operator, and is rarely faster than a B-tree on the same key. In practice, hashing is used far more inside query processing, for hash joins and hash aggregation ([4.13.9](/4.13.9)), and for the in-memory structures of the DBMS, such as the buffer table and the lock table, than for persistent indexes. MySQL's InnoDB does not offer persistent hash indexes but builds an *adaptive hash index* in memory over frequently accessed B-tree pages.

## 8.4. Log-Structured Merge Trees

### 8.4.1. Structure

A B+ tree updates pages in place: each insertion of a random key reads a leaf and eventually writes the whole page back, a large **write amplification** for a small entry. Workloads dominated by writes (event logs, time series, metrics, messaging) prefer a structure that turns random writes into sequential ones.

**Definition 8.4.1 (Log-Structured Merge Tree)** A **log-structured merge tree** (LSM tree) stores key–value entries in several components. Writes go to an in-memory sorted structure, the **memtable** (typically a **skip list**), and are also appended to a write-ahead log for durability. When the memtable is full, it is written to persistent storage as an immutable sorted file, a **sorted string table** (SSTable), and a new memtable is started. A background process called **compaction** merges SSTables into larger sorted files and discards overwritten and deleted entries. A deletion is written as a special entry, a **tombstone**, that hides older values of the key until compaction removes both.

A point lookup searches the memtable, then the SSTables from newest to oldest, and returns the first entry found. A range scan merges the sorted streams of all components. The LSM tree was described by O'Neil and others in 1996 and popularized by Google's Bigtable (2006). Today it is the storage engine of LevelDB, RocksDB (used inside MySQL's MyRocks, TiKV, CockroachDB's earlier versions and many other systems), Apache Cassandra, HBase and ScyllaDB; CockroachDB now uses Pebble, an LSM engine of its own.

### 8.4.2. Compaction Strategies

Compaction decides the trade-off between three costs: write amplification (how often an entry is rewritten), *read amplification* (how many components a lookup must examine) and *space amplification* (how much obsolete data is kept).

| Strategy | Organization | Writes | Reads and space |
|---|---|---|---|
| Leveled (LevelDB, RocksDB default) | Level $L_i$ holds non-overlapping SSTables with a total size about $T$ times that of $L_{i-1}$ (typically $T = 10$); a file is merged into the overlapping files of the next level | high: each entry is rewritten about $T$ times per level | low: one file per level to check, little obsolete data |
| Tiered or size-tiered (Cassandra default, RocksDB "universal") | Each level collects up to $T$ overlapping runs of similar size; when full, they are merged into one run of the next level | low: one rewrite per level | higher: up to $T$ runs per level, more obsolete data |

Compared with a B+ tree, an LSM tree has higher write throughput and better compression (files are immutable and written sequentially) but slower and less predictable reads, and compaction competes with the foreground workload for I/O.

### 8.4.3. Bloom Filters

To avoid reading SSTables that cannot contain a key, each SSTable carries a Bloom filter over its keys, kept in memory.

**Definition 8.4.2 (Bloom Filter)** A **Bloom filter** for a set $S$ of $n$ keys is a bit array of $m$ bits, initially zero, together with $k$ hash functions $h_1, \dots, h_k$ with values in $\{0, \dots, m-1\}$. Inserting a key $x$ sets the bits $h_1(x), \dots, h_k(x)$. A query for $y$ answers "possibly in $S$" if all bits $h_1(y), \dots, h_k(y)$ are set and "not in $S$" otherwise.

A Bloom filter has no false negatives: every key of $S$ set its own bits. It can have false positives.

**Proposition 8.4.1** If the hash functions behave like independent, uniformly distributed random functions, the probability that a query for a key $y \notin S$ answers "possibly in $S$" is approximately

$$
p \approx \left(1 - \mathrm{e}^{-kn/m}\right)^k,
$$

which, for a fixed number $c = m/n$ of bits per key, is minimized by $k = c \ln 2$, giving $p \approx 2^{-k} \approx 0.6185^{c}$.

**Proof** After $n$ insertions, $kn$ bit positions have been chosen uniformly at random, so a fixed bit is still zero with probability $(1 - 1/m)^{kn} \approx \mathrm{e}^{-kn/m}$. A false positive requires that the $k$ positions of $y$ are all set; treating the $k$ events as independent (a good approximation for large $m$) gives $p \approx (1 - \mathrm{e}^{-kn/m})^k$. Write $q = \mathrm{e}^{-k/c}$, which decreases from 1 to 0 as $k$ grows, so that $k = -c \ln q$ and $\ln p = k \ln(1 - q)$. Differentiating,

$$
\frac{\mathrm{d} \ln p}{\mathrm{d} k} = \ln(1-q) + k \cdot \frac{q}{c\,(1-q)} = \frac{(1-q)\ln(1-q) - q \ln q}{1-q} = -\frac{\psi(q)}{1-q},
\qquad \psi(q) = q \ln q - (1-q)\ln(1-q).
$$

The function $\psi$ satisfies $\psi(1-q) = -\psi(q)$, tends to $0$ at both ends of $(0,1)$, and $\psi'(q) = \ln\bigl(q(1-q)\bigr) + 2$ is negative near the ends and positive on a middle interval containing $\tfrac12$; hence $\psi < 0$ on $(0, \tfrac12)$, $\psi(\tfrac12) = 0$ and $\psi > 0$ on $(\tfrac12, 1)$. So $\ln p$ decreases in $k$ while $q > \tfrac12$ and increases once $q < \tfrac12$: the minimum is at $q = \tfrac12$, that is, $k = c \ln 2$, where $p = (1/2)^k = 2^{-c \ln 2} = (2^{-\ln 2})^c \approx 0.6185^c$. $\square$

With 10 bits per key and $k = 7$ the false-positive rate is about 0.8%; each additional 4.8 bits per key divide it by 10. The plot compares the formula with a simulation.

![False-positive rate of a Bloom filter as a function of the number of bits per key, for fixed numbers of hash functions and for the optimal integer number; the dots are a simulation with 2,000 keys and 200,000 absent probe keys.](./plots/bloom-filter-fpr.py)

Bloom filters are used well beyond LSM trees: in distributed joins to avoid shipping rows that will not match, in PostgreSQL's `bloom` extension as an index type, and in bioinformatics for $k$-mer membership in sequence assemblers and read classifiers.

## 8.5. Bitmap Indexes and Other Index Types

### 8.5.1. Bitmap Indexes

**Definition 8.5.1 (Bitmap Index)** For an attribute $A$ of a relation $r$ whose records are numbered $0, 1, \dots, n_r - 1$, a **bitmap index** stores, for each value $v$ of $A$, a bit vector of length $n_r$ whose bit $i$ is 1 if and only if record $i$ has $A = v$.

Bitmap indexes suit attributes with few distinct values, such as `tissue` or `treatment` in the running example. Conjunctions and disjunctions of conditions become bitwise operations on whole machine words: the samples with `tissue = 'lung' AND treatment = 'treated'` are the 1 bits of $B_{\text{lung}} \land B_{\text{treated}}$, and counting them is a population count. With five tissues and $n_r$ rows the index needs $5 n_r$ bits before compression, far less than a B+ tree with one entry per row. Sparse bit vectors are compressed by run-length schemes (BBC, WAH) or, in most current systems, with Roaring bitmaps, which split the vector into chunks of $2^{16}$ bits and store each chunk as a sorted array, a bitmap or runs, whichever is smallest.

Bitmap indexes are expensive to update (a new row changes a bit in the vector of its value, and compressed vectors must be partly rewritten) and are used mainly in data warehouses; Oracle offers them as a persistent index type. PostgreSQL has no persistent bitmap index, but its *bitmap index scan* builds bitmaps of matching heap pages on the fly from one or more ordinary indexes, combines them with AND and OR, and then reads the matching heap pages in physical order, which turns the random I/O of a secondary index into nearly sequential I/O.

### 8.5.2. Other Index Types

PostgreSQL's index access methods illustrate the range of index structures beyond B+ trees and hashing:

| Type | Structure | Typical use |
|---|---|---|
| `btree` | B+ tree (B-link tree) | default; equality, ranges, sorting, `LIKE 'abc%'` (with a suitable collation or operator class) |
| `hash` | linear-hashing variant | equality only |
| `gist` | generalized search tree: a balanced tree of predicates (e.g. bounding boxes, as in an R-tree) | geometry (PostGIS), ranges, nearest-neighbour search, exclusion constraints |
| `spgist` | space-partitioned trees (quadtrees, k-d trees, radix trees) | points, IP addresses, text prefixes |
| `gin` | generalized inverted index: a B-tree of elements with posting lists of rows | full-text search, `jsonb`, arrays |
| `brin` | block range index: the minimum and maximum (or another summary) of each range of 128 pages | very large tables whose physical order correlates with a column, such as timestamps of appended rows |

An *inverted index*, the structure behind GIN and behind search engines, maps each element (a word, an array element, a JSON key) to the list of rows that contain it. A BRIN index on the collection date of a table of a billion appended measurements takes a few hundred kilobytes, lets a range query skip all page ranges whose summary excludes the range, and costs almost nothing to maintain; it is useless if the column is not correlated with the physical order. Indexes for vectors and approximate nearest-neighbour search (HNSW, IVF), available in PostgreSQL through the `pgvector` extension, are discussed in [4.13.12](/4.13.12).

## 8.6. Indexes in SQL and Physical Design

### 8.6.1. Creating Indexes

The SQL standard does not define indexes (they are a physical matter), but every system supports essentially the same statement. In PostgreSQL:

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

Primary-key and unique constraints create their indexes automatically; foreign keys do not, although an index on the referencing columns is usually needed so that deleting a referenced row does not scan the referencing table. MySQL and SQLite support the same core syntax (composite, unique, expression and, in SQLite, partial indexes); MySQL's InnoDB clusters every table on its primary key, so a "secondary index" there always refers to the primary key.

### 8.6.2. Indexes at Work

The synthetic database of [4.13.7](/4.13.7) has the primary key `(sample_id, gene_id)` on `measurement`, with 100 samples and 5,000 genes. The following script, run with SQLite 3.45, times queries (median of 9 runs, data in the operating system's page cache) and prints the plan that SQLite chose.

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

The results show the main facts about indexes in one place.

- Without an index on `gene_id`, SQLite still avoids a full scan: the statistics collected by `ANALYZE` tell it that `sample_id` has only 100 distinct values, so it performs a skip scan of the primary-key index, one descent per sample (`ANY(sample_id)`).
- A secondary index on `gene_id` makes the lookup about seven times faster: one descent finds the 100 entries, followed by 100 record fetches by rowid.
- A covering index on `(gene_id, tpm)` answers the query from the index alone and is faster still.
- A secondary index helps only for selective predicates. Here the break-even point lies just below 4% of the rows; for `tpm > 1`, which matches 91% of the rows, the index plan is 16 times slower than the scan, because it fetches the records one by one in index order instead of reading the table sequentially. With the data on disk instead of in the page cache, random fetches are more expensive and the break-even fraction is lower still, typically a few percent or less. Deciding which plan to use from statistics is the task of the optimizer ([4.13.9](/4.13.9)).

### 8.6.3. Physical Design

Physical database design chooses the file organization, the indexes, partitioning and, in analytical systems, the sort order and the materialized views for a given schema and workload. Indexes are not free: each one occupies space (the covering index above is almost as large as the table) and must be updated by every insertion, deletion and update of an indexed column, and a write that would touch one page touches one more page per index. Common guidelines:

1. Start from the workload: the frequent and the expensive queries, and the rate of updates. An index that no query uses is pure cost; PostgreSQL's `pg_stat_user_indexes` counts how often each index is scanned.
2. Index the attributes of selective `WHERE` conditions and join conditions, including foreign keys.
3. Order the columns of a composite index by how queries use them: equality columns first, then the range or sort column. One index on $(A, B)$ can serve queries on $A$ and on $(A, B)$, but not, in general, on $B$.
4. Use covering indexes for frequent queries that read few columns, and partial indexes when queries concentrate on a small subset of rows.
5. Choose the clustering (in InnoDB and SQLite `WITHOUT ROWID`, the primary key) for the most important range queries, and prefer keys that increase over time, such as identity columns or time-ordered UUIDs (UUID version 7, which PostgreSQL 18 generates with `uuidv7()`), so that insertions go to the rightmost leaf instead of splitting pages all over the tree.
6. For bulk loads, drop secondary indexes, load, and recreate them: building an index by sorting is much cheaper than maintaining it row by row.
7. Measure: compare plans and timings before and after (§8.6.2), and keep statistics current with `ANALYZE`.

Automatic tools that propose indexes from a recorded workload (*index advisors*, such as SQL Server's Database Engine Tuning Advisor and the PostgreSQL extensions HypoPG and `pg_qualstats`) use the optimizer's cost model to evaluate hypothetical indexes without building them.

## Summary

- An index maps search-key values to record locations. Clustering indexes follow the file order and can be sparse; secondary indexes are dense, and fetching many records through them costs a random read each.
- The B+ tree is a balanced multilevel index with nodes at least half full; its height is at most $1 + \log_{\lceil n/2 \rceil} N$, which with fan-outs in the hundreds means three or four levels. Leaf splits copy a key up, internal splits move it up; real systems refine duplicates, compression, bulk loading, concurrency (B-link trees) and lazy deletion.
- Hash indexes support only equality; extendible hashing grows by doubling a directory and splitting one bucket at a time, linear hashing by splitting buckets in round-robin order.
- LSM trees turn writes into sequential appends of sorted runs merged by compaction, trading read and space amplification against write amplification; Bloom filters with about 10 bits per key screen out 99% of unnecessary run lookups.
- Bitmap indexes suit low-cardinality attributes in analytical workloads; inverted (GIN), generalized search tree (GiST) and block range (BRIN) indexes cover text, geometry and very large append-only tables.
- Physical design balances the speed of queries against the cost of updates; indexes help selective predicates, joins, sorting and covering, and must be checked against measured plans.
