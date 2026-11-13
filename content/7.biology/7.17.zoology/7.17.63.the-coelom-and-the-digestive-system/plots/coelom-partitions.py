# Partitions of the coelom in five vertebrate grades, schematic left lateral views (anterior to the left).
# Cavities: pericardial, pleural (lung) and peritoneal or pleuroperitoneal; septa as dark lines. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25, 10.6)

CAV = {"pericardial": "blood", "pleural": "vesicle", "peritoneal": "highlight"}


def cav(v, kind, z=4):
    bio.shape(ax, vs.smooth(v) if len(v) > 4 else np.asarray(v, float), token=CAV[kind], zorder=z, lw=0.8)


def septum(pts, lw=2.2):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=P.ink(), lw=lw, zorder=8, solid_capstyle="round")


def frame(x0, y0, title):
    body = vs.smooth([(x0 + 0.1, y0 + 1.6), (x0 + 0.8, y0 + 2.9), (x0 + 3.0, y0 + 3.3), (x0 + 6.6, y0 + 3.1),
                      (x0 + 7.6, y0 + 1.7), (x0 + 6.6, y0 + 0.2), (x0 + 3.0, y0 + 0.05), (x0 + 0.8, y0 + 0.4)])
    bio.shape(ax, body, token="animal", zorder=2)
    bio.label(ax, (x0 + 0.1, y0 + 3.85), title, size="small", ha="left")


def lung(x0, y0, cx, cy, rx, ry):
    bio.shape(ax, vs.oval((x0 + cx, y0 + cy), rx, ry), token="er", zorder=6, lw=0.7)


def gut(x0, y0, a, b):
    ax.plot([x0 + a, x0 + b], [y0 + 1.7, y0 + 1.5], color=P.edge("enzyme"), lw=3, zorder=6, solid_capstyle="round")


panels = [(0.6, 5.9, "A  Fish, salamander"), (8.9, 5.9, "B  Lizard"), (17.2, 5.9, "C  Crocodylian"),
          (4.7, 0.6, "D  Bird"), (13.0, 0.6, "E  Mammal")]

# A
x, y, t = panels[0]; frame(x, y, t)
cav([(x + 0.9, y + 0.6), (x + 2.0, y + 0.6), (x + 2.0, y + 1.6), (x + 0.9, y + 1.6)], "pericardial")
cav([(x + 2.3, y + 0.4), (x + 6.8, y + 0.4), (x + 6.8, y + 2.6), (x + 2.3, y + 2.6)], "peritoneal")
septum([(x + 2.15, y + 0.35), (x + 2.15, y + 2.7)])
gut(x, y, 2.6, 6.6); lung(x, y, 4.0, 2.3, 1.2, 0.2)
bio.callout(ax, (x + 1.4, y + 1.1), (x + 0.6, y - 0.35), "pericardial cavity", size="tiny")
bio.callout(ax, (x + 2.15, y + 2.4), (x + 2.8, y + 3.55), "septum transversum", size="tiny")
bio.callout(ax, (x + 5.6, y + 0.8), (x + 6.0, y - 0.35), "pleuroperitoneal cavity", size="tiny")
# B
x, y, t = panels[1]; frame(x, y, t)
cav([(x + 1.2, y + 0.35), (x + 2.7, y + 0.35), (x + 2.4, y + 1.3), (x + 1.2, y + 1.3)], "pericardial")
cav([(x + 1.3, y + 1.6), (x + 2.7, y + 1.6), (x + 3.1, y + 0.4), (x + 6.8, y + 0.4), (x + 6.8, y + 2.8), (x + 1.3, y + 2.8)],
    "peritoneal")
septum([(x + 1.2, y + 1.45), (x + 2.6, y + 1.45), (x + 3.0, y + 0.3)])
lung(x, y, 3.2, 2.25, 1.5, 0.35); gut(x, y, 3.4, 6.6)
bio.callout(ax, (x + 4.6, y + 2.3), (x + 5.4, y + 3.55), "lungs in the pleuroperitoneal cavity", size="tiny")
# C
x, y, t = panels[2]; frame(x, y, t)
cav([(x + 1.2, y + 0.35), (x + 2.6, y + 0.35), (x + 2.4, y + 1.3), (x + 1.2, y + 1.3)], "pericardial")
cav([(x + 1.3, y + 1.6), (x + 2.6, y + 1.6), (x + 3.0, y + 0.4), (x + 4.2, y + 0.4), (x + 4.2, y + 2.8), (x + 1.3, y + 2.8)],
    "pleural")
