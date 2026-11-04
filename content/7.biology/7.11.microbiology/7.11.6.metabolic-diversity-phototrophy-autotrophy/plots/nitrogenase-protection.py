"""Three ways to keep oxygen away from nitrogenase while living in air.

A: heterocyst of a filamentous cyanobacterium (Anabaena). Vegetative cells split water (PSII) and fix CO2;
sugar (sucrose) moves into the heterocyst, which lacks PSII, keeps PSI for ATP, has an extra glycolipid and
polysaccharide envelope that slows O2 entry and respires the O2 that leaks in; glutamine returns.
B: Azotobacter: very high rates of respiration at the cell membrane consume O2 before it reaches
nitrogenase (respiratory protection); a thick capsule slows diffusion, and on a sudden O2 shock the FeSII
(Shethna) protein binds nitrogenase into an inactive, O2-protected complex (conformational protection).
C: legume root nodule: rhizobia live as bacteroids inside symbiosomes of infected plant cells; leghemoglobin
binds O2 with high affinity and delivers it to the bacteroids' high-affinity terminal oxidase while
keeping free O2 in the nanomolar range.
"""
import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import microbio as Mi

P = bio.P
fig, ax = bio.canvas(30.0, 12.4, scale=0.42)


def ell(c, w, h, token, lw=1.3, z=5, edge=None, fill=True):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.fill(token) if fill else "none", edgecolor=P.edge(edge or token),
                         lw=lw, zorder=z))


def o2(xy, size="tiny"):
    bio.label(ax, xy, "O₂", size=size, color=P.edge("dna"), bold=True)


# A: heterocyst ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 12.2))
bio.label(ax, (5.3, 11.8), "Heterocyst ($\\it{Anabaena}$)", size="small", bold=True)
xs = [1.4, 3.0, 5.4, 7.8, 9.4]
for i, x in enumerate(xs):
    if i == 2:
        ell((x, 6.8), 2.5, 2.1, "highlight", lw=1.0, z=4, edge="atp")
        ell((x, 6.8), 2.0, 1.6, "lipid", lw=1.0, z=5, edge="atp")
        bio.label(ax, (x, 7.2), "nitrogenase", size="tiny", color=P.on_fill())
        bio.label(ax, (x, 6.5), "PSI only", size="tiny", color=P.on_fill())
    else:
        ell((x, 6.8), 1.5, 1.3, "enzyme", lw=1.2)
bio.callout(ax, (5.4 + 1.2, 7.3), (8.6, 9.9), "thick glycolipid +\npolysaccharide envelope", size="tiny")
bio.label(ax, (2.2, 9.6), "vegetative cells:\nPSII + PSI, CO₂ fixation", size="tiny")
for x in (1.4, 3.0, 7.8, 9.4):
    bio.arrow(ax, (x, 7.5), (x, 8.6), kind="process", color=P.edge("dna"), lw=1.1)
    o2((x, 8.9))
bio.arrow(ax, (3.6, 6.3), (4.3, 6.3), kind="process", color=P.edge("carbohydrate"), lw=1.3)
bio.arrow(ax, (4.3, 7.4), (3.6, 7.4), kind="process", color=P.edge("receptor"), lw=1.3)
bio.label(ax, (3.6, 5.3), "sucrose in", size="tiny", color=P.edge("carbohydrate"))
bio.label(ax, (4.5, 8.2), "glutamine out", size="tiny", color=P.edge("receptor"))
bio.label(ax, (5.4, 3.6), "no O₂ evolution; O₂ that leaks in\nis respired", size="tiny", color=P.muted())

# B: Azotobacter ---------------------------------------------------------------------------------
bio.panel(ax, "B", (10.8, 12.2))
bio.label(ax, (15.4, 11.8), "Respiratory protection ($\\it{Azotobacter}$)", size="small", bold=True)
cB = (15.4, 6.6)
ell(cB, 6.4, 5.2, "extracellular", lw=1.0, z=3, edge="carbohydrate")
ell(cB, 4.4, 3.4, "cytoplasm", lw=1.6, z=4, edge="membrane")
bio.label(ax, (cB[0], cB[1] + 0.3), "nitrogenase", size="small")
bio.label(ax, (cB[0], cB[1] - 0.5), "+ FeSII (O₂ shock)", size="tiny", color=P.muted())
for ang in np.linspace(20, 340, 7):
    a = np.radians(ang)
    p_out = (cB[0] + 3.9 * np.cos(a), cB[1] + 3.2 * np.sin(a))
    p_mem = (cB[0] + 2.25 * np.cos(a), cB[1] + 1.75 * np.sin(a))
    bio.arrow(ax, p_out, p_mem, kind="process", color=P.edge("dna"), lw=1.0, shrink=0.05)
    ax.add_patch(Ellipse(p_mem, 0.42, 0.42, facecolor=P.fill("mitochondrion"), edgecolor=P.edge("mitochondrion"), lw=0.8, zorder=8))
o2((cB[0] - 3.9, cB[1] + 2.4), size="small")
bio.callout(ax, (cB[0] + 2.2 * np.cos(np.radians(20)), cB[1] + 1.75 * np.sin(np.radians(20))), (17.6, 10.6),
            "terminal oxidases:\nO₂ → H₂O at the membrane", size="tiny")
bio.callout(ax, (cB[0] - 2.6, cB[1] - 2.0), (12.0, 2.6), "capsule (slime)", size="tiny")
bio.label(ax, (cB[0] + 0.6, 2.6), "respiration rate rises with pO₂", size="tiny", color=P.muted())

# C: root nodule ---------------------------------------------------------------------------------
bio.panel(ax, "C", (21.0, 12.2))
bio.label(ax, (25.6, 11.8), "Legume root nodule cell", size="small", bold=True)
cC = (25.6, 6.6)
bio.box(ax, cC, 7.6, 7.0, token="plant", radius=0.6, zorder=3)
bio.box(ax, cC, 7.0, 6.4, token="cytoplasm", radius=0.5, zorder=4)
rng = np.random.default_rng(3)
for (x, y) in [(23.6, 8.4), (25.6, 8.6), (27.6, 8.3), (23.4, 6.4), (27.8, 6.2), (23.8, 4.5), (25.8, 4.3), (27.6, 4.6)]:
    ell((x, y), 1.6, 1.0, "vesicle", lw=0.9, z=6)
    Mi.bacillus(ax, (x, y), 1.1, 0.42, gram="-", zorder=7)
for _ in range(26):
    x, y = rng.uniform(22.4, 28.8), rng.uniform(3.6, 9.6)
    ax.add_patch(Ellipse((x, y), 0.18, 0.18, color=P.fill("blood"), zorder=9))
bio.label(ax, (cC[0], 6.5), "leghemoglobin\n(free O₂ ≈ nM)", size="tiny", color=P.edge("blood"))
bio.callout(ax, (27.6 + 0.55, 8.3), (29.4, 10.6), "bacteroid in\nsymbiosome", size="tiny")
bio.label(ax, (cC[0], 2.3), "plant supplies dicarboxylates,\nbacteroid returns NH₃", size="tiny", color=P.muted())
