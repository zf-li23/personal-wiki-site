---
title: "NumPy: Arrays and Vectorization"
description: Why Python lists are unsuitable for numerical data; the ndarray and its dtype; type promotion in NumPy 2; memory layout, strides and contiguity; basic indexing and views; fancy and boolean indexing; universal functions, reductions and pairwise summation; broadcasting; thinking in whole arrays; NumPy and other array libraries (array API standard, DLPack).
---

NumPy is the foundation of the scientific Python stack ([4.4.1](/4.4.1#sec-1.1.2)): it provides one data structure, the n-dimensional array, together with fast operations on whole arrays. Everything else in the ecosystem, from SciPy to pandas and scikit-learn, exchanges data as NumPy arrays. This chapter explains what an array is in memory, because almost every surprise in NumPy (an assignment that changes another variable, an operation that is unexpectedly slow, an integer that silently overflows) follows from the memory model. We then study the operations that make NumPy fast: universal functions, reductions and broadcasting, and the style of programming they support, called **vectorization**. The chapter continues the discussion of memory layout from [4.1.8](/4.1.8#sec-8.2.3) and of Python's reference semantics from [4.1.8](/4.1.8#sec-8.5). Linear algebra and random numbers follow in [4.4.3](/4.4.3). The examples use NumPy 2.5 (October 2026); everything except a few noted details also holds for NumPy 2.0 and later.

## 2.1. Why NumPy

A Python list of numbers is an **array** of references, each pointing to a separate float object somewhere on the heap ([4.1.8](/4.1.8#sec-8.5)). Each float object stores, besides its 8-byte value, a reference count and a **pointer** to its type, so it occupies 24 bytes, and the list adds an 8-byte pointer per element:

```python
import sys
import numpy as np

n = 1_000_000
lst = [float(i) for i in range(n)]
arr = np.arange(n, dtype=np.float64)
print(sys.getsizeof(lst) + sum(sys.getsizeof(v) for v in lst))  # 32448728 bytes
print(arr.nbytes)                                                # 8000000 bytes
```

The NumPy array stores the same numbers as one contiguous block of raw 8-byte values, four times smaller. More importantly, because all elements have the same type and lie next to each other, an operation on the whole array can run as one compiled loop: no type checks per element, no object allocation, sequential memory access that the CPU cache and SIMD instructions handle well. Computing $\sum_i x_i^2$ for $10^6$ numbers on the test machine takes about 20 ms with a Python `for` loop over the list and about 1 ms with `(arr * arr).sum()`; a systematic comparison follows in [4.4.3](/4.4.3#sec-3.5).

The price is flexibility: an array has a fixed size and a single element type. NumPy is therefore the right container for homogeneous numerical data (vectors, matrices, images, time series, grids), and Python lists remain the right container for small heterogeneous collections that grow ([4.2.10](/4.2.10)).

## 2.2. The ndarray

### 2.2.1. Creating Arrays

**Definition 2.2.1 (ndarray)** An **ndarray** (n-dimensional array) is a fixed-size, multidimensional container of elements of one type. It consists of a block of memory, the *data buffer*, and metadata describing how to interpret it: the element type (dtype), the *shape*, a tuple giving the length along each dimension, and the strides (§2.3). The dimensions are called *axes* and numbered $0, 1, \dots, d - 1$; $d$ is the number of dimensions `ndim`.

The most common ways to create arrays are:

| Function | Result |
|---|---|
| `np.array([[1, 2], [3, 4]])` | from nested sequences; the dtype is inferred |
| `np.zeros((m, n))`, `np.ones(...)`, `np.full(shape, v)` | filled with 0, 1 or `v` (float64 by default) |
| `np.empty((m, n))` | uninitialized memory: fastest, but the values are garbage until written |
| `np.arange(start, stop, step)` | evenly spaced values, `stop` excluded (like `range`) |
| `np.linspace(a, b, n)` | `n` evenly spaced values from `a` to `b` inclusive |
| `np.eye(n)`, `np.diag(v)` | identity matrix, diagonal matrix |
| `np.zeros_like(a)`, `np.empty_like(a)` | same shape and dtype as `a` |
| `np.loadtxt`, `np.genfromtxt`, `np.load` | from text files or NumPy's binary `.npy` format |

For a floating-point range, `np.linspace` is preferable to `np.arange`: with a fractional step, rounding can make `np.arange` include or exclude the end point unexpectedly, whereas `linspace` fixes the number of points.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim, a.shape, a.size, a.dtype, a.itemsize, a.nbytes)  # 2 (2, 3) 6 int64 8 48
print(np.arange(0, 1, 0.25))   # [0.   0.25 0.5  0.75]
print(np.linspace(0, 1, 5))    # [0.   0.25 0.5  0.75 1.  ]
```

### 2.2.2. Axes

Many functions take an `axis` argument that names the axis along which they operate; that axis disappears from the result. For a matrix, `axis=0` runs down the rows and gives one value per column, `axis=1` runs along each row:

```python
print(a.sum(axis=0))   # [5 7 9]   column sums
print(a.sum(axis=1))   # [ 6 15]   row sums
print(a.sum())         # 21        all elements
print(a.sum(axis=1, keepdims=True).shape)   # (2, 1): the axis is kept with length 1
```

`keepdims=True` keeps the reduced axis with length 1, so that the result can be combined with the original array by broadcasting (§2.6). A useful convention in data analysis is to store observations along axis 0 and variables along axis 1, so that a **data matrix** with $n$ observations of $p$ variables has shape `(n, p)`, as in statistics texts.

### 2.2.3. The dtype

**Definition 2.2.2 (dtype)** The **dtype** (data type) of an array describes how each element is stored: its kind (boolean, signed or unsigned integer, floating-point, complex, string, or Python object), its size in bytes, and its byte order.

| dtype | Size | Range or precision | Notes |
|---|---|---|---|
| `bool` | 1 byte | `True`, `False` | result of comparisons |
| `int8`, `int16`, `int32`, `int64` | 1–8 bytes | $-2^{k-1}$ to $2^{k-1} - 1$ | `int64` is the default integer on 64-bit Linux, macOS and (since NumPy 2) Windows |
| `uint8`, ..., `uint64` | 1–8 bytes | $0$ to $2^k - 1$ | `uint8` for image pixels |
| `float32` | 4 bytes | about 7 significant digits | single precision, GPUs, machine learning |
| `float64` | 8 bytes | about 16 significant digits | the default; IEEE 754 double precision |
| `complex128` | 16 bytes | two `float64` | |
| `StringDType()`, `<U10` | variable / fixed | | text; `<U10` holds at most 10 characters |
| `object` | 8 bytes | references to Python objects | loses all speed advantages |

The integer types of NumPy are the fixed-width integers of C, not Python's unbounded integers ([4.1.2](/4.1.2#sec-2.2.2)), so arithmetic on arrays wraps around silently on **integer overflow**:

```python
x = np.array([100, 120], dtype=np.int8)
print(x + x)                              # [-56 -16], no warning
print(np.iinfo(np.int8).max)              # 127
print(np.finfo(np.float32).eps, np.finfo(np.float64).eps)   # 1.1920929e-07 2.220446049250313e-16
```

`np.finfo` reports the **machine epsilon** and the range of a floating-point type ([3.5.1](/3.5.1#sec-1.2.5)). **Overflow** is a real danger in practice: an image stored as `uint8` wraps around when two pixel values are added, and products of large `int32` counts overflow quickly. Converting with `a.astype(np.float64)` before arithmetic avoids both.

When an operation combines arrays of different dtypes, NumPy chooses the result dtype by *type promotion*: the smallest type that can represent both operands, so `int8 + int16` gives `int16` and `int64 + float64` gives `float64`. NumPy 2 changed the rule for Python scalars (NEP 50). A Python `int`, `float` or `complex` is now "weak": it adopts the dtype of the array it is combined with instead of influencing the result type by its value.

```python
print(np.array([1, 2], dtype=np.float32) * 2.5)   # [2.5 5. ], still float32
print((np.array([1, 2], dtype=np.int8) + 1).dtype)  # int8
np.array([1, 2], dtype=np.int8) + 1000
# OverflowError: Python integer 1000 out of bounds for int8
print(np.float32(0.1) + 0.2)                       # 0.3, a float32
print(np.array([1, 2, 3]) / 2)                     # [0.5 1.  1.5]: true division gives float64
```

The rule makes results predictable, at the cost that `float32` data stay in **single precision** when combined with Python floats. When accuracy matters, convert explicitly.

## 2.3. Memory Layout and Strides

### 2.3.1. Strides

An array has a shape, but memory is one-dimensional. The connection is made by the strides.

**Definition 2.3.1 (Stride)** The **strides** of an array are a tuple $(s_0, \dots, s_{d-1})$ of integers: $s_k$ is the number of bytes by which the memory address advances when the index along axis $k$ increases by one. The element with index $(i_0, \dots, i_{d-1})$ is stored at byte offset

$$
i_0 s_0 + i_1 s_1 + \cdots + i_{d-1} s_{d-1}
$$
from the start of the array.

A $3 \times 4$ array of `float64` created by NumPy is stored in **row-major order** (called *C order*, as in C and C++, [4.1.8](/4.1.8#sec-8.2.3)): consecutive elements of a row are adjacent, so the strides are `(32, 8)`, 32 bytes to the next row and 8 bytes to the next column. Fortran, MATLAB, R and Julia store matrices in *column-major order* (*Fortran order*), with strides `(8, 24)` for the same shape. NumPy supports both, and the strides make many operations free: they change only the metadata, never the data buffer.

```python
b = np.arange(12, dtype=np.float64).reshape(3, 4)
print(b.strides)                    # (32, 8)
print(b.T.strides)                  # (8, 32): transposing swaps the strides
print(b[:, ::2].strides)            # (32, 16): every other column
print(b[::2].strides)               # (64, 8): every other row
print(np.asfortranarray(b).strides) # (8, 24): a copy in column-major order
```

The same idea in C++ is a *strided view*: a pointer to existing data plus a shape and strides, through which the data can be read in different patterns without being copied. C++23 standardizes it as `std::mdspan`. A minimal version shows that NumPy's transposition and slicing are nothing more than arithmetic on the strides:

```cpp tab
#include <cstddef>
#include <iostream>
#include <numeric>
#include <vector>

// A minimal 2-D strided view: a pointer to the data plus shape and strides
// (measured in elements here; NumPy measures strides in bytes).
struct View2D {
    double* data;
    std::ptrdiff_t shape[2];
    std::ptrdiff_t strides[2];
    double& operator()(std::ptrdiff_t i, std::ptrdiff_t j) const {
        return data[i * strides[0] + j * strides[1]];
    }
    View2D transposed() const {
        return {data, {shape[1], shape[0]}, {strides[1], strides[0]}};
    }
};

int main() {
    std::vector<double> buf(12);
    std::iota(buf.begin(), buf.end(), 0.0);  // 0, 1, ..., 11
    View2D a{buf.data(), {3, 4}, {4, 1}};    // 3 x 4, row-major
    View2D t = a.transposed();                // 4 x 3, no data copied
    View2D every_other{buf.data(), {3, 2}, {4, 2}};  // a[:, ::2]
    t(1, 2) = -1.0;                           // writes buf[2 * 4 + 1]
    std::cout << a(2, 1) << ' ' << every_other(1, 1) << '\n';  // -1 6
}
```

```python tab
import numpy as np

a = np.arange(12.0).reshape(3, 4)   # 3 x 4, row-major
t = a.T                             # 4 x 3, no data copied
t[1, 2] = -1.0                      # writes the element a[2, 1]
print(a[2, 1], a[:, ::2][1, 1])     # -1.0 6.0
print(a.strides, t.strides, a[:, ::2].strides)  # (32, 8) (8, 32) (32, 16)
```

### 2.3.2. Contiguity and Performance

An array is *C-contiguous* if its elements occupy one block of memory in **row-major order**, and *F-contiguous* if they do so in column-major order; `a.flags` reports both. `b` above is C-contiguous, `b.T` is F-contiguous, and `b[:, ::2]` is neither.

Strides do not change the number of operations, but they change the speed. Memory is transferred to the CPU cache in lines of 64 bytes; traversing an array along its last axis (in C order) uses every byte of each line, while traversing along the first axis uses 8 bytes of each line and jumps elsewhere. On the test machine, with a $4000 \times 4000$ `float64` array (128 MB):

| Operation | Time |
|---|---|
| sum each row, `[a[i, :].sum() for i in range(4000)]` | 20 ms |
| sum each column, `[a[:, j].sum() for j in range(4000)]` | 168 ms |
| `a.copy()` | 43 ms |
| `np.ascontiguousarray(a.T)` (transpose and copy) | 220 ms |

Whole-array reductions such as `a.sum(axis=0)` are written to traverse memory efficiently whatever the axis, so the effect matters mainly when we loop over slices ourselves or pass arrays to compiled code that expects a particular layout. Some libraries (and C or Fortran routines called through them) require contiguous input and copy silently otherwise; `np.ascontiguousarray` makes the copy explicit.

## 2.4. Indexing, Views and Copies

### 2.4.1. Basic Indexing and Slicing

A multidimensional array is indexed with one index per axis, separated by commas: `m[i, j]`, not `m[i][j]` (which works but creates an intermediate array). Each index can be an integer, which removes that axis, or a slice `start:stop:step`, which keeps it. Negative indices count from the end, `...` (Ellipsis) stands for as many full slices as needed, and `np.newaxis` (equal to `None`) inserts a new axis of length 1:

```python
m = np.arange(12).reshape(3, 4)
print(m[1, 2])        # 6
print(m[1])           # [4 5 6 7]     row 1 (same as m[1, :])
print(m[:, 1])        # [1 5 9]       column 1, as a 1-D array
print(m[-1, ::-1])    # [11 10  9  8] last row reversed
print(m[..., 0])      # [0 4 8]       first entry along the last axis
print(m[:, None].shape)   # (3, 1, 4)
```

Note that `m[:, 1]` is a 1-D array of shape `(3,)`, not a column of shape `(3, 1)`; a 1-D array is neither a row nor a column vector. To keep the column shape, write `m[:, 1:2]` or `m[:, [1]]`.

### 2.4.2. Views

**Definition 2.4.1 (View)** A **view** of an array is another array object that shares its data buffer, with its own shape, strides and offset. Writing to a view changes the original array, and vice versa. The array that owns the buffer is available as the attribute `base` of the view.

Basic slicing, transposition, `reshape` (when possible) and `np.newaxis` return views, because each can be expressed by new strides and an offset (§2.3). This is the opposite of Python lists, where slicing creates a **shallow copy**:

```python
a = np.arange(10)
s = a[2:8:2]          # a view: elements 2, 4, 6
s[0] = -1
print(a)              # [ 0  1 -1  3  4  5  6  7  8  9]
print(s.base is a, np.shares_memory(a, s))   # True True

lst = list(range(5))
t = lst[1:3]          # a new list
t[0] = 99
print(lst)            # [0, 1, 2, 3, 4], unchanged
```

Views make slicing cheap (no data is copied, whatever the size) and allow in-place updates of parts of an array, such as `img[100:200, 50:150] = 0`. They are also the most common source of bugs: a function that receives a slice and modifies it modifies the caller's data. When an independent array is needed, we copy explicitly with `.copy()`. Whether an operation returns a view or a copy can be checked with `np.shares_memory`:

```python
m = np.arange(12).reshape(3, 4)
print(np.shares_memory(m, m.reshape(4, 3)))     # True: reshaping a contiguous array
print(np.shares_memory(m, m.T.reshape(12)))     # False: m.T is not contiguous, so reshape copies
print(np.shares_memory(m, m[:, 1:3].copy()))    # False
```

`np.asarray(x)` returns `x` itself if it is already an array of the requested dtype and copies only when necessary, which is what functions accepting "array-like" input should use. Since NumPy 2, `np.array(x, copy=False)` means "never copy" and raises a `ValueError` when a copy cannot be avoided; code written for NumPy 1, where it meant "copy only if needed", should use `np.asarray` instead.

### 2.4.3. Fancy and Boolean Indexing

Indexing with an integer array or a list, or with a boolean array, is called advanced indexing.

**Definition 2.4.2 (Fancy Indexing)** **Fancy indexing** (integer array indexing) selects elements by an array of indices: `x[idx]` is the array with elements `x[idx[k]]`. *Boolean indexing* `x[mask]`, with a boolean array `mask` of the same shape as `x`, selects the elements where `mask` is `True`, as a 1-D array. Both always return a copy.

```python
x = np.array([10, 20, 30, 40, 50])
y = x[np.array([4, 0, 0])]     # indices may repeat and appear in any order
y[0] = 0
print(x, y)                    # [10 20 30 40 50] [ 0 10 10]: y is a copy
mask = x > 25
print(mask, x[mask])           # [False False  True  True  True] [30 40 50]
x[x > 25] = 0                  # assignment through an index works in place
print(x)                       # [10 20  0  0  0]
```

The result of an advanced index is a copy, but *assigning* to an advanced index (`x[mask] = 0`) writes into `x`. A consequence is the classic chained-indexing bug: `x[[1, 3]][0] = -5` first makes a copy with `x[[1, 3]]` and then modifies the copy, so `x` is unchanged. Write a single indexing expression instead, such as `x[1] = -5`.

With several integer arrays, the arrays are paired elementwise, not combined as a grid: `m[[0, 2], [1, 3]]` gives the two elements `m[0, 1]` and `m[2, 3]`. The submatrix of rows 0, 2 and columns 1, 3 is `m[np.ix_([0, 2], [1, 3])]`. The function `np.nonzero(mask)` returns the index arrays of the `True` entries, and `np.where(cond, a, b)` chooses elementwise between two arrays:

```python
print(m[[0, 2], [1, 3]])                 # [ 1 11]
print(m[np.ix_([0, 2], [1, 3])])         # [[ 1  3]
                                         #  [ 9 11]]
print(np.where(m > 5, m, 0))             # entries <= 5 replaced by 0
```

The following table summarizes when we get a view:

| Operation | View or copy |
|---|---|
| `a[2:8]`, `a[:, 1]`, `a[::2, ::-1]`, `a[..., None]` | view |
| `a.T`, `a.transpose(...)`, `a.swapaxes(...)` | view |
| `a.reshape(...)`, `a.ravel()` | view if the layout allows, otherwise copy |
| `a[[1, 3]]`, `a[a > 0]` | copy |
| `a.flatten()`, `a.copy()`, `a.astype(...)` | copy |
| arithmetic `a + 1`, `np.sin(a)` | new array |

## 2.5. Universal Functions

### 2.5.1. Elementwise Operations

**Definition 2.5.1 (Universal Function)** A **universal function** (ufunc) is a function that operates on arrays element by element, implemented as a compiled loop for each supported combination of dtypes. It supports broadcasting (§2.6), type promotion, an `out` argument for writing the result into an existing array, and a `where` argument for computing only selected elements.

The arithmetic operators on arrays are ufuncs: `a + b` calls `np.add(a, b)`, `a * b` calls `np.multiply`, `a < b` calls `np.less`, and so on. NumPy has about a hundred ufuncs (counting aliases) for arithmetic (`add`, `subtract`, `multiply`, `divide`, `floor_divide`, `power`, `mod`), comparisons, logic (`logical_and`, `logical_not`), and mathematical functions (`exp`, `log`, `log1p`, `expm1`, `sqrt`, `sin`, `arctan2`, `hypot`, `abs`, `maximum`, `isnan`, `isfinite`). The functions `log1p` and `expm1` compute $\log(1 + x)$ and $\mathrm{e}^x - 1$ accurately for small $x$, avoiding **catastrophic cancellation** ([3.5.1](/3.5.1#sec-1.3.3)).

```python
print(np.add(1, [1, 2]))                      # [2 3]
out = np.empty(3)
np.exp([0, 1, 2], out=out)                    # no new array is allocated
print(out)                                    # [1.         2.71828183 7.3890561 ]
print(isinstance(np.sin, np.ufunc), np.add.nin)   # True 2
```

Floating-point exceptions do not raise errors. Division by zero gives `inf` or `nan` (**NaN**) with a `RuntimeWarning`, following IEEE 754; the **context manager** `np.errstate` changes this behavior locally, for example to silence the warning or to raise an exception:

```python
with np.errstate(divide="ignore", invalid="ignore"):
    print(np.array([1.0, 0.0, -1.0]) / 0.0)   # [ inf  nan -inf]
with np.errstate(all="raise"):
    np.log(np.array([0.0]))                   # FloatingPointError: divide by zero encountered in log
```

### 2.5.2. Reductions and Accumulations

Binary ufuncs have methods that apply the operation repeatedly:

| Method | Example | Result |
|---|---|---|
| `reduce` | `np.add.reduce([1, 2, 3, 4])` | `10` (same as `np.sum`) |
| `accumulate` | `np.add.accumulate([1, 2, 3, 4])` | `[1 3 6 10]` (same as `np.cumsum`) |
| `outer` | `np.multiply.outer([1, 2, 3], [1, 10])` | the $3 \times 2$ table of products |
| `at` | `np.add.at(c, idx, 1)` | unbuffered in-place operation, correct for repeated indices |

The common reductions have their own functions and methods: `sum`, `prod`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `any`, `all`, `cumsum`, all with an `axis` argument. Note that `np.std` and `np.var` divide by $n$ by default; the unbiased **sample variance** with divisor $n - 1$ needs `ddof=1`. Functions such as `np.nanmean` and `np.nansum` ignore `nan` entries.

The method `at` solves a subtle problem. In `c[idx] += 1`, NumPy evaluates `c[idx] + 1` first and then assigns, so an index that appears several times in `idx` is incremented only once:

```python
idx = np.array([0, 1, 1, 2, 1])
c = np.zeros(3, dtype=int); c[idx] += 1;          print(c)   # [1 1 1]
c = np.zeros(3, dtype=int); np.add.at(c, idx, 1); print(c)   # [1 3 1]
print(np.bincount(idx))                                       # [1 3 1]
```

For counting, `np.bincount` is the fastest solution; `np.add.at` is the general one (for example for assembling a matrix from element contributions).

Summation of **floating-point numbers** is not exact, and the order matters ([3.5.1](/3.5.1#sec-1.3.3)). A naive loop accumulates a **rounding error** that can grow proportionally to $n\varepsilon$. `np.sum` on floating-point data uses *pairwise summation*: it splits the array into halves recursively (with small blocks summed directly), which reduces the error bound to order $\varepsilon \log n$ at no extra cost. For the rare cases that need a correctly rounded sum, the standard library provides `math.fsum`.

## 2.6. Broadcasting

### 2.6.1. The Broadcasting Rule

Arithmetic between an array and a scalar, `a * 2.5`, multiplies every element. Broadcasting generalizes this to arrays of different shapes.

**Definition 2.6.1 (Broadcasting)** **Broadcasting** is the rule by which NumPy combines arrays of different shapes in an elementwise operation. The shapes are compared from the last axis backwards, after padding the shorter shape with 1s on the left; two lengths are compatible if they are equal or one of them is 1. The result has, along each axis, the larger of the two lengths, and an operand of length 1 along an axis is used repeatedly along it. If some pair of lengths is incompatible, the operation fails.

| Shape of `a` | Shape of `b` | Shape of `a + b` |
|---|---|---|
| `(3, 4)` | `()` (scalar) | `(3, 4)` |
| `(3, 4)` | `(4,)` | `(3, 4)`: `b` is added to every row |
| `(3, 4)` | `(3, 1)` | `(3, 4)`: `b` is added to every column |
| `(3,)` | `(4, 1)` | `(4, 3)`: an outer sum |
| `(8, 1, 6, 1)` | `(7, 1, 5)` | `(8, 7, 6, 5)` |
| `(3, 2)` | `(3,)` | error: 2 and 3 are incompatible |

Broadcasting does not copy the repeated operand: internally it is a view with stride 0 along the broadcast axes. `np.broadcast_to(np.arange(3), (4, 3))` has strides `(0, 8)` and is read-only, since its 12 entries share 3 memory locations.

```python
x = np.arange(3)                 # shape (3,)
y = np.arange(4).reshape(4, 1)   # shape (4, 1)
print(x + y)                     # shape (4, 3): entry (i, j) is y[i] + x[j]
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]]
np.ones((3, 2)) + np.ones(3)
# ValueError: operands could not be broadcast together with shapes (3,2) (3,)
print((np.ones((3, 2)) + np.ones(3)[:, None]).shape)   # (3, 2)
```

The last example shows the typical fix: to combine a vector of length 3 with the rows of a $3 \times 2$ array, we make it a column with `[:, None]`, so that the trailing axes align.

### 2.6.2. Examples

*Standardizing the columns of a data matrix.* With observations along axis 0, `X.mean(axis=0)` has shape `(p,)` and broadcasts against `X` of shape `(n, p)`:

```python
X = np.array([[1.0, 2.0], [3.0, 6.0], [5.0, 10.0]])
Z = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
print(Z)
# [[-1. -1.]
#  [ 0.  0.]
#  [ 1.  1.]]
```

Standardizing the rows instead needs `keepdims=True` (or `[:, None]`), so that the row statistics have shape `(n, 1)`.

*Pairwise distances.* For points $p_1, \dots, p_m$ and $q_1, \dots, q_k$ in $\mathbb{R}^d$, stored as arrays `P` of shape `(m, d)` and `Q` of shape `(k, d)`, inserting axes gives shapes `(m, 1, d)` and `(1, k, d)`, whose difference has shape `(m, k, d)`:

```python
rng = np.random.default_rng(0)
P, Q = rng.random((5, 2)), rng.random((3, 2))
D = np.sqrt(((P[:, None, :] - Q[None, :, :]) ** 2).sum(axis=-1))
print(D.shape)     # (5, 3): D[i, j] is the distance from P[i] to Q[j]
```

The intermediate array has $m k d$ elements. For $m = k = 10^4$ and $d = 3$ that is 2.4 GB, so for large problems a specialized function such as `scipy.spatial.distance.cdist` or a loop over blocks is preferable. Broadcasting trades memory for speed; it is not free.

*Evaluating a function on a grid.* `x[None, :]` and `y[:, None]` broadcast to a 2-D grid, which replaces `np.meshgrid` in most cases. The following figure is computed this way: the **complex numbers** $c$ of a grid are iterated by $z \mapsto z^2 + c$, and a boolean array keeps track of the points that have not yet escaped, so that the whole picture is computed with one Python loop over 60 iterations instead of a loop over 648 000 pixels.

![The Mandelbrot set computed with broadcasting and boolean masks: the color of a point c is the number of iterations of z -> z^2 + c (starting at z = 0) until |z| > 2](./plots/mandelbrot.py)

## 2.7. Vectorization

The examples above share a style: instead of writing a loop over elements, we express the computation as a few operations on whole arrays. This is **vectorization** in the sense of [3.5.2](/3.5.2), where the same idea appears in R. In NumPy it means: replace Python loops by ufuncs, reductions, broadcasting and indexing, so that the loops run in compiled code. Thinking in arrays takes practice; a few patterns cover most cases:

| Loop pattern | Vectorized form |
|---|---|
| `for i: y[i] = f(x[i])` with arithmetic | arithmetic on arrays, ufuncs |
| `if` inside the loop | `np.where(cond, a, b)`, boolean indexing, `np.clip` |
| accumulating a sum, maximum, count | `sum`, `max`, `np.count_nonzero`, with `axis` |
| running totals | `cumsum`, `cumprod`, `np.maximum.accumulate` |
| nested loops over pairs | broadcasting with `None` |
| histogram, counting by category | `np.bincount`, `np.histogram`, `np.unique(..., return_counts=True)` |
| searching in sorted data | `np.searchsorted` |

*Example: random walks.* We simulate 1000 symmetric random walks of 1000 steps and want the final positions. The loop version draws one step at a time:

```python
import random


def walks_loop(n_walkers, n_steps, seed=0):
    rnd = random.Random(seed)
    finals = []
    for _ in range(n_walkers):
        pos = 0
        for _ in range(n_steps):
            pos += 1 if rnd.random() < 0.5 else -1
        finals.append(pos)
    return finals


def walks_numpy(n_walkers, n_steps, seed=0):
    rng = np.random.default_rng(seed)
    steps = 2 * rng.integers(0, 2, size=(n_walkers, n_steps), dtype=np.int8) - 1
    paths = steps.cumsum(axis=1, dtype=np.int64)   # position after each step
    return paths[:, -1]
```

On the test machine the loop takes 66 ms and the NumPy version 12 ms. The vectorized version computes all $10^6$ positions, which we need if we want to plot the paths; if we only need the final positions, `steps.sum(axis=1, dtype=np.int64)` instead of `cumsum` takes 6 ms. Better still, a little probability removes the simulation of steps altogether: the number of up-steps is binomial, so `2 * rng.binomial(n_steps, 0.5, size=n_walkers) - n_steps` produces the final positions with the right distribution in 0.05 ms. The general lesson: vectorization speeds up a given algorithm by a constant factor, but thinking about what is actually needed can do far better.

*When vectorization does not apply.* A recurrence in which each step depends on the previous one, such as the logistic map $x_{n+1} = r x_n (1 - x_n)$, cannot be vectorized along time. It can often be vectorized across independent runs instead: iterating an array of parameter values at once keeps one Python loop over time and moves the loop over parameters into NumPy.

```python
def logistic_orbits(r, n_iter=1000, x0=0.2):
    x = np.full_like(r, x0)
    for _ in range(n_iter):          # sequential in time ...
        x = r * x * (1 - x)          # ... vectorized over all values of r
    return x


print(logistic_orbits(np.linspace(2.8, 4.0, 5)).round(4))
# [0.6429 0.7646 0.8422 0.7975 0.1382]
```

When neither works, or when vectorization would need huge temporary arrays, the loop should be compiled instead, for example with Numba ([4.4.7](/4.4.7)).

The function `np.vectorize` is not a way to vectorize. It wraps a Python function so that it accepts arrays and broadcasts, but internally it still calls the Python function once per element. For a piecewise function on $10^6$ elements, `np.vectorize(lambda v: v * v if v > 0 else 0.0)` takes 160 ms on the test machine, slower than a plain Python loop over a list (76 ms), while `np.where(x > 0, x * x, 0.0)` takes 13 ms. It is a convenience for code that does not need speed.

## 2.8. NumPy and Other Array Libraries

NumPy arrays live in main memory and are processed by the CPU. Deep learning frameworks such as PyTorch, JAX and TensorFlow, and GPU array libraries such as CuPy, provide their own array types that can live on GPUs, record operations for automatic differentiation, or be compiled just in time; how they are used is the subject of [4.7](/4.7). They all imitate the NumPy interface, so knowledge of NumPy transfers directly. Two standards connect them:

- The *Python array API standard*, published by the Consortium for Python Data API Standards, specifies a common set of functions, their signatures and semantics (creation, elementwise functions, reductions, linear algebra, indexing). An array of a conforming library returns its namespace through `x.__array_namespace__()`, so a function can be written once and work with any of them: `xp = x.__array_namespace__()` and then `xp.exp(x)`, `xp.sum(x)`. Since NumPy 2.0 the main `numpy` namespace conforms to the standard (NumPy 2.5 reports `np.__array_api_version__ == "2025.12"`); for libraries that do not fully conform yet, the package `array-api-compat` provides wrappers. SciPy and scikit-learn use this mechanism to accept PyTorch or CuPy arrays in parts of their APIs, still as an experimental, opt-in feature.
- *DLPack* is a protocol for exchanging arrays between libraries without copying: an array exposes its data pointer, shape, strides, dtype and device through the methods `__dlpack__` and `__dlpack_device__`, and `np.from_dlpack(x)`, `torch.from_dlpack(x)` or `jax.numpy.from_dlpack(x)` wrap the same memory. Only arrays on the same device can share memory; a GPU tensor must first be copied to the CPU.

```python
a = np.arange(4.0)
print(a.__array_namespace__().__name__, np.__array_api_version__)   # numpy 2025.12
b = np.from_dlpack(a)        # zero-copy: b shares memory with a
b[0] = 9.0
print(a, np.shares_memory(a, b))   # [9. 1. 2. 3.] True
```

PyTorch also offers `torch.from_numpy(a)` and `t.numpy()`, which share memory between a NumPy array and a CPU tensor in the same way. Sharing has the same consequences as a view (§2.4.2): modifying one modifies the other. One difference in semantics deserves mention: JAX arrays are immutable, so instead of `x[i] = v` one writes `x = x.at[i].set(v)`, which returns a new array.

## Summary

- An ndarray is a typed data buffer plus metadata: dtype, shape and strides. All elements have one dtype; integers have fixed width and wrap around on overflow.
- In NumPy 2, Python scalars are "weak" in type promotion: they adopt the dtype of the array.
- The strides map an index to a byte offset. Transposition, slicing and broadcasting change only the strides, so they are free; traversal along the last axis of a C-order array is cache-friendly.
- Basic slicing returns views that share memory with the original; advanced (integer or boolean) indexing returns copies, but assignment through it writes in place. Use `.copy()` when an independent array is needed, and `np.shares_memory` to check.
- Ufuncs apply compiled elementwise loops; their methods `reduce`, `accumulate`, `outer` and `at` cover reductions and scatter operations. `np.sum` uses pairwise summation.
- Broadcasting aligns shapes from the right and stretches axes of length 1; insert axes with `None` to control it, and watch the size of intermediates.
- Vectorization moves loops from Python into compiled code. It cannot handle sequential dependencies along the loop, `np.vectorize` does not make code faster, and a better algorithm beats both.
- The array API standard and DLPack let NumPy code work with, and share memory with, GPU and deep learning array libraries.
