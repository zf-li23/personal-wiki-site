# Direct and indirect allorecognition. Donor-derived molecules are drawn in the "negative" color, recipient molecules in "protein".
# A direct: a recipient T cell recognizes intact donor MHC (with a donor or self peptide) on a donor antigen-presenting cell
#   that came with the graft; B indirect: recipient APCs take up donor proteins (including shed donor MHC), process them and
#   present donor peptides on recipient (self) MHC.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 8.5)


def cells(x0, top_label, bottom_label, bottom_token):
    bio.shape(ax, bio.blob((x0 + 5.0, 7.0), 4.4, 1.1, wobble=0.015, seed=3), "cytoplasm", zorder=3)
    bio.label(ax, (x0 + 5.0, 7.0), top_label, size="small")
    bio.shape(ax, bio.blob((x0 + 5.0, 1.3), 4.4, 1.1, wobble=0.015, seed=7), bottom_token, zorder=3)
    bio.label(ax, (x0 + 5.0, 1.3), bottom_label, size="small")


bio.panel(ax, "A", (0.1, 8.2))
cells(0, "recipient T cell", "donor APC (in the graft)", "negative")
bio.protein(ax, (3.0, 5.0), 1.2, 0.45, "receptor", text="TCR")
bio.protein(ax, (3.0, 3.0), 3.4, 0.5, "negative", text="donor MHC + peptide")
bio.arrow(ax, (3.0, 3.4), (3.0, 4.6), kind="activation")
bio.protein(ax, (7.0, 5.0), 1.2, 0.45, "enzyme", text="CD28")
bio.protein(ax, (7.0, 3.0), 1.2, 0.45, "carbohydrate", text="B7")
bio.arrow(ax, (7.0, 3.4), (7.0, 4.6), kind="activation")
bio.label(ax, (5.0, 4.0), "many T cells cross-react", size="tiny", color=P.muted())

bio.panel(ax, "B", (12.1, 8.2))
cells(12, "recipient T cell", "recipient APC", "protein")
bio.protein(ax, (15.0, 5.0), 1.2, 0.45, "receptor", text="TCR")
bio.protein(ax, (15.0, 3.0), 3.8, 0.5, "protein", text="self MHC + donor peptide")
bio.arrow(ax, (15.0, 3.4), (15.0, 4.6), kind="activation")
bio.protein(ax, (20.0, 3.0), 2.4, 0.5, "negative", text="donor protein")
bio.arrow(ax, (20.0, 3.4), (17.0, 2.3), kind="process", bend=0.3, dashed=True)
bio.label(ax, (19.2, 4.2), "uptake and\nprocessing", size="tiny", color=P.muted())
