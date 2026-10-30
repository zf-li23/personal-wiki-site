"""Four dynamical motifs that recur through the course, each computed from its model.

A: a synthesis-diffusion-degradation gradient C = C0 exp(-x / lambda) read at two thresholds
   (Definition 11.4.1); doubling the source dose shifts every boundary by lambda ln 2.
B: dispersion relation of an activator-inhibitor system with Jacobian J = [[1, -1], [2, -1.5]]
   and diffusivities (1, d) (Theorem 12.3.1); the critical ratio is d = 4.5, k_c^2 = 1/3.
C: an irreversible switch dx/dt = s + 2 x^4 / (1 + x^4) - x (Proposition 11.7.1, Formula 26.2.1):
   the steady states against the signal s; a transient signal above the fold leaves the gene on.
D: a delayed negative feedback loop dx/dt = 1 / (1 + (x(t - T) / 0.5)^4) - x with T = 2
   (Formula 23.3.1): no oscillation without the delay, a sustained oscillation with it.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, axs = plt.subplots(1, 4, figsize=(14.0, 3.6))
fig.subplots_adjust(left=0.05, right=0.99, bottom=0.2, top=0.84, wspace=0.42)

# A: gradient and thresholds
a = axs[0]
x = np.linspace(0, 500, 400)
lam = 100.0
for c0, ls, tag in ((1.0, "-", "dose 1"), (2.0, (0, (4, 2)), "dose 2")):
    a.plot(x, c0 * np.exp(-x / lam), color=charts.line("dna"), lw=1.5, ls=ls)
for T, tok in ((0.3, "positive"), (0.05, "negative")):
    a.axhline(T, color=charts.line(tok), lw=0.9, ls=":")
    for c0, mk in ((1.0, "o"), (2.0, "s")):
        xb = lam * np.log(c0 / T)
        a.plot([xb], [T], mk, ms=4.5, color=charts.line(tok))
a.annotate("", xy=(lam * np.log(2 / 0.3), 0.36), xytext=(lam * np.log(1 / 0.3), 0.36),
           arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.8))
a.text(lam * np.log(1.4 / 0.3), 0.42, r"$\lambda\ln 2$", fontsize=FT["small"], color=P.ink(), ha="center")
a.text(300, 0.85, "solid: dose 1\ndashed: dose 2", fontsize=FT["tiny"], color=P.muted(), ha="left")
a.text(492, 0.31, "threshold 1", fontsize=FT["tiny"], color=charts.line("positive"), ha="right", va="bottom")
a.text(492, 0.06, "threshold 2", fontsize=FT["tiny"], color=charts.line("negative"), ha="right", va="bottom")
a.set_xlim(0, 500)
a.set_ylim(0, 1.25)
charts.style_axes(a, r"position $x$ / $\mu$m", r"$C / C_0$")
charts.title(a, "A  Gradient and thresholds")

# B: Turing dispersion relation
b = axs[1]
J = np.array([[1.0, -1.0], [2.0, -1.5]])
k2 = np.linspace(0, 1.2, 400)
for d, tok in ((3.0, "neutral"), (4.5, "enzyme"), (8.0, "negative")):
    s = [np.linalg.eigvals(J - np.diag([1.0, d]) * q).real.max() for q in k2]
    b.plot(k2, s, color=charts.line(tok), lw=1.5)
    j = int(np.argmax(s))
    b.text(k2[j] + 0.05, s[j] + 0.03, f"d = {d:g}", fontsize=FT["tiny"], color=charts.line(tok), ha="left", va="bottom")
b.axhline(0, color=P.muted(), lw=0.7)
b.plot([1 / 3], [0], "o", ms=4, color=charts.line("enzyme"))
b.text(1 / 3, -0.04, r"$k_c^2 = 1/3$", fontsize=FT["tiny"], color=P.ink(), ha="left", va="top")
b.set_xlim(0, 1.2)
b.set_ylim(-0.6, 0.35)
charts.style_axes(b, r"wavenumber squared $k^2$", r"growth rate $\sigma$")
charts.title(b, "B  Diffusion-driven instability")

# C: irreversible bistable switch
c = axs[2]
xs = np.linspace(0, 2.4, 3000)
sv = xs - 2 * xs**4 / (1 + xs**4)
dsv = np.gradient(sv, xs)
for mask, ls in ((dsv > 0, "-"), (dsv <= 0, (0, (3, 2)))):
    seg = np.where(mask, xs, np.nan)
    c.plot(np.where(mask, sv, np.nan), seg, color=charts.line("protein"), lw=1.6, ls=ls)
i_fold = np.argmax(np.where(xs < 1, sv, -1))
c.annotate("", xy=(sv[i_fold], 1.9), xytext=(sv[i_fold], xs[i_fold] + 0.08),
           arrowprops=dict(arrowstyle="->", color=charts.line("positive"), lw=1.0))
c.annotate("", xy=(0.03, 1.80), xytext=(0.36, 2.15),
           arrowprops=dict(arrowstyle="->", color=charts.line("negative"), lw=1.0))
c.text(0.42, 1.05, "switch on", fontsize=FT["tiny"], color=charts.line("positive"), ha="left")
c.text(0.03, 1.45, "signal removed:\nstays on", fontsize=FT["tiny"], color=charts.line("negative"), ha="left")
c.text(0.3, 0.2, "dashed: unstable", fontsize=FT["tiny"], color=P.muted(), ha="left")
c.set_xlim(0, 0.6)
c.set_ylim(0, 2.4)
charts.style_axes(c, r"signal $s$", r"steady state $x^*$")
charts.title(c, "C  Bistable switch with memory")

# D: delayed negative feedback
d_ax = axs[3]
dt, tmax, T = 0.005, 40.0, 2.0
n = int(tmax / dt)
lag = int(T / dt)
t = np.arange(n) * dt
for delay, tok, lab in ((0, "neutral", "no delay"), (lag, "dna", "delay T = 2")):
    y = np.full(n, 0.2)
    for i in range(max(delay, 1), n - 1):
        y[i + 1] = y[i] + dt * (1 / (1 + (y[i - delay] / 0.5) ** 4) - y[i])
    d_ax.plot(t, y, color=charts.line(tok), lw=1.4)
    d_ax.text(40.5, y[-1], lab, fontsize=FT["tiny"], color=charts.line(tok), ha="left", va="center")
d_ax.set_xlim(0, 50)
d_ax.set_ylim(0, 1.0)
charts.style_axes(d_ax, r"time / (1/b)", r"repressor level $x$")
charts.title(d_ax, "D  Delayed negative feedback")

for ax in axs:
    ax.tick_params(labelsize=FT["tiny"])
