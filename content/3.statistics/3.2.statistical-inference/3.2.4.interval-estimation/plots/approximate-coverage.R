# Coverage of approximate and exact 95% confidence intervals.
z <- qnorm(0.975)
op <- par(mfrow = c(1, 2))

# Bernoulli proportion: exact coverage of the Wald and Wilson intervals,
# summing binomial probabilities over the outcomes whose interval contains theta
theta <- 0.03
ns <- 20:500
cover <- t(sapply(ns, function(n) {
  k <- 0:n
  p <- dbinom(k, n, theta)
  ph <- k / n
  half <- z * sqrt(ph * (1 - ph) / n)
  centre <- (ph + z^2 / (2 * n)) * n / (n + z^2)
  hw <- n / (n + z^2) * z * sqrt(ph * (1 - ph) / n + z^2 / (4 * n^2))
  c(wald = sum(p[ph - half <= theta & theta <= ph + half]),
    wilson = sum(p[centre - hw <= theta & theta <= centre + hw]))
}))
matplot(ns, cover, type = "l", lty = 1, lwd = 1, col = c("steelblue", "darkorange"),
        ylim = c(0.5, 1), xlab = "sample size n", ylab = "coverage probability",
        main = "Bernoulli, theta = 0.03")
abline(h = 0.95, lty = 2, col = "grey50")
legend("bottomright", bty = "n", legend = c("Wald", "Wilson"),
       col = c("steelblue", "darkorange"), lwd = 1)

# Exponential mean: simulated coverage of the approximate and the exact interval
set.seed(0)
reps <- 4000
ns2 <- c(5, 10, 15, 20, 30, 40, 60, 80, 100, 150, 200, 300)
cover2 <- t(sapply(ns2, function(n) {
  xbar <- rowMeans(matrix(rexp(reps * n, rate = 1), reps, n))
  lo <- 2 * n * xbar / qchisq(0.975, 2 * n)
  hi <- 2 * n * xbar / qchisq(0.025, 2 * n)
  c(approx = mean(abs(xbar - 1) <= z * xbar / sqrt(n)),
    exact = mean(lo <= 1 & 1 <= hi))
}))
matplot(ns2, cover2, type = "o", lty = 1, pch = c(19, 15), cex = 0.7,
        col = c("steelblue", "darkorange"), log = "x", ylim = c(0.85, 1),
        xlab = "sample size n", ylab = "", main = "Exponential mean, theta = 1")
abline(h = 0.95, lty = 2, col = "grey50")
legend("bottomright", bty = "n", cex = 0.8,
       legend = c("x_bar +- z x_bar / sqrt(n)", "exact chi-square interval"),
       col = c("steelblue", "darkorange"), pch = c(19, 15), lty = 1)
par(op)
