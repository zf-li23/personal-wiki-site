"""Testing specification and determination: the presumptive eye region of an amphibian embryo.

Top row: the eye region of an early gastrula (marked) forms eye tissue when cultured in a neutral medium,
so it is already specified; but grafted into the trunk of a neurula, beside the somites, it forms somite
tissue like its neighbours, so it is not yet determined. Bottom row: the same region taken from a
neurula forms eye-like tissue even in the trunk: it is now determined. The isolation test asks whether a
tissue has a fate of its own; the heterotopic graft asks whether that fate can still be changed.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 12)


def gastrula(c, r=1.1, mark=True):
    ax.add_patch(Circle(c, r, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.1, zorder=5))
    ax.add_patch(Ellipse((c[0], c[1] - r * 0.62), r * 0.9, r * 0.5, facecolor=P.light("lipid"), edgecolor=P.edge("animal"),
                         lw=0.8, zorder=5.1))
    # blastopore lip as an arc on the vegetal side
    t = np.linspace(np.pi * 1.15, np.pi * 1.85, 30)
    ax.plot(c[0] + r * 0.55 * np.cos(t), c[1] - r * 0.25 + r * 0.55 * np.sin(t), color=P.edge("animal"), lw=1.4, zorder=5.2)
    if mark:
        ax.add_patch(Ellipse((c[0] - r * 0.2, c[1] + r * 0.45), r * 0.55, r * 0.38, facecolor=P.fill("highlight"),
                             edgecolor=P.edge("highlight"), lw=1.0, zorder=5.3))
    return (c[0] - r * 0.2, c[1] + r * 0.45)


def neurula(c, L=3.6, H=1.5, mark_eye=False, graft=None):
    """Dorsal view of a neurula: anterior left; keyhole-shaped neural plate; somite blocks along the trunk."""
    ax.add_patch(Ellipse(c, L, H, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1.1, zorder=5))
    t = np.linspace(0, 2 * np.pi, 120)
    xs = c[0] + L * 0.42 * np.cos(t)
    w = H * (0.17 + 0.17 * np.clip(-np.cos(t), 0, 1) ** 1.5)
    ys = c[1] + w * np.sin(t)
    ax.add_patch(Polygon(np.c_[xs, ys], closed=True, facecolor=P.light("ectoderm"), edgecolor=P.edge("ectoderm"), lw=0.9, zorder=5.2))
    for k in range(5):
        x = c[0] - L * 0.05 + k * L * 0.075
        for s in (-1, 1):
            ax.add_patch(Ellipse((x, c[1] + s * H * 0.3), L * 0.06, H * 0.16, facecolor=P.light("mesoderm"),
                                 edgecolor=P.edge("mesoderm"), lw=0.6, zorder=5.3))
    out = {"eye": (c[0] - L * 0.3, c[1] + H * 0.16), "trunk": (c[0] + L * 0.12, c[1] - H * 0.3)}
    if mark_eye:
        ax.add_patch(Ellipse(out["eye"], L * 0.12, H * 0.2, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                             lw=1.0, zorder=5.5))
    if graft:
        ax.add_patch(Ellipse(out["trunk"], L * 0.11, H * 0.22, facecolor=P.fill(graft), edgecolor=P.edge(graft), lw=1.1, zorder=5.6))
    return out


def dish(c, w=2.4, tissue="highlight", text=None):
    ax.add_patch(Ellipse(c, w, w * 0.42, facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=1.0, zorder=5))
    ax.add_patch(Ellipse((c[0], c[1] + 0.03), w * 0.88, w * 0.32, facecolor="none", edgecolor=P.muted(), lw=0.6, zorder=5.1))
    blob = bio.blob(c, 0.42, 0.22, wobble=0.12, seed=4)
    ax.add_patch(PathPatch(Path(blob, closed=True), facecolor=P.fill(tissue), edgecolor=P.edge(tissue), lw=0.9, zorder=5.2))


def eye(c, s=0.35):
    ax.add_patch(Circle(c, s, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=6))
    ax.add_patch(Circle(c, s * 0.45, facecolor=P.edge("neutral"), edgecolor="none", zorder=6.1))


# ------------------------------------------------------------------ row 1: early gastrula donor
y1 = 8.6
bio.label(ax, (2.0, 11.5), "Early gastrula", size="small", bold=True)
m = gastrula((2.0, y1))
bio.callout(ax, m, (0.5, 10.6), "presumptive eye", size="tiny")
# test 1: isolation
bio.arrow(ax, (3.3, y1 + 0.5), (7.6, y1 + 1.45), kind="process")
bio.label(ax, (5.3, y1 + 1.55), "explant, neutral medium", size="tiny", color=P.muted(), rotation=13)
dish((9.0, y1 + 1.55))
eye((10.6, y1 + 1.55), 0.25)
bio.label(ax, (13.6, y1 + 1.55), "eye tissue:\nSPECIFIED", size="small", ha="left", color=P.edge("positive"), bold=True)
# test 2: heterotopic graft
bio.arrow(ax, (3.3, y1 - 0.3), (7.4, y1 - 1.05), kind="process")
bio.label(ax, (5.3, y1 - 1.2), "graft into trunk of a neurula", size="tiny", color=P.muted(), rotation=-10)
n1 = neurula((9.4, y1 - 1.15), graft="mesoderm")
bio.callout(ax, n1["trunk"], (11.2, y1 - 2.4), "graft forms somite", size="tiny")
bio.label(ax, (13.6, y1 - 1.15), "takes the fate of its\nnew position: NOT DETERMINED", size="small", ha="left",
          color=P.edge("negative"), bold=True)

# ------------------------------------------------------------------ row 2: neurula donor
y2 = 3.2
bio.label(ax, (2.2, 5.1), "Neurula", size="small", bold=True)
n0 = neurula((2.2, y2), L=3.2, H=1.35, mark_eye=True)
bio.callout(ax, n0["eye"], (0.6, 1.4), "eye region", size="tiny")
bio.arrow(ax, (3.9, y2), (7.4, y2), kind="process")
bio.label(ax, (5.6, y2 + 0.35), "graft into trunk", size="tiny", color=P.muted())
n2 = neurula((9.4, y2), graft="highlight")
eye((n2["trunk"][0] + 0.02, n2["trunk"][1]), 0.17)
bio.callout(ax, n2["trunk"], (11.2, y2 - 1.3), "graft forms eye-like tissue", size="tiny")
bio.label(ax, (13.6, y2), "keeps its fate in a new\nposition: DETERMINED", size="small", ha="left", color=P.edge("positive"),
          bold=True)

# summary of the logic on the right
bx = 21.4
bio.box(ax, (bx + 2.4, 8.6), 5.2, 2.5, "neutral")
bio.label(ax, (bx + 2.4, 9.4), "Isolation test", size="small", bold=True, color=P.on_fill())
bio.label(ax, (bx + 2.4, 8.4), "neutral environment:\ndoes the tissue have\na fate of its own?", size="tiny", color=P.on_fill())
bio.box(ax, (bx + 2.4, 4.4), 5.2, 2.5, "neutral")
bio.label(ax, (bx + 2.4, 5.2), "Heterotopic graft", size="small", bold=True, color=P.on_fill())
bio.label(ax, (bx + 2.4, 4.2), "competing environment:\ncan the fate still\nbe changed?", size="tiny", color=P.on_fill())
bio.arrow(ax, (bx + 2.4, 7.3), (bx + 2.4, 5.7), kind="process")
bio.label(ax, (bx + 3.2, 6.5), "if yes", size="tiny", ha="left", color=P.muted())
