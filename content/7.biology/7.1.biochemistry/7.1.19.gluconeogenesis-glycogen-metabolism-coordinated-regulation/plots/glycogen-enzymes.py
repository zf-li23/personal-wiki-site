"""The enzymes that shorten and lengthen glycogen chains, with glucose residues as SNFG blue circles.

Chains run from the reducing end (left) to the nonreducing end (right); horizontal links are
(alpha1->4), vertical links (alpha1->6) branch points. Dashed outlines: residues removed in the step.
A: glycogen phosphorylase removes glucose 1-phosphate from nonreducing ends, one residue at a time,
   and stops four residues from a branch point (limit branch).
B: the transferase activity of the debranching enzyme moves three of these four residues to a nearby
   nonreducing end. C: its (alpha1->6) glucosidase activity hydrolyses the last residue, releasing glucose.
D: glycogen synthase adds glucose from UDP-glucose to nonreducing ends; the branching enzyme moves a
   terminal segment of 6-7 residues from a chain of at least 11 to the C-6 hydroxyl of a residue farther in.
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import glycan as G

P = bio.P
fig, ax = bio.canvas(25.0, 15.2, scale=0.42)
ax.set_ylim(2.0, 15.2)
DX, S = 0.62, 0.42


def residue(xy, ghost=False):
    if ghost:
        ax.add_patch(Circle(xy, S / 2, fill=False, edgecolor=P.muted(), lw=0.9, ls=(0, (2, 1.5)), zorder=12))
    else:
        G.symbol(ax, "Glc", xy, size=S)


def chain(x0, y, n, ghost=(), color=None):
    pts = [np.array([x0 + k * DX, y]) for k in range(n)]
    for k in range(n - 1):
        g = k + 1 in ghost
        ax.plot([pts[k][0], pts[k + 1][0]], [y, y], color=P.muted() if g else (color or P.ink()), lw=1.0,
                ls=(0, (2, 1.5)) if g else "-", zorder=10)
    for k, p in enumerate(pts):
        residue(p, k in ghost)
    return pts


def branch(base, n, ghost=(), up=0.75, highlight=False):
    """A branch attached (alpha1->6) to residue position ``base``; its first residue sits above it."""
    x0, y0 = base
    pts = chain(x0, y0 + up, n, ghost)
    ax.plot([x0, x0], [y0 + S / 2, y0 + up - S / 2], color=P.edge("drug") if highlight else P.ink(), lw=1.3, zorder=10)
    return pts


def title(xy, text):
    bio.label(ax, xy, text, size="small", bold=True, ha="left")


def step_arrow(a, b, text, side=None):
    bio.arrow(ax, a, b, kind="process")
    bio.label(ax, ((a[0] + b[0]) / 2, a[1] + 0.35), text, size="tiny", color=P.muted())


# --- A: phosphorylase -------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 14.8))
title((1.1, 14.75), "Glycogen phosphorylase")
m = chain(0.8, 11.6, 12, ghost=set(range(8, 12)))
b = branch(m[3], 9, ghost=set(range(4, 9)))
bio.label(ax, (m[0][0] - 0.1, 11.0), "reducing end", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (m[-1][0] + 0.45, 11.6), "n Pᵢ", size="tiny", ha="left")
bio.label(ax, (m[-1][0] + 0.45, 11.1), "→ n Glc 1-P", size="tiny", ha="left")
bio.label(ax, (b[-1][0] + 0.45, b[-1][1]), "nonreducing ends", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (m[3][0] - 0.25, 12.0), "α1→6", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (m[6][0], 10.35), "stops 4 residues from the branch point", size="tiny", color=P.edge("drug"))

# --- B: transferase ---------------------------------------------------------------------------------
bio.panel(ax, "B", (12.9, 14.8))
title((13.7, 14.75), "Debranching enzyme: transferase")
m = chain(13.4, 11.6, 8)
b = branch(m[3], 4, ghost={1, 2, 3})
new = [np.array([m[-1][0] + DX * (k + 1), 11.6]) for k in range(3)]
for k, p in enumerate(new):
    ax.plot([p[0] - DX, p[0]], [11.6, 11.6], color=P.edge("drug"), lw=1.0, zorder=10)
    G.symbol(ax, "Glc", p, size=S, lw=1.6)
bio.arrow(ax, (b[2][0], b[2][1] + 0.35), (new[1][0], new[1][1] + 0.45), kind="process", bend=-0.25,
          color=P.edge("drug"))
bio.label(ax, (21.6, 13.4), "three residues moved\n(α1→4 to α1→4)", size="tiny", color=P.edge("drug"))

# --- C: glucosidase ---------------------------------------------------------------------------------
bio.panel(ax, "C", (0.3, 8.6))
title((1.1, 8.55), "Debranching enzyme: (α1→6) glucosidase")
m = chain(0.8, 5.6, 11)
b = branch(m[3], 1, ghost={0})
free = np.array([m[3][0] + 2.2, 7.3])
G.symbol(ax, "Glc", free, size=S)
bio.arrow(ax, (m[3][0] + 0.3, 6.45), free - (0.35, 0.1), kind="process", bend=-0.2)
bio.label(ax, (free[0] + 0.4, free[1]), "free glucose (H₂O)", size="tiny", ha="left")
bio.label(ax, (m[5][0], 4.85), "an unbranched chain for phosphorylase", size="tiny", color=P.muted())

# --- D: synthase and branching enzyme ---------------------------------------------------------------
bio.panel(ax, "D", (12.9, 8.6))
title((13.7, 8.55), "Glycogen synthase and branching enzyme")
m = chain(13.4, 6.9, 14)
for p in m[7:]:
    ax.add_patch(Circle(p, S / 2 + 0.06, fill=False, edgecolor=P.edge("drug"), lw=1.0, zorder=13))
bio.label(ax, (m[-1][0] + 0.4, 7.25), "UDP-Glc", size="tiny", ha="left")
bio.label(ax, (m[-1][0] + 0.4, 6.8), "→ UDP", size="tiny", ha="left")
bio.label(ax, (m[10][0], 6.3), "chain of ≥ 11 residues", size="tiny", color=P.muted())
m2 = chain(13.4, 3.3, 7)
b2 = branch(m2[2], 7, up=0.8, highlight=True)
for p in b2:
    ax.add_patch(Circle(p, S / 2 + 0.06, fill=False, edgecolor=P.edge("drug"), lw=1.0, zorder=13))
bio.arrow(ax, (m[9][0], 6.2), (b2[4][0], b2[4][1] + 0.45), kind="process", color=P.edge("drug"))
bio.label(ax, (22.8, 5.1), "terminal 6–7 residues\nmoved to a C-6 OH\nfarther in (α1→6)", size="tiny",
          color=P.edge("drug"))
bio.label(ax, (m2[0][0] - 0.1, 2.7), "two nonreducing ends where there was one", size="tiny", color=P.muted(),
          ha="left")
