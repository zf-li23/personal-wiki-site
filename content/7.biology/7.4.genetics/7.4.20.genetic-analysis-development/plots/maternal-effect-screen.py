"""A screen for recessive maternal-effect mutations. Homozygous females from a balanced line are crossed to
wild-type males; their embryos all carry a wild-type paternal allele, so a defect in them reflects the
products the mother deposited in the egg. The reciprocal cross is the control."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(16.0, 9.6)


def geno(x, y, text, token, note=None, sex=None, w=2.5):
    bio.box(ax, (x, y), w, 0.85, token=token, text=text, size="normal")
    if note:
        bio.label(ax, (x, y - 0.75), note, size="small", color=P.muted(), va="top")
    if sex:
        bio.label(ax, (x, y + 0.75), sex, size="small")


bio.label(ax, (0.5, 9.2), "Experimental cross", size="title", ha="left", bold=True)
geno(3.0, 8.0, "$*/*$ female", "receptor", "homozygous mother\nfrom the balanced line")
bio.label(ax, (6.2, 8.0), "×", size="title")
geno(9.4, 8.0, "$+/+$ male", "dna", "wild type")
bio.arrow(ax, (6.2, 7.5), (6.2, 6.5), kind="process")
geno(6.2, 6.0, "$*/+$ embryos", "neutral", "every embryo has a wild-type\nallele from its father")
bio.label(ax, (12.0, 6.0), "defective:\nmaternal effect", size="normal", bold=True, color=P.edge("negative"))
bio.arrow(ax, (7.6, 6.0), (10.3, 6.0), kind="process")

bio.label(ax, (0.5, 4.2), "Reciprocal cross (control)", size="title", ha="left", bold=True)
geno(3.0, 3.0, "$*/+$ female", "neutral", "heterozygous mother")
bio.label(ax, (6.2, 3.0), "×", size="title")
geno(9.4, 3.0, "$*/*$ male", "receptor", "homozygous father")
bio.arrow(ax, (6.2, 2.5), (6.2, 1.5), kind="process")
geno(6.2, 1.0, "$*/*$ and $*/+$ embryos", "neutral", "same genotypes as above", w=3.9)
bio.label(ax, (12.0, 1.0), "normal:\nthe mother supplied\nthe product", size="normal", bold=True,
          color=P.edge("positive"))
bio.arrow(ax, (8.3, 1.0), (10.0, 1.0), kind="process")
