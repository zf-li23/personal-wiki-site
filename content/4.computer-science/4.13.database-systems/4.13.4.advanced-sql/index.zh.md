---
title: 高级 SQL
description: SELECT–FROM–WHERE 之外的 SQL：标量子查询、IN 子查询、EXISTS 子查询与相关子查询，NOT IN 的空值陷阱，LATERAL；UNION、INTERSECT 和 EXCEPT 以及 SQL 中的关系除；公用表表达式与在通路层次上的递归查询；用于排名、累计与滑动聚集的窗口函数；INSERT、UPDATE、DELETE、upsert、MERGE 与 RETURNING；视图与物化视图；事务与保存点；权限、角色与行级安全；以及通过 DB-API 从 Python 访问数据库，用参数化查询防御 SQL 注入。
source_hash: 7e674575ebcf
---

[4.13.3](/4.13.3) 的基本查询块是 **SQL** 中其余一切的构件。本章把查询块组合起来：作为子查询彼此嵌套，用集合运算连接，在 `WITH` 子句中命名并重复使用，并递归地应用，以便沿着层次结构走到任意深度。随后介绍窗口函数和修改数据的语句，窗口函数在不合并行的情况下计算聚集，在分析工作中不可或缺。后半部分从查询转向作为共享资源的**数据库**：视图为用户提供各自的**外模式**（[4.13.1](/4.13.1#sec-1.3.1)），SQL 所体现的事务，访问权限，以及程序向数据库安全地发送 SQL 的方式。所有示例都使用 [4.13.3](/4.13.3#sec-3.2.3) 的运行示例；与那里一样，除非标明是 DuckDB 1.5，输出均来自 SQLite 3.45。

## 4.1. 子查询

### 4.1.1. 标量子查询、IN 子查询与 EXISTS 子查询

**定义 4.1.1（子查询）** **子查询**是嵌套在另一条语句中的 `SELECT` 表达式。凡是需要一个值、一组值或一张表的地方，它都可以出现：在 `SELECT` 列表或条件中作为返回单个值的*标量子查询*，在 `IN` 或 `EXISTS` 之后作为一个集合，或在 `FROM` 中作为*派生表*。

用 `IN` 测试某个值是否属于**子查询**的结果。注释到通路 PW3 的基因：

```sql
SELECT symbol FROM gene
WHERE gene_id IN (SELECT gene_id FROM gene_pathway WHERE pathway_id = 'PW3');
```

```text
+--------+
| symbol |
+--------+
| CDKN1A |
| MDM2   |
| TP53   |
+--------+
```

`EXISTS (subquery)` 在子查询至少返回一行时为真，`NOT EXISTS` 在它一行也不返回时为真；子查询的 `SELECT` 列表无关紧要，习惯上写 `1`。它们就是关系演算的存在量词（[4.13.2](/4.13.2#sec-2.5)）。不属于任何通路的基因：

```sql
SELECT g.symbol FROM gene AS g
WHERE NOT EXISTS (SELECT 1 FROM gene_pathway AS gp WHERE gp.gene_id = g.gene_id);
```

```text
+--------+
| symbol |
+--------+
| ACTB   |
+--------+
```

子查询引用了 `g`，它是外层查询的一个表。

**定义 4.1.2（相关子查询）** 如果子查询引用了外围查询的列，它就是**相关**的。它的含义是：对外围查询的每一行求值一次，外层的列固定为该行中的值。

每种组织最近采集的样本，要把每个样本与其所属组织的最大日期相比较：

```sql
SELECT sample_id, tissue, collected_on FROM sample AS s
WHERE collected_on = (SELECT max(s2.collected_on) FROM sample AS s2 WHERE s2.tissue = s.tissue);
```

```text
+-----------+--------+--------------+
| sample_id | tissue | collected_on |
+-----------+--------+--------------+
| S03       | liver  | 2025-03-11   |
| S06       | lung   | 2025-03-25   |
+-----------+--------+--------------+
```

“每行求值一次”是语义，而不是执行计划：优化器通常把相关的 `EXISTS` 和 `IN` 子查询转换成**连接**、半连接（semijoin）（若 $r$ 的某一行在 $s$ 中至少有一个配对对象就保留它）和反连接（antijoin）（若没有就保留它），它们可以用 [4.13.9](/4.13.9) 的散列算法和归并算法计算。标量子查询至多返回一行，否则语句在运行时失败；没有行时它的值为**空值**。

比较运算符还可以与 `ANY`（`SOME`）和 `ALL` 组合：如果 `x` 大于返回的每个值，`x > ALL (subquery)` 为真。SQLite 不支持它们（输出来自 DuckDB）：

```sql
-- Samples whose CDKN1A expression exceeds that of every control sample
SELECT s.sample_id, m.tpm
FROM sample AS s JOIN measurement AS m USING (sample_id) JOIN gene AS g USING (gene_id)
WHERE g.symbol = 'CDKN1A'
  AND m.tpm > ALL (SELECT m2.tpm
                   FROM measurement AS m2 JOIN gene AS g2 USING (gene_id)
                        JOIN sample AS s2 USING (sample_id)
                   WHERE g2.symbol = 'CDKN1A' AND s2.treatment = 'control')
ORDER BY s.sample_id;
```

```text
┌───────────┬───────────────┐
│ sample_id │      tpm      │
│  varchar  │ decimal(10,2) │
├───────────┼───────────────┤
│ S03       │         88.70 │
│ S05       │        141.50 │
│ S06       │        120.80 │
└───────────┴───────────────┘
```

### 4.1.2. NOT IN 陷阱

`x NOT IN (subquery)` 的意思是对子查询的每个值 `v` 都有 `x <> v`。如果其中某个值是空值，`x <> NULL` 就是未知，于是整个条件永远不为真。在运行示例中，不是任何通路的父通路的通路应当是三个叶子（p53-dependent G1 arrest、EGFR signaling、Glycolysis），但 `parent_id` 中含有空值：

```sql
SELECT count(*) AS leaves FROM pathway
WHERE pathway_id NOT IN (SELECT parent_id FROM pathway);

SELECT name FROM pathway AS p
WHERE NOT EXISTS (SELECT 1 FROM pathway AS c WHERE c.parent_id = p.pathway_id);
```

```text
+--------+
| leaves |
+--------+
| 0      |
+--------+
+-------------------------+
|          name           |
+-------------------------+
| EGFR signaling          |
| Glycolysis              |
| p53-dependent G1 arrest |
+-------------------------+
```

`NOT EXISTS` 没有这个问题，因为它只问是否存在匹配的行。规则是：只要子查询的列可以为空，就写 `NOT EXISTS`，或者显式排除空值（在子查询中写 `WHERE parent_id IS NOT NULL`）。`IN` 不受影响，因为 `x = NULL` 为未知只是不增加匹配。

### 4.1.3. FROM 中的子查询与 LATERAL

`FROM` 中的子查询是派生表，必须给它起名字。要按窗口函数的结果过滤（§4.4），或对聚集再做聚集，就要用它。普通的派生表不能引用同一 `FROM` 子句中的其他表；`LATERAL` 子查询（SQL:1999；PostgreSQL、DuckDB、MySQL 8）可以，并且对它左边各表的每一行求值。典型的用法是“每组前 $k$ 名”，这里是每个样本中除管家基因之外表达量最高的两个基因（输出来自 DuckDB）：

```sql
SELECT s.sample_id, top.symbol, top.tpm
FROM sample AS s,
     LATERAL (SELECT g.symbol, m.tpm
              FROM measurement AS m JOIN gene AS g USING (gene_id)
              WHERE m.sample_id = s.sample_id AND g.symbol NOT IN ('GAPDH', 'ACTB')
              ORDER BY m.tpm DESC
              LIMIT 2) AS top
ORDER BY s.sample_id, top.tpm DESC;
```

```text
┌───────────┬─────────┬───────────────┐
│ sample_id │ symbol  │      tpm      │
│  varchar  │ varchar │ decimal(10,2) │
├───────────┼─────────┼───────────────┤
│ S01       │ TP53    │         35.20 │
│ S01       │ EGFR    │         15.60 │
│ S02       │ TP53    │         31.80 │
│ S02       │ EGFR    │         13.90 │
│ S03       │ CDKN1A  │         88.70 │
│ S03       │ TP53    │         42.60 │
│ S04       │ EGFR    │         62.30 │
│ S04       │ TP53    │         48.90 │
│ S05       │ CDKN1A  │        141.50 │
│ S05       │ TP53    │         55.30 │
│ S06       │ CDKN1A  │        120.80 │
│ S06       │ TP53    │         51.00 │
└───────────┴─────────┴───────────────┘
  12 rows                   3 columns
```

## 4.2. 集合运算

### 4.2.1. UNION、INTERSECT 与 EXCEPT

**关系代数**的集合运算把两个列数相同、类型相容的查询的结果组合起来：`UNION`、`INTERSECT` 和 `EXCEPT`（Oracle 21c 之前用 `MINUS`）。它们消除重复；带 `ALL` 的变体保留重复，采用**多重集**语义：如果某行在第一个输入中出现 $m$ 次、在第二个输入中出现 $n$ 次，则 `UNION ALL` 返回它 $m + n$ 次，`INTERSECT ALL` 返回 $\min(m, n)$ 次，`EXCEPT ALL` 返回 $\max(m - n, 0)$ 次。SQLite 在 `ALL` 形式中只支持 `UNION ALL`。

```sql
SELECT tissue FROM sample WHERE treatment = 'treated'
INTERSECT
SELECT tissue FROM sample WHERE donor_age > 60;

SELECT tissue FROM sample WHERE treatment = 'treated'
UNION ALL
SELECT tissue FROM sample WHERE donor_age > 60;
```

```text
+--------+
| tissue |
+--------+
| liver  |
| lung   |
+--------+
+--------+
| tissue |
+--------+
| liver  |
| lung   |
| lung   |
| liver  |
| lung   |
+--------+
```

`UNION ALL` 比 `UNION` 便宜得多，因为它不需要消除重复；只要输入不可能重叠或需要保留重复，它就是正确的选择。结果的列名取自第一个查询，末尾的 `ORDER BY` 作用于合并后的结果。

`EXCEPT` 直接表达否定。所有*没有*被测量的（样本，基因）组合，就是**笛卡儿积**减去已测量的对：

```sql
SELECT s.sample_id, g.symbol FROM sample AS s CROSS JOIN gene AS g
EXCEPT
SELECT m.sample_id, g.symbol FROM measurement AS m JOIN gene AS g USING (gene_id);
```

```text
+-----------+--------+
| sample_id | symbol |
+-----------+--------+
| S05       | EGFR   |
| S06       | EGFR   |
+-----------+--------+
```

### 4.2.2. SQL 中的除

**SQL** 没有**除**运算符（[4.13.2](/4.13.2#sec-2.3.2)）。“每个基因都被测量过的样本”有两种写法。第一种遵循定义的逻辑：如果全体基因的集合减去该样本中被测量的基因为空，这个样本就合格。

```sql
SELECT s.sample_id FROM sample AS s
WHERE NOT EXISTS (
    SELECT g.gene_id FROM gene AS g
    EXCEPT
    SELECT m.gene_id FROM measurement AS m WHERE m.sample_id = s.sample_id);
```

```text
+-----------+
| sample_id |
+-----------+
| S01       |
| S02       |
| S03       |
| S04       |
+-----------+
```

等价的双重否定，“不存在在该样本中没有被测量的基因”，是把 `EXCEPT` 换成第二个 `NOT EXISTS`。第二种写法是计数，它之所以正确，只是因为 `measurement` 的**主码**保证每个（样本，基因）对至多一行，而**外码**保证每个被测量的基因都存在：

```sql
SELECT sample_id FROM measurement
GROUP BY sample_id
HAVING count(*) = (SELECT count(*) FROM gene);
```

```text
+-----------+
| sample_id |
+-----------+
| S01       |
| S02       |
| S03       |
| S04       |
+-----------+
```

## 4.3. 公用表表达式与递归

### 4.3.1. WITH 子句

**定义 4.3.1（公用表表达式）** **公用表表达式**（CTE）是在主语句之前的 `WITH` 子句中定义的有名字的查询，形如 `WITH name (columns) AS (query) statement`；在该语句内部，以及同一子句中后面的 CTE 内部，这个名字表示该查询的结果。

**CTE** 是**关系代数**中赋值运算在 **SQL** 里的形式。它让长查询可以自上而下地读成一系列步骤，而不必由里向外地读。在处理过的样本中，某个基因比同一组织对照样本的平均值高出三倍以上的情形：

```sql
WITH ctrl AS (
    SELECT s.tissue, m.gene_id, avg(m.tpm) AS mean_ctrl
    FROM measurement AS m JOIN sample AS s USING (sample_id)
    WHERE s.treatment = 'control'
    GROUP BY s.tissue, m.gene_id
)
SELECT g.symbol, s.sample_id, s.tissue, m.tpm, round(m.tpm / c.mean_ctrl, 2) AS ratio
FROM measurement AS m
     JOIN sample AS s USING (sample_id)
     JOIN ctrl   AS c ON c.tissue = s.tissue AND c.gene_id = m.gene_id
     JOIN gene   AS g ON g.gene_id = m.gene_id
WHERE s.treatment = 'treated' AND m.tpm > 3 * c.mean_ctrl
ORDER BY ratio DESC;
```

```text
+--------+-----------+--------+-------+-------+
| symbol | sample_id | tissue |  tpm  | ratio |
+--------+-----------+--------+-------+-------+
| CDKN1A | S03       | liver  | 88.7  | 7.61  |
| CDKN1A | S05       | lung   | 141.5 | 6.97  |
| CDKN1A | S06       | lung   | 120.8 | 5.95  |
| MDM2   | S05       | lung   | 36.8  | 3.91  |
| MDM2   | S03       | liver  | 30.2  | 3.85  |
| MDM2   | S06       | lung   | 33.1  | 3.52  |
+--------+-----------+--------+-------+-------+
```

CTE 是计算一次后存储起来，还是像视图那样展开到主查询中，由系统决定。PostgreSQL 12 及以后会把只被引用一次且没有**副作用**的 CTE 内联，并接受 `AS MATERIALIZED` 和 `AS NOT MATERIALIZED` 来覆盖这一选择。在 PostgreSQL 中，CTE 还可以包含 `INSERT`、`UPDATE` 或 `DELETE ... RETURNING`（“修改数据的 CTE”）。

### 4.3.2. 递归查询

关系代数无法计算**关系**的**传递闭包**（[4.13.2](/4.13.2#sec-2.5)），而层次结构和图随处可见：通路中套通路、基因本体、系统发生树、课程的先修关系。SQL:1999 在 `WITH` 子句中加入了递归。

**定义 4.3.2（递归查询）** **递归查询**是由 `WITH RECURSIVE` 引入的公用表表达式，其查询是一个非递归的*基础*查询与一个引用该 CTE 自身的*递归*查询的并。它的值是包含基础查询结果、并对递归查询封闭的最小关系 $T$，也就是 $T = \mathit{base} \cup f(T)$ 的最小不动点。

不动点用迭代计算：从 $T_0 = \mathit{base}$ 出发，由上一轮新增的行计算 $\Delta_{i+1} = f(\Delta_i)$（使用 `UNION` 时再减去已在 $T$ 中的行），把它们加入，当某一轮没有新增时停止。只要结果是有限的、且没有哪一轮会永远产生新行，这种*半朴素*求值就会终止。每条通路的所有祖先及其距离：

```sql
WITH RECURSIVE ancestor (pathway_id, ancestor_id, depth) AS (
    SELECT pathway_id, parent_id, 1            -- base: the parent
    FROM pathway WHERE parent_id IS NOT NULL
    UNION ALL
    SELECT a.pathway_id, p.parent_id, a.depth + 1  -- recursive step: parent of an ancestor
    FROM ancestor AS a JOIN pathway AS p ON p.pathway_id = a.ancestor_id
    WHERE p.parent_id IS NOT NULL
)
SELECT * FROM ancestor ORDER BY pathway_id, depth;
```

```text
+------------+-------------+-------+
| pathway_id | ancestor_id | depth |
+------------+-------------+-------+
| PW2        | PW1         | 1     |
| PW3        | PW2         | 1     |
| PW3        | PW1         | 2     |
| PW5        | PW4         | 1     |
| PW7        | PW6         | 1     |
+------------+-------------+-------+
```

第一轮找出父通路，第二轮找出 PW3 的祖父通路，第三轮什么也找不到，因为 PW1 没有父通路。在注释**数据库**中，一个常见的应用是：当一个基因被注释到某条通路的任何子通路时，也把它算作这条通路的成员。“Cell cycle”及其下属各通路中的所有基因：

```sql
WITH RECURSIVE sub (pathway_id) AS (
    SELECT pathway_id FROM pathway WHERE name = 'Cell cycle'
    UNION
    SELECT p.pathway_id FROM pathway AS p JOIN sub ON p.parent_id = sub.pathway_id
)
SELECT DISTINCT g.symbol
FROM sub JOIN gene_pathway AS gp USING (pathway_id) JOIN gene AS g USING (gene_id)
ORDER BY g.symbol;
```

```text
+--------+
| symbol |
+--------+
| BRCA1  |
| CDKN1A |
| MDM2   |
| MYC    |
| TP53   |
+--------+
```

直接注释到“Cell cycle”的只有 MYC；其他四个基因来自它下面的检查点通路。

标准对**递归查询**加以限制，使不动点存在：递归引用只能出现一次，并且不能出现在聚集、`NOT EXISTS`、`EXCEPT` 或外**连接**的可空一侧内。这些恰是 [4.13.2](/4.13.2#sec-2.4) 中的非单调构造；当 $f$ 单调时，向 $T$ 中增加行至多使 $f(T)$ 增加行，迭代收敛到最小不动点。在含有环的数据中（一般的图而不是树），`UNION ALL` 会永远循环；只要行中不带 `depth` 这样不断增长的值，`UNION` 就会停止，因为重复访问的行被丢弃。PostgreSQL 14 及以后还提供标准的 `CYCLE` 子句，它标记并在重复访问的行处停止，还提供 `SEARCH DEPTH FIRST` / `BREADTH FIRST` 来规定输出顺序。

## 4.4. 窗口函数

### 4.4.1. 窗口

用 `GROUP BY` 做**聚集**，每组返回一行。许多分析问题需要的是把聚集值放在每一行旁边：基因在其样本中的排名、它占样本总量的份额、相对上一个时间点的变化。

**定义 4.4.1（窗口函数）** **窗口函数**对查询结果的每一行，由一组相关的行，即它的*窗口*，计算一个值，而不合并这些行。窗口由 `OVER (PARTITION BY ... ORDER BY ... frame)` 指定：分区由 `PARTITION BY` 表达式取值相同的行构成，按 `ORDER BY` 排序，可选的*框架*把窗口限制在这个顺序中靠近当前行的那些行。

**窗口函数**在 `WHERE`、`GROUP BY` 和 `HAVING` 之后、`DISTINCT`、`ORDER BY` 和 `LIMIT` 之前求值（[4.13.3](/4.13.3#sec-3.8)）。因此它们只能出现在 `SELECT` 列表和 `ORDER BY` 中；要按它们过滤，需要用派生表或 **CTE**。它们在 SQL:2003 中加入，PostgreSQL、SQLite（3.25 及以后）、DuckDB 和 MySQL 8 都支持。

### 4.4.2. 排名

`row_number()` 给每个分区的行编号 $1, 2, 3, \dots$；`rank()` 给相等的值相同的名次，并在并列之后留出空缺（1、2、2、4），`dense_rank()` 不留空缺（1、2、2、3）；`ntile(n)` 把分区分成 $n$ 个桶。两个样本中的基因按表达量排名：

```sql
SELECT m.sample_id, g.symbol, m.tpm,
       rank() OVER (PARTITION BY m.sample_id ORDER BY m.tpm DESC) AS rnk
FROM measurement AS m JOIN gene AS g USING (gene_id)
WHERE m.sample_id IN ('S03', 'S04')
ORDER BY m.sample_id, rnk
LIMIT 10;
```

```text
+-----------+--------+--------+-----+
| sample_id | symbol |  tpm   | rnk |
+-----------+--------+--------+-----+
| S03       | ACTB   | 2150.3 | 1   |
| S03       | GAPDH  | 1610.2 | 2   |
| S03       | CDKN1A | 88.7   | 3   |
| S03       | TP53   | 42.6   | 4   |
| S03       | MDM2   | 30.2   | 5   |
| S03       | EGFR   | 14.2   | 6   |
| S03       | MYC    | 3.2    | 7   |
| S03       | BRCA1  | 2.9    | 8   |
| S04       | ACTB   | 3120.4 | 1   |
| S04       | GAPDH  | 2034.5 | 2   |
+-----------+--------+--------+-----+
```

按名次过滤，可以不用 `LATERAL` 而可移植地回答“每组前 $k$ 名”。每个样本中表达量最高的非管家基因：

```sql
SELECT sample_id, symbol, tpm
FROM (SELECT m.sample_id, g.symbol, m.tpm,
             row_number() OVER (PARTITION BY m.sample_id ORDER BY m.tpm DESC) AS rn
      FROM measurement AS m JOIN gene AS g USING (gene_id)
      WHERE g.symbol NOT IN ('GAPDH', 'ACTB')) AS ranked
WHERE rn = 1
ORDER BY sample_id;
```

```text
+-----------+--------+-------+
| sample_id | symbol |  tpm  |
+-----------+--------+-------+
| S01       | TP53   | 35.2  |
| S02       | TP53   | 31.8  |
| S03       | CDKN1A | 88.7  |
| S04       | EGFR   | 62.3  |
| S05       | CDKN1A | 141.5 |
| S06       | CDKN1A | 120.8 |
+-----------+--------+-------+
```

这取代了 [4.13.3](/4.13.3#sec-3.6.2) 中不可移植的“裸列”查询。使用 `row_number()` 时并列项被任意打破；使用 `rank()` 时返回所有并列的行。

### 4.4.3. 窗口上的聚集

每个**聚集函数**都可以用作窗口函数。窗口中没有 `ORDER BY` 时，它在整个分区上计算，由此得到每个基因占样本总量的份额：

```sql
SELECT m.sample_id, g.symbol, m.tpm,
       round(100.0 * m.tpm / sum(m.tpm) OVER (PARTITION BY m.sample_id), 1) AS pct_of_sample
FROM measurement AS m JOIN gene AS g USING (gene_id)
WHERE m.sample_id = 'S05'
ORDER BY m.tpm DESC;
```

```text
+-----------+--------+--------+---------------+
| sample_id | symbol |  tpm   | pct_of_sample |
+-----------+--------+--------+---------------+
| S05       | ACTB   | 2988.1 | 57.1          |
| S05       | GAPDH  | 1987.3 | 38.0          |
| S05       | CDKN1A | 141.5  | 2.7           |
| S05       | TP53   | 55.3   | 1.1           |
| S05       | MDM2   | 36.8   | 0.7           |
| S05       | MYC    | 14.9   | 0.3           |
| S05       | BRCA1  | 5.6    | 0.1           |
+-----------+--------+--------+---------------+
```

要把每个基因在各样本间标准化（聚类或画热图之前用的 $z$ 分数 $(x - \bar x)/s$），需要该基因所在分区的均值和标准差。`WINDOW` 子句给多次使用的窗口命名（输出来自 DuckDB；SQLite 没有 `stddev_samp`）：

```sql
SELECT g.symbol, m.sample_id, m.tpm,
       round((m.tpm - avg(m.tpm) OVER w) / stddev_samp(m.tpm) OVER w, 2) AS z
FROM measurement AS m JOIN gene AS g USING (gene_id)
WHERE g.symbol IN ('CDKN1A', 'MYC')
WINDOW w AS (PARTITION BY g.symbol)
ORDER BY g.symbol, m.sample_id;
```

```text
┌─────────┬───────────┬───────────────┬────────┐
│ symbol  │ sample_id │      tpm      │   z    │
│ varchar │  varchar  │ decimal(10,2) │ double │
├─────────┼───────────┼───────────────┼────────┤
│ CDKN1A  │ S01       │         12.40 │  -0.91 │
│ CDKN1A  │ S02       │         10.90 │  -0.94 │
│ CDKN1A  │ S03       │         88.70 │   0.39 │
│ CDKN1A  │ S04       │         20.30 │  -0.77 │
│ CDKN1A  │ S05       │        141.50 │   1.29 │
│ CDKN1A  │ S06       │        120.80 │   0.94 │
│ MYC     │ S01       │          5.30 │  -0.75 │
│ MYC     │ S02       │          6.10 │  -0.64 │
│ MYC     │ S03       │          3.20 │  -1.03 │
│ MYC     │ S04       │         22.70 │   1.61 │
│ MYC     │ S05       │         14.90 │   0.56 │
│ MYC     │ S06       │         12.60 │   0.24 │
└─────────┴───────────┴───────────────┴────────┘
  12 rows                            4 columns
```

### 4.4.4. 框架与偏移

窗口中有 `ORDER BY` 时，默认的框架是 `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`：从分区开头到当前行*及其同级行*（排序中相等的行）。这使 `sum` 成为累计和。显式的框架，如 `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW`，给出两行的滑动窗口。偏移函数 `lag(x)` 和 `lead(x)` 返回分区中上一行和下一行的 `x`，`first_value`、`last_value` 和 `nth_value` 返回框架中其他位置的值。TP53 按采集顺序：

```sql
SELECT s.sample_id, s.collected_on, m.tpm,
       round(avg(m.tpm) OVER (ORDER BY s.collected_on, s.sample_id
                              ROWS BETWEEN 1 PRECEDING AND CURRENT ROW), 2) AS moving_avg,
       m.tpm - lag(m.tpm) OVER (ORDER BY s.collected_on, s.sample_id) AS change
FROM measurement AS m JOIN sample AS s USING (sample_id) JOIN gene AS g USING (gene_id)
WHERE g.symbol = 'TP53'
ORDER BY s.collected_on, s.sample_id;
```

```text
+-----------+--------------+------+------------+--------+
| sample_id | collected_on | tpm  | moving_avg | change |
+-----------+--------------+------+------------+--------+
| S01       | 2025-03-04   | 35.2 | 35.2       | NULL   |
| S02       | 2025-03-04   | 31.8 | 33.5       | -3.4   |
| S03       | 2025-03-11   | 42.6 | 37.2       | 10.8   |
| S04       | 2025-03-18   | 48.9 | 45.75      | 6.3    |
| S05       | 2025-03-18   | 55.3 | 52.1       | 6.4    |
| S06       | 2025-03-25   | 51   | 53.15      | -4.3   |
+-----------+--------------+------+------------+--------+
```

第一行没有前一行，所以 `lag` 返回**空值**，差也是空值。排序中包含 `sample_id` 是为了使它成为全序：S01 和 S02 在同一天采集，没有这个附加的排序键，它们的顺序以及随之而来的滑动平均都是未规定的。默认的 `RANGE` 框架把这样的同级行视为一个整体，所以默认框架上的 `last_value` 常常出人意料：它返回当前行的最后一个同级行，而不是分区的最后一行。

## 4.5. 修改数据

### 4.5.1. INSERT、UPDATE 与 DELETE

`INSERT INTO t (columns) VALUES (...), (...)` 添加行；省略的列取其默认值（没有声明默认值则为**空值**）。`INSERT INTO t (columns) SELECT ...` 添加一个查询的结果，就像 [4.13.3](/4.13.3#sec-3.2.3) 中装入测量值那样。`UPDATE t SET column = expression WHERE condition` 修改满足条件的行，`DELETE FROM t WHERE condition` 删除它们；没有 `WHERE` 时，每一行都受影响。`RETURNING` 子句（PostgreSQL、SQLite 3.35 及以后、DuckDB；MySQL 没有）返回被插入、更新或删除的行，例如由默认值或**标识列**填入的值；在 PostgreSQL 18 中，它可以同时返回被更新的行的 `OLD` 值和 `NEW` 值。

```sql
INSERT INTO sample (sample_id, tissue, treatment, collected_on)
VALUES ('S07', 'kidney', 'control', '2025-04-01'),
       ('S08', 'kidney', 'treated', '2025-04-01')
RETURNING sample_id, donor_age;

-- Correct one value, and rescale the EGFR values of the samples of 18 March
UPDATE sample SET donor_age = 52 WHERE sample_id = 'S05';
UPDATE measurement
SET tpm = round(tpm * 1.05, 2)
WHERE gene_id = 'ENSG00000146648'
  AND sample_id IN (SELECT sample_id FROM sample WHERE collected_on = '2025-03-18')
RETURNING sample_id, tpm;

DELETE FROM sample WHERE tissue = 'kidney';
DELETE FROM sample WHERE sample_id = 'S01';
```

```text
+-----------+-----------+
| sample_id | donor_age |
+-----------+-----------+
| S07       | NULL      |
| S08       | NULL      |
+-----------+-----------+
+-----------+-------+
| sample_id |  tpm  |
+-----------+-------+
| S04       | 65.42 |
+-----------+-------+
Runtime error near line 15: FOREIGN KEY constraint failed (19)
```

最后一条语句被拒绝，因为仍有测量值引用 S01。`UPDATE` 在修改一行之前，先在旧值上求出它的所有表达式，所以 `UPDATE t SET a = b, b = a` 会交换这两列（MySQL 是例外：它从左到右赋值，使用已经更新过的 `a`）。

### 4.5.2. Upsert 与 MERGE

装入数据往往意味着“插入这一行，如果已有具有该码的行就更新它”。PostgreSQL（9.5 及以后）和 SQLite（3.24 及以后）提供 `INSERT ... ON CONFLICT`，其中的伪表 `excluded` 保存无法插入的那一行：

```sql
INSERT INTO measurement (sample_id, gene_id, tpm)
VALUES ('S05', 'ENSG00000146648', 18.4),   -- new: EGFR was not measured in S05
       ('S05', 'ENSG00000141510', 54.9)    -- exists: TP53 is corrected
ON CONFLICT (sample_id, gene_id) DO UPDATE SET tpm = excluded.tpm;

SELECT sample_id, gene_id, tpm FROM measurement
WHERE sample_id = 'S05' AND gene_id IN ('ENSG00000146648', 'ENSG00000141510');
```

```text
+-----------+-----------------+------+
| sample_id |     gene_id     | tpm  |
+-----------+-----------------+------+
| S05       | ENSG00000141510 | 54.9 |
| S05       | ENSG00000146648 | 18.4 |
+-----------+-----------------+------+
```

`ON CONFLICT DO NOTHING` 则跳过冲突的行；MySQL 写作 `INSERT ... ON DUPLICATE KEY UPDATE`。标准语句是 `MERGE`（SQL:2003；PostgreSQL 15 及以后、DuckDB、Oracle、SQL Server），它把源表与目标表匹配，并分别为匹配和不匹配的行指定动作：

```sql
CREATE TABLE new_values (sample_id text, gene_id text, tpm numeric(10, 2));
INSERT INTO new_values VALUES ('S05', 'ENSG00000146648', 18.4), ('S05', 'ENSG00000141510', 54.9);

MERGE INTO measurement AS m
USING new_values AS n
ON m.sample_id = n.sample_id AND m.gene_id = n.gene_id
WHEN MATCHED THEN UPDATE SET tpm = n.tpm
WHEN NOT MATCHED THEN INSERT (sample_id, gene_id, tpm) VALUES (n.sample_id, n.gene_id, n.tpm);

SELECT sample_id, gene_id, tpm FROM measurement
WHERE sample_id = 'S05' AND gene_id IN ('ENSG00000146648', 'ENSG00000141510')
ORDER BY gene_id;
```

```text
┌────────┐
│ Count  │
│ int64  │
└────────┘
  0 rows

┌───────┐
│ Count │
│ int64 │
├───────┤
│     2 │
└───────┘

┌───────┐
│ Count │
│ int64 │
├───────┤
│     2 │
└───────┘

┌───────────┬─────────────────┬───────────────┐
│ sample_id │     gene_id     │      tpm      │
│  varchar  │     varchar     │ decimal(10,2) │
├───────────┼─────────────────┼───────────────┤
│ S05       │ ENSG00000141510 │         54.90 │
│ S05       │ ENSG00000146648 │         18.40 │
└───────────┴─────────────────┴───────────────┘
```

这两种形式在并发下不同：`ON CONFLICT` 依赖唯一索引，即使另一个会话在同一时刻插入同一个码，也保证要么插入要么更新，而 PostgreSQL 中的 `MERGE` 在这种情形下可能因违反唯一码而失败。对于批量装入，两者都比专用命令（PostgreSQL 和 DuckDB 中的 `COPY`，SQLite shell 中的 `.import`）慢得多。

## 4.6. 视图

**定义 4.6.1（视图）** **视图**是存储在目录中的有名字的查询，`CREATE VIEW name AS query`。视图是虚拟关系：它不存储行，引用它的查询的求值方式，就像把视图的定义代入它的名字一样。

视图有两个用途。一是简化：几乎每个对运行示例的分析都以三表**连接**开头，可以把它一次定义好。二是它们就是**三级模式结构**（[4.13.1](/4.13.1#sec-1.3)）中的**外模式**：可以只给用户访问视图的权限而不给底层表的权限，例如让用户能看到表达量而看不到供体年龄。基表改变时视图的内容随之改变，而改变后的基表模式可以隐藏在具有旧形状的视图后面，实际中逻辑数据独立性就是这样实现的。

```sql
CREATE VIEW expression AS
SELECT s.sample_id, s.tissue, s.treatment, g.symbol, m.tpm
FROM measurement AS m
     JOIN sample AS s ON s.sample_id = m.sample_id
     JOIN gene   AS g ON g.gene_id = m.gene_id;

SELECT tissue, treatment, round(avg(tpm), 1) AS mean_mdm2
FROM expression WHERE symbol = 'MDM2'
GROUP BY tissue, treatment;

UPDATE expression SET tpm = 0 WHERE symbol = 'MDM2';
```

```text
+--------+-----------+-----------+
| tissue | treatment | mean_mdm2 |
+--------+-----------+-----------+
| liver  | control   | 7.8       |
| liver  | treated   | 30.2      |
| lung   | control   | 9.4       |
| lung   | treated   | 35.0      |
+--------+-----------+-----------+
Parse error near line 11: cannot modify expression because it is a view
```

通过视图更新在一般情形下是个问题：对连接或聚集的更新并不能确定基表的唯一改变。SQLite 的视图是只读的（`INSTEAD OF` 触发器可以手工实现更新，[4.13.6](/4.13.6#sec-6.1.4)）。如果视图从单个表中选取、且不含**聚集**、`DISTINCT`、集合运算或 `LIMIT`，PostgreSQL 会自动使它可更新；`WITH CHECK OPTION` 则拒绝插入或更新后在视图中看不到的行。

物化视图（materialized view）像表一样存储它的结果：在 PostgreSQL 中写作 `CREATE MATERIALIZED VIEW gene_summary AS SELECT ...`，用 `REFRESH MATERIALIZED VIEW gene_summary` 重新计算。它用新鲜度换取速度，用于经常被读取、可以稍微过时的昂贵汇总。通过只应用基表的变化来增量地保持物化视图最新，称为*视图维护*；PostgreSQL 重新计算整个视图，而商用系统和一些扩展则增量地维护视图。

## 4.7. SQL 中的事务

事务是 **DBMS** 作为一个单元执行的一串语句：它们的所有效果要么都成为永久的，要么都不是，并发的事务也看不到彼此的中间状态。它们的理论，即 ACID 特性、调度与可串行化，是 [4.13.10](/4.13.10) 的主题；本节只展示这些语句。

在标准 **SQL** 中，事务隐式地从第一条语句开始；在 PostgreSQL、SQLite、DuckDB 和 MySQL 中，显式事务之外的每条语句自成一个事务（自动提交（autocommit）），`BEGIN`（标准：`START TRANSACTION`）开始一个多语句事务。`COMMIT` 使它的修改成为永久的，`ROLLBACK` 撤销全部修改：

```sql
BEGIN;
DELETE FROM measurement WHERE sample_id = 'S06';
SELECT count(*) AS inside FROM measurement;
ROLLBACK;
SELECT count(*) AS after_rollback FROM measurement;
```

```text
+--------+
| inside |
+--------+
| 39     |
+--------+
+----------------+
| after_rollback |
+----------------+
| 46             |
+----------------+
```

保存点（savepoint）标记事务内部的一个点，事务可以部分地回滚到该点，而不放弃之前的工作：

```sql
BEGIN;
INSERT INTO sample VALUES ('S07', 'kidney', 'control', 39, '2025-04-01');
SAVEPOINT before_measurements;
INSERT INTO measurement VALUES ('S07', 'ENSG00000141510', 40.1);
ROLLBACK TO SAVEPOINT before_measurements;
COMMIT;
SELECT (SELECT count(*) FROM sample) AS samples, (SELECT count(*) FROM measurement) AS measurements;
```

```text
+---------+--------------+
| samples | measurements |
+---------+--------------+
| 7       | 46           |
+---------+--------------+
```

新样本被保留，它的测量值没有。在 PostgreSQL 中，失败的语句会使整个事务中止（在 `ROLLBACK` 之前，后面的每条语句都被拒绝），所以**保存点**也用来在事务内部从预期的错误中恢复。大多数 **DDL** 语句在 PostgreSQL 和 SQLite 中是事务性的，所以连**模式**迁移也可以回滚；在 MySQL 和 Oracle 中，DDL 语句会隐式提交。

并发事务彼此能看到多少，是按事务设置的，在 PostgreSQL 中是 `BEGIN ISOLATION LEVEL SERIALIZABLE` 或 `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ`。各隔离级别及其允许的异常在 [4.13.11](/4.13.11) 中解释；PostgreSQL 的默认级别是 `READ COMMITTED`。

## 4.8. 授权

**数据库**服务器认识它的用户，并按用户的权限（privilege）检查每条语句。表上的 **SQL** 权限有 `SELECT`、`INSERT`、`UPDATE`、`DELETE`、`REFERENCES`（用来声明指向它的**外码**）和 `TRIGGER`；`SELECT`、`INSERT` 和 `UPDATE` 可以限制到列。权限用 `GRANT` 授予，用 `REVOKE` 收回（PostgreSQL 语法；这些语句需要服务器，这里没有运行）：

```sql
CREATE ROLE analyst;                          -- a group of users
CREATE ROLE lab_tech;
GRANT SELECT ON expression TO analyst;        -- read the view only
GRANT SELECT, INSERT ON sample, measurement TO lab_tech WITH GRANT OPTION;
CREATE ROLE alice LOGIN PASSWORD '...' IN ROLE analyst;
REVOKE INSERT ON measurement FROM lab_tech CASCADE;
```

角色（role）是可以授予用户和其他角色的、有名字的一组权限；在 PostgreSQL 中，用户就是带有 `LOGIN` 属性的角色。对象的所有者（创建者）拥有它上面的全部权限，并且可以授予它们；`WITH GRANT OPTION` 允许接受者把权限继续授予别人，`REVOKE ... CASCADE` 则把权限从所有通过被收回的授权得到它的人那里一并收回。只授予视图上的权限、不授予其基表上的权限，就恰好给出视图所暴露的行和列的访问权。PostgreSQL 还提供行级安全（row-level security）：在 `ALTER TABLE sample ENABLE ROW LEVEL SECURITY` 之后，像 `CREATE POLICY own_lab ON sample USING (lab = current_user)` 这样的策略把表上的每个查询限制在策略允许的行上。SQLite 和 DuckDB 之类的嵌入式数据库没有用户和权限；访问由数据库文件的权限控制（[4.11.7](/4.11.7)）。

最小权限原则适用：应用应当用一个只能做应用所需之事的角色连接，这样缺陷或攻击（§4.9）就不能删除表或读取无关的数据。

## 4.9. 从程序访问数据库

### 4.9.1. Python DB-API

**SQL** 不是通用语言，应用通过**数据库**接口，从宿主语言向 **DBMS** 发送 SQL 语句：Java 中是 JDBC，C 中是 ODBC，Python 中是 DB-API（PEP 249），`sqlite3`（标准库）、`psycopg`（PostgreSQL）和 `duckdb` 等驱动实现了它。模式到处相同：打开*连接*，通过它（或通过*游标*（cursor））执行语句，取回结果行，再提交或回滚。

```python
import sqlite3

con = sqlite3.connect("expr.db")
con.execute("PRAGMA foreign_keys = ON")

# A parameterized query: the driver sends the value separately from the SQL text.
symbol = "CDKN1A"
cur = con.execute(
    """SELECT s.sample_id, s.treatment, m.tpm
       FROM measurement AS m
            JOIN gene   AS g ON g.gene_id = m.gene_id
            JOIN sample AS s ON s.sample_id = m.sample_id
       WHERE g.symbol = ? AND m.tpm > ?
       ORDER BY m.tpm DESC""",
    (symbol, 50),
)
print([d[0] for d in cur.description])
for row in cur:
    print(row)

# Several rows in one call; the with-block commits on success and rolls back on error.
new_samples = [("S07", "kidney", "control", 39, "2025-04-01"),
               ("S08", "kidney", "treated", 44, "2025-04-01")]
with con:
    con.executemany("INSERT INTO sample VALUES (?, ?, ?, ?, ?)", new_samples)
print(con.execute("SELECT count(*) FROM sample").fetchone())

try:
    with con:
        con.execute("INSERT INTO sample VALUES ('S09', 'kidney', 'treated', 41, '2025-04-02')")
        con.execute("INSERT INTO measurement VALUES ('S09', 'no-such-gene', 1.0)")
except sqlite3.IntegrityError as e:
    print("rolled back:", e)
print(con.execute("SELECT count(*) FROM sample").fetchone())
con.close()
```

在 [4.13.3](/4.13.3#sec-3.2.3) 的数据库上用 Python 3.12 运行：

```text
['sample_id', 'treatment', 'tpm']
('S05', 'treated', 141.5)
('S06', 'treated', 120.8)
('S03', 'treated', 88.7)
(8,)
rolled back: FOREIGN KEY constraint failed
(8,)
```

行以 Python **元组**的形式到达，SQL 类型被转换为 Python 类型（`numeric` 在 SQLite 中变成 `float`，在 psycopg 中变成 `decimal.Decimal`），`NULL` 变成 `None`。第二个 `with` 块显示了事务的作用：失败的测量值使刚刚插入的样本回滚，计数仍为 8。DB-API 没有规定占位符的语法：`sqlite3` 用 `?` 或 `:name`，`psycopg` 用 `%s` 或 `%(name)s`。最小的 psycopg 3 程序形状相同（这里没有运行，因为它需要 PostgreSQL 服务器）：

```python
import psycopg

with psycopg.connect("dbname=expr") as conn:          # commits when the block ends
    rows = conn.execute(
        "SELECT sample_id, tpm FROM expression WHERE symbol = %s", ("MDM2",)
    ).fetchall()
```

对于分析，`pandas.read_sql(query, con, params=...)` 返回数据框（[4.4.5](/4.4.5)），DuckDB 可以直接查询 pandas 数据框和 Parquet 文件。打开服务器连接代价很高（在 PostgreSQL 中它要启动一个**进程**），所以 Web 应用保留一个由已打开连接构成的连接池（connection pool），并把连接借给各个请求。

### 4.9.2. SQL 注入

把用户输入粘贴进字符串来构造 SQL 语句，是数据库应用的经典安全漏洞。

**定义 4.9.1（SQL 注入）** **SQL 注入**是一种攻击：程序插入 SQL 语句文本中的输入被精心构造，以改变语句的结构，使数据库执行程序员并不想要的命令。

```python
import sqlite3

con = sqlite3.connect("expr.db")
user_input = "x' OR '1'='1"

# Wrong: the input becomes part of the SQL text.
unsafe = f"SELECT sample_id, donor_age FROM sample WHERE sample_id = '{user_input}'"
print(unsafe)
print(con.execute(unsafe).fetchall())

# Right: the input is bound as a value and can never change the statement.
safe = "SELECT sample_id, donor_age FROM sample WHERE sample_id = ?"
print(con.execute(safe, (user_input,)).fetchall())
con.close()
```

```text
SELECT sample_id, donor_age FROM sample WHERE sample_id = 'x' OR '1'='1'
[('S01', 54), ('S02', 61), ('S03', 58), ('S04', 47), ('S05', None), ('S06', 66)]
[]
```

输入中的引号结束了字符串字面量，其余部分变成了 SQL：条件恒为真，每一行都被返回。用其他输入，攻击者可以读取其他表（`' UNION SELECT ...`），或者在接口执行多条语句时修改数据。防御办法是参数化查询（parameterized query）：语句文本中含有占位符，值被单独发送，因此解析器从不把它们当作 SQL。参数只能代表值，不能代表表名或列名；当名字必须变化时，要对照固定的列表检查它，或用驱动的标识符引用函数（`psycopg.sql.Identifier`）加引号。手工转义引号不是防御。预备语句（prepared statement）更进一步：服务器只解析并规划语句一次（PostgreSQL 中的 `PREPARE`），然后用不同的参数多次执行，这也节省了规划时间。

### 4.9.3. 数据库内的代码与对象–关系映射

逻辑也可以在 DBMS 内部运行。用户自定义函数和存储过程（stored procedure）用 SQL 或过程式扩展编写（PostgreSQL 中的 PL/pgSQL，还有 PL/Python；Oracle 中的 PL/SQL；SQL Server 中的 T-SQL），并从查询中调用或用 `CALL` 调用。它们减少应用与服务器之间的往返，并把规则放在数据旁边，代价是多了一套用不那么方便的语言写的代码。触发器是数据改变时自动运行的过程，在 [4.13.6](/4.13.6#sec-6.1.4) 中讨论。

在另一端，对象–关系映射器（SQLAlchemy、Django ORM）让程序定义与表对应的类，并生成装入和保存对象的 SQL。它们消除了重复的代码和注入的风险，但隐藏了实际执行的查询：装入 100 个对象，再逐个装入它们的相关行，会发出 101 个查询，而不是一次**连接**（“N+1 问题”）。它们在 Web 应用中的使用属于软件工程（[4.14](/4.14)）。

## 小结

- 子查询返回一个值、一个集合或一张表。`IN`、`EXISTS` 和 `NOT EXISTS` 测试成员关系和存在性；相关子查询引用外层的行。当**子查询**返回**空值**时，`NOT IN` 永远不为真：应使用 `NOT EXISTS`。
- `UNION`、`INTERSECT` 和 `EXCEPT` 去除重复，它们的 `ALL` 形式遵循**多重集**的计数。除法用 `NOT EXISTS ... EXCEPT` 或在码约束下计数来写。
- `WITH` 给中间结果命名；`WITH RECURSIVE` 计算单调查询的最小不动点，由此可以表达传递闭包（祖先、子通路）。
- 窗口函数在分区上计算排名、累计与滑动聚集和偏移，而不合并行；它们在分组之后、`ORDER BY` 之前求值。
- `INSERT`、`UPDATE`、`DELETE`、`ON CONFLICT` 和 `MERGE` 修改数据；`RETURNING` 报告受影响的行。
- 视图是存储的查询，实现外模式；物化视图存储它的结果。
- `BEGIN`、`COMMIT`、`ROLLBACK` 和保存点划定事务的界限。`GRANT` 和 `REVOKE` 管理用户和角色对表和视图的权限。
- 程序使用 Python DB-API 之类的数据库接口；值始终作为参数传递，而不是粘贴进 SQL 文本，这样可以防止 SQL 注入。
