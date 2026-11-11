"""Adaptation of the vestibulo-ocular reflex by a cerebellar adaptive filter with two sites of learning.

Head velocity h(t): sum of sinusoids between 0.2 and 1.6 Hz (random phases), dt = 5 ms.
Eye velocity command (eye plant neglected): e(t) = -(g_b h(t) + z(t)). Brainstem pathway with gain
g_b (vestibular nucleus); flocculus output z(t) = sum_j w_j p_j(t), where the parallel fiber signals
p_j are a bank of 8 temporal filters of head velocity (h itself and low-pass filters with time
constants 10 to 400 ms), as in the adaptive-filter model (Fujita 1982; Dean and Porrill).
Lenses of magnification G = 2 require eye velocity -G h. Retinal slip s(t) = G h(t) + e(t),
signaled by climbing fibers. Cortical learning (fast, LMS / decorrelation rule):
dw_j/dt = eta s(t) p_j(t). Brainstem learning (slow, heterosynaptic: vestibular input paired with
Purkinje signal): dg_b/dt = eta_b z(t) h(t). Updates are summed over 1 s blocks. Training for 60 min, gain measured as the regression
coefficient of -e on h. At chosen times the cerebellar output is removed (lesion test) to measure
the gain carried by the brainstem alone.
A: head velocity and eye velocity (sign inverted) at the start and the end of training.
B: VOR gain against training time: total gain, the brainstem part g_b, and the gain remaining
after a flocculus lesion; the learned gain is gradually transferred from cortex to brainstem.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt = 0.005
Tmin = 60
n = int(Tmin * 60 / dt)
t = np.arange(n) * dt
freqs = np.array([0.2, 0.35, 0.5, 0.8, 1.1, 1.6])
h = (np.sin(2 * np.pi * freqs[:, None] * t[None, :] + rng.uniform(0, 2 * np.pi, (6, 1)))).sum(0)
h *= 20 / h.std()                                          # deg/s
taus = np.array([0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.4])
Pf = np.empty((n, 1 + len(taus)))
Pf[:, 0] = h
for j, tj in enumerate(taus):
    Pf[:, j + 1] = lfilter([dt / tj], [1, dt / tj - 1], h)      # first-order low-pass
G, eta, eta_b = 2.0, 6e-8, 5e-9
w = np.zeros(Pf.shape[1])
g_b = 1.0
blk = int(1 / dt)                                          # weights updated once per second
rec_t, rec_tot, rec_b = [], [], []
snap = {}
for b0 in range(0, n, blk):
    sl = slice(b0, b0 + blk)
    hb, pb = h[sl], Pf[sl]
    z = pb @ w
    e = -(g_b * hb + z)
    s_ = G * hb + e
    if b0 == 0:
        snap["start"] = (t[:2 * blk], h[:2 * blk], g_b * h[:2 * blk] + Pf[:2 * blk] @ w)
    w += eta * pb.T @ s_
    g_b += eta_b * z @ hb
    if (b0 // blk) % 30 == 0:
        rec_t.append(t[b0] / 60)
        rec_tot.append(-(hb @ e) / (hb @ hb))
        rec_b.append(g_b)
sl = slice(n - 2 * blk, n)
snap["end"] = (t[:2 * blk], h[sl], g_b * h[sl] + Pf[sl] @ w)

fig, axs = plt.subplots(1, 2, figsize=(12, 3.8), gridspec_kw={"width_ratios": [1.3, 1]})
ax = axs[0]
for k, (lab, off) in enumerate((("start", 0), ("end", 2.3))):
    tt, hh, ee = snap[lab]
    ax.plot(tt + off, hh, color=P.muted(), lw=1.3, label="head velocity" if k == 0 else None)
    ax.plot(tt + off, ee, color=P.edge("dna"), lw=1.6,
            label="eye velocity (inverted)" if k == 0 else None)
    ax.plot(tt + off, G * hh, color=P.edge("negative"), lw=0.9, ls="--",
            label="required, $2\\times$ head" if k == 0 else None)
ax.text(1.0, ax.get_ylim()[1] * 0.98, "start of training", ha="center", va="top", fontsize=8,
        color=P.muted())
ax.text(3.3, ax.get_ylim()[1] * 0.98, f"after {Tmin} min", ha="center", va="top", fontsize=8,
        color=P.muted())
ax.set_xticks([])
ax.set_ylim(-110, 95)
ax.set_xlabel("Time (two 2 s windows)")
ax.set_ylabel("Velocity (deg/s)")
ax.set_title("A  Eye and head velocity with $2\\times$ lenses", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left", ncol=3)

ax = axs[1]
rec_t, rec_tot, rec_b = map(np.array, (rec_t, rec_tot, rec_b))
ax.plot(rec_t, rec_tot, color=P.ink(), lw=2.0, label="total VOR gain")
ax.plot(rec_t, rec_b, color=P.edge("negative"), lw=1.8, label="after flocculus lesion (brainstem $g_b$)")
ax.fill_between(rec_t, rec_b, rec_tot, color=P.fill("dna"), alpha=0.35, lw=0,
                label="cerebellar contribution")
ax.axhline(G, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(0.9, 2.15)
ax.set_xlabel("Training time (min)")
ax.set_ylabel("VOR gain")
ax.set_title("B  Two sites of learning", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
