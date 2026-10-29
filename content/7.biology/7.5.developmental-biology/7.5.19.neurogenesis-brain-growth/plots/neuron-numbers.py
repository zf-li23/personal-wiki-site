"""Numbers of neurons in the whole brain and in the cerebral cortex of four mammals, counted by the isotropic
fractionator (Herculano-Houzel and colleagues; human: Azevedo et al. 2009), plotted against brain mass on
logarithmic axes. Among primates neuron number grows almost in proportion to brain mass (the primate brain is a
linearly scaled-up brain), whereas rodent brains add mass faster than neurons; the human brain, with about 86
billion neurons of which about 16 billion are cortical, is what a primate brain of its size is expected to be."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
data = [("mouse", 0.40, 71e6, 14e6, "rodent"), ("rat", 1.8, 200e6, 31e6, "rodent"),
        ("macaque", 87.0, 6.38e9, 1.69e9, "primate"), ("human", 1508.0, 86.1e9, 16.3e9, "primate")]
fig, ax = plt.subplots(figsize=(6.6, 4.2))
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.14, top=0.95)
for name, m, nb, nc, grp in data:
    tok = "enzyme" if grp == "rodent" else "receptor"
    ax.loglog(m, nb, "o", color=charts.line(tok), ms=7)
    ax.loglog(m, nc, "s", color=charts.line(tok), ms=6, mfc="none")
    ax.text(m * 1.3, nb, name, fontsize=FT["small"], color=P_.ink(), va="center")
for grp, tok in (("rodent", "enzyme"), ("primate", "receptor")):
    pts = [(m, nb) for _, m, nb, _, g in data if g == grp]
    (m0, n0), (m1, n1) = pts
    ax.loglog([m0, m1], [n0, n1], color=charts.line(tok), lw=1.0, ls="--")
    ax.text(np.sqrt(m0 * m1) * (1.6 if grp == "rodent" else 1.0), np.sqrt(n0 * n1) * (0.3 if grp == "rodent" else 1.8),
            f"{grp}s: slope {np.log(n1 / n0) / np.log(m1 / m0):.2f}", fontsize=FT["tiny"], color=charts.line(tok), ha="center")
ax.plot([], [], "o", color=P_.muted(), label="whole brain")
ax.plot([], [], "s", color=P_.muted(), mfc="none", label="cerebral cortex")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
ax.set_xlim(0.2, 5000)
charts.style_axes(ax, "brain mass / g", "number of neurons")
