# X-band (9.5 GHz) cw-EPR of a nitroxide spin label (electron S = 1/2 coupled to 14N, I = 1).
# A: energy levels in a field B: the electron Zeeman levels m_S = +-1/2, each split by the hyperfine coupling
#    into m_I = +1, 0, -1; the three allowed transitions (Delta m_S = +-1, Delta m_I = 0) at fixed microwave
#    frequency give three lines separated by the isotropic coupling a = 1.5 mT.
# B: first-derivative spectra. Fast motion (tau_c = 0.1, 0.5 and 1.5 ns): three Lorentzian lines whose widths
#    follow the motional-narrowing (Kivelson) expression 1/T2(m) = A + B m + C m^2 with B and C proportional to
#    tau_c, for axial tensors g_par = 2.0027, g_perp = 2.0075, A_par = 3.5 mT, A_perp = 0.6 mT (residual width
#    A = 0.1 mT); the high-field line (m_I = -1) broadens most. Rigid limit (tau_c > 100 ns, frozen solution):
#    powder spectrum summed over orientations with Gaussian broadening of 0.25 mT; the outer extrema are
#    separated by about 2 A_par. The intermediate regime (2-100 ns) needs the stochastic Liouville equation
#    and is not computed here.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
h, muB, hb = 6.62607015e-34, 9.2740100783e-24, 1.054571817e-34
nu = 9.5e9
gpar, gperp, Apar, Aperp = 2.0027, 2.0075, 3.5e-3, 0.6e-3
giso, aiso = (gpar + 2 * gperp) / 3, (Apar + 2 * Aperp) / 3
B0 = h * nu / (giso * muB)
Bax = np.linspace(B0 - 0.0055, B0 + 0.0055, 3000)

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw=dict(width_ratios=[0.8, 1.2]))

ax = axs[0]
ax.axis("off")
ax.set_xlim(0, 10)
ax.set_ylim(-0.3, 10)
ax.plot([0.5, 3], [5, 5], color=P.ink(), lw=1.2)
ax.text(1.7, 5.25, "B = 0", ha="center", fontsize=8, color=P.ink())
for ms, y0 in ((+0.5, 8.0), (-0.5, 2.0)):
    ax.plot([3, 4.5], [5, y0], color=P.muted(), lw=0.8, ls=":")
    ax.plot([4.5, 6], [y0, y0], color=P.ink(), lw=1.4)
    ax.text(4.6, y0 + 0.3, (r"$m_S = +1/2$" if ms > 0 else r"$m_S = -1/2$"), fontsize=8, color=P.ink())
    for mi in (1, 0, -1):
        yy = y0 + (0.8 * mi if ms > 0 else -0.8 * mi)
        ax.plot([6, 6.7], [y0, yy], color=P.muted(), lw=0.7, ls=":")
        ax.plot([6.7, 8.4], [yy, yy], color=P.ink(), lw=1.2)
        ax.text(8.5, yy, r"$m_I = %s$" % ({1: "+1", 0: "0", -1: "-1"}[mi]), fontsize=7.5, color=P.ink(), va="center")
for k, mi in enumerate((1, 0, -1)):
    x = 7.0 + 0.5 * k
    ax.annotate("", xy=(x, 8.0 + 0.8 * mi), xytext=(x, 2.0 - 0.8 * mi),
                arrowprops=dict(arrowstyle="<->", color=charts.line("rna"), lw=1.0))
ax.text(5.2, 0.2, r"$\Delta m_S = \pm 1$, $\Delta m_I = 0$: three lines, spacing $a$", fontsize=7.5, color=P.ink(), ha="center")
charts.title(ax, "A   Electron Zeeman + ¹⁴N hyperfine levels")

ax = axs[1]
ge = 1.76085963e11 * giso / 2.0023


def deriv(y):
    return np.gradient(y, Bax)


offset = 0.0
b = (2 / 3) * ge * (Apar - Aperp)                    # rad/s
dgB = (2 / 3) * (muB / hb) * (gpar - gperp) * B0      # rad/s
for tc, tok in ((0.1e-9, "protein"), (0.5e-9, "enzyme"), (1.5e-9, "rna")):
    y = np.zeros_like(Bax)
    for m in (1, 0, -1):
        w = 1e-4 + ((4 / 15) * b * dgB * tc * m + b**2 * tc / 8 * m**2) / ge   # T, half width
        Bc = B0 - m * aiso
        y += w / ((Bax - Bc) ** 2 + w**2)
    d = deriv(y)
    ax.plot((Bax - B0) * 1e3, d / np.abs(d).max() + offset, color=charts.line(tok), lw=1.3)
    ax.text(5.4, offset + 0.25, f"τc = {tc * 1e9:g} ns", fontsize=7.5, color=P.ink(), ha="right")
    offset -= 2.3
# rigid limit powder pattern
y = np.zeros_like(Bax)
for c in np.linspace(0, 1, 3000):
    g = np.sqrt(gpar**2 * c**2 + gperp**2 * (1 - c**2))
    A = np.sqrt((Apar**2 * gpar**2 * c**2 + Aperp**2 * gperp**2 * (1 - c**2))) / g
    for m in (1, 0, -1):
        Bc = h * nu / (g * muB) - m * A
        y += np.exp(-0.5 * ((Bax - Bc) / 2.5e-4) ** 2)
d = deriv(y)
ax.plot((Bax - B0) * 1e3, d / np.abs(d).max() + offset, color=charts.line("dna"), lw=1.3)
ax.text(5.4, offset + 0.4, "rigid limit", fontsize=7.5, color=P.ink(), ha="right")
ax.set_xlim(-5.5, 5.5)
ax.set_yticks([])
charts.style_axes(ax, "B − B₀ / mT  (B₀ = 0.339 T)", "dχ″/dB")
charts.title(ax, "B   Spectra report label mobility")
fig.tight_layout()
