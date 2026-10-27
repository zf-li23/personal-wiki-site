"""Lamin domains and the processing of prelamin A (human residue numbers).
(A) Domain maps drawn to scale: prelamin A (664 residues), lamin C (572; shares residues 1-566 and ends with
six unique residues), lamin B1 (586). Head, rod with coil segments 1A, 1B and 2, NLS, Ig fold, CaaX box.
(B) Processing of the prelamin A C-terminus: farnesylation of Cys661, removal of -SIM, carboxymethylation,
cleavage by ZMPSTE24 between Tyr646 and Leu647. (C) Progerin lacks residues 607-656 (exon 11 cryptic splice),
including the cleavage site, and stays farnesylated and membrane-anchored."""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 10.4)
S = 0.02  # units per residue
X0 = 3.0


def bar(y, segs, length, name, note=None):
    ax.plot([X0, X0 + length * S], [y, y], color=P.muted(), lw=2.0, solid_capstyle="round", zorder=5)
    for a, b, tok, txt in segs:
        bio.box(ax, (X0 + (a + b) / 2 * S, y), (b - a) * S, 0.5, token=tok, text=txt, size="tiny", radius=0.1, zorder=8)
    bio.label(ax, (X0 - 0.25, y), name, size="small", ha="right")
    if note:
        bio.label(ax, (X0 + length * S + 0.3, y), note, size="tiny", ha="left", color=P.muted())


bio.panel(ax, "A", (0.1, 10.3))
rod = [(34, 70, "protein", "1A"), (80, 218, "protein", "1B"), (243, 383, "protein", "2")]
bar(9.2, [(1, 33, "neutral", "")] + rod + [(417, 422, "receptor", ""), (428, 549, "enzyme", "Ig"), (661, 664, "antibody", "")],
    664, "Prelamin A", "664 aa, CaaX = CSIM")
bar(7.95, [(1, 33, "neutral", "")] + rod + [(417, 422, "receptor", ""), (428, 549, "enzyme", "Ig"), (566, 572, "highlight", "")],
    572, "Lamin C", "572 aa, no CaaX")
bar(6.9, [(1, 29, "neutral", "")] + [(30, 66, "protein", "1A"), (76, 214, "protein", "1B"), (239, 380, "protein", "2")] +
    [(415, 420, "receptor", ""), (431, 548, "enzyme", "Ig"), (583, 586, "antibody", "")], 586, "Lamin B1", "586 aa, CaaX = CAIM")
for x, t in ((17, "head"), (225, "rod (coiled coil)"), (419, "NLS"), (662, "CaaX")):
    bio.label(ax, (X0 + x * S, 9.75), t, size="tiny", va="bottom", color=P.muted())
ax.plot([X0 + 646 * S] * 2, [8.85, 9.55], color=P.edge("negative"), lw=1.2)
bio.label(ax, (X0 + 646 * S - 0.05, 9.75), "ZMPSTE24 site", size="tiny", va="bottom", ha="right", color=P.edge("negative"))
for x0, x1 in ((607, 656),):
    ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
        (X0 + x0 * S, 8.88), (x1 - x0) * S, 0.64, fill=False, edgecolor=P.edge("negative"), lw=1.0, ls=(0, (2, 1.5)), zorder=9))
bio.label(ax, (X0 + 631 * S, 8.62), "deleted in progerin", size="tiny", va="top", color=P.edge("negative"))


