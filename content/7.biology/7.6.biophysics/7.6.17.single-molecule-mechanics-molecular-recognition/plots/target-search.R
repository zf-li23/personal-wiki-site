# Facilitated diffusion: search time against the fraction of time bound to DNA (base R).
M <- 4.6e6; b <- 0.34; tau3 <- 1e-3            # bp, nm per bp, s
tsearch <- function(tau1, D1) {                  # D1 in nm^2/s
  n <- pmax(sqrt(8 * D1 * tau1 / pi) / b, 1)     # new base pairs scanned per round
  M / n * (tau1 + tau3)
}
f <- seq(0.005, 0.995, length.out = 400)
tau1 <- f / (1 - f) * tau3
D1s <- c(0.01, 0.046, 0.2) * 1e6
plot(NA, xlim = c(0, 1), ylim = c(30, 1e4), log = "y", xlab = "fraction of time bound nonspecifically",
     ylab = "search time / s")
for (i in seq_along(D1s)) {
  lines(f, tsearch(tau1, D1s[i]), col = i, lwd = 2)
  points(0.5, tsearch(tau3, D1s[i]), col = i, pch = 19)
}
abline(h = M * tau3, lty = 3)
legend("top", legend = sprintf("D1 = %g um^2/s", D1s / 1e6), col = 1:3, lwd = 2, bty = "n")
# the optimum: minimize (tau1 + tau3) / sqrt(tau1)
opt <- optimize(function(t) tsearch(t, 0.046e6), c(1e-5, 1e-1), log = FALSE)
cat(sprintf("optimal tau1 = %.2e s (tau3 = %.0e s), search time = %.0f s\n", opt$minimum, tau3, opt$objective))
