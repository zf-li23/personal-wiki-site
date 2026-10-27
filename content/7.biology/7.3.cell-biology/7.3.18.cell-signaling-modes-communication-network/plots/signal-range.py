"""How far a secreted signal reaches: diffusion against removal.

A signal released from a planar source, diffusing with coefficient D and removed with first-order rate
constant k (degradation, uptake, capture by receptors), reaches the steady profile c(x) = c0 exp(-x/lambda)
with lambda = sqrt(D/k).
A: profiles for acetylcholine in a neuromuscular cleft (D about 400 um^2/s, hydrolysis by
acetylcholinesterase with k of order 1e4 /s: lambda about 0.2 um), nitric oxide in tissue (D about
3300 um^2/s, k about 1 /s: lambda about 60 um) and the morphogen Dpp in the Drosophila wing disc
(effective D = 0.1 um^2/s, k = 2.5e-4 /s, Kicheva and colleagues 2007: lambda about 20 um).
The shaded band is the size of one cell (10-20 um).
B: lambda as a function of D and k (contours); the three signals and a typical growth factor in
extracellular matrix (D about 1 um^2/s, k about 1e-3 /s) are marked.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]

signals = [
    ("acetylcholine (synapse)", 400.0, 1e4, "neuron"),
    ("nitric oxide", 3300.0, 1.0, "drug"),
    ("Dpp (morphogen)", 0.1, 2.5e-4, "highlight"),
    ("growth factor in ECM", 1.0, 1e-3, "enzyme"),
]

fig, ax = bio.canvas(20.0, 7.4)
bio.panel(ax, "A", (0.1, 7.3))
pa = charts.axes_at(ax, (1.5, 1.3, 8.0, 5.2))
x = np.logspace(-2, 3, 500)
pa.axvspan(10, 20, color=P.fill("cytoplasm"), alpha=0.9, lw=0)
pa.text(14, 0.03, "one cell", fontsize=FS, color=P.muted(), ha="center")
for name, D, k, tok in signals[:3]:
    lam = np.sqrt(D / k)
    pa.plot(x, np.exp(-x / lam), color=charts.line(tok), lw=1.9, label=f"{name}: λ ≈ {lam:.2g} µm")
pa.set_xscale("log")
pa.set_xlim(0.01, 1000)
pa.set_ylim(0, 1.5)
pa.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper right")
charts.style_axes(pa, "distance from source x / µm", "c / c₀")
charts.title(pa, "Steady profiles c = c₀ exp(−x/λ)")

bio.panel(ax, "B", (10.6, 7.3))
pb = charts.axes_at(ax, (12.1, 1.3, 7.3, 5.2))
lk = np.linspace(-5, 5, 200)
lD = np.linspace(-2, 4, 200)
KK, DD = np.meshgrid(lk, lD)
LAM = 0.5 * (DD - KK)  # log10 lambda in um
cs = pb.contour(KK, DD, LAM, levels=[-1, 0, 1, 2, 3], colors=[P.muted()], linewidths=0.7, linestyles="solid")
pb.clabel(cs, fmt={-1: "0.1 µm", 0: "1 µm", 1: "10 µm", 2: "100 µm", 3: "1 mm"}, fontsize=FS, colors=[P.muted()],
          manual=[(-3.8, 2.2), (-4.4, -0.4), (-0.6, 1.4), (1.5, 1.5), (3.0, 1.0)])
for name, D, k, tok in signals:
    pb.plot(np.log10(k), np.log10(D), "o", ms=6, color=charts.line(tok))
    right = k > 100
    pb.text(np.log10(k) + (-0.25 if right else 0.2), np.log10(D) + 0.18, name, fontsize=FS, color=P.ink(),
            ha="right" if right else "left")
pb.set_xlim(-5, 5)
pb.set_ylim(-2, 4)
pb.set_xticks([-4, -2, 0, 2, 4])
pb.set_xticklabels(["10⁻⁴", "10⁻²", "1", "10²", "10⁴"])
pb.set_yticks([-2, 0, 2, 4])
pb.set_yticklabels(["10⁻²", "1", "10²", "10⁴"])
charts.style_axes(pb, "removal rate constant k / s⁻¹", "D / (µm² s⁻¹)")
charts.title(pb, "Decay length λ = √(D/k)")
