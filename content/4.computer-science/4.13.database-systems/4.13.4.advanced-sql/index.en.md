---
title: Advanced SQL
description: "SQL beyond SELECT–FROM–WHERE: scalar, IN, EXISTS and correlated subqueries and the NOT IN null trap, LATERAL; UNION, INTERSECT and EXCEPT and relational division in SQL; common table expressions and recursive queries over a pathway hierarchy; window functions for ranking, running and moving aggregates; INSERT, UPDATE, DELETE, upsert, MERGE and RETURNING; views and materialized views; transactions and savepoints; privileges, roles and row-level security; and database access from Python through the DB-API with parameterized queries against SQL injection."
---

The basic query block of [4.13.3](/4.13.3) is the building block of everything else in **SQL**. This chapter combines query blocks: nested inside each other as subqueries, connected by set operations, named and reused in `WITH` clauses, and applied recursively to follow a hierarchy to any depth. It then introduces window functions, which compute aggregates without collapsing rows and are indispensable in analytical work, and the statements that change data. The second half turns from queries to the **database** as a shared resource: views that give users their own **external schema** ([4.13.1](/4.13.1#sec-1.3.1)), transactions as SQL exposes them, access rights, and the way programs send SQL to a database safely. All examples use the running example of [4.13.3](/4.13.3#sec-3.2.3); as there, output comes from SQLite 3.45 unless it is marked as DuckDB 1.5.

## 4.1. Subqueries

### 4.1.1. Scalar, IN and EXISTS Subqueries

**Definition 4.1.1 (Subquery)** A **subquery** is a `SELECT` expression nested inside another statement. It may appear wherever a value, a set of values or a table is expected: in the `SELECT` list or a condition as a *scalar subquery* returning one value, after `IN` or `EXISTS` as a set, or in `FROM` as a *derived table*.

Membership in the result of a **subquery** is tested with `IN`. The genes annotated to pathway PW3:

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

`EXISTS (subquery)` is true if the subquery returns at least one row, and `NOT EXISTS` if it returns none; the `SELECT` list of the subquery is irrelevant and is conventionally `1`. These are the existential quantifiers of the relational calculus ([4.13.2](/4.13.2#sec-2.5)). The genes in no pathway:

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

The subquery refers to `g`, a table of the outer query.

**Definition 4.1.2 (Correlated Subquery)** A subquery is **correlated** if it refers to columns of an enclosing query. Its meaning is that it is evaluated once for each row of the enclosing query, with the outer columns fixed to the values in that row.

The most recently collected sample of each tissue compares each sample with the maximum date of its own tissue:

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

"Evaluated once per row" is the semantics, not the execution plan: optimizers routinely turn correlated `EXISTS` and `IN` subqueries into **joins**, *semijoins* (keep a row of $r$ if it has at least one partner in $s$) and *antijoins* (keep it if it has none), which can be computed with the hash and merge algorithms of [4.13.9](/4.13.9). A scalar subquery must return at most one row, or the statement fails at run time; with no row it yields **null**.

The comparison operators can also be combined with `ANY` (`SOME`) and `ALL`: `x > ALL (subquery)` is true if `x` is larger than every value returned. SQLite does not support them (output from DuckDB):

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

### 4.1.2. The NOT IN Trap

`x NOT IN (subquery)` means `x <> v` for every value `v` of the subquery. If one of those values is null, `x <> NULL` is unknown, so the whole condition is never true. In the running example, the pathways that are not the parent of any pathway should be the three leaves (p53-dependent G1 arrest, EGFR signaling, Glycolysis), but `parent_id` contains nulls:

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

`NOT EXISTS` has no such problem, because it asks only whether a matching row exists. The rule is to write `NOT EXISTS`, or to exclude the nulls explicitly (`WHERE parent_id IS NOT NULL` in the subquery), whenever the subquery's column is nullable. `IN` is not affected, since `x = NULL` being unknown only fails to add a match.

### 4.1.3. Subqueries in FROM and LATERAL

A subquery in `FROM` is a derived table and must be given a name. It is how a query filters on the result of a window function (§4.4) or aggregates an aggregate. A plain derived table cannot refer to the other tables of the same `FROM` clause; a `LATERAL` subquery (SQL:1999; PostgreSQL, DuckDB, MySQL 8) can, and is then evaluated for each row of the tables to its left. A typical use is "top $k$ per group", here the two most highly expressed genes per sample apart from the housekeeping genes (output from DuckDB):

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

## 4.2. Set Operations

### 4.2.1. UNION, INTERSECT and EXCEPT

The set operations of the **relational algebra** combine the results of two queries with the same number of columns and compatible types: `UNION`, `INTERSECT` and `EXCEPT` (Oracle before 21c: `MINUS`). They eliminate duplicates; the `ALL` variants keep them, with **multiset** semantics: if a row occurs $m$ times in the first and $n$ times in the second input, `UNION ALL` returns it $m + n$ times, `INTERSECT ALL` $\min(m, n)$ times and `EXCEPT ALL` $\max(m - n, 0)$ times. SQLite supports only `UNION ALL` among the `ALL` forms.

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

`UNION ALL` is much cheaper than `UNION` because it needs no duplicate elimination; it is the right choice whenever the inputs cannot overlap or duplicates are wanted. The column names of the result are those of the first query, and an `ORDER BY` at the end applies to the combined result.

`EXCEPT` expresses negation directly. All (sample, gene) combinations that were *not* measured are the **Cartesian product** minus the measured pairs:

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

### 4.2.2. Division in SQL

**SQL** has no **division** operator ([4.13.2](/4.13.2#sec-2.3.2)). "Samples in which every gene was measured" is written in one of two ways. The first follows the logic of the definition: a sample qualifies if the set of all genes, minus the genes measured in it, is empty.

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

The equivalent double negation, "no gene exists that was not measured in the sample", replaces `EXCEPT` by a second `NOT EXISTS`. The second way counts, and is correct only because the **primary key** of `measurement` guarantees at most one row per (sample, gene) pair and the **foreign key** guarantees that every measured gene exists:

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

## 4.3. Common Table Expressions and Recursion

### 4.3.1. The WITH Clause

**Definition 4.3.1 (Common Table Expression)** A **common table expression** (CTE) is a named query defined in a `WITH` clause before the main statement, `WITH name (columns) AS (query) statement`; within the statement, and within later CTEs of the same clause, the name denotes the result of the query.

**CTEs** are the **SQL** form of the assignment operation of the **relational algebra**. They let a long query be read top to bottom as a sequence of steps instead of inside out. The treated samples in which a gene is more than three times as high as the mean of the control samples of the same tissue:

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

Whether a CTE is computed once and stored or expanded into the main query like a view is up to the system. PostgreSQL 12 and later inline a CTE that is referenced once and has no **side effects**, and accept `AS MATERIALIZED` and `AS NOT MATERIALIZED` to override the choice. A CTE may also contain `INSERT`, `UPDATE` or `DELETE ... RETURNING` in PostgreSQL ("data-modifying CTEs").

### 4.3.2. Recursive Queries

The relational algebra cannot compute the **transitive closure** of a **relation** ([4.13.2](/4.13.2#sec-2.5)), yet hierarchies and graphs are everywhere: pathways within pathways, a gene ontology, a phylogenetic tree, the prerequisites of courses. SQL:1999 added recursion to the `WITH` clause.

**Definition 4.3.2 (Recursive Query)** A **recursive query** is a common table expression introduced by `WITH RECURSIVE` whose query is the union of a nonrecursive *base* query and a *recursive* query that refers to the CTE itself. Its value is the smallest relation $T$ that contains the result of the base query and is closed under the recursive query, that is, the least fixed point of $T = \mathit{base} \cup f(T)$.

The fixed point is computed by iteration: start with $T_0 = \mathit{base}$, compute $\Delta_{i+1} = f(\Delta_i)$ from the rows added in the previous round (with `UNION`, minus the rows already in $T$), add them, and stop when a round adds nothing. This *semi-naive* evaluation terminates whenever the result is finite and no round can produce new rows forever. All ancestors of every pathway, with the distance:

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

The first round finds the parents, the second the grandparent of PW3, and the third round finds nothing, because PW1 has no parent. A common application in annotation **databases** is to count a gene as a member of a pathway when it is annotated to any of its sub-pathways. All genes in "Cell cycle" or below it:

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

Directly annotated to "Cell cycle" is only MYC; the other four genes come from the checkpoint pathways beneath it.

The standard restricts the **recursive query** so that the fixed point exists: the recursive reference may occur only once, and not inside an aggregate, `NOT EXISTS`, `EXCEPT` or the nullable side of an outer **join**. These are exactly the non-monotone constructs of [4.13.2](/4.13.2#sec-2.4); with monotone $f$, adding rows to $T$ can only add rows to $f(T)$, and the iteration converges to the least fixed point. In data with cycles (a general graph rather than a tree) `UNION ALL` would loop forever; `UNION` stops because revisited rows are discarded, as long as the rows do not carry a growing value such as `depth`. PostgreSQL 14 and later also provide the standard `CYCLE` clause, which marks and stops at revisited rows, and `SEARCH DEPTH FIRST` / `BREADTH FIRST` for the output order.

## 4.4. Window Functions

### 4.4.1. Windows

**Aggregation** with `GROUP BY` returns one row per group. Many analytical questions need the aggregate next to each row instead: the rank of a gene within its sample, its share of the sample's total, the change from the previous time point.

**Definition 4.4.1 (Window Function)** A **window function** computes, for each row of a query result, a value from a set of related rows, its *window*, without merging the rows. The window is specified by `OVER (PARTITION BY ... ORDER BY ... frame)`: the partition consists of the rows with the same values of the `PARTITION BY` expressions, ordered by `ORDER BY`, and the optional *frame* restricts the window to rows near the current one in that order.

**Window functions** are evaluated after `WHERE`, `GROUP BY` and `HAVING`, and before `DISTINCT`, `ORDER BY` and `LIMIT` ([4.13.3](/4.13.3#sec-3.8)). They may therefore appear only in the `SELECT` list and in `ORDER BY`; to filter on them, a derived table or **CTE** is needed. They were added in SQL:2003 and are supported by PostgreSQL, SQLite (3.25 and later), DuckDB and MySQL 8.

### 4.4.2. Ranking

`row_number()` numbers the rows of each partition $1, 2, 3, \dots$; `rank()` gives equal values the same rank and leaves gaps after ties (1, 2, 2, 4), `dense_rank()` does not leave gaps (1, 2, 2, 3); `ntile(n)` divides the partition into $n$ buckets. The genes of two samples ranked by expression:

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

Filtering on a rank answers "top $k$ per group" portably, without `LATERAL`. The most highly expressed non-housekeeping gene of each sample:

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

This replaces the non-portable "bare column" query of [4.13.3](/4.13.3#sec-3.6.2). With `row_number()` ties are broken arbitrarily; with `rank()` all tied rows are returned.

### 4.4.3. Aggregates over Windows

Every **aggregate function** can be used as a window function. Without `ORDER BY` in the window, it is computed over the whole partition, which gives each gene's share of the sample's total:

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

Standardizing each gene across samples (the $z$-score $(x - \bar x)/s$ used before clustering or drawing a heat map) needs the mean and the standard deviation of the gene's partition. The `WINDOW` clause names a window used several times (output from DuckDB; SQLite has no `stddev_samp`):

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

### 4.4.4. Frames and Offsets

With `ORDER BY` in the window, the default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: from the start of the partition up to the current row *and its peers* (rows equal in the ordering). This turns `sum` into a running total. An explicit frame such as `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW` gives a moving window of two rows. The offset functions `lag(x)` and `lead(x)` return `x` from the previous and the next row of the partition, and `first_value`, `last_value` and `nth_value` other positions of the frame. For TP53 in collection order:

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

The first row has no predecessor, so `lag` returns **null** and so does the difference. The ordering includes `sample_id` to make it total: S01 and S02 were collected on the same day, and without the tie-breaker their order, and with it the moving average, would be unspecified. The default `RANGE` frame treats such peers as one unit, which is why `last_value` over the default frame often surprises: it returns the last peer of the current row, not the last row of the partition.

## 4.5. Modifying Data

### 4.5.1. INSERT, UPDATE and DELETE

`INSERT INTO t (columns) VALUES (...), (...)` adds rows; omitted columns receive their default (**null** if none is declared). `INSERT INTO t (columns) SELECT ...` adds the result of a query, as the measurements were loaded in [4.13.3](/4.13.3#sec-3.2.3). `UPDATE t SET column = expression WHERE condition` changes the rows satisfying the condition, and `DELETE FROM t WHERE condition` removes them; without `WHERE`, every row is affected. The clause `RETURNING` (PostgreSQL, SQLite 3.35 and later, DuckDB; not MySQL) returns the inserted, updated or deleted rows, for example the values filled in by defaults or **identity columns**; in PostgreSQL 18 it can return both the `OLD` and the `NEW` values of an updated row.

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

The last statement is rejected because measurements still refer to S01. An `UPDATE` evaluates all its expressions on the old values of a row before changing it, so `UPDATE t SET a = b, b = a` swaps the two columns (MySQL is an exception: it assigns from left to right and uses the already updated `a`).

### 4.5.2. Upsert and MERGE

Loading data often means "insert the row, or update it if a row with this key already exists". PostgreSQL (9.5 and later) and SQLite (3.24 and later) offer `INSERT ... ON CONFLICT`, in which the pseudo-table `excluded` holds the row that could not be inserted:

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

`ON CONFLICT DO NOTHING` skips the conflicting rows instead; MySQL writes `INSERT ... ON DUPLICATE KEY UPDATE`. The standard statement is `MERGE` (SQL:2003; PostgreSQL 15 and later, DuckDB, Oracle, SQL Server), which matches a source table against the target and specifies an action for matched and unmatched rows:

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

The two forms differ under concurrency: `ON CONFLICT` relies on a unique index and is guaranteed to either insert or update even when another session inserts the same key at the same moment, whereas `MERGE` in PostgreSQL can fail with a unique-key violation in that situation. For bulk loading, both are much slower than the dedicated commands (`COPY` in PostgreSQL and DuckDB, `.import` in the SQLite shell).

## 4.6. Views

**Definition 4.6.1 (View)** A **view** is a named query stored in the catalog, `CREATE VIEW name AS query`. A view is a virtual relation: it stores no rows, and a query that refers to it is evaluated as if the view's definition were substituted for its name.

Views serve two purposes. They simplify: the three-way **join** that almost every analysis of the running example begins with can be defined once. And they are the **external schemas** of the **three-schema architecture** ([4.13.1](/4.13.1#sec-1.3)): a user can be given access to a view without access to the underlying tables, for example to expression values without the donor ages. When the base tables change, so does the content of the view, and a changed base schema can be hidden behind a view with the old shape, which is how logical data independence is achieved in practice.

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

Updates through a view are a problem in general: an update of a join or an aggregate does not determine a unique change of the base tables. SQLite views are read-only (an `INSTEAD OF` trigger can implement updates by hand, [4.13.6](/4.13.6#sec-6.1.4)). PostgreSQL automatically makes a view updatable if it selects from a single table without **aggregation**, `DISTINCT`, set operations or `LIMIT`; `WITH CHECK OPTION` then rejects inserted or updated rows that would not be visible through the view.

A *materialized view* stores its result like a table: `CREATE MATERIALIZED VIEW gene_summary AS SELECT ...` in PostgreSQL, recomputed by `REFRESH MATERIALIZED VIEW gene_summary`. It trades freshness for speed, and is used for expensive summaries that are read often and may be slightly out of date. Keeping a materialized view up to date incrementally, by applying only the changes of the base tables, is called *view maintenance*; PostgreSQL recomputes the whole view, whereas commercial systems and some extensions maintain views incrementally.

## 4.7. Transactions in SQL

A transaction is a sequence of statements that the **DBMS** executes as a unit: either all of their effects become permanent or none do, and concurrent transactions do not see each other's intermediate states. Their theory, the ACID properties, schedules and serializability, is the subject of [4.13.10](/4.13.10); this section shows the statements.

In standard **SQL** a transaction begins implicitly with the first statement; in PostgreSQL, SQLite, DuckDB and MySQL every statement outside an explicit transaction is its own transaction (*autocommit*), and `BEGIN` (standard: `START TRANSACTION`) starts a multi-statement one. `COMMIT` makes its changes permanent, `ROLLBACK` undoes all of them:

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

A *savepoint* marks a point inside a transaction to which it can be rolled back partially, without abandoning the earlier work:

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

The new sample is kept and its measurement is not. In PostgreSQL, a failed statement aborts the whole transaction (every later statement is refused until `ROLLBACK`), so **savepoints** are also used to recover from an expected error inside a transaction. Most **DDL** statements are transactional in PostgreSQL and SQLite, so even a **schema** migration can be rolled back; in MySQL and Oracle a DDL statement commits implicitly.

How much concurrent transactions may see of each other is set per transaction, `BEGIN ISOLATION LEVEL SERIALIZABLE` or `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ` in PostgreSQL. The levels and the anomalies they allow are explained in [4.13.11](/4.13.11); the PostgreSQL default is `READ COMMITTED`.

## 4.8. Authorization

A **database** server knows its users and checks every statement against their *privileges*. The **SQL** privileges on a table are `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `REFERENCES` (to declare a **foreign key** to it) and `TRIGGER`; `SELECT`, `INSERT` and `UPDATE` can be restricted to columns. Privileges are given with `GRANT` and withdrawn with `REVOKE` (PostgreSQL syntax; these statements need a server and were not run here):

```sql
CREATE ROLE analyst;                          -- a group of users
CREATE ROLE lab_tech;
GRANT SELECT ON expression TO analyst;        -- read the view only
GRANT SELECT, INSERT ON sample, measurement TO lab_tech WITH GRANT OPTION;
CREATE ROLE alice LOGIN PASSWORD '...' IN ROLE analyst;
REVOKE INSERT ON measurement FROM lab_tech CASCADE;
```

A *role* is a named set of privileges that can be granted to users and to other roles; in PostgreSQL users are simply roles with the `LOGIN` attribute. The owner of an object (its creator) has all privileges on it and can grant them; `WITH GRANT OPTION` allows the recipient to pass a privilege on, and `REVOKE ... CASCADE` withdraws it also from everyone who received it through the revoked grant. Granting privileges on a view but not on its base tables gives access to exactly the rows and columns the view exposes. PostgreSQL also offers *row-level security*: after `ALTER TABLE sample ENABLE ROW LEVEL SECURITY`, a policy such as `CREATE POLICY own_lab ON sample USING (lab = current_user)` restricts every query on the table to the rows the policy admits. Embedded databases such as SQLite and DuckDB have no users or privileges; access is controlled by the permissions of the database file ([4.11.7](/4.11.7)).

The principle of least privilege applies: an application should connect with a role that may do what the application needs and nothing more, so that a bug or an attack (§4.9) cannot drop tables or read unrelated data.

## 4.9. Accessing Databases from Programs

### 4.9.1. The Python DB-API

**SQL** is not a general-purpose language, and applications send SQL statements to the **DBMS** from a host language through a **database** interface: JDBC in Java, ODBC in C, and in Python the DB-API (PEP 249), which drivers such as `sqlite3` (standard library), `psycopg` (PostgreSQL) and `duckdb` implement. The pattern is the same everywhere: open a *connection*, execute statements through it (or through a *cursor*), fetch the result rows, and commit or roll back.

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

Run with Python 3.12 on the database of [4.13.3](/4.13.3#sec-3.2.3):

```text
['sample_id', 'treatment', 'tpm']
('S05', 'treated', 141.5)
('S06', 'treated', 120.8)
('S03', 'treated', 88.7)
(8,)
rolled back: FOREIGN KEY constraint failed
(8,)
```

Rows arrive as Python **tuples**, with SQL types converted to Python types (`numeric` becomes a `float` in SQLite, a `decimal.Decimal` in psycopg) and `NULL` to `None`. The second `with` block shows the transaction at work: the failing measurement rolls back the sample inserted just before it, and the count stays at 8. The DB-API does not fix the placeholder syntax: `sqlite3` uses `?` or `:name`, `psycopg` uses `%s` or `%(name)s`. A minimal psycopg 3 program has the same shape (not run here, since it needs a PostgreSQL server):

```python
import psycopg

with psycopg.connect("dbname=expr") as conn:          # commits when the block ends
    rows = conn.execute(
        "SELECT sample_id, tpm FROM expression WHERE symbol = %s", ("MDM2",)
    ).fetchall()
```

For analysis, `pandas.read_sql(query, con, params=...)` returns a data frame ([4.4.5](/4.4.5)), and DuckDB queries pandas data frames and Parquet files directly. A server connection is expensive to open (in PostgreSQL it starts a **process**), so web applications keep a *connection pool* of open connections and lend them to requests.

### 4.9.2. SQL Injection

Building an SQL statement by pasting user input into a string is the classic security hole of database applications.

**Definition 4.9.1 (SQL Injection)** **SQL injection** is an attack in which input that a program inserts into the text of an SQL statement is crafted so that it changes the statement's structure, making the database execute commands the programmer did not intend.

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

The quote in the input closes the string literal, and the rest becomes SQL: the condition is always true and every row is returned. With other inputs an attacker can read other tables (`' UNION SELECT ...`) or, where the interface executes several statements, modify data. The defense is the *parameterized query*: the statement text contains placeholders, and the values are sent separately, so that the parser never sees them as SQL. Parameters can stand only for values, not for table or column names; when a name must vary, it is checked against a fixed list or quoted with the driver's identifier-quoting function (`psycopg.sql.Identifier`). Escaping quotes by hand is not a defense. A *prepared statement* goes one step further: the server parses and plans the statement once (`PREPARE` in PostgreSQL) and executes it many times with different parameters, which also saves planning time.

### 4.9.3. Code inside the Database and Object–Relational Mapping

Logic can also run inside the DBMS. User-defined functions and *stored procedures* are written in SQL or in a procedural extension (PL/pgSQL in PostgreSQL, also PL/Python; PL/SQL in Oracle; T-SQL in SQL Server) and called from queries or with `CALL`. They reduce round trips between application and server and keep rules next to the data, at the cost of a second code base in a less convenient language. Triggers, procedures that run automatically when data change, are treated in [4.13.6](/4.13.6#sec-6.1.4).

At the other end, object–relational mappers (SQLAlchemy, the Django ORM) let a program define classes that correspond to tables and generate the SQL for loading and saving objects. They remove repetitive code and the risk of injection, but hide which queries are executed: loading 100 objects and then their related rows one by one issues 101 queries instead of one **join** (the "N+1 problem"). Their use in web applications is part of software engineering ([4.14](/4.14)).

## Summary

- Subqueries return a value, a set or a table. `IN`, `EXISTS` and `NOT EXISTS` test membership and existence; correlated subqueries refer to the outer row. `NOT IN` is never true when the **subquery** returns a **null**: use `NOT EXISTS`.
- `UNION`, `INTERSECT` and `EXCEPT` remove duplicates, their `ALL` forms follow **multiset** counts. Division is written with `NOT EXISTS ... EXCEPT` or by counting under a key constraint.
- `WITH` names intermediate results; `WITH RECURSIVE` computes the least fixed point of a monotone query, which expresses transitive closure (ancestors, sub-pathways).
- Window functions compute ranks, running and moving aggregates and offsets over a partition without collapsing rows; they are evaluated after grouping and before `ORDER BY`.
- `INSERT`, `UPDATE`, `DELETE`, `ON CONFLICT` and `MERGE` change data; `RETURNING` reports the affected rows.
- A view is a stored query and implements an external schema; a materialized view stores its result.
- `BEGIN`, `COMMIT`, `ROLLBACK` and savepoints delimit transactions. `GRANT` and `REVOKE` manage privileges on tables and views for users and roles.
- Programs use a database interface such as the Python DB-API; values are always passed as parameters, never pasted into the SQL text, which prevents SQL injection.
