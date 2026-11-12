# Active space of a pheromone (Bossert-Wilson model; illustrative parameters).
# A: instantaneous point release of M molecules in still air, C = M/(4 pi D t)^(3/2) exp(-r^2/(4 D t));
#    the active space C >= K has radius r_K(t)^2 = 4 D t ln(M / (K (4 pi D t)^(3/2))), D = 0.07 cm^2/s.
# B: continuous source of strength Q in a wind u = 100 cm/s, time-averaged Gaussian plume with
#    sigma_y = sigma_z = 0.1 x (ground-level source, image doubles the concentration):
#    C(x, y) = Q / (pi u sy sz) exp(-y^2 / (2 sy^2)); contour C = K for three values of Q/K.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
D = 0.07
fig, ax = bio.canvas(24, 10.5)
pA = quant.Plot(ax, (1.8, 1.7, 9.0, 7.0), xlim=(0, 2500), ylim=(0, 20), xlabel="Time after release t / s",
                ylabel="Radius of active space / cm", xticks=[0, 500, 1000, 1500, 2000, 2500], yticks=[0, 5, 10, 15, 20])
for MK, tok in ((1e3, "channel"), (1e4, "enzyme"), (1e5, "negative")):
    tf = MK ** (2 / 3) / (4 * np.pi * D)
    t = np.linspace(1e-3, tf, 800)
    arg = MK / (4 * np.pi * D * t) ** 1.5
    r = np.sqrt(np.clip(4 * D * t * np.log(np.clip(arg, 1, None)), 0, None))
    rmax = np.sqrt(3 / (2 * np.pi * np.e)) * MK ** (1 / 3)
    lab = "M/K = 10^%d cm^3" % int(round(np.log10(MK)))
    if True:
        lab += ", fades at %.0f s" % tf
    pA.line(t, r, tok)
    pA.text(tf * 0.55 if MK > 1e3 else tf + 30, rmax + 0.6 if MK > 1e3 else rmax - 1.0, lab, color=quant.line_color(tok), ha="left")
    pA.hline(rmax, token=tok, dashed=True, lw=0.6)
bio.label(ax, (6.3, 9.6), "A  Instantaneous release, still air", size="small", bold=True)

pB = quant.Plot(ax, (13.6, 1.7, 9.4, 7.0), xlim=(0, 200), ylim=(-20, 20), xlabel="Distance downwind x / m",
                ylabel="Crosswind distance y / m", xticks=[0, 50, 100, 150, 200], yticks=[-20, -10, 0, 10, 20])
u = 100.0
for QK, tok in ((1e7, "channel"), (1e8, "enzyme"), (1e9, "negative")):
    x = np.linspace(1, 4.5e4, 4000)  # cm
    s = 0.1 * x
    c0 = QK / (np.pi * u * s * s)
    ok = c0 > 1
    yk = np.sqrt(2 * s[ok] ** 2 * np.log(c0[ok]))
    xs = np.concatenate([x[ok], x[ok][::-1]]) / 100
    ys = np.concatenate([yk, -yk[::-1]]) / 100
    pB.line(xs, ys, tok, lw=1.3)
    L = x[ok].max() / 100
    pB.text(L + 3, {1e7: 2.8, 1e8: -1.5, 1e9: 0}[QK], "Q/K = 10^%d cm^3/s" % int(round(np.log10(QK))), color=quant.line_color(tok), ha="left")
pB.points([0], [0], "ink", r=0.12)
bio.arrow(ax, (19.0, 2.4), (21.0, 2.4), kind="process")
bio.label(ax, (21.2, 2.4), "wind 1 m/s", size="tiny", ha="left", color=P.muted())
bio.label(ax, (18.3, 9.6), "B  Continuous source in wind (time-averaged plume)", size="small", bold=True)
