"""A minimal closed-loop model of the arterial baroreceptor reflex.

Baroreceptor firing f(P) = 1/(1 + exp(-(P - 100)/12)) (normalised; threshold near 50-60, saturation near 170 mmHg).
Efferent sympathetic drive u relaxes to u* = 0.5 + g (0.5 - f(P)) with tau = 2 s (g = 0.5: intact reflex; g = 0:
baroreceptor denervation). Effectors, all equal to baseline at u = 0.5:
heart rate HR = 70 (1 + 1.0 (u - 0.5)) /min; resistance R = R0 (1 + 1.2 (u - 0.5)) mmHg s/mL;
stressed volume V = V0 - loss + 600 (u - 0.5) mL (venoconstriction), V0 = 1500 mL;
stroke volume SV = 86 (V/V0)(1 + 0.5 (u - 0.5)) mL. Arterial pressure: C dP/dt = HR SV/60 - P/R, C = 1.5 mL/mmHg.
B: haemorrhage of 500 mL (10 % of blood volume) between 20 and 50 s.
C: R0 fluctuates as an Ornstein-Uhlenbeck process (SD 12 %, correlation time 30 s) over 2 h: the reflex narrows
the distribution of pressure without changing its mean (like dogs after sinoaortic denervation).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
G = 0.5  # reflex gain of the intact loop


def f(p):
    return 1 / (1 + np.exp(-(p - 100) / 12))


def sim(g, T, dt=0.02, loss=None, r0=None):
    n = int(T / dt)
    p, u = 100.0, 0.5
    out = np.zeros((n, 3))
    for i in range(n):
        t = i * dt
        lv = loss(t) if loss else 0.0
        R0 = r0[i] if r0 is not None else 1.0
        us = 0.5 + g * (0.5 - f(p))
        u += dt * (us - u) / 2.0
        hr = 70 * (1 + 1.0 * (u - 0.5))
        R = R0 * (1 + 1.2 * (u - 0.5))
        V = 1500 - lv + 600 * (u - 0.5)
        sv = 86 * V / 1500 * (1 + 0.5 * (u - 0.5))
        p += dt * (hr * sv / 60 - p / R) / 1.5
        out[i] = p, hr, u
    return np.arange(n) * dt, out


fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax, bx, cx = axs
pp = np.linspace(20, 220, 300)
ax.plot(pp, f(pp), color=P.edge("dna"), lw=2, label="firing (normalised)")
ax2 = ax.twinx()
g = np.gradient(f(pp), pp)
ax2.plot(pp, g / g.max(), color=P.edge("rna"), lw=1.6, ls="--", label="gain dF/dP (relative)")
ax2.set_yticks([])
ax.axvline(100, color=P.muted(), ls=":", lw=1)
ax.text(103, 0.05, "normal\nmean", fontsize=8, color=P.muted())
ax.set_xlabel("Carotid sinus pressure / mmHg")
ax.set_ylabel("Baroreceptor firing")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="center right")
ax.set_title("A  Most sensitive near 100 mmHg", loc="left", fontsize=10)

loss = lambda t: 500 * np.clip((t - 20) / 30, 0, 1)
for gg, c, lab in ((G, P.edge("dna"), "intact reflex"), (0.0, P.edge("blood"), "denervated")):
    t, o = sim(gg, 180, loss=loss)
    bx.plot(t, o[:, 0], color=c, lw=2, label=f"MAP, {lab}")
    if gg > 0:
        bx2 = bx.twinx()
        bx2.plot(t, o[:, 1], color=c, lw=1.2, ls=":", label="heart rate, intact")
        bx2.set_ylabel("Heart rate / min$^{-1}$ (dotted)")
        bx2.set_ylim(60, 100)
bx.axvspan(20, 50, color=P.fill("neutral"), alpha=0.3, lw=0)
bx.text(35, 104, "-500 mL", ha="center", fontsize=8, color=P.muted())
bx.set_ylim(50, 110)
bx.set_xlabel("Time / s")
bx.set_ylabel("Mean arterial pressure / mmHg")
bx.legend(frameon=False, fontsize=7.5, loc="lower left")
bx.set_title("B  Haemorrhage of 10 % of blood volume", loc="left", fontsize=10)

rng = np.random.default_rng(0)
dt, T = 0.05, 7200
n = int(T / dt)
x = np.zeros(n)
for i in range(1, n):
    x[i] = x[i - 1] - dt * x[i - 1] / 30 + 0.12 * np.sqrt(2 * dt / 30) * rng.standard_normal()
r0 = 1 + x
for gg, c, lab in ((G, P.edge("dna"), "intact"), (0.0, P.edge("blood"), "denervated")):
    t, o = sim(gg, T, dt=dt, r0=r0)
    m = o[int(300 / dt):, 0]
    cx.hist(m, bins=np.arange(50, 151, 2), density=True, color=c, alpha=0.5, label=f"{lab}: SD {m.std():.0f} mmHg")
cx.set_xlabel("Mean arterial pressure / mmHg")
cx.set_ylabel("Fraction of time (density)")
cx.legend(frameon=False, fontsize=7.5)
cx.set_title("C  The reflex is a pressure buffer", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
