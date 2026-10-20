---
title: Pointers and Memory
description: Variable addresses and pointers, pointer arithmetic, arrays and pointers, memory regions (code, static, stack, heap), new and delete, common memory errors (out-of-bounds access, dangling pointers, memory leaks) and tools for detecting them, modern C++ alternatives; Python comparison, covering names and objects, mutability, garbage collection.
source_hash: 6626daa093b3
---

The previous chapters treated a variable as a "named box": we assign a value to it and read the value back without caring where the box sits. This chapter opens the box. Every variable occupies a range of bytes in memory and has an address of its own, and a variable that stores an address is a pointer. Pointers let a program access data indirectly, request memory at run time, and build data structures of arbitrary shape out of nodes and links (linked lists in the next chapter, trees and graphs in [4.3 Data Structures and Algorithms](/4.3)). Pointers are also the most common source of bugs in C++ programs: out-of-bounds access, dangling pointers, and memory leaks all involve them. We first explain what pointers mean and how to compute with them, then the relation between arrays and pointers, the memory regions of a program and dynamic memory, and finally common errors and how modern C++ avoids them. Smart pointers and RAII are discussed in detail in [4.2.4](/4.2.4) and [4.2.12](/4.2.12). The chapter ends with Python: Python has no pointers, but its model of "names referring to objects" is best understood in terms of pointers.

## 8.1. Addresses and Pointers

### 8.1.1. The Address of a Variable

Memory can be viewed as a long sequence of storage cells numbered by byte; the number is the address. A variable has three parts: a name (an identifier for human readers), an address (where it starts in memory), and a value (the contents of those bytes). After compilation the name disappears; the machine knows only addresses and values.

C++ obtains the address of a variable with the address-of operator `&` and its size in bytes with `sizeof`:

```cpp
#include <iostream>

int main() {
    int n = 8;
    double x = 3.5;
    std::cout << "n: address " << &n << ", size " << sizeof n << '\n';
    std::cout << "x: address " << &x << ", size " << sizeof x << '\n';
}
```

Addresses are usually displayed in hexadecimal (such as `0x7ffd5c3a1e4c`) and may differ from run to run: modern operating systems randomize a program's memory layout to make it harder for attackers to exploit vulnerabilities.

### 8.1.2. Pointer Variables

**Definition 8.1.1 (Pointer)** A variable whose value is the address of some object is called a **pointer**. A pointer to an object of type `T` has type `T*`. Applying the dereference operator `*` to a pointer `p` yields the object `*p` that `p` points to. A pointer that points to no object is called a **null pointer**; since C++11 it is written `nullptr`.

```cpp
int n = 8;
int* p = &n;     // p holds the address of n
*p = 10;         // writes through p: now n == 10
int* q = nullptr; // a null pointer; *q would be undefined behaviour
```

The `*` in `int* p` is part of the type, whereas the `*` in the expression `*p` is an operator; the two have different meanings. In the declaration `int* p, q;` only `p` is a pointer and `q` is an `int`, so declare one pointer per line. In older code, `NULL` and `0` also denote the null pointer, but they are really integers and can select the wrong version in function overloading; modern C++ always uses `nullptr`.

The first use of pointers is to let a function modify the caller's variables. With **pass by value**, the function receives a copy of the argument (see [4.1.4](/4.1.4)); passing an address instead allows it to overwrite the original variable by dereferencing:

```cpp
#include <iostream>

void swap_values(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main() {
    int x = 1, y = 2;
    swap_values(&x, &y);
    std::cout << x << ' ' << y << '\n';  // 2 1
}
```

C++ also provides references `int&`, which are written like ordinary variables and are usually implemented with addresses underneath. For function parameters, references are generally preferred ([4.2.6](/4.2.6)); what is unique to pointers is that they can be null, can be redirected to another object, and support arithmetic.

### 8.1.3. Pointer Arithmetic and const

Integers can be added to and subtracted from pointers: if `p` points to an element of an **array**, then `p + k` points to the element `k` positions further. The address actually increases by `k * sizeof(T)` bytes, so the type of the pointer determines how long "one step" is. Two pointers into the same array can be subtracted (giving the number of elements between them) and compared. Pointer arithmetic is defined only within one array (and the position one past its end); going beyond that range is undefined behavior (§8.4).

Where `const` is placed relative to `*` determines what is restricted:

| Declaration | Can `*p` be changed? | Can `p` be changed? | Reading |
|---|---|---|---|
| `const int* p` | No | Yes | pointer to constant |
| `int* const p` | Yes | No | constant pointer |
| `const int* const p` | No | No | constant pointer to constant |

