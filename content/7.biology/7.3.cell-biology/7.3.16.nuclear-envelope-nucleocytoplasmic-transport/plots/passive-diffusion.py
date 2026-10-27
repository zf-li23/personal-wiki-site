"""Passive permeability of the nuclear pore: rigid aqueous channel versus FG mesh (Proposition 16.4.1).
Protein radius a = 0.066 M^(1/3) nm (M in Da); D proportional to 1/a (Stokes-Einstein).
Rigid pore of radius R = 4.5 nm (Renkin): P ~ D (1 - l)^2 (1 - 2.104 l + 2.09 l^3 - 0.95 l^5), l = a/R.
FG mesh (Ogston): P ~ D exp(-phi (1 + a/r_f)^2), phi = 0.1, r_f = 0.5 nm.
(A) Permeability per pore relative to a 1-kDa molecule. (B) Nuclear/cytoplasmic ratio after cytoplasmic injection,
c_n/c_c = 1 - exp(-t/tau), tau from the mesh model calibrated to tau = 2 min for a 27-kDa protein; dashed: a
110-kDa cargo bound to a 97-kDa receptor (complex 207 kDa) whose FG binding raises the partition coefficient 1000-fold."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def radius(M):
    return 0.066 * np.asarray(M, float) ** (1 / 3)


def renkin(M, R=4.5):
    lam = radius(M) / R
    f = np.where(lam < 1, (1 - lam) ** 2 * (1 - 2.104 * lam + 2.09 * lam**3 - 0.95 * lam**5), 0.0)
    return np.clip(f, 0, None) / radius(M)


def ogston(M, phi=0.1, rf=0.5, boost=1.0):
    return boost * np.exp(-phi * (1 + radius(M) / rf) ** 2) / radius(M)


M = np.logspace(3, np.log10(4e5), 400)
fig, ax = bio.canvas(19.0, 7.4)
bio.panel(ax, "A", (0.1, 7.3))
a = charts.axes_at(ax, (1.9, 1.3, 6.6, 5.6))
a.plot(M / 1e3, renkin(M) / renkin(1e3), color=charts.line("channel"), lw=1.8, label="rigid channel, 9 nm diameter")
a.plot(M / 1e3, ogston(M) / ogston(1e3), color=charts.line("positive"), lw=1.8, label="FG mesh (Ogston)")
a.axvline(60, color=P.muted(), ls=":", lw=0.9)
a.text(62, 3e-6, "60 kDa", fontsize=FT["tiny"], color=P.muted(), ha="left")
a.set_xscale("log")
a.set_yscale("log")
a.set_ylim(1e-6, 2)
a.set_xlim(1, 400)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "molecular mass / kDa", "relative permeability per pore")

bio.panel(ax, "B", (9.9, 7.3))
b = charts.axes_at(ax, (11.6, 1.3, 6.9, 5.6))
tau_gfp = 2.0
k_gfp = ogston(27e3)
t = np.linspace(0, 90, 500)
for m, tok in ((10, "channel"), (27, "positive"), (60, "antibody"), (110, "negative")):
    tau = tau_gfp * k_gfp / ogston(m * 1e3)
    b.plot(t, 1 - np.exp(-t / tau), color=charts.line(tok), lw=1.8, label=f"{m} kDa (τ = {tau:.1f} min)" if tau < 10
           else f"{m} kDa (τ = {tau:.0f} min)")
tau_c = tau_gfp * k_gfp / ogston(207e3, boost=1000)
b.plot(t, 1 - np.exp(-t / tau_c), color=charts.line("negative"), lw=1.6, ls="--", label=f"110 kDa + receptor (τ = {tau_c:.1f} min)")
b.set_xlim(0, 90)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "time after injection / min", "nuclear / cytoplasmic concentration")
