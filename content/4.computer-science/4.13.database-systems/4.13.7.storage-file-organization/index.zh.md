---
title: 存储与文件组织
description: DBMS 如何在磁盘上存储关系：存储层次与 I/O 代价模型；页与缓冲池（固定、脏页、LRU 与时钟扫描置换、扫描环、为何不用 mmap）；定长与变长记录、PostgreSQL 的元组布局与 TOAST；分槽页与记录标识符；堆、顺序、聚簇、散列与分区文件组织及其代价；行存储、列存储、PAX、压缩与 Parquet；系统目录。
source_hash: a8771724d753
---

前面各章把**关系**看作元组的数学集合，把 **SQL** 看作描述所需元组的语言。从本章起，我们打开这个黑盒，问数据库管理系统究竟如何保存这些元组、找到它们并安全地修改它们。第一个问题是物理上的：一张一亿行的表装不进内存，必须经受住断电，而读它的查询要么只碰一行，要么碰全部行。答案是分层的设计。最底层，存储设备上的文件被划分为固定大小的页；缓冲池把当前使用的页保存在内存中；页内的记录以可以增长、缩小和移动而不破坏对它们的引用的方式排布；文件组织则决定哪些记录放进哪个页。同样的思想在操作系统中出现在更低的一层（页式管理与页面置换见 [4.11.4](/4.11.4)，文件系统见 [4.11.7](/4.11.7)，设备见 [4.11.8](/4.11.8)），但 DBMS 对自己的访问模式了解得比操作系统多得多，并且利用了这些知识。索引是快速查找记录的附加结构，是 [4.13.8](/4.13.8) 的主题；这里引入的代价模型是 [4.13.9](/4.13.9) 查询优化的基础，把脏页写回磁盘的规则则由 [4.13.10](/4.13.10) 的日志与恢复补全。

