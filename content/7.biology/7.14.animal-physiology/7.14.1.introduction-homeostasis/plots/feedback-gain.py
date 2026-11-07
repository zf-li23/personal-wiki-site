# Negative feedback: how the loop gain sets the residual error, and why delay limits the gain.
# Model (dimensionless): a regulated variable x obeys tau dx/dt = -x + D(t) + u, with a step
# disturbance D = 1 applied at t = 1 (time in units of tau).
# A: proportional control u = G x (G <= 0): the steady error is D / (1 - G), so a disturbance is
#    reduced to 1/3 for G = -2 (arterial baroreflex) and to 1/34 for G = -33 (body temperature in
#    moderate cold); integral control du/dt = -k_i x removes the error completely.
# B: the same loop with a feedback delay T_d = 0.4 tau: u(t) = G x(t - T_d). A modest gain settles,
#    a higher gain (G = -3.5) rings, and G = -5 oscillates with growing amplitude.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)
dt = 0.001
t = np.arange(0, 8, dt)
D = (t >= 1).astype(float)


def run_prop(G, delay=0.0):
    x = np.zeros_like(t)
    lag = int(round(delay / dt))
    for i in range(1, t.size):
        xd = x[i - 1 - lag] if i - 1 - lag >= 0 else 0.0
        x[i] = x[i - 1] + dt * (-x[i - 1] + D[i - 1] + G * xd)
    return x


def run_integral(ki):
    x = np.zeros_like(t)
    u = 0.0
    for i in range(1, t.size):
        u += dt * (-ki * x[i - 1])
        x[i] = x[i - 1] + dt * (-x[i - 1] + D[i - 1] + u)
    return x


# ---- A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
cases = [(0, "no feedback (G = 0)", "neutral"), (-2, "G = −2", "dna"), (-10, "G = −10", "protein"),
         (-33, "G = −33", "rna")]
for G, lab, tok in cases:
    x = run_prop(G)
    pa.plot(t, x, color=charts.line(tok), lw=1.7)
    if G == -33:
        pa.text(2.2, -0.07, lab, color=charts.line(tok), fontsize=7.5, ha="left", va="center")
    else:
        pa.text(7.9, x[-1] + 0.03, lab, color=charts.line(tok), fontsize=7.5, ha="right", va="bottom")
xi = run_integral(1.5)
pa.plot(t, xi, color=charts.line("positive"), lw=1.7, ls="--")
pa.text(5.4, -0.2, "integral control: error → 0", color=charts.line("positive"), fontsize=7.5)
pa.axhline(0, color=P.muted(), lw=0.7)
pa.annotate("", (1, 1.12), (1, 1.32), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
pa.text(1.12, 1.24, "step disturbance", fontsize=7.5, color=P.ink(), va="center")
pa.set_xlim(0, 8)
pa.set_ylim(-0.25, 1.4)
charts.style_axes(pa, "time / τ", "deviation x (disturbance = 1)")
charts.title(pa, "Residual error = 1 / (1 − G)")

# ---- B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
for G, tok, lab in ((-2, "dna", "G = −2: settles"), (-3.5, "protein", "G = −3.5: rings"), (-5, "rna", "G = −5: unstable")):
    x = run_prop(G, delay=0.4)
    pb.plot(t, x, color=charts.line(tok), lw=1.6, label=lab)
leg = pb.legend(loc="lower left", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.axhline(0, color=P.muted(), lw=0.7)
pb.set_xlim(0, 8)
pb.set_ylim(-0.9, 1.4)
charts.style_axes(pb, "time / τ", "deviation x")
charts.title(pb, "Same loop with a delay of 0.4 τ")
