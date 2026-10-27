"""Graded, ultrasensitive and bistable responses.

A: steady-state responses of three modules to a stimulus s (in units of the half-maximal stimulus):
a hyperbolic (Michaelian) response s/(1 + s), a Hill function with n = 4 (cooperative or multisite
activation), and a zero-order ultrasensitive (Goldbeter-Koshland) modification cycle with K = 0.01.
B: a positive feedback loop, dx/dt = s + f x^4/(K^4 + x^4) - x with K = 0.5. Steady states are the
solutions of s = x - f x^4/(K^4 + x^4); solid branches are stable, dashed branches unstable. Without
feedback (f = 0) x = s; with weak feedback (f = 0.4) the curve is steep but single valued; with
f = 0.8 there is a bistable range between the fold points (s = 0.057 and 0.209): hysteresis; with
f = 1.2 the lower fold lies at negative s, so the switch is irreversible.
C: time courses for a pulse of stimulus (s = 0.3 from t = 10 to 20), then s = 0.1, then s = 0 from t = 60
(time in units of the inverse removal rate).
D: individual cells with thresholds spread log-normally switch all-or-none, while the population
average rises gradually (the situation of Ferrell and Machleder 1998 in Xenopus oocytes).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]
K, N = 0.5, 4


def gk(u, J1=0.01, J2=0.01):
    # Goldbeter-Koshland function: steady-state modified fraction for kinase/phosphatase ratio u
    B = 1 - u + J1 + J2 * u
    return 2 * u * J2 / (B + np.sqrt(B * B - 4 * (1 - u) * u * J2))


fig, ax = bio.canvas(20.0, 13.4)

# A: graded vs ultrasensitive
bio.panel(ax, "A", (0.1, 13.3))
pa = charts.axes_at(ax, (1.6, 8.0, 7.4, 4.6))
s = np.logspace(-2, 2, 400)
pa.plot(s, s / (1 + s), color=charts.line("neutral"), lw=1.8, label="hyperbolic (n = 1)")
pa.plot(s, s**4 / (1 + s**4), color=charts.line("enzyme"), lw=1.8, label="Hill, n = 4")
pa.plot(s, gk(s), color=charts.line("highlight"), lw=1.8, label="zero-order cycle")
pa.set_xscale("log")
pa.set_xlim(0.01, 100)
pa.set_ylim(0, 1.05)
pa.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "stimulus s (relative to EC₅₀)", "response")
charts.title(pa, "Graded and ultrasensitive responses")

# B: bifurcation diagram of the positive-feedback module
bio.panel(ax, "B", (10.3, 13.3))
pb = charts.axes_at(ax, (11.8, 8.0, 7.6, 4.6))
x = np.linspace(0, 1.6, 4000)
cases = [(0.0, "neutral", "f = 0"), (0.4, "enzyme", "f = 0.4"), (0.8, "highlight", "f = 0.8"), (1.2, "negative", "f = 1.2")]
for f, tok, name in cases:
    sx = x - f * x**N / (K**N + x**N)
    dsdx = np.gradient(sx, x)
    stable = dsdx > 0
    col = charts.line(tok)
    seg = np.split(np.arange(len(x)), np.where(np.diff(stable.astype(int)) != 0)[0] + 1)
    for k, idx in enumerate(seg):
        pb.plot(sx[idx], x[idx], color=col, lw=1.8 if stable[idx[0]] else 1.1,
                ls="-" if stable[idx[0]] else (0, (3, 2)), label=name if k == 0 else None)
# hysteresis arrows for f = 0.8
col = charts.line("highlight")
pb.annotate("", xy=(0.209, 1.02), xytext=(0.209, 0.32), arrowprops=dict(arrowstyle="->", color=col, lw=1.0))
pb.annotate("", xy=(0.057, 0.06), xytext=(0.057, 0.62), arrowprops=dict(arrowstyle="->", color=col, lw=1.0))
pb.text(0.225, 0.62, "switch on", fontsize=FS, color=col)
pb.text(0.05, 0.2, "switch off", fontsize=FS, color=col, ha="right")
pb.set_xlim(-0.05, 0.5)
pb.set_ylim(0, 1.6)
pb.axvline(0, color=P.muted(), lw=0.6)
pb.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="lower right")
charts.style_axes(pb, "stimulus s", "steady-state activity x*")
charts.title(pb, "Positive feedback: bistability and hysteresis")

# C: time courses
bio.panel(ax, "C", (0.1, 6.4))
pc = charts.axes_at(ax, (1.6, 1.3, 7.4, 4.5))


def stim(t):
    if 10 <= t < 20:
        return 0.3
    if t < 10:
        return 0.0
    return 0.1 if t < 60 else 0.0


tt = np.linspace(0, 100, 2000)
for f, tok, name in cases[1:]:
    sol = solve_ivp(lambda t, y: [stim(t) + f * y[0]**N / (K**N + y[0]**N) - y[0]], (0, 100), [0.0],
                    t_eval=tt, max_step=0.1)
    pc.plot(sol.t, sol.y[0], color=charts.line(tok), lw=1.8, label=name)
pc.plot(tt, [stim(t) for t in tt], color=P.muted(), lw=1.0, ls=(0, (4, 2)), label="stimulus s")
pc.set_xlim(0, 100)
pc.set_ylim(0, 1.6)
pc.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(pc, "time (units of 1/removal rate)", "activity x")
charts.title(pc, "A transient pulse is remembered")

# D: single cells and population
bio.panel(ax, "D", (10.3, 6.4))
pd = charts.axes_at(ax, (11.8, 1.3, 7.6, 4.5))
rng = np.random.default_rng(0)
thr = np.exp(rng.normal(np.log(0.1), 0.9, 12))
dose = np.logspace(-3, 1, 400)
for k, th in enumerate(np.sort(thr)):
    pd.plot(dose, 0.02 + (dose >= th) * 0.96, color=charts.line("neutral"), lw=0.7, alpha=0.8,
            label="single cells" if k == 0 else None)
from scipy.stats import norm  # noqa: E402

pd.plot(dose, norm.cdf((np.log(dose) - np.log(0.1)) / 0.9), color=charts.line("highlight"), lw=2.2,
        label="population average")
pd.set_xscale("log")
pd.set_xlim(1e-3, 10)
pd.set_ylim(-0.02, 1.08)
pd.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left")
charts.style_axes(pd, "hormone concentration (relative)", "fraction activated")
charts.title(pd, "All-or-none cells, graded population")
