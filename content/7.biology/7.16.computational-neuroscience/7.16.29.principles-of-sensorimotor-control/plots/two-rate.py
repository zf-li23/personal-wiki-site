"""Two-state model of motor adaptation (Smith, Ghazizadeh and Shadmehr, 2006).

x_f(n+1) = A_f x_f(n) + B_f e(n),  x_s(n+1) = A_s x_s(n) + B_s e(n),  x = x_f + x_s,  e = p - x,
A_f = 0.59, B_f = 0.21 (fast: learns and forgets quickly), A_s = 0.992, B_s = 0.02 (slow);
parameters fitted by Smith et al. to force-field adaptation.
Paradigm: 300 trials with perturbation p = 1 (force field), trials with p = -1 (deadaptation) until the
net adaptation is back at zero,
then 200 error-clamp trials (e = 0: only retention acts).
A: net adaptation and the two states: spontaneous recovery during the error clamp.
B: savings: relearning after a brief washout (p = 0 for 20 trials) is faster than the first learning,
because the slow state still holds part of the memory.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
Af, Bf, As, Bs = 0.59, 0.21, 0.992, 0.02


def run(schedule, clamp=None):
    xf = xs = 0.0
    out = []
    for n, p in enumerate(schedule):
        x = xf + xs
        out.append((x, xf, xs))
        e = 0.0 if (clamp is not None and clamp[n]) else p - x
        xf = Af * xf + Bf * e
        xs = As * xs + Bs * e
    return np.array(out)


# reversal lasts until the net adaptation has returned to zero (as in Smith et al., 2006)
nrev = 1
while run(np.r_[np.ones(300), -np.ones(nrev)])[-1, 0] > 0 and nrev < 100:
    nrev += 1
nrev -= 1
sched = np.r_[np.ones(300), -np.ones(nrev), np.zeros(200)]
clamp = np.r_[np.zeros(300 + nrev, bool), np.ones(200, bool)]
o = run(sched, clamp)
fig, axs = plt.subplots(1, 2, figsize=(11, 3.9))
ax = axs[0]
n = np.arange(len(sched))
ax.fill_between(n, -1.1, 1.1, where=clamp, color=P.fill("neutral"), alpha=0.25, lw=0)
ax.plot(n, sched * (~clamp), color=P.muted(), lw=1.0, ls=":", label="perturbation")
ax.plot(n, o[:, 0], color=P.ink(), lw=2.2, label="net adaptation $x$")
ax.plot(n, o[:, 1], color=P.edge("negative"), lw=1.6, label="fast state $x_f$")
ax.plot(n, o[:, 2], color=P.edge("dna"), lw=1.6, label="slow state $x_s$")
ax.text(300 + nrev + 100, -0.9, "error clamp", ha="center", fontsize=8, color=P.muted())
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("Trial")
ax.set_ylabel("Adaptation (fraction of perturbation)")
ax.set_title("A  Spontaneous recovery", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left")

ax = axs[1]
first = run(np.ones(100))[:, 0]
re = run(np.r_[np.ones(300), np.zeros(20), np.ones(100)])[320:, 0]
ax.plot(np.arange(100), first, color=P.muted(), lw=2.0, label="first learning")
ax.plot(np.arange(100), re, color=P.edge("dna"), lw=2.0, label="relearning after washout")
ax.set_xlabel("Trial from perturbation onset")
ax.set_ylabel("Adaptation")
ax.set_ylim(0, 1)
ax.set_title("B  Savings", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
