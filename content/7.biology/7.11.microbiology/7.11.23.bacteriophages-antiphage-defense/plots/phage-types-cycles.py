# A: the main morphotypes of bacteriophages, drawn to one scale (head diameters 60-90 nm).
# B: the virulent and the temperate life cycle, as one diagram with the decision at its centre.
import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(30, 13.6)
MUT = P.muted()
HEAD = "virus"


def head(x, y, r=0.8, prolate=0.0, tok=HEAD, zorder=10):
    pts = np.array([[-1, -1 - prolate], [-1, 0.45 + prolate], [0, 1.25 + prolate], [1, 0.45 + prolate],
                    [1, -1 - prolate], [0, -1.7 - prolate]]) * r + [x, y]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=zorder))
    return y - (1.7 + prolate) * r


def tail(x, y_top, length, sheath=False, fibres=2, tok="enzyme", zorder=9, baseplate=True):
    ax.plot([x, x], [y_top, y_top - length], color=P.edge("neutral"), lw=1.8, zorder=zorder, solid_capstyle="round")
    if sheath:
        for yy in np.arange(y_top - 0.12, y_top - length + 0.1, -0.26):
            ax.add_patch(Polygon([[x - 0.3, yy], [x + 0.3, yy], [x + 0.3, yy - 0.2], [x - 0.3, yy - 0.2]], closed=True,
                                 facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5, zorder=zorder + 1))
    if baseplate:
        ax.add_patch(Polygon([[x - 0.55, y_top - length], [x + 0.55, y_top - length], [x + 0.38, y_top - length - 0.28],
                              [x - 0.38, y_top - length - 0.28]], closed=True, facecolor=P.fill("protein"),
                             edgecolor=P.edge("protein"), lw=0.8, zorder=zorder + 2))
    for s in (-1, 1):
        for k in range(fibres):
            ax.plot([x + s * 0.45, x + s * (1.0 + 0.3 * k)], [y_top - length - 0.2, y_top - length - 0.8 - 0.25 * k],
                    color=P.edge("enzyme"), lw=0.9, zorder=zorder)


# ================================================================ A: morphotypes
bio.panel(ax, "A", (0.2, 13.3))
bio.label(ax, (1.0, 13.1), "Morphotypes", size="title", bold=True, ha="left")
y0 = 10.6
items = [
    ("myovirus\n(T4)", 1.8, "contractile tail;\ndsDNA, 169 kbp"),
    ("siphovirus\n(λ, T5)", 5.2, "long flexible tail;\ndsDNA, 48.5 kbp"),
    ("podovirus\n(T7, φ29)", 8.6, "short tail;\ndsDNA, 40 kbp"),
    ("microvirus\n(φX174)", 11.6, "no tail, spikes;\nssDNA, 5.4 kb"),
    ("levivirus\n(MS2, Qβ)", 14.0, "no tail;\nssRNA, 3.6 kb"),
    ("cystovirus\n(φ6)", 16.4, "enveloped;\nsegmented dsRNA"),
    ("inovirus\n(M13)", 19.2, "filamentous, extruded\nwithout lysis; ssDNA"),
]
# tailed phages
b = head(1.8, y0, 0.75, prolate=0.25)
tail(1.8, b, 2.2, sheath=True, fibres=2)
b = head(5.2, y0, 0.7)
tail(5.2, b, 2.6, sheath=False, fibres=1)
b = head(8.6, y0, 0.7)
tail(8.6, b, 0.7, sheath=False, fibres=1)
# tailless icosahedral: microvirus with spikes, levivirus plain
for x, spikes in ((11.6, True), (14.0, False)):
    ax.add_patch(Circle((x, y0 - 0.6), 0.62, facecolor=P.fill(HEAD), edgecolor=P.edge(HEAD), lw=1.0, zorder=10))
    if spikes:
        for a in np.arange(0, 360, 72):
            t = np.radians(a)
            ax.plot([x + 0.6 * np.cos(t), x + 0.95 * np.cos(t)], [y0 - 0.6 + 0.6 * np.sin(t), y0 - 0.6 + 0.95 * np.sin(t)],
                    color=P.edge("protein"), lw=1.2, zorder=9)
