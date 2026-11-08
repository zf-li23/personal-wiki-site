"""Firing-rate model of the basal ganglia direct and indirect pathways and the effect of dopamine.

Each population x obeys tau dx/dt = -x + F(input), F(u) = max(0, u), tau = 10 ms (rates in
spikes/s). Cortex c(t) = 2 at rest and 12 during a 0.6 s motor command.
  D1 striatum  = F(g (1 + d) c - 10)              direct pathway, dopamine excites (D1)
  D2 striatum  = F(h g (1 - d) c - 10)            indirect pathway, dopamine inhibits (D2)
  GPe          = F(65 - 1.5 D2 + 0.4 STN)
  STN          = F(75 - 0.8 GPe + 0.5 c)
  GPi/SNr      = F(55 - 1.8 D1 + STN)          tonic inhibitory output
  Thalamus     = F(40 - 0.6 GPi + 1.5 c)
g = 2; d = dopamine level (0 normal, -0.6 depleted as in Parkinson disease, +0.5 excess);
h = 1 normally and 0.3 when indirect-pathway striatal neurons are lost (early Huntington disease).
A: time courses of GPi/SNr and thalamus. B: thalamic rate during the command against d.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
F = lambda u: np.maximum(0.0, u)  # noqa: E731
tau, dt = 0.01, 0.0005
g = 2.0


def run(d=0.0, h=1.0, dur=1.6):
    n = int(dur / dt)
    t = np.arange(n) * dt
    c = np.where((t > 0.5) & (t < 1.1), 12.0, 2.0)
    x = dict(d1=0.0, d2=0.0, gpe=72.3, stn=18.2, gpi=73.2, th=0.0)
    out = {kk: np.zeros(n) for kk in x}
    for i in range(n):
        tgt = dict(
            d1=F(g * (1 + d) * c[i] - 10),
            d2=F(h * g * (1 - d) * c[i] - 10),
            gpe=F(65 - 1.5 * x["d2"] + 0.4 * x["stn"]),
            stn=F(75 - 0.8 * x["gpe"] + 0.5 * c[i]),
            gpi=F(55 - 1.8 * x["d1"] + 1.0 * x["stn"]),
            th=F(40 - 0.6 * x["gpi"] + 1.5 * c[i]),
        )
        for kk in x:
            x[kk] += dt / tau * (tgt[kk] - x[kk])
            out[kk][i] = x[kk]
    return t, out


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0), gridspec_kw=dict(width_ratios=[1.4, 1]))
cases = [("Normal", 0.0, 1.0, P.edge("dna")),
         ("Dopamine loss (PD-like)", -0.6, 1.0, P.edge("rna")),
         ("Indirect loss (HD-like)", 0.0, 0.3, P.edge("enzyme"))]
for lab, d, h, col in cases:
    t, o = run(d, h)
    ax.plot(t, o["gpi"], color=col, lw=1.4, ls="--")
    ax.plot(t, o["th"], color=col, lw=2.0, label=lab)
ax.axvspan(0.5, 1.1, color=P.muted(), alpha=0.12, lw=0, zorder=0)
ax.text(0.8, 36, "cortical command", ha="center", fontsize=8, color=P.muted())
ax.set_ylim(0, 115)
ax.set_xlim(0, 1.6)
ax.set_xlabel("Time / s")
ax.set_ylabel("Rate / (spikes/s)")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.text(1.17, 40, "dashed: GPi/SNr\nsolid: thalamus", fontsize=8, color=P.muted())
ax.set_title("A  Output disinhibits the thalamus", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)

ds = np.linspace(-0.8, 0.6, 29)
for h, col, lab in ((1.0, P.edge("dna"), "intact indirect pathway"),
                    (0.3, P.edge("enzyme"), "indirect pathway reduced")):
    th, gp = [], []
    for d in ds:
        t, o = run(d, h)
        sel = (t > 0.9) & (t < 1.1)
        th.append(o["th"][sel].mean())
        gp.append(o["gpi"][sel].mean())
    bx.plot(ds, th, color=col, lw=2, label=lab)
    bx.plot(ds, gp, color=col, lw=1.2, ls="--")
bx.axvline(0, color=P.muted(), lw=0.8)
bx.set_xlabel("Dopamine level d")
bx.set_ylabel("Rate during command / (spikes/s)")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Dopamine sets the gain of the gate", loc="left", fontsize=10)
bx.grid(True, alpha=0.3)
fig.tight_layout()
