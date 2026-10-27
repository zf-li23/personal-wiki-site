"""The plant cell wall and its growth (schematic, not to scale; model values illustrative).

A: the primary wall in face view: two lamellae of cellulose microfibrils at right angles, tethered by
cross-linking glycans (hemicelluloses such as xyloglucan) and embedded in a hydrated pectin gel.
B: walls in section between two cells: the pectin-rich middle lamella cements the primary walls of the two
cells; the lower cell has stopped growing and deposited a secondary wall in three layers (S1, S2, S3) with
different microfibril orientations. Cellulose synthase complexes in the plasma membrane spin microfibrils
into the wall while moving along cortical microtubules beneath the membrane.
C: a plasmodesma: the plasma membrane lines a channel through the wall, the desmotubule (appressed ER)
joins the ER of both cells, and the cytoplasmic sleeve between them carries small molecules; callose
deposited at the necks narrows the channel. D: the Lockhart model of cell expansion: the relative growth
rate (1/V) dV/dt = phi (P - Y) when the turgor pressure P exceeds the yield threshold Y of the wall, and zero
below it. Wall loosening (acid growth, expansins) raises the extensibility phi and lowers Y: here
phi = 0.1 to 0.3 per h per MPa and Y = 0.3 to 0.2 MPa.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(30.0, 12.4)

bio.panel(ax, "A", (0.1, 12.3))
f = J.wall_face(ax, 0.6, 5.6, 5.8, 5.8, spacing=0.62)
bio.callout(ax, f["microfibril"], (6.9, 5.0), "Cellulose microfibril", size="tiny")
bio.callout(ax, f["glycan"], (0.4, 5.0), "Cross-linking glycan", size="tiny")
bio.callout(ax, f.get("pectin", f["glycan"]), (3.5, 4.75), "Pectin", size="tiny")

bio.panel(ax, "B", (7.6, 12.3))
s = J.wall_section(ax, 8.2, 15.6, 9.0, primary=0.55, secondary=(0.3, 0.9, 0.25), lamella=0.3, csc=3)
lab = (("lamella", "Middle lamella"), ("primary2", "Primary wall (cell 2)"), ("primary", "Primary wall (cell 1)"),
       ("S1", "S1"), ("S2", "S2   secondary wall"), ("S3", "S3"), ("csc", "Cellulose synthase complex"),
       ("microtubule", "Cortical microtubule"))
ys = (9.0, 10.4, 8.4, 7.75, 7.15, 6.55, 5.3, 4.6)
for (key, txt), y in zip(lab, ys):
    p = s[key]
    if key in ("csc", "microtubule"):
        bio.callout(ax, p, (16.2, y), txt, size="tiny")
    else:
        bio.callout(ax, (15.2, p[1]), (16.2, y), txt, size="tiny")
bio.label(ax, (8.3, 11.2), "Cell 2", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.3, s["bottom"] - 1.3), "Cell 1 (cytoplasm)", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "C", (0.1, 4.4))
c = J.plasmodesma(ax, (4.4, 2.1), wall=1.0, length=6.4, width=0.5)
bio.callout(ax, c["desmotubule"], (2.6, 4.2), "Desmotubule (ER)", size="tiny")
bio.callout(ax, c["sleeve"], (6.6, 4.2), "Cytoplasmic sleeve", size="tiny")
bio.callout(ax, c["callose"], (7.4, 3.5), "Callose", size="tiny")
bio.callout(ax, c["membrane"], (1.1, 3.4), "Plasma membrane", size="tiny")
bio.callout(ax, c["wall"] + np.array([0, -2.8]), (7.8, 0.6), "Wall", size="tiny")

bio.panel(ax, "D", (21.2, 12.3))
pd = charts.axes_at(ax, (22.8, 4.6, 6.6, 6.8))
Pp = np.linspace(0, 0.8, 300)
for phi, Y, tk, name in ((0.1, 0.3, "neutral", "wall before loosening"), (0.3, 0.2, "plant", "after acid loosening (expansins)")):
    rate = np.where(Pp > Y, phi * (Pp - Y), 0.0)
    pd.plot(Pp, rate, color=quant.line_color(tk), lw=2.2, label=name)
    pd.axvline(Y, color=quant.line_color(tk), lw=0.8, ls=(0, (2, 2)))
pd.text(0.305, 0.135, "Y", fontsize=bio.core.FONT["tiny"], color=P.ink())
pd.text(0.205, 0.135, "Y'", fontsize=bio.core.FONT["tiny"], color=P.ink())
pd.set_xlim(0, 0.8)
pd.set_ylim(0, 0.2)
pd.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pd, "turgor pressure P / MPa", "relative growth rate / h$^{-1}$")
charts.title(pd, "Lockhart: growth needs P > Y")
bio.label(ax, (26.1, 2.6), r"$\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \varphi\,(P - Y)$", size="normal")
