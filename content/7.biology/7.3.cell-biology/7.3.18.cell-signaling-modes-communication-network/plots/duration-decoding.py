"""Decoding the duration of ERK activity: the immediate early gene product c-Fos as a persistence detector.

ERK activity E(t) (relative) is either transient (as with EGF in PC12 cells) or sustained (as with NGF).
The c-fos gene is transcribed in proportion to E but shuts itself off as ERK exposure accumulates
(transcription E exp(-q), dq/dt = E/10 min, a stand-in for the feedback repression of the promoter), and
its mRNA is short-lived: dm/dt = E exp(-q) - m/tau_m with tau_m = 15 min. The protein is made from the mRNA in an unphosphorylated, unstable
form Fu, which ERK (with RSK) phosphorylates into a stable form Fp:
dFu/dt = m - (d_u + k_p E) Fu, dFp/dt = k_p E Fu - d_p Fp, with d_u = ln 2/30 min, d_p = ln 2/180 min and
k_p = 0.1 per min. Values are chosen to match the observed time scales (mRNA peak within half an hour, protein
after about an hour); the logic follows Murphy and colleagues (2002).
A: the two ERK time courses. B: c-fos mRNA is a pulse of similar size in both cases. All curves are scaled to the maximum of the
sustained case.
C: phosphorylated, stable c-Fos accumulates only if ERK is still active when the protein is made,
about an hour after the stimulus: the delay between the two arms makes the circuit respond to the
duration of the signal rather than to its peak.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]
ln2 = np.log(2)
tau_m, du, dp, kp = 15.0, ln2 / 30, ln2 / 180, 0.1


def transient(t):
    return np.exp(-t / 8.0) * (1 - np.exp(-t / 1.5)) / 0.596


def sustained(t):
    return transient(t) * 0.45 + 0.55 * (1 - np.exp(-t / 3.0))


def run(E):
    def f(t, y):
        m, fu, fp, q = y
        e = E(t)
        return [e * np.exp(-q) - m / tau_m, m - (du + kp * e) * fu, kp * e * fu - dp * fp, e / 10.0]

    t = np.linspace(0, 240, 2401)
    s = solve_ivp(f, (0, 240), [0, 0, 0, 0], t_eval=t, max_step=0.5)
    return t, s.y


fig, ax = bio.canvas(20.0, 6.6)
inputs = (("transient (EGF-like)", transient, "neutral"), ("sustained (NGF-like)", sustained, "highlight"))
boxes = [(1.4, 1.2, 4.9), (8.0, 1.2, 4.9), (14.6, 1.2, 4.9)]
titles = ["ERK activity", "c-fos mRNA", "stable phospho-c-Fos"]
ylabels = ["ERK activity (relative)", "mRNA (relative)", "protein (relative)"]
axes = []
for k, (x0, y0, w) in enumerate(boxes):
    bio.panel(ax, "ABC"[k], (x0 - 1.3, 6.5))
    a = charts.axes_at(ax, (x0, y0, w, 4.6))
    axes.append(a)
runs = [(name, E, tok, *run(E)) for name, E, tok in inputs]
mmax = max(r[4][0].max() for r in runs)
fmax = max(r[4][2].max() for r in runs)
for name, E, tok, t, (m, fu, fp, q) in runs:
    col = charts.line(tok)
    axes[0].plot(t, E(t), color=col, lw=1.8, label=name)
    axes[1].plot(t, m / mmax, color=col, lw=1.8)
    axes[2].plot(t, fp / fmax, color=col, lw=1.8)
    axes[2].plot(t, fu / fmax, color=col, lw=1.0, ls=(0, (3, 2)))
axes[2].text(236, 0.5, "dashed: unstable\nunphosphorylated c-Fos", fontsize=FS, color=P.muted(), ha="right")
axes[0].legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper right")
for a, ttl, yl in zip(axes, titles, ylabels):
    a.set_xlim(0, 240)
    a.set_xticks([0, 60, 120, 180, 240])
    a.set_ylim(0, 1.1)
    charts.style_axes(a, "time after stimulus / min", yl)
    charts.title(a, ttl)
