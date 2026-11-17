"""Acquisition and allocation: the Y model (van Noordwijk and de Jong 1986).

Each individual acquires resources A and allocates a fraction p to reproduction, R = p A, and the rest to
survival or growth, S = (1 - p) A, with A and p independent. 400 individuals per panel.
A: variation mainly in acquisition (CV of A = 0.4, SD of p = 0.03, mean p = 0.5): reproduction and
survival are positively correlated across individuals although each individual faces a trade-off.
B: variation mainly in allocation (CV of A = 0.05, SD of p = 0.15): the trade-off is visible as a negative
correlation. Gray lines: the trade-off lines R + S = A of three individuals.
C: the correlation of R and S against the ratio CV(A) / SD(p) (points: simulation with 4000 individuals;
line: the covariance formula of the text, converted to a correlation).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 10.0)


def sample(cvA, sdp, n):
    A = 10 * rng.lognormal(-0.5 * np.log(1 + cvA**2), np.sqrt(np.log(1 + cvA**2)), n)
    p = np.clip(rng.normal(0.5, sdp, n), 0.01, 0.99)
    return p * A, (1 - p) * A


for k, (cvA, sdp, title, tok) in enumerate([(0.4, 0.03, "Acquisition varies", "dna"),
                                             (0.05, 0.15, "Allocation varies", "negative")]):
    pa = C.axes_at(ax, (2.0 + 10.0 * k, 1.6, 6.8, 6.8))
    R, S = sample(cvA, sdp, 400)
    for Aval in (6, 10, 14):
        pa.plot([0, Aval], [Aval, 0], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    pa.plot(R, S, "o", ms=2.5, color=Q.line_color(tok), alpha=0.7)
    r = np.corrcoef(R, S)[0, 1]
    pa.text(0.6, 14.2, f"r = {r:+.2f}", fontsize=FS["small"], color=P.ink())
    pa.set_xlim(0, 15)
    pa.set_ylim(0, 15)
    pa.set_aspect("equal")
    C.style_axes(pa, "reproduction R = pA", "survival or growth S = (1 - p)A")
    bio.panel(ax, "AB"[k], (0.5 + 10.0 * k, 9.6))
    bio.label(ax, (2.0 + 10.0 * k, 9.2), title, size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
sdp = 0.1
ratios = np.linspace(0.05, 3, 25)
sim = []
for q in ratios:
    R, S = sample(q * sdp, sdp, 4000)
    sim.append(np.corrcoef(R, S)[0, 1])
qq = np.linspace(0.05, 3, 200)
mp, vp = 0.5, sdp**2
cv2 = (qq * sdp) ** 2
cov = mp * (1 - mp) * cv2 - vp * (cv2 + 1)
varR = (vp + mp**2) * (cv2 + 1) - mp**2
varS = (vp + (1 - mp) ** 2) * (cv2 + 1) - (1 - mp) ** 2
pc.plot(qq, cov / np.sqrt(varR * varS), color=Q.line_color("protein"), lw=1.6)
pc.plot(ratios, sim, "o", ms=3.5, color=Q.line_color("enzyme"))
pc.axhline(0, color=P.muted(), lw=0.7)
pc.set_xlim(0, 3)
pc.set_ylim(-1, 1)
C.style_axes(pc, "CV of acquisition / SD of allocation", "correlation of R and S")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Which variation dominates", size="small", bold=True, ha="left")
