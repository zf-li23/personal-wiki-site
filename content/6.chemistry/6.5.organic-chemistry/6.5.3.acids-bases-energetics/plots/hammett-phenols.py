"""Hammett plot for the acidity of substituted phenols in water at 25 C. pKa values: CRC Handbook;
substituent constants: Hansch, Leo and Taft, Chem. Rev. 1991, 91, 165. The straight line is the
least-squares fit pKa(H) - pKa(X) = rho * sigma to the meta substituents and to the para substituents
without a pi-acceptor. p-NO2 and p-CN fall far off the line when plotted against sigma_p (open
circles) because the phenoxide charge is delocalized directly onto them; against sigma_p^- (filled
squares) they fall back on the line."""

import numpy as np
import matplotlib.pyplot as plt

# substituent: (sigma, pKa)
data = {
    "H": (0.00, 9.99),
    "m-CH3": (-0.07, 10.09), "p-CH3": (-0.17, 10.26),
    "m-OCH3": (0.12, 9.65), "p-OCH3": (-0.27, 10.21),
    "m-F": (0.34, 9.28), "p-F": (0.06, 9.89),
    "m-Cl": (0.37, 9.12), "p-Cl": (0.23, 9.41),
    "m-Br": (0.39, 9.03), "p-Br": (0.23, 9.37),
    "m-CN": (0.56, 8.61), "m-NO2": (0.71, 8.36),
}
acceptors = {"p-CN": (0.66, 1.00, 7.95), "p-NO2": (0.78, 1.27, 7.15)}  # sigma_p, sigma_p^-, pKa

pka_h = data["H"][1]
s = np.array([v[0] for v in data.values()])
y = np.array([pka_h - v[1] for v in data.values()])
rho = float(s @ y / (s @ s))  # line through the origin: X = H defines sigma = 0
resid = y - rho * s
r2 = 1 - (resid @ resid) / ((y - y.mean()) @ (y - y.mean()))

fig, ax = plt.subplots(figsize=(6.4, 4.6))
grid = np.linspace(-0.4, 1.4, 50)
ax.plot(grid, rho * grid, color="0.5", lw=1, label=rf"fit: $\rho = {rho:.2f}$ ($R^2 = {r2:.3f}$)")
ax.scatter(s, y, color="#2563eb", zorder=3, label=r"$\sigma_m$, $\sigma_p$")
def tex(name):
    return name.replace("CH3", "CH$_3$").replace("OCH$_3$", "OCH$_3$").replace("NO2", "NO$_2$")


shown = {"H": (-14, 4), "p-OCH3": (-10, 8), "p-CH3": (4, -12), "p-F": (6, -8), "m-OCH3": (-46, 4), "p-Cl": (6, -10), "m-Cl": (6, -10), "m-Br": (-38, 4), "m-CN": (6, -8), "m-NO2": (6, -8)}
for name, (sx, sy) in zip(data, zip(s, y)):
    if name in shown:
        ax.annotate(tex(name), (sx, sy), xytext=shown[name], textcoords="offset points", fontsize=8)
for name, (sp, sm, pka) in acceptors.items():
    d = pka_h - pka
    ax.scatter([sp], [d], facecolors="none", edgecolors="#f97316", zorder=3)
    ax.scatter([sm], [d], marker="s", color="#f97316", zorder=3)
    ax.annotate("", xy=(sm - 0.03, d), xytext=(sp + 0.03, d), arrowprops=dict(arrowstyle="->", color="#f97316", lw=1))
    ax.annotate(tex(name), (sm, d), xytext=(6, -3), textcoords="offset points", fontsize=8)
ax.scatter([], [], facecolors="none", edgecolors="#f97316", label=r"$\pi$-acceptors at $\sigma_p$")
ax.scatter([], [], marker="s", color="#f97316", label=r"$\pi$-acceptors at $\sigma_p^-$")
ax.set_xlabel(r"substituent constant $\sigma$")
ax.set_ylabel(r"$\mathrm{p}K_{\mathrm{a}}(\mathrm{H}) - \mathrm{p}K_{\mathrm{a}}(\mathrm{X})$")
ax.legend(frameon=False, fontsize=8, loc="upper left")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
