---
title: pandas：表格数据
description: 用 pandas 3 处理 Python 中的表格数据：Series、DataFrame 与索引，文件读写，缺失值，整洁数据与重塑，用 groupby 做拆分-应用-合并，连接，写时复制语义，以及 polars 简介。
source_hash: 652ee4cd8c93
---

计算生物学中的大多数数据都以表格的形式出现：每个样本一行的样本表，每个基因一行的计数矩阵，每个孔与时间点一行的酶标仪导出文件。**N 维数组**（[4.4.2](/4.4.2)）只有在每一列类型相同、且行列的含义由程序员自己记住时才能存放这类数据。pandas 补上了缺少的两样东西：类型各异的列，以及附着在行与列上、随数据穿过每一步运算的*标签*。本章讲解 pandas 的核心（对象、输入输出、缺失值、重塑、分组与连接），讲解决定 pandas 3 中赋值含义的写时复制模型，最后介绍设计思路不同的较新的库 polars。pandas DataFrame 在 R 中对应的是 [3.5.2](/3.5.2) 的**数据框**；对这些表格施用的统计方法在统计学课程中展开（回归见 [3.3](/3.3)，多元分析见 [3.4](/3.4)），下一章则把表格画成图。

下文所有输出均由 pandas 3.0.6、NumPy 2.5.4 和 PyArrow 26.0.0 在 CPython 3.14.5 上得到。pandas 3.0（2026 年 1 月）改变了两项默认行为，而旧教程和网上的许多回答仍与之相悖：字符串有了专用的 `str` **数据类型对象**，写时复制始终开启（§5.7）。为 pandas 2 写的代码多数可以原样运行，但依赖链式赋值的代码会悄悄失效。

## 5.1. Series 与 DataFrame

### 5.1.1. Series

**定义 5.1.1（pandas Series）** `Series` 是由单一 dtype 的值与等长的标签数组（即**索引**）以及一个可选的名称组成的一维数组。

索引使 `Series` 区别于 NumPy 的 **N 维数组**。元素既可以按标签选取，也可以按位置选取，布尔掩码与 NumPy 中一样选出子集：

```python
import numpy as np
import pandas as pd

tpm = pd.Series([12.1, 3.4, 850.2, 0.0],
                index=["BRCA1", "TP53", "GAPDH", "MYC"], name="tpm")
print(tpm)
print(tpm["TP53"], tpm.iloc[0])          # by label, by position
print(tpm[tpm > 5].index.tolist())       # Boolean mask
```

```text
BRCA1     12.1
TP53       3.4
GAPDH    850.2
MYC        0.0
Name: tpm, dtype: float64
3.4 12.1
['BRCA1', 'GAPDH']
```

两个 `Series` 之间的二元运算按标签而不是按位置匹配元素：结果的索引是两者索引的并集，只出现在一个操作数中的标签得到缺失值。这种索引对齐（index alignment）既是 pandas 方便之处的主要来源，也是令人意外之处的主要来源。

```python
other = pd.Series([1.0, 2.0, 3.0], index=["MYC", "TP53", "EGFR"])
print(tpm + other)
```

```text
BRCA1    NaN
EGFR     NaN
GAPDH    NaN
MYC      1.0
TP53     5.4
dtype: float64
```

确实需要按位置运算时，用 `.to_numpy()` 显式转换；标签本应一致时，要去检查（`tpm.index.equals(other.index)`），而不要相信两个文件中基因的顺序相同。

### 5.1.2. DataFrame

**定义 5.1.2（DataFrame）** **DataFrame** 是二维表格，其各列是共用同一行索引的 `Series`；列标签构成第二个索引。不同的列可以有不同的 dtype。

DataFrame 通常由列的字典构建，或从文件读入（§5.2）。下面是一次生长实验的样本表，本章通篇使用：

```python
growth = pd.DataFrame({
    "well": ["A1", "A2", "A3", "B1", "B2", "B3"],
    "strain": ["WT", "WT", "WT", "mutA", "mutA", "mutA"],
    "time_h": [0, 12, 24, 0, 12, 24],
    "od600": [0.05, 0.62, 1.18, 0.05, 0.31, np.nan],
})
print(growth)
print(growth.dtypes)
```

