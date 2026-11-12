# Insect sensilla in schematic section (cuticle at the top, hemolymph below; not to scale).
# A trichoid mechanoreceptor (shaft from the trichogen cell, socket from the tormogen cell, one ciliated
# neuron wrapped by the thecogen cell, dendrite attached at the hair base); B multiporous olfactory peg
# (wall pores, sensillum lymph, branched dendrites of several neurons); C uniporous gustatory hair (tip pore,
# several taste neurons plus one mechanosensory neuron ending at the base); D campaniform sensillum (thin
# cuticular dome); E scolopidium of a chordotonal organ (cap cell, scolopale cell with rods, ciliated
# dendrite, no external part).
import numpy as np
from matplotlib.patches import Circle, Ellipse
import wikibio as bio

P = bio.P
W = 6.0
fig, ax = bio.canvas(5 * W, 12.5)
CUT_TOP, CUT_BOT = 8.0, 7.3
LYMPH = "extracellular"


def cuticle(x0, gap=None):
    """Cuticle band of one panel, with an optional gap (x1, x2) for the sensillum."""
    segs = [(x0 + 0.2, x0 + W - 0.2)] if gap is None else [(x0 + 0.2, gap[0]), (gap[1], x0 + W - 0.2)]
    for a, b in segs:
        bio.shape(ax, [(a, CUT_BOT), (b, CUT_BOT), (b, CUT_TOP), (a, CUT_TOP)], "animal", lw=0.7, zorder=4)
    for a, b in ((x0 + 0.2, x0 + W - 0.2),):
        ax.plot([a, b], [CUT_BOT - 0.05, CUT_BOT - 0.05], color=P.edge("animal"), lw=0.4, zorder=3)


def cell(xy, rx, ry, token="cytoplasm", nucleus=True, z=5, seed=1):
    bio.shape(ax, bio.blob(xy, rx, ry, wobble=0.05, seed=seed), token, lw=0.7, zorder=z)
    if nucleus:
        ax.add_patch(Ellipse(xy, 0.42, 0.34, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=z + 1))


def neuron(x, y_soma, y_tip, axon=True, z=8, wiggle=0.0, label=None):
    ax.add_patch(Ellipse((x, y_soma), 0.55, 0.75, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.7, zorder=z))
    yy = np.linspace(y_soma + 0.35, y_tip, 30)
    ax.plot(x + wiggle * np.sin((yy - y_soma) * 3), yy, color=P.edge("neuron"), lw=1.3, zorder=z)
    if axon:
        ax.plot([x, x], [y_soma - 0.37, 0.4], color=P.edge("neuron"), lw=1.0, zorder=z)


for i, t in enumerate(["A  Trichoid (touch)", "B  Multiporous (smell)", "C  Uniporous (taste)", "D  Campaniform (strain)",
                       "E  Scolopidium (stretch)"]):
    bio.label(ax, (i * W + W / 2, 12.1), t, size="small", bold=True)
bio.label(ax, (0.3, 0.2), "hemolymph", size="tiny", color=P.muted(), ha="left")

# ---- A trichoid mechanoreceptor
x0 = 0.0
xc = x0 + 3.0
cuticle(x0, gap=(xc - 0.55, xc + 0.55))
bio.shape(ax, [(xc - 0.55, CUT_TOP), (xc - 0.32, CUT_TOP + 0.35), (xc + 0.32, CUT_TOP + 0.35), (xc + 0.55, CUT_TOP),
               (xc + 0.4, CUT_BOT), (xc - 0.4, CUT_BOT)], "bone", lw=0.7, zorder=6)   # socket membrane
hair = [(xc - 0.13, CUT_TOP + 0.15), (xc - 0.05, 11.4), (xc + 0.05, 11.4), (xc + 0.13, CUT_TOP + 0.15)]
bio.shape(ax, hair, "animal", lw=0.8, zorder=7)
cell((xc + 1.25, 6.2), 0.85, 0.75, "protein", seed=2)      # tormogen
cell((xc - 1.25, 6.2), 0.85, 0.75, "enzyme", seed=3)       # trichogen
bio.shape(ax, [(xc - 0.5, 6.9), (xc + 0.5, 6.9), (xc + 0.4, 7.25), (xc - 0.4, 7.25)], LYMPH, lw=0.5, zorder=5)
cell((xc, 4.6), 0.55, 0.9, "vesicle", nucleus=False, seed=4)   # thecogen
neuron(xc, 3.1, CUT_TOP + 0.1)
bio.callout(ax, (xc + 0.05, 10.5), (xc + 1.4, 10.8), "Hair shaft", size="tiny")
bio.callout(ax, (xc + 0.45, CUT_TOP + 0.1), (xc + 1.6, 9.2), "Socket", size="tiny")
bio.callout(ax, (xc - 1.5, 6.3), (x0 + 0.4, 5.1), "Trichogen", size="tiny")
bio.callout(ax, (xc + 1.6, 6.0), (x0 + 5.0, 5.0), "Tormogen", size="tiny")
bio.callout(ax, (xc + 0.35, 4.9), (x0 + 5.0, 3.9), "Thecogen", size="tiny")
bio.callout(ax, (xc - 0.2, 3.1), (x0 + 0.6, 2.6), "Neuron", size="tiny")
bio.callout(ax, (xc, 7.05), (x0 + 0.4, 9.0), "Lymph", size="tiny")

