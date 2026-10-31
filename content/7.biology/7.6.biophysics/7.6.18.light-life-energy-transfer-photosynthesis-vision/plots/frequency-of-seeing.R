# The Hecht-Shlaer-Pirenne analysis of the absolute threshold of vision (base R).
# P_see(n) = P(Poisson(alpha n) >= K): frequency-of-seeing curves, a simulated observer fitted by maximum
# likelihood for several K, and the hit / false-alarm trade-off caused by dark noise.
set.seed(0)
op <- par(mfrow = c(1, 3), mar = c(4.2, 4.2, 2.2, 1))

# A: curves for K = 1..10
x <- 10^seq(-1, 2, length.out = 400)
cols <- hcl.colors(10, "viridis")
plot(NA, xlim = c(-1, 2), ylim = c(0, 1), xlab = "log10 mean number absorbed", ylab = "probability of seeing",
     main = "A  Steepness reveals K")
for (K in 1:10) lines(log10(x), ppois(K - 1, x, lower.tail = FALSE), col = cols[K], lwd = 1.5)

# B: simulated observer and maximum-likelihood fit of alpha for given K
alpha_true <- 0.06; K_true <- 6
n <- c(40, 60, 80, 100, 140, 200, 300); trials <- 50
seen <- rbinom(length(n), trials, ppois(K_true - 1, alpha_true * n, lower.tail = FALSE))
plot(log10(n), seen / trials, pch = 19, ylim = c(0, 1.1), xlab = "log10 mean photons at the cornea",
     ylab = "fraction of flashes seen", main = "B  Fitting the curve")
xx <- 10^seq(1.3, 2.7, length.out = 300)
for (K in c(2, 6, 10)) {
  nll <- function(la) -sum(seen * ppois(K - 1, exp(la) * n, lower.tail = FALSE, log.p = TRUE) +
                           (trials - seen) * ppois(K - 1, exp(la) * n, log.p = TRUE))
  fit <- optimize(nll, c(log(1e-3), log(1)))
  lines(log10(xx), ppois(K - 1, exp(fit$minimum) * xx, lower.tail = FALSE), lwd = 1.5,
        lty = match(K, c(2, 6, 10)))
  cat(sprintf("K = %2d  alpha = %.3f  -logL = %.1f\n", K, exp(fit$minimum), fit$objective))
}

# C: dark noise in the summation pool (mean 0.6 events) and a 6-photon signal
d <- 0.6; s <- 6; Ks <- 1:12
plot(Ks, ppois(Ks - 1, d + s, lower.tail = FALSE), log = "y", type = "b", pch = 19, ylim = c(1e-8, 1),
     xlab = "criterion K", ylab = "probability", main = "C  Hits and false alarms")
lines(Ks, ppois(Ks - 1, d, lower.tail = FALSE), type = "b", pch = 15, lty = 2)
legend("bottomleft", c("hit", "false alarm"), pch = c(19, 15), lty = c(1, 2), bty = "n")
par(op)
