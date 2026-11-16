# Three models of limitation by two resources, N and P (dimensionless supplies, illustrative parameters).
#   Liebig:          y = min(N / (1 + N), 1.5 P / (1 + 1.5 P))   (the scarcer factor alone sets yield)
#   multiplicative:  y = [N / (1 + N)] * [1.5 P / (1 + 1.5 P)]   (each factor scales the effect of the other)
#   additive:        y = 0.5 [N / (1 + N) + 1.5 P / (1 + 1.5 P)] (factors substitute for each other)
# Top row: isoclines of equal yield in the (N, P) plane. Bottom: yield against N at two fixed levels of P,
# showing Liebig's plateau set by P (Blackman's limiting factor) and the smooth co-limitation of the others.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P_ = bio.P


def f(N):
    return N / (1 + N)


def g(Pv):
    return 1.5 * Pv / (1 + 1.5 * Pv)


models = [
    ("Liebig (minimum)", lambda N, Pv: np.minimum(f(N), g(Pv))),
    ("multiplicative", lambda N, Pv: f(N) * g(Pv)),
    ("additive", lambda N, Pv: 0.5 * (f(N) + g(Pv))),
]
n = np.linspace(0, 6, 301)
NN, PP = np.meshgrid(n, n)
fig, axs = plt.subplots(2, 3, figsize=(11.2, 6.6), gridspec_kw={"height_ratios": [1.15, 1]})
for k, (name, fn) in enumerate(models):
    a = axs[0, k]
    lev = [0.2, 0.4, 0.55, 0.7] if k < 2 else [0.4, 0.55, 0.7, 0.8]
    cs = a.contour(NN, PP, fn(NN, PP), levels=lev, colors=[P_.edge("plant")], linewidths=1.4)
    a.clabel(cs, fmt="%.2f", fontsize=7, colors=[P_.edge("plant")])
    a.set_title(name, fontsize=10, color=P_.ink())
    a.set_xlabel("Nitrogen supply N")
    if k == 0:
        a.set_ylabel("Phosphorus supply P")
    b = axs[1, k]
    for pv, tok in ((0.6, "negative"), (3.0, "dna")):
        b.plot(n, fn(n, pv), color=P_.edge(tok), lw=2, label="P = %.1f" % pv)
    b.set_ylim(0, 1)
    b.set_xlabel("Nitrogen supply N")
    if k == 0:
        b.set_ylabel("Yield (relative)")
        b.legend(frameon=False, fontsize=8, loc="lower right")
    for ax in (a, b):
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
fig.tight_layout()
