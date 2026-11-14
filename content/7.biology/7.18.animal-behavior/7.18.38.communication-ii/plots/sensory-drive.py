"""Sensory drive in Lake Victoria cichlids (schematic, after Seehausen et al. 2008).

A: downwelling light at depth z: I(l, z) = I0(l) exp(-K(l) z), with K = water absorption + turbidity term
falling with wavelength. B: Govardovskii A1 opsin templates (lambda_max 553 and 565 nm) and reflectance of a blue
and a red male. C: quantum catch ratio red male / blue male for each opsin against depth.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
lam = np.linspace(400, 700, 301)


def template(lmax):
    x = lmax / lam
    a = 0.8795 + 0.0459 * np.exp(-((lmax - 300) ** 2) / 11940)
    return 1 / (np.exp(69.7 * (a - x)) + np.exp(28 * (0.922 - x)) + np.exp(-14.9 * (1.104 - x)) + 0.674)


K = 0.05 + 1.0 * np.exp(-(lam - 400) / 45) + 0.25 * np.exp((lam - 700) / 60)  # 1/m
I0 = np.ones_like(lam)
def light(z):
    return I0 * np.exp(-K * z)

R_blue = 0.05 + 0.6 * np.exp(-((lam - 470) / 35) ** 2)
R_red = 0.05 + 0.7 / (1 + np.exp(-(lam - 600) / 12))

fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.7))
a, b, c = axs
for z, tok in ((0.5, "neutral"), (2, "dna"), (4, "positive"), (6, "rna")):
    I = light(z)
    a.plot(lam, I / I.max(), color=P.edge(tok), lw=1.6, label=f"{z:g} m")
a.set_xlabel("Wavelength / nm"); a.set_ylabel("Relative irradiance (normalized)")
a.legend(frameon=False, fontsize=8, title="depth", title_fontsize=8)
a.set_title("A", loc="left", fontweight="bold")

for lm, ls, lab in ((553, "-", "LWS short (553 nm)"), (565, "--", "LWS long (565 nm)")):
    b.plot(lam, template(lm), color=P.ink(), ls=ls, lw=1.5, label=lab)
b.plot(lam, R_blue, color=P.edge("dna"), lw=1.8, label="blue male")
b.plot(lam, R_red, color=P.edge("negative"), lw=1.8, label="red male")
b.set_xlabel("Wavelength / nm"); b.set_ylabel("Absorbance or reflectance")
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_ylim(0, 1.15)
b.set_title("B", loc="left", fontweight="bold")

zs = np.linspace(0, 7, 60)
for lm, ls, lab in ((553, "-", "short opsin"), (565, "--", "long opsin")):
    S = template(lm)
    ratio = [np.trapezoid(light(z) * R_red * S, lam) / np.trapezoid(light(z) * R_blue * S, lam) for z in zs]
    c.plot(zs, ratio, color=P.ink(), ls=ls, lw=1.7, label=lab)
c.axhline(1, color=P.muted(), lw=0.8, ls=":")
c.set_xlabel("Depth / m"); c.set_ylabel("Brightness of red male / blue male")
c.legend(frameon=False, fontsize=8)
c.set_title("C", loc="left", fontweight="bold")
for ax in axs:
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
