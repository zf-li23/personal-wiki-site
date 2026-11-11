"""Delayed feedback control and the Smith predictor.

Plant: dx/dt = u (the command sets the velocity of the hand). Target x* = 10 cm.
Delayed feedback: u(t) = -k [x(t - T) - x*], T = 100 ms. Stable iff k T < pi/2.
Smith predictor: the controller uses the estimate x_hat(t) = x(t - T) + c * integral_{t-T}^{t} u ds,
where the integral is the forward-model prediction from the efference copy of the commands
issued during the last T (c = 1: correct model; c != 1: model gain error).
A: delayed feedback with kT = 0.5, 1.2, 1.8 (slow, ringing, unstable).
B: Smith predictor with kT = 1.8: correct model (no oscillation) and model gain errors.
C: critical gain k_c = pi / (2T) and oscillation frequency 1 / (4T) against the loop delay.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.0005
T = 0.100
xs = 10.0
tmax = 1.5
n = int(tmax / dt)
lag = int(T / dt)
t = np.arange(n) * dt


def run(k, smith=False, c=1.0):
    x = np.zeros(n)
    u = np.zeros(n)
    for i in range(n - 1):
        xd = x[i - lag] if i >= lag else 0.0
        if smith:
            inflight = u[max(i - lag, 0):i].sum() * dt
            est = xd + c * inflight
        else:
            est = xd
        u[i] = -k * (est - xs)
        x[i + 1] = x[i] + dt * u[i]
    return x


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
cols = [P.edge("dna"), P.edge("positive"), P.edge("negative")]
ax = axs[0]
for kT, col in zip((0.5, 1.2, 1.8), cols):
    ax.plot(t * 1000, run(kT / T), color=col, lw=2.0, label=f"$kT$ = {kT}")
ax.axhline(xs, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(-2, 22)
ax.set_title("A  Delayed feedback ($T$ = 100 ms)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")

ax = axs[1]
k = 1.8 / T
ax.plot(t * 1000, run(k), color=P.muted(), lw=1.2, ls="--", label="no predictor")
for c, col, lab in ((1.0, P.edge("dna"), "correct model"), (0.7, P.edge("positive"), "model gain 0.7"),
                    (1.4, P.edge("rna"), "model gain 1.4")):
    ax.plot(t * 1000, run(k, smith=True, c=c), color=col, lw=2.0, label=lab)
ax.axhline(xs, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(-2, 22)
ax.set_title("B  Smith predictor ($kT$ = 1.8)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
for a in axs[:2]:
    a.set_xlabel("Time / ms")
    a.set_ylabel("Hand position / cm")

ax = axs[2]
Ts = np.linspace(0.02, 0.25, 200)
ax.plot(Ts * 1000, np.pi / (2 * Ts), color=P.edge("dna"), lw=2.0)
ax.set_xlabel("Loop delay $T$ / ms")
ax.set_ylabel("Critical gain $k_c$ / s$^{-1}$", color=P.edge("dna"))
ax.set_yscale("log")
ax2 = ax.twinx()
ax2.plot(Ts * 1000, 1 / (4 * Ts), color=P.edge("negative"), lw=2.0, ls="--")
ax2.set_ylabel("Oscillation frequency / Hz", color=P.edge("negative"))
for Tm, lab in ((0.03, "spinal"), (0.1, "visual")):
    ax.axvline(Tm * 1000, color=P.muted(), lw=0.8, ls=":")
    ax.text(Tm * 1000 + 3, 60, lab, fontsize=8, color=P.muted())
ax.set_title("C  Stability boundary", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
