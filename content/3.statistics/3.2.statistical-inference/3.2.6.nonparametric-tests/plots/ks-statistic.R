# Empirical distribution function of a sample versus a hypothesized normal CDF, with the KS statistic marked.
set.seed(0)
x <- sort(rnorm(30, mean = 0.5, sd = 1))   # true distribution N(0.5, 1)
n <- length(x)
f0 <- pnorm(x)                             # hypothesized F0 = N(0, 1)

# KS statistic: largest gap just after or just before a jump of F_n
upper <- (1:n) / n - f0
lower <- f0 - (0:(n - 1)) / n
iu <- which.max(upper)
il <- which.max(lower)
if (upper[iu] >= lower[il]) {
  xk <- x[iu]; y_emp <- iu / n; y_0 <- f0[iu]
} else {
  xk <- x[il]; y_emp <- (il - 1) / n; y_0 <- f0[il]
}
d <- abs(y_emp - y_0)
test <- ks.test(x, "pnorm")   # the same D_n, with its p-value

grid <- seq(-3, 4, length.out = 400)
plot(ecdf(x), do.points = FALSE, verticals = TRUE, col = "darkorange", lwd = 1.8,
     xlim = c(-3, 4), ylim = c(-0.02, 1.02), xlab = "x", ylab = "cumulative probability",
     main = sprintf("KS test against N(0, 1): p = %.3f", test$p.value))
lines(grid, pnorm(grid), col = "steelblue", lwd = 2)
arrows(xk, y_0, xk, y_emp, code = 3, length = 0.06, col = "firebrick", lwd = 1.8)
text(xk + 0.12, (y_emp + y_0) / 2, sprintf("D_n = %.3f", d), adj = 0, col = "firebrick")
legend("topleft", bty = "n", cex = 0.8,
       legend = c("hypothesized F_0 = N(0,1)", "empirical F_n (n = 30)"),
       col = c("steelblue", "darkorange"), lwd = c(2, 1.8))
