---
title: 用 R 进行统计计算
description: 作为统计计算工具的 R 语言：原子向量与列表，类型、强制类型转换与属性，因子、矩阵、数组与数据框，函数与流程控制，算术运算、矩阵运算与取子集，用 apply 族函数实现向量化，循环与递归的代价，以及多维数据的可视化。
source_hash: 717e4e1301ed
---

本课程的全部计算都用 R 完成。本章汇集了可靠地用 R 进行统计计算所需的知识，重点是 R 怎样表示数据，因为 R 中的编程错误大多源于对其对象的误解：被悄悄转换成字符的向量，悄悄丢掉一个维度的矩阵，用错了括号的列表取子集。本章先介绍基本对象（向量、列表、因子、矩阵、数组、数据框、函数），再介绍对它们的基本操作（输入输出、算术运算、逻辑运算与矩阵运算、取子集），然后是向量化，即 R 避免显式循环的方式，最后是多维数据的可视化工具。R 中的浮点数已在 [3.5.1](/3.5.1) 中讨论；建立在 R 矩阵运算之上的数值线性代数见 [3.5.3](/3.5.3)。

## 2.1. R 语言概况

R 是业界领先的数据分析与统计编程环境，其宗旨是把想法快速而准确地变成软件。它源于 S 语言：S 是贝尔实验室统计研究部的 John Chambers 等人从 1976 年起开发的数据分析高级语言，S 系统于 1998 年获得美国计算机协会（ACM）的软件系统奖。R 本身由 Ross Ihaka 和 Robert Gentleman 在 20 世纪 90 年代初作为 S 的自由实现而创建，1997 年成为 GNU 项目的一部分。Hadley Wickham 的 *Advanced R*（第 2 版，可在 adv-r.hadley.nz 免费阅读）是本章内容的良好参考。

Chambers 用两句口号概括了这门语言的计算模型：

> 理解 R 中的计算，有两句口号很有帮助：存在的一切都是对象；发生的一切都是函数调用。

R 可以调用其他语言编写的代码：`.C` 和 `.Fortran` 调用编译好的 C 和 Fortran 例程（[3.5.1](/3.5.1) 的 1.2.5 节提到了这些接口使用的属性 `Csingle`），`reticulate` 包嵌入 Python，`R.matlab` 与 MATLAB 交换数据。本课程只使用 R。

## 2.2. 向量

### 2.2.1. 原子向量与列表

创建变量就是在内存中预留空间来存放值。R 不提供对计算机内存的直接访问，而是提供若干种专门的数据结构，称为对象；R 是面向对象的，意思是与 R 打交道的一切都是对象，对象的数据类型就成为变量的数据类型。常用的结构有向量、矩阵、数组、数据框和列表。最基本的数据结构是向量，R 中没有标量：标量就是长度为 $1$ 的向量。

**定义 2.2.1（原子向量、列表）** R 中的向量是元素的有序序列。若所有元素类型相同，称为**原子向量**；若元素可以是任意对象（包括其他列表），称为**列表**（递归向量）。

每个向量除了内容之外还有三个性质：类型（`typeof()`，它是什么）、长度（`length()`，含有多少个元素）和属性（attribute）（`attributes()`，附加的任意元数据）。

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

三个对象 `a`、`b`、`c` 打印出来几乎一样，实际上却不同：`a` 是原子向量，`b` 是由十个长度为 $1$ 的向量组成的列表，`c` 是一维数组，即带有 `dim` 属性的原子向量，所以 `is.vector(c)` 为 `FALSE`（只有除名字外不带其他属性的向量，`is.vector` 才为 `TRUE`）。

### 2.2.2. 原子向量的类型

原子向量有六种类型：逻辑型（logical）、整型（integer）、双精度型（double，常称数值型 numeric）、字符型（character）、复数型（complex）和原始型（raw），后两种很少用。`typeof()` 给出内部类型，`class()` 给出用于方法分派的类：

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

原子向量通常用 `c()`（combine，拼接）创建，并且总是扁平的，即使嵌套调用 `c()` 也是如此：

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

用"is"函数检验向量的类型：`is.double()`、`is.integer()`、`is.character()`、`is.logical()`，或者更一般的 `is.atomic()`。注意 `is.numeric()` 是对向量"是否为数"的一般检验，对整型和双精度向量都返回 `TRUE`：`is.numeric(int_var)` 和 `is.numeric(dbl_var)` 都是 `TRUE`。

### 2.2.3. 缺失值：NA、NaN 与 NULL

缺失值用 `NA` 表示，它是长度为 $1$ 的逻辑向量。在 `c()` 中使用时，`NA` 总会被强制转换为正确的类型；特定类型的缺失值可以用 `NA_real_`（双精度）、`NA_integer_` 和 `NA_character_` 创建。三个特殊值容易混淆：

| | `NA` | `NaN` | `NULL` |
|---|---|---|---|
| 含义 | 缺失值，占位符 | 不可能的数值，例如 `0/0` | 空对象，未定义的表达式或函数结果 |
| `class()` | `"logical"` | `"numeric"` | `"NULL"` |
| `length(c(27, 29, x))` | $3$ | $3$ | $2$ |
| `x > 1` | `NA` | `NA` | `logical(0)` |

