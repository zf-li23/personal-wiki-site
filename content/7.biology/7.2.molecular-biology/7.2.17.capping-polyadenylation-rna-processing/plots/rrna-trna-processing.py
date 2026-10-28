# Processing of ribosomal and transfer RNA precursors (lengths approximately to scale within each panel).
# A: the human 47S/45S pre-rRNA made by Pol I (about 13.3 kb): 5' external transcribed spacer (ETS), 18S,
# internal transcribed spacer 1 (ITS1), 5.8S, ITS2, 28S and 3' ETS. The main pathway removes the ETSs (41S),
# cuts in ITS1 to give the 21S/18S-E precursor of 18S and the 32S precursor of 5.8S + 28S, then cuts in ITS2;
# 5.8S stays base-paired to 28S. snoRNPs (U3 and others) guide cleavage and modification.
# B: an E. coli rrn operon transcript (about 5.5 kb, made by the single bacterial RNA polymerase): 16S, a
# spacer tRNA, 23S and 5S; RNase III cuts in the long stems that enclose 16S and 23S, RNase P makes the 5'
# end of the tRNA, RNase E acts near 5S; the mature ends are trimmed further.
# C: maturation of a eukaryotic pre-tRNA: RNase P removes the 5' leader, RNase Z the 3' trailer, the
# CCA-adding enzyme adds CCA without a template, the intron (if present) is removed by the splicing
# endonuclease and ligase, and many bases are modified.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 10.6)
H = 0.5


def seg(x0, x1, yy, token, text=None, h=H):
    bio.box(ax, ((x0 + x1) / 2, yy), x1 - x0, h, token=token, text=text, size="tiny", radius=0.04, zorder=6)


def spacer(x0, x1, yy):
    ax.plot([x0, x1], [yy, yy], color=P.muted(), lw=1.6, zorder=4)


def cut(x, yy, text=None):
    ax.plot([x, x], [yy - 0.45, yy + 0.45], color=P.edge("negative"), lw=1.1, ls=(0, (2, 1.4)), zorder=8)
    if text:
        bio.label(ax, (x, yy + 0.65), text, size="tiny", color=P.edge("negative"))


# --- A: human pre-rRNA ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.85))
s = 1.0  # canvas units per kb
x0 = 1.0
parts = [("ETS", 3.6, None), ("18S", 1.9, "rrna"), ("ITS1", 1.1, None), ("5.8S", 0.16, "rrna"), ("ITS2", 1.2, None),
         ("28S", 5.0, "rrna"), ("ETS", 0.35, None)]
y = 9.7
xs = [x0]
for name, L, tok in parts:
    a, b = xs[-1], xs[-1] + L * s
    if tok:
        seg(a, b, y, tok, name if name != "5.8S" else None)
    else:
        spacer(a, b, y)
        bio.label(ax, ((a + b) / 2, y + 0.32), ("5′ " if a == x0 else "3′ " if name == "ETS" else "") + name, size="tiny",
                  color=P.muted())
    xs.append(b)
bio.label(ax, (xs[4] + 0.08, y + 0.5), "5.8S", size="tiny")
bio.label(ax, (xs[-1] + 0.25, y), "47S/45S (13.3 kb, Pol I)", size="small", bold=True, ha="left")
# 41S
y2 = 8.1
seg(xs[1], xs[2], y2, "rrna", "18S"); spacer(xs[2], xs[3], y2); seg(xs[3], xs[4], y2, "rrna")
spacer(xs[4], xs[5], y2); seg(xs[5], xs[6], y2, "rrna", "28S")
cut(xs[2] + 0.5, y2, "site 2")
bio.label(ax, (xs[-1] + 0.25, y2), "41S: both ETSs removed", size="small", ha="left")
# split
y3 = 6.5
seg(xs[1], xs[2], y3, "rrna", "18S"); spacer(xs[2], xs[2] + 0.5, y3)
bio.label(ax, (xs[1] - 0.3, y3), "21S → 18S-E", size="tiny", ha="right")
spacer(xs[2] + 1.0, xs[3], y3); seg(xs[3], xs[4], y3, "rrna"); spacer(xs[4], xs[5], y3); seg(xs[5], xs[6], y3, "rrna", "28S")
cut(xs[4] + 0.6, y3, "ITS2 cuts")
bio.label(ax, (xs[-1] + 0.25, y3), "32S (5.8S + ITS2 + 28S)", size="small", ha="left")
for yy in (y - 0.4, y2 - 0.4):
    bio.arrow(ax, (xs[0] + 0.4 + 5.0, yy), (xs[0] + 0.4 + 5.0, yy - 0.75), kind="process")
