# Principal transport proteins of the plasma membrane (top) and tonoplast (bottom) of a root cortical cell.
# Plasma membrane: the P-type H+-ATPase pumps H+ out (1 H+ per ATP) and sets up V_m = -120 to -200 mV and a pH
# gradient (apoplast pH 5.5, cytosol 7.2); K+ enters through inward-rectifying channels (AKT1) or high-affinity
# H+-coupled carriers (HAK5); nitrate and phosphate enter by H+ symport (NRT1/NRT2, PHT1); NH4+ through AMT
# transporters (down its gradient); Na+ is exported by the Na+/H+ antiporter SOS1; Ca2+ enters through channels
# and is pumped out by a Ca2+-ATPase. Tonoplast: the V-type H+-ATPase (2 H+ per ATP) and the H+-pyrophosphatase
# (1 H+ per PPi) acidify the vacuole (pH 5.5, lumen about 20-30 mV positive to the cytosol); antiporters use this
# gradient to load Na+ (NHX) and Ca2+ (CAX); anions (NO3-, Cl-, malate) enter through channels, K+ moves through
# TPK channels.
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(27.0, 13.4)
yp, yt = 9.4, 3.6
CB.sides(ax, (0.2, 26.8), yp, height=(3.1, 2.55), top="Apoplast  pH 5.5", bottom="Cytosol  pH 7.2",
         label_x=0.4)
CB.sides(ax, (0.2, 26.8), yt, height=(2.45, 2.7), top=None, bottom="Vacuole  pH 5.5", top_token="cytoplasm",
         bottom_token="vacuole", label_x=24.7)
bio.bilayer(ax, [(0.2, yp), (26.8, yp)])
bio.bilayer(ax, [(0.2, yt), (26.8, yt)])
bio.label(ax, (26.6, yp + 0.75), "plasma membrane", size="tiny", ha="right", color=P.muted())
bio.label(ax, (26.6, yt + 0.75), "tonoplast", size="tiny", ha="right", color=P.muted())
bio.label(ax, (13.5, 6.55), "$V_{\\mathrm{m}}$ = −120 to −200 mV (cytosol negative)", size="small", color=P.muted())

ION = {"H⁺": "h", "K⁺": "k", "Na⁺": "na", "Ca²⁺": "ca", "Cl⁻": "cl"}


def flow(x, y0, y1, text, ion=None, side=1):
    bio.arrow(ax, (x, y0), (x, y1), kind="process", zorder=16)
    yy = y0 + (0.15 if y1 < y0 else -0.15)
    tx = x + side * 0.28
    if ion in ION:
        bio.ion(ax, (tx + side * 0.05, y0), ION[ion], r=0.15, text=False, zorder=17)
        bio.label(ax, (tx + side * 0.32, y0), text, size="tiny", ha="left" if side > 0 else "right")
    else:
        bio.label(ax, (tx, y0), text, size="tiny", ha="left" if side > 0 else "right")


def title(x, y, a, b=None):
    bio.label(ax, (x, y), a, size="small", bold=True)
    if b:
        bio.label(ax, (x, y - 0.38), b, size="tiny", color=P.muted())


up, dn = yp - 1.55, yp + 1.55  # positions above/below the plasma membrane
# --- plasma membrane
x = 2.6
atp = CB.pump(ax, x, yp, width=1.6, token="enzyme")
flow(x - 0.4, up, dn, "H⁺", "H⁺", side=-1)
bio.molecule(ax, atp + (0.2, 0.1), token="atp", text="ATP", r=0.27, size=5.0)
title(x, 11.8, "H⁺-ATPase", "P-type, 1 H⁺/ATP")

x = 5.8
CB.channel(ax, x, yp)
flow(x, dn, up, "K⁺", "K⁺")
title(x, 11.8, "K⁺ channel", "AKT1 (inward)")

