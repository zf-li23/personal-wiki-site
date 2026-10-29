"""Which minimum does a system choose? Perfect delay, Maxwell convention and noise in the cusp.

Overdamped dynamics in the cusp potential phi = x^4 + 6 u x^2 + 4 v x at u = -0.5 with noise:
dx = -phi'(x) dt + sqrt(2 D) dW, while the control v is swept slowly from -1.2 to 1.2 and back
(one cycle in time 400, Euler-Maruyama with dt = 0.005).
A: x against v for D = 0 (perfect delay: the state jumps only where its minimum disappears, at the
fold points v = +-2(-u)^(3/2) = +-0.71, a wide hysteresis loop), D = 0.1 and D = 0.3 (the loop narrows
towards the Maxwell switch at v = 0, where the two minima are equally deep).
B: mean switching value of v on the upward sweep against noise D (8 sweeps per point), between the
perfect-delay limit 0.71 and the Maxwell limit 0.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(3)
u = -0.5
dt, T = 0.005, 400.0
n = int(T / dt)
tt = np.arange(n) * dt
vt = np.where(tt < T / 2, -1.2 + 2.4 * tt / (T / 2), 1.2 - 2.4 * (tt - T / 2) / (T / 2))


def run(D, x0=-1.2):
    x = x0
    xs = np.empty(n)
    noise = rng.standard_normal(n) * np.sqrt(2 * D * dt)
    for i in range(n):
        v = vt[i]
        x += -(4 * x ** 3 + 12 * u * x + 4 * v) * dt + noise[i]
        xs[i] = x
    return xs


fig, ax = bio.canvas(28.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 11.0, 7.0))
for D, tok in ((0.0, "protein"), (0.1, "highlight"), (0.3, "mesoderm")):
    xs = run(D, x0=1.2)
    pa.plot(vt[::20], xs[::20], color=quant.line_color(tok), lw=1.2 if D > 0 else 2.0, label=f"D = {D:g}",
            alpha=0.9 if D > 0 else 1.0)
vc = 2 * (-u) ** 1.5
for v0 in (vc, -vc):
    pa.axvline(v0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.axvline(0, color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
pa.text(vc + 0.02, 1.6, "fold", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.text(0.02, 1.6, "Maxwell", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(-1.2, 1.2)
pa.set_ylim(-1.9, 1.9)
charts.style_axes(pa, "control v", "state x")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower left")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pa, "Hysteresis narrows with noise")

bio.panel(ax, "B", (15.0, 9.9))
pb = charts.axes_at(ax, (17.0, 1.8, 10.0, 7.0))
Ds = [0.0, 0.025, 0.05, 0.1, 0.2, 0.4]
half = n // 2
sw = []
for D in Ds:
    vals = []
    for _ in range(8 if D > 0 else 1):
        xs = run(D, x0=1.2)[:half]
        k = np.argmax(xs < -0.3)
        vals.append(vt[k])
    sw.append(np.mean(vals))
pb.plot(Ds, sw, "o-", color=quant.line_color("protein"), lw=1.8, ms=4)
pb.axhline(vc, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.axhline(0, color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
pb.text(0.2, vc + 0.03, "perfect delay", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.text(0.2, 0.03, "Maxwell convention", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xlim(-0.01, 0.42)
pb.set_ylim(-0.1, 0.85)
charts.style_axes(pb, "noise D", "switching value of v (upward sweep)")
charts.title(pb, "Between the two conventions")
