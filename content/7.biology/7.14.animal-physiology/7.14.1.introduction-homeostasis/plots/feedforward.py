# Feedback, feedforward and both together, in the cruise-control example (dimensionless units).
# A car of unit mass: dv/dt = F - b v - s(t), with drag b = 1, set speed v* = 1 and a hill that adds the
# load s = 0.5 between t = 5 and t = 25 (time in units of the drag time constant 1/b).
# Feedback only: F = F0 + k_p (v* - v) + k_i * integral(v* - v), k_p = 2, k_i = 0.6. It acts only after
#   the speed has fallen, then returns it to v* (integral term).
# Feedforward only: F = F0 + s_hat, where the controller measures the slope and adds its estimate of
#   the load in advance; the estimate is imperfect (s_hat = 0.8 s), so an error remains that the
#   feedforward controller cannot see.
# Both: feedforward removes most of the disturbance at once, feedback removes the rest.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(13.0, 9.4)
dt = 0.005
t = np.arange(0, 40, dt)
s = np.where((t >= 5) & (t < 25), 0.5, 0.0)
F0 = 1.0


def run(ff, fb):
    v = np.empty_like(t)
    v[0] = 1.0
    integ = 0.0
    for i in range(1, t.size):
        e = 1.0 - v[i - 1]
        integ += dt * e
        F = F0 + (0.8 * s[i - 1] if ff else 0.0) + ((2.0 * e + 0.6 * integ) if fb else 0.0)
        v[i] = v[i - 1] + dt * (F - v[i - 1] - s[i - 1])
    return v


pa = charts.axes_at(ax, (2.0, 1.5, 10.4, 6.9))
pa.axvspan(5, 25, color=P.mix(P.muted(), P.surface(), 0.8), lw=0)
pa.text(15, 1.16, "uphill stretch (load)", fontsize=7.5, color=P.ink(), ha="center")
for ff, fb, tok, lab in ((False, False, "neutral", "no control"), (False, True, "dna", "feedback only"),
                         (True, False, "protein", "feedforward only"), (True, True, "positive", "feedforward + feedback")):
    pa.plot(t, run(ff, fb), color=charts.line(tok), lw=1.7, label=lab)
leg = pa.legend(loc="lower right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 40)
pa.set_ylim(0.45, 1.2)
charts.style_axes(pa, "time", "speed (set speed = 1)")
charts.title(pa, "Cruise control on a hill")
