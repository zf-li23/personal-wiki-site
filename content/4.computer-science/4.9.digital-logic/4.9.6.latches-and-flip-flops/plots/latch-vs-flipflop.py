import matplotlib.pyplot as plt

T_END = 17.0
RISE = 0.12
DELAY = 0.25  # drawn propagation delay


def wave(changes, v0=0):
    """Vertices of a digital waveform given (time, new value) pairs."""
    xs, ys, v = [0.0], [v0], v0
    for t, nv in changes:
        if nv != v:
            xs += [t, t + RISE]
            ys += [v, nv]
            v = nv
    xs.append(T_END)
    ys.append(v)
    return xs, ys


def value_at(changes, t, v0=0):
    v = v0
    for tc, nv in changes:
        if tc <= t:
            v = nv
    return v


# clock: period 4, high during [4k + 2, 4k + 4)
clk = []
for k in range(5):
    clk += [(4 * k + 2, 1), (4 * k + 4, 0)]
clk = [(t, v) for t, v in clk if t < T_END]
rising = [t for t, v in clk if v == 1]

d = [(1.0, 1), (2.7, 0), (3.4, 1), (4.6, 0), (6.6, 1), (8.8, 0), (10.5, 1), (11.3, 0), (12.6, 1), (15.0, 0), (15.6, 1)]

# D latch: transparent while clk = 1, holds while clk = 0
events = sorted({t for t, _ in clk} | {t for t, _ in d})
q_latch, q = [], 0
for t in events:
    if value_at(clk, t) == 1:
        nq = value_at(d, t)
        if nq != q:
            q_latch.append((t + DELAY, nq))
            q = nq
# D flip-flop: samples D at each rising edge
q_ff, q = [], 0
for t in rising:
    nq = value_at(d, t - 1e-9)
    if nq != q:
        q_ff.append((t + DELAY, nq))
        q = nq

rows = [("CLK", clk), ("D", d), ("Q (D latch)", q_latch), ("Q (D flip-flop)", q_ff)]
fig, ax = plt.subplots(figsize=(9, 3.8))
for i, (name, ch) in enumerate(rows):
    base = (len(rows) - 1 - i) * 1.3
    xs, ys = wave(ch)
    ax.plot(xs, [base + 0.8 * y for y in ys], lw=1.8, color=f"C{i}")
    ax.text(-0.3, base + 0.4, name, ha="right", va="center", fontsize=10)
for t in rising:
    ax.axvline(t, color="0.6", lw=0.8, ls="--", zorder=0)
for t, v in clk:
    if v == 1:
        ax.axvspan(t, t + 2, color="C0", alpha=0.07, lw=0)
ax.set_xlim(0, T_END)
ax.set_ylim(-0.3, len(rows) * 1.3)
ax.set_yticks([])
ax.set_xlabel("time")
ax.set_xticks([])
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.set_title("A latch is transparent while CLK = 1; a flip-flop samples D only at the rising edge", fontsize=10)
fig.tight_layout()