`NaN` 就是 [3.5.1](/3.5.1) 中 IEEE 754 的"非数"（而 `1/0` 是 `Inf`）；`is.na()` 对 `NA` 和 `NaN` 都为 `TRUE`。`NULL` 的长度为 $0$，给列表的某个分量赋值 `NULL` 就把它从列表中删除。长度为零的结果很常见：`which(11 == 1:10)` 返回 `integer(0)`。

### 2.2.4. 强制类型转换

原子向量的所有元素必须是同一类型。不同类型组合在一起时，它们被转换为最灵活的类型，这种强制类型转换（coercion）遵循以下顺序：

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

强制转换常常自动发生：大多数数学函数把参数转换为双精度或整型，大多数逻辑运算转换为逻辑型。字符串与数比较时，数被转换为字符串，再按字母顺序逐个字符比较。因此 `'3L' > 2` 为 `TRUE`（`"3L"` 排在 `"2"` 之后），`'3L-5' > 2` 也为 `TRUE`，而 `'0L+3' > 2` 为 `FALSE`：引号里的表达式从不求值。同理 `'10' < '11'` 为 `TRUE`，`'9' < '11'` 却为 `FALSE`。曾有学生用 `sum(data <= x) / length(data)` 计算一个五位数 `x` 的经验分位数，却把 `x` 读成了字符串；与 `data` 中数值的比较变成了按字母顺序比较，结果 $0.16$ 而不是 $0.84$，看上去像"正确答案的补数"，那只是巧合。

当强制转换可能丢失信息时，R 通常给出警告。容易混淆时，应当用 `as.character()`、`as.double()`、`as.integer()` 或 `as.logical()` 显式转换：

```r
as.numeric(c("a", 1))
```

```text
[1] NA  1
Warning message:
NAs introduced by coercion
```

### 2.2.5. 属性

对象可以带有任意的附加属性，用来存储关于对象的元数据。属性构成一个（名字唯一的）命名列表，用 `attr()` 逐个访问，或用 `attributes()` 一次全部访问；`structure()` 返回一个属性被修改过的新对象。

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

修改向量时，大多数属性都会丢失。不会丢失的只有三个最重要的属性：

- `names`，给每个元素一个名字的字符向量；
- `dim`，用于把向量变成矩阵和数组；
- `class`，用于实现 S3 对象系统。

它们用各自的函数 `names(x)`、`dim(x)` 和 `class(x)` 读取和设置，而不是用 `attr(x, "names")`。执行 `dim(y) <- 10` 会把整型向量 `y` 变成一维数组：`is.vector(y)` 变为 `FALSE`，`class(y)` 变为 `"array"`。

给向量命名有三种方式：创建时命名，`x <- c(a = 1, b = 2, c = 3)`；修改已有的向量，`x <- 1:3; names(x) <- c("a", "b", "c")`；或者创建一个修改过的副本，`y <- setNames(x, c("m", "n", "c"))`。名字不必唯一，但最好唯一，因为按名字取子集只返回第一个匹配。并非每个元素都需要名字：创建时缺少的名字是空字符串（`names(c(a = 1, 2, 3))` 是 `"a" "" ""`）；通过修改向量只设置部分名字时，其余的名字是 `NA`（`NA_character_`）；所有名字都缺失时，`names()` 返回 `NULL`。

### 2.2.6. 列表

列表用来构建更复杂的数据结构；数据框和拟合的线性模型都是列表。列表用 `list()` 而不是 `c()` 构造；对列表使用 `c()` 会把它们合并成一个列表，并把原子向量强制转换为列表。用 `unlist()` 把列表变成原子向量，转换规则与 `c()` 相同。用 `is.list()` 检验是否为列表，用 `as.list()` 由其他对象创建列表。

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

所以 `c()` 创建的并不总是原子向量：列表与任何东西拼接，结果都是列表。

## 2.3. 因子、矩阵与数据框

### 2.3.1. 因子

属性的一个重要用途是定义因子。

**定义 2.3.1（因子）** **因子**是只能取预先规定的值的向量，用来存储分类数据。它建立在整型向量之上，带有两个属性：`class`，其值为 `"factor"`，使它的行为不同于普通整型向量；`levels`，规定允许取值的集合。

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

不在水平之中的值不能使用。当已知变量可能的取值时，即使数据集中并未出现所有取值，因子也很有用：

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

### 2.3.2. 矩阵与数组

给原子向量加上 `dim` 属性，它就成为多维数组；矩阵是二维的特例。矩阵和数组也可以用 `matrix()` 和 `array()` 创建，用 `is.matrix()` 和 `is.array()`（或看 `dim` 的长度）检验，`as.matrix()` 和 `as.array()` 把已有的向量变成矩阵或数组。元素按列依次填入。

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

向量的函数有相应的高维推广：

| 向量 | 矩阵 | 数组 |
|---|---|---|
| `length()` | `nrow()`、`ncol()` | `dim()` |
| `names()` | `rownames()`、`colnames()` | `dimnames()`（字符向量组成的列表） |
| `c()` | `cbind()`、`rbind()` | `abind()`（`abind` 包） |
| | `t()`（转置） | `aperm()`（广义转置） |

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

