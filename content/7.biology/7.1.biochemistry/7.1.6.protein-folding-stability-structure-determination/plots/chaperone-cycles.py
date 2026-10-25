"""Chaperone cycles (schematic). A: Hsp70 (DnaK) with its nucleotide-binding domain (NBD) and
substrate-binding domain (SBD, with a helical lid). ATP state: lid open, low affinity, fast exchange;
Hsp40 (J protein) brings the substrate and stimulates ATP hydrolysis; ADP state: lid closed, high
affinity; a nucleotide-exchange factor (NEF, GrpE in E. coli) replaces ADP by ATP and the substrate is
released to fold or to be rebound. B: GroEL/GroES, side view of the two heptameric rings: the
substrate binds the hydrophobic rim of an open ring, ATP and the GroES lid close a hydrophilic folding
chamber (about 10 s), and ATP binding to the opposite ring releases GroES, ADP and the protein."""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(23.4, 9.6)


def chain(points, folded=False, lw=1.6):
    pts = np.asarray(points, float)
    t = np.linspace(0, 1, 160)
    seg = np.array([np.interp(t, np.linspace(0, 1, len(pts)), pts[:, i]) for i in range(2)]).T
    d = np.gradient(seg, axis=0)
    n = np.c_[-d[:, 1], d[:, 0]]
    n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-12
    w = seg + n * 0.09 * np.sin(t * 2 * np.pi * 9)[:, None]
    ax.plot(w[:, 0], w[:, 1], color=P.edge("highlight"), lw=lw, solid_capstyle="round", zorder=16)


def hsp70(x, y, closed, nucleotide, sub=False):
    """Hsp70 at (x, y): NBD below, SBD above; returns the SBD cleft position."""
    bio.protein(ax, (x, y), 1.5, 1.05, "enzyme", text="NBD")
    ax.add_patch(FancyBboxPatch((x - 0.45, y + 0.62), 0.9, 0.55, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.1, zorder=12))
    if not sub:
        bio.label(ax, (x, y + 0.89), "SBD", size="tiny", color=P.on_fill(), zorder=13)
    if sub:
        chain([(x - 1.1, y + 0.95), (x - 0.5, y + 0.9), (x + 0.5, y + 0.92), (x + 1.1, y + 0.85)])
    if closed:
        lid = [(x + 0.45, y + 1.17), (x - 0.35, y + 1.3)]
    else:
        lid = [(x + 0.45, y + 1.17), (x + 1.05, y + 1.75)]
    ax.plot(*np.array(lid).T, color=P.edge("receptor"), lw=5, solid_capstyle="round", zorder=17)
    bio.label(ax, (x, y - 0.8), nucleotide, size="tiny", bold=True, color=P.edge("atp"))
    return (x, y + 1.35)


bio.panel(ax, "A", (0.1, 9.5))
bio.label(ax, (0.8, 9.3), "Hsp70 cycle", size="normal", bold=True, ha="left")
# four states around a cycle
s1 = (2.0, 6.2)
s2 = (7.8, 6.2)
s3 = (7.8, 1.9)
s4 = (2.0, 1.9)
hsp70(*s1, closed=False, nucleotide="ATP")
chain([(3.6, 7.7), (4.2, 7.5), (4.8, 7.9), (5.3, 7.6)])
bio.label(ax, (4.5, 8.5), "unfolded substrate\n(exposed hydrophobic segment)", size="tiny", color=P.muted())
hsp70(*s2, closed=False, nucleotide="ATP", sub=True)
bio.protein(ax, (s2[0] + 1.5, s2[1] - 0.1), 0.8, 0.6, "drug", text="Hsp40")
hsp70(*s3, closed=True, nucleotide="ADP + Pi", sub=True)
hsp70(*s4, closed=False, nucleotide="ADP → ATP")
bio.protein(ax, (s4[0] - 1.35, s4[1] - 0.1), 0.75, 0.55, "carbohydrate", text="NEF")
bio.arrow(ax, (3.5, 6.6), (6.0, 6.6), kind="process")
bio.label(ax, (4.75, 6.95), "substrate binds\n(fast, low affinity)", size="tiny")
bio.arrow(ax, (8.6, 5.2), (8.6, 3.95), kind="process")
bio.label(ax, (9.0, 4.6), "Hsp40 stimulates\nATP hydrolysis;\nlid closes", size="tiny", ha="left")
bio.arrow(ax, (6.0, 2.3), (3.6, 2.3), kind="process")
bio.label(ax, (4.8, 2.75), "NEF: ADP out,\nATP in; lid opens", size="tiny")
bio.arrow(ax, (1.3, 3.9), (1.3, 5.2), kind="process")
# released substrate
chain([(2.6, 0.6), (3.1, 0.35), (3.6, 0.7)], lw=1.4)
bio.arrow(ax, (3.8, 0.55), (4.6, 0.55), kind="process")
bio.protein(ax, (5.1, 0.55), 0.7, 0.55, "positive", text="N")
bio.label(ax, (5.6, 0.55), "folds, or\nis rebound", size="tiny", ha="left")