x = 8.9
CB.carrier(ax, x, yp, open="out", token="receptor", width=1.45)
flow(x - 0.32, dn, up, "2 H⁺", "H⁺", side=-1)
flow(x + 0.32, dn, up, "NO₃⁻")
title(x, 11.8, "NO₃⁻/H⁺ symporter", "NRT1, NRT2")

x = 12.1
CB.carrier(ax, x, yp, open="out", token="metabolite", width=1.45)
flow(x - 0.32, dn, up, "H⁺", "H⁺", side=-1)
flow(x + 0.32, dn, up, "H₂PO₄⁻")
title(x, 11.8, "Pi/H⁺ symporter", "PHT1")

x = 15.2
CB.carrier(ax, x, yp, open="out", token="carbohydrate", width=1.25)
flow(x, dn, up, "NH₄⁺")
title(x, 11.8, "NH₄⁺ transporter", "AMT1")

x = 18.3
CB.carrier(ax, x, yp, open="out", token="drug", width=1.45)
flow(x - 0.32, dn, up, "H⁺", "H⁺", side=-1)
flow(x + 0.32, up, dn, "Na⁺", "Na⁺")
title(x, 11.8, "Na⁺/H⁺ antiporter", "SOS1")

x = 21.4
CB.channel(ax, x, yp, token="ca")
flow(x, dn, up, "Ca²⁺", "Ca²⁺")
title(x, 11.8, "Ca²⁺ channel")

x = 24.4
atp2 = CB.pump(ax, x, yp, width=1.5, token="antibody")
flow(x - 0.38, up, dn, "Ca²⁺", "Ca²⁺", side=-1)
bio.molecule(ax, atp2 + (0.2, 0.1), token="atp", text="ATP", r=0.27, size=5.0)
title(x, 11.8, "Ca²⁺-ATPase", "ACA")

# --- tonoplast (cytosol above, vacuole below): "into vacuole" is downward
cu, vd = yt + 1.5, yt - 1.5
x = 3.0
from matplotlib.patches import Ellipse  # noqa: E402
ax.add_patch(Ellipse((x, yt), 1.8, 1.05, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=1.2, zorder=12))
for k in range(5):
    xx = x - 0.6 + 0.3 * k
    ax.plot([xx, xx], [yt - 0.37, yt + 0.37], color=P.light("channel"), lw=1.8, zorder=12.5)
bio.molecule(ax, (x + 1.25, yt + 1.0), token="atp", text="ATP", r=0.27, size=5.0)
flow(x - 1.15, cu, vd, "2 H⁺", "H⁺", side=-1)
title(x, 0.75, "V-ATPase", "rotary, 2 H⁺/ATP")

x = 7.0
CB.carrier(ax, x, yt, open="in", token="enzyme", width=1.3)
bio.molecule(ax, (x + 0.95, yt + 1.0), token="metabolite", text="PPi", r=0.27, size=5.0)
flow(x - 0.25, cu, vd, "H⁺", "H⁺", side=-1)
title(x, 0.75, "H⁺-PPase", "1 H⁺/PPi")

x = 11.0
CB.carrier(ax, x, yt, open="in", token="drug", width=1.45)
flow(x - 0.32, vd, cu, "H⁺", "H⁺", side=-1)
flow(x + 0.32, cu, vd, "Na⁺", "Na⁺")
title(x, 0.75, "Na⁺/H⁺ antiporter", "NHX1")

x = 15.0
CB.carrier(ax, x, yt, open="in", token="antibody", width=1.45)
flow(x - 0.32, vd, cu, "H⁺", "H⁺", side=-1)
flow(x + 0.32, cu, vd, "Ca²⁺", "Ca²⁺")
title(x, 0.75, "Ca²⁺/H⁺ antiporter", "CAX")

x = 19.0
CB.channel(ax, x, yt, token="cl")
flow(x, cu, vd, "NO₃⁻, Cl⁻, malate")
title(x, 0.75, "anion channels")

x = 23.2
CB.channel(ax, x, yt, token="k")
flow(x, cu, vd, "K⁺", "K⁺")
title(x, 0.75, "K⁺ channel", "TPK")
