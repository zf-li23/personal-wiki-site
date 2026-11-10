# Sandwich ELISA: principle (A) and a four-parameter logistic (4PL) standard curve (B, simulated data).
#   y = d + (a - d) / (1 + (x / c)^b)        (a: response at zero dose, d: response at infinite dose, c: EC50, b: slope)
# Simulated standards: a 2-fold dilution series from 1000 pg/ml with true parameters a = 0.05, d = 2.5, c = 80 pg/ml,
# b = 1.2 and 5% multiplicative noise (duplicates); the 4PL is refitted by least squares in log-concentration and an
# unknown with absorbance 1.0 is read off the inverse curve  x = c ((a - d) / (y - d) - 1)^(1/b).
import numpy as np
from scipy.optimize import curve_fit

import wikibio as bio
from wikibio import charts

P = bio.P


def f4(x, a, b, c, d):
    return d + (a - d) / (1 + (x / c) ** b)


fig, ax = bio.canvas(14, 5.6)
# ---- A: sandwich principle -----------------------------------------------------------------------------
bio.label(ax, (0.4, 5.2), "A", size="title", bold=True)
bio.box(ax, (3.2, 0.55), 6.0, 0.5, token="neutral", text="plate surface", size="small")
for x in (1.1, 3.2, 5.3):
    bio.antibody(ax, (x, 1.85), size=1.05, token="antibody", light_token="protein")
bio.label(ax, (6.45, 1.85), "capture\nantibody", size="small", ha="left")
bio.protein(ax, (3.2, 3.15), 0.7, 0.5, "metabolite", text="antigen", size="tiny")
bio.antibody(ax, (3.2, 4.15), size=0.95, angle=180, token="receptor", light_token="protein")
bio.label(ax, (4.05, 4.2), "detection\nantibody", size="small", ha="left")
bio.protein(ax, (3.2, 5.0), 0.34, 0.3, "enzyme", text="E", size="tiny")
bio.arrow(ax, (1.0, 4.4), (1.0, 3.6), kind="process", head=0.14)
bio.label(ax, (0.6, 3.4), "substrate:\ncolour", size="tiny", ha="left")
# ---- B: 4PL curve -----------------------------------------------------------------------------------------
rng = np.random.default_rng(0)
conc = 1000.0 / 2 ** np.arange(8)
xs = np.repeat(conc, 2)
ys = f4(xs, 0.05, 1.2, 80.0, 2.5) * (1 + 0.05 * rng.standard_normal(xs.size))
popt, _ = curve_fit(lambda lx, a, b, c, d: f4(10 ** lx, a, b, c, d), np.log10(xs), ys, p0=[0.05, 1.0, 100.0, 2.5],
                    bounds=([0, 0.2, 1, 1], [0.5, 4, 1e4, 5]))
pax = charts.axes_at(ax, (8.7, 0.95, 4.9, 3.9))
grid = np.logspace(0, 3.2, 300)
pax.plot(grid, f4(grid, *popt), color=charts.line("protein"), lw=1.6, label="4PL fit")
pax.plot(xs, ys, "o", color=charts.line("receptor"), ms=3.5, label="standards")
a_, b_, c_, d_ = popt
y0 = 1.0
x0 = c_ * ((a_ - d_) / (y0 - d_) - 1) ** (1 / b_)
pax.plot([1, x0, x0], [y0, y0, 0], color=P.muted(), lw=0.9, ls="--")
pax.text(1.3, y0 + 0.07, f"unknown: A = 1.0, {x0:.0f} pg/ml", fontsize=7, color=P.muted())
pax.set_xscale("log")
pax.set_xlim(1, 1600)
pax.set_ylim(0, 2.8)
pax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0.0, 0.98))
charts.style_axes(pax, "antigen / (pg/ml)", "absorbance")
bio.label(ax, (8.2, 5.2), "B", size="title", bold=True)
