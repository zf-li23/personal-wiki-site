"""Advection toward better habitat and competition (Cantrell, Cosner and Lou 2006).

u_t = (d u_x - alpha u m_x)_x + u (m - u - v),   v_t = d v_xx + v (m - u - v),   zero-flux ends on (0, 1).
Both species have the same diffusion rate d = 0.1 and the same resource m(x) = 1 + 0.9 sin(pi x); only u
also moves up the resource gradient with advection rate alpha. Finite volumes (100 cells, upwind
advection), implicit transport and explicit reaction, dt = 0.02, run to t = 1500 from u = v = 0.5.
A: final densities for alpha = 0.05: the advecting species excludes the random disperser.
B: alpha = 2: u is concentrated near the resource peak and v persists on the flanks: coexistence.
C: mean densities at t = 1500 against alpha: exclusion of v for small alpha (up to about 0.07), then
coexistence, with u declining as alpha grows.
"""

import numpy as np
from scipy.sparse import identity, lil_matrix
from scipy.sparse.linalg import splu

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
N = 100
h = 1.0 / N
x = (np.arange(N) + 0.5) * h
xf = np.arange(1, N) * h
m = 1 + 0.9 * np.sin(np.pi * x)
mxf = 0.9 * np.pi * np.cos(np.pi * xf)
d = 0.1


def op(alpha):
    A = lil_matrix((N, N))
    ci = d / h**2
    for k in range(N - 1):
        i, j = k, k + 1
        vel = alpha * mxf[k]
        A[i, i] -= ci
        A[i, j] += ci
        A[j, j] -= ci
        A[j, i] += ci
        if vel > 0:
            A[i, i] -= vel / h
            A[j, i] += vel / h
        else:
            A[i, j] += -vel / h
            A[j, j] -= -vel / h
    return A.tocsc()


def run(alpha, T=1500.0, dt=0.02):
    I = identity(N, format="csc")
    lu = splu(I - dt * op(alpha))
    lv = splu(I - dt * op(0.0))
    u = 0.5 * np.ones(N)
    v = 0.5 * np.ones(N)
    for _ in range(int(T / dt)):
        g = m - u - v
        u, v = lu.solve(u + dt * u * g), lv.solve(v + dt * v * g)
    return u, v


fig, ax = bio.canvas(33.0, 11.0)
cu, cv = Q.line_color("dna"), Q.line_color("negative")
for k, (alpha, letter, title) in enumerate(((0.05, "A", "Weak advection, alpha = 0.05: v excluded"),
                                            (2.0, "B", "Strong advection, alpha = 2: coexistence"))):
    u, v = run(alpha)
    x0 = 2.0 + 11.0 * k
    pa = C.axes_at(ax, (x0, 1.7, 8.0, 7.6))
    pa.plot(x, m, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="resource m(x)")
    pa.plot(x, u, color=cu, lw=1.8, label="u: diffusion + advection")
    pa.plot(x, v, color=cv, lw=1.8, label="v: diffusion only")
    pa.set_xlim(0, 1)
    pa.set_ylim(0, 2.2)
    C.style_axes(pa, "position x", "density at t = 1500")
    pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
    bio.panel(ax, letter, (x0 - 1.7, 10.7))
    bio.label(ax, (x0, 10.0), title, size="small", bold=True, ha="left")

alphas = np.array([0.01, 0.03, 0.05, 0.08, 0.12, 0.2, 0.35, 0.6, 1.0, 2.0, 4.0, 8.0])
res = np.array([[w.mean() for w in run(a)] for a in alphas])
pc = C.axes_at(ax, (24.0, 1.7, 8.0, 7.6))
pc.semilogx(alphas, res[:, 0], "o-", color=cu, lw=1.6, ms=4, label="u (advecting)")
pc.semilogx(alphas, res[:, 1], "s-", color=cv, lw=1.6, ms=4, label="v (random)")
pc.set_ylim(0, 1.8)
C.style_axes(pc, "advection rate alpha", "mean density")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "C", (22.3, 10.7))
bio.label(ax, (24.0, 10.0), "Outcome against advection rate", size="small", bold=True, ha="left")
