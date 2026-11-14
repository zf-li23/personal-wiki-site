# Some of Hockett's (1960) design features of language in five communication systems: the honey bee waggle
# dance, vervet monkey alarm calls, songbird song, symbols used by language-trained apes, and human language.
# Filled: present; half-filled: limited or debated; empty: absent. Assessments follow Hockett (1960),
# Hauser (1996) and Fitch (2010): the dance refers to absent food (displacement) but is graded and partly
# iconic; vervet calls are arbitrary and functionally referential but innate in form and not combined;
# songs are learned and recombine syllables without changing meaning; trained apes use arbitrary symbols,
# sometimes for absent things, with little syntax.
from matplotlib.patches import Circle, Wedge

import wikibio as bio

P = bio.P
features = ["Vocal-auditory channel", "Semanticity", "Arbitrariness", "Discreteness", "Displacement",
            "Productivity", "Duality of patterning", "Cultural transmission", "Interchangeability"]
systems = ["Honey bee\ndance", "Vervet\nalarm calls", "Songbird\nsong", "Trained\napes", "Human\nlanguage"]
# 2 = present, 1 = limited or debated, 0 = absent
M = [
    [0, 2, 2, 0, 2],
    [2, 2, 0, 2, 2],
    [1, 2, 2, 2, 2],
    [0, 2, 2, 2, 2],
    [2, 0, 0, 1, 2],
    [1, 0, 1, 1, 2],
    [0, 0, 0, 0, 2],
    [0, 1, 2, 1, 2],
    [1, 2, 1, 2, 2],
]
fig, ax = bio.canvas(18, 11.6)
x0, y0, dx, dy = 7.6, 9.4, 2.2, 0.95
for j, s in enumerate(systems):
    bio.label(ax, (x0 + j * dx, y0 + 1.1), s, size="small")
for i, f in enumerate(features):
    y = y0 - i * dy
    bio.label(ax, (x0 - 1.2, y), f, size="small", ha="right")
    ax.plot([x0 - 1.0, x0 + 4.4 * dx], [y - dy / 2, y - dy / 2], color=P.muted(), lw=0.4)
    for j in range(5):
        c = (x0 + j * dx, y)
        v = M[i][j]
        tok = "positive" if j == 4 else "dna"
        r = 0.28
        ax.add_patch(Circle(c, r, facecolor="none", edgecolor=P.edge(tok), lw=1.2, zorder=5))
        if v == 2:
            ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=6))
        elif v == 1:
            ax.add_patch(Wedge(c, r, 90, 270, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=6))
yk = y0 - len(features) * dy - 0.3
for k, (v, t) in enumerate([(2, "present"), (1, "limited or debated"), (0, "absent")]):
    c = (x0 - 3.0 + k * 3.6, yk)
    ax.add_patch(Circle(c, 0.22, facecolor="none", edgecolor=P.edge("dna"), lw=1.2))
    if v == 2:
        ax.add_patch(Circle(c, 0.22, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.2))
    elif v == 1:
        ax.add_patch(Wedge(c, 0.22, 90, 270, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.2))
    bio.label(ax, (c[0] + 0.4, c[1]), t, size="small", ha="left")
