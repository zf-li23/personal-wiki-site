# Raup's theoretical morphospace of coiled shells (Raup 1966, J. Paleontol. 40:1178), Eq. (13.1).
# A: a grid of whorl expansion rate W (columns, log-spaced) and translation rate T (rows) at D = 0.1,
# with the approximate regions occupied by real shells (after Raup 1966). B: the planispiral plane
# (T = 0): W against D, with the curve D = 1/W above which successive whorls no longer touch.
import numpy as np
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
WS = [1.5, 2.5, 5, 10, 100, 10000]
WL = ["1.5", "2.5", "5", "10", "10²", "10⁴"]
TS = [0, 1, 2.5, 5]
C = 3.1
X0, Y0 = 2.6, 2.0
WB = [1.5, 2.2, 3.2, 5.0]
DB = [0.0, 0.2, 0.4, 0.6]
XB = X0 + C * len(WS) + 3.4
fig, ax = bio.canvas(XB + C * len(WB) + 0.8, Y0 + C * len(TS) + 1.8)


def cell(x0, i, j):
    return x0 + C * (i + 0.5), Y0 + C * (j + 0.5)


def shade(x0, i0, i1, j0, j1, tok, name, where):
    xa, ya = x0 + C * i0 + 0.1, Y0 + C * j0 + 0.1
    w, h = C * (i1 - i0 + 1) - 0.2, C * (j1 - j0 + 1) - 0.2
    bio.box(ax, (xa + w / 2, ya + h / 2), w, h, token=tok, radius=0.4, lw=0.8, zorder=1)
    ax.patches[-1].set_facecolor(P.mix(P.fill(tok), P.surface(), 0.8 if P.is_dark() else 0.62))
    ty = ya + 0.26 if where == "below" else ya + h - 0.26
    bio.label(ax, (xa + 0.18, ty), name, size="tiny", bold=True, ha="left", color=P.fill(tok) if P.is_dark() else P.edge(tok))


# A
bio.panel(ax, "A", (0.2, Y0 + C * len(TS) + 1.5))
for args in [((0, 2), (0, 0), "dna", "Coiled cephalopods", "below"), ((0, 2), (1, 3), "positive", "Gastropods", "above"),
             ((3, 5), (0, 0), "antibody", "Bivalves, brachiopods", "below"), ((3, 5), (1, 1), "antibody", "A few bivalves", "above")]:
    (i0, i1), (j0, j1), tok, name, where = args
    shade(X0, i0, i1, j0, j1, tok, name, where)
for i, W in enumerate(WS):
    for j, T in enumerate(TS):
        x, y = cell(X0, i, j)
        elev = 80 if T == 0 else (34 if W >= 10 else 10)
        zm.raup_shell(ax, (x, y), C * 0.6, W=W, D=0.1, T=T, elev=elev, n_theta=120, n_phi=16, z=5)
for i, lab in enumerate(WL):
    bio.label(ax, (cell(X0, i, 0)[0], Y0 - 0.3), lab, size="small", va="top")
for j, T in enumerate(TS):
    bio.label(ax, (X0 - 0.3, cell(X0, 0, j)[1]), f"{T:g}", size="small", ha="right")
bio.label(ax, (X0 + C * len(WS) / 2, Y0 - 1.1), "W, whorl expansion rate (log scale)", size="normal", va="top")
bio.label(ax, (X0 - 1.3, Y0 + C * len(TS) / 2), "T, translation rate", size="normal", rotation=90)
bio.label(ax, (X0 + C * len(WS) / 2, Y0 + C * len(TS) + 0.8), "D = 0.1", size="normal", bold=True)

# B: planispiral plane
bio.panel(ax, "B", (XB - 2.2, Y0 + C * len(TS) + 1.5))
# the curve D = 1/W across the cells (W positions interpolated on the log scale of the columns)
lw = np.log(WB)
Wc = np.linspace(1 / 0.6, 5.0, 200)
xc = XB + C * (0.5 + np.interp(np.log(Wc), lw, np.arange(len(WB))))
yc = Y0 + C * (0.5 + np.interp(1 / Wc, DB, np.arange(len(DB)), left=-0.5, right=len(DB) - 0.5))
ok = (1 / Wc >= DB[0] - 0.1) & (1 / Wc <= DB[-1] + 0.1)
for i, W in enumerate(WB):
    for j, D in enumerate(DB):
        x, y = cell(XB, i, j)
        if D > 1 / W:
            bio.box(ax, (x, y), C - 0.2, C - 0.2, token="negative", radius=0.3, lw=0.6, zorder=1)
            ax.patches[-1].set_facecolor(P.mix(P.fill("negative"), P.surface(), 0.82 if P.is_dark() else 0.72))
        zm.raup_shell(ax, (x, y), C * 0.62, W=W, D=D, T=0.0, elev=90, azim=200, n_theta=120, n_phi=16, z=5)
ax.plot(xc[ok], yc[ok], color=P.ink(), lw=1.4, ls=(0, (4, 3)), zorder=8)
bio.label(ax, (XB + C * 3.0, Y0 + C * 1.62), "D = 1/W", size="small", bold=True)
for i, W in enumerate(WB):
    bio.label(ax, (cell(XB, i, 0)[0], Y0 - 0.3), f"{W:g}", size="small", va="top")
for j, D in enumerate(DB):
    bio.label(ax, (XB - 0.3, cell(XB, 0, j)[1]), f"{D:g}", size="small", ha="right")
bio.label(ax, (XB + C * len(WB) / 2, Y0 - 1.1), "W (T = 0, planispiral)", size="normal", va="top")
bio.label(ax, (XB - 1.3, Y0 + C * len(DB) / 2), "D, distance from axis", size="normal", rotation=90)
bio.label(ax, (XB + C * len(WB) / 2, Y0 + C * len(TS) + 0.8), "Shaded: open coils, whorls not touching", size="small",
          color=P.muted())
