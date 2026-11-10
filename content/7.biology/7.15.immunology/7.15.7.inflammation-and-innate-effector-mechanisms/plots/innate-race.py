# The race between a pathogen and innate effector cells (Eq. 7.1 of the page), nondimensional.
#   dB/dt = r B (1 - B/K) - k N B
#   dN/dt = s + a B/(h + B) - delta N - gamma N B
# A: pathogen load for several inocula (normal parameters) and the smallest inoculum under neutropenia.
# B: phase plane with nullclines, the two stable equilibria, the saddle and its stable manifold.
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P = bio.P
R, K, KILL, DELTA, H, GAMMA = 1.0, 1.0, 1.0, 0.2, 0.1, 6.0
NORMAL = dict(s=0.3, a=0.3)
NEUTROPENIA = dict(s=0.15, a=0.15)


def rhs(t, y, s, a):
    B, N = y
    return [R * B * (1 - B / K) - KILL * N * B, s + a * B / (H + B) - DELTA * N - GAMMA * N * B]


def run(b0, pars, t_end=60.0, back=False):
    s, a = pars["s"], pars["a"]
    if back:
        f = lambda t, y: [-v for v in rhs(t, y, s, a)]
    else:
        f = lambda t, y: rhs(t, y, s, a)
    tt = np.linspace(0, t_end, 1500)

    def leave(t, y):
        return min(y[0] + 1e-3, 1.05 - y[0], y[1] + 1e-3, 2.0 - y[1])

    leave.terminal = True
    sol = solve_ivp(f, (0, t_end), b0, t_eval=tt, method="LSODA", rtol=1e-9, atol=1e-14,
                    events=leave if back else None)
    return sol.t, sol.y


fig, ax = bio.canvas(17.0, 7.4)

# --- A  time courses -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.2))
bio.label(ax, (4.6, 7.05), "Pathogen load after different inocula", size="title", bold=True)
pa = quant.Plot(ax, (1.6, 1.3, 6.2, 5.0), xlim=(0, 40), ylim=(1e-6, 2), ylog=True,
                xlabel="time (dimensionless, $1/r$)", ylabel="pathogen load $B/K$", ylabel_offset=1.25,
                xticks=[0, 10, 20, 30, 40], yticks=[(1e-6, "$10^{-6}$"), (1e-4, "$10^{-4}$"), (1e-2, "$10^{-2}$"), (1, "1")])
inocula = [(0.01, "virus"), (0.03, "enzyme"), (0.06, "drug"), (0.2, "bacterium")]
runs = []
for b0, tok in inocula:
    t, y = run([b0, NORMAL["s"] / DELTA], NORMAL, 40)
    B = np.clip(y[0], 1e-7, None)
    pa.line(t, B, tok, lw=1.7)
    runs.append((y, tok))
    txt = "$B_0 = %g$" % b0
    if B[-1] > 1e-3:
        bio.label(ax, (pa.X(40) - 0.05, float(pa.Y(B[-1])) + 0.25), txt, size="tiny", color=quant.line_color(tok), ha="right")
    else:
        level = {0.01: 1e-3, 0.03: 1e-4, 0.06: 1e-5}[b0]
        i = int(np.argmax(B < level))
        bio.label(ax, (pa.X(t[i]) - 0.12, pa.Y(level)), txt, size="tiny", color=quant.line_color(tok), ha="right")
t, y = run([0.01, NEUTROPENIA["s"] / DELTA], NEUTROPENIA, 40)
pa.line(t, np.clip(y[0], 1e-7, None), "virus", lw=1.5, dashed=True)
bio.label(ax, (pa.X(9.5), pa.Y(0.04)), "$B_0 = 0.01$,\nneutropenia", size="tiny", color=quant.line_color("virus"), ha="left")
bio.label(ax, (pa.X(20), pa.Y(3e-6)), "cleared", size="tiny", color=P.muted())
bio.label(ax, (pa.X(28), pa.Y(0.3)), "infection established", size="tiny", color=P.muted())

# --- B  phase plane -------------------------------------------------------------------------------
bio.panel(ax, "B", (9.0, 7.2))
bio.label(ax, (12.9, 7.05), "Phase plane (normal parameters)", size="title", bold=True)
pb = quant.Plot(ax, (10.2, 1.3, 6.2, 5.0), xlim=(0, 1), ylim=(0, 1.8),
                xlabel="pathogen load $B/K$", ylabel="phagocytes $N$",
                xticks=[0, 0.25, 0.5, 0.75, 1], yticks=[0, 0.5, 1.0, 1.5])
s, a = NORMAL["s"], NORMAL["a"]
bb = np.linspace(1e-4, 1, 400)
pb.line(bb, R * (1 - bb / K) / KILL, "bacterium", lw=1.1, dotted=True, text="$\\dot B = 0$", at=0.3, dy=0.25)
pb.line(bb, (s + a * bb / (H + bb)) / (DELTA + GAMMA * bb), "receptor", lw=1.1, dotted=True,
        text="$\\dot N = 0$", at=0.55, dy=0.18)


def g(b):  # intersections of the two nullclines (B > 0)
    return R * (1 - b / K) / KILL - (s + a * b / (H + b)) / (DELTA + GAMMA * b)


roots = []
grid = np.linspace(1e-4, 0.999, 2000)
vals = g(grid)
for i in range(len(grid) - 1):
    if vals[i] * vals[i + 1] < 0:
        roots.append(brentq(g, grid[i], grid[i + 1]))
saddle, infected = roots[0], roots[-1]
# stable manifold of the saddle: integrate backwards from points near it
Bs, Ns = saddle, R * (1 - saddle / K) / KILL
J = np.array([[R * (1 - 2 * Bs / K) - KILL * Ns, -KILL * Bs],
              [a * H / (H + Bs) ** 2 - GAMMA * Ns, -DELTA - GAMMA * Bs]])
w, v = np.linalg.eig(J)
vs = v[:, int(np.argmin(w.real))].real
for sign in (1, -1):
    t_, yb = run([Bs + sign * 1e-4 * vs[0], Ns + sign * 1e-4 * vs[1]], NORMAL, 25, back=True)
    m = (yb[0] > 0) & (yb[0] < 1) & (yb[1] > 0) & (yb[1] < 1.8)
    idx = np.argmin(m) if not m.all() else len(m)
    pb.line(yb[0][:idx], yb[1][:idx], "muted", lw=1.0, dashed=True)
for y, tok in runs:
    m = y[0] >= 0
    pb.line(np.clip(y[0][m], 0, 1), y[1][m], tok, lw=1.3)
pb.points([0], [s / DELTA], "positive", r=0.11)
pb.points([infected], [R * (1 - infected / K) / KILL], "negative", r=0.11)
pb.points([saddle], [Ns], "muted", r=0.09, hollow=True)
bio.label(ax, (pb.X(0.03), pb.Y(1.5) + 0.32), "cleared", size="tiny", color=quant.line_color("positive"), ha="left")
bio.label(ax, (pb.X(infected) + 0.15, pb.Y(R * (1 - infected / K)) - 0.3), "infected", size="tiny",
          color=quant.line_color("negative"), ha="left")
bio.label(ax, (pb.X(saddle) + 0.18, pb.Y(Ns) + 0.1), "saddle", size="tiny", color=P.muted(), ha="left")