```text
  well strain  time_h  od600
0   A1     WT       0   0.05
1   A2     WT      12   0.62
2   A3     WT      24   1.18
3   B1   mutA       0   0.05
4   B2   mutA      12   0.31
5   B3   mutA      24    NaN
well          str
strain        str
time_h      int64
od600     float64
dtype: object
```

这里没有给出行标签，所以索引是默认的 `RangeIndex` $0, 1, \dots, 5$。文本列的 dtype 是 `str`：自 pandas 3.0 起，字符串存放在专用的字符串 dtype 中（装有 PyArrow 时由其支撑，否则由 NumPy 的 object 数组支撑），而不再是早期版本通用的 `object` dtype。用 `dtype == object` 来找出文本列的代码必须改为 `pd.api.types.is_string_dtype(...)`。

| 属性或方法 | 返回 |
|---|---|
| `df.shape`、`len(df)` | （行数，列数），行数 |
| `df.columns`、`df.index` | 列标签，行标签 |
| `df.dtypes`、`df.info()` | 每一列的 dtype；dtype、非缺失值个数与内存占用 |
| `df.head(n)`、`df.tail(n)`、`df.sample(n)` | 前几行、后几行或随机几行 |
| `df.describe()` | 数值列的个数、均值、标准差与四分位数 |
| `df.to_numpy()` | 以 NumPy 数组形式给出的值（统一为一种 dtype） |

### 5.1.3. 选取行与列

pandas 有两个显式的索引器，一致地使用它们时代码最清晰：

- `df.loc[rows, cols]` 按标签选取：单个标签、标签列表、标签切片（包含两个端点）或布尔掩码；
- `df.iloc[rows, cols]` 按位置选取，使用 Python 通常的左闭右开切片。

`df["col"]` 以 `Series` 返回一列，`df[["a", "b"]]` 返回子表，`df[mask]` 筛选行。对于多个条件的筛选，`query()` 读起来更自然；pandas 3.0 还增加了 `pd.col("name")`，这是对某一列的延迟引用，可以在 `assign()` 和 `loc` 中代替 `lambda`：

```python
print(growth.loc[growth["strain"] == "mutA", ["well", "od600"]])
print(growth.iloc[1:3, :2])
print(growth.query("time_h > 0 and od600 > 0.5"))
print(growth.assign(log2_od=np.log2(pd.col("od600"))).head(3))
```

```text
  well  od600
3   B1   0.05
4   B2   0.31
5   B3    NaN
  well strain
1   A2     WT
2   A3     WT
  well strain  time_h  od600
1   A2     WT      12   0.62
2   A3     WT      24   1.18
  well strain  time_h  od600   log2_od
0   A1     WT       0   0.05 -4.321928
1   A2     WT      12   0.62 -0.689660
2   A3     WT      24   1.18  0.238787
```

`assign()` 返回新的 DataFrame，`growth` 保持不变。把这类方法串联起来（`df.query(...).assign(...).groupby(...)`），就把一次分析表达为一条变换流水线，每一步都可以单独检查；在写时复制（§5.7）下，这种写法不会产生不必要的复制。

## 5.2. 数据的读写

| 格式 | 读 | 写 | 说明 |
|---|---|---|---|
| CSV、TSV | `pd.read_csv(path, sep=...)` | `df.to_csv(path, index=False)` | 文本；通用但慢，没有类型信息 |
| Parquet | `pd.read_parquet(path)` | `df.to_parquet(path)` | 二进制、列式、压缩；保留 dtype；需要 PyArrow |
| Excel | `pd.read_excel(path, sheet_name=...)` | `df.to_excel(path)` | 需要 `openpyxl`；不要把它当作中间格式 |
| Feather / Arrow IPC | `pd.read_feather(path)` | `df.to_feather(path)` | 与 R 和 polars 快速交换 |
| HDF5 | `pd.read_hdf(path, key)` | `df.to_hdf(path, key=...)` | 需要 PyTables；分层存放许多张表 |

实践中最重要的 `read_csv` 参数有：`sep`（TSV 文件用 `"\t"`）、`index_col`（把某一列用作行索引，例如基因标识符）、`usecols`（只读某些列）、`dtype`（固定标识符列的类型，使名为 `0012` 的样本不会被读成整数 12）、`na_values`（额外表示“缺失”的字符串）、`parse_dates` 和 `comment`。生物学中一个常见的错误值得专门说一句：电子表格软件会悄悄把一些基因符号转换成日期（`SEPT2`、`MARCH1`），这是 HGNC 在 2020 年为这类基因改名的原因之一，也是不要让表格经过电子表格软件的充分理由。

