# Types of embryo sac development, by the number of megaspore nuclei that take part (monosporic,
# bisporic, tetrasporic). For each type: the products of meiosis in the megasporocyte (walls drawn as
# lines; grey = degenerating) and the mature embryo sac (micropylar end at the top), with the ploidy of
# the polar nuclei. Polygonum (most angiosperms), Oenothera (Onagraceae; four-celled), Allium (bisporic),
# Fritillaria (Lilium; tetrasporic, three chalazal nuclei fuse, chalazal polar nucleus and antipodals 3n)
# and Peperomia (sixteen nuclei, eight polar nuclei).
from matplotlib.patches import Circle, Ellipse, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 10.4)


def nuc(p, r=0.13, tok="nucleus", z=9):
    ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=z))


def tetrad(x, y, walls, alive):
    """Four megaspore positions in a column (top = micropylar); walls: indices of boundaries 0..2 drawn."""
    ax.add_patch(Rectangle((x - 0.45, y - 1.4), 0.9, 2.8, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"),
                           lw=0.9, zorder=6))
    for b in walls:
        yy = y + 0.7 - 0.7 * b
        ax.plot([x - 0.45, x + 0.45], [yy, yy], color=P.edge("cytoplasm"), lw=1.6, zorder=7)
    for i in range(4):
        yy = y + 1.05 - 0.7 * i
        ok = i in alive
        if not ok:
            ax.add_patch(Rectangle((x - 0.44, yy - 0.34), 0.88, 0.68, facecolor=P.fill("neutral"), edgecolor="none", zorder=6.5))
        nuc((x, yy), 0.13, tok="nucleus" if ok else "neutral")


def mature(x, y, egg=True, syn=2, anti=3, polar=("n", "n"), cells=None, extra=None):
    ax.add_patch(Ellipse((x, y), 1.6, 3.4, facecolor=P.fill("vacuole"), edgecolor=P.edge("cytoplasm"), lw=1.1, zorder=6))
    for k in range(syn):
        dx = (k - (syn - 1) / 2) * 0.55
        ax.add_patch(Ellipse((x + dx, y + 1.25), 0.45, 0.75, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.8,
                             zorder=8))
    ax.add_patch(Ellipse((x, y + 0.85), 0.5, 0.7, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.9, zorder=9))
    for k in range(anti):
        dx = (k - (anti - 1) / 2) * 0.42
        ax.add_patch(Ellipse((x + dx, y - 1.3), 0.4, 0.4, facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=0.8,
                             zorder=8))
    n = len(polar)
    per = 4 if n > 4 else n
    for k, pl in enumerate(polar):
        i, j = k % per, k // per
        dx = (i - (per - 1) / 2) * 0.28
        dy = 0.0 if n <= 4 else (0.14 - 0.28 * j)
        nuc((x + dx, y + dy), 0.12, tok="highlight")
    if extra:
        extra(x, y)


rows = [
    ("Polygonum", "monosporic", [0, 1, 2], [3], dict(polar=("n", "n")), "8 nuclei, 7 cells; polar nuclei n + n"),
    ("Oenothera", "monosporic", [0, 1, 2], [0], dict(anti=0, polar=("n",)), "4 nuclei, 4 cells; one polar nucleus"),
    ("Allium", "bisporic", [1], [2, 3], dict(polar=("n", "n")), "8 nuclei, 7 cells (two megaspore nuclei)"),
    ("Fritillaria", "tetrasporic", [], [0, 1, 2, 3], dict(polar=("n", "3n")), "8 nuclei; chalazal polar nucleus and antipodals 3n"),
    ("Peperomia", "tetrasporic", [], [0, 1, 2, 3], dict(syn=1, anti=0, polar=tuple("n" * 8)), "16 nuclei; egg, 1 synergid, 6 lateral cells, 8 polar nuclei"),
]
for k, (name, kind, walls, alive, kw, note) in enumerate(rows):
    x = 3.0 + 5.9 * k
    bio.label(ax, (x, 10.0), name, size="small", bold=True, italic=False)
    bio.label(ax, (x, 9.5), kind, size="tiny", color=P.muted())
    tetrad(x - 1.15, 6.9, walls, alive)
    bio.arrow(ax, (x - 0.55, 6.9), (x + 0.25, 6.9), kind="process", head=0.12)
    mature(x + 1.25, 6.9, **kw)
    bio.label(ax, (x, 4.6), note, size="tiny", color=P.ink())
    if name == "Peperomia":
        for dy in (0.55, -0.55):
            for dx in (-0.55, 0.55):
                ax.add_patch(Ellipse((x + 1.25 + dx, 6.9 + dy), 0.35, 0.4, facecolor=P.fill("chloroplast"),
                                     edgecolor=P.edge("chloroplast"), lw=0.7, zorder=8))
        for dy in (-1.3,):
            for dx in (-0.25, 0.25):
                ax.add_patch(Ellipse((x + 1.25 + dx, 6.9 + dy), 0.35, 0.4, facecolor=P.fill("chloroplast"),
                                     edgecolor=P.edge("chloroplast"), lw=0.7, zorder=8))
bio.label(ax, (3.0, 8.75), "meiosis products", size="tiny", color=P.muted())
leg = [("receptor", "Synergid"), ("ovule", "Egg cell"), ("highlight", "Polar nucleus"), ("chloroplast", "Antipodal / lateral cell"),
       ("neutral", "Degenerating")]
for k, (tok, t) in enumerate(leg):
    x = 2.0 + 5.4 * k
    bio.box(ax, (x, 3.4), 0.34, 0.34, token=tok, radius=0.06)
    bio.label(ax, (x + 0.3, 3.4), t, size="small", ha="left")
bio.label(ax, (15.0, 2.2), "Primary endosperm nucleus (with one sperm): Polygonum, Allium 3n; Oenothera 2n; Fritillaria 5n; Peperomia 9n",
          size="small")
bio.label(ax, (15.0, 1.4), "Micropylar end at the top of each drawing", size="tiny", color=P.muted())
