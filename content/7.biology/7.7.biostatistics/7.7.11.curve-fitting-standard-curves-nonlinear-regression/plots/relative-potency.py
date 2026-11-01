"""Relative potency from two dose-response curves (simulated data). A test preparation and a reference are
each assayed at 8 doses in triplicate (true EC50 of the test 2.5 times that of the reference, Hill slope 1.2,
response in % of control, residual SD 5). A: parallel 4PL curves with common bottom, top and slope: the
horizontal distance on the log-dose axis is the log relative potency. B: residual sum of squares of the
separate fits and of the constrained (parallel) fit, the basis of the extra-sum-of-squares F test for
parallelism; and a second, non-parallel test preparation (Hill slope 0.6) that fails it.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
dose = np.repeat(np.logspace(-1, 2.5, 8), 3)


def f(x, b, t, lec, h):
    return b + (t - b) / (1 + 10 ** (h * (np.log10(x) - lec)))


ref = f(dose, 0, 100, np.log10(2.0), 1.2) + rng.normal(0, 5, dose.size)
tst = f(dose, 0, 100, np.log10(5.0), 1.2) + rng.normal(0, 5, dose.size)
bad = f(dose, 0, 100, np.log10(5.0), 0.6) + rng.normal(0, 5, dose.size)


def parallel(X, b, t, lec, h, lrho):
    x, u = X
    return f(x, b, t, lec + lrho * u, h)


def fit_pair(y2):
    X = (np.r_[dose, dose], np.r_[np.zeros(dose.size), np.ones(dose.size)])
    yy = np.r_[ref, y2]
    pc, cc = optimize.curve_fit(parallel, X, yy, p0=[0, 100, 0.3, 1, 0.3])
    rss_c = ((yy - parallel(X, *pc)) ** 2).sum()
    rss_s = 0
    for yv in (ref, y2):
        ps, _ = optimize.curve_fit(f, dose, yv, p0=[0, 100, 0.5, 1])
        rss_s += ((yv - f(dose, *ps)) ** 2).sum()
    n = yy.size
    F = ((rss_c - rss_s) / 3) / (rss_s / (n - 8))
    return pc, cc, rss_c, rss_s, F, stats.f.sf(F, 3, n - 8)


pc, cc, rc, rs, F, p = fit_pair(tst)
pc2, cc2, rc2, rs2, F2, p2 = fit_pair(bad)
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.25)
g = np.logspace(-1.2, 2.7, 200)
ax = axs[0]
for yv, tok, lec, lab in [(ref, "dna", pc[2], "reference"), (tst, "rna", pc[2] + pc[4], "test")]:
    ax.scatter(dose, yv, s=10, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.6, zorder=3, label=lab)
    ax.plot(g, f(g, pc[0], pc[1], lec, pc[3]), color=charts.line(tok), lw=1.5)
    ax.plot([10 ** lec] * 2, [-5, (pc[0] + pc[1]) / 2], color=charts.line(tok), lw=0.8, ls="--")
ax.annotate("", (10 ** (pc[2] + pc[4]), 50), (10 ** pc[2], 50), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.9))
rho = 10 ** pc[4]
lo, hi = 10 ** (pc[4] - 1.96 * np.sqrt(cc[4, 4])), 10 ** (pc[4] + 1.96 * np.sqrt(cc[4, 4]))
ax.text(1.0, 112, f"potency ratio EC50(test)/EC50(ref) = {rho:.2f} ({lo:.2f}-{hi:.2f})", fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_ylim(-15, 125)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "dose", "response / % of control")
charts.title(ax, "A  Parallel curves")
ax = axs[1]
for yv, tok, lab in [(ref, "dna", "reference"), (bad, "protein", "test 2 (shallower)")]:
    ps, _ = optimize.curve_fit(f, dose, yv, p0=[0, 100, 0.5, 1])
    ax.scatter(dose, yv, s=10, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.6, zorder=3, label=lab)
    ax.plot(g, f(g, *ps), color=charts.line(tok), lw=1.5)
ax.text(0.07, 112, f"parallelism: test 1 F = {F:.2f}, p = {p:.2f};  test 2 F = {F2:.1f}, p = {p2:.1g}",
        fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_ylim(-15, 125)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "dose", None)
charts.title(ax, "B  A curve that is not parallel")
