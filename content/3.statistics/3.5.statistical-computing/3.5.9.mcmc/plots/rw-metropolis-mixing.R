# Random walk Metropolis for the N(0, 1) target with uniform proposals on (x - a, x + a):
# trace plots and autocorrelations for three window half-widths.
set.seed(0)
rwm <- function(a, n = 2000, x0 = 10) {
  X <- numeric(n); X[1] <- x0; acc <- 0
  for (t in 1:(n - 1)) {
    x <- X[t]
    y <- x + (2 * runif(1) - 1) * a
    if (runif(1) < exp((x^2 - y^2) / 2)) {
      X[t + 1] <- y; acc <- acc + 1
    } else {
      X[t + 1] <- x
    }
  }
  list(chain = X, rate = acc / (n - 1))
}

par(mfrow = c(3, 2))
burn <- 200
for (a in c(0.1, 2.5, 30)) {
  fit <- rwm(a)
  plot(fit$chain, type = "l", xlab = "iteration t", ylab = "X_t",
       main = sprintf("a = %g: acceptance rate %.2f", a, fit$rate))
  abline(v = burn, lty = 3)
  acf(fit$chain[-(1:burn)], lag.max = 40, main = sprintf("ACF after burn-in, a = %g", a))
}
