# Gibbs sampler for the standard bivariate normal with correlation rho.
set.seed(0)
gibbs <- function(rho, n, start = c(-3, 3)) {
  s <- sqrt(1 - rho^2)
  X <- matrix(NA, n + 1, 2); X[1, ] <- start
  for (t in 1:n) {
    x <- rnorm(1, rho * X[t, 2], s)   # X | Y = y ~ N(rho y, 1 - rho^2)
    y <- rnorm(1, rho * x, s)         # Y | X = x ~ N(rho x, 1 - rho^2)
    X[t + 1, ] <- c(x, y)
  }
  X
}

par(mfrow = c(1, 2))
X <- gibbs(0.9, 15)
plot(X, type = "b", pch = 20, asp = 1, xlab = "x", ylab = "y",
     main = "First 15 sweeps, rho = 0.9")   # sweep endpoints; each sweep moves x, then y
plot(gibbs(0.5, 1000)[, 1], type = "l", col = "steelblue", ylim = c(-4, 4),
     xlab = "sweep t", ylab = "X_t", main = "rho = 0.5 (blue) vs 0.99 (red)")
lines(gibbs(0.99, 1000)[, 1], col = "firebrick")
colMeans(gibbs(0.9, 5000)[-(1:500), ])   # both close to 0
