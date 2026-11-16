"""The Gurney-Blythe-Nisbet model of Nicholson's blowflies.

dA/dt = P A(t - tau) exp(-A(t - tau) / A0) - delta A(t): adults A recruited after a development delay
tau with a hump-shaped (Ricker-type) dependence on the adult density tau days earlier, and dying at
per capita rate delta. Illustrative parameters of the magnitude estimated for Lucilia cuprina cultures
(tau = 15 d, P = 8 per day, delta = 0.175 per day, A0 = 600 flies). Euler integration with step 0.01 d,
constant history A = 200. A: adults over 400 days; the cycle has a period of about 2.7 tau, with a
shoulder on the rising limb and a long trough, and never comes near extinction. B: the same cycle
plotted against the density one delay earlier (a delay-coordinate phase portrait): high densities
tau days ago mean low recruitment now (overcompensation), which drives the crash.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P_ = bio.P
FS = bio.core.FONT
tau, Pr, delta, A0 = 15.0, 8.0, 0.175, 600.0
dt = 0.01
lag = int(round(tau / dt))
n = int(400 / dt)
A = np.empty(n + lag + 1)
A[: lag + 1] = 200.0
for k in range(lag, lag + n):
    Ad = A[k - lag]
    A[k + 1] = A[k] + dt * (Pr * Ad * np.exp(-Ad / A0) - delta * A[k])
t = (np.arange(n + lag + 1) - lag) * dt
t, A, Alag = t[lag:], A[lag:], A[:-lag] if lag else A
Alag = Alag[: len(A)]
Astar = A0 * np.log(Pr / delta)

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 15.5, 6.8))
pa.plot(t, A, color=Q.line_color("negative"), lw=1.2)
pa.axhline(Astar, color=P_.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(398, Astar + 250, "equilibrium A*", fontsize=FS["tiny"], color=P_.muted(), ha="right")
tt, AA = t[t > 200], A[t > 200]
pk = np.where((AA[1:-1] > AA[:-2]) & (AA[1:-1] > AA[2:]) & (AA[1:-1] > 0.6 * AA.max()))[0] + 1
per = np.diff(tt[pk]).mean()
pa.text(5, A.max() * 1.02, f"period = {per:.0f} d = {per / tau:.1f} tau", fontsize=FS["tiny"], color=P_.muted(),
        va="bottom")
pa.set_xlim(0, 400)
pa.set_ylim(0, A.max() * 1.12)
C.style_axes(pa, "time / days", "adults A(t)")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Sustained cycles of adult blowflies", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (21.5, 1.6, 7.0, 6.8))
sel = t > 200
pb.plot(Alag[sel], A[sel], color=Q.line_color("dna"), lw=1.0)
pb.set_xlim(0, Alag[sel].max() * 1.05)
pb.set_ylim(0, A[sel].max() * 1.1)
C.style_axes(pb, "A(t - tau)", "A(t)")
bio.panel(ax, "B", (19.8, 9.6))
bio.label(ax, (21.5, 9.2), "Delay-coordinate portrait", size="small", bold=True, ha="left")
