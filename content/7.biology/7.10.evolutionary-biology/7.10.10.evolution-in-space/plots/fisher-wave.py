"""The spread of a favourable allele (or of a species into empty habitat) through a continuous population.
A: numerical solution of the Fisher-KPP equation dp/dt = (sigma^2/2) d^2p/dx^2 + s p (1 - p) with s = 0.05
and sigma = 1 (distance in dispersal SDs, time in generations), starting from a local introduction at x = 0;
profiles every 100 generations. B: position of the front (where p = 0.5) against time for s = 0.02, 0.05 and
0.1; after a transient the front moves at the speed sqrt(2 s sigma^2) (dashed). C: spread with a fat-tailed
dispersal kernel: an integro-difference model p(t+1) = k * g(p(t)), where g is logistic growth by a factor
1.3 per generation at low density and k is the dispersal kernel: Gaussian with variance 1 (constant
speed), or a mixture of a Laplace kernel with variance 1 (weight 0.99) and rare long jumps (a Cauchy
component of scale 20, truncated at 300 units, weight 0.01). Occasional long-distance dispersal founds
satellite colonies ahead of the front, and the spread is far faster and irregular."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.9))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.15, top=0.9, wspace=0.3)


def fisher(s, T, dx=0.25, L=320.0):
    x = np.arange(-L, L + 1e-9, dx)
    D = 0.5
    dt = min(0.4 * dx * dx / D, 0.5)
    p = np.where(np.abs(x) < 2, 1.0, 0.0)
    snaps, front = [], []
    steps = int(round(1 / dt))
    for t in range(T + 1):
        if t % 100 == 0:
            snaps.append(p.copy())
        right = x[(x > 0) & (p >= 0.5)]
        front.append(right.max() if len(right) else 0.0)
        for _ in range(steps):
            lap = np.zeros_like(p)
            lap[1:-1] = (p[2:] - 2 * p[1:-1] + p[:-2]) / dx**2
            p = p + dt * (D * lap + s * p * (1 - p))
    return x, snaps, np.array(front)


a = axs[0]
x, snaps, _ = fisher(0.05, 600)
for k, sp in enumerate(snaps):
    a.plot(x, sp, color=charts.line("dna"), lw=1.4, alpha=0.35 + 0.65 * k / (len(snaps) - 1))
a.set_xlim(-140, 140)
charts.style_axes(a, "position $x/\\sigma$", "allele frequency $p$")
charts.title(a, "A  Wave of advance, $s = 0.05$")

b = axs[1]
for s, tok in ((0.02, "rna"), (0.05, "dna"), (0.1, "plant")):
    _, _, fr = fisher(s, 600)
    t = np.arange(len(fr))
    b.plot(t, fr, color=charts.line(tok), lw=2, label=f"$s = {s:g}$")
    c = np.sqrt(2 * s)
    b.plot(t, fr[-1] - c * (t[-1] - t), color=charts.line(tok), lw=1, ls="--")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "generation", "front position $x/\\sigma$")
charts.title(b, "B  Speed $\\sqrt{2s\\sigma^2}$")

c = axs[2]
dx = 0.5
x = np.arange(-4000, 4000, dx)
n = len(x)
gk = np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)
lap = np.exp(-np.sqrt(2) * np.abs(x)) / np.sqrt(2)
cau = np.where(np.abs(x) < 300, 1 / (np.pi * 20 * (1 + (x / 20) ** 2)), 0.0)
cau = cau / (cau.sum() * dx)
mix = 0.99 * lap + 0.01 * cau
for kern, lab, tok in ((gk, "Gaussian kernel", "dna"), (mix, "fat-tailed kernel", "rna")):
    K = np.fft.rfft(np.fft.ifftshift(kern * dx))
    p = np.where(np.abs(x) < 2, 1.0, 0.0)
    fr = []
    for t in range(150):
        g = 1.3 * p / (1 + 0.3 * p)
        p = np.clip(np.fft.irfft(np.fft.rfft(g) * K, n), 0, 1)
        p[p < 1e-9] = 0.0  # remove round-off noise of the FFT, which would otherwise grow
        right = x[(x > 0) & (p >= 0.5)]
        fr.append(right.max() if len(right) else 0.0)
    c.plot(np.arange(150), fr, color=charts.line(tok), lw=2, label=lab)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(c, "generation", "front position")
charts.title(c, "C  Long-distance dispersal")
