"""Waves and sites of hematopoiesis and the switching of globin genes. A: in the mouse, a primitive wave in the yolk
sac blood islands (E7.25) makes nucleated primitive erythrocytes, macrophages and megakaryocytes; a second,
transient wave of erythro-myeloid progenitors (EMPs) arises from hemogenic endothelium of the yolk sac (E8.25)
and seeds the fetal liver and tissue-resident macrophages; definitive hematopoietic stem cells emerge from the
hemogenic endothelium of the dorsal aorta in the AGM region, the umbilical and vitelline arteries and the placenta
(E10.5-11.5), expand in the fetal liver and colonize the bone marrow shortly before birth. B: human beta-like
globin chains (percentage of the total, schematic): embryonic epsilon in the yolk-sac period, fetal gamma from
the liver period, adult beta (with a little delta) from the third trimester, the gamma-to-beta switch completing
in the first year. C: alpha-like chains: embryonic zeta replaced by alpha by about 6 weeks."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(10.4, 5.6))
gs = fig.add_gridspec(2, 2, width_ratios=[1.2, 1], hspace=0.55, wspace=0.28, left=0.08, right=0.98, bottom=0.1, top=0.92)
a = fig.add_subplot(gs[:, 0])
rows = [("primitive erythroid (yolk sac)", 7.25, 12.5, "blood"), ("EMP (yolk sac)", 8.25, 11.5, "drug"), ("HSC emergence (AGM, arteries)", 10.25, 12.0, "protein"),
        ("placenta", 10.5, 13.5, "receptor"), ("fetal liver", 11.5, 19.5, "enzyme"), ("spleen", 15.0, 19.5, "k"), ("bone marrow", 17.5, 19.5, "bone")]
for k, (txt, t0, t1, tk) in enumerate(rows):
    y = len(rows) - k
    a.barh(y, t1 - t0, left=t0, height=0.55, color=charts.line(tk))
    a.text(6.8, y, txt, ha="right", va="center", fontsize=FT["tiny"], color=P_.ink())
a.axvline(19.5, color=P_.muted(), lw=0.8, ls="--")
a.text(19.4, 7.7, "birth", ha="right", fontsize=FT["tiny"], color=P_.muted())
a.set_xlim(2.5, 20)
a.set_yticks([])
a.set_xticks([8, 10, 12, 14, 16, 18])
charts.style_axes(a, "mouse embryonic day", None)
charts.title(a, "A  Waves and sites (mouse)")


def sig(t, t0, w):
    return 1 / (1 + np.exp(-(t - t0) / w))


t = np.linspace(0, 70, 400)  # weeks after conception; birth at 38
eps = 100 * (1 - sig(t, 7, 1.2))
gam = (100 - eps) * (1 - sig(t, 44, 4)) * 1.0
beta = 100 - eps - gam
delta = 0.025 * beta
beta = beta - delta
b = fig.add_subplot(gs[0, 1])
for y, tk, txt in ((eps, "drug", "epsilon"), (gam, "enzyme", "gamma (HbF)"), (beta, "blood", "beta (HbA)"), (delta, "k", "delta")):
    b.plot(t, y, color=charts.line(tk), lw=1.7, label=txt)
b.axvline(38, color=P_.muted(), lw=0.8, ls="--")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right", ncol=1)
charts.style_axes(b, None, "% of beta-like chains")
charts.title(b, "B  beta-globin locus (human)")
c = fig.add_subplot(gs[1, 1])
zeta = 100 * (1 - sig(t, 5.5, 0.8))
c.plot(t, zeta, color=charts.line("drug"), lw=1.7, label="zeta")
c.plot(t, 100 - zeta, color=charts.line("blood"), lw=1.7, label="alpha")
c.axvline(38, color=P_.muted(), lw=0.8, ls="--")
c.text(37.5, 50, "birth", ha="right", fontsize=FT["tiny"], color=P_.muted())
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(c, "weeks after conception", "% of alpha-like")
charts.title(c, "C  alpha-globin locus")
