# Scaling of hovering flight, representative values (body mass m, wing length R, wingbeat frequency f,
# stroke amplitude, single-wing area from typical published morphology; e.g. Ellington 1984, Dudley 2000,
# Bomphrey et al. 2017; not a fitted dataset). A: wingbeat frequency against wing length (log-log); the
# dashed line has slope -1/2 (geometric similarity). Insects with asynchronous flight
# muscle (filled) lie above the hawkmoth with synchronous muscle and the hummingbird (open). B: mass-specific induced power for
# hovering from actuator-disc (Rankine-Froude) momentum theory, P = sqrt(W^3 / (2 rho A)) with the swept
# area A = Phi R^2: P/m grows as the square root of the disc loading W/A.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rho, g = 1.2, 9.81
# name, m (kg), R (m), f (Hz), Phi (rad), asynchronous
D = [("Drosophila", 1.0e-6, 2.5e-3, 220, 2.6, True), ("Culex (mosquito)", 1.4e-6, 2.8e-3, 717, 0.68, True),
     ("Apis (honey bee)", 1.0e-4, 9.5e-3, 230, 1.6, True), ("Bombus (bumblebee)", 1.75e-4, 13e-3, 155, 2.0, True),
     ("Manduca (hawkmoth)", 1.6e-3, 48e-3, 25, 2.0, False), ("hummingbird", 3.4e-3, 45e-3, 50, 2.4, False)]
fig, ax = bio.canvas(24, 10)
bio.panel(ax, "A", (0.2, 9.7))
bio.panel(ax, "B", (12.4, 9.7))
a = charts.axes_at(ax, (2.0, 1.6, 8.8, 7.4))
b = charts.axes_at(ax, (14.4, 1.6, 8.8, 7.4))
for name, m, R, f, Phi, asyn in D:
    col = charts.line("negative" if asyn else "channel")
    a.scatter(R * 1e3, f, s=36, facecolor=col if asyn else "none", edgecolor=col, lw=1.2, zorder=5)
    a.text(R * 1e3 * 1.12, f * 1.04, name, fontsize=7, color=P.ink())
    A_ = Phi * R ** 2
    Pw = np.sqrt((m * g) ** 3 / (2 * rho * A_))
    b.scatter(m * 1e3, Pw / m, s=36, facecolor=col if asyn else "none", edgecolor=col, lw=1.2, zorder=5)
    b.text(m * 1e3 * 1.15, Pw / m * 1.02, name, fontsize=7, color=P.ink())
Rr = np.logspace(0.2, 1.9, 10)
a.plot(Rr, 220 * (2.5 / Rr) ** 0.5, color=P.muted(), ls=(0, (4, 3)), lw=1)
a.set_xscale("log"); a.set_yscale("log")
a.set_xlim(1.5, 150); a.set_ylim(10, 2000)
charts.style_axes(a, "Wing length R / mm", "Wingbeat frequency f / Hz")
b.set_xscale("log")
b.set_xlim(5e-4, 30); b.set_ylim(0, 22)
charts.style_axes(b, "Body mass m / g", "Induced power P/m / (W/kg)")
a.text(1.7, 13, "filled: asynchronous flight muscle\nopen: synchronous muscle (hawkmoth)\nor vertebrate muscle (hummingbird)",
       fontsize=7, color=P.muted(), va="bottom")
