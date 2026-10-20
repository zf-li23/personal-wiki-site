---
title: R for Statistical Computing
description: "The R language as a tool for statistical computing: atomic vectors and lists, types, coercion and attributes, factors, matrices, arrays and data frames, functions and control flow, arithmetic, matrix operations and subsetting, vectorization with the apply family, the cost of loops and recursion, and the visualization of multivariate data."
---

All computations in this course are carried out in R. This chapter collects what is needed to use R reliably for statistical computing, with the emphasis on how R represents data, because most programming errors in R come from a misunderstanding of its objects: a vector that is silently coerced to character, a matrix that silently loses a dimension, a list subsetted with the wrong bracket. The chapter first describes the basic objects (vectors, lists, factors, matrices, arrays, data frames, functions), then the basic operations on them (input and output, arithmetic, logical and matrix operations, subsetting), then vectorization, R's way of avoiding explicit loops, and finally the tools for visualizing multivariate data. Floating-point numbers in R were treated in [3.5.1](/3.5.1); the numerical linear algebra built on R's matrix operations follows in [3.5.3](/3.5.3).

## 2.1. Introducing R

R is an industry-leading environment for data analysis and statistical programming, whose guideline is to turn ideas into software quickly and accurately. It grew out of the *S* language, a high-level language for data analysis developed from 1976 on by John Chambers and colleagues at the statistics research department of Bell Laboratories; the system S received the Software System Award of the Association for Computing Machinery (ACM) in 1998. R itself was created by Ross Ihaka and Robert Gentleman in the early 1990s as a free implementation of S and became part of the GNU project in 1997. Hadley Wickham's *Advanced R* (second edition, freely available at adv-r.hadley.nz) is a good reference for the material of this chapter.

Chambers summarized the computational model of the language in two slogans:

> To understand computations in R, two slogans are helpful: Everything that exists is an object. Everything that happens is a function call.

R can call code written in other languages: `.C` and `.Fortran` call compiled C and Fortran routines (Section 1.2.5 of [3.5.1](/3.5.1) mentioned the attribute `Csingle` used by these interfaces), the package `reticulate` embeds Python, and `R.matlab` exchanges data with MATLAB. This course uses only R.

## 2.2. Vectors

### 2.2.1. Atomic Vectors and Lists

When we create a variable, we reserve memory to store values. R does not provide direct access to the computer's memory but rather a number of specialized data structures, called objects; R is object-oriented in the sense that everything that comes into contact with R is an object, and the data type of the object becomes the data type of the variable. The frequently used structures are vectors, matrices, arrays, data frames and lists. The basic data structure is the vector, and there is no scalar in R: a scalar is a vector of length $1$.

**Definition 2.2.1 (Atomic Vector, List)** A *vector* in R is an ordered sequence of elements. It is an **atomic vector** if all elements have the same type, and a **list** (recursive vector) if its elements may be arbitrary objects, including other lists.

Every vector has three properties besides its contents: its *type* (`typeof()`, what it is), its *length* (`length()`, how many elements it contains) and its *attributes* (`attributes()`, additional arbitrary metadata).

```r
y <- list(2008, "Wow")
class(y); is.vector(y); is.atomic(y)
a <- 1:10
b <- as.list(1:10)
c <- as.array(1:10)
class(a); class(b); class(c)
is.vector(c); dim(c); dim(a)
```

```text
[1] "list"
[1] TRUE
[1] FALSE
[1] "integer"
[1] "list"
[1] "array"
[1] FALSE
[1] 10
NULL
```

The three objects `a`, `b`, `c` print almost alike but are different: `a` is an atomic vector, `b` is a list of ten length-one vectors, and `c` is a one-dimensional array, an atomic vector with a `dim` attribute, which is why `is.vector(c)` is `FALSE` (`is.vector` is `TRUE` only for vectors with no attributes other than names).

### 2.2.2. Types of Atomic Vectors

There are six types of atomic vectors: logical, integer, double (often called numeric), character, complex and raw; the last two are rare. `typeof()` gives the internal type, `class()` the class used for method dispatch:

```r
typeof(4); class(4)
y <- rnorm(30)
foo <- lm(y ~ 1)
typeof(foo); class(foo)
```

```text
[1] "double"
[1] "numeric"
[1] "list"
[1] "lm"
```

Atomic vectors are usually created with `c()`, short for combine (concatenate), and they are always flat, even if `c()` calls are nested:

```r
dbl_var <- c(1, 2.5, 4.5)
int_var <- c(1L, 6L, 10L)
log_var <- c(TRUE, FALSE, T, F)
chr_var <- c("these", "strings")
c(1, c(2, c(3, 4)))           # same as c(1, 2, 3, 4)
```

```text
[1] 1 2 3 4
```

The type of a vector is tested with an "is" function: `is.double()`, `is.integer()`, `is.character()`, `is.logical()`, or, more generally, `is.atomic()`. Note that `is.numeric()` is a general test for the "numberliness" of a vector and returns `TRUE` for both integer and double vectors: `is.numeric(int_var)` and `is.numeric(dbl_var)` are both `TRUE`.

### 2.2.3. Missing Values: NA, NaN and NULL

Missing values are specified with `NA`, a logical vector of length $1$. `NA` is always coerced to the correct type when used inside `c()`; missing values of a specific type can be created with `NA_real_` (a double), `NA_integer_` and `NA_character_`. Three special values are easily confused:

| | `NA` | `NaN` | `NULL` |
|---|---|---|---|
| Meaning | missing value, a placeholder | impossible numerical value, such as `0/0` | the empty object, an undefined expression or function result |
| `class()` | `"logical"` | `"numeric"` | `"NULL"` |
| `length(c(27, 29, x))` | $3$ | $3$ | $2$ |
| `x > 1` | `NA` | `NA` | `logical(0)` |

`NaN` is the IEEE 754 "not a number" of [3.5.1](/3.5.1) (whereas `1/0` is `Inf`); `is.na()` is `TRUE` for both `NA` and `NaN`. `NULL` has length $0$, and assigning `NULL` to a component removes it from a list. Zero-length results are common: `which(11 == 1:10)` returns `integer(0)`.

### 2.2.4. Coercion

All elements of an atomic vector must have the same type. When different types are combined, they are converted to the most flexible type, a *coercion* that follows the order

$$
\text{logical}<\text{integer}<\text{double}<\text{character}.
$$

```r
str(c("a", 1))
class(c(TRUE, TRUE, FALSE, 2))
x <- c(FALSE, FALSE, TRUE)
as.numeric(x)
sum(x)         # total number of TRUEs
mean(x)        # proportion of TRUEs
```

```text
 chr [1:2] "a" "1"
[1] "numeric"
[1] 0 0 1
[1] 1
[1] 0.3333333
```

