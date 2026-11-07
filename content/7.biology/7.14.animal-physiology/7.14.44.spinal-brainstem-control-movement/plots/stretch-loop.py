"""Stretch reflex as a delayed negative-feedback loop: gain, delay and tremor or clonus.

Limb segment: J x'' + b x' + k x = u(t) + d(t), with natural frequency 2 Hz and damping ratio 0.4
(units scaled so that J = 1). Reflex torque u(t) = -G [x(t - T) + 0.05 s * x'(t - T)]
(length and velocity feedback of the spindle, delay T). A brief tap d at t = 0.1 s.
A: responses for T = 40 ms at gains 0.5, 0.95 and 1.1 times the critical gain.
B: critical gain (relative to the passive stiffness k) and the oscillation frequency at the
stability boundary against loop delay, found numerically from the characteristic equation
-J w^2 + i b w + k + G (1 + i w tau_v) exp(-i w T) = 0.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
w0 = 2 * np.pi * 2.0
k = w0**2
b = 2 * 0.4 * w0
tv = 0.05


def boundary(T):
    w = np.linspace(1, 200, 200000)
    plant = -w**2 + 1j * b * w + k
    fb = (1 + 1j * w * tv) * np.exp(-1j * w * T)
    G = -plant / fb
    i = np.where(np.diff(np.sign(G.imag)) != 0)[0]
    cand = [(G.real[j], w[j]) for j in i if G.real[j] > 0]
    g, ww = min(cand)
    return g, ww / (2 * np.pi)


def simulate(G, T, dur=2.5, dt=1e-4):
    n = int(dur / dt)
    lag = int(T / dt)
    x = np.zeros(n)
    v = np.zeros(n)
    for i in range(1, n):
        j = i - 1 - lag
        xd, vd = (x[j], v[j]) if j >= 0 else (0.0, 0.0)
        tt = i * dt
        d = 200.0 if 0.1 < tt < 0.12 else 0.0
        a = -b * v[i - 1] - k * x[i - 1] - G * (xd + tv * vd) + d
        v[i] = v[i - 1] + dt * a
        x[i] = x[i - 1] + dt * v[i]
    return np.arange(n) * dt, x


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0))
T = 0.04
gc, fc = boundary(T)
for f, c in ((0.5, P.edge("dna")), (0.95, P.edge("enzyme")), (1.1, P.edge("rna"))):
    t, x = simulate(f * gc, T)
    ax.plot(t, x / 0.15, color=c, lw=1.5, label=rf"$G = {f}\,G_{{\mathrm{{crit}}}}$")
ax.set_ylim(-4, 4)
ax.set_xlabel("Time / s")
ax.set_ylabel("Joint angle (a.u.)")
ax.legend(frameon=False, fontsize=8, loc="lower left", ncol=3)
ax.set_title(f"A  Delay T = 40 ms (oscillation ~{fc:.1f} Hz)", loc="left", fontsize=10)

Ts = np.linspace(0.01, 0.12, 45)
res = np.array([boundary(v) for v in Ts])
bx.plot(Ts * 1e3, res[:, 0] / k, color=P.edge("rna"), lw=2, label="critical gain / k")
bx.set_xlabel("Loop delay / ms")
bx.set_ylabel("Critical gain (relative to k)", color=P.edge("rna"))
bx.set_yscale("log")
b2 = bx.twinx()
b2.plot(Ts * 1e3, res[:, 1], color=P.edge("dna"), lw=2, ls="--")
b2.set_ylabel("Oscillation frequency / Hz", color=P.edge("dna"))
bx.set_title("B  Longer loops: lower gain, slower oscillation", loc="left", fontsize=10)
bx.grid(True, alpha=0.3)
ax.grid(True, alpha=0.3)
fig.tight_layout()
