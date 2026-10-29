"""Epithelial-mesenchymal transition (EMT) and its reverse (MET).

Left: a polarized epithelium: columnar cells joined near their apical ends by adherens junctions
(E-cadherin), resting on a basal lamina. Middle: during EMT, Snail/Slug, Twist and Zeb repress
E-cadherin, apical-basal polarity is lost, the actin cytoskeleton is reorganized and matrix
metalloproteinases (MMPs) open the basal lamina; one cell leaves the sheet. Right: mesenchymal cells,
loosely connected, with protrusions, migrating on a fibronectin-rich matrix (N-cadherin, vimentin).
The reverse arrow (MET) marks condensations such as somites and the renal vesicle.
"""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
ybase = 3.0
# basal lamina
ax.plot([0.6, 9.6], [ybase, ybase], color=P.edge("collagen") if False else P.edge("bone"), lw=3.0, zorder=3)
ax.plot([10.6, 13.0], [ybase, ybase], color=P.edge("bone"), lw=3.0, zorder=3)
ax.plot([15.0, 18.6], [ybase, ybase], color=P.edge("bone"), lw=3.0, zorder=3)
bio.label(ax, (1.0, ybase - 0.45), "basal lamina", size="tiny", ha="left")


def column(x, w=1.05, h=3.4, token="ectoderm", tilt=0.0, y0=ybase + 0.05):
    pts = [(x - w / 2, y0), (x + w / 2, y0), (x + w / 2 + tilt, y0 + h), (x - w / 2 + tilt, y0 + h)]
    bio.shape(ax, bio.core.smooth_closed(pts) if False else pts, token, lw=1.0, zorder=5)
    t = np.linspace(0, 2 * np.pi, 30)
    cxn, cyn = x + tilt * 0.4, y0 + h * 0.4
    bio.shape(ax, np.c_[cxn + 0.28 * np.cos(t), cyn + 0.4 * np.sin(t)], "nucleus", lw=0.8, zorder=6)


xs = [1.2 + 1.1 * k for k in range(8)]
for x in xs:
    column(x)
for x in xs[:-1]:
    xm = x + 0.55
    bio.box(ax, (xm, ybase + 3.05), 0.16, 0.36, "receptor", radius=0.05, zorder=8)
bio.callout(ax, (xs[2] + 0.55, ybase + 3.05), (3.0, 8.4), "adherens junction (E-cadherin)", size="tiny")
bio.label(ax, (5.0, 9.9), "Epithelium", size="normal", bold=True)
bio.label(ax, (5.0, 7.6), "apical", size="tiny", color=P.muted())

# transition
bio.label(ax, (14.0, 9.9), "EMT", size="normal", bold=True)
for x, tok, tilt in ((11.1, "ectoderm", 0.0), (12.2, "ectoderm", 0.2), (15.6, "ectoderm", -0.2), (16.7, "ectoderm", 0.0),
                     (17.8, "ectoderm", 0.0)):
    column(x, tilt=tilt)
bio.box(ax, (16.15, ybase + 3.05), 0.16, 0.36, "receptor", radius=0.05, zorder=8)
bio.box(ax, (17.25, ybase + 3.05), 0.16, 0.36, "receptor", radius=0.05, zorder=8)
mid = bio.core.blob((14.0, ybase + 1.9), 0.75, 1.2, wobble=0.15, seed=5, k=7, angle=0.2)
bio.shape(ax, mid, "ectoderm", lw=1.0, zorder=5)
bio.shape(ax, np.c_[14.0 + 0.26 * np.cos(np.linspace(0, 6.3, 30)), ybase + 1.6 + 0.34 * np.sin(np.linspace(0, 6.3, 30))],
          "nucleus", lw=0.8, zorder=6)
bio.callout(ax, (14.5, ybase + 2.6), (16.4, 8.9 - 2.4 + 0.1), "polarity lost", size="tiny")
# escaping cell (rounded, below the opened lamina)
blob = bio.core.blob((13.9, ybase - 0.6), 0.9, 0.55, wobble=0.25, seed=3, k=7, angle=-0.3)
bio.shape(ax, blob, "mesoderm", lw=1.0, zorder=6)
t = np.linspace(0, 2 * np.pi, 30)
bio.shape(ax, np.c_[13.9 + 0.25 * np.cos(t), ybase - 0.6 + 0.25 * np.sin(t)], "nucleus", lw=0.8, zorder=7)
for k in range(3):
    xx = 13.2 + 0.6 * k
    bio.label(ax, (xx, ybase + 0.15), "✂" if False else "", size="tiny")
bio.callout(ax, (13.5, ybase), (12.0, 1.0), "MMPs open the basal lamina", size="tiny")
bio.box(ax, (14.0, 8.4), 5.6, 1.3, "highlight", text="Snail, Slug, Twist, Zeb\nrepress E-cadherin", size="tiny")
bio.arrow(ax, (14.0, 7.7), (14.0, 6.9), kind="inhibition")

# mesenchyme
bio.label(ax, (25.0, 9.9), "Mesenchyme", size="normal", bold=True)
ax.plot([20.2, 29.6], [1.2, 1.2], color=P.edge("bone"), lw=0.8, zorder=2)
rng = np.random.default_rng(2)
pos = [(21.6, 3.3), (23.6, 5.4), (25.5, 2.9), (27.6, 5.0), (22.4, 7.3), (26.4, 7.3), (28.6, 2.6)]
for k, (x, y) in enumerate(pos):
    b = bio.core.blob((x, y), 0.95, 0.5, wobble=0.35, seed=10 + k, k=6, angle=rng.uniform(0, np.pi))
    bio.shape(ax, b, "mesoderm", lw=1.0, zorder=6)
    bio.shape(ax, np.c_[x + 0.22 * np.cos(t), y + 0.22 * np.sin(t)], "nucleus", lw=0.8, zorder=7)
for k in range(40):
    x0, y0 = rng.uniform(20.4, 29.4), rng.uniform(1.4, 8.4)
    a = rng.uniform(0, np.pi)
    ax.plot([x0, x0 + 0.6 * np.cos(a)], [y0, y0 + 0.6 * np.sin(a)], color=P.edge("carbohydrate"), lw=0.6, zorder=3)
bio.callout(ax, (25.2, 4.3), (24.0, 0.5), "fibronectin-rich matrix", size="tiny")
bio.label(ax, (25.0, 8.9), "N-cadherin, vimentin; migratory", size="tiny", color=P.muted())

bio.arrow(ax, (18.9, 5.6), (20.6, 5.6), kind="process")
bio.arrow(ax, (20.6, 4.6), (18.9, 4.6), kind="process", dashed=True)
bio.label(ax, (19.75, 4.1), "MET", size="tiny")
bio.arrow(ax, (9.6, 5.6), (10.4, 5.6), kind="process")
