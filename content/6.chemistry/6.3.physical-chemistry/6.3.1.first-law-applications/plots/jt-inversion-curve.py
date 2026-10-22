import numpy as np
import matplotlib.pyplot as plt

# Inversion curve of a van der Waals gas: p_r = 24 sqrt(3 T_r) - 12 T_r - 27, 3/4 <= T_r <= 27/4.
tr = np.linspace(0.75, 6.75, 400)
pr = 24 * np.sqrt(3 * tr) - 12 * tr - 27

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(tr, pr, color="#2563eb", lw=2.2, label="vdW inversion curve")
ax.fill_between(tr, pr, color="#2563eb", alpha=0.12)
ax.text(3.0, 3.5, "cooling on expansion\n" + r"$\mu_{\mathrm{JT}} > 0$", ha="center", fontsize=10)
ax.text(5.6, 7.5, "heating on expansion\n" + r"$\mu_{\mathrm{JT}} < 0$", ha="center", fontsize=10)
# Upper inversion temperatures at low pressure, reduced by T_c (experimental, approximate)
data = {"N2": 621 / 126.2, "Ar": 723 / 150.7, "H2": 202 / 33.15, "He": 40 / 5.2}
offsets = {"N2": (10, 8), "Ar": (-10, 8), "H2": (0, 8), "He": (0, 8)}
for name, x in data.items():
    ax.plot([x], [0.15], marker="v", color="#dc2626", ms=7)
    ax.annotate(name, (x, 0.15), xytext=offsets[name], textcoords="offset points", ha="center", fontsize=9, color="#dc2626")
ax.plot([6.75], [0], marker="o", color="#2563eb")
ax.annotate(r"$T_{\mathrm{r}} = 27/4$", (6.75, 0), xytext=(6.9, 1.6), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#94a3b8"))
ax.set_xlabel(r"reduced temperature $T_{\mathrm{r}} = T/T_{\mathrm{c}}$")
ax.set_ylabel(r"reduced pressure $p_{\mathrm{r}} = p/p_{\mathrm{c}}$")
ax.set_title("Joule-Thomson inversion curve; triangles: measured low-pressure inversion temperatures", fontsize=10)
ax.set_xlim(0, 8)
ax.set_ylim(0, 10.5)
ax.grid(alpha=0.3)
ax.legend(fontsize=9, loc="upper right")
fig.tight_layout()
