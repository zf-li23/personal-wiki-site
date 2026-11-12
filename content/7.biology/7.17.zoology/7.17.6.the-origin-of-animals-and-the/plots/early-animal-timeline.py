"""The early history of animals, 760-500 Mya (approximate ages; time scale after the ICS chart 2023).

Ages are approximate literature values: Sturtian (about 717-660) and Marinoan (about 650-635) glaciations,
Gaskiers glaciation (about 580); sponge-type steroid biomarkers (about 660-635, disputed); Doushantuo
(Weng'an) embryo-like fossils (about 610-590); Avalon (about 575-560), White Sea (about 560-550) and Nama
(about 550-539) assemblages; bilaterian trace fossils from about 560; Cloudina and Namacalathus (about
550-539); base of the Cambrian at 538.8 (Treptichnus pedum); small shelly fauna (about 539-521); first
trilobites (about 521); Chengjiang and Sirius Passet (about 518); Burgess Shale (about 508). Molecular-clock
estimates for crown-group Metazoa span roughly 800-650 Mya.
"""

import wikibio as bio
from wikibio import phylo, quant

P = bio.P
fig, ax = bio.canvas(29.0, 14.0)
x0, x1 = 7.5, 25.5
A0, A1 = 760.0, 500.0


def X(a):
    return x0 + (A0 - a) / (A0 - A1) * (x1 - x0)


ROWS = [  # (label, old, young, token, kind)
    ("molecular clock: crown Metazoa", 800, 650, "dna", "range"),
    ("glaciations", None, None, "neutral", "glac"),
    ("sponge-type biomarkers (disputed)", 660, 635, "neutral", "bar"),
    ("Doushantuo embryo-like fossils", 610, 590, "neutral", "bar"),
    ("Avalon assemblage (fronds)", 575, 560, "plant", "bar"),
    ("White Sea assemblage", 560, 550, "plant", "bar"),
    ("Nama assemblage", 550, 538.8, "plant", "bar"),
    ("bilaterian trace fossils", 560, 500, "positive", "fade"),
    ("first skeletons ($\\it{Cloudina}$, $\\it{Namacalathus}$)", 550, 538.8, "atp", "bar"),
    ("small shelly fauna", 538.8, 521, "atp", "bar"),
    ("trilobites", 521, 500, "atp", "fade"),
]
top = 12.2
step = 0.82
for k, (name, a, b, tok, kind) in enumerate(ROWS):
    y = top - step * k
    bio.label(ax, (x0 - 0.25, y), name, size="small", ha="right")
    ax.plot([x0, x1], [y, y], color=P.mix(P.muted(), P.surface(), 0.75), lw=0.5, zorder=2)
    if kind == "glac":
        for g0, g1, gname in ((717, 660, "Sturtian"), (650, 635, "Marinoan"), (581, 579, "Gaskiers")):
            bio.box(ax, ((X(g0) + X(g1)) / 2, y), max(X(g1) - X(g0), 0.12), 0.42, "neutral", radius=0.06, lw=0.6)
            bio.label(ax, ((X(g0) + X(g1)) / 2, y + 0.42), gname, size="tiny", color=P.muted())
        continue
    a_draw = min(a, A0)
    xa, xb = X(a_draw), X(b)
    if kind == "range":
        bio.box(ax, ((xa + xb) / 2, y), xb - xa, 0.42, tok, radius=0.06, lw=0.6)
        bio.label(ax, (xa + 0.2, y + 0.45), "estimates extend to before 760", size="tiny", color=P.muted(), ha="left")
    elif kind == "fade":
        n = 24
        for i in range(n):
            f = i / n
            bio.box(ax, (xa + (f + 0.5 / n) * (xb - xa), y), (xb - xa) / n + 0.01, 0.42, tok, radius=0.0, lw=0.0)
            ax.patches[-1].set_alpha(0.9 - 0.6 * f)
    else:
        bio.box(ax, ((xa + xb) / 2, y), max(xb - xa, 0.12), 0.42, tok, radius=0.06, lw=0.6)

# single events as triangles with labels
yb = top - step * len(ROWS) + 0.25
for age, text, dy in ((538.8, "base of Cambrian (Treptichnus pedum)", 0.0), (518, "Chengjiang, Sirius Passet", 0.0),
                      (508, "Burgess Shale", -0.55)):
    xx = X(age)
    ax.plot([xx, xx], [yb, (13.3 if age > 515 else 12.75) + 0.1], color=P.ink() if age == 538.8 else P.muted(), lw=0.9 if age == 538.8 else 0.7,
            ls="-" if age == 538.8 else (0, (3, 2)), zorder=3)
for age, text, yy, ha, dx in ((538.8, "base of Cambrian ($\\it{Treptichnus\\ pedum}$), 538.8", 13.3, "right", -0.12),
                              (518, "Chengjiang, Sirius Passet, 518", 13.3, "left", 0.12),
                              (508, "Burgess Shale, 508", 12.75, "left", 0.12)):
    bio.label(ax, (X(age) + dx, yy), text, size="tiny", color=P.muted(), ha=ha, va="center")
# Cambrian explosion bracket
quant.bracket(ax, (X(538.8), yb - 0.1), (X(515), yb - 0.1), text="Cambrian explosion", side=-1, size="tiny")
gy = yb - 1.0
phylo.geo_scale(ax, (x0, x1), (A0, A1), gy, ranks=("era", "period"), height=0.55)
for a in (750, 700, 650, 600, 550, 500):
    xx = X(a)
    ax.plot([xx, xx], [gy - 1.1, gy - 1.25], color=P.muted(), lw=0.7)
    bio.label(ax, (xx, gy - 1.5), str(a), size="tiny", color=P.muted())
bio.label(ax, ((x0 + x1) / 2, gy - 2.0), "millions of years ago", size="small", color=P.muted())
