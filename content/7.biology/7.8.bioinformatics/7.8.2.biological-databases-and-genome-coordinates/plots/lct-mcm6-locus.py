# The LCT-MCM6 locus on chromosome 2 (GRCh38) as genome-browser tracks. Both genes are on the minus strand.
# Gene extents are approximate (LCT about 135.788-135.837 Mb, MCM6 about 135.840-135.876 Mb) and exon
# positions are schematic (17 exons each); the position of rs4988235 (135,851,076) is that of dbSNP. It lies in an
# intron of MCM6, about 13.9 kb upstream of the LCT transcription start, inside the enhancer that keeps LCT
# expressed in adult intestine.
import numpy as np
import wikibio as bio
from wikibio import sequence as S

P = bio.P
fig, ax = bio.canvas(30.0, 8.6)
gb = S.Browser(ax, (135_780_000, 135_882_000), 4.0, 29.0, chrom="chr2")
gb.axis(7.3, step=20_000)
lct = (135_787_840, 135_837_184)
mcm = (135_839_626, 135_876_443)


def exons(a, b, n, w, cuts=None):
    xs = np.linspace(b - w, a, n) if cuts is None else cuts
    return [(int(x), int(x + w)) for x in xs]


lct_ex = exons(*lct, 17, 260)
# MCM6 exons 1-17 counted from the 5' end (right); the variant falls between exons 13 and 14 (intron 13)
m_right = np.linspace(mcm[1] - 300, 135_853_000, 13)
m_left = np.linspace(135_848_500, mcm[0], 4)
mcm_ex = [(int(x), int(x + 300)) for x in np.r_[m_right, m_left]]
gb.gene(5.3, mcm_ex, strand="-", name="MCM6")
gb.gene(5.3, lct_ex, strand="-", name="LCT", token="enzyme")
gb.track_label(5.3, "genes (minus strand)")
v = 135_851_076
xv = gb.x(v)
gb.highlight(v - 1200, v + 1200, 1.0, 6.6)
ax.plot([xv, xv], [2.6, 4.9], color=P.edge("negative"), lw=1.4, zorder=12)
bio.label(ax, (xv, 2.25), "rs4988235  chr2:135,851,076 G>A  (LCT -13910C>T)", size="small", color=P.edge("negative"))
gb.track_label(2.6, "variant")
x_tss = gb.x(lct[1])
ax.annotate("", xy=(x_tss, 3.4), xytext=(xv, 3.4), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
bio.label(ax, ((x_tss + xv) / 2, 3.75), "about 13.9 kb", size="tiny")
bio.label(ax, (gb.x(135_851_076) + 0.25, 5.9), "MCM6 intron 13", size="tiny", ha="left", color=P.muted())
bio.label(ax, (4.0, 0.6), "exon positions schematic; transcription runs right to left", size="tiny", ha="left",
          color=P.muted())
