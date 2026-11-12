# The timing of sex in a monogonont rotifer: number of resting eggs produced by the end of the season as a
# function of the critical density for mixis N_c, in the model of Eq. (12.1) (same illustrative parameters as
# cyclical-parthenogenesis.py), for ponds that dry up after 10, 15, 30 or 60 days. Each curve is scaled to its
# own maximum (dot). Schematic model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
r, Fh, a, d, mmax, h, c = 0.8, 0.3, 0.002, 0.15, 0.6, 4.0, 1.0
SEASONS = (10, 15, 30, 60)
TOKENS = ("negative", "enzyme", "dna", "protein")


def eggs(Nc, dt=0.04):
    def f(y):
        A, M, F, E = y
        N = A + M
        b = r * F / (F + Fh)
        m = mmax * N ** h / (N ** h + Nc ** h)
        return np.array([b * A * (1 - m) - d * A, b * A * m - d * M, -a * N * F, c * M])
    y = np.array([1.0, 0.0, 1.0, 0.0])
    out, t = {}, 0.0
    for T in SEASONS:
        while t < T - 1e-9:
            k1 = f(y); k2 = f(y + dt / 2 * k1); k3 = f(y + dt / 2 * k2); k4 = f(y + dt * k3)
            y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            t += dt
        out[T] = y[3]
    return out


Ncs = np.logspace(0, 3, 37)
res = [eggs(n) for n in Ncs]
fig, ax = bio.canvas(16, 9.6)
p = quant.Plot(ax, (2.0, 1.5, 10.6, 7.2), xlim=(1, 1000), ylim=(0, 1.05), xlog=True,
               xlabel="Critical density for mixis $N_{\\mathrm{c}}$ / females per mL",
               ylabel="Resting eggs at end of season (relative)", xticks=[1, 10, 100, 1000], yticks=[0, 0.25, 0.5, 0.75, 1])
for T, tok in zip(SEASONS, TOKENS):
    E = np.array([rr[T] for rr in res])
    p.line(Ncs, E / E.max(), token=tok, lw=1.8)
    i = int(np.argmax(E))
    p.points([Ncs[i]], [1.0], token=tok, r=0.1)
    bio.label(ax, (p.X(1000) + 0.15, p.Y(E[-1] / E.max()) + 0.25 * SEASONS.index(T)), f"{T} days", size="tiny", ha="left",
              color=quant.line_color(tok))
p.text(1.3, 0.12, "sex too early: little asexual growth", size="tiny", ha="left", color=P.muted())
p.text(700, 0.5, "threshold never reached", size="tiny", ha="right", color=P.muted())
