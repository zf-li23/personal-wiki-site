# The photocycle of bacteriorhodopsin: a light-driven proton pump.
# Intermediates are named by letters and their absorption maxima (nm); arrows carry approximate time constants
# at room temperature and the proton movements. Photon absorption isomerizes all-trans retinal to 13-cis
# (bR -> K, a few ps); the Schiff base gives its proton to Asp85 and a proton is released to the outside
# (L -> M); Asp96 reprotonates the Schiff base from the cytoplasmic side (M -> N), takes up a proton from
# the cytoplasm as the retinal reisomerizes (N -> O), and Asp85 returns its proton to the release group
# (O -> bR). Net: one proton from inside to outside per absorbed photon, with a quantum yield of about 0.6.
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(15, 9)
steps = [
    dict(text="bR 568\nall-trans", token="receptor"),
    dict(text="K 590\n13-cis", token="rna"),
    dict(text="L 550", token="enzyme"),
    dict(text="M 410\nSchiff base\ndeprotonated", token="channel"),
    dict(text="N 560", token="enzyme"),
    dict(text="O 640\nall-trans", token="rna"),
]
labels = ["hν, ~3 ps", "~1 μs", "~50 μs\nSB → Asp85;\nH⁺ released outside", "~1–5 ms\nAsp96 → SB",
          "~5 ms\nH⁺ taken up\nfrom inside", "~5–10 ms\nAsp85 → release group"]
ecology.cycle(ax, (7.5, 4.5), 3.2, steps, start=90, clockwise=True, arrow_labels=labels, label_size="small",
              center_text="1 H⁺ pumped\nper photon")
