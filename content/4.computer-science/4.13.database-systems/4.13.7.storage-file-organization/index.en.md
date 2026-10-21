---
title: Storage and File Organization
description: "How a DBMS stores relations on disk: the storage hierarchy and the I/O cost model; pages and the buffer pool (pinning, dirty pages, LRU and clock-sweep replacement, scan rings, why not mmap); fixed- and variable-length records, the PostgreSQL tuple layout and TOAST; slotted pages and record identifiers; heap, sequential, clustered, hashed and partitioned file organizations with their costs; row stores, column stores, PAX, compression and Parquet; the system catalog."
---

The chapters so far treated a **relation** as a mathematical set of **tuples** and **SQL** as a language for describing the tuples we want. From this chapter on we open the box and ask how a database management system actually keeps those tuples, finds them and changes them safely. The first question is physical: a table of a hundred million rows does not fit in memory, must survive a power failure and is read by queries that touch either one row or all of them. The answer is a layered design. At the bottom, files on a storage device are divided into fixed-size pages; a buffer pool keeps the pages currently in use in memory; inside a page, records are laid out so that they can grow, shrink and move without breaking the references to them; and a file organization decides which records go into which page. The same ideas appear one level lower in the operating system ([4.11.4](/4.11.4) for paging and page replacement, [4.11.7](/4.11.7) for file systems, [4.11.8](/4.11.8) for devices), but a DBMS knows far more about its access patterns than an operating system can, and it uses that knowledge. Indexes, which are additional structures for finding records quickly, are the subject of [4.13.8](/4.13.8); the cost model introduced here is the basis of query optimization in [4.13.9](/4.13.9), and the rules for writing dirty pages back to disk are completed by logging and recovery in [4.13.10](/4.13.10).

