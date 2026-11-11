"""Distortion products of an active oscillator near a Hopf bifurcation.

dz/dt = (mu + i w0) z - |z|^2 z + F (exp(i w1 t) + exp(i w2 t)), w0 = 1, w1 = 0.95, w2 = 1.05
(dimensionless units). The linear part is integrated exactly and the cubic term and forcing by Euler
steps (dt = 0.02). Amplitudes at a frequency w are the magnitudes of the projection of z(t) on
exp(i w t) over the last 3000 time units, weighted by a Hann window.
A: amplitude spectrum for mu = -0.01 (just below the bifurcation) and F = 1e-3: besides the two primaries, the cubic
term produces distortion products at 2 w1 - w2 = 0.85 and 2 w2 - w1 = 1.15.
B: amplitude at w1 (primary) and at 2 w1 - w2 (distortion product) against F for the near-critical
oscillator (mu = -0.01) and a damped one (mu = -0.5): the near-critical oscillator responds
compressively and its distortion product, which grows as F^3 for weak stimuli, is about a hundred times
larger than that of the damped oscillator.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
w0, w1, w2 = 1.0, 0.95, 1.05
dt = 0.02
T_on, T_rec = 1500.0, 3000.0
Fs = np.logspace(-4.3, -0.5, 12)
mus = np.array([-0.01, -0.5])
F = np.concatenate([Fs, Fs])
mu = np.repeat(mus, len(Fs))
F = np.concatenate([F, [1e-3]])
mu = np.concatenate([mu, [-0.01]])

n_on, n_rec = int(T_on / dt), int(T_rec / dt)
z = np.zeros(len(F), complex)
lin = np.exp((mu + 1j * w0) * dt)
wgrid = np.linspace(0.7, 1.3, 241)
targets = np.array([w1, 2 * w1 - w2])
acc_t = np.zeros((len(F), 2), complex)
acc_s = np.zeros(len(wgrid), complex)
for k in range(n_on + n_rec):
    t = k * dt
    drive = F * (np.exp(1j * w1 * t) + np.exp(1j * w2 * t))
    z = z * lin + dt * (-np.abs(z) ** 2 * z + drive)
    if k >= n_on and k % 5 == 0:
        win = 1 - np.cos(2 * np.pi * (k - n_on) / n_rec)  # Hann window (mean 1)
        acc_t += win * z[:, None] * np.exp(-1j * targets * t)[None, :]
        acc_s += win * z[-1] * np.exp(-1j * wgrid * t)
nrec = n_rec // 5
amp_t = np.abs(acc_t) / nrec
amp_s = np.abs(acc_s) / nrec

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1))
ax = axs[0]
ax.semilogy(wgrid, amp_s, color=P.edge("dna"), lw=1.4)
for w, lab in ((w1, "f1"), (w2, "f2"), (2 * w1 - w2, "2f1 - f2"), (2 * w2 - w1, "2f2 - f1")):
    ax.axvline(w, color=P.muted(), lw=0.6, ls=":")
    ax.text(w, amp_s.max() * 2.2, lab, fontsize=8, color=P.muted(), ha="center")
ax.set_ylim(amp_s.max() * 1e-4, amp_s.max() * 6)
ax.set_xlabel("Frequency / characteristic frequency")
ax.set_ylabel("Response amplitude")
ax.set_title("A  Spectrum of the response (near-critical)", loc="left", fontsize=10)

ax = axs[1]
n = len(Fs)
for j, (m, c) in enumerate(zip(mus, (P.edge("rna"), P.edge("dna")))):
    lab = "near-critical" if m > -0.1 else "damped"
    ax.loglog(Fs, amp_t[j * n:(j + 1) * n, 0], "-", color=c, lw=1.8, label=f"primary f1, {lab}")
    ax.loglog(Fs, amp_t[j * n:(j + 1) * n, 1], "--", color=c, lw=1.8, label=f"2f1 - f2, {lab}")
ax.set_xlabel("Stimulus force F")
ax.set_ylabel("Amplitude")
ax.set_ylim(1e-9, 2)
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.set_title("B  Compression and distortion", loc="left", fontsize=10)
fig.tight_layout()
