# wikibio.mesoderm sampler. Row 1: the somite in transverse section (epithelial, early, mature) and the
# presomitic mesoderm with cyclic gene stripes and the FGF/Wnt and RA gradients. Row 2: endochondral
# ossification (cartilage model, primary centre, secondary centres), a growth plate, the nephric series and two
# steps of nephrogenesis. Row 3: the bipotential gonad, testis and ovary, and the genital ducts.
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(34, 30)
P = bio.P
for k, st in enumerate(("epithelial", "early", "mature")):
    x = 4.0 + k * 8.2
    a = M.somite_section(ax, (x, 28.5), 7.5, st)
    bio.label(ax, (x, 29.4), st.capitalize(), bold=True)
    if st == "mature":
        for key, dx, dy, t in (("dermomyotome", 2.2, 1.2, "Dermomyotome"), ("myotome", 2.6, 0.0, "Myotome"),
                               ("sclerotome", 2.5, -1.8, "Sclerotome"), ("syndetome", 2.8, -0.9, "Syndetome")):
            bio.callout(ax, a[key], (a[key][0] + dx, a[key][1] + dy), t)
p = M.psm(ax, (26.5, 25.5), 7.0, 0.9, phase=0.3)
bio.callout(ax, p["tailbud"], (32.5, 27.4), "Tail bud")
bio.callout(ax, p["front"], (29.0, 27.4), "Front")
for k, st in enumerate(("cartilage", "primary", "secondary")):
    M.ossification(ax, (2.5 + k * 3.2, 16.0), 5.5, st)
g = M.growth_plate(ax, (11.0, 13.0, 3.0, 6.5))
for z in ("resting", "proliferative", "hypertrophic", "metaphysis"):
    bio.label(ax, (14.3, g[z][1]), z.capitalize(), size="tiny", ha="left")
n = M.nephric_series(ax, (17.5, 13.5), 11.0, gonad=True)
for key, t in (("pronephros", "Pronephros"), ("mesonephros", "Mesonephros"), ("metanephric", "Metanephros")):
    bio.callout(ax, n[key], (n[key][0], 19.6), t)
M.nephrogenesis(ax, (30.5, 17.5), 1.0, "s-shaped")
M.nephrogenesis(ax, (33.0, 17.5), 1.0, "nephron")
for k, f in enumerate(("indifferent", "testis", "ovary")):
    M.gonad(ax, (3.0 + k * 5.0, 6.0), 1.6, f)
    bio.label(ax, (3.0 + k * 5.0, 1.8), f.capitalize(), bold=True)
for k, sx in enumerate(("indifferent", "male", "female")):
    M.genital_ducts(ax, (19.0 + k * 5.5, 6.0), 6.0, sx)
    bio.label(ax, (19.0 + k * 5.5, 1.8), sx.capitalize(), bold=True)