# mature
y4 = 5.1
seg(xs[1], xs[2], y4, "rrna", "18S")
seg(xs[5], xs[6], y4, "rrna", "28S")
seg(xs[5] + 0.1, xs[5] + 0.42, y4 + 0.45, "rrna", h=0.3)
bio.label(ax, (xs[5] + 0.55, y4 + 0.5), "5.8S, base-paired to 28S", size="tiny", ha="left")
bio.label(ax, (xs[-1] + 0.25, y4), "mature rRNAs (+ 5S from Pol III)", size="small", ha="left")
bio.arrow(ax, (xs[0] + 5.4, y3 - 0.4), (xs[0] + 5.4, y4 + 0.4), kind="process")

# --- B: E. coli operon ----------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 3.85))
y = 2.6
xb = [1.0]
bparts = [("lead", 0.6, None), ("16S", 3.1, "rrna"), ("sp", 0.4, None), ("tRNA", 0.3, "trna"), ("sp", 0.5, None),
          ("23S", 5.8, "rrna"), ("sp", 0.3, None), ("5S", 0.24, "rrna"), ("trail", 0.4, None)]
for name, L, tok in bparts:
    a, b = xb[-1], xb[-1] + L * 0.9
    if tok:
        seg(a, b, y, tok, name if name not in ("5S", "tRNA") else None)
    else:
        spacer(a, b, y)
    xb.append(b)
bio.label(ax, ((xb[3] + xb[4]) / 2, y - 0.55), "tRNA", size="tiny")
bio.label(ax, ((xb[7] + xb[8]) / 2, y - 0.55), "5S", size="tiny")
for k, t in ((1, "III"), (2, "III"), (5, "III"), (6, "III")):
    cut(xb[k] + (-0.12 if k in (1, 5) else 0.12), y, t if k != 6 else None)
    if k == 6:
        bio.label(ax, (xb[k] - 0.15, y + 0.65), t, size="tiny", color=P.edge("negative"))
cut(xb[3], y, "P")
ax.plot([xb[7] - 0.06] * 2, [y - 0.45, y + 0.45], color=P.edge("negative"), lw=1.1, ls=(0, (2, 1.4)), zorder=8)
bio.label(ax, (xb[7] + 0.1, y + 0.95), "E", size="tiny", color=P.edge("negative"))
bio.label(ax, (xb[-1] + 0.25, y), r"$\it{E.\ coli\ rrn}$ transcript (≈ 5.5 kb)", size="small", bold=True, ha="left")
bio.label(ax, (1.0, y - 1.3), "III = RNase III, P = RNase P, E = RNase E; one RNA polymerase makes all bacterial RNAs",
          size="tiny", color=P.muted(), ha="left")

# --- C: tRNA ----------------------------------------------------------------------------------------------------
bio.panel(ax, "C", (17.6, 3.85))
y = 2.6
xc = 17.9
spacer(xc, xc + 0.8, y)
seg(xc + 0.8, xc + 2.3, y, "trna", "tRNA")
bio.box(ax, (xc + 2.5, y), 0.4, H, token="neutral", text="i", size="tiny", radius=0.04, zorder=6)
seg(xc + 2.7, xc + 4.2, y, "trna", "tRNA")
spacer(xc + 4.2, xc + 5.0, y)
cut(xc + 0.8, y, "RNase P")
cut(xc + 4.2, y, "RNase Z")
bio.label(ax, (xc + 0.4, y - 0.5), "5′ leader", size="tiny", color=P.muted())
bio.label(ax, (xc + 4.6, y - 0.5), "3′ trailer", size="tiny", color=P.muted())
bio.label(ax, (xc + 2.5, y - 0.55), "intron", size="tiny", color=P.muted())
bio.label(ax, (xc + 2.5, y - 1.3), "then: + CCA (no template), intron spliced, bases modified", size="tiny",
          color=P.muted())
