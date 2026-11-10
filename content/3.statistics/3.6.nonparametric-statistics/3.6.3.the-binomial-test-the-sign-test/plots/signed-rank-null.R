# Exact null distribution of the Wilcoxon signed-rank statistic, without and with ties.
exact_dist <- function(scores) {
  signs <- as.matrix(expand.grid(rep(list(0:1), length(scores))))
  s <- round(signs %*% scores, 6)
  table(s) / nrow(signs)
}
par(mfrow = c(1, 2))
n <- 12
d <- exact_dist(1:n)               # same as dsignrank(0:78, 12)
plot(as.numeric(names(d)), as.numeric(d), type = "h", lwd = 3, col = "steelblue",
     xlab = "S+", ylab = "probability", main = "n = 12, no ties")
curve(dnorm(x, n * (n + 1) / 4, sqrt(n * (n + 1) * (2 * n + 1) / 24)), add = TRUE, col = "red")
abline(v = 7, lty = 2)
sum(dsignrank(0:7, 12))            # P(S- <= 7) = 19/4096

d1 <- exact_dist(1:7); d2 <- exact_dist(c(2.5, 2.5, 2.5, 2.5, 6, 6, 6))
plot(as.numeric(names(d1)) - 0.15, as.numeric(d1), type = "h", lwd = 3, col = "steelblue",
     xlab = "S-", ylab = "probability", main = "n = 7, with and without ties", ylim = c(0, 0.2))
lines(as.numeric(names(d2)) + 0.15, as.numeric(d2), type = "h", lwd = 3, col = "darkorange")
legend("topright", c("no ties", "ties"), col = c("steelblue", "darkorange"), lwd = 3, bty = "n")
sum(d2[as.numeric(names(d2)) <= 5])  # 11/128
