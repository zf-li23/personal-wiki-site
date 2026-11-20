"""The neural pathway of the jamming avoidance response in Eigenmannia (after Heiligenberg,
Metzner and colleagues). Boxes: stations; arrows: excitatory (open heads) and inhibitory
(bars) connections; labels give the information carried at each stage."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = plt.subplots(figsize=(11, 5.0))
ax.set_xlim(0, 22); ax.set_ylim(0, 10); ax.axis("off")


def box(x, y, w, h, text, token, sub=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.25",
                                facecolor=P.light(token), edgecolor=P.edge(token), lw=1.3))
    ax.text(x + w / 2, y + h / 2 + (0.22 if sub else 0), text, ha="center", va="center", fontsize=8.5,
            color=P.ink(), fontweight="bold")
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.32, sub, ha="center", va="center", fontsize=7, color=P.ink())
    return (x, y, w, h)


def arr(p, q, inhib=False, label=None, off=(0, 0.2)):
    ax.annotate("", q, p, arrowprops=dict(arrowstyle="-[" if inhib else "-|>", color=P.edge("negative") if inhib else P.ink(),
                                          lw=1.2, mutation_scale=10 if inhib else 12, shrinkA=2, shrinkB=2))
    if label:
        ax.text((p[0] + q[0]) / 2 + off[0], (p[1] + q[1]) / 2 + off[1], label, fontsize=7, color=P.muted(), ha="center")


box(0.3, 7.0, 3.0, 1.4, "T-units", "receptor", "tuberous: phase")
box(0.3, 4.6, 3.0, 1.4, "P-units", "receptor", "tuberous: amplitude")
box(4.6, 7.0, 3.6, 1.4, "ELL spherical cells", "neuron", "sharpened phase")
box(4.6, 4.6, 3.6, 1.4, "ELL pyramidal cells", "neuron", "E: amplitude up; I: down")
box(9.5, 5.6, 3.6, 1.8, "Torus semicircularis", "neuron", "lamina 6: differential phase;\ndeeper laminae: combine")
box(14.4, 5.6, 3.4, 1.8, "Nucleus electro-\nsensorius", "neuron", "sign of Δf, unambiguous")
box(14.6, 8.4, 2.6, 1.2, "nE↑", "positive")
box(14.6, 3.0, 2.6, 1.2, "nE↓", "negative")
box(18.6, 8.4, 3.1, 1.2, "CP/PPn-G", "protein", "thalamus")
box(18.6, 3.0, 3.1, 1.2, "SPPn", "protein", "midbrain, tonic")
box(17.6, 0.3, 4.1, 1.5, "Pacemaker nucleus", "highlight", "pacemaker cells → relay cells")
box(10.2, 0.3, 4.2, 1.5, "Spinal electromotor\nneurons", "muscle")
box(4.6, 0.3, 3.6, 1.5, "Electric organ", "muscle", "EOD")
arr((3.3, 7.7), (4.6, 7.7), label="1 spike / cycle")
arr((3.3, 5.3), (4.6, 5.3), label="spike prob.")
arr((8.2, 7.7), (9.5, 6.9))
arr((8.2, 5.3), (9.5, 6.1))
arr((13.1, 6.5), (14.4, 6.5))
arr((15.9, 7.4), (15.9, 8.4)); arr((15.9, 5.6), (15.9, 4.2))
arr((17.2, 9.0), (18.6, 9.0))
arr((17.2, 3.6), (18.6, 3.6), inhib=True, label="GABA", off=(0, 0.25))
arr((21.4, 8.4), (21.4, 1.8), label="AMPA → pacemaker\ncells: frequency up", off=(-1.2, 1.6))
arr((20.1, 3.0), (20.1, 1.8), label="NMDA → relay cells:\nfrequency down", off=(-2.6, -0.2))
arr((17.6, 1.05), (14.4, 1.05), label="command, 1:1")
arr((10.2, 1.05), (8.2, 1.05))
ax.annotate("", (1.8, 4.6), (4.6, 1.2), arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=1, ls="--",
                                                       connectionstyle="arc3,rad=-0.3"))
ax.text(1.4, 2.6, "own field\n+ neighbor", fontsize=7, color=P.muted(), ha="center")
fig.tight_layout()
