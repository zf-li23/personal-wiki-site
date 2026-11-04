# The infectious cycle, compared for a bacteriophage (left) and an enveloped animal virus (right).
# The same steps - attachment, entry and uncoating, synthesis, assembly, release - drawn around the host
# cell, with the differences that matter: the phage leaves its capsid outside and injects only the genome
# and lyses the cell, while the whole animal virion enters, uncoats inside, and leaves by budding with a
# maturation step afterwards. The eclipse period is noted under each panel.
import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(31, 14)
MUT = P.muted()


def step(n, xy, text, ha="left"):
    x, y = xy
    ax.add_patch(Circle((x, y), 0.3, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=18))
    bio.label(ax, (x, y), str(n), size="small", bold=True, color=P.on_fill(), zorder=19)
    bio.label(ax, (x + 0.45, y), text, size="small", ha=ha, va="center")


def phage(x, y, scale=1.0, empty=False, zorder=12):
    """A small tailed phage pointing down; (x, y) is the tail tip."""
    s, tok = scale, ("neutral" if empty else "virus")
    head = np.array([[-0.34, 0.62], [-0.34, 1.18], [0, 1.5], [0.34, 1.18], [0.34, 0.62], [0, 0.34]]) * s + [x, y]
    ax.add_patch(Polygon(head, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=zorder))
    ax.plot([x, x], [y + 0.34 * s, y], color=P.edge(tok), lw=1.6 * s, zorder=zorder, solid_capstyle="round")
    for sgn in (-1, 1):
        ax.plot([x, x + sgn * 0.3 * s], [y + 0.02 * s, y - 0.22 * s], color=P.edge(tok), lw=1.0 * s, zorder=zorder)


def squiggle(x, y, h=0.9, w=0.25, tok="dna", turns=4, lw=1.2, zorder=10):
    t = np.linspace(0, turns * np.pi, 90)
    ax.plot(x + w * np.cos(t), y + np.linspace(-h / 2, h / 2, 90),
            color=P.edge(tok) if not P.is_dark() else P.fill(tok), lw=lw, zorder=zorder)


def enveloped(x, y, r=0.46, spikes=10, zorder=12, core=True):
    for i in range(spikes):
        a = 2 * np.pi * i / spikes
        ax.plot([x + r * np.cos(a), x + r * 1.3 * np.cos(a)], [y + r * np.sin(a), y + r * 1.3 * np.sin(a)],
                color=P.edge("receptor"), lw=0.8, zorder=zorder - 1)
    ax.add_patch(Circle((x, y), r, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=0.9, zorder=zorder))
    if core:
        ax.add_patch(Circle((x, y), r * 0.55, facecolor=P.fill("virus"), edgecolor=P.edge("virus"), lw=0.7, zorder=zorder + 1))


# ================================================================ A: bacteriophage
bio.panel(ax, "A", (0.2, 13.7))
bio.label(ax, (1.0, 13.5), "Bacteriophage on a Gram-negative cell", size="title", bold=True, ha="left")
cx, cy = 7.0, 8.2
M.bacillus(ax, (cx, cy), 6.0, 3.0, gram="-", zorder=6)
bio.label(ax, (2.6, 8.2), "host cell", size="small", color=MUT)
phage(cx - 1.9, cy + 1.55, scale=0.95)
phage(cx + 0.8, cy + 1.55, scale=0.95, empty=True)
ax.plot([cx + 0.8, cx + 0.8], [cy + 1.55, cy + 0.9], color=P.edge("dna"), lw=1.5, zorder=14)
squiggle(cx + 0.8, cy + 0.1, h=1.4, turns=6, lw=1.4, zorder=14)
step(1, (0.4, 12.3), "attachment to a receptor\nin the outer membrane")
step(2, (8.3, 12.3), "injection: only the genome enters;\nthe capsid stays outside")
for dx, dy in [(-1.9, -0.5), (-1.1, 0.5), (-0.3, -0.8)]:
    squiggle(cx + dx, cy + dy, h=0.8, w=0.2, lw=1.0)
for dx, dy in [(1.9, 0.6), (2.3, -0.3), (1.5, -0.8)]:
    ax.add_patch(Circle((cx + dx, cy + dy), 0.17, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=10))
