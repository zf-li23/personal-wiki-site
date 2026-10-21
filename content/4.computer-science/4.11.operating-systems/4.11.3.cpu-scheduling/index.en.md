---
title: CPU Scheduling
description: "Scheduling metrics (turnaround, response time, fairness); FIFO, SJF and STCF with worked examples and the optimality of SJF; round robin and the time slice; the multi-level feedback queue; proportional share by lottery and stride scheduling; Linux's CFS and EEVDF schedulers, nice values and weights, real-time policies and sched_ext; multiprocessor scheduling, affinity and load balancing."
---

The mechanism of [4.11.2](/4.11.2), **limited direct execution** with the timer interrupt and the **context switch**, lets the kernel switch between processes. It does not say which process should run next, for how long, or on which processor. Those are the questions of the scheduling *policy*, and the answers depend on what we want: short completion times for batch jobs, quick responses for interactive programs, a fair division of the machine among users, or guarantees for tasks with deadlines. This chapter develops the classical policies from a sequence of simplifying assumptions, following the presentation of OSTEP, with computed timelines for each; then it turns to the proportional-share idea on which Linux's schedulers, CFS and its 2023 successor EEVDF, are based, and finally to scheduling on many processors. The data structures used by schedulers (queues, **priority queues**, **red-black trees**) are those of [4.3](/4.3); the parallel speed-up that multiprocessor scheduling makes possible is bounded by **Amdahl's law** ([4.4.7](/4.4.7)).

## 3.1. Workloads and Metrics

### 3.1.1. Jobs

We call the units of work that the scheduler manages *jobs* (**processes** or threads). To develop the first policies we make assumptions that we drop one by one:

1. Each job runs for the same amount of time.
2. All jobs arrive at the same time.
3. Once started, each job runs to completion.
4. Jobs use only the CPU (no I/O).
5. The run time of each job is known.

The last assumption is the most unrealistic: a general-purpose kernel does not know how long a process will run. It is useful anyway, because the policies that assume it are optimal and set the standard that practical policies try to approximate.

### 3.1.2. Metrics

**Definition 3.1.1 (Turnaround Time and Response Time)** For a job that arrives at time $T_{\mathrm{arrival}}$, first runs at time $T_{\mathrm{first}}$ and completes at time $T_{\mathrm{completion}}$, the **turnaround time** is $T_{\mathrm{turnaround}} = T_{\mathrm{completion}} - T_{\mathrm{arrival}}$, and the **response time** is $T_{\mathrm{response}} = T_{\mathrm{first}} - T_{\mathrm{arrival}}$.

Turnaround time measures how long a batch user waits for results; response time measures how long an interactive user waits before something happens. (In [4.10.1](/4.10.1) "response time" means the whole execution time of a task; in scheduling the term has the narrower meaning above.) Other criteria are **throughput** (jobs completed per unit of time, [4.10.1](/4.10.1)), *fairness* (whether each job receives its share; a job that waits indefinitely suffers *starvation*), *overhead* (the time spent in the scheduler and in **context switches**) and, for real-time tasks, meeting deadlines. The criteria conflict: we will see that the policy that is best for turnaround is bad for response time and vice versa.

## 3.2. FIFO, SJF and STCF

### 3.2.1. First In, First Out

**Definition 3.2.1 (FIFO Scheduling)** **First-in, first-out** (FIFO, also first-come, first-served) scheduling runs jobs in the order of their arrival, each to completion.

FIFO is simple and works well when the jobs are similar (assumption 1). It fails when they are not.

**Example 3.2.1** Jobs A, B and C arrive at time 0, in that order, with run times 100, 10 and 10. FIFO runs A during $[0, 100)$, B during $[100, 110)$ and C during $[110, 120)$. The turnaround times are 100, 110 and 120, with mean 110. The two short jobs wait behind the long one; this is the *convoy effect*, familiar from a supermarket queue behind a full trolley.

### 3.2.2. Shortest Job First

**Definition 3.2.2 (SJF Scheduling)** **Shortest job first** (SJF) scheduling runs, whenever a job finishes, the waiting job with the shortest run time, to completion.

