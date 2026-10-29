"""A contractile surface layer is unstable: tension-raising molecules gather where tension is high.

Minimal one-dimensional model on a closed meridian of a spherical cell (arc length s, circumference
2 pi R, R = 1): a surface species c (myosin, or Greenspan's surfactant) raises the surface tension,
T(c) = beta c / (1 + c/c_s); the surface flow v obeys the force balance xi v - eta d2v/ds2 = dT/ds
(friction xi, surface viscosity eta), and c is carried by the flow, diffuses and turns over:
dc/dt = -d(c v)/ds + D d2c/ds2 + k (c0 - c).
Linear growth rate of a mode cos(n s / R), q = n/R: s_n = q^2 [c0 T'(c0)/(xi + eta q^2) - D] - k.
Parameters: xi = 1, eta = 0.25, c0 = 1, c_s = 2, beta = 4.5 (c0 T'(c0) = 2), k = 0.1.
A: s_n for D = 0.5, 1 and 2 (n = 1: one cap, polarization; n = 2: two opposite maxima on the
meridian, i.e. an equatorial ring, a cleavage furrow). B: simulation for D = 0.5 from 1% random
noise (spectral method, 128 points): c(s, t) concentrates into two opposite peaks. C: the final c
drawn on the cell outline, rotated so that a peak lies at the equator.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(1)
xi, eta, c0, cs, beta, kt = 1.0, 0.25, 1.0, 2.0, 4.5, 0.1
A = c0 * beta / (1 + c0 / cs) ** 2

fig, ax = bio.canvas(32.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 8.2, 7.0))
nn = np.arange(1, 7)
for Dv, tok in ((0.5, "mesoderm"), (1.0, "highlight"), (2.0, "ectoderm")):
    q = nn.astype(float)
    sn = q ** 2 * (A / (xi + eta * q ** 2) - Dv) - kt
    pa.plot(nn, sn, "o-", color=quant.line_color(tok), lw=1.8, ms=4, label=f"D = {Dv:g}")
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0.6, 6.4)
pa.set_ylim(-6, 2.5)
charts.style_axes(pa, "mode n", "growth rate s_n")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower left")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pa, "Long waves go unstable first")

N = 128
s = np.linspace(0, 2 * np.pi, N, endpoint=False)
kq = np.fft.fftfreq(N, d=1 / N)
c = c0 * (1 + 0.01 * rng.standard_normal(N))
Dv = 0.5
dt, tmax = 2e-3, 12.0
kym = []
for it in range(int(tmax / dt) + 1):
    if it % 100 == 0:
        kym.append(c.copy())
    T = beta * c / (1 + c / cs)
    Th = np.fft.fft(T)
    vh = 1j * kq * Th / (xi + eta * kq ** 2)
    v = np.real(np.fft.ifft(vh))
    flux = c * v
    dc = -np.real(np.fft.ifft(1j * kq * np.fft.fft(flux))) + kt * (c0 - c)
    ch = np.fft.fft(c + dt * dc)
    c = np.real(np.fft.ifft(ch / (1 + dt * Dv * kq ** 2)))
kym = np.array(kym)

bio.panel(ax, "B", (11.6, 9.9))
pb = charts.axes_at(ax, (13.4, 1.8, 8.2, 7.0))
im = pb.imshow(kym, aspect="auto", origin="lower", extent=(0, 360, 0, tmax), cmap="magma" if P.is_dark() else "magma_r")
charts.style_axes(pb, "position on the meridian (degrees)", "time t")
pb.set_xticks([0, 90, 180, 270, 360])
charts.title(pb, "Concentration c(s, t), D = 0.5")
cb = fig.colorbar(im, ax=pb, fraction=0.05, pad=0.02)
cb.ax.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
cb.outline.set_edgecolor(P.muted())

bio.panel(ax, "C", (24.0, 9.9))
cx, cy, R = 28.0, 5.2, 3.0
ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((cx, cy), R, facecolor=P.fill("cytoplasm"),
             edgecolor=P.muted(), lw=0.8, zorder=2))
# phase the final pattern so that its maxima sit at the equator (90 and 270 degrees from the pole)
ang = s - s[int(np.argmax(c))] + np.pi / 2
x = cx + R * np.sin(ang)
y = cy + R * np.cos(ang)
cm = __import__("matplotlib").colormaps["magma" if P.is_dark() else "magma_r"]
cn = (c - c.min()) / (c.max() - c.min() + 1e-12)
for i in range(N):
    j = (i + 1) % N
    ax.plot([x[i], x[j]], [y[i], y[j]], color=cm(0.15 + 0.8 * cn[i]), lw=5, solid_capstyle="round", zorder=4)
bio.label(ax, (cx, cy + R + 0.6), "pole", size="tiny")
bio.label(ax, (cx + R + 0.4, cy), "equator", size="tiny", ha="left")
bio.label(ax, (cx, 1.0), "peaks at the equator: a contractile ring", size="tiny")
