# Protein bursts from single mRNAs (the two-stage model behind the experiment of Yu, Xiao, Ren, Lao and Xie,
# 2006), simulated with the Gillespie algorithm. Time in cell cycles.
#   mRNA made at k_m = 1.2 per cell cycle (a repressed promoter that fires rarely), degraded at
#   gamma_m = 30 per cell cycle (lifetime about 2 min for a 60-min cycle); each mRNA is translated at
#   k_p = b gamma_m with b = 4, so it makes on average b = 4 proteins before it is destroyed; proteins are
#   stable and are diluted by growth at alpha = ln 2 per cell cycle (continuous approximation of division).
# A: newly made proteins counted in three cells over three cell cycles (as in the experiment, where old proteins
#    were photobleached): they appear in steps, each step the proteins of one short-lived mRNA.
# B: burst sizes from 4000 simulated bursts (bars) and the geometric distribution with mean 4 (points): an mRNA
#    is translated again with probability k_p / (k_p + gamma_m) before it is degraded.
# C: steady-state distribution of protein number per cell (bars, long simulation) and the negative binomial
#    predicted for bursty production (line): shape a = k_m / alpha (bursts per protein lifetime), mean a b;
#    its continuous counterpart is the gamma distribution with shape a and scale b (Friedman, Cai and Xie, 2006).
import math
import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import geom, nbinom

import wikibio as bio
from wikibio import charts

P = bio.P
rnd = random.Random(0)
KM, GM, B, ALPHA = 1.2, 30.0, 4.0, math.log(2)
KP = B * GM


def run(t_end, dilution=True, record=False):
    m, p, t = 0, 0, 0.0
    made = 0
    traj, hist, bursts = [], {}, []
    cur = None
    while t < t_end:
        a = [KM, GM * m, KP * m, ALPHA * p if dilution else 0.0]
        a0 = sum(a)
        dt = -math.log(1.0 - rnd.random()) / a0
        if t > 3:
            hist[p] = hist.get(p, 0.0) + min(dt, t_end - t)
        t += dt
        u = rnd.random() * a0
        if u < a[0]:
            m += 1
            if m == 1:
                cur = 0
        elif u < a[0] + a[1]:
            m -= 1
            if m == 0 and cur is not None:
                bursts.append(cur)
                cur = None
        elif u < a[0] + a[1] + a[2]:
            p += 1
            made += 1
            if cur is not None:
                cur += 1
        else:
            p -= 1
        if record:
            traj.append((t, made))
    return traj, hist, bursts


fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

ax = axs[0]
for tok in ("protein", "dna", "negative"):
    traj, _, _ = run(3.0, dilution=False, record=True)
    tt = np.array([0.0] + [q[0] for q in traj] + [3.0])
    mm = np.array([0] + [q[1] for q in traj] + [traj[-1][1] if traj else 0])
    ax.step(tt * 60, mm, where="post", color=charts.line(tok), lw=1.5)
for k in (1, 2):
    ax.axvline(60 * k, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 180)
charts.style_axes(ax, "t / min (cell cycle 60 min)", "new protein molecules")
ax.set_title("A   Proteins appear in bursts", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
_, _, bursts = run(4000 / KM, dilution=True)
bursts = np.array(bursts[:4000])
k = np.arange(0, 25)
cnt = np.bincount(bursts, minlength=25)[:25] / len(bursts)
ax.bar(k, cnt, width=0.8, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.5, label="simulation")
q = KP / (KP + GM)
ax.plot(k, (1 - q) * q ** k, "o", color=charts.line("negative"), ms=4, label="geometric, mean b = 4")
ax.text(12, 0.12, f"mean = {bursts.mean():.2f}", fontsize=7, color=P.ink())
ax.set_xlim(-0.6, 24.6)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "proteins per burst", "fraction of bursts")
ax.set_title("B   Burst size is geometric", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
_, hist, _ = run(3000.0, dilution=True)
ks = np.array(sorted(hist))
ws = np.array([hist[x] for x in ks])
ws = ws / ws.sum()
ax.bar(ks, ws, width=0.9, color=P.fill("protein"), edgecolor="none", alpha=0.85, label="simulation")
a = KM / ALPHA
x = np.arange(0, 45)
ax.plot(x, nbinom.pmf(x, a, 1 / (1 + B)), color=charts.line("negative"), lw=1.6, label=f"neg. binomial, a = {a:.2f}, b = 4")
mu = np.sum(ks * ws)
var = np.sum(ks ** 2 * ws) - mu ** 2
ax.text(22, 0.055, f"⟨n⟩ = {mu:.1f} (a b = {a * B:.1f})\nFano = {var / mu:.1f} (1 + b = 5)", fontsize=7, color=P.ink())
ax.set_xlim(-0.6, 44)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "protein molecules per cell", "probability")
ax.set_title("C   Steady-state distribution", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