cav([(x + 4.5, y + 0.4), (x + 6.8, y + 0.4), (x + 6.8, y + 2.8), (x + 4.5, y + 2.8)], "peritoneal")
septum([(x + 1.2, y + 1.45), (x + 2.5, y + 1.45), (x + 2.9, y + 0.3)])
septum([(x + 4.35, y + 0.3), (x + 4.35, y + 2.9)])
lung(x, y, 2.6, 2.25, 1.0, 0.35)
bio.shape(ax, vs.oval((x + 3.6, y + 1.0), 0.5, 0.45), token="mitochondrion", zorder=6, lw=0.7)
gut(x, y, 4.7, 6.6)
ax.annotate("", (x + 6.0, y + 0.15), (x + 4.0, y + 0.85), arrowprops=dict(arrowstyle="-|>", color=P.edge("muscle"), lw=1.2))
bio.callout(ax, (x + 4.35, y + 2.5), (x + 5.0, y + 3.55), "post-hepatic septum", size="tiny")
bio.callout(ax, (x + 3.6, y + 1.0), (x + 2.6, y - 0.35), "liver", size="tiny")
bio.label(ax, (x + 6.3, y - 0.3), "diaphragmaticus pulls liver back", size="tiny", color=P.edge("muscle"))
# D
x, y, t = panels[3]; frame(x, y, t)
cav([(x + 1.2, y + 0.35), (x + 2.6, y + 0.35), (x + 2.4, y + 1.3), (x + 1.2, y + 1.3)], "pericardial")
cav([(x + 2.8, y + 0.4), (x + 6.8, y + 0.4), (x + 6.8, y + 2.2), (x + 2.8, y + 1.5)], "peritoneal")
lung(x, y, 3.6, 2.7, 1.5, 0.25)
septum([(x + 2.0, y + 2.4), (x + 5.2, y + 2.4)])
septum([(x + 2.7, y + 1.5), (x + 6.9, y + 2.25)], lw=1.6)
for c in ((x + 2.1, y + 1.9), (x + 5.8, y + 2.6), (x + 6.6, y + 2.6)):
    bio.shape(ax, vs.oval(c, 0.35, 0.22), token="extracellular", zorder=5, lw=0.6)
gut(x, y, 3.2, 6.6)
bio.callout(ax, (x + 3.6, y + 2.7), (x + 3.0, y + 3.55), "lungs fixed dorsally", size="tiny")
bio.callout(ax, (x + 4.8, y + 2.4), (x + 6.0, y + 3.55), "horizontal septum", size="tiny")
bio.callout(ax, (x + 4.5, y + 1.83), (x + 5.2, y - 0.35), "oblique septum; air sacs", size="tiny")
# E
x, y, t = panels[4]; frame(x, y, t)
cav([(x + 1.5, y + 0.4), (x + 2.6, y + 0.4), (x + 2.6, y + 1.3), (x + 1.5, y + 1.3)], "pericardial")
cav([(x + 1.0, y + 1.4), (x + 3.3, y + 1.4), (x + 3.3, y + 2.8), (x + 1.0, y + 2.8)], "pleural")
cav([(x + 3.7, y + 0.4), (x + 6.8, y + 0.4), (x + 6.8, y + 2.8), (x + 3.7, y + 2.8)], "peritoneal")
th = np.linspace(-1.2, 1.2, 30)
ax.plot(x + 3.5 - 0.25 * np.cos(th) + 0.25, y + 1.6 + 1.25 * np.sin(th), color=P.edge("muscle"), lw=3.2, zorder=8)
lung(x, y, 2.1, 2.1, 0.9, 0.45); gut(x, y, 4.0, 6.6)
bio.callout(ax, (x + 3.6, y + 2.6), (x + 5.0, y + 3.55), "muscular diaphragm", size="tiny")
bio.callout(ax, (x + 1.4, y + 2.6), (x + 2.2, y + 3.55), "pleural cavity", size="tiny")

# legend
lx = 21.6
for i, (k, txt) in enumerate((("pericardial", "pericardial cavity"), ("pleural", "pleural / pulmonary cavity"),
                               ("peritoneal", "peritoneal or pleuroperitoneal cavity"))):
    yy = 3.6 - 0.6 * i
    bio.shape(ax, np.array([(lx, yy), (lx + 0.45, yy), (lx + 0.45, yy + 0.32), (lx, yy + 0.32)]), token=CAV[k], lw=0.7)
    bio.label(ax, (lx + 0.6, yy + 0.16), txt, size="tiny", ha="left")
yy = 1.8
bio.shape(ax, np.array([(lx, yy), (lx + 0.45, yy), (lx + 0.45, yy + 0.32), (lx, yy + 0.32)]), token="er", lw=0.7)
bio.label(ax, (lx + 0.6, yy + 0.16), "lung", size="tiny", ha="left")
