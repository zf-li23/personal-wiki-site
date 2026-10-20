# Likelihood functions: Bernoulli trials and the capture-recapture model.
op <- par(mfrow = c(1, 2))

# Bernoulli likelihood theta^t (1 - theta)^(n - t), rescaled to maximum 1
theta <- seq(0.001, 0.999, length.out = 999)
rel_lik <- function(n, t) {
  loglik <- t * log(theta) + (n - t) * log(1 - theta)
  exp(loglik - max(loglik))
}
plot(theta, rel_lik(10, 6), type = "l", lwd = 2, col = "steelblue", ylim = c(0, 1),
     xlab = "theta", ylab = "L(theta) / max L", main = "Bernoulli likelihood, MLE t/n = 0.6")
lines(theta, rel_lik(100, 60), lwd = 2, lty = 2, col = "darkorange")
g <- (1:9) / 10
points(g, g^6 * (1 - g)^4 / (0.6^6 * 0.4^4), pch = 19, col = "steelblue")
abline(v = 0.6, lty = 3, col = "grey50")
legend("topleft", bty = "n", cex = 0.8,
       legend = c("n = 10, t = 6", "n = 100, t = 60", "theta = 0.1, ..., 0.9"),
       col = c("steelblue", "darkorange", "steelblue"), lty = c(1, 2, NA), pch = c(NA, NA, 19))

# Capture-recapture: 10 tagged, 20 recaptured, 4 of them tagged;
# L(N) = C(10, 4) C(N - 10, 16) / C(N, 20) is a hypergeometric probability
N <- 26:120
lik <- dhyper(4, m = 10, n = N - 10, k = 20)
best <- N[lik >= max(lik) * (1 - 1e-9)]
plot(N, lik, type = "o", pch = 19, cex = 0.4, col = "darkgreen",
     xlab = "population size N", ylab = "L(N)",
     main = "Capture-recapture: 4 of 20 recaptured are tagged")
points(best, lik[N %in% best], pch = 19, cex = 1.3, col = "firebrick")
legend("topright", bty = "n", cex = 0.8, pch = 19, col = "firebrick",
       legend = paste("maximum at N =", paste(best, collapse = " and ")))
par(op)
