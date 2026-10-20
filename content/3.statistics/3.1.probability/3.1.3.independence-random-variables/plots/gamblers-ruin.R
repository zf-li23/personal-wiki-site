# Gambler's ruin: ruin probability q(k) for total capital N = a + b, and simulated fortunes of fair games.
N <- 20
k <- 0:N
ruin <- function(p, k, N) {
  if (p == 0.5) return(1 - k / N)
  r <- (1 - p) / p
  (r^k - r^N) / (1 - r^N)
}

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))
ps <- c(0.45, 0.5, 0.55)
cols <- c("firebrick", "steelblue", "forestgreen")
plot(NA, xlim = c(0, N), ylim = c(0, 1), xlab = "initial capital k (N = a + b = 20)",
     ylab = "ruin probability q(k)", main = "Ruin probability")
for (j in seq_along(ps)) lines(k, ruin(ps[j], k, N), type = "o", pch = 19, cex = 0.5, col = cols[j])
legend("topright", bty = "n", lty = 1, pch = 19, col = cols, legend = paste("p =", ps))

set.seed(0)
a <- 10
walks <- lapply(1:8, function(i) {
  x <- a
  while (x[length(x)] > 0 && x[length(x)] < N) {
    x <- c(x, x[length(x)] + sample(c(-1, 1), 1))
  }
  x
})
plot(NA, xlim = c(0, max(lengths(walks)) - 1), ylim = c(0, N), xlab = "round n",
     ylab = "fortune X_n", main = "Eight fair games from a = 10, stopped at 0 or 20", cex.main = 0.9)
for (i in seq_along(walks)) lines(seq_along(walks[[i]]) - 1, walks[[i]], col = i)
abline(h = 0)
abline(h = N, lty = 2)
par(op)
