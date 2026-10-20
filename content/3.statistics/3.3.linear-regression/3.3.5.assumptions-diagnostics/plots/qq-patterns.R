# Normal Q-Q plots of typical shapes: normal, light tails, heavy tails, right skew, left skew, bimodal.
set.seed(0)
n <- 60
samples <- list(
  "normal" = rnorm(n),
  "light-tailed (uniform)" = runif(n, -1, 1),
  "heavy-tailed (t, 2 df)" = rt(n, df = 2),
  "right-skewed (exponential)" = rexp(n),
  "left-skewed (minus exponential)" = -rexp(n),
  "bimodal (normal mixture)" = c(rnorm(n / 2, -2, 0.6), rnorm(n - n / 2, 2, 0.6))
)

op <- par(mfrow = c(2, 3), oma = c(0, 0, 2, 0))
for (name in names(samples)) {
  v <- samples[[name]]
  qqnorm(v, main = name, pch = 19, cex = 0.6, col = "steelblue",
         xlab = "theoretical quantile z_i", ylab = "sample quantile x_(i)")
  qqline(v, col = "firebrick", lwd = 1.3)   # line through the quartiles
}
mtext("Normal Q-Q plots (n = 60); the line passes through the quartiles", outer = TRUE, cex = 0.9)
par(op)
