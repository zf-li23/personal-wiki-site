"""Reading a gradient with switches.

A: the two-level switch dg/dt = s + g^2 / (1 + g^2) - g / (2K) (K = 2, s = gamma a the activator input).
Steady states (solid stable, dashed unstable) form an S-shaped curve; for s = 0 the states g = 0 and
g = K + sqrt(K^2 - 1) = 3.73 are both stable. Above s* (the largest input for which a low state still exists, here
s* = 0.016) only the high state remains. B: a pulse of activator (s = 4 s*, 20 < t < 50) above s* switches the gene on, and it stays on after the activator has
gone (memory). C: a sequential (ratchet) switch: N = 4 autocatalytic genes g_i share a repressor r,
dg_i/dt = g_i^2 / r - g_i + e_i(m) g_(i-1), dr/dt = 10 (sum g_i^2 - r), with e_i(m) = 0.5 m^8 / (m^8 + theta_i^8),
theta = 0.25, 0.5, 0.8. Gene 1 is on at the start; a rising morphogen m lets gene i - 1 hand over to gene i
once m exceeds theta_i, and the common repressor keeps only one gene on. Cells in a gradient
m = 1.3 exp(-x / 0.35) end in four states that form a French flag with four colours. D: the hand-over in the cell
at x = 0 as m rises (dashed: m).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import development as D
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(26.0, 17.0)
K = 2.0

# A: steady states s(g) = g / (2K) - g^2 / (1 + g^2)
g = np.linspace(0, 4.5, 2000)
s = g / (2 * K) - g**2 / (1 + g**2)
ds = np.gradient(s, g)
pa = C.axes_at(ax, (1.8, 10.0, 9.0, 5.6))
stable = ds > 0
for mask, ls in ((stable, "-"), (~stable, (0, (3, 2)))):
    gg = np.where(mask, g, np.nan)
    pa.plot(np.where(mask, s, np.nan), gg, color=Q.line_color("protein"), lw=2.0, ls=ls)
low = g < K - np.sqrt(K * K - 1)
sstar = s[low].max()
pa.axvline(sstar, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pa.text(sstar + 0.006, 2.0, "s*", color=P.edge("highlight"), fontsize=FS["small"])
pa.axvline(0, color=P.muted(), lw=0.7)
pa.axvspan(-0.36, 0, color=P.fill("neutral"), alpha=0.25, lw=0)
pa.text(-0.34, 4.2, "s < 0 (shown to\ncomplete the curve)", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(-0.36, 0.1)
pa.set_ylim(0, 4.6)
C.style_axes(pa, "activator input s = γa", "steady state g*")
bio.panel(ax, "A", (0.3, 16.4))
bio.label(ax, (1.8, 16.4), "Two-level switch: steady states", size="small", bold=True, ha="left")

# B: memory
dt = 0.01
t = np.arange(0, 150, dt)
sa = np.where((t > 20) & (t < 50), 4.0 * sstar, 0.0)
gt = np.zeros_like(t)
for i in range(1, len(t)):
    gg = gt[i - 1]
    gt[i] = gg + dt * (sa[i - 1] + gg * gg / (1 + gg * gg) - gg / (2 * K))
pb = C.axes_at(ax, (14.8, 10.0, 9.8, 5.6))
pb.plot(t, gt, color=Q.line_color("protein"), lw=2.0, label="g")
pb.fill_between(t, 0, sa / sstar, color=P.fill("highlight"), alpha=0.5, lw=0, label="input s / s*")
pb.set_xlim(0, 150)
pb.set_ylim(0, 4.3)
pb.set_yticks([0, 1, 2, 3, 4])
C.style_axes(pb, "time", "g")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (13.3, 16.4))
bio.label(ax, (14.8, 16.4), "A transient input is remembered", size="small", bold=True, ha="left")

# C and D: sequential switch
th = np.array([0.0, 0.25, 0.5, 0.8])
N = 4


def run(mfun, ncell, Tend=150.0, dt=0.01, keep=False):
    gv = np.zeros((ncell, N))
    gv[:, 0] = 1.0
    r = np.ones(ncell)
    rec = []
    for i in range(int(Tend / dt)):
        m = mfun(i * dt)[:, None]
        e = 0.5 * m**8 / (m**8 + np.maximum(th, 1e-9) ** 8)
        e[:, 0] = 0.0
        gp = np.concatenate([np.zeros((ncell, 1)), gv[:, :-1]], axis=1)
        dg = gv * gv / r[:, None] - gv + e * gp
        r = r + dt * 10 * ((gv * gv).sum(1) - r)
        gv = gv + dt * dg
        if keep and i % 20 == 0:
            rec.append((i * dt, float(mfun(i * dt)[0]), gv[0].copy()))
    return gv, rec


ncell = 20
xc = (np.arange(ncell) + 0.5) / ncell
mfin = 1.3 * np.exp(-xc / 0.35)
gfin, _ = run(lambda tt: mfin * min(1.0, tt / 60.0), ncell)
state = gfin.argmax(1)
toks = ["neutral", "highlight", "na", "negative"]
pc = C.axes_at(ax, (1.8, 4.2, 9.0, 3.4))
pc.plot(xc, mfin, color=P.ink(), lw=1.8)
for tval in th[1:]:
    pc.axhline(tval, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pc.set_xlim(0, 1)
pc.set_ylim(0, 1.4)
C.style_axes(pc, None, "final m")
pc.set_xticks([])
D.cell_row(ax, 1.8, 10.8, 2.6, list(state), toks, h=1.0)
for k in range(N):
    bio.label(ax, (2.3 + 2.2 * k, 1.3), f"gene {k + 1} on", size="tiny", color=P.edge(toks[k]))
bio.panel(ax, "C", (0.3, 8.6))
bio.label(ax, (1.8, 8.6), "Sequential switch in a gradient", size="small", bold=True, ha="left")

_, rec = run(lambda tt: np.array([1.3 * min(1.0, tt / 60.0)]), 1, keep=True)
tt = np.array([r[0] for r in rec])
mm = np.array([r[1] for r in rec])
G = np.array([r[2] for r in rec])
pd = C.axes_at(ax, (14.8, 1.6, 9.8, 6.0))
for k in range(N):
    pd.plot(tt, G[:, k], color=Q.line_color(toks[k]), lw=1.8, label=f"$g_{k + 1}$")
pd.plot(tt, mm, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="m")
pd.set_xlim(0, 100)
pd.set_ylim(0, 1.4)
C.style_axes(pd, "time", "gene activity")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=5)
bio.panel(ax, "D", (13.3, 8.6))
bio.label(ax, (14.8, 8.6), "Hand-over as the morphogen rises", size="small", bold=True, ha="left")
