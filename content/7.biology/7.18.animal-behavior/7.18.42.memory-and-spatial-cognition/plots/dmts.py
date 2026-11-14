# Delayed matching to sample (DMTS) in pigeons. A: one trial on a three-key panel: a white ready signal on the
# center key; the sample (red) on the center key, pecked a few times; a dark retention interval; the two
# comparison stimuli on the side keys (red and blue, position randomized), of which pecking the one matching the sample
# is rewarded. B: forgetting curves (illustrative, of the shape found by Grant 1975): accuracy falls toward
# chance (50 %) within seconds, and faster when trials follow each other closely (intertrial interval, ITI,
# 4 s rather than 20 s), because the sample of the previous trial interferes with the current one (proactive
# interference). Curves: accuracy = 0.5 + 0.45 exp(-d / tau) with tau = 3 s (short ITI) and 9 s (long ITI).
import numpy as np

import wikibio as bio
from wikibio import quant
from matplotlib.patches import Circle, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(25.0, 8.8)
bio.panel(ax, "A", (0.2, 8.6))
steps = [("ready", [None, "neutral", None]), ("sample", [None, "negative", None]),
         ("delay", [None, None, None]), ("choice", ["negative", None, "dna"])]
for k, (name, keys) in enumerate(steps):
    x0 = 0.8 + k * 3.3
    ax.add_patch(FancyBboxPatch((x0, 2.6), 2.8, 3.4, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor=P.mix(P.fill("neutral"), P.surface(), 0.6), edgecolor=P.edge("neutral"),
                                lw=0.9, zorder=4))
    for j, tok in enumerate(keys):
        c = (x0 + 0.55 + j * 0.85, 4.6)
        face = P.fill(tok) if tok else P.mix(P.ink(), P.surface(), 0.75)
        ax.add_patch(Circle(c, 0.3, facecolor=face, edgecolor=P.ink(), lw=0.8, zorder=6))
    bio.label(ax, (x0 + 1.4, 3.2), name, size="small")
    if k < 3:
        bio.arrow(ax, (x0 + 2.9, 4.3), (x0 + 3.2, 4.3), kind="process")
bio.label(ax, (0.8 + 2 * 3.3 + 1.4, 1.7), "retention interval d", size="tiny", color=P.muted())
bio.label(ax, (0.8 + 3 * 3.3 + 1.4, 1.7), "peck the match: food", size="tiny", color=P.muted())
bio.label(ax, (0.8 + 3 * 3.3 + 0.55, 5.4), "match", size="tiny", color=P.muted())

pb = quant.Plot(ax, (16.6, 1.8, 7.6, 6.0), (0, 20), (0.4, 1.0), xlabel="Retention interval d / s",
                ylabel="Proportion correct", xticks=[0, 5, 10, 15, 20], yticks=[0.5, 0.75, 1.0])
bio.panel(ax, "B", (14.8, 8.6))
d = np.linspace(0, 20, 200)
pb.hline(0.5, text="chance", side="left")
pb.line(d, 0.5 + 0.45 * np.exp(-d / 9), "dna", lw=2.0, text="ITI 20 s", at=0.45, dy=0.25)
pb.line(d, 0.5 + 0.45 * np.exp(-d / 3), "rna", lw=2.0, dashed=True, text="ITI 4 s", at=0.12, dx=0.35, dy=-0.05)
