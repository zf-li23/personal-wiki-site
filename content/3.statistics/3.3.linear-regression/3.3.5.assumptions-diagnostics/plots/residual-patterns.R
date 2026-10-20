# Typical residual plots: no problem, nonlinearity, nonconstant variance, dependence over time.
set.seed(0)
op <- par(mfrow = c(2, 2))

x <- 1:30
y <- 30 + 5 * x + 25 * rnorm(length(x))
plot(x, residuals(lm(y ~ x)), pch = 19, col = "steelblue", xlab = "X", ylab = "residual e_i",
     main = "(a) no violation: a horizontal band")
abline(h = 0, col = "gray50")

y <- x^2 - 10 * x + 30 + 25 * rnorm(length(x))
plot(x, residuals(lm(y ~ x)), pch = 19, col = "darkorange", xlab = "X", ylab = "residual e_i",
     main = "(b) nonlinearity: Y = X^2 - 10X + 30 + error")
abline(h = 0, col = "gray50")

x2 <- 1:100
y2 <- 30 + 100 * x2 + 10 * x2 * rnorm(length(x2))
plot(x2, residuals(lm(y2 ~ x2)), pch = 19, cex = 0.8, col = "forestgreen", xlab = "X", ylab = "residual e_i",
     main = "(c) nonconstant variance: SD of error = 10X")
abline(h = 0, col = "gray50")

# AR(1) errors: eps_t = 0.85 eps_{t-1} + u_t
u <- rnorm(40)
eps <- as.numeric(stats::filter(u, 0.85, method = "recursive"))
xt <- runif(40, 0, 10)
yt <- 2 + 0.5 * xt + eps
plot(1:40, residuals(lm(yt ~ xt)), type = "o", pch = 19, cex = 0.8, col = "purple",
     xlab = "time order", ylab = "residual e_i", main = "(d) dependence: AR(1) errors, rho = 0.85")
abline(h = 0, col = "gray50")
par(op)
