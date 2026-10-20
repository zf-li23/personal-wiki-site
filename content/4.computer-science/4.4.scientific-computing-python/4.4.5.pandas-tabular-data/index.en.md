---
title: "pandas: Tabular Data"
description: "Tabular data in Python with pandas 3: Series, DataFrame and the index, reading and writing files, missing values, tidy data and reshaping, split-apply-combine with groupby, joins, Copy-on-Write semantics, and a short introduction to polars."
---

Most data in computational biology arrive as tables: a sample sheet with one row per sample, a count matrix with one row per gene, a plate-reader export with one row per well and time point. NumPy **ndarrays** ([4.4.2](/4.4.2)) hold such data only if every column has the same type and the meaning of rows and columns is kept in the programmer's head. pandas adds the two missing ingredients: columns of different types, and *labels* on rows and columns that travel with the data through every operation. This chapter covers the core of pandas (the objects, input and output, missing values, reshaping, grouping and joining), the Copy-on-Write model that defines what an assignment does in pandas 3, and closes with polars, a newer library with a different design. The R counterpart of the pandas DataFrame is the **data frame** of [3.5.2](/3.5.2); the statistical methods applied to these tables are developed in the statistics courses (regression in [3.3](/3.3), multivariate analysis in [3.4](/3.4)), and the next chapter turns tables into figures.

All outputs below were produced with pandas 3.0.6, NumPy 2.5.4 and PyArrow 26.0.0 on CPython 3.14.5. pandas 3.0 (January 2026) changed two defaults that older tutorials and many answers online still contradict: strings get a dedicated `str` **dtype**, and Copy-on-Write is always on (§5.7). Code written for pandas 2 mostly runs unchanged, but code that relied on chained assignment silently stops working.

## 5.1. Series and DataFrame

### 5.1.1. Series

**Definition 5.1.1 (pandas Series)** A `Series` is a one-dimensional array of values of a single dtype together with an array of labels of the same length, the **index**, and an optional name.

The index is what distinguishes a `Series` from a NumPy **ndarray**. Elements can be selected by label or by position, and a Boolean mask selects a subset as in NumPy:

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

Binary operations between two `Series` match elements by label, not by position: the result has the union of the two indexes, and labels present in only one operand give a missing value. This *index alignment* is the main source of both the convenience and the surprises of pandas.

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

When positional arithmetic is really intended, convert explicitly with `.to_numpy()`; when the labels are supposed to match, check it (`tpm.index.equals(other.index)`) rather than trusting that two files list the genes in the same order.

### 5.1.2. DataFrame

**Definition 5.1.2 (DataFrame)** A **DataFrame** is a two-dimensional table whose columns are `Series` sharing one row index; the column labels form a second index. Different columns may have different dtypes.

A DataFrame is usually built from a dictionary of columns or read from a file (§5.2). The following sample sheet of a growth experiment is used throughout the section:

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

No row labels were given, so the index is the default `RangeIndex` $0, 1, \dots, 5$. The text columns have **dtype** `str`: since pandas 3.0 strings are stored in a dedicated string dtype (backed by PyArrow when it is installed, otherwise by NumPy object arrays) instead of the generic `object` dtype of earlier versions. Code that tests `dtype == object` to find text columns must be changed to `pd.api.types.is_string_dtype(...)`.

| Attribute or method | Returns |
|---|---|
| `df.shape`, `len(df)` | (rows, columns), number of rows |
| `df.columns`, `df.index` | column labels, row labels |
| `df.dtypes`, `df.info()` | dtype of every column; dtypes, non-missing counts and memory |
| `df.head(n)`, `df.tail(n)`, `df.sample(n)` | first, last or random rows |
| `df.describe()` | count, mean, standard deviation and quartiles of numeric columns |
| `df.to_numpy()` | the values as a NumPy array (one common dtype) |

### 5.1.3. Selecting Rows and Columns

pandas has two explicit indexers, and code is clearest when it uses them consistently:

- `df.loc[rows, cols]` selects by label: single labels, lists of labels, label slices (which include both endpoints), or Boolean masks;
- `df.iloc[rows, cols]` selects by position, with the usual Python half-open slices.

`df["col"]` returns one column as a `Series` and `df[["a", "b"]]` a sub-table; `df[mask]` filters rows. For filters with several conditions, `query()` reads more naturally, and pandas 3.0 adds `pd.col("name")`, a deferred reference to a column that can be used in `assign()` and `loc` instead of a `lambda`:

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

`assign()` returns a new DataFrame and leaves `growth` unchanged. Chaining such methods (`df.query(...).assign(...).groupby(...)`) expresses an analysis as a pipeline of transformations, each of which can be inspected separately; under Copy-on-Write (§5.7) this style costs no unnecessary copies.

