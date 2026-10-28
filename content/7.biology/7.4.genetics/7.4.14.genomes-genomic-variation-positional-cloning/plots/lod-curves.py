"""LOD score curves Z(theta) (Formulas 14.9.1 and 14.9.2). Family 1: phase known, 8 informative meioses
with 1 recombinant (the sequence P P P P P P P R). Family 2: phase unknown, 6 informative meioses, all of
the same phase type. Family 3: phase known, 10 meioses, 1 recombinant. The total (sum) crosses the
conventional threshold Z = 3 near its maximum; values below -2 exclude linkage at that theta."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
th = np.linspace(0.001, 0.5, 500)


def known(R, N):
    return np.log10(th ** R * (1 - th) ** (N - R) / 0.5 ** N)


def unknown(R, N):
    return np.log10(0.5 * (th ** R * (1 - th) ** (N - R) + th ** (N - R) * (1 - th) ** R) / 0.5 ** N)


fams = [("family 1: phase known, 1 R in 8", known(1, 8), "dna", "-"),
        ("family 2: phase unknown, 0 R in 6", unknown(0, 6), "enzyme", "-"),
        ("family 3: phase known, 1 R in 10", known(1, 10), "protein", "-")]
fig, ax = plt.subplots(figsize=(6.6, 4.0))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.15, top=0.95)
tot = 0
for name, z, tok, ls in fams:
    ax.plot(th, z, color=charts.line(tok), lw=1.3, ls=ls, label=name)
    tot = tot + z
ax.plot(th, tot, color=charts.line("receptor"), lw=2.0, label="sum")
i = np.argmax(tot)
ax.plot(th[i], tot[i], "o", color=charts.line("receptor"), ms=4)
ax.annotate(f"max Z = {tot[i]:.2f} at θ = {th[i]:.2f}", (th[i], tot[i]), xytext=(12, 6), textcoords="offset points",
            fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axhline(3, color=P.muted(), lw=0.7, ls="--")
ax.axhline(-2, color=P.muted(), lw=0.7, ls=":")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.text(0.49, 3.08, "Z = 3: linkage", ha="right", va="bottom", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(0.49, -1.92, "Z = −2: exclusion", ha="right", va="bottom", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_xlim(0, 0.5)
ax.set_ylim(-3, 4.2)
charts.style_axes(ax, "recombination fraction θ", "LOD score Z(θ)")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
