"""The sex-determination cascade of Drosophila (SBGN activity flow). In XX embryos the double dose of X-linked
signal elements activates the early promoter of Sex-lethal (Sxl); Sxl protein then maintains its own
productive splicing (positive feedback), directs female splicing of transformer (tra), and Tra with Tra2
gives female-specific Doublesex (DsxF), and blocks translation of msl-2 so that there is no dosage
compensation complex. In XY embryos no early Sxl is made: Sxl and tra transcripts are spliced to include stop
codons, dsx is spliced by default to the male form (DsxM), and MSL-2 assembles the complex that doubles
transcription of the single X."""
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(20.0, 8.6)
d = network.Diagram(ax)
for k, (sex, xse) in enumerate((("XX", "2 doses of X signal elements"), ("XY", "1 dose of X signal elements"))):
    y = 6.7 - k * 4.0
    on = k == 0
    bio.label(ax, (0.5, y + 1.25), "XX embryo: female" if on else "XY embryo: male", size="small", ha="left", bold=True)
    d.activity(f"x{k}", (2.3, y), xse if False else ("SisA, Scute, Runt, Upd\n" + ("x 2" if on else "x 1")), token="highlight", size="small")
    d.activity(f"sxl{k}", (6.6, y), "Sxl" if on else "no Sxl", token="protein" if on else "neutral", size="small")
    d.activity(f"tra{k}", (10.3, y), "Tra (+ Tra2)" if on else "no Tra", token="enzyme" if on else "neutral", size="small")
    d.activity(f"dsx{k}", (14.0, y), "DsxF" if on else "DsxM", token="receptor" if on else "dna", size="small")
    d.phenotype(f"ph{k}", (18.0, y), "female soma" if on else "male soma", token="receptor" if on else "dna", size="small")
    d.activity(f"msl{k}", (10.3, y - 1.6), "MSL-2 (not translated)" if on else "MSL-2, MSL complex", token="neutral" if on else "channel", size="small")
    d.phenotype(f"dc{k}", (14.6, y - 1.6), "no X hyperactivation" if on else "X transcription x 2", token="neutral" if on else "channel", size="small")
    if on:
        d.connect(f"x{k}", f"sxl{k}", kind="positive", text="Pe", text_offset=(0, 0.25))
        d.connect(f"sxl{k}", f"sxl{k}", kind="positive", loop=90)
        d.connect(f"sxl{k}", f"tra{k}", kind="positive", text="splicing", text_offset=(0, 0.25))
        d.connect(f"tra{k}", f"dsx{k}", kind="positive", text="splicing", text_offset=(0, 0.25))
        d.connect(f"sxl{k}", f"msl{k}", kind="negative", via=[(6.6, y - 1.6)])
    else:
        d.connect(f"x{k}", f"sxl{k}", kind="positive", dashed=True, text="too weak", text_offset=(0, 0.25))
        d.connect(f"sxl{k}", f"tra{k}", kind="positive", dashed=True, text="male splicing", text_offset=(0, 0.25))
        d.connect(f"tra{k}", f"dsx{k}", kind="unknown", dashed=True, text="default", text_offset=(0, 0.25))
    d.connect(f"dsx{k}", f"ph{k}", kind="positive")
    d.connect(f"msl{k}", f"dc{k}", kind="positive")