Reading a declaration from right to left is the least error-prone way: `int* const p` reads "p is a constant, and it is a pointer to int". When a function only reads the data a pointer refers to, writing the parameter as `const T*` both states the intent and lets the compiler prevent accidental writes.

## 8.2. Arrays and Pointers

### 8.2.1. Array Names and Pointers

The elements of an **array** are stored contiguously in memory: elements with adjacent indices have adjacent addresses, differing by `sizeof(element type)` bytes. In most expressions an array name is automatically converted to a pointer to its first element, called array-to-pointer decay. Hence, for `int a[5]`,

$$
a[i] \equiv *(a + i), \qquad a + i \equiv \&a[i],
$$

so the subscript operator is itself defined by pointer arithmetic. Conversely, a pointer to an array element can also be subscripted: `p[i]` is `*(p + i)`.

An array name is not a pointer variable. Two exceptions reveal the difference: `sizeof a` gives the number of bytes of the whole array, while `sizeof p` is merely the size of an address (8 on a 64-bit platform); and an array name can be neither assigned to nor incremented.

```cpp
#include <iostream>

int main() {
    int a[5] = {1, 2, 1, 2, 9};
    int* p = a;                       // decay: p == &a[0]
    std::cout << sizeof a << ' ' << sizeof p << '\n';  // 20 8 on a 64-bit platform
    for (int* q = a; q != a + 5; ++q) // a pointer used as a loop variable
        std::cout << *q << ' ';
    std::cout << '\n' << p[2] << ' ' << *(a + 2) << '\n'; // 1 1
}
```

### 8.2.2. Arrays as Function Parameters

An array used as a function parameter also decays to a pointer: `void f(int a[])`, `void f(int a[10])`, and `void f(int* a)` are exactly equivalent, and inside the function `sizeof a` is just the size of a pointer; the length information is lost. The traditional style therefore always passes an extra length parameter, `f(a, n)`. Modern C++ offers better choices:

- For sequences of variable length, use `std::vector<T>`, passed by reference (`const std::vector<T>&`), so that the length travels with the object.
- For a function that only needs to "look at a run of contiguous elements", use C++20's `std::span<const T>`, which packages "pointer + length" and accepts built-in arrays, `std::vector`, and `std::array`.

```cpp
#include <iostream>
#include <span>
#include <vector>

int sum(std::span<const int> xs) {  // pointer + length in one object
    int s = 0;
    for (int x : xs) s += x;
    return s;
}

int main() {
    int a[] = {1, 2, 3};
    std::vector<int> v = {4, 5, 6, 7};
    std::cout << sum(a) << ' ' << sum(v) << '\n';  // 6 22
}
```

### 8.2.3. Memory Layout of Multidimensional Arrays

A C++ two-dimensional array `int m[3][4]` is an array of "3 arrays of length 4", stored contiguously in row-major order: `m[i][j]` is the $(4i + j)$-th `int` after the starting address. Because the compiler needs the number of columns to compute offsets, a two-dimensional array parameter must state it: `void f(int m[][4], int rows)`. The true type of the formal parameter is then `int (*)[4]`, a pointer to an array of length 4.

Note the difference between two similar declarations:

| Declaration | Meaning |
|---|---|
| `int (*p)[4]` | a pointer to "an array of 4 ints" |
| `int* p[4]` | an array of 4 elements, each of which is an `int*` |

When a matrix must be passed to a function, the modern approach is to store it as a one-dimensional `std::vector<double>` accessed as `i * cols + j`; this keeps the storage contiguous (cache-friendly) and avoids dealing with these types. C++23's `std::mdspan` provides a standard view for such "one-dimensional storage, multidimensional access".

## 8.3. Dynamic Memory

### 8.3.1. Memory Regions

The memory of a running program is roughly divided into four regions, and the region in which a variable lives determines its **lifetime**:

| Region | Contents | Allocated and released | Characteristics |
|---|---|---|---|
| Code | compiled machine instructions | when the program is loaded | read-only |
| Static (data) | global variables, `static` variables, string literals | from program start to end | not explicitly initialized ones are zeroed |
| Stack | local variables, function parameters, return addresses | allocated automatically on call, released on return | fast, but limited in size (typically a few MB) |
| Heap | objects requested with `new` | explicitly requested and released by the programmer | large; lifetime controlled by the program |

