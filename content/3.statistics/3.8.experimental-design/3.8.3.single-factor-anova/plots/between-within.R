# Same level means, different within-group scatter: the F statistic of two simulated experiments.
set.seed(0)
means <- c(10, 9, 12, 14, 7)
a <- length(means); n <- 10
noise <- matrix(rnorm(a * n), nrow = a)
noise <- t(apply(noise, 1, function(z) (z - mean(z)) / sd(z)))
level <- factor(rep(LETTERS[1:a], each = n))

op <- par(mfrow = c(1, 2))
for (s in c(1, 6)) {
  y <- as.vector(t(means + s * noise))
  tab <- anova(lm(y ~ level))
  boxplot(y ~ level, xlab = "level", ylab = "response",
          main = sprintf("within-group SD = %d: F0 = %.1f, p = %.2g", s, tab$`F value`[1], tab$`Pr(>F)`[1]),
          cex.main = 0.85)
  points(1:a, tapply(y, level, mean), pch = 18, col = "red", cex = 1.5)
  abline(h = mean(y), lty = 2, col = "gray")
}
par(op)
