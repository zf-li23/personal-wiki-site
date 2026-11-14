"""Model: the HPA axis as a three-stage cascade with negative feedback (after the minimal model of Gupta et al.
2007, simplified; arbitrary units, time in hours). CRH (c), ACTH (a) and glucocorticoid (g):
  dc/dt = 5 (1 + S(t)) / (1 + (g/K)^2) - c / tau_c,  da/dt = c / (1 + (g/K)^2) - a / tau_a,  dg/dt = a - g / tau_g,
with tau_c = 0.2, tau_a = 0.3, tau_g = 1.0, K = 0.3. A: a 30-min acute stressor (S = 6) causes a glucocorticoid
peak about an hour later and a return to baseline within a few hours, terminated by feedback. B: the same stressor
repeated daily for 10 days, with intact feedback (blue) or with feedback weakened to K = 0.9 (glucocorticoid
receptor downregulation in chronic stress; orange): baseline and peaks stay elevated."""
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P


def run(T, stress, K=0.3):
    def f(t, y):
        c, a, g = y
        fb = 1.0 / (1.0 + (g / K) ** 2)
        return [5 * (1 + stress(t)) * fb - c / 0.2, c * fb - a / 0.3, a - g / 1.0]
    y0 = [0.1, 0.02, 0.01]
    s = solve_ivp(f, (0, T), y0, max_step=0.02, dense_output=True)
    return s


def pulse(t0, d=0.5, S=6.0):
    return lambda t: S if t0 <= t < t0 + d else 0.0


fig, ax = bio.canvas(24, 10.2)
bio.panel(ax, "A", (0.3, 9.9))
s = run(40, pulse(30))
t = np.linspace(26, 36, 800)
y = s.sol(t)
y = y / y[:, :1]   # fold change over the pre-stressor baseline
top = 1.15 * y.max()
p = quant.Plot(ax, (2.0, 1.8, 8.8, 7.2), xlim=(0, 10), ylim=(0, top), xlabel="Time / h",
               ylabel="Fold change over baseline", xticks=[0, 2, 4, 6, 8, 10], yticks=[k for k in range(1, int(top) + 1)])
p.span(4, 4.5, "negative", text="stressor", text_y=p.Y(0.96 * top))
for k, (name, tok) in enumerate([("CRH", "enzyme"), ("ACTH", "receptor"), ("glucocorticoid", "dna")]):
    p.line(t - 26, y[k], tok, lw=1.6)
p.legend([("CRH", "enzyme", "-"), ("ACTH", "receptor", "-"), ("glucocorticoid", "dna", "-")], at=p.xy(6.2, 0.9 * top))
bio.panel(ax, "B", (12.3, 9.9))
res = []
for K in (0.3, 0.9):
    sK = run(24 * 12, lambda t: 6.0 if (t > 24 and (t % 24) < 0.5 and t < 24 * 11) else 0.0, K=K)
    res.append(sK)
tt = np.linspace(0, 24 * 12, 6000)
g0 = res[0].sol(tt)[2][1000]
q = quant.Plot(ax, (14.0, 1.8, 9.4, 7.2), xlim=(0, 12), ylim=(0, 1.15 * max(r.sol(tt)[2].max() for r in res) / g0),
               xlabel="Days", ylabel="Glucocorticoid (relative to intact baseline)", xticks=[0, 2, 4, 6, 8, 10, 12],
               yticks=[1, 2, 3])
daily = lambda t: 6.0 if (t > 24 and (t % 24) < 0.5 and t < 24 * 11) else 0.0
for sK, tok in zip(res, ("dna", "rna")):
    q.line(tt / 24, sK.sol(tt)[2] / g0, tok, lw=1.0)
q.legend([("intact feedback", "dna", "-"), ("weakened feedback", "rna", "-")], at=q.xy(0.3, 1.1 * max(r.sol(tt)[2].max() for r in res) / g0))
ax.set_ylim(0.3, 10.2)
