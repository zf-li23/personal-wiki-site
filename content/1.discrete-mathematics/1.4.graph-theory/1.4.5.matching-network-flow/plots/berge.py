# Proof of Berge's theorem: in the symmetric difference of two matchings M (blue) and M' (red)
# every vertex has degree at most 2, so the components are alternating even cycles and
# alternating paths; a path with more red than blue edges is augmenting for M.
import wikigraph as G

pos = {"a": (0, 0), "b": (1.4, 0), "c": (1.4, 1.4), "d": (0, 1.4),
       "p1": (2.6, 0), "p2": (3.6, 1.4), "p3": (4.6, 0), "p4": (5.6, 1.4),
       "q1": (6.8, 0), "q2": (6.8, 1.4)}
M = [("a", "b"), ("c", "d"), ("p2", "p3"), ("q1", "q2")]
M2 = [("b", "c"), ("d", "a"), ("p1", "p2"), ("p3", "p4"), ("q1", "q2")]
both = [e for e in M if e in M2]
fig, (left, right) = G.panels(2, 6.8, 1.4, titles=["M (blue) and M' (red)", "$M \\oplus M'$"])
hl = {e: G.BLUE for e in M} | {e: G.RED for e in M2 if e not in both} | {e: G.VIOLET for e in both}
G.draw(left, pos, M + [e for e in M2 if e not in both], highlight=hl, labels=False)
xor = [e for e in M + M2 if e not in both]
G.draw(right, pos, xor, highlight={e: hl[e] for e in xor}, labels=False)
G.caption(right, (0.7, -0.45), "even cycle", size=9)
G.caption(right, (4.1, -0.45), "augmenting path for M", size=9)
G.caption(left, (6.8, -0.45), "in both", size=9)