Coercion often happens automatically: most mathematical functions coerce to double or integer, and most logical operations coerce to logical. Comparisons between a string and a number coerce the number to a string and compare the strings alphabetically, character by character. Hence `'3L' > 2` is `TRUE` (`"3L"` sorts after `"2"`), `'3L-5' > 2` is `TRUE` as well, and `'0L+3' > 2` is `FALSE`: the expressions inside the quotes are never evaluated. In the same way `'10' < '11'` is `TRUE` but `'9' < '11'` is `FALSE`. A student once computed the empirical quantile of a five-digit number `x` with `sum(data <= x) / length(data)`, having read `x` as a string; the comparison with the numbers in `data` became alphabetical, and the result $0.16$ instead of $0.84$ looked like "one minus the right answer" only by coincidence.

R usually gives a warning if coercion might lose information. If confusion is likely, coerce explicitly with `as.character()`, `as.double()`, `as.integer()` or `as.logical()`:

```r
as.numeric(c("a", 1))
```

```text
[1] NA  1
Warning message:
NAs introduced by coercion
```

### 2.2.5. Attributes

Objects can have arbitrary additional attributes, used to store metadata about the object. The attributes form a named list (with unique names), accessed individually with `attr()` or all at once with `attributes()`; `structure()` returns a new object with modified attributes.

```r
y <- 1:10
attr(y, "my_attribute") <- "This is a vector"
attr(y, "my_attribute")
str(attributes(y))
z <- structure(y, my_attribute = "Hi")   # a modified copy; y is unchanged
attributes(y[1])                          # subsetting drops the attribute
```

```text
[1] "This is a vector"
List of 1
 $ my_attribute: chr "This is a vector"
NULL
```

Most attributes are lost when a vector is modified. The only attributes not lost are the three most important ones:

- `names`, a character vector giving each element a name;
- `dim`, used to turn vectors into matrices and arrays;
- `class`, used to implement the S3 object system.

They are read and set with their own functions, `names(x)`, `dim(x)` and `class(x)`, not with `attr(x, "names")`. Setting `dim(y) <- 10` turns the integer vector `y` into a one-dimensional array: `is.vector(y)` becomes `FALSE` and `class(y)` becomes `"array"`.

A vector can be named in three ways: when it is created, `x <- c(a = 1, b = 2, c = 3)`; by modifying an existing vector, `x <- 1:3; names(x) <- c("a", "b", "c")`; or by creating a modified copy, `y <- setNames(x, c("m", "n", "c"))`. Names do not have to be unique, but they had better be, since subsetting by a name returns only its first match. Not all elements need a name: if some names are missing when the vector is created, they are empty strings (`names(c(a = 1, 2, 3))` is `"a" "" ""`); if only some names are set by modifying the vector, the others are `NA` (`NA_character_`); if all names are missing, `names()` returns `NULL`.

### 2.2.6. Lists

Lists are used to build up more complicated data structures; data frames and fitted linear models are lists. A list is constructed with `list()` instead of `c()`; `c()` applied to lists combines them into one list, coercing atomic vectors to lists. A list is turned into an atomic vector with `unlist()`, using the same coercion rules as `c()`. Lists are tested with `is.list()` and created from other objects with `as.list()`.

```r
x <- list(list(list(list())))
is.recursive(x)
x <- list(list(1, 2), c(3, 4))
y <- c(list(1, 2), c(3, 4))
str(x)
str(y)
```

```text
[1] TRUE
List of 2
 $ :List of 2
  ..$ : num 1
  ..$ : num 2
 $ : num [1:2] 3 4
List of 4
 $ : num 1
 $ : num 2
 $ : num 3
 $ : num 4
```

So what `c()` creates is not always an atomic vector: combining a list with anything gives a list.

## 2.3. Factors, Matrices and Data Frames

### 2.3.1. Factors

One important use of attributes is to define factors.

**Definition 2.3.1 (Factor)** A **factor** is a vector that can contain only predefined values, used to store categorical data. It is built on top of an integer vector with two attributes: `class`, equal to `"factor"`, which makes it behave differently from regular integer vectors, and `levels`, which defines the set of allowed values.

```r
x <- factor(c("a", "b", "b", "a"))
x
class(x); levels(x)
x[2] <- "c"
x
```

