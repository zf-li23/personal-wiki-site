"""Simple and complex cells: a Gabor receptive field and the energy model.

Gabor receptive field (spatial part): D(x, y) = exp(-x^2/2sx^2 - y^2/2sy^2) cos(k x - phi),
sx = 0.3 deg, sy = 0.5 deg, k = 2 pi * 1.2 cycles/deg; even (phi = 0) and odd (phi = pi/2) phases.
Simple cell: r = g [L_even]_+ (half-wave rectified linear response).
Complex cell (energy model): r = g (L_even^2 + L_odd^2) for a quadrature pair.
A: the even and odd receptive fields. B: responses to a grating of the preferred orientation and
frequency drifting at 2 Hz (simple: modulated at the drift frequency; complex: nearly constant).
C: responses to a stationary grating as a function of its spatial phase.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
sx, sy, kf = 0.3, 0.5, 1.2
k = 2 * np.pi * kf
xs = np.linspace(-1.2, 1.2, 121)
X, Y = np.meshgrid(xs, xs)
env = np.exp(-X**2 / (2 * sx**2) - Y**2 / (2 * sy**2))
De, Do = env * np.cos(k * X), env * np.sin(k * X)
dA = (xs[1] - xs[0]) ** 2


def lin(D, phase):
    return (D * np.cos(k * X - phase)).sum() * dA


fig = plt.figure(figsize=(13, 4.0))
for j, (D, lab) in enumerate(((De, "even (phase 0)"), (Do, "odd (phase 90 deg)"))):
    ax = fig.add_axes([0.02 + 0.13 * j, 0.2, 0.12, 0.62])
    m = np.abs(D).max()
    ax.imshow(D, cmap="RdBu_r", vmin=-m, vmax=m, extent=[-1.2, 1.2, -1.2, 1.2])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(lab, fontsize=8.5)
fig.text(0.02, 0.9, "A  Gabor receptive fields (red ON, blue OFF)", fontsize=10)

t = np.linspace(0, 1.5, 600)
Le = np.array([lin(De, 2 * np.pi * 2 * ti) for ti in t])
Lo = np.array([lin(Do, 2 * np.pi * 2 * ti) for ti in t])
g_s = 40 / Le.max()
g_c = 40 / (Le**2 + Lo**2).max()
bx = fig.add_axes([0.34, 0.16, 0.3, 0.68])
bx.plot(t, g_s * np.maximum(Le, 0), color=P.edge("dna"), lw=1.8, label="simple cell [L$_{even}$]$_+$")
bx.plot(t, g_c * (Le**2 + Lo**2), color=P.edge("rna"), lw=1.8, label="complex cell L$_{even}^2$ + L$_{odd}^2$")
bx.set_ylim(0, 55)
bx.set_xlabel("Time / s")
bx.set_ylabel("Firing rate / Hz")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Drifting grating, 2 Hz", loc="left", fontsize=10)

cx = fig.add_axes([0.71, 0.16, 0.27, 0.68])
ph = np.linspace(0, 2 * np.pi, 100)
Le2 = np.array([lin(De, p) for p in ph])
Lo2 = np.array([lin(Do, p) for p in ph])
cx.plot(np.degrees(ph), g_s * np.maximum(Le2, 0), color=P.edge("dna"), lw=1.8, label="simple")
cx.plot(np.degrees(ph), g_c * (Le2**2 + Lo2**2), color=P.edge("rna"), lw=1.8, label="complex")
cx.set_xticks([0, 90, 180, 270, 360])
cx.set_ylim(0, 55)
cx.set_xlabel("Spatial phase of a stationary grating / deg")
cx.set_ylabel("Firing rate / Hz")
cx.legend(frameon=False, fontsize=8)
cx.set_title("C  Phase sensitivity", loc="left", fontsize=10)
