import heapq
from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
N_PAGES, N_REFS = 100, 10000

# Three workloads in the style of OSTEP, chapter 22.
workloads = {
    "No locality (uniform random)": rng.integers(0, N_PAGES, N_REFS),
    "80-20 (80% of references to 20% of pages)": np.where(
        rng.random(N_REFS) < 0.8, rng.integers(0, 20, N_REFS), rng.integers(20, N_PAGES, N_REFS)),
    "Looping sequential (pages 0-49 repeatedly)": np.arange(N_REFS) % 50,
}


def hits_opt(refs, frames):
    n = len(refs)
    next_use, last = [0] * n, {}
    for t in range(n - 1, -1, -1):          # index of the next reference to the same page
        next_use[t] = last.get(refs[t], n + t)
        last[refs[t]] = t
    resident, heap, hits = {}, [], 0          # max-heap on next use, lazy deletion
    for t, p in enumerate(refs):
        if p in resident:
            hits += 1
        elif len(resident) >= frames:
            while True:
                nu, q = heapq.heappop(heap)
                if resident.get(q) == -nu:
                    del resident[q]
                    break
        resident[p] = next_use[t]
        heapq.heappush(heap, (-next_use[t], p))
    return hits


def hits_lru(refs, frames):
    cache, hits = OrderedDict(), 0
    for p in refs:
        if p in cache:
            hits += 1
            cache.move_to_end(p)
        else:
            if len(cache) >= frames:
                cache.popitem(last=False)
            cache[p] = True
    return hits


def hits_fifo(refs, frames):
    cache, order, hits = set(), [], 0
    for p in refs:
        if p in cache:
            hits += 1
        else:
            if len(cache) >= frames:
                cache.discard(order.pop(0))
            cache.add(p)
            order.append(p)
    return hits


def hits_random(refs, frames):
    r = np.random.default_rng(1)
    cache, hits = [], 0
    members = set()
    for p in refs:
        if p in members:
            hits += 1
        else:
            if len(cache) >= frames:
                i = int(r.integers(len(cache)))
                members.discard(cache[i])
                cache[i] = p
            else:
                cache.append(p)
            members.add(p)
    return hits


def hits_clock(refs, frames):
    slots, ref_bit, where, hand, hits = [], [], {}, 0, 0
    for p in refs:
        if p in where:
            hits += 1
            ref_bit[where[p]] = 1
            continue
        if len(slots) < frames:
            where[p] = len(slots)
            slots.append(p)
            ref_bit.append(1)
            continue
        while ref_bit[hand]:
            ref_bit[hand] = 0
            hand = (hand + 1) % frames
        del where[slots[hand]]
        slots[hand], ref_bit[hand], where[p] = p, 1, hand
        hand = (hand + 1) % frames
    return hits


policies = {"OPT": hits_opt, "LRU": hits_lru, "Clock": hits_clock,
            "FIFO": hits_fifo, "Random": hits_random}
sizes = list(range(5, 101, 5))

fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
for ax, (title, refs) in zip(axes, workloads.items()):
    refs = refs.tolist()
    for name, fn in policies.items():
        rate = [100 * fn(refs, k) / len(refs) for k in sizes]
        ax.plot(sizes, rate, marker="o", markersize=3, label=name)
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("frames (cache size in pages)")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 101)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("hit rate (%)")
axes[0].legend(fontsize=8)
fig.tight_layout()
