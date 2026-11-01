# The Burrows-Wheeler transform of T = acaacg$ and the backward search for P = aac. A: the sorted
# rotations of T (the Burrows-Wheeler matrix) with the suffix array SA, the first column F and the last
# column L = BWT(T) = gc$aaac. B-D: backward search processes P from its last letter; each step maps the
# current interval of rows [sp, ep) through sp <- C[c] + Occ(c, sp), ep <- C[c] + Occ(c, ep), and the
# shaded rows are those whose rotations start with the suffix of P processed so far.
import wikibio as bio

P = bio.P
T = "acaacg$"
n = len(T)
sa = sorted(range(n), key=lambda i: T[i:])
rows = [T[i:] + T[:i] for i in sa]
L = "".join(r[-1] for r in rows)
C = {}
tot = 0
for c in sorted(set(T)):
    C[c] = tot
    tot += T.count(c)


def occ(c, i):
    return L[:i].count(c)


steps = []
sp, ep = 0, n
pat = "aac"
done = ""
for c in reversed(pat):
    sp, ep = C[c] + occ(c, sp), C[c] + occ(c, ep)
    done = c + done
    steps.append((done, sp, ep))

fig, ax = bio.canvas(30.0, 10.5)
cw, rh = 0.62, 0.95
top = 8.6


def matrix(x0, title, shade=None, show_sa=False):
    bio.label(ax, (x0 + 3.5 * cw, top + 1.25), title, size="small", bold=True)
    if show_sa:
        bio.label(ax, (x0 - 1.3, top + 0.55), "i", size="tiny", color=P.muted())
        bio.label(ax, (x0 - 0.6, top + 0.55), "SA", size="tiny", color=P.muted())
    bio.label(ax, (x0 + 0.5 * cw, top + 0.55), "F", size="tiny", color=P.muted())
    bio.label(ax, (x0 + 6.5 * cw, top + 0.55), "L", size="tiny", color=P.muted())
    for r, row in enumerate(rows):
        y = top - (r + 0.5) * rh
        if shade and shade[0] <= r < shade[1]:
            bio.shape(ax, [(x0 - 0.05, y - rh / 2 + 0.05), (x0 + 7 * cw + 0.05, y - rh / 2 + 0.05),
                           (x0 + 7 * cw + 0.05, y + rh / 2 - 0.05), (x0 - 0.05, y + rh / 2 - 0.05)],
                      token="highlight", lw=0.6)
        if show_sa:
            bio.label(ax, (x0 - 1.3, y), str(r), size="tiny", color=P.muted())
            bio.label(ax, (x0 - 0.6, y), str(sa[r]), size="small")
        for j, ch in enumerate(row):
            bold = j in (0, n - 1)
            col = P.ink() if bold else P.muted()
            bio.label(ax, (x0 + (j + 0.5) * cw, y), ch, size="small", bold=bold, color=col)


matrix(2.0, "A  sorted rotations, BWT = gc$aaac", show_sa=True)
xs = [9.6, 16.2, 22.8]
for (done, sp_, ep_), x0 in zip(steps, xs):
    matrix(x0, f"{'BCD'[xs.index(x0)]}  suffix '{done}': [{sp_}, {ep_})", shade=(sp_, ep_))
    c = done[0]
    bio.label(ax, (x0 + 3.5 * cw, 1.1), f"C[{c}] = {C[c]}", size="tiny", color=P.muted())
bio.label(ax, (15.0, 0.25), "C[$] = 0, C[a] = 1, C[c] = 4, C[g] = 6;  Occ(c, i) = number of c in L[0:i]",
          size="small", color=P.muted())
