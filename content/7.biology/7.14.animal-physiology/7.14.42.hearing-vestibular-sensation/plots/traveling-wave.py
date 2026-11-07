"""Travelling waves on a passive one-dimensional (long-wave) cochlea and the Greenwood map.

Model: two fluid scalae of height H = 1 mm (density 1000 kg m^-3) separated by a basilar membrane
of length L = 35 mm, with local specific impedance Z(x) = r(x) + i w m + s(x)/(i w).
The pressure difference p obeys d2p/dx2 = (2 rho i w / H) p / Z(x), with dp/dx fixed at the
stapes (x = 0) and p = 0 at the helicotrema (x = L); membrane velocity v = p / Z.
Mass m = 0.5 kg m^-2 (effective, including the organ of Corti); stiffness s(x) = m (2 pi f_G(x))^2 so that the local resonance follows the
Greenwood function f_G = 165.4 (10^(2.1 y) - 0.88) Hz, y = 1 - x/L (fraction of length from the apex);
damping r = m 2 pi f_G / Q with Q = 6.
A: envelope |v| (each normalised to its peak) and an instantaneous snapshot at 1 kHz.
B: Greenwood map and the model's peak positions.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_banded

import wikibio as bio

P = bio.P
L, H, rho, m, Q = 0.035, 1e-3, 1000.0, 0.5, 6.0
N = 3000
x = np.linspace(0, L, N)
h = x[1] - x[0]


def greenwood(y):
    return 165.4 * (10 ** (2.1 * y) - 0.88)


fG = greenwood(1 - x / L)
s = m * (2 * np.pi * fG) ** 2
r = m * 2 * np.pi * fG / Q


def solve(f):
    w = 2 * np.pi * f
    Z = r + 1j * w * m + s / (1j * w)
    k2 = 2 * rho * 1j * w / (H * Z)
    ab = np.zeros((3, N), dtype=complex)
    rhs = np.zeros(N, dtype=complex)
    ab[1, :] = -2 / h**2 - k2
    ab[0, 1:] = 1 / h**2
    ab[2, :-1] = 1 / h**2
    # x = 0: (p1 - p0)/h = -1 (prescribed stapes drive); x = L: p = 0
    ab[1, 0], ab[0, 1] = -1 / h, 1 / h
    rhs[0] = -1.0
    ab[1, -1], ab[2, -2] = 1.0, 0.0
    p = solve_banded((1, 1), ab, rhs)
    return p / Z


freqs = [500, 1000, 2000, 4000, 8000]
cols = [P.edge("rna"), P.edge("enzyme"), P.edge("dna"), P.edge("protein"), P.edge("highlight")]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12, 4.4), gridspec_kw={"width_ratios": [1.5, 1]})
peaks = []
for f, c in zip(freqs, cols):
    v = solve(f)
    env = np.abs(v) / np.abs(v).max()
    ax.plot(x * 1e3, env, color=c, lw=1.8, label=f"{f / 1000:g} kHz")
    peaks.append(x[np.argmax(env)])
    if f == 1000:
        for ph in (0.0, np.pi / 2):
            ax.plot(x * 1e3, np.real(v * np.exp(1j * ph)) / np.abs(v).max(), color=c, lw=0.8,
                    alpha=0.7)
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xlim(0, 35)
ax.set_ylim(-1.05, 1.1)
ax.set_xlabel("Distance from the stapes / mm  (base to apex)")
ax.set_ylabel("Basilar-membrane velocity (normalised)")
ax.legend(frameon=False, fontsize=8, loc="lower left", ncol=5)
ax.text(23, -0.45, "thin lines: 1 kHz wave\nat two instants", fontsize=8, color=P.muted())
ax.set_title("A  Travelling-wave envelopes peak at frequency-specific places", loc="left",
             fontsize=10)

bx.plot(x * 1e3, fG / 1000, color=P.ink(), lw=2, label="Greenwood function")
bx.plot(np.array(peaks) * 1e3, np.array(freqs) / 1000, "o", color=P.edge("rna"), ms=6,
        label="model envelope peaks")
bx.set_yscale("log")
bx.set_xlim(0, 35)
bx.set_xlabel("Distance from the stapes / mm")
bx.set_ylabel("Characteristic frequency / kHz")
bx.legend(frameon=False, fontsize=8)
bx.grid(True, which="both", alpha=0.25)
bx.set_title("B  Place-frequency map", loc="left", fontsize=10)
fig.tight_layout()
