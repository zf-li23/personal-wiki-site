"""The MacArthur-Wilson model with species that differ: independent two-state species.

A mainland pool of P = 100 species. Species i colonizes an island where it is absent at rate lambda_i and
goes extinct where present at rate mu_i, independently of the others (a two-state Markov chain). Rates are
lognormal: lambda_i = l0 exp(1.2 Z_i), mu_i = 0.05 exp(1.0 W_i) per year, with l0 = 0.02 (near island)
or 0.005 (far island). For an island emptied at t = 0, p_i(t) = lambda_i/(lambda_i + mu_i)(1 - exp(-(lambda_i
+ mu_i) t)), S(t) = sum p_i(t), immigration I(t) = sum lambda_i (1 - p_i(t)) and extinction E(t) = sum mu_i p_i(t).
A: I and E plotted against S along this trajectory (the curves of MacArthur and Wilson): heterogeneity
bends both curves upward (immigration falls steeply at first, extinction rises more than in proportion to
S), because good colonists arrive first and poor persisters go extinct first; dots mark the equilibria
S* = sum lambda_i/(lambda_i + mu_i), where the two rates are equal. B: recolonization of a defaunated island, expected S(t) (lines) and one stochastic realization
for each island (steps); the vertical lines mark t_0.9, the time at which 90 % of the deficit is made up.
C: species turnover at equilibrium: one realization of the near island over 200 years; S fluctuates around
S* while the list of species changes (immigrations and extinctions per decade, bars).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(7)

n = 100
Z = rng.standard_normal(n)
W = rng.standard_normal(n)
mu = 0.05 * np.exp(1.0 * W)
islands = {"near": 0.02 * np.exp(1.2 * Z), "far": 0.005 * np.exp(1.2 * Z)}
toks = {"near": "plant", "far": "enzyme"}

t = np.logspace(-2, 3.3, 600)


def expected(lam):
    k = lam + mu
    p = lam[None, :] / k[None, :] * (1 - np.exp(-k[None, :] * t[:, None]))
    return p.sum(1), (lam[None, :] * (1 - p)).sum(1), (mu[None, :] * p).sum(1)


def gillespie(lam, T, start=None):
    x = np.zeros(n, dtype=bool) if start is None else start.copy()
    tt, ts, ss, ev = 0.0, [0.0], [x.sum()], []
    while tt < T:
        rates = np.where(x, mu, lam)
        R = rates.sum()
        tt += rng.exponential(1 / R)
        i = rng.choice(n, p=rates / R)
        ev.append((tt, "ext" if x[i] else "imm"))
        x[i] = ~x[i]
        ts.append(tt)
        ss.append(x.sum())
    return np.array(ts), np.array(ss), ev, x


fig, ax = bio.canvas(31.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 7.0, 6.8))
for name, lam in islands.items():
    S, I, E = expected(lam)
    c = Q.line_color(toks[name])
    pa.plot(S, I, color=c, lw=1.7, label=f"immigration, {name}")
    pa.plot(S, E, color=c, lw=1.7, ls=(0, (1, 1.4)), label=f"extinction, {name}")
    Ss = (lam / (lam + mu)).sum()
    pa.plot([Ss], [np.interp(Ss, S, I)], "o", ms=5, color=c)
pa.set_xlim(0, 40)
pa.set_ylim(0, 2.6)
C.style_axes(pa, "species on the island S", "rate (species per year)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Concave immigration and extinction curves", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.4, 1.6, 7.0, 6.8))
for name, lam in islands.items():
    S, _, _ = expected(lam)
    c = Q.line_color(toks[name])
    pb.plot(t, S, color=c, lw=1.8, label=f"{name} island, expected")
    ts, ss, _, _ = gillespie(lam, 400)
    pb.step(ts, ss, where="post", color=c, lw=0.7, alpha=0.8)
    t90 = np.interp(0.9 * S[-1], S, t)
    pb.axvline(t90, color=c, lw=0.8, ls=(0, (3, 2)))
    pb.text(t90 + 4, 2 if name == "near" else 6, f"t₀.₉ ≈ {t90:.0f} yr", fontsize=FS["tiny"], color=c)
pb.set_xlim(0, 400)
pb.set_ylim(0, 45)
C.style_axes(pb, "years after defaunation", "species present")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.2), "Recolonization", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))
lam = islands["near"]
p_eq = lam / (lam + mu)
start = rng.random(n) < p_eq
ts, ss, ev, _ = gillespie(lam, 200, start)
pc.step(ts, ss, where="post", color=Q.line_color("plant"), lw=1.2)
pc.axhline(p_eq.sum(), color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(198, p_eq.sum() + 1, "S*", fontsize=FS["tiny"], color=P.muted(), ha="right")
pc.set_xlim(0, 200)
pc.set_ylim(0, 45)
C.style_axes(pc, "years", "species present")
pc2 = pc.twinx()
bins = np.arange(0, 201, 10)
imm = np.histogram([e[0] for e in ev if e[1] == "imm"], bins)[0]
ext = np.histogram([e[0] for e in ev if e[1] == "ext"], bins)[0]
pc2.bar(bins[:-1] + 2.5, imm, width=4.5, color=Q.line_color("dna"), alpha=0.7, label="immigrations")
pc2.bar(bins[:-1] + 7.5, ext, width=4.5, color=Q.line_color("negative"), alpha=0.7, label="extinctions")
pc2.set_ylim(0, 60)
C.style_axes(pc2, None, "events per decade")
pc2.spines["right"].set_visible(True)
pc2.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.2), "Constant number, changing list", size="small", bold=True, ha="left")
