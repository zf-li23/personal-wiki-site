"""Formation of the neuromuscular junction. (A) Before innervation, acetylcholine receptors (AChR) are spread over
the muscle fibre, with a faint prepattern in its central band. (B) The motor axon terminal releases agrin (the
neural, z+ isoform), which binds LRP4; LRP4 activates the receptor tyrosine kinase MuSK, which with Dok7 recruits
rapsyn and clusters AChR under the terminal, at the crests of the junctional folds of the postsynaptic membrane.
Neuregulin and other signals raise transcription of AChR genes in the subsynaptic nuclei, while electrical activity
of the fibre represses it in the other nuclei, so receptors become concentrated at the synapse. (C) Polyneuronal
innervation at birth is reduced to a single axon per fibre within the first weeks by activity-dependent
competition."""
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Rectangle

fig, ax = bio.canvas(24, 8.4)
P = bio.P


def fibre(x0, y0, w, h=1.6):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0))
    for k in range(4):
        ax.add_patch(Ellipse((x0 + w * (0.12 + 0.25 * k), y0 + 0.45), 0.7, 0.32, facecolor=P.light("nucleus"),
                             edgecolor=P.edge("nucleus"), lw=0.6))


def achr(x, y):
    ax.add_patch(Rectangle((x - 0.05, y), 0.1, 0.22, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.4))


bio.panel(ax, "A", (0.2, 8.2))
fibre(0.6, 3.0, 6.2)
rng = np.random.default_rng(0)
for x in rng.uniform(0.8, 6.6, 30):
    achr(x, 4.6)
for x in rng.uniform(3.0, 4.4, 10):
    achr(x, 4.6)
bio.label(ax, (3.7, 2.4), "aneural AChR prepattern", size="small")
bio.label(ax, (3.7, 6.0), "muscle fibre before innervation", size="tiny", color=P.muted())

bio.panel(ax, "B", (7.6, 8.2))
x0, y0 = 8.0, 1.2
ax.add_patch(Rectangle((x0, y0), 8.6, 2.6, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0))
# junctional folds
xs = np.linspace(x0 + 1.5, x0 + 7.1, 6)
for x in xs:
    ax.add_patch(Rectangle((x - 0.12, y0 + 1.6), 0.24, 1.0, facecolor=P.fill("extracellular"), edgecolor=P.edge("muscle"), lw=0.6))
for x in np.linspace(x0 + 1.15, x0 + 7.45, 7):
    for dx in (-0.12, 0.0, 0.12):
        achr(x + dx, y0 + 2.6)
# subsynaptic nuclei
for x in (x0 + 2.5, x0 + 5.8):
    ax.add_patch(Ellipse((x, y0 + 0.75), 1.1, 0.45, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8))
bio.label(ax, (x0 + 4.2, y0 + 0.3), "subsynaptic nuclei: more AChR transcription", size="tiny", color=P.muted())
# basal lamina and terminal
ax.plot([x0 + 0.6, x0 + 8.0], [y0 + 3.05, y0 + 3.05], color=P.edge("extracellular"), lw=2.0, ls=(0, (4, 2)))
term = bio.blob((x0 + 4.3, y0 + 4.3), 3.6, 0.9, wobble=0.04, seed=4, k=10)
bio.shape(ax, term, "neuron", lw=1.0)
ax.add_patch(Rectangle((x0 + 4.0, y0 + 5.0), 0.6, 1.8, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.0))
for k in range(14):
    ax.add_patch(Circle((x0 + 1.4 + 0.42 * k, y0 + 4.2 + 0.25 * ((k % 3) - 1)), 0.14, facecolor=P.fill("vesicle"),
                        edgecolor=P.edge("vesicle"), lw=0.5, zorder=7))
bio.label(ax, (x0 + 4.3, y0 + 7.0), "motor axon terminal", size="small")
bio.callout(ax, (x0 + 6.8, y0 + 3.05), (x0 + 9.2, y0 + 5.2), "basal lamina: agrin")
bio.callout(ax, (xs[2], y0 + 2.75), (x0 + 9.2, y0 + 4.4), "AChR clusters")
bio.callout(ax, (xs[3], y0 + 2.0), (x0 + 9.2, y0 + 3.6), "junctional folds")
bio.label(ax, (x0 + 9.0, y0 + 2.7), "agrin → LRP4 → MuSK", size="tiny", ha="left")
bio.label(ax, (x0 + 9.0, y0 + 2.3), "→ Dok7 → rapsyn", size="tiny", ha="left")
bio.label(ax, (x0 + 9.0, y0 + 1.6), "neuregulin → ErbB:", size="tiny", ha="left")
bio.label(ax, (x0 + 9.0, y0 + 1.2), "synaptic AChR genes", size="tiny", ha="left")

bio.panel(ax, "C", (19.6, 8.2))
for k, (label, n) in enumerate((("birth", 3), ("2 weeks", 1))):
    y = 5.6 - k * 3.2
    ax.add_patch(Rectangle((20.0, y - 0.5), 3.6, 1.0, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=1.0))
    for j in range(n):
        xa = 21.8 + (j - (n - 1) / 2) * 0.5
        ax.plot([xa - 0.6 + 0.6 * j, xa], [y + 1.6, y + 0.55], color=P.edge(["neuron", "receptor", "enzyme"][j]), lw=1.6)
        ax.add_patch(Circle((xa, y + 0.55), 0.14, facecolor=P.fill(["neuron", "receptor", "enzyme"][j]), edgecolor="none"))
    bio.label(ax, (21.8, y - 0.9), label, size="tiny", color=P.muted())
bio.arrow(ax, (21.8, 4.2), (21.8, 3.3), kind="process", head=0.13, lw=0.9)
