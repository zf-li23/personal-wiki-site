"""The models of the course placed by the spatial and temporal scale of the process they describe.

Each marker is one model, at the order of magnitude of the length (size of the patterned field,
tissue or organism) and time (duration, period or relaxation time) of the developmental process
it treats; the number is the chapter (7.5.n). Marker colour gives the class of model. Grey
lines: the diffusion time t = L^2 / D for D = 1 and 10 um^2/s (paracrine signals, 7.5.11), and
the distance L = U t covered by tissue flow at U = 10 nm/s, about a millimetre a day (7.5.8).
Values are orders of magnitude only. Catastrophe theory (7.5.10) has no scale and is not shown.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
MIN, H, D, Y = 60.0, 3600.0, 86400.0, 3.15e7

classes = {
    "mech": ("bone", "mechanics and energy"),
    "rd": ("dna", "diffusion, gradients, reaction-diffusion, chemotaxis"),
    "osc": ("enzyme", "oscillators and switches"),
    "sto": ("protein", "stochastic and statistical models"),
    "pop": ("positive", "growth, populations, life span"),
}

models = [  # (length / m, time / s, label, class)
    (1e-4, 5 * H, "blastocoel (5)", "mech"),
    (3e-4, 1 * D, "cell sorting (7)", "mech"),
    (2e-4, 10 * MIN, "tissue rheology (8)", "mech"),
    (1e-5, 5 * MIN, "vertex model (8)", "mech"),
    (1.2e-3, 4 * H, "frog gastrulation (9)", "mech"),
    (6e-4, 8 * H, "epiboly (9)", "mech"),
    (1.5e-3, 10 * H, "neural plate (18)", "mech"),
    (2e-4, 2 * D, "appendage spacing (22)", "mech"),
    (1.2e-3, 1.5 * D, "heart looping (28)", "mech"),
    (3e-3, 10 * D, "vessel network (29)", "mech"),
    (1e-3, 4 * D, "gut villi (30)", "mech"),
    (3e-4, 12 * H, "disc eversion (33)", "mech"),
    (1e-4, 30, "Ca2+ wave (4)", "rd"),
    (5e-5, 10 * MIN, "PAR polarity (6)", "rd"),
    (5e-4, 1.5 * H, "Bicoid gradient (11, 14)", "rd"),
    (2e-4, 1 * H, "Dpp shuttle (14)", "rd"),
    (6e-5, 2 * H, "Nodal-Lefty (16)", "rd"),
    (1e-3, 3 * H, "BMP scaling (16)", "rd"),
    (5e-5, 20 * MIN, "nodal flow (17)", "rd"),
    (2e-4, 2 * D, "Shh in neural tube (18)", "rd"),
    (5e-3, 8 * H, "Dictyostelium (13)", "rd"),
    (1e-3, 1.5 * D, "digits (32)", "rd"),
    (5e-3, 4 * D, "Hydra head (35)", "rd"),
    (3e-4, 3 * D, "compartments (33)", "rd"),
    (2e-3, 3 * D, "axon guidance (21)", "rd"),
    (3e-2, 3 * 7 * D, "enteric crest wave (20)", "rd"),
    (1e-3, 2 * H, "segmentation clock (23)", "osc"),
    (1e-2, 10 * H, "mitotic oscillator (34)", "osc"),
    (1e-4, 1 * D, "ICM switch (5)", "osc"),
    (1e-3, 6 * H, "sex switch (26)", "osc"),
    (2e-5, 2 * D, "blood lineage switch (29)", "osc"),
    (3e-5, 3 * H, "lateral inhibition (19, 29)", "osc"),
    (1e-3, 0.5, "pacemaker (28)", "osc"),
    (1e-4, 10, "polyspermy (4)", "sto"),
    (1e-4, 30 * D, "clonal drift (36)", "sto"),
    (1e-2, 40 * D, "branching (25, 30)", "sto"),
    (6e-4, 3 * D, "mitotic field (31)", "sto"),
    (1e-4, 3 * D, "XCI skew (38)", "sto"),
    (3e-3, 0.4 * Y, "genetic assimilation (39)", "sto"),
    (1e-5, 1 * D, "cell cycles (34)", "pop"),
    (1e-2, 100 * D, "cortical neurogenesis (19)", "pop"),
    (3e-3, 3 * Y, "growth plate (24)", "pop"),
    (1.7, 18 * Y, "human growth (34)", "pop"),
    (3e-2, 50 * Y, "ovarian reserve (27)", "pop"),
    (1.7, 80 * Y, "Gompertz mortality (37)", "pop"),
    (0.1, 7 * D, "liver regrowth (35)", "pop"),
    (1e-2, 5 * D, "final size (33)", "pop"),
    (1e-4, 120 * D, "bone remodelling (24)", "pop"),
    (5e-3, 30 * D, "critical periods (38)", "pop"),
]

fig, ax = plt.subplots(figsize=(13.0, 8.2))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.97)
ax.set_xscale("log")
ax.set_yscale("log")
xl, yl = (5e-6, 5.0), (0.1, 1e10)
ax.set_xlim(*xl)
ax.set_ylim(*yl)

L = np.logspace(-6, 1, 50)
for Dm in (1e-12, 1e-11):
    ax.plot(L, L**2 / Dm, color=P.muted(), lw=0.8, ls=(0, (4, 3)), zorder=1)
ax.text(6e-6, 6e-6**2 / 1e-12 * 1.3, r"$t = L^2/D$, $D = 1\,\mu\mathrm{m^2\,s^{-1}}$", rotation=36,
        fontsize=FT["tiny"], color=P.muted(), ha="left", va="bottom", rotation_mode="anchor")
ax.text(2.5e-2, 2.5e-2**2 / 1e-11 * 1.3, r"$D = 10\,\mu\mathrm{m^2\,s^{-1}}$", rotation=36,
        fontsize=FT["tiny"], color=P.muted(), ha="left", va="bottom", rotation_mode="anchor")
ax.plot(L, L / 1e-8, color=P.muted(), lw=0.8, ls=":", zorder=1)
ax.text(0.25, 0.25 / 1e-8 * 1.5, r"tissue flow, $10\,\mathrm{nm\,s^{-1}}$", rotation=16, rotation_mode="anchor", fontsize=FT["tiny"], color=P.muted(), ha="left", va="bottom")

for Lm, t, txt, cl in models:
    tok = classes[cl][0]
    ax.plot([Lm], [t], "o", ms=6.5, color=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)

# greedy label placement: try offsets around each marker, keep the first that overlaps nothing
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
placed = []
pts = [ax.transData.transform((m[0], m[1])) for m in models]
offsets = [(dx * f, dy * f, ha, va) for f in (1, 2.2) for dx, dy, ha, va in [(6, 3, "left", "bottom"), (6, -3, "left", "top"), (-6, 3, "right", "bottom"), (-6, -3, "right", "top"),
           (0, 7, "center", "bottom"), (0, -7, "center", "top"), (10, 10, "left", "bottom"), (10, -10, "left", "top"),
           (-10, 10, "right", "bottom"), (-10, -10, "right", "top"), (0, 15, "center", "bottom"), (0, -15, "center", "top")]]


def clash(bb):
    if any(bb.overlaps(o) for o in placed):
        return True
    for p in pts:
        if bb.x0 - 6 < p[0] < bb.x1 + 6 and bb.y0 - 6 < p[1] < bb.y1 + 6:
            return True
    axbb = ax.get_window_extent()
    return bb.x0 < axbb.x0 or bb.x1 > axbb.x1 or bb.y0 < axbb.y0 or bb.y1 > axbb.y1


for (Lm, t, txt, cl), p in zip(models, pts):
    for dx, dy, ha, va in offsets:
        tx = ax.annotate(txt, (Lm, t), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                         fontsize=FT["tiny"], color=P.ink(), zorder=6)
        bb = tx.get_window_extent(renderer)
        if not clash(bb) or (dx, dy) == offsets[-1][:2]:
            placed.append(bb)
            break
        tx.remove()

xt = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]
ax.set_xticks(xt)
ax.set_xticklabels(["10 µm", "100 µm", "1 mm", "1 cm", "10 cm", "1 m"])
yt = [1, MIN, H, D, 30 * D, Y, 10 * Y, 100 * Y]
ax.set_yticks(yt)
ax.set_yticklabels(["1 s", "1 min", "1 h", "1 day", "1 month", "1 year", "10 years", "100 years"])
ax.minorticks_off()
charts.style_axes(ax, "length scale of the process", "time scale of the process")

for k, (key, (tok, name)) in enumerate(classes.items()):
    xx = (0.01, 0.15, 0.45, 0.64, 0.84)[k]
    fig.text(xx + 0.012, 0.035, name, fontsize=FT["tiny"], color=P.ink(), ha="left", va="center")
    fig.add_artist(plt.Line2D([xx + 0.004], [0.035], marker="o", ms=6.5, color=P.fill(tok), mec=P.edge(tok),
                              mew=0.9, transform=fig.transFigure))
