"""Energy, temperature and productivity as correlates of species richness.

A: the prediction of the metabolic theory of ecology (Allen et al. 2002): ln S = c - E/(k_B T), plotted
against 1/(k_B T) for environmental temperatures from 0 to 30 degrees C; the slope is -E, with E = 0.65 eV
(line) and the range 0.5-0.8 eV (band). The top axis gives the temperature. B: the richness gradient this
implies along latitude for a mean annual temperature profile T(phi) = 27 - 0.0065 phi^2 degrees C (relative
to the equator; line) compared with an observed tenfold or greater decline for many groups (shaded range
schematic). C: a schematic model of the scale dependence of the productivity-diversity relationship
(Chase and Leibold 2002). A regional pool of 80 species; species i can live only where productivity
P exceeds a threshold P_i (uniform on 0-1); within a pond, competitive exclusion allows at most
k(P) = 3 + 25 (1 - P)^2 species, drawn at random from those able to live there; a catchment holds 30 ponds.
Local (alpha) richness is hump-shaped, regional (gamma) richness rises, and beta = gamma/alpha (right
axis) rises with productivity because different ponds end up dominated by different species.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(12)
kB = 8.617e-5

fig, ax = bio.canvas(31.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 7.0, 6.8))
Tc = np.linspace(0, 30, 100)
invkT = 1 / (kB * (Tc + 273.15))
x0 = invkT[0]
for E, ls, lw in ((0.65, "-", 1.8),):
    pa.plot(invkT, -E * (invkT - x0), color=Q.line_color("negative"), lw=lw, ls=ls, label="E = 0.65 eV")
pa.fill_between(invkT, -0.5 * (invkT - x0), -0.8 * (invkT - x0), color=Q.line_color("negative"), alpha=0.15, lw=0, label="E = 0.5–0.8 eV")
pa.invert_xaxis()
pa.set_xlim(invkT[0], invkT[-1])
pa.set_ylim(0, 3.6)
C.style_axes(pa, "1/(k_B T) (eV⁻¹)", "ln S − ln S(0 °C)")
top = pa.twiny()
top.set_xlim(pa.get_xlim())
ticks = [0, 10, 20, 30]
top.set_xticks([1 / (kB * (t + 273.15)) for t in ticks])
top.set_xticklabels([f"{t} °C" for t in ticks])
C.style_axes(top, None, None)
top.spines["top"].set_visible(True)
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.4), "Metabolic theory: Boltzmann factor", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.4, 1.6, 7.0, 6.8))
phi = np.linspace(0, 65, 200)
T = 27 - 0.0065 * phi ** 2
Srel = np.exp(-0.65 * (1 / (kB * (T + 273.15)) - 1 / (kB * (27 + 273.15))))
pb.semilogy(phi, Srel, color=Q.line_color("negative"), lw=1.8, label="MTE prediction from T(φ)")
pb.fill_between(phi, np.exp(-np.log(10) * phi / 65), np.exp(-np.log(50) * phi / 65), color=P.muted(), alpha=0.2, lw=0, label="10- to 50-fold decline by 65° (schematic)")
pb.set_xlim(0, 65)
pb.set_ylim(0.01, 1.2)
C.style_axes(pb, "latitude φ (degrees)", "richness relative to the equator")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.4), "Temperature alone and the latitudinal gradient", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))
pool = rng.random(80)
Ps = np.linspace(0.02, 0.98, 49)
alpha, gamma = [], []
for p in Ps:
    elig = np.flatnonzero(pool < p)
    k = int(round(3 + 25 * (1 - p) ** 2))
    al, un = [], set()
    for _ in range(30):
        take = rng.choice(elig, min(k, len(elig)), replace=False) if len(elig) else []
        al.append(len(take))
        un |= set(np.atleast_1d(take).tolist())
    alpha.append(np.mean(al))
    gamma.append(len(un))
alpha, gamma = np.array(alpha), np.array(gamma)
pc.plot(Ps, alpha, color=Q.line_color("dna"), lw=1.8, label="α: species per pond")
pc.plot(Ps, gamma, color=Q.line_color("plant"), lw=1.8, label="γ: species per catchment")
pc.set_xlim(0, 1)
pc.set_ylim(0, 85)
C.style_axes(pc, "productivity P", "species")
pc2 = pc.twinx()
pc2.plot(Ps, gamma / np.maximum(alpha, 1e-9), color=Q.line_color("enzyme"), lw=1.3, ls=(0, (4, 2)))
pc2.set_ylim(0, 20)
C.style_axes(pc2, None, "β = γ/α")
pc2.spines["right"].set_visible(True)
pc.plot([], [], color=Q.line_color("enzyme"), lw=1.3, ls=(0, (4, 2)), label="β = γ/α (right axis)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.4), "Productivity and the scale of observation", size="small", bold=True, ha="left")