phage(cx + 2.2, cy - 0.1, scale=0.55)
step(3, (0.4, 5.3), "synthesis: the host programme is shut off;\nphage DNA and proteins are made in a timed order")
step(4, (8.3, 5.3), "assembly and packaging")
for k, (px, py) in enumerate([(12.2, 10.6), (13.2, 9.3), (13.6, 7.7), (13.0, 6.2), (12.0, 5.2)]):
    phage(px, py, scale=0.6)
bio.arrow(ax, (10.4, 8.6), (11.7, 8.6), kind="process", lw=1.2, head=0.22)
step(5, (0.4, 3.2), "lysis: the cell bursts and releases the whole burst at once")
bio.label(ax, (0.4, 1.5), "eclipse period: from injection until the first complete particle exists inside the cell",
          size="small", color=MUT, ha="left")

# ================================================================ B: enveloped animal virus
bio.panel(ax, "B", (15.4, 13.7))
bio.label(ax, (16.2, 13.5), "Enveloped animal virus", size="title", bold=True, ha="left")
ex, ey = 23.0, 8.4
bio.cell(ax, (ex, ey), 3.9, 2.5, kind="animal", zorder=4)
bio.nucleus(ax, (ex + 1.8, ey + 0.9), 0.9, zorder=6)
bio.label(ax, (ex + 1.8, ey - 0.25), "nucleus", size="tiny", color=MUT, zorder=12)
enveloped(ex - 3.3, ey + 1.95)
ax.add_patch(Circle((ex - 2.75, ey + 1.65), 0.13, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=13))
bio.arrow(ax, (ex - 2.95, ey + 1.5), (ex - 2.45, ey + 1.0), kind="process", lw=1.0, head=0.16)
ax.add_patch(Circle((ex - 2.1, ey + 0.45), 0.55, facecolor=P.fill("lysosome"), edgecolor=P.edge("lysosome"), lw=1.0, zorder=8))
enveloped(ex - 2.1, ey + 0.45, r=0.24, spikes=8, zorder=9)
bio.label(ax, (ex - 2.1, ey - 0.45), "endosome,\npH 5–6", size="tiny", color=MUT, zorder=14)
squiggle(ex - 0.85, ey + 0.35, h=0.9, w=0.25, tok="rna", turns=5, lw=1.2, zorder=10)
ax.add_patch(Circle((ex + 0.2, ey - 0.95), 0.72, facecolor=P.fill("er"), edgecolor=P.edge("er"), lw=1.0, zorder=7))
for dx, dy in [(-0.3, 0.25), (0.25, 0.05), (-0.05, -0.35)]:
    squiggle(ex + 0.2 + dx, ey - 0.95 + dy, h=0.45, w=0.14, tok="rna", turns=4, lw=0.9, zorder=9)
bio.label(ax, (ex + 0.2, ey - 1.95), "replication compartment", size="tiny", color=MUT)
for i, (bx, by) in enumerate([(ex + 2.9, ey + 1.5), (ex + 3.5, ey + 0.8), (ex + 3.9, ey + 0.0)]):
    enveloped(bx, by, r=0.32, spikes=8, zorder=13, core=(i > 0))
enveloped(ex + 4.7, ey - 1.1, r=0.4, spikes=9)
bio.arrow(ax, (ex + 4.2, ey - 0.45), (ex + 4.55, ey - 0.78), kind="process", lw=1.0, head=0.16)
step(1, (15.4, 12.3), "attachment to a receptor\n(often a co-receptor as well)")
step(2, (15.4, 11.3), "entry: fusion at the plasma membrane,\nor endocytosis and acid-triggered fusion")
step(3, (15.4, 5.0), "uncoating and transport of the genome")
step(4, (15.4, 3.4), "replication and expression")
step(5, (27.0, 12.3), "assembly at a membrane")
step(6, (27.0, 10.9), "release by budding:\nthe cell may survive")
step(7, (27.0, 5.0), "maturation: a viral protease\ncleaves the precursors")
bio.label(ax, (15.4, 1.5), "eclipse period: from uncoating until the first infectious particle has been assembled",
          size="small", color=MUT, ha="left")
