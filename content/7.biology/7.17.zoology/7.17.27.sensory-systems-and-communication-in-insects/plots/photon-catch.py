# Photons absorbed per photoreceptor per integration time against luminance (Land's sensitivity formula,
# Eq. 27.5; illustrative parameters of Example 27.5.1). 1 cd m^-2 ~ 4.1e3 photons s^-1 sr^-1 um^-2 (555 nm).
# Apposition eye (bee type): S = 0.24 um^2 sr, dt = 20 ms. Nocturnal apposition eye: same S, dt = 60 ms,
# spatial summation over 10 receptors. Superposition eye (moth type): S = 66 um^2 sr, dt = 40 ms.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P


def S(A, d, f, l, k=0.0067):
    return (np.pi / 4) ** 2 * A ** 2 * (d / f) ** 2 * (1 - np.exp(-k * l))


Sapp = S(20, 2, 60, 320)
Ssup = S(300, 8, 200, 200)
conv = 4.1e3
L = np.logspace(-4, 4, 200)
fig, ax = bio.canvas(22, 11)
p = quant.Plot(ax, (2.4, 2.6, 14.0, 7.6), xlim=(1e-4, 1e4), ylim=(1e-3, 1e7), xlog=True, ylog=True,
               xlabel="Luminance / (cd m^-2)", ylabel="Photons absorbed per integration time", ylabel_offset=1.6,
               xticks=[(1e-4, "10^-4"), (1e-2, "10^-2"), (1, "1"), (1e2, "10^2"), (1e4, "10^4")],
               yticks=[(1e-3, "10^-3"), (1e-1, "10^-1"), (10, "10"), (1e3, "10^3"), (1e5, "10^5"), (1e7, "10^7")])
p.band(L, np.full_like(L, 1e-3), np.ones_like(L), "negative", alpha=0.18)
p.text(2e-4, 0.08, "fewer than 1 photon: contrast invisible", color=P.muted(), ha="left")
for s, dt, n, tok, name, at in ((Sapp, 0.02, 1, "enzyme", "apposition (bee type)", 0.72),
                                 (Sapp, 0.06, 10, "positive", "apposition, slow + summed (nocturnal bee)", 0.6),
                                 (Ssup, 0.04, 1, "channel", "superposition (moth type)", 0.3)):
    N = s * conv * L * dt * n
    p.line(L, N, tok)
    lx = 10 ** (-4 + 8 * at)
    up = tok != "enzyme"
    p.text(lx, s * conv * lx * dt * n * (4 if up else 0.12), name, color=quant.line_color(tok), ha="right" if up else "left")
y = 1.2
for lo, hi, name in ((1e-4, 1e-3, "starlight"), (5e-3, 5e-2, "moonlight"), (1, 30, "dusk"), (300, 1e4, "daylight")):
    x0, x1 = p.X(lo), p.X(hi)
    ax.plot([x0, x1], [y, y], color=P.muted(), lw=2.2, solid_capstyle="butt")
    bio.label(ax, ((x0 + x1) / 2, y - 0.45), name, size="tiny", color=P.muted())
bio.label(ax, (17.3, 9.6), "S (um^2 sr)", size="small", ha="left", bold=True)
bio.label(ax, (17.3, 8.9), "apposition: %.2f" % Sapp, size="small", ha="left")
bio.label(ax, (17.3, 8.3), "superposition: %.0f" % Ssup, size="small", ha="left")
bio.label(ax, (17.3, 7.4), "N = S x photon radiance x dt", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.3, 6.9), "signal-to-noise = sqrt(N)", size="tiny", ha="left", color=P.muted())
