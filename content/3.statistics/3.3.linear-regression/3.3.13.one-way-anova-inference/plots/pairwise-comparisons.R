# Simultaneous 95% intervals for pairwise differences of the cereal means by four methods.
sales <- c(11, 17, 16, 14, 15, 12, 10, 15, 19, 11, 23, 20, 18, 17, 27, 33, 22, 26, 28)
design <- factor(rep(1:4, times = c(5, 5, 4, 5)))

fit <- aov(sales ~ design)
print(TukeyHSD(fit, conf.level = 0.95))   # the Tukey intervals below, computed by R

r <- nlevels(design)
ni <- tapply(sales, design, length)
means <- tapply(sales, design, mean)
df <- df.residual(fit)
s <- sqrt(deviance(fit) / df)
pairs <- combn(r, 2)                      # columns (i, j) with i < j
g <- ncol(pairs)
alpha <- 0.05
crit <- c(LSD = qt(1 - alpha / 2, df),
          Bonferroni = qt(1 - alpha / (2 * g), df),
          Tukey = qtukey(1 - alpha, r, df) / sqrt(2),
          Scheffe = sqrt((r - 1) * qf(1 - alpha, r - 1, df)))

i <- pairs[1, ]; j <- pairs[2, ]
d <- means[j] - means[i]
se <- s * sqrt(1 / ni[i] + 1 / ni[j])
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")
offsets <- seq(-0.3, 0.3, length.out = length(crit))

op <- par(mar = c(5, 7, 3, 1))
plot(NA, xlim = range(d - max(crit) * se, d + max(crit) * se), ylim = c(g + 0.5, 0.5), yaxt = "n",
     xlab = "difference of means (cases sold)", ylab = "",
     main = "Pairwise comparisons: solid = excludes 0, dotted = includes 0", cex.main = 0.9)
axis(2, at = 1:g, labels = sprintf("mu%d - mu%d", j, i), las = 1)
abline(v = 0, col = "gray")
for (m in seq_along(crit)) {
  h <- crit[m] * se
  y <- 1:g + offsets[m]
  segments(d - h, y, d + h, y, col = cols[m], lwd = 2, lty = ifelse(abs(d) > h, 1, 3))
  points(d, y, pch = 19, cex = 0.6, col = cols[m])
}
legend("bottomright", bty = "n", cex = 0.8, lwd = 2, col = cols,
       legend = sprintf("%s (t_c = %.2f)", names(crit), crit))
par(op)
