# Hierarchical binning used by the BAM, CRAM, BCF and tabix indexes, with the top three levels drawn (the real
# scheme has six, from 512 Mb down to 16 kb, each 8 times finer). Each record is stored in the smallest bin that
# contains it entirely, so a short record that crosses a bin boundary goes up a level (here even to bin 0).
# A query for one position examines one bin per level (shaded) and tests only the records stored there for
# overlap; records in other bins are never read.
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 8.6)
x0, x1 = 3.0, 19.4
W = x1 - x0
ytop = 7.4
h = 0.62
gap = 1.45
q = 0.40  # query position as a fraction of the genome


def X(f):
    return x0 + f * W


for li in range(3):
    n = 8 ** li
    y = ytop - li * gap
    w = W / n
    first = (8 ** li - 1) // 7
    for k in range(n):
        hit = k == int(q * n)
        fc = P.fill("highlight") if hit else P.light("neutral")
        ax.add_patch(Rectangle((x0 + k * w, y - h / 2), w, h, facecolor=fc, edgecolor=P.edge("neutral"),
                               lw=0.4 if n > 8 else 0.7, zorder=3))
        if n <= 8 or hit:
            bio.label(ax, (x0 + (k + 0.5) * w, y + (0 if n <= 8 else 0.62)), str(first + k), size="tiny",
                      color=P.on_fill() if n <= 8 else P.ink(), zorder=6)
    bio.label(ax, (x0 - 0.2, y), f"level {li}: {n} bin{'s' if n > 1 else ''}", size="small", ha="right")
ax.plot([X(q), X(q)], [0.3, ytop + 0.6], color=P.edge("negative"), lw=1.2, ls=(0, (4, 2)), zorder=8)
bio.label(ax, (X(q), ytop + 0.85), "query position", size="small", color=P.edge("negative"))
ax.plot([X(0.375), X(0.375)], [0.3, ytop - 2 * gap - 0.4], color=P.muted(), lw=0.8, ls=(0, (1, 2)), zorder=2)
bio.label(ax, (X(0.375) - 0.1, 0.45), "bin boundary 3/8", size="tiny", ha="right", color=P.muted())


def smallest_bin(s, e):
    for lev in (2, 1):
        n = 8 ** lev
        if int(s * n) == int(e * n):
            return lev, (8 ** lev - 1) // 7 + int(s * n)
    return 0, 0


examined = {0, 1 + int(q * 8), 9 + int(q * 64)}
recs = [(0.392, 0.404), (0.38, 0.47), (0.26, 0.37), (0.3735, 0.3765), (0.12, 0.30), (0.50, 0.53)]
yr = 0.8
for i, (s, e) in enumerate(recs):
    yy = yr + i * 0.4
    lev, b = smallest_bin(s, e)
    if b in examined and s <= q <= e:
        tok, note = "positive", "examined, overlaps"
    elif b in examined:
        tok, note = "neutral", "examined, no overlap"
    else:
        tok, note = None, "not read"
    col = P.edge(tok) if tok else P.muted()
    ax.plot([X(s), X(e)], [yy, yy], color=col, lw=3.2 if tok else 1.4, solid_capstyle="butt", zorder=5,
            ls="-" if tok else (0, (3, 1.5)))
    bio.label(ax, (X(0.56), yy), f"bin {b} (level {lev}): {note}", size="tiny", ha="left",
              color=P.ink() if tok else P.muted())
bio.label(ax, (x0 - 0.2, yr + 1.0), "records", size="small", ha="right")
