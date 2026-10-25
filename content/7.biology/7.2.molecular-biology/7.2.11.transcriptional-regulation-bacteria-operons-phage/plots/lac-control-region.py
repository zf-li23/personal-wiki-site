# The lac control region (SBOL Visual glyphs, not to scale) and repression by DNA looping.
# A: lacI with its own promoter; then O3 (centered at -82), the CAP site (-61.5), the lac promoter, O1 (+11,
# overlapping the start site), lacZ containing O2 (+412), lacY and lacA; below, the polycistronic lacZYA mRNA.
# B: a repressor tetramer (two dimers joined at their C-terminal helices) bound to O1 with one dimer and to O3
# with the other, the intervening DNA (93 bp, including the CAP site and the promoter) forming a loop.
import numpy as np
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(21.0, 10.6)

# --- A: map --------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.45))
y = 9.0
parts = G.construct(ax, 0.8, y, [
    ("promoter", "P(lacI)"),
    {"kind": "cds", "text": "lacI", "token": "negative", "width": 2.2},
    ("terminator", ""),
    ("operator", "O3"),
    ("operator", "CAP"),
    ("promoter", "P(lac)"),
    ("operator", "O1"),
    {"kind": "cds", "text": "lacZ", "token": "enzyme", "width": 5.2},
    {"kind": "cds", "text": "lacY", "token": "channel", "width": 2.6},
    {"kind": "cds", "text": "lacA", "token": "protein", "width": 1.6},
    ("terminator", ""),
], unit=0.6, gap=0.2)
z = parts[7]
xo2 = z["x0"] + 0.08 * (z["x1"] - z["x0"]) + 0.3
bio.box(ax, (xo2, y - 0.75), 0.75, 0.38, token="highlight", text="O2", size="tiny", radius=0.06)
ax.plot([xo2, xo2], [y - 0.55, y - 0.1], color=P.muted(), lw=0.8)
for k, txt in [(3, "−82"), (4, "−61.5"), (6, "+11")]:
    bio.label(ax, (parts[k]["centre"], y - 0.75), txt, size="tiny", color=P.muted())
bio.label(ax, (xo2, y - 1.15), "+412", size="tiny", color=P.muted())
# mRNA
x0m, x1m = parts[6]["centre"], parts[9]["x1"] + 0.2
bio.strand(ax, (x0m, y - 2.0), (x1m, y - 2.0), token="mrna")
bio.label(ax, ((x0m + x1m) / 2, y - 2.55), "polycistronic mRNA", size="small")
bio.label(ax, (parts[1]["centre"], y - 1.4), "repressor gene", size="tiny", color=P.muted())

# --- B: loop --------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 5.6))
yb = 1.75
xa, xb = 7.0, 12.0  # O3 and O1 positions on the line
t = np.linspace(0, 1, 300)
# DNA: straight upstream, loop up between O3 and O1, straight downstream
left = np.c_[np.linspace(1.0, xa, 50), np.full(50, yb)]
ang = np.linspace(np.pi, 0, 200)
cx, rx, ry = (xa + xb) / 2, (xb - xa) / 2, 2.7
loop = np.c_[cx + rx * np.cos(ang) * (1 + 0.15 * np.sin(ang)), yb + ry * np.sin(ang)]
right = np.c_[np.linspace(xb, 20.0, 80), np.full(80, yb)]
dna = np.vstack([left, loop, right])
ax.plot(dna[:, 0], dna[:, 1], color=P.edge("dna"), lw=3.0, solid_capstyle="round", zorder=3)
for x, name in [(xa, "O3"), (xb, "O1")]:
    bio.box(ax, (x, yb), 0.9, 0.45, token="highlight", text=name, size="tiny", radius=0.06, zorder=6)
# repressor: two dimers (blobs) at the operators, joined by the tetramerization bundle
for x in (xa, xb):
    bio.protein(ax, (x + (0.55 if x == xa else -0.55), yb - 0.8), 1.3, 0.85, "negative", text="dimer", size="tiny")
ax.plot([xa + 1.1, xb - 1.1], [yb - 1.05, yb - 1.05], color=P.edge("negative"), lw=4.0, solid_capstyle="round", zorder=11)
bio.label(ax, (cx, yb - 1.4), "LacI tetramer", size="small")
# CAP and promoter inside the loop
p_cap = loop[40]
p_pro = loop[120]
bio.protein(ax, (p_cap[0], p_cap[1]), 1.0, 0.65, "positive", text="CAP", size="tiny")
bio.callout(ax, (p_pro[0] + 0.1, p_pro[1]), (14.6, 4.9), "promoter within the loop")
bio.label(ax, (cx, yb + 1.6), "93 bp loop", size="small", color=P.muted())
bio.label(ax, (17.5, yb + 0.4), "downstream: O2 in the coding region", size="tiny", color=P.muted())
