# Temperature-dependent sex determination in a sea turtle (model with illustrative parameters close to
# published values for green turtles: pivotal temperature Tp = 29.3 C).
# Sex ratio reaction norm at constant temperature: proportion female p(T) = 1 / (1 + exp(-(T - Tp) / s)),
# s = 0.4 C, so that the transitional range (5-95% female) is Tp +/- s ln 19 = 28.1-30.5 C.
# In a fluctuating nest, T(t) = m + A sin(omega t), the sex-determining temperature is taken as the
# development-weighted mean temperature T_w = int T v(T) dt / int v(T) dt with a linear development rate
# v(T) = max(T - 22, 0) (an approximation to the "constant temperature equivalent" of Georges 1989).
# A: reaction norm and transitional range. B: proportion female against mean nest temperature for daily
# amplitudes of 0, 2 and 4 C; the dashed lines show the effect of warming the nest by 1 C from a mean of 28.5 C.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
Tp, s = 29.3, 0.4
ph = np.linspace(0, 2 * np.pi, 721)[:-1]


def pfem(T):
    return 1 / (1 + np.exp(-(T - Tp) / s))


def weighted(m, A):
    T = m + A * np.sin(ph)
    v = np.clip(T - 22, 0, None)
    return np.sum(T * v) / np.sum(v)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.2))
T = np.linspace(26, 33, 701)
lo, hi = Tp - s * np.log(19), Tp + s * np.log(19)
a.axvspan(lo, hi, color=P.light("highlight"), lw=0, alpha=0.45)
a.plot(T, pfem(T), color=P.edge("petal"), lw=2)
a.axvline(Tp, color=P.muted(), lw=0.8, ls="--")
a.text(Tp + 0.1, 0.06, "pivotal\ntemperature\n%.1f °C" % Tp, fontsize=7.5, color=P.muted())
a.text((lo + hi) / 2, 1.04, "transitional range %.1f–%.1f °C" % (lo, hi), ha="center", fontsize=7.5,
       color=P.edge("highlight"))
a.text(26.3, 0.08, "all male", fontsize=8, color=P.edge("dna"))
a.text(32.7, 0.9, "all female", fontsize=8, color=P.edge("petal"), ha="right")
a.set_xlim(26, 33)
a.set_ylim(0, 1.1)
a.set_xlabel("Constant incubation temperature / °C")
a.set_ylabel("Proportion female")
a.set_title("A  Reaction norm", loc="left", fontweight="bold")

means = np.linspace(26, 33, 281)
for A, tok in ((0, "ink"), (2, "atp"), (4, "negative")):
    pf = [pfem(weighted(m, A)) for m in means]
    col = P.ink() if tok == "ink" else P.edge(tok)
    b.plot(means, pf, color=col, lw=2, label="daily amplitude %d °C" % A)
for m0 in (28.5, 29.5):
    b.axvline(m0, color=P.muted(), lw=0.7, ls=":")
b.text(28.55, 0.92, "+1 °C", fontsize=7.5, color=P.muted())
b.set_xlim(26, 33)
b.set_ylim(0, 1.05)
b.set_xlabel("Mean nest temperature / °C")
b.set_ylabel("Proportion female")
b.legend(frameon=False, fontsize=7.5, loc="lower right")
b.set_title("B  Fluctuating nests", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