设置原子向量的 `dim()` 得到矩阵；设置列表的 `dim()` 得到列表矩阵（或列表数组），其单元格可以是任意对象：

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

这些较为冷僻的结构适合把对象排成网格，例如在时空网格上拟合模型时，可以把模型存放在三维数组中以保留网格结构。

### 2.3.3. 数据框

**定义 2.3.2（数据框）** **数据框**是由等长向量组成的列表，显示为以这些向量为列的表格。

数据框是 R 中最常用的数据存储方式。它的二维结构使它兼具矩阵和列表的性质：既可以像一维结构那样取子集（此时它像由列组成的列表），也可以像二维结构那样取子集（此时它像矩阵）。它的 `length()` 是底层列表的长度，所以等于 `ncol()`，`nrow()` 给出行数；它有 `names()`、`colnames()` 和 `rownames()`，其中 `names()` 与 `colnames()` 相同。与矩阵不同，数据框的各列可以是不同类型。

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

每个列表都是向量（`is.vector(list(1))` 为 `TRUE`），但数据框不是，因为它有 `class` 和 `row.names` 属性。数据框用 `cbind()` 按列合并（行数必须一致，行名被忽略），用 `rbind()` 按行合并（列数和列名都必须一致）；`plyr::rbind.fill()` 可以合并列不相同的数据框。

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

**例 2.3.1** 下面两个数据框打印出来完全一样，逐元素比较也相等：

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

但它们并不相同。`cbind()` 先创建一个矩阵，而矩阵只有一种类型，于是数 $1,2$ 被转换为字符串 `"1"`、`"2"`，列 `Left$a` 是字符向量，`Right$a` 是整型向量。比较运算 `==` 又做了一次强制转换（`'1' == 1` 为 `TRUE`），掩盖了差别。一言以蔽之：强制类型转换。应当像 `Right` 那样直接把各列传给 `data.frame()`。

## 2.4. 函数与流程控制

### 2.4.1. 函数

R 中的函数是"一等对象"：可以像其他对象一样被赋值、作为参数传递和作为结果返回。R 软件以函数式风格编写，这既有助于理解意图，也有助于保证实现与意图一致。与函数式风格自然互补的是对象的类的定义：函数应当封装分析中的动作，类应当封装函数调用所使用和返回的对象的性质。函数调用与对象的对偶是用 R 编程反复出现的主题。

随机模拟中经常用到两个函数。`sample()` 抽取随机样本，下面分别是对数据框 `dat` 的行做不放回和有放回抽样；`set.seed()` 使伪随机数可以重现（[3.5.8](/3.5.8)）：

```r
dat[sample(1:nrow(dat), 100), ]                 # without replacement
dat[sample(1:nrow(dat), replace = TRUE), ]      # with replacement (a bootstrap sample)
```

`replicate(n, expr)` 把一个表达式求值 `n` 次并简化结果。`replicate(100, mean(rnorm(1000)))` 生成 $1000$ 个标准正态随机数并计算其均值，把这个过程重复 $100$ 次，返回 $100$ 个均值组成的向量；`replicate(10, rnorm(20))` 返回 $20\times10$ 矩阵，每列是一个样本。

好的函数检查参数、提供灵活性、在最后返回值，并且缩进整齐、带有注释：

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

参数 `...` 是一扇"后门"：没有按名字匹配的参数被传递下去，这里是把 `trim = 0.1` 传给 `mean()`，于是计算截尾均值。

### 2.4.2. 流程控制

条件语句的形式是 `if (cond) statement` 和 `if (cond) statement1 else statement2`，语句可以是花括号括起的代码块。在脚本或控制台的顶层，`else` 必须与 `if` 代码块的右花括号写在同一行：

```r
if (cond) {
  statement1
} else {               # correct
  statement2
}
```

如果 `statement1` 结束一行而 `else` 另起一行，解释器在第一行末就认为 `if` 语句已经完整，于是在 `else` 处报错（在函数体的花括号内换行无妨，但花括号的写法更稳妥）。`if` 只接受单个条件；向量化的 `ifelse()` 是另一个函数（2.6.2 节）。循环写作 `for (var in seq) statement`、`while (cond) statement` 和 `repeat statement`（用 `break` 跳出）。显式循环在 R 中很慢，只要可能就应改用向量化运算（2.6 节）。

`return` 是函数，它的参数必须放在括号里：

```r
check1 <- function(x, y) { if (x > y) return TRUE else return FALSE }
check2 <- function(x, y) { return(x > y) }
check3 <- function(x, y) { if (x > y) TRUE else FALSE }
check4 <- function(x, y) return({ if (x > y) TRUE else FALSE })
```

```text
Error: unexpected numeric constant in "check1 <- function(x, y) { if (x > y) return TRUE"
```

`check1` 是语法错误，因为 `return TRUE` 不是函数调用；`check2`、`check3`、`check4` 都是正确的。函数返回最后求值的表达式的值，所以 `check3` 不需要 `return`；`if` 本身也是有值的表达式，`check4` 把它的值传给了 `return()`。

## 2.5. 基本操作

### 2.5.1. 输入输出

