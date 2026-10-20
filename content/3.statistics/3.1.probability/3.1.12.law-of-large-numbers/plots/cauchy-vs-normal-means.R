# Running means for N(0,1) samples converge to 0; for standard Cauchy samples they do not.
set.seed(0)
n_max <- 10000
paths <- 5
n <- 1:n_max
samplers <- list("N(0, 1)" = rnorm, "standard Cauchy" = rcauchy)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))
for (name in names(samplers)) {
  means <- sapply(1:paths, function(i) cumsum(samplers[[name]](n_max)) / n)
  matplot(n, means, type = "l", lty = 1, lwd = 0.9, log = "x", ylim = c(-4, 4),
          xlab = "n (log scale)", ylab = "sample mean",
          main = paste0("running mean, ", name, " samples"))
  abline(h = 0)
}
par(op)
