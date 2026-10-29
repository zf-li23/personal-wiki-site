"""The signalling pathways used repeatedly in animal development, as activity flows (SBGN AF style).

Each row: ligand -> receptor -> key transducer -> transcriptional effector, then the main developmental
roles. Activation is an open arrowhead, inhibition a bar. Wnt (canonical): Wnt binds Frizzled and LRP5/6,
the destruction complex is inhibited and beta-catenin enters the nucleus to act with TCF/LEF. TGF-beta
superfamily: Nodal/Activin/TGF-beta receptors phosphorylate Smad2/3, BMP receptors Smad1/5/8 (Smad9), both
partner Smad4. FGF and other RTK ligands: Ras-MAPK (and PI3K, PLC-gamma, JAK-STAT). Hedgehog: Hh binds and
inhibits Patched, relieving the inhibition of Smoothened, and Gli proteins switch from repressor to activator in the
primary cilium. Notch: Delta/Jagged on a neighbour triggers cleavage of Notch, whose intracellular domain
(NICD) acts with CSL (RBPJ). Eph-ephrin: both partners are membrane-bound and signal in both directions,
mostly to the cytoskeleton (RhoA). Hippo: cell contacts, polarity and mechanics activate the kinases Mst and
Lats, which keep YAP/TAZ out of the nucleus.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 15.4)
rows = [
    ("Wnt", "Frizzled +\nLRP5/6", "destruction\ncomplex", "β-catenin\n+ TCF/LEF", "axis formation, organizer, posterior\nfates, stem-cell niches, proliferation", "receptor", ("activation", "inhibition", "inhibition")),
    ("Nodal, Activin,\nTGF-β", "type I/II\nreceptor kinases", "Smad2/3\n(+ Smad4)", "Smad complex\n+ cofactors", "mesoderm and endoderm induction,\nleft-right asymmetry", "enzyme", ("activation", "activation", "activation")),
    ("BMP, GDF", "type I/II\nreceptor kinases", "Smad1/5/8\n(+ Smad4)", "Smad complex\n+ cofactors", "dorsal-ventral pattern, epidermis vs\nneural, bone, digit spacing", "antibody", ("activation", "activation", "activation")),
    ("FGF (EGF, PDGF,\nVEGF, IGF)", "receptor tyrosine\nkinase", "Ras–MAPK,\nPI3K", "Ets and other\nTFs", "mesoderm maintenance, limb outgrowth,\nbranching, vessels, growth", "channel", ("activation", "activation", "activation")),
    ("Hedgehog\n(Shh, Ihh, Dhh)", "Patched", "Smoothened\n(primary cilium)", "Gli activator /\nrepressor", "neural tube and limb pattern,\nbone growth, gut", "positive", ("inhibition", "inhibition", "activation")),
    ("Delta, Jagged\n(on neighbour)", "Notch", "cleavage:\nNICD released", "NICD + CSL\n(RBPJ)", "lateral inhibition, boundaries,\nsomite clock, blood vessels", "drug", ("activation", "activation", "activation")),
    ("ephrin\n(on neighbour)", "Eph receptor", "RhoA, Rac\n(both cells)", "cytoskeleton,\nadhesion", "boundaries, cell sorting,\naxon and crest guidance", "protein", ("activation", "activation", "activation")),
    ("contacts, polarity,\nmechanics", "Fat, Crumbs,\njunctions", "Mst → Lats\n(kinases)", "YAP/TAZ\n+ TEAD", "organ size, inner cell mass vs\ntrophectoderm, regeneration", "metabolite", ("activation", "activation", "inhibition")),
]
xs = [2.2, 6.2, 10.2, 14.2]
heads = ["ligand / input", "receptor", "transducer", "nuclear effector"]
for x, h in zip(xs, heads):
    bio.label(ax, (x, 15.0), h, size="small", bold=True)
bio.label(ax, (23.2, 15.0), "main developmental roles", size="small", bold=True)
for k, (lig, rec, tr, eff, role, tok, inh) in enumerate(rows):
    y = 13.9 - k * 1.78
    for j, (x, t) in enumerate(zip(xs, (lig, rec, tr, eff))):
        bio.box(ax, (x, y), 3.3, 1.3, tok if j else "neutral", text=t, size="tiny")
    for j in range(3):
        bio.arrow(ax, (xs[j] + 1.7, y), (xs[j + 1] - 1.7, y), kind=inh[j], head=0.2)
    bio.arrow(ax, (xs[3] + 1.7, y), (17.6, y), kind="activation", head=0.2)
    bio.label(ax, (17.8, y), role, size="tiny", ha="left")
bio.label(ax, (15.0, 0.45), "open arrow: activation; bar: inhibition (Wnt and Hedgehog act by relieving an inhibition; Hippo kinases inhibit YAP/TAZ)",
          size="tiny", color=P.muted())
