# Spectral sensitivities of the photoreceptors used in color vision, computed with the visual-pigment
# template of Govardovskii et al. (2000) (A1 chromophore, alpha + beta bands) from published peak
# wavelengths: human cones 420/534/564 nm; dog 429/555 nm; honey bee 344/436/544 nm;
# blue tit single cones 371/449/502/563 nm (Hart et al. 2000). Colored oil droplets, which narrow
# the bird curves, and ocular media are ignored.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P


def template(lam, lmax):
    x = lmax / lam
    a = 0.8795 + 0.0459 * np.exp(-((lmax - 300) ** 2) / 11940)
    alpha = 1 / (np.exp(69.7 * (a - x)) + np.exp(28 * (0.922 - x)) + np.exp(-14.9 * (1.104 - x)) + 0.674)
    lmb = 189 + 0.315 * lmax
    bb = -40.5 + 0.195 * lmax
    beta = 0.26 * np.exp(-(((lam - lmb) / bb) ** 2))
    s = alpha + beta
    return s / s.max()


lam = np.linspace(300, 700, 400)
TOK = {"UV": "protein", "S": "channel", "M": "positive", "L": "negative"}
SPECIES = [("Human (trichromat)", [("S", 420), ("M", 534), ("L", 564)]),
           ("Dog (dichromat)", [("S", 429), ("L", 555)]),
           ("Honey bee (trichromat, UV)", [("UV", 344), ("S", 436), ("M", 544)]),
           ("Blue tit (tetrachromat, UV)", [("UV", 371), ("S", 449), ("M", 502), ("L", 563)])]
fig, ax = bio.canvas(22, 12.4)
for k, (name, cones) in enumerate(SPECIES):
    col, row = k % 2, k // 2
    x0, y0 = 1.6 + 10.6 * col, 7.0 - 5.6 * row
    p = quant.Plot(ax, (x0, y0, 9.0, 3.8), xlim=(300, 700), ylim=(0, 1.05),
                   xlabel="Wavelength / nm" if row == 1 else None,
                   ylabel="Relative sensitivity" if col == 0 else None,
                   xticks=[300, 400, 500, 600, 700], yticks=[0, 0.5, 1])
    p.span(300, 400, "neutral", strength=0.35, text="UV" if k == 0 else None)
    for cls, lm in cones:
        p.line(lam, template(lam, lm), TOK[cls])
        p.text(lm, 1.12, f"{lm}", token=TOK[cls])
    bio.label(ax, (x0, y0 + 4.55), name, size="small", bold=True, ha="left")
bio.label(ax, (11.0, 0.35), "invisible to humans below about 400 nm (grey band)", size="tiny", color=P.muted())
