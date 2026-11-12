# Why aphids multiply so fast: a life-table model (illustrative parameters of the order reported for
# aphids at about 20 C, e.g. Dixon 1998, not data for one species). A parthenogenetic, viviparous female
# matures in tau days and then produces m daughters per day for d days. The intrinsic rate of increase r
# solves the Euler-Lotka equation sum_x exp(-r x) l_x m_x = 1 (daily steps, survival l_x = 1 here).
# (A) Numbers from one founder (daily simulation) for three life histories: telescoped parthenogenetic
# viviparity; the same with an egg stage of 8 days (oviparity); and sexual reproduction with an egg stage,
# where half the offspring are sons. (B) r and doubling time as a function of tau for viviparous
# parthenogenesis: shortening the generation, which telescoping of generations does, raises r strongly.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def schedule(tau, m=4.0, d=20, egg=0, daughters=1.0, horizon=80):
    """Daily births (female-equivalents) by mothers of age x, as an array over x."""
    f = np.zeros(horizon + 1)
    start = tau + egg
    f[start:start + d] = m * daughters
    return f


def simulate(f, days=40):
    births = np.zeros(days + 1)
    births[0] = 1.0
    for t in range(1, days + 1):
        ages = t - np.arange(t)  # age of each cohort born at day s
        births[t] = np.sum(births[:t] * f[np.clip(ages, 0, len(f) - 1)] * (ages < len(f)))
    alive = np.cumsum(births)  # no mortality in this illustration
    return alive


def r_of(f):
    x = np.arange(len(f))
    lo, hi = 1e-4, 2.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if np.sum(np.exp(-mid * x) * f) > 1:
            lo = mid
        else:
            hi = mid
    return lo


fig, ax = bio.canvas(24, 9.5)
a1 = charts.axes_at(ax, (1.6, 1.4, 9.6, 7.0))
a2 = charts.axes_at(ax, (13.6, 1.4, 9.6, 7.0))
days = 40
t = np.arange(days + 1)
cases = [("viviparous parthenogenesis", schedule(7), "positive", "-"),
         ("parthenogenesis with an 8-day egg stage", schedule(7, egg=8), "enzyme", "--"),
         ("sexual, with egg stage (half sons)", schedule(7, egg=8, daughters=0.5), "negative", ":")]
for name, f, tok, ls in cases:
    n = simulate(f, days)
    r = r_of(f)
    a1.semilogy(t, n, color=P.edge(tok), lw=2, ls=ls, label=f"{name} (r = {r:.2f}/day)")
a1.set_xlabel("Days after founding")
a1.set_ylabel("Females (no mortality)")
a1.legend(fontsize=7, frameon=False, loc="upper left")
taus = np.arange(4, 15)
rs = np.array([r_of(schedule(int(k))) for k in taus])
a2.plot(taus, rs, color=P.edge("positive"), lw=2, marker="o", ms=4)
a2.set_xlabel("Development time to first birth, $\tau$ (days)")
a2.set_ylabel("Intrinsic rate of increase r (per day)")
a3 = a2.twinx()
a3.plot(taus, np.log(2) / rs, color=P.edge("enzyme"), lw=1.5, ls="--")
a3.set_ylabel("Doubling time (days)", color=P.edge("enzyme"))
a3.tick_params(axis="y", colors=P.edge("enzyme"))
for s in ("top",):
    a3.spines[s].set_visible(False)
bio.panel(ax, "A", (0.2, 9.3))
bio.panel(ax, "B", (12.2, 9.3))
bio.label(ax, (23.8, 0.3), "Model with illustrative parameters (m = 4 daughters/day for 20 days)", size="tiny",
          color=P.muted(), ha="right")
