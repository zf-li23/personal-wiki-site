"""Second-order autoregressive dynamics of log abundance (Royama's diagram).

Model: X_t = beta0 + (1 + beta1) X_{t-1} + beta2 X_{t-2} + u_t, with X = ln N, beta1 the direct and beta2
the delayed density dependence, u_t ~ N(0, 0.3^2) independent.
A: the (beta1, beta2) plane. Inside the triangle the process is stationary (both roots of
z^2 - (1 + beta1) z - beta2 = 0 inside the unit circle); below the parabola beta2 = -(1 + beta1)^2 / 4 the
roots are complex and the process cycles, with period 2 pi / theta, cos theta = (1 + beta1) / (2 sqrt(-beta2))
(contours, in time steps). The two points are the examples of B.
B: simulated series (seed 1, 120 years after a burn-in of 100) for the two points: weak direct density
dependence gives longer cycles. C: autocorrelation (ACF, bars) and partial autocorrelation (PACF, points)
of the series with period 6; the PACF is essentially zero beyond lag 2, the signature of order-2 dynamics.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
tri = np.array([[1, -1], [-3, -1], [-1, 1], [1, -1]])
pa.fill(tri[:, 0], tri[:, 1], color=P.mix(P.fill("dna2"), P.surface(), 0.55), lw=0)
pa.plot(tri[:, 0], tri[:, 1], color=P.muted(), lw=0.9)
b1 = np.linspace(-3, 1, 400)
pa.plot(b1, -(1 + b1) ** 2 / 4, color=Q.line_color("protein"), lw=1.2)
B1, B2 = np.meshgrid(np.linspace(-3, 1, 400), np.linspace(-1, 1, 300))
a1, a2 = 1 + B1, B2
inside = (a2 > -1) & (a1 + a2 < 1) & (a2 - a1 < 1) & (a1 ** 2 + 4 * a2 < 0)
with np.errstate(invalid="ignore", divide="ignore"):
    per = 2 * np.pi / np.arccos(np.clip(a1 / (2 * np.sqrt(-a2)), -1, 1))
per = np.where(inside, per, np.nan)
cs = pa.contour(B1, B2, per, levels=[2.5, 3, 4, 5, 6, 8, 12], colors=[P.muted()], linewidths=0.6)
pa.clabel(cs, fontsize=FS["tiny"] - 1, fmt="%g")
ex = [(-1.0, -0.5, "negative"), (-0.2, -0.6, "dna")]
for x, y, tok in ex:
    pa.plot([x], [y], "o", ms=5, color=Q.line_color(tok))
pa.text(-0.95, 0.55, "stationary,\nno cycles", fontsize=FS["tiny"], color=P.ink())
pa.text(-1.95, -0.32, "cycles", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(-3.1, 1.1)
pa.set_ylim(-1.1, 1.1)
C.style_axes(pa, "beta1 (direct)", "beta2 (delayed)")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Royama's diagram", size="small", bold=True, ha="left")

rng = np.random.default_rng(1)


def sim(b1, b2, n=120, burn=100, sd=0.3):
    x = np.zeros(n + burn)
    u = rng.normal(0, sd, n + burn)
    for t in range(2, n + burn):
        x[t] = (1 + b1) * x[t - 1] + b2 * x[t - 2] + u[t]
    return x[burn:]


pb = C.axes_at(ax, (12.0, 1.6, 8.5, 6.8))
series = {}
for k, (x, y, tok) in enumerate(ex):
    s = sim(x, y)
    series[tok] = s
    a1, a2 = 1 + x, y
    pr = 2 * np.pi / np.arccos(a1 / (2 * np.sqrt(-a2)))
    pb.plot(np.arange(len(s)), s + 2.2 * (1 - k), color=Q.line_color(tok), lw=1.0,
            label=f"beta1 = {x}, beta2 = {y}: period {pr:.1f}")
pb.set_yticks([])
C.style_axes(pb, "year", "log abundance (offset)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center", bbox_to_anchor=(0.5, 1.13))
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Simulated series", size="small", bold=True, ha="left")


def acf(x, L):
    x = x - x.mean()
    c0 = (x * x).mean()
    return np.array([(x[: len(x) - k] * x[k:]).mean() / c0 for k in range(L + 1)])


def pacf(x, L):
    out = []
    for k in range(1, L + 1):
        X = np.column_stack([x[k - j - 1: len(x) - j - 1] for j in range(k)] + [np.ones(len(x) - k)])
        coef = np.linalg.lstsq(X, x[k:], rcond=None)[0]
        out.append(coef[k - 1])
    return np.array(out)


s = series["dna"]
L = 12
pc = C.axes_at(ax, (23.0, 1.6, 6.5, 6.8))
pc.bar(np.arange(1, L + 1), acf(s, L)[1:], width=0.6, color=P.fill("dna2"), edgecolor=P.edge("dna2"), lw=0.4,
       label="ACF")
pc.plot(np.arange(1, L + 1), pacf(s, L), "o", ms=3.5, color=Q.line_color("negative"), label="PACF")
ci = 2 / np.sqrt(len(s))
for v in (ci, -ci):
    pc.axhline(v, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pc.axhline(0, color=P.muted(), lw=0.6)
pc.set_ylim(-1, 1)
C.style_axes(pc, "lag (years)", "correlation")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.6, 9.6))
bio.label(ax, (23.0, 9.2), "ACF and PACF", size="small", bold=True, ha="left")
