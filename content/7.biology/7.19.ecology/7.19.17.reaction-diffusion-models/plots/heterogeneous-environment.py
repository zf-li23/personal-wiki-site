"""A single species in a heterogeneous environment: u_t = d u_xx + u (m(x) - u) on (0, 1), zero flux.

Steady states theta_d are computed by finite volumes (N = 400 cells) and Newton's method, continuing
from small to large d.
A: resource m(x) = 2 + sin(2 pi x) (dashed) and steady states for d = 0.001, 0.05 and 1: slow dispersers
match the resource (theta ~ m, an ideal free distribution), fast dispersers are nearly uniform.
B: total biomass (integral of theta_d) against d: it exceeds the total resource, 2, for every d, peaks
near d = 0.15 and returns to 2 in both limits.
C: a resource that is negative on average, m(x) = -0.2 + cos(2 pi x): the principal eigenvalue
lambda_1(d) of d u'' + m u (line) decreases from max m = 0.8 to mean m = -0.2, so the species persists
only for d < d* (points: total biomass of the steady state).
"""

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import eigsh

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

N = 400
h = 1.0 / N
x = (np.arange(N) + 0.5) * h
main = -2 * np.ones(N)
main[0] = main[-1] = -1
Lap = diags([np.ones(N - 1), main, np.ones(N - 1)], [-1, 0, 1]) / h**2


def steady(d, m, th):
    th = th.copy()
    for _ in range(100):
        F = d * (Lap @ th) + th * (m - th)
        J = d * Lap + diags(m - 2 * th)
        step = spsolve(J.tocsc(), -F)
        th += step
        if np.max(np.abs(step)) < 1e-11:
            break
    return th


m = 2 + np.sin(2 * np.pi * x)
ds = np.logspace(-3, 2, 81)
bm, profiles = [], {}
th = m.copy()
for d in ds:
    th = steady(d, m, th)
    bm.append(th.sum() * h)

th = m.copy()
for dd in (0.001, 0.05, 1.0):
    th = steady(dd, m, th)
    profiles[dd] = th.copy()

pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
pa.plot(x, m, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="resource m(x)")
for dd, tok in [(0.001, "dna"), (0.05, "enzyme"), (1.0, "negative")]:
    pa.plot(x, profiles[dd], color=Q.line_color(tok), lw=1.5, label=f"d = {dd:g}")
pa.set_xlim(0, 1)
pa.set_ylim(0.8, 3.2)
C.style_axes(pa, "position x", "density")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Steady states", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pb.semilogx(ds, bm, color=Q.line_color("dna"), lw=1.7)
pb.axhline(2.0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
k = int(np.argmax(bm))
pb.plot(ds[k], bm[k], "o", ms=4.5, color=Q.line_color("negative"))
pb.text(ds[k] * 1.3, bm[k], f"max {bm[k]:.3f} at d = {ds[k]:.2f}", fontsize=FS["tiny"], color=P.ink(), va="bottom")
pb.text(2e-3, 2.002, "total resource = 2", fontsize=FS["tiny"], color=P.ink(), va="bottom")
pb.set_xlim(1e-3, 1e2)
pb.set_ylim(1.995, 2.06)
C.style_axes(pb, "diffusion rate d", "total biomass")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Biomass exceeds resources", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
m2 = -0.2 + np.cos(2 * np.pi * x)
ds2 = np.logspace(-3, 1, 60)
lam = [eigsh((d * Lap + diags(m2)).tocsc(), k=1, sigma=1.0, which="LM", return_eigenvectors=False)[0] for d in ds2]
pc.semilogx(ds2, lam, color=Q.line_color("protein"), lw=1.7, label="principal eigenvalue")
pc.axhline(0, color=P.muted(), lw=0.7)
th = np.clip(m2, 0.01, None)
bms = []
for d in ds2:
    th = steady(d, m2, np.maximum(th, 1e-3))
    bms.append(th.sum() * h if th.max() > 1e-6 else 0.0)
pc.semilogx(ds2[::4], np.array(bms)[::4], "o", ms=3.5, color=Q.line_color("enzyme"), label="total biomass")
dstar = ds2[np.argmin(np.abs(lam))]
pc.axvline(dstar, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(dstar * 1.2, 0.6, f"d* = {dstar:.3f}", fontsize=FS["tiny"], color=P.ink())
pc.set_xlim(1e-3, 10)
pc.set_ylim(-0.25, 0.85)
C.style_axes(pc, "diffusion rate d", "lambda_1 or biomass")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Poor habitat on average", size="small", bold=True, ha="left")
