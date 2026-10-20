# One case with high leverage and a large residual: the fit with and without it, and Cook's distances.
set.seed(0)
n <- 25
x <- c(runif(n - 1, 0, 10), 18)
y <- 2 + 0.5 * x + rnorm(n)
y[n] <- 2 + 0.5 * 18 - 6

fit <- lm(y ~ x)
fit_del <- lm(y[-n] ~ x[-n])
h <- hatvalues(fit)
D <- cooks.distance(fit)
summary(influence.measures(fit))   # prints the cases flagged by DFFITS, DFBETAS, Cook's D and leverage

op <- par(mfrow = c(1, 2))
plot(x[-n], y[-n], pch = 19, col = "steelblue", xlim = c(0, 19), ylim = range(y), xlab = "X", ylab = "Y")
points(x[n], y[n], pch = 15, cex = 1.4, col = "firebrick")
abline(fit, col = "firebrick", lwd = 2)
abline(coef(fit_del), col = "forestgreen", lwd = 2, lty = 2)
legend("topleft", bty = "n", cex = 0.8, pch = c(15, NA, NA), lty = c(NA, 1, 2),
       col = c("firebrick", "firebrick", "forestgreen"),
       legend = c(sprintf("case %d: h = %.2f", n, h[n]), "fit with all cases", sprintf("fit without case %d", n)))

plot(1:n, D, type = "h", lwd = 2, col = "steelblue", xlab = "case number", ylab = "Cook's distance")
abline(h = 4 / n, lty = 2, col = "darkorange")
legend("topleft", bty = "n", cex = 0.8, lty = 2, col = "darkorange", legend = "cutoff 4/n")
par(op)
