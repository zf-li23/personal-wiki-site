"""Delayed negative feedback: the her1 model of Lewis (2003), its period against the delay, and the square-wave
limit of the single-delay equation."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT


def lewis(Tm=12.0, Tp=2.8, a=4.5, b=0.23, c=0.23, k=33.0, p0=40.0, dt=0.02, tmax=500.0):
    n = int(tmax / dt)
    m, p = np.zeros(n), np.zeros(n)
    dm, dp = max(1, int(round(Tm / dt))), max(1, int(round(Tp / dt)))
    for i in range(n - 1):
        pd = p[i - dm] if i >= dm else 0.0
        md = m[i - dp] if i >= dp else 0.0
        m[i + 1] = m[i] + dt * (k / (1 + (pd / p0) ** 2) - c * m[i])
        p[i + 1] = p[i] + dt * (a * md - b * p[i])
    return np.arange(n) * dt, m, p


def period(t, x):
    half = t > t[-1] * 0.5
    xs, ts = x[half], t[half]
    if xs.max() - xs.min() < 1e-3 * max(1.0, xs.max()):
        return np.nan
    i = np.where((xs[1:-1] > xs[:-2]) & (xs[1:-1] > xs[2:]))[0] + 1
    return np.mean(np.diff(ts[i])) if len(i) > 2 else np.nan


fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.7))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.86, wspace=0.32)

t, m, p = lewis()
a = axs[0]
sel = t < 250
a.plot(t[sel], m[sel], color=charts.line("mrna"), lw=1.6, label="mRNA m")
a.plot(t[sel], p[sel] / 20, color=charts.line("protein"), lw=1.6, label="protein p / 20")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(a, "time (min)", "molecules per cell")
charts.title(a, "A  her1 oscillator (period %.0f min)" % period(t, p))

b = axs[1]
Ts = np.arange(2.0, 31.0, 2.0)
per = []
for T in Ts:
    tt, mm, pp = lewis(Tm=T - min(2.8, T / 2), Tp=min(2.8, T / 2), tmax=400.0)
    per.append(period(tt, pp))
per = np.array(per)
b.plot(Ts, per, "o", color=charts.line("protein"), ms=4, label="numerical")
Tl = np.linspace(0, 31, 50)
b.plot(Tl, 2 * (Tl + 2 / 0.23), color=P_.ink(), lw=1.2, label="2(T + 1/b + 1/c)")
b.plot(Tl, 2 * Tl, color=P_.muted(), lw=1.0, ls="--", label="2T")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
b.set_xlim(0, 31)
b.set_ylim(0, 90)
charts.style_axes(b, "total delay T (min)", "period (min)")
charts.title(b, "B  Period and delay")

c = axs[2]
dt, cc = 0.002, 20.0
n = int(8.0 / dt)
dl = int(1.0 / dt)
for K, tok, ls in ((3.0, "highlight", "-"), (1.5, "dna", "-")):
    x = np.full(n, 0.2)
    for i in range(dl, n - 1):
        x[i + 1] = x[i] + dt * cc * (K / (1 + x[i - dl] ** 2) - x[i])
    c.plot(np.arange(n) * dt, x, color=charts.line(tok), lw=1.5, ls=ls, label="K = %.1f" % K)
x0 = (3 - np.sqrt(5)) / 2
for v in (x0, 1 / x0):
    c.axhline(v, color=P_.muted(), lw=0.8, ls=":")
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
c.set_ylim(0, 3.4)
charts.style_axes(c, "time (delays)", "x")
charts.title(c, "C  Fast-turnover limit")
