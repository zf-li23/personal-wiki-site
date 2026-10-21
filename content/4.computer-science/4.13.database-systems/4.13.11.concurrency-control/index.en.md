---
title: Concurrency Control
description: "How a DBMS achieves isolation: shared and exclusive locks and the lock manager; two-phase locking with the proof that it guarantees conflict serializability, strict and rigorous 2PL; deadlock detection with wait-for graphs and prevention by wait-die and wound-wait (a runnable lock manager); multiple-granularity locking with intention locks; phantoms, predicate and next-key locking; timestamp ordering, the Thomas write rule and optimistic validation; multiversion concurrency control, snapshot isolation, write skew and serializable snapshot isolation; SQL isolation levels and their implementation in PostgreSQL, MySQL, SQLite and DuckDB, with measured behaviour."
---

[4.13.10](/4.13.10) defined what a correct concurrent execution is: a **schedule** that is **conflict serializable** and, in practice, strict. It did not say how a system produces such schedules while **transactions** arrive, run and finish unpredictably. This chapter presents the protocols that do so. *Locking* makes transactions wait for each other, and two-phase locking is the classical protocol that guarantees serializability; its price is waiting and deadlocks, which the system must detect or prevent. *Timestamp* and *optimistic* protocols order transactions in advance or check them at the end instead of waiting. *Multiversion* concurrency control keeps old versions of data so that readers never wait for writers; it is how PostgreSQL, MySQL's InnoDB, Oracle, DuckDB and most modern systems work, and it leads to *snapshot isolation*, a weaker guarantee than serializability with its own anomalies. The chapter ends with the isolation levels of SQL and what they mean in each system. The synchronization primitives of operating systems, the mutex, the reader–writer lock and **deadlock** handling ([4.11.6](/4.11.6)), are the building blocks underneath; the database protocols add the transaction as the unit of protection.

## 11.1. Lock-Based Protocols

### 11.1.1. Locks and the Lock Manager

**Definition 11.1.1 (Shared and Exclusive Locks)** A transaction that holds a **shared lock** (S lock) on a data item may read but not write it; one that holds an **exclusive lock** (X lock) may read and write it. A transaction must hold an appropriate lock before accessing an item. A lock request is granted only if the requested mode is compatible with the locks held on the item by other transactions; otherwise the requesting transaction waits.

| Requested \ held | S | X |
|---|---|---|
| S | compatible | conflict |
| X | conflict | conflict |

Any number of **transactions** may hold **S locks** on an item at once, an **X lock** excludes every other lock: this is the semantics of the **reader–writer lock** of [4.11.6](/4.11.6). The *lock manager* keeps a hash table, the *lock table*, from data items to records listing the granted locks and a queue of waiting requests; a request is granted if it is compatible with all granted locks and, to avoid starving writers, if no earlier request is waiting. A transaction that holds an S lock and wants to write may request an *upgrade* to X.

**Remark 11.1.1 (Locks and Latches)** **Database systems** distinguish locks, which protect the logical contents of the **database** between transactions, from *latches*, which protect in-memory data structures between **threads**.

| | Locks | Latches |
|---|---|---|
| Protect | rows, tables, key ranges | buffer-pool pages, the lock table, B+-tree nodes |
| Held by, for | a transaction, usually until commit | a thread, for a short critical section |
| Modes | S, X, intention modes (§11.4) | read, write |
| Deadlocks | detected and resolved by the DBMS | avoided by a fixed acquisition order |
| Implementation | entries in the lock manager | a mutex or spin lock in the object |

