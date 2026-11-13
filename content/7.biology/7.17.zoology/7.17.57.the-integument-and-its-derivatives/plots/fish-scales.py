# The scales of fishes in vertical section, schematic (surface up, anterior to the left), after Sire et al.
# (2009), Kardong (2019) and Romer & Parsons. Panels: placoid scale of a shark; cosmoid scale of an early
# sarcopterygian; palaeoniscoid ganoid scale (bichirs, early actinopterygians); lepisosteoid ganoid scale (gars);
# elasmoid scales of a teleost, overlapping in dermal pockets, the last with ctenii (ctenoid). Tissues share one
# colour key across panels. Not to scale.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 9.5)
TOK = {"enamel": "highlight", "dentine": "carbohydrate", "cosmine": "protein", "spongy": "lipid_tail",
       "bone": "bone", "plywood": "metabolite", "epidermis": "ectoderm", "dermis": "mesoderm"}


def layer(pts, key, z=5):
    bio.shape(ax, pts, token=TOK[key], zorder=z)


def bg(x0, w):
    bio.shape(ax, [(x0, 1.2), (x0 + w, 1.2), (x0 + w, 4.0), (x0, 4.0)], token=TOK["dermis"], zorder=1, lw=0.6)
    bio.shape(ax, [(x0, 4.0), (x0 + w, 4.0), (x0 + w, 4.5), (x0, 4.5)], token=TOK["epidermis"], zorder=1, lw=0.6)


titles = ["Placoid", "Cosmoid", "Ganoid (palaeoniscoid)", "Ganoid (lepisosteoid)", "Elasmoid (cycloid / ctenoid)"]
xs = [0.4, 6.3, 12.2, 18.1, 24.0]
W = 5.5
for x0, t in zip(xs, titles):
    bio.label(ax, (x0 + W / 2, 8.9), t, size="small", bold=True)

# placoid: basal plate in dermis, spine through epidermis
x0 = xs[0]
bg(x0, W)
layer([(x0 + 1.0, 2.4), (x0 + 4.4, 2.4), (x0 + 4.0, 3.2), (x0 + 1.4, 3.2)], "bone")
layer([(x0 + 1.6, 3.2), (x0 + 3.8, 3.2), (x0 + 4.9, 6.2), (x0 + 3.4, 5.4)], "dentine", z=6)
layer([(x0 + 3.4, 5.4), (x0 + 4.9, 6.2), (x0 + 4.4, 5.2)], "enamel", z=7)
bio.shape(ax, [(x0 + 2.4, 3.0), (x0 + 3.2, 3.0), (x0 + 3.9, 5.0), (x0 + 3.5, 4.8)], token="neutral", zorder=8, lw=0.6)
bio.callout(ax, (x0 + 3.5, 4.2), (x0 + 0.9, 6.7), "pulp cavity", size="tiny")
bio.callout(ax, (x0 + 4.6, 5.8), (x0 + 4.4, 7.6), "enameloid", size="tiny")
bio.callout(ax, (x0 + 2.0, 2.7), (x0 + 0.9, 0.5), "basal plate", size="tiny")

# cosmoid: thick, four layers, pore canals
x0 = xs[1]
bg(x0, W)
layer([(x0 + 0.5, 1.6), (x0 + 5.0, 1.6), (x0 + 5.0, 2.5), (x0 + 0.5, 2.5)], "bone")
layer([(x0 + 0.5, 2.5), (x0 + 5.0, 2.5), (x0 + 5.0, 3.5), (x0 + 0.5, 3.5)], "spongy")
layer([(x0 + 0.5, 3.5), (x0 + 5.0, 3.5), (x0 + 5.0, 4.6), (x0 + 0.5, 4.6)], "cosmine")
layer([(x0 + 0.5, 4.6), (x0 + 5.0, 4.6), (x0 + 5.0, 4.85), (x0 + 0.5, 4.85)], "enamel")
for k in range(6):
    xx = x0 + 0.9 + 0.75 * k
    ax.plot([xx, xx, xx + 0.15], [3.6, 4.85, 4.85], color=P.ink(), lw=0.8, zorder=9)