```text
[1] a b b a
Levels: a b
[1] "factor"
[1] "a" "b"
Warning message:
In `[<-.factor`(`*tmp*`, 2, value = "c") :
  invalid factor level, NA generated
[1] a    <NA> b    a
Levels: a b
```

Values that are not among the levels cannot be used. Factors are useful when the possible values of a variable are known, even if not all of them appear in a given data set:

```r
sex_char <- c("m", "m", "m")
sex_factor <- factor(sex_char, levels = c("m", "f"))
table(sex_char)
table(sex_factor)
```

```text
sex_char
m 
3 
sex_factor
m f 
3 0 
```

### 2.3.2. Matrices and Arrays

Adding a `dim` attribute to an atomic vector makes it a multi-dimensional array; a matrix is the special case of two dimensions. Matrices and arrays are also created with `matrix()` and `array()`, tested with `is.matrix()` and `is.array()` (or by looking at the length of `dim`), and `as.matrix()` and `as.array()` turn an existing vector into a matrix or an array. The elements are filled in column by column.

```r
c <- 1:6
dim(c) <- c(3, 2)
c
a <- matrix(1:6, ncol = 3, nrow = 2)   # specify rows and columns
b <- array(1:12, c(2, 3, 2))           # specify all dimensions
```

```text
     [,1] [,2]
[1,]    1    4
[2,]    2    5
[3,]    3    6
```

The vector functions have higher-dimensional generalizations:

| Vector | Matrix | Array |
|---|---|---|
| `length()` | `nrow()`, `ncol()` | `dim()` |
| `names()` | `rownames()`, `colnames()` | `dimnames()` (a list of character vectors) |
| `c()` | `cbind()`, `rbind()` | `abind()` (package `abind`) |
| | `t()` (transpose) | `aperm()` (generalized transpose) |

```r
rownames(a) <- c("A", "B")
colnames(a) <- c("a", "b", "c")
a
dimnames(b) <- list(c("one", "two"), c("a", "b", "c"), c("A", "B"))
b
```

```text
  a b c
A 1 3 5
B 2 4 6
, , A

    a b c
one 1 3 5
two 2 4 6

, , B

    a b c
one 7  9 11
two 8 10 12
```

Setting `dim()` of an atomic vector gives a matrix; setting `dim()` of a list gives a *list-matrix* (or list-array), whose cells are arbitrary objects:

```r
x <- list(2:4, "a", TRUE, 1.0)
dim(x) <- c(2, 2)
x
is.list(x); is.matrix(x); is.numeric(x)
```

```text
     [,1]      [,2]
[1,] integer,3 TRUE
[2,] "a"       1   
[1] TRUE
[1] TRUE
[1] FALSE
```

These relatively esoteric structures are useful for arranging objects in a grid, for example storing models fitted on a spatio-temporal grid in a three-dimensional array that preserves the grid structure.

### 2.3.3. Data Frames

**Definition 2.3.2 (Data Frame)** A **data frame** is a list of equal-length vectors, displayed as a table whose columns are the vectors.

The data frame is the most common way of storing data in R. Its two-dimensional structure makes it share properties of both a matrix and a list: it can be subsetted like a one-dimensional structure (where it behaves like a list of columns) or like a two-dimensional structure (where it behaves like a matrix). Its `length()` is the length of the underlying list, so it equals `ncol()`, while `nrow()` gives the number of rows; it has `names()`, `colnames()` and `rownames()`, with `names()` equal to `colnames()`. Unlike a matrix, a data frame can have columns of different types.

```r
df <- data.frame(x = 1:3, y = 3:1, z = letters[1:3])
typeof(df); class(df); is.data.frame(df)
is.list(df); is.matrix(df); is.vector(df)
```

```text
[1] "list"
[1] "data.frame"
[1] TRUE
[1] TRUE
[1] FALSE
[1] FALSE
```

Every list is a vector (`is.vector(list(1))` is `TRUE`), but a data frame is not, because of its `class` and `row.names` attributes. Data frames are combined with `cbind()` (column-wise; the numbers of rows must match, and row names are ignored) and `rbind()` (row-wise; both the number and the names of the columns must match); `plyr::rbind.fill()` combines data frames that do not have the same columns.

```r
cbind(df, data.frame(w = 3:1))
rbind(df, data.frame(x = 10, y = 3, z = "aa"))
```

```text
  x y z w
1 1 3 a 3
2 2 2 b 2
3 3 1 c 1
   x y  z
1  1 3  a
2  2 2  b
3  3 1  c
4 10 3 aa
```

**Example 2.3.1** The two data frames below print identically, and they even compare equal elementwise:

```r
Left <- data.frame(cbind(a = 1:2, b = c("a", "b")))
Right <- data.frame(a = 1:2, b = c("a", "b"))
Left == Right
```

```text
        a    b
[1,] TRUE TRUE
[2,] TRUE TRUE
```

Yet they are different. `cbind()` first creates a matrix, and a matrix has a single type, so the numbers $1,2$ are coerced to the strings `"1"`, `"2"`, and the column `Left$a` is a character vector; `Right$a` is an integer vector. The comparison `==` coerces again (`'1' == 1` is `TRUE`), which hides the difference. In one word: coercion. `data.frame()` should be called with the columns directly, as in `Right`.

## 2.4. Functions and Control Flow

### 2.4.1. Functions

Functions in R are "first-class objects": they can be assigned, passed as arguments and returned like any other object. R software is written in a functional style, which helps both to understand the intent and to ensure that the implementation corresponds to that intent. The natural complement of the functional style is the definition of classes of objects: functions should encapsulate the actions of an analysis, and classes should encapsulate the nature of the objects used and returned by function calls. The duality between function calls and objects is a recurrent theme of programming with R.

Two functions are used constantly in simulation. `sample()` draws a random sample, here the rows of a data frame `dat` without and with replacement; `set.seed()` makes the pseudorandom numbers reproducible ([3.5.8](/3.5.8)):

```r
dat[sample(1:nrow(dat), 100), ]                 # without replacement
dat[sample(1:nrow(dat), replace = TRUE), ]      # with replacement (a bootstrap sample)
```

`replicate(n, expr)` evaluates an expression `n` times and simplifies the results. `replicate(100, mean(rnorm(1000)))` generates $1000$ standard normal numbers, computes their mean, and repeats the process $100$ times, returning a vector of $100$ means; `replicate(10, rnorm(20))` returns a $20\times10$ matrix whose columns are the ten samples.

A good function checks its arguments, offers flexibility, returns its value at the end, and is indented and commented:

```r
SdFunc <- function(x, type = "sample", ...) {
  stopifnot(is.numeric(x), length(x) > 0,
            type %in% c("sample", "population"))   # robustness: check parameters
  x <- x[!is.na(x)]                                  # remove all missing values
  n <- length(x)
  m <- mean(x, ...)                                  # flexibility: "..." passes extra arguments on
  if (type == "sample") {
    sd <- sqrt(sum((x - m)^2) / (n - 1))
  }
  if (type == "population") {
    sd <- sqrt(sum((x - m)^2) / n)
  }
  return(sd)                                         # return at the end
}
y <- c(1:10, 50)
SdFunc(y, type = "sample", trim = 0.1)               # trim is passed to mean()
```

The argument `...` is a "back door": arguments not matched by name are passed on, here `trim = 0.1` to `mean()`, which then computes a trimmed mean.

### 2.4.2. Control Flow

The conditional statement has the forms `if (cond) statement` and `if (cond) statement1 else statement2`, where the statements may be blocks in braces. At the top level of a script or the console, `else` must be on the same line as the closing brace of the `if` block:

```r
if (cond) {
  statement1
} else {               # correct
  statement2
}
```

If `statement1` ends a line and `else` starts the next one, the interpreter considers the `if` statement complete at the end of the first line and reports an error at `else` (inside the braces of a function body the line break is harmless, but the braced style is safer). `if` takes a single condition; the vectorized `ifelse()` is a different function (Section 2.6.2). Loops are written `for (var in seq) statement`, `while (cond) statement` and `repeat statement` (left with `break`). Explicit loops are slow in R; vectorized operations should be used instead whenever possible (Section 2.6).

`return` is a function, so its argument must be in parentheses:

```r
check1 <- function(x, y) { if (x > y) return TRUE else return FALSE }
check2 <- function(x, y) { return(x > y) }
check3 <- function(x, y) { if (x > y) TRUE else FALSE }
check4 <- function(x, y) return({ if (x > y) TRUE else FALSE })
```

```text
Error: unexpected numeric constant in "check1 <- function(x, y) { if (x > y) return TRUE"
```

`check1` is a syntax error, because `return TRUE` is not a function call; `check2`, `check3` and `check4` are all correct. A function returns the value of its last evaluated expression, so `check3` needs no `return`, and `if` is itself an expression with a value, which `check4` passes to `return()`.

## 2.5. Basic Operations

### 2.5.1. Input and Output

Tabular data are the dominant format in statistical analysis. `read.table()` and `write.table()` read and write tabular text files; `read.csv()` and `read.delim()` are the same as `read.table()` but with different default values: `read.csv()` for comma-separated values (`.csv`, with `header = TRUE` and `sep = ","` by default) and `read.delim()` for tab-delimited text.

```r
a <- file.choose()                        # choose a csv file interactively
x <- read.csv(a)                          # header = TRUE by default
df <- read.table(a, sep = ",", header = TRUE)
write.csv(x, file = "foo.csv")
```

R objects are stored in the binary `.RData` format with `save()` and restored with `load()`; `save.image()` is a shortcut for "save my current workspace", that is, `save(list = ls(all.names = TRUE), file = ".RData")`. `.RData` files save space by compression and are fast to load, since no text has to be parsed.

```r
x <- runif(20)
y <- list(a = 1, b = TRUE, c = "oops")
save(x, y, file = "xy.RData")
save.image()            # creates ".RData" in the current working directory
unlink("xy.RData")      # deletes files and directories
```

### 2.5.2. Arithmetic and Logical Operators

| Operator | Description | Operator | Description |
|---|---|---|---|
| `+` | addition | `!` | logical NOT |
| `-` | subtraction | `&` | elementwise logical AND |
| `*` | multiplication | `&&` | logical AND for scalars, short-circuited |
| `/` | division | `\|` | elementwise logical OR |
| `^` | exponentiation | `\|\|` | logical OR for scalars, short-circuited |
| `%%` | modulus (remainder) | | |
| `%/%` | integer division | | |

Basic arithmetic functions include `log()`, `log2()`, `log10()`, `exp()`, the trigonometric functions `cos()`, `sin()`, `tan()`, `acos()`, `asin()`, `atan()`, and `abs()`, `sqrt()`. Values are assigned with `<-` (or `=`): `x <- 2; y = 3`.

Every operator is a function, called through its name in backquotes or quotes: `2 * 3` is the call `` `*`(2, 3) `` (also written `'*'(2, 3)`), and `x[1]` is `` `[`(x, 1) ``.

Logical operators coerce numbers to logical (zero is `FALSE`, everything else `TRUE`):

```r
x <- c(TRUE, FALSE, 0, 6)     # coerced to double: 1 0 0 6
y <- c(FALSE, TRUE, FALSE, TRUE)
!x
x & y
x | y
```

```text
[1] FALSE  TRUE  TRUE FALSE
[1] FALSE FALSE FALSE  TRUE
[1]  TRUE  TRUE FALSE  TRUE
```

In `A && B`, the expression `B` is evaluated only if `A` is `TRUE`; in `A || B`, only if `A` is `FALSE`. The scalar operators belong in `if` and `while` conditions; since R 4.3.0 they signal an error when an operand has length greater than $1$.

### 2.5.3. Vector and Matrix Operations

Arithmetic on vectors is elementwise, and the shorter vector is looped over, a rule called *recycling*; R warns when the longer length is not a multiple of the shorter one:

```r
(1:8) * (1:2)
(1:8) * (1:3)
(1:2)^(1:8)
```

```text
[1]  1  4  3  8  5 12  7 16
[1]  1  4  9  4 10 18  7 16
Warning message:
In (1:8) * (1:3) :
  longer object length is not a multiple of shorter object length
[1]   1   4   1  16   1  64   1 256
```

Common calculations are `max()`, `min()`, `range()`, `length()`, `sort()`, `sum()`, `prod()`, `mean()`, `sd()` and `var()`.

For matrices, `t()` transposes and `diag(v)` creates a diagonal matrix; `solve(A, b)` solves the linear system $A\boldsymbol{x}=\boldsymbol{b}$ and `solve(A)` returns the inverse. It is called `solve` because solving a system, by an LU decomposition ([3.5.3](/3.5.3)), is cheaper and more accurate than forming $A^{-1}$ and multiplying, which is why one should write `solve(A, b)` rather than `solve(A) %*% b`. Further indicators are the determinant `det()`, the eigenvalues and eigenvectors `eigen()`, the trace `sum(diag(M))` and the rank `qr(M)$rank`. Matrix multiplication is `%*%`; the operators `+ - * / ^` are elementwise. Elementwise operations between two matrices require the same dimensions; between a matrix and a vector, the vector is recycled along the columns, and the length of the matrix must be a multiple of the length of the vector.

**Example 2.5.1** Let `A <- matrix(1:4, 2, 2)`, that is, $A=\begin{bmatrix}1&3\\2&4\end{bmatrix}$, and `b <- c(1, 2)`. Then

| Command | Result |
|---|---|
| `out1 <- A %*% b` | the $2\times1$ matrix $(7,10)^{\mathsf T}$: the vector is treated as a column |
| `out2 <- b %*% A` | the $1\times2$ matrix $(5,11)$: the vector is treated as a row |
| `out3 <- A * b` | $\begin{bmatrix}1&3\\4&8\end{bmatrix}$: `b` recycled down the columns |
| `out4 <- b * A` | the same as `out3` |
| `out5 <- t(b) %*% A` | the $1\times2$ matrix $(5,11)$, the same as `out2` |
| `out6 <- t(b) * A` | error: non-conformable arrays ($1\times2$ and $2\times2$) |
| `out7 <- A %*% t(b)` | error: non-conformable arguments ($2\times2$ times $1\times2$) |

So `out3 == out4` and `out2 == out5` are `TRUE` elementwise, while `out1 == out2` fails, because a $2\times1$ and a $1\times2$ matrix are non-conformable arrays.

**Example 2.5.2** For an $n\times n$ matrix $M$ and a vector $\boldsymbol{z}$ of length $n$, the code

```r
(M %*% z %*% t(M %*% z)) / (t(z) %*% M %*% z)
```

meant to compute $\dfrac{M\boldsymbol{z}(M\boldsymbol{z})^{\mathsf T}}{\boldsymbol{z}^{\mathsf T}M\boldsymbol{z}}$ fails: the denominator is a $1\times1$ matrix, not a number, and dividing an $n\times n$ matrix by a $1\times1$ matrix is a non-conformable operation. Moreover $M\boldsymbol{z}$ is computed twice. A corrected version converts the denominator to a scalar and reuses $M\boldsymbol{z}$:

```r
v <- M %*% z
tcrossprod(v) / drop(crossprod(z, v))     # v v^T / (z^T v)
```

### 2.5.4. Subsetting

Subsetting selects or excludes variables and observations. There are four ways to subset, shown here for `x <- 1:10` and for the data frame `airquality`:

| Way | Examples |
|---|---|
| By position | `x[4]`, `x[-4]` (all but the fourth), `x[2:4]`, `x[-(2:4)]` or `x[-2:-4]`, `x[c(1, 2, 5)]` |
| By condition (a logical vector) | `x[x == 10]`, `x[x < 0]`, `x[x %in% c(1, 2, 5)]` |
| By name | `airquality[, "Ozone"]`, `airquality$Ozone`, `airquality[, c("Wind", "Temp")]` |
| With `subset()` | `subset(airquality, Temp > 80, select = c(Ozone, Temp))` |

Positions and conditions are different things: for `x <- 3:10`, `x[c(1, 2, 5)]` gives the first, second and fifth elements `3 4 7`, while `x[x %in% c(1, 2, 5)]` gives the elements whose values are $1$, $2$ or $5$, namely `5`. And `$` works only for recursive objects: after `x <- c(1, 2); names(x) <- c("Bob", "Ed")`, the call `x$Ed` is an error ("$ operator is invalid for atomic vectors"); use `x["Ed"]` or `x[["Ed"]]`.

The general rules are: use `[i]` for vectors and factors, `[i, j]` for matrices and data frames, and `[[i]]` for lists and data frames. If a list `x` is a train carrying objects, then `x[1:3]` is a train of cars $1$–$3$, and `x[[1]]` is the object in car $1$.

```r
A <- matrix(1:4, 2, 2)
L1 <- list(list1 = as.data.frame(A), list2 = matrix(1:16, 4, 4), list3 = c(1, 2))
L1[1]          # a list of length 1 containing the data frame
L1[[1]]        # the data frame itself
```

```text
$list1
  V1 V2
1  1  3
2  2  4

  V1 V2
1  1  3
2  2  4
```

For `x <- list(list(1, 2), c(3, 4))`, the element `2` is obtained as a number by `x[[1]][[2]]`; `x[[1]][2]` is a list of length $1$, and `x[1][2]` is a list containing `NULL`.

**Example 2.5.3 (Beware of Degradation)** To verify that a positive definite matrix has positive leading principal minors, consider

```r
check <- function(M) {
  n <- ncol(M)
  lpm <- rep(0, n)
  for (i in 1:n) {
    lpm[i] <- det(M[1:i, 1:i])
  }
  return(lpm)
}
M <- matrix(c(2, -1, 0, -1, 2, -1, 0, -1, 2), ncol = 3)
check(M)
```

```text
Error in UseMethod("determinant") :
  no applicable method for 'determinant' applied to an object of class "c('double', 'numeric')"
```

For `i = 1`, `M[1:1, 1:1]` is not a $1\times1$ matrix but the number `2`: subsetting drops every dimension of length $1$, and `det()` accepts only matrices (`det(M[1, 1])` gives the same error). Vectors, matrices with a single row or column, data frames with a single column and arrays with a single dimension all look similar, and R converts between them silently. The fix is `det(M[1:i, 1:i, drop = FALSE])`; `class(M[1, 1, drop = FALSE])` is `"matrix" "array"`, and `det(as.matrix(M[1, 1]))` also works. The function then returns `2 3 4`.

Subsetting either *simplifies* the result to the simplest possible structure or *preserves* the structure of the input. Preserving is the same for all data types; simplifying behaves slightly differently:

| | Simplifying | Preserving |
|---|---|---|
| Vector | `x[[1]]` (names removed) | `x[1]` |
| List | `x[[1]]` (the object inside, not a one-element list) | `x[1]` |
| Factor | `x[1:4, drop = TRUE]` (unused levels dropped) | `x[1:4]` |
| Matrix or array | `x[, 1]`, `x[1, ]` (dimensions of length $1$ dropped) | `x[, 1, drop = FALSE]`, `x[1, , drop = FALSE]` |
| Data frame | `x[, 1]`, `x[[1]]` (a vector if the result is a single column) | `x[, 1, drop = FALSE]`, `x[1]` |

When a single column of a data frame is selected, matrix subsetting simplifies by default and list subsetting does not:

```r
df <- data.frame(x = 1:2, y = 2:1, z = letters[1:2])
str(df["x"])        # like a list: still a data frame
str(df[, "x"])      # like a matrix: simplified to a vector
df[c("x", "z")]     # two ways to select columns give the same data frame
df[, c("x", "z")]
```

```text
'data.frame':	2 obs. of  1 variable:
 $ x: int  1 2
 int [1:2] 1 2
  x z
1 1 a
2 2 b
  x z
1 1 a
2 2 b
```

For the data frame `iris`, the four expressions `iris$Sepal.Width`, `iris[2]`, `iris[[2]]` and `iris[, 2]` select the same column; all except `iris[2]`, which is a one-column data frame, return the same numeric vector.

## 2.6. Vectorization

### 2.6.1. Binary Operators and Reduce

The expression `1:4 * 4:1` is the call `'*'(1:4, 4:1)`. Binary operators can be customized: any function named `%name%` can be used in infix form.

```r
a <- c("apple", "banana", "orange")
b <- c("grape", "banana", "orange")
"%it%" <- function(x, y) intersect(x, y)
a %it% b
c <- c("grape", "banana", "other")
a %it% b %it% c
Reduce("%it%", list(a, b, c))
```

```text
[1] "banana" "orange"
[1] "banana"
[1] "banana"
```

When more than two arguments are involved, `Reduce(f, list)` applies a binary function successively, $f(f(x_1,x_2),x_3)$ and so on, which keeps the code concise. Note the quotes and the percent signs in the operator's name.

### 2.6.2. Vectorize and the apply Family

*Vectorization* means writing computations as operations on whole vectors instead of loops over their elements. Consider a function that determines whether a number is even:

```r
func <- function(x) {
  if (x %% 2 == 0) {
    ret <- TRUE
  } else {
    ret <- FALSE
  }
  return(ret)
}
func(34)
vec <- 1:4
func(vec)
```

```text
[1] TRUE
Error in if (x%%2 == 0) { : the condition has length > 1
```

`if` accepts a single condition. `Vectorize()` turns the function into one that accepts vectors, `funcv <- Vectorize(func); funcv(vec)`, and `sapply()` applies it elementwise; here the vectorized expression `vec %% 2 == 0` is of course simplest.

```r
sapply(vec, func)
sapply(iris[, 1:4], function(x) sd(x) / mean(x))   # coefficient of variation of each column
mylist <- as.list(iris[, 1:4])
sapply(mylist, mean)
```

```text
[1] FALSE  TRUE FALSE  TRUE
Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
   0.1417113    0.1425642    0.4697441    0.6355511 
Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
    5.843333     3.057333     3.758000     1.199333 
```

Fisher's (Anderson's) `iris` data set gives the measurements in centimeters of four variables (sepal length and width, petal length and width) for $50$ flowers from each of $3$ species of iris; the code computes the **sample coefficient of variation** of each measurement. `sapply()` works on vectors, data frames and lists. `lapply()` does the same computation but returns a list, while `sapply()` simplifies the result to a vector or matrix when possible:

