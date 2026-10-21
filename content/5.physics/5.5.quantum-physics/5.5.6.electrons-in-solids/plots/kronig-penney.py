"""Kronig-Penney model with delta-function barriers: allowed bands, gaps, and the band structure E(k)."""

import numpy as np
import matplotlib.pyplot as plt

P = 3.0  # barrier strength m*alpha*a/hbar^2
qa = np.linspace(1e-6, 4 * np.pi, 6000)
rhs = np.cos(qa) + P * np.sin(qa) / qa
allowed = np.abs(rhs) <= 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

ax1.plot(qa, rhs, color="C0", lw=1.6)
ax1.fill_between(qa, -4, 4, where=allowed, color="C2", alpha=0.18, lw=0)
ax1.axhline(1, color="0.4", lw=0.8)
ax1.axhline(-1, color="0.4", lw=0.8)
ax1.set_xlim(0, 4 * np.pi)
ax1.set_ylim(-2, 4)
ax1.set_xticks(np.arange(5) * np.pi)
ax1.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
ax1.set_xlabel(r"$qa$, with $E = \hbar^2 q^2 / 2m$")
ax1.set_ylabel(r"$\cos qa + P\,\sin(qa)/qa$")
ax1.set_title("Allowed energies (shaded): right side within [-1, 1]")

# Band structure in the extended zone: k a = arccos(rhs) + n pi on the n-th band
E = qa**2  # in units of hbar^2/(2 m a^2)
ka = np.arccos(np.clip(rhs, -1, 1))
band = np.ceil(qa / np.pi) - 1
k_ext = np.where(band % 2 == 0, ka + band * np.pi, (band + 1) * np.pi - ka)
k_ext = np.where(allowed, k_ext, np.nan)
E_plot = np.where(allowed, E, np.nan)
ax2.plot(k_ext, E_plot, color="C0", lw=1.8, label="periodic potential")
ax2.plot(-k_ext, E_plot, color="C0", lw=1.8)
kk = np.linspace(-4 * np.pi, 4 * np.pi, 400)
ax2.plot(kk, kk**2, "k--", lw=1, label=r"free electron $E \propto k^2$")
# shade the gaps between consecutive allowed bands
edges = np.flatnonzero(np.diff(allowed.astype(int)))
for i0, i1 in zip(edges[1::2], edges[2::2]):
    ax2.axhspan(E[i0], E[i1], color="0.6", alpha=0.25, lw=0)
ax2.set_xlim(-4 * np.pi, 4 * np.pi)
ax2.set_ylim(0, 4 * np.pi**2 * 4.2)
ax2.set_xticks(np.arange(-4, 5, 2) * np.pi)
ax2.set_xticklabels([r"$-4\pi/a$", r"$-2\pi/a$", "0", r"$2\pi/a$", r"$4\pi/a$"])
ax2.set_xlabel("wave number k (extended zone)")
ax2.set_ylabel(r"$E\ /\ (\hbar^2/2ma^2)$")
ax2.set_title(r"Gaps open at $k = n\pi/a$")
ax2.legend(fontsize=8, loc="upper center")
fig.tight_layout()
