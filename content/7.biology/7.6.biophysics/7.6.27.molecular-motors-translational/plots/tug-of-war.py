# Tug-of-war model (Mueller, Klumpp and Lipowsky 2008): a cargo carried by N+ plus-end and N- minus-end motors.
# State (n+, n-): bound motors of each kind. Bound motors share the load equally; the cargo velocity follows
# from force balance with linear force-velocity curves (Formula 27.6.2). Each bound motor unbinds at
# eps0 exp(F/Fd) under its load F, each unbound motor binds at pi0. Symmetric tug of war: both teams have the
# kinesin-1 parameters Fs = 6 pN, Fd = 3 pN, eps0 = 1 /s, pi0 = 5 /s, vF = 1 um/s, vB = 6 nm/s and differ only in
# direction. Gillespie simulation. A: a cargo trajectory with 6 + 6 motors (color: direction of motion);
# B: distribution of the cargo velocity over 2000 s for three team compositions (time-weighted).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)
KIN = dict(Fs=6.0, Fd=3.0, e0=1.0, p0=5.0, vF=1.0, vB=0.006)
DYN = dict(KIN)  # mirror-image minus-end motor


def cargo(np_, nm):
    """Cargo velocity (um/s, plus-directed positive) and the load on each motor (pN)."""
    if np_ == 0 and nm == 0:
        return 0.0, 0.0, 0.0
    if nm == 0:
        return KIN["vF"], 0.0, 0.0
    if np_ == 0:
        return -DYN["vF"], 0.0, 0.0
    Sp, Sm = np_ * KIN["Fs"], nm * DYN["Fs"]
    if Sp >= Sm:  # plus motors move forward, minus motors are dragged backward
        vc = (Sp - Sm) / (Sp / KIN["vF"] + Sm / DYN["vB"])
        Fc = Sp * (1 - vc / KIN["vF"])
    else:
        vc = (Sp - Sm) / (Sp / KIN["vB"] + Sm / DYN["vF"])
        Fc = Sm * (1 + vc / DYN["vF"])
    return vc, Fc / np_, Fc / nm


def run(Np, Nm, T):
    t, x, s = 0.0, 0.0, (1, 1)
    ts, xs, vs, ws = [0.0], [0.0], [], []
    while t < T:
        n1, n2 = s
        vc, F1, F2 = cargo(n1, n2)
        r = np.array([n1 * KIN["e0"] * np.exp(F1 / KIN["Fd"]), (Np - n1) * KIN["p0"],
                      n2 * DYN["e0"] * np.exp(F2 / DYN["Fd"]), (Nm - n2) * DYN["p0"]])
        if n1 + n2 == 0:  # detached cargo: rebinding only (diffusion ignored)
            r[[0, 2]] = 0
        R = r.sum()
        dt = rng.exponential(1 / R)
        t += dt
        x += vc * dt
        vs.append(vc); ws.append(dt)
        ts.append(t); xs.append(x)
        k = np.searchsorted(np.cumsum(r), rng.random() * R)
        s = (n1 - 1, n2) if k == 0 else (n1 + 1, n2) if k == 1 else (n1, n2 - 1) if k == 2 else (n1, n2 + 1)
    return np.array(ts), np.array(xs), np.array(vs), np.array(ws)


fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ts, xs, vs, ws = run(6, 6, 60)
ax = axs[0]
seg_col = np.where(vs > 0.05, charts.line("enzyme"), np.where(vs < -0.05, charts.line("protein"), P.muted()))
for i in range(len(vs)):
    ax.plot(ts[i:i + 2], xs[i:i + 2], color=seg_col[i], lw=1.4, solid_capstyle="butt")
ax.plot([], [], color=charts.line("enzyme"), lw=1.6, label="plus runs")
ax.plot([], [], color=charts.line("protein"), lw=1.6, label="minus runs")
ax.plot([], [], color=P.muted(), lw=1.6, label="pauses (stalemate)")
ax.legend(fontsize=7.5, frameon=False, loc="best")
ax.set_xlim(0, 60)
charts.style_axes(ax, "$t$ / s", "cargo position / µm")
charts.title(ax, "A   Saltatory bidirectional transport (6 + 6 motors)")

ax = axs[1]
bins = np.linspace(-1.05, 1.05, 43)
for (Np, Nm), tok in (((6, 6), "neutral"), ((7, 6), "enzyme"), ((6, 7), "protein")):
    _, _, v, w = run(Np, Nm, 2000)
    h, e = np.histogram(v, bins, weights=w, density=True)
    ax.step(0.5 * (e[1:] + e[:-1]), h, where="mid", color=charts.line(tok), lw=1.6,
            label=f"{Np} plus, {Nm} minus motors (mean {np.sum(v * w) / w.sum() * 1000:.0f} nm/s)")
ax.set_yscale("log")
ax.set_ylim(1e-2, 200)
ax.legend(fontsize=7.5, frameon=False, loc="upper center")
charts.style_axes(ax, "cargo velocity / (µm s$^{-1}$)", "fraction of time (density)")
charts.title(ax, "B   Small changes in team size switch the direction")
fig.tight_layout()
