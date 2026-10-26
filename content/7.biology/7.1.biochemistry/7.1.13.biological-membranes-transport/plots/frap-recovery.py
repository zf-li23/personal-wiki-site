"""Lateral diffusion in membranes.

A: fluorescence recovery after photobleaching (FRAP) of a uniformly bleached circular spot of area
5 um^2 (radius w = 1.26 um), from the diffusion solution of Soumpasis (1983):
f(t) = exp(-2 tau/t) [I0(2 tau/t) + I1(2 tau/t)], tau = w^2/(4D), scaled by the mobile fraction.
A lipid (D = 1 um^2/s, all mobile) recovers within seconds; a membrane protein (D = 0.05 um^2/s)
recovers about twenty times more slowly, and only to 70% if 30% of the molecules are immobilized
(for example by the cytoskeleton).
B: Saffman-Delbrueck relation for a cylinder of radius a spanning a membrane of thickness
h = 4 nm and viscosity 0.1 Pa s in water (1 mPa s) at 310 K, compared with the Stokes-Einstein
relation D = kT/(6 pi eta a) for a sphere in water: the membrane diffusion coefficient depends
only logarithmically on radius.
"""

import numpy as np
from scipy.special import i0e, i1e
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 7.6)


def soumpasis(t, tau):
    x = 2 * tau / t
    return i0e(x) + i1e(x)  # exp(-x)(I0 + I1) with exponentially scaled Bessel functions


w = np.sqrt(5 / np.pi)
t = np.linspace(1e-3, 60, 1200)
bio.panel(ax, "A", (0.1, 7.5))
pa = charts.axes_at(ax, (1.6, 1.4, 7.6, 5.4))
cases = [("lipid, D = 1 µm² s⁻¹", 1.0, 1.0, "lipid_head"), ("protein, D = 0.05 µm² s⁻¹", 0.05, 1.0, "protein"),
         ("protein, D = 0.05, mobile fraction 0.7", 0.05, 0.7, "negative")]
for name, D, mf, tok in cases:
    tau = w**2 / (4 * D)
    pa.plot(t, 100 * mf * soumpasis(t, tau), color=charts.line(tok), lw=1.8, label=name)
pa.axvline(0, color=P.muted(), lw=0.6)
pa.set_xlim(-1, 60)
pa.set_ylim(0, 105)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "time after bleaching / s", "fluorescence in spot / % of prebleach")
charts.title(pa, "FRAP of a 5 µm² spot")

bio.panel(ax, "B", (10.3, 7.5))
pb = charts.axes_at(ax, (11.9, 1.4, 7.4, 5.4))
kT = 1.380649e-23 * 310
mu_m, h, eta = 0.1, 4e-9, 1e-3
a = np.logspace(np.log10(0.3e-9), np.log10(20e-9), 200)
D_sd = kT / (4 * np.pi * mu_m * h) * (np.log(mu_m * h / (eta * a)) - 0.5772)
D_se = kT / (6 * np.pi * eta * a)
pb.loglog(a * 1e9, D_sd * 1e12, color=charts.line("protein"), lw=1.8, label="in membrane (Saffman–Delbrück)")
pb.loglog(a * 1e9, D_se * 1e12, color=charts.line("dna"), lw=1.8, ls=(0, (4, 2.4)), label="sphere in water (Stokes–Einstein)")
pb.set_xlim(0.3, 20)
pb.set_ylim(0.5, 1000)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "radius a / nm", "D / (µm² s⁻¹)")
charts.title(pb, "Size dependence of diffusion")
