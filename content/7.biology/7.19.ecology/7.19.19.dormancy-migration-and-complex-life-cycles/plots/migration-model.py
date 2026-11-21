"""Why migrate? A simple model of residency, migration and partial migration.

Residents survive winter with probability exp(-w), where w measures winter severity, and gain a breeding
advantage from early territory settlement; migrants survive the journey and the winter with probability
0.6 whatever the winter. Breeding success: migrants 1; residents 1 + a (1 - f), where f is the fraction of
the population that stays (residents compete with each other for the best territories), a = 0.8.
A: fitness of a resident (f = 0 and f = 1) and of a migrant against winter severity: pure residency is
favored in mild winters, pure migration in severe ones.
B: the evolutionarily stable fraction of residents f* (equal fitness of the two tactics; f* = 0 or 1 at
the limits) against winter severity: in between, partial migration is stable.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(21.0, 10.0)
a, Sm = 0.8, 0.6
w = np.linspace(0, 2, 400)

pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
pa.plot(w, np.exp(-w) * (1 + a), color=Q.line_color("positive"), lw=1.6, label="resident, others migrate (f = 0)")
pa.plot(w, np.exp(-w), color=Q.line_color("positive"), lw=1.2, ls=(0, (4, 2)), label="resident, all stay (f = 1)")
pa.axhline(Sm, color=Q.line_color("dna"), lw=1.6, label="migrant")
pa.set_xlim(0, 2)
pa.set_ylim(0, 2)
C.style_axes(pa, "winter severity w", "fitness (survival x breeding)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Stay or go", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.5, 1.6, 7.5, 6.8))
f = np.clip((1 - Sm * np.exp(w)) / a + 1, 0, 1)
pb.plot(w, f, color=Q.line_color("protein"), lw=1.8)
w0, w1 = np.log(1 / Sm), np.log((1 + a) / Sm)
for x in (w0, w1):
    pb.axvline(x, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(w0 / 2, 0.5, "all\nresident", fontsize=FS["tiny"], color=P.ink(), ha="center")
pb.text((w0 + w1) / 2, 1.03, "partial migration", fontsize=FS["tiny"], color=P.ink(), ha="center")
pb.text((w1 + 2) / 2, 0.5, "all\nmigrate", fontsize=FS["tiny"], color=P.ink(), ha="center")
pb.set_xlim(0, 2)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "winter severity w", "stable fraction of residents f*")
bio.panel(ax, "B", (10.8, 9.6))
bio.label(ax, (12.5, 9.2), "Partial migration", size="small", bold=True, ha="left")
