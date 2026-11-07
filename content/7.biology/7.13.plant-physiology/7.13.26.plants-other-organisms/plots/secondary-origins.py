# Biosynthetic origins of the three major classes of plant secondary (specialized) metabolites, simplified
# (after Taiz et al. 6e Fig. 23.9 and Buchanan et al. 2e Ch. 24). Primary metabolism (grey) feeds:
# terpenoids (yellow) from IPP/DMAPP made by the cytosolic mevalonate (MVA) pathway from acetyl-CoA and by the
# plastid methylerythritol phosphate (MEP) pathway from pyruvate + glyceraldehyde 3-phosphate;
# phenolics (orange) mainly from the shikimate pathway via phenylalanine and PAL (phenylpropanoids), with
# malonyl-CoA supplying the second ring of flavonoids; nitrogen-containing compounds (blue) from amino acids.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)


def node(xy, text, token, w=3.4, h=0.75, size="small"):
    bio.box(ax, xy, w, h, token=token, text=text, size=size)


def arr(a, b, **kw):
    bio.arrow(ax, a, b, kind="process", **kw)


# primary metabolism column
node((13.0, 12.2), "CO₂ (photosynthesis)", "neutral", w=4.2)
node((13.0, 10.8), "Sugars (glucose)", "neutral")
node((7.0, 9.2), "Erythrose 4-P + PEP", "neutral", w=4.0)
node((13.0, 9.2), "Pyruvate + GAP", "neutral", w=3.6)
node((19.0, 9.2), "Acetyl-CoA", "neutral", w=3.0)
node((16.9, 7.6), "Malonyl-CoA", "neutral", w=3.0)
node((23.6, 9.2), "TCA cycle", "neutral", w=2.6)
arr((13.0, 11.8), (13.0, 11.2))
arr((12.0, 10.4), (8.4, 9.6))
arr((13.0, 10.4), (13.0, 9.6))
arr((14.0, 10.4), (18.2, 9.6))
arr((14.8, 9.2), (17.5, 9.2))
arr((20.5, 9.2), (22.1, 9.2))
arr((18.4, 8.82), (17.4, 7.98))

# shikimate -> aromatic aa
node((7.0, 7.6), "Shikimate pathway", "drug", w=3.6)
arr((7.0, 8.82), (7.0, 7.98))
node((7.0, 6.0), "Phe   Tyr   Trp", "neutral", w=3.6)
arr((7.0, 7.22), (7.0, 6.38))
node((3.0, 4.4), "Phenylpropanoids (C6-C3)", "drug", w=4.6)
arr((6.0, 5.62), (3.9, 4.78))
bio.label(ax, (4.5, 5.45), "PAL", size="tiny", bold=True)
for i, t in enumerate(["lignin", "coumarins, simple phenolics", "tannins", "flavonoids (C6-C3-C6; + 3 malonyl-CoA):", "anthocyanins, isoflavonoids"]):
    bio.label(ax, (0.9, 3.5 - 0.5 * i), ("• " if i != 4 else "   ") + t, size="tiny", ha="left")

# MEP and MVA -> IPP
node((13.0, 7.6), "MEP pathway (plastid)", "highlight", w=4.0)
arr((13.0, 8.82), (13.0, 7.98))
node((21.7, 7.6), "MVA pathway (cytosol)", "highlight", w=4.2)
arr((19.6, 8.82), (20.9, 7.98))
node((17.6, 5.9), "IPP ⇌ DMAPP (C5)", "highlight", w=3.8)
arr((14.2, 7.22), (16.4, 6.28))
arr((21.2, 7.22), (18.8, 6.28))
for i, (t, x) in enumerate([("C10 monoterpenes", 13.2), ("C20 diterpenes, GA", 16.3), ("C40 carotenoids, ABA", 19.6),
                            ("C15 sesquiterpenes", 22.4)]):
    pass
node((14.0, 4.2), "GPP C10 → monoterpenes", "highlight", w=4.8, size="tiny")
node((14.0, 3.2), "GGPP C20 → diterpenes, GA", "highlight", w=4.8, size="tiny")
node((14.0, 2.2), "2 GGPP → C40 carotenoids, ABA", "highlight", w=4.8, size="tiny")
node((21.4, 4.2), "FPP C15 → sesquiterpenes", "highlight", w=4.8, size="tiny")
node((21.4, 3.2), "2 FPP → C30 triterpenes, sterols", "highlight", w=4.8, size="tiny")
node((21.4, 2.2), "cardenolides, saponins", "highlight", w=4.8, size="tiny")
arr((16.8, 5.52), (15.4, 4.6))
arr((18.4, 5.52), (19.9, 4.6))
bio.label(ax, (14.0, 1.35), "plastid (MEP)", size="tiny", color=P.muted())
bio.label(ax, (21.4, 1.35), "cytosol / ER (MVA)", size="tiny", color=P.muted())
bio.label(ax, (17.7, 0.6), "rubber: cis-1,4-polyisoprene (n > 1000)", size="tiny", color=P.muted())

# nitrogen compounds
node((7.0, 2.2), "Alkaloids", "channel", w=3.0)
node((10.0, 0.9), "Glucosinolates,\ncyanogenic glycosides", "channel", w=4.2, h=1.0, size="tiny")
arr((7.0, 5.62), (7.0, 2.58))
arr((8.0, 5.62), (9.6, 1.42))
node((24.6, 5.9), "Orn, Lys, Met …", "neutral", w=2.6, size="tiny")
arr((24.0, 8.82), (24.5, 6.28))
bio.label(ax, (24.6, 5.2), "→ alkaloids (nicotine),", size="tiny")
bio.label(ax, (24.6, 4.75), "glucosinolates", size="tiny")
bio.label(ax, (2.6, 12.3), "Terpenoids", size="small", bold=True, color=P.edge("highlight"))
bio.label(ax, (2.6, 11.7), "Phenolics", size="small", bold=True, color=P.edge("drug"))
bio.label(ax, (2.6, 11.1), "N-containing", size="small", bold=True, color=P.edge("channel"))
