"""Gradient sensing by local excitation and global inhibition (LEGI; Levchenko and Iglesias 2002).

Around the perimeter of a cell (angle phi), receptor occupancy S(phi) drives a local activator E (slow
diffusion) and an inhibitor I that diffuses fast and therefore reports the mean occupancy of the whole cell:
    dE/dt = k_e S - k_-e E,      dI/dt = k_i <S> - k_-i I,
    dR/dt = k_r E (1 - R) - k_-r I R,
where R is the fraction of an effector (for example PI(3,4,5)P3 or Ras-GTP) activated at each point of the
membrane. Rate constants: k_e = k_-e = 1 per s (fast excitation), k_i = k_-i = 0.1 per s (slower inhibition),
k_r = k_-r = 1 per s.
A: a uniform step increase of chemoattractant at t = 10 s: R rises transiently and returns to the same
baseline (perfect adaptation), because at steady state E and I are both proportional to S.
B: steady-state response around the cell in a 10 % gradient (S = S0 (1 + 0.05 cos phi)) for three mean
concentrations: the front-to-back difference is the same at every mean concentration, because R depends only
on S / <S>; LEGI senses the relative gradient and ignores the absolute level. The response gradient is as
shallow as the stimulus gradient; in cells, positive feedback downstream (Rac, PI3K, actin) amplifies it.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
ke, kme, ki, kmi, kr, kmr = 1.0, 1.0, 0.1, 0.1, 1.0, 1.0
dt = 0.01


def simulate(Sfun, T, n=64):
    phi = np.linspace(-np.pi, np.pi, n, endpoint=False)
    S0 = Sfun(0.0, phi)
    E = ke * S0 / kme
    I = ki * S0.mean() / kmi * np.ones(n)
    R = kr * E / (kr * E + kmr * I)
    ts, Rf, Rb = [], [], []
    for i in range(int(T / dt)):
        t = i * dt
        S = Sfun(t, phi)
        E = E + dt * (ke * S - kme * E)
        I = I + dt * (ki * S.mean() - kmi * I)
        R = R + dt * (kr * E * (1 - R) - kmr * I * R)
        ts.append(t); Rf.append(R[n // 2]); Rb.append(R[0])
    return phi, R, np.array(ts), np.array(Rf), np.array(Rb)


fig, ax = bio.canvas(22.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.8, 1.4, 8.0, 6.0))
for amp, tk in ((2.0, "drug"), (5.0, "protein")):
    _, _, ts, Rf, _ = simulate(lambda t, p, a=amp: np.ones_like(p) * (1.0 if t < 10 else a), 80)
    pa.plot(ts, Rf, color=quant.line_color(tk), lw=1.8, label=f"uniform step 1 → {amp:g}")
pa.axvline(10, color=quant.line_color("muted"), lw=0.8, ls=(0, (3, 2)))
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pa, "time / s", "response R")
charts.title(pa, "Perfect adaptation to uniform stimuli")

bio.panel(ax, "B", (11.4, 8.3))
pb = charts.axes_at(ax, (13.2, 1.4, 8.0, 6.0))
for S0, tk in ((0.1, "channel"), (1.0, "enzyme"), (10.0, "drug")):
    phi, R, *_ = simulate(lambda t, p, s=S0: s * (1 + 0.05 * np.cos(p)), 120)
    pb.plot(np.degrees(phi), R, color=quant.line_color(tk), lw=1.8, ls="-" if S0 == 1.0 else (0, (4, 2)) if S0 > 1 else ":",
            label=f"mean S = {S0:g}")
pb.set_xticks([-180, -90, 0, 90, 180])
pb.set_xticklabels(["back", "−90°", "front", "90°", "back"])
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower center")
charts.style_axes(pb, "position on the cell perimeter", "steady-state response R")
charts.title(pb, "Relative gradient sensing (10 % gradient)")
