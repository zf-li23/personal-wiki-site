"""Transport systems in a gram-negative envelope (outside on top). Porin diffusion; proton symport
(lactose permease LacY); an ABC transporter (maltose: binding protein MalE, channel MalFG, ATPase
dimer MalK, 2 ATP per maltose); the glucose phosphotransferase system (PEP -> EI -> HPr -> EIIA ->
EIIB -> glucose 6-phosphate, EIIC the channel); iron-siderophore uptake (TonB-dependent receptor FepA
energized by TonB-ExbB-ExbD with the proton-motive force, periplasmic FepB, ABC transporter FepCDG).
Schematic, not to scale."""

from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import microbio as M

P = bio.P
W, H = 31.0, 11.2
fig, ax = bio.canvas(W, H)
x0, x1 = 0.3, W - 0.3
y = 3.2                                   # cytoplasmic membrane mid-plane
im_hi = y + M.LEAFLET + 0.02
om = im_hi + 2.3 + M.LEAFLET + 0.02       # outer membrane mid-plane
om_hi = om + M.LEAFLET + 0.02
top = om_hi + 2.3


def band(y0, y1, color):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=color, edgecolor="none", zorder=1))


band(0.3, y, P.fill("cytoplasm"))
band(y, om, M.periplasm_color())
band(om, top, P.fill("extracellular"))

xs = dict(porin=3.4, sym=8.6, abc=14.6, pts=20.6, sid=26.8)
tm_skip = [(8.1, 9.1), (13.75, 15.45), (20.1, 21.1), (25.95, 27.65), (24.0, 24.8)]
M.bilayer(ax, x0, x1, y, skip=tm_skip)
pg_top = M.peptidoglycan(ax, x0, x1, om - M.LEAFLET - 0.62, layers=1, spacing=0.3, seed=3)
om_skip = [(2.8, 4.0), (26.1, 27.5)]
M.leaflet(ax, x0, x1, om, -1, skip=om_skip)
k = 0
xx = x0 + 0.25
while xx < x1 - 0.2:
    if M._free(xx, [(a - 0.15, b + 0.15) for a, b in om_skip]):
        M.lps(ax, xx, om, o_units=(k % 3) + 1, seed=k)
    xx += 0.5
    k += 1

bio.label(ax, (0.6, top - 0.35), "Outside", size="small", ha="left", color=P.muted())
bio.label(ax, (0.6, y + 1.05), "Periplasm", size="small", ha="left", color=P.muted())
bio.label(ax, (0.6, 0.7), "Cytoplasm", size="small", ha="left", color=P.muted())


def title(x, a, b):
    bio.label(ax, (x, H - 0.45), a, size="small", bold=True)
    bio.label(ax, (x, H - 0.95), b, size="tiny", color=P.muted())


def down(x, ya, yb, **kw):
    bio.arrow(ax, (x, ya), (x, yb), kind="process", zorder=18, **kw)


# 1. porin
x = xs["porin"]
title(x, "Porin", "diffusion, < 600 Da")
M.porin(ax, x, om)
down(x, top - 0.6, y + 1.3)
bio.molecule(ax, (x + 0.55, top - 0.75), "carbohydrate", r=0.18)
bio.label(ax, (x, y + 0.9), "to inner-membrane\ntransporters", size="tiny", color=P.muted())

# 2. symporter
x = xs["sym"]
title(x, "Proton symporter", "LacY: lactose + H⁺")
M.transporter(ax, x, y, width=0.85, token="enzyme")
bio.label(ax, (x + 0.6, y - 0.75), "LacY", size="tiny", ha="left")
down(x - 0.22, om - 1.45, 1.3)
down(x + 0.22, om - 1.45, 1.3)
bio.molecule(ax, (x - 0.62, om - 1.55), "carbohydrate", text="Lac", r=0.26)
bio.ion(ax, (x + 0.6, om - 1.55), "h", r=0.15, text=False)
bio.label(ax, (x + 0.85, om - 1.55), "H⁺", size="tiny", ha="left")
bio.label(ax, (x, 0.75), "energy: proton-motive force", size="tiny", color=P.muted())

