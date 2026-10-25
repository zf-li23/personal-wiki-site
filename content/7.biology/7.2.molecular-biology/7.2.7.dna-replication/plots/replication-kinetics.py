# Two quantitative models of replication timing.
# A: Cooper-Helmstetter gene dosage in E. coli: copies of a locus at relative position m (0 = oriC,
#    1 = ter) relative to the terminus, 2^(C(1-m)/tau), for C = 40 min and three doubling times.
# B, C: stochastic origin firing on a 10 Mb segment: origins fire at random positions and times with a
#    constant rate I per unreplicated kb per minute, forks move at v; the replicated fraction is compared
#    with the Kolmogorov-Johnson-Mehl-Avrami result f(t) = 1 - exp(-I v t^2).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(22, 8.4)
rng = np.random.default_rng(0)

# ---------------------------------------------------------------- A
a = C.axes_at(ax, (1.6, 1.5, 5.0, 5.6))
Cp = 40.0
s = np.linspace(-1, 1, 401)           # -1 = ter (left replichore), 0 = oriC, +1 = ter (right)
m = np.abs(s)
for tau, tok, ls in ((20, "dna", "-"), (40, "enzyme", "--"), (100, "protein", ":")):
    a.plot(s, 2 ** (Cp * (1 - m) / tau), color=C.line(tok), lw=1.8, ls=ls, label=f"τ = {tau} min")
a.set_xticks([-1, -0.5, 0, 0.5, 1], ["ter", "", "oriC", "", "ter"])
a.set_xlim(-1, 1)
a.set_ylim(0.8, 4.4)
a.set_yticks([1, 2, 3, 4])
C.style_axes(a, "Position on the chromosome", "Copies per terminus")
leg = a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="upper right", labelcolor=P.ink())
bio.panel(ax, "A", (0.4, 7.9))
bio.label(ax, (1.0, 7.9), "Multifork replication (C = 40 min)", size="normal", bold=True, ha="left")

# ---------------------------------------------------------------- B, C: simulation
L, dxk = 10_000, 1.0      # kb, 1 kb bins
v, I = 1.5, 1.5e-5        # kb per min, per kb per min
dt, T = 1.0, 720.0
x = np.arange(L) * dxk + 0.5
origins = []              # (position, time)
times = np.arange(0, T + dt, dt)
frac = []
repl_time = np.full(L, np.inf)
for t in times:
    unrep = repl_time > t
    # new initiations in unreplicated bins during [t, t + dt)
    hits = np.where(unrep & (rng.random(L) < I * dxk * dt))[0]
    for h in hits:
        t0 = t + rng.random() * dt
        x0 = x[h] + (rng.random() - 0.5) * dxk
        origins.append((x0, t0))
        repl_time = np.minimum(repl_time, t0 + np.abs(x - x0) / v)
    frac.append(np.mean(repl_time <= t))
frac = np.array(frac)
origins = np.array(origins)

b = C.axes_at(ax, (8.6, 1.5, 5.6, 5.6))
# shade replicated region in the (x, t) plane
tgrid = np.arange(0, T + 1, 4.0)
img = (repl_time[None, :] <= tgrid[:, None]).astype(float)
b.imshow(img, extent=(0, L / 1000, T / 60, 0), aspect="auto", cmap=__import__("matplotlib.colors", fromlist=["x"]).ListedColormap(
    [P.surface(), P.fill("dna")]), interpolation="nearest")
b.plot(origins[:, 0] / 1000, origins[:, 1] / 60, "o", ms=2.6, color=P.edge("highlight"), mec=P.edge("highlight"))
b.set_xlim(0, L / 1000)
b.set_ylim(T / 60, 0)
b.set_yticks([0, 3, 6, 9, 12])
C.style_axes(b, "Position / Mb", "Time in S phase / h")
bio.panel(ax, "B", (7.5, 7.9))
bio.label(ax, (8.1, 7.9), f"Random origin firing ({len(origins)} origins)", size="normal", bold=True, ha="left")

c = C.axes_at(ax, (16.2, 1.5, 5.2, 5.6))
tt = np.linspace(0, T, 400)
c.plot(tt / 60, 1 - np.exp(-I * v * tt ** 2), color=C.line("dna"), lw=1.8, label="KJMA, Eq. (7.4)")
c.plot(times[::20] / 60, frac[::20], "o", ms=3.2, color=C.line("highlight"), label="simulation")
t99 = np.sqrt(np.log(100) / (I * v))
c.axvline(t99 / 60, color=P.muted(), lw=0.8, ls="--")
c.text(t99 / 60 + 0.2, 0.5, f"99 % at {t99 / 60:.1f} h", fontsize=bio.core.FONT["tiny"], color=P.muted())
c.set_xlim(0, T / 60)
c.set_ylim(0, 1.03)
c.set_xticks([0, 3, 6, 9, 12])
C.style_axes(c, "Time in S phase / h", "Fraction replicated")
c.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="lower right", labelcolor=P.ink())
bio.panel(ax, "C", (15.1, 7.9))
bio.label(ax, (15.7, 7.9), "Replicated fraction", size="normal", bold=True, ha="left")
