"""Three models of proximo-distal patterning, simulated.

A: progress zone model (Formula 31.5.1). The distal d = 200 um of the bud proliferate (cycle 12 h), proximal cells
do not; trajectories of cells starting at geometrically spaced distances from the tip, coloured by the time spent in
the zone (stylopod < 24 h, zeugopod 24-48 h, autopod > 48 h).
B: two-signal model (Formula 31.5.2): proximal and distal signals with decay length 50 um and threshold 0.1 in a
bud of 300 um define three domains at t = 0, which then expand by uniform growth (fivefold in 72 h).
C: signal plus timer: the same growth as in A; cells that leave the zone while within the range of the proximal
signal (x < 140 um) become stylopod; the others start a timer when they leave the signal's range and become
zeugopod if they leave the zone within 24 h of that, autopod otherwise.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
TOK = {"stylopod": "humerus", "zeugopod": "radius", "autopod": "phalanges"}
fig, ax = bio.canvas(30.0, 10.0)

d, g = 200.0, np.log(2) / 12.0
dt, T = 0.05, 72.0
t = np.arange(0, T + dt, dt)
ell = d + g * d * t
y0 = d * 0.5 ** np.linspace(0.15, 6.5, 28)       # distance from the tip at t = 0
x = (d - y0).astype(float)                        # distance from the base
X = np.zeros((len(t), len(x)))
X[0] = x
exit_t = np.full(len(x), np.nan)
esc_t = np.full(len(x), np.nan)
xc = 140.0
for k in range(1, len(t)):
    lo = ell[k - 1] - d
    v = np.where(x > lo, g * (x - lo), 0.0)
    x = x + v * dt
    X[k] = x
    newly = np.isnan(exit_t) & (x <= ell[k] - d)
    exit_t[newly] = t[k]
    esc = np.isnan(esc_t) & (x > xc)
    esc_t[esc] = t[k]


def ident_pz(te):
    te = T if np.isnan(te) else te
    return "stylopod" if te < 24 else "zeugopod" if te < 48 else "autopod"


def ident_timer(i):
    te = T if np.isnan(exit_t[i]) else exit_t[i]
    if np.isnan(esc_t[i]) or esc_t[i] > te:
        return "stylopod"
    return "zeugopod" if te - esc_t[i] < 24 else "autopod"


def traj_panel(rect, idf, title, letter, shade=None):
    pa = C.axes_at(ax, rect)
    if shade is not None:
        pa.axhspan(0, shade, color=P.mix(P.fill("highlight"), P.surface(), 0.55 if P.is_dark() else 0.6), lw=0)
        pa.text(2, shade - 30, "proximal signal", fontsize=bio.core.FONT["tiny"], color=P.muted(), va="top")
    pa.fill_between(t, ell - d, ell, color=P.mix(P.fill("pz") if False else P.fill("positive"), P.surface(), 0.72), lw=0)
    pa.plot(t, ell, color=P.ink(), lw=1.4)
    for i in range(X.shape[1]):
        idn = idf(i)
        pa.plot(t, X[:, i], color=Q.line_color(TOK[idn]), lw=1.2)
    pa.set_xlim(0, T)
    pa.set_ylim(0, ell[-1] * 1.02)
    pa.set_xticks([0, 24, 48, 72])
    C.style_axes(pa, "t / h", "distance from base / µm")
    bio.panel(ax, letter, (rect[0] - 1.4, 9.8))
    bio.label(ax, (rect[0], 9.6), title, size="small", bold=True, ha="left", va="top")
    return pa


pa = traj_panel((1.6, 1.4, 7.4, 7.4), lambda i: ident_pz(exit_t[i]), "Progress zone (timing)", "A")
pa.text(52, d + g * d * 52 + 25, "tip", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="right")

# B: two signals
pb = C.axes_at(ax, (11.6, 1.4, 7.4, 7.4))
lam, th, L0 = 50.0, 0.1, 300.0
b1 = lam * np.log(1 / th)
b2 = L0 - b1
G = np.log(5) / T
s = np.exp(G * t)
pb.fill_between(t, 0, b1 * s, color=Q.line_color("humerus"), lw=0, alpha=0.85)
pb.fill_between(t, b1 * s, b2 * s, color=Q.line_color("radius"), lw=0, alpha=0.85)
pb.fill_between(t, b2 * s, L0 * s, color=Q.line_color("phalanges"), lw=0, alpha=0.85)
for name, y in (("stylopod", b1 * 2.2), ("zeugopod", (b1 + b2) / 2 * 3.3), ("autopod", (b2 + L0) / 2 * 4.2)):
    pb.text(T * (0.32 if name == "stylopod" else 0.55 if name == "zeugopod" else 0.78) - 4, y, name,
            fontsize=bio.core.FONT["tiny"], color=P.on_fill(), ha="center", va="center")
pb.set_xlim(0, T)
pb.set_ylim(0, L0 * 5 * 1.02)
pb.set_xticks([0, 24, 48, 72])
C.style_axes(pb, "t / h", "distance from base / µm")
bio.panel(ax, "B", (10.2, 9.8))
bio.label(ax, (11.6, 9.6), "Two signals, then growth", size="small", bold=True, ha="left", va="top")

traj_panel((21.6, 1.4, 7.4, 7.4), ident_timer, "Signal plus timer", "C", shade=xc)
# legend
for k, (nm, tk) in enumerate(TOK.items()):
    yy = 7.9 - 0.55 * k
    ax.plot([2.5, 3.2], [yy, yy], color=Q.line_color(tk), lw=2.2)
    bio.label(ax, (3.35, yy), nm, size="tiny", ha="left")