```r
a <- sapply(iris[, 1:4], function(x) sd(x) / mean(x))
b <- lapply(iris[, 1:4], function(x) sd(x) / mean(x))
is.vector(a); is.list(b)
is.list(a); is.vector(b)
```

```text
[1] TRUE
[1] TRUE
[1] FALSE
[1] TRUE
```

(`b` is a list, and every list is a vector.) `tapply()` groups data by an index and applies a function to each group, returning an array; `aggregate()` is similar but returns a data frame, and its argument `by` must be a list:

```r
levels(iris$Species)
tapply(X = iris$Sepal.Length, INDEX = iris$Species, FUN = mean)
with(iris, aggregate(x = Sepal.Length, by = list(Species), FUN = mean))
```

```text
[1] "setosa"     "versicolor" "virginica" 
    setosa versicolor  virginica 
     5.006      5.936      6.588 
     Group.1     x
1     setosa 5.006
2 versicolor 5.936
3  virginica 6.588
```

`tapply()` returns an array rather than a vector because the index may be a list of several factors, and the result then has one dimension per factor:

```r
index1 <- rep(c("A", "B", "C"), each = 3)
index2 <- rep(c("X", "Y", "Z"), 3)
value <- sample(1:100, 9)
SEdata <- data.frame(index1, index2, value)
tapply(SEdata$value, list(SEdata$index1, SEdata$index2), max)        # a 3 x 3 table
aggregate(SEdata$value, list(SEdata$index1, SEdata$index2), max)    # a data frame with 9 rows
```