## 5.2. Reading and Writing Data

| Format | Read | Write | Remarks |
|---|---|---|---|
| CSV, TSV | `pd.read_csv(path, sep=...)` | `df.to_csv(path, index=False)` | text; universal but slow, no type information |
| Parquet | `pd.read_parquet(path)` | `df.to_parquet(path)` | binary, columnar, compressed; keeps dtypes; needs PyArrow |
| Excel | `pd.read_excel(path, sheet_name=...)` | `df.to_excel(path)` | needs `openpyxl`; avoid as an intermediate format |
| Feather / Arrow IPC | `pd.read_feather(path)` | `df.to_feather(path)` | fast exchange with R and polars |
| HDF5 | `pd.read_hdf(path, key)` | `df.to_hdf(path, key=...)` | needs PyTables; hierarchical storage of many tables |

The arguments of `read_csv` that matter most in practice are `sep` (`"\t"` for TSV files), `index_col` (use a column as the row index, e.g. gene identifiers), `usecols` (read only some columns), `dtype` (fix the type of identifier columns, so that a sample called `0012` is not read as the integer 12), `na_values` (extra strings meaning "missing"), `parse_dates`, and `comment`. A frequent error in biology deserves a sentence: spreadsheet programs silently convert some gene symbols to dates (`SEPT2`, `MARCH1`), which is one reason the HGNC renamed such genes in 2020 and a good reason not to pass tables through a spreadsheet.

For intermediate results, Parquet is the better default: it stores the **dtypes**, so that a reloaded table equals the saved one, and because it is columnar a reader can load a few columns of a large file without parsing the rest. Passing `dtype_backend="pyarrow"` to a reader makes every column an Arrow-backed array (`int64[pyarrow]`, `string[pyarrow]`, …), which supports missing values in every type; the default NumPy-backed dtypes remain the standard choice and are what the rest of the scientific stack expects.

Columns with a small set of repeated values (strain, condition, batch) can be stored as `category` **dtype**, which keeps each distinct value once and an integer code per row, like a factor in R. It saves memory, fixes the order of the levels (useful for plots and model contrasts) and speeds up grouping.

## 5.3. Missing Values

A *missing value* is an entry whose value is unknown: a failed measurement, a sample not yet collected, a gene absent from one annotation. pandas represents it by `NaN` in floating-point and the default string columns, by `NaT` in datetime columns, and by `pd.NA` in the nullable extension dtypes (`Int64`, `boolean`, Arrow-backed dtypes). Since `NaN` is a floating-point value, an integer column with a gap becomes `float64`, unless a nullable dtype is requested:

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

| Task | Method |
|---|---|
| detect | `isna()`, `notna()`; `df.isna().sum()` counts per column |
| remove | `dropna()`, with `subset=`, `how="all"`, `thresh=` |
| replace | `fillna(value)`, `ffill()`, `bfill()`, `interpolate()` |
| summarize | reductions skip missing values by default (`skipna=True`); `count()` counts non-missing entries |

Reductions skipping missing values is convenient and dangerous at once: the mean above is the mean of five wells, not six, and nothing in the output says so. Missing values are part of the data and should be decided on explicitly. Dropping rows is unbiased only when values are missing for reasons unrelated to the values themselves (a pipetting error, not a culture that died because the mutant grows poorly); replacing them by a mean or zero shrinks variances and distorts correlations; a zero count in sequencing data is an observation, not a missing value. Statistical treatments of missing data, such as the **EM algorithm** of [3.5.6](/3.5.6), start from this distinction.

## 5.4. Tidy Data and Reshaping

### 5.4.1. Tidy Data

The same measurements can be laid out in many tables. A count matrix with genes as rows and samples as columns is compact and is what linear algebra wants; a table with one row per (gene, sample) pair is long and redundant, but every question about it is a filter, a grouping or a join. Hadley Wickham's notion of tidy data (2014) names the layout that makes such operations uniform.

**Definition 5.4.1 (Tidy Data)** A table is **tidy** if every variable is a column, every observation is a row, and every type of observational unit forms its own table. A table with one row per measured value and columns identifying it (here gene, sample, count) is in **long format**; a table that spreads one variable over several columns (one count column per sample) is in **wide format**.

Whether a table is tidy depends on what is regarded as an observation, so the two formats are not right or wrong in themselves: plotting libraries (seaborn, Plotly Express, ggplot2 in R) and model formulas want long format, matrix computations (normalization, **principal component analysis**, **hierarchical clustering**) want wide format, and an analysis moves between them. The sample annotation (condition, batch, donor) is a different observational unit and belongs in its own table, joined in when needed (§5.6).

### 5.4.2. melt, pivot and stack