# ---- B multiporous peg
x0 = W
xc = x0 + 3.0
cuticle(x0, gap=(xc - 0.6, xc + 0.6))
peg = [(xc - 0.6, CUT_BOT), (xc - 0.6, 9.8), (xc - 0.3, 10.5), (xc + 0.3, 10.5), (xc + 0.6, 9.8), (xc + 0.6, CUT_BOT)]
bio.shape(ax, peg, LYMPH, lw=0.0, zorder=5)
ax.plot([p[0] for p in peg], [p[1] for p in peg], color=P.edge("animal"), lw=1.6, zorder=7)
for k, y in enumerate(np.arange(8.4, 10.0, 0.32)):
    for side in (-1, 1):
        ax.plot([xc + side * 0.52, xc + side * 0.68], [y, y], color=P.surface(), lw=1.2, zorder=8)
rng = np.random.default_rng(5)
for j, dx in enumerate((-0.25, 0.0, 0.25)):
    neuron(xc + dx * 3.2, 3.0 + 0.3 * j, 7.4, axon=True)
    yy = np.linspace(7.4, 10.1, 12)
    ax.plot(xc + dx + 0.06 * np.sin(yy * 4 + j), yy, color=P.edge("neuron"), lw=0.9, zorder=8)
    for y in (8.6, 9.4):
        ax.plot([xc + dx, xc + dx + 0.18 * (1 if j % 2 else -1)], [y, y + 0.25], color=P.edge("neuron"), lw=0.6, zorder=8)
    ax.plot([xc + dx * 3.2, xc + dx], [3.4 + 0.3 * j, 7.4], color=P.edge("neuron"), lw=1.0, zorder=8)
for (x, y) in ((xc - 1.0, 10.9), (xc + 1.1, 10.2), (xc - 1.3, 9.4)):
    ax.add_patch(Circle((x, y), 0.07, color=P.edge("drug"), zorder=9))
bio.arrow(ax, (xc - 1.25, 9.4), (xc - 0.72, 9.25), kind="process", head=0.12, lw=0.7)
cell((xc - 1.6, 6.0), 0.75, 0.7, "enzyme", seed=6)
cell((xc + 1.6, 6.0), 0.75, 0.7, "protein", seed=7)
bio.callout(ax, (xc + 0.62, 9.6), (xc + 1.6, 10.9), "Wall pores", size="tiny")
bio.callout(ax, (xc - 1.0, 10.9), (x0 + 0.3, 11.4), "Odour molecules", size="tiny")
bio.callout(ax, (xc + 0.25, 9.0), (xc + 1.8, 8.7), "Branched dendrites", size="tiny")
bio.callout(ax, (xc + 0.8, 3.6), (x0 + 5.0, 2.8), "Olfactory neurons", size="tiny")

# ---- C uniporous taste hair
x0 = 2 * W
xc = x0 + 3.0
cuticle(x0, gap=(xc - 0.5, xc + 0.5))
bio.shape(ax, [(xc - 0.5, CUT_TOP), (xc - 0.3, CUT_TOP + 0.3), (xc + 0.3, CUT_TOP + 0.3), (xc + 0.5, CUT_TOP),
               (xc + 0.4, CUT_BOT), (xc - 0.4, CUT_BOT)], "bone", lw=0.7, zorder=6)
outer = [(xc - 0.28, CUT_TOP + 0.2), (xc - 0.12, 11.3), (xc + 0.12, 11.3), (xc + 0.28, CUT_TOP + 0.2)]
bio.shape(ax, outer, "animal", lw=0.8, zorder=7)
ax.plot([xc, xc], [CUT_TOP + 0.3, 11.35], color=P.edge("neuron"), lw=1.1, zorder=9)
ax.plot([xc - 0.04, xc + 0.04], [11.3, 11.3], color=P.surface(), lw=2.0, zorder=10)
for j, dx in enumerate((-0.9, -0.3, 0.3, 0.9)):
    neuron(xc + dx, 3.0 + 0.25 * (j % 2), 6.9, axon=True)
    ax.plot([xc + dx, xc], [6.9, CUT_TOP + 0.3], color=P.edge("neuron"), lw=0.9, zorder=8)
