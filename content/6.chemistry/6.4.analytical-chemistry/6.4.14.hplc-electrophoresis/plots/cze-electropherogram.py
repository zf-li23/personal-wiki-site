"""Simulated capillary-zone electropherogram with electro-osmotic flow (normal polarity:
anode at the inlet, detector near the cathode). Capillary 60 cm total, 50 cm to the
detector, 25 kV; mu_eo = 5.0e-8 m^2/(V s). Each zone migrates with mu_app = mu_ep + mu_eo and
broadens only by diffusion (D = 1e-9 m^2/s), sigma_x^2 = 2 D t. Cations arrive first,
the neutral molecules all at the electro-osmotic time t_eo (unresolved), anions last; an
anion with |mu_ep| > mu_eo would never reach the detector."""

import numpy as np
import matplotlib.pyplot as plt

Lt, Ld, U, mueo, D = 0.60, 0.50, 25e3, 5.0e-8, 1.0e-9
E = U / Lt
zones = [("cation 1", 3.5e-8, "C3"), ("cation 2", 2.0e-8, "C3"), ("neutrals", 0.0, "0.3"),
         ("anion 1", -1.5e-8, "C0"), ("anion 2", -3.0e-8, "C0")]
t = np.linspace(100, 700, 60000)
fig, ax = plt.subplots(figsize=(7.2, 3.8))
curves = []
for name, mu, col in zones:
    v = (mu + mueo) * E
    tm = Ld / v
    st = np.sqrt(2 * D * tm) / v
    amp = 2.0 if name == "neutrals" else 1.0
    curves.append((name, col, tm, amp * np.exp(-0.5 * ((t - tm) / st) ** 2) / st))
top = max(c[3].max() for c in curves)
for name, col, tm, yi in curves:
    yi = yi / top
    ax.plot(t / 60, yi, color=col, lw=1.2)
    N = Ld ** 2 / (2 * D * tm)
    ax.text(tm / 60, yi.max() + 0.03, f"{name}\nN = {N / 1e3:.0f}k", ha="center", fontsize=7)
ax.axvline(Ld / (mueo * E) / 60, color="0.5", lw=0.8, ls=":")
ax.set_xlabel("migration time / min")
ax.set_ylabel("absorbance (a.u.)")
ax.set_yticks([])
ax.set_ylim(0, 1.3)
ax.set_xlim(1.8, 11)
fig.tight_layout()
