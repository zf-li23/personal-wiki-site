"""Critical slowing down before a regime shift.

The reduced lake model dV = f(V; E0) dt + sigma dW, f(V; E0) = V [1 - V (1 + (E0 hV / (hE (hV + V)))^4)],
hV = 0.2, hE = 2, sigma = 0.012, integrated by the Euler-Maruyama method (dt = 0.05) while E0 rises
linearly from 4 to 7.6 over 6000 time units; the clear state disappears at the fold E0 = 7.29.
A: vegetation cover V(t) (and the stable clear-state equilibrium, dashed) with the collapse.
B, C: variance and lag-1 autocorrelation (lag 1 time unit) of V after subtracting a Gaussian-smoothed
trend, in moving windows of 500 time units, computed only before the transition; both rise
as the fold is approached. D: the eigenvalue lambda = df/dV of the clear equilibrium against E0
(computed from the model): it tends to 0 like the square root of the distance to the fold, so the
return time 1/|lambda|, the stationary variance sigma^2/(2|lambda|) and the autocorrelation
exp(lambda) all increase.
"""

import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(8)
fig, ax = bio.canvas(30.0, 13.0)

hV, hE = 0.2, 2.0


def f(V, E0):
    return V * (1 - V * (1 + (E0 * hV / (hE * (hV + V))) ** 4))


def clear_eq(E0):
    return brentq(lambda v: f(v, E0) / v, 0.676, 0.9999)


dt, T = 0.05, 6000.0
n = int(T / dt)
E0t = np.linspace(4.0, 7.6, n)
V = np.empty(n)
V[0] = clear_eq(4.0)
noise = rng.standard_normal(n) * 0.012 * np.sqrt(dt)
for i in range(1, n):
    V[i] = max(V[i - 1] + f(V[i - 1], E0t[i - 1]) * dt + noise[i], 1e-4)
step = int(1 / dt)
t = np.arange(n)[::step] * dt
Vs = V[::step]
E0s = E0t[::step]
icol = np.argmax(Vs < 0.4)
Eeq = np.array([clear_eq(e) if e < 7.28 else np.nan for e in E0s])

pa = C.axes_at(ax, (2.6, 7.4, 11.4, 4.2))
pa.plot(t, Vs, color=Q.line_color("plant"), lw=0.8)
pa.plot(t, Eeq, color=P.ink(), lw=1.0, ls="--")
pa.axvline(t[icol], color=P.muted(), lw=0.8, ls=":")
pa.set_xlim(0, T)
pa.set_ylim(0, 1)
C.style_axes(pa, None, "vegetation V")
bio.panel(ax, "A", (0.5, 12.4))
bio.label(ax, (2.6, 12.0), "Slow increase of nutrients (E0 from 4 to 7.6)", size="small", bold=True, ha="left")

trend = gaussian_filter1d(Vs[:icol], 100)
res = Vs[:icol] - trend
w = 500
var, ac, tw = [], [], []
for k in range(w, icol):
    x = res[k - w:k]
    var.append(x.var())
    ac.append(np.corrcoef(x[:-1], x[1:])[0, 1])
    tw.append(t[k])
pb = C.axes_at(ax, (2.6, 1.6, 5.0, 4.2))
pb.plot(tw, np.array(var) * 1e4, color=Q.line_color("dna"), lw=1.4)
pb.set_xlim(0, T)
C.style_axes(pb, "time", "variance (x 1e-4)")
bio.panel(ax, "B", (0.5, 6.4))
pc = C.axes_at(ax, (9.0, 1.6, 5.0, 4.2))
pc.plot(tw, ac, color=Q.line_color("rna"), lw=1.4)
pc.set_xlim(0, T)
C.style_axes(pc, "time", "lag-1 autocorrelation")
bio.panel(ax, "C", (7.9, 6.4))

pd = C.axes_at(ax, (18.0, 1.9, 10.8, 9.4))
Eg = np.linspace(2.0, 7.288, 300)
lam = []
for e in Eg:
    v = clear_eq(e)
    lam.append((f(v + 1e-6, e) - f(v - 1e-6, e)) / 2e-6)
pd.plot(Eg, lam, color=Q.line_color("dna"), lw=1.8, label="eigenvalue of clear state")
pd.axvline(7.289, color=P.muted(), lw=0.8, ls=":")
pd.axhline(0, color=P.muted(), lw=0.6)
pd.text(7.22, -0.06, "fold", fontsize=FS["tiny"], color=P.ink(), ha="right")
pd.set_xlim(2, 7.6)
C.style_axes(pd, "nutrient level E0", "lambda = df/dV at clear equilibrium")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "D", (15.8, 12.4))
bio.label(ax, (18.0, 12.0), "Loss of resilience at the fold", size="small", bold=True, ha="left")
