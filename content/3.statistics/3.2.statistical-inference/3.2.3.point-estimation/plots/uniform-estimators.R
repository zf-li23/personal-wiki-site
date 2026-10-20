# Bias, variance and MSE of three estimators of beta for U(0, beta), estimated by simulation.
set.seed(0)
beta <- 2
reps <- 5000
ns <- seq(5, 200, by = 5)
est_names <- c("2 * mean (moment)", "X_(n) (MLE)", "(n+1)/n * X_(n)")
res <- array(0, dim = c(length(ns), 3, 3),
             dimnames = list(NULL, est_names, c("bias", "var", "mse")))
for (i in seq_along(ns)) {
  n <- ns[i]
  x <- matrix(runif(reps * n, 0, beta), reps, n)
  xmax <- apply(x, 1, max)
  ests <- cbind(2 * rowMeans(x), xmax, (n + 1) / n * xmax)
  res[i, , "bias"] <- colMeans(ests) - beta
  res[i, , "var"] <- apply(ests, 2, function(e) mean((e - mean(e))^2))
  res[i, , "mse"] <- colMeans((ests - beta)^2)
}

cols <- c("steelblue", "darkorange", "darkgreen")
titles <- c(bias = "bias", var = "variance", mse = "mean squared error")
op <- par(mfrow = c(1, 3))
for (key in names(titles)) {
  matplot(ns, res[, , key], type = "l", lty = 1, lwd = 1.8, col = cols,
          log = if (key == "bias") "" else "y",
          xlab = "sample size n", ylab = "", main = titles[[key]])
  if (key == "bias") {
    abline(h = 0, col = "grey50", lwd = 0.8)
    legend("bottomright", bty = "n", cex = 0.8, legend = est_names, col = cols, lwd = 1.8)
  }
}
par(op)
