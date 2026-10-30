"""Stem-cell lines derived from the mouse blastocyst and the post-implantation epiblast.

Center: a late blastocyst (trophectoderm, inner cell mass split into epiblast and primitive endoderm). Each
lineage gives a self-renewing line in defined conditions: embryonic stem cells (ESC, naive pluripotency, from
the epiblast; LIF with MEK and GSK3 inhibitors, "2i"), trophoblast stem cells (TSC, from the trophectoderm;
FGF4, heparin and fibroblast-conditioned medium), extraembryonic endoderm stem cells (XEN, from the primitive
endoderm). Epiblast stem cells (EpiSC, primed pluripotency) are derived from the epiblast after implantation
(FGF2 and Activin A). Below each line: the tissues it contributes to when injected into a host blastocyst.
"""

from matplotlib.patches import Circle
import wikibio as bio
from wikibio import development as dev

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(30.0, 13.0)
icm = dev.embryo(ax, (15.0, 8.0), r=2.0, stage="blastocyst", icm="positive", troph="receptor")
bio.callout(ax, (16.75, 8.9), (18.6, 11.9), "Trophectoderm", size="tiny")
bio.callout(ax, icm, (11.0, 11.9), "Epiblast (inner cell mass)", size="tiny")
bio.label(ax, (15.0, 5.4), "E4.5 mouse blastocyst", size="tiny", color=P.muted())


def colony(c, tok, kind="dome"):
    import numpy as np
    rng = np.random.default_rng(len(tok))
    if kind == "dome":
        pts = [(0, 0), (0.45, 0.1), (-0.45, 0.1), (0.2, 0.42), (-0.22, 0.4), (0.0, -0.35), (0.42, -0.3), (-0.4, -0.3)]
        r = 0.27
    else:
        pts = [(x * 0.48, y * 0.48) for x in range(-2, 3) for y in range(-1, 2)]
        r = 0.23
    for dx, dy in pts:
        ax.add_patch(Circle((c[0] + dx, c[1] + dy), r, fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.6, zorder=6))


lines = (
    ((3.5, 8.0), "positive", "dome", "ESC (naive)", "LIF + 2i (MEK, GSK3 inhibitors)", "all embryonic lineages\nand germ line"),
    ((3.5, 2.6), "positive", "flat", "EpiSC (primed)", "FGF2 + Activin A; from E5.5-6.5 epiblast",
     "rarely contribute to\nblastocyst chimeras"),
    ((26.5, 8.0), "receptor", "dome", "TSC", "FGF4 + heparin", "trophoblast lineages\n(placenta)"),
    ((26.5, 2.6), "lipid", "dome", "XEN", "from primitive endoderm", "parietal (yolk-sac)\nendoderm"),
)
for c, tok, kind, name, cond, chim in lines:
    colony(c, tok, kind)
    bio.label(ax, (c[0], c[1] + 1.25), name, size="small", bold=True)
    bio.label(ax, (c[0], c[1] - 1.0), cond, size="tiny")
    bio.label(ax, (c[0], c[1] - 1.75), chim, size="tiny", color=P.muted())
bio.arrow(ax, (13.4, 8.4), (5.2, 8.0), kind="process")
bio.arrow(ax, (17.2, 8.6), (24.8, 8.0), kind="process")
bio.arrow(ax, (15.9, 7.7), (24.8, 3.0), kind="process")
bio.label(ax, (21.5, 4.9), "primitive endoderm", size="tiny", color=P.muted())
bio.arrow(ax, (13.8, 6.8), (5.2, 3.0), kind="process", dashed=True)
bio.label(ax, (8.2, 4.9), "after implantation", size="tiny", color=P.muted())
bio.label(ax, (15.0, 0.6), "naive: two active X chromosomes (female), dome colonies; primed: X inactivation begun, flat colonies;"
          " human ES cells resemble the primed state", size="tiny", color=P.muted())
