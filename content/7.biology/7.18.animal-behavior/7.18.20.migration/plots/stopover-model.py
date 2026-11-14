"""Model: optimal fuel loads in time-minimizing migration (Alerstam and Lindstrom 1990), a marginal-value
problem. The distance a bird can fly increases with diminishing returns with its fuel load f (fraction of lean
mass): r(f) = R (1 - 1/sqrt(1 + f)), because extra fuel makes the bird heavier and flight more costly
(R = 10 000 km as a scale). At a stopover the bird first spends a search/settling time t0 (here 2 days) and then
deposits fuel at a constant rate k per day. The overall speed of migration r(f) / (t0 + f/k) is maximized at the
fuel load where a line from (-t0, 0) is tangent to r(f) plotted against stopover time: the higher the
deposition rate, the more fuel the bird should carry when it leaves. A: the construction for k = 0.02 and
k = 0.06 per day. B: optimal departure fuel load and the resulting migration speed against k."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
R, t0 = 10000.0, 2.0
r = lambda f: R * (1 - 1 / np.sqrt(1 + f))
fig, ax = bio.canvas(24, 10.4)
bio.panel(ax, "A", (0.3, 10.1))
p = quant.Plot(ax, (2.4, 1.8, 9.0, 7.6), xlim=(-3, 30), ylim=(0, 4500), xlabel="Time at the stopover / days",
               ylabel="Flight range gained / km", xticks=[0, 10, 20, 30], yticks=[0, 1000, 2000, 3000, 4000], ylabel_offset=1.5)
p.points([-t0], [0], "ink", r=0.1)
p.text(-t0, 250, "arrival", size="tiny")


def best(k):
    f = np.linspace(1e-4, 3, 30000)
    v = r(f) / (t0 + f / k)
    i = np.argmax(v)
    return f[i], v[i]


for k, tok in [(0.02, "rna"), (0.06, "dna")]:
    t = np.linspace(0, 30, 300)
    p.line(t, r(k * t), tok, lw=1.8, text=f"k = {k:g} per day", at=0.75, dy=0.6)
    fo, vo = best(k)
    to = fo / k
    tt = np.array([-t0, to + 6])
    p.line(tt, vo * (tt + t0), tok, lw=1.0, dashed=True)
    p.points([to], [r(fo)], tok, r=0.14)
    p.text(to + 0.6, r(fo) - 320, f"leave with f = {fo:.2f}", ha="left", color=P.edge(tok))
bio.panel(ax, "B", (13.0, 10.1))
q = quant.Plot(ax, (15.0, 1.8, 8.4, 7.6), xlim=(0, 0.12), ylim=(0, 1.2), xlabel="Fuel deposition rate k / per day",
               ylabel="Optimal departure fuel load", xticks=[0, 0.04, 0.08, 0.12], yticks=[0, 0.4, 0.8, 1.2])
ks = np.linspace(0.005, 0.12, 60)
fs = np.array([best(k)[0] for k in ks])
vs = np.array([best(k)[1] for k in ks])
q.line(ks, fs, "dna", lw=1.8, text="fuel load", at=0.85, dy=-0.4)
q.line(ks, vs / vs.max() * 1.1, "positive", lw=1.4, dashed=True, text="migration speed (relative)", at=0.5, dy=0.45)
ax.set_ylim(0.3, 10.4)