The concurrency-control protocols of this chapter concern locks; latches are the operating-system kind of locking applied inside the **DBMS** ([4.13.8](/4.13.8#sec-8.2.5)).

### 11.1.2. Why Locking Alone Is Not Enough

Locking each item only while it is accessed does not ensure **serializability**. Let $T_1$ move 50 units from $A$ to $B$ and $T_2$ print $A + B$, each locking an item just before accessing it and unlocking it right afterwards:

| Step | $T_1$ | $T_2$ |
|---|---|---|
| 1 | X-lock($A$); $R_1(A)$; $W_1(A)$; unlock($A$) | |
| 2 | | S-lock($A$); $R_2(A)$; unlock($A$) |
| 3 | | S-lock($B$); $R_2(B)$; unlock($B$) |
| 4 | X-lock($B$); $R_1(B)$; $W_1(B)$; unlock($B$) | |

Every access is protected by a lock, yet $T_2$ sees the new value of $A$ and the old value of $B$ and prints a sum that is 50 too small. The **precedence graph** has the edges $T_1 \to T_2$ (on $A$) and $T_2 \to T_1$ (on $B$). The cure is a discipline on *when* locks may be released.

## 11.2. Two-Phase Locking

### 11.2.1. The Protocol

**Definition 11.2.1 (Two-Phase Locking)** A transaction follows **two-phase locking** (2PL) if all its lock requests precede all its unlock operations. Its execution has a *growing phase*, in which it acquires locks and releases none, and a *shrinking phase*, in which it releases locks and acquires none. The moment of its last lock acquisition is its *lock point*.

**Theorem 11.2.1** If every **transaction** of a **schedule** follows **two-phase locking**, the schedule is conflict serializable; an equivalent serial order is the order of the lock points.

**Proof** Let $T_i \to T_j$ be an edge of the **precedence graph**: an operation of $T_i$ on an item $Q$ precedes a conflicting operation of $T_j$ on $Q$. The two operations need incompatible locks on $Q$, so $T_i$ must release its lock on $Q$ at some time $r$ before $T_j$ obtains its lock on $Q$ at some time $a$, with $r < a$. Since $T_i$ follows 2PL, it releases no lock before its **lock point**, so $\mathrm{LP}(T_i) \le r$; since $T_j$ acquires its lock on $Q$ no later than its lock point, $a \le \mathrm{LP}(T_j)$. Hence $\mathrm{LP}(T_i) < \mathrm{LP}(T_j)$. Every edge goes from an earlier to a later lock point, so the graph has no cycle, and by Theorem 10.2.1 the schedule is **conflict serializable**, with the transactions in the order of their lock points as an equivalent serial order. $\square$

The converse does not hold: some conflict **serializable schedules** cannot be produced by 2PL. Nor does 2PL avoid **cascading rollbacks**: a transaction may release an **X lock** in its shrinking phase, before it commits, and another transaction may read the uncommitted value.

**Definition 11.2.2 (Strict and Rigorous 2PL)** Under **strict two-phase locking**, a transaction follows 2PL and holds all its exclusive locks until it commits or aborts. Under **rigorous two-phase locking**, it holds all its locks, shared and exclusive, until it commits or aborts.

**Strict 2PL** produces schedules that are conflict serializable and strict ([4.13.10](/4.13.10#sec-10.3)), so recovery by before-images is correct. **Rigorous 2PL** additionally makes the **commit** order an equivalent serial order, which is convenient for replication and distributed transactions. Lock-based systems almost always use rigorous 2PL; the application never writes lock or unlock operations, the DBMS acquires the locks as statements touch rows and releases them all at commit. SQL lets a transaction take row locks explicitly while reading, with `SELECT ... FOR UPDATE` (X) and `SELECT ... FOR SHARE` (S), which is the standard way to avoid lost updates under weaker isolation levels (§11.7).

### 11.2.2. Deadlocks

Two-phase locking does not prevent **deadlocks**: if $T_1$ holds an **S lock** on $A$ and requests X on $B$ while $T_2$ holds S on $B$ and requests X on $A$, both wait forever. All four **Coffman conditions** of [4.11.6](/4.11.6#sec-6.5.2) hold, and the **DBMS**, which knows all locks, handles deadlocks itself.

**Definition 11.2.3 (Wait-For Graph)** The **wait-for graph** of a set of transactions has an edge $T_i \to T_j$ whenever $T_i$ is waiting for a lock held by $T_j$.

A deadlock exists if and only if the **wait-for graph** has a cycle. *Deadlock detection* checks the graph for cycles, either whenever a request has to wait or periodically, and breaks each cycle by aborting a *victim*, typically the youngest transaction or the one that has done the least work; the victim's locks are released and its client receives an error and can retry. PostgreSQL runs the check when a transaction has waited for `deadlock_timeout` (1 second by default), so that the common case of a short wait costs nothing; InnoDB checks immediately on every wait.

The following **lock manager** implements strict 2PL with first-come first-served queues and detects deadlocks with a **depth-first search** for a cycle in the wait-for graph.

```python
from collections import defaultdict, deque

COMPATIBLE = {("S", "S")}                     # every other pair of modes conflicts


class LockManager:
    """Strict two-phase locking with deadlock detection on a wait-for graph."""

    def __init__(self):
        self.granted = defaultdict(dict)       # item -> {txn: mode}
        self.queue = defaultdict(deque)        # item -> waiting (txn, mode)
        self.waiting = {}                      # txn -> item it waits for

    def _grantable(self, item, txn, mode):
        others = {t: m for t, m in self.granted[item].items() if t != txn}
        return all((m, mode) in COMPATIBLE for m in others.values())

    def request(self, txn, mode, item):
        held = self.granted[item].get(txn)
        if held == "X" or held == mode:
            return True                         # already held
        if not self.queue[item] and self._grantable(item, txn, mode):
            self.granted[item][txn] = mode      # grant (or upgrade S to X)
            return True
        self.queue[item].append((txn, mode))
        self.waiting[txn] = item
        return False

    def wait_for_graph(self):
        edges = set()
        for txn, item in self.waiting.items():
            for holder in self.granted[item]:
                if holder != txn:
                    edges.add((txn, holder))
        return edges

    def find_cycle(self):
        graph = defaultdict(list)
        for a, b in self.wait_for_graph():
            graph[a].append(b)
        color = {}

        def dfs(u, path):
            color[u] = "grey"
            path.append(u)
            for v in graph[u]:
                if color.get(v) == "grey":
                    return path[path.index(v):]
                if v not in color and (c := dfs(v, path)):
                    return c
            color[u] = "black"
            path.pop()
            return None

        for u in list(graph):
            if u not in color and (c := dfs(u, [])):
                return c
        return None

    def release_all(self, txn):
        """At commit or abort: release every lock and wake up the waiters."""
        woken = []
        self.waiting.pop(txn, None)
        for item in list(self.granted):
            self.granted[item].pop(txn, None)
            self.queue[item] = deque((t, m) for t, m in self.queue[item] if t != txn)
            while self.queue[item] and self._grantable(item, *self.queue[item][0]):
                t, m = self.queue[item].popleft()
                self.granted[item][t] = m
                del self.waiting[t]
                woken.append(f"{t} gets {m}({item})")
        return woken


lm = LockManager()
start = {"T1": 1, "T2": 2, "T3": 3}            # start timestamps: larger = younger
schedule = [("T1", "S", "A"), ("T2", "S", "B"), ("T3", "S", "A"),
            ("T1", "X", "B"), ("T2", "X", "A"), ("T3", "commit", None),
            ("T1", "commit", None)]
for txn, op, item in schedule:
    if op == "commit":
        print(f"{txn} commits; " + ", ".join(lm.release_all(txn) or ["nobody woken"]))
        continue
    ok = lm.request(txn, op, item)
    print(f"{txn} requests {op}({item}): {'granted' if ok else 'waits'}")
    if not ok:
        print("   wait-for graph:", sorted(lm.wait_for_graph()))
        cycle = lm.find_cycle()
        if cycle:
            victim = max(cycle, key=start.get)          # abort the youngest
            print(f"   deadlock {' -> '.join(cycle + cycle[:1])}; abort {victim}; "
                  + ", ".join(lm.release_all(victim)))
```

```text
T1 requests S(A): granted
T2 requests S(B): granted
T3 requests S(A): granted
T1 requests X(B): waits
   wait-for graph: [('T1', 'T2')]
T2 requests X(A): waits
   wait-for graph: [('T1', 'T2'), ('T2', 'T1'), ('T2', 'T3')]
   deadlock T2 -> T1 -> T2; abort T2; T1 gets X(B)
T3 commits; nobody woken
T1 commits; nobody woken
```

$T_2$'s request for an X lock on $A$ must wait for both readers of $A$, $T_1$ and $T_3$, and closes the cycle $T_1 \to T_2 \to T_1$. Aborting the youngest transaction of the cycle, $T_2$, releases its S lock on $B$, and $T_1$'s waiting request is granted. $T_3$ was never part of the deadlock.

*Deadlock prevention* ensures instead that a cycle can never form, using the start timestamp $\mathrm{TS}(T)$ of each transaction (a restarted transaction keeps its original timestamp). When $T_i$ requests a lock held by $T_j$:

- *wait-die*: if $T_i$ is older ($\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$), $T_i$ waits; otherwise $T_i$ is rolled back ("dies");
- *wound-wait*: if $T_i$ is older, $T_j$ is rolled back ("wounded"); otherwise $T_i$ waits.

**Proposition 11.2.1** Under **wait-die** and under **wound-wait** no deadlock occurs, and every transaction eventually completes.

**Proof** Under wait-die, a transaction waits only for a younger one, so every edge $T_i \to T_j$ of the wait-for graph satisfies $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$; timestamps strictly increase along every path, so there is no cycle. Under wound-wait, a transaction waits only for an older one, and timestamps strictly decrease along every path. Since a restarted transaction keeps its timestamp, it eventually becomes the oldest active transaction, which under wait-die never dies and under wound-wait is never wounded, so it completes. $\square$

A simple alternative used by many systems is a *lock timeout*: a request that waits too long is cancelled (`lock_timeout` in PostgreSQL, `innodb_lock_wait_timeout` in MySQL).

## 11.3. Phantoms and Predicate Locking

Locking the rows a **transaction** has read is not enough when the transaction reads a set of rows defined by a condition. Suppose $T_1$ counts the liver samples twice, and between the two counts $T_2$ inserts a new liver sample and **commits**. $T_2$ wrote no row that $T_1$ had locked, yet the two counts of $T_1$ differ, and no serial order explains them: $T_1$ conflicts with $T_2$ on a row that did not exist when $T_1$ first read. Such a row is a *phantom*.

The conflict is on the condition `tissue = 'liver'`. *Predicate locking* locks the condition itself, so that an insertion of a row satisfying a locked predicate conflicts with the lock; deciding whether two predicates overlap is expensive in general, and systems lock approximations instead:

- *Index locking*: a query that finds rows through an **index** locks the index leaf **pages** or entries it scans, and an insertion must lock the leaf entry where the new key goes; a query without a suitable index locks the whole table.
- *Next-key locking* (InnoDB): locking an index record also locks the gap before it, so that a range scan over `tissue BETWEEN 'kidney' AND 'liver'` blocks insertions into the scanned key range. InnoDB uses next-key locks for locking reads and updates at its default `REPEATABLE READ` level.
- PostgreSQL's serializable level (§11.6.3) records *SIRead* predicate locks on the index pages and **tuples** read; they never block, but feed the detection of dangerous dependency patterns.

## 11.4. Multiple Granularity

Locking every row of a table to scan it costs a lock-table entry per row; locking the whole table to update one row blocks everyone. A system therefore locks items of several sizes: the **database**, tables, **pages** and rows, organized as a tree in which locking a node implicitly locks all its descendants. To check quickly whether a table lock conflicts with row locks below it, **transactions** announce their intentions on the ancestors.

**Definition 11.4.1 (Intention Locks)** In **multiple-granularity locking**, besides S and X there are three **intention lock** modes: *intention-shared* (IS) and *intention-exclusive* (IX), which announce that the transaction will lock some descendant of the node in S mode, respectively in X (or S) mode, and *shared and intention-exclusive* (SIX), which locks the node in S mode and announces X locks on descendants. The compatibility of the modes is:

| Requested \ held | IS | IX | S | SIX | X |
|---|---|---|---|---|---|
| IS | yes | yes | yes | yes | no |
| IX | yes | yes | no | no | no |
| S | yes | no | yes | no | no |
| SIX | yes | no | no | no | no |
| X | no | no | no | no | no |

The protocol: locks are acquired from the root downwards; a node may be locked in S or IS mode only if its parent is held in IS or IX mode, and in X, SIX or IX mode only if its parent is held in IX or SIX mode; locks are released from the leaves upwards, and the transaction follows **two-phase locking**. A transaction that scans a table and updates a few rows takes SIX on the table and X on those rows; a concurrent reader of single rows takes IS on the table and S on rows, which is compatible with SIX. If a transaction acquires too many row locks, the system may replace them with one table lock (*lock escalation*; SQL Server does so at about 5,000 locks on one object).

PostgreSQL has eight table-level lock modes (from `ACCESS SHARE`, taken by every `SELECT`, through `ROW EXCLUSIVE`, taken by `INSERT`, `UPDATE` and `DELETE`, to `ACCESS EXCLUSIVE`, taken by `DROP TABLE` and most `ALTER TABLE` forms), which play the role of **intention locks**, and four row-level modes (`FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, `FOR KEY SHARE`). Row locks are recorded in the row version itself (in `xmax`), not in the **shared lock** table, so PostgreSQL never needs **lock escalation**; the price is a disk write for every locked row.

## 11.5. Timestamp-Based Protocols

### 11.5.1. Timestamp Ordering

Instead of discovering a serial order through waiting, a timestamp protocol fixes it in advance: the order of the start timestamps.

**Definition 11.5.1 (Timestamp-Ordering Protocol)** Each transaction $T_i$ receives a unique timestamp $\mathrm{TS}(T_i)$ when it starts, and each data item $Q$ carries $\mathrm{W\text{-}TS}(Q)$ and $\mathrm{R\text{-}TS}(Q)$, the largest timestamps of transactions that wrote and read it. The **timestamp-ordering protocol** handles operations as follows:

1. $T_i$ issues $\operatorname{read}(Q)$: if $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$, $T_i$ would read a value written by a younger **transaction**, so it is rolled back; otherwise the read is executed and $\mathrm{R\text{-}TS}(Q) := \max(\mathrm{R\text{-}TS}(Q), \mathrm{TS}(T_i))$.
2. $T_i$ issues $\operatorname{write}(Q)$: if $\mathrm{TS}(T_i) < \mathrm{R\text{-}TS}(Q)$, a younger transaction has already read the old value, and $T_i$ is rolled back; if $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$, $T_i$ would overwrite a younger write, and $T_i$ is rolled back; otherwise the write is executed and $\mathrm{W\text{-}TS}(Q) := \mathrm{TS}(T_i)$.

A rolled-back transaction restarts with a new, larger timestamp.

**Proposition 11.5.1** Every **schedule** produced by the **timestamp-ordering protocol** is **conflict serializable**, with the timestamp order as an equivalent serial order, and the protocol is free of deadlocks.

**Proof** Suppose operations $o_i$ of $T_i$ and $o_j$ of $T_j$ on $Q$ conflict and $o_i$ is executed first. If $o_i$ is a write, then $\mathrm{W\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$ afterwards, and $o_j$ (a read or a write) is executed only if $\mathrm{TS}(T_j) > \mathrm{W\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$ (timestamps are unique). If $o_i$ is a read, then $o_j$ is a write, $\mathrm{R\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$, and $o_j$ is executed only if $\mathrm{TS}(T_j) > \mathrm{TS}(T_i)$. Thus every edge $T_i \to T_j$ of the **precedence graph** has $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$, and the graph is acyclic. No transaction ever waits, so there are no **deadlocks**. $\square$

Basic timestamp ordering may produce unrecoverable schedules, since a transaction can read a value written by an uncommitted older one; it is made recoverable by delaying reads of uncommitted data or **commits**. The *Thomas write rule* weakens rule 2: if $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$ but $\mathrm{TS}(T_i) \ge \mathrm{R\text{-}TS}(Q)$, the write is obsolete (no one will read it in the timestamp order) and is ignored instead of rolling back $T_i$. The resulting schedules are **view serializable** but not always conflict serializable.

### 11.5.2. Optimistic Concurrency Control

When conflicts are rare, checking at the end is cheaper than locking. In *validation-based* (optimistic) concurrency control, a transaction runs in three phases: a *read phase*, in which it executes and writes only to private copies; a *validation phase* at commit, in which it is checked against the transactions that committed during its lifetime; and a *write phase*, in which its changes are installed. With validation timestamps $\mathrm{TS}(T_i)$ assigned at the start of validation, $T_j$ passes the test against every $T_i$ with $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$ if either $T_i$ finished before $T_j$ started, or $T_i$ finished its write phase before $T_j$ started validation and the set of items written by $T_i$ is disjoint from the set read by $T_j$. Otherwise $T_j$ is rolled back. Optimistic schemes never block and suit read-mostly workloads and in-memory systems (Microsoft's Hekaton engine for SQL Server is an example); under contention they waste work on rolled-back transactions. Application-level optimistic locking with a version column (`UPDATE ... SET ..., version = version + 1 WHERE id = ? AND version = ?`, retrying if no row was updated) applies the same idea across requests of a web application.

## 11.6. Multiversion Concurrency Control

### 11.6.1. Versions and Snapshots

Under locking, a reader of a row waits for the writer that holds an **X lock** on it, and a writer waits for readers. *Multiversion concurrency control* (MVCC) removes both waits by keeping several versions of each item: a write creates a new version, and a reader is directed to the version that is appropriate for it, without any lock. The cost is storage for old versions and their **garbage collection**.

In PostgreSQL each row version (**tuple**) stores the identifier of the **transaction** that created it, `xmin`, and of the transaction that deleted or replaced it, `xmax` (0 if none); an `UPDATE` marks the old version with its `xmax` and inserts a new version with its `xmin`, linked through `ctid` ([4.13.7](/4.13.7#sec-7.3.2)). A *snapshot* records which transactions count as committed for a reader: all transaction identifiers below a bound `xmin`, none at or above a bound `xmax`, and, in between, those not in a list of transactions that were in progress when the snapshot was taken. A version is *visible* in a snapshot if its creating transaction is committed in the snapshot and its deleting transaction (if any) is not. Committed status comes from the **commit** log `pg_xact`.

**Example 11.6.1** Transaction 100 updates the age of sample `S01` from 54 to 55 and commits; transaction 101 took its **snapshot** while 100 was still running (100 is in its in-progress list), and transaction 102 started after the commit.

| Version | `xmin` | `xmax` | Visible to 101 | Visible to 102 |
|---|---|---|---|---|
| (`S01`, age 54) | 90 | 100 | yes: 90 committed, 100 in progress for 101 | no: deleted by committed 100 |
| (`S01`, age 55) | 100 | 0 | no: 100 in progress for 101 | yes |

Both readers proceed without waiting, each seeing a consistent state. Old versions that no snapshot can see any more are removed by `VACUUM` (run automatically by autovacuum). Transaction identifiers are 32-bit numbers compared modulo $2^{32}$, so very old versions must be *frozen* (marked as visible to everyone) before the counter wraps around, which is another task of `VACUUM`.

InnoDB and Oracle update rows in place and keep the previous versions in *undo logs*; a reader with an older *read view* reconstructs the version it should see by applying undo records. DuckDB also updates in place and keeps undo information in memory, per transaction.

### 11.6.2. Snapshot Isolation

**Definition 11.6.1 (Snapshot Isolation)** Under **snapshot isolation** (SI), each transaction reads from a snapshot of the committed data as of its start (it sees its own writes as well) and is never blocked by writers. A transaction $T$ may commit only if no other transaction that was concurrent with $T$ (one that committed after $T$ started) has written an item that $T$ also wrote; otherwise $T$ is rolled back (*first-committer-wins*; systems that detect the conflict at the second write instead of at commit use *first-updater-wins*).

**Snapshot isolation** prevents dirty reads, nonrepeatable reads, **phantoms** (a snapshot does not change) and **lost updates** (two concurrent writes to the same row cannot both commit). It does not guarantee serializability. The characteristic anomaly is *write skew*: two concurrent transactions read an overlapping set of rows, make disjoint updates based on what they read, and both commit, producing a state that no serial order produces.

**Example 11.6.2** The laboratory requires that every tissue keep at least one control sample. Two transactions each check that there are two liver controls and then each converts a different one, `S01` and `S02`, to a treated sample. DuckDB 1.5 implements snapshot **isolation** with MVCC; on the running example:

```python
import duckdb

con = duckdb.connect()                      # in-memory database
con.execute(open("schema.sql").read())
con.execute(open("data.sql").read())

# Rule of the lab: every tissue keeps at least one control sample.
check = """SELECT count(*) FROM sample
           WHERE tissue = 'liver' AND treatment = 'control'"""
t1, t2 = con.cursor(), con.cursor()        # two connections, two transactions
t1.execute("BEGIN TRANSACTION")
t2.execute("BEGIN TRANSACTION")
print("T1 sees", t1.execute(check).fetchone()[0], "liver controls")
print("T2 sees", t2.execute(check).fetchone()[0], "liver controls")
t1.execute("UPDATE sample SET treatment = 'treated' WHERE sample_id = 'S01'")
t2.execute("UPDATE sample SET treatment = 'treated' WHERE sample_id = 'S02'")
t1.execute("COMMIT")
t2.execute("COMMIT")
print("after both commits:", con.execute(check).fetchone()[0], "liver controls")

# Two transactions that update the same row: the second one fails.
t1.execute("BEGIN TRANSACTION")
t2.execute("BEGIN TRANSACTION")
t1.execute("UPDATE sample SET donor_age = donor_age + 1 WHERE sample_id = 'S03'")
try:
    t2.execute("UPDATE sample SET donor_age = donor_age + 1 WHERE sample_id = 'S03'")
except duckdb.Error as e:
    print(type(e).__name__ + ":", e)
    t2.execute("ROLLBACK")
t1.execute("COMMIT")
print(con.execute("SELECT donor_age FROM sample WHERE sample_id = 'S03'").fetchone())
```

```text
T1 sees 2 liver controls
T2 sees 2 liver controls
after both commits: 0 liver controls
TransactionException: TransactionContext Error: Conflict on update!
(59,)
```

Both transactions commit, because they wrote different rows, and the rule is violated: in either serial order the second transaction would have seen only one control and refrained. The second part shows the first-updater-wins rule: the concurrent increments of the same row cannot both succeed, so there is no lost update, and the age goes from 58 to 59 exactly once. Under SI, **write skew** is prevented by making the conflict explicit, for example with `SELECT ... FOR UPDATE` on the rows read (in systems that support it), by materializing the constraint as a row that both transactions update, or by running at a serializable level.

### 11.6.3. Serializable Snapshot Isolation

Fekete and others (2005) characterized the non-serializable executions under SI: every cycle in the dependency graph of such an execution contains two consecutive *rw-antidependencies* (a transaction reads a version that a concurrent transaction overwrites) between concurrent transactions, with a pivot transaction in the middle. *Serializable snapshot isolation* (SSI; Cahill, Röhm and Fekete, 2008) runs transactions under SI, tracks rw-antidependencies with non-blocking predicate locks, and **aborts** a transaction when it detects such a dangerous structure. It may abort some transactions unnecessarily but never allows a non-serializable execution, and readers still never block. PostgreSQL implements its `SERIALIZABLE` level this way since version 9.1; in Example 11.6.2 one of the two transactions would fail with the error "could not serialize access due to read/write dependencies among transactions", and the application would retry it. CockroachDB also runs serializable transactions by default.

## 11.7. Anomalies and SQL Isolation Levels

### 11.7.1. The Anomalies

| Anomaly | What happens | Example |
|---|---|---|
| Dirty read | a transaction reads data written by an uncommitted transaction | $W_1(A), R_2(A), A_1$ |
| Nonrepeatable read | a transaction reads a row twice and gets different values, because another transaction updated it and committed in between | $R_1(A), W_2(A), C_2, R_1(A)$ |
| Phantom | a transaction evaluates a condition twice and gets different sets of rows, because another transaction inserted or deleted matching rows | §11.3 |
| Lost update | two transactions read the same row and both write it based on what they read; one update is lost | [4.13.10](/4.13.10#sec-10.2.1) |
| Write skew | two transactions read overlapping data and write disjoint rows, violating a constraint over both | Example 11.6.2 |
| Serialization anomaly | any result that no serial order of the transactions can produce | all of the above |

### 11.7.2. Isolation Levels in the Standard and in PostgreSQL

The **SQL** standard defines four **isolation** levels by the anomalies they prohibit, set with `SET TRANSACTION ISOLATION LEVEL` or `BEGIN ISOLATION LEVEL ...` ([4.13.4](/4.13.4#sec-4.7)). The standard requires only that `SERIALIZABLE` be serializable; Berenson and others ("A Critique of ANSI SQL Isolation Levels", 1995) showed that the anomaly-based definitions are ambiguous and that **snapshot isolation** falls between the standard's levels. The table gives the standard's definition and PostgreSQL's behaviour, following its documentation.

| Level | Dirty read | Nonrepeatable read | Phantom | Serialization anomaly | PostgreSQL implementation |
|---|---|---|---|---|---|
| `READ UNCOMMITTED` | possible (not in PostgreSQL) | possible | possible | possible | same as `READ COMMITTED` |
| `READ COMMITTED` | not possible | possible | possible | possible | MVCC with a new snapshot for every statement; the default |
| `REPEATABLE READ` | not possible | not possible | possible (not in PostgreSQL) | possible | snapshot isolation: one snapshot per transaction; a concurrent update of a row it wants to modify aborts it ("could not serialize access due to concurrent update") |
| `SERIALIZABLE` | not possible | not possible | not possible | not possible | serializable snapshot isolation (§11.6.3) |

In PostgreSQL's `READ COMMITTED`, an `UPDATE` that finds its target row being updated by a concurrent **transaction** waits for it to finish and then re-evaluates its condition on the new version; a read-modify-write sequence of separate statements can still lose updates, which is why `UPDATE sample SET donor_age = donor_age + 1` in one statement, or `SELECT ... FOR UPDATE`, is the safe idiom.

### 11.7.3. Other Systems

| System | Default level | Implementation |
|---|---|---|
| MySQL InnoDB | `REPEATABLE READ` | consistent (non-locking) reads from a read view created at the first read; locking reads and updates use next-key locks on the current version, so a read-modify-write can still lose an update unless the read is `FOR UPDATE`; `SERIALIZABLE` turns plain reads into locking reads |
| Oracle | `READ COMMITTED` | MVCC with undo; its `SERIALIZABLE` level is snapshot isolation |
| SQL Server | `READ COMMITTED` (locking) | 2PL-based levels; `READ_COMMITTED_SNAPSHOT` and `SNAPSHOT` add MVCC |
| SQLite | serializable | one writer at a time for the whole database; in WAL mode readers use a snapshot and do not block the writer |
| DuckDB | snapshot isolation | optimistic MVCC; concurrent updates of the same row fail at the second write (Example 11.6.2) |

SQLite's coarse approach shows that **serializability** can be cheap when there is only one writer at a time. The following program opens three connections to a **database** in **WAL** mode: a reader that starts a transaction and reads, a writer that updates the same row and commits, and a second writer that is refused immediately (`timeout=0`; by default SQLite would retry for 5 seconds).

```python
import os, sqlite3

DB = "snap.db"
for f in os.listdir("."):
    if f.startswith(DB):
        os.remove(f)
setup = sqlite3.connect(DB)
setup.executescript(open("../schema.sql").read() + open("../data.sql").read())
setup.execute("PRAGMA journal_mode = WAL")
setup.close()

reader = sqlite3.connect(DB, isolation_level=None)
writer = sqlite3.connect(DB, isolation_level=None)
other = sqlite3.connect(DB, isolation_level=None, timeout=0)   # do not wait
age = "SELECT donor_age FROM sample WHERE sample_id = 'S01'"

reader.execute("BEGIN")
print("reader, first read: ", reader.execute(age).fetchone()[0])   # snapshot starts
writer.execute("BEGIN IMMEDIATE")                                  # takes the write lock
writer.execute("UPDATE sample SET donor_age = 55 WHERE sample_id = 'S01'")
try:
    other.execute("BEGIN IMMEDIATE")                               # a second writer
except sqlite3.OperationalError as e:
    print("second writer:      ", e)
writer.execute("COMMIT")
print("reader, second read:", reader.execute(age).fetchone()[0])   # same snapshot
reader.execute("COMMIT")
print("reader, new txn:    ", reader.execute(age).fetchone()[0])
```

```text
reader, first read:  54
second writer:       database is locked
reader, second read: 54
reader, new txn:     55
```

The reader keeps its **snapshot** across the writer's **commit** and sees the new value only in its next transaction; the second writer gets `SQLITE_BUSY` ("database is locked"). Applications that use SQLite with several writing **threads** or processes should start write transactions with `BEGIN IMMEDIATE` and set a busy timeout, and long-running analytical workloads with many concurrent writers belong in a client–server system.

### 11.7.4. Choosing a Level

Serializability is the only level at which the correctness argument "each transaction is correct when run alone" carries over to concurrent execution. Weaker levels are faster or block less, but every application invariant that spans several rows must then be checked by hand against the anomalies the level permits. A reasonable practice is to use `SERIALIZABLE` (in PostgreSQL, SSI) for transactions that maintain such invariants, to write the application so that it retries transactions that fail with a serialization error (SQLSTATE `40001`) or a **deadlock** (`40P01` in PostgreSQL), and to use `READ COMMITTED` with single-statement updates or explicit row locks where performance requires it.

## Summary

- Locks in S and X modes, managed in a **lock table**, protect data items between **transactions**; latches protect in-memory structures between **threads**.
- Two-phase locking guarantees conflict serializability, with the lock points giving the serial order; strict 2PL also gives strict schedules, and rigorous 2PL makes the commit order the serial order.
- Deadlocks are cycles in the wait-for graph; they are detected and broken by aborting a victim, or prevented by wait-die and wound-wait using timestamps.
- Phantoms require locking predicates, approximated by index and next-key locking. Intention locks (IS, IX, SIX) let transactions lock tables, pages and rows consistently.
- Timestamp ordering serializes transactions in timestamp order without waiting; optimistic protocols validate at commit.
- MVCC lets readers use snapshots without blocking writers. Snapshot isolation prevents dirty reads, nonrepeatable reads, phantoms and lost updates but allows write skew; serializable snapshot isolation (PostgreSQL's `SERIALIZABLE`) detects and aborts the dangerous patterns.
- PostgreSQL's `READ COMMITTED` takes a snapshot per statement and `REPEATABLE READ` one per transaction; MySQL defaults to `REPEATABLE READ` with next-key locking, SQLite serializes writers, and DuckDB uses optimistic snapshot isolation.
