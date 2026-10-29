# Self-enhancement and lateral inhibition (SALI) of Nodal and Lefty in the lateral plate mesoderm (Formula 17.4.2;
# after Nakamura and colleagues, 2006). A line of tissue from the right (x = -1) to the left (x = +1) lateral plate,
# with the midline at x = 0, where Lefty1 is produced constitutively (the midline barrier). Nodal induces itself and
# Lefty; Lefty diffuses faster and inhibits Nodal. A transient input from the node during t < 2 is 10 % stronger on
# the left. A: steady Nodal: the small bias is amplified into all-or-none expression on the left. B: without the
# midline barrier, Nodal spreads across and is expressed on both sides (as in Lefty1 mutants). C: a symmetric input
# gives a symmetric outcome (both sides or neither), so an initial bias is required.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N = 161
x = np.linspace(-1, 1, N)
dx = x[1] - x[0]


def lapmat():
    A = np.zeros((N, N))
    for i in range(N):
        A[i, i] = -2
        if i > 0:
            A[i, i - 1] = 1
        if i < N - 1:
            A[i, i + 1] = 1
    A[0, 1] = 2
    A[-1, -2] = 2
    return A / dx ** 2


Lp, I = lapmat(), np.eye(N)


def run(bias=1.1, barrier=True, T=40.0, dt=0.02):
    DN, DL = 0.002, 0.05
    AN = np.linalg.inv(I - dt * DN * Lp)
    AL = np.linalg.inv(I - dt * DL * Lp)
    n = np.zeros(N)
    l = np.zeros(N)
    lpm = (np.abs(x) > 0.15).astype(float)
    mid = (np.abs(x) < 0.05).astype(float)
    inp = np.where(x > 0, bias, 1.0) * np.exp(-((np.abs(x) - 0.2) / 0.08) ** 2)
    for k in range(int(T / dt)):
        t = k * dt
        s = n ** 2 / (0.25 + n ** 2) / (1 + (l / 0.3) ** 2)
        drive = 0.6 * inp if t < 2 else 0.0
        n = AN @ (n + dt * (lpm * (2.0 * s + drive) - n))
        l = AL @ (l + dt * (1.0 * lpm * s + (0.8 * mid if barrier else 0.0) - 0.5 * l))
    return n, l


fig, ax = bio.canvas(22.0, 7.6)
cases = [("A", "left bias 10 %, midline barrier", dict()), ("B", "left bias 10 %, no barrier", dict(barrier=False)),
         ("C", "no bias, midline barrier", dict(bias=1.0))]
for k, (letter, title, kw) in enumerate(cases):
    n, l = run(**kw)
    pa = C.axes_at(ax, (1.4 + k * 7.2, 1.4, 6.0, 4.6))
    pa.axvspan(-0.05, 0.05, color=P.fill("neutral"), alpha=0.4, lw=0)
    pa.plot(x, n, color=C.line("receptor"), lw=2.0, label="Nodal")
    pa.plot(x, l, color=C.line("metabolite"), lw=1.4, ls=(0, (4, 2)), label="Lefty")
    pa.set_xlim(-1, 1)
    pa.set_ylim(0, 2.3)
    pa.set_xticks([-1, 0, 1])
    pa.set_xticklabels(["right", "midline", "left"])
    C.style_axes(pa, None, "level" if k == 0 else None)
    if k == 0:
        pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
    bio.panel(ax, letter, (0.3 + k * 7.2, 7.4))
    bio.label(ax, (1.4 + k * 7.2, 6.6), title, size="small", bold=True, ha="left")
