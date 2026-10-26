"""Glycated hemoglobin as a time-averaging sensor of blood glucose.
Model: erythrocytes are produced at a constant rate and removed at age T = 120 days, so ages are uniform on
(0, T). Inside each cell hemoglobin is glycated irreversibly (at the N-terminal valine of the beta chains)
with a pseudo-first-order rate k G(t), so the glycated fraction of a cell of age a is
h = 1 - exp(-k * integral of G over the cell's life), and HbA1c is the average of h over ages.
k = 1.42e-4 per mM per day is chosen so that a constant 8.6 mM (154 mg/dL) gives 7.0%.
(A) Steady-state HbA1c against mean glucose, compared with the empirical ADAG regression
(estimated average glucose = 28.7 A1C - 46.7 mg/dL; Nathan et al. 2008), converted to mM.
(B) Response to an improvement of control: mean glucose falls from 12 to 7 mM on day 0. The new value is
reached only after a full erythrocyte lifespan, and half of the change takes about 35 days, because glucose
of the last 30 days contributes about 44% of the value (weights proportional to T - s for glucose s days ago)."""

import numpy as np

import wikibio as bio
from wikibio import charts

T, K = 120.0, 1.42e-4
ages = np.linspace(0, T, 601)


def a1c_steady(g):
    x = K * g * ages
    return 100 * np.mean(1 - np.exp(-x))


def a1c_series(days, gfun):
    out = []
    for t in days:
        # cumulative exposure of a cell of age a at time t: integral of G from t - a to t
        s = np.linspace(0, T, 601)
        gs = gfun(t - s)
        cum = np.concatenate([[0.0], np.cumsum(0.5 * (gs[1:] + gs[:-1]) * np.diff(s))])
        out.append(100 * np.mean(1 - np.exp(-K * cum)))
    return np.array(out)


fig, ax = bio.canvas(19.0, 7.6)
a = charts.axes_at(ax, (1.6, 1.3, 7.0, 5.6))
g = np.linspace(4, 20, 200)
a.plot(g, [a1c_steady(x) for x in g], color=charts.line("blood"), lw=2.0, label="lifespan model")
a1c = np.linspace(4, 13, 50)
a.plot((28.7 * a1c - 46.7) / 18.0, a1c, color=charts.line("neutral"), lw=1.6, ls="--", label="ADAG regression")
for lo, hi, tok, txt in [(4, 5.7, "positive", "normal"), (6.5, 14, "negative", "diabetes (≥ 6.5%)")]:
    a.axhspan(lo, hi, color=bio.P.mix(bio.P.fill(tok), bio.P.surface(), 0.75), lw=0)
    a.text(19.6, (lo + min(hi, 13.6)) / 2, txt, fontsize=bio.core.FONT["tiny"], color=bio.P.edge(tok), ha="right",
           va="center")
a.set_xlim(4, 20)
a.set_ylim(4, 14)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=bio.P.ink(), loc="upper left")
charts.style_axes(a, "mean blood glucose / mM", "HbA1c / %")
charts.title(a, "A  Steady state")

b = charts.axes_at(ax, (11.2, 1.3, 7.0, 5.6))
days = np.linspace(-20, 160, 181)
gstep = lambda t: np.where(t < 0, 12.0, 7.0)
b.plot(days, a1c_series(days, gstep), color=charts.line("blood"), lw=2.0)
hi, lo = a1c_steady(12.0), a1c_steady(7.0)
b.axhline((hi + lo) / 2, color=bio.P.muted(), lw=0.8, ls=":")
b.axvline(T * (1 - 1 / np.sqrt(2)), color=bio.P.muted(), lw=0.8, ls=":")
b.text(T * (1 - 1 / np.sqrt(2)) + 3, hi - 0.3, "half of the change\nafter ≈ 35 days", fontsize=bio.core.FONT["tiny"],
       color=bio.P.muted(), va="top")
b.axvline(0, color=bio.P.edge("negative"), lw=1.0)
b.text(2, lo + 0.2, "glucose 12 → 7 mM", fontsize=bio.core.FONT["tiny"], color=bio.P.edge("negative"))
b.set_xlim(-20, 160)
charts.style_axes(b, "days after the change", "HbA1c / %")
charts.title(b, "B  Response to better control")
