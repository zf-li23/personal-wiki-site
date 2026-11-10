# Normal approximation to the binomial distribution: one example and the error against np.
par(mfrow = c(1, 2))
n <- 20; p <- 0.2; k <- 0:12
mu <- n * p; s <- sqrt(n * p * (1 - p))
b <- barplot(dbinom(k, n, p), names.arg = k, col = "lightblue", border = NA,
             xlab = "number of successes k", ylab = "probability", main = "n = 20, p = 0.2")
points(b, pnorm(k + 0.5, mu, s) - pnorm(k - 0.5, mu, s), col = "red", pch = 19)

maxerr <- function(n, p) {
  k <- 0:n
  max(abs(pbinom(k, n, p) - pnorm(k + 0.5, n * p, sqrt(n * p * (1 - p)))))
}
nps <- 1:20; ps <- c(0.5, 0.2, 0.05); cols <- c("steelblue", "darkorange", "forestgreen")
plot(NA, xlim = range(nps), ylim = c(0, 0.13), xlab = "np", ylab = "max CDF error",
     main = "Continuity-corrected approximation")
for (j in 1:3) lines(nps, sapply(nps, function(m) maxerr(round(m / ps[j]), ps[j])),
                     type = "b", pch = 19, cex = 0.6, col = cols[j])
abline(v = 5, lty = 2, col = "gray")
legend("topright", paste("p =", ps), col = cols, lwd = 2, bty = "n")

# The table of errors in the text: point probabilities, p = 0.2
for (n in c(15, 20, 25, 30, 35)) {
  k <- 0:n; e <- abs(dbinom(k, n, 0.2) - (pnorm(k + 0.5, n * 0.2, sqrt(n * 0.16)) -
                                           pnorm(k - 0.5, n * 0.2, sqrt(n * 0.16))))
  cat(n, round(mean(e), 6), round(max(e), 5), "\n")
}
