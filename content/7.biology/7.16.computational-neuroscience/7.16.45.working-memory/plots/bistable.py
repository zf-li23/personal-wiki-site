"""Persistent activity in a bistable recurrent population (firing-rate model).

tau dr/dt = -r + f(w r + I(t)), f(x) = r_max / (1 + exp(-(x - theta) / sigma)),
tau = 20 ms (A, B) and tau = 100 ms (C; slow NMDA-like recurrent synapses),
r_max = 100 Hz, w = 1.2 (per Hz), theta = 60, sigma = 8. Additive white noise of
standard deviation 30 Hz per sqrt(tau) is added to r in C (Euler-Maruyama).
A: graphical fixed points: f(w r) against r (curve) and the identity line: two stable states
   (low and high activity, filled) separated by an unstable one (open circle).
B: a brief excitatory pulse (I = +40 for 50 ms at t = 0.5 s) switches the population to the high
   state, which persists after the pulse; an inhibitory pulse (I = -60 at t = 2 s) switches it off.
C: with noise, the high state eventually decays spontaneously; the mean persistence time over
   40 trials is longer for slow (tau = 100 ms) than for fast (tau = 20 ms) recurrent synapses.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
rmax, w, th, sg = 100.0, 1.2, 60.0, 8.0
f = lambda x: rmax / (1 + np.exp(-(x - th) / sg))

fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
r = np.linspace(0, 100, 400)
ax = axs[0]
ax.plot(r, f(w * r), color=P.edge("dna"), lw=2, label="$f(wr)$")
ax.plot(r, r, color=P.muted(), lw=1, ls="--", label="$r$")
g = f(w * r) - r
roots = r[:-1][np.sign(g[:-1]) != np.sign(g[1:])]
for k, rr in enumerate(roots):
    stable = k != 1
    ax.plot(rr, rr, "o", ms=8, mfc=P.edge("negative") if stable else "none", mec=P.edge("negative"), mew=1.8)
ax.set_xlabel("Rate r / Hz")
ax.set_ylabel("Input-output / Hz")
ax.set_title("A  Two stable states", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")


def run(tau, T, pulses, noise=0.0, r0=0.0):
    dt = 0.001
    n = int(T / dt)
    rr = np.empty(n)
    x = r0
    for s in range(n):
        t = s * dt
        I = sum(a for (t0, d, a) in pulses if t0 <= t < t0 + d)
        x += dt / tau * (-x + f(w * x + I)) + noise * np.sqrt(dt / tau) * rng.standard_normal()
        rr[s] = x
    return np.arange(n) * dt, rr


t, rr = run(0.02, 3.0, [(0.5, 0.05, 40.0), (2.0, 0.05, -60.0)])
ax = axs[1]
ax.plot(t, rr, color=P.edge("dna"), lw=2)
for t0, c in ((0.5, P.edge("positive")), (2.0, P.edge("negative"))):
    ax.axvspan(t0, t0 + 0.05, color=c, alpha=0.3)
ax.text(0.55, 50, "excitatory\ncue", fontsize=8)
ax.text(2.05, 50, "inhibitory\npulse", fontsize=8)
ax.set_xlabel("Time / s")
ax.set_ylabel("Rate / Hz")
ax.set_title("B  Persistent activity", loc="left", fontsize=10)

ax = axs[2]
high = roots[-1]
for tau, c, lab in ((0.02, P.edge("negative"), "$\\tau$ = 20 ms"), (0.1, P.edge("dna"), "$\\tau$ = 100 ms")):
    life = []
    for trial in range(40):
        t, rr = run(tau, 10.0, [], noise=30.0, r0=high)
        drop = np.flatnonzero(rr < roots[1])
        life.append(t[drop[0]] if drop.size else 10.0)
    life = np.sort(life)
    ax.step(life, 1 - np.arange(1, 41) / 40, where="post", color=c, lw=2, label=f"{lab}, mean {np.mean(life):.1f} s")
ax.set_xlabel("Time / s")
ax.set_ylabel("Fraction still in high state")
ax.set_title("C  Noise limits persistence", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
