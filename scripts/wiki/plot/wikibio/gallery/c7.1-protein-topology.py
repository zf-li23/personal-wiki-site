# Protein topology diagrams. A: the Rossmann fold (dinucleotide-binding domain): six parallel beta-strands in
# the order 3-2-1-4-5-6, joined by right-handed beta-alpha-beta crossovers; the helices of the first
# mononucleotide-binding motif lie on one face of the sheet, those of the second on the other face, and the
# glycine-rich GxGxxG loop after beta1 binds the diphosphate of NAD(P)+ at the C-terminal edge of the sheet.
# B: the TIM (beta/alpha)8 barrel seen from the C-terminal end of the barrel (TOPS symbols: triangles are
# strands pointing at the viewer, circles helices pointing away); the active site is formed by the
# beta->alpha loops. C: the same Rossmann domain as a linear secondary-structure map (schematic residue ranges).
import math

import numpy as np
import wikibio as bio
from wikibio import metabolism as M

fig, ax = bio.canvas(19.0, 10.9)
P = bio.P

# --- A: Rossmann fold ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.75))
bio.label(ax, (0.7, 10.5), "Rossmann fold", size="normal", bold=True, ha="left")
yb, yt = 4.6, 7.6       # strand N (bottom) and C (top) ends
hb, ht = 4.75, 7.45     # helix C (bottom) and N (top) ends
sx = {3: 1.4, 2: 2.55, 1: 3.7, 4: 5.4, 5: 6.55, 6: 7.7}
hx = {1: 3.125, 2: 1.975, 3: 4.55, 4: 5.975, 5: 7.125}
back = {4, 5}           # helices of the second motif lie behind the sheet
for k, x in sx.items():
    M.strand(ax, (x, yb), (x, yt), width=0.4, text=f"β{k}", zorder=12)
for k, x in hx.items():
    M.helix(ax, (x, ht), (x, hb), width=0.42, text=f"α{k}", back=k in back, zorder=9 if k in back else 14)


def up(x1, x2, h=0.45, y1=yt, y2=ht + 0.06, dashed=False, color=None, lw=None):
    return M.loop(ax, [(x1, y1 - 0.02), (x1 + (x2 - x1) * 0.15, y1 + h), (x2 - (x2 - x1) * 0.15, y1 + h), (x2, y2)],
                  dashed=dashed, color=color, lw=lw or bio.core.LINE * 1.3)


def down(x1, x2, h=0.5, dashed=False):
    return M.loop(ax, [(x1, hb - 0.06), (x1 + (x2 - x1) * 0.15, yb - h), (x2 - (x2 - x1) * 0.15, yb - h), (x2, yb + 0.02)],
                  dashed=dashed)


gly = up(sx[1], hx[1], color=P.edge("highlight"), lw=bio.core.LINE * 2.2)          # GxGxxG loop
down(hx[1], sx[2])
up(sx[2], hx[2])
down(hx[2], sx[3])
M.loop(ax, [(sx[3], yt - 0.02), (sx[3] + 0.15, yt + 0.75), (2.6, yt + 1.05), (4.1, yt + 1.05), (hx[3], yt + 0.55), (hx[3], ht + 0.06)])
down(hx[3], sx[4])
up(sx[4], hx[4], dashed=True)
down(hx[4], sx[5], dashed=True)
up(sx[5], hx[5], dashed=True)
down(hx[5], sx[6], dashed=True)
M.loop(ax, [(sx[6], yt - 0.02), (sx[6] + 0.12, yt + 0.45), (sx[6] + 0.45, yt + 0.6)])
M.terminus(ax, (sx[6] + 0.72, yt + 0.62), "C")
M.loop(ax, [(sx[1], yb - 0.55), (sx[1], yb + 0.02)])
M.terminus(ax, (sx[1], yb - 0.78), "N")
mid = gly[len(gly) // 2]
bio.callout(ax, tuple(mid), (4.75, 9.55), "GxGxxG loop (binds the NAD⁺ diphosphate)")
bio.label(ax, (8.3, yt + 0.25), "C-terminal\nedge", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.3, yb - 0.1), "N-terminal\nedge", size="tiny", color=P.muted(), ha="left")
for (x0, x1), text in (((1.05, 4.05), "Motif 1: β1-αA-β2-αB-β3"), ((5.05, 8.05), "Motif 2: β4-αD-β5-αE-β6")):
    y = 3.35
    ax.plot([x0, x0, x1, x1], [y + 0.12, y, y, y + 0.12], color=P.muted(), lw=0.9)
    bio.label(ax, ((x0 + x1) / 2, y - 0.3), text.replace("αA", "α1").replace("αB", "α2").replace("αD", "α4").replace("αE", "α5"),
              size="tiny", color=P.muted())
