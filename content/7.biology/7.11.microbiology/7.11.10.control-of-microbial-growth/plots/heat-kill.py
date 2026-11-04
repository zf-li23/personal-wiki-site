# Kinetics of heat killing.
# A: survival curves of a mesophile at three temperatures, first-order death N(t) = N0 10^(-t/D), with the
#    decimal reduction times D = 42, 12 and 3 min at 50, 60 and 70 C (data from Madigan et al. 2019); on a
#    log scale each is a straight line and D is the time for one tenfold fall.
# B: D against temperature on a log scale (thermal death time curve). The mesophile points of A, and spores
#    of Clostridium botulinum with the classic canning parameters D(121.1 C) = 0.21 min and z = 10 C. A rise
#    of z degrees shortens D tenfold. The fitted z of the mesophile data is printed.
# C: a canning process. Temperature at the slowest-heating point of a can in a retort at 121 C (steam off at 42 min;
#    heating and cooling as first-order lags, time constants 12 and 6 min, illustrative), the lethal rate
#    L = 10^((T - 121.1)/z) with z = 10 C, and the accumulated lethality F0 = integral of L dt (minutes at
#    121.1 C). The process is adequate when F0 exceeds the 12D value for C. botulinum spores, 12 x 0.21 =
#    2.5 min (in practice F0 of at least about 3 min for low-acid foods).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(14.0, 4.2), gridspec_kw=dict(wspace=0.36))

# ---- A ------------------------------------------------------------------------------------------------
ax = axs[0]
data = [(50, 42.0, "dna"), (60, 12.0, "highlight"), (70, 3.0, "negative")]
t = np.linspace(0, 60, 300)
for T, D, tok in data:
    ax.plot(t, 1e7 * 10 ** (-t / D), color=charts.line(tok), lw=2.0, label=f"{T} $^\\circ$C: $D$ = {D:g} min")
ax.axhline(1e6, color=P.muted(), lw=0.7, ls=":")
ax.annotate("", xy=(12, 1e6), xytext=(0, 1e6), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.9))
ax.text(6, 1.4e6, "$D$", ha="center", fontsize=8, color=P.ink())
ax.set_yscale("log")
ax.set_ylim(1, 2e7)
ax.set_xlim(0, 60)
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(ax, "heating time / min", "survivors / mL$^{-1}$")
charts.title(ax, "A   Death is first order")

# ---- B ------------------------------------------------------------------------------------------------
ax = axs[1]
Tm = np.array([50, 60, 70.0])
Dm = np.array([42, 12, 3.0])
slope, icpt = np.polyfit(Tm, np.log10(Dm), 1)
zm = -1 / slope
TT = np.linspace(45, 75, 50)
ax.plot(Tm, Dm, "o", ms=5, color=charts.line("bacterium"))
ax.plot(TT, 10 ** (icpt + slope * TT), color=charts.line("bacterium"), lw=1.6, label=f"mesophile: $z$ = {zm:.0f} $^\\circ$C")
Ts = np.linspace(100, 130, 50)
Ds = 0.21 * 10 ** ((121.1 - Ts) / 10)
ax.plot(Ts, Ds, color=charts.line("negative"), lw=2.0, label="$C.\\ botulinum$ spores: $z$ = 10 $^\\circ$C")
ax.plot([121.1], [0.21], "o", ms=5, color=charts.line("negative"))
ax.text(122.5, 0.25, "$D_{121.1}$ = 0.21 min", fontsize=6.8, color=P.ink())
# z construction on the spore line
ax.plot([111.1, 121.1], [2.1, 2.1], color=P.muted(), lw=0.8)
ax.plot([121.1, 121.1], [2.1, 0.21], color=P.muted(), lw=0.8)
ax.text(116.1, 2.6, "$z$", ha="center", fontsize=8, color=P.ink())
ax.text(122.2, 0.7, "×1/10", fontsize=6.8, color=P.muted())
ax.set_yscale("log")
ax.set_ylim(0.03, 200)
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(ax, "temperature / $^\\circ$C", "$D$ / min")
charts.title(ax, "B   $D$ falls tenfold every $z$ degrees")

# ---- C ------------------------------------------------------------------------------------------------
ax = axs[2]
dt = 0.05
time = np.arange(0, 75, dt)
T0, Tr, Tc, t_off = 40.0, 121.0, 30.0, 42.0
temp = np.empty_like(time)
temp[0] = T0
for i in range(1, len(time)):
    target, tau = (Tr, 12.0) if time[i] < t_off else (Tc, 6.0)
    temp[i] = temp[i - 1] + (target - temp[i - 1]) * dt / tau
L = 10 ** ((temp - 121.1) / 10)
F0 = np.cumsum(L) * dt
ax.plot(time, temp, color=charts.line("negative"), lw=2.0)
ax.axhline(121, color=P.muted(), lw=0.7, ls=":")
ax.text(1, 123, "retort 121 $^\\circ$C", fontsize=6.8, color=P.muted())
charts.style_axes(ax, "time / min", "can centre $T$ / $^\\circ$C")
ax.set_ylim(20, 140)
ax2 = ax.twinx()
ax2.plot(time, F0, color=charts.line("dna"), lw=2.0, ls="--")
ax2.axhline(12 * 0.21, color=charts.line("dna"), lw=0.8, ls=":")
ax2.text(2, 12 * 0.21 + 0.15, "12$D$ = 2.5 min", fontsize=6.8, color=charts.line("dna"))
ax2.text(73, F0[-1] - 0.55, f"$F_0$ = {F0[-1]:.1f} min", ha="right", fontsize=7.2, color=charts.line("dna"))
ax2.set_ylim(0, max(6, F0[-1] * 1.25))
charts.style_axes(ax2, None, "accumulated lethality $F_0$ / min (dashed)")
ax2.spines["right"].set_visible(True)
charts.title(ax, "C   Lethality of a canning process")
