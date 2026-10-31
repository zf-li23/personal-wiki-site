"""Shape, friction and viscosity (Formulas 8.7.1, 8.10.2 and 8.8.1).

A: Perrin factor f_e/f_0 of prolate and oblate ellipsoids of revolution against the axial ratio
(exact closed forms), relative to a sphere of the same volume. B: Simha factor nu of the intrinsic
viscosity for the same ellipsoids, from the large-axial-ratio expansions (prolate:
nu = p^2/(15(ln 2p - 3/2)) + p^2/(5(ln 2p - 1/2)) + 14/15; oblate: nu = 16 q/(15 arctan q),
q = 1/p), plotted for axial ratios of 5 and more; nu = 2.5 for a sphere. C: sedimentation
coefficients (s_20,w) of proteins and a virus against molar mass, with the lines for spheres of
anhydrous protein volume (vbar = 0.73 mL/g) and frictional ratios 1, 1.25, 1.5, 2 and 3; the frictional
ratio of each point is computed from its s and M with the Svedberg relation f = M(1 - vbar rho)/(N_A s).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
NA, eta, rho = 6.02214e23, 1.002e-3, 998.2


def perrin(p):
    p = np.asarray(p, float)
    out = np.ones_like(p)
    pro = p > 1
    ob = p < 1
    q = p[pro]
    out[pro] = np.sqrt(q ** 2 - 1) / (q ** (1 / 3) * np.log(q + np.sqrt(q ** 2 - 1)))
    q = p[ob]
    out[ob] = np.sqrt(1 - q ** 2) / (q ** (1 / 3) * np.arctan(np.sqrt(1 - q ** 2) / q))
    return out


fig, ax = bio.canvas(25.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.4, 1.3, 6.0, 6.0))
pp = np.logspace(0, 2, 300)
pa.semilogx(pp, perrin(pp), color=charts.line("enzyme"), lw=1.7, label="prolate (cigar), p = a/b")
pa.semilogx(pp, perrin(1 / pp), color=charts.line("receptor"), lw=1.7, label="oblate (disk), p = b/a")
pa.axhspan(1.1, 1.3, color=P.mix(P.fill("protein"), P.surface(), 0.6), lw=0)
pa.text(1.1, 1.14, "typical globular proteins (with hydration)", fontsize=FT["tiny"], color=P.ink())
for p in (10, 20, 50):
    pa.plot(p, perrin(np.array([p]))[0], "o", ms=3, color=charts.line("enzyme"))
    pa.text(p, perrin(np.array([p]))[0] + 0.06, f"{perrin(np.array([p]))[0]:.2f}", fontsize=FT["tiny"], color=P.ink(), ha="center")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pa.set_ylim(0.95, 3.0)
charts.style_axes(pa, "axial ratio", r"Perrin factor $f_\mathrm{e}/f_0$", box=True)
charts.title(pa, "Friction of ellipsoids")

bio.panel(ax, "B", (8.2, 8.3))
pb = charts.axes_at(ax, (9.5, 1.3, 6.0, 6.0))
p5 = np.logspace(np.log10(5), 2, 200)
nu_pro = p5 ** 2 / (15 * (np.log(2 * p5) - 1.5)) + p5 ** 2 / (5 * (np.log(2 * p5) - 0.5)) + 14 / 15
nu_ob = 16 * p5 / (15 * np.arctan(p5))
pb.loglog(p5, nu_pro, color=charts.line("enzyme"), lw=1.7, label="prolate")
pb.loglog(p5, nu_ob, color=charts.line("receptor"), lw=1.7, label="oblate")
pb.plot([1], [2.5], "o", ms=5, color=P.ink())
pb.text(1.12, 2.0, "sphere: 2.5 (Einstein)", fontsize=FT["tiny"], color=P.ink())
pb.plot([1, 5], [2.5, nu_pro[0]], color=charts.line("enzyme"), lw=0.8, ls=":")
pb.plot([1, 5], [2.5, nu_ob[0]], color=charts.line("receptor"), lw=0.8, ls=":")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "axial ratio", r"Simha factor $\nu$", box=True)
charts.title(pb, "Viscosity is far more shape-sensitive")

# C: s against M
DATA = [  # name, M (kDa), s20,w (S), vbar (mL/g)
    ("lysozyme", 14.3, 1.91, 0.703), ("myoglobin", 17.8, 2.04, 0.741), ("chymotrypsinogen", 25.7, 2.54, 0.721),
    ("ovalbumin", 44.0, 3.55, 0.748), ("hemoglobin", 64.5, 4.46, 0.749), ("serum albumin", 66.5, 4.3, 0.734),
    ("catalase", 250.0, 11.3, 0.73), ("urease", 480.0, 18.6, 0.73), ("fibrinogen", 340.0, 7.9, 0.72),
    ("myosin", 470.0, 6.4, 0.728), ("TMV", 40000.0, 198.0, 0.73),
]
bio.panel(ax, "C", (16.3, 8.3))
pc = charts.axes_at(ax, (17.7, 1.3, 6.8, 6.0))


def s_sphere(Mk, vbar=0.73, ratio=1.0):
    M = Mk  # kg/mol
    V = M * vbar * 1e-3 / NA
    R0 = (3 * V / (4 * np.pi)) ** (1 / 3)
    f = ratio * 6 * np.pi * eta * R0
    return M * (1 - vbar * 1e-3 * rho) / (NA * f) * 1e13


MM = np.logspace(1, 5, 50)
for ratio in (1.0, 1.25, 1.5, 2.0, 3.0):
    pc.loglog(MM, s_sphere(MM, ratio=ratio), color=P.muted(), lw=0.8 if ratio != 1.0 else 1.4,
              ls="-" if ratio == 1.0 else "--")
    pc.text(1.2e5, s_sphere(1.2e5, ratio=ratio), f"{ratio:g}", fontsize=FT["tiny"], color=P.muted(), va="center")
pc.text(1.2e5, s_sphere(1.2e5, ratio=3.0) / 1.8, "f/f$_0$", fontsize=FT["tiny"], color=P.muted())
for name, Mk, s, vb in DATA:
    ratio = s_sphere(Mk, vb) / s
    tok = "enzyme" if ratio > 1.6 else "protein"
    pc.plot(Mk, s, "o", ms=5, mfc=P.fill(tok), mec=P.edge(tok))
    ha, dx = ("right", 0.85) if name in ("serum albumin", "fibrinogen", "myoglobin", "TMV") else ("left", 1.15)
    pc.text(Mk * dx, s, f"{name} ({ratio:.2f})", fontsize=FT["tiny"], color=P.ink(), va="center", ha=ha)
pc.set_xlim(8, 3e5)
pc.set_ylim(1, 1500)
charts.style_axes(pc, "molar mass M / kDa", r"$s_{20,\mathrm{w}}$ / S", box=True)
charts.title(pc, r"$s \propto M^{2/3}$ for compact particles")
