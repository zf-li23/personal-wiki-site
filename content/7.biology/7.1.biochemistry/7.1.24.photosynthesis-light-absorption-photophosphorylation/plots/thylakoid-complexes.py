"""Linear electron flow and the proton circuit in the thylakoid membrane (stroma, N side, above; lumen, P side,
below). PSII oxidizes water at the Mn4CaO5 cluster on the lumenal side and reduces plastoquinone at the QB
site, taking protons from the stroma; the cytochrome b6f complex oxidizes plastoquinol at its lumenal site in
a Q cycle and reduces plastocyanin; PSI passes the electrons through ferredoxin to ferredoxin-NADP+ reductase
(FNR). Protons move per O2 evolved (4 electrons): 4 from water oxidation and 8 from plastoquinol oxidation
into the lumen; protons are taken up from the stroma at QB, at the Qn site of b6f and by FNR. CF0F1 ATP
synthase with a c14 ring returns 14 H+ per 3 ATP."""

import wikibio as bio
from wikibio import photosynthesis as ps
from wikibio.quant import line_color

P = bio.P
fig, ax = bio.canvas(28.0, 9.6)
EC, HC = line_color(ps.COLOR["electron"]), line_color(ps.COLOR["proton"])
y = 4.9
ps.thylakoid(ax, (0.4, 27.6), y, stroma=3.9, lumen=3.0, label_x=0.6)
a = ps.psii(ax, 4.4, y)
pq1 = ps.plastoquinone(ax, (6.75, y + 0.05), reduced=True)
b = ps.cytb6f(ax, 9.6, y)
pc = ps.plastocyanin(ax, (11.65, y - 1.55))
c = ps.psi(ax, 14.0, y)
fd = ps.ferredoxin(ax, (16.0, y + 1.85))
fn = ps.fnr(ax, 18.0, y)
d = ps.atp_synthase(ax, 23.6, y)

ps.photon(ax, (2.2, y + 3.6), (a["antenna"][0] - 0.1, a["antenna"][1] + 0.6), text="hν")
ps.photon(ax, (12.3, y + 3.6), (c["antenna"][0] - 0.05, c["antenna"][1] + 0.6), text="hν")

kw = dict(kind="process", color=EC, lw=1.6, head=0.2, zorder=16)
bio.arrow(ax, (a["oec"][0] - 0.75, a["oec"][1] - 0.1), (a["oec"][0] - 0.38, a["oec"][1]), **kw)
bio.arrow(ax, (a["qb"][0] + 0.02, a["qb"][1]), (pq1[0] - 0.25, pq1[1] + 0.05), **kw)
bio.arrow(ax, (pq1[0] + 0.7, pq1[1] - 0.1), (b["qp"][0] - 0.25, b["qp"][1]), **kw)
bio.arrow(ax, (b["f"][0] + 0.3, b["f"][1] - 0.15), (pc[0] - 0.33, pc[1] + 0.05), bend=0.25, **kw)
bio.arrow(ax, (pc[0] + 0.33, pc[1] + 0.05), (c["pc_site"][0] - 0.05, c["pc_site"][1] - 0.08), bend=0.25, **kw)
bio.arrow(ax, (c["fd_site"][0] + 0.35, c["fd_site"][1] + 0.05), (fd[0] - 0.3, fd[1] - 0.02), bend=-0.2, **kw)
bio.arrow(ax, (fd[0] + 0.28, fd[1] - 0.05), (fn[0] - 0.45, fn[1] + 0.15), bend=-0.25, **kw)

bio.label(ax, (a["oec"][0] - 0.85, a["oec"][1] - 0.55), "2 H₂O → O₂ + 4 H⁺", size="tiny", ha="center", va="top")
bio.arrow(ax, (fn[0] + 0.5, fn[1] + 0.1), (fn[0] + 1.25, fn[1] + 0.85), kind="process", color=P.ink(), lw=1.1, head=0.16)
bio.label(ax, (fn[0] + 0.45, fn[1] + 1.15), "2 NADP⁺ + 2 H⁺", size="tiny", ha="right")
bio.label(ax, (fn[0] + 1.35, fn[1] + 1.1), "2 NADPH", size="tiny", ha="left", bold=True)


def h_arrow(p0, p1, text, side="right"):
    bio.arrow(ax, p0, p1, kind="process", color=HC, lw=1.3, head=0.18, zorder=17)
    ps.proton(ax, p0, text=text, side=side)


h_arrow((6.15, y + 2.25), (6.45, y + 0.35), "4 H⁺", side="left")
h_arrow((8.75, y + 2.25), (9.05, y + 0.95), "4 H⁺", side="left")
bio.arrow(ax, (b["qp"][0] + 0.1, b["qp"][1] - 0.6), (b["qp"][0] - 0.1, y - 2.2), kind="process", color=HC, lw=1.3, head=0.18)
ps.proton(ax, (b["qp"][0] - 0.25, y - 2.45), text="8 H⁺", side="right")
ps.proton(ax, (a["oec"][0] + 0.75, a["oec"][1] - 0.2), text="4 H⁺", side="right")
bio.label(ax, (b["qp"][0] - 0.05, y - 1.45), "Q cycle", size="tiny", zorder=18, ha="right")

ch = d["channel"]
bio.arrow(ax, (ch[0] + 0.15, y - 2.35), (ch[0] + 0.15, y + 1.2), kind="process", color=HC, lw=1.8, head=0.22, zorder=9)
ps.proton(ax, (ch[0] + 0.5, y - 2.15), text="14 H⁺", side="right")
atp = (d["head"][0] - 2.05, d["head"][1] + 0.05)
bio.reaction(ax, (atp[0], atp[1] - 0.55), (atp[0], atp[1] + 0.75), side=None)
bio.molecule(ax, (atp[0], atp[1] + 1.05), token="atp", text="3 ATP", r=0.36, size=5.6)
bio.label(ax, (atp[0], atp[1] - 0.85), "3 ADP + 3 Pᵢ", size="tiny")

bio.label(ax, (27.2, y + 3.4), "pH ≈ 8", size="small", ha="right", color=P.muted())
bio.label(ax, (27.2, y - 2.5), "pH ≈ 5", size="small", ha="right", color=P.muted())
for k, (text, col) in enumerate((("electrons", EC), ("protons", HC))):
    x0 = 14.9 + k * 2.6
    bio.arrow(ax, (x0, y - 2.75), (x0 + 0.7, y - 2.75), kind="process", color=col, lw=1.4, head=0.18)
    bio.label(ax, (x0 + 0.85, y - 2.75), text, size="tiny", ha="left")
bio.label(ax, (14.0, 0.45), "Per O₂: 8 photons · 4 e⁻ · 12 H⁺ into the lumen · 2 NADPH · ≈ 2.6 ATP (14 H⁺ per 3 ATP)",
          size="small", color=P.ink())
