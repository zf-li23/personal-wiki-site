# Absorption spectra of the two phytochrome forms and the photostationary state they set.
# The spectra are sums of asymmetric Gaussian bands placed at the published band positions
# (Pr 666 nm with a 610 nm shoulder and a 380 nm band; Pfr 730 nm with bands near 670 and 400 nm),
# with amplitudes tuned so that the model reproduces the measured photostationary states
# (about 0.87 Pfr under saturating red, 0.02-0.03 under far-red, about 0.6 in daylight).
# Photoconversion quantum yields: Pr->Pfr 0.15, Pfr->Pr 0.07 (approximate in-vitro values).
# phi(lambda) = eps_r Phi_r / (eps_r Phi_r + eps_fr Phi_fr) for monochromatic light.
import matplotlib.pyplot as plt
import numpy as np

wl = np.arange(300, 801, 1.0)


def band(c, a, sl, sr):
    s = np.where(wl < c, sl, sr)
    return a * np.exp(-0.5 * ((wl - c) / s) ** 2)


BASE_R = 0.012 * (wl < 720) * np.exp(-np.clip(wl - 650, 0, None) / 25)  # weak background absorption
PR = band(666, 1.0, 28, 17) + band(612, 0.22, 22, 22) + band(380, 0.28, 35, 35) + band(700, 0.0253, 25, 25) + BASE_R
PFR = band(730, 1.07, 32, 20) + band(672, 0.2125, 25, 25) + band(400, 0.541, 40, 40) + band(610, 0.10, 30, 30) + 0.012
PHI_R, PHI_FR = 0.15, 0.07

phi = PR * PHI_R / (PR * PHI_R + PFR * PHI_FR)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.0))
a.axvspan(655, 665, color="#d9463b", alpha=0.15, lw=0)
a.axvspan(725, 735, color="#8b1e3f", alpha=0.15, lw=0)
a.plot(wl, PR, color="#2f7d4f", lw=2.2, label="Pr")
a.plot(wl, PFR, color="#3b6fd8", lw=2.2, label="Pfr")
a.annotate("666 nm", xy=(666, 1.0), xytext=(545, 1.08), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.8, color="0.4"))
a.annotate("730 nm", xy=(730, 1.07), xytext=(748, 1.13), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.8, color="0.4"))
a.text(660, -0.09, "R", ha="center", fontsize=9, color="#d9463b")
a.text(730, -0.09, "FR", ha="center", fontsize=9, color="#8b1e3f")
a.set_xlim(300, 800)
a.set_ylim(-0.13, 1.2)
a.set_xlabel("Wavelength / nm")
a.set_ylabel("Relative absorbance")
a.legend(frameon=False, fontsize=9, loc="upper left")
a.set_title("A   Absorption spectra (model)", loc="left", fontsize=10)

b.plot(wl, phi, color="black", lw=2.2)
b.axhline(0.60, color="#e0a030", lw=1.2, ls="--")
b.text(305, 0.63, "daylight, about 0.6", fontsize=9, color="#b07818")
for x, y, t, dx, dy in ((660, phi[wl == 660][0], "0.87 (red)", -175, -0.12),
                        (730, phi[wl == 730][0], "0.025 (far-red)", -195, 0.12)):
    b.plot([x], [y], "o", color="#d9463b" if x == 660 else "#8b1e3f", ms=6)
    b.annotate(t, xy=(x, y), xytext=(x + dx, y + dy), fontsize=9,
               arrowprops=dict(arrowstyle="->", lw=0.8, color="0.4"))
b.set_xlim(300, 800)
b.set_ylim(0, 1.0)
b.set_xlabel("Wavelength / nm")
b.set_ylabel(r"Photostationary state $\varphi$ = [Pfr]/[P$_{\rm tot}$]")
b.set_title("B   Photostationary state of monochromatic light", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
