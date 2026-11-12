# The sonar equation for a bat and an eared moth (Eq. 27.2; illustrative parameters). One-way level at the
# moth: Ls - 20 log10(r/r0) - alpha r; echo level at the bat: Ls - 2 (20 log10(r/r0) + alpha r) + St.
# Ls = 120 dB SPL at r0 = 0.1 m (loud aerial hawker) or 94 dB (whispering bat), alpha = 1 dB/m (about 40 kHz),
# moth threshold 60 dB, target strength St = -20 dB, bat echo threshold 20 dB.
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import quant

P = bio.P
r0, alpha, Tm, St, Tb = 0.1, 1.0, 60.0, -20.0, 20.0


def g(r):
    return 20 * np.log10(r / r0) + alpha * r


fig, ax = bio.canvas(24, 10)
for k, (Ls, title, x0) in enumerate(((120.0, "A  Loud bat (source level 120 dB)", 1.6),
                                     (94.0, "B  Whispering bat (94 dB)", 13.6))):
    r = np.linspace(0.12, 25 if k == 0 else 8, 400)
    xmax = 25 if k == 0 else 8
    p = quant.Plot(ax, (x0, 1.6, 9.4, 6.8), xlim=(0, xmax), ylim=(-20, 120),
                   xlabel="Distance between bat and moth r / m", ylabel="Sound level / dB SPL",
                   xticks=[0, 5, 10, 15, 20, 25] if k == 0 else [0, 2, 4, 6, 8], yticks=[0, 20, 40, 60, 80, 100, 120])
    one = Ls - g(r)
    echo = Ls - 2 * g(r) + St
    p.line(r, one, "enzyme", text="call at moth", at=0.75 if k == 0 else 0.85, dy=0.35)
    p.line(r, echo, "channel", dashed=True, text="echo at bat", at=0.3)
    p.hline(Tm, token="enzyme", text="moth threshold", size="tiny")
    p.hline(Tb, token="channel", text="bat threshold", size="tiny")
    rm = brentq(lambda x: Ls - g(x) - Tm, 0.11, 60)
    rb = brentq(lambda x: Ls - 2 * g(x) + St - Tb, 0.11, 60)
    for rr, tok, y in ((rm, "enzyme", Tm), (rb, "channel", Tb)):
        if rr < xmax:
            p.vline(rr, token=tok, dashed=True)
            p.points([rr], [y], tok, r=0.11)
    bio.label(ax, (x0 + 4.7, 9.25), title, size="small", bold=True)
    bio.label(ax, (x0 + 4.7, 8.75), "moth hears bat within %.1f m; bat detects moth within %.1f m" % (rm, rb),
              size="tiny", color=P.muted())
