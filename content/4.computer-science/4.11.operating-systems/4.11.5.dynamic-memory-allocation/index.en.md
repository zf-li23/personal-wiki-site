---
title: Dynamic Memory Allocation
description: "How malloc and free work: the heap and the system calls brk and mmap; requirements and goals of an allocator, throughput and utilization, internal and external fragmentation; implicit free lists with boundary tags, placement, splitting and coalescing, with a complete small allocator in C; explicit and segregated free lists, the buddy system and slab allocation; glibc's allocator, tcache and arenas; memory errors in C as seen from the allocator, AddressSanitizer; garbage collection by mark-and-sweep, copying and generations."
---

Programs request memory whose size or lifetime is not known when they are compiled: a vector that grows, a tree built from input, a buffer for a file of unknown length. This is **dynamic memory allocation** ([4.1.8](/4.1.8)), served in C by `malloc` and `free`, in C++ by `new` and `delete` (which call the same allocator), and in Python and other managed languages by a runtime that allocates for every object. The **kernel** provides memory to a process only in large, page-sized pieces, through the **system calls** `brk` and `mmap` ([4.11.4](/4.11.4)); a user-space library, the *allocator*, divides those pieces into blocks of arbitrary size and takes them back. This chapter explains how: the goals an allocator must balance, the data structures it keeps inside the free memory itself, a complete small allocator in C, and the designs used in practice, from glibc's `malloc` to the buddy and slab allocators of the Linux kernel. It then looks at the familiar memory errors of C from the allocator's side, and at **garbage collection**, the alternative in which the runtime finds unused memory itself.

## 5.1. The Heap and the Allocator Interface

### 5.1.1. Where the Memory Comes From

**Definition 5.1.1 (Dynamic Memory Allocator)** A **dynamic memory allocator** manages a region of a process's virtual memory, the heap, as a collection of variable-sized *blocks*, each either *allocated* (in use by the program) or *free*. An *explicit* allocator requires the program to free blocks itself (`malloc` and `free` in C, `new` and `delete` in C++); an *implicit* allocator, or garbage collector, detects and frees blocks that the program can no longer use.

On Linux the classic heap is a contiguous region after the program's data; its end, the *program break*, is moved by the **system call** `brk` (`sbrk` in the library), and the allocator obtains more memory by raising it. For large requests, and for the heaps of additional threads, allocators use anonymous `mmap` mappings instead, which can be returned to the kernel individually with `munmap`. Pages obtained either way occupy physical memory only once they are touched (**demand paging**, [4.11.4](/4.11.4#sec-4.6.1)).

The C interface:

| Function | Meaning |
|---|---|
| `void *malloc(size_t n)` | allocate at least `n` bytes, uninitialized; `NULL` on failure |
| `void *calloc(size_t k, size_t n)` | allocate `k * n` bytes (checking overflow), zero-filled |
| `void *realloc(void *p, size_t n)` | resize the block, moving its contents if necessary |
| `void free(void *p)` | release a block returned by one of the above; `free(NULL)` does nothing |
| `void *aligned_alloc(size_t a, size_t n)` | allocate with alignment `a` (C11) |

Returned blocks are aligned for any type: on x86-64 Linux to 16 bytes. glibc shows how its allocator rounds requests:

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

The smallest block offers 24 usable bytes, and sizes grow in steps of 16: each block carries 8 bytes of bookkeeping and occupies a multiple of 16 bytes (32 bytes for `malloc(1)`). The gap of 4 KiB after the first block is the output buffer that the first `printf` allocated for `stdout`. The 200000-byte request exceeded glibc's *mmap threshold* (initially 128 KiB, adjusted dynamically) and received its own mapping, rounded up to whole pages.

### 5.1.2. Requirements and Goals

An explicit allocator works under hard constraints. It must handle any sequence of `malloc` and `free` calls, answering each immediately, without knowing future requests; it cannot move allocated blocks, since the program holds pointers to them; it must align blocks; and it may keep its own data structures only in the heap itself. Within these constraints it pursues two conflicting goals:

- **Throughput**: the number of requests served per second. Good allocators serve the common cases in a few dozen instructions.
- *Memory utilization*: how much of the heap holds data the program asked for. If after request $k$ the program holds allocated payloads of total size $P_k$ and the heap has size $H_k$, the *peak utilization* after $n$ requests is $U_n = \max_{i \le n} P_i \,/\, H_n$.

Utilization is lost to fragmentation, of two kinds.

**Definition 5.1.2 (Internal Fragmentation)** **Internal fragmentation** is the waste of memory inside allocated blocks, when a block is larger than the payload it holds: because of headers, alignment, minimum block sizes, or rounding up to a size class.

The opposite kind, **external fragmentation** ([4.11.4](/4.11.4#sec-4.2.2)), is free memory scattered in pieces between allocated blocks, none large enough for a request. Internal fragmentation is easy to measure; external fragmentation depends on future requests and is the harder problem.

## 5.2. Free Lists

### 5.2.1. Implicit Free Lists and Boundary Tags

An allocator must find a free block for each request, and find the size of each block passed to `free` (which receives only a pointer). The simplest structure that achieves both stores a header in front of every block.

**Definition 5.2.1 (Implicit Free List and Boundary Tags)** In an **implicit free list** every block begins with a *header* word that holds the block's size and a bit indicating whether it is allocated; the blocks are traversed in address order by adding each block's size to its address, so the free blocks are linked implicitly through the sizes of all blocks. A **boundary tag** is a copy of the header at the end of the block, the *footer*, which lets the allocator find the size and status of the block that precedes any given block in constant time (Knuth, 1968).

Because block sizes are multiples of 16, the low four bits of the size are always zero, and the allocated bit is stored in one of them. A block of 32 bytes holding a 10-byte payload looks like this:

| Offset | 0–7 | 8–17 | 18–23 | 24–31 |
|---|---|---|---|---|
| Content | header: `32 \| 1` | payload (10 bytes) | padding | footer: `32 \| 1` |

The pointer returned to the program points to offset 8; the header is at `p - 8`.

Serving a request involves three decisions.

- *Placement*: which free block to use. *First fit* scans from the beginning and takes the first free block that is large enough; *next fit* starts where the previous search ended; *best fit* examines all free blocks and takes the smallest one that fits. First fit is simple and leaves large blocks at the end of the heap but accumulates small "splinters" near the beginning; best fit tends to have the best utilization but needs a full search unless the free blocks are organized by size (§5.3).
- *Splitting*: if the chosen free block is much larger than the request, the allocator splits it into an allocated part and a free remainder; otherwise it allocates the whole block and accepts the internal fragmentation.
- *Coalescing*: when a block is freed, adjacent free blocks are merged with it into one larger block. Without coalescing, the heap fills with adjacent small free blocks, *false fragmentation*, that could satisfy a larger request together but not separately. With boundary tags, coalescing is constant-time in all four cases: the neighbors before and after are allocated or free.

### 5.2.2. A Small Allocator

The following allocator implements an implicit free list with boundary tags, first-fit placement, splitting and immediate coalescing over a 1 MiB arena obtained with `mmap`. A *prologue* block at the beginning and an *epilogue* header of size 0 at the end are permanently allocated, so that coalescing never has to check the edges of the heap.

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

The heap after each step, as `[A size]` for allocated and `[f size]` for free blocks:

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

Each request is rounded up to a multiple of 16 after adding 16 bytes for header and footer: 10 bytes need a 32-byte block, 100 bytes a 128-byte block. The request for 40 bytes (a 64-byte block) is placed in the 128-byte hole left by `b`, which is split. Freeing exercises the coalescing cases one after another until the heap is again a single free block. The allocator is correct but slow: `mm_malloc` scans all blocks, allocated or free, so a request costs time linear in the number of blocks. Production allocators differ mainly in how they find free blocks quickly.

### 5.2.3. Explicit Free Lists

An *explicit free list* links only the free blocks, storing the list pointers in the payload area of each free block (which the program is not using). Allocation then takes time linear in the number of free blocks only. Freed blocks can be inserted at the front of the list (LIFO order: constant time, good **locality** for blocks reused soon) or in address order (a free needs a search, but first fit in address order has better utilization, close to best fit). The pointers set a minimum block size: header, two pointers and footer make 32 bytes on a 64-bit machine.

## 5.3. Segregated Fits, Buddies and Slabs

### 5.3.1. Segregated Free Lists

**Definition 5.3.1 (Segregated Free Lists)** An allocator with **segregated free lists** partitions block sizes into *size classes* (for example 16, 32, 48, …, 512, then powers of two) and keeps a separate free list for each class. A request is served from the list of its class, or from a larger class if that list is empty, splitting the block found and placing the remainder in the list of its own class.

With segregated fits, a search examines only blocks of roughly the right size, which approximates best fit at the speed of first fit. Most production allocators use some form of it. Small objects of identical size are often served by *simple segregated storage*: a page is cut into equal blocks of one class, free blocks are kept on a singly **linked list**, allocation and freeing are a pop and a push, and no headers, splitting or coalescing are needed, at the cost of internal fragmentation and pages that cannot be reused for other sizes until all their blocks are free.

### 5.3.2. The Buddy System

**Definition 5.3.2 (Buddy System)** In the **binary buddy system** the memory is a block of $2^m$ bytes, and every block has a size that is a power of two. A request for $n$ bytes is rounded up to the smallest power of two $2^k \ge n$. If no free block of size $2^k$ exists, a larger free block is split repeatedly into two halves, the *buddies*, until a block of size $2^k$ is obtained. When a block is freed and its buddy is also free, the two are merged into a block of twice the size, repeatedly.

The buddy of the block at offset $a$ with size $2^k$ is at offset $a \oplus 2^k$ (**exclusive or**): buddies differ in exactly one bit of their address, so finding the partner for coalescing costs nothing.

**Example 5.3.1** A 1 MiB region is empty. A request for 100 KiB is rounded to 128 KiB. The region is split into two 512 KiB buddies, the first of those into two 256 KiB buddies, and the first of those into two 128 KiB buddies; the request gets the block at offset 0, wasting 28 KiB to internal fragmentation. Free blocks remain at offsets 128 KiB (128 KiB), 256 KiB (256 KiB) and 512 KiB (512 KiB). A request for 200 KiB then takes the 256 KiB block at offset 256 KiB. When the first block is freed, its buddy at offset $0 \oplus 128\,\mathrm{KiB} = 128\,\mathrm{KiB}$ is free, so they merge into a 256 KiB block at offset 0; that block's buddy, at offset 256 KiB, is allocated, so merging stops.

The buddy system coalesces quickly but rounding to powers of two wastes up to half of each block. The Linux kernel uses it to manage physical **page frames**: it allocates blocks of $2^k$ contiguous pages for *order* $k$ from 0 to 10 (4 KiB to 4 MiB). `/proc/buddyinfo` shows the number of free blocks of each order:

```text
Node 0, zone    DMA32   2818   1894   1608   1265    824    462    302    174    136    145    710
Node 0, zone   Normal    151     97     56     75     60     27      6      3      1      1    166
```

The last column counts free 4 MiB blocks. A shortage of high-order blocks while low-order ones abound is **external fragmentation** of physical memory; the kernel counters it by compaction, migrating movable pages (it can, since it controls the **page tables**) to form contiguous free ranges, for example for **huge pages**.

### 5.3.3. Slab Allocation

The kernel allocates many small objects of a few fixed types: process descriptors, inodes, network buffers. The *slab allocator* (Bonwick, 1994, for Solaris) keeps a *cache* for each object type, consisting of slabs (one or more pages from the buddy allocator) cut into objects of that type: simple segregated storage with per-CPU free lists, which make the common allocation and free lock-free on the local CPU. Linux's implementation is SLUB (the alternatives SLOB and SLAB were removed in 2023 and 2024); its caches appear under `/sys/kernel/slab`, and `kmalloc` serves general-purpose kernel requests from caches of sizes 8, 16, 32, …, 8192 bytes.

### 5.3.4. Allocators in User Space

glibc's `malloc` (ptmalloc2, derived from Doug Lea's allocator) combines these ideas:

- each thread has a *tcache* (since glibc 2.26, 2017): small per-thread lists for 64 size classes of up to about 1 KiB, seven blocks each, served without locks;
- behind it, *arenas*: heaps with their own lock, the main one grown by `brk`, others created by `mmap` for additional threads (up to eight per core), each with segregated bins of free chunks (fast bins for small sizes without coalescing, small bins of exact sizes, large bins sorted by size, an unsorted bin of recently freed chunks);
- requests above the mmap threshold go directly to `mmap`.

Other widely used allocators are jemalloc (FreeBSD, Firefox, many servers), tcmalloc (Google) and mimalloc (Microsoft; also used by the free-threaded build of CPython, [4.4.7](/4.4.7)); they emphasize per-thread caches, size-class pages and returning memory to the system, and can be substituted for glibc's without recompiling (`LD_PRELOAD=libjemalloc.so ./program`). Multithreaded programs that allocate heavily, such as many bioinformatics tools, can run noticeably faster or use less memory with them. Above the C allocator, language runtimes add their own layers: CPython keeps a small-object allocator (`pymalloc`) for objects up to 512 bytes, and NumPy allocates array data with `malloc` or `mmap` directly.

## 5.4. Memory Errors from the Allocator's Side

The errors of [4.1.8](/4.1.8) (out-of-bounds access, **dangling pointers**, double free, **memory leaks**) look different once one knows where the allocator keeps its data. A write past the end of a block overwrites the next block's header or, in a free block, the list pointers; the damage appears later, in an unrelated `malloc` or `free`. Freeing a block twice inserts it twice into a free list, so two later `malloc` calls return the same memory. Reading a block after freeing it may return list pointers written by the allocator. These errors are **undefined behavior** in C and C++, and they are the root of most memory-safety vulnerabilities: an attacker who controls the overwritten bytes can make the allocator write chosen values to chosen addresses.

glibc checks some of its invariants and aborts when they are violated, but it cannot detect everything:

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

Run with two arguments, so that both errors occur:

```text
free(): double free detected in tcache 2
bash: line 1: 30732 Aborted                 (core dumped) ./uaf 1 2
exit status 134
```

The double free is caught (the program is killed with `SIGABRT`, status $128 + 6$), but the one-byte overflow went unnoticed, because the block's usable size is 24 bytes and the overflow did not reach the next header. Compiled with AddressSanitizer (`gcc -g -fsanitize=address`), the same program stops at the overflow itself (output abridged, file names shortened):

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

AddressSanitizer replaces the allocator: it surrounds every block with *redzones*, keeps freed blocks in quarantine instead of reusing them at once, and records in *shadow memory* (one byte for every 8 bytes of the **address space**) which bytes are addressable; the compiler inserts a check of the shadow byte before every memory access. Programs run about twice as slowly, which is acceptable for testing. Valgrind's Memcheck finds the same errors without recompiling, by running the program on a simulated processor, 10 to 50 times more slowly. Other useful tools are `-fsanitize=undefined` for undefined behavior in arithmetic, glibc's malloc debugging library (`LD_PRELOAD=libc_malloc_debug.so MALLOC_CHECK_=3 ./program`) for extra heap checks, and `heaptrack` or Valgrind's Massif for finding where a program's memory goes.

## 5.5. Garbage Collection

### 5.5.1. Reachability

**Garbage collection** ([4.1.8](/4.1.8)) frees the programmer from calling `free`. The collector cannot know which blocks the program will use again, but it can determine which ones it *could* use: those reachable through pointers.

**Definition 5.5.1 (Reachability)** View memory as a directed graph whose nodes are the heap blocks and the *roots* (registers, stack slots and global variables that hold pointers), with an edge from $u$ to $v$ if $u$ contains a pointer to $v$. A block is **reachable** if there is a path from some root to it; unreachable blocks are *garbage* and can be reclaimed.

**Reference counting** ([4.2.12](/4.2.12)) approximates reachability locally: an object whose count drops to zero is certainly unreachable. It frees memory promptly and incrementally, but a cycle of objects that refer to each other keeps positive counts after it becomes unreachable, and every pointer assignment pays for count updates (atomic ones, in multithreaded programs). Tracing collectors compute reachability directly.

### 5.5.2. Tracing Collectors

**Definition 5.5.2 (Mark-and-Sweep)** A **mark-and-sweep** collector (McCarthy, 1960, for Lisp) works in two phases: the *mark* phase traverses the graph from the roots and sets a mark bit in every reachable block; the *sweep* phase scans the whole heap and frees every unmarked block (clearing the marks of the others).

Mark-and-sweep handles cycles, but it stops the program while it runs (unless made *incremental* or *concurrent*), its sweep touches the whole heap, and it leaves the free space fragmented. Two refinements underlie most modern collectors:

- A *copying collector* divides the heap into two halves and copies the reachable objects from the half in use into the other, compactly, updating the pointers; the old half is then free as a whole. Allocation becomes a pointer increment, and fragmentation disappears, at the cost of half the memory and of moving objects (which requires that the collector knows exactly which words are pointers).
- A *generational collector* exploits the observation that most objects die young: it allocates objects in a small young generation, collected often and cheaply (usually by copying), and promotes objects that survive several collections to an old generation, collected rarely. Pointers from old to young objects are tracked by a *write barrier*, code executed on every pointer store.

C and C++ compilers do not record which words are pointers, but a *conservative* collector, such as the Boehm–Demers–Weiser collector, can still trace such programs: it treats every word that looks like an address inside the heap as a pointer. It never frees reachable memory, but may retain some garbage, and it cannot move objects.

In practice: CPython uses reference counting plus a generational cycle collector (the `gc` module); Java's HotSpot virtual machine offers several generational and concurrent collectors (G1 by default, ZGC with pauses below a millisecond for heaps of terabytes); Go uses a concurrent mark-and-sweep collector; JavaScript engines use generational copying collectors; R uses a generational mark-and-sweep collector. Rust and modern C++ take a third path, without a collector: ownership is part of the type system (`unique_ptr`, `shared_ptr`; Rust's borrow checker), and memory is freed deterministically when its owner goes out of scope ([4.2.12](/4.2.12)).