表格数据是统计分析中最主要的数据格式。`read.table()` 和 `write.table()` 读写表格文本文件；`read.csv()` 和 `read.delim()` 与 `read.table()` 相同，只是默认参数不同：`read.csv()` 用于逗号分隔值文件（`.csv`，默认 `header = TRUE`、`sep = ","`），`read.delim()` 用于制表符分隔的文本。

```r
a <- file.choose()                        # choose a csv file interactively
x <- read.csv(a)                          # header = TRUE by default
df <- read.table(a, sep = ",", header = TRUE)
write.csv(x, file = "foo.csv")
```

R 对象用 `save()` 以二进制 `.RData` 格式保存，用 `load()` 恢复；`save.image()` 是"保存当前工作空间"的快捷方式，即 `save(list = ls(all.names = TRUE), file = ".RData")`。`.RData` 文件经过压缩，节省空间，并且不需要解析文本，加载很快。

```r
x <- runif(20)
y <- list(a = 1, b = TRUE, c = "oops")
save(x, y, file = "xy.RData")
save.image()            # creates ".RData" in the current working directory
unlink("xy.RData")      # deletes files and directories
```

### 2.5.2. 算术运算与逻辑运算

| 运算符 | 含义 | 运算符 | 含义 |
|---|---|---|---|
| `+` | 加 | `!` | 逻辑非 |
| `-` | 减 | `&` | 逐元素逻辑与 |
| `*` | 乘 | `&&` | 标量逻辑与，短路求值 |
| `/` | 除 | `\|` | 逐元素逻辑或 |
| `^` | 乘方 | `\|\|` | 标量逻辑或，短路求值 |
| `%%` | 取模（余数） | | |
| `%/%` | 整除 | | |

基本算术函数有 `log()`、`log2()`、`log10()`、`exp()`，三角函数 `cos()`、`sin()`、`tan()`、`acos()`、`asin()`、`atan()`，以及 `abs()`、`sqrt()`。用 `<-`（或 `=`）赋值：`x <- 2; y = 3`。

每个运算符都是函数，可以用反引号或引号括起它的名字来调用：`2 * 3` 就是调用 `` `*`(2, 3) ``（也可写作 `'*'(2, 3)`），`x[1]` 就是 `` `[`(x, 1) ``。

逻辑运算符把数强制转换为逻辑值（零为 `FALSE`，其余为 `TRUE`）：

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

在 `A && B` 中，只有 `A` 为 `TRUE` 时才计算 `B`；在 `A || B` 中，只有 `A` 为 `FALSE` 时才计算 `B`。标量运算符用于 `if` 和 `while` 的条件；自 R 4.3.0 起，操作数长度大于 $1$ 时它们会报错。

### 2.5.3. 向量运算与矩阵运算

向量的算术运算是逐元素的，较短的向量被循环使用，这一规则称为循环回收（recycling）；当较长的长度不是较短长度的整数倍时，R 给出警告：

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

常用的计算有 `max()`、`min()`、`range()`、`length()`、`sort()`、`sum()`、`prod()`、`mean()`、`sd()` 和 `var()`。

对矩阵，`t()` 转置，`diag(v)` 生成对角矩阵；`solve(A, b)` 求解线性方程组 $A\boldsymbol{x}=\boldsymbol{b}$，`solve(A)` 返回逆矩阵。函数名叫 `solve`，是因为（通过 LU 分解，[3.5.3](/3.5.3)）解方程组比先求 $A^{-1}$ 再相乘更便宜也更准确，所以应当写 `solve(A, b)` 而不是 `solve(A) %*% b`。其他指标有行列式 `det()`、特征值与特征向量 `eigen()`、迹 `sum(diag(M))` 和秩 `qr(M)$rank`。矩阵乘法是 `%*%`；运算符 `+ - * / ^` 都是逐元素的。两个矩阵之间的逐元素运算要求维数相同；矩阵与向量之间，向量沿列循环使用，矩阵的长度必须是向量长度的整数倍。

**例 2.5.1** 设 `A <- matrix(1:4, 2, 2)`，即 $A=\begin{bmatrix}1&3\\2&4\end{bmatrix}$，`b <- c(1, 2)`。则

| 命令 | 结果 |
|---|---|
| `out1 <- A %*% b` | $2\times1$ 矩阵 $(7,10)^{\mathsf T}$：向量被当作列向量 |
| `out2 <- b %*% A` | $1\times2$ 矩阵 $(5,11)$：向量被当作行向量 |
| `out3 <- A * b` | $\begin{bmatrix}1&3\\4&8\end{bmatrix}$：`b` 沿列循环使用 |
| `out4 <- b * A` | 与 `out3` 相同 |
| `out5 <- t(b) %*% A` | $1\times2$ 矩阵 $(5,11)$，与 `out2` 相同 |
| `out6 <- t(b) * A` | 报错：non-conformable arrays（$1\times2$ 与 $2\times2$） |
| `out7 <- A %*% t(b)` | 报错：non-conformable arguments（$2\times2$ 乘 $1\times2$） |

所以 `out3 == out4` 和 `out2 == out5` 逐元素为 `TRUE`，而 `out1 == out2` 报错，因为 $2\times1$ 矩阵与 $1\times2$ 矩阵是维数不相容的数组。

