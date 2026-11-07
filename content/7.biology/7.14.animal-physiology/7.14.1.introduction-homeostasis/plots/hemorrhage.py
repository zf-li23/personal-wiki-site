# A minimal model of the positive feedback loop after haemorrhage (illustrative parameters).
# Arterial pressure P (1 = normal) is set by the effective blood volume V (1 = normal) times the pumping
# ability of the heart h(P), and the heart's pumping ability depends on its own coronary perfusion, i.e.
# on P:  tau dP/dt = V h(P) - P,  with h(P) = a P^2 / (P^2 + K^2), a = 1.12, K = 0.35 (so h(1) = 1).
# Besides P = 0, fixed points satisfy P^2 - a V P + K^2 = 0; they exist only for V >= 2K/a = 0.625.
# A: the rate dP/dt against P for V = 1, 0.8 and 0.6. For V = 0.8 there is a stable point (filled) and a
#    threshold (open circle); for V = 0.6 the only fixed point is collapse at P = 0.
# B: time courses after an abrupt loss of 20% (about 1 L of 5 L) or 40% (about 2 L) of the blood volume:
#    the first recovers to a lower pressure (other negative feedbacks then restore it); the second
#    enters the vicious cycle.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
A, K = 1.12, 0.35
fig, ax = bio.canvas(24.0, 9.4)


def h(p):
    return A * p**2 / (p**2 + K**2)


# ---- A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
p = np.linspace(0, 1.2, 400)
for V, tok in ((1.0, "dna"), (0.8, "protein"), (0.6, "rna")):
    pa.plot(p, V * h(p) - p, color=charts.line(tok), lw=1.7, label=f"V = {V:.1f}")
    disc = (A * V) ** 2 - 4 * K**2
    if disc > 0:
        hi = (A * V + np.sqrt(disc)) / 2
        lo = (A * V - np.sqrt(disc)) / 2
        pa.plot([hi], [0], "o", ms=6, color=charts.line(tok))
        pa.plot([lo], [0], "o", ms=6, mfc="none", mec=charts.line(tok), mew=1.4)
pa.plot([0], [0], "o", ms=6, color=P.ink())
pa.axhline(0, color=P.muted(), lw=0.7)
pa.text(0.02, 0.03, "collapse", fontsize=7.5, color=P.ink())
pa.text(0.2, -0.17, "threshold", fontsize=7.5, color=charts.line("protein"))
leg = pa.legend(loc="upper right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 1.2)
pa.set_ylim(-0.45, 0.25)
charts.style_axes(pa, "arterial pressure P (normal = 1)", "τ dP/dt")
charts.title(pa, "Rate of change of pressure")

# ---- B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
dt = 0.01
t = np.arange(0, 20, dt)
for V, tok, lab in ((0.8, "protein", "lose 20% (≈ 1 L): recovers"), (0.6, "rna", "lose 40% (≈ 2 L): vicious cycle")):
    x = np.empty_like(t)
    x[0] = V  # the pressure falls at once in proportion to the lost volume
    for i in range(1, t.size):
        x[i] = x[i - 1] + dt * (V * h(x[i - 1]) - x[i - 1])
    pb.plot(t, x, color=charts.line(tok), lw=1.7, label=lab)
pb.axhline(1, color=P.muted(), lw=0.7, ls="--")
pb.text(19.9, 1.02, "normal", fontsize=7.5, color=P.muted(), ha="right", va="bottom")
leg = pb.legend(loc="lower left", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(0, 20)
pb.set_ylim(0, 1.15)
charts.style_axes(pb, "time / τ", "arterial pressure P")
charts.title(pb, "After an abrupt haemorrhage")
