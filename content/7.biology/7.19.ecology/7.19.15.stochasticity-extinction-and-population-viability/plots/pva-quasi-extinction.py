"""Quasi-extinction curves of a count-based population viability analysis (illustrative parameters).

Model: ln N_{t+1} = ln N_t + mu + sigma eps_t, eps_t ~ N(0, 1) independent (density-independent growth with
environmental stochasticity), starting from N0 = 20 females, quasi-extinction threshold N_q = 5, so the
distance to the threshold on the log scale is d = ln 4. Four management scenarios with different mean
log growth rates mu and standard deviations sigma (hypothetical values, chosen only to show how the
curves respond). Lines: probability of having reached the threshold by year t from the diffusion
(inverse Gaussian) approximation of Theorem 15.2.2,
G(t) = Phi((-d - mu t) / (sigma sqrt t)) + exp(-2 mu d / sigma^2) Phi((-d + mu t) / (sigma sqrt t)).
Points: fraction of 5000 simulated trajectories of the discrete model (seed 0); they lie slightly below the lines because a yearly census misses crossings of the threshold between censuses. Dotted horizontal lines:
the ultimate probability exp(-2 mu d / sigma^2) for mu > 0.
"""

import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
N0, Nq, T = 20.0, 5.0, 100
d = np.log(N0 / Nq)
scen = [("baseline", -0.02, 0.15, "negative"),
        ("reduce mortality", 0.0, 0.15, "atp"),
        ("enlarge habitat", 0.01, 0.10, "enzyme"),
        ("connect populations", 0.03, 0.15, "dna")]

fig, ax = bio.canvas(20.0, 11.0)
pa = C.axes_at(ax, (2.5, 1.6, 15.5, 8.2))
t = np.linspace(0.5, T, 300)
for name, mu, s, tok in scen:
    G = norm.cdf((-d - mu * t) / (s * np.sqrt(t))) + np.exp(-2 * mu * d / s ** 2) * norm.cdf((-d + mu * t) / (s * np.sqrt(t)))
    pa.plot(t, G, color=Q.line_color(tok), lw=1.7, label=f"{name}: mu = {mu}, sigma = {s}")
    x = np.full(5000, np.log(N0))
    hit = np.zeros(5000, bool)
    frac = []
    for k in range(1, T + 1):
        x = x + mu + s * rng.standard_normal(5000)
        hit |= x <= np.log(Nq)
        frac.append(hit.mean())
    yrs = np.arange(1, T + 1)
    pa.plot(yrs[4::10], np.array(frac)[4::10], "o", ms=3.2, color=Q.line_color(tok))
    if mu > 0:
        pa.axhline(np.exp(-2 * mu * d / s ** 2), color=Q.line_color(tok), lw=0.6, ls=(0, (1, 2)))
pa.set_xlim(0, T)
pa.set_ylim(0, 1)
C.style_axes(pa, "years", "probability of quasi-extinction (N < 5)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.label(ax, (2.5, 10.4), "Quasi-extinction curves for four scenarios", size="small", bold=True, ha="left")
