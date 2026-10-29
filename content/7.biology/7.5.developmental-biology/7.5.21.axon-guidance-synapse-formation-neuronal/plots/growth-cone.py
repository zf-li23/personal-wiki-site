"""The growth cone. (A) Structure: microtubules of the axon shaft end in the central domain, with a few exploring
the periphery; the peripheral domain is a lamellipodial veil filled with branched actin, from which filopodia
(bundled actin) extend. (B) The clutch model: actin polymerizes at the leading edge and is pulled back by myosin II
(retrograde flow); when adhesion molecules bind the substrate and engage the actin (the clutch), the flow is
slowed and polymerization pushes the membrane forward. (C) Turning: on the side of the cone facing an attractant
(for example netrin acting through DCC), Rac and Cdc42 are activated, adhesion engages and the cone advances, so
it turns towards the source; a repellent (Slit through Robo, semaphorin through plexin, ephrin through Eph)
activates RhoA and disengages the clutch on its side, so the cone turns away or, if the signal is uniform, collapses."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N
from matplotlib.patches import Circle

fig, ax = bio.canvas(25, 8.6)
P = bio.P
bio.panel(ax, "A", (0.2, 8.4))
g = N.growth_cone(ax, (6.6, 4.4), angle=0, size=2.4, shaft=3.6, filopodia=8)
bio.callout(ax, g["central"], (3.6, 7.4), "central domain (microtubules)")
bio.callout(ax, g["peripheral"], (5.0, 1.0), "peripheral domain (actin veil)")
bio.callout(ax, g["filopodia"][-1], (7.6, 7.9), "filopodia")
bio.callout(ax, g["shaft"], (1.0, 3.0), "axon shaft")

# (B) clutch model
bio.panel(ax, "B", (9.6, 8.4))
y0 = 2.0
ax.plot([10.0, 16.2], [y0, y0], color=P.edge("extracellular"), lw=3.0)
bio.label(ax, (13.1, y0 - 0.45), "substrate (laminin, cell surfaces)", size="tiny", color=P.muted())
ax.plot([15.9, 15.9], [y0 + 0.4, y0 + 4.4], color=P.edge("membrane"), lw=2.2)
bio.label(ax, (16.25, y0 + 4.6), "leading edge", size="tiny", color=P.muted(), ha="left")
for k in range(5):
    y = y0 + 1.0 + 0.7 * k
    ax.plot([11.0, 15.8], [y, y], color=P.edge("actin"), lw=2.0)
    for x in np.arange(11.2, 15.8, 0.35):
        ax.add_patch(Circle((x, y), 0.09, facecolor=P.fill("actin"), edgecolor=P.edge("actin"), lw=0.4))
bio.arrow(ax, (15.3, y0 + 4.2), (12.0, y0 + 4.2), kind="process", lw=1.4, head=0.16)
bio.label(ax, (13.6, y0 + 4.55), "retrograde flow", size="tiny")
bio.box(ax, (11.4, y0 + 2.4), 0.8, 2.6, token="myosin", text="", radius=0.15)
bio.label(ax, (11.4, y0 + 2.4), "myosin II", size="tiny", rotation=90, color=P.on_fill())
for x in (13.0, 14.4):
    ax.plot([x, x], [y0, y0 + 1.0], color=P.edge("receptor"), lw=2.4)
    ax.add_patch(Circle((x, y0 + 1.0), 0.15, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.8))
bio.label(ax, (13.7, y0 + 0.55), "clutch", size="tiny", color=P.edge("receptor"))
bio.label(ax, (15.55, y0 + 3.5), "+", size="small", bold=True)
bio.label(ax, (13.0, 7.7), "polymerization at the + ends pushes", size="tiny", color=P.muted())
bio.label(ax, (13.0, 7.3), "the edge forward when the clutch holds", size="tiny", color=P.muted())

# (C) turning in gradients
bio.panel(ax, "C", (17.2, 8.4))
rng = np.random.default_rng(3)
for k in range(160):
    x = rng.uniform(17.6, 24.8)
    p = (x - 17.6) / 7.2
    if rng.random() < p ** 1.6:
        ax.add_patch(Circle((x, rng.uniform(5.0, 7.8)), 0.05, color=P.fill("positive"), zorder=2))
    if rng.random() < p ** 1.6:
        ax.add_patch(Circle((x, rng.uniform(0.8, 3.6)), 0.05, color=P.fill("negative"), zorder=2))
ga = N.growth_cone(ax, (21.5, 6.9), angle=25, size=1.1, shaft=2.2, filopodia=6, seed=1)
gr = N.growth_cone(ax, (20.3, 1.2), angle=-70, size=1.1, shaft=2.2, filopodia=6, seed=2)
bio.label(ax, (23.6, 7.95), "attractant", size="small", color=P.edge("positive"))
bio.label(ax, (23.6, 4.35), "netrin/DCC: Rac, Cdc42, Ca2+", size="tiny", color=P.muted())
bio.label(ax, (23.6, 3.85), "repellent", size="small", color=P.edge("negative"))
bio.label(ax, (23.6, 0.35), "Slit, Sema, ephrin: RhoA", size="tiny", color=P.muted())