运行示例是 [4.13.3](/4.13.3#sec-3.2.3) 的基因表达**数据库**：其中有表 `gene`、`sample` 和 `measurement(sample_id, gene_id, tpm)` 等。为了测量存储，我们使用同一**模式**的合成版本，含 5,000 个基因和 100 个样本，即 `measurement` 中有 500,000 行。

## 7.1. 存储层次

### 7.1.1. 设备及其代价

**数据库**同时存在于多种存储上。下表给出当前硬件的典型数量级；具体数值每隔几年就变，比值的变化要慢得多。

| 存储 | 随机访问延迟 | 顺序带宽 | 持久 | 在 DBMS 中的角色 |
|---|---|---|---|---|
| CPU 高速缓存 | 1–40 ns | 数百 GB/s | 否 | 算子的执行（[4.10](/4.10)） |
| DRAM | 约 100 ns | 每个插槽数十 GB/s | 否 | 缓冲池、散列表、排序空间 |
| NVMe 闪存 SSD | 20–100 µs | 3–14 GB/s | 是 | 数据文件、日志 |
| 硬盘驱动器 | 5–10 ms | 150–300 MB/s | 是 | 批量与归档数据、备份 |
| 云对象存储（如 Amazon S3） | 首字节 10–100 ms | 聚合带宽高 | 是 | 数据湖、云数据仓库 |

两个事实主导存储引擎的设计。第一，持久存储比内存慢二到五个数量级，所以对未缓存的数据，磁盘与内存之间的页传输次数，而不是 CPU 指令数，通常决定查询的运行时间。第二，顺序访问比**随机访问**便宜得多。在硬盘上，一次随机读要付出数毫秒的**寻道时间**和**旋转延迟**，之后接下来的一兆字节几乎一样快地流入；在闪存 SSD 上差距较小但仍然存在，因为**闪存转换层**和设备内部的并行性偏爱大而对齐的请求（[4.11.8](/4.11.8#sec-8.3)）。因此**数据库系统**更喜欢读写长串连续页的算法，并使用**磁盘阵列**或跨机器的复制来获得容量与可用性。

### 7.1.2. 页与 I/O 代价模型

**定义 7.1.1（页）** **页**（也称**块**）是 DBMS 中持久存储与内存之间数据传输的单位：数据库文件中连续的、固定大小的一块，由诸如（文件号，页号）的**页标识符**标识。存储管理器的所有读写都是对整页的读写。

典型的**页**大小在 PostgreSQL 中是 8 KiB，在 MySQL 的 InnoDB 引擎中是 16 KiB，在 SQLite 中默认为 4 KiB（可在 512 字节到 64 KiB 之间配置）。数据库页通常由一个或几个文件系统块组成，与 [4.11.4](/4.11.4) 的虚拟内存页无关，尽管两者通常都是 4 KiB 或其倍数。

由于传输占主导，后续各章的代价模型以页为单位计数。

**定义 7.1.2（I/O 代价模型）** 算法的 I/O 代价是它在持久存储与内存之间执行的页传输次数。需要区分随机访问与顺序访问时，代价写作 $b \cdot t_T + S \cdot t_S$，其中 $b$ 是传输的页数，$S$ 是随机访问（寻道）的次数，$t_T$ 是传输一页的时间，$t_S$ 是一次随机访问的时间。

对 $t_S = 4\,\mathrm{ms}$、带宽为 $200\,\mathrm{MB/s}$ 的硬盘，传输一个 8 KiB 的页约需 $t_T \approx 0.04\,\mathrm{ms}$，所以一次随机访问的代价相当于顺序读约一百页。这个模型忽略 CPU 代价；对内存中的数据和列存储（§7.5），CPU 代价很重要，实际的优化器会把它作为单独的项加进来（[4.13.9](/4.13.9)）。

**注 7.1.1** 一个页是否应当一直保留在内存中，是一个经济问题。Gray 和 Putzolu 的*五分钟法则*（1987）比较保存一页的内存价格与再次取回它所需的设备带宽价格：被引用得比每个盈亏平衡间隔一次更频繁的页应当留在内存中。1987 年磁盘与 DRAM 的这个间隔约为五分钟；此后每一代硬件都重新评估了该法则（对闪存，分别在 DRAM 与 SSD 之间、SSD 与磁盘之间），盈亏平衡间隔随价格和设备速度而变。

## 7.2. 缓冲池

### 7.2.1. 结构与接口

**DBMS** 并不是每次算子需要时都从磁盘读一个**页**。它把最近使用的页保存在自己管理的一块主存区域中。

**定义 7.2.1（缓冲池）** **缓冲池**是由**缓冲区管理器**管理的、由页大小的内存槽（称为**帧**，frame）组成的数组。对每个帧，缓冲区管理器记录它存放的页、一个**固定计数**（pin count，即该页当前的使用者数；被固定的页不得被换出）、一个**脏标志**（dirty flag，即页自读入后是否被修改过），以及置换策略所需的簿记信息。一个散列表，即**缓冲表**（buffer table），把页标识符映射到帧。

接口很小。算子用 `pin(page_id)` 请求一个页并得到指向帧的指针；用完后调用 `unpin(page_id, dirty)`。在此期间，它可以就地读取和修改该页。

**算法 7.2.1（取页）** 固定页 $p$：

1. 在缓冲表中查找 $p$。若存在，则把它所在帧的固定计数加一并返回该帧（*命中*）。
2. 否则（*缺失*），按**页面置换策略**选择固定计数为 $0$ 的牺牲帧。若不存在这样的帧，则等待或报错。
3. 若牺牲帧是脏的，先把它的页写回磁盘。在采用**预写日志**的系统中，描述该页变更的日志记录必须先于页本身到达稳定存储（[4.13.10](/4.13.10)）。
4. 把 $p$ 读入该帧，更新缓冲表，把固定计数设为 $1$，清除脏标志。

在 PostgreSQL 中，**缓冲池**是共享内存区 `shared_buffers`（默认 128 MB；生产服务器通常给它约四分之一的内存），由所有服务器**进程**共享；在 InnoDB 中它是由 `innodb_buffer_pool_size` 设定大小的*缓冲池*；在 SQLite 中每个连接有自己的**页缓存**。被修改的页通常在修改很久之后才由后台写进程或在检查点写回，使得对同一页的多次修改只需一次写。自 PostgreSQL 18 起，读也可以异步发出（设置 `io_method`：默认为 `worker`，支持的 Linux 构建上为 `io_uring`，或 `sync`），使顺序扫描或 `VACUUM` 能同时保持多个页读取在途，而不必逐个等待。

### 7.2.2. 置换策略

缓冲池满时，**缓冲区管理器**必须决定换出哪个未被固定的页。这又是**虚拟内存**的**页面置换策略**问题（[4.11.4](/4.11.4#sec-4.6.2)），经典答案同样适用：**最近最少使用**（LRU）换出上次使用最久远的页，**时钟算法**用每帧一个引用位和一根旋转的指针廉价地近似 LRU。**数据库**工作负载的两个特点改变了局面。

第一个是*顺序泛洪*（sequential flooding）。扫描一张大表的查询每个页只碰一次，不再碰第二次。在 **LRU** 下，扫描的每个页都作为最近使用的页进入缓冲池，并把其他查询反复使用的页（如索引的根页）挤出去。更糟的是，若一张 $B + 1$ 页的表被反复扫描而缓冲池有 $B$ 个帧，LRU 恰好换出下一个将被需要的页，每次访问都缺失，而换出最近使用页的策略几乎每次访问都命中。

第二个是 DBMS 事先知道访问模式：查询计划说明了哪些页只被扫描一次、哪些索引页是热点、哪些页将被嵌套循环**连接**重读。实际系统以几种方式利用这一点。

| 系统 | 策略 |
|---|---|
| PostgreSQL | *时钟扫描*（clock sweep），每个缓冲区有一个使用计数：每次访问使计数加一（至多到 5），旋转的指针使它减一，并换出计数为 0 的缓冲区。大的顺序扫描、`VACUUM`、`COPY` 和批量写使用*缓冲区访问策略*：一个循环复用的小缓冲区环，使它们不会泛洪共享缓冲池。 |
| MySQL InnoDB | LRU 链表分为*年轻*和*年老*两个子表（默认年老子表占缓冲池的 3/8）。新读入的页进入年老子表的头部，只有在 `innodb_old_blocks_time`（1 秒）之后再次被访问才移入年轻子表；因此扫描的页会从年老子表中老化淘汰。 |
| 研究及其他系统 | LRU-K（按第 $K$ 次最近访问的时间换出）、2Q、ARC；提示某页不会被复用的逐查询提示。 |

下面的模拟在这样的工作负载上比较 LRU、时钟扫描和带私有扫描环的时钟扫描：90% 的点访问落在 50 个热点页上，每 2,000 次点访问之后进行一次 1,000 页的顺序扫描。三种情形缓冲池都有 100 个帧；表中报告的是点访问的命中率。

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

这里最佳可能的命中率约为 0.9，因为对 4,950 个冷页的那 10% 点访问几乎总是缺失。普通 LRU 和普通时钟扫描都在每次扫描时丢失热点页，之后必须重新加载；扫描环则保住了它们，尽管给点查询留下的帧更少。这一效应随扫描长度与缓冲池大小之比以及重新加载热点集的代价而增大。

### 7.2.3. 为什么不交给操作系统？

**操作系统**已经缓存文件页（[4.11.7](/4.11.7#sec-7.2.5)的**页缓存**），用 `mmap` 对数据库文件做**内存映射**可以让内核的虚拟内存系统扮演缓冲池的角色。尽管如此，大多数**数据库系统**仍然自己管理缓冲区，理由来自后续各章的要求：

- *写顺序。* 恢复要求脏页不得先于它的日志记录写出（[4.13.10](/4.13.10)）。用 `mmap` 时内核可能在任何时刻写回被修改的页，DBMS 无法阻止。
- *置换与预取。* 内核不知道某个页属于一次性扫描还是索引的根；DBMS 知道。
- *错误与停顿。* 用 `mmap` 时，I/O 错误以信号形式到达，**缺页**会不可见地使**线程**停顿；用显式读时，DBMS 可以异步调度 I/O，并把错误作为返回值处理。
- *双重缓冲。* 若 DBMS 缓存一个页而内核也缓存同一个页，就浪费内存。InnoDB 用直接 I/O（`O_DIRECT`）避免这一点；PostgreSQL 传统上依赖带缓冲的 I/O 并接受一定的双重缓存，把 `shared_buffers` 设置得远小于内存，让页缓存保存其余部分。

Crotty、Leis 和 Pavlo 在 2022 年的一项研究（“Are You Sure You Want to Use MMAP in Your Database Management System?”）在实践中测量了这些问题。成功使用 `mmap` 的系统，如 LMDB 和 SQLite 可选的**内存映射 I/O** 模式，要么其写路径另外受控（例如通过**写时复制**），要么只把 `mmap` 用于读。

## 7.3. 记录格式

### 7.3.1. 定长记录

*记录*（record）是一个**元组**的存储表示。若每个**属性**的大小固定（整数、浮点数、定长字符串），则**关系**的每条记录长度相同，为 $s$，页中第 $i$ 条记录从字节 $h + i\,s$ 开始，其中 $h$ 是页头的大小。删除会留下空洞。把后面的记录上移既费工又改变它们的地址；只把最后一条记录移进空洞只改变一个地址；通常的办法是保留空洞，并把所有空闲记录位置串成*空闲链表*，其表头存放在页头中，使下一次插入复用其中一个位置。

### 7.3.2. 变长记录

变长字符串、可为空的属性、数组和 JSON 值使记录长度可变。标准布局有三个部分。

1. *头部*：含记录长度、每个属性一位的*空值位图*（**空值**属性不再占用其他空间）以及系统信息（在 PostgreSQL 中是并发控制所需的事务标识符，[4.13.11](/4.13.11)）。
2. 定长部分：定长属性的值，以及每个变长属性的（偏移，长度）对或长度前缀。
3. 变长值本身。

PostgreSQL 中**堆**元组的布局（出自**页**格式的文档）是一个具体的例子。每个元组以 23 字节的头部开始（`t_xmin` 和 `t_xmax`，即插入和删除它的事务的标识符；`t_cid`；`t_ctid`，即该行本版本或更新版本的位置；含属性个数的两个标志字；以及 `t_hoff`，即用户数据的偏移），其后若有属性为空则是空值**位图**，并填充使数据从平台最大对齐的整数倍处开始，当前 64 位机器上为 8 字节。每个值按其类型对齐：`double precision` 或 `bigint` 从 8 的倍数处开始，`integer` 从 4 的倍数处开始，而较短的 `text` 值（少于 127 字节）有 1 字节的长度头，不需要对齐。

**例 7.3.1** `measurement(sample_id text, gene_id text, tpm numeric(10, 2))` 的一行，如 `('S01', 'ENSG00000141510', 35.20)`，占用 24 字节头部（23 向上取整到 8 的倍数）、`sample_id` 的 4 字节（1 字节长度加 3 个字符）、`gene_id` 的 16 字节，以及 `tpm` 的约 7 字节（`numeric` 值是变长的：1 字节长度、2 字节头部，以及 `35` 和 `.20` 各一个以 10,000 为基的 2 字节数字）：共 51 字节，由下一个元组的对齐取整为 56。若改用 `double precision` 列，则占 8 字节、对齐到 8 的倍数，前面有 4 字节填充，结果同样是 56。加上 §7.3.3 的 4 字节槽和 24 字节的页头，一个 8 KiB 的页大约容纳 $\lfloor 8168 / 60 \rfloor = 136$ 行，合成数据集的 500,000 行需要约 3,700 页，即 30 MB。而值本身每行只有 $3 + 15 + 8 = 26$ 字节：这类每行开销正是分析型系统使用 §7.5 列式布局的原因之一。

列的顺序影响填充。声明为 `(a boolean, b bigint, c boolean, d bigint)` 的表，每行数据为 $1 + 7 + 8 + 1 + 7 + 8 = 32$ 字节；声明为 `(b bigint, d bigint, a boolean, c boolean)` 则只需 $8 + 8 + 1 + 1 = 18$ 字节，在元组末尾取整为 24。PostgreSQL 按声明顺序存储列，所以对非常大的表，把定长、强对齐的列放在前面是常见的空间优化。

太大而放不进页的值存放在别处。PostgreSQL 的 TOAST 机制（“The Oversized-Attribute Storage Technique”）先压缩大的变长值，若行仍大于约 2 KB 的阈值，就把它们分块移到单独的 TOAST 表中，在行内留下一个指针；InnoDB 把 `DYNAMIC` 行格式的长列存放在单独的溢出页上，记录中留 20 字节的指针；SQLite 从单元（cell）出发链接溢出页。

### 7.3.3. 分槽页

在页内部，变长记录必须能够增长、缩小和移动（例如页被紧缩时），而不使索引持有的对它们的引用失效。标准结构增加了一层间接。

**定义 7.3.1（分槽页）** **分槽页**由页头、**槽**（slot）数组和记录区组成。页头存放槽的个数和空闲空间的边界；槽 $i$ 存放记录 $i$ 的偏移和长度，或标记该槽未使用。槽数组从页的开头向后增长，记录从页的末尾向前增长，空闲空间位于两者之间。记录由它的**记录标识符**（RID，即（页标识符，槽号）这一对）寻址。

![分槽页。每个槽指向它的记录；槽 3 未使用，因为它的记录已被删除。只要更新槽，记录就可以在页内移动，所以记录标识符保持有效。](./plots/slotted-page.py)

插入时占用一个新槽（或复用一个未使用的槽），并把记录放在空闲空间的末端。删除把槽标记为未使用；记录占用的空间可以通过把记录向页尾紧缩并更新它们的偏移来回收，这使每个 **RID** 仍然有效。若一条记录增长后放不下，它被移到另一个页，其原来的槽保留一个*转发地址*。

在 PostgreSQL 中每个页都是这种形式：24 字节的页头（其中 `pd_lower` 和 `pd_upper` 界定空闲空间，`pd_lsn` 是最近一次变更的日志位置，用于恢复），4 字节的*行指针*（line pointer）作为槽，元组从页尾开始。RID 称为*元组标识符*，可见于系统列 `ctid`：查询 `SELECT ctid, * FROM measurement` 显示 `(0,1)`、`(0,2)` 这样的值，意为第 0 页、行指针 1、2。PostgreSQL 中的更新写出该行的一个新版本，带有新的 `ctid`，并把旧版本链接到它（[4.13.11](/4.13.11)）。SQLite 的 **B 树**页也是**分槽页**：页头之后是由 2 字节偏移组成的*单元指针数组*，单元从页尾开始填满页。

## 7.4. 文件组织

记录如何分配到**页**决定了哪些操作便宜。一个**关系**存储为一个或多个文件（在 PostgreSQL 中是文件 `base/<database oid>/<relfilenode>`，分成 1 GB 的段，另有以单独的分支（fork）存放的空闲空间映射和可见性映射；在 SQLite 中整个**数据库**是单个文件）。

### 7.4.1. 堆文件

**定义 7.4.1（堆文件）** **堆文件**不按任何特定顺序存储关系的记录：新记录放进任何有足够空闲空间的页，文件支持扫描所有记录、按 RID 取记录、插入和删除。

为了不读整个文件就找到有空位放新记录的页，**DBMS** 维护一个空闲空间的目录。PostgreSQL 的*空闲空间映射*用一棵小树记录每个页的大致空闲空间，其*可见性映射*记录哪些页只含对所有事务可见的行；后者使 `VACUUM` 可以跳过这些页，也使仅索引扫描可以避免访问**堆**（[4.13.8](/4.13.8)）。**堆文件**是 PostgreSQL、Oracle 和 SQL Server（对没有聚集索引的表）的默认表组织。

### 7.4.2. 顺序文件

**定义 7.4.2（顺序文件）** **顺序文件**按搜索码（search key）排序存储关系的记录，搜索码是为此选定的一个或多个属性，使记录可以按码的顺序读取，一段码范围占据连续的页。

按码查找可以对页做**二分查找**，范围查询只读范围内的页。代价在于插入：新记录属于一个固定的位置。若它所在的页已满，它进入从那里链出的*溢出页*，多次插入之后文件必须*重组*，即按顺序重写。纯粹的**顺序文件**如今很少见；它们的角色由动态保持顺序的 B+ 树组织接替（[4.13.8](/4.13.8)）。

### 7.4.3. 聚簇组织

码值相同或相邻的记录物理上存放在一起的组织称为*聚簇*的。如今最重要的形式把表本身存放在**主码**上的 **B+ 树**的叶子中。

**定义 7.4.3（索引组织表）** **索引组织表**（或聚簇表）把记录存放在按某个码（通常是主码）排序的 B+ 树的叶页中；没有单独的堆文件。表上的其他索引通过码值而不是 RID 引用记录。

InnoDB 以这种方式存储每张表，聚簇于主码（表没有主码时用隐藏的行标识符），其辅助索引存放主码值。SQLite 把普通表存储为以 64 位 `rowid` 为键的 **B 树**；声明为 `WITHOUT ROWID` 的表则是以主码为键的 B 树。PostgreSQL 只有堆文件；它的 `CLUSTER` 命令按某个索引把表排序一次，但之后的插入不维护该顺序。

这一差别在 SQLite 中可以看到。运行示例的 `measurement` 表在 `(sample_id, gene_id)` 上有复合主码。按通常方式存储时，它是一棵 rowid B 树，加上一个强制主码并重复两个码列的单独索引；以 `WITHOUT ROWID` 存储时，记录按码的顺序保存在一棵树中。对合成数据集（500,000 行，4 KiB 页），虚拟表 `dbstat` 报告每棵 B 树的页数：

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

**聚簇表**需要 4,730 页，而不是 $4{,}550 + 4{,}060 = 8{,}610$ 页，查询某个样本的全部测量只需读几个连续的叶页。作为交换，按随机码序的插入会在树的中部分裂页，每次辅助索引查找还要多一次经主码的树下降。

一个相关的想法是*多表聚簇*：把通常被连接的若干关系的行（比如每个样本及其测量）存放在相同的页中。它加速该**连接**而减慢其他一切，如今主要存在于专门的系统中。

### 7.4.4. 散列文件与分区文件

*散列文件*由码的**散列函数**计算记录所在的页，使等值查找读一个页（加上溢出页）；散列作为索引结构见 [4.13.8](/4.13.8#sec-8.3)。

**定义 7.4.4（分区）** **分区**按*分区键*的值把表划分为互不相交的部分，即分区：按值的范围（*范围分区*）、按值的列表（*列表分区*）或按键的散列（*散列分区*）。每个分区存储为单独的表，系统把每一行路由到它所属的分区。

PostgreSQL 以三种方法支持声明式**分区**：

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

带 `WHERE measured_on >= '2026-03-01'` 的查询只读 2026 年的分区（*分区裁剪*），旧数据可以通过删除一个分区来移除，而不必删除数百万行。把同样的想法用于多台机器，就是分片（[4.13.12](/4.13.12)）。

### 7.4.5. 比较各种组织

下面的比较仿照 Ramakrishnan 和 Gehrke，统计 $B$ 页的关系的页 I/O 次数，假定对码做等值查找（至多一个匹配）、范围查找匹配 $m$ 页，以及页 80% 满的散列文件。

| 操作 | 堆文件 | 排序文件 | 散列文件 |
|---|---|---|---|
| 扫描所有记录 | $B$ | $B$ | $1.25\,B$ |
| 等值查找 | 平均 $0.5\,B$ | $\log_2 B$ | $1$ |
| 范围查找 | $B$ | $\log_2 B + m$ | $1.25\,B$ |
| 插入 | $2$（读并写一个页） | 查找 $+\ B$（移动其余部分） | $2$ |
| 删除（给定码） | 查找 $+\ 1$ | 查找 $+\ B$ | $2$ |

没有哪种组织处处占优；这就是为什么表通常存储为堆或 B+ 树组织的文件，再用索引补充其他访问路径。

## 7.5. 行存储与列存储

### 7.5.1. 三种布局

迄今为止的一切都把每条记录连续存储。这对事务型工作负载（**OLTP**，即**联机事务处理**）是理想的，其查询读写少数几个完整的行：一次**页**访问就取到整行。分析型工作负载（OLAP，联机分析处理）则不同：像“所有测量中各组织的平均 TPM”这样的查询读取数百万行，却只涉及两三列。若行连续存储，它要从磁盘读取并经过 CPU 缓存传送每一行的每个字节，其中几乎全无用处。

**定义 7.5.1（行存储与列存储）** 在 **N 元存储模型**（NSM，*行存储*）中，记录的所有属性值存放在一起，页中容纳完整的记录。在**分解存储模型**（DSM，*列存储*）中，每个属性的值按记录顺序存放在一起，位于单独的一串页中；所有列的第 $i$ 个值合起来构成第 $i$ 条记录。**PAX** 布局（Partition Attributes Across）是一种混合：记录像 NSM 那样分配到页（或更大的*行组*）中，但在每个页或行组内部，值像 DSM 那样按列分组。

列式布局是**数据库**中对应于把表存成**长格式**并按列处理的做法，如 NumPy 和 pandas 所做的那样（[4.4.5](/4.4.5)）：算子读取一个同一类型值的连续数组，这对 CPU 缓存、SIMD 指令和压缩都是理想的。它的代价在于重建行和更新：插入一行要触及每一列。因此**列存储**把插入缓冲在面向行的区域中，再分批合并到各列中。

| | 行存储 | 列存储 |
|---|---|---|
| 典型工作负载 | OLTP：点查询、小更新 | OLAP：对少数几列的扫描与聚集 |
| 对涉及 $n$ 列中 $k$ 列的查询的读取量 | 全部 $n$ 列 | $k$ 列 |
| 压缩 | 中等（一个页中混有多种类型） | 高（单一类型，常有序或重复） |
| 插入或更新一行 | 一个页 | 每列一个页，通常分批 |
| 例子 | PostgreSQL、MySQL InnoDB、SQLite、Oracle | DuckDB、ClickHouse、Snowflake、BigQuery、Amazon Redshift；文件格式 Parquet 和 ORC |

### 7.5.2. 压缩

同一列的值彼此相似，列存储用简单的方案压缩它们，这些方案往往无需解压即可求值：

- *字典编码*：把每个值替换为指向不同值字典的小整数编码。有五个不同字符串的列 `tissue` 每行只需 3 位。
- *游程编码*（RLE）：存储（值，游程长度）对；对有序或聚簇的列有效。谓词可以对每个游程只求值一次。
- *位压缩与参考帧*：把整数存储为相对于基值的差，只用范围所需的位数；*差分编码*存储相邻值之间的差（适合有序的码和时间戳）。
- *浮点方案*，如 ALP（自适应无损浮点压缩，DuckDB 使用），它利用大多数存储的双精度数其实是位数很少的十进制数这一事实。
- 在编码后的页之上再用通用压缩器（Snappy、LZ4、Zstandard）。

### 7.5.3. 列存储的实践

DuckDB（这里是 1.5 版）是嵌入式分析型数据库（[4.13.12](/4.13.12)），把表存储在每组 122,880 行的行组中，每列一个压缩段，并通过尝试可用的方法来选择每个段的压缩方式。加载 500,000 条合成测量并导出为 Parquet 文件格式，可以看到两种布局：

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

行按样本排序，所以在一个行组内，列 `sample_id` 由少数几个长游程组成，它的列块对 100,000 多个值只占 234 字节；`gene_id` 重复同样的 5,000 个标识符，采用字典编码；`tpm` 是小数点后两位的十进制数，被存储为以百分之一计数的整数并做位压缩。Parquet 文件占 2.0 MB，而同样的数据存成 CSV 为 13.2 MB，存成 SQLite 数据库为 35.7 MB（后者每行还带头部，另有主码索引）。Parquet 文件本身就是 **PAX 布局**：行组包含每列一个*列块*，列块由页组成，文件尾记录**模式**以及每个列块的统计信息，如最小值和最大值，使读取者可以跳过不可能满足谓词的行组。

介于两者之间的是*混合事务/分析处理*（HTAP）系统，它们为事务保留一个**行存储**，为分析保留一份列存储副本，并持续同步；例子有 SQL Server 的列存储索引、Oracle 的 In-Memory 选项和 TiDB 的 TiFlash 副本。

## 7.6. 系统目录

**DBMS** 把**数据库**的描述（表、列及其类型、约束、索引、视图、用户与**权限**、统计信息）作为普通关系存放在数据库自身中：这就是 [4.13.1](/4.13.1#sec-1.4) 的系统目录或数据字典。存储管理器需要它来解释页中的字节：目录说明一条记录有多少个属性、它们的类型和顺序，以及哪个文件和哪些页存放哪个关系。

在 SQLite 中，目录是一张表 `sqlite_schema`，存放在数据库文件的第 1 **页**。它的列 `rootpage` 给出每棵 **B 树**起始的页；对合成数据库：

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

每个 `PRIMARY KEY` 和 `UNIQUE` 约束都产生了一个自动索引，`ANALYZE` 创建了 `sqlite_stat1` 来保存优化器的统计信息。用 `dbstat` 测量同一个数据库文件，可以看出空间是如何分布的：

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

表 `measurement` 是按 rowid 顺序追加行填充的，SQLite 几乎完全填满这种树的叶子（未使用 0.6%）；索引 B 树的平衡方式不同，会让页的 12–18% 空闲，这使以后在中间的插入更便宜。`measurement` 的单元数多于行数，是因为 rowid 树的内部页也含有单元（每个子指针一个）。

PostgreSQL 的目录由 `pg_class`（每个表、索引、序列或视图一行，含估计的页数 `relpages` 和行数 `reltuples`）、`pg_attribute`（每列一行）和 `pg_index` 等表组成。**SQL** 标准定义了目录的可移植视图 `information_schema`，PostgreSQL、MySQL 和 DuckDB 实现了它；SQLite 则提供 `PRAGMA table_info(...)` 和诸如 `pragma_table_info('gene')` 的表值函数。

## 小结

- 存储是一个层次结构，其中持久设备比内存慢几个数量级，**随机访问**比顺序访问慢；因此 **I/O 代价模型**统计**页**传输次数，必要时把寻道分开计算。
- 缓冲池把页缓存在带有固定计数和脏标志的帧中。数据库工作负载通过顺序泛洪击败普通 LRU，所以系统使用带使用计数的时钟扫描、扫描环（PostgreSQL）或分裂的 LRU 链表（InnoDB）。DBMS 自己管理缓冲区而不依赖 `mmap`，主要是为了控制恢复所需的写顺序。
- 记录带有含空值位图和系统信息的头部；对齐填充和每行的头部使小行代价很高。大值存放在行外（TOAST、溢出页）。
- 分槽页给每条记录一个稳定的标识符（页，槽），同时允许记录在页内移动。
- 堆文件、顺序文件、索引组织表、散列文件和分区表以不同方式权衡扫描、查找、范围查询和更新的代价。
- 行存储适合事务，列存储适合分析；列存储用字典、游程和位压缩方案压缩得很好，Parquet 是用作交换格式的 PAX 布局。
- 目录在自己的表中描述数据库；SQLite 的 `sqlite_schema`、PostgreSQL 的 `pg_class` 和标准的 `information_schema` 都是例子。
