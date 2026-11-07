"""Total cross-sectional area, mean velocity and blood pressure along the systemic circulation.

Areas (cm^2) of each vessel class for an adult (Guyton & Hall): aorta 2.5, small arteries 20, arterioles 40,
capillaries 2500, venules 250, small veins 80, venae cavae 8. Flow F = 5 L/min = 83 mL/s is the same through
every cross-section (continuity), so the mean velocity is v = F / A: 33 cm/s in the aorta, 0.03 cm/s in capillaries.
Pressure: schematic mean values, with the systolic-diastolic band damped out in the small arteries and arterioles.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P

names = ["Aorta", "Small\narteries", "Arterioles", "Capillaries", "Venules", "Small\nveins", "Venae\ncavae"]
area = np.array([2.5, 20, 40, 2500, 250, 80, 8])
F = 5000 / 60  # mL/s
vel = F / area
x = np.arange(len(names))

fig, axs = plt.subplots(3, 1, figsize=(8.5, 8.2), sharex=True)
ax, bx, cx = axs
ax.bar(x, area, color=P.fill("neutral"), edgecolor=P.edge("neutral"), width=0.6)
ax.set_yscale("log")
ax.set_ylim(1, 1e4)
ax.set_ylabel("Total cross-sectional\narea / cm$^2$")
for xi, a in zip(x, area):
    ax.text(xi, a * 1.3, f"{a:g}", ha="center", va="bottom", fontsize=8)
ax.set_title("A  Area: the capillary bed is about 1000 times the aorta", loc="left", fontsize=10)

bx.plot(x, vel, "o-", color=P.edge("blood"), lw=2)
bx.set_yscale("log")
bx.set_ylim(0.01, 100)
bx.set_ylabel("Mean velocity\n/ cm s$^{-1}$")
for xi, v in zip(x, vel):
    bx.text(xi + 0.08, v * 1.4, f"{v:.2g}", fontsize=8)
bx.set_title("B  Velocity v = F/A (F = 83 mL/s everywhere)", loc="left", fontsize=10)

# schematic pressure profile on a finer grid
s = np.linspace(-0.3, 6.3, 800)
knots_x = [-0.3, 0.3, 1.0, 1.6, 2.4, 2.7, 3.3, 3.8, 4.5, 5.5, 6.3]
knots_m = [100, 98, 93, 85, 38, 33, 15, 11, 8, 4, 1]
mean = np.interp(s, knots_x, knots_m)
amp = np.interp(s, [-0.3, 0.3, 1.0, 2.0, 2.6, 6.3], [22, 24, 18, 4, 0, 0])
cx.fill_between(s, mean - amp * 0.75, mean + amp, color=P.fill("blood"), alpha=0.35, lw=0, label="systolic-diastolic range")
t = np.linspace(-0.3, 2.6, 600)
osc = np.interp(t, knots_x, knots_m) + np.interp(t, [-0.3, 0.3, 1.0, 2.0, 2.6], [22, 24, 18, 4, 0]) * np.sin(2 * np.pi * t / 0.22)
cx.plot(t, osc, color=P.edge("blood"), lw=0.8, alpha=0.7)
cx.plot(s, mean, color=P.ink(), lw=2, label="mean pressure")
cx.set_ylim(0, 130)
cx.set_ylabel("Pressure / mmHg")
sec = cx.secondary_yaxis("right", functions=(lambda p: p * 0.1333, lambda k: k / 0.1333))
sec.set_ylabel("kPa")
cx.legend(frameon=False, fontsize=8, loc="upper right")
cx.annotate("steepest fall:\narterioles", xy=(2.0, 62), xytext=(3.0, 85), fontsize=8,
            arrowprops=dict(arrowstyle="->", color=P.muted()), color=P.muted())
cx.set_title("C  Pressure: the resistance sits in the arterioles", loc="left", fontsize=10)
cx.set_xticks(x)
cx.set_xticklabels(names, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3, axis="y")
fig.tight_layout()
