# The Hahn spin echo. The field inhomogeneity is modeled by a Gaussian distribution of offsets (s.d. 6 Hz,
# 400 isochromats for the signal, 15 drawn in the vector diagrams over +-6 Hz); the true T2 is 0.15 s.
# Top: transverse magnetization in the rotating frame at four moments: just after the 90 degree x pulse (all
# along +y), at t = tau (fanned out), just after the 180 degree x pulse (each vector reflected, y -> -y, so the
# fan is reversed: the fastest isochromat is now the furthest behind), and at t = 2 tau (refocused along -y).
# Bottom: magnitude of the net transverse magnetization for tau = 60 ms: the FID decays with T2* (here set by
# the inhomogeneity), the echo at 2 tau recovers the signal up to the factor exp(-2 tau / T2); echo maxima for
# other tau values (dots) lie on exp(-t/T2), which is how T2 is measured.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
offs = np.linspace(-6.0, 6.0, 15)                # Hz, drawn isochromats
offs_sig = np.random.default_rng(1).normal(0.0, 6.0, 400)
T2, tau = 0.15, 0.060
cols = plt.get_cmap("viridis")

fig = plt.figure(figsize=(11.0, 5.6))
moments = ((0.0, False, "t = 0⁺ (after 90°ₓ)"), (tau, False, "t = τ⁻"), (tau, True, "t = τ⁺ (after 180°ₓ)"),
           (2 * tau, True, "t = 2τ: echo"))
for k, (t, flipped, name) in enumerate(moments):
    ax = fig.add_axes([0.03 + 0.245 * k, 0.53, 0.2, 0.42])
    ax.set_aspect("equal")
    ax.axis("off")
    th = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(th), np.sin(th), color=P.muted(), lw=0.5, ls=":")
    ax.plot([-1.15, 1.15], [0, 0], color=P.muted(), lw=0.6)
    ax.plot([0, 0], [-1.15, 1.15], color=P.muted(), lw=0.6)
    ax.text(1.18, 0, "x′", fontsize=8, color=P.ink(), va="center")
    ax.text(0, 1.2, "y′", fontsize=8, color=P.ink(), ha="center")
    amp = np.exp(-t / T2)
    for j, nu in enumerate(offs):
        if not flipped:
            phi = 2 * np.pi * nu * t                 # angle from +y towards +x
            x, y = np.sin(phi), np.cos(phi)
        else:
            phi = 2 * np.pi * nu * tau
            x, y = np.sin(phi), -np.cos(phi)         # 180 degree rotation about x': (x, y) -> (x, -y)
            phi2 = 2 * np.pi * nu * (t - tau)
            c, s = np.cos(phi2), np.sin(phi2)
            # free precession in the same sense as before: rotate by phi2 (clockwise seen from +z)
            x, y = x * c + y * s, -x * s + y * c
        ax.annotate("", xy=(amp * x, amp * y), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=cols(j / (len(offs) - 1)), lw=1.0, mutation_scale=7))
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.35)
    ax.text(0, -1.45, name, fontsize=8, color=P.ink(), ha="center", va="top")
fig.text(0.03, 0.97, "A   Isochromats in the rotating frame (yellow: highest offset, purple: lowest)", fontsize=9,
         color=P.ink(), weight="bold")

ax = fig.add_axes([0.07, 0.1, 0.9, 0.3])
t = np.linspace(0, 0.3, 3000)


def signal(t, tau):
    ph = np.where(t < tau, 2 * np.pi * np.outer(offs_sig, t), 2 * np.pi * np.outer(offs_sig, 2 * tau - t))
    return np.abs(np.exp(1j * ph).mean(axis=0)) * np.exp(-t / T2)


ax.plot(t * 1e3, signal(t, tau), color=charts.line("protein"), lw=1.6, label="|M⊥|, τ = 60 ms")
ax.plot(t * 1e3, np.exp(-t / T2), color=P.muted(), lw=0.9, ls="--", label="exp(−t/T₂)")
for tt in (0.02, 0.04, 0.08, 0.1, 0.12, 0.14):
    ax.plot(2 * tt * 1e3, np.exp(-2 * tt / T2), "o", color=charts.line("rna"), ms=4)
ax.plot([], [], "o", color=charts.line("rna"), ms=4, label="echo maxima for other τ")
for x, lab in ((0, "90°ₓ"), (tau * 1e3, "180°ₓ")):
    ax.axvline(x, color=charts.line("enzyme"), lw=1.2)
    ax.text(x + 2, 1.02, lab, fontsize=8, color=P.ink())
ax.set_xlim(0, 300)
ax.set_ylim(0, 1.12)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "t / ms", "|M⊥| / M₀")
charts.title(ax, "B   FID decays with T₂*; the echo at 2τ recovers it up to exp(−2τ/T₂)")
