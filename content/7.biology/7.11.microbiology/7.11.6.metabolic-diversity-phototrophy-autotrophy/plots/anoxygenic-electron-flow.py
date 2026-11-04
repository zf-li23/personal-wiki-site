"""Electron flow in the two kinds of anoxygenic phototrophs, drawn on a scale of standard reduction potential.

Approximate midpoint potentials E'° (V) after Madigan et al. (2019). Left, purple bacteria (type II,
quinone-type reaction center): light converts the special pair P870 (about +0.45 V) into the strong donor
P870* (about -1.0 V); electrons pass through bacteriochlorophyll (Bchl) and bacteriopheophytin (Bph) to the
quinones QA and QB and the membrane quinone pool (about 0 V), then through the cytochrome bc1 complex and
cytochrome c2 back to P870 (cyclic electron flow, which pumps protons). Because the quinone pool is more
positive than NAD+/NADH (-0.32 V), NADH is made by reverse electron transport driven by the proton-motive
force; electrons from H2S (S0/HS-, -0.27 V) enter at the quinone pool.
Right, green sulfur bacteria (type I, iron-sulfur reaction center, P840 about +0.25 V, P840* about -1.2 V):
the acceptors (chlorophyll a, iron-sulfur clusters) are more negative than ferredoxin (Fd, -0.42 V), which
reduces NAD+ directly and drives CO2 fixation; electrons from sulfide enter via menaquinone (MQ) and
cytochrome c (noncyclic flow). Heliobacteria (P798, bacteriochlorophyll g) resemble the right panel.
"""
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 14.0)
ytop, ybot = -1.3, 0.6
pl = quant.Plot(ax, (1.8, 0.8, 0.01, 12.4), xlim=(0, 1), ylim=(ybot, ytop), ylabel="E'° / V",
                yticks=[-1.25, -1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5], frame="l")


def Y(e):
    return float(pl.Y(e))


def node(x, e, text, token, w=2.0, size="small"):
    bio.box(ax, (x, Y(e)), w, 0.62, token=token, text=text, size=size)
    return (x, Y(e))


def e_arrow(a, b, dashed=False, color=None, bend=0.0, text=None, side=0.35):
    bio.arrow(ax, a, b, kind="process", shrink=0.36, dashed=dashed, color=color or P.edge("dna"), bend=bend)
    if text:
        bio.label(ax, ((a[0] + b[0]) / 2 + side, (a[1] + b[1]) / 2), text, size="tiny", ha="left" if side > 0 else "right",
                  color=color or P.muted())


# --- purple bacteria ---------------------------------------------------------------------------
bio.label(ax, (6.6, 13.6), "Purple bacteria: type II (Q-type) reaction center", size="small", bold=True)
xa = 4.2
p870 = node(xa, 0.45, "P870", "protein")
p870s = node(xa, -1.0, "P870*", "protein")
bchl = node(xa + 1.4, -0.75, "Bchl", "protein", w=1.3)
bph = node(xa + 2.4, -0.55, "Bph", "protein", w=1.3)
qa = node(xa + 3.3, -0.2, "QA → QB", "lipid", w=1.8)
qp = node(xa + 4.6, 0.02, "Q pool", "lipid", w=1.6)
bc1 = node(xa + 4.6, 0.25, "Cyt bc₁", "metabolite", w=1.6)
c2 = node(xa + 2.4, 0.36, "Cyt c₂", "receptor", w=1.4)
nadh = node(xa + 6.6, -0.32, "NAD⁺/NADH", "atp", w=2.0)
bio.arrow(ax, (p870[0] - 1.25, p870[1]), (p870s[0] - 1.25, p870s[1]), kind="process", color=P.edge("highlight"), lw=2.4)
bio.label(ax, (p870[0] - 1.45, (p870[1] + p870s[1]) / 2), "light", size="small", ha="right", color=P.edge("highlight"))
e_arrow(p870s, bchl)
e_arrow(bchl, bph)
e_arrow(bph, qa)
e_arrow(qa, qp)
e_arrow(qp, bc1)
e_arrow(bc1, c2)
e_arrow(c2, p870)
bio.label(ax, (xa + 2.3, Y(0.12)), "cyclic electron flow\n(pumps H⁺)", size="tiny", color=P.muted())
e_arrow((qp[0] + 0.5, qp[1] - 0.3), (nadh[0] - 0.4, nadh[1] + 0.3), dashed=True, color=P.edge("negative"))
bio.label(ax, (xa + 6.4, Y(-0.12)), "reverse electron\ntransport (costs pmf)", size="tiny", color=P.edge("negative"), ha="left")
sx = xa + 6.8
bio.label(ax, (sx + 0.1, Y(0.12)), "H₂S → S⁰", size="small", color=P.edge("atp"), ha="left")
bio.arrow(ax, (sx, Y(0.12)), (qp[0] + 0.85, qp[1] + 0.05), kind="process", color=P.edge("atp"))

# --- green sulfur bacteria -----------------------------------------------------------------------
bio.label(ax, (17.4, 13.6), "Green sulfur bacteria: type I (FeS-type) reaction center", size="small", bold=True)
xb = 14.6
p840 = node(xb, 0.25, "P840", "plant")
p840s = node(xb, -1.2, "P840*", "plant")
chl = node(xb + 1.5, -1.0, "Chl a", "plant", w=1.3)
fes = node(xb + 2.6, -0.58, "FeS", "ferredoxin", w=1.2)
fd = node(xb + 3.8, -0.42, "Fd", "ferredoxin", w=1.0)
nad2 = node(xb + 5.6, -0.32, "NAD⁺/NADH", "atp", w=2.0)
co2 = node(xb + 4.4, -0.85, "CO₂ fixation\n(rTCA)", "carbohydrate", w=2.0, size="tiny")
mq = node(xb + 3.4, -0.07, "MQ", "lipid", w=1.1)
cyt = node(xb + 2.0, 0.17, "Cyt c", "receptor", w=1.2)
bio.arrow(ax, (p840[0] - 1.25, p840[1]), (p840s[0] - 1.25, p840s[1]), kind="process", color=P.edge("highlight"), lw=2.4)
bio.label(ax, (p840[0] - 1.45, (p840[1] + p840s[1]) / 2), "light", size="small", ha="right", color=P.edge("highlight"))
e_arrow(p840s, chl)
e_arrow(chl, fes)
e_arrow(fes, fd)
e_arrow(fd, nad2)
e_arrow(fd, co2)
e_arrow(mq, cyt)
e_arrow(cyt, p840)
bio.label(ax, (xb + 4.7, Y(0.15)), "H₂S → S⁰", size="small", color=P.edge("atp"), ha="left")
bio.arrow(ax, (xb + 4.6, Y(0.15)), (mq[0] + 0.55, mq[1] + 0.05), kind="process", color=P.edge("atp"))
bio.label(ax, (xb + 3.2, Y(0.45)), "noncyclic flow: no reverse\nelectron transport needed", size="tiny", color=P.muted())
