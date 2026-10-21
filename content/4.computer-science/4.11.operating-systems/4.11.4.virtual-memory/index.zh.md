---
title: 地址空间与虚拟内存
description: 进程的地址空间及其在 x86-64 Linux 上的布局；基址与界限、分段的地址转换；分页、页表与页表项及算例；快表及其命中率；多级页表（x86-64 四级分页）；请求调页、缺页、交换与页面置换（OPT、FIFO、LRU、时钟、Belady 异常、抖动、工作集）及模拟轨迹；Linux 的内存回收与 OOM 杀手；内存映射文件、写时复制与共享库。
source_hash: c3ca4ec2f288
---

[4.11.2](/4.11.2) 中的每个**进程**都相信自己拥有一大块私有的内存，并且这块内存与其他所有进程的内存起始于相同的地址。而在物理上，所有进程共享同一块内存，它比各进程的内存之和小得多，**内核**本身也驻留在其中。虚拟内存是维持这种假象的硬件与内核软件的总和：程序使用的每个地址都是虚拟的，在每次访问时由处理器的内存管理单元按照内核建立的表翻译成物理地址。地址转换同时带来三样东西：隔离（进程甚至无法指称另一个进程的内存）、方便（每个程序都按同样的地址链接，内存看上去是连续的，尽管实际上是分散的），以及通过把一部分内存放在磁盘上，使用比实际物理内存更多内存的能力。本章一步步建立这套机制，从最简单的基址寄存器重定位，到带有多级页表和转换缓存的分页；然后转到内存满时保留哪些页这一策略问题；最后讨论内存映射文件和共享库。C 或 C++ 程序的内存区域（代码、静态数据、堆、栈；[4.1.8](/4.1.8)）是地址空间的组成部分；管理其中堆的分配器是 [4.11.5](/4.11.5) 的内容。硬件中的缓存层次在 [4.10](/4.10) 中讨论；这里的置换策略是同样的思想在低一级上的应用，只是以页代替缓存行，以磁盘代替内存。

## 4.1. 地址空间

### 4.1.1. 抽象

