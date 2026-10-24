# A: the eukaryotic cell cycle (proportions of a ~24 h human somatic cycle: G1 ~11 h, S ~8 h, G2 ~4 h,
# M ~1 h), with the three main checkpoints (restriction point / G1-S, G2-M, spindle assembly checkpoint at the
# metaphase-anaphase transition), exit into G0, and the cyclin-CDK complexes that drive each transition.
# B: a quantitative model, the minimal mitotic oscillator of Goldbeter (1991, PNAS 88: 9107): cyclin C is
# synthesised at a constant rate and activates CDK1 (fraction M) through a phosphatase; active CDK1 activates
# the cyclin-degrading APC/C (fraction X), which destroys cyclin and closes the negative feedback loop.
# Parameters as in the paper (vi = 0.025 uM/min, vd = 0.25 uM/min, Kd = 0.02 uM, kd = 0.01 /min, Kc = 0.5 uM,
# VM1 = 3 /min, V2 = 1.5 /min, VM3 = 1 /min, V4 = 0.5 /min, K1-4 = 0.005); the period is about 25 min, as in
# early embryonic cycles.
import math

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import cellbio as CB
from wikibio import charts as Ch

fig, ax = bio.canvas(21.0, 10.0)
P = bio.P

# --- A: cycle wheel ----------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.85))
c, r, w = (5.0, 4.85), 2.75, 1.15
phases = [("M", 1.5 / 24, "receptor"), ("G1", 10.5 / 24, "positive"), ("S", 8 / 24, "dna"), ("G2", 4 / 24, "highlight")]
seg = CB.cycle_wheel(ax, c, r, phases, width=w, start=90 + 11.25)
# direction: an arc arrow inside the ring, clockwise
t = np.linspace(math.radians(60), math.radians(-210), 120)
ri = r - w / 2 - 0.45
arc = np.c_[c[0] + ri * np.cos(t), c[1] + ri * np.sin(t)]
ax.plot(arc[:-5, 0], arc[:-5, 1], color=P.muted(), lw=1.0)
bio.arrow(ax, arc[-8], arc[-1], kind="process", color=P.muted(), head=0.22)
bio.label(ax, c, "Interphase\n= G1 + S + G2", size="small", color=P.muted())

g1s = seg["G1"][1] + 12
CB.checkpoint(ax, c, r, g1s, width=w, text="G1/S checkpoint\n(restriction point)", text_xy=(7.9, 0.75))
CB.checkpoint(ax, c, r, seg["G2"][1], width=w, text="G2/M checkpoint", text_xy=(2.2, 9.2))
CB.checkpoint(ax, c, r, 82.5, width=w, text="Spindle assembly checkpoint\n(metaphase → anaphase)", text_xy=(6.6, 9.2))

# cyclin-CDK complexes just outside the ring
for ang, text, tok in ((40, "cyclin D–CDK4/6", "positive"), (-38, "cyclin E–CDK2", "channel"),
                       (-150, "cyclin A–CDK2", "dna"), (148, "cyclin B–CDK1", "receptor")):
    th = math.radians(ang)
    p = (c[0] + (r + w / 2 + 0.35) * math.cos(th), c[1] + (r + w / 2 + 0.35) * math.sin(th))
    ha = "left" if math.cos(th) > 0.2 else "right" if math.cos(th) < -0.2 else "center"
    bio.label(ax, p, text, size="small", ha=ha, color=P.edge(tok), bold=True)

# G0 branch from early G1
th = math.radians(8)
a = (c[0] + (r + w / 2) * math.cos(th), c[1] + (r + w / 2) * math.sin(th))
bio.box(ax, (9.35, 5.3), 1.0, 0.6, token="neutral", text="G0", size="small")
bio.arrow(ax, a, (8.8, 5.3), kind="process", bend=-0.15)
bio.arrow(ax, (8.8, 5.05), (a[0] + 0.05, a[1] - 0.35), kind="process", bend=-0.15, color=P.muted())
bio.label(ax, (9.35, 4.7), "quiescence", size="tiny", color=P.muted())

# --- B: Goldbeter oscillator ---------------------------------------------------------------------------------
vi, vd, Kd, kd, Kc, VM1, V2, VM3, V4, K = 0.025, 0.25, 0.02, 0.01, 0.5, 3.0, 1.5, 1.0, 0.5, 0.005


def rhs(_t, y):
    C, M, X = y
    V1, V3 = VM1 * C / (Kc + C), VM3 * M
    return [vi - vd * X * C / (Kd + C) - kd * C,
            V1 * (1 - M) / (K + 1 - M) - V2 * M / (K + M),
            V3 * (1 - X) / (K + 1 - X) - V4 * X / (K + X)]


sol = solve_ivp(rhs, (0, 200), [0.01, 0.01, 0.01], max_step=0.05, rtol=1e-8, atol=1e-10)
keep = sol.t >= 100
t = sol.t[keep] - 100
C, M, X = sol.y[:, keep]

bio.panel(ax, "B", (11.3, 9.85))
pax = Ch.axes_at(ax, (12.6, 1.4, 7.9, 6.9))
on = M > 0.5
edges = np.flatnonzero(np.diff(on.astype(int)))
starts = [t[i] for i in edges if not on[i]]
ends = [t[i] for i in edges if on[i]]
if on[0]:
    starts = [t[0]] + starts
for s0, s1 in zip(starts, ends):
    pax.axvspan(s0, s1, color=P.fill("receptor"), alpha=0.35, lw=0)
pax.plot(t, C, color=Ch.line("highlight"), lw=2.0, label="cyclin $C$ / µM")
pax.plot(t, M, color=Ch.line("receptor"), lw=2.0, label="active CDK1, $M$")
pax.plot(t, X, color=Ch.line("channel"), lw=1.6, ls=(0, (4, 2)), label="active APC/C, $X$")
pax.set_xlim(0, 100)
pax.set_ylim(0, 1.08)
Ch.style_axes(pax, "time / min", "level (C in µM; M, X as fractions)")
leg = pax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.13), ncol=3, frameon=False, fontsize=bio.core.FONT["tiny"],
                 labelcolor=P.ink(), handlelength=2.2, columnspacing=1.2)
bio.label(ax, (12.6, 9.6), "Minimal mitotic oscillator (Goldbeter 1991)", size="normal", bold=True, ha="left")
bio.label(ax, (12.6, 0.35), "shaded: M > 0.5 (mitosis); period ≈ 25 min", size="tiny", ha="left", color=P.muted())