# cystovirus: envelope around a capsid
ax.add_patch(Circle((16.4, y0 - 0.6), 0.92, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=1.0, zorder=9))
ax.add_patch(Circle((16.4, y0 - 0.6), 0.58, facecolor=P.fill(HEAD), edgecolor=P.edge(HEAD), lw=0.9, zorder=10))
# inovirus: filament
t = np.linspace(0, 1, 200)
ax.plot(18.2 + 2.0 * t, y0 - 0.6 + 0.22 * np.sin(8 * np.pi * t), color=P.edge(HEAD), lw=3.2, zorder=10,
        solid_capstyle="round")
for name, x, sub in items:
    bio.label(ax, (x, 5.0), name, size="small")
    bio.label(ax, (x, 3.95), sub, size="tiny", color=MUT)
bio.scale_bar(ax, (1.3, 2.6), 2.3, "100 nm")
bio.label(ax, (11.6, 2.5), "the tail types are shapes, not taxa: the families named after them were abolished in 2022",
          size="small", color=MUT)

# ================================================================ B: life cycles
bio.panel(ax, "B", (21.0, 13.3))
bio.label(ax, (21.8, 13.1), "Virulent and temperate life cycles", size="title", bold=True, ha="left")
cx, cy = 25.0, 9.0
M.bacillus(ax, (cx, cy), 3.0, 1.7, gram="-", zorder=6)
b = head(cx - 0.9, cy + 3.0, 0.38)
tail(cx - 0.9, b, 0.6, sheath=True, fibres=1, baseplate=False)
bio.arrow(ax, (cx - 0.9, cy + 1.9), (cx - 0.9, cy + 1.1), kind="process", lw=1.1, head=0.2)
bio.label(ax, (cx - 2.6, cy + 2.2), "infection", size="small", color=MUT)
ax.add_patch(Circle((cx + 3.0, cy - 0.2), 0.85, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                    lw=0.9, zorder=13))
bio.label(ax, (cx + 3.0, cy - 0.2), "lysis\nor\nlysogeny", size="tiny", color=P.on_fill(), zorder=14)
bio.arrow(ax, (cx + 1.6, cy - 0.2), (cx + 2.0, cy - 0.2), kind="process", lw=1.1, head=0.2)
# lytic branch (down left)
bio.arrow(ax, (cx + 2.5, cy - 0.9), (cx + 0.6, cy - 2.6), kind="process", lw=1.2, head=0.22)
for px, py in [(22.4, 5.3), (23.6, 4.6), (24.6, 5.4), (23.0, 3.6), (24.4, 3.3)]:
    b2 = head(px, py + 0.5, 0.26)
    tail(px, b2, 0.4, sheath=True, fibres=1, baseplate=False)
bio.label(ax, (23.4, 1.7), "lytic cycle: replication,\nassembly, lysis; ~100 progeny", size="small")
# lysogenic branch (down right)
bio.arrow(ax, (cx + 3.6, cy - 0.9), (cx + 4.2, cy - 2.4), kind="process", lw=1.2, head=0.22)
M.bacillus(ax, (28.6, 5.4), 2.8, 1.5, gram="-", zorder=6)
ax.plot([27.6, 29.6], [5.4, 5.4], color=P.edge("dna") if not P.is_dark() else P.fill("dna"), lw=1.8, zorder=10)
ax.plot([28.3, 29.0], [5.4, 5.4], color=P.edge("negative") if not P.is_dark() else P.fill("negative"), lw=3.0, zorder=11)
bio.label(ax, (28.6, 4.4), "prophage", size="tiny", color=MUT)
bio.label(ax, (28.4, 2.6), "lysogeny: replicated with the host,\nimmunity to superinfection,\nlysogenic conversion",
          size="small")
bio.arrow(ax, (29.4, 6.3), (27.4, 8.3), kind="process", lw=1.1, head=0.2, dashed=True, bend=0.18)
bio.label(ax, (29.6, 7.6), "induction\n(SOS: DNA damage)", size="tiny", color=MUT)
