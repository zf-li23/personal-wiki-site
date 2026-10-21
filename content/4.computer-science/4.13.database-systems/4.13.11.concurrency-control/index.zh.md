---
title: 并发控制
source_hash: cf15e298be94
---

[4.13.10](/4.13.10) 定义了什么是正确的并发执行：一个**冲突可串行化**的、并且在实践中是严格的**调度**。但它没有说明，当**事务**到达、运行和结束都不可预测时，系统如何产生这样的调度。本章介绍做到这一点的协议。*封锁*（locking）使事务相互等待，两阶段锁是保证可串行化的经典协议，其代价是等待和死锁，系统必须检测或预防死锁。*时间戳*协议和*乐观*协议则不等待，而是事先给事务排序，或在事务结束时再检查。*多版本*并发控制保留数据的旧版本，使读者永远不必等待写者；PostgreSQL、MySQL 的 InnoDB、Oracle、DuckDB 和大多数现代系统都这样工作，它还引出*快照隔离*，一种比可串行化弱、并带有自己的异常的保证。本章最后讨论 SQL 的隔离级别及其在各个系统中的含义。操作系统的同步原语，即互斥锁、读写锁和**死锁**处理（[4.11.6](/4.11.6)），是其底层的构件；数据库协议则把事务加为保护的单位。

## 11.1. 基于锁的协议

### 11.1.1. 锁与锁管理器

**定义 11.1.1（共享锁与排他锁）** 持有数据项上的**共享锁**（S 锁）的事务可以读但不能写该数据项；持有**排他锁**（X 锁）的事务可以读也可以写。事务在访问数据项之前必须持有适当的锁。只有当所请求的模式与其他事务在该数据项上持有的锁相容时，锁请求才被授予；否则请求事务等待。

| 请求 \ 已持有 | S | X |
|---|---|---|
| S | 相容 | 冲突 |
| X | 冲突 | 冲突 |

任意多个**事务**可以同时持有一个数据项上的 **S 锁**，而 **X 锁**排斥其他所有锁：这就是 [4.11.6](/4.11.6) 的**读写锁**的语义。*锁管理器*保存一个散列表，即*锁表*，从数据项映射到记录，记录列出已授予的锁和一个等待请求的队列；一个请求只有与所有已授予的锁相容，并且（为避免写者饥饿）没有更早的请求在等待时，才被授予。持有 S 锁又想写的事务可以请求*升级*为 X。

**注 11.1.1（锁与闩锁）** **数据库系统**区分锁与*闩锁*（latch）：锁在事务之间保护**数据库**的逻辑内容，闩锁在**线程**之间保护内存中的数据结构。

| | 锁 | 闩锁 |
|---|---|---|
| 保护 | 行、表、键范围 | 缓冲池的页、锁表、B+ 树结点 |
| 持有者与时长 | 事务，通常持有到提交 | 线程，持有一个短的临界区 |
| 模式 | S、X、意向模式（§11.4） | 读、写 |
| 死锁 | 由数据库管理系统检测并解决 | 靠固定的获取顺序避免 |
| 实现 | 锁管理器中的条目 | 对象内的互斥锁或自旋锁 |

