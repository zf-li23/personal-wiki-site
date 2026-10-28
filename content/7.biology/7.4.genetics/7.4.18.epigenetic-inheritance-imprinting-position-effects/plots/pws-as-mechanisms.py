"""Genetic routes to Prader-Willi (PWS) and Angelman (AS) syndromes. Each panel shows the two chromosomes 15
of a child, paternal (blue) and maternal (red), with the imprinted region 15q11-q13 enlarged as a box. P:
the paternally expressed genes (SNORD116 cluster and others), M: UBE3A, expressed only from the maternal
chromosome in neurons. A green letter is an expressed gene, a grey letter a silent one; a dashed box is a
deletion and a cross a loss-of-function point mutation."""
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(18.0, 12.0)
W, L = 0.5, 3.6


def chrom(x, y, origin, imprint, deleted=False, mutant=False):
    """One acrocentric chromosome 15 with its top (short arm) at y; origin 'pat'/'mat' sets the colour,
    imprint 'pat'/'mat' the expression state of the region."""
    tok = "dna" if origin == "pat" else "receptor"
    ax.add_patch(FancyBboxPatch((x - W / 2, y - 0.35), W, 0.25, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=8))
    ax.plot([x, x], [y - 0.1, y - 0.5], color=P.edge(tok), lw=1.0, zorder=7)  # satellite stalk
    ax.add_patch(FancyBboxPatch((x - W / 2, y - L), W, L - 0.5, boxstyle="round,pad=0,rounding_size=0.22",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=8))
    ry0, ry1 = y - 1.75, y - 0.75  # the region 15q11-q13
    bx = x - 0.62
    if deleted:
        ax.add_patch(FancyBboxPatch((x - W / 2 - 0.02, ry0), W + 0.04, ry1 - ry0, boxstyle="square,pad=0",
                                    facecolor=fig.get_facecolor(), edgecolor="none", zorder=9))
        ax.add_patch(FancyBboxPatch((bx, ry0), 1.24, ry1 - ry0, boxstyle="round,pad=0,rounding_size=0.08", fill=False,
                                    edgecolor=P.muted(), lw=1.0, ls=(0, (3, 2)), zorder=10))
        return
    ax.add_patch(FancyBboxPatch((bx, ry0), 1.24, ry1 - ry0, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.light("neutral"), edgecolor=P.edge(tok), lw=1.1, zorder=10))
    for k, (name, on) in enumerate((("P", imprint == "pat"), ("M", imprint == "mat"))):
        cy = ry1 - 0.28 - k * 0.45
        c = P.edge("positive") if on and not (name == "M" and mutant) else P.muted()
        ax.add_patch(Circle((x, cy), 0.19, facecolor=P.fill("positive") if c == P.edge("positive") else "none",
                            edgecolor=c, lw=1.0, zorder=11))
        bio.label(ax, (x, cy), name, size="tiny", color=P.on_fill() if c == P.edge("positive") else P.muted(), zorder=12,
                  bold=True)
        if name == "M" and mutant:
            ax.plot([x - 0.25, x + 0.25], [cy - 0.25, cy + 0.25], color=P.edge("negative"), lw=1.6, zorder=13)
            ax.plot([x - 0.25, x + 0.25], [cy + 0.25, cy - 0.25], color=P.edge("negative"), lw=1.6, zorder=13)


panels = [
    ("Normal", "pat", "mat", {}, "normal"),
    ("Paternal deletion", "pat", "mat", {"del0": True}, "PWS"),
    ("Maternal UPD", "mat", "mat", {}, "PWS"),
    ("Imprinting defect", "pat", "mat", {"imp0": "mat"}, "PWS"),
    ("UBE3A mutation", "pat", "mat", {"mut1": True}, "AS"),
    ("Maternal deletion", "pat", "mat", {"del1": True}, "AS"),
    ("Paternal UPD", "pat", "pat", {}, "AS"),
    ("Imprinting defect", "pat", "mat", {"imp1": "pat"}, "AS"),
]
for k, (title, o0, o1, opt, result) in enumerate(panels):
    col, row = k % 4, k // 4
    cx, ytop = 2.3 + col * 4.5, 10.9 - row * 5.9
    bio.label(ax, (cx, ytop + 0.55), title.replace("UBE3A", r"$\it{UBE3A}$"), size="normal", bold=True)
    for j, (o, x) in enumerate(((o0, cx - 0.8), (o1, cx + 0.8))):
        imp = opt.get(f"imp{j}", o)
        chrom(x, ytop, o, imp, deleted=opt.get(f"del{j}", False), mutant=opt.get(f"mut{j}", False))
        bio.label(ax, (x, ytop - L - 0.35), "from father" if o == "pat" else "from mother", size="tiny", color=P.muted())
    tok = {"normal": "positive", "PWS": "dna", "AS": "receptor"}[result]
    bio.label(ax, (cx, ytop - L - 0.85), {"normal": "Normal", "PWS": "Prader-Willi", "AS": "Angelman"}[result],
              size="small", bold=True, color=P.edge(tok))
