# The detailed fluctuation theorem for the total entropy production in a nonequilibrium steady state
# (Theorem 38.3.1). Gillespie simulation of the driven three-state cycle of Figure 38.1 (forward rates
# 3, 1, 2; cycle affinity 2 kBT), 40,000 trajectories of duration t started from the stationary
# distribution. The total entropy production of a trajectory is the sum over jumps of
# ln(w_forward / w_backward) plus the change of the system entropy, ln(p_start / p_end).
# A: its distribution for t = 0.5 and t = 3: negative values ("second-law violations") are common for
# short trajectories and become exponentially rare for long ones. B: ln[P(S)/P(-S)] against S lies
# on the line of slope 1, for both durations.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kf = np.array([3.0, 1.0, 2.0])
kb = np.array([1.0, 2.0, 3.0])
kb[2] = kf.prod() / (kb[0] * kb[1])
kb = kb * np.exp(-2.0 / 3)  # cycle affinity 2 kBT

W = np.zeros((3, 3))
for i in range(3):
    W[(i + 1) % 3, i] = kf[i]
    W[i, (i + 1) % 3] = kb[i]
L = W - np.diag(W.sum(0))
p = np.linalg.lstsq(np.vstack([L, np.ones(3)]), np.r_[0, 0, 0, 1.0], rcond=None)[0]
out = W.sum(0)


def simulate(t_end, n):
    x = rng.choice(3, size=n, p=p)
    x0 = x.copy()
    t = np.zeros(n)
    S = np.zeros(n)
    alive = np.ones(n, bool)
    while alive.any():
        idx = np.where(alive)[0]
        xi = x[idx]
        t[idx] += rng.exponential(1 / out[xi])
        done = t[idx] > t_end
        alive[idx[done]] = False
        go = idx[~done]
        xg = x[go]
        fwd = rng.random(go.size) < kf[xg] / out[xg]
        new = np.where(fwd, (xg + 1) % 3, (xg - 1) % 3)
        w_f = W[new, xg]
        w_b = W[xg, new]
        S[go] += np.log(w_f / w_b)
        x[go] = new
    return S + np.log(p[x0] / p[x])


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
bins = np.arange(-6.25, 12.5, 0.5)
for t_end, tok in ((0.5, "dna"), (3.0, "negative")):
    S = simulate(t_end, 40000)
    h, e = np.histogram(S, bins=bins, density=True)
    c = 0.5 * (e[1:] + e[:-1])
    axs[0].step(c, h, where="mid", color=charts.line(tok), lw=1.6,
                label=f"$t$ = {t_end}: mean {S.mean():.2f}, P(S<0) = {np.mean(S < 0):.2f}")
    hs = dict(zip(np.round(c, 2), h))
    xs, ys = [], []
    for ci in c:
        cnt = lambda v: hs.get(round(v, 2), 0) * S.size * 0.5
        if ci > 0 and cnt(-ci) >= 25 and cnt(ci) >= 25:
            xs.append(ci)
            ys.append(np.log(hs[round(ci, 2)] / hs[round(-ci, 2)]))
    axs[1].plot(xs, ys, "o", ms=4.5, color=charts.line(tok), label=f"$t$ = {t_end}")
axs[0].axvline(0, color=P.muted(), lw=0.7)
axs[0].legend(fontsize=7.5, frameon=False)
charts.style_axes(axs[0], "total entropy production $S/k_{\\mathrm{B}}$", "probability density")
charts.title(axs[0], "A   Entropy production fluctuates")
s = np.linspace(0, 5, 10)
axs[1].plot(s, s, color=P.muted(), lw=1.0, ls="--", label="slope 1")
axs[1].legend(fontsize=7.5, frameon=False)
charts.style_axes(axs[1], "$S/k_{\\mathrm{B}}$", "$\\ln[P(S)/P(-S)]$")
charts.title(axs[1], "B   Detailed fluctuation theorem")
fig.tight_layout()