neuron(xc + 1.7, 4.6, CUT_BOT + 0.15, axon=True)
ax.plot([xc + 1.7, xc + 0.3], [CUT_BOT + 0.15, CUT_TOP - 0.1], color=P.edge("neuron"), lw=0.9, zorder=8)
bio.callout(ax, (xc, 11.3), (xc + 1.3, 11.6), "Tip pore", size="tiny")
bio.callout(ax, (xc - 0.9, 3.0), (x0 + 0.3, 2.3), "Taste neurons", size="tiny")
bio.callout(ax, (xc + 1.7, 4.3), (x0 + 5.0, 3.0), "Mechano-", size="tiny")
bio.label(ax, (x0 + 5.0, 2.65), "receptor", size="tiny", ha="left", color=P.ink())

# ---- D campaniform sensillum
x0 = 3 * W
xc = x0 + 3.0
cuticle(x0, gap=(xc - 0.7, xc + 0.7))
th = np.linspace(np.pi, 0, 40)
dome = [(xc + 0.7 * np.cos(t), CUT_TOP - 0.15 + 0.35 * np.sin(t)) for t in th]
ax.plot([p[0] for p in dome], [p[1] for p in dome], color=P.edge("animal"), lw=2.4, zorder=7)
bio.shape(ax, [(xc - 0.7, CUT_BOT), (xc - 0.7, CUT_TOP - 0.15)] + dome[::-1][::-1] + [(xc + 0.7, CUT_BOT)], LYMPH, lw=0, zorder=5)
cell((xc - 1.3, 6.2), 0.75, 0.7, "enzyme", seed=8)
cell((xc + 1.3, 6.2), 0.75, 0.7, "protein", seed=9)
neuron(xc, 3.3, CUT_TOP - 0.1)
for side in (-1, 1):
    bio.arrow(ax, (xc + side * 2.6, 7.65), (xc + side * 1.6, 7.65), kind="process", head=0.14, lw=0.8)
bio.label(ax, (xc, 9.2), "cuticle strained", size="tiny", color=P.muted())
bio.callout(ax, (xc + 0.4, CUT_TOP + 0.1), (xc + 1.5, 10.2), "Thin dome", size="tiny")
bio.callout(ax, (xc + 0.05, 5.2), (x0 + 5.0, 4.4), "Dendrite", size="tiny")

# ---- E scolopidium (lying vertically below the cuticle)
x0 = 4 * W
xc = x0 + 3.0
cuticle(x0)
bio.shape(ax, [(xc - 0.45, CUT_BOT), (xc + 0.45, CUT_BOT), (xc + 0.3, 6.2), (xc - 0.3, 6.2)], "bone", lw=0.7, zorder=6)
scol = bio.blob((xc, 5.0), 0.55, 1.2, wobble=0.03, seed=10)
bio.shape(ax, scol, "vesicle", lw=0.7, zorder=6)
for dx in (-0.25, -0.08, 0.08, 0.25):
    ax.plot([xc + dx, xc + dx * 0.4], [4.3, 5.9], color=P.edge("actin"), lw=1.2, zorder=8)
neuron(xc, 2.3, 6.1)
ax.plot([xc, xc], [5.9, 6.15], color=P.edge("neuron"), lw=2.2, zorder=9)
bio.shape(ax, [(xc - 0.2, 1.7), (xc + 0.2, 1.7), (xc + 0.15, 0.6), (xc - 0.15, 0.6)], "neutral", lw=0.5, zorder=5)
bio.callout(ax, (xc + 0.35, 6.8), (x0 + 4.9, 9.0), "Cap cell", size="tiny")
bio.callout(ax, (xc + 0.5, 5.0), (x0 + 4.9, 6.2), "Scolopale cell", size="tiny")
bio.callout(ax, (xc + 0.1, 5.2), (x0 + 0.3, 6.0), "Scolopale rods", size="tiny")
bio.callout(ax, (xc, 6.05), (x0 + 0.3, 9.0), "Cilium", size="tiny")
bio.callout(ax, (xc - 0.2, 2.3), (x0 + 0.3, 2.0), "Neuron", size="tiny")
bio.callout(ax, (xc + 0.15, 1.1), (x0 + 4.9, 1.0), "Ligament", size="tiny")
