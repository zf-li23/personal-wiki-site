"""Life cycle of Saprolegnia (an oomycete). A: asexual cycle with diplanetism and internal proliferation of
zoosporangia (the mycelium and zoospores are diploid). B: sexual cycle: meiosis in the oogonium and
antheridium (gametic meiosis), fertilization tubes, thick-walled oospores. Blue: 2n; orange: n."""
import numpy as np
from matplotlib.patches import Ellipse, Circle

import wikibio as bio
from wikibio import ecology, plant

P = bio.P
fig, ax = bio.canvas(30, 14)


def flag(x, y, ang, L=0.55, tok="dna"):
    t = np.linspace(0, 1, 30)
    a = np.radians(ang)
    u, n = np.array([np.cos(a), np.sin(a)]), np.array([-np.sin(a), np.cos(a)])
    pts = np.array([[x, y]]) + np.outer(t * L, u) + np.outer(0.06 * np.sin(t * 12), n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=0.8, zorder=12)


def primary(ax_, xy, s):
    x, y = xy
    ax.add_patch(Ellipse((x, y), 0.36, 0.52, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, zorder=11))
    flag(x - 0.03, y + 0.25, 100); flag(x + 0.03, y + 0.25, 80)


def cyst(ax_, xy, s):
    ax.add_patch(Circle(xy, 0.2, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.2, zorder=11))


def secondary(ax_, xy, s):
    x, y = xy
    ax.add_patch(Ellipse((x, y), 0.62, 0.36, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, zorder=11))
    ax.add_patch(Ellipse((x, y - 0.12), 0.18, 0.12, facecolor=bio.P.surface(), edgecolor="none", zorder=11.5))
    flag(x, y - 0.12, 160); flag(x, y - 0.12, -20)


def sporangium(ax_, xy, s):
    x, y = xy
    y += 0.55
    pts = np.c_[np.linspace(x - 1.0, x - 1.0, 2), np.linspace(y - 0.9, y - 0.9, 2)]
    plant.hypha(ax, np.array([[x, y - 0.9], [x, y + 0.4]]), width=0.34, septa=None, nuclei=0, token="dna")
    ax.plot([x - 0.17, x + 0.17], [y - 0.35, y - 0.35], color=P.edge("dna"), lw=1.0, zorder=12)
    ax.plot([x - 0.17, x + 0.17], [y - 0.05, y - 0.05], color=P.edge("dna"), lw=0.8, zorder=12, ls=(0, (2, 1)))
    for k in range(4):
        ax.add_patch(Circle((x, y + 0.05 + 0.1 * k), 0.05, facecolor=P.edge("dna"), zorder=13))


def mycelium(ax_, xy, s):
    x, y = xy
    rng = np.random.default_rng(3)
    for k in range(5):
        a = np.radians(30 + 30 * k)
        plant.hypha(ax, np.array([[x, y - 0.3], [x + 0.9 * np.cos(a), y - 0.3 + 0.8 * np.sin(a)]]), width=0.12,
                    septa=None, nuclei=0, token="dna")


bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (7.3, 13.4), "Asexual reproduction: diplanetism", size="normal", bold=True)
ecology.cycle(ax, (7.3, 6.4), 4.6, [
    dict(text="Diploid mycelium", draw=mycelium, extent=(2.0, 1.4), size="small", bold=True),
    dict(text="Zoosporangium\n(new one proliferates\ninside the old)", draw=sporangium, extent=(2.2, 2.4), size="small"),
    dict(text="Primary zoospore:\npear-shaped, apical flagella", draw=primary, extent=(2.4, 1.2), size="small"),
    dict(text="Encysts", draw=cyst, extent=(1.4, 1.0), size="small"),
    dict(text="Secondary zoospore:\nkidney-shaped, lateral flagella", draw=secondary, extent=(2.6, 1.2), size="small"),
    dict(text="Encysts, germinates", draw=cyst, extent=(1.8, 1.0), size="small")],
    start=90, gap=0.25, arrow_labels=[None, "Release", None, None, None, "Germ tube"])

bio.panel(ax, "B", (15.2, 13.8))
bio.label(ax, (22.6, 13.4), "Sexual reproduction: gametic meiosis", size="normal", bold=True)
plant.alternation_of_generations(ax, (22.6, 6.3), 3.9, [
    dict(text="Diploid mycelium (2n)", size="small", bold=True),
    dict(text="Oogonium and\nantheridium form", size="small"),
    dict(text="Eggs (oospheres) and\nmale nuclei (n)", size="small"),
    dict(text="Fertilization tubes\npenetrate the oogonium", size="small"),
    dict(text="Oospores (2n)\nthick-walled, dormant", size="small")],
    meiosis=1, fertilization=3, gap=0.2, arrow_labels=[None, None, None, None, "Germination"])
