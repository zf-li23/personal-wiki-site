"""Diffusion to capture. A: steady-state concentration c(r)/c0 = 1 - a/r around a perfectly
absorbing sphere of radius a (cross-section through the centre); the flux into the sphere is
J = 4 pi D a c0. B: probability that a molecule released at distance r0 is captured before it
wanders beyond R = 50a: walk-on-spheres Monte Carlo (dots, 4000 molecules per point) against the
exact (1/r0 - 1/R)/(1/a - 1/R), close to a/r0. C: largest radius of a spherical cell that can be
supplied with oxygen by diffusion alone, R_max = sqrt(3 D c0 / q), for D = 2000 um^2/s and
c0 = 0.25 mM (air-saturated water) or 0.13 mM (arterial plasma), against the volumetric
consumption rate q; marked: an aerobically growing bacterium (about 1 mM/s) and brain tissue
(about 0.03 mM/s)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(6)

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.4, left=0.06, right=0.97, bottom=0.17, top=0.88)

ax = axs[0]
g = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(g, g)
R = np.hypot(X, Y)
C = np.where(R > 1, 1 - 1 / np.maximum(R, 1e-9), np.nan)
im = ax.imshow(C, extent=(-5, 5, -5, 5), origin="lower", cmap="Blues", vmin=0, vmax=1)
cs = ax.contour(X, Y, np.where(R > 1, C, np.nan), levels=(0.25, 0.5, 0.75, 0.9), colors=P.ink(), linewidths=0.6)
ax.clabel(cs, fontsize=bio.core.FONT["tiny"], fmt="%.2f")
t = np.linspace(0, 2 * np.pi, 200)
ax.fill(np.cos(t), np.sin(t), color=P.fill("bacterium"), ec=P.edge("bacterium"), lw=1)
for ang in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    ax.annotate("", (1.15 * np.cos(ang), 1.15 * np.sin(ang)), (2.3 * np.cos(ang), 2.3 * np.sin(ang)),
                arrowprops=dict(arrowstyle="-|>", color=P.edge("blood"), lw=0.9))
ax.set_aspect("equal")
charts.style_axes(ax, "x / a", "y / a")
cb = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.03)
cb.ax.tick_params(labelsize=bio.core.FONT["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.outline.set_edgecolor(P.muted())
cb.set_label(r"$c/c_0$", fontsize=bio.core.FONT["small"], color=P.ink())
charts.title(ax, r"A  $c = c_0(1 - a/r)$")

ax = axs[1]
a, Rout, eps = 1.0, 50.0, 1e-3
r0s = np.array([1.2, 1.5, 2, 3, 5, 8, 12, 20, 30])
pc = []
for r0 in r0s:
    m = 4000
    p = np.tile([r0, 0.0, 0.0], (m, 1))
    state = np.zeros(m, int)  # 0 walking, 1 captured, 2 escaped
    while (state == 0).any():
        w = state == 0
        r = np.linalg.norm(p[w], axis=1)
        step = np.minimum(r - a, Rout - r)
        v = rng.normal(size=(w.sum(), 3))
        v /= np.linalg.norm(v, axis=1)[:, None]
        p[w] = p[w] + step[:, None] * v
        r = np.linalg.norm(p[w], axis=1)
        idx = np.where(w)[0]
        state[idx[r - a < eps]] = 1
        state[idx[Rout - r < eps]] = 2
    pc.append((state == 1).mean())
rr = np.linspace(1, 40, 300)
ax.plot(rr, (1 / rr - 1 / Rout) / (1 / a - 1 / Rout), color=charts.line("bacterium"), lw=1.6, label="exact, R = 50a")
ax.plot(rr, a / rr, color=P.muted(), lw=1.0, ls="--", label=r"$a/r_0$ ($R \to \infty$)")
ax.plot(r0s, pc, "o", color=charts.line("blood"), ms=4, label="walk on spheres")
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"release distance $r_0/a$", "capture probability")
charts.title(ax, "B  Return is likely but not certain")

ax = axs[2]
q = np.logspace(-3, 1, 200)  # mM/s
D = 2000.0  # um^2/s
for c0, tok, lab in ((0.25, "dna", r"$c_0 = 0.25$ mM"), (0.13, "blood", r"$c_0 = 0.13$ mM")):
    ax.plot(q, np.sqrt(3 * D * c0 / q), color=charts.line(tok), lw=1.7, label=lab)
for qq, txt in ((1.0, "bacterium"), (0.03, "brain tissue")):
    ax.axvline(qq, color=P.muted(), lw=0.5, ls=":")
    ax.text(qq * 1.1, 2.2e3, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), rotation=90, va="top")
ax.axhline(1.0, color=P.muted(), lw=0.5)
ax.text(1.2e-3, 1.15, r"$E.\ coli$ radius", fontsize=bio.core.FONT["tiny"], color=P.ink(), style="italic")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(0.5, 3e3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"$\mathrm{O_2}$ consumption $q$ / (mM s$^{-1}$)", r"$R_{\max}$ / $\mu$m")
charts.title(ax, r"C  $R_{\max} = \sqrt{3Dc_0/q}$")
