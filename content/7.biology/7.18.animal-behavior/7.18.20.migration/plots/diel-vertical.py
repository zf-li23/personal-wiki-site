"""Model: diel vertical migration following an isolume (the 'preferred light level' hypothesis). Surface irradiance
I0(t) follows the sun (zero at night, with a weak moonlit minimum); light decays with depth as I0 exp(-K z)
(K = 0.06 per m, clear oceanic water). An animal that stays at the depth where light equals a constant I* (here
1e-4 of noon surface light, too dim for visual predators to see it) is z(t) = ln(I0(t)/I*)/K, limited by a
maximum depth of 250 m and by the surface. It rises at dusk to feed in the surface layer at night and descends at
dawn. Day length 12 h (left) and 18 h (right, high-latitude summer): the night at the surface becomes short, as
observed for Antarctic krill in summer."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
K, Istar, zmax = 0.06, 1e-4, 250.0
fig, ax = bio.canvas(24, 9.8)
h = np.linspace(0, 48, 2000)
for k, (dl, title) in enumerate([(12, "Day length 12 h"), (18, "Day length 18 h")]):
    x0 = 2.0 + k * 11.6
    bio.panel(ax, "AB"[k], (x0 - 1.6, 9.5))
    bio.label(ax, (x0 + 4.6, 9.2), title, size="small", bold=True)
    p = quant.Plot(ax, (x0, 1.8, 9.2, 6.6), xlim=(0, 48), ylim=(-260, 10), xlabel="Time / h",
                   ylabel="Depth / m" if k == 0 else None, xticks=[0, 12, 24, 36, 48],
                   yticks=[(0, "0"), (-100, "100"), (-200, "200")])
    sun = np.sin(np.pi * (np.mod(h - (12 - dl / 2), 24)) / dl)
    I0 = np.where(np.mod(h - (12 - dl / 2), 24) < dl, np.clip(sun, 0, None), 0) + 1e-6
    z = np.clip(np.log(I0 / Istar) / K, 0, zmax)
    for d0 in (0, 24):
        a, b = d0 + 12 - dl / 2, d0 + 12 + dl / 2
        p.span(a, b, "highlight", strength=0.75)
    p.line(h, -z, "dna", lw=1.8)
    p.text(24, -245, "night: feeding near the surface" if k == 0 else "short night", size="tiny")
ax.set_ylim(0.3, 9.8)
