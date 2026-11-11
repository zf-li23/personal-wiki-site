"""A flip-flop model of sleep-wake switching driven by homeostatic and circadian processes.

Wake-active monoaminergic population m and sleep-active VLPO population v inhibit each other:
tau dm/dt = -m + S(I_w + A(t) - w v),   tau dv/dt = -v + S(D - w m),
S(x) = 1 / (1 + exp(-x / sigma)), tau = 0.05 h, w = 2, sigma = 0.1, I_w = 1.
The fast switch is bistable for 0 < D < w: asleep -> awake when D falls below 0, awake -> asleep when D exceeds w.
Sleep drive D = k (H - L0) - c C(t), k = w / (H0 - L0), H0 = 0.60, L0 = 0.17, c = 0.1 k,
so that the switching thresholds in terms of H are H0 + 0.1 C and L0 + 0.1 C (the two thresholds of the
two-process model). Homeostat H (process S): dH/dt = (1 - H) / 18.2 h awake, -H / 4.2 h asleep.
Circadian wake-promoting signal C(t) = cos(2 pi (t - 18 h) / 24 h).
A: steady states of the fast switch against D (sweep up and down). B: two days, then enforced wakefulness
(A = 2) from 22:00 on day 3 to 7:00 on day 5 (33 h), and recovery.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tau, w, sig, Iw = 0.05, 2.0, 0.1, 1.0
H0, L0 = 0.60, 0.17
k = w / (H0 - L0)
c = 0.1 * k


def S(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x / sig, -50, 50)))


def C(t):
    return np.cos(2 * np.pi * (t - 18.0) / 24.0)


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw=dict(width_ratios=[1, 1.9]))
Ds = np.linspace(-0.8, 2.8, 73)
branches = []
m, v = 1.0, 0.0
for sweep in (Ds, Ds[::-1]):
    ms = []
    for D in sweep:
        for _ in range(600):
            m += 0.005 / tau * (-m + S(Iw - w * v))
            v += 0.005 / tau * (-v + S(D - w * m))
        ms.append(m)
    branches.append(ms)
axs[0].plot(Ds, branches[0], color=P.edge("negative"), lw=2, label="drive increasing")
axs[0].plot(Ds[::-1], branches[1], color=P.edge("dna"), lw=2, ls="--", label="drive decreasing")
for x in (0.0, w):
    axs[0].axvline(x, color=P.muted(), lw=0.8, ls=":")
axs[0].text(1.0, 0.5, "bistable", ha="center", fontsize=8.5, color=P.muted())
axs[0].set_xlabel("Sleep drive $D$")
axs[0].set_ylabel("Wake-active activity $m$")
axs[0].set_title("A  Hysteresis of the flip-flop", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.3))

dt = 0.005
t = np.arange(0, 120, dt)
m, v, H = 1.0, 0.0, 0.5
out = np.zeros((len(t), 2))
dep = (70.0, 103.0)
for i, ti in enumerate(t):
    A = 2.0 if dep[0] <= ti < dep[1] else 0.0
    m += dt / tau * (-m + S(Iw + A - w * v))
    v += dt / tau * (-v + S(k * (H - L0) - c * C(ti) - w * m))
    H += dt * ((1.0 - H) / 18.2 if m > 0.5 else -H / 4.2)
    out[i] = m, H
ax = axs[1]
ax.axvspan(*dep, color=P.light("highlight"), zorder=0)
ax.plot(t, out[:, 1], color=P.edge("negative"), lw=2, label="homeostatic drive $H$")
ax.plot(t, H0 + 0.1 * C(t), color=P.muted(), lw=1.1, ls="--", label="sleep-onset threshold")
ax.plot(t, L0 + 0.1 * C(t), color=P.muted(), lw=1.1, ls=":", label="waking threshold")
ax.fill_between(t, 0, 0.04, where=out[:, 0] < 0.5, color=P.fill("dna"), step="mid", label="asleep")
ax.text(87, 1.02, "enforced wakefulness", ha="center", va="top", fontsize=8.5, color=P.muted())
ax.set_xticks(np.arange(0, 121, 12))
ax.set_xlabel("Time / h (0 = midnight of day 1)")
ax.set_ylabel("Drive $H$")
ax.set_ylim(0, 1.05)
ax.set_xlim(0, 120)
ax.set_title("B  Sleep-wake cycle and one night of sleep deprivation", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7.5, loc="upper left", ncol=2)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