| From | To | Method |
|---|---|---|
| wide | long | `df.melt(id_vars=..., var_name=..., value_name=...)`; `df.stack()` for a column index |
| long | wide | `df.pivot(index=..., columns=..., values=...)` (pairs must be unique); `df.unstack()` |
| long | wide, aggregating duplicates | `df.pivot_table(index=..., columns=..., values=..., aggfunc=...)` |
| two categorical columns | table of counts | `pd.crosstab(a, b)`, a **contingency table** |

A synthetic count matrix with four genes and six samples illustrates the round trip. The matrix is melted to long format and the sample annotation is joined in:

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

The index of a DataFrame can have several levels (a `MultiIndex`), as the result of a grouping by two keys in the next section shows. `stack()` moves the innermost column level into the row index and `unstack()` does the reverse; they are the index-based counterparts of `melt` and `pivot`.

## 5.5. Split-Apply-Combine

Most summaries of a table have the same shape: *split-apply-combine*, that is, split the rows into groups by the values of one or more key columns, apply a function to each group independently, and combine the results into a new table. In pandas the split is `groupby`, and what is applied determines the shape of the result:

| Operation | Function maps a group to | Result | Example |
|---|---|---|---|
| aggregation `agg` | one value | one row per group | mean count per gene and condition |
| transformation `transform` | a same-length result | same rows as the input | normalize within each sample |
| filtration `filter` | `True` / `False` | a subset of the input rows | keep genes expressed in every sample |
| `apply` | anything | depends | fallback; usually slower |

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

The `std` of pandas is the sample **standard deviation** with divisor $n - 1$ (`ddof=1`), whereas NumPy's `np.std` uses $n$ by default; mixing the two in one analysis is a classic source of small discrepancies. The second call uses *named aggregation*, `new_column=(column, function)`, which gives the result readable column names.

A transformation keeps the shape of the input. Counts per million, the simplest normalization for sequencing depth, divide each count by the total count of its sample:

$$
\mathrm{CPM}_{gs} = \frac{c_{gs}}{\sum_{g'} c_{g's}} \times 10^6 ,
$$

where $c_{gs}$ is the count of gene $g$ in sample $s$. With `transform`, the library size is computed per sample and broadcast back to every row of that sample; `pivot` then returns to a genes-by-samples matrix:

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

(With four genes the CPM values are large; real libraries have tens of thousands of genes.) Built-in aggregations given by name (`"sum"`, `"mean"`, `"std"`, `"quantile"`) run in compiled code; passing a Python function to `agg`, `transform` or `apply` calls it once per group and can be orders of magnitude slower on many small groups. The same advice as for NumPy applies: express the computation with whole-column operations where possible ([4.4.7](/4.4.7) measures the difference). Groupings by a column of `category` dtype include unobserved categories only when `observed=False` is passed; the default since pandas 3.0 is `observed=True`.

pandas computes descriptive statistics (`describe`, `corr`, `cov`, `quantile`, `rank`, `value_counts`) but no models. For regression and **ANOVA** ([3.3](/3.3)) the usual tools are statsmodels, whose formula interface takes a long-format DataFrame (`smf.ols("od600 ~ C(strain) * time_h", data=df)`), and scikit-learn; both accept DataFrames directly.

## 5.6. Combining Tables

### 5.6.1. Joins

**Definition 5.6.1 (Join)** A **join** of two tables on one or more key columns pairs every row of the first table with every row of the second that has the same key values. An **inner join** keeps only keys present in both tables; a **left join** keeps every row of the left table and fills the columns of the right table with missing values where no partner exists (a right join is symmetric); a **full outer join** keeps the keys of both tables.

Joins are the central operation of relational databases ([4.13](/4.13)); in pandas they are performed by `merge` (on columns) and `join` (on the index):

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

If a key occurs $m$ times on the left and $n$ times on the right, the join produces $mn$ rows for it. A duplicated identifier in an annotation table therefore duplicates measurements without any error, which is why `validate="one_to_one"` or `"many_to_one"` (used in §5.4.2) is worth writing: it raises an exception when the keys are not as unique as assumed. `indicator=True` adds the `_merge` column above, the quickest check of which keys failed to match (in practice, often identifiers that differ only in capitalization or in a version suffix, such as Ensembl gene identifiers with and without `.<version>`).

### 5.6.2. Concatenation

`pd.concat([df1, df2, ...])` stacks tables with the same columns, for example the per-plate exports of one experiment; `keys=["plate1", "plate2"]` records the origin in an extra index level, and `axis=1` places tables side by side, aligned on the row index. Growing a table row by row in a loop (repeated `concat` in a loop) copies the whole table every time and costs quadratic time; collect the pieces in a list and concatenate once.

## 5.7. Copy-on-Write

