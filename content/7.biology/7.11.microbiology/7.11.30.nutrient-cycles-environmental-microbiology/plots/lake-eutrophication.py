"""Hysteresis in lake eutrophication: a minimal phosphorus model (after Carpenter et al. 1999).

Phosphorus in the water, P, changes as dP/dt = L - s P + r P^q / (m^q + P^q): L is the external loading
(runoff from fertilized land, sewage), s P the loss by outflow and sedimentation, and the last term the
recycling of P from the sediments, which switches on when the hypolimnion becomes anoxic as algal biomass
(proportional to P) rises (iron(III) phosphate is reduced and P released). Dimensionless parameters
s = 1, r = 1, m = 1, q = 8.
A: equilibria as a function of loading L: stable (solid) and unstable (dashed) branches. Between the two
fold points the lake has two stable states, clear (oligotrophic) and turbid (eutrophic).
B: a simulated history: loading rises slowly to 0.85 and is then reduced again to its initial value. The lake
flips to the turbid state only after L passes the upper fold, and returns only when L falls below the lower
fold, far below the loading at which it flipped (both switches lag a little behind the folds because the
loading changes at a finite rate).
"""
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P_ = bio.P
s, r, m, q = 1.0, 1.0, 1.0, 8


def f(P, L):
    return L - s * P + r * P ** q / (m ** q + P ** q)


Ps = np.linspace(0.0, 1.85, 3000)
Lcurve = s * Ps - r * Ps ** q / (m ** q + Ps ** q)
dL = np.gradient(Lcurve, Ps)
fig, ax = bio.canvas(24.0, 10.0)

bio.panel(ax, "A", (0.3, 9.8))
pa = quant.Plot(ax, (2.2, 1.5, 8.5, 7.2), xlim=(0, 0.9), ylim=(0, 2.0), xlabel="phosphorus loading L",
                ylabel="phosphorus in the water P*", xticks=[0, 0.2, 0.4, 0.6, 0.8], yticks=[0, 0.5, 1, 1.5, 2],
                grid=True)
stable = dL > 0
seg = np.split(np.arange(Ps.size), np.flatnonzero(np.diff(stable.astype(int))) + 1)
for idx in seg:
    pa.line(Lcurve[idx], Ps[idx], "dna" if stable[idx[0]] else "muted", lw=2.0 if stable[idx[0]] else 1.3,
            dashed=not stable[idx[0]])
folds = np.flatnonzero(np.diff(np.sign(dL)) != 0)
Lf = sorted(Lcurve[folds])
for v in Lf:
    pa.vline(v, token="muted", dashed=True, lw=0.6)
pa.span(Lf[0], Lf[1], "highlight", strength=0.8)
pa.text(0.04, 0.35, "clear", token="dna", ha="left")
pa.text(0.74, 1.62, "turbid", token="dna", ha="left")
pa.text((Lf[0] + Lf[1]) / 2, 1.92, "two stable states", ha="center", color=P_.muted())

# B: time course --------------------------------------------------------------------------------------
T = 400.0
t = np.linspace(0, T, 4001)
Lt = np.where(t < T / 2, 0.05 + 0.8 * t / (T / 2), 0.85 - 0.8 * (t - T / 2) / (T / 2))
P = np.empty_like(t)
P[0] = brentq(lambda x: f(x, Lt[0]), 0, 0.5)
dt = t[1] - t[0]
for k in range(1, t.size):
    P[k] = P[k - 1] + dt * f(P[k - 1], Lt[k - 1])
bio.panel(ax, "B", (12.8, 9.8))
pb = quant.Plot(ax, (14.8, 1.5, 8.5, 7.2), xlim=(0, 0.9), ylim=(0, 2.0), xlabel="phosphorus loading L",
                ylabel="phosphorus in the water P", xticks=[0, 0.2, 0.4, 0.6, 0.8], yticks=[0, 0.5, 1, 1.5, 2], grid=True)
up = t < T / 2
pb.line(Lt[up], P[up], "negative", lw=2.0)
pb.text(0.75, 0.55, "loading rises", token="negative", ha="left")
pb.line(Lt[~up], P[~up], "positive", lw=2.0)
pb.text(0.08, 0.95, "loading falls", token="positive", ha="left")
for v in Lf:
    pb.vline(v, token="muted", dashed=True, lw=0.6)
