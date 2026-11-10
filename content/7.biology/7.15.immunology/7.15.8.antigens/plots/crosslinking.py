# Epitope occupancy and receptor cross-linking (Eq. 8.1 of the page).
# An antigen with n identical, independent epitopes; each epitope is occupied with probability
# theta = c / (K_D + c). The antigen can bridge two receptors when at least two epitopes are occupied:
#   p(n, theta) = 1 - (1 - theta)^n - n theta (1 - theta)^(n - 1).
# A: p against c/K_D for several n.  B: the c/K_D at which p = 1/2 against n.
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P = bio.P


def p_bridge(n, theta):
    return 1 - (1 - theta) ** n - n * theta * (1 - theta) ** (n - 1)


fig, ax = bio.canvas(16.0, 7.0)

bio.panel(ax, "A", (0.1, 6.85))
bio.label(ax, (4.6, 6.7), "Antigens able to bridge two receptors", size="title", bold=True)
pa = quant.Plot(ax, (1.6, 1.2, 6.2, 4.8), xlim=(1e-3, 1e2), ylim=(0, 1), xlog=True,
                xlabel="free receptor concentration / $K_\\mathrm{D}$", ylabel="bridging fraction $p$",
                xticks=[(1e-3, "$10^{-3}$"), (1e-2, "$10^{-2}$"), (1e-1, "$10^{-1}$"), (1, "1"), (10, "10"), (100, "$10^{2}$")],
                yticks=[0, 0.5, 1], ylabel_offset=1.1)
c = np.logspace(-3, 2, 400)
theta = c / (1 + c)
items = []
for n, tok in ((1, "muted"), (2, "channel"), (5, "enzyme"), (10, "drug"), (30, "negative")):
    pa.line(c, p_bridge(n, theta), tok, lw=1.8)
    items.append((f"$n = {n}$" + (" (hapten)" if n == 1 else ""), tok, "-"))
pa.legend(items, (pa.X(8) , pa.Y(0.45)))
pa.hline(0.5, dashed=True)

bio.panel(ax, "B", (8.8, 6.85))
bio.label(ax, (12.8, 6.7), "Half-maximal bridging", size="title", bold=True)
pb = quant.Plot(ax, (10.2, 1.2, 5.2, 4.8), xlim=(2, 100), ylim=(1e-2, 10), xlog=True, ylog=True,
                xlabel="epitopes per antigen $n$", ylabel="$c/K_\\mathrm{D}$ at half-maximum", ylabel_offset=1.1,
                xticks=[(2, "2"), (5, "5"), (10, "10"), (30, "30"), (100, "100")],
                yticks=[(1e-2, "$10^{-2}$"), (1e-1, "$10^{-1}$"), (1, "1"), (10, "10")])
ns = np.arange(2, 101)
half = []
for n in ns:
    th = brentq(lambda t: p_bridge(n, t) - 0.5, 1e-6, 1 - 1e-9)
    half.append(th / (1 - th))
half = np.array(half)
pb.line(ns, half, "negative", lw=1.8)
pb.line(ns, 1.68 / ns, "muted", lw=1.0, dashed=True, text="$\\approx 1.7/n$", at=0.5, dy=0.35)
for n in (2, 10, 30):
    k = int(np.where(ns == n)[0][0])
    pb.points([n], [half[k]], "negative", r=0.09)