## Summary

- The allocator divides memory obtained from the kernel (`brk` for the main heap, `mmap` for large blocks and other arenas) into blocks; it must answer each request immediately, cannot move blocks and keeps its data in the heap itself. Its goals are throughput and utilization, which internal and external fragmentation reduce.
- An implicit free list stores size and allocated bit in a header; boundary tags (footers) make coalescing with both neighbors constant-time. Placement by first, next or best fit, splitting of large free blocks and coalescing on free are the basic operations; the small allocator of §5.2.2 implements them in about 100 lines.
- Explicit free lists link only the free blocks; segregated lists keep one list per size class and approximate best fit quickly; the buddy system rounds to powers of two and finds partners by an exclusive or (Linux's page allocator); slab allocators keep caches of equal-sized objects (SLUB in Linux).
- glibc combines per-thread tcaches, arenas with segregated bins and direct `mmap` for large requests; jemalloc, tcmalloc and mimalloc are drop-in alternatives.
- Heap overflows, double frees and use after free corrupt the allocator's own data and are exploitable; glibc catches some of them, AddressSanitizer and Valgrind find them reliably.
- Garbage collectors free unreachable blocks: reference counting locally (missing cycles), mark-and-sweep by tracing from the roots, copying and generational collectors more efficiently; conservative collectors work even for C.
