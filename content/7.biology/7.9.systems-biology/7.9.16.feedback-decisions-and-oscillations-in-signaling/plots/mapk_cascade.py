"""Ultrasensitivity in a three-tier MAP kinase cascade and bistability from positive feedback.

Steady states (Huang-Ferrell type, with the formula for a distributive double-phosphorylation cycle of
7.1.15): MAPKKK active fraction a1 = E/(1 + E); MAPKK and MAPK doubly phosphorylated fractions
m = r^2/(1 + r + r^2) with r = u (1 + (m1 + m2)/K)/(1 + (m0 + m1)/K), K = 1, u = 4 x (active upstream
fraction).
A: active fraction of each tier against the input E; apparent Hill coefficients ln 81 / ln(E90/E10).
B: local response coefficients of each tier (d ln output / d ln input of that tier) and of the whole
cascade (d ln MAPK* / d ln E), which is their product.
C: positive feedback from MAPK to the synthesis of the top kinase (Mos in Xenopus oocytes):
dM/dt = s + f m3(M) - M, with the cascade at steady state for input M. Steady-state MAPK activity
against the stimulus s (progesterone-driven synthesis): f = 0 graded, f = 0.3 steeper, f = 0.5
bistable with hysteresis, f = 1 irreversible (the lower fold lies at s < 0). Solid: stable, dashed:
unstable.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
K = 1.0


def dbl(u):
    def h(r):
        m0 = 1 / (1 + r + r * r)
        return r - u * (1 + (r * m0 + r * r * m0) / K) / (1 + (m0 + r * m0) / K)
    r = brentq(h, 0, 1e6)
    return r * r / (1 + r + r * r)


def cascade(E):
    a1 = E / (1 + E)
    m2 = dbl(4 * a1)
    return a1, m2, dbl(4 * m2)


E = np.logspace(-3, 2, 1201)
A = np.array([cascade(e) for e in E]).T
fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.86, wspace=0.32)
cols = [charts.line("enzyme"), charts.line("protein"), charts.line("positive")]
names = ["MAPKKK", "MAPKK", "MAPK"]
ax = axes[0]
for k in range(3):
    y = A[k] / A[k].max()
    e10, e90 = E[np.argmax(y >= 0.1)], E[np.argmax(y >= 0.9)]
    nh = np.log(81) / np.log(e90 / e10)
    ax.semilogx(E, A[k], color=cols[k], lw=1.8, label=f"{names[k]}, nH = {nh:.1f}")
ax.legend(fontsize=7, frameon=False, loc="upper left")
ax.set_ylim(0, 1.15)
charts.style_axes(ax, "input E (units of MAPKKK activation constant)", "active fraction")
charts.title(ax, "A  Steepness grows down the cascade")

ax = axes[1]
lnE = np.log(E)
inputs = [E, A[0], A[1]]
R = [np.gradient(np.log(A[k]), np.log(inputs[k])) for k in range(3)]
Rtot = np.gradient(np.log(A[2]), lnE)
for k in range(3):
    ax.semilogx(E, R[k], color=cols[k], lw=1.3, label=f"tier {k + 1}")
ax.semilogx(E, Rtot, color=P.ink(), lw=1.8, label="whole cascade")
ax.semilogx(E, R[0] * R[1] * R[2], color=P.muted(), lw=1.0, ls="--", label="product of tiers")
ax.set_ylim(0, 7)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "input E", "response coefficient d ln y / d ln x")
charts.title(ax, "B  Local gains multiply")

ax = axes[2]
M = np.logspace(-3, 1.3, 1501)
m3 = np.array([cascade(m)[2] for m in M])
for f, tok in [(0.0, "neutral"), (0.3, "enzyme"), (0.5, "protein"), (1.0, "negative")]:
    s = M - f * m3
    ds = np.gradient(s)
    stable = ds > 0
    seg = np.split(np.arange(len(M)), np.where(np.diff(stable.astype(int)) != 0)[0] + 1)
    for j, idx in enumerate(seg):
        ax.plot(s[idx], m3[idx], color=charts.line(tok), lw=1.8 if stable[idx[0]] else 1.0,
                ls="-" if stable[idx[0]] else "--", label=f"f = {f:g}" if j == 0 else None)
ax.axvline(0, color=P.muted(), lw=0.7)
ax.set_xlim(-0.25, 0.5)
ax.set_ylim(0, 0.9)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "stimulus s", "MAPK activity at steady state")
charts.title(ax, "C  Feedback: switch and memory")
