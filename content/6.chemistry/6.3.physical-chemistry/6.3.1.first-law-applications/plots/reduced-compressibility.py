import numpy as np
import matplotlib.pyplot as plt


def z_vdw(pr, tr):
    """Compressibility factor of a van der Waals gas in reduced variables (vapour-like root)."""
    roots = np.roots([3 * pr, -(pr + 8 * tr), 9, -3])
    real = roots[np.abs(roots.imag) < 1e-9].real
    vr = real.max()
    return 3 * pr * vr / (8 * tr)


pr = np.linspace(0.01, 8, 400)
fig, ax = plt.subplots(figsize=(7.5, 5))
colors = ["#dc2626", "#d97706", "#16a34a", "#0891b2", "#2563eb", "#7c3aed"]
for tr, c in zip([1.0, 1.2, 1.5, 2.0, 3.375, 5.0], colors):
    z = [z_vdw(p, tr) for p in pr]
    label = r"$T_{\mathrm{r}}$ = " + (f"{tr:g}" if tr != 3.375 else "27/8 (Boyle)")
    ax.plot(pr, z, color=c, lw=1.8, label=label)
ax.axhline(1, color="#94a3b8", lw=0.8, ls="--")
ax.axhline(3 / 8, color="#94a3b8", lw=0.8, ls=":")
ax.annotate(r"$Z_{\mathrm{c}} = 3/8$ (vdW); real gases about 0.29", (0.05, 0.375), xytext=(2.2, 0.2),
            fontsize=9, arrowprops=dict(arrowstyle="->", color="#94a3b8"))
ax.set_xlabel(r"reduced pressure $p_{\mathrm{r}} = p/p_{\mathrm{c}}$")
ax.set_ylabel(r"$Z = pV_{\mathrm{m}}/(RT)$")
ax.set_title("Generalized compressibility chart predicted by the reduced van der Waals equation", fontsize=10.5)
ax.set_xlim(0, 8)
ax.set_ylim(0, 1.6)
ax.grid(alpha=0.3)
ax.legend(fontsize=9, loc="lower right")
fig.tight_layout()
