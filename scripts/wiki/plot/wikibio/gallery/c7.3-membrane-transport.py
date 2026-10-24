# Transport across the plasma membrane. Passive: small nonpolar molecules diffuse through the bilayer, K+ leaves
# through a K+ channel and glucose enters by the uniporter GLUT1, each down its own gradient. Secondary active:
# SGLT1 couples the entry of 2 Na+ down the Na+ gradient to glucose uptake against its gradient. Primary
# active: the Na+/K+-ATPase (P-type) pumps 3 Na+ out and 2 K+ in per ATP hydrolysed, maintaining the
# gradients (typical mammalian concentrations, right).
import numpy as np
import wikibio as bio
from wikibio import cellbio as CB
from wikibio import charts as C

fig, ax = bio.canvas(23.6, 9.6)
P = bio.P
y = 4.6
CB.sides(ax, (0.3, 19.3), y, height=(4.1, 3.9))
bio.bilayer(ax, [(0.3, y), (19.3, y)])
top, bot = y + CB.MH, y - CB.MH


def glc(xy, z=18):
    bio.molecule(ax, xy, token="carbohydrate", text="Glc", r=0.24, size=5.4, zorder=z)


def title(x, a, b):
    bio.label(ax, (x, 8.15), a, size="normal", bold=True)
    bio.label(ax, (x, 7.7), b, size="small", color=P.muted())


# 1. simple diffusion
x = 2.2
title(x, "Simple diffusion", "O₂, CO₂, steroids")
bio.arrow(ax, (x - 0.45, 6.5), (x - 0.45, 2.6), kind="process", zorder=16)
bio.molecule(ax, (x - 0.45, 6.9), token="neutral", text="O₂", r=0.22, size=5.6)
bio.arrow(ax, (x + 0.45, 2.6), (x + 0.45, 6.5), kind="process", zorder=16)
bio.molecule(ax, (x + 0.45, 2.2), token="neutral", text="CO₂", r=0.26, size=5.2)

# 2. K+ channel
x = 5.75
title(x, "Channel", "K⁺ leak channel")
CB.channel(ax, x, y)
bio.arrow(ax, (x, 2.5), (x, 6.6), kind="process", zorder=16)
for yy in (2.15, 3.4, y, 5.9):
    bio.ion(ax, (x + (0.0 if abs(yy - y) < 0.1 else 0.32), yy), "k", r=0.15, text=False, zorder=17)
bio.label(ax, (x + 0.55, 2.15), "K⁺", size="tiny", ha="left")

# 3. uniporter GLUT1
x = 9.35
title(x, "Uniporter", "GLUT1")
site = CB.carrier(ax, x, y, open="out")
bio.arrow(ax, (x, 6.6), (x, 2.5), kind="process", zorder=16)
glc((x + 0.42, 6.75))
glc(site + (0, 0.1))
glc((x + 0.42, 2.4))

# 4. symporter SGLT1
x = 13.0
title(x, "Symporter", "SGLT1")
site = CB.carrier(ax, x, y, open="out", token="receptor", width=1.45)
bio.arrow(ax, (x - 0.35, 6.6), (x - 0.35, 2.5), kind="process", zorder=16)
bio.arrow(ax, (x + 0.35, 6.6), (x + 0.35, 2.5), kind="process", zorder=16)
for k, yy in enumerate((6.75, 7.2)):
    bio.ion(ax, (x - 0.75, yy), "na", r=0.15, text=False)
bio.label(ax, (x - 1.0, 6.97), "2 Na⁺", size="tiny", ha="right")
glc((x + 0.8, 6.85))
bio.ion(ax, site + (-0.2, 0.1), "na", r=0.13, text=False, zorder=18)
glc(site + (0.2, 0.12))
bio.label(ax, (x + 0.8, 6.4), "(uphill)", size="tiny", color=P.muted())

# 5. Na+/K+-ATPase
x = 16.9
title(x, "Pump (P-type ATPase)", "Na⁺/K⁺-ATPase")
atp = CB.pump(ax, x, y, width=1.6)
bio.arrow(ax, (x - 0.55, 2.6), (x - 0.55, 6.6), kind="process", zorder=16)
bio.arrow(ax, (x - 0.05, 6.6), (x - 0.05, 2.6), kind="process", zorder=16)
for k in range(3):
    bio.ion(ax, (x - 0.95, 6.45 + 0.35 * k), "na", r=0.15, text=False)
bio.label(ax, (x - 1.2, 6.8), "3 Na⁺", size="tiny", ha="right")
for k in range(2):
    bio.ion(ax, (x + 0.3, 2.4 + 0.35 * k), "k", r=0.15, text=False)
bio.label(ax, (x + 0.55, 2.57), "2 K⁺", size="tiny", ha="left")
bio.molecule(ax, atp + (0.2, 0.35), token="atp", text="ATP", r=0.26, size=5.4)
bio.arrow(ax, atp + (0.2, 0.05), atp + (0.2, -0.45), kind="process", head=0.15)
bio.label(ax, atp + (0.2, -0.7), "ADP + Pᵢ", size="tiny")

# categories
for (x0, x1), text, tok in (((0.8, 11.0), "Passive: down the electrochemical gradient", "positive"),
                            ((11.5, 14.6), "Secondary active", "highlight"),
                            ((15.2, 18.8), "Primary active (ATP)", "negative")):
    yy = 0.95
    ax.plot([x0, x0, x1, x1], [yy + 0.15, yy, yy, yy + 0.15], color=P.edge(tok), lw=1.1)
    bio.label(ax, ((x0 + x1) / 2, yy - 0.3), text, size="small", color=P.edge(tok), bold=True)

# --- concentrations -------------------------------------------------------------------------------------------
pax = C.axes_at(ax, (20.65, 2.2, 2.6, 5.4))
ions = [("Na⁺", "na", 145, 12), ("K⁺", "k", 4, 140), ("Cl⁻", "cl", 110, 10)]
xs = np.arange(len(ions))
for i, (name, tok, out, inn) in enumerate(ions):
    pax.bar(i - 0.2, out, 0.38, color=P.edge(tok), lw=0)
    pax.bar(i + 0.2, inn, 0.38, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
pax.set_xticks(xs, [n for n, *_ in ions])
pax.set_ylim(0, 160)
C.style_axes(pax, None, "concentration / mM")
pax.tick_params(axis="x", labelsize=bio.core.FONT["small"])
C.title(pax, "Typical gradients")
bio.label(ax, (20.75, 1.35), "■", size="small", color=P.muted(), ha="left")
bio.label(ax, (21.05, 1.35), "outside", size="tiny", ha="left")
ax.add_patch(bio.core.Polygon([(22.0, 1.25), (22.2, 1.25), (22.2, 1.45), (22.0, 1.45)], closed=True, facecolor=P.surface(),
                              edgecolor=P.muted(), lw=0.8))
bio.label(ax, (22.3, 1.35), "inside", size="tiny", ha="left")
