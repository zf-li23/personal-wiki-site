"""Rate-theory (Eyring) models of permeation through a channel with one binding site between two
barriers. A: free-energy profile along the pore (electrical distance 0 = inside, 1 = outside), at
0 mV and at +60 mV, where the field tilts the profile. B: current-voltage curves with symmetric
solutions (100 mM on both sides) for symmetric barriers (ohmic-like, linear near 0) and for an
asymmetric pore (binding site near the inner end, outer barrier higher): the I-V curve bends although
the solutions are identical, so asymmetry of the pore alone rectifies. C: single-channel conductance at 0 mV against the
symmetric ion concentration: a one-site pore saturates with Michaelis-Menten form,
as measured for K+ and Na+ channels, unlike free electrodiffusion, which is linear in concentration."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)
F_RT = 1 / 25.7  # 1/mV at 25 C


def rates(V, G1, Gs, G2, d1=0.25, ds=0.5, d2=0.75, nu=1.0):
    # barrier peaks G1 (at d1), well Gs (at ds), barrier G2 (at d2), energies in kT at 0 mV, inside at 0
    u = V * F_RT  # electrical energy of a cation at fractional distance x: -u * x (inside potential V)
    # positive V = inside positive, pushes cation outward: energy at x is +u*(1-x) relative...
    E = lambda G, x: G + u * (1 - x)
    Ein, Eout = u * 1.0, 0.0
    k_in_on = nu * np.exp(-(E(G1, d1) - Ein))      # inside -> site (per M)
    k_site_in = nu * np.exp(-(E(G1, d1) - E(Gs, ds)))
    k_site_out = nu * np.exp(-(E(G2, d2) - E(Gs, ds)))
    k_out_on = nu * np.exp(-(E(G2, d2) - Eout))
    return k_in_on, k_site_in, k_site_out, k_out_on


def current(V, ci, co, G1, Gs, G2, d=(0.25, 0.5, 0.75)):
    a, b, c, d = rates(V, G1, Gs, G2, *d)
    on = a * ci + d * co
    p_occ = on / (on + b + c)
    # net outward flux = p_occ * c - (1 - p_occ) * d * co
    return p_occ * c - (1 - p_occ) * d * co


ax = axs[0]
x = np.array([0, 0.25, 0.5, 0.75, 1.0])
for V, tok in [(0.0, "neutral"), (60.0, "k")]:
    u = V * F_RT
    G = np.array([0, 8, -2, 8, 0]) + u * (1 - x)
    xs = np.linspace(0, 1, 200)
    ax.plot(xs, np.interp(xs, x, G), color=charts.line(tok), lw=1.6, label=f"V = {V:g} mV")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "electrical distance (inside 0, outside 1)", r"$G/k_{\mathrm{B}}T$")
charts.title(ax, "A  Two-barrier profile")

ax = axs[1]
V = np.linspace(-120, 120, 300)
for (G1, G2, dd), tok, lab in [((8, 8, (0.25, 0.5, 0.75)), "dna", "symmetric pore"),
                               ((6, 10, (0.1, 0.2, 0.8)), "blood", "site near inside,\nouter barrier higher")]:
    I = current(V, 0.1, 0.1, G1, -2, G2, dd)
    ax.plot(V, I / np.max(np.abs(I)), color=charts.line(tok), lw=1.7, label=lab)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(0, color=P.muted(), lw=0.6)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "V / mV (100 mM both sides)", "normalized current")
charts.title(ax, "B  Rectification by asymmetry")

ax = axs[2]
c = np.linspace(0.001, 1.0, 200)
g = []
for ci in c:
    dV = 0.5
    g.append((current(dV, ci, ci, 8, -2, 8) - current(-dV, ci, ci, 8, -2, 8)) / (2 * dV))
g = np.array(g)
ax.plot(c * 1e3, g / g.max(), color=charts.line("k"), lw=1.8, label="one-site pore")
ax.plot(c * 1e3, c / c.max(), "--", color=P.muted(), lw=1.0, label="free electrodiffusion")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "concentration / mM", "conductance (normalized)")
charts.title(ax, "C  Saturation")
