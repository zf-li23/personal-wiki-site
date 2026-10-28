"""How the formulas of the course depend on one another, in four blocks: transmission, mapping,
population genetics and quantitative genetics.

Each node is a numbered object of the course (F: Formula, A: Algorithm, T: Theorem, P: Proposition);
an arrow from one node to another means that the second is derived from or uses the first. Solid
arrows stay inside a block; dashed grey arrows cross between blocks and run in the gaps.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(28.0, 17.2)
d = network.Diagram(ax)

BW, BH, W, H = 12.8, 7.4, 5.4, 1.4
blocks = [  # (name, token, x0, y0, nodes in reading order: row by row, two columns)
    ("transmission (7.4.2–7.4.7)", "dna", 0.4, 9.4, [
        ("prod", "product and sum rules\n(F 2.4.1)"), ("binom", "binomial, multinomial\n(F 2.4.3)"),
        ("ratio", "modified ratios\n(F 4.2.1, A 4.8.1)"), ("bayes", "Bayesian risk\n(A 7.4.1, F 7.4.1)"),
        ("chi", "χ² test\n(F 2.5.1)"), ("path", "inbreeding by paths\n(F 7.5.1)"),
    ]),
    ("mapping (7.4.8–7.4.14)", "rna", 14.8, 9.4, [
        ("mather", "r ≤ 1/2, Mather\n(F 8.3.1)"), ("mapf", "Haldane, Kosambi\n(F 8.5.1, 8.5.2)"),
        ("mle", "estimating r, MLE\n(F 8.6.1, 8.6.3)"), ("tetrad", "tetrads, Perkins\n(F 9.2.2, 9.2.3)"),
        ("lod", "LOD score, LOD 3\n(F 14.9.1, P 14.9.1)"), ("three", "three-point testcross\n(A 8.4.1)"),
    ]),
    ("populations (7.4.22–7.4.23)", "plant", 0.4, 0.4, [
        ("hwe", "Hardy–Weinberg\n(T 22.2.1)"), ("inb", "p² + Fpq\n(F 22.4.1)"),
        ("sel", "selection recursion\n(T 23.3.1)"), ("drift", "drift, fixation\n(T 23.5.1, 23.6.1)"),
        ("musel", "mutation–selection\n(T 23.4.1)"), ("ld", "LD decay (1 − r)ᵗ\n(T 22.3.1)"),
    ]),
    ("quantitative traits (7.4.24–7.4.25)", "enzyme", 14.8, 0.4, [
        ("va", "$V_A$ and $V_D$\n(T 24.3.1)"), ("poly", "polygenic binomial\n(F 4.6.1, T 24.1.1)"),
        ("cov", "covariance of relatives\n(F 24.4.1)"), ("breed", "breeder's equation\n(T 24.5.1)"),
        ("assoc", "indirect association\n(F 25.2.1)"), ("pgs", "GWAS power, PGS\n(F 25.3.3, 25.6.1)"),
    ]),
]
pos = {}
for name, tok, x0, y0, nodes in blocks:
    ax.add_patch(FancyBboxPatch((x0, y0), BW, BH, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=1))
    bio.label(ax, (x0 + 0.4, y0 + BH - 0.45), name, size="small", bold=True, ha="left")
    for k, (nid, text) in enumerate(nodes):
        col, row = k % 2, k // 2
        at = (x0 + 3.3 + col * 6.2, y0 + BH - 1.95 - row * 2.15)
        pos[nid] = at
        d.activity(nid, at, text, w=W, h=H, token=tok, size="small")

inside = [("prod", "binom"), ("prod", "ratio"), ("prod", "bayes"), ("ratio", "chi"),
          ("mather", "mapf"), ("mapf", "tetrad"), ("mather", "mle"), ("mle", "lod"), ("three", "lod"),
          ("hwe", "inb"), ("hwe", "sel"), ("sel", "musel"), ("hwe", "drift"),
          ("poly", "va"), ("va", "cov"), ("cov", "breed"), ("assoc", "pgs")]
for a, b in inside:
    d.connect(a, b, "positive")


def R(n, dy=0.0):
    """Right edge of node n."""
    return (pos[n][0] + W / 2, pos[n][1] + dy)


def L(n, dy=0.0):
    """Left edge of node n."""
    return (pos[n][0] - W / 2, pos[n][1] + dy)


g = dict(dashed=True, color=P.muted())
A, B, C = 13.5, 14.0, 14.5  # lanes in the vertical gap between the blocks
d.connect("binom", "mle", "positive", start=R("binom", 0.2), via=[(A, pos["binom"][1] + 0.2), (A, pos["mle"][1] + 0.2)],
          end=L("mle", 0.2), **g)
d.connect("binom", "drift", "positive", start=R("binom", 0.2), via=[(A, pos["binom"][1] + 0.2), (A, pos["drift"][1])],
          end=R("drift"), **g)
d.connect("bayes", "lod", "positive", start=R("bayes", -0.2), via=[(B, pos["bayes"][1] - 0.2), (B, pos["lod"][1] - 0.2)],
          end=L("lod", -0.2), **g)
d.connect("mather", "ld", "positive", start=L("mather", -0.3), via=[(C, pos["mather"][1] - 0.3), (C, pos["ld"][1] + 0.3)],
          end=R("ld", 0.3), **g)
d.connect("ld", "assoc", "positive", start=R("ld", -0.3), end=L("assoc", -0.3), **g)
d.connect("inb", "va", "positive", start=R("inb"), end=L("va"), **g)
d.connect("path", "inb", "positive", start=(pos["path"][0], pos["path"][1] - H / 2),
          end=(pos["inb"][0], pos["inb"][1] + H / 2), **g)
