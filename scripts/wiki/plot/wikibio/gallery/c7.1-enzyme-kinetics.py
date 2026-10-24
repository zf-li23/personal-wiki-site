# Michaelis-Menten kinetics. A: the saturation curve v = Vmax [S] / (Km + [S]) with Vmax = 10 uM/s and
# Km = 2 mM, simulated measurements (3 % noise) and the Lineweaver-Burk double-reciprocal plot as an inset
# (intercepts 1/Vmax and -1/Km). B-D: the three reversible inhibition types in Lineweaver-Burk form at
# [I] = 0, 1, 2 mM with Ki = Ki' = 1 mM: competitive lines meet on the y axis (Vmax unchanged, Km raised),
# uncompetitive lines are parallel (both lowered by the same factor), noncompetitive lines meet on the x axis
# (Vmax lowered, Km unchanged).
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import metabolism as M

VMAX, KM, KI = 10.0, 2.0, 1.0
fig, ax = bio.canvas(20.6, 9.2)

# --- A: saturation curve with inset ---------------------------------------------------------------
a = C.axes_at(ax, (1.35, 1.6, 7.2, 6.2))
S = np.linspace(0, 20, 400)
a.axhline(VMAX, color=bio.P.muted(), lw=0.8, ls=(0, (4, 3)))
a.plot([KM, KM, 0], [0, VMAX / 2, VMAX / 2], color=bio.P.muted(), lw=0.8, ls=(0, (4, 3)))
a.plot(S, M.rate(S, VMAX, KM), color=C.line("enzyme"), lw=2.0)
rng = np.random.default_rng(3)
Sd = np.array([0.25, 0.5, 1, 2, 4, 8, 16])
vd = M.rate(Sd, VMAX, KM) * (1 + 0.03 * rng.standard_normal(len(Sd)))
a.plot(Sd, vd, "o", ms=4.5, mfc=bio.P.fill("enzyme"), mec=C.line("enzyme"), mew=0.9, zorder=5)
a.set_xlim(0, 20)
a.set_ylim(0, 11.5)
a.set_xticks([0, KM, 5, 10, 15, 20], ["0", "$K_\\mathrm{m}$", "5", "10", "15", "20"])
a.set_yticks([0, 2, VMAX / 2, 8, VMAX], ["0", "2", "$V_\\max/2$", "8", "$V_\\max$"])
C.style_axes(a, "[S] / mM", "$v_0$ / (µM s$^{-1}$)")
bio.panel(ax, "A", (0.1, 9.05))
bio.label(ax, (1.35, 8.7), "Michaelis–Menten saturation", size="normal", bold=True, ha="left")

ins = C.axes_at(ax, (5.1, 2.45, 3.1, 2.6))
x = np.linspace(-0.6, 4.2, 50)
ins.axhline(0, color=bio.P.muted(), lw=0.6)
ins.axvline(0, color=bio.P.muted(), lw=0.6)
ins.plot(x, KM / VMAX * x + 1 / VMAX, color=C.line("enzyme"), lw=1.5)
ins.plot(1 / Sd, 1 / vd, "o", ms=3, mfc=bio.P.fill("enzyme"), mec=C.line("enzyme"), mew=0.7, zorder=5)
ins.plot([-1 / KM], [0], "o", ms=3.5, color=bio.P.ink())
ins.plot([0], [1 / VMAX], "o", ms=3.5, color=bio.P.ink())
ins.annotate("$-1/K_\\mathrm{m}$", (-1 / KM, 0), (-0.75, 0.36), fontsize=bio.core.FONT["tiny"], color=bio.P.ink(),
             arrowprops=dict(arrowstyle="-", color=bio.P.muted(), lw=0.6))
ins.annotate("$1/V_\\max$", (0, 1 / VMAX), (0.25, 0.62), fontsize=bio.core.FONT["tiny"], color=bio.P.ink(),
             arrowprops=dict(arrowstyle="-", color=bio.P.muted(), lw=0.6))
ins.text(1.6, 0.12, "slope $K_\\mathrm{m}/V_\\max$", fontsize=bio.core.FONT["tiny"], color=bio.P.ink(), rotation=0)
ins.set_xlim(-0.8, 4.3)
ins.set_ylim(-0.1, 1.05)
ins.set_xticks([0, 2, 4])
ins.set_yticks([0, 0.5, 1])
C.style_axes(ins, "1/[S] / mM$^{-1}$", "1/$v_0$ / (s µM$^{-1}$)", size="tiny", box=True)
ins.set_facecolor(bio.P.surface())
ins.set_title("Lineweaver–Burk", fontsize=bio.core.FONT["tiny"], color=bio.P.ink(), pad=3)

# --- B-D: inhibition types ----------------------------------------------------------------------
types = [
    ("B", "Competitive", dict(ki=KI), "E + I ⇌ EI", "$K_\\mathrm{m}$ ↑, $V_\\max$ same"),
    ("C", "Uncompetitive", dict(kiu=KI), "ES + I ⇌ ESI", "$K_\\mathrm{m}$ ↓, $V_\\max$ ↓"),
    ("D", "Noncompetitive", dict(ki=KI, kiu=KI), "I binds E and ES", "$K_\\mathrm{m}$ same, $V_\\max$ ↓"),
]
levels = [(0.0, C.line("enzyme"), "0"), (1.0, bio.P.fill("drug"), "1"), (2.0, C.line("negative"), "2")]
x = np.linspace(-1.6, 2.2, 60)
for k, (letter, name, kw, how, effect) in enumerate(types):
    x0 = 11.0 + k * 3.4
    p = C.axes_at(ax, (x0, 1.6, 2.5, 5.6))
    p.axhline(0, color=bio.P.muted(), lw=0.6)
    p.axvline(0, color=bio.P.muted(), lw=0.6)
    for i, col, _ in levels:
        vm, km = M.apparent(VMAX, KM, i, **kw)
        p.plot(x, km / vm * x + 1 / vm, color=col, lw=1.6)
    p.set_xlim(-1.6, 2.2)
    p.set_ylim(-0.15, 1.3)
    p.set_xticks([-1, 0, 1, 2])
    p.set_yticks([0, 0.5, 1.0] if k == 0 else [0, 0.5, 1.0])
    if k:
        p.set_yticklabels([])
    C.style_axes(p, "1/[S] / mM$^{-1}$", "1/$v_0$ / (s µM$^{-1}$)" if k == 0 else None)
    bio.panel(ax, letter, (x0 - 0.45, 9.05))
    bio.label(ax, (x0 + 0.05, 8.72), name, size="normal", bold=True, ha="left")
    bio.label(ax, (x0 + 0.05, 8.15), how, size="small", ha="left")
    bio.label(ax, (x0 + 0.05, 7.65), effect, size="small", color=bio.P.muted(), ha="left")

# shared legend for B-D
lx, ly = 11.0, 0.35
bio.label(ax, (lx, ly), "[I] / mM:", size="small", ha="left")
for j, (_, col, text) in enumerate(levels):
    xx = lx + 1.6 + j * 1.25
    ax.plot([xx, xx + 0.5], [ly, ly], color=col, lw=1.8)
    bio.label(ax, (xx + 0.62, ly), text, size="small", ha="left")
bio.label(ax, (lx + 5.6, ly), "$K_\\mathrm{i} = K_\\mathrm{i}' = 1$ mM", size="small", ha="left", color=bio.P.muted())
