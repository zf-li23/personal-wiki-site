import numpy as np
import matplotlib.pyplot as plt

# Expected number of probes as a function of the load factor (Knuth's formulas),
# with a simulation of linear probing on a table of M slots.
alpha = np.linspace(0.01, 0.95, 300)
theory = {
    "separate chaining": (1 + alpha / 2, 1 + alpha),   # bucket access counted as one probe
    "linear probing": ((1 + 1 / (1 - alpha)) / 2, (1 + 1 / (1 - alpha) ** 2) / 2),
    "uniform probing (double hashing)": (np.log(1 / (1 - alpha)) / alpha, 1 / (1 - alpha)),
}

rng = np.random.default_rng(0)
M = 1 << 14
table = np.zeros(M, dtype=bool)
probe_counts = []
checkpoints = np.arange(0.05, 0.951, 0.05)
sim_alpha, sim_hit, sim_miss = [], [], []
n = 0
for target in checkpoints:
    while n < target * M:
        r = int(rng.integers(M))
        c = 1
        while table[r]:
            r = (r + 1) % M
            c += 1
        table[r] = True
        probe_counts.append(c)
        n += 1
    # Unsuccessful search from slot i examines the run of full slots after i, plus one empty slot.
    run = np.zeros(M, dtype=int)
    nxt = 0
    for i in range(2 * M - 1, -1, -1):
        nxt = nxt + 1 if table[i % M] else 0
        if i < M:
            run[i] = nxt
    sim_alpha.append(n / M)
    sim_hit.append(np.mean(probe_counts))
    sim_miss.append(np.mean(run) + 1)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharex=True)
for ax, idx, title in zip(axes, (0, 1), ("successful search", "unsuccessful search")):
    for (label, curves), color in zip(theory.items(), ("C0", "C1", "C2")):
        ax.plot(alpha, curves[idx], color=color, label=label)
    ax.plot(sim_alpha, sim_hit if idx == 0 else sim_miss, "o", color="C1", ms=4,
            label="linear probing (simulated)")
    ax.set_yscale("log")
    ax.set_xlabel("load factor $\\lambda$")
    ax.set_title(title)
    ax.grid(alpha=0.3)
axes[0].set_ylabel("expected probes")
axes[1].legend(fontsize=8, loc="upper left")
fig.tight_layout()
