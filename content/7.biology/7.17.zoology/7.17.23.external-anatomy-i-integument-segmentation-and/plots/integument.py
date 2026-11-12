# A: the insect integument in section (schematic, layers not to scale). From outside: cement and wax
# layers, the epicuticle (no chitin), the procuticle of chitin microfibrils in a protein matrix, divided
# into the sclerotized exocuticle and the unsclerotized endocuticle, both laminated by the helicoidal
# arrangement of microfibrils; pore canals carry lipids from the epidermis to the surface and branch into
# wax canals in the epicuticle. The epidermis (a single cell layer) secretes the cuticle and rests on the
# basement membrane facing the hemocoel. A dermal gland opens by a duct; a seta is formed by a trichogen
# cell (hair) and a tormogen cell (socket) and innervated by a sensory neuron.
# B: interference colour. Reflectance at normal incidence of a stack of five chitin-air layer pairs
# (refractive indices 1.56 and 1.0), computed by the transfer-matrix method; quarter-wave layers tuned to
# three wavelengths. The reflected peak is at lambda = 2 (n1 d1 + n2 d2) and shifts to shorter wavelengths
# at oblique incidence (iridescence).
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(27, 12)
bio.panel(ax, "A", (0.2, 11.6))
bio.panel(ax, "B", (16.0, 11.6))
X0, X1 = 1.0, 11.0
layers = [("Cement", "carbohydrate", 9.55, 9.75), ("Wax", "lipid", 9.3, 9.55), ("Epicuticle", "highlight", 8.9, 9.3),
          ("Exocuticle", "drug", 7.0, 8.9), ("Endocuticle", "bone", 4.2, 7.0)]
for name, tok, y0, y1 in layers:
    bio.shape(ax, [(X0, y0), (X1, y0), (X1, y1), (X0, y1)], tok, lw=0.6, zorder=3)
# lamellae
for y0, y1, step in ((7.0, 8.9, 0.22), (4.2, 7.0, 0.32)):
    for y in np.arange(y0 + step / 2, y1, step):
        xs = np.linspace(X0, X1, 120)
        ax.plot(xs, y + 0.03 * np.sin(xs * 3.0 + y * 9), color=P.muted(), lw=0.35, zorder=4)
# epidermis cells
cells = np.linspace(X0, X1, 9)
for a, b in zip(cells[:-1], cells[1:]):
    bio.shape(ax, [(a, 2.7), (b, 2.7), (b, 4.2), (a, 4.2)], "cytoplasm", lw=0.6, zorder=3)
    ax.add_patch(__import__("matplotlib").patches.Ellipse(((a + b) / 2, 3.4), 0.5, 0.35, facecolor=P.fill("nucleus"),
                                                          edgecolor=P.edge("nucleus"), lw=0.6, zorder=4))
ax.plot([X0, X1], [2.65, 2.65], color=P.edge("extracellular"), lw=2.2, zorder=4)
bio.label(ax, (6.0, 2.1), "Hemocoel", size="small", color=P.muted())
# pore canals
for x in (2.0, 3.6, 8.3, 9.8):
    ys = np.linspace(4.2, 8.9, 60)
    ax.plot(x + 0.06 * np.sin(ys * 6), ys, color=P.edge("lipid"), lw=0.8, zorder=5)
    for dx in (-0.12, 0.0, 0.12):
        ax.plot([x, x + dx], [8.9, 9.3], color=P.edge("lipid"), lw=0.5, zorder=5)
# dermal gland with duct
ax.add_patch(__import__("matplotlib").patches.Ellipse((5.0, 2.95), 1.2, 0.8, facecolor=P.fill("vesicle"),
                                                      edgecolor=P.edge("vesicle"), lw=0.8, zorder=6))
ax.plot([5.0, 5.0], [3.3, 9.75], color=P.edge("vesicle"), lw=1.4, zorder=6)
# seta with socket
ax.plot([7.0, 7.0], [3.2, 9.75], color=P.edge("neuron"), lw=0.9, zorder=6)
bio.shape(ax, [(6.75, 9.75), (7.25, 9.75), (7.2, 10.0), (6.8, 10.0)], "drug", lw=0.7, zorder=7)
hx = np.array([7.0, 7.15, 7.5, 8.0])
hy = np.array([9.9, 10.5, 11.0, 11.35])
ax.plot(hx, hy, color=P.edge("drug"), lw=2.0, zorder=7, solid_capstyle="round")
ax.add_patch(__import__("matplotlib").patches.Ellipse((7.0, 3.0), 0.9, 0.6, facecolor=P.fill("neuron"),
                                                      edgecolor=P.edge("neuron"), lw=0.7, zorder=6))
bio.label(ax, (7.0, 3.0), "", size="tiny")
for name, tok, y0, y1 in layers:
    bio.callout(ax, (X1 - 0.2, (y0 + y1) / 2), (12.6, (y0 + y1) / 2 + {"Cement": 1.2, "Wax": 0.6, "Epicuticle": 0.0}.get(name, 0)), name)
bio.callout(ax, (X1 - 0.2, 3.6), (12.6, 3.6), "Epidermis")
bio.callout(ax, (X1 - 0.3, 2.65), (12.6, 2.6), "Basement membrane")
bio.callout(ax, (9.8 + 0.05, 6.0), (12.6, 6.0), "Pore canal")
bio.callout(ax, (5.0, 2.6), (3.2, 1.3), "Dermal gland")
bio.callout(ax, (7.0, 2.75), (8.6, 1.3), "Sensory neuron")
bio.callout(ax, (7.8, 11.2), (9.2, 11.4), "Seta (trichogen cell)")
bio.callout(ax, (6.8, 9.9), (4.4, 11.2), "Socket (tormogen cell)")
ax.annotate("", xy=(0.6, 4.2), xytext=(0.6, 8.9), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
bio.label(ax, (0.35, 6.55), "Procuticle", size="small", rotation=90)

# B: multilayer reflectance
def reflectance(lam, n_layers, d_layers, n_in=1.0, n_sub=1.0):
    M = np.array([[1, 0], [0, 1]], dtype=complex)
    for n, d in zip(n_layers, d_layers):
        delta = 2 * np.pi * n * d / lam
        M = M @ np.array([[np.cos(delta), 1j * np.sin(delta) / n], [1j * n * np.sin(delta), np.cos(delta)]])
    B, C = M @ np.array([1, n_sub])
    r = (n_in * B - C) / (n_in * B + C)
    return abs(r) ** 2

pax = charts.axes_at(ax, (17.5, 1.6, 8.8, 9.0))
lam = np.linspace(350, 800, 500)
n1, n2 = 1.56, 1.0
for peak, tok in ((450, "channel"), (530, "positive"), (620, "negative")):
    d1, d2 = peak / (4 * n1), peak / (4 * n2)
    R = [reflectance(l, [n1, n2] * 5 + [n1], [d1, d2] * 5 + [d1]) for l in lam]
    pax.plot(lam, R, color=charts.line(tok), lw=1.6)
    pax.text(peak, max(R) + 0.02, "%d nm" % peak, ha="center", fontsize=8, color=charts.line(tok))
pax.set_xlim(350, 800)
pax.set_ylim(0, 1.08)
charts.style_axes(pax, "Wavelength / nm", "Reflectance")
bio.label(ax, (21.9, 11.2), "Chitin-air multilayer, 5 periods", size="small")