# B: GroEL/GroES
bio.panel(ax, "B", (11.4, 9.5))
bio.label(ax, (17.4, 9.2), "GroEL/GroES (chaperonin)", size="normal", bold=True)


def ring(x, y, w=2.4, h=1.35, token="protein", cap=False, cavity=None):
    for dx in (-w / 2, w / 2 - 0.55):
        ax.add_patch(FancyBboxPatch((x + dx, y), 0.55, h, boxstyle="round,pad=0,rounding_size=0.14",
                                    facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.0, zorder=11))
    ax.add_patch(FancyBboxPatch((x - w / 2 + 0.55, y), w - 1.1, 0.18, boxstyle="round,pad=0,rounding_size=0.06",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.8, zorder=10))
    if cavity:
        ax.add_patch(FancyBboxPatch((x - w / 2 + 0.6, y + 0.22), w - 1.2, h - 0.25, boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=P.mix(P.fill(cavity), P.surface(), 0.55), edgecolor="none", zorder=9))


def groel(x, y, cis=None, groes=False, trans_atp=False, label_rings=False):
    ring(x, y, cavity=None)                      # lower (trans) ring
    top = y + 1.4
    ax.add_patch(FancyBboxPatch((x - 1.2, top - 0.05), 2.4, 0.06, boxstyle="square,pad=0", facecolor=P.edge("protein"),
                                edgecolor="none", zorder=12))
    ring(x, top, h=1.7 if groes else 1.35, cavity="channel" if groes else None)
    if groes:
        ax.add_patch(FancyBboxPatch((x - 1.0, top + 1.72), 2.0, 0.32, boxstyle="round,pad=0,rounding_size=0.14",
                                    facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=1.0, zorder=12))
        bio.label(ax, (x, top + 1.88), "GroES", size="tiny", color=P.on_fill(), zorder=13)
    if cis == "unfolded":
        chain([(x - 0.4, top + 1.55), (x, top + 1.25), (x + 0.4, top + 1.6)], lw=1.3)
    elif cis == "folding":
        bio.protein(ax, (x, top + 0.85), 0.6, 0.55, "positive", size="tiny")
    if trans_atp:
        bio.label(ax, (x, y - 0.35), "7 ATP bind trans ring", size="tiny", color=P.edge("atp"), bold=True)
    if label_rings:
        bio.label(ax, (x - 1.55, top + 0.7), "cis", size="tiny", color=P.muted(), ha="right")
        bio.label(ax, (x - 1.55, y + 0.7), "trans", size="tiny", color=P.muted(), ha="right")


groel(13.6, 3.3, cis="unfolded", label_rings=True)
bio.label(ax, (13.6, 7.15), "substrate binds\nhydrophobic rim", size="tiny")
groel(17.4, 3.3, cis="folding", groes=True)
bio.label(ax, (17.4, 7.15), "7 ATP + GroES:\nclosed chamber,\nfolds for ~10 s", size="tiny")
groel(21.0, 3.3, cis=None, trans_atp=True)
chain([(20.4, 6.7), (20.8, 6.4)], lw=1.2)
bio.protein(ax, (21.4, 6.7), 0.5, 0.45, "positive", size="tiny")
bio.label(ax, (21.0, 7.3), "release", size="tiny")
bio.arrow(ax, (15.0, 4.7), (16.0, 4.7), kind="process")
bio.arrow(ax, (18.8, 4.7), (19.6, 4.7), kind="process")
bio.label(ax, (19.2, 5.05), "ATP → ADP", size="tiny", color=P.edge("atp"))
bio.label(ax, (17.4, 1.9), "each ring: 7 subunits of 57 kDa (two shown in section)", size="tiny", color=P.muted())