保存中间结果时，Parquet 是更好的默认选择：它保存 **dtype 对象**，因此重新载入的表与保存的表相等；又因为它是列式的，读取者可以只载入大文件中的几列而不必解析其余部分。给读取函数传入 `dtype_backend="pyarrow"` 会使每一列成为由 Arrow 支撑的数组（`int64[pyarrow]`、`string[pyarrow]` 等），每种类型都因而支持缺失值；默认的由 NumPy 支撑的 dtype 仍是标准选择，也是科学计算栈的其余部分所期望的。

取值只有少数几种且反复出现的列（菌株、条件、批次）可以存成 `category` dtype：它对每个不同的值只保存一次，每行保存一个整数编码，类似 R 中的因子。这样既节省内存，又固定了各水平的顺序（对绘图和模型对比很有用），还能加速分组。

## 5.3. 缺失值

缺失值（missing value）是值未知的条目：失败的测量、尚未采集的样本、某个注释中不存在的基因。pandas 在浮点列和默认的字符串列中用 `NaN` 表示它，在日期时间列中用 `NaT`，在可空扩展 dtype（`Int64`、`boolean`、由 Arrow 支撑的 dtype）中用 `pd.NA`。由于 `NaN` 是浮点值，有空缺的整数列会变成 `float64`，除非要求使用可空 dtype：

```python
print(growth["od600"].isna().sum(), growth["od600"].mean())
print(growth.dropna(subset=["od600"]).shape)
print(growth.groupby("strain")["od600"].count())
print(pd.Series([3, None, 5]).dtype, pd.Series([3, None, 5], dtype="Int64").tolist())
```

```text
1 0.442
(5, 4)
strain
WT      3
mutA    2
Name: od600, dtype: int64
float64 [3, <NA>, 5]
```

| 任务 | 方法 |
|---|---|
| 检测 | `isna()`、`notna()`；`df.isna().sum()` 按列计数 |
| 删除 | `dropna()`，可带 `subset=`、`how="all"`、`thresh=` |
| 替换 | `fillna(value)`、`ffill()`、`bfill()`、`interpolate()` |
| 汇总 | 归约默认跳过缺失值（`skipna=True`）；`count()` 统计非缺失条目 |

归约跳过缺失值既方便又危险：上面的均值是五个孔的均值而不是六个，而输出中没有任何地方说明这一点。缺失值是数据的一部分，应当明确地作出决定。只有当缺失的原因与值本身无关时（移液失误，而不是突变株生长不良导致培养物死亡），删除行才是无偏的；用均值或零来替换会压低方差、扭曲相关；测序数据中的零计数是一次观测，不是缺失值。对缺失数据的统计处理，如 [3.5.6](/3.5.6) 的 **EM 算法**，都从这一区分出发。

## 5.4. 整洁数据与重塑

### 5.4.1. 整洁数据

同样的测量结果可以排成许多种表格。基因为行、样本为列的计数矩阵紧凑，也是线性代数所需要的形式；每个（基因，样本）对占一行的表格又长又冗余，但关于它的每个问题都是一次筛选、分组或连接。Hadley Wickham 的整洁数据概念（2014）为使这些运算保持一致的布局命名。

**定义 5.4.1（整洁数据）** 若每个变量是一列，每个观测是一行，每种观测单位各自构成一张表，则称该表是**整洁数据**。每个测量值占一行、并以若干列标识它的表（这里是基因、样本、计数）采用**长格式**；把一个变量分散在多列中的表（每个样本一列计数）采用**宽格式**。

表格是否整洁取决于把什么看作观测，所以两种格式本身并无对错：绘图库（seaborn、Plotly Express、R 中的 ggplot2）和模型公式需要长格式，矩阵运算（归一化、**主成分分析**、**层次聚类**）需要宽格式，一次分析会在两者之间来回转换。样本注释（条件、批次、供体）是另一种观测单位，属于它自己的表，需要时再连接进来（§5.6）。

### 5.4.2. melt、pivot 与 stack

