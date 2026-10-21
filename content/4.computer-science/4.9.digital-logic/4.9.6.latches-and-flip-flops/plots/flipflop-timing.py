import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.4, 3.6))
edge = 5.0
t_su, t_h = 1.4, 0.8
t_ccq, t_pcq = 0.7, 1.8
H = 0.8


def bus(ax, base, segments, color):
    """Bus-style waveform: stable intervals drawn as two rails, changes as crosses.

    segments: list of (start, end, kind) with kind 'stable' or 'change'."""
    for a, b, kind in segments:
        if kind == "stable":
            ax.plot([a, b], [base, base], color=color, lw=1.6)
            ax.plot([a, b], [base + H, base + H], color=color, lw=1.6)
        else:
            ax.fill_between([a, b], base, base + H, color=color, alpha=0.25, lw=0, hatch="///")
            ax.plot([a, b], [base, base + H], color=color, lw=1.0)
            ax.plot([a, b], [base + H, base], color=color, lw=1.0)


# clock
cb = 3.0
ax.plot([0, edge - 2.5, edge - 2.5 + 0.1, edge, edge + 0.1, 9.5],
        [cb, cb, cb, cb, cb + H, cb + H], color="C0", lw=1.8)
ax.plot([0, 2.5, 2.6], [cb + H, cb + H, cb], color="C0", lw=1.8)
ax.text(-0.2, cb + H / 2, "CLK", ha="right", va="center")

# data input: must be stable from t_su before to t_h after the edge
db = 1.6
bus(ax, db, [(0, 1.5, "stable"), (1.5, edge - t_su - 0.6, "change"), (edge - t_su - 0.6, edge + t_h + 0.4, "stable"),
             (edge + t_h + 0.4, edge + t_h + 1.2, "change"), (edge + t_h + 1.2, 9.5, "stable")], "C1")
ax.text(-0.2, db + H / 2, "D", ha="right", va="center")
ax.axvspan(edge - t_su, edge + t_h, color="C1", alpha=0.10, lw=0)

# output: may start changing after t_ccq, settles by t_pcq
qb = 0.2
bus(ax, qb, [(0, edge + t_ccq, "stable"), (edge + t_ccq, edge + t_pcq, "change"), (edge + t_pcq, 9.5, "stable")], "C2")
ax.text(-0.2, qb + H / 2, "Q", ha="right", va="center")

ax.axvline(edge, color="0.5", ls="--", lw=0.8)


def dim(x0, x1, y, label, above=True):
    ax.annotate("", xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle="<->", lw=1.0, color="0.35"))
    ax.text((x0 + x1) / 2, y + (0.12 if above else -0.12), label, ha="center", va="bottom" if above else "top", fontsize=10)


dim(edge - t_su, edge, db + H + 0.35, r"$t_{\mathrm{su}}$")
dim(edge, edge + t_h, db + H + 0.35, r"$t_{\mathrm{h}}$")
dim(edge, edge + t_ccq, qb - 0.25, r"$t_{\mathrm{ccq}}$", above=False)
dim(edge, edge + t_pcq, qb - 0.75, r"$t_{\mathrm{pcq}}$", above=False)
ax.text(edge - t_su - 0.15, db + H + 0.4, "D stable", fontsize=9, ha="right", va="center")
ax.set_xlim(-1.2, 9.5)
ax.set_ylim(-1.3, 4.1)
ax.axis("off")
fig.tight_layout()
