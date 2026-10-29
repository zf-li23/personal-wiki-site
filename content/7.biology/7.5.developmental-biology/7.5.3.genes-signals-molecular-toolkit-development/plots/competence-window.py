"""Competence: a tissue responds to an inducer only during a window of time.

Model: the competence of the responding cells rises and falls, c(t) = sigma((t - t_on)/w) sigma((t_off - t)/w)
with sigma the logistic function, t_on = 4 h, t_off = 10 h, w = 0.5 h (for example, the competence of
amphibian animal-cap ectoderm to respond to mesoderm inducers, gained in the blastula and lost in the early
gastrula). An inducer pulse of unit strength lasting tau hours from time t0 is integrated as
R = integral c(t) S(t) dt, and a cell responds when R exceeds its threshold theta, which varies between cells
(log-normal, median 1 h, standard deviation 0.3 in ln theta).
A: the competence window and three pulses of 2 h. B: fraction of responding cells against the start of the
pulse for pulses of 1, 2 and 4 h: a short pulse works only in the middle of the window; a long pulse widens the
response window but cannot extend it beyond the period of competence.
"""

import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27, 9.6)
TON, TOFF, W = 4.0, 10.0, 0.5
t = np.linspace(0, 14, 1401)


def sig(x):
    return 1 / (1 + np.exp(-x))


c = sig((t - TON) / W) * sig((TOFF - t) / W)

bio.panel(ax, "A", (0.2, 9.4))
pa = quant.Plot(ax, (2.0, 1.6, 9.8, 6.8), xlim=(0, 14), ylim=(0, 1.25), xlabel="time / h", ylabel="competence c(t)",
                xticks=[0, 2, 4, 6, 8, 10, 12, 14], yticks=[0, 0.5, 1])
pa.line(t, c, "enzyme", text="competence", at=0.5, dy=0.1)
for t0, tok in ((2.0, "negative"), (6.0, "positive"), (9.5, "highlight")):
    pa.span(t0, t0 + 2, tok, strength=0.55)
    R = np.trapezoid(c[(t >= t0) & (t <= t0 + 2)], t[(t >= t0) & (t <= t0 + 2)])
    pa.text(t0 + 1, 1.15, f"R = {R:.2f}", size="tiny")
bio.label(ax, (6.9, 9.2), "2-h inducer pulses at three times", size="tiny", color=P.muted())

bio.panel(ax, "B", (13.8, 9.4))
pb = quant.Plot(ax, (15.6, 1.6, 9.8, 6.8), xlim=(0, 14), ylim=(0, 1.05), xlabel="start of inducer pulse t0 / h",
                ylabel="fraction of cells responding", xticks=[0, 2, 4, 6, 8, 10, 12, 14], yticks=[0, 0.5, 1])
t0s = np.linspace(0, 14, 141)
cum = np.r_[0, np.cumsum((c[1:] + c[:-1]) / 2 * np.diff(t))]
for tau, tok in ((1, "dna"), (2, "positive"), (4, "drug")):
    R = np.interp(t0s + tau, t, cum, right=cum[-1]) - np.interp(t0s, t, cum)
    frac = norm.cdf(np.log(np.maximum(R, 1e-9)) / 0.3)
    pb.line(t0s, frac, tok, text=f"τ = {tau} h", at=0.12 if tau == 4 else 0.3 + 0.03 * tau, dx=-0.6, dy=0.06)
pb.span(TON, TOFF, "enzyme", strength=0.8, text="competence window", size="tiny")
