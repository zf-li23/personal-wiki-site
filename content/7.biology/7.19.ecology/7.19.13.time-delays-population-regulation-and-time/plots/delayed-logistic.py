"""Solutions of the delayed logistic (Hutchinson) equation dN/dt = r N(t) (1 - N(t - T) / K).

Time is measured in units of 1/r and N in units of K, so the only parameter is the product rT.
History: N(t) = 0.1 for -T <= t <= 0. Integration by the explicit Euler method with step 0.001
(the delay is an integer number of steps). The four panels show the four regimes of Theorem 13.1.1:
monotone approach (rT < 1/e), damped oscillation (1/e < rT < pi/2, two examples) and a stable limit
cycle (rT > pi/2), whose period is close to 4T near the threshold and grows with rT.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT


def hutchinson(a, t_end=40.0, dt=0.001, n0=0.1):
    lag = int(round(a / dt))
    n = int(t_end / dt)
    N = np.empty(n + lag + 1)
    N[: lag + 1] = n0
    for k in range(lag, lag + n):
        N[k + 1] = N[k] + dt * N[k] * (1.0 - N[k - lag])
    t = (np.arange(n + lag + 1) - lag) * dt
    return t[lag:], N[lag:]


cases = [
    (0.3, "rT = 0.3 < 1/e: monotone", "enzyme"),
    (1.0, "rT = 1.0: damped oscillation", "dna"),
    (1.5, "rT = 1.5 (just below pi/2)", "protein"),
    (2.0, "rT = 2.0 > pi/2: limit cycle", "negative"),
]

fig, ax = bio.canvas(30.0, 16.0)
for k, (a, title, tok) in enumerate(cases):
    col, row = k % 2, k // 2
    x0, y0 = 2.0 + 15.0 * col, 9.6 - 8.0 * row
    pa = C.axes_at(ax, (x0, y0, 12.0, 5.2))
    t, N = hutchinson(a)
    pa.plot(t, N, color=Q.line_color(tok), lw=1.5)
    pa.axhline(1.0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    pa.set_xlim(0, 40)
    pa.set_ylim(0, {0.3: 1.5, 1.0: 1.5, 1.5: 2.2, 2.0: 3.7}[a])
    C.style_axes(pa, "time rt" if row == 1 else None, "N / K")
    bio.panel(ax, "ABCD"[k], (x0 - 1.6, y0 + 6.1))
    bio.label(ax, (x0, y0 + 5.8), title, size="small", bold=True, ha="left")
    if a >= 1.9:
        # measure the period of the cycle from successive maxima
        tt, NN = t[t > 20], N[t > 20]
        peaks = np.where((NN[1:-1] > NN[:-2]) & (NN[1:-1] > NN[2:]))[0] + 1
        per = np.diff(tt[peaks]).mean()
        pa.text(39, 3.65, f"period = {per:.1f}/r = {per / a:.1f} T", fontsize=FS["tiny"], color=P.muted(),
                ha="right", va="top")
