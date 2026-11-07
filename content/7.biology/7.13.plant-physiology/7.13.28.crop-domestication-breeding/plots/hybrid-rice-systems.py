# Seed systems of hybrid rice (schematic).
# A: three-line system. The CMS line (A line, S(rf rf)) is male sterile; it is propagated by pollination
#    with the maintainer line (B line, N(rf rf)), which has the same nucleus but normal cytoplasm, and
#    crossed with the restorer line (R line, carrying dominant Rf) to produce F1 seed S(Rf rf), which
#    is fertile and is sown in the field. B and R lines are propagated by selfing.
# B: two-line system. A photoperiod/thermo-sensitive genic male-sterile (PTGMS) line is sterile under
#    long days / high temperature (used for hybrid seed production with any fertile pollen parent) and
#    fertile under short days / low temperature (propagated by selfing): no maintainer line is needed.
import wikibio as bio

fig, ax = bio.canvas(24, 11.5)
W, H = 4.6, 1.9


def line_box(xy, title, genotype, token):
    bio.box(ax, xy, W, H, token=token)
    bio.label(ax, (xy[0], xy[1] + 0.38), title, size="normal", bold=True, color=bio.P.on_fill())
    bio.label(ax, (xy[0], xy[1] - 0.42), genotype, size="small", italic=True, color=bio.P.on_fill())


def cross(a, b, text=None, kind="process", bend=0.0):
    bio.arrow(ax, a, b, kind=kind, bend=bend)
    if text:
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        bio.label(ax, (m[0], m[1] + 0.35), text, size="small", color=bio.P.muted())


# Panel A: three-line system
bio.panel(ax, "A", (0.2, 11.3))
bio.label(ax, (7.2, 10.8), "Three-line system", size="title")
A, B, R, F1 = (2.8, 6.6), (2.8, 9.3), (10.8, 6.6), (7.0, 2.0)
line_box(B, "Maintainer (B line)", "N(rf rf)  fertile", "positive")
line_box(A, "CMS line (A line)", "S(rf rf)  male sterile", "negative")
line_box(R, "Restorer (R line)", "N(Rf Rf) or S(Rf Rf)", "positive")
line_box(F1, "F1 hybrid", "S(Rf rf)  fertile", "highlight")
cross((B[0], B[1] - H / 2), (A[0], A[1] + H / 2))
bio.label(ax, (B[0] + 0.25, (A[1] + B[1]) / 2), "pollen: A line propagated", size="small", ha="left", color=bio.P.muted())
cross((R[0] - W / 2, R[1]), (A[0] + W / 2, A[1]), "pollen")
cross((A[0] + 0.8, A[1] - H / 2), (F1[0] - 1.0, F1[1] + H / 2), kind="process")
cross((R[0] - 0.8, R[1] - H / 2), (F1[0] + 1.0, F1[1] + H / 2), kind="process")
bio.label(ax, (F1[0], 0.45), "hybrid seed for the field (new every season)", size="small", color=bio.P.muted())
for c in (B, R):
    bio.arrow(ax, (c[0] + W / 2, c[1] + 0.3), (c[0] + W / 2, c[1] - 0.3), bend=-1.2, kind="process")
    bio.label(ax, (c[0] + W / 2 + 0.95, c[1]), "self", size="small", color=bio.P.muted())

# Panel B: two-line system
bio.panel(ax, "B", (15.0, 11.3))
bio.label(ax, (19.6, 10.8), "Two-line system", size="title")
G1, G2, R2, F2 = (17.4, 9.3), (17.4, 6.6), (22.4, 6.6), (19.6, 2.0)
bio.box(ax, G1, W, H, token="positive")
bio.label(ax, (G1[0], G1[1] + 0.38), "PTGMS line", size="normal", bold=True, color=bio.P.on_fill())
bio.label(ax, (G1[0], G1[1] - 0.42), "short day / cool: fertile", size="small", color=bio.P.on_fill())
bio.box(ax, G2, W, H, token="negative")
bio.label(ax, (G2[0], G2[1] + 0.38), "PTGMS line", size="normal", bold=True, color=bio.P.on_fill())
bio.label(ax, (G2[0], G2[1] - 0.42), "long day / hot: sterile", size="small", color=bio.P.on_fill())
bio.box(ax, R2, 3.0, H, token="positive")
bio.label(ax, (R2[0], R2[1] + 0.38), "Pollen parent", size="normal", bold=True, color=bio.P.on_fill())
bio.label(ax, (R2[0], R2[1] - 0.42), "any fertile line", size="small", color=bio.P.on_fill())
bio.box(ax, F2, W, H, token="highlight")
bio.label(ax, (F2[0], F2[1] + 0.38), "F1 hybrid", size="normal", bold=True, color=bio.P.on_fill())
bio.label(ax, (F2[0], F2[1] - 0.42), "fertile", size="small", color=bio.P.on_fill())
bio.arrow(ax, (G1[0] + W / 2, G1[1] + 0.3), (G1[0] + W / 2, G1[1] - 0.3), bend=-1.2, kind="process")
bio.label(ax, (G1[0] + W / 2 + 0.95, G1[1]), "self", size="small", color=bio.P.muted())
bio.arrow(ax, (G1[0], G1[1] - H / 2), (G2[0], G2[1] + H / 2), dashed=True)
bio.label(ax, (G1[0] + 0.25, (G1[1] + G2[1]) / 2), "same line, other season or site", size="small", ha="left", color=bio.P.muted())
cross((R2[0] - 1.5, R2[1]), (G2[0] + W / 2, G2[1]))
bio.arrow(ax, (G2[0] + 0.8, G2[1] - H / 2), (F2[0] - 1.0, F2[1] + H / 2))
bio.arrow(ax, (R2[0] - 0.4, R2[1] - H / 2), (F2[0] + 1.0, F2[1] + H / 2))
