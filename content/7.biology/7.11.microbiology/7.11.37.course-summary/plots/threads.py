"""The threads of the course: which chapters (columns, 7.11.1-7.11.36) carry each of the eight
threads (rows). Large dots: the thread is a main subject of the chapter; small dots: the chapter
uses or extends it. Bands at the top mark the blocks of the course."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

THREADS = [  # (label, token, main chapters, secondary chapters)
    ("Cell structure", "cell_wall", [1, 2, 3, 8], [12, 18, 19, 20, 21, 34]),
    ("Metabolism and energy", "enzyme", [4, 5, 6, 7], [9, 17, 18, 19, 29, 30, 31, 36]),
    ("Growth and its control", "positive", [8, 9, 10, 14, 15], [4, 12, 23, 28, 36]),
    ("Regulation and genetics", "dna", [11, 12, 13], [15, 16, 23, 24, 25, 33, 34]),
    ("Diversity and systematics", "protein", [16, 17, 18, 19, 20, 21], [1, 26, 29]),
    ("Viruses", "virus", [22, 23, 24, 25, 26, 27, 28], [13, 29, 35]),
    ("Ecology and cycles", "channel", [29, 30, 31], [6, 7, 12, 17, 26, 32]),
    ("Microbes and humans", "blood", [14, 15, 28, 32, 33, 34, 35, 36], [1, 10, 20, 21, 27]),
]
BLOCKS = [(1, 1, "intro"), (2, 3, "cell"), (4, 7, "metabolism"), (8, 10, "growth"),
          (11, 13, "regulation,\ngenetics"), (14, 15, "drugs"), (16, 21, "diversity"),
          (22, 28, "viruses"), (29, 31, "ecology"), (32, 36, "microbes and humans")]

n = 36
x0, dx = 8.2, 0.52
nrow = len(THREADS)
fig, ax = bio.canvas(x0 + n * dx + 0.6, nrow * 0.9 + 2.9)
ytop = nrow * 0.9 + 0.4


def X(c):
    return x0 + (c - 1) * dx


for k, (lo, hi, name) in enumerate(BLOCKS):
    xa, xb = X(lo) - dx * 0.45, X(hi) + dx * 0.45
    col = P.mix(P.fill("neutral"), P.surface(), 0.55 if k % 2 == 0 else 0.8)
    ax.add_patch(plt.Rectangle((xa, 0.35), xb - xa, ytop - 0.35, color=col, zorder=0, lw=0))
    ax.text((xa + xb) / 2, ytop + 0.2, name, ha="center", va="bottom", fontsize=FT["tiny"], color=P.ink())

for i, (lab, tok, main, sec) in enumerate(THREADS):
    y = ytop - 0.5 - i * 0.9
    ax.text(x0 - 0.5, y, lab, ha="right", va="center", fontsize=FT["small"], color=P.ink())
    ax.plot([X(1), X(n)], [y, y], color=P.mix(P.muted(), P.surface(), 0.5), lw=0.5, zorder=1)
    ax.scatter([X(c) for c in main], [y] * len(main), s=95, color=P.fill(tok),
               edgecolor=charts.line(tok), lw=1.0, zorder=3)
    ax.scatter([X(c) for c in sec], [y] * len(sec), s=26, color=P.fill(tok),
               edgecolor=charts.line(tok), lw=0.8, zorder=3)

for c in range(1, n + 1):
    ax.text(X(c), 0.05, str(c), ha="center", va="top", fontsize=FT["tiny"], color=P.muted())
ax.text(X(1) + (X(n) - X(1)) / 2, -0.55, "chapter 7.11.k", ha="center", va="top",
        fontsize=FT["small"], color=P.muted())
ax.set_ylim(-1.1, ytop + 1.2)
