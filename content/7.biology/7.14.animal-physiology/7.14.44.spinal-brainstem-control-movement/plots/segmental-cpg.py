"""Travelling wave from a chain of coupled segmental oscillators (lamprey-like, phase model).

N = 100 segmental oscillators, d theta_i/dt = 2 pi f + a sin(theta_{i+1} - theta_i + phi)
+ a sin(theta_{i-1} - theta_i - phi) (nearest-neighbour coupling with a phase bias phi = 2 pi / N,
a = 200 s^-1; ends have one neighbour). Intrinsic frequencies scatter by 2 % (s.d.)
around f; started near synchrony; shown after 20 s.
A: bursts (cos theta > 0.7) of every segment over 1.5 cycles at f = 2 Hz: a head-to-tail wave.
B: intersegmental phase lag (fraction of a cycle per segment) against frequency for the coupled
chain, compared with a hypothetical chain driven through a fixed 5-ms conduction delay per
segment, whose lag would grow with frequency.
C: body curvature profile along the chain at one instant: about one wavelength per body.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N, a = 100, 200.0
phi = 2 * np.pi / N
rng = np.random.default_rng(0)


def run(f, T=20.0, dt=1e-3, keep=0.0):
    th = rng.normal(0, 0.3, N)
    omega = 2 * np.pi * f * (1 + 0.02 * rng.standard_normal(N))
    out = []
    for s in range(int(T / dt)):
        d = omega.copy()
        d[:-1] += a * np.sin(th[1:] - th[:-1] + phi)
        d[1:] += a * np.sin(th[:-1] - th[1:] - phi)
        th = th + dt * d
        if s * dt >= T - keep:
            out.append(th.copy())
    return th, np.array(out)


fig = plt.figure(figsize=(12, 4.0))
ax = fig.add_subplot(1, 3, 1)
bx = fig.add_subplot(1, 3, 2)
cx = fig.add_subplot(1, 3, 3)

f = 2.0
th, hist = run(f, keep=0.75)
tt = np.arange(len(hist)) * 1e-3
burst = np.cos(hist) > 0.7
seg, ti = np.nonzero(burst.T)
ax.scatter(tt[ti] * 1e3, seg, s=0.3, color=P.edge("rna"), rasterized=True)
ax.set_xlim(0, 750)
ax.set_ylim(N, 0)
ax.set_xticks([0, 250, 500, 750])
ax.set_xticklabels(["0", "250", "500", "750"])
ax.set_xlabel("Time / ms")
ax.set_ylabel("Segment (head = 0)")
ax.set_title("A  Head-to-tail wave of bursts", loc="left", fontsize=10)

fs = np.array([1, 2, 3, 4, 6, 8])
lags = []
for fv in fs:
    th, _ = run(fv)
    dphi = np.angle(np.exp(1j * (th[:-1] - th[1:])))
    lags.append(np.median(dphi) / (2 * np.pi))
bx.plot(fs, lags, "o-", color=P.edge("rna"), lw=1.8, ms=4, label="coupled oscillators")
bx.plot(fs, fs * 0.005, "--", color=P.edge("dna"), lw=1.8, label="fixed 5-ms delay")
bx.set_xlabel("Swimming frequency / Hz")
bx.set_ylabel("Lag per segment (cycles)")
bx.set_ylim(0, 0.045)
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Lag stays ~1 % of a cycle", loc="left", fontsize=10)

th, _ = run(f)
pos = np.arange(N) / (N - 1)
cx.plot(pos, np.sin(th - th[0]), color=P.edge("enzyme"), lw=2)
cx.axhline(0, color=P.muted(), lw=0.7)
cx.set_xlabel("Position along body (head to tail)")
cx.set_ylabel("Left-right activity, sin $\\theta$")
cx.set_title("C  One wavelength per body", loc="left", fontsize=10)
for x in (ax, bx, cx):
    x.grid(True, alpha=0.3)
fig.tight_layout()
