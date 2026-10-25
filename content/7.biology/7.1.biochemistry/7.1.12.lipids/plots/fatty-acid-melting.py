"""Melting points of fatty acids. A: saturated fatty acids against chain length (12:0 lauric to 24:0
lignoceric); each two carbons add about 6-10 deg C. B: C18 fatty acids against the number of cis double
bonds (stearic 18:0, oleic 18:1(D9), linoleic 18:2(D9,12), alpha-linolenic 18:3(D9,12,15)), with the trans
isomer of oleic acid (elaidic acid, the main trans fatty acid of partially hydrogenated oils) for
comparison; arachidonic acid 20:4 is added. Values: Lehninger, Principles of Biochemistry, 8th ed.,
Table 10-1 (linoleic acid given there as 1 to 5 deg C, drawn as a range); elaidic acid 45 deg C."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(19.0, 7.6)

bio.panel(ax, "A", (0.1, 7.5))
pa = charts.axes_at(ax, (1.6, 1.4, 6.6, 5.6))
sat = [(12, 44.2, "lauric"), (14, 53.9, "myristic"), (16, 63.1, "palmitic"), (18, 69.6, "stearic"), (20, 76.5, "arachidic"),
       (24, 86.0, "lignoceric")]
n = np.array([s[0] for s in sat])
mp = np.array([s[1] for s in sat])
pa.plot(n, mp, "-o", color=charts.line("lipid"), mfc=P.fill("lipid"), mec=charts.line("lipid"), ms=5, lw=1.6)
for c, m, name in sat:
    pa.text(c + 0.3, m - 3.2, f"{c}:0 {name}", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.axhline(37, color=P.muted(), lw=0.8, ls=(0, (4, 3)))
pa.text(12.2, 38.5, "body temperature", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(11, 26.5)
pa.set_ylim(30, 95)
pa.set_xticks([12, 14, 16, 18, 20, 22, 24])
charts.style_axes(pa, "number of carbon atoms (saturated)", "melting point / °C")

bio.panel(ax, "B", (9.6, 7.5))
pb = charts.axes_at(ax, (11.2, 1.4, 6.6, 5.6))
c18 = [(0, 69.6, "18:0 stearic"), (1, 13.4, "18:1 oleic"), (2, 3.0, "18:2 linoleic"), (3, -11.0, "18:3 α-linolenic")]
k = np.array([c[0] for c in c18])
m = np.array([c[1] for c in c18])
pb.plot(k, m, "-o", color=charts.line("lipid_head"), mfc=P.fill("lipid_head"), mec=charts.line("lipid_head"), ms=5, lw=1.6)
pb.errorbar([2], [3.0], yerr=[[2.0], [2.0]], fmt="none", ecolor=charts.line("lipid_head"), elinewidth=1.0, capsize=3)
for kk, mm, name in c18:
    pb.text(kk + 0.12, mm + 3.0, name, fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.plot([1], [45.0], "s", ms=6, mfc=P.fill("negative"), mec=charts.line("negative"))
pb.text(1.12, 48.0, "18:1 trans (elaidic)", fontsize=bio.core.FONT["tiny"], color=charts.line("negative"))
pb.plot([4], [-49.5], "o", ms=5, mfc=P.fill("drug"), mec=charts.line("drug"))
pb.text(3.4, -42.0, "20:4 arachidonic", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.axhline(37, color=P.muted(), lw=0.8, ls=(0, (4, 3)))
pb.axhline(0, color=P.muted(), lw=0.6)
pb.set_xlim(-0.4, 4.6)
pb.set_ylim(-60, 85)
pb.set_xticks([0, 1, 2, 3, 4])
charts.style_axes(pb, "number of cis double bonds", "melting point / °C")
