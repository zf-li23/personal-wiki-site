"""Gels and springs of the extracellular matrix.

A: an aggrecan aggregate of cartilage: up to about 100 aggrecan molecules (core protein with about 100
chondroitin sulfate and keratan sulfate chains) bound through link proteins to one hyaluronan chain; the
aggregate can be several micrometres long (here six aggrecans). B: why such a gel swells. The fixed negative
charges of the GAG chains (concentration c_F) hold counterions in the tissue (Donnan equilibrium with a bath
of NaCl at c_0 = 0.15 mol/L); the excess of mobile ions inside gives the osmotic swelling pressure
    Pi = R T [ sqrt(c_F^2 + 4 c_0^2) - 2 c_0 ],
plotted at T = 310 K; the shaded band is the range of fixed charge density in articular cartilage
(about 0.1-0.3 mol/L), which gives about 0.04-0.3 MPa and lets cartilage resist compression. C: elastin molecules
cross-linked into a network of random coils, relaxed and stretched: stretching straightens the chains and
lowers their conformational entropy, which provides the restoring force. D: stress-strain curves (log
scale): an ideal rubber network, sigma = (E/3)(lambda - 1/lambda^2) with E = 1 MPa (elastin), extensible
to more than 100 % strain; a tendon (type I collagen), with a toe region in which crimped fibrils straighten,
then a linear region with a modulus of about 1.2 GPa, and failure near 10 % strain (illustrative curve).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(28.0, 13.0)

bio.panel(ax, "A", (0.1, 12.9))
a = J.aggrecan_aggregate(ax, (0.8, 9.0), (13.2, 9.0), n=6, chain_len=0.5, core=2.3)
bio.callout(ax, a["hyaluronan"], (0.8, 11.9), "Hyaluronan")
bio.callout(ax, a["aggrecan"], (5.8, 12.3), "Aggrecan core protein")
bio.callout(ax, a["gag"], (8.6, 12.6), "Chondroitin and keratan sulfate chains")
bio.callout(ax, a["link"], (6.2, 6.2), "Link protein")

# B: Donnan swelling pressure
bio.panel(ax, "B", (15.0, 12.9))
pb = charts.axes_at(ax, (16.6, 7.4, 10.4, 4.8))
R, T, c0 = 8.314, 310.0, 150.0  # J/(mol K), K, mol/m^3
cF = np.linspace(0, 400, 200)  # mol/m^3
Pi = R * T * (np.sqrt(cF**2 + 4 * c0**2) - 2 * c0) / 1e3  # kPa
pb.axvspan(0.1, 0.3, color=P.mix(P.fill(J.tok("gag")), P.surface(), 0.55), lw=0)
pb.plot(cF / 1000, Pi, color=quant.line_color(J.tok("gag")), lw=2.0)
pb.set_xlim(0, 0.4)
pb.set_ylim(0, 650)
pb.text(0.2, 560, "cartilage", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(pb, "fixed charge density $c_{\\mathrm{F}}$ / (mol L$^{-1}$)", "swelling pressure $\\Pi$ / kPa")
charts.title(pb, "Donnan swelling of a GAG gel")

# C: elastin network relaxed and stretched
bio.panel(ax, "C", (0.1, 5.4))
e = J.elastin(ax, (2.8, 2.6), 3.0, 2.8, stretch=0.0)
J.elastin(ax, (9.6, 2.6), 3.0, 2.8, stretch=1.0)
bio.arrow(ax, (5.0, 2.6), (6.0, 2.6), kind="process")
bio.label(ax, (2.8, 0.4), "Relaxed", size="small")
bio.label(ax, (9.6, 0.4), "Stretched", size="small")
bio.callout(ax, e["crosslink"], (0.4, 4.9), "Cross-link", size="tiny")
bio.label(ax, (5.5, 3.2), "stretch", size="tiny", color=P.muted())

# D: stress-strain
bio.panel(ax, "D", (15.0, 5.4))
pd = charts.axes_at(ax, (16.6, 1.1, 10.4, 3.9))
eps = np.linspace(0, 1.5, 300)
lam = 1 + eps
sig_el = (1.0 / 3) * (lam - 1 / lam**2)  # MPa
pd.plot(eps * 100, sig_el, color=quant.line_color(J.tok("elastin")), lw=2.0, label="elastin (rubber network, E = 1 MPa)")
et = np.linspace(0.0005, 0.1, 300)
toe = 0.02
E = 1200.0
sig_t = np.where(et < toe, E * toe / 2 * (et / toe) ** 2, E * (et - toe / 2))
pd.plot(et * 100, sig_t, color=quant.line_color(J.tok("collagen")), lw=2.0, label="tendon (type I collagen, E ≈ 1.2 GPa)")
pd.plot([10], [sig_t[-1]], marker="x", color=quant.line_color(J.tok("collagen")), ms=7, mew=1.6)
pd.set_yscale("log")
pd.set_ylim(1e-3, 300)
pd.set_xlim(0, 150)
pd.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pd, "strain / %", "stress / MPa")
charts.title(pd, "Elastic fibers stretch, collagen resists")
