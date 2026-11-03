"""MCMC proposals for the JC69 distance of the human and orangutan 12S rRNA genes (exponential prior
with mean 0.2). A: traces of the first 1000 iterations of a sliding window (uniform on d - w/2 to
d + w/2, reflected at 0) with a window that is too small (w = 0.005), about right (w = 0.04) and too large
(w = 0.5), all started at d = 0.25. B: for sliding windows of width w and proportional scaling moves
d' = d exp(eps (u - 1/2)) of size eps, the acceptance proportion and the efficiency (the variance of the
posterior mean relative to independent sampling, estimated from 10 000 iterations) against the step
size relative to the posterior standard deviation. Efficiency is highest at intermediate steps, with
acceptance proportions near 30 to 50%."""
import math
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x, n, mu = 90, 948, 0.2


def logpost(d):
    if d <= 0:
        return -math.inf
    e = math.exp(-4 * d / 3)
    return -d / mu + x * math.log(0.75 - 0.75 * e) + (n - x) * math.log(0.25 + 0.75 * e)


def run(kind, step, N, rng, d0=0.25):
    d, lp, out, acc = d0, logpost(d0), np.empty(N), 0
    U, V = rng.random(N), np.log(rng.random(N))
    for k in range(N):
        u = U[k]
        if kind == "window":
            dn = abs(d + step * (u - 0.5))
            logratio = 0.0
        else:
            c = math.exp(step * (u - 0.5))
            dn = d * c
            logratio = math.log(c)                  # proposal ratio (Jacobian) of the scaling move
        lpn = logpost(dn)
        if V[k] < lpn - lp + logratio:
            d, lp = dn, lpn
            acc += 1
        out[k] = d
    return out, acc / N


def efficiency(s):
    s = s - s.mean()
    var = s.var()
    rho, tot = 1.0, 0.0
    for k in range(1, 2000):
        rho = np.dot(s[:-k], s[k:]) / (len(s) - k) / var
        if rho < 0.05:
            break
        tot += rho
    return 1 / (1 + 2 * tot)


rng = np.random.default_rng(7)
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 3.9), gridspec_kw={"width_ratios": [1.25, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.9, wspace=0.27)
for w, tok in ((0.005, "rna"), (0.04, "dna"), (0.5, "negative")):
    tr, ac = run("window", w, 1000, rng)
    a.plot(tr, color=charts.line(tok), lw=0.9, label=f"$w = {w:g}$ (accepted {ac:.0%})")
a.set_ylim(0.05, 0.27)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "iteration", "$d$")
charts.title(a, "A  Sliding-window traces")

sd = 0.0109
for kind, steps, tok, mk in (("window", sd * np.array([0.3, 1, 3, 8, 25]), "dna", "o"),
                             ("scale", (sd / 0.1) * np.array([0.3, 1, 3, 8, 25]), "plant", "s")):
    acc, eff = [], []
    for st in steps:
        tr, ac = run(kind, st, 10000, rng, d0=0.1)
        acc.append(ac)
        eff.append(efficiency(tr[1000:]))
    rel = steps / sd if kind == "window" else steps * 0.1 / sd
    lab = "sliding window" if kind == "window" else "proportional scaling"
    b.plot(rel, eff, mk + "-", color=charts.line(tok), lw=1.4, ms=4, label=f"{lab}: efficiency")
    b.plot(rel, acc, mk + "--", color=charts.line(tok), lw=1.0, ms=3, mfc="none", label=f"{lab}: acceptance")
b.set_xscale("log")
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "step size / posterior SD", "proportion")
charts.title(b, "B  Acceptance and efficiency")
