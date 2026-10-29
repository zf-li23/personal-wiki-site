# The experiments behind the default model of neural induction in Xenopus animal caps. Rows: an intact animal cap
# cultured alone forms epidermis; the same cells dissociated (so that secreted BMPs are diluted away) and
# reaggregated form neural tissue; dissociated cells given BMP4 form epidermis again; an intact cap expressing the
# BMP antagonists Noggin or Chordin, or a dominant-negative BMP receptor, forms neural tissue. Conclusion: BMP
# signalling among ectoderm cells keeps them epidermal; neural is the fate they adopt when BMP signalling is blocked.
import numpy as np
import wikibio as bio
from matplotlib.patches import Wedge, Circle

fig, ax = bio.canvas(22.0, 12.0)
P = bio.P
epi, neu = "channel", "neuron"
rows = [("intact animal cap", None, "epidermis", epi), ("cells dissociated, then reaggregated", "dissociate", "neural tissue", neu),
        ("dissociated cells + BMP4 protein", "dissociate+bmp", "epidermis", epi),
        ("intact cap + Noggin, Chordin or dnBMPR", "antagonist", "neural tissue", neu)]
for k, (txt, kind, out, tok) in enumerate(rows):
    y = 10.4 - k * 2.8
    bio.label(ax, (0.4, y + 0.95), txt, size="small", bold=True, ha="left")
    if kind is None or kind == "antagonist":
        ax.add_patch(Wedge((3.0, y - 0.5), 1.1, 0, 180, facecolor=P.fill(epi), edgecolor=P.edge(epi), lw=1.1, zorder=8))
        if kind == "antagonist":
            for j in range(6):
                t = np.pi * (j + 0.5) / 6
                ax.add_patch(Circle((3.0 + 0.65 * np.cos(t), y - 0.5 + 0.5 * np.sin(t)), 0.08, facecolor=P.edge("metabolite"),
                                    edgecolor="none", zorder=9))
    else:
        rng = np.random.default_rng(k)
        for j in range(14):
            ax.add_patch(Circle((2.0 + 2.0 * rng.random(), y - 0.6 + 1.0 * rng.random()), 0.16, facecolor=P.fill(epi),
                                edgecolor=P.edge(epi), lw=0.7, zorder=8))
        if kind == "dissociate+bmp":
            for j in range(10):
                ax.add_patch(Circle((2.0 + 2.0 * rng.random(), y - 0.6 + 1.0 * rng.random()), 0.05, facecolor=P.edge("drug"),
                                    edgecolor="none", zorder=9))
    bio.arrow(ax, (4.6, y - 0.1), (7.2, y - 0.1), kind="process")
    bio.box(ax, (9.2, y - 0.1), 3.2, 0.9, token=tok, text=out, size="small")
    note = {None: "BMP4 made by the cells acts on them", "dissociate": "BMP diluted in the medium",
            "dissociate+bmp": "BMP restored", "antagonist": "BMP signalling blocked"}[kind]
    bio.label(ax, (11.4, y - 0.1), note, size="tiny", color=P.muted(), ha="left")
bio.label(ax, (17.6, 6.0), "BMP on → epidermis\nBMP off → neural\n(the default model)", size="normal", bold=True)
ax.plot([15.4, 15.4], [1.2, 11.0], color=P.mix(P.muted(), P.surface(), 0.5), lw=0.8)
for k, (tok, name) in enumerate([("drug", "BMP4 protein"), ("metabolite", "antagonist (injected mRNA)")]):
    ax.add_patch(Circle((16.2, 3.0 - 0.6 * k), 0.08, facecolor=P.edge(tok), edgecolor="none"))
    bio.label(ax, (16.5, 3.0 - 0.6 * k), name, size="tiny", ha="left")
