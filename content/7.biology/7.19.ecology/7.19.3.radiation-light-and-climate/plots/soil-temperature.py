# Periodic heat conduction into a homogeneous soil (analytical solution of the heat equation).
# Surface temperature T(0, t) = Tm + A sin(omega t); then T(z, t) = Tm + A exp(-z/d) sin(omega t - z/d) with
# damping depth d = sqrt(2 kappa / omega). Thermal diffusivity kappa = 5e-7 m^2 s^-1 (moist mineral soil).
# Daily cycle: Tm = 20 C, A = 15 C, surface maximum at 13:00. Annual cycle: Tm = 12 C, A = 14 C.
# A: daily profiles (tautochrones) every 3 h, 0-60 cm. B: amplitude and time lag of the daily and annual waves
# against depth.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
kappa = 5e-7
w_day = 2 * np.pi / 86400.0
w_year = 2 * np.pi / (365.25 * 86400.0)
d_day = np.sqrt(2 * kappa / w_day)
d_year = np.sqrt(2 * kappa / w_year)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.4))
z = np.linspace(0, 0.6, 301)
hours = np.arange(1, 25, 3)
cmap = plt.get_cmap("twilight")
for k, h in enumerate(hours):
    phase = w_day * (h - 7) * 3600.0  # sin peaks at 13:00
    T = 20 + 15 * np.exp(-z / d_day) * np.sin(phase - z / d_day)
    a.plot(T, 100 * z, color=cmap(k / len(hours)), lw=1.8, label="%02d:00" % h)
a.set_ylim(60, 0)
a.set_xlabel("Soil temperature / °C")
a.set_ylabel("Depth / cm")
a.legend(frameon=False, fontsize=7, ncol=2, loc="lower right")
a.set_title("A  Daily temperature profiles", loc="left", fontweight="bold")

zz = np.linspace(0, 12, 601)
b.semilogx(100 * np.exp(-zz / d_day), zz, color=P.edge("rna"), lw=2, label="daily wave, d = %.0f cm" % (100 * d_day))
b.semilogx(100 * np.exp(-zz / d_year), zz, color=P.edge("dna"), lw=2,
           label="annual wave, d = %.1f m" % d_year)
b.set_ylim(12, 0)
b.set_xlim(0.01, 120)
b.axvline(1, color=P.muted(), lw=0.7, ls=":")
b.set_xlabel("Amplitude / % of surface amplitude (log scale)")
b.set_ylabel("Depth / m")
b.legend(frameon=False, fontsize=7.5, loc="lower left")
b.set_title("B  Damping with depth", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
