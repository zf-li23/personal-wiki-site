# Normal Q-Q plots for a normal sample, a sample with an outlier, a right-skewed sample and a heavy-tailed sample.
set.seed(0)
n <- 50
samples <- list()
samples[["Normal"]] <- rnorm(n)
samples[["Outlier"]] <- c(rnorm(n - 1), 4.5)
samples[["Right-skewed"]] <- rexp(n) * 1.5 - 1.5
samples[["Heavy tails"]] <- rt(n, df = 2.5)

op <- par(mfrow = c(1, 4))
for (name in names(samples)) {
  # qqnorm uses the plotting positions (i - 0.5) / n; qqline passes through the quartiles
  qqnorm(samples[[name]], main = name, xlab = "theoretical quantiles", ylab = "sample quantiles",
         pch = 19, cex = 0.8, col = adjustcolor("steelblue", 0.8))
  qqline(samples[[name]], col = "firebrick", lwd = 1.5)
}
par(op)
