"""Passive spread of voltage along a cable (electrotonic units X = x / lambda, T = t / tau_m).

A: steady-state profiles for a voltage clamped at X = 0: semi-infinite cable exp(-X), sealed end at
   L = 1 and L = 2 (cosh(L - X) / cosh L), and a killed (short-circuited) end at L = 1
   (sinh(L - X) / sinh L).
B: somatic-style EPSP at X = 0 and its attenuated, delayed and broadened copies at X = 0.5, 1, 2
   along a long cable (tau_m = 20 ms, alpha current of 1 ms injected at X = 0, solved on a grid
   with implicit Euler; every trace normalized to the peak at X = 0).
C: peak attenuation of that transient (dots, from the simulation) against the steady-state
   attenuation exp(-X) (dashed) and the sinusoidal attenuation exp(-X Re sqrt(1 + i omega tau_m))
   at 10 and 100 Hz (thin lines).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_banded

import wikibio as bio

P = bio.P
tau = 20.0  # ms

# ---- simulation on a long cable, dX = 0.05, sealed far end (L = 8 is effectively infinite)
dX, L = 0.05, 8.0
n = int(L / dX) + 1
dt = 0.05
tmax = 120.0
steps = int(tmax / dt)
# tau dV/dt = d2V/dX2 - V + inj  (V in units of the response to a unit-area input, dimensionless)
r = dt / tau / dX**2
ab = np.zeros((3, n))
ab[0, 1:] = -r
ab[1, :] = 1 + dt / tau + 2 * r
ab[1, 0] = 1 + dt / tau + r  # sealed ends (mirror)
ab[1, -1] = 1 + dt / tau + r
ab[2, :-1] = -r
tt = np.arange(steps) * dt
ts = 1.0
inj = (tt / ts) * np.exp(1 - tt / ts)
V = np.zeros(n)
rec = np.zeros((steps, n))
for k in range(steps):
    b = V.copy()
    b[0] += dt / tau * inj[k] / dX * 1.0
    V = solve_banded((1, 1), ab, b)
    rec[k] = V

idx = {x: int(round(x / dX)) for x in (0.0, 0.5, 1.0, 2.0)}
ref = rec[:, idx[0.0]].max()

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
ax = axs[0]
X = np.linspace(0, 3, 300)
ax.plot(X, np.exp(-X), color=P.edge("dna"), lw=2.2, label="semi-infinite")
X1 = np.linspace(0, 1, 100)
X2 = np.linspace(0, 2, 200)
ax.plot(X2, np.cosh(2 - X2) / np.cosh(2), color=P.edge("protein"), lw=2.0, label="sealed end, $L$ = 2")
ax.plot(X1, np.cosh(1 - X1) / np.cosh(1), color=P.edge("positive"), lw=2.0, label="sealed end, $L$ = 1")
ax.plot(X1, np.sinh(1 - X1) / np.sinh(1), color=P.edge("negative"), lw=2.0, label="killed end, $L$ = 1")
ax.set_xlabel("Distance $X = x/\\lambda$")
ax.set_ylabel("$V(X)/V(0)$")
ax.set_title("A  Steady state", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[1]
cols = [P.edge("dna"), P.edge("protein"), P.edge("positive"), P.edge("negative")]
for (x, i), c in zip(idx.items(), cols):
    ax.plot(tt, rec[:, i] / ref, color=c, lw=2.0, label=f"$X$ = {x:g}")
ax.set_xlim(0, 100)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Voltage / peak at $X$ = 0")
ax.set_title("B  Transient spread", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[2]
xs = np.arange(0, 3.01, 0.25)
pk = np.array([rec[:, int(round(x / dX))].max() / ref for x in xs])
ax.semilogy(xs, pk, "o", ms=5, color=P.edge("negative"), label="alpha input (peak)")
X = np.linspace(0, 3, 200)
ax.semilogy(X, np.exp(-X), color=P.ink(), lw=1.6, ls="--", label="steady state")
for f, c in ((10.0, P.edge("protein")), (100.0, P.edge("dna"))):
    w = 2 * np.pi * f * tau / 1000.0
    k = np.sqrt(1 + 1j * w).real
    ax.semilogy(X, np.exp(-X * k), color=c, lw=1.2, label=f"sinusoid, {f:g} Hz")
ax.set_ylim(1e-3, 1.5)
ax.set_xlabel("Distance $X = x/\\lambda$")
ax.set_ylabel("Relative amplitude")
ax.set_title("C  Fast signals attenuate more", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left")
for a in axs:
    a.grid(True, alpha=0.3, which="both" if a is axs[2] else "major")
fig.tight_layout()
