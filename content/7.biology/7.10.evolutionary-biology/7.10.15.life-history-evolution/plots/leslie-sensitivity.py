"""Hamilton's forces of selection (Theorem 15.1.2).

Ages 0..25. Survival p = 0.4 at ages 0 and 1, then adult survival pa (0.7 or 0.9); fecundity m = 1.5 from
age 2. lambda solves sum lambda^-x l_x m_x = 1 (bisection); T = sum x lambda^-x l_x m_x.
Sensitivities: d lambda / d ln p_a = (lambda / T) sum_{x > a} lambda^-x l_x m_x; d lambda / d m_x =
lambda^(1 - x) l_x / T.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
X = np.arange(0, 41)


def life(pa):
    p = np.where(X < 2, 0.4, pa)
    l = np.concatenate([[1.0], np.cumprod(p)[:-1]])
    m = np.where(X >= 2, 1.5, 0.0)
    lo, hi = 0.01, 10.0
    for _ in range(100):
        lam = (lo + hi) / 2
        if (lam ** -X.astype(float) * l * m).sum() > 1:
            lo = lam
        else:
            hi = lam
    v = lam ** -X.astype(float) * l * m
    T = (X * v).sum()
    sp = np.array([lam / T * v[X > a].sum() for a in X])
    sm = lam ** (1 - X.astype(float)) * l / T
    sm[0] = np.nan  # m_0 does not enter the Euler-Lotka equation
    return lam, sp, sm


fig, ax = bio.canvas(30.0, 10.0)
res = [(0.7, P.ink()), (0.9, C.line("rna"))]
xs = np.arange(0, 21)
for k, (title, x0, idx, ylab) in enumerate((("Selection on survival", 2.2, 1, "∂λ / ∂ ln p_a"),
                                          ("Selection on fecundity", 17.5, 2, "∂λ / ∂m_x"))):
    p = C.axes_at(ax, (x0, 1.6, 11.0, 6.8))
    for pa, col in res:
        out = life(pa)
        p.plot(xs, out[idx][: len(xs)], "o-", ms=3, lw=1.5, color=col, label=f"adult survival {pa:g}, λ = {out[0]:.2f}")
    p.axvline(2, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    p.text(2.2, p.get_ylim()[1] * 0.97, "maturity", color=P.muted(), fontsize=FS["tiny"], va="top")
    p.set_xlim(-0.5, 20.5)
    p.set_ylim(bottom=0)
    C.style_axes(p, "age", ylab)
    p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, "AB"[k], (x0 - 2.0, 9.8))
    bio.label(ax, (x0, 9.4), title, size="small", bold=True, ha="left")
