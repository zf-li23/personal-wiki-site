# Gene-regulatory network motifs (SBGN Activity Flow) and the dynamics each one produces.
import numpy as np

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(21, 9.6)


def simulate(f, y0, T, dt=0.005):
    y = np.array(y0, float)
    out = [y.copy()]
    for k in range(int(T / dt)):
        y = y + dt * f(k * dt, y)
        out.append(y.copy())
    return np.arange(len(out)) * dt, np.array(out)


def mini(box, t, curves, shade=(), ylabel=None):
    """A small time-course plot drawn in canvas units: curves are (values, token, name)."""
    x0, y0, w, h = box
    ax.plot([x0, x0 + w], [y0, y0], color=P.muted(), lw=0.8, solid_capstyle="butt", zorder=5)
    ax.plot([x0, x0], [y0, y0 + h], color=P.muted(), lw=0.8, solid_capstyle="butt", zorder=5)
    X = x0 + (t - t[0]) / (t[-1] - t[0]) * w
    for t0, t1, text in shade:
        a, b = x0 + (t0 - t[0]) / (t[-1] - t[0]) * w, x0 + (t1 - t[0]) / (t[-1] - t[0]) * w
        bio.shape(ax, [(a, y0), (b, y0), (b, y0 + h), (a, y0 + h), (a, y0)], P.mix(P.fill("highlight"), P.surface(), 0.6), lw=0, zorder=1)
        bio.label(ax, ((a + b) / 2, y0 + h + 0.18), text, size="tiny", color=P.muted())
    top = max(c[0].max() for c in curves)
    for v, tok, name, frac, dy in curves:
        Y = y0 + v / top * h * 0.92
        ax.plot(X, Y, color=P.edge(tok), lw=1.5, zorder=6, solid_capstyle="round")
        i = min(int(frac * (len(X) - 1)), len(X) - 1)
        bio.label(ax, (X[i] + 0.06, Y[i] + dy), name, size="tiny", ha="left", color=P.edge(tok))
    bio.label(ax, (x0 + w, y0 - 0.22), "time", size="tiny", color=P.muted(), ha="right")
    if ylabel:
        bio.label(ax, (x0 - 0.15, y0 + h / 2), ylabel, size="tiny", color=P.muted(), rotation=90)


tok = [P.protein(i + 1) for i in range(3)]
ytop, ycap = 9.4, 3.55

# A: coherent type-1 feed-forward loop with an AND gate (Mangan & Alon 2003): sign-sensitive delay
bio.panel(ax, "A", (0.2, ytop))
network.motif(ax, "ffl", (2.7, 6.3), size=4.0, gate="AND", inputs={"X": "Sx"})
bio.label(ax, (2.7, ycap), "Coherent FFL (AND gate)", size="small", bold=True)


def ffl(t, y):
    sx = 1.0 if 2 < t < 9 else 0.0
    Y, Z = y
    return np.array([sx - Y, sx * (Y > 0.5) - Z])


t, y = simulate(ffl, [0, 0], 14)
mini((0.9, 0.7, 3.3, 1.9), t, [(y[:, 0], tok[1], "Y", 0.16, 0.12), (y[:, 1], tok[2], "Z", 0.3, -0.5)], shade=[(2, 9, "Sx on")])

# B: negative autoregulation speeds the response (same steady state as simple regulation)
bio.panel(ax, "B", (5.6, ytop))
network.motif(ax, "nar", (7.6, 5.8), size=4.0)
bio.label(ax, (7.6, ycap), "Negative autoregulation", size="small", bold=True)
K, n = 0.3, 2
beta_nar = 1 + (1.0 / K) ** n  # the same steady state X = 1 as simple regulation
t, simple = simulate(lambda t, y: np.array([1.0 - y[0]]), [0], 4)
_, nar = simulate(lambda t, y: np.array([beta_nar / (1 + (y[0] / K) ** n) - y[0]]), [0], 4)
mini((6.1, 0.7, 3.0, 1.9), t, [(simple[:, 0], "neutral", "simple", 0.3, -0.45), (nar[:, 0], tok[0], "NAR", 0.06, 0.2)])

# C: toggle switch (Gardner, Cantor & Collins 2000): IPTG and heat pulses flip a stable state
bio.panel(ax, "C", (10.7, ytop))
network.motif(ax, "toggle", (13.0, 5.8), size=4.2, inputs={"lacI": ("IPTG", "negative"), "cI": ("Heat", "negative")})
bio.label(ax, (13.0, ycap), "Toggle switch", size="small", bold=True)


def toggle(t, y):
    u, v = y  # LacI, CI
    iptg = 25.0 if 4 < t < 9 else 0.0
    heat = 25.0 if 19 < t < 24 else 0.0
    return np.array([8 / (1 + (v / (1 + heat)) ** 2.5) - u, 8 / (1 + (u / (1 + iptg)) ** 2.5) - v])


t, y = simulate(toggle, [7.9, 0.1], 32)
mini((11.2, 0.7, 3.3, 1.9), t, [(y[:, 0], tok[0], "LacI", 0.86, 0.2), (y[:, 1], tok[1], "CI", 0.4, 0.2)], shade=[(4, 9, "IPTG"), (19, 24, "heat")])

# D: repressilator (Elowitz & Leibler 2000, dimensionless model)
bio.panel(ax, "D", (16.3, ytop))
network.motif(ax, "repressilator", (18.3, 6.0), size=3.6)
bio.label(ax, (18.3, ycap), "Repressilator", size="small", bold=True)
a0, a, beta, hill = 0.2, 216.0, 5.0, 2.0


def repress(t, y):
    m, p = y[:3], y[3:]
    rep = p[[2, 0, 1]]  # lacI is repressed by CI, tetR by LacI, cI by TetR
    return np.r_[-m + a / (1 + rep**hill) + a0, -beta * (p - m)]


t, y = simulate(repress, [0, 0, 0, 1.0, 1.5, 2.2], 45, dt=0.01)
keep = t > 15
mini((16.6, 0.7, 3.3, 1.9), t[keep], [(y[keep, 3], tok[0], "", 0, 0), (y[keep, 4], tok[1], "", 0, 0), (y[keep, 5], tok[2], "", 0, 0)])
for k, name in enumerate(("LacI", "TetR", "CI")):
    bio.label(ax, (20.0, 2.4 - 0.35 * k), name, size="tiny", ha="left", color=P.edge(tok[k]))
