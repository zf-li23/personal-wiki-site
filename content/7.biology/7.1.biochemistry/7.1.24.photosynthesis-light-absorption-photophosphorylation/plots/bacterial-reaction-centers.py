"""The two types of photochemical reaction center in bacteria, on a midpoint-potential axis (reducing at the
top; approximate values at pH 7 from Blankenship, Molecular Mechanisms of Photosynthesis, 2nd ed.).
(A) Purple bacteria (type II, pheophytin-quinone): light raises P870 to P870*, which reduces bacteriopheophytin
and the quinones QA and QB; quinol diffuses to the cytochrome bc1 complex, which pumps protons (Q cycle) and
returns the electron through cytochrome c2 to P870+: cyclic electron flow, ATP but no NADH (purple bacteria make
NADH by reverse electron flow). (B) Green sulfur bacteria (type I, Fe-S): P840* reduces a chlorophyll (A0),
a quinone and the Fe-S clusters FX, FA/FB, then ferredoxin, which reduces NAD+ (linear flow); the electron
lost by P840+ is replaced from H2S through cytochrome c; a cyclic route through menaquinone and the bc complex
also exists. Excited-state levels are the ground-state potentials minus the photon energies (1.42 and 1.48 eV)."""

import numpy as np

import wikibio as bio
from wikibio import photosynthesis as ps
from wikibio.quant import Plot, line_color

P = bio.P
EC = line_color(ps.COLOR["electron"])
LC = line_color(ps.COLOR["light"])
fig, ax = bio.canvas(25.0, 10.2)


def chain(box_, carriers, links, photo, cyclic=None, title=""):
    p = Plot(ax, box_, (0, 10), (0.6, -1.4), ylabel="$E_{\\mathrm{m}}$ / V",
             yticks=[(v, f"{v:+.1f}".replace("+0.0", "0").replace("-", "−")) for v in (-1.2, -0.8, -0.4, 0.0, 0.4)])
    pos = {n: p.xy(x, e) for n, e, x, t in carriers}
    for n, e, x, t in carriers:
        bio.box(ax, pos[n], 1.45 if len(n) > 6 else 1.05, 0.42, t, text=n, size="tiny", radius=0.1, zorder=14)
    for a, b, kw in links:
        pa, pb = np.array(pos[a]), np.array(pos[b])
        d = (pb - pa) / np.linalg.norm(pb - pa)
        bio.arrow(ax, pa + d * 0.45, pb - d * 0.45, kind="process", color=EC, lw=1.3, head=0.16, zorder=13, **kw)
    g, x = photo
    a, b = pos[g], pos[g + "*"]
    bio.arrow(ax, (a[0], a[1] + 0.26), (b[0], b[1] - 0.26), kind="process", color=LC, lw=3.0, head=0.32, zorder=12)
    ps.photon(ax, (a[0] + 1.7, (a[1] + b[1]) / 2 - 0.9), (a[0] + 0.2, (a[1] + b[1]) / 2 - 0.5), text=None, waves=3)
    bio.label(ax, (a[0] + 1.75, (a[1] + b[1]) / 2 - 1.25), f"hν, {x} nm", size="tiny", color=LC)
    bio.label(ax, (box_[0] + box_[2] / 2, box_[1] + box_[3] + 0.35), title, size="small", bold=True)
    return pos


bio.panel(ax, "A", (0.1, 10.1))
purple = [("P870", 0.45, 2.0, "protein"), ("P870*", -0.97, 2.0, "protein"), ("BPheo", -0.6, 3.2, "protein"),
          ("Q_A", -0.18, 4.2, "protein"), ("Q_B", -0.05, 5.1, "protein"), ("UQ pool", 0.09, 6.2, "lipid"),
          ("FeS / cyt c₁", 0.28, 7.6, "cytb6f"), ("cyt c₂", 0.35, 8.8, "drug")]
purple = [(n.replace("Q_A", "QA").replace("Q_B", "QB"), e, x, t) for n, e, x, t in purple]
pos = chain((2.0, 0.9, 9.6, 8.3), purple,
            [("P870*", "BPheo", {}), ("BPheo", "QA", {}), ("QA", "QB", {}), ("QB", "UQ pool", {}),
             ("UQ pool", "FeS / cyt c₁", {}), ("FeS / cyt c₁", "cyt c₂", {})], ("P870", 870),
            title="Purple bacteria: type II, cyclic")
a, b = np.array(pos["cyt c₂"]), np.array(pos["P870"])
bio.arrow(ax, (a[0], a[1] - 0.25), (b[0] + 0.55, b[1] - 0.15), kind="process", color=EC, lw=1.3, head=0.16, bend=-0.12)
bio.label(ax, (pos["UQ pool"][0] + 2.3, pos["UQ pool"][1] + 0.1), "bc₁: H⁺ pumped", size="tiny",
          color=line_color(ps.COLOR["proton"]), bold=True)

bio.panel(ax, "B", (12.6, 10.1))
green = [("P840", 0.24, 3.0, "psi"), ("P840*", -1.24, 3.0, "psi"), ("A₀", -1.0, 4.0, "psi"), ("A₁", -0.75, 4.6, "psi"),
         ("F_X", -0.67, 5.5, "psi"), ("F_A/F_B", -0.55, 6.5, "psi"), ("Fd", -0.45, 7.6, "drug"),
         ("NAD⁺", -0.32, 8.8, "metabolite"), ("H₂S/S", -0.27, 0.9, "highlight"), ("cyt c", 0.17, 1.5, "drug"),
         ("MK pool", -0.07, 6.4, "lipid"), ("bc", 0.15, 5.0, "cytb6f")]
green = [(n.replace("F_X", "FX").replace("F_A/F_B", "FA/FB"), e, x, t) for n, e, x, t in green]
pos = chain((14.6, 0.9, 9.6, 8.3), green,
            [("P840*", "A₀", {}), ("A₀", "A₁", {}), ("A₁", "FX", {}), ("FX", "FA/FB", {}), ("FA/FB", "Fd", {}),
             ("Fd", "NAD⁺", {}), ("H₂S/S", "cyt c", {}), ("cyt c", "P840", {})], ("P840", 840),
            title="Green sulfur bacteria: type I, linear and cyclic")
fdx = np.array(pos["Fd"])
for a_, b_ in (("Fd", "MK pool"), ("MK pool", "bc"), ("bc", "cyt c")):
    pa, pb = np.array(pos[a_]), np.array(pos[b_])
    d = (pb - pa) / np.linalg.norm(pb - pa)
    bio.arrow(ax, pa + d * 0.5, pb - d * 0.5, kind="process", color=EC, lw=1.1, head=0.15, dashed=True, zorder=12)
bio.label(ax, (pos["bc"][0], pos["bc"][1] - 0.5), "H⁺ pumped", size="tiny", color=line_color(ps.COLOR["proton"]), bold=True)
