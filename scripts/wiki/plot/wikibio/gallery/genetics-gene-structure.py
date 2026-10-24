# The human beta-globin gene (HBB): promoter, three exons, two introns, and the spliced mRNA
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(15.0, 6.0)
exons = [(0, 142), (272, 495), (1345, 1606)]  # bp from the transcription start site
cds = (50, 1474)
sc = 0.0064
g = G.gene(ax, 1.6, 4.2, exons, cds=cds, scale=sc, promoter=(-110, -20), codons=("ATG", "TAA"), polya_signal=1586,
           name="HBB", flank=180, scale_bar=200, intron="hat")
X = g["x"]
for k, ((a, b), t) in enumerate(zip(zip(exons, exons[1:]), ("Intron 1", "Intron 2"))):
    bio.label(ax, ((X(a[1]) + X(b[0])) / 2, 4.2 + 0.62), t, size="small", va="bottom")

m = G.transcript(ax, 4.4, 1.5, exons, cds=cds, scale=sc)
for (ga, gb), (ma, mb) in zip(g["exons"], m):
    for gx, mx in ((ga, ma), (gb, mb)):
        ax.plot([gx, mx], [4.2 - 0.26, 1.5 + 0.22], color=bio.P.muted(), lw=0.6, ls=(0, (2.5, 2)))
bio.label(ax, (3.25, 2.85), "Splicing", size="small", color=bio.P.muted(), ha="right")
bio.label(ax, (0.3, 5.6), "Gene", size="normal", bold=True, ha="left")
bio.label(ax, (0.3, 1.5), "mRNA", size="normal", bold=True, ha="left")
