"""Ca2+ oscillations by Ca2+-induced Ca2+ release: the two-pool model of Goldbeter, Dupont and Berridge (1990).

Z is cytosolic and Y stored (ER) Ca2+ (micromolar). dZ/dt = v0 + v1 beta - v2 + v3 + kf Y - k Z and
dY/dt = v2 - v3 - kf Y, with pumping into the store v2 = VM2 Z^2/(K2^2 + Z^2) and release from it
v3 = VM3 Y^2/(KR^2 + Y^2) Z^4/(KA^4 + Z^4), which is activated by cytosolic Ca2+ (the positive
feedback). beta, the fraction of the maximal IP3-dependent influx v1, stands for the stimulus.
Parameters of the original paper: v0 = 1 and v1 = 7.3 uM/s, k = 10/s, kf = 1/s, VM2 = 65 and
VM3 = 500 uM/s, K2 = 1, KR = 2 and KA = 0.9 uM. (They give periods of seconds; in hepatocytes and
many other cells the same mechanism with slower pumps gives periods of tens of seconds to minutes.)
A: oscillations at beta = 0.3 and 0.6. B: frequency and amplitude against beta: oscillations exist in a
window (here about 0.29 to 0.77) and their frequency rises steadily with the stimulus, while the
amplitude falls only towards the upper end of the window. C: a decoder that is activated cooperatively by Ca2+ and inactivated slowly,
dD/dt = 2 h(Z)(1 - D) - 0.5 D with h = Z^4/(1 + Z^4), reads the frequency as a mean activity.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]
v0, k, kf, v1, VM2, VM3, K2, KR, KA = 1.0, 10.0, 1.0, 7.3, 65.0, 500.0, 1.0, 2.0, 0.9


def rhs(t, y, b):
    Z, Y, D = y
    v2 = VM2 * Z**2 / (K2**2 + Z**2)
    v3 = VM3 * Y**2 / (KR**2 + Y**2) * Z**4 / (KA**4 + Z**4)
    h = Z**4 / (1 + Z**4)
    return [v0 + v1 * b - v2 + v3 + kf * Y - k * Z, v2 - v3 - kf * Y, 2.0 * h * (1 - D) - 0.5 * D]


def run(b, tmax=40.0):
    t = np.linspace(0, tmax, int(tmax * 400))
    s = solve_ivp(rhs, (0, tmax), [0.1, 1.5, 0.0], args=(b,), t_eval=t, max_step=0.004, rtol=1e-7)
    return s.t, s.y


fig, ax = bio.canvas(20.0, 12.6)

bio.panel(ax, "A", (0.1, 12.5))
pa = charts.axes_at(ax, (1.5, 7.6, 17.9, 4.2))
for b, tok in ((0.3, "ca"), (0.6, "receptor")):
    t, y = run(b, 12.0)
    pa.plot(t, y[0], color=charts.line(tok), lw=1.6, label=f"cytosolic Ca²⁺, β = {b}")
t, y = run(0.3, 12.0)
pa.plot(t, y[1], color=charts.line("er"), lw=1.1, ls=(0, (4, 2)), label="stored Ca²⁺, β = 0.3")
pa.set_xlim(0, 12)
pa.set_ylim(0, 2.6)
pa.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper right", ncol=3)
charts.style_axes(pa, "time / s", "[Ca²⁺] / µM")
charts.title(pa, "Spikes at constant stimulus: a higher stimulus gives a higher frequency")

betas = np.linspace(0.05, 0.95, 37)
freq, amp, dmean = [], [], []
for b in betas:
    t, y = run(b, 30.0)
    m = t > 15
    z, tt = y[0][m], t[m]
    rngz = z.max() - z.min()
    pk = [i for i in range(1, len(z) - 1) if z[i] > z[i - 1] and z[i] >= z[i + 1] and z[i] > z.min() + 0.5 * rngz]
    if rngz > 0.05 and len(pk) > 2:
        freq.append(1.0 / np.diff(tt[pk]).mean())
        amp.append(rngz)
    else:
        freq.append(np.nan)
        amp.append(0.0)
    dmean.append(y[2][m].mean())
freq, amp, dmean = map(np.array, (freq, amp, dmean))

bio.panel(ax, "B", (0.1, 5.9))
pb = charts.axes_at(ax, (1.5, 1.2, 7.6, 4.0))
pb.plot(betas, freq, color=charts.line("highlight"), lw=2.0, marker="o", ms=2.5, label="frequency")
pb.set_xlim(0, 1)
pb.set_ylim(0, 3.5)
charts.style_axes(pb, "stimulus β", "frequency / s⁻¹")
pb2 = pb.twinx()
pb2.plot(betas, amp, color=P.muted(), lw=1.3, ls=(0, (4, 2)), label="amplitude")
pb2.set_ylim(0, 1.6)
charts.style_axes(pb2, None, "amplitude / µM", box=True)
pb2.spines["top"].set_visible(False)
lines = pb.get_lines()[:1] + pb2.get_lines()[:1]
pb.legend(lines, [ln.get_label() for ln in lines], frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left")
charts.title(pb, "Frequency encodes the stimulus")

bio.panel(ax, "C", (10.6, 5.9))
pc = charts.axes_at(ax, (12.0, 1.2, 7.4, 4.0))
osc = ~np.isnan(freq)
pc.plot(betas, dmean, color=P.muted(), lw=1.0)
pc.plot(betas[osc], dmean[osc], color=charts.line("enzyme"), lw=2.0, marker="o", ms=2.5, label="oscillating")
pc.plot(betas[~osc], dmean[~osc], ls="none", marker="o", ms=2.5, color=P.muted(), label="steady Ca²⁺")
pc.set_xlim(0, 1)
pc.set_ylim(0, 1)
pc.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left")
charts.style_axes(pc, "stimulus β", "mean decoder activity")
charts.title(pc, "A slow decoder integrates the spikes")