| 从 | 到 | 方法 |
|---|---|---|
| 宽 | 长 | `df.melt(id_vars=..., var_name=..., value_name=...)`；列索引用 `df.stack()` |
| 长 | 宽 | `df.pivot(index=..., columns=..., values=...)`（组合必须唯一）；`df.unstack()` |
| 长 | 宽，并聚合重复项 | `df.pivot_table(index=..., columns=..., values=..., aggfunc=...)` |
| 两个分类列 | 计数表 | `pd.crosstab(a, b)`，即**列联表** |

用一个有四个基因、六个样本的模拟计数矩阵来演示这一往返过程：先把矩阵 melt 成长格式，再把样本注释连接进来：

```python
rng = np.random.default_rng(0)
genes = pd.Index(["BRCA1", "TP53", "GAPDH", "MYC"], name="gene")
samples = ["S1", "S2", "S3", "S4", "S5", "S6"]
counts = pd.DataFrame(rng.poisson([[50], [20], [400], [80]], size=(4, 6)),
                      index=genes, columns=samples)
meta = pd.DataFrame({"sample": samples,
                     "condition": ["control"] * 3 + ["treated"] * 3})

long = (counts.reset_index()
        .melt(id_vars="gene", var_name="sample", value_name="count")
        .merge(meta, on="sample", how="left", validate="many_to_one"))
print(counts)
print(long.head(5))
print(long.shape)
```

```text
        S1   S2   S3   S4   S5   S6
gene                               
BRCA1   53   32   52   51   57   59
TP53    23   26   17   22   21   22
GAPDH  411  375  401  399  438  404
MYC     82   77   72   65   88   92
    gene sample  count condition
0  BRCA1     S1     53   control
1   TP53     S1     23   control
2  GAPDH     S1    411   control
3    MYC     S1     82   control
4  BRCA1     S2     32   control
(24, 4)
```

DataFrame 的索引可以有多个层级（`MultiIndex`），下一节按两个键分组的结果就是一例。`stack()` 把最内层的列层级移入行索引，`unstack()` 则相反；它们是 `melt` 和 `pivot` 基于索引的对应物。

## 5.5. 拆分-应用-合并

表格的大多数汇总有相同的形状：拆分-应用-合并（split-apply-combine），即按一个或多个键列的取值把行拆分成组，对每组独立地应用一个函数，再把结果合并成新表。在 pandas 中，拆分由 `groupby` 完成，应用什么则决定结果的形状：

| 操作 | 函数把一组映射为 | 结果 | 例 |
|---|---|---|---|
| 聚合 `agg` | 一个值 | 每组一行 | 每个基因与条件的平均计数 |
| 变换 `transform` | 等长的结果 | 与输入行数相同 | 在每个样本内部归一化 |
| 过滤 `filter` | `True` / `False` | 输入行的一个子集 | 保留在每个样本中都表达的基因 |
| `apply` | 任意 | 视情况而定 | 备用；通常较慢 |

```python
print(long.groupby(["gene", "condition"])["count"].agg(["mean", "std", "size"]))
print(long.groupby("gene").agg(total=("count", "sum"),
                               n_samples=("sample", "nunique")))
```

```text
                       mean        std  size
gene  condition                             
BRCA1 control     45.666667  11.846237     3
      treated     55.666667   4.163332     3
GAPDH control    395.666667  18.583146     3
      treated    413.666667  21.221059     3
MYC   control     77.000000   5.000000     3
      treated     81.666667  14.571662     3
TP53  control     22.000000   4.582576     3
      treated     21.666667   0.577350     3
       total  n_samples
gene                   
BRCA1    304          6
GAPDH   2428          6
MYC      476          6
TP53     131          6
```

pandas 的 `std` 是除数为 $n - 1$（`ddof=1`）的样本**标准差**，而 NumPy 的 `np.std` 默认除以 $n$；在同一次分析中混用两者是细小差异的典型来源。第二个调用使用的是*命名聚合*，形式为 `new_column=(column, function)`，它使结果的列名具有可读性。

变换保持输入的形状。每百万计数（counts per million）是针对测序深度的最简单的归一化，它把每个计数除以所在样本的总计数：

$$
\mathrm{CPM}_{gs} = \frac{c_{gs}}{\sum_{g'} c_{g's}} \times 10^6 ,
$$

