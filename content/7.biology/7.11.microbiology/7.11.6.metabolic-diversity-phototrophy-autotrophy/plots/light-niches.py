"""Why phototrophs stratify: the spectrum of light left at depth (Beer-Lambert model, illustrative).

Irradiance at depth z and wavelength l: I(l, z) = I0 exp(-integral of a(l, z') dz'), with a flat surface
spectrum I0 = 1 (equal photon flux at every wavelength). a = a_water + sum over layers of c_k A_k(l), where
A_k is the normalized in vivo absorption of the layer's pigments (Gaussian bands at the maxima of the
companion figure) and c_k its strength.
A: stratified lake (depth in m). Pure-water absorption coefficients are approximate literature values
(about 0.01 m^-1 in the blue, 0.06 at 550 nm, 0.34 at 650 nm, 2-2.5 m^-1 at 750-800 nm, 4-7 m^-1 at
850-900 nm); a cyanobacterial layer (chlorophyll a, phycocyanin, carotenoids) occupies 0-3 m. Below a few
metres only blue-green light (about 450-570 nm) remains: purple and green sulfur bacteria in the
sulfidic hypolimnion must harvest it with carotenoids and the blue (Soret) bands of their
bacteriochlorophylls.
B: microbial mat (depth in mm, water absorption negligible). A 1-mm layer of cyanobacteria removes the
visible light; near-infrared light passes and is absorbed below by bacteriochlorophyll a (purple bacteria,
800-900 nm) and c (green bacteria, about 750 nm).
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
lam = np.linspace(400, 920, 521)


def bands(spec):
    y = np.zeros_like(lam)
    for c, s, h in spec:
        y += h * np.exp(-0.5 * ((lam - c) / s) ** 2)
    return y / y.max()


cyano = bands([(435, 18, 1.0), (680, 14, 0.75), (620, 20, 0.9), (485, 22, 0.6)])
purple = bands([(375, 16, 0.9), (590, 14, 0.3), (805, 14, 0.7), (870, 20, 1.0), (500, 25, 0.5)])
green = bands([(460, 22, 0.55), (750, 20, 1.0)])
wl = np.array([400, 420, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850,
               875, 900, 920])
aw = np.array([0.0066, 0.0045, 0.0092, 0.0114, 0.0204, 0.0425, 0.0565, 0.0943, 0.2224, 0.2834, 0.34, 0.4245,
               0.624, 1.7, 2.47, 2.4, 2.07, 2.8, 4.3, 5.0, 6.8, 12.0])
a_water = np.exp(np.interp(lam, wl, np.log(aw)))


def profile(z, layers, water=True):
    """I(lambda) at depth z below layers (z0, z1, strength, absorption spectrum)."""
    tau = (a_water * z) if water else np.zeros_like(lam)
    for z0, z1, c, A in layers:
        tau = tau + c * A * max(0.0, min(z, z1) - z0)
    return np.exp(-tau)


# A: lake ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 10.8))
bio.label(ax, (6.8, 10.5), "Stratified lake", size="small", bold=True)
pa = quant.Plot(ax, (1.9, 3.0, 9.8, 6.6), xlim=(400, 920), ylim=(1e-4, 1.5), ylog=True, xlabel="wavelength / nm",
                ylabel="relative irradiance", xticks=[400, 500, 600, 700, 800, 900],
                yticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "0.01"), (0.1, "0.1"), (1, "1")])
lake = [(0.0, 3.0, 0.9, cyano)]
for z, tok, at in ((0.5, "highlight", 0.80), (2.0, "enzyme", 0.70), (4.0, "protein", 0.45), (7.0, "plant", 0.33)):
    I = np.clip(profile(z, lake), 1e-9, None)
    pa.line(lam, I, tok, lw=1.5)
pa.legend([("0.5 m", "highlight", "-"), ("2 m (in the cyanobacterial layer)", "enzyme", "-"),
           ("4 m (purple sulfur bacteria)", "protein", "-"), ("7 m (green sulfur bacteria)", "plant", "-")],
          at=(3.0, 1.6))
pa.span(450, 570, "plant", strength=0.3)
pa.text(510, 1.25, "left at depth", size="tiny", token="plant")

# B: mat ----------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.4, 10.8))
bio.label(ax, (18.6, 10.5), "Microbial mat", size="small", bold=True)
pb = quant.Plot(ax, (13.9, 3.0, 9.8, 6.6), xlim=(400, 920), ylim=(1e-4, 1.5), ylog=True, xlabel="wavelength / nm",
                ylabel="relative irradiance", xticks=[400, 500, 600, 700, 800, 900],
                yticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "0.01"), (0.1, "0.1"), (1, "1")])
mat = [(0.0, 1.0, 7.0, cyano), (1.0, 1.6, 6.0, purple), (1.6, 2.4, 7.0, green)]
for z, tok, txt in ((0.0, "highlight", "surface"), (1.0, "enzyme", "1.0 mm: below cyanobacteria"),
                    (1.6, "protein", "1.6 mm: below purple bacteria"), (2.4, "plant", "2.4 mm: below green bacteria")):
    I = np.clip(profile(z, mat, water=False), 1e-9, None)
    pb.line(lam, I, tok, lw=1.5)
pb.legend([("surface", "highlight", "-"), ("1.0 mm: below cyanobacteria", "enzyme", "-"),
           ("1.6 mm: below purple bacteria", "protein", "-"), ("2.4 mm: below green bacteria", "plant", "-")],
          at=(15.0, 1.6))
pb.span(780, 900, "protein", strength=0.3)
pb.span(730, 770, "plant", strength=0.3)
pb.text(840, 1.25, "Bchl a", size="tiny", token="protein")
pb.text(750, 1.25, "Bchl c", size="tiny", token="plant")
