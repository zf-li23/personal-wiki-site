# Heterostyly. A: distyly (e.g. Primula): pin flowers with a long style and anthers low in the corolla
# tube, thrum flowers with a short style and anthers at the mouth of the tube; pollen picked up at one
# height on the body of an insect is deposited on stigmas at the same height, so legitimate pollination
# is between morphs (arrows). B: tristyly (e.g. Lythrum salicaria): long-, mid- and short-styled morphs,
# each with two levels of stamens at the heights of the other two stigmas.
from matplotlib.patches import Circle, Ellipse, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 10.0)
H = {"L": 7.4, "M": 5.6, "S": 3.8}


def flower(x, style, anthers, name):
    base = 1.6
    ax.add_patch(Polygon([(x - 0.55, base), (x + 0.55, base), (x + 0.65, 8.2), (x - 0.65, 8.2)], closed=True,
                         facecolor=P.light("petal"), edgecolor=P.edge("petal"), lw=1.0, zorder=4))
    for s in (-1, 1):
        ax.add_patch(Ellipse((x + s * 1.3, 8.45), 1.9, 0.55, angle=s * 12, facecolor=P.fill("petal"),
                             edgecolor=P.edge("petal"), lw=1.0, zorder=5))
    ax.add_patch(Ellipse((x, base + 0.45), 0.7, 0.9, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=6))
    ax.plot([x, x], [base + 0.9, H[style]], color=P.edge("ovary"), lw=1.6, zorder=6)
    ax.add_patch(Circle((x, H[style] + 0.12), 0.2, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=0.9, zorder=7))
    for a in anthers:
        for s in (-1, 1):
            ax.plot([x + s * 0.5, x + s * 0.38], [H[a] - 1.0, H[a]], color=P.edge("anther"), lw=1.0, zorder=6)
            ax.add_patch(Ellipse((x + s * 0.38, H[a] + 0.12), 0.24, 0.42, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                                 lw=0.8, zorder=7))
    bio.label(ax, (x, 0.9), name, size="small", bold=True)


bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (5.4, 9.6), "Distyly", size="normal", bold=True)
flower(3.0, "L", ["S"], "Pin (long style)")
flower(8.0, "S", ["L"], "Thrum (short style)")
bio.arrow(ax, (3.5, H["S"] + 0.1), (7.8, H["S"] + 0.15), kind="process", bend=0.25, color=P.edge("highlight"))
bio.arrow(ax, (7.6, H["L"] + 0.1), (3.2, H["L"] + 0.2), kind="process", bend=0.25, color=P.edge("highlight"))

bio.panel(ax, "B", (11.2, 9.8))
bio.label(ax, (18.6, 9.6), "Tristyly", size="normal", bold=True)
flower(13.8, "L", ["M", "S"], "Long-styled")
flower(18.6, "M", ["L", "S"], "Mid-styled")
flower(23.4, "S", ["L", "M"], "Short-styled")
for lev, tok in (("L", "positive"), ("M", "highlight"), ("S", "negative")):
    ax.plot([12.4, 25.0], [H[lev] + 0.12] * 2, color=P.edge(tok), lw=0.8, ls=(0, (3, 3)), zorder=3)
bio.label(ax, (25.2, H["L"] + 0.12), "long level", size="tiny", ha="left", color=P.muted())
bio.label(ax, (25.2, H["M"] + 0.12), "mid level", size="tiny", ha="left", color=P.muted())
bio.label(ax, (25.2, H["S"] + 0.12), "short level", size="tiny", ha="left", color=P.muted())
bio.label(ax, (5.5, 0.3), "arrows: legitimate (intermorph) pollen transfer", size="tiny", color=P.muted())
