"""Stochastic switching of a bistable self-activating gene, a birth-death chain with production
f(n) = Omega [0.05 + s^4/(1 + s^4)], s = n/(0.4 Omega), and degradation n (time in protein
lifetimes); Omega sets the number of molecules. A: a Gillespie trajectory for Omega = 30: long dwells
near the off and on states with rare jumps. B: the exact stationary distribution (line) and the
simulated one (bars) for Omega = 30, and the effective potential -ln P(n) (right axis) whose barrier
sets the switching rate. C: mean time to switch from off to on against Omega, from simulations
(points) and from the exact first-passage formula for birth-death chains (line): it grows
exponentially with the system size."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(4)


def prod(n, om):
    s = n / (0.4 * om)
    return om * (0.05 + s ** 4 / (1 + s ** 4))


def stationary(om):
    n = np.arange(int(4 * om))
    logp = np.concatenate([[0.0], np.cumsum(np.log(prod(n[:-1], om)) - np.log(n[1:]))])
    p = np.exp(logp - logp.max())
    return n, p / p.sum()


def states(om):
    n, p = stationary(om)
    lo = np.argmax(p[: int(0.7 * om)])
    hi = int(0.7 * om) + np.argmax(p[int(0.7 * om):])
    mid = lo + np.argmin(p[lo:hi])
    return n, p, lo, mid, hi


def mfpt(om):
    """Exact mean first-passage time from the off maximum to the on maximum."""
    n, p, lo, mid, hi = states(om)
    cum = np.cumsum(p)
    k = np.arange(lo, hi)
    return np.sum(cum[k] / (prod(k, om) * p[k]))


def run(om, tmax, n0, stop=None):
    t, n = 0.0, n0
    ts, ns = [0.0], [n0]
    while t < tmax:
        a1, a2 = prod(n, om), float(n)
        t += rng.exponential(1 / (a1 + a2))
        n += 1 if rng.random() * (a1 + a2) < a1 else -1
        ts.append(t)
        ns.append(n)
        if stop is not None and n >= stop:
            return t
    return np.array(ts), np.array(ns)


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3), gridspec_kw=dict(width_ratios=(1.3, 1, 1)))
fig.subplots_adjust(wspace=0.42, left=0.06, right=0.97, bottom=0.17, top=0.88)

om = 30
ts, ns = run(om, 6000, 1)
ax = axs[0]
ax.plot(ts[::3], ns[::3], color=charts.line("protein"), lw=0.5)
charts.style_axes(ax, "time", "protein number n")
charts.title(ax, r"A  $\Omega = 30$")

ax = axs[1]
n, p, lo, mid, hi = states(om)
dt = np.diff(ts)
w = np.bincount(ns[:-1], weights=dt, minlength=n.size)[: n.size]
ax.bar(n, w / w.sum(), width=1.0, color=P.fill("protein"), lw=0)
ax.plot(n, p, color=P.ink(), lw=1.0)
charts.style_axes(ax, "n", "probability")
ax2 = ax.twinx()
ax2.plot(n, -np.log(p), color=charts.line("blood"), lw=1.2, ls="--")
ax2.set_ylim(0, 10)
for sp in ("top",):
    ax2.spines[sp].set_visible(False)
ax2.spines["right"].set_color(P.muted())
ax2.tick_params(colors=P.muted(), labelcolor=charts.line("blood"), labelsize=bio.core.FONT["tiny"])
ax2.set_ylabel(r"$-\ln P(n)$", fontsize=bio.core.FONT["small"], color=charts.line("blood"))
ax.set_xlim(-1, 70)
charts.title(ax, "B  Bimodal distribution")

ax = axs[2]
oms = np.arange(6, 61, 1)
ax.plot(oms, [mfpt(o) for o in oms], color=P.ink(), lw=1.3, label="exact")
for o in (10, 15, 20, 25, 30):
    lo_, hi_ = states(o)[2], states(o)[4]
    T = [run(o, 1e9, lo_, stop=hi_) for _ in range(30)]
    ax.plot(o, np.mean(T), "o", ms=4, color=charts.line("protein"))
ax.set_yscale("log")
charts.style_axes(ax, r"system size $\Omega$", "mean switching time")
charts.title(ax, "C  Exponential in size")
