"""Model of the proliferative zone set by PTHrP-Ihh feedback: x_h = lam_P ln((a0 + a1 exp(-x_h/lam_I))/theta)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
lp, li, th = 1.0, 1.5, 1.0


def xh(a0, a1, theta=th):
    f = lambda x: x - lp * np.log((a0 + a1 * np.exp(-x / li)) / theta)
    if (a0 + a1) <= theta:
        return 0.0
    return brentq(f, 0.0, 20.0)


fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.6))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.19, top=0.86, wspace=0.34)
a = axs[0]
x = np.linspace(0, 4, 200)
for a1, tok, lab in ((20.0, "positive", "wild type"), (0.0, "negative", "no Ihh (a1 = 0)")):
    h = xh(3.0, a1)
    A = 3.0 + a1 * np.exp(-h / li)
    a.semilogy(x, A * np.exp(-x / lp), color=charts.line(tok), lw=1.7, label=lab)
    a.axvline(h, color=charts.line(tok), lw=0.9, ls="--")
a.axhline(th, color=P_.muted(), lw=0.9, ls=":")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, "distance from articular end x", "PTHrP P(x)")
charts.title(a, "A  PTHrP profile")

b = axs[1]
a0s = np.logspace(np.log10(1.2), np.log10(30), 60)
b.semilogx(a0s, [xh(v, 20.0) for v in a0s], color=charts.line("positive"), lw=1.7, label="with Ihh feedback")
b.semilogx(a0s, [xh(v, 0.0) for v in a0s], color=charts.line("negative"), lw=1.5, ls="--", label="without")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "basal PTHrP production a0", "proliferative zone x_h")
charts.title(b, "B  Buffering")

c = axs[2]
vals = [xh(3.0, 20.0), xh(3.0, 0.0), 0.0, xh(3.0, 20.0, theta=0.25)]
labs = ["wild\ntype", "Ihh\nnull", "PTHrP\nnull", "active\nPTH1R"]
toks = ["positive", "negative", "negative", "highlight"]
for i, (v, t) in enumerate(zip(vals, toks)):
    c.bar(i, max(v, 0.02), color=P_.fill(t), edgecolor=P_.edge(t), lw=0.8, width=0.6)
    c.text(i, max(v, 0.02) + 0.08, "%.2f" % v, ha="center", fontsize=FT["tiny"], color=P_.ink())
c.set_xticks(range(4))
c.set_xticklabels(labs, fontsize=FT["tiny"])
charts.style_axes(c, None, "zone length x_h")
charts.title(c, "C  Mutants")
