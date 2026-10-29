"""Fertilization in the sea urchin.

Top, the five steps at the egg surface (left to right): 1 the sperm is attracted and activated by peptides
diffusing from the jelly (resact, speract); 2 contact with sulfated polysaccharides of the jelly triggers the
acrosome reaction: exocytosis of the acrosomal vesicle and extension of the actin-filled acrosomal process;
3 the process digests a path through the jelly; 4 bindin on the process binds its species-specific receptor
on the vitelline envelope; 5 the sperm and egg membranes fuse and a fertilization cone of egg actin draws the
sperm in. Bottom, the slow block to polyspermy at the egg cortex: before fertilization the cortical granules
lie under the membrane and the vitelline envelope is attached by posts; at 15-60 s the granules fuse with
the membrane (exocytosis), proteases cut the posts and the bindin receptors, and mucopolysaccharides draw in
water; by about 1 min the envelope has lifted and hardened into the fertilization envelope, and hyalin forms
the hyaline layer on the egg surface.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import gametes as gam

P = bio.P
fig, ax = bio.canvas(28, 13.6)

# ---- top: a strip of the egg surface with jelly, vitelline envelope and membrane
y_mem, y_env, y_jelly = 7.6, 7.9, 10.8
ax.add_patch(Polygon([(0.4, 6.4), (27.6, 6.4), (27.6, y_mem), (0.4, y_mem)], closed=True, facecolor=P.fill("cytoplasm"),
                     edgecolor="none", zorder=2))
ax.add_patch(Polygon([(0.4, y_env), (27.6, y_env), (27.6, y_jelly), (0.4, y_jelly)], closed=True,
                     facecolor=P.mix(P.fill("carbohydrate"), P.surface(), 0.85 if P.is_dark() else 0.7), edgecolor="none", zorder=1))
ax.plot([0.4, 27.6], [y_mem, y_mem], color=P.edge("membrane"), lw=2.0, zorder=4)
ax.plot([0.4, 27.6], [y_env, y_env], color=P.edge("bone"), lw=1.4, zorder=4)
for x in np.arange(0.8, 27.6, 1.3):
    ax.add_patch(Circle((x, y_mem - 0.35), 0.18, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.6, zorder=3))
bio.label(ax, (0.6, 10.5), "jelly coat", size="small", ha="left", color=P.muted())
bio.label(ax, (27.4, 8.15), "vitelline envelope", size="tiny", ha="right", color=P.muted())
bio.label(ax, (27.4, 7.3), "cell membrane", size="tiny", ha="right", color=P.muted())
bio.label(ax, (27.4, 6.65), "egg cytoplasm with cortical granules", size="tiny", ha="right", color=P.muted())

# step 1: chemoattraction (outside the jelly), with peptide dots
s = gam.sperm(ax, (2.9, 11.3), angle=-60, length=2.2, kind="urchin")
rng = np.random.default_rng(1)
for _ in range(16):
    ax.add_patch(Circle((1.5 + rng.uniform(0, 3), 10.4 + rng.uniform(0, 1.8)), 0.05, facecolor=P.fill("highlight"),
                        edgecolor=P.edge("highlight"), lw=0.4, zorder=6))
# step 2: acrosome reaction at the jelly
gam.sperm(ax, (7.6, 10.2), angle=-90, length=3.0, kind="urchin", acrosome="reacted")
# step 3: process digests the jelly
gam.sperm(ax, (12.4, 8.6), angle=-90, length=3.0, kind="urchin", acrosome="reacted")
ax.add_patch(Ellipse((12.4, 9.4), 0.5, 1.6, facecolor=P.fill("extracellular"), edgecolor="none", zorder=3))
# step 4: binding to the vitelline envelope (bindin - receptor)
gam.sperm(ax, (17.4, 7.95), angle=-90, length=3.0, kind="urchin", acrosome="reacted")
for dx in (-0.12, 0.0, 0.12):
    ax.add_patch(Circle((17.4 + dx, y_env - 0.04), 0.06, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.4,
                        zorder=9))
# step 5: fusion and fertilization cone
xs = np.linspace(21.4, 23.4, 60)
cone = y_mem + 0.55 * np.exp(-((xs - 22.4) / 0.35) ** 2)
ax.fill_between(xs, y_mem - 0.02, cone, color=P.fill("cytoplasm"), zorder=5)
ax.plot(xs, cone, color=P.edge("membrane"), lw=1.6, zorder=5.5)
gam.sperm(ax, (22.4, 7.9), angle=-90, length=3.0, kind="urchin", acrosome="reacted")
for k, (x, t) in enumerate(((2.9, "1 attraction and\nactivation (resact)"), (7.6, "2 acrosome reaction"), (12.4, "3 digestion of jelly"),
                            (17.4, "4 bindin binds\nreceptor (EBR1)"), (22.4, "5 membrane fusion,\nfertilization cone"))):
    bio.label(ax, (x + (0.9 if k == 0 else 0), 13.2), t, size="small", va="top")

# ---- bottom: cortex before, during and after the cortical granule reaction
for k, (st, t) in enumerate((("before", "before: 0 s"), ("exocytosis", "cortical granule exocytosis: 15–60 s"),
                             ("after", "fertilization envelope: about 1 min"))):
    c = gam.cortex(ax, (0.6 + k * 9.2, 0.9, 8.4, 4.4), stage=st, granules=7)
    bio.label(ax, (4.8 + k * 9.2, 0.45), t, size="small", color=P.muted())
    if k == 0:
        bio.callout(ax, c["granule"], (1.0, 5.8), "cortical granule", size="tiny")
        bio.callout(ax, c["envelope"], (6.0, 5.8), "vitelline envelope", size="tiny")
    if k == 1:
        bio.callout(ax, c["contents"], (12.2, 5.8), "granule contents released", size="tiny")
    if k == 2:
        bio.callout(ax, c["envelope"], (24.0, 5.8), "fertilization envelope", size="tiny")
        bio.callout(ax, c["hyaline"], (19.5, 5.8), "hyaline layer", size="tiny")