其中 $c_{gs}$ 是基因 $g$ 在样本 $s$ 中的计数。用 `transform` 按样本计算文库大小，并广播回该样本的每一行；再用 `pivot` 回到基因乘样本的矩阵：

```python
lib_size = long.groupby("sample")["count"].transform("sum")
long["cpm"] = long["count"] / lib_size * 1e6
print(long.pivot(index="gene", columns="sample", values="cpm").round(0))
print(long.pivot_table(index="gene", columns="condition",
                       values="count", aggfunc="mean").round(1))
```

```text
sample        S1        S2        S3        S4        S5        S6
gene                                                              
BRCA1    93146.0   62745.0   95941.0   94972.0   94371.0  102253.0
GAPDH   722320.0  735294.0  739852.0  743017.0  725166.0  700173.0
MYC     144112.0  150980.0  132841.0  121043.0  145695.0  159445.0
TP53     40422.0   50980.0   31365.0   40968.0   34768.0   38128.0
condition  control  treated
gene                       
BRCA1         45.7     55.7
GAPDH        395.7    413.7
MYC           77.0     81.7
TP53          22.0     21.7
```

（只有四个基因时 CPM 的数值很大；真实的文库有数万个基因。）按名称给出的内置聚合（`"sum"`、`"mean"`、`"std"`、`"quantile"`）在编译代码中运行；把 Python 函数传给 `agg`、`transform` 或 `apply`，则每组调用一次，在有许多小组时可能慢几个数量级。与 NumPy 的建议相同：尽可能用整列运算表达计算（[4.4.7](/4.4.7) 测量了两者的差别）。对 `category` dtype 的列分组时，只有传入 `observed=False` 才会包含未出现的类别；自 pandas 3.0 起默认为 `observed=True`。

pandas 计算描述性统计量（`describe`、`corr`、`cov`、`quantile`、`rank`、`value_counts`），但不建立模型。回归与**方差分析**（[3.3](/3.3)）通常使用 statsmodels，其公式接口接受长格式的 DataFrame（`smf.ols("od600 ~ C(strain) * time_h", data=df)`），以及 scikit-learn；两者都直接接受 DataFrame。

## 5.6. 合并表格

### 5.6.1. 连接

**定义 5.6.1（连接）** 两张表按一个或多个键列的**连接**（join），把第一张表的每一行与第二张表中键值相同的每一行配对。**内连接**只保留两张表中都出现的键；**左连接**保留左表的每一行，右表没有配对的行时，右表各列填缺失值（右连接与之对称）；**全外连接**保留两张表的所有键。

连接是关系数据库（[4.13](/4.13)）的核心运算；在 pandas 中由 `merge`（按列）和 `join`（按索引）完成：

```python
annot = pd.DataFrame({"gene": ["BRCA1", "TP53", "MYC"], "chrom": ["17", "17", "8"]})
path = pd.DataFrame({"gene": ["TP53", "MYC", "EGFR"], "pathway": ["p53", "Wnt", "ErbB"]})
print(annot.merge(path, on="gene", how="inner"))
print(annot.merge(path, on="gene", how="outer", indicator=True))
```

```text
   gene chrom pathway
0  TP53    17     p53
1   MYC     8     Wnt
    gene chrom pathway      _merge
0  BRCA1    17     NaN   left_only
1   EGFR   NaN    ErbB  right_only
2    MYC     8     Wnt        both
3   TP53    17     p53        both
```

如果某个键在左表中出现 $m$ 次、在右表中出现 $n$ 次，连接就为它产生 $mn$ 行。因此注释表中重复的标识符会不报任何错误地使测量值重复，这正是值得写上 `validate="one_to_one"` 或 `"many_to_one"`（§5.4.2 中用过）的原因：当键并不像假定的那样唯一时，它会抛出异常。`indicator=True` 添加上面的 `_merge` 列，这是检查哪些键没有匹配上的最快办法（实践中，常常是仅在大小写或版本后缀上有差别的标识符，例如带与不带 `.<version>` 的 Ensembl 基因标识符）。

### 5.6.2. 拼接

