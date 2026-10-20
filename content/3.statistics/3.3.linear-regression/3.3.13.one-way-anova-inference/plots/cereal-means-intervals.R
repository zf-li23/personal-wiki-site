# Cereal sales by package design: data with level means, and pooled versus unpooled 95% intervals.
sales <- c(11, 17, 16, 14, 15, 12, 10, 15, 19, 11, 23, 20, 18, 17, 27, 33, 22, 26, 28)
design <- factor(rep(1:4, times = c(5, 5, 4, 5)))

fit <- aov(sales ~ design)
print(summary(fit))
r <- nlevels(design)
ni <- tapply(sales, design, length)
means <- tapply(sales, design, mean)
sds <- tapply(sales, design, sd)
s <- sqrt(deviance(fit) / df.residual(fit))           # sqrt(MSE), nT - r = 15 d.f.
h_pool <- qt(0.975, df.residual(fit)) * s / sqrt(ni)
h_own <- qt(0.975, ni - 1) * sds / sqrt(ni)
ylim <- range(sales, means - h_own, means + h_own)

set.seed(0)
op <- par(mfrow = c(1, 2))
stripchart(sales ~ design, vertical = TRUE, method = "jitter", jitter = 0.08, pch = 19, col = "steelblue",
           ylim = ylim, xlab = "package design", ylab = "cases sold", main = "Data and level means")
lines(1:r, means, type = "b", pch = 18, cex = 1.6, col = "firebrick", lwd = 1.4)
legend("topleft", bty = "n", pch = 18, lty = 1, col = "firebrick", legend = "level mean")

plot(NA, xlim = c(0.5, r + 0.5), ylim = ylim, xaxt = "n", xlab = "package design", ylab = "",
     main = "95% confidence intervals for the means")
axis(1, at = 1:r)
arrows(1:r - 0.1, means - h_pool, 1:r - 0.1, means + h_pool, angle = 90, code = 3, length = 0.05,
       col = "steelblue", lwd = 1.6)
points(1:r - 0.1, means, pch = 19, col = "steelblue")
arrows(1:r + 0.1, means - h_own, 1:r + 0.1, means + h_own, angle = 90, code = 3, length = 0.05,
       col = "darkorange", lwd = 1.6)
points(1:r + 0.1, means, pch = 15, col = "darkorange")
legend("topleft", bty = "n", cex = 0.8, pch = c(19, 15), lty = 1, col = c("steelblue", "darkorange"),
       legend = c("pooled s, 15 d.f.", "own s_i, n_i - 1 d.f."))
par(op)
