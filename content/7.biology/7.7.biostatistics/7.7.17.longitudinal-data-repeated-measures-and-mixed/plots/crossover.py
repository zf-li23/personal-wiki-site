"""The two-period, two-treatment cross-over design (schematic).

Top: participants are randomized to sequence AB or BA; each receives both treatments, separated by a
washout period with no treatment. Bottom: the expected response in each sequence and period when there is
a period effect (both treatments do a little better in period 2) and a carryover effect of A into
period 2 (dashed); the within-person difference d = A - B cancels the person's own level.
"""
import matplotlib.pyplot as plt
import wikibio as bio
from matplotlib.patches import FancyBboxPatch
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.6, 4.6), gridspec_kw=dict(height_ratios=[1.1, 1]))
fig.subplots_adjust(left=0.1, right=0.97, bottom=0.1, top=0.95, hspace=0.45)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ax.text(0.6, 1.5, "randomize", ha="center", va="center", fontsize=FT["small"], color=P.ink(), rotation=90)
for y, seq in [(2.2, "AB"), (0.8, "BA")]:
    ax.annotate("", xy=(1.5, y), xytext=(0.85, 1.5), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=1))
    for x0, lab in [(1.6, seq[0]), (6.2, seq[1])]:
        tok = "rna" if lab == "A" else "dna"
        ax.add_patch(FancyBboxPatch((x0, y - 0.32), 3.0, 0.64, boxstyle="round,pad=0.02,rounding_size=0.12",
                                    fc=P.fill(tok), ec=P.edge(tok), lw=1))
        ax.text(x0 + 1.5, y, f"treatment {lab}", ha="center", va="center", fontsize=FT["small"], color=P.on_fill())
    ax.add_patch(FancyBboxPatch((4.75, y - 0.32), 1.3, 0.64, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc="none", ec=P.muted(), lw=1, ls="--"))
    ax.text(5.4, y, "washout", ha="center", va="center", fontsize=FT["tiny"], color=P.muted())
    ax.text(9.35, y, f"sequence {seq}", ha="left", va="center", fontsize=FT["tiny"], color=P.ink())
ax.text(3.1, 2.85, "period 1", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.text(7.7, 2.85, "period 2", ha="center", fontsize=FT["tiny"], color=P.ink())
mu, tau, pi, lam = 5.0, 1.0, 0.4, 0.5
ab = [mu + tau / 2, mu - tau / 2 + pi + lam]
ba = [mu - tau / 2, mu + tau / 2 + pi]
bx.plot([1, 2], ab, "-o", color=charts.line("rna"), lw=1.6, label="sequence AB")
bx.plot([1, 2], ba, "-s", color=charts.line("dna"), lw=1.6, label="sequence BA")
bx.plot([2], [mu - tau / 2 + pi], "o", mfc="none", mec=charts.line("rna"), ms=7)
bx.plot([2, 2], [mu - tau / 2 + pi, ab[1]], color=charts.line("rna"), ls="--", lw=1)
bx.text(2.04, (mu - tau / 2 + pi + ab[1]) / 2, "carryover of A", fontsize=FT["tiny"], color=P.ink(), va="center")
for (xp, yv, lab) in [(1, ab[0], "A"), (2, ab[1], "B"), (1, ba[0], "B"), (2, ba[1], "A")]:
    bx.text(xp - 0.06, yv, lab, ha="right", va="center", fontsize=FT["tiny"], color=P.ink())
bx.set_xlim(0.7, 2.6)
bx.set_xticks([1, 2])
bx.set_xticklabels(["period 1", "period 2"])
bx.set_yticks([])
bx.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(bx, None, "mean response")
