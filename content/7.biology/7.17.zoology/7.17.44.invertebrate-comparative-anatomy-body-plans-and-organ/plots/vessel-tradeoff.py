"""Why closed circulatory systems run at high pressure and open ones at low pressure: a Poiseuille model.

Blood or hemolymph flows at a mean velocity v through parallel channels of radius r and length L that
take up a fixed fraction phi of the tissue volume. By the Hagen-Poiseuille law the pressure needed to
drive the flow is dp = 8 mu v L / r^2 (independent of the number of channels when v is fixed). The
channels are spaced s = r * sqrt(pi / phi) apart, so the farthest cell lies x = s / 2 from a channel,
and oxygen needs t = x^2 / (2 D) to diffuse that far. Fine channels (capillaries) shorten diffusion but
need high pressure; wide channels (sinuses of an open system) need almost no pressure but leave long
diffusion paths. Illustrative parameters: v = 0.5 mm/s, L = 1 mm, mu = 1.5 mPa s, phi = 0.1,
D = 2e-9 m^2/s.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
mu, v, L, phi, D = 1.5e-3, 5e-4, 1e-3, 0.1, 2e-9
r = np.logspace(np.log10(1e-6), np.log10(2e-3), 200)
dp = 8 * mu * v * L / r**2
x = 0.5 * r * np.sqrt(np.pi / phi)
tdiff = x**2 / (2 * D)

fig, ax = bio.canvas(24.0, 9.4)
um = r * 1e6
xt = [(1, "1"), (10, "10"), (100, "100"), (1000, "1000")]
for k, (yv, ylab, ylim, yt, tok, title) in enumerate((
        (dp, "pressure drop Δp / Pa", (1e-3, 1e4), [(1e-3, "0.001"), (1e-1, "0.1"), (10, "10"), (1e3, "1000")], "negative",
         "A  Pressure to drive the flow"),
        (tdiff, "diffusion time t / s", (1e-3, 1e4), [(1e-3, "0.001"), (1e-1, "0.1"), (10, "10"), (1e3, "1000")],
         "dna", "B  Diffusion from channel to tissue"))):
    x0 = 2.3 + k * 11.6
    p = quant.Plot(ax, (x0, 1.5, 8.6, 6.6), xlim=(1, 2000), ylim=ylim, xlog=True, ylog=True,
                   xlabel="channel radius r / µm", ylabel=ylab, xticks=xt, yticks=yt)
    p.span(2, 6, "negative", text="capillaries", text_y=8.25)
    p.span(50, 1000, "highlight", text="sinuses, lacunae", text_y=8.25)
    p.line(um, yv, tok, lw=2.0)
    bio.label(ax, (x0, 9.05), title, size="small", bold=True, ha="left")
bio.label(ax, (6.6, 6.9), "Δp = 8 µ v L / r²", size="small", color=quant.line_color("negative"))
bio.label(ax, (18.2, 6.9), "t = x² / 2D,  x ∝ r", size="small", color=quant.line_color("dna"))
