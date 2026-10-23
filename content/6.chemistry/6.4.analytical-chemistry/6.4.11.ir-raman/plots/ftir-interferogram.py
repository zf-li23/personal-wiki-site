"""Interferograms of a Michelson interferometer (left) and the spectra recovered from them
by a fast Fourier transform (right): a single line, two lines 100 cm-1 apart, and a broad
source with two absorption bands. The interferogram is sampled at every half wavelength of
a He-Ne laser (316.4 nm of optical path difference, Nyquist limit 15 803 cm-1); the maximum
optical path difference of 0.5 cm gives a resolution of about 2 cm-1."""

import numpy as np
import matplotlib.pyplot as plt

dx = 632.8e-7 / 2  # sampling interval of the optical path difference / cm
L = 0.5  # maximum optical path difference / cm
delta = np.arange(0, L, dx)
nu = np.linspace(400, 4400, 4001)  # cm-1, grid for the source spectra
dnu = nu[1] - nu[0]


def line(center, width=1.0):
    return np.exp(-0.5 * ((nu - center) / width)**2)


def broad():
    env = np.exp(-0.5 * ((nu - 2000) / 800)**2)
    trans = 1 - 0.8 * np.exp(-0.5 * ((nu - 2900) / 25)**2) \
        - 0.95 * np.exp(-0.5 * ((nu - 1715) / 12)**2)
    return env * trans


def interferogram(B):
    # I(delta) = sum B(nu) cos(2 pi nu delta) (the modulated part only)
    out = np.zeros_like(delta)
    for b, n in zip(B, nu):
        if b > 1e-4:
            out += b * np.cos(2 * np.pi * n * delta)
    return out * dnu


def spectrum(I):
    window = 1 - delta / L  # triangular apodization
    S = np.fft.rfft(I * window).real
    f = np.fft.rfftfreq(delta.size, d=dx)
    return f, S


cases = [("single line, 2000 cm$^{-1}$", line(2000), 0.006),
         ("two lines, 2000 and 2100 cm$^{-1}$", line(2000) + line(2100), 0.04),
         ("broad source with two absorption bands", broad(), 0.006)]

fig, axes = plt.subplots(3, 2, figsize=(10, 7.2))
for i, (title, B, span) in enumerate(cases):
    I = interferogram(B)
    ax = axes[i, 0]
    m = delta <= span
    d2 = np.concatenate([-delta[m][::-1], delta[m]])
    I2 = np.concatenate([I[m][::-1], I[m]])
    ax.plot(d2 * 1e4, I2 / np.abs(I).max(), color="C0", lw=0.9)
    ax.set_ylabel("detector signal (a.u.)", fontsize=8)
    ax.set_title(title, fontsize=9)
    ax.set_yticks([])
    if i == 2:
        ax.set_xlabel(r"optical path difference $\delta$ / $\mu$m")
    f, S = spectrum(I)
    ax = axes[i, 1]
    ax.plot(f, S / S.max(), color="C3", lw=1.0)
    ax.set_xlim(4000, 500)
    ax.set_yticks([])
    ax.set_ylabel("recovered spectrum", fontsize=8)
    if i == 2:
        ax.set_xlabel(r"wavenumber $\tilde\nu$ / cm$^{-1}$")
axes[2, 0].text(0.03, 0.85, "centerburst at zero\npath difference", fontsize=8,
                transform=axes[2, 0].transAxes)
fig.tight_layout()
