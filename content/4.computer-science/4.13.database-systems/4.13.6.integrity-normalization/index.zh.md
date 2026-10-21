---
title: 完整性约束与规范化
description: 数据库如何保证数据正确，以及如何识别好的关系模式：域完整性、实体完整性与参照完整性（含 ON DELETE 动作与延迟检查）、断言与触发器；更新异常；函数依赖、Armstrong 公理及其可靠性与完备性的证明、属性闭包、正则覆盖；无损分解与保持依赖；第一、第二、第三范式与 BC 范式及其分解与合成算法；多值依赖与第四范式；把实验室电子表格逐步规范化为运行示例的完整过程。
source_hash: 25877837744c
---

如果**数据库**能够记录世界的每一种合法状态，并且只记录合法状态，同时不把任何事实存储两次，那么**模式**就是好的。本章处理这句话的两个方面。第一部分说明完整性约束和触发器如何让 **DBMS** 自己拒绝非法数据，而不是信任每一个写数据库的程序。第二部分发展函数依赖理论，它使“把事实存储两次”变得精确，并引出范式（保证这种冗余不会出现的模式条件），以及把坏模式分解为好模式而不丢失信息的算法。[4.13.5](/4.13.5) 的 E-R 设计通常产生已经规范化的模式；规范化是检验它是否如此的手段，也是以现有的表（如电子表格）为起点时的首选方法。例子使用 [4.13.3](/4.13.3#sec-3.2.3) 的运行示例；所用的逻辑和集合论见 [1.1](/1.1) 和 [1.2](/1.2)。

## 6.1. 完整性约束

### 6.1.1. 域约束与实体完整性

**定义 6.1.1（完整性约束）** **完整性约束**是数据库的每个合法实例都必须满足的条件。DBMS 在数据库被修改时检查已声明的约束，并拒绝违反约束的修改。

**SQL** 能在 `CREATE TABLE` 中声明的约束已在 [4.13.3](/4.13.3#sec-3.2.2) 中列出。它们分为几类：

- *域约束*限制列的取值：数据类型、`NOT NULL`，以及对列的 `CHECK` 条件，如 `CHECK (tpm >= 0)`。PostgreSQL 可以为受约束的类型命名以便复用，`CREATE DOMAIN tpm_value AS numeric(10, 2) CHECK (VALUE >= 0)`。
- *码约束*：`PRIMARY KEY` 与 `UNIQUE`。
- **参照完整性**：`FOREIGN KEY ... REFERENCES`（§6.1.2）。
- *元组约束*：涉及一行中多个列的 `CHECK` 条件，如 `CHECK (start_pos <= end_pos)`。

**定义 6.1.2（实体完整性）** **实体完整性**规则要求关系的主码中没有任何属性为空。

由于**主码**是标识和引用**元组**的方式，码为**空值**的元组无法被可靠地引用；SQL 通过让 `PRIMARY KEY` 蕴含 `NOT NULL` 来强制这一规则（SQLite 是例外，见 [4.13.3](/4.13.3#sec-3.2.2)）。`CHECK` 条件在求值为真*或未知*时被满足（[4.13.2](/4.13.2#sec-2.6)），所以 `CHECK (donor_age BETWEEN 0 AND 120)` 允许年龄为空；若该值必须存在，还要加上 `NOT NULL`。标准允许在 `CHECK` 中使用子查询，但没有主流系统实现它，因为关于其他行的条件在那些行变化时都要重新检查。

### 6.1.2. 参照完整性与参照动作

**外码**（[4.13.2](/4.13.2#sec-2.2.2)）可能从两方面被违反：插入或更新的引用行，其值在被引用的表中不存在；删除或更新仍被引用的被引用行。前者总是被拒绝。对后者，外码声明选择一种*参照动作*：

| 动作（`ON DELETE ...` / `ON UPDATE ...`） | 被引用行被删除或其码改变时的效果 |
|---|---|
| `NO ACTION`（默认） | 若检查约束时仍有引用，则拒绝该修改（在语句结束时检查；若为延迟约束，则在事务结束时检查） |
| `RESTRICT` | 立即拒绝，即使该语句自己会消除这些引用 |
| `CASCADE` | 同时删除引用行（或把它们的外码改为新值） |
| `SET NULL` | 把引用行的外码置为空 |
| `SET DEFAULT` | 把它置为该列的默认值 |

`CASCADE` 适用于从属数据，如样本的等份，[4.13.5](/4.13.5#sec-5.5) 的**弱实体集**就是这样声明的；对测量值则很危险，测量是不应该因为样本行被误删而悄悄消失的结果。在下面的 SQLite 会话中，删除样本会删除它的等份，而删除仍有测量的样本会被默认动作拒绝：

```sql
CREATE TABLE aliquot (
    sample_id  text REFERENCES sample (sample_id) ON DELETE CASCADE,
    aliquot_no integer CHECK (aliquot_no >= 1),
    PRIMARY KEY (sample_id, aliquot_no)
);
INSERT INTO sample VALUES ('S07', 'kidney', 'control', 39, '2025-04-01');
INSERT INTO aliquot VALUES ('S07', 1), ('S07', 2), ('S03', 1);

DELETE FROM sample WHERE sample_id = 'S07';   -- cascades to both aliquots of S07
SELECT * FROM aliquot;
DELETE FROM sample WHERE sample_id = 'S03';   -- measurements still refer to S03
```

```text
+-----------+------------+
| sample_id | aliquot_no |
+-----------+------------+
| S03       | 1          |
+-----------+------------+
Runtime error near line 11: FOREIGN KEY constraint failed (19)
```

外码通常在每条语句结束时检查。把它声明为 `DEFERRABLE INITIALLY DEFERRED`（PostgreSQL、SQLite；在 PostgreSQL 中还可以用 `SET CONSTRAINTS ... DEFERRED` 按事务切换）会把检查推迟到事务提交时。这对循环引用是必需的，例如两张互相引用的表，它也本可以让 [4.13.3](/4.13.3#sec-3.2.3) 的通路在一个事务内以任意顺序插入。MySQL 的 InnoDB 逐行检查外码，不支持延迟。

### 6.1.3. 断言

**定义 6.1.3（断言）** **断言**是对整个数据库的命名条件，`CREATE ASSERTION name CHECK (condition)`，数据库必须始终满足它。

每个约束都可以表示为**断言**。例如，“每个样本至少有一个测量”写作

```sql
CREATE ASSERTION every_sample_measured CHECK (
    NOT EXISTS (SELECT * FROM sample AS s
                WHERE NOT EXISTS (SELECT * FROM measurement AS m
                                  WHERE m.sample_id = s.sample_id)));
```

断言自 SQL-92 起就是 SQL 标准的一部分，但三十年来没有广泛使用的系统实现它，因为在每次修改后高效地检查任意条件很困难：朴素的实现会在每次插入、更新和删除时重新计算整个查询。Oracle AI Database 26ai（2026）是第一个支持 `CREATE ASSERTION` 的主流系统，对允许的查询有所限制；PostgreSQL、MySQL、SQLite 和 SQL Server 都拒绝该语句。在这些系统中，这类条件由触发器、应用代码，或通过重构**模式**使更简单的约束就够用来强制。

### 6.1.4. 触发器

**定义 6.1.4（触发器）** **触发器**是 DBMS 在数据库被修改时作为副作用自动执行的语句。它由*事件*（对表的 `INSERT`、`UPDATE` 或 `DELETE`，可限于某些列）、触发的*条件*和*动作*指定；这就是事件–条件–动作模型。

**触发器**在事件之前（`BEFORE`）或之后（`AFTER`）触发，`FOR EACH ROW`（每个受影响的行触发一次，可通过 `OLD` 和 `NEW` 访问旧行和新行）或 `FOR EACH STATEMENT`；视图上的 `INSTEAD OF` 触发器用它的动作取代对视图的修改。常见的用途是记录测量值变更的审计日志。在 SQLite 中，动作直接内联书写：

```sql
CREATE TABLE measurement_log (
    sample_id  text,
    gene_id    text,
    old_tpm    numeric(10, 2),
    new_tpm    numeric(10, 2),
    changed_at text DEFAULT (datetime('now'))
);

CREATE TRIGGER log_tpm_change
AFTER UPDATE OF tpm ON measurement
FOR EACH ROW
WHEN OLD.tpm <> NEW.tpm
BEGIN
    INSERT INTO measurement_log (sample_id, gene_id, old_tpm, new_tpm)
    VALUES (OLD.sample_id, OLD.gene_id, OLD.tpm, NEW.tpm);
END;

UPDATE measurement SET tpm = 36.0 WHERE sample_id = 'S01' AND gene_id = 'ENSG00000141510';
UPDATE measurement SET tpm = tpm WHERE sample_id = 'S02';   -- no real change: not logged
SELECT sample_id, gene_id, old_tpm, new_tpm FROM measurement_log;
```

```text
+-----------+-----------------+---------+---------+
| sample_id |     gene_id     | old_tpm | new_tpm |
+-----------+-----------------+---------+---------+
| S01       | ENSG00000141510 | 35.2    | 36      |
+-----------+-----------------+---------+---------+
```

在 PostgreSQL 中，动作是用 PL/pgSQL（或其他过程语言）写的函数，触发器引用它；时间戳应是 `timestamptz DEFAULT now()` 列：

```sql
CREATE FUNCTION log_tpm_change() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO measurement_log (sample_id, gene_id, old_tpm, new_tpm)
    VALUES (OLD.sample_id, OLD.gene_id, OLD.tpm, NEW.tpm);
    RETURN NEW;
END $$;

CREATE TRIGGER log_tpm_change
AFTER UPDATE OF tpm ON measurement
FOR EACH ROW
WHEN (OLD.tpm IS DISTINCT FROM NEW.tpm)
EXECUTE FUNCTION log_tpm_change();
```

`INSTEAD OF` 触发器使 [4.13.4](/4.13.4#sec-4.6) 的只读视图 `expression` 对一种含义明显的修改可更新，即设置某个样本中某个基因的值：

```sql
CREATE VIEW expression AS
SELECT s.sample_id, s.tissue, s.treatment, g.symbol, m.tpm
FROM measurement AS m
     JOIN sample AS s ON s.sample_id = m.sample_id
     JOIN gene   AS g ON g.gene_id = m.gene_id;

CREATE TRIGGER expression_update
INSTEAD OF UPDATE OF tpm ON expression
BEGIN
    UPDATE measurement SET tpm = NEW.tpm
    WHERE sample_id = OLD.sample_id
      AND gene_id = (SELECT gene_id FROM gene WHERE symbol = OLD.symbol);
END;

UPDATE expression SET tpm = 9.0 WHERE sample_id = 'S04' AND symbol = 'MDM2';
SELECT sample_id, symbol, tpm FROM expression WHERE symbol = 'MDM2' AND tissue = 'lung';
```

```text
+-----------+--------+------+
| sample_id | symbol | tpm  |
+-----------+--------+------+
| S04       | MDM2   | 9    |
| S05       | MDM2   | 36.8 |
| S06       | MDM2   | 33.1 |
+-----------+--------+------+
```

触发器功能强大，也容易误用。它们适合审计日志、维护汇总表之类的派生数据，以及强制无法声明的约束。它们不适合取代声明式约束（`CHECK` 或 `FOREIGN KEY` 更短、无法绕过、在目录中可见，并且可被优化器利用），也不适合取代应用逻辑：不可见地发生、可能经其他触发器级联的动作使系统难以理解。触发器还可能被绕过：PostgreSQL 在应用逻辑复制收到的变更时不触发普通触发器，批量加载常在禁用触发器的情况下运行，所以仅靠触发器强制的约束在这类操作之后必须另行检查。

## 6.2. 冗余与异常

假设实验室把全部数据放在一张大表中，就像电子表格那样：每个测量一行，样本和基因的属性以及基因所属的通路在每行中重复。下面的查询由运行示例构造这张表（属于两条通路的基因产生两行；不属于任何通路的基因产生一行，通路列为**空值**）：

```sql
CREATE TABLE results AS
SELECT s.sample_id, s.tissue, s.treatment, s.donor_age, s.collected_on,
       g.gene_id, g.symbol, g.chrom, g.start_pos, g.end_pos, g.strand, m.tpm,
       p.pathway_id, p.name AS pathway_name, p.parent_id
FROM measurement AS m
     JOIN sample AS s ON s.sample_id = m.sample_id
     JOIN gene   AS g ON g.gene_id = m.gene_id
     LEFT JOIN gene_pathway AS gp ON gp.gene_id = g.gene_id
     LEFT JOIN pathway      AS p  ON p.pathway_id = gp.pathway_id;

SELECT count(*) AS n_rows,
       count(*) FILTER (WHERE sample_id = 'S01') AS rows_with_s01,
       count(*) FILTER (WHERE symbol = 'TP53') AS rows_with_tp53
FROM results;

SELECT sample_id, tissue, symbol, tpm, pathway_name FROM results
WHERE sample_id = 'S01' ORDER BY symbol, pathway_name LIMIT 6;
```

```text
+--------+---------------+----------------+
| n_rows | rows_with_s01 | rows_with_tp53 |
+--------+---------------+----------------+
| 58     | 10            | 12             |
+--------+---------------+----------------+
+-----------+--------+--------+--------+-------------------------+
| sample_id | tissue | symbol |  tpm   |      pathway_name       |
+-----------+--------+--------+--------+-------------------------+
| S01       | liver  | ACTB   | 2210   | NULL                    |
| S01       | liver  | BRCA1  | 1.8    | Cell cycle checkpoints  |
| S01       | liver  | CDKN1A | 12.4   | p53-dependent G1 arrest |
| S01       | liver  | EGFR   | 15.6   | EGFR signaling          |
| S01       | liver  | GAPDH  | 1520.4 | Glycolysis              |
| S01       | liver  | MDM2   | 8.1    | p53-dependent G1 arrest |
+-----------+--------+--------+--------+-------------------------+
```

“S01 是肝脏样本”这一事实被存储了 10 次，TP53 的位置被存储了十二次。这样的冗余会引起三类*异常*：

- 更新异常（update anomaly）：更正 S01 的组织需要修改十行；只修改其中一部分会使**数据库**不一致，同一个样本有了两种不同的组织。
- 插入异常（insertion anomaly）：新样本在第一个测量出现之前无法记录，新通路在有基因被注释到它之前也无法记录，除非把其他列填成空值，而这又必须允许出现在本应是码的部分中。
- 删除异常（deletion anomaly）：删除只被测量过一次的基因的测量值，同时也删除了该基因的位置和通路的唯一记录。

补救办法是把这张表*分解*成几张较小的表，每张只关于一类事物，运行示例就是这样做的。以消除这类冗余为目标、由**属性**之间的依赖引导，把**模式**替换为它的分解，称为*规范化*（*normalization*）。本章其余部分回答由此提出的问题：哪些分解是正确的，哪些是好的，以及如何系统地找到它们。

## 6.3. 函数依赖

### 6.3.1. 定义

上面的冗余产生的原因是某些**属性**决定了另一些属性：样本标识符决定组织，所以每个含 S01 的行都必须重复“liver”。函数依赖陈述的就是这类事实。

**定义 6.3.1（函数依赖）** 设 $R$ 是关系模式，$\alpha, \beta \subseteq R$。若对所有元组 $t_1, t_2 \in r$，

$$
t_1[\alpha] = t_2[\alpha] \implies t_1[\beta] = t_2[\beta],
$$
则称关系 $r(R)$ *满足* **函数依赖** $\alpha \to \beta$。若 $R$ 上的每个合法**关系**都满足它，则称该**函数依赖**在 $R$ 上*成立*。若 $\beta \subseteq \alpha$，则它是**平凡的**，此时每个关系都满足它。

用话说，$\alpha \to \beta$ 表示 $\beta$ 是 $\alpha$ 的函数（比较集合论中的**函数**）：**元组**的 $\alpha$ 值决定它的 $\beta$ 值。与码一样（[4.13.2](/4.13.2#sec-2.2.1)），依赖是否*成立*是关于应用的陈述，由设计者决定；实例只能说明某个依赖*不*成立。在当前数据中，起点位置决定基因，但 $\mathit{start\_pos} \to \mathit{gene\_id}$ 并不成立，因为不同染色体上的两个基因可以从同一位置开始。

我们用 $\alpha\beta$ 表示 $\alpha \cup \beta$，用 $A$ 表示 $\{A\}$，并用字母表开头的大写字母表示单个属性。码可以用依赖表示：$K$ 是 $R$ 的**超码**当且仅当 $K \to R$ 成立，若再没有真子集 $K' \subsetneq K$ 满足 $K' \to R$，则 $K$ 是**候选码**。（“当”的方向用到关系是集合这一事实：在 $R$ 上取值相同的两个元组就是同一个元组。）

**例 6.3.1** 在 §6.2 中表 $\mathit{results}$ 的**模式**上，下列依赖成立，并且成立的每个依赖都由它们推出（§6.3.2）：

$$
\begin{aligned}
&\mathit{sample\_id} \to \mathit{tissue}\ \mathit{treatment}\ \mathit{donor\_age}\ \mathit{collected\_on}\\
&\mathit{gene\_id} \to \mathit{symbol}\ \mathit{chrom}\ \mathit{start\_pos}\ \mathit{end\_pos}\ \mathit{strand}\\
&\mathit{symbol} \to \mathit{gene\_id}\\
&\mathit{sample\_id}\ \mathit{gene\_id} \to \mathit{tpm}\\
&\mathit{pathway\_id} \to \mathit{pathway\_name}\ \mathit{parent\_id}\\
&\mathit{pathway\_name} \to \mathit{pathway\_id}
\end{aligned}
$$

不存在右边为 $\mathit{pathway\_id}$、左边为样本或基因属性集的依赖：一个基因属于多条通路。

### 6.3.2. 逻辑蕴含与 Armstrong 公理

给定依赖集 $F$，另一些依赖随之成立：由 $\mathit{symbol} \to \mathit{gene\_id}$ 和 $\mathit{gene\_id} \to \mathit{chrom}$，同时满足这两者的每个关系也满足 $\mathit{symbol} \to \mathit{chrom}$。

**定义 6.3.2（函数依赖集的闭包）** $R$ 上的函数依赖集 $F$ *逻辑蕴含*函数依赖 $f$，记作 $F \models f$，是指 $R$ 上满足 $F$ 中所有依赖的每个关系也满足 $f$。$F$ 的闭包 $F^+$ 是被 $F$ 逻辑蕴含的所有函数依赖的集合。

$F^+$ 是有限但非常大的集合：例如它包含满足 $\beta \subseteq \alpha \subseteq R$ 的全部 $3^{\lvert R\rvert}$ 个平凡依赖 $\alpha \to \beta$（每个属性或在 $\beta$ 中，或在 $\alpha \setminus \beta$ 中，或在 $\alpha$ 之外）。下面的规则从语法上推导出它的成员。

**定义 6.3.3（Armstrong 公理）** 对属性集 $\alpha, \beta, \gamma \subseteq R$，**Armstrong 公理**是下列推理规则：

- **自反律**：若 $\beta \subseteq \alpha$，则 $\alpha \to \beta$；
- *增广律*：若 $\alpha \to \beta$，则 $\gamma\alpha \to \gamma\beta$；
- **传递律**：若 $\alpha \to \beta$ 且 $\beta \to \gamma$，则 $\alpha \to \gamma$。

若 $f$ 可由 $F$ 经有限次应用公理推出，记作 $F \vdash f$。

**定理 6.3.1（Armstrong 公理的可靠性）** 若 $F \vdash f$，则 $F \models f$。

**证明** 对推导的长度归纳，只需证明：每条公理由关系 $r$ 满足的依赖产生的依赖，也被 $r$ 满足。设 $t_1, t_2 \in r$。

- 自反律：若 $\beta \subseteq \alpha$ 且 $t_1[\alpha] = t_2[\alpha]$，则特别地 $t_1[\beta] = t_2[\beta]$。
- 增广律：设 $r$ 满足 $\alpha \to \beta$，且 $t_1[\gamma\alpha] = t_2[\gamma\alpha]$。则 $t_1[\gamma] = t_2[\gamma]$ 且 $t_1[\alpha] = t_2[\alpha]$；后者给出 $t_1[\beta] = t_2[\beta]$，故 $t_1[\gamma\beta] = t_2[\gamma\beta]$。
- 传递律：设 $r$ 满足 $\alpha \to \beta$ 和 $\beta \to \gamma$，且 $t_1[\alpha] = t_2[\alpha]$。则 $t_1[\beta] = t_2[\beta]$，从而 $t_1[\gamma] = t_2[\gamma]$。$\square$

另有三条规则可由公理导出，经常使用。

**命题 6.3.2** 下列规则可由 **Armstrong 公理**导出：

- 合并律：若 $\alpha \to \beta$ 且 $\alpha \to \gamma$，则 $\alpha \to \beta\gamma$；
- *分解律*：若 $\alpha \to \beta\gamma$，则 $\alpha \to \beta$ 且 $\alpha \to \gamma$；
- *伪传递律*：若 $\alpha \to \beta$ 且 $\gamma\beta \to \delta$，则 $\alpha\gamma \to \delta$。

**证明** 合并律：对 $\alpha \to \gamma$ 用 $\alpha$ 增广得 $\alpha \to \alpha\gamma$（因 $\alpha\alpha = \alpha$）；对 $\alpha \to \beta$ 用 $\gamma$ 增广得 $\alpha\gamma \to \beta\gamma$；由传递律得 $\alpha \to \beta\gamma$。分解律：由自反律 $\beta\gamma \to \beta$，再与 $\alpha \to \beta\gamma$ 用传递律得 $\alpha \to \beta$；对 $\gamma$ 同理。伪传递律：对 $\alpha \to \beta$ 用 $\gamma$ 增广得 $\alpha\gamma \to \gamma\beta$，再与 $\gamma\beta \to \delta$ 用传递律得 $\alpha\gamma \to \delta$。$\square$

由合并律和分解律，$\alpha \to \beta$ 可推导当且仅当对每个 $A \in \beta$，$\alpha \to A$ 可推导。这把关于依赖的问题化为关于单个属性的问题，并引出下面的集合。

**定义 6.3.4（属性闭包）** $\alpha \subseteq R$ 在 $F$ 下的**属性闭包**是集合 $\alpha^+ = \{\, A \in R \mid F \models \alpha \to A \,\}$，即由 $\alpha$ 函数确定的全部属性。

**定理 6.3.3（Armstrong 公理的完备性）** 若 $F \models f$，则 $F \vdash f$。因此 $F \models f$ 当且仅当 $F \vdash f$，$F^+$ 恰是可由 $F$ 推导的依赖的集合。

**证明** 设 $f = \alpha \to \beta$ 不能由 $F$ 推导；我们构造一个满足 $F$ 但不满足 $f$ 的关系。令 $\alpha^{\vdash} = \{\, A \in R \mid F \vdash \alpha \to A \,\}$。由自反律 $\alpha \subseteq \alpha^{\vdash}$，由合并律和分解律，$F \vdash \alpha \to \gamma$ 当且仅当 $\gamma \subseteq \alpha^{\vdash}$；所以 $\beta \not\subseteq \alpha^{\vdash}$。令 $r$ 由两个元组 $t_1, t_2$ 组成，它们在 $\alpha^{\vdash}$ 的属性上取值相同，在所有其他属性上取值不同（假定每个**域**至少有两个值）：

| | $\alpha^{\vdash}$ 中的属性 | 其他属性 |
|---|---|---|
| $t_1$ | $1\;1 \cdots 1$ | $1\;1 \cdots 1$ |
| $t_2$ | $1\;1 \cdots 1$ | $0\;0 \cdots 0$ |

关系 $r$ 满足 $F$ 中的每个 $\gamma \to \delta$。事实上，若 $t_1[\gamma] = t_2[\gamma]$，则 $\gamma \subseteq \alpha^{\vdash}$，故 $F \vdash \alpha \to \gamma$；与 $\gamma \to \delta$ 用传递律得 $F \vdash \alpha \to \delta$，所以 $\delta \subseteq \alpha^{\vdash}$，$t_1[\delta] = t_2[\delta]$。（若 $t_1[\gamma] \ne t_2[\gamma]$，依赖平凡地被满足。）但 $r$ 不满足 $\alpha \to \beta$：$t_1$ 与 $t_2$ 在 $\alpha \subseteq \alpha^{\vdash}$ 上取值相同，在 $\beta \setminus \alpha^{\vdash}$ 的某个属性上取值不同。因此 $F \not\models \alpha \to \beta$。$\square$

这个证明同时说明 $\alpha^{\vdash} = \alpha^+$，并包含本章的关键思想：恰好在一个闭属性集上取值相同的两元组关系满足 $F$。同样的构造可以证明闭包算法以及下面的无损连接检验的正确性。

## 6.4. 属性闭包的计算

### 6.4.1. 算法

计算 $F^+$ 的代价是属性个数的指数，但计算单个**属性闭包**很快。

**算法 6.4.1（属性闭包）** 输入：属性集 $\alpha$ 和函数依赖集 $F$。输出：$\alpha^+$。

1. $\mathit{result} \leftarrow \alpha$。
2. 重复直到 $\mathit{result}$ 不再变化：对 $F$ 中每个 $\beta \to \gamma$，若 $\beta \subseteq \mathit{result}$，则 $\mathit{result} \leftarrow \mathit{result} \cup \gamma$。
3. 返回 $\mathit{result}$。

**定理 6.4.1** 算法 6.4.1 终止并返回 $\alpha^+$。

**证明** 步骤 2 中每次使 $\mathit{result}$ 改变的遍历至少加入一个属性，所以至多有 $\lvert R\rvert$ 次这样的遍历。设 $Z$ 为返回的集合。

$Z \subseteq \alpha^+$：对步骤归纳，每一时刻都有 $F \models \alpha \to \mathit{result}$。开始时由自反律 $\alpha \to \alpha$ 成立。若 $\alpha \to \mathit{result}$ 成立，$\beta \subseteq \mathit{result}$ 且 $\beta \to \gamma \in F$，则由分解律 $\alpha \to \beta$，由传递律 $\alpha \to \gamma$，再由合并律 $\alpha \to \mathit{result} \cup \gamma$。

$\alpha^+ \subseteq Z$：算法停止时，每个满足 $\beta \subseteq Z$ 的 $\beta \to \gamma \in F$ 都有 $\gamma \subseteq Z$。因此恰好在 $Z$ 上取值相同的两元组**关系**（如定理 6.3.3 的证明中那样）满足 $F$：若 $t_1, t_2$ 在 $\beta$ 上取值相同，则 $\beta \subseteq Z$，所以 $\gamma \subseteq Z$，它们在 $\gamma$ 上取值也相同。对 $A \notin Z$，这个关系违反 $\alpha \to A$，因为 $\alpha \subseteq Z$。所以 $F \not\models \alpha \to A$，即 $A \notin \alpha^+$。$\square$

按上面的写法，算法需要 $O(\lvert R\rvert \cdot \lvert F\rvert)$ 次子集检验；若为每个依赖的左部缺失属性个数设置计数器，则运行时间与 $F$ 的总大小成线性（Beeri 与 Bernstein，1979）。

**例 6.4.1** 设 $R = (A, B, C, G, H, I)$，$F = \{A \to B,\ A \to C,\ CG \to H,\ CG \to I,\ B \to H\}$。计算 $(AG)^+$：从 $AG$ 开始；$A \to B$ 加入 $B$，$A \to C$ 加入 $C$，此时 $CG \subseteq \mathit{result}$，$CG \to H$、$CG \to I$ 加入 $H$ 和 $I$。所以 $(AG)^+ = ABCGHI = R$，$AG$ 是**超码**。由于 $A^+ = ABCH$ 和 $G^+ = G$ 都不是 $R$，它是**候选码**。

### 6.4.2. 属性闭包的用途

闭包算法回答关于依赖的基本问题：

| 问题 | 检验 |
|---|---|
| $\alpha \to \beta$ 是否成立，即是否在 $F^+$ 中？ | $\beta \subseteq \alpha^+$ |
| $\alpha$ 是否是 $R$ 的超码？ | $\alpha^+ = R$ |
| $\alpha$ 是否是候选码？ | $\alpha^+ = R$，且对每个 $A \in \alpha$ 有 $(\alpha \setminus \{A\})^+ \ne R$ |
| $F^+$ 是什么？ | 对每个 $\gamma \subseteq R$ 和每个 $S \subseteq \gamma^+$，输出 $\gamma \to S$（指数级，很少需要） |

Python 实现很短。它把依赖表示为一对 frozenset；`candidate_keys` 按规模递增尝试属性集，并跳过已找到的码的超集，最坏情况下是指数级的（一个**模式**可以有指数多个候选码），但对现实的模式很快：

```python
from itertools import combinations


def closure(attrs, fds):
    """Attribute closure of attrs under fds, a list of (lhs, rhs) frozensets."""
    result = set(attrs)
    changed = True
    while changed:
        changed = False
        for lhs, rhs in fds:
            if lhs <= result and not rhs <= result:
                result |= rhs
                changed = True
    return frozenset(result)


def candidate_keys(schema, fds):
    """All minimal superkeys, searched by increasing size."""
    keys = []
    for k in range(1, len(schema) + 1):
        for combo in combinations(sorted(schema), k):
            c = frozenset(combo)
            if any(key <= c for key in keys):
                continue
            if closure(c, fds) >= schema:
                keys.append(c)
    return keys


def fd(lhs, rhs):
    return frozenset(lhs.split()), frozenset(rhs.split())


def fmt(s):
    return "{" + ", ".join(sorted(s)) + "}"


R = frozenset("A B C G H I".split())
F = [fd("A", "B"), fd("A", "C"), fd("C G", "H"), fd("C G", "I"), fd("B", "H")]
print(fmt(closure({"A", "G"}, F)))
print([fmt(k) for k in candidate_keys(R, F)])
```

```text
{A, B, C, G, H, I}
['{A, G}']
```

## 6.5. 正则覆盖

依赖集往往本身含有冗余：被其他依赖蕴含的依赖，或可以去掉的**属性**。最小的等价集很有用，因为每次更新都必须对照依赖检查，而且 3NF 合成算法（§6.7.3）为每个依赖产生一个**关系**。

**定义 6.5.1（无关属性与正则覆盖）** 若 $F^+ = G^+$，则称依赖集 $F$ 与 $G$ *等价*。设 $\alpha \to \beta \in F$。若 $F$ 逻辑蕴含 $(F \setminus \{\alpha \to \beta\}) \cup \{(\alpha \setminus \{A\}) \to \beta\}$，则属性 $A \in \alpha$ 在 $\alpha$ 中是**无关的**；若 $(F \setminus \{\alpha \to \beta\}) \cup \{\alpha \to (\beta \setminus \{A\})\}$ 逻辑蕴含 $F$，则属性 $A \in \beta$ 在 $\beta$ 中是无关的。$F$ 的**正则覆盖** $F_{\mathrm{c}}$ 是与 $F$ 等价的依赖集，其中没有依赖含无关属性，且没有两个依赖的左部相同。

从左部去掉一个属性会使依赖变强，所以检验问的是更强的依赖是否仍被 $F$ 蕴含；从右部去掉一个属性会使依赖变弱，所以检验问的是 $F$ 是否仍被更弱的集合蕴含。两者都是闭包计算：

- $A \in \alpha$ 是无关的，当且仅当在 $F$ 下计算的 $\beta \subseteq (\alpha \setminus \{A\})^+$；
- $A \in \beta$ 是无关的，当且仅当在 $F' = (F \setminus \{\alpha \to \beta\}) \cup \{\alpha \to (\beta \setminus \{A\})\}$ 下计算的 $A \in \alpha^+$。

**算法 6.5.1（正则覆盖）** 重复直到 $F$ 不再变化：把左部相同的依赖 $\alpha \to \beta_1$ 和 $\alpha \to \beta_2$ 替换为 $\alpha \to \beta_1\beta_2$（合并律）；找出任一侧含无关属性的依赖并删除该属性；删除右部已变空的依赖。返回 $F$。

**例 6.5.1** 设 $R = (A, B, C)$，$F = \{A \to BC,\ B \to C,\ A \to B,\ AB \to C\}$。

1. 合并：$A \to BC$ 与 $A \to B$ 变为 $A \to BC$；此时 $F = \{A \to BC, B \to C, AB \to C\}$。
2. $A$ 在 $AB \to C$ 中是无关的：在 $F$ 下 $B^+ = BC \ni C$。该依赖变为 $B \to C$，已经存在；$F = \{A \to BC, B \to C\}$。
3. $C$ 在 $A \to BC$ 中是无关的：在 $\{A \to B, B \to C\}$ 下 $A^+ = ABC \ni C$。

所以 $F_{\mathrm{c}} = \{A \to B,\ B \to C\}$。**正则覆盖**不必唯一：对 $F = \{A \to BC, B \to AC, C \to AB\}$，$\{A \to B, B \to C, C \to A\}$ 与 $\{A \to C, C \to B, B \to A\}$ 都是正则覆盖（还有其他的）。

## 6.6. 分解

### 6.6.1. 无损分解

**定义 6.6.1（无损分解）** 关系模式 $R$ 的*分解*是满足 $R_1 \cup \cdots \cup R_n = R$ 的模式集合 $\{R_1, \dots, R_n\}$。若满足依赖集 $F$ 的每个合法关系 $r(R)$ 都等于它各个投影的自然连接，

$$
r = \Pi_{R_1}(r) \bowtie \Pi_{R_2}(r) \bowtie \cdots \bowtie \Pi_{R_n}(r),
$$
则称该分解相对于 $F$ 是**无损**的（无损连接分解）。不是无损的分解称为*有损*的。

包含关系 $r \subseteq \Pi_{R_1}(r) \bowtie \cdots \bowtie \Pi_{R_n}(r)$ 对每个分解都成立，因为每个 $t \in r$ 都与自己的**投影**相容。因此有损分解从不丢失**元组**；它产生*虚假*元组，从而丢失了“哪些组合实际存在”的信息。把 $\mathit{gene}$ 分解为 $(\mathit{gene\_id}, \mathit{chrom})$ 和 $(\mathit{chrom}, \mathit{symbol})$ 是有损的：把这两个投影在 $\mathit{chrom}$ 上连接回去，会把一条染色体上的每个基因与该染色体上的每个符号配对。


```sql
SELECT count(*) AS original FROM gene;

WITH a AS (SELECT DISTINCT gene_id, chrom FROM gene),
     b AS (SELECT DISTINCT chrom, symbol FROM gene)
SELECT count(*) AS rejoined FROM a JOIN b USING (chrom);

WITH a AS (SELECT DISTINCT gene_id, chrom FROM gene),
     b AS (SELECT DISTINCT chrom, symbol FROM gene)
SELECT a.gene_id, a.chrom, b.symbol FROM a JOIN b USING (chrom) WHERE a.chrom = 'chr17';
```

```text
+----------+
| original |
+----------+
| 8        |
+----------+
+----------+
| rejoined |
+----------+
| 14       |
+----------+
+-----------------+-------+--------+
|     gene_id     | chrom | symbol |
+-----------------+-------+--------+
| ENSG00000012048 | chr17 | BRCA1  |
| ENSG00000012048 | chr17 | TP53   |
| ENSG00000141510 | chr17 | BRCA1  |
| ENSG00000141510 | chr17 | TP53   |
+-----------------+-------+--------+
```

对于分解为两个**模式**的情形，无损性可以由依赖判定：

**定理 6.6.1（无损连接检验）** $R$ 分解为 $R_1$ 和 $R_2$ 相对于 $F$ 是无损的，当且仅当 $R_1 \cap R_2 \to R_1$ 或 $R_1 \cap R_2 \to R_2$ 在 $F^+$ 中，即当且仅当 $R_1 \cap R_2$ 是 $R_1$ 或 $R_2$ 的**超码**。

**证明** 令 $\gamma = R_1 \cap R_2$。

“若”：设 $\gamma \to R_2 \in F^+$（另一种情形对称），$r$ 满足 $F$。只需证明 $\Pi_{R_1}(r) \bowtie \Pi_{R_2}(r) \subseteq r$。**连接**的元组 $t$ 满足对某些 $t_1, t_2 \in r$ 有 $t[R_1] = t_1[R_1]$ 和 $t[R_2] = t_2[R_2]$，且 $t_1, t_2$ 在 $\gamma$ 上取值相同。由于 $r$ 满足 $\gamma \to R_2$，也有 $t_1[R_2] = t_2[R_2] = t[R_2]$。所以 $t_1$ 与 $t$ 在 $R_1 \cup R_2 = R$ 上取值相同，即 $t = t_1 \in r$。

“仅当”：设两个依赖都不在 $F^+$ 中，即 $R_1 \not\subseteq \gamma^+$ 且 $R_2 \not\subseteq \gamma^+$。令 $r = \{t_1, t_2\}$ 是恰好在 $\gamma^+$ 上取值相同的两元组**关系**；它满足 $F$（定理 6.4.1 的证明）。取 $A \in R_1 \setminus \gamma^+$ 和 $B \in R_2 \setminus \gamma^+$。由于 $\gamma \subseteq \gamma^+$，有 $A \notin R_2$ 且 $B \notin R_1$。投影 $t_1[R_1]$ 与 $t_2[R_2]$ 在 $\gamma$ 上取值相同，所以连接中含有元组 $t$，满足 $t[R_1] = t_1[R_1]$ 和 $t[R_2] = t_2[R_2]$。于是 $t[A] = t_1[A] \ne t_2[A]$，故 $t \ne t_2$；$t[B] = t_2[B] \ne t_1[B]$，故 $t \ne t_1$。连接中含有虚假元组 $t \notin r$，该分解是有损的。$\square$

在上面的例子中，$R_1 \cap R_2 = \{\mathit{chrom}\}$ 既不决定 $\mathit{gene\_id}$ 也不决定 $\mathit{symbol}$，所以分解是有损的。把 $\mathit{results}$ 分解为样本**属性**和其余部分是无损的，因为公共属性 $\mathit{sample\_id}$ 是样本部分的码。

分解为多于两个模式的情形，可以通过反复的二元拆分来检验（BC 范式算法正是这样产生它们的），或一般地用 Aho、Beeri 和 Ullman（1979）的*追赶*（chase）检验：它构造一个每个 $R_i$ 对应一行的表，并应用依赖，直到某一行不含未知值。

### 6.6.2. 保持依赖

**无损分解**保留了数据，却可能失去在单个关系内检查某个依赖的能力。

**定义 6.6.2（保持依赖）** $F$ 在 $R_i$ 上的*限制*是 $F^+$ 中只含 $R_i$ 的属性的全部依赖构成的集合 $F_i$。若 $(F_1 \cup \cdots \cup F_n)^+ = F^+$，则称分解 $\{R_1, \dots, R_n\}$ **保持依赖**。

若分解保持依赖，则每次更新只需在关系 $r_i$ 上单独检查各个 $F_i$ 就能验证。否则某些依赖只能在若干关系的连接上检查，代价很高；在 **SQL** 中这需要**断言**或**触发器**。计算 $F_i$ 需要 $F^+$，但有一个避开它的多项式检验：对 $F$ 中的每个 $\alpha \to \beta$，从 $\mathit{result} = \alpha$ 出发，对每个 $R_i$ 重复 $\mathit{result} \leftarrow \mathit{result} \cup ((\mathit{result} \cap R_i)^+ \cap R_i)$，直到不再变化。该依赖被保持当且仅当最后 $\beta \subseteq \mathit{result}$。

## 6.7. 范式

### 6.7.1. 第一范式

**定义 6.7.1（第一范式）** 若关系模式所有属性的域都是原子的，则它属于**第一范式**（1NF）。

**1NF** 是**关系模型**（[4.13.2](/4.13.2#sec-2.1.1)）的前提，而不是质量准则：用一列存放基因的通路列表，或用一组编号的列 `pathway_1`、`pathway_2`、`pathway_3`，都违背了它的精神，应当替换为单独的**关系**（$\mathit{gene\_pathway}$）。原子性取决于用法：只要没有查询把 Ensembl 标识符拆开，它就是原子的，而像 `liver-ctrl-01` 这样由程序解析其各部分的样本标识符则不是。现代系统用数组和 JSON 列有意放宽 1NF；它们适合总是整体读写的数据，不适合要被检索和连接的数据。

### 6.7.2. BC 范式

**定义 6.7.2（BC 范式）** 若对 $F^+$ 中每个满足 $\alpha, \beta \subseteq R$ 的函数依赖 $\alpha \to \beta$，下列条件至少成立一个，则称关系模式 $R$ 相对于 $F$ 属于 **BC 范式**（BCNF）：

- $\alpha \to \beta$ 是平凡的（$\beta \subseteq \alpha$）；
- $\alpha$ 是 $R$ 的**超码**。

若分解中的每个**模式**都属于 **BCNF**，则称该分解属于 BCNF。

在 BCNF 模式中，每个非平凡依赖都在说“码决定这个”，所以每个事实对每个码值存储一次，也就是每个**元组**恰好一次。$\mathit{results}$ 的模式不属于 BCNF：$\mathit{sample\_id} \to \mathit{tissue}$ 是非平凡的，而 $\mathit{sample\_id}$ 不是超码。运行示例的五个关系都属于 BCNF。

检验 $R$ 是否属于 BCNF，只需检查 $F$ 的依赖而不必检查整个 $F^+$：

**命题 6.7.1** 若 $R$ 上 $F$ 的每个依赖 $\alpha \to \beta$ 都是平凡的或 $\alpha$ 是超码，则 $R$ 相对于 $F$ 属于 BCNF。

**证明** 设 $\gamma \to \delta \in F^+$ 非平凡，并设 $\gamma$ 不是超码，即 $\gamma^+ \ne R$。由于 $\delta \not\subseteq \gamma$ 但 $\delta \subseteq \gamma^+$，算法 6.4.1 作用于 $\gamma$ 时会加入某个**属性**，用到的第一个依赖 $\alpha \to \beta \in F$ 满足 $\alpha \subseteq \gamma$ 且 $\beta \not\subseteq \gamma$；这个依赖是非平凡的。由假设 $\alpha$ 是超码，所以 $R = \alpha^+ \subseteq \gamma^+$，矛盾。$\square$

这个捷径对分解得到的模式不成立：那里的违反可能来自 $F^+$ 中不在 $F$ 里的依赖。对 $R_i \subseteq R$，正确的检验是：对每个 $\alpha \subseteq R_i$，检查（在 $F$ 下的）$\alpha^+$ 要么不含 $R_i \setminus \alpha$ 的任何属性，要么包含整个 $R_i$。

**算法 6.7.1（BCNF 分解）** 输入：模式 $R$ 和依赖 $F$。输出：$R$ 的分解为 BCNF 模式的**无损分解**。

1. $\mathit{result} \leftarrow \{R\}$。
2. 当 $\mathit{result}$ 中某个 $R_i$ 不属于 BCNF 时：在 $R_i$ 上选取非平凡的 $\alpha \to \beta \in F^+$，使 $\alpha$ 不是 $R_i$ 的超码且 $\alpha \cap \beta = \varnothing$；用两个模式 $R_i \setminus \beta$ 和 $\alpha \cup \beta$ 替换 $R_i$。
3. 返回 $\mathit{result}$。

（取 $\beta = \alpha^+ \cap R_i \setminus \alpha$ 可使每一步尽可能多地拆出。）

**定理 6.7.2** 算法 6.7.1 终止，并产生 $R$ 的无损分解，其中每个模式都属于 BCNF。

**证明** 终止性：每一步两个新模式都是 $R_i$ 的真子集。$R_i \setminus \beta \ne R_i$，因为 $\beta \ne \varnothing$（依赖非平凡且 $\alpha \cap \beta = \varnothing$）；$\alpha \cup \beta \ne R_i$，因为 $\alpha$ 不是 $R_i$ 的超码，而 $\alpha \to \alpha\beta$ 成立。模式不能无限缩小，并且每个至多有两个属性的模式都属于 BCNF（$\{A, B\}$ 上任何非平凡依赖是 $A \to B$ 或 $B \to A$，左部是超码），所以循环停止。

BCNF：循环只在每个模式都属于 BCNF 时停止。

无损性：由定理 6.6.1，每一步都是无损的二元分解，因为 $(R_i \setminus \beta) \cap (\alpha \cup \beta) = \alpha$ 且 $\alpha \to \alpha \cup \beta$ 成立。对无损分解的某个分量再做无损分解，结果仍是无损的：若 $r = \Pi_{R_1}(r) \bowtie \Pi_{R_2}(r)$，且 $R_1$ 被拆为 $R_{11}, R_{12}$，则 $\Pi_{R_1}(r)$ 满足 $F$ 在 $R_1$ 上的限制，所以 $\Pi_{R_1}(r) = \Pi_{R_{11}}(r) \bowtie \Pi_{R_{12}}(r)$，代入并由**自然连接**的结合律（[4.13.2](/4.13.2#sec-2.3.2)）得 $r = \Pi_{R_{11}}(r) \bowtie \Pi_{R_{12}}(r) \bowtie \Pi_{R_2}(r)$。对步数归纳，最终的分解是无损的。$\square$

分解不是唯一的：它取决于选择违反的顺序。

### 6.7.3. 第三范式

保持依赖时并不总能达到 BCNF。

**例 6.7.1** 某核心实验平台记录每个样本在每种检测中由哪位操作员处理。每位操作员恰好受训于一种检测，每个样本在每种检测中由一位操作员处理：在 $R = (\mathit{sample\_id}, \mathit{assay}, \mathit{operator})$ 上，

$$
F = \{\mathit{operator} \to \mathit{assay},\ \ \mathit{sample\_id}\ \mathit{assay} \to \mathit{operator}\}.
$$

**候选码**是 $\{\mathit{sample\_id}, \mathit{assay}\}$ 和 $\{\mathit{sample\_id}, \mathit{operator}\}$。$R$ 不属于 BCNF，因为 $\mathit{operator}$ 不是超码。BCNF 分解 $\{(\mathit{operator}, \mathit{assay}), (\mathit{sample\_id}, \mathit{operator})\}$ 是无损的，但没有哪个模式同时含 $\mathit{sample\_id}, \mathit{assay}, \mathit{operator}$，所以 $\mathit{sample\_id}\ \mathit{assay} \to \mathit{operator}$ 没有被保持：同一种检测的两位操作员可以同时被记录为处理同一个样本，而没有任何单个关系能察觉。$R$ 的每个 BCNF 分解都有这个缺陷，因为唯一含这三个属性的模式就是 $R$ 本身。

第三范式把 BCNF 放宽到恰好允许这样的模式。

**定义 6.7.3（第三范式）** 若对 $F^+$ 中每个满足 $\alpha, \beta \subseteq R$ 的 $\alpha \to \beta$，下列条件至少成立一个，则称关系模式 $R$ 相对于 $F$ 属于**第三范式**（3NF）：

- $\alpha \to \beta$ 是平凡的；
- $\alpha$ 是 $R$ 的超码；
- $\beta \setminus \alpha$ 中的每个属性都包含在 $R$ 的某个候选码中；这样的属性称为**主属性**。

每个 BCNF 模式都属于 **3NF**；例 6.7.1 的模式属于 3NF 但不属于 BCNF，因为 $\mathit{assay}$ 是主属性。第三个条件是**保持依赖**的代价：允许一定的冗余（操作员的检测种类对该操作员处理的每个样本都重复），但只出现在**主属性**中。

**算法 6.7.2（3NF 合成）** 输入：模式 $R$ 和依赖 $F$。输出：分解为 3NF 模式的无损、保持依赖的分解。

1. 计算 $F$ 的**正则覆盖** $F_{\mathrm{c}}$。
2. 对 $F_{\mathrm{c}}$ 中每个 $\alpha \to \beta$，把模式 $\alpha\beta$ 加入结果。
3. 若结果中没有模式包含 $R$ 的候选码，则加入一个由某个候选码构成的模式。
4. 删除被结果中另一个模式包含的每个模式。

**定理 6.7.3** 算法 6.7.2 产生的分解是保持依赖的、无损的，且其中每个模式都属于 3NF。

**证明**（概要）保持依赖：$F_{\mathrm{c}}$ 的每个依赖都落在结果的某个模式内（步骤 4 只在更大的模式包含它时才删除一个模式），且 $F_{\mathrm{c}}$ 与 $F$ 等价。无损性：设 $K$ 是某个模式 $R_j$ 中包含的候选码。用算法 6.4.1 计算 $K^+ = R$ 要应用 $F_{\mathrm{c}}$ 的一个依赖序列，其中每个依赖都包含在结果的某个模式内；沿此序列归纳，由追赶检验知，把这些模式上的**投影**与 $R_j$ 连接不产生虚假元组。3NF：考虑由 $\alpha \to \beta \in F_{\mathrm{c}}$ 产生的模式 $\alpha\beta$。$\alpha$ 是 $\alpha\beta$ 的候选码，因为由正则覆盖的极小性，$\alpha$ 的任何真子集都不决定 $\beta$。若 $\alpha\beta$ 上成立非平凡的 $\gamma \to B$，其中 $\gamma$ 不是超码且 $B$ 不是主属性，则 $B \in \beta$，可以证明 $B$ 在 $\alpha \to \beta$ 中是无关的，与正则覆盖矛盾；只含候选码的模式没有左部不是超码的非平凡依赖。完整的论证见 Silberschatz 等人的第 7 章。$\square$

对例 6.7.1，$F$ 本身就是正则覆盖；步骤 2 产生 $(\mathit{operator}, \mathit{assay})$ 和 $(\mathit{sample\_id}, \mathit{assay}, \mathit{operator})$，步骤 4 因前者被后者包含而删除它。结果就是 $R$ 本身，它属于 3NF。

两种范式之间的选择是一项设计决定：

| | BCNF | 3NF |
|---|---|---|
| 由函数依赖引起的冗余 | 无 | 主属性中可能有 |
| 无损分解 | 总能达到 | 总能达到 |
| 保持依赖 | 不一定能达到 | 总能达到 |
| 算法 | 分解（算法 6.7.1） | 由正则覆盖合成（算法 6.7.2） |

实践中以 BCNF 为目标。当它会丢失某个依赖时（如例 6.7.1），设计者要么接受 3NF 模式，要么使用 BCNF 分解并另行强制被丢失的依赖（这里是在冗余存放检测种类的表上加 `UNIQUE (sample_id, assay)` 约束，或用**触发器**）。

### 6.7.4. 第二范式

**定义 6.7.4（第二范式）** 若关系模式属于 1NF，且没有非主属性*部分依赖*于候选码（即由候选码的真子集决定），则它属于**第二范式**（2NF）。

**2NF** 主要有历史意义；它介于 1NF 与 3NF 之间，并被 3NF 蕴含。表 $\mathit{results}$ 连 2NF 都不满足，因为 $\mathit{tissue}$ 依赖于 $\mathit{sample\_id}$，它是候选码 $\{\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id}\}$ 的真子集。属于 2NF 但不属于 3NF 的模式含有*传递*依赖：非主属性经由另一个非主属性依赖于码，例如若染色体长度与每个基因一起存储，就有 $\mathit{gene\_id} \to \mathit{chrom} \to \mathit{chrom\_length}$。包含关系为 BCNF $\subsetneq$ 3NF $\subsetneq$ 2NF $\subsetneq$ 1NF。

### 6.7.5. 多值依赖与第四范式

有些冗余根本不是由函数依赖引起的。在 $\mathit{results}$ 中，基因的通路不依赖于样本：测得 TP53 的每个样本都与 TP53 的两条通路组合。去掉所有违反函数依赖的情形之后剩下的 $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$ 上的关系没有非平凡的**函数依赖**，所以属于 BCNF，却对每个样本都存储一次“TP53 属于 PW2”。

**定义 6.7.5（多值依赖）** 设 $\alpha, \beta \subseteq R$，$\gamma = R \setminus \alpha\beta$。若在每个合法关系 $r(R)$ 中，对所有满足 $t_1[\alpha] = t_2[\alpha]$ 的元组 $t_1, t_2 \in r$，都存在元组 $t_3 \in r$ 使得 $t_3[\alpha] = t_1[\alpha]$、$t_3[\beta] = t_1[\beta]$ 且 $t_3[\gamma] = t_2[\gamma]$，则称**多值依赖** $\alpha \twoheadrightarrow \beta$ 在 $R$ 上成立。

于是 $\mathit{gene\_id} \twoheadrightarrow \mathit{pathway\_id}$ 表示：对给定的基因，它的通路集合与它的样本集合是独立的：每种组合都出现。每个函数依赖 $\alpha \to \beta$ 也是**多值依赖** $\alpha \twoheadrightarrow \beta$。定理 6.6.1 的类似结论是 Fagin 定理（1977）：$R$ 分解为 $\alpha\beta$ 和 $\alpha\gamma$ 是无损的当且仅当 $\alpha \twoheadrightarrow \beta$ 成立。

**定义 6.7.6（第四范式）** 若对函数依赖和多值依赖的集合 $D$，$R$ 上 $D^+$ 中的每个多值依赖 $\alpha \twoheadrightarrow \beta$ 要么是平凡的（$\beta \subseteq \alpha$ 或 $\alpha\beta = R$），要么 $\alpha$ 是 $R$ 的超码，则称关系模式 $R$ 相对于 $D$ 属于**第四范式**（4NF）。

**4NF** 蕴含 BCNF。分解算法与 BCNF 相同，只是用多值依赖代替函数依赖。4NF 之上还有其他范式（基于**连接**依赖的投影–连接范式），但实践中很少需要。

## 6.8. 一个完整的规范化过程

现在用例 6.3.1 的依赖 $F$ 来规范化 §6.2 的表 $\mathit{results}$。

### 6.8.1. 候选码

没有依赖的右部含 $\mathit{sample\_id}$，基因或通路的**属性**也都不决定它，所以每个码都含 $\mathit{sample\_id}$；同样，每个码都含一个基因标识符（$\mathit{gene\_id}$ 或 $\mathit{symbol}$）和一个通路标识符（$\mathit{pathway\_id}$ 或 $\mathit{pathway\_name}$）。闭包计算证实 $\{\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id}\}^+$ 就是整个 $\mathit{results}$，基因标识符与通路标识符各有两种选择，共得到四个**候选码**。

### 6.8.2. BCNF 分解

$F$ 的每个依赖都违反 $\mathit{results}$ 上的 **BCNF**。下面是算法 6.7.1 的一个小实现，用 §6.4.2 的 `closure` 函数找出违反，并记录每次拆分：

```python
def bcnf_violation(schema, fds):
    """A dependency X -> Y on schema that violates BCNF, or None. Every subset X
    of the schema is tried, so violations by dependencies in F+ are found too."""
    for k in range(1, len(schema)):
        for combo in combinations(sorted(schema), k):
            x = frozenset(combo)
            xplus = closure(x, fds) & schema
            if xplus != x and xplus != schema:
                return x, xplus - x
    return None


def bcnf_decompose(schema, fds):
    result, todo = [], [frozenset(schema)]
    while todo:
        r = todo.pop()
        v = bcnf_violation(r, fds)
        if v is None:
            result.append(r)
            continue
        x, y = v
        print(f"split {fmt(r)} on {fmt(x)} -> {fmt(y)}")
        todo += [r - y, x | y]
    return result


results = frozenset("""sample_id tissue treatment donor_age collected_on
    gene_id symbol chrom start_pos end_pos strand tpm
    pathway_id pathway_name parent_id""".split())
F = [
    fd("sample_id", "tissue treatment donor_age collected_on"),
    fd("gene_id", "symbol chrom start_pos end_pos strand"),
    fd("symbol", "gene_id"),
    fd("sample_id gene_id", "tpm"),
    fd("pathway_id", "pathway_name parent_id"),
    fd("pathway_name", "pathway_id"),
]
print("keys:", [fmt(k) for k in candidate_keys(results, F)])
for r in bcnf_decompose(results, F):
    print("BCNF:", fmt(r))
```

```text
keys: ['{gene_id, pathway_id, sample_id}', '{gene_id, pathway_name, sample_id}', '{pathway_id, sample_id, symbol}', '{pathway_name, sample_id, symbol}']
split {chrom, collected_on, donor_age, end_pos, gene_id, parent_id, pathway_id, pathway_name, sample_id, start_pos, strand, symbol, tissue, tpm, treatment} on {gene_id} -> {chrom, end_pos, start_pos, strand, symbol}
split {collected_on, donor_age, gene_id, parent_id, pathway_id, pathway_name, sample_id, tissue, tpm, treatment} on {pathway_id} -> {parent_id, pathway_name}
split {collected_on, donor_age, gene_id, pathway_id, sample_id, tissue, tpm, treatment} on {sample_id} -> {collected_on, donor_age, tissue, treatment}
split {gene_id, pathway_id, sample_id, tpm} on {gene_id, sample_id} -> {tpm}
BCNF: {chrom, end_pos, gene_id, start_pos, strand, symbol}
BCNF: {parent_id, pathway_id, pathway_name}
BCNF: {collected_on, donor_age, sample_id, tissue, treatment}
BCNF: {gene_id, sample_id, tpm}
BCNF: {gene_id, pathway_id, sample_id}
```

（`bcnf_violation` 中的子集搜索是指数级的，只用于小例子。）前四个**模式**是运行示例的 $\mathit{gene}$、$\mathit{pathway}$、$\mathit{sample}$ 和 $\mathit{measurement}$，只是 $\mathit{name}$ 被重命名。由定理 6.7.2，该分解是无损的，在这里也**保持依赖**：$F$ 的每个依赖都落在某个模式内（$\mathit{symbol} \to \mathit{gene\_id}$ 在 $\mathit{gene}$ 内，其中 $\mathit{symbol}$ 是第二个候选码，被声明为 `UNIQUE`）。

### 6.8.3. 第四范式

最后一个模式 $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$ 属于 BCNF 但不属于 **4NF**，原因是 $\mathit{gene\_id} \twoheadrightarrow \mathit{pathway\_id}$（§6.7.5）。由 Fagin 定理，它可以无损地分解为 $(\mathit{gene\_id}, \mathit{pathway\_id})$（即 $\mathit{gene\_pathway}$）和 $(\mathit{gene\_id}, \mathit{sample\_id})$，后者已包含在 $\mathit{measurement}$ 中而被舍去。结果恰好是 [4.13.3](/4.13.3#sec-3.2.3) 的模式，现在还证明了它没有 §6.2 的任何异常。它还解决了电子表格中依赖没有显示出来的一个缺陷：没有通路的基因（如 ACTB）在 $\mathit{results}$ 中只能在码属性 $\mathit{pathway\_id}$ 上存放**空值**，而规范化后的模式只是在 $\mathit{gene\_pathway}$ 中没有它的行。

**3NF** 合成算法在这里给出同样的结果：除了合并左部为 $\mathit{gene\_id}$ 的两个依赖之外，$F$ 已经是**正则覆盖**；对应于 $\mathit{symbol} \to \mathit{gene\_id}$ 和 $\mathit{pathway\_name} \to \mathit{pathway\_id}$ 的模式分别被 $\mathit{gene\_id}$ 和 $\mathit{pathway\_id}$ 的模式包含而被删除，并加入候选码 $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$ 的模式。

## 6.9. 规范化的实践

**规范化**与 E-R 设计从两个方向逼近同一个目标，细致的 E-R 设计（每类对象一个**实体集**，用**联系集**表示关联，多值属性作为单独的关系）通常直接产生 BCNF 模式。E-R 设计忽略的依赖会表现为违反，例如附加在实体集 *gene* 上的属性 $\mathit{chrom\_length}$，它实际上描述的是一个染色体实体集。

规范化的**模式**需要**连接**来重新组装数据，设计有时会有意*反规范化*：在报表中保留基因符号的冗余副本，或为每个基因和组织预先计算汇总，可避免常用查询中的连接。代价是必须保持冗余副本的一致，办法有**触发器**、物化视图（[4.13.4](/4.13.4#sec-4.6)）或定期重算；物化视图通常是最干净的方案。分析型数据库（数据仓库）通常采用星型模式（star schema）：一张大的规范化事实表（fact table）存放测量值，周围是有意反规范化的维表（dimension table），如带全部属性的样本、带注释的基因，因为它们读得远多于写。还有一些看似违反的情形其实不是：把供体在*采集时*的年龄与样本一起存放并不冗余，只要没有记录出生日期，因为那时没有别的东西能决定它。

## 小结

- **完整性约束**（**域**、码、**实体完整性**、参照完整性、`CHECK`）在模式中声明，由 DBMS 在每次修改时强制执行。参照动作（`NO ACTION`、`RESTRICT`、`CASCADE`、`SET NULL`、`SET DEFAULT`）决定被引用行消失时引用如何处理；检查可以推迟到提交时。
- 断言是标准但未被实现；触发器（事件–条件–动作，`BEFORE`/`AFTER`/`INSTEAD OF`，逐行或逐语句）用于审计日志、派生数据和无法声明的约束。
- 冗余引起更新、插入和删除异常。函数依赖 $\alpha \to \beta$ 表示 $\alpha$ 决定 $\beta$；码是决定一切的集合。
- Armstrong 公理（自反律、增广律、传递律）对 $F^+$ 是可靠且完备的；属性闭包 $\alpha^+$ 由简单的不动点算法计算，可判定 $\alpha \to \beta \in F^+$（$\beta \subseteq \alpha^+$）和超码（$\alpha^+ = R$）。正则覆盖去掉无关属性。
- 二元分解是无损的当且仅当公共属性是某一方的超码；若 $F$ 的各个限制蕴含 $F$，则分解保持依赖。
- BCNF：每个非平凡依赖的左部都是超码；分解算法是无损的，但可能丢失依赖。3NF 还允许右部是主属性；合成算法是无损且保持依赖的。4NF 把 BCNF 推广到多值依赖。
- 把含样本、基因和通路属性的测量电子表格规范化，恰好得到运行示例的五个关系。
