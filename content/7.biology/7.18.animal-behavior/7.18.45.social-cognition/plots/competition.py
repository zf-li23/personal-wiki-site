# The competitive paradigm of Hare, Call and Tomasello (2000, 2001), top views. A subordinate (S) and a
# dominant (D) chimpanzee are housed in rooms on opposite sides of a central area; when the doors are
# raised, the subordinate is given a short head start. A: one food item is visible to both, a second is
# behind an opaque barrier on the subordinate's side, visible only to the subordinate: subordinates went
# for the hidden item. B: the dominant either watched the food being hidden behind a barrier (informed)
# or its door was closed during baiting (uninformed); subordinates approached the food more often when
# the dominant was uninformed, or when the dominant that had watched was replaced by another dominant.
from matplotlib.patches import Circle, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 9.6)


def arena(x0, y0, title, barriers, foods, eye_lines, door_d="open"):
    w, h = 9.4, 5.6
    for xx, ww, tok in ((x0, 1.6, "dna"), (x0 + w - 1.6, 1.6, "rna")):
        ax.add_patch(Rectangle((xx, y0), ww, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, alpha=0.35))
    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, edgecolor=P.ink(), lw=1.4))
    bio.label(ax, (x0 + 0.8, y0 + h / 2), "S", size="normal", bold=True)
    bio.label(ax, (x0 + w - 0.8, y0 + h / 2), "D", size="normal", bold=True)
    if door_d == "closed":
        ax.plot([x0 + w - 1.6, x0 + w - 1.6], [y0, y0 + h], color=P.ink(), lw=3.2)
    for bx, by, bh in barriers:
        ax.add_patch(Rectangle((bx - 0.12, by - bh / 2), 0.24, bh, facecolor=P.fill("neutral"),
                               edgecolor=P.edge("neutral"), lw=1.0, zorder=6))
    for fx, fy in foods:
        ax.add_patch(Circle((fx, fy), 0.28, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.9, zorder=7))
    for (a, b), tok in eye_lines:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(tok), lw=0.9, ls=(0, (3, 2)), zorder=5)
    bio.label(ax, (x0 + w / 2, y0 + h + 0.5), title, size="small")


bio.panel(ax, "A", (0.3, 9.2))
x0, y0 = 1.0, 1.8
arena(x0, y0, "Food visible to both vs. hidden from the dominant",
      barriers=[(x0 + 3.4, y0 + 1.5, 1.3)],
      foods=[(x0 + 4.7, y0 + 4.0), (x0 + 3.0, y0 + 1.5)],
      eye_lines=[(((x0 + 8.6, y0 + 2.8), (x0 + 4.9, y0 + 3.95)), "rna"),
                 (((x0 + 8.6, y0 + 2.8), (x0 + 3.6, y0 + 1.5)), "negative")])
bio.callout(ax, (x0 + 3.0, y0 + 1.25), (x0 + 3.0, y0 - 0.7), "seen only by S: S goes here")
bio.callout(ax, (x0 + 4.7, y0 + 4.25), (x0 + 6.2, y0 + 5.0), "seen by both")

bio.panel(ax, "B", (12.3, 9.2))
x1 = 13.6
arena(x1, y0, "Dominant uninformed (door closed during baiting)",
      barriers=[(x1 + 4.2, y0 + 2.8, 1.4)],
      foods=[(x1 + 3.8, y0 + 2.8)],
      eye_lines=[(((x1 + 1.3, y0 + 2.8), (x1 + 3.6, y0 + 2.8)), "dna")], door_d="closed")
bio.callout(ax, (x1 + 3.8, y0 + 2.55), (x1 + 3.0, y0 - 0.7), "food behind barrier: S approaches it more")
bio.callout(ax, (x1 + 7.8, y0 + 4.2), (x1 + 8.6, y0 + 6.5), "D's door closed")
