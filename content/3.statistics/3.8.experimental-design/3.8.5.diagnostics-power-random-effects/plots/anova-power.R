# Power of the one-way ANOVA F-test from the noncentral F-distribution, etching example.
a <- 4; sigma <- 25
means <- c(575, 600, 650, 675); tau <- means - mean(means)
pow <- function(n, ss_tau, alpha) {
  lam <- n * ss_tau / sigma^2; df2 <- a * (n - 1)
  pf(qf(1 - alpha, a - 1, df2), a - 1, df2, ncp = lam, lower.tail = FALSE)
}
n <- seq(2, 8, length.out = 200)
op <- par(mfrow = c(1, 2))
plot(n, pow(n, sum(tau^2), 0.05), type = "l", ylim = c(0, 1), col = "steelblue",
     xlab = "replicates per level n", ylab = "power", main = "Power of the F-test")
lines(n, pow(n, sum(tau^2), 0.01), lty = 2, col = "steelblue")
lines(n, pow(n, 75^2 / 2, 0.05), col = "darkorange")
lines(n, pow(n, 75^2 / 2, 0.01), lty = 2, col = "darkorange")
abline(h = 0.9, col = "gray")
power.anova.test(groups = 4, between.var = var(means), within.var = sigma^2,
                 sig.level = 0.01, power = 0.90)          # n = 3.52
x <- seq(0.01, 14, length.out = 400); crit <- qf(0.99, 3, 12)
plot(x, df(x, 3, 12), type = "l", xlab = "F", ylab = "density",
     main = "Null and alternative, n = 4")
lines(x, df(x, 3, 12, ncp = 4 * sum(tau^2) / sigma^2), col = "darkorange")
abline(v = crit, lty = 2)
par(op)
