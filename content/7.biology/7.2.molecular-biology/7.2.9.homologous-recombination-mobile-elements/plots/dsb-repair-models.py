# Double-strand-break repair by homologous recombination: SDSA and DSBR (double Holliday junction).
# Broken duplex blue, intact homologue pink; upper strand of each duplex runs 5'->3' left to right.
# Arrowheads mark 3' ends; dashed segments are new DNA (pink dashes: copied from the homologue,
# blue dashes: copied from the blue duplex).
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 15.0)
BL, PK = "dna", "receptor"
LW = bio.core.LINE * 2.0
s = 0.14          # half spacing of the two strands of a duplex
W = 5.6           # panel width


def line(pts, tok, dashed=False, arrow=False):
    p = np.asarray(pts, float)
    col = P.edge(tok) if not dashed else P.fill(tok)
    ax.plot(p[:, 0], p[:, 1], color=col, lw=LW, ls=(0, (2.2, 1.4)) if dashed else "-",
            solid_capstyle="round", dash_capstyle="round", zorder=10)
    if arrow:
        a, b = p[-2], p[-1]
        d = (b - a) / np.hypot(*(b - a))
        n = np.array([-d[1], d[0]])
        tip = b + d * 0.16
        ax.fill(*np.array([tip, b - d * 0.05 + n * 0.12, b - d * 0.05 - n * 0.12]).T, color=col, zorder=11, lw=0)


def title(x0, yt, num, text):
    bio.label(ax, (x0, yt + 0.75), f"{num}  {text}", size="small", bold=True, ha="left")


def homolog(x0, yh, loop=None, upper=True):
    """Intact pink duplex; loop = (xa, xb) displaces the upper strand as a D loop."""
    x1 = x0 + W
    line([(x0, yh - s), (x1, yh - s)], PK)
    if upper:
        if loop is None:
            line([(x0, yh + s), (x1, yh + s)], PK, arrow=True)
        else:
            xa, xb = loop
            line([(x0, yh + s), (xa - 0.2, yh + s), (xa, yh + 0.55), (xb, yh + 0.55), (xb + 0.2, yh + s), (x1, yh + s)], PK, arrow=True)


# ------------------------------------------------------------------ row 1: steps 1-3
y1t, gap = 13.1, 1.3
cols = [0.8, 8.1, 15.4]
# 1: break
x0 = cols[0]; xm = x0 + W / 2; yt = y1t; yh = yt - gap
title(x0, yt, 1, "Double-strand break")
line([(x0, yt + s), (xm - 0.1, yt + s)], BL, arrow=True)
line([(xm + 0.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(xm - 0.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL, arrow=True)
homolog(x0, yh)
# 2: resection
x0 = cols[1]; xm = x0 + W / 2
title(x0, yt, 2, "Resection to 3′ tails")
line([(x0, yt + s), (xm - 0.1, yt + s)], BL, arrow=True)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL, arrow=True)
homolog(x0, yh)
# 3: invasion, D loop, extension
x0 = cols[2]; xm = x0 + W / 2
title(x0, yt, 3, "Strand invasion, D loop, synthesis")
line([(x0, yt + s), (xm - 1.5, yt + s), (xm - 0.9, yh + 0.02), (xm - 0.1, yh + 0.02)], BL)
line([(xm - 0.1, yh + 0.02), (xm + 0.9, yh + 0.02)], PK, dashed=True, arrow=True)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL, arrow=True)
homolog(x0, yh, loop=(xm - 0.9, xm + 1.2))

# ------------------------------------------------------------------ row 2: SDSA
y2t = 8.6
bio.label(ax, (0.8, y2t + 1.55), "SDSA (continuing from 3)", size="normal", bold=True, ha="left", color=P.edge("enzyme"))
x0 = cols[0]; xm = x0 + W / 2; yt = y2t; yh = yt - gap
title(x0, yt, 4, "Displacement and annealing")
line([(x0, yt + s), (xm - 0.1, yt + s)], BL)
line([(xm - 0.1, yt + s), (xm + 0.9, yt + s)], PK, dashed=True, arrow=True)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL, arrow=True)
homolog(x0, yh)
x0 = cols[1]; xm = x0 + W / 2
title(x0, yt, 5, "Gap filling: noncrossover")
line([(x0, yt + s), (xm - 0.1, yt + s)], BL)
line([(xm - 0.1, yt + s), (xm + 1.1, yt + s)], PK, dashed=True)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL)
line([(xm + 0.1, yt - s), (xm - 1.1, yt - s)], BL, dashed=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
homolog(x0, yh)
bio.label(ax, (xm + 0.5, yt - 0.55), "conversion tract", size="tiny", color=P.muted())

# ------------------------------------------------------------------ row 3: DSBR
y3t = 3.6
bio.label(ax, (0.8, y3t + 1.55), "DSBR (continuing from 3)", size="normal", bold=True, ha="left", color=P.edge("protein"))
x0 = cols[0]; xm = x0 + W / 2; yt = y3t; yh = yt - gap
title(x0, yt, 6, "Second-end capture: double HJ")
xa, xb = xm - 1.2, xm + 1.4
# blue upper: crosses down at xa, runs in homologue position, crosses up at xb
line([(x0, yt + s), (xa - 0.25, yt + s), (xa + 0.25, yh + s), (xm - 0.1, yh + s)], BL)
line([(xm - 0.1, yh + s), (xb - 0.25, yh + s)], PK, dashed=True)
line([(xb - 0.25, yh + s), (xb + 0.25, yt + s), (x0 + W, yt + s)], BL, arrow=True)
# pink upper: crosses up at xa, runs in blue position, crosses down at xb
line([(x0, yh + s), (xa - 0.25, yh + s), (xa + 0.25, yt + s), (xb - 0.25, yt + s), (xb + 0.25, yh + s), (x0 + W, yh + s)], PK, arrow=True)
# lower strands
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL)
line([(xm + 0.1, yt - s), (xm - 1.1, yt - s)], PK, dashed=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0, yh - s), (x0 + W, yh - s)], PK)
for xx in (xa, xb):
    bio.label(ax, (xx, yh - 0.6), "HJ", size="tiny", color=P.muted())
