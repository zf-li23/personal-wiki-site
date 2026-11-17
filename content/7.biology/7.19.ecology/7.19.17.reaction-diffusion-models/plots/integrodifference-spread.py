"""Spread with long-distance dispersal: an integrodifference model.

N_{t+1}(x) = integral of k(x - y) f(N_t(y)) dy, with Beverton-Holt growth f(N) = R0 N / (1 + (R0 - 1) N),
R0 = 2, and three dispersal kernels of unit variance: Gaussian, Laplace (exponential) and a fat-tailed
power-law kernel k(x) proportional to (1 + |x|/a)^(-4), with a chosen numerically for unit variance. Convolution by FFT on a grid of step 0.25 over |x| < 6000.
A: the kernels on a log scale. B: front position (farthest point with N >= 0.05) over 40 generations, on a log scale;
dashed lines have the slopes predicted by c* = min over s of ln(R0 M(s)) / s, with M the moment
generating function of the kernel: 1.18 (Gaussian) and 1.35 (Laplace). The fat-tailed kernel has no
moment generating function and the front accelerates. C: density profiles at generation 30.
"""

import numpy as np
from scipy.optimize import minimize_scalar

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

dx, L = 0.25, 6000.0
x = np.arange(-L, L, dx)
n = x.size
R0 = 2.0


def normalize(k):
    k = k / (k.sum() * dx)
    var = (k * x**2).sum() * dx
    return k, var


gauss = np.exp(-x**2 / 2)
gauss, _ = normalize(gauss)
b = 1 / np.sqrt(2)
lap = np.exp(-np.abs(x) / b)
lap, _ = normalize(lap)
fat = (1 + np.abs(x)) ** -4.0
fat, v = normalize(fat)
s = np.sqrt(v)
fat = np.interp(x * s, x, fat) * s
fat, _ = normalize(fat)

kernels = [("Gaussian", gauss, "dna"), ("Laplace", lap, "enzyme"), ("fat-tailed", fat, "negative")]
pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
sel = (x >= 0) & (x <= 30)
for name, k, tok in kernels:
    pa.semilogy(x[sel], k[sel], color=Q.line_color(tok), lw=1.6, label=name)
pa.set_xlim(0, 30)
pa.set_ylim(1e-12, 1)
C.style_axes(pa, "displacement x", "kernel density k(x)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink())
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Kernels with variance 1", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
gens = 40
for name, k, tok in kernels:
    K = np.fft.rfft(np.fft.ifftshift(k)) * dx
    N = np.where(np.abs(x) < 1, 1.0, 0.0)
    front = []
    for t in range(gens + 1):
        far = x[(x > 0) & (N >= 0.05)]
        front.append(far.max() if far.size else 0.0)
        if t == 30:
            pc.plot(x, N, color=Q.line_color(tok), lw=1.4, label=name)
        g = R0 * N / (1 + (R0 - 1) * N)
        N = np.clip(np.fft.irfft(np.fft.rfft(g) * K, n), 0, None)
    pb.plot(range(gens + 1), front, "o", ms=3, color=Q.line_color(tok), label=name)
    if name != "fat-tailed":
        if name == "Gaussian":
            M = lambda q: np.exp(q * q / 2)
            qmax = 20
        else:
            M = lambda q: 1 / (1 - b * b * q * q)
            qmax = 1 / b - 1e-6
        res = minimize_scalar(lambda q: np.log(R0 * M(q)) / q, bounds=(1e-3, qmax), method="bounded")
        c = res.fun
        tt = np.arange(gens + 1)
        pb.plot(tt, front[-1] + c * (tt - gens), color=Q.line_color(tok), lw=1.0, ls=(0, (4, 2)))
        pb.text(gens + 0.5, front[-1], f"c* = {c:.2f}", fontsize=FS["tiny"], color=Q.line_color(tok), ha="left",
                va="bottom" if name == "Laplace" else "top")
pb.set_xlim(0, gens)
pb.set_yscale("log")
pb.set_ylim(1, 5000)
C.style_axes(pb, "generation t", "front position")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Constant versus accelerating spread", size="small", bold=True, ha="left")
pc.set_xlim(0, 150)
pc.set_ylim(0, 1.05)
C.style_axes(pc, "distance x", "density N (generation 30)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Fronts at generation 30", size="small", bold=True, ha="left")
