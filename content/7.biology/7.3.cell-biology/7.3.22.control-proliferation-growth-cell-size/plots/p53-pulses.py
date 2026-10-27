"""Digital pulses of p53 after DNA damage (delay model in the spirit of Lahav et al. 2004 and Batchelor et al. 2008).

A dose of ionizing radiation creates D0 double-strand breaks, each repaired at random at rate 0.1 per hour.
ATM activity A (0..1) is activated by breaks, g = D/(D + 8), with positive feedback from active ATM, and is
inactivated by the phosphatase Wip1 (W). p53 (P) is made at a constant rate and degraded by Mdm2 (M); active
ATM protects p53 from Mdm2. p53 induces Mdm2 and Wip1 after delays of 0.8 and 1.5 h (transcription,
translation, maturation):
    dA/dt = g (ka + kau A^2/(Ka^2 + A^2)) (1 - A) - kw W A / (0.1 + A)
    dP/dt = bp - (am M (1 - 0.9 A) + ap) P
    dM/dt = bm P(t - 0.8 h) - dm M
    dW/dt = bw P(t - 1.5 h)^4 / (Kw^4 + P(t - 1.5 h)^4) - dw W
with ka = 0.5, kau = 6, Ka = 0.3, kw = 1.5, bp = 1, am = 3, ap = 0.1, bm = 1, dm = 1, bw = 2, Kw = 1.2,
dw = 0.8 (per hour, concentrations relative).
(A) Single cells after a low (5 breaks) and a high (40 breaks) dose: p53 rises in pulses of nearly fixed height
and width, about 6 h apart; more damage gives more pulses, not bigger ones; pulses stop when the breaks are
repaired (grey steps: unrepaired breaks, right axis).
(B) Number of pulses in 40 simulated cells per dose (mean and range).
(C) The average over 100 cells after 20 breaks looks like a damped oscillation, although every cell pulses
with an undamped amplitude: averaging hides the single-cell dynamics.
"""

import numpy as np
from scipy.signal import find_peaks

import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT

Q = dict(ka=0.5, kau=6.0, Ka=0.3, KD=8.0, kw=1.5, bp=1.0, am=3.0, ap=0.1, fA=0.9, bm=1.0, dm=1.0, bw=2.0, Kw=1.2,
         dw=0.8, tau1=0.8, tau2=1.5, rep=0.1)


def sim(D0, seed, T=48.0, dt=0.01, burn=30.0):
    rng = np.random.default_rng(seed)
    q = Q
    n = int((T + burn) / dt)
    A = np.zeros(n); P = np.zeros(n); M = np.zeros(n); W = np.zeros(n); D = np.zeros(n)
    P[0] = M[0] = W[0] = 0.3
    k1, k2, i0 = int(q["tau1"] / dt), int(q["tau2"] / dt), int(burn / dt)
    d = 0
    for i in range(n - 1):
        if i == i0:
            d = D0
        if d > 0 and rng.random() < d * q["rep"] * dt:
            d -= 1
        D[i] = d
        g = d / (d + q["KD"])
        p1, p2 = P[max(i - k1, 0)], P[max(i - k2, 0)]
        A[i + 1] = A[i] + dt * (g * (q["ka"] + q["kau"] * A[i] ** 2 / (q["Ka"] ** 2 + A[i] ** 2)) * (1 - A[i])
                                - q["kw"] * W[i] * A[i] / (0.1 + A[i]))
        P[i + 1] = P[i] + dt * (q["bp"] - (q["am"] * M[i] * (1 - q["fA"] * A[i]) + q["ap"]) * P[i])
        M[i + 1] = M[i] + dt * (q["bm"] * p1 - q["dm"] * M[i])
        W[i + 1] = W[i] + dt * (q["bw"] * p2 ** 4 / (q["Kw"] ** 4 + p2 ** 4) - q["dw"] * W[i])
    D[-1] = d
    t = np.arange(n) * dt - burn
    return t[i0:], A[i0:], P[i0:], D[i0:]


def npulses(P):
    return len(find_peaks(P, prominence=0.5)[0])


fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a = charts.axes_at(ax, (1.8, 1.5, 9.0, 6.6))
a2 = a.twinx()
a2.set_facecolor("none")
for D0, tok, seed in ((5, "channel", 4), (40, "negative", 1)):
    t, A, P, D = sim(D0, seed)
    a.plot(t, P, color=charts.line(tok), lw=1.7, label=f"p53, {D0} breaks")
    a2.step(t, D, where="post", color=charts.line(tok), lw=0.8, alpha=0.6, ls=":")
a.set_xlim(0, 48)
a.set_ylim(0, 2.6)
a2.set_ylim(0, 60)
a2.set_ylabel("unrepaired breaks (dotted)", fontsize=FT["small"], color=P_.muted())
a2.tick_params(colors=P_.muted(), labelsize=FT["tiny"])
for sp in a2.spines.values():
    sp.set_visible(False)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, "time after irradiation / h", "nuclear p53 (relative)")

bio.panel(ax, "B", (12.6, 8.8))
b = charts.axes_at(ax, (14.2, 1.5, 5.0, 6.6))
doses = [2, 5, 10, 20, 40]
means, lo, hi = [], [], []
for D0 in doses:
    c = [npulses(sim(D0, s)[2]) for s in range(40)]
    means.append(np.mean(c)); lo.append(min(c)); hi.append(max(c))
b.errorbar(doses, means, yerr=[np.array(means) - lo, np.array(hi) - means], fmt="o-", color=charts.line("negative"),
           ms=4, lw=1.5, capsize=3)
b.set_xscale("log")
b.set_xticks(doses)
b.set_xticklabels([str(x) for x in doses])
b.set_ylim(0, 8)
charts.style_axes(b, "double-strand breaks D0", "number of p53 pulses")

bio.panel(ax, "C", (20.2, 8.8))
c_ = charts.axes_at(ax, (21.8, 1.5, 4.8, 6.6))
runs = [sim(20, 100 + s) for s in range(100)]
t = runs[0][0]
for k in range(3):
    c_.plot(t, runs[k][2], color=charts.line("neutral"), lw=0.8)
c_.plot(t, np.mean([r[2] for r in runs], axis=0), color=charts.line("negative"), lw=2.0, label="mean of 100 cells")
c_.set_xlim(0, 48)
c_.set_ylim(0, 2.6)
c_.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(c_, "time / h", "p53 (grey: single cells)")
