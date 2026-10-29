# The maternal anterior-posterior system. Top: mRNAs in the unfertilized egg (bicoid at the anterior pole, nanos at
# the posterior pole, hunchback and caudal uniform). Middle: proteins in the syncytial blastoderm: Bicoid forms an
# anterior gradient and represses caudal translation; Nanos (with Pumilio and Brat) represses hunchback translation
# posteriorly, while Bicoid activates zygotic hunchback transcription anteriorly; the result is two opposing pairs of
# gradients. Bottom: schematic profiles along the egg (decay length of Bicoid about 20 % of egg length).
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import development as D

fig, ax = bio.canvas(22.0, 10.6)
ax.set_ylim(3.4, 14.0)
P = bio.P
X, L, H = 7.4, 9.0, 2.0
tok = {"bcd": "receptor", "nos": "metabolite", "hb": "channel", "cad": "positive"}

bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.9, 13.45), "mRNA (egg)", size="normal", bold=True, ha="left")
e = D.FlyEmbryo(ax, (X, 11.6), L, H)
e.gradients([(lambda f: np.exp(-f / 0.04), tok["bcd"]), (lambda f: np.exp(-(1 - f) / 0.035), tok["nos"])], floor=0.05)
bio.label(ax, (X, 10.05), "hunchback and caudal mRNAs: uniform", size="tiny", color=P.muted())

bio.panel(ax, "B", (0.2, 9.3))
bio.label(ax, (0.9, 8.95), "Protein (syncytial blastoderm)", size="normal", bold=True, ha="left")
f_bcd = lambda f: np.exp(-f / 0.2)
f_nos = lambda f: np.exp(-(1 - f) / 0.12)
f_hb = lambda f: 1 / (1 + np.exp((f - 0.48) / 0.025))
f_cad = lambda f: np.clip(1 - np.exp(-f / 0.25), 0, 1) ** 2
e1 = D.FlyEmbryo(ax, (X - 2.3, 7.2), L / 2, H * 0.75)
e1.gradients([(f_bcd, tok["bcd"])])
bio.label(ax, (X - 2.3, 8.25), "Bicoid", size="small", bold=True)
e2 = D.FlyEmbryo(ax, (X + 2.6, 7.2), L / 2, H * 0.75)
e2.gradients([(f_nos, tok["nos"])])
bio.label(ax, (X + 2.6, 8.25), "Nanos", size="small", bold=True)
e3 = D.FlyEmbryo(ax, (X - 2.3, 4.9), L / 2, H * 0.75)
e3.gradients([(f_hb, tok["hb"])])
bio.label(ax, (X - 2.3, 3.85), "Hunchback", size="small", bold=True)
e4 = D.FlyEmbryo(ax, (X + 2.6, 4.9), L / 2, H * 0.75)
e4.gradients([(f_cad, tok["cad"])])
bio.label(ax, (X + 2.6, 3.85), "Caudal", size="small", bold=True)
# regulatory arrows
bio.arrow(ax, (X - 2.3, 6.45), (X - 2.3, 5.75), kind="activation")
bio.label(ax, (X - 3.6, 6.1), "transcription", size="tiny", color=P.muted())
bio.arrow(ax, (X + 2.6, 6.45), (X - 1.0, 5.6), kind="inhibition")
bio.label(ax, (X + 0.9, 6.35), "translation", size="tiny", color=P.muted())
bio.arrow(ax, (X - 1.1, 6.6), (X + 2.2, 5.65), kind="inhibition", dashed=False)

# C: profiles
bio.panel(ax, "C", (15.0, 13.8))
pa = C.axes_at(ax, (16.3, 7.2, 5.2, 5.6))
f = np.linspace(0, 1, 300)
for name, fn in [("Bicoid", f_bcd), ("Nanos", f_nos), ("Hunchback", f_hb), ("Caudal", f_cad)]:
    k = {"Bicoid": "bcd", "Nanos": "nos", "Hunchback": "hb", "Caudal": "cad"}[name]
    pa.plot(f, fn(f), color=C.line(tok[k]), lw=1.8, label=name)
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
pa.set_xticks([0, 0.5, 1])
pa.set_yticks([0, 0.5, 1])
C.style_axes(pa, "x / L (anterior → posterior)", "relative level")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center right")
bio.label(ax, (18.9, 5.6), "Bicoid: TF (activates hb, head genes)\nand translational repressor of caudal\n"
          "Nanos + Pumilio + Brat: translational\nrepressor of maternal hunchback", size="tiny", color=P.muted())
