import matplotlib.pyplot as plt

N_CLK = 18
PERIOD = 1.0
RISE = 0.04
DELAY = 0.08  # drawn clock-to-output delay
T_END = N_CLK * PERIOD


def wave(values, offset):
    """Waveform vertices for a signal that takes values[k] during clock period k."""
    xs, ys = [0.0], [values[0]]
    for k in range(1, len(values)):
        if values[k] != values[k - 1]:
            t = k * PERIOD + offset
            xs += [t, t + RISE]
            ys += [values[k - 1], values[k]]
    xs.append(T_END)
    ys.append(values[-1])
    return xs, ys


count = [k % 16 for k in range(N_CLK)]
rows = []
clk_x, clk_y = [0.0], [0]
for k in range(N_CLK):
    clk_x += [k * PERIOD, k * PERIOD + RISE, (k + 0.5) * PERIOD, (k + 0.5) * PERIOD + RISE]
    clk_y += [0, 1, 1, 0]
clk_x.append(T_END)
clk_y.append(0)
rows.append(("CLK", (clk_x, clk_y)))
for i in range(4):
    rows.append((f"Q{i}", wave([(c >> i) & 1 for c in count], DELAY)))
rows.append(("RCO", wave([int(c == 15) for c in count], DELAY)))

fig, ax = plt.subplots(figsize=(9.5, 4.2))
for i, (name, (xs, ys)) in enumerate(rows):
    base = (len(rows) - 1 - i) * 1.25
    ax.plot(xs, [base + 0.8 * y for y in ys], lw=1.6, color=f"C{i}")
    ax.text(-0.25, base + 0.4, name, ha="right", va="center", fontsize=10)
for k in range(N_CLK):
    ax.axvline(k * PERIOD, color="0.75", lw=0.6, ls="--", zorder=0)
    ax.text((k + 0.5) * PERIOD, len(rows) * 1.25 - 0.1, str(count[k]), ha="center", va="bottom", fontsize=8)
ax.set_xlim(0, T_END)
ax.set_ylim(-0.3, len(rows) * 1.25 + 0.4)
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlabel("time (count value shown above each clock period)")
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.set_title(r"4-bit synchronous binary counter: $Q_i$ divides the clock frequency by $2^{i+1}$", fontsize=10)
fig.tight_layout()
