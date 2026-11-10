# Pooled ranks of home prices in three villages, with mean ranks and the Kruskal-Wallis statistic.
HP <- c(139, 145, 171, 151, 163, 188, 197, 199, 250, 360)
V <- factor(rep(c("A", "B", "C"), times = c(3, 4, 3)))
print(kruskal.test(HP ~ V))                               # chi-squared = 6.7455, p = 0.0343
print(pairwise.wilcox.test(HP, V, p.adjust.method = "BH"))
r <- rank(HP)
stripchart(r ~ V, pch = 19, col = c("steelblue", "darkorange", "forestgreen"),
           xlab = "pooled rank", main = "Kruskal-Wallis ranks, home prices")
points(tapply(r, V, mean), 1:3, pch = "|", cex = 3)
abline(v = (length(HP) + 1) / 2, lty = 3)