**例 2.5.2** 设 $M$ 是 $n\times n$ 矩阵，$\boldsymbol{z}$ 是长度为 $n$ 的向量。代码

```r
(M %*% z %*% t(M %*% z)) / (t(z) %*% M %*% z)
```

本意是计算 $\dfrac{M\boldsymbol{z}(M\boldsymbol{z})^{\mathsf T}}{\boldsymbol{z}^{\mathsf T}M\boldsymbol{z}}$，却会报错：分母是 $1\times1$ 矩阵而不是数，$n\times n$ 矩阵除以 $1\times1$ 矩阵是维数不相容的运算。此外 $M\boldsymbol{z}$ 被计算了两次。改正的写法把分母变成标量，并重复使用 $M\boldsymbol{z}$：

```r
v <- M %*% z
tcrossprod(v) / drop(crossprod(z, v))     # v v^T / (z^T v)
```

### 2.5.4. 取子集

取子集就是选取或排除变量和观测。取子集有四种方式，下面以 `x <- 1:10` 和数据框 `airquality` 为例：

| 方式 | 例子 |
|---|---|
| 按位置 | `x[4]`、`x[-4]`（除第四个以外的全部）、`x[2:4]`、`x[-(2:4)]` 或 `x[-2:-4]`、`x[c(1, 2, 5)]` |
| 按条件（逻辑向量） | `x[x == 10]`、`x[x < 0]`、`x[x %in% c(1, 2, 5)]` |
| 按名字 | `airquality[, "Ozone"]`、`airquality$Ozone`、`airquality[, c("Wind", "Temp")]` |
| 用 `subset()` | `subset(airquality, Temp > 80, select = c(Ozone, Temp))` |

位置和条件是两回事：对 `x <- 3:10`，`x[c(1, 2, 5)]` 给出第一、第二、第五个元素 `3 4 7`，而 `x[x %in% c(1, 2, 5)]` 给出值为 $1$、$2$ 或 $5$ 的元素，即 `5`。另外，`$` 只适用于递归对象：执行 `x <- c(1, 2); names(x) <- c("Bob", "Ed")` 之后，`x$Ed` 会报错（"$ operator is invalid for atomic vectors"），应当用 `x["Ed"]` 或 `x[["Ed"]]`。

一般规则是：向量和因子用 `[i]`，矩阵和数据框用 `[i, j]`，列表和数据框用 `[[i]]`。如果把列表 `x` 看作一列装载对象的火车，那么 `x[1:3]` 是由第 $1$–$3$ 节车厢组成的火车，而 `x[[1]]` 是第 $1$ 节车厢里装的对象。

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

对 `x <- list(list(1, 2), c(3, 4))`，要把元素 `2` 作为数取出，应写 `x[[1]][[2]]`；`x[[1]][2]` 是长度为 $1$ 的列表，`x[1][2]` 则是一个含有 `NULL` 的列表。

**例 2.5.3（当心降维）** 为验证正定矩阵的顺序主子式全为正，考虑

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

当 `i = 1` 时，`M[1:1, 1:1]` 不是 $1\times1$ 矩阵，而是数 `2`：取子集会丢掉所有长度为 $1$ 的维度，而 `det()` 只接受矩阵（`det(M[1, 1])` 给出同样的错误）。向量、单行或单列的矩阵、单列的数据框和一维数组看起来都差不多，R 会悄悄地在它们之间转换。改正的方法是 `det(M[1:i, 1:i, drop = FALSE])`；`class(M[1, 1, drop = FALSE])` 是 `"matrix" "array"`，`det(as.matrix(M[1, 1]))` 也可以。改正后函数返回 `2 3 4`。

取子集或者把结果简化为尽可能简单的结构，或者保留输入的结构。保留对所有数据类型都一样；简化的行为则略有不同：

| | 简化 | 保留 |
|---|---|---|
| 向量 | `x[[1]]`（去掉名字） | `x[1]` |
| 列表 | `x[[1]]`（列表里的对象，而非单元素列表） | `x[1]` |
| 因子 | `x[1:4, drop = TRUE]`（去掉未用到的水平） | `x[1:4]` |
| 矩阵或数组 | `x[, 1]`、`x[1, ]`（去掉长度为 $1$ 的维度） | `x[, 1, drop = FALSE]`、`x[1, , drop = FALSE]` |
| 数据框 | `x[, 1]`、`x[[1]]`（结果只有一列时返回向量） | `x[, 1, drop = FALSE]`、`x[1]` |

从数据框中选取单独一列时，矩阵式取子集默认简化，列表式取子集则不简化：

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

对数据框 `iris`，`iris$Sepal.Width`、`iris[2]`、`iris[[2]]` 和 `iris[, 2]` 四个表达式选取的是同一列；除了 `iris[2]` 是单列数据框之外，其余三个返回同一个数值向量。

## 2.6. 向量化

### 2.6.1. 二元运算符与 Reduce

表达式 `1:4 * 4:1` 就是调用 `'*'(1:4, 4:1)`。二元运算符可以自定义：任何名为 `%name%` 的函数都可以写成中缀形式。

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

