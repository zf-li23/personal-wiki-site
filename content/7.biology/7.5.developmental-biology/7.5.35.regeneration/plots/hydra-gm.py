"""The Gierer-Meinhardt model of the Hydra head with a graded source density (Formula 35.2.1).

Model (dimensionless; time in activator lifetimes, length in units of a small polyp, head at x = 0):
a_t = eps2 a_xx + rho(x) (a^2 / h + mu) - a,  tau h_t = D h_xx + a^2 - h,  no-flux ends,
eps2 = 1e-4, D = 0.2 (inhibitor range sqrt(D) = 0.45), tau = 0.5, mu = 0.05. The source density
rho(x) = (1 + 0.1 (1 - x / L)) (1 - 0.3 exp(-(L - x) / 0.1)) falls by 10 % from head to foot and is lowered
near the foot (foot inhibition). rho is a property of the tissue and moves with it when tissue is cut or grafted.
A: steady states of a polyp of length 1 (one head) and of a grown polyp of length 1.5 (a second peak, the bud,
forms about three quarters of the way down). B: after decapitation (tissue x < 0.2 removed) the inhibitor decays
first and a new head appears at the cut within a few activator lifetimes. C: a polyp cut in two: each piece
regenerates a head at the end that faced the old head. D: a small piece of activated tissue (activator at half
the head level) grafted at x = 0.2 is absorbed; grafted at x = 0.8 it forms a second axis; in a decapitated
host a graft at x = 0.3 forms the new head.
"""

import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import splu
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
DX, D, TAU, E2, MU = 0.01, 0.2, 0.5, 1e-4, 0.05


def rho_of(x, L):
    return (1 + 0.1 * (1 - x / L)) * (1 - 0.3 * np.exp(-(L - x) / 0.1))


def run(rho, a, h, T, dt=0.05, snaps=()):
    n = len(a)
    lap = diags([np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)], [-1, 0, 1]).tolil()
    lap[0, 1] = 2
    lap[-1, -2] = 2
    lap = (lap / DX**2).tocsc()
    eye = identity(n, format="csc")
    la = splu((eye - dt * E2 * lap).tocsc())
    lh = splu((eye - dt * D / TAU * lap).tocsc())
    a, h = a.copy(), h.copy()
    out = {}
    steps = int(round(T / dt))
    want = {int(round(s / dt)): s for s in snaps}
    for k in range(steps + 1):
        if k in want:
            out[want[k]] = (a.copy(), h.copy())
        if k == steps:
            break
        f = rho * (a * a / h + MU) - a
        g = (a * a - h) / TAU
        a = la.solve(a + dt * f)
        h = np.maximum(lh.solve(h + dt * g), 1e-6)
    return a, h, out


def grid(L):
    return np.arange(0, L + DX / 2, DX)


fig, ax = bio.canvas(30.0, 19.0)
ca, cb = Q.line_color("protein"), Q.line_color("na")

# A: size and budding
pa = C.axes_at(ax, (1.8, 11.2, 11.0, 6.0))
steady = {}
for L, ls in ((1.0, "-"), (1.5, (0, (4, 2)))):
    x = grid(L)
    a, h, _ = run(rho_of(x, L), np.ones(len(x)), np.ones(len(x)), 1500.0)
    steady[L] = (x, a, h)
    pa.plot(x, a, color=ca if L == 1.0 else Q.line_color("negative"), lw=1.6, ls=ls, label=f"length {L:g}")
