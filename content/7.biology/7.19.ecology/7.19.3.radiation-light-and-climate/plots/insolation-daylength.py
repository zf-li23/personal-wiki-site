# Astronomical controls of radiation and day length (computed, not measured).
# Solar declination: delta = 23.44 deg * sin(2 pi (284 + n) / 365) (Cooper 1969); orbital eccentricity
# factor (1 + 0.033 cos(2 pi n / 365)).
# A: daily mean top-of-atmosphere insolation Q = (S0 / pi) E (h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)),
#    cos(h0) = -tan(phi) tan(delta), S0 = 1361 W m^-2, as a function of latitude and day of year.
# B: day length (hours between sunrise and sunset, sun's centre at -0.833 deg to allow for refraction and the
#    solar disc) through the year at several northern latitudes.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
S0 = 1361.0
n = np.arange(1, 366)
decl = np.radians(23.44) * np.sin(2 * np.pi * (284 + n) / 365)
ecc = 1 + 0.033 * np.cos(2 * np.pi * n / 365)


def insolation(phi_deg):
    phi = np.radians(phi_deg)[:, None]
    c = np.clip(-np.tan(phi) * np.tan(decl[None, :]), -1, 1)
    h0 = np.arccos(c)
    return S0 / np.pi * ecc[None, :] * (h0 * np.sin(phi) * np.sin(decl) + np.cos(phi) * np.cos(decl) * np.sin(h0))


def daylength(phi_deg):
    phi = np.radians(phi_deg)
    h = np.radians(-0.833)
    c = (np.sin(h) - np.sin(phi) * np.sin(decl)) / (np.cos(phi) * np.cos(decl))
    return 24 / np.pi * np.arccos(np.clip(c, -1, 1))


lat = np.linspace(-90, 90, 361)
Q = insolation(lat)
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.5), gridspec_kw={"width_ratios": [1.15, 1]})
levels = np.arange(0, 600, 50)
cf = a.contourf(n, lat, Q, levels=levels, cmap="YlOrRd")
cs = a.contour(n, lat, Q, levels=[100, 200, 300, 400, 500], colors=[P.ink()], linewidths=0.5)
a.clabel(cs, fmt="%d", fontsize=7, colors=[P.ink()])
a.plot(n, np.degrees(decl), color=P.ink(), lw=1.0, ls="--")
a.text(120, np.degrees(decl[119]) + 3, "subsolar latitude", fontsize=7.5, color=P.ink())
cb = fig.colorbar(cf, ax=a, pad=0.02)
cb.set_label("Daily mean insolation / W m⁻²", color=P.ink())
a.set_xticks([1, 80, 172, 266, 355])
a.set_xticklabels(["1 Jan", "21 Mar", "21 Jun", "23 Sep", "21 Dec"])
a.set_yticks([-90, -60, -30, 0, 30, 60, 90])
a.set_ylabel("Latitude / °")
a.set_title("A  Top-of-atmosphere insolation", loc="left", fontweight="bold")

for phi, tok in ((0, "positive"), (23.5, "atp"), (40, "rna"), (55, "negative"), (66.5, "metabolite"),
                 (70, "dna")):
    b.plot(n, daylength(phi), color=P.edge(tok), lw=1.8, label="%g° N" % phi)
b.axhline(12, color=P.muted(), lw=0.6, ls=":")
b.set_xticks([1, 80, 172, 266, 355])
b.set_xticklabels(["1 Jan", "21 Mar", "21 Jun", "23 Sep", "21 Dec"])
b.set_ylim(0, 24.5)
b.set_yticks([0, 6, 12, 18, 24])
b.set_ylabel("Day length / h")
b.legend(frameon=False, fontsize=7.5, loc="upper right", ncol=2)
b.set_title("B  Day length", loc="left", fontweight="bold")
for s in ("top", "right"):
    b.spines[s].set_visible(False)
fig.tight_layout()
