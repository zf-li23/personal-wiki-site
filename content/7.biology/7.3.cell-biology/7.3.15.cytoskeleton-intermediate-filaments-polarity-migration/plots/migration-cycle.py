"""Cell migration on a flat substratum (schematic).

A: the cycle of crawling: (1) protrusion of a lamellipodium by Arp2/3-dependent actin polymerization
(Rac, WAVE) and of filopodia (Cdc42, formins); (2) adhesion: integrins engage the matrix in nascent adhesions
under the protrusion, some of which mature into focal adhesions linked to actin; (3) contraction: myosin II in
stress fibres and the cortex (Rho, ROCK) pulls the cell body forward against the adhesions; (4) release of
the rear adhesions and retraction of the tail. Rac dominates at the front and Rho at the rear.
B: the three Rho GTPases and the actin structures they induce when activated throughout a fibroblast
(Ridley and Hall 1992; Nobes and Hall 1995): Cdc42 filopodia, Rac a circumferential lamellipodium, Rho stress
fibres ending in focal adhesions.
"""

import numpy as np

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(26.0, 10.6)

bio.panel(ax, "A", (0.1, 10.5))
steps = ["1  protrusion", "2  adhesion", "3  contraction", "4  rear release"]
for k, name in enumerate(steps):
    y = 9.0 - k * 2.25
    sub = 0.6 + 0.0
    ax.plot([0.5, 13.2], [y - 0.9, y - 0.9], color=P.edge("extracellular"), lw=2.0, zorder=1)
    shift = 0.0 if k < 2 else 0.9 if k == 2 else 1.4
    front = 10.0 + (0.0 if k == 0 else 1.0)
    rear = 2.0 + shift
    body = np.array([(rear, y - 0.85), (rear - 0.3 if k < 3 else rear + 0.4, y - 0.5), (rear + 1.5, y + 0.4), (front - 2.5, y + 0.6),
                     (front - 0.8, y - 0.35), (front + 0.6, y - 0.75), (front + 0.6, y - 0.85)])
    outline = bio.smooth_closed(np.vstack([body, [(rear + 3.0, y - 0.9)]]), n=200)
    bio.membrane(ax, outline, "cytoplasm", zorder=3)
    bio.nucleus(ax, ((rear + front) / 2 - 1.0, y - 0.15), 0.45, chromatin=False, nucleolus=False, zorder=6)
    bio.label(ax, (0.5, y + 0.75), name, size="small", bold=True, ha="left")
    # lamellipodium actin
    for xx in np.linspace(front - 0.9, front + 0.4, 6):
        ax.plot([xx - 0.18, xx + 0.12], [y - 0.75, y - 0.45], color=P.edge("actin"), lw=0.9, zorder=7)
    if k >= 1:
        for xx in ((front - 0.6, rear + 0.5) if k < 3 else (front - 0.6,)):
            ax.add_patch(Ellipse((xx, y - 0.86), 0.45, 0.14, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                                          lw=0.6, zorder=8))
    if k >= 2:
        ax.plot([rear + 0.5, front - 0.6], [y - 0.62, y - 0.62], color=P.edge("actin"), lw=2.0, zorder=7)
        C.myosin_minifilament(ax, ((rear + front) / 2, y - 0.62), 0.8, heads=2, lw=1.6)
    if k == 0:
        bio.arrow(ax, (front + 0.8, y - 0.5), (front + 1.8, y - 0.5), kind="process", head=0.16)
        bio.label(ax, (front + 1.9, y - 0.2), "Rac: WAVE → Arp2/3", size="tiny", ha="left")
    if k == 1:
        bio.label(ax, (front + 0.9, y - 0.55), "integrins:\nnascent → focal adhesion", size="tiny", ha="left")
    if k == 2:
        bio.arrow(ax, (rear + 1.4, y + 0.85), (rear + 2.6, y + 0.85), kind="process", head=0.16)
        bio.label(ax, (front + 0.9, y - 0.55), "Rho: ROCK → myosin II", size="tiny", ha="left")
    if k == 3:
        bio.label(ax, (front + 0.9, y - 0.55), "rear adhesions\ndisassemble", size="tiny", ha="left")

bio.panel(ax, "B", (16.6, 10.5))
cells = [("Cdc42: filopodia", 8.0), ("Rac: lamellipodium", 4.9), ("Rho: stress fibres", 1.8)]
for k, (name, y) in enumerate(cells):
    c = np.array([21.2, y])
    o = bio.blob(c, 2.2, 1.15, wobble=0.04, seed=k + 2, k=10)
    bio.membrane(ax, o, "cytoplasm")
    bio.nucleus(ax, c, 0.42, chromatin=False, nucleolus=False)
    bio.label(ax, (17.2, y + 1.35), name, size="small", bold=True, ha="left")
    if k == 0:
        for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
            d = np.array([np.cos(a) * 2.1, np.sin(a) * 1.08])
            p0 = c + d * 0.97
            p1 = c + d * 1.32
            ax.plot(*np.array([p0, p1]).T, color=P.edge("membrane"), lw=3.2, solid_capstyle="round", zorder=4)
            ax.plot(*np.array([c + d * 0.82, p1]).T, color=P.edge("actin"), lw=1.0, zorder=6)
    if k == 1:
        th = np.linspace(0, 2 * np.pi, 300)
        ax.plot(c[0] + 2.0 * np.cos(th), c[1] + 1.02 * np.sin(th), color=P.edge("actin"), lw=4.0, zorder=6, alpha=0.75)
    if k == 2:
        for dy in (-0.6, -0.3, 0.3, 0.6):
            a, b = c + (-1.85, dy * 1.2), c + (1.85, dy * 0.8)
            ax.plot(*np.array([a, b]).T, color=P.edge("actin"), lw=1.8, zorder=7)
            for e in (a, b):
                ax.add_patch(Ellipse(e, 0.32, 0.14, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                                              lw=0.6, zorder=8))