# 3. ABC transporter
x = xs["abc"]
title(x, "ABC transporter", "MalE + MalFG + MalK₂")
M.transporter(ax, x - 0.42, y, width=0.75, token="channel")
M.transporter(ax, x + 0.42, y, width=0.75, token="channel")
bio.label(ax, (x, y + 0.85), "MalFG", size="tiny", color=P.ink(), zorder=20)
bio.protein(ax, (x, y + 1.75), 1.5, 0.85, "receptor", text="MalE")
bio.molecule(ax, (x + 1.1, y + 1.6), "carbohydrate", text="Mal", r=0.26)
bio.protein(ax, (x - 0.45, y - 0.95), 0.85, 0.7, "atp", text="MalK")
bio.protein(ax, (x + 0.45, y - 0.95), 0.85, 0.7, "atp", text="MalK")
bio.label(ax, (x, y - 1.75), "2 ATP → 2 ADP + 2 Pᵢ", size="tiny")
down(x + 1.25, y - 0.3, 1.0, color=P.edge("carbohydrate"))
bio.label(ax, (x + 0.4, 0.65), "maltose (unchanged)", size="tiny", color=P.muted())

# 4. PTS
x = xs["pts"]
title(x, "Phosphotransferase system", "group translocation")
M.transporter(ax, x, y, width=0.9, token="protein")
bio.label(ax, (x, y), "EIIC", size="tiny", color=P.on_fill(), zorder=20)
bio.molecule(ax, (x - 0.65, om - 1.55), "carbohydrate", text="Glc", r=0.26)
down(x, om - 1.45, y + 0.75)
chain = [("EIIB", (x + 0.25, y - 1.0)), ("EIIA", (x + 1.55, y - 1.3)), ("HPr", (x + 2.3, y - 2.3)),
         ("EI", (x + 1.0, y - 2.55))]
for name, c in chain:
    bio.protein(ax, c, 1.0, 0.6, "protein", text=name, size="tiny")
pts = [c for _, c in chain]
bio.arrow(ax, (pts[3][0] + 0.5, pts[3][1] + 0.05), (pts[2][0] - 0.5, pts[2][1]), kind="process", head=0.15)
bio.arrow(ax, (pts[2][0] - 0.1, pts[2][1] + 0.3), (pts[1][0] + 0.15, pts[1][1] - 0.3), kind="process", head=0.15)
bio.arrow(ax, (pts[1][0] - 0.5, pts[1][1] + 0.05), (pts[0][0] + 0.5, pts[0][1] - 0.05), kind="process", head=0.15)
bio.label(ax, (x + 1.2, y - 3.05), "PEP → pyruvate", size="tiny")
bio.label(ax, (x + 2.05, y - 1.75), "~P", size="tiny", color=P.edge("negative"))
down(x - 0.45, y - 0.4, 1.0, color=P.edge("carbohydrate"))
bio.label(ax, (x - 0.55, 0.65), "glucose 6-P", size="tiny", color=P.muted())

# 5. siderophore
x = xs["sid"]
title(x, "Siderophore uptake", "TonB-dependent receptor + ABC")
M.porin(ax, x, om, width=1.3, token="receptor")
bio.label(ax, (x + 0.8, om - 0.75), "FepA", size="tiny", ha="left", zorder=21)
bio.molecule(ax, (x - 1.05, top - 0.85), "drug", text="Fe³⁺", r=0.3)
bio.label(ax, (x - 1.5, top - 0.85), "Fe–siderophore", size="tiny", ha="right", zorder=21)
down(x, top - 0.7, om - 1.25)
bio.protein(ax, (x, om - 1.6), 1.2, 0.6, "receptor", text="FepB", size="tiny")
M.transporter(ax, x - 0.4, y, width=0.75, token="channel")
M.transporter(ax, x + 0.4, y, width=0.75, token="channel")
bio.protein(ax, (x, y - 0.95), 1.3, 0.62, "atp", text="FepC₂", size="tiny")
down(x, y - 0.3, 1.0, color=P.edge("drug"))
# TonB-ExbB-ExbD
tx = 24.4
M.transporter(ax, tx, y, width=0.7, token="neutral")
ax.plot([tx, tx, x - 0.62], [y + 0.55, om - 0.55, om - 0.55], color=P.edge("neutral"), lw=2.0, zorder=13,
        solid_capstyle="round")
bio.label(ax, (tx - 0.35, (y + om) / 2 - 0.15), "TonB", size="tiny", ha="right")
bio.label(ax, (tx, y - 0.85), "ExbBD\n(pmf)", size="tiny", color=P.muted())
bio.label(ax, (x + 0.3, 0.65), "Fe³⁺ released by reduction", size="tiny", color=P.muted())
