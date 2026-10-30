"""Mortality and survival in the Gompertz-Makeham model (Definition 37.1.2).

Hazard mu(x) = A + B exp(gamma x) per year at age x; survival S(x) = exp(-A x - (B / gamma)(exp(gamma x) - 1)).
Parameters (illustrative, of the order of human values, not fitted to a particular country): "2020" A = 3e-4,
B = 1.7e-5, gamma = 0.10; "1900" A = 0.008, B = 6e-5, gamma = 0.085 (infant mortality not modeled).
A: hazard on a log scale; points: a life table estimated from a simulated cohort of 100 000 people (2020
parameters, seed 0), deaths over person-years at risk in each year of age; the Gompertz-Makeham fit by least
squares on log hazard (ages 30-95) recovers gamma; the mortality-rate doubling time is ln 2 / gamma. Flat lines:
age-independent hazards of animals with negligible senescence in the laboratory (Hydra, about 0.6 % per year;
naked mole-rat, about 1/10 000 per day). B: survival curves: lower background mortality makes them more
rectangular, a smaller gamma (slower aging) shifts their fall to later ages.
"""

import numpy as np
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)


def hazard(x, A, B, g):
    return A + B * np.exp(g * x)


def surv(x, A, B, g):
    return np.exp(-A * x - B / g * (np.exp(g * x) - 1))


now = (3e-4, 1.7e-5, 0.10)
old = (0.008, 6e-5, 0.085)
# simulate a cohort by inverse transform on a fine grid
xg = np.linspace(0, 130, 13001)
Sg = surv(xg, *now)
u = rng.random(100_000)
ages = np.interp(-u, -Sg, xg)
edges = np.arange(0, 111)
deaths = np.histogram(ages, edges)[0]
expo = np.array([np.clip(ages - a, 0, 1).sum() for a in edges[:-1]])
mid = edges[:-1] + 0.5
ok = expo > 50
mhat = deaths[ok] / expo[ok]
sel = ok & (mid >= 30) & (mid <= 95)
popt, _ = curve_fit(lambda x, a, lb, g: np.log(a + np.exp(lb) * np.exp(g * x)), mid[sel],
                    np.log(np.maximum(deaths[sel] / expo[sel], 1e-6)), p0=(1e-4, np.log(1e-5), 0.1),
                    bounds=([0, -20, 0.01], [0.01, 0, 0.3]))
Af, Bf, gf = popt[0], np.exp(popt[1]), popt[2]

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
x = np.linspace(0, 110, 400)
pa.semilogy(x, hazard(x, *now), color=Q.line_color("protein"), lw=1.7, label="2020-like (true)")
pa.semilogy(mid[ok][mhat > 0], mhat[mhat > 0], "o", ms=2.4, color=Q.line_color("protein"), alpha=0.7,
            label="simulated life table")
pa.semilogy(x, hazard(x, Af, Bf, gf), color=Q.line_color("negative"), lw=1.0, ls=(0, (4, 2)),
            label=f"fit: gamma = {gf:.3f}, doubling {np.log(2) / gf:.1f} y")
pa.semilogy(x, hazard(x, *old), color=Q.line_color("enzyme"), lw=1.5, label="1900-like")
pa.axhline(0.006, color=Q.line_color("positive"), lw=1.2, ls=(0, (1, 1.5)))
pa.text(2, 0.0068, "Hydra (flat)", fontsize=FS["tiny"], color=Q.line_color("positive"))
pa.axhline(0.0365, color=Q.line_color("highlight"), lw=1.2, ls=(0, (1, 1.5)))
pa.text(2, 0.041, "naked mole-rat (flat)", fontsize=FS["tiny"], color=Q.line_color("highlight"))
pa.set_xlim(0, 110)
pa.set_ylim(1e-4, 1.5)
C.style_axes(pa, "age x / years", "hazard per year")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Mortality rises exponentially with age", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.5, 1.6, 11.5, 6.8))
for par, tok, lab in ((old, "enzyme", "1900-like"), (now, "protein", "2020-like"),
                      ((3e-4, 1.7e-5 * np.exp(0.1 * 10) / np.exp(0.09 * 10), 0.09), "positive", "gamma = 0.09")):
    pb.plot(x, surv(x, *par), color=Q.line_color(tok), lw=1.7, label=lab)
    med = x[np.argmin(np.abs(surv(x, *par) - 0.5))]
    pb.plot([med], [0.5], "o", ms=3.5, color=Q.line_color(tok))
pb.axhline(0.5, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.set_xlim(0, 110)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "age x / years", "survival S(x)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Survival curves (dots: median)", size="small", bold=True, ha="left")
