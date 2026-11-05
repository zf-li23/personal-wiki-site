"""Rhizopus stolonifer. A: part of the mycelium (stolon, rhizoids, sporangiophores; a sporangium in
section with columella and sporangiospores). B: sexual reproduction of the heterothallic (+) and (-)
strains: progametangia, gametangia and suspensors, young and mature zygosporangium, germsporangium.
C: the life cycle (haplontic: zygotic meiosis)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Wedge

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(32, 13)
rng = np.random.default_rng(5)


def sporangium(c, r, section=False):
    if section:
        ax.add_patch(Circle(c, r, facecolor=P.fill("animal"), edgecolor=P.edge("chromatin"), lw=1.4, zorder=8))
        for k in range(60):
            a = rng.uniform(0, np.pi * 2); rr = rng.uniform(0.62, 0.92) * r
            p = (c[0] + rr * np.cos(a), c[1] + rr * np.sin(a))
            if p[1] > c[1] - 0.45 * r:
                ax.add_patch(Circle(p, 0.07, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.3, zorder=9))
        ax.add_patch(Ellipse((c[0], c[1] - 0.15 * r), 1.0 * r, 1.0 * r, facecolor=P.light("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=0.9, zorder=10))
    else:
        ax.add_patch(Circle(c, r, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=1.0, zorder=8))


# A morphology
bio.panel(ax, "A", (0.2, 12.8))
ax.plot([0.5, 11.5], [2.0, 2.0], color=P.muted(), lw=1.0, zorder=3)
bio.label(ax, (11.4, 1.6), "substrate", size="tiny", ha="right", color=P.muted())
t = np.linspace(0, 1, 40)
for x0, x1 in [(1.8, 6.4), (6.4, 11.0)]:
    xs = x0 + (x1 - x0) * t
    plant.hypha(ax, np.c_[xs, 2.0 + 1.2 * np.sin(np.pi * t)], width=0.16, septa=None, nuclei=0, tip=(x1 > 10))
for xn in (1.8, 6.4):
    for d in (-0.5, -0.2, 0.15, 0.45):
        plant.hypha(ax, np.array([[xn, 2.0], [xn + d, 1.0 + 0.2 * abs(d)]]), width=0.1, septa=None, nuclei=0)
    for k, (dx, h) in enumerate([(-0.9, 5.0), (0.0, 6.4), (0.9, 4.4)]):
        top = (xn + dx, 2.0 + h)
        sec = (xn == 6.4 and dx == 0.0)
        plant.hypha(ax, np.array([[xn + 0.1 * dx, 2.0], [xn + 0.4 * dx, 2.0 + 0.5 * h], top]), width=0.14, septa=None, nuclei=0, tip=False)
        sporangium((top[0], top[1] + (0.8 if sec else 0.45)), 0.85 if sec else 0.5, section=sec)
bio.callout(ax, (4.1, 3.15), (4.3, 4.6), "Stolon")
bio.callout(ax, (1.5, 1.2), (0.5, 0.5), "Rhizoids")
bio.callout(ax, (1.8, 5.5), (3.2, 9.6), "Sporangiophore")
bio.callout(ax, (6.4, 9.08), (8.6, 10.2), "Columella")
bio.callout(ax, (6.95, 9.55), (8.6, 11.4), "Sporangiospores (n)")
bio.callout(ax, (0.9, 7.45), (1.8, 11.6), "Sporangium")

# B sexual stages
bio.panel(ax, "B", (12.6, 12.8))
stages = ["Progametangia", "Gametangia,\nsuspensors", "Young\nzygosporangium", "Mature\nzygosporangium"]
for i, name in enumerate(stages):
    cx = 14.0 + i * 3.0
    y = 8.6
    plant.hypha(ax, np.array([[cx - 1.2, y - 1.8], [cx - 0.9, y - 0.3], [cx - 0.25 + (0.0 if i else -0.15), y]]), width=0.3,
                septa=None, nuclei=0, tip=(i == 0), token="lipid_tail")
    plant.hypha(ax, np.array([[cx + 1.2, y - 1.8], [cx + 0.9, y - 0.3], [cx + 0.25 - (0.0 if i else -0.15), y]]), width=0.3,
                septa=None, nuclei=0, tip=(i == 0), token="ovule")
    if i == 1:
        for sgn, tok in ((-1, "rna"), (1, "dna")):
            ax.add_patch(Ellipse((cx + sgn * 0.3, y), 0.6, 0.7, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=9))
    if i == 2:
        ax.add_patch(Ellipse((cx, y), 1.1, 0.9, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.0, zorder=9))
        for k in range(8):
            ax.add_patch(Circle((cx + rng.uniform(-0.3, 0.3), y + rng.uniform(-0.25, 0.25)), 0.06, facecolor=P.edge("dna"), zorder=10))
    if i == 3:
        ang = np.linspace(0, 2 * np.pi, 40, endpoint=False)
        rr = 0.6 + 0.08 * (np.arange(40) % 2)
        pts = np.c_[cx + rr * np.cos(ang), y + 0.85 * rr * np.sin(ang)]
        bio.shape(ax, pts, token="chromatin", zorder=9)
    bio.label(ax, (cx, y + 1.25), name, size="tiny")
    if i < 3:
        bio.arrow(ax, (cx + 1.2, y + 0.6), (cx + 1.8, y + 0.6), kind="process")
bio.label(ax, (13.0, 6.2), "(+) strain", size="tiny", ha="left", color=P.edge("lipid_tail"))
bio.label(ax, (24.0, 6.2), "(−) strain", size="tiny", ha="right", color=P.edge("ovule"))
# germination
cx, y = 18.5, 2.6
ang = np.linspace(0, 2 * np.pi, 40, endpoint=False)
rr = 0.6 + 0.08 * (np.arange(40) % 2)
bio.shape(ax, np.c_[cx + rr * np.cos(ang), y + 0.85 * rr * np.sin(ang)], token="chromatin", zorder=9)
plant.hypha(ax, np.array([[cx, y + 0.4], [cx + 0.1, y + 2.6]]), width=0.16, septa=None, nuclei=0, tip=False)
sporangium((cx + 0.1, y + 3.0), 0.45)
bio.label(ax, (cx - 0.8, y + 3.0), "Germsporangium:\nmeiosis, (+) and (−) spores", size="tiny", ha="right")
bio.label(ax, (cx - 1.0, y), "Zygospore germinates\nafter dormancy", size="tiny", ha="right")
bio.arrow(ax, (23.0, 6.9), (19.5, 2.9), kind="process", bend=-0.15)

# C cycle
bio.panel(ax, "C", (25.4, 12.8))
plant.alternation_of_generations(ax, (28.7, 6.4), 2.4, [
    dict(text="Mycelium (n)", size="tiny", bold=True), dict(text="Gametangia\n(+) (−)", size="tiny"),
    dict(text="Zygospore\n(2n nuclei)", size="tiny"), dict(text="Germ-\nsporangium", size="tiny")],
    meiosis=2, fertilization=1, gap=0.15, labels=("2n", "n"))
bio.label(ax, (28.7, 2.2), "Asexual cycle: sporangiospores (n)\nrepeat the haploid mycelium", size="tiny")
