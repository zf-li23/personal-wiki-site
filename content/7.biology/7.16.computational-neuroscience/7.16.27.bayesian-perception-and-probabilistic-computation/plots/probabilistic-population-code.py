"""A probabilistic population code: gain encodes reliability, summing responses multiplies likelihoods.

41 independent Poisson neurons, preferred values evenly spaced every 2 units from -40 to 40,
Gaussian tuning of width 8 and gain g (peak mean count g). Population a has g = 1.5, population b
g = 5; a sees stimulus -2 and b sees +2 (a cue conflict). Because the tuning curves are identical,
the summed response r_a + r_b has the likelihood L_a L_b.
A: counts of population a, b and their sum. B: likelihood functions (normalized) from a, from b and
from the summed population, and the product L_a L_b (dotted, coincides with the sum).
C: s.d. of the center-of-mass estimate over 3000 trials against the posterior s.d. predicted from
the total count, sigma_f / sqrt(sum r), for gains 0.5 to 16.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
pref = np.arange(-40, 41, 2.0)
sf = 8.0
grid = np.linspace(-15, 15, 600)


def f(s, g):
    return g * np.exp(-(np.atleast_1d(s)[..., None] - pref) ** 2 / (2 * sf ** 2))



def lik(r, g):
    ll = r @ np.log(f(grid, g)).T - f(grid, g).sum(1)
    ll -= ll.max()
    L = np.exp(ll)
    return L / np.trapezoid(L, grid)


ra = rng.poisson(f(-2.0, 1.5))[0]
rb = rng.poisson(f(2.0, 5.0))[0]
rs = ra + rb
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
ax.step(pref, ra, where="mid", color=P.edge("dna"), lw=1.6, label=f"population a ({ra.sum()} spikes)")
ax.step(pref, rb, where="mid", color=P.edge("rna"), lw=1.6, label=f"population b ({rb.sum()} spikes)")
ax.step(pref, rs, where="mid", color=P.ink(), lw=1.6, label=f"sum ({rs.sum()} spikes)")
ax.set_xlabel("Preferred stimulus")
ax.set_ylabel("Spike count")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  Population responses", loc="left", fontsize=10)

ax = axs[1]
La = lik(ra, 1.5)
Lb = lik(rb, 5.0)
Ls = lik(rs, 6.5)
prod = La * Lb
prod /= np.trapezoid(prod, grid)
ax.plot(grid, La, color=P.edge("dna"), lw=2, label="from a")
ax.plot(grid, Lb, color=P.edge("rna"), lw=2, label="from b")
ax.plot(grid, Ls, color=P.ink(), lw=2.4, label="from the summed response")
ax.plot(grid, prod, color=P.edge("positive"), lw=1.6, ls=":", label="product of a and b")
ax.set_xlabel("Stimulus s")
ax.set_ylabel("Normalized likelihood")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("B  Summing responses multiplies likelihoods", loc="left", fontsize=10)

ax = axs[2]
gains = np.array([0.5, 1, 2, 4, 8, 16])
emp, pred = [], []
for g in gains:
    r = rng.poisson(f(np.zeros(3000), g))
    ok = r.sum(1) > 0
    est = (r[ok] @ pref) / r[ok].sum(1)
    emp.append(est.std())
    pred.append(np.mean(sf / np.sqrt(r[ok].sum(1))))
ax.loglog(pred, emp, "o", color=P.edge("dna"), ms=5)
lim = [min(pred) * 0.8, max(pred) * 1.2]
ax.plot(lim, lim, color=P.muted(), lw=0.8)
ax.set_xlabel("Posterior s.d. from the total count")
ax.set_ylabel("Error s.d. of the estimate")
ax.set_title("C  Gain means reliability", loc="left", fontsize=10)
fig.tight_layout()
