---
title: 动态内存分配
source_hash: 679fc7b464fc
---

程序会请求在编译时大小或生存期尚不确定的内存：不断增长的向量、根据输入构建的树、长度未知的文件缓冲区。这就是**动态内存分配**（[4.1.8](/4.1.8)）：在 C 中由 `malloc` 和 `free` 完成，在 C++ 中由 `new` 和 `delete` 完成（它们调用同一个分配器），在 Python 等托管语言中则由运行时为每个对象分配。**内核**只以页为单位的大块向进程提供内存，所用的**系统调用**是 `brk` 和 `mmap`（[4.11.4](/4.11.4)）；用户空间的库，即分配器，负责把这些大块切分成任意大小的块并收回。本章讲解其中的做法：分配器必须权衡的目标，它在空闲内存内部维护的数据结构，一个完整的 C 语言小型分配器，以及实际系统中的各种设计，从 glibc 的 `malloc` 到 Linux 内核的伙伴分配器和 slab 分配器。随后从分配器的角度审视 C 语言中常见的内存错误，最后介绍**垃圾回收**：由运行时自己找出不再使用的内存的另一条路线。

## 5.1. 堆与分配器接口

### 5.1.1. 内存从何而来

**定义 5.1.1（动态内存分配器）** **动态内存分配器**把进程虚拟内存中的一块区域，即堆，作为一组大小可变的块来管理，每个块或者已分配（程序正在使用），或者空闲。显式分配器要求程序自己释放块（C 中的 `malloc` 和 `free`，C++ 中的 `new` 和 `delete`）；隐式分配器，即垃圾回收器，则自行检测并释放程序不再能使用的块。

