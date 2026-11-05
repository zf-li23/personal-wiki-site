# Root systems. Right: taproot system, a dominant primary root (from the radicle) with successively finer
# lateral roots (gymnosperms, most eudicots). Left: fibrous root system, many adventitious roots of similar
# thickness from the stem base (monocots). Template after a Wikimedia Commons diagram.
import wikibio as bio
from wikibio import plantmorph as PM

fig, ax = bio.canvas(20.0, 12.6)
s = PM.specimen(ax, "wikimedia/root-systems", at=(10.0, 6.0), height=11.0,
                labels=[dict(part="taproot", text="Taproot (primary root)", side="right"),
                        dict(part="lateral-root", text="Lateral root", side="right"),
                        dict(part="fibrous-root", text="Adventitious roots", side="left"),
                        dict(part="soil", text="Soil surface", side="left")])
b = s["box"]
bio.label(ax, (b[0] + 0.33 * b[2], 11.7), "Fibrous root system", size="normal", bold=True)
bio.label(ax, (b[0] + 0.8 * b[2], 11.7), "Taproot system", size="normal", bold=True)
