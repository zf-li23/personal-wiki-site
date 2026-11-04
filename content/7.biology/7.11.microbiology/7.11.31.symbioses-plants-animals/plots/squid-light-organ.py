"""Daily cycle of the squid light organ (illustrative model). Each dawn the squid expels 90 % of its
Aliivibrio fischeri; the rest regrow logistically (r = 0.45 per h, capacity K). The autoinducer
concentration follows cell density (A = N/K in relative units), and light per cell is a Hill function of A
(threshold 0.5, n = 4), so the organ is dark while the population regrows and bright from evening on."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 8.6)

r, frac_kept, Kh, nh = 0.45, 0.1, 0.5, 4
t = np.linspace(0, 48, 2401)
N = np.empty_like(t)
n = frac_kept  # just after the first dawn expulsion
dt = t[1] - t[0]
dawn2 = int(round(24 / dt))
for i in range(len(t)):
    if i > 0:
        n += r * n * (1 - n) * dt
    if i == dawn2:  # second dawn: expel 90 %
        n *= frac_kept
    N[i] = n
A = N
per_cell = A**nh / (Kh**nh + A**nh)
light = N * per_cell

bio.panel(ax, "A", (0.2, 8.4))
p = quant.Plot(ax, (1.8, 1.6, 12.6, 5.8), xlim=(0, 48), ylim=(0, 1.05), xlabel="hours after dawn",
               ylabel="relative level", xticks=[0, 6, 12, 18, 24, 30, 36, 42, 48], yticks=[0, 0.5, 1])
for a, b in ((12, 24), (36, 48)):
    p.span(a, b, "neutral", text="night", strength=0.35)
p.line(t, N, token="bacterium")
p.text(13, 1.03, "cell number N/K", token="bacterium", ha="left")
p.line(t, light, token="highlight")
p.text(13, 0.86, "luminescence", token="highlight", ha="left")
p.vline(24)
bio.label(ax, (p.X(24) + 0.15, p.Y(0.72)), "dawn:\n90 % expelled", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "B", (15.6, 8.4))
q = quant.Plot(ax, (17.4, 1.6, 6.0, 5.8), xlim=(0, 1), ylim=(0, 1.05), xlabel="autoinducer (rel.)",
               ylabel="light per cell", xticks=[0, 0.5, 1], yticks=[0, 0.5, 1])
a = np.linspace(0, 1, 200)
q.line(a, a**nh / (Kh**nh + a**nh), token="highlight")
q.vline(Kh, text="quorum threshold", size="tiny")
