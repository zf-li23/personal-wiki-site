# Simulated power of the sign, Wilcoxon signed-rank and t tests (n = 20, one-sided, level 0.05)
# for normal data and for t_3 data scaled to unit variance. Here the tests are not randomized,
# so the discrete sign and Wilcoxon tests have actual levels slightly below 0.05.
set.seed(0)
n <- 20; reps <- 4000; shifts <- seq(0, 1, by = 0.1)
power_at <- function(rdist, theta) {
  rej <- replicate(reps, {
    z <- rdist(n) + theta
    c(sign = binom.test(sum(z > 0), n, alternative = "greater")$p.value < 0.05,
      wilcoxon = wilcox.test(z, alternative = "greater")$p.value < 0.05,
      t = t.test(z, alternative = "greater")$p.value < 0.05)
  })
  rowMeans(rej)
}
op <- par(mfrow = c(1, 2))
for (case in c("normal", "t3")) {
  rdist <- if (case == "normal") rnorm else function(m) rt(m, df = 3) / sqrt(3)
  pw <- t(sapply(shifts, function(th) power_at(rdist, th)))
  matplot(shifts, pw, type = "b", pch = 19, lty = 1, col = c("steelblue", "darkorange", "forestgreen"),
          xlab = "shift theta (in standard deviations)", ylab = "power", main = case)
  abline(h = 0.05, lty = 3)
}
legend("topleft", c("sign", "Wilcoxon", "t"), col = c("steelblue", "darkorange", "forestgreen"), pch = 19, bty = "n")
par(op)
