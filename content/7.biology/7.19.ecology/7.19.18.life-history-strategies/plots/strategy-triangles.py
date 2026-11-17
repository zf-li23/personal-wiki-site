"""Two triangular classifications of life histories (schematic).

A: Grime's classification of plant habitats by the intensity of stress (shortage of light, water or
nutrients) and of disturbance (destruction of biomass): three habitat types select the competitive (C),
stress-tolerant (S) and ruderal (R) strategies; habitats with both severe stress and frequent
disturbance support no plants.
B: the CSR triangle: every plant is placed by the relative importance of the three strategies (ternary
coordinates); intermediate types CR, CS, SR and CSR lie between the corners.
C: Winemiller and Rose's triangle for fishes in the space of age at maturity, fecundity and juvenile
survival: opportunistic, periodic and equilibrium strategies at its corners.
"""

import numpy as np

import wikibio as bio

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(32.0, 11.0)

# A: 2 x 2 habitat table
x0, y0, w, h = 1.5, 1.6, 3.6, 3.3
cells = {
    (0, 1): ("Low stress\nhigh disturbance", "R: ruderals\n(weeds of arable land)", "highlight"),
    (1, 1): ("High stress\nhigh disturbance", "no viable strategy", "neutral"),
    (0, 0): ("Low stress\nlow disturbance", "C: competitors\n(tall clonal perennials)", "positive"),
    (1, 0): ("High stress\nlow disturbance", "S: stress tolerators\n(tundra, deserts)", "protein"),
}
for (i, j), (head, body, tok) in cells.items():
    bio.box(ax, (x0 + i * w + w / 2, y0 + j * h + h / 2), w - 0.15, h - 0.15, token=tok)
    bio.label(ax, (x0 + i * w + w / 2, y0 + j * h + h * 0.72), head, size="tiny", bold=True, color=P.on_fill())
    bio.label(ax, (x0 + i * w + w / 2, y0 + j * h + h * 0.32), body, size="tiny", color=P.on_fill())
bio.arrow(ax, (x0, y0 - 0.5), (x0 + 2 * w, y0 - 0.5), kind="process")
bio.label(ax, (x0 + w, y0 - 0.95), "stress", size="small")
bio.arrow(ax, (x0 - 0.5, y0), (x0 - 0.5, y0 + 2 * h), kind="process")
bio.label(ax, (x0 - 0.95, y0 + h), "disturbance", size="small", rotation=90)
bio.panel(ax, "A", (0.3, 10.4))
bio.label(ax, (1.5, 9.9), "Habitats (Grime)", size="small", bold=True, ha="left")

# B: CSR triangle
cx, base, side = 15.5, 1.6, 8.0
Cp = np.array([cx, base + side * np.sqrt(3) / 2])
Sp = np.array([cx + side / 2, base])
Rp = np.array([cx - side / 2, base])
tri = np.array([Cp, Sp, Rp, Cp])
ax.fill(tri[:, 0], tri[:, 1], color=P.fill("plant"), alpha=0.35, lw=0)
ax.plot(tri[:, 0], tri[:, 1], color=P.edge("plant"), lw=1.4)
for k in range(1, 3):
    f = k / 3
    for a, b_, c in [(Cp, Sp, Rp), (Sp, Rp, Cp), (Rp, Cp, Sp)]:
        p1 = a + f * (b_ - a)
        p2 = a + f * (c - a)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=P.muted(), lw=0.5, ls=(0, (2, 2)))
bio.label(ax, (Cp[0], Cp[1] + 0.45), "C  competitor", size="small", bold=True)
bio.label(ax, (Sp[0] + 0.2, Sp[1] - 0.5), "S  stress tolerator", size="small", bold=True)
bio.label(ax, (Rp[0] - 0.2, Rp[1] - 0.5), "R  ruderal", size="small", bold=True)
cen = (Cp + Sp + Rp) / 3
bio.label(ax, tuple(cen), "CSR", size="small")
for p, q, lab in [((Cp + Rp) / 2, None, "CR"), ((Cp + Sp) / 2, None, "CS"), ((Sp + Rp) / 2, None, "SR")]:
    off = (p - cen) / np.linalg.norm(p - cen) * 0.75
    bio.label(ax, tuple(p + off), lab, size="tiny")
bio.panel(ax, "B", (10.6, 10.4))
bio.label(ax, (11.5, 9.9), "The CSR triangle", size="small", bold=True, ha="left")

# C: Winemiller-Rose triangle
cx2 = 26.5
O = np.array([cx2 - 3.6, base + 2.6])
Pe = np.array([cx2 + 3.6, base + 2.6])
E = np.array([cx2, base + 6.2])
t2 = np.array([O, Pe, E, O])
ax.fill(t2[:, 0], t2[:, 1], color=P.fill("dna"), alpha=0.3, lw=0)
ax.plot(t2[:, 0], t2[:, 1], color=P.edge("dna"), lw=1.4)
for pt in (O, Pe, E):
    ax.plot(*pt, "o", ms=6, color=P.edge("dna"))
bio.label(ax, (O[0] - 0.3, O[1] - 0.5), "Opportunistic", size="small", bold=True, ha="left")
bio.label(ax, (O[0] - 0.3, O[1] - 0.9), "early maturity, small clutches,\nlow juvenile survival;\nsmall short-lived fishes",
          size="tiny", ha="left", va="top")
bio.label(ax, (Pe[0] + 0.3, Pe[1] - 0.5), "Periodic", size="small", bold=True, ha="right")
bio.label(ax, (Pe[0] + 0.3, Pe[1] - 0.9), "late maturity, very high fecundity,\nlow juvenile survival;\ncod, sturgeons",
          size="tiny", ha="right", va="top")
bio.label(ax, (E[0], E[1] + 1.55), "Equilibrium", size="small", bold=True)
bio.label(ax, (E[0], E[1] + 0.3), "late maturity, few large young,\nhigh juvenile survival, care;\nlivebearing sharks",
          size="tiny", va="bottom")
bio.panel(ax, "C", (21.2, 10.4))
bio.label(ax, (22.0, 9.9), "Fish life histories (Winemiller-Rose)", size="small", bold=True, ha="left")
