"""Decline of the ovarian reserve (Formula 27.6.1). A: number of oocytes (non-growing follicles after birth) on a
log scale. Before birth germ cells rise to about 7 million at 20 weeks and fall to about 1 million at birth
(schematic, grey). After birth dN/dt = -lambda(N) N, with lambda rising from 0.097 to 0.237 per year as N falls
through about 25 000 (late thirties); menopause occurs when about 1000 follicles remain. Curves: median reserve
at birth and the 2.5 and 97.5 percentiles of a log-normal spread (sigma = 0.4). B: the predicted distribution of
the age at menopause (mean about 50 years, SD about 4); the tails below 40 and 45 years correspond to primary
ovarian insufficiency and early menopause."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
l1, l2, Ns, Nm = 0.097, 0.237, 25000.0, 1000.0


def lam(N):
    return l1 + (l2 - l1) / (1 + (N / Ns) ** 4)


def trajectory(N0, T=60, dt=0.02):
    t = np.arange(0, T, dt)
    N = np.empty_like(t)
    N[0] = N0
    for i in range(1, len(t)):  # exact in log N for small steps
        N[i] = N[i - 1] * np.exp(-lam(N[i - 1]) * dt)
    return t, N


def t_meno(N0):
    u = np.linspace(np.log(Nm), np.log(N0), 300)
    return np.trapezoid(1 / lam(np.exp(u)), u)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.88, wspace=0.25)
# fetal phase (schematic, years from birth)
tf = np.array([-0.62, -0.4, -0.25, 0.0])
nf = np.array([3e3, 7e6, 3e6, 1e6])
a.plot(tf, nf, color=P_.muted(), lw=1.4)
for z, tk, txt in ((-1.96, "receptor", "2.5th percentile"), (0, "protein", "median"), (1.96, "channel", "97.5th percentile")):
    N0 = 1e6 * np.exp(0.4 * z)
    t, N = trajectory(N0)
    m = N > 300
    a.plot(t[m], N[m], color=charts.line(tk), lw=1.7, label=f"{txt}: menopause at {t_meno(N0):.0f} y")
for y, txt in ((Ns, "about 25 000: faster loss"), (Nm, "about 1000: menopause")):
    a.axhline(y, color=P_.muted(), lw=0.7, ls=":")
    a.text(59, y * 1.25, txt, ha="right", fontsize=FT["tiny"], color=P_.muted())
a.set_yscale("log")
a.set_xlim(-1, 60)
a.set_ylim(300, 2e7)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.92))
charts.style_axes(a, "age / years", "oocytes per woman")
charts.title(a, "A  The ovarian reserve")
rng = np.random.default_rng(0)
ages = np.array([t_meno(x) for x in np.exp(np.log(1e6) + 0.4 * rng.standard_normal(4000))])
b.hist(ages, bins=np.arange(36, 66, 1.0), color=charts.line("protein"), alpha=0.75)
for x in (40, 45):
    b.axvline(x, color=P_.muted(), lw=0.8, ls="--")
b.text(39.5, b.get_ylim()[1] * 0.92, f"< 40: {100 * (ages < 40).mean():.1f}%", ha="right", fontsize=FT["tiny"], color=P_.ink())
b.text(45.5, b.get_ylim()[1] * 0.92, f"< 45: {100 * (ages < 45).mean():.0f}%", ha="left", fontsize=FT["tiny"], color=P_.ink())
charts.style_axes(b, "age at menopause / years", "women (of 4000)")
charts.title(b, "B  Predicted age at menopause")
