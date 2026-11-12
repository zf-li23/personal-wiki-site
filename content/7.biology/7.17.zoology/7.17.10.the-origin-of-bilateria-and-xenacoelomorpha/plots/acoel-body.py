# Body of an acoel (schematic): A, dorsal view; B, cross-section coloured by germ layer (acoelomate).
import numpy as np
import wikibio as bio
from wikibio import zoology as zoo
from matplotlib.patches import Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(24, 11.0)
bio.panel(ax, "A", (0.2, 10.8))
cx, cy, L, W = 7.0, 5.6, 4.4, 1.9
t = np.linspace(0, 2 * np.pi, 300)
# outline: blunt anterior (top), tapering posterior
r = 1 + 0.18 * np.sin(t)
xs, ys = cx + W * np.cos(t) * (0.85 + 0.15 * np.sin(t)), cy + L * np.sin(t)
ax.add_patch(Polygon(np.c_[xs, ys], closed=True, facecolor=P.mix(P.fill("ectoderm"), P.surface(), 0.55),
                     edgecolor=P.edge("ectoderm"), lw=1.0, zorder=3))
for k in range(0, 300, 3):  # cilia
    n = np.array([np.cos(t[k]) / W, np.sin(t[k]) / L]); n /= np.linalg.norm(n)
    ax.plot([xs[k], xs[k] + 0.14 * n[0]], [ys[k], ys[k] + 0.14 * n[1]], color=P.muted(), lw=0.5, zorder=2)
# digestive syncytium
ax.add_patch(Ellipse((cx, cy - 0.6), 2.0, 4.6, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.9, zorder=4))
# brain, nerve cords, statocyst, frontal organ
ax.add_patch(Ellipse((cx, cy + 2.6), 1.9, 0.55, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.9, zorder=6))
for dx in (-0.75, -0.3, 0.3, 0.75):
    ax.plot([cx + dx * 0.9, cx + dx * 1.5, cx + dx * 0.8], [cy + 2.4, cy - 0.5, cy - 3.6], color=P.edge("neuron"), lw=1.2, zorder=5)
ax.add_patch(Ellipse((cx, cy + 2.6), 0.42, 0.42, facecolor=P.surface(), edgecolor=P.ink(), lw=0.9, zorder=7))
ax.add_patch(Ellipse((cx, cy + 2.6), 0.16, 0.16, facecolor=P.ink(), edgecolor="none", zorder=8))
for dx in (-0.25, 0, 0.25):
    ax.plot([cx + dx, cx + dx * 0.4], [cy + 3.5, cy + 4.25], color=P.edge("vesicle"), lw=2.0, zorder=6)
ax.add_patch(Ellipse((cx, cy + 0.4), 0.55, 0.3, facecolor=P.surface(), edgecolor=P.ink(), lw=1.0, zorder=7))  # mouth (ventral)
rng = np.random.default_rng(1)
for _ in range(7):
    ax.add_patch(Ellipse((cx + rng.uniform(-1.3, 1.3), cy + rng.uniform(-1.2, 1.4)), 0.32, 0.32, facecolor=P.fill("highlight"),
                         edgecolor=P.edge("highlight"), lw=0.6, zorder=6))
ax.add_patch(Ellipse((cx, cy - 3.4), 0.6, 0.8, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.9, zorder=6))
bio.callout(ax, (cx, cy + 4.2), (cx + 3.6, cy + 4.7), "Frontal organ", size="small")
bio.callout(ax, (cx, cy + 2.6), (cx + 3.6, cy + 3.5), "Statocyst in the brain", size="small")
bio.callout(ax, (cx + 0.26, cy + 0.42), (cx + 3.6, cy + 1.6), "Mouth (ventral)", size="small")
bio.callout(ax, (cx + 1.25, cy - 0.5), (cx + 3.6, cy - 0.3), "Nerve cord", size="small")
bio.callout(ax, (cx + 0.6, cy - 1.8), (cx + 3.6, cy - 1.9), "Digestive syncytium", size="small")
bio.callout(ax, (cx, cy - 3.4), (cx + 3.6, cy - 3.5), "Copulatory organ", size="small")
oo = (cx - 1.0, cy + 1.0)
bio.callout(ax, (cx - 1.2, cy + 0.2), (cx - 3.4, cy + 1.6), "Oocytes in\nparenchyma", size="small")
bio.callout(ax, (cx - 1.85, cy + 2.2), (cx - 3.4, cy + 3.6), "Ciliated\nepidermis", size="small")
bio.label(ax, (cx, 0.5), "Dorsal view", size="small", color=P.muted())

bio.panel(ax, "B", (14.6, 10.8))
a = zoo.body_plan(ax, (19.0, 5.6), 2.6, "acoelomate")
bio.callout(ax, a["ectoderm"], (22.4, 8.6), "Ciliated epidermis", size="small")
bio.callout(ax, a["mesoderm"], (22.4, 7.6), "Muscle and parenchyma", size="small")
bio.callout(ax, a["endoderm"], (22.4, 2.6), "Digestive tissue", size="small")
zoo.germ_layer_legend(ax, (15.4, 1.2), items=("ectoderm", "mesoderm", "endoderm"), step=2.8)
bio.label(ax, (19.0, 9.9), "Cross-section", size="small", color=P.muted())
