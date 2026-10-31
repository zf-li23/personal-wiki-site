# A. F. Huxley's 1957 cross-bridge model. A cross-bridge at distance x from its equilibrium position (units of h,
# the range of attachment) attaches at f(x) = f1 x/h for 0 < x < h and detaches at g(x) = g1 x/h for x > 0 and
# g2 for x < 0; an attached bridge pulls with the spring force k x. With Huxley's ratios g1/f1 = 3/13 and
# g2/(f1 + g1) = 3.919, the steady state n(x) at shortening velocity v solves -v dn/dx = f(1 - n) - g n.
# A: n(x) at four velocities (v in units of h (f1 + g1)/2 per half-sarcomere); B: the force-velocity relation
# (tension relative to isometric) with the best-fitting Hill hyperbola (Definition 27.7.1) and the mechanical
# power; C: rate of ATP splitting (one ATP per attachment) relative to isometric: energy liberation rises with
# velocity (the Fenn effect).
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq, curve_fit

import wikibio as bio
from wikibio import charts

P = bio.P
f1 = 1.0
g1 = 3 / 13 * f1
g2 = 3.919 * (f1 + g1)
phi = (f1 + g1) / 2
x = np.linspace(-1.5, 1.0, 1251)
f = np.where((x >= 0) & (x <= 1), f1 * x, 0.0)
g = np.where(x >= 0, g1 * x, g2)


def profile(v):
    """n(x) by exact exponential integration from x = 1 (n = 0) downward on the grid."""
    if v == 0:
        return np.where((x >= 0) & (x <= 1), f1 / (f1 + g1), 0.0)
    n = np.zeros_like(x)
    for i in range(len(x) - 1, 0, -1):
        dx = x[i] - x[i - 1]
        fi, gi = 0.5 * (f[i] + f[i - 1]), 0.5 * (g[i] + g[i - 1])
        lam = (fi + gi) / v
        neq = fi / (fi + gi) if fi + gi > 0 else 0.0
        n[i - 1] = neq + (n[i] - neq) * np.exp(-lam * dx)  # moving to smaller x relaxes n toward f/(f + g)
    return n


def tension(v):
    return np.trapezoid(x * profile(v), x)


def atp_rate(v):
    return np.trapezoid(f * (1 - profile(v)), x)


T0 = tension(0.0)
vmax = brentq(tension, 0.3, 5.0)
vs = np.linspace(0, vmax, 60)
T = np.array([tension(v) for v in vs]) / T0
A_fit = curve_fit(lambda Tn, A: vmax * A * (1 - Tn) / (Tn + A), T, vs, p0=[0.25])[0][0]

fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
for v, tok in ((0.0, "muscle"), (0.3 * phi, "enzyme"), (1.0 * phi, "dna"), (3.0 * phi, "rna")):
    ax.plot(x, profile(v), color=charts.line(tok), lw=1.8, label=f"$v$ = {v / phi:.1f}")
ax.axvspan(0, 1, color=P.fill("highlight"), alpha=0.25, lw=0)
ax.text(0.5, 0.92, "attachment\nzone $0<x<h$", ha="center", fontsize=7.5, color=P.ink())
ax.text(-1.45, 0.55, "negatively strained\nbridges resist", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 1.0)
ax.legend(fontsize=7.5, frameon=False, loc="upper left", title="velocity", title_fontsize=7.5)
charts.style_axes(ax, "bridge position $x/h$", "fraction attached $n(x)$")
charts.title(ax, "A   Fewer, less strained bridges when fast")

ax = axs[1]
Tn = np.linspace(0, 1, 200)
ax.plot(T, vs / vmax, color=charts.line("muscle"), lw=2.0, label="Huxley model")
ax.plot(Tn, A_fit * (1 - Tn) / (Tn + A_fit), color=P.muted(), lw=1.0, ls="--", label=f"Hill, $a/F_0$ = {A_fit:.2f}")
ax.plot(T, T * vs / vmax * 4, color=charts.line("enzyme"), lw=1.2, label="power (×4)")
ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.02)
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "tension $F/F_0$", "velocity $v/v_\\max$")
charts.title(ax, "B   A hyperbolic force–velocity curve")

ax = axs[2]
vr = np.linspace(0, vmax, 40)
ax.plot(vr / vmax, [atp_rate(v) / atp_rate(0) for v in vr], color=charts.line("atp"), lw=2.0)
ax.set_xlim(0, 1)
charts.style_axes(ax, "velocity $v/v_\\max$", "ATP turnover / isometric")
charts.title(ax, "C   Shortening costs more ATP (Fenn effect)")
fig.tight_layout()
