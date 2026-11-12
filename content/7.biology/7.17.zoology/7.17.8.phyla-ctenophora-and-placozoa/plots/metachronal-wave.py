# Phase model of metachronal waves in a ctenophore comb row: phi_k(t) = 2 pi f t - k dphi.
# The beat cycle is asymmetric: a fast effective stroke (a quarter of the cycle) and a slow recovery.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import quant

P = bio.P
f, dphi, n = 15.0, np.pi / 4, 24
EFF = 0.25  # fraction of the cycle spent in the effective stroke


def angle(phase):
    u = np.mod(phase, 2 * np.pi) / (2 * np.pi)
    eff = u < EFF
    out = np.where(eff, -60 + 120 * (u / EFF), 60 - 120 * ((u - EFF) / (1 - EFF)))
    return out, eff


fig, ax = bio.canvas(26, 9.6)
k = np.arange(n)
bio.panel(ax, "A", (0.2, 9.4))
pa = quant.Plot(ax, (2.0, 1.6, 10.4, 6.6), (-0.5, n - 0.5), (-75, 95), xlabel="Plate number (aboral to oral)",
                ylabel="Beat angle (degrees)", xticks=[0, 6, 12, 18, 23], yticks=[-60, 0, 60])
tokens = ["dna", "negative", "positive"]
for j, t in enumerate([0.0, 1 / (8 * f), 2 / (8 * f)]):
    th, eff = angle(2 * np.pi * f * t - k * dphi)
    pa.line(k, th, token=tokens[j], lw=1.4)
    for i in range(n):
        ax.plot(pa.X(k[i]), pa.Y(th[i]), "o", ms=4.2 if eff[i] else 2.6, color=quant.line_color(tokens[j]), zorder=12)
    bio.label(ax, (pa.X(n - 0.5) + 0.2, pa.Y(th[-1])), f"t = {j}/8 cycle", size="tiny", color=quant.line_color(tokens[j]), ha="left")
bio.arrow(ax, (pa.X(4), pa.Y(86)), (pa.X(10), pa.Y(86)), kind="process", color=P.muted(), lw=1.2)
bio.label(ax, (pa.X(10.4), pa.Y(86)), "wave travels toward the mouth", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "B", (14.6, 9.4))
T = 3 / f
pb = quant.Plot(ax, (16.2, 1.6, 8.6, 6.6), (-0.5, n - 0.5), (0, T * 1000), xlabel="Plate number (aboral to oral)",
                ylabel="Time (ms)", xticks=[0, 6, 12, 18, 23], yticks=[0, 50, 100, 150, 200])
ts = np.linspace(0, T, 240)
dx = pb.X(1) - pb.X(0)
dy = pb.Y(ts[1] * 1000) - pb.Y(0)
for i in range(n):
    _, eff = angle(2 * np.pi * f * ts - i * dphi)
    for t0, e in zip(ts, eff):
        if e and t0 < T - 1.5 * ts[1]:
            ax.add_patch(plt.Rectangle((pb.X(i) - dx * 0.42, pb.Y(t0 * 1000)), dx * 0.84, dy * 1.05,
                                       facecolor=P.edge("dna"), edgecolor="none", zorder=7))
lam = 2 * np.pi / dphi
bio.label(ax, (pb.X(n / 2), pb.Y(T * 1000) + 0.35), f"wavelength = {lam:.0f} plates, period = {1000 / f:.0f} ms", size="tiny",
          color=P.muted())
