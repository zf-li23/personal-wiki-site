# Thon rings: the power spectrum of an image of an amorphous specimen shows the square of the CTF.
# Simulation: a 512 x 512 image (pixel 1 A) of a random weak phase object (white projected potential,
# like amorphous carbon or ice) imaged at 300 kV, Cs = 2.7 mm, A = 0.07, mean defocus 1.5 um with
# 0.1 um of astigmatism (axis at 30 degrees), envelope exp(-B k^2 / 4) with B = 80 A^2, plus white
# detector noise. A: the power spectrum |F[I]|^2 (log scale, averaged over 4 independent images); the
# rings are slightly elliptical because of the astigmatism. B: rotational average of the spectrum of an
# image without astigmatism (background subtracted, normalized) and the model CTF^2 x envelope^2; the
# zeros of the CTF fall where the measured oscillation has its minima, which is how defocus is estimated.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
lam, Cs, A, B = 0.019687, 2.7e7, 0.07, 80.0
n, px = 512, 1.0
f = np.fft.fftfreq(n, d=px)
KX, KY = np.meshgrid(f, f, indexing="xy")
K = np.hypot(KX, KY)
TH = np.arctan2(KY, KX)


def ctf2d(df_mean, df_ast, ang):
    df = df_mean + 0.5 * df_ast * np.cos(2 * (TH - ang))
    c = np.pi * lam * df * K**2 - 0.5 * np.pi * Cs * lam**3 * K**4
    return -(np.sqrt(1 - A**2) * np.sin(c) + A * np.cos(c)) * np.exp(-B * K**2 / 4)


def spectrum(h, nimg=4):
    ps = np.zeros((n, n))
    for _ in range(nimg):
        phi = rng.standard_normal((n, n))
        img = 2 * 0.05 * np.real(np.fft.ifft2(np.fft.fft2(phi) * h)) + 0.08 * rng.standard_normal((n, n))
        ps += np.abs(np.fft.fft2(img)) ** 2
    return ps / nimg


fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.6), gridspec_kw={"width_ratios": [1.0, 1.5]})
ax = axs[0]
ps = spectrum(ctf2d(1.5e4, 0.1e4, np.deg2rad(30)))
show = np.fft.fftshift(np.log(ps))
m = n // 4                                    # show |k| <= 0.25 A^-1
c = n // 2
ax.imshow(show[c - m:c + m, c - m:c + m], cmap="gray", extent=(-0.25, 0.25, -0.25, 0.25), origin="lower",
          vmin=np.percentile(show, 2), vmax=np.percentile(show, 99.7))
ax.set_xticks([-0.2, 0, 0.2])
ax.set_yticks([-0.2, 0, 0.2])
charts.style_axes(ax, "kx / Å⁻¹", "ky / Å⁻¹", box=True)
charts.title(ax, "A   Power spectrum (Δf = 1.5 µm, astigmatic)")

ax = axs[1]
h = ctf2d(1.5e4, 0.0, 0.0)
ps = spectrum(h, nimg=8)
bins = np.linspace(0, 0.45, 300)
idx = np.digitize(K.ravel(), bins)
prof = np.array([ps.ravel()[idx == i].mean() for i in range(1, len(bins))])
kc = 0.5 * (bins[1:] + bins[:-1])
noise_bg = (0.08**2) * n * n
sig = (prof - noise_bg) / (2 * 0.05) ** 2 / (n * n)
model = np.array([np.mean((h.ravel()[idx == i]) ** 2) for i in range(1, len(bins))])
ax.plot(kc, sig, color=charts.line("neutral"), lw=1.0, label="rotational average (simulated)")
ax.plot(kc, model, color=charts.line("negative"), lw=1.2, ls="--", label="model CTF² × envelope²")
kk = np.linspace(0.001, 0.45, 4000)
cc = np.pi * lam * 1.5e4 * kk**2 - 0.5 * np.pi * Cs * lam**3 * kk**4 + np.arctan(A / np.sqrt(1 - A**2))
zeros = kk[1:][np.diff(np.floor(cc / np.pi)) != 0]
for z in zeros[:6]:
    ax.axvline(z, color=P.muted(), lw=0.5, ls=":")
ax.text(zeros[0] + 0.004, 0.95, f"first zero\n{1 / zeros[0]:.1f} Å", fontsize=7, color=P.muted(), va="top")
ax.set_xlim(0, 0.45)
ax.set_ylim(-0.05, 1.0)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "spatial frequency k / Å⁻¹", "normalized power")
charts.title(ax, "B   Rotational average and CTF fit (Δf = 1.5 µm)")
fig.tight_layout()
