# Shade light, R:FR and the phytochrome photostationary state.
# Daylight: 5800 K black-body photon spectrum with a slight tilt, giving R:FR = 1.15.
# Canopy: Beer-Lambert attenuation I = I0 exp(-k LAI a(lambda)), k = 0.5, with a leaf absorptance
# a(lambda) of about 0.9 in the blue and red, 0.75 in the green and 0.1 in the far-red (schematic;
# scattering ignored). R:FR = photon flux 655-665 nm / 725-735 nm (Smith's definition).
# phi is computed with the same Pr/Pfr model spectra as in phytochrome-spectra.py.
# Panel C: internode extension rate falls linearly with phi (after Morgan & Smith's experiments with
# Chenopodium album and woodland species, 1970s); slopes and intercepts are illustrative.
import matplotlib.pyplot as plt
import numpy as np

wl = np.arange(300, 801, 1.0)


def band(c, a, sl, sr):
    s = np.where(wl < c, sl, sr)
    return a * np.exp(-0.5 * ((wl - c) / s) ** 2)


BASE_R = 0.012 * (wl < 720) * np.exp(-np.clip(wl - 650, 0, None) / 25)
PR = band(666, 1.0, 28, 17) + band(612, 0.22, 22, 22) + band(380, 0.28, 35, 35) + band(700, 0.0253, 25, 25) + BASE_R
PFR = band(730, 1.07, 32, 20) + band(672, 0.2125, 25, 25) + band(400, 0.541, 40, 40) + band(610, 0.10, 30, 30) + 0.012
PHI_R, PHI_FR = 0.15, 0.07

h, c, kB = 6.626e-34, 2.998e8, 1.381e-23
lam = wl * 1e-9
sun = lam**-4 / (np.exp(h * c / (lam * kB * 5800)) - 1)
sun = sun / sun[wl == 660] * (1 + 0.00146 * (660 - wl))

absorb = 0.1 + 0.8 / (1 + np.exp((wl - 700) / 6)) - 0.15 * np.exp(-0.5 * ((wl - 550) / 30) ** 2)


def canopy(lai):
    return sun * np.exp(-0.5 * lai * absorb)


def rfr(spec):
    return spec[(wl >= 655) & (wl <= 665)].sum() / spec[(wl >= 725) & (wl <= 735)].sum()


def phi(spec):
    k1 = (spec * PR * PHI_R).sum()
    k2 = (spec * PFR * PHI_FR).sum()
    return k1 / (k1 + k2)


fig, (a, b, cc) = plt.subplots(1, 3, figsize=(13.5, 4.0))
cols = {0: "#e0a030", 1: "#6aa84f", 3: "#2f7d4f", 6: "#1d4d30"}
for lai, col in cols.items():
    s = canopy(lai)
    a.plot(wl, s / sun[wl == 660], color=col, lw=2.0,
           label=f"LAI {lai}: R:FR = {rfr(s):.2f}, " + r"$\varphi$" + f" = {phi(s):.2f}")
a.set_yscale("log")
a.set_ylim(5e-3, 2)
a.set_xlim(400, 800)
a.set_xlabel("Wavelength / nm")
a.set_ylabel("Photon flux (relative to daylight at 660 nm)")
a.legend(frameon=False, fontsize=8, loc="lower right")
a.set_title("A   Light beneath a canopy (model)", loc="left", fontsize=10)

lais = np.linspace(0, 8, 120)
z = np.array([rfr(canopy(x)) for x in lais])
ph = np.array([phi(canopy(x)) for x in lais])
b.plot(z, ph, color="black", lw=2.2)
for lai, col in cols.items():
    s = canopy(lai)
    b.plot([rfr(s)], [phi(s)], "o", color=col, ms=7)
b.axhline(0.87, color="#d9463b", lw=0.8, ls=":")
b.axhline(0.025, color="#8b1e3f", lw=0.8, ls=":")
b.text(1.25, 0.82, "red limit 0.87", fontsize=8.5, color="#d9463b", ha="right")
b.text(1.25, 0.05, "far-red limit 0.025", fontsize=8.5, color="#8b1e3f", ha="right")
b.set_xlim(0, 1.3)
b.set_ylim(0, 0.95)
b.set_xlabel("R:FR (photon ratio)")
b.set_ylabel(r"Photostationary state $\varphi$")
b.set_title("B   R:FR sets $\\varphi$", loc="left", fontsize=10)

p = np.linspace(0.1, 0.7, 50)
cc.plot(p, 2.0 - 2.6 * (p - 0.1), color="#d9463b", lw=2.2, label="open-habitat (sun) species")
cc.plot(p, 0.65 - 0.25 * (p - 0.1), color="#2f7d4f", lw=2.2, label="woodland (shade-tolerant) species")
cc.set_xlabel(r"Photostationary state $\varphi$")
cc.set_ylabel(r"Internode extension rate / mm d$^{-1}$")
cc.set_ylim(0, 2.2)
cc.legend(frameon=False, fontsize=8.5, loc="upper right")
cc.set_title("C   Elongation responds to $\\varphi$", loc="left", fontsize=10)
for ax in (a, b, cc):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