Each function call pushes a **stack frame** onto the stack, holding the parameters and local variables of that call; when the function returns, the frame is popped and its variables become invalid. This is the physical realization of the **call stack** of [4.1.4](/4.1.4), and the recursion of [4.1.10](/4.1.10) depends on it as well. The size of the stack is fixed when the program starts, so recursing too deeply or defining an overly large local array in a function (such as `int a[10000000];`) causes a **stack overflow**.

### 8.3.2. new and delete

The size of a stack object must be known at compile time, and its lifetime is tied to the function call. When the length of an array is known only at run time, or an object must outlive the function that created it, we allocate on the heap.

**Definition 8.3.1 (Dynamic Memory Allocation)** Requesting a block of memory from the system at run time as needed, and explicitly returning it after use, is called **dynamic memory allocation**. In C++, `new T` creates an object of type `T` on the heap and returns its address, and `new T[n]` creates an array of `n` elements (where `n` may be a variable); `delete p` and `delete[] p` release them, respectively.

```cpp
#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int* a = new int[n];          // size known only at run time
    for (int i = 0; i < n; ++i) a[i] = i * i;
    std::cout << a[n - 1] << '\n';
    delete[] a;                   // every new[] needs exactly one delete[]
    a = nullptr;                  // do not keep a dangling address
}
```

The rules are simple but hard to follow: pair `new` with `delete` and `new[]` with `delete[]`, release each block exactly once, and never use it after release.

The traditional way to build a two-dimensional dynamic array takes two steps: first allocate an array of `m` pointers, then allocate one row for each pointer; release proceeds in strictly the opposite order:

```cpp
int** e = new int*[m];               // step 1: an array of m row pointers
for (int i = 0; i < m; ++i)
    e[i] = new int[n];               // step 2: one row of n ints for each pointer
// ... use e[i][j] ...
for (int i = 0; i < m; ++i) delete[] e[i];  // release the rows first
delete[] e;                                  // then the array of pointers
```

The rows of such a structure are not contiguous in memory, both allocation and release require loops, and a mistake in any step leaks memory. Its value is in helping us understand "pointers to pointers"; in actual programs, use the approach of the next subsection.

### 8.3.3. The Modern Approach

The fundamental problem of manual memory management is that the responsibility for releasing memory falls on the programmer, while a function may have several exits (`return`, exceptions), and forgetting `delete` at any one of them is an error. The modern C++ principle is to let objects manage their resources themselves, releasing them automatically through the destructor when they leave scope (this idea is called RAII, see [4.2.4](/4.2.4)):

| Need | Manual approach | Modern approach |
|---|---|---|
| Array whose length is fixed at run time | `new T[n]` / `delete[]` | `std::vector<T> a(n);` |
| Matrix | `new T*[m]` + loop | `std::vector<T> a(m * n);`, accessed as `a[i * n + j]` |
| String | `new char[len + 1]` | `std::string` |
| Single heap object (exclusive ownership) | `new T` / `delete` | `auto p = std::make_unique<T>();` |
| Heap object shared in several places | manual counting | `std::shared_ptr<T>` |

`std::unique_ptr` and `std::shared_ptr` are called **smart pointers**, discussed in detail in [4.2.12](/4.2.12). The rule of thumb is that application code contains no bare `new` and `delete`; a raw pointer `T*` is used only to "observe" an object owned by someone else and is not responsible for releasing it. Learning raw pointers remains necessary: the standard containers, smart pointers, and the linked lists of the next chapter are all built on them, and addresses are what we see when debugging.

## 8.4. Common Memory Errors

C++ does not check whether a pointer is valid. Reading or writing through an invalid pointer is **undefined behavior** ([4.1.2](/4.1.2)): the program may crash, may "appear to work", or may silently corrupt other data, and the behavior changes with the compiler or optimization level. The most common kinds are the following:

**Definition 8.4.1** A pointer that still holds the old address after the object it pointed to has been released or has ended its lifetime is called a **dangling pointer**. Dynamically allocated memory that is no longer referenced by any pointer but has not been released, and so can never be reclaimed before the program ends, is called a **memory leak**.

| Error | Typical code | Consequence |
|---|---|---|
| Out-of-bounds access | `int a[30]; a[30] = 1;` | overwrites an adjacent variable, often showing up elsewhere |
| Uninitialized pointer | `int* p; *p = 1;` | writes to a random address |
| Dereferencing a null pointer | `int* p = nullptr; *p = 1;` | usually crashes immediately (segmentation fault) |
| Dangling pointer: use after free | `delete[] a; a[0] = 1;` | may read the old value, or may corrupt the heap |
| Dangling pointer: returning the address of a local variable | `int* f() { int x = 1; return &x; }` | the stack frame has been popped; the address is invalid |
| Double free | `delete p; delete p;` | corrupts the heap's bookkeeping structures |
| Memory leak | `new` in a loop without `delete`; overwriting the only pointer | memory grows steadily in long-running programs |
| Mixing `new[]` and `delete` | `int* a = new int[4]; delete a;` | undefined behavior |

