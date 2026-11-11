"""Optimal integration of two Gaussian cues (visual-haptic size estimation, after Ernst and Banks 2002).

Haptic noise s.d. 2.0 (arbitrary size units), visual noise s.d. between 0.6 and 6.
A: likelihoods of a visual cue (sd 1.0) and a haptic cue (sd 2.0) for one trial with observed
values 52 and 56, and the posterior under a flat prior (precision-weighted mean 52.8, sd 0.89).
B: weight of vision w_v = sigma_h^2 / (sigma_v^2 + sigma_h^2) against the visual noise level (line)
and the weight estimated from 4000 simulated conflict trials (points). C: threshold (s.d.) of the
vision-alone, haptic-alone and combined estimators against visual noise; the combined one is
below both (line: theory, points: simulation).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
sh = 2.0
sv = np.array([0.6, 1.0, 1.5, 2.0, 3.0, 4.5, 6.0])

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
x = np.linspace(45, 62, 500)
g = lambda m, s: np.exp(-(x - m) ** 2 / (2 * s ** 2)) / (np.sqrt(2 * np.pi) * s)
xv, xh, s1, s2 = 52.0, 56.0, 1.0, 2.0
w = (1 / s1 ** 2) / (1 / s1 ** 2 + 1 / s2 ** 2)
mu = w * xv + (1 - w) * xh
sp = np.sqrt(1 / (1 / s1 ** 2 + 1 / s2 ** 2))
ax.plot(x, g(xv, s1), color=P.edge("dna"), lw=2, label="vision")
ax.plot(x, g(xh, s2), color=P.edge("rna"), lw=2, label="touch")
ax.plot(x, g(mu, sp), color=P.ink(), lw=2.4, label="combined")
ax.set_xlabel("Size estimate")
ax.set_ylabel("Likelihood (normalized)")
ax.legend(frameon=False, fontsize=8)
ax.set_title(f"A  Weights {w:.2f} and {1 - w:.2f}", loc="left", fontsize=10)

wv = sh ** 2 / (sv ** 2 + sh ** 2)
ax = axs[1]
sim_w, sim_sd = [], []
for s in sv:
    n = 4000
    dlt = 2.0   # cue conflict: vision says +dlt/2, touch says -dlt/2
    v = rng.normal(dlt / 2, s, n)
    h = rng.normal(-dlt / 2, sh, n)
    wopt = sh ** 2 / (s ** 2 + sh ** 2)
    est = wopt * v + (1 - wopt) * h
    sim_w.append((est.mean() + dlt / 2) / dlt)   # PSE shift towards vision
    sim_sd.append(est.std())
xx = np.linspace(0.5, 6.2, 100)
ax.plot(xx, sh ** 2 / (xx ** 2 + sh ** 2), color=P.edge("dna"), lw=2, label="vision")
ax.plot(xx, 1 - sh ** 2 / (xx ** 2 + sh ** 2), color=P.edge("rna"), lw=2, label="touch")
ax.plot(sv, sim_w, "o", color=P.edge("dna"), ms=4)
ax.plot(sv, 1 - np.array(sim_w), "o", color=P.edge("rna"), ms=4)
ax.set_xlabel("Visual noise s.d. (haptic: 2.0)")
ax.set_ylabel("Weight in the combined estimate")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Weights follow reliability", loc="left", fontsize=10)

ax = axs[2]
comb = lambda s: np.sqrt(s ** 2 * sh ** 2 / (s ** 2 + sh ** 2))
ax.plot(xx, xx, color=P.edge("dna"), lw=2, label="vision alone")
ax.plot(xx, np.full_like(xx, sh), color=P.edge("rna"), lw=2, label="touch alone")
ax.plot(xx, comb(xx), color=P.ink(), lw=2.4, label="combined (theory)")
ax.plot(sv, sim_sd, "o", color=P.ink(), ms=4)
ax.set_xlabel("Visual noise s.d. (haptic: 2.0)")
ax.set_ylabel("Estimate s.d. (threshold)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("C  Combining reduces the variance", loc="left", fontsize=10)
fig.tight_layout()
