# Translocation ratchet: perfect and reversible-binding force-velocity curves (base R).
# Units d = 1, D = 1, kBT = 1; w = F d / kBT.
v_perfect <- function(w) ifelse(abs(w) < 1e-6, 2, w^2 / (exp(w) - w - 1))
v_reversible <- function(w, G, n = 300) {
  x <- (seq_len(n) - 0.5) / n
  X <- outer(x, rep(1, n)); Y <- outer(rep(1, n), x)
  dV <- w * Y - G * (floor(X + Y) - floor(X))      # staircase potential F x - G floor(x)
  (1 - exp(-(G - w))) / mean(exp(dV))
}
w <- seq(-1, 8, length.out = 200)
plot(w, v_perfect(w), type = "l", lwd = 2, ylim = c(-1, 3.2),
     xlab = "load w = F d / kBT", ylab = "velocity / (D/d)")
cols <- c(3, 4, 2); cK <- c(100, 10, 1)
for (i in 1:3) {
  G <- log(1 + cK[i])
  lines(w, sapply(w, v_reversible, G = G), col = cols[i], lwd = 2)
  cat(sprintf("c/Kd = %g: stall at w = %.2f\n", cK[i], G))
}
abline(h = 0, lty = 3)
legend("topright", c("perfect", paste("c/Kd =", cK)), col = c(1, cols), lwd = 2, bty = "n")
