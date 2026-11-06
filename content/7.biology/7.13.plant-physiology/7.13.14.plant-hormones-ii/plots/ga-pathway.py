# Gibberellin biosynthesis and inactivation in three compartments (simplified).
# Plastid: IPP -> GGPP -> ent-CPP (CPS) -> ent-kaurene (KS); ER: KO, KAO -> GA12, GA13ox -> GA53;
# cytosol: GA20ox, GA3ox -> bioactive GA4 / GA1; GA2ox -> inactive GA34 / GA8.
# Orange tags: growth retardants and their target steps; red italics: classic dwarf mutants.
import wikibio as bio
from matplotlib.patches import FancyBboxPatch
from wikibio import metabolism as M

fig, ax = bio.canvas(23, 11)
P = bio.P
for (x, w, tok, name) in ((0.3, 5.4, "chloroplast", "Plastid"), (6.0, 5.6, "er", "Endoplasmic reticulum"),
                          (11.9, 10.8, "cytoplasm", "Cytosol")):
    fc = P.mix(P.edge(tok), P.surface(), 0.78) if P.is_dark() else P.light(tok)
    ax.add_patch(FancyBboxPatch((x, 0.2), w, 10.2, boxstyle="round,pad=0,rounding_size=0.4", facecolor=fc,
                                edgecolor=P.edge(tok), lw=1.1, zorder=1))
    bio.label(ax, (x + 0.3, 10.0), name, size="small", bold=True, ha="left")

pw = M.Pathway(ax, size="small")
pw.node("ipp", (3.0, 8.7), "IPP (C5)")
pw.node("ggpp", (3.0, 6.7), "GGPP (C20)")
pw.node("cpp", (3.0, 4.7), "ent-CPP")
pw.node("kau", (3.0, 2.4), "ent-Kaurene")
pw.node("kaa", (8.8, 2.4), "ent-Kaurenoic acid")
pw.node("ga12", (8.8, 5.3), "GA₁₂", bold=True)
pw.node("ga53", (8.8, 8.3), "GA₅₃")
pw.node("ga9", (14.6, 6.4), "GA₉")
pw.node("ga4", (14.6, 4.0), "GA₄ (active)", bold=True, token="positive")
pw.node("ga34", (14.6, 1.6), "GA₃₄ (inactive)", token="neutral")
pw.node("ga20", (19.6, 6.4), "GA₂₀")
pw.node("ga1", (19.6, 4.0), "GA₁ (active)", bold=True, token="positive")
pw.node("ga8", (19.6, 1.6), "GA₈ (inactive)", token="neutral")

pw.step("ipp", "ggpp", enzyme="×4", enzyme_size="tiny")
pw.step("ggpp", "cpp", enzyme="CPS", enzyme_size="small")
pw.step("cpp", "kau", enzyme="KS", enzyme_size="small")
pw.step("kau", "kaa", enzyme="KO (P450)", enzyme_size="small")
pw.step("kaa", "ga12", enzyme="KAO (P450)", enzyme_size="small", enzyme_flip=True)
pw.step("ga12", "ga53", enzyme="GA13ox", enzyme_size="small", enzyme_flip=True)
pw.step("ga12", "ga9", enzyme="GA20ox", enzyme_size="small")
pw.step("ga53", "ga20", enzyme="GA20ox", enzyme_size="small")
pw.step("ga9", "ga4", enzyme="GA3ox", enzyme_size="small", enzyme_flip=True)
pw.step("ga20", "ga1", enzyme="GA3ox", enzyme_size="small", enzyme_flip=True)
pw.step("ga4", "ga34", enzyme="GA2ox", enzyme_size="small", enzyme_flip=True)
pw.step("ga1", "ga8", enzyme="GA2ox", enzyme_size="small", enzyme_flip=True)
bio.label(ax, (19.6, 9.3), "13-OH pathway", size="tiny", color=P.muted())
bio.label(ax, (14.6, 9.3), "non-13-OH pathway", size="tiny", color=P.muted())


def tag(xy, text):
    bio.box(ax, xy, 0.25 + 0.13 * len(text), 0.5, token="highlight", text=text, size="tiny", radius=0.12, zorder=14)


tag((4.55, 5.75), "CCC, Pix")
tag((5.4, 3.1), "paclobutrazol")
tag((17.1, 5.2), "prohexadione-Ca")
neg = P.edge("negative")
bio.label(ax, (4.55, 5.2), "ga1", size="tiny", italic=True, color=neg)
bio.label(ax, (10.6, 3.9), "na", size="tiny", italic=True, color=neg)
bio.label(ax, (21.4, 5.2), "le, d1", size="tiny", italic=True, color=neg)
bio.label(ax, (21.0, 7.4), "sd1 (GA20ox2)", size="tiny", italic=True, color=neg)
