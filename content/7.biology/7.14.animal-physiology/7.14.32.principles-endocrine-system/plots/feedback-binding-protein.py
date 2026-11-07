# Negative feedback regulates the free hormone; binding proteins change only the total.
# Dimensionless axis model (time in days): the gland secretes s(F) = 2 / (1 + F^n) (n = 4), which falls
# as the free hormone F rises (feedback through the hypothalamus-pituitary); only free hormone is cleared,
# at rate F. Total hormone u = F * r, where r = (1 + P/Kd) relative to baseline measures the binding
# capacity of plasma. du/dt = k0 (s(F) - F), k0 = ln 2 / 7 d (a thyroxine-like half-life).
# A: the steady state is where secretion meets clearance; the set point moves when the feedback
#    sensitivity (K) or the clearance changes, but not when the binding capacity changes.
# B: binding capacity doubled (as TBG rises with oestrogen in pregnancy) or halved at day 5.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
n = 4


def secretion(F, K=1.0):
    return 2.0 / (1.0 + (F / K) ** n)


fig, ax = bio.canvas(24.0, 9.6)

# ---- A -------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 8.6, 6.9))
F = np.linspace(0, 2.0, 300)
pa.plot(F, secretion(F), color=charts.line("dna"), lw=1.8)
pa.plot(F, secretion(F, K=1.3), color=charts.line("dna"), lw=1.3, ls="--")
pa.plot(F, F, color=charts.line("rna"), lw=1.8)
pa.plot(F, 1.5 * F, color=charts.line("rna"), lw=1.3, ls="--")
for K, c in ((1.0, 1.0), (1.3, 1.0), (1.0, 1.5)):
    # steady state: secretion(F) = c F
    Fs = F[np.argmin(np.abs(secretion(F, K) - c * F))]
    pa.scatter([Fs], [c * Fs], s=28, color=P.ink(), zorder=5)
pa.text(1.28, 0.1, "secretion s(F)", color=charts.line("dna"), fontsize=7.5, ha="left")
pa.text(1.25, secretion(1.6, 1.3) + 0.55, "less sensitive\nfeedback (K ×1.3)", color=charts.line("dna"),
        fontsize=7.2, ha="left")
pa.text(1.72, 1.72 + 0.04, "clearance F", color=charts.line("rna"), fontsize=7.5, ha="right", va="bottom")
pa.text(1.18, 1.78 + 0.04, "clearance ×1.5", color=charts.line("rna"), fontsize=7.2, ha="right", va="bottom")
pa.set_xlim(0, 2.0)
pa.set_ylim(0, 2.2)
charts.style_axes(pa, "free hormone F (baseline = 1)", "rate (baseline = 1)")
charts.title(pa, "Set point: secretion = clearance")

# ---- B -------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
k0 = np.log(2) / 7.0
dt = 0.01
t = np.arange(0, 70, dt)
for r_new, ls, tag in ((2.0, "-", "×2"), (0.5, "--", "×0.5")):
    r = np.where(t < 5, 1.0, r_new)
    u = np.ones_like(t)
    for i in range(1, t.size):
        Fi = u[i - 1] / r[i - 1]
        u[i] = u[i - 1] + dt * k0 * (secretion(Fi) - Fi)
    Ff = u / r
    pb.plot(t, u, color=charts.line("protein"), lw=1.7, ls=ls)
    pb.plot(t, Ff, color=charts.line("positive"), lw=1.7, ls=ls)
    pb.plot(t, secretion(Ff), color=charts.line("dna"), lw=1.2, ls=ls)
pb.text(69, 2.0, "total, capacity ×2", color=charts.line("protein"), fontsize=7.3, ha="right", va="bottom")
pb.text(69, 0.5, "total, capacity ×0.5", color=charts.line("protein"), fontsize=7.3, ha="right", va="top")
pb.text(69, 1.04, "free (both)", color=charts.line("positive"), fontsize=7.3, ha="right", va="bottom")
pb.text(9.0, 1.72, "secretion", color=charts.line("dna"), fontsize=7.3, ha="left")
pb.annotate("", (5, 2.35), (5, 2.62), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
pb.text(5.8, 2.5, "binding capacity changed", fontsize=7.3, color=P.ink(), va="center")
pb.set_xlim(0, 70)
pb.set_ylim(0, 2.7)
charts.style_axes(pb, "time / d", "relative to baseline")
charts.title(pb, "Total follows binding capacity; free returns")
