"""Kinetics and equilibrium of P + L <=> PL with the ligand in excess (pseudo-first order).

d[PL]/dt = k_on [P][L] - k_off [PL] with [L] constant relaxes exponentially to equilibrium:
theta(t) = theta_eq (1 - exp(-k_obs t)), k_obs = k_on [L] + k_off, theta_eq = [L] / ([L] + K_d).
Illustrative constants: k_on = 1e7 M^-1 s^-1, k_off = 0.1 s^-1, so K_d = 10 nM and the complex
lives 1/k_off = 10 s. A: association time courses at [L] = 0.3, 1, 3 and 10 K_d (each curve reaches
its plateau faster the higher [L]); B: k_obs against [L] is a straight line with slope k_on and
intercept k_off, the standard way to measure both rate constants; C: the equilibrium binding curve on
a logarithmic axis, where occupancy rises from 10 % to 90 % over an 81-fold range of [L]."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
KON, KOFF = 1e7, 0.1  # M^-1 s^-1, s^-1
KD = KOFF / KON  # 10 nM
levels = [(0.3, "channel"), (1.0, "enzyme"), (3.0, "protein"), (10.0, "negative")]

fig, ax = bio.canvas(24.0, 8.4)
tiny = bio.core.FONT["tiny"]

bio.panel(ax, "A", (0.1, 8.3))
a = charts.axes_at(ax, (1.4, 1.0, 6.4, 6.4))
t = np.linspace(0, 30, 400)
for x, tok in levels:
    kobs = KON * x * KD + KOFF
    th_eq = x / (1 + x)
    a.plot(t, th_eq * (1 - np.exp(-kobs * t)), color=charts.line(tok), lw=1.9,
           label=f"[L] = {x:g} $K_\\mathrm{{d}}$")
    a.axhline(th_eq, color=charts.line(tok), lw=0.7, ls=":")
a.set_xlim(0, 30)
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="lower right", bbox_to_anchor=(1.0, 0.25), handlelength=1.6)
charts.style_axes(a, "$t$ / s", r"$\theta(t)$")
charts.title(a, "Association after mixing")
a.text(1, 0.94, r"$\theta(t) = \theta_{\mathrm{eq}}\,(1 - \mathrm{e}^{-k_{\mathrm{obs}}t})$", fontsize=tiny, color=P.ink())

bio.panel(ax, "B", (8.9, 8.3))
b = charts.axes_at(ax, (10.3, 1.0, 5.6, 6.4))
L = np.linspace(0, 120, 50)  # nM
b.plot(L, KON * L * 1e-9 + KOFF, color=charts.line("enzyme"), lw=1.8)
for x, tok in levels:
    b.plot([x * KD * 1e9], [KON * x * KD + KOFF], "o", ms=6, mfc=P.fill(tok), mec=charts.line(tok))
b.annotate("intercept $k_{\\mathrm{off}}$", (0, KOFF), (30, 0.12), fontsize=tiny, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.text(45, 0.95, "slope $k_{\\mathrm{on}}$", fontsize=tiny, color=P.ink())
b.set_xlim(0, 120)
b.set_ylim(0, 1.4)
charts.style_axes(b, "[L] / nM", r"$k_{\mathrm{obs}}$ / s$^{-1}$")
charts.title(b, r"$k_{\mathrm{obs}} = k_{\mathrm{on}}[\mathrm{L}] + k_{\mathrm{off}}$")

bio.panel(ax, "C", (17.0, 8.3))
c = charts.axes_at(ax, (18.4, 1.0, 5.3, 6.4))
x = np.logspace(-2.5, 2.5, 400)
c.semilogx(x, x / (1 + x), color=charts.line("enzyme"), lw=2.0)
c.axvspan(1 / 9, 9, color=P.light("highlight"), lw=0)
for th in (0.1, 0.5, 0.9):
    c.axhline(th, color=P.muted(), lw=0.6, ls=":")
c.text(1.0, 0.03, "81-fold", fontsize=tiny, color=P.ink(), ha="center")
c.set_xlim(10**-2.5, 10**2.5)
c.set_ylim(0, 1)
charts.style_axes(c, r"[L] / $K_\mathrm{d}$", r"$\theta_{\mathrm{eq}}$")
charts.title(c, "Equilibrium: 10 % to 90 %")
