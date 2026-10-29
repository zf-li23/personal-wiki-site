"""Condensation of cells by adhesion in a continuum model (one dimension, periodic domain).

Cell density u(x, t) (scaled so that u = 1 is close packing) obeys
    du/dt = D d2u/dx2 - d/dx[ u (1 - u) F ],   F(x) = (alpha / R) int_{-R}^{R} u(x + s) sgn(s) ds,
an adhesive drift towards neighbours within the sensing range R (an "adhesive trap"), limited by
crowding through the factor 1 - u (the bound n_max of the text). D = 1, R = 1, alpha = 12, domain
length 20 R, mean density 0.3 with 1% random perturbations; explicit finite differences
(400 points, dt = 2e-4).
A: kymograph of u(x, t) for 0 <= t <= 25: the uniform state breaks up into aggregates, which then
coarsen slowly. B: profiles at t = 2, 6 and 25. C: linear growth rate of a perturbation exp(ikx),
s(k) = -D k^2 + 2 alpha u0 (1 - u0)(1 - cos kR) / R for alpha = 4 (stable) and 12 (unstable).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(4)
Ld, n, Dc, R, alpha, u0 = 20.0, 400, 1.0, 1.0, 12.0, 0.3
dx = Ld / n
x = np.arange(n) * dx
u = u0 * (1 + 0.01 * rng.standard_normal(n))
m = int(round(R / dx))
kern = np.r_[-np.ones(m), 0.0, np.ones(m)] * dx * alpha / R  # sgn(s) weights, s = -R..R


def force(u):
    up = np.r_[u[-m:], u, u[:m]]
    return np.convolve(up, kern[::-1], mode="valid")


dt = 2e-4
tmax = 25.0
steps = int(tmax / dt)
snaps_t = np.linspace(0, tmax, 126)
kym, prof = [], {}
si = 0
for it in range(steps + 1):
    t = it * dt
    if si < len(snaps_t) and t >= snaps_t[si] - 1e-9:
        kym.append(u.copy())
        si += 1
    for tt in (2.0, 6.0, 25.0):
        if abs(t - tt) < dt / 2:
            prof[tt] = u.copy()
    F = force(u)
    flux_adv = u * (1 - u) * F
    # fluxes at i+1/2
    fa = 0.5 * (flux_adv + np.roll(flux_adv, -1))
    fd = -Dc * (np.roll(u, -1) - u) / dx
    J = fa + fd
    u = u - dt * (J - np.roll(J, 1)) / dx
    u = np.clip(u, 0, 1)

kym = np.array(kym)
fig, ax = bio.canvas(32.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 9.0, 7.2))
im = pa.imshow(kym, aspect="auto", origin="lower", extent=(0, Ld, 0, tmax), cmap="magma" if P.is_dark() else "magma_r",
               vmin=0, vmax=1)
charts.style_axes(pa, "position x / R", "time t")
charts.title(pa, "Cell density u(x, t)")
cb = fig.colorbar(im, ax=pa, fraction=0.05, pad=0.02)
cb.ax.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
cb.outline.set_edgecolor(P.muted())

bio.panel(ax, "B", (12.6, 9.9))
pb = charts.axes_at(ax, (14.2, 1.8, 7.6, 7.2))
for tt, tok in ((2.0, "ectoderm"), (6.0, "highlight"), (25.0, "mesoderm")):
    pb.plot(x, prof[tt], color=quant.line_color(tok), lw=1.8, label=f"t = {tt:g}")
pb.axhline(u0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_xlim(0, Ld)
pb.set_ylim(0, 1.05)
charts.style_axes(pb, "position x / R", "density u")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pb, "Aggregates limited by crowding")

bio.panel(ax, "C", (23.0, 9.9))
pc = charts.axes_at(ax, (24.6, 1.8, 7.0, 7.2))
k = np.linspace(0, 8, 400)
for al, tok in ((4.0, "ectoderm"), (12.0, "mesoderm")):
    s = -Dc * k ** 2 + 2 * al * u0 * (1 - u0) * (1 - np.cos(k * R)) / R
    pc.plot(k, s, color=quant.line_color(tok), lw=1.8, label=f"α = {al:g}")
pc.axhline(0, color=P.muted(), lw=0.8)
pc.set_xlim(0, 8)
pc.set_ylim(-8, 3)
charts.style_axes(pc, "wavenumber k R", "growth rate s")
leg = pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower left")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pc, "Instability of the uniform state")
