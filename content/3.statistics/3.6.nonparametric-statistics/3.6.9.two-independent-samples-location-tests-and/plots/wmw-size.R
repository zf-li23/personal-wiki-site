# Rejection rates under equal medians but unequal spreads: WMW, Welch t and Brunner-Munzel tests.
# The Brunner-Munzel statistic is computed directly (lawstat::brunner.munzel.test gives the same).
bm_test <- function(x, y) {
  n1 <- length(x); n2 <- length(y); N <- n1 + n2
  r <- rank(c(x, y)); r1 <- r[1:n1]; r2 <- r[-(1:n1)]
  s1 <- var(r1 - rank(x)); s2 <- var(r2 - rank(y))
  stat <- n1 * n2 * (mean(r2) - mean(r1)) / (N * sqrt(n1 * s1 + n2 * s2))
  df <- (n1 * s1 + n2 * s2)^2 / ((n1 * s1)^2 / (n1 - 1) + (n2 * s2)^2 / (n2 - 1))
  2 * pt(-abs(stat), df)
}
set.seed(0)
reps <- 2000; ratios <- c(1, 1.5, 2, 3, 4)
for (d in list(c(10, 30), c(30, 10))) {
  res <- sapply(ratios, function(s) {
    p <- replicate(reps, {
      x <- rnorm(d[1], 0, s); y <- rnorm(d[2])
      c(wilcox.test(x, y)$p.value, t.test(x, y)$p.value, bm_test(x, y))
    })
    rowMeans(p < 0.05)
  })
  dimnames(res) <- list(c("WMW", "Welch t", "Brunner-Munzel"), paste0("sd=", ratios))
  cat("n1 =", d[1], " n2 =", d[2], "\n"); print(round(res, 3))
}
