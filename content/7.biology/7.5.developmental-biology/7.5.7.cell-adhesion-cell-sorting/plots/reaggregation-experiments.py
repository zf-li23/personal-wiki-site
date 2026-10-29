"""Three classical experiments on the self-organization of dissociated embryonic cells.

A: dissociation and reaggregation (Holtfreter; Townes and Holtfreter 1955): presumptive epidermis and
neural plate of an amphibian neurula are dissociated in alkaline medium, mixed, and allowed to
reaggregate; the mixed aggregate sorts out, epidermis outside and neural tissue inside.
B: fusion of two intact fragments (Steinberg): the less cohesive tissue (here liver) spreads over the
more cohesive one (limb bud mesoderm) and envelops it, the same end state as from a mixture.
C: the "shish kebab" variant: two aggregates threaded on a glass fibre so that they stay in contact.
Cells are drawn as circles; colours mark cell types, not germ layers.
"""

import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(7)
fig, ax = bio.canvas(32.0, 13.0)


def aggregate(center, R, kind, r=0.16, tokA="neuron", tokB="ectoderm", frac=0.5, offset=(0, 0), RA=None, lw=0.5):
    cx, cy = center
    step = 2 * r * 1.02
    for j, y in enumerate(np.arange(-R, R + 1e-9, step * np.sqrt(3) / 2)):
        for x in np.arange(-R + (j % 2) * step / 2, R + 1e-9, step):
            if x * x + y * y > (R - r * 0.6) ** 2:
                continue
            if kind == "mix":
                tok = tokA if rng.random() < frac else tokB
            elif kind == "sorted":
                dx, dy = x - offset[0], y - offset[1]
                tok = tokA if dx * dx + dy * dy < RA ** 2 else tokB
            else:
                tok = kind
            t = np.linspace(0, 2 * np.pi, 16)
            bio.shape(ax, np.c_[cx + x + r * np.cos(t), cy + y + r * np.sin(t)], tok, lw=lw, zorder=6)


# A: dissociation-reaggregation
bio.panel(ax, "A", (0.1, 12.9))
aggregate((2.2, 10.0), 1.0, "ectoderm")
aggregate((2.2, 7.4), 1.0, "neuron")
bio.label(ax, (2.2, 11.4), "presumptive epidermis", size="tiny")
bio.label(ax, (2.2, 6.0), "neural plate", size="tiny")
bio.arrow(ax, (3.5, 8.7), (5.2, 8.7), kind="process")
bio.label(ax, (4.35, 9.2), "dissociate,\nmix", size="tiny")
for _ in range(60):
    x, y = rng.uniform(5.8, 8.6), rng.uniform(7.0, 10.4)
    t = np.linspace(0, 2 * np.pi, 16)
    bio.shape(ax, np.c_[x + 0.16 * np.cos(t), y + 0.16 * np.sin(t)], "neuron" if rng.random() < 0.5 else "ectoderm", lw=0.5)
bio.arrow(ax, (9.0, 8.7), (10.6, 8.7), kind="process")
bio.label(ax, (9.8, 9.2), "reaggregate", size="tiny")
aggregate((12.4, 8.7), 1.5, "mix")
bio.arrow(ax, (14.2, 8.7), (15.8, 8.7), kind="process")
bio.label(ax, (15.0, 9.2), "sort out", size="tiny")
aggregate((17.7, 8.7), 1.6, "sorted", RA=1.0)
bio.callout(ax, (18.9, 9.5), (20.0, 10.9), "epidermis outside", size="tiny")
bio.callout(ax, (17.7, 8.7), (20.0, 6.6), "neural tissue inside", size="tiny")

# B: fusion of fragments
bio.panel(ax, "B", (0.1, 4.6))
aggregate((2.0, 2.2), 1.0, "mesoderm")
aggregate((4.05, 2.2), 1.0, "highlight")
bio.label(ax, (2.0, 0.6), "limb bud (γ = 20 mN/m)", size="tiny")
bio.label(ax, (4.3, 3.6), "liver (γ = 4.6 mN/m)", size="tiny")
bio.arrow(ax, (5.4, 2.2), (7.0, 2.2), kind="process")
bio.label(ax, (6.2, 2.7), "days", size="tiny")
aggregate((9.0, 2.2), 1.6, "sorted", tokA="mesoderm", tokB="highlight", RA=0.95, offset=(-0.15, 0.0))
bio.label(ax, (9.0, 0.2), "limb bud enveloped by liver", size="tiny")

# C: shish kebab
bio.panel(ax, "C", (13.0, 4.6))
ax.plot([13.6, 21.6], [2.2, 2.2], color=P.muted(), lw=1.4, zorder=8)
aggregate((15.3, 2.2), 0.95, "mesoderm")
aggregate((17.25, 2.2), 0.95, "highlight")
bio.label(ax, (16.3, 3.6), "two aggregates on a glass fibre", size="tiny")
bio.arrow(ax, (18.5, 2.9), (19.8, 2.9), kind="process")
ax.plot([22.0, 30.5], [2.2, 2.2], color=P.muted(), lw=1.4, zorder=8)
aggregate((26.0, 2.2), 1.6, "sorted", tokA="mesoderm", tokB="highlight", RA=0.95, offset=(-0.2, 0.0))
bio.label(ax, (26.0, 0.2), "the less cohesive tissue spreads along the fibre and over its partner", size="tiny")

# legend for A colours
for k, (tok, name) in enumerate((("ectoderm", "epidermal cell"), ("neuron", "neural plate cell"),
                                  ("mesoderm", "limb bud mesoderm"), ("highlight", "liver"))):
    yy = 12.4 - 0.6 * k
    t = np.linspace(0, 2 * np.pi, 16)
    bio.shape(ax, np.c_[25.0 + 0.18 * np.cos(t), yy + 0.18 * np.sin(t)], tok, lw=0.6)
    bio.label(ax, (25.4, yy), name, size="tiny", ha="left")
