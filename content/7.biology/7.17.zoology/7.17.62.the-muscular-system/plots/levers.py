# Three classes of lever, and the output force-velocity curves of a Hill-type muscle acting through levers
# of different mechanical advantage (Example 62.7.2). Model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23, 9.4)

bio.panel(ax, "A", (0.3, 9.0))
bio.label(ax, (0.9, 9.0), "Classes of lever", size="title", ha="left")


def lever(y, f_x, e_x, l_x, e_up, title):
    x0, x1 = 1.0, 8.2
    ax.plot([x0, x1], [y, y], color=P.edge("bone"), lw=5, solid_capstyle="round", zorder=4)
    ax.plot([x0, x1], [y, y], color=P.fill("bone"), lw=3.4, solid_capstyle="round", zorder=5)
    tri = np.array([(f_x, y - 0.08), (f_x - 0.3, y - 0.6), (f_x + 0.3, y - 0.6)])
    bio.shape(ax, tri, token="neutral", zorder=3, lw=0.8)
    if e_up:
        bio.arrow(ax, (e_x, y + 0.12), (e_x, y + 1.0), kind="process", color=P.edge("muscle"), lw=1.8)
    else:
        bio.arrow(ax, (e_x, y + 1.0), (e_x, y + 0.12), kind="process", color=P.edge("muscle"), lw=1.8)
    bio.arrow(ax, (l_x, y + 1.0), (l_x, y + 0.12), kind="process", color=P.muted(), lw=1.8)
    bio.label(ax, (f_x, y - 0.85), "F", size="tiny")
    bio.label(ax, (e_x + 0.25, y + 0.85), "E", size="tiny", ha="left", color=P.edge("muscle"))
    bio.label(ax, (l_x + 0.25, y + 0.85), "L", size="tiny", ha="left")
    bio.label(ax, (x0, y + 1.45), title, size="small", ha="left")


lever(6.7, 4.0, 6.8, 1.6, False, "first class (head balanced on the atlas)")
lever(3.95, 1.3, 7.6, 4.4, True, "second class (rising on the toes)")
lever(1.2, 1.3, 2.6, 7.6, True, "third class (biceps flexing the elbow)")
bio.label(ax, (4.6, 0.0), "E: muscle force; L: load; F: fulcrum (joint)", size="tiny", color=P.muted())

bio.panel(ax, "B", (10.0, 9.0))
p = quant.Plot(ax, (12.0, 1.4, 9.6, 6.9), xlim=(0, 4.2), ylim=(0, 1.05), xlabel="output velocity (units of v_max for m = 1)",
               ylabel="output force / F0", xticks=[0, 1, 2, 3, 4], yticks=[0, 0.25, 0.5, 0.75, 1.0])
k = 0.25
for m, tok in ((1.0, "muscle"), (0.5, "enzyme"), (0.25, "dna")):
    v = np.linspace(0, 1 / m, 300)
    vm = m * v
    f = m * (1 - vm) / (1 + vm / k)
    p.line(v, f, tok)
    p.text(0.1, m + 0.035, f"m = {m:g}", size="tiny", color=quant.line_color(tok), ha="left")
    p.line(v, f * v * 5, tok, dashed=True, lw=1.1)
p.text(3.0, 0.62, "dashed: output power × 5", size="tiny", color=P.muted())
p.text(3.0, 0.55, "(same maximum for every m)", size="tiny", color=P.muted())