本章的并发控制协议涉及的是锁；闩锁则是操作系统那种封锁在**数据库管理系统**内部的应用（[4.13.8](/4.13.8#sec-8.2.5)）。

### 11.1.2. 为什么只靠封锁不够

只在访问数据项期间对它加锁，并不能保证**可串行化**。设 $T_1$ 把 50 个单位从 $A$ 转到 $B$，$T_2$ 打印 $A + B$，二者都在访问数据项之前刚好加锁，访问之后立即解锁：

| 步骤 | $T_1$ | $T_2$ |
|---|---|---|
| 1 | X-lock($A$)；$R_1(A)$；$W_1(A)$；unlock($A$) | |
| 2 | | S-lock($A$)；$R_2(A)$；unlock($A$) |
| 3 | | S-lock($B$)；$R_2(B)$；unlock($B$) |
| 4 | X-lock($B$)；$R_1(B)$；$W_1(B)$；unlock($B$) | |

每次访问都有锁保护，但 $T_2$ 看到的是 $A$ 的新值和 $B$ 的旧值，打印出的和少了 50。**优先图**有边 $T_1 \to T_2$（在 $A$ 上）和 $T_2 \to T_1$（在 $B$ 上）。解决办法是对锁*何时*可以释放加以约束。

## 11.2. 两阶段锁

### 11.2.1. 协议

**定义 11.2.1（两阶段锁）** 若事务的所有加锁请求都先于它的所有解锁操作，则称该事务遵循**两阶段锁**（2PL）。它的执行有一个*增长阶段*，其间获取锁而不释放任何锁；以及一个*收缩阶段*，其间释放锁而不获取任何锁。它最后一次获取锁的时刻是它的封锁点（lock point）。

**定理 11.2.1** 若一个**调度**中的每个**事务**都遵循**两阶段锁**，则该调度是冲突可串行化的；封锁点的顺序就是一个等价的串行顺序。

**证明** 设 $T_i \to T_j$ 是**优先图**的一条边：$T_i$ 对数据项 $Q$ 的某个操作先于 $T_j$ 对 $Q$ 的一个冲突操作。这两个操作需要 $Q$ 上不相容的锁，所以 $T_i$ 必须在某个时刻 $r$ 释放它在 $Q$ 上的锁，而 $T_j$ 在其后某个时刻 $a$ 获得它在 $Q$ 上的锁，$r < a$。由于 $T_i$ 遵循 2PL，它在**封锁点**之前不释放任何锁，所以 $\mathrm{LP}(T_i) \le r$；由于 $T_j$ 获取它在 $Q$ 上的锁不晚于它的封锁点，$a \le \mathrm{LP}(T_j)$。因此 $\mathrm{LP}(T_i) < \mathrm{LP}(T_j)$。每条边都从较早的封锁点指向较晚的封锁点，所以图中没有环，由定理 10.2.1，该调度是**冲突可串行化**的，按封锁点顺序排列的事务是一个等价的串行顺序。$\square$

逆命题不成立：有些冲突**可串行化调度**不能由 2PL 产生。2PL 也不能避免**级联回滚**：事务可能在它的收缩阶段、在提交之前释放 **X 锁**，另一个事务便可能读到未提交的值。

**定义 11.2.2（严格与强两阶段锁）** 在**严格两阶段锁**下，事务遵循 2PL，并且持有它所有的排他锁直到提交或中止。在**强两阶段锁**下，它持有所有的锁，无论共享还是排他，直到提交或中止。

**严格两阶段锁**产生的调度既是冲突可串行化的，又是严格的（[4.13.10](/4.13.10#sec-10.3)），所以通过前像恢复是正确的。**强两阶段锁**还使**提交**顺序成为一个等价的串行顺序，这对复制和分布式事务很方便。基于锁的系统几乎总是使用强 2PL；应用程序从不编写加锁或解锁操作，数据库管理系统在语句触及行时获取锁，并在提交时全部释放。SQL 允许事务在读取时显式地加行锁，用 `SELECT ... FOR UPDATE`（X）和 `SELECT ... FOR SHARE`（S），这是在较弱的隔离级别下避免丢失更新的标准做法（§11.7）。

### 11.2.2. 死锁

两阶段锁不能防止**死锁**：若 $T_1$ 持有 $A$ 上的 **S 锁** 并请求 $B$ 上的 X 锁，而 $T_2$ 持有 $B$ 上的 S 锁并请求 $A$ 上的 X 锁，则二者将永远等待。[4.11.6](/4.11.6#sec-6.5.2) 的四个 **Coffman 条件**都成立，而知道全部锁的**数据库管理系统**自己处理死锁。

**定义 11.2.3（等待图）** 一组事务的**等待图**在每当 $T_i$ 正在等待 $T_j$ 持有的锁时有一条边 $T_i \to T_j$。

死锁存在，当且仅当**等待图**有环。*死锁检测*检查图中是否有环，可以在每次请求必须等待时检查，也可以定期检查，并通过中止一个*牺牲者*来打破每个环，牺牲者通常是最年轻的事务或做的工作最少的事务；牺牲者的锁被释放，它的客户端收到一个错误并可以重试。PostgreSQL 在事务等待了 `deadlock_timeout`（默认 1 秒）之后才运行检查，使常见的短等待不花任何代价；InnoDB 则在每次等待时立即检查。

下面的**锁管理器**实现严格 2PL，使用先来先服务的队列，并用对等待图的**深度优先搜索**检测环来发现死锁。

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

$T_2$ 对 $A$ 的 X 锁请求必须等待 $A$ 的两个读者 $T_1$ 和 $T_3$，并封闭了环 $T_1 \to T_2 \to T_1$。中止环中最年轻的事务 $T_2$ 释放了它在 $B$ 上的 S 锁，$T_1$ 等待中的请求得到授予。$T_3$ 从未参与这次死锁。

*死锁预防*则保证环永远不会形成，它使用每个事务的开始时间戳 $\mathrm{TS}(T)$（重启的事务保留它原来的时间戳）。当 $T_i$ 请求 $T_j$ 持有的锁时：

- 等待-死亡（wait-die）：若 $T_i$ 较老（$\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$），$T_i$ 等待；否则 $T_i$ 被回滚（“死亡”）；
- 受伤-等待（wound-wait）：若 $T_i$ 较老，$T_j$ 被回滚（“受伤”）；否则 $T_i$ 等待。

**命题 11.2.1** 在**等待-死亡**和**受伤-等待**下都不会发生死锁，并且每个事务最终都会完成。

**证明** 在等待-死亡下，事务只等待比它年轻的事务，所以等待图的每条边 $T_i \to T_j$ 都满足 $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$；沿每条路径时间戳严格增大，所以没有环。在受伤-等待下，事务只等待比它老的事务，沿每条路径时间戳严格减小。由于重启的事务保留它的时间戳，它最终会成为最老的活动事务，这样的事务在等待-死亡下永远不会死亡，在受伤-等待下永远不会受伤，所以它会完成。$\square$

许多系统使用的一个简单替代办法是*锁超时*：等待太久的请求被取消（PostgreSQL 的 `lock_timeout`，MySQL 的 `innodb_lock_wait_timeout`）。

## 11.3. 幻影与谓词锁

当事务读取的是由条件定义的一组行时，只锁住它读过的行是不够的。设 $T_1$ 两次统计肝脏样本的数量，而在两次统计之间 $T_2$ 插入了一个新的肝脏样本并**提交**。$T_2$ 没有写任何被 $T_1$ 锁住的行，但 $T_1$ 的两次计数不同，并且没有任何串行顺序能解释它们：$T_1$ 与 $T_2$ 的冲突发生在 $T_1$ 第一次读取时还不存在的一行上。这样的一行是*幻影*（phantom）。

冲突发生在条件 `tissue = 'liver'` 上。*谓词锁*（predicate locking）锁住条件本身，使得插入满足被锁谓词的行时与该锁冲突；判断两个谓词是否重叠一般代价很高，系统转而锁定近似：

- *索引封锁*（index locking）：通过**索引**找到行的查询，锁住它扫描的索引叶**页**或条目，而插入必须锁住新键所在的叶条目；没有合适索引的查询锁住整张表。
- *临键锁*（next-key locking）（InnoDB）：锁定一条索引记录也锁定它之前的间隙，使得对 `tissue BETWEEN 'kidney' AND 'liver'` 的范围扫描阻塞对被扫描键范围的插入。InnoDB 在其默认的 `REPEATABLE READ` 级别下，对加锁读和更新使用临键锁。
- PostgreSQL 的可串行化级别（§11.6.3）在读过的索引页和**元组**上记录 *SIRead* 谓词锁；它们从不阻塞，只是用于检测危险的依赖模式。

## 11.4. 多粒度

为扫描一张表而锁住它的每一行，要在锁表中为每行付出一个条目；为更新一行而锁住整张表，则会阻塞所有人。因此系统锁定多种大小的数据项：**数据库**、表、**页**和行，它们组织成一棵树，锁定一个结点就隐式地锁定它的所有后代。为了快速检查表锁是否与其下的行锁冲突，**事务**在祖先结点上声明它们的意图。

**定义 11.4.1（意向锁）** 在**多粒度封锁**中，除 S 和 X 之外还有三种**意向锁**模式：*意向共享*（IS）和*意向排他*（IX），它们声明事务将以 S 模式、相应地以 X（或 S）模式锁定该结点的某个后代；以及*共享意向排他*（SIX），它以 S 模式锁定该结点并声明将在后代上加 X 锁。各模式的相容性为：

| 请求 \ 已持有 | IS | IX | S | SIX | X |
|---|---|---|---|---|---|
| IS | 是 | 是 | 是 | 是 | 否 |
| IX | 是 | 是 | 否 | 否 | 否 |
| S | 是 | 否 | 是 | 否 | 否 |
| SIX | 是 | 否 | 否 | 否 | 否 |
| X | 否 | 否 | 否 | 否 | 否 |

协议是：锁从根向下获取；结点只有在其父结点被持有 IS 或 IX 模式时才能以 S 或 IS 模式锁定，只有在其父结点被持有 IX 或 SIX 模式时才能以 X、SIX 或 IX 模式锁定；锁从叶向上释放，并且事务遵循**两阶段锁**。扫描一张表并更新其中几行的事务，在表上取 SIX，在这些行上取 X；并发地读取单行的读者在表上取 IS、在行上取 S，这与 SIX 相容。若一个事务获取了太多行锁，系统可以用一个表锁取代它们（*锁升级*（lock escalation）；SQL Server 在一个对象上约有 5,000 个锁时这样做）。

PostgreSQL 有八种表级锁模式（从每条 `SELECT` 都取的 `ACCESS SHARE`，到 `INSERT`、`UPDATE` 和 `DELETE` 取的 `ROW EXCLUSIVE`，再到 `DROP TABLE` 和大多数 `ALTER TABLE` 形式取的 `ACCESS EXCLUSIVE`），它们起**意向锁**的作用；还有四种行级模式（`FOR UPDATE`、`FOR NO KEY UPDATE`、`FOR SHARE`、`FOR KEY SHARE`）。行锁记录在行版本本身（`xmax`）中，而不在**共享锁**表中，所以 PostgreSQL 从不需要**锁升级**；代价是每个加锁的行都要一次磁盘写。

## 11.5. 基于时间戳的协议

### 11.5.1. 时间戳排序

时间戳协议不是通过等待来发现一个串行顺序，而是事先确定它：就是开始时间戳的顺序。

**定义 11.5.1（时间戳排序协议）** 每个事务 $T_i$ 在开始时获得一个唯一的时间戳 $\mathrm{TS}(T_i)$，每个数据项 $Q$ 带有 $\mathrm{W\text{-}TS}(Q)$ 和 $\mathrm{R\text{-}TS}(Q)$，分别是写过和读过它的事务的最大时间戳。**时间戳排序协议**对操作的处理如下：

1. $T_i$ 发出 $\operatorname{read}(Q)$：若 $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$，则 $T_i$ 将读到较年轻的**事务**写的值，所以它被回滚；否则执行读取，并令 $\mathrm{R\text{-}TS}(Q) := \max(\mathrm{R\text{-}TS}(Q), \mathrm{TS}(T_i))$。
2. $T_i$ 发出 $\operatorname{write}(Q)$：若 $\mathrm{TS}(T_i) < \mathrm{R\text{-}TS}(Q)$，则较年轻的事务已经读了旧值，$T_i$ 被回滚；若 $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$，则 $T_i$ 将覆盖较年轻的事务的写入，$T_i$ 被回滚；否则执行写入，并令 $\mathrm{W\text{-}TS}(Q) := \mathrm{TS}(T_i)$。

被回滚的事务以一个新的、更大的时间戳重新开始。

**命题 11.5.1** **时间戳排序协议**产生的每个**调度**都是**冲突可串行化**的，时间戳顺序就是一个等价的串行顺序，并且该协议不会死锁。

**证明** 设 $T_i$ 的操作 $o_i$ 与 $T_j$ 的操作 $o_j$ 在 $Q$ 上冲突，并且 $o_i$ 先执行。若 $o_i$ 是写，则其后 $\mathrm{W\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$，而 $o_j$（读或写）只有在 $\mathrm{TS}(T_j) > \mathrm{W\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$ 时才被执行（时间戳唯一）。若 $o_i$ 是读，则 $o_j$ 是写，$\mathrm{R\text{-}TS}(Q) \ge \mathrm{TS}(T_i)$，而 $o_j$ 只有在 $\mathrm{TS}(T_j) > \mathrm{TS}(T_i)$ 时才被执行。于是**优先图**的每条边 $T_i \to T_j$ 都有 $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$，图是无环的。没有事务会等待，所以没有**死锁**。$\square$

基本的时间戳排序可能产生不可恢复的调度，因为事务可能读到未提交的较老事务所写的值；通过推迟对未提交数据的读取或推迟**提交**，可使它可恢复。Thomas 写规则（Thomas write rule）削弱了规则 2：若 $\mathrm{TS}(T_i) < \mathrm{W\text{-}TS}(Q)$ 但 $\mathrm{TS}(T_i) \ge \mathrm{R\text{-}TS}(Q)$，则该写入已过时（按时间戳顺序没有人会读它），可被忽略而不必回滚 $T_i$。所得的调度是**视图可串行化**的，但并不总是冲突可串行化的。

### 11.5.2. 乐观并发控制

当冲突很少时，在结束时检查比加锁便宜。在*基于验证*的（乐观）并发控制中，事务分三个阶段运行：*读阶段*，其间它执行并且只写入私有副本；提交时的*验证阶段*，其间对照在它生存期内提交的事务检查它；以及*写阶段*，其间它的更改被安装。设验证时间戳 $\mathrm{TS}(T_i)$ 在验证开始时分配，则 $T_j$ 通过对每个满足 $\mathrm{TS}(T_i) < \mathrm{TS}(T_j)$ 的 $T_i$ 的检验，当且仅当 $T_i$ 在 $T_j$ 开始之前已结束，或者 $T_i$ 在 $T_j$ 开始验证之前已结束写阶段、并且 $T_i$ 写的数据项集合与 $T_j$ 读的数据项集合不相交。否则 $T_j$ 被回滚。乐观方案从不阻塞，适合以读为主的负载和内存系统（例如 SQL Server 的 Hekaton 引擎）；在竞争下它们会在被回滚的事务上浪费工作。应用层面带版本列的乐观锁（`UPDATE ... SET ..., version = version + 1 WHERE id = ? AND version = ?`，若没有行被更新则重试）把同样的想法用于 Web 应用的多个请求之间。

## 11.6. 多版本并发控制

### 11.6.1. 版本与快照

在封锁下，行的读者要等待持有它 **X 锁**的写者，而写者要等待读者。*多版本并发控制*（multiversion concurrency control），简称 MVCC，通过保留每个数据项的多个版本来消除这两种等待：写入创建新版本，读者被导向适合它的版本，不需要任何锁。代价是旧版本的存储空间及其**垃圾回收**。

在 PostgreSQL 中，每个行版本（**元组**）存储创建它的**事务**的标识符 `xmin`，以及删除或替换它的事务的标识符 `xmax`（没有则为 0）；`UPDATE` 用 `xmax` 标记旧版本并插入带 `xmin` 的新版本，二者通过 `ctid` 链接（[4.13.7](/4.13.7#sec-7.3.2)）。*快照*（snapshot）为读者记录哪些事务算作已提交：所有低于界限 `xmin` 的事务标识符，没有一个高于或等于界限 `xmax` 的，而在二者之间的，则是不在取快照时进行中的事务列表里的那些。若创建某版本的事务在快照中已提交，并且删除它的事务（若有）在快照中未提交，则该版本在快照中*可见*。已提交的状态来自**提交**日志 `pg_xact`。

**例 11.6.1** 事务 100 把样本 `S01` 的年龄从 54 更新为 55 并提交；事务 101 在 100 仍在运行时取了它的**快照**（100 在它的进行中列表里），事务 102 在提交之后才开始。

| 版本 | `xmin` | `xmax` | 对 101 可见 | 对 102 可见 |
|---|---|---|---|---|
| （`S01`，年龄 54） | 90 | 100 | 是：90 已提交，对 101 而言 100 在进行中 | 否：被已提交的 100 删除 |
| （`S01`，年龄 55） | 100 | 0 | 否：对 101 而言 100 在进行中 | 是 |

两个读者都不等待地继续，各自看到一致的状态。没有任何快照还能看到的旧版本由 `VACUUM`（由 autovacuum 自动运行）清除。事务标识符是 32 位数，按模 $2^{32}$ 比较，所以非常老的版本必须在计数器回绕之前被*冻结*（标记为对所有人可见），这是 `VACUUM` 的另一项任务。

InnoDB 和 Oracle 就地更新行，并把之前的版本保存在*撤销日志*中；持有较旧*读视图*的读者通过应用撤销记录重建它应当看到的版本。DuckDB 同样就地更新，并按事务在内存中保存撤销信息。

### 11.6.2. 快照隔离

**定义 11.6.1（快照隔离）** 在**快照隔离**（SI）下，每个事务从它开始时已提交数据的快照中读取（它也能看到自己的写入），并且从不被写者阻塞。只有当与事务 $T$ 并发的任何其他事务（在 $T$ 开始之后提交的事务）都没有写过 $T$ 也写过的数据项时，$T$ 才可以提交；否则 $T$ 被回滚（*先提交者获胜*，first-committer-wins；在第二次写入而不是提交时检测冲突的系统使用*先更新者获胜*，first-updater-wins）。

**快照隔离**防止脏读、不可重复读、**幻影**（快照不变）和**丢失更新**（对同一行的两次并发写入不能都提交）。它不保证可串行化。其特有的异常是*写偏斜*（write skew）：两个并发事务读取重叠的一组行，根据读到的内容做不相交的更新，并且都提交，产生了没有任何串行顺序能产生的状态。

**例 11.6.2** 实验室要求每种组织至少保留一个对照样本。两个事务各自检查有两个肝脏对照样本，然后各自把其中不同的一个，`S01` 和 `S02`，改为处理样本。DuckDB 1.5 用 MVCC 提供快照隔离级别的**隔离性**；在运行示例上：

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

两个事务都提交了，因为它们写的是不同的行，而规则被违反了：在任一串行顺序下，第二个事务都只会看到一个对照样本并且不做更改。第二部分显示了先更新者获胜规则：对同一行的并发递增不能都成功，所以没有丢失更新，年龄恰好从 58 变为 59 一次。在 SI 下，**写偏斜**可以通过使冲突显式化来防止，例如对所读的行使用 `SELECT ... FOR UPDATE`（在支持它的系统中），把约束物化为一个两个事务都更新的行，或者在可串行化级别下运行。

### 11.6.3. 可串行化快照隔离

Fekete 等人（2005）刻画了 SI 下的不可串行化执行：这类执行的依赖图中，每个环都含有并发事务之间两条相邻的 *rw 反依赖*（一个事务读取的版本被并发事务覆盖），中间有一个枢轴事务。可串行化快照隔离（serializable snapshot isolation）（SSI；Cahill、Röhm 与 Fekete，2008）让事务在 SI 下运行，用非阻塞的谓词锁跟踪 rw 反依赖，并在检测到这样的危险结构时**中止**一个事务。它可能不必要地中止一些事务，但绝不允许不可串行化的执行，而且读者仍然从不阻塞。PostgreSQL 自 9.1 版起用这种方式实现它的 `SERIALIZABLE` 级别；在例 11.6.2 中，两个事务之一会以错误 “could not serialize access due to read/write dependencies among transactions” 失败，应用程序随后重试它。CockroachDB 也默认运行可串行化事务。

## 11.7. 异常与 SQL 隔离级别

### 11.7.1. 各种异常

| 异常 | 发生什么 | 例子 |
|---|---|---|
| 脏读 | 事务读取未提交事务写的数据 | $W_1(A), R_2(A), A_1$ |
| 不可重复读 | 事务两次读取同一行得到不同的值，因为另一个事务在其间更新并提交了它 | $R_1(A), W_2(A), C_2, R_1(A)$ |
| 幻影 | 事务两次计算同一条件得到不同的行集，因为另一个事务插入或删除了匹配的行 | §11.3 |
| 丢失更新 | 两个事务读取同一行，并都根据读到的内容写它；一个更新丢失 | [4.13.10](/4.13.10#sec-10.2.1) |
| 写偏斜 | 两个事务读取重叠的数据，写入不相交的行，违反了涉及二者的约束 | 例 11.6.2 |
| 串行化异常 | 任何不能由这些事务的某个串行顺序产生的结果 | 以上全部 |

### 11.7.2. 标准与 PostgreSQL 中的隔离级别

**SQL** 标准按各级别所禁止的异常定义四个**隔离性**级别，用 `SET TRANSACTION ISOLATION LEVEL` 或 `BEGIN ISOLATION LEVEL ...` 设置（[4.13.4](/4.13.4#sec-4.7)）。标准只要求 `SERIALIZABLE` 是可串行化的；Berenson 等人（《A Critique of ANSI SQL Isolation Levels》，1995）表明，基于异常的定义含糊不清，并且**快照隔离**介于标准的各个级别之间。下表给出标准的定义和 PostgreSQL 的行为，依据它的文档。

| 级别 | 脏读 | 不可重复读 | 幻影 | 串行化异常 | PostgreSQL 的实现 |
|---|---|---|---|---|---|
| `READ UNCOMMITTED` | 可能（PostgreSQL 中不会） | 可能 | 可能 | 可能 | 与 `READ COMMITTED` 相同 |
| `READ COMMITTED` | 不可能 | 可能 | 可能 | 可能 | MVCC，每条语句取一个新快照；默认级别 |
| `REPEATABLE READ` | 不可能 | 不可能 | 可能（PostgreSQL 中不会） | 可能 | 快照隔离：每个事务一个快照；若它想修改的行被并发更新，它就被中止（“could not serialize access due to concurrent update”） |
| `SERIALIZABLE` | 不可能 | 不可能 | 不可能 | 不可能 | 可串行化快照隔离（§11.6.3） |

在 PostgreSQL 的 `READ COMMITTED` 下，`UPDATE` 发现其目标行正被并发**事务**更新时，会等待它结束，然后在新版本上重新计算它的条件；由多条独立语句组成的读-改-写序列仍然可能丢失更新，所以单条语句的 `UPDATE sample SET donor_age = donor_age + 1` 或者 `SELECT ... FOR UPDATE` 才是安全的惯用法。

### 11.7.3. 其他系统

| 系统 | 默认级别 | 实现 |
|---|---|---|
| MySQL InnoDB | `REPEATABLE READ` | 从第一次读取时创建的读视图进行一致性（非加锁）读；加锁读和更新对当前版本使用临键锁，所以读-改-写仍可能丢失更新，除非该读取带有 `FOR UPDATE`；`SERIALIZABLE` 把普通读变成加锁读 |
| Oracle | `READ COMMITTED` | 带撤销的 MVCC；它的 `SERIALIZABLE` 级别是快照隔离 |
| SQL Server | `READ COMMITTED`（加锁） | 基于 2PL 的级别；`READ_COMMITTED_SNAPSHOT` 和 `SNAPSHOT` 增加 MVCC |
| SQLite | 可串行化 | 整个数据库同一时刻只有一个写者；在 WAL 模式下读者使用快照，不阻塞写者 |
| DuckDB | 快照隔离 | 乐观 MVCC；对同一行的并发更新在第二次写入时失败（例 11.6.2） |

SQLite 的粗粒度做法表明，当同一时刻只有一个写者时，**可串行化**可以很便宜。下面的程序对一个 **WAL** 模式的**数据库**打开三个连接：一个读者开始事务并读取，一个写者更新同一行并提交，第二个写者被立即拒绝（`timeout=0`；默认情况下 SQLite 会重试 5 秒）。

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

读者在写者**提交**之后仍保持它的**快照**，只在下一个事务中才看到新值；第二个写者得到 `SQLITE_BUSY`（“database is locked”）。在多个写线程或写进程下使用 SQLite 的应用程序，应当用 `BEGIN IMMEDIATE` 开始写事务并设置忙等待超时，而有大量并发写者的长时间分析型负载则属于客户端–服务器系统。

### 11.7.4. 选择级别

可串行化是唯一使“每个事务单独运行时是正确的”这一论证可以延伸到并发执行的级别。较弱的级别更快或阻塞更少，但这时每个跨越多行的应用不变式都必须针对该级别所允许的异常人工检查。一个合理的做法是：对维护这类不变式的事务使用 `SERIALIZABLE`（在 PostgreSQL 中即 SSI），编写应用程序时让它重试因串行化错误（SQLSTATE `40001`）或**死锁**（PostgreSQL 中为 `40P01`）而失败的事务，并在性能需要的地方使用带单语句更新或显式行锁的 `READ COMMITTED`。

## 小结

- S 和 X 模式的锁由**锁表**管理，在**事务**之间保护数据项；闩锁在**线程**之间保护内存中的结构。
- 两阶段锁保证冲突可串行化，由封锁点给出串行顺序；严格 2PL 还给出严格调度，强 2PL 使提交顺序成为串行顺序。
- 死锁是等待图中的环；检测到后通过中止牺牲者打破，或者利用时间戳用等待-死亡和受伤-等待预防。
- 幻影要求锁定谓词，用索引封锁和临键锁近似。意向锁（IS、IX、SIX）使事务能对表、页和行一致地加锁。
- 时间戳排序不等待地按时间戳顺序使事务串行化；乐观协议在提交时验证。
- MVCC 使读者使用快照而不阻塞写者。快照隔离防止脏读、不可重复读、幻影和丢失更新，但允许写偏斜；可串行化快照隔离（PostgreSQL 的 `SERIALIZABLE`）检测并中止危险的模式。
- PostgreSQL 的 `READ COMMITTED` 每条语句取一个快照，`REPEATABLE READ` 每个事务取一个；MySQL 默认 `REPEATABLE READ` 并带临键锁，SQLite 把写者串行化，DuckDB 使用乐观快照隔离。