涉及两个以上的参数时，`Reduce(f, list)` 依次应用二元函数，$f(f(x_1,x_2),x_3)$，依此类推，使代码简洁。注意运算符名字中的引号和百分号。

### 2.6.2. Vectorize 与 apply 族函数

向量化（vectorization）指把计算写成对整个向量的运算，而不是对元素的循环。考虑一个判断数是否为偶数的函数：

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

`if` 只接受单个条件。`Vectorize()` 把函数变成接受向量的函数，`funcv <- Vectorize(func); funcv(vec)`，`sapply()` 则逐元素应用它；当然在这里，向量化的表达式 `vec %% 2 == 0` 最简单。

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

Fisher（Anderson）的 `iris` 数据集给出了 $3$ 种鸢尾花各 $50$ 朵的四个变量（花萼长、宽与花瓣长、宽）的测量值，单位为厘米；上面的代码计算了每个测量的**样本变异系数**。`sapply()` 适用于向量、数据框和列表。`lapply()` 做同样的计算但返回列表，而 `sapply()` 在可能时把结果简化为向量或矩阵：

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

（`b` 是列表，而每个列表都是向量。）`tapply()` 按索引对数据分组，对每组应用函数，返回数组；`aggregate()` 与之类似，但返回数据框，并且参数 `by` 必须是列表：

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

`tapply()` 返回数组而不是向量，是因为索引可以是由若干个因子组成的列表，此时结果对每个因子各有一个维度：

```r
index1 <- rep(c("A", "B", "C"), each = 3)
index2 <- rep(c("X", "Y", "Z"), 3)
value <- sample(1:100, 9)
SEdata <- data.frame(index1, index2, value)
tapply(SEdata$value, list(SEdata$index1, SEdata$index2), max)        # a 3 x 3 table
aggregate(SEdata$value, list(SEdata$index1, SEdata$index2), max)    # a data frame with 9 rows
```

`apply(X, MARGIN, FUN)` 把矩阵计算按行（`MARGIN = 1`）或按列（`MARGIN = 2`）向量化：

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

对数据框使用 `apply()` 要小心，因为它先用 `as.matrix()` 转换数据框，含有字符列的数据框会变成字符矩阵，其中的数被格式化为相同的小数位数。要删除所有含 $-1$ 的行：

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

第二次调用什么也没有删除：每一行都是 `"b" "-1.00000"` 这样的字符向量，`-1 %in% row` 比较的是字符串 `"-1"` 与 `"-1.00000"`（`'-1' %in% '-1'` 为 `TRUE`，`'-1' %in% '-1.000000'` 为 `FALSE`）。直接处理数值列就能避免这个问题：`x[x$score != -1, ]`、`x[!sapply(x[, 2], function(v) -1 %in% v), ]`，或者 `x[x == -1] <- NA; na.omit(x)`。

`mapply()` 是 `sapply()` 的多元版本：它把多元函数 $f(x_1,x_2,\dots)$ 逐元素地应用于若干个向量；`MoreArgs` 提供不参与向量化的参数。

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

（`mapply(rep, 1:4, 4:1)` 按位置匹配参数，即 `x = 1:4, times = 4:1`。）两个参数都从 $1$ 变到 $9$ 的九九乘法表，可以用 `mapply()` 对 `expand.grid()` 生成的所有组合（一个数据框）计算；当只有两个参数时，也可以用 `outer()`，它把向量化函数应用于所有的数对并返回矩阵：

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

条件判断用 `ifelse(test, yes, no)` 向量化，其值从 `yes` 和 `no` 中循环取得；多分支用 `switch()`。`switch()` 的第一个参数若是数，就返回相应位置的参数；若是字符串，就与后面参数的名字精确匹配，最后一个不带名字的参数作为默认值。

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

`switch()` 不是向量化的；要应用于年龄向量，必须套上 `sapply()`，而 `ifelse()` 可以一次处理整个向量。

### 2.6.3. 循环与递归

R 提供 `for`、`while` 和 `repeat`（配合 `break`）。在 R 中修改变量一般需要复制它，这既消耗内存又耗费计算时间，所以在循环中修改变量可能非常慢。作为例子，比较判断 $1,\dots,10^5$ 中每个数是否为素数的三种写法：

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

在一台机器上，三者的运行时间约为 $30.6$、$2.7$ 和 $2.3$ 秒。用 `x <- c(x, y)` 扩展向量，每一步都要复制整个向量，总工作量按 $n^2$ 增长；预先分配好的向量则可以原地修改。向量化的写法最简洁也最快，只要可能就应当用它代替循环。如果必须用循环，应事先定义好结果变量。不过，当计算步骤相互依赖时，例如 Fibonacci 递推 $F_k=F_{k-1}+F_{k-2}$，就不能向量化，只能用循环。

![计算 n 个数的平方所需的时间（双对数坐标）：在循环中扩展结果向量，斜率为 2，从 n = 100 时的 1e-4 秒增长到 n = 1e5 时的约 15 秒；预先分配的循环斜率为 1；单次向量化调用还要再快两到三个数量级](./plots/loop-vectorization-timing.py)

**例 2.6.1（四重循环）** 一位硕士生需要计算 $p\times p$ 矩阵