`apply(X, MARGIN, FUN)` vectorizes matrix calculations over rows (`MARGIN = 1`) or columns (`MARGIN = 2`):

```r
set.seed(1)
vec <- round(runif(12) * 100)
mat <- matrix(vec, nrow = 3)
mat
apply(mat, 1, sum)
apply(mat, 2, function(x) max(x) - min(x))
```

```text
     [,1] [,2] [,3] [,4]
[1,]   27   91   94    6
[2,]   37   20   66   21
[3,]   57   90   63   18
[1] 218 144 228
[1] 30 71 31 15
```

`apply()` on a data frame must be used with caution, because it first converts the data frame with `as.matrix()`, and a data frame with a character column becomes a character matrix, in which the numbers are formatted to a common number of digits. To remove all rows containing $-1$:

```r
x <- data.frame(names = letters[1:4], score = c(-2, -1, 1, -1))
x[!apply(x, 1, function(row) -1 %in% row), ]
x <- data.frame(names = letters[1:4], score = c(-2.78787, -1, 1.89766, -1))
x[!apply(x, 1, function(row) -1 %in% row), ]
```

```text
  names score
1     a    -2
3     c     1
  names    score
1     a -2.78787
2     b -1.00000
3     c  1.89766
4     d -1.00000
```

The second call removes nothing: the rows are character vectors such as `"b" "-1.00000"`, and `-1 %in% row` compares the string `"-1"` with `"-1.00000"` (`'-1' %in% '-1'` is `TRUE`, `'-1' %in% '-1.000000'` is `FALSE`). Working on the numeric column avoids the problem: `x[x$score != -1, ]`, `x[!sapply(x[, 2], function(v) -1 %in% v), ]`, or `x[x == -1] <- NA; na.omit(x)`.

