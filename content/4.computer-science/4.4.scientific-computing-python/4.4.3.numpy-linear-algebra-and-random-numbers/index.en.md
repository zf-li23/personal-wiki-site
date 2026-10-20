---
title: "NumPy: Linear Algebra and Random Numbers"
description: Matrix products with @, matmul, vecdot and stacked arrays; BLAS and LAPACK; numpy.linalg for linear systems, least squares, factorizations and eigenvalues; why not to invert matrices; einsum and contraction order; the Generator interface for random numbers, distribution parameterizations, seeds and parallel streams; Monte Carlo error; measuring loops against vectorized code.
---

This chapter covers the two parts of NumPy that scientific programs use most after basic array arithmetic: dense linear algebra and random number generation. In both cases NumPy is an interface to carefully engineered compiled code, the BLAS and LAPACK libraries for linear algebra and modern pseudorandom generators for random numbers, and the main skill is to call that code correctly: to choose the right function (solve rather than invert, `eigh` rather than `eig` for symmetric matrices), to respect the conventions of the interface (shapes, parameterizations of distributions, seeding), and to know what accuracy to expect. The theory behind the algorithms is not repeated here; it is in the statistical computing course: floating-point arithmetic and conditioning in [3.5.1](/3.5.1), numerical linear algebra in [3.5.3](/3.5.3), and random number generation in [3.5.8](/3.5.8). The chapter ends by measuring the speed difference between Python loops and vectorized code, which explains the programming style of [4.4.2](/4.4.2#sec-2.7). The examples use NumPy 2.5 (October 2026).

## 3.1. Matrix Products

### 3.1.1. The @ Operator

The operator `*` on arrays is elementwise multiplication. **Matrix multiplication** is written `@` (PEP 465), which calls `np.matmul`:

```python
import numpy as np

A = np.array([[1.0, 2.0], [3.0, 4.0]])
v = np.array([1.0, 1.0])
print(A @ A)        # [[ 7. 10.]  [15. 22.]]  matrix product
print(A * A)        # [[ 1.  4.]  [ 9. 16.]]  elementwise product
print(A @ v)        # [3. 7.]   matrix times vector
print(v @ A)        # [4. 6.]   vector times matrix
print(v @ v)        # 2.0       inner product
print(np.outer(v, v))   # [[1. 1.]  [1. 1.]]
```

A 1-D array is neither a row nor a column vector ([4.4.2](/4.4.2#sec-2.4.1)): in `A @ v` it is treated as a column, in `v @ A` as a row, and `v.T` is the same 1-D array. When the distinction matters, we use 2-D arrays of shape `(n, 1)` or `(1, n)`.

`matmul` also works on stacks of matrices: for arrays of shape `(..., m, k)` and `(..., k, n)`, it multiplies the matrices in the last two axes and broadcasts over the leading axes. This batch operation is common in statistics (one covariance matrix per group) and in machine learning. NumPy 2 added further functions in the same spirit:

| Function | Operation on the last axes | Shapes |
|---|---|---|
| `a @ b`, `np.matmul(a, b)` | matrix product | `(..., m, k) @ (..., k, n) -> (..., m, n)` |
| `np.vecdot(x, y)` | inner product of vectors (conjugating `x`) | `(..., n), (..., n) -> (...)` |
| `np.matvec(A, x)`, `np.vecmat(x, A)` | matrix–vector products | `(..., m, n), (..., n) -> (..., m)` |
| `a.mT`, `np.linalg.matrix_transpose(a)` | transpose of the last two axes | `(..., m, n) -> (..., n, m)` |
| `np.dot(a, b)` | older function; for 2-D arrays the matrix product, for higher dimensions a different (rarely wanted) rule | |

```python
S = np.arange(24.0).reshape(2, 3, 4)
T = np.ones((2, 4, 5))
print((S @ T).shape, S.mT.shape)                  # (2, 3, 5) (2, 4, 3)
print(np.vecdot(np.ones((3, 4)), np.arange(4.0))) # [6. 6. 6.]: one inner product per row
```

The class `np.matrix`, in which `*` meant matrix multiplication, is deprecated and should not be used; plain arrays with `@` replace it.

### 3.1.2. BLAS and LAPACK

NumPy does not implement matrix multiplication itself. It calls *BLAS* (Basic Linear Algebra Subprograms), a standard interface for vector and matrix operations defined in the 1970s and 1980s and implemented by optimized libraries for each processor family. BLAS is organized in three levels: Level 1 for vector operations (inner product, $y \leftarrow \alpha x + y$) with $O(n)$ work on $O(n)$ data, Level 2 for matrix–vector operations with $O(n^2)$ work, and Level 3 for matrix–matrix operations with $O(n^3)$ work on $O(n^2)$ data. Only Level 3 performs many operations per byte loaded from memory, so only Level 3 runs close to the peak speed of the processor; this is why algorithms in [3.5.3](/3.5.3#sec-3.1.1) are reorganized into blocks that use matrix–matrix products. *LAPACK* (Linear Algebra PACKage) builds on BLAS and provides factorizations, linear solvers, least squares and eigenvalue routines; `numpy.linalg` and `scipy.linalg` are wrappers around it.

The wheels of NumPy and SciPy on PyPI include OpenBLAS; conda-forge also offers Intel MKL, and on Apple processors NumPy can use Apple's Accelerate framework. `np.show_config()` shows which library is in use. These libraries are multithreaded, and the number of threads can be limited with environment variables such as `OPENBLAS_NUM_THREADS=1` or `OMP_NUM_THREADS=1`, or at run time with the package threadpoolctl. Limiting threads is necessary when we parallelize at a higher level ourselves, for example by running many processes ([4.4.7](/4.4.7)), because otherwise every process starts as many BLAS threads as there are cores.

The difference between a compiled, blocked, vectorized implementation and a naive one is large. On the test machine (a laptop with an 8-core Intel processor), the product of two $2000 \times 2000$ matrices takes $2n^3 = 1.6 \times 10^{10}$ floating-point operations (**flops**):

| Implementation | Time | Speed |
|---|---|---|
| triple loop in pure Python ($n = 200$, lists of floats) | 0.37 s | 0.04 GFLOP/s |
| `A @ B`, OpenBLAS, 1 thread | 0.81 s | 20 GFLOP/s |
| `A @ B`, OpenBLAS, 4 or 8 threads | 0.31 s | 52 GFLOP/s |

The pure Python loop is about 500 times slower than a single BLAS thread, and would need about 6 minutes for $n = 2000$. Threads, on the other hand, help only for large Level 3 operations: for Level 1 operations such as the inner product of two vectors of length $10^6$, starting threads costs more than it saves, and on the test machine the multithreaded `a @ a` was even slower than the single-threaded one.

## 3.2. numpy.linalg

### 3.2.1. Solving Linear Systems

To solve $A\boldsymbol{x} = \boldsymbol{b}$ we call `np.linalg.solve(A, b)`, which computes the **LU decomposition** with **partial pivoting** (LAPACK's `gesv`) and then solves two triangular systems ([3.5.3](/3.5.3#sec-3.1.3)). The tempting alternative `np.linalg.inv(A) @ b` should be avoided: it does about three times the work, and it is less accurate.

```python
from scipy.linalg import hilbert   # H[i, j] = 1 / (i + j + 1), a classic ill-conditioned matrix

for n in (6, 10, 13):
    H = hilbert(n)
    x_true = np.ones(n)
    b = H @ x_true
    x1 = np.linalg.solve(H, b)
    x2 = np.linalg.inv(H) @ b
    # condition number, relative errors, residual norms (see the table)
```

| $n$ | $\kappa_2(H)$ | error of `solve` | error of `inv` | residual $\Vert H\hat{\boldsymbol{x}} - \boldsymbol{b}\Vert$, `solve` | residual, `inv` |
|---|---|---|---|---|---|
| 6 | $1.5 \times 10^{7}$ | $1.4 \times 10^{-10}$ | $5.3 \times 10^{-10}$ | $5.2 \times 10^{-16}$ | $2.6 \times 10^{-10}$ |
| 10 | $1.6 \times 10^{13}$ | $8.7 \times 10^{-5}$ | $2.8 \times 10^{-3}$ | $5.7 \times 10^{-16}$ | $4.8 \times 10^{-5}$ |
| 13 | $1.5 \times 10^{18}$ | $3.6$ | $3.0 \times 10^{2}$ | $4.8 \times 10^{-16}$ | $5.2$ |

The table illustrates two lessons of [3.5.1](/3.5.1#sec-1.4.4). First, the relative error of the solution is roughly the **condition number** times the **machine epsilon**: for $n = 13$ no method in double precision can recover $\boldsymbol{x}$, and `np.linalg.cond(A)` tells us so in advance. Second, the residual of `solve` stays at the level of rounding errors even when the error is huge. This is **backward stability**: the computed solution is the exact solution of a nearby system. The explicit inverse loses this property, so its residuals and errors are larger. For a $2000 \times 2000$ system, `solve` took 0.39 s and `inv(A) @ b` 1.29 s on the test machine.

When the same matrix is used with many right-hand sides, we either pass them all at once as the columns of a matrix `B` (`np.linalg.solve(A, B)`), or factor once and reuse the factorization with `scipy.linalg.lu_factor` and `lu_solve` ([4.4.4](/4.4.4#sec-4.1)). For symmetric positive definite matrices, such as covariance matrices, the **Cholesky decomposition** is twice as fast as LU and numerically stable without pivoting (`scipy.linalg.cho_factor`, `cho_solve`).

### 3.2.2. Least Squares

For an overdetermined system $A\boldsymbol{\beta} \approx \boldsymbol{y}$ with $A \in \mathbb{R}^{n \times p}$, $n > p$, the **least squares** solution minimizes $\Vert \boldsymbol{y} - A\boldsymbol{\beta} \Vert_2$. `np.linalg.lstsq(A, y)` computes it from the **singular value decomposition** and returns the solution, the residual sum of squares, the numerical rank and the singular values. Forming the **normal equations** $A^{\mathsf T}A\boldsymbol{\beta} = A^{\mathsf T}\boldsymbol{y}$ instead squares the condition number ([3.5.3](/3.5.3#sec-3.2.8)). A polynomial fit of degree 12 on 50 equispaced points in $[0, 1]$ makes the difference visible:

```python
x = np.linspace(0, 1, 50)
A = np.vander(x, 13, increasing=True)       # columns 1, x, ..., x^12
beta_true = np.ones(13)
y = A @ beta_true                           # exact data, no noise
b_ls, rss, rank, sv = np.linalg.lstsq(A, y)
b_ne = np.linalg.solve(A.T @ A, A.T @ y)
print(f"{np.linalg.cond(A):.1e} {np.linalg.cond(A.T @ A):.1e}")  # 6.8e+08 1.0e+18
print(f"{np.abs(b_ls - beta_true).max():.1e}")                  # 1.9e-08
print(f"{np.abs(b_ne - beta_true).max():.1e}")                  # 1.6e+00
```

With noise-free data, `lstsq` recovers the coefficients to about 8 digits, as expected from $\kappa(A) \approx 7 \times 10^8$; the normal equations, with $\kappa(A^{\mathsf T}A) \approx 10^{18}$, do not recover a single digit. In practice, polynomial fitting should also avoid the monomial basis: `np.polynomial.Polynomial.fit(x, y, deg)` maps the data to the interval $[-1, 1]$ before fitting, which improves the conditioning considerably, and the `numpy.polynomial` package offers Chebyshev and Legendre bases. The older function `np.polyfit` is still available but is no longer recommended for new code.

### 3.2.3. Factorizations and Eigenvalues

The main functions of `numpy.linalg`, with the sections of [3.5.3](/3.5.3) that explain the algorithms:

| Task | Function | Notes |
|---|---|---|
| Cholesky $A = LL^{\mathsf T}$ | `cholesky(A)` | returns the lower factor $L$; raises `LinAlgError` if $A$ is not positive definite ([3.5.3](/3.5.3#sec-3.1.5)) |
| QR | `qr(A)` | reduced by default: $Q$ is $n \times p$ ([3.5.3](/3.5.3#sec-3.2.3)) |
| SVD $A = U\Sigma V^{\mathsf T}$ | `svd(A, full_matrices=False)` | returns $U$, the singular values as a 1-D array, and $V^{\mathsf T}$ (not $V$) ([3.5.3](/3.5.3#sec-3.2.7)) |
| symmetric / Hermitian eigenproblem | `eigh(A)`, `eigvalsh(A)` | real eigenvalues in ascending order, orthonormal eigenvectors |
| general eigenproblem | `eig(A)`, `eigvals(A)` | complex results; eigenvectors are the columns of the second output ([3.5.3](/3.5.3#sec-3.3.3)) |
| determinant | `det(A)`, `slogdet(A)` | `slogdet` returns sign and $\log\lvert\det A\rvert$, avoiding overflow and underflow |
| norms, condition, rank | `norm(x, ord)`, `cond(A)`, `matrix_rank(A)` | `norm(A)` is the Frobenius norm, `norm(A, 2)` the spectral norm |
| pseudoinverse | `pinv(A)` | via the SVD |

A few details are easily overlooked:

- For a symmetric matrix, always use `eigh`. It is faster, it returns real eigenvalues in ascending order, and the eigenvectors are exactly orthonormal; `eig` treats the matrix as general and may return slightly complex results caused by rounding. Since NumPy 2.5, `eig` and `eigvals` always return complex arrays, even when all eigenvalues happen to be real; earlier versions returned real arrays when possible, so the dtype of the result depended on the values.
- Determinants are rarely what we want numerically. `np.linalg.det(0.1 * np.eye(500))` returns `0.0` because $10^{-500}$ underflows, while `slogdet` returns the logarithm $-1151.29$ correctly. Log-likelihoods of multivariate normal distributions need $\log\det\Sigma$ and should use `slogdet` or the Cholesky factor ($\log\det\Sigma = 2\sum_i \log L_{ii}$).
- All functions accept stacks of matrices: `np.linalg.solve` with `A` of shape `(k, n, n)` solves $k$ systems at once.

`scipy.linalg` contains everything in `numpy.linalg` and more: LU with access to the factors, triangular solves (`solve_triangular`), Schur and QZ decompositions, matrix functions such as the matrix exponential `expm`, and solvers for structured matrices (banded, Toeplitz, circulant). When SciPy is available, it is generally the better choice ([4.4.4](/4.4.4#sec-4.1)).

## 3.3. Einstein Summation

### 3.3.1. The Notation

Many array operations are sums of products over some indices: the matrix product $C_{ik} = \sum_j A_{ij}B_{jk}$, the **trace** $\sum_i A_{ii}$, the quadratic form $\sum_{i,j} x_i A_{ij} x_j$. In the *Einstein summation convention*, from tensor calculus in physics, the summation signs are omitted and an index that appears twice is summed over. `np.einsum` implements a version of this convention: a string lists the indices of each operand, and after `->` the indices of the result; indices that do not appear in the result are summed over.

| Operation | Formula | `einsum` |
|---|---|---|
| trace | $\sum_i A_{ii}$ | `np.einsum("ii", A)` |
| diagonal | $A_{ii}$ | `np.einsum("ii->i", A)` |
| transpose | $A_{ji}$ | `np.einsum("ij->ji", A)` |
| matrix product | $\sum_j A_{ij}B_{jk}$ | `np.einsum("ij,jk->ik", A, B)` |
| batch matrix product | $\sum_j A_{bij}B_{bjk}$ | `np.einsum("bij,bjk->bik", A, B)` |
| quadratic form | $\sum_{i,j} x_i A_{ij} x_j$ | `np.einsum("i,ij,j", x, A, x)` |
| row-wise inner products | $\sum_j X_{ij}X_{ij}$ | `np.einsum("ij,ij->i", X, X)` |
| cross-product matrix $X^{\mathsf T}X$ | $\sum_n X_{ni}X_{nj}$ | `np.einsum("ni,nj->ij", X, X)` |

```python
A = np.arange(9.0).reshape(3, 3)
x = np.array([1.0, 2.0, 3.0])
print(np.einsum("ii", A), np.einsum("ii->i", A))   # 12.0 [0. 4. 8.]
print(np.einsum("i,ij,j", x, A, x), x @ A @ x)     # 192.0 192.0
X = np.arange(6.0).reshape(3, 2)
print(np.einsum("ij,ij->i", X, X))                 # [ 1. 13. 41.]: squared row norms
```

The value of `einsum` is that it states exactly which indices are contracted, which makes formulas from papers easy to translate and avoids chains of transposes and reshapes. For operations that have a dedicated function (`@`, `trace`, `sum`), the dedicated function is usually at least as fast.

### 3.3.2. Contraction Order

For more than two operands, the order of contraction matters, as in the matrix chain multiplication problem of dynamic programming ([4.1.13](/4.1.13)). For matrices of shapes $10 \times 100$, $100 \times 5$ and $5 \times 1000$, computing $(AB)C$ costs about $10 \cdot 100 \cdot 5 + 10 \cdot 5 \cdot 1000 = 55\,000$ multiplications, while the naive simultaneous sum over $j$ and $k$ in `einsum` costs $10 \cdot 100 \cdot 5 \cdot 1000 = 5 \times 10^6$. With `optimize=True`, `einsum` searches for a good order and dispatches pairwise contractions to BLAS; `np.einsum_path` shows the plan:

```python
rng = np.random.default_rng(0)
a, b, c = rng.random((10, 100)), rng.random((100, 5)), rng.random((5, 1000))
path, info = np.einsum_path("ij,jk,kl->il", a, b, c, optimize="optimal")
print(path)    # ['einsum_path', (0, 1), (0, 1)]: first a with b, then the result with c
# info reports: Naive FLOP count 1.500e+07, Optimized FLOP count 1.100e+05
```

On the test machine, `np.einsum("ij,jk,kl->il", a, b, c)` takes 3.2 ms without optimization and 0.04 ms with `optimize=True`. For contractions of many tensors, the package opt_einsum provides more elaborate path searches.

## 3.4. Random Numbers

### 3.4.1. The Generator Interface

Computers generate random numbers with a **pseudorandom number generator** ([3.5.8](/3.5.8#sec-8.1.1)): a deterministic algorithm whose output passes statistical tests of randomness and which is completely determined by its initial state, the **seed**. NumPy separates two layers. A *bit generator* produces a stream of random bits; the default is PCG64, a permuted **linear congruential generator** ([3.5.8](/3.5.8#sec-8.1.2)) with 128-bit state, which is fast, has good statistical properties and supports independent parallel streams. The Mersenne Twister of [3.5.8](/3.5.8#sec-8.1.4) is available as `MT19937` for compatibility. A `Generator` turns these bits into numbers from distributions.

The recommended interface since NumPy 1.17 is a `Generator` object created by `np.random.default_rng`:

```python
rng = np.random.default_rng(12345)       # Generator(PCG64), seeded
print(rng.random(3))                     # uniform on [0, 1): [0.22733602 0.31675834 0.79736546]
print(rng.integers(1, 7, size=10))       # dice: integers from 1 to 6 (the upper bound is excluded)
print(rng.normal(loc=0.0, scale=2.0, size=3))
print(rng.choice(["A", "C", "G", "T"], size=12))   # random DNA sequence
print(rng.permutation(5))                # random permutation of 0, ..., 4
print(rng.choice(10, size=4, replace=False))       # sampling without replacement
```

The older interface, `np.random.seed(0)` followed by functions such as `np.random.rand` or `np.random.normal`, uses one hidden global `RandomState` object with the Mersenne Twister. It is kept for backward compatibility (its streams are frozen and never change between versions) but should not be used in new code: global state means that any library function that draws random numbers changes the stream of every other part of the program, which makes results hard to reproduce and impossible to parallelize safely. The `Generator` methods also use better algorithms (for example the ziggurat method for normal variates, faster than the Box–Muller transform of [3.5.8](/3.5.8#sec-8.4.2)). A good convention is that every function that needs randomness takes a `rng` argument:

```python
def bootstrap_means(data, n_boot, rng):
    idx = rng.integers(0, data.size, size=(n_boot, data.size))
    return data[idx].mean(axis=1)
```

### 3.4.2. Distributions and Parameterizations

`Generator` provides about 35 distributions. Their parameterizations follow the conventions of the underlying algorithms and differ in places from the notation of probability courses (the notation of this wiki: $\mathrm{Exp}(\lambda)$ with rate $\lambda$, $\mathcal{N}(\mu, \sigma^2)$ with variance $\sigma^2$). These mismatches are a frequent source of errors:

| Distribution | Notation | NumPy call | Pitfall |
|---|---|---|---|
| uniform | $\mathrm{U}(a, b)$ | `rng.uniform(a, b)` | |
| normal | $\mathcal{N}(\mu, \sigma^2)$ | `rng.normal(loc=mu, scale=sigma)` | `scale` is the standard deviation, not the variance |
| exponential | $\mathrm{Exp}(\lambda)$ | `rng.exponential(scale=1/lam)` | `scale` is the mean $1/\lambda$, not the rate |
| Gamma | $\Gamma(\alpha, \lambda)$ | `rng.gamma(shape=alpha, scale=1/lam)` | scale, not rate |
| binomial | $\mathrm{Bin}(n, p)$ | `rng.binomial(n, p)` | |
| Poisson | $\mathrm{Poi}(\lambda)$ | `rng.poisson(lam)` | |
| geometric | $\mathrm{Geo}(p)$ | `rng.geometric(p)` | values $1, 2, \dots$ (trials until the first success) |
| negative binomial | $\mathrm{NB}(r, p)$ | `rng.negative_binomial(r, p)` | number of failures before the $r$-th success |
| multivariate normal | $\mathcal{N}_p(\boldsymbol{\mu}, \Sigma)$ | `rng.multivariate_normal(mu, Sigma)` | covariance matrix, not its square root |
| multinomial | $\mathrm{Mult}(n, \boldsymbol{p})$ | `rng.multinomial(n, pvals)` | |

A quick simulation is the best check of a parameterization:

```python
lam = 2.0
rng = np.random.default_rng(1)
print(rng.exponential(scale=1/lam, size=1_000_000).mean())    # 0.499..., the mean is 1/lambda
g = rng.gamma(shape=3.0, scale=1/lam, size=1_000_000)
print(g.mean(), g.var())                                       # about 1.5 and 0.75 = alpha/lambda^2
```

The same holds for `scipy.stats` ([4.4.4](/4.4.4#sec-4.5)), which uses `loc` and `scale` throughout. Note also that `Generator` streams are not frozen across NumPy versions: when an algorithm is improved or corrected, the same seed can produce different numbers. NumPy 2.5, for example, corrected an error in the algorithm for `Generator.binomial` and `multinomial`. Bit-for-bit reproducibility therefore requires recording the NumPy version together with the seed, which a lock file does ([4.4.1](/4.4.1#sec-1.2.3)).

### 3.4.3. Seeds, Reproducibility and Parallel Streams

A seeded generator reproduces its stream exactly, which makes simulations repeatable and bugs reproducible:

```python
print(np.random.default_rng(2026).random() == np.random.default_rng(2026).random())   # True
```

`np.random.default_rng()` without a seed draws fresh entropy from the operating system. For a reproducible analysis we can do this once, record the value, and seed with it afterwards: `np.random.SeedSequence().entropy` returns such a 128-bit integer.

Parallel simulations need several streams that do not overlap or correlate. Seeding the workers with `0, 1, 2, ...` is a common habit; with the seeding procedure of NumPy (`SeedSequence`, which hashes the seed) it is not wrong, but the clean solution is to *spawn* independent child generators from one parent:

```python
rng = np.random.default_rng(2026)
children = rng.spawn(3)                    # three independent Generators
print([int(g.integers(100)) for g in children])   # [62, 74, 8]
```

`np.random.SeedSequence(2026).spawn(3)` does the same at the level of seeds, which is convenient for passing to worker processes. A `Generator` object must not be shared between threads without a lock; giving each thread or process its own child generator is both correct and fast ([4.4.7](/4.4.7)).

### 3.4.4. Example: Monte Carlo Estimation

The **Monte Carlo method** estimates a quantity as the average of random samples. To estimate $\pi$, we draw $n$ points uniformly in the unit square and count the fraction that falls in the quarter disk $x^2 + y^2 \le 1$, whose area is $\pi/4$:

```python
def estimate_pi(n, rng):
    pts = rng.random((n, 2))
    return 4.0 * np.mean((pts ** 2).sum(axis=1) <= 1.0)


rng = np.random.default_rng(2026)
print([round(float(estimate_pi(n, rng)), 4) for n in (100, 10_000, 1_000_000)])
# [3.28, 3.1304, 3.142]
```

The indicator of the quarter disk is a Bernoulli variable with $p = \pi/4$, so the estimator $4\bar X$ has standard deviation $4\sqrt{p(1-p)/n} = \sqrt{\pi(4 - \pi)/n} \approx 1.64/\sqrt{n}$. By the **central limit theorem** the error is approximately normal with this standard deviation: to gain one decimal digit we need 100 times more samples. The figure shows 100 independent estimates for each $n$; their root mean square error follows the predicted line.

![Absolute error of 100 independent Monte Carlo estimates of pi for each number of points n, with the root mean square error and the theoretical standard error sqrt(pi (4 - pi) / n)](./plots/monte-carlo-error.py)

The rate $n^{-1/2}$ does not depend on the dimension, which is why Monte Carlo methods are the method of choice for high-dimensional integrals and for the simulation studies of statistics; in one or two dimensions, deterministic quadrature ([4.4.4](/4.4.4#sec-4.3.1)) is far more accurate for the same work.

## 3.5. Vectorization versus Loops

### 3.5.1. Measuring Run Time

Statements about speed must be measured, not guessed. The standard library module `timeit` runs a statement many times and reports the total time; it disables garbage collection during the measurement and uses the most precise clock available. In IPython and Jupyter, `%timeit stmt` does this automatically and chooses the number of repetitions:

```python
import timeit

x = np.random.default_rng(0).random(1_000_000)
t = min(timeit.repeat(lambda: (x * x).sum(), number=100, repeat=5)) / 100
print(f"{t * 1e3:.2f} ms per call")
```

Some rules make measurements meaningful:

- Repeat the measurement and take the minimum (or the median), since other processes add noise but never make code faster.
- Measure realistic sizes: the relative speed of two methods often depends on $n$, as the figure below shows.
- Exclude setup from the timed code (creating the input data), unless it is part of what is being compared.
- Be aware of caching and of lazy evaluation: the second call of a function may be much faster than the first (compiled code is cached, data are in the CPU cache).
- For whole programs, `time.perf_counter()` around a block measures wall-clock time; profilers ([4.4.7](/4.4.7)) show where the time goes.

### 3.5.2. Results

We compare three ways of computing $\sum_i x_i^2$: a Python `for` loop over a list, the built-in `sum` over a generator expression, and NumPy's `(x * x).sum()`.

![Run time of the sum of squares against n for a Python for loop, sum() over a generator and NumPy (left), and the time per element (right), measured on the build machine](./plots/loop-vs-vectorized.py)

On the test machine (Python 3.14, NumPy 2.5) the results were as follows; the figure is regenerated on the machine that builds this site, with other versions, so its numbers differ somewhat:

| $n$ | Python `for` loop | `sum` over a generator | NumPy `(x * x).sum()` |
|---|---|---|---|
| $10$ | 0.22 µs | 0.37 µs | 0.69 µs |
| $10^3$ | 16 µs | 22 µs | 1.2 µs |
| $10^6$ | 24 ms | 23 ms | 1.1 ms |

### 3.5.3. Why the Difference

A simple model explains the figure: the time of an operation on $n$ elements is approximately $a + bn$, with a fixed overhead $a$ and a cost $b$ per element.

- For the Python loop, $a$ is small but $b$ is about 20 ns: each iteration executes several bytecode instructions, each `v * v` and `s += ...` dispatches on the types of the operands (**dynamic typing**), and each intermediate result is a newly allocated float object, later freed by **reference counting**. The generator expression adds the overhead of resuming the generator for each element.
- For NumPy, $a$ is about 1 µs: argument parsing, dtype resolution, allocating the result array of `x * x`. But $b$ is about 1 ns, since the compiled loop works on raw `float64` values, uses SIMD instructions that process several elements per instruction, and reads memory sequentially.

Hence NumPy loses for very small arrays (below a few dozen elements) and wins by a factor of about 20 for large ones. Several consequences guide the design of numerical Python code:

- Vectorize the innermost, most frequently executed loops over large arrays; a Python loop over 60 iterations around vectorized operations (as in the Mandelbrot example of [4.4.2](/4.4.2#sec-2.6.2)) costs nothing.
- Do not vectorize tiny operations inside a long Python loop: calling NumPy on 3-element arrays a million times is slower than plain Python arithmetic. Restructure the computation so that the loop runs over the large dimension inside NumPy, or compile the loop ([4.4.7](/4.4.7)).
- Temporaries cost memory bandwidth: `(x * x).sum()` writes and reads an intermediate array of size $n$; `x @ x` or `np.einsum("i,i", x, x)` avoid it, and the `out` argument of ufuncs ([4.4.2](/4.4.2#sec-2.5.1)) reuses existing memory.
- The largest gains come from the algorithm, not from the implementation: the matrix product of §3.1.2 is 500 times faster in BLAS than in Python, and the random walk example of [4.4.2](/4.4.2#sec-2.7) became another hundred times faster through a better formulation.

## Summary

- `@` is matrix multiplication, `*` is elementwise; `matmul`, `vecdot`, `matvec` and `.mT` work on stacks of matrices. 1-D arrays are neither rows nor columns.
- Dense linear algebra runs in BLAS and LAPACK; only matrix–matrix operations reach high speed, and BLAS threads should be limited when parallelizing at a higher level.
- Solve linear systems with `solve` (or a reusable factorization), never with `inv`; use `lstsq` or QR instead of the normal equations; use `eigh` for symmetric matrices and `slogdet` instead of `det`. The condition number predicts the attainable accuracy.
- `einsum` expresses sums of products by index strings; `optimize=True` chooses the contraction order.
- Create one `Generator` with `np.random.default_rng(seed)` and pass it to every function that needs randomness; check parameterizations (scale versus rate, standard deviation versus variance); spawn child generators for parallel streams; record the NumPy version for exact reproducibility.
- Monte Carlo errors decrease like $n^{-1/2}$.
- Measure with `timeit`; the time of an operation is roughly overhead plus per-element cost, which explains when vectorization pays off.