在 Linux 上，传统的堆是紧接在程序数据之后的一段连续区域，其末端称为程序断点（program break），由**系统调用** `brk`（库函数为 `sbrk`）移动，分配器通过抬高它来获得更多内存。对于大块请求以及其他线程的堆，分配器改用匿名 `mmap` 映射，这类映射可以用 `munmap` 单独还给内核。无论哪种方式得到的页，都要等到被访问时才占用物理内存（**请求调页**，[4.11.4](/4.11.4#sec-4.6.1)）。

C 语言的接口如下：

| 函数 | 含义 |
|---|---|
| `void *malloc(size_t n)` | 分配至少 `n` 字节，不初始化；失败时返回 `NULL` |
| `void *calloc(size_t k, size_t n)` | 分配 `k * n` 字节（检查溢出），并清零 |
| `void *realloc(void *p, size_t n)` | 调整块的大小，必要时移动其内容 |
| `void free(void *p)` | 释放由上述函数返回的块；`free(NULL)` 不做任何事 |
| `void *aligned_alloc(size_t a, size_t n)` | 按对齐 `a` 分配（C11） |

返回的块对任何类型都是对齐的：在 x86-64 Linux 上为 16 字节对齐。下面的程序展示 glibc 的分配器如何对请求取整：

```c
#include <malloc.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    void *brk0 = sbrk(0);                              /* current end of the heap */
    size_t sizes[] = {1, 24, 25, 100, 1000, 200000};
    for (int i = 0; i < 6; i++) {
        void *p = malloc(sizes[i]);
        printf("malloc(%6zu) -> %p  usable %6zu  %s\n", sizes[i], p,
               malloc_usable_size(p),
               (char *)p >= (char *)brk0 && (char *)p < (char *)sbrk(0)
                   ? "heap (brk)" : "separate mmap");
    }
    return 0;
}
```

```text
malloc(     1) -> 0x5ddd219b12a0  usable     24  heap (brk)
malloc(    24) -> 0x5ddd219b22d0  usable     24  heap (brk)
malloc(    25) -> 0x5ddd219b22f0  usable     40  heap (brk)
malloc(   100) -> 0x5ddd219b2320  usable    104  heap (brk)
malloc(  1000) -> 0x5ddd219b2390  usable   1000  heap (brk)
malloc(200000) -> 0x73ebef689010  usable 200688  separate mmap
```

最小的块提供 24 字节的可用空间，之后以 16 字节为步长增长：每个块带有 8 字节的管理信息，并占据 16 的整数倍字节（`malloc(1)` 占 32 字节）。第一个块之后相隔的 4 KiB 是第一次 `printf` 为 `stdout` 分配的输出缓冲区。200000 字节的请求超过了 glibc 的 mmap 阈值（初始为 128 KiB，会动态调整），因此获得了独立的映射，大小向上取整为整页。

### 5.1.2. 要求与目标

显式分配器在严格的约束下工作：它必须处理任意的 `malloc` 和 `free` 调用序列，不知道将来的请求，却要立即响应每一个；它不能移动已分配的块，因为程序持有指向这些块的指针；它必须使块对齐；它只能把自己的数据结构保存在堆本身之中。在这些约束之内，它追求两个相互冲突的目标：

- **吞吐率**：每秒处理的请求数。好的分配器只用几十条指令就能处理常见情形。
- 内存利用率：堆中有多大比例存放的是程序所要求的数据。设第 $k$ 次请求之后程序持有的已分配有效载荷总大小为 $P_k$，堆的大小为 $H_k$，则 $n$ 次请求之后的峰值利用率为 $U_n = \max_{i \le n} P_i \,/\, H_n$。

利用率的损失来自碎片，分为两类。

**定义 5.1.2（内部碎片）** **内部碎片**是已分配块内部浪费的内存，即块比其中存放的有效载荷更大：原因可能是块头、对齐、最小块大小，或向上取整到某个大小类。

相对的一类是**外部碎片**（[4.11.4](/4.11.4#sec-4.2.2)），即散落在已分配块之间的空闲内存，其中每一片都不足以满足某个请求。内部碎片容易度量；外部碎片取决于将来的请求，是更难处理的问题。

## 5.2. 空闲链表

### 5.2.1. 隐式空闲链表与边界标记

分配器必须为每个请求找到空闲块，还要能确定传给 `free` 的块的大小（`free` 只收到一个指针）。同时做到这两点的最简单的结构，是在每个块前面存一个块头。

**定义 5.2.1（隐式空闲链表与边界标记）** 在**隐式空闲链表**中，每个块以一个块头字开始，其中存放块的大小和一个表示该块是否已分配的位；通过把每个块的大小加到它的地址上，按地址顺序遍历所有块，因此空闲块是通过所有块的大小被隐式地链接起来的。**边界标记**是块末尾的块头副本，即块脚（footer），它使分配器能在常数时间内找到任一块的前一个块的大小和状态（Knuth，1968）。

由于块大小是 16 的倍数，大小的低四位总是零，已分配位就存放在其中一位里。一个存放 10 字节有效载荷、共 32 字节的块如下所示：

| 偏移 | 0–7 | 8–17 | 18–23 | 24–31 |
|---|---|---|---|---|
| 内容 | 块头：`32 \| 1` | 有效载荷（10 字节） | 填充 | 块脚：`32 \| 1` |

返回给程序的指针指向偏移 8 处；块头位于 `p - 8`。

处理一个请求涉及三项决定。

- 放置：使用哪个空闲块。首次适配（first fit）从头扫描，取第一个足够大的空闲块；下次适配（next fit）从上一次搜索结束的位置开始；最佳适配（best fit）检查所有空闲块，取其中能容纳请求的最小者。首次适配简单，并把大块留在堆的末端，但会在开头附近积累小的"碎片"；最佳适配的利用率往往最好，但除非空闲块按大小组织，否则需要完整搜索（§5.3）。
- 分割：如果选中的空闲块比请求大得多，分配器就把它分割成已分配的部分和空闲的余块；否则整块分配出去，接受内部碎片。
- 合并：释放一个块时，把相邻的空闲块与它合并成一个更大的块。如果不合并，堆里会充满相邻的小空闲块，即假碎片，它们合在一起能满足较大的请求，单独却不能。有了边界标记，前后邻块是已分配还是空闲的四种情形都能在常数时间内完成合并。

### 5.2.2. 一个小型分配器

下面的分配器在用 `mmap` 得到的 1 MiB 区域上，实现了带边界标记的隐式空闲链表、首次适配放置、分割以及立即合并。堆开头的序言块和末尾大小为 0 的结尾块头永远处于已分配状态，因此合并时无需检查堆的边界。

```c
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

/* A small allocator: implicit free list with boundary tags (Knuth),
   first-fit placement, splitting and immediate coalescing.
   Every block has a 8-byte header and an 8-byte footer holding
   size | allocated-bit; sizes are multiples of 16, payloads 16-aligned. */

#define WSIZE 8
#define ALIGN 16
#define ARENA (1 << 20)

static char *heap_lo, *heap_hi;                     /* usable block range */

static size_t get(void *p)              { return *(size_t *)p; }
static void   put(void *p, size_t v)    { *(size_t *)p = v; }
static size_t size_of(void *hdr)        { return get(hdr) & ~(size_t)0xF; }
static int    is_alloc(void *hdr)       { return get(hdr) & 1; }
static char  *hdr_of(void *bp)          { return (char *)bp - WSIZE; }
static char  *next_bp(void *bp)         { return (char *)bp + size_of(hdr_of(bp)); }
static char  *prev_bp(void *bp)         { return (char *)bp - size_of((char *)bp - 2 * WSIZE); }

static void set_block(void *bp, size_t size, int alloc) {
    put(hdr_of(bp), size | alloc);
    put((char *)bp + size - 2 * WSIZE, size | alloc);   /* footer */
}

int mm_init(void) {
    char *base = mmap(NULL, ARENA, PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (base == MAP_FAILED) return -1;
    /* layout: padding | prologue hdr+ftr (allocated, 16) | free block | epilogue hdr */
    put(base + WSIZE, 16 | 1);                      /* prologue header */
    put(base + 2 * WSIZE, 16 | 1);                  /* prologue footer */
    heap_lo = base + 4 * WSIZE;                     /* first payload, 16-aligned */
    size_t free_size = ARENA - 4 * WSIZE - 2 * WSIZE;
    set_block(heap_lo, free_size, 0);
    heap_hi = heap_lo + free_size;
    put(hdr_of(heap_hi), 0 | 1);                    /* epilogue: size 0, allocated */
    return 0;
}

static void *coalesce(void *bp) {
    int prev_alloc = is_alloc((char *)bp - 2 * WSIZE);  /* previous block's footer */
    int next_alloc = is_alloc(hdr_of(next_bp(bp)));
    size_t size = size_of(hdr_of(bp));
    if (!next_alloc) size += size_of(hdr_of(next_bp(bp)));
    if (!prev_alloc) {
        bp = prev_bp(bp);
        size += size_of(hdr_of(bp));
    }
    set_block(bp, size, 0);
    return bp;
}

void *mm_malloc(size_t n) {
    if (n == 0) return NULL;
    size_t asize = (n + 2 * WSIZE + ALIGN - 1) & ~(size_t)(ALIGN - 1);  /* + header, footer */
    for (char *bp = heap_lo; size_of(hdr_of(bp)) > 0; bp = next_bp(bp)) {  /* first fit */
        size_t bsize = size_of(hdr_of(bp));
        if (!is_alloc(hdr_of(bp)) && bsize >= asize) {
            if (bsize - asize >= 2 * ALIGN) {       /* split if the rest is useful */
                set_block(bp, asize, 1);
                set_block(next_bp(bp), bsize - asize, 0);
            } else {
                set_block(bp, bsize, 1);
            }
            return bp;
        }
    }
    return NULL;                                    /* out of memory */
}

void mm_free(void *bp) {
    if (!bp) return;
    set_block(bp, size_of(hdr_of(bp)), 0);
    coalesce(bp);
}

static void dump(const char *title) {
    printf("%-26s", title);
    for (char *bp = heap_lo; size_of(hdr_of(bp)) > 0; bp = next_bp(bp))
        printf(" [%s %zu]", is_alloc(hdr_of(bp)) ? "A" : "f", size_of(hdr_of(bp)));
    printf("\n");
}

int main(void) {
    mm_init();
    dump("initial");
    char *a = mm_malloc(10), *b = mm_malloc(100), *c = mm_malloc(24), *d = mm_malloc(5000);
    dump("malloc 10, 100, 24, 5000");
    printf("payload alignment: %lu %lu %lu %lu\n",
           (uintptr_t)a % 16, (uintptr_t)b % 16, (uintptr_t)c % 16, (uintptr_t)d % 16);
    mm_free(b);
    dump("free b (100)");
    char *e = mm_malloc(40);
    dump("malloc 40 (first fit)");
    mm_free(c);
    dump("free c: merge with prev");
    mm_free(e);
    dump("free e: merge with next");
    mm_free(a);
    dump("free a: merge with next");
    mm_free(d);
    dump("free d: merge both sides");
    return 0;
}
```

每一步之后的堆，已分配块写作 `[A 大小]`，空闲块写作 `[f 大小]`：

```text
initial                    [f 1048528]
malloc 10, 100, 24, 5000   [A 32] [A 128] [A 48] [A 5024] [f 1043296]
payload alignment: 0 0 0 0
free b (100)               [A 32] [f 128] [A 48] [A 5024] [f 1043296]
malloc 40 (first fit)      [A 32] [A 64] [f 64] [A 48] [A 5024] [f 1043296]
free c: merge with prev    [A 32] [A 64] [f 112] [A 5024] [f 1043296]
free e: merge with next    [A 32] [f 176] [A 5024] [f 1043296]
free a: merge with next    [f 208] [A 5024] [f 1043296]
free d: merge both sides   [f 1048528]
```

每个请求先加上块头和块脚的 16 字节，再向上取整为 16 的倍数：10 字节需要 32 字节的块，100 字节需要 128 字节的块。40 字节的请求（64 字节的块）被放在 `b` 留下的 128 字节空洞中，该空洞随之被分割。释放操作依次演示了各种合并情形，直到堆重新成为一个完整的空闲块。这个分配器是正确的，但很慢：`mm_malloc` 扫描所有块，无论已分配还是空闲，因此一次请求的时间与块的数目成线性关系。实用的分配器的差别主要在于怎样快速找到空闲块。

### 5.2.3. 显式空闲链表

显式空闲链表（explicit free list）只链接空闲块，链表指针存放在每个空闲块的有效载荷区（程序并未使用这部分）。这样分配的时间只与空闲块的数目成线性关系。释放的块可以插在链表前端（后进先出：常数时间，对很快会被重用的块有良好的**局部性**），也可以按地址顺序插入（释放时需要搜索，但按地址顺序的首次适配利用率更好，接近最佳适配）。指针带来了最小块大小的限制：在 64 位机器上，块头、两个指针和块脚共 32 字节。

## 5.3. 分离适配、伙伴系统与 slab

### 5.3.1. 分离空闲链表

**定义 5.3.1（分离空闲链表）** 使用**分离空闲链表**的分配器把块大小划分为若干大小类（例如 16、32、48、…、512，之后是 2 的幂），并为每个类维护一个单独的空闲链表。请求由其所属类的链表来满足；该链表为空时，从更大的类中取块，分割之后把余块放入它自己所属类的链表。

采用分离适配时，搜索只检查大小大致合适的块，以首次适配的速度近似了最佳适配。大多数实用的分配器都使用某种形式的分离适配。对于大小相同的小对象，常用简单分离存储：把一页切成同一类的等大块，空闲块串在单向**链表**上，分配和释放就是一次出栈和一次入栈，无需块头、分割或合并；代价是内部碎片，以及在一页中的所有块都空闲之前，该页不能用于其他大小。

### 5.3.2. 伙伴系统

**定义 5.3.2（伙伴系统）** 在二进制**伙伴系统**中，内存是一块 $2^m$ 字节的区域，每个块的大小都是 2 的幂。对 $n$ 字节的请求先向上取整为满足 $2^k \ge n$ 的最小 2 的幂。如果不存在大小为 $2^k$ 的空闲块，就把更大的空闲块反复分成两半，即两个伙伴，直到得到大小为 $2^k$ 的块。释放一个块时，如果它的伙伴也空闲，就把两者合并为大小加倍的块，并反复这样做。

偏移为 $a$、大小为 $2^k$ 的块，其伙伴位于偏移 $a \oplus 2^k$（**异或**）处：伙伴的地址恰好有一位不同，因此找到合并所需的伙伴毫无代价。

**例 5.3.1** 一块 1 MiB 的区域是空的。对 100 KiB 的请求被取整为 128 KiB。区域被分成两个 512 KiB 的伙伴，其中第一个再分成两个 256 KiB 的伙伴，再把其中第一个分成两个 128 KiB 的伙伴；请求得到偏移 0 处的块，内部碎片浪费 28 KiB。空闲块还剩下偏移 128 KiB 处的块（128 KiB）、偏移 256 KiB 处的块（256 KiB）和偏移 512 KiB 处的块（512 KiB）。随后对 200 KiB 的请求取走偏移 256 KiB 处的 256 KiB 块。释放第一个块时，它的伙伴在偏移 $0 \oplus 128\,\mathrm{KiB} = 128\,\mathrm{KiB}$ 处，是空闲的，所以两者合并为偏移 0 处的 256 KiB 块；该块的伙伴位于偏移 256 KiB，已被分配，合并到此为止。

伙伴系统合并迅速，但取整为 2 的幂最多会浪费每个块的一半。Linux 内核用它管理物理**页框**：对阶数 $k$（从 0 到 10），分配 $2^k$ 个连续页组成的块（4 KiB 到 4 MiB）。`/proc/buddyinfo` 显示每一阶的空闲块数目：

```text
Node 0, zone    DMA32   2818   1894   1608   1265    824    462    302    174    136    145    710
Node 0, zone   Normal    151     97     56     75     60     27      6      3      1      1    166
```

最后一列是 4 MiB 空闲块的数目。低阶块很多而高阶块短缺，就是物理内存的**外部碎片**；内核用紧缩来对付它：迁移可移动的页（内核掌管**页表**，因此做得到），以形成连续的空闲区间，例如供**大页**使用。

### 5.3.3. slab 分配

内核要分配许多固定的几种类型的小对象：进程描述符、索引节点、网络缓冲区。slab 分配器（slab allocator）由 Bonwick 于 1994 年为 Solaris 提出，为每种对象类型维护一个缓存，缓存由若干 slab（来自伙伴分配器的一页或多页）组成，每个 slab 被切成该类型的对象：这就是带有每 CPU 空闲链表的简单分离存储，使本地 CPU 上常见的分配和释放无需加锁。Linux 的实现是 SLUB（替代方案 SLOB 和 SLAB 已于 2023 年和 2024 年移除）；其缓存见于 `/sys/kernel/slab`，`kmalloc` 用大小为 8、16、32、…、8192 字节的缓存来满足内核的通用请求。

### 5.3.4. 用户空间的分配器

glibc 的 `malloc`（ptmalloc2，源自 Doug Lea 的分配器）综合了上述思想：

- 每个线程有一个 tcache（自 glibc 2.26，2017 年起）：每线程的小型链表，对应不超过约 1 KiB 的 64 个大小类，每类 7 个块，无需加锁即可使用；
- 其后是 arena：各有自己的锁的堆，主 arena 用 `brk` 增长，其余的为额外的线程用 `mmap` 创建（每个核最多 8 个），每个 arena 内有分离的空闲块箱（小尺寸、不合并的 fast bin，精确大小的 small bin，按大小排序的 large bin，以及存放最近释放的块的 unsorted bin）；
- 超过 mmap 阈值的请求直接交给 `mmap`。

其他广泛使用的分配器有 jemalloc（FreeBSD、Firefox 及许多服务器）、tcmalloc（Google）和 mimalloc（Microsoft；CPython 的自由线程构建也使用它，[4.4.7](/4.4.7)）；它们强调每线程缓存、按大小类划分的页以及把内存归还给系统，并且无需重新编译即可替换 glibc 的分配器（`LD_PRELOAD=libjemalloc.so ./program`）。大量分配内存的多线程程序，例如许多生物信息学工具，使用它们可能明显更快，或占用更少内存。在 C 分配器之上，各语言运行时还加上了自己的层次：CPython 为不超过 512 字节的对象提供小对象分配器（`pymalloc`），NumPy 则直接用 `malloc` 或 `mmap` 分配数组数据。

## 5.4. 从分配器角度看内存错误

[4.1.8](/4.1.8) 中的错误（越界访问、**悬垂指针**、重复释放、**内存泄漏**），在了解分配器把数据存放在哪里之后，看起来就不同了。越过块末尾的写操作会覆盖下一个块的块头，或者在空闲块中覆盖链表指针；破坏要到后来才表现出来，出现在某次无关的 `malloc` 或 `free` 中。把一个块释放两次，会使它两次插入空闲链表，于是之后的两次 `malloc` 返回同一块内存。读取已释放的块，可能读到分配器写入的链表指针。这些错误在 C 和 C++ 中是**未定义行为**，也是大多数内存安全漏洞的根源：控制了被覆盖字节的攻击者，可以让分配器把选定的值写到选定的地址。

glibc 会检查自己的一些不变式，一旦被违反就中止程序，但它无法检测一切：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    char *name = malloc(8);
    strcpy(name, "sample_");                 /* 8 bytes including the terminator */
    if (argc > 1) name[8] = 'X';             /* heap buffer overflow by one byte */
    free(name);
    if (argc > 2) free(name);                /* double free */
    return 0;
}
```

用两个参数运行，使两个错误都发生：

```text
free(): double free detected in tcache 2
bash: line 1: 30732 Aborted                 (core dumped) ./uaf 1 2
exit status 134
```

重复释放被捕获了（程序被 `SIGABRT` 终止，状态为 $128 + 6$），但一个字节的溢出却未被发现，因为该块的可用大小是 24 字节，溢出没有碰到下一个块头。用 AddressSanitizer 编译（`gcc -g -fsanitize=address`）后，同一程序在溢出发生处就停止了（输出有删节，文件名已缩短）：

```text
==30740==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x502000000018 at pc 0x5cd7bd0592a7 bp 0x7ffd63faf8e0 sp 0x7ffd63faf8d0
WRITE of size 1 at 0x502000000018 thread T0
    #0 0x5cd7bd0592a6 in main uaf.c:8
0x502000000018 is located 0 bytes after 8-byte region [0x502000000010,0x502000000018)
allocated by thread T0 here:
    #0 0x7a13006fd9c7 in malloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:69
    #1 0x5cd7bd059245 in main uaf.c:6
SUMMARY: AddressSanitizer: heap-buffer-overflow uaf.c:8 in main
```

AddressSanitizer 取代了分配器：它在每个块周围放置红区（redzone），把已释放的块放进隔离区而不是立即重用，并在影子内存（shadow memory，**地址空间**中每 8 字节对应一个字节）中记录哪些字节可以访问；编译器在每次内存访问之前插入对影子字节的检查。程序大约变慢到原来的两倍，这对测试是可以接受的。Valgrind 的 Memcheck 无需重新编译就能发现同样的错误，方法是让程序在模拟的处理器上运行，慢 10 到 50 倍。其他有用的工具有：检查算术中的未定义行为的 `-fsanitize=undefined`，用于额外堆检查的 glibc 的 malloc 调试库（`LD_PRELOAD=libc_malloc_debug.so MALLOC_CHECK_=3 ./program`），以及用于查明程序的内存花在哪里的 `heaptrack` 或 Valgrind 的 Massif。

## 5.5. 垃圾回收

### 5.5.1. 可达性

**垃圾回收**（[4.1.8](/4.1.8)）使程序员不必再调用 `free`。回收器无法知道程序以后还会使用哪些块，但可以确定哪些块有可能被使用：那些通过指针可达的块。

**定义 5.5.1（可达性）** 把内存看作一个有向图，其结点是堆块和根（持有指针的寄存器、栈槽和全局变量），若 $u$ 中含有指向 $v$ 的指针，则有一条从 $u$ 到 $v$ 的边。如果存在从某个根到一个块的路径，则称该块**可达**；不可达的块是垃圾，可以回收。

**引用计数**（[4.2.12](/4.2.12)）局部地近似可达性：计数降为零的对象肯定不可达。它释放内存及时且是渐进的，但互相引用的一圈对象在变得不可达之后仍保持正的计数，而且每次指针赋值都要付出更新计数的代价（多线程程序中还是原子更新）。追踪式回收器则直接计算可达性。

### 5.5.2. 追踪式回收器

**定义 5.5.2（标记-清除）** **标记-清除**回收器（McCarthy，1960，用于 Lisp）分两个阶段工作：标记阶段从根出发遍历图，在每个可达块上设置标记位；清除阶段扫描整个堆，释放每个未标记的块（并清除其余块的标记）。

标记-清除能处理环，但运行时程序要停下来（除非做成增量式或并发的），清除阶段要访问整个堆，并且留下的空闲空间是碎片化的。大多数现代回收器基于两项改进：

- 复制式回收（copying collector）把堆分成两半，把可达对象从正在使用的一半紧凑地复制到另一半，同时更新指针；旧的一半随即整体空闲。分配变成一次指针递增，碎片也消失了，代价是用掉一半的内存，以及要移动对象（这要求回收器确切知道哪些字是指针）。
- 分代回收（generational collector）利用的观察是：大多数对象很快就会死亡。它在小的年轻代中分配对象，年轻代经常而廉价地回收（通常用复制），把经过若干次回收仍存活的对象提升到老年代，老年代很少回收。从老对象指向年轻对象的指针由写屏障（write barrier）来记录，这是每次指针存储时都要执行的一段代码。

C 和 C++ 的编译器不记录哪些字是指针，但保守式回收器，例如 Boehm–Demers–Weiser 回收器，仍然可以追踪这类程序：它把每个看起来像堆内地址的字都当作指针。它从不释放可达的内存，但可能保留一些垃圾，并且不能移动对象。

实际中：CPython 使用引用计数加上分代的环回收器（`gc` 模块）；Java 的 HotSpot 虚拟机提供多种分代和并发的回收器（默认为 G1，ZGC 对 TB 级的堆停顿也在一毫秒以下）；Go 使用并发的标记-清除回收器；JavaScript 引擎使用分代复制式回收器；R 使用分代的标记-清除回收器。Rust 和现代 C++ 走第三条路，没有回收器：所有权是类型系统的一部分（`unique_ptr`、`shared_ptr`；Rust 的借用检查器），内存在其所有者离开作用域时确定地被释放（[4.2.12](/4.2.12)）。

## 小结

- 分配器把从内核获得的内存（主堆用 `brk`，大块和其他 arena 用 `mmap`）划分成块；它必须立即回答每个请求，不能移动块，并把自己的数据保存在堆本身之中。它的目标是吞吐率和利用率，而内部碎片和外部碎片会降低利用率。
- 隐式空闲链表在块头中存放大小和已分配位；边界标记（块脚）使与前后两个邻块的合并只需常数时间。按首次、下次或最佳适配放置，分割大的空闲块，以及释放时合并，是基本操作；§5.2.2 的小型分配器用大约 100 行实现了它们。
- 显式空闲链表只链接空闲块；分离链表为每个大小类保留一个链表，快速近似最佳适配；伙伴系统取整为 2 的幂，并用异或找到伙伴（Linux 的页分配器）；slab 分配器维护等大对象的缓存（Linux 中是 SLUB）。
- glibc 综合了每线程的 tcache、带分离箱的 arena，以及对大块请求直接使用 `mmap`；jemalloc、tcmalloc 和 mimalloc 是可以直接替换的备选。
- 堆溢出、重复释放和释放后使用会破坏分配器自己的数据，并且可被利用；glibc 能捕获其中一些，AddressSanitizer 和 Valgrind 则能可靠地发现它们。
- 垃圾回收器释放不可达的块：引用计数是局部的（会漏掉环），标记-清除从根出发追踪，复制式和分代回收器效率更高；保守式回收器甚至适用于 C。
