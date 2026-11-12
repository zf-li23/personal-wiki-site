# A: internal organs of a generalized orthopteroid insect (female), lateral view, head to the left
# (schematic, proportions approximate), coloured by system: foregut (pharynx, esophagus, crop,
# proventriculus), midgut (gastric caeca, ventriculus) and hindgut (ileum, colon, rectum with rectal pads);
# Malpighian tubules at the midgut-hindgut junction; salivary glands; dorsal vessel (heart with ostia in
# the abdomen, aorta into the head); central nervous system (brain, subesophageal ganglion, ventral nerve
# cord); retrocerebral endocrine glands (corpora cardiaca and corpora allata) behind the brain and the
# prothoracic glands; ovaries of ovarioles, oviducts and spermatheca. B: transverse section of the
# abdomen: the dorsal and ventral diaphragms divide the hemocoel into the pericardial, perivisceral and
# perineural sinuses.
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(30, 11)
bio.panel(ax, "A", (0.2, 10.7))
bio.panel(ax, "B", (22.6, 10.7))
body = smooth_closed([(1.0, 5.2), (1.6, 7.6), (3.4, 8.4), (5.0, 8.3), (9.0, 8.6), (16, 8.2), (20.6, 7.0), (21.4, 5.4),
                      (20.4, 3.9), (16, 3.2), (9.0, 2.6), (5.0, 2.8), (3.2, 2.6), (1.6, 3.2)])
bio.shape(ax, body, "animal", lw=1.0, zorder=1, alpha=0.35)
for x in (4.4, 6.2, 8.4) + tuple(np.linspace(10.2, 19.4, 9)):
    ax.plot([x, x], [2.9, 8.4], color=P.muted(), lw=0.3, ls=(0, (2, 3)), zorder=2)
L = lambda pts, tok, w, z=5: ax.plot(*np.array(pts).T, color=P.edge(tok), lw=w, solid_capstyle="round", zorder=z)
# gut
L([(1.4, 4.4), (2.2, 5.0), (3.0, 5.4), (4.0, 5.6)], "drug", 4)                        # pharynx/esophagus
bio.shape(ax, smooth_closed([(4.0, 5.2), (5.0, 6.3), (6.8, 6.3), (7.6, 5.6), (6.8, 4.8), (5.0, 4.8)]), "drug", lw=0.9, zorder=5)
bio.shape(ax, [(7.6, 5.25), (8.4, 5.3), (8.4, 5.9), (7.6, 5.95)], "drug", lw=0.9, zorder=5)  # proventriculus
for dy in (0.55, 0.2, -0.2, -0.55):                                                     # gastric caeca
    L([(8.6, 5.6 + dy * 0.3), (7.8, 5.6 + dy * 1.6)], "golgi", 3.2, 4)
bio.shape(ax, smooth_closed([(8.4, 5.1), (11, 4.9), (13.5, 5.0), (13.6, 6.1), (11, 6.2), (8.4, 6.1)]), "golgi", lw=0.9, zorder=5)
L([(13.6, 5.55), (15, 5.4), (16.5, 5.8), (18.0, 5.5)], "protein", 3.6)                  # ileum, colon
bio.shape(ax, smooth_closed([(18.0, 5.1), (19.4, 5.0), (20.4, 5.4), (19.4, 6.0), (18.0, 5.9)]), "protein", lw=0.9, zorder=5)
for x in (18.5, 19.1, 19.7):
    ax.add_patch(Ellipse((x, 5.45), 0.35, 0.55, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=6))
# Malpighian tubules
rng = np.random.default_rng(1)
for k in range(9):
    t = np.linspace(0, 1, 30)
    a = rng.uniform(-1, 1)
    xs = 13.6 + t * rng.uniform(2.0, 4.5) * np.sign(rng.uniform(-0.3, 1))
    ys = 5.55 + np.sin(t * np.pi * rng.uniform(1, 3)) * 0.9 * a - t * rng.uniform(-1.4, 1.6)
    ax.plot(xs, ys, color=P.edge("metabolite"), lw=0.9, zorder=4)
# salivary glands
for c in ((5.4, 3.9), (6.0, 3.6), (6.6, 3.9)):
    ax.add_patch(Circle(c, 0.32, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.6, zorder=4))
L([(5.4, 3.7), (3.0, 4.0), (2.0, 4.2)], "vesicle", 1.0, 4)
# dorsal vessel
L([(2.6, 7.0), (6.0, 7.4), (10.0, 7.6)], "blood", 2.0)
L([(10.0, 7.6), (19.5, 6.9)], "blood", 4.0)
for x in np.linspace(10.8, 18.8, 8):
    y = 7.6 - (x - 10) * 0.7 / 9.5
    ax.plot([x - 0.12, x + 0.12], [y + 0.18, y - 0.18], color=P.ink(), lw=0.8, zorder=7)
# nervous system
ax.add_patch(Ellipse((2.7, 6.3), 1.3, 0.9, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=6))
ax.add_patch(Ellipse((2.6, 4.0), 0.8, 0.5, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=6))
L([(2.6, 4.0), (4.5, 3.3), (6.2, 3.1), (8.4, 3.1), (12, 3.3), (16, 3.6), (17.6, 3.8)], "neuron", 1.2, 6)
for x, y in ((4.5, 3.3), (6.2, 3.1), (8.4, 3.1), (10.3, 3.2), (11.8, 3.3), (13.3, 3.4), (14.8, 3.5), (16.3, 3.6), (17.6, 3.8)):
    ax.add_patch(Circle((x, y), 0.22, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.6, zorder=7))
