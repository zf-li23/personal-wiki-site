"""The respiratory chain on the redox scale. Standard transformed reduction potentials E'0 of the carriers
(Lehninger 8e, Tables 13-7 and 19-2), in the order of electron flow; electrons move upward. The three
proton-pumping segments (Complexes I, III, IV) are shaded; for each, the drop in E'0, the standard Gibbs
energy per pair of electrons, dG'0 = -2F dE'0, and the protons moved per pair are given. Succinate enters
at the level of ubiquinone through Complex II, which pumps no protons."""

import numpy as np

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio.quant import Plot, line_color

P = bio.P
F = be.F
carriers = [  # name, E'0 / V, x, token
    ("NADH", -0.320, 0.6, "metabolite"),
    ("FMN", -0.30, 1.6, be.COLOR["complex_i"]),
    ("Fe–S (N2)", -0.15, 2.6, be.COLOR["complex_i"]),
    ("Q / QH₂", 0.045, 3.8, be.COLOR["q"]),
    ("cyt b", 0.077, 4.9, be.COLOR["complex_iii"]),
    ("cyt c₁", 0.22, 5.9, be.COLOR["complex_iii"]),
    ("cyt c", 0.254, 6.95, be.COLOR["cyt_c"]),
    ("cyt a", 0.29, 8.0, be.COLOR["complex_iv"]),
    ("cyt a₃–Cu_B", 0.35, 9.05, be.COLOR["complex_iv"]),
    ("O₂ / H₂O", 0.816, 10.2, "positive"),
]

fig, ax = bio.canvas(19.0, 12.0)
p = Plot(ax, (2.2, 1.0, 13.2, 10.2), xlim=(0, 11), ylim=(-0.45, 0.92), ylabel="$E'^{\\circ}$ / V",
         yticks=[-0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8], grid=True, frame="l")
spans = [(0.15, 3.25, be.COLOR["complex_i"], "Complex I", -0.320, 0.045, 4),
         (3.4, 6.45, be.COLOR["complex_iii"], "Complex III", 0.045, 0.254, 4),
         (6.6, 10.75, be.COLOR["complex_iv"], "Complex IV", 0.254, 0.816, 2)]
for a, b, tok, name, e0, e1, h in spans:
    p.span(a, b, tok, strength=0.78)
    dE = e1 - e0
    dG = -2 * F * dE
    x, y = p.xy((a + b) / 2, 0.9)
    bio.label(ax, (x, y), name, size="small", bold=True)
    bio.label(ax, (x, y - 0.42), f"ΔE′° = {dE:.3f} V", size="tiny")
    bio.label(ax, (x, y - 0.78), f"ΔG′° = {dG:.0f} kJ mol⁻¹".replace("-", "−"), size="tiny")
    bio.label(ax, (x, y - 1.14), f"{h} H⁺ per 2 e⁻", size="tiny", color=line_color(be.COLOR["proton"]), bold=True)

pos, wid = {}, {}
H = 0.42
for name, e, x, tok in carriers:
    xy = p.xy(x, e)
    pos[name] = xy
    wid[name] = 1.25 if len(name) > 6 else 0.95
    bio.box(ax, xy, wid[name], H, tok, text=name.replace("_B", "B"), size="tiny", radius=0.1, zorder=14)


def edge(name, v):
    # where the ray from a box centre along v leaves the box
    c = np.asarray(pos[name])
    tx = (wid[name] / 2 + 0.06) / abs(v[0]) if abs(v[0]) > 1e-9 else 1e9
    ty = (H / 2 + 0.06) / abs(v[1]) if abs(v[1]) > 1e-9 else 1e9
    return c + v * min(tx, ty)


ec = line_color(be.COLOR["electron"])
names = [c[0] for c in carriers]
for a, b in zip(names[:-1], names[1:]):
    pa, pb = np.array(pos[a]), np.array(pos[b])
    d = (pb - pa) / np.linalg.norm(pb - pa)
    bio.arrow(ax, edge(a, d), edge(b, -d), kind="process", color=ec, lw=1.3, head=0.15, zorder=13)

# succinate entry through Complex II
sx, sy = p.xy(3.85, -0.2)
bio.box(ax, (sx, sy), 1.9, 0.42, be.COLOR["complex_ii"], text="succinate (via II)", size="tiny", radius=0.1, zorder=14)
bio.arrow(ax, (sx, sy + 0.27), (pos["Q / QH₂"][0], pos["Q / QH₂"][1] - 0.27), kind="process", color=ec,
          lw=1.2, head=0.15, dashed=True)

# right-hand energy scale: dG'0 for transferring 2 e- from the level to O2
q = Plot(ax, (15.4, 1.0, 0.01, 10.2), xlim=(0, 1), ylim=(-2 * F * (0.816 + 0.45), -2 * F * (0.816 - 0.92)),
         frame=None, yticks=None)
for v in (-240, -200, -150, -100, -50, 0):
    yy = q.Y(v)
    ax.plot([15.4, 15.5], [yy, yy], color=P.muted(), lw=0.8)
    bio.label(ax, (15.6, yy), f"{v}".replace("-", "−"), size="tiny", ha="left", color=P.muted())
ax.plot([15.4, 15.4], [1.0, 11.2], color=P.muted(), lw=0.8)
bio.label(ax, (17.4, 6.1), "ΔG′° for 2 e⁻ → O₂ / (kJ mol⁻¹)", size="small", rotation=90)
bio.label(ax, (8.8, 0.45), "NADH → O₂: ΔE′° = 1.136 V, ΔG′° = −219 kJ mol⁻¹; 10 H⁺ pumped", size="small")
