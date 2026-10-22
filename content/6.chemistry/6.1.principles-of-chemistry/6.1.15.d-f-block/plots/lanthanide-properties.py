"""Lanthanoids La-Lu: (a) metallic radius (coordination number 12) and Ln3+ ionic radius (Shannon, CN 6);
(b) third ionization energy (CRC Handbook); (c) effective magnetic moments of Ln3+ at about 300 K:
g_J sqrt(J(J+1)) from the Hund ground term, the spin-only value sqrt(n(n+2)), and typical measured values."""

import numpy as np
import matplotlib.pyplot as plt

sym = "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu".split()
Z = np.arange(57, 72)
r_met = [187.7, 182.5, 182.8, 182.1, 181.1, 180.4, 204.2, 180.1, 178.3, 177.4, 176.6, 175.7, 174.6, 194.0, 173.4]
r_ion = [103.2, 101.0, 99.0, 98.3, 97.0, 95.8, 94.7, 93.8, 92.3, 91.2, 90.1, 89.0, 88.0, 86.8, 86.1]
i3 = [1850, 1949, 2086, 2130, 2150, 2260, 2404, 1990, 2114, 2200, 2204, 2194, 2285, 2417, 2022]
mu_exp = [0, 2.4, 3.5, 3.5, np.nan, 1.5, 3.4, 7.9, 9.7, 10.5, 10.5, 9.5, 7.3, 4.5, 0]


def hund(n):
    """Ground term (S, L, J) of f^n by Hund's rules."""
    ml = [3, 2, 1, 0, -1, -2, -3]
    if n <= 7:
        S, L = n / 2, sum(ml[:n])
    else:
        S, L = (14 - n) / 2, sum(ml[: n - 7])
    J = abs(L - S) if n < 7 else L + S
    return S, L, J


mu_j, mu_s = [], []
for n in range(15):
    S, L, J = hund(n)
    if J == 0:
        mu_j.append(0.0)
    else:
        g = 1 + (J * (J + 1) + S * (S + 1) - L * (L + 1)) / (2 * J * (J + 1))
        mu_j.append(g * np.sqrt(J * (J + 1)))
    mu_s.append(2 * np.sqrt(S * (S + 1)))

fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
ax = axes[0]
ax.plot(Z, r_met, "o-", color="C0", label="metallic radius (CN 12)")
ax.plot(Z, r_ion, "s-", color="C3", label=r"Ln$^{3+}$ radius (CN 6)")
ax.set_ylabel("radius / pm")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("(a) lanthanide contraction; Eu and Yb are divalent in the metal", fontsize=10)
ax = axes[1]
ax.plot(Z, i3, "o-", color="C2")
ax.set_ylabel(r"$I_3$ / (kJ mol$^{-1}$)")
ax.set_title(r"(b) third ionization energy: maxima at Eu (4f$^7$) and Yb (4f$^{14}$)", fontsize=10)
ax = axes[2]
ax.plot(Z, mu_j, "o-", color="C1", label=r"$g_J\sqrt{J(J+1)}$")
ax.plot(Z, mu_s, "s--", color="0.5", label=r"spin only $\sqrt{n(n+2)}$")
ax.plot(Z, mu_exp, "^", color="C0", ms=8, label="measured (about 300 K)")
ax.set_ylabel(r"$\mu_{\mathrm{eff}}$ / $\mu_{\mathrm{B}}$")
ax.set_title(r"(c) magnetic moments of Ln$^{3+}$", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_xticks(Z)
ax.set_xticklabels(sym)
fig.tight_layout()