`mapply()` is the multivariate version of `sapply()`: it applies a function of several arguments $f(x_1,x_2,\dots)$ elementwise to several vectors; `MoreArgs` supplies arguments that are not vectorized over.

```r
mapply(rep, times = 1:4, MoreArgs = list(x = 42))
mapply(rep, times = 1:4, x = 4:1)
mapply(function(x, y, z, k) (x + k)^(y + z),
       c(a = 2, b = 3), c(A = 3, B = 4), MoreArgs = list(1, 2))
```

```text
[[1]]
[1] 42

[[2]]
[1] 42 42

[[3]]
[1] 42 42 42

[[4]]
[1] 42 42 42 42

[[1]]
[1] 4

[[2]]
[1] 3 3

[[3]]
[1] 2 2 2

[[4]]
[1] 1 1 1 1

   a    b 
 256 3125 
```

(`mapply(rep, 1:4, 4:1)` matches the arguments by position, `x = 1:4, times = 4:1`.) A multiplication table for two parameters varying from $1$ to $9$ can be built with `mapply()` over all combinations from `expand.grid()`, a data frame, or, when there are only two parameters, with `outer()`, which applies a vectorized function to all pairs and returns a matrix:

```r
vec1 <- vec2 <- 1:9
para <- expand.grid(vec1, vec2)
res <- mapply(FUN = "*", para[, 1], para[, 2])
head(cbind(para, res), 3)
outer(vec1, vec2, FUN = "*")[1:3, ]
myfunc <- function(x, y) paste0(x, "*", y, "=", x * y)
outer(vec1, vec2, FUN = myfunc)[1:2, 1:4]
```

```text
  Var1 Var2 res
1    1    1   1
2    2    1   2
3    3    1   3
     [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9]
[1,]    1    2    3    4    5    6    7    8    9
[2,]    2    4    6    8   10   12   14   16   18
[3,]    3    6    9   12   15   18   21   24   27
     [,1]    [,2]    [,3]    [,4]   
[1,] "1*1=1" "1*2=2" "1*3=3" "1*4=4"
[2,] "2*1=2" "2*2=4" "2*3=6" "2*4=8"
```

Conditions are vectorized with `ifelse(test, yes, no)`, whose values are recycled from `yes` and `no`, and with `switch()` for multiple branches. If the first argument of `switch()` is a number, the argument in that position is returned; if it is a string, it is matched exactly against the names of the following arguments, and an unnamed last argument serves as the default.

```r
num <- 1:6
ifelse(num %% 2 == 0, yes = "even", no = "odd")
age <- sample(20:70, 20, replace = TRUE)
res <- ifelse(age > 50, "senior", ifelse(age < 30, "young", "middle-aged"))
switch(2, "banana", "apple", "other")
age <- 40
switch((age > 50) + (age >= 30) + 1, "young", "middle-aged", "senior")
price <- function(fruit) {
  switch(fruit, apple = 10, orange = 12, grape = 16, banana = 8, 0)
}
sapply(c("apple", "orange", "grape", "grape", "other"), price)
```

```text
[1] "odd"  "even" "odd"  "even" "odd"  "even"
[1] "apple"
[1] "middle-aged"
 apple orange  grape  grape  other 
    10     12     16     16      0 
```

`switch()` is not vectorized; applied to a vector of ages it must be wrapped in `sapply()`, while `ifelse()` works on the whole vector at once.

### 2.6.3. Loops and Recursion

R provides `for`, `while` and `repeat` (with `break`). In R, modifying a variable generally requires copying it, which consumes memory and takes computation time, so variable modification inside loops can be very slow. As an example, compare three ways of judging whether each of the numbers $1,\dots,10^5$ is prime:

```r
findprime <- function(x) {
  if (x %in% c(2, 3, 5, 7)) return(TRUE)
  if (x %% 2 == 0 | x == 1) return(FALSE)
  xsqrt <- round(sqrt(x))
  xseq <- seq(from = 3, to = xsqrt, by = 2)
  if (all(x %% xseq != 0)) return(TRUE)
  else return(FALSE)
}
system.time({                            # 1: grow the result vector
  x <- NULL
  for (i in 1:1e5) {
    y <- findprime(i)
    x <- c(x, y)
  }
})
system.time({                            # 2: preallocate the result vector
  x <- logical(1e5)
  for (i in 1:1e5) {
    y <- findprime(i)
    x[i] <- y
  }
})
system.time(x <- sapply(1:1e5, findprime))   # 3: vectorized
```

On one machine the elapsed times were about $30.6$, $2.7$ and $2.3$ seconds. Growing a vector with `x <- c(x, y)` copies the whole vector at every step, so the total work grows like $n^2$; a preallocated vector is modified in place. The vectorized version is the most concise and the fastest, and it should replace loops whenever possible. If a loop must be used, define the result variable in advance. However, when the calculation steps are interdependent, as in the Fibonacci recursion $F_k=F_{k-1}+F_{k-2}$, vectorization cannot be used and only a loop can.

