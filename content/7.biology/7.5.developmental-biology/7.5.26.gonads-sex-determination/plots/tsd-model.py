"""Temperature-dependent sex determination: reaction norms (patterns Ia and II), population sex ratio under
warming, and a temperature-shift experiment (model curves)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
T = np.linspace(22, 36, 300)
Tp, beta = 29.0, 1.5
male_Ia = 1 / (1 + np.exp(beta * (T - Tp)))
male_II = 1 / (1 + np.exp(-1.6 * (T - 31.0))) * 1 / (1 + np.exp(1.6 * (T - 34.0)))
fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.6))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.32)
a = axs[0]
a.plot(T, male_Ia, color=charts.line("dna"), lw=1.7, label="pattern Ia (turtle-like)")
a.plot(T, male_II, color=charts.line("drug"), lw=1.7, label="pattern II (crocodilian-like)")
a.axvline(Tp, color=P_.muted(), lw=0.8, ls=":")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
a.set_ylim(-0.03, 1.15)
charts.style_axes(a, "incubation temperature ($^\\circ$C)", "fraction male")
charts.title(a, "A  Reaction norms")
b = axs[1]
mus = np.linspace(26, 33, 200)
x = np.linspace(15, 45, 3000)
frac = []
for mu in mus:
    w = np.exp(-0.5 * ((x - mu) / 1.5) ** 2)
    frac.append(np.sum(w / (1 + np.exp(beta * (x - Tp)))) / np.sum(w))
frac = np.array(frac)
b.plot(mus, frac, color=charts.line("dna"), lw=1.7)
for dmu in (0.0, 1.5):
    v = np.interp(Tp + dmu, mus, frac)
    b.plot(Tp + dmu, v, "o", color=charts.line("drug"), ms=4)
    b.text(Tp + dmu + 0.15, v + 0.04, "%.0f%% males" % (100 * v), fontsize=FT["tiny"], color=P_.ink())
charts.style_axes(b, "mean nest temperature ($^\\circ$C)", "population fraction male")
charts.title(b, "B  Warming")
c = axs[2]
tt = np.linspace(0, 1, 200)
def committed(t):
    return 1 / (1 + np.exp(-(t - 0.5) / 0.05))
c.plot(tt, 1 - committed(tt), color=charts.line("drug"), lw=1.7, label="female after shift")
c.axvspan(1 / 3, 2 / 3, color=P_.light("highlight"), lw=0)
c.text(0.36, 0.55, "sensitive\nperiod", fontsize=FT["tiny"], color=P_.ink())
c.set_ylim(-0.03, 1.05)
charts.style_axes(c, "time of shift (fraction of incubation)", "fraction female")
charts.title(c, "C  Shift from cool to warm")
