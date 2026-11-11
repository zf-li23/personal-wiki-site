"""Anticipative tracking by a CANN with adaptation.

Same A-CANN as adaptive-cann.py but N = 128 neurons (a = 0.3, k = 1, tau = 1, tau_v = 50),
strong input alpha = 0.5 moving at constant speed v_ext. After a transient (t > 400 tau),
the steady displacement s = z_bump - z of the bump center from the stimulus is measured.
A: displacement against the adaptation strength m for v_ext = 0.002, 0.004 and 0.006 rad/tau:
   without adaptation the bump lags behind the stimulus (s < 0); above a critical m it leads.
B: the same data as anticipation time s / v_ext (positive: the bump is ahead by this time).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N, tau, tauv, a, k, dt, alpha = 128, 1.0, 50.0, 0.3, 1.0, 0.2, 0.5
x = -np.pi + 2 * np.pi * np.arange(N) / N
D = np.angle(np.exp(1j * (x[:, None] - x[None, :])))
J = np.exp(-(D**2) / (2 * a**2)) / (np.sqrt(2 * np.pi) * a) * (2 * np.pi / N) / (2 * np.pi / 256)


def displacement(m, vext, T=600.0):
    u = np.zeros(N)
    v = np.zeros(N)
    out = []
    for s in range(int(T / dt)):
        t = s * dt
        z = vext * t
        I = alpha * np.exp(-np.angle(np.exp(1j * (x - z))) ** 2 / (4 * a**2))
        u2 = np.maximum(u, 0) ** 2
        r = u2 / (1 + k * u2.sum() * 256 / N)
        u = u + dt * (-u + J @ r - v + I) / tau
        v = v + dt * (-v + m * u) / tauv
        if t > 400:
            out.append(np.angle(np.exp(1j * (np.angle(np.sum(r * np.exp(1j * x))) - z))))
    return np.mean(out)


fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
ms = np.array([0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06])
for vext, c in zip((0.002, 0.004, 0.006), (P.edge("dna"), P.edge("positive"), P.edge("negative"))):
    d = np.array([displacement(m, vext) for m in ms])
    axs[0].plot(ms, d, "o-", ms=4, lw=1.8, color=c, label=f"$v_{{ext}}$ = {vext}")
    axs[1].plot(ms, d / vext, "o-", ms=4, lw=1.8, color=c, label=f"$v_{{ext}}$ = {vext}")
axs[0].axhline(0, color=P.muted(), lw=0.8)
axs[0].set_xlabel("Adaptation strength m")
axs[0].set_ylabel("Displacement $z_{\\mathrm{bump}} - z$ / rad")
axs[0].set_title("A  From lag to lead", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8)
axs[1].axhline(0, color=P.muted(), lw=0.8)
axs[1].set_xlabel("Adaptation strength m")
axs[1].set_ylabel("Anticipation time $s/v_{ext}$ / $\\tau$")
axs[1].set_title("B  Anticipation time", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