In Example 3.2.1, SJF runs B, C, A: turnaround times 10, 20, 120, mean 50 instead of 110.

**Theorem 3.2.1 (Optimality of SJF)** If all jobs arrive at the same time and run to completion on one processor, SJF minimizes the mean turnaround time.

**Proof** Let the jobs run in some order with run times $L_1, L_2, \dots, L_n$. The $k$-th job completes at $L_1 + \cdots + L_k$, so the sum of the turnaround times is

$$
\sum_{k=1}^{n} \sum_{j=1}^{k} L_j = \sum_{j=1}^{n} (n - j + 1)\, L_j .
$$

The run time of the $j$-th job is counted $n - j + 1$ times, once for itself and once for each job after it. If some adjacent pair is out of order, $L_j > L_{j+1}$, swapping the two jobs changes the sum by $(n - j + 1) L_{j+1} + (n - j) L_j - (n - j + 1) L_j - (n - j) L_{j+1} = L_{j+1} - L_j < 0$. So an order with a smaller-before-larger violation is never optimal, and the sorted order, SJF, is optimal. $\square$

### 3.2.3. Shortest Time-to-Completion First

When jobs arrive at different times (dropping assumption 2), SJF can still be bad.

**Example 3.2.2** A (run time 100) arrives at time 0, B and C (run time 10 each) at time 10. When they arrive, A is already running, and non-preemptive SJF must let it finish: B and C complete at 110 and 120, and the mean turnaround is $(100 + 100 + 110)/3 = 103.3$.

**Definition 3.2.3 (STCF Scheduling)** **Shortest time-to-completion first** (STCF, also shortest remaining time first, SRTF) is the preemptive version of SJF: whenever a new job arrives, the scheduler compares the remaining run times of all jobs, including the running one, and runs the job with the least time remaining.

In Example 3.2.2, STCF preempts A at time 10, runs B during $[10, 20)$, C during $[20, 30)$ and A until 120. The turnaround times are 120, 10 and 20, mean 50. STCF is optimal for mean turnaround time when jobs arrive at arbitrary times (a classical result of Schrage, 1968; the proof is an exchange argument like that of Theorem 3.2.1, applied to units of work).

![Timelines of the worked examples of §3.2 and §3.3](./plots/scheduling-timelines.py)

## 3.3. Round Robin

### 3.3.1. Response Time and the Time Slice

With interactive users the response time matters. STCF is poor here: in Example 3.2.1, C waits 10 time units before it starts, and with more jobs the last one waits for all the others.

**Definition 3.3.1 (Round-Robin Scheduling)** **Round-robin scheduling** (RR) runs each ready job for at most one *time slice* (a *quantum*), then preempts it, puts it at the end of the ready queue, and runs the job at the head of the queue.

**Example 3.3.1** A, B and C arrive at time 0, each with run time 5. SJF (here the same as FIFO) runs them one after another: response times 0, 5, 10 (mean 5), turnaround times 5, 10, 15 (mean 10). RR with a time slice of 1 runs A, B, C, A, B, C, …: response times 0, 1, 2 (mean 1), but A completes only at 13, B at 14, C at 15, so the mean turnaround is 14, worse than SJF and close to the worst possible.

The examples can be checked with a small simulator:

