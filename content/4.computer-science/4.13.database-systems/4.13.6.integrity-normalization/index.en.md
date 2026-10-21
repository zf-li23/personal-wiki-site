---
title: Integrity Constraints and Normalization
description: "How a database keeps its data correct and how to recognize a good relational schema: domain, entity and referential integrity with ON DELETE actions and deferred checking, assertions and triggers; update anomalies; functional dependencies, Armstrong's axioms with proofs of soundness and completeness, attribute closure, canonical covers; lossless decomposition and dependency preservation; first, second and third normal form and Boyce–Codd normal form with the decomposition and synthesis algorithms; multivalued dependencies and fourth normal form; a worked normalization of a laboratory spreadsheet into the running example."
---

A schema is good if the database can record every legal state of the world, and only legal states, without storing any fact twice. This chapter treats both halves of that statement. The first part shows how integrity constraints and triggers let the DBMS itself reject illegal data, instead of trusting every program that writes to the database. The second part develops the theory of functional dependencies, which makes "storing a fact twice" precise and leads to the normal forms, conditions on a schema under which this redundancy cannot occur, and to algorithms that decompose a bad schema into good ones without losing information. The E-R design of [4.13.5](/4.13.5) usually produces schemas that are already normalized; normalization is the check that it did, and the method of choice when the starting point is an existing table, such as a spreadsheet. The examples use the running example of [4.13.3](/4.13.3#sec-3.2.3); the logic and set theory are those of [1.1](/1.1) and [1.2](/1.2).

## 6.1. Integrity Constraints

### 6.1.1. Domain Constraints and Entity Integrity

**Definition 6.1.1 (Integrity Constraint)** An **integrity constraint** is a condition that every legal instance of a database must satisfy. The DBMS checks the declared constraints whenever the database is modified and rejects a modification that would violate one.

The constraints that SQL can declare in `CREATE TABLE` were listed in [4.13.3](/4.13.3#sec-3.2.2). They fall into a few kinds:

- *Domain constraints* restrict the values of a column: its data type, `NOT NULL`, and `CHECK` conditions on the column such as `CHECK (tpm >= 0)`. PostgreSQL can name a constrained type for reuse, `CREATE DOMAIN tpm_value AS numeric(10, 2) CHECK (VALUE >= 0)`.
- *Key constraints*: `PRIMARY KEY` and `UNIQUE`.
- **Referential integrity**: `FOREIGN KEY ... REFERENCES` (§6.1.2).
- *Tuple constraints*: `CHECK` conditions involving several columns of a row, such as `CHECK (start_pos <= end_pos)`.

**Definition 6.1.2 (Entity Integrity)** The **entity integrity** rule requires that no attribute of the primary key of a relation be null.

Since the primary key is how a tuple is identified and referenced, a tuple with a null key could not be referenced reliably; SQL enforces the rule by making `PRIMARY KEY` imply `NOT NULL` (with the SQLite exception noted in [4.13.3](/4.13.3#sec-3.2.2)). A `CHECK` condition is satisfied when it evaluates to true *or unknown* ([4.13.2](/4.13.2#sec-2.6)), so `CHECK (donor_age BETWEEN 0 AND 120)` admits a null age; if the value must be present, `NOT NULL` has to be added. The standard allows subqueries in `CHECK`, but no major system implements them, because a condition on other rows would have to be rechecked whenever those rows change.

### 6.1.2. Referential Integrity and Referential Actions

A foreign key ([4.13.2](/4.13.2#sec-2.2.2)) can be violated from two sides: by inserting or updating a referencing row whose value does not exist in the referenced table, and by deleting or updating a referenced row that is still referenced. The first is always rejected. For the second, the foreign-key declaration chooses a *referential action*:

| Action (`ON DELETE ...` / `ON UPDATE ...`) | Effect when a referenced row is deleted or its key changed |
|---|---|
| `NO ACTION` (the default) | reject the change if references remain when the constraint is checked (at the end of the statement, or of the transaction if deferred) |
| `RESTRICT` | reject immediately, even if the statement would remove the references itself |
| `CASCADE` | delete the referencing rows as well (or change their foreign key to the new value) |
| `SET NULL` | set the foreign key of the referencing rows to null |
| `SET DEFAULT` | set it to the column's default value |

`CASCADE` is appropriate for dependent data, such as the aliquots of a sample, which is how the weak entity set of [4.13.5](/4.13.5#sec-5.5) was declared; it would be dangerous for measurements, which are results that should not disappear silently because a sample row was deleted by mistake. In the following SQLite session, deleting a sample removes its aliquots, but deleting a sample that still has measurements is rejected by the default action:

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

A foreign key is normally checked at the end of each statement. Declaring it `DEFERRABLE INITIALLY DEFERRED` (PostgreSQL, SQLite; in PostgreSQL also switchable per transaction with `SET CONSTRAINTS ... DEFERRED`) postpones the check to the commit of the transaction. This is needed for cyclic references, for example two tables that reference each other, and it would have allowed the pathways of [4.13.3](/4.13.3#sec-3.2.3) to be inserted in any order within one transaction. MySQL's InnoDB checks foreign keys row by row and does not support deferral.

### 6.1.3. Assertions

**Definition 6.1.3 (Assertion)** An **assertion** is a named condition on the database as a whole, `CREATE ASSERTION name CHECK (condition)`, which the database must always satisfy.

Every constraint can be expressed as an assertion. For example, "every sample has at least one measurement" is

```sql
CREATE ASSERTION every_sample_measured CHECK (
    NOT EXISTS (SELECT * FROM sample AS s
                WHERE NOT EXISTS (SELECT * FROM measurement AS m
                                  WHERE m.sample_id = s.sample_id)));
```

Assertions have been part of the SQL standard since SQL-92, but for three decades no widely used system implemented them, because checking an arbitrary condition efficiently after every modification is hard: a naive implementation would re-evaluate the whole query on every insert, update and delete. Oracle AI Database 26ai (2026) is the first major system to support `CREATE ASSERTION`, with restrictions on the allowed queries; PostgreSQL, MySQL, SQLite and SQL Server reject the statement. In those systems such conditions are enforced by triggers, by application code, or by restructuring the schema so that a simpler constraint suffices.

### 6.1.4. Triggers

**Definition 6.1.4 (Trigger)** A **trigger** is a statement that the DBMS executes automatically as a side effect of a modification of the database. It is specified by an *event* (an `INSERT`, `UPDATE` or `DELETE` on a table, possibly limited to some columns), a *condition* under which it fires, and an *action*; this is the event–condition–action model.

A trigger fires `BEFORE` or `AFTER` the event, `FOR EACH ROW` (once per affected row, with access to the old and new row as `OLD` and `NEW`) or `FOR EACH STATEMENT`; an `INSTEAD OF` trigger on a view replaces the modification of the view by its action. A common use is an audit log of changes to the measurements. In SQLite, the action is written inline:

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

In PostgreSQL the action is a function written in PL/pgSQL (or another procedural language) and the trigger refers to it; the timestamp would be a `timestamptz DEFAULT now()` column:

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

An `INSTEAD OF` trigger makes the read-only view `expression` of [4.13.4](/4.13.4#sec-4.6) updatable for the one change that has an obvious meaning, setting the value of a gene in a sample:

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

Triggers are powerful and easy to misuse. They are appropriate for audit logs, for maintaining derived data such as summary tables, and for enforcing constraints that cannot be declared. They are a poor substitute for declared constraints (a `CHECK` or `FOREIGN KEY` is shorter, cannot be bypassed, is visible in the catalog and can be used by the optimizer) and for application logic: actions that happen invisibly, possibly cascading through other triggers, make a system hard to understand. Triggers can also be bypassed: PostgreSQL does not fire ordinary triggers when it applies changes received by logical replication, and bulk loads are often run with triggers disabled, so constraints enforced only by triggers must be checked separately after such operations.

## 6.2. Redundancy and Anomalies

Suppose the laboratory had kept all its data in one large table, as a spreadsheet would: one row per measurement, with the sample's and the gene's properties and the gene's pathway repeated in every row. The following query builds this table from the running example (a gene in two pathways gives two rows; a gene in none, one row with null pathway columns):

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

The fact "S01 is a liver sample" is stored 10 times, the position of TP53 twelve times. Such redundancy causes three kinds of *anomalies*:

- *Update anomaly*: correcting the tissue of S01 requires changing ten rows; changing only some of them leaves the database inconsistent, with two different tissues for the same sample.
- *Insertion anomaly*: a new sample cannot be recorded before its first measurement, nor a new pathway before a gene is annotated to it, unless the other columns are filled with nulls, which then must also be allowed in what would naturally be the key.
- *Deletion anomaly*: deleting the measurements of a gene that was measured only once also deletes the only record of that gene's position and pathways.

The remedy is to *decompose* the table into several smaller ones, each about one kind of thing, as the running example does. Replacing a schema by a decomposition that eliminates such redundancy, guided by the dependencies among the attributes, is called *normalization*. The rest of this chapter answers the questions this raises: which decompositions are correct, which are good, and how to find them systematically.

## 6.3. Functional Dependencies

### 6.3.1. Definition

The redundancy above arises because some attributes determine others: the sample identifier determines the tissue, so every row with S01 must repeat "liver". Functional dependencies state such facts.

**Definition 6.3.1 (Functional Dependency)** Let $R$ be a relation schema and $\alpha, \beta \subseteq R$. A relation $r(R)$ *satisfies* the **functional dependency** $\alpha \to \beta$ if for all tuples $t_1, t_2 \in r$,

$$
t_1[\alpha] = t_2[\alpha] \implies t_1[\beta] = t_2[\beta].
$$
The functional dependency *holds* on $R$ if every legal relation on $R$ satisfies it. It is **trivial** if $\beta \subseteq \alpha$, in which case every relation satisfies it.

In words, $\alpha \to \beta$ says that $\beta$ is a function of $\alpha$ (compare a **function** in set theory): the $\alpha$-value of a tuple determines its $\beta$-value. As with keys ([4.13.2](/4.13.2#sec-2.2.1)), whether a dependency *holds* is a statement about the application, decided by the designer; an instance can only show that a dependency does *not* hold. In the current data the start position determines the gene, but $\mathit{start\_pos} \to \mathit{gene\_id}$ does not hold, since two genes on different chromosomes may start at the same position.

We write $\alpha\beta$ for $\alpha \cup \beta$ and $A$ for $\{A\}$, and use upper-case letters near the beginning of the alphabet for single attributes. Keys can be expressed with dependencies: $K$ is a superkey of $R$ if and only if $K \to R$ holds, and a candidate key if, in addition, no proper subset $K' \subsetneq K$ has $K' \to R$. (The "if" direction uses that a relation is a set: two tuples that agree on $R$ are the same tuple.)

**Example 6.3.1** On the schema of the table $\mathit{results}$ of §6.2, the following dependencies hold, and every dependency that holds follows from them (§6.3.2):

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

There is no dependency with $\mathit{pathway\_id}$ on the right of a sample or gene attribute set: a gene belongs to several pathways.

### 6.3.2. Logical Implication and Armstrong's Axioms

Given a set $F$ of dependencies, others follow: from $\mathit{symbol} \to \mathit{gene\_id}$ and $\mathit{gene\_id} \to \mathit{chrom}$, every relation that satisfies both also satisfies $\mathit{symbol} \to \mathit{chrom}$.

**Definition 6.3.2 (Closure of a Set of Functional Dependencies)** A set $F$ of functional dependencies on $R$ *logically implies* a functional dependency $f$, written $F \models f$, if every relation on $R$ that satisfies all dependencies of $F$ also satisfies $f$. The closure $F^+$ of $F$ is the set of all functional dependencies logically implied by $F$.

$F^+$ is a finite but very large set: it contains, for instance, all $3^{\lvert R\rvert}$ trivial dependencies $\alpha \to \beta$ with $\beta \subseteq \alpha \subseteq R$ (each attribute lies in $\beta$, in $\alpha \setminus \beta$ or outside $\alpha$). The following rules derive its members syntactically.

**Definition 6.3.3 (Armstrong's Axioms)** For attribute sets $\alpha, \beta, \gamma \subseteq R$, **Armstrong's axioms** are the inference rules

- **reflexivity**: if $\beta \subseteq \alpha$, then $\alpha \to \beta$;
- *augmentation*: if $\alpha \to \beta$, then $\gamma\alpha \to \gamma\beta$;
- **transitivity**: if $\alpha \to \beta$ and $\beta \to \gamma$, then $\alpha \to \gamma$.

We write $F \vdash f$ if $f$ can be derived from $F$ by finitely many applications of the axioms.

**Theorem 6.3.1 (Soundness of Armstrong's Axioms)** If $F \vdash f$, then $F \models f$.

**Proof** By induction on the length of the derivation it suffices to show that each axiom produces, from dependencies satisfied by a relation $r$, a dependency also satisfied by $r$. Let $t_1, t_2 \in r$.

- Reflexivity: if $\beta \subseteq \alpha$ and $t_1[\alpha] = t_2[\alpha]$, then in particular $t_1[\beta] = t_2[\beta]$.
- Augmentation: suppose $r$ satisfies $\alpha \to \beta$ and $t_1[\gamma\alpha] = t_2[\gamma\alpha]$. Then $t_1[\gamma] = t_2[\gamma]$ and $t_1[\alpha] = t_2[\alpha]$; the latter gives $t_1[\beta] = t_2[\beta]$, so $t_1[\gamma\beta] = t_2[\gamma\beta]$.
- Transitivity: suppose $r$ satisfies $\alpha \to \beta$ and $\beta \to \gamma$, and $t_1[\alpha] = t_2[\alpha]$. Then $t_1[\beta] = t_2[\beta]$, hence $t_1[\gamma] = t_2[\gamma]$. $\square$

Three further rules are derived from the axioms and are used constantly.

**Proposition 6.3.2** The following rules are derivable from Armstrong's axioms:

- **union**: if $\alpha \to \beta$ and $\alpha \to \gamma$, then $\alpha \to \beta\gamma$;
- *decomposition*: if $\alpha \to \beta\gamma$, then $\alpha \to \beta$ and $\alpha \to \gamma$;
- *pseudotransitivity*: if $\alpha \to \beta$ and $\gamma\beta \to \delta$, then $\alpha\gamma \to \delta$.

**Proof** Union: augmenting $\alpha \to \gamma$ by $\alpha$ gives $\alpha \to \alpha\gamma$ (as $\alpha\alpha = \alpha$); augmenting $\alpha \to \beta$ by $\gamma$ gives $\alpha\gamma \to \beta\gamma$; transitivity yields $\alpha \to \beta\gamma$. Decomposition: $\beta\gamma \to \beta$ by reflexivity, and transitivity with $\alpha \to \beta\gamma$ gives $\alpha \to \beta$; likewise for $\gamma$. Pseudotransitivity: augmenting $\alpha \to \beta$ by $\gamma$ gives $\alpha\gamma \to \gamma\beta$, and transitivity with $\gamma\beta \to \delta$ gives $\alpha\gamma \to \delta$. $\square$

By union and decomposition, $\alpha \to \beta$ is derivable if and only if $\alpha \to A$ is derivable for every $A \in \beta$. This reduces questions about dependencies to questions about single attributes, and motivates the following set.

**Definition 6.3.4 (Attribute Closure)** The **attribute closure** of $\alpha \subseteq R$ under $F$ is the set $\alpha^+ = \{\, A \in R \mid F \models \alpha \to A \,\}$ of all attributes functionally determined by $\alpha$.

**Theorem 6.3.3 (Completeness of Armstrong's Axioms)** If $F \models f$, then $F \vdash f$. Hence $F \models f$ if and only if $F \vdash f$, and $F^+$ is exactly the set of dependencies derivable from $F$.

**Proof** Suppose $f = \alpha \to \beta$ is not derivable from $F$; we construct a relation that satisfies $F$ but not $f$. Let $\alpha^{\vdash} = \{\, A \in R \mid F \vdash \alpha \to A \,\}$. By reflexivity $\alpha \subseteq \alpha^{\vdash}$, and by union and decomposition, $F \vdash \alpha \to \gamma$ if and only if $\gamma \subseteq \alpha^{\vdash}$; so $\beta \not\subseteq \alpha^{\vdash}$. Let $r$ consist of two tuples $t_1, t_2$ that agree on the attributes of $\alpha^{\vdash}$ and differ on every other attribute (every domain is assumed to have at least two values):

| | attributes in $\alpha^{\vdash}$ | other attributes |
|---|---|---|
| $t_1$ | $1\;1 \cdots 1$ | $1\;1 \cdots 1$ |
| $t_2$ | $1\;1 \cdots 1$ | $0\;0 \cdots 0$ |

The relation $r$ satisfies every $\gamma \to \delta$ in $F$. Indeed, if $t_1[\gamma] = t_2[\gamma]$ then $\gamma \subseteq \alpha^{\vdash}$, so $F \vdash \alpha \to \gamma$; transitivity with $\gamma \to \delta$ gives $F \vdash \alpha \to \delta$, so $\delta \subseteq \alpha^{\vdash}$ and $t_1[\delta] = t_2[\delta]$. (If $t_1[\gamma] \ne t_2[\gamma]$, the dependency is satisfied trivially.) But $r$ does not satisfy $\alpha \to \beta$: $t_1$ and $t_2$ agree on $\alpha \subseteq \alpha^{\vdash}$ and differ on an attribute of $\beta \setminus \alpha^{\vdash}$. Hence $F \not\models \alpha \to \beta$. $\square$

The proof also shows that $\alpha^{\vdash} = \alpha^+$, and it contains the key idea of this chapter: a two-tuple relation that agrees exactly on a closed set of attributes satisfies $F$. The same construction proves the correctness of the closure algorithm and of the lossless-join test below.

## 6.4. Computing Attribute Closures

### 6.4.1. The Algorithm

Computing $F^+$ is exponential in the number of attributes, but computing a single attribute closure is fast.

**Algorithm 6.4.1 (Attribute Closure)** Input: a set $\alpha$ of attributes and a set $F$ of functional dependencies. Output: $\alpha^+$.

1. $\mathit{result} \leftarrow \alpha$.
2. Repeat until $\mathit{result}$ does not change: for each $\beta \to \gamma$ in $F$, if $\beta \subseteq \mathit{result}$ then $\mathit{result} \leftarrow \mathit{result} \cup \gamma$.
3. Return $\mathit{result}$.

**Theorem 6.4.1** Algorithm 6.4.1 terminates and returns $\alpha^+$.

**Proof** Each pass of step 2 that changes $\mathit{result}$ adds at least one attribute, so there are at most $\lvert R\rvert$ such passes. Let $Z$ be the returned set.

$Z \subseteq \alpha^+$: by induction on the steps, $F \models \alpha \to \mathit{result}$ at every moment. Initially $\alpha \to \alpha$ holds by reflexivity. If $\alpha \to \mathit{result}$ holds, $\beta \subseteq \mathit{result}$ and $\beta \to \gamma \in F$, then $\alpha \to \beta$ by decomposition, $\alpha \to \gamma$ by transitivity and $\alpha \to \mathit{result} \cup \gamma$ by union.

$\alpha^+ \subseteq Z$: when the algorithm stops, every $\beta \to \gamma \in F$ with $\beta \subseteq Z$ has $\gamma \subseteq Z$. Hence the two-tuple relation that agrees exactly on $Z$ (as in the proof of Theorem 6.3.3) satisfies $F$: if $t_1, t_2$ agree on $\beta$, then $\beta \subseteq Z$, so $\gamma \subseteq Z$ and they agree on $\gamma$. For $A \notin Z$ this relation violates $\alpha \to A$, since $\alpha \subseteq Z$. So $F \not\models \alpha \to A$, that is, $A \notin \alpha^+$. $\square$

As written, the algorithm needs $O(\lvert R\rvert \cdot \lvert F\rvert)$ subset tests; with counters for the number of missing left-hand-side attributes of each dependency it runs in time linear in the total size of $F$ (Beeri and Bernstein, 1979).

**Example 6.4.1** Let $R = (A, B, C, G, H, I)$ and $F = \{A \to B,\ A \to C,\ CG \to H,\ CG \to I,\ B \to H\}$. Computing $(AG)^+$: start with $AG$; $A \to B$ adds $B$, $A \to C$ adds $C$, now $CG \subseteq \mathit{result}$ and $CG \to H$, $CG \to I$ add $H$ and $I$. So $(AG)^+ = ABCGHI = R$, and $AG$ is a superkey. Since $A^+ = ABCH$ and $G^+ = G$ are not $R$, it is a candidate key.

### 6.4.2. Uses of Attribute Closure

The closure algorithm answers the basic questions about dependencies:

| Question | Test |
|---|---|
| Does $\alpha \to \beta$ hold, i.e. is it in $F^+$? | $\beta \subseteq \alpha^+$ |
| Is $\alpha$ a superkey of $R$? | $\alpha^+ = R$ |
| Is $\alpha$ a candidate key? | $\alpha^+ = R$ and $(\alpha \setminus \{A\})^+ \ne R$ for every $A \in \alpha$ |
| What is $F^+$? | for every $\gamma \subseteq R$ and every $S \subseteq \gamma^+$, output $\gamma \to S$ (exponential, rarely needed) |

A Python implementation is short. It represents a dependency as a pair of frozensets; `candidate_keys` tries attribute sets in increasing size and skips the supersets of keys already found, which is exponential in the worst case (a schema can have exponentially many candidate keys) but fast for realistic schemas:

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

## 6.5. Canonical Cover

A set of dependencies often contains redundancy of its own: dependencies implied by the others, or attributes that can be dropped. A minimal equivalent set is useful because every update must be checked against the dependencies, and because the 3NF synthesis algorithm (§6.7.3) produces one relation per dependency.

**Definition 6.5.1 (Extraneous Attribute and Canonical Cover)** Two sets $F$ and $G$ of dependencies are *equivalent* if $F^+ = G^+$. Let $\alpha \to \beta \in F$. An attribute $A \in \alpha$ is **extraneous** in $\alpha$ if $F$ logically implies $(F \setminus \{\alpha \to \beta\}) \cup \{(\alpha \setminus \{A\}) \to \beta\}$; an attribute $A \in \beta$ is extraneous in $\beta$ if $(F \setminus \{\alpha \to \beta\}) \cup \{\alpha \to (\beta \setminus \{A\})\}$ logically implies $F$. A **canonical cover** $F_{\mathrm{c}}$ of $F$ is a set of dependencies equivalent to $F$ in which no dependency contains an extraneous attribute and no two dependencies have the same left side.

Removing an attribute from a left side makes a dependency stronger, so the test asks whether the stronger dependency is still implied by $F$; removing one from a right side makes it weaker, so the test asks whether $F$ is still implied by the weaker set. Both are closure computations:

- $A \in \alpha$ is extraneous if and only if $\beta \subseteq (\alpha \setminus \{A\})^+$ computed under $F$;
- $A \in \beta$ is extraneous if and only if $A \in \alpha^+$ computed under $F' = (F \setminus \{\alpha \to \beta\}) \cup \{\alpha \to (\beta \setminus \{A\})\}$.

**Algorithm 6.5.1 (Canonical Cover)** Repeat until $F$ does not change: replace dependencies with equal left sides $\alpha \to \beta_1$ and $\alpha \to \beta_2$ by $\alpha \to \beta_1\beta_2$ (union rule); find a dependency with an extraneous attribute on either side and delete the attribute; delete any dependency whose right side has become empty. Return $F$.

**Example 6.5.1** Let $R = (A, B, C)$ and $F = \{A \to BC,\ B \to C,\ A \to B,\ AB \to C\}$.

1. Union: $A \to BC$ and $A \to B$ become $A \to BC$; now $F = \{A \to BC, B \to C, AB \to C\}$.
2. $A$ is extraneous in $AB \to C$: under $F$, $B^+ = BC \ni C$. The dependency becomes $B \to C$, already present; $F = \{A \to BC, B \to C\}$.
3. $C$ is extraneous in $A \to BC$: under $\{A \to B, B \to C\}$, $A^+ = ABC \ni C$.

So $F_{\mathrm{c}} = \{A \to B,\ B \to C\}$. A canonical cover need not be unique: for $F = \{A \to BC, B \to AC, C \to AB\}$ both $\{A \to B, B \to C, C \to A\}$ and $\{A \to C, C \to B, B \to A\}$ are canonical covers (and there are others).

## 6.6. Decomposition

### 6.6.1. Lossless Decomposition

**Definition 6.6.1 (Lossless Decomposition)** A *decomposition* of a relation schema $R$ is a set of schemas $\{R_1, \dots, R_n\}$ with $R_1 \cup \cdots \cup R_n = R$. It is **lossless** (a lossless-join decomposition) with respect to a set $F$ of dependencies if every legal relation $r(R)$ satisfying $F$ equals the natural join of its projections:

$$
r = \Pi_{R_1}(r) \bowtie \Pi_{R_2}(r) \bowtie \cdots \bowtie \Pi_{R_n}(r).
$$
A decomposition that is not lossless is *lossy*.

The inclusion $r \subseteq \Pi_{R_1}(r) \bowtie \cdots \bowtie \Pi_{R_n}(r)$ holds for every decomposition, since each $t \in r$ agrees with its own projections. A lossy decomposition therefore never loses tuples; it produces *spurious* tuples, and so loses the information which combinations were actually present. Decomposing $\mathit{gene}$ into $(\mathit{gene\_id}, \mathit{chrom})$ and $(\mathit{chrom}, \mathit{symbol})$ is lossy: joining the two projections back on $\mathit{chrom}$ pairs every gene on a chromosome with every symbol on that chromosome.

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

For a decomposition into two schemas, losslessness can be decided from the dependencies:

**Theorem 6.6.1 (Lossless-Join Test)** A decomposition of $R$ into $R_1$ and $R_2$ is lossless with respect to $F$ if and only if $R_1 \cap R_2 \to R_1$ or $R_1 \cap R_2 \to R_2$ is in $F^+$, that is, if and only if $R_1 \cap R_2$ is a superkey of $R_1$ or of $R_2$.

**Proof** Let $\gamma = R_1 \cap R_2$.

"If": suppose $\gamma \to R_2 \in F^+$ (the other case is symmetric), and let $r$ satisfy $F$. It suffices to show $\Pi_{R_1}(r) \bowtie \Pi_{R_2}(r) \subseteq r$. A tuple $t$ of the join has $t[R_1] = t_1[R_1]$ and $t[R_2] = t_2[R_2]$ for some $t_1, t_2 \in r$, which agree on $\gamma$. Because $r$ satisfies $\gamma \to R_2$, also $t_1[R_2] = t_2[R_2] = t[R_2]$. So $t_1$ agrees with $t$ on $R_1 \cup R_2 = R$, that is, $t = t_1 \in r$.

"Only if": suppose neither dependency is in $F^+$, so $R_1 \not\subseteq \gamma^+$ and $R_2 \not\subseteq \gamma^+$. Let $r = \{t_1, t_2\}$ be the two-tuple relation that agrees exactly on $\gamma^+$; it satisfies $F$ (proof of Theorem 6.4.1). Choose $A \in R_1 \setminus \gamma^+$ and $B \in R_2 \setminus \gamma^+$. Since $\gamma \subseteq \gamma^+$, $A \notin R_2$ and $B \notin R_1$. The projections $t_1[R_1]$ and $t_2[R_2]$ agree on $\gamma$, so the join contains the tuple $t$ with $t[R_1] = t_1[R_1]$ and $t[R_2] = t_2[R_2]$. Then $t[A] = t_1[A] \ne t_2[A]$, so $t \ne t_2$, and $t[B] = t_2[B] \ne t_1[B]$, so $t \ne t_1$. The join contains the spurious tuple $t \notin r$, and the decomposition is lossy. $\square$

In the example above, $R_1 \cap R_2 = \{\mathit{chrom}\}$ determines neither $\mathit{gene\_id}$ nor $\mathit{symbol}$, so the decomposition is lossy. Decomposing $\mathit{results}$ into the sample attributes and the rest is lossless, because the common attribute $\mathit{sample\_id}$ is a key of the sample part.

Decompositions into more than two schemas can be tested by repeated binary splits (as the BCNF algorithm produces them) or, in general, by the *chase* test of Aho, Beeri and Ullman (1979), which builds a tableau with one row per $R_i$ and applies the dependencies until some row becomes free of unknowns.

### 6.6.2. Dependency Preservation

A lossless decomposition keeps the data, but it may lose the ability to check a dependency within a single relation.

**Definition 6.6.2 (Dependency Preservation)** The *restriction* of $F$ to $R_i$ is the set $F_i$ of all dependencies in $F^+$ that contain only attributes of $R_i$. A decomposition $\{R_1, \dots, R_n\}$ is **dependency preserving** if $(F_1 \cup \cdots \cup F_n)^+ = F^+$.

If a decomposition preserves dependencies, every update can be validated by checking each $F_i$ on the relation $r_i$ alone. Otherwise some dependency can be checked only on the join of several relations, which is expensive; in SQL it would need an assertion or a trigger. Computing the $F_i$ requires $F^+$, but there is a polynomial test that avoids it: for each $\alpha \to \beta$ in $F$, start with $\mathit{result} = \alpha$ and repeat, for each $R_i$, $\mathit{result} \leftarrow \mathit{result} \cup ((\mathit{result} \cap R_i)^+ \cap R_i)$ until nothing changes. The dependency is preserved if and only if $\beta \subseteq \mathit{result}$ at the end.

## 6.7. Normal Forms

### 6.7.1. First Normal Form

**Definition 6.7.1 (First Normal Form)** A relation schema is in **first normal form** (1NF) if the domains of all its attributes are atomic.

1NF is a precondition of the relational model ([4.13.2](/4.13.2#sec-2.1.1)) rather than a quality criterion: a column holding the list of a gene's pathways, or a set of numbered columns `pathway_1`, `pathway_2`, `pathway_3`, violates the spirit of it, and is replaced by a separate relation ($\mathit{gene\_pathway}$). Atomicity depends on use: an Ensembl identifier is atomic as long as no query takes it apart, whereas a sample identifier like `liver-ctrl-01` whose parts are parsed by programs is not. Modern systems relax 1NF deliberately with arrays and JSON columns; they are appropriate for data that is always read and written as a whole, not for data that is searched and joined.

### 6.7.2. Boyce–Codd Normal Form

**Definition 6.7.2 (Boyce–Codd Normal Form)** A relation schema $R$ is in **Boyce–Codd normal form** (BCNF) with respect to $F$ if for every functional dependency $\alpha \to \beta$ in $F^+$ with $\alpha, \beta \subseteq R$, at least one of the following holds:

- $\alpha \to \beta$ is trivial ($\beta \subseteq \alpha$);
- $\alpha$ is a superkey of $R$.

A decomposition is in BCNF if each of its schemas is.

In a BCNF schema, every nontrivial dependency says "the key determines this", so every fact is stored once per key value, which is exactly once per tuple. The schema of $\mathit{results}$ is not in BCNF: $\mathit{sample\_id} \to \mathit{tissue}$ is nontrivial, and $\mathit{sample\_id}$ is not a superkey. Each of the five relations of the running example is in BCNF.

To test whether $R$ is in BCNF it suffices to check the dependencies of $F$ rather than all of $F^+$:

**Proposition 6.7.1** If every dependency $\alpha \to \beta \in F$ on $R$ is trivial or has a superkey $\alpha$, then $R$ is in BCNF with respect to $F$.

**Proof** Let $\gamma \to \delta \in F^+$ be nontrivial, and suppose $\gamma$ is not a superkey, so $\gamma^+ \ne R$. Since $\delta \not\subseteq \gamma$ but $\delta \subseteq \gamma^+$, Algorithm 6.4.1 applied to $\gamma$ adds some attribute, using a first dependency $\alpha \to \beta \in F$ with $\alpha \subseteq \gamma$ and $\beta \not\subseteq \gamma$; this dependency is nontrivial. By assumption $\alpha$ is a superkey, so $R = \alpha^+ \subseteq \gamma^+$, a contradiction. $\square$

The shortcut fails for the schemas of a decomposition: there a violation may come from a dependency of $F^+$ that is not in $F$. For $R_i \subseteq R$, the correct test is to check, for every $\alpha \subseteq R_i$, that $\alpha^+$ (under $F$) either contains no attribute of $R_i \setminus \alpha$ or contains all of $R_i$.

**Algorithm 6.7.1 (BCNF Decomposition)** Input: a schema $R$ and dependencies $F$. Output: a lossless decomposition of $R$ into BCNF schemas.

1. $\mathit{result} \leftarrow \{R\}$.
2. While some $R_i \in \mathit{result}$ is not in BCNF: choose a nontrivial $\alpha \to \beta \in F^+$ on $R_i$ such that $\alpha$ is not a superkey of $R_i$ and $\alpha \cap \beta = \varnothing$; replace $R_i$ by the two schemas $R_i \setminus \beta$ and $\alpha \cup \beta$.
3. Return $\mathit{result}$.

(Choosing $\beta = \alpha^+ \cap R_i \setminus \alpha$ makes each step remove as much as possible.)

**Theorem 6.7.2** Algorithm 6.7.1 terminates and produces a lossless decomposition of $R$ in which every schema is in BCNF.

**Proof** Termination: in each step both new schemas are proper subsets of $R_i$. $R_i \setminus \beta \ne R_i$ because $\beta \ne \varnothing$ (the dependency is nontrivial and $\alpha \cap \beta = \varnothing$), and $\alpha \cup \beta \ne R_i$ because $\alpha$ is not a superkey of $R_i$, while $\alpha \to \alpha\beta$ holds. Schemas cannot shrink forever, and every schema with at most two attributes is in BCNF (any nontrivial dependency on $\{A, B\}$ is $A \to B$ or $B \to A$, with a superkey on the left), so the loop stops.

BCNF: the loop stops only when every schema is in BCNF.

Losslessness: each step is a lossless binary decomposition by Theorem 6.6.1, because $(R_i \setminus \beta) \cap (\alpha \cup \beta) = \alpha$ and $\alpha \to \alpha \cup \beta$ holds. A lossless decomposition of one component of a lossless decomposition is again lossless: if $r = \Pi_{R_1}(r) \bowtie \Pi_{R_2}(r)$ and $R_1$ is split into $R_{11}, R_{12}$, then $\Pi_{R_1}(r)$ satisfies the restriction of $F$ to $R_1$, so $\Pi_{R_1}(r) = \Pi_{R_{11}}(r) \bowtie \Pi_{R_{12}}(r)$, and substituting gives $r = \Pi_{R_{11}}(r) \bowtie \Pi_{R_{12}}(r) \bowtie \Pi_{R_2}(r)$ by the associativity of the natural join ([4.13.2](/4.13.2#sec-2.3.2)). By induction on the number of steps the final decomposition is lossless. $\square$

The decomposition is not unique: it depends on the order in which violations are chosen.

### 6.7.3. Third Normal Form

BCNF cannot always be reached while preserving dependencies.

**Example 6.7.1** A core facility records which operator processed each sample in each assay. Each operator is trained for exactly one assay, and each sample is processed in each assay by one operator: on $R = (\mathit{sample\_id}, \mathit{assay}, \mathit{operator})$,

$$
F = \{\mathit{operator} \to \mathit{assay},\ \ \mathit{sample\_id}\ \mathit{assay} \to \mathit{operator}\}.
$$

The candidate keys are $\{\mathit{sample\_id}, \mathit{assay}\}$ and $\{\mathit{sample\_id}, \mathit{operator}\}$. $R$ is not in BCNF, since $\mathit{operator}$ is not a superkey. The BCNF decomposition $\{(\mathit{operator}, \mathit{assay}), (\mathit{sample\_id}, \mathit{operator})\}$ is lossless, but no schema contains all of $\mathit{sample\_id}, \mathit{assay}, \mathit{operator}$, so $\mathit{sample\_id}\ \mathit{assay} \to \mathit{operator}$ is not preserved: two operators trained for the same assay could both be recorded for one sample without any single relation noticing. Every BCNF decomposition of $R$ has this defect, because the only schema containing the three attributes is $R$ itself.

Third normal form relaxes BCNF just enough to allow such schemas.

**Definition 6.7.3 (Third Normal Form)** A relation schema $R$ is in **third normal form** (3NF) with respect to $F$ if for every $\alpha \to \beta$ in $F^+$ with $\alpha, \beta \subseteq R$, at least one of the following holds:

- $\alpha \to \beta$ is trivial;
- $\alpha$ is a superkey of $R$;
- every attribute in $\beta \setminus \alpha$ is contained in some candidate key of $R$; such an attribute is called a **prime attribute**.

Every BCNF schema is in 3NF; the schema of Example 6.7.1 is in 3NF but not in BCNF, because $\mathit{assay}$ is prime. The third condition is the price of dependency preservation: some redundancy is allowed (the assay of an operator is repeated for every sample the operator processed), but only in prime attributes.

**Algorithm 6.7.2 (3NF Synthesis)** Input: a schema $R$ and dependencies $F$. Output: a lossless, dependency-preserving decomposition into 3NF schemas.

1. Compute a canonical cover $F_{\mathrm{c}}$ of $F$.
2. For each $\alpha \to \beta$ in $F_{\mathrm{c}}$, add the schema $\alpha\beta$ to the result.
3. If no schema of the result contains a candidate key of $R$, add a schema consisting of one candidate key.
4. Remove each schema that is contained in another schema of the result.

**Theorem 6.7.3** Algorithm 6.7.2 produces a decomposition that is dependency preserving, lossless, and in which every schema is in 3NF.

**Proof** (sketch) Dependency preservation: every dependency of $F_{\mathrm{c}}$ lies within one schema of the result (step 4 removes a schema only when a larger one contains it), and $F_{\mathrm{c}}$ is equivalent to $F$. Losslessness: let $K$ be the candidate key contained in some schema $R_j$. Computing $K^+ = R$ with Algorithm 6.4.1 applies a sequence of dependencies of $F_{\mathrm{c}}$, each contained in a schema of the result; by induction along this sequence, the chase test shows that joining the projections on these schemas with $R_j$ creates no spurious tuples. 3NF: consider a schema $\alpha\beta$ created from $\alpha \to \beta \in F_{\mathrm{c}}$. $\alpha$ is a candidate key of $\alpha\beta$, since by the minimality of the canonical cover no proper subset of $\alpha$ determines $\beta$. If a nontrivial $\gamma \to B$ holds on $\alpha\beta$ with $\gamma$ not a superkey and $B$ not prime, then $B \in \beta$, and one shows that $B$ would be extraneous in $\alpha \to \beta$, contradicting the canonical cover; the schema containing only a candidate key has no nontrivial dependency with a non-superkey on the left. The full argument is in Silberschatz et al., Chapter 7. $\square$

For Example 6.7.1, $F$ is its own canonical cover; step 2 creates $(\mathit{operator}, \mathit{assay})$ and $(\mathit{sample\_id}, \mathit{assay}, \mathit{operator})$, and step 4 removes the first because it is contained in the second. The result is $R$ itself, which is in 3NF.

The choice between the two normal forms is a design decision:

| | BCNF | 3NF |
|---|---|---|
| redundancy from functional dependencies | none | possible in prime attributes |
| lossless decomposition | always achievable | always achievable |
| dependency preservation | not always achievable | always achievable |
| algorithm | decomposition (Algorithm 6.7.1) | synthesis from a canonical cover (Algorithm 6.7.2) |

In practice BCNF is the goal. When it would lose a dependency, as in Example 6.7.1, designers either accept the 3NF schema, or use the BCNF decomposition and enforce the lost dependency separately (here, a `UNIQUE (sample_id, assay)` constraint on a table that stores the assay redundantly, or a trigger).

### 6.7.4. Second Normal Form

**Definition 6.7.4 (Second Normal Form)** A relation schema is in **second normal form** (2NF) if it is in 1NF and no nonprime attribute is *partially dependent* on a candidate key, that is, determined by a proper subset of a candidate key.

2NF is of historical interest; it lies between 1NF and 3NF and is implied by 3NF. The table $\mathit{results}$ violates even 2NF, since $\mathit{tissue}$ depends on $\mathit{sample\_id}$, a proper subset of the candidate key $\{\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id}\}$. A schema in 2NF but not 3NF has a *transitive* dependency of a nonprime attribute on a key through another nonprime attribute, such as $\mathit{gene\_id} \to \mathit{chrom} \to \mathit{chrom\_length}$ if the chromosome length were stored with every gene. The inclusions are BCNF $\subsetneq$ 3NF $\subsetneq$ 2NF $\subsetneq$ 1NF.

### 6.7.5. Multivalued Dependencies and Fourth Normal Form

Some redundancy is not caused by functional dependencies at all. In $\mathit{results}$, the pathways of a gene do not depend on the sample: every sample in which TP53 is measured is combined with both of TP53's pathways. The relation on $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$ that remains after removing all functional-dependency violations has no nontrivial functional dependency, so it is in BCNF, and yet it stores "TP53 belongs to PW2" once for every sample.

**Definition 6.7.5 (Multivalued Dependency)** Let $\alpha, \beta \subseteq R$ and $\gamma = R \setminus \alpha\beta$. The **multivalued dependency** $\alpha \twoheadrightarrow \beta$ holds on $R$ if, in every legal relation $r(R)$, for all tuples $t_1, t_2 \in r$ with $t_1[\alpha] = t_2[\alpha]$ there is a tuple $t_3 \in r$ with $t_3[\alpha] = t_1[\alpha]$, $t_3[\beta] = t_1[\beta]$ and $t_3[\gamma] = t_2[\gamma]$.

Thus $\mathit{gene\_id} \twoheadrightarrow \mathit{pathway\_id}$ says that, for a given gene, the set of its pathways and the set of its samples are independent: every combination occurs. Every functional dependency $\alpha \to \beta$ is also a multivalued dependency $\alpha \twoheadrightarrow \beta$. The analogue of Theorem 6.6.1 is Fagin's theorem (1977): the decomposition of $R$ into $\alpha\beta$ and $\alpha\gamma$ is lossless if and only if $\alpha \twoheadrightarrow \beta$ holds.

**Definition 6.7.6 (Fourth Normal Form)** A relation schema $R$ is in **fourth normal form** (4NF) with respect to a set $D$ of functional and multivalued dependencies if for every multivalued dependency $\alpha \twoheadrightarrow \beta$ in $D^+$ on $R$, either it is trivial ($\beta \subseteq \alpha$ or $\alpha\beta = R$) or $\alpha$ is a superkey of $R$.

4NF implies BCNF. The decomposition algorithm is the same as for BCNF, with multivalued dependencies in place of functional ones. Normal forms beyond 4NF (project-join normal form, based on join dependencies) exist but are rarely needed in practice.

## 6.8. A Worked Normalization

We now normalize the table $\mathit{results}$ of §6.2 with the dependencies $F$ of Example 6.3.1.

### 6.8.1. Candidate Keys

No dependency has $\mathit{sample\_id}$ on its right side, and none of the gene or pathway attributes determines it, so every key contains $\mathit{sample\_id}$; likewise every key contains a gene identifier ($\mathit{gene\_id}$ or $\mathit{symbol}$) and a pathway identifier ($\mathit{pathway\_id}$ or $\mathit{pathway\_name}$). Closures confirm that $\{\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id}\}^+$ is all of $\mathit{results}$, and the two choices of a gene identifier and of a pathway identifier give four candidate keys.

### 6.8.2. BCNF Decomposition

Each dependency of $F$ violates BCNF on $\mathit{results}$. A small implementation of Algorithm 6.7.1, using the `closure` function of §6.4.2 to find violations, records each split:

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

(The subset search in `bcnf_violation` is exponential and serves only small examples.) The first four schemas are $\mathit{gene}$, $\mathit{pathway}$, $\mathit{sample}$ and $\mathit{measurement}$ of the running example, with $\mathit{name}$ renamed. The decomposition is lossless by Theorem 6.7.2 and here also dependency preserving: each dependency of $F$ lies within one schema ($\mathit{symbol} \to \mathit{gene\_id}$ within $\mathit{gene}$, where $\mathit{symbol}$ is the second candidate key and is declared `UNIQUE`).

### 6.8.3. Fourth Normal Form

The last schema, $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$, is in BCNF but not in 4NF, because of $\mathit{gene\_id} \twoheadrightarrow \mathit{pathway\_id}$ (§6.7.5). By Fagin's theorem it decomposes losslessly into $(\mathit{gene\_id}, \mathit{pathway\_id})$, which is $\mathit{gene\_pathway}$, and $(\mathit{gene\_id}, \mathit{sample\_id})$, which is already contained in $\mathit{measurement}$ and is dropped. The result is exactly the schema of [4.13.3](/4.13.3#sec-3.2.3), now with a proof that it has none of the anomalies of §6.2. It also resolves a defect of the spreadsheet that the dependencies do not show: a gene without a pathway, such as ACTB, could be stored in $\mathit{results}$ only with a null in the key attribute $\mathit{pathway\_id}$, whereas the normalized schema simply has no row for it in $\mathit{gene\_pathway}$.

The 3NF synthesis algorithm gives the same result here: $F$ is already a canonical cover apart from merging the two dependencies with left side $\mathit{gene\_id}$; the schemas for $\mathit{symbol} \to \mathit{gene\_id}$ and $\mathit{pathway\_name} \to \mathit{pathway\_id}$ are contained in those for $\mathit{gene\_id}$ and $\mathit{pathway\_id}$ and are removed, and a schema for the candidate key $(\mathit{sample\_id}, \mathit{gene\_id}, \mathit{pathway\_id})$ is added.

## 6.9. Normalization in Practice

Normalization and E-R design approach the same goal from two directions, and a careful E-R design (one entity set per kind of object, relationship sets for the associations, multivalued attributes as separate relations) usually yields BCNF schemas directly. Dependencies that the E-R design overlooked show up as violations, for example an attribute $\mathit{chrom\_length}$ attached to the entity set *gene*, which really describes a chromosome entity set.

Normalized schemas need joins to reassemble the data, and a design is sometimes *denormalized* on purpose: a redundant copy of the gene symbol in a reporting table, or a precomputed summary per gene and tissue, avoids joins in frequent queries. The cost is that the redundant copies must be kept consistent, by triggers, by materialized views ([4.13.4](/4.13.4#sec-4.6)) or by recomputing them periodically; materialized views are usually the cleanest solution. Analytical databases (data warehouses) routinely use a *star schema*, a large normalized *fact table* (the measurements) surrounded by deliberately denormalized *dimension tables* (samples with all their attributes, genes with their annotation), because they are read far more often than written. And a few things that look like violations are not: storing the donor's age *at collection* together with the sample is not redundant if the date of birth is not recorded, since then nothing else determines it.

## Summary

- Integrity constraints (domain, key, entity integrity, referential integrity, `CHECK`) are declared in the schema and enforced by the DBMS on every modification. Referential actions (`NO ACTION`, `RESTRICT`, `CASCADE`, `SET NULL`, `SET DEFAULT`) decide what happens to references when a referenced row goes away; checks can be deferred to commit.
- Assertions are standard but not implemented; triggers (event–condition–action, `BEFORE`/`AFTER`/`INSTEAD OF`, per row or per statement) serve audit logs, derived data and undeclarable constraints.
- Redundancy causes update, insertion and deletion anomalies. A functional dependency $\alpha \to \beta$ states that $\alpha$ determines $\beta$; keys are the sets that determine everything.
- Armstrong's axioms (reflexivity, augmentation, transitivity) are sound and complete for $F^+$; the attribute closure $\alpha^+$, computed by a simple fixed-point algorithm, decides $\alpha \to \beta \in F^+$ ($\beta \subseteq \alpha^+$) and superkeys ($\alpha^+ = R$). A canonical cover removes extraneous attributes.
- A binary decomposition is lossless iff the common attributes are a superkey of one side; a decomposition preserves dependencies if the restrictions of $F$ imply $F$.
- BCNF: every nontrivial dependency has a superkey on the left; the decomposition algorithm is lossless but may lose dependencies. 3NF additionally allows prime attributes on the right; the synthesis algorithm is lossless and dependency preserving. 4NF extends BCNF to multivalued dependencies.
- Normalizing a spreadsheet of measurements with sample, gene and pathway attributes yields exactly the five relations of the running example.
