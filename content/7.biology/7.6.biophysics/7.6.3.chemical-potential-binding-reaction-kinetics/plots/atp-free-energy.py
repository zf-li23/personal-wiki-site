# The free energy of ATP hydrolysis, ATP + H2O -> ADP + Pi, depends on the mass-action ratio
# Q = [ADP][Pi]/[ATP] (concentrations in M, relative to 1 M): dG = dG0' + RT ln Q at 310 K, with the biochemical
# standard value dG0' = -30.5 kJ/mol (pH 7, about -12 kBT). Points: the standard state (Q = 1), the
# equilibrium (dG = 0, Q = 1.4e5), an E. coli cell (ATP 5 mM, ADP 0.5 mM, Pi 10 mM, Q = 1e-3: about -19 kBT)
# and resting human skeletal muscle (ATP 8 mM, free ADP 0.02 mM, Pi 3 mM, Q = 7.5e-6: about -24 kBT).
# Right axis: the same energies in kJ/mol.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
RT = 8.314462618 * 310 / 1000
G0 = -30.5
fig, ax = plt.subplots(figsize=(7.4, 3.9))
lq = np.linspace(-7, 7, 300)
dg = (G0 + RT * np.log(10.0 ** lq)) / RT
ax.plot(lq, dg, color=charts.line("atp"), lw=2.0)
ax.axhline(0, color=P.muted(), lw=0.7)
pts = [(0.0, "standard state\n(all 1 M)", "neutral", (0.25, 1.2)),
       (-G0 / RT / np.log(10), "equilibrium", "neutral", (-3.6, 1.6)),
       (np.log10(0.5e-3 * 10e-3 / 5e-3), "E. coli cell", "bacterium", (0.3, -2.6)),
       (np.log10(0.02e-3 * 3e-3 / 8e-3), "resting muscle", "muscle", (0.3, -2.4))]
for x, txt, tok, (dx, dy) in pts:
    y = (G0 + RT * x * np.log(10)) / RT
    ax.plot([x], [y], "o", color=charts.line(tok), ms=6, zorder=5)
    if txt == "E. coli cell":
        txt = "$\\it{E.\\ coli}$ cell"
    lab = "equilibrium, ΔG = 0" if txt == "equilibrium" else f"{txt}\n{y:.0f} kBT".replace("-", "−")
    ax.text(x + dx, y + dy, lab, fontsize=7, color=P.ink())
ax.set_xlim(-7, 7)
ax.set_ylim(-30, 8)
ax.set_xticks(range(-6, 8, 2))
ax.set_xticklabels([f"10{str(v).replace('-', '⁻').translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹'))}" for v in range(-6, 8, 2)])
charts.style_axes(ax, "mass-action ratio Q = [ADP][Pi]/[ATP]  (M)", "ΔG / kBT  (310 K)")
sec = ax.secondary_yaxis("right", functions=(lambda e: e * RT, lambda q: q / RT))
sec.set_ylabel("ΔG / (kJ mol⁻¹)", fontsize=8, color=P.ink())
sec.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=6.8)
sec.spines["right"].set_color(P.muted())
fig.tight_layout()
