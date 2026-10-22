import numpy as np
import matplotlib.pyplot as plt

# Fugacity coefficient of a van der Waals gas in reduced variables (law of corresponding states).


def lnphi(pr, Tr):
    A = 27 * pr / (64 * Tr**2)
    B = pr / (8 * Tr)
    roots = np.roots([1, -(1 + B), A, -A * B])
    Z = roots[np.abs(roots.imag) < 1e-9].real.max()  # gas-like root
    return Z - 1 - np.log(Z - B) - A / Z, Z


pr = np.linspace(1e-3, 10, 400)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
colors = ["#7c3aed", "#2563eb", "#0891b2", "#16a34a", "#d97706", "#dc2626"]
for Tr, c in zip([1.0, 1.2, 1.5, 2.0, 3.0, 5.0], colors):
    vals = np.array([lnphi(p, Tr) for p in pr])
    a1.plot(pr, np.exp(vals[:, 0]), color=c, lw=2, label=f"$T_r$ = {Tr}")
    a2.plot(pr, vals[:, 1], color=c, lw=2, label=f"$T_r$ = {Tr}")
for ax in (a1, a2):
    ax.axhline(1, color="#94a3b8", lw=1)
    ax.set_xlabel("$p_r = p/p_c$")
    ax.grid(alpha=0.3)
a1.set_ylabel(r"$\varphi = f/p$")
a1.set_title("Fugacity coefficient, van der Waals gas", fontsize=11)
a1.legend(fontsize=9, loc="upper left", ncol=2)
a2.set_ylabel("$Z = pV_\\mathrm{m}/RT$")
a2.set_title("Compressibility factor", fontsize=11)
a2.legend(fontsize=9, loc="upper left", ncol=2)
fig.tight_layout()