# B: processing of the C-terminus, drawn as the last residues on a membrane
def tail(x, y, steps, cut=False, title=None, anchored=True, progerin=False):
    """A C-terminal tail ending at y (membrane level) with modifications listed in steps."""
    # membrane (inner nuclear membrane, nucleoplasm above)
    ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
        (x - 1.3, y - 0.55), 2.6, 0.32, facecolor=P.fill("membrane"), edgecolor=P.edge("membrane"), lw=0.8, zorder=3))
    top = y + 2.2
    ax.plot([x, x], [top, y + 0.35], color=P.muted(), lw=2.0, zorder=5, solid_capstyle="round")
    if not progerin:
        bio.label(ax, (x + 0.15, y + 1.3), "Y646", size="tiny", ha="left")
        bio.label(ax, (x + 0.15, y + 1.0), "L647", size="tiny", ha="left")
        ax.plot([x - 0.12, x + 0.12], [y + 1.15] * 2, color=P.edge("negative") if cut else P.muted(), lw=1.4, zorder=6)
    bio.label(ax, (x + 0.15, y + 0.5), "C661", size="tiny", ha="left")
    if "SIM" in steps:
        bio.label(ax, (x + 0.15, y + 0.25), "-SIM", size="tiny", ha="left", color=P.muted())
    if "F" in steps:  # farnesyl: a zigzag into the membrane
        zz = np.array([[x + 0.0, y + 0.35], [x - 0.12, y + 0.15], [x + 0.06, y - 0.0], [x - 0.12, y - 0.15], [x + 0.06, y - 0.3],
                       [x - 0.08, y - 0.45]])
        if not anchored:
            zz = zz + np.array([0.0, 1.2])
        ax.plot(zz[:, 0], zz[:, 1], color=P.edge("lipid"), lw=1.8, zorder=7, solid_joinstyle="round")
    if "Me" in steps:
        bio.label(ax, (x - 0.2, y + 0.55), "OMe", size="tiny", ha="right", color=P.edge("enzyme"))
    if title:
        bio.label(ax, (x, top + 0.25), title, size="small", va="bottom")


bio.panel(ax, "B", (0.1, 6.0))
yb = 1.6
steps = [("prelamin A", ["SIM"]), ("1. farnesylation", ["SIM", "F"]), ("2. -aaX removed", ["F"]), ("3. methylation", ["F", "Me"])]
xs = [1.8, 4.6, 7.4, 10.2]
for (t, st), x in zip(steps, xs):
    tail(x, yb, st, title=t)
for a, b, e in ((xs[0], xs[1], "FTase"), (xs[1], xs[2], "RCE1 or ZMPSTE24"), (xs[2], xs[3], "ICMT")):
    bio.arrow(ax, (a + 0.75, yb + 1.3), (b - 0.75, yb + 1.3), kind="process")
    bio.label(ax, ((a + b) / 2, yb + 1.55), e, size="tiny", va="bottom", color=P.muted())
# cleavage
x = 13.3
ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
    (x - 1.3, yb - 0.55), 2.6, 0.32, facecolor=P.fill("membrane"), edgecolor=P.edge("membrane"), lw=0.8, zorder=3))
ax.plot([x - 0.4, x - 0.4], [yb + 3.4, yb + 1.6], color=P.muted(), lw=2.0, solid_capstyle="round")
bio.label(ax, (x - 0.4, yb + 3.65), "mature lamin A", size="small", va="bottom")
bio.label(ax, (x - 0.25, yb + 1.6), "Y646", size="tiny", ha="left")
ax.plot([x + 0.45, x + 0.45], [yb + 1.0, yb + 0.35], color=P.muted(), lw=2.0, solid_capstyle="round")
zz = np.array([[x + 0.45, yb + 0.35], [x + 0.33, yb + 0.15], [x + 0.51, yb], [x + 0.33, yb - 0.15], [x + 0.51, yb - 0.3]])
ax.plot(zz[:, 0], zz[:, 1], color=P.edge("lipid"), lw=1.8, solid_joinstyle="round")
bio.label(ax, (x + 0.6, yb + 0.75), "farnesylated 15-mer", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (xs[3] + 0.75, yb + 1.3), (x - 0.9, yb + 1.3), kind="process")
bio.label(ax, ((xs[3] + x) / 2 - 0.1, yb + 1.55), "4. ZMPSTE24", size="tiny", va="bottom", color=P.edge("negative"))

# C: progerin
bio.panel(ax, "C", (15.4, 6.0))
tail(17.6, yb, ["F", "Me"], title="progerin", progerin=True)
bio.label(ax, (17.6, yb - 0.9), "no cleavage site:", size="tiny", va="top", color=P.edge("negative"))
bio.label(ax, (17.6, yb - 1.25), "stays anchored", size="tiny", va="top", color=P.edge("negative"))
bio.label(ax, (19.6, yb - 0.4), "INM", size="tiny", ha="right", color=P.muted())
bio.label(ax, (0.6, yb - 0.85), "Inner nuclear membrane (nucleoplasm above)", size="tiny", ha="left", color=P.muted())
