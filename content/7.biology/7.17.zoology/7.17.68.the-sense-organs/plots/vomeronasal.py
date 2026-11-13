# The vomeronasal organ of a snake (median section), of a mammal (frontal section) and the forked tongue
# sampling two points. Schematic, not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 7.6)
# A snake snout median section
bio.label(ax, (0.4, 7.2), "A  Snake, median section", size="small", ha="left")
snout = vs.smooth([(0.6, 4.2), (1.4, 5.6), (5.0, 6.0), (8.0, 5.6), (8.2, 3.0), (5.0, 2.2), (1.2, 2.8)])
bio.shape(ax, snout, token="animal", zorder=1)
bio.shape(ax, vs.oval((4.4, 5.0), 2.2, 0.45), token="extracellular", zorder=2)          # nasal cavity
bio.shape(ax, vs.oval((5.6, 5.1), 0.9, 0.3), token="neuron", zorder=3)                  # olfactory epithelium
bio.shape(ax, vs.oval((3.0, 4.15), 0.7, 0.35), token="receptor", zorder=3)              # VNO
ax.plot([3.0, 3.0], [3.8, 3.35], color=P.edge("receptor"), lw=2, zorder=4)
ax.plot([0.9, 8.0], [3.3, 3.3], color=P.edge("bone"), lw=3, zorder=3)                   # palate
t = np.linspace(0, 1, 30)
ax.plot(1.2 + 6.0 * t, 2.95 - 0.05 * np.sin(np.pi * t), color=P.edge("receptor"), lw=3.5, zorder=4)
ax.plot([1.2, 0.2], [2.95, 3.25], color=P.edge("receptor"), lw=2, zorder=4)
ax.plot([1.2, 0.2], [2.95, 2.65], color=P.edge("receptor"), lw=2, zorder=4)
for p, q, s in [((3.0, 4.15), (2.0, 6.8), "vomeronasal organ"), ((5.6, 5.1), (6.6, 6.8), "olfactory epithelium"),
                ((3.0, 3.5), (2.4, 1.4), "duct opening into the mouth"), ((5.0, 2.95), (7.6, 2.0), "forked tongue"),
                ((7.5, 3.3), (8.6, 4.4), "palate")]:
    bio.callout(ax, p, q, s, size="tiny")
# B mammal frontal section
bio.label(ax, (10.2, 7.2), "B  Mammal, frontal section", size="small", ha="left")
cx, cy = 13.2, 4.2
bio.shape(ax, vs.oval((cx, cy), 2.2, 2.3), token="animal", zorder=1)
for s in (-1, 1):
    bio.shape(ax, vs.oval((cx + s * 1.0, cy + 0.3), 0.75, 1.6), token="extracellular", zorder=2)
    for k in range(3):
        bio.shape(ax, vs.oval((cx + s * 1.35, cy + 1.0 - k * 0.8), 0.32, 0.22), token="neuron" if k == 0 else "bone",
                  zorder=3, lw=0.6)
    bio.shape(ax, vs.oval((cx + s * 0.32, cy - 1.0), 0.17, 0.3), token="receptor", zorder=4, lw=0.6)
ax.plot([cx, cx], [cy - 1.6, cy + 2.0], color=P.edge("bone"), lw=3, zorder=3)
for p, q, s in [((cx + 0.32, cy - 1.0), (cx + 2.6, cy - 2.2), "vomeronasal organs"), ((cx + 1.35, cy + 1.0), (cx + 2.6, cy + 2.4), "ethmoturbinal (olfactory)"),
                ((cx + 1.35, cy - 0.6), (cx + 2.7, cy + 0.2), "turbinals"), ((cx, cy + 1.6), (cx - 1.8, cy + 2.8), "nasal septum")]:
    bio.callout(ax, p, q, s, size="tiny")
# C tongue sampling
bio.label(ax, (18.6, 7.2), "C  Two-point sampling", size="small", ha="left")
xs = np.linspace(18.4, 23.6, 60)
for i, xx in enumerate(xs):
    a = np.exp(-((xx - 22.5) ** 2) / 2.0)
    ax.plot([xx, xx], [1.6, 5.6], color=P.fill("receptor"), lw=4.5, alpha=0.15 + 0.6 * a, zorder=1)
ax.plot([19.5, 20.6], [3.6, 3.6], color=P.edge("receptor"), lw=3, zorder=3)
ax.plot([20.6, 21.4], [3.6, 4.3], color=P.edge("receptor"), lw=2, zorder=3)
ax.plot([20.6, 21.4], [3.6, 2.9], color=P.edge("receptor"), lw=2, zorder=3)
bio.label(ax, (21.0, 1.2), "odour concentration rises to the right; the stronger tip guides the turn", size="tiny")
