# Golf experiment (GCBD): cell means of the 9 golfers at the 3 tee heights (5 drives each).
cellmeans <- matrix(c(143.18, 141.64, 147.40, 173.18, 176.14, 188.04,
                      141.64, 147.40, 143.18, 176.10, 178.04, 175.72,
                      204.68, 213.20, 226.26, 137.10, 148.56, 146.70,
                      171.18, 166.46, 173.14, 168.88, 187.38, 176.06,
                      227.18, 241.72, 242.04), ncol = 3, byrow = TRUE)
d <- data.frame(dist = as.vector(cellmeans),
                teehgt = factor(rep(1:3, each = 9)), id = factor(rep(1:9, 3)))
par(mfrow = c(1, 2))
with(d, interaction.plot(teehgt, id, dist, xlab = "tee height (level)",
                         ylab = "mean distance", trace.label = "golfer", bty = "L"))
d$centered <- d$dist - ave(d$dist, d$id)
with(d, interaction.plot(teehgt, id, centered, xlab = "tee height (level)",
                         ylab = "cell mean minus golfer mean", legend = FALSE, bty = "L"))
abline(h = 0, lty = 2, col = "gray")
par(mfrow = c(1, 1))
summary(aov(dist ~ id + teehgt, data = d))