# 7: dissolution -> NCO
x0 = cols[1]; xm = x0 + W / 2
title(x0, yt, 7, "Dissolution (BTR): noncrossover")
line([(x0, yt + s), (xm - 0.1, yt + s)], BL)
line([(xm - 0.1, yt + s), (xm + 1.1, yt + s)], PK, dashed=True)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], BL, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], BL)
line([(xm + 0.1, yt - s), (xm - 1.1, yt - s)], PK, dashed=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
homolog(x0, yh)
# 8: resolution -> crossover
x0 = cols[2]; xm = x0 + W / 2
title(x0, yt, 8, "Resolution: crossover (or not)")
line([(x0, yt + s), (xm + 1.1, yt + s)], BL)
line([(xm + 1.1, yt + s), (x0 + W, yt + s)], PK, arrow=True)
line([(x0 + W, yt - s), (xm + 0.1, yt - s)], PK)
line([(xm + 0.1, yt - s), (xm - 1.1, yt - s)], PK, dashed=True)
line([(xm - 1.1, yt - s), (x0, yt - s)], BL, arrow=True)
line([(x0, yh + s), (xm - 1.1, yh + s)], PK)
line([(xm - 1.1, yh + s), (x0 + W, yh + s)], BL, arrow=True)
line([(x0 + W, yh - s), (xm - 1.1, yh - s)], BL)
line([(xm - 1.1, yh - s), (x0, yh - s)], PK, arrow=True)
bio.label(ax, (xm, yh - 0.6), "flanks exchanged", size="tiny", color=P.muted())

# arrows between panels and legend
for (a, b) in (((6.7, y1t - 0.6), (7.7, y1t - 0.6)), ((14.0, y1t - 0.6), (15.0, y1t - 0.6)),
               ((6.7, y2t - 0.6), (7.7, y2t - 0.6)), ((6.7, y3t - 0.6), (7.7, y3t - 0.6))):
    bio.arrow(ax, a, b, kind="process")
bio.arrow(ax, (3.4, y3t - 2.35), (18.2, y3t - 2.35), kind="process", bend=-0.04)
bio.label(ax, (10.8, y3t - 2.05), "or", size="tiny", color=P.muted())
ly = 0.45
for k, (tok, dashed, text) in enumerate(((BL, False, "broken duplex"), (PK, False, "homologue"),
                                         (PK, True, "new DNA copied from homologue"), (BL, True, "new DNA copied from blue duplex"))):
    xx = 0.8 + k * 5.3
    line([(xx, ly), (xx + 0.7, ly)], tok, dashed=dashed)
    bio.label(ax, (xx + 0.9, ly), text, size="tiny", ha="left")
