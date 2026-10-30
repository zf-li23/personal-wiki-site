"""Spermatogenesis. A: cross-section of a seminiferous tubule. Spermatogonia sit on the basement membrane,
spermatocytes in meiosis and spermatids lie progressively closer to the lumen, all embedded in Sertoli cells;
peritubular myoid cells surround the tubule and Leydig cells (testosterone) lie in the interstitium beside the
capillaries. B: one type B spermatogonium gives two primary spermatocytes' worth of descendants; here one
primary spermatocyte gives two secondary spermatocytes and four spermatids, which stay joined by cytoplasmic
bridges until they are released as sperm. C: duration of the phases in the mouse (about 35 days) and in humans
(about 64-74 days); each spermatogonium entering differentiation joins the cycle of the seminiferous epithelium,
whose period (8.6 days in the mouse, 16 days in humans) is about a quarter of the whole process."""
import wikibio as bio
from wikibio import organogenesis as O, quant

P = bio.P
fig, ax = bio.canvas(26, 11)
bio.panel(ax, "A", (0.2, 10.8))
t = O.seminiferous_tubule(ax, (5.0, 5.6), 3.6)
bio.callout(ax, t["spermatogonium"], (0.4, 1.2), "Spermatogonia")
bio.callout(ax, t["spermatocyte"], (0.4, 10.0), "Spermatocytes")
bio.callout(ax, t["spermatid"], (9.6, 10.4), "Spermatids")
bio.callout(ax, t["sperm"], (9.9, 1.0), "Sperm in lumen")
bio.callout(ax, t["leydig"], (10.2, 9.4), "Leydig cells")
bio.callout(ax, t["sertoli"], (10.2, 5.6), "Sertoli cell nucleus")
bio.callout(ax, t["myoid"], (10.0, 2.0), "Peritubular myoid cells")

bio.panel(ax, "B", (12.6, 10.8))
g = O.germ_lineage(ax, (13.8, 7.6), "sperm", step=2.3, r=0.42)
for key, txt in (("gonium", "B spermatogonium\n2n, 2c"), ("primary", "primary\nspermatocyte\n2n, 4c"),
                 ("secondary", "secondary\nspermatocytes\n1n, 2c"), ("spermatid", "spermatids\n1n, 1c"), ("sperm", "sperm")):
    bio.label(ax, (g[key][0], 5.6), txt, size="tiny", color=P.muted())
for a_, b_, txt in (("primary", "secondary", "meiosis I"), ("secondary", "spermatid", "meiosis II"), ("spermatid", "sperm", "spermiogenesis")):
    bio.label(ax, ((g[a_][0] + g[b_][0]) / 2, 9.4), txt, size="tiny", color=P.muted())
bio.callout(ax, (g["spermatid"][0], g["spermatid"][1] + 0.38), (24.6, 10.4), "cytoplasmic bridges")

bio.panel(ax, "C", (12.6, 4.6))
pl = quant.Plot(ax, (15.2, 1.2, 10.2, 2.6), xlim=(0, 75), ylim=(0, 2), xlabel="days", ylabel=None, xticks=[0, 20, 40, 60, 75],
                yticks=[])
for row, (name, seg) in enumerate((("human", (16, 24, 24)), ("mouse", (8, 13, 13.5)))):
    x0 = 0
    y = 0.5 + row
    for k, (d, tk) in enumerate(zip(seg, ("protein", "receptor", "channel"))):
        X0, Y0 = pl.xy(x0, y - 0.32)
        X1, Y1 = pl.xy(x0 + d, y + 0.32)
        bio.shape(ax, [(X0, Y0), (X1, Y0), (X1, Y1), (X0, Y1)], tk, lw=0.7, zorder=8)
        x0 += d
    bio.label(ax, (pl.xy(0, y)[0] - 0.2, pl.xy(0, y)[1]), name, size="small", ha="right")
for k, (txt, tk) in enumerate((("spermatogonia", "protein"), ("spermatocytes (meiosis)", "receptor"), ("spermiogenesis", "channel"))):
    bio.box(ax, (16.0 + 3.6 * k, 4.4), 0.4, 0.3, tk)
    bio.label(ax, (16.3 + 3.6 * k, 4.4), txt, size="tiny", ha="left")