早期的机器一次运行一个程序，它使用除操作系统占用部分之外的全部内存。**多道程序设计**和**分时**（[4.11.1](/4.11.1#sec-1.2)）使多个程序同时驻留内存，随之而来的是保护问题（一个程序不能写入另一个程序）和重定位问题（程序事先无法知道自己会被装入物理内存的什么位置）。

**定义 4.1.1（地址空间）** 进程的**地址空间**是进程可以使用的地址范围，连同进程所见的这些地址上的内容。程序产生的地址是**虚拟地址**；内存硬件中实际单元的地址是**物理地址**。**虚拟内存**是给每个进程配备其自己的地址空间的技术，其中虚拟地址由硬件和内核映射到物理地址（或磁盘上的数据）。

虚拟内存系统的目标是透明性（程序注意不到转换）、效率（转换耗时少，表占的空间小）和保护（进程只能按内核授予的权限访问自己的内存）。

### 4.1.2. x86-64 Linux 上的布局

下面这个小程序打印一个函数、一个**全局变量**、一个堆块和一个**局部变量**的地址，然后打印它自己来自 `/proc/self/maps` 的内存映射：

```c
#include <stdio.h>
#include <stdlib.h>

int global_init = 42;          /* .data */
int global_zero;               /* .bss */

int main(void) {
    int local = 0;             /* stack */
    int *heap = malloc(16);    /* heap */
    printf("code %p (main)\n", (void *)main);
    printf("data %p (global_init)\n", (void *)&global_init);
    printf("bss %p (global_zero)\n", (void *)&global_zero);
    printf("heap %p (malloc)\n", (void *)heap);
    printf("libc %p (printf)\n", (void *)printf);
    printf("stack %p (local)\n", (void *)&local);
    fflush(stdout);
    FILE *f = fopen("/proc/self/maps", "r");
    char line[512];
    while (fgets(line, sizeof line, f)) fputs(line, stdout);
    fclose(f);
    free(heap);
    return 0;
}
```

输出（文件的长目录名已缩短，列的填充空格已去掉）：

```text
code 0x653efa473160 (main)
data 0x653efa476010 (global_init)
bss 0x653efa476024 (global_zero)
heap 0x653f133372a0 (malloc)
libc 0x7bf081e60100 (printf)
stack 0x7ffdbc9f9e9c (local)
653efa472000-653efa473000 r--p 00000000 08:30 1178010 /home/user/maps
653efa473000-653efa474000 r-xp 00001000 08:30 1178010 /home/user/maps
653efa474000-653efa475000 r--p 00002000 08:30 1178010 /home/user/maps
653efa475000-653efa476000 r--p 00002000 08:30 1178010 /home/user/maps
653efa476000-653efa477000 rw-p 00003000 08:30 1178010 /home/user/maps
653f13337000-653f13358000 rw-p 00000000 00:00 0 [heap]
7bf081e00000-7bf081e28000 r--p 00000000 08:30 55518 libc.so.6
7bf081e28000-7bf081fb1000 r-xp 00028000 08:30 55518 libc.so.6
7bf081fb1000-7bf082000000 r--p 001b1000 08:30 55518 libc.so.6
7bf082000000-7bf082004000 r--p 001ff000 08:30 55518 libc.so.6
7bf082004000-7bf082006000 rw-p 00203000 08:30 55518 libc.so.6
7bf082006000-7bf082013000 rw-p 00000000 00:00 0
7bf0820b6000-7bf0820b9000 rw-p 00000000 00:00 0
7bf0820c2000-7bf0820c4000 rw-p 00000000 00:00 0
7bf0820c4000-7bf0820c5000 r--p 00000000 08:30 55515 ld-linux-x86-64.so.2
7bf0820c5000-7bf0820f0000 r-xp 00001000 08:30 55515 ld-linux-x86-64.so.2
7bf0820f0000-7bf0820fa000 r--p 0002c000 08:30 55515 ld-linux-x86-64.so.2
7bf0820fa000-7bf0820fc000 r--p 00036000 08:30 55515 ld-linux-x86-64.so.2
7bf0820fc000-7bf0820fe000 rw-p 00038000 08:30 55515 ld-linux-x86-64.so.2
7ffdbc9db000-7ffdbc9fd000 rw-p 00000000 00:00 0 [stack]
7ffdbcb72000-7ffdbcb76000 r--p 00000000 00:00 0 [vvar]
7ffdbcb76000-7ffdbcb78000 r-xp 00000000 00:00 0 [vdso]
```

每一行是一个映射（Linux 称之为虚拟内存区域）：一段虚拟地址范围、权限（`r`ead 读、`w`rite 写、e`x`ecute 执行；`p`rivate 私有或 `s`hared 共享）、它映射的文件内的偏移、文件所在的设备和索引节点，以及名称。从低地址到高地址：

| 区域 | 权限 | 内容 |
|---|---|---|
| 程序文件 | `r--`、`r-x`、`r--`、`rw-` | ELF 头和只读数据、代码（`.text`）、常量、已初始化和零初始化的全局变量（`.data`、`.bss`） |
| `[heap]` | `rw-` | 由 `malloc` 管理的内存，用 `brk` 系统调用增长（[4.11.5](/4.11.5)） |
| 内存映射区 | 各不相同 | 共享库（这里是 C 库和动态链接器）、用于大块分配和线程栈的匿名映射、被映射的文件 |
| `[stack]` | `rw-` | 主线程的栈，从用户空间上半部分的顶部附近向下增长 |
| `[vvar]`、`[vdso]` | `r--`、`r-x` | 内核的数据页，以及无需模式切换的系统调用的代码（[4.11.1](/4.11.1#sec-1.4.3)） |

用户空间只使用 47 位地址，最高到 `0x7fffffffffff`（128 TiB）；64 位范围的上半部分属于内核，它被映射到每个进程中，但只能在**内核态**访问。代码不可写，栈和堆不可执行：把**机器语言**代码写到栈上的**缓冲区溢出**不再能直接执行它。再次运行程序会打印出不同的地址：地址空间布局随机化（address space layout randomization），简称 ASLR，每次运行都把程序、库、堆和栈放在随机的偏移处，使攻击者无法预测代码和数据在哪里。

## 4.2. 地址转换

### 4.2.1. 基址与界限

**定义 4.2.1（地址转换与 MMU）** **地址转换**是把运行中的程序发出的每个虚拟地址转换为物理地址，由硬件在每次取指、加载和存储时执行。执行转换的硬件单元是**内存管理单元**（MMU）。

最简单的转换，在 1960 年代使用，是用两个寄存器做动态重定位（dynamic relocation）：基址寄存器保存地址空间在物理内存中的起始地址，界限（限长）寄存器保存其大小。对每次访问，MMU 检查 $0 \le \mathit{va} < \mathit{bounds}$（否则引发**异常**，内核通常杀死该进程），并计算 $\mathit{pa} = \mathit{base} + \mathit{va}$。只有内核可以修改这两个寄存器，并在每次**上下文切换**时重新装入它们。例如，基址为 32 KiB、界限为 16 KiB 时，虚拟地址 3000 映射到物理地址 $32768 + 3000 = 35768$，虚拟地址 17000 则引发故障。

基址与界限能保护和重定位，但浪费内存：整个地址空间，包括堆与栈之间未使用的空隙，都必须占据连续的物理内存。

### 4.2.2. 分段

**定义 4.2.2（分段）** 在**分段**中，地址空间由几个大小可变的段（通常是代码、堆和栈）组成，每个段有自己的基址、界限和保护位。虚拟地址指明一个段（例如通过它的高位）和段内的偏移；MMU 对照段的界限检查偏移，并加上段的基址。

段可以独立地放置，只有地址空间中使用的部分才占据内存，库代码等段还可以在进程之间共享。但是各段的大小不同，随着它们被分配和释放，物理内存变成已用段与空闲空洞拼成的补丁。

**定义 4.2.3（外部碎片）** **外部碎片**是已分配块之间零散的空闲块造成的内存浪费，其中每块都太小而无法满足请求，尽管它们的总和足够。

三个 10 KiB 的空洞共有 30 KiB 空闲时，对 20 KiB 段的请求会失败。紧缩（移动段以合并空洞）代价高昂。同样的问题在堆分配器中再次出现（[4.11.5](/4.11.5)）。在 x86-64 上，分段只以残留的形式存在：段寄存器 `fs` 和 `gs` 的基址指向每线程和每 CPU 的数据。

## 4.3. 分页

### 4.3.1. 页与页表

分页把内存分成固定大小的块，从而避免了外部碎片。

**定义 4.3.1（页、页框与页表）** 在**分页**中，虚拟地址空间被划分为称为**页**的固定大小的块，物理内存被划分为同样大小的称为**页框**的块。虚拟地址由虚拟页号（VPN）和页内的偏移组成。进程的**页表**把每个虚拟页号映射到存放该页的物理页框号（PFN）；物理地址是页框号后面接上不变的偏移。

页的大小为 $2^p$ 字节时，偏移是地址的低 $p$ 位，虚拟页号是其余的高位：

$$
\mathit{pa} = \mathrm{PFN}(\mathrm{VPN}) \cdot 2^{p} + \mathit{offset}, \qquad \mathrm{VPN} = \lfloor \mathit{va} / 2^{p} \rfloor, \qquad \mathit{offset} = \mathit{va} \bmod 2^{p} .
$$

x86-64 和大多数 ARM 系统的标准页大小是 4 KiB（$p = 12$）；Apple 的 ARM 处理器使用 16 KiB。

**定义 4.3.2（页表项）** **页表项**（PTE）保存页的页框号和状态位，最重要的有：存在位（有效位）——页在内存中；可写位和用户位——访问权限（用户态访问没有用户位的页会引发故障）；不可执行位——不得从该页取指令；访问位（引用位）——每次访问时由硬件置位；脏位——每次写入时由硬件置位。

**例 4.3.1** 32 位地址空间、4 KiB 的页：20 位页号，12 位偏移。虚拟地址 `0x00403A7C` 的 VPN 是 `0x00403`，偏移是 `0xA7C`。若页表的第 `0x403` 项保存页框号 `0x001F2` 且存在位已置位，则物理地址为 `0x001F2A7C`。对该地址的存储只有在表项还有可写位时才成功；此后硬件已置位它的访问位和脏位。访问表项不存在的页会引发缺页（4.6 节）。

### 4.3.2. 两个问题：空间与时间

刚才描述的分页有两项代价。

- 空间：线性页表为每个虚拟页保存一项，不论是否使用。对上面的 32 位例子，$2^{20}$ 项、每项 4 字节，共 4 MiB，每个进程一份。对 48 位地址空间、每项 8 字节，则是每个进程 $2^{36} \cdot 8\,\mathrm{B} = 512\,\mathrm{GiB}$：不可能。4.5 节用多级页表解决这个问题。
- 时间：页表在内存中，所以程序的每次内存访问都需要多一次访问来读 PTE，使内存访问的开销加倍（对多级页表则是五倍）。4.4 节用转换的缓存解决这个问题。

## 4.4. 快表

### 4.4.1. 缓存转换

**定义 4.4.1（TLB）** **快表**（translation lookaside buffer，TLB）是 MMU 内部一个小而快的缓存，缓存从虚拟页号到页表项的最近的转换。每次内存访问时，硬件在 TLB 中查找 VPN；*TLB 命中*时，页框号和权限来自 TLB；*TLB 未命中*时，查询页表（在 x86-64、ARM 和 RISC-V 上由硬件页表遍历器完成，在 MIPS 等较老的 RISC 体系结构上由内核陷阱处理程序完成），并在重试访问之前把该转换插入 TLB。

现代的核有一个小的一级 TLB（数据 TLB 约 64 项）和一个较大的二级 TLB（一千到几千项）；命中除了正常的缓存访问外没有额外开销。TLB 之所以有效，是因为内存访问的**局部性**（[4.3.8](/4.3.8)）：连续的访问通常落在同一页内（空间局部性），同样的页很快会再次使用（时间局部性）。

**例 4.4.1** 在页大小为 16 字节的玩具系统中（OSTEP，第 19 章），一个由十个 4 字节整数组成的数组始于虚拟地址 100。元素占据地址 100 到 139，即第 6 页（地址 96–111：`a[0]` 到 `a[2]`）、第 7 页（112–127：`a[3]` 到 `a[6]`）和第 8 页（128–143：`a[7]` 到 `a[9]`）。TLB 起初为空时对数组求和，在 `a[0]`、`a[3]` 和 `a[7]` 处未命中，其余七次访问命中：命中率 70 %。页大小为 4 KiB 时，对 `int` 数组的一次顺序扫描每 1024 个元素未命中一次。

设 TLB 命中率为 $h$，内存访问时间为 $m$，一次页表遍历需要 $k$ 次内存访问，则一次内存访问的有效开销约为 $h\,m + (1 - h)(k + 1)\,m$。取 $m = 100\,\mathrm{ns}$、$k = 4$（4.5 节）、$h = 0.99$，开销为 $99 + 5 = 104\,\mathrm{ns}$；$h = 0.9$ 时为 $90 + 50 = 140\,\mathrm{ns}$。（实际上页表项本身也缓存在数据缓存中，所以一次遍历通常比 $k$ 次完整的内存访问便宜。）

TLB 的覆盖范围，即它的项数乘以页大小，限制了程序在没有 TLB 未命中的情况下能访问多少内存。下面的程序从 $n$ 个页的每一页读取一个整数，重复多次，并打印每次访问的平均时间：

```c
#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Read one int on each of n pages, many times; report the time per access.
   The offset within the page varies so that the accesses spread over
   different cache sets: the growth in time then comes from the TLB. */
int main(void) {
    cpu_set_t set;
    CPU_ZERO(&set);
    CPU_SET(2, &set);
    sched_setaffinity(0, sizeof set, &set);
    const long PAGE = 4096, MAXPAGES = 1L << 14;
    int *a = aligned_alloc(PAGE, MAXPAGES * PAGE);
    long *idx = malloc(MAXPAGES * sizeof(long));
    for (long i = 0; i < MAXPAGES * PAGE / (long)sizeof(int); i++) a[i] = 1;
    for (long p = 0; p < MAXPAGES; p++)
        idx[p] = p * (PAGE / sizeof(int)) + (p % 64) * 16;  /* page p, line p mod 64 */
    printf("pages   ns/access\n");
    long sum = 0;
    for (long n = 8; n <= MAXPAGES; n *= 2) {
        long rounds = (1L << 26) / n;
        struct timespec t0, t1;
        clock_gettime(CLOCK_MONOTONIC, &t0);
        for (long r = 0; r < rounds; r++)
            for (long p = 0; p < n; p++) sum += a[idx[p]];
        clock_gettime(CLOCK_MONOTONIC, &t1);
        double ns = ((t1.tv_sec - t0.tv_sec) * 1e9 + (t1.tv_nsec - t0.tv_nsec))
                    / (double)(rounds * n);
        printf("%6ld  %6.2f\n", n, ns);
    }
    return sum == 42;
}
```

```text
pages   ns/access
     8    0.36
    16    0.31
    32    0.40
    64    0.44
   128    0.39
   256    0.44
   512    0.46
  1024    0.74
  2048    1.17
  4096    4.78
  8192    5.95
 16384    6.43
```

各次访问相互独立，所以乱序处理器把小的一级 TLB 的未命中与其他工作重叠起来，直到 512 页（2 MiB）为止，开销都低于半纳秒。在 1024 到 4096 页之间，二级 TLB 不再能容纳所有转换，每次访问都需要一次页表遍历，开销上升十倍以上。（所访问的缓存行最多为 16384 × 64 B = 1 MiB，可以放进处理器的二级缓存，所以增长来自 TLB 而不是数据缓存。）反复扫描大数组的程序受益于大页（huge page）：在 x86-64 上，页目录项可以直接映射 2 MiB 的页，页目录指针项可以映射 1 GiB 的页，使 TLB 的覆盖范围扩大 512 倍或 $2^{18}$ 倍。Linux 自动以透明大页的方式提供它们（模式 `always`，或 `madvise`，即程序用 `madvise(MADV_HUGEPAGE)` 标出的区域，这台机器上的设置），也通过 `hugetlbfs` 显式提供。

### 4.4.2. 上下文切换与 TLB 击落

TLB 项属于某一个地址空间。在**上下文切换**时，内核要么冲刷 TLB，使下一个进程从未命中开始；要么用地址空间标识符（address space identifier），简称 ASID（x86-64 称之为进程上下文标识符 PCID）标记各项，使多个进程的表项共存，只有匹配的才命中。x86-64 上的 Linux 使用 PCID（`/proc/cpuinfo` 中的 `pcid` 标志），并且自 2018 年的 Meltdown 缓解措施以来，还用它廉价地保持内核页表与用户页表分离。

当内核修改或删除一个其他 CPU 可能已缓存在其 TLB 中的映射时，它必须让它们使该项失效：它向它们发送核间**中断**并等待确认，这称为 TLB 击落（TLB shootdown）。TLB 击落是 `munmap` 和 `mprotect` 在多线程程序中开销很大的原因之一。

## 4.5. 多级页表

### 4.5.1. 思想

地址空间的大部分是未使用的：在 4.1.2 节的映射中，128 TiB 中只映射了几十 MB。线性页表却为全部地址空间花费表项。

**定义 4.5.1（多级页表）** **多级页表**是由页大小的表组成的树。虚拟页号被分成几个索引字段；第一个字段索引根表，根表的表项给出第二级表的物理地址，由第二个字段索引，依此类推；最后一级表中的表项就是 PTE。只映射未使用地址的子树被省略，它在父表中的表项标记为不存在。

代价是 TLB 未命中时每一级一次内存访问；收益是表的大小与实际使用的内存成正比。另外的方案有反置页表（inverted page table），它为每个物理页框而不是每个虚拟页保存一项，以及哈希页表；二者都通过以虚拟页号为键的**散列表**来查找（PowerPC 和 Itanium 使用了这类设计）。

### 4.5.2. x86-64 上的四级分页

x86-64 使用 48 位虚拟地址（第 48–63 位必须是第 47 位的副本）和四级表，每个表是一个 4 KiB 的页，有 512 个 8 字节的表项，所以每一级消耗 9 位：

| 位 | 47–39 | 38–30 | 29–21 | 20–12 | 11–0 |
|---|---|---|---|---|---|
| 字段 | PML4 索引 | PDPT 索引 | PD 索引 | PT 索引 | 偏移 |
| 表（Intel 名称） | page map level 4 | page directory pointer table | page directory | page table | — |
| 一个表项映射 | 512 GiB | 1 GiB | 2 MiB | 4 KiB | — |

**例 4.5.1** 虚拟地址 `0x7f3a12345678`（位于某进程的内存映射区）分解为：PML4 索引 $\lfloor \mathit{va}/2^{39} \rfloor \bmod 512 = 254$，PDPT 索引 $232$，PD 索引 $145$，PT 索引 $325$，偏移 `0x678`。TLB 未命中时，遍历器从寄存器 `CR3`（由内核在每次上下文切换时装入）读出 PML4 表的物理地址，读取 PML4 的第 254 项，它指向一个 PDPT；再读其第 232 项，它指向一个页目录；再读其第 145 项，它指向一个页表；最后读其第 325 项，即带有页框号的 PTE。如果途中任何一项不存在，遍历以缺页告终。

```mermaid
flowchart LR
  CR3["CR3"] --> L4["PML4 表<br/>第 254 项"]
  L4 --> L3["PDPT<br/>第 232 项"]
  L3 --> L2["页目录<br/>第 145 项"]
  L2 --> L1["页表<br/>第 325 项"]
  L1 --> F["页框 + 偏移 0x678<br/>= 物理地址"]
```

使用一兆字节连续内存的进程在每一级需要一个表，共四个页即 16 KiB 的页表，而不是线性表的 512 GiB。在本课程使用的笔记本电脑上，所有进程的页表合计占 65 MiB（`/proc/meminfo` 中的 `PageTables`），对应约 3.6 GiB 的进程内存。自 Linux 4.14 起，具有五级分页的处理器（Intel 的 LA57，57 位地址，128 PiB 的用户空间）可以使用第五级；只有在硬件支持时内核才启用它。RISC-V 定义了类似的方案 Sv39、Sv48 和 Sv57，分别有 3、4 和 5 级（[4.10.3](/4.10.3)）；ARMv8 使用最多四级、粒度为 4、16 或 64 KiB 的表。

## 4.6. 交换与页面置换

### 4.6.1. 请求调页与缺页

到目前为止，地址空间的每一页都在内存中。存在位允许更多的可能：一页可以不在内存中但仍然有效，它的内容在文件或交换设备上，只在被访问时才调入。

**定义 4.6.1（缺页与请求调页）** **缺页**是程序访问其表项不存在、或不允许该访问的虚拟页时，MMU 引发的异常。内核的缺页处理程序判断该地址对进程是否有效；若有效，它获取一个空闲页框（必要时淘汰另一页），填充它（用零、从文件或从交换区），更新页表并返回，使出错的指令被重试。若地址无效，进程收到 `SIGSEGV`（[4.11.2](/4.11.2#sec-2.4.1)）。**请求调页**是只在页第一次被访问时才装入它的策略。**交换空间**是磁盘上的区域（分区或文件），内核把从内存中淘汰的匿名内存页存放在那里。

不需要磁盘 I/O 的缺页（第一次访问零填充的页、已在页缓存中的页、写时复制的拷贝）是次缺页（minor fault），耗时约一微秒或更少；必须从磁盘读取的缺页是主缺页（major fault），耗时从约一百微秒（SSD）到几毫秒（硬盘）。请求调页可以直接观察到：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <unistd.h>

static long minor_faults(void) {
    struct rusage u;
    getrusage(RUSAGE_SELF, &u);
    return u.ru_minflt;
}

static long rss_kib(void) {          /* resident set size from /proc */
    FILE *f = fopen("/proc/self/statm", "r");
    long pages_total, pages_resident;
    if (fscanf(f, "%ld %ld", &pages_total, &pages_resident) != 2) pages_resident = -1;
    fclose(f);
    return pages_resident * (sysconf(_SC_PAGESIZE) / 1024);
}

int main(void) {
    const size_t size = 256UL << 20;                  /* 256 MiB */
    const long page = sysconf(_SC_PAGESIZE);
    printf("page size %ld bytes\n", page);

    char *p = mmap(NULL, size, PROT_READ | PROT_WRITE,
                   MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    printf("after mmap:      RSS %7ld KiB\n", rss_kib());

    long f0 = minor_faults();
    for (size_t i = 0; i < size; i += page) p[i] = 1; /* touch every page */
    long f1 = minor_faults();
    printf("after touching:  RSS %7ld KiB, %ld page faults for %zu pages\n",
           rss_kib(), f1 - f0, size / page);

    fflush(stdout);
    pid_t pid = fork();                               /* copy-on-write */
    if (pid == 0) {
        long g0 = minor_faults();
        for (size_t i = 0; i < size / 4; i += page) p[i] = 2;  /* write a quarter */
        printf("child wrote 64 MiB: %ld copy-on-write faults\n", minor_faults() - g0);
        fflush(stdout);
        _exit(0);
    }
    waitpid(pid, NULL, 0);
    printf("parent still sees p[0] = %d\n", p[0]);
    munmap(p, size);
    return 0;
}
```

```text
page size 4096 bytes
after mmap:      RSS    1536 KiB
after touching:  RSS  263772 KiB, 65536 page faults for 65536 pages
child wrote 64 MiB: 16384 copy-on-write faults
parent still sees p[0] = 1
```

256 MiB 的 `mmap` 只是预留了地址；驻留集大小（resident set size），简称 RSS，即实际在内存中的内存没有变化。每页第一次被访问引起一次次缺页，分配一个清零的页框。`fork` 之后，子进程的每次写入都引起一次复制一页的缺页（4.7.2 节），父进程的内存不受影响。

一个后果是，Linux 默认过量承诺（overcommit）内存：即使内存不可用，对巨大块的 `malloc` 也会成功，因为它可能永远不会被访问。如果进程随后访问的内存超过内存与交换区所能容纳的，内核的 OOM 杀手（out-of-memory killer）会选择一个进程，优先选用内存最多的进程（可用 `/proc/<pid>/oom_score_adj` 调整），并用 `SIGKILL` 杀死它；内核日志（`dmesg`、`journalctl -k`）会记录这件事。**批处理作业**和容器的内存限制在它们的控制组内同样起作用（[4.11.9](/4.11.9)、[4.11.11](/4.11.11)）：超出限制的作业被杀死，状态为 137。

**例 4.6.1** 设一次内存访问需要 $m = 100\,\mathrm{ns}$，一次来自硬盘的主缺页需要 $8\,\mathrm{ms}$。每次访问的缺页概率为 $p$ 时，有效访问时间为 $(1 - p) \cdot 100\,\mathrm{ns} + p \cdot 8\,\mathrm{ms}$。要使变慢不超过 10 %，需要 $p \cdot 8 \times 10^{6}\,\mathrm{ns} < 10\,\mathrm{ns}$，即 $p < 1.25 \times 10^{-6}$：每 800000 次访问中缺页不得超过一次。对于 SSD（约 $100\,\mathrm{\mu s}$），界限宽松 80 倍，但仍然很严格。交换是安全阀，而不是用比机器所有的更多内存来计算的办法。

### 4.6.2. 置换策略

内存已满而必须调入一页时，必须淘汰另一页。此时主存充当所有地址空间的页的缓存，置换策略决定它的未命中率。未命中分为强制未命中（对页的第一次访问）、容量未命中（缓存对工作数据来说太小）和冲突未命中（在页框这样的全相联缓存中不会出现）。

**定义 4.6.2（置换策略）** 必须淘汰一页时，**最优置换算法**（OPT，Belady 的 MIN）淘汰下一次使用在最远的将来的页；**FIFO** 淘汰在内存中停留最久的页；**最近最少使用**（LRU）淘汰上一次使用在最远的过去的页；随机置换淘汰随机的一页。

OPT 使未命中数最小（Belady，1966），但需要知道未来；它充当基准。LRU 用过去预测未来，在有局部性时有效。

**例 4.6.2** 引用串 `0 1 2 0 1 3 0 3 1 2 1`，三个页框（OSTEP，第 22 章）。在 OPT 下：前三次引用未命中（强制），`0` 和 `1` 命中；`3` 未命中并淘汰 `2`，因为它的下一次使用最远；`0`、`3`、`1` 命中；`2` 未命中并淘汰 `0` 或 `3`，二者都不再被使用；`1` 命中。共 6 次命中、5 次未命中。下面是本节四种策略的模拟器：

```python
def simulate(refs, frames, policy):
    """Return the number of page faults and the trace of memory contents."""
    mem, faults, trace = [], 0, []
    last_use, ref_bit, hand = {}, {}, 0
    for t, page in enumerate(refs):
        hit = page in mem
        if not hit:
            faults += 1
            if len(mem) < frames:
                mem.append(page)
            else:
                if policy == "FIFO":                 # mem is kept in arrival order
                    victim = 0
                elif policy == "LRU":
                    victim = min(range(frames), key=lambda i: last_use[mem[i]])
                elif policy == "OPT":                # farthest next use
                    def next_use(p):
                        rest = refs[t + 1:]
                        return rest.index(p) if p in rest else float("inf")
                    victim = max(range(frames), key=lambda i: next_use(mem[i]))
                elif policy == "CLOCK":              # second chance
                    while ref_bit[mem[hand]]:
                        ref_bit[mem[hand]] = 0
                        hand = (hand + 1) % frames
                    victim = hand
                    hand = (hand + 1) % frames
                if policy == "FIFO":
                    mem.pop(0)
                    mem.append(page)
                else:
                    mem[victim] = page
        last_use[page] = t
        ref_bit[page] = 1
        trace.append(("hit " if hit else "miss") + " " + str(mem))
    return faults, trace

refs = [0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1]
for policy in ["OPT", "FIFO", "LRU", "CLOCK"]:
    f, _ = simulate(refs, 3, policy)
    print(f"{policy:5s} {f} faults, {len(refs) - f} hits")
_, trace = simulate(refs, 3, "OPT")
for page, line in zip(refs, trace):
    print(f"  ref {page}: {line}")

belady = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
for frames in [3, 4]:
    print(f"FIFO with {frames} frames: {simulate(belady, frames, 'FIFO')[0]} faults;",
          f"LRU: {simulate(belady, frames, 'LRU')[0]} faults")
```

```text
OPT   5 faults, 6 hits
FIFO  7 faults, 4 hits
LRU   5 faults, 6 hits
CLOCK 7 faults, 4 hits
  ref 0: miss [0]
  ref 1: miss [0, 1]
  ref 2: miss [0, 1, 2]
  ref 0: hit  [0, 1, 2]
  ref 1: hit  [0, 1, 2]
  ref 3: miss [0, 1, 3]
  ref 0: hit  [0, 1, 3]
  ref 3: hit  [0, 1, 3]
  ref 1: hit  [0, 1, 3]
  ref 2: miss [2, 1, 3]
  ref 1: hit  [2, 1, 3]
FIFO with 3 frames: 9 faults; LRU: 10 faults
FIFO with 4 frames: 10 faults; LRU: 8 faults
```

在这个短的引用串上，LRU 与 OPT 相同。最后两行显示了 Belady 异常（Belady's anomaly）：对 FIFO，引用串 `1 2 3 4 1 2 5 1 2 3 4 5` 在三个页框时引起 9 次缺页，在四个页框时却引起 10 次。更多的内存可能使 FIFO 变得更差。LRU 不会这样：它是一种栈算法（stack algorithm），即它在 $k$ 个页框时保留的页集合总是它在 $k + 1$ 个页框时保留的页集合的子集，所以增加页框从不增加未命中。

策略的表现取决于工作负载。图中比较了三种合成负载（对 100 个页的 10000 次引用）：没有局部性时，除 OPT 外所有策略的命中率相同，并与缓存大小成正比；对 80-20 的热点集，LRU 是实际策略中最好的；在对 50 个页的循环中，当页框少于 50 个时，LRU 和 FIFO 每次访问都未命中（每个页恰好在需要之前被淘汰），而随机置换则平缓地退化。

![三种负载下各置换策略的命中率随页框数的变化](./plots/page-replacement-hit-rates.py)

### 4.6.3. 近似 LRU：时钟算法

精确的 LRU 需要在每次内存访问时更新时间戳或链表，没有哪种硬件这样做。PTE 的访问位提供了一种廉价的近似。

**定义 4.6.3（时钟算法）** **时钟算法**（二次机会算法）把页框排成一个圆圈，有一个指针指向其中之一。为选择牺牲者，它检查指针所指的页：若它的访问位已置位，就清除该位并让指针前进；若该位为零，则该页在指针转完一整圈的期间没有被使用过，就把它淘汰。

在有局部性的负载上，时钟算法能很好地近似 LRU（图中的 "Clock" 曲线在 80-20 负载上靠近 LRU）。实际的系统对它做了改进：它们优先选择干净页而不是脏页，因为脏页在其页框可被重用之前必须写回；并且在后台写回脏页，使需要时有干净的页框可用。

### 4.6.4. 抖动与工作集

**定义 4.6.4（工作集与抖动）** 进程在时刻 $t$、窗口 $\tau$ 的**工作集**是它在最近 $\tau$ 个时间单位内引用过的页的集合（Denning，1968）。当各运行进程的工作集合起来超过物理内存时，系统把大部分时间花在内存与磁盘之间搬运页上，几乎没有进展；这就是**抖动**。

发生抖动的机器磁盘一直很忙，CPU 大多空闲（在等待缺页），而且不会自行恢复。补救办法是同时运行更少的进程（旧的系统会挂起整个进程；Linux 的 OOM 杀手是现代的残酷版本）、增加内存，或减少所使用的内存。对数据分析来说，这里的实际教训是：检查数据以及分析所做的它的副本能否放进内存（`free -h`、`top` 的 `RES` 列、用 `/usr/bin/time -v` 得到命令的峰值 RSS），放不下时就分块处理数据或使用流式工具。

### 4.6.5. Linux 中的内存回收

Linux 把所有其他方面空闲的内存用作文件数据的缓存（页缓存，[4.11.7](/4.11.7)，在 `free` 中显示为 `buff/cache`），所以"空闲"内存通常很少，有意义的数字是"可用"内存（空闲内存加上容易回收的缓存）。当空闲内存不足时，内核线程（`kswapd`）在后台回收页框，当这还不够时，分配内存的进程直接回收。

- Linux 传统上为每个内存组保存两个 LRU 链表，活跃的和不活跃的，分别用于文件页和匿名页；页根据它们的访问位在两者之间移动，这是时钟算法的双链表变体。自 Linux 6.1 起，可选的多代 LRU（MGLRU）按最近使用情况把页分为几代，降低了 CPU 开销，并在内存压力下做出更好的选择；有些发行版默认启用它（`/sys/kernel/mm/lru_gen/enabled`）。
- 参数 `vm.swappiness`（默认 60，范围 0–200）设置淘汰匿名页（到交换区）与文件页（可从文件重新读取）的相对偏好。
- 交换区不必是磁盘：zram 是内存中的压缩块设备，zswap 是交换设备前的压缩缓存；二者都用 CPU 时间换取更少的磁盘写入，常见于笔记本电脑和手机。

## 4.7. 内存映射与共享

### 4.7.1. mmap

**定义 4.7.1（内存映射）** **内存映射**是地址空间中的一个区域，它的页由文件支持（文件支持的映射，其内容就是文件的内容）或不由任何东西支持（匿名映射，初始为零）。它由系统调用 `mmap` 创建。共享映射使修改对映射同一文件的所有进程可见，并把修改写入文件；私有映射给每个进程它所修改的每一页的私有副本。

4.1.2 节的所有区域都是映射：程序的代码是可执行文件的私有只读映射，堆和栈是匿名映射。程序可以自己映射文件，然后用普通的内存访问读取它们，由内核按需装入页：

```c
#include <fcntl.h>
#include <stdio.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

/* GC content of a sequence file, read through a memory mapping. */
int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s FILE\n", argv[0]); return 2; }
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) { perror("open"); return 1; }
    struct stat st;
    fstat(fd, &st);
    const char *s = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (s == MAP_FAILED) { perror("mmap"); return 1; }
    close(fd);                               /* the mapping stays valid */
    madvise((void *)s, st.st_size, MADV_SEQUENTIAL);   /* hint: read ahead */
    long gc = 0, acgt = 0;
    for (off_t i = 0; i < st.st_size; i++) {
        char c = s[i];                       /* page faults load the file lazily */
        if (c == 'G' || c == 'C') gc++;
        if (c == 'A' || c == 'C' || c == 'G' || c == 'T') acgt++;
    }
    printf("%ld bases, GC content %.4f\n", acgt, (double)gc / acgt);
    munmap((void *)s, st.st_size);
    return 0;
}
```

对一个 100 MB 的文件（一百万行随机生成的、每行 99 个碱基，C 和 G 各占 20 %）：

```text
99000000 bases, GC content 0.4000
```

内存映射避免了把数据从内核复制到用户缓冲区，并使多个进程能共享一个大的只读文件（索引、参考基因组）的同一份副本；NumPy 的 `np.memmap` 和许多生物信息学索引都使用它。它的代价是缺页而不是大块读取，以及当文件在映射之下缩小时以 `SIGBUS` 出现的错误。对于单次顺序扫描，用大缓冲区的普通 `read` 调用一样快（[4.11.8](/4.11.8)）。

### 4.7.2. 写时复制

**定义 4.7.2（写时复制）** **写时复制**（COW）是在多个地址空间之间、或在私有映射与它的文件之间共享一页的技术：把它以只读方式映射到所有这些空间，只在其中一个写入时才复制它：写入引发故障，故障处理程序把该页复制到新的页框，为写入者把副本映射为可写，并重试写入。

写时复制使 `fork` 开销很小（[4.11.2](/4.11.2#sec-2.2.1)）：只复制页表，页在父进程或子进程修改它们时逐页复制；在 4.6.1 节的测量中，子进程写入 64 MiB 恰好引起 16384 次复制缺页。它也使私有文件映射开销很小：程序的数据区域与可执行文件共享，直到程序写某个变量。Python 的 multiprocessing 在 `fork` 启动方式下依靠它免费地给工作进程提供大的只读数据结构；引用计数会写入它访问的每个对象，这会逐渐破坏这种共享。

### 4.7.3. 共享库

**动态库**（[4.2.2](/4.2.2)）通过把它的文件映射到使用它的每个进程中来加载。代码页以只读方式映射并共享，所以 C 库 1.6 MB 的代码只需一份物理副本就能服务机器上的每个进程；只有每个进程写入的页（它自己的库全局变量和指针表的副本）通过写时复制成为私有的。由于库在每个进程中被映射到不同的（随机化的）地址，它的代码被编译为**位置无关代码**（`-fPIC`）：它通过相对于**程序计数器**的地址访问自己的数据，并通过动态链接器填写的指针表（全局偏移表 GOT 和过程链接表 PLT）调用其他库中的函数。`ldd` 列出程序将要映射的库：

```text
$ ldd ./maps
	linux-vdso.so.1 (0x00007fff9892b000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ec408600000)
	/lib64/ld-linux-x86-64.so.2 (0x00007ec408904000)
```

vDSO 被列为库，尽管没有文件支持它：内核把它映射到每个进程中。库的搜索路径（`LD_LIBRARY_PATH`、记录在可执行文件中的路径、`/etc/ld.so.cache`）是在发行版的**包管理器**之外安装的软件常出问题的来源，这也是需要 [4.11.9](/4.11.9) 和 [4.11.11](/4.11.11) 中的环境管理器和容器的原因之一。

## 小结

- 每个进程有一个由虚拟地址组成的私有地址空间，MMU 在每次访问时把它翻译为物理地址。在 x86-64 Linux 上，用户空间的上半部分（128 TiB）容纳程序、堆、带有库的内存映射区和栈，它们的地址由 ASLR 随机化。
- 基址与界限能重定位和保护，但需要连续的内存；分段分配大小可变的段，受外部碎片之苦。分页把内存划分为固定大小的页和页框；页表项保存页框号以及存在、权限、访问和脏位。
- TLB 缓存转换；局部性使它的命中率接近 100 %，大页扩大它的覆盖范围。ASID（PCID）避免上下文切换时的冲刷；修改映射需要 TLB 击落。
- 多级页表只存储表中使用的部分：x86-64 遍历四级、每级 512 项的表（9 + 9 + 9 + 9 + 12 位）。
- 页按需装入：缺页调入该页并重试指令。Linux 过量承诺内存，内存耗尽时用 OOM 杀手杀死进程。
- OPT 淘汰在最远的将来才使用的页，是基准；LRU 在有局部性的负载上近似它，并且与 FIFO 不同，没有 Belady 异常；时钟算法用访问位近似 LRU。当工作集超过内存时，系统发生抖动。
- `mmap` 映射文件和匿名内存；写时复制使 `fork` 和私有映射开销很小；共享库在内存中只映射一份，由所有进程共享，使用位置无关代码。
