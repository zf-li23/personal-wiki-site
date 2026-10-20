# Nonlinear regression: the conditional mean E(X | Y = y) versus the best linear predictor (least squares line).
set.seed(0)
n <- 1500
y <- runif(n, -2, 2)
m <- sin(1.5 * y) + 0.3 * y^2
x <- m + rnorm(n, 0, 0.35)
fit <- lm(x ~ y)   # slope Cov(Y, X) / Var(Y), intercept mean(x) - slope * mean(y)

grid <- seq(-2, 2, length.out = 400)
plot(y, x, pch = 19, cex = 0.4, col = adjustcolor("steelblue", 0.3), xlab = "y", ylab = "x",
     main = "conditional expectation as the best mean-square prediction")
lines(grid, sin(1.5 * grid) + 0.3 * grid^2, col = "firebrick", lwd = 2.2)
abline(fit, col = "darkorange", lwd = 1.8, lty = 2)
legend("topleft", bty = "n", cex = 0.8, pch = c(19, NA, NA), lty = c(NA, 1, 2),
       col = c("steelblue", "firebrick", "darkorange"),
       legend = c("sample of (Y, X)", "E(X | Y = y): best predictor", "best linear predictor"))