`pd.concat([df1, df2, ...])` 把列相同的表上下堆叠，例如同一实验各块板的导出文件；`keys=["plate1", "plate2"]` 把来源记录在额外的一层索引中，`axis=1` 则把表格并排放置，并按行索引对齐。在循环中逐行扩充表格（循环里反复 `concat`）每次都要复制整张表，耗时为平方级；应把各部分收集在列表中，只拼接一次。

## 5.7. 写时复制

较早的 pandas 版本中，索引操作的结果有时是原数据的**视图**，有时是副本，取决于内部细节；当一次赋值可能传播也可能不传播时，它会以 `SettingWithCopyWarning` 发出警告。pandas 3.0 用一条规则取代了这些规则。

**定义 5.7.1（写时复制）** 在**写时复制**下，通过索引或方法从另一个 DataFrame 或 Series 得到的每个 DataFrame 或 Series，其行为都相当于独立的副本：修改它绝不会修改原对象，反之亦然。内部实现上，两个对象共享内存，只有当其中一个第一次被修改时才复制数据。

写时复制是一种通用技术（操作系统用它处理由 `fork` 创建的进程的内存，见 [4.4.7](/4.4.7)）。在 pandas 中它有三个实际的后果：

```python
df = pd.DataFrame({"gene": ["BRCA1", "TP53", "MYC"], "count": [53, 23, 82]})
high = df[df["count"] > 30]
high.loc[:, "count"] = 0                       # modifies `high` only
print(df["count"].tolist(), high["count"].tolist())

df["count"][df["gene"] == "TP53"] = -1         # chained assignment: no effect
print(df["count"].tolist())
df.loc[df["gene"] == "TP53", "count"] = -1     # one indexing step: works
print(df["count"].tolist())
print(df["count"].to_numpy().flags.writeable)
```

```text
[53, 23, 82] [0, 0]
[53, 23, 82]
[53, -1, 82]
False
```

1. 修改子集绝不会改变父表，因此旧代码中防御性的 `.copy()` 调用是不必要的。
2. 链式赋值，即经过两步索引的赋值，如 `df["count"][mask] = value`，修改的是临时对象，对 `df` 没有影响；pandas 会发出 `ChainedAssignmentError` 警告。对 DataFrame 的每次更新都必须是单个 `loc` 或 `iloc` 赋值。
3. 通过 `to_numpy()`（或 `.values`）得到的、与 DataFrame 共享内存的数组是只读的；就地修改之前，先对该数组调用 `.copy()`。

由于复制被推迟，`df.rename(...).assign(...).query(...)` 这样的方法链不再在每一步复制整张表。旧选项 `mode.copy_on_write` 在 pandas 3.0 中不起作用，许多方法的 `copy=` 关键字也已弃用。

## 5.8. polars

polars 是用 Rust 写成的 DataFrame 库，建立在 Apache Arrow 列式内存格式之上；2.0 版于 2026 年 10 月发布。它的设计在对大表重要的几个方面与 pandas 不同：

| | pandas | polars |
|---|---|---|
| 行索引 | 居于核心（对齐、`loc`） | 没有：行由列标识 |
| API | DataFrame 与 Series 上的方法 | 表达式（`pl.col("x").mean()`），在上下文（`select`、`with_columns`、`filter`、`group_by().agg`）中求值 |
| 执行 | 即时，多为单线程 | 多线程；即时的 `DataFrame` 或*惰性*的 `LazyFrame` |
| 内存 | NumPy 数组，可选 Arrow | Arrow；流式引擎可处理超过内存的数据 |
| 生态 | statsmodels、scikit-learn、seaborn 的标准输入 | 用 `to_pandas()`、`to_numpy()` 转换；直接支持日渐增多 |

§5.4 与 §5.5 的流水线用 polars 写成如下（polars 2.0.0）：

```python
import numpy as np
import polars as pl

rng = np.random.default_rng(0)
genes = ["BRCA1", "TP53", "GAPDH", "MYC"]
samples = ["S1", "S2", "S3", "S4", "S5", "S6"]
counts = rng.poisson(lam=[[50], [20], [400], [80]], size=(4, 6))
wide = pl.DataFrame({"gene": genes, **{s: counts[:, j] for j, s in enumerate(samples)}})
meta = pl.DataFrame({"sample": samples, "condition": ["control"] * 3 + ["treated"] * 3})

long = (
    wide.unpivot(index="gene", variable_name="sample", value_name="count")
    .join(meta, on="sample", how="left")
    .with_columns(cpm=pl.col("count") / pl.col("count").sum().over("sample") * 1e6)
)
summary = (
    long.group_by("gene", "condition")
    .agg(mean=pl.col("count").mean(), sd=pl.col("count").std())
    .sort("gene", "condition")
)
print(summary.head(4))
```

