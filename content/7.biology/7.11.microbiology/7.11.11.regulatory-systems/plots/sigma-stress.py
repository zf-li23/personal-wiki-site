"""Two ways of keeping an alternative sigma factor in check in E. coli.
A: the envelope stress response. The anti-sigma factor RseA spans the cytoplasmic membrane and holds
   sigma-E (RpoE) at the membrane. Unfolded outer-membrane proteins (their C-terminal peptides) activate
   the periplasmic protease DegS, which cuts RseA; RseP then cuts it inside the membrane and the
   cytoplasmic remnant is degraded, releasing sigma-E to transcribe envelope-repair genes (and rpoH).
B: the heat shock response as a titration feedback (model, arbitrary units). Free DnaK (Hsp70) promotes
   the degradation of sigma-32 (RpoH); unfolded proteins sequester DnaK. After a temperature step
   (t = 10) unfolded proteins rise, sigma-32 is stabilized and heat shock proteins are made at a much
   higher rate; as DnaK accumulates it captures the unfolded proteins and again degrades sigma-32, so the
   synthesis rate falls back to a moderately raised level.
   Model: ds/dt = 1 - (0.02 + 5 Df) s, dD/dt = s - 0.05 D, dU/dt = u(t) - D U/(K + U),
   Df = D K/(K + U), K = 0.1, u = 0.2 before and 2 after the step."""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(26.0, 9.6)
bio.panel(ax, "A", (0.2, 9.5))

# membranes
for y0, name in ((7.4, "outer membrane"), (4.0, "cytoplasmic membrane")):
    ax.add_patch(FancyBboxPatch((0.6, y0), 12.6, 0.7, boxstyle="round,pad=0,rounding_size=0.2",
                                facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_head"), lw=1.2, zorder=2))
    bio.label(ax, (13.4, y0 + 0.35), name.replace(" ", "\n"), size="tiny", color=P.muted(), ha="left")
bio.label(ax, (0.8, 6.0), "periplasm", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (0.8, 1.0), "cytoplasm", size="tiny", color=P.muted(), ha="left")

# left: unstressed
x1 = 3.5
ax.add_patch(FancyBboxPatch((x1 - 0.25, 3.0), 0.5, 3.0, boxstyle="round,pad=0,rounding_size=0.2",
                            facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.1, zorder=6))
bio.label(ax, (x1 + 0.8, 5.4), "RseA", size="tiny")
ax.add_patch(Ellipse((x1, 2.4), 1.6, 0.9, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.1, zorder=7))
bio.label(ax, (x1, 2.4), "σᴱ", size="small", color=P.on_fill(), zorder=8)
bio.label(ax, (x1, 8.9), "no stress:\nσᴱ held at the membrane", size="tiny", color=P.muted())

# right: stressed
x2 = 9.5
for xy in [(8.2, 6.9), (8.8, 6.6), (7.7, 6.4)]:
    ax.add_patch(Circle(xy, 0.2, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=6))
bio.label(ax, (7.2, 6.95), "unfolded\nOMPs", size="tiny", ha="right")
ax.add_patch(Ellipse((x2, 5.5), 1.4, 0.8, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=1.1, zorder=6))
bio.label(ax, (x2, 5.5), "DegS", size="tiny", color=P.on_fill(), zorder=7)
bio.arrow(ax, (8.6, 6.4), (9.1, 5.9), kind="activation", lw=1.0, head=0.18)
ax.add_patch(FancyBboxPatch((x2 + 1.0, 4.0), 0.5, 1.4, boxstyle="round,pad=0,rounding_size=0.2",
                            facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.1, zorder=6, alpha=0.6))
ax.add_patch(Ellipse((x2 + 2.2, 4.35), 1.2, 0.7, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=1.1, zorder=6))
bio.label(ax, (x2 + 2.2, 4.35), "RseP", size="tiny", color=P.on_fill(), zorder=7)
bio.arrow(ax, (x2 + 0.3, 5.2), (x2 + 0.95, 4.9), kind="process", lw=1.0, head=0.16)
bio.label(ax, (x2 + 0.6, 6.2), "cut 1", size="tiny", color=P.muted())
bio.label(ax, (x2 + 2.2, 3.55), "cut 2", size="tiny", color=P.muted())
ax.add_patch(Ellipse((x2 - 0.2, 2.2), 1.6, 0.9, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.1, zorder=7))
bio.label(ax, (x2 - 0.2, 2.2), "σᴱ", size="small", color=P.on_fill(), zorder=8)
bio.arrow(ax, (x2 + 0.6, 2.2), (x2 + 2.6, 2.2), kind="activation", lw=1.2, head=0.2)
bio.label(ax, (x2 + 2.8, 2.2), "envelope repair,\nrpoH", size="tiny", ha="left")
bio.label(ax, (x2, 8.9), "envelope stress:\nRseA cleaved, σᴱ free", size="tiny", color=P.muted())

# B: heat-shock model
bio.panel(ax, "B", (16.0, 9.5))
pax = charts.axes_at(ax, (17.4, 1.6, 8.2, 6.6))


def run(u0=0.2, u1=2.0, K=0.1, dt=0.002):
    x = np.array([1.0, 1.0, 0.1])

    def f(x, u):
        s, D, U = x
        Df = D * K / (K + U)
        return np.array([1 - (0.02 + 5 * Df) * s, s - 0.05 * D, u - D * U / (K + U)])

    for _ in range(300000):
        x = x + dt * f(x, u0)
    t = np.arange(0, 80, dt)
    out = np.empty((t.size, 3))
    for k, tk in enumerate(t):
        out[k] = x
        x = x + dt * f(x, u0 if tk < 10 else u1)
    return t, out


t, o = run()
s, D, U = o.T
Df = D * 0.1 / (0.1 + U)
pax.axvspan(10, 80, color=P.mix(P.fill("negative"), P.surface(), 0.85), lw=0)
pax.plot(t, s / s[0], color=charts.line("enzyme"), lw=2.0, label="σ³² and HSP synthesis rate")
pax.plot(t, D / D[0], color=charts.line("protein"), lw=1.6, ls="--", label="total DnaK")
pax.plot(t, Df / Df[0], color=charts.line("dna"), lw=1.4, ls=":", label="free DnaK")
pax.set_xlim(0, 80)
pax.set_ylim(0, 5)
pax.text(11, 4.6, "temperature raised", fontsize=7, color=P.edge("negative"))
pax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(pax, "time (a.u.)", "relative to before the step")
charts.title(pax, "Heat shock: a titration feedback (model)")
