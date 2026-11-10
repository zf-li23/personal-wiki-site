# Regression through the origin when the true model has an intercept:
# rejection rates of the t-test for the slope and of the permutation test.
set.seed(1)
n <- 30; alpha <- 0.05; beta0 <- 1; nrep <- 500; nperm <- 199  # fewer replications than the Python version (R loops are slow)
betas <- seq(-1, 1, by = 0.2)   # betas[6] is the null value 0
tcrit <- qt(1 - alpha / 2, df = n - 1)
z <- rnorm(n); z <- (z - mean(z)) / sqrt(mean((z - mean(z))^2))

perm_pvalue <- function(x, y, nperm) {
  s_obs <- abs(cor(x, y))
  s_perm <- replicate(nperm, abs(cor(sample(x), y)))
  (1 + sum(s_perm >= s_obs)) / (nperm + 1)
}

par(mfrow = c(1, 2))
for (delta in c(0, 2)) {
  x <- z + if (delta > 0) delta / sqrt(n - delta^2) else 0
  rate_t <- rate_p <- numeric(length(betas))
  for (k in seq_along(betas)) {
    res <- replicate(nrep, {
      y <- beta0 + betas[k] * x + rnorm(n)
      fit <- lm(y ~ x - 1)                     # mis-specified: no intercept
      tval <- coef(summary(fit))[, "t value"]
      c(abs(tval) > tcrit, perm_pvalue(x, y, nperm) <= alpha)
    })
    rate_t[k] <- mean(res[1, ]); rate_p[k] <- mean(res[2, ])
  }
  plot(betas, rate_p, type = "b", pch = 19, col = "steelblue", ylim = c(0, 1),
       xlab = "true slope beta1", ylab = "rejection rate",
       main = sprintf("delta = %d: t-test size = %.3f", delta, rate_t[6]))
  lines(betas, rate_t, type = "b", pch = 15, lty = 2, col = "firebrick")
  abline(h = alpha, col = "gray")
  legend("topleft", c("permutation test", "t-test"), col = c("steelblue", "firebrick"),
         lty = c(1, 2), pch = c(19, 15), bty = "n")
}
