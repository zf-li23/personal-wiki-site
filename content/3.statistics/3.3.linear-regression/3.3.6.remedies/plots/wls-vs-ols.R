# Sampling distributions of OLS and WLS estimates when the error SD is proportional to X.
set.seed(0)
x <- 1:100
X <- cbind(1, x)
w <- 1 / x^2
reps <- 4000
ols <- matrix(NA_real_, reps, 2)
wls <- matrix(NA_real_, reps, 2)
for (r in 1:reps) {
  y <- 30 + 100 * x + 10 * x * rnorm(length(x))
  # lm.fit / lm.wfit are the fast workhorses behind lm(y ~ x) and lm(y ~ x, weights = w)
  ols[r, ] <- lm.fit(X, y)$coefficients
  wls[r, ] <- lm.wfit(X, y, w)$coefficients
}

params <- c("intercept b0", "slope b1")
truth <- c(30, 100)
op <- par(mfrow = c(1, 2), oma = c(0, 0, 2, 0))
for (j in 1:2) {
  d_ols <- density(ols[, j])
  d_wls <- density(wls[, j])
  lims <- quantile(c(ols[, j], wls[, j]), c(0.002, 0.998))
  plot(d_wls, xlim = lims, ylim = c(0, max(d_ols$y, d_wls$y)), col = "firebrick", lwd = 2,
       xlab = "estimate", main = sprintf("%s: true value %g", params[j], truth[j]))
  lines(d_ols, col = "steelblue", lwd = 2)
  abline(v = truth[j], lty = 2, col = "gray40")
  legend("topright", bty = "n", cex = 0.8, lwd = 2, col = c("steelblue", "firebrick"),
         legend = c(sprintf("OLS, SD = %.2f", sd(ols[, j])),
                    sprintf("WLS (w = 1/X^2), SD = %.2f", sd(wls[, j]))))
}
mtext("Y = 30 + 100 X + 10 X eps, 4000 simulated data sets: both unbiased, WLS far more precise",
      outer = TRUE, cex = 0.85)
par(op)
