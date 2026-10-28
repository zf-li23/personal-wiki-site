"""The insulator model of imprinting at the mouse H19/Igf2 locus (not to scale). The imprinting control
region (ICR) between the genes is unmethylated and bound by CTCF on the maternal chromosome, which keeps the
shared downstream enhancers on H19; on the paternal chromosome the ICR and the H19 promoter are methylated,
CTCF cannot bind and the enhancers reach Igf2."""
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(17.0, 9.6)
U = 0.6


def lollipops(x0, y, n, filled, dx=0.3, h=0.5):
    for k in range(n):
        x = x0 + k * dx
        ax.plot([x, x], [y, y + h], color=P.ink(), lw=0.9, zorder=13)
        ax.add_patch(Circle((x, y + h + 0.11), 0.11, facecolor=P.ink(), edgecolor=P.ink(), lw=0.9, zorder=14) if filled
                     else Circle((x, y + h + 0.11), 0.11, fill=False, edgecolor=P.ink(), lw=0.9, zorder=14))


def allele(y, maternal):
    tok = "receptor" if maternal else "dna"
    bio.label(ax, (0.4, y + 1.25), "Maternal chromosome" if maternal else "Paternal chromosome", size="normal",
              ha="left", bold=True, color=P.edge(tok))
    ax.plot([0.8, 15.6], [y, y], color=P.ink(), lw=bio.core.LINE * 1.5, zorder=11, solid_capstyle="round")
    igfp = G.glyph(ax, "promoter", 1.3, y, unit=U)
    igf = G.glyph(ax, "cds", igfp["x1"] + 0.15, y, unit=U, width=2.4, text="Igf2", italic=True,
                  token="positive" if not maternal else "neutral")
    icr = G.glyph(ax, "insulator", 6.4, y, unit=U, width=0.75)
    bio.label(ax, (icr["centre"], y - 0.55), "ICR", size="small")
    h19p = G.glyph(ax, "promoter", 9.0, y, unit=U)
    h19 = G.glyph(ax, "cds", h19p["x1"] + 0.15, y, unit=U, width=2.0, text="H19", italic=True,
                  token="positive" if maternal else "neutral")
    enh = G.glyph(ax, "region", 14.0, y, unit=U, width=0.8, text="E")
    bio.label(ax, (enh["centre"], y - 0.55), "enhancers", size="small", color=P.muted())
    if maternal:
        lollipops(icr["centre"] - 0.3, y + 0.32, 3, filled=False)
        bio.protein(ax, (icr["centre"], y - 1.25), 1.0, 0.55, "protein", text="CTCF")
        bio.arrow(ax, (enh["centre"], enh["top"] + 0.1), (h19p["x0"] + 0.05, y + 0.95), kind="activation", bend=-0.3)
        bio.arrow(ax, (h19p["x0"] - 0.3, y + 1.55), (icr["x1"] + 0.15, y + 1.55), kind="inhibition", dashed=True)
        bio.label(ax, (12.2, y + 2.05), r"enhancers activate $\it{H19}$", size="small")
        bio.label(ax, (icr["centre"] + 0.8, y + 2.05), "blocked at the insulator", size="small", color=P.muted())
        bio.label(ax, (igf["centre"], y - 0.7), "silent", size="small", color=P.muted())
        bio.label(ax, (h19["centre"], y - 0.7), "expressed", size="small", color=P.edge("positive"))
    else:
        lollipops(icr["centre"] - 0.3, y + 0.32, 3, filled=True)
        lollipops(h19p["x0"] - 0.55, y + 0.32, 2, filled=True)
        bio.arrow(ax, (enh["centre"], enh["top"] + 0.1), (igfp["x0"] + 0.2, y + 0.95), kind="activation", bend=-0.16)
        bio.label(ax, (9.6, y + 2.1), r"enhancers activate $\it{Igf2}$ over 90 kb", size="small")
        bio.label(ax, (icr["centre"], y - 1.05), "methylated: CTCF cannot bind", size="small", color=P.muted())
        bio.label(ax, (igf["centre"], y - 0.7), "expressed", size="small", color=P.edge("positive"))
        bio.label(ax, (h19["centre"], y - 0.7), "silent", size="small", color=P.muted())


allele(6.4, True)
allele(1.5, False)
kx, ky = 0.7, 4.05
ax.add_patch(Circle((kx, ky), 0.11, fill=False, edgecolor=P.ink(), lw=0.9, zorder=14))
bio.label(ax, (kx + 0.3, ky), "unmethylated CpG", size="small", ha="left")
ax.add_patch(Circle((kx + 3.6, ky), 0.11, facecolor=P.ink(), edgecolor=P.ink(), lw=0.9, zorder=14))
bio.label(ax, (kx + 3.9, ky), "methylated CpG", size="small", ha="left")
