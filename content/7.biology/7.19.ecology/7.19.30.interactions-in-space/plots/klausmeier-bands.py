"""Vegetation bands on a slope: the Klausmeier (1999) model in dimensionless form.

w_t = a - w - w n^2 + nu w_x  (water: rainfall a, evaporation, uptake, downhill flow toward -x),
n_t = w n^2 - m n + n_xx      (plant biomass: growth on water, mortality, spread),
with m = 0.45 and nu = 182.5 (Klausmeier's values for grasses); uphill is +x.
A: uniform equilibria: bare soil n = 0 (stable for all a), and for a > 2m the vegetated states
n_pm = (a pm sqrt(a^2 - 4 m^2)) / (2m); the lower branch is a saddle, the upper branch is stable to
uniform perturbations but, for a below about 3.3 (shaded), unstable to perturbations of finite wavelength,
computed from the dispersion relation.
B: space-time plot of n for a = 1.2 on a periodic slope of length 200 (512 Fourier modes, Crank-Nicolson
for the linear terms, dt = 0.005), started from the uniform state with 5 % noise; shown from t = 300 to
400: four bands that migrate steadily uphill.
C: plant biomass n and water w along the slope at t = 400: water accumulates as it flows downhill across
the bare ground and is taken up at the uphill edge of the next band, where the plants grow; they die
back at the downhill edge, so the bands move uphill.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
m, nu = 0.45, 182.5


def growth(a, ks):
    n = (a + np.sqrt(a * a - 4 * m * m)) / (2 * m)
    g = []
    for k in ks:
        M = np.array([[-1 - n * n + 1j * nu * k, -2 * m], [n * n, m - k * k]])
        g.append(np.linalg.eigvals(M).real.max())
    return max(g)


fig, ax = bio.canvas(33.0, 11.0)
pa = C.axes_at(ax, (2.0, 1.7, 8.0, 7.6))
aa = np.linspace(2 * m, 4.0, 300)
up = (aa + np.sqrt(aa**2 - 4 * m * m)) / (2 * m)
lo = (aa - np.sqrt(aa**2 - 4 * m * m)) / (2 * m)
ks = np.linspace(0.005, 2.0, 300)
agrid = np.linspace(2 * m + 1e-3, 4.0, 80)
unst = np.array([growth(a, ks) > 0 for a in agrid])
amax = agrid[unst].max()
pa.axvspan(2 * m, amax, color=P.mix(P.fill("highlight"), P.surface(), 0.4), lw=0)
pa.plot(aa, up, color=Q.line_color("plant"), lw=1.8, label="vegetated, n+")
pa.plot(aa, lo, color=Q.line_color("plant"), lw=1.4, ls=(0, (4, 2)), label="saddle, n−")
pa.plot([0, 4], [0, 0], color=P.ink(), lw=1.8, label="bare soil")
pa.text(1.2, 6.8, "patterns\n(bands)", fontsize=FS["tiny"], color=P.ink())
pa.text(amax + 0.05, 1.0, f"a = {amax:.1f}", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 4)
pa.set_ylim(-0.3, 9)
C.style_axes(pa, "rainfall a", "uniform plant biomass n")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Uniform states and pattern range", size="small", bold=True, ha="left")

a, L, N, dt, T = 1.2, 200.0, 512, 0.005, 400.0
x = np.linspace(0, L, N, endpoint=False)
k = 2 * np.pi * np.fft.fftfreq(N, d=L / N)
n0 = (a + np.sqrt(a * a - 4 * m * m)) / (2 * m)
rng = np.random.default_rng(0)
n = n0 * (1 + 0.05 * rng.standard_normal(N))
w = (m / n0) * np.ones(N)
Lw = -1 + 1j * nu * k
Ln = -m - k**2
Ew, Fw = (1 + dt / 2 * Lw) / (1 - dt / 2 * Lw), dt / (1 - dt / 2 * Lw)
En, Fn = (1 + dt / 2 * Ln) / (1 - dt / 2 * Ln), dt / (1 - dt / 2 * Ln)
rec, every = [], int(1.0 / dt)
for s in range(int(T / dt)):
    wn2 = w * n * n
    w = np.fft.ifft(Ew * np.fft.fft(w) + Fw * np.fft.fft(a - wn2)).real
    n = np.fft.ifft(En * np.fft.fft(n) + Fn * np.fft.fft(wn2)).real
    if s * dt >= 300 and s % every == 0:
        rec.append(n.copy())
rec = np.array(rec)
cmap = LinearSegmentedColormap.from_list("veg", [P.surface(), P.fill("plant"), P.edge("plant")])
pb = C.axes_at(ax, (13.0, 1.7, 8.0, 7.6))
pb.imshow(rec, cmap=cmap, origin="lower", aspect="auto", extent=[0, L, 300, 400], interpolation="bilinear")
C.style_axes(pb, "position x (uphill to the right)", "time t", box=True)
bio.panel(ax, "B", (11.3, 10.7))
bio.label(ax, (13.0, 10.0), "Bands migrating uphill (a = 1.2)", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (24.0, 1.7, 8.0, 7.6))
pc.plot(x, n, color=Q.line_color("plant"), lw=1.6, label="plants n")
pc2 = pc.twinx()
pc2.plot(x, w, color=Q.line_color("dna"), lw=1.4, label="water w")
pc.set_xlim(0, L)
C.style_axes(pc, "position x (uphill to the right)", "plant biomass n")
C.style_axes(pc2, None, "water w")
pc2.spines["right"].set_visible(True)
pc2.spines["right"].set_color(P.muted())
h1, l1 = pc.get_legend_handles_labels()
h2, l2 = pc2.get_legend_handles_labels()
pc.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (22.3, 10.7))
bio.label(ax, (24.0, 10.0), "Profile at t = 400", size="small", bold=True, ha="left")
