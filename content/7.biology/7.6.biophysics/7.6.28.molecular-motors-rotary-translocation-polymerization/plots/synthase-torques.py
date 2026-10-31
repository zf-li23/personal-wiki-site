# The two motors of ATP synthase push against each other. A: schematic of FoF1 (mitochondrial orientation,
# matrix below): protons flowing through Fo turn the c ring and the central stalk one way, ATP hydrolysis in F1
# turns them the other. B: torque of Fo, tau_o = n_c e dp / (2 pi) (Formula 28.3.1), against the proton-motive
# force for c rings of 8 (animal mitochondria), 10 (yeast, E. coli) and 14 subunits (chloroplasts), and the
# torque of F1, tau_1 = dG_p / (2 pi / 3), for a phosphorylation potential of 45-60 kJ/mol (band). Fo wins and
# ATP is made where its line lies above the band; the crossing gives the minimum proton-motive force.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(11.5, 4.4))
ax = fig.add_axes([0.0, 0.0, 0.40, 1.0])
ax.set_xlim(0, 9); ax.set_ylim(0, 9.6); ax.set_aspect("equal"); ax.axis("off")
be.inner_membrane(ax, (0.3, 8.7), y=6.2, ims=2.4, matrix=4.8, n_side="bottom", names=True)
s = be.atp_synthase(ax, 4.0, 6.2, text=None, c_ring=10, n_side="bottom")
be.proton_arrow(ax, (s["channel"][0] + 0.3, 7.9), (s["channel"][0] + 0.3, 4.9), text="$n_c$ H⁺ per turn", side="right")
bio.panel(ax, "A", (0.1, 9.45))
# torque arcs
for (cx, cy), sgn, txt, tok in (((4.0, 6.75), 1, "$\\tau_\\mathrm{o}$ (protons)", "h"), ((4.0, 3.65), -1, "$\\tau_1$ (ATP hydrolysis)", "atp")):
    th = np.linspace(-0.9, 0.9, 40) + (np.pi / 2 if sgn > 0 else -np.pi / 2)
    rx, ry = 1.35, 0.45
    xs, ys = cx + rx * np.cos(th), cy + ry * np.sin(th) * (1 if sgn > 0 else 1)
    col = charts.line(tok)
    ax.plot(xs, ys, color=col, lw=1.8, zorder=30)
    ax.annotate("", xy=(xs[0], ys[0]), xytext=(xs[3], ys[3]),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.5), zorder=30)
    bio.label(ax, (cx - 1.5, cy + (0.55 if sgn > 0 else -0.45)), txt, size="small", color=col, ha="right", zorder=31)
bio.label(ax, (4.5, 0.75), "synthesis: $\\tau_\\mathrm{o} > \\tau_1$;  hydrolysis and pumping: $\\tau_1 > \\tau_\\mathrm{o}$", size="small")

ax = fig.add_axes([0.50, 0.15, 0.47, 0.75])
e = 1.602176634e-19
dp = np.linspace(0, 260, 300)  # mV
for nc, tok, lab in ((8, "mitochondrion", "c$_8$ (animal mitochondria)"), (10, "dna", "c$_{10}$ (yeast, E. coli)"),
                     (14, "chloroplast", "c$_{14}$ (chloroplast)")):
    tau = nc * e * dp * 1e-3 / (2 * np.pi) * 1e21  # pN nm
    ax.plot(dp, tau, color=charts.line(tok), lw=1.8, label=lab)
NA = 6.02214076e23
t1 = lambda G: G * 1e3 / NA / (2 * np.pi / 3) * 1e21
ax.axhspan(t1(45), t1(60), color=P.fill("atp"), alpha=0.35, lw=0)
ax.text(5, t1(52.5), "F$_1$ torque for $\\Delta G_\\mathrm{p}$ = 45–60 kJ/mol", fontsize=7.5, color=P.ink(), va="center")
ax.axvspan(170, 220, color=P.fill("neutral"), alpha=0.3, lw=0)
ax.text(195, 8, "mitochondria\n(170–220 mV)", fontsize=7.5, color=P.ink(), ha="center")
ax.set_xlim(0, 260); ax.set_ylim(0, 100)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "proton-motive force $\\Delta p$ / mV", "torque / pN nm")
charts.title(ax, "B   Torque balance decides the direction")
