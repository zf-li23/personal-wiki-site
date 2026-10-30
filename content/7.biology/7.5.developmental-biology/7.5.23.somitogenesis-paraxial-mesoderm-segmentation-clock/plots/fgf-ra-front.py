"""The wavefront. (A, B) Steady states of the FGF-RA model F_t = -gF - aAF + DF'', A_t = A(1 - A) - bAF in the frame
of the tail bud (F = F0 at x = 0). (C) Fisher's equation from a step: profiles and the speed of the level 0.5."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
D, g, al, be = 1.0, 1.0, 8.0, 1.0


def steady(F0, L=12.0, dx=0.1, T=25.0):
    x = np.arange(0, L + dx / 2, dx)
    F = F0 * np.exp(-x)
    A = np.full(x.size, 0.5)
    dt = 0.2 * dx * dx / D
    for _ in range(int(T / dt)):
        lap = np.empty_like(F)
        lap[1:-1] = (F[2:] - 2 * F[1:-1] + F[:-2]) / dx ** 2
        lap[-1] = 2 * (F[-2] - F[-1]) / dx ** 2
        lap[0] = 0.0
        F, A = F + dt * (-g * F - al * A * F + D * lap), A + dt * (A * (1 - A) - be * A * F)
        F[0] = F0
        A = np.maximum(A, 1e-9)
    return x, F, A


fig, axs = plt.subplots(1, 4, figsize=(14.0, 3.6), gridspec_kw={"width_ratios": [1.15, 1, 1, 0.75]})
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.17, top=0.86, wspace=0.45)

x, F, A = steady(20.0)
a = axs[0]
a.semilogy(x, F, color=charts.line("drug"), lw=1.8, label="FGF  F")
a.set_ylim(1e-4, 40)
x0 = x[np.argmax(be * F < 1)]
a.axvline(x0, color=P_.muted(), lw=0.8, ls="--")
charts.style_axes(a, "distance from tail bud x", "F (log scale)")
a2 = a.twinx()
a2.plot(x, A, color=charts.line("positive"), lw=1.8)
a2.set_ylim(0, 1.1)
for sp in ("top", "left", "bottom"):
    a2.spines[sp].set_visible(False)
a2.spines["right"].set_color(P_.muted())
a2.tick_params(colors=P_.ink(), labelsize=FT["tiny"])
a2.set_ylabel("retinoic acid A", color=P_.ink(), fontsize=FT["small"])
a.text(0.6, 3.0, "F", color=charts.line("drug"), fontsize=FT["small"])
a.text(8.5, 5, "A", color=charts.line("positive"), fontsize=FT["small"])
charts.title(a, "A  Two zones (F0 = 20)")

b = axs[1]
F0s = np.array([3.0, 6.0, 12.0, 25.0, 50.0, 100.0, 200.0])
fr = []
for f0 in F0s:
    xx, FF, AA = steady(f0)
    fr.append(xx[np.argmax(be * FF < 1)])
b.semilogx(F0s, fr, "o", color=charts.line("drug"), ms=4, label="numerical")
ff = np.logspace(np.log10(2), np.log10(300), 50)
b.semilogx(ff, np.sqrt(D / g) * np.log(be * ff), color=P_.ink(), lw=1.2, label="ln(beta F0)")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "source strength F0", "front position x0")
charts.title(b, "B  Logarithmic position")

c = axs[2]
dx, dt = 0.2, 0.01
X = np.arange(-20, 80, dx)
u = (X < 0).astype(float)
times, pos = [], []
snaps = {5, 10, 15, 20, 25}
for k in range(1, int(26 / dt) + 1):
    lap = (np.roll(u, 1) - 2 * u + np.roll(u, -1)) / dx ** 2
    lap[0] = lap[-1] = 0
    u = u + dt * (u - u * u + lap)
    t = k * dt
    if k % 20 == 0:
        times.append(t)
        pos.append(X[np.argmax(u < 0.5)])
    if abs(t - round(t)) < dt / 2 and round(t) in snaps:
        c.plot(X, u, color=charts.line("dna"), lw=1.2)
        c.text(X[np.argmax(u < 0.5)] + 1, 0.55, "t=%d" % round(t), fontsize=FT["tiny"], color=P_.muted())
c.set_xlim(-5, 60)
charts.style_axes(c, "position X", "a")
charts.title(c, "C  Fisher front from a step")
ins = axs[3]
tt, pp = np.array(times), np.array(pos)
sp = np.gradient(pp, tt)
w = 15
sp = np.convolve(sp, np.ones(w) / w, mode="same")
m = (tt > 2) & (tt < 24)
ins.plot(tt[m], sp[m], color=charts.line("drug"), lw=1.2)
ins.axhline(2, color=P_.muted(), lw=0.8, ls="--")
ins.set_ylim(1.4, 2.1)
charts.style_axes(ins, "time t", "speed of level a = 0.5")
charts.title(ins, "D  Speed")