The running example is the gene-expression **database** of [4.13.3](/4.13.3#sec-3.2.3): tables `gene`, `sample` and `measurement(sample_id, gene_id, tpm)` among others. For measurements of storage we use a synthetic version of the same **schema** with 5,000 genes and 100 samples, that is, 500,000 rows in `measurement`.

## 7.1. The Storage Hierarchy

### 7.1.1. Devices and Their Costs

A **database** lives on several kinds of storage at once. The table gives typical orders of magnitude for current hardware; the exact numbers change every few years, the ratios much more slowly.

| Storage | Random access latency | Sequential bandwidth | Persistent | Role in a DBMS |
|---|---|---|---|---|
| CPU caches | 1–40 ns | hundreds of GB/s | no | execution of operators ([4.10](/4.10)) |
| DRAM | about 100 ns | tens of GB/s per socket | no | buffer pool, hash tables, sort space |
| NVMe flash SSD | 20–100 µs | 3–14 GB/s | yes | data files, log |
| Hard disk drive | 5–10 ms | 150–300 MB/s | yes | bulk and archival data, backups |
| Cloud object storage (e.g. Amazon S3) | 10–100 ms to first byte | high in aggregate | yes | data lakes, cloud warehouses |

Two facts dominate the design of storage engines. First, persistent storage is between two and five orders of magnitude slower than memory, so the number of page transfers between disk and memory, not the number of CPU instructions, usually determines the running time of a query on data that is not cached. Second, sequential access is much cheaper than **random access**. On a hard disk a random read pays a **seek time** and a **rotational latency** of several milliseconds, after which the next megabyte streams in about as fast; on a flash SSD the gap is smaller but still present, because the **flash translation layer** and the device's internal parallelism favour large, aligned requests ([4.11.8](/4.11.8#sec-8.3)). **Database systems** therefore prefer algorithms that read and write long runs of consecutive pages, and they use **RAID** or replication across machines for capacity and availability.

### 7.1.2. Pages and the I/O Cost Model

**Definition 7.1.1 (Page)** A **page** (also called a **block**) is the unit of data transfer between persistent storage and memory in a DBMS: a contiguous, fixed-size piece of a database file, identified by a **page identifier** such as (file number, page number). All reads and writes of the storage manager are reads and writes of whole pages.

Typical **page** sizes are 8 KiB in PostgreSQL, 16 KiB in MySQL's InnoDB engine and 4 KiB by default in SQLite (configurable from 512 bytes to 64 KiB). A database page usually consists of one or several file-system blocks and is unrelated to the virtual-memory page of [4.11.4](/4.11.4), although both are commonly 4 KiB or a multiple of it.

Because transfers dominate, the cost model of the following chapters counts pages.

**Definition 7.1.2 (I/O Cost Model)** The I/O cost of an algorithm is the number of page transfers it performs between persistent storage and memory. When random and sequential accesses must be distinguished, the cost is written as $b \cdot t_T + S \cdot t_S$, where $b$ is the number of pages transferred, $S$ the number of random accesses (seeks), $t_T$ the time to transfer one page and $t_S$ the time of one random access.

For a hard disk with $t_S = 4\,\mathrm{ms}$ and a bandwidth of $200\,\mathrm{MB/s}$, transferring an 8 KiB page takes $t_T \approx 0.04\,\mathrm{ms}$, so one random access costs as much as reading about a hundred pages sequentially. CPU costs are ignored in this model; for data in memory and for column stores (§7.5) they matter, and real optimizers add them as separate terms ([4.13.9](/4.13.9)).

**Remark 7.1.1** Whether a page should be kept in memory at all is an economic question. Gray and Putzolu's *five-minute rule* (1987) compares the price of the memory that holds a page with the price of the device bandwidth needed to fetch it again: a page that is referenced more often than once per break-even interval should stay in memory. The interval was about five minutes for disks and DRAM in 1987; the rule has been re-evaluated for each generation of hardware since (for flash, between DRAM and SSD and between SSD and disk), and the break-even interval moves with prices and device speeds.

## 7.2. The Buffer Pool

### 7.2.1. Structure and Interface

A **DBMS** does not read a **page** from disk every time an operator needs it. It keeps recently used pages in a region of main memory that it manages itself.

**Definition 7.2.1 (Buffer Pool)** The **buffer pool** is an array of page-sized memory slots called **frames**, managed by the **buffer manager**. For each frame the buffer manager records which page it holds, a **pin count** (the number of current users of the page; a pinned page may not be evicted), a **dirty flag** (whether the page was modified since it was read), and the bookkeeping of the replacement policy. A hash table, the **buffer table**, maps page identifiers to frames.

The interface is small. An operator asks for a page with `pin(page_id)` and receives a pointer to the frame; when it has finished with the page it calls `unpin(page_id, dirty)`. In between, it may read and modify the page in place.

**Algorithm 7.2.1 (Fetching a Page)** To pin page $p$:

1. Look up $p$ in the buffer table. If it is present, increment the pin count of its frame and return the frame (a *hit*).
2. Otherwise (a *miss*), choose a victim frame with pin count $0$ according to the **replacement policy**. If no such frame exists, wait or report an error.
3. If the victim is dirty, write its page back to disk first. In a system with **write-ahead logging** the log records describing the changes to that page must reach stable storage before the page itself ([4.13.10](/4.13.10)).
4. Read $p$ into the frame, update the buffer table, set the pin count to $1$ and clear the dirty flag.

In PostgreSQL the **buffer pool** is the shared memory area `shared_buffers` (128 MB by default; production servers commonly give it about a quarter of RAM), shared by all server **processes**; in InnoDB it is the *buffer pool* sized by `innodb_buffer_pool_size`; in SQLite each connection has its own **page cache**. A modified page is normally written back long after it was changed, by a background writer or at a checkpoint, so that many changes to the same page cost one write. Since PostgreSQL 18, reads can also be issued asynchronously (setting `io_method`: `worker` by default, `io_uring` on Linux builds that support it, or `sync`), so that a sequential scan or `VACUUM` keeps several page reads in flight instead of waiting for each one.

### 7.2.2. Replacement Policies

When the buffer pool is full, the **buffer manager** must decide which unpinned page to evict. This is the **page replacement policy** problem of **virtual memory** ([4.11.4](/4.11.4#sec-4.6.2)) again, and the classical answers carry over: **least recently used** (LRU) evicts the page whose last use lies furthest in the past, and the **clock algorithm** approximates LRU cheaply with one reference bit per frame and a rotating hand. Two features of **database** workloads change the picture.

The first is *sequential flooding*. A query that scans a large table touches each page once, never again. Under **LRU**, every page of the scan enters the pool as the most recently used page and pushes out pages that other queries use repeatedly, such as the root pages of indexes. Worse, if a table of $B + 1$ pages is scanned repeatedly with a pool of $B$ frames, LRU evicts exactly the page that will be needed next and every access misses, while a policy that evicts the most recently used page would hit on almost every access.

The second is that the DBMS knows the access pattern in advance: the query plan says which pages will be scanned once, which index pages are hot and which pages a nested-loop **join** will reread. Real systems exploit this in several ways.

| System | Policy |
|---|---|
| PostgreSQL | *Clock sweep* with a usage count per buffer: each access increments the count (up to 5), the sweeping hand decrements it and evicts a buffer whose count is 0. Large sequential scans, `VACUUM`, `COPY` and bulk writes use a *buffer access strategy*: a small ring of buffers reused circularly, so that they cannot flood the shared pool. |
| MySQL InnoDB | LRU list split into a *young* and an *old* sublist (by default the old sublist holds 3/8 of the pool). A newly read page enters at the head of the old sublist and moves to the young sublist only if it is accessed again after `innodb_old_blocks_time` (1 second); a scan therefore ages out through the old sublist. |
| Research and other systems | LRU-K (evict by the time of the $K$-th most recent access), 2Q, ARC; per-query hints that a page will not be reused. |

The following simulation compares LRU, clock sweep, and clock sweep with a private scan ring on a workload in which 90% of point accesses go to 50 hot pages and a 1,000-page sequential scan runs after every 2,000 point accesses. The pool has 100 frames in all cases; the table reports the hit rate of the point accesses.

```python
from collections import OrderedDict
import random


class LRUPool:
    """Buffer pool that evicts the least recently used unpinned page."""

    def __init__(self, n_frames):
        self.n_frames = n_frames
        self.frames = OrderedDict()   # page id -> page contents
        self.hits = self.misses = 0

    def get_page(self, page_id):
        if page_id in self.frames:
            self.hits += 1
            self.frames.move_to_end(page_id)        # most recently used
        else:
            self.misses += 1
            if len(self.frames) == self.n_frames:
                self.frames.popitem(last=False)     # evict the LRU page
            self.frames[page_id] = f"<page {page_id}>"  # read from disk
        return self.frames[page_id]


class ClockSweepPool:
    """PostgreSQL-style clock sweep with a usage count capped at 5."""

    MAX_USAGE = 5

    def __init__(self, n_frames):
        self.n_frames = n_frames
        self.page_of = [None] * n_frames   # frame -> page id
        self.usage = [0] * n_frames        # frame -> usage count
        self.frame_of = {}                 # page id -> frame (the buffer table)
        self.hand = 0
        self.hits = self.misses = 0

    def get_page(self, page_id):
        f = self.frame_of.get(page_id)
        if f is not None:
            self.hits += 1
            self.usage[f] = min(self.usage[f] + 1, self.MAX_USAGE)
            return f
        self.misses += 1
        while True:                        # sweep until a frame with count 0
            f = self.hand
            self.hand = (self.hand + 1) % self.n_frames
            if self.page_of[f] is None or self.usage[f] == 0:
                break
            self.usage[f] -= 1
        if self.page_of[f] is not None:
            del self.frame_of[self.page_of[f]]
        self.page_of[f], self.usage[f] = page_id, 1
        self.frame_of[page_id] = f
        return f


def point_hit_rate(trace, pool, ring=None):
    """Hit rate of the point accesses (page ids < 10,000) only."""
    hits = total = 0
    for p in trace:
        target = ring if (ring is not None and p >= 10_000) else pool
        before = target.hits
        target.get_page(p)
        if p < 10_000:
            total += 1
            hits += target.hits - before
    return hits / total


random.seed(0)
# Workload: 90% of point accesses go to 50 hot pages (index roots, a small
# lookup table); after every 2,000 point accesses a query scans 1,000 pages
# of a large table (page ids 10,000-10,999).
trace = []
for rnd in range(20):
    trace += [random.randrange(50) if random.random() < 0.9
              else random.randrange(50, 5000) for _ in range(2000)]
    trace += list(range(10_000, 11_000))

print(f"LRU, 100 frames:               {point_hit_rate(trace, LRUPool(100)):.3f}")
print(f"clock sweep, 100 frames:       {point_hit_rate(trace, ClockSweepPool(100)):.3f}")
print(f"clock sweep, 84 frames + ring: "
      f"{point_hit_rate(trace, ClockSweepPool(84), LRUPool(16)):.3f}")
```

```text
LRU, 100 frames:               0.874
clock sweep, 100 frames:       0.874
clock sweep, 84 frames + ring: 0.898
```

The best possible hit rate here is about 0.9, since the 10% of point accesses to the 4,950 cold pages almost always miss. Plain LRU and plain clock sweep both lose the hot pages to every scan and must reload them afterwards; the scan ring keeps them, although it leaves the point queries fewer frames. The effect grows with the ratio of scan length to pool size and with the cost of reloading the hot set.

### 7.2.3. Why Not Let the Operating System Do It?

The **operating system** already caches file pages in its **page cache** ([4.11.7](/4.11.7#sec-7.2.5)), and **memory mapping** a database file with `mmap` would let the kernel's virtual-memory system play the role of the buffer pool. Most **database systems** nevertheless manage their own buffers, for reasons that follow from the requirements of later chapters:

- *Write ordering.* Recovery requires that a dirty page is not written before its log records ([4.13.10](/4.13.10)). With `mmap` the kernel may write a modified page back at any moment, and the DBMS cannot prevent it.
- *Replacement and prefetching.* The kernel does not know that a page belongs to a one-time scan or to the root of an index; the DBMS does.
- *Errors and stalls.* With `mmap`, an I/O error arrives as a signal and a **page fault** stalls the **thread** invisibly; with explicit reads the DBMS can schedule I/O asynchronously and handle errors as return values.
- *Double buffering.* If the DBMS caches a page and the kernel caches the same page, memory is wasted. InnoDB avoids it with direct I/O (`O_DIRECT`); PostgreSQL traditionally relies on buffered I/O and accepts some double caching, sizing `shared_buffers` well below RAM so that the page cache holds the rest.

A 2022 study by Crotty, Leis and Pavlo ("Are You Sure You Want to Use MMAP in Your Database Management System?") measured these problems in practice. Systems that use `mmap` successfully, such as LMDB and SQLite's optional **memory-mapped I/O** mode, are designs in which the write path is controlled separately (for instance by **copy-on-write**), or in which `mmap` is used only for reading.

## 7.3. Record Formats

### 7.3.1. Fixed-Length Records

A *record* is the stored representation of one **tuple**. If every **attribute** has a fixed size (integers, floating-point numbers, fixed-length character strings), every record of the **relation** has the same length $s$, and record $i$ of a page starts at byte $h + i\,s$, where $h$ is the size of the page header. Deletion leaves a hole. Moving the following records up costs work and changes their addresses; moving only the last record into the hole changes one address; the usual solution is to leave the hole and chain all free record positions into a *free list* whose head is stored in the page header, so that the next insertion reuses one of them.

### 7.3.2. Variable-Length Records

Strings of variable length, nullable attributes, arrays and JSON values make records variable in length. The standard layout has three parts.

1. A *header* with the record length, a *null bitmap* with one bit per attribute (a **null** attribute occupies no further space), and system information (in PostgreSQL the transaction identifiers needed for concurrency control, [4.13.11](/4.13.11)).
2. A fixed-size part: the values of the fixed-length attributes and, for each variable-length attribute, an (offset, length) pair or a length prefix.
3. The variable-length values themselves.

The layout of a **heap** tuple in PostgreSQL, from the documentation of the **page** format, is a concrete case. Each tuple starts with a 23-byte header (`t_xmin` and `t_xmax`, the identifiers of the inserting and deleting transactions; `t_cid`; `t_ctid`, the location of this or a newer version of the row; two words of flags with the number of attributes; and `t_hoff`, the offset of the user data), followed by the null **bitmap** if any attribute is null, padded so that the data starts at a multiple of the platform's maximum alignment, 8 bytes on current 64-bit machines. Each value is aligned according to its type: a `double precision` or `bigint` starts at a multiple of 8, an `integer` at a multiple of 4, while a short `text` value (under 127 bytes) has a 1-byte length header and needs no alignment.

**Example 7.3.1** A row of `measurement(sample_id text, gene_id text, tpm numeric(10, 2))` such as `('S01', 'ENSG00000141510', 35.20)` takes 24 bytes of header (23 rounded up to 8), 4 bytes for `sample_id` (1-byte length and 3 characters), 16 bytes for `gene_id` and about 7 bytes for `tpm` (a `numeric` value is variable-length: a 1-byte length, a 2-byte header and one 2-byte digit in base 10,000 for each of `35` and `.20`): 51 bytes, which the next tuple's alignment rounds to 56. A `double precision` column would instead take 8 bytes aligned to a multiple of 8, with 4 bytes of padding before it, and also give 56. With the 4-byte slot of §7.3.3 and a 24-byte page header, an 8 KiB page holds about $\lfloor 8168 / 60 \rfloor = 136$ such rows, and the 500,000 rows of the synthetic data set need about 3,700 pages, 30 MB. The values themselves amount to only $3 + 15 + 8 = 26$ bytes per row: per-row overhead of this kind is one reason why analytical systems use the column layouts of §7.5.

Column order affects padding. A table declared as `(a boolean, b bigint, c boolean, d bigint)` has data of $1 + 7 + 8 + 1 + 7 + 8 = 32$ bytes per row; declared as `(b bigint, d bigint, a boolean, c boolean)` it needs only $8 + 8 + 1 + 1 = 18$ bytes, rounded to 24 at the end of the tuple. PostgreSQL stores columns in declaration order, so placing fixed-width, strongly aligned columns first is a common space optimization for very large tables.

Values too large for a page are stored elsewhere. PostgreSQL's TOAST mechanism ("The Oversized-Attribute Storage Technique") first compresses large variable-length values and, if the row is still larger than a threshold of about 2 KB, moves them in chunks to a separate TOAST table, leaving a pointer in the row; InnoDB stores long columns of its `DYNAMIC` row format on separate overflow pages with a 20-byte pointer in the record; SQLite chains overflow pages from the cell.

### 7.3.3. Slotted Pages

Inside a page, variable-length records must be able to grow, shrink and move (for example when the page is compacted) without invalidating the references to them held by indexes. The standard structure adds one level of indirection.

**Definition 7.3.1 (Slotted Page)** A **slotted page** consists of a header, an array of **slots** and a record area. The header stores the number of slots and the boundaries of the free space; slot $i$ stores the offset and length of record $i$, or marks the slot as unused. The slot array grows from the beginning of the page and the records grow from the end, with the free space between them. A record is addressed by its **record identifier** (RID), the pair (page identifier, slot number).

![A slotted page. Each slot points to its record; slot 3 is unused because its record was deleted. Records can move inside the page as long as their slots are updated, so a record identifier stays valid.](./plots/slotted-page.py)

Insertion takes a new slot (or reuses an unused one) and places the record at the end of the free space. Deletion marks the slot unused; the space of the record can be reclaimed by compacting the records towards the end of the page and updating their offsets, which leaves every **RID** valid. If a record grows and no longer fits, it is moved to another page and its old slot keeps a *forwarding address*.

In PostgreSQL every page has this form: a 24-byte page header (with `pd_lower` and `pd_upper` delimiting the free space and `pd_lsn`, the log position of the last change, used in recovery), 4-byte *line pointers* as slots, and the tuples from the end of the page. The RID is called a *tuple identifier* and is visible as the system column `ctid`: the query `SELECT ctid, * FROM measurement` shows values such as `(0,1)`, `(0,2)`, meaning page 0, line pointers 1, 2. An update in PostgreSQL writes a new version of the row with a new `ctid` and links the old version to it ([4.13.11](/4.13.11)). SQLite's **B-tree** pages are **slotted pages** too: a *cell pointer array* of 2-byte offsets follows the page header and the cells fill the page from the end.

## 7.4. File Organization

How records are assigned to **pages** determines which operations are cheap. A **relation** is stored as one or more files (in PostgreSQL, the file `base/<database oid>/<relfilenode>`, split into 1 GB segments, together with a free space map and a visibility map stored as separate forks; in SQLite, the whole **database** is a single file).

### 7.4.1. Heap Files

**Definition 7.4.1 (Heap File)** A **heap file** stores the records of a relation in no particular order: a new record goes into any page with enough free space, and the file supports scanning all records, fetching a record by its RID, insertion and deletion.

To find a page with room for a new record without reading the whole file, the **DBMS** maintains a directory of free space. PostgreSQL's *free space map* records the approximate free space of each page in a small tree, and its *visibility map* records which pages contain only rows visible to all transactions; the latter lets `VACUUM` skip pages and lets index-only scans avoid visiting the **heap** ([4.13.8](/4.13.8)). **Heap files** are the default table organization in PostgreSQL, Oracle and SQL Server (for tables without a clustered index).

### 7.4.2. Sequential Files

**Definition 7.4.2 (Sequential File)** A **sequential file** stores the records of a relation sorted by a *search key*, one or more attributes chosen for this purpose, so that the records can be read in key order and a range of keys occupies consecutive pages.

Searching by key can use **binary search** over the pages, and a range query reads only the pages of the range. The price is insertion: a new record belongs at a fixed position. If its page is full, it goes to an *overflow page* chained from there, and after many insertions the file must be *reorganized*, that is, rewritten in order. Pure **sequential files** are rare today; their role is taken over by B+-tree organizations, which keep the order dynamically ([4.13.8](/4.13.8)).

### 7.4.3. Clustered Organizations

An organization in which records with equal or neighbouring key values are stored physically together is called *clustered*. The most important form today stores the table itself in the leaves of a **B+ tree** on the **primary key**.

**Definition 7.4.3 (Index-Organized Table)** An **index-organized table** (or clustered table) stores its records in the leaf pages of a B+ tree ordered by a key, usually the primary key; there is no separate heap file. Other indexes on the table refer to a record by its key value instead of by a RID.

InnoDB stores every table in this way, clustered on the primary key (or on a hidden row identifier if the table has none), and its secondary indexes store primary-key values. SQLite stores an ordinary table as a **B-tree** keyed by its 64-bit `rowid`; a table declared `WITHOUT ROWID` is instead a B-tree keyed by its primary key. PostgreSQL has only heap files; its `CLUSTER` command sorts a table once according to an index, but later insertions do not maintain the order.

The difference is visible in SQLite. The `measurement` table of the running example has a composite primary key on `(sample_id, gene_id)`. Stored normally, it is a rowid B-tree plus a separate index that enforces the primary key and repeats both key columns; stored `WITHOUT ROWID`, the records are kept in key order in one tree. With the synthetic data set (500,000 rows, 4 KiB pages), the virtual table `dbstat` reports the pages of each B-tree:

```sql
CREATE TABLE measurement_clustered (
    sample_id  text REFERENCES sample (sample_id),
    gene_id    text REFERENCES gene (gene_id),
    tpm        numeric(10, 2) NOT NULL CHECK (tpm >= 0),
    PRIMARY KEY (sample_id, gene_id)
) WITHOUT ROWID;
INSERT INTO measurement_clustered SELECT * FROM measurement;

SELECT name, count(*) AS pages
FROM dbstat
WHERE name LIKE '%measurement%'
GROUP BY name
ORDER BY name;
```

```text
+--------------------------------+-------+
|              name              | pages |
+--------------------------------+-------+
| measurement                    | 4550  |
| measurement_clustered          | 4730  |
| sqlite_autoindex_measurement_1 | 4060  |
+--------------------------------+-------+
```

The **clustered table** needs 4,730 pages instead of $4{,}550 + 4{,}060 = 8{,}610$, and a query for all measurements of one sample reads a few consecutive leaf pages. In exchange, insertions in random key order split pages in the middle of the tree, and every secondary index lookup costs a second tree descent through the primary key.

A related idea is *multitable clustering*: storing the rows of several relations that are usually joined (each sample followed by its measurements, say) in the same pages. It speeds up that **join** and slows down everything else, and today it survives mainly in specialized systems.

### 7.4.4. Hashed and Partitioned Files

A *hashed file* computes the page of a record from a **hash function** of a key, so that an equality search reads one page (plus overflow pages); hashing as an index structure is treated in [4.13.8](/4.13.8#sec-8.3).

**Definition 7.4.4 (Partitioning)** **Partitioning** divides a table into disjoint parts, the partitions, according to the value of a *partition key*: by ranges of values (*range partitioning*), by lists of values (*list partitioning*) or by a hash of the key (*hash partitioning*). Each partition is stored as a separate table, and the system routes each row to its partition.

PostgreSQL supports declarative **partitioning** with all three methods:

```sql
CREATE TABLE measurement_log (
    sample_id   text,
    gene_id     text,
    tpm         double precision,
    measured_on date NOT NULL
) PARTITION BY RANGE (measured_on);

CREATE TABLE measurement_log_2025 PARTITION OF measurement_log
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
CREATE TABLE measurement_log_2026 PARTITION OF measurement_log
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');
```

A query with `WHERE measured_on >= '2026-03-01'` reads only the 2026 partition (*partition pruning*), and old data can be removed by dropping a partition instead of deleting millions of rows. The same idea, applied across machines, is sharding ([4.13.12](/4.13.12)).

### 7.4.5. Comparing the Organizations

The following comparison, in the style of Ramakrishnan and Gehrke, counts page I/Os for a relation of $B$ pages, assuming an equality search on a key (at most one match), a range search matching $m$ pages, and a hashed file whose pages are 80% full.

| Operation | Heap file | Sorted file | Hashed file |
|---|---|---|---|
| Scan all records | $B$ | $B$ | $1.25\,B$ |
| Equality search | $0.5\,B$ on average | $\log_2 B$ | $1$ |
| Range search | $B$ | $\log_2 B + m$ | $1.25\,B$ |
| Insert | $2$ (read and write one page) | search $+\ B$ (shift the rest) | $2$ |
| Delete (given the key) | search $+\ 1$ | search $+\ B$ | $2$ |

No organization wins everywhere; this is why tables are usually stored as heaps or B+-tree organized files and supplemented by indexes for the other access paths.

## 7.5. Row Stores and Column Stores

### 7.5.1. Three Layouts

Everything so far stored each record contiguously. That is ideal for transactional workloads (**OLTP**, **online transaction processing**), whose queries read or write a few complete rows: one **page** access fetches the whole row. Analytical workloads (OLAP, online analytical processing) are different: a query such as "average TPM per tissue over all measurements" reads millions of rows but only two or three columns. With rows stored contiguously, it reads every byte of every row from disk and through the CPU caches, almost all of it useless.

**Definition 7.5.1 (Row Store and Column Store)** In the **N-ary storage model** (NSM, *row store*), the values of all attributes of a record are stored together and pages hold whole records. In the **decomposition storage model** (DSM, *column store*), the values of each attribute are stored together, in record order, in a separate sequence of pages; the $i$-th values of all columns together form the $i$-th record. The **PAX** layout (Partition Attributes Across) is a hybrid: records are assigned to pages (or larger *row groups*) as in NSM, but inside each, the values are grouped by column as in DSM.

The column layout is the **database** analogue of storing a table in **long format** and processing it column by column, as NumPy and pandas do ([4.4.5](/4.4.5)): an operator reads one contiguous array of values of one type, which is ideal for CPU caches, SIMD instructions and compression. Its cost is in reconstructing rows and in updates: inserting one row touches every column. **Column stores** therefore buffer insertions in a row-oriented area and merge them into the columns in batches.

| | Row store | Column store |
|---|---|---|
| Typical workload | OLTP: point queries, small updates | OLAP: scans and aggregates over few columns |
| Reads for a query on $k$ of $n$ columns | all $n$ columns | $k$ columns |
| Compression | moderate (mixed types in a page) | high (one type, often sorted or repetitive) |
| Insert or update of one row | one page | one page per column, usually batched |
| Examples | PostgreSQL, MySQL InnoDB, SQLite, Oracle | DuckDB, ClickHouse, Snowflake, BigQuery, Amazon Redshift; file formats Parquet and ORC |

### 7.5.2. Compression

Values of one column are similar, and column stores compress them with simple schemes that can often be evaluated without decompressing:

- *Dictionary encoding*: replace each value by a small integer code into a dictionary of distinct values. A column `tissue` with five distinct strings needs 3 bits per row.
- *Run-length encoding* (RLE): store (value, run length) pairs; effective on sorted or clustered columns. A predicate can be evaluated once per run.
- *Bit-packing and frame of reference*: store integers as differences from a base value, using only as many bits as the range requires; *delta encoding* stores differences between consecutive values (good for sorted keys and timestamps).
- *Floating-point schemes* such as ALP (adaptive lossless floating-point compression, used by DuckDB), which exploit the fact that most stored doubles are decimal numbers with few digits.
- General-purpose compressors (Snappy, LZ4, Zstandard) on top of the encoded pages.

### 7.5.3. Column Storage in Practice

DuckDB (here version 1.5), an embedded analytical database ([4.13.12](/4.13.12)), stores tables in row groups of 122,880 rows with one compressed segment per column, and chooses the compression of each segment by trying the available methods. Loading the 500,000 synthetic measurements and exporting them to the Parquet file format shows both layouts:

```python
import duckdb, os
con = duckdb.connect("col.duckdb")
con.execute("""CREATE TABLE measurement (
    sample_id text, gene_id text, tpm numeric(10, 2) NOT NULL)""")
con.execute("INSERT INTO measurement SELECT * FROM read_csv('m.csv')")
con.execute("CHECKPOINT")
con.execute("COPY measurement TO 'measurement.parquet' (FORMAT parquet)")
print(con.sql("""
SELECT column_name, compression, count(*) AS segments
FROM pragma_storage_info('measurement')
WHERE segment_type <> 'VALIDITY'
GROUP BY ALL ORDER BY column_name, compression"""))
print(con.sql("""
SELECT row_group_id, path_in_schema AS column_name, compression,
       total_compressed_size AS compressed, total_uncompressed_size AS uncompressed
FROM parquet_metadata('measurement.parquet')
WHERE row_group_id = 0"""))
print(con.sql("SELECT count(DISTINCT row_group_id) AS row_groups FROM parquet_metadata('measurement.parquet')"))
for f in ["m.csv", "measurement.parquet", "big.db"]:
    print(f, os.path.getsize(f))
```

```text
┌─────────────┬─────────────┬──────────┐
│ column_name │ compression │ segments │
│   varchar   │   varchar   │  int64   │
├─────────────┼─────────────┼──────────┤
│ gene_id     │ Dictionary  │        8 │
│ sample_id   │ Dictionary  │        5 │
│ tpm         │ BitPacking  │        8 │
└─────────────┴─────────────┴──────────┘

┌──────────────┬─────────────┬─────────────┬────────────┬──────────────┐
│ row_group_id │ column_name │ compression │ compressed │ uncompressed │
│    int64     │   varchar   │   varchar   │   int64    │    int64     │
├──────────────┼─────────────┼─────────────┼────────────┼──────────────┤
│            0 │ sample_id   │ SNAPPY      │        234 │          320 │
│            0 │ gene_id     │ SNAPPY      │     176321 │       295210 │
│            0 │ tpm         │ SNAPPY      │     269534 │       319435 │
└──────────────┴─────────────┴─────────────┴────────────┴──────────────┘

┌────────────┐
│ row_groups │
│   int64    │
├────────────┤
│          5 │
└────────────┘

m.csv 13170537
measurement.parquet 1954422
big.db 35749888
```

The rows are ordered by sample, so within a row group the column `sample_id` consists of a few long runs and its column chunk occupies 234 bytes for over 100,000 values; `gene_id` repeats the same 5,000 identifiers and is dictionary-encoded; `tpm`, a decimal with two digits after the point, is stored as integers counting hundredths and bit-packed. The Parquet file takes 2.0 MB, against 13.2 MB for the same data as CSV and 35.7 MB for the SQLite database, which stores each row with its header and the primary-key index besides. A Parquet file is itself a **PAX** layout: row groups contain one *column chunk* per column, chunks consist of pages, and a footer records the **schema** and, per chunk, statistics such as the minimum and maximum value, which let a reader skip row groups that cannot satisfy a predicate.

Between the two worlds, *hybrid transactional/analytical processing* (HTAP) systems keep a **row store** for transactions and a column copy for analytics, synchronized continuously; examples are SQL Server's columnstore indexes, Oracle's In-Memory option and TiDB's TiFlash replicas.

## 7.6. The System Catalog

A **DBMS** stores the description of the **database** (tables, columns and their types, constraints, indexes, views, users and **privileges**, statistics) in the database itself, as ordinary relations: the system catalog or data dictionary of [4.13.1](/4.13.1#sec-1.4). The storage manager needs it to interpret the bytes of a page: the catalog says how many attributes a record has, their types and order, and which file and pages hold which relation.

In SQLite the catalog is a single table, `sqlite_schema`, stored in **page** 1 of the database file. Its column `rootpage` gives the page on which each **B-tree** starts; for the synthetic database:

```sql
SELECT type, name, tbl_name, rootpage FROM sqlite_schema;
```

```text
+-------+---------------------------------+--------------+----------+
| type  |              name               |   tbl_name   | rootpage |
+-------+---------------------------------+--------------+----------+
| table | gene                            | gene         | 2        |
| index | sqlite_autoindex_gene_1         | gene         | 3        |
| index | sqlite_autoindex_gene_2         | gene         | 4        |
| table | sample                          | sample       | 5        |
| index | sqlite_autoindex_sample_1       | sample       | 6        |
| table | measurement                     | measurement  | 7        |
| index | sqlite_autoindex_measurement_1  | measurement  | 8        |
| table | pathway                         | pathway      | 9        |
| index | sqlite_autoindex_pathway_1      | pathway      | 10       |
| index | sqlite_autoindex_pathway_2      | pathway      | 11       |
| table | gene_pathway                    | gene_pathway | 12       |
| index | sqlite_autoindex_gene_pathway_1 | gene_pathway | 13       |
| table | sqlite_stat1                    | sqlite_stat1 | 8728     |
+-------+---------------------------------+--------------+----------+
```

Each `PRIMARY KEY` and `UNIQUE` constraint produced an automatic index, and `ANALYZE` created `sqlite_stat1` for the optimizer's statistics. The same database file, measured with `dbstat`, shows how the space is distributed:

```sql
SELECT name, count(*) AS pages,
       sum(pagetype = 'leaf') AS leaf_pages,
       sum(ncell) AS cells,
       round(avg(unused) * 100.0 / 4096, 1) AS pct_unused
FROM dbstat
GROUP BY name
ORDER BY pages DESC;
```

```text
+---------------------------------+-------+------------+--------+------------+
|              name               | pages | leaf_pages | cells  | pct_unused |
+---------------------------------+-------+------------+--------+------------+
| measurement                     | 4550  | 4538       | 504537 | 0.6        |
| sqlite_autoindex_measurement_1  | 4060  | 4022       | 500000 | 12.7       |
| gene                            | 57    | 56         | 5055   | 2.8        |
| sqlite_autoindex_gene_1         | 33    | 32         | 5000   | 14.7       |
| sqlite_autoindex_gene_2         | 19    | 18         | 5000   | 17.8       |
| sqlite_stat1                    | 1     | 1          | 4      | 95.2       |
| sqlite_schema                   | 1     | 1          | 13     | 53.0       |
| sqlite_autoindex_sample_1       | 1     | 1          | 100    | 73.0       |
| sqlite_autoindex_pathway_2      | 1     | 1          | 0      | 99.8       |
| sqlite_autoindex_pathway_1      | 1     | 1          | 0      | 99.8       |
| sqlite_autoindex_gene_pathway_1 | 1     | 1          | 0      | 99.8       |
| sample                          | 1     | 1          | 100    | 9.6        |
| pathway                         | 1     | 1          | 0      | 99.8       |
| gene_pathway                    | 1     | 1          | 0      | 99.8       |
+---------------------------------+-------+------------+--------+------------+
```

The table `measurement` was filled by appending rows in rowid order, and SQLite packs the leaves of such a tree almost completely (0.6% unused); the index B-trees are balanced differently and leave 12–18% of their pages free, which makes later insertions in the middle cheaper. The cell count of `measurement` exceeds the number of rows because interior pages of a rowid tree also contain cells (one per child pointer).

PostgreSQL's catalog consists of tables such as `pg_class` (one row per table, index, sequence or view, with the estimated number of pages `relpages` and of rows `reltuples`), `pg_attribute` (one row per column) and `pg_index`. The **SQL** standard defines a portable view of the catalog, the `information_schema`, which PostgreSQL, MySQL and DuckDB implement; SQLite offers `PRAGMA table_info(...)` and table-valued functions such as `pragma_table_info('gene')` instead.

## Summary

- Storage is a hierarchy in which persistent devices are orders of magnitude slower than memory and **random access** is slower than sequential access; the **I/O cost model** therefore counts **page** transfers, separating seeks when necessary.
- The buffer pool caches pages in frames with pin counts and dirty flags. Database workloads defeat plain LRU through sequential flooding, so systems use clock sweep with usage counts, scan rings (PostgreSQL) or a split LRU list (InnoDB). DBMSs manage their own buffers instead of relying on `mmap`, mainly to control write ordering for recovery.
- Records carry a header with a null bitmap and system information; alignment padding and per-row headers make small rows expensive. Large values go out of line (TOAST, overflow pages).
- Slotted pages give each record a stable identifier (page, slot) while allowing records to move within the page.
- Heap files, sequential files, index-organized tables, hashed files and partitioned tables trade the costs of scans, searches, range queries and updates differently.
- Row stores suit transactions, column stores suit analytics; column stores compress well with dictionary, run-length and bit-packing schemes, and Parquet is a PAX layout used as an exchange format.
- The catalog describes the database in its own tables; SQLite's `sqlite_schema`, PostgreSQL's `pg_class` and the standard `information_schema` are examples.
