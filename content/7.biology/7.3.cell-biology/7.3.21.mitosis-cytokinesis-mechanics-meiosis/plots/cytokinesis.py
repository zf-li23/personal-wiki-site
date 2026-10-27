"""Cytokinesis in animal and plant cells (schematic).

(A) Positioning and assembly of the contractile ring in an animal cell in anaphase. Centralspindlin (the
kinesin-6 MKLP1 with the RhoGAP Cyk4/MgcRacGAP), clustered by Aurora B on the antiparallel overlaps of the
spindle midzone, recruits the RhoGEF Ect2 and activates RhoA in a narrow equatorial zone of the cortex;
astral microtubules inhibit cortical contractility near the poles. Active RhoA-GTP activates formins (linear
actin filaments) and Rho kinase (ROCK), which phosphorylates the regulatory light chain of myosin II, so that a
ring of actin and myosin II filaments assembles and contracts.
(B) Abscission. The furrow ingresses to an intercellular bridge about 1 um wide around the midbody (the
compacted midzone). ESCRT-III, recruited by CEP55 and ALIX/TSG101, polymerizes as a cortical helix that
constricts the membrane beside the midbody; spastin severs the bridge microtubules and the membrane is cut.
(C) A higher plant cell. Before mitosis, a preprophase band of microtubules and actin marks the future
division plane at the cortex. In telophase the remnants of the spindle form the phragmoplast, two disks of
antiparallel microtubules with plus ends at the equator; Golgi-derived vesicles with cell-wall material are
carried to the equator, fuse into the cell plate, and the plate grows centrifugally until it joins the
parental wall at the site marked by the preprophase band.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path

import wikibio as bio
from wikibio import cytoskel as C
from wikibio.core import smooth_closed

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 11.0)

# ----- A
bio.panel(ax, "A", (0.2, 10.8))
c = np.array([5.6, 5.2])
th = np.linspace(0, 2 * np.pi, 90, endpoint=False)
x = 4.6 * np.cos(th)
y = 3.3 * np.sin(th) * (1 - 0.18 * np.exp(-(x / 1.4) ** 2))
pts = smooth_closed(np.c_[x + c[0], y + c[1]], n=300)
ax.add_patch(PathPatch(Path(pts, closed=True), facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.4,
                       zorder=2))
poles = [c + [-3.2, 0], c + [3.2, 0]]
for s, pole in ((-1, poles[0]), (1, poles[1])):
    for yy in (-0.45, -0.15, 0.15, 0.45):
        C.mt_line(ax, pole, (c[0] - s * 0.35, c[1] + yy), lw=1.0, zorder=6)
    for a in np.linspace(-60, 60, 5):
        r = np.radians(a)
        C.mt_line(ax, pole, pole + 1.0 * np.array([s * np.cos(r), np.sin(r)]), lw=0.9, plus=True, zorder=6)
    ax.add_patch(Circle(pole, 0.22, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=7))
    for k in range(3):
        ax.plot([pole[0] - s * 0.45, pole[0] - s * 0.75], [pole[1] - 0.5 + 0.5 * k] * 2, color=P.edge("chromatin"),
                lw=3.0, solid_capstyle="round", zorder=8)
# centralspindlin at the overlap
for yy in (-0.3, 0.0, 0.3):
    ax.add_patch(Circle((c[0], c[1] + yy), 0.11, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.7, zorder=9))
bio.callout(ax, (c[0] + 0.1, c[1] - 0.3), (c[0] + 1.6, c[1] - 1.9), "centralspindlin + Ect2\n(midzone, Aurora B)", size="tiny")
# RhoA zone and ring
for s in (-1, 1):
    yy = c[1] + s * 3.3 * (1 - 0.18)
    ax.add_patch(Ellipse((c[0], yy - s * 0.12), 1.5, 0.42, facecolor=P.fill("negative"), alpha=0.5, edgecolor="none", zorder=3))
    ax.plot([c[0] - 0.35, c[0] + 0.35], [yy - s * 0.12] * 2, color=P.edge("muscle"), lw=5, solid_capstyle="round", zorder=9)
    bio.arrow(ax, (c[0] + 0.0, c[1] + s * 1.0), (c[0], yy - s * 0.45), kind="activation", color=P.edge("enzyme"), dashed=True)
bio.label(ax, (c[0], 9.7), "RhoA zone and contractile ring", size="tiny", bold=True, color=P.edge("negative"))
bio.label(ax, (c[0] - 3.6, 8.8), "astral microtubules\ninhibit the polar cortex", size="tiny", color=P.muted())
# signaling cascade
cx = 12.0
steps = [("Ect2 (RhoGEF)", "enzyme"), ("RhoA–GTP", "negative"), ("formin → actin\nROCK → myosin II", "muscle"),
         ("ring contraction", "positive")]
for i, (txt, tok) in enumerate(steps):
    yy = 8.8 - 2.0 * i
    bio.box(ax, (cx, yy), 3.0, 1.1, token=tok, text=txt, size="tiny")
    if i:
        bio.arrow(ax, (cx, yy + 1.45), (cx, yy + 0.6), kind="activation", color=P.ink())

# ----- B
bio.panel(ax, "B", (14.3, 10.8))
by = 7.6
for s in (-1, 1):
    ax.add_patch(Ellipse((17.2 + s * 2.35, by), 3.2, 3.2, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"),
                         lw=1.3, zorder=2))
ax.add_patch(Rectangle((15.7, by - 0.28), 3.0, 0.56, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=3))
for s in (-1, 1):
    ax.plot([15.95, 18.45], [by + s * 0.28] * 2, color=P.edge("membrane"), lw=1.3, zorder=4)
for yy in (-0.12, 0.0, 0.12):
    ax.plot([15.7, 18.7], [by + yy] * 2, color=P.edge("channel"), lw=0.8, zorder=5)
ax.add_patch(Ellipse((17.2, by), 0.55, 0.62, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=6))
xs_ = np.linspace(17.75, 18.5, 7)
ax.plot(xs_, by + 0.32 * np.cos(np.linspace(0, 6 * np.pi, 7)) * np.linspace(1, 0.6, 7), color=P.edge("drug"), lw=1.6,
        zorder=7)
bio.callout(ax, (17.2, by + 0.3), (16.3, by + 2.3), "midbody", size="tiny")
bio.callout(ax, (18.2, by - 0.25), (19.1, by - 2.1), "ESCRT-III helix\nconstricts, cuts", size="tiny")
bio.label(ax, (17.2, 4.6), "abscission", size="small", bold=True)

# ----- C
bio.panel(ax, "C", (21.0, 10.8))
pc = np.array([24.0, 5.6])
ax.add_patch(FancyBboxPatch((pc[0] - 2.6, pc[1] - 4.2), 5.2, 8.4, boxstyle="round,pad=0,rounding_size=0.3",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=3.0, zorder=2))
for s in (-1, 1):
    ax.add_patch(Ellipse((pc[0], pc[1] + s * 2.6), 1.6, 1.1, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                         lw=1.0, zorder=4))
    for xx in np.linspace(pc[0] - 1.6, pc[0] + 1.6, 7):
        C.mt_line(ax, (xx, pc[1] + s * 1.7), (xx, pc[1] + s * 0.15), lw=0.9, zorder=5)
ax.add_patch(Rectangle((pc[0] - 1.5, pc[1] - 0.09), 3.0, 0.18, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"),
                       lw=0.8, zorder=6))
for xx, yy in ((pc[0] - 2.0, pc[1]), (pc[0] + 2.0, pc[1]), (pc[0] - 1.3, pc[1] + 0.5), (pc[0] + 0.4, pc[1] - 0.5),
               (pc[0] + 1.1, pc[1] + 0.6), (pc[0] - 0.4, pc[1] + 0.9)):
    ax.add_patch(Circle((xx, yy), 0.14, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.7, zorder=6))
for s in (-1, 1):
    ax.plot([pc[0] + s * 2.6, pc[0] + s * 2.6], [pc[1] - 0.35, pc[1] + 0.35], color=P.edge("highlight"), lw=4, zorder=7)
bio.arrow(ax, (pc[0] + 1.55, pc[1] - 0.5), (pc[0] + 2.2, pc[1] - 0.5), kind="process")
bio.arrow(ax, (pc[0] - 1.55, pc[1] - 0.5), (pc[0] - 2.2, pc[1] - 0.5), kind="process")
bio.callout(ax, (pc[0] + 0.6, pc[1] + 0.05), (pc[0] + 0.9, pc[1] + 4.7), "cell plate", size="tiny")
bio.callout(ax, (pc[0] - 1.0, pc[1] + 1.0), (pc[0] - 2.4, pc[1] + 4.7), "phragmoplast", size="tiny")
bio.callout(ax, (pc[0] + 2.6, pc[1] + 0.3), (pc[0] + 2.8, pc[1] - 3.6), "site of the\npreprophase band", size="tiny")
bio.label(ax, (pc[0] - 2.6, 0.9), "Golgi vesicles fuse at the equator", size="tiny", ha="left", color=P.muted())
