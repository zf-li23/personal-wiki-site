# Thermodynamic uncertainty relation: Q = Var(J) * sigma / <J>^2 (in kB) for random four-state networks,
# from the scaled cumulant generating function (largest eigenvalue of the tilted generator),
# compared with the one-state motor x coth(x/2) and the bound Q = 2.
set.seed(0)
n <- 4
edges <- t(combn(n, 2))
scgf <- function(W, d, s) {
  Ls <- W * exp(s * d)
  diag(Ls) <- -colSums(W)
  max(Re(eigen(Ls, only.values = TRUE)$values))
}
stationary <- function(W) {
  L <- W; diag(L) <- -colSums(W)
  A <- rbind(L, rep(1, n))
  qr.solve(A, c(rep(0, n), 1))
}
res <- t(replicate(3000, {
  W <- matrix(0, n, n)
  for (k in seq_len(nrow(edges))) {
    i <- edges[k, 1]; j <- edges[k, 2]
    W[j, i] <- 10^runif(1, -2, 2); W[i, j] <- 10^runif(1, -2, 2)
  }
  d <- matrix(0, n, n); d[2, 1] <- 1; d[1, 2] <- -1   # net jumps 1 -> 2
  h <- 1e-3
  lp <- scgf(W, d, h); lm <- scgf(W, d, -h)
  m <- (lp - lm) / (2 * h); v <- (lp + lm) / h^2
  p <- stationary(W)
  sig <- 0
  for (k in seq_len(nrow(edges))) {
    i <- edges[k, 1]; j <- edges[k, 2]
    a <- W[j, i] * p[i]; b <- W[i, j] * p[j]
    sig <- sig + (a - b) * log(a / b)
  }
  c(x = sig / abs(m), Q = v * sig / m^2)
}))
res <- res[is.finite(res[, "Q"]) & res[, "x"] > 0, ]
cat("minimum Q over random networks:", min(res[, "Q"]), "\n")
plot(res[, "x"], res[, "Q"], log = "xy", pch = 16, cex = 0.3, col = rgb(0.4, 0.3, 0.7, 0.4),
     xlim = c(1e-2, 1e3), ylim = c(1, 1e4),
     xlab = "entropy produced per unit current", ylab = "uncertainty product Q")
x <- 10^seq(-2, 3, length.out = 300)
lines(x, x / tanh(x / 2), col = "firebrick", lwd = 2)
abline(h = 2, lty = 2)
legend("topleft", c("random networks", "one-state motor", "TUR bound"),
       pch = c(16, NA, NA), lty = c(NA, 1, 2), col = c("slateblue", "firebrick", "black"), bty = "n")