# endocrine
ax.add_patch(Circle((3.55, 6.6), 0.16, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=8))
ax.add_patch(Circle((3.95, 6.35), 0.16, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=8))
ax.add_patch(Ellipse((4.5, 4.4), 0.7, 0.3, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.6, zorder=8))
# ovary
for k in range(6):
    x0 = 11.0 + k * 0.75
    L([(x0, 7.0), (x0 + 0.5, 6.6), (x0 + 1.1, 6.35)], "petal", 3.0, 4)
L([(15.4, 6.3), (16.6, 4.6), (17.6, 4.0), (18.4, 3.7)], "petal", 1.4, 4)
ax.add_patch(Circle((18.7, 4.3), 0.25, facecolor=P.fill("petal"), edgecolor=P.edge("petal"), lw=0.6, zorder=6))
C = bio.callout
C(ax, (2.7, 6.5), (1.0, 9.9), "Brain")
C(ax, (3.55, 6.6), (3.0, 10.3), "Corpus cardiacum")
C(ax, (3.95, 6.35), (5.2, 10.3), "Corpus allatum")
C(ax, (5.0, 7.3), (7.2, 9.9), "Aorta")
C(ax, (6.0, 6.0), (9.0, 10.3), "Crop")
C(ax, (8.0, 5.6), (10.8, 9.9), "Proventriculus")
C(ax, (7.85, 6.45), (12.8, 10.3), "Gastric caeca")
C(ax, (14.5, 7.3), (14.8, 9.9), "Heart (ostia)")
C(ax, (12.4, 6.6), (16.8, 10.3), "Ovarioles")
C(ax, (19.5, 5.6), (19.6, 9.6), "Rectal pads")
C(ax, (2.6, 3.9), (0.8, 1.7), "Subesophageal ganglion")
C(ax, (4.5, 4.4), (3.6, 0.9), "Prothoracic gland")
C(ax, (6.0, 3.5), (6.2, 1.5), "Salivary gland")
C(ax, (8.4, 3.1), (7.4, 0.4), "Ventral nerve cord")
C(ax, (11.0, 5.1), (10.8, 1.6), "Midgut")
C(ax, (15.0, 4.8), (14.2, 0.4), "Malpighian tubules")
C(ax, (16.5, 5.8), (15.6, 1.6), "Hindgut")
C(ax, (18.7, 4.2), (18.4, 0.8), "Spermatheca")
# B: cross-section
cx, cy = 26.2, 5.4
ax.add_patch(Ellipse((cx, cy), 6.2, 7.2, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.2, zorder=2))
ax.add_patch(Ellipse((cx, cy), 5.8, 6.8, facecolor=P.light("cytoplasm") if hasattr(P, "light") else P.fill("cytoplasm"), edgecolor="none", zorder=2))
ax.plot([cx - 2.6, cx - 1.0, cx + 1.0, cx + 2.6], [6.9, 7.4, 7.4, 6.9], color=P.edge("muscle"), lw=1.4, zorder=4)
ax.plot([cx - 2.5, cx + 2.5], [3.0, 3.0], color=P.edge("muscle"), lw=1.4, zorder=4)
ax.add_patch(Circle((cx, 8.1), 0.45, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.8, zorder=5))
ax.add_patch(Circle((cx, 5.2), 1.2, facecolor=P.fill("golgi"), edgecolor=P.edge("golgi"), lw=0.8, zorder=5))
for a in np.linspace(0, 2 * np.pi, 7)[:-1]:
    ax.add_patch(Circle((cx + 1.75 * np.cos(a), 5.2 + 1.75 * np.sin(a)), 0.16, facecolor=P.fill("metabolite"),
                        edgecolor=P.edge("metabolite"), lw=0.5, zorder=5))
for x, y in ((cx - 2.2, 5.4), (cx + 2.2, 5.0), (cx - 1.6, 3.6), (cx + 1.7, 6.6)):
    ax.add_patch(Ellipse((x, y), 0.8, 0.5, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.5, zorder=5))
ax.add_patch(Circle((cx, 2.4), 0.3, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=5))
C(ax, (cx, 8.3), (cx + 1.6, 10.3), "Dorsal vessel")
C(ax, (cx - 1.0, 7.4), (cx - 3.2, 10.2), "Dorsal diaphragm")
C(ax, (cx + 1.4, 8.0), (cx + 3.4, 9.0), "Pericardial sinus")
C(ax, (cx, 4.6), (cx + 3.6, 4.0), "Gut")
C(ax, (cx + 1.75, 5.2), (cx + 3.6, 5.6), "Malpighian tubule")
C(ax, (cx + 2.2, 5.0), (cx + 3.6, 6.6), "Fat body")
C(ax, (cx - 2.0, 6.2), (cx - 3.6, 7.6), "Perivisceral sinus")
C(ax, (cx - 1.5, 3.0), (cx - 3.6, 2.0), "Ventral diaphragm")
C(ax, (cx, 2.2), (cx + 1.6, 0.6), "Nerve cord (perineural sinus)")
