"""The human embryonic period (days after fertilization, approximate; Carnegie stages CS1-CS23).

Bands: preimplantation development (days 0-6), implantation and the bilaminar disc (week 2), gastrulation
(week 3), neurulation and somitogenesis (weeks 3-4), organogenesis (to the end of week 8). Events: zygote
(CS1, day 1), morula (day 3-4), blastocyst (CS3, day 4-5), implantation begins (CS4-5, day 6-7), primitive
streak (CS6, day 14-15), neural plate (day 18-19), first somites (CS9, day 20), heart begins to beat (day
21-22), anterior neuropore closes (CS11, day 24-26), posterior neuropore closes (CS12, day 26-28), upper
limb buds (CS12, day 26-28), lower limb buds (CS13, day 28-30), end of the embryonic period (CS23, day 56).
Gestational age, counted from the last menstrual period, is about 14 days more.
"""

from matplotlib.patches import Circle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(28, 8.4)
p = quant.Plot(ax, (1.2, 3.8, 25.8, 0.6), xlim=(0, 60), ylim=(0, 1), xlabel="days after fertilization",
               xticks=[0, 7, 14, 21, 28, 35, 42, 49, 56], frame=None)
ax.plot([p.X(0), p.X(60)], [3.8, 3.8], color=P.ink(), lw=1.6, zorder=5)
for d in range(0, 61, 7):
    ax.plot([p.X(d), p.X(d)], [3.8, 3.7], color=P.ink(), lw=1.0, zorder=5)
bands = [(0, 6, "cytoplasm", "preimplantation"), (6, 14, "receptor", "implantation,\nbilaminar disc"),
         (14, 21, "highlight", "gastrulation"), (21, 28, "ectoderm", "neurulation,\nsomites"), (28, 56, "positive", "organogenesis")]
for a, b, tok, text in bands:
    bio.box(ax, ((p.X(a) + p.X(b)) / 2, 4.15), p.X(b) - p.X(a) - 0.05, 0.55, tok, radius=0.06)
    bio.label(ax, ((p.X(a) + p.X(b)) / 2, 2.55 if text.count("\n") else 2.75), text, size="tiny", color=P.muted())
events = [(1, "zygote (CS1)", 1), (3.5, "morula", 2), (4.5, "blastocyst (CS3)", 3), (6.5, "implantation\nbegins", 4),
          (14.5, "primitive streak (CS6)", 1), (18.5, "neural plate", 2), (20, "first somites (CS9)", 3), (21.5, "heartbeat", 4),
          (25, "anterior neuropore\ncloses (CS11)", 1), (27, "posterior neuropore\ncloses; arm buds (CS12)", 2.6),
          (29, "leg buds (CS13)", 4), (56, "end of embryonic\nperiod (CS23)", 1.5)]
for d, text, lev in events:
    x = float(p.X(d))
    y = 4.5 + 0.7 * lev
    ax.plot([x, x], [4.45, y - 0.05], color=P.muted(), lw=0.7, zorder=4)
    ax.add_patch(Circle((x, 4.45), 0.07, color=P.ink(), zorder=6))
    bio.label(ax, (x + 0.08, y), text, size="tiny", ha="left", va="bottom")
bio.label(ax, (p.X(42), 1.85), "gestational age (from the last menstrual period) is about 2 weeks more", size="tiny",
          color=P.muted())

# trim the empty band at the bottom
ax.set_ylim(1.4, 8.4)
fig.set_size_inches(28 * 0.45, 7.0 * 0.45)
