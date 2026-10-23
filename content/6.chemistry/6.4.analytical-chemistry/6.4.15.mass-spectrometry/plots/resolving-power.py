"""CO+ and N2+ (nominal m/z 28) recorded with Gaussian peaks of resolving power R = m / FWHM
equal to 1000, 3000 and 10000 (left), and the FWHM and 10 % valley definitions of R (right)."""

import numpy as np
import matplotlib.pyplot as plt

m_e = 0.000548580
m_co = 12.0 + 15.99491462 - m_e
m_n2 = 2 * 14.00307400 - m_e
x = np.linspace(27.96, 28.04, 4001)


def peak(m0, fwhm):
    s = fwhm / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-((x - m0) ** 2) / (2 * s**2))


fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.4, 3.9), gridspec_kw={"width_ratios": [1.25, 1]})
for k, (R, color) in enumerate([(1000, "C0"), (3000, "C1"), (10000, "C2")]):
    fwhm = 28.0 / R
    y = peak(m_co, fwhm) + peak(m_n2, fwhm)
    ax.plot(x, y / y.max() + 1.2 * (2 - k), color=color, lw=1.6)
    ax.text(27.962, 1.2 * (2 - k) + 0.75, f"$R = {R:,}$".replace(",", r"\,"), color=color, fontsize=9)
for m0, name in [(m_co, r"$\mathrm{CO^{+}}$" + f"\n{m_co:.4f}"), (m_n2, r"$\mathrm{N_2^{+}}$" + f"\n{m_n2:.4f}")]:
    ax.axvline(m0, color="0.6", lw=0.6, ls=":")
    ax.text(m0, 3.55, name, ha="center", va="bottom", fontsize=8)
ax.set_xlim(27.96, 28.04)
ax.set_ylim(-0.05, 4.1)
ax.set_yticks([])
ax.set_xlabel("$m/z$")
ax.set_title("same sample, three resolving powers", fontsize=10)

# Right: the two definitions for one peak pair at the 10 % valley separation.
s = 1.0
xx = np.linspace(-6, 10, 2001)
fwhm = 2 * np.sqrt(2 * np.log(2)) * s
dm = 2 * s * np.sqrt(2 * np.log(20))  # 10 % valley: each peak is 5 % high at the midpoint
g1 = np.exp(-xx**2 / 2)
g2 = np.exp(-((xx - dm) ** 2) / 2)
bx.plot(xx, g1 + g2, color="k", lw=1.6)
bx.plot(xx, g1, color="C0", lw=0.9, ls="--")
bx.plot(xx, g2, color="C0", lw=0.9, ls="--")
bx.annotate("", xy=(-fwhm / 2, 0.5), xytext=(fwhm / 2, 0.5), arrowprops=dict(arrowstyle="<->", lw=0.9))
bx.text(-fwhm / 2 - 0.3, 0.5, r"FWHM", ha="right", va="center", fontsize=8)
bx.annotate("", xy=(0, 1.12), xytext=(dm, 1.12), arrowprops=dict(arrowstyle="<->", lw=0.9))
bx.text(dm / 2, 1.17, r"$\Delta m$ (10 % valley)", ha="center", fontsize=8)
bx.axhline(0.1, color="C3", lw=0.7, ls=":")
bx.text(9.8, 0.13, "valley = 10 %", ha="right", fontsize=8, color="C3")
bx.set_ylim(0, 1.32)
bx.set_xlim(-6, 10)
bx.set_yticks([0, 0.5, 1.0])
bx.set_xticks([])
bx.set_xlabel("$m/z$")
bx.set_title(r"$R = m/\Delta m$: $\Delta m_{10\%\,\mathrm{valley}} \approx 2.08\,\mathrm{FWHM}$", fontsize=10)
fig.tight_layout()
