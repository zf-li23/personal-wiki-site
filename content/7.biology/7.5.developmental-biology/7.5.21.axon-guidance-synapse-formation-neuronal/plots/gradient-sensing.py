"""Physical limits on gradient sensing by a growth cone (Formula 21.4.1). (A) The smallest fractional difference in
concentration across the growth cone that can be detected with signal-to-noise ratio 1, as a function of the
concentration c relative to the dissociation constant K of the receptor, for 5000 receptors on each half of the
cone and M independent readings (M = T / tau: averaging time over receptor correlation time). Sensitivity is best
at c = K and is lost when receptors are nearly empty or nearly saturated. (B) A growth cone 10 µm wide in an
exponential gradient with decay length 200 µm experiences a fractional difference of 5% everywhere; it can read
the gradient only where the threshold of (A) is below 5%, which limits guidance to a window of distances from
the source (c0 = 1000 K at the source; shaded: detectable for M = 50)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
Nh = 5000
c = np.logspace(-3, 3, 400)
p = c / (1 + c)


def dmin(M):
    return np.sqrt(2.0 / (Nh * M * p * (1 - p)))


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.3)
for M, tok in ((1, "neutral"), (50, "receptor"), (1000, "protein")):
    a.loglog(c, dmin(M), color=charts.line(tok), lw=1.6, label=f"M = {M}")
a.axhline(0.05, color=P_.muted(), lw=0.8, ls="--")
a.text(1.5e-3, 0.058, "5% across the cone", fontsize=FT["tiny"], color=P_.muted())
a.axvline(1.0, color=P_.muted(), lw=0.6, ls=":")
a.set_ylim(1e-3, 3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper center")
charts.style_axes(a, "concentration c / K", "minimum detectable dc / c")
charts.title(a, "A  Detection threshold")

lam, w, c0 = 200.0, 10.0, 1000.0
x = np.linspace(0, 3000, 600)
cx = c0 * np.exp(-x / lam)
px = cx / (1 + cx)
thr = np.sqrt(2.0 / (Nh * 50 * px * (1 - px)))
b.semilogy(x, thr, color=charts.line("receptor"), lw=1.6, label="threshold (M = 50)")
b.axhline(w / lam, color=P_.muted(), lw=1.0, ls="--", label="signal a / lambda = 5%")
ok = thr < w / lam
b.fill_between(x, 1e-3, 10, where=ok, color=P_.fill("positive"), alpha=0.35, lw=0)
b.set_ylim(2e-3, 3)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "distance from source / µm", "dc / c")
charts.title(b, "B  Guidance window")