Older pandas versions made the result of an indexing operation sometimes a **view** of the original data and sometimes a copy, depending on internal details, and warned with `SettingWithCopyWarning` when an assignment might or might not propagate. pandas 3.0 replaced these rules with a single one.

**Definition 5.7.1 (Copy-on-Write)** Under **Copy-on-Write**, every DataFrame or Series obtained from another one, by indexing or by a method, behaves as an independent copy: modifying it never modifies the original, and vice versa. Internally the two objects share memory, and the data are copied only when one of them is first modified.

Copy-on-Write is a general technique (operating systems use it for the memory of a process created by `fork`, see [4.4.7](/4.4.7)). In pandas it has three practical consequences:

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

1. Modifying a subset never changes the parent table, so the defensive `.copy()` calls of older code are unnecessary.
2. *Chained assignment*, an assignment through two indexing steps such as `df["count"][mask] = value`, modifies a temporary object and has no effect on `df`; pandas emits a `ChainedAssignmentError` warning. Every update of a DataFrame must be a single `loc` or `iloc` assignment.
3. Arrays obtained by `to_numpy()` (or `.values`) that share memory with a DataFrame are read-only; call `.copy()` on the array before modifying it in place.

Because copies are deferred, method chains such as `df.rename(...).assign(...).query(...)` no longer copy the table at every step. The old option `mode.copy_on_write` has no effect in pandas 3.0, and the `copy=` keyword of many methods is deprecated.

## 5.8. polars

polars is a DataFrame library written in Rust, built on the Apache Arrow columnar memory format; version 2.0 was released in October 2026. Its design differs from pandas in ways that matter for large tables:

| | pandas | polars |
|---|---|---|
| row index | central (alignment, `loc`) | none: rows are identified by columns |
| API | methods on DataFrames and Series | expressions (`pl.col("x").mean()`) evaluated inside contexts (`select`, `with_columns`, `filter`, `group_by().agg`) |
| execution | eager, mostly single-threaded | multi-threaded; eager `DataFrame` or *lazy* `LazyFrame` |
| memory | NumPy arrays, optionally Arrow | Arrow; streaming engine processes data larger than memory |
| ecosystem | the standard input of statsmodels, scikit-learn, seaborn | converts with `to_pandas()`, `to_numpy()`; growing direct support |

The pipeline of §5.4 and §5.5 in polars reads as follows (polars 2.0.0):

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

The window expression `pl.col("count").sum().over("sample")` plays the role of `groupby(...).transform("sum")`. The numbers agree with the pandas results. Note the explicit `sort`: polars does not guarantee the row order of the result of a `group_by`, and since version 2.0 the same holds by default for joins and `unpivot`.

In *lazy evaluation* the operations are not executed when they are written; they are recorded as a query plan, which runs only when the result is requested. A `LazyFrame` (from `pl.scan_parquet`, `pl.scan_csv` or `df.lazy()`) builds such a plan, and `collect()` executes it after an optimizer has rewritten it, for instance by pushing filters and column selections down to the file reader so that unneeded rows and columns are never loaded. `explain()` prints the optimized plan:

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

The plan reads only three of the five columns. In polars 2.0, `collect()` uses the streaming engine by default, which processes the data in batches and can spill to disk, so that files larger than the memory can be summarized.

A reasonable rule: pandas remains the common language of the scientific Python ecosystem and is the right choice for small and medium tables, interactive work and anything that feeds directly into statsmodels, scikit-learn or seaborn; polars (or an embedded SQL engine such as DuckDB) pays off for tables of many millions of rows, for files larger than memory, and for pipelines where its query optimizer and multithreading matter. Since both use Arrow, converting between them at the boundary is cheap.

## Summary

- A `Series` is an array with an index; a DataFrame is a table of `Series` sharing a row index. Operations align on labels, so check that labels match instead of relying on order.
- Select with `loc` (labels) and `iloc` (positions); express analyses as method chains of `query`, `assign`, `groupby` and `merge`.
- Prefer Parquet to CSV for intermediate data; fix the dtypes of identifier columns when reading text files; keep tables away from spreadsheets.
- Missing values are skipped silently by reductions; decide explicitly how to treat them.
- Tidy, long-format data suit grouping, modelling and plotting; wide matrices suit linear algebra; `melt` and `pivot` convert between them.
- Split-apply-combine: `agg` gives one row per group, `transform` keeps the shape, `filter` keeps whole groups; named built-in aggregations are fast.
- Joins multiply duplicated keys; use `validate=` and `indicator=True`.
- pandas 3 uses Copy-on-Write: derived objects never alias their parent, chained assignment does nothing, and updates are single `loc` assignments.
- polars offers an expression API, lazy query optimization and multithreading; it complements rather than replaces pandas.
