# Correspondence analysis biplots (scaling 1 and scaling 2) of a 3 sites by 5 species abundance table.
counts <- matrix(c(45, 10, 15, 0, 10,
                   25, 8, 10, 0, 3,
                   7, 15, 20, 14, 12), nrow = 3, byrow = TRUE,
                 dimnames = list(paste("Site", 1:3), paste("Sp", 1:5)))
P <- counts / sum(counts)
r <- rowSums(P)
cm <- colSums(P)
Q <- (P - outer(r, cm)) / sqrt(outer(r, cm))  # standardized residuals
sv <- svd(Q)
U <- sv$u[, 1:2]
s <- sv$d[1:2]
V <- sv$v[, 1:2]
sgn <- sign(V[4, ])  # orient axes so that species 4 has positive coordinates
U <- sweep(U, 2, sgn, "*")
V <- sweep(V, 2, sgn, "*")

A <- V / sqrt(cm)                     # species, scaling 1 (standard coordinates)
Frow <- sweep(U / sqrt(r), 2, s, "*") # sites, scaling 1 (principal coordinates)
B <- U / sqrt(r)                      # sites, scaling 2
G <- sweep(A, 2, s, "*")              # species, scaling 2
# MASS::corresp(counts, nf = 2) returns the standard coordinates U / sqrt(r) and V / sqrt(c) as well.

inertia <- 100 * s[1]^2 / sum(sv$d^2)
par(mfrow = c(1, 2))
for (case in list(list(rows = Frow, cols = A, title = "Scaling 1: sites at chi-square distances"),
                  list(rows = B, cols = G, title = "Scaling 2: species at chi-square distances"))) {
  all_pts <- rbind(case$rows, case$cols)
  pad <- 0.15 * diff(range(all_pts))
  plot(all_pts, type = "n", xlim = range(all_pts[, 1]) + c(-pad, pad), ylim = range(all_pts[, 2]) + c(-pad, pad),
       xlab = sprintf("CA axis 1 (%.1f%% of inertia)", inertia), ylab = "CA axis 2", main = case$title, cex.main = 0.9)
  abline(h = 0, v = 0, col = "gray", lwd = 0.6)
  points(case$rows, pch = 19)
  text(case$rows, labels = rownames(counts), pos = 3, cex = 0.8)
  points(case$cols, pch = 15, col = "firebrick")
  text(case$cols, labels = colnames(counts), pos = 1, col = "firebrick", cex = 0.8)
}
