# Two-sample t-test: null and alternative distributions, and power against n.
alpha <- 0.05
par(mfrow = c(1, 2))

n <- 10; d <- 1.2; df <- 2 * n - 2
ncp <- d / sqrt(2 / n); cval <- qt(1 - alpha / 2, df)
x <- seq(-4.5, 8, length.out = 800)
f0 <- dt(x, df); f1 <- dt(x, df, ncp = ncp)
pw <- pt(cval, df, ncp = ncp, lower.tail = FALSE) + pt(-cval, df, ncp = ncp)
plot(x, f0, type = "l", lwd = 2, col = "steelblue", ylim = c(0, max(f0)), xlab = "t statistic",
     ylab = "density", main = sprintf("n = 10 per group, d = 1.2: power = %.2f", pw), cex.main = 0.9)
lines(x, f1, lwd = 2, col = "firebrick")
abline(v = c(-cval, cval), lty = 2, col = "gray")
# Same power from power.t.test
power.t.test(n = 10, delta = 1.2, sd = 1, strict = TRUE)

ns <- 2:60
plot(NA, xlim = range(ns), ylim = c(0, 1), xlab = "n per group", ylab = "power",
     main = "Power curves, two-sided two-sample t-test", cex.main = 0.9)
cols <- c("steelblue", "darkorange", "forestgreen")
ds <- c(0.5, 1, 1.5)
for (k in 1:3) {
  p <- sapply(ns, function(m) power.t.test(n = m, delta = ds[k], sd = 1, strict = TRUE)$power)
  lines(ns, p, lwd = 2, col = cols[k])
}
abline(h = 0.8, lty = 3, col = "gray")
legend("bottomright", paste("d =", ds), col = cols, lwd = 2, bty = "n")
