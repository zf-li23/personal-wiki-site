"""Monozygotic twins and the time of separation (classical interpretation, after the extraembryonic
membranes the twins share). Separation of blastomeres before the trophectoderm forms (days 1 to 3) gives two
chorions and two amnions (dichorionic diamniotic, about a third of monozygotic twins); division of the inner
cell mass in the blastocyst (days 4 to 8) gives one chorion and two amnions (monochorionic diamniotic, about
two thirds); division of the embryonic disc after the amnion forms (days 8 to 12) gives one chorion and one
amnion (monochorionic monoamniotic, about 1 %); incomplete division later, around the time of gastrulation,
gives conjoined twins. That some dichorionic twins arise from later events is debated (see text)."""
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse

P = bio.P
fig, ax = bio.canvas(22, 8.6)
cho, amn, emb = "metabolite", "dna2", "animal"


def sac(c, r, tok, z):
    ax.add_patch(Circle(c, r, facecolor=P.fill("vacuole"), edgecolor=P.edge(tok), lw=1.6, zorder=z))


def embryo(c, ang=0):
    ax.add_patch(Ellipse(c, 0.55, 0.28, angle=ang, facecolor=P.fill(emb), edgecolor=P.edge(emb), lw=1.0, zorder=9))


xs = [3.0, 8.4, 13.8, 19.2]
y = 5.2
# dichorionic diamniotic
for dx in (-1.05, 1.05):
    sac((xs[0] + dx, y), 0.95, cho, 5)
    sac((xs[0] + dx, y + 0.1), 0.55, amn, 6)
    embryo((xs[0] + dx, y + 0.05))
# monochorionic diamniotic
sac((xs[1], y), 1.75, cho, 5)
for dx in (-0.7, 0.7):
    sac((xs[1] + dx, y + 0.2), 0.62, amn, 6)
    embryo((xs[1] + dx, y + 0.15))
# monochorionic monoamniotic
sac((xs[2], y), 1.75, cho, 5)
sac((xs[2], y + 0.2), 1.05, amn, 6)
embryo((xs[2] - 0.4, y + 0.25), 20)
embryo((xs[2] + 0.4, y + 0.1), -25)
# conjoined
sac((xs[3], y), 1.75, cho, 5)
sac((xs[3], y + 0.2), 1.05, amn, 6)
o = bio.blob((xs[3], y + 0.2), 0.62, 0.26, wobble=0.12, seed=4, k=7)
bio.shape(ax, o, emb, lw=1.0, zorder=9)
names = ["Dichorionic,\ndiamniotic", "Monochorionic,\ndiamniotic", "Monochorionic,\nmonoamniotic", "Conjoined"]
share = ["about 1/3", "about 2/3", "about 1 %", "about 1 in 200 000 births"]
for x, nm, sh in zip(xs, names, share):
    bio.label(ax, (x, 7.75), nm, size="small", bold=True)
    bio.label(ax, (x, 3.05), sh, size="small", color=P.muted())
# time axis
ax.plot([1.0, 21.4], [1.6, 1.6], color=P.ink(), lw=1.2)
bio.arrow(ax, (21.0, 1.6), (21.6, 1.6), kind="process", head=0.22)
spans = [(1.2, 4.8, "days 1-3: blastomeres\n(before trophectoderm)"), (6.2, 10.6, "days 4-8: inner cell mass\n(before amnion)"),
         (11.6, 16.0, "days 8-12: embryonic disc\n(after amnion)"), (17.0, 21.0, "after day 12:\nincomplete division")]
for a, b, text in spans:
    ax.plot([a, b], [1.85, 1.85], color=P.edge("highlight"), lw=4, solid_capstyle="butt")
    bio.label(ax, ((a + b) / 2, 0.85), text, size="tiny")
bio.label(ax, (21.6, 2.0), "time of separation", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (1.0, 8.4), "Chorion", size="tiny", color=P.edge(cho), ha="left")
bio.label(ax, (2.6, 8.4), "Amnion", size="tiny", color=P.edge(amn), ha="left")