$$
\tilde\Upsilon_{jk}=\frac1n\sum_{i=1}^n\Bigl(\sum_{t\ne j,k}(1-\rho_t)\tilde X_{ij}\tilde X_{ik}\tilde X_{it}^2\hat\beta_t^2\Bigr),
$$
其中 $n=150$，$p=100$，$\rho_t=\rho=0.8$ 为常数。他写了对 $j,k,i,t$ 的四重嵌套循环，运行了半小时：

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

把最内层循环换成对 `t` 的 `sapply()`，再用 `Reduce("+", lapply(1:n, G))` 把各观测的贡献相加（其中 `G(i)` 计算观测 $i$ 对应的 $p\times p$ 矩阵），时间降到约 $125$ 秒（用循环 `for (i in 1:n) G2 <- G2 + G(i)` 需要 $130$ 秒）。完全向量化还能更进一步。记 $Z_{it}=\tilde X_{it}^2\hat\beta_t^2$，$w_i=\sum_tZ_{it}$，则内层和在 $j\ne k$ 时为 $w_i-Z_{ij}-Z_{ik}$，在 $j=k$ 时为 $w_i-Z_{ij}$，所以

$$
\tilde\Upsilon=\frac{1-\rho}{n}\Bigl(\tilde X^{\mathsf T}\operatorname{diag}(\boldsymbol{w})\tilde X-(\tilde X\circ Z)^{\mathsf T}\tilde X-\tilde X^{\mathsf T}(\tilde X\circ Z)+\operatorname{diag}\bigl(\boldsymbol{1}^{\mathsf T}(\tilde X\circ\tilde X\circ Z)\bigr)\Bigr),
$$
其中 $\circ$ 表示逐元素乘积。在 R 中这只是几次矩阵乘法，不到一秒就能算完：

```r
Z <- sweep(X.hat^2, 2, beta.hat^2, "*")       # Z[i, t] = X[i, t]^2 * beta[t]^2
w <- rowSums(Z)
XZ <- X.hat * Z
G3 <- crossprod(X.hat, w * X.hat) - crossprod(XZ, X.hat) - crossprod(X.hat, XZ)
diag(G3) <- diag(G3) + colSums(X.hat * XZ)    # t = j = k was subtracted twice
G3 <- (1 - rho1) / n * G3
all.equal(G2, G3)
```

递归（recursion）指函数在自身的函数体内调用自己。它可以看作反方向的数学归纳法，把大问题逐步分解成小问题：

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

所有递归程序都可以改写成循环，而且递归比循环耗时，因为每次调用都要创建新的函数环境；朴素的递归 Fibonacci 函数 `fib <- function(n) if (n <= 2) 1 else fib(n - 1) + fib(n - 2)` 甚至要把同样的值重复计算指数多次，而循环只需 $30$ 步就能算出 $F_{30}$。速度的排序是

$$
\text{向量化}>\text{循环（预先分配）}>\text{递归}.
$$
当问题可以自然地分解成子问题、且递归深度不大时，递归才是合适的。

## 2.7. 多维数据可视化

可视化是用图形元素表示数据的艺术。它在探索性数据分析（"探索性"是与"验证性"即假设检验相对而言的）和展示研究结果中都必不可少。好的可视化讲述数据的故事，传达分析的重要信息：它显示趋势和模式，揭示离群点，提示应当提出哪些问题、使用哪些方法。对多维数据，人们还关心降维以及发现数据中的结构或类群。

### 2.7.1. 面板展示

面板展示是由变量两两之间的二维图形摘要组成的阵列：散点图矩阵（scatterplot matrix）`pairs(iris[, 1:4])` 画出每一对变量，条件图 `coplot(Y ~ X | Z, data)` 对第三个变量 $Z$ 的不同范围画出 $Y$ 对 $X$ 的图。按组给点着色时，每个观测需要一种颜色：

```r
pairs(iris[, 1:4], col = iris$Species, lower.panel = NULL)
par(xpd = TRUE)                      # allow plotting outside the plot region
legend("bottomleft", fill = 1:3, legend = levels(iris$Species))
```

参数 `col = 1:3` 会沿 $150$ 个观测循环使用，把它们依次着色为 $1,2,3,1,2,3,\dots$，与种类无关；`col = iris$Species`（因子，通过其整数编码使用）或 `col = c("red", "green", "blue")[iris$Species]` 才是按组分配颜色。下三角的面板可以显示其他摘要，例如样本**相关系数**：

![鸢尾花四个测量的散点图矩阵：上三角面板中，setosa（圆圈）在花瓣测量上与 versicolor（三角形）和 virginica（加号）明显分开；下三角面板给出相关系数，从花萼宽与花瓣长之间的 -0.43 到花瓣长与花瓣宽之间的 0.96](./plots/iris-scatterplot-matrix.py)

花萼长与花萼宽的总体相关系数 $-0.12$ 是混合的结果：在每个种类内部两者都是正相关的。这提醒我们，面板展示应当分组来读。

### 2.7.2. 曲面图与等高线图