```python
from collections import deque

def simulate(jobs, policy, quantum=1):
    """jobs: list of (name, arrival, length). Returns the schedule as
    (name, start, end) slices and per-job (turnaround, response)."""
    remaining = {n: L for n, a, L in jobs}
    arrival = {n: a for n, a, L in jobs}
    order = {n: i for i, (n, a, L) in enumerate(jobs)}   # tie-break: list order
    t, slices, first, done = 0, [], {}, {}
    queue = deque()                                     # ready queue
    pending = sorted(jobs, key=lambda j: (j[1], order[j[0]]))
    while len(done) < len(jobs):
        while pending and pending[0][1] <= t:           # admit arrivals
            queue.append(pending.pop(0)[0])
        if not queue:                                   # idle until next arrival
            t = pending[0][1]
            continue
        if policy == "FIFO":
            job, run = queue[0], remaining[queue[0]]
        elif policy == "SJF":                           # non-preemptive
            job = min(queue, key=lambda n: (remaining[n], order[n]))
            run = remaining[job]
        elif policy == "STCF":                          # preempt at the next arrival
            job = min(queue, key=lambda n: (remaining[n], order[n]))
            nxt = pending[0][1] - t if pending else remaining[job]
            run = min(remaining[job], nxt)
        elif policy == "RR":
            job, run = queue[0], min(quantum, remaining[queue[0]])
        first.setdefault(job, t)
        queue.remove(job)
        if slices and slices[-1][0] == job and slices[-1][2] == t:
            slices[-1] = (job, slices[-1][1], t + run)  # merge adjacent slices
        else:
            slices.append((job, t, t + run))
        t += run
        remaining[job] -= run
        while pending and pending[0][1] <= t:           # arrivals during the slice
            queue.append(pending.pop(0)[0])
        if remaining[job] == 0:
            done[job] = t
        elif policy == "RR":
            queue.append(job)                           # back of the queue
        else:
            queue.appendleft(job)
    stats = {n: (done[n] - arrival[n], first[n] - arrival[n]) for n, a, L in jobs}
    return slices, stats

def report(title, jobs, policy, **kw):
    slices, stats = simulate(jobs, policy, **kw)
    tat = sum(s[0] for s in stats.values()) / len(stats)
    resp = sum(s[1] for s in stats.values()) / len(stats)
    timeline = " ".join(f"{n}[{a},{b})" for n, a, b in slices)
    print(f"{title:11s} {timeline}")
    print(f"{'':11s} mean turnaround {tat:6.2f}, mean response {resp:6.2f}")

ex1 = [("A", 0, 100), ("B", 0, 10), ("C", 0, 10)]
ex2 = [("A", 0, 100), ("B", 10, 10), ("C", 10, 10)]
ex3 = [("A", 0, 5), ("B", 0, 5), ("C", 0, 5)]
report("FIFO ex1", ex1, "FIFO")
report("SJF ex1", ex1, "SJF")
report("SJF ex2", ex2, "SJF")
report("STCF ex2", ex2, "STCF")
report("SJF ex3", ex3, "SJF")
report("RR(1) ex3", ex3, "RR", quantum=1)
```

```text
FIFO ex1    A[0,100) B[100,110) C[110,120)
            mean turnaround 110.00, mean response  70.00
SJF ex1     B[0,10) C[10,20) A[20,120)
            mean turnaround  50.00, mean response  10.00
SJF ex2     A[0,100) B[100,110) C[110,120)
            mean turnaround 103.33, mean response  63.33
STCF ex2    A[0,10) B[10,20) C[20,30) A[30,120)
            mean turnaround  50.00, mean response   3.33
SJF ex3     A[0,5) B[5,10) C[10,15)
            mean turnaround  10.00, mean response   5.00
RR(1) ex3   A[0,1) B[1,2) C[2,3) A[3,4) B[4,5) C[5,6) A[6,7) B[7,8) C[8,9) A[9,10) B[10,11) C[11,12) A[12,13) B[13,14) C[14,15)
            mean turnaround  14.00, mean response   1.00
```

The trade-off is fundamental: any policy that is fair, dividing the processor evenly over short intervals, delays the completion of every job, and a policy that minimizes turnaround is unfair to long jobs.

