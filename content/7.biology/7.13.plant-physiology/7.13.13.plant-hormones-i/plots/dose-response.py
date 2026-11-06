# Dose-response of root, bud and stem growth to auxin (schematic after Thimann 1937).
# Growth relative to no auxin: G(c) = (1 + Emax * A(c)) * I(c) - 1, with a promotion term
# A = c^n / (K1^n + c^n) and an inhibition term I = K2^n / (K2^n + c^n) (Eq. 13.7, product form).
import matplotlib.pyplot as plt
import numpy as np

c = np.logspace(-13, -2, 600)
organs = [
    # name, K1, K2, Emax, colour
    ("Root", 10 ** -11.0, 10 ** -8.6, 1.6, "#c0504d"),
    ("Bud", 10 ** -9.0, 10 ** -6.6, 1.6, "#4f9a52"),
    ("Stem", 10 ** -6.2, 10 ** -3.6, 2.0, "#2f6fb5"),
]
n = 1.4


def growth(c, k1, k2, emax):
    a = c ** n / (k1 ** n + c ** n)
    i = k2 ** n / (k2 ** n + c ** n)
    return 100 * ((1 + emax * a) * i - 1)


fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.axhline(0, color="0.5", lw=0.8)
for name, k1, k2, emax, col in organs:
    g = growth(c, k1, k2, emax)
    ax.plot(c, g, color=col, lw=2.3, label=name)
    j = np.argmax(g)
    ax.plot(c[j], g[j], "o", color=col, ms=5)
    ax.annotate(f"optimum\n~10$^{{{np.log10(c[j]):.0f}}}$ M", (c[j], g[j]), xytext=(0, 10),
                textcoords="offset points", ha="center", fontsize=8.5, color=col)
ax.axvline(1e-6, color="0.4", lw=0.9, ls="--")
ax.text(1.3e-6, -88, "$10^{-6}$ M: stem promoted,\nroot inhibited", fontsize=8.5, va="bottom")
ax.set_xscale("log")
ax.set_xlim(1e-13, 1e-2)
ax.set_ylim(-105, 250)
ax.set_xticks([1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2])
ax.set_xlabel("Auxin concentration / (mol L$^{-1}$)")
ax.set_ylabel("Growth change vs. control / %")
ax.text(2e-13, 30, "promotion", fontsize=8.5, color="0.4")
ax.text(2e-13, -40, "inhibition", fontsize=8.5, color="0.4")
ax.legend(frameon=False, loc="center right", fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