pa.set_xlim(0, 1.5)
C.style_axes(pa, "position x (head at 0)", "activator a")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
pa.annotate("head", (0.0, steady[1.0][1][0]), (0.18, 0.9 * steady[1.0][1][0]), color=P.muted(), fontsize=FS["tiny"],
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
xb = steady[1.5][0][np.argmax(steady[1.5][1][50:]) + 50]
pa.annotate("bud", (xb, steady[1.5][1][50:].max()), (xb - 0.3, 0.8 * steady[1.5][1][50:].max()), color=P.muted(),
            fontsize=FS["tiny"], arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
bio.panel(ax, "A", (0.2, 18.7))
bio.label(ax, (1.8, 18.4), "Growth: a second peak (bud) forms", size="small", bold=True, ha="left")

# B: decapitation
x, a, h = steady[1.0]
k = int(round(0.2 / DX))
xs = x[k:]
_, _, snaps = run(rho_of(x, 1.0)[k:], a[k:], h[k:], 40.0, snaps=(0, 2, 4, 6, 10, 40))
pb = C.axes_at(ax, (17.0, 11.2, 11.0, 6.0))
pb.plot(x, a, color=P.muted(), lw=0.9, ls=(0, (2, 2)), label="before the cut")
shades = np.linspace(0.25, 1.0, len(snaps))
for (t, (aa, hh)), s in zip(sorted(snaps.items()), shades):
    pb.plot(xs, aa, color=ca, lw=1.4, alpha=s if s < 1 else None, label=f"t = {t:g}" if t in (0, 6, 40) else None)
pb.axvline(0.2, color=P.muted(), lw=0.8)
pb.text(0.21, 0.95 * a.max(), "cut", color=P.muted(), fontsize=FS["tiny"], va="top")
pb.set_xlim(0, 1.0)
C.style_axes(pb, "position x", "activator a")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.4, 18.7))
bio.label(ax, (17.0, 18.4), "Decapitation: a head regenerates at the cut", size="small", bold=True, ha="left")

# C: cutting in two
pc = C.axes_at(ax, (1.8, 1.6, 11.0, 6.0))
pc.plot(x, a, color=P.muted(), lw=0.9, ls=(0, (2, 2)), label="intact polyp")
r = rho_of(x, 1.0)
for lo, hi, tok in ((0.0, 0.5, "protein"), (0.5, 1.0, "negative")):
    m = (x >= lo - 1e-9) & (x <= hi + 1e-9)
    aa, hh, _ = run(r[m], a[m], h[m], 1000.0)
    pc.plot(x[m], aa, color=Q.line_color(tok), lw=1.6, label=f"piece {lo:g}-{hi:g}")
pc.axvline(0.5, color=P.muted(), lw=0.8)
pc.set_xlim(0, 1.0)
C.style_axes(pc, "original position x", "activator a")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (0.2, 9.1))
bio.label(ax, (1.8, 8.8), "Two pieces: each head forms at the apical end", size="small", bold=True, ha="left")

# D: grafts of activated tissue
pd = C.axes_at(ax, (17.0, 1.6, 11.0, 6.0))
L = 1.2
x2 = grid(L)
r2 = rho_of(x2, L)
a2, h2, _ = run(r2, np.ones(len(x2)), np.ones(len(x2)), 1500.0)
for xg, tok, lab in ((0.2, "protein", "graft at 0.2: absorbed"), (0.8, "negative", "graft at 0.8: second axis")):
    m = (x2 >= xg) & (x2 < xg + 0.06)
    ag = a2.copy()
    ag[m] = 0.5 * a2.max()
    aa, _, _ = run(r2, ag, h2, 1200.0)
    pd.plot(x2, aa, color=Q.line_color(tok), lw=1.6, label=lab)
    pd.plot([xg + 0.03], [0.05 * a2.max()], marker="v", ms=5, color=Q.line_color(tok))
k = 10
m = (x2[k:] >= 0.3) & (x2[k:] < 0.36)
ag = a2[k:].copy()
ag[m] = 0.5 * a2.max()
aa, _, _ = run(r2[k:], ag, h2[k:], 1200.0)
pd.plot(x2[k:], aa, color=Q.line_color("positive"), lw=1.4, ls=(0, (4, 2)), label="decapitated host, graft at 0.3")
pd.set_xlim(0, L)
C.style_axes(pd, "position x (host length 1.2)", "activator a")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center")
bio.panel(ax, "D", (15.4, 9.1))
bio.label(ax, (17.0, 8.8), "Grafts: inhibited near the head, not far away", size="small", bold=True, ha="left")