```text
shape: (4, 4)
┌───────┬───────────┬────────────┬───────────┐
│ gene  ┆ condition ┆ mean       ┆ sd        │
│ ---   ┆ ---       ┆ ---        ┆ ---       │
│ str   ┆ str       ┆ f64        ┆ f64       │
╞═══════╪═══════════╪════════════╪═══════════╡
│ BRCA1 ┆ control   ┆ 45.666667  ┆ 11.846237 │
│ BRCA1 ┆ treated   ┆ 55.666667  ┆ 4.163332  │
│ GAPDH ┆ control   ┆ 395.666667 ┆ 18.583146 │
│ GAPDH ┆ treated   ┆ 413.666667 ┆ 21.221059 │
└───────┴───────────┴────────────┴───────────┘
```

窗口表达式 `pl.col("count").sum().over("sample")` 的作用相当于 `groupby(...).transform("sum")`。数值与 pandas 的结果一致。请注意显式的 `sort`：polars 不保证 `group_by` 结果的行序，自 2.0 版起，连接与 `unpivot` 默认也是如此。

在惰性求值（lazy evaluation）中，运算在写下时并不执行，而是被记录为查询计划，只有在需要结果时才运行。`LazyFrame`（来自 `pl.scan_parquet`、`pl.scan_csv` 或 `df.lazy()`）构建这样的计划，`collect()` 在优化器改写计划之后执行它，例如把筛选和列选择下推到文件读取器，使不需要的行和列根本不会被载入。`explain()` 打印优化后的计划：

```python
query = (long.lazy()
         .filter(pl.col("condition") == "treated")
         .group_by("gene").agg(pl.col("cpm").mean())
         .sort("gene"))
print(query.explain())
```

```text
SORT BY [col("gene")]
  AGGREGATE[maintain_order: false]
    [col("cpm").mean()] BY [col("gene")]
    FROM
    simple π 2/2 ["gene", "cpm"]
      FILTER col("condition") == "treated"
      FROM
        DF ["gene", "sample", "count", "condition", ...]; PROJECT["gene", "cpm", "condition"] 3/5 COLUMNS
```

该计划只读取五列中的三列。在 polars 2.0 中，`collect()` 默认使用流式引擎，它分批处理数据并可以溢出到磁盘，因此可以汇总比内存更大的文件。

一条合理的经验规则：pandas 仍是科学计算 Python 生态的通用语言，适用于中小型表格、交互式工作，以及直接输入 statsmodels、scikit-learn 或 seaborn 的任何场合；polars（或 DuckDB 之类的嵌入式 SQL 引擎）则在数百万行以上的表格、超过内存的文件，以及需要它的查询优化器和多线程的流水线中物有所值。两者都使用 Arrow，所以在边界处相互转换的代价很小。

## 小结

- `Series` 是带索引的数组；DataFrame 是共用同一行索引的 `Series` 构成的表。运算按标签对齐，因此要检查标签是否一致，而不要依赖顺序。
- 用 `loc`（标签）和 `iloc`（位置）选取；把分析表达为由 `query`、`assign`、`groupby` 和 `merge` 构成的方法链。
- 中间数据优先用 Parquet 而不是 CSV；读取文本文件时固定标识符列的 dtype；让表格远离电子表格软件。
- 归约会悄悄跳过缺失值；要明确决定如何处理它们。
- 整洁的长格式数据适合分组、建模和绘图；宽矩阵适合线性代数；`melt` 与 `pivot` 在两者之间转换。
- 拆分-应用-合并：`agg` 每组给出一行，`transform` 保持形状，`filter` 保留整组；按名称给出的内置聚合很快。
- 连接会使重复的键成倍增加；使用 `validate=` 与 `indicator=True`。
- pandas 3 使用写时复制：派生对象绝不与父对象共享别名，链式赋值不起作用，更新要写成单个 `loc` 赋值。
- polars 提供表达式 API、惰性查询优化和多线程；它是 pandas 的补充，而不是替代。