二元函数可以画成曲面。对两个分量独立、均服从标准正态的**二元正态分布**，**概率密度**为 $f(x,y)=\dfrac{1}{2\pi}\mathrm{e}^{-(x^2+y^2)/2}$，$(x,y)\in\mathbb{R}^2$；用 `outer()` 在网格上计算它，用 `persp()` 画出曲面：

```r
f <- function(x, y) {
  z <- (1 / (2 * pi)) * exp(-0.5 * (x^2 + y^2))
}
y <- x <- seq(-3, 3, length = 50)
z <- outer(x, y, f)                  # compute the density for all (x, y)
persp(x, y, z, theta = 45, phi = 30, col = "green", ticktype = "detailed",
      ltheta = 120, shade = 0.75, xlab = "X", ylab = "Y", zlab = "f(x, y)", expand = 0.6)
```

交互式图形可以用鼠标旋转。`rgl` 包绘制 OpenGL 场景，`rglwidget()` 生成可在浏览器中查看的 WebGL 版本；`plotly`、`threejs` 和 `graph3D` 包创建交互式 JavaScript 图形（`plot_ly()` 把 R 对象映射到 plotly.js，这是一个采用 MIT 许可证的网页图表库）：

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

等高线图（contour plot）画出函数的**等值线**，`image()` 用颜色区分各个水平。内置矩阵 `volcano` 记录了新西兰一座火山的地形：

```r
contour(volcano)                                   # contour lines with labels
image(volcano, col = terrain.colors(100))          # colors identify the levels
contour(volcano, levels = seq(100, 200, by = 10), add = TRUE)
plot_ly(z = ~volcano) %>% add_surface()
```

**例 2.7.1** 设 $X$ 与 $Y$ 独立同分布，服从正态混合分布 $p_1\mathcal{N}(0,1)+p_2\mathcal{N}(3,1)$，$p_2=1-p_1$。它们的联合密度是两个边缘混合密度的乘积，在 $(0,0)$、$(0,3)$、$(3,0)$ 和 $(3,3)$ 附近有四个众数。当 $p_1=0.7$ 时，$(3,3)$ 处的峰高只有主峰的 $0.09/0.49\approx0.18$ 倍，默认的等高线水平可能漏掉它；必须调整水平，才能让次要众数的等高线显示出来：

![左：两个独立的 0.7 N(0, 1) + 0.3 N(3, 1) 变量的联合密度曲面图，原点处有一个主峰和三个较低的峰；右：叠加在 500 个模拟样本点上的等高线图，水平从 0.002 到 0.07，较低的水平显示出 (0, 3)、(3, 0) 和 (3, 3) 处的次要众数](./plots/normal-mixture-surface-contour.py)

### 2.7.3. 三维散点图

三维数据可以用 `rgl`、`car`、`lattice`、`scatterplot3d`、`graph3d` 等包显示。用 `rgl` 画出按种类着色的鸢尾花测量值、每组的 $95\%$ 数据椭球和组标签：

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

在回归分析中，可以用 `surface3d()` 把拟合平面 $z=a+bx+cy$ 加到散点图上：

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

最后一行生成旋转场景的 GIF 动画。它需要 ImageMagick 程序，`rgl` 用其中的 `convert` 工具拼接各帧；没有它时 `movie3d()` 报告找不到 ImageMagick，只留下一系列 PNG 文件（在 Windows 上安装时要勾选"Install legacy utilities (e.g. convert)"，然后重启 R）。再次调用 `plot3d()` 会覆盖当前图形；添加元素可以用 `points3d()`、`lines3d()`、`segments3d()`、`text3d()`、`abclines3d()`、`planes3d()`、`spheres3d()`、`surface3d()`、`terrain3d()`、`drape3d()`、`arrow3d()` 和 `pch3d()`。

## 小结

| 主题 | 要点 |
|---|---|
| 对象 | 一切都是对象；向量是基本结构；原子向量（单一类型）与列表（递归） |
| 原子类型 | 逻辑型、整型（`1L`）、双精度型、字符型（以及复数型、原始型）；强制转换顺序 logical $<$ integer $<$ double $<$ character |
| 缺失值 | `NA`（缺失，任意类型）、`NaN`（`0/0`）、`NULL`（无对象，长度 $0$） |
| 属性 | `names`、`dim`、`class` 在修改后保留，其他属性丢失 |
| 特殊对象 | 因子 = 整型向量 + `levels` + `class`；矩阵/数组 = 原子向量 + `dim`；数据框 = 等长列组成的列表 |
| 运算 | 运算符都是函数（`` `*`(2, 3) ``）；`&`、`\|` 逐元素，`&&`、`\|\|` 标量且短路；循环回收；`%*%` 与 `*`；`solve(A, b)` |
| 取子集 | `[` 保留结构（对列表），`[[` 和 `$` 取出单个元素；`drop = FALSE` 保留矩阵维度 |
| 向量化 | `sapply` 简化，`lapply` 返回列表，`tapply` 分组（数组），`aggregate`（数据框），`mapply` 多参数，`outer` 所有数对，`ifelse`、`switch`、`Reduce` |
| 速度 | 向量化 $>$ 预先分配的循环 $>$ 扩展向量、递归 |
| 图形 | `pairs`、`coplot`、`persp`、`contour`、`image`；交互式的 `rgl`、`plotly`、`threejs` |
