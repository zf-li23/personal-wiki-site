"""Left: the orientation factor 3 cos^2(theta) - 1 of dipolar couplings and chemical shift
anisotropy; it vanishes at the magic angle 54.74 deg. Right: simulated 13C spectra of an
axially symmetric chemical shift tensor (anisotropy 8 kHz) for a static powder and under
magic-angle spinning at 2 kHz (centerband and spinning sidebands) and 12 kHz."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axes[0]
th = np.linspace(0, 90, 361)
ax.plot(th, 3 * np.cos(np.radians(th))**2 - 1, color="k", lw=1.8)
ax.axhline(0, color="0.6", lw=0.6)
tm = np.degrees(np.arccos(1 / np.sqrt(3)))
ax.axvline(tm, color="C3", lw=1.0, ls="--")
ax.text(tm + 2, 1.3, f"magic angle\n{tm:.2f} deg", color="C3", fontsize=9)
ax.set_xlim(0, 90)
ax.set_xticks(range(0, 91, 15))
ax.set_xlabel(r"$\theta$ / deg")
ax.set_ylabel(r"$3\cos^2\theta - 1$")

# powder average over beta (angle between tensor axis and rotor axis) and gamma
delta = 2 * np.pi * 8000.0  # anisotropy / rad s-1
nb, ng = 300, 60
beta = np.arccos(np.linspace(-1, 1, nb))  # uniform in cos(beta)
gam = np.linspace(0, 2 * np.pi, ng, endpoint=False)
B, G = np.meshgrid(beta, gam, indexing="ij")
sw, n = 64000.0, 4096
t = np.arange(n) / sw
x = np.fft.fftshift(np.fft.fftfreq(n, d=1 / sw)) / 1e3  # kHz


def mas_spectrum(wr):
    a1 = (np.sqrt(2) / 2) * np.sin(2 * B)
    a2 = 0.5 * np.sin(B)**2
    fid = np.zeros(n, complex)
    for k, tk in enumerate(t):
        phase = delta * (a1 * (np.sin(wr * tk + G) - np.sin(G)) / wr
                         + a2 * (np.sin(2 * wr * tk + 2 * G) - np.sin(2 * G)) / (2 * wr))
        fid[k] = np.exp(1j * phase).mean()
    fid *= np.exp(-t / 0.004)
    s = np.fft.fftshift(np.fft.fft(fid)).real
    return s / s.max()


def static_spectrum():
    w = delta * 0.5 * (3 * np.cos(beta)**2 - 1) / (2 * np.pi * 1e3)  # kHz
    h, edges = np.histogram(w, bins=400, range=(-20, 20))
    centers = 0.5 * (edges[1:] + edges[:-1])
    k = np.exp(-0.5 * (np.linspace(-3, 3, 31) / 1.0)**2)
    h = np.convolve(h, k / k.sum(), mode="same")
    return centers, h / h.max()


ax = axes[1]
xc, hs = static_spectrum()
ax.plot(xc, hs + 2.4, color="k", lw=1.2)
ax.text(19, 2.6, "static powder", ha="right", fontsize=9)
for off, wr_hz in [(1.2, 2000.0), (0.0, 12000.0)]:
    s = mas_spectrum(2 * np.pi * wr_hz)
    ax.plot(x, s + off, color="C0" if wr_hz < 5000 else "C3", lw=1.0)
    ax.text(19, off + 0.2, f"MAS {wr_hz / 1e3:.0f} kHz", ha="right", fontsize=9)
ax.set_xlim(20, -20)
ax.set_ylim(-0.1, 3.6)
ax.set_yticks([])
ax.set_xlabel("frequency offset from the isotropic shift / kHz")
fig.tight_layout()
