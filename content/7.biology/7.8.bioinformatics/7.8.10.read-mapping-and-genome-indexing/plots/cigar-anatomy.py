# Anatomy of an alignment record. A read of 30 nt aligned to a reference from one-based position 101:
# its first 3 bases are soft-clipped (adapter remnant, kept in the record but not aligned), then 8
# aligned bases with one mismatch, an insertion of 2 bases in the read, 7 aligned bases, a deletion of
# 2 reference bases and 10 aligned bases. The CIGAR string 3S8M2I7M2D10M and the tags NM:i:5 (edit
# distance: 1 mismatch + 2 inserted + 2 deleted bases) and MD:Z:5A9^AG10 follow from the drawing.
import wikibio as bio

P = bio.P
ref = "TTGACCTGAGCATTCGATAGGCATGACTTACGGATCA"
#      ^ ref index 0 corresponds to position 98
ops = [("S", 3), ("M", 8), ("I", 2), ("M", 7), ("D", 2), ("M", 10)]
seg1 = ref[3:11]
seg1 = seg1[:5] + "T" + seg1[6:]          # one mismatch (reference A at position 106)
read = "gtc".upper() + seg1 + "GG" + ref[11:18] + ref[20:30]
ref_start = 3   # read's first aligned base is ref[3] = position 101
# build aligned rows
top, bot, ops_row = [], [], []
ri, qi = ref_start, 0
cols = []
for op, n in ops:
    for _ in range(n):
        if op == "S":
            cols.append((" ", read[qi], "S")); qi += 1
        elif op == "M":
            cols.append((ref[ri], read[qi], "M")); ri += 1; qi += 1
        elif op == "I":
            cols.append(("-", read[qi], "I")); qi += 1
        elif op == "D":
            cols.append((ref[ri], "-", "D")); ri += 1
assert qi == len(read)
# MD and NM from the drawing
md, run, nm = "", 0, 0
prev_del = False
for r, q, o in cols:
    if o == "M":
        if r == q:
            run += 1
        else:
            md += f"{run}{r}"; run = 0; nm += 1
        prev_del = False
    elif o == "D":
        if not prev_del:
            md += f"{run}^"; run = 0
        md += r; nm += 1; prev_del = True
    elif o == "I":
        nm += 1
md += str(run)
cigar = "".join(f"{n}{o}" for o, n in ops)
print(cigar, "NM", nm, "MD", md)

fig, ax = bio.canvas(24.0, 7.5)
cw = 0.52
x0 = 1.0
yR, yQ, yO = 5.2, 4.2, 3.2
bio.label(ax, (x0 - 0.2, yR + 1.0), "reference (one-based position)", size="small", ha="left", color=P.muted())
for j, (r, q, o) in enumerate(cols):
    x = x0 + (j + 3.5) * cw
    if r.strip():
        bio.label(ax, (x, yR), r, size="small", color=P.NUCLEOTIDE.get(r, P.ink()))
    if o == "S":
        bio.label(ax, (x, yQ), q.lower(), size="small", color=P.muted())
    elif q != "-":
        mism = o == "M" and q != r
        bio.label(ax, (x, yQ), q, size="small", bold=mism or o == "I", color=P.NUCLEOTIDE.get(q, P.ink()))
    else:
        bio.label(ax, (x, yQ), "-", size="small", color=P.muted())
# leading reference bases before the read
for j in range(3):
    bio.label(ax, (x0 + (j + 3.5) * cw, yR), ref[j], size="small", color=P.NUCLEOTIDE.get(ref[j]))
# position ticks
pos = 98
j_ref = 0
xs_ref = []
for j in range(3):
    xs_ref.append(x0 + (j + 3.5) * cw)
for j, (r, q, o) in enumerate(cols):
    if o != "S" and r.strip() and r != "-":
        xs_ref.append(x0 + (j + 3.5) * cw)
for k_, x in enumerate(xs_ref):
    p = 98 + k_
    if p % 5 == 0 or p == 101:
        bio.label(ax, (x, yR + 0.55), str(p), size="tiny", color=P.muted())
# operation row with brackets
j = 0
for o, n in ops:
    xa = x0 + (j + 3.5) * cw - cw / 2
    xb = xa + n * cw
    ax.plot([xa + 0.05, xb - 0.05], [yO + 0.25, yO + 0.25], color=P.muted(), lw=1.0)
    bio.label(ax, ((xa + xb) / 2, yO - 0.15), f"{n}{o}", size="small", bold=True)
    j += n
bio.label(ax, (x0 - 0.2, yQ), "read", size="small", ha="right", color=P.muted())
bio.label(ax, (12.0, 1.9), f"POS = 101   CIGAR = {cigar}   NM:i:{nm}   MD:Z:{md}", size="normal")
bio.label(ax, (12.0, 1.0), "S: soft clip (in SEQ, not aligned)   M: aligned (match or mismatch)   "
          "I: inserted in read   D: deleted from read", size="small", color=P.muted())
bio.label(ax, (12.0, 0.3), "aligned span on the reference = 8 + 7 + 2 + 10 = 27 bases: positions 101-127",
          size="small", color=P.muted())
