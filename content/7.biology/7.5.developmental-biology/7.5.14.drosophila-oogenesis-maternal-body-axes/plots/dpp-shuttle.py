# The shuttling mechanism that concentrates Dpp at the dorsal midline (Formula 14.6.1), solved on the half-
# circumference 0 <= s <= 1 (ventral midline 0, dorsal midline 1) with no-flux ends; dimensionless units. Dpp (M) is
# made in the dorsal 40 % and hardly diffuses on its own; Sog (S) is made in excess in the lateral neuroectoderm
# (0.3 <= s < 0.6) and diffuses; the Dpp-Sog complex (C) diffuses and is cleaved by Tolloid, present dorsally, which
# releases Dpp. A: free Dpp with the shuttle (solid) and without Sog (dashed): without Sog Dpp simply fills the
# region where it is made; with Sog it is carried to and released at the midline, the point farthest from the Sog
# source. B: the same profile for half, normal and double Dpp production; the threshold for the highest fate
# (amnioserosa, dotted) is crossed only near the midline in all three.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N = 81
s = np.linspace(0, 1, N)
ds = s[1] - s[0]
dors = (s >= 0.6).astype(float)
lat = ((s >= 0.3) & (s < 0.6)).astype(float)
Dm, Ds = 0.0005, 0.05
kon, koff, lam, km, ks = 50.0, 0.1, 1.0, 1.0, 0.05


def lap(u):
    out = np.empty_like(u)
    out[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
    out[0] = 2 * (u[1] - u[0])
    out[-1] = 2 * (u[-2] - u[-1])
    return out / ds ** 2


def run(etaM=1.0, etaS=10.0, T=30.0):
    M = np.zeros(N); S = np.zeros(N); Cc = np.zeros(N)
    dt = 0.2 * ds ** 2 / Ds
    for _ in range(int(T / dt)):
        b = kon * M * S - koff * Cc
        cut = lam * dors * Cc
        M = M + dt * (Dm * lap(M) - b + cut - km * M + etaM * dors)
        S = S + dt * (Ds * lap(S) - b - ks * S + etaS * lat)
        Cc = Cc + dt * (Ds * lap(Cc) + b - cut)
    return M


M1 = run()
M0 = run(etaS=0.0)
Mh = run(etaM=0.5)
M2 = run(etaM=2.0)

fig, ax = bio.canvas(20.0, 7.8)
pa = C.axes_at(ax, (1.6, 1.4, 7.8, 5.4))
pa.axvspan(0.3, 0.6, color=P.fill("protein"), alpha=0.25, lw=0)
pa.axvspan(0.6, 1.0, color=P.fill("highlight"), alpha=0.25, lw=0)
pa.plot(s, M1, color=C.line("highlight"), lw=2.0, label="with Sog")
pa.plot(s, M0, color=P.muted(), lw=1.4, ls=(0, (4, 3)), label="no Sog")
top = M1.max() * 1.1
pa.set_ylim(0, top)
pa.text(0.45, top * 0.9, "sog made", fontsize=bio.core.FONT["tiny"], ha="center", style="italic", color=P.muted())
pa.text(0.8, top * 0.9, "dpp, tolloid made", fontsize=bio.core.FONT["tiny"], ha="center", style="italic", color=P.muted())
pa.set_xlim(0, 1)
C.style_axes(pa, "s (ventral midline 0 → dorsal midline 1)", "free Dpp")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center left")
bio.panel(ax, "A", (0.2, 7.7))
pb = C.axes_at(ax, (12.2, 1.4, 7.0, 5.4))
for M, f, t in [(Mh, "× 0.5", 0.7), (M1, "× 1", 0.35), (M2, "× 2", 0.0)]:
    pb.plot(s, M, color=P.mix(C.line("highlight"), P.surface(), t), lw=1.8, label="Dpp production " + f)
pb.axhline(2.0, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pb.text(0.52, 2.15, "threshold for amnioserosa", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xlim(0.5, 1)
pb.set_ylim(0, M2.max() * 1.08)
C.style_axes(pb, "s", "free Dpp")
pb.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.8, 7.7))
