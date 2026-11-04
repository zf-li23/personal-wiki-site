"""Habitats of the human microbiome: cell density along the digestive tract and the dominant taxa of the
main body sites. Densities and dominant groups from Madigan et al. (2019) and Sender et al. (2016)."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26, 11)

# ---------------- A: density along the tract
bio.panel(ax, "A", (0.2, 10.8))
segments = [("mouth, saliva", 1e9, "receptor"), ("stomach (pH 1-2)", 1e3, "lysosome"),
            ("duodenum", 1e3, "carbohydrate"), ("jejunum, ileum", 1e7, "enzyme"),
            ("colon", 1e11, "bacterium")]
p = quant.Plot(ax, (3.6, 1.8, 7.6, 7.6), xlim=(1, 1e12), ylim=(0, 5), xlog=True,
               xlabel="cells per gram of contents",
               xticks=[(1, "1"), (1e3, "10³"), (1e6, "10⁶"), (1e9, "10⁹"), (1e12, "10¹²")],
               yticks=[], frame="l")
for k, (name, n, tok) in enumerate(segments):
    yy = 4.5 - k
    x1 = p.X(n)
    bio.shape(ax, [(p.X(1), p.Y(yy - 0.3)), (x1, p.Y(yy - 0.3)), (x1, p.Y(yy + 0.3)), (p.X(1), p.Y(yy + 0.3))],
              token=tok, lw=0.8)
    bio.label(ax, (p.X(1) - 0.2, p.Y(yy)), name, size="small", ha="right")
bio.label(ax, (7.4, 0.7), "about 3.8 × 10¹³ bacteria in all, almost all in the colon",
          size="tiny", color=P.muted())

# ---------------- B: dominant taxa by site
bio.panel(ax, "B", (13.8, 10.8))
sites = [
    ("skin (sebaceous)", [("Cutibacterium", 0.55, "enzyme"), ("Staphylococcus", 0.2, "receptor"),
                          ("Corynebacterium", 0.12, "metabolite"), ("other", 0.13, "neutral")]),
    ("mouth (plaque)", [("Streptococcus", 0.3, "receptor"), ("Actinomyces", 0.18, "enzyme"),
                        ("Fusobacterium", 0.14, "virus"), ("Veillonella", 0.12, "carbohydrate"),
                        ("other", 0.26, "neutral")]),
    ("stomach", [("Helicobacter", 0.5, "negative"), ("Streptococcus", 0.2, "receptor"),
                 ("Prevotella", 0.15, "metabolite"), ("other", 0.15, "neutral")]),
    ("colon", [("Bacillota", 0.5, "bacterium"), ("Bacteroidota", 0.35, "metabolite"),
               ("Actinomycetota", 0.07, "enzyme"), ("other", 0.08, "neutral")]),
    ("vagina", [("Lactobacillus", 0.8, "positive"), ("anaerobes", 0.12, "virus"), ("other", 0.08, "neutral")]),
]
x0, w = 15.4, 7.6
yb = 9.3
for name, comp in sites:
    bio.label(ax, (x0, yb + 0.42), name, size="small", ha="left")
    cx = x0
    for taxon, frac, tok in comp:
        bio.shape(ax, [(cx, yb - 0.3), (cx + w * frac, yb - 0.3), (cx + w * frac, yb + 0.25), (cx, yb + 0.25)],
                  token=tok, lw=0.8)
        if frac * w > 0.082 * len(taxon) + 0.2:
            bio.label(ax, (cx + w * frac / 2, yb - 0.03), taxon, size="tiny", color=P.on_fill(),
                      italic=taxon[0].isupper() and taxon not in ("Bacillota", "Bacteroidota", "Actinomycetota"))
        cx += w * frac
    yb -= 1.85
bio.label(ax, (x0, 0.6), "relative abundance, typical values; variation between people is large",
          size="tiny", ha="left", color=P.muted())