Use after free is especially insidious: `delete[]` does not change the value of the pointer variable and does not necessarily clear the memory right away, so reading `a[0]` immediately afterward often still returns the old value and the program "appears to work", until the memory is reallocated to another object.

There are three layers of defense:

1. Avoid the problem at the root with the modern approach: containers, `std::string`, and smart pointers manage memory, and `std::span` or references replace "pointer + length"; using `.at(i)` instead of `[i]` throws an exception on out-of-bounds access.
2. Let the compiler help: turn on warnings (`-Wall -Wextra`) and initialize pointers at declaration (use `nullptr` when there is no object to point to).
3. Detect with tools: compile with `-fsanitize=address,undefined` (AddressSanitizer and UBSan, supported by both GCC and Clang; MSVC supports the former), and the program reports the offending line and the history of the memory at the moment an out-of-bounds access, use after free, or leak occurs; Valgrind on Linux can also check without recompiling. The memory window of a **debugger** lets us inspect the contents at an address directly ([4.1.5](/4.1.5)).

```bash
g++ -std=c++20 -g -fsanitize=address,undefined main.cpp && ./a.out
```

## 8.5. Python Comparison

Python has no pointers or address arithmetic, but its variable model can be understood through pointers: a Python variable is a name, and a name refers to an object. The assignment `b = a` does not copy the object; it only makes the name `b` refer to the same object that `a` refers to, which amounts to copying a pointer. `id(x)` returns the identity of an object (in CPython, the object's address), and `a is b` tests whether two names refer to the same object.

Whether this is "visible" depends on whether the object is mutable. Integers, floats, strings, and tuples are immutable: any "modification" creates a new object and makes the name refer to it, so sharing causes no surprises. Lists, dictionaries, and sets are mutable: a modification made through one name is seen through the other.

```python
a = [1, 2, 3]
b = a            # b and a refer to the same list
b.append(4)
print(a, a is b)  # [1, 2, 3, 4] True

s = "abc"
t = s
t += "d"         # creates a new string; s is unchanged
print(s, t)      # abc abcd

grid = [[0] * 3] * 3      # three references to ONE row
grid[0][0] = 1
print(grid)               # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
grid = [[0] * 3 for _ in range(3)]  # three distinct rows
```

The last example is one of the most common Python mistakes among beginners, and its cause is exactly the same as two pointers pointing to the same block of memory in C++. Function arguments are passed in the same way: the function receives a reference to the object, so modifying a mutable argument inside the function affects the caller, whereas rebinding the parameter name does not ([4.1.4](/4.1.4)). When an independent copy is needed, use `list(a)`, `a.copy()`, or `copy.deepcopy(a)` ([4.2.6](/4.2.6)).

A Python list is stored in memory as a contiguous "array of references", each element being a pointer to some object. This is why one list can hold objects of different types, but also why numeric data are not as compact as in a C++ array; large-scale numerical computation uses NumPy's contiguous arrays ([4.4.2](/4.4.2)).

Python programmers do not need to free memory; this is done by *garbage collection*, in which the runtime system automatically finds objects that the program can no longer reach and reclaims their memory. The main mechanism of CPython is reference counting: each object records how many references point to it and is reclaimed immediately when the count drops to 0. In addition, a cycle collector runs periodically to handle groups of objects that refer to one another so that their counts never reach 0. Hence dangling pointers and double frees do not occur in Python; but if a long-lived container (such as a global cache dictionary) keeps holding objects that are no longer needed, memory still grows steadily, which is a "memory leak" in garbage-collected languages.

## Summary

| Concept | C++ | Python |
|---|---|---|
| Indirect access | pointer `T*`, `&` takes the address, `*` dereferences | names refer to objects; assignment shares the reference |
| Arrays and addresses | stored contiguously, `a[i] == *(a + i)` | a list is a contiguous array of references |
| Requesting memory at run time | `new` / `delete`; containers and smart pointers recommended | creating an object allocates |
| Release | the programmer's responsibility (automated by RAII) | garbage collection |
| Typical errors | out-of-bounds access, dangling pointers, leaks, double free | accidental sharing of mutable objects, containers holding unneeded objects |
