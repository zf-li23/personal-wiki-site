"""Clone sizes of a stem cell in the linear birth-death process (Theorem 36.4.1).

One stem cell at t = 0; each stem cell divides into two stem cells at rate p = 1 and is lost (divides into two
differentiated cells) at rate q = 0.4 (time in units of 1/p). A: the distribution of the number N of stem
cells at t = 4: exact formula (bars) and 20 000 runs of the Gillespie algorithm (points, seed 0); the bar at
N = 0 is extinction. B: survival P(N > 0) over time, tending to 1 - q/p = 0.6. C: the scaled size w = N / mean
at t = 8 for surviving clones, compared with the limit law: an exponential of rate 1 - q/p.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
p, q = 1.0, 0.4
fig, ax = bio.canvas(30.0, 9.0)
rng = np.random.default_rng(0)


def exact(N, t):
    E = np.exp((p - q) * t)
    P0 = q * (1 - 1 / E) / (p - q / E)
    g = (1 - 1 / E) / (1 - q / p / E)
    PN = (p - q) ** 2 * E / (p * (E - 1) * (p * E - q)) * g ** N
    return np.where(N == 0, P0, PN)


def gillespie(t_end, runs):
    out = np.empty(runs, dtype=int)
    for k in range(runs):
        n, t = 1, 0.0
        while n > 0:
            t += rng.exponential(1.0 / ((p + q) * n))
            if t > t_end:
                break
            n += 1 if rng.random() < p / (p + q) else -1
        out[k] = n
    return out


sim4 = gillespie(4.0, 20000)
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.2))
N = np.arange(0, 41)
pa.bar(N, exact(N, 4.0), width=0.8, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.4, label="exact")
freq = np.bincount(sim4, minlength=41)[:41] / len(sim4)
pa.plot(N, freq, "o", ms=2.6, color=Q.line_color("negative"), label="Gillespie, 20 000 runs")
pa.set_xlim(-1, 40)
C.style_axes(pa, "stem cells N at t = 4", "probability")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
pa.text(1.2, exact(np.array([0]), 4.0)[0] * 0.97, "extinct", fontsize=FS["tiny"], color=P.muted(), va="top")
bio.panel(ax, "A", (0.2, 8.8))
bio.label(ax, (2.0, 8.5), "Clone-size distribution", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.2))
t = np.linspace(0.02, 10, 300)
surv = 1 - exact(np.zeros_like(t, dtype=int), t)
pb.plot(t, surv, color=Q.line_color("protein"), lw=1.7)
pb.axhline(1 - q / p, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(6.0, 1 - q / p + 0.03, "1 - q/p", fontsize=FS["tiny"], color=P.muted())
pb.plot([4.0], [(sim4 > 0).mean()], "o", ms=3.5, color=Q.line_color("negative"))
pb.set_ylim(0, 1.05)
C.style_axes(pb, "time t (units of 1/p)", "P(clone survives)")
bio.panel(ax, "B", (10.6, 8.8))
bio.label(ax, (12.0, 8.5), "Survival", size="small", bold=True, ha="left")

sim8 = gillespie(8.0, 6000)
mean8 = np.exp((p - q) * 8.0)
w = sim8[sim8 > 0] / mean8
pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.2))
pc.hist(w, bins=np.linspace(0, 6, 31), density=True, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.4,
        label="surviving clones, t = 8")
ww = np.linspace(0, 6, 200)
lam = 1 - q / p
pc.plot(ww, lam * np.exp(-lam * ww), color=Q.line_color("negative"), lw=1.6, label="limit: rate 1 - q/p")
C.style_axes(pc, "scaled size w = N / mean", "density")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (20.6, 8.8))
bio.label(ax, (22.0, 8.5), "Scaled sizes are exponential", size="small", bold=True, ha="left")
