"""Propagation of the action potential along an unmyelinated axon: the Hodgkin-Huxley membrane
(6.3 C) coupled by the cable equation, C dV/dt = (a / 2 R_i) d2V/dx2 - I_ion, with axoplasm resistivity
R_i = 35.4 Ohm cm, solved by finite differences (explicit in V, sealed ends) after a stimulus at x = 0.
A: membrane potential in space and time for the squid giant axon (radius a = 238 um): a pulse of fixed
shape travels at constant speed (slope of the band). B: snapshots of V(x) at three times; the
refractory tail behind the spike prevents backward propagation. C: conduction velocity from
simulations with radii from 3 to 300 um (dots) follows v proportional to the square root of the
diameter (line), compared with the empirical line for myelinated mammalian fibers, v of about 6 m/s per
um of outer diameter (Hursh 1939), which is proportional to the diameter; note the different
temperatures, which make the comparison qualitative."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import neuro

P = bio.P
FT = bio.core.FONT
p = neuro.HH


def run(a, L_nodes=200, tmax=None, record=False):
    Ri, C = 35.4, 1.0
    Dc = 1000 * a / (2 * Ri * C)  # cm^2/ms
    dx = 0.05 * np.sqrt(a / 0.0238)
    dt = 0.3 * dx * dx / Dc
    dt = min(dt, 0.005)
    n = L_nodes
    V = np.full(n, -65.0)
    m, h, nn = [np.full(n, x) for x in neuro.hh_steady(-65.0)]
    t = 0.0
    tmax = tmax or 6.0 * np.sqrt(0.0238 / a) + 4
    rec, times = [], []
    cross = {}
    step = 0
    while t < tmax:
        am, bm, ah, bh, an, bn = neuro.hh_rates(V)
        Iion = p["gNa"] * m ** 3 * h * (V - p["ENa"]) + p["gK"] * nn ** 4 * (V - p["EK"]) + p["gL"] * (V - p["EL"])
        lap = np.empty(n)
        lap[1:-1] = V[2:] - 2 * V[1:-1] + V[:-2]
        lap[0] = 2 * (V[1] - V[0])
        lap[-1] = 2 * (V[-2] - V[-1])
        Istim = np.zeros(n)
        if t < 0.5:
            Istim[:5] = 200.0
        V = V + dt * (Dc * lap / dx ** 2 + (Istim - Iion) / C)
        m = m + dt * (am * (1 - m) - bm * m)
        h = h + dt * (ah * (1 - h) - bh * h)
        nn = nn + dt * (an * (1 - nn) - bn * nn)
        t += dt
        for k in (60, 140):
            if k not in cross and V[k] > 0:
                cross[k] = t
        step += 1
        if record and step % max(1, int(0.02 / dt)) == 0:
            rec.append(V.copy())
            times.append(t)
    v = (80 * dx) / (cross[140] - cross[60]) * 10 if (60 in cross and 140 in cross) else np.nan  # cm/ms -> m/s
    return v, dx, np.array(times), np.array(rec)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.4, left=0.06, right=0.98, bottom=0.17, top=0.87)
v0, dx0, times, rec = run(0.0238, tmax=8.0, record=True)
x = np.arange(rec.shape[1]) * dx0

ax = axs[0]
im = ax.imshow(rec.T, aspect="auto", origin="lower", extent=[times[0], times[-1], 0, x[-1]], cmap="magma",
               vmin=-80, vmax=45)
cb = fig.colorbar(im, ax=ax, pad=0.02)
cb.ax.tick_params(labelsize=FT["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.set_label("V / mV", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "time / ms", "position / cm", box=True)
charts.title(ax, f"A  Squid axon, v = {v0:.1f} m/s")

ax = axs[1]
for tt, tok in [(2.0, "dna"), (4.0, "bacterium"), (6.0, "blood")]:
    i = np.argmin(np.abs(times - tt))
    ax.plot(x, rec[i], color=charts.line(tok), lw=1.5, label=f"t = {tt:g} ms")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "position / cm", "V / mV")
charts.title(ax, "B  Travelling spike")

ax = axs[2]
radii = np.array([3e-4, 1e-3, 3e-3, 1e-2, 3e-2])
vs = np.array([run(a)[0] for a in radii])
d_um = 2 * radii * 1e4
ax.loglog(d_um, vs, "o", color=charts.line("neuron"), ms=5, label="HH cable (6.3 °C)")
c = np.exp(np.mean(np.log(vs) - 0.5 * np.log(d_um)))
dd = np.logspace(0, 3, 50)
ax.loglog(dd, c * np.sqrt(dd), color=charts.line("neuron"), lw=1.0, label=r"$\propto\sqrt{d}$ unmyelinated")
dm = np.logspace(0, 1.4, 20)
ax.loglog(dm, 6 * dm, "--", color=charts.line("lipid_head"), lw=1.5, label=r"myelinated, $\approx 6\,d$ (37 °C)")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"fiber diameter $d$ / $\mu$m", "conduction velocity / m s$^{-1}$")
charts.title(ax, "C  Velocity and diameter")
