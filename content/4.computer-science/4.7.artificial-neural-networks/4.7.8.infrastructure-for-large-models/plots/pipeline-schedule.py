"""Pipeline-parallel schedules on 4 stages with 8 micro-batches: GPipe (all
forward passes, then all backward passes) and 1F1B (one forward, one backward).
A backward pass takes twice as long as a forward pass. Both schedules have the
same bubble; 1F1B keeps fewer micro-batches in flight."""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

P, M, TF, TB = 4, 8, 1.0, 2.0


def orders(kind):
    result = []
    for s in range(P):
        if kind == "gpipe":
            ops = [("F", m) for m in range(M)] + [("B", m) for m in range(M)]
        else:
            warm = P - s - 1
            ops = [("F", m) for m in range(warm)]
            f, b = warm, 0
            while b < M:
                if f < M:
                    ops.append(("F", f))
                    f += 1
                ops.append(("B", b))
                b += 1
        result.append(ops)
    return result


def simulate(kind):
    order = orders(kind)
    done = {}
    free = [0.0] * P
    pos = [0] * P
    events = []
    while any(pos[s] < len(order[s]) for s in range(P)):
        progressed = False
        for s in range(P):
            if pos[s] == len(order[s]):
                continue
            op, m = order[s][pos[s]]
            if op == "F":
                deps = [("F", s - 1, m)] if s > 0 else []
            else:
                deps = [("F", s, m)] + ([("B", s + 1, m)] if s < P - 1 else [])
            if all(d in done for d in deps):
                start = max([free[s]] + [done[d] for d in deps])
                end = start + (TF if op == "F" else TB)
                done[(op, s, m)] = end
                free[s] = end
                events.append((s, op, m, start, end))
                pos[s] += 1
                progressed = True
        if not progressed:
            raise RuntimeError("deadlock")
    return events


fig, axes = plt.subplots(2, 1, figsize=(11, 5.0), sharex=True)
titles = {"gpipe": "GPipe: all forward passes, then all backward passes",
          "1f1b": "1F1B: after warm-up, alternate one forward and one backward pass"}
for ax, kind in zip(axes, ["gpipe", "1f1b"]):
    events = simulate(kind)
    total = max(e[4] for e in events)
    for s, op, m, start, end in events:
        color = "C0" if op == "F" else "C1"
        ax.barh(s, end - start, left=start, height=0.8, color=color,
                edgecolor="white", linewidth=0.8)
        ax.text((start + end) / 2, s, str(m + 1), ha="center", va="center",
                fontsize=7, color="white")
    busy = P * M * (TF + TB)
    bubble = 1 - busy / (P * total)
    ax.set_title(f"{titles[kind]}  (idle share {bubble:.0%})", fontsize=10)
    ax.set_yticks(range(P))
    ax.set_yticklabels([f"GPU {s + 1}" for s in range(P)])
    ax.invert_yaxis()
    ax.set_xlim(0, total)
axes[-1].set_xlabel("time (forward pass of one micro-batch = 1)")
fig.legend(handles=[Patch(color="C0", label="forward"), Patch(color="C1", label="backward")],
           loc="lower right", fontsize=8, ncol=2)
fig.tight_layout()
