# Major events in the history of insects on the ICS time scale (ages approximate, Ma). Vertical ticks mark
# fossil events; bars mark molecular-clock estimates (origin of insects ~480 Ma and of winged insects ~405 Ma,
# Misof et al. 2014) and the hexapod gap (~385-325 Ma).
import wikibio as bio
from matplotlib.patches import Circle, Rectangle
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(27, 12)
X0, X1, OLD = 1.0, 26.0, 500.0


def x(age):
    return X0 + (OLD - age) / OLD * (X1 - X0)


phylo.geo_scale(ax, (X0, X1), (OLD, 0.0), y=2.2, ranks=("era", "period"), height=0.45)
for t in range(500, -1, -100):
    ax.plot([x(t), x(t)], [2.25, 2.45], color=P.muted(), lw=0.8)
    bio.label(ax, (x(t), 2.7), "%d Ma" % t if t else "0", size="tiny", color=P.muted())

# molecular estimates and gap (bars)
for a, b, yy, text, tok in ((480, 470, 3.4, "origin of insects (molecular)", "neutral"),
                            (405, 395, 3.4, "origin of Pterygota (molecular)", "neutral"),
                            (385, 325, 3.95, "hexapod gap", "negative")):
    ax.add_patch(Rectangle(
        (x(a), yy - 0.15), x(b) - x(a), 0.3, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=0.7, zorder=5))
    if a == 405:
        bio.label(ax, (x(b) + 0.1, yy), text, size="tiny", color=P.edge(tok), ha="left")
    else:
        bio.label(ax, ((x(a) + x(b)) / 2, yy + 0.38), text, size="tiny", color=P.edge(tok))

events = [
    (410, "Rhynie chert:\noldest hexapods"),
    (325, "first winged\ninsects"),
    (311, "oldest holometabolan\nlarva"),
    (300, "giant\ngriffinflies"),
    (295, "early beetle\nrelatives"),
    (252, "end-Permian\nextinction"),
    (240, "first flies"),
    (225, "first sawflies"),
    (201, "moth scales"),
    (165, "Daohugou: long-proboscid\npollinators"),
    (130, "angiosperms;\nLebanese amber"),
    (99, "Kachin amber:\noldest ants, bees"),
    (66, "K–Pg\nextinction"),
    (44, "Baltic\namber"),
    (18, "Dominican\namber"),
]
levels = [5.2, 6.6, 8.0, 9.4, 10.8]
for k, (age, text) in enumerate(events):
    yy = levels[k % len(levels)]
    tok = "negative" if "extinction" in text else "enzyme"
    ax.plot([x(age), x(age)], [2.7 + 0.2, yy - 0.45], color=P.edge(tok), lw=0.8, zorder=4)
    ax.add_patch(Circle((x(age), 2.95), 0.1,
                 facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=6))
    bio.label(ax, (x(age), yy), text, size="tiny")
bio.label(ax, (13.5, 0.6), "Ages approximate; bars: molecular-clock estimates and the gap in the fossil record",
          size="tiny", color=P.muted())
