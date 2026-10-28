"""The three-line system for producing hybrid seed with cytoplasmic male sterility (CMS), as used for hybrid rice.
Genotypes are written cytoplasm(nuclear restorer genotype): S = sterile cytoplasm, N = normal cytoplasm,
Rf = dominant fertility-restorer allele. A line S(rf rf): male sterile, used as the female parent.
B line N(rf rf), the maintainer: fertile, and as pollen parent on the A line it gives S(rf rf) progeny again.
R line N(Rf Rf), the restorer: as pollen parent on the A line it gives the F1 hybrid S(Rf rf), which is fertile."""

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(17.0, 8.6)


def line_box(xy, title, geno, note, token):
    bio.box(ax, xy, 4.0, 1.7, token=token)
    bio.label(ax, (xy[0], xy[1] + 0.45), title, size="normal", bold=True, color=P.on_fill())
    bio.label(ax, (xy[0], xy[1] - 0.05), geno, size="normal", color=P.on_fill())
    bio.label(ax, (xy[0], xy[1] - 0.5), note, size="tiny", color=P.on_fill())


A, B, R, F1 = (8.5, 6.6), (2.6, 6.6), (14.4, 6.6), (11.5, 2.0)
line_box(B, "B line (maintainer)", "N (rf rf)", "fertile", "positive")
line_box(A, "A line (CMS)", "S (rf rf)", "male sterile: female parent", "negative")
line_box(R, "R line (restorer)", "N (Rf Rf)", "fertile", "channel")
line_box(F1, "F1 hybrid", "S (Rf rf)", "fertile, heterotic", "highlight")
line_box((5.6, 2.0), "A line seed", "S (rf rf)", "sterile again", "negative")

bio.label(ax, (5.55, 7.05), "pollen", size="tiny")
bio.arrow(ax, (4.6, 6.6), (6.5, 6.6), kind="process")
bio.label(ax, (11.45, 7.05), "pollen", size="tiny")
bio.arrow(ax, (12.4, 6.6), (10.5, 6.6), kind="process")
bio.arrow(ax, (7.7, 5.7), (6.3, 2.9), kind="process")
bio.label(ax, (5.9, 4.4), "A x B\nmaintains the A line", size="tiny", ha="right")
bio.arrow(ax, (9.3, 5.7), (10.8, 2.9), kind="process")
bio.label(ax, (10.6, 4.4), "A x R\nhybrid seed", size="tiny", ha="left")
for c in (B, R):
    bio.arrow(ax, (c[0] - 0.8, c[1] + 1.0), (c[0] + 0.8, c[1] + 1.0), bend=0.5, kind="process")
    bio.label(ax, (c[0], c[1] + 1.75), "selfed: propagates itself", size="tiny")
bio.icon(ax, "dbcls/rice", at=(15.6, 2.0), height=2.4)
