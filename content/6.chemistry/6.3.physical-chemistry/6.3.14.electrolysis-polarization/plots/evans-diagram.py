"""Evans diagrams for the corrosion of iron at 25 C (illustrative Tafel parameters).
Anodic: Fe -> Fe2+ + 2e-, E_eq = -0.62 V (a(Fe2+) = 1e-6), j0 = 1e-4 A/m2, Tafel slope 0.06 V/decade.
Left, deaerated acid (pH 1): cathodic H+ reduction on Fe, E_eq = -0.06 V, j0 = 1e-2 A/m2, 0.12 V/decade.
Right, aerated neutral water: O2 reduction, E_eq = +0.82 V, j0 = 1e-6 A/m2, 0.12 V/decade, limited by
O2 diffusion to j_L = 0.5 A/m2. The corrosion potential and current lie where the anodic and
cathodic currents are equal."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

E = np.linspace(-0.9, 1.0, 800)
ja = lambda e: 1e-4 * 10 ** ((e + 0.62) / 0.06)
jh = lambda e: 1e-2 * 10 ** (-(e + 0.06) / 0.12)
jo_kin = lambda e: 1e-6 * 10 ** (-(e - 0.82) / 0.12)
jo = lambda e: 1 / (1 / jo_kin(e) + 1 / 0.5)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), sharey=True)
for ax, jc, Ec, name in [(axes[0], jh, -0.06, r"H$^+$ reduction (pH 1)"), (axes[1], jo, 0.82, r"O$_2$ reduction (pH 7)")]:
    ec = brentq(lambda e: np.log10(ja(e)) - np.log10(jc(e)), -0.9, 0.8)
    ma = E > -0.62
    mc = E < Ec
    ax.plot(np.log10(ja(E[ma])), E[ma], color="C3", lw=1.8, label=r"Fe $\to$ Fe$^{2+}$ + 2e$^-$")
    ax.plot(np.log10(jc(E[mc])), E[mc], color="C0", lw=1.8, label=name)
    ax.plot(np.log10(ja(ec)), ec, "ko", ms=6)
    ax.annotate(rf"$E_\mathrm{{corr}}$ = {ec:.2f} V" + "\n" + rf"$j_\mathrm{{corr}}$ = {ja(ec):.2g} A m$^{{-2}}$",
                (np.log10(ja(ec)), ec), xytext=(-5.8, ec + 0.25), fontsize=9,
                arrowprops=dict(arrowstyle="->", lw=0.8))
    ax.set_xlim(-6.5, 2)
    ax.set_xlabel(r"$\lg\,(|j|$ / A m$^{-2})$")
    ax.legend(frameon=False, fontsize=8.5, loc="lower right")
axes[0].set_ylim(-0.9, 1.0)
axes[0].set_ylabel(r"$E$ / V (vs SHE)")
axes[0].set_title("deaerated acid: activation-controlled", fontsize=10)
axes[1].set_title("aerated neutral water: diffusion-limited O$_2$", fontsize=10)
fig.tight_layout()
