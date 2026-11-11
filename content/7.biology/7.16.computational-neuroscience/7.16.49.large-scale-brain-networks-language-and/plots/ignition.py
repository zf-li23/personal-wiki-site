"""Global ignition: an all-or-none late response from a bistable recurrent "workspace" population.

Sensory population r1: tau1 dr1/dt = -r1 + s * stim(t) (stimulus of 40 ms), tau1 = 20 ms; linear.
Workspace population r2 with recurrent excitation and slow adaptation a:
  tau2 dr2/dt = -r2 + F(w r2 + c r1 - a - theta) + noise,  tau_a da/dt = -a + k_a r2,
F(x) = 1 / (1 + exp(-x / 0.1)), tau2 = 30 ms, w = 1.4, c = 1.5, theta = 0.85, tau_a = 400 ms, k_a = 0.6,
noise std 0.35 (Euler-Maruyama, dt = 1 ms). Strong recurrence makes r2 bistable: a stimulus that drives
it past threshold ignites self-sustained activity lasting hundreds of milliseconds.
A: single trials at three stimulus strengths. B: 300 trials per strength: the early sensory response
grows linearly while the probability of ignition (late r2 at 150-250 ms > 0.5) is a steep sigmoid.
C: late r2 at a threshold stimulus is bimodal ("seen" and "unseen" trials with the same stimulus).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)
dt, T = 1.0, 600.0
tau1, tau2, taua = 20.0, 30.0, 400.0
w, c, theta, ka, noise = 1.4, 1.5, 0.85, 0.6, 0.35


def F(x):
    return 1.0 / (1.0 + np.exp(-x / 0.1))


def sim(s, ntr):
    nt = int(T / dt)
    r1 = np.zeros(ntr)
    r2 = np.zeros(ntr)
    a = np.zeros(ntr)
    R1 = np.zeros((nt, ntr))
    R2 = np.zeros((nt, ntr))
    for k in range(nt):
        t = k * dt
        stim = s if 50 <= t < 90 else 0.0
        r1 += dt / tau1 * (-r1 + stim)
        r2 += dt / tau2 * (-r2 + F(w * r2 + c * r1 - a - theta)) + noise * np.sqrt(dt) / tau2 * rng.normal(size=ntr)
        r2 = np.clip(r2, 0, 1.2)
        a += dt / taua * (-a + ka * r2)
        R1[k] = r1
        R2[k] = r2
    return R1, R2


t = np.arange(int(T / dt)) * dt
fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9))
ax = axs[0]
for s, col in ((0.25, P.edge("dna")), (0.4, P.edge("enzyme")), (0.6, P.edge("negative"))):
    R1, R2 = sim(s, 1)
    ax.plot(t, R1[:, 0], color=col, lw=1.0, ls="--")
    ax.plot(t, R2[:, 0], color=col, lw=1.8, label=f"s = {s:g}")
ax.axvspan(50, 90, color=P.fill("highlight"), alpha=0.5, lw=0)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Activity")
ax.text(330, 0.35, "dashed: sensory $r_1$", fontsize=8, color=P.muted())
ax.legend(frameon=False, fontsize=8, title="workspace $r_2$", title_fontsize=8)
ax.set_title("A  Single trials", loc="left", fontsize=10)

ax = axs[1]
ss = np.linspace(0.1, 0.7, 13)
early, pign = [], []
late_th = None
for s in ss:
    R1, R2 = sim(s, 300)
    early.append(R1[80].mean())
    late = R2[150:250].mean(axis=0)
    pign.append((late > 0.5).mean())
ax.plot(ss, np.array(early) / max(early), "o-", color=P.edge("dna"), lw=1.6, ms=4, label="early sensory response (normalized)")
ax.plot(ss, pign, "s-", color=P.edge("negative"), lw=1.6, ms=4, label="probability of ignition")
ax.set_xlabel("Stimulus strength $s$")
ax.set_ylabel("Response / probability")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("B  Linear input, all-or-none ignition", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)
sth = ss[np.argmin(np.abs(np.array(pign) - 0.5))]

ax = axs[2]
R1, R2 = sim(sth, 600)
late = R2[150:250].mean(axis=0)
ax.hist(late, bins=30, range=(0, 1.1), color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.4)
ax.set_xlabel("Late workspace activity (150-250 ms)")
ax.set_ylabel("Trials")
ax.set_title(f"C  Bimodality at threshold (s = {sth:.2f})", loc="left", fontsize=10)
fig.tight_layout()
