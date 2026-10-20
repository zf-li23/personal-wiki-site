# Sample mean versus sample range: independent for normal samples (Basu), dependent for exponential samples.
set.seed(0)
n <- 10
reps <- 3000
samples <- list(
  "N(0, 1) samples" = matrix(rnorm(reps * n), reps, n),
  "Exp(1) samples" = matrix(rexp(reps * n), reps, n)
)

op <- par(mfrow = c(1, 2))
for (name in names(samples)) {
  data <- samples[[name]]
  m <- rowMeans(data)
  r <- apply(data, 1, max) - apply(data, 1, min)
  plot(m, r, pch = 16, cex = 0.4, col = adjustcolor("steelblue", 0.35),
       xlab = "sample mean", ylab = "sample range",
       main = sprintf("%s, n = %d: correlation %.2f", name, n, cor(m, r)))
}
par(op)
