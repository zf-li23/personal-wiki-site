"""Looming detection by the locust LGMD: the eta function.

An object of half-size l approaches at constant speed v; at time t before collision (t < 0)
it subtends theta(t) = 2 arctan(l / (v |t|)). Gabbiani, Krapp and Laurent (1999) found that the
firing rate of the LGMD is described by eta(t) = C theta'(t - delta) exp(-alpha theta(t - delta)):
a product of the angular velocity and a negative exponential of the angular size, computed by the
neuron as exp(log theta' - alpha theta). Parameters: alpha = 4.7 /rad, delay delta = 27 ms (typical).
The peak then occurs when theta reaches a fixed threshold angle, a fixed delay after that, so the
peak time is a linear function of l/|v|.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
alpha, delta = 4.7, 0.027
t = np.linspace(-1.0, -0.001, 4000)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
ratios = [0.01, 0.03, 0.05]
cols = [P.edge("negative"), P.edge("rna"), P.edge("dna")]
peaks = []
for r, col in zip(ratios, cols):
    th = 2 * np.arctan(r / np.abs(t))
    dth = np.gradient(th, t)
    eta = dth * np.exp(-alpha * th)
    ts = t + delta  # response delayed by delta
    m = ts < 0
    a.plot(ts[m] * 1e3, eta[m] / eta.max(), color=col, lw=2, label=f"l/|v| = {r * 1e3:.0f} ms")
    a.plot(t * 1e3, np.degrees(th) / 180, color=col, lw=0.9, ls=":")
a.set_xlim(-600, 0)
a.set_ylim(0, 1.08)
a.set_xlabel("Time to collision / ms")
a.set_ylabel("Normalized η (solid); angular size / 180° (dotted)")
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A", loc="left", fontweight="bold")
rr = np.linspace(0.005, 0.06, 40)
tp = []
thr = []
for r in rr:
    th = 2 * np.arctan(r / np.abs(t))
    dth = np.gradient(th, t)
    eta = dth * np.exp(-alpha * th)
    k = np.argmax(eta)
    tp.append(t[k] + delta)
    thr.append(np.degrees(th[k]))
tp = np.array(tp)
b.plot(rr * 1e3, -tp * 1e3, "o", ms=3.5, color=P.edge("dna"))
fit = np.polyfit(rr, -tp, 1)
b.plot(rr * 1e3, np.polyval(fit, rr) * 1e3, color=P.muted(), lw=1)
b.text(8, 180, f"peak {abs(fit[1]) * 1e3:.0f} ms after the object\nreaches {np.mean(thr):.0f}° (threshold angle)",
       fontsize=8, color=P.ink())
b.set_xlabel("l/|v| / ms")
b.set_ylabel("Time of peak before collision / ms")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
