"""Filtering the variants of an exome or genome to find the cause of a rare Mendelian disease (typical
numbers for one individual of European ancestry; they vary with ancestry and with the capture kit)."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 8.2)
steps = [("All variants in a genome", "about 4–5 million", 20.0, "neutral"),
         ("In protein-coding exons and splice sites", "about 20 000–25 000", 16.0, "dna"),
         ("Rare (population frequency below 1 % or 0.1 %)", "about 500–1 000", 12.4, "enzyme"),
         ("Predicted to alter the protein (missense, nonsense, frameshift, splice)", "about 100–300", 9.6, "antibody"),
         ("Fits the mode of inheritance (de novo in a trio, biallelic, segregates)", "1–10 candidates", 7.0, "receptor"),
         ("Gene matches the phenotype; functional or replication evidence", "diagnosis", 4.4, "negative")]
y = 7.4
for text, n, w, tok in steps:
    bio.box(ax, (11, y), w, 0.9, token=tok)
    bio.label(ax, (11, y + 0.17), text, size="small", color=P.on_fill(), zorder=12)
    bio.label(ax, (11, y - 0.22), n, size="tiny", color=P.on_fill(), zorder=12)
    y -= 1.25
