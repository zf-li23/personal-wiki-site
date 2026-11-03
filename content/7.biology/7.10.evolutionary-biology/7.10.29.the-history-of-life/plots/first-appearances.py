"""First appearances of some major groups in the fossil record (approximate dates in Mya; bars to the present
or to extinction), on the ICS periods; red triangles mark the five largest mass extinctions."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(26, 12)
x0, x1 = 6.5, 25.5


def X(a):
    return x0 + (560 - a) / 560 * (x1 - x0)


ROWS = [("trilobites", 521, 252, "neutral"), ("vertebrates", 518, 0, "animal"), ("jawed fishes", 430, 0, "animal"),
        ("vascular plants", 430, 0, "plant"), ("insects", 410, 0, "positive"), ("tetrapods", 370, 0, "animal"),
        ("amniotes", 318, 0, "animal"), ("nonavian dinosaurs", 230, 66, "neutral"), ("mammaliaforms", 210, 0, "animal"),
        ("birds", 150, 0, "animal"), ("angiosperms", 130, 0, "plant"), ("grasslands", 30, 0, "plant"),
        ("hominins", 7, 0, "animal")]
top = 11.0
for k, (name, a, b, tok) in enumerate(ROWS):
    y = top - 0.72 * k
    bio.box(ax, ((X(a) + X(b)) / 2, y), max(X(b) - X(a), 0.15), 0.42, tok, radius=0.08, lw=0.6)
    bio.label(ax, (x0 - 0.2, y), name, size="small", ha="right")
yb = top - 0.72 * len(ROWS) + 0.2
phylo.geo_scale(ax, (x0, x1), (560, 0), yb, ranks=("era", "period"), height=0.55)
for a in (500, 400, 300, 200, 100, 0):
    ax.plot([X(a), X(a)], [yb - 1.1, yb - 1.25], color=P.muted(), lw=0.7)
    bio.label(ax, (X(a), yb - 1.5), str(a), size="tiny", color=P.muted())
bio.label(ax, ((x0 + x1) / 2, yb - 2.0), "millions of years ago", size="small", color=P.muted())
for a in (445, 372, 252, 201.4, 66):
    ax.plot([X(a)], [top + 0.55], marker="v", ms=8, color=P.edge("negative"))