The length of the time slice is a second trade-off. A shorter slice improves response time, but every switch costs time, directly and through cold caches ([4.11.2](/4.11.2#sec-2.3.3)). If a switch costs $c$ and the slice is $q$, the fraction of processor time lost is $c / (q + c)$: with $c = 1\,\mathrm{ms}$ and $q = 10\,\mathrm{ms}$ about 9 %, with $q = 100\,\mathrm{ms}$ about 1 %. The cost is *amortized* over the slice. Real kernels use slices of a few milliseconds; the cost of a switch is then well below 1 % even including cache effects.

### 3.3.2. Incorporating I/O

Dropping assumption 4: a job that starts an I/O operation blocks, and the scheduler should run another job meanwhile. A scheduler that treats each CPU burst between two I/O operations as a separate short job (as STCF would) naturally favors interactive jobs: a text editor that computes for 1 ms after every keystroke gets the processor immediately, while a long computation uses the time in between. This overlap of computation and I/O is the original reason for **multiprogramming** ([4.11.1](/4.11.1#sec-1.2)).

## 3.4. The Multi-Level Feedback Queue

### 3.4.1. Learning from the Past

Without assumption 5 the scheduler does not know which jobs are short. The multi-level feedback queue (MLFQ), first used in CTSS (Corbató, 1962) and in the schedulers of BSD Unix, Solaris and Windows, learns it from the past behavior of each job: a job that keeps using whole time slices is probably long and CPU-bound; a job that gives up the processor quickly is probably interactive.

**Definition 3.4.1 (Multi-Level Feedback Queue)** A **multi-level feedback queue** scheduler keeps several ready queues with different priorities and obeys the following rules:

1. If the priority of A is greater than that of B, A runs (and B does not).
2. If A and B have the same priority, they run in round robin.
3. A job that enters the system starts at the highest priority.
4. When a job has used up its *time allotment* at a priority level (however many times it gave up the processor in between), its priority is reduced by one level.
5. After a fixed period $S$, all jobs are moved to the highest priority (*priority boost*).

Rule 3 assumes every new job might be short; if it is, it finishes quickly at a high priority, and if not, rule 4 moves it down, so MLFQ approximates SJF without knowing run times.

**Example 3.4.1** Three levels, with time slices (equal to the allotments) of 10 ms at the top level Q2, 20 ms at Q1 and 40 ms at Q0. A long CPU-bound job A arrives at time 0: it runs 10 ms in Q2, 20 ms in Q1 and from time 30 on in Q0. At time 100 a short job C with 20 ms of work arrives. It enters Q2 and preempts A (rule 1), uses its 10 ms allotment and moves to Q1, where it still has priority over A and finishes at time 120. C's turnaround is 20 ms, as under SJF, although the scheduler never knew its length. An interactive job that runs for 1 ms and then waits for input uses its allotment only slowly and stays at the top level, receiving immediate response.

### 3.4.2. Why Rules 4 and 5

Earlier versions of the rules let a job keep its priority whenever it gave up the processor before its slice expired. That opened two holes. A job could *game* the scheduler by issuing a dummy I/O operation just before the end of every slice, staying at the top priority while using almost the whole processor; rule 4 closes this by charging the accumulated time at each level. And CPU-bound jobs could *starve* when many interactive jobs kept the higher queues busy; moreover a job that changed from CPU-bound to interactive would never move up again. The priority boost of rule 5 solves both problems. Its period $S$ is a "voodoo constant": too long and long jobs starve, too short and interactive jobs get too little of the processor. Production MLFQ schedulers have many such parameters (Solaris's table had 60 levels with slices from 20 to a few hundred milliseconds), and some let users or administrators advise the scheduler, as the Unix command `nice` does.

## 3.5. Proportional Share

### 3.5.1. Lottery Scheduling

A different goal is to guarantee each job a certain *fraction* of the processor, instead of optimizing turnaround or response time.

**Definition 3.5.1 (Lottery Scheduling)** In **lottery scheduling** (Waldspurger and Weihl, 1994) each job holds a number of *tickets*. At every scheduling decision the scheduler draws a ticket uniformly at random and runs the job holding it; a job with $t_i$ of the $T$ tickets therefore runs with probability $t_i / T$ in each time slice.

Randomness makes the scheduler simple and stateless, and it adapts immediately when jobs arrive or leave. Its weakness is short-term unfairness: over $n$ slices the number won by a job with share $p = t_i/T$ follows the **binomial distribution** $\mathrm{Bin}(n, p)$, whose relative standard deviation $\sqrt{(1 - p)/(np)}$ decreases only like $1/\sqrt{n}$. Two equal jobs with 100 slices each finish, on average, noticeably apart; the proportions are exact only in the long run (by the **law of large numbers**).

### 3.5.2. Stride Scheduling

**Definition 3.5.2 (Stride Scheduling)** In **stride scheduling** each job $i$ has a *stride* $s_i = K / t_i$, inversely proportional to its tickets $t_i$ ($K$ a large constant), and a *pass* value, initially 0. The scheduler always runs the job with the smallest pass value and, after its slice, increases that job's pass by its stride.

**Example 3.5.1** Jobs A, B and C hold 100, 50 and 250 tickets; with $K = 10000$ the strides are 100, 200 and 40. Breaking ties alphabetically:

| pass A | pass B | pass C | runs |
|---|---|---|---|
| 0 | 0 | 0 | A |
| 100 | 0 | 0 | B |
| 100 | 200 | 0 | C |
| 100 | 200 | 40 | C |
| 100 | 200 | 80 | C |
| 100 | 200 | 120 | A |
| 200 | 200 | 120 | C |
| 200 | 200 | 160 | C |
| 200 | 200 | 200 | A |

After 8 slices all pass values are equal again (200): C ran 5 times, A twice, B once, exactly the ratio $250 : 100 : 50$. Stride scheduling is deterministic and exact over every such cycle. Its drawback is global state: a job that arrives later must be given a sensible pass value (if it started at 0 it would monopolize the processor), whereas a lottery needs no such care.

### 3.5.3. The Completely Fair Scheduler

The proportional-share idea, in the deterministic form of stride scheduling, is the basis of Linux's scheduling of ordinary processes. The *Completely Fair Scheduler* (CFS), written by Ingo Molnár, was the Linux scheduler from version 2.6.23 (2007) to 6.5.

CFS keeps for each task its *virtual runtime* `vruntime`, the time it has run scaled by its weight, and always runs the task with the smallest virtual runtime: the task that has received the least of its fair share so far. The tasks are kept in a **red-black tree** ordered by virtual runtime, so the next task (the leftmost node) is found in $O(1)$ with a cached pointer, and inserting a task back costs $O(\log n)$. Weights come from the *nice value* of a **process**, an integer from $-20$ (highest priority) to $19$ (lowest), 0 by default:

$$
w(\mathit{nice}) \approx \frac{1024}{1.25^{\mathit{nice}}}, \qquad
\Delta\mathit{vruntime} = \Delta t \cdot \frac{1024}{w} .
$$

The kernel uses a fixed table (`sched_prio_to_weight`): nice $-20$: 88761, $-5$: 3121, $-1$: 1277, 0: 1024, 1: 820, 5: 335, 10: 110, 19: 15. Each nice step changes the weight by about a factor 1.25, so that a process gains or loses about 10 % of the processor relative to a competitor; the shares depend only on the ratios of the weights. A process with nice 0 competing with one at nice 5 should receive $1024 / (1024 + 335) = 75.3\,\%$ of one CPU. A measurement with two CPU-bound loops pinned to the same CPU for 3 s confirms it:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Count loop iterations for a fixed wall-clock time. */
int main(int argc, char **argv) {
    double seconds = argc > 1 ? atof(argv[1]) : 3.0;
    struct timespec t0, t;
    clock_gettime(CLOCK_MONOTONIC, &t0);
    unsigned long n = 0;
    do {
        for (int i = 0; i < 100000; i++) __asm__ volatile ("");
        n++;
        clock_gettime(CLOCK_MONOTONIC, &t);
    } while ((t.tv_sec - t0.tv_sec) + (t.tv_nsec - t0.tv_nsec) * 1e-9 < seconds);
    printf("%s %lu\n", argc > 2 ? argv[2] : "", n);
    return 0;
}
```

```bash
taskset -c 3 ./spin 3 "nice 0:" & taskset -c 3 nice -n 5 ./spin 3 "nice 5:" & wait
```

```text
nice 0: 111282
nice 5: 37380
```

The first process did $111282 / (111282 + 37380) = 74.9\,\%$ of the work. CFS had two more ingredients. It aimed to run every runnable task once within a *target latency* (`sched_latency`, 6 ms by default, scaled with the number of CPUs), giving each a slice proportional to its weight but at least a minimum granularity. And a task waking up after sleeping was placed near the current minimum virtual runtime, rather than at its old, small value, so that a long sleeper could not monopolize the processor after waking.

### 3.5.4. EEVDF

CFS divided the processor fairly but had no notion of latency: a task that needed the processor quickly but only briefly (an audio thread, an interactive program) could not ask for it without also asking for a larger share, and the heuristics that favored waking tasks were fragile. Since Linux 6.6 (October 2023) the fair scheduling class uses Earliest Eligible Virtual Deadline First (EEVDF), an algorithm published by Stoica and Abdel-Wahab in 1995 and implemented in Linux by Peter Zijlstra. It keeps the weights and virtual runtimes of CFS and adds two notions:

**Definition 3.5.3 (EEVDF Scheduling)** Let task $i$ have weight $w_i$ and virtual runtime $v_i$, and let $V = \sum_i w_i v_i / \sum_i w_i$ be the weighted average of the virtual runtimes of the runnable tasks. The *lag* of task $i$ is $\ell_i = w_i (V - v_i)$, the service it is owed ($\ell_i > 0$) or has received in excess ($\ell_i < 0$); a task is *eligible* if $\ell_i \ge 0$. Each task requests a time slice $r_i$, and its *virtual deadline* is $d_i = v_i + r_i / w_i$. **Earliest eligible virtual deadline first** (EEVDF) scheduling always runs, among the eligible tasks, the one with the earliest virtual deadline.

Eligibility preserves fairness (no task runs ahead of its share by more than a slice), and the deadline expresses latency: a task with a short requested slice has an early deadline, so it runs sooner, but for a shorter time, and its long-run share is still determined only by its weight.

**Example 3.5.2** Tasks A and B have equal weight 1; A requests slices of 3 ms, B of 1 ms. Both start with $v = 0$. In the table, $V$ is the average virtual runtime and $d$ the virtual deadlines at each decision:

| time | $V$ | $v_A$ | $v_B$ | eligible | $d_A$ | $d_B$ | runs |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | A, B | 3 | 1 | B |
| 1 | 1/2 | 0 | 1 | A | 3 | 2 | A |
| 4 | 2 | 3 | 1 | B | 6 | 2 | B |
| 5 | 5/2 | 3 | 2 | B | 6 | 3 | B |
| 6 | 3 | 3 | 3 | A, B | 6 | 4 | B |
| 7 | 7/2 | 3 | 4 | A | 6 | 5 | A |
| 10 | 5 | 6 | 4 | B | 9 | 5 | B |
| 11 | 11/2 | 6 | 5 | B | 9 | 6 | B |

In the first 12 ms each task receives 6 ms, as their equal weights demand, but B never waits more than 3 ms while A, which asked for long slices, gets them in one piece.

In Linux the default requested slice is the *base slice* (`/sys/kernel/debug/sched/base_slice_ns`, about 3 ms on machines with 8 or more CPUs); since Linux 6.12 a task may request a different one through the `sched_setattr` system call. The lag of a task that sleeps is remembered and decays, so that a task cannot gain service by sleeping or lose it by being briefly blocked. The real implementation keeps the runnable tasks in an augmented red-black tree that finds the eligible task with the earliest deadline in $O(\log n)$.

### 3.5.5. Linux Scheduling Classes in Practice

Linux runs several *scheduling classes* in strict priority order; a task's class is set by its scheduling policy:

| Class | Policies | Behavior |
|---|---|---|
| Deadline | `SCHED_DEADLINE` | earliest deadline first with reservations (runtime, period, deadline); for periodic real-time tasks |
| Real-time | `SCHED_FIFO`, `SCHED_RR` | fixed priorities 1–99; FIFO runs until it blocks or yields, RR adds time slices among equal priorities |
| Fair | `SCHED_NORMAL` (also called `SCHED_OTHER`), `SCHED_BATCH`, `SCHED_IDLE` | EEVDF with nice weights; BATCH is never treated as interactive; IDLE gets only otherwise idle time |
| Extensible | `SCHED_EXT` | scheduling policy supplied as an eBPF program (*sched_ext*, since Linux 6.12) |

A real-time task that never blocks would starve everything else; by default the kernel reserves 5 % of each second for non-real-time tasks (`/proc/sys/kernel/sched_rt_runtime_us` = 950000 of `sched_rt_period_us` = 1000000). sched_ext lets new policies be loaded at run time without rebuilding the kernel, for experiments and for workloads such as games and large servers; if the eBPF scheduler misbehaves, the kernel falls back to the fair class.

The everyday commands:

```bash
nice -n 10 ./long_analysis.sh      # start with lower priority (nice 10)
renice -n 5 -p 12345               # change the nice value of a running process
chrt -p 12345                      # show the policy and priority of a process
ps -o pid,ni,cls,pri,comm -p 12345 # nice value and class in ps
```

Ordinary users may only increase the nice value of their processes; lowering it, or choosing a real-time policy, needs privileges. On a shared server, running a long computation with `nice -n 19` is a courtesy to the other users.

## 3.6. Multiprocessor Scheduling

### 3.6.1. Caches and Affinity

With several processors, a scheduler must also decide where each job runs. A job that has been running on one CPU has warmed that CPU's caches (and its translation buffer, [4.11.4](/4.11.4)); moved to another CPU, it must reload everything. Schedulers therefore prefer *cache affinity*: keep a job on the CPU where it ran before, unless the imbalance between CPUs becomes too large.

Two basic designs exist:

- *Single-queue multiprocessor scheduling* (SQMS) keeps one shared ready queue from which every CPU takes jobs. It balances load automatically, but the shared queue needs a lock, which becomes a bottleneck on many CPUs, and jobs migrate between CPUs freely, losing affinity.
- *Multi-queue multiprocessor scheduling* (MQMS) gives each CPU its own queue, scheduled independently. It scales and preserves affinity, but queues can become unbalanced: one CPU idle while another has three jobs. The remedy is *migration*, usually by *work stealing*: an underloaded CPU looks at the queues of others and takes jobs from a busier one.

Linux uses per-CPU run queues and balances them periodically and whenever a CPU becomes idle, within a hierarchy of *scheduling domains* that reflects the hardware: hyperthreads of one core share caches, so moving a task between them is cheap; cores of one socket share the last-level cache; moving between sockets (NUMA nodes, with their own memory) is the most expensive and is done most reluctantly. On processors with cores of different kinds (performance and efficiency cores, as in recent Intel and ARM designs), the scheduler also takes core capacity into account, with hints from the hardware.

### 3.6.2. Practical Consequences

- A program can restrict the CPUs it runs on with `taskset` or `sched_setaffinity` (used in the measurements of [4.11.2](/4.11.2#sec-2.3.3) and §3.5.3); batch systems and containers restrict them through control groups ([4.11.9](/4.11.9)).
- Parallel programs should not start more CPU-bound threads or processes than there are CPUs available to them. *Oversubscription*, for example a **process pool** of 8 workers each running a multithreaded **BLAS** with 8 threads ([4.4.7](/4.4.7)), causes constant context switches and cache thrashing, and usually runs slower than a correctly sized pool.
- Threads that cooperate closely (sharing data, waiting for each other) suffer when they are not scheduled at the same time; *gang scheduling* (co-scheduling) runs them together, which matters for parallel jobs on clusters ([4.11.11](/4.11.11)).
- The number of CPUs a process may use is reported by `nproc`, which respects affinity masks; `os.cpu_count()` in Python reports all CPUs of the machine, and `os.process_cpu_count()` (Python 3.13) those available to the process.

## Summary

- Turnaround time (completion minus arrival) and response time (first run minus arrival) are the main metrics; fairness, throughput and overhead are others. Policies good for one are bad for the other.
- FIFO suffers from the convoy effect. SJF is optimal for mean turnaround when all jobs arrive together (exchange argument), STCF in general; both need run times and starve long jobs.
- Round robin gives good response time and poor turnaround; the time slice trades responsiveness against the amortized cost of context switches.
- MLFQ learns which jobs are interactive: new jobs start at top priority, jobs that use up their allotment move down, and periodic boosts prevent starvation and gaming.
- Proportional share gives each job a fraction of the processor: randomly by lottery, deterministically by stride. CFS (2007–2023) ran the task with the smallest weighted virtual runtime; EEVDF (Linux 6.6 and later) runs the eligible task with the earliest virtual deadline, adding latency control to fairness. Nice values set the weights, about 10 % per step.
- On multiprocessors, per-CPU queues with load balancing preserve cache affinity; avoid oversubscribing CPUs and use `taskset`, `nice` and the CPU limits of the batch system.
