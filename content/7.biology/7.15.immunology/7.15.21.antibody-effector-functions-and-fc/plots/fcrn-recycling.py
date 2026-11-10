# FcRn and the serum half-life of IgG: a saturable recycling model (illustrative parameters).
# Endothelial and other cells take up plasma IgG by fluid-phase pinocytosis at rate k_u. In the acidic
# endosome (pH ~6) IgG binds FcRn and is returned to the surface, where it is released at pH 7.4;
# unbound IgG goes on to the lysosome. The rescued fraction falls when FcRn is saturated:
#     f(C) = f_max / (1 + C / K),   elimination rate  k(C) = k_u (1 - f(C)),   t_1/2 = ln 2 / k(C).
# Calibration: t_1/2 = 2.5 d without rescue and 21 d at C = 10 g/L (typical adult IgG).
# Panel B: FcRn blockade lowers f_max (0.95 to 0.6). Panel C: maternal IgG transferred across the placenta decays after
# birth while the infant's own synthesis rises, giving the physiological trough at about 3 months.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
LN2 = np.log(2)
ku = LN2 / 2.5
fmax = 0.95
K = 10 / ((fmax / (1 - 2.5 / 21)) - 1)  # so that t1/2(10 g/L) = 21 d


def k_el(C, fm=fmax):
    return ku * (1 - fm / (1 + C / K))


fig, ax = bio.canvas(27, 9.6)

# ---- A: half-life vs serum IgG ---------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.4))
C = np.linspace(0.5, 45, 300)
pa = quant.Plot(ax, (1.9, 1.6, 6.3, 6.6), (0, 45), (0, 40), xlabel="Serum IgG / (g L⁻¹)", ylabel="IgG half-life / d",
                xticks=[0, 10, 20, 30, 40], yticks=[0, 10, 20, 30, 40], grid=True)
pa.line(C, LN2 / k_el(C), "dna", lw=1.8)
pa.hline(2.5, "negative", text="no FcRn rescue", side="right")
for c0, txt in ((3, "hypogamma-\nglobulinemia"), (10, "normal adult"), (35, "after high-dose IgG")):
    t0 = LN2 / k_el(c0)
    pa.points([c0], [t0], "dna", r=0.1)
    pa.text(c0 + 1.2, t0 + 1.5, f"{txt}: {t0:.0f} d", ha="left", va="bottom")

# ---- B: FcRn blockade -------------------------------------------------------------------------------------
bio.panel(ax, "B", (9.5, 9.4))
prod = k_el(10) * 10  # steady-state production at 10 g/L
t = np.arange(0, 120.0, 0.1)
Cb = np.empty_like(t)
Cb[0] = 10
for i in range(1, t.size):
    fm = 0.6 if 14 <= t[i] < 56 else fmax
    Cb[i] = Cb[i - 1] + 0.1 * (prod - k_el(Cb[i - 1], fm) * Cb[i - 1])
pb = quant.Plot(ax, (11.3, 1.6, 6.3, 6.6), (0, 120), (0, 12), xlabel="Time / d", ylabel="Serum IgG / (g L⁻¹)",
                xticks=[0, 30, 60, 90, 120], yticks=[0, 4, 8, 12], grid=True)
pb.span(14, 56, "highlight", text="FcRn blocked (f_max 0.95 → 0.6)", text_y=pb.Y(11.3))
pb.line(t, Cb, "dna", lw=1.8)
low = Cb[(t > 14) & (t < 56)].min()
pb.text(57, low - 0.3, f"−{100 * (1 - low / 10):.0f} %", ha="left", va="top")
bio.label(ax, (14.45, 0.25), "production unchanged; only the rescue fraction falls", size="tiny", color=P.muted())

# ---- C: infant IgG ----------------------------------------------------------------------------------------------
bio.panel(ax, "C", (18.8, 9.4))
td = np.arange(0, 731)
k_inf = LN2 / 21
km = LN2 / 28           # maternal IgG half-life in the infant ~4 weeks
Pa = k_inf * 11
own = np.zeros(td.size)
for i in range(1, td.size):
    own[i] = own[i - 1] + Pa * td[i] / (td[i] + 200) - k_inf * own[i - 1]
mat = 10 * np.exp(-km * td)
tot = own + mat
pc = quant.Plot(ax, (20.6, 1.6, 6.0, 6.6), (0, 24), (0, 12), xlabel="Age / months", ylabel="Serum IgG / (g L⁻¹)",
                xticks=[0, 6, 12, 18, 24], yticks=[0, 4, 8, 12], grid=True)
m = td / 30.4
pc.line(m, mat, "rna", lw=1.5, dashed=True, text="maternal (via FcRn)", at=0.1, dx=0.3, dy=0.2, ha="left", va="bottom")
pc.line(m, own, "positive", lw=1.5, dashed=True, text="infant's own", at=0.8, dy=-0.25, va="top")
pc.line(m, tot, "dna", lw=1.9, text="total", at=0.92, dy=0.25, va="bottom")
i0 = int(np.argmin(tot))
pc.points([m[i0]], [tot[i0]], "dna", r=0.1)
pc.text(m[i0] + 0.6, tot[i0] - 0.4, f"trough ~{m[i0]:.0f} months", ha="left", va="top")
