# Receptor activation with desensitization under pulsatile versus continuous stimulation.
# Model (time in minutes):
#   dRa/dt = kon C (1 - Ra) - koff Ra          (Ra: fraction of receptors occupied/active)
#   dD/dt  = kd Ra (1 - D) - kr D              (D: fraction desensitized, 0..1)
#   effective signal S = Ra (1 - D)
# Hormone C(t) (units of its Kd = koff/kon): either 6-min square pulses of height 10 every 60 min,
# or a continuous infusion with the same mean (1.0). Rates: kon = 1 /min per unit C, koff = 1 /min,
# kd = 0.2 /min, kr = 0.03 /min (recovery half-time ~23 min). The cell's output is a
# threshold-like function of the signal, R = S^4 / (S^4 + 0.3^4) (e.g. LH release); its time integral is printed. Illustrative values in the spirit of
# GnRH acting on gonadotrophs (hourly pulses restore LH output; continuous GnRH suppresses it).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
dt = 0.01
t = np.arange(0, 600, dt)
kon, koff, kd, kr = 1.0, 1.0, 0.2, 0.03
pulse = np.where((t % 60.0) < 6.0, 10.0, 0.0)
cont = np.full_like(t, pulse.mean())


def run(C):
    Ra = np.zeros_like(t)
    D = np.zeros_like(t)
    for i in range(1, t.size):
        Ra[i] = Ra[i - 1] + dt * (kon * C[i - 1] * (1 - Ra[i - 1]) - koff * Ra[i - 1])
        D[i] = D[i - 1] + dt * (kd * Ra[i - 1] * (1 - D[i - 1]) - kr * D[i - 1])
    return Ra, D, Ra * (1 - D)


fig, ax = bio.canvas(24.0, 9.6)
for col, (C, lab, letter) in enumerate(((pulse, "Hourly pulses (mean 1)", "A"),
                                        (cont, "Continuous infusion (same mean)", "B"))):
    x0 = 2.2 + 12.4 * col
    bio.panel(ax, letter, (x0 - 2.0, 9.5))
    p = charts.axes_at(ax, (x0, 1.5, 8.8, 6.9))
    Ra, D, S = run(C)
    th = t / 60.0
    p.fill_between(th, 0, C / 10.0, color=P.mix(charts.line("receptor"), P.surface(), 0.7), lw=0)
    p.plot(th, Ra, color=charts.line("dna"), lw=1.1)
    p.plot(th, D, color=charts.line("negative"), lw=1.5, ls="--")
    p.plot(th, S, color=charts.line("positive"), lw=1.8)
    p.set_xlim(0, 10)
    p.set_ylim(0, 1.05)
    charts.style_axes(p, "time / h", "fraction")
    charts.title(p, lab)
    R = S ** 4 / (S ** 4 + 0.3 ** 4)
    area = R.sum() * dt
    p.axhline(0.3, color=P.muted(), lw=0.7, ls=":")
    p.text(0.15 if col else 9.9, 0.31, "output threshold", fontsize=6.8, color=P.muted(),
           ha="left" if col else "right", va="bottom")
    p.text(9.9, 1.0, f"output ∫R dt = {area:.0f} min", fontsize=7.3, color=charts.line("positive"), ha="right",
           va="top")
    if col == 0:
        p.text(0.15, 0.93, "hormone (scaled)", fontsize=7.0, color=P.muted())
    p.text(9.9, (D[-1] + 0.03) if col else 0.42, "desensitized D", fontsize=7.2, color=charts.line("negative"), ha="right",
           va="bottom")
    p.text(9.9, S[-1] - 0.03 if col else 0.82, "effective signal S", fontsize=7.2,
           color=charts.line("positive"), ha="right", va="top")
    p.text(9.9, Ra[-1] - 0.03 if col else 0.92, "active Ra", fontsize=7.2, color=charts.line("dna"),
           ha="right", va="top" if col else "bottom")