bio.callout(ax, (x0 + 1.65, 4.3), (x0 + 1.0, 6.4), "pore canals", size="tiny")

# palaeoniscoid ganoid: ganoine layers, dentine, bone; rhombic
x0 = xs[2]
bg(x0, W)
layer([(x0 + 0.7, 2.0), (x0 + 4.8, 2.0), (x0 + 4.4, 3.1), (x0 + 1.1, 3.1)], "bone")
layer([(x0 + 1.1, 3.1), (x0 + 4.4, 3.1), (x0 + 4.25, 3.6), (x0 + 1.25, 3.6)], "dentine")
for k in range(5):
    y = 3.6 + 0.2 * k
    layer([(x0 + 1.25 + 0.04 * k, y), (x0 + 4.25 - 0.04 * k, y), (x0 + 4.21 - 0.04 * k, y + 0.2),
           (x0 + 1.29 + 0.04 * k, y + 0.2)], "enamel", z=6 + k)
bio.callout(ax, (x0 + 2.7, 4.3), (x0 + 1.0, 6.4), "ganoine (layered)", size="tiny")

# lepisosteoid: ganoine on bone
x0 = xs[3]
bg(x0, W)
layer([(x0 + 0.7, 2.2), (x0 + 4.8, 2.2), (x0 + 4.4, 3.5), (x0 + 1.1, 3.5)], "bone")
for k in range(5):
    y = 3.5 + 0.2 * k
    layer([(x0 + 1.1 + 0.04 * k, y), (x0 + 4.4 - 0.04 * k, y), (x0 + 4.36 - 0.04 * k, y + 0.2),
           (x0 + 1.14 + 0.04 * k, y + 0.2)], "enamel", z=6 + k)
bio.callout(ax, (x0 + 2.7, 2.8), (x0 + 1.0, 0.5), "bone (no dentine)", size="tiny")

# elasmoid: thin overlapping scales in pockets
x0 = xs[4]
bg(x0, W)
for k in range(3):
    a = x0 + 0.2 + 1.45 * k
    pts = [(a, 2.3), (a + 2.4, 3.75), (a + 2.4, 3.95), (a, 2.55)]
    layer(pts, "plywood", z=5 + 2 * k)
    layer([(a + 0.4, 2.69), (a + 2.4, 3.9), (a + 2.4, 3.97), (a + 0.4, 2.76)], "bone", z=6 + 2 * k)
for j in range(4):  # ctenii on the last scale
    xx = x0 + 3.5 + 0.18 * j
    ax.plot([xx, xx + 0.25], [3.6 + 0.1 * j, 3.85 + 0.1 * j], color=P.ink(), lw=0.8, zorder=12)
bio.callout(ax, (x0 + 4.1, 3.9), (x0 + 3.6, 6.4), "ctenii (ctenoid)", size="tiny")
bio.callout(ax, (x0 + 1.5, 3.0), (x0 + 0.6, 0.5), "collagen plywood", size="tiny")

entries = [("enamel", "enamel, enameloid, ganoine"), ("dentine", "dentine"), ("cosmine", "cosmine"),
           ("spongy", "spongy vascular bone"), ("bone", "lamellar bone, bony layer"),
           ("plywood", "collagen plywood (elasmodine)"), ("epidermis", "epidermis"), ("dermis", "dermis")]
for i, (k, t) in enumerate(entries):
    x = 0.6 + (i % 4) * 7.4
    y = -0.6 - 0.7 * (i // 4)
    bio.shape(ax, [(x, y - 0.2), (x + 0.5, y - 0.2), (x + 0.5, y + 0.2), (x, y + 0.2)], token=TOK[k], lw=0.6)
    bio.label(ax, (x + 0.7, y), t, size="tiny", ha="left")
ax.set_ylim(-1.8, 9.5)
