# Host range, tropism and spread within a host.
# A: three receptor requirements and the cells they restrict the virus to.
# B: the routes a virus takes once it has entered: local replication, haematogenous spread in two
#    stages of viraemia, or retrograde axonal transport along peripheral nerves, and then shedding.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 9.2)

# --- A  receptors ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.0))
bio.label(ax, (8.5, 8.85), "The receptor sets which cells are susceptible", size="title", bold=True)

COLS = [
    (2.8, "Hepatitis B virus", "NTCP", "channel", None,
     "bile-acid transporter,\nbasolateral membrane\nof hepatocytes", "strict hepatotropism;\nnarrow host range"),
    (8.5, "SARS-CoV-2", "ACE2", "rtk", "TMPRSS2",
     "ACE2 on nasal, bronchial\nand alveolar epithelium,\ngut, kidney, endothelium",
     "respiratory entry,\nsystemic complications"),
    (14.2, "HIV-1", "CD4", "rtk", "CCR5",
     "CD4 with a chemokine\ncoreceptor on T cells,\nmacrophages, dendritic cells",
     "$CCR5$-$\\Delta32$ homozygotes\nare largely resistant"),
]
for x, virus, rec, kind, second, where, consequence in COLS:
    y = 6.6
    bio.bilayer(ax, [(x - 2.2, y), (x + 2.2, y)])
    bio.label(ax, (x - 2.35, y + 0.45), "outside", size="tiny", color=P.muted(), ha="left")
    bio.label(ax, (x - 2.35, y - 0.5), "cytoplasm", size="tiny", color=P.muted(), ha="left")
    bio.receptor(ax, x - 0.7, y, kind=kind, token="receptor", text=rec)
    if second:
        bio.receptor(ax, x + 0.8, y, kind="channel", token="enzyme", text=second)
    bio.structures.virus(ax, (x - 0.7, y + 1.3), r=0.42, kind="enveloped", token="virus", spikes=10)
    bio.label(ax, (x, 8.55), virus, size="small", bold=True)
    bio.label(ax, (x, 5.0), where, size="tiny", color=P.muted())
    bio.label(ax, (x, 4.25), consequence, size="tiny", color=P.edge("virus"))

bio.label(ax, (8.5, 3.6), "a cell with the receptor is susceptible; it is productively infected only if it is also "
                          "permissive and its defences are overcome", size="tiny", color=P.muted())

# --- B  spread ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 3.6))
bio.label(ax, (3.2, 3.35), "Routes within the host", size="title", bold=True)


def stage(center, w, h, token, title, sub=None, size="small"):
    bio.box(ax, center, w, h, token=token, radius=0.2)
    bio.label(ax, (center[0], center[1] + (0.2 if sub else 0)), title, size=size, bold=True,
              color=P.on_fill())
    if sub:
        bio.label(ax, (center[0], center[1] - 0.26), sub, size="tiny", color=P.on_fill())


stage((1.9, 1.95), 3.0, 1.5, "metabolite", "Entry",
      "respiratory tract,\nalimentary tract, urogenital\ntract, conjunctiva, skin breach")
stage((5.6, 1.95), 2.7, 1.0, "bacterium", "Local replication", "at the portal of entry")
stage((9.7, 2.95), 4.3, 0.95, "neutral", "Local disease", "influenza virus, rotavirus")
stage((9.7, 1.75), 4.3, 1.15, "blood", "Haematogenous spread",
      "primary viraemia → liver, spleen,\nlymph node → secondary viraemia")
stage((9.7, 0.45), 4.3, 0.95, "neuron", "Neural spread", "retrograde axonal transport")
stage((14.4, 1.75), 3.8, 1.4, "animal", "Target organ",
      "poliovirus → motor neurons\nmeasles virus → skin\nrabies virus → brain")

bio.arrow(ax, (3.45, 1.95), (4.2, 1.95), kind="process")
bio.arrow(ax, (7.0, 2.2), (7.5, 2.9), kind="process")
bio.arrow(ax, (7.0, 1.95), (7.5, 1.8), kind="process")
bio.arrow(ax, (7.0, 1.7), (7.5, 0.55), kind="process")
bio.arrow(ax, (11.9, 1.75), (12.45, 1.75), kind="process")
bio.arrow(ax, (11.9, 0.55), (12.6, 1.2), kind="process")

bio.label(ax, (14.7, 0.5), "Shedding: secretions, saliva, faeces,\n"
                           "urine, milk, semen, blood, lesions", size="tiny", color=P.muted())
bio.arrow(ax, (14.4, 1.0), (14.4, 0.78), kind="process", color=P.edge("virus"))
