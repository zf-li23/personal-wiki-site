"""Elementary hypercycle dx_i/dt = x_i (k_i x_{i-1} - phi): n = 3 approaches equilibrium, n = 5 oscillates;
a parasite catalysed by member 2 (k = 1.5) but catalysing nothing invades a 3-member cycle at t = 30."""
import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(27, 8)
TOK = ["dna", "rna", "positive", "protein", "highlight"]


def cycle(t, x, k):
    prev = np.roll(x, 1)
    g = k * prev
    return x * (g - np.sum(g * x))


axes = []
for j, (x0, title) in enumerate(((2.0, "A  n = 3"), (11.0, "B  n = 5"), (20.0, "C  n = 3 + parasite"))):
    a = charts.axes_at(ax, (x0, 1.6, 6.4, 5.6))
    charts.title(a, title)
    axes.append(a)

y0 = np.array([0.6, 0.3, 0.1])
s = solve_ivp(cycle, (0, 60), y0, args=(np.ones(3),), dense_output=True, rtol=1e-8)
tt = np.linspace(0, 60, 600)
for i in range(3):
    axes[0].plot(tt, s.sol(tt)[i], color=charts.line(TOK[i]), lw=1.5, label=f"member {i + 1}")
y0 = np.array([0.4, 0.25, 0.15, 0.12, 0.08])
s = solve_ivp(cycle, (0, 120), y0, args=(np.ones(5),), dense_output=True, rtol=1e-8)
tt = np.linspace(0, 120, 1200)
for i in range(5):
    axes[1].plot(tt, s.sol(tt)[i], color=charts.line(TOK[i]), lw=1.3)


def with_parasite(t, x):
    a1, a2, a3, p = x
    g = np.array([a1 * a3, a2 * a1, a3 * a2, 1.5 * p * a2])
    return g - x * g.sum()


s1 = solve_ivp(cycle, (0, 30), np.array([0.6, 0.3, 0.1]), args=(np.ones(3),), dense_output=True, rtol=1e-8)
xs = s1.sol(30)
start = np.r_[xs * 0.99, 0.01]
s2 = solve_ivp(with_parasite, (30, 120), start, dense_output=True, rtol=1e-8)
t1 = np.linspace(0, 30, 300)
t2 = np.linspace(30, 120, 900)
for i in range(3):
    axes[2].plot(np.r_[t1, t2], np.r_[s1.sol(t1)[i], s2.sol(t2)[i]], color=charts.line(TOK[i]), lw=1.4)
axes[2].plot(t2, s2.sol(t2)[3], color=charts.line("negative"), lw=1.8, label="parasite")
axes[2].axvline(30, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
for a, xl in zip(axes, (60, 120, 120)):
    a.set_xlim(0, xl)
    a.set_ylim(0, 1)
    charts.style_axes(a, "time", "relative concentration")
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
axes[2].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
