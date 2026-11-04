"""The EnvZ-OmpR two-component system of E. coli.
A: the sensor histidine kinase EnvZ (a dimer in the cytoplasmic membrane) autophosphorylates on a
   histidine (H) with ATP when the osmolarity of the medium rises, transfers the phosphoryl group to an
   aspartate (D) of the response regulator OmpR, and also dephosphorylates OmpR-P (bifunctional kinase).
   OmpR-P binds upstream of ompF and ompC. ompC is also followed by the divergent micF gene, whose small
   RNA blocks translation of ompF mRNA.
B: a model of the outputs (arbitrary units): high-affinity OmpR-P sites activate ompF at low OmpR-P,
   low-affinity sites repress ompF and activate ompC (and micF) at high OmpR-P, so the cell exchanges the
   wide porin OmpF for the narrower OmpC as osmolarity rises."""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio
from wikibio import charts
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(24.0, 10.0)
bio.panel(ax, "A", (0.2, 9.85))

# membrane band
my0, my1 = 6.2, 7.2
ax.add_patch(FancyBboxPatch((0.6, my0), 14.0, my1 - my0, boxstyle="round,pad=0,rounding_size=0.2",
                            facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_head"), lw=1.4, zorder=2))
bio.label(ax, (6.0, 8.0), "Outside (osmolarity changes)", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (0.8, 5.75), "Cytoplasm", size="tiny", color=P.muted(), ha="left")


def subunit(x, top, bottom, w=0.75):
    ax.add_patch(FancyBboxPatch((x - w / 2, bottom), w, top - bottom, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=1.2, zorder=6))


for x in (3.2, 4.1):
    subunit(x, 8.4, 4.0)
bio.label(ax, (3.65, 8.75), "EnvZ", size="small", bold=True)
bio.label(ax, (2.0, 7.9), "sensor", size="tiny", color=P.muted())
bio.label(ax, (2.0, 4.6), "kinase", size="tiny", color=P.muted())


def site(xy, text, phos):
    ax.add_patch(Circle(xy, 0.28, facecolor=P.fill("highlight") if phos else P.surface(), edgecolor=P.edge("highlight"),
                        lw=1.0, zorder=9))
    bio.label(ax, xy, text, size="tiny", color=P.on_fill() if phos else P.ink(), zorder=10)


site((4.1, 4.9), "H~P", True)
bio.label(ax, (3.65, 3.6), "ATP → ADP", size="tiny")


def rr(x, y, phos):
    ax.add_patch(Ellipse((x, y), 1.7, 0.95, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=1.2, zorder=6))
    bio.label(ax, (x - 0.2, y), "OmpR", size="tiny", color=P.on_fill(), zorder=8)
    site((x + 0.85, y + 0.35), "D~P" if phos else "D", phos)


rr(7.6, 4.6, False)
rr(11.6, 4.6, True)
bio.arrow(ax, (4.5, 5.05), (6.7, 4.8), kind="process", lw=1.3, head=0.2)
bio.label(ax, (5.7, 5.35), "phosphotransfer", size="tiny", color=P.muted())
bio.arrow(ax, (8.6, 4.75), (10.6, 4.75), kind="process", lw=1.3, head=0.2)
bio.arrow(ax, (10.7, 4.35), (8.6, 4.35), kind="process", lw=1.0, head=0.16, dashed=True)
bio.label(ax, (9.6, 3.95), "dephosphorylation by EnvZ", size="tiny", color=P.muted())

# genes
gy = 1.2
gl = G.construct(ax, 1.0, gy, [{"kind": "promoter"}, {"kind": "cds", "text": "ompF", "width": 2.2, "token": "dna"}])
gl2 = G.construct(ax, 6.4, gy, [{"kind": "cds", "text": "micF", "width": 1.6, "token": "rna", "reverse": True},
                                {"kind": "promoter", "reverse": True}, {"kind": "promoter"},
                                {"kind": "cds", "text": "ompC", "width": 2.2, "token": "dna"}])
bio.arrow(ax, (10.9, 4.1), (gl[0]["centre"] + 0.25, 1.75), kind="modulation", lw=1.0, head=0.2)
bio.label(ax, (0.8, 3.2), "low OmpR-P: on\nhigh OmpR-P: off", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (11.8, 4.05), (gl2[2]["centre"] + 0.1, 1.7), kind="activation", lw=1.0, head=0.2)
bio.label(ax, (12.6, 2.4), "high OmpR-P: on", size="tiny", color=P.muted())
bio.arrow(ax, (gl2[0]["x0"] - 0.1, gy - 0.5), (gl[1]["centre"], gy - 0.5), kind="inhibition", lw=1.0, head=0.2,
          color=P.edge("rna"), bend=-0.2)
bio.label(ax, (4.9, 0.25), "MicF sRNA blocks ompF translation", size="tiny", color=P.edge("rna"))

# B: model of outputs
bio.panel(ax, "B", (15.6, 9.85))
pax = charts.axes_at(ax, (17.0, 2.4, 6.4, 6.0))
s = np.linspace(0, 1, 300)  # osmolarity (scaled)
x = s ** 2 / (0.25 + s ** 2) * 1.25  # OmpR-P level
hill = lambda v, K, n: v ** n / (K ** n + v ** n)
ompf = hill(x, 0.12, 2) * (1 - hill(x, 0.55, 4))
ompc = hill(x, 0.6, 4)
pax.plot(s, ompf / ompf.max(), color=charts.line("dna"), lw=2.0, label="OmpF (wide pore)")
pax.plot(s, ompc / ompc.max(), color=charts.line("receptor"), lw=2.0, ls="--", label="OmpC (narrow pore)")
pax.plot(s, x / x.max(), color=charts.line("highlight"), lw=1.3, ls=":", label="OmpR-P")
pax.set_xlim(0, 1)
pax.set_ylim(0, 1.15)
pax.set_xticks([0, 1], ["low", "high"])
pax.set_yticks([])
pax.legend(fontsize=6.8, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
charts.style_axes(pax, "osmolarity of medium", "level (a.u.)")
charts.title(pax, "Porin switch (model)")
