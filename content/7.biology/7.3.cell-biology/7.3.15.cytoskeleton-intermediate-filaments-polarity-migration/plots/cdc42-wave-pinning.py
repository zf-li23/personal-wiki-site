"""Spontaneous polarization by a conserved GTPase: the wave-pinning model (Mori, Jilkine and Edelstein-Keshet
2008), a minimal model of Cdc42 polarity.

a(x, t): active, membrane-bound GTPase (slow diffusion D_a); b(x, t): inactive, cytosolic GTPase (fast D_b).
    da/dt = D_a d2a/dx2 + f(a, b),    db/dt = D_b d2b/dx2 - f(a, b),
    f(a, b) = b (k0 + gamma a^2 / (K^2 + a^2)) - delta a,
on a one-dimensional cell of length L = 10 um with no-flux ends, so that the total amount is conserved.
The Hill term is positive feedback (active GTPase recruits its own GEF, as Cdc42-GTP recruits the
Bem1-Cdc24 complex in yeast). Parameters: D_a = 0.1, D_b = 10 um^2/s, k0 = 0.067, gamma = 1, delta = 1 per s,
K = 1; the cell starts homogeneous (a = 0.27, b = 2.0) with a transient stimulus raising a near x = 0.
A: kymograph of a: the front of activation travels into the cell and stops (is pinned) as the cytosolic
pool is depleted. B: final profiles of a and b. C: total active GTPase against time for the stimulated cell
and for one with a weak stimulus that decays back to the uniform state (a threshold).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
L, nx = 10.0, 101
x = np.linspace(0, L, nx)
dx = x[1] - x[0]
Da, Db, k0, gam, K, dl = 0.1, 10.0, 0.067, 1.0, 1.0, 1.0
dt = 0.2 * dx * dx / Db


def lap(u):
    out = np.empty_like(u)
    out[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
    out[0] = 2 * (u[1] - u[0])
    out[-1] = 2 * (u[-2] - u[-1])
    return out / dx**2


def run(amp, T=60.0, snap=0.5):
    a = np.full(nx, 0.2683312)
    b = np.full(nx, 2.0)
    a = a + amp * np.exp(-(x / 1.0) ** 2)
    ks, ts, tot = [], [], []
    nsnap = int(round(snap / dt))
    for i in range(int(T / dt)):
        f = b * (k0 + gam * a**2 / (K**2 + a**2)) - dl * a
        a = a + dt * (Da * lap(a) + f)
        b = b + dt * (Db * lap(b) - f)
        if i % nsnap == 0:
            ks.append(a.copy()); ts.append(i * dt); tot.append(a.mean())
    return a, b, np.array(ks), np.array(ts), np.array(tot)


a, b, ks, ts, tot = run(1.5)
_, _, _, ts2, tot2 = run(0.12)

fig, ax = bio.canvas(27.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.7, 1.4, 7.6, 6.0))
im = pa.imshow(ks.T, origin="lower", aspect="auto", extent=(0, ts[-1], 0, L), cmap="magma" if P.is_dark() else "magma_r")
charts.style_axes(pa, "time / s", "position x / µm")
charts.title(pa, "Active GTPase a(x, t)")

bio.panel(ax, "B", (10.6, 8.3))
pb = charts.axes_at(ax, (12.2, 1.4, 6.4, 6.0))
pb.plot(x, a, color=quant.line_color("drug"), lw=1.8, label="active, membrane (a)")
pb.plot(x, b, color=quant.line_color("channel"), lw=1.8, label="inactive, cytosol (b)")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
pb.set_ylim(0, 3.2)
charts.style_axes(pb, "position x / µm", "concentration (a.u.)")
charts.title(pb, "Pinned front: one polar cap")

bio.panel(ax, "C", (19.8, 8.3))
pc = charts.axes_at(ax, (21.4, 1.4, 5.3, 6.0))
pc.plot(ts, tot, color=quant.line_color("drug"), lw=1.8, label="strong stimulus")
pc.plot(ts2, tot2, color=quant.line_color("muted"), lw=1.6, ls=(0, (4, 2)), label="weak stimulus")
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(pc, "time / s", "mean active GTPase")
charts.title(pc, "A threshold for polarization")
