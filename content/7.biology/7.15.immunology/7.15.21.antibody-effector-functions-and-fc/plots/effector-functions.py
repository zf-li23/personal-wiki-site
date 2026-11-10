# Five effector mechanisms of antibodies. The Fab arms give specificity; the Fc decides what happens next.
# A neutralization (Fab only: blocks attachment of a virus or toxin to its host receptor);
# B opsonization (IgG Fc bound by activating FcγR on a macrophage triggers phagocytosis);
# C complement activation (clustered Fc bind C1q: classical pathway, C3b deposition, membrane attack);
# D ADCC (IgG on a target cell is bound by FcγRIIIA, CD16, on an NK cell, which releases perforin and granzymes);
# E IgE held by FcεRI on a mast cell is cross-linked by a multivalent antigen, triggering degranulation.
import math

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(30, 8.6)
W = 6.0


def title(i, letter, text):
    x = i * W
    bio.panel(ax, letter, (x + 0.1, 8.45))
    bio.label(ax, (x + W / 2, 8.1), text, size="small")


def ab(xy, angle, size=0.55):
    bio.antibody(ax, xy, size=size, angle=angle)


# A neutralization
title(0, "A", "Neutralization")
ax.plot([0.4, 5.6], [1.2, 1.2], color=P.edge("membrane"), lw=3, zorder=3)
bio.label(ax, (3.0, 0.65), "host cell", size="tiny", color=P.muted())
for x in (1.6, 4.4):
    ax.plot([x, x], [1.2, 1.9], color=P.edge("receptor"), lw=2.2, zorder=4)
    bio.protein(ax, (x, 2.05), 0.45, 0.32, "receptor")
v = (3.0, 4.6)
bio.virus(ax, v, 0.75, kind="enveloped")
for a in (0, 60, 120, 180, 240, 300):
    th = math.radians(a)
    ab((v[0] + 1.35 * math.cos(th), v[1] + 1.35 * math.sin(th)), a - 90 + 180)
bio.arrow(ax, (3.0, 3.25), (3.0, 2.4), kind="inhibition")
bio.label(ax, (3.0, 6.9), "Fab blocks the attachment\nprotein: no entry", size="tiny")

# B opsonization
title(1, "B", "Opsonization")
mac = (W + 2.2, 3.4)
immuno.immune_cell(ax, mac, r=1.55, kind="dendritic", token="neutral", seed=3)
bio.label(ax, (mac[0], 1.0), "macrophage (FcγRI, FcγRIIA)", size="tiny")
bac = (W + 4.6, 4.6)
bio.shape(ax, bio.blob(bac, 0.75, 0.45, wobble=0.03, seed=2), "bacterium", zorder=8)
for a in (90, 150, 210, 30, -30):
    th = math.radians(a)
    ab((bac[0] + 1.1 * math.cos(th), bac[1] + 0.85 * math.sin(th)), a - 90 + 180, size=0.45)
bio.arrow(ax, (bac[0] - 1.1, bac[1] - 0.4), (mac[0] + 1.0, mac[1] + 0.3), kind="process")
bio.label(ax, (W + 3.6, 6.9), "Fc bound by FcγR:\nphagocytosis, killing", size="tiny")

# C complement
title(2, "C", "Complement activation")
x0 = 2 * W
bio.shape(ax, bio.blob((x0 + 3.0, 2.4), 2.4, 0.9, wobble=0.02, seed=5), "bacterium", zorder=5)
for k, x in enumerate((x0 + 2.0, x0 + 2.7, x0 + 3.4, x0 + 4.1)):
    ab((x, 3.75), 180, size=0.45)
c1q = (x0 + 3.05, 4.35)
bio.protein(ax, c1q, 1.4, 0.5, "drug", text="C1q")
bio.label(ax, (x0 + 3.0, 6.4), "≥ 2 adjacent Fc (IgG hexamer\nor one bound IgM) bind C1q", size="tiny")
for x in (x0 + 1.4, x0 + 4.6):
    bio.protein(ax, (x, 2.4), 0.45, 0.35, "enzyme", text="C3b")
bio.label(ax, (x0 + 3.0, 0.7), "C3b opsonizes; C5b–9 (MAC) lyses", size="tiny")

# D ADCC
title(3, "D", "ADCC")
x0 = 3 * W
tgt = (x0 + 1.7, 3.6)
bio.shape(ax, bio.blob(tgt, 1.2, 1.5, wobble=0.04, seed=8), "virus", zorder=5)
bio.label(ax, (tgt[0], 1.4), "infected or\ntumor cell", size="tiny")
nk = (x0 + 4.4, 3.6)
immuno.immune_cell(ax, nk, r=1.1, token="positive", seed=9)
bio.label(ax, (nk[0], 1.9), "NK cell (CD16)", size="tiny")
for y in (2.8, 3.6, 4.4):
    ab((x0 + 3.05, y), 90, size=0.42)
for k in range(5):
    bio.protein(ax, (x0 + 2.95 + 0.05 * (k % 2), 3.2 + 0.2 * k), 0.13, 0.13, "negative")
bio.label(ax, (x0 + 3.0, 6.9), "perforin + granzymes:\ntarget apoptosis", size="tiny")

# E mast cell
title(4, "E", "Mast-cell activation")
x0 = 4 * W
mc = (x0 + 3.0, 2.6)
bio.shape(ax, bio.blob(mc, 2.4, 1.6, wobble=0.03, seed=11), "neutral", zorder=4)
rng = np.random.default_rng(1)
for k in range(14):
    g = (mc[0] + rng.uniform(-1.8, 1.8), mc[1] + rng.uniform(-1.0, 0.6))
    ax.add_patch(Circle(g, 0.14, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.7, zorder=6))
for x in (x0 + 2.2, x0 + 3.8):
    ab((x, 4.45), 0, size=0.5)
allergen = (x0 + 3.0, 5.0)
bio.protein(ax, allergen, 2.3, 0.45, "carbohydrate", text="antigen")
bio.label(ax, (x0 + 3.0, 7.0), "cross-linked IgE–FcεRI:\nhistamine, mediators", size="tiny")
