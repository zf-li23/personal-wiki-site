"""The Hassenstein-Reichardt correlation detector and its response to drifting gratings.

Two inputs sample luminance at points separated by dx. Each half-detector multiplies the low-pass
filtered (delayed) signal of one input with the undelayed signal of the other; the detector output is
the difference of the mirror-symmetric halves: R(t) = s1_d(t) s2(t) - s2_d(t) s1(t).
Low-pass filter: first order, tau = 50 ms. Grating: I(x, t) = 1 + c cos(2 pi (x/lam - f t)), c = 0.5.
For a sinusoid the mean output is R = c^2 sin(2 pi dx/lam) * omega tau / (1 + (omega tau)^2)
(up to the sign of motion), maximal at temporal frequency f = 1/(2 pi tau), independent of lam.
A: schematic. B: output time course for rightward then leftward motion (f = 2 Hz, lam = 4 dx).
C: mean output versus temporal frequency for three spatial wavelengths (simulation and formula).
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio

P = bio.P
tau, dx, c = 0.05, 1.0, 0.5
dt = 1e-3


def lowpass(x):
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = y[i - 1] + dt / tau * (x[i - 1] - y[i - 1])
    return y


def run(lam, f, T=3.0, direction=1):
    t = np.arange(0, T, dt)
    s1 = 1 + c * np.cos(2 * np.pi * (0 / lam - direction * f * t))
    s2 = 1 + c * np.cos(2 * np.pi * (dx / lam - direction * f * t))
    # remove the mean luminance (high-pass at the input, as photoreceptors adapt)
    s1, s2 = s1 - 1, s2 - 1
    return t, lowpass(s1) * s2 - lowpass(s2) * s1


fig = plt.figure(figsize=(13, 4.2))
ax = fig.add_axes([0.01, 0.08, 0.26, 0.84])
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
ink, mut = P.ink(), P.muted()
for x0, lab in ((2.5, "input 1"), (7.5, "input 2")):
    ax.add_patch(Circle((x0, 8.8), 0.55, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.2))
    ax.text(x0, 9.7, lab, ha="center", fontsize=8.5, color=ink)
for x0 in (1.4, 8.6):
    ax.add_patch(FancyBboxPatch((x0 - 0.7, 5.6), 1.4, 1.0, boxstyle="round,pad=0.05",
                                facecolor=P.fill("highlight"), edgecolor=mut, lw=1))
    ax.text(x0, 6.1, "delay", ha="center", va="center", fontsize=8, color=P.on_fill())
for x0 in (3.6, 6.4):
    ax.add_patch(Circle((x0, 3.9), 0.45, facecolor="none", edgecolor=ink, lw=1.2))
    ax.text(x0, 3.9, "x", ha="center", va="center", fontsize=10, color=ink)
ax.add_patch(Circle((5, 1.6), 0.5, facecolor="none", edgecolor=ink, lw=1.2))
ax.text(5, 1.6, "-", ha="center", va="center", fontsize=13, color=ink)
kw = dict(color=ink, lw=1.1)
ax.plot([2.5, 1.4, 1.4], [8.25, 7.8, 6.6], **kw)
ax.plot([1.4, 3.3], [5.6, 4.15], **kw)
ax.plot([7.5, 3.9], [8.25, 4.25], **kw)
ax.plot([7.5, 8.6, 8.6], [8.25, 7.8, 6.6], **kw)
ax.plot([8.6, 6.7], [5.6, 4.15], **kw)
ax.plot([2.5, 6.1], [8.25, 4.25], **kw)
ax.annotate("", xy=(4.65, 1.95), xytext=(3.6, 3.45), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.1))
ax.annotate("", xy=(5.35, 1.95), xytext=(6.4, 3.45), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.1))
ax.text(3.0, 2.4, "+", fontsize=10, color=ink)
ax.text(6.7, 2.4, "-", fontsize=11, color=ink)
ax.annotate("", xy=(5, 0.1), xytext=(5, 1.1), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.1))
ax.text(5.4, 0.35, "R", fontsize=9, color=ink)
ax.text(0.2, 0.3, "A", fontsize=11, color=ink, weight="bold")

bx = fig.add_axes([0.33, 0.14, 0.3, 0.74])
t, R1 = run(4 * dx, 2.0, direction=1)
_, R2 = run(4 * dx, 2.0, direction=-1)
tt = np.concatenate([t, t + t[-1] + dt])
RR = np.concatenate([R1, R2])
bx.plot(tt, RR, color=P.edge("dna"), lw=1.0)
bx.axhline(0, color=mut, lw=0.6)
bx.axvline(t[-1], color=mut, lw=0.8, ls="--")
bx.text(1.5, RR.max() * 1.05, "preferred direction", ha="center", fontsize=8, color=mut)
bx.text(4.5, RR.max() * 1.05, "null direction", ha="center", fontsize=8, color=mut)
bx.set_ylim(RR.min() * 1.25, RR.max() * 1.25)
bx.set_xlabel("Time / s")
bx.set_ylabel("Detector output R")
bx.set_title("B  Grating drifting at 2 Hz", loc="left", fontsize=10)

cx = fig.add_axes([0.71, 0.14, 0.28, 0.74])
fs = np.logspace(-1, 1.6, 22)
ff = np.logspace(-1, 1.6, 200)
for lam, col in ((3 * dx, P.edge("dna")), (4 * dx, P.edge("rna")), (8 * dx, P.edge("positive"))):
    sim = [run(lam, f, T=max(3.0, 6 / f))[1][1000:].mean() for f in fs]
    w = 2 * np.pi * ff
    theo = c**2 * np.sin(2 * np.pi * dx / lam) * w * tau / (1 + (w * tau) ** 2)
    cx.plot(fs, sim, "o", color=col, ms=3.5)
    cx.plot(ff, theo, color=col, lw=1.5, label=f"wavelength = {lam / dx:.0f} dx")
cx.axvline(1 / (2 * np.pi * tau), color=mut, lw=0.8, ls=":")
cx.set_xscale("log")
cx.set_xlabel("Temporal frequency / Hz")
cx.set_ylabel("Mean output")
cx.legend(frameon=False, fontsize=8)
cx.set_title("C  Tuned to temporal frequency", loc="left", fontsize=10)