# legend for the faces
lx, ly = 1.0, 2.55
M.helix(ax, (lx, ly), (lx + 0.6, ly), width=0.26, zorder=14)
bio.label(ax, (lx + 0.8, ly), "helix in front of the sheet", size="tiny", ha="left")
M.helix(ax, (lx + 4.0, ly), (lx + 4.6, ly), width=0.26, back=True, zorder=9)
bio.label(ax, (lx + 4.8, ly), "helix behind the sheet", size="tiny", ha="left")

# --- B: TIM barrel, top view ------------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 10.75))
bio.label(ax, (11.2, 10.5), "TIM barrel, (β/α)₈", size="normal", bold=True, ha="left")
c = np.array([14.6, 6.85])
rs, rh = 1.15, 2.35
S = [c + rs * np.array([math.cos(math.radians(90 - 45 * k)), math.sin(math.radians(90 - 45 * k))]) for k in range(8)]
H = [c + rh * np.array([math.cos(math.radians(90 - 45 * k - 22.5)), math.sin(math.radians(90 - 45 * k - 22.5))]) for k in range(8)]
for k in range(8):
    a, h, b = S[k], H[k], S[(k + 1) % 8]
    # beta->alpha loop at the top (catalytic) face: solid; alpha->beta loop at the bottom face: dashed
    ax.plot(*np.array([a, h]).T, color=P.edge("highlight"), lw=bio.core.LINE * 1.8, solid_capstyle="round", zorder=10)
    ax.plot(*np.array([h, b]).T, color=P.muted(), lw=bio.core.LINE, ls=(0, (2.5, 2)), zorder=10)
for k in range(8):
    M.tops_strand(ax, S[k], r=0.36, up=True, text=f"{k + 1}")
    M.tops_helix(ax, H[k], r=0.36, text=f"α{k + 1}")
bio.label(ax, tuple(c), "active\nsite", size="tiny", color=P.edge("highlight"), bold=True)
ly = 3.6
M.tops_strand(ax, (11.4, ly), r=0.22)
bio.label(ax, (11.75, ly), "β-strand (towards viewer)", size="tiny", ha="left")
M.tops_helix(ax, (15.4, ly), r=0.22)
bio.label(ax, (15.75, ly), "α-helix (away)", size="tiny", ha="left")
ly2 = 3.0
ax.plot([11.2, 11.65], [ly2, ly2], color=P.edge("highlight"), lw=bio.core.LINE * 1.8)
bio.label(ax, (11.75, ly2), "βα loop (top, catalytic face)", size="tiny", ha="left")
ax.plot([15.2, 15.65], [ly2, ly2], color=P.muted(), lw=bio.core.LINE, ls=(0, (2.5, 2)))
bio.label(ax, (15.75, ly2), "αβ loop (bottom)", size="tiny", ha="left")

# --- C: linear map -----------------------------------------------------------------------------------------
bio.panel(ax, "C", (0.1, 1.95))
segs = [("strand", 3, 9, "β1"), ("helix", 15, 28, "α1"), ("strand", 33, 38, "β2"), ("helix", 43, 55, "α2"),
        ("strand", 60, 64, "β3"), ("helix", 70, 84, "α3"), ("strand", 90, 95, "β4"), ("helix", 100, 113, "α4"),
        ("strand", 118, 123, "β5"), ("helix", 128, 142, "α5"), ("strand", 148, 153, "β6")]
X = M.ss_track(ax, 1.0, 1.05, segs, 165, scale=17.0 / 165, ticks=20, height=0.56)
bio.label(ax, (X(1) - 0.2, 1.05), "N", size="small", bold=True, ha="right")
bio.label(ax, (X(165) + 0.2, 1.05), "C", size="small", bold=True, ha="left")
ax.add_patch(bio.core.FancyBboxPatch((X(10), 0.82), X(14) - X(10), 0.46, boxstyle="round,pad=0,rounding_size=0.08",
                                     facecolor="none", edgecolor=P.edge("highlight"), lw=1.2, zorder=14))
bio.label(ax, ((X(10) + X(14)) / 2, 1.62), "GxGxxG", size="tiny", color=P.edge("highlight"), bold=True, va="bottom")