![Run time of computing the squares of n numbers, on log-log axes: growing the result vector inside a loop rises with slope 2, from 1e-4 seconds at n = 100 to about 15 seconds at n = 1e5, a preallocated loop rises with slope 1, and a single vectorized call is two to three orders of magnitude faster still](./plots/loop-vectorization-timing.py)

**Example 2.6.1 (A Fourfold Loop)** A master's student needed the $p\times p$ matrix

$$
\tilde\Upsilon_{jk}=\frac1n\sum_{i=1}^n\Bigl(\sum_{t\ne j,k}(1-\rho_t)\tilde X_{ij}\tilde X_{ik}\tilde X_{it}^2\hat\beta_t^2\Bigr),
$$
for $n=150$, $p=100$ and a constant $\rho_t=\rho=0.8$, and wrote four nested loops over $j,k,i,t$, which took half an hour:

```r
n <- 150; p <- 100
X.hat <- matrix(rnorm(n * p), ncol = p)
rho1 <- 0.8; beta.hat <- rep(1, p)
G2 <- matrix(rep(0, p * p), nrow = p)
for (j in 1:p) {
  for (k in 1:p) {
    for (i in 1:n) {
      for (t in 1:p) {
        if (t != j & t != k) {
          V1 <- ((1 / n) * (1 - rho1) * X.hat[i, j] *
                   X.hat[i, k] * X.hat[i, t]^2 * beta.hat[t]^2)
        } else {
          V1 <- 0
        }
        G2[j, k] <- V1 + G2[j, k]
      }
    }
  }
}
```

Replacing the innermost loop by `sapply()` over `t` and summing the contributions of the observations with `Reduce("+", lapply(1:n, G))`, where `G(i)` computes the $p\times p$ matrix of observation $i$, reduced the time to about $125$ seconds (a loop `for (i in 1:n) G2 <- G2 + G(i)` took $130$ seconds). Full vectorization goes further. With $Z_{it}=\tilde X_{it}^2\hat\beta_t^2$ and $w_i=\sum_tZ_{it}$, the inner sum is $w_i-Z_{ij}-Z_{ik}$ for $j\ne k$ and $w_i-Z_{ij}$ for $j=k$, so

$$
\tilde\Upsilon=\frac{1-\rho}{n}\Bigl(\tilde X^{\mathsf T}\operatorname{diag}(\boldsymbol{w})\tilde X-(\tilde X\circ Z)^{\mathsf T}\tilde X-\tilde X^{\mathsf T}(\tilde X\circ Z)+\operatorname{diag}\bigl(\boldsymbol{1}^{\mathsf T}(\tilde X\circ\tilde X\circ Z)\bigr)\Bigr),
$$
where $\circ$ is the elementwise product. In R this is a handful of matrix products, computed in a fraction of a second:

```r
Z <- sweep(X.hat^2, 2, beta.hat^2, "*")       # Z[i, t] = X[i, t]^2 * beta[t]^2
w <- rowSums(Z)
XZ <- X.hat * Z
G3 <- crossprod(X.hat, w * X.hat) - crossprod(XZ, X.hat) - crossprod(X.hat, XZ)
diag(G3) <- diag(G3) + colSums(X.hat * XZ)    # t = j = k was subtracted twice
G3 <- (1 - rho1) / n * G3
all.equal(G2, G3)
```

*Recursion* means that a function calls itself inside its own body. It can be seen as mathematical induction in the opposite direction, gradually breaking a big problem down into small problems:

```r
Fac1 <- function(n) {                 # recursion
  if (n == 0) return(1)
  return(n * Fac1(n - 1))
}
Fac2 <- function(n) {                 # loop
  if (n == 0) return(1)
  res <- n
  while (n > 1) {
    res <- res * (n - 1)
    n <- n - 1
  }
  return(res)
}
Fac1(10); Fac2(10)
```

```text
[1] 3628800
[1] 3628800
```

All recursive programs can be turned into loops, and recursion takes longer than loops, because every call creates a new function environment; a naive recursive Fibonacci function, `fib <- function(n) if (n <= 2) 1 else fib(n - 1) + fib(n - 2)`, even recomputes the same values exponentially many times, while a loop computes $F_{30}$ in $30$ steps. The speed ranking is

$$
\text{vectorization}>\text{loop (with preallocation)}>\text{recursion}.
$$
Recursion is appropriate when a problem decomposes naturally into subproblems and the depth is small.

## 2.7. Visualization of Multivariate Data

Visualization is the art of representing data through graphical elements. It is essential both in exploratory data analysis ("exploratory" in contrast to "confirmatory", that is, hypothesis testing) and in presenting the results of a study. Good visualizations tell the story of the data and communicate the important messages of an analysis: they show trends and patterns, reveal outliers, and suggest which questions to ask and which methods are appropriate. With multivariate data one is further interested in dimension reduction and in finding structure or groups.

### 2.7.1. Panel Displays

A panel display is an array of two-dimensional graphical summaries of pairs of variables: the *scatterplot matrix* `pairs(iris[, 1:4])` plots every pair of variables, and the conditioning plot `coplot(Y ~ X | Z, data)` plots $Y$ against $X$ for different ranges of a third variable $Z$. Coloring the points by group requires one color per observation:

```r
pairs(iris[, 1:4], col = iris$Species, lower.panel = NULL)
par(xpd = TRUE)                      # allow plotting outside the plot region
legend("bottomleft", fill = 1:3, legend = levels(iris$Species))
```

The argument `col = 1:3` would be recycled along the $150$ observations, coloring them $1,2,3,1,2,3,\dots$ regardless of species; `col = iris$Species` (a factor, used through its integer codes) or `col = c("red", "green", "blue")[iris$Species]` assigns the colors by group. The lower panels can show other summaries, such as the sample **correlation coefficients**:

![Scatterplot matrix of the four iris measurements: in the upper panels setosa (circles) is clearly separated from versicolor (triangles) and virginica (crosses) in the petal measurements, and the lower panels give the correlations, from -0.43 between sepal width and petal length to 0.96 between petal length and petal width](./plots/iris-scatterplot-matrix.py)

The overall correlation $-0.12$ between sepal length and width is a mixture effect: within each species the two are positively correlated, a reminder that panel displays should be read group by group.

### 2.7.2. Surface and Contour Plots

A function of two variables is displayed as a surface. For the **bivariate normal distribution** with independent standard normal components, the **probability density function** is $f(x,y)=\dfrac{1}{2\pi}\mathrm{e}^{-(x^2+y^2)/2}$, $(x,y)\in\mathbb{R}^2$; `outer()` evaluates it on a grid and `persp()` draws the surface:

```r
f <- function(x, y) {
  z <- (1 / (2 * pi)) * exp(-0.5 * (x^2 + y^2))
}
y <- x <- seq(-3, 3, length = 50)
z <- outer(x, y, f)                  # compute the density for all (x, y)
persp(x, y, z, theta = 45, phi = 30, col = "green", ticktype = "detailed",
      ltheta = 120, shade = 0.75, xlab = "X", ylab = "Y", zlab = "f(x, y)", expand = 0.6)
```

Interactive graphics can be rotated with the mouse. The package `rgl` draws OpenGL scenes, and `rglwidget()` produces a WebGL version for a browser; the packages `plotly`, `threejs` and `graph3D` create interactive JavaScript plots (`plot_ly()` maps R objects to plotly.js, an MIT-licensed web-based charting library):

```r
library(rgl)
persp3d(x, y, z, front = "lines", color = terrain.colors(50))
rglwidget()
M <- expand.grid(seq(-3, 3, length = 50), seq(-3, 3, length = 50))
x <- M[, 1]; y <- M[, 2]; z <- f(x, y)        # x, y, z are vectors of points
plot3d(x, y, z, col = rainbow(50), type = "l")
library(plotly)
xg <- yg <- seq(-3, 3, length = 50)
plot_ly(x = xg, y = yg, z = outer(xg, yg, f)) %>% add_surface()
library(threejs)
scatterplot3js(x, y, z, color = rainbow(length(z)), cex = 0.3)
```

A *contour plot* draws the **level curves** of the function, and `image()` uses colors to identify the levels. The built-in matrix `volcano` holds the topography of a volcano in New Zealand:

```r
contour(volcano)                                   # contour lines with labels
image(volcano, col = terrain.colors(100))          # colors identify the levels
contour(volcano, levels = seq(100, 200, by = 10), add = TRUE)
plot_ly(z = ~volcano) %>% add_surface()
```

**Example 2.7.1** Let $X$ and $Y$ be independent and identically distributed with the normal mixture distribution $p_1\mathcal{N}(0,1)+p_2\mathcal{N}(3,1)$, $p_2=1-p_1$. Their joint density is the product of the two marginal mixture densities, with four modes near $(0,0)$, $(0,3)$, $(3,0)$ and $(3,3)$. For $p_1=0.7$ the mode at $(3,3)$ has only $0.09/0.49\approx0.18$ times the height of the main mode, so the default contour levels can miss it; the levels must be adjusted to make the contours of the minor modes visible:

![Left: surface plot of the joint density of two independent 0.7 N(0, 1) + 0.3 N(3, 1) variables, with a dominant peak at the origin and three lower peaks; right: contour plot with levels from 0.002 to 0.07 over a simulated sample of 500 points, where the low levels show the minor modes at (0, 3), (3, 0) and (3, 3)](./plots/normal-mixture-surface-contour.py)

### 2.7.3. Three-Dimensional Scatterplots

Three-dimensional data are displayed with the packages `rgl`, `car`, `lattice`, `scatterplot3d` or `graph3d`, among others. With `rgl`, the iris measurements colored by species, a $95\%$ data ellipsoid for each group and the group labels are drawn by

```r
x <- iris$Sepal.Length; y <- iris$Sepal.Width; z <- iris$Petal.Length
gcol <- c("red", "green", "blue")
library(rgl)
plot3d(x, y, z, type = "s", radius = 0.15, col = gcol[as.numeric(iris$Species)],
       xlab = "sep.l", ylab = "sep.w", zlab = "pet.l")
groups <- iris$Species
levs <- levels(groups)
for (i in 1:length(levs)) {          # compute an ellipsoid for each group
  selected <- groups == levs[i]
  xx <- x[selected]; yy <- y[selected]; zz <- z[selected]
  ellips <- ellipse3d(cov(cbind(xx, yy, zz)),
                      centre = c(mean(xx), mean(yy), mean(zz)), level = 0.95)
  shade3d(ellips, col = gcol[i], alpha = 0.1)                   # show the ellipsoid
  texts3d(mean(xx), mean(yy), mean(zz), text = levs[i], col = gcol[i], cex = 2)
}
aspect3d(1, 1, 1)                    # rescale each coordinate
rglwidget()
```

In regression analysis, a fitted plane $z=a+bx+cy$ can be added to the scatterplot with `surface3d()`:

```r
plot3d(x, y, z, type = "s", radius = 0.15, col = "orange")
fit <- lm(z ~ x + y)                 # the linear regression z = a + b x + c y
x.pred <- seq(min(x), max(x), length.out = 20)
y.pred <- seq(min(y), max(y), length.out = 20)
xy <- expand.grid(x = x.pred, y = y.pred)
z.pred <- matrix(predict(fit, newdata = xy), nrow = 20, ncol = 20)
surface3d(x.pred, y.pred, z.pred, col = "steelblue", alpha = 0.5, lit = FALSE)
surface3d(x.pred, y.pred, z.pred, col = "black", alpha = 0.5, lit = FALSE,
          front = "lines", back = "lines")                        # add grid lines
movie3d(spin3d(axis = c(0, 0, 1)), duration = 10, movie = "regression", dir = getwd())
```

The last line creates an animated GIF of the rotating scene. It requires the program ImageMagick, whose `convert` utility `rgl` uses to assemble the frames; without it `movie3d()` reports that ImageMagick was not found and leaves a series of PNG files instead (on Windows, select "Install legacy utilities (e.g. convert)" during installation and restart R). Calling `plot3d()` again overwrites the current plot; elements are added with `points3d()`, `lines3d()`, `segments3d()`, `text3d()`, `abclines3d()`, `planes3d()`, `spheres3d()`, `surface3d()`, `terrain3d()`, `drape3d()`, `arrow3d()` and `pch3d()`.

## Summary

| Topic | Key facts |
|---|---|
| Objects | everything is an object; the vector is the basic structure; atomic vectors (one type) and lists (recursive) |
| Atomic types | logical, integer (`1L`), double, character (complex, raw); coercion logical $<$ integer $<$ double $<$ character |
| Missing values | `NA` (missing, any type), `NaN` (`0/0`), `NULL` (no object, length $0$) |
| Attributes | `names`, `dim`, `class` survive modification; others are lost |
| Special objects | factor = integer vector + `levels` + `class`; matrix/array = atomic vector + `dim`; data frame = list of equal-length columns |
| Operations | operators are functions (`` `*`(2, 3) ``); `&`, `\|` elementwise, `&&`, `\|\|` scalar and short-circuited; recycling; `%*%` vs `*`; `solve(A, b)` |
| Subsetting | `[` preserves (for lists), `[[` and `$` extract one element; `drop = FALSE` keeps matrix dimensions |
| Vectorization | `sapply` simplifies, `lapply` returns a list, `tapply` by groups (array), `aggregate` (data frame), `mapply` several arguments, `outer` all pairs, `ifelse`, `switch`, `Reduce` |
| Speed | vectorization $>$ preallocated loop $>$ growing vectors, recursion |
| Graphics | `pairs`, `coplot`, `persp`, `contour`, `image`; interactive `rgl`, `plotly`, `threejs` |
