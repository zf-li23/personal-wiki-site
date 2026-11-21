"""When should an insect stop breeding and enter diapause? (after Cohen 1970)

An adult on date t can either lay diapausing eggs, each of which survives the winter (value 1), or lay
m non-diapausing eggs that develop into a new generation within tau = 30 days; that generation counts
only if it completes development before the season ends. The end of the season is random, normal with
mean T and standard deviation 10 days. Breeding again pays if m P(end > t + tau) > 1, so the switch date
t* satisfies P(end > t* + tau) = 1/m.
A: m P(end > t + tau) against the date for m = 5 and 20 (T = day 270); diapause is favored where the
curve falls below 1 (points: t*).
B: the switch date against the mean end of the season T for m = 5 and 20, compared with the date T - tau
(dashed) at which the last generation would just finish in an average year: the switch date tracks the
season, and a high payoff m of a further generation justifies gambling on a late end of the season.
"""

import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(21.0, 10.0)
tau, sd = 30.0, 10.0
t = np.linspace(180, 260, 400)

pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
for m, tok in [(5, "dna"), (20, "negative")]:
    val = m * norm.sf(t + tau, loc=270, scale=sd)
    pa.plot(t, val, color=Q.line_color(tok), lw=1.6, label=f"m = {m}")
    ts = 270 + sd * norm.isf(1 / m) - tau
    pa.plot(ts, 1, "o", ms=5, color=Q.line_color(tok))
pa.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(182, 1.4, "value of a diapausing egg = 1", fontsize=FS["tiny"], color=P.ink())
pa.set_yscale("log")
pa.set_xlim(180, 260)
pa.set_ylim(0.05, 30)
C.style_axes(pa, "date t (day of year)", "expected value of breeding again")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Breed again or diapause", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.5, 1.6, 7.5, 6.8))
T = np.linspace(220, 320, 200)
for m, tok in [(5, "dna"), (20, "negative")]:
    pb.plot(T, T + sd * norm.isf(1 / m) - tau, color=Q.line_color(tok), lw=1.6, label=f"m = {m}")
pb.plot(T, T - tau, color=P.muted(), lw=0.9, ls=(0, (4, 2)), label="T - tau")
pb.set_xlim(220, 320)
C.style_axes(pb, "mean end of season T (day of year)", "switch date t*")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.8, 9.6))
bio.label(ax, (12.5, 9.2), "Shorter seasons, earlier diapause", size="small", bold=True, ha="left")
