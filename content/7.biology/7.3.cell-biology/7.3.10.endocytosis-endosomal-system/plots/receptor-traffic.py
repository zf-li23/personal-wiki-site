"""Kinetic model of receptor traffic (Wiley-Cunningham type), rate constants per minute.
Surface receptors S are delivered at V_s, internalized with k_e and return with k_r; internal receptors
are degraded with k_h. Ligand binding (occupied fraction theta, assumed fast) switches a receptor to the
rate constants of the occupied state (EGFR-like: k_e* = 0.15, k_r* = 0.05, k_h* = 0.02 min^-1).
(A) Surface receptors after addition of ligand at t = 0: EGFR at saturating and half-saturating ligand,
and the transferrin receptor, which cycles constitutively and is not down-regulated.
(B) Total receptor number for the same cases.
(C) Steady-state surface fraction f_s = 1/(1 + k_e/(k_r + k_h)) with the positions of the receptors used
in the text (GLUT4: k_e = 0.1, exocytosis 0.01 basal and 0.1 with insulin)."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

# unoccupied EGFR-like receptor, occupied receptor, transferrin receptor
ke, kr, kh = 0.03, 0.10, 0.004
ke2, kr2, kh2 = 0.15, 0.05, 0.02
tf = dict(ke=0.20, kr=0.10, kh=0.0005)


def egfr(theta):
    s0 = 1.0
    ri0 = ke / (kr + kh) * s0
    vs = kh * ri0

    def f(t, y):
        s, ri, ci = y
        th = theta if t >= 0 else 0.0
        return [vs - ((1 - th) * ke + th * ke2) * s + kr * ri + kr2 * ci,
                (1 - th) * ke * s - (kr + kh) * ri,
                th * ke2 * s - (kr2 + kh2) * ci]

    t = np.linspace(0, 240, 600)
    sol = solve_ivp(f, (0, 240), [s0, ri0, 0.0], t_eval=t, rtol=1e-8)
    return t, sol.y[0], sol.y.sum(axis=0) / (s0 + ri0)


fig, ax = bio.canvas(22.0, 7.6)
T = np.linspace(0, 240, 600)

bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.4, 5.6))
for theta, tok, ls, name in ((1.0, "negative", "-", "EGFR, saturating EGF"), (0.5, "drug", "--", "EGFR, θ = 0.5")):
    t, s, tot = egfr(theta)
    a.plot(t, s, color=charts.line(tok), lw=1.8, ls=ls, label=name)
a.plot(T, np.ones_like(T), color=charts.line("channel"), lw=1.8, label="TfR with transferrin")
a.set_xlim(0, 240)
a.set_ylim(0, 1.15)
a.set_xticks([0, 60, 120, 180, 240])
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "t / min", "surface receptors (relative)")

bio.panel(ax, "B", (7.8, 7.5))
b = charts.axes_at(ax, (9.4, 1.3, 5.0, 5.6))
for theta, tok, ls in ((1.0, "negative", "-"), (0.5, "drug", "--")):
    t, s, tot = egfr(theta)
    b.plot(t, tot, color=charts.line(tok), lw=1.8, ls=ls)
b.plot(T, np.ones_like(T), color=charts.line("channel"), lw=1.8)
b.set_xlim(0, 240)
b.set_ylim(0, 1.15)
b.set_xticks([0, 60, 120, 180, 240])
charts.style_axes(b, "t / min", "total receptors (relative)")

bio.panel(ax, "C", (15.1, 7.5))
c = charts.axes_at(ax, (16.6, 1.3, 5.0, 5.6))
x = np.logspace(-2, 2, 200)
c.plot(x, 1 / (1 + x), color=charts.line("neutral"), lw=1.6)
pts = [("TfR", tf["ke"] / (tf["kr"] + tf["kh"]), "channel"),
       ("EGFR", ke / (kr + kh), "positive"),
       ("EGFR + EGF", ke2 / (kr2 + kh2), "negative"),
       ("GLUT4 basal", 0.1 / 0.01, "metabolite"),
       ("GLUT4 + insulin", 0.1 / 0.1, "atp")]
offs = {"TfR": (0.75, -0.07), "EGFR": (1.5, 0.02), "EGFR + EGF": (1.4, 0.03), "GLUT4 basal": (1.4, 0.04),
        "GLUT4 + insulin": (1.4, 0.03)}
for name, xx, tok in pts:
    yy = 1 / (1 + xx)
    c.plot([xx], [yy], "o", color=charts.line(tok), ms=5.5)
    dx, dy = offs[name]
    c.text(xx * dx, yy + dy, name, fontsize=FT["tiny"], color=P.ink(), ha="left" if dx > 1 else "right", va="bottom")
c.set_xscale("log")
c.set_xlim(0.01, 100)
c.set_ylim(0, 1.05)
charts.style_axes(c, r"$k_\mathrm{e}/(k_\mathrm{r}+k_\mathrm{h})$", r"surface fraction $f_\mathrm{s}$")
