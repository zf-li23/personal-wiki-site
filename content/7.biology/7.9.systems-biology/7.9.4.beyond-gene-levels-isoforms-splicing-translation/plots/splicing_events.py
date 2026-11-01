"""The five basic classes of alternative splicing events and how reads measure them. A: skipped exon
(SE), mutually exclusive exons (MXE), alternative 5' splice site (A5SS), alternative 3' splice site
(A3SS) and retained intron (RI); constitutive exons in blue, alternative regions in orange, the
inclusion form joined above and the exclusion form below. B: a sashimi plot of a skipped exon in two
conditions: read coverage over the three exons and arcs for the junctions, labelled with the numbers
of junction reads. Inclusion junction counts I (the two arcs through the middle exon) and skipping
counts S (the long arc) give the percent spliced in with effective lengths l_I = 2(L - 2a + 1) and
l_S = L - 2a + 1 (read length L = 100, minimum anchor a = 8)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.4, 5.4))
ax = fig.add_axes([0.0, 0.0, 0.47, 1.0])
ax.set_xlim(0, 10.5)
ax.set_ylim(-0.4, 11.4)
ax.set_aspect("equal")
ax.axis("off")


def exon(x0, x1, y, tok="dna", h=0.55):
    ax.add_patch(Rectangle((x0, y - h / 2), x1 - x0, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5))


def arc(x0, x1, y, up=True, tok="dna", hgt=0.4):
    t = np.linspace(0, np.pi, 60)
    xs = x0 + (x1 - x0) * (1 - np.cos(t)) / 2
    ys = y + (1 if up else -1) * (0.28 + hgt * np.sin(t))
    ax.plot(xs, ys, color=charts.line(tok), lw=1.2, zorder=4)


def intron(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.muted(), lw=0.8, zorder=3)


rows = [("SE", "skipped exon"), ("MXE", "mutually exclusive exons"), ("A5SS", "alternative 5' splice site"),
        ("A3SS", "alternative 3' splice site"), ("RI", "retained intron")]
bio.panel(ax, "A", (0.1, 11.35))
for k, (code, name) in enumerate(rows):
    y = 9.4 - 2.05 * k
    bio.label(ax, (0.2, y + 1.25), code, size="small", bold=True, ha="left")
    bio.label(ax, (1.3, y + 1.25), name, size="tiny", ha="left", color=P.muted())
    intron(0.5, 10.0, y)
    if code == "SE":
        exon(0.5, 2.0, y); exon(4.5, 5.7, y, "rna"); exon(8.5, 10.0, y)
        arc(2.0, 4.5, y); arc(5.7, 8.5, y); arc(2.0, 8.5, y, up=False, tok="rna")
    elif code == "MXE":
        exon(0.5, 2.0, y); exon(3.6, 4.6, y, "rna"); exon(6.0, 7.0, y, "rna"); exon(8.5, 10.0, y)
        arc(2.0, 3.6, y); arc(4.6, 8.5, y); arc(2.0, 6.0, y, up=False, tok="rna"); arc(7.0, 8.5, y, up=False, tok="rna")
    elif code == "A5SS":
        exon(0.5, 3.0, y); exon(3.0, 4.0, y, "rna"); exon(8.5, 10.0, y)
        arc(4.0, 8.5, y); arc(3.0, 8.5, y, up=False, tok="rna")
    elif code == "A3SS":
        exon(0.5, 2.0, y); exon(6.0, 7.0, y, "rna"); exon(7.0, 10.0, y)
        arc(2.0, 6.0, y); arc(2.0, 7.0, y, up=False, tok="rna")
    else:
        exon(0.5, 3.5, y); exon(3.5, 7.0, y, "rna", h=0.3); exon(7.0, 10.0, y)
        arc(3.5, 7.0, y, up=False, tok="rna")
        bio.label(ax, (5.25, y + 0.45), "intron kept", size="tiny", color=P.muted())
bio.label(ax, (5.2, -0.2), "above: inclusion form (MXE: first exon)     below: exclusion form", size="tiny", color=P.muted())

# B: sashimi plot
L, a = 100, 8
lS = L - 2 * a + 1
lI = 2 * lS
conds = [("Control", (45, 39, 12)), ("Treated", (16, 14, 40))]
ex = [(0, 150), (450, 570), (870, 1020)]
pos = np.arange(0, 1021)
for j, (nm, (j1, j2, sk)) in enumerate(conds):
    bx = fig.add_axes([0.53, 0.56 - 0.42 * j, 0.45, 0.32])
    cov = np.zeros_like(pos, float)
    rng = np.random.default_rng(j)
    for (s, e), depth in zip(ex, [j1 + sk + 25, j1 + j2, j2 + sk + 25]):
        cov[s:e] = depth * (1 + 0.12 * rng.standard_normal(e - s).cumsum() / np.sqrt(e - s))
    tok = "rna" if j else "dna"
    bx.fill_between(pos, 0, np.clip(cov, 0, None), color=P.fill(tok), lw=0)
    top = cov.max()
    for (x0, x1, n, up) in [(150, 450, j1, True), (570, 870, j2, True), (150, 870, sk, False)]:
        t = np.linspace(0, np.pi, 80)
        xs = x0 + (x1 - x0) * (1 - np.cos(t)) / 2
        h = (0.25 + 0.35 * up) * top
        ys = (0.55 * top + h * np.sin(t)) if up else (-0.05 * top - 0.45 * top * np.sin(t))
        bx.plot(xs, ys, color=charts.line(tok), lw=0.6 + 2.2 * n / 50)
        bx.text((x0 + x1) / 2, ys.max() + 0.04 * top if up else ys.min() - 0.04 * top, str(n), ha="center",
                va="bottom" if up else "top", fontsize=8, color=P.ink())
    I, S = j1 + j2, sk
    psi = (I / lI) / (I / lI + S / lS)
    bx.text(1.0, 0.98, f"{nm}: I = {I}, S = {S}\nPSI = {psi:.2f}", transform=bx.transAxes, ha="right", va="top",
            fontsize=8, color=P.ink())
    bx.set_xlim(-20, 1040)
    bx.set_ylim(-0.7 * top, 1.35 * top)
    bx.set_yticks([0, round(top, -1)])
    charts.style_axes(bx, "position (bp)" if j else None, "coverage")
    if j == 0:
        charts.title(bx, "B  Sashimi plot of a skipped exon")
        bx.set_xticklabels([])
